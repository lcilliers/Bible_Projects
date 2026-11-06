# Collections: registering the method, the tables and the load, design for approval (#2361)

> Developer Mode session 325129d4, 2026-11-06. Nothing in this design is built. It answers the researcher's instruction of 2026-11-06 (recorded verbatim on #2361): (a) capture the collection process in the framework of the study (configs, governance, documentation); (b) flush the results into the database; (c) make the work revisable from any point, with each refinement recorded in tables that can be queried from several directions; (d) keep the helper lists (poles, possible opposites, associated words and so on) as tables. A new mechanism and new tables are a design, so it comes to the researcher first (B:105, B:44). Parent: #2360.

## 1. What exists today, and what is wrong with it

- The surface work lives in **files** under `outputs/concept-mapping/`: the first split (`surface-group/first-split-v4-20261104.jsonl`), the bases (`outputs/escalation/2359-surfaces-and-bases-v1-20261104.xlsx`) and the collection runs (`collections/*.json`, `*.jsonl`, `*.npy`). The prompts and thresholds are in scratch scripts outside the project. The app cannot query, inspect or govern any of it.
- The database has no surface-level table. `surface_subgroup` is per (Strong's code, surface) pair and its `surface_group` column is empty in every row. `surface_pair_verdict` is the per-pair home of the group and has 0 rows. The first split judged the **surface text only**, never the code (ruling of 2026-11-02), so it needs a surface-level home.
- **Finding for the register:** `surface_subgroup` holds 6,070 distinct surfaces; the first split judged 6,069. The extra one is the empty string `''`, a defect in `surface_subgroup`. The load reports it and does not hide it.

## 2. What goes into the database (counted from the files)

| Content | Count | Source |
|---|---|---|
| Surfaces, each with its group | 6,069 (behaviour 1,317; inner being state 2,533; being 716; other 1,503) | `first-split-v4-20261104.jsonl` |
| Bases (of the 3,850 behaviour and state surfaces), 1,303 single words and 1,178 phrases | 2,481 | surfaces-and-bases workbook, combined base |
| Collections (seeds) | 48 | `collections-v4` to `v8-20261105.json`, latest run per seed |
| Collection links by tier | core and members 279 rows (255 distinct bases, 23 of them in two or more collections); possible opposites 161; associated 448; set aside 77 | same, plus `assoc-*`, `judge-*`, `lists-*` (counted in `outputs/escalation/2360-collections-status-v1-20261105.xlsx`) |
| Poles and model-listed words | 48 poles; 48 lists | `poles-*`, `lists-*` |
| Judgements (every call of the five runs that count) | 4,170 | `judge-v4` to `v8` |
| Runs | 5 (Batch 1 to 4, Re-run 1) | the logs |

The surfaces of the groups being and other (2,219) and the 1,178 phrase bases are loaded and stay **untouched**: no base work and no collection yet (phrases are assigned last, ruling D2).

## 3. The tables

All are `data` tables, built from their `cfg_column` rows (`lib/db.table_ddl`), each with the standard `run_id`, `created_at`, `updated_at`, `created_by` and `deleted` columns, as `concept_domain` has. Names and columns are for your approval.

| Table | One row per | Key columns | What it answers |
|---|---|---|---|
| `surface_term` | distinct English surface (6,069) | `surface` (unique), `form` (word or phrase), `surface_group` (behaviour, inner_being_state, being, other), `group_reason`, `group_judged_by`, `base_id` | "what is this surface, which group, which base" |
| `surface_base` | base (2,481) | `base` (unique), `is_phrase`, `base_source` (own, structure, ollama), `base_how` (the construct or the reason) | "which surfaces share a base" |
| `collection` | collection (48) | `core_base_id`, `name`, `status` (indicative, confirmed, merged, retired), `merged_into_id`, `concept_id` (NULL until the later rollup into concepts) | "what are the collections and in what state" |
| `collection_link` | (collection, base, tier) | `tier` (core, synonym, opposite, possible_opposite, associated, set_aside), `status` (live, superseded, removed), `superseded_by_id`, `shared` (1 when the base is live in another collection), `judgement_id`, `reason` | "where is this base, what is in this collection, what is set aside" |
| `collection_judgement` | every judge call (append-only) | `collection_id`, `base_id`, `step` (synonym, score, opposite, pole_synonym, associated), `prompt_key`, `model`, `relation`, `score`, `via`, `answer`, `secs` | "why is it there, who or what decided, with which prompt" |
| `collection_pole` | collection and its named opposite pole | `pole_word`, `pole_of_pole`, `reciprocal`, `real_word`, `status` | the poles helper list |
| `collection_listing` | word the model listed for a collection | `word`, `kind` (synonym, opposite), `base_id` (NULL when not in the pool), `outcome` | the model-listed words helper list |
| `collection_run` | run | `label`, `kind` (seed, rerun, load, edit), `seeds`, `settings_snapshot` (prompt keys and thresholds in force), `started_at`, `finished_at`, `log_path` | "which run made this, with which method" |
| `collection_event` | each change by the researcher or by a tool (append-only) | `collection_id`, `base_id`, `action` (confirm, move, remove, merge, retire, reopen, set_tier), `before`, `after`, `by`, `reason` | "what was revised, by whom, and why" |

The possible opposites, the associated words and the set-aside words are **tiers of `collection_link`**, not separate tables, so a word moves between tiers (set aside, then member) by one superseding row and one event, and nothing is overwritten. A partial unique index allows one live link per (collection, base). A base live in two collections is allowed (ruling of 2026-11-05) and is flagged `shared` and counted in the tally.

**Queried from different directions** (a step, section 5): by surface (its group, base, collection, tier and the judgements behind it), by base, by collection (members, tiers, helper lists), by run, by judge or model, by tier (all the set-aside words), and the untouched surfaces.

## 4. Configuration and rules

- **Settings** (new module `collection`, added to `cfg_enum config_module`): the seven prompts (`synonym`, `opposite_wording`, `score`, `pole`, `real_word`, `list`, `associated`), `score_min` 8, `shortlist_k` 40, `pole_k` 25, `max_passes` 5, `associated_k` 40, the embedding model (`qwen3-embedding`), the folder for the embedding files. The server, tunnel and halting stay in the existing `ollama.*` and `surface_judge.*` rows (B:124).
- **Enums** for the status, tier, step, kind and action values above, and `surface_term.surface_group`.
- **Behaviour rules** (new `cfg_behaviour_rule` rows, linked to the tool and tables in `cfg_rule_scope`; wording for your approval):
  1. A candidate is judged against the collection's **core word only**, never against its growing membership, because judging against the membership drifted (fear became a distress group).
  2. An opposite joins a collection only when the wording judge and the named-pole judge agree and the pole is a real word whose own opposite returns to the core word; any other opposite is a possible opposite for the researcher.
  3. A word that does not bind is **set aside**, not forced and not counted untouched (researcher, 2026-11-05).
  4. Every judgement is inferential (B:4) and logged with its prompt key and model; a collection is indicative until the researcher confirms it; every researcher edit is an event.
  5. A base in more than one collection is the exception, flagged `shared` and counted; seeds that share members are merge candidates.
  A long run still follows B:125 (no new rule).
- **Governance and documents:** a short section in `GOVERNANCE.md` (the mechanism and pointers, no rule text), a section in `USER-GUIDE.md` for the tool, a `BUILD.md` entry, and the method record. The record of what was tried and rejected (comparison of the embedding models, the judge wordings, the score test, the reasoning test) goes into the `BUILD.md` entry and `collection_run.settings_snapshot`.

## 5. The tool

Work package `collection-build`, entry point `iba/app/ps/Collections.ps1`, library `iba/app/lib/collections.py`, handlers `iba/app/handlers/collections.py`, registered in `cfg_work_package`, `cfg_step`, `cfg_utility` and `cfg_write_grant` in the same unit of work (rule 62). The prototype scripts in the session scratchpad become this code and are not kept.

| Step | Does |
|---|---|
| `collection.status` | the tally from the tables: collections, placed, set aside, listed only, untouched, shared (read-only) |
| `collection.show` | one surface, base, collection, run, tier or model with everything behind it (read-only) |
| `collection.seed` | run new seed words: shortlist, judge, write links and judgements; resumable; started outside the session (B:125) |
| `collection.rerun` | re-judge one collection under the settings now in force; the previous links are superseded, not deleted |
| `collection.set` | the researcher's edit: confirm, move, remove or change the tier of a base; writes the link and an event |
| `collection.merge` | merge one collection into another; the merged one stays, status `merged`, with its links superseded |
| `collection.export` | the workbook for inspection |

## 6. The load, the test and the reconciliation

1. **Rollback point:** a named snapshot of the database (`iba/app/lib/dbsnapshot.py --named`, B:97).
2. **Migration** `iba/app/migration/collections_2361_v1_20261106.py`: builds the nine tables from `cfg_column`, registers the settings, enums, rules, work package, steps, grants and utilities through `apply_logged()`, and loads the content of section 2. It is idempotent, one transaction, runs once and then moves to `migration/archive/`.
3. **Test on a copy** made with `dbsnapshot.copy_db` (never the live database) in this session. The result is recorded on #2361.
4. **Reconciliation, from the tables, must equal the files:** 6,069 surfaces; 2,481 bases; 48 live collections; the tally reproduced exactly (placed 255, set aside 77, listed only 238, untouched 733, shared 23, over 1,303 single-word bases); 4,170 judgements; every `collection_link` has a judgement or a load event. `Config-Maintenance.ps1 -Step Validate` must pass with no new coherence error.
5. Only then the same migration on the live database.

## 7. Not in this build

- The merge rollup of collections into concepts and the replacement of `concept_subgroup` (ruling D1: later). `collection.concept_id` is the hook.
- Assigning the 1,178 phrase bases and the 2,219 being and other surfaces to collections (phrases last, D2; the being group is outside the first collections).
- The embedding vectors stay in files (1,303 vectors of 4,096 numbers); they are regenerated from the settings. Putting them in a table is possible and not proposed.

## 8. For the researcher to decide (defaults in brackets)

1. **The nine tables** as in section 3, with the helper lists as tiers of `collection_link` [accept]. Or a separate table for each helper list.
2. **Loading the judgements of the two discarded runs** (v2, v3: 1,335 judgements from the wording that drifted) [no; they stay as files].
3. **A base in two collections** is allowed and flagged `shared` [yes, as ruled on 2026-11-05].
4. **The five behaviour rules** in section 4 [accept the wording as drafted, to be refined].
5. **The empty-string surface** in `surface_subgroup` [load it as a flagged row `surface_term` with `form` empty and raise it as its own item for correction].
6. **Go ahead** with the build, the copy test and, once the reconciliation matches, the live load [yes].
