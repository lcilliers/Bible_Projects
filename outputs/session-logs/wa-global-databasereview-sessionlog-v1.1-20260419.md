# DB-Wide Review — Session Log v1.1 — 2026-04-19 (session 2)

| Field | Value |
|---|---|
| Filename | wa-global-databasereview-sessionlog-v1.1-20260419.md |
| Session date | 2026-04-19 (session 2) |
| Obslog version at close | wa-global-databasereview-obslog-v1.1-20260419.md |
| Governing instruction | wa-global-database-review-instruction-v1_0-20260419.md |
| Session outcome | Phase B complete; G2 and 3 RD items awaiting researcher approval |

---

## What Was Accomplished

**Phase B — Change Plan — COMPLETE** (plus deeper investigation correcting one Phase A assumption)

Resumption S0–S4 + Phase B Steps B.1–B.4 executed. Full detail in:

- Observations log v1.1: [outputs/session-logs/wa-global-databasereview-obslog-v1.1-20260419.md](../session-logs/wa-global-databasereview-obslog-v1.1-20260419.md)
- **Change Plan (G2 artefact):** [outputs/reports/wa-global-database-changeplan-v1-20260419.md](../reports/wa-global-database-changeplan-v1-20260419.md) — 10 migration bundles (M19–M28); 44 DBR-CHG items; organised per-phase (per Q8 override)
- **RD accumulator:** [outputs/wa-global-databasereview-rd-v1-20260419.md](../wa-global-databasereview-rd-v1-20260419.md) — 3 items filed

**Step summary:**

| Step | Outcome |
|---|---|
| S0 | Obslog incremented v1 → v1.1 (prior retained) |
| S1–S2 | Governing documents + schema version re-confirmed |
| S3–S4 | Resume position: Phase B.1; G1 approval noted on audit report |
| B — deeper investigation | 4 major findings surfaced that refine Phase A recommendations |
| B.1 | 10 migration bundles identified from audit + investigation |
| B.2 | Per-bundle format applied (rationale, DBR-CHG items, risk, scripts) |
| B.3 | Bundles sequenced M19–M28 with dependency gates |
| B.4 | Change Plan document produced with G2 block + per-bundle approval table |

---

## Key Discoveries (deeper investigation beyond Phase A audit)

### 1. CLAUDE.md §17.6 supersession claim is contradicted by data

`wa_term_inventory.somatic_link` and `.god_as_subject` are claimed as "superseded by mti_term_flags". In practice:

- `mti_term_flags` has only 54 rows total
- Somatic overlap: 2 rows shared with 160+ rows in `wa_term_inventory` having no corresponding flag
- God-as-subject overlap: 13 shared; 195 rows only in `wa_term_inventory`

**Implication:** two-phase migration added — M23 populates `mti_term_flags` from `wa_term_inventory`, then M24 drops the columns. New RD-DBR-003 raised for approach confirmation.

### 2. `word_registry.inference_note` should be RETAINED (Phase A recommendation reversed)

24 rows contain substantive researcher-authored notes. CLAUDE.md §17.6 already says "researcher-set only, pipeline must never overwrite". Retention was always intentional; the "redundant" tag in §17.6 is misleading.

### 3. Orphan rows — specific rows identified for deletion

- `mti_term_cross_refs`: 2 rows pointing to `mti_term_id=517` (non-existent)
- `wa_meaning_sense`: 25 rows across parent IDs 2173, 2310, 2311, 2312
- `wa_term_phase2_flags`: 10 rows from `source='bulk_patch'` dated 2026-03-19

All hard-deleted in M19 with explicit approval.

### 4. FK simplification: `wa_dimension_index` has 0 mismatches on denormalised copies → safe to drop 8 derivable columns (M25)

---

## Current Position

**Phase B is complete pending:**

1. **G2 approval** on the Change Plan as a unit
2. **RD-DBR-001** (lock sentinel casing) — resolution needed for M26 constraint on `phase1_status`
3. **RD-DBR-002** (schema_version rebuild) — resolution needed for M27
4. **RD-DBR-003** (boolean flag reconciliation strategy) — resolution needed for M23 → M24 sequence

CC does not begin Phase C until:

- G2 approval is marked
- All 3 RD items are either RESOLVED or have a researcher decision to defer their dependent bundles

---

## Open Items

### RD accumulator status

| RD-ID | Subject | Status |
|---|---|---|
| RD-DBR-001 | Lock sentinel casing (`IN_PROGRESS` vs `In Progress`) | OPEN |
| RD-DBR-002 | `schema_version` rebuild strategy | OPEN |
| RD-DBR-003 | `somatic_link` / `god_as_subject` reconciliation | OPEN |

All three filed in `outputs/wa-global-databasereview-rd-v1-20260419.md` with options + recommendations.

### Outstanding tasks file

Not created — no items beyond CC's skill surfaced this session.

### Minor Phase D script-update items already identified (to be logged during Phase D)

- **PD.1** — `engine/constants.py::LOCK_SENTINEL` correction per RD-DBR-001 (single-line change; not a migration)
- **PD.2** — fix the `mf.id` cross-check bug in the Phase A audit script (`mti_term_flags` has compound PK, no `id` column)
- **PD.3** — CLAUDE.md updates for §17.6 (supersession reality, inference_note retention)

---

## Exact Resume Instructions

**Next session starts at:** Phase C kickoff (once G2 + 3 RD items resolved).

**Precondition before starting Phase C:**

1. Confirm G2 marker present on `outputs/reports/wa-global-database-changeplan-v1-20260419.md`
2. Read researcher resolutions for RD-DBR-001, RD-DBR-002, RD-DBR-003 in RD accumulator
3. Increment obslog to v1.2 (per CC-OBS-001 / GR-OBS-004 resumption protocol)
4. Confirm schema version still 3.9.0

**First Phase C action:** Step C.1 — author migration code for Bundle 1 (M19 orphan cleanup). Continue M20–M28 in sequence. Each migration gets a design note + G3 per-migration approval. Bundles dependent on RD items hold until RD resolved.

**Recommended bundle execution order** (after all G3 approvals on file):

1. M19 Orphan cleanup (no RD dependencies)
2. M20 Prose store setup (no RD dependencies)
3. M21 Registry enrichment (no RD dependencies)
4. M22 Obvious redundant drops (no RD dependencies)
5. M23 MTI flag reconciliation (**requires RD-DBR-003**)
6. M24 Drop reconciled booleans (depends on M23 post-check)
7. M25 Dimension index simplification (after Phase D script updates)
8. M26 Constraint coverage (**requires RD-DBR-001**)
9. M27 schema_version rebuild (**requires RD-DBR-002**)
10. M28 Index optimisation (last — benefits from stable schema)

---

## Downloads / Deliverables

1. [outputs/session-logs/wa-global-databasereview-obslog-v1.1-20260419.md](../session-logs/wa-global-databasereview-obslog-v1.1-20260419.md) (session 2 obslog)
2. [outputs/session-logs/wa-global-databasereview-sessionlog-v1.1-20260419.md](../session-logs/wa-global-databasereview-sessionlog-v1.1-20260419.md) (this file)
3. [outputs/reports/wa-global-database-changeplan-v1-20260419.md](../reports/wa-global-database-changeplan-v1-20260419.md) (the G2 artefact)
4. [outputs/wa-global-databasereview-rd-v1-20260419.md](../wa-global-databasereview-rd-v1-20260419.md) (RD accumulator — 3 items for researcher markup)

---

**SESSION CLOSED: 2026-04-19 (session 2)**

Next session: resume at Phase C kickoff once G2 + RD-DBR-001/002/003 resolutions are on file.

*End of session log v1.1 — 2026-04-19*
