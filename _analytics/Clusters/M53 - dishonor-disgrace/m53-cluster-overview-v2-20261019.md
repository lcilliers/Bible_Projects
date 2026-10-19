# M53 Dishonor & Disgrace: cluster overview (full), read beside M07

**Date:** 2026-10-19 · **Escalation:** #2171 (the M07 strand) · **Status:** data overview. No verse has been read for M53 as a cluster; M53 A and E are being read with M07 under #2171 (batch 1 done).

**Instructions (researcher, chat 2026-10-19, verbatim):**
- *"I suggest we do the summary of M53 at the same time, with a few of considering if there are parts of M53 and M07 that need to be read together"*
- *"Agreed: read M53 A (taunt, revile) with M07 C (reproach) as one set, and M53 E with M07 D. Keep it under 2171."*
- On v1: *"you did not do a full summary of M53."*

**What v2 adds to v1:** the scan of same-sense words outside M53 (§5), surface variation within each word with its stems (§4), books, the full co-occurrence table, earlier work per group, the narrative word counts and claims (§6), and the within-M53 pairs (§7). §9 (which parts belong with M07) is v1's §6 with the ruling added. v1 is in `archive/`.

**Companion:** the M07 overview, [`m07-cluster-overview-v1-20261019.md`](../M07%20-%20shame-confusion/m07-cluster-overview-v1-20261019.md).

**Source:** read-only against iba.db, same method as the M07 and M08 overviews.
- Pull: [`m53-cluster-overview-pull-v1-20261019.py`](m53-cluster-overview-pull-v1-20261019.py). Extras: [`m53-cluster-overview-extras-v1-20261019.py`](m53-cluster-overview-extras-v1-20261019.py) (groups, earlier-strand coverage, M07 meeting points) and [`m53-cluster-overview-extras-v2-20261019.py`](m53-cluster-overview-extras-v2-20261019.py) (everything v2 adds).
- Hits: [`m53-cluster-hits-v1-20261019.csv`](m53-cluster-hits-v1-20261019.csv) (131 rows). Per Strong's: [`m53-cluster-strongs-v1-20261019.csv`](m53-cluster-strongs-v1-20261019.csv) (23 rows). Other M-codes: [`m53-cluster-mcode-cooccurrence-v1-20261019.csv`](m53-cluster-mcode-cooccurrence-v1-20261019.csv). Verse crossref: [`m53-cluster-verses-crossref-v1-20261019.csv`](m53-cluster-verses-crossref-v1-20261019.csv) (126 rows). M07 meeting points: [`m53-m07-meeting-points-v1-20261019.csv`](m53-m07-meeting-points-v1-20261019.csv) (35 rows).

## 1. The cluster

- **Name:** Dishonor & Disgrace.
- **Definition in `cluster`:** "Dishonor, mutilation, filth, reviling, disgrace".
- **Status:** `t_cluster_assignment_completed`.
- **How the 23 live Strong's came to be tagged** (`cluster_strong.source`):

| Source | Strong's |
| --- | --- |
| heuristic family grouping (2026-09-05) | 20 |
| Claude scan (2026-09-08): H6674 *ṣōʾ* and G4508 *rhyparos* "filthy" | 2 |
| researcher ruling (#1880, item D-R10, 2026-09-28): H2778A *ḥārap̄* "to taunt", moved from M08 with the rationale "Reproach is disgrace" | 1 |

- **Deleted rows:** none.
- Its noun, H2781 *ḥerpāh* "reproach", is in M07. Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.

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
| Verses already cited in the narrative | 31 |
| Verses that are a source in the claims register | 21 |

M53 is a third the size of M07 (385 verses). Two words are over half of it: H2778A *ḥārap̄* (38 verses) and H8213 *šāpēl* (29). Fifteen of the 23 Strong's have three verses or fewer.

**Books:**

| Book | Verses | Book | Verses |
| --- | --- | --- | --- |
| Isa | 28 | 2Ki | 5 |
| Psa | 16 | 1Cor | 4 |
| Pro | 8 | Jam, Job, Eze, 2Sa | 3 each |
| Mar | 7 | Rom, Luk, 1Ti, Zep, Act, Judg, Zec, Rev | 2 each |
| 1Sa | 7 | 12 other books | 1 each |
| 1Pe, Mat | 5 each | | |

Isaiah is high because of H8213 "bring low" (Isa 2, 5, 25, 26) and the Sennacherib account (Isa 37). Mark is the mute spirit and the silencing words.

## 3. The Strong's by gloss

The groups are a reading aid by gloss and surface. They are not a finding or a sub-grouping. "Read earlier" counts the verses in a reading register or triage file of an earlier strand.

| Group | Strong's | Hits | Verses | Cited | In claims register | No other M-code | Read earlier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A taunt, revile | 5 | 58 | 55 | 7 | 1 | 6 | 8 (M08 7, M18 1) |
| B abase, bring low | 1 | 31 | 29 | 16 | 16 | 3 | 29 (M09 29, M08 14) |
| C mute, silence, muzzle | 5 | 23 | 23 | 4 | 2 | 5 | 1 |
| D filth | 7 | 13 | 13 | 3 | 1 | 2 | 1 |
| E mutilation, indecency | 3 | 4 | 4 | 1 | 1 | 0 | 0 |
| F gloss away from the cluster | 2 | 2 | 2 | 0 | 0 | 1 | 0 |

### 3A. Taunt, revile (5 Strong's, 58 hits, 55 verses)

| Strong's | Gloss | Hits | Verses | Surfaces |
| --- | --- | --- | --- | --- |
| H2778A *ḥārap̄* | to taunt | 39 | 38 | mock 6, taunted 6, mocked 4, taunt 3, defied 3, defy 3, taunts 2, insults 2, reproach 2 |
| G3679 *oneidizō* | to revile | 9 | 9 | reviled 2, reproached, insulted, revile, reproach, rebuked, denounce |
| G3058 *loidoreō* | to revile | 4 | 4 | reviled 3, revile 1 |
| H1421 *giddûp̄îm* | reviling | 3 | 3 | revilings 2, reviling 1 |
| G3059 *loidoria* | reviling | 3 | 2 | reviling 2, slander 1 |

Where H2778A falls: Goliath and the giants (1Sa 17; 2Sa 21:21; 23:9; 1Ch 20:7), Sennacherib (2Ki 19; Isa 37; 2Ch 32:17), the psalmists' adversaries (Psa 42:10; 44:16; 55:12; 57:3; 69:9; 74:10, 18; 79:12; 89:51; 102:8; 119:42), Proverbs (14:31; 17:5; 27:11), Nehemiah (6:13), Judges (5:18; 8:15), Zephaniah (2:8, 10), Isa 65:7 and Job 27:6. The Greek: Christ reviled (Mar 15:32; Mat 27:44; 1Pe 2:23), the disciples reviled and blessed (Mat 5:11; Luk 6:22; 1Pe 4:14), not returning reviling (1Pe 3:9; 1Co 4:12), Rom 15:3, Joh 9:28, Act 23:4, 1Ti 5:14, Jam 1:5, Mat 11:20, Mar 16:14.

### 3B. Abase, bring low (1 Strong's, 31 hits, 29 verses)

H8213 *šāpēl*: low 11, brought low 7, humbled 2, lowly 2, down 2. All 29 verses were read in the M09 humbling fan-out (#2148), 14 in M08 (#2156). 16 are claim sources, mostly in 10.14 *The proud brought low, the lowly raised*.

### 3C. Mute, silence, muzzle (5 Strong's, 23 hits, 23 verses)

| Strong's | Gloss | Verses | Surfaces |
| --- | --- | --- | --- |
| G5392 *phimoō* | to muzzle | 8 | silent 2, muzzle 2, speechless, still, silence, silenced |
| H0483 *ʾillēm* | mute | 6 | mute 3, mute man, speechless, silent |
| G0880 *aphōnos* | mute | 4 | speechless, without meaning, silent, mute |
| G0216 *alalos* | mute | 3 | mute 3 |
| H2629 *ḥāsam* | to muzzle | 2 | muzzle, block |

### 3D. Filth (7 Strong's, 13 hits, 13 verses)

| Strong's | Gloss | Verses | Surfaces |
| --- | --- | --- | --- |
| H6675 *ṣōʾāh* | filth | 5 | dung 2 (2Ki 18:27; Isa 36:12), filth 2 (Isa 4:4; Pro 30:12), filthy (Isa 28:8) |
| H6674 *ṣōʾ* | filthy | 2 | filthy (Zec 3:3, 4) |
| G4508 *rhyparos* | filthy | 2 | filthy (Rev 22:11), shabby (Jam 2:2) |
| G4507 *rhyparia*, G4509 *rhypos* | filth | 1 each | filthiness (Jam 1:21), dirt (1Pe 3:21) |
| H5206 *nîḏāh*, H5708 *ʿiddāh* | filth | 1 each | became filthy (Lam 1:8), polluted (Isa 64:6) |

### 3E. Mutilation, indecency (3 Strong's, 4 verses)

G0808 *aschēmosynē* "indecency": "shameless acts" (Rom 1:27), "seen exposed" (Rev 16:15). H4893A *mišḥāt* "marred" (Isa 52:14, the servant). G2699 *katatomē* "those who mutilate the flesh" (Php 3:2).

### 3F. Gloss away

H5356B "cleanness [of teeth]" (Amo 4:6, hunger) and H6477 "the charge was" (1Sa 13:21, the price of sharpening). Data.

## 4. Where the surface varies within one Strong's

This is where the change-of-character reading (#1919) would start. No reading has been done for these, beyond what batch 1 and the trial read.

- **H2778A *ḥārap̄*: the stem changes the direction.** Piel 35 hits: taunting, defying and mocking another. Qal 4 hits: Psa 69:9 and Psa 119:42 ("those who reproach you", "him who taunts me"), Pro 27:11 ("him who reproaches me"), and **Job 27:6, "my heart does not reproach me"**. In Job 27:6 the reproach is the heart's own act on the self (told in Ch 8). And Judg 5:18 (Piel) has the people's own soul as the object: "reproached its soul to death", rendered "risked their lives" (batch 1).
- **H2778A's English** runs from "defy" (Goliath) to "mock" (Sennacherib), "taunt" (the psalms), "insults" (Pro 14:31; 17:5, "insults his Maker"), "reproach" and "shame" (Psa 57:3).
- **G3679 *oneidizō*:** reviling and insulting by people (Mat 5:11; Mar 15:32) versus Jesus who "rebuked them for their unbelief and hardness of heart" (Mar 16:14) and "began to denounce the cities" (Mat 11:20), versus God "who gives generously to all without reproach" (Jam 1:5).
- **H8213 *šāpēl*:** Hiphil 19 (bring low, mostly God's act: 1Sa 2:7; Psa 75:7; 147:6) versus Qal 11 (be low: Isa 2:9, 11, 17; 5:15). Psa 113:6 (Hiphil) is God who "looks far down", literally "makes himself low to see" (13.1 *Lowering himself*).
- **G5392 *phimoō*:** the ox not muzzled (1Co 9:9; 1Ti 5:18) versus Jesus silencing the unclean spirit (Mar 1:25; Luk 4:35) and the sea (Mar 4:39) versus the guest "speechless" (Mat 22:12), the Sadducees "silenced" (Mat 22:34), and doing good to "put to silence the ignorance of foolish people" (1Pe 2:15).
- **G0880 *aphōnos*:** the lamb "silent" before its shearer (Act 8:32, Isa 53:7) versus "mute idols" (1Co 12:2) versus the "speechless donkey" (2Pe 2:16) versus languages "without meaning" (1Co 14:10).
- **H0483 *ʾillēm*:** God "who makes him mute" (Exo 4:11), the psalmist "like a mute man who does not open his mouth" (Psa 38:13), "open your mouth for the mute" (Pro 31:8), "the tongue of the mute sing for joy" (Isa 35:6), the watchmen "silent dogs" (Isa 56:10), and "speechless idols" (Hab 2:18).
- **H6675 *ṣōʾāh*:** the Rabshakeh's taunt about dung (2Ki 18:27; Isa 36:12) versus the filth the Lord washes away (Isa 4:4) and a generation "not washed of their filth" (Pro 30:12).
- **G4508 *rhyparos*:** "the filthy still be filthy" (Rev 22:11) versus "a poor man in shabby clothing" (Jam 2:2).

## 5. Words outside M53 that carry the same sense (gloss and surface scan)

This scan follows the OT-02 lesson (`feedback_strand_pulls_check_t_coded_synonyms`). None of these words is pulled. Particle and pronoun codes, and surface matches that are not the sense ("entrails", "slowly", "dungeon"), are left out.

**Taunt, mock, revile.** The sense is spread across four clusters:

| Strong's | Gloss | Tagged | Verses | Shared with M53 | Cited | Surface |
| --- | --- | --- | --- | --- | --- | --- |
| H2781 *ḥerpāh* | reproach | M07 | 72 | 5 | 15 | taunt 6, taunts 4 (M53's noun) |
| H3887 *lîṣ* | to mock | M08 | 27 | 0 | 15 | scoffer 11, scoffers 3 |
| H3932 *lāʿaḡ* | to mock | M08 | 18 | 1 | 8 | mocks 5, mock 3, jeered 2 |
| G1702 *empaizō* | to mock | M08 | 13 | 0 | 3 | mocked 9 (the mocking of Jesus) |
| G0987 *blasphēmeō* | to blaspheme | M58 | 34 | 0 | 7 | reviled 3, derided 2, railed |
| H1442 *gādap̄* | to blaspheme | M58 | 7 | 3 | 0 | reviled 4 (Sennacherib, with M53) |
| H3933, H3944, H7047, H7048, H8103, H4426, H2049, H3934, H4485 | derision, scorning, mockery | M06 | 1–7 each | 0 | 0–2 | derision, scoffers, mockers |
| G2551 *kakologeō* | to revile | M06 | 4 | 0 | 0 | reviles |
| G3060 *loidoros*, G1703 *empaiktēs*, G1701, G5512 | reviler, mocker, jeering, to sneer | T2 / T3 | 1–2 each | 0 | 0–1 | reviler, scoffers |
| H4912 *māšāl* | proverb | M35 | 39 | 0 | 4 | "taunt" 3 (a taunt-song) |

The M08 mocking words were read in the M08 strand (10.15 *The mock*). The M06 derision words and M58 blaspheming words are not read.

**Silence, muteness (M53 C).** Most of the silence words are in **M33 Rest & Peace** ("Rest, stillness, quiet, peace, calm"):

| Strong's | Gloss | Tagged | Verses | Shared with M53 | Cited |
| --- | --- | --- | --- | --- | --- |
| H2790B *ḥāraš* | be quiet | M33 | 43 | 0 | 6 |
| H2814 *ḥāšāh* | be silent | M33 | 16 | 0 | 5 |
| H1826H *dāmam* | to be silent | M33 | 15 | 0 | 7 |
| G4623 *siōpaō* | be quiet | M33 | 11 | 1 | 3 |
| G4601 *sigaō* | be silent | M33 | 9 | 0 | 1 |
| H2013 *has* | to silence | M33 | 8 | 0 | 2 |
| H0481 *ʾālam* | be dumb | **M14** | 9 | 0 | 2 |
| G2974 *kōphos* | deaf, mute | T2 | 12 | 2 | 1 |
| H1827, H1747, G2270, G1993, G4602, H5535 | silence | M33 | 1–5 each | 0 | 0–3 |
| H4269 *maḥsôm* | muzzle | T2 | 1 | 0 | 1 |

**Filth, uncleanness (M53 D).** Most of these words are in **M10c Defilement** ("Defilement and Impurity"):

| Strong's | Gloss | Tagged | Verses | Shared with M53 | Cited |
| --- | --- | --- | --- | --- | --- |
| H2930A *ṭāmēʾ* | to defile | M10c | 142 | 0 | 5 |
| H2931 *ṭāmēʾ* | unclean | M10c | 78 | 1 | 2 |
| H2932 *ṭumʾāh* | uncleanness | M10c | 31 | 0 | 1 |
| G0169 *akathartos* | unclean | M10c | 30 | 1 | 5 |
| H5079 *niddāh* | impurity | M10c | 24 | 0 | 1 |
| H1351, H2610, G3435, G3436, G4510, G3393, G3394, G0234 | defile, pollute, defilement | M10c | 1–9 each | 0–1 | 0–1 |
| G2840 *koinoō* | to profane | T3 | 11 | 0 | 2 |
| H6569, H1828, H1561, H0830G, H1557, H6627 and others | dung, refuse, excrement | T2 | 1–7 each | 0 | 0–2 |

**Lowly (M53 B).** H8217 *šāpāl* "low" (M09, 16 verses), G5011 *tapeinos* (M09, 8), and H7817 *šāḥaḥ* "to bow" (T3, 21 verses, **8 shared with M53**: "brought low" beside H8213, as in Isa 2:11, 17; 5:15).

**Indecency, exposure (M53 E).** H6172 *ʿerwāh* "nakedness" (T2; "indecent" in Deu 23:14; 24:1), G0809 *aschēmōn* "unpresentable" (T2, 1Co 12:23), G1570 *ekthetos* "exposed" (T2), H1540I *gālāh* "uncover" (T3).

Points that follow from the scan, with no reading done:
- **M53 C is a small part of the silence family.** The M33 silence words above are in 113 verses (M33 as a whole has 773, most of them rest and peace). *ʾālam* "be dumb" is in M14 Deceit & Falsehood.
- **M53 D is a small part of the uncleanness family.** The M10c words above are in 293 verses (M10c as a whole has 319). The dung words are T2.
- **M53 A shares its sense with M08 (mocking, read), M06 (derision, not read) and M58 (blaspheming, not read)**, as well as its own noun in M07.

## 6. Other M-codes in the same verses

109 of the 126 verses hold another M-code:

| M-code | Verses | M-code | Verses |
| --- | --- | --- | --- |
| M22 Praise & Song | 21 | M07 Shame & Confusion | 7 |
| M08 Pride & Arrogance | 21 | M25 Life & Death | 7 |
| M47 Inner Seat | 14 | M15 Knowing & Understanding | 6 |
| M72 Authority & Dominion | 12 | M56 Sin & Guilt | 6 |
| M58 Wickedness | 11 | M11 Turning & Repentance | 6 |
| M65 Speech & Tongue | 11 | M55 Destruction & Ruin | 6 |
| M24 Faintness & Despair | 11 | M16 Wisdom & Folly | 5 |
| M09 Humility & Lowliness | 9 | M12 Righteousness & Integrity | 5 |
| M45 Renewal & Transformation | 8 | M61 Purity & Holiness | 5 |
| M06 Malice & Enmity | 8 | M05, M46, M26, M19, M30 | 4 each |
| M41 Being Heard | 8 | | |

- **M08 (21), M09 (9), M22 (21):** almost all group B ("The haughty looks of man shall be brought low … and the Lord alone will be exalted in that day", Isa 2:11). M22 is the exalt words beside "bring low". Read in M09 and M08.
- **M47 (14):** Isa 51:7 ("the people in whose heart is my law; fear not the reproach of man"), Job 27:6 ("my heart does not reproach me"), Pro 27:11 ("make my heart glad, that I may answer him who reproaches me"), Mar 9:17, 25 (the mute spirit), Jam 1:21, 1Pe 3:21, Pro 16:19, Pro 29:23, Judg 5:18, Isa 4:4, Isa 64:6, Mar 16:14, 1Pe 4:14. These fall under the #1979 check.
- **M65 (11):** the Rabshakeh's and Sennacherib's words, and the silencing words.
- **Open threads:** none name M53 or an M53 Strong's.

**In the narrative now.** 31 verses are cited:

| Chapter | Verses cited |
| --- | --- |
| 10.14 | 19 |
| Ch 12 | 6 |
| 13.1, 10.15 | 5 each |
| Ch 6, 10.6, 10.7 | 3 each |
| 10.10, 10.11, Ch 11, Ch 8, 10.12 | 2 each |
| Ch 5, 10.2, Ch 14, 10.8, Ch 2, 10.4, Ch 4 | 1 each |

- **Sections:** 10.14 *The proud brought low, the lowly raised* and *A lowly and contrite spirit*, 10.7 *Taking the lower place*, 13.1 *Lowering himself* (group B); 10.15 *The mock* (mocking, from M08). There is no section on taunting, reviling, silence or filth.
- **M53 words in the current chapter files:** "brought low" 15 (10.14 has 12), "silence" 15 (10.5 has 6), the mock words about 40 (most in 10.15), "taunt" 10 and "taunts" 3 (spread across Ch 11, Ch 2, 10.1, 10.5, 10.6, 10.10, 10.2, 10.15), "insults" 6, "reviling" 3 (10.6), "mute" 3, "speechless" 2, "filth" 1.
- **Claims with M53 words:** bringing low C-180, C-181, C-203, C-257; mocking C-213, C-222, C-233, C-234, C-241; Habakkuk's taunt C-253 (*māšāl*); "silently" C-95. 21 M53 verses are claim sources, 16 of them group B.

**Verses with no other M-code (17):** 1Sa 17:10; 2Sa 21:21; 1Ch 20:7; Psa 42:10; Joh 9:28; Act 23:4 (group A); Psa 113:6; Isa 25:12; Isa 40:4 (B); Mar 1:25; Act 8:32; Mat 22:34; 1Co 14:10; Deu 25:4 (C); Isa 28:8; Zec 3:3 (D); 1Sa 13:21 (F).

## 7. Within-M53 pairs

Only 5 verses have more than one M53 hit: Psa 89:51 (*ḥārap̄* twice: "with which your enemies mock, O Lord, with which they mock the footsteps of your anointed"), Zep 2:8 (*giddûp̄îm* with *ḥārap̄*: "the taunts of Moab and the revilings of the Ammonites"), 1Pe 3:9 (*loidoria* twice: "Do not repay evil for evil or reviling for reviling"), Isa 5:15 and Isa 26:5 (*šāpēl* twice). The groups never share a verse.

## 8. Earlier work

- There is no pre-reset M53 study in `_analytics/Clusters/archive/stale-20260907/`, and the M53 folder was empty before this pull.
- Group B was read in M09 (#2148) and M08 (#2156).
- Group A: Sennacherib (2Ki 19:22–23; Isa 37:23–24), Judg 5:18, Zep 2:10 and Pro 17:5 were decided in M08; batch 1 of #2171 has now read 18 group A verses in their passages (1Sa 17, 2Ki 19, Isa 37, 2Ch 32, Neh 6:13, Judg 5:18, Judg 8:15, 2Sa 21:21, 23:9, 1Ch 20:7), and the trial read Psa 69:9 and Rom 15:3.

## 9. Which parts of M53 and M07 belong together (decided)

**Decided (researcher, 2026-10-19):** M53 A with M07 C as one set; M53 E with M07 D. Under #2171. The grounds were these:

M53 is not one theme. It holds five groups that meet M07 very unevenly. Of the 126 M53 verses, **28 have an M07 word in the same verse or within three verses of it in the same chapter** (meeting-points CSV): 19 in group A, 4 in B, 3 in C, 1 in D, 1 in E. 7 share a verse with M07.

**A, taunt and revile, with M07's reproach (group C there).**
- **One root, split across two clusters.** The verb *ḥārap̄* "to taunt" (M53, 38 verses) and its noun *ḥerpāh* "reproach" (M07, 72 verses). In the same way, *oneidizō* "to revile" (M53, 9 verses) and *oneidismos* / *oneidos* "reproach" (M07, 6 verses).
- **They sit in the same verses and passages.** Verb and noun share 4 verses and come within three verses of each other in 9: Goliath (1Sa 17:25–26), Psa 44:13–16, Psa 69:6–10, Psa 79:12, Psa 89:50–51, Psa 119:39–42, Zep 2:8–10. Rom 15:3 quotes Psa 69:9 with both Greek words: "The reproaches of those who reproached you fell on me."
- **The same verses also carry M07's shame words.** Psa 44:15 "All day long my disgrace is before me, and shame has covered my face", next to the taunter of 44:16. Psa 69:6–7 "let not those who hope in you be put to shame … dishonor has covered my face", before 69:9. 1Pe 4:14 "if you are insulted for the name of Christ" is two verses from 4:16 "let him not be ashamed". 1Co 4:12 "when reviled, we bless" sits between "we in disrepute" (4:10) and "I do not write these things to make you ashamed" (4:14).
- **Reading A apart from M07 would split one passage across two strands.** Sennacherib's mocking (2Ki 19:23; Isa 37:24) ends in its inhabitants "dismayed and confounded" (2Ki 19:26; Isa 37:27), which are among M07's 8 M72 forwards.

**E, indecency and mutilation (4 verses), with M07's dishonor (group D there).** Rom 1:27 "shameless acts" is one sentence of a passage that also has "the dishonoring of their bodies" (1:24) and "dishonorable passions" (1:26), both M07 (read in the trial). Rev 16:15 "naked and be seen exposed" belongs with the nakedness words, which are T2. Isa 52:14 (the servant "marred") and Php 3:2 have no M07 word near them.

**B, abase and bring low (29 verses), is already read** in M09 and M08 and told in 10.14. It meets M07 in four places, for example "put lower in the presence of a noble" (Pro 25:7) beside "when your neighbor puts you to shame" (25:8) and "lest he who hears you bring shame upon you" (25:10). Only these four meeting points come with the M07 reading.

**C, mute and silence (23 verses), is not part of #2171.** It meets M07 three times only, each a neighbouring verse with another subject: an idol "speechless" (Hab 2:18) two verses from "you will have your fill of shame" (2:16); the muzzled ox (Deu 25:4) next to the brother not to be "degraded" (25:3); Balaam's donkey (2Pe 2:16) near "accursed children" (2:14). Its own family is the silence words of M33 Rest & Peace (§5).

**D, filth (13 verses), is not part of #2171.** It meets M07 once (Isa 4:4, three verses from "take away our reproach", 4:1). Its own family is the uncleanness words of M10c Defilement (§5). One verse carries shame without an M07 word: "therefore she became filthy; all who honored her despise her, for they have seen her nakedness; she herself groans and turns her face away" (Lam 1:8).

**F is data.**

## 10. Points for your direction

1. **A and E are being read under #2171** (batch 1 of 7 done; batch 2 waits on your review of the weaving).
2. **B needs no further reading** beyond its four M07 meeting points.
3. **C (silence) and D (filth) are left open.** The scan (§5) shows each is a small part of a larger family: C of the silence words in M33 Rest & Peace (113 verses), D of the uncleanness words in M10c Defilement (293 verses). Whether they are read when M33 or M10c is taken up, or held now as thread items so that they are not lost, is for you to say.
4. **The derision words (M06) and blaspheming words (M58)** carry the same sense as M53 A and are not read. Whether any are read with set 1 is for you to say.
5. **F is data.**

## 11. Note on the data

- "Within three verses" means the same book and chapter and at most three verses apart. It is a pointer to the passage, not a reading.
- "Read earlier" is a match on the `reference` column of the reading registers, validation registers and triage files in the other cluster folders (not archive). It shows that a strand decided the verse, not that the M53 word was read in it.
- The stem in §4 is the third letter of `verse_lexical.morph_code` for Hebrew (p Piel, q Qal, h Hiphil).
- The narrative counts come from current `narrative_citation` rows; the word counts from the current chapter files, because `narrative_passage` holds only passages that tell a claim; the claims from `narrative_claim` (current).
- The §5 scan matched surfaces as well as glosses. The silence (113) and uncleanness (293) totals are distinct verses for the words listed in those tables, not a pull.
