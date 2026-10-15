# M08 Pride & Arrogance: cluster overview (strand start)

**Date:** 2026-10-15 · **Escalation:** #2156 · **Status:** data overview only. No verse has been read for M08.

**Instruction (researcher, chat 2026-10-15, verbatim):** *"start with M08 and do a summary of the cluster"*.

**Source:** read-only against iba.db, in the same shape as the M09 overview (#2148). It uses live `cluster_strong` rows only and hits from `verse_lexical`. The "other" side is every other M-cluster. Narrative citations and claims-register sources are read live from `narrative_citation` and `narrative_claim_source` (#2110).
- Pull script: [`m08-cluster-overview-pull-v1-20261015.py`](m08-cluster-overview-pull-v1-20261015.py). This is the M09 script with the code changed.
- Extras script (gloss groups, surface split, the scan of words outside M08, narrative sections and claims): [`m08-cluster-overview-extras-v1-20261015.py`](m08-cluster-overview-extras-v1-20261015.py).
- All hits: [`m08-cluster-hits-v1-20261015.csv`](m08-cluster-hits-v1-20261015.csv) (607 rows).
- Per Strong's, with the tag source: [`m08-cluster-strongs-v1-20261015.csv`](m08-cluster-strongs-v1-20261015.csv) (75 rows).
- Other M-codes in the same verses: [`m08-cluster-mcode-cooccurrence-v1-20261015.csv`](m08-cluster-mcode-cooccurrence-v1-20261015.csv).
- Every M08 verse with its M08 Strong's, its narrative places, whether it is in the claims register, and its other M-codes: [`m08-cluster-verses-crossref-v1-20261015.csv`](m08-cluster-verses-crossref-v1-20261015.csv) (528 rows).

## 1. The cluster

- **Name:** Pride & Arrogance.
- **Definition in `cluster`:** "Pride, arrogance, haughtiness, boasting, scoffing, self-exaltation".
- **Status:** `t_cluster_assignment_completed`.
- **How the 75 live Strong's came to be tagged** (`cluster_strong.source`):

| Source | Strong's |
| --- | --- |
| old-system migration | 47 |
| LLM allocation v1.3 | 13 |
| auto-precedent | 11 |
| heuristic family grouping (2026-09-05), family "pride-arrogance-scoffing" | 3 |
| Claude scan (2026-09-08): H7342I "broad: arrogant" | 1 |

- **Deleted rows (4):**
  - Three Strong's left M08 earlier:
    - G0757 "be first", now T3
    - H6965B "to arise: rise", now T3
    - H2778A *ḥārap̄* "to taunt", now M53
  - One is a superseded duplicate of a row that is still live: H1984H *hālal* "to boast".
- Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.

## 2. Scale

| Measure | Count |
| --- | --- |
| M08 Strong's (live), all with hits | 75 (45 Hebrew, 30 Greek) |
| M08 hits (distinct verse · position · Strong's) | 607 |
| Verses | 528 (OT 403, NT 125) |
| Books | 56 |
| Verses with more than one M08 hit | 59 |
| Verses that also hold another M-code | 432 |
| Verses with no other M-code | 96 |
| Verses already cited in the narrative | 122 |
| Verses that are a source in the claims register | 46 |

M08 is about twice the size of M09 (273 verses) and well under half of M18 (1,370).

**Books with the most M08 verses:**

| Book | Verses |
| --- | --- |
| Psa | 66 |
| Isa | 61 |
| Pro | 42 |
| Eze | 41 |
| Job | 31 |
| Jer | 30 |
| 2Cor | 27 |
| 2Ch | 17 |
| 1Ki | 16 |
| Exo | 15 |
| Rom | 14 |
| 1Cor | 14 |
| Deu | 12 |
| Luk | 11 |

1Ki and Exo are mostly measurements: the height of the temple, its pillars and the tabernacle furniture (group B). 2Cor is Paul's boasting (group C).

## 3. The Strong's by gloss

These groups are a reading aid by gloss and surface only. They are not a finding, and they are not a sub-grouping of the cluster.

| Gloss group | Strong's | Hits | Verses | Cited | No other M-code |
| --- | --- | --- | --- | --- | --- |
| A. pride, arrogance, presumption | 37 | 189 | 165 | 48 | 13 |
| B. height, high, lofty | 11 | 237 | 211 | 38 | 59 |
| C. boast, boasting | 8 | 92 | 80 | 20 | 12 |
| D. mock, scoff, taunt | 12 | 77 | 76 | 17 | 11 |
| E. majesty | 2 | 6 | 6 | 1 | 1 |
| F. gloss away from the cluster | 5 | 6 | 6 | 3 | 0 |

**Most verses hold one group only:**

| Groups in the verse | Verses |
| --- | --- |
| B only | 199 |
| A only | 152 |
| C only | 77 |
| D only | 73 |
| A and B | 9 |
| F only | 6 |
| E only | 5 |
| A and D, A and C | 2 each |
| B and C, B and D, B and E | 1 each |

The height words make up 39% of the hits, the pride words 31%, boasting 15% and mocking 13%.

### 3A. Pride, arrogance, presumption (37 Strong's, 189 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H1347 *gāʾôn* | pride | 49 | 45 | pride (25), majesty (9), proud (4), thicket (3), majestic (2), pomp (2) |
| H1346 *gaʾăwāh* | pride | 19 | 19 | pride (7), arrogance (4), proudly (2), majesty (2), back (2), triumph (1) |
| H2086 *zēd* | arrogant | 13 | 13 | insolent (8), arrogant (3), pomp, presumptuous |
| H2087 *zādôn* | arrogance | 11 | 11 | pride (4), presumptuously (2), proud one (2), presumption, insolence |
| H2102 *zîd* | to boil | 10 | 10 | acted presumptuously (2), act presumptuously, presumes, acted arrogantly, proudly defied |
| H1343 *gēʾeh* | proud | 9 | 9 | proud (8), arrogant (1) |
| H1348 *gēʾût* | majesty | 8 | 8 | proud (2), majesty (2), arrogantly, gloriously, raging, column |
| G5448 *physioō* | to inflate | 7 | 7 | arrogant (3), puffed up (2), puffs up |
| H1342 *gāʾāh* | to rise up | 7 | 5 | triumphed (2), gloriously (2), grow, lifted up, risen |
| H7312 *rûm* | height | 6 | 6 | lofty pride (2), haughtiness, Haughty, height, boastful |
| G5244 *hyperēphanos* | arrogant | 5 | 5 | proud (3), haughty, arrogant |
| 26 others | | 45 | | 1–4 hits each, among them H6277 "arrogant", H7292 *rāhab* "insolent", G5187 "puffed up", G5229 "becoming conceited", G0212/G0213 *alazoneia*/*alazōn* "arrogance", "boastful", G0829 "self-willed", G2755 "conceited", G4409 "preeminent" (Col 1:18, of Christ), G5367 "lovers of self" (2Ti 3:2), G5309 "haughty" (1Ti 6:17), G5252 "more highly" (Rom 12:3) |

### 3B. Height, high, lofty (11 Strong's, 237 hits)

| Strong's | Gloss | Hits | Verses | Hits with a pride-like surface |
| --- | --- | --- | --- | --- |
| H4791 *mārôm* | height | 54 | 52 | 2 (Obd 3 "lofty"; Psa 56:2 "proudly") |
| H6967 *qômāh* | height | 44 | 42 | 0 (height, stature, tallest) |
| H1364 *gābōah* | high | 41 | 36 | 11 (arrogant, proudly, haughty, lofty, proud) |
| H1361 *gābah* | to exult | 34 | 33 | 15 (proud, haughty, grew proud, exalted) |
| H5945A *ʿelyôn* | high | 19 | 19 | 1 (2Ch 7:21 "exalted"); mostly "upper" (11) |
| H1363 *gōbah* | height | 17 | 16 | 4 (Psa 10:4 and 2Ch 32:26 "pride"; Jer 48:29; Pro 16:18) |
| G5308 *hypsēlos* | high | 11 | 11 | 4 (Luk 16:15; Rom 11:20; Rom 12:16; Act 13:17) |
| G5311 *hypsos* | height | 6 | 6 | 1 (Jam 1:9 "exaltation") |
| H7314, H5920H, G5313 | height, top, above | 11 | | 1 (2Co 10:5 "lofty opinion") |

Only 39 of the 237 hits carry a surface that names pride or exaltation (a surface match, not a reading). The rest are height as a measure (the ark, the altar, the temple pillars, Goliath), high places and towers, and God "on high".

### 3C. Boast, boasting (8 Strong's, 92 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| G2744 *kauchaomai* | to boast | 37 | 32 | boast (27), rejoice (3), boasts (3), boasting (2), glory, boasted |
| H1984H *hālal* | to boast | 24 | 21 | boast (11), boasts (4), glory (4), exult (2), Glory (2), boasted |
| G2746 *kauchēsis* | pride | 12 | 12 | boasting (6), pride (2), proud, boast, confident, boastful |
| G2745 *kauchēma* | pride | 11 | 11 | boasting (5), boast (3), glory, proud, boast about |
| G2620 *katakauchaomai* | to boast | 4 | 3 | boast, arrogant, triumphs |
| G4068, G5246, G6094 | | 4 | | boast, loud boasts, boasters, boasts |

### 3D. Mock, scoff, taunt (12 Strong's, 77 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H3887 *lîṣ* | to mock | 28 | 27 | scoffer (10), scoffers (3), scoff (2), mocks, mockers |
| H3932 *lāʿag* | to mock | 18 | 18 | mocks (5), mock (3), jeered (2), scorns (2), derision (2) |
| G1702 *empaizō* | to mock | 13 | 13 | mocked (9), mock (2), tricked (1), mocking (1) |
| H7046 *qālas* | to mock | 4 | 4 | jeered, mock, scorned, scoff |
| H8148 *šᵊnînāh* | taunt | 4 | 4 | byword (3), taunt (1) |
| G2606 *katagelaō* | to mock | 3 | 3 | laughed (3) |
| 6 others | | 7 | | H8591, H1422, H2048A, H4167, H5607A, G3456 (1–2 each) |

### 3E and 3F

- **E. Majesty** (G3168 *megaleiotēs*, G3172 *megalōsynē*): "Majesty" in Heb 1:3 and 8:1, Jude 25, and the "majesty" of God and of Christ in Luk 9:43 and 2Pe 1:16. Under #1982 these go to God's character (13.1). The sixth verse is Act 19:27, the "magnificence" of Artemis.
- **F. Gloss away from the cluster.** Each came in by migration or by precedent.
  - G0193 *akratēs* "without self-control" (2Ti 3:3)
  - H5719 *ʿādîn* "lover of pleasures" (Isa 47:8)
  - H5953C "infants" (Isa 3:12)
  - H7293 *rahab* "Rahab", the name (2 verses)
  - H7296 *rōhab* "span" (Psa 90:10)

## 4. Where the surface varies within one Strong's

This is where the change-of-character reading (#1919) would start. No reading has been done.
- **H1347 *gāʾôn*:** human "pride" (25) versus God's "majesty" (9) versus "the thicket of the Jordan" (3).
- **H1361 *gābah*:** "proud" and "haughty" (Eze 28:2, 5; 2Ch 26:16; 32:25) versus "towered" and "higher" (physical) versus "exalted" of God (Isa 5:16) and of the servant (Isa 52:13).
- **H1364 *gābōah* and H1363 *gōbah*:** high walls and tall men versus "haughty eyes" and "a haughty spirit" (Pro 16:18).
- **G2744 *kauchaomai*:** "boast" versus "rejoice" (Rom 5:2–3, 11). Boasting in oneself versus "let the one who boasts, boast in the Lord" (1Co 1:31; 2Co 10:17).
- **H1984H *hālal*:** "boast" versus "glory" and "exult" (Jer 9:24, "let him who boasts boast in this").
- **G1702 *empaizō*:** Jesus "mocked" in the passion accounts versus Herod "tricked" by the magi (Mat 2:16).
- **H7292 *rāhab*:** "insolent" (Isa 3:5) versus "plead urgently" (Pro 6:3) versus "overwhelm" (Song 6:5).

## 5. Words outside M08 that carry the same sense (gloss and surface scan)

This scan follows the OT-02 lesson (`feedback_strand_pulls_check_t_coded_synonyms`). Some Strong's carry pride, exaltation, boasting or mocking in their gloss or surface but are tagged to another cluster. None of them is pulled. The table records where they sit. Pronoun and particle codes (H90xx, H0853, H3588A and others) are left out. They match only because a span surface is attached to the particle, not to the word.

| Strong's | Gloss | Tagged | Verses | Shared with M08 | Cited | Surface that bears on M08 |
| --- | --- | --- | --- | --- | --- | --- |
| H7311A *rûm* | to exalt | M22 | 184 | 16 | 28 | exalted (28), exalt (11), lofty (5), exalts (4) |
| G5312 *hypsoō* | to lift up | T3 | 15 | 1 | 8 | exalted (9), exalts (3), exalt (2) |
| H5375L *nāśāʾ* | to lift: exalt | T3 | 13 | 1 | 5 | exalted (7), exalting yourself (1) |
| H7682 *śāgab* | to exalt | M22 | 20 | 5 | 4 | exalted (6), lofty (1) |
| H1431 *gādal* | to magnify | M22 | 114 | 2 | 16 | boast (2), exalted (2), deals insolently (1) |
| H2781 *ḥerpāh* | reproach | M07 | 72 | 2 | 12 | scorn (6), insolence (2), mocked, insolently |
| H2778A *ḥārap̄* | to taunt | M53 | 38 | 7 | 4 | mock (6), mocked (4), scoff, scoffs (left M08) |
| H3933, H3934, H3944, H2049, H4426, H7589, H4485 | derision, mocking, scorning | M06 | 1–7 each | 3 | 3 | scorn, scoffers, mockers |
| H7832 *śāḥaq* | to laugh | M04 | 36 | 6 | 11 | mocked, scorns, scorn |
| H1984C *hālal* | to be foolish | M16 | 9 | 0 | 1 | boastful (2), arrogant, boast |
| H1433 *gōdel* | greatness | M71 | 13 | 2 | 4 | arrogance, arrogant |
| H5678 *ʿebrāh* | fury | M02 | 34 | 3 | 19 | insolence (2), pride (1) |
| G5111 *tolmaō* | be bold | M23 | 15 | 0 | 5 | boast (2), presume |
| G2754 *kenodoxia* | empty conceit | T2 | 1 | 0 | 1 | conceit (Php 2:3) |
| G5197 *hybristēs* | insolent man | T2 | 2 | 1 | 1 | insolent (Rom 1:30; 1Ti 1:13) |
| G1703 *empaiktēs*, G1701, G5512 *chleuazō* | scoffer, jeering, to sneer | T2 / T3 | 1–2 each | 0 | 1 | scoffers (2Pe 3:3; Jud 18), mocking |
| H0907 *bad*, H7317 *rômāh*, H4062 | bluster, haughtily, insolence | T2 | 1–7 each | 2 | 3 | idle boasting, haughtily, insolent fury |

Points that follow from the scan, with no reading done:
- **Self-exaltation**, which the definition names, sits mostly outside M08. H7311A *rûm* (M22, 184 verses) holds "exalted" and "lofty". G5312 *hypsoō* (T3) holds "whoever exalts himself will be humbled" (Mat 23:12; Luk 14:11; 18:14), and also the Son of Man "lifted up" (Joh 3:14; 8:28; 12:34) and God exalting the humble (Jam 4:10; 1Pe 5:6). Most of these words also carry God being exalted, which is why they sit in M22 Praise.
- **Scorn and derision words** sit in M06 Malice & Enmity. H2778A "to taunt" is in M53.
- **Php 2:3 "empty conceit"** (G2754) and the NT scoffers of 2Pe 3:3 (G1703) are T2.

## 6. Other M-codes in the same verses

432 of the 528 verses also hold a word from another M-cluster. Shared verses, top 25:

| M-code | Verses | M-code | Verses |
| --- | --- | --- | --- |
| M47 Inner Seat | 65 | M14 Deceit & Falsehood | 22 |
| M72 Authority & Dominion | 55 | M41 Being Heard | 22 |
| M23 Strength & Courage | 47 | M61 Purity & Holiness | 22 |
| M22 Praise & Song | 47 | M06 Malice & Enmity | 21 |
| M58 Wickedness | 42 | M53 Dishonor & Disgrace | 21 |
| M15 Knowing & Understanding | 39 | M02 Anger & Wrath | 20 |
| M65 Speech & Tongue | 36 | M12 Righteousness & Integrity | 20 |
| M16 Wisdom & Folly | 29 | M46 Wealth & Riches | 19 |
| M18 Desire & Longing | 26 | M25 Life & Death | 19 |
| M01 Fear & Awe | 24 | M43 Prophecy & Vision | 18 |
| M24 Faintness & Despair | 24 | M30 Rebellion & Stubbornness | 17 |
| M04 Joy & Gladness | 23 | M10 Violence & Cruelty | 17 |
| M09 Humility & Lowliness | 23 | | |

**What earlier strands already hold for M08:**
- **M09 (23 shared verses).** These are the paired sayings, for example Jam 4:6, 1Pe 5:5, Pro 3:34, Pro 29:23, Pro 11:2, Psa 138:6, Job 22:29, Eze 21:26 and Dan 4:37. Most were read in the M09 humbling fan-out (#2148) and woven into **10.14 *The proud brought low, the lowly raised***.
- **M47 (65 shared verses).** Under the #1979 closure, each strand checks its M47 verses for dropped placements, by word and not by citation (OT-09).
- **M72 (55 shared verses).** Two group B verses are marked forward to M08: Eze 19:11 and Eze 29:15 (`m72-group-B-role-triage-v1-20261012.csv`). One group D verse names M08 among its forwards: Psa 36:11, "the foot of arrogance" (`m72-group-D-forward-v2-20261012.csv`).
- **M18 (26 shared verses), OT-97 item 25 (`cluster:M08`).** Two verses are marked forward to M08: 2Co 11:12 and 2Co 12:6, both Paul's boasting (`m18-group-C-role-triage-v2-20261012.csv`).
- **M02 (20 shared verses), OT-103 item 22 (`cluster:M08`).** These 20 verses fall across 16 anger faces. The list is the M08 rows of `wa-cluster-M02-mcode-face-combinations-v1-20261005.csv`.
- **OT-05 item 16 (`cluster:M08`).** Self-glory: "she glorified herself" (Rev 18:7) and "they glory in their shame" (Php 3:19). These are G1391 *doxa* verses (M22), held in `life-death-ot05-body-raised-groups-v1-20261014.csv`.
- **Open threads matched** (`Escalation.ps1 -Action Match -Cluster M08 -Strong <75>`): OT-05 (item 16), OT-97 (item 25) and OT-103 (item 22). No thread names an M08 Strong's or verse directly.

**In the narrative now.** 122 M08 verses are cited. By chapter:

| Chapter | Verses cited |
| --- | --- |
| 10.14 | 40 |
| Ch 12 | 20 |
| Ch 11 | 19 |
| 13.1 | 16 |
| Ch 2 | 14 |
| 10.13 | 13 |
| Ch 4 | 11 |
| 10.6, 10.12 | 10 each |
| 10.10 | 8 |
| 10.7, Ch 7 | 7 each |
| Ch 6, 10.1 | 6 each |
| 10.4 | 5 |

A citation is verse-level and does not mean the M08 word was read (#1987).

- **Sections on pride already exist:**
  - **Ch 12 *Pride and the lifted-up heart and spirit*.**
  - **10.14 *The proud brought low, the lowly raised*** (from M09).
- **Pride words in the current narrative text:** "proud" 23 times, "pride" 20, "haughty" 11, "boast" and its forms 9 (all but one in 10.14), "lifted up" 3, "arrogant" 2, "mock" and its forms 2. Ch 12 and 10.14 hold most of them.
- **Claims on pride in the register (all current):**
  - C-207 to C-211: pride in the heart and spirit, comparison, given beauty, death brings pride down, designed honour. These were registered for Ch 12 in update 142 (#2152).
  - C-168, C-171 and C-180 to C-182: humility set against a rising, Hezekiah, God brings low a bearing, only God lifts up and puts down, the boast moved to what God does. These come from M09.
  - 2-2: the spirit judged as haughty.
- 46 M08 verses are claim sources.
- Under rule 77 (#2154), when Ch 12 or 10.14 is touched, the existing claims on pride in those chapters are reconciled in the same pass.

**Verses with no other M-code (96).** Most are height as a measure: Exo 25 to 38, 1Ki 6 to 7, Eze 40 to 42, and Goliath in 1Sa 17:4. Others are central to the cluster:
- Paul's boasting: Rom 15:17, Gal 6:14, 1Co 1:31, 2Co 10:17, 2Co 12:1, Eph 2:9
- Jam 3:5, the tongue that "boasts of great things"
- Isa 3:16, the daughters of Zion "haughty"
- the mocking of Jesus: Mat 27:31, Mat 27:41, Mar 15:20, Luk 23:36
- 2Ki 2:23, the boys who jeered Elisha

The list is in the crossref CSV (blank `other_mcodes`).

## 7. Within-M08 pairs (verses with more than one M08 hit)

There are 107 unordered pairs in 59 verses:

| Pair | Count |
| --- | --- |
| H1364 + H1364 (high, high) | 7 |
| H1346 + H1347 (pride, pride: *gaʾăwāh* with *gāʾôn*) | 5 |
| G2744 + G2744 (boast, boast) | 5 |
| H1347 + H1347 | 4 |
| H1347 + H1363 (pride, height) | 4 |
| H1984H + H1984H | 4 |
| H1361 + H6967 (be high, height) | 4 |
| H1361 + H1363, H1363 + H6967, H4791 + H6967, H1364 + H6967 | 3 each |

The *gāʾôn* and *gaʾăwāh* pairs are the stacked pride sayings, for example Jer 48:29 and Isa 16:6.

## 8. Earlier M08 work (pre-reset, archived)

The old system produced an M08 study before the 2026-06-25 method reset. It holds 177 files in `_analytics/Clusters/archive/stale-20260907/M08-Pride/`. It is legacy under that reset and is not used here. It is noted only so that the investigation it holds is known.

## 9. Points for your direction

M09 began from an overview like this one and was then fanned out. These are the facts that bear on where to start. The choice is yours.

1. **Group A, the pride words** (37 Strong's, 165 verses). These are closest to the inner act the definition names: the proud heart, haughty eyes, presumption, being puffed up.
2. **Group C, boasting** (80 verses). Its main change of character is boasting in oneself versus boasting in the Lord (1Co 1:31; 2Co 10–12; Jer 9:24). 2Cor alone has 27 M08 verses.
3. **Group D, mocking and scoffing** (76 verses). It covers the scoffer of Proverbs, the mocking of others (Elisha, the righteous), and the mocking of Jesus in the passion accounts. The scorn words are in M06 (§5).
4. **Group B, the height words** (211 verses). Only 39 hits carry a pride-like surface; the rest are measures, places and God on high. This is like the M72 ruling (#1998): read by role, the height word is mostly a qualifier or a measure, with C (no bearing) for the measures. Those 39 hits are where B bears on M08.
5. **E (majesty) goes to God's character only (13.1). F is data.**
6. **The words outside M08** (§5): self-exaltation in M22 and T3 (H7311A *rûm*, G5312 *hypsoō*), scorn in M06, taunting in M53, and "empty conceit" (Php 2:3) in T2. Under #1970 these are not re-tagged. Whether any of them is read with this strand is for you to say.
7. **What is already in the narrative:** Ch 12 *Pride and the lifted-up heart and spirit*, 10.14 *The proud brought low, the lowly raised*, and claims C-207 to C-211. The M09 shared verses are largely read.
8. **What earlier strands hold:**
   - 2 M18 forward marks (OT-97)
   - the 20 M02 verses (OT-103)
   - 3 M72 forward marks
   - OT-05 self-glory
   - the 65 M47 verses (#1979 check)

## 10. Note on the data

- The narrative counts come from `narrative_citation` rows with `last_version IS NULL` in active chapters, which are the current citations. The claims-register count comes from `narrative_claim_source.verse_id`. The word counts come from current `narrative_passage` text.
- The pride-like surface split in §3B is a surface pattern match (proud, haught, arrogan, lofty, exalt, pride, conceit, lifted). It is a pointer, not a reading.
- The §5 scan matched surfaces as well as glosses. Particle and pronoun codes are excluded from the table, because they carry the surface of the span they are attached to.
