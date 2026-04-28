# Session A — JSON Production
## Framework B Soul Word Analysis | Phase 1 | v4 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`

This is the structured data file. It holds all enumerable, tabular, and factual data for the word. The Analysis MD (Session B) and Context MD (Session C) are produced in separate sessions that depend on this file as their only input. Get this file right — everything downstream depends on it.

---

## Input files required for this session

Attach both of the following before starting:

1. **The word source file** — the STEP markdown file for the word being analysed (e.g. `word_grief.md`)
2. **The existing JSON file** if one exists (e.g. `WA-072-grief-data-2026-03-05.json`) — attach for reference only; the new file supersedes it entirely

Do not begin until both attached files have been read in full.

---

## Process sequence — follow this order exactly

**Step 1 — Read the entire source file from beginning to end.** Do not begin any output until the full file has been read.

**Step 2 — Identify every term in the STEP related word list.** Note any terms listed in the primary term list at the top of the file that do not appear in the STEP section — flag these as TERMS_IN_HEADER_NOT_IN_STEP in data quality.

**Step 3 — For each term, extract from its word analysis block:**
- Strong's number (H or G number)
- Transliteration (the pronunciation spelling used throughout — no Hebrew or Greek script characters)
- Short label (the English word or phrase STEP uses as the heading for this term)
- Full meaning range with all numbered sub-definitions, copied as plain text
- All related words from the related words cluster for this term
- Occurrence count (the number stated in STEP, or null if not stated)
- Whether any meaning sub-definition or verse in this term's section shows God as the one experiencing or causing this state
- Whether the meaning block or verses show the state being expressed through the body (trembling, weeping, physical collapse, etc.)
- Whether a causative form is listed in the meaning block — that is, a form meaning "to cause someone else to experience this state" (for Hebrew verbs: Hiphil or Piel causative)
- The root family this term belongs to — identified by the shared Hebrew or Greek root consonants. Assign a short uppercase label (e.g. TSR, TSUQ, RA, THLIBO). If the term belongs to no family, set this to null. If a term bridges two families, list both.
- Which Testament the term's verses belong to: OT, NT, or both — derived by scanning the verse list for this term

**Step 4 — For every verse under every term, record the verse.** Read each verse text individually. Do not skip or assume. Record the book, reference, and full verse text for every verse in the source file.

**Step 5 — Identify all cross-registry links** from related word clusters, STEP term list overlaps, and any verse sharing with other known word files.

**Step 6 — Record all data quality flags** for gaps, inconsistencies, thin data, absent word analysis blocks, format errors, and terms that appear to be duplicates or consolidation candidates.

---

## JSON file structure — populate all sections

### Filename
`WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`

---

### meta block

```json
"meta": {
  "schema_version": "2.2",
  "phase": "Phase 1 — STEP Data Assimilation",
  "produced_date": "yyyy-mm-dd",
  "source_file": "word_[word].md",
  "translation_used": "ESV",
  "specification": "Session A Instruction v4",
  "revision_note": null,
  "word": "[English word]",
  "registry_id": "[e.g. 051]",
  "source_list": "[High Confidence / Missing Inner Being Words / Low Confidence / Inferred]",
  "category": "[category label from file header, or null]",
  "testament_coverage": "[OT_only / NT_only / both]"
}
```

`testament_coverage` at the word level is derived from the combined verse set: if the word has at least one OT term with listed verses and at least one NT term with listed verses, set "both"; otherwise set "OT_only" or "NT_only".

---

### term_inventory_hebrew array

One entry per Hebrew term. Fields:

```json
{
  "term_id": "H6869B",
  "step_search_gloss": "distress",
  "step_search_flag": null,
  "transliteration": "tsa.rah",
  "strongs_number": "H6869B",
  "word_analysis_gloss": "distress",
  "occurrence_count": 70,
  "occurrence_count_qualifier": "about",
  "meaning": "[full plain-text meaning block]",
  "meaning_numbered": null,
  "related_words": [
    { "gloss": "narrow", "transliteration": "tsar" }
  ],
  "also_spelled": null,
  "root_family": ["TSR"],
  "testament": "OT",
  "god_as_subject": false,
  "somatic_link": false,
  "causative_form_present": false,
  "phase2_flags": []
}
```

**Field notes:**

- `root_family` — array of short uppercase root labels. Null if the term belongs to no family. Use the same label consistently across all terms that share a root.
- `testament` — "OT", "NT", or "both". Derived from the verse list for this term: if all verses are from the Old Testament books, set "OT"; if all are from the New Testament books, set "NT"; if both, set "both". Old Testament books are Genesis through Malachi. New Testament books are Matthew through Revelation.
- `god_as_subject` — true if any meaning sub-definition or verse in this term's section shows God as the one who experiences or causes this inner state. False otherwise.
- `somatic_link` — true if the meaning block or any verse in this term's section connects this inner state to a physical bodily expression (trembling, weeping, physical collapse, writhing, somatic language of any kind). False otherwise.
- `causative_form_present` — true if the meaning block lists a Hiphil or Piel form with a meaning that amounts to "to cause someone else to experience this state." False otherwise.
- `phase2_flags` — empty array in Session A output. Session B will populate this field. Do not add values here.

---

### term_inventory_greek array

One entry per Greek term. Same fields as Hebrew with the following differences:

- `lsj_entry` — the full LSJ (Liddell-Scott-Jones) dictionary text if present in the source file. Null if not present.
- `causative_form_present` — Greek verbs do not use Hiphil/Piel stems. Set true only if the meaning block explicitly describes a causative sense (e.g. "to cause grief in another," "to make afraid"). False otherwise.
- No `also_spelled` field.
- No `meaning_numbered` field.

---

### verse_records array

One entry per verse per term. Do not bundle verses.

```json
{
  "term_id": "H6869B",
  "transliteration": "tsa.rah",
  "testament": "OT",
  "book": "Genesis",
  "reference": "Gen 35:3",
  "verse_text": "Then let us arise and go up to Bethel..."
}
```

Every verse in the source file must appear here. Do not silently omit any verse.

---

### cross_registry_links array

```json
{
  "linked_word": "grief",
  "linked_registry_id": "072",
  "connection_type": "shared_term",
  "connecting_term": "tsa.rah",
  "note": "tsa.rah appears in the grief word set as well as the distress word set."
}
```

`connection_type` options: `shared_term` / `shared_root` / `shared_verse` / `semantic_overlap`

---

### data_quality_flags array

```json
{
  "term_id": "H7379",
  "flag": "FORMAT_ERROR_IN_SOURCE",
  "description": "The word analysis block for me.tsar displays data for riv (H7379) instead of the correct data for H4689."
}
```

`flag` options: `OCCURRENCE_COUNT_MISMATCH` / `TERMS_IN_HEADER_NOT_IN_STEP` / `FORMAT_ERROR_IN_SOURCE` / `NO_WORD_ANALYSIS` / `PARSE_ERROR` / `CONSOLIDATION_CANDIDATE` / `THIN_DATA`

Use `CONSOLIDATION_CANDIDATE` when two or more terms in the inventory appear to name the same functional state and their verse sets do not reveal meaningful differences. State which terms are the candidates in the description.

---

## Rules — what the JSON must never contain

- Data not traceable to the source file
- Inference, interpretation, or import from outside the STEP file
- Hebrew or Greek script characters — transliteration only
- Framework B vocabulary
- Fabricated data where the source file is silent — use null

---

## Pre-submission checks for Session A

Before finalising:

- [ ] Every term in the STEP related word list has an entry in term_inventory_hebrew or term_inventory_greek
- [ ] Every verse in the source file appears in verse_records
- [ ] Every term has root_family assigned or explicitly set to null
- [ ] Every term has testament assigned (OT / NT / both)
- [ ] testament_coverage in meta is consistent with the term-level testament fields
- [ ] god_as_subject, somatic_link, and causative_form_present are set for every term
- [ ] phase2_flags is an empty array on every term — not null, not absent
- [ ] All data quality flags are recorded
- [ ] No field contains data not traceable to the source file
- [ ] Transliteration only — no script characters
- [ ] JSON is valid (no syntax errors)
- [ ] If updating a prior version, revision_note states precisely what changed

---

## Output

Produce the completed JSON file. This file is the only input for Session B (Analysis MD) and Session C (Context MD).
