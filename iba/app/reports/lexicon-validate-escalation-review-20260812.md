# Review — paused `lexicon.validate` escalation (RUN-20260811_172851_742-LEXICON-PARSE)

> Re-evaluation requested 2026-08-12, re-establishing context after the 08-11/12 power-failure
> session before acting on any of its "left open" items. Investigated against the live DB and code,
> not against BUILD.md's summary alone.

## What is actually paused

- **Run:** `RUN-20260811_172851_742-LEXICON-PARSE` (`run.id` 1583), work package `lexicon-parse`,
  step `lexicon.validate`, started `2026-08-11T16:28:52Z`, state `paused` — a standalone
  `-Step Validate` invocation, not chained after Parse/Related in this run (see below).
- **Escalation:** `escalation.id` 607, `state='raised'` (not yet answered), full question text:

  > "Lexicon-parse coverage/value-quality findings: 2 strong_lexicon row(s) with no
  > strong_lsj_parsed output, 2 with no strong_mounce_parsed output, 2 strong row(s) with no
  > strong_related fetch attempted yet, 0 value-quality violation(s) across the 4 tables. Approve to
  > acknowledge as current/known state, reject to flag for action (most likely re-running
  > lexicon.parse/lexicon.related), or revise with a comment."

- Full detail report: [`lexicon-parse-v1-20260811.md`](lexicon-parse-v1-20260811.md).

## What the "6 gaps" actually are

Traced each of the three counts to its exact rows (not just the aggregate numbers in the report).
**All six trace to the same two Strong's codes: `G6507` and `G7167`** — both `strong_lexicon`
rows missing `strong_lsj_parsed`, both missing `strong_mounce_parsed`, and the same two `strong`
rows missing a `strong_related` fetch. This is 2 codes short of full coverage, not 6 independent
gaps.

- `G6507` = ἀποτύφλωσις ("making blind" — LXX Zech 12:4 only). `G7167` = ἐκτυφλόω ("make quite
  blind"). Both belong to `word_strong.word_id=183` → **`word_registry` "blindness"** (status
  `raw-complete`), onboarded via `new-word` run `RUN-20260811_055200_755-NEW-WORD`, completed
  `2026-08-11T04:52:05Z` ("validation PASSED").
- **Both have zero `strong_verse` rows** — confirmed against all 14 of blindness's Strong's codes:
  12 have verse occurrences (2–135 verses each), only these two have none. This is not a fetch
  shortfall: `raw.verses` reported no shortfall and `raw.validate`'s parse-check passed clean for
  this run, so STEP genuinely returns 0 indexed verses for these two Greek codes (LXX-cited-only
  lemmas that never surface as a span tag in STEP's ESV-keyed text).
- **0 value-quality violations** anywhere across the 4 parsed/related tables — confirmed directly
  against the escalation's own `preset` and the report.

## Why they're unparsed/unfetched — root cause, not a data defect

Re-ran `lib.lexiconparse.lsj_rows()`/`mounce_rows()` against the live DB right now: **both codes
parse cleanly** (sensible headword + sense rows for both) — the parser is not broken and there is
nothing malformed about this pair's raw LSJ/Mounce text.

The actual cause is a pipeline-wiring gap:

- `lexicon.parse`/`lexicon.related` are **standalone** steps (`Lexicon-Parse.ps1 -Step Parse` /
  `-Step Related`), invoked manually — never auto-chained after `new-word`. Confirmed via
  `cfg_step`: the `new-word` work package is exactly 7 steps, `registry.exists` →
  `registry.create` → `raw.discover` → `raw.detail` → `raw.verses` → `raw.write` →
  `raw.validate` — no parse/related/lexical step anywhere in it.
- `handlers/raw.py` already contains `related()` (step `raw.related`) and `lexical()` — both
  written specifically to close this exact class of gap, with docstrings citing **BUILD.md sec98,
  2026-08-10 ("`receive`")**: *"the `new-word` chain had no step that populated `strong_related` at
  all... Per-word onboarding silently left every newly-registered code without its related-terms
  fetch until someone happened to check."* **Neither function is registered in `cfg_step` for any
  work package today** — confirmed by an exhaustive search (only `raw.backfill_meaning` uses
  `handlers/raw.py` outside the `new-word` chain). They are dormant code left over from `receive`,
  which BUILD.md §1 (this session's recovery log) records was **rolled back** on 2026-08-10 on a
  relevance judgement call, and whose **rebuild** is explicitly one of this session's still-open
  items (§3 below).
- This is exactly what the paused run caught: `-Step Validate` was run in isolation on 2026-08-11
  without a preceding `-Step Parse`/`-Step Related` re-run, so blindness's two newly-added codes
  (added 04:52, six hours before this validate run) were never picked up.

## Re-evaluation — Approve vs. Reject

The escalation's own two named options:

- **Approve (acknowledge as known state):** defensible for *these two specific rows* — zero verse
  occurrences means they can never enter `verse_lexical`/HIB/phenomenon work regardless of parse
  status; this is a completeness gap with no analytical consequence today.
- **Reject (flag for action, "most likely re-running lexicon.parse/lexicon.related"):** would clear
  these two rows, but **would not fix the underlying gap** — the next word onboarded through
  `new-word` will hit the identical gap again (for codes that may well have real verse occurrences
  next time), because the chain itself still has no parse/related/lexical step.

**Recommendation:** Approve this specific escalation as known state (truly zero-risk: 2 codes, 0
verse occurrences, 0 value-quality findings) — but treat that as separate from, not a substitute
for, the systemic fix. The systemic fix is already queued as this session's own **"`receive`
rebuild"** open item (a fresh build of the `raw.related`/parse-refresh/`lexical` wiring into
`new-word`, not a rollback-undo) — this escalation is direct, current-data evidence that the gap
`receive` was built to close is real and already recurring. Sequencing this rebuild before the next
`new-word` run would prevent a third occurrence.

This is a judgement call, not a standards violation — decision is the researcher's.
