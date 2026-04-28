# wa-global-database-review — Design Workings (v1)

| Field | Value |
|---|---|
| Filename | wa-global-database-review-design-v1-20260419.md |
| Status | DRAFT — awaiting researcher markup. Updated 2026-04-19 PM to fold in approved prose store scope. |
| Purpose | Design workings for the DB-wide schema/FK/index review and reorganisation instruction. This runs **before** the per-word readiness sweep. Now also includes prose infrastructure (tables + routines) per researcher direction 2026-04-19. |
| Next artefacts | `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-database-review-instruction-v1_0-20260419.md` (the instruction itself) |
| Companion design doc — sweep | `outputs/investigations/wa-global-readiness-sweep-design-v1-20260419.md` — the per-word sweep that runs **after** this |
| Companion design doc — prose | `outputs/investigations/wa-prose-store-design-v1-20260419.md` — prose storage schema and round-trip tooling (folded in; researcher approved 2026-04-19) |
| Produced | 2026-04-19 |

---

## How to Review This Document

Same model as the sweep design doc. Answer Q1–Q12 inline. Strike/override PROPOSED items. Mark the Approval block at the end.

---

## 1. Requirements — My Interpretation

Pulled verbatim from your direction on 2026-04-19:

| # | Requirement | Source |
|---|---|---|
| D1 | Resolve database-wide anomalies and fixes | Direct |
| D2 | Reduce complex/unnecessary FK relationships that add joins and complexity | Direct |
| D3 | Remove redundant, unused, and conflicting columns | Direct |
| D4 | Optimise indexing if needed | Direct |
| D5 | Split this work out as a separate instruction running before the word-by-word sweep | Direct (explicit endorsement) |
| D14 | Prepare infrastructure (tables) and supporting routines for DB-canonical prose storage per Option D | Direct 2026-04-19 (follow-up) |
| D15 | `.md` edit format supports any number of sections in any order; import routes each section to the correct DB row automatically | Direct 2026-04-19 (follow-up) |

**Implicit requirements:**

| # | Implicit requirement | Derivation |
|---|---|---|
| D6 | Work via migrations (M19+), not patches | DDL operations use `engine/migrate.py`; patches are DML only |
| D7 | Full backup before each migration; rollback plan | Standard risk mitigation for schema changes |
| D8 | Read-only audit before any DDL is written | Cannot know what to change without measuring current state |
| D9 | All dependent scripts (engine, analytics, patches, exports) updated coordinated with migration | Schema breaks downstream consumers |
| D10 | `EXPECTED_SCHEMA_VERSION` bumped with each applied migration | engine/constants.py convention |
| D11 | Schema JSON export regenerated post-migration | AI project reference |
| D12 | CLAUDE.md §3 + §17 regenerated post-migration | Project reference accuracy |
| D13 | Workings logged to `.md` files, not chat; markup is the response channel | Universal project protocol |

---

## 2. Guiding Principles

**PROPOSED** — may be overridden in markup:

| Principle | Statement |
|---|---|
| Measure before change | No DDL proposed without an audit finding backing it. No speculative cleanup. |
| Single approval plan | All proposed schema changes are assembled into one Change Plan, reviewed and approved as a unit. Execution then proceeds migration by migration. |
| Migration discipline | One logical change per migration. Each migration is atomic: either fully applies or rolls back. No migration mixes unrelated changes. |
| Pre-check and post-check | Each migration has a numerical pre-check query and matching post-check query. Outcomes recorded. |
| Backup per migration | A pre-migration backup is named and retained beyond the BACKUP_RETENTION=10 default. |
| Script update first, migration second | For any column removal, every script/query that references the column is updated (or confirmed not to reference it) **before** the DROP migration runs. |
| No data loss without explicit approval | Any migration that drops data from existing rows (not just schema) requires a separate approval line in the Change Plan marked `DATA-LOSS: YES — approved by researcher`. |
| Reversibility | Every migration has a documented down-migration path, even if applying down is not routine. |
| Coordination with per-word sweep | Change Plan explicitly states which columns/tables the per-word sweep depends on; those are deferred or handled last. |

---

## 3. Proposed Phases

### Phase A — Schema Audit (read-only)

Produce a comprehensive audit report. No DDL. Output is a markdown report that drives the Change Plan.

**A.1 — Table inventory**
- All tables, row counts, size estimate, creation date, last-modified inference
- Table category (reference / registry / WA file index / WA term data / etc. per CLAUDE.md §3)

**A.2 — Column inventory per table**
- Column name, type, NULL allowed, default value, FK (if any)
- **Usage metrics per column:**
    - Rows with non-NULL value (absolute count + %)
    - Rows with default value only (indicates never-written)
    - Distinct value count (low cardinality may suggest boolean or enum waste)
- **Reference metrics per column** — grep all scripts for references:
    - Read references (SELECT)
    - Write references (INSERT/UPDATE)
    - Python scripts referencing the column
    - Patch operations referencing the column
- **Redundancy flags:**
    - Column duplicated in another table (same value)
    - Column superseded per CLAUDE.md §17.6
    - Column matching patterns: `*_note` fields, `*_flag` with boolean duplicate

**A.3 — FK graph**
- All FK relationships extracted from `create_tables.sql`
- Per FK: source table/column → target table/column, ON DELETE behavior, ON UPDATE behavior
- Graph metrics:
    - Hop count from common query starting points (e.g. `word_registry` → `wa_verse_records`)
    - FK fan-in and fan-out per table
    - Cyclic FKs (if any)
- **FK utility assessment per FK:**
    - Is referential integrity actually enforced in practice?
    - Does any query cross this FK? How often?
    - Does removing this FK simplify the most common query paths?

**A.4 — Index inventory**
- All indexes from `create_tables.sql` plus any CREATE INDEX in migrations
- Per index: table, columns, UNIQUE flag, partial (WHERE) clause
- **Usage assessment:** for each index, is there a query that benefits? (Approximate via grep of WHERE/JOIN clauses.)
- **Missing index candidates:** common query patterns that do full scans

**A.5 — Constraint inventory**
- NOT NULL constraints
- UNIQUE constraints
- CHECK constraints
- Coverage: which columns have no constraint but should

**A.6 — Orphan rows**
- For each FK: count rows whose FK target no longer exists
- For soft-delete: rows where parent is `delete_flagged=1` but child is not

**A.7 — Data type inconsistencies**
- Dates: ISO string (e.g. `'2026-04-19T10:30:00Z'`) vs INTEGER unix timestamp vs TEXT with varied formats
- Booleans: INTEGER 0/1 (programme standard) vs TEXT 'true'/'false' vs NULL-as-false
- Strong's numbers: confirm `H`/`G` prefix consistency; suffix letter casing

**A.8 — Redundant/superseded columns — known candidates confirmed**
From CLAUDE.md §17.6 — confirm usage metrics match:
- `wa_term_inventory.god_as_subject`
- `wa_term_inventory.somatic_link`
- `wa_term_inventory.status_note`
- `word_registry.inference_note`
- `mti_terms.status_note`

Plus the audit finds others via A.2.

**A.9 — Audit report output**
- `outputs/reports/wa-global-database-audit-{YYYYMMDD}.md` — full audit findings
- One section per A.1–A.8
- Each finding tagged: `INFORMATIONAL` / `CLEANUP_CANDIDATE` / `RISK` / `BROKEN_INVARIANT`

### Phase B — Change Plan

Assemble findings into a concrete change plan. Each proposed change is an item with:

| Field | Content |
|---|---|
| Change ID | `DBR-CHG-001`, `DBR-CHG-002`, ... |
| Type | DROP_COLUMN / RENAME_COLUMN / CHANGE_TYPE / ADD_INDEX / DROP_INDEX / DROP_FK / ADD_CONSTRAINT / DATA_FIX / OTHER |
| Target | table.column or FK name |
| Rationale | One paragraph: why this change |
| Current state | Concrete: row count affected, query count affected, etc. |
| Proposed state | Concrete: new schema shape |
| Data loss? | YES / NO — if YES, explicit approval line required |
| Scripts affected | List of files that reference the target; update status (UPDATE_REQUIRED / CONFIRMED_NOT_REFERENCED) |
| Migration number | M19, M20, ... (assigned in Phase C) |
| Risk | LOW / MEDIUM / HIGH with justification |
| Reversibility | EASY / MODERATE / HARD |
| Sequencing dependency | Must come before/after other DBR-CHG items |

Change Plan written to: `outputs/reports/wa-global-database-changeplan-v{n}-{YYYYMMDD}.md`.

Approved as a unit by researcher before Phase C begins.

### Phase C — Migration Development

For each approved change:

1. Author migration in `engine/migrate.py` (or split into dedicated migration file if growing large)
2. Write migration pre-check and post-check queries
3. Update `EXPECTED_SCHEMA_VERSION` in `engine/constants.py`
4. Update `data/schema/create_tables.sql` (canonical DDL) to match target state
5. Update any affected scripts identified in Phase B
6. Dry-run migration on a DB copy; confirm pre/post counts match expectations
7. Write migration entry to `outputs/reports/wa-global-database-migrations-applied-{YYYYMMDD}.md`

**Phase C scope now includes (per D14, D15) — see `wa-prose-store-design-v1-20260419.md` for full spec:**

| Mig ID | Description |
| --- | --- |
| M_P1 | `CREATE TABLE prose_section_type` + indexes |
| M_P2 | `CREATE TABLE prose_section` + indexes |
| M_P3 | `CREATE VIRTUAL TABLE prose_section_fts` (FTS5) + sync triggers |
| M_P4 | `CREATE TABLE prose_section_dimension_link` |
| M_P5 | `CREATE TABLE prose_section_finding_link` |
| M_P6 | Seed `prose_section_type` with initial catalogue (includes 6 `session_a` types per `session-a-extract-section-types-advice-v1-20260419.md`) |
| M_P7 | `ALTER TABLE word_registry ADD COLUMN word_synopsis TEXT` — researcher-authored 1–2 sentence word synopsis, rendered into Session A Summary section (per Q7 resolution 2026-04-19) |

(M_P7 — import existing prose — deferred; not in this review.)

### Phase D — Script Update Sweep

For each column/FK/constraint removed or changed, audit scripts:

- `engine/*.py` — updated where needed
- `analytics/*.py` — updated where needed
- `scripts/*.py` — updated where needed (hundreds of scripts here)
- `scripts/apply_session_patch.py` applicator — updated operation mappings
- Schema export: `scripts/export_database_schema.py` re-run
- File manifest: `scripts/build_file_manifest.py` re-run

**Phase D scope now includes (prose routines per D14, D15):**

- New script: `scripts/export_prose.py` — round-trip export
- New script: `scripts/import_prose.py` — round-trip import with marker parsing, conflict detection, dry-run, report
- New script: `scripts/render_prose.py` — publication rendering (md/docx)
- Applicator extension: `scripts/apply_session_patch.py` gains PROSE patch type + operations (`insert`, `supersede`, `delete`, `approve`, `bulk_supersede` on `prose_section`)
- Extract extension: `scripts/build_complete_extract.py` includes approved prose sections
- Test harness: `scripts/_test_prose_roundtrip.py` — verifies round-trip byte-fidelity

All changes go through a single Phase D patch-style change log; researcher approves as a unit.

### Phase E — Execution

Per migration:

1. Full DB backup named with migration number (e.g. `bible_research_pre_M19_YYYYMMDD_HHMMSS.db`) — retained beyond normal rotation
2. Run pre-check query; record count
3. Apply migration via `python -m engine.engine --migrate`
4. Run post-check query; record count
5. Run migration-specific verification (e.g. `SELECT COUNT(*) FROM X WHERE [condition]`)
6. Run smoke tests on critical scripts (one word export, one audit, one patch dry-run)
7. If any failure: halt; either roll back via backup restore or write corrective micro-migration
8. Record outcome in execution log

### Phase F — Documentation Regeneration

After all migrations applied:

1. `python scripts/export_database_schema.py` — regenerate schema JSON (now includes prose tables + FTS5)
2. `python scripts/build_file_manifest.py` — refresh manifest
3. Update CLAUDE.md §3 (schema — add Table Group 17: Prose Store), §10 (programme state), §17 (redundant fields — now removed, not just flagged)
4. Produce Schema Completion Record: `outputs/reports/wa-global-database-completion-{YYYYMMDD}.md`
5. Notify per-word sweep that it may begin

---

## 4. Proposed Artefact Set

### 4.1 Review session artefacts (programme-level)

| Artefact | Filename pattern |
|---|---|
| Review session log | `outputs/session-logs/wa-global-databasereview-sessionlog-v{n}-{YYYYMMDD}.md` |
| Review observations log | `outputs/session-logs/wa-global-databasereview-obslog-v{n}-{YYYYMMDD}.md` |
| Outstanding tasks (shared with sweep) | `outputs/wa-global-outstanding-tasks-v{n}-{YYYYMMDD}.md` |
| RESEARCHER_DECISION accumulator | `outputs/wa-global-databasereview-rd-v{n}-{YYYYMMDD}.md` |

### 4.2 Phase outputs

| Phase | Artefact | Filename |
|---|---|---|
| A — Audit | Audit report | `outputs/reports/wa-global-database-audit-{YYYYMMDD}.md` |
| B — Plan | Change plan | `outputs/reports/wa-global-database-changeplan-v{n}-{YYYYMMDD}.md` |
| C — Migration | Per-migration design note | `outputs/reports/wa-global-database-migration-M{nn}-{YYYYMMDD}.md` |
| D — Scripts | Script update log | `outputs/reports/wa-global-database-scriptupdates-{YYYYMMDD}.md` |
| E — Execution | Execution log | `outputs/reports/wa-global-database-execution-{YYYYMMDD}.md` |
| F — Closeout | Completion record | `outputs/reports/wa-global-database-completion-{YYYYMMDD}.md` |

### 4.3 Code changes produced

| Target | File |
|---|---|
| Migrations | `engine/migrate.py` — new M19+ migration functions |
| Schema version | `engine/constants.py` — `EXPECTED_SCHEMA_VERSION` bumps |
| Canonical DDL | `data/schema/create_tables.sql` — target state |
| Schema export | `data/schema/archive/database-schema-{YYYYMMDD}.json` — regenerated |
| Affected scripts | Various in `engine/`, `analytics/`, `scripts/` — updated per Phase D |

---

## 5. Approval Gates

This work has **five** explicit approval gates:

| Gate | Moment | What researcher approves |
|---|---|---|
| G1 | After Phase A | Audit report — confirms the current state is accurately described |
| G2 | After Phase B | Change Plan as a unit — proceed to migration development |
| G3 | Before each migration in Phase E | Per-migration approval (brief, standard form) |
| G4 | After Phase E | Execution outcome — all migrations applied, verification clean |
| G5 | After Phase F | Completion — ready to release sweep |

Gates G3 are the most routine — each migration is small and approved in sequence. G1, G2, G4, G5 are major gates.

---

## 6. Risk and Reversibility Matrix

For each change TYPE, pre-stated risk profile:

| Change type | Risk | Reversibility | Backup strategy |
|---|---|---|---|
| DROP_COLUMN (confirmed-unused) | LOW | EASY via ALTER ADD + restore | Pre-migration backup |
| DROP_COLUMN (historically populated) | MEDIUM | MODERATE — data lost unless backup | Pre-migration backup kept 6 months |
| RENAME_COLUMN | MEDIUM | EASY | Pre-migration backup |
| CHANGE_TYPE (e.g. TEXT → INTEGER for dates) | HIGH | MODERATE — conversion may lose precision | Pre-migration backup + post-verification |
| ADD_INDEX | LOW | TRIVIAL — just drop if wrong | None needed |
| DROP_INDEX | LOW | TRIVIAL — add back | None needed |
| DROP_FK | LOW | EASY — re-add constraint | None needed; FK does not affect data |
| ADD_FK | MEDIUM | EASY — drop constraint | Pre-migration check for violations |
| ADD_CONSTRAINT (NOT NULL, CHECK) | MEDIUM | EASY — drop constraint | Pre-migration check for violators |
| DATA_FIX (bulk UPDATE during migration) | MEDIUM-HIGH | MODERATE — data change not reversible without backup | Pre-migration backup |

---

## 7. Proposed Instruction Structure

Once this design doc is approved, the instruction will contain:

1. Header + metadata
2. Governing Rules (global rules, CC rules, patch instruction, directive instruction)
3. Change Log
4. Pipeline Position (first-in-sequence gate before sweep)
5. What to Attach at Session Start
6. Governing Disciplines (CC-specific; principle list from §2)
7. Relationship to sweep (coordination, deferred columns)
8. Phase A — Schema Audit: checklist, SQL library, output format
9. Phase B — Change Plan: format, per-change schema, sequencing rules
10. Phase C — Migration Development: conventions, pre/post checks, constants bump
11. Phase D — Script Update Sweep: grep strategy, update log format
12. Phase E — Execution: backup, apply, verify, record
13. Phase F — Documentation Regeneration
14. Approval Gate Protocol (G1–G5)
15. Rollback Protocol (per change type)
16. Fallback Protocol (interruption, partial migration, broken script)
17. Completion Record Format
18. Integrity Rules (DBR-01 onwards)
19. Appendix A — SQL library for audit queries
20. Appendix B — Migration template
21. Appendix C — Common change types

---

## 8. Known Starting Points

Some audit work can be stated confidently from current project state:

### 8.1 Known redundant columns (CLAUDE.md §17.6)

| Table | Column | Reason | Action |
|---|---|---|---|
| `wa_term_inventory` | `god_as_subject` | Superseded by `mti_term_flags` | Confirm zero writes, then DROP |
| `wa_term_inventory` | `somatic_link` | Superseded by `mti_term_flags` | Confirm zero writes, then DROP |
| `wa_term_inventory` | `status_note` | NULL across all records | Confirm, then DROP |
| `word_registry` | `inference_note` | Researcher-set only; no pipeline use | Confirm retention intent; likely KEEP as metadata field |
| `mti_terms` | `status_note` | Written by audit_word A10 only | Assess: is A10's output used? If not, DROP |

### 8.2 Suspected FK-graph complexity

Without audit, candidates to examine:

- `wa_verse_records` has both `file_id` (→ `wa_file_index`) **and** `term_inv_id` (→ `wa_term_inventory`). Is `file_id` redundant given the term's file is derivable?
- `verse_context` has `verse_record_id`, `group_id`, and `mti_term_id` — three FKs. Is one derivable from another?
- `wa_data_quality_flags` keyed by both `file_id` and `term_inv_id`. Is `file_id` needed?
- Multiple `file_id` FKs across the WA-family tables add joins. Evaluate whether parent is reachable through a shorter path.

These are SUSPICIONS — the audit will confirm or refute.

### 8.3 Index strategy — current state (inferred)

Current migrations M01–M18 add indexes ad-hoc. No holistic strategy recorded. Phase A.4 will produce an index usage audit; Phase B will propose a consolidated strategy.

### 8.4 Type inconsistency candidates

- Dates: ISO 8601 strings in most tables; confirm consistency
- Booleans: INTEGER 0/1 mostly; confirm no stray TEXT
- Strong's: check `H`/`G` prefix casing

---

## 9. Open Design Questions

Please answer each inline. My recommendation given for each.

### Q1 — Instruction filename — **RESOLVED**

**Researcher decision (2026-04-19):** Agreed. Filename: `wa-global-database-review-instruction-v1_0-20260419.md`.

---

### Q2 — Scope of audit — **RESOLVED**

**Researcher decision (2026-04-19):** All tables (matches recommendation). Reference tables, MTI tables, engine control tables all in scope.

---

### Q3 — CC designs AND applies migrations with per-migration approval — **RESOLVED**

**Researcher decision (2026-04-19):** Yes, with explicit G3 approval per migration. CC designs migrations per Change Plan; each migration has its own G3 approval before application.

<!-- previous recommendation block retained via git history -->  
 
---

### Q4 — Archive redundant scripts — **RESOLVED (override)**

**Researcher decision (2026-04-19):** **Archive all redundant scripts.** Active scripts made redundant by schema changes are **actively moved** to `archive/scripts/` during Phase D (rather than left in place). Active scripts that remain useful are updated. Scripts already in `archive/` before this review remain untouched.

**Implementation implication for instruction (Phase D):**

1. Identify scripts with heavy dependency on removed/renamed columns
2. Assess: can it be updated meaningfully, or is its purpose now gone?
3. If redundant → move to `archive/scripts/` with a one-line entry in the script-update log recording the archival reason and date
4. If still useful → update in place

<!-- previous recommendation block retained via git history -->  
 
---

### Q5 — Historical patches/instructions immutable — **RESOLVED**

**Researcher decision (2026-04-19):** No — historical patches are immutable. Instructions are not modified retrospectively for new methods; new methods live in new instruction documents. Dropped-column references in old patches remain as historical artefacts.

**Implementation implication:** No rewriting of `data/imports/WA/Patches/` or `archive/patches/`. Phase A audit flags any dropped columns referenced in those paths for awareness only (not for action).

<!-- previous recommendation block retained via git history -->  
 
---

### Q6 — Backup retention policy — **RESOLVED**

**Researcher decision (2026-04-19):** Agreed. Pre-migration backups retained **6 months minimum**, separate from rolling `BACKUP_RETENTION = 10`. Named with the migration identifier (e.g. `bible_research_pre_M19_YYYYMMDD_HHMMSS.db`). Stored in `backups/` outside rotation.

<!-- previous recommendation block retained via git history -->  
 
---

### Q7 — When does the per-word sweep start — **RESOLVED**

**Researcher decision (2026-04-19):** After all migration phases are complete. Option (a). Sweep does not begin until Phase A–F all closed and the Schema Completion Record is produced.

<!-- previous recommendation block retained via git history -->  
 
---

### Q8 — Granularity of the Change Plan — **RESOLVED (override to per-phase)**

**Researcher decision (2026-04-19):** **Per phase**, not per table. Many tables are related; a single migration may span multiple tables where the changes are semantically connected. Each migration in Phase C bundles a cohesive set of related changes.

**Implementation implication for instruction:** The Change Plan document is organised as:

```
Phase C Migration Bundle 1 — [descriptor]
  Tables touched: [t1, t2, t3]
  Rationale: [one paragraph — why these changes belong together]
  Changes:
    - DBR-CHG-001 (t1): ...
    - DBR-CHG-002 (t2): ...
    - DBR-CHG-003 (t3): ...
  Risk: [aggregated]
  Reversibility: [aggregated]

Phase C Migration Bundle 2 — [descriptor]
  ...
```

Each bundle maps to a single migration (M19, M20, ...) applied as one transaction. Individual changes remain labelled by table but are grouped by migration bundle.

<!-- previous recommendation block retained via git history -->  
 
---

### Q9 — Touch `mti_terms` — **RESOLVED**

**Researcher decision (2026-04-19):** Yes — migration takes precedence. The readiness sweep will be **adjusted afterward** to match the post-migration schema.

**Implementation implication:** `mti_terms` changes proceed under standard G3 approval. Readiness sweep design (`wa-global-readiness-sweep-design-v1`) will need a review/update pass after migrations land. Phase F documentation regeneration explicitly includes a sweep-design review task.

<!-- previous recommendation block retained via git history -->  
 
---

### Q10 — DB-access layers, and historic instructions — **RESOLVED**

**Researcher decision (2026-04-19):**

- DB-access layers (`engine/db.py`, `analytics/db_client.py`) updated first in Phase D, per recommendation (blocks cascade breakage).
- Separately: **historic instruction documents** will be reviewed and adjusted **after migration** — this is a follow-on instruction-maintenance pass, not part of the DB review itself.

**Implementation implication for instruction:**

- Phase D: DB-access layers updated ahead of other script updates
- Phase F: Schema Completion Record lists "instruction documents requiring review" as a follow-on task — that review is a separate session governed by standard instruction-update discipline (GR-REF-002 `[current]` token; no in-place edits to approved instructions; new versions produced)

<!-- previous recommendation block retained via git history -->  
 
---

### Q11 — External tool dependencies — **RESOLVED**

**Researcher decision (2026-04-19):** No external tool dependencies. Plain SQL + stdlib `sqlite3` only.

<!-- previous recommendation block retained via git history -->  
 
---

### Q12 — Coordination with 6 Analysis-Complete words — **RESOLVED (override — full reprocess)**

**Researcher decision (2026-04-19):** The 6 completed words (compassion 23, fellowship 62, forgiveness 64, grace 68, love 103, mercy 111) will **go through the same process and be reprocessed**. Not just extract regeneration — full pipeline reprocess under the new post-migration schema.

**Implementation implication — major:**

Post-migration, the 6 completed words enter the pipeline **as if fresh**:

1. Fresh data extract (new schema)
2. Session A extract (new prose-store format)
3. Readiness sweep (per-word data audit + remediation)
4. Stage 1 Analysis Readiness (v1.6) — full re-run
5. Stage 2 Analysis Output — full re-run (produces new Stage 2c chapters)
6. Session C — regenerated from new Stage 2 outputs

Session B narratives from the prior cycle are **archived, not discarded**. They become prior-version prose sections in the prose store (author tag retained; `status = 'archived'`; superseded chain optional). Historical record preserved without blocking the re-run.

`session_b_status` for the 6 words is **reset** to a re-entry state after migration (likely `Verse Context Reset` or equivalent — confirmed during Phase F). Researcher approves the reset as part of Phase F closeout.

**This is a significant commitment — surfacing it explicitly in the instruction (Phase F) and in downstream sweep scheduling.**

<!-- previous recommendation block retained via git history -->  
 
---

## 10. Proposed Integrity Rules (preview — full set in instruction)

- DBR-01: No DDL without a Change Plan item backing it.
- DBR-02: No migration runs without its G3 approval recorded in the execution log.
- DBR-03: Pre- and post-check counts required per migration; mismatch halts.
- DBR-04: Backup must exist before each migration application; missing backup halts.
- DBR-05: `EXPECTED_SCHEMA_VERSION` is bumped in the same commit as the migration code.
- DBR-06: Every DROP_COLUMN migration is preceded by script update confirming no active references.
- DBR-07: Schema completion record produced before the per-word sweep is permitted to start.
- DBR-08: Rollback procedure stated in the migration design note; tested via backup restore if MODERATE or HIGH risk.

---

## 11. Approval

**Researcher approval — all 12 questions answered 2026-04-19 (see §9):**

Status: [X] APPROVED — PROCEED  [ ] REVISIONS REQUESTED — see markup

Date: 2026-04-19
Reviewer: le Roux Cilliers
Notes: All Q1–Q12 marked RESOLVED with inline answers. Three decisions are overrides with scope impact (captured in §9 and summarised below):

- **Q4 (override)**: actively archive redundant scripts during Phase D (not leave in place)
- **Q8 (override)**: Change Plan organised per-phase (bundles of related changes across tables), not per-table
- **Q12 (override)**: the 6 Analysis-Complete words undergo full pipeline reprocess post-migration, not just extract regen

These three items are material scope expansions and will be surfaced prominently in the DB-wide review instruction.

---

*End of design workings v1 — 2026-04-19*
