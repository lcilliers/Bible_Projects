# Node and observation rules, normalised: for confirmation before registration in config

Status: draft of the rule set and its open questions. Nothing registered, nothing changed in iba/app/db/iba.db. Sources: the researcher's words verbatim on #2484, #2487, #2486, #2485, #2488, #2491 and #2463 (read in full today), the node plan v3 (outputs/escalation/2487-node-salvage-plan-v3-20261112.md, R1 to R13), cfg_column for ib_node and ib_observation, cfg_setting reading.node_roles, and behaviour rules 69, 110, 121, 122. Where two sayings of yours conflict, the later one wins and is named. Section 4 holds the questions I could not settle from your words; section 5 what I register once they are settled.

## 1. Scope

**S1. The scope is the live collections** (169 confirmed after the rebuild; your "277" and "approx 177" were earlier counts). A verse is in scope if it holds an occurrence of a member surface of a live collection. Nothing outside the scope is touched or judged; rules apply only in scope (2026-11-12, "my rule evaluation only applies to collection related work"). Out-of-scope nodes were withdrawn on 2026-11-12 (BUILD 495).
**S2. Entity and other surfaces in an in-scope verse are in scope**, as the supportive nodes of the observation that covers them (R12). A verse with only entity or other surfaces is out of scope.

## 2. The rules (normalised; R-numbers are those of plan v3)

| id | rule | source |
|---|---|---|
| N1 (R1) | Every collection surface has at least one finding, a finding being an observation plus a node. Coverage is read on the nodes, not on the observations. | #2487 R1, D2 |
| N2 | A node cannot exist without a live observation, and a live observation has at least one live node. A node has exactly one surface; an observation has several nodes; a verse has several observations. A node is the cross-reference linking a verse to the element the observation evaluates. | #2487 R1 |
| N3 (R2, R11) | The collection is on the node: a node on a collection surface carries the collection of its surface (own row, else its base). Every in-scope node carries one; one without is an error to resolve. | #2487 R2, R11; #2484 |
| N4 (R12, new ruling 2026-11-13) | A node on an entity or other surface carries the collection of the surface it supports, so that every node of the collection is discoverable through the collection. | #2484 |
| N5 (R2) | An observation is tied to a verse and a surface. One that is not is malformed: it is restated, specific to its verses and surfaces, with a node for each verse and surface it applies to. | #2487 R2 |
| N6 (R9) | An observation is an application or analytic statement interpreting what its verse says, founded in the verse. A repeat of the verse text, or a statement not founded in its verse, is malformed (and is let scripture speak, B:69). | #2487 R9 and later |
| N7 (R10) | Where an observation covers several surfaces there is a node for each. The same surface in the same verse under a different observation has its own node there. | #2487 R10, D3 |
| N8 (new) | **No duplicates.** Two live nodes with the same observation, the same occurrence (verse_lexical_id) and the same collection are a duplicate: the later is withdrawn, with its reason, and a duplicate is refused on write. The same for two live observations with the same text on the same nodes. | #2484, 2026-11-13 |
| N9 (R4) | A node that names a word carries a role from cfg_enum observation_role; characteristic and qualifier are relevant, object, relational_target and enactment bear on (cfg_setting reading.node_roles). | #2487 R4 |
| N10 (R5) | A finding the verse no longer supports is withdrawn, the node or the finding everywhere, with its reason in ib_observation_change. A deletion is a soft delete (deleted = 1), never physical. | #2487 R5; cfg_column deleted |
| N11 (R8) | The surface is the lens: it is read per Strong's from verse_lexical.surface (B:110). | #2487 R8 |
| N12 (R13) | cluster_code and cluster_subgroup_code on a node are history, not analytic; reports read the collection. They stay as stored. | #2487 R13, #2484 |
| N13 (R3) | The parts of an observation vary by observation and need; there is no aim to make them consistent. | #2487 R3 |
| N14 | A node has a validation flag (unvalidated, validated, held, with date, run and rule-set version), set only by the validation process; any other change returns it to unvalidated. Work is done by hand, verified, in small steps; a class goes in bulk only after a pilot, with predicted counts checked. | #2487 (the flag, method) |
| N15 (R6, R7) | Void: replaced by collections. | #2487 |

## 3. The columns of a node: required, and how each is determined

Counts are live nodes (61,473) with the column empty, read now.

| column | required | how it is determined | empty now |
|---|---|---|---|
| observation_id | yes | the observation the node serves | 0 |
| verse_reference | yes | the osisId of the verse of the occurrence (verse.osisId), never taken from text | 0 |
| verse_lexical_id | yes, in scope | the verse_lexical row of the occurrence: the word of that verse whose surface equals the node surface (and Strong's code where the observation names one) | 4,268 |
| surface | yes | verse_lexical.surface of that row (0 mismatches in 63,371 linked nodes) | 74 |
| strong | yes | verse_lexical.strong of that row | 74 |
| morph_code | yes | verse_lexical.morph_code of that row | 76 |
| collection_id | yes, in scope | N3 for a collection surface; N4 for a supportive node | 16,171 |
| role | yes on a node naming a word | the word's role in this finding (N9), judged from the observation, not from the word | 15,521 |
| source_stage | yes | the stage of the observation | 0 |
| seq | yes | per-observation ordinal, unique with observation_id | 0 |
| created_at | yes | UTC time of writing | 0 |
| cluster_code | yes (NOT NULL, history) | the word's M or T code per cluster_strong at write time; not analytic | 0 |
| deleted | yes | 0, or 1 on withdrawal with its reason | 0 |
| validation flag columns | yes (new) | N14 | not yet |
| cluster_subgroup_code, question_code, traced_observation_id, reading_id, disposition, disposition_note | no | as the config text of each column states | allowed empty |

## 4. Open questions (not settled by your words)

**Q1. What a duplicate is, against repeating a node for several collections.** You ruled both that duplicates are not allowed and, on 2026-11-12, that a surface needing several collections gets several nodes. The key in N8 includes the collection, so a node repeated for another collection is not a duplicate. Today 1,805 groups (2,096 extra rows) share observation, verse, surface and occurrence. Is N8's key right? Recommended: yes.

**Q2. A supportive node whose observation spans several collections** (N4). Your 2026-11-12 words: look at the observation for which collection words it captures, then update or create nodes. Recommended: the node takes the collection of the surface it supports, found by reading the observation (by me, no model call); where it supports two collection surfaces, it is repeated for each; where I cannot tell, it is held for you. Right?

**Q3. How a missing role is determined** (15,457 nodes with a surface have none). Roles cannot be set by script: they are a reading of the observation. Recommended: only nodes in scope are assessed, by the plan's method (by hand, in verse batches, with before and after); the characteristic is the word the observation is about, a qualifier a word that shapes it, and a supportive entity or other node is object, relational_target or enactment; a node I cannot judge is held. Or do you want a rule that a class takes a default? Please say which.

**Q4. A node with no verse_lexical_id and two or more matching occurrences** (the word twice in a verse, or several Strong's codes). Recommended: the observation's own Strong's code decides where it names one; otherwise the node is split into one node per occurrence if the observation covers them all (N7), or held for you.

**Q5. An observation whose nodes are only entity or other** (no collection surface to support): it cannot reach a collection. Recommended: it is malformed under N5, so I draft a restatement with its collection-surface node, or withdraw it with a reason, and you approve each restatement. Right?

**Q6. Registration form.** Behaviour rules (class study_method) for N1 to N15, plus the column text and expectation of ib_node updated to say how each column is determined, plus a cfg_setting for scope S1. Do you want it in this form, or the node rules in a separate rules table?

## 5. After your answers

I register the rules through the app's logged config path (apply_logged), with the same rows recorded in BUILD.md, and the sources named. Then I build the validation process: a read-only checker that lists every node and observation by the rule it breaks, with counts and samples, and the flag; then the fixing by class as in plan v3 section 5. Nothing is changed in the study data before the checker report has been read by you.
