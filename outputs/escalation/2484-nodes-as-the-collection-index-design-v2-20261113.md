# The nodes as the collection index: design for decision (v2)

Status: design only. Nothing built, nothing changed in iba/app/db/iba.db. Replaces v1 (a separate `observation_collection` index), which is archived: the researcher's point of 2026-11-13 is that the nodes are the index, and a second index to index the index is not needed.

## The principle

A node is the cross-reference from a verse and a surface to an observation (plan v3 R1). If every live node carries its collection, then:

- the collections of an observation are `SELECT DISTINCT collection_id FROM ib_node WHERE observation_id=? AND deleted=0`;
- the observations and nodes of a collection are `SELECT ... FROM ib_node WHERE collection_id=? AND deleted=0` (with the observation by join).

One stored column, one query, no new table. The index is the node table, as originally planned.

## Why the nodes do not do this today (measured read-only, 2026-11-13)

| gap | size | cause |
|---|---|---|
| nodes with no collection | 16,171 of 61,473 live | entity, `other`, unmatched and no-surface nodes were never given one (7,891 + 7,890 + 316 + 74) |
| observations reached by no node column | 2,247 of 14,947 live | every node of these has no collection |
| a node that should carry several collections | 1,307 mapped today; the unmapped ones with several sibling collections 8,757 | the column holds one collection |
| readers do not read the column | all three | the evidence report goes by `verse_lexical_id`, engagement and reading by verse; none reads `ib_node.collection_id` |

The column itself is correct where filled (0 of 42,949 nodes disagree with the other routes). So the gaps are completeness and the readers, not a missing structure.

## What closes the gaps, with no new table

1. **Complete the nodes.** A supportive node (entity or `other` surface) takes the collection of the surface it supports, by your ruling of 2026-11-13. Where that surface is in one collection the node carries it. Where the observation needs several collections the node is repeated, one per collection, as you ruled on 2026-11-12 (that repeat is already known to be large for own-surface nodes: 20,634 new nodes; the count for supportive nodes is not yet measured).
2. **How a supportive node knows what it supports.** Either by reading each observation and setting the collection by hand-checked list (my recommendation: the node's collection is written, with the reason in `ib_observation_change`, as every earlier fill), or by the same-verse rule by script for the clear cases (4,764 nodes) and a list for the rest. No support-link column is needed: the collection on the node is the record.
3. **Readers read the nodes.** The evidence report, engagement and reading take their observations from `ib_node.collection_id`, in one change, with counts before and after on three collections compared and the differences explained.
4. **A standing check, not an index:** the stored-data faults of the evidence report gain "live node with no collection" and "live observation none of whose nodes has a collection", listed on every read, so an orphan is never silently absent.
5. **The node-writing path** (Reading.ps1 Record) sets the collection at write time (point D5 of #2484), so new nodes are complete.

## Decisions for you

- **D1. Supportive nodes: by hand-checked reading (recommended) or by the same-verse script for the 4,764 clear cases and a list for the rest.**
- **D2. Several collections:** repeat the node per collection (your earlier ruling; recommended, after I measure the count for supportive nodes and report it) or leave empty and list.
- **D3. The 2,247 observations whose nodes none carries a collection:** list them per stage for you, the older verse-reading (1,291) and prior-capture (570) first, for restatement or withdrawal (plan v3 R2, R5).
- **D4. Readers:** all three on the node column in one change (recommended) or the evidence report first.
- **D5. The 4,268 live nodes with no verse_lexical_id:** the readers no longer depend on it, so the fill is no longer what hides them; the fill stays a separate matter.

## What you are asked to approve

D1 to D5. On approval I measure the repeat count for supportive nodes first and report it, then build on a copy, compare actual with predicted, and write live only after a named snapshot.
