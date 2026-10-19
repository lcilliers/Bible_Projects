# M53 Dishonor & Disgrace: cluster overview, read beside M07

**Date:** 2026-10-19 · **Escalation:** #2171 (the M07 strand) · **Status:** data overview only. No verse has been read for M53 or M07.

**Instruction (researcher, chat 2026-10-19, verbatim):** *"I suggest we do the summary of M53 at the same time, with a few of considering if there are parts of M53 and M07 that need to be read together"*.

**Companion:** the M07 overview, [`m07-cluster-overview-v1-20261019.md`](../M07%20-%20shame-confusion/m07-cluster-overview-v1-20261019.md). This file follows its shape, and **§6 answers the question asked: which parts of M53 and M07 belong together.**

**Source:** read-only against iba.db, same method as the M07 and M08 overviews (live `cluster_strong` rows, hits from `verse_lexical`, narrative citations and claim sources read live).
- Pull script: [`m53-cluster-overview-pull-v1-20261019.py`](m53-cluster-overview-pull-v1-20261019.py) (the M07 script with the code changed).
- Extras script (gloss groups, surfaces, earlier-strand coverage, M07 meeting points): [`m53-cluster-overview-extras-v1-20261019.py`](m53-cluster-overview-extras-v1-20261019.py).
- Hits: [`m53-cluster-hits-v1-20261019.csv`](m53-cluster-hits-v1-20261019.csv) (131 rows). Per Strong's: [`m53-cluster-strongs-v1-20261019.csv`](m53-cluster-strongs-v1-20261019.csv) (23 rows). Other M-codes: [`m53-cluster-mcode-cooccurrence-v1-20261019.csv`](m53-cluster-mcode-cooccurrence-v1-20261019.csv). Verse crossref: [`m53-cluster-verses-crossref-v1-20261019.csv`](m53-cluster-verses-crossref-v1-20261019.csv) (126 rows).
- **M07 meeting points:** [`m53-m07-meeting-points-v1-20261019.csv`](m53-m07-meeting-points-v1-20261019.csv). Every M53 verse with an M07 hit in the same verse or within three verses of it in the same chapter (35 rows).

## 1. The cluster

- **Name:** Dishonor & Disgrace.
- **Definition in `cluster`:** "Dishonor, mutilation, filth, reviling, disgrace".
- **Status:** `t_cluster_assignment_completed`.
- **How the 23 live Strong's came to be tagged:** heuristic family grouping (2026-09-05) 20; Claude scan (2026-09-08) 2 (H6674, G4508 "filthy"); researcher ruling 1 (H2778A, below).
- **H2778A *ḥārap̄* "to taunt"** was moved from M08 to M53 on 2026-09-28 in the M47 re-allocation (#1880, item D-R10), with the rationale "Reproach is disgrace". Its noun, H2781 *ḥerpāh* "reproach", is in M07.
- **Deleted rows:** none.
- Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.

## 2. Scale

| Measure | Count |
| --- | --- |
| M53 Strong's (live), all with hits | 23 (12 Hebrew, 11 Greek) |
| M53 hits | 131 |
| Verses | 126 (OT 89, NT 37) |
| Books | 34 |
| Verses with more than one M53 hit | 5 |
| Verses that also hold another M-code | 109 |
| Verses with no other M-code | 17 |
| Verses already cited in the narrative | 31 (10.14 holds 19) |
| Verses that are a source in the claims register | 21 |

M53 is a third the size of M07 (385 verses). Two words are over half of it: H2778A *ḥārap̄* (38 verses) and H8213 *šāpēl* (29).

**Books:** Isa 28, Psa 16, Pro 8, Mar 7, 1Sa 7, 2Ki 5, 1Pe 5, Mat 5, 1Cor 4.

## 3. The Strong's by gloss

The groups are a reading aid by gloss and surface. They are not a finding or a sub-grouping. "Read earlier" counts the verses that appear in a reading register or triage file of an earlier strand.

| Group | Strong's | Hits | Verses | Cited | In claims register | Read earlier |
| --- | --- | --- | --- | --- | --- | --- |
| A taunt, revile | 5 | 58 | 55 | 7 | 1 | 8 (M08 7, M18 1) |
| B abase, bring low | 1 | 31 | 29 | 16 | 16 | 29 (M09 29, M08 14) |
| C mute, silence, muzzle | 5 | 23 | 23 | 4 | 2 | 1 |
| D filth | 7 | 13 | 13 | 3 | 1 | 1 |
| E mutilation, indecency | 3 | 4 | 4 | 1 | 1 | 0 |
| F gloss away from the cluster | 2 | 2 | 2 | 0 | 0 | 0 |

### 3A. Taunt, revile (55 verses)

| Strong's | Gloss | Verses | Surfaces |
| --- | --- | --- | --- |
| H2778A *ḥārap̄* | to taunt | 38 | mock 6, taunted 6, mocked 4, taunt 3, defied 3, defy 3, taunts 2, insults 2, reproach 2 |
| G3679 *oneidizō* | to revile | 9 | reviled, reproached, insulted, revile, reproach, rebuked, denounce |
| G3058 *loidoreō* | to revile | 4 | reviled 3, revile 1 (Joh 9:28; Act 23:4; 1Pe 2:23; 1Co 4:12) |
| H1421 *giddûp̄îm* | reviling | 3 | revilings (Isa 51:7; Zep 2:8), reviling (Isa 43:28) |
| G3059 *loidoria* | reviling | 2 | reviling (1Pe 3:9), slander (1Ti 5:14) |

H2778A covers Goliath, who "defied" the ranks of Israel (1Sa 17:10, 25, 26, 36, 45; also 2Sa 21:21; 23:9; 1Ch 20:7), Sennacherib, who "mocked" the living God (2Ki 19:4, 16, 22, 23; Isa 37), the psalmists' adversaries (Psa 42:10; 44:16; 55:12; 74:10, 18; 79:12; 89:51; 102:8; 119:42), and Proverbs: "Whoever oppresses a poor man insults his Maker" (Pro 14:31; 17:5). The Greek covers Christ reviled (Mar 15:32; Mat 27:44; 1Pe 2:23), the disciples reviled and blessed (Mat 5:11; Luk 6:22; 1Pe 4:14), and the command not to return reviling (1Pe 3:9; 1Co 4:12).

### 3B. Abase, bring low (29 verses)

H8213 *šāpēl*: low 11, brought low 7, humbled 2, lowly 2. All 29 verses were read in the M09 humbling fan-out (#2148), and 14 of them in M08 (#2156). 16 are claim sources, mostly in 10.14 *The proud brought low, the lowly raised*. This group is already in the narrative.

### 3C. Mute, silence, muzzle (23 verses)

G5392 *phimoō* "to muzzle" (8: the ox, 1Co 9:9; 1Ti 5:18; Jesus silencing the spirit and the sea, Mar 1:25; 4:39; the guest "speechless", Mat 22:12), H0483 *ʾillēm* "mute" (6: Exo 4:11; Psa 38:13; Isa 35:6; 56:10; Pro 31:8; Hab 2:18), G0880 *aphōnos* (4), G0216 *alalos* "mute" (3, the mute spirit in Mar 7 and 9), H2629 *ḥāsam* (2). One verse was read earlier.

### 3D. Filth (13 verses)

The filthy garments of Joshua the high priest (Zec 3:3–4), "the filth of the daughters of Zion" (Isa 4:4), "all our righteous deeds are like a polluted garment" (Isa 64:6), "those who are clean in their own eyes but are not washed of their filth" (Pro 30:12), "therefore she became filthy" (Lam 1:8), "put away all filthiness" (Jam 1:21), "not as a removal of dirt from the body" (1Pe 3:21), the "shabby" clothing of Jam 2:2, the Rabshakeh's taunt about dung (2Ki 18:27; Isa 36:12), and Rev 22:11.

### 3E. Mutilation, indecency (4 verses)

G0808 *aschēmosynē*: "shameless acts" (Rom 1:27) and "seen exposed" (Rev 16:15). H4893A *mišḥāt* "marred" (Isa 52:14, the servant). G2699 *katatomē* "those who mutilate the flesh" (Php 3:2).

### 3F. Gloss away

H5356B "cleanness [of teeth]" (Amo 4:6) and H6477 "the charge was" (1Sa 13:21). Data.

## 4. Other M-codes in the same verses

109 of the 126 verses hold another M-code. The largest: M08 Pride 21, M22 Praise 21, M47 Inner Seat 14, M72 Authority 12, M58 Wickedness 11, M24 Faintness 11, M65 Speech 11, M09 Humility 9, M41 Being Heard 8, M06 Malice 8, M45 Renewal 8, M25 Life & Death 7, **M07 Shame 7**.

- **M08 (21) and M09 (9)** are almost all group B, already read.
- **M47 (14):** Isa 51:7 "the people in whose heart is my law; fear not the reproach of man", Job 27:6 "my heart does not reproach me", Pro 27:11 "make my heart glad, that I may answer him who reproaches me", Mar 9:17, 25 (the mute spirit), Jam 1:21, 1Pe 3:21 and others. These fall under the #1979 check.
- **M65 Speech (11):** the taunts of Sennacherib and the Rabshakeh, and the silencing words.
- **No open thread names M53 or an M53 Strong's** apart from what the earlier strands read.

**In the narrative now.** 31 verses are cited: 10.14 19, Ch 12 6, 13.1 5, 10.15 5, then 1 to 3 each in Ch 6, 10.6, 10.7, Ch 8, Ch 11, 10.10, 10.11, 10.12. Group B is most of it. There is no section on reviling or taunting.

**Verses with no other M-code (17):** Goliath's defiance (1Sa 17:10; 2Sa 21:21; 1Ch 20:7), Psa 42:10 ("my adversaries taunt me … 'Where is your God?'"), Joh 9:28, Act 23:4, Act 8:32, Zec 3:3, Isa 28:8, Isa 40:4, Isa 25:12, Psa 113:6, Mar 1:25, Mat 22:34, 1Co 14:10, Deu 25:4, 1Sa 13:21.

## 5. Earlier work

There is no pre-reset M53 study in `_analytics/Clusters/archive/stale-20260907/`, and the M53 folder was empty before this pull. I did not run a separate scan of same-sense words outside M53 (the OT-02 lesson). The M07 scan (M07 overview §5) already covers the taunt, revile, reproach, despise and contempt words. If C (silence) or D (filth) is taken up, their own scan comes first.

## 6. Which parts of M53 and M07 belong together

M53 is not one theme. It holds five groups that meet M07 very unevenly. Of the 126 M53 verses, **28 have an M07 word in the same verse or within three verses of it in the same chapter** (meeting-points CSV): 19 in group A, 4 in B, 3 in C, 1 in D, 1 in E. 7 share a verse with M07. Group by group:

**A, taunt and revile, belongs with M07's reproach (group C there). Recommended: read them as one set.**
- **One root, split across two clusters.** The verb *ḥārap̄* "to taunt" (M53, 38 verses) and its noun *ḥerpāh* "reproach" (M07, 72 verses). In the same way, *oneidizō* "to revile" (M53, 9 verses) and *oneidismos* / *oneidos* "reproach" (M07, 6 verses).
- **They sit in the same verses and passages.** Verb and noun share 4 verses and come within three verses of each other in 9: Goliath (1Sa 17:25–26), Psa 44:13–16, Psa 69:6–10, Psa 79:12, Psa 89:50–51, Psa 119:39–42, Zep 2:8–10. Rom 15:3 quotes Psa 69:9 with both Greek words: "The reproaches of those who reproached you fell on me."
- **The same verses also carry M07's shame words.** Psa 44:15 "All day long my disgrace is before me, and shame has covered my face", next to the taunter of 44:16. Psa 69:6–7 "let not those who hope in you be put to shame … dishonor has covered my face", before 69:9. 1Pe 4:14 "if you are insulted for the name of Christ" is two verses from 4:16 "let him not be ashamed". 1Co 4:12 "when reviled, we bless" sits between "we in disrepute" (4:10) and "I do not write these things to make you ashamed" (4:14).
- **Reading A apart from M07 would split one passage across two strands.** Sennacherib's mocking (2Ki 19:23; Isa 37:24) ends in its inhabitants "dismayed and confounded" (2Ki 19:26; Isa 37:27), which are among M07's 8 M72 forwards.
- The set would be about 55 (M53 A) + 82 (M07 C) verses, less the overlap, plus the M07 shame verses in the same passages.

**E, indecency and mutilation (4 verses), belongs with M07's dishonor (group D there).** Rom 1:27 "shameless acts" is one sentence of a passage that also has "the dishonoring of their bodies" (1:24) and "dishonorable passions" (1:26), both M07. Rev 16:15 "naked and be seen exposed" belongs with the nakedness words, which are T2 (M07 overview §5). Isa 52:14 (the servant "marred") and Php 3:2 have no M07 word near them.

**B, abase and bring low (29 verses), is already read** in M09 and M08 and told in 10.14. It meets M07 in four places, for example "put lower in the presence of a noble" (Pro 25:7) beside "when your neighbor puts you to shame" (25:8) and "lest he who hears you bring shame upon you" (25:10). Recommended: no re-reading as a group; take the four meeting points with the M07 verses they touch.

**C, mute and silence (23 verses), does not belong with M07.** It meets M07 three times only, each a neighbouring verse with another subject: an idol "speechless" (Hab 2:18) two verses from "you will have your fill of shame" (2:16); the muzzled ox (Deu 25:4) next to the brother not to be "degraded" (25:3); Balaam's donkey (2Pe 2:16) near "accursed children" (2:14). Its own concern is speech, healing and silencing (M65 Speech 11 shared). Recommended: leave it out of the M07 strand.

**D, filth (13 verses), meets M07 once** (Isa 4:4, three verses from "take away our reproach", 4:1). Its concern is cleansing and garments, with M61 Purity and M47. One verse carries shame without an M07 word: "therefore she became filthy; all who honored her despise her, for they have seen her nakedness; she herself groans and turns her face away" (Lam 1:8). Recommended: not as a group. Lam 1:8 can be taken with the nakedness question if the M07 reading goes there.

**F is data.**

## 7. Points for your direction

1. **Read M53 group A (taunt, revile) with M07 group C (reproach) as one set** (§6). Within it, three threads stand out in the data: the defiance of God and his people (Goliath, Sennacherib), reproach suffered by the one who prays (the psalms), and reproach borne for God and by Christ (Psa 69:9; Rom 15:3; Heb 11:26; 13:13; 1Pe 2:23; 4:14). Heb 12:2, "despising the shame", is an M07 verse with G0152.
2. **Take M53 E with M07 group D** (dishonor), chiefly Rom 1:24–27.
3. **Group B is already read**; only its four M07 meeting points come with the M07 reading.
4. **Groups C and D stay out of the M07 strand.** They can be taken up when M65 (silence) or M61 (filth) is read, or on their own.
5. Whether M53's A and E are counted under #2171 or get their own escalation is for you to say. They are recorded under #2171 for now.

## 8. Note on the data

- "Within three verses" means the same book and chapter and at most three verses apart. It is a pointer to the passage, not a reading. 35 rows link 28 M53 verses to 33 M07 verses.
- "Read earlier" in §3 is a match on the `reference` column of the reading registers, validation registers and triage files in the other cluster folders (not archive). It shows that a strand decided the verse, not that the M53 word was read in it.
- The narrative counts come from current `narrative_citation` rows; the claims-register count from `narrative_claim_source.verse_id`.
