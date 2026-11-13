# Retiring cluster and subgroup from the node and observation code (design v1)

Escalation #2495. Status: **design for your decision; nothing built, no rule retired, nothing changed in `iba/app/db/iba.db`.** Everything below is read from the live config and the code, 2026-11-13.

Your ruling (#2484, item 4.4, verbatim): *"clusters and sub groups have served their purpose in the creation and establishment of the collections. notes and observations should not have any part to play with clusters and sub groups. all rules associated to the maintenance of clusters and sub groups in the observations process must be retired."* The rules for nodes and observations (behaviour rules 130 and 131) already say it. What is left is the rules and code that still enforce the old way, and a retirement of a rule while the code still enforces it would leave config and code in disagreement (B:62). So each rule below is retired **in the same unit of work as the code that enforces it**, or with the process it belongs to.

Already done (BUILD 514): behaviour rules 70 and 122 and method rule RA-01 retired; behaviour rule 121 restated.

## 1. What is still there

Live data: 60,424 of the live nodes hold a `cluster_subgroup_code` and the nodes carry 93 different `cluster_code` values. These stay as history (ruling N12): reports read the collection.

### 1.1 Rules (live config)

| Rule | What it says | Enforced by | Belongs to |
|---|---|---|---|
| behaviour rules 117 (subgroups are surface groups), 118 (surface mapping conditions), 119 (scope enters through the surface and its subgroups), 120 (scope home and multiplicity) | the subgroup structure of a cluster, how it is mapped, how a reading scope is built from subgroups and a home cluster | `iba/app/lib/surfacemap.py`, `iba/app/lib/versescope.py`; `iba/app/ps/Surface-Map.ps1`, `iba/app/ps/Reading.ps1 -Step Open` (it takes one subgroup as its home and refuses an unmapped M cluster) | the cluster reading process, which the reading by collections (#2448) replaces |
| method rules RO13 (segment a large subgroup), RM-03 and RO8 (no whole-cluster reading) on `reading.open` | how a cluster or subgroup scope is segmented | `iba/app/lib/reading.py` (Open) | the same process |
| method rules CP-07 (node classification: strong, occurrence, cluster and subgroup from the tables), CP-09 (clusterless documents last), CP-10 (nodes on the M-coded words only) on `prior_capture.record` | how the old capture tool placed nodes | `iba/app/lib/priorcapture.py`, run as `iba/app/ps/Prior-Capture.ps1` | the old capture tool |
| method rules NR-01 (resolve from the tables, the sub_group of the surface in the node's cluster) and NR-04 (subgroup only where the occurrences agree) on `node_resolve.apply` | the node sweep that fills occurrence, morph code and sub_group | `iba/app/lib/noderesolve.py`, `iba/app/ps/Node-Resolve.ps1` | the node sweep |

### 1.2 Code that still makes a node or observation depend on them

| Where | What it does |
|---|---|
| `iba/app/lib/observationrecord.py` (`check`, `write`, `subgroup_code`, `word_clusters`, `modify_node`) | a node needs a cluster: it **refuses** a Strong's code in several clusters unless the cluster is named, writes `ib_node.cluster_code` (NOT NULL) and looks up a subgroup; `modify_node` may set `cluster_subgroup_code` and `cluster_code` |
| `iba/app/lib/reading.py` (Observe, Record, 6 uses of the subgroup) | the sheet and the record carry the subgroup of each occurrence |
| `iba/app/lib/recordingpass.py`, `iba/app/lib/strandreading.py` | the writers of the older stages (verse-reading, strand-reading): `recordingpass.py` reads and writes the cluster and the subgroup of its nodes, `strandreading.py` the cluster |
| `iba/app/lib/priorcapture.py`, `iba/app/lib/noderesolve.py`, `iba/app/handlers/noderesolve.py` | as in 1.1 |
| `iba/app/lib/collectionevidence.py`, `iba/app/lib/versecollate.py`, `iba/app/lib/engagement.py` | read the subgroup (one or two places each) |
| `iba/app/lib/draftapply.py` (mine, #2498) | fills the history cluster so the NOT NULL holds; writes no subgroup |
| config: `cfg_setting reading.verse_loop` (`node_set` lists `cluster_subgroup_code`, `cluster_code`) and `reading.observation_parts` (`node` lists `cluster_code`) | which columns a reading may modify or record on a node |
| config: `ib_node.cluster_code` NOT NULL in `cfg_column` | the writers must give a value |
| test `iba/app/tools/temp_2320_analysis_phase_1_test_run.py` line 216 | asserts `standalone` is not a role, which behaviour rule 130 and `reading.node_roles` now contradict |

The cluster and subgroup code in the cluster pipeline itself (`clusterstatus.py`, `handlers/cluster.py`, `lexical.py`, `surfacemap.py`, `clusterreport.py` and others) is the **cluster work**, not the observation process, and is outside this item.

## 2. The plan, in three stages

**Stage 1: the writers stop depending on cluster and subgroup (code and config, one unit of work, tested on a copy).**
1. `observationrecord.check` and `write`: a node no longer needs a cluster and no longer refuses a Strong's code in several clusters; no subgroup is looked up or written; the node's collection is set from its surface by the own-row rule (this is also open point D5 of #2484). `modify_node` stops offering `cluster_subgroup_code` and `cluster_code`.
2. `reading.py` Observe and Record, `recordingpass.py`, `strandreading.py`, `collectionevidence.py`, `versecollate.py`, `engagement.py`: stop reading or writing the subgroup on nodes and observations.
3. Config: remove `cluster_subgroup_code` and `cluster_code` from `reading.verse_loop` `node_set` and from `reading.observation_parts` `node`; settle `ib_node.cluster_code` (decision Q1).
4. Fix the test at line 216 (a recognised role, `standalone`, is a role) and add cases for the new behaviour.
5. Reword behaviour rule 130's column list and `cfg_column` text for `cluster_code` and `cluster_subgroup_code` ("history, written by no process").

**Stage 2: retire the tools that only served the old way (config retirement, no code left enforcing).**
1. The old capture tool: retire work package `prior-capture` (its steps inactive, `Prior-Capture.ps1` moved to the retired scripts), with method rules CP-01 to CP-10. It is replaced by the reading with the documents' lines (#2448) and the loader `Draft-Apply.ps1`. The table `prior_capture_line` and the documents' index stay as history and as the old answer shown on the sheet.
2. The node sweep: remove its subgroup part (rule NR-04 retired, NR-01 reworded to occurrence and morph code only), or retire the whole sweep (decision Q3).

**Stage 3: with the reading by collections (#2448), not before.** Behaviour rules 117 to 120 and method rules RO13, RM-03 and RO8, with `Surface-Map.ps1` and the Open step's subgroup home. They govern the cluster reading, which still runs until #2448 replaces it; retiring them now would leave `Reading.ps1 -Step Open` enforcing what the config no longer says. They are listed on #2448 as part of its change list.

## 3. Test plan (each run on a copy first, results in the build's resolution; B:46)

| Case | Expected |
|---|---|
| a node on a Strong's code in two clusters, no cluster named | written (before: refused); no subgroup written |
| a node on a word with no cluster | written; no error |
| a node written through the reading Record | carries `collection_id` of its surface (own-row rule) |
| `modify_node` with `cluster_code` or `cluster_subgroup_code` | refused: not a modifiable column |
| the sheet (Observe) for a verse | no subgroup column; existing observations, roles and collections shown |
| the pilot loads (`2498-pilot-load`, `2498-fear-roles-load`) re-checked | still nothing to change |
| the node checker before and after | no new finding; nodes and observations unchanged |
| `iba/app/tools/temp_2320_analysis_phase_1_test_run.py` | passes with standalone a role |
| `Config-Maintenance.ps1 -Step Validate` | coherence passes; no rule enforced by code that no longer enforces it |
| stage 2: `Prior-Capture.ps1` | refused as retired; `Prior-Capture.ps1 -Step Report` no longer in the worksheet |

## 4. Decisions for you

| # | Question | Options | My recommendation |
|---|---|---|---|
| Q1 | `ib_node.cluster_code` (NOT NULL, history) | a) make it nullable (rebuild of `ib_node`, 68,000 rows) and write nothing for new nodes; b) keep NOT NULL and fill it as history with the word's own cluster or the document's | **a** for a clean break; **b** is the cheaper step and keeps every report as it is. Either works with stage 1 |
| Q2 | the stages | a) the three stages as above; b) all in one pass, including the cluster reading rules now | **a** (b leaves `Reading.ps1 -Step Open` enforcing retired rules) |
| Q3 | the node sweep | a) remove its subgroup part and keep the sweep for occurrence and morph code; b) retire the sweep entirely (its work was done by the 2484 migrations) | **a** (89 nodes still lack an occurrence) |
| Q4 | the old capture tool | a) retire it with CP-01 to CP-10; b) keep the code, retire only CP-07, CP-09, CP-10 | **a** |
| Q5 | order | a) stage 1 now, stage 2 straight after, stage 3 with #2448; b) stage 1 only now | **a** |

After your decisions I build stage 1, rehearse it on a copy with the test plan, and show you the results before the live run.
