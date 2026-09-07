# wa-cluster-M05-dir-002-subgroup-assign-v1-20260507

> Framework B Soul Word Analysis Programme — Cluster-process Directive
> Cluster: M05 — Love, Compassion and Kindness
> Directive sequence: dir-002 (sub-group assignment)
> Version: v1 | Date: 20260507
> Instruction: wa-directive-instruction-v1_4-20260506 §11.3, §11.4
> Session B Instruction: wa-sessionb-cluster-instruction-v1_1-20260507 §7
> Status: READY FOR CC EXECUTION — researcher OQ dispositions confirmed 2026-05-07

---

## DIRECTIVE ID

`DIR-20260507-M05-002`

---

## MOTIVATION

The M05 cluster (Love, Compassion and Kindness) has completed the Phase 3 characteristic debate and Phase 4 control read per `wa-sessionb-cluster-instruction-v1_1-20260507`. The control read produced the confirmed sub-group structure across 7 characteristic sub-groups plus one BOUNDARY sub-group, with 5 open questions all resolved by researcher confirmation on 2026-05-07.

Source documents:
- `WA-M05-characteristic-debate-v1-20260507.md` — Phase 3 provisional sub-group debate
- `wa-obslog-M05-love-compassion-kindness-v1-20260507.md` — Phase 4 control read, OQ register, and OQ resolutions (section: PHASE 4)
- `wa-cluster-M05-comprehensive-v5-20260507.md` — term identity and group data used in control read

This directive creates `cluster_subgroup` rows for each sub-group and BOUNDARY category, then assigns `mti_terms.cluster_subgroup_id` for all 87 terms in M05. It also sets the cluster status transition from `Data - In Progress` to `Analysis - In Progress`.

One term (H4263 mach.mal, mti_id=1264) is assigned to BOUNDARY here and is subject to a separate cluster reassignment directive (dir-003) — its BOUNDARY placement is provisional pending that reassignment.

---

## SCOPE

### Operation A — Create `cluster_subgroup` rows

Create the following 8 rows in `cluster_subgroup` (one per sub-group + BOUNDARY). If rows with the same `cluster_code` + `subgroup_code` already exist, UPDATE the label and description; do not duplicate.

| subgroup_code | label | description |
|---|---|---|
| M05-A | Love | Terms naming the inner orientation of directed attachment toward an object — person, God, community, or stranger. Spans covenantal steadfast love (che.sed, a.ha.vah), self-giving love (agapē, agapaō), natural affection and friendship (fileō, a.hev, filia, filos, re.eh), and the philo- compound family naming specific relational directions of the same orientation. Includes person-types constituted by love (cha.sid, a.hav) and the beloved-designation (ye.di.dut) as the relational object at love's most intimate register. |
| M05-B | Compassion | Terms naming the inward movement triggered by encountering suffering or need — visceral, directional toward the sufferer. Core families: the Hebrew RACHAM root (ra.cha.mim, ra.cha.min, ra.cham, ra.chum, ra.cha.ma.ni) naming womb-rooted compassion; the Greek splanchn- root (splanchnizō, eusplanchnos) naming bowel-rooted compassion; the sym-pathos group (sumpathēs, sumpatheō) naming fellow-feeling; and the sparing/pity register (chus, cha.mal, chem.lah). Also includes the Greek oiktir- family (oiktirmos, oiktirmōn, oikteirō) of compassionate mercy. |
| M05-C | Mercy | Terms naming the compassionate disposition of the greater toward the lesser — covenantally and judicially framed. The eleos/eleeō family: God's mercy as defining inner attribute (eleos), the act of mercy (eleeō), mercifulness as character quality (eleēmōn), and the structural opposites (aneleēmōn, anileōs — merciless). Includes eleeinos (pitiable) as the condition-term that defines the mercy characteristic's scope and calls it forth. |
| M05-D | Kindness and Goodness | Terms naming the inner quality of gracious generous goodwill — expressed as goodness toward others and as God's character that leads to repentance. The chrēstos/chrēstotēs/chrēsteuomai family (kindness as Spirit-produced inner quality) and the agathos compound family (goodness as inner moral orientation, activity, and person-type). Also includes haplotēs (singleness/generosity as undivided inner orientation) and pronoeō (purposive care as inner intention). |
| M05-E | Gentleness | Terms naming the inner disposition of yielding, non-coercive, non-retaliatory strength — operating in conflict, correction, and community as the mark of the renewed person. The praus/praotēs/prautēs family (Greek meekness/gentleness), the Hebrew an.vah/a.na.vah family (humility/gentleness), and epieikeia/epieikēs (gracious reasonable fairness). Also includes anochē (divine tolerance/forbearance — restrained from exacting what is deserved) and anexikakos (patient endurance of evil without resentment). |
| M05-F | Comfort and Encouragement | Terms naming the inner orientation directed specifically toward the distressed or faltering — bringing consolation, strengthening, calling alongside. Hebrew na.cham (to comfort/console, including divine relenting) and tan.chum (consolation as God's gift); Greek parakaleō (to comfort, exhort, plead) and paraklēsis (encouragement/comfort as inner experience); and la.vav (to captivate/encourage the heart). |
| M05-G | Fellowship and Participation | Terms naming the inner-relational bond of shared life — mutual belonging, common participation, generous sharing as expression of the participation bond. The koinōnia/koinōnos family (fellowship and the participant), katallagē (reconciliation as inner-relational restoration), homofrōn and isopsuchos (communal unity of inner orientation as the fellowship characteristic in its harmony expression), and epoikodomeō (building up the community as the participation characteristic in its formative expression). |
| M05-BOUNDARY | Boundary | Terms that qualify, contextualise, or express the cluster's characteristics without themselves being inner-being characteristics. Includes: assembly occasions (ekklēsia, miq.ra, a.tsa.rah); physical expressions of love (filēma/kiss, katafileō/to kiss, cheq/bosom); expressive and demonstrative acts (endeiknumi, eirēnopoieō, dōreō); freedom from disordered love (afilarguros); the lovely/fitting quality of objects that direct inner attention (na.eh, prosfilēs); and H4263 mach.mal (held in BOUNDARY pending cluster reassignment — see dir-003). |

### Operation B — Assign `mti_terms.cluster_subgroup_id`

For each term below, UPDATE `mti_terms` SET `cluster_subgroup_id` = (the id of the named subgroup_code) WHERE `strongs_number` = the given Strong's and `cluster_code` = 'M05'.

CC must resolve `cluster_subgroup_id` by looking up the newly created/confirmed `cluster_subgroup.id` for each `subgroup_code`. All terms below are currently `cluster_subgroup_id = NULL`.

#### M05-A — Love (23 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| H2617A | 536 | che.sed | kindness |
| G0025 | 571 | agapaō | to love |
| G0026 | 562 | agapē | love |
| H0160 | 537 | a.ha.vah | love |
| H0158 | 539 | a.hav | lover |
| G5368 | 572 | fileō | to love |
| H0157H | 1600 | a.hev | to love: friend |
| G5360 | 558 | filadelfia | brotherly love |
| G5387 | 554 | filostorgos | affectionate |
| G5362 | 561 | filandros | husband-loving |
| G5388 | 559 | filoteknos | child loving |
| G5363 | 556 | filanthrōpia | benevolence |
| G5381 | 1585 | filoxenia | hospitality |
| G5382 | 1582 | filoxenos | hospitable |
| G5391 | 1009 | filofrōn | friendly |
| G5358 | 566 | filagathos | lover of good |
| G5361 | 567 | filadelfos | loving the brothers |
| G5373 | 1588 | filia | friendship |
| H2623 | 540 | cha.sid | pious |
| H2616A | 1635 | cha.sad | be kind |
| G5384 | 1579 | filos | friendly/friend |
| H7463 | 1623 | re.eh | friend |
| H3033 | 535 | ye.di.dut | beloved |

#### M05-B — Compassion (15 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| H7356B | 544 | ra.cha.mim | compassion |
| H7359 | 988 | ra.cha.min | compassion |
| H7355 | 551 | ra.cham | to have compassion |
| H7349 | 1614 | ra.chum | compassionate |
| H7362 | 1616 | ra.cha.ma.ni | compassionate |
| G3628 | 992 | oiktirmos | compassion |
| G3629 | 3158 | oiktirmōn | compassionate |
| G3627 | 731 | oikteirō | to have compassion |
| G4697 | 730 | splanchnizō | to pity |
| G2155 | 593 | eusplanchnos | compassionate |
| G4835 | 3980 | sumpathēs | sympathetic |
| G4834 | 734 | sumpatheō | to sympathize |
| H2347 | 3182 | chus | to pity |
| H2550 | 487 | cha.mal | to spare |
| H2551 | 2192 | chem.lah | compassion |

#### M05-C — Mercy (6 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| G1656 | 983 | eleos | mercy |
| G1653 | 981 | eleeō | to have mercy |
| G1655 | 3164 | eleēmōn | merciful |
| G0415 | 3165 | aneleēmōn | merciless |
| G0448 | 993 | anileōs | merciless |
| G1652 | 3168 | eleeinos | pitiful |

#### M05-D — Kindness and Goodness (10 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| G5544 | 886 | chrēstotēs | kindness |
| G5543 | 954 | chrēstos | good/kind |
| G5541 | 5729 | chrēsteuomai | be kind |
| G0018 | 881 | agathos | good |
| G0015 | 1638 | agathopoieō | to do good |
| G0014 | 1640 | agathoergeō | to do good |
| G0016 | 1641 | agathopoiia | doing good |
| G0017 | 1642 | agathopoios | doing good |
| G0572 | 810 | haplotēs | openness |
| G4306 | 1187 | pronoeō | to care for |

#### M05-E — Gentleness (9 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| G4239 | 46 | praus | gentle |
| G4236 | 882 | praotēs | gentleness |
| G4240 | 47 | prautēs | gentleness |
| H6038 | 189 | a.na.vah | gentleness |
| H6037 | 188 | an.vah | gentleness |
| G1932 | 883 | epieikeia | gentleness |
| G1933 | 5425 | epieikēs | gentle |
| G0463 | 7502 | anochē | tolerance |
| G0420 | 856 | anexikakos | not resentful |

#### M05-F — Comfort and Encouragement (5 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| H5162G | 445 | na.cham | to be sorry: comfort |
| G3870 | 510 | parakaleō | to plead/comfort |
| G3874 | 1290 | paraklēsis | encouragement |
| H3823A | 587 | la.vav | to encourage |
| H8575 | 1292 | tan.chum | consolation |

#### M05-G — Fellowship and Participation (6 terms)

| Strong's | mti_id | Transliteration | Gloss |
|---|---|---|---|
| G2842 | 873 | koinōnia | participation |
| G2844 | 5367 | koinōnos | participant |
| G2643 | 1093 | katallagē | reconciliation |
| G3675 | 1008 | homofrōn | like-minded |
| G2473 | 1402 | isopsuchos | like-minded |
| G2026 | 7064 | epoikodomeō | to build up/upon |

#### M05-BOUNDARY — Boundary (13 terms)

| Strong's | mti_id | Transliteration | Gloss | Note |
|---|---|---|---|---|
| G1577 | 4833 | ekklēsia | assembly | |
| H4744 | 4827 | miq.ra | assembly | |
| H6116 | 6209 | a.tsa.rah | assembly | |
| G5370 | 1580 | filēma | kiss | |
| G2705 | 1581 | katafileō | to kiss | |
| H2436G | 575 | cheq | bosom: embrace | |
| H5000 | 547 | na.eh | lovely | |
| G4375 | 565 | prosfilēs | lovely | |
| G0866 | 569 | afilarguros | not greedy | |
| G1433 | 6845 | dōreō | to give | |
| G1731 | 1354 | endeiknumi | to show | |
| G1517 | 430 | eirēnopoieō | to make peace | |
| H4263 | 1264 | mach.mal | compassion | PROVISIONAL — cluster reassignment pending dir-003 |

### Operation C — Cluster status transition

UPDATE `cluster` SET `status` = 'Analysis - In Progress' WHERE `cluster_code` = 'M05'.

---

## OUTCOME REQUIRED

1. **8 `cluster_subgroup` rows** exist for M05 — one per sub-group code (M05-A through M05-G plus M05-BOUNDARY) — with the label and description as specified above.

2. **All 87 `mti_terms` rows** with `cluster_code = 'M05'` have `cluster_subgroup_id` populated (non-null), pointing to one of the 8 sub-group rows.

3. **Per-sub-group term counts match exactly:**

| subgroup_code | Expected term count |
|---|---:|
| M05-A | 23 |
| M05-B | 15 |
| M05-C | 6 |
| M05-D | 10 |
| M05-E | 9 |
| M05-F | 5 |
| M05-G | 6 |
| M05-BOUNDARY | 13 |
| **Total** | **87** |

4. **Cluster status** = `Analysis - In Progress` for cluster_code = 'M05'.

5. **No `wa_session_b_findings` rows written** — cluster-process directive does not touch that table.

6. **No `verse_context` rows modified** — sub-group assignment does not touch verse-level data.

---

## COMPLETION CONFIRMATION

CC returns the following after execution:

**Query 1 — sub-group term counts:**
```sql
SELECT cs.subgroup_code, cs.label, COUNT(mt.id) AS term_count
FROM cluster_subgroup cs
LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id = cs.id
WHERE cs.cluster_code = 'M05'
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
```
Expected: 8 rows matching the table above exactly.

**Query 2 — zero unassigned terms:**
```sql
SELECT COUNT(*) AS unassigned
FROM mti_terms
WHERE cluster_code = 'M05' AND cluster_subgroup_id IS NULL;
```
Expected: 0

**Query 3 — cluster status:**
```sql
SELECT cluster_code, status FROM cluster WHERE cluster_code = 'M05';
```
Expected: `M05 | Analysis - In Progress`

**Query 4 — sample rows (3 representative terms, one per sub-group family):**
```sql
SELECT mt.strongs_number, mt.transliteration, cs.subgroup_code
FROM mti_terms mt
JOIN cluster_subgroup cs ON cs.id = mt.cluster_subgroup_id
WHERE mt.cluster_code = 'M05'
AND mt.strongs_number IN ('G0026', 'H7356B', 'G1656', 'G5544', 'G4236', 'H5162G', 'G2842', 'G1577')
ORDER BY cs.subgroup_code;
```
Expected: agapē→M05-A, ra.cha.mim→M05-B, eleos→M05-C, chrēstotēs→M05-D, praotēs→M05-E, na.cham→M05-F, koinōnia→M05-G, ekklēsia→M05-BOUNDARY.

**Query 5 — wa_session_b_findings unchanged:**
```sql
SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id IN (
  SELECT DISTINCT registry_id FROM mti_terms WHERE cluster_code = 'M05'
);
```
Expected: same count as before this directive (no new rows written).

---

*wa-cluster-M05-dir-002-subgroup-assign-v1-20260507*
*Source obslog: wa-obslog-M05-love-compassion-kindness-v1-20260507 Phase 4*
*Source debate: WA-M05-characteristic-debate-v1-20260507*
*Companion: wa-cluster-M05-dir-003-term-rebind-v1-20260507 (mach.mal reassignment)*
