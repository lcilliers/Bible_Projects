# wa-cluster-M05-dir-005-B-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-B (Compassion)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-005 in the M05 cluster directive sequence
> Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-B-group-verse-mapping-v1-20260507.md

---

## DIRECTIVE ID

`DIR-20260507-M05-005`

---

## MOTIVATION

The M05-B sub-group (Compassion, 15 terms) has completed Phase 6 group-verse mapping. The mapping establishes: (1) Group 629 split into 629-a (genuine positive human compassion) and 629-b (disobedient compassion — sparing commanded-destruction targets); (2) 1 P-status verse assigned (Job 27:22); (3) anchor designations for all 18 groups; (4) 11 cross-group dual assignments.

---

## SCOPE

**Cluster:** M05 | **Sub-group:** M05-B — Compassion
**Terms (15):** mti_ids 544, 988, 551, 1614, 1616, 992, 3158, 731, 730, 593, 3980, 734, 3182, 487, 2192

**md_version values:**

| mti_id | Strong's | md_version |
|---|---|---|
| 487 | H2550 | 2 |
| 544 | H7356B | 1 |
| 551 | H7355 | 1 |
| 593 | G2155 | 1 |
| 730 | G4697 | 1 |
| 731 | G3627 | 1 |
| 734 | G4834 | 1 |
| 988 | H7359 | 1 |
| 992 | G3628 | 1 |
| 1614 | H7349 | 1 |
| 1616 | H7362 | 1 |
| 2192 | H2551 | 1 |
| 3158 | G3629 | 1 |
| 3182 | H2347 | 1 |
| 3980 | G4835 | 1 |

**Tables:** `verse_context_group` (INSERT 2 new rows for 629-a and 629-b; UPDATE descriptions on 1596, 1638, 1639, 333, 2717, 337, 338, 630); `verse_context` (UPSERT 1 P-verse; set anchors; INSERT 11 dual rows; distribute 629 verses to 629-a/629-b)

**Set-asides:** 4 SA rows (Job 6:10, Isa 30:14, Jer 50:14, Jer 51:3 — all H2550) are NOT re-evaluated.

---

## SCOPE — Detailed operations

### 1. Group split: Group 629 → 629-a and 629-b

**New group 629-a** (genuine human compassion):
- `group_code`: `487-001-a`; `mti_term_id`: 487
- `description`: Term names human compassion as the inner disposition of pity that moves toward and spares those in need — whether a child, a prisoner, or an enemy; genuine compassion as the inner motivation for sparing
- `anchor verse`: Exo 2:6 — `is_anchor=1`
- Verses to assign (from existing 629 pool): Exo 2:6, 1Sa 23:21, 2Sa 21:7, Mal 3:17, Job 27:22 (P-verse)
- Also: Deu 13:8 — compassion prohibition context (shared with 629-b as dual)

**New group 629-b** (disobedient compassion):
- `group_code`: `487-001-b`; `mti_term_id`: 487
- `description`: Term names compassion toward commanded-destruction targets as disobedience — where the inner disposition of pity violates the covenantal obligation to carry out judgment
- `anchor verse`: 1Sa 15:9 — `is_anchor=1`
- Verses to assign: 1Sa 15:3, 1Sa 15:9, 1Sa 15:15, 2Sa 12:4, 2Sa 12:6, Pro 6:34 (if assigned to 629), Hab 1:17

Note: Remaining 629 verses (Zec 11:5, 11:6, Eze 36:21, 2Ch 36:15, 2Ch 36:17 — divine compassion/withdrawal context) should be reviewed against Group 630 (divine compassion group); if already in 630, verify and leave unchanged.

### 2. P-status verse assignment

| vr_id | Reference | Term | Group |
|---|---|---|---|
| 59048 (confirm exact ID) | Job 27:22 | H2550 cha.mal | 629-a |

### 3. Anchor verse designations

| Group | Anchor reference | Term |
|---|---|---|
| 1596 | Isa 54:7 | H7356B ra.cha.mim |
| 1595 | Psa 103:13 | H7355 ra.cham |
| 1594 | Exo 34:6 | H7349 ra.chum |
| 1672 | Dan 2:18 | H7359 ra.cha.min |
| 349 | Lam 4:10 | H7362 ra.cha.ma.ni |
| 1638 | 2Cor 1:3 | G3628 oiktirmos |
| 1639 | Luk 6:36 | G3629 oiktirmōn |
| 331 | Rom 9:15 | G3627 oikteirō |
| 333 | Luk 15:20 | G4697 splanchnizō |
| 2717 | Eph 4:32 | G2155 eusplanchnos |
| 334 | Heb 4:15 | G4834 sumpatheō |
| 335 | 1Pe 3:8 | G4835 sumpathēs |
| 337 | Jon 4:11 | H2347 chus |
| 338 | Deu 13:8 | H2347 chus |
| 629-a | Exo 2:6 | H2550 cha.mal |
| 629-b | 1Sa 15:9 | H2550 cha.mal |
| 630 | 2Ch 36:15 | H2550 cha.mal |
| 339 | Isa 63:9 | H2551 chem.lah |

### 4. Cross-group dual assignments (11)

| Reference | Primary | Secondary | Reason |
|---|---|---|---|
| Deu 13:17 | 1595 | 1596 | H7355 + H7356B |
| 1Ki 8:50 | 1595 | 1596 | H7355 + H7356B |
| 2Ch 30:9 | 1594 | 1596 | H7349 + H7356B |
| Jer 13:14 | 629-b | 338 | H2550 + H2347 |
| Jer 21:7 | 630 | 338 | H2550 + H2347 |
| Deu 13:8 | 629-b | 338 | H2550 + H2347 (also 629-a dual via distinction) |
| Eze 5:11 | 630 | 338 | H2550 + H2347 |
| Eze 7:4 | 630 | 338 | H2550 + H2347 |
| Eze 8:18 | 630 | 338 | H2550 + H2347 |
| Eze 9:5 | 630 | 338 | H2550 + H2347 |
| 1Pe 3:8 | 335 | 2717 | G4835 + G2155 |

---

## OUTCOME REQUIRED

1. 2 new group rows (629-a, 629-b); original 629 retired; 14 + 1 P-verse distributed
2. 1 P-verse (Job 27:22) assigned to 629-a; vc_status updated
3. 18 groups each with exactly 1 anchor row
4. 11 secondary verse_context rows for dual assignments
5. 4 SA rows unchanged
6. wa_session_b_findings count unchanged

---

## COMPLETION CONFIRMATION

```sql
-- Verse counts and anchors per M05-B group
SELECT vcg.id, vcg.group_code, COUNT(vc.id) AS verse_count, SUM(vc.is_anchor) AS anchors
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
WHERE vcg.mti_term_id IN (544,988,551,1614,1616,992,3158,731,730,593,3980,734,3182,487,2192)
GROUP BY vcg.id ORDER BY vcg.id;

-- Anchor check (expect 0 rows)
SELECT vcg.id, SUM(vc.is_anchor) FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id
WHERE vcg.mti_term_id IN (544,988,551,1614,1616,992,3158,731,730,593,3980,734,3182,487,2192)
GROUP BY vcg.id HAVING SUM(vc.is_anchor) != 1;
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-B-group-mapping-applied-v1-20260507.md`

---

*wa-cluster-M05-dir-005-B-mapping-v1-20260507 | Researcher approval required before CC executes*

---
---

# wa-cluster-M05-dir-006-C-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-C (Mercy)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-006 | Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-C-through-G-group-verse-mapping-v1-20260507.md (M05-C section)

## DIRECTIVE ID

`DIR-20260507-M05-006`

## MOTIVATION

M05-C (Mercy, 6 terms, 60 verses) has completed Phase 6. No splits. 1 P-verse assigned (Mar 5:19 → Group 1629). Anchor designations for all 9 groups. 2 dual assignments.

## SCOPE

**Cluster:** M05 | **Sub-group:** M05-C | **Terms (6):** mti_ids 983, 981, 3164, 3165, 993, 3168

**md_version values:**

| mti_id | Strong's | md_version |
|---|---|---|
| 981 | G1653 | 2 |
| 983 | G1656 | 1 |
| 993 | G0448 | 1 |
| 3164 | G1655 | 1 |
| 3165 | G0415 | 1 |
| 3168 | G1652 | 1 |

### P-verse assignment

| vr_id | Reference | Term | Group |
|---|---|---|---|
| (confirm ID) | Mar 5:19 | G1653 eleeō | 1629 |

### Anchor designations

| Group | Anchor reference | Term |
|---|---|---|
| 1628 | Rom 9:16 | G1653 eleeō |
| 1629 | Mar 10:48 | G1653 eleeō |
| 1630 | Mat 18:33 | G1653 eleeō |
| 1631 | Heb 2:17 | G1655 eleēmōn |
| 1632 | Eph 2:4 | G1656 eleos |
| 1633 | Jam 2:13 | G1656 eleos |
| 1625 | Rom 1:31 | G0415 aneleēmōn |
| 1626 | Jam 2:13 | G0448 anileōs |
| 328 | Rev 3:17 | G1652 eleeinos |

### Dual assignments (2)

| Reference | Primary | Secondary |
|---|---|---|
| Mat 5:7 | 1629 | 1630 — G1653 eleeō + G1655 eleēmōn both present |
| Jam 2:13 | 1633 | 1626 — G1656 eleos + G0448 anileōs both present |

## OUTCOME REQUIRED

9 groups each with 1 anchor; 1 P-verse assigned; 2 dual secondary rows; SA count unchanged (0 SA for M05-C).

## COMPLETION CONFIRMATION

```sql
SELECT vcg.id, vcg.group_code, COUNT(vc.id), SUM(vc.is_anchor)
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id
WHERE vcg.mti_term_id IN (983,981,3164,3165,993,3168)
GROUP BY vcg.id;
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-C-group-mapping-applied-v1-20260507.md`

*Researcher approval required before CC executes*

---
---

# wa-cluster-M05-dir-007-D-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-D (Kindness and Goodness)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-007 | Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-C-through-G-group-verse-mapping-v1-20260507.md (M05-D section)

## DIRECTIVE ID

`DIR-20260507-M05-007`

## MOTIVATION

M05-D (Kindness and Goodness, 10 terms, 127 active verses) has completed Phase 6. No splits. No P-verses. 1 SA verse (Luk 5:39 — chrēstos in sensory sense, retained). Anchor designations for all 16 groups. 3 dual assignments.

## SCOPE

**Cluster:** M05 | **Sub-group:** M05-D | **Terms (10):** mti_ids 886, 954, 5729, 881, 1638, 1640, 1641, 1642, 810, 1187

**md_version values:**

| mti_id | Strong's | md_version |
|---|---|---|
| 810 | G0572 | 1 |
| 881 | G0018 | 1 |
| 886 | G5544 | 2 |
| 954 | G5543 | 2 |
| 1187 | G4306 | 1 |
| 1638 | G0015 | 1 |
| 1640 | G0014 | 1 |
| 1641 | G0016 | 1 |
| 1642 | G0017 | 1 |
| 5729 | G5541 | 1 |

### Anchor designations

| Group | Anchor reference | Term |
|---|---|---|
| 1111 | Rom 11:22 | G5544 chrēstotēs |
| 1112 | Gal 5:22 | G5544 chrēstotēs |
| 1469 | Luk 6:35 | G5543 chrēstos |
| 1467 | 1Cor 13:4 | G5541 chrēsteuomai |
| 1096 | Mar 10:18 | G0018 agathos |
| 1097 | Mat 12:35 | G0018 agathos |
| 1098 | Eph 2:10 | G0018 agathos |
| 1099 | Rom 8:28 | G0018 agathos |
| 1100 | Rom 7:19 | G0018 agathos |
| 1093 | 1Pe 2:20 | G0015 agathopoieō |
| 1092 | 1Ti 6:18 | G0014 agathoergeō |
| 1094 | 1Pe 4:19 | G0016 agathopoiia |
| 1095 | 1Pe 2:14 | G0017 agathopoios |
| 687 | 2Cor 11:3 | G0572 haplotēs |
| 688 | 2Cor 9:11 | G0572 haplotēs |
| 2290 | 2Cor 8:21 | G4306 pronoeō |

### Dual assignments (3)

| Reference | Primary | Secondary |
|---|---|---|
| Rom 2:4 | 1111 | 1469 — G5544 chrēstotēs + G5543 chrēstos |
| Rom 12:8 | 603 (M05-F) | 688 — G3870 + G0572; note this is a cross-sub-group dual; flag in report |
| 1Cor 13:4 | 1467 | 1543 (M05-A group) — G5541 + G0026; cross-sub-group dual; flag |

**Note on cross-sub-group duals:** Rom 12:8 and 1Cor 13:4 involve terms from different sub-groups (M05-D and M05-A/F). Record as dual assignments where both terms have verse_context rows for the same vr_id. No special treatment needed beyond the secondary row.

### Set-aside

1 SA row (Luk 5:39, G5543 chrēstos) — not re-evaluated.

## OUTCOME REQUIRED

16 groups each with 1 anchor; 0 P-verses; 3 dual secondary rows; 1 SA unchanged; wa_session_b_findings count unchanged.

## COMPLETION CONFIRMATION

```sql
SELECT vcg.id, vcg.group_code, COUNT(vc.id), SUM(vc.is_anchor)
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id
WHERE vcg.mti_term_id IN (886,954,5729,881,1638,1640,1641,1642,810,1187)
GROUP BY vcg.id;
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-D-group-mapping-applied-v1-20260507.md`

*Researcher approval required before CC executes*

---
---

# wa-cluster-M05-dir-008-E-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-E (Gentleness)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-008 | Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-C-through-G-group-verse-mapping-v1-20260507.md (M05-E section)

## DIRECTIVE ID

`DIR-20260507-M05-008`

## MOTIVATION

M05-E (Gentleness, 9 terms, 30 verses) has completed Phase 6. No splits. No P-verses. One special case: G0463 anochē (mti=7502, md_version=1) has no existing `verse_context_group` rows and requires a new group to be created. 8 existing groups confirmed with anchors. 2 dual assignments.

## SCOPE

**Cluster:** M05 | **Sub-group:** M05-E | **Terms (9):** mti_ids 46, 882, 47, 189, 188, 883, 5425, 7502, 856

**md_version values:**

| mti_id | Strong's | md_version |
|---|---|---|
| 46 | G4239 | 1 |
| 47 | G4240 | 1 |
| 188 | H6037 | 1 |
| 189 | H6038 | 1 |
| 856 | G0420 | 1 |
| 882 | G4236 | 1 |
| 883 | G1932 | 1 |
| 5425 | G1933 | 1 |
| 7502 | G0463 | 1 |

### Special case: New group required for G0463 anochē (mti=7502)

**CC pre-flight:** Query `verse_context` WHERE `mti_term_id = 7502` to confirm current rows and their `vc_status`. These rows need a group_id assigned.

**New group to create:**
- `group_code`: `7502-001`; `mti_term_id`: 7502
- `description`: Term names divine forbearance/tolerance — God's inner disposition of restraining judgment that would be fully warranted; the patience that withholds what is deserved, revealing the inner character of sovereign mercy toward the disobedient
- `anchor verse`: Rom 2:4 — `is_anchor=1` (note: Rom 2:4 also appears in M05-D Group 1111 for chrēstotēs; the anochē group's anchor is the same verse for a different term — confirm with CC that the verse_context row for mti=7502 at Rom 2:4 is the correct one)

**CC action:** Create the new group row; assign all anochē verse_context rows to it; set anchor.

If CC finds that anochē has 0 verse_context rows (no extractions), CC should halt on this item, report the gap, and proceed with the remaining 8 groups. Do not fabricate verse rows.

### Anchor designations (8 existing groups)

| Group | Anchor reference | Term |
|---|---|---|
| 1104 | 2Cor 10:1 | G4236 praotēs |
| 1261 | 1Pe 3:4 | G4239 praus |
| 1262 | Jam 1:21 | G4240 prautēs |
| 1102 | 2Cor 10:1 | G1932 epieikeia |
| 1103 | Phili 4:5 | G1933 epieikēs |
| 1272 | Pro 22:4 | H6038 a.na.vah |
| 1271 | 2Sa 22:36 | H6037 an.vah |
| 867 | 2Ti 2:24 | G0420 anexikakos |

**Note on Group 1102:** The anchor is 2Cor 10:1, same reference as Group 1104. This is valid — two different terms (G1932 epieikeia and G4236 praotēs) both present in the same verse. Confirm the correct term's verse_context row is set is_anchor=1 for each group.

### Dual assignments (2)

| Reference | Primary | Secondary |
|---|---|---|
| 2Cor 10:1 | 1104 (praotēs) | 1102 (epieikeia) — both terms present |
| Tit 3:2 | 1103 (epieikēs) | 1262 (prautēs) — both terms present |

## OUTCOME REQUIRED

9 groups (8 existing + 1 new for anochē) each with 1 anchor; 0 P-verses; 2 dual secondary rows; 0 SA; wa_session_b_findings count unchanged.

If anochē has 0 verse_context rows: 8 groups confirmed, anochē gap reported, directive partially applied and gap flagged for follow-up.

## COMPLETION CONFIRMATION

```sql
SELECT vcg.id, vcg.group_code, COUNT(vc.id), SUM(vc.is_anchor)
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id
WHERE vcg.mti_term_id IN (46,882,47,189,188,883,5425,7502,856)
GROUP BY vcg.id;

-- Anochē check
SELECT COUNT(*) FROM verse_context WHERE mti_term_id = 7502;
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-E-group-mapping-applied-v1-20260507.md`

*Researcher approval required before CC executes*

---
---

# wa-cluster-M05-dir-009-F-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-F (Comfort and Encouragement)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-009 | Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-C-through-G-group-verse-mapping-v1-20260507.md (M05-F section)

## DIRECTIVE ID

`DIR-20260507-M05-009`

## MOTIVATION

M05-F (Comfort and Encouragement, 5 terms, 206 verses) has completed Phase 6. One conglomerate-group split: Group 604 (G3870 parakaleō, 55 verses) split into 604-a (pastoral/apostolic appeal) and 604-b (social requests/urgings). Anchor designations for all 11 groups. 6 dual assignments.

## SCOPE

**Cluster:** M05 | **Sub-group:** M05-F | **Terms (5):** mti_ids 445, 510, 1290, 587, 1292

**md_version values:**

| mti_id | Strong's | md_version |
|---|---|---|
| 445 | H5162G | 1 |
| 510 | G3870 | 1 |
| 587 | H3823A | 1 |
| 1290 | G3874 | 1 |
| 1292 | H8575 | 1 |

### 1. Group split: Group 604 → 604-a and 604-b

**New group 604-a** (pastoral/apostolic appeal):
- `group_code`: `510-003-a`; `mti_term_id`: 510
- `description`: Term names the pastoral or apostolic appeal — the inner relational care and authority of the one urging another toward faithful conduct, endurance, and inner transformation; grounded in the mercies of God and the authority of the gospel
- `anchor verse`: Rom 12:1 — `is_anchor=1`
- Verses to assign (from 604 pool, pastoral/apostolic register): Act 11:23, Act 14:22, Act 15:32, Act 20:1, Act 20:2, Rom 12:1, Rom 12:8 (parakaleō), Rom 15:30, Rom 16:17, 1Cor 1:10, 1Cor 4:16, 1Cor 14:31, 1Cor 16:12, 1Cor 16:15, 2Cor 2:8, 2Cor 5:20, 2Cor 6:1, 2Cor 8:6, 2Cor 9:5, 2Cor 10:1, 2Cor 12:18, 2Cor 13:11, Eph 4:1, Eph 6:22, Phili 4:2, Col 2:2, Col 4:8, 1Th 2:12, 1Th 3:2, 1Th 4:1, 1Th 4:10, 1Th 4:18, 1Th 5:11, 1Th 5:14, 2Th 2:17, 2Th 3:12, 1Ti 1:3, 1Ti 2:1, 1Ti 5:1, 1Ti 6:2, 2Ti 4:2, Tit 1:9, Tit 2:6, Tit 2:15, Phile 9, Phile 10, Heb 3:13, Heb 10:25, Heb 13:19, Heb 13:22 (parakaleō), 1Pe 2:11, 1Pe 5:1, 1Pe 5:12, Jude 3
- (Luk 3:18 and Act 2:40 — exhortation in preaching context — also 604-a)

**New group 604-b** (social requests/urgings):
- `group_code`: `510-003-b`; `mti_term_id`: 510
- `description`: Term names the social or interpersonal request — inviting, urging, asking someone to do or refrain from something in the context of ordinary social or relational life, without the pastoral or apostolic authority dimension
- `anchor verse`: Act 16:15 — `is_anchor=1`
- Verses to assign: Act 8:31, Act 9:38, Act 16:15, Act 16:39, Act 16:40, Act 19:31, Act 21:12, Act 24:4, Act 25:2, Act 27:33, Act 27:34, Act 28:14, Act 28:20, Luk 15:28 (father entreating son), 2Cor 12:8 (Paul pleading with Lord — note this is also in Group 602 as affliction comfort; may be dual)

**CC guidance:** If uncertain about a specific verse's register (pastoral vs social), default to 604-a and flag in the application report.

### 2. Anchor designations (all 11 groups)

| Group | Anchor reference | Term |
|---|---|---|
| 1741 | Isa 40:1 | H5162G na.cham |
| 1742 | Isa 66:13 | H5162G na.cham |
| 2741 | Song 4:9 | H3823A la.vav |
| 3079 | Psa 94:19 | H8575 tan.chum |
| 602 | 2Cor 1:4 | G3870 parakaleō |
| 603 | Mar 5:23 | G3870 parakaleō |
| 604-a | Rom 12:1 | G3870 parakaleō |
| 604-b | Act 16:15 | G3870 parakaleō |
| 3073 | 2Cor 1:3 | G3874 paraklēsis |
| 3074 | Rom 15:4 | G3874 paraklēsis |
| 3075 | Phile 7 | G3874 paraklēsis |

### 3. Dual assignments (6)

| Reference | Primary | Secondary |
|---|---|---|
| 2Cor 1:3 | 602 (parakaleō comfort) | 3073 (paraklēsis comfort) — both terms |
| 2Cor 1:4 | 602 | 3073 — both terms |
| 2Cor 1:5 | 602 | 3073 — both terms |
| 2Cor 1:6 | 602 | 3073 — both terms |
| 2Cor 1:7 | 602 | 3073 — both terms |
| Rom 12:8 | 604-a | 688 (M05-D haplotēs) — G3870 + G0572 cross-sub-group dual |

## OUTCOME REQUIRED

11 groups (10 original + 1 from 604 split) each with 1 anchor; 0 P-verses; 6 dual secondary rows; 0 SA; wa_session_b_findings count unchanged.

## COMPLETION CONFIRMATION

```sql
SELECT vcg.id, vcg.group_code, COUNT(vc.id), SUM(vc.is_anchor)
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id
WHERE vcg.mti_term_id IN (445,510,1290,587,1292)
GROUP BY vcg.id;
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-F-group-mapping-applied-v1-20260507.md`

*Researcher approval required before CC executes*

---
---

# wa-cluster-M05-dir-010-G-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-G (Fellowship and Participation)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-010 | Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-C-through-G-group-verse-mapping-v1-20260507.md (M05-G section)

## DIRECTIVE ID

`DIR-20260507-M05-010`

## MOTIVATION

M05-G (Fellowship and Participation, 6 terms, 40 active verses) has completed Phase 6. No splits. 9 P-status verses assigned. Anchor designations for all 8 groups. 6 dual assignments.

## SCOPE

**Cluster:** M05 | **Sub-group:** M05-G | **Terms (6):** mti_ids 873, 5367, 1093, 1008, 1402, 7064

**md_version values:**

| mti_id | Strong's | md_version |
|---|---|---|
| 873 | G2842 | 2 |
| 1008 | G3675 | 1 |
| 1093 | G2643 | 1 |
| 1402 | G2473 | 1 |
| 5367 | G2844 | 2 |
| 7064 | G2026 | 2 |

### 1. P-verse assignments (9 verses)

| vr_id | Reference | Term | Group |
|---|---|---|---|
| (confirm) | Luk 5:10 | G2844 koinōnos | 1057 |
| (confirm) | 2Cor 8:23 | G2844 koinōnos | 1057 |
| (confirm) | Rom 15:26 | G2842 koinōnia | 1056 |
| (confirm) | 2Cor 9:13 | G2842 koinōnia | 1056 |
| (confirm) | Heb 13:16 | G2842 koinōnia | 1056 |
| (confirm) | 1Cor 3:10 | G2026 epoikodomeō | 2849 |
| (confirm) | 1Cor 3:12 | G2026 epoikodomeō | 2849 |
| (confirm) | 1Cor 3:14 | G2026 epoikodomeō | 2849 |
| (confirm) | Eph 2:20 | G2026 epoikodomeō | 2849 |

**CC pre-flight:** Confirm vr_ids from `verse_ref` table for each reference above before assigning.

### 2. Anchor designations

| Group | Anchor reference | Term |
|---|---|---|
| 1055 | 1Jo 1:3 | G2842 koinōnia |
| 1056 | Act 2:42 | G2842 koinōnia |
| 1057 | 2Pe 1:4 | G2844 koinōnos |
| 1058 | Mat 23:30 | G2844 koinōnos |
| 1813 | 1Pe 3:8 | G3675 homofrōn |
| 1795 | Phili 2:20 | G2473 isopsuchos |
| 2069 | 2Cor 5:19 | G2643 katallagē |
| 2849 | Eph 2:20 | G2026 epoikodomeō |

### 3. Dual assignments (6)

| Reference | Primary | Secondary |
|---|---|---|
| Act 2:42 | 1056 (horizontal koinōnia) | 1055 (vertical koinōnia) — same term, two phenomena |
| Phili 2:1 | 1055 | 3073 (M05-F paraklēsis) — G2842 + G3874 cross-sub-group |
| 1Jo 1:3 | 1055 | 1056 — vertical and horizontal fellowship simultaneous |
| 1Jo 1:6 | 1055 | 1056 |
| 1Jo 1:7 | 1055 | 1056 |
| 2Cor 1:7 | 1057 | 3073 (M05-F) — G2844 koinōnos + G3874 paraklēsis |

**Note on Act 2:42 dual:** The same verse_context row for G2842 koinōnia at Act 2:42 is the anchor for group 1056. The secondary assignment is to group 1055 (vertical fellowship). CC should confirm whether a single verse_context row can be anchor of one group and secondary member of another, or whether a secondary row is needed.

## OUTCOME REQUIRED

8 groups each with 1 anchor; 9 P-verse rows updated (vc_status → assigned, group_id set); 6 dual secondary rows; 0 SA; wa_session_b_findings count unchanged.

## COMPLETION CONFIRMATION

```sql
SELECT vcg.id, vcg.group_code, COUNT(vc.id), SUM(vc.is_anchor)
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id
WHERE vcg.mti_term_id IN (873,5367,1093,1008,1402,7064)
GROUP BY vcg.id;

-- P-verse count check (expect 0 P-status remaining)
SELECT COUNT(*) FROM verse_context
WHERE mti_term_id IN (873,5367,1093,1008,1402,7064)
AND vc_status = 'P';
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-G-group-mapping-applied-v1-20260507.md`

*Researcher approval required before CC executes*
