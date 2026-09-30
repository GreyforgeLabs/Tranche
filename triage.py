#!/usr/bin/env python3
"""Omarchy PR triage via TypeSafe Jev.

Groups the open PRs of omacom/omarchy into review tranches, surfaces duplicate
clusters, and flags items that are not in finished form — the roll-up work DHH
asked the triage team to do (x.com/dhh/status/2098755120540393908).

Judgments come from TypeSafe's System One API (Jev). Code owns the workflow:
fetch -> judge (one batched call per PR) -> confirm duplicate pairs -> cluster.

Usage:
  python3 triage.py fetch              # refresh data/pages/*.json
  python3 triage.py judge [--limit N] [--resume]
  python3 triage.py dupes [--max-pairs N]
  python3 triage.py cluster            # writes out/clusters.json, out/dupes.json,
                                       #            out/tranches.md, out/summary.json
  python3 triage.py all [--limit N]
"""

from __future__ import annotations

import argparse
import difflib
import json
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    import os
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
    for attempt in range(6):
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
                raise TriageFatal(f"Auth rejected (401). Check the key. {last}")
            if e.code == 422:
                raise TriageFatal(f"Request rejected (422) — question shape bug. {last}")
            if e.code in (429, 529) or e.code >= 500:
                time.sleep(backoff + random.random())
                backoff = min(backoff * 2, 60)
                continue
            raise TriageFatal(last)
        except urllib.error.URLError as e:
            last = f"network: {e}"
            time.sleep(backoff + random.random())
            backoff = min(backoff * 2, 60)
    raise TriageFatal(f"Retries exhausted. Last error: {last}")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_prs() -> dict[int, dict]:
    prs: dict[int, dict] = {}
    for path in sorted(PAGES_DIR.glob("page_*.json")):
        for p in json.loads(path.read_text()):
            raw_body = p.get("body") or ""
            refs = sorted({int(x) for x in re.findall(r"#(\d{2,6})", raw_body)})
            body = re.sub(r"<!--.*?-->", "", raw_body, flags=re.S)
            body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)  # images
            body = re.sub(r"https?://\S+", "", body)          # bare links
            body = re.sub(r"\s+", " ", body).strip()[:BODY_CHARS]
            prs[p["number"]] = {
                "number": p["number"],
                "title": p["title"].strip(),
                "body": body,
                "author": ((p.get("user") or p.get("author") or {}).get("login", "unknown")),
                "created": p.get("created_at", ""),
                "updated": p.get("updated_at", ""),
                "draft": bool(p.get("draft")),
                "files": p.get("changed_files", 0),
                "additions": p.get("additions", 0),
                "deletions": p.get("deletions", 0),
                "labels": [l["name"] for l in p.get("labels", [])],
                "refs": refs,
            }
    return prs


def pr_state(pr: dict) -> dict:
    return {
        "pr": {
            "title": pr["title"],
            "body": pr["body"] or "(empty body)",
            "author": pr["author"],
            "diffstat": f"{pr['files']} files changed, +{pr['additions']}/-{pr['deletions']}",
            "draft": pr["draft"],
        }
    }


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_fetch(args) -> None:
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    page, total = 1, 0
    while True:
        out = PAGES_DIR / f"page_{page}.json"
        with urllib.request.urlopen(
            f"https://api.github.com/repos/{REPO}/pulls?state=open&per_page=100&page={page}", timeout=60
        ) as r:
            arr = json.load(r)
        if not arr:
            if page == 1:
                print("no open PRs (or rate-limited); keeping existing pages")
            else:
                out.write_text("[]")
            break
        out.write_text(json.dumps(arr))
        total += len(arr)
        print(f"page {page}: {len(arr)} PRs (total {total})")
        if len(arr) < 100:
            # drop stale pages beyond the end
            stale = page + 1
            while (PAGES_DIR / f"page_{stale}.json").exists():
                (PAGES_DIR / f"page_{stale}.json").unlink()
                stale += 1
            break
        page += 1
        time.sleep(0.4)
    print(f"fetched {total} open PRs into {PAGES_DIR}")


def load_done() -> dict[int, dict]:
    done: dict[int, dict] = {}
    if JUDGMENTS_PATH.exists():
        for line in JUDGMENTS_PATH.read_text().splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "error" not in rec:
                done[rec["number"]] = rec
    return done


def cmd_judge(args) -> None:
    prs = load_prs()
    done = load_done() if args.resume else {}
    if not args.resume:
        JUDGMENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        JUDGMENTS_PATH.write_text("")
    todo = [n for n in sorted(prs, reverse=True) if n not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(prs)} PRs, {len(done)} already judged, {len(todo)} to go")
    key = read_key()
    lock = threading.Lock()
    errors: list[str] = []
    tokens_in = tokens_out = 0

    def work(number: int) -> None:
        nonlocal tokens_in, tokens_out
        pr = prs[number]
        try:
            resp = ask(pr_state(pr), judge_questions(), key)
            rec = {"number": number, "title": pr["title"], "answers": resp["answers"], "usage": resp.get("usage", {})}
        except TriageFatal as e:
            with lock:
                errors.append(f"#{number}: {e}")
            if "401" in str(e):
                raise
            return
        with lock:
            with JUDGMENTS_PATH.open("a") as f:
                f.write(json.dumps(rec) + "\n")
            tokens_in += resp.get("usage", {}).get("input_tokens", 0)
            tokens_out += resp.get("usage", {}).get("output_tokens", 0)
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

    print(f"done: {len(done) + 0 if not todo else len(done)} judged this session's target; errors: {len(errors)}")
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
        cat = j["answers"].get("category", {}).get("choice", "unclear")
        by_cat[cat].append(n)
    pairs = []
    for cat, nums in by_cat.items():
        nums = sorted(nums)
        for i, a in enumerate(nums):
            ta, tb_ = prs[a]["title"].lower(), None
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
            if b in prs and b in judgments and (a, b) not in seen:
                seen.add((a, b))
                pairs.append((1.0, a, b))
    pairs.sort(key=lambda t: -t[0])
    return pairs


def cmd_dupes(args) -> None:
    prs = load_prs()
    judgments = load_judgments()
    missing = len(prs) - len(judgments)
    if missing > 100:
        print(f"warning: {missing} PRs not judged yet; dupe pass runs on judged subset", file=sys.stderr)
    done_pairs: set[tuple[int, int]] = set()
    if PAIRS_PATH.exists():
        for line in PAIRS_PATH.read_text().splitlines():
            try:
                rec = json.loads(line)
                done_pairs.add((rec["a"], rec["b"]))
            except json.JSONDecodeError:
                continue
    pairs = [(s, a, b) for s, a, b in lexical_pairs(prs, judgments) if (a, b) not in done_pairs]
    pairs = pairs[: args.max_pairs]
    print(f"{len(pairs)} candidate pairs to confirm (skipping {len(done_pairs)} already done)")
    key = read_key()
    lock = threading.Lock()

    def brief(n):
        p = prs[n]
        return {"number": n, "title": p["title"], "body": (p["body"] or "")[:400]}

    def work(item):
        s, a, b = item
        resp = ask({"pr_a": brief(a), "pr_b": brief(b)}, pair_questions(), key)
        rec = {
            "a": a, "b": b, "similarity": round(s, 3),
            "verdict": resp["answers"]["sameness"]["choice"],
            "probabilities": resp["answers"]["sameness"]["probabilities"],
            "usage": resp.get("usage", {}),
        }
        with lock:
            with PAIRS_PATH.open("a") as f:
                f.write(json.dumps(rec) + "\n")

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(work, it) for it in pairs]
        for i, f in enumerate(as_completed(futures)):
            f.result()
            if (i + 1) % 25 == 0:
                print(f"confirmed {i + 1}/{len(pairs)}")
    print("dupe confirmation complete")


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


def cmd_cluster(args) -> None:
    prs = load_prs()
    judgments = load_judgments()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- duplicate groups from confirmed pairs ---
    verdicts = []
    if PAIRS_PATH.exists():
        for line in PAIRS_PATH.read_text().splitlines():
            try:
                verdicts.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    dsu = DSU()
    for v in verdicts:
        if v["verdict"] == "same_change" and v["probabilities"].get("same_change", 0) >= 0.65:
            dsu.union(v["a"], v["b"])
    groups: dict[int, list[int]] = defaultdict(list)
    for n in {x for v in verdicts for x in (v["a"], v["b"])}:
        if n in judgments:
            groups[dsu.find(n)].append(n)
    dupe_groups = sorted(
        [sorted(members) for members in groups.values() if len(members) >= 2],
        key=lambda g: -len(g),
    )
    superseded: dict[int, int] = {}
    for members in dupe_groups:
        keep = min(members)  # lowest number = oldest = canonical candidate
        for n in members:
            if n != keep:
                superseded[n] = keep

    # --- category x risk clustering ---
    clusters: dict[str, dict] = {}
    for n, j in judgments.items():
        a = j["answers"]
        cat = a.get("category", {}).get("choice", "unclear")
        risk = a.get("risk", {}).get("score", 0)
        band = "low" if risk <= 1.5 else ("core" if risk <= 2.5 else "danger")
        clusters.setdefault(cat, {}).setdefault(band, []).append(n)

    cluster_out = {
        cat: {
            band: [
                {
                    "number": n,
                    "title": prs[n]["title"],
                    "author": prs[n]["author"],
                    "risk": round(judgments[n]["answers"].get("risk", {}).get("score", 0), 2),
                    "finished_form": round(judgments[n]["answers"].get("finished_form", {}).get("score", 0), 2),
                    "is_fix": round(judgments[n]["answers"].get("is_fix", {}).get("noul", 0), 2),
                    "review_effort": round(judgments[n]["answers"].get("review_effort", {}).get("score", 0), 2),
                    "superseded_by": superseded.get(n),
                }
                for n in sorted(nums, key=lambda n: -judgments[n]["answers"].get("finished_form", {}).get("score", 0))
            ]
            for band, nums in bands.items()
        }
        for cat, bands in clusters.items()
    }
    (OUT_DIR / "clusters.json").write_text(json.dumps(cluster_out, indent=1))
    (OUT_DIR / "dupes.json").write_text(json.dumps(dupe_groups, indent=1))

    # --- tranches ---
    def band_of(n):
        cat = judgments[n]["answers"].get("category", {}).get("choice", "unclear")
        risk = judgments[n]["answers"].get("risk", {}).get("score", 0)
        return cat, ("low" if risk <= 1.5 else ("core" if risk <= 2.5 else "danger"))

    in_dupe_group = {n for g in dupe_groups for n in g}
    tranches = []
    for cat, bands in cluster_out.items():
        for band, items in bands.items():
            if band != "low":
                continue
            ready = [
                it for it in items
                if it["finished_form"] >= 1.8 and it["is_fix"] >= 0.6
                and it["number"] not in in_dupe_group
                and judgments[it["number"]]["answers"].get("security_flag", {}).get("noul", 0) < 0.5
                and not it["superseded_by"]
            ]
            if ready:
                tranches.append((cat, ready))

    follow_up = [
        n for n, j in judgments.items()
        if j["answers"].get("finished_form", {}).get("score", 3) <= 1.0
        and n not in in_dupe_group and not superseded.get(n)
    ]
    escalate = [
        n for n, j in judgments.items()
        if j["answers"].get("risk", {}).get("score", 0) >= 3.0
        or j["answers"].get("security_flag", {}).get("noul", 0) >= 0.5
    ]

    tokens = Counter()
    for j in judgments.values():
        u = j.get("usage", {})
        tokens["in"] += u.get("input_tokens", 0)
        tokens["out"] += u.get("output_tokens", 0)
    for v in verdicts:
        u = v.get("usage", {})
        tokens["in"] += u.get("input_tokens", 0)
        tokens["out"] += u.get("output_tokens", 0)

    summary = {
        "repo": REPO,
        "prs_in_corpus": len(prs),
        "judged": len(judgments),
        "dupe_groups": len(dupe_groups),
        "prs_in_dupe_groups": len(in_dupe_group),
        "superseded": len(superseded),
        "ready_tranches": len(tranches),
        "ready_prs": sum(len(r) for _, r in tranches),
        "needs_author_followup": len(follow_up),
        "escalate_review": len(escalate),
        "tokens": {"input": tokens["in"], "output": tokens["out"]},
    }
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=1))

    # --- human report ---
    lines = [
        f"# Omarchy PR tranches — Jev triage",
        "",
        f"Corpus: {len(prs)} open PRs, {len(judgments)} judged. "
        f"Duplicate groups: {len(dupe_groups)} ({len(in_dupe_group)} PRs). "
        f"Ready-to-roll candidates: {summary['ready_prs']}. "
        f"Needs author follow-up: {len(follow_up)}. Escalate: {len(escalate)}.",
        "",
        "Method: one batched Jev call per PR (category / risk / is_fix / dupe_signal / "
        "finished_form / review_effort / security_flag); duplicate candidates found by title "
        "similarity within a category, confirmed by a Jev pair judgment; groups via union-find.",
        "",
    ]
    for cat, ready in sorted(tranches, key=lambda t: -len(t[1])):
        lines += [f"## Tranche: {cat} — {len(ready)} PRs recommended as a merge-ready roll-up", ""]
        lines += ["| PR | title | author | finished | effort | fix |", "|---|---|---|---|---|---|"]
        for it in ready:
            lines.append(
                f"| #{it['number']} | {it['title'][:80]} | {it['author']} | "
                f"{it['finished_form']:.1f} | {it['review_effort']:.1f} | {it['is_fix']:.2f} |"
            )
        lines.append("")
    if dupe_groups:
        lines += ["## Duplicate / overlapping clusters (consolidate; maintainer picks the winner)", ""]
        for g in dupe_groups:
            members = ", ".join(
                f"#{n}{' (superseded)' if n in superseded else ' (canonical candidate)'}" for n in g
            )
            first = prs[g[0]]["title"][:70]
            lines.append(f"- {members} — e.g. “{first}”")
        lines.append("")
    if escalate:
        lines += ["## Escalate to senior review (high risk or security-relevant)", ""]
        for n in sorted(escalate):
            j = judgments[n]["answers"]
            why = []
            if j.get("risk", {}).get("score", 0) >= 3.0:
                why.append(f"risk {j['risk']['score']:.1f}")
            if j.get("security_flag", {}).get("noul", 0) >= 0.5:
                why.append(f"security {j['security_flag']['noul']:.2f}")
            lines.append(f"- #{n} {prs[n]['title'][:80]} ({', '.join(why)})")
        lines.append("")
    if follow_up:
        lines += ["## Not in finished form — send back to authors", ""]
        for n in sorted(follow_up):
            lines.append(f"- #{n} {prs[n]['title'][:90]}")
        lines.append("")
    (OUT_DIR / "tranches.md").write_text("\n".join(lines))

    print(json.dumps(summary, indent=1))
    print(f"\nwrote {OUT_DIR}/clusters.json dupes.json tranches.md summary.json")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="refresh open-PR pages from GitHub")
    j = sub.add_parser("judge", help="Jev judgment pass over PRs")
    j.add_argument("--limit", type=int, default=None, help="judge only the N newest unjudged PRs")
    j.add_argument("--resume", action="store_true", help="skip PRs already in out/judgments.jsonl")
    d = sub.add_parser("dupes", help="confirm candidate duplicate pairs with Jev")
    d.add_argument("--max-pairs", type=int, default=300)
    sub.add_parser("cluster", help="build clusters, tranches and reports")
    a = sub.add_parser("all", help="judge --resume, dupes, cluster")
    a.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
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
