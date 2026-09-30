# Database Overview — 2026-07-14

## Companion Report
- Functional pools companion: [outputs/markdown/wa-programme-database-functional-pools-20260714.md](outputs/markdown/wa-programme-database-functional-pools-20260714.md)

## Scope
Read-only structural overview of the live database file at c:\Bible_study_projects\database\bible_research.db.

## Headline Metrics

| Metric | Value |
|---|---:|
| Schema version | 3.40.0 |
| Database file size (MB) | 761.875 |
| Page size (bytes) | 4096 |
| Page count | 195040 |
| Freelist pages | 0 |
| Table count | 107 |
| View count | 2 |

## Size Method
Per-table size below is data_size_mb, estimated as payload bytes from summing LENGTH(CAST(column AS BLOB)) over all rows and columns.

This estimate:
- Includes row payload content.
- Excludes SQLite B-tree/page overhead and index storage.
- Is useful for relative table footprint comparison, not exact on-disk object size.

## Top 20 Tables by Row Count

| Table | Rows | Data size (MB) |
|---|---:|---:|
| verse_evidence_index | 804805 | 28.482 |
| ve_lexical | 598969 | 54.022 |
| ve_lexical_legacy | 507651 | 65.230 |
| finding | 438099 | 74.333 |
| finding_question_link | 332204 | 13.601 |
| verse_morphology | 325507 | 22.936 |
| verse_span_index | 325474 | 34.048 |
| verse_term_index | 275593 | 2.495 |
| wa_verse_records | 247046 | 72.940 |
| wa_verse_term_links | 237531 | 12.508 |
| wa_term_related_words | 103944 | 3.150 |
| verse_context | 55775 | 6.719 |
| finding_citation | 51148 | 3.077 |
| ve_lexical_faculty_pre_reset_20260626 | 29203 | 3.130 |
| ve_lexical_faculty_backup | 29031 | 2.265 |
| ve_lexical_valence_quarantine_20260626 | 26993 | 2.382 |
| verse | 25634 | 5.333 |
| verse_morphology_raw | 25634 | 25.859 |
| verse_coverage | 23593 | 2.935 |
| verse_morph_complexity | 23593 | 0.898 |

## Top 20 Tables by Estimated Data Size

| Table | Data size (MB) | Rows |
|---|---:|---:|
| finding | 74.333 | 438099 |
| wa_verse_records | 72.940 | 247046 |
| ve_lexical_legacy | 65.230 | 507651 |
| ve_lexical | 54.022 | 598969 |
| verse_span_index | 34.048 | 325474 |
| verse_evidence_index | 28.482 | 804805 |
| verse_morphology_raw | 25.859 | 25634 |
| verse_morphology | 22.936 | 325507 |
| prose_section | 14.274 | 1039 |
| prose_section_fts_content | 13.695 | 1039 |
| prose_section_fts | 13.692 | 1039 |
| finding_question_link | 13.601 | 332204 |
| cluster_finding | 13.178 | 19997 |
| wa_verse_term_links | 12.508 | 237531 |
| verse_context | 6.719 | 55775 |
| verse | 5.333 | 25634 |
| wa_term_inventory | 4.207 | 7844 |
| prose_section_fts_data | 4.029 | 1059 |
| wa_finding_catalogue_links | 3.317 | 6199 |
| wa_term_related_words | 3.150 | 103944 |

## All Tables (Rows + Estimated Data Size)

| Table | Rows | Data size (MB) |
|---|---:|---:|
| book_code_variants | 112 | 0.001 |
| books | 66 | 0.004 |
| characteristic | 277 | 0.134 |
| characteristic_subgroup | 146 | 0.022 |
| cluster | 49 | 0.053 |
| cluster_finding | 19997 | 13.178 |
| cluster_observation | 276 | 0.503 |
| cluster_subgroup | 175 | 0.101 |
| engine_run_log | 875 | 0.279 |
| engine_stream_checkpoint | 1948 | 0.189 |
| finding | 438099 | 74.333 |
| finding_citation | 51148 | 3.077 |
| finding_question_link | 332204 | 13.601 |
| finding_revision | 0 | 0.000 |
| finding_verse_link | 3659 | 0.150 |
| ib_characteristic | 1621 | 0.691 |
| ib_characteristic_legacy | 29 | 0.025 |
| ib_observation | 81 | 0.028 |
| lemma_faculty_map | 1717 | 0.180 |
| lexicon | 11666 | 2.297 |
| mti_term_cross_refs | 462 | 0.008 |
| mti_term_flags | 1005 | 0.004 |
| mti_term_subgroup | 1196 | 0.151 |
| mti_terms | 7861 | 0.868 |
| passage | 4296 | 0.250 |
| phase2_flag_types | 25 | 0.003 |
| prose_section | 1039 | 14.274 |
| prose_section_dimension_link | 0 | 0.000 |
| prose_section_finding_link | 0 | 0.000 |
| prose_section_fts | 1039 | 13.692 |
| prose_section_fts_config | 1 | 0.000 |
| prose_section_fts_content | 1039 | 13.695 |
| prose_section_fts_data | 1059 | 4.029 |
| prose_section_fts_docsize | 1039 | 0.011 |
| prose_section_fts_idx | 894 | 0.008 |
| prose_section_type | 108 | 0.029 |
| reread_worklist | 150 | 0.006 |
| schema_version | 16 | 0.120 |
| segment_unit | 877 | 0.332 |
| segment_unit_verse | 11276 | 0.187 |
| session_d_observations | 0 | 0.000 |
| session_d_runs | 0 | 0.000 |
| session_d_term_links | 0 | 0.000 |
| session_d_verse_links | 0 | 0.000 |
| sources | 0 | 0.000 |
| term_collection_lexical | 1081 | 0.113 |
| term_fetch_log | 2377 | 0.182 |
| themes | 0 | 0.000 |
| vcg_term | 5091 | 0.431 |
| ve_lexical | 598969 | 54.022 |
| ve_lexical_divinv_pre_reverse_20260626 | 860 | 0.092 |
| ve_lexical_divinv_roles_premap_20260626 | 5187 | 0.575 |
| ve_lexical_faculty_backup | 29031 | 2.265 |
| ve_lexical_faculty_pre_reset_20260626 | 29203 | 3.130 |
| ve_lexical_faculty_seat_reverse_20260626 | 1492 | 0.192 |
| ve_lexical_legacy | 507651 | 65.230 |
| ve_lexical_objtype_premap_20260626 | 9534 | 0.926 |
| ve_lexical_origin_quarantine_20260626 | 3623 | 0.424 |
| ve_lexical_overlay_reverse_20260626 | 1387 | 0.133 |
| ve_lexical_valence_quarantine_20260626 | 26993 | 2.382 |
| verse | 25634 | 5.333 |
| verse_analysis_progress | 33 | 0.004 |
| verse_context | 55775 | 6.719 |
| verse_context_group | 4155 | 1.136 |
| verse_coverage | 23593 | 2.935 |
| verse_coverage_morphology | 2877 | 0.160 |
| verse_evidence_index | 804805 | 28.482 |
| verse_evidence_orphan | 222 | 0.008 |
| verse_morph_complexity | 23593 | 0.898 |
| verse_morphology | 325507 | 22.936 |
| verse_morphology_raw | 25634 | 25.859 |
| verse_span_index | 325474 | 34.048 |
| verse_term_index | 275593 | 2.495 |
| wa_addendum_registry | 22 | 0.024 |
| wa_cross_registry_links | 158 | 0.025 |
| wa_crosslink_type | 11 | 0.001 |
| wa_data_quality_flags | 19866 | 2.060 |
| wa_dim_review_cluster_log | 6 | 0.003 |
| wa_dimension_index | 3509 | 0.432 |
| wa_file_index | 308 | 0.056 |
| wa_file_name_pattern | 23 | 0.004 |
| wa_finding_catalogue_links | 6199 | 3.317 |
| wa_finding_entity_links | 287 | 0.010 |
| wa_flag_type_question_link | 12 | 0.001 |
| wa_label_pattern | 11 | 0.002 |
| wa_lsj_parsed | 9 | 0.007 |
| wa_meaning_parsed | 7748 | 0.389 |
| wa_meaning_sense | 17125 | 1.603 |
| wa_meaning_stem | 13 | 0.001 |
| wa_obs_question_catalogue | 424 | 0.146 |
| wa_patch_type_registry | 20 | 0.005 |
| wa_prose_section_citations | 562 | 0.026 |
| wa_quality_flag_types | 29 | 0.006 |
| wa_rule_registry | 59 | 0.066 |
| wa_session_b_dimensions | 2 | 0.003 |
| wa_session_b_findings | 2883 | 2.724 |
| wa_session_research_flags | 715 | 0.468 |
| wa_term_inventory | 7844 | 4.207 |
| wa_term_phase2_flags | 1570 | 0.042 |
| wa_term_related_words | 103944 | 3.150 |
| wa_term_root_family | 2861 | 0.187 |
| wa_verse_records | 247046 | 72.940 |
| wa_verse_term_links | 237531 | 12.508 |
| wa_vocab_member | 39 | 0.004 |
| wa_vocab_set | 8 | 0.003 |
| word_registry | 222 | 0.417 |
| word_run_state | 539 | 0.599 |

## Views

| View |
|---|
| v_l2_meaning |
| v_l2_tier |
