# wa-cluster-M26-dir-004-A2-straggler-cleanup-v1-20260510

**Directive ID:** DIR-M26-20260510-004  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Sub-group:** M26-A2 — Human Righteousness — State of being right  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11  
**Companion:** DIR-M26-20260510-003 (applied — v12 state)  

---

## DIRECTIVE ID

DIR-M26-20260510-004

---

## MOTIVATION

Following application of DIR-M26-20260510-003, CC surfaced 8 straggler verses that were described in the directive as reassigned but not explicitly placed in a destination group (I-6 omissions). Additionally, 4 verses remain in the legacy group `3246-001` which was intended to be fully dissolved. This directive places all 12 verses in their correct M26-A2 groups, completing the restructure.

All assignments are based on close reading of each verse against the new VSG descriptions established in DIR-003.

---

## SCOPE

**Table:** `verse_context` — UPDATE `verse_context_group_id` for 12 rows  
**Cluster:** M26 / Sub-group: M26-A2  
**No new VSGs required** — all destinations are existing groups from DIR-003  

---

## OUTCOME REQUIRED

Assign each verse_context row to its destination group. CC to resolve group_id from group_code before executing.

### 8 Straggler verses (I-6 omissions from DIR-003)

| vr_id | ref | term | current group | destination group | rationale |
|------:|-----|------|--------------|-------------------|-----------|
| 25184 | Isa 5:23 | H6666 tse.da.qah | 911-002 | M26-A2-010 | "Deprive innocent of his right" — righteousness wrongly overridden by corrupt judgment; same meaning as Isa 5:23 H6662 already in M26-A2-010 |
| 28314 | Isa 26:10 | H6664G tse.deq | 942-001 | M26-A2-003 | Wicked fails to learn righteousness even in uprightness — distortion/absence; righteousness learnable but refused |
| 28315 | Isa 26:9 | H6664G tse.deq | 942-001 | M26-A2-006 | Soul yearns for God; inhabitants of world learn righteousness when God's judgments are present — hunger/pursuit dimension |
| 28330 | Isa 61:3 | H6664G tse.deq | 942-001 | M26-A2-008 | "Oaks of righteousness, the planting of the Lord" — righteousness as identity conferred by God; fits new-self/constituted identity group |
| 28333 | Isa 64:5 | H6664G tse.deq | 942-001 | 950-002 | "You meet him who joyfully works righteousness" — active joyful conduct drawing God's presence; lived/practiced orientation |
| 96008 | Psa 17:15 | H6664G tse.deq | 942-001 | M26-A2-014 | "I shall behold your face in righteousness; when I awake, satisfied with your likeness" — eschatological God-orientation; note for future eschatological VSG split |
| 96013 | Psa 35:27 | H6664G tse.deq | 942-001 | 3246-003 | "Those who delight in my righteousness shout for joy — Great is the Lord" — joy and delight expressed toward God; characteristic inner response |
| 169443 | Pro 18:10 | H6662 tsad.diq | 3246-003 | M26-A2-014 | "Righteous man runs into name of Lord and is safe" — trust expressed as refuge-seeking in God; relational orientation toward God |

---

### 4 Legacy remnants (still in dissolved `3246-001`)

| vr_id | ref | term | current group | destination group | rationale |
|------:|-----|------|--------------|-------------------|-----------|
| 169461 | Pro 9:9 | H6662 tsad.diq | 3246-001 | M26-A2-006 | "Teach a righteous man and he will increase in learning" — teachability as formation; righteous person is formable through instruction |
| 169429 | Pro 12:5 | H6662 tsad.diq | 3246-001 | M26-A2-011 | "Thoughts of righteous are just" — justice operative at the cognitive level; the interior of speech and expression |
| 169358 | Eze 3:21 | H6662 tsad.diq | 3246-001 | M26-A2-002 | "Warn righteous, he heeds and does not sin — shall live" — heeding warning prevents loss of standing; Ezekiel precarious cluster |
| 169374 | Hos 14:9 | H6662 tsad.diq | 3246-001 | M26-A2-017 | "Ways of Lord are right, righteous walk in them" — life path dimension; righteous walk in God's ways |

---

## NOTES FOR CC

**On vr_id 25184 (Isa 5:23):** This verse appears under H6666 (vr_id 25184) and under H6662 (vr_id 169383, already in M26-A2-010). Both are the same biblical reference under different terms. Both should be in M26-A2-010. Confirm vr_id 169383 is already correctly placed.

**On vr_id 96008 (Psa 17:15):** Assigned to M26-A2-014 (relational orientation toward God) as the closest existing group. This verse has an eschatological dimension — "behold your face in righteousness, awake satisfied with your likeness" — that warrants its own VSG eventually. CC to add an analytical note on this verse flagging the eschatological dimension for future review.

**On `3246-001`:** After placing the 4 remnants, `3246-001` should be empty of M26-A2 verses. CC to confirm and soft-delete or deactivate the group if the applicator supports it.

---

## COMPLETION CONFIRMATION

**1. Confirm all 12 verses placed:**
```sql
SELECT vc.id, vcg.group_code, vc.verse_ref, mt.strong
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE vc.id IN (25184, 28314, 28315, 28330, 28333, 96008, 96013, 169443,
                169461, 169429, 169358, 169374)
ORDER BY vcg.group_code;
```
Expected: 12 rows, each with its destination group code as listed above.

**2. Confirm `3246-001` is empty in M26-A2:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE vcg.group_code = '3246-001'
AND cs.subgroup_code = 'M26-A2'
AND vc.status IN ('extracted', 'extracted_thin');
```
Expected: 0 rows.

**3. Confirm no M26-A2 verse is groupless:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A2'
AND vc.verse_context_group_id IS NULL
AND vc.status IN ('extracted', 'extracted_thin');
```
Expected: 0 rows.

**4. Report final M26-A2 verse count by group:**
```sql
SELECT vcg.group_code, COUNT(vc.id) as verse_count
FROM verse_context_group vcg
LEFT JOIN verse_context vc ON vc.verse_context_group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A2'
AND vc.status IN ('extracted', 'extracted_thin')
GROUP BY vcg.group_code
ORDER BY vcg.group_code;
```

---

*DIR-M26-20260510-004 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11*  
*Companion to DIR-M26-20260510-003 — straggler cleanup only*
