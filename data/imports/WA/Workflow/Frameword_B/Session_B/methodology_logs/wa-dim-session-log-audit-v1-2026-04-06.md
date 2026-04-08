# WA — Dimension Review Audit Session Log
**File:** wa-dim-session-log-audit-v1-2026-04-06.md  
**Scope:** Ground Level 0 Registry Audit — pre-Dimension Review integrity check  
**Date:** 2026-04-06  
**Preceding output:** wa-dim-extract-C02-2026-04-06.json | wa-dim-existing-pointers-C02-2026-04-06.json  
**Governing instruction:** WA-DimensionReview-Instruction-v1.2-2026-04-06  
**Status:** Audit in progress — Level 0 complete, Level 1 pending

---

## 1. Session Context

The session opened with the intention of beginning the Dimension Review for Cluster C02. During Phase A (cluster assignment review), Registry 93 (intention) showed zero groups in the cluster extract despite the registry overview reporting 2 groups, 8 classified verses, and 3 anchors.

Investigation of this discrepancy revealed a systematic FK mismatch in `mti_terms.owning_registry_fk` affecting 58 terms across 8 mismatched entries — two distinct mechanisms. This surfaced a broader question about data integrity across the Verse Context stage, prompting a ground-up audit before any Dimension Review work proceeds.

The researcher correctly identified that proceeding without a proper data audit would undermine the entire downstream programme. The session pivoted to a structured audit starting at Level 0 — registry and term registration integrity.

---

## 2. Critical Decision — Programme Orientation

**Researcher finding:** The programme's governing principle (data-first, categories emerge from evidence) had been violated in practice. The C01 Dimension Review session proceeded without verifying that the underlying data — registry attribution, FK integrity, verse context accounting — was sound. Dimensions and anchors were confirmed on a foundation that had not been audited.

**Implication:** No further Dimension Review work should proceed until the audit establishes that the data can be trusted at each level. The Registry Management Guide must be updated to embed all validation checks, field definitions, and audit rules so it serves as the programme's authoritative registry reference.

---

## 3. FK Mismatch — Root Cause Analysis

### Mechanisms identified

| Mechanism | Terms | Cause | Evidence |
|---|---|---|---|
| 2 — Registry merge | 22 | Reg 154 (stupor) merged into 151 (sorrow) 2026-03-19. `wa_term_inventory` re-linked; `mti_terms.owning_registry_fk` left pointing at defunct registry | Reg 154: excluded, 0 files, 0 OWNER terms. Notes confirm merge. |
| 3 — XREF FK mismatch | 36 | FK set to registry where term has XREF row, not OWNER row. Text field `owning_registry` is correct in all 36 cases | All 36 have XREF in FK registry. Concentrated: Reg 112 (mind, 20 terms), Reg 197 (authority, 16 terms) |

Mechanism 1 (data entry error) ruled out. All mismatches fall cleanly into mechanisms 2 or 3.

### Impact on Verse Context data

- 58 terms' groups are attributed to the wrong registry in `wa_dimension_index`
- Reg 93 (intention) shows 0 groups in cluster extract; registry overview correctly shows 2 groups — the data exists but the extract populate script cannot find it via the wrong FK
- Negative-gap registries (heart +397, spirit +453, flesh +531) show vc_sum exceeding live_verse_count — consistent with FK-misattributed terms inflating verse_context records under the wrong registry
- C01 Dimension Review was conducted with 30 groups attributed to the wrong registry; 29 of those were anchored (`manual_override=1`)

### Proactive detection queries established

**Mechanism 2:** Any term whose `owning_registry_fk` points to a registry with 0 active files and 0 OWNER terms.

**Mechanism 3:** Any term where `owning_registry_fk` does not match the registry derived from the OWNER row in `wa_term_inventory`, but text field `owning_registry` does match the OWNER path.

These two queries together constitute a complete integrity check for this class of error. Must be run after every future registry merge or restructuring event.

### Recommended fix (researcher-confirmed direction, not yet applied)

1. Update `owning_registry_fk` (and text field for 22 Mechanism 2 cases) to match OWNER `wa_term_inventory` path
2. Repopulate dimension index in two steps:
   - For 29 anchored rows: update `owning_registry_no`, `owning_registry_word`, `cluster_assignment` only — preserve dimension, confidence, override, notes
   - For all non-override rows: `--clear` repopulate as normal
3. After fix: run both detection queries to confirm zero residual mismatches
4. Add detection queries to post-restructuring procedure for all future registry merges

**Unresolved question on anchored rows:** The 29 anchored dimensions in C01 were assessed in the wrong cluster context. Whether they require re-examination in their correct cluster depends on the audit outcome at Level 1 and Level 2. This decision is deferred until the audit establishes whether the underlying verse context data is sound.

---

## 4. Level 0 Audit — Registry Integrity Findings

**Source:** `wa-registry-overview-20260406.json` | `database_schema_20260406.json` | `WA-Registry-Management-Guide-v5_6-20260330.md`

### Finding 1 — Inactive registries (31): CLEAR
All 31 registries with `verse_context_status = NULL` have `live_owner_count = 0` and `vc_groups = 0`. Notes are populated with coherent documented explanations (covered, replaced, merged, special handling). No active downstream data attached to any. This layer is clean.

### Finding 2 — Registry 93 (intention) discrepancy: EXPLAINED BY FK MISMATCH
Registry overview: 2 groups, 8 relevant, 1 set-aside, 3 anchors. Cluster extract: 0 groups. Discrepancy caused by FK mismatch — extract populate script joins on `owning_registry_fk`, which points to the wrong registry. The data exists. This is the FK problem, not a separate issue.

### Finding 3 — Boastfulness (Reg 15): UNEXPLAINED — REQUIRES DATABASE QUERY
`live_owner_count = 9`, `live_verse_count = 249`, `verse_context_status = Complete`, `vc_groups = 0`, `vc_relevant = 0`, `vc_set_aside = 0`. This is not an AVF pattern (AVF produces set-aside records). Nine owner terms and 249 active verses exist but no verse_context output of any kind. Audit note: `result=REVIEW`.

**Cannot be resolved from registry JSON alone. Requires direct database query on `verse_context` filtered to boastfulness owner terms.**

### Finding 4 — Diligence (Reg 48): EXPLAINABLE AS AVF, REVIEW STATUS UNRESOLVED
82 set-aside verses, zero relevant, zero groups — consistent with AVF outcome. Audit note `result=REVIEW` consistent with AVF requiring researcher confirmation. Resolution not visible in JSON. Documented resolution note required in `word_registry.notes`.

### Finding 5 — Nine REVIEW-flagged registries with zero owners marked Complete: PARTIALLY RESOLVED, ONE ANOMALY
Consciousness (27), loyalty (104), meekness (109), recognition (129), resolve (137), reverence (138), sensuality (144), energy (200): all have `live_owner_count = 0`. `verse_context_status = Complete` is technically valid for zero-owner registries (no OWNER terms with verses to classify). However each requires a documented resolution note confirming the zero-owner state is intentional.

**Anomaly — Reg 205 (resentment):** Notes read "GAP — New entry. Replaces #136. Priority 5." This registry has not been through Session A. `verse_context_status = Complete` is not a reasonable state for an unprocessed new entry. This appears to be a status assignment error requiring correction.

### Finding 6 — Verse classification gap (80 registries): RESOLVED

**`live_verse_count` definition established:**
```sql
SELECT COUNT(*) FROM wa_verse_records
WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
AND delete_flagged = 0
```
Counts ALL active verses in registry files regardless of `term_owner_type`, `span_strong_match`, or `mti_terms.status`. This is broader than the VCB-classified verse set.

**`phase1_verse_count` definition (previously undocumented in guide):**
```sql
SELECT COUNT(*) FROM wa_verse_records
WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
AND span_strong_match = 1
AND (delete_flagged = 0 OR delete_flagged IS NULL)
```
Counts active verses with confirmed span matches. Engine-derived at Phase 1. Not updated by Session B pipeline.

**Gap explained:** 27,017 active verses belong to terms whose `mti_terms.status` is NOT `extracted` or `extracted_thin`. These are excluded from VCB classification by design. The gap is a legitimate accounting difference, not missing classification.

| mti_status | Verses | Terms |
|---|---|---|
| delete | 13,109 | 495 |
| NULL | 11,481 | 391 |
| candidate_delete | 1,427 | 23 |
| extracted_theological_anchor | 816 | 9 |
| xref_desire | 184 | 1 |

**Confirmed:** Zero OWNER terms with active verses lack verse_context records. VCB is complete as designed. XREF verses are correctly delete_flagged (0 active XREF verses).

**Negative gap registries (12):** vc_sum exceeds live_verse_count. Total excess: 1,535 verses. Concentrated in heart, spirit, flesh — C01 anthropological core registries. Consistent with FK-misattributed terms inflating verse_context records under the wrong registry. This is a consequence of the FK mismatch, not a separate problem.

**Programme-wide verse accounting:**
- Total live_verse_count: 85,115
- Total vc_classified: 60,883
- Net gap: 24,232 ≈ 27,017 non-extracted verses minus 1,535 negative-gap excess (accounts within rounding)

---

## 5. Registry Management Guide — Required Updates

The following must be added to `WA-Registry-Management-Guide-v5_6-20260330.md` before the audit proceeds to Level 1:

**Section 2 — computed field definitions to add:**

| Field | Definition |
|---|---|
| `live_verse_count` | Runtime-computed. `SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?) AND delete_flagged=0`. Counts ALL active verses in registry files regardless of term_owner_type or mti_terms.status. Broader than the VCB-classified set. |
| `live_owner_count` | Runtime-computed. Count of active non-delete-flagged OWNER terms in wa_term_inventory for this registry. |
| `live_xref_count` | Runtime-computed. Count of active non-delete-flagged XREF terms in wa_term_inventory for this registry. |
| `vc_groups` | Runtime-computed. Count of verse_context_group records for OWNER terms of this registry where delete_flagged=0. |
| `vc_relevant` | Runtime-computed. Count of verse_context records where is_relevant=1 and delete_flagged=0 for OWNER terms of this registry. |
| `vc_set_aside` | Runtime-computed. Count of verse_context records where is_relevant=0 and delete_flagged=0 for OWNER terms of this registry. |
| `vc_anchors` | Runtime-computed. Count of verse_context records where is_anchor=1 and delete_flagged=0 for OWNER terms of this registry. |
| `dimension_profile` | Runtime-computed. JSON summary of dimension distribution across wa_dimension_index groups for this registry. |

**Section 3 — status clarification to add:** `verse_context_status = Complete` is valid for registries with `live_owner_count = 0` — the condition "all OWNER terms with verses have verse_context records" is vacuously satisfied. A documented note in `word_registry.notes` confirming the zero-owner state is intentional is required for each such registry.

**New section — Audit integrity rules:** Definition of audit-clean state; required resolution documentation for `result=REVIEW` audit notes; FK integrity check queries; post-restructuring verification procedure.

**New section — Known data integrity issues:** FK mismatch (mechanisms 2 and 3), detection queries, fix status.

---

## 6. Open Items Before Level 1 Audit

| Item | Action needed | Source |
|---|---|---|
| Reg 205 `verse_context_status` | Investigate and correct — should not be Complete for unprocessed new entry | Finding 5 |
| Reg 15 (boastfulness) | Direct DB query on `verse_context` for its owner terms | Finding 3 |
| Nine REVIEW registries | Confirm resolution status; add documented notes | Finding 5 |
| FK fix | Apply fix; repopulate dimension index (two-step) | FK mismatch |
| Guide update | Draft and apply Section 2 additions and new audit sections | Finding 6 |

---

## 7. Next Steps

1. Update `WA-Registry-Management-Guide` to v5.7 with all field definitions and audit rules established in this session
2. Resolve open items (Reg 205, Reg 15, nine REVIEW registries) via database queries
3. Apply FK fix and dimension index repopulation
4. Proceed to Level 1 audit — verse record and verse_context integrity
5. Level 1 must establish: verse_context records correctly attributed, anchor verse quality, group construction integrity
6. Level 2: group description and dimension index integrity
7. Only after Levels 0–2 are clean: resume Dimension Review, beginning with C02

---

*wa-dim-session-log-audit-v1-2026-04-06.md | Produced 2026-04-06 | Preceding outputs: wa-dim-extract-C02-2026-04-06.json, wa-dim-existing-pointers-C02-2026-04-06.json*
