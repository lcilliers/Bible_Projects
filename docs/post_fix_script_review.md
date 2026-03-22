# Post-Fix Script & Documentation Review
**Date:** 2026-03-22  
**Scope:** engine/audit_word.py, engine/new_word.py, engine/gap_fill.py, engine/flag_engine.py  
**Against:** Fixes 2–7, 9 (schema 3.2.0)

---

## Summary

Four issues require action before the next engine run. One is critical and will corrupt the
database if not addressed immediately.

| # | Severity | File | Issue |
|---|----------|------|-------|
| 1 | **CRITICAL** | `analytics/db_client.py` | Sets `PRAGMA journal_mode = WAL` on every connection — will flip DB back to WAL mode |
| 2 | **BUG** | `engine/gap_fill.py` | `.zfill(3)` on `word_run_state.registry_id` queries — returns nothing post-Fix 2, silently writes wrong status |
| 3 | **Data gap** | `engine/new_word.py` | `mti_terms` INSERT omits `owning_registry_fk`, `word_data_ref_fk` (new Fix 9 columns) |
| 4 | **Data gap** | `engine/gap_fill.py` | Same omission in `mti_terms` INSERT |
| 5 | **Data gap** | `engine/new_word.py` | `mti_term_cross_refs` INSERT omits `registry_fk` (new Fix 9 column) |
| 6 | **Data gap** | `engine/gap_fill.py` | Same omission in `mti_term_cross_refs` INSERT |
| 7 | **Docs** | `docs/db_relationship_report.md` | Written before Fix 9 — missing 3 new integer FK columns |

---

## Issue 1 — CRITICAL: WAL mode re-enabled on every connection

**File:** [analytics/db_client.py](../analytics/db_client.py#L95)  
**Line 95:** `conn.execute("PRAGMA journal_mode = WAL")  # better concurrent read performance`

Fix 7 switched the database to DELETE journal mode to prevent corruption on Google Drive.
`db_client.py` issues `PRAGMA journal_mode = WAL` on every connection open, which will
immediately flip the database back to WAL mode the next time any engine script runs.

**Required fix:** Remove or change that line.
- Option A: Remove the line entirely — DELETE mode is stored in the file header and persists.
- Option B: Replace with a safety assertion that verifies the mode is DELETE and raises if not.

Option B is recommended: it will catch any future accidental mode change.

```python
# analytics/db_client.py — replace line 95
mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
if mode != "delete":
    raise RuntimeError(
        f"Database journal_mode is '{mode}', expected 'delete'. "
        "Do not run engine scripts in WAL mode on Google Drive."
    )
```

---

## Issue 2 — BUG: gap_fill.py zero-padding in word_run_state query

**File:** [engine/gap_fill.py](../engine/gap_fill.py#L369)  
**Lines 369 and 373** (S7 — Registry update, fallback path):

```python
"SELECT audit_result FROM word_run_state WHERE registry_id = ? ORDER BY id DESC LIMIT 1",
(str(registry_id).zfill(3),),          # ← padded: "007"
```

```python
"SELECT id FROM word_run_state WHERE registry_id = ? LIMIT 1",
(str(registry_id).zfill(3),),          # ← padded: "007"
```

Fix 2 normalised `word_run_state.registry_id` to unpadded values (e.g. `"7"` not `"007"`).
These queries now silently return nothing. The S7 logic then falls back to `audit_res = "UNKNOWN"`
and writes `phase1_status = "In Progress"` to `word_registry`, masking the actual audit outcome.

**Required fix:** Remove `.zfill(3)` from both lines — use `str(registry_id)` only.

---

## Issue 3 & 4 — Data gap: mti_terms INSERTs omit Fix 9 columns

**Files:**  
- [engine/new_word.py](../engine/new_word.py#L397) (N10 block)  
- [engine/gap_fill.py](../engine/gap_fill.py#L688) (run_bulk_gap_fill)

Both INSERT into `mti_terms` with this column list:
```sql
(id, strongs_number, transliteration, gloss, language,
 owning_registry, owning_word, owning_part,
 word_data_reference, status, extraction_date, strongs_reconciled)
```

Fix 9 added `owning_registry_fk` (INTEGER, FK → word_registry) and `word_data_ref_fk`
(INTEGER, FK → wa_file_index). Neither is populated by these INSERTs — new rows will have
NULL in both columns.

The values to populate them from are available at INSERT time:
- `owning_registry_fk` ← the integer `registry_id` (word_registry.id)
- `word_data_ref_fk` ← the integer `file_id` (wa_file_index.id)

**Required fix (both scripts):** Add the two columns to the INSERT column list and supply
the integer values.

```sql
-- new column list
(id, strongs_number, transliteration, gloss, language,
 owning_registry, owning_word, owning_part,
 word_data_reference, owning_registry_fk, word_data_ref_fk,
 status, extraction_date, strongs_reconciled)
```

```python
-- new values tuple (add registry_id, file_id after word_data_reference)
(mt_id, resolved,
 vocab.get("transliteration", ""), vocab.get("gloss", ""), lang,
 str(registry_id), word,
 str(file_id),
 registry_id, file_id,   # ← owning_registry_fk, word_data_ref_fk
 'extracted', _today(), 1 if resolved != strongs else 0)
```

Note: `gap_fill.py` uses `registry_no` instead of `registry_id` for the TEXT column —
confirm the variable name when editing that file.

---

## Issue 5 & 6 — Data gap: mti_term_cross_refs INSERTs omit Fix 9 column

**Files:**  
- [engine/new_word.py](../engine/new_word.py#L512) (N13 block)  
- [engine/gap_fill.py](../engine/gap_fill.py#L617) (run_bulk_gap_fill)

Both INSERT:
```sql
INSERT INTO mti_term_cross_refs (id, mti_term_id, registry, word) VALUES (?, ?, ?, ?)
```

Fix 9 added `registry_fk` (INTEGER, FK → word_registry). Not populated — new rows will have NULL.

`registry` (TEXT) holds `str(registry_id)`, so `registry_fk` = `int(registry_id)`.

**Required fix (both scripts):** Add `registry_fk` to the INSERT:
```sql
INSERT INTO mti_term_cross_refs (id, mti_term_id, registry, word, registry_fk)
VALUES (?, ?, ?, ?, ?)
```
Add `int(registry_id)` (or `registry_no` in gap_fill.py) as the fifth parameter.

---

## Issue 7 — Documentation: db_relationship_report.md predates Fix 9

**File:** [docs/db_relationship_report.md](../docs/db_relationship_report.md)

Was produced before Fix 9 ran. Missing from that document:
- `mti_terms.owning_registry_fk` (INTEGER) — FK → word_registry(id)
- `mti_terms.word_data_ref_fk` (INTEGER) — FK → wa_file_index(id)
- `mti_term_cross_refs.registry_fk` (INTEGER) — FK → word_registry(id)

The report should be updated to reflect the 3.2.0 schema when next used as a reference.

---

## What was NOT affected

- `engine/audit_word.py` — all INSERTs/UPDATEs use named-column lists; touches only
  `wa_verse_records` and `wa_data_quality_flags` (no new columns in either table).
- `engine/flag_engine.py` — only touches `wa_data_quality_flags` (no new columns).
- `new_word.py` `--force` purge of `wa_term_related_words` — Fix 5/6 added `ON DELETE CASCADE`
  on both `wa_term_related_words` and `wa_term_root_family → wa_term_inventory`. The purge
  DELETE of `wa_term_inventory` (line 184) will now cascade automatically. No code change needed.

---

## Recommended action order

1. Fix Issue 1 (`db_client.py`) — do this **before any engine run**  
2. Fix Issue 2 (`gap_fill.py` zero-padding) — do before next gap-fill run  
3. Fix Issues 3–6 (new FK columns) — do before next new-word or gap-fill run  
4. Update `db_relationship_report.md` — low urgency, do at next documentation pass  
