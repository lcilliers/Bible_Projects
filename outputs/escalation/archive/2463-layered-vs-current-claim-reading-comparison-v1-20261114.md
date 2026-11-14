# #2463 The layered claim reading compared with the current claim reading (v1, 2026-11-14)

Status: a comparison for the researcher to correct. Read-only: no rule, config row, table, claim or observation was changed. Everything labelled "my reading" is inferential (B:4). Counts are copied from the records named in section 7.

The researcher asked for #2463, #2386 and the claim configs. `#2386` is a completed prose-tool issue (an unknown `-FlagCode`), unrelated to claims; I took `#2486` (Cross-link every claim to its collection) as meant. Say if another item was meant.

## 1. The three things compared

| Name used here | What it is | Where it is written down | State |
|---|---|---|---|
| **Current reading** | The claims process in the app: `Reading.ps1` Open, Observe, Record, Check (Observe gate), Synergy, Apply, Check (claims gate), Narrate, Check (narrate gate), Publish. Claims are written at Apply, from findings. | `iba/app/USER-GUIDE.md` section 8.2; `cfg_step` rows `reading.*`; `cfg_setting` `reading.*`; behaviour rules B:69, 71, 74, 76, 77, 112, 114, 116, 121 | Built and in use. Its scope is still a subgroup (#2495: "Open takes any subgroup"); the reading by collections (#2448) is meant to replace it and is on hold. |
| **The #2486 design** | What a claim is and is not, four levels, a skeleton destination, node-level links, a claim work-up list (14 questions), tested end to end on six claims on a copy. | `outputs/escalation/2486-claim-objectives-and-definition-draft-v2-20261113.md`, `2486-what-claims-do-draft-v2-20261113.md`, `2486-end-to-end-trial-findings-v1-20261113.md`, `2486-claim-collection-design-v2-20261113.md` | Drafts and a trial on a copy. Nothing in live config. Decisions open on #2486 (waiting on the researcher). |
| **The layered approach** | Your instruction of 2026-11-14 on #2463: claim reading and synergy in layers, starting from the collection evidence; each step ends in observations with nodes. | #2463 comment v16 (verbatim) | Described to layer 2, step 1. Nothing beyond layer 2 is handled yet. |

## 2. The layered approach in one table (what you described)

| Layer and step | Question | Material | Output |
|---|---|---|---|
| 1.1 | What does each word do for the inner being? Group the words; isolate any with no inner-being role. | md section 2.1; workbook sheets Links, Members (the 33 words) | One observation per group; the group's surfaces are its nodes. |
| 1.2 | What do the Strong's codes say about each group? Validate the grouping; give a short definition (for example, what meditation means); fix the codes that link the group to its usage. | md sections 2.2 and 3; sheets Strongs codes, Meaning trees | One observation per enrichment; the group's Strong's codes are its nodes. |
| 2.1 | Which words in the verse pair with which group? Which other words stand out? Are groups related or interchangeable? Qualifiers and their significance; number of entities, whether entities differ by group, whether direction of travel changes. Keep validating and reform groups, or record a double meaning. | md section 3.1; sheet Occurrences | An `ib_observation` per group or word, with nodes for verse, surface, Strong's, related surface (entity), role and the rest. |

## 3. Side by side

"Current" is the Reading.ps1 pipeline; "#2486" is the design in draft; "Layered" is the new approach. A dash means the item is not stated.

| # | Aspect | Current reading | #2486 design | Layered approach |
|---|---|---|---|---|
| 1 | **Unit of study** | One subgroup (or a segment of it) with an objective. Subgroups are history data since the collections rebuild (BUILD 498-512), still the only way to Open. | The collection (B:127); 169 collections would give 169 sub-chapters, which the researcher called enormous. The design lets claims cross collections. | One collection (thought, 33 words) as the first worked case. |
| 2 | **Where the work starts** | The verse. Observe puts verses in hand, 5 at a time; each surface of each verse is evaluated. | Claims already in the register (294 verse-only claims to re-evaluate against observations). The trial started from claim C-367 and worked back. | The words of the collection, before any verse (layer 1), then the Strong's behind them, then the verses (layer 2). Bottom up. |
| 3 | **First product** | Observations per verse, nodes on each occurrence. | A claim's backward link (claim, observation, node) and a skeleton destination. | Word groups and their definitions, held as observations. |
| 4 | **Grouping of words** | None inside the reading; collections and subgroups come from the rebuild. A surface with no inner-being role gets no observation. | Not addressed. | Central: groups within a collection by what the words do (starting, weighing, types of thought), and isolation of words with no inner-being role. Closest existing rule: B:129 (like words together), which stops at the collection. |
| 5 | **Role of the Strong's codes** | A per-verse sheet carries meaning tree, sense and lexicon columns (`reading.sheet_meaning`). Used when reading a verse, not to define a group. | Used in work-up question 2 (same surface, different Strong's) and question 3 (surface differs from root). | A step of its own: each group's codes are its definition and its link to usage. |
| 6 | **What an observation is** | One finding of one of eight kinds (face, qualification, party, statement, link, use, term, silence); nine items per observation (`reading.observation_items`); basis stated or read; applied through nodes to verses and words. | What the verse says, stopping short of how the inner being works (the new border). Observations that cross it are cut back. | A group, a group's Strong's enrichment, or a pairing (layer 2). In layers 1.1 and 1.2 the observation is about words, above the level of one verse. |
| 7 | **What a node is** | One occurrence in one verse (`verse_lexical_id`), with surface, Strong's, morph code, collection, role (B:130). | Same, plus a node-level claim link; empty roles on 14,065 of 68,406 live nodes block it. | Layer 1 nodes are surfaces and Strong's codes of a group. Layer 2 nodes carry verse, surface, Strong's, related surface (entity), role. |
| 8 | **Related words, entities, qualifiers, direction** | Per verse: party and link findings, qualifier role, polarity (refusal or pursuit), circumstance, chain. No profile across a collection. | Work-up questions 4 to 9: binding has four dimensions (partner type, reach, mode, expectation); the expectation is learned from how a collection's words operate; none of the four is held today. | Layer 2: pairing, standing-out words, relations between groups, interchangeability, qualifier significance, entity counts and direction. Same ground as #2486 questions 4 to 9 and 11, placed before claims. |
| 9 | **Where claims arise** | At Apply, after Synergy, from the findings of the scope; each node is disposed (claim, held, data, context, withdrawn). | A claim is what the verse says about how the inner being works, on one of four levels (surface, interaction, across, meta); the work-up list finds and tests them. | Not stated beyond layer 2. |
| 10 | **Validation** | Gates checked from the tables: Observe gate (every verse done), claims gate (every node disposed; every claim rests on a finding), narrate gate. | The researcher's verdict decides a claim, not the tool; a reading sheet per claim (C-367 done). | Each step validates the one before it (1.2 validates 1.1; 2.1 keeps validating and reforming groups). The validation is the researcher's reading; no tool check is described. |
| 11 | **Link to the narrative** | Tellings (`narrative_claim_telling`), 913 rows; main chapter or section set on 62 of 393 claims. | A skeleton index with stable keys (the four movements of #2345), one destination per claim; the telling relation stays for "told in several places". | Not stated. |
| 12 | **Order of reading** | A verse at a time, then synergy over the scope. | A claim at a time, working back to its evidence. | A layer at a time across the whole collection, then verse by verse. |
| 13 | **Execution** | Built. You will not have the tokens to run and test it for the thought collection. | A trial on six claims, done on a copy. | A process to be written; a worked illustration per step, no full analysis (your instruction). |

## 4. What the three share, and where the layered approach fits

1. **The collection is the starting frame.** The current reading will move there with #2448; the #2486 design and the layered approach already assume it.
2. **Observations and nodes carry the evidence; claims rest on them.** The claims gate already requires every current claim to rest on a finding. The layered approach does not change that.
3. **Layer 2 covers the same ground as the #2486 claim work-up.** Layer 2 step 1 (pairing, standing-out words, interchange, qualifiers, entities, direction of travel) is questions 4 to 9 and 11 of `2486-what-claims-do-draft-v2-20261113.md`. That draft proposed the work as a step between Observe and Synergy. The layered approach gives it a shape of its own: it is built in layers and written down as observations.
4. **Layer 1 is the surface level (level 1) of the four claim levels.** My reading: layers 1.1 and 1.2 ask what a word does (the surface level); layer 2 asks what words do together (the interaction level). Later layers would then be across collections and meta. That mapping is mine; you have said nothing past layer 2.

## 5. Where they differ in substance

1. **Direction.** Current works verse to claim; #2486 works claim back to verse; layered works word to group to verse. The layered approach is the only one that defines the groups inside a collection before the verses are read, and the only one that gives the Strong's codes a step of their own.
2. **The product of the early steps.** The current reading and the #2486 draft produce findings tied to verses. Layered steps 1.1 and 1.2 produce findings about a group of words and their codes, with no verse.
3. **When the inner-being meaning is stated.** The #2486 border puts "what it does for the inner being" in the claim, and the observation stops at what the verse says. Layer 2 asks what a pairing does "in or for the inner being" and records the answer as an observation. That is the crossing the researcher has ruled out for observations.
4. **Who decides.** The current reading lets Claude fill sheets and the app check them; #2486 makes the researcher's verdict final. The layered approach is the researcher's reading with Claude preparing, closer to #2486 and to B:127.
5. **Breadth.** The current reading is done per scope; the layered approach goes through the whole collection in each layer, which is more breadth per step and less depth per verse.

## 6. Conflicts and gaps if the layered approach is adopted (my reading; not decided, B:105)

| # | Point | The rule or record it meets | Question for the researcher |
|---|---|---|---|
| a | **Layer 1 nodes have no verse.** A node links a verse to the element an observation evaluates and carries `verse_reference` and `verse_lexical_id` (B:130). A group of words, and the Strong's codes of a group, are not an occurrence. | B:130 | Is a layer 1 node one node per occurrence of each surface of the group (many rows, each with a verse), or are layer 1 observations a different kind with a different anchor? If the second, the node rules need a new kind. |
| b | **The observation border.** Layer 2's "what it does in or for the inner being" is the claim side of the border. | #2486 v2 section 2; B:131 | Is layer 2 allowed to cross the border, or is "what it does for the inner being" the layer's claim, with observations stopping at what the verse says? |
| c | **A definition from the Strong's is not founded in a verse.** An observation is founded in its verse (B:131). A short definition of meditation from its codes is founded in the lexicon. | B:131; `reading.observation_parts` kinds `face` and `term` | Is the enrichment a lexicon-based `term` finding with the codes as nodes, and does B:131 need to name that basis? |
| d | **Groups inside a collection.** The collection is the unit; clusters and sub groups play no part in nodes and observations (B:130). The new groups (starting, weighing, the types) are a layer below the collection. | B:129, B:130 | Do the groups live only as observations, or also as a stored grouping that layer 2 reads? I have assumed observations only. |
| e | **A word in the collection with no inner-being role.** Isolation is in your instruction. Today such a word is `not_relevant` and kept in the scope JSON, or `standalone` on a node. | `reading.surface_requirements`, `reading.node_roles` | Which form does isolation take at the collection level, and is it recorded anywhere durable? |
| f | **Where the Check gates sit.** The claims gate requires every node of a reading to be disposed and every claim to rest on a finding. Layers 1 and 2 do not say how claims come out of them or how each node is disposed. | `reading.check`; USER-GUIDE 8.2 | Does the layered process replace Synergy and Apply, or come before Synergy as its preparation? |
| g | **The skeleton destination and the four claim levels of #2486 have no place yet in the layers.** | #2486 design | Do they come after layer 2 (layer 3 and later)? |
| h | **Node roles and collections are missing on many nodes.** 258 of the 394 occurrences of the collection thought have no live node, and 14,065 of 68,406 live nodes have no role. Layer 2 asks for the role on every node. | `2486-reading-c-367-outcome-v1-20261113.md`; trial findings 4 and 5 | Layer 2 can only run on occurrences that have nodes. Does layer 2 create them? |
| i | **Configs that would change.** `reading.observation_items` (nine items per verse observation), `reading.observation_parts`, `reading.node_roles` and the `reading.*` steps assume a verse and a subgroup. A layered process would need its own items (for a group and for a pairing), its own steps and rows in `cfg_step` and `cfg_enum`. Per `governance.rules_must_be_config_driven` they are `cfg_*` rows, not text in a document. | `cfg_setting reading.*`; `cfg_step reading.*` | None yet: this follows from the answers above. |

## 7. Facts used and where they come from

- Layered instruction: #2463 comment v16, quoted verbatim.
- Current reading steps and gates: `iba/app/USER-GUIDE.md` section 8.2 (lines 551-672); `cfg_step` rows `reading.open`, `observe`, `record`, `check`, `synergy`, `apply`, `narrate`, `publish`, `account`, `reopen`.
- Subgroup still the Open scope, until #2448: `iba/app/USER-GUIDE.md` line 440.
- Claim register: 393 rows in `narrative_claim`, 12 held (read from the table 2026-11-14); 2,228 source rows, 87 naming an observation, 913 tellings (from `2329-what-a-claim-is-v1-20261030.md`, not re-counted today); main chapter set on 62 of 393 (trial findings, finding 6: 331 have none).
- Claim levels, border, destination, work-up questions, binding: the #2486 drafts named in section 1.
- Thought collection: 33 member words, 132 Strong's codes (`_analytics/surfaces/exports/collection-evidence-thought-v1-20261113.md` sections 2.1 and 2.2).
- Rules named: B:69, 71, 74, 76, 77, 112, 114, 116, 121, 127, 129, 130, 131, read from `cfg_behaviour_rule` on 2026-11-14.
- Not checked: whether `reading.*` settings or `cfg_step` hold a layered or collection option I did not find, beyond the names read; whether #2448 already specifies a collection reading in layers (its record was not opened, because it is on hold and not taken up).
