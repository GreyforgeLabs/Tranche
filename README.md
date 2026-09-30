# Tranche

<img src="docs/assets/tranche-mascot.png" alt="Tranche, a watchful geometric owl holding a bundle of three pull-request cards" width="200">

**Tranche, the backlog keeper.** Spots duplicates and gathers fixes into reviewable
batches. Jev supplies the judgments; humans make the merge call.

Model-assisted discovery and review prioritization for the Omarchy PR backlog, built for the triage team DHH stood up
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

This tool uses [TypeSafe](https://docs.typesafe.ai)'s System One model **Jev**
to suggest review candidates and related PR groups. Code owns the workflow;
Jev supplies judgments about the descriptions it receives. This is a discovery
and prioritization pass, not completed QA, verified duplicate detection or a
security review. Maintainers decide what to merge or close.

## Setup

```bash
# Needed only for judge/dupes; fetch, cluster and tests do not use a model key
echo "apikey_..." > ~/Documents/jevapi.txt     # or: export TYPESAFE_API_KEY=...
```

## Usage

```bash
python3 tranche.py fetch            # atomically replace data/pages/snapshot.json (open PRs, unauthenticated GH)
python3 tranche.py judge            # Jev pass over all PRs  (~7 questions, one call per PR)
python3 tranche.py judge --resume   # reuse only matching input/question/model bindings
python3 tranche.py dupes            # compare candidate pairs using shortened descriptions
python3 tranche.py cluster          # build out/{clusters.json,dupes.json,tranches.md,summary.json}
python3 tranche.py all --resume     # judge --resume + dupes + cluster
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

## Evidence and candidate groups

The per-PR projection includes title, author, draft status and at most 1200
cleaned body characters. Pair comparisons receive titles and at most 400 body
characters each. These calls do **not** inspect patches, test/CI results,
reproductions, merged history or full fix coverage. `finished_form` reflects
described testing, not testing performed by this pipeline. Risk/security scores
are model suggestions; their probabilities have not been independently calibrated.

The GitHub PR-list response generally omits diffstat. Missing or invalid counts
are explicitly **unknown**, never zero. Enriched legacy pages can provide real
counts, but neither input path verifies patch contents.

Title similarity (SequenceMatcher ≥ 0.72 or Jaccard ≥ 0.62) within a model category,
plus body references, proposes pairs. `same_change` with P(same) ≥ 0.65 proposes a
connection. A connected group is only model-consistent when **all** its internal
pairs were tested and agree. Contradictory, uncertain, untested or unbound internal
relationships go to `review_groups` with their diagnostics. The shared pair classifier
also exposes standalone contradictory or malformed responses in `uncertain_pairs`,
Markdown and HTML: a different-change verdict with P(same) ≥ 0.65, or a same-change
verdict with P(same) < 0.35, contradicts its probability. The middle band remains
uncertain, not contradictory. A valid different-change verdict with P(same) < 0.35
remains strong difference evidence (and a conflict inside a connected group), not
an undecided standalone pair. Invalid verdicts or probabilities are malformed.
Even a consistent
model group still needs source comparison. PR age does not select a survivor;
no member is automatically marked superseded.

## Outputs

- `out/tranches.md` — model-suggested review candidates, relationship diagnostics,
  risk/security escalation leads and possible author follow-up.
- `out/clusters.json` — matching judgments by category × model risk band
  (`low`, `core`, `danger`, `unknown`); includes source digest, head SHA and URL.
- `out/dupes.json` — `confirmed_groups` (model-consistent candidates, **not verified
  duplicates**), `review_groups` and `uncertain_pairs`.
- `out/summary.json` — counts, token usage for selected records, input binding and
  output digests. Historical `ready_*` keys now count **review candidates**;
  `superseded` is zero and `superseded_by` is null.
- `python3 gen_page.py` — render the matching report to `docs/index.html`. Refuses
  legacy, changed or mixed report inputs until `cluster` is rerun.

Review-candidate thresholds remain risk ≤ 1.5, finished_form ≥ 1.8, is_fix ≥ 0.6,
security_flag < 0.5, outside a candidate group. All required numeric fields
(including review effort) must be valid; the judgment must be current and the PR
must not be a draft. Missing judgment fields cannot qualify an item.

## Freshness and migration

`fetch` commits exact observed membership in one atomic local snapshot, including
empty results and page-boundary endings. Failed pagination leaves the previous
snapshot untouched. GitHub pagination is not a point-in-time snapshot: PRs can
change during acquisition, and this tool does not certify that a captured item is
still open when read later. `make fetch` uses the same code with `--transport curl`
for the original host's urllib/IPv6 workaround; `make all` runs stages in order.

Each new judgment binds the repository, full captured PR JSON digest (including
head SHA/updated time when provided), actual projected model input, questions,
requested model and binding version. Pair records bind both source inputs and the
pair questions. Resume reuses only matching records; closed, changed or differently
configured inputs are excluded from reports. Matching but malformed responses remain
reportable as unknown values with `normalization_errors`; they are not resume hits.
Required category, risk, finished-form, effort, fix and security answers must be valid
for judgment reuse (the advisory dupe signal is optional). Pair reuse requires a valid
verdict and finite P(same). New responses and existing JSONL caches share normalization:
invalid metrics become null, valid evidence is retained, non-finite numbers are removed,
and usage counters become nonnegative integers (invalid/missing counters become zero).
Malformed JSONL records without valid positive integer identities are ignored. Recovery
is in memory and never adds bindings to legacy records. New JSONL writes are strict JSON.
New records retain the input,
requested model, returned model/request ID when supplied, and judgment time.
The local digest detects changed captured bytes, not authenticity or live freshness.
A floating model alias such as `jev-latest` can move without changing the requested
name; use a fixed supported model name or rerun `judge` to force reevaluation.

**Published historical judgments have no bindings and cannot safely be retrofitted.**
`judge --resume` will reevaluate them, which incurs API cost. Run `judge --resume
--limit N` and `dupes --max-pairs N` to bound work per pass (`all --resume --limit N
--max-pairs N` also works). Reports explicitly count excluded unjudged/stale items.
For offline inspection only, `cluster --allow-unbound` includes legacy judgments
with warnings; they never enter review-candidate tranches. Bound-but-stale records
remain excluded even in this mode. Existing published output files are retained
as historical artifacts rather than regenerated without their original inputs.

## Offline regression checks

```bash
python3 -m unittest discover -s tests -v  # or make test
```

Tests use synthetic inputs and mocked transports/model responses. They make no
network calls, require no credentials and do not modify the published reports.
