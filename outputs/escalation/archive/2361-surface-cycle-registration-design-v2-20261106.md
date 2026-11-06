# The surface cycle in the database: tables, modules, working files and load, design v2 for approval (#2361)

> Developer Mode session 325129d4, 2026-11-06. Nothing is built. This version answers the researcher's refinements of 2026-11-06 (recorded verbatim on #2361): all analytic files in the `_analytics` branch with a migration and working-file rules; local AI cycles baked into every method; every component of the last ten days whose code is gone refactored, with no gap left to redesign in flight; the state of every item held in the tables; the app description, column notes and guidance clear about how the processes fit and how the tables link; everything back-trackable. It replaces design v1 (archived). New tables and a new mechanism are a design, so it comes to the researcher first (B:105, B:44).

## 1. What changed from v1

| Refinement | Where answered |
|---|---|
| `_analytics` branch, migration of existing files, working-file rules | section 4 |
| AI to the maximum, local cycles baked in | section 5 |
| Components whose code is gone, refactored | section 3 |
| State of every item in the tables | section 6 |
| Clear description, column notes, guidance, relationships | section 7 |
| Back-trackable | section 8 |

## 2. How the pieces fit

```
 surfaces (6,069)                                             scope a = behaviour + inner being state (3,850)
     |                                                        scope b = being (716), scope c = other (1,503): loaded, untouched
     v
 [1 GROUP]      judge each surface text            -> surface_term.surface_group      (+ corrections, AI audit)
     |
     v  (scope a only)
 [2 STRUCTURE]  79 construct rules on the words    -> surface_derivation (hits, leads, siblings)   (deterministic + AI check of each hit)
     |
 [3 BASE-AI]    Ollama base form of every word     -> surface_derivation (method ollama)           (independent second opinion; disagreements flagged)
     |
     v
 [4 RESOLVE]    evidence + resolve order           -> surface_term.base_id, surface_base           (+ AI arbiter on conflicts)
     |
     v  (single-word bases)
 [5 COLLECT]    seeds, shortlist, judges, poles    -> collection, collection_link (tiers)          (embeddings + 5 judges + AI review)
```

Each module is a work package of its own. It reads the tables the one before wrote (never a file), writes its own, records a run, and can be repeated alone. Stages 1 and 5 existed as tools or prototypes; stages 2 to 4 existed as outputs only.

## 3. Inventory of the components whose code is gone, and their refactor

Sources: the session logs of 2026-10-31 to 2026-11-05, `BUILD.md`, the files themselves. "Reproduction" is the check that the rebuilt module gives the recorded result.

| # | Component (what it did) | What survives | Becomes | Reproduction check |
|---|---|---|---|---|
| G1 | **Structure matching** v1 to v3: normalise the 3,850 surfaces, apply 79 construct rules (strip, add, undouble, prefix; direction same or candidate), find bases, statuses, leads (opposite, other, starts-with), sibling groups with computed bases, bases found outside the list | `surface-match-control-v3` json: the 79 constructs, 1,386 hits, normalised list, 47 sibling groups, counts per status | module 2, `cfg_base_construct` rows, `surface_derivation` | exactly: 1,386 hits, all status counts of v1 and v2, 681 unmatched single words, 26 outside-list bases |
| G2 | **Group correction (repoint)**: the base word of derived words moved into the derived words' group (56 applied, 52 pairs on 39 bases held), by an explicit list after a regex slip | `first-split-v4` (changed lines carry `original_group`, `corrected_by`, `correction_basis`), `surface-repoint-m1` workbook (Applied, Held) | module 1 step `group.repoint`: a rule over the structure derivations plus a held queue; held pairs become `surface_flag` rows | the same 56 changes and the same 52 held pairs |
| G3 | **Combined base and the inspection workbook**: structure base, else Ollama base (flagged), else the word itself; base in the list or not | `2359-surfaces-and-bases` workbook and its Columns tab | module 4 and the export step | the combined base and its source equal for all 3,850 surfaces (structure 1,246, Ollama 387, own 2,217) |
| G4 | **Ollama result handling**: accepted, none, failed; the flag column (possible opposites, moved meanings); the 289 unchecked "none" answers | `base-form-v1` jsonl, `2359-base-form-results` workbook (tabs Accepted with a flag column, None, Failed, Notes) | module 3, flag rules in config, `surface_flag` | 676 answered, 31 failed, 22 flagged opposites; the flag rule is read from the workbook at stage 0 and written as a setting |
| G5 | **Collection stage prototypes** (scratchpad, outside the project): the pool of single-word bases, embeddings (4 configurations), recall test, pair judge, seed rounds, the anchored judge, poles and reciprocity, model-listed words, the associated tier, the score and wording tests, the tally and the workbooks | the output files, `BUILD`-style notes in #2360 | module 5 and the evaluation step (section 5) | the tally (placed 255, set aside 77, listed only 238, untouched 733, shared 23) and the 4,170 judgements |
| G6 | **Method tests** (embedding recall on 53 opposite pairs; 36 true synonyms against 64 false ones; the opposite wording cases) | the case lists in the session scripts and logs | `surface_eval_case` and `eval` runs: every prompt or threshold change is tested against the recorded cases before use | the recorded results (for example the synonym wording: 28 of 36 found, 0 of 42 false let in) |
| G7 | **Cluster-based first perspective** (`surface-group-rows`, `surfaces-vs-classes`, `subgroup-surface-classes`) and the **stemmer families** | the files | recorded as history in the file registry; the cluster comparison is a plain join of `surface_term` to `surface_subgroup` and the cluster tables, answered by the `show` step, and stays the reserved later cross-check (ruling of 2026-11-04). Not refactored as a process, because the researcher dropped it as a basis | none needed |
| G8 | **Pilots and the human test** of 2026-10-31 and 11-01 (`pilot-surfaces-*`, `surface-human-test-*`) | scripts exist in `iba/app/staging/`; outputs are files | history in the registry; the human test's labels, **if they are the researcher's own judgements** (not yet checked), load as researcher gold cases in `surface_eval_case` | to be read at stage 0 |
| G9 | **Anything not listed here** | unknown | **Stage 0, a sweep that closes the list**: every file under `outputs/` and `_analytics/` newer than 2026-10-26 is matched against the registered code (`cfg_utility`, `cfg_step`, `BUILD.md`); each with no producer is listed and classified (module, history, or deliverable) before any code is written | the sweep report is part of the approval of the build order |

**Rule against gaps:** for each of G1 to G5 the specification is written from the recorded output **before** the code, shown against the output, and the code is accepted only on its reproduction check. No process is left to be designed in flight; a point the output does not settle is a decision for you (B:44), raised before the code, not decided inline.

## 4. The `_analytics` branch, the migration and working-file management

The project already has `_analytics/` (Bible_Books, Clusters, lexicon, registry and others). The surface cycle gets one branch of its own:

```
_analytics/surface_cycle/
    group/         judge batches, progress files, corrections lists
    structure/     match exports
    base/          Ollama batches, pilots
    collections/   per-run batches, exports
    embeddings/    vector caches (regenerable, never an input)
    exports/       workbooks made by the export steps for inspection
    import/        the only place a file may be read as input (one-time load, or a researcher list to import)
    history/       superseded versions, kept and registered, out of the read path
```

- **Migration of existing files:** the files of the cycle move (a move, not a copy; `git mv` where the file is tracked) from `outputs/concept-mapping/{surface-group,collections}` and the surface files in `outputs/concept-mapping/` to the folders above by a mapping table in the migration; each move is recorded in the file registry with its old path (`migrated_from`). Nothing is deleted. The session logs and `BUILD.md` entries that name the old paths are history and are not edited; the registry answers "where did it go".
- **Escalation deliverables stay under `outputs/escalation/`** (B:60: plans, designs, one-off reports for the researcher). The workbooks that the export steps make for inspection go to `_analytics/surface_cycle/exports/`. This split is a decision for you (section 11, item 3).
- **Settings** (module `analytics`): `surface_cycle.root`, one folder setting per module, the naming pattern (B:56, B:57), the keep-live count per kind, the import folder.
- **Rules** (working-file management, new `cfg_behaviour_rule` rows):
  1. A module writes working files only under its folder in the branch.
  2. Every working file is registered when written (path, kind, module, run, sha256, size, status) and is named by the pattern.
  3. A file is never an input to a module; the import folder is the one exception, used by a named import step.
  4. The latest version of a kind is live; older versions move to `history/` in the same unit of work and stay registered.
  5. A cache (embeddings) is marked regenerable and the tool rebuilds it when absent.
- **Table `analytic_file`:** the registry. It also holds the old path of every migrated file and, for loaded rows, the file and line they came from.

## 5. AI to the maximum: local cycles baked into every method

Every module has three passes: **deterministic**, **AI**, **AI audit of the disagreements**. The AI runs on zeta-assist through the existing route (`ollama.*`, the ssh tunnel, the server check and halting of B:124).

- **Model roles in settings** (module `models`): `judge` (qwen3:30b), `embed` (qwen3-embedding), `embed_fast` (nomic-embed-text), `quick` (qwen2.5-coder:3b for cheap high-volume checks such as the real-word check, subject to the evaluation cases), `reviewer` (qwen3:30b with its reasoning on, only for the borderline band). A module names a role, never a model.
- **One cycle runner** (`lib/aicycle.py`, generalising `run_cycle` of `surfacejudge`): items to process are those whose **state** in the tables is pending or failed; work periods with a cool-down, retry after a halt, stop flag, progress, resume; started outside the session (B:125). No file queue.
- **Per module**

| Module | Deterministic | AI | AI audit |
|---|---|---|---|
| 1 group | resolve order for the current group | judge every surface (as built) | re-judge `other` and `being` and a sample of the rest with a second prompt; conflicts with the structure (a base and its derived words in different groups) go to the reviewer |
| 2 structure | the 79 constructs | the judge checks **every** hit for same root meaning (not only the unmatched), catching opposites and moved meanings such as `unfaithful` and `grateful` | the disagreements become flags |
| 3 base-AI | none | Ollama gives the base of **every** single word, not only the 681 the structure left | disagreement with the structure becomes a flag; the reviewer rules the borderline |
| 4 resolve | the resolve order | the reviewer arbitrates a conflict | the ruling is logged |
| 5 collect | shortlist by embedding | listing, anchored judge, score, pole, associated (as built) | an outlier check on each collection (a member that does not fit) and merge candidates by centroid similarity |

- **Evaluation as a standing step:** a prompt, threshold or model change is run against `surface_eval_case` (G6) and its result is stored, so tuning is repeatable and recorded.

## 6. The tables (fourteen), with the state of every item

All `data` tables except the rule table; built from `cfg_column`; each has `run_id`, `created_at`, `updated_at`, `created_by`, `deleted`, and a `load_ref` (the file and line a loaded row came from).

| Table | One row per | Key columns |
|---|---|---|
| `surface_term` | distinct English surface (6,069, plus the flagged empty one) | `surface`, `form` (word, phrase), `scope` (a, b, c), `surface_group` (current), `group_state`, `base_id`, `base_source`, `base_state` |
| `surface_base` | base (2,481) | `base`, `is_phrase`, `collection_state` |
| `surface_run` | run of any module | `module`, `kind` (run, rerun, load, eval, edit, import), `settings_snapshot`, `prompt_hashes`, `started_at`, `finished_at`, `status`, `counts` |
| `surface_judgement` | every model call, append-only | `module`, `step`, `surface_id`, `base_id`, `collection_id`, `prompt_key`, `prompt_hash`, `model_role`, `model`, `result`, `score`, `via`, `answer`, `outcome` (answered, refused, failed, halted), `error`, `secs` |
| `surface_derivation` | evidence for a base, append-only | `surface_id`, `method`, `evidence` (construct id, sibling group, judgement id), `kind`, `base_word`, `accepted`, `status` (live, superseded) |
| `cfg_base_construct` | construct rule (79), config | `id`, `kind`, `direction`, `strip`, `add`, `undouble`, `strip_prefix`, `description`, `example`, `active` |
| `surface_flag` | exception to settle | `subject_kind`, `subject_id`, `kind`, `note`, `status` (open, settled), `escalation_id` |
| `collection` | collection (48) | `core_base_id`, `name`, `status`, `merged_into_id`, `concept_id`, `pole_word` |
| `collection_link` | (collection, base, tier) | `tier`, `status`, `superseded_by_id`, `shared`, `judgement_id` |
| `collection_pole` | named pole | `pole_word`, `pole_of_pole`, `reciprocal`, `real_word` |
| `collection_listing` | word the model listed | `word`, `kind`, `base_id`, `outcome` |
| `surface_event` | each revision, append-only | `subject_kind`, `subject_id`, `action`, `field`, `before`, `after`, `by`, `reason`, `run_id` |
| `analytic_file` | working file | `path`, `kind`, `module`, `run_id`, `sha256`, `size`, `status` (live, history, regenerable), `migrated_from` |
| `surface_eval_case` | method test case | `module`, `step`, `a`, `b`, `expected`, `source` (researcher, claude), `note` |

**States (enums, each value defined in the column note):**
- `group_state`: unjudged, judged, failed, corrected, confirmed.
- `base_state`: out_of_scope (b, c), phrase_not_tested, unmatched, matched_structure, matched_sibling, lead_only, ai_answered, ai_none, ai_failed, resolved_own, resolved, flagged, confirmed.
- `collection_state` (on the base): untouched, placed, set_aside, listed_only, shared.
- `collection_link.tier`: core, synonym, opposite, possible_opposite, associated, set_aside. `status`: live, superseded, removed.
- `collection.status`: indicative, confirmed, merged, retired. `surface_flag.status`: open, settled. `analytic_file.status`: live, history, regenerable.
- `surface_judgement.outcome`: answered, refused, failed, halted.

A state is written in the same transaction as the row that changes it. The `check` step proves the stored states equal the states re-derived from the evidence and the links.

## 7. Making the description, the column notes and the guidance unambiguous

- **A standard for the notes (a rule):** every `cfg_table.use` begins with the module and stage ("Module 2, stage 2 of 5: ..."), states the grain, what writes it and what reads it. Every `cfg_column.use` says what the value means; every foreign key says **what it points to and how to navigate** ("`surface_term.base_id` → `surface_base.id`: the base this surface currently resolves to; from the base, `surface_derivation` holds the evidence").
- **A generated section** in the config report, "The surface cycle map": the five modules in order, each with its tables, steps, settings, states, and the foreign-key paths between components (generated from `cfg_column`, so it cannot drift).
- **USER-GUIDE:** a chapter "The surface cycle" with the picture of section 2, the state dictionary, the navigation map (the foreign-key paths), and **recipes**: from a surface to its collection; from a collection to its evidence; why is this word set aside; what is still unmatched; what changed and who changed it; what was judged with which prompt and model.
- **GOVERNANCE.md:** the mechanism only, pointing to the rule keys; **BUILD.md:** one entry per stage, including what was tried and rejected; **ps tools worksheet:** one tab per tool.

## 8. Back-trackable

Every value traces to its origin without a file: a surface's group or base → the live evidence (`surface_derivation`, `surface_judgement`) → the prompt key and hash, the model and role → the run and its settings snapshot → for loaded rows the source file and line in `analytic_file`. A revision supersedes and is an event (who, when, before, after, why). The `show` step has an `-Explain` switch that prints this chain for a surface, a base, a collection or a link.

## 9. The load, the tests and the reconciliation

1. Stage 0 sweep (G9) and the file migration into `_analytics/surface_cycle/`, registered.
2. Named snapshot of the database (`dbsnapshot.py --named`); work on a copy (`copy_db`).
3. One migration builds the tables, registers config, tools and rules through `apply_logged()`, and loads from the migrated files once.
4. **Reproduction:** the structure module against G1 exactly; the repoint against G2; the resolve against G3 for all 3,850 surfaces.
5. **Reconciliation:** 6,069 surfaces by group; 2,481 bases by source; 676 answered and 31 failed Ollama answers; 48 collections; the tally of the collection stage; 4,170 judgements; every loaded row has a `load_ref`.
6. **Independence:** on the copy, with `outputs/concept-mapping/` and `_analytics/surface_cycle/` (except `import/`) moved away, every module's `status`, `show`, `export` and re-run step works from the tables.
7. `Config-Maintenance.ps1 -Step Validate` passes with no new coherence error; the existing tests of the group and base tools (the base tool's 38 cases and the judge tests) are updated and pass. Then the same migration on the live database.

## 10. Build order

0. Stage 0 sweep and the file migration. 1. Tables, config, loader, reconciliation. 2. Structure module (G1) and repoint (G2). 3. Group, base-AI and resolve modules writing the tables (G3, G4). 4. Cycle runner and the evaluation step (G6). 5. Collection module (G5). 6. Notes, generated map, guide, BUILD, worksheet. Each stage is tested on a copy and its result recorded on #2361.

## 11. For the researcher to decide (defaults in brackets)

1. **The fourteen tables** and the state vocabularies in section 6 [accept].
2. **Rebuild G1 to G5 from their recorded outputs,** each accepted only on its reproduction check; G7 and G8 kept as registered history, G9 settled by the sweep [accept].
3. **Where the inspection workbooks go:** `_analytics/surface_cycle/exports/`, while plans and designs for you stay in `outputs/escalation/` (B:60) [accept].
4. **The AI design of section 5:** base-AI on every word, AI check of every structure hit, the reviewer on the borderline only, `quick` for cheap checks [accept]; and whether the human-test labels (G8), if they are your own, become gold cases [yes, after I read them].
5. **The working-file and method rules** of sections 4 and 7 [accept the wording, to be refined].
6. **History loaded:** the counting group run (v3) with the 56 corrections, the Ollama answers, the five collection runs that count; earlier runs stay registered as history files [accept].
7. **The empty-string surface** loaded as a flagged row and raised as its own item [yes].
8. **Go ahead** in the order of section 10, a copy test at each stage, live load once everything reconciles [yes].
