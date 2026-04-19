# WA — Schema Changes Required for Session B Catalogue Integration
**Filename:** wa-global-schema-sessionb-changes-v1_1-20260416.md
**Date:** 2026-04-16
**Version:** v1.1
**Change note (v1.1):** Baseline updated from schema v3.7.0 to v3.8.0 (2026-04-16). SC-01 revised — several fields already applied in v3.8.0; remaining required fields identified post-catalogue. SC-02 confirmed as still required. SC-03 redesigned per researcher direction (obs_id as PK, question_code as UNIQUE, active replaced by status with three values, deleted field added). SC-04 confirmed with explicit PK. SC-05 confirmed as already created in v3.8.0 — remaining gap identified. SC-06 closed — wa_session_research_flags confirmed as Session D table only; no structural change required. New SC-07 added — wa_session_research_flags Step 1.3c gate requirement (instruction change only, no schema change). Step 1.3 restructure confirmed: three sub-steps 1.3a / 1.3b / 1.3c replacing old Steps 1.3 and 1.4. Two open questions from v1.0 resolved.
**Supersedes:** wa-global-schema-sessionb-changes-v1_0-20260416.md

**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_1-20260416.md (task list)
- wa-global-session-log-catalogue-findings-v1-20260415.md (DIR-20260415-002)
- database-schema-20260416.json (schema v3.8.0 — current baseline)
- assessment-wa-session-b-findings.md (findings table assessment)
- assessment-wa-session-research-flags.md (research flags assessment)
- wa-sessionb-findings-all-20260415.json / wa-sessionb-findings-split-20260415.json (data)

---

## Purpose

This document identifies all schema changes required to support the Session B catalogue integration and the Step 1.3 restructure. It is the design authority for the CC directive(s) that must be executed before the updated Session B instruction can be used operationally.

---

## Baseline: Schema v3.8.0 (2026-04-16)

Schema v3.8.0 contains 42 tables. Changes from v3.7.0 relevant to this work:

**`wa_session_b_findings`** (171 rows) — v3.8.0 fields:
`id, finding_id, registry_id, file_id, finding_type, finding, anchor_verses, raised_date, session_b_instruction, pass_ref, study_segment, delete_flag, obsolete_reason, obsolete_date, superseded_by_id, related_finding_id, resolution_note, thin_evidence`

Nine lifecycle fields were added by DIR-20260415-004. `pass_ref`, `study_segment`, `delete_flag`, `thin_evidence` now exist. `delete_flag` naming is confirmed — the schema uses this name (not `delete_flagged`); Q1 from v1.0 is resolved.

**`wa_finding_entity_links`** (0 rows) — created by DIR-20260415-005:
`id, finding_id, entity_type, entity_id, entity_strongs, raised_date`
FK: `finding_id → wa_session_b_findings(id)`

**`wa_session_research_flags`** (327 rows) — unchanged from v3.7.0:
`id, registry_id, file_id, flag_code, flag_label, strongs_reference, cross_registry_id, priority, session_target, description, session_raised, raised_date, resolved, resolved_date, resolved_note`
- 318 rows: `session_target = 'D'`
- 9 rows: `session_target = 'B'` (data quality / pre-analysis issues requiring Session B resolution)

**`wa_term_phase2_flags`** (1,580 rows) — unchanged from v3.7.0:
`term_inv_id, flag_id, description, source, raised_date`

**`wa_obs_question_catalogue`**: **DOES NOT EXIST**

**`wa_finding_catalogue_links`**: **DOES NOT EXIST**

---

## Confirmed Decisions

**Q1 (v1.0) — `delete_flag` naming:** Resolved by schema evidence. The field is `delete_flag` on `wa_session_b_findings` (confirmed in v3.8.0). No change needed.

**Q2 (v1.0) — SC-06 `wa_session_research_flags`:** Resolved by researcher direction. `wa_session_research_flags` is the Session D directive table. No structural changes required. The 9 `session_target = 'B'` rows are handled through the instruction (Step 1.3c), not through schema changes. SC-06 is closed.

**Step 1.3 restructure:** Confirmed. Old Steps 1.3 and 1.4 replaced by three sub-steps:
- **1.3a** — Clear `wa_term_phase2_flags` (was Step 1.4)
- **1.3b** — Complete open `wa_session_b_findings`
- **1.3c** — Clear `wa_session_research_flags` `session_target = 'B'` flags (hard gate)
Steps 1.5 and 1.6 renumber to 1.4 and 1.5 accordingly.

---

## Gap Analysis (updated against v3.8.0)

### Gap 1 — `wa_session_b_findings`: remaining fields still required post-catalogue

Fields added by DIR-20260415-004 and present in v3.8.0:
`pass_ref` ✓ | `study_segment` ✓ | `delete_flag` ✓ | `thin_evidence` ✓ | `obsolete_reason` ✓ | `obsolete_date` ✓ | `superseded_by_id` ✓ | `related_finding_id` ✓ | `resolution_note` ✓

Fields still required by the catalogue integration (not yet in schema):

| Field | Type | Purpose |
|---|---|---|
| `status` | TEXT DEFAULT 'pending' | Lifecycle state: pending / in_review / complete. Required by session log item 3.5 close procedure and Step 1.3b review. |
| `term_id` | INTEGER NULL | FK to `mti_terms.id` — for findings triggered by specific terms. Required by DIR-20260415-002. |

**Observation:** The pre-catalogue instruction gaps are resolved. Only the two catalogue-specific fields remain.

### Gap 2 — `wa_finding_entity_links`: table exists but is incomplete

Table created by DIR-20260415-005. Current fields:
`id, finding_id, entity_type, entity_id, entity_strongs, raised_date`

Missing field required by the instruction and consistent with schema conventions:

| Field | Type | Purpose |
|---|---|---|
| `delete_flagged` | INTEGER DEFAULT 0 | Soft delete — consistent with programme-wide convention |

Additional observation: `entity_strongs` provides a denormalised Strong's reference. This is a reasonable design choice for the polymorphic FK pattern. No change required here.

### Gap 3 — `wa_obs_question_catalogue` does not exist

Designed in DIR-20260415-002. Researcher direction this session adds the following changes to that design:
- `obs_id` as auto-generated PK (not `question_code`)
- `question_code` as UNIQUE constraint (not PK)
- Replace `active` (integer 0/1) with `status` TEXT with three values: `active` / `word_specific` / `non_word`
- Add `deleted` field (INTEGER DEFAULT 0) for soft delete

**Note on `status` values:**
- `active` — universal question, applied to every word
- `word_specific` — question formulated for a specific word's analysis; not applied universally
- `non_word` — question captured in the catalogue but only occasionally applicable; not in the standard word-analysis rotation

### Gap 4 — `wa_finding_catalogue_links` does not exist

Designed in DIR-20260415-002. Needs an explicit auto-generated PK (was absent from original design).

### Gap 5 — `wa_term_phase2_flags`: missing soft-delete fields

Still required. Not addressed by any directive to date.

### Gap 6 — CLOSED

`wa_session_research_flags` requires no schema changes. The `session_target = 'B'` gate is an instruction requirement (Step 1.3c), not a schema change.

---

## Proposed Schema Changes

Listed in execution order.

---

### SC-01 — Alter `wa_session_b_findings`: add two catalogue fields
**Type:** ALTER TABLE (ADD COLUMN × 2)
**Prerequisite:** None
**Table:** `wa_session_b_findings`

| Column | Type | Default | Constraints | Purpose |
|---|---|---|---|---|
| `status` | TEXT | 'pending' | NULL allowed | Lifecycle state: pending / in_review / complete |
| `term_id` | INTEGER | NULL | FK → mti_terms(id) ON DELETE SET NULL | Finding triggered by a specific term |

**Note:** All other required fields are already present in v3.8.0. This SC adds only the two catalogue-integration fields.

---

### SC-02 — Alter `wa_term_phase2_flags`: add soft-delete fields
**Type:** ALTER TABLE (ADD COLUMN × 2)
**Prerequisite:** None
**Table:** `wa_term_phase2_flags`

| Column | Type | Default | Purpose |
|---|---|---|---|
| `delete_flagged` | INTEGER | 0 | Soft delete — 1 = flag rejected during Step 1.3a audit |
| `obsolete_reason` | TEXT | NULL | Records why the flag was rejected |

---

### SC-03 — Create `wa_obs_question_catalogue`
**Type:** CREATE TABLE
**Prerequisite:** None
**Table:** `wa_obs_question_catalogue`

| Column | Type | Constraints | Purpose |
|---|---|---|---|
| `obs_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Auto-generated surrogate key |
| `question_code` | TEXT | NOT NULL UNIQUE | e.g. 'Q001', 'F-001', 'C-008' — human-readable stable reference |
| `section` | TEXT | NOT NULL | Section label (e.g. 'Section 1', 'Mercy Extensions') |
| `source_word` | TEXT | NULL | Word study that generated the question |
| `source_registry_no` | INTEGER | NULL FK → word_registry(id) | Registry of source word |
| `question_text` | TEXT | NOT NULL | Full question text |
| `pattern_type` | TEXT | NULL | Pattern code (e.g. P01, P14) if question maps to a pattern |
| `scope` | TEXT | NOT NULL DEFAULT 'universal' | 'universal' or 'word_specific' — analytical scope |
| `status` | TEXT | NOT NULL DEFAULT 'active' | 'active' / 'word_specific' / 'non_word' |
| `deleted` | INTEGER | NOT NULL DEFAULT 0 | Soft delete |
| `date_added` | TEXT | NOT NULL | ISO date |
| `catalogue_version` | TEXT | NOT NULL | Catalogue version at which question was added (e.g. 'v2.0') |

**Note on `scope` vs `status`:** Both fields are retained. `scope` captures the analytical scope at creation (universal / word_specific). `status` captures the operational state (active / word_specific / non_word). They serve different purposes and both are needed.

**To be populated:** 194 rows from `wa-global-obs-question-master-catalogue-v2_0-20260415.md` plus any additional questions confirmed from C-1 through C-9 gap candidates (T-08, pending researcher decision).

---

### SC-04 — Create `wa_finding_catalogue_links`
**Type:** CREATE TABLE
**Prerequisite:** SC-01 (status field on findings), SC-03 (catalogue table exists)
**Table:** `wa_finding_catalogue_links`

| Column | Type | Constraints | Purpose |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Auto-generated surrogate key |
| `finding_id` | INTEGER | NOT NULL FK → wa_session_b_findings(id) | |
| `question_id` | INTEGER | NOT NULL FK → wa_obs_question_catalogue(obs_id) | |
| `coverage` | TEXT | NULL | FULL / PARTIAL — how well the question covers the finding |
| `status` | TEXT | NOT NULL DEFAULT 'suggested' | suggested / validated / rejected |
| `pattern_type` | TEXT | NULL | Pattern code from the 18-pattern analysis |
| `mapped_date` | TEXT | NULL | Date the link was first mapped |
| `validated_date` | TEXT | NULL | Date the link was validated during Session B |
| `validated_by` | TEXT | NULL | Session reference (e.g. 'Session B v5.1 — Registry 023') |
| `session_b_note` | TEXT | NULL | Analyst note on why this question applies |
| `delete_flagged` | INTEGER | NOT NULL DEFAULT 0 | Soft delete — consistent with schema convention |

**Unique index:** `(finding_id, question_id)`

**Note on `delete_flag` vs `delete_flagged`:** This table uses `delete_flagged` to be consistent with the programme-wide schema convention. `wa_session_b_findings` uses `delete_flag` (as confirmed in v3.8.0) — that is an existing schema fact and is not changed here.

---

### SC-05 — Alter `wa_finding_entity_links`: add soft-delete field
**Type:** ALTER TABLE (ADD COLUMN × 1)
**Prerequisite:** None (table already exists in v3.8.0)
**Table:** `wa_finding_entity_links`

| Column | Type | Default | Purpose |
|---|---|---|---|
| `delete_flagged` | INTEGER | 0 | Soft delete — consistent with programme-wide convention |

**Current state:** Table exists with 0 rows. Addition is safe with no data impact.

---

### SC-06 — CLOSED
No changes to `wa_session_research_flags`. Session D table — design confirmed as correct. The `session_target = 'B'` rows are managed through instruction Step 1.3c (hard gate), not schema changes.

---

## Summary of Changes

| SC | Table | Type | Status | Notes |
|---|---|---|---|---|
| SC-01 | `wa_session_b_findings` | ALTER — 2 columns | Ready to draft directive | Post-catalogue fields only |
| SC-02 | `wa_term_phase2_flags` | ALTER — 2 columns | Ready to draft directive | Soft-delete support for Step 1.3a |
| SC-03 | `wa_obs_question_catalogue` | CREATE TABLE | Ready to draft directive | obs_id PK; status replaces active; deleted added |
| SC-04 | `wa_finding_catalogue_links` | CREATE TABLE | Ready to draft directive | Explicit PK added |
| SC-05 | `wa_finding_entity_links` | ALTER — 1 column | Ready to draft directive | Table exists; add delete_flagged only |
| SC-06 | `wa_session_research_flags` | — | CLOSED | No schema change required |

**All open questions from v1.0 are resolved. No researcher decisions required before directive is drafted.**

---

## Instruction Changes Confirmed (not schema changes)

These are instruction-level changes confirmed during this review. They are recorded here for completeness and will be incorporated into the task list.

| Item | Instruction location | Change |
|---|---|---|
| Step 1.3 restructure | Stage 1 | Old Steps 1.3 + 1.4 replaced by Steps 1.3a / 1.3b / 1.3c |
| Step 1.3a | New | Review and disposition `wa_term_phase2_flags` per active terms |
| Step 1.3b | New | Review and disposition existing `wa_session_b_findings` for this registry |
| Step 1.3c | New | Hard gate: resolve all `wa_session_research_flags` rows with `session_target = 'B'` and `resolved = 0` |
| Step renumbering | Stage 1 | Old Step 1.5 → Step 1.4; Old Step 1.6 → Step 1.5 |

---

## Next Step

T-SC: Draft a single CC directive covering SC-01 through SC-05. Submit for researcher approval, then CC execution. Schema verification query to follow. This is the prerequisite for tasks T-02 through T-07.

---

*End of wa-global-schema-sessionb-changes-v1_1-20260416.md*
*Supersedes wa-global-schema-sessionb-changes-v1_0-20260416.md*
*Schema baseline: v3.8.0 (2026-04-16)*
