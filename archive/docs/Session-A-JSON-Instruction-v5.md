# Session A — JSON Production
## Framework B Soul Word Analysis | Phase 1 | v5 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-data[-part[n]]-[yyyy-mm-dd].json`

This is the structured data file. It holds all enumerable, tabular, and factual data for the word. The Analysis MD (Session B) and Context MD (Session C) are produced in separate sessions that depend on this file as their only input. Get this file right — everything downstream depends on it.

---

## Process overview

Session A runs in three distinct stages. Do not proceed from one stage to the next without completing the current one.

```
Stage 1 — Pre-validation     Read the source file. Check for structural errors
                              and size. Resolve all issues before any data extraction.
                              ↓ (only if source passes or all issues are resolved)
Stage 2 — Data extraction    Extract all term data and verses into the JSON structure.
                              ↓
Stage 3 — Output             Write the JSON file. Record root family labels used.
```

---

## Stage 1 — Pre-validation

Pre-validation runs before any data extraction. Its purpose is to catch source file problems that would silently corrupt the JSON if left undetected. Stage 2 must not begin until Stage 1 is complete with no outstanding hard stops.

### Step 1.1 — Read the source file in full

Check the line count first using the bash tool: `wc -l [filepath]`

If the file exceeds 3,000 lines, read in sequential blocks using explicit line ranges (e.g. 1–1500, 1501–3000). Confirm the final block has been reached before proceeding. Do not begin Stage 2 until all blocks have been read.

### Step 1.2 — Term count and size check

Count the total number of distinct terms in the source file.

**If the term count is fewer than 12:** proceed to Step 1.3.

**If the term count is 12 or more:** the file is a candidate for splitting. Run the split assessment below before proceeding to Step 1.3.

---

#### Split assessment (term count 12 or more)

1. Scan the full term list and identify all root families by examining related-word clusters and shared root consonants.
2. Count the total verse records across all terms.
3. Propose a split that:
   - Creates parts of approximately 8–10 terms each
   - Keeps all members of a root family in the same part wherever possible
   - If a root family is large enough to require splitting across parts, note this explicitly

4. Present the split plan to the user in this exact format and stop. Do not write any part files until the user explicitly approves:

```
SPLIT PLAN PROPOSED
Word: [word] | Registry: [id] | Total terms: [n] | Estimated total verses: [n]
Reason: Term count exceeds single-session threshold (12+).

Proposed split:
  Part 1 — [n] terms: [transliteration list]
           Root families: [list]
  Part 2 — [n] terms: [transliteration list]
           Root families: [list]
  [Part 3 etc. if needed]

Root families that must span parts (unavoidable): [list, or "none"]

Awaiting your approval before writing part files.
If you wish to adjust the split, please advise and I will revise.
```

5. Once the user approves, write the split source files named `Word_[word]_Part[n].md` and confirm they are ready.
6. Session A then runs separately for each part file. Return to Step 1.1 for the assigned part.

---

### Step 1.3 — Structural integrity checks

For every term in the source file, verify the following three conditions.

#### Check A — Term heading and word analysis match (Hard Stop)

The heading for each term must match the word analysis block that follows it. A mismatch occurs when the heading identifies one term but the analysis block belongs to a different term — detectable when the Strong's number, transliteration, or meaning content of the block does not correspond to the heading.

**On failure — present this and stop:**

```
VALIDATION FAILURE — HARD STOP
Check A: Term heading / word analysis mismatch
Term heading: [heading as written]
Location: [section or approximate position in source file]
Problem: The word analysis block in this section contains data
         for "[mismatched content identifier]", not for the term
         named in the heading.
Required action: The source file must be manually corrected.
                 Re-attach the corrected file to continue.
```

Do not proceed until the user confirms the correction and re-attaches the file. Then re-run Steps 1.1 and 1.3 from the beginning.

#### Check B — Word analysis block present (Hard Stop)

Every term must have a word analysis block containing at minimum a meaning description. A term with only a heading and no content cannot be processed.

**On failure — present this and stop:**

```
VALIDATION FAILURE — HARD STOP
Check B: Missing word analysis block
Term: [transliteration] ([Strong's number if visible])
Location: [section or approximate position in source file]
Problem: This term has a header entry but no word analysis block.
         There is no meaning data to extract.
Required action: The source file must be manually corrected.
                 Re-attach the corrected file to continue.
```

Do not proceed until the user confirms the correction and re-attaches the file.

#### Check C — Verse records present (Soft Warning)

Every term should have at least one verse record in its section. A term with a meaning block but no verses can still be partially processed, but verse analysis will not be possible.

**On failure — present this and wait for the user's decision:**

```
VALIDATION WARNING — DECISION REQUIRED
Check C: No verse records found
Term: [transliteration] ([Strong's number])
Situation: This term has a word analysis block but no verse records
           in the source file.

Options:
  (a) Proceed — extract the meaning block, record the term with an
      empty verse set, and flag it as NO_VERSES in data quality.
      Verse analysis will not be possible for this term.
  (b) Stop — treat this as a source file error requiring correction
      before proceeding.

Please advise. If multiple terms have this issue, your answer
will be applied to all of them.
```

Wait for the user's decision before continuing. If the user chooses (a), apply that instruction to all no-verse terms in the same file.

---

### Step 1.4 — Validation summary

After completing all three checks (and resolving any failures), present this summary:

```
VALIDATION SUMMARY
Source file: [filename]
Terms identified: [n]

Check A (heading/analysis match): [PASS / FAIL — resolved]
Check B (analysis block present): [PASS / FAIL — resolved]
Check C (verses present):         [PASS / n terms flagged — decision: a or b]

Split required: [yes — plan approved / no]

[If all clear:]   Source file passes validation. Proceeding to Stage 2.
[If outstanding:] Awaiting resolution of the above before proceeding.
```

---

## Stage 2 — Data extraction

Begin Stage 2 only after Stage 1 is complete with no outstanding hard stops.

### Step 2.1 — Identify every term in the STEP related word list

Note any terms listed in the primary term list at the top of the file that do not appear in the STEP section — flag these as TERMS_IN_HEADER_NOT_IN_STEP in data quality.

### Step 2.2 — For each term, extract from its word analysis block

- Strong's number (H or G number)
- Transliteration (the pronunciation spelling — no Hebrew or Greek script characters)
- Short label (the English word or phrase STEP uses as the heading)
- Full meaning range with all numbered sub-definitions, copied as plain text
- All related words from the related words cluster for this term
- Occurrence count (as stated in STEP, or null if not stated)
- Whether any meaning sub-definition or verse shows God experiencing or causing this state (`god_as_subject`)
- Whether the meaning block or verses connect this state to physical bodily expression (`somatic_link`)
- Whether the meaning block lists a causative form — Hiphil or Piel for Hebrew — meaning "to cause someone else to experience this state" (`causative_form_present`)
- The root family this term belongs to, as a short uppercase label (e.g. TSR, TSUQ, RA, THLIBO). Use labels from `root_families_in_prior_parts` for consistency across parts. Set to null if no family. List both families if the term bridges two.
- Testament coverage (OT / NT / both) — derived by scanning the verse list

### Step 2.3 — For every verse under every term, record the verse

Read each verse text individually. Do not skip or assume. Record the book, reference, and full verse text for every verse in the source file.

After recording verses for each term, check: if the verse count recorded is less than 20% of the occurrence count for any term with 20 or more occurrences, flag that term as SMALL_VERSE_SAMPLE.

### Step 2.4 — Identify all cross-registry links

Identify cross-registry connections from related word clusters, STEP term list overlaps, and any verse sharing with other known word files.

### Step 2.5 — Record all data quality flags

Record flags for all findings from Stage 1 (resolved issues should be recorded for completeness) and Stage 2 (gaps, thin data, consolidation candidates, etc.).

---

## Stage 3 — JSON file structure

### Filename

Single-part word: `WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`
Multi-part word: `WA-[registry-no]-[word]-data-part[n]-[yyyy-mm-dd].json`

---

### meta block

```json
"meta": {
  "schema_version": "2.3",
  "phase": "Phase 1 — STEP Data Assimilation",
  "produced_date": "yyyy-mm-dd",
  "source_file": "word_[word].md",
  "translation_used": "ESV",
  "specification": "Session A Instruction v5",
  "revision_note": null,
  "word": "[English word]",
  "registry_id": "[e.g. 051]",
  "source_list": "[High Confidence / Missing Inner Being Words / Low Confidence / Inferred]",
  "category": "[category label from file header, or null]",
  "testament_coverage": "[OT_only / NT_only / both]",
  "part_number": null,
  "total_parts": null,
  "is_split": false,
  "root_families_in_prior_parts": []
}
```

**Field notes:**

- `part_number` — integer. Null for single-part words.
- `total_parts` — integer. Null for single-part words.
- `is_split` — true if this word's source data spans multiple part files. False otherwise.
- `root_families_in_prior_parts` — array of root family labels already assigned in earlier parts. Empty array for Part 1 or single-part words.
- `testament_coverage` — "both" if the combined verse set covers both Testaments; "OT_only" or "NT_only" otherwise.

---

### term_inventory_hebrew array

One entry per Hebrew term:

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

- `phase2_flags` — empty array in Session A output. Session B populates this field. Do not add values here.

**Phase 2 flag labels (reference — Session B populates these from Session A's signal feature fields):**
- `"god_as_subject"` — term applied to God or the Holy Spirit as the one who experiences or causes the state
- `"somatic_inner_link"` — inner state connected to a physical bodily expression
- `"causative_of_inner_state"` — a form of this term causes the inner state in another person
- `"generation_resolution_pair"` — same root appears for both producing and resolving this inner state
- `"nt_faculty_naming"` — NT locates the state in a named inner faculty where OT treats it as a general condition
- `"body_inner_expression"` — inner state acts on the body or the body expresses the inner state

---

### term_inventory_greek array

Same fields as Hebrew, with these differences:
- Add `lsj_entry` — full LSJ text if present in the source. Null if not.
- `causative_form_present` — true only if the meaning block explicitly states a causative sense. No Hiphil/Piel.
- No `also_spelled` field.
- No `meaning_numbered` field.

---

### verse_records array

One entry per verse per term:

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

Every verse in the source file must appear. Do not silently omit any verse.

---

### cross_registry_links array

```json
{
  "linked_word": "grief",
  "linked_registry_id": "072",
  "connection_type": "shared_term",
  "connecting_term": "tsa.rah",
  "note": "tsa.rah appears in both the grief and distress word sets."
}
```

`connection_type` options: `shared_term` / `shared_root` / `shared_verse` / `semantic_overlap`

---

### data_quality_flags array

```json
{
  "term_id": "H7379",
  "flag": "HEADING_MISMATCH",
  "description": "Heading reads 'riv' but word analysis block contains data for me.tsar (H4689). Resolved: source file corrected before extraction."
}
```

`flag` options:
- `HEADING_MISMATCH` — term heading and word analysis block do not correspond (Stage 1 Check A)
- `NO_WORD_ANALYSIS` — term has no meaning block (Stage 1 Check B)
- `NO_VERSES` — term has a meaning block but no verse records; user chose to proceed (Stage 1 Check C)
- `TERMS_IN_HEADER_NOT_IN_STEP` — term in source header is absent from the STEP section
- `OCCURRENCE_COUNT_MISMATCH` — stated occurrence count is inconsistent with available data
- `FORMAT_ERROR_IN_SOURCE` — structural malformation preventing reliable extraction
- `PARSE_ERROR` — section malformed in a way that prevented extraction
- `CONSOLIDATION_CANDIDATE` — two or more terms appear to name the same state with no meaningful verse-set differences
- `THIN_DATA` — sparse data (fewer than 5 verses, very low occurrence count)
- `SMALL_VERSE_SAMPLE` — verses recorded are less than 20% of occurrence count for a term with 20+ occurrences; register assessments may not be representative

Stage 1 findings that were resolved should still be recorded here for completeness. State that they were resolved and how.

---

## Rules — what the JSON must never contain

- Data not traceable to the source file
- Inference, interpretation, or import from outside the STEP file
- Hebrew or Greek script characters — transliteration only
- Framework B vocabulary
- Fabricated data where the source file is silent — use null

---

## Pre-submission checks

Before finalising:

- [ ] Stage 1 complete — no outstanding hard stops
- [ ] All soft warnings resolved and user decisions recorded
- [ ] Split plan approved if term count was 12 or more
- [ ] Every term has an entry in term_inventory_hebrew or term_inventory_greek
- [ ] Every verse in the source file appears in verse_records
- [ ] Every term has root_family assigned or explicitly set to null
- [ ] Every term has testament assigned (OT / NT / both)
- [ ] Root family labels are consistent with `root_families_in_prior_parts` if this is a later part
- [ ] testament_coverage in meta is consistent with the term-level testament fields
- [ ] god_as_subject, somatic_link, and causative_form_present are set for every term
- [ ] phase2_flags is an empty array on every term — not null, not absent
- [ ] All data quality flags recorded, including Stage 1 findings and SMALL_VERSE_SAMPLE terms
- [ ] meta fields part_number, total_parts, is_split, and root_families_in_prior_parts correctly populated
- [ ] No field contains data not traceable to the source file
- [ ] Transliteration only — no script characters anywhere
- [ ] JSON is valid (no syntax errors)
- [ ] If updating a prior version, revision_note states precisely what changed
- [ ] Large file confirmed fully read before any writing began

---

## Closing output note

After producing the JSON, state:

1. The root family labels assigned in this session (e.g. `["CHARAH", "TSR", "BAHAL", "LUPE"]`)
2. Whether any root families from `root_families_in_prior_parts` recurred in this part
3. Any unresolved soft warnings the user should be aware of before running Session B

For multi-part words: carry the root family labels forward into `root_families_in_prior_parts` in the meta block of subsequent parts.

**Phase 1 sequence note:** This JSON is the only input for Session B (Analysis MD) and Session C (Context MD). When all parts are complete, Session D (Cross-Part Synthesis) produces the integrated Phase 1 analysis before Phase 2 work begins. Session D is a Phase 1 completion step — Phase 2 does not start until Session D is done.
