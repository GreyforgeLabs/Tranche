#!/usr/bin/env python3
"""Render the PR workbench from mutually consistent, bound report inputs."""

import html
import json
from pathlib import Path

import tranche

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
DOCS = ROOT / "docs"

summary = json.loads((OUT / "summary.json").read_text())
dupes = json.loads((OUT / "dupes.json").read_text())
clusters = json.loads((OUT / "clusters.json").read_text())
prs = tranche.load_prs()
allow_unbound = summary.get("allow_unbound", False)
judgments = tranche.current_judgments(prs, allow_unbound=allow_unbound)
verdicts = tranche.current_pairs(prs, judgments, allow_unbound=allow_unbound)
if (summary.get("format_version") != 2
        or summary.get("repo") != tranche.REPO
        or summary.get("report_binding") != tranche.report_binding(prs, judgments, verdicts)
        or summary.get("output_digests") != {"clusters.json": tranche.digest(clusters),
                                              "dupes.json": tranche.digest(dupes)}):
    raise tranche.TrancheFatal("Report inputs changed or are legacy/mixed; rerun cluster before rendering")

# Issue #4: merge batches ship with the workbench when present; a stale or
# foreign batches file must never be shown against a newer dupe run.
batches_path = OUT / "batches.json"
batches = None
if batches_path.exists():
    batches = json.loads(batches_path.read_text())
    if (batches.get("format_version") != 3 or batches.get("repo") != tranche.REPO
            or batches.get("dupes_digest") != summary["output_digests"]["dupes.json"]):
        raise tranche.TrancheFatal("batches.json is stale or foreign; rerun 'tranche.py batches' before rendering")
# Issue #8: the park record renders beside the batches it gated. A batches
# run that parked PRs without its park record - or against a mutated one -
# must never render, same discipline as gen_page's other bound inputs.
parked = None
parked_path = OUT / "parked.json"
if parked_path.exists():
    parked = json.loads(parked_path.read_text())
    expected_parked = tranche.parked_payload(
        tranche.park_state(dupes, judgments, prs), prs, judgments, summary["output_digests"]["dupes.json"])
    if parked != expected_parked:
        raise tranche.TrancheFatal("parked.json is stale, foreign or modified; rerun 'tranche.py batches' before rendering")
if (batches or {}).get("parked_prs") and parked is None:
    raise tranche.TrancheFatal("batches.json parked PRs but parked.json is missing; rerun 'tranche.py batches'")
batch_of = {}
for batch in (batches or {}).get("batches", []):
    tag = {"id": batch["id"], "count": batch["count"]}
    for number in batch["members"]:
        batch_of.setdefault(number, []).append(tag)
merge_batches = [
    {"id": batch["id"], "count": batch["count"], "members": batch["members"],
     "security_members": batch["security_members"],
     "average_risk": batch["average_risk"], "created": batch["created"],
     "review_prompt": batch["review_prompt"]}
    for batch in (batches or {}).get("batches", [])
]

CAT_LABELS = {
    "security-review": "Security (meta)",
    "install-setup": "Install & Setup", "desktop-config": "Desktop Config",
    "shell-cli": "Shell & CLI", "apps-integrations": "Apps & Integrations",
    "hardware-drivers": "Hardware & Drivers", "update-release": "Update & Release",
    "agents-ai": "Agents & AI", "docs": "Docs", "fix-misc": "Fixes & Misc",
    "unclear": "Unclear", "unknown": "Unknown",
}

# Eligibility stays in the CLI policy; this renderer never reclassifies a judgment.
in_dupe = {n for g in dupes["confirmed_groups"] for n in g} | {n for g in dupes["review_groups"] for n in g["members"]}
related = in_dupe | {n for pair in dupes["uncertain_pairs"] for n in (pair["a"], pair["b"])}
parked_by_number = {m["number"]: m for m in (parked or {}).get("members", [])}
rows = []
for n, pr in sorted(prs.items()):
    judgment = judgments.get(n, {})
    finished = tranche.metric(judgment, "finished_form")
    rows.append({
        "number": n, "title": pr["title"], "body": pr["body"],
        "body_truncated": pr["body_truncated"], "author": pr["author"],
        "created": pr["created"], "draft": pr["draft"],
        "category": tranche.category(judgment) if judgment else "unknown",
        "categories": ([ "security-review" ]
                       if judgment and tranche.security_priority(judgment) else []),
        "freshness": judgment.get("freshness", "unjudged or stale"),
        "risk": tranche.metric(judgment, "risk"),
        "security": tranche.metric(judgment, "security_flag", "noul"),
        "security_priority": bool(judgment) and tranche.security_priority(judgment),
        "finished": finished, "effort": tranche.metric(judgment, "review_effort"),
        "is_fix": tranche.metric(judgment, "is_fix", "noul"),
        "diffstat": tranche.pr_state(pr)["pr"]["diffstat"],
        "candidate": bool(judgment) and tranche.review_candidate(pr, judgment, in_dupe),
        "senior": tranche.escalated(judgment),
        "followup": finished is not None and finished <= 1 and n not in in_dupe,
        "related": n in related,
        "parked": parked_by_number.get(n, {}).get("reasons", []),
        "batches": batch_of.get(n, []),
    })
# JSON remains data, never HTML: escape HTML delimiters and JS separators.
payload = json.dumps({"prs": rows, "categories": CAT_LABELS, "groups": dupes,
                      "batches": merge_batches,
                      "batches_available": batches is not None,
                      "parked": parked},
                     ensure_ascii=True, allow_nan=False, separators=(",", ":"))
payload = payload.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
options = ''.join(f'<option value="{cat}">{html.escape(label)}</option>' for cat, label in CAT_LABELS.items())
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<title>OMARCHY — TRIAGE with Tranche (powered by Jev)</title>
<link rel="stylesheet" href="assets/workbench.css">
<script src="assets/workbench.js" defer></script>
</head><body>
<a class="skip-link" href="#search">Skip to PR search</a>
<div class="shell">
<header class="masthead">
<div class="report-brand">
<h1><picture class="wordmark"><source media="(max-width:600px) and (prefers-reduced-motion: reduce)" srcset="assets/omarchy-title.png"><source media="(max-width:600px)" srcset="assets/omarchy.gif"><source media="(prefers-reduced-motion: reduce)" srcset="assets/tranche-title.png"><img src="assets/tranche.gif" alt="OMARCHY — TRIAGE with Tranche (powered by Jev)" width="1560" height="473"></picture></h1>
<div class="mobile-signoff">TRIAGE with <span class="tranche-motion">Tranche</span> <small>(powered by Jev)</small></div>
<figure class="keeper"><img src="assets/tranche-mascot.png" alt="Tranche, the backlog keeper, holding three pull-request cards" width="564" height="800"></figure>
</div>
<div class="masthead-context"><span class="eyebrow">PULL REQUEST WORKBENCH</span><a href="https://github.com/omacom/omarchy">omacom/omarchy ↗</a><p>{len(prs):,} captured PRs</p></div>
</header>
<div class="workbench">
<aside aria-label="PR categories" class="sidebar">
<div class="sidebar-heading"><span class="eyebrow">CATEGORIES</span><span class="small">PRs</span></div>
<div id="category-buttons"></div>
<label class="mobile-category" for="category">Category<select id="category"><option value="all">All categories</option>{options}</select></label>
<div class="sidebar-foot"><span class="status-dot"></span> Review deliberately<p>Built for the Omarchy triage team.</p><a href="https://github.com/blackopsrepl/Tranche">Tranche source ↗</a></div>
</aside>
<main id="main">
<div class="queue-heading"><h2>Pull requests</h2><span class="small">FIND · INSPECT · REVIEW</span></div>
<p class="product-note">AI-assisted priorities; review code and tests before merging.</p>
<nav id="queues" class="queues" aria-label="Review queues">
<button type="button" data-queue="security" aria-pressed="false">Security first <span></span></button>
<button type="button" data-queue="all" aria-pressed="true">All <span></span></button>
<button type="button" data-queue="candidates" aria-pressed="false">Review candidates <span></span></button>
<button type="button" data-queue="senior" aria-pressed="false">Senior review <span></span></button>
<button type="button" data-queue="followup" aria-pressed="false">Author follow-up <span></span></button>
<button type="button" data-queue="parked" aria-pressed="false">Parked <span></span></button>
<button type="button" data-queue="related" aria-pressed="false">Related PRs <span></span></button>
<button type="button" id="batches-view" aria-pressed="false">Batches <span></span></button>
</nav>
<section id="batch-overview" class="batch-overview" aria-label="Pre-release merge batches" hidden>
<h3 class="overview-heading">Suggested merge batches</h3>
<p class="small">Each batch is a Jev-determined group of PRs to merge into ONE pull request. Ordered security-first, then average model risk. Model-suggested — never a merge approval. Open a batch to inspect its PRs.</p>
<div id="batch-list"></div>
</section>
<div class="toolbar">
<div class="search-field"><label for="search" class="sr-only">Search PR title, number, author or description</label><input type="search" id="search" placeholder="Search title, #number, @author, description…" autocomplete="off" spellcheck="false" aria-describedby="search-help"><kbd aria-hidden="true">/</kbd></div>
<label class="sort-field" for="sort">Sort<select id="sort"><option value="newest">Newest first</option><option value="oldest">Oldest first</option><option value="risk">Model risk: high first</option></select></label>
</div>
<div class="result-summary"><p id="result-count" role="status" aria-live="polite" aria-atomic="true"></p><button id="reset" type="button">Reset filters</button></div>
<p id="search-help" class="search-help">Typo-tolerant search · combine terms · exact #number / @author <span>Ctrl+K to search</span></p>
<div class="column-head" aria-hidden="true"><span>PR / TITLE</span><span>MODEL RISK</span></div>
<ol id="results" class="results" aria-label="Pull requests"></ol>
<div id="empty" class="empty" hidden><span class="eyebrow">NO MATCHES</span><h3>No pull requests found.</h3><p>Try fewer terms or a different queue or category.</p><button id="empty-reset" type="button">Show all pull requests</button></div>
<nav class="pagination" aria-label="Results pages"><button id="prev" type="button">← Previous</button><span id="page-label"></span><button id="next" type="button">Next →</button></nav>
<noscript><p>Enable JavaScript to search and inspect {len(prs)} captured PRs. <a href="https://github.com/omacom/omarchy/pulls">Browse on GitHub</a>.</p></noscript>
<footer><a href="https://github.com/blackopsrepl/Tranche">Tranche</a><span>{len(prs)} captured PRs · <a href="https://github.com/omacom/omarchy/pulls">Open GitHub ↗</a></span></footer>
</main>
</div>
</div>
<dialog id="pr-dialog" aria-labelledby="detail-title">
<div class="dialog-toolbar"><span class="eyebrow" id="detail-number"></span><button id="close-detail" type="button" autofocus aria-label="Close PR details">Close <kbd>Esc</kbd></button></div>
<div id="detail-content"></div>
</dialog>
<script id="workbench-data" type="application/json">{payload}</script>
</body></html>
"""
DOCS.mkdir(exist_ok=True)
(DOCS / "index.html").write_text(page)
print(f"wrote docs/index.html ({len(page)//1024} KB); {len(rows)} captured PRs")
print(f"candidates: {sum(r['candidate'] for r in rows)}, senior: {sum(r['senior'] for r in rows)}, "
      f"follow-up: {sum(r['followup'] for r in rows)}, parked: {len(parked_by_number)}, "
      f"related: {sum(r['related'] for r in rows)}")
