# Validation after stage 4: understanding and plan

Escalation #2538, 2026-11-22. Not built; for the researcher's approval (B:17).

## 1. The instruction as understood

After stage 4 of a collection is complete, a validation runs over the collection: every live observation with its nodes. The observation comes first, and a node's standing hangs on it.

1. **What the observation says.** Is it true, founded in its verse and the base data, sensible, and coherent with the other observations?
2. **Whether its nodes are appropriately referenced.** Each node fills the maximum of its reference columns; where a column cannot be filled, the node says why.
3. **Whether the observation is unique in meaning.** No two observations say the same thing.

**Repair first.** Deletion is never the first option; making the observation true and its nodes properly referenced is pursued first. In order:
- An observation that is partly untrue or unfounded is restated so that it is true and founded, where the verse and base data support a true statement. Its change and reason are recorded.
- A node with an empty reference column that can be derived from context is completed.
- Duplicates are consolidated into one observation with a node for each variant, the second withdrawn.
- A node is deleted only when it cannot be referenced and the observation keeps at least one other live node that gives it context. The test before deleting a node: if this node were deleted, which other node still gives the observation its context?
- An observation is deleted only when it cannot be made true or founded, or is wholly duplicate. It is marked as such in its comment with the reason, then set deleted.

## 2. What the record shows that bears on the design

- Soft delete with its reason exists: `ib_observation.deleted` with the reason in `ib_observation_change`, and the same for nodes (B:130, B:131). The observation comment column is `revisit_note`; a node's free-text column is `disposition_note`. No schema change is needed.
- Node reference columns named in B:130: verse_reference, verse_lexical_id, surface, strong, morph_code, collection_id, subgroup_id, role.
- B:130 already provides for salvaging: a missing column derivable from context is derived; where a re-read is needed it is done; by hand, verified, in small steps, after a pilot, with counts predicted.
- B:131 already provides for restating a malformed observation (drafted by Claude, approved by the researcher) and for consolidation.
- Thought's gaps (counts in `outputs/escalation/2538-observations-fitness-1chr-28-9-v1-20261121.md`): 827 stage 4 nodes with no verse, word or collection; subgroup_id empty on 1,807 layer-2 and 1,346 layer-3 nodes; near-duplicate observations 22342, 22524 and 22604.

## 3. Points the researcher decides

1. **The 827 traced nodes.** Under repair-first they are not deleted at once. The first step measures what each is: whether the observation it belongs to has other live nodes that carry the verse and collection, and whether the node can be completed from the observation it traces. Open: where a traced node cannot carry a verse or collection, is it a valid reference of another kind, or is it deleted once another node gives the context?
2. **Partner words and subgroup_id.** Their collections have no subgroups yet, so the column cannot be filled. I propose the node keeps a stated reason in `disposition_note` and is not deleted for that alone.
3. **Restating an observation.** B:131 has the restatement drafted by Claude and approved by the researcher. Open: does the validation restate on Claude's reading and list each restatement for scrutiny, or hold each restatement for approval?
4. **Scope.** The collection includes older observations whose nodes carry its collection_id (prior-capture, verse-reading, char-answers and others), not only stages 1 to 4. Open: validate those by the same tests, or stages 1 to 4 only.

## 4. Plan, once approved

1. Register the step and its rules in config (`cfg_setting layer.reading`, a routine of `Collection-Build.ps1`: Pull, Record, Check), tested on a copy of the database under a named snapshot, with counts predicted and checked.
2. Pull: for the collection, list live observations with nodes, empty reference columns per node, candidate duplicate groups, and per observation the other nodes that would remain.
3. Read: Claude reads each observation against its verses and base data and decides, in this order: keep; repair (restate, complete a node); consolidate; delete a node (with the surviving context named); delete the observation (with the reason).
4. Record through the existing soft-delete, merge and node functions; every change in `ib_observation_change`.
5. Check: no live observation without a live node; no live node on a deleted observation; no two live observations of one meaning; every live node's empty reference columns carry a reason; every deletion carries its reason and, for a node, the surviving context; counts equal the prediction.
6. Pilot on thought. The stage 4 ledger stays closed only after the check passes.
7. Document the step in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12, governance.build_md_on_code_change).

## 5. Limits

Counts quoted are from read-only queries in this session. How many observations the thought scope holds across all stages, and how many stage 4 observations depend only on traced nodes, are not yet measured.
