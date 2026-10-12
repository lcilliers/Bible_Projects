# M72 Authority & Dominion: cluster overview (strand start)

**Date:** 2026-10-12 · **Escalation:** #1998 · **Status:** data overview only. No verse has been read for M72.

**Instruction (researcher, chat 2026-10-12, verbatim):** *"proceed with M72, starting with overview of M72"*.

**Source:** read-only against iba.db, the same shape as the M18 overview (#1993) and the M64 quick summary (#1978): live `cluster_strong` rows only, hits from `verse_lexical`, and the "other" side is every other M-cluster.
- Script: [`m72-cluster-overview-pull-v1-20261012.py`](m72-cluster-overview-pull-v1-20261012.py), the M18 script with the code changed
- All hits: [`m72-cluster-hits-v1-20261012.csv`](m72-cluster-hits-v1-20261012.csv) (5,599 rows)
- Per Strong's, with the tag source: [`m72-cluster-strongs-v1-20261012.csv`](m72-cluster-strongs-v1-20261012.csv) (55 rows)
- Other M-codes in the same verses: [`m72-cluster-mcode-cooccurrence-v1-20261012.csv`](m72-cluster-mcode-cooccurrence-v1-20261012.csv)
- Every M72 verse against the current narrative and the open threads register (crossref v3): [`m72-cluster-verses-crossref-v1-20261012.csv`](m72-cluster-verses-crossref-v1-20261012.csv) (3,972 rows)

## 1. The cluster

- **Name:** Authority & Dominion. **Definition in `cluster`:** "Authority, dominion, kingship, rule, reigning, lordship". Status `t_cluster_assignment_completed`.
- **How the 55 live Strong's came to be tagged** (`cluster_strong.source`):

| Source | Strong's |
| --- | --- |
| heuristic family grouping (2026-09-05) | 46 |
| Claude scan (2026-09-08): H4428G king, H3027H hand: power, H8269 ruler, H4430 king | 4 |
| researcher ruling #1880 (2026-09-28): G0746 *archē* | 1 |
| old-system migration: H3678G throne | 1 |
| LLM allocation v1.3: H4438 royalty | 1 |
| auto-precedent: H5387A leader | 1 |
| manual backfill triage: H7218H head: leader | 1 |

- No deleted rows. Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.
- The four Strong's added by the Claude scan hold 3,606 of the 5,599 hits (64%).

## 2. Scale

| Measure | Count |
| --- | --- |
| M72 Strong's (live), all with hits | 55 (33 Hebrew, 22 Greek) |
| M72 hits (distinct verse · position · Strong's) | 5,599 |
| Verses | 3,972 (OT 3,532, NT 440) |
| Books | 62 |
| Verses with more than one M72 hit | 1,144 |
| Verses that also hold another M-code | 2,978 |
| Verses already cited in the narrative | 388 |

For comparison, M18 had 88 Strong's, 1,510 hits and 1,370 verses. M72 has almost three times as many verses as M18, and 89% of them are in the Old Testament.

Books with the most M72 verses: 2Ki 341, 2Ch 335, Jer 334, 1Ki 305, 2Sa 246, Dan 192, Isa 189, 1Ch 165, 1Sa 152, Psa 148, Est 125, Eze 106, Judg 98, Mat 97. These are the history books and the prophets.

**One Strong's dominates.** H4428G *melekh*, "king", has 2,441 hits in 1,870 verses: 44% of all hits and 47% of the verses. The most frequent pair in one verse is "king" with "king" (735 verses), then "king" with "ruler" (204) and "king" with "hand" (184).

## 3. The Strong's by gloss

The groups below are a reading aid by gloss only. They are not a finding and not a sub-grouping of the cluster.

| Gloss group | Strong's | Hits | Verses |
| --- | --- | --- | --- |
| A. king, reign, kingdom, throne, palace | 18 | 3,572 | 2,582 |
| B. rule, dominion, authority, lordship (the act of ruling) | 25 | 309 | 275 |
| C. officials, leaders, masters | 5 | 757 | 651 |
| D. hand as power | 1 | 578 | 510 |
| E. titles of God: Lord of hosts, Most High | 3 | 295 | 283 |
| F. gloss away from authority | 3 | 88 | 86 |

**In 3,118 verses the only M72 words are from groups A, C and E.** These are kings, officials and divine titles. In 243 verses the only M72 word is "hosts" in "the Lord of hosts". Group B, where ruling is named as an act, is in 275 verses.

### 3A. King, reign, kingdom, throne, palace (18 Strong's, 3,572 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H4428G *melekh* | king | 2,441 | 1,870 | king (1,686), King (243), kings (221), king's (219), Kings (47), royal (9) |
| H4427A *mālakh* | to reign | 347 | 283 | reigned (150), reign (99), king (44), became king (11), reigns (9), made him king (7) |
| H4430 *melekh* (Aramaic) | king | 177 | 128 | king (126), King (22), king's (14), kings (11), royal (4) |
| G0932 *basileia* | kingdom | 162 | 154 | kingdom (156), kingdoms (3), royal power (2), dominion (1) |
| H3678G *kissēʾ* | throne | 124 | 114 | throne (111), thrones (6), seat (4) |
| H4467 *mamlākhāh* | kingdom | 117 | 113 | kingdom (55), kingdoms (48), royal (6), royal power (3) |
| H4438 *malkhût* | royalty | 91 | 82 | kingdom (43), reign (20), royal (18), realm (3) |
| H4437 *malkhû* (Aramaic) | kingdom | 54 | 41 | kingdom (44), kingdoms (3), royal (3) |
| G0936 *basileuō* | to reign | 21 | 18 | reign (13), reigned (4), kings (2) |
| H1002 *bîrāh* | palace | 16 | 16 | citadel (12), palace (2) |
| H4468 *mamlākhût* | kingdom | 8 | 8 | kingdom (7), reign (1) |
| 7 others | | 14 | | G0937 *basilikos* "official, royal" 5; H1055 palace 3; G4821 "reign with" 2; G0933, G0934, G0938G "queen", H0643 1 each |

97 of the 154 G0932 verses say "kingdom of God" or "kingdom of heaven".

### 3B. Rule, dominion, authority, lordship (25 Strong's, 309 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| G1849 *exousia* | authority | 102 | 93 | authority (64), power (12), right (11), authorities (8), rightful claim (1) |
| H4910 *māšal* | to rule | 81 | 74 | rule (27), ruler (18), ruled (8), rules (7), rulers (6) |
| H7287A *rādāh* | to rule | 22 | 22 | dominion (6), rule over (3), rule (3), ruled (2), charge (2) |
| H4475 *memšālāh* | dominion | 17 | 16 | dominion (8), rule (4), realm (2), authority (2) |
| H7985 *šolṭān* (Aramaic) | dominion | 14 | 9 | dominion (13) |
| H7990 *šallîṭ* (Aramaic) | ruling | 10 | 10 | rules (5), powerful, captain, ruler, lawful |
| H7980 *šālaṭ* | to domineer | 8 | 7 | power (3), get dominion, mastery, gained mastery, lorded |
| G2961 *kurieuō* | to lord over | 7 | 7 | has dominion over, dominion, exercise lordship, binding on |
| H7981 *šᵊlēṭ* (Aramaic) | to rule | 7 | 7 | ruler (3), rule (2), overpowered, power |
| H8323A *śārar* | to rule | 5 | 4 | rule (2), master, make, prince |
| 15 others | | 36 | | G1850 "authority over, dominated" 4; G2634 "lord it, domineering, mastered" 4; G2963 "authority, dominions" 4; H7989 4; H4474 3; H7786 "strove, ruled" 3; G2715 "exercise authority" 2; G5247 "high positions" 2; H2632 2; H4915B 2; H4951 "government" 2; G0831 "exercise authority" 1; G1018 "rule" (of peace, Col 3:15) 1; G2230 1; H4896 1 |

### 3C. Officials, leaders, masters (5 Strong's, 757 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H8269 *śar* | ruler | 410 | 357 | princes (86), officials (72), commanders (62), commander (39), captains (22), chief (21) |
| H7218H *rōʾš* | head: leader | 154 | 141 | heads (66), chief (30), head (27), chiefs (12), leader (4) |
| H5387A *nāśîʾ* | leader | 102 | 88 | prince (28), chiefs (20), chief (16), leaders (14), princes (13) |
| G2962H *kurios* | lord: master | 85 | 79 | master (33), Sir (12), Lord (7), owner (6), Master (6), masters (5) |
| H7336 *rāzan* | to rule | 6 | 6 | rulers (4), princes (2) |

### 3D. Hand as power (1 Strong's, 578 hits)

H3027H *yād* "hand: power", 510 verses. Surface: hand (459), power (30), hands (29), charge (10), under the direction (5), direction (5). This is the hand in the sense of power or control: "into the hand of", "by the hand of", "the hand of the Lord".

### 3E. Titles of God (3 Strong's, 295 hits)

H6635B *ṣᵊbāʾôt* "[Lord of] Hosts" 283 (hosts 281); G4519 *sabaōth* 2; H5943 *ʿillay* "Most High" (Aramaic, Daniel) 10.

### 3F. Gloss away from authority (3 Strong's, 88 hits)

- G0746 *archē*: 56 hits. Surface: beginning (36), rulers (6), rule (3), first (2), corners (2), authorities (1). It was tagged by researcher ruling #1880.
- G2233 *hēgeomai*: 28 hits. Surface: count (7), leaders (3), ruler (2), considered (2), regard (2), thought (2). Mostly a verb of reckoning. Its use in 2Pe 2:13 ("count it pleasure") is the worked case in the reading-by-role guide §6.
- G2583 *kanōn*: 4 hits. Surface: influence (3), rule (1).

## 4. Where the surface varies within one Strong's

This is where the change-of-character reading (#1919) would start. No reading has been done.
- H3027H *yād*: hand / power / charge / direction.
- G1849 *exousia*: authority / power / right / authorities / "rightful claim".
- H4427A *mālakh*: reign / "became king" / "made him king".
- H7786 *śûr*: "strove" (Hos 12:4, of Jacob) and "ruled".
- G0746 *archē* and G2233 *hēgeomai*, as in §3F.

The same surface word sits under several Strong's. For example:
- "kingdom" is under 7: G0932, H4467, H4438, H4437, H4468, and as "dominion" or "realm" under others
- "rule" or "ruler" is under 12 or more, across groups B and C
- "authority" is under G1849, H3027H ("authority" in Gen 41:35), G2963, H4475 and H4474

## 5. Other M-codes in the same verses

2,978 of the 3,972 verses also hold a word from another M-cluster. Verses shared, top 25:

| M-code | Verses | M-code | Verses |
| --- | --- | --- | --- |
| M65 Speech & Tongue | 438 | M24 Faintness & Despair | 162 |
| M23 Strength & Courage | 322 | M10 Violence & Cruelty | 158 |
| M25 Life & Death | 294 | M22 Praise & Song | 150 |
| M15 Knowing & Understanding | 267 | M58 Wickedness | 131 |
| M41 Being Heard | 239 | M36 Worship & Service | 131 |
| M47 Inner Seat | 238 | M01 Fear & Awe | 129 |
| M45 Renewal & Transformation | 211 | M06 Malice & Enmity | 129 |
| M43 Prophecy & Vision | 195 | M12 Righteousness & Integrity | 124 |
| M42 Prayer & Petition | 185 | M16 Wisdom & Folly | 110 |
| M18 Desire & Longing | 182 | M63 Reasoning & Interpretation | 109 |
| | | M33 Rest & Peace | 107 |
| | | M02 Anger & Wrath | 100 |
| | | M46 Wealth & Riches | 99 |

Also: M64 Will & Resolve, 60 verses; M20 Doubt & Discouragement, 29. The rest are in the CSV.

**What earlier strands already hold for M72:**
- **M18 (182 verses), OT-98.** All 182 have been decided in the M18 strand, and the 51 not read before were woven on 2026-10-12. Seven go forward to M72 itself: Gen 31:29; Ezr 7:9; Ezr 8:18; Neh 2:8; Neh 2:18; 1Sa 15:28; Isa 52:7. There is also a pointer to 1Ki 2:15.
- **M02 (100 verses), OT-16.** These span 54 anger faces. The largest are 4P "The ruler's anger, and those beneath it" (9) and 2P "The ruler's wrath, and those beneath it" (5). Their trigger is "M72 is analysed: read only these anger verses, face by face, for how the two operate together".
- **M47 (238 verses).** Under the #1979 closure, each strand checks its M47 verses for dropped placements, by word and not by citation (OT-09). Earlier M47 work called M72 "narrative setting" and gave it low priority (`M47-other-cluster-cooccurrence-assessment-v1-20260927.md`: *"king, hand, hosts, kingdom | Narrative setting; 'Lord of hosts' is a set phrase"*).
- **M25 (294 verses).** The life-death strand candidate note gives the reason for the count: *"die / live + king (mostly 'long live the king', reign notices)"*.
- **Signpost #1893 (hands).** The memory `project_signpost_hands_inner_being` says: when the inner being acting through the hands is taken up, resume the God's-hand pass in `../M02 - anger-wrath/wa-investigation-god-heavy-hand-perception-source-v1-20260929.md` §4. H3027H, "hand: power" (510 verses), holds much of that ground. Whether M72 is that moment is for you to say.

**In the narrative now.** 388 M72 verses are cited, most often in 10.7 (86), Ch 11 (69), 13.1 (50), 10.10 (47), 10.13 (44), 10.6 (37) and 10.1 (36). A citation is verse-level. It does not mean the M72 word was read (#1987).

## 6. Within-M72 pairs (verses with more than one M72 hit)

2,331 unordered pairs, in 1,144 verses. The most frequent:

| Pair | Count |
| --- | --- |
| H4428G + H4428G (king, king) | 735 |
| H4428G + H8269 (king, ruler) | 204 |
| H3027H + H4428G (hand, king) | 184 |
| H4427A + H4428G (reign, king) | 136 |
| H3027H + H3027H | 80 |
| H8269 + H8269 | 77 |
| H3678G + H4428G (throne, king) | 70 |
| H4427A + H4427A | 69 |
| H4428G + H4438 (king, royalty) | 65 |
| H4430 + H4430 (Aramaic king) | 64 |

This reflects the reign notices and court narrative of Kings, Chronicles, Esther and Daniel.

## 7. Points for your direction

M64 and M18 were taken in focused pulls, not broad brush (#1978). M72 is the largest strand so far, and in most of its verses the M72 word names who acts or who decides. These are the facts that bear on where to start. The choice is yours.

1. **Group B, ruling as an act** (25 Strong's, 309 hits, 275 verses): authority, rule, dominion, lording it over, domineering. These words are closest to the cluster definition, and the set is small.
2. **What earlier strands hold:** the 7 M72 forward marks and the 182 M18 readings (OT-98), and the 100 M02 verses by anger face (OT-16). They were read from the partner side and wait for the M72 side.
3. **G0932 "kingdom"** (154 verses, 97 of them "kingdom of God" or "of heaven"). This is mostly God's reign (route A, 13.1), with the human response to it.
4. **H3027H "hand: power"** (510 verses), and signpost #1893.
5. **The title verses** (3,118 verses where M72 is only king, official or divine title). Reading these needs a filter first, as the delight-and-pleasure pairing filter did for M18. Example: pair each title with the act word next to it, then keep the verses where the act is an inner-being act.
6. **The M47 check** (238 verses), under #1979.

## 8. Note on the data

95 verse references in single-chapter books have no chapter in `verse.reference` (for example "Jude 6", "2Jo 5", "Obd 3", "Phile 6"; the `osisId` is `Jude.1.6`). The crossref v3 parser fails on that form. These references were written as "Jude 1:6" etc. for the narrative check only; the hits CSV keeps the DB form.
