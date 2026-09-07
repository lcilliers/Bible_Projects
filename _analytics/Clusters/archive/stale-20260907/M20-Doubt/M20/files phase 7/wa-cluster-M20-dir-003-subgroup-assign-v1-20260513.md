# wa-cluster-M20-dir-003-subgroup-assign-v1-20260513

**DIRECTIVE ID:** DIR-20260513-003  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Directive type:** Sub-group assignment (§11.3)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Produced by:** Claude AI — M20 Session B Phase 4  
**Date:** 2026-05-13  
**Sequence note:** dir-001 = historical status-init; dir-002 = term-rebind (DIR-20260513-002, applied); dir-003 = this sub-group assignment.

---

## MOTIVATION

Phase 4 control read of M20 Doubt, Despair and Anxiety is complete. The cluster's 12 active terms (following removal of na.dad and apelpizo via DIR-20260513-002) have been analytically grouped into four sub-groups through the characteristic debate (Phase 3, `WA-M20-characteristic-debate-v1-20260513.md`) and validated by the bidirectional control read (Phase 4, `wa-obslog-M20-m20-doubt-v1-20260513.md`).

No `cluster_subgroup` rows exist for M20. This directive instructs CC to create those rows and assign each of the 12 terms to its sub-group via the `mti_term_subgroup` join table (the m:n structure confirmed in DIR-20260513-002's apply notes — `mti_terms.cluster_subgroup_id` does not exist post-M46).

---

## SCOPE

**Tables affected:**
1. `cluster_subgroup` — INSERT four new rows (one per sub-group M20-A through M20-D)
2. `mti_term_subgroup` — INSERT twelve rows (one per term, linking term to sub-group)

**Cluster:** M20

**Sub-groups to create:**

| Sub-group code | Label | Terms (Strong's) | Term count |
|---|---|---|---|
| M20-A | Anxiety and Worry | H1672, G3309, G3308 | 3 |
| M20-B | Despair and Hopelessness | H2976, G1820 | 2 |
| M20-C | Discouragement and Loss of Heart | G1573, H3512A, H3512B, G0120, G3642 | 5 |
| M20-D | Doubt and Indecision | G1365, G1374 | 2 |

**Term-to-sub-group mapping (all Strong's to be resolved by CC to mti_id):**

| Strong's | Transliteration | Sub-group |
|---|---|---|
| H1672 | da.ag | M20-A |
| G3309 | merimnaō | M20-A |
| G3308 | merimna | M20-A |
| H2976 | ya.ash | M20-B |
| G1820 | exaporeō | M20-B |
| G1573 | ekkakeō | M20-C |
| H3512A | ka.ah | M20-C |
| H3512B | ka.eh | M20-C |
| G0120 | athumeō | M20-C |
| G3642 | oligopsuchos | M20-C |
| G1365 | distazō | M20-D |
| G1374 | dipsuchos | M20-D |

**Note on schema:** `mti_terms.cluster_subgroup_id` does not exist (removed in M46). Sub-group membership is recorded in `mti_term_subgroup` (m:n). CC to inspect `mti_term_subgroup` schema to confirm column names before writing.

**Note on strongs_number format:** H3512A and H3512B are split entries from the same root. CC to confirm the exact strongs_number values in `mti_terms` for these two terms before writing.

**Out of scope:** verse_context rows, verse_context_group rows, cluster_finding rows, any patch operations. This directive creates sub-group structure and term assignments only.

---

## OUTCOME REQUIRED

After execution:

1. Four `cluster_subgroup` rows exist for cluster_code='M20' with subgroup_codes M20-A, M20-B, M20-C, M20-D and labels as specified above
2. Twelve `mti_term_subgroup` rows link the 12 terms to their sub-groups (one row per term)
3. No term in M20 is unassigned (every mti_terms row with cluster_code='M20' has a corresponding mti_term_subgroup row)
4. No term from another cluster is assigned to an M20 sub-group
5. na.dad (H5074) and apelpizo (G0560) have no mti_term_subgroup rows for M20 sub-groups (they are in M18; confirmed already clean per DIR-20260513-002 notes)

---

## COMPLETION CONFIRMATION

CC to provide:

```sql
-- 1. Confirm sub-group rows created
SELECT subgroup_code, label, cluster_code
FROM cluster_subgroup
WHERE cluster_code = 'M20'
ORDER BY subgroup_code;
-- Expected: 4 rows — M20-A, M20-B, M20-C, M20-D

-- 2. Confirm term assignments
SELECT cs.subgroup_code, mt.strongs_number, mt.transliteration
FROM mti_term_subgroup mts
JOIN mti_terms mt ON mt.id = mts.mti_term_id
JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
WHERE cs.cluster_code = 'M20'
ORDER BY cs.subgroup_code, mt.strongs_number;
-- Expected: 12 rows matching the term-to-sub-group mapping above

-- 3. Confirm no M20 terms unassigned
SELECT mt.strongs_number
FROM mti_terms mt
LEFT JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
    AND mts.cluster_subgroup_id IN (
        SELECT id FROM cluster_subgroup WHERE cluster_code = 'M20'
    )
WHERE mt.cluster_code = 'M20'
  AND COALESCE(mt.delete_flagged, 0) = 0
  AND mts.mti_term_id IS NULL;
-- Expected: 0 rows (no unassigned terms)

-- 4. Confirm term counts per sub-group
SELECT cs.subgroup_code, COUNT(*) as term_count
FROM mti_term_subgroup mts
JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
WHERE cs.cluster_code = 'M20'
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
-- Expected: M20-A=3, M20-B=2, M20-C=5, M20-D=2
```

---

*wa-cluster-M20-dir-003-subgroup-assign-v1-20260513 | DIR-20260513-003 | Sub-group assignment for M20 Doubt, Despair and Anxiety — 4 sub-groups, 12 terms | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
