# WA — Session log: Psalms first macro view

**File:** `WA-session-log-psalms-macro-v1.0-2026-07-14.md`
**Date:** 2026-07-14
**Breakpoint:** end of first macro pass; awaiting researcher decision on Q-1…Q-4.
**Outputs this segment:** `WA-psalms-macro-view-v1.0-2026-07-14.md`, `WA-psalms-macro-tables-v1.0-2026-07-14.json`
**Prior outputs referenced:** `README-preamble.md` + four supplied Psalms projection CSVs (no earlier WA output was available in this session).

---

## 1. Researcher instruction (verbatim)

> "The next task is to use the lexical analysis of Psalms which are captured in the README. familiarise yourself and then proceed with the first macro view of the inner being characteristics as captured in Psalms."

Standing instructions in force: observe-don't-impose; distinguish observation / interpretation / reflection; no external sources unless invited; flag insufficiency; pause at interpretive choices; measurement informs but never decides; a movement of one is a movement; prefix WA; version control; session log at breakpoints.

## 2. What was done — the working sequence

1. Read `README-preamble.md` in full. Registered its two governing warnings: (i) `NONE` (assessed silence) ≠ `ABSENT` (unread) — "the single most important error to avoid"; (ii) the three layers — lemma base gloss / meaning-in-context / occurrence — must not be collapsed.
2. Profiled all four CSVs directly (no sampling; full-file aggregation).
3. Established coverage, type, direction, locus, device, object_kind, cluster, tag and edge distributions.
4. Cross-checked the flattened `reading_view` against `dimensions_long` at span level.
5. Wrote the macro view and the companion table file.

## 3. The debate — thinking, including the wrong turns

**First reading of the dimension fill looked like a contradiction.** `effect` was NONE in 2,118 of 2,168 rows, yet the README declares the retrofit COMPLETE with 0 `ABSENT`. I initially read this as a projection failure. It is not: the README's own definition makes NONE an *assessed* value. The retrofit claim and the 97.7% NONE rate are consistent. **But that resolution is exactly what makes it interesting** — it converts a suspected bug into a substantive claim about the book: Psalms records the movement and withholds the outcome. I did **not** accept that claim; I escalated it as Q-1, because an under-read dimension and an assessed silence are indistinguishable from the data supplied, and the whole of any future consequence-analysis rests on which it is.

**Second: `locus` failed its own enum in 666 rows.** My first hypothesis was projection error. Checking `dimensions_long` at span 268779 (Psa 100:1) showed ve-112 (`coupling`) holding `external:god` and ve-116 (`locus`) holding "paired with serving with gladness" — i.e. the fields are **transposed at source**, and the projection is faithfully carrying the transposition through. Logged as DQ-01. I chose to normalise *in analysis*, declared, rather than silently repair — and to put the source-fix decision to the researcher (Q-2).

**Third: a self-caught imposition risk.** The strongest-looking finding (I-1: the inner being in Psalms moves God-ward) converges neatly with the reset methodology's own premise that the inner being is a traffic, not an anatomy. I flagged this against myself in §3 of the macro view: we built a column called `direction`, so we found directions. Convergence with one's own hypothesis is not evidence for it. The finding stands as a **candidate**, not a conclusion.

**Fourth: I nearly asserted a verse-count denominator (2,461) from memory to compute a coverage percentage.** It is not in the supplied data. Under the no-external-sources instruction I removed it from the table file and replaced it with an explicit request for the verse universe. This is now GAP-2 and the most important missing datum in the pass.

**Fifth: the frequency trap.** The top-30 characteristic list is seductive (heart 77, praise 73, soul 65). But 385 of 657 characteristics (58.6%) occur exactly once. Under the singleton rule, the majority of the book's distinct content is in the tail. Recorded as I-7 so that no later pass mistakes the head of the distribution for the book.

**Sixth: Psalm 119.** 244 readings, 11.3% of the book. Every unstratified figure in §1 is potentially a Psalm-119 figure. Flagged (I-8) and explicitly marked as **not yet done**.

## 4. Findings carried forward

- I-3 (`faculty` ↔ `inward`: 54 of 108 faculty readings are inward, against a 7.5% book-wide inward rate) is the strongest structural asymmetry found and the leading movement candidate.
- I-6 (seat named in only 4.8% of readings) bears directly on the programme's spirit–soul–body boundary question: at the point of the movement, the text mostly does not draw the boundary.
- 403 `READ-EMERGENT-2026` readings (characteristics the old model missed) are, per the README, a finding in themselves and have not yet been examined.

## 5. Decisions taken

- Counted **readings** as the unit for this pass (declared; alternatives put to the researcher as Q-3).
- Normalised locus in-analysis rather than patching source (declared; source-fix put as Q-2).
- Refused to assert any figure not derivable from the supplied files.

## 6. Open questions to the researcher

- **Q-1** `effect` 97.7% NONE — assessed genre-silence, or under-read dimension?
- **Q-2** DQ-01 transposition — issue a `.json` patch for CC, or continue with declared normalisation?
- **Q-3** Governing unit for the next pass — readings / verses / characteristics / lemmas?
- **Q-4** Next move — (i) the 385 singletons, (ii) the faculty↔inward asymmetry, (iii) the edge graph?

## 7. Next steps (pending Q-4)

1. Re-run §1 tables with Psalm 119 excluded (control for the outlier).
2. Request: the qualifier/standalone rows; the verse universe; `WA-projection-schema-and-companion-spec-v1-20260714.md`; the Proverbs projection as contrast control.
3. Only then: begin movement work across the four-level cascade.

---
*End of session log.*
