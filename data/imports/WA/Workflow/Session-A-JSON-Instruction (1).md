# Session A — JSON Production
## Framework B Soul Word Analysis | Phase 1 | v3 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`

This is the structured data file. It holds all enumerable, tabular, and machine-readable data for the word. The Analysis MD and Context MD are produced in separate sessions (B and C) that depend on this file as input.

---

## Input files required for this session

Attach all three of the following to the session before starting:

1. **The word source file** — the STEP markdown file for the word being analysed (e.g. `word_grief.md`)
2. **The v3 specification document** — `WA-Phase1-Specification-v3-2026-03-07.docx`
3. **The existing v1 JSON file** if one exists (e.g. `WA-072-grief-data-2026-03-05.json`) — attach for reference only; the new file supersedes it entirely

Do not begin until all attached files have been read in full.

---

## Process sequence — follow this order exactly

**Step 1 — Read the entire source file from beginning to end.** Do not begin any output until the full file has been read.

**Step 2 — Identify every term in the STEP related word list.** Note any terms in the primary term list at the top of the file that do not appear in the STEP section — flag these as MISSING_TERM in data quality.

**Step 3 — For each term, extract from its word analysis block:**
- Strong's number (H or G)
- Full grammatical form string for the anchor occurrence
- Anchor stem (for Hebrew verbs: Qal / Niphal / Piel / Hiphil / Hophal / Hithpael / Pual)
- All stems present in the meaning section (full_stem_range)
- Occurrence count (integer or null if not stated)
- Full meaning range with numbered sub-definitions
- All related words from the related words cluster

**Step 4 — Classify every verse under every term.** Apply one of: CORE / EXTENDED / AMBIGUOUS / PERIPHERAL. Read each verse text in the source file individually before classifying. Do not sub-select or assume — read every verse. Apply the bundling rule where two or more verses under the same term show the same inner-being function in the same way. Record a reason clause for every EXTENDED, AMBIGUOUS, and PERIPHERAL classification. CORE needs no reason.

**Step 5 — Identify all cross-registry links** from related word clusters, STEP term list overlaps, and any verse sharing with other known word files.

**Step 6 — Record all data quality flags** for gaps, inconsistencies, thin data, absent word analysis blocks, format issues, and consolidation candidates.

---

## JSON file structure — populate all sections

### Filename
`WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`

### meta block
- `schema_version`: "1.1"
- `phase`: "Phase 1 — STEP Data Assimilation"
- `produced_date`: today's date
- `source_file`: filename of the source word file
- `specification`: "WA-Phase1-Specification v3 (2026-03-07)"
- `revision_note`: if updating a prior version, state precisely what changed

### word_identity block
- `word`: English word exactly as listed in the 181
- `registry_id`: registry number; null if TBC
- `source_list`: exactly as stated in the file header (High Confidence / Missing Inner Being Words / Low Confidence / Inferred)
- `category_label`: if stated in the file header; otherwise null
- `inference_note`: any inference flag from the file header; otherwise null

### qualification_assessment block
Apply the definition test strictly:

> *"Inner being characteristics are the non-physical, internal states, capacities, and expressions that constitute a person's invisible life — encompassing how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God."*

Fields:
- `qualification_verdict`: QUALIFIES / PROVISIONAL / BORDERLINE / DOES NOT QUALIFY / INSUFFICIENT DATA
- `qualification_basis`: one sentence — which part of the definition does the word satisfy, and from which specific term or verse
- `qualification_confidence`: HIGH / MEDIUM / LOW
- `qualification_flag`: specific reason for uncertainty; null if none

### term_inventory array
One entry per term from the STEP related word list. Fields per entry:
- `transliteration`: as given in the STEP file
- `strongs_number`: H or G number as given
- `language`: Hebrew or Greek
- `anchor_gloss`: English gloss in the STEP heading
- `word_type`: noun / verb / adjective / adverb
- `anchor_grammatical_form`: full form string from the word analysis block (null if no block)
- `anchor_stem`: for Hebrew verbs, the stem of the anchor form; null otherwise
- `full_stem_range`: list of all stems present in the meaning section
- `occurrence_count`: integer or null
- `meaning_summary`: primary meaning in plain English, max two sentences, drawn from the numbered meaning list
- `causative_stem_present`: true / false — whether Hiphil or Piel causative stem is listed
- `divine_subject_possible`: true / false — whether any meaning sub-definition or verse shows God as subject
- `somatic_dimension`: true / false — whether meaning or verses indicate bodily expression of the state

### related_words_index array
For each related word in each term's related words cluster:
- `host_term`: transliteration of the term whose cluster this comes from
- `related_transliteration`: as given
- `gloss`: as given
- `registry_crossref`: object with `registry_id` and `word` if this corresponds to another word in the 181; otherwise null
- `root_relationship`: same root / derived form / semantic family

### verse_classifications array
One entry per verse (or one entry per bundle). Fields:
- `term`: transliteration of the term this verse belongs to
- `reference`: book chapter:verse (or list of references if bundled)
- `classification`: CORE / EXTENDED / AMBIGUOUS / PERIPHERAL
- `reason`: one clause of explanation for EXTENDED / AMBIGUOUS / PERIPHERAL; null for CORE

Every verse reference in the source file must appear in exactly one entry. Do not silently omit any verse.

### cross_registry_links array
Fields per link:
- `linked_word`: English word
- `linked_registry_id`: registry number or null
- `connection_type`: shared_term / shared_root / shared_verse / semantic_overlap
- `connecting_term`: the specific term or verse that creates the link
- `note`: one sentence — what the connection is, without interpreting its significance

### data_quality_flags array
Fields per flag:
- `flag_type`: MISSING_TERM / THIN_DATA / NO_WORD_ANALYSIS / DUPLICATE_ENTRY / VERSE_WITHOUT_TERM / TERM_WITHOUT_VERSES / FORMAT_INCONSISTENCY / CONSOLIDATION_NOTE / PERIPHERAL_TERM / OTHER
- `affected_term`: transliteration or null if file-level
- `description`: one sentence describing the issue

---

## Rules — what the JSON must never contain

- Data not traceable to the source file
- Inference, interpretation, or import from outside the STEP file
- Hebrew or Greek script characters — transliteration only
- Framework B vocabulary (three-state typology, soul function labels, transformation stages)
- Any field left populated with fabricated data where the source file is silent — use null

---

## Pre-submission checks for Session A

Before finalising:

- [ ] Every term in the STEP related word list has an entry in term_inventory
- [ ] Every verse in the source file appears in verse_classifications (individually or bundled)
- [ ] No field contains data not traceable to the source file
- [ ] All data quality flags are recorded
- [ ] Bundling is noted with a reason in every bundled entry
- [ ] All cross-registry links are recorded even if significance is unclear
- [ ] Transliteration only — no script characters
- [ ] JSON is valid (no syntax errors)
- [ ] If updating a prior version, revision_note states precisely what changed

---

## Output

Produce the completed JSON file. This file is the input for Session B (Analysis MD) and Session C (Context MD).
