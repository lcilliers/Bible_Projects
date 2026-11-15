# #2505 Layers 1 and 2 of the collection reading: build design (v1, 2026-11-15)

Authority: the researcher's answers of 2026-11-15 on the readiness audit (verbatim on #2505) and the layer definition of 2026-11-14 (verbatim on #2463, v16, with the answers v18 to v22). Each choice below is traced to those words. Design choices the researcher delegated ("think through how the kinds and stages support your objectives") are marked (delegated). Everything built is tested on a database copy under a named snapshot (B:97).

## 1. What the layers are (the researcher's definition, as the rules will state it)

| Step | Question | Output | Gate before it |
|---|---|---|---|
| 1.1 groups | What does each word do for the inner being? Words with no inner-being role are isolated. | One observation per group, its surfaces' occurrences as nodes | the lexical gate: every member occurrence of the collection already carries a lexical node |
| 1.2 enrichment | What do the Strong's codes of a group say? Validate the grouping; a short definition; the codes are the link to usage. | One observation per group, its codes' occurrences as nodes | every 1.1 row validated |
| 2.1 pairings | What do the other words of the verse do for or with each group? Which stand out, are groups related or interchangeable, what qualifiers do, how many entities and do they differ between groups, does the direction of travel change, where a word has a double meaning. | One observation per aspect, nodes on the group's and the partner's occurrences | every 1.2 row validated |

Claims are formulated after the last layer from these observations. Layers 1 and 2 only prepare the base data.

## 2. Kinds and stages (delegated)

Stage records which layer wrote an observation: `layer-1`, `layer-2` (new `ib_observation.stage` values).

The eight existing kinds describe a reading of one verse. The layers need observations about a group, about its definition, about pairings and about relations between groups, so four kinds are added to `ib_observation.tag` (the existing `qualification`, `party` and `face` are kept for what they already mean):

| Item | Kind | Subject | Nodes | May be recorded as "none" |
|---|---|---|---|---|
| group-definition (1.1) | **group** (new) | a subgroup | every occurrence of the group's surfaces | no |
| strong-enrichment (1.2) | **enrichment** (new) | a subgroup | the occurrences carrying each Strong's code of the group; every code must have a node | no |
| pairing (2.1) | **pairing** (new) | a subgroup and a partner collection that shares at least `layer.reading` thresholds.pair_min_verses verses with it | the group's occurrences and the partner's occurrences in those verses | yes, with a reason |
| qualifier (2.1) | qualification (existing) | a subgroup with a qualifier candidate among its pairings | the group's occurrences and the qualifier candidates | yes |
| entity (2.1) | party (existing, route) | a subgroup with an entity among its pairings | the group's occurrences and the entities | yes |
| direction (2.1) | **relation** (new) | a subgroup with an entity | as entity | yes |
| group-relation (2.1) | **relation** (new) | two subgroups sharing at least thresholds.relation_min_verses verses | the occurrences of both in the shared verses | yes |
| double-meaning (2.1) | face (existing) | a surface of a group whose occurrences carry more than one Strong's code | its occurrences | yes |

A word with no inner-being role is recorded in the index as `isolated` with its reason (it has no observation; B:130 `standalone` and `reading.surface_requirements` already say so).

## 3. The ledger: nothing hangs in the air (delegated)

New table `collection_layer_item`: one row for every aspect a step requires, derived mechanically from the data when the step is opened (collection, step, item, subgroup, subject), with a state (`open`, `observed`, `none`, `retired`), the observation that answers it, a reason for `none`, and `validated` (set only by the check). A step is closed when every row is `observed` or `none` and validated. The next step cannot be opened until the previous one is closed. A row whose subject disappears (a group retired, a partner no longer shared) is retired by the next open; an observation whose nodes no longer match what the data demands fails its validation.

## 4. The group on the node

`ib_node.subgroup_id` (new, nullable, foreign key to `collection_subgroup`) carries the group of the node's surface (the researcher: "if the claim need to references a group it should be able to discover it"). The four node writers fill it (observationrecord, draftapply, engagement, recordingpass); `collection.subgroup` placements update live nodes; a refresh step (`NodeGroups`) and the index check keep it in agreement with the index.

## 5. Routines (Collection-Build.ps1, work package collection-build)

| Action | Does |
|---|---|
| LayerOpen -Collection -Step | checks the gates, derives the ledger rows of the step; read-only with -Check |
| LayerPull -Collection -Step | writes the working file of the open rows with the evidence to read (occurrences with verse text, Strong's meanings, pairings) |
| LayerRecord -File [-Check] | checks the filled file whole and writes the observations, their nodes (built from the data, so they are complete) and the ledger answers, in one transaction |
| LayerCheck -Collection | validates every ledger row against the tables, sets `validated`, reports what is open, stale or missing; also states the lexical gate |
| NodeGroups [-Check] | sets `ib_node.subgroup_id` from the index |

## 6. Rules (G1, G2, G3, G5; replace, retire, do not duplicate)

- New behaviour rules: the layers and their order (points to `cfg_setting layer.reading` for the content, B:3); lexical and claims readings are separate and the lexical gate; who decides (AI reads the evidence and decides; the researcher scrutinises, and sees only what the evidence could not settle).
- B:119 and B:120 reworded for collections (draft v2); RW-02 restated; RG-09 last sentence aligned; RO13 retired.
- Method rules for the new steps (kinds, nodes, ledger, validation).

## 7. Housekeeping

- 274 stale `shared` flags on collection links reset (IndexCheck finding), each with a surface_event.
- The concept prototype retired (researcher: abandoned; replaced by collections and surface groups): rows soft-deleted, the tool and the rules that name it retired, readers cleaned. Footprint measured first.
- Dangling reference in the #2463 context to the destroy plan: history, left as it is (B:96).

## 8. Not decided here

The groups of any collection (the researcher's reading; `Collection-Build.ps1 -Action Subgroup`). Until a collection's lexical gate passes and its surfaces are placed, LayerOpen refuses for it, and says why.
