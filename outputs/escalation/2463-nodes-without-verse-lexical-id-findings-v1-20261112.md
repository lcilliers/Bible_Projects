# #2463 — live nodes with no verse_lexical_id: findings and a plan for approval (v1, 2026-11-12)

Researcher, verbatim (2026-11-12): 'Start with fixing the observations - but you should do it accross the study, because it seems to be an issue accross multiple live nodes that there are no verse-lexical id'

## What I read first (B:123)
- `cfg_table` ib_node: one row per verse, word, cluster, subgroup, question or other thing a finding applies to (#2273).
- `cfg_column` ib_node.verse_lexical_id: "the occurrence the node reads, one verse_lexical row; NULL until #2296 fills it. A node that matches more than one occurrence goes to its cluster's anomaly group (B6)". Filled by reading.record (#2296).
- So a NULL is by design for a node that is not a word node, and a defect for a word node the filling never reached.

## Measured (live database, all live nodes, `deleted = 0`)
- 78,099 live nodes; 14,728 (19%) have no verse_lexical_id.
- By stage (nodes with no id of all live nodes in the stage): prior-capture 14,122 of 52,064; verse-reading 408 of 11,043; strand-reading 128 of 3,992; char-answers 54 of 1,418; char-reading 16 of 429. engagement (7,735), Analysis_phase_1, reading, char-subgroup and engagement-note: none.
- The 14,728 split into two kinds:
  - **No word on the node** (no surface, no strong): about 10,200, nearly all prior-capture (role standalone or empty, cluster only). Verse-level or cluster-level nodes; a NULL here may be correct.
  - **Word nodes** (surface and strong present): about 4,500 (prior-capture 3,900; older stages about 600). These are the ones the extract loses.
- 1,545 live observations have live nodes and none of them has an id, so such an observation can never reach a claim through the collection extract.
- Resolvability test for the word nodes: matching on verse and Strong's code gives 2 or more verse_lexical rows for every one of them (3,698 give 2, 572 give 3, 215 give 4, 20 give 5 or 6), none gives exactly 1. So verse plus code alone does not identify the occurrence; surface (and position) would have to decide. Not yet tested.

## What I have not done
Nothing is changed. No fill was attempted.

## Proposed plan (needs your approval; the matching rule is a new decision, B:44, B:105)
1. Split the 14,728 by kind (word node, non-word node) and record the split.
2. For the word nodes, test a match rule read-only: verse, code and surface (and word order where the node carries it) against the live verse_lexical rows; report how many resolve to exactly one, to several, to none, by stage.
3. Bring you the result with options for the remainder: where several match, the cluster anomaly group the column's own text names (B6); where none match, a finding per row.
4. On your approval of the rule: fill the ids through the app (a Claude-written script registered in cfg_*, run through the IBA tool, with a snapshot first and every change recorded in ib_observation_change), then rerun the verse extract for Pro 20:27 and the collection extract to show the effect.
5. Decide separately whether the non-word nodes need an id (probably not; they carry a verse reference).

Decision for you: approve steps 1-3 (read-only measurement and the match test, nothing written). Step 4 returns to you with the rule before anything is written.
