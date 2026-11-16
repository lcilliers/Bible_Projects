# #2507 The lexical observations by collection: what is in place, the full inventory of what must change, and the design (v2, 2026-11-15)

Status: read-only audit and a design for the researcher's correction (B:105). Nothing is changed. v1 (archived, `archive/2507-lexical-observations-by-collection-alignment-and-design-v1-20261115.md`) was not approved: its section 3 listed the misalignments I had already seen and did not show that the list was complete. This version replaces it. Section 3 is now an inventory made by a scan of every control home in the control map (`cfg_control_home`), with a disposition for each hit and a statement of what the scan did not reach (3.12).

"Lexical observation" is used in the researcher's sense (#2507 v1): an observation about the structural composition of the verse, explicitly not inner-being aware.

Disposition codes: **KEEP** (stays as it is), **RETIRE** (inactive, file to its `archive/` folder), **REWORD** (stays, its text changes), **SPLIT** (part moves to the lexical process, part stays), **ADD** (new), **#2448** (belongs to the collection Open and the realignment of the old reading; carried there, not decided here), **DECIDE** (needs the researcher).

## 1. What the record says the lexical observations are

- `verse_lexical` is the structural composition of the verse and "can never carry an inner-being concept" (researcher ruling, #1383 v23). The next step is the observations about that structure, entered through the collections (#2507 v1).
- `lexical.enrich` (`verse_lexical_note`) was retired on 2026-09-16 (#1706) and `lexical.run` on 2026-09-07 (#1549). The replacement was the verse-reading stage: `lexical.meaning` (word level) and `lexical.relational`, split on the researcher's word of 2026-09-23 (#1860).
- The question catalogue marks lexical evidence as dimension M0; its scope `Word/term (lexical)` holds 26 active questions (M0.1 name, M0.2 kind, M0.3 boundary, M0.4 grammatical form, M0.5 lexical and semantic analysis).
- Layer 2 has two sets (#2507 v1): the lexical-structural set and the inner-being set (the claims process). Faces are identified in the lexical work; what they do for the inner being is layer 2 (#2463 v22).

## 2. What is in place

The structure (`verse_lexical`: 544,667 live rows, checked 2026-11-15); the typed neighbours of every member occurrence (`collectionevidence.build_pairs`, #2502); the kinds term, face, link, use (`reading.observation_parts`); the ledger, recorder, nodes-from-data and the check (`layerreading.py`, #2505); the 26 lexical prompts; the build and readiness steps of `verse_lexical` (`lexical.build`, `lexical.readiness`, `report.verse_lexical`).

## 3. The inventory

### 3.0 How it was made

For each control home in `cfg_control_home` the active rows (or the file) were searched for: `lexical.meaning`, `lexical.relational`, `lexical.enrich`, `lexical.run`, `VerseReading`, `RelationalReading`, `Run-Stage1Batch`, `verse_lexical_note`, `verse-reading`, `verse reading`, `cluster-agnostic`, `lexical`, `M-code`, `word-level`, `relational`, `Stage 1`, `Layer 2`, `structural`; imports of the old modules were traced in `iba/app/lib`, `handlers`, `ps`, `tools`; `ib_observation` was counted by stage and tag. A word search finds only what names the old process; the 61 `reading.*` method rules were therefore also read by their first 170 characters (3.6). Results by control home:

| Control home | Scanned | Active rows or files that name the old process |
|---|---|---|
| `cfg_step`, `cfg_work_package`, `cfg_on_fail` | yes | 24 of 169 steps (3.1) |
| `cfg_utility` | yes | 30 of 176 (3.2) |
| `cfg_write_grant` | yes | 28 of 307; 6 are the two old steps (3.3) |
| `cfg_setting` | yes | 54 of 328 (3.4) |
| `cfg_enum`, catalogue, `cfg_column`, `cfg_table` | yes | (3.5) |
| `cfg_method_rule` | yes | 27 of 99 by word; all `reading.*` read (3.6) |
| `cfg_behaviour_rule`, `cfg_rule_scope` | yes | 18 of 115 by word (3.7) |
| `cfg_report`, `cfg_report_section`, `cfg_quality_check`, `cfg_trigger`, `cfg_prose_concept` | yes | (3.3, 3.8) |
| `iba/app/GOVERNANCE.md`, `iba/app/CHARTER.md` | yes | none name the old process; no change (see 3.9) |
| `iba/app/USER-GUIDE.md` | yes | sections 6 and 7 and the layered reading paragraph (3.9) |
| `.claude/commands`, `.claude/hooks`, `.claude/settings.json` | yes | none |
| `iba/app/lib`, `handlers`, `ps`, `tools` | yes | (3.10) |
| `ib_observation` data | yes | (3.11) |
| `iba/docs`, `Workflow`, `iba/app/reports` | counted, not read | (3.12) |

### 3.1 Steps (`cfg_step`)

| Step | State | Disposition |
|---|---|---|
| `lexical.meaning`, `lexical.relational` (work package verse-lexical, ordinal 6, 7) | active; all their method rules inactive | **RETIRE** (D3) |
| `lexical.build`, `lexical.readiness`, `report.verse_lexical` | active | **KEEP** (base data); `lexical.readiness` text names cluster: **REWORD** if it does |
| `report.lexical_exceptions`, `report.lexical_extract` | active; their text names the retired `lexical.enrich` and the table `verse_lexical_note` | **DECIDE** (D7): retire with the table, or keep as reports of what exists |
| `lexical.enrich`, `lexical.run` | already inactive | none; their guidance remains in USER-GUIDE section 6 (3.9) |
| `reading.open` (opens one subgroup) | active | **#2448** (the sequencing breach on rules 119, 120, RO13 stays open there) |
| `engagement.pull`, `.record`, `.group`, `.check`, `.review`, `.close` | active | **DECIDE** (D8): engagement writes the kinds face, use, qualification, statement, link (3.11); the boundary between its `face` and the lexical `word-face` must be stated |
| `collection.layer_open` (text names the lexical gate) | active | **REWORD** (the gate becomes "step 0.2 closed") |
| `cluster.assign`, `cluster.validate`, `report.cluster`, `spine.check`, `verse_scope.resolve`, `verse_collate.collate`, `strong.reconcile`, `raw.*`, `open_item.due`, `observation_enhancer.*`, `collection.export_members`, `collection.export_surfaces` | active; hit only on the word cluster or subgroup | not lexical; **#2448** (named so that none is hidden) |

### 3.2 Utilities and code (`cfg_utility`, import trace)

| Item | Finding | Disposition |
|---|---|---|
| `ps_versereading`, `ps_relationalreading`, `ps_run_stage1batch` and their scripts | front doors of the two old steps | **RETIRE** |
| `lib/versereadinggenerate.py`, `lib/stage1coverage.py` | generator and coverage of the old steps | **RETIRE** |
| `handlers/lexical.py`: `meaning`, `relational`, `_chunk_*` | old steps | **SPLIT**: archive these; keep `build`, `readiness` |
| `lib/lexicalenrichgenerate.py` | its `call_api`, `log_usage` and the cost and error classes are imported by `versereadinggenerate`, `charanswergenerate`, `charreadinggenerate`, `subgroupgenerate`; the retired Layer 2 text sits in the same file | **DECIDE** (D6) |
| `lib/charanswergenerate.py`, `charreadinggenerate.py`, `subgroupgenerate.py` | the retired cluster stages (#2299: `cluster.subgroup`, `.reading`, `.answer` inactive); utilities still active; import `versereadinggenerate._meaning_sources` | **DECIDE** (D6) |
| `lib/lexicalscope.py`, `lib/clusterstatus.py`, `lib/recordingpass.py`, `handlers/cluster.py` | `lexicalscope.resolve_strongs` is used by `clusterstatus` and `cluster.py` | **KEEP** until the cluster-era chain goes (#2448); do not archive with the old steps |
| `lib/lexical.py` | base build | **KEEP** |
| `tools/temp_2295_scope_resolver_test_run.py`, `temp_2323_deleted_and_fixes_test_run.py` | name the old modules | check at build; **REWORD** or archive with the modules |

Nothing may be archived before the import trace is re-run on the result (a stored check, D9).

### 3.3 Grants, failure handling, reports

- `cfg_write_grant`: six rows (`lexical.meaning` and `lexical.relational` on `ib_observation`, `ib_node`, `run_batch`): **RETIRE**. `run_batch`'s own `step` column text names `lexical.meaning`: **REWORD**.
- `cfg_on_fail`: no row names the old steps.
- `cfg_report` and `cfg_report_section`: `report.lexical_exceptions` (4 sections) follows D7; `report.verse_lexical` and `lexical.readiness`: **KEEP**.
- `cfg_quality_check` (reading.check): `every-word-has-role`, `full-lexical-range`, `verse-actually-supports-it`, `bindings-relations-pointers`: **REWORD** or **SPLIT** with the reading rules (3.6).

### 3.4 Settings (`cfg_setting`)

| Setting | Disposition |
|---|---|
| `lexical.meaning_max_verses_per_batch`, `lexical.meaning_max_strongs_per_batch` (already inactive), `lexical.relational_max_verses_per_batch`, `report.stage1_coverage_validation_pattern` | **RETIRE** |
| `lexical.llm_*` (nine keys: URL, version, model, rates, caps, usage log) | **DECIDE** (D6): shared by the generation chain |
| `lexical.span_surface`, `lexical.readiness_report_path`, `report.verse_lexical_output_pattern` | **KEEP** |
| `report.lexical_extract_output_dir`, `report.lexical_extract_output_pattern` | follows D7 |
| `reading.observe_prompts`: gives the M0 lexical prompts to the inner-being reading under the kinds face (8 prompts) and term (6) | **DECIDE** (D8) |
| `reading.node_roles` and `engagement.roles`: inner-being roles only | **ADD** the role group `lexical` to the first (D2) |
| `layer.reading` (layers 1 and 2, gate `lexical-gate`) | **ADD** layer 0; gate replaced (D1) |
| `reading.observation_parts` (the eight kinds, one pass) | **REWORD**: kinds the lexical layer uses, kinds the inner-being layer uses |
| `ib_observation.tag_stage_excluded` (key `verse-reading`), `collection.evidence_catalogue_stages` | **KEEP** as history of the old stage |
| `governance.programme_stages`: "Base_data (STEP through lexical); Analysis (deriving understanding of the inner being); Publishing" | **DECIDE** (D10): the lexical observations are neither `verse_lexical` base data nor inner-being analysis |
| `glossary.currency_check` (terms the glossary must keep current) | **ADD** the term "lexical observation" |
| `reading.gap_types` (term_cluster and other cluster gaps), `cluster.*` | **#2448** |

### 3.5 Enums, catalogue, columns, tables

- `cfg_enum ib_observation.stage`: **ADD** `lexical`; `verse-reading` stays (history).
- `cfg_enum wa_obs_question_catalogue.scope`: the description of `Word/term (lexical)` ("NOT selected by any live stage's query", checked 2026-09-21): **REWORD** (D4). `cfg_column` text of `wa_obs_question_catalogue.section`, `prompt_seq`, `ib_observation.stage`, `ib_observation.cluster_code`: **REWORD** where they name the verse-reading stage.
- `cfg_enum ib_observation.window` (`relational` and the lexical Window 1) and `narrative_claim_source_kind` (`lexical`): **CHECK** at build whether a layer 0 observation takes a window and whether claims may cite it as a source kind.
- `verse_lexical_note` (12 `cfg_column` rows) and `passage.genre`, `passage.lexical_complete_at`: the retired `lexical.enrich` surface; **DECIDE** with D7 whether the registration stays as history.

### 3.6 Method rules (`cfg_method_rule`), all `reading.*` read

Active: `lexical.build` 5 and `lexical.readiness` 1 (KEEP); `reading.observe` 45, `reading.open` 11, `reading.narrate` 16, `reading.record` 2, `reading.check` 2, `reading.reopen` 1. The 98 and 16 rules deactivated on 2026-10-24 and 2026-11-13, and the 38 `lexical.enrich`, `lexical.meaning` and `lexical.relational` rules already inactive, need no action. The reading rules describe one pass that does the lexical and the inner-being work together; the proposed classification (from the rule text, to be confirmed rule by rule at build):

| Class | Rules | Disposition |
|---|---|---|
| Lexical-structural: belongs to layer 0 | RG-08 (the original word), RG-09 (face), RG-14 (morph read), RG-16 (homonym, data error), RG-21 (grain, B:113), RG-24 (adverbial qualifier), RW-04, RW-05 (concise, span-grounded) | **SPLIT**: restated as LR rules for layer 0; the inner-being rule keeps only what the face does for the inner being |
| Mixed: structure and inner being in one rule | RG-03 (role per occurrence), RG-05 (relational and pointer), RG-07 (negators, connectives, body parts), RS-01, RS-03 (surfaces evaluated "by the tests of the lexical work") | **SPLIT**: the structural half to layer 0 step 0.2, the inner-being half stays |
| Inner-being: stays | RG-01, RG-02, RG-04, RG-06, RG-10, RG-11, RG-13, RG-15, RG-18, RG-22, RG-23, RG-25, RS-05, RN rules on claims | **KEEP** |
| Generic recording, applies to both | RO1, RO2, RO11, RG-17, RG-19, RG-20, RW-01 to RW-03, RW-06 to RW-11, RS-02, RS-04, RS-06, RS-07, RS-08, RS-10, DA-02 | **KEEP**; scope also names the lexical steps where they apply (3.8) |
| Scope and home (cluster or subgroup) | RM-01 to RM-04, RO3 to RO6, RO8, RO10, RS-07 | **#2448** |

`reading.narrate` has 16 active rules; only RN-11 (words and terms, names the M-code) was found by the scan and the others were not read for this inventory: **to be read at build** (3.12).

### 3.7 Behaviour rules and rule scopes

| Rule | Finding | Disposition |
|---|---|---|
| B:133 `lexical-and-claims-readings-are-separate` | names the lexical gate of my build | **REWORD** to step 0.2 |
| B:132 `collection-reading-runs-in-layers`, B:130 (`nodes-index-the-collection...`, names role and relational) | | **REWORD** for layer 0 and the role group `lexical` |
| B:113 (grain), B:121 (reading recorded per occurrence) | delivered at `Reading.ps1` and `Verse-Scope.ps1` only; layer 0 runs under `Collection-Build.ps1` | **ADD** the `cfg_rule_scope` rows (`ps` `Collection-Build.ps1`) |
| B:7 `cost-cap-before-call`, B:8 `usage-log-required`, B:9 `sonnet-default-model` | delivered at `VerseLexical.ps1`, written for the API generators | **DECIDE** with D6 |
| B:119, B:120, RO13 | rules say collection; `Reading.ps1 -Step Open` opens a subgroup (my breach of 2026-11-15) | **#2448** |
| B:67, B:71, B:110, B:94, B:116 and the other cluster rules | not the lexical process | **#2448** |
| B:68, B:73 | already inactive | none |

### 3.8 Rule delivery

`cfg_rule_scope` delivers B:7 to B:9 at `VerseLexical.ps1` and B:113, B:119 to B:121 at `Reading.ps1` and `Verse-Scope.ps1`. The layer machinery (`Collection-Build.ps1 -Action Layer*`) is reached by B:130 to B:133 (general) and the method rules LR-01 to LR-05. Layer 0 adds the grain rule and the per-occurrence rule to that scope (3.7).

### 3.9 Documents

| Document | Finding | Disposition |
|---|---|---|
| `iba/app/USER-GUIDE.md` section 6 "Verse lexical and the debate pipeline (book-scoped)" | lists `lexical.enrich -PayloadPath`, `report.lexical_exceptions`, `lexical.notes`; the retired Layer 2 | **REWORD** (D7) |
| section 7 "Cluster-reading pipeline" | tells the reader to run `VerseReading.ps1`, `RelationalReading.ps1`, `Run-Stage1Batch.ps1`, with "Stage 1" language and the "role arrays are stale" refusal | **REWORD**: the retired scripts named as retired, and where the lexical observations are made |
| the layered reading paragraph (mine, 2026-11-15) | layers 1 and 2 only | **REWORD**: layer 0 |
| section 8.16 `verse_lexical` and the unit; line 337 `Lexical-Readiness.ps1` | base data | **KEEP** |
| `iba/app/GOVERNANCE.md`, `iba/app/CHARTER.md` | no mention of the old lexical process or of the layers | **KEEP**; B:3 forbids a copy, so only a pointer is added if B:132 gains one |
| `iba/app/BUILD.md` | history | an entry for the change |
| `iba/docs/ps tools worksheet.xlsx` | not scanned (3.12) | the rows of the three retired scripts removed; the Collection-Build tab updated |
| `.claude/commands`, `.claude/hooks` | no mention | none |

### 3.10 Scripts

`ps/VerseReading.ps1`, `ps/RelationalReading.ps1`, `ps/Run-Stage1Batch.ps1`: **RETIRE**. `ps/VerseLexical.ps1` (28 hits; also carries the steps `lexical.build`, `lexical.readiness`, `report.*`): **SPLIT**, its `-Step` list loses the retired steps. `ps/ClusterSubgroup.ps1` (2 hits): **#2448**.

### 3.11 Data

`ib_observation` live observations by stage, for the kinds that mean lexical work (the kinds are written outside any lexical process):

| Stage | Observations | Lexical kinds |
|---|---|---|
| verse-reading (old catalogue tags) | 5,522 | the tags are the retired catalogue's; 6,142 nodes, all without a role |
| prior-capture | 6,709 | face 470, link 336, term 113, use 59 |
| engagement | 520 | face 109, use 117, link 21, qualification 67 |
| Analysis_phase_1 | 522 | face 73, link 53, party 62, qualification 14 |
| reading | 27 | term 11, face 11 |
| char-reading, char-subgroup, char-answers, strand-reading | the retired September stages | history |

No observation exists in a stage `lexical`. (D5.)

### 3.12 What this inventory did not reach

1. `reading.narrate` (16 rules), `reading.open` rules RO3 to RO6 beyond their first 170 characters, and `cfg_setting` hits that the word list does not contain: not read in full.
2. The three Excel worksheets in `iba/docs` were not opened; the retired scripts' rows are expected there.
3. `iba/docs` (about 20 files naming the old steps, engineering notes, `cfg_control_home` kind `engineering_note`), `Workflow/Instructions`, `Workflow/Programme`, `Workflow/Catalogue`, `Workflow/schema/*.csv` and `iba/app/reports`: counted only. They are history or generated output; the origin of `Workflow/schema/*.csv` is not established and is checked at build (regenerate, or find that nothing reads it).
4. A word search finds a rule that names the old process; a rule that describes it without the words is found only where I read the text (3.6).
5. Items I took as cluster- or subgroup-only in 3.1 and 3.7 are not examined for the lexical process; they belong to #2448.

Because the inventory is a scan, it can be repeated: D9 makes the scan a stored check, so completeness is shown by a run and not by my statement.

## 4. The design

**D1. Layer 0 through the machinery just built.** `cfg_setting layer.reading` gains a layer 0 with two steps and the stage `lexical`; the ledger, working file, recorder, check and group on the node are used as they are, generalised for the new items. The gate of step 1.1 becomes "step 0.2 is closed", replacing `lexical_gate`.

| Step | Item | Kind | Subject and grain | Nodes |
|---|---|---|---|---|
| 0.1 words | word-lexical | term | each member surface and lettered Strong's code of the collection (never the bare lemma, B:113, RG-21): name, kind, boundary, grammatical forms, root and semantic range, aspect, structural opposite, Testament context, coinage, by the 26 prompts | every occurrence of that surface and code |
| 0.1 words | word-face | face | each occurrence whose meaning diverges from the usual sense (M0.5.11); none allowed with a reason | that occurrence |
| 0.2 structure | verse-structure | link | each verse holding a member occurrence: how the member words stand (typed neighbours with side and distance, connectives, negators and their reach, entity and pronoun references, qualifier presence); no inner-being statement | the member occurrences and the neighbours named |

**D2. A role for a lexical node:** a group `lexical` (value `lexical`) in `reading.node_roles`; B:130's role requirement holds and the gate tests for it.

**D3. Retire** `lexical.meaning`, `lexical.relational`, their grants, settings, utilities, the three scripts, `versereadinggenerate` and `stage1coverage`; split `handlers/lexical.py` and `VerseLexical.ps1`.

**D4. Guidance:** the 26 prompts guide step 0.1; the stale catalogue text is corrected; LR-01 to LR-05 gain the lexical items; the rules in 3.6 are split as classified; B:132 and B:133 reworded.

**D6 (new). The shared generation code.** The retired cluster generators and the two old lexical steps share one LLM client (`lexicalenrichgenerate`) and one helper (`versereadinggenerate._meaning_sources`), with nine `lexical.llm_*` settings and B:7 to B:9. Either (A) retire the whole dead chain together (the five generators, the nine settings, the rule scope of B:7 to B:9), after an import trace shows nothing active calls it; or (B) keep the client and its settings under a neutral name for the later claims work. I recommend A: nothing active uses them after D3, and a kept unused client is the kind of residue the researcher has said is choking the process.

**D7 (new). The report and notes surface of the retired Layer 2** (`report.lexical_exceptions`, `report.lexical_extract`, `lexical.notes`, `verse_lexical_note`): retire with its USER-GUIDE section, or keep as reports of what exists. I recommend retire.

**D8 (new). The boundary of engagement and the reading prompts.** Engagement (#2406) and the reading's `observe_prompts` already hand the M0 lexical prompts to inner-being work and already write face and term observations. I recommend: the lexical prompts move to step 0.1, the reading and engagement read the layer 0 observations as their base, and their face observations state only what a face does for the inner being.

**D9 (new). A stored alignment check:** a config check run by `Config-Validate` that lists every active step, utility, setting, method rule, behaviour rule, rule scope and every guidance section that names a retired lexical entry without a disposition; the scans of 3.0 are its seed. Layer 0 is not closed until it runs clean.

**D10 (new). The place of the lexical observations in `governance.programme_stages`:** a new stage between Base_data and Analysis, or part of Base_data. I recommend a stage of its own named "Lexical observation".

**D5 (open from v1).** The 6,142 nodes of the old stage and the face, term and link observations of the four other stages (3.11): re-read into the lexical stage by the collection that carries them (as the prior documents were, #2498), or left as history.

## 5. Decisions for the researcher

| # | Decision | Recommendation |
|---|---|---|
| 1 | D1: layer 0 through the new machinery, or adapt the cluster-based steps | the new machinery |
| 2 | D2: the role `lexical` | yes |
| 3 | D3: retire the old steps and scripts | yes |
| 4 | Grain of step 0.1: per surface and lettered code, or per surface | per surface and lettered code |
| 5 | D5: the existing nodes and the face, term, link observations | re-read by collection |
| 6 | D6: the shared generation chain | retire together |
| 7 | D7: the Layer 2 report surface | retire |
| 8 | D8: the engagement and prompt boundary | lexical prompts move to layer 0 |
| 9 | D9: the stored alignment check | yes |
| 10 | D10: the programme stage | a stage of its own |

## 6. If approved, the build

In this order, one unit of work with a snapshot, a test on a copy and the check D9 run before and after: config (`layer.reading` layer 0, stage, role group, items, gate; `cfg_rule_scope` rows; the method rule split; B:132 and B:133; the retirements of 3.1 to 3.4; the catalogue and column text); code (`layerreading.py` generalised, pull evidence for 0.1 and 0.2, the archive moves after the import trace, `handlers/lexical.py` and `VerseLexical.ps1` split); documents (USER-GUIDE sections 6 and 7 and the layered paragraph, the worksheets, BUILD); then the first run on `thought` by the ledger. The two steps named in 3.12 as not reached are read first.
