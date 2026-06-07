# DB-Wide Review — RESEARCHER_DECISION Accumulator v1 — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-databasereview-rd-v1-20260419.md |
| Governs | RESEARCHER_DECISION items raised during the DB-wide review |
| Discipline | CC-RD-001 (via file, not chat); GR-RD-001 through GR-RD-006 |
| Format | Mark up answers inline. Each item has OPEN / RESOLVED status. |
| Produced | 2026-04-19 |

---

## How to Respond

For each open RD item:

1. Read the options and CC's recommendation
2. Write your decision inline under **Researcher decision:**
3. Change status to `RESOLVED — [date]`
4. CC polls this file at session resume; acts on resolved items; does not act on OPEN items

---

## RD-DBR-001 — Lock sentinel casing

**Status:** OPEN — raised 2026-04-19 at Phase A §A.7

**Source step:** A.7 (Type inconsistencies)

**Context:**

`engine/constants.py::LOCK_SENTINEL = 'IN_PROGRESS'` (uppercase underscore)
`word_registry.phase1_status` actual distinct values: `'Complete'` · `'Excluded'` · `'In Progress'` (title case space)

These do not match. Any code path that compared `status` to `LOCK_SENTINEL` would never find a match under the current data convention.

**Why unresolvable without researcher input:**

- Path 1 (data correction): impossible to know authoritative direction without researcher intent
- Path 2 (re-run): not applicable — this is a semantic/naming decision, not a process
- Path 3 (defer to verse reading): not applicable — pure constant/data consistency question

**Question:**

Which is canonical?

**Options:**

- **(a)** Update `engine/constants.py::LOCK_SENTINEL` to `'In Progress'`. Data is authoritative. Change is in one file; low impact.
- **(b)** Update `word_registry.phase1_status` data to `'IN_PROGRESS'`. Update all 2 currently 'In Progress' rows; document as the canonical value going forward. Future inserts use this value.
- **(c)** Introduce a controlled-vocabulary lookup table `phase1_status_types` with FK enforcement. More invasive but prevents future drift.
- **(d)** Other — specify

**CC's recommendation:** **(a)** — data is authoritative; constant was never correctly matched. Single-file change; no DML needed. Include in a dedicated migration bundle as a pure code change (no DDL, no DML) — logged in the Phase D script-update log, not in Phase C migrations.

**Researcher decision:** Accept CC recommendation — option (a). Update `engine/constants.py::LOCK_SENTINEL` to `'In Progress'`.

**Status after resolution:** [X] RESOLVED — 2026-04-19 — option (a)  [ ] OPEN

---

## RD-DBR-003 — Strategy for `somatic_link` / `god_as_subject` reconciliation

**Status:** OPEN — raised 2026-04-19 at Phase B

**Source step:** B.1 (Change Plan grouping)

**Context:**

Phase A §A.8 assumed CLAUDE.md §17.6's "superseded by mti_term_flags" was accurate and recommended DROP. Deeper investigation in Phase B revealed:

| Column | `wa_term_inventory` rows with value=1 | `mti_term_flags` rows covering same concept | Overlap |
|---|---|---|---|
| `somatic_link` | 162 | 6 (flag_id 3, 4) | 2 |
| `god_as_subject` | 208 | 39 (flag_id 1) | 13 |

The "supersession" did not happen at the data level. Dropping the boolean columns today would lose ~350 rows of analytical content not reflected in `mti_term_flags`.

**Why unresolvable without researcher input:**

- Path 1: population strategy is a policy decision, not a data correction
- Path 2/3: not applicable

**Question:**

Which reconciliation strategy?

**Options:**

- **(a)** Populate `mti_term_flags` from the booleans in a new migration (M23), then drop the booleans in M24. Makes `mti_term_flags` canonical going forward. CC recommends this — matches CLAUDE.md §17.6 original intent.
- **(b)** Retain both as equal sources; update CLAUDE.md §17.6 to reflect dual-source reality; no drops. Simpler but preserves data duplication.
- **(c)** Designate `wa_term_inventory.somatic_link` / `.god_as_subject` as canonical; deprecate the corresponding `mti_term_flags` rows; simplify by reducing the flag table's role.

**CC's recommendation:** **(a) populate then drop**. Honours the CLAUDE.md §17.6 original intent while safely migrating the data. Makes `mti_term_flags` authoritative as documented.

**Researcher decision:** Accept CC recommendation — option (a). M23 populates `mti_term_flags`; M24 drops the boolean columns after post-check PASS.

**Status after resolution:** [X] RESOLVED — 2026-04-19 — option (a)  [ ] OPEN

---

## RD-DBR-002 — `schema_version` table rebuild

**Status:** OPEN — raised 2026-04-19 at Phase A §A.7

**Source step:** A.7 (Type inconsistencies)

**Context:**

`schema_version` table has three rows. `id` does NOT reflect application order:

| id | version_code | applied_at |
|---|---|---|
| 1 | **3.9.0** (newest) | 2026-04-16 05:17:38 (space-separator) |
| 2 | 3.7.1 (older) | 2026-03-29T12:52:09Z (T-separator UTC) |
| 3 | 3.8.0 (intermediate) | 2026-03-29T12:54:48Z (T-separator UTC) |

Two inconsistencies:

1. `id` autoincrement has been reset or re-used at some point; order is not preserved
2. `applied_at` format varies between rows

**Why unresolvable without researcher input:**

- Path 1 (data correction): the fix approach (rebuild vs normalise forward) is a policy decision
- Path 2, 3: not applicable

**Question:**

How should `schema_version` order and format be handled?

**Options:**

- **(a)** Rebuild the table in a dedicated migration: preserve `version_code`, `applied_at`, `migration_history` content; assign new `id` reflecting chronological order; normalise `applied_at` to T-separator UTC throughout. Includes a pre/post-check for row count equality.
- **(b)** Leave historical rows as-is; only enforce ordering for new rows going forward. Add a trigger or application-level check.
- **(c)** Replace `schema_version` with a new table `schema_version_log` with stronger invariants (UNIQUE on `version_code`; NOT NULL + CHECK on `applied_at` format); migrate content; drop old table.
- **(d)** Other — specify

**CC's recommendation:** **(a)** — rebuild. Simple migration; content preserved; ordering invariant established. Schema audit reliability improves. No downstream impact expected (schema_version is primarily read for humans and engine startup checks).

**Researcher decision:** Accept CC recommendation — option (a). Rebuild `schema_version` with chronologically ordered id; normalise `applied_at` to T-separator UTC.

**Status after resolution:** [X] RESOLVED — 2026-04-19 — option (a)  [ ] OPEN

---

## How CC Acts on Resolutions

- RESOLVED items: incorporated into the current Change Plan bundle authoring
- OPEN items: Phase B may proceed for bundles not dependent on the RD, but any bundle touching the affected area (e.g. constants in RD-DBR-001) is held until resolution
- Deferred items: moved to outstanding tasks if researcher indicates "not now"

---

*End of RD accumulator v1 — 2026-04-19*
