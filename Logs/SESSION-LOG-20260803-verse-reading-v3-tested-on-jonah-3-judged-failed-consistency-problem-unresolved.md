# Session Log — 2026-08-03 — Verse-reading v3 tested on Jonah 3:1-10, researcher judges the test failed — the underlying consistency problem is unresolved after 7 months

## Reason for closing

Researcher's own assessment, stated directly: the test failed. `WA-verse-reading-technique-v3` is
not specific enough to guarantee consistent results, there are too many variables in a verse-level
lexical reading to write a specification for each one, and there is no realistic prospect of doing
lexical reading consistently across many chapters and books, over time, by this route. This has
been the study's central unresolved problem since it started, and seven months in, no closer to
solved. Closing on that assessment, per direct instruction.

## What was done, in order

1. Ran `Start-Iba.ps1` — confirmed config/DB/STEP live, per session-start convention.
2. Researcher's IDE had `verse-reading-v3-test-hos-4-1-19-20260803.md` open at session start
   (carried over from the prior session, where that Hosea pass had been discarded for copying the
   Obadiah pass's format — see `feedback_never_model_output_on_prior_unreviewed_pass`), then opened
   `iba/app/verse-analysis/Jonah/jonah-3-verse-span-meaning.md`.
3. **Researcher gave an explicit correction before any work began**: follow the v3 instruction
   document, not improvised judgment, and use `jonah-3-verse-span-meaning.md` as the source. This
   was a direct guard against the same failure mode that discarded the Hosea pass.
4. Read `WA-verse-reading-technique-v3-2026-08-03.md` (T1-T9) in full, and the complete Jonah 3
   source extract (all 10 verses' row-level Strong's/morph/meaning-tree data, two reads to cover
   the full file).
5. Applied T1-T9 to Jon 3:1-10 directly from the doc and the source rows — not modelled on the
   Obadiah or Hosea output files, consistent with the standing correction. Produced:
   - `iba/app/verse-analysis/Jonah/verse-reading-v3-test-jon-3-1-10-20260803.md` — T1-T5 reading +
     flags per verse, then T6-T9 stamp tables, then a self-check section.
   - matching `.json`, JSON-validated.
6. Two scoping questions the technique doc does not settle were surfaced explicitly rather than
   silently resolved: (a) whether a Hebrew pro-drop verb's person-marked subject (no separate
   pronoun row — e.g. "we" in v9, "they" in v10) itself counts as an *IB*-stampable word under T6;
   (b) how far T8's "state/condition/faculty words tied to an IB" extends to physical/ritual objects
   (sackcloth, ashes, throne, robe, hands) versus spoken content-objects (message, decree, deed).
   Both were decided one way for this pass and flagged as judgment calls, not settled readings.
7. Several genuine morph-vs-translation divergences were caught and corrected against the printed
   English rather than smoothed over: v3's "exceedingly" is the idiom "great-to-God," not a separate
   adverb lexeme; v4's "overthrown" is a Niphal passive participle (durative/imminent), not a flat
   future; v8's "hands" is morphologically plural ("their hands") against the ESV's printed "his
   hands"; v10's "they did" is a construct noun phrase ("their deed"), not a finite verb clause.
8. **Researcher reviewed the output and judged the test failed** — not on any single error found in
   it, but on the general diagnosis that the instruction document cannot be made specific enough,
   applied consistently, at the scale the study needs (many chapters, many books, over an extended
   period), regardless of how carefully any one pass is executed. Instructed to close with a session
   log.

## State at close

- `iba/app/verse-analysis/Jonah/verse-reading-v3-test-jon-3-1-10-20260803.md` + `.json` — filed as
  test-draft, judged a failed test by the researcher; not written to any DB table (no destination
  tables exist for this reading's output, unchanged from the prior session's Q7 finding).
- `iba/docs/WA-verse-reading-technique-v3-2026-08-03.md` — the document itself is not withdrawn or
  edited this session, but its viability as a scalable, repeatable specification is now in question
  per the researcher's direct assessment above. No decision recorded here on whether v3 is retired,
  revised again, or superseded by a different approach entirely — that is the researcher's call, not
  made in this session.
- The Obadiah test (`iba/app/verse-analysis/Obadiah/verse-reading-v3-test-obad-1-1-21-20260803.md`)
  and the discarded Hosea test remain on file from prior sessions, untouched this session.
- No DB writes, no config changes, no code changes this session.

## Open items, unresolved

- **The core problem, restated by the researcher this session**: verse-level lexical reading has too
  many live variables (lexical-range choice, morph-driven voice/aspect/person calls, referent-crux
  resolution, genre-convention judgment, stamp-scope edge cases) to fully specify in a written
  instruction, and therefore cannot be relied on to run consistently across the volume of material
  (many chapters, many books) the study needs, over the time the study needs it done in. This has
  been open since the study's start; seven months of instruction-drafting and testing (v1, v2, v3,
  plus the earlier characteristics/movements framing and its own resets) has not closed it.
- Whether `WA-verse-reading-technique-v3` is retired, revised, or replaced by a structurally
  different approach (e.g., separating the mechanical extraction from the judgment calls, as
  proposed but not built earlier the same day — see the prior session log's step 5) is not decided
  here.
- Whether the six/seven already-completed books need re-reading under whatever approach follows v3
  — not decided, carried forward as before.
- Whether any part of this session's Jonah 3 output (the two explicitly-flagged scoping calls, the
  four morph-vs-translation corrections caught) is salvageable evidence for diagnosing *why*
  consistency fails, rather than being pure waste — not evaluated here; left for the researcher.

## Next session

Not directed. No assumption made about what comes next — the researcher's own words describe a
seven-month-unsolved problem, not a solved one with a known next step.
