# wa-cluster-M20-dir-008-M20-D-mapping-v1-20260513

**DIRECTIVE ID:** DIR-20260513-008  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Sub-group:** M20-D — Doubt and Indecision  
**Directive type:** Group-verse mapping apply (§10.4 / §11.4)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Source mapping:** WA-M20-D-group-verse-mapping-v1-20260513.md  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Date:** 2026-05-13  

---

## MOTIVATION

Phase 6 VCG reconciliation for M20-D (Doubt and Indecision) is complete. The mapping document `WA-M20-D-group-verse-mapping-v1-20260513.md` specifies reconciliation decisions for all 2 existing VCGs covering 4 connected verse_context rows.

The mapping produces: 2 REFINE only. No new VCGs, no splits, no soft-deletes. Net: 2 existing → 2 VCGs (descriptions updated). 0 set-asides. This is the simplest directive in the M20 Phase 7 sequence.

---

## SCOPE

**Cluster:** M20 | **Sub-group:** M20-D | **Terms:** G1365 distazō, G1374 dipsuchos

---

### Operation set 1 — REFINE only

| Group id | Current code | Refined description |
|---|---|---|
| 1792 | 1398-001 | Double-mindedness as dispositional indecision — the inner person not settling, not committing, hedging between two orientations; the consequence is instability across all of life (Jam 1:8); the remedy is purification of the heart as the seat of inner orientation (Jam 4:8) |
| 3060 | 1288-001 | Doubt as situational faith-wavering — the inner person failing to complete the move from seeing to trusting in a specific encounter; addressed directly by Jesus (Mat 14:31); coexisting with worship in the same group at the resurrection appearance (Mat 28:17) |

---

### Operation set 2 — verse_context UPSERT (anchor confirmation only)

All 4 verse_context rows retain their existing group_id. Confirm and set is_anchor per mapping:

| Reference | Term (strongs) | Group id | is_anchor |
|---|---|---|---|
| Jam 4:8 | G1374 | 1792 (1398-001) | 0 |
| Jam 1:8 | G1374 | 1792 (1398-001) | 1 |
| Mat 14:31 | G1365 | 3060 (1288-001) | 1 |
| Mat 28:17 | G1365 | 3060 (1288-001) | 0 |

Note: Jam 1:8 is designated as anchor (not Jam 4:8). CC to confirm current anchor state and update if needed.

Set-asides: none.

---

## OUTCOME REQUIRED

| VCG | Code | Verses | Anchors |
|---|---|---|---|
| id=1792 | 1398-001 (REFINE) | 2 | 1 (Jam 1:8) |
| id=3060 | 1288-001 (REFINE) | 2 | 1 (Mat 14:31) |
| **Total** | | **4** | **2** |

Soft-deleted VCGs: 0. Dual assignments: 0.

---

## COMPLETION CONFIRMATION

```sql
-- 1. Verse count and anchors per VCG (M20-D)
SELECT vcg.group_code, vcg.id,
       COUNT(vc.id) as verse_count,
       SUM(vc.is_anchor) as anchor_count
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.strongs_number IN ('G1365','G1374')
  AND COALESCE(vcg.delete_flagged, 0) = 0
GROUP BY vcg.id, vcg.group_code;
-- Expected: 2 rows; each verse_count=2, anchor_count=1

-- 2. Confirm anchor assignments
SELECT vr.reference, vc.is_anchor, vcg.group_code
FROM verse_context vc
JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vcg.id IN (1792, 3060)
ORDER BY vcg.id, vc.is_anchor DESC;
-- Expected: Jam 1:8 is_anchor=1 in 1792; Mat 14:31 is_anchor=1 in 3060

-- 3. Confirm descriptions updated
SELECT id, group_code, context_description
FROM verse_context_group WHERE id IN (1792, 3060);
-- Expected: descriptions match refined text above

-- 4. No soft-deletes (VCG count unchanged)
SELECT COUNT(*) FROM verse_context_group
WHERE COALESCE(delete_flagged, 0) = 0
  AND id IN (1792, 3060);
-- Expected: 2
```

CC to save application report to: `Sessions/Session_Clusters/M20/WA-M20-D-group-mapping-applied-v1-20260513.md`

---

*wa-cluster-M20-dir-008-M20-D-mapping-v1-20260513 | DIR-20260513-008 | M20-D group-verse mapping apply | 2 REFINE only | 4 verses | 0 set-asides | No new VCGs | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
