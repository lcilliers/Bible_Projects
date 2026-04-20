# DB-Wide Review — Change Plan v1 — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-database-changeplan-v1-20260419.md |
| Instruction | `wa-global-database-review-instruction-v1_0-20260419.md` (Active — approved 2026-04-19) |
| Phase | B — Change Plan |
| Precondition | G1 approved 2026-04-19 on audit report |
| Audit source | `outputs/reports/wa-global-database-audit-20260419.md` |
| Deeper investigation | Recorded in obslog v1.1 (this session) |
| Organisation | Per-migration-phase bundles (per Q8 override — each bundle spans multiple related tables) |
| Produced | 2026-04-19 |

---

## Summary

- **Total bundles: 10**
- **Migrations:** M19 – M28
- **Tables touched across plan:** 18
- **Total DBR-CHG items:** 44
- **Risk aggregate:** LOW: 4 · MEDIUM: 5 · HIGH: 1
- **Data-loss migrations:** 3 (all with explicit approval required per DBR rules)
- **RD items gating plan execution:** 2 (RD-DBR-001, RD-DBR-002 — already filed)

---

## Revised Findings (post-deeper-investigation)

### Critical reversal: `somatic_link` and `god_as_subject` are NOT safely superseded

CLAUDE.md §17.6 states these columns are "superseded by `mti_term_flags`". **Live-data cross-check contradicts this:**

| Column | `wa_term_inventory` rows with value=1 | `mti_term_flags` rows covering same concept | Overlap | Gap if dropped |
|---|---|---|---|---|
| `somatic_link` | 162 | 6 (flag_id 3, 4) | 2 | **162 rows of somatic data lost** |
| `god_as_subject` | 208 | 39 (flag_id 1) | 13 | **195 rows of god-as-subject data lost** |

`mti_term_flags` total: 54 rows vs `wa_term_inventory` 7,164 active rows. The "supersession" did not happen at the data level.

**Consequence for Change Plan:** these columns cannot be dropped until the data is reconciled. Either:

- (A) Populate `mti_term_flags` from `wa_term_inventory` before dropping, then drop
- (B) Retain both — update CLAUDE.md §17.6 to reflect reality (neither is sole source; both are partial)
- (C) Designate `wa_term_inventory.*` as canonical and deprecate `mti_term_flags`

**RD item candidate:** raise this to researcher. Recommend (A) — populate-then-drop, in a two-phase bundle.

### `word_registry.inference_note` contains active researcher content — RETAIN

24 rows have substantive researcher-authored notes (e.g. "Character as a psychological construct — the sum of stable moral and psychological traits…"). CLAUDE.md §17.6 says "researcher-set only; pipeline must never overwrite" — implying retention was intentional all along.

**Consequence:** DROP recommendation from Phase A §A.8 REVERSED. Column RETAINED. Add CHECK or protective trigger to prevent pipeline overwrite. Update CLAUDE.md §17.6 to mark as RETAINED.

### `wa_dimension_index` denormalised fields — all consistent → safe to drop

0 mismatches across `mti_term_id`, `group_code`, `strongs_number` vs parent tables. Clean simplification candidate.

### `wa_verse_records.file_id` — 765 mismatches with `term_inv.file_id`

This FK is NOT derivable — cannot simply drop. Needs investigation of the 765 cases before any simplification.

### `verse_context.mti_term_id` — 0 mismatches but 27,230 (43%) rows have NULL `group_id`

Cannot drop `mti_term_id` because 43% of rows (set-aside verses) don't have a group to derive it from. Retain.

---

## Pre-Flight — Dependencies and Sequencing Constraints

1. **Orphan rows must be cleaned early** (Bundle 1) so later FK additions don't re-fail.
2. **Prose store tables must be added before** the Session A extract generation script expects them (Bundle 2).
3. **Data reconciliation (somatic_link / god_as_subject)** must precede column drops (Bundle 5 → Bundle 6).
4. **`schema_version` rebuild** (Bundle 9) should be late in the sequence — it is the record of what migrations were applied.
5. **Script updates (Phase D)** interleave with migrations: DB-access layers updated before DROP_COLUMN migrations; applicator extensions ready before new tables are consumed.

---

## Bundle Index

| Migration | Bundle descriptor | Tables touched | Risk | Data loss | RD gate |
|---|---|---|---|---|---|
| **M19** | Bundle 1 — Orphan & cascade cleanup | `mti_term_cross_refs`, `wa_meaning_sense`, `wa_term_phase2_flags`, `wa_verse_records`, `verse_context_group` | LOW | YES (explicit) | — |
| **M20** | Bundle 2 — Prose store setup | `prose_section_type`, `prose_section`, `prose_section_fts`, `prose_section_dimension_link`, `prose_section_finding_link` | LOW | NO | — |
| **M21** | Bundle 3 — Registry enrichment | `word_registry` | LOW | NO | — |
| **M22** | Bundle 4 — Obvious redundant drops | `wa_term_inventory`, `mti_terms` | MEDIUM | YES (confirmed ≤ 20%) | — |
| **M23** | Bundle 5 — MTI flag data reconciliation | `mti_term_flags`, `wa_term_inventory` | MEDIUM | NO (additive) | RD-DBR-003 (new) |
| **M24** | Bundle 6 — Drop reconciled bool flags | `wa_term_inventory` | MEDIUM | YES (post-reconcile) | Depends on M23 verification |
| **M25** | Bundle 7 — Dimension index simplification | `wa_dimension_index` | MEDIUM | NO (derivable) | — |
| **M26** | Bundle 8 — Constraint coverage | 8 columns across `word_registry`, `wa_term_inventory`, `wa_dimension_index` | MEDIUM | NO | RD-DBR-001 (lock sentinel resolution) |
| **M27** | Bundle 9 — `schema_version` rebuild | `schema_version` | LOW | NO (rebuild preserves content) | RD-DBR-002 |
| **M28** | Bundle 10 — Index optimisation | Various | LOW | NO | — |

*(Phase D non-migration work — LOCK_SENTINEL constant correction — will be a separate script-update item, not a migration.)*

---

## Bundles (in migration order)

---

### Migration Bundle M19 — Orphan & Cascade Cleanup

**Tables touched:** `mti_term_cross_refs`, `wa_meaning_sense`, `wa_term_phase2_flags`, `wa_verse_records`, `verse_context_group`

**Rationale:**

Phase A §A.6 found 37 orphan rows across 3 FKs plus 13 soft-delete cascade inconsistencies. Deeper investigation (this session) identified the specific rows. All are consequences of historical data operations that did not fully cascade. Must be cleaned before any FK additions or constraint strengthening.

**Changes:**

- **DBR-CHG-001** (`mti_term_cross_refs`): DELETE 2 rows where `mti_term_id = 517` (target `mti_terms.id` does not exist). Cross-refs for "mind" (r112) and "being" (r211). Reason: stale FK from prior `mti_terms` deletion.
- **DBR-CHG-002** (`wa_meaning_sense`): DELETE 25 rows where `parsed_meaning_id` is in (2173, 2310, 2311, 2312) — these parent `wa_meaning_parsed` rows no longer exist. Distinct orphan parent IDs: 4.
- **DBR-CHG-003** (`wa_term_phase2_flags`): DELETE 10 rows where `term_inv_id` is in (1059, 1061, 1065, 1066, 1071, 1072, 1075, 1077). All are `source='bulk_patch'` from 2026-03-19. Parent terms no longer exist.
- **DBR-CHG-004** (`wa_verse_records`): UPDATE `delete_flagged = 1` on 6 rows where parent `wa_term_inventory.delete_flagged = 1`. Cascade the soft-delete downward.
- **DBR-CHG-005** (`verse_context_group`): UPDATE `delete_flagged = 1` on 7 rows where parent `mti_terms.status = 'delete'`. Same cascade rationale.

**Risk:** LOW — all orphans are confirmed dangling; cascade cleanup is consistent with the soft-delete discipline.

**Reversibility:** MODERATE — deleted rows preserved only in backup. Pre-migration backup captures all 37 + 13 = 50 rows.

**Data loss:** YES — 37 hard-deleted rows. Approval: needs explicit `[X] APPROVED — acceptable loss (orphans)`.

**Scripts affected:** None (no active scripts reference these specific rows).

**Migration identifier:** M19

**Sequencing:** First — clears the decks for subsequent FK work.

---

### Migration Bundle M20 — Prose Store Setup

**Tables touched:** `prose_section_type`, `prose_section`, `prose_section_fts` (virtual), `prose_section_dimension_link`, `prose_section_finding_link`

**Rationale:**

Per `wa-prose-store-design-v1-20260419.md` (APPROVED 2026-04-19). Adds infrastructure for DB-canonical prose storage (Option D). Additive only.

**Changes:**

- **DBR-CHG-006** — CREATE TABLE `prose_section_type` per prose store design §3.1
- **DBR-CHG-007** — CREATE TABLE `prose_section` per §3.2
- **DBR-CHG-008** — CREATE VIRTUAL TABLE `prose_section_fts` (FTS5) + 3 sync triggers per §3.3
- **DBR-CHG-009** — CREATE TABLE `prose_section_dimension_link` per §3.4
- **DBR-CHG-010** — CREATE TABLE `prose_section_finding_link` per §3.4
- **DBR-CHG-011** — INSERT seed rows into `prose_section_type` (6 session_a types; 5 session_b Stage 2c chapters; 5 session_c v1 chapters; 10 session_d dimensional clusters). Column alignment in seed will follow schema §3.1 (chapter name in `label`, `lifecycle_tag = NULL` except Session C = 'v1').

**Risk:** LOW — pure additive; no impact on existing data.

**Reversibility:** EASY — `DROP TABLE` each in reverse order.

**Data loss:** NO.

**Scripts affected:**

- `scripts/apply_session_patch.py` — add PROSE patch type + 6 new operations (per Phase D)
- `scripts/build_complete_extract.py` — include approved prose sections (Phase D)
- New scripts: `scripts/export_prose.py`, `scripts/import_prose.py`, `scripts/render_prose.py`, `scripts/_test_prose_roundtrip.py` (Phase D)

**Migration identifier:** M20

**Sequencing:** Second — establishes prose infrastructure before any consumer script expects it.

---

### Migration Bundle M21 — Registry Enrichment

**Tables touched:** `word_registry`

**Rationale:**

Add `word_synopsis TEXT` column per Session A advice Q7 resolution (2026-04-19). Serves the Session A Summary section (1–2 sentence word synopsis, researcher-authored once per word).

**Changes:**

- **DBR-CHG-012** (`word_registry`): ADD COLUMN `word_synopsis TEXT NULL`.

**Risk:** LOW — single additive column.

**Reversibility:** EASY — ALTER TABLE DROP COLUMN (SQLite 3.35+).

**Data loss:** NO.

**Scripts affected:**

- `scripts/apply_session_patch.py` — allow `update` on `word_registry.word_synopsis`
- `scripts/build_complete_extract.py` — include `word_synopsis` in extract
- CLAUDE.md §3 — update schema reference

**Migration identifier:** M21

---

### Migration Bundle M22 — Obvious Redundant Column Drops

**Tables touched:** `wa_term_inventory`, `mti_terms`

**Rationale:**

Drop columns confirmed redundant with low data utility and zero code references in active scripts.

**Changes:**

- **DBR-CHG-013** (`wa_term_inventory`): DROP COLUMN `status_note`. Evidence: 177 / 7550 non-NULL (2.3%); zero code refs; purpose unclear.
- **DBR-CHG-014** (`mti_terms`): DROP COLUMN `status_note`. Evidence: 1504 / 7571 non-NULL (19.9%); zero code refs; written by audit_word A10 only, never read elsewhere. Content appears to be runtime diagnostics that have outlived usefulness.

**Note — REVERSAL from Phase A:**

- `word_registry.inference_note` — NOT DROPPED. Contains 24 substantive researcher notes; CLAUDE.md §17.6 already flagged as "researcher-set only, pipeline must never overwrite" (read: retention was intentional). Will update §17.6 to RETAINED.
- `wa_term_inventory.god_as_subject` and `.somatic_link` — deferred to M23/M24 (reconcile first).

**Risk:** MEDIUM — data loss but well-characterised.

**Reversibility:** MODERATE — data only in backup.

**Data loss:** YES — 177 + 1504 = 1,681 non-NULL text cells. Approval: needs explicit `[X] APPROVED — loss acceptable (stale diagnostics)`.

**Scripts affected:**

- `engine/db.py`, `engine/audit_word.py` — remove references to `mti_terms.status_note`
- Test: run one audit_word dry-run post-migration to confirm no break

**Migration identifier:** M22

---

### Migration Bundle M23 — MTI Flag Data Reconciliation

**Tables touched:** `mti_term_flags`, `wa_term_inventory` (read-only source)

**Rationale:**

Phase A §A.8 cross-check (fixed in this session) revealed `mti_term_flags` is severely underpopulated — 54 rows total, with only 6 somatic flags and 39 GOD_AS_SUBJECT flags, against 162 `somatic_link=1` and 208 `god_as_subject=1` rows in `wa_term_inventory`. The supposed "supersession" per CLAUDE.md §17.6 never happened at the data level.

This bundle **populates `mti_term_flags` from `wa_term_inventory`** so the flag table becomes authoritative before the boolean columns are dropped in M24.

**Changes:**

- **DBR-CHG-015** — INSERT INTO `mti_term_flags` (mti_term_id, flag_id) — for each `wa_term_inventory.somatic_link = 1` row, resolve to `mti_terms.id` via strongs_number and insert `(mti_term_id, 3)` (SOMATIC_INNER_LINK). INSERT OR IGNORE to skip existing.
- **DBR-CHG-016** — INSERT INTO `mti_term_flags` (mti_term_id, flag_id) — for each `wa_term_inventory.god_as_subject = 1` row, resolve to `mti_terms.id` and insert `(mti_term_id, 1)` (GOD_AS_SUBJECT). INSERT OR IGNORE.

**Pre-check:**

```sql
SELECT 'pre_somatic_mtf', COUNT(*) FROM mti_term_flags WHERE flag_id IN (3,4);
SELECT 'pre_god_mtf', COUNT(*) FROM mti_term_flags WHERE flag_id = 1;
SELECT 'pre_somatic_ti', COUNT(*) FROM wa_term_inventory WHERE somatic_link = 1;
SELECT 'pre_god_ti', COUNT(*) FROM wa_term_inventory WHERE god_as_subject = 1;
```

**Post-check:**

```sql
-- After migration, somatic flags should cover all unique mti_terms matching somatic_link=1
SELECT COUNT(DISTINCT mt.id) 
FROM mti_terms mt
JOIN wa_term_inventory wti ON wti.strongs_number = mt.strongs_number
WHERE wti.somatic_link = 1
  AND NOT EXISTS (SELECT 1 FROM mti_term_flags mtf WHERE mtf.mti_term_id = mt.id AND mtf.flag_id IN (3, 4));
-- Expected: 0 (or near 0 if duplicate strongs resolutions)
```

**Risk:** MEDIUM — data addition (non-destructive) but must be verified carefully before M24 can proceed.

**Reversibility:** EASY — DELETE the INSERTed rows via a matching WHERE clause.

**Data loss:** NO (additive).

**Scripts affected:**

- Phase D: `engine/flag_engine.py` may need updated read paths if it uses `mti_term_flags`
- Applicator: no change — inserts are via migration code

**RD gate:** **RD-DBR-003 (new) — confirm population strategy for dual-boolean flags.** This bundle assumes the approach is to populate `mti_term_flags` from the booleans. Alternative: retain both as equal sources, deprecate the supersession claim in CLAUDE.md §17.6.

**Migration identifier:** M23

---

### Migration Bundle M24 — Drop Reconciled Boolean Flags

**Tables touched:** `wa_term_inventory`

**Rationale:**

After M23 populates `mti_term_flags`, the boolean columns `somatic_link` and `god_as_subject` become redundant — all their data is reflected in `mti_term_flags`. Safe to drop.

**Changes:**

- **DBR-CHG-017** (`wa_term_inventory`): DROP COLUMN `somatic_link`.
- **DBR-CHG-018** (`wa_term_inventory`): DROP COLUMN `god_as_subject`.

**Pre-check:** Must verify M23 post-check succeeded with 0 rows missing before M24 can apply. This is an explicit dependency gate.

**Risk:** MEDIUM — data drop of columns with historical content.

**Reversibility:** MODERATE — data recoverable via `mti_term_flags` reconstruction + backup.

**Data loss:** YES — but reconciled with `mti_term_flags` in M23. Approval: needs explicit `[X] APPROVED — data reflected in mti_term_flags post M23`.

**Scripts affected:**

- `engine/*` — search for `somatic_link` and `god_as_subject` references; update to read via `mti_term_flags` joins
- `scripts/*` — same
- `scripts/apply_session_patch.py` — remove operations targeting these columns
- Session B readiness v1.6 — obsolete references to `somatic_link` and `god_as_subject` quality checks (Section B1); update or defer to instruction-review follow-on

**Migration identifier:** M24

**Sequencing:** After M23 post-check passes.

---

### Migration Bundle M25 — Dimension Index Simplification

**Tables touched:** `wa_dimension_index`

**Rationale:**

Phase A §A.3 identified multiple denormalised copies in `wa_dimension_index`. Deeper investigation (this session) confirmed 0 mismatches across `mti_term_id`, `group_code`, `strongs_number` vs parent tables. Clean simplification.

**Changes:**

- **DBR-CHG-019** (`wa_dimension_index`): DROP COLUMN `mti_term_id` (derivable via `verse_context_group.mti_term_id`)
- **DBR-CHG-020** (`wa_dimension_index`): DROP COLUMN `group_code` (derivable via `verse_context_group.group_code`)
- **DBR-CHG-021** (`wa_dimension_index`): DROP COLUMN `strongs_number` (derivable via `mti_terms.strongs_number`)
- **DBR-CHG-022** (`wa_dimension_index`): DROP COLUMN `transliteration` (derivable via `mti_terms.transliteration`)
- **DBR-CHG-023** (`wa_dimension_index`): DROP COLUMN `gloss` (derivable via `mti_terms.gloss`)
- **DBR-CHG-024** (`wa_dimension_index`): DROP COLUMN `language` (derivable via `mti_terms.language`)
- **DBR-CHG-025** (`wa_dimension_index`): DROP COLUMN `owning_registry_word` (derivable via `word_registry.word`)
- **DBR-CHG-026** (`wa_dimension_index`): DROP COLUMN `context_description` (derivable via `verse_context_group.context_description`)

**Retained on `wa_dimension_index`:** `id`, `verse_context_group_id` (FK), `owning_registry_no` (useful for performance filtering), `cluster_assignment`, `dimension`, `dimension_confidence`, `anchor_count`, `related_count`, `set_aside_count`, `total_verse_count`, `delete_flagged`, `manual_override`, `notes`, `last_modified`, `dominant_subject`.

**Risk:** MEDIUM — many scripts read from `wa_dimension_index`; must update all before DROP.

**Reversibility:** EASY — ADD COLUMN back + restore via joins.

**Data loss:** NO (all data derivable).

**Scripts affected:**

- `scripts/build_complete_extract.py` — reads many of these columns; update to join
- `scripts/build_dimension_extract.py` — same
- `scripts/apply_session_patch.py` — operations like `update (wa_dimension_index)` need column-list update
- Session A extract generator (new) — must use join-based query

**Migration identifier:** M25

**Sequencing:** After scripts updated in Phase D.

---

### Migration Bundle M26 — Constraint Coverage

**Tables touched:** `word_registry`, `wa_term_inventory`, `wa_dimension_index`

**Rationale:**

Phase A §A.5 identified 8 controlled-vocabulary columns without CHECK constraints. Strengthening this prevents future drift. Precondition: `RD-DBR-001` resolution (lock sentinel casing) must be done first — the CHECK on `phase1_status` depends on the canonical value set.

**Changes:**

- **DBR-CHG-027** (`word_registry.session_b_status`): ADD CHECK constraint matching controlled vocabulary per CLAUDE.md §17.1: NULL, 'Verse Context Reset', 'Ready for Analysis', 'Pre-Analysis Complete', 'Analysis Complete', 'Session B Complete'
- **DBR-CHG-028** (`word_registry.verse_context_status`): ADD CHECK matching §17.2: NULL, 'In Progress', 'Complete', 'Verse Context Reset'
- **DBR-CHG-029** (`word_registry.phase1_status`): ADD CHECK after RD-DBR-001 resolution; values: 'Complete', 'Excluded', 'In Progress' (if casing stays) OR 'IN_PROGRESS' (if casing changes)
- **DBR-CHG-030** (`word_registry.carry_forward`): ADD CHECK `carry_forward IN (0, 1)`
- **DBR-CHG-031** (`wa_term_inventory.term_owner_type`): ADD CHECK `term_owner_type IN ('OWNER', 'XREF')` — after confirming no other values exist
- **DBR-CHG-032** (`wa_term_inventory.language`): ADD CHECK `language IN ('Hebrew', 'Greek')` — after confirming no other values exist
- **DBR-CHG-033** (`wa_term_inventory.evidential_status`): ADD CHECK matching §17.4: NULL or one of ('confirmed', 'plausible', 'uncertain', 'instrumental', 'relational_only')
- **DBR-CHG-034** (`wa_dimension_index.dimension_confidence`): ADD CHECK matching observed vocabulary: NULL or one of ('CLAUDE_AI', 'RESEARCHER', 'KEYWORD_STRONG', 'KEYWORD_WEAK', 'ROOT_INFERRED', 'UNCLASSIFIED')

**Pre-check per column:** `SELECT DISTINCT {col} FROM {table}` — verify all current values are in the proposed CHECK set. Fail migration if violators exist.

**Note:** SQLite does not support ALTER TABLE ADD CHECK directly — this migration requires table rebuild (`CREATE TABLE ... AS SELECT ... + constraints; DROP + RENAME`). Established SQLite pattern; CC must use it carefully.

**Risk:** MEDIUM — table rebuilds touch data; pre-check reduces risk.

**Reversibility:** EASY — rebuild without the CHECK.

**Data loss:** NO.

**Scripts affected:** None directly — CHECK constraints are purely declarative.

**RD gate:** RD-DBR-001 must be resolved before DBR-CHG-029.

**Migration identifier:** M26

---

### Migration Bundle M27 — `schema_version` Rebuild

**Tables touched:** `schema_version`

**Rationale:**

Phase A §A.7 identified: `id` does not reflect application order; `applied_at` format is inconsistent. Per RD-DBR-002 proposal: rebuild with id reflecting chronological order; normalise date format.

**Changes:**

- **DBR-CHG-035** — CREATE TEMP TABLE `schema_version_new` with same columns; INSERT rows ordered by `applied_at` normalised to ISO-8601 UTC with T-separator.
- **DBR-CHG-036** — DROP `schema_version`; RENAME `schema_version_new` to `schema_version`.
- **DBR-CHG-037** — Post-insert: append this migration's entry with correct new-format timestamp.

**Pre-check:** `SELECT COUNT(*) FROM schema_version` — record pre-count.

**Post-check:** `SELECT COUNT(*)` equals pre + 1 (this migration's row).

**Risk:** LOW — schema_version is read for humans + engine startup; table rebuild is brief.

**Reversibility:** EASY — rebuild from backup.

**Data loss:** NO (content preserved).

**Scripts affected:** `engine/engine.py` startup check + `engine/migrate.py`  logic — may not need changes if they read by version_code.

**RD gate:** RD-DBR-002 confirms rebuild approach.

**Migration identifier:** M27

---

### Migration Bundle M28 — Index Optimisation

**Tables touched:** Various — based on Phase A §A.4 findings.

**Rationale:**

Phase A showed 86 indexes (25 auto + 61 explicit). No large tables lack indexes. Refinement rather than major change. Partial indexes on active vs deleted sets are the primary opportunity.

**Changes (candidates — finalise at C.1):**

- **DBR-CHG-038** — Add partial index on `wa_term_inventory(strongs_number)` WHERE delete_flagged = 0 (speeds live-term lookups, common in engine + scripts)
- **DBR-CHG-039** — Add partial index on `wa_verse_records(term_inv_id)` WHERE delete_flagged = 0
- **DBR-CHG-040** — Add partial index on `verse_context(group_id, is_anchor)` WHERE delete_flagged = 0 AND is_anchor = 1 (common anchor-lookup pattern)
- **DBR-CHG-041** — Drop any explicit index fully shadowed by another (analysis pending during C.1)
- **DBR-CHG-042** — Add index on `prose_section(registry_id, section_type_id)` WHERE superseded_by_id IS NULL AND delete_flagged = 0 (already in prose store design)

**Risk:** LOW — indexes are reversible; no data impact.

**Reversibility:** TRIVIAL.

**Data loss:** NO.

**Scripts affected:** None.

**Migration identifier:** M28

**Sequencing:** Last — benefits from all prior structural changes being stable.

---

## Additional Phase D Items (not migrations)

### PD.1 — Fix `LOCK_SENTINEL` constant (per RD-DBR-001)

Pending RD-DBR-001. Single-file change to `engine/constants.py`. Logged in Phase D script-update log.

### PD.2 — Correct A.8 audit-script cross-check bug

Minor. The Phase A audit script used `mf.id` on `mti_term_flags` (which has compound PK `(mti_term_id, flag_id)`, no `id` column). Not blocking — cross-checks were re-run correctly in this session.

### PD.3 — CLAUDE.md updates to reflect reality

- §17.6 "Redundant Fields" — update:
  - `god_as_subject` / `somatic_link`: clarify "partially reflected in mti_term_flags; to be reconciled in M23 then dropped in M24"
  - `inference_note`: RETAINED (was mis-flagged as pipeline-redundant; actually substantive researcher content)

---

## New RD Item Raised

### RD-DBR-003 — Strategy for boolean flag → mti_term_flags population

**Status:** OPEN — raised 2026-04-19 at Phase B

Confirms the approach in M23 → M24. Options:

- **(a)** Populate `mti_term_flags` from booleans (M23), then drop booleans (M24) — CC's recommendation. Makes `mti_term_flags` authoritative going forward.
- **(b)** Retain both as equal sources; update CLAUDE.md to reflect "dual source"; no drops.
- **(c)** Designate `wa_term_inventory.*` as canonical; deprecate `mti_term_flags`; simplify by dropping the flags table.

**CC recommendation:** (a).

Full RD item to be appended to `outputs/wa-global-databasereview-rd-v1-20260419.md` once this Change Plan is marked up.

---

## G2 Approval Block

Status: [X] APPROVED — PROCEED to Phase C  [ ] REVISIONS REQUESTED — see markup

Date: 2026-04-19

Reviewer: le Roux Cilliers

Notes: All 10 migrations reviewed and approved. All 3 RD items resolved per CC recommendations (see RD accumulator).

### Bundle-level approval

| Migration | Approval |
|---|---|
| M19 — Orphan cleanup | [X] APPROVED |
| M20 — Prose store setup | [X] APPROVED |
| M21 — Registry enrichment (word_synopsis) | [X] APPROVED |
| M22 — Obvious redundant drops | [X] APPROVED |
| M23 — MTI flag reconciliation | [X] APPROVED (RD-DBR-003 resolved: option (a) populate then drop) |
| M24 — Drop reconciled booleans | [X] APPROVED (conditional on M23 post-check PASS) |
| M25 — Dimension index simplification | [X] APPROVED |
| M26 — Constraint coverage | [X] APPROVED (RD-DBR-001 resolved: option (a) update constant to match data) |
| M27 — schema_version rebuild | [X] APPROVED (RD-DBR-002 resolved: option (a) rebuild) |
| M28 — Index optimisation | [X] APPROVED |

---

*End of Change Plan v1 — 2026-04-19*
