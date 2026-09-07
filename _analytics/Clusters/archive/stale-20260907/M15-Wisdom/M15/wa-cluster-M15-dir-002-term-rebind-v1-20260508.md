# wa-cluster-M15-dir-002-term-rebind-v1-20260508

**DIRECTIVE ID:** DIR-20260508-002

**Produced by:** Claude AI — Soul Word Analysis Programme Session B, M15 Phase 4  
**Source documents:** WA-M15-characteristic-debate-v2-20260508.md · wa-obslog-M15-sessionb-v1-20260508.md  
**Governing instruction:** wa-sessionb-cluster-instruction-v1_1-20260507.md §7 · wa-directive-instruction-v1_4-20260506.md §11.6  
**Dependency:** Execute AFTER DIR-20260508-001 is confirmed complete.  
**Researcher approval required:** YES — per GR-PROC-004. Do not execute until researcher confirms.  
**Status:** AWAITING RESEARCHER APPROVAL

---

## MOTIVATION

Phase 4 of the M15 Session B analytical pass identified three terms currently in M15 whose confirmed verse evidence does not support placement in a wisdom/knowledge/understanding cluster. These terms carry inner-being relevance but their primary semantic load belongs to a different characteristic domain. The terms were placed in the M15 BOUNDARY sub-group by DIR-20260508-001 pending this reassignment directive.

The three terms and their analytical basis for reassignment:

**1. G0841 autarkeia (self-sufficiency/contentment):**  
Confirmed verses: 2Cor 9:8 ("having all sufficiency in all things"), 1Ti 6:6 ("godliness with contentment is great gain"), Phili 4:11 (contentment in all circumstances). autarkeia names inner contentment and self-sufficient adequacy — not a wisdom characteristic but an inner state of relational-emotional sufficiency independent of circumstances. This belongs to a contentment/peace cluster, not M15.

**2. G4993 sōfroneō (be of sound mind), G4994 sōfronizō (to train to soundness), G4997 sōfrosunē (mental soundness/self-control):**  
Confirmed verses: Rom 12:3 ("think with sober judgment"), Tit 2:4 ("train young women"), Tit 2:6 ("urge younger men to be self-controlled"), 1Pe 4:7 ("be self-controlled and sober-minded"), 1Ti 2:9 ("with modesty and self-control"), 1Ti 2:15 ("holiness with self-control"), Act 26:25 ("speaking true and rational words"). The cluster consistently names inner orderliness, self-governance, and sobriety of mind — not wisdom-as-character or discernment-as-faculty. This is a self-regulation/temperance cluster characteristic, not a wisdom/knowledge characteristic.

**3. G5591 psuchikos (natural/unspiritual):**  
Confirmed verses: Jam 3:15 ("earthly, unspiritual, demonic" — qualifier of false wisdom), Jude 19 ("worldly people, devoid of the Spirit"). psuchikos is a TYPE 2 qualifier — it characterises the category of person lacking the Spirit, not an inner characteristic itself. It is a qualifier of persons, not a characteristic held by persons.

These three terms (four mti_ids: autarkeia, sōfroneō, sōfronizō, sōfrosunē, psuchikos = 5 mti_ids) require reassignment out of M15. The receiving cluster is not yet determined for all of them; the correct action is to move them to a holding state — either their original cluster or a FLAG state — pending researcher decision on receiving cluster.

**Researcher decision required before execution:** What cluster should these terms be moved to? Options:
- Move to FLAG cluster (temporary holding for researcher review)
- Move to an existing cluster identified by the researcher (e.g. a self-control or contentment cluster)
- Retain in M15 BOUNDARY if the receiving cluster is not yet established

This directive is authored but **should not be executed until the researcher confirms the receiving cluster for each term.** CC should not improvise the destination.

---

## SCOPE

**Source cluster:** M15  
**Table:** `mti_terms` — column `cluster_code` and `cluster_subgroup_id`  
**Terms affected (5 mti_ids):**

| Strong's | Translit | mti_id | Current cluster | Receiving cluster |
|---|---|---|---|---|
| G0841 | autarkeia | 743 | M15 | **[RESEARCHER TO CONFIRM]** |
| G4993 | sōfroneō | 999 | M15 | **[RESEARCHER TO CONFIRM]** |
| G4994 | sōfronizō | 4190 | M15 | **[RESEARCHER TO CONFIRM]** |
| G4997 | sōfrosunē | 1108 | M15 | **[RESEARCHER TO CONFIRM]** |
| G5591 | psuchikos | 1396 | M15 | **[RESEARCHER TO CONFIRM]** |

**Operations (pending researcher confirmation):**
- For each term: UPDATE `mti_terms` SET `cluster_code = '{receiving_cluster}'`, `cluster_subgroup_id = NULL` WHERE `id = {mti_id}`
- The BOUNDARY `cluster_subgroup_id` assigned by DIR-20260508-001 should be cleared (set to NULL) as part of the move, since the term is leaving M15.

**Cluster sub-group impact:**  
After removal, the M15 BOUNDARY sub-group loses 5 terms (from 18 to 13). This is expected and correct.

---

## OUTCOME REQUIRED

After execution (once receiving clusters are confirmed):

1. The 5 named terms have `cluster_code` set to their respective receiving clusters (not M15).
2. The 5 named terms have `cluster_subgroup_id = NULL` (cleared from M15 BOUNDARY).
3. M15 term count decreases from 90 to 85.
4. The receiving cluster(s) term counts increase correspondingly.
5. No `verse_context` or `cluster_finding` rows for these terms are deleted — data is preserved for the receiving cluster's analysis.

---

## COMPLETION CONFIRMATION

**Query 1 — Confirm terms left M15:**
```sql
SELECT strongs_number, transliteration, cluster_code, cluster_subgroup_id
FROM mti_terms
WHERE strongs_number IN ('G0841','G4993','G4994','G4997','G5591');
```
Expected: cluster_code ≠ 'M15' for all 5; cluster_subgroup_id = NULL for all 5.

**Query 2 — M15 term count:**
```sql
SELECT COUNT(*) FROM mti_terms WHERE cluster_code = 'M15';
```
Expected: 85 (down from 90).

**Query 3 — M15 BOUNDARY sub-group count:**
```sql
SELECT COUNT(*) as boundary_terms
FROM mti_terms mt
JOIN cluster_subgroup cs ON cs.id = mt.cluster_subgroup_id
WHERE mt.cluster_code = 'M15' AND cs.subgroup_code = 'BOUNDARY';
```
Expected: 13 (down from 18 after the 5 reassignments).

---

## NOTE ON EXECUTION DEPENDENCY

This directive is a companion to DIR-20260508-001. The correct execution sequence is:
1. Researcher approves DIR-20260508-001 → CC executes and confirms
2. Researcher confirms receiving clusters for the 5 terms above
3. Researcher approves DIR-20260508-002 → CC executes and confirms

DIR-20260508-002 should not be executed before DIR-20260508-001 is confirmed, and should not be executed without researcher confirmation of receiving clusters.

---

*wa-cluster-M15-dir-002-term-rebind-v1-20260508 | DIR-20260508-002 | M15 Phase 4 cluster reassignment | Source: WA-M15-characteristic-debate-v2-20260508.md · wa-obslog-M15-sessionb-v1-20260508.md*
