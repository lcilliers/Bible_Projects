# Database Functional Pools Companion — 2026-07-14

## Companion Report
- Relatedness/staleness assessment: [outputs/markdown/wa-programme-database-functional-pool-relatedness-assessment-20260714.md](outputs/markdown/wa-programme-database-functional-pool-relatedness-assessment-20260714.md)

## Scope
Companion to [outputs/markdown/wa-programme-database-overview-20260714.md](outputs/markdown/wa-programme-database-overview-20260714.md), grouping all tables into related functional pools with consolidated counts and size estimates.

## Basis and Method
- Database: c:\Bible_study_projects\database\bible_research.db
- Schema version: 3.40.0
- Tables grouped: 107
- Views: 2
- Table data_size_mb is estimated payload size from SUM(LENGTH(CAST(column AS BLOB))) and excludes index/B-tree overhead.

## Pool Summary (sorted by estimated data size)

| Pool | Tables | Total rows | Estimated data size (MB) |
|---|---:|---:|---:|
| P3 Verse Lexical Indexes | 14 | 2620099 | 194.436 |
| P1 Finding Model | 7 | 845383 | 104.842 |
| P5 WA Term Verse Foundation | 6 | 599534 | 93.048 |
| P4 Verse Core and Morphology | 14 | 508563 | 67.189 |
| P9 Prose Store | 11 | 6780 | 45.763 |
| P7 Meaning and Lexicon | 7 | 39359 | 4.590 |
| P12 Registry and IB | 10 | 8811 | 4.368 |
| P8 Observation Catalogue and Registries | 13 | 6882 | 3.580 |
| P10 Quality Flags and Research | 4 | 22301 | 2.576 |
| P11 Engine Control and Run State | 4 | 5739 | 1.250 |
| P6 MTI and Term Junctions | 4 | 10524 | 1.031 |
| P2 Cluster Model | 4 | 647 | 0.311 |
| P15 Metadata | 1 | 16 | 0.120 |
| P13 Reference Static | 4 | 178 | 0.005 |
| P14 SessionD Legacy | 4 | 0 | 0.000 |

## Pool Definitions and Breakdown

### P1 Finding Model
| Table | Rows | Data size (MB) |
|---|---:|---:|
| finding | 438099 | 74.333 |
| finding_question_link | 332204 | 13.601 |
| finding_citation | 51148 | 3.077 |
| finding_verse_link | 3659 | 0.150 |
| finding_revision | 0 | 0.000 |
| cluster_finding | 19997 | 13.178 |
| cluster_observation | 276 | 0.503 |

### P2 Cluster Model
| Table | Rows | Data size (MB) |
|---|---:|---:|
| cluster | 49 | 0.053 |
| characteristic | 277 | 0.134 |
| characteristic_subgroup | 146 | 0.022 |
| cluster_subgroup | 175 | 0.101 |

### P3 Verse Lexical Indexes
| Table | Rows | Data size (MB) |
|---|---:|---:|
| ve_lexical | 599266 | 54.060 |
| ve_lexical_legacy | 507651 | 65.230 |
| ve_lexical_faculty_backup | 29031 | 2.265 |
| ve_lexical_faculty_pre_reset_20260626 | 29203 | 3.130 |
| ve_lexical_valence_quarantine_20260626 | 26993 | 2.382 |
| ve_lexical_origin_quarantine_20260626 | 3623 | 0.424 |
| ve_lexical_overlay_reverse_20260626 | 1387 | 0.133 |
| ve_lexical_divinv_pre_reverse_20260626 | 860 | 0.092 |
| ve_lexical_divinv_roles_premap_20260626 | 5187 | 0.575 |
| ve_lexical_objtype_premap_20260626 | 9534 | 0.926 |
| ve_lexical_faculty_seat_reverse_20260626 | 1492 | 0.192 |
| verse_evidence_index | 804805 | 28.482 |
| verse_span_index | 325474 | 34.048 |
| verse_term_index | 275593 | 2.495 |

### P4 Verse Core and Morphology
| Table | Rows | Data size (MB) |
|---|---:|---:|
| verse | 25634 | 5.333 |
| passage | 4296 | 0.250 |
| segment_unit | 877 | 0.332 |
| segment_unit_verse | 11276 | 0.187 |
| verse_context | 55775 | 6.719 |
| verse_context_group | 4155 | 1.136 |
| vcg_term | 5091 | 0.431 |
| verse_coverage | 23593 | 2.935 |
| verse_coverage_morphology | 2877 | 0.160 |
| verse_morph_complexity | 23593 | 0.898 |
| verse_morphology | 325507 | 22.936 |
| verse_morphology_raw | 25634 | 25.859 |
| verse_analysis_progress | 33 | 0.004 |
| verse_evidence_orphan | 222 | 0.008 |

### P5 WA Term Verse Foundation
| Table | Rows | Data size (MB) |
|---|---:|---:|
| wa_file_index | 308 | 0.056 |
| wa_term_inventory | 7844 | 4.207 |
| wa_term_related_words | 103944 | 3.150 |
| wa_term_root_family | 2861 | 0.187 |
| wa_verse_records | 247046 | 72.940 |
| wa_verse_term_links | 237531 | 12.508 |

### P6 MTI and Term Junctions
| Table | Rows | Data size (MB) |
|---|---:|---:|
| mti_terms | 7861 | 0.868 |
| mti_term_flags | 1005 | 0.004 |
| mti_term_cross_refs | 462 | 0.008 |
| mti_term_subgroup | 1196 | 0.151 |

### P7 Meaning and Lexicon
| Table | Rows | Data size (MB) |
|---|---:|---:|
| wa_meaning_parsed | 7748 | 0.389 |
| wa_meaning_sense | 17125 | 1.603 |
| wa_meaning_stem | 13 | 0.001 |
| wa_lsj_parsed | 9 | 0.007 |
| lexicon | 11666 | 2.297 |
| term_collection_lexical | 1081 | 0.113 |
| lemma_faculty_map | 1717 | 0.180 |

### P8 Observation Catalogue and Registries
| Table | Rows | Data size (MB) |
|---|---:|---:|
| wa_obs_question_catalogue | 424 | 0.146 |
| wa_finding_catalogue_links | 6199 | 3.317 |
| wa_flag_type_question_link | 12 | 0.001 |
| wa_rule_registry | 59 | 0.066 |
| wa_addendum_registry | 22 | 0.024 |
| wa_vocab_set | 8 | 0.003 |
| wa_vocab_member | 39 | 0.004 |
| wa_patch_type_registry | 20 | 0.005 |
| wa_file_name_pattern | 23 | 0.004 |
| wa_label_pattern | 11 | 0.002 |
| wa_quality_flag_types | 29 | 0.006 |
| phase2_flag_types | 25 | 0.003 |
| wa_crosslink_type | 11 | 0.001 |

### P9 Prose Store
| Table | Rows | Data size (MB) |
|---|---:|---:|
| prose_section_type | 108 | 0.029 |
| prose_section | 1039 | 14.274 |
| prose_section_fts | 1039 | 13.692 |
| prose_section_fts_data | 1059 | 4.029 |
| prose_section_fts_idx | 894 | 0.008 |
| prose_section_fts_content | 1039 | 13.695 |
| prose_section_fts_docsize | 1039 | 0.011 |
| prose_section_fts_config | 1 | 0.000 |
| prose_section_dimension_link | 0 | 0.000 |
| prose_section_finding_link | 0 | 0.000 |
| wa_prose_section_citations | 562 | 0.026 |

### P10 Quality Flags and Research
| Table | Rows | Data size (MB) |
|---|---:|---:|
| wa_data_quality_flags | 19866 | 2.060 |
| wa_session_research_flags | 715 | 0.468 |
| wa_term_phase2_flags | 1570 | 0.042 |
| reread_worklist | 150 | 0.006 |

### P11 Engine Control and Run State
| Table | Rows | Data size (MB) |
|---|---:|---:|
| engine_run_log | 875 | 0.279 |
| engine_stream_checkpoint | 1948 | 0.189 |
| word_run_state | 539 | 0.599 |
| term_fetch_log | 2377 | 0.182 |

### P12 Registry and IB
| Table | Rows | Data size (MB) |
|---|---:|---:|
| word_registry | 222 | 0.417 |
| wa_cross_registry_links | 158 | 0.025 |
| wa_dimension_index | 3509 | 0.432 |
| wa_dim_review_cluster_log | 6 | 0.003 |
| wa_session_b_dimensions | 2 | 0.003 |
| wa_session_b_findings | 2883 | 2.724 |
| wa_finding_entity_links | 287 | 0.010 |
| ib_characteristic | 1634 | 0.700 |
| ib_characteristic_legacy | 29 | 0.025 |
| ib_observation | 81 | 0.028 |

### P13 Reference Static
| Table | Rows | Data size (MB) |
|---|---:|---:|
| books | 66 | 0.004 |
| book_code_variants | 112 | 0.001 |
| themes | 0 | 0.000 |
| sources | 0 | 0.000 |

### P14 SessionD Legacy
| Table | Rows | Data size (MB) |
|---|---:|---:|
| session_d_runs | 0 | 0.000 |
| session_d_observations | 0 | 0.000 |
| session_d_term_links | 0 | 0.000 |
| session_d_verse_links | 0 | 0.000 |

### P15 Metadata
| Table | Rows | Data size (MB) |
|---|---:|---:|
| schema_version | 16 | 0.120 |

## Coverage Check
All current user tables are assigned to a functional pool.

## Views
- v_l2_meaning
- v_l2_tier
