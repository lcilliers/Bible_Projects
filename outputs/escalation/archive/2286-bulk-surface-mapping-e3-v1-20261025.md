# #2286 prototype step 9: can the surface-to-subgroup mapping be done in bulk before analysis? (E3)

Date: 2026-10-25. Escalation #2286 v20. Read-only measures on live iba.db (0.9 s). This is a view for
the researcher; nothing is built.

## 0. The researcher's answers (v20, verbatim)

> E1 - agree, strongly; E2 - surface to verse is in the verse-lexical table. Cluster to sub group is
> saved in sub group table. surface to subgroup is saved in a new table. E3 - is there any reason why
> the sub group mapping cannot be done prior to Analysis in bulk, similar to what was done for cluster
> work. E4 - this decision is not clear. more exploration is needed for it.

| | state |
|---|---|
| E1 surface is the basis | decided |
| E2 storage: `verse_lexical` (surface to verse), `cluster_subgroup` (cluster to subgroup), a new table (surface to subgroup) | decided in principle. The table design comes to you before any build (B:105). |
| E3 bulk mapping before analysis | this paper |
| E4 the "good, better, well" qualifier group | open, more exploration needed |

## 1. The scale (facts)

| measure | value |
|---|---|
| live M clusters | 80 |
| M-tagged codes | 2,924. **Every code is in exactly one M cluster,** so a surface group never has to cross a cluster. |
| M-coded hits (occurrences) | 64,460, in 24,227 verses |
| distinct (code, surface) pairs to map | **13,411** |
| distinct surfaces | 6,029 |
| hits with no surface | 4 |
| pairs covering 80% / 90% / 95% of the hits | 3,079 / 6,965 / 10,188 |
| pairs with one hit only | 8,101 |
| pairs per cluster | median 129. Largest: M24 Faintness & Despair 582, M23 Strength & Courage 574, M15 Knowing & Understanding 460, M18 454, M47 Inner Seat 393. |
| codes with 10 or more surfaces / with one surface | 338 / 1,042 |

M18, the step 8 trial, is the fourth largest cluster. Its 279 surfaces (454 code-and-surface pairs) took 1 minute 44 seconds on the
system clock, for the pull, the grouping and the comparison. The whole set is about 30 times M18.

**How the cluster work was done in bulk** (`cluster_strong.source`, M clusters): heuristic family
grouping 1,137 codes, old-system migration 1,015, LLM allocation 394, auto-precedent 235, Claude
scan 58. Researcher rulings since then corrected 63 (rulings #1880: 50, and #2163: 13).

## 2. My view: no reason it can't be done in bulk, under five conditions

The data is complete and each code sits in one cluster, so nothing in the data stops a bulk mapping.
Done before analysis, it gives every cluster its segmentation up front. That is what RM-03 asks for,
and it is what the paths in step 3 need (cluster to subgroup to verses, and verse back to subgroup).
The cluster work shows the pattern: a bulk first pass, then corrections by ruling.

**The conditions** (inferential, from steps 7 and 8):

1. **Mapped per cluster, in the session, and recorded with reasons.** About 13,400 pairs at the M18
   rate would be 80 cluster passes, not one pass. In M18, many single-hit surfaces were forms or phrases of
   a common one ("desires to", "longed for", "will you"). If the same holds for the other clusters
   (not checked), a first pass can group a pair with its common form, leaving a smaller set that
   needs judgement. LLM allocation was part of the cluster
   work; whether this mapping may use the API is your call, given #2275 (#2268 B3) plans to retire
   the API steps.
2. **Pairs with two senses are flagged, not forced.** Some pairs carry two senses that only the verse
   can separate: "please" on *ṭôb* ("if it pleases the king" is will or favour, not delight), "long"
   as desire or distance. A bulk mapping at the pair level can't settle these. They need an
   "ambiguous" mark, settled per occurrence in the reading. **So the new table would need to allow an
   occurrence-level exception** (a design point for E2).
3. **The mapping is provisional, not a finding** (step 7 D4). A reading may move a pair, with its
   reason. The cluster work needed 63 corrections by ruling, and a surface mapping will need its own.
4. **A size check, and a group for "not this cluster's sense"** (step 7 D3). Step 8 needed S12 for
   distance, collection and matter. Every cluster will need one, named the same way. Large groups
   (M18 S8 "good" had 364 hits) need a rule for when to split.
5. **It follows cluster changes.** When a code moves cluster (`strongs_reassigned`, B:66), its pairs'
   subgroups must be redone. This would sit with #2281 (#2268 B9, the cluster status lifecycle).

**Where it sits in the programme** (governance.programme_stages): you've said the base data layer is
complete. A bulk surface mapping is preparation that happens before analysis but after base data. It
would be a new step with its own config and rules, built through the app (governance.project_change_rule).

## 3. For your decision

| # | point | your answer |
|---|---|---|
| E3a | bulk mapping before analysis, under conditions 1 to 5 | |
| E3b | made in the session, cluster by cluster, or with an API pass first | |
| E3c | before the bulk run, trial two more clusters of different kinds, for example a small one and M47 Inner Seat (the seat words heart, soul, spirit), to test the conditions | |
| E4 | still open: the qualifier group ("good, better, well"), for more exploration | |
