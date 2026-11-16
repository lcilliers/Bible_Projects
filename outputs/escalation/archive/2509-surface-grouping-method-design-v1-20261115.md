# #2509 The method for grouping the surfaces of a collection (stage 2): design (v1, 2026-11-15)

Status: design for approval (B:105). Nothing is built. Prompted by the researcher (2026-11-15, verbatim): "I gather the surface groups have no method designed to perform the grouping." Confirmed: see section 1.

## 1. The gap, from the code and the record

- `lib/collectionindex.py` `make_group` and `place` (and `Collection-Build.ps1 -Action Subgroup`) make a subgroup and place a surface only "on the researcher's instruction, with a reason"; the USER-GUIDE and the step text say the same. Nothing reads the evidence of a collection and groups its surfaces.
- The researcher's definition (#2463 v16): layer 1 step 1 "place[s] the words into groups of what it is or does for the inner being", a word "that has no inner being role is isolated", and "each grouping becomes an observation with the surfaces as the nodes"; the aim is that AI decides in the majority of cases and the researcher scrutinises (#2463 v18, 5.4); rule 132: Claude reads the evidence and decides.
- My build made the grouping a gate in front of step 1.1 and left it to the researcher's instruction. That contradicts the definition: the grouping is Claude's work, and my note on #2463 v38 (the groups are the researcher's instruction) was wrong.

## 2. What the method is

Stage 2, the last part (the researcher, #2507 v7): "creating surface subgroups with collections". For one collection, Claude reads the evidence of every member surface and decides, in one pass, three things: the groups (each a name and a definition of what its surfaces are or do for the inner being), the group of each surface, and the surfaces with no inner-being role (isolated, with the reason). The researcher's groups of `thought` on #2463 v16 (starting: conceive, gives thought, imagine; weighing: considered, conflicting thoughts; the types: imagination, meditation, minding and musing, opinion, reasoning, pondering, thinking, suggestion) are the test of the method: the method's result for `thought` is compared with them.

**Evidence per surface** (all stored; nothing is invented): the surface and its Strong's codes with the occurrence count of each; the surface's own link in the collection (tier core, synonym, opposite) and the collection's pole word; for each code the lexicon sense (`strong_sense` head, `strong_meaning_tree`); the stage 1 observations of the word where they exist (the lexical reading of the word and its face observations) and, where they do not, the mechanical facts only (morph classes, `verse_lexical` structure, sample verses); the surface's group in `surface_term.surface_group` (behaviour or inner_being_state); its history, if any, as a hint only (the retired cluster subgroup and concept of the surface). Stage 1 is not a precondition of the grouping; it is evidence when it exists.

## 3. The routine

Two new actions of `Collection-Build.ps1`, in the pattern of LayerPull and LayerRecord, and nothing new in the tables:

1. **`GroupPull -Collection <name>`** writes a working file (`layer.working_dir`) with one row for each member surface (and one for each code of a surface already split by code), carrying its evidence, and empty `fill` fields: `group` (a group name), or `isolate` with a `reason`; plus a `groups` list to fill (name, definition) and for each row a `certainty` (`decided` or `uncertain`, an uncertain one with what the evidence could not settle).
2. **`GroupRecord -File <file> [-Check]`** checks the whole file and writes it in one transaction, or refuses all of it: every surface (and every code of a split surface) is covered once; a group has a name that is unique in the collection and a definition of at least `min_text_chars`; every group holds a surface; an isolate has its reason in words; an uncertain row says what could not be settled; a surface split by code follows the rule of the index (the other codes stay unplaced unless the file places them). It writes the groups and the placements through `collectionindex.make_group` and `place`, each change a `surface_event` with the reason "Claude's judgement from the evidence, file <name>, run <id>" and `created_by` Claude, and refreshes the group on the nodes (`refresh_nodes`, as placement already does). A second run with a changed file re-places the surfaces and the processed move reopens what depends on it (the ledger retires or fails the rows; B:120).
3. **The scrutiny**: `IndexCheck` is extended to list, for a collection, every group with its definition and surfaces, every isolate with its reason and every `uncertain` placement with what was unsettled (one versioned report, `collection.index_check_name`). The researcher reads that report; a correction is the researcher's `Subgroup` instruction, which stays as it is (it keeps its `-Reason` of the researcher's words) and wins over Claude's placement.

The grouping gate of step 1.1 (`grouping_gate`) stays: every surface placed or isolated with a reason, every group holding a surface. Step 1.1 then records each group as an observation (its definition by what the surfaces do for the inner being), as built.

## 4. Where the grouping judgement is Claude's and what reaches the researcher

Claude decides every placement. What reaches the researcher is (a) the report of section 3, and (b) the cases marked `uncertain`, with the evidence: where the evidence does not settle whether a surface has an inner-being role or which of two groups it belongs to. Nothing is put to the researcher as a question that the evidence settles.

## 5. Control list

| # | Item | Home | Action |
|---|---|---|---|
| C1 | steps `collection.group_pull`, `collection.group_record`, their routed condition, write grants (`collection_subgroup`, `collection_subgroup_surface`, `surface_event`, `ib_node`, `ib_observation_change`) | `cfg_step`, `cfg_on_fail`, `cfg_write_grant` | add |
| C2 | the settings of the grouping (the fields the file carries, the minimum lengths) | `cfg_setting` (a sibling of `layer.reading`) | add |
| C3 | method rules GP-01 to GP-04 (the evidence, one pass and whole-file, the isolate and uncertain reasons, the researcher's `Subgroup` wins) | `cfg_method_rule` | add |
| C4 | the text "only on the researcher's instruction" | `lib/collectionindex.py` docstrings and error text, `handlers/collectionbuild.py` `subgroup`, step `collection.subgroup` and `collection.index` text, USER-GUIDE 8.x (the collection index paragraph), B:132 (stage 2 names `Subgroup`) | reword: Claude's judgement through GroupRecord, the researcher's instruction for corrections |
| C5 | code: `GroupPull` and `GroupRecord` in `lib/collectionindex.py` (or a new `lib/collectiongroup.py` if the file grows), `handlers/collectionbuild.py`, `ps/Collection-Build.ps1`, the `IndexCheck` report | code | add |
| C6 | test `tools/temp_2509_grouping_test_run.py` on a copy: the refusals (a surface missing, twice, an empty group, an isolate with no reason, an uncertain with no reason), the record, the nodes' group, a regroup, and the comparison of the result for `thought` with the researcher's groups | tests | add |
| C7 | USER-GUIDE, BUILD, the ps tools worksheet (the two new actions) | documents | add |

## 6. First run and scale

The first run is on `thought`: 33 surfaces; the researcher's groups are the test. The scale is 169 collections; the grouping is one pass of a few dozen surfaces for a collection and does not need stage 1. Stage 1 itself is larger than I had said: the index holds about 17,900 surface and code rows over the confirmed collections, so stage 1 is of the order of that many word aspects (and as many face aspects) across all collections; `thought` has 197. That is the cost of the grain B:113 requires (a word per lettered Strong's code), recorded here so that the researcher can see it before more collections are run.

## 7. Approval

On approval I build it as the control list says, test on a copy, apply, run it on `thought` and bring the report and the comparison with the researcher's groups.
