# WA — CC Schema Directive: Session B Catalogue Integration
**Filename:** wa-global-dir-20260416-001-schema-catalogue-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Directive reference:** DIR-20260416-001
**Governed by:** wa-global-general-rules-v2_2-20260415.json (GR-DIR-001 through GR-DIR-005)
**Design authority:** wa-global-schema-sessionb-changes-v1_1-20260416.md
**Previous output refs:**
- wa-global-schema-sessionb-changes-v1_1-20260416.md (schema design document)
- wa-global-sessionb-update-tasklist-v1_2-20260416.md (task T-SC)
- database-schema-20260416.json (schema v3.8.0 — baseline)

---

## Directive Summary

Five schema changes are required to support the Session B catalogue integration. All five are additive — no existing data is modified, no columns are removed, no tables are dropped. The current row counts in affected tables are preserved intact.

**Scope:**
- SC-01: ALTER `wa_session_b_findings` — add 2 columns
- SC-02: ALTER `wa_term_phase2_flags` — add 2 columns
- SC-03: CREATE TABLE `wa_obs_question_catalogue`
- SC-04: CREATE TABLE `wa_finding_catalogue_links`
- SC-05: ALTER `wa_finding_entity_links` — add 1 column

---

## Motivation

The Session B instruction is being updated to integrate the Observation-Question Master Catalogue (194 questions, `wa-global-obs-question-master-catalogue-v2_0-20260415.md`) into the analytical process. This requires:

1. A lifecycle `status` field and a term-link `term_id` field on `wa_session_b_findings` — to track finding progress through Session B and link findings to specific terms
2. Soft-delete support on `wa_term_phase2_flags` — to record rejected flags during the Stage 1 audit (Step 1.3a) without physical deletion
3. A new table `wa_obs_question_catalogue` — to store all analytical questions (universal and word-specific) as a queryable database asset
4. A new junction table `wa_finding_catalogue_links` — to record the many-to-many links between findings and catalogue questions, with coverage and validation status
5. A soft-delete field on `wa_finding_entity_links` — consistent with the programme-wide `delete_flagged` convention; table was created without it

---

## Operations

Execute all five operations in the order listed. Each is independent and safe to execute sequentially. Confirm each operation before proceeding to the next.

---

### SC-01 — ALTER `wa_session_b_findings`: add 2 columns

**Table:** `wa_session_b_findings` (current row count: 171)

**Operation:** Add two columns.

```sql
ALTER TABLE wa_session_b_findings
ADD COLUMN status TEXT DEFAULT 'pending';

ALTER TABLE wa_session_b_findings
ADD COLUMN term_id INTEGER REFERENCES mti_terms(id) ON DELETE SET NULL;
```

**Expected outcome:**
- Column `status` exists on `wa_session_b_findings` with default value `'pending'`
- Column `term_id` exists on `wa_session_b_findings`, nullable, FK to `mti_terms(id)`
- All 171 existing rows have `status = 'pending'` and `term_id = NULL`
- No existing data is changed

**Valid values for `status`:** `pending` / `in_review` / `complete`

---

### SC-02 — ALTER `wa_term_phase2_flags`: add 2 columns

**Table:** `wa_term_phase2_flags` (current row count: 1,580)

**Operation:** Add two columns.

```sql
ALTER TABLE wa_term_phase2_flags
ADD COLUMN delete_flagged INTEGER DEFAULT 0;

ALTER TABLE wa_term_phase2_flags
ADD COLUMN obsolete_reason TEXT;
```

**Expected outcome:**
- Column `delete_flagged` exists on `wa_term_phase2_flags` with default value `0`
- Column `obsolete_reason` exists on `wa_term_phase2_flags`, nullable TEXT
- All 1,580 existing rows have `delete_flagged = 0` and `obsolete_reason = NULL`
- No existing data is changed

---

### SC-03 — CREATE TABLE `wa_obs_question_catalogue`

**Table:** `wa_obs_question_catalogue` (does not exist — new table)

**Operation:** Create the table.

```sql
CREATE TABLE wa_obs_question_catalogue (
    obs_id            INTEGER  PRIMARY KEY AUTOINCREMENT,
    question_code     TEXT     NOT NULL UNIQUE,
    section           TEXT     NOT NULL,
    source_word       TEXT,
    source_registry_no INTEGER  REFERENCES word_registry(id),
    question_text     TEXT     NOT NULL,
    pattern_type      TEXT,
    scope             TEXT     NOT NULL DEFAULT 'universal',
    status            TEXT     NOT NULL DEFAULT 'active',
    deleted           INTEGER  NOT NULL DEFAULT 0,
    date_added        TEXT     NOT NULL,
    catalogue_version TEXT     NOT NULL
);
```

**Expected outcome:**
- Table `wa_obs_question_catalogue` exists with 12 columns as specified
- `obs_id` is auto-generated integer PK
- `question_code` has a UNIQUE constraint
- `scope` has three valid values: `universal` / `word_specific` (populated at question level)
- `status` has three valid values: `active` / `word_specific` / `non_word`
- `deleted` is soft-delete flag — 0 by default
- Table is empty at creation — population (194 rows from master catalogue v2.0) is a separate operation

**Note on `scope` vs `status`:**
- `scope` — the analytical scope at question creation: `universal` (applies to every word) or `word_specific` (formulated for one word's analysis only)
- `status` — the operational state: `active` (in the standard rotation), `word_specific` (captured but not in universal rotation), `non_word` (occasionally applicable, not standard)
These serve different purposes and both are retained.

---

### SC-04 — CREATE TABLE `wa_finding_catalogue_links`

**Table:** `wa_finding_catalogue_links` (does not exist — new table)

**Operation:** Create the table.

```sql
CREATE TABLE wa_finding_catalogue_links (
    id              INTEGER  PRIMARY KEY AUTOINCREMENT,
    finding_id      INTEGER  NOT NULL REFERENCES wa_session_b_findings(id),
    question_id     INTEGER  NOT NULL REFERENCES wa_obs_question_catalogue(obs_id),
    coverage        TEXT,
    status          TEXT     NOT NULL DEFAULT 'suggested',
    pattern_type    TEXT,
    mapped_date     TEXT,
    validated_date  TEXT,
    validated_by    TEXT,
    session_b_note  TEXT,
    delete_flagged  INTEGER  NOT NULL DEFAULT 0,
    UNIQUE (finding_id, question_id)
);
```

**Expected outcome:**
- Table `wa_finding_catalogue_links` exists with 11 columns as specified
- `id` is auto-generated integer PK
- Unique constraint on `(finding_id, question_id)` prevents duplicate links
- `status` valid values: `suggested` / `validated` / `rejected`
- `coverage` valid values: `FULL` / `PARTIAL` (nullable — assigned during Session B validation)
- FKs enforce: `finding_id` → `wa_session_b_findings(id)`; `question_id` → `wa_obs_question_catalogue(obs_id)`
- Table is empty at creation

---

### SC-05 — ALTER `wa_finding_entity_links`: add 1 column

**Table:** `wa_finding_entity_links` (current row count: 0)

**Operation:** Add one column.

```sql
ALTER TABLE wa_finding_entity_links
ADD COLUMN delete_flagged INTEGER NOT NULL DEFAULT 0;
```

**Expected outcome:**
- Column `delete_flagged` exists on `wa_finding_entity_links` with default value `0`
- Table remains empty — no data impact
- Consistent with programme-wide soft-delete convention

---

## Verification Required After Execution

After all five operations are complete, run the following verification and return the results:

**1. Column check — `wa_session_b_findings`:**
```sql
PRAGMA table_info(wa_session_b_findings);
```
Confirm: `status` and `term_id` appear in results.

**2. Column check — `wa_term_phase2_flags`:**
```sql
PRAGMA table_info(wa_term_phase2_flags);
```
Confirm: `delete_flagged` and `obsolete_reason` appear in results.

**3. Table existence and column check — `wa_obs_question_catalogue`:**
```sql
PRAGMA table_info(wa_obs_question_catalogue);
```
Confirm: 12 columns present; `obs_id`, `question_code`, `status`, `deleted` visible.

**4. Table existence and column check — `wa_finding_catalogue_links`:**
```sql
PRAGMA table_info(wa_finding_catalogue_links);
```
Confirm: 11 columns present; unique constraint visible.

**5. Column check — `wa_finding_entity_links`:**
```sql
PRAGMA table_info(wa_finding_entity_links);
```
Confirm: `delete_flagged` appears in results.

**6. Row count confirmation — no data loss:**
```sql
SELECT
    (SELECT COUNT(*) FROM wa_session_b_findings)   AS findings_rows,
    (SELECT COUNT(*) FROM wa_term_phase2_flags)     AS phase2_flags_rows,
    (SELECT COUNT(*) FROM wa_finding_entity_links)  AS entity_links_rows,
    (SELECT COUNT(*) FROM wa_obs_question_catalogue) AS catalogue_rows,
    (SELECT COUNT(*) FROM wa_finding_catalogue_links) AS cat_links_rows;
```
Expected: `findings_rows = 171`, `phase2_flags_rows = 1580`, `entity_links_rows = 0`, `catalogue_rows = 0`, `cat_links_rows = 0`.

**7. Default value spot-check:**
```sql
SELECT status, term_id FROM wa_session_b_findings LIMIT 5;
SELECT delete_flagged, obsolete_reason FROM wa_term_phase2_flags LIMIT 5;
SELECT delete_flagged FROM wa_finding_entity_links LIMIT 1;
```
Expected: `status = 'pending'`, `term_id = NULL`, `delete_flagged = 0`, `obsolete_reason = NULL` on all rows.

---

## Expected Outcome Summary

| SC | Table | Change | Rows affected |
|---|---|---|---|
| SC-01 | `wa_session_b_findings` | +2 columns (status, term_id) | 171 existing rows get defaults |
| SC-02 | `wa_term_phase2_flags` | +2 columns (delete_flagged, obsolete_reason) | 1,580 existing rows get defaults |
| SC-03 | `wa_obs_question_catalogue` | New table — 12 columns | 0 rows (population is separate) |
| SC-04 | `wa_finding_catalogue_links` | New table — 11 columns | 0 rows |
| SC-05 | `wa_finding_entity_links` | +1 column (delete_flagged) | 0 rows (table was empty) |

No data is deleted. No existing columns are modified. No existing rows are changed except for default value population on new columns.

---

## Schema Version

After successful execution and verification, the schema version should be updated to **v3.9.0** to reflect these additive structural changes.

---

## Completion Confirmation Required

CC must return:
1. Confirmation that all five operations executed without error
2. The PRAGMA table_info output for all five affected tables
3. The row count query result
4. The default value spot-check result
5. Confirmation of schema version update to v3.9.0

This directive is complete when all five confirmations are returned and verified by Claude AI.

---

*End of wa-global-dir-20260416-001-schema-catalogue-v1-20260416.md*
*Governed by wa-global-general-rules-v2_2-20260415.json*
*Design authority: wa-global-schema-sessionb-changes-v1_1-20260416.md*
