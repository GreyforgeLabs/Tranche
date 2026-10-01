# Decision: park before batch

Issue: [#8](https://github.com/blackopsrepl/Tranche/issues/8) — *Some PRs should be parked
before they are categorised or batched.* Status: accepted, 2026-10-01.

## Defect, measured

On the 2026-10-01 corpus (2,873 observed PRs, 2,873 current judgments, 0 stale):

| Fact | Value |
|---|---|
| Park set (draft ∪ `finished_form ≤ 1`) | **184** PRs (104 drafts, 96 low finished form, 16 overlap) |
| Batches containing ≥ 1 parked PR | **147 of 574 (26 %)** |
| Batches *led* by a parked PR | **39** (10 of them security-first-led) |
| same_change groups containing a parked member | **9 of 91** (11 PRs; 4 groups are all-draft) |
| Parked PRs that are security-flagged | **36** |

The workbench renders the same PR under *Author follow-up* and inside a batch whose
prompt orders an agent to plan a five-PR merge. A batch that claims "merge these five"
while listing a PR the pipeline itself holds for author follow-up is a contradiction in
the shipped artifact, not a policy question.

## Why full exclusion (Option A), not park-in-place (Option A′)

A′'s only advantage is protecting published batch ordinals. That invariant does not
exist in this system. Measured across the two committed runs (`9b6e7c0` → `3629017`),
driven by a 2.3 % corpus change (52 arrivals, 12 departures):

| Cross-run churn, baseline | Value |
|---|---|
| PRs keeping the same batch ID | 270 / 2,790 = **10 %** |
| Batch-mate pairs surviving | **18 %** |
| Byte-identical batches | **4 / 565 (1 %)** |

The pack is a full recomputation on every refresh. A normal refresh already invalidates
~99 % of published prompts with or without A′, so A′ would permanently embed a
per-slot exception ("4 to merge, 1 held") into 26 % of batches while protecting nothing
that survives the next run. Every future consumer (evidence packets in #9, assignment in
#5, a Fizzy surface in #7) would have to re-derive the exception per slot, per run.

The residual concern behind A′ — someone reviewing against "B012" — is solved at the
identity layer, not the packing layer: review identity binds to repository + batch
membership digest + exact head revisions (the #9 packet contract), never to an ordinal.

## Contract

1. **Park is a pre-pack gate in `merge_batches`.** Park set: draft, no current judgment
   (unjudged/stale), `finished_form ≤ 1`. Parked PRs never enter a batch.
2. **Atomic units hold whole.** A same_change group with a parked member is held out
   entirely; splitting an atomic unit would claim the surviving members twice. The group
   re-enters on the refresh after its parked member clears (author pushes → judgment
   re-binds → next `judge --resume`).
3. **Park is a hold, never a close.** Every parked PR has a named unblock path and
   re-enters automatically. No GitHub writes; closing stays a maintainer call.
4. **First-class output.** `out/parked.json` (format_version 1, bound to the same
   `dupes_digest` as `batches.json`), its own workbench queue, a park section appended to
   `tranches.md`. Same discipline as the security meta-category: membership never
   replaces the PR's own category.
5. **Security interplay.** Park removes a PR from merge batches only. The security queue
   still lists security-flagged parked PRs, annotated.
6. **Invariants, enforced.** `merge_batches` asserts no batch member is parked;
   `gen_page.py` refuses stale/foreign/missing `parked.json`; the MCP server serves
   parked state computed by the same policy function.
7. **Invalidation contract, stated.** Batches recompute on every refresh; reviewers bind
   to membership digest + head SHAs, never to `B0xx`.

## Effect on the current corpus

Shipped in v0.5.0: 533 batches (520 full), 2,650 PRs packed, **192 parked** — 104
drafts, 96 without finished form, and 19 members of 9 same_change groups holding
whole for a parked member. 36 parked PRs are security-flagged and stay in the
security meta-category. Every batch park-free by construction. Batch count shifts
are the documented cost of every refresh; the change makes every future batch mean
exactly what its prompt says.
