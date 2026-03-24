# Engine DML Audit — 22 March 2026

Scope: `engine/new_word.py`, `engine/audit_word.py`, `engine/gap_fill.py`, `engine/flag_engine.py`, `engine/db.py`  
Target tables: `mti_terms`, `mti_term_cross_refs`, `wa_file_index`, `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family`, `wa_verse_records`, `wa_data_quality_flags`

---

## 1 · engine/db.py — Connection & PRAGMA audit

| Item | Finding |
|---|---|
| `get_connection()` | Delegates to `analytics.db_client.get_connection()` (line 14) |
| `PRAGMA foreign_keys` | **SET ON** — `db_client.py` line 97: `conn.execute("PRAGMA foreign_keys = ON")` |
| `PRAGMA journal_mode` | WAL — `db_client.py` line 98: `conn.execute("PRAGMA journal_mode = WAL")` |
| Extra engine setting | `engine/db.py` line 17: `conn.execute("PRAGMA busy_timeout = 5000")` |

**Conclusion:** `PRAGMA foreign_keys = ON` is active on every connection. No raw `sqlite3.connect()` call bypasses it.

---

## 2 · engine/new_word.py — All DML on target tables

### 2a · DELETEs (N2: `--force` purge path, lines 155–190)

These execute only when `--force` is passed and existing `wa_file_index` rows are found for the registry.

| Line | Table | Statement |
|---|---|---|
| 167 | `wa_data_quality_flags` | `DELETE FROM wa_data_quality_flags WHERE file_id = ?` |
| 183 | `wa_verse_records` | `DELETE FROM wa_verse_records WHERE file_id = ?` |
| 184 | `wa_term_inventory` | `DELETE FROM wa_term_inventory WHERE file_id = ?` |
| 185 | `mti_terms` | `DELETE FROM mti_terms WHERE word_data_reference = ?` — param is `str(old_id)` (file_id cast to TEXT) |
| 186 | `wa_file_index` | `DELETE FROM wa_file_index WHERE id = ?` |
| 188–190 | `mti_term_cross_refs` | `DELETE FROM mti_term_cross_refs WHERE registry = ? AND word = ?` — params: `str(registry_id)`, `word` |

Note: `wa_term_root_family` — **not touched** anywhere in this file. `wa_term_related_words` — deleted indirectly via `wa_term_inventory` FK cascade (if FK cascade is defined on that table) or not at all: there is no explicit `DELETE FROM wa_term_related_words` in the force-purge loop. The loop deletes `wa_term_inventory` at line 184 but does not explicitly delete `wa_term_related_words` rows first. If FK `ON DELETE CASCADE` is not configured on that FK, orphan rows will remain.

### 2b · INSERTs (N9–N13: transaction block)

All use **explicit named-column lists** — no positional/SELECT* patterns.

| Lines | Table | Column list |
|---|---|---|
| 369–379 | `wa_file_index` | `(id, filename, registry_id, word_registry_fk, word, part_number, total_parts, is_split, specification, phase, produced_date, translation_used, source_list, testament_coverage)` |
| 397–411 | `mti_terms` | `(id, strongs_number, transliteration, gloss, language, owning_registry, owning_word, owning_part, word_data_reference, status, extraction_date, strongs_reconciled)` |
| 427–445 | `wa_term_inventory` | `(id, file_id, language, term_id, strongs_number, transliteration, step_search_gloss, word_analysis_gloss, occurrence_count, meaning, meaning_numbered, lsj_entry, short_def_mounce, testament, causative_form_present, status_note)` — `testament` bound as NULL literal in the column list position |
| 454–457 | `wa_term_related_words` | `(term_inv_id, gloss, transliteration, strongs_number)` |
| 474–487 | `wa_verse_records` | `(id, file_id, term_inv_id, term_id, transliteration, book_id, reference, chapter, verse_num, testament, translation, verse_text, target_word, span_strong_match, context_before, context_after)` — `translation` always `'ESV'`; `context_before`, `context_after` always `NULL` |
| 512–514 | `mti_term_cross_refs` | `(id, mti_term_id, registry, word)` |

### 2c · UPDATEs

| Line | Table | SET clause |
|---|---|---|
| 572 | `wa_file_index` | `SET testament_coverage = ? WHERE id = ?` |
| 591 | `wa_term_inventory` | `SET testament = ? WHERE id = ?` |
| 748 | `wa_term_inventory` | `SET also_spelled = ? WHERE id = ?` (field-fill, N18) |
| 769 | `wa_term_inventory` | `SET occurrence_count_qualifier = ? WHERE id = ?` (field-fill, N18) |

### 2d · registry_id / owning_registry / registry column comparisons

| Lines | Table | Column | Usage | Padding |
|---|---|---|---|---|
| 152–153 | `wa_file_index` | `registry_id` | `WHERE registry_id = ?` param `str(registry_id)` | **Unpadded** (e.g. `"7"`) |
| 188–190 | `mti_term_cross_refs` | `registry` | `WHERE registry = ? AND word = ?` param `str(registry_id)` | **Unpadded** |
| 378 | `wa_file_index` | `registry_id` | INSERT value `str(registry_id)` | **Unpadded** |
| 407 | `mti_terms` | `owning_registry` | INSERT value `str(registry_id)` | **Unpadded** |
| 506–507 | `mti_term_cross_refs` | `registry` | `WHERE mti_term_id = ? AND registry = ? AND word = ? AND part IS NULL` param `str(registry_id)` | **Unpadded** |
| 514 | `mti_term_cross_refs` | `registry` | INSERT value `str(registry_id)` | **Unpadded** |
| 79, 82 | `mti_terms` | `owning_registry` | Read-only: `SELECT owning_registry ... WHERE strongs_number = ?`, then Python comparison `str(owner["owning_registry"]) != str(registry_id)` | No WHERE on this column |

---

## 3 · engine/audit_word.py — All DML on target tables

### 3a · INSERTs (A3a: verse sync — INSERT missing rows)

All use **explicit named-column lists**.

| Lines | Table | Column list |
|---|---|---|
| 197–212 | `wa_verse_records` | `(id, file_id, term_inv_id, term_id, transliteration, book_id, reference, chapter, verse_num, testament, translation, verse_text, target_word, span_strong_match, context_before, context_after)` — `translation` always `'ESV'`; `context_before`, `context_after` always `NULL` |
| 408–412 | `wa_data_quality_flags` | `INSERT OR IGNORE INTO wa_data_quality_flags (file_id, term_id, flag_id, description) VALUES (?, NULL, ?, ?)` (A8: SPAN_BACK_POPULATED flag) |

### 3b · UPDATEs

| Lines | Table | SET clause | Notes |
|---|---|---|---|
| 238 | `wa_verse_records` | `SET {', '.join(updates)} WHERE id = ?` — dynamic but always named columns: `span_strong_match` always written; `target_word`, `verse_text`, `context_before`, `context_after` conditionally appended | A3a UPDATE existing rows |
| 249 | `wa_verse_records` | `SET span_strong_match = -1 WHERE id = ?` | A3a orphan marking |
| 309–322 | `wa_term_inventory` | `SET step_search_gloss = COALESCE(NULLIF(...,''),?), word_analysis_gloss = COALESCE(NULLIF(...,''),?), meaning = COALESCE(NULLIF(...,''),?), meaning_numbered = COALESCE(NULLIF(...,''),?), occurrence_count = COALESCE(occurrence_count,?), lsj_entry = COALESCE(NULLIF(...,''),?), short_def_mounce = COALESCE(NULLIF(...,''),?) WHERE id = ?` | A4: non-destructive refresh (COALESCE guards existing values) |
| 436 | `wa_file_index` | `SET testament_coverage = ? WHERE id = ?` | A9 |

### 3c · registry_id comparisons

| Lines | Table | Column | Usage | Padding |
|---|---|---|---|---|
| 109–110 | `wa_file_index` | `registry_id` | `WHERE registry_id = ?` param `str(registry_id)` | **Unpadded** |

---

## 4 · engine/gap_fill.py — All DML on target tables

### 4a · run_gap_fill (per-word mode)

#### INSERTs (S3: verse gap-fill)

All use **explicit named-column lists**.

| Lines | Table | Column list |
|---|---|---|
| 233–248 | `wa_verse_records` | `(id, file_id, term_inv_id, term_id, transliteration, book_id, reference, chapter, verse_num, testament, translation, verse_text, target_word, span_strong_match, context_before, context_after)` — `translation` always `'ESV'`; `context_before`, `context_after` always `NULL` |

#### UPDATEs (S4: meaning gap-fill)

| Lines | Table | SET clause |
|---|---|---|
| 289–298 | `wa_term_inventory` | `SET meaning = ?, meaning_numbered = ?, step_search_gloss = COALESCE(step_search_gloss, ?), word_analysis_gloss = COALESCE(word_analysis_gloss, ?) WHERE id = ?` |
| 301 | `wa_term_inventory` | `SET lsj_entry = COALESCE(lsj_entry, ?) WHERE id = ?` |

#### registry_id comparisons (run_gap_fill)

| Lines | Table | Column | Usage | Padding |
|---|---|---|---|---|
| 140–141 | `wa_file_index` | `registry_id` | `WHERE registry_id = ?` param `str(registry_id)` | **Unpadded** |
| 367–369 | `word_run_state` | `registry_id` | `WHERE registry_id = ?` param `str(registry_id).zfill(3)` | ⚠️ **ZERO-PADDED** (e.g. `"007"`) |
| 372–373 | `word_run_state` | `registry_id` | `WHERE registry_id = ? LIMIT 1` param `str(registry_id).zfill(3)` | ⚠️ **ZERO-PADDED** (e.g. `"007"`) |

> **Risk:** `word_run_state` is not in the primary 8 target tables, but the `zfill(3)` padding at lines 369 and 373 is the only surviving use of zero-padded registry values anywhere in these four scripts. If the `word_run_state.registry_id` column has been normalised to unpadded values, the S7 fallback `audit_res` lookup will fail silently (returns `"UNKNOWN"`), affecting the `final_status` written to `word_registry`.

### 4b · run_bulk_gap_fill (bulk mode)

#### INSERTs (S2 Phase A — wa_file_index + mti_term_cross_refs)

| Lines | Table | Column list | Note |
|---|---|---|---|
| 594–608 | `wa_file_index` | `(id, filename, registry_id, word_registry_fk, word, part_number, total_parts, is_split, specification, phase, produced_date, translation_used, source_list, testament_coverage)` | `registry_id` stored as `str(registry_no)` — **unpadded** |
| 617–621 | `mti_term_cross_refs` | `INSERT OR IGNORE INTO mti_term_cross_refs (id, mti_term_id, registry, word)` | `registry` stored as `str(registry_no)` — **unpadded** |

#### INSERTs (S2 Phase C — mti_terms + wa_term_inventory + wa_term_related_words)

| Lines | Table | Column list |
|---|---|---|
| 688–702 | `mti_terms` | `(id, strongs_number, transliteration, gloss, language, owning_registry, owning_word, owning_part, word_data_reference, status, extraction_date, strongs_reconciled)` — `owning_registry` stored as `str(registry_no)` — **unpadded** |
| 710–727 | `wa_term_inventory` | `(id, file_id, language, term_id, strongs_number, transliteration, step_search_gloss, word_analysis_gloss, occurrence_count, meaning, meaning_numbered, lsj_entry, short_def_mounce, testament, causative_form_present, status_note)` — `testament` bound as NULL literal; `status_note` bound as NULL literal |
| 736–739 | `wa_term_related_words` | `(term_inv_id, gloss, transliteration, strongs_number)` |

#### INSERTs (S3 — wa_verse_records)

| Lines | Table | Column list |
|---|---|---|
| 832–846 | `wa_verse_records` | `(id, file_id, term_inv_id, term_id, transliteration, book_id, reference, chapter, verse_num, testament, translation, verse_text, target_word, span_strong_match, context_before, context_after)` — `translation` always `'ESV'`; `context_before`, `context_after` always `NULL` |

#### registry_id comparisons (run_bulk_gap_fill)

| Lines | Table | Column | Usage | Padding |
|---|---|---|---|---|
| 560–561 | `wa_file_index` | `registry_id` | `WHERE registry_id = ?` param `str(registry_no)` | **Unpadded** |
| 781 | `wa_file_index` | `registry_id` | `JOIN word_registry wr ON wr.no = CAST(fi.registry_id AS INTEGER)` | CAST to integer — safe with either format |
| 882 | `wa_file_index` | `registry_id` | `JOIN word_registry wr ON wr.no = CAST(fi.registry_id AS INTEGER)` | CAST to integer — safe with either format |

---

## 5 · engine/flag_engine.py — All DML on target tables

### 5a · DELETE (idempotency purge — executes on every call)

| Lines | Table | Statement |
|---|---|---|
| 87–94 | `wa_data_quality_flags` | `DELETE FROM wa_data_quality_flags WHERE file_id = ? AND flag_id IN (SELECT id FROM wa_quality_flag_types WHERE flag_code IN (?, ?, ?, ?, ?, ?))` — params: `(file_id, "HIGH_FREQUENCY_ANCHOR", "THIN_DATA", "SMALL_VERSE_SAMPLE", "NO_WORD_ANALYSIS", "NO_VERSES", "SPAN_RESOLUTION_CONFLICT")` |

### 5b · INSERTs (via `_write_quality_flag`, called multiple times)

| Lines | Table | Column list |
|---|---|---|
| 51–54 | `wa_data_quality_flags` | `INSERT INTO wa_data_quality_flags (file_id, term_id, flag_id, description) VALUES (?, ?, ?, ?)` — **named columns** ✓ |

No references to `registry_id`, `owning_registry`, or `registry` anywhere in `flag_engine.py`.

---

## 6 · wa_term_root_family — not touched

No INSERT, UPDATE, or DELETE referencing `wa_term_root_family` appears in any of the four scripts.

---

## 7 · Named-column vs positional INSERT summary

| File | Table | Named columns? |
|---|---|---|
| new_word.py | `wa_file_index` | ✅ Yes |
| new_word.py | `mti_terms` | ✅ Yes |
| new_word.py | `wa_term_inventory` | ✅ Yes |
| new_word.py | `wa_term_related_words` | ✅ Yes |
| new_word.py | `wa_verse_records` | ✅ Yes |
| new_word.py | `mti_term_cross_refs` | ✅ Yes |
| audit_word.py | `wa_verse_records` | ✅ Yes |
| audit_word.py | `wa_data_quality_flags` | ✅ Yes |
| gap_fill.py (run_gap_fill) | `wa_verse_records` | ✅ Yes |
| gap_fill.py (run_bulk_gap_fill) | `wa_file_index` | ✅ Yes |
| gap_fill.py (run_bulk_gap_fill) | `mti_term_cross_refs` | ✅ Yes |
| gap_fill.py (run_bulk_gap_fill) | `mti_terms` | ✅ Yes |
| gap_fill.py (run_bulk_gap_fill) | `wa_term_inventory` | ✅ Yes |
| gap_fill.py (run_bulk_gap_fill) | `wa_term_related_words` | ✅ Yes |
| gap_fill.py (run_bulk_gap_fill) | `wa_verse_records` | ✅ Yes |
| flag_engine.py | `wa_data_quality_flags` | ✅ Yes |

**No positional or SELECT* INSERT patterns found anywhere.**

---

## 8 · Zero-padding risk summary

All registry-related values written to and read from the 8 target tables use **unpadded** `str(integer)` (e.g. `"7"`, not `"007"`). The normalisation is consistent across all new write paths.

**One surviving zero-pad use — outside the 8 target tables:**

| File | Lines | Table | Column | Issue |
|---|---|---|---|---|
| gap_fill.py | 367–369 | `word_run_state` | `registry_id` | `str(registry_id).zfill(3)` used in S7 fallback `audit_res` lookup |
| gap_fill.py | 372–373 | `word_run_state` | `registry_id` | `str(registry_id).zfill(3)` used in existence check |

If `word_run_state.registry_id` has been normalised to unpadded values, both queries will return nothing. The S7 fallback path then defaults `audit_res = "UNKNOWN"`, which causes `final_status = "In Progress"` even when the audit previously passed. This does not corrupt the 8 target tables, but it will write an incorrect `phase1_status` to `word_registry`.

---

## 9 · Notable structural observations (factual only)

1. **N2 force-purge omits `wa_term_related_words`** (new_word.py lines 155–186): The loop deletes `wa_term_inventory` (line 184) but has no explicit `DELETE FROM wa_term_related_words`. Orphan rows will remain unless the FK has `ON DELETE CASCADE` defined in the schema.

2. **`wa_verse_records` INSERT always sets `context_before = NULL, context_after = NULL`** across all three scripts (new_word.py L474, audit_word.py L197, gap_fill.py L233 and L832). The UPDATE path in audit_word.py (line 238) does conditionally write `context_before` and `context_after` if the STEP response provides them, but the initial INSERT never does.

3. **`testament_coverage` on `wa_file_index` is always `NULL` at INSERT time** — it is set in a subsequent UPDATE (new_word.py N14 line 572, audit_word.py A9 line 436).

4. **`wa_file_index.registry_id` is stored as TEXT** (`str(registry_id)`) everywhere. JOINs to `word_registry.no` (INTEGER) use `CAST(fi.registry_id AS INTEGER)` in bulk queries — consistent and safe.
