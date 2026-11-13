# Node and observation rules, normalised from the current rules and your rulings (v2)

Status: draft for registration. Nothing registered, nothing changed in iba/app/db/iba.db. v1 asked six questions that the existing rules and your earlier rulings already answer; it is archived. This version states each answer with its source, and brings you only the conflicts and the rules that make no sense (section 4).

Sources read: your words on #2484, #2487, #2486, #2485, #2488, #2491 and #2463; `cfg_setting` reading.node_roles, reading.observation_rules, reading.observation_items, reading.observation_parts, reading.surface_requirements, reading.verse_loop; `cfg_column` of ib_node and ib_observation; behaviour rules 69, 70, 110, 121, 122, 127, 129; the #2273 design v6 and node usage v2 (your rulings of 2026-10-24); the writer iba/app/lib/engagement.py line 392; plan v3 R1 to R13.

## 1. Scope

- **S1.** The scope is the live collections (169 confirmed; your "277" and "approx 177" were earlier counts). A verse is in scope if it holds an occurrence of a member surface. Rules apply only in scope (2026-11-12).
- **S2.** Entity and other surfaces in an in-scope verse are in scope, as nodes of the observation that covers them; a verse with only entity or other surfaces is out of scope (R12).

## 2. The rules

| id | rule | source |
|---|---|---|
| N1 (R1) | Every collection surface has at least one finding (observation plus node); coverage is read on the nodes. | #2487 R1, D2; reading.surface_requirements |
| N2 | A node cannot exist without a live observation; a live observation has at least one live node; a node has one surface; an observation has several nodes. The node links the verse to the element the observation evaluates. | #2487 R1 |
| N3 (R2, R11) | The collection is on the node. A node on a collection surface carries its surface's collection (own row, else its base); every surface sits in exactly one collection (B:129), so a node carries one. | #2487 R2, R11; #2491; B:129 |
| N4 (R12; #2484 2026-11-13) | A node on an entity or other surface carries the collection of the surface it supports, so every node of the collection is discoverable through it. | #2484 |
| N5 (R2) | An observation is tied to a verse and a surface. One that is not is malformed: it is restated, specific to its verses and surfaces, a node for each; you approve each restatement. | #2487 R2, D4 |
| N6 (R9) | An observation is an application or analytic statement founded in its verse. A repeat of the verse text (more than 7 consecutive verse words, `max_verse_words_copied`) or a statement not founded in its verse is malformed. | #2487 R9; reading.observation_items; B:69 |
| N7 (R10) | Where an observation covers several surfaces it has a node for each. The same surface in the same verse under another observation has its own node. | #2487 R10, D3 |
| N8 | **No duplicates.** A duplicate observation is a second live observation with the same text: the writer refuses it and adds nodes to the existing one (reading.observation_rules merge_same_text_only; #2273 design v6 §3.1; your 2026-10-24 ruling). A duplicate node is a second live node on the same observation and the same occurrence (verse_lexical_id): refused on write (engagement.py line 392). Existing duplicates are withdrawn with their reason; the surviving node keeps the best-founded values. | your ruling 2026-10-24 and 2026-11-13; code |
| N9 (R4) | A node that names a word carries a role from cfg_enum observation_role, judged per finding from the verse, never from the cluster tag (RG-03, D7). An observation has at least one node of role characteristic or qualifier; one whose nodes only bear on (object, relational_target, enactment) is refused (bears_on_only_refused). | reading.node_roles, reading.observation_rules; #2273 D7 |
| N10 (R5) | A finding the verse no longer supports is withdrawn, the node or the finding everywhere, with its reason in ib_observation_change. A deletion is a soft delete (deleted = 1), never physical. | #2487 R5; cfg_column deleted |
| N11 (R8) | The surface is the lens, read per Strong's from verse_lexical.surface (B:110). | #2487 R8 |
| N12 (R13) | cluster_code and cluster_subgroup_code on a node are history, not analytic; reports read the collection. | #2487 R13; #2484 |
| N13 (R3) | The parts of an observation vary by observation and need; no aim to make them consistent. | #2487 R3 |
| N14 | A node has a validation flag (unvalidated, validated, held; date, run, rule-set version), set only by the validation process; any other change returns it to unvalidated. Work is by hand, verified, in small steps; a class goes in bulk only after a pilot with predicted counts checked. | #2487 (your method points a to d) |
| N15 | Records are registered as behaviour rules and settings; each change of a node or observation is recorded in ib_observation_change with its reason (RW-01). | #2273 design v6 §3.3; governance.rules_must_be_config_driven |

R6 and R7 are void (replaced by collections).

## 3. The columns of a node: required, how determined (live nodes, 61,473; empty now)

| column | required | how determined | empty |
|---|---|---|---|
| observation_id | yes | the observation served | 0 |
| verse_reference | yes | verse.osisId of the occurrence, resolved, never taken from text | 0 |
| verse_lexical_id | yes in scope | the verse_lexical row of the word in that verse whose surface equals the node's, narrowed by the observation's Strong's code; if still several, by hand (B:121) | 4,268 |
| surface | yes | verse_lexical.surface of that row (0 mismatches in 63,371 linked nodes) | 74 |
| strong | yes | verse_lexical.strong of that row | 74 |
| morph_code | yes | verse_lexical.morph_code of that row | 76 |
| collection_id | yes in scope | N3, N4 | 16,171 |
| role | yes on a node naming a word | N9, by reading the observation for that occurrence, by hand in verse batches (B:127: no bulk or model pass); held if not judgeable | 15,521 |
| source_stage | yes | the stage of the observation | 0 |
| seq | yes | per-observation ordinal, unique with observation_id | 0 |
| created_at | yes | UTC time of writing | 0 |
| cluster_code | yes (NOT NULL, history) | the word's code per cluster_strong at write time; not analytic | 0 |
| deleted | yes | 0, or 1 on withdrawal with its reason | 0 |
| validation flag | yes (new) | N14 | not yet |
| cluster_subgroup_code, question_code, traced_observation_id, reading_id, disposition, disposition_note | no | as the cfg_column text states | allowed empty |

## 4. Conflicts and rules that make no sense: for your ruling

Each is a case where two rules I found do not agree, or a rule no longer fits. None of them asks you to redefine a rule you answered.

1. **A supportive node over two collections against no duplicate nodes.** Your ruling (#2487, 2026-11-12) says a surface that refers to several collections gets several nodes; your ruling of 2026-10-24 and the writer (engagement.py line 392) refuse a second node on the same observation and occurrence. Since the rebuild an own-surface node never needs this (each surface is in one collection). It arises only for a supportive entity or other node in an observation whose collection surfaces sit in two collections: one node cannot carry two, and a second is a duplicate. Which governs for that case: (a) the observation is itself split into one finding per collection, so each node has one; (b) the node is repeated, and the duplicate rule keys on observation, occurrence and collection?
2. **Role standalone is not in reading.node_roles.** The enum has six roles; reading.node_roles lists five (relevant: characteristic, qualifier; bears on: object, relational_target, enactment) and omits `standalone`. 17,064 live nodes carry it. The rule "an observation needs a characteristic or qualifier node" therefore fails for 8,608 live observations (mostly prior-capture, strand-reading and verse-reading), which the bears-on-only refusal never saw because it runs on write. Is `standalone` a role that counts as relevant, bears on, or neither?
3. **D6 against the salvage.** #2273 D6 (2026-10-24) says existing nodes are not reclassified unless a re-read finds an error. Your salvage ruling (2026-11-12 and 2026-11-13) requires every in-scope node to comply. I read the later ruling as superseding D6 for in-scope nodes, and restate cfg_column text accordingly. Confirm that D6 is superseded.
4. **Cluster and subgroup rules that no longer fit R13.** B:121 sends a node that cannot be placed on one occurrence to its cluster's anomaly group; B:122 settles subgroups in the claims step; B:70 keeps cluster allocation as a loose association; ib_node.cluster_code is NOT NULL ("the word's own classification") and reading.verse_loop node_set and reading.observation_parts still list cluster_code and cluster_subgroup_code; 54,790 live nodes hold a subgroup. All of this treats cluster and subgroup as working categories, which R13 retires. Do I restate B:121 (by hand, no cluster anomaly group), retire B:122 and reduce B:70 and the settings to a history note?
5. **Stale column text.** cfg_column ib_node.collection_id still says that a node whose surface is in several collections "waits for the researcher's ruling", and ib_node.verse_lexical_id says "NULL until #2296 fills it". Both are overtaken (one collection per surface; the id is required in scope). I restate both. No decision needed, listed so you see it.
6. **Observation rules written for one stage.** reading.observation_rules, the eight kinds and the parts apply to stage Analysis_phase_1 and reading (549 observations). 14,000 live observations belong to other stages (prior-capture 6,709, verse-reading 5,520, strand-reading 771, engagement 520 and others) whose tags and parts follow older rules; R3 says no consistency of parts is sought. Do N5, N6, N8 and N9 apply to all stages, as I assume, while kinds, tags and parts are left as written?

## 5. After your rulings

I register N1 to N15 (behaviour rules class study_method; the machine-checkable parts in cfg_setting beside reading.observation_rules; column text and expectation in cfg_column), through apply_logged on a copy first and then live after a named snapshot, with the sources named and a BUILD.md entry. Then the read-only checker that lists every node and observation by the rule it breaks, and the fixing by class.
