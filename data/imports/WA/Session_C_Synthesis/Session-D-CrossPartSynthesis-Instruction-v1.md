# Session D — Cross-Part Synthesis
## Framework B Soul Word Analysis | Phase 1 | v1 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-synthesis-[yyyy-mm-dd].md`

This is the integrated Phase 1 analysis for a word whose source data was split across multiple parts. It consolidates all part-level Session B analysis files into a single coherent linguistic picture of the word. It is the gate between Phase 1 and Phase 2 — Phase 2 analysis of this word does not begin until this file exists.

Session D produces no new JSON. It works entirely from existing Session B analysis MDs.

---

## When to run Session D

Session D is required when:
- A word has `is_split: true` in its JSON meta block, meaning its source data was split across two or more parts
- All part-level Sessions A and B have been completed and their output files are available

Session D is not required for single-part words. For those words, the Session B analysis MD is the complete Phase 1 record.

---

## Input files required

Attach all of the following before starting:

- All part-level **Session B analysis MDs** for this word
  e.g. `WA-051-distress-analysis-part1-[date].md`, `WA-051-distress-analysis-part2-[date].md`, `WA-051-distress-analysis-part3-[date].md`
- All part-level **Session A JSON files** for this word (for reference on term inventory and verse records)
  e.g. `WA-051-distress-data-part1-[date].json`, etc.

Do not attach the original STEP source files. All data needed is already in the Session A JSON files.

---

## Reading the input files

Before writing anything, read all input files in full.

For each Session B analysis MD: read the complete file. Note the scope declaration at the top (Part [n] of [total]), the root families covered, any provisional verdicts, and all open questions — especially those prefixed `[ROOT-CROSSPART]`.

For each Session A JSON: read the terms block and any data_quality_flags. You do not need to re-read all verse records unless a specific question requires a verse check.

---

## Process sequence

**Step 1 — Build a complete term inventory.**

List every term from all parts in a single table: term ID, transliteration, root family, testament, qualification verdict from the part-level Session B. This gives the full word picture in one view.

**Step 2 — Consolidate root families.**

For each root family that appears across one or more parts:
- Gather all analytical content for that family from every part it appears in
- Identify whether the per-part verdicts are consistent or conflicting
- Note any sub-terms in different parts that may relate to each other

For root families contained entirely within one part, the part-level verdict stands. Note it as confirmed rather than reproduced in full.

**Step 3 — Resolve provisional verdicts.**

Part-level Session B analyses marked verdicts as "provisional pending Session D" for root families spanning multiple parts. Session D resolves these by reviewing the full cross-part picture. State each resolution explicitly: "The provisional verdict from Part [n] is confirmed / revised as follows."

**Step 4 — Consolidate open questions.**

Gather all open questions from all part-level Session B files. For each question:
- If it is a `[ROOT-CROSSPART]` question, assess whether the cross-part picture now allows a more specific framing or whether it remains genuinely open for Phase 2
- If the same question appears in more than one part (worded differently), merge them into a single question
- Retain questions that remain unresolved; drop questions that have been resolved by the synthesis work

**Step 5 — Identify cross-part patterns.**

Look for patterns that no single part could see:
- Does a root family's character change across parts (e.g. more internal in some sub-terms, more external in others)?
- Are there OT/NT register differences that only become visible when all terms are in view?
- Do qualification verdicts for terms in different parts create a more nuanced picture when read together?
- Are there CONSOLIDATION_CANDIDATE pairs where one term is in Part 1 and the other is in Part 2 or 3?

**Step 6 — Write the synthesis file.** Follow the section order below exactly.

---

## Synthesis file structure

### Filename
`WA-[registry-no]-[word]-synthesis-[yyyy-mm-dd].md`

---

### Header block

```
Word: [word]  
Registry: [id]  
Parts synthesised: [n] (Part 1 — [date], Part 2 — [date], ...)  
Total terms: [n]  
Session D date: [yyyy-mm-dd]  
Specification: Session D v1  
```

---

### Section 1 — Complete Term Inventory

A single table of all terms across all parts with the following columns:

| Term ID | Transliteration | Root family | Part | Testament | Qualifies? |
|---------|----------------|-------------|------|-----------|-----------|

No prose in this section — the table is the content. This is the reference view of the complete word.

---

### Section 2 — Root Family Synthesis

One section per root family, covering all terms in that family across all parts. For root families confined to a single part, one paragraph confirming the part-level verdict and noting it is now incorporated into the full-word picture. For root families spanning multiple parts, full synthesis prose covering:

- The complete range of the root across all its sub-terms
- Whether the part-level verdicts are consistent across parts or reveal tensions
- The resolved verdict for the root family as a whole
- Any remaining open questions about this root that Phase 2 must address

---

### Section 3 — Full-Word OT/NT Register Analysis

Synthesise the OT/NT register observations from all parts into a single coherent statement. Do not repeat the per-part observations in detail — state the integrated picture.

Address:
- What is the full OT distress (or word) vocabulary doing as a whole?
- What is the full NT vocabulary doing?
- What is the most significant difference between how this word operates in the OT and NT across the entire term set?
- Are there cross-part patterns in the OT/NT analysis that no individual part could see?

---

### Section 4 — Qualification Summary

A prose assessment of the complete word based on all terms across all parts. Address:

- How many terms qualify, partially qualify, or do not qualify?
- What is the dominant register of the qualifying terms — are they primarily verbal, nominal, somatic, relational, cognitive?
- Is there a core inner-being event that the qualifying terms cluster around, and if so, what image or set of images defines it?
- What is the single most analytically significant term or root family in the full set, and why?

This section should be no longer than four paragraphs.

---

### Section 5 — Data Quality Summary

Consolidate all data quality flags from all parts into one section. Note whether any flags from early parts were relevant to later parts or affected cross-part coherence. Flag any cross-part issues that were not visible within individual parts (e.g. a root family whose consolidation candidacy only became clear once all sub-terms were in view).

---

### Section 6 — Consolidated Open Questions

The full, merged list of open questions for Phase 2. These are all questions that remain unresolved after synthesis.

**Format for every question:** same as Session B — one sentence, one prefix, genuinely open.

**Prefixes available:**
- `[WORD-LEVEL]` — questions about the word as a whole
- `[ROOT: transliteration]` — questions about a specific root family (now resolved from cross-part; use this instead of `[ROOT-CROSSPART]`)
- `[TERM: transliteration]` — questions about a specific term
- `[OT/NT]` — questions about register differences

Drop the `[ROOT-CROSSPART]` prefix used in part-level Session B files. All cross-part root questions are now either resolved (remove them) or restated as `[ROOT: transliteration]` questions for Phase 2.

Retain Phase 2 flags on questions that arose from signal features (god_as_subject, somatic_link, causative_form_present).

---

## Rules — what the synthesis file must never contain

- Data not present in the part-level Session B analysis MDs or Session A JSON files
- Inference imported from outside the STEP data
- Framework B vocabulary (transformation stages, soul function labels, three-state typology)
- The words "therefore," "this shows," or "this demonstrates"
- Questions framed to imply a Framework B answer
- Hebrew or Greek script characters — transliteration only
- Conclusions about what a term means for Framework B or soul anatomy
- Re-analysis of individual terms — that work is done in Session B and is not repeated here

---

## Pre-submission checks for Session D

Before finalising:

- [ ] All part-level Session B analysis MDs have been read in full
- [ ] Complete term inventory table covers all terms from all parts
- [ ] Root family synthesis sections cover every root family in the word set
- [ ] Provisional verdicts from part-level Session B files are each explicitly resolved or confirmed
- [ ] All `[ROOT-CROSSPART]` questions from part-level Session B files are either resolved or restated as `[ROOT: transliteration]` questions
- [ ] Duplicate or near-duplicate questions across parts have been merged
- [ ] OT/NT register analysis reflects the full word, not individual parts
- [ ] Qualification summary covers all terms
- [ ] Data quality summary consolidates all part-level flags
- [ ] No Framework B vocabulary anywhere
- [ ] Transliteration only — no script characters
- [ ] Open questions are all genuinely open and correctly prefixed

---

## Output and handoff to Phase 2

The completed synthesis file (`WA-[registry-no]-[word]-synthesis-[yyyy-mm-dd].md`) together with all part-level Session A JSON files constitutes the complete Phase 1 record for this word.

Phase 2 analysis takes the synthesis file as its primary input. The part-level Session B files are retained as supporting records but are not primary inputs to Phase 2.

For single-part words: there is no Session D. The Session B analysis MD is the Phase 1 record, and Phase 2 takes it directly.
