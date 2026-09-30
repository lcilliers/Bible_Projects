# Regrouping outputs/ and research/ — allocation proposal (v1)

**Date:** 2026-09-30 · **Status:** PROPOSAL for researcher review. Nothing has been moved yet.

**Request (researcher, verbatim):** *"review, and reallocate any investigations and finding in C:\Bible_study_projects\outputs and C:\Bible_study_projects\research and move it to _analytics if any of the results are useful, else move the files to archive."*

## 1. Summary

Scanned **907** live files (existing `archive/` subfolders excluded).

| Bucket | Files | Action |
|---|--:|---|
| Useful results → `_analytics` | 47 | move (§3) |
| Judgement calls | 14 | your decision (§4) |
| Live tool outputs / governed folders | 305 | **leave in place** (§5) |
| Process / superseded material | 541 | move to archive (§6, Appendix) |

**Finding:** nearly all of these files are process work, not results about the inner being. They cover DB repairs, dedup, morph backfill, L1/L2 dry-runs, AI-router tests, verse-context patch design, cluster-coverage checks, publishing readiness and backup incidents. The few files with lasting analytical value are in §3.

## 2. Decisions needed from you

1. **Archive destination.** Proposed: mirror the original path under the top-level `archive/`, i.e. `archive/research/investigations/…` and `archive/outputs/…` (including `outputs/markdown/…`). This keeps provenance readable. The alternative is the in-place `research/archive/` and `outputs/archive/` folders. Your folder-destination rule says I should ask rather than assume.
2. **New folder `_analytics/cross-cluster-web/`** for group A. Is this acceptable, or would you prefer somewhere else, e.g. under `_analytics/Clusters/`?
3. **Destinations in §3** (per group), and **§4 judgement calls**.

How the moves would be done: `git mv` (history kept), one commit. Afterwards I will check links: any moved file linked from CLAUDE.md, `iba/app/*.md` or memory is listed in the "linked from" column, and those links will be updated in the same pass.

## 3. Useful results → `_analytics` (proposed)

### A. Cross-cluster web (2026-06-08 roll-up + relationship probes + faculty-by-cluster) → `_analytics/cross-cluster-web/`

Direct bearing on the fan-out method: the inner being as a web. Measures how often clusters share verses (44% of verses are cross-cluster), classifies links as same-ish / relational / kin, lists homonyms that span clusters, and records the 06-08 reframe "the unit is a typed thing → relationship → effect, not the cluster". **Caveat:** counts come from the pre-reset bible_research.db cluster model (M01–M46), so they are background evidence, not current fact.

| File | Linked from |
|---|---|
| `research/investigations/wa-cluster-profiles-v1-20260608.md` | — |
| `research/investigations/wa-cross-cluster-cooccurrence-v1-20260608-matrix.csv` | — |
| `research/investigations/wa-cross-cluster-cooccurrence-v1-20260608.md` | — |
| `research/investigations/wa-cross-cluster-rollup-synthesis-v1-20260608.md` | memory/project_cross_cluster_three_link_classes.md |
| `research/investigations/wa-keyword-overlap-v1-20260608.md` | — |
| `research/investigations/wa-link-correlation-v1-20260608.md` | — |
| `research/investigations/wa-ontology-reframe-typed-relationships-v1-20260608.md` | memory/feedback_ontology_typed_relationships.md |
| `research/investigations/wa-relprobe-fear-strength-v1-20260608.md` | — |
| `research/investigations/wa-relprobe-life-relational-v1-20260608.md` | — |
| `research/investigations/wa-relprobe-sin-repentance-v1-20260608.md` | — |
| `research/investigations/wa-shared-forms-v1-20260608.md` | — |
| `outputs/markdown/validation/wa-faculty-by-cluster-20260624.md` | — |

### B. Ruthlessness / cruelty lexical discovery (2026-06-28) → `_analytics/characteristics/`

Living investigation doc + 7 STEP term-map/triage pairs (cruel, fierce, harsh, oppression, ruthless, severity, violence). Joins the 8 ruthlessness files already in `_analytics/characteristics/`.

| File | Linked from |
|---|---|
| `research/discovery/cruel_term_map_20260628.json` | — |
| `research/discovery/cruel_triage_20260628.md` | — |
| `research/discovery/fierce_term_map_20260628.json` | — |
| `research/discovery/fierce_triage_20260628.md` | — |
| `research/discovery/harsh_term_map_20260628.json` | — |
| `research/discovery/harsh_triage_20260628.md` | — |
| `research/discovery/oppression_term_map_20260628.json` | — |
| `research/discovery/oppression_triage_20260628.md` | — |
| `research/discovery/ruthless_term_map_20260628.json` | — |
| `research/discovery/ruthless_triage_20260628.md` | — |
| `research/discovery/severity_term_map_20260628.json` | — |
| `research/discovery/severity_triage_20260628.md` | — |
| `research/discovery/violence_term_map_20260628.json` | — |
| `research/discovery/violence_triage_20260628.md` | — |
| `research/investigations/wa-ruthlessness-investigation.md` | memory/feedback_single_living_register.md |

### C. Goodness word deep-dive (R067, 2026-04-28) → `_analytics/registry/word_registry/056_goodness/`

Prose, readiness, flags, Q&A and citations for goodness. Old-method, but the only consolidated goodness read-out.

| File | Linked from |
|---|---|
| `research/investigations/word_deep_dive/goodness/goodness-1-prose.md` | — |
| `research/investigations/word_deep_dive/goodness/goodness-2-analytic-readiness.md` | — |
| `research/investigations/word_deep_dive/goodness/goodness-3-open-flags.md` | — |
| `research/investigations/word_deep_dive/goodness/goodness-4-qa-list.md` | — |
| `research/investigations/word_deep_dive/goodness/goodness-5-citations.md` | — |

### D. Patience — DB appearance + related words (2026-06-14) → `_analytics/registry/word_registry/095_patience/`

Summary of where patience appears and its related words. Checked: `095_patience/` already holds `vc-report-116-patience-20260402.docx`, so it is the patience folder, even though the numbers differ (registry 116 vs folder prefix 095).

| File | Linked from |
|---|---|
| `outputs/markdown/patience-db-appearance-and-related-words-20260614.md` | — |

### E. John 1 — candidate-char analysis, human-presence screen, span heatmap → `_analytics/Bible_Books/John/`

The only John reading. Belongs with the book.

| File | Linked from |
|---|---|
| `outputs/markdown/john-1-candidate-char-analysis-v1.md` | — |
| `outputs/markdown/john-1-human-presence-screen-v1.md` | — |
| `outputs/markdown/span-heatmap-john-1-humanscreen.json` | — |
| `outputs/markdown/span-heatmap-john-1-v1.html` | — |

### F. Location / seat map + spirit under-detection (2026-06-18) → `_analytics/Clusters/M47 - inner-seat/`

The lexicon-mined inventory of seats and vessels (heart, soul, spirit, kidneys …) against faculties, and the finding that spirit was under-detected. Directly relevant to M47 inner-seat.

| File | Linked from |
|---|---|
| `outputs/markdown/wa-location-by-cluster-summary-v2-20260618.md` | — |
| `outputs/markdown/wa-location-coverage-and-spirit-underdetection-20260618.md` | — |
| `outputs/markdown/wa-location-seat-map-proposal-v1-20260618.md` | — |

### G. Grace × mercy term-pair binding + grace morph roles (2026-06-27) → `_analytics/registry/word_registry/057_grace/`

How the grace and mercy terms bind in their 6 shared verses, and what grammatical roles the grace terms take.

| File | Linked from |
|---|---|
| `outputs/markdown/validation/wa-term-morph-roles-G5485_H2580_H2603-20260627.md` | — |
| `outputs/markdown/validation/wa-term-pair-binding-grace-mercy-20260627.md` | — |

### H. Psalms base-source 112/116 transposition note (2026-07-12) → `_analytics/Bible_Books/Ps/_base-sources/`

An open data-quality note about the Psalms base sources. It should sit next to those files so it is seen.

| File | Linked from |
|---|---|
| `outputs/markdown/validation/wa-psalms-base-source-coupling-locus-transposition-v1-20260712.md` | memory/project_psalms_narratives_rollout_complete.md |

### I. M10c defilement cluster-report prototype (2026-09-07) → `_analytics/Clusters/M10c - defilement/`

The only analytical output for M10c.

| File | Linked from |
|---|---|
| `outputs/cluster-report-prototype-20260907/a-cluster-overview.md` | — |
| `outputs/cluster-report-prototype-20260907/b-cluster-assessment-M10c.md` | — |
| `outputs/cluster-report-prototype-20260907/c1-cluster-table-M10c.csv` | — |
| `outputs/cluster-report-prototype-20260907/c2-cluster-plus-lexical-layer1-M10c.csv` | — |

## 4. Judgement calls

### J1. M02 L2 exports from 2026-06-10 (AI verse meanings, tier findings, quality check, gate)

M02 is the live strand, but these were produced by the shelved AI verse-analysis method, and your 09-24 ruling says old findings are no longer relevant. **Recommendation: archive.** The alternative is `Clusters/M02 - anger-wrath/archive/` as labelled provenance.

- `outputs/markdown/M02-cluster-gate-20260610.md`
- `outputs/markdown/M02-meaning-quality-check-20260610.md`
- `outputs/markdown/M02-tier-wide-20260610.md`
- `outputs/markdown/M02-verse-meanings-20260610.md`

### J2. Your own notes and method reflections

program reset.md, general observations.md (a Zotero note), Passage read guidance.md, AI failures & Cognitive splitting (+2 source extracts), reading-unit-method v1/v2. These are your writing, not findings, so I will not archive them without your word. **Recommendation:** Passage read guidance and reading-unit-method v2 → `_analytics/` method notes (e.g. `_analytics/Bible_Books/_methodology/`); the rest → archive.

- `research/investigations/general observations.md`
- `research/notes/program reset.md`
- `outputs/markdown/AI failures and Cognitive splitting-20260724.md`
- `outputs/markdown/Passage read guidance.md`
- `outputs/markdown/ai-failures-source-extract-v1-20260724.md`
- `outputs/markdown/ai-failures-source-extract-v2-20260724.md`
- `outputs/markdown/reading-unit-method-characteristic-cluster-v1.md`
- `outputs/markdown/reading-unit-method-characteristic-cluster-v2.md`

### J3. Patience full DB extract (61k lines, old DB) + text search

A raw dump of the old DB. **Recommendation: archive.**

- `outputs/markdown/patience-full-db-extract-20260614.md`
- `outputs/markdown/patience-text-search-20260614.md`

## 5. Left in place (not investigations; tools write here)

These are **not moved**. Under `cfg_behaviour_rule` #60, a tool's report stays where its `cfg_setting` points: `escalation.history_report_dir` → outputs/escalation, `configmaint.report_path` → outputs/configs, `report.stage1_coverage_validation_pattern` → outputs/, `validation.output_dir`, the `content_index.*`, `research/discovery` report paths, and the cost-history ledger. Also left in place: `outputs/csv` (table exports), `outputs/markdown/project-reconstruction` (named in CLAUDE.md as authoritative background), `research/templates`, the discovery data files read by `iba/app/migration/*.py`, and the live 09-28 travel/website plan.

Noted but not in scope: `outputs/` root holds **~57 superseded Stage-1 run CSVs from 2026-09-22** (M67 test runs). They are tool output, so pruning them is a separate retention question. I can raise that as its own item.

| Folder | Files |
|---|--:|
| `outputs` | 55 |
| `outputs/configs` | 4 |
| `outputs/content_index` | 1 |
| `outputs/cost-history` | 4 |
| `outputs/cost-history/api-exports` | 3 |
| `outputs/csv` | 21 |
| `outputs/escalation` | 188 |
| `outputs/markdown/project-reconstruction` | 5 |
| `research/discovery` | 20 |
| `research/investigations` | 1 |
| `research/templates` | 3 |

## 6. Archive — process / superseded (summary)

| Source folder | Files | Typical content |
|---|--:|---|
| `outputs` | 62 | Aug–Sep 2026 pipeline audits, catalogue reviews, Stage-1/M67 test runs + logs, window1 tests, escalation-specific decision guides |
| `outputs/cc` | 3 | AI L2 tier-finding sample packets (shelved method) |
| `outputs/markdown` | 66 | Jun–Sep 2026 process reports: DB loss/backup incidents, fix plans, cfg reviews, prose searches (regenerable), M01 findings report, silent-answer audits, folder/log surveys |
| `outputs/markdown/validation` | 36 | Jun 2026 reset-era validation: faculty resets, M10/M11 cold-read validation, lexical-extension design, dossiers, spiderweb index build |
| `research/discovery` | 1 | love_step_data_20260323.md (old STEP pull) |
| `research/investigations` | 373 | Mar–Jun 2026 DB integrity, dedup, mti/VC/pointer repairs, L1/L2 design, dry-run/live logs, AI router tests (Sonnet meanings), cluster-coverage, old-method M01/M15/M26 findings |

All archived files that are linked from CLAUDE.md / `iba/app/*.md` / memory:

| File | Linked from |
|---|---|
| `research/investigations/anchor-meaning-analytics-20260604.md` | memory/project_keyword_analytics_revision_parked.md |
| `research/investigations/cluster-naming-assessment-20260521.md` | memory/feedback_cluster_file_naming_canonical.md |
| `research/investigations/dim-c01-post-patch-plan-20260420.md` | memory/project_dim_c01_post_patch_plan.md |
| `research/investigations/findings-deleted-terms-integrity-20260601.md` | memory/feedback_evidence_signal_completeness.md |
| `research/investigations/keyword-analytics-revision-plan-20260604.md` | memory/project_keyword_analytics_revision_parked.md |
| `research/investigations/pass-a-meaning-centric-direction-20260605.md` | memory/project_meaning_centric_direction_emerging.md |
| `research/investigations/session-bd-pointers-linking-20260601.md` | memory/project_pointer_lifecycle_model.md |
| `research/investigations/verse-analysis-methodology-test-20260605.md` | memory/feedback_term_corpus_anchors_meaning.md |
| `research/investigations/verse-span-cross-cluster-usage-20260605.md` | memory/feedback_span_pairing_and_reciprocal_findings.md |
| `research/investigations/wa-column-wise-ve-hypothesis-v1-20260611.md` | memory/project_column_wise_ve_hypothesis.md, memory/project_meaning_duplicates_then_fabricates.md |
| `research/investigations/wa-keyword-digestion-methodology-v1-20260608.md` | memory/feedback_keyword_digestion_methodology.md |
| `research/investigations/wa-l1-test-failure-analysis-v1-20260608.md` | memory/feedback_l1_must_be_verse_aware.md |
| `research/investigations/wa-l2-finding-schema-design-v2-20260609.md` | memory/feedback_all_study_work_in_db.md, memory/feedback_session_b_findings_resolved_through_l2.md |
| `research/investigations/wa-l2-findings-catalogue-coverage-v1-20260609.md` | memory/feedback_characteristic_is_typed_term_in_verse.md |
| `research/investigations/wa-meaning-run-yare-v1-20260608.md` | memory/project_p2_l2_decision_architecture.md |
| `research/investigations/wa-method-checkpoint-does-l1-change-the-approach-v1-20260608.md` | memory/project_method_checkpoint_v3_2_evolves_not_replaced.md |
| `research/investigations/wa-p1-keyword-rebuild-M01-v1-20260608.md` | memory/project_p2_l2_decision_architecture.md |
| `research/investigations/wa-p2-l2-decision-design-v1-20260608.md` | memory/project_p2_l2_decision_architecture.md |
| `research/investigations/wa-registry-grounding-v1-20260608.md` | memory/project_registry_words_not_all_lexically_grounded.md |
| `research/investigations/wa-step-morph-viability-M01-v1-20260608.md` | memory/project_p2_l2_decision_architecture.md |
| `research/investigations/wa-t2-cleanup-dispositions-v1-20260608.md` | memory/feedback_qualifier_routes_per_verse_occurrence.md |
| `research/investigations/wa-term-coverage-method-integrity.md` | memory/feedback_term_coverage_cascade_is_index_not_census.md |
| `research/investigations/wa-v3_2-l1-l2-architecture-synthesis-v1-20260608.md` | memory/feedback_l1_l2_is_multi_angle_report_then_synthesise.md, memory/project_all_clusters_l1_sweep_first.md |
| `research/investigations/wa-verse-read-meaning-plan-v1-20260609.md` | memory/project_l2_verse_read_meaning_live.md |
| `outputs/1706-build-session-status-v1-20260916.md` | iba/app/BUILD.md |
| `outputs/cluster-finding-to-finding-migration-plan-20260829.md` | iba/app/BUILD.md |
| `outputs/cluster-reading-pipeline-full-trace-20260920-v2.md` | iba/app/BUILD.md |
| `outputs/cluster-strong-span-verselexical-crosscheck-20260920-v2.md` | iba/app/BUILD.md |
| `outputs/finding-tables-landscape-review-20260829.md` | iba/app/BUILD.md |
| `outputs/gap-closure-design-20260921.md` | iba/app/BUILD.md |
| `outputs/m02-token-burn-review-20260929.md` | memory/project_cluster_reading_token_cost_20260929.md |
| `outputs/markdown/cluster_audit_v1_20260601.md` | memory/project_remediation_orchestrator_active.md |
| `outputs/markdown/gate1-onboarding-audit-report-20260706.md` | memory/project_per_book_corrective_pipeline.md |
| `outputs/markdown/iba-table-review-response-v1-20260816.md` | iba/app/BUILD.md |
| `outputs/markdown/log-consolidation-survey-v1-20260817.md` | iba/app/BUILD.md |
| `outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md` | iba/app/BUILD.md |
| `outputs/markdown/validation/wa-divine-involvement-grounding-audit-v1-20260626.md` | memory/feedback_lexical_strictly_verse_bounded_no_implied_evidence.md |
| `outputs/markdown/validation/wa-faculty-audit-have-we-got-the-grips-v1-20260624.md` | memory/project_faculty_not_gripped_audit_20260624.md |
| `outputs/markdown/validation/wa-faculty-state-diagnosis-v1-20260626.md` | memory/feedback_faculty_only_if_explicit_or_inferred_on_verse.md |
| `outputs/markdown/validation/wa-lexical-revelation-test-LRT-spec-v1-20260624.md` | memory/feedback_lexical_revelation_test_step3_gate.md |
| `outputs/markdown/validation/wa-overlay-bleeding-audit-and-reversals-v1-20260626.md` | memory/feedback_lexical_strictly_verse_bounded_no_implied_evidence.md |
| `outputs/markdown/validation/wa-ve-lexical-item-sanity-scan-v1-20260626.md` | memory/feedback_lexical_strictly_verse_bounded_no_implied_evidence.md |
| `outputs/markdown/wa-backup-health-check-20260621.md` | memory/project_backup_alerting_and_outlook_smtp_block.md |
| `outputs/markdown/wa-db-loss-incident-20260603.md` | CLAUDE.md, memory/project_db_loss_blocker_20260603.md, memory/reference_operational_governance_git_backup_manifest.md |
| `outputs/markdown/wa-db-recovery-assessment-20260603.md` | memory/project_db_loss_blocker_20260603.md |
| `outputs/markdown/wa-instructions-archival-proposal-20260708.md` | memory/project_lexical_cycle_finalised_and_integrity_invariant.md |
| `outputs/markdown/wa-m10-rasha-coverage-gap-20260622.md` | memory/project_step_60cap_truncation_and_forwardwalk_fix.md |
| `outputs/markdown/wa-nas-backup-failure-20260618.md` | memory/project_backup_alerting_and_outlook_smtp_block.md |
| `outputs/markdown/wa-rule-registry-full-review-v1-20260817.md` | CLAUDE.md, iba/app/BUILD.md |
| `outputs/markdown/wa-step-truncation-sweep-20260622.md` | memory/project_step_60cap_truncation_and_forwardwalk_fix.md |
| `outputs/observations-based-on-incorrect-role-20260920.md` | iba/app/GOVERNANCE.md |
| `outputs/raw-data-integrity-validation-v2-20260906.md` | memory/feedback_audit_deliverables_need_cross_check_before_presenting.md |
| `outputs/session-close-effectiveness-review-20260930.md` | iba/app/BUILD.md |
| `outputs/stage1-existing-nodes-20260922.csv` | iba/app/BUILD.md |
| `outputs/stage1-expected-nodes-20260922.csv` | iba/app/BUILD.md |
| `outputs/stage1-question-objective-review-20260923.md` | iba/app/BUILD.md |
| `outputs/verse-lexical-visibility-20260905.md` | iba/app/BUILD.md |

## Appendix — full archive list

- `research/discovery/love_step_data_20260323.md`
- `research/investigations/CLAUDE-MD-Update-Audit-20260330.md`
- `research/investigations/Corrective action for Table relatio.txt`
- `research/investigations/Session-A-v9-Empty-Words-Analysis-20260318.md`
- `research/investigations/WA-InstructionGaps-v2-20260330_1 researcher comments.md`
- `research/investigations/WA-InstructionGaps-v2_2-20260330.md`
- `research/investigations/WA-manual-test-jon4-2-H2617A-20260503.md`
- `research/investigations/action-q-path1-investigation-20260420.md`
- `research/investigations/analysis-processing-focus-20260503.md`
- `research/investigations/analysis-processing-inputs-20260503.md`
- `research/investigations/anchor-gap-profile-20260503.md`
- `research/investigations/anchor-meaning-analytics-20260604.md`
- `research/investigations/anchor-noise-with-groups-20260503.md`
- `research/investigations/applicator-hardening-rowcount-v1-20260424.md`
- `research/investigations/assessment-session-d-tables.md`
- `research/investigations/assessment-wa-cross-registry-links.md`
- `research/investigations/assessment-wa-session-b-findings.md`
- `research/investigations/assessment-wa-session-research-flags.md`
- `research/investigations/assessment-wa-term-phase2-flags.md`
- `research/investigations/audit-word-onboarding-worklist-20260708.md`
- `research/investigations/brief-meaning-router-results-claude-sonnet-4-6-20260504.json`
- `research/investigations/brief-meaning-router-results-claude-sonnet-4-6-20260504.md`
- `research/investigations/brief-meaning-router-smoke-sonnet-4-6-20260504.json`
- `research/investigations/brief-meaning-router-smoke-sonnet-4-6-20260504.md`
- `research/investigations/brief-verse-router-results-claude-sonnet-4-6-20260504.json`
- `research/investigations/brief-verse-router-results-claude-sonnet-4-6-20260504.md`
- `research/investigations/brief-verse-router-smoke-sonnet-4-6-20260504.json`
- `research/investigations/brief-verse-router-smoke-sonnet-4-6-20260504.md`
- `research/investigations/characteristic-layer-concept-20260403.md`
- `research/investigations/cluster-analysis-complete-validation-20260531.md`
- `research/investigations/cluster-audit-interpretation-20260603.md`
- `research/investigations/cluster-finding-citation-model-design-v1-20260507.md`
- `research/investigations/cluster-instruction-streamlining-audit-v1-20260514.md`
- `research/investigations/cluster-link-apply-log-20260603.md`
- `research/investigations/cluster-naming-assessment-20260521.md`
- `research/investigations/cluster-update-strategy-decision-20260601.md`
- `research/investigations/cluster_input_coverage_M01_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M02_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M03_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M04_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M06_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M07_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M08_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M09_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M15_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M20_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M26_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M38_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M39_v2_20260530.md`
- `research/investigations/cluster_input_coverage_M46_v2_20260530.md`
- `research/investigations/coverage-flags-redesign-v1-20260420.md`
- `research/investigations/cross_registry_root_analysis_20260328.png`
- `research/investigations/cross_registry_term_analysis_20260328.png`
- `research/investigations/db-capture-architecture-comparison-v1-20260427.md`
- `research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md`
- `research/investigations/db_preflight_findings.md`
- `research/investigations/deleted-but-live-terms-20260601.md`
- `research/investigations/design-decisions-summary-v1-20260419.md`
- `research/investigations/diligence-registry-investigation-v1-20260426.md`
- `research/investigations/dim-c01-phase-a-incoming-analysis-20260420.md`
- `research/investigations/dim-c01-post-patch-plan-20260420.md`
- `research/investigations/dim-label-noncanonical-rows-20260420.json`
- `research/investigations/dim-label-verse-evidence-extract-20260420.json`
- `research/investigations/dimension-index-analysis-20260404.md`
- `research/investigations/dimension-label-canonicalisation-plan-20260420.md`
- `research/investigations/empty-registry-inspection-20260503.md`
- `research/investigations/engine_dml_audit_20260322.md`
- `research/investigations/file-cleanup-plan-v1-20260423.md`
- `research/investigations/file-cleanup-tier3-plan-v1-20260423.md`
- `research/investigations/file-organisation-assessment-20260414.md`
- `research/investigations/findings-deleted-terms-integrity-20260601.md`
- `research/investigations/flag-classification-validation-20260601.md`
- `research/investigations/flag-cluster-classification-package-v1-20260601.md`
- `research/investigations/flag-cluster-worklist-20260601.md`
- `research/investigations/flag-rescue-apply-log-20260603.md`
- `research/investigations/flag-rescue-from-source-validation-20260603.md`
- `research/investigations/flag-tables-extract-joins-20260415.md`
- `research/investigations/flag-tables-listing-20260414.md`
- `research/investigations/flag_system_evaluation_20260324.md`
- `research/investigations/followon-clarifications-20260420.md`
- `research/investigations/g3958-span-survival-test-20260601.md`
- `research/investigations/ib-judgement-accepted-20260707.md`
- `research/investigations/ib-judgement-rejected-20260707.md`
- `research/investigations/incomplete-elements-register-20260601.md`
- `research/investigations/inprogress-cluster-pointers-20260601.md`
- `research/investigations/inspect_peace_registry.md`
- `research/investigations/investigation_db_only_terms_soul_20260323.md`
- `research/investigations/keyword-analytics-revision-plan-20260604.md`
- `research/investigations/keyword-bias-extract-20260604.md`
- `research/investigations/level1-tierC-risk-assessment-20260406.json`
- `research/investigations/level1-tierC-top10-verses-20260406.json`
- `research/investigations/live-dup-terms-detail-20260601.md`
- `research/investigations/m06_findings_verification_20260506.txt`
- `research/investigations/m10-finding-citation-extraction-20260525.md`
- `research/investigations/m10-h-actual-verses-input-20260605.md`
- `research/investigations/m10-h-vcg-redo-test-20260605.md`
- `research/investigations/m10-vcg-population-analytics-20260605.md`
- `research/investigations/m10d-actual-verses-input-20260605.md`
- `research/investigations/m10d-vcg-redo-test-20260605.md`
- `research/investigations/m15-doc-comparison-v1-20260530.md`
- `research/investigations/m15-dq-flag-investigation-v1-20260513.md`
- `research/investigations/m26-h2-unrouted-A1-E-v1-20260510.md`
- `research/investigations/m26-meanings-by-subject-claude-sonnet-4-6-M26-A-20260509-by-subject.md`
- `research/investigations/m26-meanings-claude-sonnet-4-6-20260509-by-term.md`
- `research/investigations/m26-meanings-claude-sonnet-4-6-20260509.jsonl`
- `research/investigations/m26-meanings-errors-claude-sonnet-4-6-20260509.jsonl`
- `research/investigations/m26-phase2-ut-router-results-claude-sonnet-4-6-20260508.json`
- `research/investigations/m26-phase3-debate-results-claude-sonnet-4-6-20260509.json`
- `research/investigations/m26-phase456-truncated-M26-A-20260509.txt`
- `research/investigations/m26-subject-claude-sonnet-4-6-M26-A-20260509.jsonl`
- `research/investigations/m39-boundary-exit-investigation-v1-20260514.md`
- `research/investigations/m39-subgroup-multi-term-design-v1-20260510.md`
- `research/investigations/m46-phase7-patch-alignment-v1-20260515.md`
- `research/investigations/m46-session-a-extraction-brief-v1-20260514.md`
- `research/investigations/manual-test-brief-briefing-20260504.md`
- `research/investigations/manual-test-brief-briefing-H3045-20260504.md`
- `research/investigations/manual-test-brief-input-100-20260504.json`
- `research/investigations/manual-test-brief-input-100-H3045-20260504.json`
- `research/investigations/manual-test-brief-verse-briefing-20260504.md`
- `research/investigations/manual-test-brief-verse-input-50-20260504.json`
- `research/investigations/manual-test-briefing-20260503.md`
- `research/investigations/manual-test-input-jon4-2-H2617A.json`
- `research/investigations/manual-test-thin-verse-briefing-20260504.md`
- `research/investigations/manual-test-thin-verse-input-50-20260504.json`
- `research/investigations/mti-dedup-investigation-20260330.md`
- `research/investigations/mti-diff-vs-backup-20260601.md`
- `research/investigations/mti-owning-registry-fk-mismatch-20260406.md`
- `research/investigations/mti-terms-dedup-design-v1-20260420.md`
- `research/investigations/mti-terms-dedup-status-20260601.md`
- `research/investigations/mti_dedup_plan_20260330.csv`
- `research/investigations/mti_orphans_20260330.csv`
- `research/investigations/mti_terms_full_20260330.csv`
- `research/investigations/multi_owner_terms_20260330.csv`
- `research/investigations/no-primary-registries-detail-20260503.md`
- `research/investigations/open-items-currency-and-table-disposition-20260614.md`
- `research/investigations/orphan-old-vcg-dissolution-audit-20260601.md`
- `research/investigations/orphan_flags_audit.csv`
- `research/investigations/orphaned_verses_check.md`
- `research/investigations/ot-lemmas-unmatched-20260707.md`
- `research/investigations/pass-a-meaning-centric-direction-20260605.md`
- `research/investigations/per-bucket-strongs-profile-20260503.md`
- `research/investigations/pointer-cluster-link-redo-scope-20260603.md`
- `research/investigations/pointer-full-linkage-20260601.md`
- `research/investigations/pointer-nolink-retention-20260601.md`
- `research/investigations/pos-noise-crosstab-20260503.json`
- `research/investigations/pos-noise-crosstab-20260503.md`
- `research/investigations/pos-noise-set-aside-preflight-20260503.md`
- `research/investigations/post_fix_script_review.md`
- `research/investigations/programme-prose-session-bundle-v1-20260421.md`
- `research/investigations/programme-prose-structure-design-v1-20260421.md`
- `research/investigations/programme-prose-v2-recommendations-v1-20260427.md`
- `research/investigations/programme-snapshot-20260427.md`
- `research/investigations/prose-in-sqlite-advice-v1-20260419.md`
- `research/investigations/prose-instructions-compatibility-review-v1-20260421.md`
- `research/investigations/publishing_input_audit_v2_findings_20260530.md`
- `research/investigations/publishing_readiness_cleanup_summary_20260530.md`
- `research/investigations/publishing_readiness_programme_v1_20260530.md`
- `research/investigations/redundant-report-version-sweep-20260601.md`
- `research/investigations/reference-as-database-design-20260420.md`
- `research/investigations/reference-as-database-framework-execution-20260420.md`
- `research/investigations/remaining-terms-categorised-20260402.csv`
- `research/investigations/repair-bd-noreason-backfill-20260601.md`
- `research/investigations/repair-delete-flag-desync-20260601.md`
- `research/investigations/repair-span-terms-to-flag-20260601.md`
- `research/investigations/repair-span-terms-to-flag-apply-20260603.md`
- `research/investigations/rescue-physical-setaside-20260604.md`
- `research/investigations/rollback-comment-eval-fragmentation-20260603.md`
- `research/investigations/schema-change-impact-report-20260415.md`
- `research/investigations/schema-impact-review-scripts-20260415.md`
- `research/investigations/sense-sampling-walkthrough-20260328.md`
- `research/investigations/session-a-extract-section-types-advice-v1-20260419.md`
- `research/investigations/session-a-prose-for-vc-input-analysis-v1-20260423.md`
- `research/investigations/session-bd-pointers-assessment-20260601.md`
- `research/investigations/session-bd-pointers-content-mining-20260601.md`
- `research/investigations/session-bd-pointers-linking-20260601.md`
- `research/investigations/session-c-cluster-design-v4-20260512.md`
- `research/investigations/sessionb-cluster-api-automation-feasibility-v1-20260508.md`
- `research/investigations/sessionb-export-spec-verification-20260415.md`
- `research/investigations/soul_phase2_root_cause_analysis.md`
- `research/investigations/soul_step_routes_20260323_063217.md`
- `research/investigations/special-status-terms-20260406.json`
- `research/investigations/stale-version-scan-v1-20260426.md`
- `research/investigations/step-extract-archive-plan-20260423.md`
- `research/investigations/step-extract-coverage-20260423.md`
- `research/investigations/step-pos-extractor-run-20260503.log`
- `research/investigations/step-pos-lookup-20260503.json`
- `research/investigations/step_api_findings_20260323.md`
- `research/investigations/subprocess-cohort-framework-v1-20260420.md`
- `research/investigations/task5-zero-term-investigation-20260327.md`
- `research/investigations/term-G2285-thambos-verbatim-20260601.md`
- `research/investigations/term-disposition-by-span-20260601.md`
- `research/investigations/term-introduction-classification-proposals-20260420.md`
- `research/investigations/term-primacy-tiering-20260503.json`
- `research/investigations/term-primacy-tiering-20260503.md`
- `research/investigations/term_sharing_network_20260328.png`
- `research/investigations/thin-verse-router-H3034-results-claude-sonnet-4-6-20260504.json`
- `research/investigations/thin-verse-router-H3034-results-claude-sonnet-4-6-20260504.md`
- `research/investigations/thin-verse-router-H4191-results-claude-sonnet-4-6-20260504.json`
- `research/investigations/thin-verse-router-H4191-results-claude-sonnet-4-6-20260504.md`
- `research/investigations/thin-verse-router-results-claude-sonnet-4-6-20260504.json`
- `research/investigations/thin-verse-router-results-claude-sonnet-4-6-20260504.md`
- `research/investigations/tier-question-linkage-analysis-v1-20260507.md`
- `research/investigations/today-writes-severity-20260601.md`
- `research/investigations/unclassified-sample-100-pairs-20260504.json`
- `research/investigations/unclassified-sample-100-pairs-H3045-20260504.json`
- `research/investigations/unclassified-verse-sample-50-verses-20260504.json`
- `research/investigations/unclassified-verse-sample-50-verses-H3034-20260504.json`
- `research/investigations/unclassified-verse-sample-50-verses-H4191-20260504.json`
- `research/investigations/unclustered-no-reason-terms-bd-detail-20260601.md`
- `research/investigations/unclustered-outstanding-items-20260601.md`
- `research/investigations/unclustered-terms-remediation-plan.md`
- `research/investigations/undelete-candidates-20260601.md`
- `research/investigations/v5-impact-assessment-20260327.md`
- `research/investigations/validity-checking-status-20260423.md`
- `research/investigations/vc-corrective-strategy-v2-20260426.md`
- `research/investigations/vc-four-patch-design-v1-20260424.md`
- `research/investigations/vc-instruction-session-a-md-alignment-v4-20260424.md`
- `research/investigations/vc-quality-flags-practical-view-v1-20260426.md`
- `research/investigations/vc-revision-ledger-v1-20260425.csv`
- `research/investigations/vc-revision-ledger-v1-20260425.md`
- `research/investigations/vc-session-output-model-v1-20260424.md`
- `research/investigations/vc-strategy-pivot-proposal-v1-20260426.md`
- `research/investigations/vc-v3_1-ambiguities-needing-researcher-decision-v1-20260424.md`
- `research/investigations/vc-v3_5-instruction-amendment-v1-20260424.md`
- `research/investigations/vcb-009-state-verification-20260402.md`
- `research/investigations/vcb-011-batch-prep-20260425.md`
- `research/investigations/vcb-012-batch-prep-20260425.md`
- `research/investigations/vcb-013-batch-prep-20260425.md`
- `research/investigations/verse-analysis-methodology-test-20260605.md`
- `research/investigations/verse-context-per-verse-walkthrough-20260503.md`
- `research/investigations/verse-context-records-sample-20260503.json`
- `research/investigations/verse-dup-current-20260601.md`
- `research/investigations/verse-gap-by-term-20260503.json`
- `research/investigations/verse-gap-by-term-20260503.md`
- `research/investigations/verse-meaning-keyword-instructions-v29-v30-extract-20260605.md`
- `research/investigations/verse-meaning-router-results-20260503.json`
- `research/investigations/verse-meaning-router-results-20260503.md`
- `research/investigations/verse-meaning-router-results-sonnet-4-6-20260503.json`
- `research/investigations/verse-meaning-router-results-sonnet-4-6-20260503.md`
- `research/investigations/verse-span-cross-cluster-usage-20260605.md`
- `research/investigations/verse-term-registry-profile-20260503.md`
- `research/investigations/verses_gen24_21.csv`
- `research/investigations/wa-a1-corroboration-m01-results-and-method-v1-20260607.md`
- `research/investigations/wa-a1-corroboration-scan-m01-v1-20260607.md`
- `research/investigations/wa-a1-verse-meaning-corroboration-m01-ademoneo-v1-20260607.md`
- `research/investigations/wa-characteristic-distillation-design-v1-20260609.md`
- `research/investigations/wa-column-wise-ve-hypothesis-v1-20260611.md`
- `research/investigations/wa-corpus-keyword-map-v1-20260608.csv`
- `research/investigations/wa-corpus-keyword-map-v1-20260608.md`
- `research/investigations/wa-corpus-keyword-typed-v1-20260608.csv`
- `research/investigations/wa-corpus-keyword-typed-v1-20260608.md`
- `research/investigations/wa-d1-excluded-cascade-dryrun-v1-20260615.md`
- `research/investigations/wa-d1-excluded-cascade-live-v1-20260615.md`
- `research/investigations/wa-d1-excluded-cascade-live-v1-20260615.md.ids.json`
- `research/investigations/wa-d2a-link-dryrun-v1-20260615.md`
- `research/investigations/wa-d2a-link-live-v1-20260615.md`
- `research/investigations/wa-d2a-link-live-v1-20260615.md.ids.json`
- `research/investigations/wa-d2b-a-orphan-softdelete-v1-20260615.md`
- `research/investigations/wa-d2b-a-orphan-softdelete-v1-20260615.md.ids.json`
- `research/investigations/wa-d2b-unregistered-terms-decision-v1-20260615.md`
- `research/investigations/wa-db-architecture-decision-v1-20260505.md`
- `research/investigations/wa-file-index-onboarding-assessment-v1-20260615.md`
- `research/investigations/wa-finding-lifecycle-run-v1-20260609.md`
- `research/investigations/wa-finding-lifecycle-synthesis-v1-20260609.md`
- `research/investigations/wa-fk-audit-and-proposal-v1-20260505.md`
- `research/investigations/wa-flag-triage-moves-dryrun-v1-20260610.md`
- `research/investigations/wa-flag-triage-moves-v1-20260610.md`
- `research/investigations/wa-flag-triage-v1-20260610.md`
- `research/investigations/wa-global-database-review-design-v1-20260419.md`
- `research/investigations/wa-global-readiness-sweep-design-v1-20260419.md`
- `research/investigations/wa-h2-16anomalies-A.ids.json`
- `research/investigations/wa-h2-delete-marked-cluster-anomalies-decision-v1-20260615.md`
- `research/investigations/wa-keyword-corpus-assessment-v1-20260608.md`
- `research/investigations/wa-keyword-digestion-methodology-v1-20260608.md`
- `research/investigations/wa-l1-prototype-findings-and-r-decisions-v1-20260607.md`
- `research/investigations/wa-l1-prototype-m01-m02-comparison-v1-20260607.md`
- `research/investigations/wa-l1-prototype-r7-morph-m01-m02-v1-20260607.md`
- `research/investigations/wa-l1-sweep-prelaunch-state-and-rollback-v1-20260608.md`
- `research/investigations/wa-l1-test-failure-analysis-v1-20260608.md`
- `research/investigations/wa-l2-finding-schema-design-v1-20260609.md`
- `research/investigations/wa-l2-finding-schema-design-v2-20260609.md`
- `research/investigations/wa-l2-findings-catalogue-coverage-v1-20260609.md`
- `research/investigations/wa-l2-findings-view-M15-M10-M26-v1-20260609.md`
- `research/investigations/wa-l2-findings-view-M15-M10-M26-v2-20260609.md`
- `research/investigations/wa-l2-refit-M01-live-v1-20260609.md`
- `research/investigations/wa-l2-refit-M15-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-refit-M15-live-v1-20260609.md`
- `research/investigations/wa-l2-rollup-m01-v1-20260609.md`
- `research/investigations/wa-l2-rollup-m15-v1-20260609.md`
- `research/investigations/wa-l2-triage-yare-v1-20260609.md`
- `research/investigations/wa-l2-write-M10-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-M23-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-M25-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-M44-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-batch1-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-batch1-live-v1-20260609.md`
- `research/investigations/wa-l2-write-m01-versecomplete-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-m01-versecomplete-live-v1-20260609.md`
- `research/investigations/wa-l2-write-m01full-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-m01full-live-v1-20260609.md`
- `research/investigations/wa-l2-write-m15-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-m15-live-v1-20260609.md`
- `research/investigations/wa-l2-write-m15-versecomplete-dryrun-v1-20260609.md`
- `research/investigations/wa-l2-write-m15-versecomplete-live-v1-20260609.md`
- `research/investigations/wa-language-testament-consistency-check-v1-20260615.md`
- `research/investigations/wa-m-tables-dependencies-v1-20260505.md`
- `research/investigations/wa-m01-assembly-batch1-v1-20260608.md`
- `research/investigations/wa-m01-findings-batch1-v1-20260608.md`
- `research/investigations/wa-m01-findings-store-v1-20260609.json`
- `research/investigations/wa-m01-findings-store-v2-20260609.json`
- `research/investigations/wa-mar722-g5243-dedup.ids.json`
- `research/investigations/wa-meaning-run-yare-v1-20260608.md`
- `research/investigations/wa-method-checkpoint-does-l1-change-the-approach-v1-20260608.md`
- `research/investigations/wa-migration-control-integrity-v1-20260607.md`
- `research/investigations/wa-mode-consistency-check-v1-20260615.md`
- `research/investigations/wa-morph-backfill-M01-dryrun-v1-20260608.md`
- `research/investigations/wa-morph-backfill-M01-live-v1-20260608.md`
- `research/investigations/wa-morph-backfill-batch2-v1-20260608.md`
- `research/investigations/wa-morph-backfill-batch3-v1-20260608.md`
- `research/investigations/wa-morph-backfill-batch4-v1-20260608.md`
- `research/investigations/wa-morph-backfill-catchup-live-v1-20260614.md`
- `research/investigations/wa-morph-backfill-gap-programme-wide-v1-20260614.md`
- `research/investigations/wa-morph-targeted-newlylinked-v1-20260615.md`
- `research/investigations/wa-mti-duplicate-terms-v1-20260609.md`
- `research/investigations/wa-p1-keyword-rebuild-M01-v1-20260608.md`
- `research/investigations/wa-p2-l2-decision-design-v1-20260608.md`
- `research/investigations/wa-p2-l2-scenario-typing-M01-v1-20260608.md`
- `research/investigations/wa-prose-store-design-v1-20260419.md`
- `research/investigations/wa-qa-method-effectiveness-20260428.json`
- `research/investigations/wa-qa-method-effectiveness-20260428.md`
- `research/investigations/wa-qa-method-triage-20260428.md`
- `research/investigations/wa-qa-quality-review-20260428.json`
- `research/investigations/wa-qa-quality-review-20260428.md`
- `research/investigations/wa-r211-orphan-cleanup-v1-20260615.md`
- `research/investigations/wa-r211-orphan-cleanup-v1-20260615.md.ids.json`
- `research/investigations/wa-read-dedup-estimate-v1-20260609.md`
- `research/investigations/wa-registry-grounding-v1-20260608.md`
- `research/investigations/wa-registry-vs-keywords-v1-20260608.md`
- `research/investigations/wa-row-level-completeness-prerebuild-v1-20260607.md`
- `research/investigations/wa-sb-finding-migration-v1-20260609.md`
- `research/investigations/wa-scaling-design-and-layers-v1-20260608.md`
- `research/investigations/wa-sessionb-cluster-instruction-v2_5-DRAFT-20260518.md`
- `research/investigations/wa-sessionb-cluster-instruction-v2_5-DRAFT-changes-summary-20260518.md`
- `research/investigations/wa-sessionb-v1_6-instruction-alignment-review-20260430.md`
- `research/investigations/wa-sessionb-v1_8-stage2c-compliance-20260430.md`
- `research/investigations/wa-softdelete-excluded-empty-terms-v1-20260615.md.ids.json`
- `research/investigations/wa-step-morph-viability-M01-v1-20260608.md`
- `research/investigations/wa-step-morphology-sense-disambiguation-v1-20260607.md`
- `research/investigations/wa-t2-cleanup-dispositions-v1-20260608.md`
- `research/investigations/wa-t2-flag-sample-v1-20260609.md`
- `research/investigations/wa-t2-relevance-surface-scan-v1-20260607.md`
- `research/investigations/wa-t2-relevance-surface-v1-20260607.md`
- `research/investigations/wa-t2-soft-delete-list-v1-20260608.md`
- `research/investigations/wa-task1-term-dedup-dryrun-v1-20260607.md`
- `research/investigations/wa-term-coverage-method-integrity.md`
- `research/investigations/wa-term-orphan-integration-build.md`
- `research/investigations/wa-term-type-classification-v1-2026-05-04.json`
- `research/investigations/wa-termsense-ranking-v1-20260609.md`
- `research/investigations/wa-v3_2-l1-l2-architecture-synthesis-v1-20260608.md`
- `research/investigations/wa-verse-extraction-gaps-v1-20260610.md`
- `research/investigations/wa-verse-read-M01-full-run-20260609.log`
- `research/investigations/wa-verse-read-M01-review-v1-20260609.md`
- `research/investigations/wa-verse-read-M15-full-run-20260609.log`
- `research/investigations/wa-verse-read-M15-gate-v1-20260609.md`
- `research/investigations/wa-verse-read-meaning-plan-v1-20260609.md`
- `research/investigations/wa-verse-read-pilot-dryrun-pachad-v1-20260609.txt`
- `research/investigations/wa-verse-read-pilot-live-M01-run-20260609.log`
- `research/investigations/wa-verse-read-pilot-review-M01-v1-20260609.md`
- `research/investigations/wa-verse-uniqueness-cleanup-v1-20260615.md.ids.json`
- `research/investigations/wa-xref-verse-duplication-blocker-v1-20260615.md`
- `research/investigations/wa_file_index_export.csv`
- `research/investigations/wa_term_inventory_full_20260330.csv`
- `research/investigations/wa_verse_records_refs_inspect.csv`
- `research/investigations/wr19_parse_warnings_soul_20260323.md`
- `outputs/1605-37-t2-vs-m-code-review-20260909.csv`
- `outputs/1706-build-session-status-v1-20260916.md`
- `outputs/1753-decision-guide-20260918-v2.md`
- `outputs/1766-soft-delete-purge-audit-20260918-v2.md`
- `outputs/cascade-softdelete-discrepancies-20260924.md`
- `outputs/catalogue-coverage-audit-20260921-v5.csv`
- `outputs/catalogue-coverage-audit-20260921-v5.md`
- `outputs/catalogue-question-wording-review-20260921-v8.csv`
- `outputs/catalogue-question-wording-review-20260921-v8.md`
- `outputs/cc/cc_output.md`
- `outputs/cc/cc_packets.md`
- `outputs/cc/cc_packets.md.map`
- `outputs/cluster-finding-to-finding-migration-plan-20260829.md`
- `outputs/cluster-population-vs-observations-20260921-v3.csv`
- `outputs/cluster-reading-pipeline-full-trace-20260920-v2.md`
- `outputs/cluster-strong-span-verselexical-crosscheck-20260920-v2.md`
- `outputs/escalation-history-catalogue-20260904.md`
- `outputs/finding-tables-landscape-review-20260829.md`
- `outputs/flag-type-question-catalogue-review-20260829.md`
- `outputs/folder-census-20260828.csv`
- `outputs/folder-purpose-export-20260828.csv`
- `outputs/gap-closure-design-20260921.md`
- `outputs/m02-token-burn-review-20260929.md`
- `outputs/m67-full-backfill-20260922.log`
- `outputs/m67-wordlevel-BEFORE-20260923.csv`
- `outputs/m67-wordlevel-BEFORE-20260923.json`
- `outputs/m67-wordlevel-full-force-run-20260923.json`
- `outputs/m67-wordlevel-full-force-run-resume1-20260923.json`
- `outputs/m67-wordlevel-remaining23-resume2-20260923.json`
- `outputs/m67-wordlevel-remaining25-resume1-20260923.json`
- `outputs/m67-wordlevel-remaining25-run-20260923.json`
- `outputs/markdown/1682-findings-table-design-options-v1-20260911.md`
- `outputs/markdown/1682-m10-family-vs-legacy-subgroup-comparison-v1-20260912.md`
- `outputs/markdown/1683-m10-legacy-data-hard-delete-scope-v1-20260912.md`
- `outputs/markdown/1706-stage1-prompt-visibility-v1-20260917.md`
- `outputs/markdown/L1-L2-design-vs-measured-gap-20260614.md`
- `outputs/markdown/L1-catalogue-signoff-document-index-20260614.md`
- `outputs/markdown/_silent_inventory_working.json`
- `outputs/markdown/analysis-phase-stream-robustness-assessment-20260828.md`
- `outputs/markdown/cfg-quality-check-null-enforced-by-review-v1-20260830.md`
- `outputs/markdown/cfg-review-session-capture-20260830.md`
- `outputs/markdown/cfg-table-purpose-success-review-v1-20260830.md`
- `outputs/markdown/cluster-processing-timing-20260610.md`
- `outputs/markdown/cluster_audit_v1_20260601.md`
- `outputs/markdown/consolidated-sessions-folder-design-v6-20260827.md`
- `outputs/markdown/drop-code-findings-extract-20260611.csv`
- `outputs/markdown/drop-code-findings-extract-20260611.md`
- `outputs/markdown/folder-analytic-file-management-analysis-v2-20260827.md`
- `outputs/markdown/gate1-onboarding-audit-report-20260706.md`
- `outputs/markdown/grace-prose-search-20260814.md`
- `outputs/markdown/iba-table-review-response-v1-20260816.md`
- `outputs/markdown/lexical-verse-lexical-status-and-open-items-20260914.md`
- `outputs/markdown/log-consolidation-survey-v1-20260817.md`
- `outputs/markdown/m-vs-r-divergence-20260611.csv`
- `outputs/markdown/m-vs-r-divergence-20260611.md`
- `outputs/markdown/m-vs-r-divergence-interpretation-20260611.md`
- `outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md`
- `outputs/markdown/programme-control-gap-diagnosis-v1-20260830.md`
- `outputs/markdown/project-review-response-2-20260815.md`
- `outputs/markdown/project-review-response-20260815.md`
- `outputs/markdown/project-sanity-check-20260815.md`
- `outputs/markdown/prose-search-grace-20260821.md`
- `outputs/markdown/prose-search-grace-findings-20260814.md`
- `outputs/markdown/prose-search-grace-or-love-20260814.md`
- `outputs/markdown/prose-search-grace-programme-20260814.md`
- `outputs/markdown/prose-search-inner-being-20260821.md`
- `outputs/markdown/table-reconciliation-extract-v1-20260827.md`
- `outputs/markdown/validation/wa-10-random-verses-full-detail-v1-20260626.md`
- `outputs/markdown/validation/wa-4-focus-verses-dossier-v1-20260627.md`
- `outputs/markdown/validation/wa-M12-dissection-pilot-review-v1-20260625.md`
- `outputs/markdown/validation/wa-autonomous-progress-log-lexical-refinement-20260624.md`
- `outputs/markdown/validation/wa-baseline-dataset-status-v1-20260627.md`
- `outputs/markdown/validation/wa-cross-cluster-structure-lessons-m12-m13-m14-v1-20260624.md`
- `outputs/markdown/validation/wa-divine-involvement-grounding-audit-v1-20260626.md`
- `outputs/markdown/validation/wa-exegesis-gate-drycount-v1-20260626.md`
- `outputs/markdown/validation/wa-faculty-audit-have-we-got-the-grips-v1-20260624.md`
- `outputs/markdown/validation/wa-faculty-reset-dryrun-v1-20260626.md`
- `outputs/markdown/validation/wa-faculty-reset-outcome-v1-20260626.md`
- `outputs/markdown/validation/wa-faculty-state-diagnosis-v1-20260626.md`
- `outputs/markdown/validation/wa-layer1-286-annotated-v1-20260627.md`
- `outputs/markdown/validation/wa-layer1-simplest-286-verses-v1-20260627.md`
- `outputs/markdown/validation/wa-lexical-discovery-register-v1-20260624.md`
- `outputs/markdown/validation/wa-lexical-extension-deepdive-into-01b-DESIGN-v1-20260624.md`
- `outputs/markdown/validation/wa-lexical-extension-model-v2-with-additions-20260624.md`
- `outputs/markdown/validation/wa-lexical-extension-rerun-and-compound-design-v1-20260624.md`
- `outputs/markdown/validation/wa-lexical-revelation-test-LRT-spec-v1-20260624.md`
- `outputs/markdown/validation/wa-m03-m09-deviation-diagnostic-v1-20260624.md`
- `outputs/markdown/validation/wa-m10-m11-coldread-validation-framework-and-foundation-v1-20260624.md`
- `outputs/markdown/validation/wa-m10-m11-validation-MASTER-synthesis-v1-20260624.md`
- `outputs/markdown/validation/wa-m10-validation-characteristic-condition-v1-20260624.md`
- `outputs/markdown/validation/wa-m10-validation-expression-mechanism-remedy-agency-v1-20260624.md`
- `outputs/markdown/validation/wa-m10-validation-record-identity-v1-20260624.md`
- `outputs/markdown/validation/wa-m10-validation-structure-and-unit-distinctions-v1-20260624.md`
- `outputs/markdown/validation/wa-m11-validation-report-v1-20260624.md`
- `outputs/markdown/validation/wa-overlay-bleeding-audit-and-reversals-v1-20260626.md`
- `outputs/markdown/validation/wa-reset-evaluation-and-synthesis-gap-v1-20260624.md`
- `outputs/markdown/validation/wa-reset-rollout-db-concern-tracker-v1-20260625.md`
- `outputs/markdown/validation/wa-reset-sweep-outcome-and-honest-assessment-v1-20260626.md`
- `outputs/markdown/validation/wa-step-extract-multicode-resolver-bug-v1-20260713.md`
- `outputs/markdown/validation/wa-term-morph-roles-G5485_H2603-20260627.md`
- `outputs/markdown/validation/wa-ve-lexical-item-sanity-scan-v1-20260626.md`
- `outputs/markdown/validation/wa-ve-reset-fidelity-fixes-validation-v1-20260625.md`
- `outputs/markdown/validation/wa-verse-evidence-spiderweb-index-v1-20260627.md`
- `outputs/markdown/ve-by-cluster-20260610.md`
- `outputs/markdown/wa-M01-term-verse-findings-report-v1-20260609.md`
- `outputs/markdown/wa-backup-alerting-plan-v1-20260618.md`
- `outputs/markdown/wa-backup-health-check-20260621.md`
- `outputs/markdown/wa-cluster-setaside-status-v1-20260620.md`
- `outputs/markdown/wa-db-loss-incident-20260603.md`
- `outputs/markdown/wa-db-recovery-assessment-20260603.md`
- `outputs/markdown/wa-findings-capture-model-proposal-v1-20260619.md`
- `outputs/markdown/wa-findings-supersede-and-capture-completion-v1-20260619.md`
- `outputs/markdown/wa-findings-supersede-and-capture-plan-v1-20260619.md`
- `outputs/markdown/wa-instructions-archival-proposal-20260708.md`
- `outputs/markdown/wa-isa43-1-2-ve-lexical-morphology-dump-20260705.md`
- `outputs/markdown/wa-language-derivation-bug-fix-plan-v1-20260615.md`
- `outputs/markdown/wa-location-by-cluster-summary-20260618.md`
- `outputs/markdown/wa-location-engine-fix-plan-v1-20260618.md`
- `outputs/markdown/wa-m01-findings-capture-plan-v1-20260619.md`
- `outputs/markdown/wa-m10-rasha-coverage-gap-20260622.md`
- `outputs/markdown/wa-morph-at-source-fix-plan-v1-20260615.md`
- `outputs/markdown/wa-nas-backup-failure-20260618.md`
- `outputs/markdown/wa-programme-database-functional-pool-relatedness-assessment-20260714.md`
- `outputs/markdown/wa-programme-database-functional-pools-20260714.md`
- `outputs/markdown/wa-programme-database-overview-20260714.md`
- `outputs/markdown/wa-rule-registry-full-review-v1-20260817.md`
- `outputs/markdown/wa-session-close-report-20260602.md`
- `outputs/markdown/wa-silent-answers-by-cluster-char-v1-20260621.md`
- `outputs/markdown/wa-silent-answers-why-expected-v1-20260621.md`
- `outputs/markdown/wa-softdelete-integrity-hardening-plan-v1-20260615.md`
- `outputs/markdown/wa-step-truncation-sweep-20260622.md`
- `outputs/markdown/wa-tier-catalogue-refit-patch-review-v1-20260619.md`
- `outputs/markdown/wa-ve-signal-list-audit-and-rerun-v1-20260619.md`
- `outputs/mcode-cluster-final-assessment-20260907.md`
- `outputs/observation-counts-by-question-20260920-v2.md`
- `outputs/observation-counts-by-question-20260920.csv`
- `outputs/observations-based-on-incorrect-role-20260920.csv`
- `outputs/observations-based-on-incorrect-role-20260920.md`
- `outputs/pipeline-wiring-audit-20260921-v4.csv`
- `outputs/pipeline-wiring-audit-20260921-v4.md`
- `outputs/population-vs-observations-density-20260921-v3.md`
- `outputs/raw-data-integrity-validation-v2-20260906.md`
- `outputs/session-close-effectiveness-review-20260930.md`
- `outputs/stage1-batch-RUN-20260922_081511_226-STAGE1-BATCH.csv`
- `outputs/stage1-batch-RUN-20260922_165226_097-STAGE1-BATCH.csv`
- `outputs/stage1-batch-RUN-20260922_165235_253-STAGE1-BATCH.csv`
- `outputs/stage1-batch-RUN-20260922_191407_609-STAGE1-BATCH.csv`
- `outputs/stage1-batch-RUN-20260922_191434_564-STAGE1-BATCH.csv`
- `outputs/stage1-existing-nodes-20260922.csv`
- `outputs/stage1-expected-nodes-20260922.csv`
- `outputs/stage1-expected-vs-existing-comparison-20260922.csv`
- `outputs/stage1-observations-by-question-M67-5verse-20260922.csv`
- `outputs/stage1-observations-by-question-M67-5verse-20260922.md`
- `outputs/stage1-question-objective-review-20260923.md`
- `outputs/stage1-questions-20260922.csv`
- `outputs/stage1-verse-by-verse-review-M67-5verse-20260922.md`
- `outputs/strong-population-vs-observations-20260921-v3.csv`
- `outputs/subgroup-population-vs-observations-20260921-v3.csv`
- `outputs/t4-t9-cluster-membership-20260909.csv`
- `outputs/verse-lexical-visibility-20260905.md`
- `outputs/verse-reading-observations-exposed-to-contaminated-role-20260920.csv`
- `outputs/verse-reading-observations-exposed-to-contaminated-role-20260920.md`
- `outputs/window1-10verse-verse_lexical-20260905-v4.csv`
- `outputs/window1-10verse-verse_lexical_note-20260905-v3.csv`
- `outputs/window1-layer1-layer2-design-vs-code-vs-results-20260905.md`
- `outputs/window1-layer1-layer2-review-20260905-v3.md`
- `outputs/window1-layer2-10verse-test-20260905-v2.md`
