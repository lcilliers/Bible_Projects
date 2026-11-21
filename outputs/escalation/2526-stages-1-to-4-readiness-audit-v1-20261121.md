# Stages 1 to 4: is everything built and in place? Readiness audit (v1, 2026-11-21)

Request (researcher, 2026-11-21, verbatim): "I agree with §1. Except that the stage 4 should be fully specified - and built. This needs to be clarified and changed in the programme prose to reflect. I also want you to step through 1-4 of this section (exclude 5 - claims) and read through the code and individual methods to ensure that all the code, rules, guides, configs are built and in place for every element of the processing of 1-4. I am expecting you are going to fall over your feet, but I am hoping it is not the case and that our previous work was solid and completed."

Carried on #2526 (stages 1 to 3) and #2528 (stage 4). Section numbers refer to outputs/escalation/2527-where-the-programme-is-picked-up-and-the-stage-end-v2-20261121.md.

## 1. What was checked, and how

| Check | Method | Result |
|---|---|---|
| The four test suites of the layered reading | Run on fresh copies of iba.db, never the live database | temp_2505_layers_test_run.py 47 of 47 pass; temp_2509_grouping_test_run.py 24 of 24 pass; temp_2507_alignment_test_run.py 12 of 12 pass; temp_2503_collection_index_test_run.py stops with an exception (finding F6) |
| The live pipeline on thought | LayerOpen -Check for S1 and 1.1, LayerPull for S1, GroupPull | All run on the live data (S1 demands 177 words, 0 added; 1.1 refuses because S1 is not closed, as designed; the S1 pull wrote 167 rows; the grouping pull wrote 197 rows) |
| The code | Read: iba/app/lib/layerreading.py (the data load, the gates, what each step demands, the nodes each aspect must carry). Read through the tests, not line by line: the recorder and checker of layerreading.py, iba/app/lib/collectiongroup.py, iba/app/lib/collectionindex.py. Read by structure only: iba/app/lib/reading.py (1,556 lines). | See the limits in section 5 |
| The configuration | cfg_setting layer.reading, the behaviour rules 130 to 134, the method rules LR, LX and GP, the step registrations, the write grants, the table and column meanings, the rule delivery | See section 2 |
| The guides | iba/app/USER-GUIDE.md on the index, the grouping and the layered reading | See F7 |
| The data | The ledger, the index, the subgroups and the observations of thought | See F1 and F2 |

## 2. Verdict by stage

| Stage | Code | Config and rules | Guide | Tests | State of the data | Verdict |
|---|---|---|---|---|---|---|
| 1 Lexical analysis (S1) | Built: open, pull, record, check, adopt; function words excluded by the morph class | layer.reading item word-sense; rules LR-01 to LR-04, LX-01 | Described | Pass | Not run: 10 of 177 words answered, 167 open (F1) | Built and sound; not yet run |
| 2 Grouping | Built: Index, GroupPull, GroupRecord, Subgroup, NodeGroups, IndexCheck | Rules GP-01 to GP-04; steps and grants registered | Described | Pass | The withdrawn first grouping still stands in the tables (F2) | Built and sound; the data needs clearing; the method is the open work |
| 3 Verse-lexical (1.1, 1.2, 2.1) | Built: the gates, the ledger rows demanded from the data, the nodes built from the data, the check | Steps, items, thresholds (three shared verses) in layer.reading | Described | Pass, on a test collection | Never run on a real collection | Built and sound; never run live |
| 4 Inner-being analysis | Not built: no step, no ledger item, no stage value, no recorder, no check | The definition exists, scattered in the reading configuration for a cluster reading (F4) | Not described (the guide says not built) | None | None | Not built; to be specified and built |

So: stages 1 to 3 did not fall over. The machinery is built, tested and works on the live data. What is not in order is the state of the data left by the first attempts, three mismatches between the rules, the configuration and the Programme book, one broken test, and stage 4.

## 3. Findings

| No | Finding | Evidence | What it needs | Where carried |
|---|---|---|---|---|
| F1 | Stage 1 on thought is not closed and was not "run once, to be revisited". The first run (281 observations) was withdrawn on 2026-11-15 when the step was redesigned to one observation for each sense a word has in its verses. The redesigned step was run on 10 of the 177 words; 167 are open. The ledger holds 394 retired rows of the old design. The record (#2463 v38, "394 aspects validated") describes the withdrawn run. | Ledger collection_layer_item for thought: observed 10, open 167, retired 394; observations of stage lexical: 11 live drafts, 294 withdrawn | The Programme book row is corrected (done, section 4). Stage 1 on thought is run in full, the 10 existing observations read again, and the anomaly list (H1961, G1161, H0413, H6424, G6063, G1097) used as cases to test the redesigned step. | #2526 step 1 |
| F2 | The withdrawn grouping still stands in the tables. Thought holds ten subgroups, 116 placed surfaces and 81 surfaces set aside from the withdrawn method. The gate of step 1.1 reads them as a finished grouping, so a step could be opened on a grouping the researcher has ruled out. The Programme book said "no subgroup stands"; that was the ruling, not the data. | collection_subgroup 10 live rows; collection_subgroup_surface thought: placed 116, isolated 81, unplaced 0 | The grouping is run again for thought (GroupRecord retires emptied groups, tested at W6). Until then no step after S1 is opened for thought. The Programme book row now says what the tables hold. | #2526 step 2 |
| F3 | Rule 132 and the Programme book disagree on the stage of step 1.1. Rule 132 puts the groups (1.1) in stage 2 and steps 1.2 and 2.1 in stage 3; the Programme book puts 1.1, 1.2 and 2.1 in stage 3 and the grouping alone in stage 2. The configuration's own stage values are lexical, layer-1 and layer-2, which map to neither. The Programme book already says the numbering is open. | cfg_behaviour_rule 132; layer.reading stages; Programme flow | One wording of the stage numbers in rule 132, layer.reading and the guide, through a configuration proposal. It is part of the stage 4 build because stage 4 adds a stage value. | #2528 step 4 |
| F4 | Stage 4 has nothing built. There is no stage value for its observations (the stage values are the earlier methods, lexical, layer-1 and layer-2), no step or item in layer.reading, no recorder or check for it, no method rules like LR and GP, no test and no guide. Its definition exists, in the reading configuration, written for a cluster or subgroup reading that did the lexical and inner-being work in one pass. See section 4. | cfg_enum ib_observation.stage; layer.reading steps S1, 1.1, 1.2, 2.1 only; the reading settings | Specified and built. See section 4. | #2528 |
| F5 | The old reading machinery still scopes by cluster or subgroup. iba/app/ps/Reading.ps1 Open takes one subgroup as its home; reading.home_cluster is not null; rules 119 and 120 and method rules RM-03, RO8 and RO13 describe that scope; the guide says it stays "until the reading by collections (#2448) replaces it", and #2448 is superseded. The breach recorded at #2448 v16 (rules 119, 120 and RO13 changed before the collection Open existed) is part of this. | iba/app/lib/reading.py (5 references to home_cluster); iba/app/USER-GUIDE.md; the method rules of reading.open | Stage 4 is built from that machinery, so its scope rules are replaced in the same unit of work as the code. | #2528 step 4 |
| F6 | The test of the collection index (iba/app/tools/temp_2503_collection_index_test_run.py) stops with an exception on the live data: it places the surface meditate whole, and meditate is now split by Strong's code in thought. The test depends on the live thought collection. | Run on a copy: IndexError_ "'meditate' is split by Strong's code in collection thought: name the sense with -Strong" | Make the test use a collection it builds itself, as the 2505 test does. | #2526 step 4 |
| F7 | The guide describes the layered reading as one paragraph of about 2,000 words, and says stage 4 is "not yet built". It has no short run order for a collection (Index, GroupPull, GroupRecord, NodeGroups, then S1, 1.1, 1.2, 2.1 each with open, pull, record, check). The rules 132, 133 and 134 are delivered at the start of every session; the method rules are delivered with the step. | USER-GUIDE.md; cfg_rule_scope | A run order as a short list and the stage 4 wording, written when stage 4 is built. | #2528 step 4 |
| F8 | The grouping rule GP-01 allows a verse to be read where the dictionary leaves two groups open; the Programme book says the grouping is judged without the verses. The pull gives dictionary evidence only (test P1). | cfg_method_rule 243; Programme flow, Volume | One wording; decided with the grouping method design. | #2526 step 2 |
| F9 | The checks of the layers are structural. LayerCheck and GroupRecord check that rows are answered, nodes equal the data and the text names its verses; none checks that a judgement is right. This is the gap the Programme book already names ("no check of content before a stage closes"), and it is the reason the first grouping passed every structural test and still failed. | Test results; Programme flow, what stands unsolved | The researcher reads thought's grouping and stage 3 account (the Review steps). A content check is part of the design of step 2. | #2526 step 2 |
| F10 | The stage 3 demands for direction and for qualifiers rest on heuristics of the evidence report: direction is demanded for the verses where an entity occurs, and a qualifier candidate is a negator or a word whose morph class is adjective or adverb. | iba/app/lib/layerreading.py derive; the guide on evidence pairs | Read on the first real run of stage 3 for thought; any missed or surplus demand is corrected then. | #2526 step 3 |
| F11 | Two things the record carries are not built: the validation flag of ruling N14 on the node, and the node and observation classes the checker still lists for the earlier methods. | #2448 v12 | Worked as each collection is read. | #2526 and #2528 |
| F12 | The pilot collection is a small one. Thought has 33 surfaces and 351 verses; the median collection has 15 surfaces and the largest, desire, 63. (The earlier figure of 197 was the number of index rows after the first grouping split the surfaces by Strong's code.) | collection_subgroup_surface and verse_lexical counts, 2026-11-21 | Not a defect. The pilot is a sensible size for the first test; it is not a test of scale. | #2526 |

## 4. Stage 4: what the record already defines, and what building it takes

The Programme book now states stage 4 as required, to be fully specified and built. The parts already defined in the live configuration:

| Part | Where | What it holds |
|---|---|---|
| Items explored for each characteristic | cfg_setting reading.observation_items | Nine: meaning, role, polarity, object, enactment, party with route, circumstance, operation with its chain, flag |
| Kinds of finding | reading.observation_parts | face, qualification, party, statement, link, use, term, silence |
| Node roles | reading.node_roles | characteristic and qualifier (relevant); object, relational_target, enactment (bears on); standalone; lexical |
| How a verse is read | Method rules RG-01 to RG-25 | Outward from the verse; passage and genre; role for each occurrence; qualifier binding; parties and route; the original; never close on "not X"; the hidden behind an act; source against enablement; morph read; simile tenor; faculty last |
| How a finding is written | RW-01 to RW-11, RO1, RO2, RO11 | No duplicates, concise and verse-specific, span-grounded, one row for each slant, a re-read builds on earlier observations |
| What counts as covered | RS-01 to RS-10 | Every surface evaluated for a role; one observation for each item of each characteristic |
| Nuances | reading.nuance_pointers | Sixteen |
| Question catalogue | reading.observe_prompts | M-code and D-code prompts |
| Node and observation rules | Behaviour rules 130 and 131 | Govern every layer already |
| The interventions the Programme book lists | The programme prose | Read beyond the verse, read outward, check the original, reclassify a word whose role here is not its collection's, do not force a meaning, record a discovery outside the verse separately: defined, not carried into the layered reading |

What building stage 4 takes (a design to the researcher first, per behaviour rule 105; nothing is built from this audit):

1. **Split the items.** Of the nine items, meaning (face) is done by stages 1 and 3; the lexical side of role (the qualifier by the grammar) is done by step 2.1; what remains for stage 4 is the role of the characteristic, what the qualifier gives it in place, polarity, object, enactment, party and route, circumstance, operation and chain, and flag.
2. **Re-scope.** Take the rules off the cluster and the subgroup of the old reading and put them on the collection, the subgroup and the ledger.
3. **Register.** A stage value for its observations, its steps and items in layer.reading, method rules in the form of LR and GP, the write grants, the table and column meanings, and the rule delivery.
4. **Build.** The open, pull, record and check for stage 4 on the same ledger, with the recorder refusing what the rules refuse (the route, the roles, the kinds).
5. **Add the level the Programme book names**: across subgroups and across collections.
6. **Carry the interventions** into the pull, as prompts and checks.
7. **Test** on a copy, as the 2505 and 2509 tests do, then run on thought.
8. **Guide and prose.** The guide and the Programme book describe it as built.

The Programme book also says, from the researcher, that how a working across several nodes is one record, and the unit of a batch, are not stated. Those go into the design in step 1 of this list.

## 5. Limits of this audit

- The recorder and checker of layerreading.py, the whole of collectiongroup.py and collectionindex.py were tested through their test suites and exercised live through the pull and the previews; they were not read line by line. The 83 passing cases cover their refusals and their writes on a test collection.
- iba/app/lib/reading.py was read by its structure and its scope handling only. Reading it in full is part of the stage 4 design.
- No row was recorded on the live database. The two working files written by the live pulls are working files, not records: _analytics/surfaces/working_files/layers/layer-thought-S1-20261121.json and _analytics/surfaces/working_files/layers/group-thought-20261121.json.
- The quality of any judgement (a sense, a group) was not tested; no check of that kind exists (F9).

## 6. Changes made with this audit

- The Programme book (sections Programme flow, The analytical grouping, The collection reading, Claims and synthesis across collections, and Claims and the narrative) now states stage 4 as required, to be fully specified and built, and corrects the stage 1 and stage 2 rows to the state of the tables (F1, F2). Patch archive/patches/wa-prose-stage4-required-20261121T070000Z.json; export Workflow/Programme/programme_prose/wa-programme-prose-extract-20261121.md.
- Nothing else was changed.
