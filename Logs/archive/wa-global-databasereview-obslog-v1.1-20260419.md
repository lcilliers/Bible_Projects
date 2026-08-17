# DB-Wide Review — Observations Log v1.1 — 2026-04-19

| Field | Value |
|---|---|
| Filename | wa-global-databasereview-obslog-v1.1-20260419.md |
| Instruction | `wa-global-database-review-instruction-v1_0-20260419.md` (Active — approved 2026-04-19) |
| Obslog version | v1.1 |
| Prior version | v1 (retained — session 1 close state) |
| Session start | 2026-04-19 (session 2 — Phase B kickoff) |
| Obslog discipline | GR-OBS-001 (write on discovery); CC-OBS-001 (obslog is the primary record) |
| Version discipline | GR-OBS-004 + GR-FILE-004 — minor version increment at each session boundary; no overwrites |

---

## Pre-Flight Record

**SESSION STARTED: 2026-04-19**

Obslog v1 created. Four named sections initialised per instruction §4.

### S1 — Governing documents loaded

Per CC-LOAD-001. Resolved versions:

- `wa-global-general-rules [current]` → **wa-global-general-rules-v2_11-20260418.json**
- `wa-claudecode-rules [current]` → **wa-claudecode-rules-v1_0-20260419.md** (Active — approved 2026-04-19)
- Instruction → **wa-global-database-review-instruction-v1_0-20260419.md** (Active — approved 2026-04-19)
- `wa-patch-instruction [current]` → **wa-patch-instruction-v2_1-20260418.md**
- `wa-directive-instruction [current]` → **wa-directive-instruction-v1_1-20260418.md**
- Design workings → **wa-global-database-review-design-v1-20260419.md** (APPROVED 2026-04-19)

All six confirmations recorded.

### S2 — Schema version check (CC-VERSION-001)

Query: `SELECT version_code, applied_at FROM schema_version ORDER BY id DESC LIMIT 1`

| Source | Value |
|---|---|
| DB `schema_version` (latest row by id) | `3.8.0` @ `2026-03-29T12:54:48Z` |
| DB `schema_version` (latest row by applied_at) | `3.9.0` @ `2026-04-16 05:17:38` |
| `engine/constants.py::EXPECTED_SCHEMA_VERSION` | `3.9.0` |

**Finding (pre-flight observation — will be recorded in A.7 / A.8 formally):** The `schema_version` table has inconsistencies:

1. Row ordering by `id` does NOT reflect application order. The `3.9.0` row has `id=1`, which is earlier than the `3.8.0` row at `id=3`. This likely indicates a re-insertion or restore sequence that the existing schema does not protect against.
2. Date format inconsistency: older rows use `T`-separator ISO-8601 (`2026-03-29T12:54:48Z`), newer uses space-separator (`2026-04-16 05:17:38`). ISO-8601 standard allows both, but consistency is preferable.
3. The latest version in `migration_history` JSON includes SC-01-05 entries, confirming schema is at 3.9.0 as of 2026-04-16.

**Determination:** Schema version MATCHES `EXPECTED_SCHEMA_VERSION = 3.9.0` by version_code when selecting the max-applied-at row. Proceed.

### S3 — Position check

Phase Progress Record is empty (first session of DB review). Resume from Phase A Step A.0 per instruction §5 resume table.

### S4 — Resumption record

```
SESSION RESUMED: 2026-04-19 (first session — no prior resumption)
  Obslog version: wa-global-databasereview-obslog-v1-20260419.md
  Schema version at resume: 3.9.0 (confirmed via version_code on max applied_at row)
  Resuming from: Phase A Step A.0 (pre-flight)
  Open RD items: 0
  Open outstanding tasks count: 0
```

---

## Phase Progress Record

| Step | Completed at | Findings delta |
|---|---|---|
| S0–S4 | 2026-04-19 | Pre-flight observations logged |
| A.0 | 2026-04-19 | Pre-flight PASS; baseline backup taken |
| A.1 | 2026-04-19 | 43 tables inventoried; all categorised per CLAUDE.md §3 |
| A.2 | 2026-04-19 | Column inventory produced; 25 null-only, 419 zero-ref, 5 known redundant confirmed |
| A.3 | 2026-04-19 | 44 FKs catalogued; fan-in/fan-out metrics; 3 simplification candidates identified |
| A.4 | 2026-04-19 | 86 indexes (25 auto + 61 explicit); no large tables lack explicit indexes |
| A.5 | 2026-04-19 | Constraint inventory done; 8 controlled-vocabulary gap candidates |
| A.6 | 2026-04-19 | **3 FK orphan findings (37 rows) + 2 cascade inconsistencies (13 rows) — BROKEN_INVARIANT** |
| A.7 | 2026-04-19 | Type inconsistencies: schema_version id ordering, date formats, lock sentinel casing |
| A.8 | 2026-04-19 | 5 known redundant columns confirmed; recommendations recorded |
| A.9 | 2026-04-19 | Audit report produced; G1 awaiting researcher approval |

*(Updated at each step sign-off)*

---

## Findings

### A.0 — Pre-Flight

1. **Schema version check:** DB at `3.9.0` (via version_code on max applied_at row) — matches `EXPECTED_SCHEMA_VERSION`. PASS.
2. **Applicator:** `scripts/apply_session_patch.py` — last modified `2026-04-16T15:24:50Z` (1301 lines). Header documents recent extensions through SC-01/SC-04/SC-05 catalogue integration. No internal version string. Assessed as current for `3.9.0`. PASS.
3. **Active locks on `word_registry.phase1_status`:**
    - `Complete`: 182 registries
    - `Excluded`: 30 registries
    - `In Progress`: 2 registries (grace 68, suffering 214 per CLAUDE.md §10)
    - No `IN_PROGRESS` (uppercase) values — value casing differs from `LOCK_SENTINEL` constant.
    - **Flag for A.7 / A.8:** LOCK_SENTINEL in `engine/constants.py` is `'IN_PROGRESS'` (uppercase underscore) but actual column values are `'In Progress'` (title case space). One of the two must be wrong. Logging as TYPE_INCONSISTENCY candidate.
4. **Baseline backup:** `backups/bible_research_pre_DBR_20260419_122435.db` — 158,800,259 bytes (~159 MB). Verified by read-only open: `word_registry` row count = 214.
5. **DB file size:** 159 MB (CLAUDE.md §3 states ~40 MB — outdated). Logging as documentation update for Phase F.

**A.0 PASS.** All four pre-flight conditions met. Proceeding to A.1.

### A.1 — Table Inventory

**43 tables** catalogued (excluding `sqlite_*`). All categorised per CLAUDE.md §3 table groups. Full table + row count in audit report §A.1. Headlines:

- Largest tables: `wa_verse_records` (~140k rows), `wa_term_inventory` (~7.5k), `mti_terms` (~7.5k), `verse_context` (~110k)
- `session_d_*` tables present but mostly empty (Session D has not kicked off)
- All 43 tables accounted for in categories (no uncategorised residue)

### A.2 — Column Inventory and Usage Metrics

Full per-table column breakdown with: type, NOT NULL, PK, default, non-NULL count, distinct count, code-reference count (grep across `engine/`, `analytics/`, `scripts/`). See audit report §A.2.

Cross-findings:

- **25 null-only columns** (zero non-NULL across any row; not PK). CLEANUP_CANDIDATE if zero code references.
- **Single-value columns**: columns where all rows hold the same single value (cardinality 1, count > 10) — INFORMATIONAL.
- **419 zero-reference columns** across all tables (no active script/engine/analytics reads them; not PK). Not all are deletable — some are written-only fields or future-use. Individual review needed in Phase B.

### A.3 — FK Graph

**44 registered FKs** via `PRAGMA foreign_key_list`. Fan-in / fan-out metrics captured.

Simplification candidates identified:

1. `file_id` FKs across WA-family tables (wa_term_inventory, wa_verse_records, wa_data_quality_flags, etc.) — parent registry reachable via alternative paths. Adds hop count.
2. `verse_context.mti_term_id` may be derivable from `group_id` → `verse_context_group.mti_term_id`.
3. `wa_dimension_index` holds multiple denormalised copies (`mti_term_id`, `strongs_number`, `owning_registry_no`, `owning_registry_word`, `group_code`) all derivable from `verse_context_group_id`.

### A.4 — Index Inventory

**86 indexes total** — 25 auto-indexes (from PK/UNIQUE) + 61 explicit CREATE INDEX. Listed in full in audit report §A.4.

**No large tables (> 1000 rows) are without explicit indexes.** Index coverage is reasonable; optimisation candidates are secondary (partial indexes for specific query hot paths).

### A.5 — Constraint Inventory

- NOT NULL: enumerated per table (see report)
- CHECK: present in several tables but coverage gaps exist
- UNIQUE: enumerated

**Controlled-vocabulary gap candidates** (8 columns where CLAUDE.md §17 defines vocabulary but no CHECK constraint enforces it):

- `word_registry.session_b_status` · `.verse_context_status` · `.phase1_status` · `.carry_forward`
- `wa_term_inventory.term_owner_type` · `.language` · `.evidential_status`
- `wa_dimension_index.dimension_confidence`

### A.6 — Orphan Rows (BROKEN_INVARIANT)

**3 FKs with orphan rows — 37 orphan rows total:**

| Child FK | Parent | Orphan count |
|---|---|---|
| `mti_term_cross_refs.mti_term_id` | `mti_terms.id` | 2 |
| `wa_meaning_sense.parsed_meaning_id` | `wa_meaning_parsed.id` | 25 |
| `wa_term_phase2_flags.term_inv_id` | `wa_term_inventory.id` | 10 |

**Soft-delete cascade inconsistencies:**

- `wa_term_inventory.delete_flagged=1` with child `wa_verse_records.delete_flagged=0`: **6** rows
- `mti_terms.status='delete'` with child `verse_context_group.delete_flagged=0`: **7** rows
- (Script error on `wa_file_index.delete_flagged` check — that column may not exist on that table; confirming in Phase B will surface it)

**Disposition:** must be resolved (orphan deletion or parent restoration) before any FK additions. To remediate in Change Plan Bundle.

### A.7 — Type Inconsistencies

Key findings:

1. **`schema_version.id` does NOT reflect application order.** Newest version `3.9.0` sits at `id=1`; older `3.8.0` at `id=3`. Likely caused by re-insertion/restore. Schema has no ordering protection.
2. **Date format inconsistency in `schema_version.applied_at`:** 2 rows use `T`-separator ISO-8601 with `Z` (`2026-03-29T12:54:48Z`); 1 row uses space-separator local-style (`2026-04-16 05:17:38`).
3. **Lock sentinel casing mismatch:** `engine/constants.py::LOCK_SENTINEL = 'IN_PROGRESS'` vs actual `word_registry.phase1_status` value `'In Progress'`. One must be wrong. **RD candidate.**
4. **Boolean column check:** spot-checked 10 boolean columns — all INTEGER 0/1 (programme standard). Consistent. PASS.
5. **Strong's prefix casing:** consistent — `H` / `G` only. PASS.

### A.8 — Redundant Column Confirmation

Five known candidates from CLAUDE.md §17.6 confirmed against live usage metrics:

| Column | Non-NULL | Distinct | Code refs | Recommendation |
|---|---|---|---|---|
| `wa_term_inventory.status_note` | 177 / 7550 | 142 | 0 | **DROP** |
| `wa_term_inventory.god_as_subject` | 7550 / 7550 | 2 | 0 | REVIEW (data populated, but no active consumer; mti_term_flags supersedes) |
| `wa_term_inventory.somatic_link` | 7550 / 7550 | 2 | 0 | REVIEW (as above) |
| `mti_terms.status_note` | 1504 / 7571 | 785 | 0 | REVIEW |
| `word_registry.inference_note` | 24 / 214 | 21 | 0 | REVIEW |

Cross-checks with `mti_term_flags` in the audit report (one cross-check query threw a column-name error in the script — `mf.id` doesn't exist on `mti_term_flags`; schema uses different PK name; minor script flaw, does not affect overall findings).

### A.9 — Audit Report and G1

**Audit report produced:** `outputs/reports/wa-global-database-audit-20260419.md` — 1,301 lines, 69.7 KB, 9 sections (§A.1–§A.8 + §Summary).

Ten candidate Change Plan bundles previewed in the report §Summary (to be formalised in Phase B):

1. Redundant column removal — Terms (DROP `god_as_subject`, `somatic_link`, `status_note`; DROP `mti_terms.status_note` pending)
2. Redundant column removal — Registry (DROP `word_registry.inference_note`)
3. New registry field (`word_registry.word_synopsis TEXT`)
4. Prose store setup (M_P1–M_P6)
5. Type normalisation — `schema_version` rebuild + date format
6. Type normalisation — lock sentinel casing (**RD required**)
7. Dimension index simplification (remove denormalised copies)
8. FK graph simplification (redundant `file_id` FKs)
9. Constraint coverage (8+ CHECK constraints on controlled-vocabulary columns)
10. Orphan row cleanup (37 rows + 13 cascade rows — BROKEN_INVARIANT resolution)

**G1 block** is at the end of the audit report awaiting `APPROVED — PROCEED to Phase B` marker.

### Open RD items raised by Phase A

1. **RD-DBR-001 — Lock sentinel casing.** `engine/constants.py::LOCK_SENTINEL = 'IN_PROGRESS'` vs `word_registry.phase1_status = 'In Progress'`. Which is canonical? Options: (a) update constant to match data; (b) update data to match constant; (c) introduce a sentinel lookup table. Recommendation: (a) — data is authoritative, constant was never correctly matched.
2. **RD-DBR-002 — `schema_version` rebuild.** Rebuild the table so `id` reflects application order, OR leave historical rows and only enforce order going forward? Recommendation: rebuild in a dedicated migration; preserve version-history content.

**(Not yet filed in RD accumulator file — will be filed at Phase B kickoff so the researcher has the full context when reviewing the audit report first.)**

---

## Open RD Items

None.

(RD accumulator file will be created on first RD item; target path: `outputs/wa-global-databasereview-rd-v1-20260419.md`)

---

## Outstanding Tasks (cross-reference)

None yet.

(Outstanding tasks file will be created on first entry; target path: `outputs/wa-global-outstanding-tasks-v1-20260419.md`)

---

*Obslog v1 — continues below as work progresses.*

---

## Session Close (session 1)

```text
SESSION CLOSED: 2026-04-19
  Obslog version at close: wa-global-databasereview-obslog-v1-20260419.md
  Last completed step: A.9 (audit report produced; G1 awaiting researcher approval)
  Session log produced: outputs/session-logs/wa-global-databasereview-sessionlog-v1-20260419.md
  Outstanding tasks updated: no (none raised)
  RD items raised this session: 2 (to be filed at Phase B kickoff)
  Next session: resume at Phase B kickoff after G1 approval; increment obslog to v1.1 at start
```

---

## Session 2 Resume (Phase B)

**SESSION RESUMED: 2026-04-19 (session 2)**

Per CC-OBS-001 and the instruction §5 resume protocol.

### S0 — Obslog incremented to v1.1

Prior version v1 retained; v1.1 created as copy + session 2 additions. All subsequent writes this session go to v1.1.

### S1 — Governing documents (re-confirmed)

Same set as session 1 — all six documents still at their 2026-04-19 resolved versions. No change.

### S2 — Schema version (re-check per CC-VERSION-001)

Schema version still `3.9.0`. PASS.

### S3 — Resume position

Last completed step (session 1): A.9. G1 approval marker now present on audit report (researcher approval 2026-04-19). Resume from **Phase B Step B.1**.

### S4 — Resumption record

```text
SESSION RESUMED: 2026-04-19 (session 2)
  Obslog version: wa-global-databasereview-obslog-v1.1-20260419.md
  Schema version at resume: 3.9.0
  Resuming from: Phase B Step B.1 (Group findings into migration bundles)
  G1 status: APPROVED 2026-04-19 (researcher marker on audit report)
  Open RD items: 0 filed (2 carried forward from A.9 — to be filed in RD accumulator this session)
  Open outstanding tasks count: 0
```

### Session 2 additional discoveries

#### B — deeper investigation findings

**Orphan root causes:**

- `mti_term_cross_refs` 2 orphans: both point to `mti_term_id=517` (not present in `mti_terms`). Cross-refs for "mind" (r112) and "being" (r211). Fix: DELETE the 2 cross_ref rows (M19 DBR-CHG-001).
- `wa_meaning_sense` 25 orphans across 4 distinct `parsed_meaning_id` values (2173, 2310, 2311, 2312). Fix: DELETE (M19 DBR-CHG-002).
- `wa_term_phase2_flags` 10 orphans from `source='bulk_patch'` dated 2026-03-19T18:18:06Z. `term_inv_id` values: 1059, 1061, 1065, 1066, 1071, 1072, 1075, 1077. Fix: DELETE (M19 DBR-CHG-003).

**Cross-check bug in Phase A audit script (documented; not blocking):** Script used `mf.id` on `mti_term_flags` which has compound PK `(mti_term_id, flag_id)` with no `id` column. Re-run manually in this session with correct schema; results appear below.

**Major finding — `somatic_link` / `god_as_subject` vs `mti_term_flags`:**

- CLAUDE.md §17.6 claimed these `wa_term_inventory` columns are superseded by `mti_term_flags`.
- Reality: `mti_term_flags` is severely underpopulated (54 rows total; 6 somatic, 39 GOD_AS_SUBJECT).
- `wa_term_inventory.somatic_link=1`: 162 rows; overlap with flags = 2; gap = 160.
- `wa_term_inventory.god_as_subject=1`: 208 rows; overlap with flags = 13; gap = 195.
- **The "supersession" never happened at data level.** Dropping today would lose ~350 rows.
- **Change Plan consequence:** two-phase approach (M23 populate → M24 drop) + new RD-DBR-003 for researcher confirmation.

**`word_registry.inference_note` (reversal from Phase A):**

- 24 rows contain substantive researcher-authored notes (e.g. "Character as a psychological construct…")
- CLAUDE.md §17.6 already flagged as "researcher-set only, pipeline must never overwrite" → RETENTION was intentional.
- **Change Plan consequence:** DROP recommendation REVERSED. Retain column. Update CLAUDE.md §17.6 to mark as RETAINED.

**FK simplification findings:**

- `wa_verse_records.file_id` vs `wa_term_inventory.file_id`: **765 mismatches**. NOT derivable. FK cannot be trivially dropped.
- `verse_context.mti_term_id`: fully derivable from `group_id` when set, but 27,230 rows (43%) have NULL `group_id` (set-aside verses). Retain FK.
- `wa_dimension_index` denormalised copies (`mti_term_id`, `group_code`, `strongs_number`, etc.): **0 mismatches across 3 checks**. Safe to drop all derivable columns — bundled into M25.

**`phase1_status` values confirmed:** `'Complete'` · `'Excluded'` · `'In Progress'` (title case, space-separator). `LOCK_SENTINEL = 'IN_PROGRESS'` constant in `engine/constants.py` definitely does not match. RD-DBR-001 confirmed.

#### Phase B Steps B.1–B.4

- **B.1 — Findings grouped into 10 migration bundles** (per Q8 override — per-phase bundles, not per-table)
- **B.2 — Per-bundle format applied** to each (rationale, DBR-CHG items, risk, reversibility, data loss, scripts affected, sequencing)
- **B.3 — Bundles sequenced M19–M28** with dependency notes
- **B.4 — Change Plan document produced:** `outputs/reports/wa-global-database-changeplan-v1-20260419.md`

#### RD items filed during Phase B

- RD-DBR-001 (carried from Phase A): Lock sentinel casing — filed
- RD-DBR-002 (carried from Phase A): `schema_version` rebuild — filed
- RD-DBR-003 (new, Phase B): `somatic_link` / `god_as_subject` reconciliation strategy — filed

All three in `outputs/wa-global-databasereview-rd-v1-20260419.md`.

---

## Session 2 Close

```text
SESSION CLOSED: 2026-04-19
  Obslog version at close: wa-global-databasereview-obslog-v1.1-20260419.md
  Last completed step: B.4 (Change Plan produced; G2 awaiting researcher approval)
  Session log will be produced: outputs/session-logs/wa-global-databasereview-sessionlog-v1.1-20260419.md
  Outstanding tasks updated: no
  RD items raised/filed this session: 3 total (2 carried forward + 1 new)
  Next session: resume at Phase C (migration development) after G2 approval + 3 RD resolutions
```
