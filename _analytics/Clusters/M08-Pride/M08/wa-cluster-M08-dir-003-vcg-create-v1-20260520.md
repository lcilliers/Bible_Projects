# wa-cluster-M08-dir-003-vcg-create-v1-20260520

> Cluster directive — M08 Phase 7 VCG creation + verse routing + anchor reset
> Cluster: M08 — Pride, Arrogance and Boasting
> Date: 2026-05-20
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

---

## MOTIVATION

Phase 7 AI session designed **25 VCGs across 9 sub-groups** for the 296 substantive M08 verses. Validation passed (`scripts/_validate_m08_phase7_vcg_output_20260520.py`): all per-sub-group sums match DB, all 25 anchors are in their VCG's `verses` array, no duplicate vc_ids, BOUNDARY VCG correctly contains the 1 BOUNDARY verse, M22 (M08-C) and M23 (M08-E) cross-register flags are preserved in VCG descriptions.

Sources:
- Per-sub-group designs (9): [Sessions/Session_Clusters/M08/files phase 7/](files%20phase%207/)
- Unified JSON: [Sessions/Session_Clusters/M08/WA-M08-vcg-creation-v1-20260520.json](WA-M08-vcg-creation-v1-20260520.json)
- Validator: `scripts/_validate_m08_phase7_vcg_output_20260520.py` (PASSED 2026-05-21)

VCG breakdown:

| Sub-group | VCGs | Verses |
|---|---:|---:|
| M08-A1 (heart-elevation) | 3 | 32 |
| M08-A2 (eyes/outward bearing) | 2 | 11 |
| M08-A3 (national/collective) | 4 | 40 |
| M08-A4 (general dispositional) | 5 | 68 |
| M08-B (presumptuous defiance) | 3 | 45 |
| M08-C (boasting; **M22 flag**) | 3 | 70 |
| M08-D (vain conceit) | 2 | 12 |
| M08-E (pride of power; **M23 flag**) | 2 | 17 |
| M08-BOUNDARY | 1 | 1 |
| **Total** | **25** | **296** |

---

## SCOPE

### Operation A — INSERT verse_context_group rows (25)

```sql
INSERT INTO verse_context_group (group_code, context_description, vertical_pass_flag)
VALUES (?, ?, 0);
```

Insert 25 rows with `group_code` = each VCG's provisional_code (e.g. `M08-A1-VCG-01`) and `context_description` = each VCG's description from the JSON.

Pre-check: `SELECT COUNT(*) FROM verse_context_group WHERE group_code LIKE 'M08-%-VCG-%' AND COALESCE(delete_flagged,0)=0` → 0.
Post-check: → 25.

### Operation B — INSERT vcg_term link rows

For every distinct `(vcg_id, mti_term_id)` pair where the VCG covers at least one verse of the term, insert one `vcg_term` row.

```sql
INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date)
VALUES (?, ?, 'Phase 7 routing', 0, ?, ?);
```

### Operation C — UPDATE verse_context.group_id

For every is_relevant=1 vc_id in the JSON, set `group_id` to the new VCG's id.

```sql
UPDATE verse_context SET group_id=?
WHERE id=? AND COALESCE(delete_flagged,0)=0;
```

296 UPDATE statements expected.

### Operation D — Anchor reset

Two-step:

1. Clear all prior `is_anchor=1` on M08 is_relevant vc rows (95 prior anchors from inherited structure, all on previous VCG design before the Phase 5–6 restructure).
2. Set `is_anchor=1` on the 25 new Phase 7 anchors (one per VCG, per JSON).

```sql
-- Step 1
UPDATE verse_context SET is_anchor=0
WHERE id IN (
    SELECT vc.id FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code='M08' AND vc.is_anchor=1
      AND COALESCE(vc.delete_flagged,0)=0
);

-- Step 2 (×25)
UPDATE verse_context SET is_anchor=1
WHERE id=? AND COALESCE(delete_flagged,0)=0;
```

---

## OUTCOME REQUIRED

- 25 new `verse_context_group` rows (group_code `M08-{X}-VCG-NN`).
- N `vcg_term` links inserted (one per distinct VCG/term covered).
- 296 `verse_context.group_id` populated (no is_relevant=1 M08 vc with group_id pointing to anything other than a new M08-{X}-VCG-NN).
- 25 `verse_context.is_anchor=1` rows on M08 verses (was 95 inherited anchors, now 25 Phase 7 anchors).
- Inherited VCGs still in DB (Phase 8 dissolves them).

## COMPLETION CONFIRMATION

```sql
-- 25 new VCGs
SELECT COUNT(*) FROM verse_context_group
WHERE group_code LIKE 'M08-%-VCG-%' AND COALESCE(delete_flagged,0)=0;

-- 296 routed to new VCGs
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE mt.cluster_code='M08' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0
  AND vcg.group_code LIKE 'M08-%-VCG-%';

-- 25 anchors
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M08' AND vc.is_anchor=1
  AND COALESCE(vc.delete_flagged,0)=0;
```

## ROLLBACK

```sql
-- Reverse anchors
UPDATE verse_context SET is_anchor=0
WHERE id IN (
    SELECT vc.id FROM verse_context vc
    JOIN verse_context_group vcg ON vcg.id = vc.group_id
    WHERE vcg.group_code LIKE 'M08-%-VCG-%'
);

-- Reverse group_id (back to inherited VCGs lost — full rollback requires Phase 6 redo)
UPDATE verse_context SET group_id=NULL
WHERE group_id IN (SELECT id FROM verse_context_group WHERE group_code LIKE 'M08-%-VCG-%');

-- Delete vcg_term + verse_context_group
DELETE FROM vcg_term
WHERE vcg_id IN (SELECT id FROM verse_context_group WHERE group_code LIKE 'M08-%-VCG-%');

DELETE FROM verse_context_group WHERE group_code LIKE 'M08-%-VCG-%';
```

## SCRIPT

`scripts/_apply_m08_phase7_vcg_create_20260520.py` — runs Op A / B / C / D with pre/post checks.

---

*M08 Phase 7 VCG creation directive. Cross-register flags (M22 on M08-C, M23 on M08-E) preserved in VCG context_descriptions for Phase 9 catalogue consumption. Inherited VCGs still present in DB — Phase 8 dissolves them.*
