# M07 Shame & Confusion: cluster overview (strand start)

**Date:** 2026-10-19 · **Escalation:** #2171 · **Status:** data overview only. No verse has been read for M07.

**Instruction (researcher, chat 2026-10-19, verbatim):** *"start a new escalation to analyse M07 cluster. step 1 is prepare an overview of the cluster for my review."*

**Source:** read-only against iba.db, in the same shape as the M08 overview (#2156). It uses live `cluster_strong` rows only and hits from `verse_lexical`. The "other" side is every other M-cluster. Narrative citations and claims-register sources are read live from `narrative_citation` and `narrative_claim_source` (#2110).
- Pull script: [`m07-cluster-overview-pull-v1-20261019.py`](m07-cluster-overview-pull-v1-20261019.py). This is the M08 script with the code changed.
- Extras script (gloss groups, surface splits, the scan of words outside M07, narrative sections and claims): [`m07-cluster-overview-extras-v1-20261019.py`](m07-cluster-overview-extras-v1-20261019.py).
- All hits: [`m07-cluster-hits-v1-20261019.csv`](m07-cluster-hits-v1-20261019.csv) (475 rows).
- Per Strong's, with the tag source: [`m07-cluster-strongs-v1-20261019.csv`](m07-cluster-strongs-v1-20261019.csv) (38 rows).
- Other M-codes in the same verses: [`m07-cluster-mcode-cooccurrence-v1-20261019.csv`](m07-cluster-mcode-cooccurrence-v1-20261019.csv).
- Every M07 verse with its M07 Strong's, its narrative places, whether it is in the claims register, and its other M-codes: [`m07-cluster-verses-crossref-v1-20261019.csv`](m07-cluster-verses-crossref-v1-20261019.csv) (385 rows).

## 1. The cluster

- **Name:** Shame & Confusion.
- **Definition in `cluster`:** "Shame, confusion, disgrace, reproach, dishonor".
- **Status:** `t_cluster_assignment_completed`.
- **How the 38 live Strong's came to be tagged** (`cluster_strong.source`):

| Source | Strong's |
| --- | --- |
| old-system migration | 24 |
| LLM allocation v1.3 | 9 |
| heuristic family grouping (2026-09-05) | 3 |
| Claude scan (2026-09-08): G0820 *atimos* "dishonored" | 1 |
| auto-precedent | 1 |

- **Deleted rows:** none.
- The nine LLM-allocated rows are mostly the **curse** words (group E, §3E). They sit in M07 beside the shame words.
- Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.

## 2. Scale

| Measure | Count |
| --- | --- |
| M07 Strong's (live), all with hits | 38 (19 Hebrew, 19 Greek) |
| M07 hits (distinct verse · position · Strong's) | 475 |
| Verses | 385 (OT 303, NT 82) |
| Books | 56 |
| Verses with more than one M07 hit | 71 |
| Verses that also hold another M-code | 351 |
| Verses with no other M-code | 34 |
| Verses already cited in the narrative | 73 |
| Verses that are a source in the claims register | 26 |

M07 is smaller than M08 (528 verses) and larger than M09 (273). One word, H0954 *bôš* "be ashamed", is 113 of the 385 verses.

**Books with the most M07 verses:**

| Book | Verses |
| --- | --- |
| Psa | 63 |
| Jer | 48 |
| Isa | 33 |
| Pro | 25 |
| Eze | 24 |
| Deu | 14 |
| 1Cor | 13 |
| Rom | 11 |
| Heb | 10 |
| Luk | 9 |
| Job, 1Sa | 8 each |
| Hos | 7 |
| Mic | 6 |

Psalms and the prophets hold over half. Deu is mostly the curse words (the blessing and the curse, Deu 11, 27–30).

## 3. The Strong's by gloss

The groups are a reading aid by gloss and surface. They are not a finding or a sub-grouping.

| Group | Strong's | Hits | Verses | Cited | In claims register | No other M-code |
| --- | --- | --- | --- | --- | --- | --- |
| A be ashamed, put to shame, confounded | 7 | 219 | 172 | 28 | 9 | 11 |
| B shame, disgrace (nouns) | 9 | 79 | 70 | 14 | 6 | 6 |
| C reproach, taunt | 6 | 83 | 82 | 15 | 4 | 11 |
| D dishonor, contempt | 9 | 46 | 45 | 11 | 5 | 4 |
| E curse | 6 | 47 | 46 | 9 | 2 | 4 |
| F gloss away from the cluster | 1 | 1 | 1 | 0 | 0 | 0 |

Most verses fall in one group only: A alone 156, C alone 65, B alone 52, D alone 43, E alone 41. The overlaps are small: A with B 10, C with E 5, A with B and C 4, B with C 4.

### 3A. Be ashamed, put to shame, confounded (7 Strong's, 219 hits, 172 verses)

| Strong's | Gloss | Hits | Verses | Surfaces |
| --- | --- | --- | --- | --- |
| H0954 *bôš* | be ashamed | 126 | 113 | put to shame 57, ashamed 34, shame 10, confounded 5, shamed 5 |
| H3637 *kālam* | be humiliated | 38 | 38 | ashamed 10, confounded 8, blush 3, brought to dishonor 3, shame 3 |
| H2659 *ḥāpēr* | be ashamed | 17 | 17 | disappointed 4, disgraced 3, disgrace 2, shame 2, confounded 2 |
| G2617 *kataischynō* | to dishonor | 13 | 12 | shame 6, put to shame 3, dishonors 2, humiliated 1 |
| G1870 *epaischynomai* | be ashamed of | 11 | 9 | ashamed 11 |
| G1788 *entrepō* | to cause shame | 9 | 9 | respect 6, ashamed 2, shame 1 |
| G0153 *aischynomai* | be ashamed | 5 | 5 | ashamed 4, shame 1 |

The three Hebrew verbs are often stacked: H0954 with H3637 in 21 verses, H0954 with H2659 in 14 (§7).

### 3B. Shame, disgrace: the nouns (9 Strong's, 79 hits, 70 verses)

| Strong's | Gloss | Hits | Verses | Surfaces |
| --- | --- | --- | --- | --- |
| H1322 *bōšet* | shame | 30 | 29 | shame 27 |
| H3639 *kᵊlimmāh* | shame | 30 | 29 | shame 8, dishonor 8, disgrace 7, reproach 4 |
| G0152 *aischynē* | shame | 6 | 6 | shame 5, disgraceful 1 |
| G0150 *aischros* | shameful | 4 | 4 | shameful 3, disgraceful 1 |
| H0955 *bûšāh* | shame | 4 | 4 | shame |
| G1791 *entropē* | shame | 2 | 2 | shame |
| H1317 *bošnāh*, H3640 *kᵊlimmût* | shame | 1 each | 1 each | shame |
| H8218 *šiplāh* | humiliation | 1 | 1 | "utterly" (Isa 32:19) |

### 3C. Reproach, taunt (6 Strong's, 83 hits, 82 verses)

| Strong's | Gloss | Hits | Verses | Surfaces |
| --- | --- | --- | --- | --- |
| H2781 *ḥerpāh* | reproach | 73 | 72 | reproach 27, disgrace 11, taunt 6, scorn 6, shame 4, taunts 4 |
| G3680 *oneidismos* | reproach | 5 | 5 | reproach 3, reproaches 1, disgrace 1 |
| H2617B *ḥeseḏ* | shame | 2 | 2 | disgrace (Lev 20:17), reproach (Pro 14:34) |
| G3681 *oneidos* | disgrace | 1 | 1 | reproach (Luk 1:25) |
| H2616B *ḥāsaḏ* | to shame | 1 | 1 | bring shame |
| G0176 *akatagnōstos* | beyond reproach | 1 | 1 | "cannot be condemned" (Tit 2:8) |

H2781 is the largest word after H0954. Several of its verses have no other M-code and are about reproach being **taken away** (Gen 30:23; Jos 5:9; Luk 1:25 with G3681) or **borne** (Psa 69:9 is shared with M18; Heb 13:13 has no other M-code).

### 3D. Dishonor, contempt (9 Strong's, 46 hits, 45 verses)

| Strong's | Gloss | Hits | Verses | Surfaces |
| --- | --- | --- | --- | --- |
| H7036 *qālôn* | dishonor | 17 | 17 | shame 8, disgrace 4, abuse 2, dishonor 2 |
| G0818 *atimazō* | to dishonor | 7 | 7 | dishonor 3, shamefully 2 |
| G0819 *atimia* | dishonour | 7 | 7 | dishonorable 2, dishonor 2, shame, disgrace |
| H7034 *qālāh* | to dishonor | 6 | 6 | reputation, contempt, lowly, despised, degraded, dishonors (one each) |
| G0820 *atimos* | dishonored | 4 | 4 | without honor 2, disrepute, less honorable |
| G1165 *deigmatizō* | to disgrace | 2 | 2 | "put to shame" (Mat 1:19), "put them to open shame" (Col 2:15) |
| G3856 *paradeigmatizō* | to disgrace | 1 | 1 | contempt (Heb 6:6) |
| H6173 *ʿarvāh* | dishonor | 1 | 1 | dishonor (Ezr 4:14) |
| H7022 *qîqālôn* | disgrace | 1 | 1 | shame |

### 3E. Curse (6 Strong's, 47 hits, 46 verses)

| Strong's | Gloss | Hits | Verses | Surfaces |
| --- | --- | --- | --- | --- |
| H7045 *qᵊlālāh* | curse | 33 | 33 | curse 25, cursing 4, curses 3 |
| G2671 *katara* | curse | 6 | 5 | curse 3, accursed, cursing, cursed |
| H3994 *mᵊʾērāh* | curse | 5 | 5 | curse 4, curses 1 |
| G0685 *ara*, G2652 *katanathema*, H8381 *taʾălāh* | curse | 1 each | 1 each | curses, accursed, curse |

The **verbs** for cursing are not in M07: H0779 *ʾārar* (M06, 52 verses), H7043 *qālal* (T3, 79 verses), G2672 *kataraomai* (M06). So the curse nouns are in M07 and the curse verbs in M06 and T3 (§5).

### 3F. Gloss away

- G0577 *apoballō* "to throw away": "Therefore do not throw away your confidence" (Heb 10:35).

## 4. Where the surface varies within one Strong's

This is where the change-of-character reading (#1919) would start. No reading has been done.

- **H0954 *bôš*: the English "put to shame" is mostly the plain verb.** By stem: Qal 94 hits (put to shame 47, ashamed 30, other 17), Hiphil 29 (put to shame 12, ashamed 3, other 14, including "acts shamefully" and "shame"), Piel 2 ("delayed", Exo 32:1), Hithpael 1 ("ashamed"). The ESV renders the plain (Qal) verb as "put to shame" more often than as "ashamed". So the English does not show whether another party causes the shame; the original stem has to be checked verse by verse.
- **H0954 also names conduct:** the Hiphil participle is "a son who brings shame" (Pro 10:5) and "one who acts shamefully" (Pro 14:35, shared with M02 and M18).
- **H2659 *ḥāpēr*:** "disappointed" (4) beside "disgraced" and "confounded": shame as hope that came to nothing.
- **G1788 *entrepō*:** "respect" (Mat 21:37; Mar 12:6; Luk 18:2, 4; Luk 20:13; Heb 12:9) beside "ashamed" (1Co 4:14; 2Th 3:14) and "shame" (Tit 2:8). One verb names regard for another and being put to shame.
- **H2781 *ḥerpāh*:** reproach suffered (taunt, scorn, byword) versus reproach that one *is* or *becomes* ("become a reproach") versus reproach removed (Gen 30:23; Jos 5:9).
- **H7034 *qālāh*:** six verses, six surfaces: "reputation" (1Sa 18:23), "lowly" (Pro 12:9), "despised" (Isa 3:5), "degraded" (Deu 25:3), "dishonors" (Deu 27:16), "contempt" (Isa 16:14). It is the "lightly esteemed" family.
- **H2617B *ḥeseḏ*:** the homonym of the word for steadfast love, here "disgrace" (Lev 20:17) and "reproach" (Pro 14:34).
- **H3639 *kᵊlimmāh*:** shame, dishonor, disgrace and reproach in near-equal numbers.
- **G1165 *deigmatizō*:** Joseph "unwilling to put her to shame" (Mat 1:19) beside Christ who "put them to open shame" (Col 2:15).

## 5. Words outside M07 that carry the same sense (gloss and surface scan)

This scan follows the OT-02 lesson (`feedback_strand_pulls_check_t_coded_synonyms`). Some Strong's carry shame, reproach, dishonor, contempt, cursing or nakedness in their gloss or surface but are tagged to another cluster. None of them is pulled. The table records where they sit. Particle and pronoun codes (H90xx, H0853, H3588A and others) are left out; they match only because a span surface is attached to the particle.

| Strong's | Gloss | Tagged | Verses | Shared with M07 | Cited | Surface that bears on M07 |
| --- | --- | --- | --- | --- | --- | --- |
| H0779 *ʾārar* | to curse | M06 | 52 | 3 | 4 | cursed (43), curse (16) |
| H7043 *qālal* | to lighten | T3 | 79 | 4 | 11 | cursed (16), curse (15), contempt (4) |
| H0959 *bāzāh* | to despise | M30 | 42 | 1 | 14 | despised (27), despise (6), despises (5) |
| H6172 *ʿerwāh* | nakedness | T2 | 33 | 3 | 2 | nakedness (35) |
| H2778A *ḥārap̄* | to taunt | M53 | 38 | 4 | 5 | taunted (6), taunt (3), insults (2) |
| H3988A *māʾas* | to reject | M30 | 67 | 2 | 23 | despise (10), despised (5) |
| H0423 *ʾālāh* | oath | T2 | 32 | 3 | 4 | curse (11), curses (5) |
| H5006 *nāʾaṣ* | to spurn | M30 | 24 | 0 | 8 | despised (9), despise (3) |
| H6174, H5903, G1131 | naked | T2 | 10–15 each | 1 | 2–4 | naked |
| H6895 *qāḇaḇ* | to curse | M06 | 12 | 0 | 2 | curse (10), cursed (3) |
| H0936, H0937 *bûz* | to despise, contempt | M30, M06 | 11 each | 0, 2 | 4 each | despise, contempt |
| G1848, G2706 | to despise | M30 | 11, 9 | 0, 2 | 1, 2 | despise, contempt |
| G2672 *kataraomai*, G0331 *anathema*, G1944 | to curse, accursed | M06, T2 | 3–6 each | 0–2 | 0 | curse, accursed |
| G5195 *hybrizō* | to mistreat | M06 | 5 | 0 | 0 | shamefully treated (2) |
| G3679 *oneidizō* | to revile | M53 | 9 | 1 | 0 | reproached, insulted |
| G0410, G0423 | irreproachable | T2 | 5, 3 | 0 | 1, 0 | above reproach |
| G0422 *anepaischyntos* | unashamed | T2 | 1 | 0 | 0 | "no need to be ashamed" (2Ti 2:15) |
| G0335 *anaideia* | shamelessness | T2 | 1 | 0 | 0 | (Luk 11:8, "impudence") |
| G4797, H2000, H4103, H3998 | to confound, confusion | T3, T2 | 2–14 each | 0–1 | 0–1 | confusion, confounded |
| H6031B *ʿānāh*, H8213, G5014, H8217 | to afflict, abase, lowliness | M24, M53, M09 | 4–76 | 0–1 | — | humiliated, abased |

**M53 Dishonor & Disgrace** is a separate cluster whose definition overlaps M07's ("Dishonor, mutilation, filth, reviling, disgrace"). It has 23 Strong's and 126 verses, of which only 7 are shared with M07. Its main words are H2778A *ḥārap̄* "to taunt" (the verb of M07's H2781 *ḥerpāh*), H8213 *šāpēl* "to abase", G3679 *oneidizō* "to revile" (the verb of M07's G3680), and the mute, muzzle and filth words. **M71 Glory & Splendor** holds the honour words (G5092 *timē*, G5091 *timaō*; 212 verses), only 4 shared with M07. **The M53 overview, read beside this one, is [`m53-cluster-overview-v2-20261019.md`](../M53%20-%20dishonor-disgrace/m53-cluster-overview-v2-20261019.md); its §9 says which parts of M53 and M07 belong together.**

Points that follow from the scan, with no reading done:
- **The verb and its noun are often in different clusters:** *ḥārap̄* (M53) and *ḥerpāh* (M07); *oneidizō* (M53) and *oneidismos* (M07); *ʾārar* / *qālal* (M06, T3) and *qᵊlālāh* (M07).
- **Despising and contempt** sit in M30 and M06.
- **Nakedness** (*ʿerwāh*, *ʿārôm*, *gymnos*) is T2. Gen 2:25, "naked and were not ashamed", is an M07 verse with no other M-code.
- **The opposite of shame** (unashamed, irreproachable, shamelessness) is T2.

## 6. Other M-codes in the same verses

351 of the 385 verses also hold a word from another M-cluster. Shared verses, top 25:

| M-code | Verses | M-code | Verses |
| --- | --- | --- | --- |
| M72 Authority & Dominion | 40 | M23 Strength & Courage | 23 |
| M24 Faintness & Despair | 37 | M18 Desire & Longing | 20 |
| M06 Malice & Enmity | 37 | M19 Trust & Refuge | 19 |
| M15 Knowing & Understanding | 31 | M43 Prophecy & Vision | 18 |
| M47 Inner Seat | 31 | M56 Sin & Guilt | 18 |
| M45 Renewal & Transformation | 30 | M25 Life & Death | 17 |
| M16 Wisdom & Folly | 29 | M02 Anger & Wrath | 17 |
| M22 Praise & Song | 29 | M03 Grief & Lament | 16 |
| M01 Fear & Awe | 27 | M80 Blessing | 16 |
| M41 Being Heard | 27 | M08 Pride & Arrogance | 15 |
| M65 Speech & Tongue | 27 | M12 Righteousness & Integrity | 15 |
| M58 Wickedness | 25 | M55 Destruction & Ruin | 14 |
| | | M30 Rebellion & Stubbornness | 13 |

M80 Blessing (16) is the curse words beside blessing (Deu 11, 27–30). M19 Trust & Refuge (19) is the pairing of trust and not being put to shame (for example Psa 25:2, 20; 31:1; Rom 5:5 is in the claims register).

**What earlier strands already hold for M07:**
- **M02 (17 shared verses), OT-103 item 25 (`cluster:M07`).** These 17 verses fall across 14 anger faces. The list is the M07 rows of `wa-cluster-M02-mcode-face-combinations-v1-20261005.csv`. This is the only open thread that `Escalation.ps1 -Action Match -Cluster M07 -Strong <38>` finds.
- **M72 group D (8 verses forwarded to M07).** Eze 16:27, Ezr 8:22, Isa 26:11, 2Ki 19:26, Isa 37:27, 1Sa 25:39, Ezr 9:7, Jer 46:24, all with the hand word as a qualifier (`m72-group-D-forward-v2-20261012.csv`). They are not on a thread. Isa 26:11 is already in 13.1 *Jealousy*; Ezr 8:22 is a claim source (C-248, C-252).
- **M72 group B.** Five verses carry an M07 word. Each was decided in the M72 reading (2Co 10:8 read; Col 2:15 and Rom 9:21 to 13.1; Joe 2:17 carried; Pro 17:2 forwarded to M16). None was forwarded to M07.
- **M18 (20 shared verses).** Read or decided in the M18 strand (for example Luk 18:4 carried in 10.12, Mat 1:19 in 10.7 *Willing*, 1Co 14:35 data). None was forwarded to M07.
- **M08 (15 shared verses).** Read in the M08 strand (for example Pro 11:2 "when pride comes, then comes disgrace", Zep 3:11, Isa 3:5, 2Co 7:14 and 9:4 in the boast). Php 3:19 "glory in their shame" was woven this morning (#2160, C-327).
- **M09 (6), M64 (8), M25 (17), M01 (27), M20 (4) shared verses.** These strands read their own words; the M07 word in these verses was not the focus.
- **M47 (31 shared verses).** Under the #1979 closure, each strand checks its M47 verses for dropped placements, by word and not by citation (OT-09).

**In the narrative now.** 73 M07 verses are cited. By chapter:

| Chapter | Verses cited |
| --- | --- |
| 10.7 | 14 |
| 10.14 | 12 |
| Ch 2, 10.6 | 9 each |
| 10.12, 10.13, 13.1 | 8 each |
| Ch 11 | 7 |
| 10.10 | 6 |
| Ch 4, 10.1, 10.2 | 5 each |
| 10.5, Ch 12, 10.15 | 4 each |

A citation is verse-level and does not mean the M07 word was read (#1987).

- **There is no section on shame.** The one section with shame in its heading is **10.3 *Remembering in shame*** (Eze 16:63; 20:43). Shame otherwise appears in passing: 10.7 *Shame at the thing chosen* (Isa 1:29; 65:13), Saul's "to your own shame" (1Sa 20:30) in 10.7, Joseph "unwilling to put her to shame" (Mat 1:19) in 10.7, Ephraim "ashamed and confounded" (Jer 31:19) in 13.1, "some to shame and everlasting contempt" (Dan 12:2) in Ch 2, and *In shame* (Php 3:19) in 10.15.
- **Shame words in the current chapter files:** "shame" and its forms 35 (10.7 has 8), "reproach" 14, "ashamed" 5, "disgrace" 5, "humiliat-" 5, "blush" 3, "dishonor" 3, "confound" 2. "Curse" and its forms appear 41 times, "despise" 53 and "contempt" 25, but most of those carry words outside M07 (§5).
- **Claims on shame in the register:** C-327 (glorying in shame, this morning) and parts of C-155 (reproach after a death) and C-307 (anger at contempt). 26 M07 verses are claim sources.
- Under rule 77 (#2152), when a chapter is touched, its existing claims on shame are reconciled in the same pass.

**Verses with no other M-code (34).** Some of them:
- reproach taken away: Gen 30:23 (Rachel), Jos 5:9 (Gilgal), Luk 1:25 (Elizabeth)
- reproach borne: Heb 13:13 "bear the reproach he endured", Psa 89:41, 45, Psa 109:25
- "naked and were not ashamed" (Gen 2:25)
- "Those who look to him are radiant, and their faces shall never be ashamed" (Psa 34:5)
- Miriam's shame (Num 12:14), Rom 1:26 "dishonorable passions", Eph 5:12, Pro 6:33
- the parable of the tenants, "They will respect my son" (Mat 21:37; Mar 12:6)
- 1Co 4:14 "I do not write these things to make you ashamed"

The list is in the crossref CSV (blank `other_mcodes`).

## 7. Within-M07 pairs (verses with more than one M07 hit)

There are 115 unordered pairs in 71 verses:

| Pair | Count |
| --- | --- |
| H0954 + H3637 (*bôš* with *kālam*: ashamed and confounded) | 21 |
| H0954 + H0954 | 15 |
| H0954 + H2659 (*bôš* with *ḥāpēr*) | 14 |
| H0954 + H3639 (*bôš* with *kᵊlimmāh*) | 9 |
| H1322 + H3639 (two shame nouns) | 7 |
| H2781 + H7045 (reproach with curse) | 5 |
| H0954 + H1322, H0954 + H2781, H2781 + H3639 | 5 each |
| H2659 + H3637 | 4 |

The stacked pairs are the paired cries of the psalms and prophets, "let them be put to shame and confounded" (for example Psa 35:4, 26; 40:14; 70:2). H2781 with H7045 is the prophetic list "a reproach, a byword, a taunt, and a curse" (for example Jer 24:9; 42:18; 44:8, 12).

## 8. Earlier M07 work (pre-reset, archived)

The old system produced an M07 study before the 2026-06-25 method reset. It holds 171 files in `_analytics/Clusters/archive/stale-20260907/M07-Shame/`, including a science extract (`wa-m07-shame-scienceextract-v1_0-20260513.md`). It is legacy under that reset and is not used here. It is noted only so that the investigation it holds is known.

## 9. Points for your direction

These are the facts that bear on where to start. The choice is yours.

1. **Group A, being ashamed** (172 verses, H0954 alone 113). This is closest to the inner act the definition names. The English "put to shame" mostly translates the plain verb (§4), so the stem has to be looked at in each verse. 28 of the 172 are cited.
2. **The nouns, group B** (70 verses), go with A in many verses (§7). A and B could be read together.
3. **Group C, reproach** (82 verses, mostly H2781 *ḥerpāh*). Reproach suffered, reproach one becomes, reproach taken away, reproach borne for God (§4). Its verb *ḥārap̄* "to taunt" is in M53 (38 verses).
4. **Group D, dishonor and contempt** (45 verses). The "lightly esteemed" words (*qālôn*, *qālāh*) and the Greek *atim-* words. The honour words are in M71.
5. **Group E, the curse nouns** (46 verses). Their verbs are in M06 and T3 (§5). Whether the curse is read in this strand at all, or with the curse verbs, is for you to say.
6. **The words outside M07** (§5): the taunt and revile verbs in M53, despising in M30, contempt and the curse verbs in M06, nakedness and "unashamed" in T2. Under #1970 these are not re-tagged. Whether any are read with this strand is for you to say.
7. **What earlier strands hold:** the 17 M02 verses (OT-103.25), the 8 M72 group D forwards, the 31 M47 verses (#1979 check), and the 15 M08 verses already read.
8. **What is in the narrative:** no shame section yet; 10.3 *Remembering in shame* is the nearest.

## 10. Note on the data

- The narrative counts come from `narrative_citation` rows with `last_version IS NULL` in active chapters, which are the current citations. The claims-register count comes from `narrative_claim_source.verse_id`. The word counts in §6 come from the current chapter files, because `narrative_passage` holds only passages that tell a claim.
- The H0954 stem split in §4 comes from `verse_lexical.morph_code` (third letter: q Qal, h Hiphil, p Piel, t Hithpael). It is a pointer for the reading, not a reading.
- The §5 scan matched surfaces as well as glosses. Particle and pronoun codes are excluded from the table, because they carry the surface of the span they are attached to.
