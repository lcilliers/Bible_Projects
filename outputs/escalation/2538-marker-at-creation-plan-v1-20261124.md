# #2538 — Marker at creation: plan for approval (v1, 2026-11-24)

Researcher, 2026-11-24, in chat: first task of #2538 is "Marker at creation". Nothing is built. This file states what I understood, what I will change, how it is tested and the points I need decided (rule B:17).

## 1. What I understood

The stage 1 to 4 builds of the collection reading must write the marker (`ib_observation.nature`, evidence or inner_being) and the required node columns when they create an observation, so that no later validation has to mark or complete them. No old observation is read or changed: the 15,461 unmarked ones stay as they are until a collection build touches them. No scratch script is written; everything lives in code and config and is tested on a copy.

## 2. What is there today (read from the code and the tables)

- The recording paths that create observations: `iba/app/lib/layerreading.py` `record` (two direct inserts, for the stages 1 to 3 items: one for the single-sense case, one for the multi-sense case) and `iba/app/lib/layerinner.py` (stage 4 findings, through `orec.write` in `iba/app/lib/observationrecord.py`). `iba/app/lib/reading.py` is the older reading path and is not touched.
- None of them writes `nature`. Rule VA-05 says the marker follows content and purpose, never the stage, and `cfg_column.use` says it is "set only by the validation".
- Node columns: `layerreading.record` writes strong, verse_reference, surface, morph_code, role, verse_lexical_id, collection_id and subgroup_id from the verse_lexical row; the collection's subgroup comes from `collectionindex.subgroup_for`. A node whose source row has an empty morph or no subgroup is written with the gap and nothing refuses it.
- Items and their steps (`cfg_setting layer.reading`): S1 word-sense; 1.1 group-definition; 1.2 strong-enrichment; 2.1 pairing, qualifier, entity, direction, group-relation, double-meaning; 3.1 subgroup-analysis; 3.2 collection-gathering; 3.3 interworking.

## 3. What I will change

1. **Config.** Each item of `layer.reading` gets a `nature` value (the table in section 5). A new setting lists the node columns required at creation (role, collection_id, subgroup_id, verse_lexical_id, strong, surface, morph_code, verse_reference). Done by one idempotent migration under `iba/app/migration/` through `configmaint.apply_logged`, registered inactive, run once, then archived (USER-GUIDE, config work in Developer Mode).
2. **Code.** `layerreading.record`: both inserts write `nature` from the item's config. `observationrecord.write` takes an optional `nature` that `layerinner` passes. A finding file cannot set or override the marker; the item decides.
3. **Refusals at record time (the check, before any write).** An item with no `nature` in config is refused. A node that would be written without a required column is refused, naming the node and the column, unless the data cannot give it; in that case the reason is recorded in `ib_observation_change` in the same way `lib/validationactions.py` records a node completion with its reason (I will reuse that function, not write a second one). An inner_being finding whose traced node points at a deleted observation is refused; one traced to an unmarked older observation is accepted and reported pending, as IB-07 says.
4. **Records.** Amend VA-05 and the `nature` column text so that the marker is set at creation from the item and changed only by the validation; USER-GUIDE entry; BUILD entry; an escalation note on #2538 for each step done.
5. **Not in this task:** back-filling old observations, the reading of the remaining thought verses, the deferred items, the stage 5 claims.

## 4. How it is tested (rule B:97: on a copy, same session)

- Named snapshot of `iba/app/db/iba.db`, then a copy; the migration and the code are run on the copy only.
- One test file in the existing pattern (`iba/app/tools/temp_2538_marker_at_creation_test_run.py`), cases: each item records one observation with the right `nature`; an item without `nature` is refused and nothing is written; a node with a missing required column is refused; a node whose data cannot give the column is written only with its reason recorded; a finding that tries to set `nature` is refused; stage 4 traced to a deleted observation is refused and to an unmarked one is accepted; a second identical record writes nothing new; the existing validation tests (27 cases) and layer tests still pass.
- Only after the copy passes do I ask for your approval to migrate live, under a new named snapshot.

## 5. Decisions I need from you

1. **The marker of each item.** My proposal, from what each item states:

| Step | Item | Proposed nature | Why |
|---|---|---|---|
| S1 | word-sense | evidence | states what the word means in its verses |
| 1.1 | group-definition | evidence | defines the group from the words it holds |
| 1.2 | strong-enrichment | evidence | states what the Strong's code adds |
| 2.1 | pairing, qualifier, entity, direction, group-relation, double-meaning | evidence | state how words stand with the collection's words in the data |
| 3.1 | subgroup-analysis | inner_being | what the subgroup's words do for the inner being |
| 3.2 | collection-gathering | inner_being | the behaviours the collection gathers |
| 3.3 | interworking | inner_being | how the collection works with partners |

   I am unsure of group-definition and the 2.1 relation items (direction, group-relation); they could be read as inner being. Say which you rule differently.
2. **No override by a finding.** I propose that a finding file never sets the marker, since a finding that states both is split by the validation (VA-05). Confirm or say otherwise.
3. **Required columns.** Is the list in section 3.1 the one you mean, and may a node whose data cannot give a column (for example a source row with an empty morph code, as in #2541 case 2.1) be written with its reason recorded, rather than refused?
