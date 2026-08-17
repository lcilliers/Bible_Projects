# SESSION LOG — 2026-08-05 — verse-span-meaning + T1-T3 redesign (design phase, no build)

**Trigger.** Session opened on the standing "startup iba app" routine (`Start-Iba.ps1`). The
researcher's IDE selection was open on `iba/docs/WA-verse-reading-technique-v4-2026-08-05.md`
(dated the same day), directly conflicting with `project_study_closed_20260803` (the whole study —
main DB and IBA app — closed by the researcher's own decision 2026-08-03). Flagged the conflict in
chat rather than silently treating it as business-as-usual; researcher confirmed a deliberate
reopening, specifically of the verse-lexical-reading line, rewriting v4 himself in small dictated
steps. Recorded as [[project_iba_study_reopened_20260805_v4]] — supersedes the closure memory for
this one line of work, does not reverse it.

## What happened, in sequence

1. Described the DB tables behind v4's raw-data list (`verse`, `span`, `strong`,
   `strong_meaning_tree`/`_parsed`, `strong_lsj_parsed`, `strong_mounce_parsed`, `strong_sense`,
   `strong_related`, `lemma_inventory`, `strong_verse`, `strong_lexicon`) — verified live against
   `iba.db`, not from memory/docs.
2. Traced the exact live derivation mechanism for a span's `meaning` cell
   (`lib/versespanmeaningreport.py:meaning_for_code`) — stepGloss anchor, exact-variant vs.
   base-fallback `strong_meaning_parsed`, sibling-ambiguity check with live STEP resolution, Greek-
   only LSJ/Mounce. Measured real coverage: `strong` table covers 100% of the six debate-campaign
   books but only 24.8% of Matthew — an emergent side-effect of word-by-word onboarding pulling
   whole-Bible concordances, not a deliberate corpus-coverage plan.
3. Full routine detail for `report.verse_span_meaning` produced on request — config-governed
   metadata vs. code-only algorithm split; real DB write side-effects (auto-backfill touches five
   tables + a full rebuild of three parsed tables before every render); current live entry point
   (`Chapter-Generate.ps1`, after the old standalone package was retired 2026-08-02 purely to
   resolve a step-name collision, per BUILD.md §54).
4. **Core diagnosis, researcher-led:** multi-Strong's-code spans (e.g. `G1722 G0505`, "genuine," a
   preposition+adjective idiom) render as two disconnected dictionary dumps despite `morph_code`
   already stating they're one grammatical unit — traced concretely against 2Cor 6:6 and Dan 8:1.
   Researcher identified this as the root mechanism behind the project's standing consistency
   problem: incomplete units force every downstream pass to silently reconstruct what the producing
   step should have already delivered, at uneven, unaudited cost — confirmed against the Jon 3:9-10
   v3 test, where real synthesis only happened because the reading pass bypassed the table and
   re-derived structure from raw morph/strong data itself.
5. Full design arc followed from that diagnosis — method boundary (T1-T3 mechanical/deterministic
   vs. T4-T9 interpretive, passage-scoped), producer/consumer contract, schema shape (separate rows,
   soft-delete versioning, no stored prose reading), report shape (on-demand, DB-generated),
   module registration (standalone, not folded into `chapter-generate`), `passage_debate` rework
   scope (DB-read gate swap now; T4-T9 integration explicitly deferred to the researcher), and the
   a-e rollout plan with refinements (spec-before-DDL, hard-case testing across languages/genres,
   full-corpus backfill sized at 10,241 missing codes / ≈15-20k live STEP calls, batched by book
   using the existing `cfg_book_order` sequence).
6. One self-correction recorded to memory: a draft illustration included a hedge note pointing back
   to raw source data "if needed" — caught live as the exact incompleteness pattern being fixed.
   See [[feedback_no_hedge_pointers_in_complete_records]].

## State at close

**Design only. No schema, config, or code changed this session.** Full decision record:
[`iba/app/reports/t1-t3-design-decisions-20260805.md`](../app/reports/t1-t3-design-decisions-20260805.md)
— consolidates and supersedes-in-summary the session's five other working files (listed in its own
header). That file, not this log, is the authoritative reference for anyone picking this up next.

**Explicitly open, not decided:**
- `chapter-generate`'s restructuring (retire vs. reshape once the extract step is pulled out).
- Whether the already-filled `passage_debate` docs (Hosea/Daniel/Obadiah/Jonah/Joel/Micah) get
  re-checked against the fixed T1-T3 data once it exists, or are left as historical — researcher
  instruction: "to be decided later. note the concern."
- Exact T1-T3 field shape — pending a spec pass against real hard verses (Dan 8, Jonah 3, 2Cor 6:6)
  before any DDL is cut.

**Next step, researcher-directed:** close this session with this log, clear context, begin the
build sequence (spec → schema → script → first test run) in a fresh session, starting from
`t1-t3-design-decisions-20260805.md` rather than this log or chat history.

## Memory written this session

`project_iba_study_reopened_20260805_v4`, `feedback_no_hedge_pointers_in_complete_records`
(both indexed in `MEMORY.md`).
