# Verse-related schema — CURRENT (existing) state

> Generated 2026-06-15 directly from `database/bible_research.db` (schema 3.32.0). **This is the EXISTING schema.** Anything I called `ve_lexical`, or proposed new columns on `verse_context`, is a PROPOSAL in `wa-ve-lexical-data-model-redesign-v1` and is **NOT** in here yet.

## Raw verse layer (one row per term-in-verse occurrence; the text/morph/span facts)

### `wa_verse_records`  — the term-as-used-in-a-verse: text, morph_code/stem (=mode), span_strong_match, word_registry_fk
_rows: 230,454_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| file_id | INTEGER | 1 |  | 0 |
| term_inv_id | INTEGER | 0 |  | 0 |
| term_id | TEXT | 0 |  | 0 |
| transliteration | TEXT | 0 |  | 0 |
| testament | TEXT | 0 |  | 0 |
| reference | TEXT | 0 |  | 0 |
| verse_text | TEXT | 0 |  | 0 |
| last_changed | TEXT | 0 | datetime('now') | 0 |
| book_id | INTEGER | 0 |  | 0 |
| chapter | INTEGER | 0 |  | 0 |
| verse_num | INTEGER | 0 |  | 0 |
| translation | TEXT | 1 | 'ESV' | 0 |
| note | TEXT | 0 |  | 0 |
| claude_output | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| updated_at | TEXT | 0 |  | 0 |
| target_word | TEXT | 0 |  | 0 |
| span_strong_match | INTEGER | 0 |  | 0 |
| context_before | TEXT | 0 |  | 0 |
| context_after | TEXT | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |
| mti_term_id | INTEGER | 0 | NULL | 0 |
| morph_code | TEXT | 0 |  | 0 |
| stem | TEXT | 0 |  | 0 |
| word_registry_fk | INTEGER | 0 |  | 0 |

FKs: book_id→books.id; term_inv_id→wa_term_inventory.id; file_id→wa_file_index.id

### `wa_verse_term_links`  — per-occurrence STEP subgloss (step_subgloss_label) + span match
_rows: 227,288_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| verse_id | INTEGER | 1 |  | 0 |
| term_inv_id | INTEGER | 1 |  | 0 |
| step_subgloss_code | TEXT | 0 |  | 0 |
| step_subgloss_label | TEXT | 0 |  | 0 |
| span_strong_match | INTEGER | 0 |  | 0 |
| target_word | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 | strftime('%Y-%m-%dT%H:%M:%S','now') | 0 |

FKs: term_inv_id→wa_term_inventory.id; verse_id→wa_verse_records.id

## Analytical layer (the per-term-in-verse unit the VE analysis attaches to)

### `verse_context`  — THE analytical unit: verse_record_id+mti_term_id, sense_id, step_meaning_applied, cluster refs (group_id, cluster_subgroup_id), pole, triage_status
_rows: 43,722_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| verse_record_id | INTEGER | 1 |  | 0 |
| mti_term_id | INTEGER | 1 |  | 0 |
| group_id | INTEGER | 0 |  | 0 |
| cluster_subgroup_id | INTEGER | 0 |  | 0 |
| is_anchor | INTEGER | 1 | 0 | 0 |
| is_relevant | INTEGER | 1 | 0 | 0 |
| is_related | INTEGER | 1 | 0 | 0 |
| notes | TEXT | 0 | NULL | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |
| set_aside_reason | TEXT | 0 | NULL | 0 |
| analysis_note | TEXT | 0 |  | 0 |
| keywords | TEXT | 0 |  | 0 |
| step_meaning_applied | TEXT | 0 |  | 0 |
| sense_id | INTEGER | 0 |  | 0 |
| sense_multiplicity | TEXT | 0 |  | 0 |
| step_envelope_note | TEXT | 0 |  | 0 |
| pole | TEXT | 0 |  | 0 |
| pole_is_metaphor | INTEGER | 0 | 0 | 0 |
| residue_flag | INTEGER | 0 | 0 | 0 |
| thing_type | TEXT | 0 |  | 0 |
| triage_status | TEXT | 0 |  | 0 |
| meaning_provenance | TEXT | 0 |  | 0 |
| flagged_for_review | INTEGER | 0 | 0 | 0 |

FKs: cluster_subgroup_id→cluster_subgroup.id; group_id→verse_context_group.id; mti_term_id→mti_terms.id; verse_record_id→wa_verse_records.id

### `verse_context_group`  — VCG groups of verse_context rows
_rows: 4,155_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| group_code | TEXT | 1 |  | 0 |
| context_description | TEXT | 1 |  | 0 |
| notes | TEXT | 0 | NULL | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |

## Findings (current home of the interpretive VE fields — sense/type/etc.)

### `finding`  — the universal finding store; level=VERSE rows = the per-term-in-verse field values
_rows: 343,434_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| level | TEXT | 1 |  | 0 |
| verse_context_id | INTEGER | 0 |  | 0 |
| mti_term_id | INTEGER | 0 |  | 0 |
| cluster_code | TEXT | 0 |  | 0 |
| finding_value | TEXT | 0 |  | 0 |
| finding_status | TEXT | 0 |  | 0 |
| provenance | TEXT | 0 |  | 0 |
| justified_by_finding_id | INTEGER | 0 |  | 0 |
| supersedes_id | INTEGER | 0 |  | 0 |
| source_legacy_ref | TEXT | 0 |  | 0 |
| flagged_for_review | INTEGER | 0 | 0 | 0 |
| created_at | TEXT | 0 |  | 0 |
| last_updated_date | TEXT | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |

### `finding_question_link`  — links a finding to its catalogue question (the 'key')
_rows: 332,184_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| finding_id | INTEGER | 1 |  | 0 |
| question_id | INTEGER | 1 |  | 0 |
| coverage | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |

### `finding_citation`  — citations on a finding
_rows: 51,148_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| source_table | TEXT | 1 |  | 0 |
| source_id | INTEGER | 1 |  | 0 |
| citation_type | TEXT | 1 |  | 0 |
| citation_value | TEXT | 1 |  | 0 |
| position | INTEGER | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |
| created_at | TEXT | 0 |  | 0 |

### `finding_verse_link`  — verse links on a finding
_rows: 3,586_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| finding_id | INTEGER | 1 |  | 0 |
| verse_record_id | INTEGER | 0 |  | 0 |
| reference | TEXT | 0 |  | 0 |
| role | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |

## Catalogue (the tier 'keys' the findings link to)

### `wa_obs_question_catalogue`  — the 173 tiered T0-T7 questions + extensions
_rows: 412_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| obs_id | INTEGER | 0 |  | 1 |
| question_code | TEXT | 1 |  | 0 |
| section | TEXT | 1 |  | 0 |
| source_word | TEXT | 0 |  | 0 |
| source_registry_no | INTEGER | 0 |  | 0 |
| question_text | TEXT | 1 |  | 0 |
| pattern_type | TEXT | 0 |  | 0 |
| scope | TEXT | 1 | 'universal' | 0 |
| status | TEXT | 1 | 'active' | 0 |
| deleted | INTEGER | 1 | 0 | 0 |
| date_added | TEXT | 1 |  | 0 |
| catalogue_version | TEXT | 1 |  | 0 |
| review_note | TEXT | 0 |  | 0 |
| tier | TEXT | 0 |  | 0 |
| component_code | TEXT | 0 |  | 0 |
| component_title | TEXT | 0 |  | 0 |
| prompt_seq | INTEGER | 0 |  | 0 |

FKs: source_registry_no→word_registry.id

## Terms

### `mti_terms`  — one row per Strong's; cluster_code, owning_registry_fk, gloss, language, status
_rows: 7,581_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| strongs_number | TEXT | 0 |  | 0 |
| transliteration | TEXT | 0 |  | 0 |
| gloss | TEXT | 0 |  | 0 |
| language | TEXT | 0 |  | 0 |
| owning_registry | TEXT | 0 |  | 0 |
| owning_registry_fk | INTEGER | 0 |  | 0 |
| owning_word | TEXT | 0 |  | 0 |
| owning_part | TEXT | 0 |  | 0 |
| word_data_reference | TEXT | 0 |  | 0 |
| word_data_ref_fk | INTEGER | 0 |  | 0 |
| status | TEXT | 0 |  | 0 |
| exclusion_reason | TEXT | 0 |  | 0 |
| extraction_date | TEXT | 0 |  | 0 |
| strongs_reconciled | INTEGER | 0 |  | 0 |
| anchor_note | TEXT | 0 |  | 0 |
| last_changed | TEXT | 0 |  | 0 |
| delete_flagged | INTEGER | 0 |  | 0 |
| vc_status | TEXT | 1 | 'not_done' | 0 |
| vc_instruction_version | TEXT | 0 |  | 0 |
| vc_status_updated_at | TEXT | 0 |  | 0 |
| vc_status_note | TEXT | 0 |  | 0 |
| md_version | INTEGER | 1 | 1 | 0 |
| cluster_code | TEXT | 0 |  | 0 |

FKs: owning_registry_fk→word_registry.id

### `wa_term_inventory`  — per term-in-registry; OWNER/XREF, glosses, parsed_meaning_id, word_registry_fk
_rows: 7,560_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| file_id | INTEGER | 1 |  | 0 |
| language | TEXT | 1 |  | 0 |
| term_id | TEXT | 1 |  | 0 |
| strongs_number | TEXT | 0 |  | 0 |
| transliteration | TEXT | 1 |  | 0 |
| step_search_gloss | TEXT | 0 |  | 0 |
| word_analysis_gloss | TEXT | 0 |  | 0 |
| occurrence_count | INTEGER | 0 |  | 0 |
| occurrence_count_qualifier | TEXT | 0 |  | 0 |
| meaning | TEXT | 0 |  | 0 |
| meaning_numbered | TEXT | 0 |  | 0 |
| also_spelled | TEXT | 0 |  | 0 |
| lsj_entry | TEXT | 0 |  | 0 |
| testament | TEXT | 0 |  | 0 |
| causative_form_present | INTEGER | 0 | 0 | 0 |
| last_changed | TEXT | 0 | datetime('now') | 0 |
| short_def_mounce | TEXT | 0 |  | 0 |
| parsed_meaning_id | INTEGER | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |
| evidential_status | TEXT | 0 | NULL | 0 |
| retention_note | TEXT | 0 | NULL | 0 |
| term_owner_type | TEXT | 0 | NULL | 0 |
| term_introduction_source | TEXT | 0 |  | 0 |
| term_introduction_rationale | TEXT | 0 |  | 0 |
| term_introduction_date | TEXT | 0 |  | 0 |
| word_registry_fk | INTEGER | 0 |  | 0 |

FKs: file_id→wa_file_index.id

## Senses / parsed meaning (the canonical 'all glosses' inventory)

### `wa_meaning_parsed`  — parsed meaning per term
_rows: 7,459_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| term_inv_id | INTEGER | 1 |  | 0 |
| strongs_number | TEXT | 1 |  | 0 |
| language | TEXT | 1 |  | 0 |
| top_sense_count | INTEGER | 0 | 0 | 0 |
| stem_count | INTEGER | 0 | 0 | 0 |
| has_causative_stem | INTEGER | 0 | 0 | 0 |
| has_domain_tags | INTEGER | 0 | 0 | 0 |
| parsed_at | TEXT | 1 |  | 0 |
| parse_version | TEXT | 1 |  | 0 |
| parse_warnings | TEXT | 0 |  | 0 |

FKs: term_inv_id→wa_term_inventory.id

### `wa_meaning_sense`  — the canonical sense rows (sense_text) per parsed-meaning
_rows: 16,005_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| parsed_meaning_id | INTEGER | 1 |  | 0 |
| level_code | TEXT | 1 |  | 0 |
| level_depth | INTEGER | 1 |  | 0 |
| parent_level_code | TEXT | 0 |  | 0 |
| sense_text | TEXT | 0 |  | 0 |
| is_stem_label | INTEGER | 0 | 0 | 0 |
| stem_label | TEXT | 0 |  | 0 |
| domain_tag | TEXT | 0 |  | 0 |
| sort_order | INTEGER | 1 |  | 0 |
| is_homonym | INTEGER | 0 | 0 | 0 |

FKs: parsed_meaning_id→wa_meaning_parsed.id

## Clusters

### `cluster`  — M-code clusters
_rows: 49_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| cluster_code | TEXT | 0 |  | 1 |
| description | TEXT | 0 |  | 0 |
| gloss | TEXT | 1 |  | 0 |
| source | TEXT | 0 |  | 0 |
| bucket | TEXT | 0 |  | 0 |
| status | TEXT | 0 |  | 0 |
| version | TEXT | 0 |  | 0 |
| last_updated_date | TEXT | 0 |  | 0 |
| short_name | TEXT | 0 |  | 0 |
| char_structure | TEXT | 0 |  | 0 |

### `cluster_subgroup`  — sub-groups under a cluster
_rows: 175_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| cluster_code | TEXT | 1 |  | 0 |
| subgroup_code | TEXT | 1 |  | 0 |
| label | TEXT | 1 |  | 0 |
| core_description | TEXT | 0 |  | 0 |
| sort_order | INTEGER | 0 | 0 | 0 |
| status | TEXT | 0 |  | 0 |
| version | TEXT | 0 |  | 0 |
| source | TEXT | 0 |  | 0 |
| notes | TEXT | 0 |  | 0 |
| delete_flagged | INTEGER | 0 | 0 | 0 |
| created_at | TEXT | 0 |  | 0 |
| last_updated_date | TEXT | 0 |  | 0 |

FKs: cluster_code→cluster.cluster_code

## Registry / file

### `word_registry`  — the ~215 word entries
_rows: 215_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| no | INTEGER | 0 |  | 0 |
| word | TEXT | 1 |  | 0 |
| source_list | TEXT | 0 |  | 0 |
| category_hint | TEXT | 0 |  | 0 |
| phase1_input_file | TEXT | 0 |  | 0 |
| phase1_status | TEXT | 0 |  | 0 |
| phase1_output_file | TEXT | 0 |  | 0 |
| phase2_datasets | REAL | 0 |  | 0 |
| notes | TEXT | 0 |  | 0 |
| automation_eligible | INTEGER | 0 | 1 | 0 |
| last_automation_run | TEXT | 0 |  | 0 |
| automation_run_id | TEXT | 0 |  | 0 |
| phase1_term_count | INTEGER | 0 |  | 0 |
| phase1_verse_count | INTEGER | 0 |  | 0 |
| strongs_list | TEXT | 0 |  | 0 |
| description | TEXT | 0 |  | 0 |
| origin | TEXT | 0 |  | 0 |
| dimensions | TEXT | 0 |  | 0 |
| inference_note | TEXT | 0 |  | 0 |
| session_b_status | TEXT | 0 |  | 0 |
| cluster_assignment | TEXT | 0 | "unassigned" | 0 |
| sb_classification | TEXT | 0 | NULL | 0 |
| sb_classification_reasoning | TEXT | 0 | NULL | 0 |
| carry_forward | INTEGER | 0 | 1 | 0 |
| unique_term_count | INTEGER | 0 | 0 | 0 |
| shared_term_count | INTEGER | 0 | 0 | 0 |
| term_sharing_ratio | REAL | 0 | 0.0 | 0 |
| verse_context_status | TEXT | 0 | NULL | 0 |
| dim_review_status | TEXT | 0 | NULL | 0 |
| dim_review_version | TEXT | 0 | NULL | 0 |
| word_synopsis | TEXT | 0 |  | 0 |

### `wa_file_index`  — LEGACY file index (stub only; bypass FK = word_registry_fk)
_rows: 207_

| column | type | notnull | default | pk |
|---|---|---|---|---|
| id | INTEGER | 0 |  | 1 |
| filename | TEXT | 1 |  | 0 |
| registry_id | TEXT | 1 |  | 0 |
| word_registry_fk | INTEGER | 0 |  | 0 |
| word | TEXT | 1 |  | 0 |
| part_number | INTEGER | 0 |  | 0 |
| total_parts | INTEGER | 0 |  | 0 |
| is_split | INTEGER | 0 |  | 0 |
| schema_version | TEXT | 0 |  | 0 |
| phase | TEXT | 0 |  | 0 |
| produced_date | TEXT | 0 |  | 0 |
| source_file | TEXT | 0 |  | 0 |
| translation_used | TEXT | 0 |  | 0 |
| specification | TEXT | 0 |  | 0 |
| revision_note | TEXT | 0 |  | 0 |
| source_list | TEXT | 0 |  | 0 |
| category | TEXT | 0 |  | 0 |
| testament_coverage | TEXT | 0 |  | 0 |
| root_families_in_prior_parts | TEXT | 0 |  | 0 |
| last_changed | TEXT | 0 | datetime('now') | 0 |

FKs: word_registry_fk→word_registry.id
