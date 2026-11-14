# #2463 Is the concept level in the database, and in what format (v1, 2026-11-14)

Status: findings for the researcher to correct; read-only; nothing built or changed. Prompted by the researcher (#2463, 2026-11-14, verbatim): "did you resolve the concept question, is it in the database and in what format". Earlier answer (comparison v3, section 6, point 3) said only that `concept` sits above the collection; I had not followed the chain down to the surfaces. This paper does. Read first (B:123): `cfg_table.use` and `cfg_column.use` of `concept`, `concept_subgroup`, `concept_domain`, `cluster_subgroup`, `surface_subgroup`, `collection`, `surface_term`. Counts are my queries of 2026-11-14; readings are inferential (B:4).

## 1. The answer

Partly. A concept grouping of words is in the database, but it is a grouping of Strong's-and-surface pairs by cluster subgroup, built before the collections, not a grouping of the surfaces of a collection. It reaches the verse occurrences by a join and is not on the nodes. The grouping you described for thought (starting, weighing, the types of thought) is not stored anywhere.

## 2. The format: the chain from a word in a verse to a domain

| Level | Table | What a row holds | Rows (live) |
|---|---|---|---|
| word in a verse | `verse_lexical` | one code of one word: `strong`, `surface`, `position` | 544,667 |
| pair | `surface_subgroup` | `strong` + `surface` (lower case) allocated to a subgroup; `two_sense` (the pair carries two senses, settled per occurrence), `allocated_by`, `reason` | 13,452 |
| subgroup | `cluster_subgroup` | `cluster_code` (an M cluster), `subgroup_code` (for example `M15_thinking`), `label` ("Thinking, supposing, judging"), `core_description` (which sense of the cluster theme it covers), `kind` (group, qualifier, not_this_sense, anomaly) | 406 of kind group, 5 qualifier, 80 not_this_sense, 81 anomaly |
| concept | `concept` (via `concept_subgroup`, a subgroup is in one concept) | `name` (for example "Mind, thinking, considering, meditating"), `domain_id`, `description` (empty on all), `narrative_section_id` (empty until the narrative is rebuilt on it) | 101 |
| domain | `concept_domain` | `name` ("Knowing and thinking", "Will and action", ...), `narrative_chapter_id` | 14 |
| collection | `collection` | `concept_id`, described as "NULL until the rollup of collections into concepts, which will replace concept_subgroup"; empty on all 169 live collections | 169 |

The join to a verse occurrence is `verse_lexical.strong` + `lower(trim(verse_lexical.surface))` = `surface_subgroup.strong` + `surface`. 65,148 of the 544,667 live rows have a pair. The collection report's earlier `ExportMembers` and `ExportSurfaces` already carry subgroup, concept and domain by this join.

On the nodes: `ib_node` has `cluster_subgroup_code` (60,424 of 68,406 live nodes, history: no process writes it since #2495) and `ib_observation` has `cluster_subgroup_id`. `ib_node.collection_id` is on 62,072 nodes. There is no concept or group column on a node, and nothing links a subgroup, a concept or a group to a collection.

## 3. What it gives for thought (the real data)

235 of the 394 thought occurrences have a pair; 159 have none. The pairs sit in these subgroups, here with their concepts:

| Subgroup (label) | Occurrences | Concept |
|---|---|---|
| M15_thinking (Thinking, supposing, judging) | 98 | Mind, thinking, considering, meditating |
| M15_considering (Considering, meditating) | 23 | the same concept |
| M63_mind (Mind, thinking, discernment) | 17 | the same concept |
| M06_plotting (Plotting, devising) | 19 | Hatred, enmity, malice, plotting (domain Relational) |
| M64_counting (Counting, esteeming, regarding) | 9 | Reckoning, counting, regarding |
| M63_reasoning (Reasoning, disputing, questioning) | 8 | Doubt, perplexity, ignorance (domain Feeling: anxiety and doubt) |
| M64_devising, M84_murmuring, M47_heart, M26_counting, M15_knowing and others | 1 to 6 each | various |
| not_this_sense (several clusters) | 26 | none |

So one concept, "Mind, thinking, considering, meditating", holds 140 of the 235. It is too coarse to separate the kinds of thought. The subgroups are finer but are driven by the Strong's code and its cluster, and they cut across the groups you named:

| Your group | What the subgroups say (occurrences) |
|---|---|
| thinking (think, thinks, thinking) | M15_thinking about 44, M63_mind 5, one not_this_sense |
| the collective word (thought, thoughts) | `thought`: M15_thinking 15, M63_mind 3; `thoughts`: M06_plotting 19 and M15_thinking 16. One English word is in two concepts: a plotting sense and a thinking sense. |
| reasoning | `reasoned` and `reasoning`: M63_reasoning 8 (concept: doubt, perplexity, ignorance); `reason`: M26_not_this_sense 4 and M15_mind 2 |
| meditation | M15_considering 15, M84_murmuring 5 (a mutter or moan sense), one not_this_sense |
| weighing | `considered`: M15_considering 5 and M64_counting 3; `weigh`: M63_judging 1 |
| suggestion (suppose) | M15_thinking 7 |
| starting | `conceive`: one not_this_sense, 8 with no pair; `imagine`: M64_devising; `gives thought`: M16_wisdom |
| not placed (regard) | `regard`: M15_knowing 3 and M16_not_this_sense 2; `regarded`: M64_counting 4 and M15_thinking 3 |

My reading, with two points that bear on your layers:
1. **The subgroup data already splits some words by sense** (`thoughts` into plotting and thinking, `meditate` into considering and murmuring). That is the layer 1 step 2 work (the Strong's behind each group), partly done.
2. **The `not_this_sense` subgroup is already an isolation of words with no inner-being role** (26 of the thought occurrences, among them `reason` as cause), which is layer 1 step 1.

The gaps: 159 of 394 occurrences have no pair, among them the 25 `thought` and 8 `thinking` occurrences of H0559 (the saying word rendered as thought), `conceive` (H2029, H2030A, 8), `suppose` (H0194, 5), `weighing` (H4948, 4). The pairs were made for the M clusters, and the codes of the collection that are not in an M cluster, or were added after, have none.

## 4. What this means for your concept question

- Your remark that the groups are concepts and the database already provides for them is right for the chain above. Two things differ from what you described: the grouping was built on the Strong's code through the cluster, before the collections, and clusters and subgroups are no longer the starting or readying unit (your 4.1); and the groups you named for thought (starting, weighing, the types) are a finer cut by what a word does than any subgroup here.
- To get a concept on the nodes by the existing chain needs no new table: a node's `verse_lexical_id` gives the strong and surface, and the join gives the subgroup, the concept and the domain. That would put a history-built, code-driven grouping on the nodes, with 60 per cent coverage for thought.
- To hold your layer 1 groups, nothing exists: no table says "surface X of collection Y is in group G". The `collection.concept_id` column is for a roll-up of collections into concepts (a level above), not for groups inside a collection.

## 5. Decisions for the researcher

| # | Decision | Options | My recommendation |
|---|---|---|---|
| 1 | Where the layer 1 groups live | (a) the existing chain: a subgroup per pair, with a concept above it; (b) a new grouping below the collection, linking surfaces of a collection to a named group, with the group carried on the node; (c) the group as the layer 1 observation, found through its nodes, with no table of its own | (b) or (c) after the layer 1 pilot on thought; the existing chain is too coarse (one concept for 140 occurrences) and cut by the Strong's code. Whichever is chosen is a design to approve before any build (B:105) |
| 2 | The use of the existing subgroup data | ignore it; show it as a hint beside the surface in the report (subgroup, concept, not_this_sense); or use it to seed layer 1 | show it as a hint in the report (the join exists, nothing is stored); it already marks `not_this_sense` and the two-sense splits |
| 3 | The report's group column (the pairing paper, decision 1) | an approved list from config now, or the hint above | the approved list, with the hint beside it |

## 6. Not done

No table, column, row, report or rule changed. I did not check how the 159 occurrences without a pair arose, or whether those pairs would be made by a run of the cluster allocation; that process is retired as a starting unit.
