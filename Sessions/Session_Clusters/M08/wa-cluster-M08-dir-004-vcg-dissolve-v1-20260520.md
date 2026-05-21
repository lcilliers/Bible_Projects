# wa-cluster-M08-dir-004-vcg-dissolve-v1-20260520

> Cluster directive — M08 Phase 8 inherited-VCG dissolution
> Cluster: M08 — Pride, Arrogance and Boasting
> Date: 2026-05-21
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §11

---

## MOTIVATION

Phase 7 created 25 new M08 VCGs and migrated every is_relevant verse (293) via `verse_context.group_id`. Per §11.2, **61 inherited VCGs** remain — linked to M08 mti_terms via `vcg_term` but with `group_code` patterns from pre-cluster-pivot Session B (`100-001`, `1113-001`, `1587-001`, `26-001`, etc. — registry-id–based codes from the original word registries: pride reg#100, ambition reg#3, boldness reg#16, etc.).

**Pre-state check:** 61 inherited VCGs / 0 is_relevant verses still reference them. Dissolution is safe — no analytical loss; descriptions remain queryable for audit reference via the soft-delete pattern.

Uniform disposition: **OBSOLETE**. Inherited framings reflect pre-cluster Session B work on the original 13 contributing registries; they have no analogue in M08's new meaning-derived VCG structure.

## OPERATIONS

### Op A — Soft-delete inherited `verse_context_group` rows (×61)

```sql
UPDATE verse_context_group
SET delete_flagged = 1,
    notes = 'Dissolved at M08 Phase 8 ' || ? || ' (replaced by M08-*-VCG-NN; per dir-004)'
WHERE id IN (<61 inherited vcg ids>)
  AND COALESCE(delete_flagged,0) = 0;
```

### Op B — Soft-delete `vcg_term` links to inherited VCGs

```sql
UPDATE vcg_term
SET delete_flagged = 1, last_updated_date = ?
WHERE vcg_id IN (<61 inherited vcg ids>)
  AND COALESCE(delete_flagged,0) = 0;
```

## OUTCOME REQUIRED

- 61 `verse_context_group.delete_flagged = 1` UPDATEs.
- All `vcg_term` rows referencing those VCGs have `delete_flagged = 1`.
- M08's active VCG count = 25 (Phase 7 set; no inherited remain).
- 0 inherited VCG rows linked to M08 in the active set.

## COMPLETION CONFIRMATION

```sql
-- 0 (no inherited remain active)
SELECT COUNT(*) FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id = vcg.id
JOIN mti_terms mt ON mt.id = vt.mti_term_id
WHERE mt.cluster_code='M08'
  AND COALESCE(vcg.delete_flagged,0)=0
  AND COALESCE(vt.delete_flagged,0)=0
  AND NOT (vcg.group_code LIKE 'M08-%-VCG-%');

-- 25 (Phase 7 VCGs still active)
SELECT COUNT(DISTINCT vcg.id) FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id = vcg.id
JOIN mti_terms mt ON mt.id = vt.mti_term_id
WHERE mt.cluster_code='M08'
  AND COALESCE(vcg.delete_flagged,0)=0
  AND COALESCE(vt.delete_flagged,0)=0
  AND vcg.group_code LIKE 'M08-%-VCG-%';
```

## ROLLBACK

```sql
UPDATE vcg_term SET delete_flagged=0 WHERE vcg_id IN (<inherited ids>);
UPDATE verse_context_group SET delete_flagged=0, notes=NULL WHERE id IN (<inherited ids>);
```

## SCRIPT

`scripts/_apply_m08_phase8_vcg_dissolve_20260520.py` — runs both operations with pre/post checks.

---

*Phase 8 directive. All 61 inherited VCGs verified empty (0 is_relevant references) prior to dissolution.*
