# wa-cluster-M20-dir-006-M20-B-mapping-v1-20260513

**DIRECTIVE ID:** DIR-20260513-006  
**Cluster:** M20 Doubt, Despair and Anxiety  
**Sub-group:** M20-B — Despair and Hopelessness  
**Directive type:** Group-verse mapping apply (§10.4 / §11.4)  
**Governing instruction:** wa-directive-instruction-v1_4-20260506  
**Source mapping:** WA-M20-B-group-verse-mapping-v1-20260513.md  
**Session reference:** wa-obslog-M20-m20-doubt-v1-20260513  
**Date:** 2026-05-13  

---

## MOTIVATION

Phase 6 VCG reconciliation for M20-B (Despair and Hopelessness) is complete. The mapping document `WA-M20-B-group-verse-mapping-v1-20260513.md` specifies reconciliation decisions for all 2 existing VCGs and 8 connected verse_context rows.

The mapping produces: 1 REFINE (808-001 retained with description update), 1 SPLIT (394-001 soft-deleted; 3 NEW VCGs created). Net: 2 existing → 4 VCGs post-apply. 0 set-asides.

---

## SCOPE

**Cluster:** M20 | **Sub-group:** M20-B | **Terms:** G1820 exaporeō, H2976 ya.ash

**Schema note:** `verse_context.cluster_subgroup_id` — CC to confirm existence post-M46 before writing.

---

### Operation set 1 — REFINE

| Group id | Current code | Refined description |
|---|---|---|
| 660 | 808-001 | Despair as the outer limit of inner endurance — the inner person burdened beyond capacity, despaired of life itself (2Cor 1:8); and the edge approached but not crossed under God's sustaining grace, perplexed but not driven to despair (2Cor 4:8) |

Anchor for id=660: 2Cor 1:8 (is_anchor=1). 2Cor 4:8 (is_anchor=0).

---

### Operation set 2 — SPLIT: soft-delete group id=1238 (394-001); create 3 NEW VCGs

Soft-delete group id=1238 (394-001).

**NEW VCG-B2 (insert):**
- group_code: M20-B-NEW-01
- mti_term_id: resolve from strongs_number='H2976'
- context_description: Despair as volitional act — the heart actively surrendered to hopelessness (Ecc 2:20); despair as the natural terminus of exhausted pursuit when all options are gone (1Sa 27:1); despair leaving a recognisable inner signature in speech — the despairing man's words are wind (Job 6:26)
- Member verses: Ecc 2:20, 1Sa 27:1, Job 6:26
- Anchor: Ecc 2:20 (is_anchor=1)

**NEW VCG-B3 (insert):**
- group_code: M20-B-NEW-02
- mti_term_id: resolve from strongs_number='H2976'
- context_description: Despair as declaration — the word of hopelessness spoken or withheld, and its consequences; the declaration not made (Isa 57:10: "you did not say it is hopeless") illuminating the characteristic by its resistance; the declaration made (Jer 2:25: "it is hopeless, I have loved foreigners") closing off the path of return
- Member verses: Isa 57:10, Jer 2:25
- Anchor: Jer 2:25 (is_anchor=1)

**NEW VCG-B4 (insert):**
- group_code: M20-B-NEW-03
- mti_term_id: resolve from strongs_number='H2976'
- context_description: Despair weaponised — hopelessness-language deployed to foreclose repentance and justify continued rebellion; "that is in vain, we will follow our own plans" (Jer 18:12); the darkest dimension of the characteristic: despair as a posture used against the inner person's own potential for transformation
- Member verse: Jer 18:12
- Anchor: Jer 18:12 (is_anchor=1)

---

### Operation set 3 — verse_context UPSERT

| Reference | Term (strongs) | Target group | is_anchor |
|---|---|---|---|
| 2Cor 1:8 | G1820 | id=660 (808-001, REFINE) | 1 |
| 2Cor 4:8 | G1820 | id=660 | 0 |
| Ecc 2:20 | H2976 | NEW M20-B-NEW-01 | 1 |
| 1Sa 27:1 | H2976 | NEW M20-B-NEW-01 | 0 |
| Job 6:26 | H2976 | NEW M20-B-NEW-01 | 0 |
| Isa 57:10 | H2976 | NEW M20-B-NEW-02 | 0 |
| Jer 2:25 | H2976 | NEW M20-B-NEW-02 | 1 |
| Jer 18:12 | H2976 | NEW M20-B-NEW-03 | 1 |

Set-asides: none.

---

## OUTCOME REQUIRED

| VCG | Code | Verses | Anchors |
|---|---|---|---|
| id=660 | 808-001 (REFINE) | 2 | 1 (2Cor 1:8) |
| NEW M20-B-NEW-01 | VCG-B2 | 3 | 1 (Ecc 2:20) |
| NEW M20-B-NEW-02 | VCG-B3 | 2 | 1 (Jer 2:25) |
| NEW M20-B-NEW-03 | VCG-B4 | 1 | 1 (Jer 18:12) |
| **Total** | | **8** | **4** |

Soft-deleted VCGs: id=1238 (394-001) — 1 row. Dual assignments: 0.

---

## COMPLETION CONFIRMATION

```sql
-- 1. Verse count per VCG (M20-B)
SELECT vcg.group_code, vcg.id, COUNT(vc.id) as verse_count
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.strongs_number IN ('G1820','H2976')
  AND COALESCE(vcg.delete_flagged, 0) = 0
GROUP BY vcg.id, vcg.group_code
ORDER BY vcg.group_code;
-- Expected: 4 rows matching table above

-- 2. Anchor count per VCG = 1
SELECT vcg.group_code, COUNT(*) as anchor_count
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.is_anchor = 1
  AND vcg.mti_term_id IN (
      SELECT id FROM mti_terms WHERE strongs_number IN ('G1820','H2976'))
GROUP BY vcg.group_code;
-- Expected: 1 per active VCG

-- 3. Soft-deleted VCG
SELECT id, group_code, delete_flagged FROM verse_context_group WHERE id = 1238;
-- Expected: delete_flagged = 1

-- 4. Total M20-B verse_context rows
SELECT COUNT(*) FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.strongs_number IN ('G1820','H2976');
-- Expected: 8
```

CC to save application report to: `Sessions/Session_Clusters/M20/WA-M20-B-group-mapping-applied-v1-20260513.md`

---

*wa-cluster-M20-dir-006-M20-B-mapping-v1-20260513 | DIR-20260513-006 | M20-B group-verse mapping apply | 1 REFINE + 1 SPLIT + 3 NEW | 8 verses | 0 set-asides | Session reference: wa-obslog-M20-m20-doubt-v1-20260513*
