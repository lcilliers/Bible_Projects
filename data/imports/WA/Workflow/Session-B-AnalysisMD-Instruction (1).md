# Session B — Analysis MD Production
## Framework B Soul Word Analysis | Phase 1 | v3 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-analysis-[yyyy-mm-dd].md`

This is the prose analysis file. It holds the documented linguistic and lexical observations drawn from the STEP data, organised by root family. It does not hold structured data (that is in the JSON) and does not hold verse context records (that is in the Context MD, produced in Session C).

---

## Input files required for this session

Attach all three of the following before starting:

1. **The word source file** — the STEP markdown file for the word (e.g. `word_grief.md`)
2. **The completed JSON file from Session A** — `WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`
3. **The v3 specification document** — `WA-Phase1-Specification-v3-2026-03-07.docx`

The JSON file is the primary reference for verse classifications, term data, and data quality flags. The source file is the primary reference for verse texts and meaning ranges. Do not begin until both have been read in full.

---

## Process sequence — follow this order exactly

**Step 1 — Read the JSON file in full.** Note all verse classifications, data quality flags, cross-registry links, and term inventory entries. These are the agreed data layer; the Analysis MD interprets them in prose — it does not contradict or re-classify them.

**Step 2 — Read the source file in full.** Focus on the meaning sections and verse texts for the analytical work in steps below.

**Step 3 — Group all terms into root families.** Use the related words index in the JSON and the STEP meaning blocks to identify which terms share roots. Terms with no root family membership receive an individual section.

**Step 4 — For each root family, plan the within-root contextual differentiation (Layer 1):** what does each sub-entry's verse set cluster around, and do the STEP distinctions reflect genuine functional register differences or mechanical lexical segmentation?

**Step 5 — Plan the OT/NT register analysis (Layer 2):** if the word has terms in both Testaments, identify what the OT vocabulary does that the NT does not, and vice versa. Note the most significant functional difference as an observed difference, not a theological conclusion.

**Step 6 — Identify all anthropological signal features (Layer 3):** root metaphor embeddings, causative stems, terms applied to God as subject, somatic-inner links, same-root generation-and-resolution pairs, faculty-naming terms. Plan the Flag for Phase 2 annotations for each.

**Step 7 — Plan the Open Questions.** Every Layer 2 OT/NT difference must become an [OT/NT] prefixed question. Every Layer 3 feature must have a Flag for Phase 2 annotation on its question. No question may imply a Framework B answer.

**Step 8 — Write the file.** Follow the section order below exactly.

---

## Analysis MD file structure

### Filename
`WA-[registry-no]-[word]-analysis-[yyyy-mm-dd].md`

### Section 1 — Header and Qualification Assessment
Word, registry ID, source list, date, version number. One short paragraph stating whether the word provisionally qualifies under the inner being definition, on what basis, and with what confidence — drawn exactly from the JSON qualification assessment block.

### Section 2 — Root Family Analysis

This is the primary section of the file and the longest. Organise all terms into root families. For each root family, write one prose section that covers all members together.

Each root family section must address:
- What the root metaphor or core meaning is, and how it generates the range of terms in the cluster
- How individual sub-entries within the family are differentiated in verse context — even when their dictionary meanings appear similar
- What each term contributes to the inner-being picture that the others do not
- What the grammatical structure (stem range, causative forms, passive forms) adds to the inner-being analysis for the family as a whole
- Whether the English translation captures or conceals the distinctions within the family
- A within-root contextual differentiation verdict: are the sub-entries genuinely distinct functional registers, near-homonyms, or one with the other being a peripheral extension?

Terms that do not belong to a root family receive their own individual section using the same framework.

**Every term in the STEP related word list must appear in exactly one root family section or one individual term section. No term may be treated only in the verse classification without a corresponding prose section.**

### Section 3 — Verse Contexts that Distinguish Sub-entries

Required whenever the term inventory contains sub-entries (two or more closely related terms from the same root) where the verse data reveals distinct functional registers.

For each such case, state:
- Which sub-entries are being compared
- What the verse contexts reveal about how each sub-entry functions distinctly — citing specific verses from the source file
- Whether the STEP differentiation reflects genuine lexical distinction or appears to be mechanical segmentation of what is functionally one term

If the word has no significant sub-entry differentiation, state this explicitly: "No significant sub-entry differentiation identified in this word set."

### Section 4 — OT/NT Register Analysis (Layer 2)

Required for every word with terms in both Testaments.

Address the following, strictly from the verse data:
- Does the NT vocabulary add new terms with no direct Hebrew equivalent in the word set? If so, what inner-being dimension do they add?
- Does the NT use existing concepts differently from the OT (different subject, function, context type)?
- What is present in the OT verse set but absent from the NT, and vice versa?
- What is the most significant functional difference between the OT and NT usage — stated as an observed difference, not a theological conclusion?

If the word has terms in only one Testament, state this and omit this section.

**Note:** All OT/NT differences identified here must be carried forward as Open Questions with the [OT/NT] prefix in Section 6. They are not conclusions — they are questions for Phase 2 to resolve.

### Section 5 — Data Quality Notes

Plain prose. Any gaps, inconsistencies, or thin data in the source file that affect the completeness of this analysis. Reference specific terms. State what is missing and what effect this has on the analysis. Do not speculate about what the missing data might show. This section should align with and expand on the data_quality_flags in the JSON.

### Section 6 — Open Questions

A numbered list of questions arising from the data that cannot be answered from the STEP file alone. These are genuine open questions for Phase 2.

**Format rules for every question:**
- One sentence ending in a question mark
- Prefix using exactly one of: [WORD-LEVEL] / [ROOT: transliteration] / [TERM: transliteration] / [OT/NT]
- Must be genuinely open — must not imply a Framework B answer
- Must not speculate on the answer

**Required categories:**
- At least one [OT/NT] question for every OT/NT register difference identified in Section 4
- A Flag for Phase 2 annotation on every question that identifies an anthropological signal feature

**Flag for Phase 2 format:**
> *Flag for Phase 2: [one sentence stating what is at stake for the inner-being model — not what the answer is, but what question the data forces the model to address.]*

**Anthropological signal features to actively look for** — each of these reliably generates a Flag for Phase 2:
- A term whose root metaphor embeds a physical-inner connection
- A term applied to God as subject
- A term with a causative stem (Hiphil/Piel) enabling one person to cause the inner state in another
- A term whose verse set shows the same root used for both generation and resolution of an inner state
- A term where the NT locates the inner state in a named internal faculty while the OT uses it as an event or condition without naming the faculty
- A term where the verb-object relationship shows the inner state acting on the body or the body expressing the inner state

---

## Rules — what the Analysis MD must never contain

- Data not traceable to the source file or to the JSON
- Inference, cross-word synthesis, or import from outside the STEP data
- Neuroscience, epigenetics, psychology (biblical or modern)
- Framework B vocabulary (three-state typology, soul function labels, transformation stages)
- The words "therefore," "this shows," or "this demonstrates"
- Questions framed to imply a Framework B answer
- Hebrew or Greek script characters — transliteration only
- Conclusions about what a term means for Framework B or soul anatomy

---

## Pre-submission checks for Session B

Before finalising:

- [ ] Every term appears in exactly one root family section or individual term section
- [ ] Every root family with 2+ sub-entries has a within-root contextual differentiation verdict
- [ ] If sub-entries are functionally indistinguishable, this is recorded as a consolidation candidate in the JSON (confirm this is present in the JSON before writing the verdict)
- [ ] Section 3 (Verse Contexts) is present or explicitly noted as absent
- [ ] Section 4 (OT/NT Register Analysis) is present if the word has both OT and NT terms
- [ ] All OT/NT differences are carried forward as [OT/NT] prefixed Open Questions
- [ ] All anthropological signal features have Flag for Phase 2 annotations on their questions
- [ ] All Open Questions are genuinely open and prefix-labelled
- [ ] No Framework B vocabulary appears anywhere
- [ ] Transliteration only — no script characters
- [ ] Data Quality Notes align with the JSON data_quality_flags
- [ ] Verse citations in the prose are traceable to the source file and consistent with the JSON classifications

---

## Output

Produce the completed Analysis MD file. This file, together with the JSON from Session A and the Context MD from Session C, constitutes the complete Phase 1 record for this word.
