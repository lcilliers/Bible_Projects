# The surface cycle in the database: design v3 (reuse of existing tables, AI control, working files), #2361

> Developer Mode session 325129d4, 2026-11-06. Nothing is built. This version builds in every comment the researcher made on design v2 (verbatim on #2361 v7). It replaces v2 (archived). The researcher's instruction on the last point: "go ahead if you are confident that all my comments have been properly considered and built into the proposal"; section 1 shows where each one is handled and section 13 states the confidence and what is not yet certain.

## 1. Each comment of the researcher, and where it is handled

| Comment | Handled in |
|---|---|
| Test cases and human reviews from prototyping are in-progress work, not the ultimate decision | 5.4: they load as `provisional`, results are shown as against provisional cases, never used as a gate or as truth |
| Why a new `surface_term`? Use or extend existing tables with columns; no table that repeats existing data and forces routines to keep tables in sync. Include a clear map of old and new tables | 2 (the audit of what exists), 3 (the map), 4 (what is extended, re-grained, new) |
| 11.2 agree: rebuild G1 to G5 from their recorded outputs, history G7 and G8, the sweep G9 | 9 |
| 11.3 folders `_analytics/surfaces/working_files` and `_analytics/surfaces/exports` | 8 |
| 11.4 zeta-assist: clear documentation, mapping and control; prompts and outputs reproducible and visible; prompts tracked, to know which worked best | 6 |
| 11.5 working files and methods reset to be app ready, not one-off exercises | 8.4, 10 |
| 11.6 history of a method that will not be needed again is discarded and not registered | 8.5 |
| 11.7 junk surfaces that are errors of the past are marked as deleted | 7 |
| 11.8 go ahead if confident | 13 |

## 2. What already exists, and what I had wrongly proposed to duplicate

Checked in the live schema (121 tables, `cfg_table.use` read for each of these):

| I had proposed | What exists | Decision |
|---|---|---|
| `surface_term` (a table of distinct surfaces) | **No table is at the grain of the distinct surface.** The surface text sits in `verse_lexical` (1,520,168 rows), `span`, `ib_node` and `reading_strand_hit` (per occurrence) and in `surface_subgroup` (13,462 rows) and `surface_pair_verdict` (0 rows), which are per (Strong's code, surface) pair. The pair tables cannot carry a judgement made on the text alone (ruling of 2026-11-02): the group or base of `love` would repeat on every code it occurs under and have to be kept in step | re-grain the **empty** `surface_pair_verdict`, which #2354 created for exactly this and nothing ever wrote, into the surface-grain table `surface_term` (section 4.2); retire the unread column `surface_subgroup.surface_group` (no routine reads it) |
| `surface_base` | a base is itself a surface (`sin` is a surface) | no table: `surface_term.base_id` points to another `surface_term` row; a base that is not a surface (`adulter`) is a row with `origin = computed` |
| `surface_run` | `run` (6,268 rows: run id, work package, params, config version, state, resume point, outcome) | reuse `run`; add `settings_snapshot` and `counts` |
| `lib/aicycle.py` and a task queue | `run_batch` and `lib/batchcontrol.py` (the sole writer): batch control, resume and skip, crash safeguard, live progress, "for every long-running LLM-calling step" | reuse; the AI cycle is built on it; add `model_role`, `model`, `calls`, `secs` |
| `analytic_file` | `file_manifest` (25,016 rows, every file of the tree) and `folder_purpose` (959 folders) | extend `file_manifest` with `module`, `run_id`, `sha256`, `analytic_status`, `migrated_from`; change `manifest.rebuild`, which now deletes and re-inserts every row, to update by path so the added columns survive; register the new folders in `folder_purpose` |
| `collection_pole` | none | folded into `collection` as columns (a pole is one value per collection) |
| the `cfg_connection` and `cfg_api` for zeta-assist | they hold the STEP server only; the Ollama server is `cfg_setting` module `ollama` | new registries for the AI use (section 6): they are not a repeat of anything |
| `surface_flag` | `escalation` (open items) | keep: thousands of per-item flags are not escalations; a flag may carry its `escalation_id`, and an escalation carries counts and the report path, never the lists (B:40) |
| `surface_event` | per-domain change tables (`ib_observation_change`, `narrative_claim_change`, `debate_change_detail`) | follow the convention: one change table for this domain |

## 3. The map of the tables, old and new

```
EXISTING (unchanged unless marked)                                   NEW or CHANGED (marked + or ~)
------------------------------------------------------------------   ---------------------------------------------------------------------
strong (15,455)  <----------------------------+
verse (29,762)                                  |
   ^                                            |
span (378,182) --> verse                        |
   ^                                            |
verse_lexical (1.52M) -- strong, verse, span    |
        .surface  (lower/trim) ------------------------------------>  ~ surface_term   (one row per distinct surface text; join: surface)
                                                |                          .base_id --> surface_term.id   (self: a base is a term)
cluster_strong (cluster_code, strong) ----------+                          .group / base / collection states
cluster (96)                                                               .deleted  (junk surfaces)
   ^                                                                              ^            ^
cluster_subgroup (572) -- cluster_code                                            |            |
   ^                                                                       + surface_derivation   (evidence for a base: structure, sibling, ollama)
surface_subgroup (13,462)  (cluster_code, strong, surface, subgroup)       + cfg_base_construct   (79 construct rules, config)
   .surface --- join by text ---> surface_term.surface                      + collection ---------> core term (surface_term.id)
   ~ column surface_group retired                                                  .concept_id ----> concept.id   (the later rollup, NULL now)
   ~ junk rows deleted=1                                                    + collection_link     (collection x term x tier: core, synonym, opposite,
concept_subgroup (411) -- concept, cluster_subgroup                                                 possible_opposite, associated, set_aside)
   ^  (replaced by collection.concept_id after the rollup, ruling D1)       + collection_listing  (words the model listed for a collection)
concept (101) -- domain_id, narrative_section_id                            + surface_flag        (exceptions to settle; escalation_id optional)
   ^                                                                        + surface_event       (every revision: who, what, before, after, why)
concept_domain (14) -- narrative_chapter_id                                 + surface_eval_case   (method test cases, standing provisional)
                                                                            + ai_call             (every AI call: prompt version, model, request, answer)
run (6,268) <--------------- run_id on every new row                        + cfg_ai_prompt       (every version of every prompt)
   ~ settings_snapshot, counts                                              + cfg_ai_model        (the models on zeta-assist and their roles)
run_batch (236) -- run_id (the AI cycle control)  ~ model_role, model,
   calls, secs
file_manifest (25,016) -- path   ~ module, run_id, sha256, analytic_status, migrated_from
folder_purpose (959) -- folder_path  (+ rows for the new folders)
escalation (1,634) <--- surface_flag.escalation_id
```

**How to navigate (the paths an analysis uses):**
1. A surface in the corpus: `verse_lexical.surface` = `surface_term.surface`; from the term to its group, base (`base_id`), evidence (`surface_derivation`), collection (`collection_link`) and every AI call behind it (`ai_call.subject_id`).
2. A surface to the old cluster work: `surface_term.surface` = `surface_subgroup.surface` (with `strong`) then `cluster_subgroup_id` then `concept_subgroup` then `concept`; this is the later cross-check against clusters.
3. A collection to a concept: `collection.concept_id` to `concept.id` (domain and narrative section follow from `concept`).
4. Any value to its origin: row, evidence, `ai_call` (prompt version, model, request), `run_id` to `run` and `run_batch`, and for loaded rows `load_ref` to `file_manifest.path`.

## 4. The tables

### 4.1 Extended existing tables (columns added, no new table)

| Table | Added | Why |
|---|---|---|
| `run` | `settings_snapshot`, `counts` | the settings and prompt versions in force and what the run produced; `work_package` already names the module |
| `run_batch` | `model_role`, `model`, `calls`, `secs` | the AI cycle control; `cost_usd` stays 0 for local models |
| `file_manifest` | `module`, `run_id`, `sha256`, `analytic_status` (live, regenerable), `migrated_from` | the working-file registry; `manifest.rebuild` changed from delete-and-insert to update by path |
| `folder_purpose` | rows for the new folders | purpose, status, governing setting |
| `surface_subgroup` | none; the unread column `surface_group` is retired; junk rows get `deleted = 1` | no repeated data |

### 4.2 Re-grained: `surface_pair_verdict` becomes `surface_term` (0 rows, no data loss)

| Column | Meaning |
|---|---|
| `id`, `surface` (unique), `form` (word, phrase), `origin` (surface, computed) | the key and what it is |
| `scope` (a behaviour and state, b being, c other) | which study the surface belongs to; b and c are loaded and untouched |
| `surface_group`, `group_reason`, `group_state` | the current group and its state |
| `base_id` (self), `base_source`, `base_state` | the current base and its state |
| `collection_state` | the state of this term as a base in collections |
| the standard `run_id`, `created_at`, `updated_at`, `created_by`, `deleted`, `load_ref` | provenance |
`strong` and `pair_kind` are dropped (a pair's trust is derivable from `verse_lexical` and is not a property of the text); `use` (for a qualifier) stays.

### 4.3 New tables (eleven)

| Table | One row per | Key columns |
|---|---|---|
| `surface_derivation` | evidence for a base (append-only) | `term_id`, `method` (structure, sibling, ollama, own, researcher), `evidence` (construct id, sibling group, `ai_call` id), `kind` (inflection, derivation, lead_opposite, lead_other, lead_starts_with), `base_word`, `accepted`, `status` (live, superseded) |
| `cfg_base_construct` | construct rule (79), config | `id`, `kind`, `direction` (same, candidate), `strip`, `add`, `undouble`, `strip_prefix`, `description`, `example`, `active` |
| `collection` | collection (48) | `core_term_id`, `name`, `status` (indicative, confirmed, merged, retired), `merged_into_id`, `concept_id`, `pole_word`, `pole_of_pole`, `pole_reciprocal`, `pole_real_word` |
| `collection_link` | (collection, term, tier) | `tier`, `status` (live, superseded, removed), `superseded_by_id`, `shared`, `ai_call_id` |
| `collection_listing` | word the model listed for a collection | `word`, `kind` (synonym, opposite), `term_id`, `outcome` |
| `surface_flag` | exception to settle | `subject_kind`, `subject_id`, `kind`, `note`, `status` (open, settled), `escalation_id` |
| `surface_event` | revision (append-only) | `subject_kind`, `subject_id`, `action`, `field`, `before`, `after`, `by`, `reason`, `run_id` |
| `surface_eval_case` | method test case | `module`, `step`, `a`, `b`, `expected`, `source`, `standing` (provisional, confirmed), `note` |
| `ai_call` | every AI call (append-only) | see 6.3 |
| `cfg_ai_prompt` | prompt version (config, append-only) | see 6.2 |
| `cfg_ai_model` | model on the server (config) | see 6.1 |

All are built from their `cfg_column` rows; every table and column note follows the standard of section 11. No new table repeats a value held elsewhere; the only stored derived value is the three `*_state` columns, written in the same transaction as the change and proved equal to the evidence by the `check` step.

## 5. The modules, the states and the AI passes

### 5.1 Five modules, each a work package, each repeatable alone

1. **surface-group** (extends `Surface-Judge.ps1`): judge each surface; corrections (`group.repoint`); writes `surface_term.surface_group`, `ai_call`, events.
2. **surface-structure** (new): apply `cfg_base_construct` to the scope-a terms; writes `surface_derivation` (hits, leads, siblings) and flags.
3. **surface-base** (extends `Surface-Base.ps1`): the AI base of **every** single word, an independent second opinion; disagreements become flags.
4. **base-resolve** (new): resolve order from settings (structure, sibling, AI, own); writes `surface_term.base_id`, `base_source`, `base_state`, and the computed-base terms.
5. **collection-build**: seeds, shortlist by embedding, judges, listing, pole, associated tier, outlier review; writes `collection`, `collection_link`, `collection_listing`.

Each has `status`, `show` (with `-Explain`), `export` and a re-run step, and runs its long AI work through the shared cycle (5.3).

### 5.2 States (enums; each value defined in its column note)

`group_state`: unjudged, judged, failed, corrected, confirmed. `base_state`: out_of_scope, phrase_not_tested, unmatched, matched_structure, matched_sibling, lead_only, ai_answered, ai_none, ai_failed, resolved_own, resolved, flagged, confirmed. `collection_state`: untouched, placed, set_aside, listed_only, shared. `collection_link.tier` and `status`, `collection.status`, `surface_flag.status`, `ai_call.outcome` (answered, refused, failed, halted), `cfg_ai_prompt.status` (draft, active, retired).

### 5.3 The AI cycle

The unit of work is a batch in `run_batch` (`lib/batchcontrol`: content key, resume and skip, crash safeguard, progress): work periods with a cool-down, retry after a halt, stop flag, started outside the session (B:125). The items of a batch are the terms whose state is pending or failed; there is no file queue. Every module has a deterministic pass, an AI pass and an AI audit of the disagreements (for example: the AI checks every structure hit for same root meaning; the AI base is run on every word; the reviewer role rules only the borderline).

### 5.4 Test cases and human reviews are provisional

`surface_eval_case.standing` is `provisional` for everything loaded from the prototyping (the 53 opposite pairs, the 36 and 64 synonym cases, the opposite cases, and the human-test labels). A report that uses them says "against provisional cases". They inform and compare prompts; they never decide, gate or activate anything, and the researcher confirms a case to change its standing.

## 6. Zeta-assist: documentation, mapping and control

### 6.1 `cfg_ai_model`: what is on the server and what it is for
One row per model on zeta-assist (today qwen3:30b, qwen3-embedding, nomic-embed-text, qwen3-coder:30b, qwen2.5-coder:3b): `name`, `tag`, `digest`, `parameters`, `role` (judge, embed, embed_fast, quick, reviewer), `purpose`, `status` (active, retired), `pulled_on`. A module names a **role**, the role resolves to a model in settings, so a model is replaced in one place.

### 6.2 `cfg_ai_prompt`: every prompt, every version
`prompt_key`, `version`, `text`, `hash`, `role`, `purpose`, `expected_output`, `status` (draft, active, retired), `parent_version`, `change_note`, `created_by`, `created_at`, `activated_at`. Append-only: changing a prompt is a **new version** made by a step that records the change note; `cfg_setting` holds only which version is active per key. The prompts now in scratch scripts and the earlier versions of the group and base prompts (v1 to v3, the amended base question, the drifted collection wordings) are loaded as retired versions with their text, because which prompt worked best is the point of the register.

### 6.3 `ai_call`: every call, reproducible
`run_id`, `batch_id`, `module`, `step`, `role`, `model`, `model_digest`, `prompt_key`, `prompt_version`, `prompt_hash`, `options` (temperature, seed, context, format, reasoning), `request_hash` (prompt plus variables), `subject_kind`, `subject_id`, `request`, `answer`, `result`, `score`, `via`, `outcome`, `error`, `tokens`, `secs`.

### 6.4 Control
- **One route.** All calls go through `lib/aiclient.py`: it refuses a model that is not active, a prompt that is not active, options outside settings, runs the server check and halting of B:124, and writes the `ai_call` row. No module calls the server any other way.
- **Replay.** `ai.replay` re-sends a stored request and reports where the new answer differs: the measure of reproducibility.
- **Compare.** `ai.compare -Step <step>` reports, per prompt version and model, over the evaluation cases and the live results: answered, failed, agreement with the cases (provisional), seconds. The result is a view on demand, so "which worked best" is never a stored claim.
- **Status.** `ai.status`: the server and tunnel, the models loaded, calls today by module, prompt and model.
- **Documentation and mapping.** A generated section of the config report, "The AI use map" (module and step, role, model, prompt key and active version, settings), and a chapter of USER-GUIDE.md "Using zeta-assist" with the rules, the registers, the control and the recipes.

## 7. Junk surfaces

Four surfaces in `surface_subgroup` are errors of the past, found by an objective rule (empty; no letter; punctuation inside the text): the empty string (4 pair rows), `^` (4 rows), `32,000` (1 row) and `you, do` (1 row): **4 surfaces, 10 pair rows**. The rule is a setting (`surface.junk_rules`) so a later scan finds the same; a step `surface.junk_mark` previews the effect (the subgroups the rows sit in) and then sets `deleted = 1` on the pair rows and on the term rows, each with an event. `a` and `i` are real words and stay. Of the 408,392 `verse_lexical` rows with no surface, 408,274 are NULL (occurrences with no English of their own, to be confirmed) and **118 hold an empty string**, which is the source of the empty-surface pair rows; those 118 are an error of the past, recorded as a flagged item, and changing `verse_lexical` is outside this build and needs the researcher's decision (stage 0 sweep, finding 2).

## 8. The `_analytics/surfaces` branch, the migration and working-file management

### 8.1 Layout
```
_analytics/surfaces/working_files/   files used during the method processing
      group/  structure/  base/  collection/  embeddings/ (regenerable)  import/ (the one place a file may be read as input)
_analytics/surfaces/exports/         the results of surface analysis, for inspection (workbooks, reports)
```
### 8.2 Migration of existing files
By a mapping table in the migration: the surface-cycle files move (git `mv` where tracked) from `outputs/concept-mapping/` to the folders above; each moved file gets its `migrated_from` in `file_manifest`. Plans and designs for the researcher stay in `outputs/escalation/` (B:60).
### 8.3 Rules (new `cfg_behaviour_rule` rows and settings)
A module writes working files only under its folder; every working file is in `file_manifest` with its module and run; the naming pattern is B:56 and B:57; **a file is never an input except from `import/`**; an embedding file is regenerable and rebuilt when absent; the root and folders are settings (`surfaces.working_files_root`, `surfaces.exports_root`).
### 8.4 App-ready reset
The scratch scripts and one-off file names are not carried over: each method becomes a parameterised module reading settings and tables, each working file takes the pattern name, and no script named for an experiment remains in use.
### 8.5 History
History is registered only for a method that may be needed again: the counting group run and its corrections, the Ollama answers, the structure output, the collection runs that count, and every prompt version. A method that will not be needed again is **discarded and not registered**: the cluster-based perspective, the stemmer families and the pilot runs of superseded wordings. Their files are not deleted (no deletion without your approval); they move to `_analytics/surfaces/discarded/`, outside the registry and outside every read path.

## 9. The components whose code is gone (agreed 11.2)

G1 structure matching: exact reproduction of 1,386 hits, the status counts of both versions, 681 unmatched, 47 sibling groups, 26 outside-list bases. G2 the 56-change repoint and the 52 held pairs. G3 the combined base for all 3,850 surfaces (structure 1,246, Ollama 387, own 2,217). G4 Ollama result handling (676 answered, 31 failed, 22 flagged, 289 "none"). G5 the collection prototypes (tally 255, 77, 238, 733, 23). G6 the method tests as provisional cases. G7 and G8: see 8.5 and 5.7. **G9** closes the list: a sweep matches every file under `outputs/` and `_analytics/` newer than 2026-10-26 to its producing code before anything is built. Each of G1 to G5 is specified from its recorded output before it is coded and accepted only on its reproduction check; a point the output does not settle is raised to you before the code (B:44).

## 10. Back-trackable

Value, then evidence, then `ai_call` (prompt version, model, request), then `run` and `run_batch`, then for loaded rows the source file and line (`load_ref` to `file_manifest`). Revisions supersede and are events. `show -Explain` prints the chain for a surface, a term, a collection or a link.

## 11. Descriptions, notes and guidance

Standard (a rule): every `cfg_table.use` begins with the module and stage ("Module 2 of 5, structure: ..."), the grain, what writes it and what reads it; every `cfg_column.use` says what the value means and, for a key, what it points to and how to navigate; every state value is defined. A generated section of the config report, "The surface cycle map" (modules in order, tables, steps, states, foreign-key paths, from `cfg_column`, so it cannot drift). USER-GUIDE.md: a chapter "The surface cycle" (the picture of section 3, the state dictionary, recipes: from a surface to its collection, why a word is set aside, what is unmatched, what changed and who changed it, what was judged with which prompt and model). GOVERNANCE.md: the mechanism only, pointing to rule keys. BUILD.md: one entry per stage. `ps tools worksheet`: one tab per tool.

## 12. Load, tests, build order

Named snapshot (`dbsnapshot.py --named`); work on a copy (`copy_db`). Order: **0** sweep (G9), file migration, `file_manifest` change; **1** tables, config, loader, junk marking, reconciliation (6,069 terms by group, 2,481 bases by source, 676 and 31 Ollama answers, 48 collections, the tally, 4,170 calls, every loaded row with a `load_ref`); **2** structure and repoint on exact reproduction; **3** group, AI base and resolve writing the tables; **4** `aiclient`, prompt and model registers, replay and compare; **5** collection module; **6** notes, generated maps, guide, BUILD, worksheet. Each stage on a copy first, with the independence test (working files moved away; every module's `status`, `show`, `export` and re-run still works), `Config-Maintenance.ps1 -Step Validate` clean, the existing tests of the group and base tools updated and passing; the result of each recorded on #2361. The live load only when the stage reconciles.

## 13. Confidence, and what is not yet certain

- Every comment of the researcher is traced in section 1. I am confident of the design as the researcher's rulings define it.
- **Choices I made inside those rulings, not new decisions** (reversible before data is loaded): re-graining the empty `surface_pair_verdict` into `surface_term` (the alternative is a differently named new table, which the researcher's rule argues against); folding the base into `surface_term` by a self-reference; folding the pole into `collection`; changing `manifest.rebuild` to update by path; the junk rule of section 7.
- **Not yet known, settled by stage 0 before any code:** the producers of files with no recorded origin (G9); whether the 408,392 empty `verse_lexical` surfaces are by design; the flag rule of the Ollama workbook (G4), which is read from the workbook.
- A point that the recorded outputs do not settle will be put to the researcher before it is coded.
