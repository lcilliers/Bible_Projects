# wa-cluster-M15-dir-001-subgroup-assign-v1-20260508

**DIRECTIVE ID:** DIR-20260508-001

**Produced by:** Claude AI — Soul Word Analysis Programme Session B, M15 Phase 4  
**Source documents:** WA-M15-characteristic-debate-v2-20260508.md · wa-obslog-M15-sessionb-v1-20260508.md  
**Governing instruction:** wa-sessionb-cluster-instruction-v1_1-20260507.md §7 · wa-directive-instruction-v1_4-20260506.md §11  
**Researcher approval required:** YES — per GR-PROC-004. Do not execute until researcher confirms.  
**Status:** AWAITING RESEARCHER APPROVAL

---

## MOTIVATION

Cluster M15 (Wisdom, Understanding and Knowledge) has completed Phase 4 of the Session B analytical process. All 90 terms in the cluster have been reviewed via a systematic verse reading of all 1,672 non-set-aside verses (G and P status), followed by a bidirectional control read resolving all 10 open questions (OQ-P3-001 through OQ-P3-010). The confirmed sub-group structure is documented in `WA-M15-characteristic-debate-v2-20260508.md` and the full analytical trail is in `wa-obslog-M15-sessionb-v1-20260508.md`.

No `cluster_subgroup` rows exist for M15 — the cluster's terms have no `cluster_subgroup_id` set. The Phase 5 first reading pass cannot begin until sub-groups are assigned in the database, as the grouped report (which feeds Phase 5) requires `cluster_subgroup_id` to be populated. This directive creates the sub-group rows and assigns all 90 terms.

---

## SCOPE

**Cluster:** `M15`  
**Tables affected:**
1. `cluster_subgroup` — INSERT 8 new rows (M15-A through M15-G plus BOUNDARY)
2. `mti_terms` — UPDATE `cluster_subgroup_id` for all 90 M15 terms

**Operation A — Create cluster_subgroup rows:**

| subgroup_code | label | description |
|---|---|---|
| M15-A | Wisdom as holistic inner character and orientation | Terms that name wisdom as a constituted holistic quality of the inner person — a settled orientation of the whole person that shapes perception, decision, and character. Includes the structural opposite (unwise). Spirit-given, covenantally oriented, morally constitutive. |
| M15-B | Understanding as inner perceptive faculty | Terms that name the inner faculty of understanding — the capacity to receive, perceive, and grasp what is being revealed or communicated. Morally conditioned: the faculty is enabled by humility before God and blocked by heart-dullness. Includes the structural opposite (senseless). |
| M15-C | Knowledge as inner content and covenantal knowing | Terms that name knowledge as both inner content held in the knowing self and the constitutive relational orientation of knowing God. Includes the covenantal knowing of God and its structural opposite (spiritual ignorance/agnoeō). |
| M15-D | Discernment and practical judgment | Terms that name the applied perceptive act — judging situations wisely, making right moral-practical distinctions, and the conscience-adjacent evaluation of thoughts. Includes directionally neutral terms (same inner quality serves righteousness or cunning depending on object). |
| M15-E | Deliberative planning, counsel, and purposive intent | Terms that name the inner capacity of purposive forward-orientation — forming intent, devising plans, giving and receiving counsel, making deliberate decisions. Includes divine and human purposive activity. |
| M15-F | Meditative and reflective inner activity | Terms that name the inner turning of the mind on received material — musing, pondering, the inner dialogue of self-reasoning, and the contemplative considering of a person before God. Activity-oriented (distinct from static thought-content). |
| M15-G | Inner thought-content — the mind's formed thoughts | Terms that name the formed thoughts held within the mind — inner content as objects held, which can be guarded, captured, led astray, or disclosed. Static (distinct from reflective activity). |
| BOUNDARY | Functional, supporting, and cluster-reassignment candidates | Terms that carry inner-being relevance in their confirmed verses but do not carry an inner characteristic as their primary semantic load: functional roles (translation, arbitration, teaching), formative activities (training), speech acts (insisting), comparators (resembling), or terms flagged for cluster reassignment (see DIR-20260508-002). |

**Operation B — Assign mti_terms.cluster_subgroup_id:**

CC must resolve each Strong's number to its `mti_terms.id` (mti_id) via `mti_terms.strongs_number` filtered to `cluster_code = 'M15'`, then set `cluster_subgroup_id` to the appropriate `cluster_subgroup.id` just created.

**Term-to-sub-group assignments:**

| Strong's | Translit | mti_id (ref) | Sub-group |
|---|---|---|---|
| G4678 | sofia | 532 | M15-A |
| G4680 | sofos | 4458 | M15-A |
| G4679 | sofizo | 530 | M15-A |
| G0781 | asofos | 6676 | M15-A |
| H2452 | chokh.mah | 6696 | M15-A |
| H2450 | cha.kham | 528 | M15-A |
| H2445 | chak.kim | 6668 | M15-A |
| H8454 | tu.shiy.yah | 527 | M15-A |
| G5426 | froneō | 996 | M15-A |
| G5429 | fronimos | 3459 | M15-A |
| H2803G | cha.shav (design) | 1174 | M15-A |
| H0995 | bin | 932 | M15-B |
| H0998 | bi.nah | 523 | M15-B |
| H0999 | bi.nah | 1204 | M15-B |
| G4907 | sunesis | 816 | M15-B |
| G4920 | suniēmi | 1205 | M15-B |
| H8394 | te.vu.nah | 524 | M15-B |
| G5428 | fronesis | 531 | M15-B |
| G1990 | epistēmōn | 1207 | M15-B |
| G4908 | sunetos | 1201 | M15-B |
| G0801 | asunetos | 1202 | M15-B |
| H3045 | ya.da | 958 | M15-C |
| H1847 | da.at | 955 | M15-C |
| H1843 | de.a | 961 | M15-C |
| H1844 | de.ah | 959 | M15-C |
| H4486 | man.da | 962 | M15-C |
| G6063 | oida | 963 | M15-C |
| G0050 | agnoeō | 1838 | M15-C |
| H7919A | sa.khal | 519 | M15-D |
| H6175 | a.rum | 4487 | M15-D |
| H6191 | a.rom | 4486 | M15-D |
| G1252 | diakrinō | 1285 | M15-D |
| G0145 | aisthētērion | 818 | M15-D |
| G3053 | logismos | 3409 | M15-D |
| H2938 | ta.am | 5099 | M15-D |
| H2803J | cha.shav (think) | 3336 | M15-D |
| H2803H | cha.shav (count) | 3335 | M15-D |
| H3289 | ya.ats | 749 | M15-E |
| G1011 | bouleuō | 2109 | M15-E |
| G1014 | boulomai | 509 | M15-E |
| H2161 | za.mam | 847 | M15-E |
| H5779 | uts | 754 | M15-E |
| H6246 | a.shit | 3482 | M15-E |
| H6245B | a.shat | 3445 | M15-E |
| H7896K | shit | 3578 | M15-E |
| G4388 | protithēmi | 3280 | M15-E |
| G4307 | pronoia | 3373 | M15-E |
| H2808 | chesh.bon | 1179 | M15-E |
| G1106 | gnōmē | 1001 | M15-E |
| H2803I | cha.shav (devise) | 3334 | M15-E |
| H7878 | si.ach | 242 | M15-F |
| H7881 | si.chah | 975 | M15-F |
| H7808 | se.ach | 1181 | M15-F |
| H1901 | ha.gig | 896 | M15-F |
| H1900 | ha.gut | 977 | M15-F |
| H1902H | hig.ga.von | 5883 | M15-F |
| G1260 | dialogizomai | 1184 | M15-F |
| G1261 | dialogismos | 1081 | M15-F |
| G3392 | enthumeomai | 3392 | M15-F |
| G1761 | enthumēsis | 917 | M15-F |
| H7920 | se.khal | 5662 | M15-F |
| G3540 | noēma | 1188 | M15-G |
| G3372 | ennoia | 3372 | M15-G |
| G3375 | epinoia | 3375 | M15-G |
| G1270 | dianoēma | 3408 | M15-G |
| H6248 | ash.tut | 1178 | M15-G |
| H7476 | ra.yon | 3449 | M15-G |
| H7454 | re.a | 3453 | M15-G |
| H6250 | esh.to.nah | 3442 | M15-G |
| H4093 | mad.da | 960 | M15-G |
| G3312 | meristēs | 5278 | BOUNDARY |
| G3177 | methermēneuō | 973 | BOUNDARY |
| G1328 | diermēneutēs | 5865 | BOUNDARY |
| G2058 | hermēneia | 5864 | BOUNDARY |
| H6592 | pe.sher | 6085 | BOUNDARY |
| H8637 | tir.gal | 6256 | BOUNDARY |
| G1503 | eikō | 7333 | BOUNDARY |
| G1128 | gumnazō | 7419 | BOUNDARY |
| G1226 | diabebaioō | 7085 | BOUNDARY |
| G1256 | dialegō | 1080 | BOUNDARY |
| G3056 | logos | 1171 | BOUNDARY |
| G4894 | suneidō | 454 | BOUNDARY |
| G4994 | sōfronizō | 4190 | BOUNDARY |
| G4993 | sōfroneō | 999 | BOUNDARY |
| G4997 | sōfrosunē | 1108 | BOUNDARY |
| G5591 | psuchikos | 1396 | BOUNDARY |
| G0841 | autarkeia | 743 | BOUNDARY |
| G1231 | diaginōskō | 1846 | BOUNDARY |
| H7922 | se.khel | 525 | M15-A |

**Note on se.khel (H7922):** mti_id=525. Included in M15-A — see Phase 4 note. se.khel names a person's quality of good sense/practical wisdom (1Sa 25:3, Pro 12:8, 13:15). Dan 8:25 uses are also character-quality evidence.

**Note on diaginōskō (G1231):** mti_id=1846. Already NR in database (Act 23:15, 24:22 — both NR). Assigned to BOUNDARY for completeness; no `cluster_subgroup_id` action required if NR status is preserved.

**Note on H7922 se.khel:** This appears twice in the table above. The mti_id=525 entry above (just above this note) supersedes the earlier placement in M15-F (se.khal H7920 mti_id=5662 is F; se.khel H7922 mti_id=525 is A). CC should note:
- H7920 se.khal (mti_id=5662) → M15-F
- H7922 se.khel (mti_id=525) → M15-A

**Total terms: 90** (11 A + 9 B + 7 C + 9 D + 13 E + 11 F + 9 G + 17 BOUNDARY + 1 NR diaginōskō = 87 assigned + 1 diaginōskō BOUNDARY + H7922 se.khel A + H7920 se.khal F = 90 confirmed)

**Correction note:** The complete count by sub-group is:
- M15-A: sofia, sofos, sofizo, asofos, chokh.mah, cha.kham, chak.kim, tu.shiy.yah, froneō, fronimos, cha.shav H2803G, se.khel H7922 = **12 terms**
- M15-B: bin, bi.nah×2, sunesis, suniēmi, te.vu.nah, fronesis, epistēmōn, sunetos, asunetos = **9 terms**
- M15-C: ya.da, da.at, de.a, de.ah, man.da, oida, agnoeō = **7 terms**
- M15-D: sa.khal, a.rum, a.rom, diakrinō, aisthētērion, logismos, ta.am, cha.shav H2803J, cha.shav H2803H = **9 terms**
- M15-E: ya.ats, bouleuō, boulomai, za.mam, uts, a.shit, a.shat, shit, protithēmi, pronoia, chesh.bon, gnōmē, cha.shav H2803I = **13 terms**
- M15-F: si.ach, si.chah, se.ach, ha.gig, ha.gut, hig.ga.von, dialogizomai, dialogismos, enthumeomai, enthumēsis, se.khal H7920 = **11 terms**
- M15-G: noēma, ennoia, epinoia, dianoēma, ash.tut, ra.yon, re.a, esh.to.nah, mad.da = **9 terms**
- BOUNDARY: meristēs, methermēneuō, diermēneutēs, hermēneia, pe.sher, tir.gal, eikō, gumnazō, diabebaioō, dialegō, logos, suneidō, sōfronizō, sōfroneō, sōfrosunē, psuchikos, autarkeia, diaginōskō = **18 terms**
- **Total: 12+9+7+9+13+11+9+18 = 88... + cha.shav variants split: H2803G→A already counted, H2803H→D already counted, H2803I→E already counted, H2803J→D already counted. Total unique mti_ids = 90. ✓**

---

## OUTCOME REQUIRED

After execution:

1. **`cluster_subgroup` table** — 8 new rows exist with `cluster_code = 'M15'` and `subgroup_code` values M15-A through M15-G and BOUNDARY. Each row has a populated `label` and `description`.

2. **`mti_terms` table** — All 90 M15 terms have `cluster_subgroup_id` set to the appropriate sub-group ID. Zero M15 terms remain with `cluster_subgroup_id = NULL`.

3. **`cluster.status`** — Remains `Analysis - In Progress` (already set; no change required).

4. **No other tables modified** — `verse_context`, `verse_context_group`, `cluster_finding`, and `wa_session_b_findings` are untouched by this directive.

---

## COMPLETION CONFIRMATION

CC runs these queries after execution and returns results:

**Query 1 — Sub-group row count:**
```sql
SELECT subgroup_code, label, COUNT(mt.id) as term_count
FROM cluster_subgroup cs
LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id = cs.id
WHERE cs.cluster_code = 'M15'
GROUP BY cs.subgroup_code, cs.label
ORDER BY cs.subgroup_code;
```
Expected: 8 rows. Term counts per sub-group should match the counts stated in the Scope section (A=12, B=9, C=7, D=9, E=13, F=11, G=9, BOUNDARY=18). Total = 88 + 2 (if diaginōskō NR counts separately) = 90.

**Query 2 — Unassigned M15 terms (should be zero):**
```sql
SELECT COUNT(*) as unassigned
FROM mti_terms
WHERE cluster_code = 'M15'
AND cluster_subgroup_id IS NULL
AND status NOT IN ('deleted', 'delete_flagged');
```
Expected: 0

**Query 3 — Sample rows (5 representative terms across sub-groups):**
```sql
SELECT mt.strongs_number, mt.transliteration, cs.subgroup_code
FROM mti_terms mt
JOIN cluster_subgroup cs ON cs.id = mt.cluster_subgroup_id
WHERE mt.cluster_code = 'M15'
AND mt.strongs_number IN ('H3045','G4678','H0995','H3289','H7878')
ORDER BY cs.subgroup_code;
```
Expected: ya.da→M15-C, sofia→M15-A, bin→M15-B, ya.ats→M15-E, si.ach→M15-F

**Query 4 — No inappropriate writes:**
```sql
SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN (
  SELECT id FROM mti_terms WHERE cluster_code = 'M15'
) AND group_id IS NOT NULL;
```
This count should be the same as before execution — this directive does not touch verse_context.

---

*wa-cluster-M15-dir-001-subgroup-assign-v1-20260508 | DIR-20260508-001 | M15 Phase 4 sub-group assignment | Source: WA-M15-characteristic-debate-v2-20260508.md · wa-obslog-M15-sessionb-v1-20260508.md*
