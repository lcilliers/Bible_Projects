# Memory Index

> One line per memory; detail in the topic file. Demoted memories are unindexed files, recoverable via the foot comment blocks.

## ★ Foundational — always apply

- [feedback_review_via_files_not_chat](feedback_review_via_files_not_chat.md) — ★★ `AskUserQuestion` is BANNED + config-blocked project-wide (permissions.deny) since 2026-07-22 — 3rd violation, one answer lost entirely. Use plain chat or a filed .md review instead, always.
- [feedback_token_cost_history_required](feedback_token_cost_history_required.md) — ★ COST: on-disk auditable token/cost history REQUIRED (cost_ledger.py); Claude Code = subscription; ~87% cost is context → one task/session.
- [project_api_reads_budget_bounded_small_batches](project_api_reads_budget_bounded_small_batches.md) — ★ COST: API reads = small bounded batches + $ estimate + checkpoint; NEVER full-corpus push.
- [feedback_iba_no_synthesis_small_units_only](feedback_iba_no_synthesis_small_units_only.md) — ★ IBA planning docs: NEVER self-synthesize across docs; ask if resolved elsewhere first; small dictated units only.
- [feedback_iba_gap_analysis_requires_live_build_inspection](feedback_iba_gap_analysis_requires_live_build_inspection.md) — ★ IBA gap/compliance work: inspect LIVE code+DB, never doc-text dump; utility-before-use, rule-before-fix; check full principle/sextet.
- [feedback_iba_completeness_check_against_live_upstream_source](feedback_iba_completeness_check_against_live_upstream_source.md) — ★ "does X capture everything" = call the LIVE upstream source (STEP) directly and diff its full field set against the DB, not just re-check extract logic against DB.
- [feedback_structural_validation_is_not_value_quality_validation](feedback_structural_validation_is_not_value_quality_validation.md) — ★ a validate step passing (FK/notnull/enum) ≠ values are fit for purpose; check both, separately, always.
- [feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches](feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches.md) — ★ IBA "fixes" = mostly CONFIG CONTENT or a utility needing REGISTRATION in cfg_work_package/cfg_step — not code patches; triage into 3 buckets first.
- [feedback_iba_config_first_not_doc_archaeology](feedback_iba_config_first_not_doc_archaeology.md) — ★★ ANY IBA task starts at cfg_work_package/cfg_step (find the routine) then cfg_setting (its inputs) — NEVER start from instruction docs or prior output files.
- [project_iba_db_is_master_over_legacy_json_seeds](project_iba_db_is_master_over_legacy_json_seeds.md) — ★ IBA: live DB (cfg_* AND candidate_seed) = MASTER; old/archived JSON seeds = one-time reference only, NEVER a reload source.
- [feedback_iba_config_changes_require_researcher_approval_never_silent](feedback_iba_config_changes_require_researcher_approval_never_silent.md) — ★ IBA config changes: NEVER silent/automatic writes — propose→validate→escalate→apply.
- [feedback_iba_validation_approval_must_be_representative_and_three_way](feedback_iba_validation_approval_must_be_representative_and_three_way.md) — ★ IBA escalations: payload must be REPRESENTATIVE (tailored, not a generic diff); answer = Approve/Not-approve/Resubmit-with-comment, never yes/no.
- [feedback_iba_data_judgment_calls_must_escalate_not_silent_report](feedback_iba_data_judgment_calls_must_escalate_not_silent_report.md) — ★ IBA: any check needing a researcher JUDGMENT CALL must ESCALATE (batched per-run if count is large), never a silent advisory list in Outcome.counts — only 3/15 conditions app-wide currently escalate.
- [feedback_fix_standard_violations_dont_ask](feedback_fix_standard_violations_dont_ask.md) — ★ deviation from an ALREADY-established, documented standard = a bug, fix it, don't ask "should I?" — only ask on genuine judgment calls.
- [feedback_close_the_loop_not_just_investigate_and_report](feedback_close_the_loop_not_just_investigate_and_report.md) — ★ don't stall reviews at "found it, here's a doc" — implement/fix/verify before reporting back.
- [feedback_iba_record_rules_when_set_in_configs](feedback_iba_record_rules_when_set_in_configs.md) — ★ IBA rules defined many times over in docs/logs already; search hard before claiming a gap; record+APPLY rules when configs set them, not just memory-update.
- [feedback_iba_preapproved_instructions_self_approve_configmaint](feedback_iba_preapproved_instructions_self_approve_configmaint.md) — ★ 07-23 backlog-clearing ONLY: self-approve configmaint.propose runs that faithfully implement already-detailed researcher instructions; flag disagreement/uncovered judgment calls instead.
- [feedback_iba_session_start_read_live_docs_not_memory](feedback_iba_session_start_read_live_docs_not_memory.md) — ★ IBA session start: actually Read GOVERNANCE.md/BUILD.md/CONFIG-REPORT.md before governance claims — don't answer from memory summaries alone.
- [feedback_iba_exploratory_use_logs_escalations_not_inline_fixes](feedback_iba_exploratory_use_logs_escalations_not_inline_fixes.md) — ★ during app-usage sessions: log spotted errors as escalations (Escalation.ps1 -Action Raise), don't fix inline, until told to clear backlog.
- [feedback_avoid_unsubstantiated_superlatives](feedback_avoid_unsubstantiated_superlatives.md) — ★ don't write "most/clearest/strongest" unless actually checked against every candidate; state the fact plainly instead.

- [feedback_source_of_truth_is_written_record](feedback_source_of_truth_is_written_record.md) — truth = written record via file_manifest; verify, don't assert.
- [feedback_simple_steps_not_engineered_designs](feedback_simple_steps_not_engineered_designs.md) — ★ build in SIMPLE STEPS; machinery-heavy plans get rejected as overengineering.
- [feedback_interaction_protocols](feedback_interaction_protocols.md) — confirm before acting; write workings to files; no guessing.
- [feedback_proceed_autonomously_on_stable_rules](feedback_proceed_autonomously_on_stable_rules.md) — once rules/plan set, run to completion; don't stop every step.
- [feedback_reusable_engine_scripts_and_continuous_learning](feedback_reusable_engine_scripts_and_continuous_learning.md) — scripts REUSABLE, parameter-driven; read back, update rules, re-run.
- [feedback_integrity_and_intent_first](feedback_integrity_and_intent_first.md) — ask intent/integrity BEFORE acting; never act on unverified data.
- [feedback_quality_regression_selfcheck_and_apply_memory](feedback_quality_regression_selfcheck_and_apply_memory.md) — self-check vs known; APPLY memory; act on clear instruction.
- [feedback_filing_is_first_class_governance](feedback_filing_is_first_class_governance.md) — filing/file-org is first-class governance.
- [feedback_follow_filing_standards](feedback_follow_filing_standards.md) — comply with docs/file-organisation-rules.md.
- [feedback_single_living_register](feedback_single_living_register.md) — an investigation = ONE living doc; update in place, strike reversals.
- [feedback_commit_incrementally](feedback_commit_incrementally.md) — commit units of work throughout the session.
- [feedback_check_governance_layers_not_just_pipeline](feedback_check_governance_layers_not_just_pipeline.md) — weight governance/operational layers, not just the pipeline.
- [feedback_bake_guidance_into_authoritative_instructions](feedback_bake_guidance_into_authoritative_instructions.md) — researcher guidance goes into dated authoritative instructions, not only memory.
- [feedback_root_fix_not_one_off](feedback_root_fix_not_one_off.md) — fix the cause not the instance; NEVER a one-off when it may recur.

## Active state

- [project_iba_book_by_book_debate_phase](project_iba_book_by_book_debate_phase.md) — ★★ 07-28: NEW MAJOR PHASE — passage-debate every book of the Bible, prophets first then other genres, ~1.5 months. Book 1 Daniel + book 2 Jonah done, book 3 Joel PARKED; check here first for current book-by-book status.
- [project_iba_verse_existence_gated_on_term_discovery](project_iba_verse_existence_gated_on_term_discovery.md) — ★ 07-29: OPEN — a verse only exists in `iba.db` if term-discovery surfaced a study word there (Joel 1:15/2:4 missing); dedicated session needed before Joel/any book resumes.
- [project_iba_passage_debate_no_separate_ai_chat_needed](project_iba_passage_debate_no_separate_ai_chat_needed.md) — ★ 07-27: passage-debate work done directly in Claude Code via `report.passage_debate`; the old separate Claude.ai upload-chat workflow is no longer needed.
- [feedback_passage_debate_dont_force_close_eqs_cover_all_parties](feedback_passage_debate_dont_force_close_eqs_cover_all_parties.md) — ★ 07-28: leave emergent questions open, don't force-resolve; surface EVERY party's IB state (not just the protagonist) — confirmed on Jonah 1.
- [project_daniel_passage_debates_complete_narrative_next](project_daniel_passage_debates_complete_narrative_next.md) — RESOLVED 07-28: Daniel 1-12 debates+whole-book-read+3 narrative passes all complete; kept only for the reusable narrative-brief shape. See project_iba_book_by_book_debate_phase for current state.
- [project_iba_analytic_phase_blocked_on_data_layer_stability](project_iba_analytic_phase_blocked_on_data_layer_stability.md) — ★ 07-21: analytic phase paused, back to IBA core data-layer build (see Foundational IBA entries above).
- [project_iba_output_spiderweb_process_locality_augment](project_iba_output_spiderweb_process_locality_augment.md) — ★ 07-20: IBA output = SPIDERWEB of concordances; PROCESS = locality/augment not bulk-update.
- [project_iba_candidate_seeding_registry_direct_noise](project_iba_candidate_seeding_registry_direct_noise.md) — RESOLVED 07-19: candidate seeding fixed to double-control-only, 66 books → 1732 clean candidates.
- [project_lexical_cycle_finalised_and_integrity_invariant](project_lexical_cycle_finalised_and_integrity_invariant.md) — ★ 07-08: cycle finalised; candidate-without-verse-record = DB INTEGRITY VIOLATION.
- [project_reread_success_gates_and_scored_audit](project_reread_success_gates_and_scored_audit.md) — book re-reads measured by 9 gates G0-G8 + scored audit; baseline-then-delta.
- [project_book_lexical_readiness_assessment](project_book_lexical_readiness_assessment.md) — 07-12: repeatable BOOK-readiness pre-flight; registry path + role model + staged sequence.
- [project_candidate_characteristic_seed_and_role_model](project_candidate_characteristic_seed_and_role_model.md) — role={characteristic,standalone,qualifier}; candidate≠role; 824 OT seed.
- [project_ib_characteristic_meaning_keyed](project_ib_characteristic_meaning_keyed.md) — 07-11: ib_characteristic keyed on MEANING-IN-CONTEXT; two-phase.
- [project_per_book_corrective_pipeline](project_per_book_corrective_pipeline.md) — per-book pipeline (a-e); onboarding via engine audit_word only.
- [project_otdbr009_overdeleted_core_ib_terms](project_otdbr009_overdeleted_core_ib_terms.md) — OT-DBR-009 over-deleted core IB terms; expect more per book.
- [project_leviticus_terminology_study](project_leviticus_terminology_study.md) — Leviticus as TERMINOLOGY study, corpus-native in DB; infra+pilot done.
- [project_genesis_narrative_span_depth_progress](project_genesis_narrative_span_depth_progress.md) — OT narratives SPAN DEPTH; Genesis 1-36 + Exodus Block 1 done; NEXT = Exodus Block 2.
- [project_passage_reading_checkback_gate](project_passage_reading_checkback_gate.md) — MANDATORY per-passage GATE; re-file until clean.
- [project_prophets_wisdom_read_at_movement_depth_debt](project_prophets_wisdom_read_at_movement_depth_debt.md) — filed prophet/wisdom readings = MOVEMENT-depth; span-depth DEBT.
- [project_poetic_chapter_driven_method](project_poetic_chapter_driven_method.md) — poetic chapter-driven; Phase1 per-verse + Phase2 whole-chapter. ★ PSALTER COMPLETE.
- [project_cross_chapter_synthesis_per_characteristic](project_cross_chapter_synthesis_per_characteristic.md) — NEXT: cross-chapter summary PER CHARACTERISTIC; re-align first.
- [project_movement_operation_definition_written](project_movement_operation_definition_written.md) — 07-26: "movement" definition signed off — Passage read guidance.md gives the operational subject/operation/source/target spec.
- [project_lexical_prose_endpoint_and_ve_lexical_phase1](project_lexical_prose_endpoint_and_ve_lexical_phase1.md) — per-term endpoint = story; ve_lexical Phase1 (M63, 3.37.0).
- [project_psalms_narratives_rollout_complete](project_psalms_narratives_rollout_complete.md) — 07-12: Psalms two-narrative rollout COMPLETE 46/46; open = DB-load + cross-term.
- [project_ib_observation_folds_into_ve_lexical](project_ib_observation_folds_into_ve_lexical.md) — ib_observation transitional → ve_lexical items; don't link the stores.
- [project_findings_audit_gate_live](project_findings_audit_gate_live.md) — run findings audit BEFORE capture + essay, M07-on.
- [project_findings_capture_file_as_finding](project_findings_capture_file_as_finding.md) — new findings stored file-as-finding in prose_section.
- [project_cluster_rework_phase_started](project_cluster_rework_phase_started.md) — rework every cluster M01-up; output → Sessions-v2/.
- [project_verse_layer_rollout_before_distill](project_verse_layer_rollout_before_distill.md) — roll verse-meaning through many clusters before distilling.
- [project_iba_value_quality_engine_and_candidate_curate](project_iba_value_quality_engine_and_candidate_curate.md) — 07-21: IBA lib/valuequality.py (cfg_column.expectation) + candidate.curate built; repaired 228 strong_sense.head parser-bug rows.

## Technical / DB

- [project_morph_is_source_of_truth](project_morph_is_source_of_truth.md) — morph_code = linguistic source of truth; stem/language derive.
- [project_measure_layer_persisted](project_measure_layer_persisted.md) — schema 3.34.0/M60; full-verse morphology in DB.
- [reference_strongs_zero_padded_4digit_in_db](reference_strongs_zero_padded_4digit_in_db.md) — DB Strong's zero-padded 4-digit; zfill before comparing.
- [reference_canonical_tier_scheme_is_T0_T7](reference_canonical_tier_scheme_is_T0_T7.md) — canonical tiers = DB T0–T7; T1–T8 doc superseded.
- [reference_file_index_legacy_use_bypass_fks](reference_file_index_legacy_use_bypass_fks.md) — wa_file_index legacy; use bypass FKs, never join through it.
- [reference_term_add_update_authoritative](reference_term_add_update_authoritative.md) — adding/updating a term = the authoritative pipeline doc; new_word DELETED.
- [project_engine_onboard_curate_terms_array](project_engine_onboard_curate_terms_array.md) — onboarding: curate the extract's `terms` ARRAY; --fetch-step.
- [feedback_translit_always_with_gloss](feedback_translit_always_with_gloss.md) — a transliteration never shown without its gloss.
- [feedback_evidence_signal_completeness](feedback_evidence_signal_completeness.md) — judge evidence on term_id + verse_context, not mti_term_id.
- [feedback_enumerate_link_tables_first](feedback_enumerate_link_tables_first.md) — enumerate every junction before calling a record orphaned.
- [feedback_heredoc_only_in_powershell](feedback_heredoc_only_in_powershell.md) — @'…'@ here-strings only in PowerShell tool, not Bash.
- [project_backup_alerting_and_outlook_smtp_block](project_backup_alerting_and_outlook_smtp_block.md) — NAS backups alert on failure; Outlook SMTP blocked, use Gmail.
- [feedback_pre_op_db_snapshots_prune_or_skip](feedback_pre_op_db_snapshots_prune_or_skip.md) — _apply_* snapshot the ~670MB DB; use --no-backup on loops.
- [project_git_remote_silently_blocked_by_large_file](project_git_remote_silently_blocked_by_large_file.md) — >100MB file blocked ALL pushes; purged 07-13; check `git rev-list --count @{u}..HEAD`.

## Orientation / reference

- [reference_core_memory_orientation_map](reference_core_memory_orientation_map.md) — START HERE: docs/project-orientation-core-memory-map.md.
- [project_reconstruction_baseline_20260614](project_reconstruction_baseline_20260614.md) — 06-14 reconstruction = authoritative current-state (01-04).
- [reference_operational_governance_git_backup_manifest](reference_operational_governance_git_backup_manifest.md) — git/backup/manifest operational governance.
- [reference_reusable_scripts_catalogue](reference_reusable_scripts_catalogue.md) — reusable report/extract/process scripts catalogue.
- [reference_study_definition_and_nine_principles](reference_study_definition_and_nine_principles.md) — study definition (Soul Word Analysis Programme; 9 principles).
- [reference_study_end_point_and_milestones](reference_study_end_point_and_milestones.md) — end point: evidenced findings corpus → products.
- [reference_analysis_rules_finding_lifecycle](reference_analysis_rules_finding_lifecycle.md) — finding = universal unit, DB sole record; drafts sifted.
- [feedback_term_is_the_unit_of_movement](feedback_term_is_the_unit_of_movement.md) — the TERM is the unit of movement; work clusters whole.
- [feedback_use_cluster_full_names](feedback_use_cluster_full_names.md) — give the full cluster NAME ("M33 (Peace)").
- [user_profile](user_profile.md) — le Roux Cilliers: researcher, sole authority on scope/methodology.
- [feedback_copilot_frustration](feedback_copilot_frustration.md) — be precise, ask before acting.
- [feedback_working_style](feedback_working_style.md) — investigate first, show evidence, structured docs, wait for approval.

<!-- Demoted 2026-07-21 (files retained/recoverable): reference_iba_live_config_is_db_resident (superseded by project_iba_db_is_master_over_legacy_json_seeds — the *.csv-seed claim is wrong; DB is master, no file is the seed); the "Current method — RESET (characteristics → movements)" section — paused behind the IBA data-layer work (see project_iba_analytic_phase_blocked_on_data_layer_stability): project_RESET_characteristics_to_movements_changeover, project_dimension_d13_cohabitation, project_lexical_rules_reset_process_reframe, feedback_faculty_only_if_explicit_or_inferred_on_verse, feedback_lexical_revelation_test_step3_gate, feedback_expression_vs_characteristic_object_type, feedback_understand_term_in_cluster_not_export, feedback_t2_reference_flag_reclassify, project_t2_flag_are_seats_and_qualifiers; verse/lexical-study-methodology foundational items, same pause: project_focus_points_scripture_as_data_source, project_multi_contributor_spiderweb, project_verse_fanout_operating_model, project_inner_being_reading_questions_first, project_term_is_sense_not_lemma, project_term_driven_genre_aware_lexical_method, project_ve_lexical_is_verse_first, feedback_verse_raw_data_must_pull_all_study_evidence, feedback_term_coverage_cascade_is_index_not_census, feedback_lexical_strictly_verse_bounded_no_implied_evidence, feedback_characteristic_list_validates_not_imputes, feedback_candidate_seed_independent_over_inclusive_control, feedback_verify_contributor_reference_text_first, feedback_verse_meaning_grounded_not_imported, feedback_read_by_passage_not_whole_chapter, feedback_all_study_work_in_db, feedback_no_stats_trends_review_fabricated_data, feedback_test_dimensions_for_reader_drift, project_lexical_rule_validation_failed_build_headless_app, feedback_two_governing_principles, feedback_each_chapter_first_principles_find_the_gems, feedback_multilens_layered_reads_foundation_no_drift, feedback_lens_is_inner_being_process_not_god_relation, feedback_ib_screen_first_god_is_arena, feedback_resist_grouping_preserve_distinctions, feedback_read_completeness_is_verse_level_not_passage_level, feedback_qualifiers_carry_modifying_dimensions, feedback_char_driven_read_not_span_sweep, feedback_name_dimensions_not_just_codes, feedback_inner_being_full_scope. -->
<!-- Demoted 2026-07-13 (files retained/recoverable): project_step_60cap_truncation_and_forwardwalk_fix, project_location_seat_engine_fixed, project_new_word_retirement_blocked, project_pointer_lifecycle_model, project_session_d_moot, project_m10_family_status_primary_logical_units, project_ve_lexical_normalisation_and_groundings, project_superstructure_eisegesis_validation_20260624, project_extended_lexical_model_refinement, project_cluster_review_backlog_and_m12_method_20260624, project_faculty_not_gripped_audit_20260624, project_next_action_audit_surface_verses; + pre-RESET legacy principles (feedback_t1_vs_t2_ontology, feedback_no_rework_paid_twice, project_db_loss_blocker_20260603, etc.) -->
<!-- NOTE: further pre-RESET/legacy memory FILES exist unindexed in this directory (demoted 2026-07-05 and earlier). All are retained and recoverable — list the memory dir to enumerate. -->
