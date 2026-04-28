# Word Study Extract — Design Reference

**Date:** 2026-03-23  
**Status:** In progress — awaiting confirmation before coding begins

---

## Purpose

This document captures the agreed design for `word_study_extract.py` — a single script that replaces the three-script pipeline (`_discover_word_terms.py`, `_apply_term_decisions.py`, `_extract_word_terms.py`).

**Phase covered here:** Step 1 — STEP data pull only.  
No DB reads. No DB writes. Output is a complete JSON (+ optional summary .md).

---

## Scope boundary — Step 1

Step 1 queries STEP only. **No DB reads. No DB writes.**

The extract output will not include terms that are already in `wa_term_inventory` from a prior run (e.g. H4578, H5397 for soul), nor terms registered in `mti_terms` that fall outside the STEP cluster. Both categories are only discoverable by comparing the extract output against the DB — that comparison is part of the audit-word process (step A4), not the extract.

---

## What the script produces (Step 1)

Input: English word from `word_registry` (e.g. `--word soul`)

Output: `research/discovery/{word}_step_data_{YYYYMMDD}.json`

### JSON structure

```
{
  "meta": { ... },          ← extraction metadata and summary counts
  "terms": [ ... ],         ← one record per term code in the STEP cluster
}
```

---

### JSON output — annotated example (soul, 2026-03-23)

The values below are real data returned by STEP on 2026-03-23. Four term records are shown, one per decision group, to illustrate each code path through the filter logic.

```json
{
  "meta": {
    "english_anchor": "soul",
    "generated": "2026-03-23",
    "step_version": "ESV_th",
    "anchor_codes": ["H5315G", "G5590G"],
    "particle_ceiling": 1000,
    "total_terms_evaluated": 24,
    "summary_by_group": { "G1": 14, "G2": 1, "G2r": 3, "G3": 2, "G4": 1, "G5": 3 },
    "include_codes": ["H5315G", "H5315A", "H5315B", "H5315C", "H5315D", "H5315E",
                      "H5315F", "H5315H", "G5590G", "G5590A", "G5590B", "G5590C",
                      "G5590D", "G5590E", "H5314", "H5317", "G5594"],
    "exclude_codes": ["H5316", "H5318", "G4151", "H0776G", "H7307G", "H3820G",
                      "H3824"]
  },

  "terms": [

    {
      "_comment": "── G1 example: primary anchor sub-gloss, include, verses fetched ──",
      "code": "H5315G",
      "gloss": "soul",
      "transliteration": "ne.phesh",
      "script_form": "נֶ֫פֶשׁ",
      "language": "Hebrew",
      "vocab_count": 249,
      "medium_def": "1) soul, self, life, creature, person, appetite, mind, living being, desire, emotion, passion\n1a) that which breathes, the breathing substance or being, soul, the inner being of man\n1b) living being\n1c) the man himself, self, person or individual\n1d) departed soul, dead person\n1e) the will as the seat of appetite\n1f) activity of mind\n1g) activity of the will\n1h) activity of the character",
      "lsj_entry": "",
      "short_def_mounce": "",
      "related_words": [
        { "strong": "H5305", "form": "נָפִישׁ", "gloss": "Naphish",     "translit": "na.phish" },
        { "strong": "H5314", "form": "נָפַשׁ",  "gloss": "be refreshed", "translit": "na.phash" },
        { "strong": "H5315H","form": "נֶ֫פֶשׁ",  "gloss": "soul: life",   "translit": "ne.phesh" }
      ],
      "raw_related_numbers": "H5305,H5314,H5315H",
      "freq_list": "Gen:6,Exod:3,Lev:9,Num:8,Deut:14,Josh:3,Judg:2,...",
      "is_proper_noun": false,
      "is_sub_gloss": false,
      "step_parent_code": "H5315G",
      "step_section_type": "primary",
      "decision_group": "G1",
      "action": "include",
      "decision_reason": "F4: parent H5315G in anchor list, section_type=primary",
      "verses_fetched": true,
      "verse_count": 179,
      "testament_coverage": "OT_only",
      "meaning_numbered": true,
      "causative_form_present": false,
      "data_quality_flags": [],
      "quality_flag_detail": {},
      "verses": [
        {
          "osisId": "Gen.34.3",
          "ref": "Gen 34:3",
          "book_code": "Gen",
          "chapter": 34,
          "verse_num": 3,
          "esv_text": "And his soul was drawn to Dinah the daughter of Jacob. He loved the young woman and spoke tenderly to her.",
          "target_word": "soul",
          "testament": "OT",
          "fetched_under_code": "H5315G",
          "preview_html": "<span morph='HNcfsc HC HSp3ms' strong='H5315G H9002 H9023'>soul</span>...",
          "span_strong_match": 1,
          "span_code_found": "H5315G",
          "span_label_found": "soul",
          "context_before": "And his",
          "context_after": "was drawn to Dinah the"
        }
      ]
    },

    {
      "_comment": "── G2 example: confirmed NPŠ root, include, verses fetched ──",
      "code": "H5314",
      "gloss": "be refreshed",
      "transliteration": "na.phash",
      "script_form": "נָפַשׁ",
      "language": "Hebrew",
      "vocab_count": 3,
      "medium_def": "(Niphal) to take breath, refresh oneself",
      "lsj_entry": "",
      "short_def_mounce": "",
      "related_words": [],
      "raw_related_numbers": "",
      "freq_list": "Exod:1,2Sam:1,Isa:1",
      "is_proper_noun": false,
      "is_sub_gloss": false,
      "step_parent_code": "H5315G",
      "step_section_type": "related_term",
      "decision_group": "G2",
      "action": "include",
      "decision_reason": "F5a: parent H5315G in anchor list, section_type=related_term, root confirmed (H5314 in confirmed-root set)",
      "verses_fetched": true,
      "verse_count": 3,
      "testament_coverage": "OT_only",
      "meaning_numbered": false,
      "causative_form_present": false,
      "data_quality_flags": [],
      "quality_flag_detail": {},
      "verses": [
        {
          "osisId": "2Sam.16.14",
          "ref": "2Sa 16:14",
          "book_code": "2Sam",
          "chapter": 16,
          "verse_num": 14,
          "esv_text": "And the king, and all the people who were with him, arrived weary at the Jordan. And there he refreshed himself.",
          "target_word": "refreshed",
          "testament": "OT",
          "fetched_under_code": "H5314",
          "preview_html": "<span morph='HVNrmsa' strong='H5314'>refreshed</span>...",
          "span_strong_match": 1,
          "span_code_found": "H5314",
          "span_label_found": "be refreshed",
          "context_before": "there he",
          "context_after": "himself ."
        }
      ]
    },

    {
      "_comment": "── G4 example: grammatical particle, exclude, no verses ──",
      "code": "H9005",
      "gloss": "to/for",
      "transliteration": "le",
      "script_form": "לְ",
      "language": "Hebrew",
      "vocab_count": 20899,
      "medium_def": "preposition: to, for, in, at, of",
      "lsj_entry": "",
      "short_def_mounce": "",
      "related_words": [],
      "raw_related_numbers": "",
      "freq_list": "",
      "is_proper_noun": false,
      "is_sub_gloss": false,
      "step_parent_code": "H5315G",
      "step_section_type": "primary",
      "decision_group": "G4",
      "action": "exclude",
      "decision_reason": "F2: vocab_count 20899 > particle_ceiling 1000",
      "verses_fetched": false,
      "verse_count": null,
      "testament_coverage": null,
      "meaning_numbered": false,
      "causative_form_present": false,
      "data_quality_flags": [],
      "quality_flag_detail": {},
      "verses": []
    },

    {
      "_comment": "── G5 example: lexically distant (parent not anchor), exclude, no verses ──",
      "code": "G4151",
      "gloss": "spirit/breath: spirit",
      "transliteration": "pneuma",
      "script_form": "πνεῦμα",
      "language": "Greek",
      "vocab_count": 679,
      "medium_def": "wind, breath, spirit",
      "lsj_entry": "πνεῦμα...",
      "short_def_mounce": "wind, breath; spirit",
      "related_words": [],
      "raw_related_numbers": "",
      "freq_list": "",
      "is_proper_noun": false,
      "is_sub_gloss": false,
      "step_parent_code": "G4151",
      "step_section_type": "primary",
      "decision_group": "G5",
      "action": "exclude",
      "decision_reason": "F3x: parent G4151 not in anchor list [H5315G, G5590G], section_type=primary is not sub_gloss/related_term — caught by F3 (primary outside anchor)",
      "verses_fetched": false,
      "verse_count": null,
      "testament_coverage": null,
      "meaning_numbered": false,
      "causative_form_present": false,
      "data_quality_flags": [],
      "quality_flag_detail": {},
      "verses": []
    }

  ]
}
```

**Notes on the example:**

- `_comment` keys are documentation only — the production script does not write them
- `preview_html` values are truncated with `...` for readability; the real output contains the full raw HTML string
- `freq_list` is the raw STEP frequency string; the example shows an abbreviated form
- `verses: []` on excluded terms (G4/G5) — the key is present but the array is empty, so the structure is uniform across all term records
- The `span_label_found` value `"soul"` on H5315G reflects that `span_code_found` = `"H5315G"` which is present in the terms array with `gloss` = `"soul"`. For a sub-gloss match (e.g. `span_code_found` = `"H5315H"`), the label would be `"soul: life"` (from that term's gloss)

---

#### `meta` block
| Field | Value |
|-------|-------|
| `english_anchor` | the word passed in (e.g. `"soul"`) |
| `generated` | ISO date of this run |
| `step_version` | STEP version string (e.g. `"ESV_th"`) |
| `anchor_codes` | the parent codes used as soul-concept anchors (e.g. `["H5315G", "G5590G"]`) |
| `particle_ceiling` | the vocab_count threshold used for G4 exclusion (default 1000) |
| `total_terms_evaluated` | count of all term codes seen in STEP cluster |
| `summary_by_group` | counts per decision group: `{G1: N, G2: N, G2r: N, G3: N, G4: N, G5: N}` |
| `include_codes` | list of codes with action=include |
| `exclude_codes` | list of codes with action=exclude |

---

### Per-term fields (all codes in the STEP cluster)

#### From STEP vocab (`get_vocab_info`)
| Field | Source |
|-------|--------|
| `code` | STEP cluster (resolved canonical form, e.g. `H5315G` not `H5315`) |
| `gloss` | STEP `stepGloss` |
| `transliteration` | STEP `stepTransliteration` |
| `script_form` | STEP `accentedUnicode` — accented Hebrew or Greek unicode |
| `language` | derived from code prefix (`H` → `"Hebrew"`, `G` → `"Greek"`) |
| `vocab_count` | STEP `occurrence_count` — token count (NOT verse count) |
| `medium_def` | STEP `mediumDef` — full definition, HTML stripped, `<br>` → newlines |
| `lsj_entry` | STEP `lsjDefs` — LSJ dictionary text, HTML stripped (Greek only; `""` for Hebrew) |
| `short_def_mounce` | STEP `shortDefMounce` — Mounce short definition (Greek only; `""` for Hebrew) |
| `related_words` | STEP `relatedNos` — list of `{strong, form, gloss, translit}` |
| `raw_related_numbers` | STEP `rawRelatedNumbers` — comma-separated related Strong's string |
| `freq_list` | STEP `freqList` — raw frequency distribution string |
| `is_proper_noun` | STEP vocab flag |

#### From STEP cluster structure
| Field | Value |
|-------|-------|
| `is_sub_gloss` | `true` if this code is a sub-gloss entry of its parent |
| `step_parent_code` | the primary code of the cluster this term belongs to |
| `step_section_type` | `"primary"` / `"sub_gloss"` / `"related_term"` |

#### Derived from STEP data (computed by the script)
| Field | How derived |
|-------|-------------|
| `decision_group` | G1 / G2 / G2r / G3 / G4 / G5 — from filter logic F1–F5 (see below) |
| `action` | `"include"` / `"exclude"` — from decision group (G2r → `"include"`) |
| `decision_reason` | text explanation from the filter that assigned this group |
| `verses_fetched` | `true` for G1/G2/G2r (include terms only); `false` for G3/G4/G5 (excluded — no STEP verse call made) |
| `verse_count` | integer count of verses returned by paginated pull; `null` for excluded terms |
| `testament_coverage` | `"OT_only"` / `"NT_only"` / `"both"` / `null` — derived from `book_code` of fetched verses; `null` for excluded terms |
| `meaning_numbered` | `true` if `medium_def` contains numbered sub-senses (`1)`, `1a)`) |
| `causative_form_present` | `true` if `medium_def` mentions Hiphil or Piel stem |
| `data_quality_flags` | list of flag codes raised for this term (see flag rules per group below) |
| `quality_flag_detail` | dict of flag code → detail text |

---

### Per-verse data (included terms only)

Verse fetching via STEP (`get_verse_records_with_html()`) is performed **only for terms with `action = include`** (G1, G2, G2r). No STEP verse call is made for G3/G4/G5 terms — the decision to exclude them is made entirely from vocab-level data and no verse data is needed.

The `_with_html` variant is used (not `get_verse_records()`) so that the raw preview HTML travels with the data for span filtering without requiring a second API call.

Each verse record contains:
| Field | Source |
|-------|--------|
| `osisId` | STEP canonical verse ID (e.g. `"Gen.31.27"`) |
| `ref` | Human-readable reference (e.g. `"Gen 31:27"`) |
| `book_code` | OSIS book code (e.g. `"Gen"`, `"Matt"`) |
| `chapter` | integer |
| `verse_num` | integer |
| `esv_text` | ESV verse text, HTML stripped |
| `target_word` | the ESV word(s) in the verse whose `<span>` carries this Strong's number |
| `testament` | `"OT"` or `"NT"` — derived from `book_code` |
| `fetched_under_code` | the Strong's code used to fetch this verse (e.g. `"H5315G"`) — needed by Step 4 to populate `wa_verse_term_links.step_subgloss_code` |
| `preview_html` | raw `<span>`-tagged HTML from STEP — retained for span filter (not displayed in .md summary) |
| `span_strong_match` | `1` = span confirmed, `0` = span not found, `null` = no HTML available — output of `apply_span_filter()` against `preview_html` → stored in both `wa_verse_records.span_strong_match` and `wa_verse_term_links.span_strong_match` |
| `span_code_found` | the specific Strong's code from the matching span's `strong=` attribute (e.g. `"H5315H"`) — may differ from `fetched_under_code`; `null` if no match. **Note:** `apply_span_filter()` currently discards the matched code internally — it must be extended to return it alongside `target_word`. → stored as `wa_verse_term_links.step_subgloss_code` |
| `span_label_found` | the English gloss of the matched sub-gloss code (e.g. `"soul: life"`) — **not present in the HTML**. The HTML span `<span strong='H5315E'>soul</span>` carries only the surface word, not the sense label. Resolved by looking up `span_code_found` against the `terms` array in this same JSON and taking that term record's `gloss` field. If `span_code_found` is not present in the terms array (e.g. it is a sibling sub-gloss that was not independently fetched), set to `null` in the Step 1 output and resolve at import time via `get_vocab_info(span_code_found)`. → stored as `wa_verse_term_links.step_subgloss_label` |
| `context_before` | ~5 words of ESV text immediately before `target_word` — extracted from `preview_html` → stored in `wa_verse_records.context_before` |
| `context_after` | ~5 words of ESV text immediately after `target_word` — extracted from `preview_html` → stored in `wa_verse_records.context_after` |

**Span filter logic (from `engine/span_filter.py`):**
- Parses `<span strong='...'>` attributes in the preview HTML
- Match = the queried Strong's code, OR any sub-gloss sharing the same numeric base (e.g. H7965H matches H7965A–F), appears in a non-particle span
- Grammar-particle codes (`H9xxx` / `G9xxx`) are ignored
- Result: `span_strong_match=1` → verse confirmed; `span_strong_match=0` → verse flagged (potential false positive from STEP search)
- Conflict condition: if ALL verses for a term have `span_strong_match=0`, a `SPAN_RESOLUTION_CONFLICT` data quality flag is raised on that term

---

## Span data destination — which fields go to which table

The span filter produces two categories of output. Each targets a different table.

| Field | Value populated | Target table | Target column |
|-------|----------------|-------------|---------------|
| `span_strong_match` | `1` / `0` / `null` | `wa_verse_records` | `span_strong_match` |
| `target_word` | ESV surface form from span text | `wa_verse_records` | `target_word` |
| `context_before` | ~5 words before target word | `wa_verse_records` | `context_before` |
| `context_after` | ~5 words after target word | `wa_verse_records` | `context_after` |
| `span_strong_match` | same value as above | `wa_verse_term_links` | `span_strong_match` |
| `target_word` | same value as above | `wa_verse_term_links` | `target_word` |
| `span_code_found` | matched Strong's code from span `strong=` attribute | `wa_verse_term_links` | `step_subgloss_code` |
| `span_label_found` | gloss of matched sub-gloss code (resolved from terms array) | `wa_verse_term_links` | `step_subgloss_label` |

**Key point:** `span_strong_match` and `target_word` are written to **both** tables because `wa_verse_records` needs them for general verse-level queries while `wa_verse_term_links` needs them for per-(verse, term) span confirmation.

`step_subgloss_code` and `step_subgloss_label` belong only on `wa_verse_term_links` — they are a property of the specific (verse × term) relationship, not of the verse itself.

---

## FK resolution — what the extract JSON must carry for DB import

Step 1 output contains no DB IDs. The import step (Step 4+) must resolve the following cross-references before writing to `wa_verse_term_links`.

### Resolving verse_id (→ `wa_verse_records.id`)

`wa_verse_term_links.verse_id` is a FK to `wa_verse_records.id`.

Resolution at import time:
```sql
SELECT id FROM wa_verse_records
WHERE file_id = :file_id
  AND term_id  = :fetched_under_code
  AND reference = :ref
```
or using canonical fields:
```sql
SELECT id FROM wa_verse_records
WHERE file_id   = :file_id
  AND book_id   = (SELECT id FROM books WHERE osis_code = :book_code)
  AND chapter   = :chapter
  AND verse_num = :verse_num
  AND term_id   = :fetched_under_code
```

Required fields in the extract JSON verse record to support this lookup:
- `osisId` (or `book_code` + `chapter` + `verse_num`)
- `fetched_under_code` — the Strong's code used to fetch this verse

### Resolving term_inv_id (→ `wa_term_inventory.id`)

`wa_verse_term_links.term_inv_id` is a FK to `wa_term_inventory.id`.

In the audit/import context, the term being linked is the one whose verse fetch produced this record. That is `fetched_under_code` for G1 terms (direct sub-glosses), or the term's own `code` for G2/G2r terms.

Resolution at import time:
```sql
SELECT id FROM wa_term_inventory
WHERE file_id = :file_id
  AND (strongs_number = :code OR term_id = :code)
```

Required field in the extract JSON term record:
- `code` — the canonical Strong's code for this term

### UNIQUE constraint

`wa_verse_term_links` has `UNIQUE (verse_id, term_inv_id)`. The import logic must use `INSERT OR IGNORE` or `INSERT OR REPLACE` to handle re-runs. Re-runs should UPDATE the span fields on the existing row rather than inserting duplicates.

---

## Filter Logic (F1–F5)

Filters are applied in order. The first filter that matches determines the group. All decisions are mechanical — no semantic interpretation is applied.

| Filter | Condition | → Group | Action |
|--------|-----------|---------|--------|
| **F1** | `is_proper_noun == true` | G3 | exclude |
| **F2** | `vocab_count > particle_ceiling` (default 1000) | G4 | exclude |
| **F3** | `section_type == "primary"` AND `step_parent_code` NOT in anchor list | G4 | exclude |
| **F4** | `step_parent_code` IN anchor list AND `section_type` in (`"primary"`, `"sub_gloss"`) | G1 | include |
| **F5a** | `step_parent_code` IN anchor list AND `section_type == "related_term"` AND root confirmed (see below) | G2 | include |
| **F5b** | `step_parent_code` IN anchor list AND `section_type == "related_term"` AND root NOT confirmed | G2r | include + flag |
| **F3x** | `step_parent_code` NOT in anchor list AND `section_type` in (`"related_term"`, `"sub_gloss"`) | G5 | exclude |

**Root confirmation rules (F5):**
- **Greek:** `script_form` contains the character `ψ` → psuchē compound positively identified
- **Hebrew:** code is in the confirmed-root set (currently: `H5314` — nāphash verbal root, confirmed NPŠ consonants)
- **All other cases:** root unverifiable from STEP JSON alone → F5b (G2r)

---

## Decision Groups

### G1 — Soul sub-glosses → **include**
**Filter:** F4  
**Verse fetch:** YES  
**Flags raised:**
- `NO_VERSES` if `verse_count == 0` after fetch
- `SPAN_RESOLUTION_CONFLICT` if all fetched verses have `span_strong_match=0`

---

### G2 — Soul root-family (confirmed) → **include**
**Filter:** F5a  
**Verse fetch:** YES  
**Flags raised:**
- `NO_VERSES` if `verse_count == 0` after fetch
- `SPAN_RESOLUTION_CONFLICT` if all fetched verses have `span_strong_match=0`

---

### G2r — Soul STEP-related, root unverified → **include with flag**
**Filter:** F5b  
**Verse fetch:** YES  
**Flags raised:**
- `NOTE_ON_ROOT_FAMILY` always — with detail text: root consonant mismatch explanation (e.g. H5317: NPT ≠ NPŠ)
- `NO_VERSES` if `verse_count == 0` after fetch
- `SPAN_RESOLUTION_CONFLICT` if all fetched verses have `span_strong_match=0`

---

### G3 — Proper nouns → **exclude**
**Filter:** F1  
**Verse fetch:** NO — `verse_count = null`, `testament_coverage = null`  
**Flags raised:** none

---

### G4 — Grammatical particles → **exclude**
**Filter:** F2 or F3  
**Verse fetch:** NO — `verse_count = null`, `testament_coverage = null`  
**Flags raised:** none

---

### G5 — Lexically distant / noise → **exclude**
**Filter:** F3x  
**Verse fetch:** NO — `verse_count = null`, `testament_coverage = null`  
**Flags raised:** none

---

## Soul anchor codes

The two parent clusters everything is measured against:

| Code | Term | Language |
|------|------|----------|
| `H5315G` | nephesh | Hebrew |
| `G5590G` | psuchē | Greek |

---

## Open question — anchor code detection

The decision group logic is keyed on the soul anchor list (`H5315G`, `G5590G`). For other words (e.g. spirit, anger, love) different anchors will apply.

**Two options:**

**Option A — Auto-detect from text search results:**  
The script runs the English text search, identifies the codes with the largest verse counts, and treats those as the anchor parents.  
- Pros: zero manual configuration per word
- Cons: may misidentify the dominant code for ambiguous words

**Option B — Explicitly passed as a parameter:**  
`--anchors H5315G,G5590G`  
- Pros: deterministic, researcher-controlled
- Cons: requires one manual step per word

**Recommendation pending researcher decision.**

---

## Script input/output

```powershell
# Usage
python scripts/word_study_extract.py --word soul

# Optional explicit anchors (if auto-detect not trusted)
python scripts/word_study_extract.py --word soul --anchors H5315G,G5590G
```

Output files written to `research/discovery/`:
- `182_soul_step_data_20260323.json` — full structured data (machine-readable)
- `182_soul_step_data_20260323.md` — summary table (human-readable review)

### Output filename convention

```
{registry_no}_{word}_step_data_{YYYYMMDD}.json
{registry_no}_{word}_step_data_{YYYYMMDD}.md
```

| Part | Format | Example | Source |
|------|--------|---------|--------|
| `registry_no` | 3-digit, zero-padded | `182`, `004`, `072` | `word_registry.id` looked up by word (read-only, single SELECT) |
| `word` | lowercase English word | `soul`, `love`, `anger` | `--word` argument |
| `YYYYMMDD` | ISO date of this run | `20260323` | system date |

Falls back to `000` as the registry prefix if the word is not yet present in `word_registry`.

---

## Status

- [ ] Anchor detection approach confirmed by researcher
- [ ] Script coded
- [ ] Tested against soul
