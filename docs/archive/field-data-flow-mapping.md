# Field-Level Data Flow Mapping
## Session A v9 Automation Engine — Complete Field Provenance Reference

**Purpose:** For every field in every table written by the engine, this document records: where the data originates, which processing mode writes it, the Python file responsible, and the specific function or subroutine that performs the write.

**Modes covered:** NEW_WORD (N1–N19) · GAP_FILL single-word (S1–S8) · BULK_GAP_FILL (S1–S4) · AUDIT_WORD (A1–A10)  
**Engine package:** `engine/`  
**API client:** `analytics/step_client.py`  

---

## How to Read This Document

- **Data Source** describes where the value originates: the STEP REST API field name, a derived/calculated value, a hardcoded constant, or a researcher prompt.
- **Mode — Step** shows which processing mode writes the field and which step number within that mode.
- A blank cell means the mode does not write that field.
- `COALESCE update` means the field is only updated if the existing value is NULL or empty.
- `Phase 2 reserved` means the column is added by migration but intentionally left NULL in Phase 1.

---

## Part 1 — Registration Tables

### 1.1 `word_registry`

The master anchor table. One row per English word being researched.

| Field | NEW_WORD | GAP_FILL (single) | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | — | — | — | — | Pre-set at `--register` | `engine/register.py` | `run_register()` |
| `no` | — | — | — | — | Pre-set at `--register` | `engine/register.py` | `run_register()` |
| `word` | Read N1 | Read S1 | Read S1/S2 | Read A1 | Pre-set at `--register` | `engine/register.py` | `run_register()` |
| `source_list` | Read N9 | — | Read S2 | — | Pre-set at `--register` | `engine/register.py` | `run_register()` |
| `category_hint` | — | — | — | — | Pre-set at `--register` | `engine/register.py` | `run_register()` |
| `phase1_status` | Read N1. Set `'In Progress'` or `'Complete'` at N19 | Read S1. Set final status at S7 | Written `'In Progress'` in S2 Phase A | Not written (retains current). Set `'In Progress'` if audit fails at A10 | Engine logic based on audit result | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N19 · `run_gap_fill()` S7 · `run_audit_word()` A10 |
| `automation_eligible` | Read N1 | — | — | — | Pre-set; not modified | — | — |
| `last_automation_run` | N6: set to `LOCK_SENTINEL` ("IN_PROGRESS"). N19: set to `_now()` UTC timestamp | S1: check for lock; set to `LOCK_SENTINEL`. S7: set to `_now()` | S2 Phase A: set to `_now()` | A10: set to `_now()` | Engine datetime `_now()` | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N6/N19 · `run_gap_fill()` S1/S7 · `run_audit_word()` A10 |
| `automation_run_id` | N19: set to `run_id` | S7: set to `run_id` | S2 Phase A: set to `run_id` | A10: set to `run_id` | `make_run_id()` — formatted `RUN-YYYYMMDD_HHMMss-MODE` | `engine/run_log.py` · called from mode files | `make_run_id()` |
| `phase1_term_count` | N19: count of NEW terms written (`counts["total_terms_new"]`) | S7: re-query `COUNT(*) FROM wa_term_inventory WHERE file_id IN (...)` | Not written | A10: re-query `COUNT(*) FROM wa_term_inventory WHERE file_id IN (...)` | Derived DB count | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N19 · `run_gap_fill()` S7 · `run_audit_word()` A10 |
| `phase1_verse_count` | N19: `counts["total_verses_inserted"]` | S7: re-query confirmed verse count (`span_strong_match=1 OR IS NULL`) | Not written | A10: re-query confirmed verse count | Derived DB count | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N19 · `run_gap_fill()` S7 · `run_audit_word()` A10 |
| `phase1_input_file` | N19: set to `run_id` | Not written | Not written | Not written | `run_id` string | `engine/new_word.py` | `run_new_word()` N19 |
| `strongs_list` | Not written | Not written | S1: populated as JSON array `[{"strong": "H7965", "count": 148}, …]` | Not written | `StepClient.get_strongs_for_word(word)` — text search across ESV, tallies by span | `analytics/step_client.py` · `engine/gap_fill.py` | `StepClient.get_strongs_for_word()` · `run_bulk_gap_fill()` S1 |

---

## Part 2 — Core Word Data Tables

### 2.1 `wa_file_index`

One row per word (per v9; legacy words may have multiple rows for split parts).

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N9: `get_max_id("wa_file_index") + 1` | — | S2 Phase A: `get_max_id("wa_file_index") + 1` | — | Derived sequential ID | `engine/db.py` | `get_max_id()` |
| `filename` | N9: set to `run_id` | — | S2 Phase A: set to `run_id` | — | `run_id` string (not a filesystem path) | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `registry_id` | N9: `str(registry_id)` | — | S2: `str(registry_no)` | — | Input argument (word_registry.no) | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `word_registry_fk` | N9: `reg_row["id"]` (word_registry primary key) | — | S2: `reg["id"]` | — | `word_registry.id` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `word` | N9: `word` from registry | — | S2: `word` from registry | — | `word_registry.word` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `part_number` | N9: NULL | — | S2: NULL | — | Legacy field; not used by v9 | `engine/new_word.py` | `run_new_word()` N9 |
| `total_parts` | N9: NULL | — | S2: NULL | — | Legacy field; not used by v9 | `engine/new_word.py` | `run_new_word()` N9 |
| `is_split` | N9: `0` (hardcoded) | — | S2: `0` (hardcoded) | — | Hardcoded; v9 never splits | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `specification` | N9: `SPECIFICATION` constant (`"Session A v9 Automation"`) | — | S2: same | — | `engine/constants.py` → `SPECIFICATION` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `phase` | N9: `'Phase 1'` (hardcoded) | — | S2: `'Phase 1'` | — | Hardcoded | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `produced_date` | N9: `_today()` (YYYY-MM-DD UTC) | — | S2: `_today()` | — | Engine datetime `_today()` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `translation_used` | N9: `'ESV'` (hardcoded) | — | S2: `'ESV'` | — | Hardcoded | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `source_list` | N9: `reg_row["source_list"]` | — | S2: `reg["source_list"]` | — | `word_registry.source_list` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N9 · `run_bulk_gap_fill()` S2 |
| `testament_coverage` | N9: NULL. N14: set to `'OT_only'`, `'NT_only'`, `'both'`, or NULL | — | — | A9: re-derived from confirmed verses | Derived from `DISTINCT testament` in `wa_verse_records WHERE span_strong_match=1 OR IS NULL` | `engine/new_word.py` · `engine/audit_word.py` | `run_new_word()` N14 · `run_audit_word()` A9 |
| `root_families_in_prior_parts` | Not written | — | — | — | Legacy only; read-only in v9 | — | — |

---

### 2.2 `mti_terms`

Global Strong's number registry. One row per unique Strong's number, owned by the first word that processes it.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N10: `get_max_id("mti_terms") + 1` | — | S2 Phase C: `get_max_id("mti_terms") + 1` | — | Derived sequential ID | `engine/db.py` | `get_max_id()` |
| `strongs_number` | N10: `vocab["strong_number"]` | — | S2 Phase C: `vocab["strong_number"]` | — | STEP REST API: `vocabInfos[0].strongNumber` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `transliteration` | N10: `vocab["transliteration"]` | — | S2 Phase C: `vocab["transliteration"]` | — | STEP REST API: `vocabInfos[0].stepTransliteration` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `gloss` | N10: `vocab["gloss"]` | — | S2 Phase C: `vocab["gloss"]` | — | STEP REST API: `vocabInfos[0].stepGloss` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `language` | N10: `vocab["language"]` | — | S2 Phase C: `vocab["language"]` | — | Derived from Strong's prefix: `"G"` → `"Greek"`, else `"Hebrew"` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `owning_registry` | N10: `str(registry_id)` | — | S2 Phase C: `str(registry_no)` | — | Input arg (`word_registry.no`) | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N10 · `run_bulk_gap_fill()` S2 |
| `owning_word` | N10: `word` | — | S2 Phase C: `word` | — | `word_registry.word` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N10 · `run_bulk_gap_fill()` S2 |
| `owning_part` | N10: NULL | — | S2: NULL | — | Legacy field; not used by v9 | `engine/new_word.py` | `run_new_word()` N10 |
| `word_data_reference` | N10: `str(file_id)` | — | S2 Phase C: `str(file_id)` | — | `wa_file_index.id` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N10 · `run_bulk_gap_fill()` S2 |
| `status` | N10: `'extracted'` (hardcoded) | — | S2: `'extracted'` | — | Hardcoded | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N10 · `run_bulk_gap_fill()` S2 |
| `extraction_date` | N10: `_today()` | — | S2: `_today()` | — | Engine datetime | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N10 · `run_bulk_gap_fill()` S2 |
| `strongs_reconciled` | N10: `1` if resolved ≠ input, else `0` | — | S2: `1` if `resolved != strong`, else `0` | — | Comparison of input Strong's vs STEP-resolved Strong's number | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N10 · `run_bulk_gap_fill()` S2 |
| `also_spelled` | Not written by engine | — | — | — | Architecture v4: removed from automation writes | — | — |

---

### 2.3 `mti_term_cross_refs`

Cross-references recording which words share a Strong's number (XREF terms).

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N13: `get_max_id("mti_term_cross_refs") + 1` | — | S2 Phase A: `get_max_id("mti_term_cross_refs") + 1` | — | Derived sequential ID | `engine/db.py` | `get_max_id()` |
| `mti_term_id` | N13: `mti_terms.id` looked up by strongs_number | — | S2 Phase A: `existing_mt["id"]` | — | `mti_terms.id` (existing row, not newly created) | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N13 · `run_bulk_gap_fill()` S2 Phase A |
| `registry` | N13: `str(registry_id)` | — | S2: `str(registry_no)` | — | Input arg | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N13 · `run_bulk_gap_fill()` S2 |
| `word` | N13: `word` | — | S2: `word` | — | `word_registry.word` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N13 · `run_bulk_gap_fill()` S2 |

> **Note:** Rows are inserted with `INSERT OR IGNORE` — if a cross-ref already exists for this (mti_term_id, registry) pair, no duplicate is created.

---

### 2.4 `wa_term_inventory`

Detailed lexical data for each term, scoped to a specific word file. One row per Strong's number per word.

| Field | NEW_WORD | GAP_FILL (single) | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N11: `get_max_id("wa_term_inventory") + 1` | — | S2 Phase C: `get_max_id("wa_term_inventory") + 1` | — | Derived sequential ID | `engine/db.py` | `get_max_id()` |
| `file_id` | N11: `file_id` | — | S2: `file_id` | — | `wa_file_index.id` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N11 · `run_bulk_gap_fill()` S2 |
| `language` | N11: `vocab["language"]` | — | S2: `vocab["language"]` | A4: `COALESCE` update (only fills if NULL) | Derived from Strong's prefix; `"G"` → `"Greek"`, else `"Hebrew"` | `analytics/step_client.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` · `run_audit_word()` A4 |
| `term_id` | N11: `vocab["strong_number"]` (resolved) | — | S2: `vocab["strong_number"]` | — | STEP REST API: `vocabInfos[0].strongNumber` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `strongs_number` | N11: `vocab["strong_number"]` (resolved) | — | S2: `vocab["strong_number"]` | — | STEP REST API: `vocabInfos[0].strongNumber` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `transliteration` | N11: `vocab["transliteration"]` | — | S2: `vocab["transliteration"]` | A4: `COALESCE(NULLIF(step_search_gloss,''), ?)` | STEP REST API: `vocabInfos[0].stepTransliteration` | `analytics/step_client.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` · `run_audit_word()` A4 |
| `step_search_gloss` | N11: `vocab["gloss"]` | S4: `COALESCE` update if NULL | S2: `vocab["gloss"]` | A4: `COALESCE(NULLIF(step_search_gloss,''), ?)` | STEP REST API: `vocabInfos[0].stepGloss` | `analytics/step_client.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` · `run_gap_fill()` S4 · `run_audit_word()` A4 |
| `word_analysis_gloss` | N11: `vocab["gloss"]` | S4: `COALESCE` update if NULL | S2: `vocab["gloss"]` | A4: `COALESCE(NULLIF(word_analysis_gloss,''), ?)` | STEP REST API: `vocabInfos[0].stepGloss` (same as `step_search_gloss` currently) | `analytics/step_client.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` · `run_gap_fill()` S4 · `run_audit_word()` A4 |
| `occurrence_count` | N11: `vocab["occurrence_count"]` | — | S2: `vocab["occurrence_count"]` | A4: `COALESCE(occurrence_count, ?)` (only fills if NULL) | STEP REST API: `vocabInfos[0].count` (token count, NOT verse count) | `analytics/step_client.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` · `run_audit_word()` A4 |
| `occurrence_count_qualifier` | N18: researcher field-fill (interactive prompt or null if non-interactive) | — | — | — | Researcher input: `'about'` or NULL for exact count | `engine/new_word.py` | `_run_field_fill()` N18 |
| `meaning` | N11: `vocab["medium_def"]` | S4: `UPDATE ... SET meaning=? WHERE id=?` if NULL | S2: `vocab["medium_def"]` | A4: `COALESCE(NULLIF(meaning,''), ?)` | STEP REST API: `vocabInfos[0].mediumDef` — HTML stripped with newlines preserved by `_strip_html_preserve_newlines()` | `analytics/step_client.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` → `_strip_html_preserve_newlines()` · `run_gap_fill()` S4 · `run_audit_word()` A4 |
| `meaning_numbered` | N11: mirrors `medium_def` text | S4: updated alongside `meaning` | S2: `vocab["medium_def"]` | A4: `COALESCE(NULLIF(meaning_numbered,''), ?)` | Same as `meaning` (currently stored as plain text, not yet distinct) | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N11 · `run_gap_fill()` S4 · `run_audit_word()` A4 |
| `lsj_entry` | N11: `vocab["lsj_entry"]` (Greek only; NULL for Hebrew) | S4: `COALESCE(lsj_entry, ?)` update | S2: `vocab["lsj_entry"] or None` | A4: `COALESCE(NULLIF(lsj_entry,''), ?)` | STEP REST API: `vocabInfos[0].lsjDefs` — HTML stripped. Greek terms only. | `analytics/step_client.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` → `_strip_html_preserve_newlines()` · `run_gap_fill()` S4 · `run_audit_word()` A4 |
| `short_def_mounce` | N11: `vocab["short_def_mounce"]` (Greek only) | — | S2: `vocab["short_def_mounce"] or None` | A4: `COALESCE(NULLIF(short_def_mounce,''), ?)` | STEP REST API: `vocabInfos[0].shortDefMounce` — Greek only; empty string for Hebrew | `analytics/step_client.py` · `engine/audit_word.py` | `StepClient.get_vocab_info()` · `run_audit_word()` A4 |
| `testament` | N14: `'OT'`, `'NT'`, `'both'`, or NULL — derived per-term | — | — | — | Derived: `DISTINCT testament FROM wa_verse_records WHERE term_inv_id=? AND span_strong_match=1` | `engine/new_word.py` | `run_new_word()` N14 |
| `causative_form_present` | N11: `vocab["causative_form_present"]` — `1` if Hiphil or Piel found in `medium_def` | — | S2: `1 if vocab.get("causative_form_present") else 0` | — | Derived in `StepClient`: `re.search(r'\b(Hiphil\|Piel)\b', medium_def, re.IGNORECASE)` | `analytics/step_client.py` | `StepClient.get_vocab_info()` |
| `also_spelled` | N18: researcher field-fill for Hebrew terms only (interactive prompt or null). Asks researcher to check STEP UI. | — | — | — | Researcher input: JSON string or NULL | `engine/new_word.py` | `_run_field_fill()` N18 |
| `status_note` | N11: last 3 error messages if any errors occurred during N7/N8 fetches, else NULL | — | — | — | Engine `errors` list | `engine/new_word.py` | `run_new_word()` N11 |
| `parsed_meaning_id` | N15: set to `wa_meaning_parsed.id` via `run_parser()` | S4: set via `run_parser_for_file()` | S4: set via `run_parser_for_file()` | A5: reset via `run_parser_for_file()` | FK to `wa_meaning_parsed.id` | `engine/meaning_parser.py` | `run_parser()` — final `UPDATE wa_term_inventory SET parsed_meaning_id=?` |
| `god_as_subject` | Not written by engine | — | — | — | Judgment-deferred; Phase 2 researcher field | — | — |
| `somatic_link` | Not written by engine | — | — | — | Judgment-deferred; Phase 2 researcher field | — | — |

---

### 2.5 `wa_term_related_words`

Related words for each term as returned by the STEP API. One row per related Strong's number.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `term_inv_id` | N11: `ti_id` | — | S2 Phase C: `ti_id` | — | `wa_term_inventory.id` | `engine/new_word.py` · `engine/gap_fill.py` | `run_new_word()` N11 · `run_bulk_gap_fill()` S2 |
| `gloss` | N11: `rw["gloss"]` | — | S2: `rw.get("gloss")` | — | STEP REST API: `vocabInfos[0].relatedNos[i].gloss` | `analytics/step_client.py` | `StepClient.get_vocab_info()` → `related_words` list |
| `transliteration` | N11: `rw["translit"]` | — | S2: `rw.get("translit")` | — | STEP REST API: `vocabInfos[0].relatedNos[i].stepTransliteration` | `analytics/step_client.py` | `StepClient.get_vocab_info()` → `related_words` list |
| `strongs_number` | N11: `rw["strong"]` | — | S2: `rw.get("strong")` | — | STEP REST API: `vocabInfos[0].relatedNos[i].strongNumber` | `analytics/step_client.py` | `StepClient.get_vocab_info()` → `related_words` list |

---

### 2.6 `wa_verse_records`

One row per verse per term. Only span-confirmed verses are stored (span_strong_match = 1).

| Field | NEW_WORD | GAP_FILL (single) | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N12: `get_max_id("wa_verse_records") + 1` | S3: `get_max_id(...) + 1` | S3: `get_max_id(...) + 1` | A3a: `get_max_id(...) + 1` (INSERT only) | Derived sequential ID | `engine/db.py` | `get_max_id()` |
| `file_id` | N12: `file_id` | S3: `file_id` | S3: `file_id` | A3a: `fid` | `wa_file_index.id` | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N12 · `run_gap_fill()` S3 · `run_audit_word()` A3a |
| `term_inv_id` | N12: `ti_id` | S3: `ti_id` | S3: `ti_id` | A3a: `ti_id` | `wa_term_inventory.id` | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N12 · `run_gap_fill()` S3 · `run_audit_word()` A3a |
| `term_id` | N12: strongs number | S3: strongs | S3: strongs | A3a: strongs | Strong's number string | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N12 · `run_gap_fill()` S3 · `run_audit_word()` A3a |
| `transliteration` | N12: `vocab_map[strongs]["transliteration"]` | S3: `ti_row["transliteration"]` | S3: `row["transliteration"]` | A3a: `ti["transliteration"]` | `wa_term_inventory.transliteration` (already stored) | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N12 · `run_gap_fill()` S3 · `run_audit_word()` A3a |
| `book_id` | N12: `get_book_id(rec["book_code"])` | S3: `get_book_id(...)` | S3: `get_book_id(...)` | A3a: `get_book_id(...)` | `books.id` looked up via `book_code_variants` table by OSIS book code | `engine/db.py` | `get_book_id()` |
| `reference` | N12: `rec["ref"]` | S3: `rec["ref"]` | S3: `rec["ref"]` | A3a: `ref` (from step_verses) | STEP REST API: `results[i]["key"]` (e.g. `"Gen 31:27"`) | `analytics/step_client.py` | `StepClient.get_verse_records_with_html()` |
| `chapter` | N12: `rec["chapter"]` | S3: `rec["chapter"]` | S3: `rec["chapter"]` | A3a: `rec["chapter"]` | Parsed from OSIS ID: `_parse_osisid("Gen.31.27")` → `31` | `analytics/step_client.py` | `StepClient._parse_osisid()` |
| `verse_num` | N12: `rec["verse_num"]` | S3: `rec["verse_num"]` | S3: `rec["verse_num"]` | A3a: `rec["verse_num"]` | Parsed from OSIS ID: `_parse_osisid("Gen.31.27")` → `27` | `analytics/step_client.py` | `StepClient._parse_osisid()` |
| `testament` | N12: `rec["testament"]` | S3: `rec["testament"]` | S3: `rec["testament"]` | A3a: `rec["testament"]` | Derived in StepClient: `"NT"` if `book_code in _NT_BOOKS` else `"OT"` | `analytics/step_client.py` | `StepClient.get_verse_records_with_html()` |
| `translation` | N12: `'ESV'` hardcoded | S3: `'ESV'` | S3: `'ESV'` | A3a: `'ESV'` | Hardcoded (STEP version is always ESV in these runs) | `engine/new_word.py` · `engine/gap_fill.py` · `engine/audit_word.py` | `run_new_word()` N12 · all S3/A3a inserts |
| `verse_text` | N12: `rec["esv_text"]` | S3: `rec["esv_text"]` | S3: `rec["esv_text"]` | A3a INSERT: `rec["esv_text"]`. UPDATE: `verse_text=?` if `rec.get("esv_text")` | STEP REST API: `results[i]["preview"]` — all HTML tags stripped by `_strip_html()` | `analytics/step_client.py` | `StepClient._strip_html()` |
| `target_word` | N12: `rec.get("target_word", "")` | S3: `rec.get("target_word", "")` | S3: `rec.get("target_word", "")` | A3a INSERT: `rec.get("target_word","")`. UPDATE: overwritten if `rec.get("target_word")` | Extracted from span HTML: text content of the `<span>` tag whose `strong=` attribute contains the queried Strong's | `engine/span_filter.py` | `apply_span_filter()` — returns `target_word` from matching span text |
| `span_strong_match` | N12: `rec.get("span_strong_match", 1)` — only matched records reach N12 | S3: same | S3: same | A3a INSERT: `1` (span-confirmed). UPDATE: set to current filter result. ORPHAN: set to `-1` | `filter_verse_records()` result: `1`=span matched, `0`=span present but no match, `None`=no HTML available, `-1`=in DB but absent from STEP (AUDIT_WORD orphan) | `engine/span_filter.py` | `filter_verse_records()` and `apply_span_filter()` |
| `context_before` | N12: NULL | S3: NULL | S3: NULL | A3a: NULL | Phase 2 reserved — not populated in Phase 1 | — | — |
| `context_after` | N12: NULL | S3: NULL | S3: NULL | A3a: NULL | Phase 2 reserved — not populated in Phase 1 | — | — |
| `note` | Not written by engine | — | — | — | Phase 2 reserved — researcher annotation field | — | — |
| `claude_output` | Not written by engine | — | — | — | Phase 2 reserved — AI analysis output field | — | — |

---

## Part 3 — Meaning Parse Tables

### 3.1 `wa_meaning_parsed`

Root parse record — one row per term. Created at N15 (NEW_WORD), S4 (GAP_FILL), or A5 (AUDIT_WORD). Re-parse deletes and re-inserts (idempotent).

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N15: `get_max_id("wa_meaning_parsed") + 1` | S4: via `run_parser()` | S4: via `run_parser()` | A5: via `run_parser()` | Derived sequential ID | `engine/db.py` | `get_max_id()` |
| `term_inv_id` | N15: `term["id"]` | S4: `term_inv_id` arg | S4: `term_inv_id` arg | A5: `term["id"]` | `wa_term_inventory.id` | `engine/meaning_parser.py` | `run_parser()` |
| `strongs_number` | N15: `vocab["strong_number"]` | S4: vocab key | S4: vocab key | A5: vocab key | Strong's number string | `engine/meaning_parser.py` | `run_parser()` |
| `language` | N15: `vocab["language"]` | S4: `vocab["language"]` | S4: same | A5: same | Derived from vocab dict | `engine/meaning_parser.py` | `run_parser()` → `parse_term()` |
| `top_sense_count` | N15: count of `level_depth=1` AND `is_stem_label=0` nodes | S4: same | S4: same | A5: same | `parse_term()`: `sum(1 for n in sense_nodes if n["level_depth"]==1 and not n["is_stem_label"])` | `engine/meaning_parser.py` | `parse_term()` |
| `stem_count` | N15: `len(stem_nodes)` | S4: same | S4: same | A5: same | `parse_term()`: number of distinct Hebrew stems detected | `engine/meaning_parser.py` | `parse_term()` |
| `has_causative_stem` | N15: `1` if Hiphil or Piel stem found in `stem_nodes` OR in `meaning` text | S4: same | S4: same | A5: same | `parse_term()`: `any(n["stem_label"] in ("Hiphil","Piel") for n in stem_nodes) OR re.search(r"\b(Hiphil\|Piel)\b", meaning)` | `engine/meaning_parser.py` | `parse_term()` |
| `has_domain_tags` | N15: `0` (hardcoded; not yet implemented) | S4: `0` | S4: `0` | A5: `0` | Hardcoded; domain tag extraction not yet implemented | `engine/meaning_parser.py` | `parse_term()` |
| `parsed_at` | N15: `_now()` | S4: `_now()` | S4: `_now()` | A5: `_now()` | Engine UTC timestamp | `engine/meaning_parser.py` | `run_parser()` → `_now()` |
| `parse_version` | N15: `PARSER_VERSION` | S4: same | S4: same | A5: same | `engine/constants.py` → `PARSER_VERSION` (currently `"1.0.0"`) | `engine/meaning_parser.py` | `run_parser()` |
| `parse_warnings` | N15: JSON list of warnings (e.g. `["PROSE_ONLY"]`) or NULL | S4: same | S4: same | A5: same | Generated during `_parse_hebrew_numbered()`, `_parse_hebrew_prose()`, or `_parse_greek_prose()` | `engine/meaning_parser.py` | `parse_term()` |

---

### 3.2 `wa_meaning_sense`

Sense tree nodes — one row per numbered sense from the meaning definition.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N15: AUTOINCREMENT | S4: auto | S4: auto | A5: auto | SQLite AUTOINCREMENT | `engine/meaning_parser.py` | `run_parser()` |
| `parsed_meaning_id` | N15: `wa_meaning_parsed.id` | S4: same | S4: same | A5: same | FK to parent record | `engine/meaning_parser.py` | `run_parser()` |
| `level_code` | N15: e.g. `"1"`, `"1a"`, `"2b1"`, `"qal"` (stem labels lowercased) | S4: same | S4: same | A5: same | Parsed from meaning text using `_OUTLINE_RE` regex `r"^(\d+[a-z0-9]*)\)"` | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |
| `level_depth` | N15: int — depth derived from `level_code` structure | S4: same | S4: same | A5: same | `len(re.sub(r"\d","",code)) + 1` — counts alphabetic characters in code | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |
| `parent_level_code` | N15: parent code or NULL for roots | S4: same | S4: same | A5: same | `_parent_level_code(code)` — truncates last alphanumeric segment | `engine/meaning_parser.py` | `_parent_level_code()` |
| `sense_text` | N15: text of that meaning line (continuation lines appended) | S4: same | S4: same | A5: same | Text after the level code prefix in the `medium_def` string | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` · `_parse_hebrew_prose()` · `_parse_greek_prose()` |
| `is_stem_label` | N15: `1` if this node is a Hebrew stem label, `0` otherwise | S4: same | S4: same | A5: same | `_STEM_LABEL_RE` regex match: `r"^\s*\((Qal\|Niphal\|Piel\|…)\)\s*$"` | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |
| `stem_label` | N15: e.g. `"Qal"`, `"Hiphil"` — or NULL | S4: same | S4: same | A5: same | Stem name from `_STEM_LABEL_RE` match | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |
| `domain_tag` | N15: NULL (not yet implemented) | S4: NULL | S4: NULL | A5: NULL | Not yet populated | `engine/meaning_parser.py` | — |
| `sort_order` | N15: sequential integer per loop | S4: same | S4: same | A5: same | Loop counter `sort_order` incremented per line during parse | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |

---

### 3.3 `wa_meaning_stem`

Hebrew stem records — one row per detected stem (Qal, Niphal, Hiphil, etc.) per term.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N15: AUTOINCREMENT | S4: auto | S4: auto | A5: auto | SQLite AUTOINCREMENT | `engine/meaning_parser.py` | `run_parser()` |
| `parsed_meaning_id` | N15: `wa_meaning_parsed.id` | S4: same | S4: same | A5: same | FK to parent record | `engine/meaning_parser.py` | `run_parser()` |
| `stem_name` | N15: e.g. `"Qal"`, `"Hiphil"` | S4: same | S4: same | A5: same | Hebrew stem label detected by `_STEM_LABEL_RE` | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |
| `stem_type` | N15: `"simple"`, `"passive"`, `"causative"`, `"reflexive"`, or `"other"` | S4: same | S4: same | A5: same | `_STEM_TYPE` dict lookup: `{"Qal":"simple","Niphal":"passive","Hiphil":"causative",…}` | `engine/meaning_parser.py` | `run_parser()` → `_STEM_TYPE` dict |
| `sense_count` | N15: count of child sense nodes under this stem during parse | S4: same | S4: same | A5: same | Incremented in `stems[stem_name]["sense_count"]` per outline match under the stem | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |
| `top_sense_text` | N15: first child sense text (max 120 chars) | S4: same | S4: same | A5: same | `stems[stem_name]["top_sense_text"]` — set on first outline match under the stem | `engine/meaning_parser.py` | `_parse_hebrew_numbered()` |

---

### 3.4 `wa_lsj_parsed`

Structured LSJ (Liddell-Scott-Jones) entry — Greek terms only. One row per term.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N15: AUTOINCREMENT | S4: auto | S4: auto | A5: auto | SQLite AUTOINCREMENT | `engine/meaning_parser.py` | `run_parser()` |
| `term_inv_id` | N15: `term_inv_id` | S4: same | S4: same | A5: same | `wa_term_inventory.id` | `engine/meaning_parser.py` | `run_parser()` |
| `raw_lsj` | N15: `vocab["lsj_entry"]` | S4: same | S4: same | A5: same | `wa_term_inventory.lsj_entry` (already stored) | `engine/meaning_parser.py` | `run_parser()` |
| `lsj_gloss` | N15: first segment before `"."` in `lsj_entry` | S4: same | S4: same | A5: same | `_parse_lsj()`: `re.split(r"\.\s+", lsj_text, maxsplit=1)[0]` | `engine/meaning_parser.py` | `_parse_lsj()` |
| `lsj_domains` | N15: JSON array of bracketed abbreviations | S4: same | S4: same | A5: same | `_parse_lsj()`: `re.findall(r"\[([A-Za-z0-9 ,]+?)\]", lsj_text)` | `engine/meaning_parser.py` | `_parse_lsj()` |
| `lsj_philosophical_note` | N15: semicolon-joined philosopher names found in text | S4: same | S4: same | A5: same | `_parse_lsj()`: presence check for `["Plato","Aristotle","Plut","Philo","Josephus",…]` | `engine/meaning_parser.py` | `_parse_lsj()` |
| `lsj_etymology_note` | N15: first 2 etymology sentences | S4: same | S4: same | A5: same | `_parse_lsj()`: sentences containing `["from","deriv","root","akin","cogn"]` | `engine/meaning_parser.py` | `_parse_lsj()` |
| `lsj_cognate_forms` | N15: JSON array of cognate Greek forms | S4: same | S4: same | A5: same | `_parse_lsj()`: `re.findall(r"\b([A-Z][a-z]+ós\|[A-Z][a-z]+ē\|[A-Z][a-z]+on)\b", lsj_text)` | `engine/meaning_parser.py` | `_parse_lsj()` |
| `parsed_at` | N15: `_now()` | S4: `_now()` | S4: `_now()` | A5: `_now()` | Engine UTC timestamp | `engine/meaning_parser.py` | `run_parser()` → `_now()` |
| `parse_version` | N15: `PARSER_VERSION` | S4: same | S4: same | A5: same | `engine/constants.py` → `PARSER_VERSION` | `engine/meaning_parser.py` | `run_parser()` |

---

## Part 4 — Quality Flags

### 4.1 `wa_data_quality_flags`

One row per flag per term. Written by the flag engine (N16/S5/A6) and by AUDIT_WORD A8.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N16: AUTOINCREMENT | S5: auto | S4: auto | A6: auto; A8: auto | SQLite AUTOINCREMENT | `engine/flag_engine.py` · `engine/audit_word.py` | `_write_quality_flag()` · `run_audit_word()` A8 |
| `file_id` | N16: `file_id` | S5: `file_id` | S4: `file_id` | A6: `file_id`; A8: `file_id` | `wa_file_index.id` | `engine/flag_engine.py` · `engine/audit_word.py` | `_write_quality_flag()` · `run_audit_word()` A8 |
| `term_id` | N16: `strongs` string | S5: `strongs` | S4: `strongs` | A6: `strongs`; A8: NULL | Strong's number (or NULL for word-level A8 flag) | `engine/flag_engine.py` · `engine/audit_word.py` | `_write_quality_flag()` |
| `flag_id` | N16: from `_flag_id()` cache | S5: same | S4: same | A6: same; A8: specific flag id | `wa_quality_flag_types.id` — looked up by `flag_code` | `engine/flag_engine.py` · `engine/audit_word.py` | `_flag_id()` cache function · `run_audit_word()` A8 |
| `description` | N16: generated message per flag type | S5: same | S4: same | A6: same; A8: `"AUDIT_WORD A3a verse sync: inserted=N updated=N orphans_marked=N"` | Engine-generated string | `engine/flag_engine.py` · `engine/audit_word.py` | `_write_quality_flag()` · `run_audit_word()` A8 |

**Flags written by `run_flag_engine()` (called at N16/S5/A6):**

| Flag Code | Condition | `wa_quality_flag_types.id` |
|---|---|---|
| `HIGH_FREQUENCY_ANCHOR` | `occurrence_count >= 500` (`HIGH_FREQ_THRESHOLD` in constants.py) | Looked up by code |
| `THIN_DATA` | `0 < occurrence_count < 20` (`THIN_DATA_THRESHOLD`) | Looked up by code |
| `SPAN_RESOLUTION_CONFLICT` | Term was in `queued_span_conflicts` set (from fetch step) | id=23 |
| `SMALL_VERSE_SAMPLE` | `0 < confirmed_verse_count < 5` (`SMALL_VERSE_SAMPLE_THRESHOLD`) | Looked up by code |
| `NO_VERSES` | `confirmed_verse_count == 0` AND not a span conflict | Looked up by code |
| `NO_WORD_ANALYSIS` | `meaning IS NULL` | Looked up by code |

**Flag written by `run_audit_word()` A8:**

| Flag Code | Condition | Written by |
|---|---|---|
| `SPAN_BACK_POPULATED` | A3a ran AND `backpop_count > 0` AND not `skip_span_backpop` | `engine/audit_word.py` `run_audit_word()` A8 |

---

## Part 5 — Engine Control Tables

### 5.1 `engine_run_log`

One row per engine run. Opened at mode start; closed at mode end.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | AUTOINCREMENT | auto | auto | auto | SQLite AUTOINCREMENT | `engine/run_log.py` | `open_run()` |
| `run_id` | `make_run_id("NEW_WORD")` → `"RUN-YYYYMMDD_HHMMss-NEW_WORD"` | `make_run_id("GAP_FILL")` | `make_run_id("BULK_GAP_FILL")` | `make_run_id("AUDIT_WORD")` | UTC timestamp + mode string | `engine/run_log.py` | `make_run_id()` |
| `mode` | `"NEW_WORD"` | `"GAP_FILL"` | `"GAP_FILL"` | `"AUDIT_WORD"` | Hardcoded mode string | `engine/run_log.py` | `open_run()` |
| `target_registry_ids` | `str(registry_id)` | `str(registry_id)` | `""` (all pending) | `str(registry_id)` | Input arg | `engine/run_log.py` | `open_run()` |
| `started_at` | `_now()` at mode start | same | same | same | UTC timestamp | `engine/run_log.py` | `open_run()` |
| `completed_at` | `_now()` at N19 | `_now()` at S8 | `_now()` | `_now()` at A10 | UTC timestamp | `engine/run_log.py` | `close_run()` |
| `outcome` | `"COMPLETE"` / `"PARTIAL"` / `"STOPPED"` | `"COMPLETE"` / `"STOPPED"` | same | same | Engine result logic | `engine/run_log.py` | `close_run()` |
| `words_attempted` | `1` | `1` | count | `1` | `counts["words_attempted"]` | `engine/run_log.py` | `close_run()` |
| `words_complete` | `1` if PASS, else `0` | `1` if complete | count | `1` | `counts["words_complete"]` | `engine/run_log.py` | `close_run()` |
| `words_stopped` | `1` if STOP | `1` if stopped | count | `1` if stopped | `counts["words_stopped"]` | `engine/run_log.py` | `close_run()` |
| `total_terms_new` | count of NEW Strong's written | `0` (not tracked) | count | `0` | `counts["total_terms_new"]` | `engine/run_log.py` | `close_run()` |
| `total_terms_xref` | count of XREF terms | `0` | count | `0` | `counts["total_terms_xref"]` | `engine/run_log.py` | `close_run()` |
| `total_verses_inserted` | verse record count | verse count from S3 | verse count | `0` | `counts["total_verses_inserted"]` | `engine/run_log.py` | `close_run()` |
| `total_verses_filtered` | filtered verse count | filtered count | filtered count | `0` | `counts["total_verses_filtered"]` | `engine/run_log.py` | `close_run()` |
| `total_meanings_parsed` | count from `run_parser_for_file()` | count from S4 | count | count from A5 | `counts["total_meanings_parsed"]` | `engine/run_log.py` | `close_run()` |
| `error_detail` | JSON list of error messages, or NULL | same | same | same | `counts["errors"]` list | `engine/run_log.py` | `close_run()` |
| `resume_from` | Not written (reserved) | — | — | — | Reserved for future resume support | — | — |

---

### 5.2 `engine_stream_checkpoint`

Written only in GAP_FILL modes. One row per stream per run (upserted via `upsert_checkpoint()`).

| Field | GAP_FILL (single) | BULK_GAP_FILL | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|
| `id` | AUTOINCREMENT | auto | SQLite AUTOINCREMENT | `engine/run_log.py` | `upsert_checkpoint()` |
| `run_id` | `run_id` | `run_id` | Engine run_id | `engine/run_log.py` | `upsert_checkpoint()` |
| `stream_name` | `"S3"`, `"S4"`, `"S5"`, `"S6"` | `"S1"`, `"S2"`, `"S3"`, `"S4"` | Hardcoded stream identifier | `engine/run_log.py` | `upsert_checkpoint()` |
| `status` | `"running"` then `"complete"` (or `"failed"`) | same | Engine logic | `engine/run_log.py` | `upsert_checkpoint()` |
| `last_registry_id` | NULL in current implementation | NULL | Optional checkpoint resumption data | `engine/run_log.py` | `upsert_checkpoint()` |
| `last_strong` | NULL in current implementation | NULL | Optional checkpoint resumption data | `engine/run_log.py` | `upsert_checkpoint()` |
| `rows_written` | Count of rows written in that stream | same | `rows_written` arg | `engine/run_log.py` | `upsert_checkpoint()` |
| `rows_filtered` | Filtered verse count (S3 only) | same for S3 | `rows_filtered` arg | `engine/run_log.py` | `upsert_checkpoint()` |
| `error_detail` | NULL in normal operation | NULL | Error string if stream failed | `engine/run_log.py` | `upsert_checkpoint()` |
| `started_at` | `_now()` at stream start | same | UTC timestamp on first upsert | `engine/run_log.py` | `upsert_checkpoint()` |
| `completed_at` | `_now()` when status becomes `"complete"` or `"failed"` | same | UTC timestamp on status change | `engine/run_log.py` | `upsert_checkpoint()` |

---

### 5.3 `word_run_state`

Per-word audit snapshot. One row written after each audit run.

| Field | NEW_WORD | GAP_FILL | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N17: AUTOINCREMENT | S6: auto | S4: auto | A7: auto | SQLite AUTOINCREMENT | `engine/run_log.py` | `write_word_run_state()` |
| `run_id` | N17: `run_id` | S6: `run_id` | S4: `run_id` | A7: `run_id` | Engine run_id | `engine/run_log.py` | `write_word_run_state()` |
| `registry_id` | N17: `str(registry_id).zfill(3)` | S6: same | S4: same | A7: same | Input arg, zero-padded to 3 digits | `engine/run_log.py` | `write_word_run_state()` |
| `word` | N17: `word` | S6: `word` | S4: `word` | A7: `word` | `word_registry.word` | `engine/run_log.py` | `write_word_run_state()` |
| `phase_reached` | N17: `"AUDIT"` | S6: `"GAP_FILL_S6"` | S4: `"GAP_FILL_S6"` | A7: `"AUDIT_WORD_A7"` | Hardcoded per mode | `engine/run_log.py` | `write_word_run_state()` |
| `audit_result` | N17: `"PASS"` / `"REVIEW"` / `"STOP"` | S6: same | S4: same | A7: same | `run_audit()` overall result | `engine/audit.py` | `run_audit()` |
| `audit_detail` | N17: JSON object — `{check_id: {r: result, d: detail}, …}` for all WR-01 to WR-20 | S6: same | S4: same | A7: same | All 20 audit checks and their results | `engine/run_log.py` · `engine/audit.py` | `write_word_run_state()` · `run_audit()` |
| `stop_reason` | N17: stop reason string or NULL | S6: same | S4: same | A7: same | From `run_audit()["stop_reason"]` | `engine/audit.py` | `run_audit()` |
| `researcher_approved` | Not written (defaults to `0`) | — | — | — | Researcher sign-off field; not set by engine | — | — |
| `approved_by` | Not written | — | — | — | Researcher sign-off field | — | — |
| `approved_at` | Not written | — | — | — | Researcher sign-off field | — | — |

---

### 5.4 `term_fetch_log`

Per-term record of each STEP API call. Written during vocab and verse fetch steps.

| Field | NEW_WORD | GAP_FILL (single) | BULK_GAP_FILL | AUDIT_WORD | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|---|---|---|
| `id` | N7/N8: AUTOINCREMENT | S3: auto | S2/S3: auto | Not written | SQLite AUTOINCREMENT | `engine/run_log.py` | `log_fetch()` |
| `run_id` | N7/N8: `run_id` | S3: `run_id` | S2/S3: `run_id` | — | Engine run_id | `engine/run_log.py` | `log_fetch()` |
| `registry_id` | N7/N8: `str(registry_id)` | S3: `registry_id` | S2: `registry_no` · S3: `registry_no` | — | Input arg | `engine/run_log.py` | `log_fetch()` |
| `strongs_input` | N7: the queried Strong's (as supplied) | S3: `strongs` | S2/S3: `strongs` | — | Input Strong's number | `engine/run_log.py` | `log_fetch()` |
| `strongs_resolved` | N7: `vocab["strong_number"]` — may differ from input | S3: `strongs` (same in single mode) | S2: `vocab["strong_number"]` · S3: `strongs` | — | STEP API resolved Strong's | `engine/run_log.py` | `log_fetch()` |
| `suffix_resolution` | N7: `1` if resolved ≠ input, else `0` | S3: `0` | S2: `1 if resolved != strong else 0` · S3: `0` | — | Comparison flag | `engine/run_log.py` | `log_fetch()` |
| `vocab_status` | N7: `"ok"` / `"failed"`. N13: `"xref"` for XREF terms | S3: `"ok"` | S2: `"ok"` / `"failed"` / `"xref"` | — | Engine logic | `engine/run_log.py` | `log_fetch()` |
| `verse_status` | N8: `"ok"` / `"zero_results"` | S3: `"ok"` / `"zero_results"` | S3: `"ok"` / `"zero_results"` | — | `len(stored) == 0` check | `engine/run_log.py` | `log_fetch()` |
| `verse_count_fetched` | N8: `len(raw_records)` | S3: `len(raw_records)` | S3: `len(raw_records)` | — | `StepClient.get_verse_records_with_html()` result count | `engine/run_log.py` | `log_fetch()` |
| `verse_count_stored` | N8: `len(filter_result["stored"])` | S3: `len(stored)` | S3: `len(stored)` | — | `filter_verse_records()` stored count | `engine/run_log.py` | `log_fetch()` |
| `verse_count_filtered` | N8: `len(filter_result["filtered"])` | S3: `len(filter_result["filtered"])` | S3: `len(filtered_recs)` | — | `filter_verse_records()` filtered count | `engine/run_log.py` | `log_fetch()` |
| `span_conflict` | N8: `1` if `filter_result["conflict"]` else `0` | S3: `1 if conflict else 0` | S3: `1 if conflict else 0` | — | `filter_verse_records()` conflict flag | `engine/run_log.py` | `log_fetch()` |
| `api_warnings` | N7: JSON list of warnings, or NULL | S3: NULL | S2: `["vocab fetch returned empty"]` if failed, else NULL | — | Engine warning messages | `engine/run_log.py` | `log_fetch()` |
| `fetched_at` | N7/N8: `_now()` | S3: `_now()` | S2/S3: `_now()` | — | UTC timestamp | `engine/run_log.py` | `log_fetch()` |

---

### 5.5 `schema_version`

Single row. Created by M01 migration. Updated by each migration step.

| Field | Written by | Data Source | Py File | Function/Subroutine |
|---|---|---|---|---|
| `id` | M01: `1` (fixed) | Hardcoded | `engine/migrate.py` | `_m01()` |
| `version_code` | M01: `"2.2.0"`. Each migration updates to target version at end | Migration logic | `engine/migrate.py` | `run_migrations()` → final `UPDATE` |
| `applied_at` | M01: `_now()`. Updated by each migration | UTC timestamp | `engine/migrate.py` | `_m01()` and `run_migrations()` |
| `migration_history` | Running JSON array of applied migration refs | Accumulated by `run_migrations()` | `engine/migrate.py` | `run_migrations()` |
| `engine_min_version` | Not written by current implementation | — | — | — |

---

## Part 6 — Span Filter Logic Reference

The span filter (`engine/span_filter.py`) is the core mechanism determining which verses are stored. It is called from three places:

| Call Site | Mode | Step | Function Called |
|---|---|---|---|
| `new_word.py` | NEW_WORD | N8 — after `client.get_verse_records_with_html()` | `filter_verse_records(raw_records, resolved, html_map)` |
| `gap_fill.py` | GAP_FILL / BULK_GAP_FILL | S3 — after `client.get_verse_records_with_html()` | `filter_verse_records(raw_records, resolved, html_map)` |
| `audit_word.py` | AUDIT_WORD | A3a — for every term in every file | `filter_verse_records(raw_records, strongs, html_map)` |

**Filter logic in `filter_verse_records(raw_records, queried_strong, raw_html_map)`:**

1. For each verse record, look up `raw_html_map[osisId]` for its preview HTML.
2. If HTML is absent, the record is passed through as `span_strong_match = None` (treated as confirmed for legacy compatibility).
3. Call `apply_span_filter(html, queried_strong)` which:
   a. Parses all `<span … strong="…">word</span>` tags via `_parse_spans()`.
   b. Checks each span's `strong=` list (excluding H9xxx / G9xxx grammatical prefixes).
   c. Returns `match=True` if `queried_strong` appears directly, OR if the span contains any code sharing the same numeric base (e.g. `H7965A` satisfies query `H7965H`).
   d. Returns `target_word` from the text content of the first matching span.
4. Records with `match=True` → `stored` list with `span_strong_match=1`.
5. Records with `match=False` → `filtered` list with `span_strong_match=0`.
6. If `stored` is empty and `filtered` is non-empty → `conflict=True` (SPAN_RESOLUTION_CONFLICT).

---

## Part 7 — STEP REST API Field Map

All data originating from the STEP API. Source: `analytics/step_client.py`.

### From `StepClient.get_vocab_info(strong)`

| STEP JSON Field | `StepClient` dict key | Written to DB field | Table |
|---|---|---|---|
| `vocabInfos[0].strongNumber` | `strong_number` | `strongs_number` (resolved) | `mti_terms`, `wa_term_inventory` |
| _derived from `strongNumber` prefix_ | `language` | `language` | `mti_terms`, `wa_term_inventory` |
| `vocabInfos[0].stepTransliteration` | `transliteration` | `transliteration` | `mti_terms`, `wa_term_inventory` |
| `vocabInfos[0].stepGloss` | `gloss` | `step_search_gloss`, `word_analysis_gloss`, `gloss` | `wa_term_inventory`, `mti_terms` |
| `vocabInfos[0].count` | `occurrence_count` | `occurrence_count` | `wa_term_inventory` |
| `vocabInfos[0].mediumDef` (HTML stripped) | `medium_def` | `meaning`, `meaning_numbered` | `wa_term_inventory` |
| `vocabInfos[0].lsjDefs` (HTML stripped, Greek only) | `lsj_entry` | `lsj_entry`, `raw_lsj` | `wa_term_inventory`, `wa_lsj_parsed` |
| `vocabInfos[0].shortDefMounce` (Greek only) | `short_def_mounce` | `short_def_mounce` | `wa_term_inventory` |
| `vocabInfos[0].relatedNos[i].strongNumber` | `related_words[i]["strong"]` | `strongs_number` | `wa_term_related_words` |
| `vocabInfos[0].relatedNos[i].gloss` | `related_words[i]["gloss"]` | `gloss` | `wa_term_related_words` |
| `vocabInfos[0].relatedNos[i].stepTransliteration` | `related_words[i]["translit"]` | `transliteration` | `wa_term_related_words` |
| _derived from mediumDef text_ | `causative_form_present` | `causative_form_present` | `wa_term_inventory` |

### From `StepClient.get_verse_records_with_html(strong)`

| STEP JSON Field | `StepClient` dict key | Written to DB field | Table |
|---|---|---|---|
| `results[i]["key"]` | `ref` | `reference` | `wa_verse_records` |
| `results[i]["preview"]` (HTML stripped) | `esv_text` | `verse_text` | `wa_verse_records` |
| `results[i]["osisId"]` parsed → book | `book_code` | → `book_id` via `get_book_id()` | `wa_verse_records` |
| `results[i]["osisId"]` parsed → chapter | `chapter` | `chapter` | `wa_verse_records` |
| `results[i]["osisId"]` parsed → verse | `verse_num` | `verse_num` | `wa_verse_records` |
| _derived: `book_code in _NT_BOOKS`_ | `testament` | `testament` | `wa_verse_records` |
| `results[i]["preview"]` span text extraction | `target_word` | `target_word` | `wa_verse_records` |
| `results[i]["preview"]` span filter result | `span_strong_match` | `span_strong_match` | `wa_verse_records` |

### From `StepClient.get_strongs_for_word(english_word)` (BULK_GAP_FILL S1 only)

| Derived from | Written to DB field | Table |
|---|---|---|
| Span analysis of ESV text search results — tallied Strong's numbers per verse | `strongs_list` (JSON array `[{"strong": "H7965", "count": 148}]`) | `word_registry` |

---

## Part 8 — Fields NOT Written by the Engine

These fields exist in the schema but are explicitly excluded from engine writes. They are either judgment-deferred (requiring researcher evaluation), Phase 2 reserved, or legacy read-only fields.

| Table | Field | Reason |
|---|---|---|
| `wa_term_inventory` | `god_as_subject` | Judgment-deferred — requires theological assessment |
| `wa_term_inventory` | `somatic_link` | Judgment-deferred — requires semantic evaluation |
| `wa_verse_records` | `context_before` | Phase 2 reserved — surrounding context by researcher judgment |
| `wa_verse_records` | `context_after` | Phase 2 reserved — surrounding context by researcher judgment |
| `wa_verse_records` | `note` | Phase 2 reserved — researcher verse-level annotation |
| `wa_verse_records` | `claude_output` | Phase 2 reserved — AI analysis output |
| `wa_file_index` | `part_number` | Legacy multi-part field — NULL for all v9 writes |
| `wa_file_index` | `total_parts` | Legacy multi-part field — NULL for all v9 writes |
| `wa_file_index` | `root_families_in_prior_parts` | Legacy multi-part field — read-only in v9 |
| `wa_term_inventory` | `occurrence_count_qualifier` | Filled only in NEW_WORD N18 interactive field-fill (null in non-interactive runs) |
| `wa_term_inventory` | `also_spelled` | Filled only in NEW_WORD N18 interactive field-fill for Hebrew terms only |
| `word_run_state` | `researcher_approved`, `approved_by`, `approved_at` | Researcher sign-off fields — not set by engine |
| `schema_version` | `engine_min_version` | Not written by current implementation |
| `wa_meaning_sense` | `domain_tag` | Not yet implemented — always NULL |
| `wa_meaning_parsed` | `has_domain_tags` | Not yet implemented — always `0` |
| All `mti_term_flags.*` | All judgment flag fields | Phase 2 judgment flags — deferred to researcher |
| All `wa_term_phase2_flags.*` | All 25 flag types | Phase 2 judgment flags — deferred to researcher |

---

## Part 9 — Processing Mode Quick Reference

### NEW_WORD Mode (`engine/new_word.py` → `run_new_word()`)

| Step | Table Written | Key Fields | Subroutine |
|---|---|---|---|
| N6 | `word_registry` | `last_automation_run = "IN_PROGRESS"` | `run_new_word()` inline |
| N7 | `term_fetch_log` | vocab fetch result (one row per term) | `run_log.log_fetch()` |
| N8 | `term_fetch_log` | verse fetch result + span filter counts | `run_log.log_fetch()` |
| N9 | `wa_file_index` | all fields except `testament_coverage` | `run_new_word()` inline (transaction) |
| N10 | `mti_terms` | all fields | `run_new_word()` inline (transaction) |
| N11 | `wa_term_inventory`, `wa_term_related_words` | all API-sourced fields | `run_new_word()` inline (transaction) |
| N12 | `wa_verse_records` | all fields; `context_before`/`context_after` = NULL | `run_new_word()` inline (transaction) |
| N13 | `mti_term_cross_refs` | all fields (XREF terms only) | `run_new_word()` inline (transaction) |
| N14 | `wa_file_index`, `wa_term_inventory` | `testament_coverage`, `testament` | `run_new_word()` inline |
| N15 | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | all parsed meaning fields | `meaning_parser.run_parser_for_file()` → `run_parser()` |
| N16 | `wa_data_quality_flags` | quality/coverage flags | `flag_engine.run_flag_engine()` → `_write_quality_flag()` |
| N17 | `word_run_state` | audit snapshot | `audit.run_audit()` · `run_log.write_word_run_state()` |
| N18 | `wa_term_inventory` | `also_spelled`, `occurrence_count_qualifier` (interactive only) | `_run_field_fill()` |
| N19 | `word_registry` | `phase1_status`, `phase1_term_count`, `phase1_verse_count`, `last_automation_run`, `automation_run_id`, `phase1_input_file` | `run_new_word()` inline |
| N19 | `engine_run_log` | `completed_at`, `outcome`, all count fields | `run_log.close_run()` |

### GAP_FILL Mode — Single Word (`engine/gap_fill.py` → `run_gap_fill()`)

| Step | Table Written | Key Fields | Subroutine |
|---|---|---|---|
| S1 | `word_registry` | `last_automation_run = "IN_PROGRESS"` | `run_gap_fill()` inline |
| S3 | `wa_verse_records` | all fields; fills gaps for terms with zero verses | `run_gap_fill()` S3 inline |
| S3 | `term_fetch_log` | verse fetch + span filter results | `run_log.log_fetch()` |
| S4 | `wa_term_inventory` | `meaning`, `step_search_gloss`, `word_analysis_gloss`, `lsj_entry` (COALESCE updates) | `run_gap_fill()` S4 inline |
| S4 | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | re-parse after meaning fill | `meaning_parser.run_parser_for_file()` |
| S5 | `wa_data_quality_flags` | refreshed quality flags | `flag_engine.run_flag_engine()` |
| S6 | `word_run_state` | audit snapshot | `audit.run_audit()` · `run_log.write_word_run_state()` |
| S3–S6 | `engine_stream_checkpoint` | stream progress | `run_log.upsert_checkpoint()` |
| S7 | `word_registry` | `phase1_status`, `phase1_term_count`, `phase1_verse_count`, `last_automation_run`, `automation_run_id` | `run_gap_fill()` S7 inline |
| S8 | `engine_run_log` | `completed_at`, `outcome`, all counts | `run_log.close_run()` |

### BULK_GAP_FILL Mode (`engine/gap_fill.py` → `run_bulk_gap_fill()`)

| Step | Table Written | Key Fields | Subroutine |
|---|---|---|---|
| S1 | `word_registry` | `strongs_list` (JSON array) | `run_bulk_gap_fill()` S1 inline |
| S1 | `engine_stream_checkpoint` | S1 progress | `run_log.upsert_checkpoint()` |
| S2 | `wa_file_index` | all fields except `testament_coverage` | `run_bulk_gap_fill()` S2 Phase A |
| S2 | `word_registry` | `phase1_status = 'In Progress'`, `automation_run_id`, `last_automation_run` | `run_bulk_gap_fill()` S2 Phase A |
| S2 | `mti_terms` | all fields (NEW terms); idempotent | `run_bulk_gap_fill()` S2 Phase C |
| S2 | `mti_term_cross_refs` | XREF registrations | `run_bulk_gap_fill()` S2 Phase A |
| S2 | `wa_term_inventory`, `wa_term_related_words` | all API-sourced fields | `run_bulk_gap_fill()` S2 Phase C |
| S2 | `term_fetch_log` | vocab fetch results | `run_log.log_fetch()` |
| S2 | `engine_stream_checkpoint` | S2 progress | `run_log.upsert_checkpoint()` |
| S3 | `wa_verse_records` | all fields per verse | `run_bulk_gap_fill()` S3 inline |
| S3 | `term_fetch_log` | verse fetch + span filter | `run_log.log_fetch()` |
| S3 | `engine_stream_checkpoint` | S3 progress | `run_log.upsert_checkpoint()` |
| S4 | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | all parsed meaning fields | `meaning_parser.run_parser_for_file()` |
| S4 | `wa_data_quality_flags` | quality flags | `flag_engine.run_flag_engine()` |
| S4 | `word_run_state` | audit snapshot | `audit.run_audit()` · `run_log.write_word_run_state()` |
| S4 | `engine_stream_checkpoint` | S4 progress | `run_log.upsert_checkpoint()` |

### AUDIT_WORD Mode (`engine/audit_word.py` → `run_audit_word()`)

| Step | Table Written | Key Fields | Subroutine |
|---|---|---|---|
| A3a | `wa_verse_records` | INSERT missing verses; UPDATE `span_strong_match`/`target_word`/`verse_text`; set `span_strong_match=-1` for orphans | `run_audit_word()` A3a inline |
| A4 | `wa_term_inventory` | COALESCE updates for gloss, meaning, lsj_entry, short_def_mounce, occurrence_count | `run_audit_word()` A4 inline |
| A5 | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | full re-parse (idempotent delete+insert) | `meaning_parser.run_parser_for_file()` |
| A6 | `wa_data_quality_flags` | refreshed quality flags | `flag_engine.run_flag_engine()` |
| A7 | `word_run_state` | audit snapshot | `audit.run_audit()` · `run_log.write_word_run_state()` |
| A8 | `wa_data_quality_flags` | `SPAN_BACK_POPULATED` flag (if A3a inserted/updated rows) | `run_audit_word()` A8 inline |
| A9 | `wa_file_index` | `testament_coverage` refreshed | `run_audit_word()` A9 inline |
| A10 | `word_registry` | `phase1_term_count`, `phase1_verse_count`, `last_automation_run`, `automation_run_id` | `run_audit_word()` A10 inline |
| A10 | `engine_run_log` | `completed_at`, `outcome`, all counts | `run_log.close_run()` |

---

*Document generated: 2026-03-19. Based on engine v1.0.0, schema v3.1.0, architecture specification v4 Final (2026-03-18).*
