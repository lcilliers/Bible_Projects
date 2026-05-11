# wa-cluster-M26-dir-001-A2-rename-boundary-reassign-v1-20260510

**Directive ID:** DIR-M26-20260510-001  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11 (Cluster-process directives)  
**Filename pattern:** wa-cluster-{cluster_code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md  

---

## DIRECTIVE ID

DIR-M26-20260510-001

---

## MOTIVATION

During the M26 analytical session of 2026-05-09/10, the 589 M26-A verses were split by subject (God / man / both / neither) using the pre-classified file `m26-meanings-by-subject-claude-sonnet-4-6-M26-A-20260509-by-subject.md`. This produced two active sub-groups — M26-A1 (God Righteousness, 157 verses) and M26-A2 (Human Righteousness, 341 verses) — and identified 11 verses classified as "both" (where both God and human are active subjects in the same verse) and 80 verses classified as "neither" (where righteousness qualifies an impersonal noun or abstraction).

The 11 "both" verses require separate analytical focus and are analytically distinct from both the God and human sub-groups. Per programme precedent (M06) and the BOUNDARY sub-group's defined purpose — holding verses that support the cluster's activity without themselves constituting the core inner-being characteristic — these "both" verses are most appropriately held in M26-BOUNDARY pending dedicated analysis.

This directive effects two changes to the M26-A2 sub-group:

1. **Description update:** The current M26-A2 description is a placeholder left by the 2026-05-10 split. It requires replacement with a substantive description reflecting the sub-group's confirmed analytical scope — human righteousness as a governing inner state.

2. **Verse reassignment:** 10 verses currently assigned to M26-A2 (and also to M26-A1 — see DIR-M26-20260510-002) were classified as "both" in the analytical file. These are to be reassigned from M26-A2 to M26-BOUNDARY. One "both" verse (Hos 10:12, H6666, vr_id 25168) is addressed in DIR-M26-20260510-002 (M26-A1 scope).

---

## SCOPE

**Primary table:** `cluster_subgroup`  
**Secondary table:** `verse_context` (subgroup assignment field)  
**Cluster:** M26  
**Sub-group affected:** M26-A2  
**Destination sub-group (for moved verses):** M26-BOUNDARY  

**Operation 1 — Description update:**  
Update `cluster_subgroup` WHERE `cluster_code = 'M26'` AND `subgroup_code = 'M26-A2'`.  
Field: `description` (or equivalent label/description field in schema).

**Operation 2 — Verse reassignment:**  
Update `verse_context.cluster_subgroup_id` (or equivalent field linking a verse_context row to a sub-group) for each of the 10 vr_ids listed below, from the M26-A2 sub-group ID to the M26-BOUNDARY sub-group ID.

CC must resolve the integer sub-group IDs from `cluster_subgroup` before executing updates. Do not hardcode IDs.

---

## OUTCOME REQUIRED

### Operation 1 — M26-A2 description

Replace the current placeholder description with the following:

> Located in the character, conduct, and covenantal standing of the human person; the term names the state of being rightly oriented toward God and toward others — a governing inner condition from which just thought, truthful speech, generous action, stability under adversity, and appropriate response to God (fear, trust, joy, prayer) all flow. The state is never directly defined in the text; its content is evidenced by what the righteous person is and does. It is assessed before God, not before human observers. Structurally opposed by wickedness (*rasha*, M26-G) and injustice (*aval*, M26-G). Distinguished from M26-A1 (God's own righteousness) and from M26-C (the divine act of declaring a person righteous). Verses where both God and a human person are foregrounded as active subjects are held in M26-BOUNDARY.

### Operation 2 — Verse reassignment from M26-A2 to M26-BOUNDARY

The following 10 verse_context rows are to be reassigned. Each was classified as "both" in the analytical subject-classification file, meaning God and a human person are both active subjects in the verse. They are analytically distinct from pure human-righteousness verses and require dedicated treatment in M26-BOUNDARY.

| vr_id | mti_id | Reference | Term | Current sub-group | Destination sub-group |
|------:|-------:|-----------|------|------------------|----------------------|
| 93748 | 3193 | 1Jo 2:29 | G1342 dikaios | M26-A2 | M26-BOUNDARY |
| 93750 | 3193 | 1Jo 3:7 | G1342 dikaios | M26-A2 | M26-BOUNDARY |
| 28726 | 950 | 2Cor 5:21 | G1343 dikaiosunē | M26-A2 | M26-BOUNDARY |
| 25165 | 911 | Gen 15:6 | H6666 tse.da.qah | M26-A2 | M26-BOUNDARY |
| 28307 | 942 | Hos 10:12 | H6664G tse.deq | M26-A2 | M26-BOUNDARY |
| 25190 | 911 | Isa 56:1 | H6666 tse.da.qah | M26-A2 | M26-BOUNDARY |
| 25214 | 911 | Judg 5:11 | H6666 tse.da.qah | M26-A2 | M26-BOUNDARY |
| 93744 | 950 | Phili 3:9 | G1343 dikaiosunē | M26-A2 | M26-BOUNDARY |
| 169505 | 3246 | Psa 7:9 | H6662 tsad.diq | M26-A2 | M26-BOUNDARY |
| 28747 | 950 | Rom 10:4 | G1343 dikaiosunē | M26-A2 | M26-BOUNDARY |

**Note on Hos 10:12:** This reference appears twice in the cluster — once as H6664G (vr_id 28307, addressed here) and once as H6666 (vr_id 25168, addressed in DIR-M26-20260510-002 as it currently sits in M26-A1). Both instances are "both" verses and both are to be moved to M26-BOUNDARY. CC should confirm both are moved.

**Note on SA verses:** Three verse_context rows in M26-A2 have status SA (no_inner_being): vr_id 95976 (Deu 25:15), vr_id 95982 (Eze 45:10), vr_id 28346 (Lev 19:36). These are correctly set aside. No action required on these rows.

---

## COMPLETION CONFIRMATION

CC must confirm the following after execution:

**1. M26-A2 description updated:**
```sql
SELECT subgroup_code, label, description
FROM cluster_subgroup
WHERE cluster_code = 'M26' AND subgroup_code = 'M26-A2';
```
Expected: description field matches the new text above (or its first 100 characters confirm the replacement).

**2. Verse counts after reassignment:**
```sql
-- M26-A2 remaining count (should be 345: 355 − 10 moved)
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A2'
AND vc.status IN ('extracted', 'extracted_thin');

-- M26-BOUNDARY count (should be 112 + 10 = 122 minimum, accounting for any pre-existing)
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-BOUNDARY'
AND vc.status IN ('extracted', 'extracted_thin');
```

**3. Confirm all 10 vr_ids now in BOUNDARY:**
```sql
SELECT vc.id as vr_id, cs.subgroup_code, mt.strong, vc.verse_ref
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE vc.id IN (93748, 93750, 28726, 25165, 28307, 25190, 25214, 93744, 169505, 28747)
ORDER BY vc.verse_ref;
```
Expected: all 10 rows showing `subgroup_code = 'M26-BOUNDARY'`.

**4. Confirm Hos 10:12 H6666 (vr_id 25168) — handled in DIR-M26-20260510-002:**
```sql
SELECT vc.id, cs.subgroup_code, mt.strong
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE vc.id = 25168;
```
Expected after DIR-M26-20260510-002 executes: `subgroup_code = 'M26-BOUNDARY'`.

---

*DIR-M26-20260510-001 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11*
