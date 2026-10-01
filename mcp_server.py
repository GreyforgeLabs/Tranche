#!/usr/bin/env python3
"""Read-only, model-free access to Tranche's bound local observation."""
import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

import tranche

MAX_FILE_BYTES = 128 * 1024 * 1024
MAX_TOTAL_BYTES = 256 * 1024 * 1024
MAX_INPUT_FILES = 512
MAX_RESULT_BYTES = 1024 * 1024


def input_digests():
    """Bounded byte fingerprints include optional files and corpus membership."""
    snapshot = tranche.PAGES_DIR / "snapshot.json"
    sources = [snapshot] if snapshot.exists() else sorted(tranche.PAGES_DIR.glob("page_*.json"))
    paths = [snapshot, *sources, tranche.JUDGMENTS_PATH, tranche.PAIRS_PATH,
             *(tranche.OUT_DIR / name for name in
               ("summary.json", "clusters.json", "dupes.json", "batches.json"))]
    if len(paths) > MAX_INPUT_FILES:
        raise ReportError("Input file count exceeds limit")
    result, total = {}, 0
    for path in dict.fromkeys(paths):
        if not path.exists():
            result[str(path)] = None
            continue
        with path.open("rb") as stream:
            data = stream.read(MAX_FILE_BYTES + 1)
        total += len(data)
        if len(data) > MAX_FILE_BYTES or total > MAX_TOTAL_BYTES:
            raise ReportError("Input bytes exceed limit")
        result[str(path)] = hashlib.sha256(data).hexdigest()
    return result

DISCLAIMER = ("Model suggestions from titles and shortened descriptions, not merge/close "
              "approval. Patches, CI, reproductions and security have not been verified.")


class ReportError(ValueError):
    """The local observation cannot safely be served."""


def result_text(result):
    """The exact JSON text sent over MCP; the SDK must not reserialize it."""
    text = json.dumps(result, ensure_ascii=False, allow_nan=False)
    if len(text.encode()) > MAX_RESULT_BYTES:
        raise ReportError("Response exceeds byte limit; narrow filters or lower limit")
    return text


class Reports:
    def _load(self):
        try:
            before = input_digests()
            self._read()
            if input_digests() != before:
                raise ReportError("Report files changed during read; retry")
            self.identity["input_bytes"] = before
        except ReportError:
            raise
        except (OSError, ValueError, TypeError, KeyError, AttributeError, tranche.TrancheFatal) as exc:
            raise ReportError("Invalid or missing bound reports; rerun cluster and batches") from exc

    def _read(self):
        summary = json.loads((tranche.OUT_DIR / "summary.json").read_text())
        clusters = json.loads((tranche.OUT_DIR / "clusters.json").read_text())
        dupes = json.loads((tranche.OUT_DIR / "dupes.json").read_text())
        prs = tranche.load_prs()
        if tranche.JUDGMENTS_PATH.exists():
            for line in tranche.JUDGMENTS_PATH.read_text().splitlines():
                if line.strip() and not isinstance(json.loads(line), dict):
                    raise ReportError("Malformed judgment record")
        judgments = tranche.current_judgments(prs)
        # Only the producer's current projection, which the report must bind.
        pairs = tranche.current_pairs(prs, judgments)
        if tranche.PAIRS_PATH.exists():
            for line in tranche.PAIRS_PATH.read_text().splitlines():
                if line.strip() and not isinstance(json.loads(line), dict):
                    raise ReportError("Malformed pair record")
        expected = {"clusters.json": tranche.digest(clusters), "dupes.json": tranche.digest(dupes)}
        if (summary.get("format_version") != 2 or summary.get("repo") != tranche.REPO
                or summary.get("allow_unbound") is not False
                or summary.get("report_binding") != tranche.report_binding(prs, judgments, pairs)
                or summary.get("output_digests") != expected):
            raise ReportError("Reports are stale, unbound, foreign or modified; rerun cluster")
        batches_path = tranche.OUT_DIR / "batches.json"
        batches = json.loads(batches_path.read_text()) if batches_path.exists() else None
        if batches is not None and tranche.digest(batches) != tranche.digest(tranche.merge_batches(
                dupes, judgments, prs, expected["dupes.json"])):
            raise ReportError("batches.json is stale or modified; rerun batches")
        self.batches = batches
        self.summary, self.clusters, self.dupes = summary, clusters, dupes
        self.prs, self.judgments, self.pairs = prs, judgments, pairs
        self.identity = {"report_binding": summary["report_binding"],
                         "batches.json": tranche.digest(batches) if batches is not None else None,
                         **summary["output_digests"]}

    def _envelope(self, **data):
        result = {"repo": tranche.REPO, "disclaimer": DISCLAIMER,
                  "digests": self.identity, **data}
        result_text(result)
        return result

    def _rows(self):
        grouped = {n for group in self.dupes["confirmed_groups"] for n in group}
        grouped |= {n for group in self.dupes["review_groups"] for n in group["members"]}
        related = grouped | {n for pair in self.dupes["uncertain_pairs"] for n in (pair["a"], pair["b"])}
        rows = []
        for number, pr in self.prs.items():
            judgment = self.judgments.get(number, {})
            risk = tranche.metric(judgment, "risk")
            finished = tranche.metric(judgment, "finished_form")
            row = dict(pr, answers=judgment.get("answers", {}),
                       category=tranche.category(judgment) if judgment else "unknown",
                       risk=risk, finished_form=finished,
                       security=tranche.metric(judgment, "security_flag", "noul"),
                       security_priority=tranche.security_priority(judgment),
                       freshness=judgment.get("freshness", "unjudged"),
                       judgment_binding=judgment.get("binding"),
                       risk_band="unknown" if risk is None else
                       "low" if risk <= 1.5 else "core" if risk <= 2.5 else "danger",
                       candidate=bool(judgment) and tranche.review_candidate(pr, judgment, grouped),
                       senior=tranche.escalated(judgment),
                       followup=finished is not None and finished <= 1 and number not in grouped,
                       related=number in related)
            rows.append(row)
        rows.sort(key=lambda row: (not row["security_priority"],
                                  row["risk"] if row["risk"] is not None else 99,
                                  row["created"], row["number"]))
        return rows

    def query(self, text: str = "", category: str | None = None,
              risk_band: str | None = None, security: bool | None = None,
              finished_form: float | None = None, batch: str | None = None,
              queue: str = "all", offset: int = 0, limit: int = 25):
        self._load()
        if (type(offset) is not int or not 0 <= offset <= 100000
                or type(limit) is not int or not 1 <= limit <= 100
                or not isinstance(text, str) or len(text) > 512
                or category is not None and (not isinstance(category, str) or category not in
                    [*tranche.judge_questions()["category"]["criteria"], "security-review", "unknown"])
                or risk_band is not None and risk_band not in ("low", "core", "danger", "unknown")
                or security is not None and type(security) is not bool
                or finished_form is not None and (type(finished_form) not in (int, float)
                    or not 0 <= finished_form <= 3 or not math.isfinite(finished_form))
                or queue not in ("all", "security", "candidates", "senior", "followup", "related")
                or batch is not None and (not isinstance(batch, str) or
                    re.fullmatch(r"B[0-9]{3,6}", batch) is None)):
            raise ReportError("Invalid query arguments; limit 1..100, offset 0..100000")
        members = None
        if batch is not None:
            members = self._batch(batch)["members"]
        terms = text.casefold().split()
        rows = []
        for row in self._rows():
            haystack = f"#{row['number']} @{row['author']} {row['title']} {row['body']}".casefold()
            if (any(term not in haystack for term in terms)
                    or category is not None and not (row["category"] == category or
                        category == "security-review" and row["security_priority"])
                    or risk_band is not None and row["risk_band"] != risk_band
                    or security is not None and (row["security"] is None or
                        row["security_priority"] != security)
                    or finished_form is not None and row["finished_form"] != finished_form
                    or members is not None and row["number"] not in members
                    or queue != "all" and not row[{
                        "security": "security_priority", "candidates": "candidate",
                        "senior": "senior", "followup": "followup", "related": "related"}[queue]]):
                continue
            rows.append(row)
        end = offset + limit
        return self._envelope(items=rows[offset:end], total=len(rows), offset=offset,
                              next_offset=end if end < len(rows) else None)

    def _batch(self, batch_id):
        if not isinstance(batch_id, str) or re.fullmatch(r"B[0-9]{3,6}", batch_id) is None:
            raise ReportError("Expected exact batch id such as B001")
        if self.batches is None:
            raise ReportError("batches.json is unavailable; run tranche.py batches")
        for batch in self.batches["batches"]:
            if batch["id"] == batch_id:
                return batch
        raise ReportError("Unknown batch id")

    def pick(self, batch_id: str):
        self._load()
        batch = self._batch(batch_id)
        rows = {row["number"]: row for row in self._rows()}
        return self._envelope(batch=batch, prs=[rows[n] for n in batch["members"]])

    def next_prompt(self, after: int | str | None = None):
        self._load()
        if self.batches is None:
            raise ReportError("batches.json is unavailable; run tranche.py batches")
        if isinstance(after, str):
            after = self._batch(after)["ordinal"]
        if after is None:
            after = 0
        if type(after) is not int or not 0 <= after <= len(self.batches["batches"]):
            raise ReportError("after must be an existing batch id or ordinal (0 starts)")
        batch = next((b for b in self.batches["batches"] if b["ordinal"] > after), None)
        return self._envelope(batch=batch)

    def related(self, number: int, offset: int = 0, limit: int = 25):
        self._load()
        if (type(number) is not int or number not in self.prs
                or type(offset) is not int or not 0 <= offset <= 100000
                or type(limit) is not int or not 1 <= limit <= 100):
            raise ReportError("Expected captured PR number and bounded pagination")
        items = []
        for group in self.dupes["confirmed_groups"]:
            if number in group:
                items.append({"kind": "confirmed_group", "members": group})
        for group in self.dupes["review_groups"]:
            if number in group["members"]:
                items.append(dict(group, kind="review_group"))
        for pair in self.pairs:
            if number in (pair["a"], pair["b"]):
                items.append(dict(pair, kind="pair", classification=tranche.pair_classification(pair)))
        page = items[offset:offset + limit]
        for item in page:
            members = item.get("members", [item.get("a"), item.get("b")])
            item["sources"] = {str(n): {key: self.prs[n][key] for key in
                                       ("number", "source_digest", "head_sha", "updated", "url")}
                               for n in members}
        end = offset + limit
        return self._envelope(items=page, total=len(items), offset=offset,
                              next_offset=end if end < len(items) else None)

    def digests(self):
        self._load()
        return self._envelope()

    def surface(self):
        self._load()
        overview = [{key: batch[key] for key in
                     ("id", "ordinal", "count", "security_members", "average_risk", "created")}
                    for batch in (self.batches or {}).get("batches", [])]
        rows = self._rows()
        category_counts = {}
        for row in rows:
            category_counts[row["category"]] = category_counts.get(row["category"], 0) + 1
        queues = {}
        for queue, field in {"all": None, "security": "security_priority",
                             "candidates": "candidate", "related": "related",
                             "senior": "senior", "followup": "followup"}.items():
            members = [row["number"] for row in rows if field is None or row[field]]
            queues[queue] = {"count": len(members), "members": members}
        # summary.json coverage is outside output_digests; derive it from inputs.
        coverage = {"prs_in_corpus": len(self.prs), "judged": len(self.judgments),
                    "unjudged": len(self.prs) - len(self.judgments)}
        return self._envelope(summary=coverage, batches_available=self.batches is not None,
                              category_counts=category_counts, queues=queues,
                              batches=overview, filters={
                                  "categories": ["security-review", *tranche.judge_questions()["category"]["criteria"], "unknown"],
                                  "risk_bands": ["low", "core", "danger", "unknown"],
                                  "queues": ["security", "all", "candidates", "senior", "followup", "related"],
                              })


PROTOCOL_VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
PROTOCOL_VERSION = PROTOCOL_VERSIONS[0]


def _version():
    """Repository VERSION when present, so serverInfo tracks the checkout."""
    try:
        return (Path(__file__).resolve().parent / "VERSION").read_text().strip() or "0"
    except OSError:
        return "0"


def _tool_definitions():
    """Standard MCP tool definitions: JSON Schema in, `readOnlyHint` annotations out."""
    descriptions = {
        "surface": "Inspect bound report coverage; model suggestions, never merge approval.",
        "query": "Security-first PR search. Exact filters, finished_form score; offset/limit pagination.",
        "pick": "Inspect one exact batch id with source-bound PRs and the unchanged review prompt.",
        "next_prompt": "Next batch in report order; after is an existing ordinal/id, 0 starts.",
        "related": "Inspect model relationship evidence, conflicts and missing pairs; no survivor selected.",
        "digests": "Read current report binding, output checksums and before/after checked input byte digests.",
    }
    pagination = {
        "offset": {"type": "integer", "minimum": 0, "maximum": 100000, "default": 0},
        "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 25},
    }
    batch_id = {"type": "string", "pattern": r"^B[0-9]{3,6}$"}
    properties = {
        "surface": {},
        "query": {
            "text": {"type": "string", "maxLength": 512, "default": ""},
            "category": {"type": ["string", "null"], "default": None,
                         "enum": [*tranche.judge_questions()["category"]["criteria"],
                                  "security-review", "unknown", None]},
            "risk_band": {"type": ["string", "null"], "default": None,
                          "enum": ["low", "core", "danger", "unknown", None]},
            "security": {"type": ["boolean", "null"], "default": None},
            "finished_form": {"type": ["number", "null"], "minimum": 0,
                              "maximum": 3, "default": None},
            "batch": {"type": ["string", "null"], "pattern": batch_id["pattern"],
                      "default": None},
            "queue": {"type": "string", "default": "all", "enum":
                      ["all", "security", "candidates", "senior", "followup", "related"]},
            **pagination,
        },
        "pick": {"batch_id": batch_id},
        "next_prompt": {"after": {"anyOf": [
            {"type": "integer", "minimum": 0}, batch_id, {"type": "null"}],
            "default": None}},
        "related": {"number": {"type": "integer", "minimum": 1}, **pagination},
        "digests": {},
    }
    required = {"pick": ["batch_id"], "related": ["number"]}
    return [{
        "name": name,
        "description": description,
        "inputSchema": {"type": "object", "properties": properties[name],
                        "additionalProperties": False, "required": required.get(name, [])},
        "annotations": {"readOnlyHint": True, "destructiveHint": False,
                        "idempotentHint": True, "openWorldHint": False},
    } for name, description in descriptions.items()]


TOOLS = _tool_definitions()
TOOL_NAMES = {tool["name"] for tool in TOOLS}


def error_response(code, message, request_id):
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def call_tool(name, arguments):
    """Invoke one tool; the reports' own validators are the argument contract."""
    if name not in TOOL_NAMES:
        raise ReportError(f"Unknown tool: {name}")
    if not isinstance(arguments, dict):
        raise ReportError("Tool arguments must be an object")
    return result_text(getattr(Reports(), name)(**arguments))


def dispatch(message):
    """Handle one JSON-RPC message. Returns the response, or None for a notification."""
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
        return error_response(-32600, "Invalid Request", message.get("id") if isinstance(message, dict) else None)
    method = message.get("method")
    request_id = message.get("id")
    if not isinstance(method, str):
        return error_response(-32600, "Invalid Request", request_id)
    if request_id is None:  # notification
        return None
    if method == "initialize":
        requested = (message.get("params") or {}).get("protocolVersion")
        version = requested if requested in PROTOCOL_VERSIONS else PROTOCOL_VERSION
        return {"jsonrpc": "2.0", "id": request_id, "result": {
            "protocolVersion": version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "tranche", "version": _version()},
            "instructions": DISCLAIMER}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": request_id, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": request_id, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = message.get("params") or {}
        if params.get("name") not in TOOL_NAMES:
            return error_response(-32602, f"Unknown tool: {params.get('name')}", request_id)
        try:
            text = call_tool(params.get("name"), params.get("arguments") or {})
        except Exception as exc:  # execution errors are results with isError
            return {"jsonrpc": "2.0", "id": request_id, "result": {
                "content": [{"type": "text", "text": str(exc)}], "isError": True}}
        return {"jsonrpc": "2.0", "id": request_id, "result": {
            "content": [{"type": "text", "text": text}], "isError": False}}
    return error_response(-32601, f"Method not found: {method}", request_id)


def serve(stdin=None, stdout=None):
    """Newline-delimited JSON-RPC over stdio; the standard MCP stdio transport."""
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    for line in stdin:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
        except ValueError:
            response = error_response(-32700, "Parse error", None)
        else:
            response = dispatch(message)
        if response is not None:
            stdout.write(json.dumps(response, ensure_ascii=False, allow_nan=False) + "\n")
            stdout.flush()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=tranche.ROOT,
                        help="Local Tranche report root (data/pages and out); no acquisition")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    tranche.ROOT = root
    tranche.PAGES_DIR = root / "data" / "pages"
    tranche.OUT_DIR = root / "out"
    tranche.JUDGMENTS_PATH = tranche.OUT_DIR / "judgments.jsonl"
    tranche.PAIRS_PATH = tranche.OUT_DIR / "pair_verdicts.jsonl"
    serve()


if __name__ == "__main__":
    main()
