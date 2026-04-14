# Session B — Analysis MD Production
## Framework B Soul Word Analysis | Phase 1 | v4 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-analysis-[yyyy-mm-dd].md`

This is the prose analysis file. It holds the written linguistic and lexical observations drawn from the JSON data file produced in Session A. It does not reproduce the structured data — it interprets it in plain prose, organised by root family.

---

## Input files required for this session

**One file only:**

- **The completed JSON file from Session A** — `WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`

Do not attach or read the STEP source file. The JSON is the only source for this session. Everything you need — term meanings, verse texts, root family groupings, occurrence counts, testament coverage, and signal feature flags — is already in the JSON. If something is not in the JSON, it does not belong in this file.

---

## Process sequence — follow this order exactly

**Step 1 — Read the JSON file in full.** Work through every term entry and every verse record before writing anything. Note the root family groupings, the testament field on each term, and the three signal feature fields (god_as_subject, somatic_link, causative_form_present). These are the facts the analysis is built on.

**Step 2 — Group the terms by root family.** The `root_family` field on each term entry tells you which family it belongs to. Terms with `root_family: null` stand alone and receive individual sections. Write down the list of families and which terms belong to each before you start writing.

**Step 3 — For each root family, plan the within-family analysis.** Look at the verse_records for each term in the family and identify: does the verse set for each sub-term cluster around a different type of situation, a different subject, or a different inner-being function? If yes, note what the difference is. If no, note that the terms appear functionally similar.

**Step 4 — Plan the OT/NT analysis.** Check the `testament_coverage` field in meta. If the word has terms in both Testaments, identify: what does the OT vocabulary do that the NT does not, and vice versa? Base this only on the verse records in the JSON.

**Step 5 — Identify signal features.** For every term where any of the three signal feature fields is true — `god_as_subject`, `somatic_link`, `causative_form_present` — plan what the analysis will say about that feature and what open question it raises. Every signal feature must produce at least one open question in Section 6 with a Phase 2 flag attached.

**Step 6 — Write the file.** Follow the section order below exactly.

---

## Analysis MD file structure

### Filename
`WA-[registry-no]-[word]-analysis-[yyyy-mm-dd].md`

---

### Section 1 — Header and Qualification Assessment

Word, registry ID, source list, date, version number. One short paragraph stating whether the word provisionally qualifies under the inner being definition, on what basis, and with what level of confidence. Draw this from the JSON meta block and term data — do not add reasoning that is not supported by what is in the JSON.

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
- What is the single most significant difference between how distress (or whatever the word is) functions in the OT verse set versus the NT verse set — stated as an observed difference, not a conclusion about what it means?

If `testament_coverage` is "OT_only" or "NT_only," omit this section and state that the word set is confined to one Testament.

All differences identified here must become open questions with the prefix [OT/NT] in Section 6.

---

### Section 5 — Data Quality Notes

Plain prose. State any gaps, inconsistencies, or thin data in the JSON that affect the completeness of this analysis. Identify which terms are affected and what effect the gap has on the analysis. Do not guess what the missing data might show. This section should match and expand on the data_quality_flags in the JSON.

---

### Section 6 — Open Questions

A numbered list of questions that cannot be answered from the JSON alone. These are genuine questions for Phase 2 to investigate.

**Format for every question:**

- One sentence ending in a question mark
- One prefix from this list: [WORD-LEVEL] / [ROOT: transliteration] / [TERM: transliteration] / [OT/NT]
- The question must be genuinely open — it must not imply what the answer is

**Required coverage:**

- At least one [OT/NT] question for every difference identified in Section 4
- A Phase 2 flag on every question that arises from a signal feature (god_as_subject, somatic_link, or causative_form_present being true for a term)

**Phase 2 flag format:**

> *Phase 2 flag: [one sentence stating what the inner-being model will need to decide or account for — not what the answer is, but what the question forces the model to address.]*

**Signal features that require a Phase 2 flag on their question:**

- A term where `god_as_subject` is true — God or the Holy Spirit is shown experiencing or causing this inner state
- A term where `somatic_link` is true — the inner state is connected to a physical bodily expression
- A term where `causative_form_present` is true — the language allows one person to cause this inner state in another
- A term whose verse set shows the same root used for both producing and resolving an inner state
- A term where the NT names the inner state as located in a specific inner faculty (heart, soul, spirit) while the OT uses it as a general event or condition
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

---

## Pre-submission checks for Session B

Before finalising:

- [ ] Every term in the JSON appears in exactly one root family section or individual term section
- [ ] Every root family section with two or more terms includes a verdict on whether the terms are doing different work
- [ ] Section 3 is present or explicitly noted as absent
- [ ] Section 4 is present if testament_coverage is "both," omitted and noted if not
- [ ] All OT/NT differences from Section 4 are carried forward as [OT/NT] prefixed open questions in Section 6
- [ ] All signal features (god_as_subject, somatic_link, causative_form_present = true) have generated at least one open question with a Phase 2 flag
- [ ] All open questions are genuinely open and correctly prefixed
- [ ] No Framework B vocabulary appears anywhere
- [ ] Transliteration only — no script characters
- [ ] Data quality notes align with the data_quality_flags in the JSON
- [ ] Verse citations in the prose are consistent with the verse_records in the JSON
- [ ] The JSON has been updated with phase2_flags where applicable

---

## Output

Produce the completed Analysis MD file, then produce the updated JSON file with phase2_flags populated. These two files, together with the Context MD from Session C, form the complete Phase 1 record for this word.
