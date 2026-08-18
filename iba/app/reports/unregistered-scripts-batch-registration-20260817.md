# Unregistered scripts -- batch registration (escalation #699)

> 343 scripts registered into `cfg_utility` in one governed batch, under the researcher's aggregate approval on #699 ("register all, mark any not clearly alive inactive") -- not 343 individual `configmaint.propose` round-trips.

**Active (inactive=0): 202**  ·  **Inactive (date-stamped one-off, inactive=1): 141**  ·  **No docstring found, purpose is a placeholder: 5**

## All rows

| module | file_path | inactive | purpose |
|---|---|---|---|
| iba_prototype_build_layers | iba/prototype/build_layers.py | 0 | build_layers.py — the STEP pull as SEARCH LAYERS, one table per layer. |
| iba_prototype_build_prototype | iba/prototype/build_prototype.py | 0 | build_prototype.py — test the term -> sense -> span model against real STEP data. |
| iba_prototype_export_md | iba/prototype/export_md.py | 0 | export_md.py — render the prototype's JSON "tables" as markdown for review. |
| iba_prototype_inspect_verse | iba/prototype/inspect_verse.py | 0 | inspect_verse.py — select a verse; watch the backtrack; see what emerges. |
| iba_scripts_build_dbschema | iba/scripts/build_dbschema.py | 0 | build_dbschema.py -- capture a database's schema into its DBSchema register. |
| iba_scripts_cfg_apply | iba/scripts/cfg_apply.py | 0 | cfg_apply.py — the configurator-maintenance utility's WRITE PATH. |
| iba_scripts_cfg_helper | iba/scripts/cfg_helper.py | 0 | cfg_helper.py -- export each config json to a configuration component helper (.md). |
| iba_scripts_cfg_kernel | iba/scripts/cfg_kernel.py | 0 | cfg_kernel.py — the envelope-validator KERNEL for the IBA configurator. |
| iba_scripts_probe_step_api | iba/scripts/probe_step_api.py | 0 | probe_step_api.py — dump the FULL raw response of each STEP API, unmodified. |
| query_db | query_db.py | 0 | prose_section_type joined to active current prose_section rows |
| research_VE_lexical_faculty_map_build_build_batch4 | research/VE-lexical/faculty-map-build/_build_batch4.py | 0 | -*- coding: utf-8 -*- |
| research_VE_lexical_faculty_map_build_classify_batch1 | research/VE-lexical/faculty-map-build/_classify_batch1.py | 0 | Faculty classification for inventory slice 0..343. Decisions grounded in gloss+senses, original-language aware. |
| scripts_apply_add_role_to_master_index_v1_20260707 | scripts/_apply_add_role_to_master_index_v1_20260707.py | 1 | _apply_add_role_to_master_index_v1_20260707.py — M64: add per-span `role` to the master index |
| scripts_apply_backfill_chapter_verses_v1_20260702 | scripts/_apply_backfill_chapter_verses_v1_20260702.py | 1 | _apply_backfill_chapter_verses_v1_20260702.py |
| scripts_apply_backfill_verse_id_active_20260701 | scripts/_apply_backfill_verse_id_active_20260701.py | 1 | _apply_backfill_verse_id_active_20260701.py |
| scripts_apply_build_ib_char_index_v1_20260711 | scripts/_apply_build_ib_char_index_v1_20260711.py | 1 | (c) Build ib_characteristic into the normalised characteristic index, from the sources |
| scripts_apply_cause_from_api | scripts/_apply_cause_from_api.py | 0 | _apply_cause_from_api.py (2026-06-16) — apply the cause-resolution API output back into ve_lexical. |
| scripts_apply_charfix_master_v1_20260711 | scripts/_apply_charfix_master_v1_20260711.py | 1 | Fix (a) the emergent-characteristic seed failure + (b) populate the char on the master. |
| scripts_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701 | scripts/_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py | 1 | _apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py |
| scripts_apply_cluster_schema_v1_20260505 | scripts/_apply_cluster_schema_v1_20260505.py | 1 | _apply_cluster_schema_v1_20260505.py — DB-modifying. |
| scripts_apply_comment_findings_v1_20260602 | scripts/_apply_comment_findings_v1_20260602.py | 1 | Applier for COMMENT_EVALUATION outcomes (per cluster). |
| scripts_apply_create_and_populate_passages_20260701 | scripts/_apply_create_and_populate_passages_20260701.py | 1 | _apply_create_and_populate_passages_20260701.py |
| scripts_apply_create_constitution_cluster | scripts/_apply_create_constitution_cluster.py | 0 | _apply_create_constitution_cluster.py — WRITES. Creates the new M47 'Constitution' cluster (the inner-being |
| scripts_apply_create_vc_for_onboarded | scripts/_apply_create_vc_for_onboarded.py | 0 | Create verse_context units for engine-onboarded terms (post-onboard catch-up step). |
| scripts_apply_d6_capture_contributor_source | scripts/_apply_d6_capture_contributor_source.py | 0 | D6 — capture a contributor source (Logos / AI-Chat) into prose_section, strip it |
| scripts_apply_descriptions_patch | scripts/_apply_descriptions_patch.py | 0 | (no module docstring or leading comment found -- needs a manual purpose write-up) |
| scripts_apply_dq01_locus_coupling_swap_v1_20260714 | scripts/_apply_dq01_locus_coupling_swap_v1_20260714.py | 1 | DQ-01 source fix: un-transpose coupling(112) <-> locus(116) for Psalms read-2026 (v1, 2026-07-14). |
| scripts_apply_drop_code_softdelete | scripts/_apply_drop_code_softdelete.py | 0 | _apply_drop_code_softdelete.py — MODIFIES DB. Soft-delete every finding referencing the §3 DROP tier codes |
| scripts_apply_excluded_registry_cascade | scripts/_apply_excluded_registry_cascade.py | 0 | _apply_excluded_registry_cascade.py — D1 rule (2026-06-15): when a registry is phase1_status='Excluded', |
| scripts_apply_extend_characteristic_baseline_v1_20260703 | scripts/_apply_extend_characteristic_baseline_v1_20260703.py | 1 | Extend the `characteristic` baseline (199 rows, 17 clusters) to the Ps/Pro-raised |
| scripts_apply_faculty_map_rederive_20260624 | scripts/_apply_faculty_map_rederive_20260624.py | 1 | Re-found FACULTY on a curated Strong's-lemma->faculty MAP (P2-compliant, replacing |
| scripts_apply_faculty_rederive_v1 | scripts/_apply_faculty_rederive_v1.py | 0 | _apply_faculty_rederive_v1.py (2026-06-15) — re-derive VE7 (faculty) against the actual faculty |
| scripts_apply_field_from_api | scripts/_apply_field_from_api.py | 0 | _apply_field_from_api.py (2026-06-16) — apply a field read API output back into ve_lexical. |
| scripts_apply_file_chapter_lexical_prose_v1_20260702 | scripts/_apply_file_chapter_lexical_prose_v1_20260702.py | 1 | _apply_file_chapter_lexical_prose_v1_20260702.py |
| scripts_apply_file_passage_lexical_prose_v1_20260704 | scripts/_apply_file_passage_lexical_prose_v1_20260704.py | 1 | _apply_file_passage_lexical_prose_v1_20260704.py |
| scripts_apply_file_ruthlessness_lexical_prose_20260702 | scripts/_apply_file_ruthlessness_lexical_prose_20260702.py | 1 | _apply_file_ruthlessness_lexical_prose_20260702.py |
| scripts_apply_file_synthesis_prose_v1_20260703 | scripts/_apply_file_synthesis_prose_v1_20260703.py | 1 | File a cross-chapter SYNTHESIS document as a DB-canonical prose_section |
| scripts_apply_fix_8_mti_mismatches_percase_20260701 | scripts/_apply_fix_8_mti_mismatches_percase_20260701.py | 1 | _apply_fix_8_mti_mismatches_percase_20260701.py |
| scripts_apply_fix_verse_context_mti_mismatch_20260701 | scripts/_apply_fix_verse_context_mti_mismatch_20260701.py | 1 | _apply_fix_verse_context_mti_mismatch_20260701.py |
| scripts_apply_flag_empty_to_t2 | scripts/_apply_flag_empty_to_t2.py | 0 | _apply_flag_empty_to_t2.py — empties FLAG: every remaining FLAG term -> T2 (the catch-all reference bucket; |
| scripts_apply_flag_triage_moves | scripts/_apply_flag_triage_moves.py | 0 | _apply_flag_triage_moves.py — classify FLAG terms by gloss and move the confident ones: clear characteristic |
| scripts_apply_gate1_term_onboard_v1_20260705 | scripts/_apply_gate1_term_onboard_v1_20260705.py | 1 | *** RETIRED 2026-07-12 (researcher direction). DO NOT USE. *** |
| scripts_apply_generate_collection_lexical_20260624 | scripts/_apply_generate_collection_lexical_20260624.py | 1 | Collection-lexical GENERATOR (01b Part C, the term-scope layer). |
| scripts_apply_generate_ve_lexical_v2 | scripts/_apply_generate_ve_lexical_v2.py | 0 | _apply_generate_ve_lexical_v2.py (2026-06-16) — generate the v2 verse-lexical for ALL analysed |
| scripts_apply_generic_characteristic_backfill_20260527 | scripts/_apply_generic_characteristic_backfill_20260527.py | 1 | Generic 1:1 characteristic backfill for pre-v2_6 closed clusters. |
| scripts_apply_ib_char_cluster_assign_v1_20260711 | scripts/_apply_ib_char_cluster_assign_v1_20260711.py | 1 | Assign each ib_characteristic record (Psalms) to a CLUSTER based on its term. |
| scripts_apply_ib_char_cluster_assign_v2_20260711 | scripts/_apply_ib_char_cluster_assign_v2_20260711.py | 1 | Assign CLUSTER via the deterministic chain: master -> its 1 mti_term -> its 1 |
| scripts_apply_ib_char_family_grouping_v1_20260711 | scripts/_apply_ib_char_family_grouping_v1_20260711.py | 1 | Group meaning-records (ib_characteristic, a given book_scope) into <=50 semantic |
| scripts_apply_ingest_verse_morphology | scripts/_apply_ingest_verse_morphology.py | 0 | _apply_ingest_verse_morphology.py (2026-06-16) — populate the persisted MEASURE LAYER (M60). |
| scripts_apply_l2_rollup | scripts/_apply_l2_rollup.py | 0 | _apply_l2_rollup.py — roll the VERSE-level L2 findings up to CLUSTER-level findings (the "characteristic = |
| scripts_apply_l2_write | scripts/_apply_l2_write.py | 0 | _apply_l2_write.py — the L2 WRITER (verse-complete). Enters by --cluster (the verses that contain a |
| scripts_apply_l2_write_refit | scripts/_apply_l2_write_refit.py | 0 | _apply_l2_write_refit.py — L2 writer on the REFIT basis (wa-catalogue-refit-two-layer / verse-extraction |
| scripts_apply_language_reconcile | scripts/_apply_language_reconcile.py | 0 | _apply_language_reconcile.py — make mti_terms.language / wa_term_inventory.language |
| scripts_apply_lev_study_v1_20260705 | scripts/_apply_lev_study_v1_20260705.py | 1 | _apply_lev_study_v1_20260705.py  — Leviticus terminology study loader (corpus-native). |
| scripts_apply_link_mti_term_id | scripts/_apply_link_mti_term_id.py | 0 | _apply_link_mti_term_id.py — D2a (2026-06-15): populate the missing wa_verse_records.mti_term_id link |
| scripts_apply_load_segmentation_v1_20260703 | scripts/_apply_load_segmentation_v1_20260703.py | 1 | Load an inner-being SEGMENTATION (units) into the generic segment store. |
| scripts_apply_locus_dimension_v1_20260704 | scripts/_apply_locus_dimension_v1_20260704.py | 1 | Derive a LOCUS dimension (ve_nr 116) on target/bearer spans: IB-internal vs external. |
| scripts_apply_m03_characteristic_backfill_20260527 | scripts/_apply_m03_characteristic_backfill_20260527.py | 1 | M03 characteristic backfill (test cluster for pre-v2_6 characteristic retrofit). |
| scripts_apply_m03_findings_capture_20260620 | scripts/_apply_m03_findings_capture_20260620.py | 1 | _apply_m03_findings_capture_20260620.py — capture M03 (Grief) findings, in line with M02. |
| scripts_apply_master_index_backfill_v1_20260706 | scripts/_apply_master_index_backfill_v1_20260706.py | 1 | Master-index -> wa_verse_records backfill (per book). |
| scripts_apply_merge_m10bc_into_m10_20260623 | scripts/_apply_merge_m10bc_into_m10_20260623.py | 1 | Merge M10b + M10c into M10 (researcher decision 2026-06-23): the three-way split |
| scripts_apply_migrate_sb_findings | scripts/_apply_migrate_sb_findings.py | 0 | _apply_migrate_sb_findings.py — migrate Session B findings (wa_session_b_findings) into the universal |
| scripts_apply_migrate_ve_findings_to_lexical | scripts/_apply_migrate_ve_findings_to_lexical.py | 0 | _apply_migrate_ve_findings_to_lexical.py (2026-06-15) — retrofit the VE field-value findings OUT of |
| scripts_apply_morph_backfill | scripts/_apply_morph_backfill.py | 0 | _apply_morph_backfill.py — L0 of the L1 sweep. Populates wa_verse_records.morph_code / stem from STEP |
| scripts_apply_mti_dedup_active_duplicates_v1_20260713 | scripts/_apply_mti_dedup_active_duplicates_v1_20260713.py | 1 | Isolate duplicate ACTIVE mti_terms rows — one active row per Strong's (OT-DBR-009). |
| scripts_apply_passage_build_v2_20260713 | scripts/_apply_passage_build_v2_20260713.py | 1 | Passage build v2 — candidate-driven, per book (Stage 0 of the cycle). |
| scripts_apply_passage_completeness_v1_20260707 | scripts/_apply_passage_completeness_v1_20260707.py | 1 | Passage completeness (reading-unit repair) — per book, reusable. |
| scripts_apply_passage_process_markers_v1_20260701 | scripts/_apply_passage_process_markers_v1_20260701.py | 1 | _apply_passage_process_markers_v1_20260701.py |
| scripts_apply_persist_narration_finding_v1 | scripts/_apply_persist_narration_finding_v1.py | 0 | _apply_persist_narration_finding_v1.py (2026-06-15) — persist the templated narration as the single |
| scripts_apply_phase2_flags_patch | scripts/_apply_phase2_flags_patch.py | 0 | Apply phase2-flag-reassessment-20260319-v1.json |
| scripts_apply_poetic_chapter_lexical_v1_20260702 | scripts/_apply_poetic_chapter_lexical_v1_20260702.py | 1 | _apply_poetic_chapter_lexical_v1_20260702.py |
| scripts_apply_prose_programme_chapter01 | scripts/_apply_prose_programme_chapter01.py | 0 | _apply_prose_programme_chapter01.py |
| scripts_apply_psalm_role_reassess_v1_20260706 | scripts/_apply_psalm_role_reassess_v1_20260706.py | 1 | _apply_psalm_role_reassess_v1_20260706.py — Step 2: re-assess the role dimension for a psalm. |
| scripts_apply_psalms_gate1_completeness_v1_20260706 | scripts/_apply_psalms_gate1_completeness_v1_20260706.py | 1 | _apply_psalms_gate1_completeness_v1_20260706.py — Step (d) Gate-1 completeness for PSALMS. |
| scripts_apply_psalms_gate1_reactivate_v1_20260706 | scripts/_apply_psalms_gate1_reactivate_v1_20260706.py | 1 | _apply_psalms_gate1_reactivate_v1_20260706.py — finish Step (d) for Psalms. |
| scripts_apply_psalms_linkage_fix_v1_20260706 | scripts/_apply_psalms_linkage_fix_v1_20260706.py | 1 | _apply_psalms_linkage_fix_v1_20260706.py — Step 1 (linkages) for PSALMS only. |
| scripts_apply_rebuild_ib_char_meaning_keyed_v3_20260711 | scripts/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py | 1 | (v3) Rebuild ib_characteristic keyed on MEANING-IN-CONTEXT, not base lemma. |
| scripts_apply_rebuild_passages_consecutive_v2_20260701 | scripts/_apply_rebuild_passages_consecutive_v2_20260701.py | 1 | _apply_rebuild_passages_consecutive_v2_20260701.py |
| scripts_apply_recode_sessionb_m10_findings_20260623 | scripts/_apply_recode_sessionb_m10_findings_20260623.py | 1 | Recode mis-migrated session_b CLUSTER-level findings off M10 to their correct |
| scripts_apply_registry_metadata_patch | scripts/_apply_registry_metadata_patch.py | 0 | _apply_registry_metadata_patch.py |
| scripts_apply_reread_lexical_v1_20260709 | scripts/_apply_reread_lexical_v1_20260709.py | 1 | Apply a char-driven re-read lexical JSON to ve_lexical. REUSABLE per chapter/book. |
| scripts_apply_reread_roles_from_velexical_v1_20260709 | scripts/_apply_reread_roles_from_velexical_v1_20260709.py | 1 | _apply_reread_roles_from_velexical_v1_20260709.py |
| scripts_apply_reset_l2_meaning_flags | scripts/_apply_reset_l2_meaning_flags.py | 0 | _apply_reset_l2_meaning_flags.py — WRITES. Recomputes finding.flagged_for_review for ALL l2_meaning |
| scripts_apply_retrofit_dims_v1_20260714 | scripts/_apply_retrofit_dims_v1_20260714.py | 1 | Retrofit-authoring apply for the new/reinstated dimensions (v1, 2026-07-14). |
| scripts_apply_role_reassess_v1_20260707 | scripts/_apply_role_reassess_v1_20260707.py | 1 | _apply_role_reassess_v1_20260707.py — Step (c) role reassessment, generalised per book. |
| scripts_apply_ruthlessness_sanitycheck_rerun_v4_20260702 | scripts/_apply_ruthlessness_sanitycheck_rerun_v4_20260702.py | 1 | _apply_ruthlessness_sanitycheck_rerun_v4_20260702.py |
| scripts_apply_schema_ve_pairmodel_genre_v1_20260702 | scripts/_apply_schema_ve_pairmodel_genre_v1_20260702.py | 1 | _apply_schema_ve_pairmodel_genre_v1_20260702.py |
| scripts_apply_seed_ib_characteristic_registry_v1_20260703 | scripts/_apply_seed_ib_characteristic_registry_v1_20260703.py | 1 | Create + seed the inner-being CHARACTERISTIC control registry (ib_characteristic). |
| scripts_apply_sense_from_subgloss | scripts/_apply_sense_from_subgloss.py | 0 | _apply_sense_from_subgloss.py (2026-06-15) — set VE1 (sense) in ve_lexical to the PER-OCCURRENCE STEP |
| scripts_apply_softdelete_excluded_empty_terms | scripts/_apply_softdelete_excluded_empty_terms.py | 0 | _apply_softdelete_excluded_empty_terms.py (2026-06-15) — ground the canonical term list: |
| scripts_apply_softdelete_orphan_verses | scripts/_apply_softdelete_orphan_verses.py | 0 | _apply_softdelete_orphan_verses.py — D2b option A (2026-06-15): soft-delete ACTIVE verses that are |
| scripts_apply_stamp_char_candidate_on_master_v1_20260708 | scripts/_apply_stamp_char_candidate_on_master_v1_20260708.py | 1 | _apply_stamp_char_candidate_on_master_v1_20260708.py — M65: stamp the candidate-characteristic |
| scripts_apply_stem_patch | scripts/_apply_stem_patch.py | 0 | Apply stem-extraction-patch-20260319-v1.json |
| scripts_apply_supersede_old_mechanical | scripts/_apply_supersede_old_mechanical.py | 0 | _apply_supersede_old_mechanical.py — WRITES (reversible soft-delete). Supersedes the old l2_mechanical |
| scripts_apply_t2_soft_delete | scripts/_apply_t2_soft_delete.py | 0 | _apply_t2_soft_delete.py — soft-delete Parked (T2) terms that NEVER co-occur with a characteristic. |
| scripts_apply_term_decisions | scripts/_apply_term_decisions.py | 0 | _apply_term_decisions.py |
| scripts_apply_term_driven_lexical_ruthlessness_v7_20260702 | scripts/_apply_term_driven_lexical_ruthlessness_v7_20260702.py | 1 | _apply_term_driven_lexical_ruthlessness_v7_20260702.py |
| scripts_apply_ve_lexical_phase1_archive_legacy_20260702 | scripts/_apply_ve_lexical_phase1_archive_legacy_20260702.py | 1 | _apply_ve_lexical_phase1_archive_legacy_20260702.py  (M63, schema -> 3.37.0) |
| scripts_apply_ve_lexical_span_keyable_v1_20260702 | scripts/_apply_ve_lexical_span_keyable_v1_20260702.py | 1 | _apply_ve_lexical_span_keyable_v1_20260702.py |
| scripts_apply_ve_rebuild_mechanical_v1 | scripts/_apply_ve_rebuild_mechanical_v1.py | 0 | _apply_ve_rebuild_mechanical_v1.py (2026-06-15) — mechanical rebuild of ve_lexical fields |
| scripts_apply_verse_read_meaning | scripts/_apply_verse_read_meaning.py | 0 | _apply_verse_read_meaning.py — L2 VERSE-READ = MEANING pipeline (verse-complete, term-driven). |
| scripts_apply_verse_record_link_repair_all_ot_v1_20260708 | scripts/_apply_verse_record_link_repair_all_ot_v1_20260708.py | 1 | Verse-record -> verse / master-index link repair, WHOLE OT in one pass. |
| scripts_apply_verse_record_link_repair_v1_20260707 | scripts/_apply_verse_record_link_repair_v1_20260707.py | 1 | Verse-record -> verse / master-index link repair (per book, reusable). |
| scripts_apply_verse_record_structural_backfill_v1_20260705 | scripts/_apply_verse_record_structural_backfill_v1_20260705.py | 1 | _apply_verse_record_structural_backfill_v1_20260705.py — safe, determinate structural backfill. |
| scripts_apply_verse_record_traceability_v1_20260704 | scripts/_apply_verse_record_traceability_v1_20260704.py | 1 | Add analysis-traceability columns to wa_verse_records (the primary control table). |
| scripts_apply_verse_uniqueness_cleanup | scripts/_apply_verse_uniqueness_cleanup.py | 0 | _apply_verse_uniqueness_cleanup.py (2026-06-15) — move wa_verse_records toward "one active row per |
| scripts_apply_vr_link_targetword_and_flag_v1_20260708 | scripts/_apply_vr_link_targetword_and_flag_v1_20260708.py | 1 | Second-pass verse-record link repair for the multi-span (ambiguous) OT residual. |
| scripts_apply_wipe_ve_lexical_v1 | scripts/_apply_wipe_ve_lexical_v1.py | 0 | _apply_wipe_ve_lexical_v1.py (2026-06-15) — PERMANENTLY remove all rows from ve_lexical. |
| scripts_apply_write_ruthlessness_index_driven_v3_20260702 | scripts/_apply_write_ruthlessness_index_driven_v3_20260702.py | 1 | _apply_write_ruthlessness_index_driven_v3_20260702.py |
| scripts_apply_write_ruthlessness_lexical_v1_20260702 | scripts/_apply_write_ruthlessness_lexical_v1_20260702.py | 1 | _apply_write_ruthlessness_lexical_v1_20260702.py |
| scripts_apply_write_ruthlessness_passages_full_v2_20260702 | scripts/_apply_write_ruthlessness_passages_full_v2_20260702.py | 1 | _apply_write_ruthlessness_passages_full_v2_20260702.py |
| scripts_assess_cluster_profiles | scripts/_assess_cluster_profiles.py | 0 | _assess_cluster_profiles.py — READ-ONLY. Per-cluster L1 profile correlated to the co-occurrence matrix: |
| scripts_assess_cluster_v3_2_preeval | scripts/_assess_cluster_v3_2_preeval.py | 0 | _assess_cluster_v3_2_preeval.py  — READ-ONLY V3_2 cluster pre-evaluation. |
| scripts_assess_corpus_keyword_map | scripts/_assess_corpus_keyword_map.py | 0 | _assess_corpus_keyword_map.py — READ-ONLY. Corpus-wide PRELIMINARY keyword allocation: runs the validated |
| scripts_assess_corpus_keyword_typed | scripts/_assess_corpus_keyword_typed.py | 0 | _assess_corpus_keyword_typed.py — READ-ONLY. Corpus keyword map v2: each term gets its THING-TYPE |
| scripts_assess_cross_cluster_cooccurrence | scripts/_assess_cross_cluster_cooccurrence.py | 0 | _assess_cross_cluster_cooccurrence.py — READ-ONLY. The cross-cluster co-occurrence matrix: which |
| scripts_assess_keyword_corpus_report | scripts/_assess_keyword_corpus_report.py | 0 | _assess_keyword_corpus_report.py — READ-ONLY. Directional assessment of the corpus-wide keyword |
| scripts_assess_keyword_overlap | scripts/_assess_keyword_overlap.py | 0 | _assess_keyword_overlap.py — READ-ONLY. Cluster-level keyword overlap (angle 5). Builds each cluster's |
| scripts_assess_l2_findings_view | scripts/_assess_l2_findings_view.py | 0 | _assess_l2_findings_view.py — READ-ONLY. For each requested cluster, shows the L1 + L2 results per verse: |
| scripts_assess_l2_triage | scripts/_assess_l2_triage.py | 0 | _assess_l2_triage.py — READ-ONLY. Runs the L2 MECHANICAL pass + ADEQUACY TRIAGE on every verse of a term: |
| scripts_assess_link_correlation | scripts/_assess_link_correlation.py | 0 | _assess_link_correlation.py — READ-ONLY. The correlated roll-up: ties angle 1 (co-occurrence = CONTEXTUAL |
| scripts_assess_meaning_tables | scripts/_assess_meaning_tables.py | 0 | _assess_meaning_tables.py |
| scripts_assess_mti_duplicate_terms | scripts/_assess_mti_duplicate_terms.py | 0 | _assess_mti_duplicate_terms.py — READ-ONLY. Re-surfaces OT-DBR-009 (mti_terms duplication) from the |
| scripts_assess_p2_verse_scenarios | scripts/_assess_p2_verse_scenarios.py | 0 | _assess_p2_verse_scenarios.py — READ-ONLY. Types every verse of a cluster into the L2 decision-scenario |
| scripts_assess_pipeline_integrity_v1_20260704 | scripts/_assess_pipeline_integrity_v1_20260704.py | 1 | Read-only PIPELINE-INTEGRITY diagnostic for the verse-analysis (inner-being lexical) chain. |
| scripts_assess_qa_method_effectiveness | scripts/_assess_qa_method_effectiveness.py | 0 | _assess_qa_method_effectiveness.py — read-only Q&A coverage extraction. |
| scripts_assess_qa_method_quality_review | scripts/_assess_qa_method_quality_review.py | 0 | _assess_qa_method_quality_review.py — qualitative-review-oriented Q&A coverage. |
| scripts_assess_read_dedup | scripts/_assess_read_dedup.py | 0 | _assess_read_dedup.py — READ-ONLY. Estimates how much the (expensive) read layer would DUPLICATE across |
| scripts_assess_registry_grounding | scripts/_assess_registry_grounding.py | 0 | _assess_registry_grounding.py — READ-ONLY. Tests the researcher's expectation: does every registry (anchor) |
| scripts_assess_registry_vs_keywords | scripts/_assess_registry_vs_keywords.py | 0 | _assess_registry_vs_keywords.py — READ-ONLY. Diagnoses WHY some of the 214 registry (anchor) words are |
| scripts_assess_relationship_probe | scripts/_assess_relationship_probe.py | 0 | _assess_relationship_probe.py — READ-ONLY. For a cluster PAIR, pull the verses where both co-occur and |
| scripts_assess_shared_forms | scripts/_assess_shared_forms.py | 0 | _assess_shared_forms.py — READ-ONLY. Shared-form / homonym index: transliterations whose terms are |
| scripts_assess_study_state | scripts/_assess_study_state.py | 0 | Read-only: render the live state of the verse-lexical study to ONE page (verse-analysis/_STATE.md). |
| scripts_assess_t2_cleanup | scripts/_assess_t2_cleanup.py | 0 | _assess_t2_cleanup.py  — READ-ONLY. Proposes a disposition for every Parked (T2) cluster term. |
| scripts_assess_t2_relevance_surface | scripts/_assess_t2_relevance_surface.py | 0 | _assess_t2_relevance_surface.py  — READ-ONLY. |
| scripts_assess_termsense_ranking | scripts/_assess_termsense_ranking.py | 0 | _assess_termsense_ranking.py — READ-ONLY. Reasonability check on the read-dedup: ranks every (term, sense) |
| scripts_assess_verse_assembly | scripts/_assess_verse_assembly.py | 0 | _assess_verse_assembly.py — READ-ONLY. L1 establishment per verse for a cluster: assembles each verse's |
| scripts_assess_verse_corroboration | scripts/_assess_verse_corroboration.py | 0 | _assess_verse_corroboration.py  — READ-ONLY (A1 verse-meaning corroboration scan). |
| scripts_assess_verse_raw_data | scripts/_assess_verse_raw_data.py | 0 | Read-only: assemble the FULL raw study evidence for a verse -> markdown. |
| scripts_audit_cluster_against_instruction_v25_v1_20260518 | scripts/_audit_cluster_against_instruction_v25_v1_20260518.py | 1 | Audit a cluster against v2_5 instruction compliance. |
| scripts_audit_findings_v1_20260621 | scripts/_audit_findings_v1_20260621.py | 1 | _audit_findings_v1_20260621.py — read-only findings audit (wa-findings-audit-spec-v1_0). |
| scripts_audit_gate1_additions_v1_20260706 | scripts/_audit_gate1_additions_v1_20260706.py | 1 | Gate-1 onboarding audit — pre/post accountability for the orphan-term additions. |
| scripts_audit_step_extract_archiving | scripts/_audit_step_extract_archiving.py | 0 | Auditor + applicator for STEP Extracts archiving. |
| scripts_backfill_span_match | scripts/_backfill_span_match.py | 0 | _backfill_span_match.py |
| scripts_batch_audit | scripts/_batch_audit.py | 0 | _batch_audit.py — Run audit_word on all registries that need it. |
| scripts_batch_extract | scripts/_batch_extract.py | 0 | _batch_extract.py — Run STEP extraction for all words that need a discovery JSON. |
| scripts_build_M01_verse_read_review | scripts/_build_M01_verse_read_review.py | 0 | _build_M01_verse_read_review.py — READ-ONLY. Full M01 verse-complete run review: coverage, cross-cluster |
| scripts_build_cluster_verse_read_gate | scripts/_build_cluster_verse_read_gate.py | 0 | _build_cluster_verse_read_gate.py — READ-ONLY. The standard PER-CLUSTER GATE report produced as each |
| scripts_build_gate1_registry_final_map_v1_20260706 | scripts/_build_gate1_registry_final_map_v1_20260706.py | 1 | Read-only: render the FINAL single-home-per-term registry mapping for the 97 gate1 orphans, |
| scripts_build_m04_characteristic_phase9_bundle_20260519 | scripts/_build_m04_characteristic_phase9_bundle_20260519.py | 1 | Build a multi-characteristic Phase 9 AI package (bundle). |
| scripts_build_m04_characteristic_phase9_package_20260518 | scripts/_build_m04_characteristic_phase9_package_20260518.py | 1 | Build a per-characteristic Phase 9 AI package for M04. |
| scripts_build_m08_characteristic_phase9_bundle_20260521 | scripts/_build_m08_characteristic_phase9_bundle_20260521.py | 1 | Build a multi-characteristic Phase 9 AI package (bundle). |
| scripts_build_m08_characteristic_phase9_package_20260521 | scripts/_build_m08_characteristic_phase9_package_20260521.py | 1 | Build a per-characteristic Phase 9 AI package for M08. |
| scripts_build_m10_unit_verse_evidence_20260623 | scripts/_build_m10_unit_verse_evidence_20260623.py | 1 | Emit the PER-VERSE structured evidence section for an M10 unit, from the on-disk |
| scripts_build_projection_v2_20260714 | scripts/_build_projection_v2_20260714.py | 1 | Build the flattened reading projection + technical data layer for a re-read book (v2, 2026-07-14). |
| scripts_build_ps119 | scripts/_build_ps119.py | 0 | Persistent char-by-char builder for Ps 119 (641 candidates, 176 verses). |
| scripts_build_t2_flag_sample | scripts/_build_t2_flag_sample.py | 0 | _build_t2_flag_sample.py — READ-ONLY. Shows real verses + meaning paragraphs from the T2 and FLAG buckets, |
| scripts_build_term_verse_findings_report | scripts/_build_term_verse_findings_report.py | 0 | _build_term_verse_findings_report.py — READ-ONLY. For N terms, show up to K verses each with the verse |
| scripts_build_vc_batch | scripts/_build_vc_batch.py | 0 | _build_vc_batch.py |
| scripts_build_vc_revision_ledger | scripts/_build_vc_revision_ledger.py | 0 | Build the VC revision ledger from VCB-7..11 patches. |
| scripts_build_verse_read_pilot_review | scripts/_build_verse_read_pilot_review.py | 0 | _build_verse_read_pilot_review.py — READ-ONLY. Assembles the M01 verse-read pilot review: |
| scripts_cc_verse_read | scripts/_cc_verse_read.py | 0 | _cc_verse_read.py — CC-GENERATION mode of the verse-read = meaning layer. Same output as the API pipeline |
| scripts_check_book_lexical_readiness_v1_20260712 | scripts/_check_book_lexical_readiness_v1_20260712.py | 1 | Book lexical-rework READINESS assessment (read-only). |
| scripts_check_dimension_band_drift_v1_20260714 | scripts/_check_dimension_band_drift_v1_20260714.py | 1 | Reader-drift diagnostic for every ve dimension (v1, 2026-07-14). |
| scripts_check_doc_versions | scripts/_check_doc_versions.py | 0 | GR-FILE-003 compliance check for instruction documents. |
| scripts_check_family_narratives_20260712 | scripts/_check_family_narratives_20260712.py | 1 | Verify a family's narrative JSON against its base source WORK_CONTRACT. |
| scripts_check_fi_ti_chain | scripts/_check_fi_ti_chain.py | 0 | 1. wa_term_inventory rows with no parent in wa_file_index (orphaned terms) |
| scripts_check_ib_char_i7_v1_20260714 | scripts/_check_ib_char_i7_v1_20260714.py | 1 | Cheap I7 check (v1, 2026-07-14) — read-2026 characteristics with NO ib_char link. |
| scripts_check_integrity_controls | scripts/_check_integrity_controls.py | 0 | _check_integrity_controls.py (2026-06-28) — DB integrity anchor for the term-orphan build (READ-ONLY). |
| scripts_check_lexical_content_validity_v1_20260714 | scripts/_check_lexical_content_validity_v1_20260714.py | 1 | CONTENT-VALIDITY gate for a re-read book (v1, 2026-07-14). |
| scripts_check_m10_cross_cluster_bonds_20260623 | scripts/_check_m10_cross_cluster_bonds_20260623.py | 1 | Cross-cluster BONDS for the M10-family logical units (read-only). |
| scripts_check_mti_terms | scripts/_check_mti_terms.py | 0 | Consistency check for mti_terms table. |
| scripts_check_passage_reading_coverage_v1_20260704 | scripts/_check_passage_reading_coverage_v1_20260704.py | 1 | _check_passage_reading_coverage_v1_20260704.py |
| scripts_check_psalms_reread_progress_v1_20260709 | scripts/_check_psalms_reread_progress_v1_20260709.py | 1 | Psalms re-read progress monitor — READ-ONLY. Run anytime to see how far the re-read has got. |
| scripts_check_reread_conformance_v1_20260714 | scripts/_check_reread_conformance_v1_20260714.py | 1 | Reusable per-cycle re-read conformance check (v1, 2026-07-14). |
| scripts_check_reread_measures_v3_20260709 | scripts/_check_reread_measures_v3_20260709.py | 1 | Re-read success measures (G0-G10) — READ-ONLY, BOOK-GENERAL. v3 (2026-07-09). |
| scripts_check_softdelete_integrity | scripts/_check_softdelete_integrity.py | 0 | _check_softdelete_integrity.py — H5 (2026-06-15): the standing soft-delete integrity check, and the |
| scripts_check_ve_seat_completeness | scripts/_check_ve_seat_completeness.py | 0 | _check_ve_seat_completeness.py — standing guard: is the location SEAT vocabulary complete? |
| scripts_check_ve_signal_lists | scripts/_check_ve_signal_lists.py | 0 | _check_ve_signal_lists.py — completeness audit of EVERY seed/signal list in the VE engine. |
| scripts_db_introspect | scripts/_db_introspect.py | 0 | Temporary introspection script — outputs JSON for report generation. |
| scripts_delete_empty_fi | scripts/_delete_empty_fi.py | 0 | fi.id rows to KEEP (backlog words with strongs_list, awaiting new-word import) |
| scripts_derive_retrofit_dims_v1_20260714 | scripts/_derive_retrofit_dims_v1_20260714.py | 1 | Derive the 5 retrofit dims (intensity/specifier/effect/device/direction) for read-2026 chars, |
| scripts_discover_word_terms | scripts/_discover_word_terms.py | 0 | _discover_word_terms.py |
| scripts_exploratory_brief_meaning_router_v1_20260504 | scripts/_exploratory_brief_meaning_router_v1_20260504.py | 1 | _exploratory_brief_meaning_router_v1_20260504.py — read-only. |
| scripts_exploratory_brief_verse_router_v1_20260504 | scripts/_exploratory_brief_verse_router_v1_20260504.py | 1 | _exploratory_brief_verse_router_v1_20260504.py — read-only. |
| scripts_exploratory_unclassified_verse_sample_v1_20260504 | scripts/_exploratory_unclassified_verse_sample_v1_20260504.py | 1 | _exploratory_unclassified_verse_sample_v1_20260504.py — read-only. |
| scripts_explore_cluster_timing | scripts/_explore_cluster_timing.py | 0 | _explore_cluster_timing.py — READ-ONLY timing analysis of completed L2 verse-read clusters. |
| scripts_explore_drop_code_findings | scripts/_explore_drop_code_findings.py | 0 | _explore_drop_code_findings.py — READ-ONLY extract of every finding referencing the §3 DROP tier codes. |
| scripts_explore_m_vs_r_divergence | scripts/_explore_m_vs_r_divergence.py | 0 | _explore_m_vs_r_divergence.py — READ-ONLY. For VE-01 (obs 395), compare the MECHANICAL term-gloss (M) |
| scripts_explore_tier_findings | scripts/_explore_tier_findings.py | 0 | _explore_tier_findings.py — READ-ONLY explorer/export for the L2 verse-read tier findings. |
| scripts_explore_ve_by_cluster | scripts/_explore_ve_by_cluster.py | 0 | _explore_ve_by_cluster.py — READ-ONLY: VE field x cluster x value comparison across clusters. |
| scripts_export_md_to_pdf_v1_20260703 | scripts/_export_md_to_pdf_v1_20260703.py | 1 | Reusable Markdown -> PDF exporter (reportlab; no external binaries). |
| scripts_export_prose_to_md_v1_20260703 | scripts/_export_prose_to_md_v1_20260703.py | 1 | Regenerate folder .md documents FROM the DB corpus (prose_section is canonical), |
| scripts_extract_m10_core_group_20260623 | scripts/_extract_m10_core_group_20260623.py | 1 | Mechanical assembly of an M10 CORE reading group from the on-disk corpus |
| scripts_generate_cluster_findings_report_v1_20260506 | scripts/_generate_cluster_findings_report_v1_20260506.py | 1 | _generate_cluster_findings_report_v1_20260506.py — read-only. |
| scripts_generate_cluster_gate | scripts/_generate_cluster_gate.py | 0 | _generate_cluster_gate.py  — READ-ONLY per-cluster gate report for the L2 verse-read. |
| scripts_generate_cluster_keyword_analytics_v1_20260523 | scripts/_generate_cluster_keyword_analytics_v1_20260523.py | 1 | Generate a cluster-level keyword analytics report from verse_context.keywords. |
| scripts_generate_cluster_overview_v1_20260508 | scripts/_generate_cluster_overview_v1_20260508.py | 1 | _generate_cluster_overview_v1_20260508.py — read-only. |
| scripts_generate_cluster_term_report_v1_20260505 | scripts/_generate_cluster_term_report_v1_20260505.py | 1 | _generate_cluster_term_report_v1_20260505.py — read-only. |
| scripts_generate_dimension_report | scripts/_generate_dimension_report.py | 0 | Generate a dimension index summary report. |
| scripts_generate_meaning_quality_check | scripts/_generate_meaning_quality_check.py | 0 | Read-only quality-check report: N random covered verses per term, showing the |
| scripts_generate_programme_report | scripts/_generate_programme_report.py | 0 | Generate a comprehensive programme status report. |
| scripts_generate_verse_meanings_export | scripts/_generate_verse_meanings_export.py | 0 | Read-only export of verse MEANINGS (l2_meaning paragraphs only) for a cluster. |
| scripts_harvest_characteristic_evidence_v1_20260703 | scripts/_harvest_characteristic_evidence_v1_20260703.py | 1 | Read-only harvest: scan the 150 Psalm Phase-2 readings for the recurring |
| scripts_inspect_unit_lexical_v1_20260703 | scripts/_inspect_unit_lexical_v1_20260703.py | 1 | Read-back inspector: lay a segmentation UNIT's verse text alongside its Phase-1 |
| scripts_integrity_full_check | scripts/_integrity_full_check.py | 0 | DB path resolved relative to this script (project moved off Google Drive 2026-06-03; see CLAUDE.md §13) |
| scripts_keyword_cluster_analysis_v1_20260523 | scripts/_keyword_cluster_analysis_v1_20260523.py | 1 | Stage 2 keyword clustering analysis for the discovery pass. |
| scripts_keyword_discovery_subgroup_v1_20260523 | scripts/_keyword_discovery_subgroup_v1_20260523.py | 1 | Interim keyword-discovery pass for an under-digested sub-group. |
| scripts_lexical_revelation_test_20260624 | scripts/_lexical_revelation_test_20260624.py | 1 | Lexical-Revelation Test (LRT) — runs DURING deep evidence gathering (step 3) to |
| scripts_list_shared_words | scripts/_list_shared_words.py | 0 | List all 100%-shared words with their terms and cross-registry links. |
| scripts_load_keywords_to_db_v1_20260523 | scripts/_load_keywords_to_db_v1_20260523.py | 1 | Load inner-being keywords from discovery JSONs into verse_context.keywords. |
| scripts_onboard_satan_h7854_v1_20260706 | scripts/_onboard_satan_h7854_v1_20260706.py | 1 | Force-onboard H7854 (Satan) into the 'spiritual powers' registry (195) as a third-party |
| scripts_patch_report | scripts/_patch_report.py | 0 | Apply all corrections and additions to the programme report in one pass. |
| scripts_preflight_m20_dir_005_M20_A_mapping | scripts/_preflight_m20_dir_005_M20_A_mapping.py | 0 | Pre-flight for DIR-20260513-005 (M20-A mapping apply). |
| scripts_pro_read_lib | scripts/_pro_read_lib.py | 0 | Compact builder for Proverbs char-driven readings (Stage-4). |
| scripts_probe_gate1_registry_homes_v1_20260706 | scripts/_probe_gate1_registry_homes_v1_20260706.py | 1 | Read-only: for each of the 97 gate1 orphan strongs, find its natural registry home. |
| scripts_probe_gate1_span_orphans_v1_20260705 | scripts/_probe_gate1_span_orphans_v1_20260705.py | 1 | _probe_gate1_span_orphans_v1_20260705.py  — Gate-1 span-orphan audit (reusable, read-only). |
| scripts_probe_isa43_validation_dump_v1_20260705 | scripts/_probe_isa43_validation_dump_v1_20260705.py | 1 | _probe_isa43_validation_dump_v1_20260705.py — full DB dump for Isa 43:1-2 (read-only). |
| scripts_probe_lexical_all14_v8_20260702 | scripts/_probe_lexical_all14_v8_20260702.py | 1 | _probe_lexical_all14_v8_20260702.py  (READ-ONLY) |
| scripts_probe_lexical_derivation_all14_v5_20260701 | scripts/_probe_lexical_derivation_all14_v5_20260701.py | 1 | _probe_lexical_derivation_all14_v5_20260701.py  (READ-ONLY) |
| scripts_probe_lexical_derivation_all14_v6_20260701 | scripts/_probe_lexical_derivation_all14_v6_20260701.py | 1 | _probe_lexical_derivation_all14_v6_20260701.py  (READ-ONLY) |
| scripts_probe_lexical_derivation_end_to_end_v4_20260701 | scripts/_probe_lexical_derivation_end_to_end_v4_20260701.py | 1 | _probe_lexical_derivation_end_to_end_v4_20260701.py  (READ-ONLY) |
| scripts_probe_lexical_derivation_harness_v1_20260701 | scripts/_probe_lexical_derivation_harness_v1_20260701.py | 1 | _probe_lexical_derivation_harness_v1_20260701.py  (READ-ONLY validation harness) |
| scripts_probe_lexical_derivation_harness_v2_passage_20260701 | scripts/_probe_lexical_derivation_harness_v2_passage_20260701.py | 1 | _probe_lexical_derivation_harness_v2_passage_20260701.py  (READ-ONLY, PASSAGE-AWARE) |
| scripts_probe_lexical_derivation_harness_v3_startup_20260701 | scripts/_probe_lexical_derivation_harness_v3_startup_20260701.py | 1 | _probe_lexical_derivation_harness_v3_startup_20260701.py  (READ-ONLY) |
| scripts_probe_passage_material_v1_20260704 | scripts/_probe_passage_material_v1_20260704.py | 1 | Read-only: pull the raw material for one narrative passage (segment_unit) so the |
| scripts_probe_primary_span_prose_reference_v1_20260705 | scripts/_probe_primary_span_prose_reference_v1_20260705.py | 1 | _probe_primary_span_prose_reference_v1_20260705.py — per book: primary spans + how many are |
| scripts_probe_psalms_gate1_completeness_v1_20260706 | scripts/_probe_psalms_gate1_completeness_v1_20260706.py | 1 | _probe_psalms_gate1_completeness_v1_20260706.py — Step (d) diagnostic (read-only). |
| scripts_probe_psalms_gate1_validate_v1_20260706 | scripts/_probe_psalms_gate1_validate_v1_20260706.py | 1 | _probe_psalms_gate1_validate_v1_20260706.py — Step (e) full-integrity validation (read-only). |
| scripts_probe_ve_lexical_per_book_census_v1_20260705 | scripts/_probe_ve_lexical_per_book_census_v1_20260705.py | 1 | _probe_ve_lexical_per_book_census_v1_20260705.py — per-book ve_lexical extraction (read-only, DB only). |
| scripts_probe_verse_record_orphan_census_v1_20260705 | scripts/_probe_verse_record_orphan_census_v1_20260705.py | 1 | _probe_verse_record_orphan_census_v1_20260705.py — per-book IB span-orphan census (read-only). |
| scripts_produce_family_base_source_json_20260711 | scripts/_produce_family_base_source_json_20260711.py | 1 | Produce a JSON BASE SOURCE per family (+ one OUTLIERS file) for Psalms. |
| scripts_produce_family_cluster_comparison_20260711 | scripts/_produce_family_cluster_comparison_20260711.py | 1 | Read-only: compare the FAMILY grouping (meaning/keyword-based) with the CLUSTER |
| scripts_produce_family_passage_base_source_v2_20260712 | scripts/_produce_family_passage_base_source_v2_20260712.py | 1 | Base source per family — WORK-CONTRACT + PASSAGE-UNIT + RAW-COMPLETE + ANCHORED. |
| scripts_produce_final_extract | scripts/_produce_final_extract.py | 0 | _produce_final_extract.py |
| scripts_produce_grain_index_v1_20260702 | scripts/_produce_grain_index_v1_20260702.py | 1 | _produce_grain_index_v1_20260702.py  (READ-ONLY) |
| scripts_produce_registry_full_extract | scripts/_produce_registry_full_extract.py | 0 | Produce a FULL markdown extract of a single registry word: every term and |
| scripts_produce_term_evidence_digest_v1_20260702 | scripts/_produce_term_evidence_digest_v1_20260702.py | 1 | _produce_term_evidence_digest_v1_20260702.py  (READ-ONLY) |
| scripts_produce_vc_word_report | scripts/_produce_vc_word_report.py | 0 | Produce a Verse Context word report — shows the full classification result |
| scripts_produce_ve_narration_v1 | scripts/_produce_ve_narration_v1.py | 0 | _produce_ve_narration_v1.py (2026-06-15) — compose the TEMPLATED NARRATION for a term-in-verse |
| scripts_prototype_finding_lifecycle | scripts/_prototype_finding_lifecycle.py | 0 | _prototype_finding_lifecycle.py — READ-ONLY prototype of the finding correction cycle. Loads a findings |
| scripts_prototype_l1_mechanical | scripts/_prototype_l1_mechanical.py | 0 | _prototype_l1_mechanical.py  — READ-ONLY L1-mechanical prototype (resolves R2/R4/R6; R7 via --morph). |
| scripts_prototype_l1_morph | scripts/_prototype_l1_morph.py | 0 | _prototype_l1_morph.py  — READ-ONLY R7 morphology pass (STEP + DB). |
| scripts_prototype_meaning_run | scripts/_prototype_meaning_run.py | 0 | _prototype_meaning_run.py — READ-ONLY prototype of the L1 verse-level MEANING RUN. For a term, parses its |
| scripts_prototype_p1_keywords | scripts/_prototype_p1_keywords.py | 0 | _prototype_p1_keywords.py — READ-ONLY prototype. Rebuilds the L1 keyword set from a term's STEP meaning |
| scripts_prototype_step_morph | scripts/_prototype_step_morph.py | 0 | _prototype_step_morph.py — READ-ONLY prototype. Pulls STEP preview HTML per verse and extracts the |
| scripts_pull_reread_passage_input_v1_20260714 | scripts/_pull_reread_passage_input_v1_20260714.py | 1 | Leaner re-read passage-input pull (v1, 2026-07-14). |
| scripts_pull_verify_batch_v1_20260714 | scripts/_pull_verify_batch_v1_20260714.py | 1 | Pull a batch of lexicals for MANUAL source-verification of one dimension (read-only, v1 2026-07-14). |
| scripts_purge_softdeleted_velexical_v1_20260714 | scripts/_purge_softdeleted_velexical_v1_20260714.py | 1 | Hard-purge ANCIENT soft-deleted ve_lexical rows to reclaim DB space (v1, 2026-07-14). |
| scripts_realign_meaning_tables | scripts/_realign_meaning_tables.py | 0 | _realign_meaning_tables.py |
| scripts_realign_quality_flags | scripts/_realign_quality_flags.py | 0 | _realign_quality_flags.py |
| scripts_remediate_cluster_v1_20260602 | scripts/_remediate_cluster_v1_20260602.py | 1 | Master cluster-remediation orchestrator (one cluster, packaged). |
| scripts_render_narratives_to_md_20260712 | scripts/_render_narratives_to_md_20260712.py | 1 | Render a family's narrative output to readable markdown: each passage, then the |
| scripts_repair_02_zero_padding | scripts/_repair_02_zero_padding.py | 0 | Fix 2 — Normalise zero-padded registry IDs in 4 tables. |
| scripts_repair_03_wa_file_index | scripts/_repair_03_wa_file_index.py | 0 | Fix 3 — Recreate wa_file_index to register FK to word_registry(id). |
| scripts_repair_05_wa_term_related_words | scripts/_repair_05_wa_term_related_words.py | 0 | Fix 5 — Recreate wa_term_related_words to register FK to wa_term_inventory(id). |
| scripts_repair_06_wa_term_root_family | scripts/_repair_06_wa_term_root_family.py | 0 | Fix 6 — Recreate wa_term_root_family to register FK to wa_term_inventory(id). |
| scripts_repair_07_wa_verse_records | scripts/_repair_07_wa_verse_records.py | 0 | Fix 7 — Recreate wa_verse_records to register FKs to wa_file_index(id) |
| scripts_repair_step_missing_verses_v1_20260713 | scripts/_repair_step_missing_verses_v1_20260713.py | 1 | Repair STEP-missing verse-records — morphology-anchored (researcher direction 2026-07-13). |
| scripts_reread_finish_v1_20260709 | scripts/_reread_finish_v1_20260709.py | 1 | _reread_finish_v1_20260709.py -- finish one re-read chapter: apply -> gate -> commit -> close -> stamp. |
| scripts_reread_ledger_lib | scripts/_reread_ledger_lib.py | 0 | Reusable ledger-scaffolding helpers for the corrected-method Psalms reread. |
| scripts_reread_worklist_v1_20260709 | scripts/_reread_worklist_v1_20260709.py | 1 | _reread_worklist_v1_20260709.py  --  control table for the isolated-per-chapter re-read loop. |
| scripts_reset_registry_status | scripts/_reset_registry_status.py | 0 | One-off: reset word_registry.phase1_status for all 170 'In Progress' words. |
| scripts_reverse_findings_stageC_restrict_20260619 | scripts/_reverse_findings_stageC_restrict_20260619.py | 1 | _reverse_findings_stageC_restrict_20260619.py — REVERSE Stage C (un-restrict the OLD findings). |
| scripts_roll_retrofit_v1_20260714 | scripts/_roll_retrofit_v1_20260714.py | 1 | Roll the retrofit-dim derivation across a chapter batch: derive -> apply(live) -> READ-BACK (v1, 2026-07-14). |
| scripts_run_cause_api | scripts/_run_cause_api.py | 0 | _run_cause_api.py (2026-06-16) — run the focused cause-resolution API package and save the output. |
| scripts_run_gate1_onboard_batch_v1_20260706 | scripts/_run_gate1_onboard_batch_v1_20260706.py | 1 | Gate-1 orphan onboarding orchestrator (Group C — clean adds to existing/new registries). |
| scripts_run_passa_via_api_v1_20260515 | scripts/_run_passa_via_api_v1_20260515.py | 1 | Pass A meaning record via Claude API (cluster-agnostic). |
| scripts_run_proverbs_stage1_onboard_v1_20260712 | scripts/_run_proverbs_stage1_onboard_v1_20260712.py | 1 | Proverbs Stage-1 onboarding (registry path) — the 30 candidate terms absent from |
| scripts_run_ve_reads_governed | scripts/_run_ve_reads_governed.py | 0 | _run_ve_reads_governed.py (2026-06-17) — governed corpus API read for ONE VE field. |
| scripts_schema_dump | scripts/_schema_dump.py | 0 | (no module docstring or leading comment found -- needs a manual purpose write-up) |
| scripts_snapshot_db_v1_20260714 | scripts/_snapshot_db_v1_20260714.py | 1 | Cadence-aware DB snapshot + prune helper (v1, 2026-07-14). |
| scripts_term_sharing_spider | scripts/_term_sharing_spider.py | 0 | Generate term-sharing spider/network diagram showing pools of connected words. |
| scripts_tmp_read_cycle2_rest | scripts/_tmp_read_cycle2_rest.py | 0 | Build the remaining cycle-2 passage readings (Pro 1:24 - 2:3) via _pro_read_lib. |
| scripts_tmp_read_cycle3 | scripts/_tmp_read_cycle3.py | 0 | Build cycle-3 passage readings (Pro 2:4 - 2:20) via _pro_read_lib. Each in isolation. |
| scripts_update_claude_code_instructions | scripts/_update_claude_code_instructions.py | 0 | Update WA-SessionB-ClaudeCode-Instructions.md with all post-v5 changes. |
| scripts_update_reference_doc | scripts/_update_reference_doc.py | 0 | Update WA-Reference-v5.1 to v5.2 with new columns from housekeeping. |
| scripts_update_registry_guide | scripts/_update_registry_guide.py | 0 | Update Registry Management Guide with new fields, queries, and terminology. |
| scripts_ve_engine_v2 | scripts/_ve_engine_v2.py | 0 | _ve_engine_v2.py (2026-06-16) — FIRST working build of the verse-lexical engine per 01b v2. |
| scripts_analytics_bible_analytics | scripts/analytics/bible_analytics.py | 0 | bible_analytics.py |
| scripts_analytics_db_client | scripts/analytics/db_client.py | 0 | db_client.py |
| scripts_analytics_morph_util | scripts/analytics/morph_util.py | 0 | morph_util.py — canonical morphology-code helpers (STEP / OSHB + Robinson Greek). |
| scripts_analytics_step_client | scripts/analytics/step_client.py | 0 | step_client.py |
| scripts_analytics_word_export | scripts/analytics/word_export.py | 0 | word_export.py |
| scripts_analytics_zotero_client | scripts/analytics/zotero_client.py | 0 | zotero_client.py |
| scripts_apply_session_patch | scripts/apply_session_patch.py | 0 | apply_session_patch.py |
| scripts_audit_cluster_v1_20260601 | scripts/audit_cluster_v1_20260601.py | 1 | Consolidated, reusable cluster auditor (read-only). |
| scripts_backfill_root_families | scripts/backfill_root_families.py | 0 | backfill_root_families.py |
| scripts_backup_db_to_nas | scripts/backup_db_to_nas.py | 0 | backup_db_to_nas.py — consistent off-Drive backup of bible_research.db to the NAS. |
| scripts_build_cause_api_package | scripts/build_cause_api_package.py | 0 | build_cause_api_package.py (2026-06-16) — Alt 2: prepare a focused, single-purpose API run that does |
| scripts_build_cluster_findings_digest | scripts/build_cluster_findings_digest.py | 0 | Read-only: dump a cluster's active findings as a navigable markdown digest. |
| scripts_build_complete_extract | scripts/build_complete_extract.py | 0 | build_complete_extract.py |
| scripts_build_corpus_prose | scripts/build_corpus_prose.py | 0 | build_corpus_prose.py — Compile completed word-analysis chapters into a book. |
| scripts_build_correlation_extract | scripts/build_correlation_extract.py | 0 | build_correlation_extract.py |
| scripts_build_dimension_extract | scripts/build_dimension_extract.py | 0 | build_dimension_extract.py |
| scripts_build_field_api_package | scripts/build_field_api_package.py | 0 | build_field_api_package.py (2026-06-16) — Alt 3: prepare a focused, single-instruction API read for ANY |
| scripts_build_file_manifest | scripts/build_file_manifest.py | 0 | build_file_manifest.py — Generates database/file_manifest.json |
| scripts_build_file_patterns_extract | scripts/build_file_patterns_extract.py | 0 | build_file_patterns_extract.py — File-name pattern registry extract (M35). |
| scripts_build_flag_classification_package_v1_20260601 | scripts/build_flag_classification_package_v1_20260601.py | 1 | Assemble the FLAG-cluster classification package for Claude AI (chat). |
| scripts_build_label_patterns_extract | scripts/build_label_patterns_extract.py | 0 | build_label_patterns_extract.py — Label pattern registry extract (M35). |
| scripts_build_m01_by_characteristic | scripts/build_m01_by_characteristic.py | 0 | build_m01_by_characteristic.py (2026-06-18) — emit M01 verse-records grouped BY characteristic. |
| scripts_build_m01_findings_oldnew_extract | scripts/build_m01_findings_oldnew_extract.py | 0 | build_m01_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M01 findings: |
| scripts_build_m02_findings_oldnew_extract | scripts/build_m02_findings_oldnew_extract.py | 0 | build_m02_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M02 findings: |
| scripts_build_obs_catalogue_export | scripts/build_obs_catalogue_export.py | 0 | build_obs_catalogue_export.py — generic Observation Question Catalogue export. |
| scripts_build_obs_catalogue_tiered_extract | scripts/build_obs_catalogue_tiered_extract.py | 0 | build_obs_catalogue_tiered_extract.py — read-only. |
| scripts_build_patch_types_extract | scripts/build_patch_types_extract.py | 0 | build_patch_types_extract.py — Patch type registry extract (M35 scope). |
| scripts_build_programme_prose_extract | scripts/build_programme_prose_extract.py | 0 | build_programme_prose_extract.py — Prose-book extract. |
| scripts_build_reference_snapshot | scripts/build_reference_snapshot.py | 0 | build_reference_snapshot.py — Reference-as-Database snapshot extractor. |
| scripts_build_rules_extract | scripts/build_rules_extract.py | 0 | build_rules_extract.py — Global rules + addenda JSON extract. |
| scripts_build_script_registry | scripts/build_script_registry.py | 0 | build_script_registry.py — canonical, regenerable registry of the project's scripts. |
| scripts_build_session_a_prose | scripts/build_session_a_prose.py | 0 | Render per-word Session A prose as a self-contained `.md` for Verse Context input. |
| scripts_build_tier_catalogue_update_patch_20260619 | scripts/build_tier_catalogue_update_patch_20260619.py | 1 | build_tier_catalogue_update_patch_20260619.py — emit the tier-catalogue refit as a reviewable JSON patch. |
| scripts_build_ve_lexical_extract | scripts/build_ve_lexical_extract.py | 0 | build_ve_lexical_extract.py (2026-06-16) — emit a cluster's v2 verse-lexical as JSON for AI Chat. |
| scripts_build_vocab_extract | scripts/build_vocab_extract.py | 0 | build_vocab_extract.py — Controlled vocabulary extract (M32 scope). |
| scripts_build_word_relationship_report | scripts/build_word_relationship_report.py | 0 | build_word_relationship_report.py — READ-ONLY. |
| scripts_classify_term_introduction_source | scripts/classify_term_introduction_source.py | 0 | classify_term_introduction_source.py — Heuristic classifier for M30 backfill. |
| scripts_combine_cluster_published_to_docx | scripts/combine_cluster_published_to_docx.py | 0 | Combine the latest chapter drafts in a cluster's Published/ folder into one .docx. |
| scripts_cost_ledger | scripts/cost_ledger.py | 0 | cost_ledger.py — ONE combined cost ledger across all three Claude surfaces. |
| scripts_export_database_schema | scripts/export_database_schema.py | 0 | export_database_schema.py |
| scripts_export_prose_chapter_edit | scripts/export_prose_chapter_edit.py | 0 | Export one current prose chapter or section as a temporary editable Markdown file. |
| scripts_export_tier_catalogue | scripts/export_tier_catalogue.py | 0 | export_tier_catalogue.py (2026-06-17) — read-only export of the Tier Catalogue |
| scripts_export_ve_status_reports | scripts/export_ve_status_reports.py | 0 | export_ve_status_reports.py (2026-06-17) — two read-only status reports over `ve_lexical`: |
| scripts_export_word_json | scripts/export_word_json.py | 0 | export_word_json.py |
| scripts_extract_term_data | scripts/extract_term_data.py | 0 | extract_term_data.py |
| scripts_generate_cluster_summary_v1_20260603 | scripts/generate_cluster_summary_v1_20260603.py | 1 | generate_cluster_summary_v1_20260603.py |
| scripts_generate_full_cluster_audit_v1_20260603 | scripts/generate_full_cluster_audit_v1_20260603.py | 1 | generate_full_cluster_audit_v1_20260603.py  (READ-ONLY) |
| scripts_generate_programme_snapshot | scripts/generate_programme_snapshot.py | 0 | Generate a programme snapshot report. |
| scripts_generate_registry_overview | scripts/generate_registry_overview.py | 0 | generate_registry_overview.py |
| scripts_generate_session_a_extract | scripts/generate_session_a_extract.py | 0 | generate_session_a_extract.py — Mechanical Session A extract generator. |
| scripts_import_prose_chapter_edit | scripts/import_prose_chapter_edit.py | 0 | Turn an edited prose chapter Markdown file into a PROSE supersede patch. |
| scripts_inspect_db_only_terms | scripts/inspect_db_only_terms.py | 0 | Detail query for DB_ONLY terms flagged during soul audit. |
| scripts_list_tables | scripts/list_tables.py | 0 | (no module docstring or leading comment found -- needs a manual purpose write-up) |
| scripts_populate_dimension_index | scripts/populate_dimension_index.py | 0 | populate_dimension_index.py |
| scripts_query_h2734 | scripts/query_h2734.py | 0 | (no module docstring or leading comment found -- needs a manual purpose write-up) |
| scripts_readiness_sweep_pilot | scripts/readiness_sweep_pilot.py | 0 | Readiness Sweep Pilot — read-only inspection for a single registry. |
| scripts_readiness_sweep_programme_scan | scripts/readiness_sweep_programme_scan.py | 0 | Programme-wide readiness sweep scan. |
| scripts_search_prose | scripts/search_prose.py | 0 | Search prose_section across all prose books. |
| scripts_token_cost_history | scripts/token_cost_history.py | 0 | token_cost_history.py — an auditable history of token consumption and estimated cost. |
| scripts_v3_2_l1 | scripts/v3_2_l1.py | 0 | v3_2_l1.py  — V3_2 Level 1 (verse establishment) command. |
| scripts_verify_soul | scripts/verify_soul.py | 0 | Quick post-audit verification for soul (registry 182). |
| scripts_verse_vertical_pass | scripts/verse_vertical_pass.py | 0 | verse_vertical_pass.py |
| scripts_word_full_extract | scripts/word_full_extract.py | 0 | (no module docstring or leading comment found -- needs a manual purpose write-up) |
| scripts_word_study_extract | scripts/word_study_extract.py | 0 | word_study_extract.py |

## Files with no discoverable docstring/comment (purpose is a placeholder)

- `scripts/_apply_descriptions_patch.py`
- `scripts/_schema_dump.py`
- `scripts/list_tables.py`
- `scripts/query_h2734.py`
- `scripts/word_full_extract.py`
