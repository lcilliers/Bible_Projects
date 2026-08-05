# verse-span-meaning + T1-T3 — design decisions of record, 2026-08-05

Consolidated from the full working session. Supersedes nothing on disk yet — no schema, config, or
code changed. This is the decision record to build from once the researcher moves to execution.
Related working files from the same session: `verse-lexical-tables-20260805.md`,
`verse-span-meaning-db-capture-question-20260805.md`, `versespanmeaning-routine-detail-20260805.md`,
`t1-t3-before-after-illustration-20260805.md`, `t1-t3-rollout-plan-review-20260805.md`.

## The core diagnosis

`report.verse_span_meaning` fetches everything it needs (`morph_code`, compound `strong_variant`
codes, stem-segmented `strong_meaning_tree` text) but never closes the loop between what it fetches
and what it renders — multi-code spans render as unconnected dictionary dumps, morph-driven stem
selection never happens. This forces every downstream reading pass to silently reconstruct that
structural work itself, ad hoc, un-persisted, every verse, every time — the root mechanism behind
the project's standing consistency problem (confirmed against the Jon 3:9-10 v3 test: real
synthesis happened there, but only by the reading pass bypassing the table and re-deriving from raw
morph/strong data itself).

## Method boundary (governs the whole design)

- **T1-T3 = mechanical, deterministic, no interpretation.** Row-level reading, full lexical range,
  morph-driven voice/person/aspect, compound-span unit-grouping. All of it is grammar fact already
  sitting in the fetched data — no AI judgment required, no LLM call needed to produce it.
- **T4-T9 = interpretive**, requires an AI/researcher reading pass. Referent cruxes with multiple
  live readings, genre-conventional observations, sense selection among genuinely live options,
  IB/Agent/Process/Action stamping. Must be considered **at passage level, not per-verse** — cross-
  verse referent chains (Jon 3:9 "we" / 3:10 "them" both resolve back to v5) need read access to
  neighbouring verses' resolved records, not just the current one.
- The two must stay mechanically separate (matches this app's own standing principle — Claude Code
  mechanical, Claude AI/researcher analytical). Merging them would make the "mechanical" layer
  depend on an LLM every run, reintroducing the cost/drift problem the study closed over.

## Producer/consumer contract

- `verse-span-meaning + T1-T3` runs standalone, independent of T4-T9 and all subsequent analysis —
  no awareness of what reads it downstream.
- Its DB record must be **complete in grammatical fact** (everything T4-T9 needs, so raw
  `span`/`strong`/`morph_code` is never touched again downstream) — but must **not** resolve what's
  genuinely interpretive (named as live options, not narrowed). A "complete" record must never hedge
  with "see raw data if needed" — resolve it or flag it unresolved, no quiet third option
  ([[feedback_no_hedge_pointers_in_complete_records]]).

## Schema shape

- **Separate rows per span/unit** — not a single text column on `verse` (one-to-many can't fit a
  scalar column; prose also isn't machine-queryable back into structured fact).
- **No separately stored verse-level prose reading** — the compiled verse is assembled by ordering
  the resolved rows by `position`, rendered on demand. Same principle as MD-as-report (below):
  derived, never itself a source of truth.
- **Version-aware writes**: insert the new row, soft-delete the superseded row (`deleted=1`) — the
  same convention already used by every other table in `iba.db` (`verse.deleted`, `span.deleted`,
  `strong.deleted`, etc.), not a new mechanism. Uniqueness for "the current row" must be scoped to
  `deleted=0` (this app already has the mechanism — `cfg_unique`).
- Field shape to be **spec'd against real hard verses first** (Dan 8's multi-stem verbs, Jonah 3's
  dense Hebrew compounds, 2Cor 6:6's content-empty function-word component), *then* DDL cut — not
  designed on paper first. Schema itself is `cfg_table`/`cfg_column`-governed, via
  `configmaint.propose`, same as every other schema change traced this session.

## Report

- **On-demand**, scoped by passage or book (matches existing `-Book`/`-Range` call shape — no new
  invocation model needed).
- **MD is a generated report off the DB**, not an independent write — DB is sole source of truth.
  Layout: EV text and lexical text placed together (exact pairing TBD against the field-shape spec).

## Module registration — DECIDED

- **New standalone module**, not folded into `chapter-generate` — resolves the fork raised mid-
  session. New `cfg_work_package`/`cfg_step`, registered independently (this app allows a step name
  under only one active work package at a time — validated live, `configmaint.validate`).
- Old `report.verse_span_meaning` step **retired** (`inactive=1`) — same governed path already used
  to retire `verse-analysis-report`/`passage-debate-report` (BUILD.md §54).
- **`chapter-generate` needs restructuring or retirement** — it exists only to chain the old extract
  step into `report.passage_debate`; with the extract pulled out, a 2-step chain of one step is an
  orphaned artifact. Not resolved — flagged for whenever this is built.

## `report.passage_debate` — re-invigorated, DB-sourced, reworked (SCOPED, split in two)

- Traced precisely: `BaseExtractMissing` today is a bare `extract_path.exists()` filesystem check —
  `passagedebatereport.py` already re-derives verse/gap data straight from the `verse` table itself;
  the MD file was only ever a completion gate, never actually read for content. So swapping the gate
  for a DB-existence check against the new table is a small, bounded change, not a rewrite of how it
  sources verse data.
- **What happens now (when this gets built):** swap the gate check to read from the DB; park or
  deactivate whatever in `passage_debate` is now divorced from the old module.
- **What's explicitly deferred to the researcher, after the new module has run through:** the actual
  rework combining T4-T9 with the current `passage_debate` structure. Not Claude Code's task at
  build time — noted here so it isn't silently attempted.

## Rollout (a-e, as refined)

- a) Spec-then-schema, config-governed (above).
- b) DB is source of truth, MD is a generated report (above).
- c) Test against hard cases specifically — multi-stem Hebrew verbs, dense compounds, Greek, mixed
  genre. An easy passage proves nothing.
- d) Backfill of already-completed books (Dan/Hosea/Obadiah/Jonah/Joel/Micah/Amos) — **agreed to
  happen**, batched by book.
- e) Full-corpus completion — **agreed, no principled blocker.** Sized: 10,241 distinct Strong's
  codes (6,110 Hebrew, 4,131 Greek) still need live-STEP backfill for full coverage, ≈15-20k live
  calls. **Batched by book, break at each book boundary** (researcher's call, overriding this
  session's earlier "bulk first" suggestion) — reuses the existing per-book architecture and
  `cfg_book_order` sequence rather than building new bulk-processing machinery; gives a clean
  resume point if interrupted, at the cost of `strong_meaning_parsed`/`strong_lsj_parsed`/
  `strong_mounce_parsed` being fully rebuilt once per book (accepted trade-off, not a blocker).
- **Old MD extracts get archived only after the new DB write is generated AND cross-checked against
  the old MD** — not archived pre-emptively, not left live indefinitely either. Sequencing decided
  this session: DB write → cross-check → archive.

## Explicitly open / deferred — tracked, not lost

1. **`chapter-generate`'s restructuring** — needs a decision when this is built (retire vs. reshape).
2. **Already-filled `passage_debate` docs** (Hosea/Daniel/Obadiah/Jonah/Joel/Micah) were built on the
   *old* extract. Whether they get re-checked against the fixed T1-T3 data, or left as historical —
   **to be decided later.** Concern noted per researcher's explicit instruction, not to be
   forgotten or defaulted past.
3. Exact field-shape of the T1-T3 record — pending the spec-against-real-verses pass in (a).
4. Exact standalone-vs-folded registration mechanics for the new module and `report.passage_debate`
   — pending build time.
