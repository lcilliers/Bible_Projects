# The surface cycle in the database: tables, modules and load, design for approval (#2361)

> Developer Mode session 325129d4, 2026-11-06. Nothing in this design is built. It answers the researcher's instructions of 2026-11-06 (recorded verbatim on #2361): capture the process in the framework of the study (configs, governance, documentation); put the results in the database; make every part revisable, with each refinement recorded in tables that can be queried from several directions; keep the helper lists as tables; and, in the second instruction, **include the whole cycle back to the surface groupings (#2354, #2359), as modules that can each be repeated in their own right, so that the files stay as working files and are no dependency for analysis or reprocessing**. New tables and a new mechanism are a design, so it comes to the researcher first (B:105, B:44). It replaces the first design of the same day, which covered the collections stage only (archived).

## 1. The cycle as it was done, and what holds it today

| Stage | What was done | Held today in |
|---|---|---|
| 0. Surfaces | the 6,069 distinct English surfaces of the concept pairs | `surface_subgroup` (per code and surface; its `surface_group` is empty in every row); the empty string `''` is a 6,070th distinct surface that nothing judged |
| 1. Group (#2354) | one call per surface to the Ollama server: behaviour 1,317, inner being state 2,533, being 716, other 1,503; then 56 base-word repoints in a corrected copy (v4) | `first-split-v1` to `v4` jsonl, the repoint workbook, a registered tool (`Surface-Judge.ps1`) that writes **files only** |
| 2. Structure (#2359) | 79 word-structure construct rules (strip, add, undouble, prefix) applied to the 3,850 behaviour and state surfaces: 1,386 hits, statuses, leads (opposite, other, starts-with), 89 sibling surfaces (and 9 more bases that have siblings) in 47 sibling groups, 26 bases found outside the list | `surface-match-control-v1` to `v3` json. **The scripts that made them were never kept in the project**; only their outputs exist |
| 3. Base by Ollama (#2359) | the base form of the 707 words the structure left unmatched: 676 answered, 31 failed | `base-form-v1-20261104.jsonl`; registered tool `Surface-Base.ps1` (files only) |
| 4. Combined base (#2359) | per surface: structure base, else the Ollama base, else its own: 2,481 bases (structure 1,246, Ollama 387, own 2,217 surfaces) | `2359-surfaces-and-bases-v1` workbook |
| 5. Collections (#2360) | seeds, shortlists, five judges, poles, listed words, tiers: 48 collections | `collections/*` json and jsonl, embeddings `.npy`, the prompts in scratch scripts |

None of it can be queried, inspected from another direction, re-run on its own or governed by the app today.

## 2. The principle

- **The database is master. A file is a working copy or a log.** Every module reads its input from tables and settings and never from a file; the load is the last time a file is read as input. This is tested (section 7): the modules must run with the working-files folder moved away.
- **Each stage is a module of its own**: a work package that reads the tables the stage before it wrote, writes its own, records a run, and can be repeated alone (for example the combined base re-resolved after a construct is amended, or one collection re-judged under a new prompt) without repeating the others.
- **Nothing is overwritten.** A decision is a row with its source, run and model; a revision is a new row that supersedes the old one, plus an event with who and why. The current value of a surface's group or base is **resolved from the live decisions by a rule in settings**, so it can be re-derived and inspected.
- **Everything the model decided stays inferential (B:4)** until the researcher confirms it.

## 3. The tables (twelve)

All `data` tables except the rule table, built from their `cfg_column` rows, with `run_id`, `created_at`, `updated_at`, `created_by`, `deleted` as `concept_domain` has. Names and columns are for your approval.

| Table | One row per | Key columns |
|---|---|---|
| `surface_term` | distinct English surface (6,069, plus the flagged empty one) | `surface` (unique), `form` (word or phrase), `surface_group` (behaviour, inner_being_state, being, other: the current group), `group_source`, `base_id`, `base_source` (structure, sibling, ollama, own, researcher), `scope` (a = behaviour and state, b = being, c = other) |
| `surface_base` | base (2,481) | `base` (unique), `is_phrase` |
| `surface_run` | run of any module | `module` (group, structure, ollama_base, base_resolve, collection), `label`, `kind` (run, rerun, load, edit), `settings_snapshot` (prompt keys and thresholds in force), `started_at`, `finished_at`, `log_path`, `counts` |
| `surface_judgement` | every judge call (append-only, shared by the modules) | `module`, `step`, `surface_id`, `base_id`, `collection_id`, `prompt_key`, `model`, `result` (group, relation or tier), `score`, `via`, `answer`, `secs`, `run_id` |
| `surface_derivation` | piece of evidence for a surface's base (append-only) | `surface_id`, `method` (structure, sibling, ollama, own, researcher), `evidence` (a construct id, a sibling group, a judgement id), `kind` (inflection, derivation, lead_opposite, lead_other, lead_starts_with), `base_word`, `accepted`, `status` (live, superseded) |
| `cfg_base_construct` | construct rule (79) | `id`, `kind`, `direction` (same, candidate), `strip`, `add`, `undouble`, `strip_prefix`, `description`, `example`, `active` (a **rule table in config**, like `cfg_candidate_rule`) |
| `surface_flag` | exception to settle later (as recorded on #2359 and #2360: the flagged opposites, meaning-shifted derivations, held M1 pairs, the 31 failed words; and the possessive bases, the empty surface) | `subject_kind`, `subject_id`, `kind`, `note`, `status` (open, settled), `escalation_id` |
| `collection` | collection (48) | `core_base_id`, `name`, `status` (indicative, confirmed, merged, retired), `merged_into_id`, `concept_id` (NULL until the later rollup into concepts), `pole_word` |
| `collection_link` | (collection, base, tier) | `tier` (core, synonym, opposite, possible_opposite, associated, set_aside), `status` (live, superseded, removed), `superseded_by_id`, `shared`, `judgement_id` |
| `collection_pole` | named opposite pole of a collection | `pole_word`, `pole_of_pole`, `reciprocal`, `real_word` |
| `collection_listing` | word the model listed for a collection | `word`, `kind` (synonym, opposite), `base_id`, `outcome` |
| `surface_event` | each revision by the researcher or a tool (append-only) | `subject_kind` (surface, base, collection, link), `subject_id`, `action`, `field`, `before`, `after`, `by`, `reason`, `run_id` |

Possible opposites, associated words and set-aside words are tiers of `collection_link`. A partial unique index allows one live link per (collection, base). A base live in two collections is allowed (ruling of 2026-11-05) and is flagged `shared`.

**Queried from different directions** by the read steps: by surface (group, base, evidence, collection, every judgement and event behind it), by base (its surfaces), by collection (members, tiers, poles, listed words), by run, by model or prompt, by tier or flag, and the untouched.

## 4. The modules (work packages)

| Module | Reads | Writes | Repeat on its own |
|---|---|---|---|
| **surface-group** (extended from `Surface-Judge.ps1`) | `surface_term` surfaces, `surface_judge.*` settings | judgements, `surface_term.surface_group`, events for corrections (the 56 repoints) | judge the unjudged or a chosen set again; apply a researcher correction |
| **surface-structure** (new; rebuilt from the output) | surfaces of scope a, `cfg_base_construct` | derivations (hits and leads), sibling evidence, flags | re-match after a construct is amended |
| **surface-base** (extended from `Surface-Base.ps1`) | the surfaces still unmatched | judgements and derivations (method ollama) | re-ask a word or a set |
| **base-resolve** (new) | derivations, the resolve order in settings | `surface_base`, `surface_term.base_id` and `base_source`, events | re-resolve after any evidence or rule changes |
| **collection-build** | bases, collections, the `collection.*` settings | judgements, collections, links, poles, listings | seed, re-run one collection, set a base, merge, export (steps: status, show, seed, rerun, set, merge, export) |

Each has its own PowerShell entry point, steps, `cfg_work_package`, `cfg_step`, `cfg_utility` and `cfg_write_grant` rows (rule 62), a `status` and a `show` step. Long runs start outside the session (B:125). The server, tunnel and halting stay in `ollama.*` and `surface_judge.*` (B:124).

## 5. Configuration, rules and documents

- **Settings:** the prompts now in scratch scripts become `cfg_setting` rows (module `collection`: the seven collection prompts and thresholds; the group and base prompts already are rows in `surface_judge.*`). New rows: the base resolve order (structure, sibling, ollama, own), the group resolve order (researcher, correction, judge), the real-word source.
- **Enums** for every status, tier, step, kind and action value above.
- **Behaviour rules** (new rows, linked to the tools in `cfg_rule_scope`; wording for your approval; the existing rulings are not restated):
  1. The group and the base of a surface are judged on the surface text, never the Strong's code or the cluster (ruling of 2026-11-02 and 2026-11-04; the cluster is a later cross-check).
  2. A base is accepted only when it shares the root meaning of the surface; opposites, look-alikes and meaning-shifted words are leads, not bases.
  3. A candidate is judged against a collection's core word only, never its growing membership.
  4. An opposite joins only when the wording judge and the named-pole judge agree and the pole is a real word whose own opposite returns to the core word.
  5. A word that does not bind is set aside, not forced and not counted untouched.
  6. Every decision is a row with its source, run and model; a revision supersedes and is an event; nothing is overwritten.
  7. The database is master: no module reads a working file as input.
- **Documents:** `GOVERNANCE.md` (a section on the surface cycle: mechanism and pointers, no rule text), `USER-GUIDE.md` (one section per module tool), `BUILD.md` (entries, including the record of what was tried and rejected: embedding models, judge wordings, the score and reasoning tests), and `CHARTER.md` unchanged.

## 6. The load, and why it can be checked

One migration, `iba/app/migration/surface_cycle_2361_v1_20261106.py`, after a named snapshot (`dbsnapshot.py --named`) and a test on a copy made with `dbsnapshot.copy_db`. It builds the tables, registers config and tools through `apply_logged()`, and loads from the files once.

- **Deterministic stage, rebuilt:** the structure module is written as code and **must reproduce the file's results exactly**: 1,386 hits, the status counts of both versions (for example 681 unmatched single words, 89 siblings), 47 sibling groups and the 26 outside-list bases. This also proves the rebuild is the same method.
- **Recorded stages, loaded:** the group judgements (6,069 and 56 corrections), the Ollama base answers (676 and 31 failed), the collections stage (48 collections; 4,170 judgements; 48 poles; 48 listings; tiers).
- **Reconciliation from the tables:** 6,069 surfaces by group; 2,481 bases by source; the combined base per surface equal to the workbook for all 3,850; the collection tally equal to `2360-collections-tally.md` (placed 255, set aside 77, listed only 238, untouched 733, shared 23).
- **Independence test:** on the copy, with `outputs/concept-mapping/` moved away, every module's `status`, `show`, `export` and re-run step works.
- `Config-Maintenance.ps1 -Step Validate` passes with no new coherence error. Only then the same migration on the live database.

## 7. Build order

1. Schema, config and loader, with the reconciliation (the data in the database and queryable).
2. The structure module, tested against the file.
3. The group and base modules changed to write the tables, and base-resolve.
4. The collection module from the tested prototypes.
5. Documents, then a BUILD entry for each stage, and the session close.
Each stage is tested on a copy before the next; the result of each is recorded on #2361.

## 8. Not in this build

The rollup of collections into concepts and the replacement of `concept_subgroup` (ruling D1; `collection.concept_id` is the hook); collections for the phrases and for the being and other surfaces (phrases last, ruling D2; scope b and c are loaded and untouched, and their error rate is yours to assess); the embedding vectors, which stay a regenerable cache the tool rebuilds when absent and never an input.

## 9. For the researcher to decide (defaults in brackets)

1. **The twelve tables** as in section 3, with one shared judgement log and one shared event log [accept].
2. **The existing group and base tools** are changed to write the tables, their batch files becoming working copies; step names stay, their 38 tests are updated [accept].
3. **The structure module is rebuilt** from the 79 constructs, accepted only if it reproduces the file's 1,386 hits and all status counts exactly [accept].
4. **History loaded:** the group judge run that counts (v3, 6,069) and the 56 corrections as events; the earlier first-split runs (v1, v2) and the two discarded collection wordings (tags v2, v3: 1,335 judgements) stay as files [accept].
5. **The seven rules** as drafted [accept the wording, to be refined].
6. **The empty-string surface** loaded as a flagged row and raised as its own item [yes].
7. **Go ahead** with the build in the order of section 7, a copy test at each stage, and the live load once everything reconciles [yes].
