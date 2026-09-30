#!/usr/bin/env python3
"""Generate the GitHub Pages site (docs/index.html) from real out/ data.

Every number and row on the page comes from the pipeline outputs; nothing is
a substitute for source verification. Re-run `python3 triage.py cluster` then
this script to refresh.
"""

import html
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import triage

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
DOCS = ROOT / "docs"

summary = json.loads((OUT / "summary.json").read_text())
dupes = json.loads((OUT / "dupes.json").read_text())
clusters = json.loads((OUT / "clusters.json").read_text())
prs = triage.load_prs()
allow_unbound = summary.get("allow_unbound", False)
judgments = triage.current_judgments(prs, allow_unbound=allow_unbound)
verdicts = triage.current_pairs(prs, judgments, allow_unbound=allow_unbound)
if (summary.get("format_version") != 2
        or summary.get("repo") != triage.REPO
        or summary.get("report_binding") != triage.report_binding(prs, judgments, verdicts)
        or summary.get("output_digests") != {"clusters.json": triage.digest(clusters),
                                              "dupes.json": triage.digest(dupes)}):
    raise triage.TriageFatal("Report inputs changed or are legacy/mixed; rerun cluster before rendering")
snapshot = triage.PAGES_DIR / "snapshot.json"
SNAPSHOT_LABEL = json.loads(snapshot.read_text()).get("observed_at", "not recorded") if snapshot.exists() else "not recorded (legacy pages)"
MODEL_LABEL = ", ".join(sorted({str(j.get("resolved_model")) for j in judgments.values() if j.get("resolved_model")})) or "resolved model not recorded"

CAT_LABELS = {
    "install-setup": "Install & Setup",
    "desktop-config": "Desktop Config",
    "shell-cli": "Shell & CLI",
    "apps-integrations": "Apps & Integrations",
    "hardware-drivers": "Hardware & Drivers",
    "update-release": "Update & Release",
    "agents-ai": "Agents & AI",
    "docs": "Docs",
    "fix-misc": "Fixes & Misc",
    "unclear": "Unclear",
}

e = html.escape


def pr_link(n, title=None):
    t = e((title or prs.get(n, {}).get("title", ""))[:78])
    return f'<a href="https://github.com/omacom/omarchy/pull/{n}" target="_blank">#{n}</a> {t}'


# Use the same eligibility and grouping policy as the CLI report.
in_dupe = {n for g in dupes["confirmed_groups"] for n in g} | {n for g in dupes["review_groups"] for n in g["members"]}
escalate = [n for n, j in judgments.items() if triage.escalated(j)]
followup = [n for n, j in judgments.items() if triage.metric(j, "finished_form") is not None
            and triage.metric(j, "finished_form") <= 1 and n not in in_dupe]

# Category distribution
cat_counts = Counter(
    triage.category(j) for j in judgments.values()
)

parts = []
parts.append(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Omarchy PR Triage — Jev</title>
<style>
:root{{--bg:#16161e;--bg2:#1a1b26;--fg:#c0caf5;--dim:#565f89;--acc:#7aa2f7;--pur:#bb9af7;--grn:#9ece6a;--red:#f7768e;--yel:#e0af68;--line:#24253a}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1060px;margin:0 auto;padding:32px 20px 80px}}
a{{color:var(--acc);text-decoration:none}} a:hover{{text-decoration:underline}}
code{{background:var(--bg2);border:1px solid var(--line);border-radius:0;padding:1px 6px;font-size:.9em}}
header{{border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:28px}}
h1{{font-size:1.9em;margin:0 0 6px}} h1 .jev{{color:var(--pur)}}
.sub{{color:var(--dim)}}
blockquote{{margin:18px 0;padding:10px 18px;border-left:3px solid var(--pur);color:var(--fg);background:var(--bg2);border-radius:0}}
blockquote .who{{color:var(--dim)}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:26px 0}}
.stat{{background:var(--bg2);border:1px solid var(--line);border-radius:0;padding:14px 16px}}
.stat .n{{font-size:1.7em;font-weight:700}} .stat .l{{color:var(--dim);font-size:.85em}}
.stat.g .n{{color:var(--grn)}} .stat.p .n{{color:var(--pur)}} .stat.y .n{{color:var(--yel)}} .stat.r .n{{color:var(--red)}} .stat.b .n{{color:var(--acc)}}
h2{{font-size:1.35em;margin:40px 0 12px}}
details{{background:var(--bg2);border:1px solid var(--line);border-radius:0;margin:10px 0}}
summary{{cursor:pointer;padding:12px 16px;font-weight:600;list-style:none}}
summary::before{{content:"▸ ";color:var(--dim)}} details[open] summary::before{{content:"▾ "}}
summary .cnt{{color:var(--dim);font-weight:400}}
.inner{{padding:4px 16px 14px}}
table{{width:100%;border-collapse:collapse;font-size:.92em;margin-top:8px}}
th{{text-align:left;color:var(--dim);font-weight:600;border-bottom:1px solid var(--line);padding:6px 8px}}
td{{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}}
tr:last-child td{{border-bottom:none}}
.sup{{background:#3b2a4d;color:var(--pur);border-radius:0;padding:0 6px;font-size:.8em}}
.canon{{color:var(--grn)}}
.muted{{color:var(--dim)}}
.bar{{height:8px;border-radius:0;background:var(--bg2);overflow:hidden;display:flex;margin-top:6px}}
.bar i{{display:block;height:100%}}
.legend{{display:flex;flex-wrap:wrap;gap:14px;color:var(--dim);font-size:.85em;margin-top:10px}}
.legend b{{color:var(--fg);font-weight:600}}
footer{{margin-top:60px;border-top:1px solid var(--line);padding-top:18px;color:var(--dim);font-size:.88em}}
</style></head><body><main>
<header>
<img src="assets/omarchy-triage.gif" alt="OMARCHY TRIAGE x Jev" title="OMARCHY TRIAGE × Jev — the triage report" style="width:min(1560px,100%);height:auto;display:block;margin:2px 0 12px">
<div class="sub">{summary['prs_in_corpus']} observed open pull requests of <a href="https://github.com/omacom/omarchy" target="_blank">omacom/omarchy</a>, judged by TypeSafe's <a href="https://docs.typesafe.ai" target="_blank">System One model Jev</a> and arranged into model-suggested review candidates. Built by <a href="https://github.com/blackopsrepl" target="_blank">@blackopsrepl</a> for the Omarchy triage team.</div>
<blockquote>“We're 2,200 PRs deep on GH now and getting nearly a hundred new ones every day. I'll never be able to catch up. Agents will help, but we need humans too. If you have DEEP Linux experience, is agent-forward, and want to join the new Omarchy triage team, write triage@omarchy.org.”<br><span class="who">— DHH, 12 Sep 2026 · <a href="https://x.com/dhh/status/2098755120540393908" target="_blank">x.com/dhh/…</a></span></blockquote>
<div class="stats">
<div class="stat b"><div class="n">{summary['judged']}</div><div class="l">matching judgments</div></div>
<div class="stat g"><div class="n">{summary['ready_prs']}</div><div class="l">review candidates</div></div>
<div class="stat p"><div class="n">{summary['dupe_groups']}</div><div class="l">model-consistent groups</div></div>
<div class="stat y"><div class="n">{summary['uncertain_pairs']}</div><div class="l">pairs needing a human call</div></div>
<div class="stat r"><div class="n">{len(escalate)}</div><div class="l">escalate: high risk / security</div></div>
</div>
<div class="muted">Observation: {e(SNAPSHOT_LABEL)} · requested {e(triage.MODEL)} · {e(MODEL_LABEL)} · fresh runs: <code>fetch → judge --resume → dupes → cluster</code></div>
<p>Titles and shortened descriptions only; patches, CI, reproductions, fix coverage and security have not been verified. These are model suggestions, not merge/closure approvals. API pagination is an observation, not a point-in-time snapshot.</p>
<p>{summary['unjudged_or_stale']} PRs unjudged or stale; {summary['unbound_judgments']} unbound legacy judgments; {summary['unknown_risk_or_security']} with unknown risk/security values; {summary['review_groups']} groups needing relationship review. Unbound legacy judgments cannot enter review-candidate tranches.</p>
</header>""")

# --- landscape ---
parts.append("<h2>The backlog at a glance</h2><div class=\"inner\">")
total = sum(cat_counts.values())
colors = ["#7aa2f7", "#bb9af7", "#9ece6a", "#e0af68", "#f7768e", "#73daca", "#b4f9f8", "#c0caf5", "#89ddff", "#565f89"]
bar = "".join(
    f'<i style="width:{100 * cnt / max(total, 1):.2f}%;background:{colors[i % len(colors)]}" title="{e(CAT_LABELS.get(c, c))}: {cnt}"></i>'
    for i, (c, cnt) in enumerate(cat_counts.most_common())
)
parts.append(f'<div class="bar">{bar}</div><div class="legend">')
for c, cnt in cat_counts.most_common():
    parts.append(f"<span><b>{e(CAT_LABELS.get(c, c))}</b> {cnt}</span>")
parts.append("</div></div>")

# --- tranches ---
parts.append(f"<h2>Model-suggested review candidates <span class='muted'>({summary['ready_prs']} PRs — source review and testing still required)</span></h2>")
tranche_cats = []
for cat, bands in clusters.items():
    ready = [it for it in bands.get("low", [])
             if triage.review_candidate(prs[it["number"]], judgments[it["number"]], in_dupe)]
    if ready:
        tranche_cats.append((cat, ready))
tranche_cats.sort(key=lambda t: -len(t[1]))
for cat, ready in tranche_cats:
    rows = "".join(
        f"<tr><td>{pr_link(it['number'])}</td><td>{e(it['title'][:90])}</td>"
        f"<td class='muted'>{e(it['author'])}</td><td>{it['finished_form']:.1f}</td><td>{it['is_fix']:.2f}</td></tr>"
        for it in ready
    )
    parts.append(
        f"<details><summary>{e(CAT_LABELS.get(cat, cat))} <span class='cnt'>— {len(ready)} PRs, prioritized by model scores; verify before acting</span></summary>"
        f"<div class='inner'><table><tr><th>PR</th><th>Title</th><th>Author</th><th>Finished</th><th>Is&nbsp;fix</th></tr>{rows}</table></div></details>"
    )

# --- candidate groups ---
parts.append(f"<h2>Model-consistent candidate groups <span class='muted'>({len(dupes['confirmed_groups'])} groups — no survivor selected)</span></h2>")
for group in dupes["confirmed_groups"]:
    parts.append("<div class='inner'>" + " · ".join(pr_link(n) for n in group) + "</div>")
parts.append("<p>All tested internal pairs agreed at P(same) ≥ 0.65. This does not verify source equivalence or fix coverage; no PR is automatically superseded.</p>")
parts.append(f"<h2>Candidate groups needing relationship review ({len(dupes['review_groups'])})</h2>")
for group in dupes["review_groups"]:
    parts.append("<details><summary>" + " · ".join(pr_link(n) for n in group["members"]) + "</summary><div class='inner'>")
    for field in ("conflicting_pairs", "uncertain_pairs", "missing_pairs"):
        if group[field]:
            parts.append(f"<p>{e(field)}: <code>{e(json.dumps(group[field]))}</code></p>")
    if group["unbound_evidence"]:
        parts.append("<p>Unbound legacy evidence: revisions cannot be checked.</p>")
    parts.append("</div></details>")

# --- uncertain ---
parts.append(f"<h2>Jev is undecided <span class='muted'>({len(dupes['uncertain_pairs'])} pairs — uncertain, contradictory or malformed evidence; human comparison needed)</span></h2>")
for p in dupes["uncertain_pairs"][:60]:
    parts.append(
        f"<div class='inner'>⚖️ {pr_link(p['a'], prs.get(p['a'], {}).get('title', '')[:60])} ↔ "
        f"{pr_link(p['b'], prs.get(p['b'], {}).get('title', '')[:60])} <span class='muted'>P(same)={p['p_same']}; "
        f"verdict={e(str(p['verdict']))}; {e(p['classification'])}</span></div>"
    )
if len(dupes["uncertain_pairs"]) > 60:
    parts.append(f"<div class='inner muted'>…and {len(dupes['uncertain_pairs']) - 60} more in the repo's <code>out/dupes.json</code></div>")

# --- escalate ---
parts.append(f"<h2>Escalate to senior review <span class='muted'>({len(escalate)} PRs — risk ≥ 3 or security-relevant, never batch-merge these)</span></h2>")
for n in sorted(escalate):
    a = judgments[n]["answers"]
    tags = []
    risk = triage.metric(judgments[n], "risk")
    security = triage.metric(judgments[n], "security_flag", "noul")
    if risk is not None and risk >= 3:
        tags.append(f"<span style='color:var(--red)'>risk {a['risk']['score']:.1f}</span>")
    if security is not None and security >= 0.5:
        tags.append(f"<span style='color:var(--yel)'>security {a['security_flag']['noul']:.2f}</span>")
    parts.append(f"<div class='inner'>⚠️ {pr_link(n)} {e(prs[n]['title'][:80])} <span class='muted'>({', '.join(tags)})</span></div>")

# --- followup ---
parts.append(f"<h2>Possible author follow-up <span class='muted'>({len(followup)} PRs — verify before requesting changes)</span></h2>")
for n in sorted(followup):
    parts.append(f"<div class='inner'>✏️ {pr_link(n)} {e(prs[n]['title'][:90])}</div>")

parts.append(f"""<footer>
<p><b>Method.</b> Code owns the workflow; Jev supplies judgments about the provided descriptions. One batched call per PR asks seven typed questions. The projection contains a title and at most 1200 body characters; pair comparisons use at most 400 body characters each. Missing diffstat is unknown. Title similarity and references propose pairs; connectivity proposes groups. Conflicting, uncertain, missing or unbound internal relationships require review. Scores and probabilities are not independently calibrated. Model risk/security scores do not constitute security review. Full pipeline and data: <a href="https://github.com/blackopsrepl/omarchy-pr-jev-triage" target="_blank">github.com/blackopsrepl/omarchy-pr-jev-triage</a>.</p>
<p class="muted">Every merge and closure decision belongs to a maintainer. Generated {datetime.now(timezone.utc).strftime('%d %b %Y %H:%M UTC')}.</p>
</footer>
<script>document.querySelectorAll('details').forEach(d=>{{if(!d.open&&d.querySelector('table'))d.open=false}})</script>
</main></body></html>""")

DOCS.mkdir(exist_ok=True)
out = "\n".join(parts)
(DOCS / "index.html").write_text(out)
print(f"wrote docs/index.html ({len(out)//1024} KB)")
print(f"tranches: {[(c, len(r)) for c, r in tranche_cats]}")
print(f"escalate: {len(escalate)}, followup: {len(followup)}, dupes: {len(dupes['confirmed_groups'])}, uncertain: {len(dupes['uncertain_pairs'])}")
