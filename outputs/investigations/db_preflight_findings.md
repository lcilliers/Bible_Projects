# Database Remediation — Pre-Flight Findings

**Script run:** `scripts/_preflight_validate.py` (read-only, no writes)  
**Database:** `data/bible_research.db` — schema v3.1.0 (applied 2026-03-18)  
**Plan document:** `docs/db_remediation_plan.md`  
**Date assessed:** 2026-03-20

---

## Summary Table

| Fix | Description | Status | Action Required |
|-----|-------------|--------|-----------------|
| Fix 1 | FK Enforcement (PRAGMA) | ✅ ALREADY DONE | Skip — already in `db_client.py` |
| Fix 2 | Zero-padding normalisation | ⚠ DATA READY | 509 rows to update; no blockers |
| Fix 3 | Recreate `wa_file_index` with FK | ✅ READY | Columns verified; no triggers |
| Fix 4 | Recreate `wa_term_inventory` with FK | ✅ READY | Columns verified; 0 orphans |
| Fix 5 | Recreate `wa_term_related_words` with FK | ✅ READY | Columns verified; 0 orphans |
| Fix 6 | Recreate `wa_term_root_family` with FK | ✅ READY | Columns verified; 0 orphans |
| Fix 7 | Recreate `wa_verse_records` with FKs | ❌ NOT READY | **Trigger recreation DDL missing from plan — must be added first** |
| Fix 8a | Export DQF orphan audit CSV | ✅ READY | 53 orphans confirmed; script is read-only |
| Fix 8b | Recreate `wa_data_quality_flags` with FK | 🔒 BLOCKED | Requires researcher's completed Fix 8a CSV |
| Fix 9 | Recreate MTI tables with FKs | ✅ READY | All columns verified; all values castable |

**Schema version after completion:** 3.1.0 → **3.2.0** (must be updated in the final repair script)

---

## Findings by Fix

---

### Fix 1 — FK Enforcement (`PRAGMA foreign_keys = ON`)

**Result: ALREADY DONE — no script needed**

`analytics/db_client.py` already contains `PRAGMA foreign_keys = ON` inside `get_connection()`. All engine and analytics connections route through this function. The `engine/db.py` module chains to `db_client.get_connection()`, inheriting the setting without needing to repeat it.

The pre-flight script confirmed:
- `PRAGMA foreign_keys` = **1** on the test connection (going through `db_client.py`)
- `PRAGMA foreign_key_check` = **0 violations** — the live database has no existing FK violations

**The `_repair_01_*.py` script should be omitted or marked as already applied.**

Note: the original `db_relationship_report.md` reported FK enforcement as OFF. That report used a raw `sqlite3.connect()` call without going through `db_client.py`, which is why it showed `PRAGMA foreign_keys = 0`. That reading was accurate for a direct connection but not for production engine connections.

---

### Fix 2 — Zero-Padding Normalisation

**Result: READY (data confirmed, no blockers)**

Zero-padded registry IDs found across four tables:

| Table | Column | Zero-padded rows |
|-------|--------|-----------------|
| `wa_file_index` | `registry_id` | 27 rows |
| `mti_terms` | `owning_registry` | 371 rows |
| `mti_term_cross_refs` | `registry` | 28 rows |
| `word_run_state` | `registry_id` | 83 rows |
| **Total** | | **509 rows** |

Cross-check: `wa_file_index` rows where `registry_id != CAST(word_registry_fk AS TEXT)` = 27 — these are exactly the zero-padded rows. Post-fix, this count should be 0.

The WARNs for this fix are expected — they confirm the data that needs to change, not a problem with the plan.

---

### Fix 3 — Recreate `wa_file_index`

**Result: READY**

| Check | Result |
|-------|--------|
| Column list (20 cols) matches plan exactly | ✅ PASS |
| No triggers on this table | ✅ PASS — no trigger recreation needed |

Column inventory confirmed (ordered):
`id, filename, registry_id, word_registry_fk, word, part_number, total_parts, is_split, schema_version, phase, produced_date, source_file, translation_used, specification, revision_note, source_list, category, testament_coverage, root_families_in_prior_parts, last_changed`

---

### Fix 4 — Recreate `wa_term_inventory`

**Result: READY**

| Check | Result |
|-------|--------|
| Column list (22 cols) matches plan exactly | ✅ PASS |
| `file_id` orphans (FK to `wa_file_index`) | 0 ✅ |
| `file_id` NULLs | 0 ✅ — NOT NULL constraint in plan is safe |
| `parsed_meaning_id` retained in column list | ✅ PASS — engine writes this at step N15 |

Column inventory confirmed (ordered):
`id, file_id, language, term_id, strongs_number, transliteration, step_search_gloss, word_analysis_gloss, occurrence_count, occurrence_count_qualifier, meaning, meaning_numbered, also_spelled, lsj_entry, testament, god_as_subject, somatic_link, causative_form_present, status_note, last_changed, short_def_mounce, parsed_meaning_id`

---

### Fix 5 — Recreate `wa_term_related_words`

**Result: READY**

| Check | Result |
|-------|--------|
| Column list matches plan exactly | ✅ PASS |
| `term_inv_id` orphans (FK to `wa_term_inventory`) | 0 ✅ |
| `term_inv_id` NULLs | 0 |

---

### Fix 6 — Recreate `wa_term_root_family`

**Result: READY**

| Check | Result |
|-------|--------|
| Column list matches plan exactly | ✅ PASS |
| `term_inv_id` orphans (FK to `wa_term_inventory`) | 0 ✅ |

---

### Fix 7 — Recreate `wa_verse_records`

**Result: NOT READY — mandatory addition required before execution**

| Check | Result |
|-------|--------|
| Row count = 57,130 | ✅ PASS — matches plan expectation |
| `file_id` orphans (FK to `wa_file_index`) | 0 ✅ |
| `file_id` NULLs | 0 ✅ — NOT NULL constraint in plan is safe |
| `term_inv_id` orphans (FK to `wa_term_inventory`) | 0 ✅ |
| Column list (21 cols) matches plan exactly | ✅ PASS |
| **Trigger `wa_verse_records_updated_at` exists** | ⚠ **WARN — NOT in plan script** |

**Trigger gap — mandatory fix:**

The live table has a trigger that must be recreated after the table swap. The current Fix 7 script in `db_remediation_plan.md` recreates indexes but does **not** include `CREATE TRIGGER`.

Full trigger DDL (from `create_tables.sql` and confirmed via `sqlite_master`):

```sql
CREATE TRIGGER IF NOT EXISTS wa_verse_records_updated_at
AFTER UPDATE ON wa_verse_records
BEGIN
    UPDATE wa_verse_records
    SET updated_at = strftime('%Y-%m-%dT%H:%M:%S','now')
    WHERE id = NEW.id;
END;
```

This line must be added to `_repair_07_wa_verse_records.py` immediately after the index recreation block, before `COMMIT`.

**Without this, every UPDATE to `wa_verse_records` will silently fail to maintain `updated_at`.** The engine uses `updated_at` for change tracking. This is a mandatory addition, not optional.

---

### Fix 8a — DQF Orphan Audit Export

**Result: READY (read-only script)**

| Check | Result |
|-------|--------|
| `wa_data_quality_flags` total rows | 3,254 |
| Orphan flags (term_id not in `wa_term_inventory`) | **53** ✅ — matches plan exactly |

Orphan breakdown confirmed:

| Category | Count |
|----------|-------|
| `NOT_IN_DB` | 44 — terms from early words not carried to inventory |
| `NO_STRONG` | 6 — placeholder codes (`NO STRONG-043-…`, `NO STRONG-135-…`) |
| `RELATED_SUFFIX` | 3 — `G3949_related` variants |
| `WRONG_FILE` | 0 |

Fix 8a script exports the audit CSV with blank `researcher_decision` column for researcher to complete.

---

### Fix 8b — Recreate `wa_data_quality_flags`

**Result: BLOCKED on researcher input**

| Check | Result |
|-------|--------|
| All source columns present in live table | ✅ PASS |

Fix 8b cannot run until the researcher returns the completed `orphan_flags_audit.csv` from Fix 8a with decisions filled in. Valid decision values: `KEEP_AS_FILE_LEVEL`, `RESOLVE_TO_TERM`, `DELETE`, `KEEP_UNLINKED`.

Duplicate pair confirmation (2 pairs, MIN resolution):
- `file_id=29, term_id=G0150` → ids `[437, 438]` → MIN will use **437**
- `file_id=48, term_id=H7999A` → ids `[625, 627]` → MIN will use **625**

---

### Fix 9 — Recreate MTI Tables

**Result: READY**

| Check | Result |
|-------|--------|
| `mti_terms` source columns match plan (16 cols) | ✅ PASS |
| `mti_terms.word_data_reference` — all non-null values cast to INTEGER | ✅ PASS (0 non-castable rows) |
| `mti_terms.owning_registry` — all non-null values numeric | ✅ PASS |
| `mti_term_cross_refs` source columns match plan | ✅ PASS |
| `mti_term_cross_refs.registry` — all non-null values numeric | ✅ PASS |

New FK columns added to existing tables (no new table names):
- `mti_terms.owning_registry_fk` (INTEGER → `word_registry(id)`)
- `mti_terms.word_data_ref_fk` (INTEGER → `wa_file_index(id)`)
- `mti_term_cross_refs.registry_fk` (INTEGER → `word_registry(id)`)
- `wa_data_quality_flags.term_inv_id` (INTEGER → `wa_term_inventory(id)`)

**`_ALLOWED_TABLES` whitelist:** No new table names are introduced by any fix. The whitelist in `analytics/db_client.py` does not need updating.

---

## Execution Readiness

### What requires action before execution begins

**1. Fix 7 trigger — mandatory addition (see Fix 7 above)**

The `_repair_07_wa_verse_records.py` script must include `CREATE TRIGGER IF NOT EXISTS wa_verse_records_updated_at` after index recreation. Full DDL provided above.

**2. Fix 8b — blocked on researcher input**

Run Fix 8a, complete the CSV, then run Fix 8b. No execution sequence issue; Fix 8a can be run at any time as it is read-only.

### What is already done and requires no script

- **Fix 1** — `PRAGMA foreign_keys = ON` is already in `db_client.py`. No repair script needed.

### Fixes clear to proceed (pending trigger addition for Fix 7)

| Execution Order | Fix | Notes |
|-----------------|-----|-------|
| 1 | Fix 2 — zero-padding | Simple UPDATE, 4 tables |
| 2 | Fix 3 — `wa_file_index` | Must precede Fix 4 (FK target) |
| 3 | Fix 4 — `wa_term_inventory` | Must precede Fixes 5, 6, 7 (FK target) |
| 4 | Fix 5 — `wa_term_related_words` | Depends on Fix 4 |
| 5 | Fix 6 — `wa_term_root_family` | Depends on Fix 4 |
| 6 | Fix 7 — `wa_verse_records` | **After trigger DDL is added to script** |
| 7 | Fix 8a — DQF audit export | Read-only; can run at any point |
| 8 | Fix 8b — `wa_data_quality_flags` | After researcher returns CSV |
| 9 | Fix 9 — MTI tables | No FK dependencies on earlier fixes |
| — | Schema bump to 3.2.0 | Must be last step |

---

## Items to Update in `db_remediation_plan.md`

1. **Fix 1** — mark as already implemented; no script to run. Note `db_client.py` already contains the pragma.
2. **Fix 7** — add `CREATE TRIGGER` DDL to the script logic block (full DDL above).
3. **Post-completion** — add `schema_version` UPDATE statement to 3.2.0 as the final step.
