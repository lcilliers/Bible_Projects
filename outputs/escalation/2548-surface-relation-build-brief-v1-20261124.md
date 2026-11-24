# Surface relations: build brief for #2548 (v1, 2026-11-24)

For the Claude session the researcher opens in developer mode. Everything the researcher decided is in section 1; the rest is what to build and where to look. Nothing here has been built: the review and this brief only.

## 1. The researcher's decisions (2026-11-24, in chat)

- Capture the WordNet surface study of 2026-11-23 in `iba.db` so it lives and is used in analysis ("agree with the suggested build").
- Validate WordNet `same_base` pairs against `surface_term.base_id`: yes.
- Surfaces outside the study (group `other`, and the 56 with no group yet): include them.
- The code: register it (a controlled step with a run record), not a `temp_` script.
- Programme prose: add a holistic description of how surface understanding and the surface tables work together and how this is used in the study to articulate and explore the inner-being meaning of the verses (section 6).
- Standing views of the researcher on the result (#2545 v4): the 85 small WordNet groups (group 1 left out) are the clear concepts; the 154 surfaces with no pair are dealt with by hand; collections are not the basis for a study of behaviours. Neither the collections nor the WordNet groups alone give a basis for narrative or a holistic picture (message of 2026-11-24). Record these as the researcher's views, never as findings.

## 2. What the study already holds (reviewed 2026-11-24)

| Table | Live rows | Role |
|---|---|---|
| `surface_term` | 6,241 | Hub, one row per distinct surface text (lower-case, trimmed; same key as `verse_lexical.surface`). Carries `surface_group`, `group_state`, `base_id`, `base_source`, `base_state`, `collection_state`. A base is itself a row. |
| `surface_derivation` | 4,769 | Append-only evidence for each base (method structure, sibling, ollama, own; kind inflection, derivation, lead_opposite, lead_other, lead_starts_with, own; `accepted`). |
| `collection`, `collection_link` | 278, 11,722 | Collections and placement of bases by tier (core, synonym, opposite, possible_opposite, associated, set_aside). Links are on the base; a surface with no own link reads through `surface_term.base_id`. |
| `collection_listing`, `collection_subgroup`, `collection_subgroup_surface`, `surface_subgroup` | | Listed candidates, subgroups, the (Strong's code, surface) pairing. |
| `surface_flag`, `surface_event`, `surface_eval_case` | 509, 10,467, 252 | Open questions for the researcher, every change with before and after, test cases. |
| `strong_related` | 88,467 | Relations between Strong's codes (from STEP). The only relation table, at original-language level. |

No table relates one English surface to another. The 2,742 surfaces of the WordNet study all match a live `surface_term` row by text (checked: 2,742 of 2,742; all `form = word`; groups at 2026-11-24: inner_being_state 1,463, behaviour 856, other 367, none 56). The other 1,700 word surfaces are `entity` (521) or `other` and out of scope (1,179); they are not in the study's network. **To settle first in the build:** the exact scope rule for the 2,742 (the export `_analytics/surfaces/exports/behaviour-and-inner-state-surfaces-v3-20261109.csv`, single words, is the snapshot; the group of a surface has changed since: 367 are now `other`, 65 of them `out_of_scope`). Decide the rule from the data and hold it as a `cfg_setting`, do not hard-code a list.

## 3. What to build

Follow the pattern of the #2361 schema migration (`iba/app/migration/archive/surface_cycle_schema_2361_v1_20261106.py`, design `outputs/escalation/2361-surface-cycle-registration-design-v3-20261106.md`): columns registered in `cfg_column`, enums in `cfg_enum`, a `cfg_table` and `cfg_table_purpose` row for each table, the tail columns (`run_id`, `created_at`, `updated_at`, `created_by`, `deleted`, `load_ref`), soft delete only, every `cfg_*` write through `configmaint.apply_logged()`, a named rollback snapshot, one transaction, idempotent, dry-run.

1. **`surface_relation`**, one row per unordered pair (`term_a_id` < `term_b_id`, both `surface_term.id`), about 11,725 rows. Columns: `pair_type` (enum: synonym, antonym, derivational, similar, same_base, both), `weight`, `synsets_shared`, `antonym_links`, `derivational_links`, `similar_links`, `source` and `source_version` (WordNet 3.0), tail. Unique on the live pair per source. The pair type priority and weight rule are in `iba/app/tools/temp_2545_wordnet_surface_pairs.py` (same_base > synonym/both > derivational > similar > antonym; distance length = 1/weight). Pair counts of the run of 2026-11-23: synonym 7,993, same_base 1,765, derivational 706, similar 666, antonym 594, both 1.
2. **`surface_network_group`**, one row per surface per run: `term_id`, `group_no`, `group_size`, `kind` (main, small, no_pair), `in_wordnet`, `status` (indicative, confirmed), tail. Connected components of `surface_relation`. Group 1 (2,321 surfaces) is `main`; 85 groups of 2 to 15 are `small`; 154 are `no_pair`. The run is kept so a changed rule or WordNet version does not overwrite the earlier grouping. `status` carries the researcher's recognition of the 85 as clear concepts only when the researcher confirms it.
3. **No-pair review as `surface_flag`**: add flag kind `wordnet_no_pair` (and enum values for the manual-intervention class, or hold the class in the note: decide against the enum pattern of `surface_flag.kind`), `subject_kind = surface_term`. Source: `_analytics/surfaces/exports/wordnet-no-pair-review-v2-20261123.xlsx` (classes: reallocate 33, decision 28, Strong's root 62, no relation 15, study base 7, not in WordNet 7, sense conflict 2; `who_acts`). Use `escalation_id` #2545 until the researcher gives the flags their own item.
4. **Not stored, derived on demand** (record in the table purposes): the hops and weighted distance matrices (7.5 million cells, maximum 17 hops, regenerable from `surface_relation`; register the two CSVs in `file_manifest` as `regenerable`), the collection overlay (a join of `surface_relation` and `collection_link`; offer a view), Strong's root partners (from `strong_related` and the surface-Strong's pairing).
5. **Validation (decided yes):** compare WordNet `same_base` and the groups with `surface_term.base_id`, report where they disagree, write nothing to `base_id`. A disagreement is a case to read (WordNet is an outside source and modern English), not a correction. Earlier run: 711 of 764 study base groups fall inside one WordNet group.
6. **The code, registered**: a step set in the pattern of `Surface-Base.ps1`, `handlers/surfacebase.py`, `lib/surfacebase.py` (registered utility, run record, config settings for scope, WordNet folder `surfaces.wordnet_data_dir` = `data/imports/wordnet`, relation types and weights). Steps: load WordNet pairs into `surface_relation`, compute and store the network groups, flag the no-pair surfaces, validate against bases, a status report. Read the surface list from `surface_term`, not from the CSV. The workbook `_analytics/surfaces/exports/wordnet-surface-pairs-v3-20261123.xlsx` (sheets surface_pairs, pairs, groups, not_in_wordnet) is the reference to check the first load against; the step must recompute from WordNet so it can run again. The temp scripts to promote and then retire per `governance.scripts_and_routines`: `temp_2545_wordnet_surface_pairs.py`, `temp_2545_nopair_review.py`, `temp_2545_wordnet_overlay.py`.

## 4. Known data points to carry or settle

- The overlay allocation read from the `collections-v3` CSV missed 24 surfaces the database allocates through their base; the registered step reads `collection_link` live (own link, else base).
- Possessive and hyphenated-compound surfaces are not looked up in WordNet (11 surfaces); a lookup fix was offered, not asked.
- WordNet broader-narrower links are not used; offered, not asked.
- `wordnet-surface-pairs-v1-20261123.xlsx` is still unarchived (Excel held it).
- Uncommitted at the time of this brief: BUILD entry 559, the regenerated overlay workbook, script and diagrams, four CONFIG-REPORT files.

## 5. Rules to meet in the build

Developer mode is exempt from the `configmaint.propose` approval gate. Read `cfg_behaviour_rule` for schema changes, new utilities, B:59 filing, B:128 (analytic outputs under `_analytics/surfaces/exports/`), `governance.build_md_on_code_change`, B:105. Working mode of #2544: the researcher validates; report what was built, with counts checked against the 2026-11-23 figures, and stop.

## 6. Programme prose (the researcher's additional note)

A holistic description is to be written into the programme prose of `bible_research.db` (the canonical authority, `governance.prose_canonical_authority`): how surface understanding and the surface tables work together and how they are used in the study to articulate and explore the inner-being meaning of the verses. A draft, for the researcher's reading, is in `outputs/escalation/2548-surface-understanding-prose-draft-v1-20261124.md`. Where it goes: a new section in the Programme book, chapter 4 'Data architecture' (beside section 23 'Surfaces, collections and the registry' and section 25), with a pointer added in chapter 2 section 9 'Word selection: surfaces and collections', and section 23 amended to name the new tables. Use `Prose.ps1 -Step ImportChapter` to a patch, then `-Step ApplyPatch -DryRun`, then apply. The prose is the researcher's study voice: the draft is Claude's, status draft until the researcher reads it. Check glossary terms and the register check before applying. The glossary is Claude's job (B:126).
