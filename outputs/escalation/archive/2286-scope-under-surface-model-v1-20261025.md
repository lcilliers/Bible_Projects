# #2286 prototype step 11: the scope under the surface and subgroup model, and the queries re-analysed

Date: 2026-10-25. Escalation #2286 v29. Read-only measures on live iba.db. This is a view for
discussion, not a design: nothing is built.

## 0. The question (v29, verbatim)

> before proceeding to build the surface table and sub groups, I want to revisit the scope thinking.
> analysis process entry point is defined by the verse collection that is discoverable through the
> surface table and sub group. The question is then what is the scope. The scope is a sub group
> verses, or a subset of verses. however, if a verse of collection of verses is selected, the query
> through surface table will present multiple sub groups in most cases. Does it matter? Is that not
> exactly what we want to analyse, is the multiplicity of the context of the verse? The queries
> earlier designed need to be re-analysed for implications

## 1. The model as ruled

| link | held in |
|---|---|
| verse to occurrence (code, surface, position) | `verse_lexical` |
| occurrence (code, surface) to subgroup, with the two-sense flag | `surface_subgroup` (new) |
| subgroup to cluster | `cluster_subgroup` |
| a T-coded word | no subgroup. It is context in the verse (T-b), unless a reading adds it to a cluster (T-a, rule 70 as amended). |

## 2. How many subgroups a verse brings (facts)

Surface subgroups don't exist yet, so this counts M clusters per verse. A verse has at least as
many subgroups as it has clusters.

| | verses | 1 cluster | 2 | 3 | 4 | 5 | 6 or more |
|---|---|---|---|---|---|---|---|
| all verses with an M-coded word | 24,227 | 8,466 (35%) | 7,182 | 4,702 | 2,296 | 989 | 592 |
| M18's verses | 1,370 | 190 (14%) | 330 | 400 | 231 | 126 | 93 |

Across the whole Bible the median verse holds 2 M clusters, and the most any verse holds is 10. M18's
verses run higher, with a median of 3. **So yes: almost any verse selection brings several subgroups.**

The M18 ledger met this and handled it by hand. Before its own groups, it did read-backs of the
verses it shares with M47 (208), M25 (89), M02 (51) and later M72 (182). 1,177 of its 1,370 verses
hold another M cluster (step 6).

## 3. My view: the multiplicity is what we want to analyse, and it brings three requirements

This is my reading (inferential), set against the rules already in force.

**It is the method, not a side effect.** RM-01 says the inner being is a web of interrelated activity.
RG-01 says to read outward from the verse: first record everything the verse carries, with where
each finding bears, and answer the scope's question last. RG-05 says to record how the M-coded words
work together. B:116 says the verse is read for what it says. A verse that brings three subgroups is
a verse where three workings of the inner being meet, and that meeting is the finding.

**Three things decide whether it stays workable:**

- **R1. A scope keeps a home.** The objective defines the home of what the scope records (RM-02,
  RO10). The scope is opened for a subgroup, or a set of them: that is its home. The other subgroups
  in its verses are read, and what they show is recorded at their own occurrences, as findings of
  their own subgroup or as relational findings. They are not forced into the home's claims.
- **R2. The multiplicity is read in the scope's verses; it does not grow the verse set.** When a
  verse in the scope brings subgroup X, X is read there. **X's other verses are not pulled in.** They
  become an open item or a candidate scope for X. This is exactly where the step 3 "similar verses"
  queries ran away: 829 verses by shared word and 2,338 by related word, for one verse, Psa 51:10.
- **R3. The record of reading is per occurrence, not per verse.** When a later scope comes to X, it
  gathers what was already recorded on X's occurrences (RM-04, RO3), and it can see which of them were
  never read for X. Every one of the 16,901 `ib_node` rows already carries its code and surface, so a
  node can be placed on its occurrence. This is also the gap behind #2262 ("gap analysis counts any
  observation as read") and B:93 (check by word, not by citation).

## 4. The step 3 queries, re-analysed

| path | step 3 (designed) | under the surface model |
|---|---|---|
| **a) cluster, subgroup, verses** | cluster or subgroup codes, then every verse holding a code | `cluster_subgroup` to `surface_subgroup` (code, surface), joined to `verse_lexical` on code and surface. **The verse set is occurrence-exact:** a code rendered with another subgroup's surface is left out. Flagged pairs come in and carry their flag. |
| **a) thread item** | resolved by its kind; scope items missed (#2287) | An item enters at a cluster (path a), a Strong's code, or a verse (path c). **A Strong's entry can land in several subgroups,** because its surfaces split (step 8: *ṭôb* splits six ways). The entry then lists them. The 296 open scope items (pairings across two clusters) enter by their stored verses (path c), with the target cluster's subgroups named. #2287 stands. |
| **b) word** | word to codes (`word_strong`), then verses | 175 of the 180 registry words occur as a surface. So a word can go **straight to the surface** and from there to its subgroups and verses. That is consistent with E1. The `word_strong` route is a gloss-era route. |
| **c) verse** | four candidate "similar verse" relations; two ran to hundreds or thousands | verse to its occurrences to their subgroups: **the multiplicity, shown, not expanded** (R2). The scope is the selected verses, with each subgroup listed and its occurrences in them. A subgroup's other verses are offered as candidate scopes, not added. c1 to c4 are retired. |
| **d) chapter or block** | live citations to verses | unchanged to the verses, then as c |
| **e) claim** | verse sources to verses; observation sources listed as "not a verse" (#2287) | verse sources as c; observation sources as f |
| **f) observation** | its nodes to verses, then as c | **its nodes to their occurrences to their subgroups directly**, since a node holds code and surface. This is more exact than going through the whole verse. |

**What changes in the output JSON:**
- Today it lists verses and their routes. Under this model, each verse lists its occurrences: code,
  surface, subgroup, cluster, the two-sense flag, and whether the occurrence is in the scope's home.
- T-coded occurrences are listed as context, with no subgroup.
- A summary per subgroup gives its occurrences in the scope and its total verses, as candidate scopes.
- The resolver as built (`iba/app/lib/versescope.py`) returns verses only, so it would be rebuilt on
  this shape.

## 5. Questions

| # | question | your answer |
|---|---|---|
| S1 | Does every scope have a home: the subgroup or subgroups it is opened for, with the other subgroups in its verses read and recorded at their own occurrences? (R1) | |
| S2 | Does the multiplicity stay within the scope's verses, with another subgroup's other verses becoming an open item or candidate scope, never an expansion? (R2) | |
| S3 | Is the record of reading kept per occurrence, so that a later scope gathers instead of rereading? (R3) | |
| S4 | Path b: does a word enter through the surface, or through `word_strong`? | |
| S5 | When a Strong's entry lands in several subgroups: list them and choose, or take them all as the home? | |
