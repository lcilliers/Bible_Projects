# #2487 — Salvaging the nodes: plan for decision

Plan only. Nothing built, nothing changed in iba/app/db/iba.db. Your direction, verbatim, is on #2487; in short: do not throw the work away; salvage it methodically; no sweeping updates without verifying the effect and all the facts; keep the base rules for observations and nodes in view; expect updates, conflicts, duplicates to withdraw and nodes to split; flag each node validated, and repeat until every node is.

## 1. The base rules I will hold every node to

These are stated here so you can correct them. Rules 1 to 9 are in config today; rules 10 to 13 are your rulings of 2026-11-12 and are not yet in config, so registering them is the first build step (B:31, governance.rules_must_be_config_driven).

| no | rule | source | what it asks of a node or observation |
|---|---|---|---|
| 1 | One finding per observation, applied by its nodes | cfg_setting reading.observation_parts | The observation holds the finding (text, meaning, implication, basis, tag, route, parts); a node only says where it applies: verse, word, role, reading. |
| 2 | Per occurrence | B:121 | A node sits on one occurrence, one verse_lexical row. A node that cannot be placed on one occurrence goes to its cluster's anomaly group and is cleared by hand. The same finding over several verses stays one observation with an anchor verse. |
| 3 | A node has the parts its kind needs | cfg_setting reading.observation_parts, gap type observation_part_missing | A node has the word's role; a party finding has its route; a qualification has both qualifier and characteristic. Something present but wrong is not resolved. |
| 4 | Roles | cfg_setting reading.node_roles | Roles that count: characteristic, qualifier (relevant); object, relational_target, enactment (bears on). |
| 5 | A finding the verse no longer supports is withdrawn | gap type observation_unsupported | Withdraw the node for that verse, or the finding everywhere, with a reason in ib_observation_change. |
| 6 | Cluster is loose | B:70 | A reading never moves a word out of a cluster. |
| 7 | Subgroup is settled only in the claims step | B:122 | The observe reading changes no subgroup. |
| 8 | Surface is the lens | B:110 | The verse_lexical surface is read per Strong's. |
| 9 | Let scripture speak | B:69 | Observation text states what the verse says; no imputed pattern. |
| 10 | A verse-related node has a surface | researcher, 2026-11-12 | Else it comes to you to decide if it has any value; I decide nothing about it. |
| 11 | A surface in a collection puts that collection on the node | researcher, 2026-11-12 | The node carries every collection its surface is in. |
| 12 | A verse-related node in no collection must have a surface in group being (`entity`, to be confirmed) or other | researcher, 2026-11-12 | Else it is an exception for you. |
| 13 | Cluster and subgroup of a node are not analytic | researcher, 2026-11-12: "no longer of analytic consequence or value, and often is misleading" | Kept as history; reports read the collection. |

Every change I make is written through apply_logged (rule 75), with a row in ib_observation_change (node, column, old value, new value, reason, run) so each change can be read and reversed. B:44 applies: a point that needs a new decision stops and comes to you; I do not answer it inline.

## 2. What the data shows (read-only, 2026-11-12)

Counts of live nodes (78,099) against the rules; each is a count, not a judgement of which node is right.

| finding | nodes |
|---|---|
| created in one bulk write on 2026-10-26 by the prior-capture stage | 52,064 (two thirds of all) |
| on observations still in `draft` | 72,190 |
| live nodes on a withdrawn observation (the observation is deleted, the node is not) | 4,962 |
| exact duplicates (same observation, verse, Strong's code, surface, role): groups / extra rows | 2,027 / 2,317 |
| duplicates on the same verse_lexical row and role | 351 groups / 423 extra rows |
| no role | 25,052 (11,043 verse-reading, 4,236 prior-capture, 3,991 strand-reading, 3,916 engagement, others) |
| no verse_lexical_id, word occurs more than once in its verse (placement or split candidates, rule 2) | 4,505 |
| verse-related with no surface (rule 10) | 10,179 |
| surface in no collection and not in group entity or other (rule 12) | 7,045 |
| surface with no surface_term row | 458 |
| observations with no live node | 63 |

Nodes were written in waves (2026-09-17 to 09-23; 10-22 to 10-30; 11-09 to 11-11). The history of the bulk updates that made it worse is not yet read: that is step A below. The counts are not yet cross-checked against one another (a node can be in several rows).

## 3. The flag

Four columns on ib_node, added by the documented procedure (cfg_table and cfg_column meaning rows, B:123):
- `validation_state`: `unvalidated` (default, every node today), `validated`, or `held` (waiting on you).
- `validated_at` and `validated_run_id`: when and by which run.
- `validated_rule_set`: the version of the rules in section 1 it was validated against, so a node validated under old rules shows up again when a rule changes ("repeat until every node is fully validated").

A node returns to `unvalidated` whenever anything other than a validation run changes it. A withdrawn node (deleted = 1, with reason) leaves the count; a split makes new nodes, each `unvalidated` until checked.

## 4. The method: one verse at a time

The unit is one verse with all its nodes and their observations together, because duplicates, conflicts and splits are only visible side by side (B:116: the verse is read first). Each round:
1. Pull the verse's nodes and observations as they stand.
2. Check each node against rules 1 to 13; write down every finding: conflict, duplicate (and which is kept), placement or split, missing part, missing surface, missing collection.
3. Write the proposed action per node: validate as it is, change a field (before and after), withdraw (reason), split (what the pieces are), or hold for you.
4. Predict the counts after the actions. A round does not apply if the prediction cannot be made.
5. Apply on a copy of the database first (dbsnapshot.copy_db), compare actual against predicted; only on a match apply to the live database, after a named rollback snapshot.
6. Set the flag; re-run the checks on the verse; record on this escalation.
7. Repeat for the next verse. Report to you the count of nodes by state after each batch.

No bulk update runs across the table. A class of change (for example withdrawing the 4,962 nodes on withdrawn observations) is applied in bulk only after the same class has been done by hand and proven on a pilot, and then its before and after counts are checked against the prediction; if they differ it stops and is restored.

## 5. Order of work

- **A. Read the history** (read-only): what each bulk write did (ib_observation_change has 2,569 rows; BUILD.md entries; #2273 D6, #2286, #2296; the 2026-10-26 prior-capture write), so we know how the nodes got where they are.
- **B. Build the flag and the checker** (no node changed): register rules 10 to 13 in config; add the four columns; build one repeatable check that reports each rule per node, filling the flag only from a validation run.
- **C. Pilot** on a small set of verses, with every action shown to you before it is applied; the defect classes found on the pilot decide what can later be done as proven batches.
- **D. Rounds** until no node is `unvalidated` or `held`.
- **E. Close**: the checks run clean on the whole table; the rules are in config and documented (BUILD.md, USER-GUIDE.md, GOVERNANCE.md).

#2484 (collection on the node), #2485 (verse_lexical_id fill) and #2486 (claims to collections) become rules and steps inside this programme, in the order you set; none is built on its own.

## 6. What you are asked to approve or decide

1. **The base rules** in section 1: correct, complete? Is "being" the surface group `entity`?
2. **The unit** of validation is one verse with its nodes and observations (alternative: one observation).
3. **The flag**: the four columns and the three states in section 3 (alternative: a separate validation table, leaving ib_node unchanged).
4. **The approach**: pilot with every action shown to you; proven classes later in bulk with verified counts (alternative: every change shown to you, never in bulk).
5. **The order** A to E, and whether #2484, #2485 and #2486 fold into it as stated.

On approval I start with step A (read-only) and report before building anything.

Limits: the counts come from one read-only pass and overlap; none of the findings has been checked node by node; every classification here is inferential (B:4) until the rounds confirm it.
