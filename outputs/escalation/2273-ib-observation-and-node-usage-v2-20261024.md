# #2273 How ib_observation and ib_node have been used together (v2)

**Date:** 2026-10-24 · **Escalations:** #2273 (B1), #2274 (B2) · **Status:** inspection for the researcher.
Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"the ib_observation carries the distinct description, the nodes apply
the description to its 'classification'. … you first need to inspect if these missing columns need to be
applied in the nodes. this should also answer your question for a duplicate ib_observation. The same text can
be applied to multiple verses, terms etc. I think I need to inspect how you have been using the combination of
these two tables because I would not be surprised if you got it terribly muddled up"*

Every number below is from the live `iba/app/db/iba.db` on 2026-10-24. The queries are in section 5.

## 1. The model, and the verdict

**The model:**
- An `ib_observation` row is one distinct description.
- Its `ib_node` rows apply that description to what it is about: a verse, a term (strong, surface, morph), a
  cluster, a subgroup, a question, or another observation.
- Anything that can differ from one application to the next belongs on the node, not on the observation.

**The verdict:** the code has not kept to this model. Classification is held on both tables. The node's
`cluster_code` has been used for the reading that wrote it, not for the word's classification. The strand
reading put per-verse facts (parties, setting) on the observation, so one value stands for up to 42 verses. My
design v1 for B2 repeated the mistake: it added face, role, route, home and disposition as observation columns,
and defined a duplicate by verse, strong and cluster, not by the description.

## 2. What the tables hold, by stage

**Nodes per observation:**

| Stage | Observations with nodes | 1 node | 2 to 5 | more than 5 | most |
|---|---|---|---|---|---|
| verse-reading | 9,871 | 9,260 | 561 | 50 | 19 |
| strand-reading | 773 | 109 | 394 | 270 | 42 |
| char-answers | 705 | 296 | 393 | 16 | 12 |
| char-reading | 105 | 51 | 35 | 19 | 36 |
| char-subgroup | 14 | 9 | 5 | 0 | 2 |

Observations with no node: verse-reading 724 (722 withdrawn, 2 draft), char-answers 43, char-reading 13,
char-subgroup 5, all draft. A draft observation with no node applies to nothing.

**Classification held on the observation as well as on its nodes:**

| Stage | Rows | `cluster_code` | `cluster_subgroup_id` | `strong` | `question_code` |
|---|---|---|---|---|---|
| verse-reading | 10,595 | 4,883 | 0 | 10,595 | 10,595 |
| strand-reading | 773 | 773 | 0 | 268 | 0 |
| char-answers | 748 | 748 | 748 | 318 | 748 |
| char-reading | 118 | 118 | 118 | 118 | 0 |
| char-subgroup | 19 | 19 | 0 | 19 | 0 |

The nodes of every stage carry strong, verse, surface and morph. The char stages' nodes also carry the subgroup,
and verse-reading's and char-answers' nodes carry the question. In verse-reading, 82 observations name a strong
that differs from one of their own nodes' strongs.

## 3. Where it is muddled

| # | Muddle | Evidence | Written by |
|---|---|---|---|
| M1 | **`ib_node.cluster_code` means two things.** The code comment says it is "the PASS that cited the occurrence", that is, the reading's cluster, not the word's. In verse-reading, 3,179 nodes carry a cluster the word does not belong to (`cluster_strong`, live). In strand-reading, every node carries the home cluster: 213 nodes are words of another cluster (for example H6974, a T3 word, under M25 at Isa 26:19). The char stages are clean (1,866 of 1,866 match). | `iba/app/lib/recordingpass.py` `record_one_observation` (comment before `_insert_node`), `record_strand_observations` | the API recording pass; the strand reading (#2172) |
| M2 | **Per-verse facts on the observation.** The strand reading writes the October ledger parts (setting, meaning, implication, chain, basis, parties) as observation columns. 632 of its 773 observations apply to more than one verse. 234 of those hold one `parties` value for all their verses: observation 12481 holds "God; priests, Levites, kings, the servant, witnesses" across 32 verses. 145 hold one `setting` across several verses. | `recordingpass.STRAND_PARTS`, `record_strand_observations` | the strand reading (#2172), used by `Reading.ps1 -Step Record` |
| M3 | **Classification copied onto the observation.** `strong`, `question_code`, `cluster_code` and `cluster_subgroup_id` are written on the observation as well as on its nodes. The strand reading sets `strong` only when all nodes share one, and `cluster_code` to the home cluster. | `_insert_observation`, `record_strand_observations` | every stage |
| M4 | **The same description written as several rows.** Live rows with identical text: verse-reading 17 texts on 50 rows (for example "No constitutional level specified." on two rows for two words of Rom 12:8), strand-reading 1 text on 5 rows, char-answers 1 text on 2 rows. Under the model each is one observation with several nodes. | `record_one_observation` decides "same or new" by prose similarity, not by the text | the API recording pass |
| M5 | **Fragments imported as observations.** Nine strand-reading rows are a heading with no content, such as "Already read in unit 1:" (ids 11795, 12064, 12068, 12102, 12105, 12114, 12124, 12125, 12130; runs CATCHUP-2172-B-20261022-anger and -fear). | the #2172 catch-up import | recorded on #2266 |
| M6 | **Design v1 for B2** put face, role, route, home and disposition on the observation, and defined a duplicate by verse, strong and cluster. Both are wrong under the model. | `outputs/escalation/archive/2273-2274-reading-phases-and-observation-record-design-v1-20261024.md` §2 | this session |

The reading process (`iba/app/lib/reading.py`) finds a scope's observations through their nodes (`ib_node.verse_reference`),
which fits the model. Its only writer is `record_strand_observations`, so a reading inherits M1 to M3.

## 4. What this means for B2

Each part of the observation record (`cfg_setting reading.observation_parts`) is placed by asking whether it can
differ from one application of the same description to the next.

| Part | Can it differ between the verses or terms the description applies to? | Belongs on |
|---|---|---|
| role (characteristic, qualifier, standalone) | yes: the role comes from this verse, never the cluster tag (RG-03) | the node |
| route (A, B, C) | yes: per verse and its parties (RG-06) | the node |
| parties (who acts, towards whom, to what effect) | the party's role is itself a description, which may apply to many verses and terms (researcher, 2026-10-24) | an observation, applied by its nodes to every verse and term it affects |
| home (the scope objective it was recorded for) | yes: a description recorded in one reading may be applied by another (RM-02) | the node (it is what M1's "pass" was trying to be) |
| disposition (told, claim, held, data, context, withdrawn) | yes: "where a verse ends up" (R5) | the node |
| face | the face is itself a description (how the word appears here and why it differs) | an observation, applied by its nodes to the occurrences that show it |
| operation | depends on whether it is a controlled value or a description | decision D3 in the design v2 |

A duplicate is then **a second live observation with the same description**. The same text applied to another
verse or term is a new node on the existing observation, never a new row.

## 5. Queries

```sql
-- nodes per observation, by stage
SELECT o.stage, count(*), sum(n=1), sum(n BETWEEN 2 AND 5), sum(n>5), max(n) FROM ib_observation o
JOIN (SELECT observation_id, count(*) n FROM ib_node GROUP BY 1) k ON k.observation_id=o.id GROUP BY o.stage;
-- node cluster is one of the word's own clusters
SELECT n.source_stage, count(*), sum(EXISTS(SELECT 1 FROM cluster_strong cs WHERE cs.strong=n.strong
  AND cs.deleted=0 AND cs.cluster_code=n.cluster_code)) FROM ib_node n GROUP BY 1;
-- strand observations holding one parties value over several verses
SELECT count(*) FROM ib_observation o WHERE o.stage='strand-reading' AND o.parties IS NOT NULL
  AND (SELECT count(DISTINCT verse_reference) FROM ib_node WHERE observation_id=o.id) > 1;
-- the same text on several live rows
SELECT stage, count(*), sum(k) FROM (SELECT stage, obs_text, count(*) k FROM ib_observation
  WHERE status<>'withdrawn' GROUP BY stage, obs_text HAVING k>1) GROUP BY stage;
```
