# DB-Wide Review — Session Log v1.2 — 2026-04-19 (session 3)

| Field | Value |
|---|---|
| Filename | wa-global-databasereview-sessionlog-v1.2-20260419.md |
| Session date | 2026-04-19 (session 3 — Phase C) |
| Obslog version at close | wa-global-databasereview-obslog-v1.2-20260419.md |
| Governing instruction | wa-global-database-review-instruction-v1_0-20260419.md |
| Session outcome | Phase C complete; G3 awaiting approval |

---

## What Was Accomplished

**Phase C — Migration Development — COMPLETE**

All 10 migrations (M19–M28) designed, authored, dry-run-verified against a live-DB copy, and documented. Five supporting non-migration changes applied to the codebase (Phase D early deliverables) to enable the dry-run.

### Artefacts produced

1. **Migration code** — `engine/migrate.py` gained functions `_m19` through `_m28` (10 `@_register`-decorated migrations). ~320 lines added.
2. **Design notes (consolidated)** — [outputs/reports/wa-global-database-migration-M19-M28-20260419.md](../reports/wa-global-database-migration-M19-M28-20260419.md) covering all 10 migrations with rationale, pre/post-checks, dry-run outcomes, rollback procedure, per-migration G3 approval blocks + batch G3 approval block.
3. **Canonical DDL** — `data/schema/create_tables.sql` regenerated from the dry-run post-migration DB. Prior preserved as `create_tables.sql.pre_DBR_bak`.
4. **Dry-run DB copy** — `backups/dryrun/bible_research_dryrun_M19-M28_20260419.db` retained as evidence.
5. **Observations log v1.2** — [obslog v1.2](../session-logs/wa-global-databasereview-obslog-v1.2-20260419.md) with Phase C execution record.

### Code changes (Phase D deliverables applied early — required for dry-run correctness)

| File | Change | Reason |
|---|---|---|
| `engine/db.py::get_schema_version` | WHERE id=1 → WHERE id=(SELECT MAX(id) FROM schema_version) | M27 rebuilds schema_version so id=1 becomes earliest; MAX(id) reads latest. Back-compatible pre-M27. |
| `engine/migrate.py::_update_migration_history` | Same MAX(id) pattern | Same reason |
| `engine/constants.py::LOCK_SENTINEL` | `'IN_PROGRESS'` → `'In Progress'` | RD-DBR-001 resolution |
| `engine/constants.py::EXPECTED_SCHEMA_VERSION` | `'3.9.0'` → `'3.10.0'` | M28 target |
| `data/schema/create_tables.sql` | Regenerated | Reflect post-migration target state |

---

## Dry-Run Evidence Summary

Two iterations:

- **Iteration 1:** Surfaced 2 bugs — FTS5 `content='prose_section'` referenced non-existent column `section_type_code`; M25 ALTER TABLE DROP COLUMN failed due to dependent index.
- **Iteration 2 (after fixes):** ALL 10 migrations applied cleanly.

Post-migration verification:

- M19: 2 + 25 + 10 orphan deletes; 6 + 7 cascade updates → matches Phase A §A.6 exactly
- M20: 5 tables + 3 triggers + FTS5 virtual + 26 seed rows; FTS5 MATCH smoke test PASS
- M21: `word_registry.word_synopsis TEXT` added
- M22: Both `status_note` columns dropped
- M23: `mti_term_flags` grown from 54 → 1,005 rows; post-check gap 0/0
- M24: `somatic_link` + `god_as_subject` dropped from `wa_term_inventory`
- M25: `wa_dimension_index` shrunk from 23 → 15 columns; dependent index handled; 3 retained indexes recreated
- M26: All 8 controlled-vocabulary columns clean (no violators); CHECK rebuild deferred to follow-on M26b
- M27: `schema_version` rebuilt chronologically (id=1→3.7.1 earliest; id=3→3.9.0 latest)
- M28: 3 partial indexes added; version bumped to 3.10.0; `get_schema_version()` returns `'3.10.0'`

---

## Current Position

**Phase C is complete pending G3 approval.**

G3 gating model (per instruction): each migration requires G3 before application in Phase E. User may grant individually or as a batch (preferred given all 10 are co-designed and dry-run-verified together).

**Preconditions for Phase E to begin:**

- [ ] G3 approval on [design notes](../reports/wa-global-database-migration-M19-M28-20260419.md) — batch or per-migration
- No outstanding RD items — all 3 resolved 2026-04-19
- Baseline backup present — yes (`backups/bible_research_pre_DBR_20260419_122435.db`, 159 MB)

---

## Open Items

**No open RD items.** (RD-DBR-001/002/003 all RESOLVED.)

**Outstanding tasks file:** not created — no items beyond CC's skill surfaced.

**Minor follow-on considerations:**

- **M26b** — a follow-on migration to actually apply the CHECK constraints via table-rebuild pattern. M26 was pre-check only by design. M26b can be authored for the next Change Plan revision.
- **Phase D remaining work** — consumer-script updates beyond the 5 done early:
  - `scripts/apply_session_patch.py` — add PROSE patch type + 7 new operations (insert/supersede/delete/approve/bulk_supersede/session_a_replace on `prose_section`; inserts on link tables)
  - `scripts/build_complete_extract.py` — include prose sections; drop references to removed columns
  - Archive redundant scripts per Q4
  - Other scripts that referenced dropped columns (`somatic_link`, `god_as_subject`, `mti_terms.status_note`, `wa_term_inventory.status_note`, denormalised dimension_index fields)
- **Phase F** — docs regeneration + 6-word reprocess trigger per Q12

---

## Exact Resume Instructions

**Next session starts at:** Phase E execution (after G3 approval).

**Precondition before starting Phase E:**

1. Confirm G3 marker(s) present on `outputs/reports/wa-global-database-migration-M19-M28-20260419.md`
2. Take fresh pre-migration backup: `python -m engine.engine --backup --label="pre_M19_<ts>"` (instruction Phase E Step E.2)
3. Increment obslog to v1.3 at session 4 start
4. Confirm schema version still 3.9.0 in live DB (not yet migrated)

**First Phase E action:** Step E.1 per M19 — confirm G3 approval; take backup; run pre-check; `python -m engine.engine --migrate` will apply all pending M19–M28 sequentially (transactionally per migration). Post-check + smoke tests per migration per instruction §12.

**Alternative:** if researcher wants to apply migrations one at a time (safer), invoke with `--to=M19` first, verify, then `--to=M20`, etc. The `_MIGRATIONS` registry runner supports `stop_at` parameter.

---

## Downloads / Deliverables

1. [outputs/session-logs/wa-global-databasereview-obslog-v1.2-20260419.md](../session-logs/wa-global-databasereview-obslog-v1.2-20260419.md) (session 3 obslog)
2. [outputs/session-logs/wa-global-databasereview-sessionlog-v1.2-20260419.md](../session-logs/wa-global-databasereview-sessionlog-v1.2-20260419.md) (this file)
3. [outputs/reports/wa-global-database-migration-M19-M28-20260419.md](../reports/wa-global-database-migration-M19-M28-20260419.md) (**the G3 artefact**)
4. `engine/migrate.py` (modified — M19–M28 added)
5. `engine/db.py` (modified — get_schema_version uses MAX(id))
6. `engine/constants.py` (modified — LOCK_SENTINEL and EXPECTED_SCHEMA_VERSION)
7. `data/schema/create_tables.sql` (regenerated)
8. `data/schema/create_tables.sql.pre_DBR_bak` (retained pre-migration DDL)
9. `backups/dryrun/bible_research_dryrun_M19-M28_20260419.db` (dry-run evidence)

---

**SESSION CLOSED: 2026-04-19 (session 3)**

Next session: resume at Phase E execution after G3 approval on migration design notes.

*End of session log v1.2 — 2026-04-19*
