#!/usr/bin/env python3
"""Generate the GitHub Pages site (docs/index.html) from real out/ data.

Every number and row on the page comes from the pipeline outputs; nothing is
hardcoded except the snapshot label. Re-run `python3 triage.py cluster` then
this script to refresh.
"""

import json
import html
from collections import Counter
from datetime import datetime
from pathlib import Path

import triage

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
DOCS = ROOT / "docs"

# The PR snapshot was fetched 2026-09-30 ~13:10 CEST; judgments completed shortly after
# (mtime of out/judgments.jsonl). Re-fetch + re-cluster to refresh.
SNAPSHOT_LABEL = "30 Sep 2026, ~13:10 CEST"
JUDGED_AT = datetime.fromtimestamp((OUT / "judgments.jsonl").stat().st_mtime).strftime("%d %b %Y, %H:%M")

summary = json.loads((OUT / "summary.json").read_text())
dupes = json.loads((OUT / "dupes.json").read_text())
clusters = json.loads((OUT / "clusters.json").read_text())
judgments = triage.load_judgments()
prs = triage.load_prs()

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


def pr_link(n, title=None, sup=False):
    t = e((title or prs.get(n, {}).get("title", ""))[:78])
    s = ' <span class="sup">superseded</span>' if sup else ""
    return f'<a href="https://github.com/omacom/omarchy/pull/{n}" target="_blank">#{n}</a> {t}{s}'


# Re-derive escalate / follow-up exactly as cmd_cluster does
in_dupe = {n for g in dupes["confirmed_groups"] for n in g}
superseded = {n: g[0] for g in dupes["confirmed_groups"] for n in g if n != g[0]}
escalate, followup = [], []
for n, j in judgments.items():
    a = j["answers"]
    if a.get("risk", {}).get("score", 0) >= 3.0 or a.get("security_flag", {}).get("noul", 0) >= 0.5:
        escalate.append(n)
    if a.get("finished_form", {}).get("score", 3) <= 1.0 and n not in in_dupe and n not in superseded:
        followup.append(n)

# Category distribution
cat_counts = Counter(
    j["answers"].get("category", {}).get("choice", "unclear") for j in judgments.values()
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
<div class="sub">All {summary['prs_in_corpus']} open pull requests of <a href="https://github.com/omacom/omarchy" target="_blank">omacom/omarchy</a>, judged by TypeSafe's <a href="https://docs.typesafe.ai" target="_blank">System One model Jev</a> and clustered into merge tranches. Built by <a href="https://github.com/blackopsrepl" target="_blank">@blackopsrepl</a> for the Omarchy triage team.</div>
<blockquote>“We're 2,200 PRs deep on GH now and getting nearly a hundred new ones every day. I'll never be able to catch up. Agents will help, but we need humans too. If you have DEEP Linux experience, is agent-forward, and want to join the new Omarchy triage team, write triage@omarchy.org.”<br><span class="who">— DHH, 12 Sep 2026 · <a href="https://x.com/dhh/status/2098755120540393908" target="_blank">x.com/dhh/…</a></span></blockquote>
<div class="stats">
<div class="stat b"><div class="n">{summary['prs_in_corpus']}</div><div class="l">open PRs judged</div></div>
<div class="stat g"><div class="n">{summary['ready_prs']}</div><div class="l">in merge-ready tranches</div></div>
<div class="stat p"><div class="n">{summary['dupe_groups']}</div><div class="l">duplicate clusters ({summary['prs_in_dupe_groups']} PRs)</div></div>
<div class="stat y"><div class="n">{summary['uncertain_pairs']}</div><div class="l">pairs needing a human call</div></div>
<div class="stat r"><div class="n">{len(escalate)}</div><div class="l">escalate: high risk / security</div></div>
</div>
<div class="muted">Snapshot of open PRs: {SNAPSHOT_LABEL} · judged {JUDGED_AT} with jev-1.13.0 · fresh runs: <code>fetch → judge --resume → dupes → cluster</code></div>
</header>""")

# --- landscape ---
parts.append("<h2>The backlog at a glance</h2><div class=\"inner\">")
total = sum(cat_counts.values())
colors = ["#7aa2f7", "#bb9af7", "#9ece6a", "#e0af68", "#f7768e", "#73daca", "#b4f9f8", "#c0caf5", "#89ddff", "#565f89"]
bar = "".join(
    f'<i style="width:{100 * cnt / total:.2f}%;background:{colors[i % len(colors)]}" title="{e(CAT_LABELS.get(c, c))}: {cnt}"></i>'
    for i, (c, cnt) in enumerate(cat_counts.most_common())
)
parts.append(f'<div class="bar">{bar}</div><div class="legend">')
for c, cnt in cat_counts.most_common():
    parts.append(f"<span><b>{e(CAT_LABELS.get(c, c))}</b> {cnt}</span>")
parts.append("</div></div>")

# --- tranches ---
parts.append(f"<h2>Merge-ready tranches <span class='muted'>({summary['ready_prs']} PRs — reviewed &amp; QA'd as batches, the roll-ups DHH asked for)</span></h2>")
tranche_cats = []
for cat, bands in clusters.items():
    ready = [
        it for it in bands.get("low", [])
        if it["finished_form"] >= 1.8 and it["is_fix"] >= 0.6
        and it["number"] not in in_dupe and not it["superseded_by"]
        and judgments[it["number"]]["answers"].get("security_flag", {}).get("noul", 0) < 0.5
    ]
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
        f"<details><summary>{e(CAT_LABELS.get(cat, cat))} <span class='cnt'>— {len(ready)} PRs, all low-risk fixes in finished form</span></summary>"
        f"<div class='inner'><table><tr><th>PR</th><th>Title</th><th>Author</th><th>Finished</th><th>Is&nbsp;fix</th></tr>{rows}</table></div></details>"
    )

# --- dupes ---
parts.append(f"<h2>Duplicate &amp; overlapping clusters <span class='muted'>({len(dupes['confirmed_groups'])} groups, {summary['superseded']} PRs superseded — consolidate, maintainer picks the winner)</span></h2>")
for g in dupes["confirmed_groups"]:
    members = " · ".join(
        f"<span class='canon'>{pr_link(n)}</span>" if n == g[0] else f"{pr_link(n, sup=True)}"
        for n in g
    )
    parts.append(f"<div class='inner'>👥 {members} <span class='muted'>— “{e(prs[g[0]]['title'][:70])}”</span></div>")
parts.append("<div class='inner muted' style='margin-top:8px'>Oldest PR in each cluster is the canonical candidate; the rest are marked superseded. Every union was confirmed by a Jev pair judgment at P(same change) ≥ 0.65.</div>")

# --- uncertain ---
parts.append(f"<h2>Jev is undecided <span class='muted'>({len(dupes['uncertain_pairs'])} pairs — 0.35 ≤ P(same) &lt; 0.65, human decides)</span></h2>")
for p in dupes["uncertain_pairs"][:60]:
    parts.append(
        f"<div class='inner'>⚖️ {pr_link(p['a'], prs.get(p['a'], {}).get('title', '')[:60])} ↔ "
        f"{pr_link(p['b'], prs.get(p['b'], {}).get('title', '')[:60])} <span class='muted'>P(same)={p['p_same']:.2f}</span></div>"
    )
if len(dupes["uncertain_pairs"]) > 60:
    parts.append(f"<div class='inner muted'>…and {len(dupes['uncertain_pairs']) - 60} more in the repo's <code>out/dupes.json</code></div>")

# --- escalate ---
parts.append(f"<h2>Escalate to senior review <span class='muted'>({len(escalate)} PRs — risk ≥ 3 or security-relevant, never batch-merge these)</span></h2>")
for n in sorted(escalate):
    a = judgments[n]["answers"]
    tags = []
    if a.get("risk", {}).get("score", 0) >= 3.0:
        tags.append(f"<span style='color:var(--red)'>risk {a['risk']['score']:.1f}</span>")
    if a.get("security_flag", {}).get("noul", 0) >= 0.5:
        tags.append(f"<span style='color:var(--yel)'>security {a['security_flag']['noul']:.2f}</span>")
    parts.append(f"<div class='inner'>⚠️ {pr_link(n)} {e(prs[n]['title'][:80])} <span class='muted'>({', '.join(tags)})</span></div>")

# --- followup ---
parts.append(f"<h2>Not in finished form <span class='muted'>({len(followup)} PRs — send back to authors)</span></h2>")
for n in sorted(followup):
    parts.append(f"<div class='inner'>✏️ {pr_link(n)} {e(prs[n]['title'][:90])}</div>")

parts.append(f"""<footer>
<p><b>Method.</b> Code owns the workflow, Jev owns the judgments. One batched TypeSafe call per PR asks seven typed questions: category (Choice), merge risk 0–4 (Score), is-a-fix and security flag (Noul), finished form 0–3 and review effort (Score), duplicate signal (Noul). Duplicate candidates come from title similarity within a category plus body cross-references, and every union is confirmed by a separate Jev pair judgment. A PR is tranche-ready when it is low-risk, a fix, in finished form (≥ 1.8), security-clean, and not superseded. Full pipeline and data: <a href="https://github.com/blackopsrepl/omarchy-pr-jev-triage" target="_blank">github.com/blackopsrepl/omarchy-pr-jev-triage</a>.</p>
<p class="muted">Jev supplies typed judgments and probabilities; every merge decision belongs to a human. Recommendations are not endorsements. Generated {datetime.utcnow().strftime('%d %b %Y %H:%M UTC')}.</p>
</footer>
<script>document.querySelectorAll('details').forEach(d=>{{if(!d.open&&d.querySelector('table'))d.open=false}})</script>
</main></body></html>""")

DOCS.mkdir(exist_ok=True)
out = "\n".join(parts)
(DOCS / "index.html").write_text(out)
print(f"wrote docs/index.html ({len(out)//1024} KB)")
print(f"tranches: {[(c, len(r)) for c, r in tranche_cats]}")
print(f"escalate: {len(escalate)}, followup: {len(followup)}, dupes: {len(dupes['confirmed_groups'])}, uncertain: {len(dupes['uncertain_pairs'])}")
