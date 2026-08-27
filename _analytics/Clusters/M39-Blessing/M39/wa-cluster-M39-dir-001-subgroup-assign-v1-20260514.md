# wa-cluster-M39-dir-001-subgroup-assign-v1-20260514

**Cluster:** M39 — Blessing, Favour and Grace  
**Directive sequence:** dir-001  
**Pattern:** cluster-process directive per wa-directive-instruction [current] §11.4  
**Authored by:** Claude AI  
**Date:** 2026-05-14  
**Status:** AWAITING RESEARCHER REVIEW — do not apply until approved

---

## MOTIVATION

This directive assigns all 16 terms in cluster M39 to analytical sub-groups, completing Phase 4 of the Session B cluster analysis.

The sub-group structure was determined by:
1. Phase 3 characteristic debate (WA-M39-characteristic-debate-v1-20260514.md) — provisional groupings from gloss-level reading applying the T1 five-criterion framework
2. Phase 4 bidirectional control read (wa-obslog-M39-sessionb-v1-20260514.md, Phase 4 section) — validated groupings against §3 per-term comprehensive detail

Researcher approved the confirmed sub-group structure 2026-05-14 before this directive was authored.

Two sub-groups carry characteristic-bearing terms (M39-A and M39-B). One BOUNDARY sub-group holds supportive/descriptive/undecided terms (G1435 dōron, H7862 shay, H2868 te.ev) pending verse-level validation.

No terms move out of cluster M39 — Operation B (cluster_code rebind) is not required.

---

## SCOPE

### Operation A — cluster_subgroup CREATE and mti_terms.cluster_subgroup_id ASSIGN

**Step A1: Create three cluster_subgroup rows**

| Field | M39-A | M39-B | M39-BOUNDARY |
|---|---|---|---|
| cluster_code | M39 | M39 | M39 |
| subgroup_code | M39-A | M39-B | M39-BOUNDARY |
| label | Blessing and Grace | Goodness | BOUNDARY |
| description | The sovereign, initiated movement of the greater toward the lesser — God's blessing, grace, and favour as dispositioned gift; the inner-being characteristic in which one person (primarily God) constitutes favour, standing, and inner transformation in another who cannot earn or generate it. Terms span the act of blessing (ba.rakh), the noun of grace-disposition (charis, chen), the verbal act of being gracious (cha.nan), the act of grace-giving (charizō), the completed standing-in-grace (charitoō), the divine inner pleasure as ground of blessing (eudokia), the character-type of graciousness (chan.nun), the grace-endowment (charisma), and the acceptance/delight face of the grace dynamic (ra.tsah). | The inner moral-affective quality of being good — the character of the person or act assessed as genuinely good, morally right, and producing goodness in community and relationship. Includes the moral evaluation faculty, the affective gladness-at-good, and the volitional preference for what is genuinely beneficial. Terms: ya.tav (bridging moral goodness, affective gladness, and approval-of-good) and tov (the broadest OT goodness term covering moral rightness, covenantal reliability, and volitional preference). | Temporary holding group for terms that are supportive, descriptive, qualifying, or undecided pending verse-level analysis. Per programme BOUNDARY conventions, terms here are re-evaluated during Phase 10 and must exit BOUNDARY before cluster closure. |
| is_boundary | 0 | 0 | 1 |

**Step A2: Assign mti_terms.cluster_subgroup_id for all 16 terms**

| mti_id | Strong's | Translit | Gloss | Target subgroup_code |
|---|---|---|---|---|
| 1299 | H1288 | ba.rakh | to bless | M39-A |
| 888 | G5485 | charis | grace | M39-A |
| 984 | H2603A | cha.nan | be gracious | M39-A |
| 889 | H2580 | chen | favor | M39-A |
| 5470 | G5483 | charizō | to give grace | M39-A |
| 5471 | G5487 | charitoō | to favor | M39-A |
| 494 | G2107 | eudokia | goodwill | M39-A |
| 2330 | H2587 | chan.nun | gracious | M39-A |
| 1301 | G5486 | charisma | gift | M39-A |
| 989 | H2604 | cha.nan | be gracious | M39-A |
| 795 | H7521 | ra.tsah | to accept | M39-A |
| 632 | H3190 | ya.tav | be good | M39-B |
| 542 | H2895 | tov | be pleasing | M39-B |
| 6837 | G1435 | dōron | gift | M39-BOUNDARY |
| 2976 | H7862 | shay | gift | M39-BOUNDARY |
| 633 | H2868 | te.ev | be good | M39-BOUNDARY |

### Operation B — cluster_code rebind

**NOT REQUIRED.** No terms move out of cluster M39. All 16 terms retain cluster_code = 'M39'.

### Operation C — cluster.status transition

UPDATE cluster SET status = 'Analysis - In Progress' WHERE cluster_code = 'M39'.

This transition fires as the final step of this directive's operation succession, after Operations A1 and A2 complete successfully.

---

## OUTCOME REQUIRED

After successful application:

1. Three `cluster_subgroup` rows exist for cluster M39:
   - subgroup_code = 'M39-A', label = 'Blessing and Grace', is_boundary = 0
   - subgroup_code = 'M39-B', label = 'Goodness', is_boundary = 0
   - subgroup_code = 'M39-BOUNDARY', label = 'BOUNDARY', is_boundary = 1

2. All 16 mti_terms rows for cluster M39 have cluster_subgroup_id populated (none NULL):
   - M39-A: 11 terms (mti_ids: 1299, 888, 984, 889, 5470, 5471, 494, 2330, 1301, 989, 795)
   - M39-B: 2 terms (mti_ids: 632, 542)
   - M39-BOUNDARY: 3 terms (mti_ids: 6837, 2976, 633)
   - Total assigned: 16

3. Operation B: no rebind rows — count = 0

4. cluster.status = 'Analysis - In Progress' for cluster_code = 'M39'

---

## COMPLETION CONFIRMATION

CC runs the following queries after applying this directive and returns results to the researcher for verification:

**Query 1 — Sub-group counts by subgroup_code:**
```sql
SELECT cs.subgroup_code, cs.label, COUNT(mt.id) AS term_count
FROM cluster_subgroup cs
LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id = cs.id
WHERE cs.cluster_code = 'M39'
GROUP BY cs.subgroup_code, cs.label
ORDER BY cs.subgroup_code;
```
Expected result:
| subgroup_code | label | term_count |
|---|---|---|
| M39-A | Blessing and Grace | 11 |
| M39-B | Goodness | 2 |
| M39-BOUNDARY | BOUNDARY | 3 |

**Query 2 — All M39 terms with their assigned subgroup_code (verify no NULLs):**
```sql
SELECT mt.id AS mti_id, mt.strongs_id, mt.transliteration, mt.gloss,
       cs.subgroup_code
FROM mti_terms mt
LEFT JOIN cluster_subgroup cs ON cs.id = mt.cluster_subgroup_id
WHERE mt.cluster_code = 'M39'
  AND mt.status IN ('extracted', 'extracted_thin')
ORDER BY cs.subgroup_code, mt.strongs_id;
```
Expected: 16 rows, no NULL in subgroup_code column.

**Query 3 — Cluster status:**
```sql
SELECT cluster_code, status FROM cluster WHERE cluster_code = 'M39';
```
Expected: cluster_code = 'M39', status = 'Analysis - In Progress'

**Query 4 — H1 connectivity health post-assign (sub-group routing check):**
```sql
SELECT COUNT(*) AS unrouted_vc_rows
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M39'
  AND mt.status IN ('extracted', 'extracted_thin')
  AND vc.cluster_subgroup_id IS NULL;
```
Expected: count > 0 is acceptable at this stage (verse_context.cluster_subgroup_id is populated in Phase 7, not Phase 4). This query is for baseline recording only — not a pass/fail check.

---

## APPLICATION NOTES FOR CC

- Operations A1, A2, and C execute in succession within a single transaction
- Rollback if any operation fails
- If cluster_subgroup rows for M39 already exist (re-run scenario), confirm row counts before proceeding; do not create duplicates
- The is_boundary flag = 1 for M39-BOUNDARY; = 0 for M39-A and M39-B
- All mti_terms updates set cluster_subgroup_id to the id of the newly created cluster_subgroup row (not the subgroup_code string)
- Operation C executes only after A1 and A2 complete successfully

---

*wa-cluster-M39-dir-001-subgroup-assign-v1-20260514*  
*References: WA-M39-characteristic-debate-v1-20260514.md | wa-obslog-M39-sessionb-v1-20260514.md*  
*Previous output: wa-cluster-M39-patch-vcnew-utreview-v1-20260514.json*
