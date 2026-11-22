# Validation pilot, part 1: the read-only pull and structural tests on thought

Escalation #2538, 2026-11-22. Plan: `outputs/escalation/2538-validation-step-plan-v8-20261122.md`. Nothing was written to the live database or to the copy; the pull only reads.

## What was run

- A named rollback point of the live database: `iba/app/db/snapshots/kept/iba-20261122T055813Z-pre-2538-validation-pilot.db` (`dbsnapshot --named`).
- A test copy of the live database (`dbsnapshot --copy-to`, SQLite backup API) in the session scratchpad.
- `python -m iba.app.tools.temp_2538_validation_pull <copy> thought`: finds the scope (a, b, c) of collection 56 and runs the structural tests of the plan. It is a temporary script (`governance.scripts_and_routines`), not yet a registered routine.

## Prediction and result

| count | predicted (from earlier read-only queries) | result on the copy |
|---|---|---|
| a) observations with a node carrying the collection | 785 | 785 |
| b) observations with a node on its 351 verses | 1,180 | 1,180 |
| c) observations on a member surface with its lettered strong | 775 | 775 |
| union of a, b and c | 1,180 | 1,180 |
| traced nodes (stage 4) | 827 | 827 |

## Structural findings for thought's scope (1,180 live observations; 15,784 word nodes and 827 traced nodes)

- **Live observations by stored stage:** prior-capture 419, layer-3 217, lexical 202, layer-2 132, strand-reading 79, engagement 60, verse-reading 27, char-answers 26, layer-1 14, char-reading 3, char-subgroup 1.
- **Word nodes missing a required column: 1,212 of 15,784.** By column: role 628, collection_id 617, morph_code 14, verse_lexical_id 5, surface 2, strong 2.
- **Where they sit:** prior-capture 488 nodes missing collection_id (131 observations hold one) and 3 missing verse_lexical_id; strand-reading 486 missing role and 44 missing role and collection (79 observations); engagement 80 missing collection_id; char-answers 56, verse-reading 29 + 3, char-reading 8 and char-subgroup 1 missing role. The current-method stages carry only morph_code gaps: layer-2 6, layer-3 3, layer-1 2 (and 1 on lexical).
- **Word nodes with no subgroup_id: 11,457** (reported, not judged; empty is right where the surface is not placed).
- **Live traced nodes pointing at a deleted observation: 0.** The 93 dangling traces found earlier are in other collections' scope.
- **Exact-text duplicate groups (same stage, same text): 0.** Duplicates by meaning, which is the plan's test, are found by reading.
- **Nodes reaching into other collections: 9,577 nodes in 158 collections.** Per principle 1 these observations are in the scope and each node must be traceable when the other collection is analysed.
- **Observations with no live node: 63 in the whole table; none is in thought's scope by its own strong.** They are in no collection's scope by structure and are left to the reading (d).

## What the synthetic test proved

A small in-memory database with known defects: the scope (a, b and c, including an orphan found by its own strong), an observation with no live node, a word node missing role and collection, a trace to a deleted observation with no replacement, a same-text duplicate differing in spacing and case, and a node reaching into another collection. Expected and result agree on all (`synthetic PASS`). The first synthetic run failed: an observation with no live node was never in scope, because scope is found through live nodes. The pull now also finds such an observation by its own strong, and counts the rest.

## What this shows

- The completeness gap the researcher named is real in the older stages: of the 1,212 incomplete word nodes, all but 11 are in the older pipeline (prior-capture, strand-reading, engagement, verse-reading, char-answers, char-reading, char-subgroup); the current stages have only 11 morph_code gaps.
- The structural tests find completeness and reference defects but cannot find a duplicate by meaning, a statement that is untrue, or an observation that is neither evidence nor inner being; those are the reading.

## Not done

The marker column, the trace rule, the ruling state, the consumption record and the function that annotates a deleted observation are not built. No observation or node was read for truth or meaning. The routine is not yet a registered step with a PowerShell entry point, a test plan, or a USER-GUIDE entry (B:41, B:42, B:46, B:62); those come with the promotion of the pilot.
