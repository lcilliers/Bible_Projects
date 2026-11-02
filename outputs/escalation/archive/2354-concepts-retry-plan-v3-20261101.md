# Concepts retry at surface grain, in layers from both ends: plan v3 (#2354, 2026-11-01)

Nothing is built or written to iba/app/db/iba.db. Counts were read from the live tables today.

## Your instruction (verbatim, recorded on #2354 v5)
"the surfaces that does not fit in must be allocated to 'Not allocated' group so I can inspect it in detail. what worries me is that you want to try and load all 15000 in memory, and that use the same complex inner being assessment to all 15000. if you do the it is layers it should be much better. and do it from both ends: those that can easily be classified as inner being, and those that are clearly not related. We have done this many times over."

## What already exists and is reused before any judgement is made
1. **The layered design of #2344** (outputs/concept-mapping/surface-inner-being-filter-design-v1-20261031.md): assign the obvious at both ends without an LLM, judge only the remainder, and judge per Strong's code, not per inflection. It was never built; this plan builds on it.
2. **Your take-out list, batch 1** (outputs/concept-mapping/surface-take-out-list-v1-20261031.md): 9 words, 26 pairs, "not a characteristic".
3. **The subgroup kinds:** 2,593 pairs sit in not_this_sense subgroups (by their definition not the cluster's sense) and 147 in anomaly subgroups. Together 2,740 pairs are already marked as not fitting.
4. **The clusters:** surface_subgroup holds only the 81 M clusters, and each Strong's code sits in exactly one cluster (0 of 2,948 are in two). The outward T clusters (places, objects, natural world, body parts, calendar, connectives and so on) were already taken out earlier. So the cluster is a free first signal: M85 Other Beings (51 pairs) is a being outright, and the 81 cluster names (Anger & Wrath, Sin & Guilt, Walk & Conduct and so on) say what theme each pair belongs to.
5. **Strong's data:** `strong.stepGloss`, `strong_meaning_tree` and the lexicons, for the Strong's code, not the surface.

## Layers
Each layer works on what the earlier layers left, in batches of about 100 Strong's codes; each batch's result is written to its own file before the next starts, so nothing is held in memory.

**From the "clearly not" end**
- **L1, already decided:** the 26 take-out pairs and the 2,740 not_this_sense and anomaly pairs go to **Not allocated**, each with the layer that put it there.
- **L2, plain outward words:** a short list of outward words (objects, places, ritual acts, kinship, numerals, particles) drafted from the stepGloss of the remaining codes, for your review once, as #2344 proposed. Matches go to Not allocated.

**From the "clearly in" end**
- **L3, by cluster:** you give one kind per cluster where the cluster is single-kind: for example M85 is beings; M56 Sin & Guilt and M12 Righteousness & Integrity are states; M10 Violence & Cruelty is behaviour. That is a table of 81 rows for you to rule on, which I draft. Pairs in an unmixed cluster take its kind with no further assessment.
- **L4, mixed clusters:** a cluster that holds two or three kinds (the case you found) is split by Strong's code from the stepGloss and the pair's recorded `reason`, in batches.

**The remainder, last**
- **L5, the hard cases:** only the codes L1 to L4 left undecided get the full assessment (meaning tree and senses). A code I cannot place goes to **Not allocated** for your inspection, never forced into a kind.

## Labels and the new group
Each pair ends with one of: behaviour, inner being state, being (divine, other spirits, human spirit, angels, Satan and demons, other people; spirit is here, as you ruled), or Not allocated. The result is stored in the new surface-group column on `surface_subgroup` (the Developer Mode step you approved), with the layer that decided it.

## Order of work
1. Developer Mode session: add the surface-group column on `surface_subgroup` (and the three `description` columns of #2355 in the same migration, if you want them).
2. L1 and L2 drafted for your review; the L3 table of 81 clusters for your ruling.
3. L4 and L5 run in batches; each layer's counts reported as it finishes, so you can see how few reach L5.
4. Concepts compiled from the labelled pairs and written over the existing concept tables.

## Not claimed
Every label from L2 onward is my reading of recorded text and is inferential (B:4) until you confirm it. I have not yet counted how many codes will reach L5; that comes from running L1 to L4.
