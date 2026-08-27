# Directive DIR-20260515-002 — M01 Phase 4 sub-group assignment

> Produced by: wa-directive-instruction-v1_4-20260506
> Governed by: wa-global-rules-all-v2-20260427
> Scope: cluster M01 (wa-cluster-M01-dir-001-subgroup-assign)
> Produced date: 2026-05-15

---

## DIRECTIVE ID

`DIR-20260515-002`

---

## MOTIVATION

Following Phase 3 characteristic debate and the execution of DIR-20260515-001 (cross-cluster term transfer), cluster M01 now contains 82 terms across 1,029 active verses. No sub-groups exist yet (H6=82 — all 82 terms unassigned). Phase 4 requires CC to create 8 named sub-groups plus one BOUNDARY sub-group in `cluster_subgroup`, assign all 82 terms to their primary sub-group, and transition the cluster status to `Analysis - In Progress`.

The sub-group structure was determined by systematic T1 testing across all 82 terms in the Phase 3 characteristic debate (wa-obslog-M01-cluster-m01-v1-20260515.md). The assignment is analytically grounded; CC executes without modification.

Important: several terms carry VCG content spanning more than one sub-group (e.g., H3372G ya.re has groups for both "fear not" commands and reverential fear and threatening fear). The **primary sub-group** assignment in this directive governs `mti_terms.cluster_subgroup_id` and the `mti_term_subgroup` link. Verse-level routing to secondary sub-groups is Phase 6 VCG mapping work — do not attempt verse-level sub-group routing in this directive.

Source: `wa-cluster-M01-comprehensive-v4-20260515.md` — confirms 82 terms, H6=82, all unassigned.

---

## SCOPE

**Tables:**
- `cluster_subgroup` — INSERT 9 new rows (8 named sub-groups + 1 BOUNDARY)
- `mti_term_subgroup` (or equivalent term-to-subgroup linking table) — INSERT 82 rows, one per term
- `mti_terms.cluster_subgroup_id` — UPDATE 82 rows to the newly created sub-group IDs
- `cluster` — UPDATE `status` field for M01 from `Data - In Progress` → `Analysis - In Progress`

**Cluster:** `M01`

**Pre-condition:** CC must verify `SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' AND status IN ('extracted','extracted_thin')` returns 82 before proceeding.

---

## OUTCOME REQUIRED

### 1. Sub-groups to create in `cluster_subgroup`

CC resolves the correct column names from the schema. Each row requires at minimum: `cluster_code`, `subgroup_code`, `subgroup_label`, `description`, and any required FK or ordering fields. CC uses schema v3.17.0 to determine exact column set.

| subgroup_code | subgroup_label | description |
|---|---|---|
| M01-A | Reverential Fear / Fear of God | The fear of the Lord as the proper inner orientation — reverential awe before divine majesty, the beginning of wisdom, the ground of covenant obedience and worship. God is the object; wisdom, holiness, and faithful conduct are the outcomes. |
| M01-B | Threatening / Creaturely Fear | The alarm-response to perceived danger — fear of enemies, threatening powers, circumstances, and death. Includes the divine 'do not fear' reassurance commands, whose meaning requires the threatening fear to be identified. |
| M01-C | Terror and Dread | Overwhelming, acute terror — externally imposed, comprehensive, often divinely sent. The inner being not merely afraid but engulfed, overwhelmed, and shattered. The most intense end of the fear spectrum. |
| M01-D | Dismay and Alarm | The destabilising, paralysing form of fear — the inner collapse of composure under threat; the overwhelmed and immobilised inner person, unable to act. |
| M01-E | Trembling and Shuddering | The somatic-inner expression of fear, dread, and awe — trembling and shuddering as the felt inner-bodily manifestation across the full fear spectrum. Names what fear looks like as it moves through the body-inner interface. |
| M01-F | Anxiety | Chronic, anticipatory inner-being agitation — accumulated apprehensive thoughts, worried restlessness, the inner person dwelling on feared possibilities. Temporal structure is forward-looking and sustained, not immediate-response. |
| M01-G | Awe and Wonder | Overwhelmed astonishment before the extraordinary — the wonder-fear response to divine action, miraculous presence, or the unexpected. Astonishment is the primary element; fear is secondary and derivative. |
| M01-H | Timidity and Cowardice | The dispositional form of fear — the settled inner orientation of fearfulness that impairs faith and action. Cowardice as a moral inner condition: the person characterised by chronic fearfulness rather than trust. |
| M01-BOUNDARY | Boundary | Terms held in BOUNDARY pending programme-level cluster reassignment decision. Current content: perplexity/bewilderment terms (cognitive disorientation — being at a loss before the inexplicable). Distinct from fear; no current cluster home. |

### 2. Term-to-sub-group assignments

Assign each term to its **primary** sub-group. CC resolves mti_id from the patch-authoring reference table in the v4 report; Strong's number is provided as a cross-check.

**M01-A — Reverential Fear / Fear of God (19 terms)**

| Strong's | mti_id | Notes |
|---|---|---|
| H3374 yir.ah | 269 | definitive fear-of-God noun |
| H3372G ya.re | 298 | primary A; VCG-003 content verse-routed to B in Phase 6 |
| H3372H ya.re | 1682 | to fear: revere |
| H3373 ya.re | 1681 | God-fearing person |
| G5401 fobos | 266 | primary A; VCG-003 verse-routed to B |
| G5399 fobeō | 292 | primary A; VCG-003 verse-routed to B |
| H6342 pa.chad | 291 | primary A (VCG-002); VCG-001 verse-routed to B |
| H6343 pa.chad | 829 | primary A (VCG-001 Fear of Isaac); VCGs-002,003,004 verse-routed to B/C |
| H6345 pach.dah | 263 | reverential fear of God owed but absent |
| H1481C gur | 290 | primary A (VCG-001); VCG-002 verse-routed to B |
| H4172A mo.rah | 270 | primary A (VCG-002); VCG-001 verse-routed to C |
| H4172B mo.ra | 271 | primary A (VCG-002); VCG-001 verse-routed to C |
| H4035 me.gu.rah | 272 | fears as divine-judgment instrument — fear-of-God register |
| G6015 deos | 704 | reverent awe for worship |
| H2730 cha.red | 310 | primary A (VCG-001: trembling at word of God) |
| H6206 a.rats | 306 | primary A (VCG-002: holy reverence); VCG-001 verse-routed to B |
| H2865 cha.tat | 703 | primary D; VCG-003 (reverential awe) verse-routed to A in Phase 6 |
| G5156 tromos | 308 | primary E; VCG-002 (trembling reverential service) verse-routed to A |
| H7578 re.tet | 1713 | trembling of reverential awe/deference |

**M01-B — Threatening / Creaturely Fear (7 unique primary-B terms; others primary-A with B secondary)**

| Strong's | mti_id | Notes |
|---|---|---|
| G1719 emfobos | 257 | afraid before divine/threatening presence |
| H3025 ya.gor | 296 | fearful dread before what may befall |
| H3016 ya.gor | 276 | inner condition of fear before powerful enemy |
| H4032 ma.gor | 286 | comprehensive inner terror of being surrounded |
| H4034 me.go.rah | 273 | inner fears that oppress the person |
| H7297 ra.hah | 297 | fear commanded against in divine reassurance |
| G4423 ptoēsis | 267 | inner condition of fear before what is frightening |
| G4422 ptoeō | 1690 | inner fear-response to alarming events |
| G4426 pturomai | 1692 | inner intimidation by hostile opposition |
| G5398 foberos | 274 | divine judgment/presence as terror-inducing quality |
| G1630 ekfobos | 283 | overwhelming inner terror before divine presence |
| H1763 de.chal | 294 | commanded reverence / inner terror before visions/powers |
| H2119B za.chal | 1734 | dread-filled trembling before God/power |

**M01-C — Terror and Dread (17 terms)**

| Strong's | mti_id |
|---|---|
| H0367 e.mah | 284 |
| H1091 bal.la.hah | 1156 |
| H1205 be.a.tah | 1154 |
| H4288 me.chit.tah | 1152 |
| H2851 chit.tit | 1151 |
| H2847 chit.tah | 1155 |
| H2844A chat | 1723 |
| H2849 chat.chat | 1729 |
| H2866 cha.tat | 1730 |
| H8606 tiph.le.tset | 1720 |
| H4637 ma.a.ra.tsah | 1776 |
| H6178 a.ruts | 1777 |
| H0366 a.yom | 1722 |
| H2283 chag.ga | 1157 |
| H2189 za.a.vah | 1162 |
| H8047G sham.mah | 1161 |
| H4712 me.tsar | 162 |

**M01-D — Dismay and Alarm (5 terms)**

| Strong's | mti_id |
|---|---|
| H0926 ba.hal | 92 |
| H0927 be.hal | 5187 |
| H2865 cha.tat | 703 |
| H8541 tim.ma.hon | 1732 |
| H3735 ke.ra | 152 |

**M01-E — Trembling and Shuddering (19 terms)**

| Strong's | mti_id |
|---|---|
| H2729 cha.rad | 305 |
| H2731 cha.ra.dah | 309 |
| H2730 cha.red | 310 |
| H7264 ra.gaz | 1554 |
| H7268 rag.gaz | 1576 |
| H7269 rog.zah | 1577 |
| H7460 ra.ad | 1793 |
| H7461A ra.ad | 1792 |
| H7461B re.a.dah | 311 |
| H8175A sa.ar | 1744 |
| H8178A sa.ar | 1746 |
| H6427 pal.la.tsut | 282 |
| H6426 pa.lats | 1719 |
| H2113 ze.va.ah | 1158 |
| H7374 re.tet | 279 |
| H8429 te.vah | 1733 |
| G5156 tromos | 308 |
| G1790 entromos | 307 |
| H6206 a.rats | 306 |

**M01-F — Anxiety (3 terms)**

| Strong's | mti_id |
|---|---|
| H1674 de.a.gah | 107 |
| H8312 sar.ap.pim | 349 |
| G0085 ademoneo | 2 |

**M01-G — Awe and Wonder (4 terms)**

| Strong's | mti_id |
|---|---|
| G1568 ekthambeo | 16 |
| G1569 ekthambos | 5126 |
| G2285 thambos | 1245 |
| H8539 ta.mah | 289 |

**M01-H — Timidity and Cowardice (3 terms)**

| Strong's | mti_id |
|---|---|
| G1167 deilia | 288 |
| G1168 deiliaō | 261 |
| G1169 deilos | 1701 |

**M01-BOUNDARY (3 terms)**

| Strong's | mti_id |
|---|---|
| G1280 diaporeō | 4481 |
| G0639 aporeō | 4482 |
| H7672 she.vash | 4483 |

### 3. Cluster status transition

Update `cluster.status` for `cluster_code = 'M01'` from `'Data - In Progress'` → `'Analysis - In Progress'`.

---

## COMPLETION CONFIRMATION

CC must return all of the following:

**1. Pre-execution term count:**
```sql
SELECT COUNT(*) FROM mti_terms
WHERE cluster_code = 'M01'
AND status IN ('extracted','extracted_thin');
```
Expected: 82. If not 82 — halt and report.

**2. Sub-groups created:**
```sql
SELECT subgroup_code, subgroup_label
FROM cluster_subgroup
WHERE cluster_code = 'M01'
ORDER BY subgroup_code;
```
Expected: 9 rows — M01-A, M01-B, M01-C, M01-D, M01-E, M01-F, M01-G, M01-H, M01-BOUNDARY.

**3. Term assignments — count per sub-group:**
```sql
SELECT cs.subgroup_code, COUNT(*) AS term_count
FROM mti_terms mt
JOIN cluster_subgroup cs ON mt.cluster_subgroup_id = cs.id
WHERE mt.cluster_code = 'M01'
AND mt.status IN ('extracted','extracted_thin')
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
```
Expected counts:

| subgroup_code | term_count |
|---|---|
| M01-A | 19 |
| M01-B | 13 |
| M01-C | 17 |
| M01-D | 5 |
| M01-E | 19 |
| M01-F | 3 |
| M01-G | 4 |
| M01-H | 3 |
| M01-BOUNDARY | 3 |
| **Total** | **86** |

Note: Total = 86, not 82. This is correct — 4 terms appear in two sub-group assignments (H2865 cha.tat: primary D + secondary A note; H2730 cha.red: primary E + secondary A note; G5156 tromos: primary E + secondary A note; H6206 a.rats: primary E + secondary A note). If the schema uses a single `cluster_subgroup_id` FK per term, the total will be 82 (one row per term). If a separate `mti_term_subgroup` many-to-many table is used, secondary assignments may also be inserted. CC determines from schema — report whichever count reflects the actual insert.

**4. H6 health check — all terms now assigned:**
```sql
SELECT COUNT(*) FROM mti_terms mt
WHERE mt.cluster_code = 'M01'
AND mt.status IN ('extracted','extracted_thin')
AND mt.cluster_subgroup_id IS NULL;
```
Expected: **0** — all terms assigned.

**5. Cluster status:**
```sql
SELECT status FROM cluster WHERE cluster_code = 'M01';
```
Expected: `Analysis - In Progress`

**6. Sample — 3 rows per sub-group (one representative term each):**
CC to return one row per sub-group showing: `subgroup_code`, `strongs_number`, `mti_id` — confirming assignments are correctly linked.

---

*DIR-20260515-002 | wa-cluster-M01-dir-001-subgroup-assign-v1-20260515.md | Phase 4 sub-group assignment — 9 sub-groups created, 82 terms assigned | Basis: wa-obslog-M01-cluster-m01-v1-20260515.md Phase 4 | Source report: wa-cluster-M01-comprehensive-v4-20260515.md | Predecessor: DIR-20260515-001 (cross-cluster transfer) | Next: Phase 5 (UT review — vacuous) → Phase 6 (VCG mapping) via DIR-20260515-003*
