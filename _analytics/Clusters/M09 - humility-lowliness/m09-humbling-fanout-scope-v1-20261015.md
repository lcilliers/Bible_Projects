# M09 fan-out: humbling oneself, scope and reading plan

**Date:** 2026-10-15 · **Escalation:** #2148 · **Status:** scoped and pulled. No verse is read yet for the fan-out.

**Decision (researcher, chat 2026-10-15).** The researcher observed: *"It again shows that this cluster can hardly be analysed as a cluster."* Two options were offered: (a) create threads and move to the next cluster, or (b) fan out each thread across clusters. Claude recommended a mix of the two:
- fan out **humbling oneself** now
- turn the **poor and needy** work into threads

The researcher replied, verbatim: *"proceed as suggested"*.

The reasons given for the recommendation:
- Humbling is the inner act the cluster is named for, and the narrative has no section on it.
- Its words are spread across clusters whose own readings would meet humility only at the edges (OT-99, fragmented readings).
- The poor/needy response, by contrast, is the subject of M05, M12, M10 and M46. Threads tied to those clusters will be cleared when they are worked, as was set up for OT-05.

## 1. The verse set

Script: [`m09-humbling-fanout-pull-v1-20261015.py`](m09-humbling-fanout-pull-v1-20261015.py) → [`m09-humbling-fanout-verses-v1-20261015.csv`](m09-humbling-fanout-verses-v1-20261015.csv). The CSV holds each verse's words, tier, other M-codes, narrative chapters and ESV text.

| Measure | Count |
| --- | --- |
| Verses | **218** |
| with an M09 word | 112 |
| from words outside M09 only | 106 |
| already cited in the narrative | 59 |

**The words, in three tiers** (overview v3 §3A, §3C, §3D/3E.1, §5):

| Tier | Rule | Words (cluster, verses) |
| --- | --- | --- |
| whole | every verse of the Strong's | **M09:** H3665 (32), H6035 (21), H8217 (16), G5013 (11), G5011 (8), G5012 (7), H8214 (4), G5014 (4), G5292 (4), H1793A (2), H8215, H6800A, H6800B, H7807, G0036 (1 each). **Outside M09:** G5293 *hypotassō* (M23, 32), H8213 *šāphēl* (M53, 29), G4236 (M05, 7), H6038 (M05, 5), G4239 (M05, 4), G4240 (M05, 4), G0506 (M75, 4), H5223 (M73, 3), H6037 (M05, 2), G4235 (M05, 1), G5226 (T3, 1) |
| surface | only where the surface says humble, lowly, meek, submit or contrite | H6031B *ʿānāh* (M24, 13), H6041 *ʿānî* (M24, 5), H7817 (T3, 4), H1794 and H1792 "contrite" (M10, 1 each), G5391 "humble mind" (M05, 1) |
| joined | a broken/crushed surface in the same verse as heart, spirit or soul, where the heart or spirit is what is broken | H7665 (M24/T3, 7), H5218B (T2, 3), H7115, H2254B, H3512A, H2490A (1 each) |

The "joined" rule is a working aid. Its candidates were checked, and 12 were left out because the broken thing is a kingdom, a horn, bows, a snare, a city wall, plans or winds (listed in the script). One known miss: Psa 38:8 *"I am feeble and crushed; I groan because of the tumult of my heart"*. Its "crushed" is H1794, which is taken by surface only for "contrite". It will be read with batch 3.

The M09 words keep their other senses in the set: H3665 "subdued", H8217 "deeper", G5012 "asceticism", and H6035 in its "poor/afflicted" sense. 23 verses carry "subdue/subjection/deeper". Each is read by its role in its passage (rule 73), not dropped by sense in advance.

## 2. What earlier strands hold inside this set

| Source | In the fan-out | Handling |
| --- | --- | --- |
| OT-103.44 (M02 × M09) | 2Ch 12:7, 2Ch 12:12, 2Ch 32:26, Zep 2:3, plus Rom 13:5 and Job 40:11 | read here. The item was narrowed on 2026-10-15 and closes when the fan-out is read. Luk 14:21 and Psa 10:14 went to OT-105 |
| M72 group D forward to M09 | 2Ch 12:7, Neh 9:24, 1Sa 7:13, 2Sa 8:1, 1Ch 18:1, Psa 106:42 | read here (H3665). Jer 20:13, Psa 82:4 and Job 5:15 (the poor) belong with OT-105 |
| M47 (#1979 check: dropped placements, by word) | 50 verses | the check is made as each batch is read |
| M08 Pride | 30 verses (e.g. Jam 4:6, 1Pe 5:5, Pro 3:34, 11:2, 16:19, 29:23, Isa 2:11–17, Dan 4:37) | read here for the humbling side. Ch 12 *Pride and the lifted-up heart and spirit* is re-read where these touch it |
| The 27 no-other-M-code reading | group A's 7 verses (Mat 23:12, Luk 14:11, Jam 4:10, 2Ch 30:11, 2Sa 6:22, Luk 1:52, Num 12:3) | already read in their passages (`m09-no-other-mcode-reading-v1-20261015.md`). They are carried in, not read again |

The open threads matched on M09 were OT-97 (item 17, superseded, carried by OT-105) and OT-103 (item 44, narrowed).

## 3. Reading plan

The method is the one approved for M64 §2a and M18:
- each verse is read in its passage, with no framework
- the account grows from the readings
- the main inner-being operation is found first, and the pulled word is placed by its role (rule 73; guide `wa-verse-reading-by-role-guide-v1-20261011`)
- God's own acts go to 13.1 (route A), the human inner being to route B, and other verses are data (rule 72)
- every verse gets a recorded decision
- the change of character is recorded for each word (#1919)
- quotes are checked against the ESV in iba.db

The batches follow the word families. A verse goes to the first batch whose words it holds.

| Batch | Words | Verses | Cited | With an M09 word |
| --- | --- | --- | --- | --- |
| 1 | Hebrew humbling and bringing low: H3665, H8213, H8214, H8215, H6031B, H7817 | 79 | 16 | 43 |
| 2 | Hebrew: the humble, lowly, meek; humility: H6035, H6041, H8217, H6800A/B, H7807, H6038, H6037 | 43 | 10 | 34 |
| 3 | Contrite and broken heart or spirit: H1793A, H5223, the joined words, plus Psa 38:8 | 15 | 8 | 1 |
| 4 | Greek humility and meekness: G5011–G5014, G0036, the *praus* family, G5391 | 43 | 14 | 30 |
| 5 | Submission: G5292, G5293, G0506, G5226 | 38 | 11 | 4 |

After the five batches:
- an account of humbling oneself
- the cross-check against M08 Pride, M47 and the narrative
- weaving, on the researcher's instruction

Where the account sits in the narrative is a structure question for then. Group A has no home yet. The options are a Ch 10 sub-chapter (#1961) or sections woven by activity (#1920).

## 4. The poor and needy, now threads

| Thread | Holds | Comes back when |
| --- | --- | --- |
| **OT-105** (#2149) *The poor as seen by another: what it moves* | 127 verses: 93 another person, 34 God. 15 items: M05, M12, M10, M24, M46, M58, M26, M02, M18, 13.1, four joining verses, and the source | a strand works M05, M12, M10, M24, M46, M58 or M26, or 13.1 is worked for God seeing the poor |
| **OT-106** (#2150) *Poor and needy: the poor person's own side* | 48 verses, plus H6041. The researcher's three dimensions are carried as the question. 11 items: M24, M46, M47, H0034, H1800, G4434, H6041, Pro 18:23, 1Sa 18:23, Luk 18:22, and the source | a strand works M24 or M46, or reads poverty joined to the spirit or heart |

Source for both threads: [`m09-poor-needy-split-v1-20261015.csv`](m09-poor-needy-split-v1-20261015.csv) and overview v3 §3B.1, §3G. Neither thread is analysed through to the narrative on its own (OT-05 ruling).
