# Are the stored observations fit for purpose? 1Chr.28.9 and the whole table

Escalation #2538, session 20261121 (Developer Mode), read-only against `iba/app/db/iba.db`. Prompted by the researcher's extract of 1Chr.28.9.
Read first (B:123): `cfg_table.use` and `cfg_column.use`, `expectation` and `filled_by` for `ib_observation` and `ib_node`.
Method: the researcher's join (live node, live observation) counted by observation stage; the wording of up to five observations per stage read in full for the verse; whole-table counts of the empty columns and of the node rules of B:130 and B:131. The wording of other verses' observations was **not** read; counts there are structural only. Every number is from a query run in this session.

## 1. The verse: 55 live observations, 154 live nodes

| stage | observations | nodes | what is filled |
|---|---|---|---|
| lexical, layer-1, layer-2, layer-3 (stages 1 to 4 of the current method) | 23 | 52 | collection_id, role, verse_lexical_id, strong, surface and morph_code on every node; subgroup_id missing on 29 of 52 (the partner words) |
| engagement | 2 | 2 | role and collection filled; subgroup_id and window empty |
| prior-capture | 20 | 87 | role filled; collection_id empty on 3; subgroup_id empty on 83 |
| char-answers, char-reading, verse-reading, strand-reading (the September and October work) | 10 | 13 | role empty on every node; subgroup_id empty on every node; meaning, implication, setting and parts empty on the observations |

`disposition` is empty on every node of every stage on this verse; by its recorded meaning it is set at the claims step, so empty is expected now.

## 2. Opinion on fitness, by group

**Stages 1 to 4 (the thought build): fit in form, with three gaps.**
- Each is a specific statement about this verse's words, with verses and distances named. They are found through `collection_id` on the node.
- Gap A: `subgroup_id` is empty on partner-word nodes (willing, plan, heart, mind, hearts, searches, seek, know). Not established whether that is by design while those collections are ungrouped or an omission; the recorded text of the column is cut off at that point and the rest was not read.
- Gap B: the stage 4 building-block observations (stage value layer-3) carry 827 nodes in the whole table with no verse_reference, verse_lexical_id, strong, surface or collection_id; they are set against another observation through traced_observation_id. B:130 says an in-scope node without a collection is an error and every node has one surface. Whether a traced node is in scope is not stated in the rules read. Observations reached only through such nodes cannot be found by collection.
- Gap C: two layer-3 observations on this verse, 22524 and 22604, say nearly the same thing (the heart or mind stands with the thought in ten verses, naming the same verses); 22342 at layer-2 says it a third time. B:131 forbids the same wording and meaning twice; the exact-text test cannot see this. How many such pairs exist is not measured.
- Smaller: 22594 names an escalation number (#2536) inside the observation text; 22360 says 'positions not stored'. Working notes in findings text.

**The older stages: not fit for purpose for the claims work as they stand.**
- role is empty on all 6,142 verse-reading nodes, 3,869 of 4,002 strand-reading nodes and all char-answers, char-reading and char-subgroup nodes: 12,753 live nodes in all. The claims step reads the role.
- The text of the verse-reading and char-answers observations on this verse is mostly comparison across other verses (5797 lists co-occurring codes M15, M36, M34, M47 bare, against B:100; 7319 and 7320 are about Jer.29.13 and Isa.55.6 and rest on this verse's node for one clause). The evidential weight for this verse is small.
- meaning, implication and setting are empty on all 5,522 verse-reading and 740 char-answers observations.
- B:130 says a live observation has at least one live node: 63 do not (char-answers 43, char-reading 13, char-subgroup 5, verse-reading 2).
- B:130 duplicate nodes, tested as same observation, verse_lexical_id, role, collection, subgroup, surface, strong and morph: 222 groups, 668 rows. None on 1Chr.28.9.
- Duplicate observations by exact text and stage: 19 groups, 38 rows.
- Nodes created since 2026-11-13 with no collection_id: layer-3 827, prior-capture 284, verse-reading 49, char-answers 34, strand-reading 10, char-reading 5.

## 3. The column the researcher's extract filters on

`node.cluster_subgroup_code` is history: written by no process since 2026-11-13 (`cfg_column.use`, #2495). 'M21_asking' is held by 442 live nodes, all of the older stages (Analysis_phase_1 373, prior-capture 63, engagement 4, verse-reading 2). The stage 1 to 4 nodes carry NULL there, so a search by that column finds none of the thought build. The current index is `collection_id` and `subgroup_id`.

## 4. For #2538

The codified process must write, for every node: verse_lexical_id, strong, surface, morph_code, role, collection_id and subgroup_id, and test them at close, so that no later stage repeats Gaps A and B. The older rows need the enhancement pass B:131 describes (the collections read again); that is a design decision, not a fix taken here (B:105).

## 5. Limits

One verse read in full; five observations per stage read for wording; counts elsewhere are structural. Not tested: that any observation's text is founded in its verse, or that the stage 1 to 4 content is correct.
