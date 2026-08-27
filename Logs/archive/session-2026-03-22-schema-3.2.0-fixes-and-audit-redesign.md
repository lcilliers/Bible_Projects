# Session Log — 22 March 2026
**Branch:** main  
**Schema version:** 3.2.0  
**Focus:** Schema 3.2.0 engine script fixes + audit_word redesign (STEP-master) + anger audit run

---

## 1. Engine Script Audit (post-schema-3.2.0 fixes)

A full audit of engine scripts against schema 3.2.0 was performed. Seven issues found and documented in `docs/post_fix_script_review.md`.

---

## 2. Fixes Applied

### Fix 1 — `analytics/db_client.py` (CRITICAL)
- **Problem:** Was issuing `PRAGMA journal_mode = WAL` on every DB connection, re-enabling WAL mode and risking data corruption on Google Drive.
- **Fix:** Replaced with a `RuntimeError` assertion that verifies `journal_mode = delete` before allowing any connection to proceed.

### Fix 2 — `engine/gap_fill.py` — zero-padding in word_run_state queries
- **Problem:** S7 fallback queried `word_run_state` using `.zfill(3)`-padded values after schema Fix 2 had removed zero-padding from that column.
- **Fix:** Removed `.zfill(3)` from both query parameters (lines ~369 and ~373).

### Fixes 3–4 — `mti_terms` INSERT in `engine/new_word.py` and `engine/gap_fill.py`
- **Problem:** INSERT statements omitted `owning_registry_fk` and `word_data_ref_fk` columns added in schema 3.2.0.
- **Fix:** Added both columns with values `registry_id` / `file_id` (new_word.py) and `registry_no` / `file_id` (gap_fill.py).

### Fixes 5–6 — `mti_term_cross_refs` INSERT in `engine/new_word.py` and `engine/gap_fill.py`
- **Problem:** INSERT statements omitted `registry_fk` column added in schema 3.2.0.
- **Fix:** Added `registry_fk` with values `registry_id` / `registry_no` respectively.

### Fix 7 — `engine/constants.py`
- **Change:** `EXPECTED_SCHEMA_VERSION` bumped from `"3.1.0"` to `"3.2.0"`.

---

## 3. Documentation Update

### `docs/db_relationship_report.md` — updated to schema 3.2.0
- Section 4.1 FK map expanded to 28 entries (9 new FKs from Fixes 3–7, 9)
- Section 4.2 parent table ownership updated
- Section 4.3 resolved entries removed with note
- Section 5 all issues marked resolved
- Section 6 orphan rates corrected to 0% for mti tables
- Section 7 mti_terms and mti_term_cross_refs entries updated with new formal FKs

---

## 4. audit_word.py — Full Redesign (STEP-master, two-phase)

### Motivation
Original audit_word.py used `COALESCE` guards that prevented STEP data from overwriting existing DB values, and did not delete verses no longer returned by STEP. This meant STEP was not truly the master source.

### New design principles
- **STEP is master** for all STEP-owned fields — no COALESCE guards
- **Two-phase:** Phase 1 = diff report only (dry-run); Phase 2 = apply (normal run)
- **Verse deletion:** rows not returned by STEP after span filter are DELETEd (not marked -1)
- **Researcher fields never overwritten:** status_note, also_spelled, occurrence_count_qualifier, causative_form_present, language, term_id, parsed_meaning_id

### STEP-owned `wa_term_inventory` fields (overwritten by audit)
transliteration, step_search_gloss, word_analysis_gloss, occurrence_count, meaning, meaning_numbered, lsj_entry, short_def_mounce

### Step sequence
| Step | Action |
|------|--------|
| A1 | Registry + file_index confirmation |
| A2 | Schema version check |
| A3 | STEP fetch: vocab + verses for every term (span-filtered) |
| A3r | Build diff report → `outputs/audit_diff_<word>_<registry>_<ts>.md`; STOP if dry-run |
| A4 | Apply STEP data: UPDATE ti, DELETE obsolete verses, INSERT new, UPDATE existing |
| A5 | Meaning parser refresh |
| A6 | Flag engine refresh (derivable flags only; researcher flags untouched) |
| A7 | Audit WR-01–WR-20 |
| A8 | Update testament_coverage |
| A9 | Update word_registry |

### Outcomes
- `--dry-run`: writes diff report, stops, returns `"DRY_RUN"`
- Normal run: writes diff report + applies all changes, returns `"COMPLETE"` or `"REVIEW"`

### Side fix — `engine/engine.py`
- Removed import of `register_book_override` (no longer in audit_word.py)
- `--add-book-code` CLI flag now returns an informative error message directing user to `book_code_variants` table

---

## 5. Anger Registry 4 — Audit Run

### Dry-run (review)
```
python -m engine.engine --mode=audit_word --registry=4 --dry-run
```
Diff report: `outputs/audit_diff_anger_4_20260322_204336.md`  
Result: 89 ti field changes, 762 INSERT, 133 UPDATE, 9 DELETE — approved by researcher.

### Apply run
```
python -m engine.engine --mode=audit_word --registry=4
```
Results:
- A4: 762 inserted, 133 updated, 9 deleted → 895 total verse records
- A5: 32 meanings re-parsed
- A6: 62 quality flags
- A7: 15 PASS | 5 REVIEW | 0 STOP → overall result: **REVIEW**

### A7 REVIEW items (anger)
| Check | Detail |
|-------|--------|
| WR-04 | 3 rows with null strongs_number (sub-entries e.g. G3949_related) |
| WR-08 | Low verse/occurrence ratio on G3709, G3710, G3949_related, G3949, G2372, G2373, G3947 — span filter working correctly |
| WR-13 | G_mēnis, G_enkotēma, G_cholos: no STEP occurrence_count |
| WR-18 | G_mēnis, G_enkotēma, G_cholos: no parsed meaning |
| WR-19 | 16 terms have parse warnings without NOTE flag |

---

## 6. Next Session

- Run AUDIT_WORD for all remaining words listed in `docs/orphan_flags_audit.csv` (anger/registry 4 done)
- Workflow: `--dry-run` first → researcher reviews diff report → apply
