# DB-Wide Review — Schema Completion Record — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-database-completion-20260419.md |
| Instruction | `wa-global-database-review-instruction-v1_0-20260419.md` |
| Phase | F — Documentation Regeneration and Completion (G5 artefact) |
| Produced | 2026-04-19 |

---

## Summary

**Schema version before:** 3.9.0
**Schema version after:** 3.10.0

**Migrations applied:** M19 → M28 (10 migrations, all successful on live DB 2026-04-19)

### Tables added

- `prose_section_type` — 26 seeded rows (6 Session A + 5 Session B Stage 2c + 5 Session C v1 + 10 Session D synthesis)
- `prose_section` — 0 rows (ready for writes)
- `prose_section_fts` — FTS5 virtual table (standalone)
- `prose_section_dimension_link` — 0 rows (ready)
- `prose_section_finding_link` — 0 rows (ready)

### Columns added

- `word_registry.word_synopsis TEXT` — researcher-authored 1–2 sentence word synopsis (rendered into Session A Summary section)

### Columns dropped

- `wa_term_inventory.status_note` (M22)
- `mti_terms.status_note` (M22)
- `wa_term_inventory.somatic_link` (M24, after M23 populated `mti_term_flags` flag_id=3)
- `wa_term_inventory.god_as_subject` (M24, after M23 populated `mti_term_flags` flag_id=1)
- `wa_dimension_index.mti_term_id`, `.group_code`, `.strongs_number`, `.transliteration`, `.gloss`, `.language`, `.owning_registry_word`, `.context_description` (M25 — all derivable via joins)

### Indexes changed

- 3 new partial indexes (M28): `idx_wa_ti_strongs_live`, `idx_wa_vr_term_live`, `idx_vc_grp_anchor_live`
- `idx_dim_index_mti` dropped (M25 — column gone)
- 3 `wa_dimension_index` indexes recreated on retained columns (M25)

### Structural changes

- `mti_term_flags` populated with 951 new flag rows (somatic +406, god_as_subject +545) to reconcile with dropped boolean columns (M23). Post-check gap = 0.
- `schema_version` table rebuilt with chronologically ordered id and normalised ISO-8601 UTC `applied_at` (M27).
- 37 orphan rows hard-deleted (M19); 13 soft-delete cascade inconsistencies resolved.

### Constraint strengthening

- M26 pre-check confirmed all 8 controlled-vocabulary columns clean (no violators). Actual CHECK application deferred to M26b (outstanding task OT-DBR-008).

---

## Migrations Executed

| M | Description | Applied at |
|---|---|---|
| M19 | Orphan cleanup and cascade soft-delete | 2026-04-19T13:36Z |
| M20 | Prose store setup (5 tables + FTS5 + 26 seeds) | 2026-04-19T13:36Z |
| M21 | Add `word_registry.word_synopsis` | 2026-04-19T13:36Z |
| M22 | Drop `status_note` columns | 2026-04-19T13:36Z |
| M23 | Populate `mti_term_flags` from booleans | 2026-04-19T13:36Z |
| M24 | Drop `somatic_link` / `god_as_subject` | 2026-04-19T13:36Z |
| M25 | Simplify `wa_dimension_index` (drop 8 derivable cols) | 2026-04-19T13:36Z |
| M26 | CHECK pre-check (constraint coverage) | 2026-04-19T13:37Z |
| M27 | Rebuild `schema_version` chronologically | 2026-04-19T13:37Z |
| M28 | Partial indexes + version bump to 3.10.0 | 2026-04-19T13:37Z |

---

## Phase D — Script Updates

See [wa-global-database-scriptupdates-20260419.md](wa-global-database-scriptupdates-20260419.md).

- Updated: 7 files (migrate.py, db.py, constants.py, create_tables.sql, export_database_schema.py, schema JSON, file manifest)
- Archived: 7 files per Q4
- Deferred: 5 consumer-script rewrites tracked as OT-DBR-001/002/003/004/005 in outstanding tasks file

---

## Phase F Actions Completed

### F.1 — Schema JSON regeneration

- File: `data/schema/database-schema-v3.10.0-20260419.json` — regenerated post-migration
- Fixed `scripts/export_database_schema.py::get_schema_version` to use MAX(id) pattern

### F.2 — File manifest rebuild

- File: `database/file_manifest.json` — refreshed
- Totals: 2,678 files (1,938 active, 740 archived — the 7 newly-archived scripts are counted in the 740)

### F.3 — CLAUDE.md updates

- Header timestamp noted 2026-04-19 DB-wide review
- §3 schema section title: "v3.9.0" → "v3.10.0"
- §3 Table Groups: added Table Group 17 "Prose Store" entry
- §4 Key Constants: `EXPECTED_SCHEMA_VERSION = "3.10.0"`; `LOCK_SENTINEL = "In Progress"` with rationale
- §10 Current Programme State: updated date to 2026-04-19; added schema v3.10.0 marker; documented 6-word reset; flagged OT-DBR-001/002 as known blockers
- §17.6: rewritten — redundant fields split into "DROPPED" (5 columns) and "RETAINED" (inference_note + new word_synopsis) sections

### F.4 — Readiness sweep design review (per Q9)

The sweep design `research/investigations/wa-global-readiness-sweep-design-v1-20260419.md` is in DRAFT state (awaiting researcher markup of Q1–Q14). Post-migration review required:

- **Phase R.B term checks** — update to reference `mti_term_flags` joins instead of dropped `somatic_link`/`god_as_subject` fields (Section B1 of v1.6 pattern)
- **Phase R.E dimension checks** — update for simplified `wa_dimension_index` (15 cols, joins for derived data)
- **Phase R.H (new)** — consider adding prose coverage checks now that prose store is operational

These updates are part of the follow-on sweep design work; not blocking for DB review closeout.

### F.5 — Instruction documents requiring review (per Q10)

The following instruction docs reference dropped columns or old schema assumptions and will need revision in a follow-on session:

- **wa-claudecode-instruction [current]** — if any references to dropped columns in CC responsibilities
- **wa-patch-instruction [current]** — needs PROSE patch type + new operations documented
- **wa-sessionb-analysis-readiness [current]** — v1.6 Step 1.2 Section B1 references `somatic_link` and `god_as_subject` checks — replace with `mti_term_flags` joins
- **wa-registry-management-guide [current]** — `word_synopsis` is a new column researchers will author
- **wa-reference [current]** — schema reference section

These updates happen post-DB-review per Q10. Logged here for awareness.

### F.6 — 6-Word Reprocess Trigger (per Q12)

**DONE** — 2026-04-19. Six registries reset:

| no | word | prior session_b_status | new session_b_status |
|---|---|---|---|
| 23 | compassion | Analysis Complete | Verse Context Reset |
| 62 | fellowship | Analysis Complete | Verse Context Reset |
| 64 | forgiveness | Analysis Complete | Verse Context Reset |
| 68 | grace | Analysis Complete | Verse Context Reset |
| 103 | love | Analysis Complete | Verse Context Reset |
| 111 | mercy | Analysis Complete | Verse Context Reset |

Prior Session B narratives (`.md` files in `Sessions/Session_B/09_Analysis_output_logs/` and `outputs/markdown/`) remain as historical artefacts — not deleted, not imported into the prose store at this time (deferred per prose store design Q2 = "new work only").

**Reprocess is NOT yet runnable** — blocked by OT-DBR-001 / OT-DBR-002 (audit_word.py and audit.py need rewrite to use `mti_term_flags` joins). Reprocess will resume once those are fixed.

---

## Sweep Design Items Requiring Update (per Q9)

See §F.4 above. Short list:

- Replace `somatic_link` / `god_as_subject` references with `mti_term_flags` joins
- Update `wa_dimension_index` reading paths (15 cols; join for derived data)
- Add optional Phase R.H prose coverage checks

---

## Instruction Documents Requiring Review (per Q10)

See §F.5 above. Short list:

- `wa-patch-instruction` (PROSE type)
- `wa-sessionb-analysis-readiness` (v1.6 Section B1 + B3 data references)
- `wa-registry-management-guide` (word_synopsis)
- `wa-reference` (schema reference)
- `wa-claudecode-instruction` (if any direct column references)

---

## Outstanding Tasks (carry-forward from this review)

See [`outputs/wa-global-outstanding-tasks-v1-20260419.md`](../wa-global-outstanding-tasks-v1-20260419.md) for the full register:

| Task ID | Priority | Subject |
|---|---|---|
| OT-DBR-001 | HIGH | `engine/audit_word.py` rewrite for `mti_term_flags` joins |
| OT-DBR-002 | HIGH | `engine/audit.py` update |
| OT-DBR-003 | MEDIUM | applicator PROSE operations |
| OT-DBR-004 | MEDIUM | `build_dimension_extract.py` update |
| OT-DBR-005 | LOW | `word_full_extract.py` update |
| OT-DBR-006 | RESOLVED | 7 scripts archived |
| OT-DBR-007 | LOW | schema consumer validation |
| OT-DBR-008 | LOW | M26b CHECK constraint application |

---

## G5 Approval Block

**DB-WIDE REVIEW COMPLETE — schema v3.9.0 → v3.10.0**

Artefacts produced across all phases (Phase A through F):

- Phase A: `outputs/reports/wa-global-database-audit-20260419.md` (G1 approved)
- Phase B: `outputs/reports/wa-global-database-changeplan-v1-20260419.md` (G2 approved)
- Phase C: `outputs/reports/wa-global-database-migration-M19-M28-20260419.md` (G3 approved)
- Phase D: `outputs/reports/wa-global-database-scriptupdates-20260419.md` (G4 — this session)
- Phase E: `outputs/reports/wa-global-database-execution-20260419.md` (all migrations applied)
- Phase F: `outputs/reports/wa-global-database-completion-20260419.md` (this file — G5)

Supporting:

- RD accumulator: `outputs/wa-global-databasereview-rd-v1-20260419.md` (3 items resolved)
- Outstanding tasks: `outputs/wa-global-outstanding-tasks-v1-20260419.md` (8 items, 1 resolved, 7 open)
- Per-session obslogs: `outputs/session-logs/wa-global-databasereview-obslog-v1{,.1,.2,.3,.4}-20260419.md`
- Per-session session logs: `outputs/session-logs/wa-global-databasereview-sessionlog-v1{,.1,.2,.3}-20260419.md`
- Baseline backup: `backups/bible_research_pre_DBR_20260419_122435.db` (159 MB, retained 6+ months)
- Per-migration backups: 10 files in `backups/bible_research_pre_M{19–28}_20260419_133xxx.db`

**Preconditions for readiness sweep start (per Q7):**

- [X] Phase A audit complete (G1 approved)
- [X] Phase B Change Plan approved (G2)
- [X] Phase C migration design + dry-run clean (G3)
- [X] Phase E migrations applied to live DB
- [X] Phase D critical script updates (remainder tracked as outstanding tasks)
- [X] Phase F documentation regenerated
- [X] Schema Completion Record produced (this document)

**Readiness sweep may begin** — but note it would require the audit_word/audit rewrites (OT-DBR-001/002) first if it triggers any audit_word re-runs. The sweep itself can inspect and classify without audit_word, but any Path 2 re-extraction directives will be blocked until OT-DBR-001 is resolved.

---

Status: [X] APPROVED — DB review complete; readiness sweep may be scheduled  [ ] REVISIONS REQUESTED

Date: 2026-04-19

Reviewer: le Roux Cilliers

Notes: DB-wide review formally closed. Schema at 3.10.0. Readiness sweep work authorised — proceed to prepare sweep instruction.

---

*End of Schema Completion Record — 2026-04-19*
