# Omarchy PR tranches — Jev triage

Corpus: 2832 open PRs, 5 judged. Duplicate groups: 0 (0 PRs). Ready-to-roll candidates: 1. Needs author follow-up: 0. Escalate: 1.

Method: one batched Jev call per PR (category / risk / is_fix / dupe_signal / finished_form / review_effort / security_flag); duplicate candidates found by title similarity within a category, confirmed by a Jev pair judgment; groups via union-find.

## Tranche: apps-integrations — 1 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #13858 | Hide Hermes' renamed CLI launcher from Apps | unknown | 2.8 | 0.5 | 0.97 |

## Escalate to senior review (high risk or security-relevant)

- #13856 Launch Claude with a real permission bypass (security 0.88)
