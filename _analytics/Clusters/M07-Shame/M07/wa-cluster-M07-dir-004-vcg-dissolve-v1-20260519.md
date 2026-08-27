# wa-cluster-M07-dir-004-vcg-dissolve-v1-20260519

> Cluster directive — M07 Phase 8 inherited-VCG dissolution
> Cluster: M07 — Shame, Disgrace and Humiliation
> Date: 2026-05-19
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §11

---

## MOTIVATION

Phase 7 created 29 new M07 VCGs and migrated every is_relevant verse (363) via `verse_context.group_id`. Per §11.2, 40 inherited VCGs remain — linked to M07 mti_terms via `vcg_term` but with `group_code` patterns from pre-cluster-pivot Session B (`244-001`, `313-002`, `1135-001`, etc. — registry-id–based codes from the original word registries).

Comparison report ([WA-M07-vcg-dissolution-comparison-v1-20260519.md](WA-M07-vcg-dissolution-comparison-v1-20260519.md)) confirms:

- **40 inherited VCGs total**
- **40 of 40 already empty** — 0 active `verse_context` rows point at any of them
- **Uniform disposition: OBSOLETE** — the inherited framings reflect Session B work on the original word registries; they have no analogue in M07's new meaning-derived VCG structure

Soft-delete is safe; no analytical loss; descriptions remain queryable for audit reference.

## OPERATIONS

### Op A — Soft-delete inherited `verse_context_group` rows (×40)

```sql
UPDATE verse_context_group
SET delete_flagged = 1,
    notes = 'Dissolved at M07 Phase 8 ' || COALESCE(?, '') || ' (replaced by M07-*-VCG-NN; per dir-004)'
WHERE id IN (<40 inherited vcg ids>)
  AND COALESCE(delete_flagged,0) = 0;
```

### Op B — Soft-delete `vcg_term` links to inherited VCGs

```sql
UPDATE vcg_term
SET delete_flagged = 1
WHERE vcg_id IN (<40 inherited vcg ids>)
  AND COALESCE(delete_flagged,0) = 0;
```

## OUTCOME REQUIRED

- 40 `verse_context_group.delete_flagged = 1` UPDATEs.
- All `vcg_term` rows referencing those VCGs have `delete_flagged = 1`.
- M07's active VCG count = 29 (Phase 7 set; no inherited remain).
- 0 inherited VCG rows linked to M07 in the active set.
- H5 health check (orphan VCG with no active vc references) clean across the dissolved set.

## COMPLETION CONFIRMATION

```sql
-- 0
SELECT COUNT(*) FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id = vcg.id
JOIN mti_terms mt ON mt.id = vt.mti_term_id
WHERE mt.cluster_code='M07'
  AND COALESCE(vcg.delete_flagged,0)=0
  AND COALESCE(vt.delete_flagged,0)=0
  AND NOT (vcg.group_code LIKE 'M07%-VCG-%');

-- 29
SELECT COUNT(*) FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id = vcg.id
JOIN mti_terms mt ON mt.id = vt.mti_term_id
WHERE mt.cluster_code='M07'
  AND COALESCE(vcg.delete_flagged,0)=0
  AND COALESCE(vt.delete_flagged,0)=0
  AND vcg.group_code LIKE 'M07%-VCG-%';
```

## ROLLBACK

```sql
UPDATE vcg_term SET delete_flagged=0 WHERE vcg_id IN (<inherited ids>);
UPDATE verse_context_group SET delete_flagged=0, notes=NULL WHERE id IN (<inherited ids>);
```

## SCRIPT

`scripts/_apply_m07_phase8_vcg_dissolve_20260519.py` — runs both operations with pre/post checks.

---

*Phase 8 directive. Researcher-gate satisfied: 40/40 inherited VCGs are empty (Phase 7 verified 0 is_relevant verses point at them).*
