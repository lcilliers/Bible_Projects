# wa_verse_records — Orphan & Integrity Check

**Date:** 2026-03-19  
**Database:** `data/bible_research.db`  
**Schema version:** v3.1.0  
**Total rows in wa_verse_records:** 57,130

---

## Final State (post all fixes)

| Check | Result | Status |
|---|---|---|
| Orphan `file_id` (no parent in `wa_file_index`) | 0 | ✅ Clean |
| Orphan `term_inv_id` (no parent in `wa_term_inventory`, excl. NULLs) | 0 | ✅ Clean |
| Orphan `book_id` (no parent in `books`, excl. NULLs) | 0 | ✅ Clean |
| NULL `file_id` | 0 | ✅ Clean |
| NULL `book_id` | 0 | ✅ Fixed |
| NULL `chapter` | 0 | ✅ Clean |
| NULL `verse_num` | 0 | ✅ Clean |
| NULL `term_inv_id` | 0 | ✅ Fixed |
| NULL `term_id` | 0 | ✅ Fixed |
| NULL `reference` | 0 | ✅ Clean |
| NULL `testament` | 0 | ✅ Clean |
| NULL `verse_text` | 0 | ✅ Clean |
| NULL `span_strong_match` | 3,975 | ℹ️ No STEP HTML (irreducible) |
| NULL `target_word` | 4,393 | ℹ️ No match or no HTML |

*Verified by `scripts/_integrity_full_check.py` after all fixes applied.*

---

## Fixes Applied This Session

### Fix 1 — 161 rows with NULL `book_id` ✅ Resolved

**Root causes:**
1. `Phili` alias missing from `book_code_variants` (Philippians)
2. `resolve_verse_refs()` had not been run for `file_id = 51` (pre-M05 import)

**Source file:** `WA-186-gladness-data-20260317.json` (word: gladness, registry: 186)

**Fix applied by `scripts/_fix_book_resolve.py`:**
1. Inserted `Phili → books.id = 50` into `book_code_variants`
2. Ran `resolve_verse_refs(only_missing=True)` → all 161 rows resolved
3. Final NULL `book_id` count: **0**

---

### Fix 2 — 1 row with NULL `term_inv_id` ✅ Resolved

| Field | Value |
|---|---|
| `wa_verse_records.id` | 1636 |
| `file_id` | 10 |
| `term_id` | G3715 |
| `transliteration` | orexis |
| `reference` | Rom 1:27 |

**Root cause:** Import matched verse on `term_id = 'G3715'` but `wa_term_inventory` row had `term_id = 'G3713'` / `strongs_number = 'G3715'` — FK was not set because the import keyed on `term_id` not `strongs_number`.

**Fix applied by `scripts/_fix_term_inv_link.py`:**
- Set `term_inv_id = 173` directly on `wa_verse_records.id = 1636`
- Final NULL `term_inv_id` count: **0**

---

### Fix 3 — 728 rows with NULL `term_id` ✅ Resolved

**Root cause:** Denormalized `term_id` field was not populated during old (pre-M05) imports.

**Fix applied by `scripts/_fix_null_term_id.py`:**
- SQL UPDATE joining `wa_term_inventory` via `term_inv_id` to copy `strongs_number → term_id`
- 728 rows updated
- Final NULL `term_id` count: **0**

---

### Fix 4 — 12,877 rows with NULL `span_strong_match` — Partially Resolved

**Root cause:** Pre-M05 imports; span filter was not in place when these rows were inserted.

**Fix applied by `scripts/_backfill_span_match.py`:**
- Grouped NULL rows by `strongs_number` (613 unique terms)
- One STEP API call per term (`get_verse_records_with_html`)
- Matched DB rows by `reference` string to STEP records
- Applied span filter, updated `span_strong_match` + `target_word` per row
- Committed after each term (resume-safe)

**Results:**
- Rows updated: **8,902**
- `span_strong_match = 1` (confirmed match): **8,485**
- `span_strong_match = 0` (span not found in verse HTML): varies by term
- Remaining NULL after backfill: **3,975** — STEP returned no HTML for these verses (irreducible with current approach)
- 1 term skipped: `strongs_number = NULL` in `wa_term_inventory` (1 row left NULL)

---

## Original Findings (Initial Orphan Check)

The initial check (`scripts/_orphan_check.py`, `scripts/_orphan_check2.py`) found:

| Check | Original Result |
|---|---|
| True FK orphans (`file_id`, `term_inv_id`, `book_id`) | 0 |
| NULL `book_id` | 161 |
| NULL `term_inv_id` | 1 |

All true FK relationships were intact at import time. The NULL fields were patching gaps from pre-M05 import pipelines that lacked the `resolve_verse_refs()` and span-filter steps.

---

## Remaining Known Limitations

- **3,975 rows with `span_strong_match = NULL`:** STEP Bible API returns no parsed HTML for these verse/term combinations. These cannot be resolved without a different data source. The rows are valid and their `reference`, `verse_text`, and FK fields are fully populated.
- **1 row with `span_strong_match = NULL` (null strongs_number):** `wa_term_inventory` has one row where `strongs_number` is NULL — the backfill script skipped it. Row identity: the single verse record linked to that inventory entry remains unresolved.

---

*Initial check: `scripts/_orphan_check.py` and `scripts/_orphan_check2.py`*  
*Full integrity check: `scripts/_integrity_full_check.py`*  
*Fixes: `scripts/_fix_book_resolve.py`, `scripts/_fix_term_inv_link.py`, `scripts/_fix_null_term_id.py`, `scripts/_backfill_span_match.py`*
