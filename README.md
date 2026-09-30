# omarchy-pr-jev-triage

<img src="docs/assets/tranche-mascot.png" alt="Tranche, a watchful geometric owl holding a bundle of three pull-request cards" width="200">

**Tranche, the backlog keeper.** Spots duplicates and gathers fixes into reviewable
batches. Jev supplies the judgments; humans make the merge call.

Triage tooling for the Omarchy PR backlog, built for the triage team DHH stood up
on 2026-09-12 ([x.com/dhh/status/2098755120540393908](https://x.com/dhh/status/2098755120540393908)):

> "We're 2,200 PRs deep on GH now and getting nearly a hundred new ones every day. I'll never
> be able to catch up. Agents will help, but we need humans too. If you have DEEP Linux
> experience, is agent-forward, and want to join the new Omarchy triage team, write
> triage@omarchy.org."
>
> "What we need in particular is people who can roll-up batches of fixes into clusters that I
> can trust are fully reviewed … so I can merge whole tranches of fixes into core."
> "Omarchy Triage can help consolidate PRs, remove dupes, and ensure that everything is ready
> for consideration in a finished form."

This tool does exactly that with [TypeSafe](https://docs.typesafe.ai)'s System One model
**Jev**: every PR gets a batched set of typed judgments, duplicate candidates are confirmed
pair-wise, and code clusters the results into merge tranches. Code owns the workflow; Jev
supplies the semantic judgments. Skill: `.claude/skills/typesafe-ai` (installed via
`npx skills add typesafe-ai/skills --skill typesafe-ai`).

## Setup

```bash
# API key (already present on this machine)
echo "apikey_..." > ~/Documents/jevapi.txt     # or: export TYPESAFE_API_KEY=...
```

## Usage

```bash
python3 triage.py fetch            # refresh data/pages/*.json (open PRs, unauthenticated GH)
python3 triage.py judge            # Jev pass over all PRs  (~7 questions, one call per PR)
python3 triage.py judge --resume   # skip already-judged PRs (out/judgments.jsonl)
python3 triage.py dupes            # confirm candidate duplicate pairs with a Jev pair judgment
python3 triage.py cluster          # build out/{clusters.json,dupes.json,tranches.md,summary.json}
python3 triage.py all --resume     # judge --resume + dupes + cluster
```

## What Jev is asked (one batched call per PR)

| Question      | Type   | Meaning                                             |
|---------------|--------|-----------------------------------------------------|
| `category`    | Choice | install-setup / desktop-config / shell-cli / apps-integrations / hardware-drivers / update-release / agents-ai / docs / fix-misc / unclear |
| `risk`        | Score  | 0 text-only → 4 could break existing installs        |
| `is_fix`      | Noul   | P(bug fix, not feature/taste change)                 |
| `dupe_signal` | Noul   | P(title/body admits duplication or supersedence)     |
| `finished_form` | Score | 0 no description → 3 what+why+QA evidence           |
| `review_effort` | Score | 0 trivial → 3 substantial                           |
| `security_flag` | Noul  | P(touches secrets/sudo/remote-code/network exposure) |

Duplicate detection: title-similarity candidates (SequenceMatcher ≥ 0.72 or Jaccard ≥ 0.62)
**within the same Jev category**, then a Jev `sameness` Choice per pair
(`same_change` / `related_but_different` / `unrelated`); pairs with
P(same_change) ≥ 0.65 are unioned into clusters. Oldest PR in a cluster is the canonical
candidate; the rest are marked superseded.

## Outputs

- `out/tranches.md` — the human report: merge-ready tranches, duplicate clusters,
  escalation list (risk ≥ 3.0 or security ≥ 0.5), send-back-to-author list (finished_form ≤ 1.0).
- `out/clusters.json` — every judged PR by category × risk band (low / core / danger).
- `out/dupes.json` — confirmed duplicate clusters.
- `out/summary.json` — counts and token spend.

A PR is tranche-ready when: risk band `low`, finished_form ≥ 1.8, is_fix ≥ 0.6,
security_flag < 0.5, not in a duplicate cluster. **The tool recommends; humans merge.**

## Freshness

PR state moves fast (DHH: ~100 new/day). Re-run `fetch` then `all --resume`; only
new/changed PRs cost Jev tokens.
