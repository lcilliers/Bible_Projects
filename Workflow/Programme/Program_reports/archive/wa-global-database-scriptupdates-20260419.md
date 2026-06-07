# DB-Wide Review — Phase D Script Update Log — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-database-scriptupdates-20260419.md |
| Phase | D — Script Update Sweep |
| Instruction | `wa-global-database-review-instruction-v1_0-20260419.md` |
| Produced | 2026-04-19 |

---

## Summary

Phase D partial — critical script changes applied; remaining consumer updates tracked in outstanding tasks file.

| Category | Count |
|---|---|
| Files updated in place (active consumers) | 4 |
| Files archived per Q4 | 7 |
| Applicator operations to be added | 10 (deferred — OT-DBR-003) |
| Broken scripts needing rewrite | 5 (deferred — OT-DBR-001/002/004/005) |

---

## Updated files

| File | Change | Rationale |
|---|---|---|
| `engine/migrate.py` | Added M19–M28 (~320 lines); `_update_migration_history` uses MAX(id) pattern | Phase C migration authoring + post-M27 ordering |
| `engine/db.py` | `get_schema_version` uses MAX(id) pattern | M27 rebuilds `schema_version` with chronological id; latest is MAX(id) |
| `engine/constants.py` | `EXPECTED_SCHEMA_VERSION = "3.10.0"`; `LOCK_SENTINEL = "In Progress"` | M28 target; RD-DBR-001 resolution |
| `Workflow/schema/create_tables.sql` | Regenerated from post-migration DB | Canonical DDL reflects target state; prior preserved as `.pre_DBR_bak` |
| `scripts/export_database_schema.py` | `get_schema_version` uses MAX(id) pattern | Same fix as `engine/db.py` for consistent schema version reads |
| `data/schema/database-schema-v3.10.0-20260419.json` | New export | Phase F.1 schema JSON regeneration |
| `database/file_manifest.json` | Rebuilt (2678 files, 1938 active, 740 archived) | Phase F.2 manifest refresh |

---

## Archived files (per Q4 — redundant due to dropped columns or superseded purpose)

All moved from `scripts/` to `archive/scripts/` on 2026-04-19:

| Source | Reason |
|---|---|
| `_analyse_term_inventory.py` | Diagnostic on dropped `somatic_link` / `god_as_subject` / `status_note` columns; purpose moot |
| `_repair_04_wa_term_inventory.py` | Repair script for columns that no longer exist |
| `_repair_09_mti.py` | References dropped `mti_terms.status_note` |
| `_preflight_validate.py` | Validation across dropped columns; would error in current shape |
| `_extract_word_terms.py` | 3-phase pipeline; superseded by single-pass `word_study_extract.py`; also references dropped columns |
| `_explore_soul_step_routes.py` | One-off exploration; references dropped `status_note` |
| `_exploratory_sessionb_export_v1_20260415.py` | Spec v1.1 extract; references dropped `somatic_link`/`god_as_subject`; superseded by `build_complete_extract.py` for post-migration work |

---

## Deferred to outstanding tasks file

Tracked in `outputs/wa-global-outstanding-tasks-v1-20260419.md`:

| Task ID | Priority | Subject |
|---|---|---|
| OT-DBR-001 | HIGH | `engine/audit_word.py` rewrite for `mti_term_flags` joins |
| OT-DBR-002 | HIGH | `engine/audit.py` update |
| OT-DBR-003 | MEDIUM | `scripts/apply_session_patch.py` PROSE operations + 3 pre-existing applicator gaps |
| OT-DBR-004 | MEDIUM | `scripts/build_dimension_extract.py` update for wa_dimension_index simplification |
| OT-DBR-005 | LOW | `scripts/word_full_extract.py` update |
| OT-DBR-007 | LOW | `create_tables.sql` consumer validation |
| OT-DBR-008 | LOW | M26b follow-on for actual CHECK constraint application |

**Why deferred:** these require substantive engineering (not mechanical edits) plus testing. Doing them at speed risks introducing bugs. HIGH-priority items block Phase F.6 reprocess runs; LOW/MEDIUM items are non-blocking.

---

## Unaffected files (intentionally not updated)

- `engine/gap_fill.py`, `engine/new_word.py` — flagged "superseded, retained for reference" in CLAUDE.md §4. References to dropped columns are historical; not a live code path.
- `engine/migrate.py` M01–M15 function bodies — these reference columns that are now dropped, but only within historical migrations whose content is immutable (per DBR-12 / Q5). References are correct in the context of when those migrations ran; no update needed.
- Files in `archive/` (pre-existing) — per Q4 policy, pre-existing archive is left alone.
- `Sessions/Patches/**/*.json` — historical patches; immutable per DBR-12.

---

## G4 Approval Block

Status: [X] APPROVED — Phase D complete (with deferred items tracked in outstanding tasks)  [ ] REVISIONS REQUESTED

Date: 2026-04-19

Reviewer: le Roux Cilliers

Notes: Phase D partial approved. Critical infrastructure updates applied. Consumer-script rewrites (audit_word, audit, applicator PROSE, build_dimension_extract) tracked as outstanding tasks OT-DBR-001 through OT-DBR-005.

---

*End of Phase D script update log — 2026-04-19*
