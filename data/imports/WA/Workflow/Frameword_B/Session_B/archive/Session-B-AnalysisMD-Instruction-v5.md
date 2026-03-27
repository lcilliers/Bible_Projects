# Session B — Analysis MD Production
## Framework B Soul Word Analysis | Phase 1 | v5 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-analysis[-part[n]]-[yyyy-mm-dd].md`

This is the prose analysis file. It holds the written linguistic and lexical observations drawn from the JSON data file produced in Session A. It does not reproduce the structured data — it interprets it in plain prose, organised by root family.

---

## Multi-part words — read this before starting

If the JSON file has `is_split: true`, you are producing a **part-level analysis**. Before writing anything, state the following at the top of the file and at the start of your session:

> "This Session B covers Part [n] of [total] for the word [word]. Analysis is scoped to the terms and verses in this part file only. Root families that also appear in other parts are noted where relevant; cross-part synthesis of those families belongs in Session D."

**Scope rule for multi-part words:**
- Analyse only the terms and verses in this part's JSON
- Do not import analytical content from other parts
- If a root family in this part also appeared in a prior part (check `root_families_in_prior_parts` in the meta block), note this explicitly in the root family section: "This root family also appears in Part [n]. Root-level conclusions should be treated as provisional until Session D cross-part synthesis is complete."
- Open questions about root-level behaviour (spanning all sub-IDs across parts) should be prefixed [ROOT-CROSSPART] rather than [ROOT: transliteration] and flagged as requiring Session D before they can be answered

---

## Input files required for this session

**One file only:**

- **The completed JSON file from Session A** — `WA-[registry-no]-[word]-data[-part[n]]-[yyyy-mm-dd].json`

Do not attach or read the STEP source file. The JSON is the only source for this session. Everything you need — term meanings, verse texts, root family groupings, occurrence counts, testament coverage, and signal feature flags — is already in the JSON. If something is not in the JSON, it does not belong in this file.

---

## Reading large JSON files

Before reading the JSON file:

1. Check the file line count: `wc -l [filepath]`
2. If the file exceeds 3,000 lines, read it in sequential blocks using explicit line ranges
3. Read the terms block first (typically the first 10–20% of the file)
4. Then read the verse_records block in batches
5. Confirm the final block has been read before writing anything
6. Note any truncated view outputs — if a view call returns a truncation warning, re-read that range with a narrower window before proceeding

---

## Process sequence — follow this order exactly

**Step 1 — Read the JSON file in full.** Work through every term entry and every verse record before writing anything. If the file is large, read in sequential blocks per the rule above. Note the root family groupings, the testament field on each term, the three signal feature fields, and any `root_families_in_prior_parts` entries.

**Step 2 — State scope.** For multi-part words, write the scope declaration described above. For single-part words, proceed directly.

**Step 3 — Group the terms by root family.** The `root_family` field on each term entry tells you which family it belongs to. Terms with `root_family: null` stand alone. Write down the complete list of families and which terms belong to each before starting to write.

**Step 4 — For each root family, plan the within-family analysis.** Look at the verse_records for each term in the family and identify: does the verse set for each sub-term cluster around a different type of situation, a different subject, or a different inner-being function? If yes, note what the difference is. If no, note that the terms appear functionally similar.

**Step 5 — Plan the OT/NT analysis.** Check the `testament_coverage` field in meta. If the word has terms in both Testaments, identify: what does the OT vocabulary do that the NT does not, and vice versa? Base this only on the verse records in the JSON.

**Step 6 — Identify signal features.** For every term where any of the three signal feature fields is true — `god_as_subject`, `somatic_link`, `causative_form_present` — plan what the analysis will say about that feature and what open question it raises. Every signal feature must produce at least one open question in Section 6 with a Phase 2 flag attached.

**Step 7 — Check for SMALL_VERSE_SAMPLE flags.** For any term flagged as SMALL_VERSE_SAMPLE in the JSON's data_quality_flags, note in the analysis that register assessments for that term are limited by the sample size, and generate an open question calling for a fuller verse set in Phase 2.

**Step 8 — Write the file.** Follow the section order below exactly.

---

## Analysis MD file structure

### Filename
Single-part word: `WA-[registry-no]-[word]-analysis-[yyyy-mm-dd].md`  
Multi-part word: `WA-[registry-no]-[word]-analysis-part[n]-[yyyy-mm-dd].md`

---

### Header block (multi-part words only)

At the very top of the file, before Section 1, insert:

```
**Part scope:** Part [n] of [total] | Terms covered: [list of transliterations] | Root families covered: [list]
**Cross-part note:** Root families shared with other parts: [list, or "none"]
```

Omit this block for single-part words.

---

### Section 1 — Header and Qualification Assessment

Word, registry ID, source list, date, version number. One short paragraph stating whether the word provisionally qualifies under the inner being definition, on what basis, and with what level of confidence. Draw this from the JSON meta block and term data — do not add reasoning that is not supported by what is in the JSON.

For multi-part words: state that this assessment covers only the terms in this part.

---

### Section 2 — Root Family Analysis

This is the main section of the file. Use the `root_family` groupings from the JSON to organise the terms. Write one prose section per root family, covering all the terms in that family together. Terms with no root family receive their own individual sections.

Each root family section must address:

- What the root's basic image or core meaning is, and how it generates the range of terms in the family
- How the different terms within the family are used differently in their verse sets — even when their dictionary meanings look similar
- What each term adds to the inner-being picture that the others in the family do not
- What the verb forms and their different types (including causative forms if present) add to the picture
- Whether the English translation captures or hides the distinctions between the terms
- A verdict at the end: are the terms in this family genuinely doing different work, are they near-synonyms, or are some of them candidates for consolidation?
- For root families that also appear in other parts: a note that the verdict here is provisional pending Session D

Every term in the JSON must appear in exactly one root family section or one individual term section. No term may be mentioned only in passing without its own analytical treatment.

---

### Section 3 — Where Sub-terms Do Different Work

Required whenever the JSON contains two or more terms from the same root family where the verse sets reveal that the terms function differently.

For each such case, state:
- Which terms are being compared
- What the verse sets reveal about how each term functions — cite specific verse references from the JSON
- Whether the difference is genuine (the terms reliably appear in different types of situations) or whether it appears to be a labelling distinction within what is functionally one term

If no meaningful differences are found between sub-terms in any family, state this explicitly: "No significant differences between sub-terms were found in this word set."

---

### Section 4 — OT/NT Register Analysis

Required only if `testament_coverage` in the JSON meta is "both."

Address the following, using only the verse records in the JSON:

- Does the NT vocabulary introduce terms or uses that have no direct equivalent in the OT portion of this word set? If so, what do they add?
- Does the NT use concepts from this word set differently from the OT — different subject, different context type, different direction of the state?
- What is present in the OT verses but absent from the NT, and vice versa?
- What is the single most significant difference between how the word functions in the OT verse set versus the NT verse set — stated as an observed difference, not a conclusion about what it means?

If `testament_coverage` is "OT_only" or "NT_only," omit this section and state that the word set is confined to one Testament.

All differences identified here must become open questions with the prefix [OT/NT] in Section 6.

---

### Section 5 — Data Quality Notes

Plain prose. State any gaps, inconsistencies, or thin data in the JSON that affect the completeness of this analysis. Identify which terms are affected and what effect the gap has on the analysis. Do not guess what the missing data might show. This section should match and expand on the data_quality_flags in the JSON. For multi-part words, include a note on which cross-part dependencies affect this part's analysis.

---

### Section 6 — Open Questions

A numbered list of questions that cannot be answered from the JSON alone. These are genuine questions for Phase 2 to investigate.

**Format for every question:**

- One sentence ending in a question mark
- One prefix from this list: [WORD-LEVEL] / [ROOT: transliteration] / [ROOT-CROSSPART] / [TERM: transliteration] / [OT/NT]
- The question must be genuinely open — it must not imply what the answer is

**New prefix for multi-part words:**

`[ROOT-CROSSPART]` — use when the question about a root family cannot be answered from a single part's data. These questions are held open until Session D (Cross-Part Synthesis).

**Required coverage:**

- At least one [OT/NT] question for every difference identified in Section 4
- A Phase 2 flag on every question that arises from a signal feature (god_as_subject, somatic_link, or causative_form_present being true for a term)
- At least one question for every SMALL_VERSE_SAMPLE term, calling for a fuller verse review in Phase 2

**Phase 2 flag format:**

> *Phase 2 flag: [one sentence stating what the inner-being model will need to decide or account for — not what the answer is, but what the question forces the model to address.]*

**Signal features that require a Phase 2 flag on their question:**

- A term where `god_as_subject` is true
- A term where `somatic_link` is true
- A term where `causative_form_present` is true
- A term whose verse set shows the same root used for both producing and resolving an inner state
- A term where the NT names the inner state as located in a specific inner faculty while the OT uses it as a general condition
- A term where the verse-object relationship shows the inner state acting on the body or the body expressing the inner state

---

### After writing Section 6 — update the JSON

For every term where a signal feature generated a Phase 2 flag, add the appropriate label to that term's `phase2_flags` array in the JSON and save the updated JSON file alongside the Analysis MD.

Use these labels:
- `"god_as_subject"` — term is applied to God or the Holy Spirit as the one who experiences or causes the state
- `"somatic_inner_link"` — inner state is connected to a physical bodily expression
- `"causative_of_inner_state"` — a form of this term is used to cause the inner state in another person
- `"generation_resolution_pair"` — the same root appears in the verse set for both producing and resolving this inner state
- `"nt_faculty_naming"` — NT locates the inner state in a named inner faculty where OT treats it as a general condition
- `"body_inner_expression"` — verse-object relationship shows the inner state acting on the body or the body expressing the inner state

---

## Rules — what the Analysis MD must never contain

- Data not in the JSON — if it is not in the JSON, it does not belong here
- Inference imported from outside the STEP data (no neuroscience, psychology, or cross-word synthesis)
- Framework B vocabulary (transformation stages, soul function labels, three-state typology)
- The words "therefore," "this shows," or "this demonstrates"
- Questions framed to imply a Framework B answer
- Hebrew or Greek script characters — transliteration only
- Conclusions about what a term means for Framework B or soul anatomy
- Cross-part synthesis conclusions — these belong in Session D, not in a part-level Session B

---

## Pre-submission checks for Session B

Before finalising:

- [ ] Scope declaration is present at the top for multi-part words
- [ ] Every term in the JSON appears in exactly one root family section or individual term section
- [ ] Every root family section with two or more terms includes a verdict on whether the terms are doing different work
- [ ] Root families shared with other parts are noted as provisional in their section verdicts
- [ ] Section 3 is present or explicitly noted as absent
- [ ] Section 4 is present if testament_coverage is "both," omitted and noted if not
- [ ] All OT/NT differences from Section 4 are carried forward as [OT/NT] prefixed open questions in Section 6
- [ ] All signal features (god_as_subject, somatic_link, causative_form_present = true) have generated at least one open question with a Phase 2 flag
- [ ] SMALL_VERSE_SAMPLE terms have generated at least one open question calling for fuller verse review
- [ ] All open questions are genuinely open and correctly prefixed
- [ ] [ROOT-CROSSPART] prefix used for root-level questions spanning multiple parts
- [ ] No Framework B vocabulary appears anywhere
- [ ] Transliteration only — no script characters
- [ ] Data quality notes align with the data_quality_flags in the JSON
- [ ] Verse citations in the prose are consistent with the verse_records in the JSON
- [ ] The JSON has been updated with phase2_flags where applicable
- [ ] Large file confirmed fully read before writing began

---

## Output

Produce the completed Analysis MD file, then produce the updated JSON file with phase2_flags populated. These two files, together with the Context MD from Session C, form the complete Phase 1 record for this word or word-part.

For multi-part words: when all parts are complete, a Session D (Cross-Part Synthesis) session should be run to produce the integrated analysis across all parts. Session D takes all part-level Session B analysis files as its inputs.

---

## Appendix — Session D reference

Session D (Cross-Part Synthesis) is defined in its own instruction document: `Session-D-CrossPartSynthesis-Instruction-v1.md`.

Its function in brief:
- **Input:** all part-level Session B analysis MDs for a single word, plus all part-level Session A JSON files for reference
- **Output:** one integrated synthesis MD (`WA-[registry-no]-[word]-synthesis-[yyyy-mm-dd].md`) covering the full word
- **Scope:** resolve provisional root-family verdicts, merge open questions across parts, identify cross-part patterns no single part could see, produce an integrated qualification assessment and OT/NT register analysis for the complete word

Session D runs only after all part-level Sessions A and B are complete. It is a **Phase 1 completion step** — Phase 2 analysis does not begin until the Session D synthesis file exists.
