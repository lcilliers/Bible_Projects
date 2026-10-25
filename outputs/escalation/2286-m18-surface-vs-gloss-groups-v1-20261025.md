# #2286 prototype step 8: M18 grouped by surface, compared with the gloss groups

Date: 2026-10-25. Escalation #2286 v18. Read-only on live iba.db (`verse_lexical.surface`, the ESV
rendering of each word). Nothing is written to the tables. The pull and grouping scripts are in the
session scratchpad.

## 0. The instruction (v18, verbatim)

> the basis for the subgroup should be the surface not the gloss. can you run M18 as a comparison and
> see what the difference will be

## 1. How it was done, and the time

1. All 1,510 M18 hits (88 codes, 1,370 verses) were pulled with their surface. All of them have one.
   There are 279 distinct surfaces (lower-cased).
2. Each surface was put into a surface group by what the English says. **The 279-to-12 assignment is
   my judgement (inferential).** It is listed in the appendix so you can check it. Three surfaces
   carry two senses and were assigned per code: "long" (G3117 is distance), "eager" (G2207 is zeal,
   H3700 is longing) and "dear".
3. Each hit then sits in the surface group of its own rendering. The groups were compared with the
   overview's gloss groups A to G (`m18-cluster-overview-v1-20261008.md` section 3).

**Time on the system clock:** 14:01:00 to 14:02:44 UTC, so **1 minute 44 seconds**. That covers the
pull, the grouping and the comparison. No API call was made. For comparison, the pipeline method
first needs Stage 1, estimated at $850 (step 5).

## 2. The groups

| surface group | codes | hits | verses |
|---|---|---|---|
| S1 desire, craving, longing, lust | 41 | 253 | 234 |
| S2 delight, pleasure, gladness | 28 | 230 | 222 |
| S3 will, wish, choosing, willingness | 13 | 295 | 275 |
| S4 favour, acceptance, approval | 7 | 52 | 50 |
| S5 jealousy, zeal, envy | 9 | 112 | 97 |
| S6 thirst, hunger | 5 | 45 | 43 |
| S7 precious, costly, valued | 10 | 77 | 75 |
| S8 good, better, well (a quality of something) | 3 | 364 | 344 |
| S9 beauty | 6 | 20 | 19 |
| S10 harm, ruin | 1 | 14 | 14 |
| S11 striving, vanity | 3 | 9 | 9 |
| S12 no desire sense (distance, collection, matter, other) | 16 | 39 | 39 |

The gloss groups, for comparison: A 258 hits, B 640, C 372, D 112, E 45, F 60, G 23.

## 3. Where the two differ

**Where each gloss group's hits go by surface:**

| gloss group | goes to (hits) |
|---|---|
| A desire, craving, longing | S1 194, S2 23, S7 15, **S10 14**, **S11 7**, S12 3, S9 1, S3 1 |
| **B delight, pleasure, pleasant, good** | **S8 364**, S2 185, S3 21, S1 21, S9 19, S4 14, S12 11, S7 4, S11 1 |
| C will, willing, acceptance | S3 273, **S4 38**, S1 38, S2 22, S11 1 |
| D jealousy, zeal | S5 112 (unchanged) |
| E thirst, hunger | S6 45 (unchanged) |
| F precious, costly | S7 58, S12 2 |
| G gloss away from desire | S12 23 (unchanged) |

**What changes:**

1. **Group B comes apart, and that is the main difference.** Its 640 hits go into "good, better,
   well" (S8, 364 hits, 351 of them *ṭôb* H2896A) and "delight, pleasure" (S2, 185), with the rest
   scattered. The ledger had to make this split by hand: the pairing filter, buckets 1 to 3, B1
   delight, B2 pleasant, then the role triage. It then ruled the "good" hits secondary (step 6).
   Surface grouping gives the same split directly, at the start. 204 of the 224 undecided M18 verses
   (step 6) are on *ṭôb*, and 351 of *ṭôb*'s 408 hits are in S8. I have not checked verse by verse
   that the 204 are among them.
2. **Group C splits into will (S3) and favour or acceptance (S4).** S4 is mostly *rāṣôn* H7522
   ("favor, accepted, acceptable"). C also gives 38 hits to desire (S1), where *thelō* G2309 is
   rendered "desire, desiring".
3. **Group A gives up three groups the gloss hid:**
   - **harm** (S10): H1942, glossed "desire", rendered "destruction, calamity, ruin" in 14 of 16 hits.
   - **striving** (S11): H7469, glossed "longing", rendered "striving" in all 7.
   - **precious** (S7): H2532A and H4261.
4. **Groups D, E and G don't change.** For these words the gloss and the surface agree.
5. **Five groups are new by surface:** S4 favour, S8 good, S9 beauty, S10 harm, S11 striving.

**What it means for the unit:**

- **The unit of a surface group is the occurrence, not the code.** 27 of the 88 codes fall into two or
  more surface groups. *ṭôb* H2896A falls into six (good 351, delight 31, beauty 15, favour 7,
  precious 3, will 1), and *thelō* G2309 into three. The subgroup table enforces one code, one
  subgroup (`UNIQUE(strong)` on `cluster_subgroup_strong`), so **it can't hold surface groups as it
  stands.** A surface group is a set of (code, surface) pairs, or of occurrences.
- **Verses in more than one group:** 51 by surface, against 38 by gloss. That is a small rise.
- **Hits moved:** 620 of 1,510 (41%) land in a surface group other than the one their gloss group
  would suggest. 377 of those are *ṭôb*. Leaving *ṭôb* aside, 243 of the remaining 1,102 hits move
  (22%).

## 4. Limits

- **The surface narrows the sense but does not settle it.** "please" on *ṭôb* ("if it pleases the
  king") went to delight (S2), but in the verse it is the king's will or favour. "love" on H2836A
  went to desire (S1). The role in the verse (RG-03) still decides. A surface group is a better
  starting segmentation than a gloss group, but it is still provisional.
- **The grouping of 279 surfaces is a judgement.** Made again, a few small surfaces could fall
  differently. The large ones (good, will, desire, delight, want, precious, jealousy) are not in doubt.

## 5. For your decision

| # | point | your answer |
|---|---|---|
| E1 | adopt surface as the basis for subgroups (step 7 D3, now surface rather than gloss and surface) | |
| E2 | the subgroup unit is the (code, surface) pair or the occurrence, so the one-code-one-subgroup rule goes. Where should surface groups be stored? | |
| E3 | the mapping of surfaces to groups is made in the session and recorded with its reasons, like this appendix | |
| E4 | S8 "good, better, well", the qualifier group: read as its own unit, or left to the primary clusters as the ledger ruling did | |

## Appendix: the surfaces in each group

- **S1:** desire, desires, desired, desiring, desirous, desirable, desires to, yearn for, craving, craves, crave, craved, long, long for, longing, longed, longed for, longs, longingly, yearns, pant, pants, lust, lusts, lustful, lusty, passions, passions draw, sinful desire, flesh, covet, coveted, covets, covetousness, urges, heat, wanton, aspires, aspire, ambition, aim, earnestly, greedy, get, make gain, who gets, carried out, sniffing, hastens, love, heart, had, you, who desire, greatly, shameless, eager (H3700)
- **S2:** delight, delights, delighted, delighting, delight in, great delight, delightful, pleasure, pleasures, good pleasure, pleased, pleased to, well pleased, pleases, please, pleasing, pleasing to, pleasant, pleasantness, pleasant places, glad, merry, cheerful, joyful, happiness, happier, content, cheer, play, bounced, darling, beloved, one beloved, sweet, delicate, delicately bred
- **S3:** will, wills, will you, want, wants, wanted, want to, would (and its forms: you, we, who, I, he, they, anyone would), wish, wishes, wished, wishing, wished to, willing, willing to, unwilling, willingly, refused, refuse, choose, chose, chosen, decided, determined, disposed, well disposed, insisting, preferred, deliberately, let, meant, mean, human will, willfulness, purpose, persisted, undertaken, undertook, like, readiness, ready, eagerness, good will, freely offered, freely offers, offering freely, freewill offerings, vowed willingly, volunteer, moves him, moved him, moved them, offerings, offered, given, made
- **S4:** favor, favors, favorable, favorably, accepted, acceptable, acceptance, enjoy acceptance, gracious, approve, to him
- **S5:** jealousy, jealous, zeal, zealous, zealot, envy, envious, envied, fury, worked, exceedingly, very, eager (G2207)
- **S6:** thirst, thirsty, thirsts, thirsted, suffer thirst, parched ground, hungry
- **S7:** precious, precious things, costly, jewels, jewel, treasures, rare, more rare, most rare, seldom, esteemed, was priced, honor, glory, splendor, choice, choicest, outweighs, dear
- **S8:** good, better, best, well, fine, more, right, upright, blameless, pure, discerning, safe, profitable, bountiful, rich, prospered, prospering, go well, welloff, better off, seems good, suits, best place, word, promise, feast, holiday, searches, much, anointing, and
- **S9:** beautiful, more beautiful, beauty, lovely, attractive, handsome, more handsome
- **S10:** destruction, calamity, ruin, deadly, wicked, mischievous, evil
- **S11:** striving, vain, useless
- **S12:** far, far off, far away, long way, long (G3117), collection, collecting, collected, gathered together, pools, holding, thick, cool, cold, out of trouble, free from anxieties, matter, care, cares, is, any, whatever, did, truly, balak, mocking, ones regret
