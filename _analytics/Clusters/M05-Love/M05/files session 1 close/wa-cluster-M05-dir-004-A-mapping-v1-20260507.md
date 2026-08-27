# wa-cluster-M05-dir-004-A-mapping-v1-20260507

> Cluster-process directive — Group-verse mapping apply for M05-A (Love)
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4 (Worked pattern A)
> Sequence: dir-004 in the M05 cluster directive sequence
> Produced by: Claude AI — Session B Phase 7 | 20260507
> Source mapping: WA-M05-A-group-verse-mapping-v1-20260507.md
> Obslog reference: wa-obslog-M05-love-compassion-kindness-v1-20260507 Phase 6/7

---

## DIRECTIVE ID

`DIR-20260507-M05-004`

---

## MOTIVATION

The M05-A sub-group (Love, 23 terms) has been analytically reviewed through Phase 5 (first reading pass) and Phase 6 (group-verse mapping) of Session B. The mapping document `WA-M05-A-group-verse-mapping-v1-20260507.md` establishes:

1. **One conglomerate-group split:** Group 1583 (H2617A che.sed, 115 verses, "God's steadfast love") is analytically distinct across two phenomena and must be split into:
   - **1583-a** — God's chesed as his eternal declared attribute (Exo 34:6, Lam 3:22 type)
   - **1583-b** — God's chesed enacted in specific historical acts (Exo 15:13, Gen 19:19 type)
2. **22 P-status verses assigned** to existing groups (see §SCOPE).
3. **Anchor verse designations** for all 37 groups (36 original + 1 new from split).
4. **6 cross-group dual assignments** identified.
5. **Group description refinements** for groups 1559, 1572, 1576, 1584, 1585, 1562, 1598.

The mapping must land in the database to enable Phase 8 (catalogue-prompt findings) to proceed.

---

## SCOPE

**Cluster:** `M05` — Love, Compassion and Kindness
**Sub-group:** `M05-A` — Love
**Terms (23):** mti_ids 536, 571, 562, 537, 539, 572, 1600, 558, 554, 561, 559, 556, 1585, 1582, 1009, 566, 567, 1588, 540, 1635, 1579, 1623, 535

**md_version values (from v6 report patch-authoring refs — use as input_versions):**

| mti_id | Strong's | md_version |
|---|---|---|
| 535 | H3033 | 1 |
| 536 | H2617A | 3 |
| 537 | H0160 | 1 |
| 539 | H0158 | 1 |
| 540 | H2623 | 1 |
| 554 | G5387 | 1 |
| 556 | G5363 | 2 |
| 558 | G5360 | 1 |
| 559 | G5388 | 1 |
| 561 | G5362 | 1 |
| 562 | G0026 | 1 |
| 566 | G5358 | 1 |
| 567 | G5361 | 1 |
| 571 | G0025 | 1 |
| 572 | G5368 | 1 |
| 1009 | G5391 | 1 |
| 1579 | G5384 | 2 |
| 1582 | G5382 | 1 |
| 1585 | G5381 | 1 |
| 1588 | G5373 | 1 |
| 1600 | H0157H | 2 |
| 1623 | H7463 | 2 |
| 1635 | H2616A | 1 |

**Tables touched:**
- `verse_context_group` — INSERT new group rows (1583-a, 1583-b); UPDATE descriptions on groups 1559, 1562, 1572, 1576, 1584, 1585, 1598; description refinements noted on 1540, 1583 (parent — may be retired or renamed)
- `verse_context` — UPSERT `group_id` on 22 P-status verse rows; set `is_anchor=1` on anchor verses; clear stale anchors first (any existing `is_anchor=1` rows for M05-A groups); INSERT secondary membership rows for 6 dual assignments; distribute 1583's 115 existing verse rows between 1583-a and 1583-b

**Set-asides:** 3 SA rows (vr_ids for 2Ch 32:32, 2Ch 35:26, Isa 40:6 — all H2617A) are NOT re-evaluated. Do not touch.

---

## SCOPE — Detailed operations

### 1. Group split: Group 1583 → 1583-a and 1583-b

**Action:** Create two new `verse_context_group` rows. Retain group 1583 as deprecated/renamed or soft-delete it after migration.

**New group 1583-a** (to be created):
- `group_code`: `536-001-a` (or per CC convention for split groups)
- `mti_term_id`: 536
- `description`: God's chesed as his eternal declared attribute — the covenantal faithfulness that never ceases, is proclaimed in the divine self-disclosure formula (Exo 34:6), and is the ground of Israel's hope and petition even in desolation (Lam 3:22)
- `anchor verse`: Lam 3:22 — `is_anchor=1`

**New group 1583-b** (to be created):
- `group_code`: `536-001-b`
- `mti_term_id`: 536
- `description`: God's chesed enacted in specific historical acts toward individuals and toward Israel — the covenantal faithfulness made concrete in protection, provision, deliverance, and sustained presence (Exo 15:13, Gen 19:19 type)
- `anchor verse`: Exo 15:13 — `is_anchor=1`

**Verse distribution between 1583-a and 1583-b:** CC should read each of the 115 verse rows currently assigned to group 1583 and route them:
- Verses carrying God's chesed as declared attribute / liturgical refrain / petition ground → 1583-a. Diagnostic: verses where chesed is named as God's character quality without reference to a specific act (e.g. Exo 34:6, Deu 7:9, Psa 36:5, Psa 63:3, Psa 103:8, Psa 107:1, Psa 136 series, Lam 3:22-23)
- Verses carrying God's chesed enacted in a specific historical act toward a named person or Israel → 1583-b. Diagnostic: verses with a named beneficiary and a specific moment of chesed enacted (e.g. Gen 19:19 Lot, Gen 24:12 Abraham's servant, Gen 39:21 Joseph, Exo 15:13 Exodus, 2Sa 7:15 David)
- If in doubt for a specific verse, assign to 1583-b (enacted) as the more concrete group; flag in the application report.

### 2. P-status verse assignments (22 verses → existing groups)

| vr_id | Reference | Term | Assign to group |
|---|---|---|---|
| 68172 | 1Ki 4:5 | H7463 re.eh | 1598 |
| 3940 | Neh 13:14 | H2617A che.sed | 1584 |
| 3942 | Est 2:9 | H2617A che.sed | 1584 |
| 3943 | Est 2:17 | H2617A che.sed | 1584 |
| 67683 | Est 5:10 | H0157H a.hev | 1576 |
| 67684 | Est 5:14 | H0157H a.hev | 1576 |
| 67685 | Est 6:13 | H0157H a.hev | 1576 |
| 67690 | Pro 14:20 | H0157H a.hev | 1576 |
| 67687 | Jer 20:4 | H0157H a.hev | 1576 |
| 67688 | Jer 20:6 | H0157H a.hev | 1576 |
| 66970 | Luk 7:6 | G5384 filos | 1572 |
| 66961 | Luk 14:10 | G5384 filos | 1572 |
| 66962 | Luk 14:12 | G5384 filos | 1572 |
| 66963 | Luk 15:29 | G5384 filos | 1572 |
| 66967 | Luk 21:16 | G5384 filos | 1572 |
| 66968 | Luk 23:12 | G5384 filos | 1572 |
| 66955 | Joh 19:12 | G5384 filos | 1572 |
| 66946 | Act 10:24 | G5384 filos | 1572 |
| 66947 | Act 19:31 | G5384 filos | 1572 |
| 66948 | Act 27:3 | G5384 filos | 1572 |
| 4614 | Act 28:2 | G5363 filanthrōpia | 1559 |
| 66945 | 3Jo 15 | G5384 filos | 1572 |

### 3. Anchor verse designations (one per group)

For each group listed below, set `is_anchor=1` on the named verse row. Clear any existing stale `is_anchor=1` rows for M05-A groups first.

| Group | Anchor verse reference | Term |
|---|---|---|
| 1537 | Mat 22:37 | G0025 agapaō |
| 1538 | Joh 13:1 | G0025 agapaō |
| 1539 | Mat 5:44 | G0025 agapaō |
| 1540 | Joh 13:34 | G0025 agapaō |
| 1541 | Joh 3:19 | G0025 agapaō |
| 1542 | 1Jo 4:8 | G0026 agapē |
| 1543 | 1Cor 13:4 | G0026 agapē |
| 1544 | 2Cor 5:14 | G0026 agapē |
| 1555 | Tit 1:8 | G5358 filagathos |
| 1556 | Heb 13:1 | G5360 filadelfia |
| 1557 | 1Pe 3:8 | G5361 filadelfos |
| 1558 | Tit 2:4 | G5362 filandros |
| 1559 | Tit 3:4 | G5363 filanthrōpia |
| 1562 | Joh 11:36 | G5368 fileō |
| 1563 | Mat 10:37 | G5368 fileō |
| 1564 | Joh 21:17 | G5368 fileō |
| 1567 | Jam 4:4 | G5373 filia |
| 157 | Tit 1:8 | G5382 filoxenos |
| 158 | 1Pe 4:9 | G5382 filoxenos |
| 159 | Heb 13:2 | G5381 filoxenia |
| 1572 | Joh 15:15 | G5384 filos |
| 1573 | Rom 12:10 | G5387 filostorgos |
| 1574 | Tit 2:4 | G5388 filoteknos |
| 1576 | Pro 18:24 | H0157H a.hev |
| 1577 | Pro 5:19 | H0158 a.hav |
| 1578 | Jer 31:3 | H0160 a.ha.vah |
| 1579 | 2Sa 1:26 | H0160 a.ha.vah |
| 1580 | Pro 10:12 | H0160 a.ha.vah |
| 1583-a | Lam 3:22 | H2617A che.sed |
| 1583-b | Exo 15:13 | H2617A che.sed |
| 1584 | Rut 3:10 | H2617A che.sed |
| 1585 | Hos 6:6 | H2617A che.sed |
| 1586 | Psa 4:3 | H2623 cha.sid |
| 1588 | Jer 12:7 | H3033 ye.di.dut |
| 1598 | 2Sa 16:16 | H7463 re.eh |
| 1823 | 1Pe 3:8 | G5391 filofrōn |
| 343 | 2Sa 22:26 | H2616A cha.sad |

### 4. Cross-group dual assignments (6 verse rows with secondary group membership)

Insert secondary `verse_context` row for each dual assignment (same vr_id, different group_id):

| Reference | Term | Primary group | Secondary group |
|---|---|---|---|
| Rom 12:10 | G5360 filadelfia + G5387 filostorgos | 1556 | 1573 |
| Tit 2:4 | G5362 filandros + G5388 filoteknos | 1558 | 1574 |
| Tit 1:8 | G5382 filoxenos + G5358 filagathos | 157 | 1555 |
| 1Pe 3:8 | G5391 filofrōn + G5361 filadelfos | 1823 | 1557 |
| Joh 15:9 | G0025 + G0026 (love toward/from) | 1538 | 1542 |
| Joh 17:26 | G0025 + G0026 | 1538 | 1542 |

### 5. Description updates (existing groups)

Update `description` field in `verse_context_group` for:
- Group 1559: refined to include Act 28:2 human filanthrōpia alongside Tit 3:4 divine
- Group 1562: refined to note Judas-kiss instances as friendship bond weaponised
- Group 1572: refined to include the everyday social friendship register
- Group 1576: refined to include the morally inverted register (Est 5:14, Jer 20:6)
- Group 1584: refined description as per mapping document
- Group 1585: refined as failure/withdrawal of chesed

---

## OUTCOME REQUIRED

Post-application state:

1. **Group split confirmed:** 2 new `verse_context_group` rows (1583-a and 1583-b) exist; original 1583 retired or cleared; 115 verses distributed between the two new groups; each has exactly one `is_anchor=1` row.
2. **P-verse assignments:** 22 verse rows have `vc_status` updated from `P` to `G` (or equivalent assigned state) and `group_id` set per the table above.
3. **Anchor designations:** Every M05-A group (37 total) has exactly one `is_anchor=1` row; no M05-A group has 0 or >1 anchor rows.
4. **Dual assignments:** 6 secondary `verse_context` rows present; each has the same `vr_id` as a primary row but a different `group_id`.
5. **SA rows unchanged:** 3 set-aside rows (2Ch 32:32, 2Ch 35:26, Isa 40:6) remain untouched.
6. **wa_session_b_findings row count:** Unchanged (cluster-process directive does not write to this table).

---

## COMPLETION CONFIRMATION

CC returns:

1. Verse counts per group for M05-A terms:
   ```sql
   SELECT vcg.id, vcg.group_code, COUNT(vc.id) AS verse_count, SUM(vc.is_anchor) AS anchors
   FROM verse_context_group vcg
   JOIN verse_context vc ON vc.group_id = vcg.id
   WHERE vcg.mti_term_id IN (536,571,562,537,539,572,1600,558,554,561,559,556,1585,1582,1009,566,567,1588,540,1635,1579,1623,535)
   GROUP BY vcg.id ORDER BY vcg.id;
   ```

2. Anchor count check — confirm each group has exactly 1 anchor:
   ```sql
   SELECT vcg.id, SUM(vc.is_anchor) AS anchor_count
   FROM verse_context_group vcg
   JOIN verse_context vc ON vc.group_id = vcg.id
   WHERE vcg.mti_term_id IN (536,571,562,537,539,572,1600,558,554,561,559,556,1585,1582,1009,566,567,1588,540,1635,1579,1623,535)
   GROUP BY vcg.id
   HAVING anchor_count != 1;
   -- Expected: 0 rows
   ```

3. Dual-assignment count:
   ```sql
   SELECT COUNT(*) FROM verse_context vc
   WHERE vc.group_id IN (SELECT id FROM verse_context_group WHERE mti_term_id IN (536,571,562,537,539,572,1600,558,554,561,559,556,1585,1582,1009,566,567,1588,540,1635,1579,1623,535))
   AND vc.vr_id IN (SELECT vr_id FROM verse_context GROUP BY vr_id HAVING COUNT(*) > 1);
   -- Expected: ≥6 rows (the 6 dual pairs)
   ```

4. SA row check:
   ```sql
   SELECT vr_id, set_aside_reason FROM verse_context
   WHERE vr_id IN (SELECT vr_id FROM verse_ref WHERE reference IN ('2Ch 32:32','2Ch 35:26','Isa 40:6'))
   AND mti_term_id = 536;
   -- Expected: 3 rows with set_aside_reason populated, is_relevant=0 unchanged
   ```

5. wa_session_b_findings count unchanged (query before and after, confirm same count).

6. Application report saved to `Sessions/Session_Clusters/M05/WA-M05-A-group-mapping-applied-v1-20260507.md`.

---

*wa-cluster-M05-dir-004-A-mapping-v1-20260507 | Cluster-process directive per wa-directive-instruction-v1_4-20260506 §11.4 | Researcher approval required before CC executes*
