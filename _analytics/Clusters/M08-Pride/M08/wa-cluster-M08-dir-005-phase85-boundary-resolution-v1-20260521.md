# wa-cluster-M08-dir-005-phase85-boundary-resolution-v1-20260521

> Cluster directive — M08 Phase 8.5 BOUNDARY resolution
> Cluster: M08 — Pride, Arrogance and Boasting
> Date: 2026-05-21
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §11A

---

## MOTIVATION

Phase 3 verdicts placed one term — **G0193 akratēs** (intemperate, mti_id=1113, 1 verse at 2Ti 3:3, vc_id=36675) — at BOUNDARY under §6.3.1 reason 3 (supportive/qualifying register). Phase 5 v2 routed the BOUNDARY verse to its own sub-group `M08-BOUNDARY` with VCG `M08-BOUNDARY-VCG-01`, awaiting researcher disposition.

**Researcher decision (2026-05-21): PROMOTE-TO-SUBGROUP.** Keep G0193 in M08 as the *enabling-condition register* through which CHAR-1 (Arrogant self-elevation) operates unchecked. The single verse (2Ti 3:3) sits in the same vice catalogue as `filautos` (2Ti 3:2) and `huperēfanos` (2Ti 3:2) — already routed at Phase 7 to **M08-A4-VCG-01** ("Self-Love as Root and NT Vice-Catalogue Pride"). The akratēs verse is the immediate continuation of that catalogue and belongs in the same VCG.

The rationale aligns with the AI's Phase 3 framing: *"lack of self-control appears as the breakdown of inner discipline through which pride operates unchecked: it is the enabling condition rather than the characteristic itself."* This makes it analytically a qualifying-supportive verse for CHAR-1's NT vice-catalogue register — exactly what M08-A4-VCG-01 represents.

## OPERATIONS

### Op A — Reroute vc_id=36675 to M08-A4 / M08-A4-VCG-01

```sql
UPDATE verse_context
SET cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-A4' AND COALESCE(delete_flagged,0)=0),
    group_id = (SELECT id FROM verse_context_group WHERE group_code='M08-A4-VCG-01' AND COALESCE(delete_flagged,0)=0)
WHERE id = 36675 AND COALESCE(delete_flagged,0)=0;
```

### Op B — Update mti_term_subgroup link for G0193

Change the existing link from M08-BOUNDARY → M08-A4 with placement_note reflecting promotion.

```sql
UPDATE mti_term_subgroup
SET cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-A4' AND COALESCE(delete_flagged,0)=0),
    placement_note = '[primary] 1 verse — promoted from BOUNDARY at Phase 8.5 (per dir-005); supportive/qualifying register for CHAR-1 NT vice catalogue',
    last_updated_date = ?
WHERE mti_term_id = 1113
  AND cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY' AND COALESCE(delete_flagged,0)=0);
```

### Op C — Insert vcg_term link for G0193 in M08-A4-VCG-01

```sql
INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date)
VALUES (
  (SELECT id FROM verse_context_group WHERE group_code='M08-A4-VCG-01'),
  1113,
  'Phase 8.5 promotion from M08-BOUNDARY',
  0, ?, ?
);
```

### Op D — Soft-delete M08-BOUNDARY-VCG-01 + its vcg_term link

```sql
-- Soft-delete the VCG
UPDATE verse_context_group
SET delete_flagged = 1,
    notes = 'Dissolved at M08 Phase 8.5 ' || ? || ' (BOUNDARY resolved — G0193 promoted to M08-A4; per dir-005)'
WHERE group_code = 'M08-BOUNDARY-VCG-01' AND COALESCE(delete_flagged,0)=0;

-- Soft-delete the vcg_term link
UPDATE vcg_term
SET delete_flagged = 1, last_updated_date = ?
WHERE vcg_id = (SELECT id FROM verse_context_group WHERE group_code='M08-BOUNDARY-VCG-01')
  AND COALESCE(delete_flagged,0)=0;
```

### Op E — Soft-delete M08-BOUNDARY cluster_subgroup row

```sql
UPDATE cluster_subgroup
SET delete_flagged = 1,
    notes = 'Dissolved at M08 Phase 8.5 ' || ? || ' (BOUNDARY resolved — G0193 promoted to M08-A4; per dir-005)',
    last_updated_date = ?
WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY' AND COALESCE(delete_flagged,0)=0;
```

## OUTCOME REQUIRED

- vc_id=36675 (G0193 akratēs at 2Ti 3:3) now lives in M08-A4 / M08-A4-VCG-01.
- M08-A4-VCG-01 verse count: 10 → 11.
- M08-A4 sub-group total: 68 → 69 verses.
- G0193 `mti_term_subgroup` link points to M08-A4 (1 row).
- New `vcg_term` link: (M08-A4-VCG-01, mti_id=1113) inserted.
- M08-BOUNDARY-VCG-01 + M08-BOUNDARY cluster_subgroup rows soft-deleted.
- M08 active sub-group count: 9 → 8 (M08-A1, A2, A3, A4, B, C, D, E).
- M08 active VCG count: 25 → 24.
- M08 substantive corpus unchanged at 293 verses (BOUNDARY's 1 verse was already in is_relevant=1 substantive count).

## COMPLETION CONFIRMATION

```sql
-- 0 (no active M08-BOUNDARY)
SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY' AND COALESCE(delete_flagged,0)=0;

-- 1 (vc routed to M08-A4-VCG-01)
SELECT cs.subgroup_code, vcg.group_code FROM verse_context vc
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.id = 36675;
-- expected: 'M08-A4', 'M08-A4-VCG-01'

-- 11 (new M08-A4-VCG-01 count)
SELECT COUNT(*) FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vcg.group_code='M08-A4-VCG-01' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0;

-- 8 (active M08 sub-groups, M08-BOUNDARY excluded)
SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0;
```

## ROLLBACK

```sql
-- Reverse Op E
UPDATE cluster_subgroup SET delete_flagged=0, notes=NULL WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY';

-- Reverse Op D
UPDATE verse_context_group SET delete_flagged=0, notes=NULL WHERE group_code='M08-BOUNDARY-VCG-01';
UPDATE vcg_term SET delete_flagged=0 WHERE vcg_id = (SELECT id FROM verse_context_group WHERE group_code='M08-BOUNDARY-VCG-01');

-- Reverse Op C
DELETE FROM vcg_term WHERE vcg_id = (SELECT id FROM verse_context_group WHERE group_code='M08-A4-VCG-01') AND mti_term_id=1113 AND placement_note LIKE 'Phase 8.5 promotion%';

-- Reverse Op B
UPDATE mti_term_subgroup SET cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY'), placement_note='[primary] 1 verses' WHERE mti_term_id=1113 AND cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-A4');

-- Reverse Op A
UPDATE verse_context SET cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY'), group_id = (SELECT id FROM verse_context_group WHERE group_code='M08-BOUNDARY-VCG-01') WHERE id = 36675;
```

## SCRIPT

`scripts/_apply_m08_phase85_boundary_resolution_20260521.py` — runs Op A / B / C / D / E with pre/post checks.

---

*Phase 8.5 directive. BOUNDARY resolved by PROMOTE-TO-SUBGROUP — G0193 akratēs joins M08-A4-VCG-01 (NT vice-catalogue register) where it sits in scriptural context (2Ti 3:2-3) with filautos and huperēfanos. The cluster proceeds to Phase 8.7 with 8 sub-groups, 24 VCGs, 293 verses.*
