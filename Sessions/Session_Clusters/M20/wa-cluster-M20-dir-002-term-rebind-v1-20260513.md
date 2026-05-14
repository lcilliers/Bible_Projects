# wa-cluster-M20-dir-002-term-rebind-v1-20260513

**DIRECTIVE ID:** DIR-20260513-002  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Directive type:** Cluster reassignment (§11.6)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Produced by:** Claude AI — M20 Session B Phase 4  
**Date:** 2026-05-13  

---

## MOTIVATION

Phase 4 control read of M20 Doubt, Despair and Anxiety has identified two terms whose inner-being content does not fit M20 and requires reassignment to M18 (Hope, Expectation and Waiting).

**H5074 na.dad (mti_id=5571):** The researcher's direction (wa-cluster-M20-phase4-resolution-items-v1-20260513.md, 2026-05-13) identifies na.dad as the inner-being opposite of hope — restlessness, sleep fleeing, spiritual straying — rather than a primary doubt/despair/anxiety term. The researcher explicitly distinguishes na.dad from its root-NADAD siblings (H5076, H5079, H5206) which carry impurity/defilement content. na.dad's correct analytical home is M18 as the experiential absence of rest and hope. Its current cluster_code (M20) is incorrect.

**G0560 apelpizo (mti_id=808 — note: mti_id to be confirmed by CC against strongs_number='G0560'):** The term's gloss "to despair" appears in M20 but its sole verse (Luk 6:35) and its Mounce definition ("to expect nothing in return") carry a positive inner-being posture — the absence of self-directed hope as the disposition of generous love. This is not distress vocabulary. The researcher's direction places it in M18 with the retention note: "absence of self-directed hope as posture of genuine love." Its current cluster_code (M20) is incorrect.

Both reassignments move M20 → M18. Both can be executed in a single operation.

---

## SCOPE

**Tables affected:** `mti_terms` only (column `cluster_code`; column `cluster_subgroup_id` if currently set — both terms were in BOUNDARY in M20 with no sub-group assigned, so `cluster_subgroup_id` is expected to be null; CC to verify).

**Term set:**

| Strong's | Transliteration | mti_id | Current cluster_code | Target cluster_code |
|---|---|---|---|---|
| H5074 | na.dad | 5571 | M20 | M18 |
| G0560 | apelpizo | (CC to confirm) | M20 | M18 |

**Note on na.dad verse_context rows:** The 13 Phase-2 set-aside verse_context rows (mti_term_id=5571, is_relevant=0, applied in PATCH-20260513-M20-VCNEW-UTREVIEW-V1) follow the term implicitly — they reference mti_term_id, not cluster_code. No verse_context update is required for the set-aside rows. The 13 G-status verse_context rows (vcg_id=1306, all is_relevant=1) similarly follow the term — no verse_context update required.

**Note on VCG row for na.dad:** vcg_id=1306, group_code=5571-001 is term-scoped (5571-prefix). It follows the term to M18. No rename or migration required.

**Note on na.dad G-status verses:** The proposed VCREVISE set-aside patch for G-status verses is CANCELLED per researcher direction. The 13 G-status verses remain is_relevant=1 and follow the term to M18.

**Out of scope:** verse_context rows, verse_context_group rows, cluster_finding rows, any patch operations. This directive is mti_terms.cluster_code updates only.

---

## OUTCOME REQUIRED

After execution:

1. `mti_terms.cluster_code = 'M18'` for strongs_number = 'H5074'
2. `mti_terms.cluster_code = 'M18'` for strongs_number = 'G0560'
3. `mti_terms.cluster_subgroup_id = null` for both terms (expected already null; confirm)
4. M20 active term count decreases by 2 (from 14 to 12)
5. M18 active term count increases by 2
6. All verse_context rows for mti_term_id=5571 remain unchanged (count: 26 total — 13 set-aside + 13 G-status)
7. vcg_id=1306 (group_code=5571-001) remains unchanged

---

## COMPLETION CONFIRMATION

CC to provide:

```sql
-- 1. Confirm reassignment
SELECT strongs_number, cluster_code, cluster_subgroup_id
FROM mti_terms
WHERE strongs_number IN ('H5074', 'G0560');
-- Expected: both rows show cluster_code='M18', cluster_subgroup_id=null

-- 2. Confirm M20 term count post-reassignment
SELECT COUNT(*) FROM mti_terms
WHERE cluster_code = 'M20' AND COALESCE(delete_flagged, 0) = 0;
-- Expected: 12

-- 3. Confirm verse_context rows for na.dad unchanged
SELECT COUNT(*) FROM verse_context
WHERE mti_term_id = 5571 AND COALESCE(delete_flagged, 0) = 0;
-- Expected: 26

-- 4. Confirm VCG for na.dad intact
SELECT id, group_code, cluster_code FROM verse_context_group
WHERE id = 1306;
-- Expected: id=1306, group_code='5571-001', cluster_code updated to M18
-- (or cluster_code field not present on verse_context_group — CC to confirm schema)
```

---

*wa-cluster-M20-dir-002-term-rebind-v1-20260513 | DIR-20260513-002 | Cluster reassignment M20 → M18 for H5074 na.dad and G0560 apelpizo | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
