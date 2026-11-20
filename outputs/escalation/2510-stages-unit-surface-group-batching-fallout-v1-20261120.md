# #2510 The stages of the programme: unit, surface groups, batching, fallout (v1, 2026-11-20)

Status: a record of what the study has already decided, gathered from the escalation record (#2463 v16 to v22, #2507, #2509 v1 to v7), the rules (B:127 to B:134), `cfg_setting layer.reading`, the glossary and the code (`iba/app/lib/layerreading.py`), and checked against `iba.db` on 2026-11-20 (read-only). Where the record does not answer, the point is marked **NOT SETTLED** with the evidence searched. It decides nothing new (B:105) and labels inference (B:4). It answers the researcher's message of 2026-11-20 (recorded verbatim at #2510 v20).

## 1. Answers to the questions asked

1. **The comment column and the history report differ.** Both hold the same text; they are built differently. `escalation.comment` (the column on the item) is cumulative: it holds every comment added over the life of the item (`_APPEND_COLS`, `iba/app/lib/escalation.py` line 82); for #2510 it is 29,261 characters. `escalation_history.comment` and the history report print only what each version added ("set this version", `write_history_report`). Checked: every one of the 19 increments is present in the cumulative column, none missing. The report you read (v2, generated 18:42 on 2026-11-19) stops at v18; v19 and v20 were added after it. The report shows no thread of comments, so side by side the two will not look alike. This is a design property of the report, not a loss of data. **Not explained:** your count of 56 versions. The database held 20 versions of #2510 when this was written (v1 to v20, none duplicated). Whatever shows 56 is another view (the Excel tool sheet or a different item) and I have not seen it.
2. **What §5 of the stage 3 draft v2 says is written, and what is written.** §5 describes the mechanism as built (USER-GUIDE and `layerreading.py`). It is not confirmed by a run. In the database: no stage 3 observation exists (`ib_observation` has no stage `layer-1` or `layer-2` row), the ledger `collection_layer_item` holds rows for one collection only (`thought`, id 56) and only for step S1 (stage 1): 177 word-sense rows, 10 observed and validated, 167 open, plus 394 rows retired. No row of step 1.1, 1.2 or 2.1 has ever been opened for any collection. So §5 for steps 1.2 and 2.1 is untested in operation; the draft's wording "built" is true of the code only. Stage 3 cannot open for `thought` today: stage 1 is not closed (167 open) and the grouping is under the researcher's verdict (section 4).
3. **Where surfaces and surface groups are defined and finalised.** Section 3. The phrase "surface group" carries two meanings in the study, and the stage 3 draft v2 mixed them.
4. **The role of the group in stages 3 and 4, with the reasoning.** Section 4. v2 gave only the mechanical purpose (three points); it did not carry the researcher's reasoning, and it did not state that the grouping run was declared a failure. Both are corrected here.
5. **Unit, batching, fallout by stage.** Sections 5 to 7.

## 2. The stages, as the researcher defined them (2026-11-15, #2507 v7; `governance.programme_stages`, B:132, glossary "stage (collection reading)")

| Stage | What it is |
|---|---|
| Base data | STEP, the spine and `verse_lexical`; the surface cycle (CHARTER section 5) that sorts the English surfaces into the four surface groups and gathers the collections |
| 1 | Lexical analysis of the words (each word in its verses, lexical only; relations between words are base data, not analysed here) |
| 2 | Grouping of the surfaces: the four surface groups, the collections of behaviour and inner_being_state, the subgroups within a collection judged from dictionary meaning |
| 3 | Verse-lexical observations (steps 1.1 to 2.1 of the layers; verse-lexical only) |
| 4 | Inner-being analysis made from the stage 3 observations; the first step of claim formulation. Not built. |
| 5 | Claim formulation and update of the claims register. Not decided. |

Stages 1 to 3 are lexical and carry nothing of the inner being; lexical and claims readings never run in one process (B:132, B:133; researcher, #2463 v20: "the verse cannot be lexical analysed and determine the ib implications in the same process, it needs separate observations").

## 3. Surfaces and surface groups: where defined, where finalised

**"Surface group" has two meanings.**

| Term | Meaning | Held in | Made by | State on 2026-11-20 |
|---|---|---|---|---|
| surface group | The first sorting of a surface text by what it names: behaviour, inner_being_state, entity or other (glossary, approved) | `surface_term.surface_group` | The surface cycle module "group", judged by a model; inferential until confirmed | behaviour 1,204; inner_being_state 2,180; entity 717; other 2,071; 69 not set. Judgement state: confirmed by the researcher 82; corrected 652 (394 by Claude under researcher direction, 46 by the model, 212 by rule); judged by the model only 5,435; unjudged 56 |
| subgroup (the researcher also says "surface group" and "grouping") | A group of the surfaces of one collection that mean the same or the same kind of thing, judged from dictionary meaning; each is a concept (researcher, #2463 v18 (d)) | `collection_subgroup`, `collection_subgroup_surface` | Stage 2: `GroupPull`, `GroupRecord`, corrected with `Subgroup` | `thought` only: 10 subgroups, 116 index rows placed, 81 set aside (`isolated`); the other 168 confirmed collections: 3,404 index rows, all `unplaced` |

**Where each is defined and finalised.**
- The four surface groups: defined by the surface cycle (base data); the researcher's own stage 2 definition counts them in stage 2. They are final only as far as the researcher has confirmed them (82 of 6,225 rows) or they were corrected under the researcher's direction (394); the model's judgement (5,435) and the rule-set rows (212, 46 by the model) stay inferential (B:4).
- The collections (membership): gathered by the surface cycle (module "collections", `collection_link` tiers); a collection is `confirmed` by status (169 confirmed, 86 merged, 23 retired). Changes to collections are made class by class under the procedure of B:129.
- The subgroups: defined in stage 2 and finalised when the stage 2 gate holds for the collection: the index filled, every surface placed in a subgroup or set aside with its reason, every subgroup holding a surface (`grouping_gate`). **No collection has passed it.** For `thought` the gate is met on the face of the data (no unplaced row), but the grouping run was declared a failure by the researcher on 2026-11-15 (#2509 v6, verbatim in section 4) and was not rolled back (snapshot `iba-20261115T182511Z-pre-2509-grouping.db`). **NOT SETTLED:** whether the thought groups stand, are rolled back or are re-made; the record shows no later decision.
- Stage 2 is therefore a prerequisite of stage 3 that is, today, not satisfied for any collection.

## 4. The role of the subgroup across the stages, and the reasoning

What the researcher said, in order (verbatim openings are in the escalation record):

1. **#2463 v16 (2026-11-14), the first statement.** Looking at the 33 words of thought he saw groups: starting (conceiving, give thought, imagine), weighing (considered, conflicting thoughts), types of thought (imagination, meditation, minding and musing, opinion, reasoning, pondering, thinking, suggestion). "The word thought is a collective word that have lots of different nuances. Each grouping becomes an observation with the surfaces as the nodes." Step 2 enriches each group from the Strong's codes of its members, "as this will become the link to the usage of the grouping", and gives it a short definition (what does meditation mean). Layer 2 reads what stands with each group, whether groups relate or are used interchangeably, qualifiers, entities, direction of travel; "keep on validating the grouping, reform the groups if needed".
2. **#2463 v18 (2026-11-14), the reasons.** (a) Each surface is linked to verses, so "when you create a surface grouping, the verses travel with it in the nodes" (B:120 then, B:130 now). (b) The observation is likely made for a group of surfaces, "all the derivatives of mind that travels together e.g. minding, in mind, to mind, minds". (d) "These sub groups are concepts"; the database provides for it, they need only be made discoverable through the nodes. (e) Words are never analysed alone in the claims reading: each is bound with its partner (the characteristic) or excluded; a word wrongly included is moved to entity or other and the move is processed "else it will cause issues when completeness tests are being performed". Layers 1 and 2 are "all about preparing the base data for the claim formulation".
3. **#2509 v3 (2026-11-15), the correction.** "the surface groups has nothing to do with the inner being. it is about the meaning of the surface words... in the majority of cases is about simply judging the dictionary meaning of the words". The what-it-does-for-the-inner-being half moved to stage 4.
4. **#2509 v6 and v7 (2026-11-15), the verdict on the run.** "nope. this is off. the groups will not serve any purpose. grouping is not a skill you have. I suspect you have completely overengineered it, and missed the boat completely. you simply changed the meaning of the underlying words which will completely drive any analysis in the wrong direction." Later: "your explanation of what you did just further show that you have not even considered or thought about what the groups are being used for."

**What the construct is, as the record states it (the reading below is labelled inferential, B:4, and is for the researcher to correct).**

The subgroup is a concept inside a collection: the surfaces that carry one meaning, gathered so that the study reads and states things once for the concept and not once for each surface, while the verses still travel with it through the nodes. It is the unit at which a finding is attached, found again, and carried forward.

| Stage | Role of the subgroup | Source |
|---|---|---|
| 2 | Is made: a set of surfaces of one dictionary meaning, named for it; a surface not carrying the collection's meaning is set aside with its reason. Judges meaning only. | #2509 v3, B:132, glossary "subgroup" |
| 3 | Is the unit every observation is keyed to: its definition (step 1.1), its Strong's enrichment, which links the group to the usage of the group in the verses (step 1.2), then the pairings, qualifiers, entities, direction, relations between groups and double meaning of the group (step 2.1). Validates the grouping by reading it ("keep on validating the grouping, reform the groups if needed"). States what the words and the verses show; nothing of the inner being. | #2463 v16, `layer.reading` |
| 4 | **Not defined in config.** The record says the observation about what a word does for the inner being "is likely to be made for a group of surfaces"; the word is bound with its partner (the characteristic) or excluded; the group's observations are found through its nodes. Stage 4 reads the stage 3 observations of the group as its evidence and does not redo them. **Inference:** the group is the unit at which the inner-being role is stated in stage 4; the researcher has not said so for stage 4 itself (#2463 v18 (b) was said of layer 1 before the stages were re-cut on 2026-11-15). | #2463 v18; the stage 4 draft (a proposal) |
| 5 | Not decided. The group reaches claims only through the nodes of its observations. | `governance.programme_stages` |

**NOT SETTLED, with the evidence searched.** (i) What the failed run got wrong: the verdict says the groups "changed the meaning of the underlying words" and "will not serve any purpose". #2509 v5 says the run was to be compared with the groups named at #2463 v16; the comparison is in the report `collection-groups-thought-v1-20261115`, not read here. Until it is, it is not known whether the fault was the method (dictionary meaning), the output, or the purpose the groups were built for. (ii) The stage 4 role is inferred, above. (iii) The record has the groups as concepts (v18 (d)) and the glossary has `concept` and `concept_subgroup` holding a level above the collection (#2463 v20); how the subgroup relates to them is in the record only as "the DB already provides for it".

## 5. The unit of study, by stage

| Level | Unit | Source |
|---|---|---|
| The programme | The **collection**: observations, claims and narration follow it; each collection becomes a chapter of the narration | B:127, glossary "collection" |
| Stage 1 | The **word**: a surface with its lettered Strong's code, read in its verses within one collection; one row of the ledger (`word-sense`) for each; one observation for each sense the verses give it, with the occurrences as nodes; a word of function occurrences only (preposition, particle, pronoun, article, suffix, and the like) has no row of its own, except a negator (RG-22). `thought`: 177 rows; all collections: about 17,900 | `layer.reading`, `layerreading.derive`; #2509 design v2 section 5 |
| Stage 2 | The **surface** within its collection: one index row for each member surface (and each of its codes if it splits); placed in a subgroup or set aside | `collection_subgroup_surface`, USER-GUIDE |
| Stage 3 | The **subgroup**: every row is keyed (step, item, subgroup, subject); the subject is the partner collection (pairing), the other subgroup (relation) or the surface (double meaning). The collection is the gate; the verse is the place read | `collection_layer_item`, `layerreading.derive` |
| Stage 4 | **Not defined in config.** Inferred: the subgroup, bound with its partner (section 4) | as section 4 |
| Stage 5 | Not decided | |

The cluster is no longer a unit of reading or of nodes (researcher, #2463 v18 §4.1; #2495).

## 6. Volume and batching

What the record and the code give:
- The **collection** is the batch the process works in. Every pull, record and check takes one collection (`-Collection <name>`); every gate is per collection.
- Stage 2: one whole-file pass for a collection (`GroupPull` then `GroupRecord`); sized as a short pass for each, because it judges dictionary meaning without the verses; 169 collections and about 3,400 surfaces in all (#2509 design v2 section 5).
- Stage 1 is the large part of the work: about 17,900 word rows over all collections (`thought` alone 177). The pull shows at most 80 nodes for each row (`layer.reading pull_max_nodes`), which bounds a row, not a collection.
- B:125 governs only a job that runs longer than a few minutes (start it outside the session, with a log, a way to check, stop and resume). It does not say how work is divided.
- **NOT SETTLED:** I found no stored rule for (a) the order in which the 169 collections are taken, (b) how stage 1 of a large collection is split across sessions (the pull and record are whole-file; the ledger lets a step stay partly answered, as `thought` shows with 10 of 177, but no batch size or resume rule is configured), (c) whether stage 3 for a collection is taken whole or by subgroup. Searched: `layer.reading`, `collection.*` settings, B:125, B:127, B:132, B:134, the 2507 and 2509 design documents, the `Collection-Build.ps1` parameter list (only `-Limit`, used by `Ask`).

## 7. Fallout: what is not analysed, and what is done about it

| What falls out | Where it falls out | What the record says is done | State |
|---|---|---|---|
| Surfaces of the groups entity and other, and surfaces of neither behaviour nor inner_being_state | Not members of any collection; "deliberately outside the collections" | Entity and other surfaces of an in-scope verse enter as nodes of the observation that covers them; a verse holding only entity or other surfaces is out of scope and not touched (B:129, B:130) | Decided |
| A word wrongly included in a collection | Found at any stage | Moved to entity or other by the collection change procedure; the move is processed so the step reopens and the completeness tests hold (researcher, #2463 v18 (e); B:129, B:134) | Decided |
| Function words in stage 1 | No row of their own (RG-22) | Read with their unit; a negator is a row | Decided |
| A surface whose meaning is not the collection's (set aside, `isolated`) | Stage 2; 81 in `thought` | Kept in the index with its reason, not grouped (B:134). In stage 3, the pairing, qualifier, entity, direction and relation rows are derived from placed occurrences only: a set-aside surface's occurrences are skipped without a row, a record or a failed check (`layerreading.derive`, line 161: `if g is None: continue`) | **NOT SETTLED:** the record says the surface is set aside and, if wrongly included, moved; it does not say what a surface that is rightly in the collection but set aside is read for afterwards, and the researcher's rule that words are bound with their partner or excluded (#2463 v18 (e)) has no recorded step that excludes it with a record |
| A pairing or relation of fewer than 3 shared verses | Stage 3 | No row is demanded (`pair_min_verses` and `relation_min_verses` are 3); the pairs remain in the evidence report | **NOT SETTLED:** whether below-threshold pairs are meant to be unread; no ruling found |
| A qualifier, entity or double meaning that is not present | Stage 3 | A none with a reason is allowed where the item allows it (B:134) | Decided |
| Surfaces not yet placed | Stage 2 | They block step 1.1 (`grouping_gate`): 3,404 index rows in 168 collections | Decided (a gate) |
| A Strong's aspect missing from the verse corpus | Stage 1 | Not a conflict or error; the application may enlighten the word's use for the inner being; no observation need focus on the non-inner-being meaning (researcher, #2463 v18 (c)) | Decided |
| Surfaces of the groups with no group set (69) or unjudged (56) | Base data | None recorded | **NOT SETTLED:** the record shows the counts, no rule on whether they are in or out of the collections |

## 8. Corrections to my earlier documents

1. Stage 3 draft v2 said stage 3 "is built". True of the code only; never run (section 1, point 2). Corrected in draft v3.
2. v2 §4 treated "surface group" as one thing and gave the purpose as three mechanical points; it left out the second meaning, the researcher's reasoning, and the verdict of 2026-11-15 on the grouping run. Corrected in draft v3 (section 4 points here).
3. v2 §7 item 2 treated "stage 4 is not gated until all of stage 3 is completed" as settled with one inference. It stands as the researcher's statement; the inference on its scope is kept and labelled.
4. The gap list v2 and the stage 3 draft each needed this account: the prose rewrite of chapter 2 (method) must carry sections 2, 3, 5, 6 and 7 of this document as the programme's own statement of its stages. Sections 4, 6 and 7 hold **NOT SETTLED** points; the prose states what is settled and does not carry a guess (standard 2 of the gap list).

## 9. What is open (raised in #2510 v21; each is a gap in the record, not a question I could answer by reading)

1. The state of the `thought` groups (stand, roll back or re-make) and what the failed run got wrong, after reading the comparison report.
2. The role of the subgroup in stage 4, which is not defined in config.
3. Batching: the order of collections, the split of stage 1 for a large collection, stage 3 by collection or by subgroup.
4. The fallout rows marked **NOT SETTLED** in section 7: set-aside surfaces in stage 3, below-threshold pairs, and surfaces with no group or unjudged.
