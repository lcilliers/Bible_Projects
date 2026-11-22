# Validation after stage 4: understanding and plan

Escalation #2538, 2026-11-22. Not built; for the researcher's approval (B:17).

## 1. The instruction as understood

After stage 4 of a collection is complete, a validation runs over every observation related to the collection, with its nodes. An observation's standing comes first, and a node's standing hangs on it.

**Scope (researcher, 2026-11-22).** All observations through the entire study with any relation to the contents of the collection, where related means:
- a) it refers to the collection;
- b) it refers to a verse in the collection;
- c) it refers to a strong that is part of the collection;
- d) its meaning relates to the collection.
Previously deleted observations and nodes are excluded.

**Tests, for each observation:**
1. What it says: true, founded in its verse and the base data, sensible, coherent with the other observations.
2. Whether its nodes are appropriately referenced: the maximum of each node's reference columns filled, with a stated reason where one cannot be.
3. Unique in meaning: no two observations say the same thing.

**Repair first, delete last.** In order:
- Keep it if it passes.
- Repair: restate a partly untrue or unfounded observation so it is true and founded where the verse and base data support it; complete a node column that can be derived from context.
- Consolidate duplicates into one observation with a node for each variant; withdraw the other.
- Delete a node only when it cannot be referenced and another live node still gives the observation its context (that node is named before the deletion).
- Delete an observation only when it cannot be made true or founded, or is wholly duplicate; its comment records the reason first.

## 2. What the record shows that bears on the design

- Soft delete with reason exists: `ib_observation.deleted` with the reason in `ib_observation_change`; the same for nodes (B:130, B:131). Observation comment: `revisit_note`; node comment: `disposition_note`. No schema change needed.
- Node reference columns (B:130): verse_reference, verse_lexical_id, surface, strong, morph_code, collection_id, subgroup_id, role.
- B:130 provides for salvaging (derive, re-read, by hand, pilot, counts predicted); B:131 for restating and consolidating.
- Thought's gaps (counts in `outputs/escalation/2538-observations-fitness-1chr-28-9-v1-20261121.md`): 827 stage 4 nodes with no verse, word or collection; subgroup_id empty on 1,807 layer-2 and 1,346 layer-3 nodes; near-duplicates 22342, 22524, 22604.
- **Size of the scope for thought (collection 56), read-only, 2026-11-22:**
  - a) live observations with a live node carrying the collection: 785.
  - b) live observations with a live node on one of its 351 verses: 1,180, of which 395 are not in a).
  - c) by strong: a count by the 132 strongs that thought's own member words carry gives 2,946 observations. It is inflated. Those 132 strongs include function-word codes that sit inside its phrases (for example G3588, G2532, G1519), so almost every verse observation matches. The strong set must be defined before c) can be run.
  - Union of a, b and c as counted: 3,228 (prior-capture 2,087, layer-3 217, verse-reading 215, lexical 202, engagement 181, layer-2 132, strand-reading 98, others 96).
  - d) is by meaning, read, and is not counted; it can add to this.

## 3. Points the researcher decides

1. **The traced nodes (827).** Not deleted at once. Open: where a traced node cannot carry a verse or collection, is it a valid reference of another kind, or deleted once another node gives the context?
2. **Partner words and subgroup_id.** Their collections have no subgroups yet. Proposed: the node keeps a stated reason in `disposition_note` and is not deleted for that alone.
3. **Restating an observation.** B:131 has Claude draft and the researcher approve. Open: restate on Claude's reading and list each for scrutiny, or hold each for approval.
4. **The strong set for c).** Open: which strongs count as part of the collection: those of its single-word members only; or also those of the words inside its phrases, excluding function words (and by what list); or all of them.
5. **Order of work at this size.** About 3,200 observations or more for one collection, each read against its verses, is large work, repeated for 169 collections. Open: do the structural tests (columns, duplicates by text) for all first, and the reading of truth and meaning in batches per verse; or one pass per observation.

## 4. Plan, once approved

1. Register the step and its rules in config (`cfg_setting layer.reading`, a routine of `Collection-Build.ps1`: Pull, Record, Check), tested on a copy under a named snapshot with counts predicted and checked.
2. Pull: the scope of the collection by a), b), c) as defined, listed per observation with its nodes, empty reference columns, candidate duplicates, and the other nodes that would remain; d) added by the reading.
3. Read each observation against its verses and base data and decide: keep, repair, consolidate, delete a node, delete the observation.
4. Record through the existing soft-delete, merge and node functions; every change in `ib_observation_change`.
5. Check: no live observation without a live node; no live node on a deleted observation; no two live observations of one meaning; every empty reference column has its reason; every deletion has its reason and, for a node, the surviving context; counts equal the prediction.
6. Pilot on thought. The stage 4 ledger stays closed only after the check passes.
7. Document in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12, governance.build_md_on_code_change).

## 5. Limits

Counts are from read-only queries in this session. d) is unmeasured. The strong set for c) is not yet defined.
