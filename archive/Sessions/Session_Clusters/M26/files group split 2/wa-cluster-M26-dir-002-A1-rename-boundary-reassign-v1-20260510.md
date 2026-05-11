# wa-cluster-M26-dir-002-A1-rename-boundary-reassign-v1-20260510

**Directive ID:** DIR-M26-20260510-002  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11 (Cluster-process directives)  
**Filename pattern:** wa-cluster-{cluster_code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md  
**Companion directive:** DIR-M26-20260510-001 (M26-A2 rename and BOUNDARY reassignment)

---

## DIRECTIVE ID

DIR-M26-20260510-002

---

## MOTIVATION

This directive is the companion to DIR-M26-20260510-001 and operates on M26-A1 (God Righteousness) using the same analytical decisions. The M26-A1 sub-group currently holds 168 verse_context rows — 157 where righteousness is attributed to God alone, and 11 classified as "both" (where both God and a human person are active subjects in the same verse).

The 11 "both" verses in M26-A1 are the same 11 verses identified in the analysis file (the same verse_context rows appear in both M26-A1 and M26-A2 because both sub-groups share the same six terms). Moving them from M26-A2 to BOUNDARY (DIR-M26-20260510-001) without also moving them from M26-A1 would leave them inconsistently assigned. This directive completes the reassignment by removing them from M26-A1 as well, leaving M26-A1 with 157 verses — consistent with the God righteousness analytical file (`WA-M26A-god-righteousness-v1_0-20260509.md`).

This directive also replaces the M26-A1 placeholder description with substantive analytical content derived from the session analysis.

**Important:** Hos 10:12 appears as two separate verse_context rows in M26-A1 — vr_id 28307 (H6664G) and vr_id 25168 (H6666). Both are "both" verses. Both are to be moved to BOUNDARY. vr_id 28307 is also addressed in DIR-M26-20260510-001 (M26-A2 scope); its BOUNDARY reassignment is the same operation regardless of which directive references it, but CC should confirm both vr_ids are moved as a result of the combined execution of these two directives.

---

## SCOPE

**Primary table:** `cluster_subgroup`  
**Secondary table:** `verse_context` (subgroup assignment field)  
**Cluster:** M26  
**Sub-group affected:** M26-A1  
**Destination sub-group (for moved verses):** M26-BOUNDARY  

**Operation 1 — Description update:**  
Update `cluster_subgroup` WHERE `cluster_code = 'M26'` AND `subgroup_code = 'M26-A1'`.  
Field: `description` (or equivalent label/description field in schema).

**Operation 2 — Verse reassignment:**  
Update `verse_context.cluster_subgroup_id` (or equivalent field) for each of the 11 vr_ids listed below, from the M26-A1 sub-group ID to the M26-BOUNDARY sub-group ID.

CC must resolve the integer sub-group IDs from `cluster_subgroup` before executing updates. Do not hardcode IDs.

---

## OUTCOME REQUIRED

### Operation 1 — M26-A1 description

Replace the current placeholder description with the following:

> Located in the character, judgments, acts, and covenant faithfulness of God himself; the term names God's own righteousness — a foundational, permanent attribute that is self-grounded, never defined in the text but consistently evidenced by what God is and does. God's righteousness is expressed through judgments that conform to what is right, through covenant faithfulness that extends across generations, and through saving acts directed toward his people. It is the standard against which human unrighteousness is measured, and the ground on which his people appeal for deliverance. In the NT, God's righteousness is revealed through the gospel and resolved through the cross — where the justice/mercy tension is explicitly reconciled by the declaration that God is simultaneously just and the justifier of those who have faith. The sub-group also includes messianic verses where the Righteous One (Christ) is defined by this quality and where God's righteousness becomes the means of transfer to human persons. Distinguished from M26-A2 (human righteousness) and from M26-C (the divine act of declaring a person righteous). Verses where both God and a human person are foregrounded as active subjects are held in M26-BOUNDARY.

### Operation 2 — Verse reassignment from M26-A1 to M26-BOUNDARY

The following 11 verse_context rows are to be reassigned. Each was classified as "both" in the analytical subject-classification file, meaning God and a human person are both active subjects in the verse.

| vr_id | mti_id | Reference | Term | Current sub-group | Destination sub-group |
|------:|-------:|-----------|------|------------------|----------------------|
| 93748 | 3193 | 1Jo 2:29 | G1342 dikaios | M26-A1 | M26-BOUNDARY |
| 93750 | 3193 | 1Jo 3:7 | G1342 dikaios | M26-A1 | M26-BOUNDARY |
| 28726 | 950 | 2Cor 5:21 | G1343 dikaiosunē | M26-A1 | M26-BOUNDARY |
| 25165 | 911 | Gen 15:6 | H6666 tse.da.qah | M26-A1 | M26-BOUNDARY |
| 28307 | 942 | Hos 10:12 | H6664G tse.deq | M26-A1 | M26-BOUNDARY |
| 25168 | 911 | Hos 10:12 | H6666 tse.da.qah | M26-A1 | M26-BOUNDARY |
| 25190 | 911 | Isa 56:1 | H6666 tse.da.qah | M26-A1 | M26-BOUNDARY |
| 25214 | 911 | Judg 5:11 | H6666 tse.da.qah | M26-A1 | M26-BOUNDARY |
| 93744 | 950 | Phili 3:9 | G1343 dikaiosunē | M26-A1 | M26-BOUNDARY |
| 169505 | 3246 | Psa 7:9 | H6662 tsad.diq | M26-A1 | M26-BOUNDARY |
| 28747 | 950 | Rom 10:4 | G1343 dikaiosunē | M26-A1 | M26-BOUNDARY |

**Note on Hos 10:12:** Two separate verse_context rows for this reference — vr_id 28307 (H6664G) and vr_id 25168 (H6666) — both present in M26-A1. Both are to be moved to BOUNDARY. vr_id 28307 is also listed in DIR-M26-20260510-001; the reassignment is the same target (BOUNDARY) regardless of which directive processes it first.

**Note on Pending (P) verses in M26-A1:** The current M26-A1 set includes 13 verse_context rows with status P (pending — relevant but no group assigned). These are not affected by this directive. Their group assignment is parked for a later analytical pass.

---

## COMPLETION CONFIRMATION

CC must confirm the following after execution, ideally run after both DIR-M26-20260510-001 and DIR-M26-20260510-002 have been applied:

**1. M26-A1 description updated:**
```sql
SELECT subgroup_code, label, description
FROM cluster_subgroup
WHERE cluster_code = 'M26' AND subgroup_code = 'M26-A1';
```
Expected: description field matches the new text above (or its first 100 characters confirm replacement).

**2. M26-A1 verse count after reassignment:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A1'
AND vc.status IN ('extracted', 'extracted_thin');
```
Expected: 157 (168 − 11 moved to BOUNDARY).

**3. Confirm all 11 vr_ids now in BOUNDARY:**
```sql
SELECT vc.id as vr_id, cs.subgroup_code, mt.strong, vc.verse_ref
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE vc.id IN (93748, 93750, 28726, 25165, 28307, 25168, 25190, 25214, 93744, 169505, 28747)
ORDER BY vc.verse_ref;
```
Expected: all 11 rows showing `subgroup_code = 'M26-BOUNDARY'`.

**4. Combined BOUNDARY count after both directives:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-BOUNDARY'
AND vc.status IN ('extracted', 'extracted_thin');
```
Note: The 11 "both" verses appear in both M26-A1 and M26-A2 (shared terms). The BOUNDARY count increase will reflect deduplicated verse_context rows, not double-counting. CC should report the actual pre- and post-move counts to confirm net change.

**5. Cross-directive consistency check — Hos 10:12:**
```sql
SELECT vc.id, cs.subgroup_code, mt.strong, vc.verse_ref
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE vc.id IN (28307, 25168);
```
Expected: both rows showing `subgroup_code = 'M26-BOUNDARY'`.

---

*DIR-M26-20260510-002 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11 | Companion: DIR-M26-20260510-001*
