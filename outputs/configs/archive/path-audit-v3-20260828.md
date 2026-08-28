# Project-wide hardcoded-location-literal scan

> Project-wide scan for hardcoded folder/file-path string literals not backed by a live cfg accessor — ADVISORY, see lib/pathaudit.py's own docstring for method and honest limits. Escalation #971/#976.

## Contents

- [Summary](#summary)
- [Findings](#findings)

<a id="summary"></a>
## Summary

- **216** script(s) scanned (inactive-marked scripts excluded)
- **126** hardcoded location literal(s) found in **61** file(s)

<a id="findings"></a>
## Findings

| file | line | literal | cfg_utility registered |
| --- | --- | --- | --- |
| iba/app/lib/manifest.py | 139 | research/investigations | yes |
| iba/app/lib/manifest.py | 149 | data/imports/wa/patches | yes |
| iba/app/lib/manifest.py | 149 | archive/patches | yes |
| iba/app/lib/manifest.py | 155 | data/imports | yes |
| iba/app/lib/manifest.py | 157 | data/exports | yes |
| iba/app/lib/manifest.py | 159 | research/discovery | yes |
| iba/app/lib/manifest.py | 161 | data/schema | yes |
| iba/app/lib/manifest.py | 163 | archive/scripts | yes |
| iba/app/lib/manifest.py | 165 | archive/logs | yes |
| iba/app/lib/manifest.py | 167 | archive/docs | yes |
| iba/app/lib/manifest.py | 169 | outputs/reports | yes |
| iba/app/lib/prosestore.py | 54 | Workflow | yes |
| iba/app/lib/prosestore.py | 55 | outputs | yes |
| iba/app/lib/prosestore.py | 56 | outputs | yes |
| iba/app/lib/prosestore.py | 62 | outputs | yes |
| iba/app/lib/prosestore.py | 84 | outputs/markdown/prose-edits | yes |
| iba/app/migration/add_passage_story_columns.py | 30 | iba/app/db/iba.db | NO |
| iba/app/migration/add_resolution_kind_column_v1_20260822.py | 21 | iba/app/migration/add_resolution_kind_column_v1_20260822.py | yes |
| iba/app/migration/allocate_strongs.py | 34 | research/discovery/registry-synonyms-curated-20260707.json | NO |
| iba/app/migration/anchor_test_plan_governance_rule_20260822.py | 42 | iba/app/migration/anchor_test_plan_governance_rule_20260822.py | yes |
| iba/app/migration/backfill_passage_tracking_daniel.py | 28 | iba/app/verse-analysis/Daniel | NO |
| iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | 65 | Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md | yes |
| iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | 73 | Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md | yes |
| iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | 78 | Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md | yes |
| iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | 84 | Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md | yes |
| iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | 90 | Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md | yes |
| iba/app/migration/bootstrap_behaviour_rules_v1_20260818.py | 280 | iba/app/migration/bootstrap_behaviour_rules_v1_20260818.py | yes |
| iba/app/migration/bootstrap_book_narrative_generate.py | 26 | iba/app/ps/BookNarrative-Generate.ps1 | NO |
| iba/app/migration/bootstrap_book_narrative_generate.py | 75 | iba/docs/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md | NO |
| iba/app/migration/bootstrap_book_narrative_generate.py | 101 | iba/app/reports/export/narrative-generate-usage.csv | NO |
| iba/app/migration/bootstrap_book_narrative_generate.py | 110 | iba/app/lib/narrativegenerate.py | NO |
| iba/app/migration/bootstrap_book_narrative_validate.py | 28 | iba/app/ps/BookNarrative-Validate.ps1 | NO |
| iba/app/migration/bootstrap_book_narrative_validate.py | 82 | iba/docs/WA-inner-being-narrative-guidance-v1-2026-07-28.md | NO |
| iba/app/migration/bootstrap_book_narrative_validate.py | 88 | iba/app/reports/book-narrative-scope-check.md | NO |
| iba/app/migration/bootstrap_cluster_tables_20260811.py | 51 | iba/app/reports/cluster-master-20260811.csv | NO |
| iba/app/migration/bootstrap_configuration_maintenance.py | 114 | "iba/app/config/CONFIG-REPORT.md" | NO |
| iba/app/migration/bootstrap_configuration_maintenance.py | 118 | "iba/app/config/archive" | NO |
| iba/app/migration/bootstrap_content_index.py | 171 | iba/app/ps/ContentIndex-Rebuild.ps1 | NO |
| iba/app/migration/bootstrap_content_index.py | 177 | iba/app/ps/ContentIndex-Search.ps1 | NO |
| iba/app/migration/bootstrap_content_index.py | 186 | iba/app/reports/content-index-rebuild.md | NO |
| iba/app/migration/bootstrap_content_index.py | 189 | iba/app/reports/content-index-size-profile.md | NO |
| iba/app/migration/bootstrap_content_index.py | 193 | iba/app/lib/contentindex.py | NO |
| iba/app/migration/bootstrap_content_index.py | 218 | iba/app/ps/ContentIndex-SizeProfile.ps1 | NO |
| iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py | 40 | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py | yes |
| iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py | 196 | iba/app/reports/passage-quality.md | yes |
| iba/app/migration/bootstrap_file_manifest.py | 125 | iba/app/ps/Manifest-Rebuild.ps1 | NO |
| iba/app/migration/bootstrap_file_manifest.py | 131 | iba/app/ps/Manifest-Search.ps1 | NO |
| iba/app/migration/bootstrap_file_manifest.py | 145 | iba/app/reports/file-manifest.md | NO |
| iba/app/migration/bootstrap_file_manifest.py | 148 | iba/app/lib/manifest.py | NO |
| iba/app/migration/bootstrap_lexicon_parsed_layer.py | 312 | iba/app/ps/Lexicon-Parse.ps1 | NO |
| iba/app/migration/bootstrap_lexicon_parsed_layer.py | 334 | "iba/app/reports/lexicon-parse.md" | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 50 | iba/app/ps/SeedCandidate-Report.ps1 | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 54 | iba/app/reports/seed-candidate.md | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 63 | iba/app/ps/StrongMeaning-Report.ps1 | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 67 | iba/app/reports/strong-meaning.md | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 76 | iba/app/ps/SpanAnalysis-Report.ps1 | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 80 | iba/app/reports/span-analysis.md | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 89 | iba/app/ps/SchemaOverview-Report.ps1 | NO |
| iba/app/migration/bootstrap_new_reports_phase1.py | 93 | iba/app/reports/schema-overview.md | NO |
| iba/app/migration/bootstrap_oneoff_report_naming.py | 32 | iba/app/reports/ | NO |
| iba/app/migration/bootstrap_passage_debate_report.py | 31 | iba/app/ps/PassageDebate-Report.ps1 | NO |
| iba/app/migration/bootstrap_passage_debate_report.py | 105 | iba/docs/WA-passage-read-guidance-v1.2-2026-07-27.md | NO |
| iba/app/migration/bootstrap_passage_debate_report.py | 111 | iba/docs/WA-interpretation-questions-v1.0-2026-07-26.md | NO |
| iba/app/migration/bootstrap_passage_debate_sync.py | 38 | iba/app/ps/PassageDebate-Sync.ps1 | NO |
| iba/app/migration/bootstrap_project_database_enum_v1_20260818.py | 56 | iba/app/db/iba.db | NO |
| iba/app/migration/bootstrap_prose_authority_v1_20260818.py | 57 | Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md | NO |
| iba/app/migration/bootstrap_raw_backfill.py | 60 | iba/app/ps/Raw-Backfill.ps1 | NO |
| iba/app/migration/bootstrap_report_persistence_governance.py | 45 | iba/app/reports/candidate-quality.md | NO |
| iba/app/migration/bootstrap_report_persistence_governance.py | 47 | iba/app/reports/passage-quality.md | NO |
| iba/app/migration/bootstrap_reports_registration.py | 76 | iba/app | NO |
| iba/app/migration/bootstrap_reports_registration.py | 79 | iba/app/reports | NO |
| iba/app/migration/bootstrap_retention_table_export_registration.py | 73 | iba/app/ps/Log-Retention.ps1 | NO |
| iba/app/migration/bootstrap_retention_table_export_registration.py | 81 | iba/app/ps/Export-Tables.ps1 | NO |
| iba/app/migration/bootstrap_retention_table_export_registration.py | 86 | iba/app/export | NO |
| iba/app/migration/bootstrap_retention_table_export_registration.py | 130 | iba/app/reports/candidate-load.md | NO |
| iba/app/migration/bootstrap_span_reading.py | 70 | iba/app/ps/VerseSpanReading.ps1 | NO |
| iba/app/migration/bootstrap_verse_analysis_report.py | 25 | iba/app/ps/VerseSpanMeaning-Report.ps1 | NO |
| iba/app/migration/bootstrap_verse_analysis_report.py | 67 | iba/app/verse-analysis | NO |
| iba/app/migration/bootstrap_whole_book_read.py | 25 | iba/app/ps/WholeBookRead-Report.ps1 | NO |
| iba/app/migration/bootstrap_word_audit.py | 103 | iba/app/ps/Word-Audit.ps1 | NO |
| iba/app/migration/bootstrap_word_registry_span_report.py | 30 | iba/app/ps/WordRegistrySpan-Report.ps1 | NO |
| iba/app/migration/bootstrap_word_registry_span_report.py | 73 | iba/app/verse-analysis/word_registry | NO |
| iba/app/migration/build_base_all_books.py | 76 | iba/app/reports | NO |
| iba/app/migration/build_cfg_index_table.py | 32 | iba/app/db/iba.db | NO |
| iba/app/migration/build_closing_sections_schema.py | 37 | iba/app/db/iba.db | NO |
| iba/app/migration/build_method_rule_table.py | 43 | iba/app/db/iba.db | NO |
| iba/app/migration/build_operations_schema.py | 40 | iba/app/db/iba.db | NO |
| iba/app/migration/build_quality_check_table.py | 32 | iba/app/db/iba.db | NO |
| iba/app/migration/cleanout_retired_passage_config.py | 49 | iba/app/db/iba.db | NO |
| iba/app/migration/correct_dan_1_boundary_range.py | 45 | iba\app\verse-analysis\Daniel\dan-1-8-21-verse-span-meaning.md | NO |
| iba/app/migration/correct_dan_1_boundary_range.py | 46 | iba\app\verse-analysis\Daniel\WA-dan-1-8-21-debate-v1.3-2026-07-29.md | NO |
| iba/app/migration/escalation_redesign_v1_20260819.py | 57 | iba/app/db/iba.db | NO |
| iba/app/migration/escalation_redesign_v1_20260819_ROLLBACK.py | 21 | iba/app/db/iba.db | NO |
| iba/app/migration/escalation_redesign_v2_20260820.py | 45 | iba/app/db/iba.db | NO |
| iba/app/migration/escalation_reset_v1_20260816.py | 57 | iba/app/db/iba.db | NO |
| iba/app/migration/escalation_reset_v1_20260816.py | 259 | iba/app/lib/clusterassign.py | NO |
| iba/app/migration/escalation_reset_v1_20260816.py | 260 | iba/app/lib/clusterreport.py | NO |
| iba/app/migration/escalation_reset_v1_20260816.py | 261 | iba/app/lib/strongreconcile.py | NO |
| iba/app/migration/escalation_v1_load_20260821.py | 51 | iba/app/reports/escalation-v1-snapshot-20260821.json | NO |
| iba/app/migration/escalation_v1_snapshot_20260821.py | 49 | iba/app/db/archive/escalation-export-20260820.json | NO |
| iba/app/migration/escalation_v1_snapshot_20260821.py | 165 | iba/app/reports/escalation-v1-snapshot-20260821.json | NO |
| iba/app/migration/fix_cfg_column_fk_gaps.py | 27 | iba/app/db/iba.db | NO |
| iba/app/migration/fix_dispatcher_answerrun_795_20260822.py | 49 | iba/app/migration/fix_dispatcher_answerrun_795_20260822.py | yes |
| iba/app/migration/fix_escalation_history_write_grant_20260820.py | 19 | iba/app/db/iba.db | NO |
| iba/app/migration/fix_escalation_short_description_and_columns_20260820.py | 59 | outputs/markdown/iba-table-review-response-v1-20260816.md | NO |
| iba/app/migration/fix_escalation_short_description_and_columns_20260820.py | 86 | iba/app/reports/gr-prog-001-prose-canonical-authority-plan-20260818.md | NO |
| iba/app/migration/folder_purpose_build_v1_20260828.py | 258 | iba/app/lib/folderpurpose.py | NO |
| iba/app/migration/folder_purpose_build_v1_20260828.py | 263 | iba/app/ps/FolderPurpose.ps1 | NO |
| iba/app/migration/folder_purpose_build_v1_20260828.py | 290 | iba/docs/file-naming-and-location-governance-plan-v1-20260826.md | NO |
| iba/app/migration/import_seed.py | 30 | research/discovery/lemma-inventory-master-no-particles-20260707.json | NO |
| iba/app/migration/import_seed.py | 31 | research/investigations/ib-judgement-rejected-20260707.md | NO |
| iba/app/migration/pathaudit_build_v1_20260828.py | 64 | "outputs/configs/path-audit.md" | NO |
| iba/app/migration/pathaudit_build_v1_20260828.py | 67 | iba/app/lib/pathaudit.py | NO |
| iba/app/migration/pathaudit_build_v1_20260828.py | 72 | iba/app/ps/PathAudit.ps1 | NO |
| iba/app/migration/populate_cfg_index_rows.py | 24 | iba/app/db/iba.db | NO |
| iba/app/migration/rebuild_escalation_from_export_20260821.py | 69 | iba/app/db/archive | NO |
| iba/app/migration/rebuild_escalation_from_export_20260821.py | 382 | iba/app/db/archive/escalation-export-20260820.json | NO |
| iba/app/migration/rebuild_escalation_from_export_20260821.py | 383 | iba/app/db/archive/escalation_history-export-20260820.json | NO |
| iba/app/migration/rebuild_escalation_from_export_20260821.py | 405 | iba/app/reports/escalation-rebuild-dry-run-20260821.md | NO |
| iba/app/migration/rebuild_escalation_from_export_20260821.py | 409 | iba/app/reports/escalation-rebuild-dry-run-20260821.json | NO |
| iba/app/migration/reconcile_daniel_debate_paths.py | 37 | iba\app\verse-analysis\Daniel\ | NO |
| iba/app/migration/reconcile_daniel_debate_paths_20260808.py | 40 | iba\app\verse-analysis\Daniel\ | NO |
| iba/app/migration/rename_span_reading_to_lexical.py | 26 | iba/app/db/iba.db | NO |
| iba/app/migration/retrofit_debate_lexicon_tables.py | 35 | iba/app/db/iba.db | NO |
| iba/app/migration/seed_method_rules.py | 20 | iba/app/db/iba.db | NO |
| iba/app/tools/word_strong_span_report.py | 181 | iba/app/db/iba.db | NO |
