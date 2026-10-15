# M09 Humility & Lowliness: cluster overview (strand start)

**Date:** 2026-10-15 · **Escalation:** #2148 · **Status:** data overview only. No verse has been read for M09.

**Instruction (researcher, chat 2026-10-15, verbatim):** *"starting a new cluster M09.  add a new escalation, prepare a summary of M09 cluster"*.

**Source:** read-only against iba.db, in the same shape as the M72 overview (#1998) and the M18 overview (#1993). It uses live `cluster_strong` rows only and hits from `verse_lexical`. The "other" side is every other M-cluster. There is one change from M72: narrative citations and claims-register sources are read live from `narrative_citation` and `narrative_claim_source` (#2110), not parsed from the chapter files. So single-chapter books (Jude, Phile, etc.) cause no parsing gap.
- Script: [`m09-cluster-overview-pull-v1-20261015.py`](m09-cluster-overview-pull-v1-20261015.py). This is the M72 script with the code changed and the narrative cross-reference added.
- All hits: [`m09-cluster-hits-v1-20261015.csv`](m09-cluster-hits-v1-20261015.csv) (304 rows).
- Per Strong's, with the tag source: [`m09-cluster-strongs-v1-20261015.csv`](m09-cluster-strongs-v1-20261015.csv) (26 rows).
- Other M-codes in the same verses: [`m09-cluster-mcode-cooccurrence-v1-20261015.csv`](m09-cluster-mcode-cooccurrence-v1-20261015.csv).
- Every M09 verse with its M09 Strong's, its narrative places, whether it is in the claims register, and its other M-codes: [`m09-cluster-verses-crossref-v1-20261015.csv`](m09-cluster-verses-crossref-v1-20261015.csv) (273 rows).

## 1. The cluster

- **Name:** Humility & Lowliness.
- **Definition in `cluster`:** "Humility, lowliness, meekness, contrition, being needy/poor".
- **Status:** `t_cluster_assignment_completed`.
- **How the 26 live Strong's came to be tagged** (`cluster_strong.source`):

| Source | Strong's |
| --- | --- |
| heuristic family grouping (2026-09-05), family "humility-lowliness-contrition" | 11 |
| old-system migration | 10 |
| LLM allocation v1.3 (H8214, H7807, G0036) | 3 |
| researcher ruling #1880 (2026-09-28): H1793A *dakkāʾ* "contrite", moved from M11 | 1 |
| auto-precedent: H8215 | 1 |

- **Deleted rows (8):**
  - Four Strong's left M09 earlier:
    - G1299 "to direct", now T3
    - G5549 and H4102 "to delay", now T3
    - H5081G "noble: willing", now M64
  - Four are superseded duplicates of rows that are still live: H0034, H1800, H7326 and H1793A. Under #1880 (D-R6) "needy/poor" stays in M09 by design, because the cluster's own definition names it.
- Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.

## 2. Scale

| Measure | Count |
| --- | --- |
| M09 Strong's (live), all with hits | 26 (16 Hebrew, 10 Greek) |
| M09 hits (distinct verse · position · Strong's) | 304 |
| Verses | 273 (OT 202, NT 71) |
| Books | 42 |
| Verses with more than one M09 hit | 29 |
| Verses that also hold another M-code | 246 |
| Verses with no other M-code | 27 |
| Verses already cited in the narrative | 51 |
| Verses that are a source in the claims register | 4 (Luk 16:22, Psa 34:18, 2Ch 7:14, Phili 2:8) |

M09 is small. It is about a fifth of M18 (1,370 verses) and a fourteenth of M72 (3,972).

**Books with the most M09 verses:**

| Book | Verses |
| --- | --- |
| Psa | 44 |
| Pro | 37 |
| Job | 15 |
| Luk | 15 |
| 2Ch | 13 |
| Lev | 12 |
| Isa | 11 |
| Eze | 9 |
| 2Cor | 8 |
| Mat | 8 |
| Jam | 8 |
| Amo | 7 |
| 2Sa | 7 |

The cluster is centred on the wisdom books and the Psalms. 2Ch is mostly the "humbled himself" accounts of the kings.

## 3. The Strong's by gloss

These groups are a reading aid by gloss only. They are not a finding, and they are not a sub-grouping of the cluster.

| Gloss group | Strong's | Hits | Verses | Cited | No other M-code |
| --- | --- | --- | --- | --- | --- |
| A. humble, lowly, humility (the humbling words) | 12 | 95 | 86 | 20 | 8 |
| B. poor, needy, destitute | 10 | 180 | 164 | 22 | 17 |
| C. *ʿānāw*: humble, afflicted, poor, meek (one word across A and B) | 1 | 22 | 21 | 8 | 1 |
| D. contrite | 1 | 2 | 2 | 2 | 0 |
| E. submission | 1 | 4 | 4 | 1 | 1 |
| F. gloss away from the cluster | 1 | 1 | 1 | 0 | 0 |

**Most verses hold one group only:**

| Groups in the verse | Verses |
| --- | --- |
| B only | 160 |
| A only | 85 |
| C only | 17 |
| B and C | 4 |
| A and D (Isa 57:15) | 1 |

The words for being poor make up 59% of the hits. The humbling words make up 31%.

### 3A. Humble, lowly, humility (12 Strong's, 95 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H3665 *kānaʿ* | be humble | 36 | 32 | humbled (12), subdued (10), subdue (4), humbled yourself (3), humble (3) |
| H8217 *šāphāl* | low | 17 | 16 | lowly (7), deeper (4), low (2), abased (2), humble (1) |
| G5013 *tapeinoō* | to humble | 14 | 11 | humbled (4), humbles (4), Humble yourselves (2), made low (1) |
| G5011 *tapeinos* | lowly | 8 | 8 | humble (3), lowly (3), downcast (1), humble estate (1) |
| G5012 *tapeinophrosynē* | humility | 7 | 7 | humility (5), asceticism (2) |
| H8214 *šᵊphal* (Aramaic) | be low | 4 | 4 | humbled (2), humble (1), put down (1) |
| G5014 *tapeinōsis* | lowliness | 4 | 4 | humiliation (2), lowly (1), humble estate (1) |
| 5 others | | 5 | | H6800A "humbly" (Mic 6:8), H6800B "humble", H7807 "lowly", H8215 "lowliest", G0036 "low" (1 each) |

### 3B. Poor, needy, destitute (10 Strong's, 180 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H0034 *ʾebyôn* | needy | 61 | 58 | needy (46), poor (14), needy one (1) |
| H1800 *dal* | poor | 47 | 46 | poor (35), weak (3), poor man (3), needy (2), weakest, haggard |
| G4434 *ptōchos* | poor | 34 | 34 | poor (30), poor man (3), worthless (1) |
| H7326 *rûš* | be poor | 24 | 24 | poor (17), poor man (2), destitute (1) |
| H4134 *mûkh* | be poor | 5 | 5 | becomes poor (4), poor (1) |
| H4542 *miskēn* | poor | 4 | 3 | poor (4) (Ecclesiastes) |
| 4 others | | 5 | | H2489 "helpless" 2; G3993 *penēs* 1 (2Co 9:9); G4433 "became poor" 1 (2Co 8:9); H6199 "destitute" 1 |

The most frequent pair in one verse is "needy" with "poor" (H0034 + H1800, 10 verses).

### 3C. *ʿānāw* (H6035, 22 hits, 21 verses)

Surface: humble (9), afflicted (5), poor (4), meek (4). This one word is rendered on both sides of the cluster's definition. Examples:
- "the meek" (Num 12:3 of Moses; Psa 37:11)
- "the humble" (Pro 3:34; Psa 25:9)
- "the afflicted" (Psa 9:12; 10:12)
- "the poor" (Isa 61:1; Pro 16:19)

### 3D, 3E, 3F

- **D.** H1793A *dakkāʾ* "contrite": Isa 57:15 ("contrite and lowly spirit") and Psa 34:18 ("crushed in spirit"). Both are cited in the narrative.
- **E.** G5292 *hypotagē* "submission": 2Co 9:13, Gal 2:5, 1Ti 2:11, 1Ti 3:4.
- **F.** G3635 *okneō* "to delay": Act 9:38 ("do not delay"). It came in by old-system migration. Its gloss has no bearing on humility.

## 4. Where the surface varies within one Strong's

This is where the change-of-character reading (#1919) would start. No reading has been done.
- **H3665 *kānaʿ*:** "humbled himself" (kings in 2Ch, 1Ki 21:29, 2Ki 22:19) versus "subdued" (nations in Judg, 1Sa 7:13, 2Sa 8:1, 1Ch 18:1, Psa 81:14). It is the same verb for humbling oneself before God and for being brought low by another.
- **H8217 *šāphāl*:** "lowly" (Isa 57:15; Psa 138:6; Pro 29:23) versus "deeper than the skin" (Lev 13 and 14, leprosy, 4 verses) versus "low" of a vine and a kingdom (Eze 17; 29:14–15).
- **G5012 *tapeinophrosynē*:** "humility" (Phili 2:3; Col 3:12; Eph 4:2; 1Pe 5:5; Act 20:19) versus "asceticism" (Col 2:18, 23).
- **H6035 *ʿānāw*:** humble / afflicted / poor / meek, as in §3C.
- **H1800 *dal*:** poor / weak / "haggard" (2Sa 13:4, Amnon).
- **G4434 *ptōchos*:** poor / "worthless" (Gal 4:9, the elementary principles).

## 5. Words outside M09 that carry the same sense (gloss and surface scan)

This scan follows the OT-02 lesson (`feedback_strand_pulls_check_t_coded_synonyms`). Some Strong's carry humility or poverty in their gloss or surface but are tagged to another cluster. None of them is pulled. The table records where they sit.

| Strong's | Gloss | Tagged | Verses | Shared with M09 | Cited | Surface that bears on M09 |
| --- | --- | --- | --- | --- | --- | --- |
| H6041 *ʿānî* | afflicted | M24 | 72 | 32 | 15 | poor (48), humble (5) |
| H6031B *ʿānāh* | to afflict | M24 | 76 | 1 | 22 | humble (5), humbled (4), might humble (3) |
| H6040 *ʿŏnî* | affliction | M24 | 36 | 1 | 10 | (affliction) |
| H8213 *šāphēl* | to abase | M53 | 29 | 6 | 2 | humbled, lowly |
| H7817 *šāḥaḥ* | to bow | T3 | 21 | 0 | 3 | humbled (4) |
| H6038 *ʿănāwāh* | gentleness | M05 | 5 | 1 | 1 | humility (4) |
| H6037 *ʿanwāh* | gentleness | M05 | 2 | 0 | 0 | meekness |
| G4236 / G4240 *praotēs*, *prautēs* | gentleness | M05 | 7 / 4 | 3 / 0 | 3 / 4 | meekness |
| G4239 / G4235 *praus*, *praos* | gentle | M05 | 4 / 1 | 0 / 1 | 1 / 1 | humble, meek (Mat 5:5; 11:29) |
| G5293 *hypotassō* | to subject | M23 | 32 | 2 | 12 | submit, submissive |
| H1792 / H1794 *dākhāʾ*, *dākhāh* | to crush | M10 | 18 / 5 | 3 / 0 | 4 / 2 | contrite |

Points that follow from the scan, with no reading done:
- *ʿānî* (H6041) is the partner of *ʿānāw* and of "poor and needy". It shares 32 verses with M09. This accounts for much of M24's place as M09's largest co-occurring cluster (§6).
- "Humility" as a noun in the OT (Pro 15:33; 18:12; 22:4, H6038) sits in M05, not M09.
- "Meek" and "gentle" in the NT (Mat 5:5; 11:29; Gal 5:23) sit in M05.
- H8213 *šāphēl*, "to bring low", sits in M53. Its 29 verses include 1Sa 2:7, Psa 18:27, Pro 29:23, Isa 2:9–17 and Eze 21:26.

## 6. Other M-codes in the same verses

246 of the 273 verses also hold a word from another M-cluster. Shared verses, top 25:

| M-code | Verses | M-code | Verses |
| --- | --- | --- | --- |
| M24 Faintness & Despair | 47 | M23 Strength & Courage | 17 |
| M47 Inner Seat | 34 | M42 Prayer & Petition | 16 |
| M72 Authority & Dominion | 33 | M50 Grace & Mercy | 16 |
| M46 Wealth & Riches | 30 | M58 Wickedness | 14 |
| M12 Righteousness & Integrity | 28 | M25 Life & Death | 14 |
| M08 Pride & Arrogance | 23 | M05 Kindness & Friendship | 13 |
| M18 Desire & Longing | 23 | M56 Sin & Guilt | 13 |
| M15 Knowing & Understanding | 21 | M41 Being Heard | 12 |
| M65 Speech & Tongue | 20 | M30 Rebellion & Stubbornness | 12 |
| M45 Renewal & Transformation | 19 | M63 Reasoning & Interpretation | 12 |
| M10 Violence & Cruelty | 19 | M03 Grief & Lament | 10 |
| M22 Praise & Song | 18 | M16 Wisdom & Folly | 10 |
| | | M26 Judgment & Condemnation | 10 |

**M08 Pride & Arrogance (23 verses)** holds the paired sayings, for example:
- Jam 4:6, 1Pe 5:5 and Pro 3:34 ("opposes the proud, gives grace to the humble")
- Pro 29:23 and Pro 11:2
- Psa 138:6, Job 5:11 and Job 22:29
- Eze 17:24 and Eze 21:26
- Dan 4:37

The full list is in the crossref CSV. M08 has not been taken as a strand. The narrative already has **Ch 12 *Pride and the lifted-up heart and spirit***.

**What earlier strands already hold for M09:**
- **M18 (23 shared verses), OT-97 item 17 (`cluster:M09`).** Three verses are marked forward to M09: Job 31:16 and Rom 15:26 (group B triage v2) and Mar 14:7 (group C triage v2). The others were decided in the M18 strand. For example, Pro 22:9 was read and Mat 19:21 was carried in 10.6.
- **M02 (6 shared verses), OT-103 item 44 (`cluster:M09`):** Luk 14:21, 2Ch 12:7, 2Ch 12:12, 2Ch 32:26, Zep 2:3 and Psa 10:14. In the 2Ch verses, God's wrath turns when the king humbles himself.
- **M72 (33 shared verses).** The group D forward list (`m72-group-D-forward-v2-20261012.csv`) marks 9 hand verses forward to M09: 2Ch 12:7, Jer 20:13, Psa 82:4, Neh 9:24, 1Sa 7:13, 2Sa 8:1, 1Ch 18:1, Job 5:15 and Psa 106:42. Most of them are H3665 "subdued" or "the needy". Neh 9:24 was already read and woven in M18 group C.
- **M47 (34 shared verses).** Under the #1979 closure, each strand checks its M47 verses for dropped placements, by word and not by citation (OT-09). The earlier M47 assessment lists M09 under "D. Moral condition" (`M47-other-cluster-cooccurrence-assessment-v1-20260927.md`).
- **M25 (14 shared verses).** The life-death overview gives these pairings: to live + low (Isa 57:15), to die + needy (Isa 14:30, Psa 109:16), to die + poor (Luk 16:22).
- **Open threads matched (`Escalation.ps1 -Action Match -Cluster M09 -Strong <26>`):** only OT-97 (item 17) and OT-103 (item 44). No thread names an M09 Strong's or verse directly.

**In the narrative now.** 51 M09 verses are cited. By chapter:

| Chapter | Verses cited |
| --- | --- |
| 10.7 | 12 |
| 10.13 | 10 |
| Ch 11 | 9 |
| 10.6 | 9 |
| Ch 4 | 7 |
| 10.10 | 7 |
| 13.1 | 6 |
| Ch 2 | 5 |
| Ch 6, Ch 14, 10.9, 10.1, 10.5, 10.4 | 2 each |
| Ch 3 | 1 |

There is no section on humility or lowliness. The words appear in passing: "contrite" 16 times, "lowly" 15, "humbled" 15, "humble" 12, "humility" 5, "meekness" 2. A citation is verse-level and does not mean the M09 word was read (#1987). Only 4 M09 verses are sources in the claims register.

**Verses with no other M-code (27).** Unlike the M64 choose verses that were parked (OT-93), these include verses central to the cluster:
- Num 12:3 (Moses very meek)
- Mat 23:12, Luk 14:11 and Jam 4:10 (humble yourself and be exalted)
- Luk 1:52 ("exalted those of humble estate")
- 2Sa 6:22 (David "abased in my own eyes")
- the widow's offering (Mar 12:42; Luk 21:3)

The list is in the crossref CSV (blank `other_mcodes`).

## 7. Within-M09 pairs (verses with more than one M09 hit)

There are 33 unordered pairs in 29 verses:

| Pair | Count |
| --- | --- |
| H0034 + H1800 (needy, poor) | 10 |
| H3665 + H3665 (humble, humble) | 4 |
| G5013 + G5013 | 3 |
| H0034 + H0034 | 3 |
| H1793A + H8217 (contrite, lowly) | 2 |
| H1800 + H6035, H1800 + H7326, H0034 + H6035 | 2 each |

## 8. Earlier M09 work (pre-reset, archived)

The old system produced a full M09 study in June 2026. It holds 134 files in `_analytics/Clusters/archive/stale-20260907/M09-Humility/`: characteristic A–D evidence and tier findings, a findings audit, a VE-lexical extract, and an essay (`wa-m09-humility-essay-v1-20260621`). It predates the 2026-06-25 method reset and is legacy under that reset. It is not used here, and it is noted only so that the investigation it holds is known.

## 9. Points for your direction

M64, M18 and M72 were taken in focused pulls (#1978, #1998). These are the facts that bear on where to start. The choice is yours.

1. **Group A, the humbling words** (12 Strong's, 86 verses), with D (contrite, 2 verses). These words are closest to the inner act the definition names: humbling oneself, a lowly spirit, humility.
2. **Group B, poor and needy** (164 verses). Many of these are likely to name a social condition rather than an inner act. Under rule 73 they would be read by role: the act that moves in the verse (care for the poor, oppression, God hearing the needy), with the poverty word as a qualifier or as the party acted on. This is the M72 question again. B is 59% of the hits.
3. **H6035 *ʿānāw*** (21 verses), which spans A and B, together with its partner H6041 *ʿānî* (M24, 32 shared verses).
4. **The words outside M09** (§5): humility and meekness in M05 (H6038, *praus*), H8213 in M53, contrite in M10. Under #1970 these are not re-tagged. Whether any of them is read with this strand is for you to say.
5. **What earlier strands hold:** the 3 M18 forward marks (OT-97), the 6 M02 verses (OT-103), the 9 M72 group D forward marks, and the 34 M47 verses (#1979 check).
6. **The pride pairing with M08** (23 verses) and Ch 12 *Pride and the lifted-up heart and spirit*.

## 10. Note on the data

- The narrative counts come from `narrative_citation` rows with `last_version IS NULL` in active chapters, which are the current citations. The claims-register count comes from `narrative_claim_source.verse_id`.
- H8217 *šāphāl* includes "and its" (Eze 17:6), a span-surface artefact of the word's position in the verse. It is counted as a hit, as in the DB.
