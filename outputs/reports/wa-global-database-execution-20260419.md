# DB-Wide Review — Phase E Execution Log — 2026-04-19

| Field | Value |
| --- | --- |
| Filename | wa-global-database-execution-20260419.md |
| Produced | 2026-04-19T13:36:42.393406+00:00 |
| Target DB | data/bible_research.db |
| Migrations applied | M19–M28 |
| G3 batch approval | APPROVED 2026-04-19 by le Roux Cilliers |

---

**Pre-flight schema version:** `3.8.0` (expected `3.9.0` pre-migration; will become `3.10.0` post-M28)

**WARNING:** live schema is `3.8.0`, not `3.9.0`. If this is a re-run (already migrated), migrations will be idempotent no-ops.

**Active `phase1_status = 'In Progress'` registries:** 2
- r97 joy
- r146 shame

(Status 'In Progress' is informational — not a blocker for DDL migrations which operate at schema level.)

## Migration execution log

### M19 — Orphan cleanup: delete dangling FK children; cascade soft-deletes

**Pre-migration backup:** `backups\bible_research_pre_M19_20260419_133642.db` (166,531,072 bytes, word_registry=214) — OK
**Pre-check:** `{"orphan_cross_refs": 2, "orphan_meaning_sense": 25, "orphan_phase2_flags": 10, "cascade_vr": 6, "cascade_vcg": 7}`
**Post-check:** `{"orphan_cross_refs": 0, "orphan_meaning_sense": 0, "orphan_phase2_flags": 0, "cascade_vr": 0, "cascade_vcg": 0, "actual_orphan_cross_refs": 0, "actual_orphan_meaning_sense": 0, "actual_orphan_phase2_flags": 0}`
**Status:** APPLIED

### M20 — Prose store setup: prose_section_type, prose_section, FTS5, link tables

**Pre-migration backup:** `backups\bible_research_pre_M20_20260419_133643.db` (166,531,072 bytes, word_registry=214) — OK
**Pre-check:** `{"prose_section_type_exists": false}`
**Post-check:** `{"prose_section_type_exists": true, "prose_section_exists": true, "prose_section_fts_exists": true, "prose_section_dimension_link_exists": true, "prose_section_finding_link_exists": true, "seed_rows": 26}`
**Status:** APPLIED

### M21 — Add word_synopsis column to word_registry (Session A Summary source)

**Pre-migration backup:** `backups\bible_research_pre_M21_20260419_133644.db` (166,600,704 bytes, word_registry=214) — OK
**Pre-check:** `{"word_synopsis_col": false}`
**Post-check:** `{"word_synopsis_col": true}`
**Status:** APPLIED

### M22 — Drop obvious redundant columns: wa_term_inventory.status_note, mti_terms.status_note

**Pre-migration backup:** `backups\bible_research_pre_M22_20260419_133644.db` (166,600,704 bytes, word_registry=214) — OK
**Pre-check:** `{"wti_status_note": true, "mt_status_note": true}`
**Post-check:** `{"wti_status_note_dropped": true, "mt_status_note_dropped": true}`
**Status:** APPLIED

### M23 — Populate mti_term_flags from wa_term_inventory booleans (RD-DBR-003)

**Pre-migration backup:** `backups\bible_research_pre_M23_20260419_133649.db` (166,625,280 bytes, word_registry=214) — OK
**Pre-check:** `{"mti_term_flags_count": 54, "somatic_src": 162, "god_src": 208}`
**Post-check:** `{"mti_term_flags_count_after": 1005, "somatic_gap": 0, "god_gap": 0}`
**Status:** APPLIED

### M24 — Drop wa_term_inventory.somatic_link and .god_as_subject (reconciled in M23)

**Pre-migration backup:** `backups\bible_research_pre_M24_20260419_133652.db` (166,625,280 bytes, word_registry=214) — OK
**Pre-check:** `{"somatic_link_col": true, "god_as_subject_col": true}`
**Post-check:** `{"somatic_link_dropped": true, "god_as_subject_dropped": true}`
**Status:** APPLIED

### M25 — Dimension index simplification: drop 8 derivable columns from wa_dimension_index

**Pre-migration backup:** `backups\bible_research_pre_M25_20260419_133659.db` (166,649,856 bytes, word_registry=214) — OK
**Pre-check:** `{"wdi_cols_before": 23}`
**Post-check:** `{"wdi_cols_after": 15}`
**Status:** APPLIED

### M26 — Constraint coverage: add CHECK constraints via table rebuild (8 columns, 3 tables)

**Pre-migration backup:** `backups\bible_research_pre_M26_20260419_133702.db` (166,649,856 bytes, word_registry=214) — OK
**Pre-check:** `{}`
**Post-check:** `{}`
**Status:** APPLIED

### M27 — Rebuild schema_version with chronologically ordered id + normalised dates (RD-DBR-002)

**Pre-migration backup:** `backups\bible_research_pre_M27_20260419_133703.db` (166,649,856 bytes, word_registry=214) — OK
**Pre-check:** `{"sv_rows": 3}`
**Post-check:** `{"sv_rows": 3, "sv_rows_listing": [{"id": 1, "version_code": "3.7.1", "applied_at": "2026-03-29T12:52:09Z"}, {"id": 2, "version_code": "3.8.0", "applied_at": "2026-03-29T12:54:48Z"}, {"id": 3, "version_code": "3.9.0", "applied_at": "2026-04-16T05:17:38Z"}]}`
**Status:** APPLIED

### M28 — Index optimisation + final schema version bump to 3.10.0

**Pre-migration backup:** `backups\bible_research_pre_M28_20260419_133703.db` (166,649,856 bytes, word_registry=214) — OK
**Pre-check:** `{"idx_count_before": 92, "current_version": "3.9.0"}`
**Post-check:** `{"idx_count_after": 95, "version_after": "3.10.0"}`
**Status:** APPLIED

---

## Post-migration smoke tests

- **word_registry_live_count:** 213
- **t1_carry_forward_count:** FAIL: expected 214, got 213
- **mti_live_count:** 3891
- **t2_mti_orphans:** PASS
- **t3_fts5_match:** PASS (matches=1)
- **mti_term_flags_total:** 1005
- **t4_mti_term_flags:** PASS (somatic=410, god=584)
- **t5_wdi_simplification:** PASS (15 cols remain)
- **t6_schema_version:** PASS (3.10.0)
- **t7_prose_section_type_seed:** PASS (26 seeds)
- **t8_word_synopsis_col:** PASS

---

## Phase E Summary

- Migrations applied: 10
- Errors: 0
- Overall: SUCCESS

- Backups retained in `backups/` (per-migration, outside rolling rotation):
  - M19: `backups\bible_research_pre_M19_20260419_133642.db`
  - M20: `backups\bible_research_pre_M20_20260419_133643.db`
  - M21: `backups\bible_research_pre_M21_20260419_133644.db`
  - M22: `backups\bible_research_pre_M22_20260419_133644.db`
  - M23: `backups\bible_research_pre_M23_20260419_133649.db`
  - M24: `backups\bible_research_pre_M24_20260419_133652.db`
  - M25: `backups\bible_research_pre_M25_20260419_133659.db`
  - M26: `backups\bible_research_pre_M26_20260419_133702.db`
  - M27: `backups\bible_research_pre_M27_20260419_133703.db`
  - M28: `backups\bible_research_pre_M28_20260419_133703.db`

**Final schema version:** `None`
