# wa-cluster-M20-dir-005-M20-A-mapping-v1-20260513

**DIRECTIVE ID:** DIR-20260513-005  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Sub-group:** M20-A — Anxiety and Worry  
**Directive type:** Group-verse mapping apply (§10.4 / §11.4)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Source mapping:** WA-M20-A-group-verse-mapping-v2-20260513.md  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Date:** 2026-05-13  

---

## MOTIVATION

Phase 6 VCG reconciliation for M20-A (Anxiety and Worry) is complete. The mapping document `WA-M20-A-group-verse-mapping-v2-20260513.md` (supersedes v1 per researcher methodological correction — no set-asides; all verses retained as illuminating some dimension of the characteristic) specifies reconciliation decisions for all 7 existing VCGs and 30 connected verse_context rows.

The mapping produces: 4 REFINE operations (existing VCGs retained with description updates), 3 SPLIT operations (existing VCGs soft-deleted; 6 NEW VCGs created), 0 OBSOLETE, 0 MERGE. Net: 7 existing → 10 VCGs post-apply. 0 set-asides throughout.

---

## SCOPE

**Cluster:** M20 | **Sub-group:** M20-A | **Terms:** G3308 merimna, G3309 merimnaō, H1672 da.ag

**Schema note:** `verse_context.cluster_subgroup_id` may not exist post-M46 schema change — CC to confirm before writing. If absent, omit from UPSERT operations.

---

### Operation set 1 — REFINE: update context_description, retain group id

| Group id | Current code | Refined description |
|---|---|---|
| 220 | 350-001 | Anxiety as choking weight on the inner person — cares of the world, riches, and pleasures operating together to strangle spiritual fruitfulness and prevent the word from maturing in the inner person |
| 222 | 2709-001 | Anxiety about material provision — the inner person preoccupied with food, drink, clothing, the body, and tomorrow; addressed by Jesus as both futile (cannot add a single hour) and unnecessary (God provides) |
| 224 | 2709-003 | The anxiety-faculty rightly directed — merimnaō naming the intensity of directed concern for God's things and for others' welfare; the same inner faculty that produces anxiety when misdirected is the substance of devotion and love when rightly oriented |
| 888 | 259-002 | Anxiety as the fuel of contrition — da.ag naming the inner energy that drives genuine sorrow over sin; the anxious, troubled quality of the inner person directed toward personal wrongdoing rather than external threat |

---

### Operation set 2 — SPLIT: soft-delete existing VCGs; create NEW VCGs; migrate verses

**SPLIT 1: group id=221 (350-002) → NEW VCG-A8 + NEW VCG-A9**

Soft-delete group id=221 (350-002).

NEW VCG-A8 (insert):
- group_code: M20-A-NEW-01
- mti_term_id: resolve from strongs_number='G3308'
- context_description: Anxiety cast onto God — the person currently carrying real anxieties commanded to transfer the weight to God, with the theological ground: he cares for you (1Pe 5:7)
- Member verse: 1Pe 5:7 (mti_term_id=G3308; vr_id to be resolved by CC from reference + term)
- Anchor: 1Pe 5:7 (is_anchor=1)

NEW VCG-A9 (insert):
- group_code: M20-A-NEW-02
- mti_term_id: resolve from strongs_number='G3308'
- context_description: Pastoral burden as the weight of love — merimna naming the daily pressure of apostolic care for the churches; love expressed as a carried burden over time (2Cor 11:28)
- Member verse: 2Cor 11:28 (mti_term_id=G3308)
- Anchor: 2Cor 11:28 (is_anchor=1)

**SPLIT 2: group id=223 (2709-002) → NEW VCG-A3 + NEW VCG-A4**

Soft-delete group id=223 (2709-002).

NEW VCG-A3 (insert):
- group_code: M20-A-NEW-03
- mti_term_id: resolve from strongs_number='G3309'
- context_description: Anticipatory anxiety about speech and defence under threat — anxiety directed toward a specific future performance situation; the remedy named is Spirit-provision in the moment (Mat 10:19; Luk 12:11)
- Member verses: Mat 10:19, Luk 12:11 (mti_term_id=G3309)
- Anchor: Mat 10:19 (is_anchor=1)

NEW VCG-A4 (insert):
- group_code: M20-A-NEW-04
- mti_term_id: resolve from strongs_number='G3309'
- context_description: Anxiety as proliferation — the inner person anxious and troubled about many things; attentional scattering across multiplicity, contrasted with the one-thing orientation of the non-anxious person (Luk 10:41)
- Member verse: Luk 10:41 (mti_term_id=G3309)
- Anchor: Luk 10:41 (is_anchor=1)

**SPLIT 3: group id=887 (259-001) → NEW VCG-A6 + NEW VCG-A7**

Soft-delete group id=887 (259-001).

NEW VCG-A6 (insert):
- group_code: M20-A-NEW-05
- mti_term_id: resolve from strongs_number='H1672'
- context_description: Relational anxiety — worried concern for an absent or endangered person; anxiety as the dark face of relational love when the loved one is missing or at risk; voiced as distress seeking resolution (1Sa 9:5; 1Sa 10:2)
- Member verses: 1Sa 9:5, 1Sa 10:2 (mti_term_id=H1672)
- Anchor: 1Sa 10:2 (is_anchor=1)

NEW VCG-A7 (insert):
- group_code: M20-A-NEW-06
- mti_term_id: resolve from strongs_number='H1672'
- context_description: Anxiety in the face of concrete external threats — and its structural opposite; da.ag applied to real, named dangers (Isa 57:11; Jer 38:19; Jer 42:16); Jer 17:8 as the structural opposite: rootedness in God producing non-anxiety even under genuine threat — the most precise OT statement of what anxiety, at its core, is
- Member verses: Isa 57:11, Jer 38:19, Jer 42:16, Jer 17:8 (mti_term_id=H1672)
- Anchor: Jer 17:8 (is_anchor=1) — structural-opposite anchor; secondary distress anchor: Jer 38:19

---

### Operation set 3 — verse_context UPSERT

For all 30 verse_context rows in M20-A: set group_id to the correct new or retained group, is_anchor per mapping, is_relevant=1 (confirmed: 0 set-asides).

CC to resolve vr_ids from (reference, strongs_number) pairs. Full verse-to-group assignment:

| Reference | Term (strongs) | Target group | is_anchor |
|---|---|---|---|
| Mat 13:22 | G3308 | id=220 (350-001, REFINE) | 0 |
| Mar 4:19 | G3308 | id=220 | 0 |
| Luk 8:14 | G3308 | id=220 | 0 |
| Luk 21:34 | G3308 | id=220 | 1 |
| 1Pe 5:7 | G3308 | NEW VCG-A8 (M20-A-NEW-01) | 1 |
| 2Cor 11:28 | G3308 | NEW VCG-A9 (M20-A-NEW-02) | 1 |
| Mat 6:25 | G3309 | id=222 (2709-001, REFINE) | 1 |
| Mat 6:27 | G3309 | id=222 | 0 |
| Mat 6:28 | G3309 | id=222 | 0 |
| Mat 6:31 | G3309 | id=222 | 0 |
| Mat 6:34 | G3309 | id=222 | 0 |
| Luk 12:22 | G3309 | id=222 | 0 |
| Luk 12:25 | G3309 | id=222 | 0 |
| Luk 12:26 | G3309 | id=222 | 0 |
| Phili 4:6 | G3309 | id=222 | 0 |
| Mat 10:19 | G3309 | NEW VCG-A3 (M20-A-NEW-03) | 1 |
| Luk 12:11 | G3309 | NEW VCG-A3 | 0 |
| Luk 10:41 | G3309 | NEW VCG-A4 (M20-A-NEW-04) | 1 |
| 1Cor 7:32 | G3309 | id=224 (2709-003, REFINE) | 1 |
| 1Cor 7:33 | G3309 | id=224 | 0 |
| 1Cor 7:34 | G3309 | id=224 | 0 |
| 1Cor 12:25 | G3309 | id=224 | 0 |
| Phili 2:20 | G3309 | id=224 | 0 |
| 1Sa 9:5 | H1672 | NEW VCG-A6 (M20-A-NEW-05) | 0 |
| 1Sa 10:2 | H1672 | NEW VCG-A6 | 1 |
| Isa 57:11 | H1672 | NEW VCG-A7 (M20-A-NEW-06) | 0 |
| Jer 17:8 | H1672 | NEW VCG-A7 | 1 |
| Jer 38:19 | H1672 | NEW VCG-A7 | 0 |
| Jer 42:16 | H1672 | NEW VCG-A7 | 0 |
| Psa 38:18 | H1672 | id=888 (259-002, REFINE) | 1 |

**Set-asides:** none. Set-aside rows from Phase 2 (13 rows, mti_term_id=H5074 na.dad — now in M18) not touched by this directive.

---

## OUTCOME REQUIRED

| VCG | Code | Verses | Anchors |
|---|---|---|---|
| id=220 | 350-001 (REFINE) | 4 | 1 (Luk 21:34) |
| NEW M20-A-NEW-01 | VCG-A8 | 1 | 1 (1Pe 5:7) |
| NEW M20-A-NEW-02 | VCG-A9 | 1 | 1 (2Cor 11:28) |
| id=222 | 2709-001 (REFINE) | 9 | 1 (Mat 6:25) |
| NEW M20-A-NEW-03 | VCG-A3 | 2 | 1 (Mat 10:19) |
| NEW M20-A-NEW-04 | VCG-A4 | 1 | 1 (Luk 10:41) |
| id=224 | 2709-003 (REFINE) | 5 | 1 (1Cor 7:32) |
| NEW M20-A-NEW-05 | VCG-A6 | 2 | 1 (1Sa 10:2) |
| NEW M20-A-NEW-06 | VCG-A7 | 4 | 1 (Jer 17:8) |
| id=888 | 259-002 (REFINE) | 1 | 1 (Psa 38:18) |
| **Total** | | **30** | **10** |

Soft-deleted VCGs: id=221 (350-002), id=223 (2709-002), id=887 (259-001) — 3 rows

Dual assignments: 0

---

## COMPLETION CONFIRMATION

```sql
-- 1. Verse count per VCG (M20-A)
SELECT vcg.group_code, vcg.id, COUNT(vc.id) as verse_count
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.cluster_code = 'M20'
  AND mt.strongs_number IN ('G3308','G3309','H1672')
  AND COALESCE(vcg.delete_flagged, 0) = 0
GROUP BY vcg.id, vcg.group_code
ORDER BY vcg.group_code;
-- Expected: 10 rows matching table above

-- 2. Anchor count per VCG = 1
SELECT vcg.group_code, COUNT(*) as anchor_count
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.is_anchor = 1
  AND vcg.group_code LIKE '%350%' OR vcg.group_code LIKE '%2709%'
  OR vcg.group_code LIKE '%259%' OR vcg.group_code LIKE 'M20-A-%'
GROUP BY vcg.group_code;
-- Expected: 1 per VCG

-- 3. Soft-deleted VCGs
SELECT id, group_code, delete_flagged
FROM verse_context_group
WHERE id IN (221, 223, 887);
-- Expected: all 3 rows have delete_flagged = 1

-- 4. Total M20-A verse_context rows unchanged
SELECT COUNT(*) FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.strongs_number IN ('G3308','G3309','H1672');
-- Expected: 30

-- 5. Set-aside rows untouched (Phase 2 set-asides remain under M18 term)
SELECT COUNT(*) FROM verse_context WHERE mti_term_id = 5571 AND is_relevant = 0;
-- Expected: 13 (unchanged)
```

CC to save application report to: `Sessions/Session_Clusters/M20/WA-M20-A-group-mapping-applied-v1-20260513.md`

---

*wa-cluster-M20-dir-005-M20-A-mapping-v1-20260513 | DIR-20260513-005 | M20-A group-verse mapping apply | 4 REFINE + 3 SPLIT + 6 NEW | 30 verses | 0 set-asides | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
