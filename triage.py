#!/usr/bin/env python3
"""Omarchy PR triage via TypeSafe Jev.

Groups observed open PRs of omacom/omarchy into review candidates, proposes
related groups, and flags items that may need follow-up — supporting the roll-up work DHH
asked the triage team to do (x.com/dhh/status/2098755120540393908).

Judgments come from TypeSafe's System One API (Jev). Code owns the workflow:
fetch -> judge (one batched call per PR) -> compare candidate pairs -> cluster.

Usage:
  python3 triage.py fetch              # refresh data/pages/snapshot.json
  python3 triage.py judge [--limit N] [--resume]
  python3 triage.py dupes [--max-pairs N]
  python3 triage.py cluster            # writes out/clusters.json, out/dupes.json,
                                       #            out/tranches.md, out/summary.json
  python3 triage.py all [--limit N]
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import math
import os
import random
import re
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "data" / "pages"
OUT_DIR = ROOT / "out"
JUDGMENTS_PATH = OUT_DIR / "judgments.jsonl"
PAIRS_PATH = OUT_DIR / "pair_verdicts.jsonl"
KEY_FILE = Path.home() / "Documents" / "jevapi.txt"

API_URL = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-latest"
REPO = "omacom/omarchy"
BODY_CHARS = 1200
WORKERS = 6
BINDING_VERSION = 1


def digest(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, allow_nan=False)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

# ---------------------------------------------------------------------------
# Jev questions — one batched call per PR (independent questions over one state
# run in parallel and are far cheaper than one call per question).
# ---------------------------------------------------------------------------

def judge_questions() -> dict:
    return {
        "category": {
            "type": "choice",
            "instructions": {
                "question": (
                    "Which area of Omarchy does this pull request mainly touch? "
                    "Read `pr.title` and `pr.body`; `pr.diffstat` shows the size. "
                    "Pick exactly one; use `unclear` only when the text is too thin to tell."
                )
            },
            "criteria": {
                "install-setup": "omarchy-setup menu, installer, first boot, ISO, dotfiles bootstrap",
                "desktop-config": "Hyprland, Walker, waybar, wlogout, mako, keybinds, wallpapers, theming",
                "shell-cli": "zsh config, aliases, starship, CLI tool defaults, terminal usage",
                "apps-integrations": "default apps, mime handling, new application integrations (e.g. dropbox, spotify, 1password)",
                "hardware-drivers": "NVIDIA, wifi, bluetooth, audio, power, HiDPI, laptops, ARM/Snapdragon, firmware",
                "update-release": "omarchy-update, version bumps, release machinery, migration between versions, boot entries",
                "agents-ai": "AI coding agents, agent hooks, MCP, integrations for Claude/Codex/Gemini-like tools",
                "docs": "README, documentation, wiki, help text only",
                "fix-misc": "a real change that fits none of the above",
                "unclear": "cannot be placed from title and body alone",
            },
        },
        "risk": {
            "type": "score",
            "instructions": {
                "question": (
                    "How risky is merging this pull request for existing Omarchy installations? "
                    "Judge from `pr.title`, `pr.body` and `pr.diffstat`."
                )
            },
            "criteria": [
                "Text-only: docs, themes, wallpapers, menu definitions; nothing executes",
                "Config or script change that is scoped and revertible; no root-side effects at install/update time",
                "Runs as root during install or update, edits boot entries or mounts, or flips system-wide defaults",
                "Touches disk layout, networking, sudo/permissions, security posture, or kernel drivers/firmware",
                "Could break existing installs outright: data loss, boot failure, or user lockout",
            ],
        },
        "is_fix": {
            "type": "noul",
            "instructions": (
                "Is this pull request primarily a fix for a bug or regression, rather than "
                "a new feature, a default/taste change, or a refactor? Judge from `pr.title` and `pr.body`."
            ),
        },
        "dupe_signal": {
            "type": "noul",
            "instructions": (
                "Do `pr.title` or `pr.body` indicate this pull request duplicates another change, "
                "or is superseded by / supersedes one (another open PR, or already-merged upstream work)?"
            ),
        },
        "finished_form": {
            "type": "score",
            "instructions": {
                "question": (
                    "Is this pull request in finished, reviewable form as described by `pr.body` "
                    "(with `pr.title`)? DHH asked the triage team to ensure everything is ready "
                    "for consideration in a finished form."
                )
            },
            "criteria": [
                "Empty or near-empty body; no description of what or why",
                "Says what it does but not why, or shows no evidence it was tried",
                "Clear what and why; states that it was tested on a real system",
                "Clear what and why plus concrete QA evidence (before/after, screenshots, test steps); small and focused",
            ],
        },
        "review_effort": {
            "type": "score",
            "instructions": {
                "question": "How much reviewer effort does this pull request need, judging by `pr.diffstat` and the change described?"
            },
            "criteria": [
                "Trivial and mechanical: a typo, version number, or one-line constant",
                "Small: one focused change a reviewer can hold in their head",
                "Moderate: several related edits that must be checked together",
                "Substantial: architectural or many-part change needing deep review",
            ],
        },
        "security_flag": {
            "type": "noul",
            "instructions": (
                "Does this change touch credentials or secrets, download-and-execute remote code, "
                "sudo/permission changes, network exposure, or crypto material? Judge from `pr.title` and `pr.body`."
            ),
        },
    }


def pair_questions() -> dict:
    return {
        "sameness": {
            "type": "choice",
            "instructions": {
                "question": (
                    "Do `pr_a` and `pr_b` propose the same underlying change to Omarchy? "
                    "Judge by what they modify and the outcome, not by wording."
                )
            },
            "criteria": {
                "same_change": "two attempts at the same change; merging one makes the other redundant",
                "related_but_different": "same area or theme but distinct outcomes; both could merge",
                "unrelated": "different changes that merely share words",
            },
        },
    }


# ---------------------------------------------------------------------------
# TypeSafe HTTP
# ---------------------------------------------------------------------------

class TriageFatal(RuntimeError):
    pass


def read_key() -> str:
    key = os.environ.get("TYPESAFE_API_KEY")
    if key:
        return key.strip()
    if KEY_FILE.exists():
        return KEY_FILE.read_text().strip()
    raise TriageFatal(f"No API key: set TYPESAFE_API_KEY or create {KEY_FILE}")


def ask(state, questions: dict, key: str, timeout: int = 90) -> dict:
    payload = json.dumps({"state": state, "model": MODEL, "questions": questions}).encode()
    backoff = 2.0
    last = ""
    for _attempt in range(6):
        req = urllib.request.Request(
            API_URL,
            data=payload,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode(errors='replace')[:300]}"
            if e.code == 401:
                raise TriageFatal(f"Auth rejected (401). Check the key. {last}") from e
            if e.code == 422:
                raise TriageFatal(f"Request rejected (422) — question shape bug. {last}") from e
            if e.code in (429, 529) or e.code >= 500:
                time.sleep(backoff + random.random())
                backoff = min(backoff * 2, 60)
                continue
            raise TriageFatal(last) from e
        except urllib.error.URLError as e:
            last = f"network: {e}"
            time.sleep(backoff + random.random())
            backoff = min(backoff * 2, 60)
    raise TriageFatal(f"Retries exhausted. Last error: {last}")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def validate_pr(item):
    if (not isinstance(item, dict) or type(item.get("number")) is not int
            or item["number"] <= 0 or not isinstance(item.get("title"), str)
            or item.get("body") is not None and not isinstance(item["body"], str)):
        raise TriageFatal("Invalid captured PR shape; fetch again")
    for field in ("head", "user", "author"):
        if item.get(field) is not None and not isinstance(item[field], dict):
            raise TriageFatal(f"Invalid captured PR {field}; fetch again")
    labels = item.get("labels", [])
    if not isinstance(labels, list) or any(not isinstance(label, dict) or not isinstance(label.get("name"), str) for label in labels):
        raise TriageFatal("Invalid captured PR labels; fetch again")


def load_prs() -> dict[int, dict]:
    prs: dict[int, dict] = {}
    snapshot = PAGES_DIR / "snapshot.json"
    if snapshot.exists():
        value = json.loads(snapshot.read_text())
        if (not isinstance(value, dict) or type(value.get("version")) is not int
                or value.get("version") != 1 or value.get("repo") != REPO
                or value.get("digest") != digest(value.get("items"))):
            raise TriageFatal("Fetched snapshot identity or checksum differs; fetch again")
        pages = [value["items"]]
    else:
        # Existing/enriched page caches remain readable until the next fetch.
        pages = [json.loads(path.read_text()) for path in sorted(PAGES_DIR.glob("page_*.json"))]
    for page in pages:
        if not isinstance(page, list):
            raise TriageFatal("Captured PR membership must be a list; fetch again")
        for p in page:
            validate_pr(p)
            if p["number"] in prs:
                raise TriageFatal("Repeated PR in captured membership; fetch again")
            raw_body = p.get("body") or ""
            refs = sorted({int(x) for x in re.findall(r"#(\d{2,6})", raw_body)})
            body = re.sub(r"<!--.*?-->", "", raw_body, flags=re.S)
            body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)  # images
            body = re.sub(r"https?://\S+", "", body)          # bare links
            body = re.sub(r"\s+", " ", body).strip()
            prs[p["number"]] = {
                "number": p["number"],
                "title": p["title"].strip(),
                "body": body[:BODY_CHARS],
                "author": ((p.get("user") or p.get("author") or {}).get("login", "unknown")),
                "created": p.get("created_at", ""),
                "updated": p.get("updated_at", ""),
                "draft": bool(p.get("draft")),
                "files": p.get("changed_files"),
                "additions": p.get("additions"),
                "deletions": p.get("deletions"),
                "labels": [label["name"] for label in p.get("labels", [])],
                "refs": refs,
                "head_sha": (p.get("head") or {}).get("sha"),
                "url": p.get("html_url") or f"https://github.com/{REPO}/pull/{p['number']}",
                "source_digest": digest(p),
                "body_truncated": len(body) > BODY_CHARS,
            }
    return prs


def pr_state(pr: dict) -> dict:
    sizes = [pr[key] for key in ("files", "additions", "deletions")]
    known = all(type(size) is int and size >= 0 for size in sizes)
    return {
        "pr": {
            "title": pr["title"],
            "body": pr["body"] or "(empty body)",
            "author": pr["author"],
            "diffstat": f"{sizes[0]} files changed, +{sizes[1]}/-{sizes[2]}" if known else "unknown (not supplied by the captured PR list)",
            "draft": pr["draft"],
            "evidence_basis": "title and shortened description; patches, CI and reproduction results not verified",
            "diffstat_available": known,
            "body_truncated": pr["body_truncated"],
        }
    }


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_fetch(args) -> None:
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    page, total = 1, 0
    captured = []
    seen = set()
    while True:
        url = f"https://api.github.com/repos/{REPO}/pulls?state=open&per_page=100&page={page}"
        if getattr(args, "transport", "urllib") == "curl":
            # Keep the Makefile's workaround for hosts with broken urllib IPv6.
            result = subprocess.run(["curl", "--fail", "--silent", "--show-error",
                                     "--max-time", "60", url], capture_output=True, text=True)
            if result.returncode:
                raise TriageFatal("curl fetch failed; previous snapshot retained")
            arr = json.loads(result.stdout)
        else:
            with urllib.request.urlopen(url, timeout=60) as r:
                arr = json.load(r)
        if not isinstance(arr, list):
            raise TriageFatal("GitHub did not return a PR list; previous snapshot retained")
        if not arr:
            break
        for item in arr:
            validate_pr(item)
            if item["number"] in seen:
                raise TriageFatal("Invalid or repeated PR during pagination; previous snapshot retained")
            seen.add(item["number"])
        captured.extend(arr)
        total += len(arr)
        print(f"page {page}: {len(arr)} PRs (total {total})")
        if len(arr) < 100:
            break
        page += 1
        time.sleep(0.4)
    # One atomic membership commit, including an empty or exact-page result.
    # Failed/partial fetches leave the last committed observation untouched.
    atomic_json(PAGES_DIR / "snapshot.json", {
        "version": 1, "repo": REPO, "items": captured, "digest": digest(captured),
        "observed_at": datetime.now(timezone.utc).isoformat(),
    })
    print(f"fetched {total} observed open PRs into {PAGES_DIR}")


def finite_json(value):
    """Keep evidence JSON-shaped while removing non-standard numeric constants."""
    if isinstance(value, dict):
        return {key: finite_json(item) for key, item in value.items()}
    if isinstance(value, list):
        return [finite_json(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def normalized_record(record):
    record = {key: finite_json(value) for key, value in record.items()}
    usage = record.get("usage")
    usage = usage if isinstance(usage, dict) else {}
    record["usage"] = {field: usage.get(field) if type(usage.get(field)) is int
                       and usage[field] >= 0 else 0
                       for field in ("input_tokens", "output_tokens")}
    return record


def normalize_pair(record):
    record = normalized_record(record)
    choices = pair_questions()["sameness"]["criteria"]
    verdict = record.get("verdict")
    if not isinstance(verdict, str) or verdict not in choices:
        record["verdict"] = None
    probabilities = record.get("probabilities")
    probabilities = dict(probabilities) if isinstance(probabilities, dict) else {}
    for key, value in probabilities.items():
        if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1:
            probabilities[key] = None
    record["probabilities"] = probabilities
    probabilities["same_change"] = p_same(record)
    record["normalization_errors"] = [field + ": invalid or missing" for field, value in
        (("verdict", record.get("verdict")), ("probabilities.same_change", p_same(record)))
        if value is None]
    return record


def reusable_pair(record):
    return record.get("verdict") is not None and p_same(record) is not None


def normalize_judgment(record):
    record = normalized_record(record)
    data = record.get("answers")
    data = data if isinstance(data, dict) else {}
    record["answers"] = data
    errors = []
    for name, question in judge_questions().items():
        answer = data.get(name)
        answer = dict(answer) if isinstance(answer, dict) else {}
        field = {"choice": "choice", "score": "score", "noul": "noul"}[question["type"]]
        if field == "choice":
            value = answer.get(field)
            valid = isinstance(value, str) and value in question["criteria"]
        else:
            value = metric(record, name, field)
            valid = value is not None
        if not valid:
            errors.append(f"answers.{name}.{field}: invalid or missing")
            value = None
        answer[field] = value
        data[name] = answer
    record["normalization_errors"] = errors
    return record


def reusable_judgment(record):
    return (record["answers"]["category"]["choice"] is not None
            and all(metric(record, name, field) is not None for name, field in (
                ("risk", "score"), ("finished_form", "score"), ("review_effort", "score"),
                ("is_fix", "noul"), ("security_flag", "noul"))))


def load_done() -> dict[int, dict]:
    done: dict[int, dict] = {}
    if JUDGMENTS_PATH.exists():
        for line in JUDGMENTS_PATH.read_text().splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (isinstance(rec, dict) and "error" not in rec
                    and type(rec.get("number")) is int and rec["number"] > 0):
                done[rec["number"]] = normalize_judgment(rec)
    return done


def judgment_binding(pr):
    return digest({"version": BINDING_VERSION, "repo": REPO,
                   "source": pr["source_digest"], "state": pr_state(pr),
                   "questions": judge_questions(), "model": MODEL})


def current_judgments(prs, *, allow_unbound=False):
    current = {}
    for number, record in load_done().items():
        if number not in prs:
            continue
        matches = record.get("binding") == judgment_binding(prs[number])
        legacy = "binding" not in record and allow_unbound
        if matches or legacy:
            current[number] = dict(record, freshness="current" if matches else "unbound")
    return current


def brief(pr):
    return {"number": pr["number"], "title": pr["title"], "body": pr["body"][:400],
            "evidence_basis": "shortened descriptions only; source equivalence not verified"}


def pair_binding(prs, a, b):
    a, b = sorted((a, b))
    return digest({"version": BINDING_VERSION, "repo": REPO, "model": MODEL,
                   "sources": [prs[a]["source_digest"], prs[b]["source_digest"]],
                   "state": [brief(prs[a]), brief(prs[b])], "questions": pair_questions()})


def current_pairs(prs, judgments, *, allow_unbound=False):
    pairs = {}
    if PAIRS_PATH.exists():
        for line in PAIRS_PATH.read_text().splitlines():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (not isinstance(record, dict) or "error" in record
                    or any(type(record.get(key)) is not int or record[key] <= 0 for key in ("a", "b"))):
                continue
            a, b = sorted((record["a"], record["b"]))
            if a == b or a not in judgments or b not in judgments:
                continue
            matches = record.get("binding") == pair_binding(prs, a, b)
            legacy = "binding" not in record and allow_unbound
            if matches or legacy:
                record = normalize_pair(record)
                pairs[a, b] = dict(record, a=a, b=b, freshness="current" if matches else "unbound")
    return list(pairs.values())


def cmd_judge(args) -> None:
    prs = load_prs()
    done = {n: rec for n, rec in current_judgments(prs).items()
            if reusable_judgment(rec)} if args.resume else {}
    if not args.resume:
        JUDGMENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        JUDGMENTS_PATH.write_text("")
    JUDGMENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    todo = [n for n in sorted(prs, reverse=True) if n not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(prs)} PRs, {len(done)} already judged, {len(todo)} to go")
    if not todo:
        return
    key = read_key()
    lock = threading.Lock()
    errors: list[str] = []
    tokens_in = tokens_out = 0

    def work(number: int) -> None:
        nonlocal tokens_in, tokens_out
        pr = prs[number]
        try:
            resp = ask(pr_state(pr), judge_questions(), key)
            if not isinstance(resp, dict):
                resp = {}
            rec = {"number": number, "title": pr["title"], "answers": resp.get("answers"), "usage": resp.get("usage", {}),
                   "binding": judgment_binding(pr), "input": pr_state(pr),
                   "source_digest": pr["source_digest"], "head_sha": pr["head_sha"],
                   "updated_at": pr["updated"], "requested_model": MODEL,
                   "judged_at": datetime.now(timezone.utc).isoformat(),
                   "resolved_model": resp.get("model"), "request_id": resp.get("request_id")}
        except TriageFatal as e:
            with lock:
                errors.append(f"#{number}: {e}")
            if "401" in str(e):
                raise
            return
        rec = normalize_judgment(rec)
        with lock:
            with JUDGMENTS_PATH.open("a") as f:
                f.write(json.dumps(rec, allow_nan=False) + "\n")
            tokens_in += rec["usage"]["input_tokens"]
            tokens_out += rec["usage"]["output_tokens"]
            n = len(done) + 1
            done[number] = rec
            if n % 25 == 0:
                print(f"judged {n}/{len(todo)}  (in {tokens_in} tok / out {tokens_out} tok)")

    try:
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            futures = [ex.submit(work, n) for n in todo]
            for f in as_completed(futures):
                f.result()
    except TriageFatal as e:
        print(f"FATAL: {e}", file=sys.stderr)
        print("partial progress is saved; re-run with --resume", file=sys.stderr)
        sys.exit(2)

    print(f"done: {len(done)} matching judgments; errors: {len(errors)}")
    for e in errors[:10]:
        print("  " + e)
    print(f"tokens: in={tokens_in} out={tokens_out}")


def load_judgments() -> dict[int, dict]:
    return load_done()


def lexical_pairs(prs, judgments, threshold=0.72, jaccard_threshold=0.62) -> list[tuple[float, int, int]]:
    """Candidate duplicate pairs: high title similarity within the same judged category."""

    def toks(s):
        return set(re.findall(r"[a-z0-9]+", s.lower())) - {
            "the", "a", "an", "and", "or", "to", "of", "for", "in", "on", "with", "fix", "add",
        }

    by_cat: dict[str, list[int]] = defaultdict(list)
    for n, j in judgments.items():
        cat = category(j)
        by_cat[cat].append(n)
    pairs = []
    for nums in by_cat.values():
        nums = sorted(nums)
        for i, a in enumerate(nums):
            ta = prs[a]["title"].lower()
            for b in nums[i + 1:]:
                tb = prs[b]["title"].lower()
                ratio = difflib.SequenceMatcher(None, ta, tb).ratio()
                if ratio >= threshold:
                    pairs.append((ratio, a, b))
                    continue
                A, B = toks(prs[a]["title"]), toks(prs[b]["title"])
                if A and B:
                    jac = len(A & B) / len(A | B)
                    if jac >= jaccard_threshold:
                        pairs.append((jac, a, b))
    pairs.sort(reverse=True)
    seen = {(a, b) for _, a, b in pairs}
    # Cross-referenced PRs (body cites each other) are candidate duplicates even
    # when titles differ — e.g. fixes to the same bug split across files.
    for n, pr in prs.items():
        if n not in judgments:
            continue
        for r in pr.get("refs", []):
            a, b = min(n, r), max(n, r)
            if a in prs and b in prs and a in judgments and b in judgments and (a, b) not in seen:
                seen.add((a, b))
                pairs.append((1.0, a, b))
    pairs.sort(key=lambda t: -t[0])
    return pairs


def cmd_dupes(args) -> None:
    prs = load_prs()
    judgments = current_judgments(prs)
    missing = len(prs) - len(judgments)
    if missing > 100:
        print(f"warning: {missing} PRs not judged yet; dupe pass runs on judged subset", file=sys.stderr)
    done_pairs = {(rec["a"], rec["b"]) for rec in current_pairs(prs, judgments)
                  if reusable_pair(rec)}
    pairs = [(s, a, b) for s, a, b in lexical_pairs(prs, judgments) if (a, b) not in done_pairs]
    pairs = pairs[: args.max_pairs]
    print(f"{len(pairs)} candidate pairs to compare (skipping {len(done_pairs)} matching records)")
    if not pairs:
        return
    PAIRS_PATH.parent.mkdir(parents=True, exist_ok=True)
    key = read_key()
    lock = threading.Lock()

    def work(item):
        s, a, b = item
        if a not in prs or b not in prs:
            return  # candidate became stale (PR closed and refetched mid-run)
        resp = ask({"pr_a": brief(prs[a]), "pr_b": brief(prs[b])}, pair_questions(), key)
        resp = resp if isinstance(resp, dict) else {}
        data = resp.get("answers")
        data = data if isinstance(data, dict) else {}
        answer = data.get("sameness")
        answer = answer if isinstance(answer, dict) else {}
        rec = {
            "a": a, "b": b, "similarity": round(s, 3),
            "verdict": answer.get("choice"),
            "probabilities": answer.get("probabilities"),
            "usage": resp.get("usage", {}),
            "binding": pair_binding(prs, a, b),
            "requested_model": MODEL, "resolved_model": resp.get("model"),
            "request_id": resp.get("request_id"),
            "judged_at": datetime.now(timezone.utc).isoformat(),
            "input": {"pr_a": brief(prs[a]), "pr_b": brief(prs[b])},
        }
        rec = normalize_pair(rec)
        with lock:
            with PAIRS_PATH.open("a") as f:
                f.write(json.dumps(rec, allow_nan=False) + "\n")

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(work, it) for it in pairs]
        for i, f in enumerate(as_completed(futures)):
            f.result()
            if (i + 1) % 25 == 0:
                print(f"compared {i + 1}/{len(pairs)}")
    print("candidate pair comparison complete")


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def metric(judgment, name, field="score"):
    """Absent, non-finite or out-of-range model values are unknown, never zero."""
    answer = (judgment.get("answers") or {}).get(name)
    value = answer.get(field) if isinstance(answer, dict) else None
    ceiling = 1 if field == "noul" else (4 if name == "risk" else 3)
    if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= ceiling:
        return None
    return value


def category(judgment):
    answer = (judgment.get("answers") or {}).get("category")
    value = answer.get("choice") if isinstance(answer, dict) else None
    return value if isinstance(value, str) and value in judge_questions()["category"]["criteria"] else "unclear"


def p_same(pair):
    probabilities = pair.get("probabilities")
    value = probabilities.get("same_change") if isinstance(probabilities, dict) else None
    return value if type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1 else None


def pair_classification(pair):
    """Separate genuine contradictions from the human-review threshold band."""
    probability = p_same(pair)
    verdict = pair.get("verdict")
    if probability is None or verdict not in ("same_change", "related_but_different", "unrelated"):
        return "malformed"
    if verdict == "same_change":
        return "same" if probability >= 0.65 else ("contradictory" if probability < 0.35 else "uncertain")
    return "different" if probability < 0.35 else ("contradictory" if probability >= 0.65 else "uncertain")


def accepted_pair(pair):
    return pair_classification(pair) == "same"


def duplicate_groups(verdicts):
    """Connectivity proposes groups; every internal relationship remains visible."""
    dsu = DSU()
    indexed = {(v["a"], v["b"]): v for v in verdicts}
    for v in verdicts:
        if accepted_pair(v):
            dsu.union(v["a"], v["b"])
    connected = defaultdict(list)
    for number in sorted(dsu.parent):
        connected[dsu.find(number)].append(number)
    consistent, review = [], []
    for members in sorted(connected.values(), key=lambda g: (-len(g), g)):
        if len(members) < 2:
            continue
        conflicts, uncertain, missing = [], [], []
        unbound = False
        for a, b in combinations(members, 2):
            pair = indexed.get((a, b))
            if pair is None:
                missing.append([a, b])
                continue
            unbound |= pair.get("freshness") != "current"
            if accepted_pair(pair):
                continue
            classification = pair_classification(pair)
            diagnostic = {"a": a, "b": b, "verdict": pair.get("verdict"),
                          "p_same": p_same(pair), "classification": classification}
            # Strong difference evidence conflicts with the proposed group;
            # a self-contradictory model response also requires relationship review.
            if classification in ("different", "contradictory"):
                conflicts.append(diagnostic)
            else:
                uncertain.append(diagnostic)
        if conflicts or uncertain or missing or unbound:
            review.append({"members": members, "conflicting_pairs": conflicts,
                           "uncertain_pairs": uncertain, "missing_pairs": missing,
                           "unbound_evidence": unbound})
        else:
            consistent.append(members)
    return consistent, review


def review_candidate(pr, judgment, grouped):
    required = [metric(judgment, "risk"), metric(judgment, "finished_form"),
                metric(judgment, "is_fix", "noul"), metric(judgment, "security_flag", "noul"),
                metric(judgment, "review_effort")]
    if (judgment.get("freshness") != "current" or not reusable_judgment(judgment) or pr["draft"]
            or pr["number"] in grouped or any(value is None for value in required)):
        return False
    risk, finished, fix, security, _ = required
    return risk <= 1.5 and finished >= 1.8 and fix >= 0.6 and security < 0.5


def escalated(judgment):
    risk, security = metric(judgment, "risk"), metric(judgment, "security_flag", "noul")
    return (risk is not None and risk >= 3) or (security is not None and security >= 0.5)


def report_binding(prs, judgments, verdicts):
    return digest({"version": BINDING_VERSION, "repo": REPO,
                   "sources": {n: pr["source_digest"] for n, pr in prs.items()},
                   "judgments": judgments, "pairs": verdicts,
                   "questions": [judge_questions(), pair_questions()], "model": MODEL})


def cmd_cluster(args) -> None:
    prs = load_prs()
    allow_unbound = getattr(args, "allow_unbound", False)
    judgments = current_judgments(prs, allow_unbound=allow_unbound)
    verdicts = current_pairs(prs, judgments, allow_unbound=allow_unbound)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dupe_groups, review_groups = duplicate_groups(verdicts)
    in_group = {n for g in dupe_groups for n in g} | {n for g in review_groups for n in g["members"]}
    uncertain_pairs = [{"a": v["a"], "b": v["b"], "p_same": p_same(v),
                        "similarity": v.get("similarity"), "verdict": v.get("verdict"),
                        "classification": pair_classification(v)}
                       for v in verdicts if pair_classification(v) in
                       ("uncertain", "contradictory", "malformed")]
    uncertain_pairs.sort(key=lambda v: -(v["p_same"] if v["p_same"] is not None else -1))

    clusters = {}
    tranches = defaultdict(list)
    follow_up, escalate = [], []
    for n, j in sorted(judgments.items()):
        risk = metric(j, "risk")
        band = "unknown" if risk is None else ("low" if risk <= 1.5 else ("core" if risk <= 2.5 else "danger"))
        cat = category(j)
        item = {"number": n, "title": prs[n]["title"], "author": prs[n]["author"],
                "risk": risk, "finished_form": metric(j, "finished_form"),
                "is_fix": metric(j, "is_fix", "noul"), "review_effort": metric(j, "review_effort"),
                "security_flag": metric(j, "security_flag", "noul"), "freshness": j["freshness"],
                "superseded_by": None, "source_digest": prs[n]["source_digest"],
                "head_sha": prs[n]["head_sha"], "url": prs[n]["url"]}
        clusters.setdefault(cat, {}).setdefault(band, []).append(item)
        if review_candidate(prs[n], j, in_group):
            tranches[cat].append(item)
        finished = metric(j, "finished_form")
        if finished is not None and finished <= 1 and n not in in_group:
            follow_up.append(n)
        if escalated(j):
            escalate.append(n)
    tokens = Counter()
    for record in [*judgments.values(), *verdicts]:
        for field in ("input_tokens", "output_tokens"):
            value = record.get("usage", {}).get(field)
            if type(value) is int and value >= 0:
                tokens[field] += value

    dupes = {"confirmed_groups": dupe_groups, "review_groups": review_groups,
             "uncertain_pairs": uncertain_pairs,
             "meaning": "Model-consistent candidate groups, not verified duplicates. No survivor selected."}
    summary = {
        "format_version": 2, "repo": REPO, "prs_in_corpus": len(prs), "judged": len(judgments),
        "unjudged_or_stale": len(prs) - len(judgments),
        "unbound_judgments": sum(j["freshness"] == "unbound" for j in judgments.values()),
        "allow_unbound": allow_unbound, "report_binding": report_binding(prs, judgments, verdicts),
        "dupe_groups": len(dupe_groups), "review_groups": len(review_groups),
        "uncertain_pairs": len(uncertain_pairs), "prs_in_dupe_groups": len(in_group),
        "superseded": 0, "ready_tranches": len(tranches),
        "ready_prs": sum(map(len, tranches.values())),
        "recommendation_kind": "review-candidates", "needs_author_followup": len(follow_up),
        "escalate_review": len(escalate),
        "unknown_risk_or_security": sum(metric(j, "risk") is None or metric(j, "security_flag", "noul") is None
                                        for j in judgments.values()),
        "tokens": {"input": tokens["input_tokens"], "output": tokens["output_tokens"]},
        "output_digests": {"clusters.json": digest(clusters), "dupes.json": digest(dupes)},
    }
    atomic_json(OUT_DIR / "clusters.json", clusters)
    atomic_json(OUT_DIR / "dupes.json", dupes)
    lines = [
        "# Omarchy PR review candidates — Jev triage", "",
        f"Corpus: {len(prs)} observed open PRs; {len(judgments)} matching judgments; "
        f"{summary['unjudged_or_stale']} unjudged/stale; {summary['unbound_judgments']} unbound legacy judgments.",
        f"Review candidates: {summary['ready_prs']}. Model-consistent groups: {len(dupe_groups)}. "
        f"Groups needing relationship review: {len(review_groups)}.", "",
        "Evidence: titles and shortened descriptions (1200 characters per PR; 400 per pair). "
        "Diffstat is unknown unless captured input supplies it. Patches, CI, reproductions, "
        "fix coverage and security have not been verified. Model scores are suggestions, "
        "not calibrated guarantees or approval to merge/close. Pagination records an observation, not a point-in-time GitHub snapshot.", "",
    ]
    if allow_unbound:
        lines += ["LEGACY INSPECTION: unbound judgments cannot establish freshness or enter review-candidate tranches.", ""]
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    for cat, candidates in sorted(tranches.items(), key=lambda t: -len(t[1])):
        lines += [f"## Review candidates: {cat} — {len(candidates)} PRs", "",
                  "| PR | Title | Author | Model finished | Model effort | Model fix |",
                  "|---|---|---|---|---|---|"]
        for it in candidates:
            lines.append(f"| [#{it['number']}]({it['url']}) | {cell(it['title'][:80])} | {cell(it['author'])} | "
                         f"{it['finished_form']:.1f} | {it['review_effort']:.1f} | {it['is_fix']:.2f} |")
        lines.append("")
    for label, groups in (("Model-consistent candidate groups — verify fix coverage; no survivor selected", dupe_groups),
                          ("Candidate groups needing relationship review", review_groups)):
        if groups:
            lines += [f"## {label}", ""]
            for group in groups:
                members = group if isinstance(group, list) else group["members"]
                lines.append("- " + ", ".join(f"#{n}" for n in members))
                if isinstance(group, dict):
                    for field in ("conflicting_pairs", "uncertain_pairs", "missing_pairs"):
                        if group[field]:
                            lines.append(f"  - {field}: {json.dumps(group[field])}")
                    if group["unbound_evidence"]:
                        lines.append("  - Unbound legacy evidence; revisions cannot be checked.")
            lines.append("")
    if uncertain_pairs:
        lines += ["## Uncertain pairs — human comparison needed", ""]
        for pair in uncertain_pairs:
            lines.append(f"- #{pair['a']} ↔ #{pair['b']}: P(same)={pair['p_same']}; "
                         f"verdict={pair['verdict']}; {pair['classification']}")
        lines.append("")
    for label, numbers in (("Escalate for risk/security review", escalate),
                           ("Possible author follow-up — verify before requesting changes", follow_up)):
        if numbers:
            lines += [f"## {label}", "", *[f"- #{n} {cell(prs[n]['title'])}" for n in numbers], ""]
    (OUT_DIR / "tranches.md").write_text("\n".join(lines), encoding="utf-8")
    # Commit the report manifest last. The renderer rejects mixed generations.
    atomic_json(OUT_DIR / "summary.json", summary)
    print(json.dumps(summary, indent=1))
    print(f"\nwrote {OUT_DIR}/clusters.json dupes.json tranches.md summary.json")

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    fetch = sub.add_parser("fetch", help="refresh observed open-PR membership from GitHub")
    fetch.add_argument("--transport", choices=("urllib", "curl"), default="urllib")
    j = sub.add_parser("judge", help="Jev judgment pass over PRs")
    j.add_argument("--limit", type=int, default=None, help="judge only the N newest unjudged PRs")
    j.add_argument("--resume", action="store_true", help="reuse judgments bound to unchanged input/questions/model")
    d = sub.add_parser("dupes", help="compare candidate pairs with Jev")
    d.add_argument("--max-pairs", type=int, default=300)
    cluster = sub.add_parser("cluster", help="build candidate groups and review reports offline")
    cluster.add_argument("--allow-unbound", action="store_true", help="inspect legacy judgments with freshness warnings; no legacy review tranches")
    a = sub.add_parser("all", help="judge --resume, dupes, cluster")
    a.add_argument("--limit", type=int, default=None)
    a.add_argument("--resume", action="store_true", help="accepted for compatibility; all always resumes")
    a.add_argument("--max-pairs", type=int, default=300)
    args = ap.parse_args()
    if getattr(args, "limit", None) is not None and args.limit <= 0:
        ap.error("--limit must be positive")
    if getattr(args, "max_pairs", 0) < 0:
        ap.error("--max-pairs must be nonnegative")
    if args.cmd == "fetch":
        cmd_fetch(args)
    elif args.cmd == "judge":
        cmd_judge(args)
    elif args.cmd == "dupes":
        cmd_dupes(args)
    elif args.cmd == "cluster":
        cmd_cluster(args)
    elif args.cmd == "all":
        args.resume = True
        cmd_judge(args)
        cmd_dupes(args)
        cmd_cluster(args)


if __name__ == "__main__":
    main()
