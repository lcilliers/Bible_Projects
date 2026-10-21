# #2184: Memory holds only what config cannot (v1, 2026-10-21)

Escalation #2184 (option E of the #2179 review; an element of the IBA app reset, #2177). The
control map gives Claude's memory one job, kind `claude_memory`: who the researcher is, and a few
data pointers. No rule and no project state. Researcher, 2026-10-21: *"There should be no instance
of the same rule in multiple documents."*

## Result

**Before:** 345 memory files, 115 of them in an index read every conversation (12 KB). Many
repeated a config rule in different words. Some contradicted each other: one memory said to wait
for approval before any non-trivial task, another said to proceed without approval steps.

**After:** 6 files:
- the researcher's profile
- 5 data pointers (ESV text table, `strong_related` keys, zero-padded Strong's, `narrative_passage`,
  the notes folder)

There is a short index. The other 339 files are in the memory folder's `archive/`, read only
deliberately.

**Where each file's content went:**

| Disposition | Files | Where the content lives now |
|---|---|---|
| Rule already in config | 77 | the `cfg_behaviour_rule` / `cfg_setting` named per file below |
| Live rule that existed only in memory | 22 | **15 new rules** (migration `iba/app/migration/memory_rules_to_config_v1_20261021.py`, run `DEVMODE-2184-MEMORY-RULES-20261021`) |
| Tool usage (how to run Escalation.ps1, Config-Maintenance, the Excel sheets, the cost-history tool) | 7 | the USER-GUIDE rewrite, #2187 |
| Study principle whose currency under the current method is not settled | 29 | archived; for the researcher when the study re-opens (§3) |
| Rule of a retired method (the cluster pipeline phases 1–9, L1/L2, VE lexical, Session B/C, Verse Context, patches, tier catalogue) | 70 | history |
| Project state or history | 122 | history; current state is in `iba.db` and the escalations |
| Stale or superseded pointer, index | 12 | history |
| Kept | 7 | profile, 5 pointers, index |

**Contradiction resolved.** The approval conflict existed only between memory copies. Config already
settles it: rule 17 (confirm before starting non-trivial new work) and rule 22 (run an approved plan
to completion without re-confirming each step) name each other. Neither memory copy is read any
more.

**Also retired:** `docs/interaction-preferences.md` and `docs/file-organisation-rules.md`, now
`archive/docs/*-history-to-20261021.md`:
- the first restated rules 16–29
- the second held the retired `Sessions-v2/` scheme and legacy filename templates

`cfg_behaviour_class.authoritative_doc` for `chat` and `terminal` pointed at the first. It is now
empty: the rules are the authority.

## 1. New rules (from memory only)

| Class | Rule key |
|---|---|
| chat | `fix-standard-violations-dont-ask`, `read-instruction-in-whole-chat-context`, `names-not-bare-codes`, `ready-to-run-commands`, `status-reports-checked-facts-only` |
| development | `match-established-convention-when-extending`, `check-new-rules-against-existing-first`, `diagnosis-is-not-licence-to-build`, `no-per-item-approval-steps-in-designs` |
| sqlite | `enumerate-link-tables-before-orphan-verdict` |
| terminal | `tool-layer-escaping-checks` |
| study_method | `read-verses-before-asking`, `surface-is-the-sensitivity-lens`, `filters-are-working-aids`, `narrative-is-story-claims-are-derived` |

## 2. For the USER-GUIDE rewrite (#2187)

These are tool facts, not rules:
- closing a `configmaint.propose` item with `-NeedsFollowup 0`
- `ready_for_approval` needs `-AssignedTo` to move an item
- file links go in `-Context`, not `-Resolution`
- Claude's own propose for an already-decided change goes straight to `ready_for_approval`
- a dispatcher-tied item's `AnswerRun` is Claude-only
- check the Excel tool sheets for a lock file before writing
- the token-cost history tool

## 3. For the researcher when the study re-opens

29 study principles from June–July. They may still hold under the fan-out method, or may belong to
the retired pipeline:
- inner-being full scope
- the lens on processes, not the God-relation
- set-aside verses inform word meaning
- resist grouping
- passage-grounded meaning
- read by passage
- verse-level completeness
- phenomenon-level emergent reading
- no forced structure
- external pole is not an inner state
- God as arena
- multi-lens reads
- each chapter from first principles
- no statistics as review
- coverage flags
- the two governing principles
- revisit as a rule
- the term corpus anchors meaning
- understand a term in its cluster
- passage debate keeps every party open
- qualifiers carry dimensions
- qualifiers route per occurrence
- the characteristic list validates and never imputes
- a verse's raw data pulls all evidence
- the lexical is strictly verse-bounded
- no rework paid twice
- analytical before editorial
- verify contributor references
- chat versus API for classification

They are archived, not lost. Making any of them a `study_method` rule is the researcher's call; I
haven't judged their currency.

## 4. Not done here

- `docs/` still holds 36 old pre-IBA files (Session A architecture, schema overviews from
  July, filing audits) that no routine reads. They are candidates for the same retirement check as
  D (#2182).
- The git mirror of memory (`memory/` in the repo) and the NAS mirror copy the memory folder as it
  now is, at their next run.

## 5. Every memory file

| File | Disposition |
|---|---|
| `MEMORY.md` | kept |
| `archive-demoted-index-pre-20260721.md` | index or history |
| `feedback_ai_package_self_declaration.md` | retired method (history) |
| `feedback_alignment_work_is_register_driven_plan_gated.md` | retired method (history) |
| `feedback_all_study_work_in_db.md` | retired method (history) |
| `feedback_analytical_phase_vs_editorial_phase.md` | study principle: currency to be settled when the study re-opens |
| `feedback_audit_before_prose.md` | retired method (history) |
| `feedback_audit_deliverables_need_cross_check_before_presenting.md` | in config: rule 65 |
| `feedback_audit_must_be_self_critical.md` | retired method (history) |
| `feedback_authoritative_source_only.md` | in config: rule 83 |
| `feedback_avoid_unsubstantiated_superlatives.md` | in config: rule 36 |
| `feedback_backslash_b_becomes_backspace_byte.md` | new rule (#2184) |
| `feedback_bake_guidance_into_authoritative_instructions.md` | in config: rule 31 |
| `feedback_boundary_resolution_required.md` | retired method (history) |
| `feedback_brief_classifier_pass.md` | retired method (history) |
| `feedback_candidate_seed_independent_over_inclusive_control.md` | retired method (history) |
| `feedback_catalogue_refit_four_principles.md` | retired method (history) |
| `feedback_cc_only_pipeline_verdict.md` | retired method (history) |
| `feedback_char_driven_read_not_span_sweep.md` | retired method (history) |
| `feedback_characteristic_is_typed_term_in_verse.md` | retired method (history) |
| `feedback_characteristic_list_validates_not_imputes.md` | study principle: currency to be settled when the study re-opens |
| `feedback_chat_items_become_escalations_same_turn.md` | in config: rule 21 |
| `feedback_chat_vs_api_for_classification.md` | study principle: currency to be settled when the study re-opens |
| `feedback_check_governance_layers_not_just_pipeline.md` | in config: rule 31 |
| `feedback_check_new_rules_against_existing_governance_first.md` | new rule (#2184) |
| `feedback_claims_register_keeps_narrative_honest.md` | in config: rule 77 |
| `feedback_clarifications_reusable_but_state_not_induce.md` | retired method (history) |
| `feedback_close_configmaint_propose_with_needsfollowup0.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_close_the_loop_not_just_investigate_and_report.md` | in config: rule 23 |
| `feedback_cluster_file_naming_canonical.md` | retired method (history) |
| `feedback_cluster_publish_outputs.md` | retired method (history) |
| `feedback_cluster_status_advance.md` | retired method (history) |
| `feedback_column_alignment_is_claudes_job_not_a_question_back.md` | new rule (#2184) |
| `feedback_comment_to_findings_model.md` | retired method (history) |
| `feedback_commit_incrementally.md` | in config: rule 26 |
| `feedback_confirm_folder_destinations_until_baselines_reset.md` | in config: rule 59 |
| `feedback_confirm_output_exists_before_reporting_done.md` | in config: rule 2 |
| `feedback_copilot_frustration.md` | in config: user_profile |
| `feedback_coverage_flags_philosophy.md` | study principle: currency to be settled when the study re-opens |
| `feedback_cross_cluster_co_occurrence.md` | retired method (history) |
| `feedback_decision_required_never_via_answerrun.md` | in config: rule 45 |
| `feedback_default_readonly_db_connections.md` | in config: rule 11 |
| `feedback_deliberately_sparse_instructions_to_probe_defaults.md` | in config: user_profile |
| `feedback_design_build_needs_checkpoint_not_just_diagnosis.md` | new rule (#2184) |
| `feedback_design_work_is_never_self_correctable.md` | new rule (#2184) |
| `feedback_developer_mode_trust_is_the_only_constraint.md` | in config: rule 97 |
| `feedback_developer_mode_vs_app_mode_operating_model.md` | in config: rule 97; CHARTER section 4 |
| `feedback_devmode_bulk_config_is_a_migration_not_propose.md` | in config: rule 75 |
| `feedback_doc_archaeology_signals_missing_config.md` | in config: governance.past_precedent_investigation_signals_missing_config |
| `feedback_document_scope_decisions_prominently_not_just_in_escalations.md` | in config: rule 31 (its CLAUDE.md framing replaced by the control map) |
| `feedback_dont_assume_which_database.md` | in config: rule 13 |
| `feedback_dont_bake_design_judgment_calls_into_code_fixes.md` | in config: rule 44 |
| `feedback_dont_restate_stale_memory_status_suffix.md` | in config: moot: memory holds no state |
| `feedback_dont_sidestep_reported_ps_errors.md` | in config: rule 28 |
| `feedback_each_chapter_first_principles_find_the_gems.md` | study principle: currency to be settled when the study re-opens |
| `feedback_emergent_aggregate_questions.md` | retired method (history) |
| `feedback_entry_word_is_not_the_main_operation.md` | in config: rule 73 |
| `feedback_enumerate_link_tables_first.md` | new rule (#2184) |
| `feedback_escalation_answerrun_is_claude_only_reassign_for_researcher.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_escalation_links_go_in_context_not_resolution.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_escalation_reassign_requires_assignedto.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_evidence_signal_completeness.md` | retired method (history) |
| `feedback_expression_vs_characteristic_object_type.md` | retired method (history) |
| `feedback_external_pole_not_inner_state.md` | study principle: currency to be settled when the study re-opens |
| `feedback_faculty_must_be_per_term_not_per_cluster.md` | retired method (history) |
| `feedback_faculty_only_if_explicit_or_inferred_on_verse.md` | retired method (history) |
| `feedback_filing_is_first_class_governance.md` | in config: rules 56-59 |
| `feedback_filters_are_working_aids_not_decision_items.md` | new rule (#2184) |
| `feedback_findings_marginal_value.md` | retired method (history) |
| `feedback_fix_standard_violations_dont_ask.md` | new rule (#2184) |
| `feedback_focused_capture_no_whole_scope_tasks.md` | in config: rule 84 |
| `feedback_follow_filing_standards.md` | in config: rules 56-59 |
| `feedback_heredoc_only_in_powershell.md` | in config: rule 27 |
| `feedback_holy_spirit_part_of_13_1_divine.md` | in config: rule 87 |
| `feedback_ib_screen_first_god_is_arena.md` | study principle: currency to be settled when the study re-opens |
| `feedback_iba_backfill_cluster_assignment_via_analysis_not_bulk_automation.md` | retired method (history) |
| `feedback_iba_completeness_check_against_live_upstream_source.md` | retired method (history) |
| `feedback_iba_config_changes_require_researcher_approval_never_silent.md` | in config: the propose gate (GOVERNANCE.md section 4) |
| `feedback_iba_config_first_not_doc_archaeology.md` | in config: governance.past_precedent_investigation_signals_missing_config |
| `feedback_iba_data_judgment_calls_must_escalate_not_silent_report.md` | in config: rule 40 |
| `feedback_iba_exploratory_use_logs_escalations_not_inline_fixes.md` | in config: rules 21, 40 |
| `feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches.md` | in config: rule 62; governance.new_utility_registration_timing |
| `feedback_iba_gap_analysis_requires_live_build_inspection.md` | in config: rules 1, 65 |
| `feedback_iba_no_synthesis_small_units_only.md` | retired method (history) |
| `feedback_iba_phenomenon_set_hib_first_lexical_verified.md` | retired method (history) |
| `feedback_iba_preapproved_instructions_self_approve_configmaint.md` | retired method (history) |
| `feedback_iba_record_rules_when_set_in_configs.md` | in config: rule 31 |
| `feedback_iba_session_start_read_live_docs_not_memory.md` | in config: rule 81 (the start routine) |
| `feedback_iba_validation_approval_must_be_representative_and_three_way.md` | in config: rule 63 |
| `feedback_inactive_tables_never_active_inputs.md` | in config: rule 61 |
| `feedback_inner_being_full_scope.md` | study principle: currency to be settled when the study re-opens |
| `feedback_integrity_and_intent_first.md` | in config: rules 1, 19 |
| `feedback_interaction_over_reallocation.md` | in config: rule 70 |
| `feedback_interaction_protocols.md` | in config: rules 17, 18, 19 |
| `feedback_interdependent_clusters_finalise_together.md` | retired method (history) |
| `feedback_keyword_digestion_methodology.md` | retired method (history) |
| `feedback_keyword_discovery_interim_phase.md` | retired method (history) |
| `feedback_l1_l2_is_multi_angle_report_then_synthesise.md` | retired method (history) |
| `feedback_l1_must_be_verse_aware.md` | retired method (history) |
| `feedback_l2_mechanical_api_triage.md` | retired method (history) |
| `feedback_label_inferential_output_not_confirmed.md` | in config: rule 4 |
| `feedback_lens_is_inner_being_process_not_god_relation.md` | study principle: currency to be settled when the study re-opens |
| `feedback_let_scripture_speak_no_imputed_synthesis.md` | in config: rule 69 |
| `feedback_lexical_revelation_test_step3_gate.md` | retired method (history) |
| `feedback_lexical_review_is_insight_coverage_not_stats.md` | retired method (history) |
| `feedback_lexical_strictly_verse_bounded_no_implied_evidence.md` | study principle: currency to be settled when the study re-opens |
| `feedback_match_established_convention_when_extending.md` | new rule (#2184) |
| `feedback_methodology_cycle_cost.md` | retired method (history) |
| `feedback_multilens_layered_reads_foundation_no_drift.md` | study principle: currency to be settled when the study re-opens |
| `feedback_name_dimensions_not_just_codes.md` | new rule (#2184) |
| `feedback_narrative_citation_is_verse_level_not_word_coverage.md` | in config: rule 93 |
| `feedback_narrative_is_story_claims_are_derived_statements.md` | new rule (#2184) |
| `feedback_never_model_output_on_prior_unreviewed_pass.md` | in config: rule 37 |
| `feedback_no_approval_steps_researcher_feedback_in_chat.md` | new rule (#2184) |
| `feedback_no_askuserquestion_tool.md` | in config: rule 16 |
| `feedback_no_forced_structure_audit_surfaces_analysis_compensates.md` | study principle: currency to be settled when the study re-opens |
| `feedback_no_hedge_pointers_in_complete_records.md` | in config: rule 32 |
| `feedback_no_patch_to_nice_pointintime_result.md` | in config: rule 38 |
| `feedback_no_rework_paid_twice.md` | study principle: currency to be settled when the study re-opens |
| `feedback_no_stats_trends_review_fabricated_data.md` | study principle: currency to be settled when the study re-opens |
| `feedback_no_unchecked_claims_in_status_reports.md` | new rule (#2184) |
| `feedback_obslog_discipline_for_cc.md` | retired method (history) |
| `feedback_ontology_typed_relationships.md` | retired method (history) |
| `feedback_open_threads_register_check_each_unit.md` | in config: rule 74 |
| `feedback_own_propose_calls_ready_for_approval.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_passage_debate_dont_force_close_eqs_cover_all_parties.md` | study principle: currency to be settled when the study re-opens |
| `feedback_patch_format.md` | retired method (history) |
| `feedback_per_chapter_scaffolding_validated.md` | retired method (history) |
| `feedback_phase2_passa_emits_keywords.md` | retired method (history) |
| `feedback_phase3_verse_level_relationship_test.md` | retired method (history) |
| `feedback_phase5_subgroups_represent_characteristics.md` | retired method (history) |
| `feedback_phase8_silent_softdelete.md` | retired method (history) |
| `feedback_phase9_science_extract_required.md` | retired method (history) |
| `feedback_phase9_tier_by_tier_mandatory.md` | retired method (history) |
| `feedback_phase_a_light_meaning_at_vcg.md` | retired method (history) |
| `feedback_phase_brief_standard_practice.md` | retired method (history) |
| `feedback_phenomenon_level_emergent_reading.md` | study principle: currency to be settled when the study re-opens |
| `feedback_powershell_dollar_escaping.md` | new rule (#2184) |
| `feedback_pre_op_db_snapshots_prune_or_skip.md` | retired method (history) |
| `feedback_pre_phase1_split_pattern.md` | retired method (history) |
| `feedback_present_ready_to_run_ps_commands.md` | new rule (#2184) |
| `feedback_proceed_autonomously_on_stable_rules.md` | in config: rule 22 |
| `feedback_qualifier_routes_per_verse_occurrence.md` | study principle: currency to be settled when the study re-opens |
| `feedback_qualifiers_carry_modifying_dimensions.md` | study principle: currency to be settled when the study re-opens |
| `feedback_quality_regression_selfcheck_and_apply_memory.md` | in config: rules 2, 29 |
| `feedback_re_examination_workflow.md` | retired method (history) |
| `feedback_read_by_passage_not_whole_chapter.md` | study principle: currency to be settled when the study re-opens |
| `feedback_read_completeness_is_verse_level_not_passage_level.md` | study principle: currency to be settled when the study re-opens |
| `feedback_read_researcher_comment_in_whole_chat_context.md` | new rule (#2184) |
| `feedback_read_the_whole_passage_of_a_marked_verse.md` | in config: rule 91 |
| `feedback_read_verse_for_inner_act_not_event_template.md` | in config: rule 91 |
| `feedback_read_verses_before_asking_researcher.md` | new rule (#2184) |
| `feedback_remediation_is_analysis_not_reassignment.md` | retired method (history) |
| `feedback_remediation_stop_points.md` | retired method (history) |
| `feedback_report_shape_that_worked_ot02.md` | new rule (#2184) |
| `feedback_researcher_pictures_not_narrative_terms.md` | in config: rule 86 |
| `feedback_resist_grouping_preserve_distinctions.md` | study principle: currency to be settled when the study re-opens |
| `feedback_reusable_engine_scripts_and_continuous_learning.md` | in config: governance.scripts_and_routines |
| `feedback_reuse_extracted_base_data.md` | in config: rule 71 |
| `feedback_review_via_files_not_chat.md` | in config: rule 16 |
| `feedback_revisit_as_rule.md` | study principle: currency to be settled when the study re-opens |
| `feedback_role_label_never_licenses_dropping_what_verse_joins.md` | in config: rule 73 |
| `feedback_root_fix_not_one_off.md` | in config: rule 38 |
| `feedback_route_dual_cluster_findings.md` | retired method (history) |
| `feedback_rule_extract_obsolete_default.md` | retired method (history) |
| `feedback_session_b_findings_resolved_through_l2.md` | retired method (history) |
| `feedback_session_log_every_session_read_config_not_folders.md` | in config: governance.session_log_required_content |
| `feedback_setaside_verses_inform_word_meaning.md` | study principle: currency to be settled when the study re-opens |
| `feedback_simple_steps_not_engineered_designs.md` | in config: rule 39 |
| `feedback_single_living_register.md` | in config: rule 33 |
| `feedback_small_chunks_over_elaborate_pipelines.md` | retired method (history) |
| `feedback_source_of_truth_is_written_record.md` | in config: rule 34 |
| `feedback_span_pairing_and_reciprocal_findings.md` | retired method (history) |
| `feedback_spec_review_edits_in_situ_not_versioned.md` | retired method (history) |
| `feedback_step_only_through_raw_layer.md` | in config: rule 95 |
| `feedback_strand_pulls_check_t_coded_synonyms.md` | in config: rule 94 |
| `feedback_structural_validation_is_not_value_quality_validation.md` | in config: rule 24 |
| `feedback_surface_is_the_sensitivity_lens.md` | new rule (#2184) |
| `feedback_t1_vs_t2_ontology.md` | retired method (history) |
| `feedback_t2_reference_flag_reclassify.md` | retired method (history) |
| `feedback_term_corpus_anchors_meaning.md` | study principle: currency to be settled when the study re-opens |
| `feedback_term_coverage_cascade_is_index_not_census.md` | retired method (history) |
| `feedback_term_is_the_unit_of_movement.md` | retired method (history) |
| `feedback_test_dimensions_for_reader_drift.md` | retired method (history) |
| `feedback_threads_are_handle_networks_cleared_by_cluster_work.md` | in config: rule 74 |
| `feedback_three_cluster_types.md` | retired method (history) |
| `feedback_token_cost_history_required.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_transitive_faculty_verb_is_qualifier.md` | retired method (history) |
| `feedback_translit_always_with_gloss.md` | new rule (#2184) |
| `feedback_two_governing_principles.md` | study principle: currency to be settled when the study re-opens |
| `feedback_understand_term_in_cluster_not_export.md` | study principle: currency to be settled when the study re-opens |
| `feedback_use_cluster_full_names.md` | new rule (#2184) |
| `feedback_use_descriptive_nomenclature_not_invented_codes.md` | new rule (#2184) |
| `feedback_verify_before_reporting_fixed.md` | in config: rule 29 |
| `feedback_verify_contributor_reference_text_first.md` | study principle: currency to be settled when the study re-opens |
| `feedback_verify_db_claims_via_visible_tooling.md` | in config: rule 24 |
| `feedback_verify_db_state_before_acting.md` | in config: rule 1 |
| `feedback_verify_live_data_before_raising_design_question.md` | in config: rules 1, 16 |
| `feedback_verse_change_revalidation.md` | retired method (history) |
| `feedback_verse_level_extraction_feeds_tiers.md` | retired method (history) |
| `feedback_verse_meaning_grounded_not_imported.md` | study principle: currency to be settled when the study re-opens |
| `feedback_verse_raw_data_must_pull_all_study_evidence.md` | study principle: currency to be settled when the study re-opens |
| `feedback_version_discipline.md` | in config: rule 57 |
| `feedback_warn_before_editing_excel_tool_interface.md` | tool usage: for the USER-GUIDE rewrite (#2187) |
| `feedback_weave_not_fit_narrative.md` | in config: rule 88 |
| `feedback_weave_with_meaning_not_quote_lists.md` | in config: rules 90, 91 |
| `feedback_working_style.md` | in config: user_profile; rules 17, 19 |
| `index-iba-config-escalation-procedures.md` | index or history |
| `project_RESET_characteristics_to_movements_changeover.md` | project state or history (state lives in iba.db and the escalations) |
| `project_a1_resolved_rollup_v3_audit_design.md` | project state or history (state lives in iba.db and the escalations) |
| `project_ai_verse_analysis_shelved_20260924.md` | project state or history (state lives in iba.db and the escalations) |
| `project_all_clusters_l1_sweep_first.md` | project state or history (state lives in iba.db and the escalations) |
| `project_analysis_phase_augment_not_harvest_or_redo.md` | project state or history (state lives in iba.db and the escalations) |
| `project_api_reads_budget_bounded_small_batches.md` | project state or history (state lives in iba.db and the escalations) |
| `project_audit_sequencing_clusters_then_meaning.md` | project state or history (state lives in iba.db and the escalations) |
| `project_backup_alerting_and_outlook_smtp_block.md` | project state or history (state lives in iba.db and the escalations) |
| `project_base_data_spine_verse_span_strong_parse.md` | project state or history (state lives in iba.db and the escalations) |
| `project_bible_research_db_prose_only_20260924.md` | project state or history (state lives in iba.db and the escalations) |
| `project_book_lexical_readiness_assessment.md` | project state or history (state lives in iba.db and the escalations) |
| `project_candidate_characteristic_seed_and_role_model.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cc_generation_mode.md` | project state or history (state lives in iba.db and the escalations) |
| `project_change_of_character_key_discovery.md` | project state or history (state lives in iba.db and the escalations) |
| `project_characteristic_analysis_lexicon_noise_doubt.md` | project state or history (state lives in iba.db and the escalations) |
| `project_characteristic_backfill_backlog.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cluster_folder_rule.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cluster_health_test_m08_paused_20260829.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cluster_reading_token_cost_20260929.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cluster_review_backlog_and_m12_method_20260624.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cluster_rework_phase_started.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cluster_schema_live.md` | project state or history (state lives in iba.db and the escalations) |
| `project_column_wise_ve_hypothesis.md` | project state or history (state lives in iba.db and the escalations) |
| `project_constitution_cluster_and_flag_resolution.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cross_chapter_synthesis_per_characteristic.md` | project state or history (state lives in iba.db and the escalations) |
| `project_cross_cluster_three_link_classes.md` | project state or history (state lives in iba.db and the escalations) |
| `project_current_architecture_and_status_20260815.md` | project state or history (state lives in iba.db and the escalations) |
| `project_current_work.md` | project state or history (state lives in iba.db and the escalations) |
| `project_daniel_passage_debates_complete_narrative_next.md` | project state or history (state lives in iba.db and the escalations) |
| `project_db_loss_blocker_20260603.md` | project state or history (state lives in iba.db and the escalations) |
| `project_dim_c01_post_patch_plan.md` | project state or history (state lives in iba.db and the escalations) |
| `project_dimension_d13_cohabitation.md` | project state or history (state lives in iba.db and the escalations) |
| `project_engine_onboard_curate_terms_array.md` | project state or history (state lives in iba.db and the escalations) |
| `project_escalation_register_v9_built_20260821.md` | project state or history (state lives in iba.db and the escalations) |
| `project_extended_lexical_model_refinement.md` | project state or history (state lives in iba.db and the escalations) |
| `project_faculty_not_gripped_audit_20260624.md` | project state or history (state lives in iba.db and the escalations) |
| `project_fan_out_replaces_cluster_analysis_20260930.md` | project state or history (state lives in iba.db and the escalations) |
| `project_findings_audit_gate_live.md` | project state or history (state lives in iba.db and the escalations) |
| `project_findings_capture_file_as_finding.md` | project state or history (state lives in iba.db and the escalations) |
| `project_flesh_and_body_strand_2162.md` | project state or history (state lives in iba.db and the escalations) |
| `project_focus_points_scripture_as_data_source.md` | project state or history (state lives in iba.db and the escalations) |
| `project_genesis_narrative_span_depth_progress.md` | project state or history (state lives in iba.db and the escalations) |
| `project_git_remote_silently_blocked_by_large_file.md` | project state or history (state lives in iba.db and the escalations) |
| `project_god_character_routing_20261007.md` | project state or history (state lives in iba.db and the escalations) |
| `project_ib_characteristic_meaning_keyed.md` | project state or history (state lives in iba.db and the escalations) |
| `project_ib_observation_folds_into_ve_lexical.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_analytic_phase_blocked_on_data_layer_stability.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_book_by_book_debate_phase.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_candidate_seeding_registry_direct_noise.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_config_governance_hardening_20260730.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_config_report_required.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_configmaint_escalation_self_answered_anomaly.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_cross_book_theme_mechanism_flagged.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_db_is_master_over_legacy_json_seeds.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_narrative_generate_pipeline_built.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_output_spiderweb_process_locality_augment.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_passage_debate_no_separate_ai_chat_needed.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_study_reopened_20260805_v4.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_value_quality_engine_and_candidate_curate.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_verse_existence_gated_on_term_discovery.md` | project state or history (state lives in iba.db and the escalations) |
| `project_iba_verse_reading_v3_judged_failed_consistency_unresolved.md` | project state or history (state lives in iba.db and the escalations) |
| `project_inner_being_narrative_reset_20260930.md` | project state or history (state lives in iba.db and the escalations) |
| `project_inner_being_reading_questions_first.md` | project state or history (state lives in iba.db and the escalations) |
| `project_keyword_analytics_revision_parked.md` | project state or history (state lives in iba.db and the escalations) |
| `project_l1l2_field_reliability_direction.md` | project state or history (state lives in iba.db and the escalations) |
| `project_l2_multicluster_learnings_20260609.md` | project state or history (state lives in iba.db and the escalations) |
| `project_l2_verse_read_meaning_live.md` | project state or history (state lives in iba.db and the escalations) |
| `project_l2_writer_verse_complete.md` | project state or history (state lives in iba.db and the escalations) |
| `project_leviticus_terminology_study.md` | project state or history (state lives in iba.db and the escalations) |
| `project_lexical_cycle_finalised_and_integrity_invariant.md` | project state or history (state lives in iba.db and the escalations) |
| `project_lexical_prose_endpoint_and_ve_lexical_phase1.md` | project state or history (state lives in iba.db and the escalations) |
| `project_lexical_rule_validation_failed_build_headless_app.md` | project state or history (state lives in iba.db and the escalations) |
| `project_lexical_rules_reset_process_reframe.md` | project state or history (state lives in iba.db and the escalations) |
| `project_location_seat_engine_fixed.md` | project state or history (state lives in iba.db and the escalations) |
| `project_m04_paused_at_phase9.md` | project state or history (state lives in iba.db and the escalations) |
| `project_m10_family_status_primary_logical_units.md` | project state or history (state lives in iba.db and the escalations) |
| `project_m47_cross_cluster_batches.md` | project state or history (state lives in iba.db and the escalations) |
| `project_m64_focused_strand_20261006.md` | project state or history (state lives in iba.db and the escalations) |
| `project_m72_scope_titles_are_qualifiers.md` | project state or history (state lives in iba.db and the escalations) |
| `project_meaning_centric_direction_emerging.md` | project state or history (state lives in iba.db and the escalations) |
| `project_meaning_duplicates_then_fabricates.md` | project state or history (state lives in iba.db and the escalations) |
| `project_measure_layer_persisted.md` | project state or history (state lives in iba.db and the escalations) |
| `project_method_checkpoint_v3_2_evolves_not_replaced.md` | project state or history (state lives in iba.db and the escalations) |
| `project_morph_is_source_of_truth.md` | project state or history (state lives in iba.db and the escalations) |
| `project_movement_operation_definition_written.md` | project state or history (state lives in iba.db and the escalations) |
| `project_multi_contributor_spiderweb.md` | project state or history (state lives in iba.db and the escalations) |
| `project_narrative_claim_register_in_iba_db_2110.md` | project state or history (state lives in iba.db and the escalations) |
| `project_new_word_retirement_blocked.md` | project state or history (state lives in iba.db and the escalations) |
| `project_next_action_audit_surface_verses.md` | project state or history (state lives in iba.db and the escalations) |
| `project_open_loops_20260415.md` | project state or history (state lives in iba.db and the escalations) |
| `project_otdbr009_overdeleted_core_ib_terms.md` | project state or history (state lives in iba.db and the escalations) |
| `project_p2_l2_decision_architecture.md` | project state or history (state lives in iba.db and the escalations) |
| `project_passage_reading_checkback_gate.md` | project state or history (state lives in iba.db and the escalations) |
| `project_per_book_corrective_pipeline.md` | project state or history (state lives in iba.db and the escalations) |
| `project_poetic_chapter_driven_method.md` | project state or history (state lives in iba.db and the escalations) |
| `project_pointer_lifecycle_model.md` | project state or history (state lives in iba.db and the escalations) |
| `project_poor_needy_multiple_dimensions.md` | project state or history (state lives in iba.db and the escalations) |
| `project_prophets_wisdom_read_at_movement_depth_debt.md` | project state or history (state lives in iba.db and the escalations) |
| `project_psalms_narratives_rollout_complete.md` | project state or history (state lives in iba.db and the escalations) |
| `project_reconstruction_baseline_20260614.md` | project state or history (state lives in iba.db and the escalations) |
| `project_registry_words_not_all_lexically_grounded.md` | project state or history (state lives in iba.db and the escalations) |
| `project_remediation_orchestrator_active.md` | project state or history (state lives in iba.db and the escalations) |
| `project_reread_success_gates_and_scored_audit.md` | project state or history (state lives in iba.db and the escalations) |
| `project_session_d_moot.md` | project state or history (state lives in iba.db and the escalations) |
| `project_signpost_hands_inner_being.md` | project state or history (state lives in iba.db and the escalations) |
| `project_step_60cap_truncation_and_forwardwalk_fix.md` | project state or history (state lives in iba.db and the escalations) |
| `project_study_closed_20260803.md` | project state or history (state lives in iba.db and the escalations) |
| `project_superstructure_eisegesis_validation_20260624.md` | project state or history (state lives in iba.db and the escalations) |
| `project_t2_flag_are_seats_and_qualifiers.md` | project state or history (state lives in iba.db and the escalations) |
| `project_term_anchor_reset.md` | project state or history (state lives in iba.db and the escalations) |
| `project_term_driven_genre_aware_lexical_method.md` | project state or history (state lives in iba.db and the escalations) |
| `project_term_is_sense_not_lemma.md` | project state or history (state lives in iba.db and the escalations) |
| `project_v25_audit_tool.md` | project state or history (state lives in iba.db and the escalations) |
| `project_v3_0_active.md` | project state or history (state lives in iba.db and the escalations) |
| `project_v3_0_catch_up_done.md` | project state or history (state lives in iba.db and the escalations) |
| `project_ve_lexical_is_verse_first.md` | project state or history (state lives in iba.db and the escalations) |
| `project_ve_lexical_normalisation_and_groundings.md` | project state or history (state lives in iba.db and the escalations) |
| `project_ve_proposition_gap.md` | project state or history (state lives in iba.db and the escalations) |
| `project_verse_extraction_cause_side_gap.md` | project state or history (state lives in iba.db and the escalations) |
| `project_verse_fanout_operating_model.md` | project state or history (state lives in iba.db and the escalations) |
| `project_verse_layer_rollout_before_distill.md` | project state or history (state lives in iba.db and the escalations) |
| `project_work_done_in_online_interface_20261002.md` | project state or history (state lives in iba.db and the escalations) |
| `reference_analysis_rules_finding_lifecycle.md` | stale or superseded pointer (history) |
| `reference_canonical_tier_scheme_is_T0_T7.md` | stale or superseded pointer (history) |
| `reference_chat_responses_notes_location.md` | kept |
| `reference_core_memory_orientation_map.md` | stale or superseded pointer (history) |
| `reference_esv_verse_text_in_iba_db.md` | kept |
| `reference_file_index_legacy_use_bypass_fks.md` | stale or superseded pointer (history) |
| `reference_iba_live_config_is_db_resident.md` | stale or superseded pointer (history) |
| `reference_narrative_passage_table_holds_only_told_passages.md` | kept |
| `reference_operational_governance_git_backup_manifest.md` | stale or superseded pointer (history) |
| `reference_reusable_scripts_catalogue.md` | stale or superseded pointer (history) |
| `reference_strong_related_keyed_on_exact_code_not_base.md` | kept |
| `reference_strongs_zero_padded_4digit_in_db.md` | kept |
| `reference_study_definition_and_nine_principles.md` | stale or superseded pointer (history) |
| `reference_study_end_point_and_milestones.md` | stale or superseded pointer (history) |
| `reference_term_add_update_authoritative.md` | stale or superseded pointer (history) |
| `user_profile.md` | kept |
