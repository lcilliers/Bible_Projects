# Validation after stage 4: understanding and plan

Escalation #2538, 2026-11-22. Not built; for the researcher's approval (B:17).

## 1. The instruction as understood

After stage 4 of a collection is complete, a validation runs over every observation related to the collection, with its nodes. The observation comes first; a node's standing hangs on it.

**Scope (researcher, 2026-11-22).** All observations in the study related to the collection, excluding deleted observations and nodes. Related means: a) it refers to the collection; b) it refers to a verse in the collection; c) it refers to a strong that is part of the collection; d) its meaning relates to the collection.

**Tests, for each observation:**
1. What it says: true, founded in its verse and the base data, sensible, coherent with the other observations.
2. Its nodes are appropriately referenced: each column its kind of node requires is filled, supplementary columns are filled where it can be done, and a column left empty has its reason.
3. Unique in meaning: no two observations say the same thing.

**Repair first, delete last.**
- Keep it if it passes.
- Repair: restate a partly untrue or unfounded observation so that it is true and founded; where the restatement changes the meaning, it is validated against the base data (researcher, 2026-11-22). Complete a node column derivable from context.
- Consolidate duplicates into one observation with a node for each variant; withdraw the other.
- Delete a node only when it cannot be referenced and another live node gives the observation its context.
- Delete an observation (and its nodes) when it is meaningless for the study and cannot be made true, or is wholly duplicate, with its reason in its comment first.

## 2. What a traced node is (read from the code and the recorded text, 2026-11-22)

- `ib_node.traced_observation_id`: "set when grounded in ANOTHER observation instead of a verse". It is the link by which a stage 4 observation records which stage 3 observations it rests on.
- `iba/app/lib/layerinner.py` (the stage 4 check) requires, for each stage 4 observation, both nodes on occurrences (a word of a verse) and at least one traced node: "rests on no observation (a traced node on each)". Each traced observation must be one the step may rest on; every stage 3 observation the step reads must be rested on by some finding or declared not used with a reason. So the traced node is the evidence chain of stage 4. A traced node carries no verse, word, strong, role or collection by design: it names an observation, not a word.
- The 827 traced nodes with all word columns empty (thought, stage 4) are therefore not incomplete word nodes. My earlier statement that they break B:130 was a misreading of mine and is withdrawn. They are deleted only with an observation that is meaningless for the study, as the researcher states; deleting one alone breaks the stage 4 check for its observation.

## 3. The node columns, by kind (from `cfg_column.use`; items marked "not verified" were not checked in the code)

**System, every node:** id, observation_id, source_stage, seq, created_at, deleted.

**Required on a word node (a node on an occurrence):**
- verse_reference, verse_lexical_id, surface, strong, morph_code: the verse_lexical row of the occurrence ("required").
- role: judged per finding; "required on a node that names a word". Values by stage: lexical on stage 1 nodes; the inner-being roles on stage 4 (the check refuses any other); characteristic, qualifier, object, relational_target, enactment or standalone on others.
- collection_id: "required on every in-scope node; NULL only on a node not yet validated".

**Required on a traced node:** traced_observation_id, with the word columns empty by design.

**Required once the surface is placed, otherwise empty with its reason:** subgroup_id. It is the collection's subgroup of the surface, "NULL while the surface is unplaced or isolated, or on a node with no collection"; it is how the claims find a group's observations.

**Supplementary, to be filled where it can be:** reading_id (the reading that applied the finding; filled by nodes of the reading process; not verified for other kinds), disposition and disposition_note (the claims step sets them; empty until then is correct; disposition_note carries a deleted node's reason).

**Redundant or history (noise for new work):**
- cluster_code and cluster_subgroup_code: written by no process since 2026-11-13 (#2484, #2495); the collection replaced them. They are held by old nodes only.
- question_code: the catalogue question of the old API stages; held by verse-reading (6,142) and char-answers (1,405) nodes only and by none of the others. Whether it is redundant is not stated in its recorded text; not verified.

## 4. Where thought stands against that (read-only, 2026-11-22)

Word nodes of stages 1 to 4 (lexical 367, layer-1 788, layer-2 3,394, layer-3 1,704 = 6,253):
- collection_id and role: empty on none.
- morph_code: empty on 12 (layer-1 2, layer-2 6, layer-3 3, lexical 1). These are real gaps.
- subgroup_id: empty on 1,807 layer-2 and 519 layer-3 word nodes. A test against collection_subgroup_surface (surface text, same collection, state placed) finds none of them on a surface that is placed. By that test it is empty for the stated reason, not an omission. The test matches by surface text only.
- traced nodes: 827, all word columns empty by design.

My earlier statement that the thought nodes were incomplete in their node columns, which I agreed with on the strength of the counts, was wrong except for the 12 morph_code values. The incompleteness that stands is in the older stages: role empty on 12,753 live nodes, and collections empty on the older nodes counted earlier.

## 5. The scope for thought (collection 56)

- The rule that exists for the strongs of a collection is stage 1 of B:132: every word of the collection by surface and lettered Strong's code, at its occurrences. In the ledger that is 197 surface and strong pairs (for example conceive with G2192).
- c) therefore means observations with a node on a member surface carrying its own lettered strong: 775 observations, all already inside a). My earlier count of 2,946 took the strongs without their surface and is withdrawn.
- a) 785 observations with a node carrying the collection; b) 1,180 with a node on one of its 351 verses (it contains a)). So a, b and c together are 1,180 observations for thought. d) is added by reading.
- Not yet checked: whether the 351 verses are the right verse set for b) (they are the verses of nodes that carry the collection, including verses reached by supporting words).

## 6. Plan, once approved

1. Register the step and its rules in config (`cfg_setting layer.reading`, a routine of `Collection-Build.ps1`: Pull, Record, Check), tested on a copy under a named snapshot, counts predicted and checked.
2. Pull: the scope by a), b), c) as in section 5; per observation its nodes by kind (section 3), the columns empty and their reasons, candidate duplicates, the other nodes that would remain.
3. Structural tests for the whole scope first; then the reading of truth, foundation and meaning, batched by verse so that each verse is read once with all its observations; d) found in that reading.
4. Record through the existing soft-delete, merge and node functions; every change in `ib_observation_change`; a restatement that changes meaning carries its base-data check.
5. Check: no live observation without a live node; no live node on a deleted observation; each stage 4 observation keeps its traced node; no two live observations of one meaning; every empty column has its reason; every deletion has its reason and, for a node, the surviving context; counts equal the prediction.
6. Pilot on thought. The stage 4 ledger stays closed only after the check passes.
7. Document in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12, governance.build_md_on_code_change).

## 7. Limits

Counts come from read-only queries in this session. d) is unmeasured. Section 3's classification rests on the recorded column text; question_code and reading_id were not checked in code. The verse set for b) is as stated in section 5.
