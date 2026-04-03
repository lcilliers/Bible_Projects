# WA-VerseContext-SetupInstruction-v1-20260329

**Framework B — Soul Word Analysis Programme**
**Verse Context Stage — Setup Instruction**
**Version 1.1 | March 2026 | Status: Active**

| **Document** | **Value** |
|---|---|
| Filename | WA-VerseContext-SetupInstruction-v1_1-20260329.md |
| Supersedes | WA-VerseContext-SetupInstruction-v1-20260329.md |
| Change note | v1.1 — Section 1.0 added: patch applicator update (`apply_session_patch.py`) required before any Verse Context patch is applied. Verse Context patch types (VERSECONTEXT, VCGROUP, VCVERSE) exempted from `session_b_status` presence requirement. |
| Audience | Claude Code exclusively |
| Purpose | All schema migrations, field changes, data resets, and validations required before Verse Context work begins |
| Governing reference | WA-VerseContext-ImpactStudy-v3-20260329.md |
| Companion documents | WA-VerseContext-Instruction-v1-20260329.md |

---

## 0. Purpose and Scope

This document governs all setup actions that must be completed before any Verse Context work begins. It covers two schema migrations (M17 and M18), field removals, programme-wide status resets, and data integrity validations.

**Sequence is mandatory.** Each task must be completed and validated before the next begins. Do not proceed on partial completion.

**Do not execute until researcher approval is confirmed.**

After all tasks are confirmed complete, schema version advances from 3.7.0 to 3.8.0 and the programme is ready for Verse Context Stage 1.

---

## 1. Pre-Execution Checks

Before executing any migration, run these checks and report results.

### 1.0 Update patch applicator — REQUIRED BEFORE ANY VERSE CONTEXT PATCH IS APPLIED

The current `apply_session_patch.py` rejects any patch where `session_b_status` is absent or null in `_patch_meta`. Verse Context patches intentionally carry `session_b_status: null` — they operate via `verse_context_status`, not `session_b_status`.

Update the validation logic in `apply_session_patch.py` as follows:

- Patches of type `VERSECONTEXT`, `VCGROUP`, and `VCVERSE` are exempt from the `session_b_status` presence requirement
- For all other patch types (`PREANALYSIS`, `SESSIONB`, `REPAIR`, `CLUSTERING`, `SESSIOND`): retain the existing rejection behaviour — `session_b_status` must be present and non-null
- Where `session_b_status` is present in `_patch_meta` but its value is `null` AND the patch type is a Verse Context type: accept and proceed without setting `session_b_status` on `word_registry`

**Validation:**
Confirm the updated applicator accepts a test patch with `"session_b_status": null` and `patch_id` containing `VERSECONTEXT` without rejection. Confirm it still rejects a PREANALYSIS patch with null `session_b_status`.

This code change must be confirmed before any Verse Context patch is submitted.

### 1.1 SQLite version check

```sql
SELECT sqlite_version();
```

Record the version. Migration strategy for M17 depends on it:
- 3.35.0+ → DROP COLUMN supported
- 3.25.0+ → RENAME COLUMN supported
- Below 3.25.0 → table recreation required for both operations

### 1.2 Current schema state

```sql
SELECT version_code, applied_at, migration_history
FROM schema_version
ORDER BY id DESC LIMIT 1;
```

Expected: version_code = '3.7.0', migration_history includes M01–M16.

### 1.3 Current programme state

```sql
SELECT session_b_status, COUNT(*) as count
FROM word_registry
GROUP BY session_b_status
ORDER BY session_b_status;
```

Record all counts. Expected baseline: 33 NULL, 35 Analysis Complete, 144 Ready for Analysis.

### 1.4 Confirm tables do not already exist

```sql
SELECT name FROM sqlite_master
WHERE type='table'
AND name IN ('verse_context_group','verse_context');
```

Expected: zero rows. If either table already exists, stop and report to researcher before proceeding.

---

## 2. Migration M17 — Field Corrections on `word_registry`

Two actions on `word_registry`. Execute as a single transaction where possible.

### 2.1 Action 1 — Rename `source_category` to `dimensions`

This rename was documented in WA-Reference v5.1 (March 2026) but the migration was never executed. The column has been referred to as `dimensions` in all analytical documents since then. The rename brings the database into alignment with programme documentation.

**No data migration required** — existing values are retained. Only the column name changes.

**If SQLite >= 3.25.0:**
```sql
ALTER TABLE word_registry RENAME COLUMN source_category TO dimensions;
```

**If SQLite < 3.25.0 — table recreation:**
```sql
-- Step 1: Create new table with correct column name
CREATE TABLE word_registry_new AS SELECT * FROM word_registry;
-- Then rebuild with correct schema via migrate.py standard pattern
-- See migrate.py for table recreation procedure
```

**Validation:**
```sql
-- Must succeed:
SELECT dimensions FROM word_registry LIMIT 1;

-- Must fail with "no such column":
SELECT source_category FROM word_registry LIMIT 1;

-- Data integrity — count must be unchanged:
SELECT COUNT(*) FROM word_registry;
```

### 2.2 Action 2 — Remove `anchor_verses` field

`word_registry.anchor_verses` is an informal free-text field holding ad-hoc verse references. It is superseded by the `verse_context` anchor mechanism which operates at term level with formal structure. The field is redundant and its removal reduces confusion.

**⚠ SQLite DROP COLUMN requires version 3.35.0+**

**If SQLite >= 3.35.0:**
```sql
ALTER TABLE word_registry DROP COLUMN anchor_verses;
```

**If SQLite < 3.35.0:**
The column cannot be dropped. Apply the following deprecation action instead:

```sql
-- Record deprecation in schema notes
UPDATE schema_version
SET migration_history = migration_history || ', M17-anchor_verses-deprecated'
WHERE id = (SELECT MAX(id) FROM schema_version);
```

Then update all instruction documents to ignore this field. Do not write to it. Do not read from it in exports. Flag it in the schema as deprecated.

**Report the SQLite version outcome to researcher** — confirming whether the field was dropped or deprecated.

**Validation (if dropped):**
```sql
-- Must fail with "no such column":
SELECT anchor_verses FROM word_registry LIMIT 1;
```

**Validation (if deprecated):**
```sql
-- Must succeed but field should contain no analytical data going forward:
SELECT anchor_verses FROM word_registry WHERE anchor_verses IS NOT NULL LIMIT 5;
-- Report any existing values to researcher for information
```

### 2.3 Update schema_version for M17

```sql
INSERT INTO schema_version (version_code, applied_at, migration_history, engine_min_version)
VALUES ('3.7.1', date('now'),
  (SELECT migration_history FROM schema_version ORDER BY id DESC LIMIT 1) || ', M17',
  (SELECT engine_min_version FROM schema_version ORDER BY id DESC LIMIT 1));
```

---

## 3. Migration M18 — New Tables and New Field

### 3.1 Create `verse_context_group`

```sql
CREATE TABLE IF NOT EXISTS verse_context_group (
  id                  INTEGER PRIMARY KEY,
  mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id),
  group_code          TEXT NOT NULL UNIQUE,
  context_description TEXT NOT NULL,
  notes               TEXT DEFAULT NULL,
  delete_flagged      INTEGER DEFAULT 0
);
```

**Field notes:**
- `id` — INTEGER PK, auto-increment. Used for all joins. Never use group_code as a join key.
- `mti_term_id` — FK to `mti_terms.id`. Programme-wide term identifier. One record per Strong's number. Never registry-instance specific.
- `group_code` — format `{mti_term_id}-{3-digit-serial}` e.g. `142-001`. Constructed by Claude AI at patch time. Human-readable reference only.
- `context_description` — brief phrase capturing the inner-being engagement of the term in this group. Produced by Claude AI during Verse Context.
- `delete_flagged` — 1 = dissolved group. Programme-wide no-physical-delete policy applies to this table.

**Validation:**
```sql
SELECT name FROM sqlite_master WHERE type='table' AND name='verse_context_group';
-- Expected: one row

PRAGMA table_info(verse_context_group);
-- Confirm all columns present
```

### 3.2 Create `verse_context`

```sql
CREATE TABLE IF NOT EXISTS verse_context (
  id              INTEGER PRIMARY KEY,
  verse_record_id INTEGER NOT NULL REFERENCES wa_verse_records(id),
  mti_term_id     INTEGER NOT NULL REFERENCES mti_terms(id),
  group_id        INTEGER REFERENCES verse_context_group(id),
  is_anchor       INTEGER NOT NULL DEFAULT 0,
  is_relevant     INTEGER NOT NULL DEFAULT 0,
  is_related      INTEGER NOT NULL DEFAULT 0,
  notes           TEXT DEFAULT NULL,
  delete_flagged  INTEGER DEFAULT 0,
  UNIQUE (verse_record_id, mti_term_id, group_id)
);
```

**Field notes:**
- `is_anchor = 1` — this verse is the canonical citation for its group. Session B reads this. Programme cites this.
- `is_relevant = 0` — verse set aside (no inner-being engagement for this term in this verse). group_id must be NULL.
- `is_related = 1` — verse shares group meaning with anchor; pre-classified; not re-read in Session B.
- `delete_flagged = 1` — record excluded. Programme-wide no-physical-delete policy.
- UNIQUE constraint: same verse may appear under two groups for the same term (dual-context) but never twice in the same group.

**Logical consistency rules Claude Code must validate after patch application:**

| Rule | Check |
|---|---|
| R1 | SELECT COUNT(*) FROM verse_context WHERE is_relevant=0 AND (group_id IS NOT NULL OR is_anchor=1 OR is_related=1); — Expected: 0 |
| R2 | SELECT COUNT(*) FROM verse_context WHERE is_anchor=1 AND (is_relevant=0 OR is_related=1 OR group_id IS NULL); — Expected: 0 |
| R3 | SELECT COUNT(*) FROM verse_context vc WHERE is_related=1 AND NOT EXISTS (SELECT 1 FROM verse_context a WHERE a.group_id=vc.group_id AND a.is_anchor=1 AND a.delete_flagged=0); — Expected: 0 |

**Validation:**
```sql
SELECT name FROM sqlite_master WHERE type='table' AND name='verse_context';
-- Expected: one row

PRAGMA table_info(verse_context);
-- Confirm all columns present
```

### 3.3 Add `verse_context_status` to `word_registry`

```sql
ALTER TABLE word_registry
ADD COLUMN verse_context_status TEXT DEFAULT NULL;
```

Valid values: NULL / `In Progress` / `Complete`

This field tracks Verse Context completion independently of `session_b_status`. It operates at registry level — Claude Code sets it based on OWNER term completion (see Section 5). Claude AI does not set this field directly.

**Validation:**
```sql
SELECT verse_context_status FROM word_registry LIMIT 1;
-- Expected: returns NULL (default)

SELECT COUNT(*) FROM word_registry WHERE verse_context_status IS NOT NULL;
-- Expected: 0 (before status reset in Section 4)
```

### 3.4 Update schema_version for M18

```sql
INSERT INTO schema_version (version_code, applied_at, migration_history, engine_min_version)
VALUES ('3.8.0', date('now'),
  (SELECT migration_history FROM schema_version ORDER BY id DESC LIMIT 1) || ', M18',
  (SELECT engine_min_version FROM schema_version ORDER BY id DESC LIMIT 1));
```

---

## 4. Programme-Wide Status Resets

Execute these operations only after M17 and M18 are both confirmed complete. Each operation must be validated before the next proceeds.

### 4.1 Set `verse_context_status` for active registries

```sql
UPDATE word_registry
SET verse_context_status = 'In Progress'
WHERE phase1_status = 'Complete'
  AND phase1_term_count > 0
  AND phase1_term_count IS NOT NULL;
```

**Validation:**
```sql
SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'In Progress';
-- Record count — expected approximately 177

SELECT no, word, phase1_status, phase1_term_count, verse_context_status
FROM word_registry
WHERE phase1_status = 'Complete'
  AND (phase1_term_count = 0 OR phase1_term_count IS NULL);
-- Report any Complete registries with zero terms to researcher
```

### 4.2 Reset 35 Analysis Complete registries

These registries completed Session B under the old word-by-word workflow. With the introduction of pool-based simultaneous Session B, their analyses must be rerun with cross-word context. Their existing analytical documents (narratives, patches, JSON outputs) are parked — not deleted — but superseded.

```sql
UPDATE word_registry
SET session_b_status = 'Verse Context Reset',
    verse_context_status = 'In Progress'
WHERE session_b_status = 'Analysis Complete';
```

**`Verse Context Reset`** is a new `session_b_status` value meaning: prior Session B work exists but has been superseded by pool-based re-analysis. It is distinct from NULL (never started). The existing analytical documents for these 35 registries are retained on disk for reference but are no longer the current analytical record.

**Validation:**
```sql
SELECT COUNT(*) FROM word_registry WHERE session_b_status = 'Verse Context Reset';
-- Expected: 35

SELECT no, word FROM word_registry WHERE session_b_status = 'Verse Context Reset' ORDER BY no;
-- Report full list to researcher for information
```

### 4.3 Review 33 NULL-status registries

```sql
SELECT no, word, phase1_status, phase1_term_count, session_b_status, verse_context_status
FROM word_registry
WHERE session_b_status IS NULL
ORDER BY no;
```

For each registry returned: if `phase1_status = 'Complete'` and `phase1_term_count > 0`, it should have been captured by Operation 4.1. If not, investigate and resolve. Report findings to researcher.

### 4.4 Final programme state validation

```sql
SELECT
  session_b_status,
  verse_context_status,
  COUNT(*) as count
FROM word_registry
GROUP BY session_b_status, verse_context_status
ORDER BY session_b_status, verse_context_status;
```

Report full matrix to researcher before proceeding.

---

## 5. Claude Code Operational Rules for Verse Context

These rules govern Claude Code's behaviour throughout the Verse Context stage. They are established here and referenced by the Verse Context instruction.

### 5.1 Batch construction rules

Batches contain OWNER terms only (`wa_term_inventory.term_owner_type = 'OWNER'`). Never include XREF terms in batches.

Include only terms where `mti_terms.status IN ('extracted', 'extracted_thin')`. Exclude `delete`, `candidate_delete`, `excluded`.

Include only terms where `COUNT(wa_verse_records WHERE delete_flagged = 0) > 0`. Terms with zero active verse records are excluded from Verse Context.

Target 2,000–2,500 unclassified verses per batch. Never split a term across batches.

Priority order: terms where `verse_context` records do not exist, ordered by `mti_terms.owning_registry_fk` ascending.

### 5.2 Registry completion check

After applying each VERSECONTEXT patch, for each registry whose OWNER terms appear in the batch:

```sql
-- Check 1: Any OWNER terms in this registry still missing verse_context records?
SELECT COUNT(*) as unclassified_owner_terms
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE wr.no = {registry_no}
  AND ti.term_owner_type = 'OWNER'
  AND ti.delete_flagged = 0
  AND mt.status IN ('extracted','extracted_thin')
  AND EXISTS (SELECT 1 FROM wa_verse_records vr
              WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0)
  AND NOT EXISTS (SELECT 1 FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0);
```

If result > 0: registry remains `In Progress`.

If result = 0: advance `verse_context_status` to `Complete`:

```sql
UPDATE word_registry
SET verse_context_status = 'Complete'
WHERE no = {registry_no};
```

### 5.3 Anchor integrity check

After any VCGROUP or VCVERSE patch that may affect anchor status, for each affected term:

```sql
SELECT COUNT(*) as active_anchors
FROM verse_context vc
WHERE vc.mti_term_id = {mti_term_id}
  AND vc.is_anchor = 1
  AND vc.delete_flagged = 0;
```

If result = 0: flag to researcher — this term has no anchor and cannot proceed to Session B. Do not advance registry status.

### 5.4 Re-extraction trigger

After every audit_word re-run on any registry:

```sql
-- Find OWNER terms with new verse records not yet in verse_context
SELECT DISTINCT mt.id as mti_term_id, mt.strongs_number
FROM wa_verse_records vr
JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
JOIN mti_terms mt ON mt.id = vr.mti_term_id
WHERE ti.term_owner_type = 'OWNER'
  AND vr.delete_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse_context vc
    WHERE vc.verse_record_id = vr.id
      AND vc.mti_term_id = mt.id
  );
```

For each term returned: set the owning registry's `verse_context_status = 'In Progress'`.

Also cascade delete_flag on verse records to verse_context:
```sql
UPDATE verse_context
SET delete_flagged = 1
WHERE verse_record_id IN (
  SELECT id FROM wa_verse_records WHERE delete_flagged = 1
)
AND delete_flagged = 0;
```

### 5.5 Integrity validation — run after every patch cycle

```sql
-- Validate: no active verse_context for delete/excluded terms
SELECT mt.strongs_number, mt.status, COUNT(vc.id) as active_vc_rows
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.status IN ('delete','excluded')
  AND vc.delete_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation — report to researcher.
```

### 5.6 group_code → integer id resolution

When applying a VERSECONTEXT patch, verse_context_group inserts must be processed before verse_context inserts. After each group insert, capture the new integer id:

```sql
SELECT last_insert_rowid() as new_group_id;
```

Use this integer for all subsequent verse_context inserts in the same patch that reference this group. Never use group_code as a join key in the database.

---

## 6. Post-Setup Confirmation

When all tasks are complete, run the following confirmation report and provide to researcher:

```sql
-- Schema version
SELECT version_code, applied_at, migration_history FROM schema_version ORDER BY id DESC LIMIT 1;

-- New tables
SELECT name FROM sqlite_master WHERE type='table'
AND name IN ('verse_context_group','verse_context');

-- word_registry field state
PRAGMA table_info(word_registry);

-- Programme state matrix
SELECT session_b_status, verse_context_status, COUNT(*) as count
FROM word_registry
GROUP BY session_b_status, verse_context_status
ORDER BY session_b_status, verse_context_status;

-- Verse Context ready registries
SELECT COUNT(*) as ready_for_verse_context
FROM word_registry
WHERE verse_context_status = 'In Progress';
```

Report all results. Researcher confirms readiness before Verse Context Stage 1 begins.

---

*WA-VerseContext-SetupInstruction-v1-20260329 | Claude Code only | Execute with researcher approval | Governs all setup actions for Verse Context implementation*
