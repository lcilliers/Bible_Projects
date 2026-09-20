# Escalation #1767 — two-tier (map-reduce) redesign for `cluster.reading` — build proposal

**Not built.** This is the proposal you asked for (v2: "propose a build for this two tier
process"), grounded in the live schema and today's actual char-reading data — not built or run
this session, per your v1 instruction ("don't try to fix it in this run").

## Why (recap, so this stands alone)

M83 subgroup A hit a case #1761's surface-split fix can't cover: **two member strongs
simultaneously over the occurrence cap** (`MultipleOverCapStrongs`). The surface-split fix assumes
exactly one over-cap strong per subgroup, with every other member riding along unpartitioned for
cross-strong comparison — that assumption breaks the moment two strongs are both over cap at once.
Your own diagnosis: this gets worse as more/larger clusters run, so the real fix is structural, not
another one-off patch.

## Current shape (Stage 3 / `char-reading`, live today)

One call per subgroup: every member strong's full occurrence set goes into a single prompt, model
returns one `ib_observation` row per strong (`question_code=NULL`, free-form narrative, up to
~1,200 chars live today — checked, not assumed). No batching, no resumability below the
whole-subgroup grain. This is exactly what breaks under the over-cap case and what won't scale as
clusters grow.

## Proposed two tiers

**Tier 1 — batch reading.** Resolve the WHOLE subgroup's occurrence set across every member
strong together (not siloed per-strong like #1761's split), batch by VERSE the same way Stage 1
(`lexical.meaning`) already chunks — reuse its existing cost-estimation/batch-sizing infrastructure
(`lexical.llm_max_cost_per_batch`, `lexical.llm_rate_input_per_million` etc., already `cfg_setting`-
driven) rather than inventing new sizing logic. Each batch reads its verses and writes grounded
`ib_observation` rows — **proposed:** new stage value `char-reading-tier1` (keeps Tier 1's output
queryable/countable separately from today's `char-reading`, and keeps `_strongs_needing_battery`-
style "any row = covered" logic unambiguous once Tier 2 exists) — same `batchcontrol` resume/skip/
crash-safety mechanism #1756 already built for `lexical.meaning`/`cluster.reading`.

**Tier 2 — synthesis over Tier 1.** A SEPARATE call per subgroup, reading Tier 1's OWN
`char-reading-tier1` observations for that subgroup (not raw verse text again) — condensed input,
so it comfortably fits one call regardless of how many strongs/occurrences the subgroup has. This
call's output IS today's `char-reading` narrative (kept as the stage name — no rename, minimizes
downstream disruption to anything already reading `stage='char-reading'`, e.g. `char-answers`'
existing input assembly).

This closes both problems structurally: the two-simultaneously-over-cap-strongs deadlock (Tier 1
never holds more than one batch's occurrences at once, so "over cap" stops being a per-call
blocker at all), and the general scaling concern (Tier 2 always reads a bounded, condensed input
no matter how large the subgroup).

## Open questions this proposal does NOT resolve unilaterally

1. **Tier 1 batch size** — reuse Stage 1's existing verse-count chunking as a default, or does
   Stage 3's cross-strong-comparison need differ enough to warrant its own cap? (Recommendation:
   start with the same default, tune from real behaviour once M83 subgroup A actually runs through
   it — matches this session's own working pattern for #1761.)
2. **Does Tier 2 supersede Tier 1's rows, or do both stand as permanent records?** Recommendation:
   both stand — Tier 1 rows are real grounded findings in their own right (same status as any
   other `ib_observation`), Tier 2 is a distinct synthesis layer on top, not a replacement. Matches
   how `char-answers` already treats `char-reading` (reads it, doesn't delete/supersede it).
3. **Re-reads** — you already said M49/M83 (and likely other already-processed clusters) will
   probably need re-reading once this lands, since single-call Stage 3 is being superseded, not
   supplemented. Scope of "which clusters need a re-read" not assessed here — a separate pass once
   this is approved and built.

## What I'd actually build, in order, once approved

1. `cfg_enum ib_observation.stage` — add `char-reading-tier1` (a `configmaint.propose`).
2. `charreadinggenerate.py` — new `assemble_tier1_batches` (verse-chunked, mirrors
   `lexical.meaning`'s own batch assembly) alongside the existing subgroup-package assembly (kept,
   becomes Tier 2's own assembly once Tier 1 exists).
3. `handlers/cluster.py`'s `reading` — rewritten to run Tier 1's batch loop (batchcontrol-tracked,
   same shape as `cluster.reading`'s existing multi-package loop from #1761) then, once every Tier 1
   batch for a subgroup commits, run Tier 2 as a single follow-up call reading Tier 1's own rows.
4. Verify against M83 subgroup A specifically (the case that motivated this) before touching any
   already-completed cluster's re-read.

Not started. Waiting on your direction on the 3 open questions above (or "proceed with your
recommendations" if you'd rather not adjudicate each one separately).
