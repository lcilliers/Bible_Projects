# Validation after stage 4: understanding and plan

Escalation #2538, session 20261121 continued on 2026-11-22. Not built; for the researcher's approval (B:17).

## 1. The instruction as understood

After stage 4 of a collection is complete, a validation runs over that collection. Its scope is every live observation of the collection with its nodes. It does three things:

- **a) Consolidate.** No two observations say the same thing, judged by meaning and not by wording.
- **b) Complete the node references.** Each node fills the maximum of its reference columns. Where a column cannot be filled, the node carries a clear comment of why.
- **c) Test the observation.** Each is true, founded in its verse and the base data, makes sense, and is coherent with the others.

Outcomes:
- An unfounded or untrue observation is marked as such in its comment and set deleted.
- Duplicated observations are consolidated into one; the others are marked deleted.
- A node that cannot be referenced is deleted.

It is part of the codified process of #2538, so it runs the same way for every collection.

## 2. What the record shows that bears on the design

- Soft delete with its reason already exists: `ib_observation.deleted` with the reason in `ib_observation_change`, and the same for nodes (B:130, B:131). The observation comment column is `revisit_note`. A node's only free-text column is `disposition_note`, which by its recorded meaning is the reason for the disposition (withdrawn when deleted). No schema change is needed for the comments.
- Node reference columns named in B:130: verse_reference, verse_lexical_id, surface, strong, morph_code, collection_id, subgroup_id, role.
- B:131 already provides for consolidation: one observation with a node for each variant; the second is withdrawn and its nodes moved to the first.
- Thought's gaps found this session (counts in `outputs/escalation/2538-observations-fitness-1chr-28-9-v1-20261121.md`): 827 stage 4 nodes with no verse, word or collection; subgroup_id empty on 1,807 layer-2 and 1,346 layer-3 nodes; near-duplicate observations (22342, 22524, 22604).

## 3. Points the researcher decides

1. **The 827 traced nodes.** They carry no verse, word or collection. Under (c) they are deleted. B:130 then requires that an observation with no live node is deleted too. If those nodes are the only live nodes of some stage 4 building-block observations, the validation as worded would delete those observations. I have not measured how many; the first step counts them and predicts before anything is changed. Decision: delete them as worded, or treat a node traced to another observation as a valid reference of a different kind.
2. **Partner words and subgroup_id.** Partner words sit in collections with no subgroups yet, so the column cannot be filled. Under (b) the node says why in `disposition_note`, and is not deleted for that alone. Decision: confirm that an unfilled subgroup_id with a stated reason is acceptable; a node is deleted only where the verse, word or collection cannot be given.
3. **Who decides "true and founded".** The check is by Claude reading the verse and the base data. Under B:4 the result is inferential until you confirm. Under B:132 Claude decides and brings only what the evidence cannot settle. Decision: Claude deletes on its reading and lists each deleted observation with its reason for your scrutiny, or Claude deletes only the clear cases and holds the doubtful ones for you.
4. **Scope.** The collection's scope includes the older observations whose nodes carry its collection_id (prior-capture, verse-reading, char-answers and others), not only stages 1 to 4. They are validated by the same three tests, so the older rows that cannot be revived leave through (c). The first step counts them.

## 4. Plan, once approved

1. Register the validation as a step after the stage 4 steps in `cfg_setting layer.reading` and as a routine of `Collection-Build.ps1` (Pull, Record, Check, like the layers), with its rules in config (B:31, governance.rules_must_be_config_driven). Tested on a copy of the database, under a named snapshot, with counts predicted and checked.
2. Pull: for the collection, list its live observations with nodes, the empty reference columns per node, and candidate duplicate groups.
3. Read: Claude reads each observation against its verses and the base data, and decides keep, consolidate, or delete with a reason.
4. Record: apply through the existing soft-delete, merge and node functions; every change in `ib_observation_change`.
5. Check: no live observation without a live node; no live node on a deleted observation; no two live observations of one meaning; every live node's empty reference columns carry a reason; counts equal the prediction.
6. Run on thought first as the pilot. The ledger of stage 4 stays closed only after the check passes.
7. Documentation of the new step in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12, governance.build_md_on_code_change).

## 5. Limits

Counts quoted are from this session's read-only queries. How many observations the thought scope holds across all stages, and how many stage 4 observations depend only on traced nodes, are not yet measured.
