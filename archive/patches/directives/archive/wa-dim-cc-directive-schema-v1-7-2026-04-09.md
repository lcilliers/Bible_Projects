# WA-DIM CC Directive — Schema Additions for DimensionReview v1.7
Date: 2026-04-09
Directive type: Schema DDL
Governing instruction: WA-DimensionReview-Instruction-v1.7-2026-04-09
Previous schema version: 3.7.0 (database_schema_20260408.json)

---

## Action Required

Apply the following schema additions to `bible_research.db` before any DIMREVIEW patch that includes a stamp operation is applied. These additions are required by Section 10.3 of WA-DimensionReview-Instruction-v1.7-2026-04-09.

Do not apply a DIMREVIEW patch containing `word_registry` stamp operations or a `wa_dim_review_cluster_log` insert until all three DDL statements below are confirmed successful.

---

## DDL — Apply in order

```sql
-- 1. Registry-level Dimension Review status field
ALTER TABLE word_registry ADD COLUMN dim_review_status TEXT DEFAULT NULL;

-- 2. Registry-level Dimension Review version field
ALTER TABLE word_registry ADD COLUMN dim_review_version TEXT DEFAULT NULL;

-- 3. Cluster-level Dimension Review completion log
CREATE TABLE wa_dim_review_cluster_log (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  cluster             TEXT    NOT NULL UNIQUE,
  completed_date      TEXT    NOT NULL,
  instruction_version TEXT    NOT NULL,
  registry_count      INTEGER NOT NULL DEFAULT 0,
  group_count         INTEGER NOT NULL DEFAULT 0,
  anchored_count      INTEGER NOT NULL DEFAULT 0,
  notes               TEXT,
  last_modified       TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now'))
);
```

---

## Verification Queries

Run after DDL application. All three must return expected results before any stamp operation proceeds.

```sql
-- 1. Confirm dim_review_status column exists on word_registry
SELECT COUNT(*) as col_exists
FROM pragma_table_info('word_registry')
WHERE name = 'dim_review_status';
-- Expected: 1

-- 2. Confirm dim_review_version column exists on word_registry
SELECT COUNT(*) as col_exists
FROM pragma_table_info('word_registry')
WHERE name = 'dim_review_version';
-- Expected: 1

-- 3. Confirm wa_dim_review_cluster_log table exists
SELECT COUNT(*) as table_exists
FROM sqlite_master
WHERE type = 'table' AND name = 'wa_dim_review_cluster_log';
-- Expected: 1

-- 4. Confirm all existing word_registry rows show NULL for both new fields
SELECT COUNT(*) as rows_with_null
FROM word_registry
WHERE dim_review_status IS NULL AND dim_review_version IS NULL
  AND session_b_status IS NOT NULL;
-- Expected: 181 (all active registries start with NULL stamps)

-- 5. Confirm wa_dim_review_cluster_log is empty
SELECT COUNT(*) as row_count FROM wa_dim_review_cluster_log;
-- Expected: 0
```

---

## Reporting

Report to researcher:
- Confirmation that all three DDL statements applied successfully
- Results of all five verification queries
- Updated schema version (increment patch-level: 3.7.0 → 3.8.0 or per current versioning convention)
- Confirmation that DIMREVIEW patches with stamp operations may now be applied

If any DDL statement fails, report the error and do not proceed with any DIMREVIEW patch that includes stamp operations.

---

## Context

These schema additions support the Dimension Review version stamp system introduced in WA-DimensionReview-Instruction-v1.7-2026-04-09 Section 10. The stamps record, at registry and cluster level, which version of the instruction was used to review and confirm the data. Session B gates on `wa_dim_review_cluster_log` containing a record for the cluster (Section 10.4). The additions have no effect on existing data — all new fields default to NULL and the new table starts empty.

This directive is a one-time operation. Once applied and verified, no further DDL is required for v1.7 stamp operations.
