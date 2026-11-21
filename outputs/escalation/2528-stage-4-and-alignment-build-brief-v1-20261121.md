# #2528 Build brief for the developer-mode session: stage 4 and the alignment of stages 1 to 3 (v1, 2026-11-21)

Written so that a fresh Developer Mode session can start from this file alone. It follows the researcher's instruction of 2026-11-21 (verbatim): "it looks like you know what to do so everything is in place and clear. make sure that you prepare yourself for a develop-mode session which will allow you to make all the adjustments and build stage 4." The audit it rests on is outputs/escalation/2526-stages-1-to-4-readiness-audit-v1-20261121.md (findings F1 to F12). The pick-up point and stage ends are in outputs/escalation/2527-where-the-programme-is-picked-up-and-the-stage-end-v2-20261121.md. The Programme book (Workflow/Programme/programme_prose/wa-programme-prose-extract-20261121.md, section Programme flow) states stage 4 as required, to be fully specified and built.

## 1. The end state

When this session is done:
1. Stage 4 exists as built steps of the layered reading, on the same ledger, gates and checks as stages 1 to 3, with its method rules, configuration, write grants, table meanings, guide, tests and Programme prose all in place.
2. The adjustments to stages 1 to 3 that the audit found (F3, F5, F6, F7, F8, and the withdrawn thought grouping F2) are made.
3. Nothing of the study is run: no row is recorded on any collection. The study work is #2526, in a standard session, after this build.

## 2. Start of the session

The researcher types `/developer-mode` as the first message of a fresh session (CLAUDE.md). Then: read this file, the audit, the two sections of the Programme book named above, and the files in section 8. Run the tests of section 9 on database copies first, to see the baseline (47, 24 and 12 pass; the collection index test stops on the live data, F6).

## 3. Work list, in order

| No | Work | Files and config | Done when |
|---|---|---|---|
| B1 | Read iba/app/lib/reading.py in full (the part this session only read by structure), especially _validate_sheet (the rules of a filled verse sheet), _write_verse, the item and role handling, and iba/app/lib/observationrecord.py (orec: rules, kinds, node_role_groups, modify, delete). Write the stage 4 design as outputs/escalation/2528-stage-4-design-v1-20261121.md from section 4 below, corrected by what the code shows. The researcher reads it in the session before B5 starts. | reading.py, observationrecord.py | The design file exists and the researcher has read it |
| B2 | Clear the withdrawn thought grouping (F2): retire the ten subgroups and return the 116 placed and 81 isolated index rows of thought to unplaced, clear the group on the thought nodes, as an archived one-run migration (iba/app/migration/archive/, rule 96) with the run kept in surface_event. The researcher ruled that nothing previously done stands (#2515 Q3). Check with LayerOpen -Check that step 1.1 of thought then refuses for want of a grouping. | collection_subgroup, collection_subgroup_surface, ib_node.subgroup_id | LayerOpen -Collection thought -Step 1.1 -Check names "the collection has no subgroup" and the unplaced surfaces |
| B3 | Align the stage numbers (F3): one wording of which steps belong to which stage in rule 132 (cfg_behaviour_rule), cfg_setting layer.reading (stages), the guide and the Programme book. The Programme book's account is the base: stage 1 is S1; stage 2 is the grouping; stage 3 is 1.1, 1.2, 2.1; stage 4 is the new steps. Align rule GP-01 with the Programme book (F8): the grouping is judged from the dictionary meaning without the verses, as the pull gives it. | cfg_behaviour_rule 132, cfg_method_rule 243, cfg_setting layer.reading | One wording in all four places; lexicalalignment check passes |
| B4 | Fix the collection index test (F6): it builds its own collection as the 2505 test does and no longer depends on live thought. | iba/app/tools/temp_2503_collection_index_test_run.py | 2503 test passes on a copy |
| B5 | Build stage 4 (section 4 and 5): configuration, code, rules, tests. | See section 5 | Section 9 acceptance |
| B6 | Retire the cluster and subgroup scope of the old reading (F5), in the same unit of work as B5: rules 119 and 120 and method rules RM-03, RO8 and RO13 (reading.open), the guide line that waits for #2448, reading.home_cluster and the Open step of iba/app/ps/Reading.ps1. Decide from B1 what stage 4 reuses of reading.py and what is retired; whatever the narrative steps (Synergy, Apply, Narrate, Publish) still need stays, re-scoped. Record the breach of #2448 v16 as closed. | iba/app/lib/reading.py, iba/app/ps/Reading.ps1, cfg_behaviour_rule 119 and 120, cfg_method_rule | No active rule or guide line describes a cluster or subgroup reading as current; the alignment check passes |
| B7 | Guide and records: a short run order for a collection in iba/app/USER-GUIDE.md (Index, GroupPull, GroupRecord, NodeGroups, then each step with open, pull, record, check) and the stage 4 steps; BUILD.md entries naming every file changed (SC10); GOVERNANCE.md if a rule changed; iba/docs/project-map.md; the Programme book sections that now say stage 4 "is not built" (Programme flow stage 4 row, The collection reading, Claims and synthesis across collections, The analytical grouping) changed to describe it as built, through Prose.ps1. | the listed files | Session-close clean |

Config changes go through Config-Maintenance.ps1 -Step Propose; Developer Mode is exempt from the approval gate (cfg_behaviour_rule developer-mode-scope-and-conduct). A new enum value is a change to controlled vocabulary: record it in the BUILD.md entry.

## 4. Stage 4: the recommended design

This is the design from this session's reading of the configuration and of layerreading.py. B1 corrects it against the code. Basis for each choice is given; the researcher's words are the Programme book's: the inner-being observations are made from the stage 3 observations, "for specific behaviours, for groups of behaviours, and across subgroups and collections", the same subgroups are used, a stage closes before the next opens, every aspect is answered by an observation with its nodes or a recorded none with its reason.

**Three steps, in layer 3, each closed before the next opens, and none opens before stage 3 is closed for the collection** (the Programme book: "stage 4 is not opened until stage 3 is complete"):

| Step | Level | Ledger row | Item | What it leaves |
|---|---|---|---|---|
| 3.1 | Specific behaviours | One for each subgroup and verse in which the subgroup has an occurrence. Subject: the verse. | verse-working | For that verse, the findings of the inner-being reading for the subgroup's occurrences: one observation for each applicable item of the old reading (role of the characteristic and what a qualifier gives it in place, polarity, object, enactment, party with its route, circumstance, operation with its chain, flag), each with its nodes and the role of each node |
| 3.2 | Groups of behaviours | One for each subgroup. | subgroup-working | What the subgroup's workings show across its verses (modes, states, transitions, the operations it takes part in), as observations resting on named 3.1 observations, with nodes that are occurrences of the subgroup |
| 3.3 | Across subgroups and collections | One for each pair of subgroups that share at least three verses, and one for each partner collection that shares at least three verses with a subgroup (the thresholds of stage 3). | interworking | How the subgroups, and the subgroup and the partner collection, work together in the verses they share, with the nodes of both |

Basis: the three levels are the Programme book's. The row grain for 3.1 is the verse because the old reading's verse loop and its item rules (RS-10, RG-01 to RG-25) were written per verse and per characteristic, so the existing rules apply unchanged; it is also the grain at which a node ties the finding to the text. The thresholds of 3.3 are the ones the Programme book and layer.reading already give stage 3.

**What is taken out of the old nine items, because stages 1 and 3 do it:** the meaning and face of a word (stages 1 and 3.1 of the lexical layers), and the qualifier by the grammar (step 2.1). **What stays:** the rest, as above. This is the split in section 4 of the audit.

**Roles and kinds.** The nodes of a stage 4 observation carry the roles of reading.node_roles (characteristic, qualifier; object, relational_target, enactment; standalone), chosen for each node by the reading, not fixed for the row as stages 1 to 3 do. The kinds are those of reading.observation_parts that the items name; the route (A, B or C) is required where the item says so (party), allowed for link, refused otherwise: reading.observation_rules already states this.

**The recorder.** Extend layerreading.record, derive, expected_nodes, pull and check, rather than write a second recorder. They are driven by the item definition (kind, kinds, none_allowed, member_role, partner_role, route, multi, tie_to_verse, grounds_in, subset), and already refuse a problem anywhere in the file, write in one transaction, withdraw an earlier observation on a re-record, and validate by re-deriving from the tables. What is added: a per-node role in the fill (a list of the occurrence and its role), the findings list of the verse-working row (like the senses list of word-sense), and the check that each applicable item is answered or recorded as none with a reason (RS-10).

**The earlier observations.** The pull of a stage 4 row shows the existing inner-being observations on the verse (the stages Analysis_phase_1, strand-reading, char-*, verse-reading, prior-capture, engagement, as the S1 pull already shows the lexical ones). The reading adopts, modifies, deletes with its reason or leaves each one (RS-04, RW-01, RW-09): an old observation is improved, not replaced, and one that cannot be made to comply with rules 130 and 131 is retired with its nodes and its reason. The documents that name the verse are read for that verse only (#2448 v11; #2498 design v4 sections 2, 3, 7, 8), as lines on the row.

**The interventions.** A setting (layer.interventions) lists read beyond the verse in its passage, genre and speaker; read outward and not inward from a question; check the original; reclassify a word whose role here is not its collection's (the move is processed so the step reopens); do not force a meaning and never close on "not X"; record a discovery outside the verse separately. The pull carries them on each row as prompts, and a discovery is recorded as a flag finding.

**The grain across several nodes** (the Programme book says how one working across several nodes is one record is not stated). Rule: one observation for each finding, never a duplicate; a finding that applies to several words or verses carries several nodes (RO11, RW-03). The chain of operations is one link-kind observation. This follows rules already in force.

## 5. What B5 adds

**Configuration.**
- cfg_enum ib_observation.stage: the value layer-3.
- cfg_setting layer.reading: stage "3": "layer-3"; steps 3.1, 3.2, 3.3 with their needs (2.1, 3.1, 3.2); the items verse-working, subgroup-working, interworking with their asks; the interventions in layer.interventions; thresholds reused.
- Method rules in the form of LR and GP for the stage 4 steps (the open on its gate, the findings and the per-node roles, none with a reason, the check); the existing RG, RW, RS rules stay and are not restated (rule 3).
- The step registrations: none new if the stage 4 steps run through LayerOpen, LayerPull, LayerRecord and LayerCheck (the Step parameter accepts the new keys; the ValidateSet in iba/app/ps/Collection-Build.ps1 and the usage text change).
- cfg_table and cfg_column: any new column or value described. The ledger (collection_layer_item) needs no new column if the verse is the subject; check that its step and item columns accept the new values.
- iba/app/lib/lexicalalignment.py: the boundary check (no inner-being role, route or kind in a lexical item) applies to steps of layers 0 to 2 only, and a new check asks that every layer 3 item carries a role rule.

**Code.** iba/app/lib/layerreading.py (derive, expected_nodes, pull, record, check, the step definitions), iba/app/handlers/collectionbuild.py (only if the step handling is keyed to the old keys), iba/app/ps/Collection-Build.ps1 (parameters and help).

## 6. Do not

- Do not record a row on any real collection, or run any step of the study, in this session. The working files of 2026-11-21 under _analytics/surfaces/working_files/layers/ are working files, not records.
- Do not run tests on the live database: copy iba.db to a scratch folder and run them there (iba/app/tools/temp_2505_layers_test_run.py takes the copy and a scratch folder).
- Do not change the Programme book beyond describing what is built; stage 5 stays undecided.
- Do not leave a one-run migration in the live folder (#2523): archive it.
- The point-of-use rule hooks show a rule set once per operation and then ask for the call to be re-issued; re-issue it.

## 7. What the researcher reads in the session

The stage 4 design (B1), then the built steps' configuration before the tests are run. Nothing else is asked.

## 8. Files to read first

- iba/app/lib/layerreading.py (794 lines): the whole file.
- iba/app/lib/reading.py: _validate_sheet, _write_verse, observe, record, the item handling.
- iba/app/lib/observationrecord.py: rules, kinds, node_role_groups, modify_node, delete_node, soft_delete_observation, copies_verse, live_text.
- iba/app/lib/lexicalalignment.py and iba/app/tools/temp_2507_alignment_test_run.py.
- iba/app/tools/temp_2505_layers_test_run.py (the model for the stage 4 test).
- cfg_setting layer.reading, reading.observation_items, reading.observation_parts, reading.observation_rules, reading.node_roles, reading.nuance_pointers, reading.observe_prompts.
- cfg_behaviour_rule 130 to 134; cfg_method_rule steps reading.observe, reading.record, reading.open, collection.layer_open, collection.layer_record, collection.layer_check, collection.group_record.
- iba/app/USER-GUIDE.md, the layered reading and the index and subgroups paragraphs.

## 9. Acceptance

1. A new test, iba/app/tools/temp_2528_stage4_test_run.py, in the form of the 2505 test, on a database copy, with a test collection taken through stages 1 to 3 on the copy and then steps 3.1, 3.2, 3.3: the gates refuse until the previous step is closed and until stage 3 is closed; a whole file is refused for a problem anywhere; the nodes carry the roles the reading gave and each has a collection and a subgroup; a route is required where an item says so and refused where it does not; an item answered as none needs its reason; an earlier observation is adopted, modified or retired with a reason; a re-record withdraws the earlier observation; the check re-derives and validates; a change to the grouping reopens the rows.
2. The tests 2503, 2505, 2507, 2509 pass on database copies, with the boundary check updated.
3. The alignment check finds no active step, rule or guide line that names the retired cluster or subgroup reading as current.
4. Collection-Build.ps1 -Action LayerOpen -Collection thought -Step 3.1 -Check on the live database refuses with the stage 3 gate, and the pull for a later step is not possible, proving the live wiring without recording anything.
5. Session-close is clean: BUILD.md, the guide, the project map and the Programme book all state stage 4 as built.
