# #2487 — Salvaging the nodes: plan v2 for decision

Plan only. Nothing built, nothing changed in iba/app/db/iba.db. Revised to your points of 2026-11-12 (verbatim on #2487). The first version is archived.

## 1. Scope

Only verses included in a collection are in scope. Verses, observations and nodes that bear on no collection are not touched now, and the rules are not applied to them. Where a verse has no collection surface and only entity or other surfaces, the whole verse is out of scope. Where an in-scope verse also has entity or other surfaces, those surfaces are part of the scope and are included in the verse's observations. Nothing is changed for out-of-scope material; it is only marked as out of scope.

How big the scope is depends on how "included in a collection" is defined (counts from iba.db, read-only; a verse counts if one of its words is a surface of a member base):

| definition | collection surfaces | verses in scope (of 29,762) |
|---|---|---|
| all member tiers (core, synonym, opposite, gathered, phrase), own and shared words | 2,965 | 26,101 |
| all member tiers, own words only | 2,965 | 25,597 |
| core, synonym, opposite | 1,753 | 25,361 |
| core only | 741 | 18,065 |

Verses that carry any live node today: 13,384. So by the widest definition nearly every verse is in scope; whether that is what you mean, or whether scope is the collections you have taken up (B:127), is decision 1.

## 2. Rules for nodes and observations, as I now hold them

Your words are the source for the rows marked "R". Rules 6 and 7 of v1 (cluster loose, subgroup in the claims step) no longer apply: the collection replaces them.

| no | rule | what it asks |
|---|---|---|
| R1 | Every collection surface has at least one finding | A finding is an observation plus a node. A node cannot exist without an observation; an observation must have at least one active node; a node has only one surface; an observation usually has several nodes and a verse several observations. The node is the cross-reference from the verse to the element the observation evaluates. |
| R2 | The collection is on the node; clusters are no longer relevant | Any in-scope node without a collection is an error. An observation not tied to a verse or surface should be rare; it is probably malformed and should be restated specifically, since a generic statement usually applies to a group of verses, which is captured by a node for each verse and surface it applies to. Malformed observations are the root cause of most of the present issues. |
| R3 | Observation parts | Parts vary by observation and by what the verse's analysis needs, and have changed focus over time. No aim to make them consistent across the scope. |
| R4 | Roles | characteristic and qualifier (relevant); object, relational_target and enactment (bears on): cfg_setting reading.node_roles. |
| R5 | A finding the verse no longer supports is withdrawn | The node for that verse, or the finding everywhere, with a reason in ib_observation_change. |
| R8 | Surface is the lens | The verse_lexical surface is read per Strong's (B:110). |
| R9 | Scripture speaks | An observation is never a repeat of the verse text; it is an application or analytic statement interpreting what the verse says (B:69). |
| R10 | One node for each surface an observation covers | Where an observation covers several surfaces, each has its node. |
| R11 | The node carries every collection its surface is in | |
| R12 | Entity and other surfaces | A verse with only entity or other surfaces is out of scope; in an in-scope verse they are part of the scope. |
| R13 | Cluster and subgroup on a node are not analytic | Kept as history; reports read the collection. |

Config holds R4, R5, R8 and R9 now. R1, R2, R10 to R13 and the scope are your rulings and must be registered in config first (B:31, governance.rules_must_be_config_driven). Every change is written through apply_logged with a row in ib_observation_change (node, column, old value, new value, reason, run); a point needing a new decision comes to you (B:44).

## 3. What the data shows inside the scope (all member tiers, own and shared; counts overlap)

| finding | count |
|---|---|
| nodes on in-scope verses | 76,400 (46,423 with a surface in a collection); with the 1,653 and 46 below this is all 78,099 |
| in-scope nodes with no surface | 9,596 |
| in-scope nodes whose surface is in no collection | 20,381 (entity 8,298; other 4,904; behaviour 1,770; inner_being_state 4,982; no surface_term row 426; not judged 1) |
| nodes on out-of-scope verses (left alone) | 1,653 |
| nodes with no verse at all | 46 |
| observations with all nodes in scope / some / none | 19,618 / 857 / 260 |
| in-scope observations whose nodes all lack a surface (candidates for restatement, R2) | 1,240 |
| observations with no live node, so against R1 | 63 |
| live nodes on a withdrawn observation, so against R1 | 4,962 |
| collection surface words with no node at all | 1,182 of 2,965 |
| own-kind occurrences of collection surfaces that have a linked node | 16,077 of 65,267 |
| in-scope observations with at least 90% of their words in their verse's text (R9; rough detector, to be read, not trusted) | 557 of 16,155 |
| exact duplicate rows (whole table) | 2,317 extra rows in 2,027 groups |

The two counts under R1 give a different answer depending on whether "every collection surface has a finding" means per surface word or per occurrence: decision 2.

## 4. The flag

Four columns on ib_node (documented procedure, cfg_table and cfg_column meaning rows, B:123): `validation_state` (`unvalidated` default, `validated`, `held` for you, and `out_of_scope` for nodes outside the scope), `validated_at`, `validated_run_id`, `validated_rule_set` (version of section 2, so a node validated under old rules appears again when a rule changes). A node returns to `unvalidated` when anything but a validation run changes it. A withdrawn node leaves the count; a split makes new nodes, each `unvalidated`.

## 5. The method

One verse at a time for checking: its nodes and observations together, so duplicates, conflicts, splits and missing nodes are visible side by side. A malformed observation (R2) is repaired as one piece of work across the verses it applies to, since restating it creates its nodes. Each round:
1. Pull the verse's nodes and observations as they stand.
2. Check each against section 2; write down every finding.
3. Write the action per node or observation: validate as it is, change a field (before and after), withdraw (reason), split, add a missing node, restate an observation (the restatement drafted by me, approved by you), or hold for you.
4. Predict the counts afterwards; if they cannot be predicted the round does not apply.
5. Apply on a copy first (dbsnapshot.copy_db), compare actual with predicted, apply to the live database only on a match and after a named rollback snapshot.
6. Set the flag, re-run the checks on the verse, record the result on #2487.
7. Repeat, reporting the count of nodes by state after each batch.

No sweeping updates. A class of change is applied in bulk only after the same class has been done by hand and proven on a pilot, and then with before and after counts checked against the prediction; a mismatch stops it and restores the snapshot.

## 6. Order

0. Settle the scope (decisions 1 and 3), then register the rules in config.
A. Read how the bulk writes made it worse (read-only): ib_observation_change (2,569 rows), BUILD.md, #2273, #2286, #2296, the 52,064-node prior-capture write of 2026-10-26.
B. Build the flag and the checker; no node changed.
C. Pilot on a small set of verses, every action shown to you.
D. Rounds until no in-scope node is `unvalidated` or `held`.
E. Close: checks clean on the whole scope; rules in config and documented.

#2484, #2485 and #2486 fold in as rules and steps, in the order you set.

## 7. What I need from you

1. **Scope.** Which definition of "included in a collection" (section 1): all collections, or the collections taken up in the study? If the latter, name them or the rule that picks them.
2. **R1 unit.** Must every collection surface word have a finding (1,182 of 2,965 have none), or every occurrence of it in the verses in scope (16,077 of 65,267 have a linked node)? A finding on one occurrence of a word is not necessarily a finding on the others (B:121).
3. **R2 and R12 together.** In an in-scope verse an entity or other surface is in scope, but R2 says an in-scope node without a collection is an error, and an entity surface is in no collection. Which collection does such a node carry: (a) every collection of the verse's collection surfaces, (b) the collections of the observation's own collection-surface nodes, or (c) none, with these nodes exempt from the collection rule? I recommend (b), because it follows the finding and not the verse.
4. **Malformed observations (R2).** I draft each restatement and the nodes it needs, and you approve each; the alternative is that you restate them. The 1,240 in-scope observations with no node surface are the first list, to be read before they are called malformed.
5. **Carried from v1.** The flag and its four states; the pilot-then-proven-bulk approach; the order 0, A to E, with #2484 to #2486 folded in.

Limits: counts come from one read-only pass on 2026-11-12 and overlap; scope by surface text is inferential (B:4) until you define it; the verse-text detector is a rough word overlap and flags only candidates.
