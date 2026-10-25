# #2286 prototype step 7: the cluster_subgroup method against the gloss method, a view

Date: 2026-10-25. Escalation #2286 v16. This is a view for the researcher's decision. Nothing is
changed. Everything in sections 2 and 3 is my judgement (inferential); the facts it rests on are cited
from steps 4 to 6.

## 0. The proposal (v16, verbatim)

> I what to propose that the cluster_subgroup method is over engineered for its purpose. The subgroup
> method used in the clusters using the by "gloss" method is more appropriate. What is your view.

## 1. The two methods side by side (facts)

| | cluster_subgroup method (pipeline) | gloss method (M18 ledger) |
|---|---|---|
| what it needs first | Stage 1 verse reading complete for every code (`clusterstatus.py` gate). For M18, a preview estimated about $850 (step 5). | one read-only data pull: gloss, surface, hits and verses per code (`m18-cluster-overview-v1-20261008.md`) |
| how the groups are made | one LLM call over the whole cluster, meaning-based, at most 10 groups | by hand, by gloss, in the overview |
| what it adds | a status lifecycle (cluster and subgroup), then the Stage 3 and Stage 4 API steps per subgroup | none: the groups go straight to reading |
| clusters done | 3 of 80 (step 4) | M18, and others by the same overview shape (M64 #1978) |
| what it leaves in the tables | `cluster_subgroup`, `cluster_subgroup_strong`, and nodes carrying the subgroup code | nothing: the groups exist only in the overview file |
| how the groups were treated | as findings (status `answer_complete`) | "a reading aid by gloss only ... not a finding" |

## 2. My view

**I agree with the proposal on the method.** I'd separate the method from the table.

**Why the gloss method fits the purpose better:**

1. **It comes before the reading, not after it.** The pipeline will only group a cluster once its
   verses have been read. Rule RM-03 asks the reverse: a cluster scope starts from an overview that
   segments it, and the reading follows. The gloss method does that. The pipeline's order is why 77
   clusters have no subgroups and M18 can't get any without the $850 stage first.
2. **It treats the group as provisional, which is right.** A gloss group is a way into the verses, not
   a verdict on meaning. That matches B:89 (a word's meaning is never taken from its tag) and RG-09
   (the face is found per verse). The pipeline marks its groups `answer_complete`, which reads as a
   finding made before the verses were read in the current way.
3. **It is cheap and quick.** M18's overview is dated 2026-10-08 and the first group readings
   2026-10-09, and it needed no API call. (How long the overview itself took is not recorded.) That is the scale a reliable work unit step needs, for any cluster.
4. **It worked in practice.** M18 reached a decision on 1,146 of its 1,370 verses (84%) group by group
   (step 6).

**What the gloss method lacked, and should not be lost:**

1. **The groups were never stored.** Paths a, c and f (step 3) need a query from a cluster to its
   groups, and from a verse back to them. Today that is possible only for the 3 pipeline clusters. A
   gloss group needs a home in the tables. The existing `cluster_subgroup` and
   `cluster_subgroup_strong` tables could hold one: they have a label, a description, an anchor verse
   and a placement note per code. **The over-engineering is in the pipeline around the table, not in
   the table.** Whether to keep the table for gloss groups is a design question for you.
2. **The gloss misleads on some codes, and the overview had to say so.** H2896A *ṭôb* has the gloss
   "pleasant" but is mostly "good / better". H1942 has the gloss "desire" but reads as "destruction /
   ruin". H7469 has the gloss "longing" but reads as "striving". The overview caught these by putting
   the surface beside the gloss (section 4 of the overview, and B:110 surface first). So a gloss group
   should be made from gloss and surface together.
3. **Some groups were too big to work as one unit.** Group B had 640 hits, 408 of them on one code.
   It had to be split during the work (B1 delight, B2 pleasant, then the rest by role). So making the
   groups needs a size check, with a split by surface or role where a group is too large.
4. **The leftover bin.** Group G ("gloss away from desire", 7 codes) was a holding place for codes
   that didn't fit. It is honest, but it shows that a cluster's tags can hold words that belong
   elsewhere (B:70: recorded in an observation, not re-tagged).
5. **What has no carrier.** Step 6 found 41 M18 verses that no other cluster's reading will reach. A
   gloss group's deferred verses need their way back recorded when the group is made.

## 3. What a decision would cover

If you accept the proposal, these are the points a design would need. Each is your call:

| # | point | your answer |
|---|---|---|
| D1 | retire the pipeline method for making subgroups (`cluster.subgroup` and the Stage 1 gate on it) | |
| D2 | store gloss groups in `cluster_subgroup` / `cluster_subgroup_strong`, or somewhere else | |
| D3 | gloss groups are made from gloss **and** surface, with a size check and a split rule | |
| D4 | a gloss group is a provisional reading aid, never a finding: its status says so | |
| D5 | what happens to the 13 existing pipeline subgroups for M49, M67 and M83: keep them as they are, or remake them as gloss groups | |
