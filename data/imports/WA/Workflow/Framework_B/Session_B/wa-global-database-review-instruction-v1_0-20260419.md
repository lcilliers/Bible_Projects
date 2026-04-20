# WA — Global Database Review and Reorganisation Instruction

**Framework B — Soul Word Analysis Programme  
DB-Wide Schema, FK, Index, and Column Review — migration-based reorganisation  
Version 1_0 | 20260419 | Status: Active — approved 2026-04-19 by le Roux Cilliers**

| **Document** | **Value** |
|---|---|
| Filename | wa-global-database-review-instruction-v1_0-20260419.md |
| Supersedes | (new document) |
| Companion documents | wa-global-general-rules [current] · wa-reference [current] · wa-claudecode-rules-v1_0-20260419.md · wa-patch-instruction [current] · wa-directive-instruction [current] · wa-prose-store-design-v1-20260419.md |
| Design reference | outputs/investigations/wa-global-database-review-design-v1-20260419.md |
| Produced | 2026-04-19 |
| Primary actor | Claude Code (CC) — executes phases, produces artefacts, applies migrations under approval gates |
| Researcher role | Author approvals at each gate (G1–G5); author RESEARCHER_DECISION resolutions |
| Claude AI role | Null — no analytical work in this instruction |
| Handoff to | wa-global-readiness-sweep-instruction (per-word sweep) after Phase F Schema Completion Record produced |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules [current]** (per direction 2026-04-19, global rules apply to CC as well as Claude AI). CC-specific operating rules live in **wa-claudecode-rules [current]**.

Rules stated in those files are not repeated here. Where a section references a rule, the rule ID is cited.

**CC confirms at session start** (per CC-LOAD-001):

- Global rules file loaded — state resolved version
- This instruction loaded — state resolved version
- CC rules file loaded — state resolved version
- Patch instruction loaded — state resolved version
- Directive instruction loaded — state resolved version

Do not proceed without all five confirmations recorded in the session observations log.

---

## Change Log

**v1_0 (2026-04-19):** New document. Based on researcher-approved design workings `wa-global-database-review-design-v1-20260419.md`. All 12 design questions resolved 2026-04-19; three decisions are scope overrides flagged throughout (see §7 Key Scope Decisions).

---

## 1. Pipeline Position

```text
STEP Bible → Phase 1 (registration + extraction) → audit_word
       │
       ▼
Verse Context (per word, Claude AI)
       │
       ▼
Dimension Review (per word / cluster, Claude AI)
       │
       ▼
═══════════════════════════════════════════════════════════
wa-global-database-review (THIS INSTRUCTION)
  Schema / FK / index / column / prose-store review.
  Migration-based (M19+). Phases A–F with gates G1–G5.
  One-off; rerun only if new schema issues surface.
═══════════════════════════════════════════════════════════
       │
       ▼
wa-global-readiness-sweep (per-word mechanical data audit)
       │
       ▼
Session B Stage 1 (Analysis Readiness — v1.6) — per word
       │
       ▼
Session B Stage 2 (Analysis Output) — per word
       │
       ▼
Session C → Session D
```

**Sequencing rule** (resolved 2026-04-19, Q7): The readiness sweep does not begin until Phase A–F are all complete and the Schema Completion Record is produced.

---

## 2. What to Attach at Session Start

| File | Purpose |
|---|---|
| This instruction | Phase and step reference |
| `wa-global-general-rules [current]` | Programme governance |
| `wa-claudecode-rules [current]` | CC operating rules |
| `wa-patch-instruction [current]` | Patch construction (for REPAIR/FAILURE patches if needed) |
| `wa-directive-instruction [current]` | Directive specification (not primarily used here; DDL work goes via migrations) |
| `wa-global-database-review-design-v1-20260419.md` | Resolved design decisions; overrides recorded in §9 |
| `wa-prose-store-design-v1-20260419.md` | Prose store schema design (Phase C includes M_P1–M_P6+M_P7 for prose) |
| Prior audit report (if re-running) | `outputs/reports/wa-global-database-audit-{prior-date}.md` |

No live data is attached. CC queries the live DB as needed.

---

## 3. Governing Disciplines

These disciplines apply across all phases.

**Step-by-step.** Per GR-PROC-001. Each step is completed and confirmed in the observations log before the next begins.

**Write on discovery.** Per GR-OBS-001 and CC-OBS-001. Every finding, decision, and action is written to the observations log at the moment it is determined. Nothing is accumulated in memory.

**Data authoritative.** Per GR-PROC-002 and CC-DATA-001. Work strictly from what is in the DB and the design workings. Do not import general knowledge.

**All changes through migrations.** DDL is performed via migrations in `engine/migrate.py`, never via ad-hoc SQL. Migration design notes are produced per migration; each migration has its own G3 approval.

**No DB state assumptions.** Per GR-DB-001 and CC-VERSION-001. Before any write, confirm current schema version via `SELECT version FROM schema_version`. On mismatch, halt.

**Researcher decision via file, not chat.** Per CC-RD-001. Any question requiring researcher judgement is written to an RD accumulator `.md` with options and recommendation; CC does not ask in chat.

**Skill-limit to outstanding tasks.** Per CC-SKILL-001. Tasks beyond CC's tooling or skill are recorded in `outputs/wa-global-outstanding-tasks-v{n}-{date}.md` with an explicit statement of what capability is missing.

**Session logs at every breakpoint.** Per GR-PROC-006. Resumable from any natural stopping point.

**No analytical work.** This instruction performs mechanical / schema-level work only. Any task requiring analytical judgement is surfaced as Path 3 (deferred) or Path 4 (RD).

---

## 4. Tracking Document Structure

Four persistent tracking documents are opened at Phase A start and maintained across all phases.

| Document | Filename pattern | Purpose |
|---|---|---|
| Observations log | `outputs/session-logs/wa-global-databasereview-obslog-v{n}-{YYYYMMDD}.md` | Primary working record. Written continuously per GR-OBS-001. Minor version incremented at each session boundary per GR-OBS-004 and GR-FILE-004. |
| Session log | `outputs/session-logs/wa-global-databasereview-sessionlog-v{n}-{YYYYMMDD}.md` | Produced at every natural breakpoint and session end. Handoff document; records position and resume instructions. |
| Outstanding tasks file | `outputs/wa-global-outstanding-tasks-v{n}-{YYYYMMDD}.md` | Persistent across all sessions (DB review, sweep, later). Lists tasks beyond CC's capability. |
| RESEARCHER_DECISION accumulator | `outputs/wa-global-databasereview-rd-v{n}-{YYYYMMDD}.md` | RD items raised during DB review; researcher marks up in-file. |

**Observations log structure** — create these four named sections at Phase A start, before any DB read:

```text
## Pre-Flight Record
[S0–S3 checks per §5]

## Phase Progress Record
[Step-by-step sign-off as each is completed]

## Findings
[A.1 – A.8 per step; changes per B; migrations per C; script updates per D; execution per E; closeout per F]

## Open RD Items
[Cross-reference to the RD accumulator file]
```

---

## 5. Session Start Protocol

Apply at the start of every session working on any phase of the DB review.

**Step S0 — Open or increment observations log:**

Per GR-OBS-004 and GR-FILE-004. First action of every session.

| Condition | Action |
|---|---|
| First session of DB review | Create obslog `wa-global-databasereview-obslog-v1-{YYYYMMDD}.md`. Write the four empty named sections per §4. Record `SESSION STARTED: [date]. Obslog v1 created.` |
| Resumption — prior session ended cleanly | Read current obslog filename. Increment `v[n]` to `v[n.1]`. Copy prior to new version. Record `SESSION RESUMED: [date]. Obslog v[n.1] from v[n].` |
| Resumption — prior interrupted | Same as clean. Prior version preserved as last confirmed state. |

**Step S1 — Confirm governing documents loaded (CC-LOAD-001):**

State: `Global rules wa-global-general-rules [current] loaded. DB review instruction loaded. CC rules [current] loaded. Patch instruction [current] loaded. Directive instruction [current] loaded. Design workings wa-global-database-review-design-v1-20260419.md loaded.`

Do not proceed without all six confirmations.

**Step S2 — Confirm schema version (CC-VERSION-001):**

Run: `SELECT version FROM schema_version ORDER BY applied_at DESC LIMIT 1;`

Record the result. Compare against `engine/constants.py::EXPECTED_SCHEMA_VERSION`. If mismatched: halt, produce RD item, do not proceed.

**Step S3 — Determine resume position:**

Read the Phase Progress Record in obslog. Locate the last completed step. Use the table below to determine resume point.

| Last completed step | Resume from |
|---|---|
| (none — blank progress record) | Phase A Step A.0 |
| A.0 — Pre-flight | A.1 |
| A.1–A.8 | next A substep |
| A.9 — audit report produced, G1 approved | B.1 |
| B.1–B.3 | next B substep |
| B.4 — plan approved G2 | C per first bundle |
| C per bundle — migration designed | E per that bundle |
| E per bundle — applied G3 | either next bundle's C, or D if all bundles done |
| D — script updates G4 approved | F |
| F — closeout | **DB review complete; sweep may start** |

**Step S4 — Record resumption:**

```text
SESSION RESUMED: [date and time]
  Obslog version: [wa-...-v{n}-YYYYMMDD.md]
  Schema version at resume: [value]
  Resuming from: [phase/step]
  Open RD items: [n — RD-IDs]
  Open outstanding tasks count: [n]
```

---

## 6. Session Close Protocol

**Step C1 — Complete current step or reach a clean stopping point:**

Do not end mid-step if avoidable. If interrupted, record exact position: which item was being processed, what was determined, what remains.

**Step C2 — Verify obslog is current:**

Confirm all four sections reflect state:

- Phase Progress Record: last completed step signed off
- Findings: all discoveries this session recorded
- Open RD Items: accurate
- Pre-Flight Record: current if anything changed

**Step C3 — Produce session log:**

Per GR-PROC-006. Record:

- Obslog version at close (exact filename)
- Phases/steps worked this session
- Open RD items by ID
- Open outstanding tasks count
- Exact resume instructions

**Step C4 — Save obslog with version increment and deliver:**

Per GR-OBS-004, GR-FILE-004, GR-PASS-001.

Before delivery:

1. Write `SESSION CLOSED: [date and time]` record to obslog
2. Save obslog under current versioned filename (do not overwrite)
3. Session log states obslog filename and version
4. Make both files available per GR-PASS-001

Record:

```text
SESSION CLOSED: [date and time]
  Obslog version at close: [filename]
  Last completed step: [identifier]
  Session log produced: [filename]
  Outstanding tasks updated: [yes/no — count delta if yes]
  RD items raised this session: [n]
  Next session: resume from [step]; increment obslog to v[n.1] at start
```

---

## 7. Key Scope Decisions (from Design §9 resolutions)

Three 2026-04-19 researcher decisions expand the default scope. Highlighted here because they govern Phase content below.

### 7.1 Q4 — Actively archive redundant scripts (Phase D)

Scripts made redundant by schema changes are **moved to `archive/scripts/`** during Phase D, not left in place. A script-update log records each archival with reason and date. See Phase D Step D.5.

### 7.2 Q8 — Change Plan organised per-phase (Phase B)

Change Plan bundles related changes across multiple tables into single migrations. Each migration bundle covers a cohesive set of related changes. See Phase B Step B.1 and the template in Appendix B.

### 7.3 Q12 — 6 Analysis-Complete words undergo full reprocess (Phase F)

Post-migration, the six completed words (compassion 23, fellowship 62, forgiveness 64, grace 68, love 103, mercy 111) enter the pipeline **as if fresh**: fresh extract → Session A → readiness sweep → Stage 1 → Stage 2 → Session C regen. Prior Session B narratives are archived in the prose store (`status='archived'`), not discarded. `session_b_status` is reset to a re-entry state. See Phase F Step F.6.

### 7.4 Supplementary decisions

- **Q5**: Historical patches and instructions are immutable. No retrospective rewriting.
- **Q9**: Migration takes precedence over sweep concerns. Readiness sweep design will be reviewed/updated in Phase F after migrations land.
- **Q10**: DB-access layers updated first in Phase D (standard). Historic instruction documents reviewed/updated as a follow-on session after Phase F (not part of this instruction).

---

## 8. Phase A — Schema Audit (read-only)

**Gate on exit:** G1 — researcher approves audit report.

**Output artefact:** `outputs/reports/wa-global-database-audit-{YYYYMMDD}.md`

### Step A.0 — Pre-Flight

1. Confirm schema version matches `EXPECTED_SCHEMA_VERSION` (per S2)
2. Confirm applicator (`scripts/apply_session_patch.py`) version is current
3. Confirm no active locks on registries (`word_run_state.phase1_status = 'IN_PROGRESS'` or equivalent)
4. Take a baseline backup: `backups/bible_research_pre_DBR_{YYYYMMDD}_{HHMMSS}.db` — retained beyond rolling rotation (per Q6)
5. Record: `Pre-flight PASS. Baseline backup: [path].`

### Step A.1 — Table Inventory

Query:

```sql
SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name;
```

For each table record: name, row count, size estimate, category (per CLAUDE.md §3 table groups).

Output row count:

```sql
SELECT 'table_name' AS tbl, COUNT(*) AS n FROM table_name;
```

Record in obslog Findings section: `A.1 complete. [n] tables inventoried. Categories: [list with counts].`

### Step A.2 — Column Inventory and Usage Metrics

For each table (in alphabetical order), for each column:

**Metadata:**

```sql
PRAGMA table_info(table_name);
```

Record: column name, type, NOT NULL, default, PRIMARY KEY flag.

**Usage metrics:**

```sql
-- Rows with non-NULL value
SELECT COUNT(*) AS non_null FROM table_name WHERE column_name IS NOT NULL;

-- Rows with default value (if applicable)
SELECT COUNT(*) AS at_default FROM table_name WHERE column_name = <default_value>;

-- Distinct cardinality
SELECT COUNT(DISTINCT column_name) AS distinct_vals FROM table_name;

-- For boolean-like columns
SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;
```

**Reference metrics** — for each column, grep the code corpus:

```text
rg -l "\bcolumn_name\b" engine/ analytics/ scripts/
```

Record for each column: number of files referencing; summary of read vs write usage.

**Redundancy flags:**

- Column matches a known redundant column per CLAUDE.md §17.6
- Column duplicates data in another table
- Column is `*_note` with NULL across all rows
- Column has single distinct value across all rows

Record in audit report: `A.2 complete. [n] columns inventoried. [n] non-NULL anywhere. [n] flagged as CLEANUP_CANDIDATE.`

### Step A.3 — FK Graph

Extract FK definitions from `data/schema/create_tables.sql` and `sqlite_master`:

```sql
SELECT sql FROM sqlite_master WHERE type='table';
-- parse REFERENCES clauses from the DDL
```

Also run:

```sql
PRAGMA foreign_key_list(table_name);
```

For each FK record: source, target, ON DELETE, ON UPDATE behaviour.

**Graph metrics:**

- FK fan-in per table (incoming refs)
- FK fan-out per table (outgoing refs)
- Hop count from `word_registry` to each major table along most common paths
- Cyclic FKs (if any)

**Utility assessment per FK:**

- Is referential integrity actually enforced in current workflow?
- Does any query cross this FK? (grep JOIN clauses)
- Would removing this FK simplify common paths?

Record: `A.3 complete. [n] FKs identified. Common query paths: [list with hop counts]. FKs flagged for review: [n].`

### Step A.4 — Index Inventory

```sql
SELECT name, tbl_name, sql FROM sqlite_master WHERE type='index' ORDER BY tbl_name, name;
```

For each index: table, columns, UNIQUE flag, partial WHERE clause.

**Usage assessment:** for each index, grep WHERE/JOIN clauses to find likely consumers.

**Missing index candidates:** identify common query patterns that do full scans:

- Any JOIN on non-indexed FK
- Any WHERE on a selective column without an index

Record: `A.4 complete. [n] indexes. [n] in active use. [n] candidates for removal. [n] candidates for addition.`

### Step A.5 — Constraint Inventory

From DDL parsing:

- NOT NULL: count per table
- UNIQUE: list
- CHECK: list

**Coverage gaps:** columns where a constraint appears justified but absent (e.g. status fields with controlled vocabulary but no CHECK).

Record: `A.5 complete. [n] NOT NULL, [n] UNIQUE, [n] CHECK. Constraint gaps: [list].`

### Step A.6 — Orphan Rows

For each FK:

```sql
SELECT COUNT(*) AS orphans
FROM child_table c
LEFT JOIN parent_table p ON c.fk_column = p.id
WHERE p.id IS NULL;
```

For soft-deleted parents:

```sql
SELECT COUNT(*) AS deleted_parent_live_child
FROM child_table c
JOIN parent_table p ON c.fk_column = p.id
WHERE p.delete_flagged = 1 AND c.delete_flagged = 0;
```

Record counts per FK. Orphans > 0 → candidate for BROKEN_INVARIANT.

### Step A.7 — Type Inconsistencies

Check:

- Date columns: ISO string vs INTEGER unix timestamp vs other
- Boolean columns: INTEGER 0/1 (programme standard) vs other
- Strong's numbers: `H`/`G` prefix casing consistent

Record inconsistencies.

### Step A.8 — Redundant Column Confirmation

Confirm the known candidates from CLAUDE.md §17.6 and from Step A.2 redundancy flags:

- `wa_term_inventory.god_as_subject` — cross-check vs `mti_term_flags`
- `wa_term_inventory.somatic_link` — cross-check vs `mti_term_flags`
- `wa_term_inventory.status_note` — confirm NULL across all rows
- `word_registry.inference_note` — confirm not pipeline-written
- `mti_terms.status_note` — confirm limited usage

Plus any additional candidates surfaced in A.2.

For each: concrete evidence of redundancy or explicit retention reason.

### Step A.9 — Audit Report and G1

Produce `outputs/reports/wa-global-database-audit-{YYYYMMDD}.md` containing:

- §A.1 table inventory
- §A.2 column inventory with usage metrics
- §A.3 FK graph with utility assessment
- §A.4 index inventory
- §A.5 constraint inventory
- §A.6 orphan rows
- §A.7 type inconsistencies
- §A.8 redundant column confirmations
- §Summary: findings tagged INFORMATIONAL / CLEANUP_CANDIDATE / RISK / BROKEN_INVARIANT
- §G1 Approval block

**G1 gate:** researcher marks `APPROVED` on the audit report. Without G1, Phase B does not begin.

Record: `A.9 complete. Audit report: [path]. G1: awaiting researcher approval.`

Upon G1 approval:

- Record `G1 approval received: [date]. Proceeding to Phase B.` in obslog
- Begin Phase B

---

## 9. Phase B — Change Plan (per-phase bundles)

**Gate on exit:** G2 — researcher approves Change Plan as a unit.

**Output artefact:** `outputs/reports/wa-global-database-changeplan-v{n}-{YYYYMMDD}.md`

### Step B.1 — Group Audit Findings into Migration Bundles

Per Q8 override: organise the plan as **per-phase migration bundles**, each bundle covering a cohesive set of related changes across one or more tables.

**Grouping principle:**

A bundle contains changes that:

1. Should succeed or fail together (atomic transaction)
2. Share a rationale (e.g. "remove redundant term-level boolean fields superseded by mti_term_flags")
3. Would break the DB if split (e.g. DROP FK + DROP referenced column + DROP index on FK)

**Typical bundle categories:**

| Bundle category | Example contents |
|---|---|
| Prose store setup | M_P1–M_P6 per prose store design; new tables + FTS + links + seed |
| Redundant column removal — Terms | DROP `wa_term_inventory.god_as_subject`, `somatic_link`, `status_note` (superseded by mti_term_flags) |
| Redundant column removal — Registry | DROP `word_registry.inference_note` (never pipeline-written) |
| New registry field | ADD `word_registry.word_synopsis TEXT` (per Session A advice Q7) |
| FK simplification | Where audit identifies a redundant FK that adds join complexity |
| Index optimisation | ADD missing indexes, DROP unused, CREATE covering |
| Type normalisation | Where date / boolean inconsistencies warrant column-type ALTERs |
| Constraint strengthening | ADD NOT NULL or CHECK where audit shows unanimous compliance |

### Step B.2 — Per Bundle Format

Each bundle is documented with:

```text
### Migration Bundle M_XX — [descriptor]

**Tables touched:** [t1, t2, t3]

**Rationale:**
[one paragraph — why these changes belong together]

**Changes:**
- DBR-CHG-001 (t1.col): [action] — [brief justification; audit finding reference]
- DBR-CHG-002 (t2.col): [action] — [...]
- DBR-CHG-003 (t3): [action] — [...]

**Risk:** [LOW / MEDIUM / HIGH] — [brief rationale]

**Reversibility:** [EASY / MODERATE / HARD]

**Data loss:** [NO / YES — approved: ___]

**Scripts affected:** [list with status UPDATE_REQUIRED / CONFIRMED_NOT_REFERENCED / CANDIDATE_FOR_ARCHIVE]

**Sequencing dependency:** [must come before/after bundle M_YY — reason]

**Migration identifier:** M[N]

**G3 approval reference:** [to be filled at Phase E]
```

### Step B.3 — Sequence Bundles

Order bundles so that:

1. New tables (prose store) come before any migration that would reference them
2. Additive changes (ADD COLUMN, ADD INDEX) before destructive (DROP COLUMN, DROP FK)
3. Constraint strengthening (ADD NOT NULL) after related data cleanup
4. Type normalisation late (requires stable column presence)

### Step B.4 — Change Plan Document and G2

Assemble bundles into the Change Plan:

```text
# DB-Wide Change Plan — v{n} — {date}

## Summary
Total bundles: N
Migrations: M19 – M{19+N-1}
Tables touched across plan: [list]
Total DBR-CHG items: X
Risk aggregate: [LOW: n · MEDIUM: n · HIGH: n]

## Bundle Index
- M19 — [descriptor]
- M20 — [descriptor]
- ...

## Bundles (in migration order)
[each bundle per B.2 format]

## G2 Approval
[ ] APPROVED — PROCEED to Phase C
[ ] REVISIONS REQUESTED — see markup
Date: ___
Reviewer: le Roux Cilliers
```

**G2 gate:** researcher marks `APPROVED` on the Change Plan as a unit (not per bundle — that's G3). Without G2, Phase C does not begin.

Record: `B.4 complete. Change Plan: [path]. G2: awaiting researcher approval.`

---

## 10. Phase C — Migration Development

**Gate per migration:** G3 — researcher approves each migration before application.

**Output artefacts per migration:**

- Migration code in `engine/migrate.py` (new M{N} function)
- Migration design note: `outputs/reports/wa-global-database-migration-M{NN}-{YYYYMMDD}.md`
- Updated `data/schema/create_tables.sql`
- Updated `engine/constants.py::EXPECTED_SCHEMA_VERSION`

### Step C.1 — Author Migration Code

Per approved bundle:

1. Add a function `migration_M{N}(conn)` to `engine/migrate.py`
2. Migration must be idempotent-safe: check pre-state before applying; abort cleanly if pre-state not as expected
3. All DDL wrapped in a single transaction per migration
4. `schema_version` table row inserted on success: `INSERT INTO schema_version (version, applied_at, description) VALUES (?, ?, ?)`

### Step C.2 — Pre-Check and Post-Check Queries

For each migration, write:

**Pre-check:** confirms the migration is applicable — counts or state that must be true before applying.

```sql
-- Example: confirm column exists before dropping
SELECT COUNT(*) FROM pragma_table_info('table') WHERE name='column';
-- Expected: 1
```

**Post-check:** confirms the migration succeeded.

```sql
-- Example: confirm column gone
SELECT COUNT(*) FROM pragma_table_info('table') WHERE name='column';
-- Expected: 0
```

Record the expected values in the migration design note.

### Step C.3 — Bump EXPECTED_SCHEMA_VERSION

In `engine/constants.py`:

```python
EXPECTED_SCHEMA_VERSION = "3.10.0"  # bumped per migration M19
```

Version increment rule: major.minor.patch — bump `minor` per DB-wide review; bump `patch` only for hotfixes.

### Step C.4 — Update Canonical DDL

Edit `data/schema/create_tables.sql` to reflect the target state of this migration.

**Rule:** `create_tables.sql` always represents the **final state** (post all applied migrations). After each migration, it is updated synchronously.

### Step C.5 — Dry-Run on DB Copy

1. Copy live DB to `backups/dryrun/bible_research_dryrun_M{N}_{YYYYMMDD}.db`
2. Apply the migration to the copy via `python -m engine.engine --migrate --dry-run --db=backups/dryrun/...`
3. Run pre-check, expected to match
4. Run post-check, expected to match
5. Run a small smoke test: one word export, one audit report, one patch dry-run against the modified copy

If any step fails: fix the migration code; re-dry-run. Do not proceed to Step C.6 until dry-run clean.

### Step C.6 — Migration Design Note

Produce `outputs/reports/wa-global-database-migration-M{NN}-{YYYYMMDD}.md`:

```text
# Migration M{N} — [descriptor]

## Bundle reference
Change Plan bundle: M{N}
Tables touched: [t1, t2, t3]
DBR-CHG items included: [list]

## Pre-check
[SQL + expected value]

## Post-check
[SQL + expected value]

## Dry-run outcome
[pass/fail summary + smoke test results]

## Rollback procedure
[Description — use pre-migration backup if anything worse than MODERATE risk]

## Script update list (feeds Phase D)
[scripts/files requiring update or archive]

## Risk and data loss
Risk: [LOW/MEDIUM/HIGH]
Data loss: [NO / YES — approved by researcher in Change Plan]

## G3 approval
[ ] APPROVED — proceed to Phase E for this migration
Date: ___
Notes: ___
```

**G3 gate:** researcher marks `APPROVED` per migration. Without G3, that migration does not advance to Phase E execution. Multiple migrations may wait for G3 simultaneously; Phase D script updates proceed in parallel.

Record: `C.6 complete for M{N}. Design note: [path]. G3: awaiting researcher approval.`

### Step C — Repeat for each bundle

Repeat C.1–C.6 for every bundle in the Change Plan before proceeding to Phase D.

---

## 11. Phase D — Script Update Sweep

**Gate on exit:** G4 — researcher approves Phase D change log.

**Output artefact:** `outputs/reports/wa-global-database-scriptupdates-{YYYYMMDD}.md`

### Step D.1 — Update DB-Access Layers First

Priority per Q10 resolution. These are the choke point; fixing them first prevents cascade breakage.

Files:

- `engine/db.py` — connection factory, query helpers, whitelists
- `analytics/db_client.py` — SQLite connection, JSON import/export, table whitelist

For each: search for references to columns/FKs/constraints changed in Phase C. Update:

- Table whitelists (if columns dropped)
- Query helpers (if joins change)
- Type coercion (if types change)

Test after update: instantiate a connection, run a trivial query against live DB, verify no errors.

### Step D.2 — Update Engine Scripts

Files:

- `engine/audit_word.py`
- `engine/gap_fill.py` (superseded, but retained for reference — update if non-trivial dependency)
- `engine/new_word.py` (superseded, but retained — same)
- `engine/flag_engine.py`
- `engine/meaning_parser.py`
- `engine/register.py`
- `engine/report.py`
- `engine/audit.py`
- `engine/run_log.py`
- `engine/span_filter.py`
- `engine/backup.py` — update if backup schema changes

For each: grep for changed columns/FKs; update; run a smoke test.

### Step D.3 — Update Analytics Scripts

Files:

- `analytics/bible_analytics.py`
- `analytics/step_client.py` (probably no change — external API)
- `analytics/word_export.py`
- `analytics/zotero_client.py` (probably no change)

### Step D.4 — Update Scripts Directory

Files in `scripts/`. Many; expect to grep and update incrementally.

**Approach:**

1. Grep `scripts/**/*.py` for each changed column name
2. For each hit: assess update vs archive (see D.5)
3. Update in place if script is still useful
4. Log every update in the script update log

Key scripts likely to need updates:

- `scripts/apply_session_patch.py` — gain new operations (PROSE type, Session A replace; see D.6)
- `scripts/build_complete_extract.py` — include prose sections
- `scripts/build_correlation_extract.py` — check for dropped column refs
- `scripts/build_dimension_extract.py`
- `scripts/_produce_final_extract.py`
- `scripts/_generate_programme_report.py`
- `scripts/_exploratory_sessionb_export_v1_20260415.py`
- `scripts/export_database_schema.py` — re-run after migrations to regenerate schema JSON
- `scripts/build_file_manifest.py` — no code change but re-run
- `scripts/generate_registry_overview.py`

### Step D.5 — Archive Redundant Scripts (per Q4 override)

For each active script referencing dropped columns/features that cannot be meaningfully updated:

1. Move to `archive/scripts/`
2. Record in script update log:

```text
ARCHIVED: scripts/{name}.py → archive/scripts/{name}.py
Date: {YYYYMMDD}
Reason: [specific reason — e.g., "script purpose was to inspect wa_term_inventory.god_as_subject which is being dropped; mti_term_flags now authoritative"]
```

**Decision rule:**

- Script is the only consumer of a feature being removed → archive
- Script's logic is now covered by another active script → archive
- Script still useful with update → update, do not archive
- Script is already in `archive/` → leave alone (per Q4 clarification)

### Step D.6 — Update Applicator for New Operations

`scripts/apply_session_patch.py` gains per prose store design and per researcher decisions:

| Operation | Applied to | Purpose |
|---|---|---|
| `insert` on `prose_section` | new section row | standard |
| `supersede` on `prose_section` | replace current row with new version for narrative prose | per prose store §3.2 |
| `delete` on `prose_section` | soft-delete | standard |
| `approve` on `prose_section` | status transition + approval metadata | standard |
| `bulk_supersede` on `prose_section` | programme-wide edits | per prose store §7.4 |
| `session_a_replace` on `prose_section` | **in-place UPDATE** for Session A mechanical extracts | per Session A advice Q5 (immutability exception) |
| `insert` on `prose_section_type` | new section type | standard |
| `insert` on `prose_section_dimension_link` / `prose_section_finding_link` | link population | per Session A advice Q6 |
| `update` on `wa_session_research_flags` | per applicator gap close | per CLAUDE.md open loop §3.3.1 |
| `insert` on `wa_dimension_index` | per applicator gap close | per CLAUDE.md open loop §3.3.2 |
| `SDPOINTERS` patch type | per applicator gap close | per CLAUDE.md open loop §3.3.3 |

Also close the three open applicator gaps from CLAUDE.md (known at the start of this review).

### Step D.7 — Update Schema Export + Manifest

After all migrations designed (but before execution starts):

1. `python scripts/export_database_schema.py` — note this will be re-run after execution too
2. `python scripts/build_file_manifest.py` — refresh manifest including any scripts archived

### Step D.8 — Phase D Change Log and G4

Produce `outputs/reports/wa-global-database-scriptupdates-{YYYYMMDD}.md`:

```text
# Phase D Script Update Log — {date}

## Summary
Files updated: N
Files archived: M
Applicator operations added: K

## Updated files
| File | Changes | Rationale |
|---|---|---|
| engine/db.py | Table whitelist; helper for new FK | M19, M20 |
| ... | ... | ... |

## Archived files (per Q4)
| Source | Destination | Reason | Date |
|---|---|---|---|
| scripts/{name}.py | archive/scripts/{name}.py | ... | ... |
| ... | ... | ... | ... |

## Applicator operation additions
[list with test references]

## Smoke tests
[list of smoke tests run and outcomes]

## G4 Approval
[ ] APPROVED — proceed to Phase E execution
Date: ___
```

**G4 gate:** researcher marks `APPROVED`. Without G4, Phase E does not begin.

Record: `D.8 complete. Script updates: [path]. G4: awaiting researcher approval.`

---

## 12. Phase E — Execution

**Gate per migration:** G3 already received in Phase C; Phase E enforces G3 at application time.

**Output artefact:** `outputs/reports/wa-global-database-execution-{YYYYMMDD}.md`

### Step E — Per Migration

For each migration M{N} in Change Plan order:

**E.1 — Confirm G3 approval on file:**

Read the migration design note. Confirm approval block marked APPROVED. If not: halt that migration; proceed with the next if it is independent; otherwise halt Phase E.

**E.2 — Take pre-migration backup:**

```bash
python -m engine.engine --backup --label="pre_M{N}_{YYYYMMDD}_{HHMMSS}"
```

Retained per Q6 — 6 months minimum, outside rolling rotation. Named `bible_research_pre_M{N}_{YYYYMMDD}_{HHMMSS}.db`.

**E.3 — Run pre-check:**

Execute the pre-check SQL from the migration design note. Confirm value matches expected. If not: halt; do not apply.

**E.4 — Apply migration:**

```bash
python -m engine.engine --migrate
```

Migration code from Phase C; migrate.py picks up the new M{N} function; applies in a transaction. On success, `schema_version` row inserted.

**E.5 — Run post-check:**

Execute the post-check SQL. Confirm value matches expected. If not: halt; consult rollback protocol (§15).

**E.6 — Run migration-specific verification:**

Per migration design note. Typically:

- Row count checks on affected tables (before vs after — expect match unless migration alters data)
- Spot-check: open a known-good registry's data; confirm queries still work
- For prose migrations: confirm FTS5 triggers fire correctly (INSERT a test row, query the FTS index, verify match)

**E.7 — Smoke tests:**

- `python -m engine.engine --db-status` — confirms schema version reflects the new migration
- `python -m engine.engine --report --registry=68` — one word report runs cleanly
- `python scripts/build_complete_extract.py --registry=68 --complete-only` — extract runs cleanly
- `python scripts/apply_session_patch.py --help` — applicator starts cleanly (no import errors)

**E.8 — Record outcome:**

```text
MIGRATION M{N} APPLIED: {date and time}
Pre-check: PASS
Post-check: PASS
Verification: PASS
Smoke tests: PASS
schema_version now: X.Y.Z
Backup: {filename}
```

Append to execution log.

**E.9 — On any failure:**

1. Halt immediately — do not proceed to next migration
2. Produce RD item: `RD-DBR-{seq}: Migration M{N} failed at step E.{n}. Details: [...]. Options: [rollback via backup restore; produce corrective patch; manual investigation].`
3. Await researcher response before acting
4. If rollback: restore `backups/bible_research_pre_M{N}_{YYYYMMDD}_{HHMMSS}.db` to live; record rollback in obslog; update schema_version

### Step E.final — Phase E Complete Record

When all migrations applied cleanly:

```text
PHASE E COMPLETE: {date}
Migrations applied: M19, M20, ..., M{N}
Final schema version: X.Y.Z
All post-checks PASS
All smoke tests PASS
Pre-migration backups retained: [list of paths]
```

Proceed to Phase F.

---

## 13. Phase F — Documentation Regeneration and Reprocess Triggers

**Gate on exit:** G5 — researcher approves Schema Completion Record; DB review is closed; sweep may begin.

**Output artefact:** `outputs/reports/wa-global-database-completion-{YYYYMMDD}.md`

### Step F.1 — Regenerate schema JSON

```bash
python scripts/export_database_schema.py
```

Output: `data/schema/archive/database-schema-{YYYYMMDD}.json` + update canonical location per existing convention.

### Step F.2 — Rebuild file manifest

```bash
python scripts/build_file_manifest.py
```

Reflects archived scripts from Phase D.

### Step F.3 — Update CLAUDE.md

Per Phase A–E outcomes:

- §3 — schema table groups (reflect prose store additions; reflect dropped columns; note new columns like `word_synopsis`)
- §10 — programme state (post-migration version, schema version)
- §15 — patch system reference (new PROSE patch type, new operations)
- §17 — redundant fields (move from "do not write" to "removed in M{N}" or delete entry entirely)

Commit CLAUDE.md update alongside the migration commits.

### Step F.4 — Readiness Sweep Design Review (per Q9)

Open `outputs/investigations/wa-global-readiness-sweep-design-v1-20260419.md`. Review each phase (R.A–R.L) against the new schema:

- Are any referenced columns now dropped?
- Are any referenced tables restructured?
- Does the resolution classification still fit?

Record findings as an appendix to the Schema Completion Record: `Sweep design items requiring update: [list]`.

The actual sweep design update is a separate session (outside this instruction), but this task lists what needs updating.

### Step F.5 — List Instruction Documents Requiring Review (per Q10)

Historic instructions likely needing post-migration review:

- `wa-claudecode-instruction [current]` — CC responsibilities may have shifted (new PROSE operations, new session_a_replace)
- `wa-patch-instruction [current]` — new patch type, new operations
- `wa-sessionb-analysis-readiness [current]` — if columns referenced by v1.6 Step 1.2 checks were dropped
- `wa-registry-management-guide [current]` — if `word_registry` schema changed (e.g. new `word_synopsis` column)
- `wa-reference [current]` — schema reference section

Record as an appendix to the Schema Completion Record. Actual review is a separate session (follow-on).

### Step F.6 — Reset the 6 Analysis-Complete Words (per Q12 override)

For each of the six completed words (compassion 23, fellowship 62, forgiveness 64, grace 68, love 103, mercy 111):

**F.6a — Archive prior Session B narratives in prose store (if prose store is populated yet):**

If prose store migrations M_P1–M_P6 are applied and historical import has been done for these words:

```sql
UPDATE prose_section
SET status = 'archived'
WHERE registry_id IN (SELECT id FROM word_registry WHERE no IN (23, 62, 64, 68, 103, 111))
  AND source_stage IN ('session_b', 'session_c')
  AND status = 'approved'
  AND delete_flagged = 0;
```

If prose store is populated but not yet imported with historical narratives: skip this sub-step — historical content remains only in the .md files on disk per the "new work only" default.

**F.6b — Reset session_b_status:**

```sql
UPDATE word_registry
SET session_b_status = 'Verse Context Reset'
WHERE no IN (23, 62, 64, 68, 103, 111);
```

Note: 'Verse Context Reset' is an existing status value per CLAUDE.md §17.1 controlled vocabulary. Confirms the word re-enters the pipeline through Verse Context → Dimension Review → Stage 1 → Stage 2.

**F.6c — Produce reprocess trigger note:**

Append to the Schema Completion Record:

```text
## 6-Word Reprocess Trigger (per Q12)

The following six registries have been reset to enter the full pipeline as if fresh:

| no | word | prior session_b_status | new session_b_status |
|---|---|---|---|
| 23 | compassion | Analysis Complete | Verse Context Reset |
| 62 | fellowship | Analysis Complete | Verse Context Reset |
| 64 | forgiveness | Analysis Complete | Verse Context Reset |
| 68 | grace | Analysis Complete | Verse Context Reset |
| 103 | love | Analysis Complete | Verse Context Reset |
| 111 | mercy | Analysis Complete | Verse Context Reset |

Prior Session B narratives (where stored in prose store): archived via status='archived'; rows retained for history.
Prior .md analytical outputs in outputs/markdown/ and data/imports/WA/Session_B_Analysis/: untouched — historical artefacts.

Once the readiness sweep runs and these six words' data reach the usual hard gates, they proceed through Stage 1 → Stage 2 producing new analytical output under the post-migration schema.
```

### Step F.7 — Schema Completion Record and G5

Produce `outputs/reports/wa-global-database-completion-{YYYYMMDD}.md`:

```text
# DB-Wide Review — Schema Completion Record — {date}

## Summary
Schema version before: X.Y.Z
Schema version after: X'.Y'.Z'
Migrations applied: M19 – M{N}
Tables added: [list]
Tables modified: [list]
Columns dropped: [list]
Columns added: [list]
Indexes added / removed: [summary]
FKs changed: [summary]

## Migrations executed
[Table: M-id, descriptor, applied_at, schema_version_after]

## Phase D — script updates
Updated: N files
Archived: M files (per Q4)
Applicator operations added: K

## Phase F — regeneration and triggers
Schema JSON: [path]
File manifest: refreshed
CLAUDE.md: updated

## Sweep design items requiring update (per Q9)
[list]

## Instruction documents requiring review (per Q10)
[list]

## 6-word reprocess trigger (per Q12)
[Six registries reset; see F.6 detail]

## Outstanding tasks appended (this session)
[list from outstanding tasks file delta]

## G5 Approval
[ ] APPROVED — DB review complete; readiness sweep may begin
Date: ___
Reviewer: le Roux Cilliers
Notes: ___
```

**G5 gate:** researcher marks `APPROVED`. Without G5, the DB review is not formally closed and the sweep does not start.

Record: `F.7 complete. Schema Completion Record: [path]. G5: awaiting researcher approval.`

Upon G5 approval:

- DB review is complete
- Readiness sweep may begin when scheduled (separate instruction)
- Session B/C/D instruction update pass may begin (separate session)

---

## 14. Approval Gate Protocol (Summary)

Five gates govern progression:

| Gate | Follows | What researcher approves | Blocking effect |
|---|---|---|---|
| G1 | Phase A | Audit report accurately describes current state | Phase B blocked |
| G2 | Phase B | Change Plan as a unit; proceed to migration development | Phase C blocked |
| G3 | Phase C (per migration) | Each migration individually; proceed to apply | Phase E blocked for that migration |
| G4 | Phase D | Phase D script update log | Phase E final-commit blocked (but per-migration E.1-E.8 may proceed for migrations G3-approved before G4) |
| G5 | Phase F | Schema Completion Record; DB review closes | Sweep start blocked |

**Approval recording convention:**

Researcher writes `APPROVED: [initials] [date]` on the approval block of the relevant artefact file. CC polls the artefact file; does not proceed until the line is present.

**Rejection convention:**

Researcher writes `REJECT: [reason]` on the approval block. CC halts work on that gate; produces RD item for resolution.

---

## 15. Rollback Protocol

Applied when a migration fails in Phase E or a problem is discovered post-application.

**Per change type, rollback approach:**

| Change type | Rollback |
|---|---|
| ADD_COLUMN | Migration was additive — rollback = ALTER TABLE DROP COLUMN (SQLite 3.35+); OR restore backup |
| DROP_COLUMN | Column data is gone — **restore backup is the only full rollback** |
| RENAME_COLUMN | ALTER TABLE RENAME; or restore backup |
| CHANGE_TYPE | Usually a CREATE+COPY+DROP+RENAME sequence — rollback requires restore backup |
| ADD_INDEX | DROP INDEX |
| DROP_INDEX | CREATE INDEX from DDL |
| ADD_FK | Not directly supported in SQLite — typically table rebuild; rollback = restore backup |
| DROP_FK | Same — restore backup |
| ADD_CONSTRAINT (NOT NULL, CHECK) | Table rebuild; restore backup |
| DATA_FIX (UPDATE during migration) | Restore backup (data change not reversible without it) |

**General procedure:**

1. Halt Phase E
2. Identify which migration M{N} failed
3. Stop the `engine.engine --migrate` run if still in progress
4. Take a snapshot of current state: `bible_research_post_fail_M{N}_{YYYYMMDD}_{HHMMSS}.db`
5. Restore the pre-migration backup: copy `bible_research_pre_M{N}_{YYYYMMDD}_{HHMMSS}.db` → `data/bible_research.db`
6. Confirm `schema_version` reflects the pre-M{N} state
7. Record rollback in execution log
8. Produce RD item for corrective action

---

## 16. Fallback Protocol

| Failure mode | Fallback position |
|---|---|
| Session interrupted mid-phase | Beginning of current step. Read obslog to understand work completed within step; continue from last recorded action. |
| Migration applied but post-check fails | Immediate rollback via pre-migration backup; RD item for corrective migration design. |
| Script update breaks a consumer | Revert the specific file change; pin migration application until updated script is correct. |
| Dry-run fails in Step C.5 | Do not advance to Phase E for that migration. Iterate migration code; re-dry-run. |
| Researcher approval pending longer than expected | Session may end cleanly. Gate holds; next session resumes at the same step. No forced progression. |
| RD item unresolvable within a session | Session may end cleanly with RD item open. Phase / step holds until resolution. |

---

## 17. Completion Record Format (Schema Completion Record — §F.7 template above)

See §13 Step F.7 for the full template.

---

## 18. Integrity Rules

These rules govern the DB-wide review.

| Rule | Status | Text |
|---|---|---|
| DBR-01 | Active | No DDL without a Change Plan item backing it (traces from Phase B bundle → migration → execution). |
| DBR-02 | Active | No migration runs without G3 approval recorded in the migration design note. |
| DBR-03 | Active | Pre- and post-check counts required per migration; mismatch halts E.3 or E.5. |
| DBR-04 | Active | Backup must exist before each migration application; missing backup halts E.2. |
| DBR-05 | Active | `EXPECTED_SCHEMA_VERSION` is bumped in the same commit as the migration code. |
| DBR-06 | Active | Every DROP_COLUMN migration is preceded by script update confirming no active references (Phase D completes before the DROP_COLUMN migration applies in Phase E). |
| DBR-07 | Active | Schema Completion Record produced before the per-word readiness sweep is permitted to start. |
| DBR-08 | Active | Rollback procedure stated in the migration design note; tested via backup restore if MODERATE or HIGH risk. |
| DBR-09 | Active (per Q4) | Redundant scripts are moved to `archive/scripts/` during Phase D, with the script update log recording source, destination, reason, and date. |
| DBR-10 | Active (per Q8) | The Change Plan is organised as per-phase migration bundles, not per-table. Each bundle's changes are semantically related and apply in one transaction. |
| DBR-11 | Active (per Q12) | The six Analysis-Complete words (compassion 23, fellowship 62, forgiveness 64, grace 68, love 103, mercy 111) are reset to `Verse Context Reset` during Phase F.6 and enter the full pipeline as if fresh post-migration. Prior Session B narratives are archived in the prose store (if stored there); prior `.md` outputs on disk remain as historical artefacts. |
| DBR-12 | Active | Historical patches in `data/imports/WA/Patches/` and `archive/patches/` are immutable. No rewriting for new schema (per Q5). |
| DBR-13 | Active | CC asks no questions in chat. All researcher-input items are written to the RD accumulator `.md` per CC-RD-001. |
| DBR-14 | Active | Every artefact produced during DB review is versioned per GR-FILE-004 (no overwrites); obslog increments minor version at session boundaries per GR-OBS-004. |

---

## 19. Appendix A — SQL Library for Phase A Audit

Boilerplate queries to reuse during Phase A. Run each against the live DB; capture output in the audit report.

### A.1 Tables

```sql
SELECT name, sql FROM sqlite_master
WHERE type='table' AND name NOT LIKE 'sqlite_%'
ORDER BY name;
```

### A.2 Row counts per table

```sql
-- Programmatically build via script: for each table name from above,
-- execute: SELECT 'table' AS name, COUNT(*) AS n FROM table;
```

### A.2 Column metadata

```sql
SELECT name, type, "notnull", dflt_value, pk
FROM pragma_table_info('table_name');
```

### A.2 Column usage

```sql
-- Non-NULL count
SELECT COUNT(*) FROM table_name WHERE column_name IS NOT NULL;

-- Distinct cardinality
SELECT COUNT(DISTINCT column_name) FROM table_name;
```

### A.3 FK list

```sql
SELECT * FROM pragma_foreign_key_list('table_name');
```

### A.3 Orphans per FK

```sql
SELECT COUNT(*) AS orphans
FROM child_table c
LEFT JOIN parent_table p ON c.fk_column = p.id
WHERE p.id IS NULL;
```

### A.4 Index list

```sql
SELECT name, tbl_name, sql FROM sqlite_master
WHERE type='index'
ORDER BY tbl_name, name;
```

### A.4 Index columns

```sql
SELECT * FROM pragma_index_info('index_name');
```

### A.5 Constraint inventory (parse from DDL)

```sql
SELECT sql FROM sqlite_master WHERE type='table';
-- Parse NOT NULL / UNIQUE / CHECK clauses in code
```

### A.6 Schema version

```sql
SELECT version, applied_at, description
FROM schema_version
ORDER BY applied_at DESC;
```

---

## 20. Appendix B — Migration Design Note Template

```text
# Migration M{N} — [short descriptor]

## Bundle reference
- Change Plan bundle: [bundle descriptor]
- Tables touched: [list]
- DBR-CHG items: [list]
- Risk: [LOW / MEDIUM / HIGH]
- Reversibility: [EASY / MODERATE / HARD]
- Data loss: [NO / YES — approved: ___]

## Pre-check
```sql
-- SQL here
```
Expected: ___

## Migration code location
`engine/migrate.py` — function `migration_M{N}(conn)`

## Post-check
```sql
-- SQL here
```
Expected: ___

## Verification tests
- Row counts on affected tables before vs after: ___
- Smoke test list: ___

## Rollback procedure
[Specific to this migration — usually "restore backup bible_research_pre_M{N}_{...}.db"]

## Script updates required (feeds Phase D)
- [file]: [change description]

## G3 Approval
[ ] APPROVED — proceed to Phase E application
Date: ___
Reviewer: le Roux Cilliers
Notes: ___

## Execution outcome (filled at Phase E)
Pre-check: ___
Post-check: ___
Smoke tests: ___
schema_version after: ___
Backup retained: ___
```

---

## 21. Appendix C — Change Type Catalogue with Risk and Reversibility

| Change Type | Risk | Reversibility | Backup strategy | Notes |
|---|---|---|---|---|
| ADD_COLUMN | LOW | EASY (ALTER DROP) | Pre-migration backup | Purely additive |
| DROP_COLUMN (confirmed unused) | LOW | EASY via re-ADD + restore | Pre-migration backup | Drop after Phase D confirms no references |
| DROP_COLUMN (historically populated) | MEDIUM | MODERATE | Pre-migration backup 6mo | Data lost unless backup |
| RENAME_COLUMN | MEDIUM | EASY | Pre-migration backup | Update all references in Phase D first |
| CHANGE_TYPE (TEXT → INTEGER, etc.) | HIGH | MODERATE | Pre-migration backup | Conversion may lose precision; test on dry-run |
| ADD_INDEX | LOW | TRIVIAL | None needed | DROP INDEX to reverse |
| DROP_INDEX | LOW | TRIVIAL | None needed | CREATE INDEX from DDL to reverse |
| DROP_FK | LOW | EASY | None needed | Re-add via table rebuild if reversing |
| ADD_FK | MEDIUM | EASY | Pre-migration check for violations | Confirm no violators before adding |
| ADD_CONSTRAINT (NOT NULL, CHECK) | MEDIUM | EASY | Pre-migration check | Confirm no violators |
| DATA_FIX (UPDATE during migration) | MEDIUM-HIGH | MODERATE | Pre-migration backup | Requires explicit researcher approval in Change Plan |
| ADD_TABLE | LOW | TRIVIAL | None needed | DROP TABLE to reverse |
| ADD_VIRTUAL_TABLE (FTS5) | LOW | TRIVIAL | None needed | Rebuild from content table if needed |

---

*wa-global-database-review-instruction-v1_0-20260419.md*
*Framework B — Soul Word Analysis Programme*
*Based on: wa-global-database-review-design-v1-20260419.md (approved 2026-04-19)*
*Paired with: wa-global-readiness-sweep-instruction (to be produced for Phase F follow-on)*
