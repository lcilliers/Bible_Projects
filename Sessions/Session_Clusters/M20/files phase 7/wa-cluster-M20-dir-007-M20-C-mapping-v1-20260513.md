# wa-cluster-M20-dir-007-M20-C-mapping-v1-20260513

**DIRECTIVE ID:** DIR-20260513-007  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Sub-group:** M20-C — Discouragement and Loss of Heart  
**Directive type:** Group-verse mapping apply (§10.4 / §11.4)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Source mapping:** WA-M20-C-group-verse-mapping-v1-20260513.md  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Date:** 2026-05-13  

---

## MOTIVATION

Phase 6 VCG reconciliation for M20-C (Discouragement and Loss of Heart) is complete. The mapping document `WA-M20-C-group-verse-mapping-v1-20260513.md` specifies reconciliation decisions for all 5 existing VCGs covering 15 verse_context rows (12 unique verses; 3 verses shared between ka.ah and ka.eh terms, producing dual-term rows).

The mapping produces: 2 REFINE, 3 SPLIT (→5 NEW). Net: 5 existing → 7 VCGs post-apply. 0 set-asides.

**Critical pre-flight note:** Three verses (Psa 109:16, Eze 13:22, Dan 11:30) appear in both the ka.ah group (574-001, id=2739) and the ka.eh group (1700-001, id=1014) — 6 verse_context rows across two terms. After the splits, these 6 rows must be assigned to the correct new groups. CC must confirm that both the ka.ah and ka.eh vc rows for each shared verse are migrated together to the same new group.

---

## SCOPE

**Cluster:** M20 | **Sub-group:** M20-C | **Terms:** G0120 athumeō, G1573 ekkakeō, G3642 oligopsuchos, H3512A ka.ah, H3512B ka.eh

**Schema note:** CC to confirm exact strongs_number values for H3512A and H3512B in mti_terms before writing (noted as split entries in prior directive work). Also confirm `verse_context.cluster_subgroup_id` existence post-M46.

---

### Operation set 1 — REFINE

| Group id | Current code | Refined description |
|---|---|---|
| 489 | 2078-001 | Discouragement as the inner state produced by interpersonal provocation — one person's provoking act creating another's loss of heart; the relational origin of the characteristic named explicitly (Col 3:21) |
| 2657 | 1403-001 | The fainthearted soul — the inner person diminished in courage (oligopsuchos: small-souled), requiring the response of being drawn alongside (paraklēsis) rather than correction or practical assistance (1Th 5:14) |

Anchors: id=489 anchor = Col 3:21. id=2657 anchor = 1Th 5:14. Both retain existing anchors.

---

### Operation set 2 — SPLIT

**SPLIT 1: group id=1014 (1700-001, ka.eh) → NEW VCG-C2 + NEW VCG-C3**

Soft-delete group id=1014.

**NEW VCG-C2 (insert):**
- group_code: M20-C-NEW-01
- mti_term_id: resolve from strongs_number='H3512B' (ka.eh)
- context_description: Discouragement inflicted on the vulnerable — the disheartened as the specific target of cruelty (Psa 109:16: the brokenhearted pursued to death) and deceptive spiritual speech (Eze 13:22: false prophets disheartening the righteous falsely); the inner state of the vulnerable making them a target
- Member verses (ka.eh rows): Psa 109:16, Eze 13:22
- Anchor (ka.eh): Eze 13:22 (is_anchor=1)

**NEW VCG-C3 (insert):**
- group_code: M20-C-NEW-02
- mti_term_id: resolve from strongs_number='H3512B' (ka.eh)
- context_description: Discouragement producing inner retreat — loss of resolve under military-political pressure, expressed immediately in withdrawal and turning back (Dan 11:30)
- Member verse (ka.eh row): Dan 11:30
- Anchor (ka.eh): Dan 11:30 (is_anchor=1)

**SPLIT 2: group id=2716 (603-001, ekkakeō) → NEW VCG-C5 + NEW VCG-C6**

Soft-delete group id=2716.

**NEW VCG-C5 (insert):**
- group_code: M20-C-NEW-03
- mti_term_id: resolve from strongs_number='G1573'
- context_description: Loss of heart in sustained effort — long-haul endurance failing under temporal frustration; the discouragement that accumulates from persistent prayer (Luk 18:1), ministry (2Cor 4:1), doing good (Gal 6:9; 2Th 3:13), bearing another's suffering (Eph 3:13); countered by theological means (mercy received, future harvest) not circumstantial relief
- Member verses: Luk 18:1, 2Cor 4:1, Gal 6:9, Eph 3:13, 2Th 3:13
- Anchor: Luk 18:1 (is_anchor=1)

**NEW VCG-C6 (insert):**
- group_code: M20-C-NEW-04
- mti_term_id: resolve from strongs_number='G1573'
- context_description: Loss of heart and the inner person's renewal — the outer person wasting away while the inner person is renewed day by day; physical decline cannot produce inner collapse when the inner person is sustained by God; the outer/inner distinction named precisely (2Cor 4:16)
- Member verse: 2Cor 4:16
- Anchor: 2Cor 4:16 (is_anchor=1)

**SPLIT 3: group id=2739 (574-001, ka.ah) → NEW VCG-C2 (shared) + NEW VCG-C3 (shared) + NEW VCG-C7**

Soft-delete group id=2739.

**NEW VCG-C7 (insert):**
- group_code: M20-C-NEW-05
- mti_term_id: resolve from strongs_number='H3512A' (ka.ah)
- context_description: The crushed and sinking — total inner overwhelm of the helpless; ka.ah in its most acute form: the victim crushed, sinking down, and falling under superior might; complete inner collapse with no capacity for resistance (Psa 10:10)
- Member verse (ka.ah only): Psa 10:10
- Anchor: Psa 10:10 (is_anchor=1)

**Dual-term shared verses — ka.ah rows:**
The 3 shared verses (Psa 109:16, Eze 13:22, Dan 11:30) have both a ka.eh vc row (migrated to VCG-C2/C3 above) and a ka.ah vc row (currently in group 574-001). The ka.ah rows for these 3 verses must also be migrated to the same new groups:
- Psa 109:16 (ka.ah row) → NEW VCG-C2 (M20-C-NEW-01), is_anchor=0
- Eze 13:22 (ka.ah row) → NEW VCG-C2 (M20-C-NEW-01), is_anchor=0
- Dan 11:30 (ka.ah row) → NEW VCG-C3 (M20-C-NEW-02), is_anchor=0

Note: VCG-C2 and VCG-C3 are created with mti_term_id=ka.eh (H3512B) as the owning term, but contain verse_context rows for both ka.eh and ka.ah. CC to confirm whether verse_context_group.mti_term_id must be a single term, or whether both terms' vc rows can point to the same group regardless. If the schema requires separate groups per term, create mirror groups for ka.ah (M20-C-NEW-01B, M20-C-NEW-02B) with identical descriptions.

---

### Operation set 3 — verse_context UPSERT (complete assignment)

| Reference | Term (strongs) | Target group | is_anchor |
|---|---|---|---|
| Col 3:21 | G0120 | id=489 (2078-001, REFINE) | 1 |
| 1Th 5:14 | G3642 | id=2657 (1403-001, REFINE) | 1 |
| Psa 109:16 | H3512B (ka.eh) | NEW M20-C-NEW-01 | 0 |
| Eze 13:22 | H3512B (ka.eh) | NEW M20-C-NEW-01 | 1 |
| Dan 11:30 | H3512B (ka.eh) | NEW M20-C-NEW-02 | 1 |
| Psa 109:16 | H3512A (ka.ah) | NEW M20-C-NEW-01 | 0 |
| Eze 13:22 | H3512A (ka.ah) | NEW M20-C-NEW-01 | 0 |
| Dan 11:30 | H3512A (ka.ah) | NEW M20-C-NEW-02 | 0 |
| Psa 10:10 | H3512A (ka.ah) | NEW M20-C-NEW-05 | 1 |
| Luk 18:1 | G1573 | NEW M20-C-NEW-03 | 1 |
| 2Cor 4:1 | G1573 | NEW M20-C-NEW-03 | 0 |
| 2Cor 4:16 | G1573 | NEW M20-C-NEW-04 | 1 |
| Gal 6:9 | G1573 | NEW M20-C-NEW-03 | 0 |
| Eph 3:13 | G1573 | NEW M20-C-NEW-03 | 0 |
| 2Th 3:13 | G1573 | NEW M20-C-NEW-03 | 0 |

Set-asides: none.

---

## OUTCOME REQUIRED

| VCG | Code | Verse_context rows | Anchors |
|---|---|---|---|
| id=489 | 2078-001 (REFINE) | 1 | 1 (Col 3:21) |
| id=2657 | 1403-001 (REFINE) | 1 | 1 (1Th 5:14) |
| NEW M20-C-NEW-01 | VCG-C2 | 4 (2 ka.eh + 2 ka.ah) | 1 (Eze 13:22 ka.eh) |
| NEW M20-C-NEW-02 | VCG-C3 | 2 (1 ka.eh + 1 ka.ah) | 1 (Dan 11:30 ka.eh) |
| NEW M20-C-NEW-03 | VCG-C5 | 5 | 1 (Luk 18:1) |
| NEW M20-C-NEW-04 | VCG-C6 | 1 | 1 (2Cor 4:16) |
| NEW M20-C-NEW-05 | VCG-C7 | 1 | 1 (Psa 10:10) |
| **Total** | | **15** | **7** |

Soft-deleted VCGs: id=1014 (1700-001), id=2716 (603-001), id=2739 (574-001) — 3 rows. Dual assignments: 0.

---

## COMPLETION CONFIRMATION

```sql
-- 1. Verse_context row count per VCG (M20-C)
SELECT vcg.group_code, vcg.id, COUNT(vc.id) as vc_rows
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.strongs_number IN ('G0120','G1573','G3642','H3512A','H3512B')
  AND COALESCE(vcg.delete_flagged, 0) = 0
GROUP BY vcg.id, vcg.group_code
ORDER BY vcg.group_code;
-- Expected: 7 rows matching table above

-- 2. Anchor count per active VCG = 1
SELECT vcg.group_code, COUNT(*) as anchor_count
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE vc.is_anchor = 1
  AND mt.strongs_number IN ('G0120','G1573','G3642','H3512A','H3512B')
  AND COALESCE(vcg.delete_flagged, 0) = 0
GROUP BY vcg.group_code;
-- Expected: 1 per active VCG (7 rows, each = 1)

-- 3. Soft-deleted VCGs
SELECT id, group_code, delete_flagged
FROM verse_context_group WHERE id IN (1014, 2716, 2739);
-- Expected: all 3 have delete_flagged = 1

-- 4. Total M20-C verse_context rows = 15
SELECT COUNT(*) FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.strongs_number IN ('G0120','G1573','G3642','H3512A','H3512B');
-- Expected: 15
```

CC to save application report to: `Sessions/Session_Clusters/M20/WA-M20-C-group-mapping-applied-v1-20260513.md`

---

*wa-cluster-M20-dir-007-M20-C-mapping-v1-20260513 | DIR-20260513-007 | M20-C group-verse mapping apply | 2 REFINE + 3 SPLIT + 5 NEW | 15 vc rows | Dual-term shared verses require careful CC handling | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
