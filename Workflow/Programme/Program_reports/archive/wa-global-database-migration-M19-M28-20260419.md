# DB-Wide Review — Migration Design Notes M19–M28 — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-database-migration-M19-M28-20260419.md |
| Instruction | `wa-global-database-review-instruction-v1_0-20260419.md` |
| Change Plan | `wa-global-database-changeplan-v1-20260419.md` (G2 approved 2026-04-19) |
| Migration code | `engine/migrate.py` — functions `_m19` … `_m28` |
| Target schema version | 3.10.0 (bumped from 3.9.0) |
| Dry-run DB copy | `backups/dryrun/bible_research_dryrun_M19-M28_20260419.db` |
| Dry-run outcome | **ALL 10 MIGRATIONS APPLIED CLEANLY** (2026-04-19) |
| FTS5 smoke test | PASS — insert + MATCH returns expected row |
| G3 gate | Per-migration approval required before Phase E execution |

---

## Consolidated Dry-Run Summary

All 10 migrations applied in sequence against a copy of the live DB (159 MB). Pre- and post-check outcomes match Phase A / Phase B investigation findings precisely.

| Migration | Applied | Pre-count / Input | Post-count / Output | Notes |
|---|---|---|---|---|
| M19 | ✓ | 37 orphan rows + 13 cascade candidates | 37 deletes + 13 cascade updates | Exactly matches Phase A §A.6 findings |
| M20 | ✓ | No prior prose tables | 5 tables + 3 triggers + 1 FTS5 virtual + 26 seed rows | FTS5 smoke test PASS |
| M21 | ✓ | `word_registry` had 23 cols | `word_registry` has 24 cols | `word_synopsis TEXT` added |
| M22 | ✓ | `status_note` in 2 tables | Both dropped | |
| M23 | ✓ | `mti_term_flags` 54 rows | `mti_term_flags` 1,005 rows | somatic +406, god_as_subject +545; post-check gap = 0 |
| M24 | ✓ | `somatic_link`/`god_as_subject` present | Both dropped | After M23 post-check clean |
| M25 | ✓ | `wa_dimension_index` 23 cols | `wa_dimension_index` 15 cols | 8 derivable columns dropped |
| M26 | ✓ | 8 controlled-vocab columns to check | All 8 clean (no violators) | CHECK rebuild deferred to M26b follow-on |
| M27 | ✓ | schema_version 3 rows, disordered id | 3 rows, chronological id | Date format normalised |
| M28 | ✓ | 92 indexes | 95 indexes; version 3.10.0 | Final version bump |

---

## Per-Migration Detail

---

### M19 — Orphan cleanup and soft-delete cascade

**DBR-CHG items:** 001, 002, 003, 004, 005

**Target tables:** `mti_term_cross_refs`, `wa_meaning_sense`, `wa_term_phase2_flags`, `wa_verse_records`, `verse_context_group`

**Operation:**

1. Hard-delete orphans:
    - `DELETE FROM mti_term_cross_refs WHERE mti_term_id NOT IN (SELECT id FROM mti_terms)` — 2 rows (both `mti_term_id=517`)
    - `DELETE FROM wa_meaning_sense WHERE parsed_meaning_id NOT IN (SELECT id FROM wa_meaning_parsed)` — 25 rows (parents 2173, 2310, 2311, 2312)
    - `DELETE FROM wa_term_phase2_flags WHERE term_inv_id NOT IN (SELECT id FROM wa_term_inventory)` — 10 rows (from `source='bulk_patch' 2026-03-19`)

2. Cascade soft-deletes:
    - Mark `wa_verse_records.delete_flagged=1` where parent term is `delete_flagged=1` — 6 rows
    - Mark `verse_context_group.delete_flagged=1` where parent mti term has `status='delete'` — 7 rows

**Pre-check:** COUNT(*) FROM each target filter.

**Post-check:** Same counts should return 0 after migration.

**Dry-run outcome:** PASS — counts 2+25+10+6+7 = 50 operations as expected.

**Risk:** LOW. **Data loss:** YES (37 hard-deleted rows). **Reversibility:** MODERATE via backup.

---

### M20 — Prose store setup

**DBR-CHG items:** 006, 007, 008, 009, 010, 011

**Target tables:** `prose_section_type`, `prose_section`, `prose_section_fts` (virtual), `prose_section_dimension_link`, `prose_section_finding_link`

**Operation:**

1. CREATE TABLE `prose_section_type` per prose store design §3.1 + index on (source_stage, lifecycle_tag)
2. CREATE TABLE `prose_section` per §3.2 with CHECK constraints on status + author + 3 indexes
3. CREATE VIRTUAL TABLE `prose_section_fts` (standalone FTS5, not content-linked — avoids base-table column pitfall) + 3 sync triggers
4. CREATE TABLE `prose_section_dimension_link` + `prose_section_finding_link`
5. INSERT OR IGNORE 26 seed rows into `prose_section_type`:
    - 6 Session A chapters (codes `sa_s1_d1` … `sa_s1_d6`) — Summary, Meaning, Verses, Terms, Pointers, Questions
    - 5 Session B Stage 2c chapters (codes `sb_s2c_ch1` … `sb_s2c_ch5`) — per catalogue extract
    - 5 Session C v1 chapters (codes `sc_v1_ch1` … `sc_v1_ch5`) — Synopsis, Description, Inner being at work, At work in scripture, Lexicon
    - 10 Session D cluster synthesis types (codes `sd_synthesis_Cl1` … `sd_synthesis_Cl10`)

**FTS5 design note:** switched from content-linked (`content='prose_section'`) to standalone during dry-run because the declared FTS column `section_type_code` is a joined-in denormalised value, not a base-table column. Standalone FTS5 stores its own copy of data; larger footprint but unambiguous semantics. Triggers explicitly sync.

**Pre-check:** Tables do not exist.

**Post-check:** All 5 tables present; 26 seed rows; FTS5 smoke test (insert + MATCH query) returns expected row.

**Dry-run outcome:** PASS. FTS5 smoke test confirmed.

**Risk:** LOW. **Data loss:** NO. **Reversibility:** EASY (DROP TABLE).

---

### M21 — word_synopsis column

**DBR-CHG item:** 012

**Target table:** `word_registry`

**Operation:** `ALTER TABLE word_registry ADD COLUMN word_synopsis TEXT` (via `_add_column_if_missing` helper — idempotent).

**Pre-check:** column absent.

**Post-check:** `PRAGMA table_info(word_registry)` shows column present.

**Dry-run outcome:** PASS — column added.

**Risk:** LOW. **Data loss:** NO. **Reversibility:** EASY.

---

### M22 — Obvious redundant column drops

**DBR-CHG items:** 013, 014

**Target tables:** `wa_term_inventory`, `mti_terms`

**Operation:** `ALTER TABLE ... DROP COLUMN status_note` on each (SQLite 3.35+, engine is 3.50.4).

**Pre-check:** columns present.

**Post-check:** columns absent.

**Dry-run outcome:** PASS — both dropped.

**Risk:** MEDIUM (data loss — 1,681 cells total). **Reversibility:** MODERATE via backup.

---

### M23 — MTI flag data reconciliation

**DBR-CHG items:** 015, 016
**RD reference:** RD-DBR-003 RESOLVED — option (a) populate then drop

**Target table:** `mti_term_flags` (INSERT); `wa_term_inventory` (READ only)

**Operation:**

1. `INSERT OR IGNORE INTO mti_term_flags(mti_term_id, flag_id)` — from somatic_link=1 → flag_id=3
2. `INSERT OR IGNORE INTO mti_term_flags(mti_term_id, flag_id)` — from god_as_subject=1 → flag_id=1

**Pre-check:** 54 rows in `mti_term_flags`; 162/208 source rows in `wa_term_inventory`.

**Post-check:** Count of mti_terms with `somatic_link=1` that STILL lack `mti_term_flags.flag_id=3`: must be 0. Same for god_as_subject / flag_id=1.

**Dry-run outcome:** PASS — 406 somatic + 545 god inserts; both gaps = 0. (Higher insert counts than source row counts are expected: the JOIN expands per mti_terms duplicates by strongs_number.)

**Risk:** MEDIUM. **Data loss:** NO (additive). **Reversibility:** EASY — DELETE matching criteria.

---

### M24 — Drop reconciled boolean flags

**DBR-CHG items:** 017, 018

**Target table:** `wa_term_inventory`

**Operation:** DROP COLUMN somatic_link; DROP COLUMN god_as_subject.

**Pre-check (explicit gate):** M23 post-check must have been 0 gaps.

**Post-check:** Columns absent.

**Dry-run outcome:** PASS.

**Risk:** MEDIUM. **Data loss:** YES — reflected in mti_term_flags post-M23. **Reversibility:** MODERATE.

---

### M25 — Dimension index simplification

**DBR-CHG items:** 019–026

**Target table:** `wa_dimension_index`

**Operation:**

1. Identify explicit indexes on `wa_dimension_index` that reference to-be-dropped columns; DROP them.
2. DROP COLUMN on 8 derivable columns:
    - `mti_term_id`, `group_code`, `strongs_number`
    - `transliteration`, `gloss`, `language`
    - `owning_registry_word`, `context_description`
3. RECREATE minimal retained indexes: on `verse_context_group_id`, `owning_registry_no`, `dimension`.

**Pre-check:** Columns present; index dependencies known.

**Post-check:** Columns dropped; new indexes present.

**Dry-run outcome:** PASS. Table down from 23 cols to 15; `idx_dim_index_mti` dropped; 3 new indexes created.

**Risk:** MEDIUM. **Data loss:** NO (all derivable via joins). **Reversibility:** EASY.

---

### M26 — Constraint coverage (pre-check only)

**DBR-CHG items:** 027–034
**RD reference:** RD-DBR-001 RESOLVED — option (a): update LOCK_SENTINEL to `'In Progress'`

**Target tables:** `word_registry`, `wa_term_inventory`, `wa_dimension_index`

**Operation:** Pre-check only for this migration. For each of the 8 controlled-vocabulary columns:

- Query `SELECT DISTINCT col` and compare against the allowed value set
- Report whether the column is clean (no violators) or has values outside the allowed set

If all 8 are clean, a follow-on migration **M26b** (to be authored when confirmed clean) applies the CHECK constraints via the table-rebuild pattern. Not applied in this migration to keep the bundle focused on pre-check / verification only.

**Dry-run outcome:** ALL 8 clean (no violators). 4/word_registry + 3/wa_term_inventory + 1/wa_dimension_index.

**Risk:** LOW (no state change). **Data loss:** NO. **Reversibility:** TRIVIAL (nothing to reverse).

**Follow-on:** M26b is a candidate for the next Change Plan revision (outside this bundle).

---

### M27 — schema_version rebuild

**DBR-CHG items:** 035, 036, 037
**RD reference:** RD-DBR-002 RESOLVED — option (a): rebuild with chronological id + normalised dates

**Target table:** `schema_version`

**Operation:**

1. Read existing rows `(version_code, applied_at, migration_history, engine_min_version)`
2. Normalise `applied_at` to `'YYYY-MM-DDTHH:MM:SSZ'` form (T-separator UTC)
3. Sort rows chronologically
4. CREATE `schema_version_new` with same schema
5. INSERT rows ordered — new id reflects order
6. DROP old table, RENAME new → `schema_version`

**Pre-check:** Row count.

**Post-check:** Same row count, new id ordering, consistent dates.

**Dry-run outcome:** PASS. Before: id=1→3.9.0, id=2→3.7.1, id=3→3.8.0 (disordered). After: id=1→3.7.1, id=2→3.8.0, id=3→3.9.0 (which M28 then bumps to 3.10.0).

**Side-effect:** `get_schema_version` helper and `_update_migration_history` in `engine/db.py` and `engine/migrate.py` updated to use `MAX(id)` pattern (Phase D deliverable already completed for compatibility with the rebuild).

**Risk:** LOW (small table, content preserved). **Data loss:** NO. **Reversibility:** EASY via backup.

---

### M28 — Index optimisation and final version bump

**DBR-CHG items:** 038, 039, 040, 041, 042

**Target tables:** `wa_term_inventory`, `wa_verse_records`, `verse_context`, `schema_version`

**Operation:**

1. CREATE partial index `idx_wa_ti_strongs_live` ON `wa_term_inventory(strongs_number)` WHERE delete_flagged=0
2. CREATE partial index `idx_wa_vr_term_live` ON `wa_verse_records(term_inv_id)` WHERE delete_flagged=0
3. CREATE partial index `idx_vc_grp_anchor_live` ON `verse_context(group_id, is_anchor)` WHERE delete_flagged=0 AND is_anchor=1
4. UPDATE `schema_version.version_code = '3.10.0'` on the latest row (MAX(id))

**Pre-check:** Indexes absent; version < 3.10.0.

**Post-check:** Indexes present; version = 3.10.0; `get_schema_version` returns 3.10.0.

**Dry-run outcome:** PASS. 3 partial indexes added; `get_schema_version(conn)` returns `'3.10.0'`.

**Risk:** LOW. **Data loss:** NO. **Reversibility:** TRIVIAL.

---

## Phase D side-effects already applied (early)

The following non-migration changes were made alongside the migration authoring, because M27 and the MAX(id) semantics of schema_version require them to be in place for the dry-run to validate:

1. **`engine/db.py::get_schema_version`** — updated to use `WHERE id = (SELECT MAX(id) FROM schema_version)`. Back-compatible with pre-M27 state where MAX(id) == 1.
2. **`engine/migrate.py::_update_migration_history`** — same pattern (MAX(id)).
3. **`engine/constants.py::LOCK_SENTINEL`** — changed from `'IN_PROGRESS'` to `'In Progress'` per RD-DBR-001 resolution.
4. **`engine/constants.py::EXPECTED_SCHEMA_VERSION`** — bumped from `'3.9.0'` to `'3.10.0'`.
5. **`Workflow/schema/create_tables.sql`** — regenerated from dry-run post-migration DB. Prior file preserved as `create_tables.sql.pre_DBR_bak`.

Full Phase D script update log will be produced separately covering remaining consumer-script updates (applicator operations, `build_complete_extract.py`, etc.).

---

## Rollback Procedure (all migrations)

**For any single migration failure during Phase E execution:**

1. Halt Phase E
2. Take snapshot: `bible_research_post_fail_M{N}_{ts}.db`
3. Restore pre-migration backup: copy `backups/bible_research_pre_M{N}_{ts}.db` → `database/bible_research.db`
4. Verify `get_schema_version` reflects pre-M{N} state
5. Record rollback in execution log
6. Produce RD item for corrective action

**Full rollback of all 10 migrations:**

Restore the baseline backup `backups/bible_research_pre_DBR_20260419_122435.db` to `database/bible_research.db`. This reverts to the pre-Phase-A state.

---

## Per-Migration G3 Approval Block

Each migration requires G3 approval before application during Phase E. Marking one block here as a unit is acceptable if all 10 are approved together (they have been at G2).

| Migration | G3 Approval | Date | Notes |
|---|---|---|---|
| M19 | [ ] APPROVED | | Ready (dry-run clean) |
| M20 | [ ] APPROVED | | Ready (dry-run clean; FTS5 smoke PASS) |
| M21 | [ ] APPROVED | | Ready |
| M22 | [ ] APPROVED | | Ready |
| M23 | [ ] APPROVED | | Ready (dry-run gap = 0) |
| M24 | [ ] APPROVED | | Ready (conditional on M23 post-check) |
| M25 | [ ] APPROVED | | Ready (dry-run clean) |
| M26 | [ ] APPROVED | | Pre-check only; follow-on M26b authored separately |
| M27 | [ ] APPROVED | | Ready (schema_version rebuild tested) |
| M28 | [ ] APPROVED | | Ready (final version bump) |

### Consolidated G3 Approval (batch)

Status: [X] APPROVED ALL — PROCEED to Phase E execution  [ ] PARTIAL — see per-migration table  [ ] REVISIONS REQUESTED

Date: 2026-04-19

Reviewer: le Roux Cilliers

Notes: Dry-run clean; all 10 migrations approved as a batch. Proceed with Phase E execution on live DB.

---

*End of migration design notes M19–M28 — 2026-04-19*
