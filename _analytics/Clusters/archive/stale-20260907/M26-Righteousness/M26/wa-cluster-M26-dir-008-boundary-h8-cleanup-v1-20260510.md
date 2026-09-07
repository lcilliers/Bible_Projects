# wa-cluster-M26-dir-008-boundary-h8-cleanup-v1-20260510

**Directive ID:** DIR-M26-20260510-008  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11  

---

## DIRECTIVE ID

DIR-M26-20260510-008

---

## MOTIVATION

Following DIR-006 and DIR-007 execution, v17 was read in full. Two categories of outstanding work identified:

**1. H8 residuals** — 9 of the 9 reported H8 VSGs were examined individually. Five are correctly split between M26-A2 and BOUNDARY (governance/national/forensic verses correctly held). Four VSGs contain BOUNDARY verses that should move to A2, plus two BOUNDARY verses using a wrong VSG code.

**2. H7 — H8200 she.phat** — one term with no VSGs (Ezr 7:25, vr_id 146258, status NR). Requires a VSG or confirmed NR treatment.

No new VSGs are required for items 1–2. All actions use existing VSG codes.

---

## SCOPE

**Tables:** `verse_context` — UPDATE subgroup_id, verse_context_group_id  
**Source:** M26-BOUNDARY  
**Destinations:** M26-A2 VSGs (942-001, 950-002, M26-A2-009, M26-A2-014, 3246-003)  
**Within-BOUNDARY reassignments:** 2 verses (911-003 → 942-002)  

---

## PHASE 1 — Within-BOUNDARY VSG reassignments (2 verses)

VSG 911-003 is now resident in M26-A1. Two BOUNDARY verses still carry the 911-003 code but describe God's righteousness — they should be reassigned to 942-002 (God's foundational attribute, the correct BOUNDARY God-righteousness VSG).

| vr_id | ref | term | current BOUNDARY VSG | → BOUNDARY VSG | reason |
|------:|-----|------|----------------------|----------------|--------|
| 169299 | Psa 11:7 | H6666 tse.da.qah | `911-003` | `942-002` | "The Lord is righteous; he loves righteous deeds; the upright shall behold his face." — describes God's character and his love of righteous deeds; fits 942-002 (God's foundational divine attribute). The second clause (upright behold his face) makes it a "both" verse, correctly held in BOUNDARY. |
| 25170 | Isa 10:22 | H6666 tse.da.qah | `911-003` | `942-002` | "Destruction is decreed, overflowing with righteousness." — God's righteous judgment overflowing, qualifying the decree; fits 942-002 (God's attribute expressed in acts). Complex context correctly held in BOUNDARY. |

**SQL pattern:**
```sql
UPDATE verse_context
SET verse_context_group_id = (
    SELECT id FROM verse_context_group WHERE group_code = '942-002'
    AND -- scoped to M26 cluster
)
WHERE id IN (169299, 25170);
```

---

## PHASE 2 — BOUNDARY → M26-A2 verse moves (9 verses)

All 9 verses move from M26-BOUNDARY to M26-A2. CC updates both `cluster_subgroup_id` (to M26-A2) and `verse_context_group_id` (to destination VSG). Status remains G.

### → M26-A2 / `942-001` (personal moral standing before God — appealed to in prayer)

| vr_id | ref | term | reason |
|------:|-----|------|--------|
| 28339 | Job 31:6 | H6664G tse.deq | "Let me be weighed in a just balance, and let God know my integrity!" — direct personal appeal to God to assess righteousness; exact match to 942-001 pattern. |
| 96036 | Psa 94:15 | H6664G tse.deq | "Justice will return to the righteous, and all the upright in heart will follow it." — the righteous person's standing rewarded as justice returns to them; fits the "standing God sees and vindicates" pattern of 942-001. |

### → M26-A2 / `M26-A2-014` (relational orientation toward God)

| vr_id | ref | term | reason |
|------:|-----|------|--------|
| 96006 | Psa 15:2 | H6664G tse.deq | "He who walks blamelessly and does what is right and speaks truth in his heart." — describes who may dwell on God's holy hill; righteousness as the qualification for God's presence — the defining statement of relational orientation toward God. |

### → M26-A2 / `3246-003` (inner response of righteous person — gladness, praise, thanksgiving)

| vr_id | ref | term | reason |
|------:|-----|------|--------|
| 96002 | Psa 119:62 | H6664G tse.deq | "At midnight I rise to praise you, because of your righteous rules." — rising at midnight to praise; intense inner response to God's righteous rules. |
| 96000 | Psa 119:164 | H6664G tse.deq | "Seven times a day I praise you for your righteous rules." — repeated daily praise as the righteous person's sustained inner response. |
| 96001 | Psa 119:172 | H6664G tse.deq | "My tongue will sing of your word, for all your commandments are right." — singing as inner response to the rightness of God's commandments. |

### → M26-A2 / `950-002` (practiced, lived orientation — daily direction of conduct)

| vr_id | ref | term | reason |
|------:|-----|------|--------|
| 28765 | Rom 6:13 | G1343 dikaiosunē | "Present yourselves to God as those brought from death to life, and your members to God as instruments of righteousness." — bodily presentation as instruments of righteousness; the lived, embodied dimension of the practiced orientation. |

### → M26-A2 / `M26-A2-009` (righteousness as something worn — clothing, armour, escort)

| vr_id | ref | term | reason |
|------:|-----|------|--------|
| 28728 | 2Cor 6:7 | G1343 dikaiosunē | "With the weapons of righteousness for the right hand and for the left." — righteousness as active defensive and offensive equipment worn in ministry; fits the armour dimension of M26-A2-009. |

---

## PHASE 3 — H7: H8200 she.phat assessment

**vr_id 146258** (Ezr 7:25, H8200 she.phat, status NR, BOUNDARY, ungrouped):

> "And you, Ezra, according to the wisdom of your God that is in your hand, appoint magistrates and judges who may judge all the people in the province Beyond the River, all such as know the laws of your God."

H8200 she.phat is the Aramaic cognate of H8199 sha.phat (judge). This verse describes Ezra being commissioned to appoint judges — a governance/administrative act. There is no inner-being content in this verse specific to the term she.phat. The term carries the judicial appointment function only.

**Assessment:** Status NR (not relevant) is correct. No VSG can be authored for this single verse at this stage without evidence of inner-being content. The term should remain NR in BOUNDARY.

**Action:** No DB change required. Confirm to CC that H7 × 1 (she.phat) is correctly NR and no VSG is required. This is a satisfactory terminal state for this term in M26.

---

## PHASE 4 — Verification

**1. Confirm Phase 1 within-BOUNDARY reassignments:**
```sql
SELECT vc.id, vc.verse_ref, vcg.group_code
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
WHERE vc.id IN (169299, 25170);
```
Expected: both rows → `group_code = '942-002'`.

**2. Confirm Phase 2 moves to M26-A2:**
```sql
SELECT vc.id, vc.verse_ref, cs.subgroup_code, vcg.group_code
FROM verse_context vc
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE vc.id IN (28339, 96036, 96006, 96002, 96000, 96001, 28765, 28728)
AND mt.cluster_code = 'M26';
```
Expected:
- 28339, 96036 → M26-A2 / 942-001
- 96006 → M26-A2 / M26-A2-014
- 96002, 96000, 96001 → M26-A2 / 3246-003
- 28765 → M26-A2 / 950-002
- 28728 → M26-A2 / M26-A2-009

**3. Confirm H8 count reduced from 9:**
```sql
-- Run the H8 multi-subgroup VSG check
SELECT vcg.group_code, COUNT(DISTINCT cs.subgroup_code) as subgroup_count,
       GROUP_CONCAT(DISTINCT cs.subgroup_code) as subgroups
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.verse_context_group_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M26'
AND vc.status IN ('extracted', 'extracted_thin', 'G')
GROUP BY vcg.group_code
HAVING subgroup_count > 1
ORDER BY vcg.group_code;
```
Expected: reduced count. 911-003 should now appear in M26-A1 only (BOUNDARY verses reassigned to 942-002). 942-001, 942-003, 950-002 should have BOUNDARY populations reduced.

**4. Confirm BOUNDARY final count:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-BOUNDARY'
AND vc.status IN ('extracted', 'extracted_thin', 'G');
```
Expected: 66 (75 − 9 moved to A2).

**5. Report final M26 sub-group verse counts:**
```sql
SELECT cs.subgroup_code, COUNT(*) as verse_count,
       SUM(CASE WHEN vc.status = 'G' THEN 1 ELSE 0 END) as grouped,
       SUM(CASE WHEN vc.status = 'SA' THEN 1 ELSE 0 END) as set_aside,
       SUM(CASE WHEN vc.status = 'NR' THEN 1 ELSE 0 END) as not_relevant
FROM verse_context vc
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M26'
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
```

---

## OUTSTANDING ITEMS NOT ADDRESSED IN THIS DIRECTIVE

**H8 × residual:** After Phase 2, remaining H8 VSGs (911-001, 911-002, 3246-002, 3246-003) are correctly split between A2 and BOUNDARY — their BOUNDARY verses are governance/forensic/national material appropriately held. No further action required on these.

**A1 VSG term column display:** M26-A1-002 shows G1738 endikos, M26-A1-004 shows H8196 she.phot, M26-A1-007 shows G0159 aitios as representative terms — these are display artefacts from the last-added verse, not data integrity issues. CC to note.

**M26 analytical work complete.** All sub-groups structured, all verses assigned or correctly set aside. M26 is ready for Session C (findings/report writing).

---

*DIR-M26-20260510-008 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11*
