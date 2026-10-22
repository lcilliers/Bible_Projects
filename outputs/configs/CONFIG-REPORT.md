# IBA app — configuration report

> **Generated snapshot of the live config store** (`iba/app/db/iba.db`, tables `cfg_*`). The DB is master — do not hand-edit this file. Change config only via `configmaint.propose` (approval-gated; see GOVERNANCE.md §5A); this report regenerates automatically after an approved change and is overwritten in place.

| field | value |
| --- | --- |
| database | iba |
| config_version | app-0.1.0 |
| generated_at | 2026-10-22T14:44:31Z |
| current_seed_hash | bootstrap:configuration-maintenance-2026-07-21 |

## Contents

- [0. Findings — needing researcher judgement](#0-findings-needing-researcher-judgement)
- [1. Inactive configs — historical record, not a decision](#1-inactive-configs-historical-record-not-a-decision)
- [2. Utilities registry](#2-utilities-registry)
- [3. Connection (STEP)](#3-connection-step)
- [4. Settings — every rule / threshold, grouped by owning module](#4-settings-every-rule-threshold-grouped-by-owning-module)
- [5. STEP apis](#5-step-apis)
- [6. Work packages & steps (the sequence)](#6-work-packages-steps-the-sequence)
- [7. on_fail — condition -> path (the fork rules)](#7-on-fail-condition-path-the-fork-rules)
- [8. Write grants — who may write what](#8-write-grants-who-may-write-what)
- [9. Status flow](#9-status-flow)
- [10. Schema — data tables built from config](#10-schema-data-tables-built-from-config)
- [11. Enums](#11-enums)
- [12. Book order](#12-book-order)
- [13. Change-log — every accepted load (audit)](#13-change-log-every-accepted-load-audit)
- [Reports — full governance per report](#14-reports-full-governance-per-report)
- [15. Control map — one home per kind of control](#15-control-map-one-home-per-kind-of-control)

<a id="0-findings-needing-researcher-judgement"></a>
## 0. Findings — needing researcher judgement

_Computed fresh on every regenerate — the full detail behind `configmaint.validate`'s escalation, which references this section by path rather than repeating it. Not errors — advisory. See GOVERNANCE.md §5B._ Items are numbered (running count across every category below) so any one item can be referenced by number, e.g. "item 7" — the numbering is a snapshot of THIS regenerate, not a stable ID across runs. Historical/already-decided records (inactive configs) are §1, not here — everything below is something that actually needs your judgement.

**Orphan configs** (0) — a `cfg_setting`/`cfg_enum` not referenced by any code:
_(none)_

**Settings needing justification** (0) — module already has its own dedicated table:
_(none)_

**Missing report paths** (0) — a quality-check step with nowhere for its findings to persist (governance.reports_must_persist violation):
_(none)_

**Stale filled_by** (0) — cfg_column.filled_by names a now-inactive step:
_(none)_

**Unregistered lib modules** (0) — iba/app/lib/*.py with no cfg_utility row:
_(none)_

**Low config-density utilities** (0) — NON-EXEMPT cfg_utility module with zero real Cfg-method call sites of its own (see §2 Utilities registry for the full module list, including the 11 already declared config_exempt):
_(none)_

**Orphan book_order** (0) — cfg.book_order() unused, or a duplicate book/ordinal:
_(none)_

**Orphan connection keys** (0) — a cfg_connection key not read via cfg.connection(...) anywhere:
_(none)_

**Orphan candidate rules** (0) — a kind called with zero active rows, or active rows no code asks for:
_(none)_

**Report version clutter** (0) — more than one version of a one-off report simultaneously live in governance.oneoff_report_dir (oneoff_path() found 2026-08-08 to version without archiving, BUILD.md §83) — the rest belong in archive/:
_(none)_

**Unresolvable location settings** (0) — a *_dir/*_path/*_folder value (cfg_setting or any per-module table shaped like it) that does not resolve to a real folder on disk:
_(none)_

**Escalation.ps1 ValidateSet drift** (0) — a -Parameter's [ValidateSet(...)] values not matching the live cfg_enum group it's supposed to mirror:
_(none)_

**FolderPurpose.ps1 ValidateSet drift** (0) — same check, for -Type/-Status against folder_purpose_type/folder_purpose_status:
_(none)_

**Hand-rolled versioning** (1) — a script building a -v{n} filename by hand instead of via filingkit.versioned_path()/reportkit.oneoff_path():
1. iba/app/lib/narrativeregister.py builds a -v{n} filename by hand — no filingkit.versioned_path()/reportkit.oneoff_path() call site in the same file

**PS/worksheet drift** (0) — a script's live param() names not matching its tab's flag headers in governance.ps_worksheet_path:
_(none)_

**Escalation.ps1/worksheet drift** (0) — an Escalation.ps1 parameter not used as a -Flag header anywhere in governance.escalation_worksheet_path:
_(none)_

**Unenforced behaviour rules** (13) — an active cfg_behaviour_rule row whose enforcement_status is neither mechanically_enforced nor context_delivered (the compliance file restates and proves those) — see the row's own enforced_by text for the reason:
2. [chat] #74 open-threads-carried-as-escalations — partially_enforced
3. [chat] #76 narrative-claim-register-kept-in-iba-db — partially_enforced
4. [chat] #81 session-compliance-restated-and-proved — partially_enforced
5. [chat] #82 session-close-blocks-commit-on-open-findings — partially_enforced
6. [development] #46 test-plan-per-module-utility — deliberately_deferred
7. [development] #66 cluster-label-must-track-membership — buildable_not_built
8. [development] #97 developer-mode-scope-and-conduct — partially_enforced
9. [documentation] #32 no-hedge-in-complete-records — partially_enforced
10. [filing] #56 naming-shape — partially_enforced
11. [filing] #58 archiving-trigger — partially_enforced
12. [filing] #60 tool-report-path-vs-deliverable-document — buildable_not_built
13. [sqlite] #68 stage1-corrections-only-via-real-rerun — buildable_not_built
14. [sqlite] #78 narrative-chapters-change-only-through-the-register — partially_enforced

**Unpushed commits** (0) — a local commit not yet pushed to the upstream branch:
_(none)_

**PS scripts bypassing run.py** (0) — an active PS script calling iba.app.(handlers|lib|tools) directly instead of dispatching through iba.app.run:
_(none)_

**Steps without a PS entry point** (0) — an active cfg_step whose work package has no cfg_work_package.ps_script:
_(none)_

**Escalation-file naming drift** (0) — a Workflow/Catalogue or iba/docs file whose own header names an escalation the filename doesn't carry as its prefix:
_(none)_

**Config hedge phrases** (0) — an active cfg_method_rule/cfg_setting row still carrying an unresolved 'not yet .../TBD' with no follow-up:
_(none)_

**Restated authoritative content** (0) — a GOVERNANCE.md/USER-GUIDE.md/CLAUDE.md paragraph closely duplicating an active cfg_* row's own text instead of pointing to it:
_(none)_

**Query file convention** (0) — an ad-hoc SQL scratch file not under scripts/SQLite/{IBA_DB,Research_DB}/, or with a space in its name, or untitled:
_(none)_

<a id="1-inactive-configs-historical-record-not-a-decision"></a>
## 1. Inactive configs — historical record, not a decision

**Inactive configs** (527 row(s) across 10 table(s)) — deactivated, not deleted; excluded from validation above. 359 from the candidate-system retraction, 2026-07-23 (GOVERNANCE.md §15D; migration/retract_candidate_system.py); 12 from the passage-system retirement, 2026-07-26 (reports/archive/passage-system-retirement-record-20260726.md); **156 UNATTRIBUTED** (not part of a known retirement — needs a look): cfg_setting.governance.procedural_document_taxonomy, cfg_setting.lexical.meaning_max_strongs_per_batch, cfg_setting.lexical.run_max_verses, cfg_setting.method.inner_being_narrative_guidance_path, cfg_setting.method.narrative_hard_constraints_path, cfg_setting.narrative.generate_max_cost, cfg_setting.narrative.generate_max_output_tokens, cfg_setting.narrative.generate_model, cfg_setting.narrative.output_pattern, cfg_setting.narrative.rate_input_per_million, cfg_setting.narrative.rate_output_per_million, cfg_setting.narrative.scope_check_report_path, cfg_setting.narrative.usage_log_path, cfg_setting.report.batch_progress_path, cfg_setting.report.lexical_notes_output_pattern, cfg_step.batch-progress-report/report.batch_progress, cfg_step.book-narrative-generate/report.book_narrative_generate, cfg_step.book-narrative-validate/report.book_narrative_validate, cfg_step.book-narrative/report.book_narrative_generate, cfg_step.book-narrative/report.book_narrative_validate, cfg_step.chapter-generate/report.verse_span_meaning, cfg_step.content-index-rebuild/content_index.rebuild, cfg_step.lexicon-parse/lexicon.parse, cfg_step.narrative-register/narrative_register.record, cfg_step.verse-analysis-report/report.verse_span_meaning, cfg_step.verse-lexical/lexical.enrich, cfg_step.verse-lexical/lexical.run, cfg_step.word-audit/word.apply_changes, cfg_step.word-audit/word.audit_checks, cfg_step.word-audit/word.confirm, cfg_step.word-audit/word.export, cfg_step.word-audit/word.flag_reset, cfg_step.word-audit/word.gap_display, cfg_step.word-audit/word.gap_report, cfg_step.word-audit/word.load_json, cfg_step.word-audit/word.meaning, cfg_step.word-audit/word.registry_close, cfg_step.word-registry-span-report/report.word_registry_span, cfg_work_package.batch-progress-report, cfg_work_package.book-narrative, cfg_work_package.book-narrative-generate, cfg_work_package.book-narrative-validate, cfg_work_package.chapter-generate, cfg_work_package.content-index-rebuild, cfg_work_package.verse-analysis-report, cfg_work_package.word-audit, cfg_work_package.word-registry-span-report, cfg_write_grant.configmaint.propose -> cfg_change_detail, cfg_write_grant.configmaint.propose -> cfg_change_log, cfg_write_grant.configmaint.propose -> cfg_lexical_code_class, cfg_write_grant.escalation -> word_registry, cfg_write_grant.lexical.enrich -> verse_lexical_note, cfg_write_grant.lexical.run -> verse_lexical, cfg_write_grant.lexical.run -> verse_lexical_note, cfg_write_grant.lexicon.parse -> strong_lsj_parsed, cfg_write_grant.lexicon.parse -> strong_meaning_parsed, cfg_write_grant.lexicon.parse -> strong_mounce_parsed, cfg_write_grant.narrative_register.record -> narrative_chapter, cfg_write_grant.narrative_register.record -> narrative_citation, cfg_write_grant.narrative_register.record -> narrative_claim, cfg_write_grant.narrative_register.record -> narrative_claim_change, cfg_write_grant.narrative_register.record -> narrative_claim_source, cfg_write_grant.narrative_register.record -> narrative_claim_telling, cfg_write_grant.narrative_register.record -> narrative_section, cfg_write_grant.narrative_register.record -> narrative_update, cfg_write_grant.narrative_register.record -> narrative_update_ref, cfg_write_grant.run -> escalation, cfg_report.report.batch_progress, cfg_report.report.book_narrative_generate, cfg_report.report.book_narrative_validate, cfg_report.report.word_registry_span, cfg_report_section.report.batch_progress/recent_committed, cfg_report_section.report.batch_progress/recent_failures, cfg_report_section.report.batch_progress/running_now, cfg_report_section.report.batch_progress/summary, cfg_report_section.report.book_narrative_validate/findings, cfg_report_section.report.word_registry_span/overview, cfg_report_section.report.word_registry_span/strongs, cfg_report_section.session.close/build_gaps, cfg_report_section.session.close/escalation_gaps, cfg_report_section.session.close/governance_gaps, cfg_report_section.spine.check/discoverability, cfg_enum.escalation_answer=approve, cfg_enum.escalation_answer=reject, cfg_enum.escalation_answer=revise, cfg_enum.escalation_next_action=approve, cfg_enum.escalation_next_action=approved, cfg_enum.escalation_next_action=hold, cfg_enum.escalation_next_action=noted, cfg_enum.escalation_next_action=ready_for_approval, cfg_enum.escalation_next_action=reject, cfg_enum.escalation_next_action=review, cfg_enum.escalation_next_action=revise, cfg_enum.escalation_requirement_check_kind=requires_prior_ready_for_approval_if_decision_required, cfg_enum.escalation_state=answered, cfg_enum.escalation_state=paused, cfg_enum.escalation_state=re-assign, cfg_enum.escalation_state=retracted, cfg_enum.escalation_type=crash, cfg_enum.escalation_type=interactive, cfg_enum.escalation_type=prompted, cfg_enum.escalation_type=report-stop, cfg_enum.ib_observation.tag=cross-cluster-significance, cfg_enum.ib_observation.tag=instance-meaning, cfg_enum.lexical_code_class=connective_causal, cfg_enum.lexical_code_class=connective_coordinating, cfg_enum.lexical_code_class=connective_purpose, cfg_enum.lexical_code_class=negator, cfg_enum.lexical_code_class=party_angelic, cfg_enum.lexical_code_class=party_divine, cfg_enum.lexical_code_class=party_human, cfg_enum.narrative_required_channel=Human ↔ human, cfg_enum.narrative_required_channel=Non-human ↔ human, cfg_enum.narrative_required_channel=Physical world ↔ human, cfg_enum.note_type=chain, cfg_enum.note_type=compound_unit, cfg_enum.note_type=connective, cfg_enum.note_type=cross_lemma_shared_gloss, cfg_enum.note_type=entity_link, cfg_enum.note_type=idiom, cfg_enum.note_type=inert, cfg_enum.note_type=noun_relational, cfg_enum.note_type=noun_severity, cfg_enum.note_type=polarity, cfg_enum.note_type=pronoun_resolution, cfg_enum.note_type=recurrence_role_shift, cfg_enum.note_type=related_word, cfg_enum.note_type=structural_pattern, cfg_enum.note_type=verb_argument, cfg_enum.prose_section_type_lifecycle_tag=source, cfg_enum.prose_section_type_lifecycle_tag=v1, cfg_enum.prose_section_type_lifecycle_tag=v2, cfg_enum.prose_section_type_lifecycle_tag=v3, cfg_enum.resolution_status=checked_empty, cfg_enum.resolution_status=not_supported_this_language, cfg_enum.resolution_status=resolved, cfg_enum.resolution_status=unclassified, cfg_enum.resolution_status=unresolved, cfg_on_fail.narrative_register.record/refused, cfg_on_fail.report.book_narrative_generate/api-error, cfg_on_fail.report.book_narrative_generate/api-key-missing, cfg_on_fail.report.book_narrative_generate/cost-cap-exceeded, cfg_on_fail.report.book_narrative_generate/declined, cfg_on_fail.report.book_narrative_generate/guidance-doc-missing, cfg_on_fail.report.book_narrative_generate/needs-approval, cfg_on_fail.report.book_narrative_generate/needs-revision, cfg_on_fail.report.book_narrative_generate/no-debates-found, cfg_on_fail.report.book_narrative_validate/guidance-doc-missing, cfg_on_fail.report.book_narrative_validate/narrative-file-missing, cfg_on_fail.report.book_narrative_validate/no-path-given, cfg_on_fail.report.book_narrative_validate/scope-check-incomplete, cfg_on_fail.report.book_narrative_validate/scope-check-missing, cfg_on_fail.report.word_registry_span/word-not-found, cfg_on_fail.session.close/gaps-found, cfg_on_fail.word.confirm/needs-confirmation, cfg_on_fail.word.gap_display/needs-approval.
- **cfg_setting** (23): `candidate.concept_delimiter_pattern`, `candidate.lemma_base_pattern`, `candidate.load_report_path`, `candidate.quality_report_path`, `candidate.tag_clean_pattern`, `candidate.tag_max_words`, `candidate.transliteration_pattern`, `governance.procedural_document_taxonomy`, `lexical.meaning_max_strongs_per_batch`, `lexical.run_max_verses`, `method.inner_being_narrative_guidance_path`, `method.narrative_hard_constraints_path`, `narrative.generate_max_cost`, `narrative.generate_max_output_tokens`, `narrative.generate_model`, `narrative.output_pattern`, `narrative.rate_input_per_million`, `narrative.rate_output_per_million`, `narrative.scope_check_report_path`, `narrative.usage_log_path`, `report.batch_progress_path`, `report.lexical_notes_output_pattern`, `validation.show_candidate`
- **cfg_step** (33): `batch-progress-report/report.batch_progress`, `book-narrative-generate/report.book_narrative_generate`, `book-narrative-validate/report.book_narrative_validate`, `book-narrative/report.book_narrative_generate`, `book-narrative/report.book_narrative_validate`, `build-passages/passage.suggest_boundary`, `candidate-curation/candidate.curate`, `candidate-curation/candidate.load`, `candidate-quality/candidate.validate`, `chapter-generate/report.passage_debate`, `chapter-generate/report.verse_span_meaning`, `content-index-rebuild/content_index.rebuild`, `lexicon-parse/lexicon.parse`, `narrative-register/narrative_register.record`, `passage-debate-report/report.passage_debate`, `passage-debate-sync/passage.debate_sync`, `seed-candidate-report/report.seed_candidate`, `set-candidates/candidate.seed`, `set-candidates/candidate.set`, `verse-analysis-report/report.verse_span_meaning`, `verse-lexical/lexical.enrich`, `verse-lexical/lexical.run`, `word-audit/word.apply_changes`, `word-audit/word.audit_checks`, `word-audit/word.confirm`, `word-audit/word.export`, `word-audit/word.flag_reset`, `word-audit/word.gap_display`, `word-audit/word.gap_report`, `word-audit/word.load_json`, `word-audit/word.meaning`, `word-audit/word.registry_close`, `word-registry-span-report/report.word_registry_span`
- **cfg_work_package** (15): `batch-progress-report`, `book-narrative`, `book-narrative-generate`, `book-narrative-validate`, `candidate-curation`, `candidate-quality`, `chapter-generate`, `content-index-rebuild`, `passage-debate-report`, `passage-debate-sync`, `seed-candidate-report`, `set-candidates`, `verse-analysis-report`, `word-audit`, `word-registry-span-report`
- **cfg_write_grant** (30): `candidate.curate -> candidate_seed`, `candidate.load -> candidate_seed`, `candidate.seed -> candidate_seed`, `candidate.seed -> lemma_inventory`, `candidate.set -> span_candidate`, `configmaint.propose -> cfg_change_detail`, `configmaint.propose -> cfg_change_log`, `configmaint.propose -> cfg_lexical_code_class`, `escalation -> word_registry`, `lexical.enrich -> passage`, `lexical.enrich -> verse_lexical_note`, `lexical.run -> verse_lexical`, `lexical.run -> verse_lexical_note`, `lexicon.parse -> strong_lsj_parsed`, `lexicon.parse -> strong_meaning_parsed`, `lexicon.parse -> strong_mounce_parsed`, `migration -> candidate_seed`, `narrative_register.record -> narrative_chapter`, `narrative_register.record -> narrative_citation`, `narrative_register.record -> narrative_claim`, `narrative_register.record -> narrative_claim_change`, `narrative_register.record -> narrative_claim_source`, `narrative_register.record -> narrative_claim_telling`, `narrative_register.record -> narrative_passage`, `narrative_register.record -> narrative_section`, `narrative_register.record -> narrative_update`, `narrative_register.record -> narrative_update_ref`, `narrative_register.tell -> narrative_passage`, `report.debate -> passage`, `run -> escalation`
- **cfg_report** (7): `candidate.load`, `candidate.validate`, `report.batch_progress`, `report.book_narrative_generate`, `report.book_narrative_validate`, `report.seed_candidate`, `report.word_registry_span`
- **cfg_report_section** (22): `candidate.load/duplicates`, `candidate.load/exceptions`, `candidate.validate/gloss`, `candidate.validate/orphan_lemmas`, `candidate.validate/seed_tag`, `candidate.validate/span_tag`, `report.batch_progress/recent_committed`, `report.batch_progress/recent_failures`, `report.batch_progress/running_now`, `report.batch_progress/summary`, `report.book_narrative_validate/findings`, `report.seed_candidate/distribution`, `report.seed_candidate/over_time`, `report.seed_candidate/summary`, `report.seed_candidate/top_lemmas`, `report.word_registry_span/overview`, `report.word_registry_span/strongs`, `session.close/build_gaps`, `session.close/escalation_gaps`, `session.close/governance_gaps`, `spine.check/discoverability`, `validation.book/candidate`
- **cfg_report_csv_table** (6): `candidate.load/candidate_seed`, `candidate.validate/candidate_seed`, `candidate.validate/lemma_inventory`, `candidate.validate/span_candidate`, `report.seed_candidate/candidate_seed`, `validation.book/candidate_seed`
- **cfg_enum** (73): `candidate_decision=candidate`, `candidate_decision=exception`, `candidate_decision=rejected`, `candidate_decision=undecided`, `candidate_ib_referent=body_part`, `candidate_ib_referent=characteristic`, `candidate_ib_referent=other_being`, `candidate_source=curated-synonym`, `candidate_source=ib-judgement`, `candidate_source=read-emergent`, `candidate_source=registry-direct`, `candidate_step_status=in_strong`, `candidate_step_status=not_in_step`, `candidate_step_status=step_has_verses_pending`, `candidate_step_status=step_no_verses`, `escalation_answer=approve`, `escalation_answer=reject`, `escalation_answer=revise`, `escalation_next_action=approve`, `escalation_next_action=approved`, `escalation_next_action=hold`, `escalation_next_action=noted`, `escalation_next_action=ready_for_approval`, `escalation_next_action=reject`, `escalation_next_action=review`, `escalation_next_action=revise`, `escalation_requirement_check_kind=requires_prior_ready_for_approval_if_decision_required`, `escalation_state=answered`, `escalation_state=paused`, `escalation_state=re-assign`, `escalation_state=retracted`, `escalation_type=crash`, `escalation_type=interactive`, `escalation_type=prompted`, `escalation_type=report-stop`, `ib_observation.tag=cross-cluster-significance`, `ib_observation.tag=instance-meaning`, `lexical_code_class=connective_causal`, `lexical_code_class=connective_coordinating`, `lexical_code_class=connective_purpose`, `lexical_code_class=negator`, `lexical_code_class=party_angelic`, `lexical_code_class=party_divine`, `lexical_code_class=party_human`, `narrative_required_channel=Human ↔ human`, `narrative_required_channel=Non-human ↔ human`, `narrative_required_channel=Physical world ↔ human`, `note_type=chain`, `note_type=compound_unit`, `note_type=connective`, `note_type=cross_lemma_shared_gloss`, `note_type=entity_link`, `note_type=idiom`, `note_type=inert`, `note_type=noun_relational`, `note_type=noun_severity`, `note_type=polarity`, `note_type=pronoun_resolution`, `note_type=recurrence_role_shift`, `note_type=related_word`, `note_type=structural_pattern`, `note_type=verb_argument`, `passage_source=passage-build`, `passage_source=single-verse-emergent`, `prose_section_type_lifecycle_tag=source`, `prose_section_type_lifecycle_tag=v1`, `prose_section_type_lifecycle_tag=v2`, `prose_section_type_lifecycle_tag=v3`, `resolution_status=checked_empty`, `resolution_status=not_supported_this_language`, `resolution_status=resolved`, `resolution_status=unclassified`, `resolution_status=unresolved`
- **cfg_on_fail** (29): `candidate.curate/change-rejected`, `candidate.curate/invalid-proposal`, `candidate.curate/needs-approval`, `candidate.curate/needs-revision`, `candidate.load/needs-review`, `candidate.seed/no-inventory`, `candidate.set/no-spans`, `candidate.validate/findings-rejected`, `candidate.validate/needs-review`, `candidate.validate/needs-revision`, `narrative_register.record/refused`, `passage.build/no-candidates`, `report.book_narrative_generate/api-error`, `report.book_narrative_generate/api-key-missing`, `report.book_narrative_generate/cost-cap-exceeded`, `report.book_narrative_generate/declined`, `report.book_narrative_generate/guidance-doc-missing`, `report.book_narrative_generate/needs-approval`, `report.book_narrative_generate/needs-revision`, `report.book_narrative_generate/no-debates-found`, `report.book_narrative_validate/guidance-doc-missing`, `report.book_narrative_validate/narrative-file-missing`, `report.book_narrative_validate/no-path-given`, `report.book_narrative_validate/scope-check-incomplete`, `report.book_narrative_validate/scope-check-missing`, `report.word_registry_span/word-not-found`, `session.close/gaps-found`, `word.confirm/needs-confirmation`, `word.gap_display/needs-approval`
- **cfg_candidate_rule** (by kind): accept=289

<a id="2-utilities-registry"></a>
## 2. Utilities registry

**956** registered module(s) — **503** declared `config_exempt` (a legitimate zero for config-setting/enum usage, not a completeness gap), **837** inactive (module removed/merged). See §0 "Low config-density utilities" for any NON-exempt module still flagged.

| module | file | purpose | active | exempt | exempt reason |
| --- | --- | --- | --- | --- | --- |
| Copy-NarrativeToLearning4Comfort.ps1 | iba/app/ps/Copy-NarrativeToLearning4Comfort.ps1 | PS wrapper for narrativecopy.py (-DryRun). Run on completion of a section of work, on request, and in /session-close (escalation #1941). | ✓ | ✓ | thin wrapper; config is read by narrativecopy.py |
| Narrative-Register.ps1 | iba/app/ps/Narrative-Register.ps1 | PS entry point for the narrative claim register (escalation #2110); every action dispatches through run.py, work package narrative-register. | ✓ | ✓ | thin wrapper; config is read by the handlers through run.py |
| Strand-Reading.ps1 | iba/app/ps/Strand-Reading.ps1 | PS entry point for the reading process (escalation #2172); every step dispatches through run.py, work package strand-reading. | ✓ | ✓ | thin wrapper; config is read by the handlers through run.py |
| VerseMeta.ps1 | iba/app/ps/VerseMeta.ps1 | PS entry point of work package verse-meta: VerseMeta.ps1 -Step SetStatus -References "Gen.1.1,Rom 1:2" -Status analysed, dispatched through run.py (step verse_meta.set_status, #2207). Escalation #1661. | ✓ | ✓ | PS entry point: the step's config is read by the handler and lib/versemeta.py |
| add_adversarial_cluster_v1_20260905 | iba/app/migration/archive/add_adversarial_cluster_v1_20260905.py | ONE-OFF migration -- architecture correction, researcher verdict 2026-09-05: Strong's-code classification (negator/connective/party) belongs in cluster/cluster_strong, not cfg_lexical_code_class/configmaint. Creates cluster T4 'Adversarial' and reallocates H7854/G4567/G1228G from T2 to T4 (first of several tracked de-cfg-ification escalations). inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| add_concise_verse_specific_rule_v1_20260921 | iba/app/migration/archive/add_concise_verse_specific_rule_v1_20260921.py | ONE-OFF migration -- escalation #1824: registers a new cfg_method_rule requiring concise, verse-specific obs_text for lexical.meaning/cluster.reading/cluster.answer, fixing the root cause of the same/broaden/new dedup never firing. Run once, then set inactive=1. |  |  |  |
| add_elevation_candidate_question_v1_20260922 | iba/app/migration/archive/add_elevation_candidate_question_v1_20260922.py | ONE-OFF migration -- escalation #1836: registers M0.8.1 (T2/T3 elevation-candidate question) in wa_obs_question_catalogue. Run once (applied directly, script written for provenance), then set inactive=1. |  |  |  |
| add_lexicon_header_pos_tags_setting_v1_20260910 | iba/app/migration/add_lexicon_header_pos_tags_setting_v1_20260910.py | One-off: seeds cfg_setting lexicon.header_pos_tags (22 bare POS-tag values lib/lexiconparse.py:is_header_only_line() matches against). Escalation #1668, 2026-09-10. Idempotent, safe to re-run. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| add_meaning_keywords_column_v1_20260921 | iba/app/migration/archive/add_meaning_keywords_column_v1_20260921.py | ONE-OFF migration -- escalation #1824: adds ib_observation.meaning_keywords for the new structured-key same/broaden/new matching path. Run once, then set inactive=1. |  |  |  |
| add_negator_connective_partydivine_clusters_v1_20260905 | iba/app/migration/archive/add_negator_connective_partydivine_clusters_v1_20260905.py | ONE-OFF migration -- part of the cfg_lexical_code_class -> cluster de-cfg-ification (escalation #1499). Creates clusters T5 (Negator), T6 (Connective, kept unsplit per the researcher's own granularity test), T7 (Party-Divine); reallocates 19 codes from T2, inserts 3 fresh (no prior cluster_strong row). inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831 | iba/app/migration/archive/add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py | ONE-OFF migration, escalation #1007 -- adds wa_obs_question_catalogue.source/last_modified (bible_research.db DDL) and registers the catalogue-update work package/step/write-grant/utility rows. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| add_party_human_angelic_clusters_v1_20260905 | iba/app/migration/archive/add_party_human_angelic_clusters_v1_20260905.py | ONE-OFF migration -- part of the cfg_lexical_code_class -> cluster de-cfg-ification (escalation #1500). Creates clusters T8 (Party-Human, 8 codes) and T9 (Party-Angelic, 5 codes incl. sub-entries). inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| add_ps_scripts_dispatch_through_run_py_rule | iba/app/migration/add_ps_scripts_dispatch_through_run_py_rule_20260821.py | One-off migration: escalation #8 -- adds cfg_behaviour_rule (development, every-active-ps-script-dispatches-through-run-py). | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| add_resolution_kind_column | iba/app/migration/add_resolution_kind_column_v1_20260822.py | One-off migration: escalation #798/#799 Stage 2 (schema half) -- adds the resolution_kind column to escalation/escalation_history, closing a gap left by Stage 1's config-only pass. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| add_verse_meta_status_column_v1_20260910 | iba/app/migration/add_verse_meta_status_column_v1_20260910.py | Adds verse_meta.status + verse_meta.status_changed_at (domain: cfg_enum verse_meta_status = exclude/citated/analysed; 'anchor' deliberately excluded, already verse_meta.is_passage_anchor). Idempotent, safe to re-run. Escalation #1661. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| add_verse_substantiation_questions_v1_20260921 | iba/app/migration/archive/add_verse_substantiation_questions_v1_20260921.py | ONE-OFF migration -- escalation #1806: adds 16 new word-level, characteristic-agnostic verse-reading questions (M0.7.1-16), one per Category A char-question. Run once, then set inactive=1. |  |  |  |
| analytics_bible_books_scripts_archive_compare_h2_vs_storymarkers | _analytics/Bible_Books/scripts/archive/Compare-H2-vs-StoryMarkers.ps1 | Retired (#2200): not in a utility or module. Was _analytics/Bible_Books/scripts/Compare-H2-vs-StoryMarkers.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_bible_books_scripts_archive_count_storymarkersbyfile | _analytics/Bible_Books/scripts/archive/Count-StoryMarkersByFile.ps1 | Retired (#2200): not in a utility or module. Was _analytics/Bible_Books/scripts/Count-StoryMarkersByFile.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_bible_books_scripts_archive_generate_psalmsstorycombined | _analytics/Bible_Books/scripts/archive/Generate-PsalmsStoryCombined.ps1 | Retired (#2200): not in a utility or module. Was _analytics/Bible_Books/scripts/Generate-PsalmsStoryCombined.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_bible_books_scripts_archive_validate_psalmsstorycombined | _analytics/Bible_Books/scripts/archive/Validate-PsalmsStoryCombined.ps1 | Retired (#2200): not in a utility or module. Was _analytics/Bible_Books/scripts/Validate-PsalmsStoryCombined.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_archive_1692_ib_node_mockup_generator_v1_20260914 | _analytics/Clusters/archive/1692-ib-node-mockup-generator-v1-20260914.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/1692-ib-node-mockup-generator-v1-20260914.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_archive_1692_ib_node_web_artifact_builder_v1_20260914 | _analytics/Clusters/archive/1692-ib-node-web-artifact-builder-v1-20260914.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/1692-ib-node-web-artifact-builder-v1-20260914.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m01_fear_awe_archive_fear_quote_check_v1_20261001 | _analytics/Clusters/M01 - fear-awe/archive/fear-quote-check-v1-20261001.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M01 - fear-awe/fear-quote-check-v1-20261001.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m01_fear_awe_archive_ot_07_2_weave_v1_20261019 | _analytics/Clusters/M01 - fear-awe/archive/ot-07-2-weave-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M01 - fear-awe/ot-07-2-weave-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_chapter_match_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-chapter-match-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-chapter-match-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_overview_forms_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-overview-forms-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-overview-forms-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_reconciliation_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-reconciliation-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-reconciliation-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_unit1_face_assign_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-unit1-face-assign-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-unit1-face-assign-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_unit2_face_assign_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-unit2-face-assign-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-unit2-face-assign-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_unit3_face_assign_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-unit3-face-assign-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-unit3-face-assign-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_unit4_face_assign_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-unit4-face-assign-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-unit4-face-assign-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_anger_unit5_face_assign_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/anger-unit5-face-assign-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/anger-unit5-face-assign-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_m02_pairing_done_strands_check_build_v1_20261013 | _analytics/Clusters/M02 - anger-wrath/archive/m02-pairing-done-strands-check-build-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/m02-pairing-done-strands-check-build-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_m02_pairing_done_strands_context_v1_20261013 | _analytics/Clusters/M02 - anger-wrath/archive/m02-pairing-done-strands-context-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/m02-pairing-done-strands-context-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_m02_pairing_done_strands_worksheet_v1_20261013 | _analytics/Clusters/M02 - anger-wrath/archive/m02-pairing-done-strands-worksheet-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/m02-pairing-done-strands-worksheet-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_m02_pairing_gaps_records_update_v1_20261013 | _analytics/Clusters/M02 - anger-wrath/archive/m02-pairing-gaps-records-update-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/m02-pairing-gaps-records-update-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_m02_pairing_gaps_weave_v1_20261013 | _analytics/Clusters/M02 - anger-wrath/archive/m02-pairing-gaps-weave-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/m02-pairing-gaps-weave-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_ot_07_3_weave_v1_20261019 | _analytics/Clusters/M02 - anger-wrath/archive/ot-07-3-weave-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/ot-07-3-weave-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_wa_cluster_m02_recovery_consolidation_build_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/wa-cluster-M02-recovery-consolidation-build-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/wa-cluster-M02-recovery-consolidation-build-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m02_anger_wrath_archive_wa_cluster_m02_recovery_tests_v1_20261005 | _analytics/Clusters/M02 - anger-wrath/archive/wa-cluster-M02-recovery-tests-v1-20261005.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M02 - anger-wrath/wa-cluster-M02-recovery-tests-v1-20261005.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m07_shame_confusion_archive_m07_cluster_overview_extras_v1_20261019 | _analytics/Clusters/M07 - shame-confusion/archive/m07-cluster-overview-extras-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M07 - shame-confusion/m07-cluster-overview-extras-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m07_shame_confusion_archive_m07_cluster_overview_pull_v1_20261019 | _analytics/Clusters/M07 - shame-confusion/archive/m07-cluster-overview-pull-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M07 - shame-confusion/m07-cluster-overview-pull-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m07_shame_confusion_archive_m07_m53_reading_set_build_v1_20261019 | _analytics/Clusters/M07 - shame-confusion/archive/m07-m53-reading-set-build-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M07 - shame-confusion/m07-m53-reading-set-build-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_batch1_register_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-batch1-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-batch1-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_batch2_register_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-batch2-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-batch2-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_batch3_register_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-batch3-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-batch3-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_batch4_register_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-batch4-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-batch4-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_batch5_register_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-batch5-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-batch5-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_batch_pull_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-batch-pull-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-batch-pull-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_cluster_overview_extras_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-cluster-overview-extras-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-cluster-overview-extras-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_cluster_overview_pull_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-cluster-overview-pull-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-cluster-overview-pull-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_group_b_scan_pull_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-group-B-scan-pull-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-group-B-scan-pull-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_group_b_scan_triage_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-group-B-scan-triage-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-group-B-scan-triage-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_narrative_quote_check_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-narrative-quote-check-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-narrative-quote-check-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_pride_anchor_classify_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-pride-anchor-classify-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-pride-anchor-classify-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_pride_anchor_scan_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-pride-anchor-scan-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-pride-anchor-scan-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_pride_register_update_build_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-pride-register-update-build-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-pride-register-update-build-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_pride_weave_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-pride-weave-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-pride-weave-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_quote_check_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-quote-check-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-quote-check-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_m08_reading_scope_v1_20261015 | _analytics/Clusters/M08 - pride-arrogance/archive/m08-reading-scope-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/m08-reading-scope-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m08_pride_arrogance_archive_ot_05_16_weave_v1_20261019 | _analytics/Clusters/M08 - pride-arrogance/archive/ot-05-16-weave-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M08 - pride-arrogance/ot-05-16-weave-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_cluster_overview_pull_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-cluster-overview-pull-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-cluster-overview-pull-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_batch1_register_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-batch1-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-batch1-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_batch2_register_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-batch2-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-batch2-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_batch3_register_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-batch3-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-batch3-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_batch4_register_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-batch4-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-batch4-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_batch5_register_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-batch5-register-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-batch5-register-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_crosscheck_pull_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-crosscheck-pull-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-crosscheck-pull-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humbling_fanout_pull_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humbling-fanout-pull-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humbling-fanout-pull-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humility_reconcile_register_build_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humility-reconcile-register-build-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humility-reconcile-register-build-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humility_reconcile_text_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humility-reconcile-text-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humility-reconcile-text-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humility_register_update_build_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humility-register-update-build-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humility-register-update-build-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_humility_weave_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-humility-weave-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-humility-weave-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_poor_needy_dimension_markers_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-poor-needy-dimension-markers-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-poor-needy-dimension-markers-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m09_humility_lowliness_archive_m09_poor_needy_split_v1_20261015 | _analytics/Clusters/M09 - humility-lowliness/archive/m09-poor-needy-split-v1-20261015.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M09 - humility-lowliness/m09-poor-needy-split-v1-20261015.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_cluster_overview_pull_v1_20261008 | _analytics/Clusters/M18 - desire-longing/archive/m18-cluster-overview-pull-v1-20261008.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-cluster-overview-pull-v1-20261008.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_delight_pleasure_filter_v1_20261008 | _analytics/Clusters/M18 - desire-longing/archive/m18-delight-pleasure-filter-v1-20261008.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-delight-pleasure-filter-v1-20261008.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_delight_pleasure_pairing_pull_v1_20261008 | _analytics/Clusters/M18 - desire-longing/archive/m18-delight-pleasure-pairing-pull-v1-20261008.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-delight-pleasure-pairing-pull-v1-20261008.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_a_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-A-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-A-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_a_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-A-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-A-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b1_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B1-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B1-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b1_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B1-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B1-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b1_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B1-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B1-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b2_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B2-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B2-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b2_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B2-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B2-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b2_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B2-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B2-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_bucket1_list_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-bucket1-list-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-bucket1-list-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_bucket1_remaining_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-bucket1-remaining-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-bucket1-remaining-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_ch11_faces_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-ch11-faces-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-ch11-faces-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_ch11_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-ch11-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-ch11-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_correction_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-correction-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-correction-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_correction_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-correction-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-correction-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_remaining_records_update_v1_20261011 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-remaining-records-update-v1-20261011.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-remaining-records-update-v1-20261011.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_remaining_role_triage_v1_20261011 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-remaining-role-triage-v1-20261011.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-remaining-role-triage-v1-20261011.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_remaining_weave_v1_20261011 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-remaining-weave-v1-20261011.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-remaining-weave-v1-20261011.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_verb_split_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-verb-split-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-verb-split-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_b_verse_list_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-B-verse-list-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-B-verse-list-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_c_records_update_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-C-records-update-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-C-records-update-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_c_role_triage_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-C-role-triage-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-C-role-triage-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_c_weave_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-C-weave-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-C-weave-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_d_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-D-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-D-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_d_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-D-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-D-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_d_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-D-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-D-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_e_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-E-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-E-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_e_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-E-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-E-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_f_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-F-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-F-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_f_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-F-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-F-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_f_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-F-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-F-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_g_decisions_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-G-decisions-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-G-decisions-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_g_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-G-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-G-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_g_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-G-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-G-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_pull_worksheet_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-pull-worksheet-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-pull-worksheet-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_group_register_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-group-register-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-group-register-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_held_items_pull_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-held-items-pull-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-held-items-pull-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m02_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m02-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m02-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m02_validation_register_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m02-validation-register-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m02-validation-register-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m02_validation_worksheet_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m02-validation-worksheet-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m02-validation-worksheet-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m25_held_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m25-held-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m25-held-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m25_validation_register_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m25-validation-register-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m25-validation-register-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m25_validation_worksheet_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m25-validation-worksheet-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m25-validation-worksheet-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m47_narrative_weave_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m47-narrative-weave-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m47-narrative-weave-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m47_records_update_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m47-records-update-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m47-records-update-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m47_validation_register_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m47-validation-register-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m47-validation-register-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m47_validation_worksheet_build_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-m47-validation-worksheet-build-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m47-validation-worksheet-build-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m72_shared_pull_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-m72-shared-pull-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m72-shared-pull-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m72_shared_records_update_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-m72-shared-records-update-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m72-shared-records-update-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m72_shared_triage_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-m72-shared-triage-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m72-shared-triage-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_m72_shared_weave_v1_20261012 | _analytics/Clusters/M18 - desire-longing/archive/m18-m72-shared-weave-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-m72-shared-weave-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_shared_analysis_crossref_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-shared-analysis-crossref-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-shared-analysis-crossref-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_m18_shared_m47_m25_m02_pull_v1_20261009 | _analytics/Clusters/M18 - desire-longing/archive/m18-shared-m47-m25-m02-pull-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/m18-shared-m47-m25-m02-pull-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m18_desire_longing_archive_ot_98_2_weave_v1_20261019 | _analytics/Clusters/M18 - desire-longing/archive/ot-98-2-weave-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M18 - desire-longing/ot-98-2-weave-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_claim_register_crosscheck_v1_20261013 | _analytics/Clusters/M25 - life-death/archive/life-death-claim-register-crosscheck-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-claim-register-crosscheck-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_claim_register_crosscheck_v2_20261013 | _analytics/Clusters/M25 - life-death/archive/life-death-claim-register-crosscheck-v2-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-claim-register-crosscheck-v2-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot02_ch2_v25_weave_v1_20261014 | _analytics/Clusters/M25 - life-death/archive/life-death-ot02-ch2-v25-weave-v1-20261014.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot02-ch2-v25-weave-v1-20261014.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot02_face_coverage_v1_20261014 | _analytics/Clusters/M25 - life-death/archive/life-death-ot02-face-coverage-v1-20261014.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot02-face-coverage-v1-20261014.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot02_register_update_build_v1_20261014 | _analytics/Clusters/M25 - life-death/archive/life-death-ot02-register-update-build-v1-20261014.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot02-register-update-build-v1-20261014.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot05_26_body_raised_r0_decisions_v1_20261019 | _analytics/Clusters/M25 - life-death/archive/life-death-ot05-26-body-raised-r0-decisions-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot05-26-body-raised-r0-decisions-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot05_26_body_raised_r0_pull_v1_20261019 | _analytics/Clusters/M25 - life-death/archive/life-death-ot05-26-body-raised-r0-pull-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot05-26-body-raised-r0-pull-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot05_26_weave_v1_20261019 | _analytics/Clusters/M25 - life-death/archive/life-death-ot05-26-weave-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot05-26-weave-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot05_cuts_v1_20261014 | _analytics/Clusters/M25 - life-death/archive/life-death-ot05-cuts-v1-20261014.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot05-cuts-v1-20261014.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_ot05_grouping_v1_20261014 | _analytics/Clusters/M25 - life-death/archive/life-death-ot05-grouping-v1-20261014.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-ot05-grouping-v1-20261014.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_q2_q3_face_assign_v1_20261004 | _analytics/Clusters/M25 - life-death/archive/life-death-q2-q3-face-assign-v1-20261004.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-q2-q3-face-assign-v1-20261004.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_strong_verse_pull_v1_20261013 | _analytics/Clusters/M25 - life-death/archive/life-death-strong-verse-pull-v1-20261013.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-strong-verse-pull-v1-20261013.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_unit2_face_assign_v1_20261002 | _analytics/Clusters/M25 - life-death/archive/life-death-unit2-face-assign-v1-20261002.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-unit2-face-assign-v1-20261002.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_unit3_face_assign_v1_20261003 | _analytics/Clusters/M25 - life-death/archive/life-death-unit3-face-assign-v1-20261003.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-unit3-face-assign-v1-20261003.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_unit3_supplement_face_assign_v1_20261004 | _analytics/Clusters/M25 - life-death/archive/life-death-unit3-supplement-face-assign-v1-20261004.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-unit3-supplement-face-assign-v1-20261004.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_unit4_face_assign_v1_20261004 | _analytics/Clusters/M25 - life-death/archive/life-death-unit4-face-assign-v1-20261004.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-unit4-face-assign-v1-20261004.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_life_death_unit4_supplement_face_assign_v1_20261004 | _analytics/Clusters/M25 - life-death/archive/life-death-unit4-supplement-face-assign-v1-20261004.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/life-death-unit4-supplement-face-assign-v1-20261004.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_narrative_quote_check_v1_20261014 | _analytics/Clusters/M25 - life-death/archive/narrative-quote-check-v1-20261014.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/narrative-quote-check-v1-20261014.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_strand_cooccurrence_pull_v1_20261004 | _analytics/Clusters/M25 - life-death/archive/strand-cooccurrence-pull-v1-20261004.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/strand-cooccurrence-pull-v1-20261004.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_strand_overview_v1_20261002 | _analytics/Clusters/M25 - life-death/archive/strand-overview-v1-20261002.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/strand-overview-v1-20261002.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m25_life_death_archive_strand_unit_pull_v1_20261002 | _analytics/Clusters/M25 - life-death/archive/strand-unit-pull-v1-20261002.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M25 - life-death/strand-unit-pull-v1-20261002.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m53_dishonor_disgrace_archive_m53_cluster_overview_extras_v1_20261019 | _analytics/Clusters/M53 - dishonor-disgrace/archive/m53-cluster-overview-extras-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M53 - dishonor-disgrace/m53-cluster-overview-extras-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m53_dishonor_disgrace_archive_m53_cluster_overview_extras_v2_20261019 | _analytics/Clusters/M53 - dishonor-disgrace/archive/m53-cluster-overview-extras-v2-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M53 - dishonor-disgrace/m53-cluster-overview-extras-v2-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m53_dishonor_disgrace_archive_m53_cluster_overview_pull_v1_20261019 | _analytics/Clusters/M53 - dishonor-disgrace/archive/m53-cluster-overview-pull-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M53 - dishonor-disgrace/m53-cluster-overview-pull-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_choose_mcode_cooccurrence_v1_20261007 | _analytics/Clusters/M64 - will-resolve/archive/m64-choose-mcode-cooccurrence-v1-20261007.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-choose-mcode-cooccurrence-v1-20261007.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_choose_mcode_hib_qualifier_v1_20261007 | _analytics/Clusters/M64 - will-resolve/archive/m64-choose-mcode-hib-qualifier-v1-20261007.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-choose-mcode-hib-qualifier-v1-20261007.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_choose_reading_placement_v2_20261007 | _analytics/Clusters/M64 - will-resolve/archive/m64-choose-reading-placement-v2-20261007.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-choose-reading-placement-v2-20261007.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_choose_routing_v1_20261007 | _analytics/Clusters/M64 - will-resolve/archive/m64-choose-routing-v1-20261007.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-choose-routing-v1-20261007.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_choose_verses_pull_v3_20261008 | _analytics/Clusters/M64 - will-resolve/archive/m64-choose-verses-pull-v3-20261008.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-choose-verses-pull-v3-20261008.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_h6942h_verses_pull_v1_20261006 | _analytics/Clusters/M64 - will-resolve/archive/m64-H6942H-verses-pull-v1-20261006.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-H6942H-verses-pull-v1-20261006.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_m47_marked_verses_m47_trace_v1_20261006 | _analytics/Clusters/M64 - will-resolve/archive/m64-m47-marked-verses-m47-trace-v1-20261006.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-m47-marked-verses-m47-trace-v1-20261006.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_m47_uncited_pull_v1_20261006 | _analytics/Clusters/M64 - will-resolve/archive/m64-m47-uncited-pull-v1-20261006.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-m47-uncited-pull-v1-20261006.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_m64_plan_scan_grouping_v1_20261008 | _analytics/Clusters/M64 - will-resolve/archive/m64-plan-scan-grouping-v1-20261008.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/m64-plan-scan-grouping-v1-20261008.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_verse_narrative_ot_crossref_v3_20261009 | _analytics/Clusters/M64 - will-resolve/archive/verse-narrative-ot-crossref-v3-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/verse-narrative-ot-crossref-v3-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m64_will_resolve_archive_verse_narrative_ot_crossref_v3_test_v1_20261009 | _analytics/Clusters/M64 - will-resolve/archive/verse-narrative-ot-crossref-v3-test-v1-20261009.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M64 - will-resolve/verse-narrative-ot-crossref-v3-test-v1-20261009.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_cluster_overview_pull_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-cluster-overview-pull-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-cluster-overview-pull-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_completed_strand_check_pull_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-completed-strand-check-pull-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-completed-strand-check-pull-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_focus_pull_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-focus-pull-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-focus-pull-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_b_passage_pull_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-B-passage-pull-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-B-passage-pull-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_b_records_update_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-B-records-update-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-B-records-update-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_b_records_update_v2_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-B-records-update-v2-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-B-records-update-v2-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_b_role_triage_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-B-role-triage-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-B-role-triage-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_b_weave_activities_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-B-weave-activities-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-B-weave-activities-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_b_weave_ch11_and_faculties_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-B-weave-ch11-and-faculties-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-B-weave-ch11-and-faculties-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_clusters_m72_authority_dominion_archive_m72_group_d_forward_v1_20261012 | _analytics/Clusters/M72 - authority-dominion/archive/m72-group-D-forward-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/Clusters/M72 - authority-dominion/m72-group-D-forward-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_cross_cluster_web_archive_escalation_2000_open_threads_import_preview_v1_20261012 | _analytics/cross-cluster-web/archive/escalation-2000-open-threads-import-preview-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/cross-cluster-web/escalation-2000-open-threads-import-preview-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_cross_cluster_web_archive_escalation_2000_register_export_compare_v1_20261012 | _analytics/cross-cluster-web/archive/escalation-2000-register-export-compare-v1-20261012.py | Retired (#2200): not in a utility or module. Was _analytics/cross-cluster-web/escalation-2000-register-export-compare-v1-20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| analytics_cross_cluster_web_archive_reading_to_narrative_trace_v1_20261019 | _analytics/cross-cluster-web/archive/reading-to-narrative-trace-v1-20261019.py | Retired (#2200): not in a utility or module. Was _analytics/cross-cluster-web/reading-to-narrative-trace-v1-20261019.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| anchor_test_plan_governance_rule | iba/app/migration/anchor_test_plan_governance_rule_20260822.py | Anchors the researcher's 2026-08-22 test-plan-per-module/utility instruction in governance (cfg_behaviour_rule + governance.* cfg_setting), escalation #795. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| apply_1598_cluster_batch | iba/app/migration/apply_1598_cluster_batch.py | Reusable, parameter-driven runner for escalation #1598 ongoing small-batch cluster reallocation work -- applies any reviewable JSON payload (new_clusters/inserts/relocations/removals) to cluster_strong/cluster, idempotent, used across Phases A-O this session. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| apply_1598_phase_a_reallocation_v1_20260908 | iba/app/migration/apply_1598_phase_a_reallocation_v1_20260908.py | ONE-OFF migration -- escalation #1598 Phase A: creates T10 Places/T11 Corporate-Collective/T7 Party-Divine etc cluster scaffolding and applies the first reallocation batch. Already run live. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| apply_2199_2201_decisions_v1_20261021 | iba/app/migration/archive/apply_2199_2201_decisions_v1_20261021.py | ONE-OFF migration -- escalations #2199/#2201: the researcher's approved decisions, through configmaint.apply_logged under run_id DEVMODE-2201-DECISIONS-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| apply_catalogue_wording_v1_20260921 | iba/app/migration/archive/apply_catalogue_wording_v1_20260921.py | ONE-OFF migration -- escalation #1814 v6 (approved): applies the 48 REVISE rows' revised wording to wa_obs_question_catalogue.question_text, plus fixes the M0.5.11/M0.6.5 tier=NULL column-alignment bug found in the same audit. Run once, then set inactive=1. |  |  |  |
| apply_flesh_body_complex_2163_v1_20261018 | iba/app/migration/apply_flesh_body_complex_2163_v1_20261018.py | One-off migration, escalation #2163 (for #2162): re-codes the T-coded flesh/body terms to M47 in cluster_strong and links them to word 150 flesh in word_strong, from iba/docs/flesh-body-complex-spec-2163-v*-20261018.json. Writer: migration. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (same class as apply_1598_cluster_batch, #2107 triage E) |
| apply_verse_plaintext_column | iba/app/tools/_apply_verse_plaintext_column.py | One-time-but-re-runnable correction/backfill: populates verse.text (plain-text derived from verse.preview) via the shared lib/stepapi.py:preview_to_text function. Originally the sole source of that derivation (escalation #1063); now also imports it rather than duplicating it, since handlers/raw.py:verses_one calls the same function at insert time (escalation #1662, 2026-09-10 -- fixed the gap where 723 verse rows ingested after this script's original one-time run carried text=NULL despite cfg_column(verse.text).filled_by already claiming handlers/raw.py:verses). Useful going forward as the catch-up backfill for any row left behind by a future ingestion gap. Idempotent -- safe to re-run any time. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| assign_1807_unmapped_strongs_v1_20260921 | iba/app/migration/archive/assign_1807_unmapped_strongs_v1_20260921.py | ONE-OFF migration -- escalation #1807/#1817: assigns the 9 strongs Leg 3 found with zero cluster_strong allocation. 3 (G2375/H6446 -> T12, G4537 -> T3) fit an existing T-code once checked against every definition + live precedent; the other 6 (G2279/G2863/G3118/G5353/H1998/H8088A) genuinely fit none, researcher-confirmed T2. Run once, then set inactive=1. |  |  |  |
| assign_leg3_orphan_strongs_v1_20260915 | iba/app/migration/archive/assign_leg3_orphan_strongs_v1_20260915.py | ONE-OFF migration -- escalation #1606: registers the two new cfg_on_fail 'unclassified' rows + refreshes 3 cfg_step.does texts for the reconcile()-guarantee code change, and classifies the 111 live strongs Leg 3 found with zero cluster_strong allocation (T5/T6/T2, by hand, morph-pattern + individual gloss check). Run once, then set inactive=1. |  |  |  |
| backfill_all_strong_meaning_tree_gaps_v1_20260910 | iba/app/migration/archive/backfill_all_strong_meaning_tree_gaps_v1_20260910.py | backfill_all_strong_meaning_tree_gaps_v1_20260910.py -- broadened continuation of fix_strong_meaning_tree_collapse.py (2026-07-26), escalation #1655. Backfills every live strong code's own exact-variant strong_meaning_tree row where STEP has real content (519/522), leaving only genuine STEP-empty codes (3). Run once and verified live. |  |  |  |
| batchcontrol | iba/app/lib/batchcontrol.py | batchcontrol.py -- the single writer for run_batch (escalation #1756). start_batch/commit_batch/fail_batch wrap every long-running step's own API-call-plus-write unit; already_committed/content_key implement resume/skip. | ✓ |  |  |
| batchprogressreport | iba/app/lib/archive/batchprogressreport.py | batchprogressreport.py -- read-only live progress report generator over run_batch (escalation #1756), backing report.batch_progress / BatchProgress.ps1. |  |  |  |
| behaviour | iba/app/lib/behaviour.py | Read-only report of cfg_behaviour_class/cfg_behaviour_rule (escalations #715/#732/#733): writes the live rule set to behaviour.list_report_path. Run as step behaviour.list (handlers/reports.py) behind Behaviour.ps1 (#2207). Rules are written through configmaint, never by this module. | ✓ |  |  |
| bootstrap_behaviour_rules | iba/app/migration/bootstrap_behaviour_rules_v1_20260818.py | One-off migration: creates cfg_behaviour_class/cfg_behaviour_rule and seeds cycle-1 ('the obvious ones') content -- GR-DB-001/GR-PROC-001/GR-REF-001/GR-PROG-009 reworded as definitive statements. Escalation #715. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3 (creates + populates them), same class as cfgload.py, already exempted from usage-checks for the same reason. |
| bootstrap_behaviour_rules_cycle2 | iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | One-off migration: escalation #715 cycle 2 -- seeds cfg_behaviour_rule content from the Workflow/Claude_API, Workflow/SQLite, Workflow/Obsidian usage guides (2026-08-15, never previously folded in). Found unregistered during cycle 3's sweep (governance.new_utility_registration_timing gap) and registered retroactively. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| bootstrap_behaviour_rules_cycle3 | iba/app/migration/bootstrap_behaviour_rules_cycle3_v1_20260818.py | One-off migration: escalation #715 cycle 3 -- seeds cfg_behaviour_rule content from docs/interaction-preferences.md, CLAUDE.md sec9, the orphaned wa-operational-governance-v1_0 doc, cfg_escalation.chat_routing (cross-referenced), and confirmed feedback_* memory rules; adds governance.behaviour_boundary.* + governance.procedural_document_taxonomy settings. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| bootstrap_behaviour_rules_cycle4 | iba/app/migration/bootstrap_behaviour_rules_cycle4_v1_20260818.py | One-off migration: escalation #715 cycle 4 -- adds the development behaviour class (escalation #732) after a structural read-through (#733) of cycles 1-3. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| bootstrap_catalogue_overview_report_v1_20260829 | iba/app/migration/archive/bootstrap_catalogue_overview_report_v1_20260829.py | ONE-OFF migration, escalation #1007 -- registers the catalogue-report work package/step, report.obs_catalogue config, and the cataloguereport.py utility. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| bootstrap_decision_vs_defect_axis | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py | One-off migration: escalation #798/#799 Stage 1 -- cfg_behaviour_rule 'decision-points-are-terminal-not-inline', cfg_enum resolution_kind, the raise-time requirement, the new cfg_passage module table (with governance registration and 6 rows, replacing 4 cfg_setting.passage.* rows), and raw.zero_strongs_action. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| build_debate_report | iba/app/tools/build_debate_report.py | Step 6 debate report for one hib-continuity passage, run by Debate-Run.ps1. | ✓ | ✓ | app core, outside the utility config-density check |
| build_verse_lexical_window1_layer1_layer2_v1_20260904 | iba/app/migration/archive/build_verse_lexical_window1_layer1_layer2_v1_20260904.py | ONE-OFF migration, escalation #1383 -- builds the verse_lexical Window-1 Layer-1/Layer-2 schema+config (verse_lexical +8 cols, passage +2 cols, verse_lexical_note and cfg_lexical_code_class new tables, cfg_enum/cfg_method_rule/cfg_step/cfg_write_grant/cfg_report rows), seeds the negator/connective/party_divine lexicon, fixes the H0853 role bug, and backfills the 8 new columns across the whole existing corpus. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| catalogue_column_governance_v1_20260921 | iba/app/migration/archive/catalogue_column_governance_v1_20260921.py | ONE-OFF migration -- escalation #1818 v2: fixes prompt_seq (9 rows) + status/deleted disagreement (4 rows), registers cfg_enum for status/tier/scope, upgrades cfg_column.use for section/prompt_seq/tier/scope/status, marks section superseded by dimension. Run once, then set inactive=1. |  |  |  |
| cataloguereport | iba/app/lib/cataloguereport.py | report.obs_catalogue -- wa_obs_question_catalogue structural review, no findings joins | ✓ |  |  |
| cataloguewrite | iba/app/lib/cataloguewrite.py | obs_catalogue.update -- validated partial UPDATE of wa_obs_question_catalogue by obs_id, auto-filling last_modified/catalogue_version where not explicitly given. Escalation #1007. | ✓ |  |  |
| catchup_october_ledgers_2172_v1_20261022 | iba/app/migration/archive/catchup_october_ledgers_2172_v1_20261022.py | ONE-OFF -- escalation #2172 catch-up B: the October row ledgers into ib_observation through Strand-Reading Define, Context and Record; run_id CATCHUP-2172-B-20261022. inactive once run. |  | ✓ | one-off catch-up script (#2172 catch-up B), run once |
| cfg | iba/app/lib/cfg.py | cfg.py — the runtime config reader. THE ONLY WAY THE APP READS CONFIG. | ✓ | ✓ | defines .setting()/.enum() itself — the config reader; cannot call its own accessor. |
| cfgcheck | iba/app/lib/archive/cfgcheck.py | cfgcheck.py — the config-maintenance / validation utility for the app config. |  | ✓ | validates the raw seed dict before any Cfg/DB object exists — structurally cannot call .setting()/.enum(). |
| cfgload | iba/app/lib/archive/cfgload.py | cfgload.py — load the JSON SEEDS into the config tables in the DATABASE. |  | ✓ | writes the seed INTO the cfg_* tables (creates + populates them) — same class as migration/ scripts, already excluded from usage-checks for the same reason. |
| cfgquality | iba/app/lib/cfgquality.py | cfgquality.py — shared config-quality checks, used by BOTH handlers/configmaint.py (the | ✓ | ✓ | works directly against a raw sqlite3.Connection (not a Cfg wrapper), by design — usable from both configmaint.py (has a Cfg) and cfgreport.py (doesn't); queries cfg_setting/cfg_enum via raw SQL, not Cfg's convenience methods. Found 2026-07-30 only after fixing this same check's own text-collision false negative for this file — same class of legitimate zero as the other 11, not an oversight. |
| cfgreport | iba/app/lib/cfgreport.py | cfgreport.py — full-visibility config report, generated FROM the config store. | ✓ | ✓ | generates reports by querying cfg_* tables directly; the paths it needs (out_path/db_path) are resolved by its caller (configmaint.report), not read here. |
| charanswergenerate | iba/app/lib/charanswergenerate.py | charanswergenerate.py — the LLM-calling half of `cluster.answer` (the `char-answers` stage, | ✓ |  |  |
| charreadinggenerate | iba/app/lib/charreadinggenerate.py | charreadinggenerate.py — the LLM-calling half of `cluster.reading` (the `char-reading` stage, | ✓ |  |  |
| claude_md_rules_to_config_v1_20261021 | iba/app/migration/archive/claude_md_rules_to_config_v1_20261021.py | ONE-OFF migration -- escalation #2181: moves the rules CLAUDE.md held with no cfg_* home into config, every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2181-CLAUDE-MD-RULES-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| clear_content_index | iba/app/migration/clear_content_index_20260821.py | One-off migration: escalation #758 -- empties content_index + content_index_scan (the current design judged unsupportable, decommissioned pending redesign #770). | ✓ | ✓ | one-off migration script -- writes directly into content_index/content_index_scan via raw sqlite3, same class as cfgload.py |
| clusterassign | iba/app/lib/clusterassign.py | cluster.assign -- allocates strongs to M-code clusters | ✓ |  |  |
| clusterfamilyscan | iba/app/lib/archive/clusterfamilyscan.py | Escalation #1598: candidate-generation via strong_related lexical-family data instead of gloss-keyword matching, with proper-noun filtering. Not a bulk-apply tool -- surfaces candidates for individual verse-check + JSON-batch review via apply_1598_cluster_batch.py. Validated: reliable for place/party/collective candidates, unreliable for M-code thematic fit (documented in module docstring). |  |  |  |
| clusterreport | iba/app/lib/clusterreport.py | report.cluster -- cluster content/quality report | ✓ |  |  |
| clusterstatus | iba/app/lib/clusterstatus.py | clusterstatus.py — the `cluster.status` lifecycle transitions `#1697` designed but never built | ✓ |  |  |
| compliance | iba/app/lib/compliance.py | compliance.py -- rule compliance read at start and proved at close (#2173 P2): delivery of the rules, the session compliance file, its start and close checks. | ✓ |  |  |
| contentindex | iba/app/lib/contentindex.py | contentindex.py — file-content concordance search over .md files, keyed on Strong's numbers/glosses/words sourced from strong/word_registry. Round 2 of the manifest + content-search plan; file_manifest (round 1) is its coverage baseline. | ✓ |  |  |
| control_file_check_v1_20261021 | iba/app/migration/archive/control_file_check_v1_20261021.py | ONE-OFF migration -- escalation #2186: session-close control-file check SC15, every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2186-CONTROL-FILE-CHECK-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| control_kinds_add_tool_usage_v1_20261021 | iba/app/migration/archive/control_kinds_add_tool_usage_v1_20261021.py | ONE-OFF migration -- escalation #2187: adds tool_usage (USER-GUIDE.md) to session_close.control_kinds, every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2187-CONTROL-KINDS-TOOL-USAGE-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| control_map_v1_20261021 | iba/app/migration/archive/control_map_v1_20261021.py | ONE-OFF migration -- escalation #2180: the control map (cfg_control_home), every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2180-CONTROL-MAP-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| create_verse_meta_table_v1_20260909 | iba/app/migration/create_verse_meta_table_v1_20260909.py | Creates verse_meta (1:1 companion to verse, base-data grain -- language/testament/chapter/verse_num/passage linkage), one-off populates it from bible_research.db-informed design + iba.db's own osisId/cfg_book_order/verse_lexical/verse_passage, validates the result, and builds the 4 auto-sync triggers (verse/verse_lexical/verse_passage inserts, verse.deleted updates). Idempotent, safe to re-run. Escalation #1608. | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| create_vw_strong_gloss_v1_20260910 | iba/app/migration/archive/create_vw_strong_gloss_v1_20260910.py | create_vw_strong_gloss_v1_20260910.py -- creates/replaces vw_strong_gloss, a uniform gloss view unioning strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed (researcher instruction 2026-09-10). source column carries the literal source table name (researcher instruction, verbatim: 'adjust the view to show the label for the source table is a column'), not a short alias. NOTE: the view itself is deliberately NOT registered in cfg_table -- escalation #1654's incident (crashed Start-Iba.ps1, build_data_tables has no category filter for views) and #1658 (open, not yet decided how views should be registered safely). Re-runnable via --replace. |  |  |  |
| create_vw_strong_meaning_raw_v1_20260910 | iba/app/migration/create_vw_strong_meaning_raw_v1_20260910.py | Creates/replaces vw_strong_meaning_raw -- raw, unparsed union of strong_meaning_tree + strong_lexicon.lsj/.mounce, keyed by strong. Sibling to vw_strong_gloss (parsed) but one layer upstream -- no HTML stripped, no segmentation, nothing decided. Built for direct source-vs-parse comparison, escalation #1668. Re-runnable via --replace. NOTE: the view itself is deliberately NOT registered in cfg_table, same reasoning as vw_strong_gloss (escalation #1654's incident, #1658 open). | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| db | iba/app/lib/db.py | db.py — the DATA layer. Built FROM the config in the database. | ✓ |  |  |
| dbsnapshot | iba/app/lib/dbsnapshot.py | dbsnapshot.py — pre-write DB snapshots. THE GAP FOUND 2026-07-22: this app had no rollback | ✓ |  |  |
| debateaudit | iba/app/lib/debateaudit.py | debateaudit.py — the shared per-row CRUD audit trail for every debate writer (`hib.set`, | ✓ | ✓ | writes to a fixed table name (debate_change_detail) only -- no cfg.setting()/cfg.enum() usage by design, same shape as other pure DB-write utilities already exempt |
| debaterun | iba/app/lib/debaterun.py | Debate-Run.ps1 readiness checks (mirrors each operations-ingest/build-passages handler own gate) + staging-payload path resolution (passage.debate_staging_path_pattern) | ✓ |  |  |
| dedupe_ib_node_2verses_v1_20260923 | iba/app/migration/archive/dedupe_ib_node_2verses_v1_20260923.py | ONE-OFF migration -- escalation #1847: 2Cor.8.16 and 2Pet.1.5 carried redundant ib_node rows citing the identical occurrence under an already-consolidated observation (residue from the #1832/#1834 dedup rework before its final form). ib_node has no soft-delete column, so cleanup is a physical DELETE keeping the earliest node per duplicate group. Run 2026-09-23: 29 groups, 36 redundant rows deleted (live scope grown slightly from the v4 estimate of 27/~30 -- more accrued between estimate and run). Idempotent, but inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| delete_strongs_not_in_verses_v1_20260910 | iba/app/migration/archive/delete_strongs_not_in_verses_v1_20260910.py | delete_strongs_not_in_verses_v1_20260910.py -- one-off migration, researcher-directed 2026-09-10 ('delete strongs not in verses'). Soft-deletes the 250 strong rows found in escalation #1613's audit with zero live span AND zero strong_verse reference (confirmed not verse-gap-by-design), cascaded across 10 dependent tables. Dry-run tested, then committed and verified live: 250/250/241/1069/242/409/262/284/248/262 rows soft-deleted respectively. |  |  |  |
| devmode_rule_from_command_v1_20261021 | iba/app/migration/archive/devmode_rule_from_command_v1_20261021.py | ONE-OFF migration -- escalation #2183: moves the Developer Mode scope and conduct rule out of the /developer-mode command into cfg_behaviour_rule, every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2183-DEVMODE-RULE-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| docs_archive_pointers_v1_20261021 | iba/app/migration/archive/docs_archive_pointers_v1_20261021.py | ONE-OFF migration -- escalation #2191: repoints the cfg texts naming docs/prose-store-architecture.md after docs/ was archived, through configmaint.apply_logged under run_id DEVMODE-2191-DOCS-ARCHIVE-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| drop_verse_meta_genre_column_v1_20260909 | iba/app/migration/drop_verse_meta_genre_column_v1_20260909.py | ONE-OFF migration -- escalation #1608: drops verse_meta.genre (ALTER TABLE DROP COLUMN) and deletes its cfg_column row, per researcher verdict that genre has no role in this study's verse-focused lexical analysis. Already run live. passage.genre was NOT touched (stays inactive=1, not dropped -- researcher named verse-meta specifically). | ✓ | ✓ | one-off migration/tool that has already run; zero config reads is legitimate (#2107 triage E, approved under #2108) |
| enforce_span_grounding_word_level_v1_20260923 | iba/app/migration/archive/enforce_span_grounding_word_level_v1_20260923.py | ONE-OFF migration -- researcher correction 2026-09-23, same day as #1849 follow-on: prior 'this term' rewording was still generic (answerable without the verse). Reworded to require span/morph grounding, matching every other live question's own 'In this verse...' convention. Run once, then set inactive=1. |  |  |  |
| engine_audit | engine/archive/audit.py | Audit framework -- WR-01 through WR-20, run after all writes. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_audit_word | engine/archive/audit_word.py | AUDIT_WORD mode (v4) -- Pre-A1 through A11, unified new-word + re-audit pipeline. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_backup | engine/archive/backup.py | DB backup management (SG-01, SG-12, SG-13) -- timestamped pre-run backup, abort if it fails. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_cli | engine/archive/engine.py | CLI entry point (python -m engine.engine). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_constants | engine/constants.py | Shared constants. | ✓ | ✓ | values move to cfg_setting instead |
| engine_db | engine/archive/db.py | DB access helpers (wraps analytics/db_client.py). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_flag | engine/archive/flag_engine.py | Derivable flag evaluation (S5/N16/A7). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_gap_fill | engine/archive/gap_fill.py | GAP_FILL mode (S1-S8), superseded by audit_word. |  |  |  |
| engine_meaning_parser | engine/archive/meaning_parser.py | Meaning text parser -> wa_meaning_parsed/_sense/_stem, wa_lsj_parsed. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_migrate | engine/migrate.py | Schema migration runner v2.2->v3.0 (M01-M10). | ✓ | ✓ | one-shot historical, same class as iba/app/migration/* |
| engine_register | engine/archive/register.py | REGISTER subcommand -- new word_registry row. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_report | engine/archive/report.py | Word overview report. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_run_log | engine/archive/run_log.py | engine_run_log/word_run_state write helpers. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_softdelete | engine/archive/softdelete.py | Shared soft-delete cascade helpers (H1-H3, H5). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_span_filter | engine/archive/span_filter.py | STEP masterSearch HTML span filtering (Sec5.2 v4). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| enrich_verse_relational_reading_v1_20260921 | iba/app/migration/archive/enrich_verse_relational_reading_v1_20260921.py | ONE-OFF migration -- escalation #1819: enriches M0.6.5 with structured relation-type vocabulary, adds new M0.6.6 (whole-network relational synthesis). Run once, then set inactive=1. |  |  |  |
| escalation | iba/app/lib/escalation.py | escalation.py -- util.escalation. The authoritative record of open items in the project: errors, issues, and building tasks. All runtime errors are reported in it; both Claude and Researcher record emerging issues, tasks, followups as feedback or to get feedback. It pauses a running process and allows it to resume at resume_point when answered (dispatcher-tied), or tracks a backlog item through raise/update/correction (manual -- correction is error-correction only, escalation #774). Five types (task/issue/notice/run_error/config), each a distinct shape of life -- see USER-GUIDE.md sec4. Type thread (escalation #2000): the open threads register, alias OT-nn, with item and response child tables (escalation_thread_item, escalation_thread_item_response) -- see USER-GUIDE.md sec4. | ✓ |  |  |
| escalationcontext | iba/app/lib/escalationcontext.py | escalationcontext.py -- what every open escalation points to (#2173 P1): every file named in any field of any version, resolved to its latest live version; findings missing / bare. | ✓ |  |  |
| export_tables_csv | iba/app/tools/export_tables_csv.py | CSV dump of data tables, used by the table-export work package. | ✓ | ✓ | app core, outside the utility config-density check |
| filingkit | iba/app/lib/filingkit.py | filingkit.py -- the project-wide filing utility: naming-shape, same-day -v{n} versioning, archive-before-overwrite, for any writer. Generalises reportkit.oneoff_path(), which now delegates here. Escalation #863/#971/#992. Calls cfg.setting() directly (governance.oneoff_* fallback defaults) -- not config_exempt, a real call site. | ✓ |  |  |
| fix_characteristic_terminology_stage1_v1_20260923 | iba/app/migration/archive/fix_characteristic_terminology_stage1_v1_20260923.py | ONE-OFF migration -- researcher instruction 2026-09-23: replaces cluster/characteristic wording with M-code word/role-T3 wording in D7.7.1/M0.6.5/M0.6.6 (verse-reading is cluster-agnostic per #1810/#1824). Run once, then set inactive=1. |  |  |  |
| fix_dead_gate_citations_v1_20260921 | iba/app/migration/archive/fix_dead_gate_citations_v1_20260921.py | ONE-OFF migration -- escalation #1823: fixes 15 questions citing a per-verse gate question by code that is STRUCTURALLY-UNREACHABLE, inlining the filter condition in plain language instead. Run once, then set inactive=1. |  |  |  |
| fix_dispatcher_answerrun_795 | iba/app/migration/fix_dispatcher_answerrun_795_20260822.py | Escalation #795: split the dispatcher shape's collapsed approve/reject/revise transition into 3 distinct rules, and retargeted cfg_status_flow to match. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| fix_from_id_closed_items | iba/app/migration/fix_from_id_closed_items_20260821.py | One-off data repair: escalation #767 v3 -- corrects from_id on 10 closed/completed escalation rows where the correct spawn parent was discoverable from the item's own recorded text; update() cannot touch closed items, so this calls _snapshot() directly. | ✓ | ✓ | one-off migration script -- calls the real escalation._snapshot() mechanism directly, same class as fix_escalation_short_description_and_columns_20260820.py |
| fix_ib_node_verse_reference_doc_v1_20260922 | iba/app/migration/archive/fix_ib_node_verse_reference_doc_v1_20260922.py | ONE-OFF migration, escalation #1824 -- corrects cfg_column.use for ib_node.verse_reference, which wrongly claimed resolution against verse.reference when the real write path uses verse.osisId. inactive=1 once applied. |  |  |  |
| fix_no_vocab_shells_v1_20260910 | iba/app/migration/archive/fix_no_vocab_shells_v1_20260910.py | fix_no_vocab_shells_v1_20260910.py -- one-off migration, researcher-directed 2026-09-10 (escalation #1647). Creates strong/strong_sense/strong_meaning_tree shell rows for H3673/H3674 (Dan.3.2-27, Ezra.4.7 -- real words, STEP itself has no vocab data), sense_text/head literally 'no known meaning'. Run once and verified live; Lexicon-Parse.ps1 -Step Parse run separately afterward to generate the matching strong_meaning_parsed row through the normal pipeline. |  |  |  |
| fix_not_count_2207_v1_20261022 | iba/app/migration/archive/fix_not_count_2207_v1_20261022.py | ONE-OFF migration -- escalation #2207: wires 3 enum expectations and retires apply_session_patch, through configmaint.apply_logged under run_id DEVMODE-2207-FIX-NOT-COUNT-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| fix_primary_term_terminology_v1_20260921 | iba/app/migration/archive/fix_primary_term_terminology_v1_20260921.py | ONE-OFF migration -- escalation #1822: replaces undefined 'the primary term' with 'this term' in M0.4.1/M0.5.2/M0.5.3/M0.6.1. Run once, then set inactive=1. |  |  |  |
| fix_stage1_governance_gaps_v1_20260922 | iba/app/migration/archive/fix_stage1_governance_gaps_v1_20260922.py | ONE-OFF migration, escalation #1824 -- fixes 5 real governance gaps found by a full audit of 2026-09-21/22's Stage 1 work (2 unregistered/orphaned cfg_setting keys, 1 stale cfg_method_rule, 1 undocumented behaviour rule, 1 hardcoded report path). inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| flag_management_build_v1_20260823 | iba/app/migration/archive/flag_management_build_v1_20260823.py | ONE-OFF migration, escalation #833 (Flag Management) -- repurposes wa_quality_flag_types/wa_data_quality_flags for prose-quality checks, adds cfg_column.inactive, retires phase2_flag_types, marks 2 dead columns inactive, records wa_session_research_flags' retention. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| folderpurpose | iba/app/lib/folderpurpose.py | folderpurpose.py -- folder_purpose table: seed/refresh from a live directory scan (Method A), cross-check against cfg_setting *_dir/*_path values (Method B), and hand-edit type/status/usage_description (Method C). Escalation #971. | ✓ |  |  |
| handlers_base | iba/app/handlers/base.py | Handler contract: Ctx, Outcome, ok/fail/escalate, used by every handler. | ✓ | ✓ | app core, outside the utility config-density check |
| handlers_catalogue | iba/app/handlers/catalogue.py | Thin dispatcher adapter over cataloguewrite.py, registers obs_catalogue.update as a work-package step. | ✓ | ✓ | thin step wrapper: checks -ObsId and -Set; the write and its rules are in lib/cataloguewrite.py (#2207 decision 3a) |
| handlers_compliance | iba/app/handlers/compliance.py | handlers/compliance.py -- the compliance.template and compliance.check_start steps (#2173 P2). | ✓ | ✓ | thin step wrappers: every setting is read in lib/compliance.py, which they call |
| handlers_narrativeregister | iba/app/handlers/narrativeregister.py | handlers/narrativeregister.py -- the run.py handlers for work package narrative-register (one per Narrative-Register.ps1 action); the logic is in lib/narrativeregister.py (escalation #2110). | ✓ |  |  |
| handlers_strandreading | iba/app/handlers/strandreading.py | handlers/strandreading.py -- the run.py handlers for work package strand-reading (one per Strand-Reading.ps1 step); the logic is in lib/strandreading.py (escalation #2172). | ✓ |  |  |
| history_out_of_read_path_v1_20261021 | iba/app/migration/archive/history_out_of_read_path_v1_20261021.py | ONE-OFF migration -- escalation #2183: replaced history out of the read path (rule 96), every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2183-HISTORY-OUT-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| iba_app_handlers_archive_candidate | iba/app/handlers/archive/candidate.py | Retired (#2200): not in a utility or module. Was iba/app/handlers/candidate.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_handlers_archive_narrative | iba/app/handlers/archive/narrative.py | Retired (#2201). Was iba/app/handlers/narrative.py. |  | ✓ | retired script (#2201): kept for reference only; use needs the researcher's approval |
| iba_app_handlers_archive_wordaudit | iba/app/handlers/archive/wordaudit.py | Retired (#2201). Was iba/app/handlers/wordaudit.py. |  | ✓ | retired script (#2201): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_candidate_seed_referent_columns | iba/app/migration/archive/add_candidate_seed_referent_columns.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_candidate_seed_referent_columns.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_candidate_seed_strong_variant | iba/app/migration/archive/add_candidate_seed_strong_variant.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_candidate_seed_strong_variant.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_table_category_column_20260831 | iba/app/migration/archive/add_cfg_table_category_column_20260831.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_table_category_column_20260831.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_table_database_column | iba/app/migration/archive/add_cfg_table_database_column.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_table_database_column.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_table_inactive_column | iba/app/migration/archive/add_cfg_table_inactive_column.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_table_inactive_column.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_table_purpose_and_success_columns_20260830 | iba/app/migration/archive/add_cfg_table_purpose_and_success_columns_20260830.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_table_purpose_and_success_columns_20260830.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_table_purpose_review_20260830 | iba/app/migration/archive/add_cfg_table_purpose_review_20260830.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_table_purpose_review_20260830.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_unique_database_column_v1_20260818 | iba/app/migration/archive/add_cfg_unique_database_column_v1_20260818.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_unique_database_column_v1_20260818.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_utility_config_exempt | iba/app/migration/archive/add_cfg_utility_config_exempt.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_utility_config_exempt.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_cfg_write_grant_database_column | iba/app/migration/archive/add_cfg_write_grant_database_column.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_cfg_write_grant_database_column.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_debate_change_detail_writer_column_20260808 | iba/app/migration/archive/add_debate_change_detail_writer_column_20260808.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_debate_change_detail_writer_column_20260808.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_escalation_state_in_progress | iba/app/migration/archive/add_escalation_state_in_progress.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_escalation_state_in_progress.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_healing_word_strong_20260810 | iba/app/migration/archive/add_healing_word_strong_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_healing_word_strong_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_hib_centric_traversal_method_rules_20260807 | iba/app/migration/archive/add_hib_centric_traversal_method_rules_20260807.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_hib_centric_traversal_method_rules_20260807.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_lexical_weight_and_closing_checks_20260807 | iba/app/migration/archive/add_lexical_weight_and_closing_checks_20260807.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_lexical_weight_and_closing_checks_20260807.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_lexicon_parse_settings | iba/app/migration/archive/add_lexicon_parse_settings.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_lexicon_parse_settings.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_passage_story_columns | iba/app/migration/archive/add_passage_story_columns.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_passage_story_columns.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_verse_lexical_updated_at_v1_20260905 | iba/app/migration/archive/add_verse_lexical_updated_at_v1_20260905.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_verse_lexical_updated_at_v1_20260905.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_add_work_package_chained_column | iba/app/migration/archive/add_work_package_chained_column.py | Retired (#2200): not in a utility or module. Was iba/app/migration/add_work_package_chained_column.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_allocate_strongs | iba/app/migration/archive/allocate_strongs.py | Retired (#2200): not in a utility or module. Was iba/app/migration/allocate_strongs.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_apply_cluster_alloc_v1_3_20260812 | iba/app/migration/archive/apply_cluster_alloc_v1_3_20260812.py | Retired (#2200): not in a utility or module. Was iba/app/migration/apply_cluster_alloc_v1_3_20260812.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_apply_m47_reallocation_1880_v1_20260928 | iba/app/migration/archive/apply_m47_reallocation_1880_v1_20260928.py | Retired (#2200): not in a utility or module. Was iba/app/migration/apply_m47_reallocation_1880_v1_20260928.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_apply_prior_reassignments_v1_1_20260812 | iba/app/migration/archive/apply_prior_reassignments_v1_1_20260812.py | Retired (#2200): not in a utility or module. Was iba/app/migration/apply_prior_reassignments_v1_1_20260812.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_apply_semantic_allocation | iba/app/migration/archive/apply_semantic_allocation.py | Retired (#2200): not in a utility or module. Was iba/app/migration/apply_semantic_allocation.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_archive_oneoff_report_clutter_20260808 | iba/app/migration/archive/archive_oneoff_report_clutter_20260808.py | Retired (#2200): not in a utility or module. Was iba/app/migration/archive_oneoff_report_clutter_20260808.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_cfg_change_detail_2000_v1_20261012 | iba/app/migration/archive/backfill_cfg_change_detail_2000_v1_20261012.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_cfg_change_detail_2000_v1_20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_foundational_cfg_tables_v1_20260818 | iba/app/migration/archive/backfill_foundational_cfg_tables_v1_20260818.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_foundational_cfg_tables_v1_20260818.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_healing_exact_variant_meaning_20260810 | iba/app/migration/archive/backfill_healing_exact_variant_meaning_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_healing_exact_variant_meaning_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_morphless_span_fix_20260810 | iba/app/migration/archive/backfill_morphless_span_fix_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_morphless_span_fix_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_passage_tracking_daniel | iba/app/migration/archive/backfill_passage_tracking_daniel.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_passage_tracking_daniel.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_receive_exact_variant_meaning_20260810 | iba/app/migration/archive/backfill_receive_exact_variant_meaning_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_receive_exact_variant_meaning_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_backfill_subgroup_columns_char_reading_answers_v1_20260918 | iba/app/migration/archive/backfill_subgroup_columns_char_reading_answers_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/backfill_subgroup_columns_char_reading_answers_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_book_narrative_generate | iba/app/migration/archive/bootstrap_book_narrative_generate.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_book_narrative_generate.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_book_narrative_validate | iba/app/migration/archive/bootstrap_book_narrative_validate.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_book_narrative_validate.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_cfg_utility | iba/app/migration/archive/bootstrap_cfg_utility.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_cfg_utility.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_cluster_strong_evidence_columns_20260812 | iba/app/migration/archive/bootstrap_cluster_strong_evidence_columns_20260812.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_cluster_strong_evidence_columns_20260812.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_cluster_tables_20260811 | iba/app/migration/archive/bootstrap_cluster_tables_20260811.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_cluster_tables_20260811.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_configuration_maintenance | iba/app/migration/archive/bootstrap_configuration_maintenance.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_configuration_maintenance.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_content_index | iba/app/migration/archive/bootstrap_content_index.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_content_index.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_file_manifest | iba/app/migration/archive/bootstrap_file_manifest.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_file_manifest.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_inactive_column | iba/app/migration/archive/bootstrap_inactive_column.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_inactive_column.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_lexicon_parsed_layer | iba/app/migration/archive/bootstrap_lexicon_parsed_layer.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_lexicon_parsed_layer.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_new_reports_phase1 | iba/app/migration/archive/bootstrap_new_reports_phase1.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_new_reports_phase1.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_oneoff_report_naming | iba/app/migration/archive/bootstrap_oneoff_report_naming.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_oneoff_report_naming.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_passage_debate_report | iba/app/migration/archive/bootstrap_passage_debate_report.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_passage_debate_report.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_passage_debate_sync | iba/app/migration/archive/bootstrap_passage_debate_sync.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_passage_debate_sync.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_project_database_enum_v1_20260818 | iba/app/migration/archive/bootstrap_project_database_enum_v1_20260818.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_project_database_enum_v1_20260818.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_prose_authority_v1_20260818 | iba/app/migration/archive/bootstrap_prose_authority_v1_20260818.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_prose_authority_v1_20260818.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_quality_validate_steps | iba/app/migration/archive/bootstrap_quality_validate_steps.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_quality_validate_steps.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_raw_backfill | iba/app/migration/archive/bootstrap_raw_backfill.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_raw_backfill.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_report_content_governance | iba/app/migration/archive/bootstrap_report_content_governance.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_report_content_governance.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_report_csv_virtual_table | iba/app/migration/archive/bootstrap_report_csv_virtual_table.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_report_csv_virtual_table.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_report_persistence_governance | iba/app/migration/archive/bootstrap_report_persistence_governance.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_report_persistence_governance.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_reports_registration | iba/app/migration/archive/bootstrap_reports_registration.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_reports_registration.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_research_db_cfg_table | iba/app/migration/archive/bootstrap_research_db_cfg_table.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_research_db_cfg_table.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_retention_table_export_registration | iba/app/migration/archive/bootstrap_retention_table_export_registration.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_retention_table_export_registration.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_setting_module_column | iba/app/migration/archive/bootstrap_setting_module_column.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_setting_module_column.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_span_reading | iba/app/migration/archive/bootstrap_span_reading.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_span_reading.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_step_kind | iba/app/migration/archive/bootstrap_step_kind.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_step_kind.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_strong_origin_column_20260811 | iba/app/migration/archive/bootstrap_strong_origin_column_20260811.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_strong_origin_column_20260811.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_verse_analysis_report | iba/app/migration/archive/bootstrap_verse_analysis_report.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_verse_analysis_report.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_whole_book_read | iba/app/migration/archive/bootstrap_whole_book_read.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_whole_book_read.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_word_audit | iba/app/migration/archive/bootstrap_word_audit.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_word_audit.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_bootstrap_word_registry_span_report | iba/app/migration/archive/bootstrap_word_registry_span_report.py | Retired (#2200): not in a utility or module. Was iba/app/migration/bootstrap_word_registry_span_report.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_base_all_books | iba/app/migration/archive/build_base_all_books.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_base_all_books.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_cfg_index_table | iba/app/migration/archive/build_cfg_index_table.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_cfg_index_table.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_closing_sections_schema | iba/app/migration/archive/build_closing_sections_schema.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_closing_sections_schema.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_hib_change_detail_table_20260808 | iba/app/migration/archive/build_hib_change_detail_table_20260808.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_hib_change_detail_table_20260808.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_method_rule_table | iba/app/migration/archive/build_method_rule_table.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_method_rule_table.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_operations_schema | iba/app/migration/archive/build_operations_schema.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_operations_schema.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_build_quality_check_table | iba/app/migration/archive/build_quality_check_table.py | Retired (#2200): not in a utility or module. Was iba/app/migration/build_quality_check_table.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_catalogue_cleanup_v2_20260917 | iba/app/migration/archive/catalogue_cleanup_v2_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/catalogue_cleanup_v2_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_clean_invalid_question_code_observations_v1_20260917 | iba/app/migration/archive/clean_invalid_question_code_observations_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/clean_invalid_question_code_observations_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_cleanout_retired_chapter_generate_config | iba/app/migration/archive/cleanout_retired_chapter_generate_config.py | Retired (#2200): not in a utility or module. Was iba/app/migration/cleanout_retired_chapter_generate_config.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_cleanout_retired_passage_config | iba/app/migration/archive/cleanout_retired_passage_config.py | Retired (#2200): not in a utility or module. Was iba/app/migration/cleanout_retired_passage_config.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_cleanout_retired_verse_span_meaning_config | iba/app/migration/archive/cleanout_retired_verse_span_meaning_config.py | Retired (#2200): not in a utility or module. Was iba/app/migration/cleanout_retired_verse_span_meaning_config.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_clear_dan1_stale_passage_20260807 | iba/app/migration/archive/clear_dan1_stale_passage_20260807.py | Retired (#2200): not in a utility or module. Was iba/app/migration/clear_dan1_stale_passage_20260807.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_complete_method_config_20260807 | iba/app/migration/archive/complete_method_config_20260807.py | Retired (#2200): not in a utility or module. Was iba/app/migration/complete_method_config_20260807.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_correct_dan_1_boundary_range | iba/app/migration/archive/correct_dan_1_boundary_range.py | Retired (#2200): not in a utility or module. Was iba/app/migration/correct_dan_1_boundary_range.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_create_cluster_reading_pipeline_tables_v1_20260916 | iba/app/migration/archive/create_cluster_reading_pipeline_tables_v1_20260916.py | Retired (#2200): not in a utility or module. Was iba/app/migration/create_cluster_reading_pipeline_tables_v1_20260916.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_create_observation_enhancer_tables_v1_20260920 | iba/app/migration/archive/create_observation_enhancer_tables_v1_20260920.py | Retired (#2200): not in a utility or module. Was iba/app/migration/create_observation_enhancer_tables_v1_20260920.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_create_run_batch_table_v1_20260918 | iba/app/migration/archive/create_run_batch_table_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/create_run_batch_table_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_delete_blank_tag_candidates | iba/app/migration/archive/delete_blank_tag_candidates.py | Retired (#2200): not in a utility or module. Was iba/app/migration/delete_blank_tag_candidates.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_design_and_backfill_char_windows_v1_20260918 | iba/app/migration/archive/design_and_backfill_char_windows_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/design_and_backfill_char_windows_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_drop_cluster_gloss_v1_20260917 | iba/app/migration/archive/drop_cluster_gloss_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/drop_cluster_gloss_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_crash_review_rollout_20260821 | iba/app/migration/archive/escalation_crash_review_rollout_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_crash_review_rollout_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_explicit_state_priority_fix_20260821 | iba/app/migration/archive/escalation_explicit_state_priority_fix_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_explicit_state_priority_fix_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_open_threads_import_v1_20261012 | iba/app/migration/archive/escalation_open_threads_import_v1_20261012.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_open_threads_import_v1_20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_open_threads_v1_20261012 | iba/app/migration/archive/escalation_open_threads_v1_20261012.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_open_threads_v1_20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_redesign_v1_20260819 | iba/app/migration/archive/escalation_redesign_v1_20260819.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_redesign_v1_20260819.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_redesign_v1_20260819_rollback | iba/app/migration/archive/escalation_redesign_v1_20260819_ROLLBACK.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_redesign_v1_20260819_ROLLBACK.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_redesign_v2_20260820 | iba/app/migration/archive/escalation_redesign_v2_20260820.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_redesign_v2_20260820.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_register_v9_build_20260821 | iba/app/migration/archive/escalation_register_v9_build_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_register_v9_build_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_reset_v1_20260816 | iba/app/migration/archive/escalation_reset_v1_20260816.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_reset_v1_20260816.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_thread_config_corrections_v1_20261012 | iba/app/migration/archive/escalation_thread_config_corrections_v1_20261012.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_thread_config_corrections_v1_20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_thread_lifecycle_v1_20261012 | iba/app/migration/archive/escalation_thread_lifecycle_v1_20261012.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_thread_lifecycle_v1_20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_thread_reassign_keeps_state_v1_20261012 | iba/app/migration/archive/escalation_thread_reassign_keeps_state_v1_20261012.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_thread_reassign_keeps_state_v1_20261012.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_v1_load_20260821 | iba/app/migration/archive/escalation_v1_load_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_v1_load_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_escalation_v1_snapshot_20260821 | iba/app/migration/archive/escalation_v1_snapshot_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/escalation_v1_snapshot_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_extend_tag_vocabulary_v1_20260917 | iba/app/migration/archive/extend_tag_vocabulary_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/extend_tag_vocabulary_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_family_reallocation_v1_20260905 | iba/app/migration/archive/family_reallocation_v1_20260905.py | Retired (#2200): not in a utility or module. Was iba/app/migration/family_reallocation_v1_20260905.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_filingkit_build_v1_20260828 | iba/app/migration/archive/filingkit_build_v1_20260828.py | Retired (#2200): not in a utility or module. Was iba/app/migration/filingkit_build_v1_20260828.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_cfg_column_fk_gaps | iba/app/migration/archive/fix_cfg_column_fk_gaps.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_cfg_column_fk_gaps.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_cluster_anomalies_v2_20260917 | iba/app/migration/archive/fix_cluster_anomalies_v2_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_cluster_anomalies_v2_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_cluster_keyword_collisions_v1_20260917 | iba/app/migration/archive/fix_cluster_keyword_collisions_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_cluster_keyword_collisions_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_cluster_subgroup_unique_constraints_v1_20260917 | iba/app/migration/archive/fix_cluster_subgroup_unique_constraints_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_cluster_subgroup_unique_constraints_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_compound_pk_registration_v1_20260818 | iba/app/migration/archive/fix_compound_pk_registration_v1_20260818.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_compound_pk_registration_v1_20260818.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_escalation_history_write_grant_20260820 | iba/app/migration/archive/fix_escalation_history_write_grant_20260820.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_escalation_history_write_grant_20260820.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_escalation_short_description_and_columns_20260820 | iba/app/migration/archive/fix_escalation_short_description_and_columns_20260820.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_escalation_short_description_and_columns_20260820.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_escalation_titles_v2_20260820 | iba/app/migration/archive/fix_escalation_titles_v2_20260820.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_escalation_titles_v2_20260820.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_from_id_mutability_20260821 | iba/app/migration/archive/fix_from_id_mutability_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_from_id_mutability_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_hib_is_human_only_method_rule | iba/app/migration/archive/fix_hib_is_human_only_method_rule.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_hib_is_human_only_method_rule.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_lexical_meaning_batch_scaling_v1_20260917 | iba/app/migration/archive/fix_lexical_meaning_batch_scaling_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_lexical_meaning_batch_scaling_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_missing_write_grants_v1_20260818 | iba/app/migration/archive/fix_missing_write_grants_v1_20260818.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_missing_write_grants_v1_20260818.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_module_blocking_enforced_by_20260821 | iba/app/migration/archive/fix_module_blocking_enforced_by_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_module_blocking_enforced_by_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_nonhuman_scope_method_rule | iba/app/migration/archive/fix_nonhuman_scope_method_rule.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_nonhuman_scope_method_rule.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_run_batch_unique_constraint_v1_20260918 | iba/app/migration/archive/fix_run_batch_unique_constraint_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_run_batch_unique_constraint_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_strong_meaning_tree_collapse | iba/app/migration/archive/fix_strong_meaning_tree_collapse.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_strong_meaning_tree_collapse.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_fix_stuck_run_states | iba/app/migration/archive/fix_stuck_run_states.py | Retired (#2200): not in a utility or module. Was iba/app/migration/fix_stuck_run_states.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_folder_purpose_autoassess_build_v1_20260828 | iba/app/migration/archive/folder_purpose_autoassess_build_v1_20260828.py | Retired (#2200): not in a utility or module. Was iba/app/migration/folder_purpose_autoassess_build_v1_20260828.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_folder_purpose_build_v1_20260828 | iba/app/migration/archive/folder_purpose_build_v1_20260828.py | Retired (#2200): not in a utility or module. Was iba/app/migration/folder_purpose_build_v1_20260828.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_import_legacyregistry | iba/app/migration/archive/Import-LegacyRegistry.ps1 | Retired (#2200): not in a utility or module. Was iba/app/migration/Import-LegacyRegistry.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_import_seed | iba/app/migration/archive/import_seed.py | Retired (#2200): not in a utility or module. Was iba/app/migration/import_seed.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_legacy_import | iba/app/migration/archive/legacy_import.py | Retired (#2200): not in a utility or module. Was iba/app/migration/legacy_import.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_make_verse_lexical_note_passage_id_nullable_v1_20260905 | iba/app/migration/archive/make_verse_lexical_note_passage_id_nullable_v1_20260905.py | Retired (#2200): not in a utility or module. Was iba/app/migration/make_verse_lexical_note_passage_id_nullable_v1_20260905.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_mark_bible_research_findings_inactive_v1_20260924 | iba/app/migration/archive/mark_bible_research_findings_inactive_v1_20260924.py | Retired (#2200): not in a utility or module. Was iba/app/migration/mark_bible_research_findings_inactive_v1_20260924.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_merge_m17_into_m16_v1_20260906 | iba/app/migration/archive/merge_m17_into_m16_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/merge_m17_into_m16_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_merge_m27_into_m55_v1_20260906 | iba/app/migration/archive/merge_m27_into_m55_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/merge_m27_into_m55_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_merge_m29_into_m18_v1_20260906 | iba/app/migration/archive/merge_m29_into_m18_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/merge_m29_into_m18_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_merge_m38_into_m45_v1_20260906 | iba/app/migration/archive/merge_m38_into_m45_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/merge_m38_into_m45_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_migrate_obs_question_catalogue_to_iba_v1_20260916 | iba/app/migration/archive/migrate_obs_question_catalogue_to_iba_v1_20260916.py | Retired (#2200): not in a utility or module. Was iba/app/migration/migrate_obs_question_catalogue_to_iba_v1_20260916.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_move_g2983_suffering_to_receive_20260810 | iba/app/migration/archive/move_g2983_suffering_to_receive_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/move_g2983_suffering_to_receive_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_pathaudit_build_v1_20260828 | iba/app/migration/archive/pathaudit_build_v1_20260828.py | Retired (#2200): not in a utility or module. Was iba/app/migration/pathaudit_build_v1_20260828.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_populate_cfg_index_rows | iba/app/migration/archive/populate_cfg_index_rows.py | Retired (#2200): not in a utility or module. Was iba/app/migration/populate_cfg_index_rows.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_progressive_relational_verse_reading_v1_20260917 | iba/app/migration/archive/progressive_relational_verse_reading_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/progressive_relational_verse_reading_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_prose_output_dirs_build_v1_20260828 | iba/app/migration/archive/prose_output_dirs_build_v1_20260828.py | Retired (#2200): not in a utility or module. Was iba/app/migration/prose_output_dirs_build_v1_20260828.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_reactivate_passage_quality | iba/app/migration/archive/reactivate_passage_quality.py | Retired (#2200): not in a utility or module. Was iba/app/migration/reactivate_passage_quality.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_realign_catalogue_to_dimensions_v1_20260917 | iba/app/migration/archive/realign_catalogue_to_dimensions_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/realign_catalogue_to_dimensions_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rebuild_escalation_from_export_20260821 | iba/app/migration/archive/rebuild_escalation_from_export_20260821.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rebuild_escalation_from_export_20260821.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rebuild_escalation_rules_config_20260820 | iba/app/migration/archive/rebuild_escalation_rules_config_20260820.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rebuild_escalation_rules_config_20260820.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rebuild_span_combined_units | iba/app/migration/archive/rebuild_span_combined_units.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rebuild_span_combined_units.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rebuild_verse_lexical_layer1_v1_20260916 | iba/app/migration/archive/rebuild_verse_lexical_layer1_v1_20260916.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rebuild_verse_lexical_layer1_v1_20260916.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_reclassify_g0627_to_t3_v1_20260917 | iba/app/migration/archive/reclassify_g0627_to_t3_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/reclassify_g0627_to_t3_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_reconcile_daniel_debate_paths | iba/app/migration/archive/reconcile_daniel_debate_paths.py | Retired (#2200): not in a utility or module. Was iba/app/migration/reconcile_daniel_debate_paths.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_reconcile_daniel_debate_paths_20260808 | iba/app/migration/archive/reconcile_daniel_debate_paths_20260808.py | Retired (#2200): not in a utility or module. Was iba/app/migration/reconcile_daniel_debate_paths_20260808.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_cluster_answer_step_v1_20260918 | iba/app/migration/archive/register_cluster_answer_step_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_cluster_answer_step_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_cluster_reading_step_v1_20260918 | iba/app/migration/archive/register_cluster_reading_step_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_cluster_reading_step_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_cluster_subgroup_step_v1_20260917 | iba/app/migration/archive/register_cluster_subgroup_step_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_cluster_subgroup_step_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_ib_observation_enums_v1_20260917 | iba/app/migration/archive/register_ib_observation_enums_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_ib_observation_enums_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_lexical_meaning_step_v1_20260917 | iba/app/migration/archive/register_lexical_meaning_step_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_lexical_meaning_step_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_lexical_readiness_check_v1_20260916 | iba/app/migration/archive/register_lexical_readiness_check_v1_20260916.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_lexical_readiness_check_v1_20260916.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_needs_adjacent_verse_context_tag_v1_20260918 | iba/app/migration/archive/register_needs_adjacent_verse_context_tag_v1_20260918.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_needs_adjacent_verse_context_tag_v1_20260918.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_prose_set_status_v1_20260827 | iba/app/migration/archive/register_prose_set_status_v1_20260827.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_prose_set_status_v1_20260827.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_purge_audit_step_v1_20260919 | iba/app/migration/archive/register_purge_audit_step_v1_20260919.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_purge_audit_step_v1_20260919.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_purge_execute_step_v1_20260924 | iba/app/migration/archive/register_purge_execute_step_v1_20260924.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_purge_execute_step_v1_20260924.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_purge_retire_database_step_v1_20260924 | iba/app/migration/archive/register_purge_retire_database_step_v1_20260924.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_purge_retire_database_step_v1_20260924.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_register_session_close_step_v1_20260924 | iba/app/migration/archive/register_session_close_step_v1_20260924.py | Retired (#2200): not in a utility or module. Was iba/app/migration/register_session_close_step_v1_20260924.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rehome_multi_chapter_vigilance_rule_20260807 | iba/app/migration/archive/rehome_multi_chapter_vigilance_rule_20260807.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rehome_multi_chapter_vigilance_rule_20260807.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rename_hib_change_detail_to_debate_change_detail_20260808 | iba/app/migration/archive/rename_hib_change_detail_to_debate_change_detail_20260808.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rename_hib_change_detail_to_debate_change_detail_20260808.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_rename_span_reading_to_lexical | iba/app/migration/archive/rename_span_reading_to_lexical.py | Retired (#2200): not in a utility or module. Was iba/app/migration/rename_span_reading_to_lexical.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_repair_dan8_daniel_phenomenon_hib_id_20260808 | iba/app/migration/archive/repair_dan8_daniel_phenomenon_hib_id_20260808.py | Retired (#2200): not in a utility or module. Was iba/app/migration/repair_dan8_daniel_phenomenon_hib_id_20260808.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_repair_strong_sense_head | iba/app/migration/archive/repair_strong_sense_head.py | Retired (#2200): not in a utility or module. Was iba/app/migration/repair_strong_sense_head.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_repurpose_incurability_to_suffering_20260810 | iba/app/migration/archive/repurpose_incurability_to_suffering_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/repurpose_incurability_to_suffering_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_repurpose_passage_tracking | iba/app/migration/archive/repurpose_passage_tracking.py | Retired (#2200): not in a utility or module. Was iba/app/migration/repurpose_passage_tracking.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_reset_escalation_tables_20260820 | iba/app/migration/archive/reset_escalation_tables_20260820.py | Retired (#2200): not in a utility or module. Was iba/app/migration/reset_escalation_tables_20260820.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_reset_m67_for_progressive_reading_v1_20260917 | iba/app/migration/archive/reset_m67_for_progressive_reading_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/reset_m67_for_progressive_reading_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolve_mcode_conflicts_by_name_match_v1_20260906 | iba/app/migration/archive/resolve_mcode_conflicts_by_name_match_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolve_mcode_conflicts_by_name_match_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolve_mcode_conflicts_heuristic_wins_v1_20260906 | iba/app/migration/archive/resolve_mcode_conflicts_heuristic_wins_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolve_mcode_conflicts_heuristic_wins_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolve_mcode_conflicts_review_flag_v1_20260906 | iba/app/migration/archive/resolve_mcode_conflicts_review_flag_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolve_mcode_conflicts_review_flag_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolve_mcode_conflicts_synonym_match_v1_20260906 | iba/app/migration/archive/resolve_mcode_conflicts_synonym_match_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolve_mcode_conflicts_synonym_match_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolve_old_migration_self_duplicates_v1_20260906 | iba/app/migration/archive/resolve_old_migration_self_duplicates_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolve_old_migration_self_duplicates_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolved_sense_mcode_only_v1_20260906 | iba/app/migration/archive/resolved_sense_mcode_only_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolved_sense_mcode_only_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolved_sense_removed_v1_20260907 | iba/app/migration/archive/resolved_sense_removed_v1_20260907.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolved_sense_removed_v1_20260907.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_resolved_sense_revived_v1_20260910 | iba/app/migration/archive/resolved_sense_revived_v1_20260910.py | Retired (#2200): not in a utility or module. Was iba/app/migration/resolved_sense_revived_v1_20260910.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_restore_incurability_legacy_word_strong_20260810 | iba/app/migration/archive/restore_incurability_legacy_word_strong_20260810.py | Retired (#2200): not in a utility or module. Was iba/app/migration/restore_incurability_legacy_word_strong_20260810.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_restructure_configmaint_report_sections | iba/app/migration/archive/restructure_configmaint_report_sections.py | Retired (#2200): not in a utility or module. Was iba/app/migration/restructure_configmaint_report_sections.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retag_answered_no_flag_v1_20260917 | iba/app/migration/archive/retag_answered_no_flag_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retag_answered_no_flag_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retire_cfg_prose_chapter_v1_20260827 | iba/app/migration/archive/retire_cfg_prose_chapter_v1_20260827.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retire_cfg_prose_chapter_v1_20260827.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retire_old_layer2_lexical_enrich_v1_20260917 | iba/app/migration/archive/retire_old_layer2_lexical_enrich_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retire_old_layer2_lexical_enrich_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retire_old_migration_mcode_conflicts_v1_20260906 | iba/app/migration/archive/retire_old_migration_mcode_conflicts_v1_20260906.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retire_old_migration_mcode_conflicts_v1_20260906.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retract_candidate_system | iba/app/migration/archive/retract_candidate_system.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retract_candidate_system.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retract_passage_system | iba/app/migration/archive/retract_passage_system.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retract_passage_system.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_retrofit_debate_lexicon_tables | iba/app/migration/archive/retrofit_debate_lexicon_tables.py | Retired (#2200): not in a utility or module. Was iba/app/migration/retrofit_debate_lexicon_tables.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_run_verse_lexical_layer1_rebuild_v1_20260916 | iba/app/migration/archive/run_verse_lexical_layer1_rebuild_v1_20260916.py | Retired (#2200): not in a utility or module. Was iba/app/migration/run_verse_lexical_layer1_rebuild_v1_20260916.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_seed_method_rules | iba/app/migration/archive/seed_method_rules.py | Retired (#2200): not in a utility or module. Was iba/app/migration/seed_method_rules.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_stage_rename_and_baseline_tag_v1_20260917 | iba/app/migration/archive/stage_rename_and_baseline_tag_v1_20260917.py | Retired (#2200): not in a utility or module. Was iba/app/migration/stage_rename_and_baseline_tag_v1_20260917.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_migration_archive_strengthen_closing_set_rules_20260807 | iba/app/migration/archive/strengthen_closing_set_rules_20260807.py | Retired (#2200): not in a utility or module. Was iba/app/migration/strengthen_closing_set_rules_20260807.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_book-narrative | iba/app/ps/archive/Book-Narrative.ps1 | Retired (#2201). Was iba/app/ps/Book-Narrative.ps1. |  | ✓ | retired script (#2201): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_booknarrative_generate | iba/app/ps/archive/BookNarrative-Generate.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/BookNarrative-Generate.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_booknarrative_validate | iba/app/ps/archive/BookNarrative-Validate.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/BookNarrative-Validate.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_candidate_curate | iba/app/ps/archive/Candidate-Curate.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/Candidate-Curate.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_candidate_quality | iba/app/ps/archive/Candidate-Quality.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/Candidate-Quality.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_chapter_generate | iba/app/ps/archive/Chapter-Generate.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/Chapter-Generate.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_contentindex_rebuild | iba/app/ps/archive/ContentIndex-Rebuild.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/ContentIndex-Rebuild.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_create_iba_view_template | iba/app/ps/archive/create-iba-view-template.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/create-iba-view-template.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_create_passage_view_and_export | iba/app/ps/archive/create-passage-view-and-export.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/create-passage-view-and-export.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_create_passages_by_book_view_and_export | iba/app/ps/archive/create-passages-by-book-view-and-export.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/create-passages-by-book-view-and-export.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_export_iba_config_tables | iba/app/ps/archive/export-iba-config-tables.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/export-iba-config-tables.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_generate_iba_db_schema_report | iba/app/ps/archive/generate-iba-db-schema-report.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/generate-iba-db-schema-report.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_passagedebate_report | iba/app/ps/archive/PassageDebate-Report.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/PassageDebate-Report.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_passagedebate_sync | iba/app/ps/archive/PassageDebate-Sync.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/PassageDebate-Sync.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_seedcandidate_report | iba/app/ps/archive/SeedCandidate-Report.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/SeedCandidate-Report.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_set_candidates | iba/app/ps/archive/Set-Candidates.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/Set-Candidates.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_versespanmeaning_report | iba/app/ps/archive/VerseSpanMeaning-Report.ps1 | Retired (#2200): not in a utility or module. Was iba/app/ps/VerseSpanMeaning-Report.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_word-audit | iba/app/ps/archive/Word-Audit.ps1 | No file: the retired word-audit work package named iba/app/ps/Word-Audit.ps1 as its ps_script, but that script never existed (#2201). |  | ✓ | retired script (#2201): kept for reference only; use needs the researcher's approval |
| iba_app_ps_archive_wordregistryspan-report | iba/app/ps/archive/WordRegistrySpan-Report.ps1 | Retired (#2201). Was iba/app/ps/WordRegistrySpan-Report.ps1. |  | ✓ | retired script (#2201): kept for reference only; use needs the researcher's approval |
| iba_app_ps_behaviour | iba/app/ps/Behaviour.ps1 | PS entry point of work package behaviour: Behaviour.ps1 -Action List [-Class], dispatched through run.py (step behaviour.list, #2207). | ✓ | ✓ | PS entry point: the step's config is read by the handler |
| iba_app_ps_debate_run | iba/app/ps/Debate-Run.ps1 | Orchestrates the debate pipeline steps (operations-ingest) using lib/debaterun.py readiness checks. | ✓ | ✓ | operational script outside the dispatcher (#2200) |
| iba_app_ps_start_iba | iba/app/ps/Start-Iba.ps1 | Session bootstrap: runs iba.app.init (config check, load, tables, STEP preflight, rule delivery). | ✓ | ✓ | operational script outside the dispatcher (#2200) |
| iba_app_tools_archive_build_lexicon_combined_extract | iba/app/tools/archive/build_lexicon_combined_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_lexicon_combined_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_lexicon_lookup_extract | iba/app/tools/archive/build_lexicon_lookup_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_lexicon_lookup_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_lsj_sense_extract | iba/app/tools/archive/build_lsj_sense_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_lsj_sense_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_meaning_tree_extract | iba/app/tools/archive/build_meaning_tree_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_meaning_tree_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_mounce_lexicon_extract | iba/app/tools/archive/build_mounce_lexicon_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_mounce_lexicon_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_span_heatmap_v1 | iba/app/tools/archive/build_span_heatmap_v1.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_span_heatmap_v1.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_span_term_reconciliation | iba/app/tools/archive/build_span_term_reconciliation.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_span_term_reconciliation.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_strong_info_extract | iba/app/tools/archive/build_strong_info_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_strong_info_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_strong_related_extract | iba/app/tools/archive/build_strong_related_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_strong_related_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_verse_span_meaning_extract | iba/app/tools/archive/build_verse_span_meaning_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_verse_span_meaning_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_build_verse_span_strongtree_extract | iba/app/tools/archive/build_verse_span_strongtree_extract.py | Retired (#2200): not in a utility or module. Was iba/app/tools/build_verse_span_strongtree_extract.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_check_ib_related_span_step_coverage | iba/app/tools/archive/_check_ib_related_span_step_coverage.py | Retired (#2200): not in a utility or module. Was iba/app/tools/_check_ib_related_span_step_coverage.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_check_missing_strongs_in_step | iba/app/tools/archive/_check_missing_strongs_in_step.py | Retired (#2200): not in a utility or module. Was iba/app/tools/_check_missing_strongs_in_step.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_check_span_unmatched_lexicon_json | iba/app/tools/archive/_check_span_unmatched_lexicon_json.py | Retired (#2200): not in a utility or module. Was iba/app/tools/_check_span_unmatched_lexicon_json.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_ib_relevance_classifier | iba/app/tools/archive/ib_relevance_classifier.py | Retired (#2200): not in a utility or module. Was iba/app/tools/ib_relevance_classifier.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_lexicon_split_common | iba/app/tools/archive/lexicon_split_common.py | Retired (#2200): not in a utility or module. Was iba/app/tools/lexicon_split_common.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_log_retention | iba/app/tools/archive/log_retention.py | Retired (#2200): not in a utility or module. Was iba/app/tools/log_retention.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_purge_word | iba/app/tools/archive/purge_word.py | Retired (#2200): not in a utility or module. Was iba/app/tools/purge_word.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_app_tools_archive_temp_2200_gate_test | iba/app/tools/archive/temp_2200_gate_test.py | Retired (#2200): not in a utility or module. Was iba/app/tools/temp_2200_gate_test.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| iba_prototype_build_layers | iba/prototype/archive/build_layers.py | build_layers.py — the STEP pull as SEARCH LAYERS, one table per layer. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| iba_prototype_build_prototype | iba/prototype/archive/build_prototype.py | build_prototype.py — test the term -> sense -> span model against real STEP data. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| iba_prototype_export_md | iba/prototype/archive/export_md.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). export_md.py — render the prototype's JSON "tables" as markdown for review. |  |  |  |
| iba_prototype_inspect_verse | iba/prototype/archive/inspect_verse.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). inspect_verse.py — select a verse; watch the backtrack; see what emerges. |  |  |  |
| iba_scripts_build_dbschema | iba/scripts/archive/build_dbschema.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_dbschema.py -- capture a database's schema into its DBSchema register. |  |  |  |
| iba_scripts_cfg_apply | iba/scripts/archive/cfg_apply.py | cfg_apply.py — the configurator-maintenance utility's WRITE PATH. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| iba_scripts_cfg_helper | iba/scripts/archive/cfg_helper.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). cfg_helper.py -- export each config json to a configuration component helper (.md). |  |  |  |
| iba_scripts_cfg_kernel | iba/scripts/archive/cfg_kernel.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). cfg_kernel.py — the envelope-validator KERNEL for the IBA configurator. |  |  |  |
| iba_scripts_probe_step_api | iba/scripts/archive/probe_step_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). probe_step_api.py — dump the FULL raw response of each STEP API, unmodified. |  |  |  |
| init | iba/app/init.py | The app bootstrap: config check and load, data tables, STEP preflight, rule delivery. | ✓ | ✓ | app core, outside the utility config-density check |
| lexical | iba/app/lib/lexical.py | lexical.py — the the lexical (`verse_lexical`) engine: T1-T3 of the verse-lexical technique Extended 2026-09-04 (escalation #1383): also computes position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/party_kind and applies the H0853 role exception. | ✓ |  |  |
| lexicalenrich | iba/app/lib/archive/lexicalenrich.py | Stage 1 Layer 2 engine: verse_lexical_note capture + passage.genre/lexical_complete_at, JSON-payload-driven. Escalation #1383. |  |  |  |
| lexicalenrichgenerate | iba/app/lib/lexicalenrichgenerate.py | The LLM-calling half of lexical.run Layer 2 (escalation #1549 continued) -- batches the verse-list, assembles a lean cost-estimated package per batch, calls the Anthropic Messages API, parses the response, writes via lexicalenrich.enrich_passage, logs real usage. Config-driven from the start (module lexical), unlike its own template narrativegenerate.py which is flagged non-compliant. | ✓ |  |  |
| lexicalscope | iba/app/lib/lexicalscope.py | Selector-to-verse-id resolution: a cluster, word, Strong's list or verse list resolves to verse ids via span.strong_variant (exact-token match), never strong_verse. Used by steps lexical.meaning, lexical.relational, cluster.subgroup and by lib/clusterstatus.py. | ✓ | ✓ | pure SQL resolver over span, cluster_strong and word_strong: no value in it is a setting (#2207 decision 1a) |
| lexicon | iba/app/handlers/lexicon.py | handlers/lexicon.py -- Lexicon-parsed-layer handlers (L2b): parse/related/validate steps for the lexicon-parse work package. rebuild_parsed_tables() is the full parse rebuild (also called directly by raw.backfill_meaning); as of escalation #1655 (2026-09-10) it also adds a standing lemma-derived-with-note fallback for any strong code STEP returns no exact-variant result for, so every live strong code has parse coverage matching strong's own grain. | ✓ |  |  |
| lexiconparse | iba/app/lib/lexiconparse.py | lexiconparse.py — the governed parse of the raw lexicon layer (strong_meaning_tree.sense_text, | ✓ |  |  |
| m0_5_11_surface_cue_v1_20260923 | iba/app/migration/archive/m0_5_11_surface_cue_v1_20260923.py | ONE-OFF migration -- researcher instruction 2026-09-23: names surface-form variation as the explicit diagnostic cue for M0.5.11's divergence check. Run once, then set inactive=1. |  |  |  |
| manifest | iba/app/lib/manifest.py | manifest.py — the project-wide file manifest (rebuild + search). Filename/path metadata only; the baseline lib/contentindex.py (round 2) cross-checks file-content search coverage against. | ✓ |  |  |
| meaning_source_2207_v1_20261022 | iba/app/migration/archive/meaning_source_2207_v1_20261022.py | ONE-OFF migration -- escalation #2207: meaning_source sources and aliases, through configmaint.apply_logged under run_id DEVMODE-2207-MEANING-SOURCE-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| memory_rules_to_config_v1_20261021 | iba/app/migration/archive/memory_rules_to_config_v1_20261021.py | ONE-OFF migration -- escalation #2184: moves the live rules held only in Claude memory into config, every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2184-MEMORY-RULES-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| migration | iba/app/migration/archive/add_escalation_needs_followup_column_20260830.py | ONE-OFF: adds escalation.needs_claude_followup / escalation_history.needs_claude_followup (INTEGER, default 0). Idempotent. escalation #1075. |  |  |  |
| narrative_blocks_2172_v1_20261022 | iba/app/migration/archive/narrative_blocks_2172_v1_20261022.py | ONE-OFF migration -- escalation #2172 step A: narrative_section.block_text, each chapter's blocks from its current file, run_id DEVMODE-2172-NARRATIVE-BLOCKS-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| narrative_chapter_table_config_v1_20261018 | iba/app/migration/archive/narrative_chapter_table_config_v1_20261018.py | ONE-OFF migration -- escalation #2155: the chapter table as the authority for the chapters (kind/purpose/purpose_ref columns, enum, setting, add_chapter step, grants, behaviour rule, the approved purposes, Structure log entries), every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2155-CHAPTER-20261018. inactive=1 once applied. |  |  |  |
| narrative_claim_register_config_v1_20261013 | iba/app/migration/archive/narrative_claim_register_config_v1_20261013.py | ONE-OFF migration -- escalation #2110, build steps 1 and 2: config (cfg_trigger new; enums, settings, behaviour rule, work package narrative-register, steps, grants, on_fail, reports, utilities) and schema (11 narrative_* tables, indexes, 19 history triggers, all from config through lib/db.py), every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2110-CONFIG-20261013. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| narrative_claim_register_import_v1_20261013 | iba/app/migration/archive/narrative_claim_register_import_v1_20261013.py | ONE-OFF import -- escalation #2110, build steps 6 and 7 (spec sec6): --preview reads the claim register v1-v51 (R1), its 53 dated sections (R2), the narrative index (R3), the imputed-readings audit (R5) and digest sec4 (R6), plus the current chapter headings and citations, and writes the preview JSON/md and the review list beside the specification -- no DB write. --apply --preview-file imports the APPROVED preview as it stands (writer migration), once; it refuses a second run. Applied 2026-10-13 (researcher: "process the import"): 81 claims, 129 updates, 35 chapters, 347 sections, 6,267 citations. inactive=1 once applied. |  |  |  |
| narrative_home_2172_v1_20261022 | iba/app/migration/archive/narrative_home_2172_v1_20261022.py | ONE-OFF migration -- escalation #2172: governance.narrative_home, its rule links, the control map's study rows; run_id DEVMODE-2172-NARRATIVE-HOME-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| narrativecopy | iba/app/lib/narrativecopy.py | narrativecopy.py -- copies the active chapters' current files (narrative_chapter, in reading order) from the narrative folder to the learning4comfort inbox; a .md file in the folder that is no chapter's current file is reported and not copied (#2155 D3). Earlier versions in the inbox are replaced; nothing else there is touched; never runs git (#1941). | ✓ |  |  |
| narrativegenerate | iba/app/lib/archive/narrativegenerate.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). report.book_narrative_generate's assembly (debates + governing docs), cost estimate/cap, Anthropic Messages API call, and narrative filing |  |  |  |
| narrativeregister | iba/app/lib/narrativeregister.py | narrativeregister.py -- the narrative claim register in iba.db (escalation #2110): the reference parser and book-alias map, the register actions (AddClaim, Edit, Tell, Untell, Withdraw, EditNote, AddChapter, EditChapter, EditSection, Find, History, Check), Export of the three published files, and the narrative held as blocks: rewrite() and publish_chapter() (#2172). See USER-GUIDE.md and GOVERNANCE.md. | ✓ |  |  |
| observationenhancer | iba/app/handlers/observationenhancer.py | observationenhancer.py -- the observation_enhancer utility (escalation #1778). preview(ctx)/apply(ctx): applies a researcher-confirmed cfg_observation_enhancer_rule (selector_sql + update_json) to ib_observation, logging every change to ib_observation_enhancer_log. | ✓ |  |  |
| passagedebatereport | iba/app/lib/passagedebatereport.py | passagedebatereport.py — registers the passage-debate method (`WA-passage-read-guidance` + | ✓ |  |  |
| passagetrack | iba/app/lib/passagetrack.py | passagetrack.py — the completion-tracking record for the verse-fanout method (`report. | ✓ | ✓ | receives an already-open cfg/connection from its caller; only checks cfg.may_write(), no settings/enums of its own. |
| pathaudit | iba/app/lib/pathaudit.py | pathaudit.py -- project-wide scan for hardcoded folder/file-path string literals not backed by a live cfg accessor. Escalation #971/#976, the automated successor to the one-off #648 sweep for the location subset specifically. | ✓ | ✓ | legitimate zero, same shape as retention.py/seedreport.py: lib/pathaudit.py takes a pre-opened Cfg object and calls .conn.execute()/normalize_setting_value() directly -- its caller (handlers/pathaudit.py) is the one that calls cfg.setting("pathaudit.report_path", ...); the lib module itself resolves no config of its own. |
| prose_add_edit_rules_build_v1_20260826 | iba/app/migration/archive/prose_add_edit_rules_build_v1_20260826.py | ONE-OFF migration, escalation #890 (Prose add/edit operational rules layer) -- cfg_behaviour_rule (D2, prose_section_type creation gate), prose_section_verse_link table + cfg_table/cfg_column/cfg_write_grant (D4), cfg_step for prose.flag_fix_propose/.flag_fix_apply (D5), cfg_prose.book_stage_map use-text correction (D6, no filtering bug found). D1 (leave prose_section_finding_link's FK as-is), D3 (edit-file delete refusal) are code-only, not this migration. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prose_change_log_build_v1_20260824 | iba/app/migration/archive/prose_change_log_build_v1_20260824.py | ONE-OFF migration, escalation #836 (Prose change log design) -- creates record_change_log, moves prose_section/prose_section_type to Model A (mutate-in-place) versioning, migrates the 91 existing superseded prose_section rows into the log then hard-deletes them, baseline-backfills version pointers for every surviving row, and registers the full cfg_table/cfg_column/cfg_enum/cfg_write_grant/cfg_behaviour_rule content. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prose_first_layer_build_v1_20260824 | iba/app/migration/archive/prose_first_layer_build_v1_20260824.py | ONE-OFF migration, escalation #829 (Prose management IBA first-layer) -- builds cfg_prose, fills/corrects cfg_column use text, cfg_enum (5 groups), cfg_status_flow, cfg_behaviour_rule (3 rows), cfg_write_grant (3 rows), the prose work package + 5 cfg_step rows, reactivates the 4 original scripts. D10 (book_stage_map vs. book_label) deliberately deferred, not built here. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prose_orphan_enum_fix_v1_20260826 | iba/app/migration/archive/prose_orphan_enum_fix_v1_20260826.py | ONE-OFF migration, escalations #896/#900/#901/#902 -- closes the 7 orphan cfg_enum findings per the researcher's own rule: fix the validator for the 4 already-CHECK-enforced groups (cfg_column.expectation wired); fix the code for the 3 genuinely unenforced prose_section_type groups (real CHECK constraints added, then the same expectation wiring). inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prosestore | iba/app/lib/prosestore.py | The DB-canonical prose store: extract, search, chapter export/import. Escalation #784, 2026-08-21 -- incorporates operations previously standalone in scripts/build_programme_prose_extract.py, scripts/search_prose.py, scripts/export_prose_chapter_edit.py, scripts/import_prose_chapter_edit.py into the app. | ✓ |  |  |
| ps_charanswer | iba/app/ps/CharAnswer.ps1 | Front door for the char-answers stage (cluster-reading work package). | ✓ | ✓ | app core, outside the utility config-density check |
| ps_charreading | iba/app/ps/CharReading.ps1 | Front door for the char-reading stage (cluster-reading work package). | ✓ | ✓ | app core, outside the utility config-density check |
| ps_dir_setting_2208_v1_20261021 | iba/app/migration/archive/ps_dir_setting_2208_v1_20261021.py | ONE-OFF migration -- escalation #2208: adds governance.scripts_ps_dir to compliance.value_settings, through configmaint.apply_logged under run_id DEVMODE-2208-PS-DIR-SETTING-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| ps_lexical_readiness | iba/app/ps/Lexical-Readiness.ps1 | Front door for lexical.readiness (verse-lexical work package). | ✓ | ✓ | app core, outside the utility config-density check |
| ps_lib_notify | iba/app/ps/_lib/Notify.ps1 | PS helper library: completion notifications for the PS front doors. | ✓ | ✓ | app core, outside the utility config-density check |
| ps_relationalreading | iba/app/ps/RelationalReading.ps1 | Front door for lexical.relational (verse-lexical work package). | ✓ | ✓ | app core, outside the utility config-density check |
| ps_run_stage1batch | iba/app/ps/Run-Stage1Batch.ps1 | Runs the Stage 1 verse-reading steps over a cluster (verse-lexical work package). | ✓ | ✓ | app core, outside the utility config-density check |
| ps_through_runpy_2207_v1_20261022 | iba/app/migration/archive/ps_through_runpy_2207_v1_20261022.py | ONE-OFF migration -- escalation #2207 item 1: Behaviour.ps1 and VerseMeta.ps1 through run.py (work packages, steps, write grant, on_fail rules), through configmaint.apply_logged under run_id DEVMODE-2207-PS-THROUGH-RUNPY-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| ps_versereading | iba/app/ps/VerseReading.ps1 | Front door for lexical.meaning (verse-lexical work package). | ✓ | ✓ | app core, outside the utility config-density check |
| purge | iba/app/handlers/purge.py | purge.py -- app-wide soft-delete purge audit + execute + database retirement (escalation #1766/#1868/#1872/#1873): per-table soft-deleted counts + live-dependency safety check (audit, read-only); allow-listed soft-deleted-row removal (execute, preview-then-live); and full-table clearing of every cfg_table.inactive=1 table for a database, with dangling-FK cleanup on retained tables (retire_database, preview-then-live). All three always persist a report. | ✓ |  |  |
| query_db | archive/query_db.py | prose_section_type joined to active current prose_section rows -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| quotecheck | iba/app/lib/quotecheck.py | quotecheck.py -- the narrative quote check moved into the app (#2173 G14). | ✓ | ✓ | pure functions over a connection: the callers read narrative.quote_min_words and pass it |
| reading_waste_2206_v1_20261021 | iba/app/migration/archive/reading_waste_2206_v1_20261021.py | ONE-OFF migration -- escalation #2206: inserts compliance.value_settings, through configmaint.apply_logged under run_id DEVMODE-2206-READING-WASTE-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rebuild_prose_section_fk_v1_20260905 | iba/app/migration/archive/rebuild_prose_section_fk_v1_20260905.py | ONE-OFF migration, escalation #1452 (approved 2026-09-05) -- rebuilds bible_research.db's prose_section table, correcting its stale FK (was REFERENCES prose_section_type_old, a nonexistent leftover-rename table; now correctly REFERENCES prose_section_type). Rename/recreate/copy/drop pattern matching retire_cfg_prose_chapter_v1_20260827.py; all 1035 rows preserved with ids intact, 5 indexes + 3 FTS-sync triggers recreated, FTS rowid linkage verified 0 mismatches, PRAGMA foreign_key_check clean post-rebuild. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| record_retire_onfail_2172_v1_20261022 | iba/app/migration/archive/record_retire_onfail_2172_v1_20261022.py | ONE-OFF migration -- escalation #2172/#2214: the retired narrative_register.record's cfg_on_fail row set inactive, run_id DEVMODE-2172-RECORD-ONFAIL-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| recordingpass | iba/app/lib/recordingpass.py | recordingpass.py — the single writer for `ib_observation`/`ib_node` (escalation #1693's design, | ✓ |  |  |
| reframe_what_is_to_what_does_show_v1_20260923 | iba/app/migration/archive/reframe_what_is_to_what_does_show_v1_20260923.py | ONE-OFF migration -- researcher instruction 2026-09-23: reframe bare 'what is <stored field>' questions to 'what does it show' (morph example). Fixed M0.5.2 (had the literal morph antipattern) and M0.5.3 (missed in earlier reworks, also lacked span-grounding entirely). Run once, then set inactive=1. |  |  |  |
| register_20261021_migrations_v1_20261021 | iba/app/migration/archive/register_20261021_migrations_v1_20261021.py | ONE-OFF migration -- escalation #2196: registers the 2026-10-21 Developer Mode migrations in cfg_utility (this file), every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2196-REGISTER-MIGRATIONS-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| register_active_app_files_v1_20261021 | iba/app/migration/archive/register_active_app_files_v1_20261021.py | ONE-OFF migration -- escalation #2198/#2200: registers the active app files with no cfg_utility row, through configmaint.apply_logged under run_id DEVMODE-2198-REGISTER-ACTIVE-FILES-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| registryreport | iba/app/lib/registryreport.py | registryreport.py — evaluate/review the `word_registry`: a summary, its join to `strong` (via | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| renamed_paths_2207_v1_20261022 | iba/app/migration/archive/renamed_paths_2207_v1_20261022.py | ONE-OFF migration -- escalation #2207: 7 live cfg rows point at the renamed iba/docs plans and the archived file-organisation rules, through configmaint.apply_logged under run_id DEVMODE-2207-RENAMED-PATHS-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| report_word_raw | iba/app/report.py | The word-raw report, called by handlers/reports.py and its CLI. | ✓ | ✓ | app core, outside the utility config-density check |
| reportkit | iba/app/lib/reportkit.py | reportkit.py — shared report scaffold (title/ToC/sections/footer) + archive-on-write, reading | ✓ | ✓ | Its one cfg.setting() call site (inside oneoff_path()) moved to lib/filingkit.py 2026-08-28 (escalation #971/#992) when oneoff_path() became a thin delegating wrapper -- reportkit.py itself now only reads cfg_report/cfg_report_section via raw conn.execute() (render_scaffold/write_report), never through a Cfg wrapper method. Legitimate zero, same shape as retention.py/seedreport.py. |
| research_VE_lexical_faculty_map_build_build_batch4 | research/VE-lexical/faculty-map-build/_build_batch4.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). -*- coding: utf-8 -*- |  |  |  |
| research_VE_lexical_faculty_map_build_classify_batch1 | research/VE-lexical/faculty-map-build/_classify_batch1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Faculty classification for inventory slice 0..343. Decisions grounded in gloss+senses, original-language aware. |  |  |  |
| retention | iba/app/lib/retention.py | retention.py — log growth / run-health visibility for the append-only audit tables | ✓ | ✓ | receives cfg.conn from its caller; its own setting (retention.snapshot_keep_count) is read by dbsnapshot.py, not here. |
| retire_from_id_related_activity_v1_20260827 | iba/app/migration/archive/retire_from_id_related_activity_v1_20260827.py | ONE-OFF migration, escalation #909 -- full removal of D14 (from_id) and D15 (related_activity's pairing/graph role): 6 cfg_escalation_requirement rows, 6 cfg_report_section rows, 4 cfg_column rows deleted; from_id/related_activity columns physically dropped from escalation/escalation_history. Researcher decision after two live audits found the mechanism unreliable and unused. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| retire_m10b_into_m58_v1_20260906 | iba/app/migration/archive/retire_m10b_into_m58_v1_20260906.py | ONE-OFF migration -- escalation #1525: M58/M10b were the only duplicate short_name ('Wickedness') among live M-clusters, zero member overlap. Researcher verdict verbatim: retire M10b, keep M58. Relocates M10b's 43 live cluster_strong members to M58 (rationale appended), merges M10b's gloss/description onto the surviving M58 row, sets M10b cluster.deleted=1. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| retire_uncontrolled_scripts_v1_20261021 | iba/app/migration/archive/retire_uncontrolled_scripts_v1_20261021.py | ONE-OFF migration -- escalation #2200: retires every script not in a utility or module, through configmaint.apply_logged under run_id DEVMODE-2200-RETIRE-SCRIPTS-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| reword_word_level_questions_strong_keyed_v1_20260923 | iba/app/migration/archive/reword_word_level_questions_strong_keyed_v1_20260923.py | ONE-OFF migration -- researcher ruling 2026-09-23: cluster dropped from M0.1.x/M0.5.x, reworded to single-term facts via strong_related for the relational ones; M0.5.10 retired. Run once, then set inactive=1. |  |  |  |
| rule59_drop_dead_pointer_v1_20261021 | iba/app/migration/archive/rule59_drop_dead_pointer_v1_20261021.py | ONE-OFF migration -- escalation #2195: drops the dead pointer to the archived docs/interaction-preferences.md from cfg_behaviour_rule 59, through configmaint.apply_logged under run_id DEVMODE-2195-RULE59-POINTER-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rule63_approval_handover_checks_v1_20261021 | iba/app/migration/archive/rule63_approval_handover_checks_v1_20261021.py | ONE-OFF migration -- escalation #2178: adds the approval hand-over checks to cfg_behaviour_rule 63, every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2178-RULE63-HANDOVER-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rule81_general_2209_v1_20261022 | iba/app/migration/archive/rule81_general_2209_v1_20261022.py | ONE-OFF migration -- escalation #2209: rule 81 text to general-rule delivery, through configmaint.apply_logged under run_id DEVMODE-2209-RULE81-GENERAL-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rule97_copy_with_backup_api_v1_20261021 | iba/app/migration/archive/rule97_copy_with_backup_api_v1_20261021.py | ONE-OFF migration -- escalation #2193: rule 97 names dbsnapshot.copy_db as how a database test copy is made, through configmaint.apply_logged under run_id DEVMODE-2193-RULE97-BACKUP-COPY-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rule_delivery_scope_v1_20261021 | iba/app/migration/archive/rule_delivery_scope_v1_20261021.py | ONE-OFF migration -- escalation #2185: scopes the start-up rule print and the compliance restatement to the session (deliver_when), every cfg_* write through configmaint.apply_logged under run_id DEVMODE-2185-RULE-DELIVERY-SCOPE-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rule_scope_2209_v1_20261021 | iba/app/migration/archive/rule_scope_2209_v1_20261021.py | ONE-OFF migration -- escalation #2209: creates cfg_rule_scope and links every rule to its operations, through configmaint.apply_logged under run_id DEVMODE-2209-RULE-SCOPE-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| rule_scope_grant_2209_v1_20261021 | iba/app/migration/archive/rule_scope_grant_2209_v1_20261021.py | ONE-OFF migration -- escalation #2209: write grant for cfg_rule_scope, through configmaint.apply_logged under run_id DEVMODE-2209-RULE-SCOPE-GRANT-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| run | iba/app/run.py | The dispatcher and run-state machine: cfg_step handler, cfg_on_fail path, run rows. | ✓ | ✓ | app core, outside the utility config-density check |
| schema_overview | iba/app/tools/build_schema_overview_report.py | Renders the DBSchema register (iba/config/DBSchema/DBSchema.json, built by iba/scripts/build_dbschema.py) into a human-readable markdown overview report -- one row per table with description/rows/cols/PK/FKs/indexes, plus an undescribed-items flag section. Escalation #1306. |  |  |  |
| schemareport | iba/app/lib/schemareport.py | schemareport.py — the IBA app's own DATA-schema snapshot, one of the four "missing reports" | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| scripts_analytics_bible_analytics | scripts/analytics/archive/bible_analytics.py | bible_analytics.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_db_client | scripts/analytics/archive/db_client.py | db_client.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_morph_util | scripts/analytics/archive/morph_util.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). morph_util.py — canonical morphology-code helpers (STEP / OSHB + Robinson Greek). |  |  |  |
| scripts_analytics_step_client | scripts/analytics/archive/step_client.py | step_client.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_word_export | scripts/analytics/archive/word_export.py | word_export.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_zotero_client | scripts/analytics/archive/zotero_client.py | zotero_client.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_add_role_to_master_index_v1_20260707 | scripts/archive/_apply_add_role_to_master_index_v1_20260707.py | _apply_add_role_to_master_index_v1_20260707.py — M64: add per-span `role` to the master index |  |  |  |
| scripts_apply_backfill_chapter_verses_v1_20260702 | scripts/archive/_apply_backfill_chapter_verses_v1_20260702.py | _apply_backfill_chapter_verses_v1_20260702.py |  |  |  |
| scripts_apply_backfill_verse_id_active_20260701 | scripts/archive/_apply_backfill_verse_id_active_20260701.py | _apply_backfill_verse_id_active_20260701.py |  |  |  |
| scripts_apply_build_ib_char_index_v1_20260711 | scripts/archive/_apply_build_ib_char_index_v1_20260711.py | (c) Build ib_characteristic into the normalised characteristic index, from the sources |  |  |  |
| scripts_apply_cause_from_api | scripts/archive/_apply_cause_from_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_cause_from_api.py (2026-06-16) — apply the cause-resolution API output back into ve_lexical. |  |  |  |
| scripts_apply_charfix_master_v1_20260711 | scripts/archive/_apply_charfix_master_v1_20260711.py | Fix (a) the emergent-characteristic seed failure + (b) populate the char on the master. |  |  |  |
| scripts_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701 | scripts/archive/_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py | _apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py |  |  |  |
| scripts_apply_cluster_schema_v1_20260505 | scripts/archive/_apply_cluster_schema_v1_20260505.py | _apply_cluster_schema_v1_20260505.py — DB-modifying. |  |  |  |
| scripts_apply_comment_findings_v1_20260602 | scripts/archive/_apply_comment_findings_v1_20260602.py | Applier for COMMENT_EVALUATION outcomes (per cluster). |  |  |  |
| scripts_apply_create_and_populate_passages_20260701 | scripts/archive/_apply_create_and_populate_passages_20260701.py | _apply_create_and_populate_passages_20260701.py |  |  |  |
| scripts_apply_create_constitution_cluster | scripts/archive/_apply_create_constitution_cluster.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_create_constitution_cluster.py — WRITES. Creates the new M47 'Constitution' cluster (the inner-being |  |  |  |
| scripts_apply_create_vc_for_onboarded | scripts/archive/_apply_create_vc_for_onboarded.py | Create verse_context units for engine-onboarded terms (post-onboard catch-up step). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_d6_capture_contributor_source | scripts/archive/_apply_d6_capture_contributor_source.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). D6 — capture a contributor source (Logos / AI-Chat) into prose_section, strip it |  |  |  |
| scripts_apply_descriptions_patch | scripts/archive/_apply_descriptions_patch.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_dq01_locus_coupling_swap_v1_20260714 | scripts/archive/_apply_dq01_locus_coupling_swap_v1_20260714.py | DQ-01 source fix: un-transpose coupling(112) <-> locus(116) for Psalms read-2026 (v1, 2026-07-14). |  |  |  |
| scripts_apply_drop_code_softdelete | scripts/archive/_apply_drop_code_softdelete.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_drop_code_softdelete.py — MODIFIES DB. Soft-delete every finding referencing the §3 DROP tier codes |  |  |  |
| scripts_apply_excluded_registry_cascade | scripts/archive/_apply_excluded_registry_cascade.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_excluded_registry_cascade.py — D1 rule (2026-06-15): when a registry is phase1_status='Excluded', |  |  |  |
| scripts_apply_extend_characteristic_baseline_v1_20260703 | scripts/archive/_apply_extend_characteristic_baseline_v1_20260703.py | Extend the `characteristic` baseline (199 rows, 17 clusters) to the Ps/Pro-raised |  |  |  |
| scripts_apply_faculty_map_rederive_20260624 | scripts/archive/_apply_faculty_map_rederive_20260624.py | Re-found FACULTY on a curated Strong's-lemma->faculty MAP (P2-compliant, replacing |  |  |  |
| scripts_apply_faculty_rederive_v1 | scripts/archive/_apply_faculty_rederive_v1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_faculty_rederive_v1.py (2026-06-15) — re-derive VE7 (faculty) against the actual faculty |  |  |  |
| scripts_apply_field_from_api | scripts/archive/_apply_field_from_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_field_from_api.py (2026-06-16) — apply a field read API output back into ve_lexical. |  |  |  |
| scripts_apply_file_chapter_lexical_prose_v1_20260702 | scripts/archive/_apply_file_chapter_lexical_prose_v1_20260702.py | _apply_file_chapter_lexical_prose_v1_20260702.py |  |  |  |
| scripts_apply_file_passage_lexical_prose_v1_20260704 | scripts/archive/_apply_file_passage_lexical_prose_v1_20260704.py | _apply_file_passage_lexical_prose_v1_20260704.py |  |  |  |
| scripts_apply_file_ruthlessness_lexical_prose_20260702 | scripts/archive/_apply_file_ruthlessness_lexical_prose_20260702.py | _apply_file_ruthlessness_lexical_prose_20260702.py |  |  |  |
| scripts_apply_file_synthesis_prose_v1_20260703 | scripts/archive/_apply_file_synthesis_prose_v1_20260703.py | File a cross-chapter SYNTHESIS document as a DB-canonical prose_section |  |  |  |
| scripts_apply_finding_catalogue_consolidation_v1_20260829 | scripts/archive/_apply_finding_catalogue_consolidation_v1_20260829.py | ONE-OFF migration, researcher-directed 2026-08-29 (finding-tables landscape review) -- folds cluster_finding into finding (structural links retained as new columns) and wa_finding_catalogue_links into finding_question_link (finding_id remapped via the session_b SB: tag; 743 rows with no source finding_id left unmigrated in the retained source table). Run and verified live 2026-08-29 -- one-off, not a reusable routine. |  |  |  |
| scripts_apply_finding_verse_term_index_v1_20260829 | scripts/archive/_apply_finding_verse_term_index_v1_20260829.py | ONE-OFF migration, researcher-directed 2026-08-29 (finding verse/term index plan) -- creates finding_verse_index (M:N, direct to iba.verse.id) via 3 passes (structural, finding_verse_link migration, text-mined), backfills finding.strong_number via mti_terms.strongs_number -> iba.strong.strongNumber. Run and verified live 2026-08-29 -- one-off, not a reusable routine. |  |  |  |
| scripts_apply_fix_8_mti_mismatches_percase_20260701 | scripts/archive/_apply_fix_8_mti_mismatches_percase_20260701.py | _apply_fix_8_mti_mismatches_percase_20260701.py |  |  |  |
| scripts_apply_fix_verse_context_mti_mismatch_20260701 | scripts/archive/_apply_fix_verse_context_mti_mismatch_20260701.py | _apply_fix_verse_context_mti_mismatch_20260701.py |  |  |  |
| scripts_apply_flag_empty_to_t2 | scripts/archive/_apply_flag_empty_to_t2.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_flag_empty_to_t2.py — empties FLAG: every remaining FLAG term -> T2 (the catch-all reference bucket; |  |  |  |
| scripts_apply_flag_triage_moves | scripts/archive/_apply_flag_triage_moves.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_flag_triage_moves.py — classify FLAG terms by gloss and move the confident ones: clear characteristic |  |  |  |
| scripts_apply_gate1_term_onboard_v1_20260705 | scripts/archive/_apply_gate1_term_onboard_v1_20260705.py | *** RETIRED 2026-07-12 (researcher direction). DO NOT USE. *** |  |  |  |
| scripts_apply_generate_collection_lexical_20260624 | scripts/archive/_apply_generate_collection_lexical_20260624.py | Collection-lexical GENERATOR (01b Part C, the term-scope layer). |  |  |  |
| scripts_apply_generate_ve_lexical_v2 | scripts/archive/_apply_generate_ve_lexical_v2.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_generate_ve_lexical_v2.py (2026-06-16) — generate the v2 verse-lexical for ALL analysed |  |  |  |
| scripts_apply_generic_characteristic_backfill_20260527 | scripts/archive/_apply_generic_characteristic_backfill_20260527.py | Generic 1:1 characteristic backfill for pre-v2_6 closed clusters. |  |  |  |
| scripts_apply_ib_char_cluster_assign_v1_20260711 | scripts/archive/_apply_ib_char_cluster_assign_v1_20260711.py | Assign each ib_characteristic record (Psalms) to a CLUSTER based on its term. |  |  |  |
| scripts_apply_ib_char_cluster_assign_v2_20260711 | scripts/archive/_apply_ib_char_cluster_assign_v2_20260711.py | Assign CLUSTER via the deterministic chain: master -> its 1 mti_term -> its 1 |  |  |  |
| scripts_apply_ib_char_family_grouping_v1_20260711 | scripts/archive/_apply_ib_char_family_grouping_v1_20260711.py | Group meaning-records (ib_characteristic, a given book_scope) into <=50 semantic |  |  |  |
| scripts_apply_ingest_verse_morphology | scripts/archive/_apply_ingest_verse_morphology.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_ingest_verse_morphology.py (2026-06-16) — populate the persisted MEASURE LAYER (M60). |  |  |  |
| scripts_apply_l2_rollup | scripts/archive/_apply_l2_rollup.py | _apply_l2_rollup.py — roll the VERSE-level L2 findings up to CLUSTER-level findings (the "characteristic = -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_l2_write | scripts/archive/_apply_l2_write.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_l2_write.py — the L2 WRITER (verse-complete). Enters by --cluster (the verses that contain a |  |  |  |
| scripts_apply_l2_write_refit | scripts/archive/_apply_l2_write_refit.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_l2_write_refit.py — L2 writer on the REFIT basis (wa-catalogue-refit-two-layer / verse-extraction |  |  |  |
| scripts_apply_language_reconcile | scripts/archive/_apply_language_reconcile.py | _apply_language_reconcile.py — make mti_terms.language / wa_term_inventory.language -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_lev_study_v1_20260705 | scripts/archive/_apply_lev_study_v1_20260705.py | _apply_lev_study_v1_20260705.py  — Leviticus terminology study loader (corpus-native). |  |  |  |
| scripts_apply_link_mti_term_id | scripts/archive/_apply_link_mti_term_id.py | _apply_link_mti_term_id.py — D2a (2026-06-15): populate the missing wa_verse_records.mti_term_id link -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_load_segmentation_v1_20260703 | scripts/archive/_apply_load_segmentation_v1_20260703.py | Load an inner-being SEGMENTATION (units) into the generic segment store. |  |  |  |
| scripts_apply_locus_dimension_v1_20260704 | scripts/archive/_apply_locus_dimension_v1_20260704.py | Derive a LOCUS dimension (ve_nr 116) on target/bearer spans: IB-internal vs external. |  |  |  |
| scripts_apply_m03_characteristic_backfill_20260527 | scripts/archive/_apply_m03_characteristic_backfill_20260527.py | M03 characteristic backfill (test cluster for pre-v2_6 characteristic retrofit). |  |  |  |
| scripts_apply_m03_findings_capture_20260620 | scripts/archive/_apply_m03_findings_capture_20260620.py | _apply_m03_findings_capture_20260620.py — capture M03 (Grief) findings, in line with M02. |  |  |  |
| scripts_apply_master_index_backfill_v1_20260706 | scripts/archive/_apply_master_index_backfill_v1_20260706.py | Master-index -> wa_verse_records backfill (per book). |  |  |  |
| scripts_apply_merge_m10bc_into_m10_20260623 | scripts/archive/_apply_merge_m10bc_into_m10_20260623.py | Merge M10b + M10c into M10 (researcher decision 2026-06-23): the three-way split |  |  |  |
| scripts_apply_migrate_sb_findings | scripts/archive/_apply_migrate_sb_findings.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_migrate_sb_findings.py — migrate Session B findings (wa_session_b_findings) into the universal |  |  |  |
| scripts_apply_migrate_ve_findings_to_lexical | scripts/archive/_apply_migrate_ve_findings_to_lexical.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_migrate_ve_findings_to_lexical.py (2026-06-15) — retrofit the VE field-value findings OUT of |  |  |  |
| scripts_apply_morph_backfill | scripts/archive/_apply_morph_backfill.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_morph_backfill.py — L0 of the L1 sweep. Populates wa_verse_records.morph_code / stem from STEP |  |  |  |
| scripts_apply_mti_dedup_active_duplicates_v1_20260713 | scripts/archive/_apply_mti_dedup_active_duplicates_v1_20260713.py | Isolate duplicate ACTIVE mti_terms rows — one active row per Strong's (OT-DBR-009). |  |  |  |
| scripts_apply_passage_build_v2_20260713 | scripts/archive/_apply_passage_build_v2_20260713.py | Passage build v2 — candidate-driven, per book (Stage 0 of the cycle). |  |  |  |
| scripts_apply_passage_completeness_v1_20260707 | scripts/archive/_apply_passage_completeness_v1_20260707.py | Passage completeness (reading-unit repair) — per book, reusable. |  |  |  |
| scripts_apply_passage_process_markers_v1_20260701 | scripts/archive/_apply_passage_process_markers_v1_20260701.py | _apply_passage_process_markers_v1_20260701.py |  |  |  |
| scripts_apply_persist_narration_finding_v1 | scripts/archive/_apply_persist_narration_finding_v1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_persist_narration_finding_v1.py (2026-06-15) — persist the templated narration as the single |  |  |  |
| scripts_apply_phase2_flags_patch | scripts/archive/_apply_phase2_flags_patch.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Apply phase2-flag-reassessment-20260319-v1.json |  |  |  |
| scripts_apply_poetic_chapter_lexical_v1_20260702 | scripts/archive/_apply_poetic_chapter_lexical_v1_20260702.py | _apply_poetic_chapter_lexical_v1_20260702.py |  |  |  |
| scripts_apply_prose_programme_chapter01 | scripts/archive/_apply_prose_programme_chapter01.py | _apply_prose_programme_chapter01.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_psalm_role_reassess_v1_20260706 | scripts/archive/_apply_psalm_role_reassess_v1_20260706.py | _apply_psalm_role_reassess_v1_20260706.py — Step 2: re-assess the role dimension for a psalm. |  |  |  |
| scripts_apply_psalms_gate1_completeness_v1_20260706 | scripts/archive/_apply_psalms_gate1_completeness_v1_20260706.py | _apply_psalms_gate1_completeness_v1_20260706.py — Step (d) Gate-1 completeness for PSALMS. |  |  |  |
| scripts_apply_psalms_gate1_reactivate_v1_20260706 | scripts/archive/_apply_psalms_gate1_reactivate_v1_20260706.py | _apply_psalms_gate1_reactivate_v1_20260706.py — finish Step (d) for Psalms. |  |  |  |
| scripts_apply_psalms_linkage_fix_v1_20260706 | scripts/archive/_apply_psalms_linkage_fix_v1_20260706.py | _apply_psalms_linkage_fix_v1_20260706.py — Step 1 (linkages) for PSALMS only. |  |  |  |
| scripts_apply_rebuild_ib_char_meaning_keyed_v3_20260711 | scripts/archive/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py | (v3) Rebuild ib_characteristic keyed on MEANING-IN-CONTEXT, not base lemma. |  |  |  |
| scripts_apply_rebuild_passages_consecutive_v2_20260701 | scripts/archive/_apply_rebuild_passages_consecutive_v2_20260701.py | _apply_rebuild_passages_consecutive_v2_20260701.py |  |  |  |
| scripts_apply_recode_sessionb_m10_findings_20260623 | scripts/archive/_apply_recode_sessionb_m10_findings_20260623.py | Recode mis-migrated session_b CLUSTER-level findings off M10 to their correct |  |  |  |
| scripts_apply_registry_metadata_patch | scripts/archive/_apply_registry_metadata_patch.py | _apply_registry_metadata_patch.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_reread_lexical_v1_20260709 | scripts/archive/_apply_reread_lexical_v1_20260709.py | Apply a char-driven re-read lexical JSON to ve_lexical. REUSABLE per chapter/book. |  |  |  |
| scripts_apply_reread_roles_from_velexical_v1_20260709 | scripts/archive/_apply_reread_roles_from_velexical_v1_20260709.py | _apply_reread_roles_from_velexical_v1_20260709.py |  |  |  |
| scripts_apply_reset_l2_meaning_flags | scripts/archive/_apply_reset_l2_meaning_flags.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_reset_l2_meaning_flags.py — WRITES. Recomputes finding.flagged_for_review for ALL l2_meaning |  |  |  |
| scripts_apply_retrofit_dims_v1_20260714 | scripts/archive/_apply_retrofit_dims_v1_20260714.py | Retrofit-authoring apply for the new/reinstated dimensions (v1, 2026-07-14). |  |  |  |
| scripts_apply_role_reassess_v1_20260707 | scripts/archive/_apply_role_reassess_v1_20260707.py | _apply_role_reassess_v1_20260707.py — Step (c) role reassessment, generalised per book. |  |  |  |
| scripts_apply_ruthlessness_sanitycheck_rerun_v4_20260702 | scripts/archive/_apply_ruthlessness_sanitycheck_rerun_v4_20260702.py | _apply_ruthlessness_sanitycheck_rerun_v4_20260702.py |  |  |  |
| scripts_apply_schema_ve_pairmodel_genre_v1_20260702 | scripts/archive/_apply_schema_ve_pairmodel_genre_v1_20260702.py | _apply_schema_ve_pairmodel_genre_v1_20260702.py |  |  |  |
| scripts_apply_seed_ib_characteristic_registry_v1_20260703 | scripts/archive/_apply_seed_ib_characteristic_registry_v1_20260703.py | Create + seed the inner-being CHARACTERISTIC control registry (ib_characteristic). |  |  |  |
| scripts_apply_sense_from_subgloss | scripts/archive/_apply_sense_from_subgloss.py | _apply_sense_from_subgloss.py (2026-06-15) — set VE1 (sense) in ve_lexical to the PER-OCCURRENCE STEP -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_session_patch | scripts/archive/apply_session_patch.py | apply_session_patch.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_softdelete_excluded_empty_terms | scripts/archive/_apply_softdelete_excluded_empty_terms.py | _apply_softdelete_excluded_empty_terms.py (2026-06-15) — ground the canonical term list: -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_softdelete_orphan_verses | scripts/archive/_apply_softdelete_orphan_verses.py | _apply_softdelete_orphan_verses.py — D2b option A (2026-06-15): soft-delete ACTIVE verses that are -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_stamp_char_candidate_on_master_v1_20260708 | scripts/archive/_apply_stamp_char_candidate_on_master_v1_20260708.py | _apply_stamp_char_candidate_on_master_v1_20260708.py — M65: stamp the candidate-characteristic |  |  |  |
| scripts_apply_stem_patch | scripts/archive/_apply_stem_patch.py | Apply stem-extraction-patch-20260319-v1.json -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_supersede_old_mechanical | scripts/archive/_apply_supersede_old_mechanical.py | _apply_supersede_old_mechanical.py — WRITES (reversible soft-delete). Supersedes the old l2_mechanical -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_t2_soft_delete | scripts/archive/_apply_t2_soft_delete.py | _apply_t2_soft_delete.py — soft-delete Parked (T2) terms that NEVER co-occur with a characteristic. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_term_decisions | scripts/archive/_apply_term_decisions.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_term_decisions.py |  |  |  |
| scripts_apply_term_driven_lexical_ruthlessness_v7_20260702 | scripts/archive/_apply_term_driven_lexical_ruthlessness_v7_20260702.py | _apply_term_driven_lexical_ruthlessness_v7_20260702.py |  |  |  |
| scripts_apply_ve_lexical_phase1_archive_legacy_20260702 | scripts/archive/_apply_ve_lexical_phase1_archive_legacy_20260702.py | _apply_ve_lexical_phase1_archive_legacy_20260702.py  (M63, schema -> 3.37.0) |  |  |  |
| scripts_apply_ve_lexical_span_keyable_v1_20260702 | scripts/archive/_apply_ve_lexical_span_keyable_v1_20260702.py | _apply_ve_lexical_span_keyable_v1_20260702.py |  |  |  |
| scripts_apply_ve_rebuild_mechanical_v1 | scripts/archive/_apply_ve_rebuild_mechanical_v1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_ve_rebuild_mechanical_v1.py (2026-06-15) — mechanical rebuild of ve_lexical fields |  |  |  |
| scripts_apply_verse_read_meaning | scripts/archive/_apply_verse_read_meaning.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_verse_read_meaning.py — L2 VERSE-READ = MEANING pipeline (verse-complete, term-driven). |  |  |  |
| scripts_apply_verse_record_link_repair_all_ot_v1_20260708 | scripts/archive/_apply_verse_record_link_repair_all_ot_v1_20260708.py | Verse-record -> verse / master-index link repair, WHOLE OT in one pass. |  |  |  |
| scripts_apply_verse_record_link_repair_v1_20260707 | scripts/archive/_apply_verse_record_link_repair_v1_20260707.py | Verse-record -> verse / master-index link repair (per book, reusable). |  |  |  |
| scripts_apply_verse_record_structural_backfill_v1_20260705 | scripts/archive/_apply_verse_record_structural_backfill_v1_20260705.py | _apply_verse_record_structural_backfill_v1_20260705.py — safe, determinate structural backfill. |  |  |  |
| scripts_apply_verse_record_traceability_v1_20260704 | scripts/archive/_apply_verse_record_traceability_v1_20260704.py | Add analysis-traceability columns to wa_verse_records (the primary control table). |  |  |  |
| scripts_apply_verse_uniqueness_cleanup | scripts/archive/_apply_verse_uniqueness_cleanup.py | _apply_verse_uniqueness_cleanup.py (2026-06-15) — move wa_verse_records toward "one active row per -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_vr_link_targetword_and_flag_v1_20260708 | scripts/archive/_apply_vr_link_targetword_and_flag_v1_20260708.py | Second-pass verse-record link repair for the multi-span (ambiguous) OT residual. |  |  |  |
| scripts_apply_wipe_ve_lexical_v1 | scripts/archive/_apply_wipe_ve_lexical_v1.py | _apply_wipe_ve_lexical_v1.py (2026-06-15) — PERMANENTLY remove all rows from ve_lexical. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_write_ruthlessness_index_driven_v3_20260702 | scripts/archive/_apply_write_ruthlessness_index_driven_v3_20260702.py | _apply_write_ruthlessness_index_driven_v3_20260702.py |  |  |  |
| scripts_apply_write_ruthlessness_lexical_v1_20260702 | scripts/archive/_apply_write_ruthlessness_lexical_v1_20260702.py | _apply_write_ruthlessness_lexical_v1_20260702.py |  |  |  |
| scripts_apply_write_ruthlessness_passages_full_v2_20260702 | scripts/archive/_apply_write_ruthlessness_passages_full_v2_20260702.py | _apply_write_ruthlessness_passages_full_v2_20260702.py |  |  |  |
| scripts_archive_discover_file_locations_v1_20260928 | scripts/archive/_discover_file_locations_v1_20260928.py | Retired (#2200): not in a utility or module. Was scripts/_discover_file_locations_v1_20260928.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| scripts_archive_env_setup | scripts/archive/env_setup.ps1 | Retired (#2200): not in a utility or module. Was scripts/env_setup.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| scripts_archive_generate_iba_db_schema_report | scripts/archive/generate-iba-db-schema-report.ps1 | Retired (#2200): not in a utility or module. Was scripts/generate-iba-db-schema-report.ps1. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| scripts_assess_cluster_profiles | scripts/archive/_assess_cluster_profiles.py | _assess_cluster_profiles.py — READ-ONLY. Per-cluster L1 profile correlated to the co-occurrence matrix: -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_cluster_v3_2_preeval | scripts/archive/_assess_cluster_v3_2_preeval.py | _assess_cluster_v3_2_preeval.py  — READ-ONLY V3_2 cluster pre-evaluation. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_corpus_keyword_map | scripts/archive/_assess_corpus_keyword_map.py | _assess_corpus_keyword_map.py — READ-ONLY. Corpus-wide PRELIMINARY keyword allocation: runs the validated -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_corpus_keyword_typed | scripts/archive/_assess_corpus_keyword_typed.py | _assess_corpus_keyword_typed.py — READ-ONLY. Corpus keyword map v2: each term gets its THING-TYPE -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_cross_cluster_cooccurrence | scripts/archive/_assess_cross_cluster_cooccurrence.py | _assess_cross_cluster_cooccurrence.py — READ-ONLY. The cross-cluster co-occurrence matrix: which -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_keyword_corpus_report | scripts/archive/_assess_keyword_corpus_report.py | _assess_keyword_corpus_report.py — READ-ONLY. Directional assessment of the corpus-wide keyword -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_keyword_overlap | scripts/archive/_assess_keyword_overlap.py | _assess_keyword_overlap.py — READ-ONLY. Cluster-level keyword overlap (angle 5). Builds each cluster's -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_l2_findings_view | scripts/archive/_assess_l2_findings_view.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_l2_findings_view.py — READ-ONLY. For each requested cluster, shows the L1 + L2 results per verse: |  |  |  |
| scripts_assess_l2_triage | scripts/archive/_assess_l2_triage.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_l2_triage.py — READ-ONLY. Runs the L2 MECHANICAL pass + ADEQUACY TRIAGE on every verse of a term: |  |  |  |
| scripts_assess_link_correlation | scripts/archive/_assess_link_correlation.py | _assess_link_correlation.py — READ-ONLY. The correlated roll-up: ties angle 1 (co-occurrence = CONTEXTUAL -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_meaning_tables | scripts/archive/_assess_meaning_tables.py | _assess_meaning_tables.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_mti_duplicate_terms | scripts/archive/_assess_mti_duplicate_terms.py | _assess_mti_duplicate_terms.py — READ-ONLY. Re-surfaces OT-DBR-009 (mti_terms duplication) from the -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_p2_verse_scenarios | scripts/archive/_assess_p2_verse_scenarios.py | _assess_p2_verse_scenarios.py — READ-ONLY. Types every verse of a cluster into the L2 decision-scenario -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_pipeline_integrity_v1_20260704 | scripts/archive/_assess_pipeline_integrity_v1_20260704.py | Read-only PIPELINE-INTEGRITY diagnostic for the verse-analysis (inner-being lexical) chain. |  |  |  |
| scripts_assess_qa_method_effectiveness | scripts/archive/_assess_qa_method_effectiveness.py | _assess_qa_method_effectiveness.py — read-only Q&A coverage extraction. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_qa_method_quality_review | scripts/archive/_assess_qa_method_quality_review.py | _assess_qa_method_quality_review.py — qualitative-review-oriented Q&A coverage. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_read_dedup | scripts/archive/_assess_read_dedup.py | _assess_read_dedup.py — READ-ONLY. Estimates how much the (expensive) read layer would DUPLICATE across -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_registry_grounding | scripts/archive/_assess_registry_grounding.py | _assess_registry_grounding.py — READ-ONLY. Tests the researcher's expectation: does every registry (anchor) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_registry_vs_keywords | scripts/archive/_assess_registry_vs_keywords.py | _assess_registry_vs_keywords.py — READ-ONLY. Diagnoses WHY some of the 214 registry (anchor) words are -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_relationship_probe | scripts/archive/_assess_relationship_probe.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_relationship_probe.py — READ-ONLY. For a cluster PAIR, pull the verses where both co-occur and |  |  |  |
| scripts_assess_shared_forms | scripts/archive/_assess_shared_forms.py | _assess_shared_forms.py — READ-ONLY. Shared-form / homonym index: transliterations whose terms are -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_study_state | scripts/archive/_assess_study_state.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Read-only: render the live state of the verse-lexical study to ONE page (verse-analysis/_STATE.md). |  |  |  |
| scripts_assess_t2_cleanup | scripts/archive/_assess_t2_cleanup.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_t2_cleanup.py  — READ-ONLY. Proposes a disposition for every Parked (T2) cluster term. |  |  |  |
| scripts_assess_t2_relevance_surface | scripts/archive/_assess_t2_relevance_surface.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_t2_relevance_surface.py  — READ-ONLY. |  |  |  |
| scripts_assess_termsense_ranking | scripts/archive/_assess_termsense_ranking.py | _assess_termsense_ranking.py — READ-ONLY. Reasonability check on the read-dedup: ranks every (term, sense) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_verse_assembly | scripts/archive/_assess_verse_assembly.py | _assess_verse_assembly.py — READ-ONLY. L1 establishment per verse for a cluster: assembles each verse's -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_verse_corroboration | scripts/archive/_assess_verse_corroboration.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_verse_corroboration.py  — READ-ONLY (A1 verse-meaning corroboration scan). |  |  |  |
| scripts_assess_verse_raw_data | scripts/archive/_assess_verse_raw_data.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Read-only: assemble the FULL raw study evidence for a verse -> markdown. |  |  |  |
| scripts_audit_cluster_against_instruction_v25_v1_20260518 | scripts/archive/_audit_cluster_against_instruction_v25_v1_20260518.py | Audit a cluster against v2_5 instruction compliance. |  |  |  |
| scripts_audit_cluster_v1_20260601 | scripts/archive/audit_cluster_v1_20260601.py | Consolidated, reusable cluster auditor (read-only). |  |  |  |
| scripts_audit_findings_v1_20260621 | scripts/archive/_audit_findings_v1_20260621.py | _audit_findings_v1_20260621.py — read-only findings audit (wa-findings-audit-spec-v1_0). |  |  |  |
| scripts_audit_gate1_additions_v1_20260706 | scripts/archive/_audit_gate1_additions_v1_20260706.py | Gate-1 onboarding audit — pre/post accountability for the orphan-term additions. |  |  |  |
| scripts_audit_step_extract_archiving | scripts/archive/_audit_step_extract_archiving.py | Auditor + applicator for STEP Extracts archiving. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_backfill_root_families | scripts/archive/backfill_root_families.py | backfill_root_families.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_backfill_span_match | scripts/archive/_backfill_span_match.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _backfill_span_match.py |  |  |  |
| scripts_backup_db_to_nas | scripts/backup_db_to_nas.py | backup_db_to_nas.py -- consistent off-Drive backup of bible_research.db or iba.db to the NAS (integrity check, backup-API snapshot, hash-verified copy, grandfather-father-son pruning, local status and alert). Settings from cfg_setting backup.nas_db_backup, with a built-in fallback when iba.db cannot be read. | ✓ |  |  |
| scripts_backup_watchdog | scripts/backup_watchdog.ps1 | Watchdog over the NAS backup jobs, run by the scheduled task 'BibleResearch Backup Watchdog'. | ✓ | ✓ | operational script outside the dispatcher (#2200) |
| scripts_batch_audit | scripts/archive/_batch_audit.py | _batch_audit.py — Run audit_word on all registries that need it. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_batch_extract | scripts/archive/_batch_extract.py | _batch_extract.py — Run STEP extraction for all words that need a discovery JSON. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_M01_verse_read_review | scripts/archive/_build_M01_verse_read_review.py | _build_M01_verse_read_review.py — READ-ONLY. Full M01 verse-complete run review: coverage, cross-cluster -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_cause_api_package | scripts/archive/build_cause_api_package.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_cause_api_package.py (2026-06-16) — Alt 2: prepare a focused, single-purpose API run that does |  |  |  |
| scripts_build_cluster_findings_digest | scripts/archive/build_cluster_findings_digest.py | Read-only: dump a cluster's active findings as a navigable markdown digest. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_cluster_verse_read_gate | scripts/archive/_build_cluster_verse_read_gate.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_cluster_verse_read_gate.py — READ-ONLY. The standard PER-CLUSTER GATE report produced as each |  |  |  |
| scripts_build_complete_extract | scripts/archive/build_complete_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_complete_extract.py |  |  |  |
| scripts_build_corpus_prose | scripts/archive/build_corpus_prose.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_corpus_prose.py — Compile completed word-analysis chapters into a book. |  |  |  |
| scripts_build_correlation_extract | scripts/archive/build_correlation_extract.py | build_correlation_extract.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_dimension_extract | scripts/archive/build_dimension_extract.py | build_dimension_extract.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_field_api_package | scripts/archive/build_field_api_package.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_field_api_package.py (2026-06-16) — Alt 3: prepare a focused, single-instruction API read for ANY |  |  |  |
| scripts_build_file_manifest | archive/scripts/build_file_manifest.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_file_manifest.py — Generates database/file_manifest.json -- RETIRED 2026-08-18 (escalation #730): superseded by iba.db manifest.rebuild/manifest.search (escalation #691, applied 2026-08-15); moved to archive/, database/file_manifest.json moved to database/archive/. |  |  |  |
| scripts_build_file_patterns_extract | scripts/archive/build_file_patterns_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_file_patterns_extract.py — File-name pattern registry extract (M35). |  |  |  |
| scripts_build_flag_classification_package_v1_20260601 | scripts/archive/build_flag_classification_package_v1_20260601.py | Assemble the FLAG-cluster classification package for Claude AI (chat). |  |  |  |
| scripts_build_gate1_registry_final_map_v1_20260706 | scripts/archive/_build_gate1_registry_final_map_v1_20260706.py | Read-only: render the FINAL single-home-per-term registry mapping for the 97 gate1 orphans, |  |  |  |
| scripts_build_label_patterns_extract | scripts/archive/build_label_patterns_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_label_patterns_extract.py — Label pattern registry extract (M35). |  |  |  |
| scripts_build_m01_by_characteristic | scripts/archive/build_m01_by_characteristic.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_m01_by_characteristic.py (2026-06-18) — emit M01 verse-records grouped BY characteristic. |  |  |  |
| scripts_build_m01_findings_oldnew_extract | scripts/archive/build_m01_findings_oldnew_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_m01_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M01 findings: |  |  |  |
| scripts_build_m02_findings_oldnew_extract | scripts/archive/build_m02_findings_oldnew_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_m02_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M02 findings: |  |  |  |
| scripts_build_m04_characteristic_phase9_bundle_20260519 | scripts/archive/_build_m04_characteristic_phase9_bundle_20260519.py | Build a multi-characteristic Phase 9 AI package (bundle). |  |  |  |
| scripts_build_m04_characteristic_phase9_package_20260518 | scripts/archive/_build_m04_characteristic_phase9_package_20260518.py | Build a per-characteristic Phase 9 AI package for M04. |  |  |  |
| scripts_build_m08_characteristic_phase9_bundle_20260521 | scripts/archive/_build_m08_characteristic_phase9_bundle_20260521.py | Build a multi-characteristic Phase 9 AI package (bundle). |  |  |  |
| scripts_build_m08_characteristic_phase9_package_20260521 | scripts/archive/_build_m08_characteristic_phase9_package_20260521.py | Build a per-characteristic Phase 9 AI package for M08. |  |  |  |
| scripts_build_m10_unit_verse_evidence_20260623 | scripts/archive/_build_m10_unit_verse_evidence_20260623.py | Emit the PER-VERSE structured evidence section for an M10 unit, from the on-disk |  |  |  |
| scripts_build_obs_catalogue_export | scripts/archive/build_obs_catalogue_export.py | build_obs_catalogue_export.py — generic Observation Question Catalogue export. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_obs_catalogue_tiered_extract | scripts/archive/build_obs_catalogue_tiered_extract.py | build_obs_catalogue_tiered_extract.py — read-only. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_patch_types_extract | scripts/archive/build_patch_types_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_patch_types_extract.py — Patch type registry extract (M35 scope). |  |  |  |
| scripts_build_programme_prose_extract | scripts/build_programme_prose_extract.py | CLI entry point for the programme-prose extract; the logic is iba/app/lib/prosestore.py, also run as prose.extract (Prose.ps1 -Step Extract). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_build_projection_v2_20260714 | scripts/archive/_build_projection_v2_20260714.py | Build the flattened reading projection + technical data layer for a re-read book (v2, 2026-07-14). |  |  |  |
| scripts_build_ps119 | scripts/archive/_build_ps119.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Persistent char-by-char builder for Ps 119 (641 candidates, 176 verses). |  |  |  |
| scripts_build_reference_snapshot | scripts/archive/build_reference_snapshot.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_reference_snapshot.py — Reference-as-Database snapshot extractor. |  |  |  |
| scripts_build_rules_extract | scripts/archive/build_rules_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_rules_extract.py — Global rules + addenda JSON extract. |  |  |  |
| scripts_build_script_registry | scripts/archive/build_script_registry.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_script_registry.py — canonical, regenerable registry of the project's scripts. |  |  |  |
| scripts_build_session_a_prose | scripts/archive/build_session_a_prose.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Render per-word Session A prose as a self-contained `.md` for Verse Context input. |  |  |  |
| scripts_build_t2_flag_sample | scripts/archive/_build_t2_flag_sample.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_t2_flag_sample.py — READ-ONLY. Shows real verses + meaning paragraphs from the T2 and FLAG buckets, |  |  |  |
| scripts_build_term_verse_findings_report | scripts/archive/_build_term_verse_findings_report.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_term_verse_findings_report.py — READ-ONLY. For N terms, show up to K verses each with the verse |  |  |  |
| scripts_build_tier_catalogue_update_patch_20260619 | scripts/archive/build_tier_catalogue_update_patch_20260619.py | build_tier_catalogue_update_patch_20260619.py — emit the tier-catalogue refit as a reviewable JSON patch. |  |  |  |
| scripts_build_vc_batch | scripts/archive/_build_vc_batch.py | _build_vc_batch.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_vc_revision_ledger | scripts/archive/_build_vc_revision_ledger.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Build the VC revision ledger from VCB-7..11 patches. |  |  |  |
| scripts_build_ve_lexical_extract | scripts/archive/build_ve_lexical_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_ve_lexical_extract.py (2026-06-16) — emit a cluster's v2 verse-lexical as JSON for AI Chat. |  |  |  |
| scripts_build_verse_read_pilot_review | scripts/archive/_build_verse_read_pilot_review.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_verse_read_pilot_review.py — READ-ONLY. Assembles the M01 verse-read pilot review: |  |  |  |
| scripts_build_vocab_extract | scripts/archive/build_vocab_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_vocab_extract.py — Controlled vocabulary extract (M32 scope). |  |  |  |
| scripts_build_word_relationship_report | scripts/archive/build_word_relationship_report.py | build_word_relationship_report.py — READ-ONLY. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_cc_verse_read | scripts/archive/_cc_verse_read.py | _cc_verse_read.py — CC-GENERATION mode of the verse-read = meaning layer. Same output as the API pipeline -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_book_lexical_readiness_v1_20260712 | scripts/archive/_check_book_lexical_readiness_v1_20260712.py | Book lexical-rework READINESS assessment (read-only). |  |  |  |
| scripts_check_dimension_band_drift_v1_20260714 | scripts/archive/_check_dimension_band_drift_v1_20260714.py | Reader-drift diagnostic for every ve dimension (v1, 2026-07-14). |  |  |  |
| scripts_check_doc_versions | scripts/archive/_check_doc_versions.py | GR-FILE-003 compliance check for instruction documents. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_family_narratives_20260712 | scripts/archive/_check_family_narratives_20260712.py | Verify a family's narrative JSON against its base source WORK_CONTRACT. |  |  |  |
| scripts_check_fi_ti_chain | scripts/archive/_check_fi_ti_chain.py | 1. wa_term_inventory rows with no parent in wa_file_index (orphaned terms) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_ib_char_i7_v1_20260714 | scripts/archive/_check_ib_char_i7_v1_20260714.py | Cheap I7 check (v1, 2026-07-14) — read-2026 characteristics with NO ib_char link. |  |  |  |
| scripts_check_integrity_controls | scripts/archive/_check_integrity_controls.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _check_integrity_controls.py (2026-06-28) — DB integrity anchor for the term-orphan build (READ-ONLY). |  |  |  |
| scripts_check_lexical_content_validity_v1_20260714 | scripts/archive/_check_lexical_content_validity_v1_20260714.py | CONTENT-VALIDITY gate for a re-read book (v1, 2026-07-14). |  |  |  |
| scripts_check_m10_cross_cluster_bonds_20260623 | scripts/archive/_check_m10_cross_cluster_bonds_20260623.py | Cross-cluster BONDS for the M10-family logical units (read-only). |  |  |  |
| scripts_check_mti_terms | scripts/archive/_check_mti_terms.py | Consistency check for mti_terms table. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_passage_reading_coverage_v1_20260704 | scripts/archive/_check_passage_reading_coverage_v1_20260704.py | _check_passage_reading_coverage_v1_20260704.py |  |  |  |
| scripts_check_psalms_reread_progress_v1_20260709 | scripts/archive/_check_psalms_reread_progress_v1_20260709.py | Psalms re-read progress monitor — READ-ONLY. Run anytime to see how far the re-read has got. |  |  |  |
| scripts_check_reread_conformance_v1_20260714 | scripts/archive/_check_reread_conformance_v1_20260714.py | Reusable per-cycle re-read conformance check (v1, 2026-07-14). |  |  |  |
| scripts_check_reread_measures_v3_20260709 | scripts/archive/_check_reread_measures_v3_20260709.py | Re-read success measures (G0-G10) — READ-ONLY, BOOK-GENERAL. v3 (2026-07-09). |  |  |  |
| scripts_check_softdelete_integrity | scripts/archive/_check_softdelete_integrity.py | _check_softdelete_integrity.py — H5 (2026-06-15): the standing soft-delete integrity check, and the -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_ve_seat_completeness | scripts/archive/_check_ve_seat_completeness.py | _check_ve_seat_completeness.py — standing guard: is the location SEAT vocabulary complete? -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_ve_signal_lists | scripts/archive/_check_ve_signal_lists.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _check_ve_signal_lists.py — completeness audit of EVERY seed/signal list in the VE engine. |  |  |  |
| scripts_classify_term_introduction_source | scripts/archive/classify_term_introduction_source.py | classify_term_introduction_source.py — Heuristic classifier for M30 backfill. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_combine_cluster_published_to_docx | scripts/archive/combine_cluster_published_to_docx.py | Combine the latest chapter drafts in a cluster's Published/ folder into one .docx. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_cost_ledger | scripts/archive/cost_ledger.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). cost_ledger.py — ONE combined cost ledger across all three Claude surfaces. |  |  |  |
| scripts_db_introspect | scripts/archive/_db_introspect.py | Temporary introspection script — outputs JSON for report generation. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_delete_empty_fi | scripts/archive/_delete_empty_fi.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). fi.id rows to KEEP (backlog words with strongs_list, awaiting new-word import) |  |  |  |
| scripts_derive_retrofit_dims_v1_20260714 | scripts/archive/_derive_retrofit_dims_v1_20260714.py | Derive the 5 retrofit dims (intensity/specifier/effect/device/direction) for read-2026 chars, |  |  |  |
| scripts_discover_word_terms | scripts/archive/_discover_word_terms.py | _discover_word_terms.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_discovery_archive_check_glossary_fallout_20260902 | scripts/discovery/archive/_check_glossary_fallout-20260902.py | Retired (#2200): not in a utility or module. Was scripts/discovery/_check_glossary_fallout-20260902.py. |  | ✓ | retired script (#2200): kept for reference only; use needs the researcher's approval |
| scripts_exploratory_brief_meaning_router_v1_20260504 | scripts/archive/_exploratory_brief_meaning_router_v1_20260504.py | _exploratory_brief_meaning_router_v1_20260504.py — read-only. |  |  |  |
| scripts_exploratory_brief_verse_router_v1_20260504 | scripts/archive/_exploratory_brief_verse_router_v1_20260504.py | _exploratory_brief_verse_router_v1_20260504.py — read-only. |  |  |  |
| scripts_exploratory_unclassified_verse_sample_v1_20260504 | scripts/archive/_exploratory_unclassified_verse_sample_v1_20260504.py | _exploratory_unclassified_verse_sample_v1_20260504.py — read-only. |  |  |  |
| scripts_explore_cluster_timing | scripts/archive/_explore_cluster_timing.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_cluster_timing.py — READ-ONLY timing analysis of completed L2 verse-read clusters. |  |  |  |
| scripts_explore_drop_code_findings | scripts/archive/_explore_drop_code_findings.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_drop_code_findings.py — READ-ONLY extract of every finding referencing the §3 DROP tier codes. |  |  |  |
| scripts_explore_m_vs_r_divergence | scripts/archive/_explore_m_vs_r_divergence.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_m_vs_r_divergence.py — READ-ONLY. For VE-01 (obs 395), compare the MECHANICAL term-gloss (M) |  |  |  |
| scripts_explore_tier_findings | scripts/archive/_explore_tier_findings.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_tier_findings.py — READ-ONLY explorer/export for the L2 verse-read tier findings. |  |  |  |
| scripts_explore_ve_by_cluster | scripts/archive/_explore_ve_by_cluster.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_ve_by_cluster.py — READ-ONLY: VE field x cluster x value comparison across clusters. |  |  |  |
| scripts_export_database_schema | scripts/archive/export_database_schema.py | export_database_schema.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_export_md_to_pdf_v1_20260703 | scripts/archive/_export_md_to_pdf_v1_20260703.py | Reusable Markdown -> PDF exporter (reportlab; no external binaries). |  |  |  |
| scripts_export_prose_chapter_edit | scripts/export_prose_chapter_edit.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.export_chapter (Prose.ps1 -Step ExportChapter). Kept as the documented CLI entry point, reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_export_prose_to_md_v1_20260703 | scripts/archive/_export_prose_to_md_v1_20260703.py | Regenerate folder .md documents FROM the DB corpus (prose_section is canonical), |  |  |  |
| scripts_export_tier_catalogue | scripts/archive/export_tier_catalogue.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). export_tier_catalogue.py (2026-06-17) — read-only export of the Tier Catalogue |  |  |  |
| scripts_export_ve_status_reports | scripts/archive/export_ve_status_reports.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). export_ve_status_reports.py (2026-06-17) — two read-only status reports over `ve_lexical`: |  |  |  |
| scripts_export_word_json | scripts/archive/export_word_json.py | export_word_json.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_extract_m10_core_group_20260623 | scripts/archive/_extract_m10_core_group_20260623.py | Mechanical assembly of an M10 CORE reading group from the on-disk corpus |  |  |  |
| scripts_extract_term_data | scripts/archive/extract_term_data.py | extract_term_data.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_cluster_findings_report_v1_20260506 | scripts/archive/_generate_cluster_findings_report_v1_20260506.py | _generate_cluster_findings_report_v1_20260506.py — read-only. |  |  |  |
| scripts_generate_cluster_gate | scripts/archive/_generate_cluster_gate.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _generate_cluster_gate.py  — READ-ONLY per-cluster gate report for the L2 verse-read. |  |  |  |
| scripts_generate_cluster_keyword_analytics_v1_20260523 | scripts/archive/_generate_cluster_keyword_analytics_v1_20260523.py | Generate a cluster-level keyword analytics report from verse_context.keywords. |  |  |  |
| scripts_generate_cluster_overview_v1_20260508 | scripts/archive/_generate_cluster_overview_v1_20260508.py | _generate_cluster_overview_v1_20260508.py — read-only. |  |  |  |
| scripts_generate_cluster_summary_v1_20260603 | scripts/archive/generate_cluster_summary_v1_20260603.py | generate_cluster_summary_v1_20260603.py |  |  |  |
| scripts_generate_cluster_term_report_v1_20260505 | scripts/archive/_generate_cluster_term_report_v1_20260505.py | _generate_cluster_term_report_v1_20260505.py — read-only. |  |  |  |
| scripts_generate_dimension_report | scripts/archive/_generate_dimension_report.py | Generate a dimension index summary report. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_full_cluster_audit_v1_20260603 | scripts/archive/generate_full_cluster_audit_v1_20260603.py | generate_full_cluster_audit_v1_20260603.py  (READ-ONLY) |  |  |  |
| scripts_generate_meaning_quality_check | scripts/archive/_generate_meaning_quality_check.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Read-only quality-check report: N random covered verses per term, showing the |  |  |  |
| scripts_generate_programme_report | scripts/archive/_generate_programme_report.py | Generate a comprehensive programme status report. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_programme_snapshot | scripts/archive/generate_programme_snapshot.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Generate a programme snapshot report. |  |  |  |
| scripts_generate_registry_overview | scripts/archive/generate_registry_overview.py | generate_registry_overview.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_session_a_extract | scripts/archive/generate_session_a_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). generate_session_a_extract.py — Mechanical Session A extract generator. |  |  |  |
| scripts_generate_verse_meanings_export | scripts/archive/_generate_verse_meanings_export.py | Read-only export of verse MEANINGS (l2_meaning paragraphs only) for a cluster. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_harvest_characteristic_evidence_v1_20260703 | scripts/archive/_harvest_characteristic_evidence_v1_20260703.py | Read-only harvest: scan the 150 Psalm Phase-2 readings for the recurring |  |  |  |
| scripts_import_prose_chapter_edit | scripts/import_prose_chapter_edit.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.import_chapter (Prose.ps1 -Step ImportChapter). Kept as the documented CLI entry point, reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_inspect_db_only_terms | scripts/archive/inspect_db_only_terms.py | Detail query for DB_ONLY terms flagged during soul audit. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_inspect_unit_lexical_v1_20260703 | scripts/archive/_inspect_unit_lexical_v1_20260703.py | Read-back inspector: lay a segmentation UNIT's verse text alongside its Phase-1 |  |  |  |
| scripts_install_backup_watchdog_task | scripts/install_backup_watchdog_task.ps1 | Installs the backup watchdog scheduled task. | ✓ | ✓ | operational script outside the dispatcher (#2200) |
| scripts_integrity_full_check | scripts/archive/_integrity_full_check.py | DB path resolved relative to this script (project moved off Google Drive 2026-06-03; see CLAUDE.md §13) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_keyword_cluster_analysis_v1_20260523 | scripts/archive/_keyword_cluster_analysis_v1_20260523.py | Stage 2 keyword clustering analysis for the discovery pass. |  |  |  |
| scripts_keyword_discovery_subgroup_v1_20260523 | scripts/archive/_keyword_discovery_subgroup_v1_20260523.py | Interim keyword-discovery pass for an under-digested sub-group. |  |  |  |
| scripts_lexical_revelation_test_20260624 | scripts/archive/_lexical_revelation_test_20260624.py | Lexical-Revelation Test (LRT) — runs DURING deep evidence gathering (step 3) to |  |  |  |
| scripts_list_shared_words | scripts/archive/_list_shared_words.py | List all 100%-shared words with their terms and cross-registry links. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_list_tables | scripts/archive/list_tables.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_load_keywords_to_db_v1_20260523 | scripts/archive/_load_keywords_to_db_v1_20260523.py | Load inner-being keywords from discovery JSONs into verse_context.keywords. |  |  |  |
| scripts_mirror_to_nas | scripts/mirror_to_nas.ps1 | Daily full project mirror to the NAS, run by the scheduled task 'BibleResearch Full Mirror to NAS'. | ✓ | ✓ | operational script outside the dispatcher (#2200) |
| scripts_notify_backup_alert | scripts/notify_backup_alert.ps1 | Alert sink for the NAS backup jobs and the watchdog (backup.alerting_policy). | ✓ | ✓ | operational script outside the dispatcher (#2200) |
| scripts_onboard_satan_h7854_v1_20260706 | scripts/archive/_onboard_satan_h7854_v1_20260706.py | Force-onboard H7854 (Satan) into the 'spiritual powers' registry (195) as a third-party |  |  |  |
| scripts_patch_report | scripts/archive/_patch_report.py | Apply all corrections and additions to the programme report in one pass. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_populate_dimension_index | scripts/archive/populate_dimension_index.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). populate_dimension_index.py |  |  |  |
| scripts_preflight_m20_dir_005_M20_A_mapping | scripts/archive/_preflight_m20_dir_005_M20_A_mapping.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Pre-flight for DIR-20260513-005 (M20-A mapping apply). |  |  |  |
| scripts_pro_read_lib | scripts/archive/_pro_read_lib.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Compact builder for Proverbs char-driven readings (Stage-4). |  |  |  |
| scripts_probe_gate1_registry_homes_v1_20260706 | scripts/archive/_probe_gate1_registry_homes_v1_20260706.py | Read-only: for each of the 97 gate1 orphan strongs, find its natural registry home. |  |  |  |
| scripts_probe_gate1_span_orphans_v1_20260705 | scripts/archive/_probe_gate1_span_orphans_v1_20260705.py | _probe_gate1_span_orphans_v1_20260705.py  — Gate-1 span-orphan audit (reusable, read-only). |  |  |  |
| scripts_probe_isa43_validation_dump_v1_20260705 | scripts/archive/_probe_isa43_validation_dump_v1_20260705.py | _probe_isa43_validation_dump_v1_20260705.py — full DB dump for Isa 43:1-2 (read-only). |  |  |  |
| scripts_probe_lexical_all14_v8_20260702 | scripts/archive/_probe_lexical_all14_v8_20260702.py | _probe_lexical_all14_v8_20260702.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_all14_v5_20260701 | scripts/archive/_probe_lexical_derivation_all14_v5_20260701.py | _probe_lexical_derivation_all14_v5_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_all14_v6_20260701 | scripts/archive/_probe_lexical_derivation_all14_v6_20260701.py | _probe_lexical_derivation_all14_v6_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_end_to_end_v4_20260701 | scripts/archive/_probe_lexical_derivation_end_to_end_v4_20260701.py | _probe_lexical_derivation_end_to_end_v4_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_harness_v1_20260701 | scripts/archive/_probe_lexical_derivation_harness_v1_20260701.py | _probe_lexical_derivation_harness_v1_20260701.py  (READ-ONLY validation harness) |  |  |  |
| scripts_probe_lexical_derivation_harness_v2_passage_20260701 | scripts/archive/_probe_lexical_derivation_harness_v2_passage_20260701.py | _probe_lexical_derivation_harness_v2_passage_20260701.py  (READ-ONLY, PASSAGE-AWARE) |  |  |  |
| scripts_probe_lexical_derivation_harness_v3_startup_20260701 | scripts/archive/_probe_lexical_derivation_harness_v3_startup_20260701.py | _probe_lexical_derivation_harness_v3_startup_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_passage_material_v1_20260704 | scripts/archive/_probe_passage_material_v1_20260704.py | Read-only: pull the raw material for one narrative passage (segment_unit) so the |  |  |  |
| scripts_probe_primary_span_prose_reference_v1_20260705 | scripts/archive/_probe_primary_span_prose_reference_v1_20260705.py | _probe_primary_span_prose_reference_v1_20260705.py — per book: primary spans + how many are |  |  |  |
| scripts_probe_psalms_gate1_completeness_v1_20260706 | scripts/archive/_probe_psalms_gate1_completeness_v1_20260706.py | _probe_psalms_gate1_completeness_v1_20260706.py — Step (d) diagnostic (read-only). |  |  |  |
| scripts_probe_psalms_gate1_validate_v1_20260706 | scripts/archive/_probe_psalms_gate1_validate_v1_20260706.py | _probe_psalms_gate1_validate_v1_20260706.py — Step (e) full-integrity validation (read-only). |  |  |  |
| scripts_probe_ve_lexical_per_book_census_v1_20260705 | scripts/archive/_probe_ve_lexical_per_book_census_v1_20260705.py | _probe_ve_lexical_per_book_census_v1_20260705.py — per-book ve_lexical extraction (read-only, DB only). |  |  |  |
| scripts_probe_verse_record_orphan_census_v1_20260705 | scripts/archive/_probe_verse_record_orphan_census_v1_20260705.py | _probe_verse_record_orphan_census_v1_20260705.py — per-book IB span-orphan census (read-only). |  |  |  |
| scripts_produce_family_base_source_json_20260711 | scripts/archive/_produce_family_base_source_json_20260711.py | Produce a JSON BASE SOURCE per family (+ one OUTLIERS file) for Psalms. |  |  |  |
| scripts_produce_family_cluster_comparison_20260711 | scripts/archive/_produce_family_cluster_comparison_20260711.py | Read-only: compare the FAMILY grouping (meaning/keyword-based) with the CLUSTER |  |  |  |
| scripts_produce_family_passage_base_source_v2_20260712 | scripts/archive/_produce_family_passage_base_source_v2_20260712.py | Base source per family — WORK-CONTRACT + PASSAGE-UNIT + RAW-COMPLETE + ANCHORED. |  |  |  |
| scripts_produce_final_extract | scripts/archive/_produce_final_extract.py | _produce_final_extract.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_produce_grain_index_v1_20260702 | scripts/archive/_produce_grain_index_v1_20260702.py | _produce_grain_index_v1_20260702.py  (READ-ONLY) |  |  |  |
| scripts_produce_registry_full_extract | scripts/archive/_produce_registry_full_extract.py | Produce a FULL markdown extract of a single registry word: every term and -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_produce_term_evidence_digest_v1_20260702 | scripts/archive/_produce_term_evidence_digest_v1_20260702.py | _produce_term_evidence_digest_v1_20260702.py  (READ-ONLY) |  |  |  |
| scripts_produce_vc_word_report | scripts/archive/_produce_vc_word_report.py | Produce a Verse Context word report — shows the full classification result -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_produce_ve_narration_v1 | scripts/archive/_produce_ve_narration_v1.py | _produce_ve_narration_v1.py (2026-06-15) — compose the TEMPLATED NARRATION for a term-in-verse -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_prototype_finding_lifecycle | scripts/archive/_prototype_finding_lifecycle.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_finding_lifecycle.py — READ-ONLY prototype of the finding correction cycle. Loads a findings |  |  |  |
| scripts_prototype_l1_mechanical | scripts/archive/_prototype_l1_mechanical.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_l1_mechanical.py  — READ-ONLY L1-mechanical prototype (resolves R2/R4/R6; R7 via --morph). |  |  |  |
| scripts_prototype_l1_morph | scripts/archive/_prototype_l1_morph.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_l1_morph.py  — READ-ONLY R7 morphology pass (STEP + DB). |  |  |  |
| scripts_prototype_meaning_run | scripts/archive/_prototype_meaning_run.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_meaning_run.py — READ-ONLY prototype of the L1 verse-level MEANING RUN. For a term, parses its |  |  |  |
| scripts_prototype_p1_keywords | scripts/archive/_prototype_p1_keywords.py | _prototype_p1_keywords.py — READ-ONLY prototype. Rebuilds the L1 keyword set from a term's STEP meaning -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_prototype_step_morph | scripts/archive/_prototype_step_morph.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_step_morph.py — READ-ONLY prototype. Pulls STEP preview HTML per verse and extracts the |  |  |  |
| scripts_pull_reread_passage_input_v1_20260714 | scripts/archive/_pull_reread_passage_input_v1_20260714.py | Leaner re-read passage-input pull (v1, 2026-07-14). |  |  |  |
| scripts_pull_verify_batch_v1_20260714 | scripts/archive/_pull_verify_batch_v1_20260714.py | Pull a batch of lexicals for MANUAL source-verification of one dimension (read-only, v1 2026-07-14). |  |  |  |
| scripts_purge_softdeleted_velexical_v1_20260714 | scripts/archive/_purge_softdeleted_velexical_v1_20260714.py | Hard-purge ANCIENT soft-deleted ve_lexical rows to reclaim DB space (v1, 2026-07-14). |  |  |  |
| scripts_query_h2734 | scripts/archive/query_h2734.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_readiness_sweep_pilot | scripts/archive/readiness_sweep_pilot.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Readiness Sweep Pilot — read-only inspection for a single registry. |  |  |  |
| scripts_readiness_sweep_programme_scan | scripts/archive/readiness_sweep_programme_scan.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Programme-wide readiness sweep scan. |  |  |  |
| scripts_realign_meaning_tables | scripts/archive/_realign_meaning_tables.py | _realign_meaning_tables.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_realign_quality_flags | scripts/archive/_realign_quality_flags.py | _realign_quality_flags.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_remediate_cluster_v1_20260602 | scripts/archive/_remediate_cluster_v1_20260602.py | Master cluster-remediation orchestrator (one cluster, packaged). |  |  |  |
| scripts_render_narratives_to_md_20260712 | scripts/archive/_render_narratives_to_md_20260712.py | Render a family's narrative output to readable markdown: each passage, then the |  |  |  |
| scripts_repair_02_zero_padding | scripts/archive/_repair_02_zero_padding.py | Fix 2 — Normalise zero-padded registry IDs in 4 tables. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_repair_03_wa_file_index | scripts/archive/_repair_03_wa_file_index.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 3 — Recreate wa_file_index to register FK to word_registry(id). |  |  |  |
| scripts_repair_05_wa_term_related_words | scripts/archive/_repair_05_wa_term_related_words.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 5 — Recreate wa_term_related_words to register FK to wa_term_inventory(id). |  |  |  |
| scripts_repair_06_wa_term_root_family | scripts/archive/_repair_06_wa_term_root_family.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 6 — Recreate wa_term_root_family to register FK to wa_term_inventory(id). |  |  |  |
| scripts_repair_07_wa_verse_records | scripts/archive/_repair_07_wa_verse_records.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 7 — Recreate wa_verse_records to register FKs to wa_file_index(id) |  |  |  |
| scripts_repair_step_missing_verses_v1_20260713 | scripts/archive/_repair_step_missing_verses_v1_20260713.py | Repair STEP-missing verse-records — morphology-anchored (researcher direction 2026-07-13). |  |  |  |
| scripts_reread_finish_v1_20260709 | scripts/archive/_reread_finish_v1_20260709.py | _reread_finish_v1_20260709.py -- finish one re-read chapter: apply -> gate -> commit -> close -> stamp. |  |  |  |
| scripts_reread_ledger_lib | scripts/archive/_reread_ledger_lib.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Reusable ledger-scaffolding helpers for the corrected-method Psalms reread. |  |  |  |
| scripts_reread_worklist_v1_20260709 | scripts/archive/_reread_worklist_v1_20260709.py | _reread_worklist_v1_20260709.py  --  control table for the isolated-per-chapter re-read loop. |  |  |  |
| scripts_reset_registry_status | scripts/archive/_reset_registry_status.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). One-off: reset word_registry.phase1_status for all 170 'In Progress' words. |  |  |  |
| scripts_reverse_findings_stageC_restrict_20260619 | scripts/archive/_reverse_findings_stageC_restrict_20260619.py | _reverse_findings_stageC_restrict_20260619.py — REVERSE Stage C (un-restrict the OLD findings). |  |  |  |
| scripts_roll_retrofit_v1_20260714 | scripts/archive/_roll_retrofit_v1_20260714.py | Roll the retrofit-dim derivation across a chapter batch: derive -> apply(live) -> READ-BACK (v1, 2026-07-14). |  |  |  |
| scripts_run_cause_api | scripts/archive/_run_cause_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _run_cause_api.py (2026-06-16) — run the focused cause-resolution API package and save the output. |  |  |  |
| scripts_run_gate1_onboard_batch_v1_20260706 | scripts/archive/_run_gate1_onboard_batch_v1_20260706.py | Gate-1 orphan onboarding orchestrator (Group C — clean adds to existing/new registries). |  |  |  |
| scripts_run_passa_via_api_v1_20260515 | scripts/archive/_run_passa_via_api_v1_20260515.py | Pass A meaning record via Claude API (cluster-agnostic). |  |  |  |
| scripts_run_proverbs_stage1_onboard_v1_20260712 | scripts/archive/_run_proverbs_stage1_onboard_v1_20260712.py | Proverbs Stage-1 onboarding (registry path) — the 30 candidate terms absent from |  |  |  |
| scripts_run_ve_reads_governed | scripts/archive/_run_ve_reads_governed.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _run_ve_reads_governed.py (2026-06-17) — governed corpus API read for ONE VE field. |  |  |  |
| scripts_schema_dump | scripts/archive/_schema_dump.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_search_prose | scripts/search_prose.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.search (Prose.ps1 -Step Search). Kept as the documented CLI entry point, reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_snapshot_db_v1_20260714 | scripts/archive/_snapshot_db_v1_20260714.py | Cadence-aware DB snapshot + prune helper (v1, 2026-07-14). |  |  |  |
| scripts_term_sharing_spider | scripts/archive/_term_sharing_spider.py | Generate term-sharing spider/network diagram showing pools of connected words. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_tmp_read_cycle2_rest | scripts/archive/_tmp_read_cycle2_rest.py | Build the remaining cycle-2 passage readings (Pro 1:24 - 2:3) via _pro_read_lib. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_tmp_read_cycle3 | scripts/archive/_tmp_read_cycle3.py | Build cycle-3 passage readings (Pro 2:4 - 2:20) via _pro_read_lib. Each in isolation. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_token_cost_history | scripts/archive/token_cost_history.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). token_cost_history.py — an auditable history of token consumption and estimated cost. |  |  |  |
| scripts_update_claude_code_instructions | scripts/archive/_update_claude_code_instructions.py | Update WA-SessionB-ClaudeCode-Instructions.md with all post-v5 changes. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_update_reference_doc | scripts/archive/_update_reference_doc.py | Update WA-Reference-v5.1 to v5.2 with new columns from housekeeping. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_update_registry_guide | scripts/archive/_update_registry_guide.py | Update Registry Management Guide with new fields, queries, and terminology. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_v3_2_l1 | scripts/archive/v3_2_l1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). v3_2_l1.py  — V3_2 Level 1 (verse establishment) command. |  |  |  |
| scripts_ve_engine_v2 | scripts/archive/_ve_engine_v2.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _ve_engine_v2.py (2026-06-16) — FIRST working build of the verse-lexical engine per 01b v2. |  |  |  |
| scripts_verify_soul | scripts/archive/verify_soul.py | Quick post-audit verification for soul (registry 182). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_verse_vertical_pass | scripts/archive/verse_vertical_pass.py | verse_vertical_pass.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_word_full_extract | scripts/archive/word_full_extract.py | CORRUPTED (pasted chat text after the SQL string, confirmed via tokenizer crash) -- escalation #701, never valid since its only commit 2026-03-19 |  |  |  |
| scripts_word_study_extract | scripts/archive/word_study_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). word_study_extract.py |  |  |  |
| seedreport | iba/app/lib/seedreport.py | seedreport.py — analysis of `candidate_seed`, one of the four "missing reports" from | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| session_close | iba/app/handlers/session_close.py | session_close.py -- session-close detection (#1875; rebuilt #2173 SC1-SC14): findings with stable keys, cleared only by a fix or a checked disposition; Session-Close.ps1 exits 3 while any is open. Remediation is Claude's via .claude/commands/session-close.md. | ✓ |  |  |
| session_routines_2173_v1_20261020 | iba/app/migration/session_routines_2173_v1_20261020.py | Developer Mode config migration for #2173/#2174 (this file). | ✓ | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| sessionwindow | iba/app/lib/sessionwindow.py | sessionwindow.py -- the running session, its start, git window and transcript; the last-session check at start (#2173 S6). Shared by start-up and session-close. | ✓ |  |  |
| simplify_M0_8_1_elevation_flag_v1_20260923 | iba/app/migration/archive/simplify_M0_8_1_elevation_flag_v1_20260923.py | ONE-OFF migration -- researcher instruction 2026-09-23 ('fix the solution for M0.8.1'): reworded from a formal elevation ruling to a plain attention flag; live evidence was 75% mismatched-tag usage on the old wording. Matching prompt paragraph in versereadinggenerate.py edited same unit of work. Run once, then set inactive=1. |  |  |  |
| snapshot_policy_text_v1_20261021 | iba/app/migration/archive/snapshot_policy_text_v1_20261021.py | ONE-OFF migration -- escalation #2193: corrects backup.pre_run_snapshot_policy to the backup-API snapshot, through configmaint.apply_logged under run_id DEVMODE-2193-SNAPSHOT-POLICY-TEXT-20261021. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| spanreport | iba/app/lib/spanreport.py | spanreport.py — analysis of the span layer (`span` + `span_candidate`), one of the four | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| spine | iba/app/handlers/spine.py | spine.py -- the base-data spine check (#1613; extended #2173 P3): span -> strong, verse <-> span, strong -> cluster, strong -> meaning against STEP. compute() is shared with session-close SC2. Read-only, always persists a report. | ✓ |  |  |
| split_lexical_meaning_word_relational_v1_20260923 | iba/app/migration/archive/split_lexical_meaning_word_relational_v1_20260923.py | ONE-OFF migration -- escalation #1860 (researcher approval v3): applies the config layer (cfg_step, cfg_write_grant, cfg_method_rule, cfg_setting) for the word-level/relational Stage 1 split. Narrows lexical.meaning to M0.1/M0.5 only; inserts lexical.relational (M0.6.5/M0.6.6/D7.7.1/M0.7/M0.8.1, ordinal 7); duplicates 9 cross-cutting method rules; moves the cluster.status transition rule; adds grounding + readiness-gate rules. Full design: iba/docs/1860-word-relational-split-build-plan-v1-20260923.md. Run 2026-09-23: applied clean. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| split_obs_catalogue_mechanical_interpretive_codes_v1_20260904 | iba/app/migration/archive/split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py | ONE-OFF migration, escalation #1444/#1383 -- splits 5 bundled wa_obs_question_catalogue codes (T0.1.2, T4.6.2, T4.6.3, T7.2.2, T1.4.1) each into a mechanical (Word/term lexical) + interpretive child pair, soft-deleting the old unified code. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| stage1coverage | iba/app/lib/stage1coverage.py | Deterministic expected-vs-actual coverage validation for Stage 1 (lexical.meaning + lexical.relational, escalation #1824 v14 / #1860). expected_nodes()/validate_coverage()/fully_covered_verse_ids()/missing_word_level_coverage() -- all read-only against live verse_lexical/ib_observation/ib_node state, never call an LLM. Caught live by configmaint.validate 2026-09-23 (pre-existing registration gap, unrelated to this files own content) while this file was being extended for the #1860 split -- registered now rather than left open. | ✓ | ✓ | legitimate zero, same shape as pathaudit.py: takes a pre-opened conn and reads live tables directly, resolves no cfg.setting()/cfg.enum() of its own -- its caller (handlers/lexical.py) is the one that reads lexical.* settings. |
| stepapi | iba/app/lib/stepapi.py | stepapi.py — the three STEP calls. Governed by config, fully. | ✓ |  |  |
| strand_items_2219_v1_20261022 | iba/app/migration/archive/strand_items_2219_v1_20261022.py | ONE-OFF migration -- escalation #2219 option A: reading_strand_item, reading_strand.thread_id, the strand steps' grants, the close gate on open items; run_id DEVMODE-2219-STRAND-ITEMS-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| strand_reading_enums_2172_v1_20261022 | iba/app/migration/archive/strand_reading_enums_2172_v1_20261022.py | ONE-OFF migration -- escalation #2172/#2215: enum values config_module strand_reading and check kind strand_account_clean; Tell/Untell step text; run_id DEVMODE-2172-STRAND-ENUMS-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| strand_reading_schema_2172_v1_20261022 | iba/app/migration/archive/strand_reading_schema_2172_v1_20261022.py | ONE-OFF migration -- escalation #2172 build step 1: ib_observation parts, claim source observation, reading_strand tables, tellings per block; run_id DEVMODE-2172-STRAND-SCHEMA-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| strand_reading_steps_2172_v1_20261022 | iba/app/migration/archive/strand_reading_steps_2172_v1_20261022.py | ONE-OFF migration -- escalation #2172: work package strand-reading, its steps, grants, reports and setting; the strand close gate; rule links; run_id DEVMODE-2172-STRAND-STEPS-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| strandreading | iba/app/lib/strandreading.py | strandreading.py -- the reading process (escalation #2172): define a strand, then context, record, gather, map, derive, rewrite and account; account_gaps() is the close gate. Observations through recordingpass, the narrative through narrativeregister. | ✓ |  |  |
| strongreconcile | iba/app/lib/strongreconcile.py | strong reconciliation utility | ✓ |  |  |
| strongreport | iba/app/lib/strongreport.py | strongreport.py — analysis of the meaning-parse layer (`strong` + `strong_lexicon` + | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| strongversereport | iba/app/lib/strongversereport.py | on-demand verse restatement, by ONE Strongs reference -- formalises the G2128/G2127 preview samples | ✓ | ✓ | receives cfg.conn from its caller; the one setting it reads (report.strong_verse_output_dir) belongs to module report, matching registryreport.py precedent |
| subgroupgenerate | iba/app/lib/subgroupgenerate.py | subgroupgenerate.py — the LLM-calling half of `cluster.subgroup` (process b, the `char-subgroup` | ✓ |  |  |
| taggingguidance | iba/app/lib/taggingguidance.py | taggingguidance.py -- the one shared source of ib_observation.tag definitions for every LLM-calling generator stage (escalation #1836); imported by four generators. | ✓ |  |  |
| threadaudit | iba/app/lib/threadaudit.py | threadaudit.py -- thread quality, validity and integrity (#2173 P5), T-a to T-g by item. | ✓ |  |  |
| utilities_2207_v1_20261022 | iba/app/migration/archive/utilities_2207_v1_20261022.py | ONE-OFF migration -- escalation #2207 item 2: batch monitoring and lexicalenrich retired, tag definitions into cfg_setting, through configmaint.apply_logged under run_id DEVMODE-2207-UTILITIES-20261022. inactive=1 once applied. |  | ✓ | one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations |
| validation | iba/app/validation.py | Word/book validation reports, called by handlers/reports.py. | ✓ | ✓ | app core, outside the utility config-density check |
| valuequality | iba/app/lib/valuequality.py | valuequality.py — the generic column-level VALUE-QUALITY engine. | ✓ |  |  |
| versemeta | iba/app/lib/versemeta.py | Write path for verse_meta.status (cfg_enum verse_meta_status: exclude/citated/analysed). Stamps status_changed_at only on an actual value change. Run as step verse_meta.set_status (handlers/versemeta.py) behind VerseMeta.ps1 (#2207). Escalation #1661. | ✓ |  |  |
| versereadinggenerate | iba/app/lib/versereadinggenerate.py | versereadinggenerate.py — the LLM-calling half of `lexical.meaning` (the `verse-reading` stage, | ✓ |  |  |
| versespanmeaningreport | iba/app/lib/versespanmeaningreport.py | versespanmeaningreport.py — the governed copy of `tools/build_verse_span_meaning_extract.py`'s | ✓ |  |  |
| wholebookread | iba/app/lib/wholebookread.py | wholebookread.py — registers the whole-book-read step (`report.whole_book_read`) as a real | ✓ |  |  |
| withdraw_stale_word_level_observations_v1_20260923 | iba/app/migration/archive/withdraw_stale_word_level_observations_v1_20260923.py | ONE-OFF migration -- escalation #1856: withdraws 4477 stale pre-fix word-level observations so normal reruns naturally re-derive them, per researcher's own decision (v3). Run once, then set inactive=1. |  |  |  |
| word_strong_span_report | iba/app/tools/archive/word_strong_span_report.py | SUPERSEDED 2026-08-09 (own module docstring) -- promoted the same day into a real registered report, WordRegistrySpan-Report.ps1 / report.word_registry_span / lib/wordregistryspanreport.py. Kept for history only, never registered until now (the gap path-audit escalation #971/#976 found: a hardcoded iba/app/db/iba.db default with zero cfg_utility row at all). Registered inactive rather than fixed, since fixing a hardcoded path in dead code is wasted effort -- use the live replacement instead. |  |  |  |
| wordregistryspanreport | iba/app/lib/archive/wordregistryspanreport.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). wordregistryspanreport.py — word_registry -> word_strong -> strong -> parse-meaning -> unique |  |  |  |
| words | iba/app/lib/words.py | words.py — registry word normalisation. Config-governed. | ✓ |  |  |

<a id="3-connection-step"></a>
## 3. Connection (STEP)

| key | value |
| --- | --- |
| base_url | http://localhost:8989 |
| timeout_seconds | 30 |
| version | ESV_th |

<a id="4-settings-every-rule-threshold-grouped-by-owning-module"></a>
## 4. Settings — every rule / threshold, grouped by owning module

_Every setting must have a module (enum.config_module) — configmaint.propose enforces this on every new row; see GOVERNANCE.md §5A._
| module | key | value | use |
| --- | --- | --- | --- |
| backup | backup.alerting_policy | NAS backup tasks alert on failure; Outlook SMTP is blocked from this network, alerting uses Gmail instead. |  |
| backup | backup.iba_db_gap | RESOLVED 2026-08-17 (escalation #703): iba.db now has its own dedicated NAS backup+alerting script -- scripts/backup_db_to_nas.py, generalized to serve both databases (filename prefix, pruning lineage, and alert job identity all derived from --source, not hardcoded), scheduled task "IBA DB Backup to NAS" (daily 18:10, staggered 10 min after bible_research.db's 18:00 task). Found and fixed while resolving this: a 2026-07-19 commit had accidentally repointed the shared script's DEFAULT_SOURCE to iba.db, so the 18:00 task had been backing up iba.db under misleading bible_research_-prefixed names for ~29 days, leaving bible_research.db with no dedicated integrity-checked backup in that window -- confirmed via NAS file-size comparison, not assumed. Restored + root-fixed (prefix now derived, not constant) so this class of accident cannot silently recur. |  |
| backup | backup.nas_db_backup | {'default_source': 'database/bible_research.db', 'target': '\\\\LSUK-SYNRACK\\HomeMedia\\bible_study_projects\\db_backups', 'log_name': 'backup_log.txt', 'status_dir': 'C:\\Users\\lerouxc\\nas_mirror_logs', 'keep_recent': 24, 'keep_daily': 30, 'keep_weekly': 26, 'min_bytes': {'bible_research': 10485760, 'iba': 419430400}, 'min_bytes_default': 10485760} | Settings of scripts/backup_db_to_nas.py: default source (project-relative), NAS target folder, NAS log file name, local status folder, the three retention tiers (keep_recent, keep_daily, keep_weekly) and the per-database size floor in bytes (min_bytes by source stem, min_bytes_default otherwise). If iba.db cannot be read the script uses its built-in copy of these values and says so in its log line. |
| backup | backup.nas_db_backup_schedule | database/bible_research.db backed up daily 18:00 (task 'BibleResearch DB Backup to NAS') and iba/app/db/iba.db daily 18:10 (task 'IBA DB Backup to NAS'), both by scripts/backup_db_to_nas.py, to \\LSUK-SYNRACK\HomeMedia\bible_study_projects\db_backups\. Each run integrity-checks, hash-verifies the NAS copy and refuses a source under its PER-DATABASE size floor (bible_research 10 MB, iba 400 MB; #2141, 2026-10-14 -- a single 50 MB floor had refused the prose-only bible_research.db since 2026-09-28). Tasks run in a hidden window (pwsh -WindowStyle Hidden) so closing a console cannot kill them (#2141); missed runs are not caught up (researcher, 2026-10-14). scripts/backup_watchdog.ps1 (daily 19:00 + logon) alerts on FAIL or >26 h staleness for mirror, dbbackup and dbbackup_iba. |  |
| backup | backup.nas_full_mirror_schedule | whole project folder + memory mirrored daily 18:30 (Windows scheduled task 'BibleResearch Full Mirror to NAS', scripts/mirror_to_nas.ps1, robocopy /MIR, run in a hidden window since #2141) to \\LSUK-SYNRACK\HomeMedia\bible_study_projects\mirror\ + claude-backup\. The mirror also carries a copy of both databases as files, without an integrity check; the integrity-checked, hash-verified DB backups are the separate 18:00 (bible_research.db) and 18:10 (iba.db) tasks -- see backup.nas_db_backup_schedule. |  |
| backup | backup.pre_run_snapshot_policy | a full DB snapshot (made with the SQLite backup API, lib/dbsnapshot.copy_db) is taken automatically before every NEW run (run.py:_ensure_run -> lib/dbsnapshot.snapshot()), never on resume -- this already covers every step in every pipeline; retention.snapshot_keep_count controls how many are kept (oldest pruned first). IBA_NO_SNAPSHOT=1 skips it for a tight loop. |  |
| backup | backup.write_atomicity_guarantee | every DB write happens inside one atomic transaction -- sqlite3 default deferred-transaction isolation, nothing commits until a handler's own single final commit(). A hard kill (power loss, session breakdown, process death) at any point before that commits NOTHING -- the DB file is left exactly as it was before the call started, and re-submitting the identical call is always safe. |  |
| behaviour | behaviour.list_report_path | outputs/configs/behaviour-rules-list.md | output path for Behaviour.ps1 -Action List / python -m iba.app.lib.behaviour list |
| behaviour | behaviour.study_state | on_hold | The study's state flag (cfg_enum study_state): 'active' delivers the study_active rules at start; 'on_hold' withholds them. Set only on the researcher's instruction; the ruling and reason are in governance.study_status. Escalation #2185. |
| behaviour | compliance.acknowledgement | I have read the governance settings, behaviour rules and escalation rules, and will comply with them. | #2173 P2 C: the sentence the compliance file must carry (checked) |
| behaviour | compliance.copy_min_words | 8 | #2173 P2 B: a restatement under this many words is not judged as a copy (a short line on the same subject shares most of its word runs with the rule without copying it) |
| behaviour | compliance.copy_share_max | 0.6 | #2173 P2 B: a restatement whose n-word runs occur in the rule text at this share or more is a copy, not a reading (a finding) |
| behaviour | compliance.copy_shingle_words | 3 | #2173 P2 B: n for the n-word runs used to tell a copied restatement from a reading |
| behaviour | compliance.dir | Logs/compliance/ | #2173 P2: folder of the session compliance files COMPLIANCE-<date>-<session8>.md |
| behaviour | compliance.engaged_statuses | ['engaged'] | #2173 P2 D: the statuses whose rows need evidence at close |
| behaviour | compliance.value_settings | ['governance.escalation_worksheet_path', 'governance.oneoff_report_archive_dir', 'governance.oneoff_report_dir', 'governance.oneoff_report_format', 'governance.oneoff_report_naming_pattern', 'governance.ps_worksheet_path', 'governance.scripts_ps_dir', 'governance.session_log_dir'] | #2206 option 3: governance settings holding a plain value (a path, a format), read by the code that uses them; lib/compliance.py leaves them out of the delivered rules and the compliance file |
| candidate | candidate.concept_delimiter_pattern | [:/] | a character in a candidate.load input word signalling more than one concept -- split into one sub-item per piece before validating, rather than reject or guess which half is right |
| candidate | candidate.lemma_base_pattern | ^([HG]\d+)([A-Z]?)$ | capture group 1 = the base Strong's (sub-letters stripped) — the lemma key. The seed/stamp key on this. |
| candidate | candidate.load_report_path | iba/app/reports/candidate-load.md | where candidate.load persists its per-run duplicates/exceptions report |
| candidate | candidate.quality_report_path | iba/app/reports/candidate-quality.md | where candidate.validate persists its findings |
| candidate | candidate.tag_clean_pattern | ^[A-Za-z][A-Za-z' -]*$ | a clean candidate_tag: letters/spaces/hyphens/apostrophe only — no parenthetical transliteration, punctuation, or multi-clause gloss text |
| candidate | candidate.tag_max_words | 5 | a candidate.load input word/tag longer than this many space-separated tokens is treated as a sentence, not a concept, and written as an exception row |
| candidate | candidate.transliteration_pattern | ^[a-z]+'[a-z]+$ | STARTER heuristic, tune via configmaint.propose as real cases are seen: a bare lowercase token with no space is a plausible transliteration (e.g. 'asah', 'halak') and gets written as an exception for a human read, not silently accepted -- it cannot distinguish a genuine single-word English gloss ('hearing') from a transliteration by shape alone, so this is a conservative flag-for-review test, not a hard linguistic classifier |
| cluster | cluster.assign.exclude_flag_gloss_from_voting | True | the cluster-allocation session pitfall: cluster.csv FLAG gloss list is an uncertainty bag, never a positive P2 precedent-match signal |
| cluster | cluster.assign.word_optional_clusters | ['T2', 'T3'] | cluster codes exempt from the needs-a-word_registry-link rule (Q2.4.1 exception 1) -- researcher correction 2026-08-12: a word generates the verse, it does not need to own every strong later found in it; T3 is inherently not word-specific |
| cluster | cluster.quality_report_path | _analytics/Clusters/cluster-assign.md | report path for cluster.validate, same convention as lexicon.quality_report_path |
| cluster | cluster.recording_similarity_threshold | 0.85 | recordingpass.py record_one_observation: obs_text similarity score (0-1, difflib SequenceMatcher) above which a same-coordinate new observation is treated as a superficial edit of an existing one (align in place) rather than a genuine broaden (new row). Was a hardcoded module constant with no live tuning; promoted to cfg_setting per escalation #1753/#1761 precedent. |
| cluster | ib_observation.meaning_source_aliases | {'char_reading_observations': 'observations', 'char_subgroup_observations': 'observations', 'cluster.cluster_code': 'cluster', 'cluster_codes': 'cluster', 'context': 'verse-text', 'lexicon': 'strong_lexicon', 'lexicon.lsj': 'strong_lexicon.lsj', 'lexicon.mounce': 'strong_lexicon.mounce', 'lsj': 'strong_lexicon.lsj', 'lsj cross-reference': 'strong_lexicon.lsj', 'm0.5': 'cluster', 'morph data': 'verse-text', 'mounce': 'strong_lexicon.mounce', 'role list': 'role-tags', 'role tags': 'role-tags', 'role-context': 'role-tags', 'role-tag context': 'role-tags', 'role-tag reading': 'role-tags', 'roles_in_verse': 'role-tags', 'text': 'verse-text', 'verse': 'verse-text', 'verse_reading_observations': 'observations'} | #2207: each spelling the model has used for a meaning source, mapped to its value in cfg_enum ib_observation.meaning_source; lib/recordingpass.normalise_meaning_source applies it to every new observation |
| cluster | ib_observation.tag_guidance | {'qualifier-for-term': 'the word functions as a MODIFIER (manner, intensifier, or other state/measure/intensity enhancer) of another word\'s action or quality, rather than naming a disposition/operation/quality in its own right -- e.g. an adverb qualifying HOW an operation is performed, or an adjective qualifying another M-code noun ("godly" qualifying "grief").', 'no-impact': "the occurrence's surface form/stepGloss carries no distinguishing nuance beyond the term's base sense -- a real 'no divergence' finding, not an absence of an answer. Contrast `alternative-meaning` (a real divergence IS found) and `surface-gloss-divergence` (the surface FORM itself, not just the sense, diverges from the dictionary gloss).", 'not-related-to-meaningful-word': "the sub-question's target item (a contrast, a related word-form, a co-occurring item the question asks you to identify) genuinely does not exist or apply for this term/verse -- a real negative finding, not a shrug.", 'sole-mcode-in-verse': 'no other M-code characteristic co-occurs in this verse at all -- distinct from `no-direct-connection`, which means other M-codes ARE present but unrelated to this one.', 'tightly-related': "this term's own role connects SUBSTANTIVELY to another M-code term present in the same scope -- a real causal/enabling/response/tension link, or the two share the same acting party -- not just topical co-presence in the same list or catalogue.", 'no-direct-connection': "other M-code term(s) ARE present in this scope, but this term's own role does not meaningfully connect to them (no causal link, no shared party, no real interaction) -- distinct from `sole-mcode-in-verse`, where nothing else is present to connect to at all.", 'cluster-pole-negative': 'this term occupies the negative/negligent pole of a dual-natured cluster (e.g. idleness within a sloth-vs-diligence cluster).', 'cluster-pole-positive': 'this term occupies the positive/virtuous pole of a dual-natured cluster (e.g. diligence/zeal within a sloth-vs-diligence cluster).', 'attested-pre-nt': 'the term is attested in classical/pre-NT Greek or Hebrew usage, not coined in the NT period.', 'nt-coinage': 'the term (or this specific sense of it) has no attestation before the NT -- a NT-period coinage or semantic innovation.', 'alternative-meaning': "this SPECIFIC occurrence genuinely supports MORE THAN ONE plausible reading/sense, and the data does not clearly settle which -- real ambiguity, not just a divergence from the usual sense (that's `surface-gloss-divergence` when it's the FORM, or a plain substantive answer when the sense is clear but simply different from elsewhere). State both/all candidate readings in `obs_text`, not just one.", 'surface-gloss-divergence': "this occurrence's actual surface form (`span.surface`, the inflected text as it appears) diverges from its `stepGloss` dictionary-standard rendering in a way worth noting -- a form-level fact (e.g. an idiomatic rendering, a metaphorical extension the standard gloss doesn't capture), not a claim of multiple valid readings (`alternative-meaning`).", 'no-human-context': "this strong is exclusively a homonym or proper name with no meaningful context for a human reader to analyse -- earmark it as such and stop; do not force an analysis where none is genuinely available (cfg_method_rule 'homonym-no-context-earmarked-and-left').", 'data-error': "a data-quality issue noticed while reading (wrong cluster/subgroup membership, a broken span/verse link, a corrupted meaning source) -- flag it here, in its own section; never chase it down or fix it as part of this task (cfg_method_rule 'data-errors-flagged-separately').", 'verse-grouping': "several of THIS strong's own occurrences, across different verses, share one genuinely alike reading -- group them under one finding rather than repeating the same point per verse. Requires visibility across a strong's full occurrence set; not meaningful at a single-verse grain.", 'difference-inference': "a specific inference or distinction drawn from comparing THIS strong's own occurrences against EACH OTHER (morph-driven distinctions included -- e.g. whether a stem/voice variation across occurrences is meaning-relevant). Requires visibility across a strong's full occurrence set; not meaningful at a single-verse grain.", 'could-not-resolve': "a genuine 'couldn't resolve' case -- state in `obs_text` what signal suggests it should be resolvable with further analysis, never a bare flag with no reason.", 'needs_adjacent_verse_context': "this verse's own content is insufficient and an adjacent/surrounding verse would help -- state explicitly in `obs_text` what's outstanding and what the follow-up cross-check needs to establish. Resolution happens in a later analytic pass, never fetched ad hoc here.", 'elevation-candidate': "this T2/T3-tagged (non-M-code) word's role in THIS verse suggests it names a distinct inner-being characteristic in its own right, not just a supporting role -- state the reason in `obs_text` (M0.8.1 only; escalation #1836). A later, separate process reviews elevation candidates for actual cluster promotion -- this tag only surfaces the candidate, it does not itself change any cluster/role assignment.", 'answered-no-flag': 'a genuinely plain, substantive answer that matches none of the other tags and has nothing else worth categorising (e.g. a straightforward root-meaning or primary-term identification) -- a LAST RESORT, not a default. Check every observation against the other tags above before reaching for this one.'} | #2207: the definition of each ib_observation.tag value, given to the model by every LLM-calling generator stage (lib/taggingguidance.guidance_block). A tag in cfg_enum ib_observation.tag with no definition here is not offered to any stage. |
| cluster | ib_observation.tag_stage_excluded | {'verse-reading': ['difference-inference', 'verse-grouping'], 'char-subgroup': [], 'char-reading': [], 'char-answers': []} | #2207: per generator stage, the tags it may not offer (lib/taggingguidance.tags_for_stage). verse-reading sees one verse at a time, so the cross-occurrence tags are excluded there. |
| configmaint | configmaint.auto_report | True | whether an approved configmaint.propose automatically chains to configmaint.report |
| configmaint | configmaint.csv_export_dir | workflow/schema | folder for the per-cfg_*-table CSV pairing that accompanies CONFIG-REPORT.md (reportkit.write_csv_pairing) -- independently repointable, no longer hardcoded as a sibling of configmaint.report_path |
| configmaint | configmaint.csv_export_on_auto_report | 0 | whether the auto-triggered post-propose/validate CONFIG-REPORT.md regeneration also writes the CSV table-pairing side-output (default off). An explicit -Step Report run always writes it regardless of this flag. Escalation #1314. |
| configmaint | configmaint.report_path | outputs/configs/CONFIG-REPORT.md | where configmaint.report writes the snapshot |
| content_index | content_index.exclude_size_threshold_bytes | 52428800 | a .md file this size or larger (bytes; default 50MB) is excluded from content_index.rebuild/.refresh by default, unless it matches an active cfg_content_index_size_override pattern |
| content_index | content_index.report_path | outputs/content_index/content-index-rebuild.md | where content_index.rebuild writes its summary report |
| content_index | content_index.size_profile_report_path | outputs/content_index/content-index-size-profile.md | where content_index.size_profile writes its .md-file-size report |
| database | database.bible_research.path | database/bible_research.db | bible_research.db's file path, project-root-relative (aka research_db in prose elsewhere -- that alias isn't repeated here, see governance.project_databases). Structured counterpart, escalation #723. |
| database | database.iba.path | iba/app/db/iba.db | iba.db's file path, project-root-relative -- structured counterpart to governance.project_databases' prose, part of escalation #723's project_database enum + path settings. |
| escalation | escalation.context_file_extensions | ['.md', '.csv', '.py', '.ps1', '.json', '.xlsx', '.txt', '.sql', '.html', '.jsonl'] | #2173 P1: the extensions that mark a file reference in escalation text |
| escalation | escalation.context_report_path | outputs/escalation/escalation-context.md | #2173 P1: report of every file each open escalation names, resolved to its latest live version (Escalation.ps1 -Action Context; lib/escalationcontext.py) |
| escalation | escalation.control_objectives | the escalation table manages all open items, irrespective of source or reason -- AI or researcher raise the escalation when discovered or raised, using the escalation module |  |
| escalation | escalation.control_process | escalations are raised, processed, and completed using the escalation utility module |  |
| escalation | escalation.history_report_dir | outputs/escalation |  |
| escalation | escalation.list_report_path | outputs/escalation/escalation-list.md |  |
| escalation | escalation.thread_audit_report_path | outputs/escalation/escalation-thread-audit.md | #2173 P5: thread audit report (Escalation.ps1 -Action ThreadAudit; lib/threadaudit.py) |
| escalation | escalation.thread_register_path | _analytics/cross-cluster-web/open-threads-register.md | the generated open threads register (Escalation.ps1 -Action Export -Type thread; regenerated at session-close) -- same path as the hand-kept register it replaces (escalation #2000, decision 3) |
| escalation | escalation.thread_report_path | outputs/escalation/escalation-threads.md | where Escalation.ps1 -Action Thread writes the open threads report (escalation #2000) |
| escalation | escalation.worked_strand_escalations | {'M01': [1962], 'M02': [1963], 'M25': [1932], 'M47': [1911, 2172], 'M64': [1978, 1986], 'M18': [1993], 'M72': [1998], 'M09': [2148], 'M08': [2156], 'M07': [2171]} | #2173 P5 T-d: per cluster, the escalations that carry its strand. A strand counts as worked only when every listed escalation is completed (read from state at audit time, never from memory); M47 lists #2172, so it is not worked while #2172 is open. Add a cluster here when its strand escalation is raised. |
| governance | governance.User_Guide_scope | The user guide must reflect the latest state of all the tools and details on the use of the tools, geared towards user interaction for the entire project. |  |
| governance | governance.base_data_spine | verse-span-strong-cluster-must-sync: every strong occurring in a live span must resolve, through cluster_strong, to a live cluster -- not merely to a live strong row. A strong with zero live cluster_strong allocation is a spine failure (FATAL), not a lexical-build-specific precondition. | The base-data spine, researcher ruling 2026-09-10 (escalation #1613 audit, iba/docs/1613-meaning-layer-config-inventory-v1-20260909.md section17): verse defines what is INCLUDED in the study; span defines HOW meaning is derived from the verse text; strong defines WHAT the meaning IS -- the operative anchor. These three must be in sync at all times; a discovered desync (e.g. a span-referenced code with no live strong row) is a FATAL ERROR, fixed on discovery, not merely logged. strong is the main operative: extended meaning is pulled from language-specific repositories (Hebrew+Greek: strong_meaning_tree/strong_meaning_parsed; Greek-only: strong_lexicon/strong_lsj_parsed/strong_mounce_parsed) and these must be absolutely in sync by language. Missing extended meaning is an ACCEPTED, non-fatal anomaly ONLY when explained by classification (T2/T3-T15/backfill -- see method rule spine-extended-meaning-accepted-anomaly), pulled on demand as analysis needs it, not proactively for every strong. Parse (strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed) makes extended meaning digestible: every strong with extended meaning pulled MUST have a parse row; a break here is a FATAL ERROR, fixed on discovery. Once the spine is sound, verse-strong-parse is the whole route for meaning-in-context during analysis; if a term becomes significant during analysis and its parse is missing, pull it through on demand. Diagnosis: existing base-data incompleteness/errors trace to mismanagement of this spine, not unrelated bugs. Adjusted 2026-09-10 (escalations #1622-1624): discovery of a missing meaning/parse entry must TRIGGER its update at the point of discovery, not merely be logged for later. |
| governance | governance.behaviour_boundary.backup_recovery | Backup/recovery and data-durability discipline is classified under the `sqlite` behaviour class (database-interaction discipline), not a separate class -- ensuring a write is replayable/captured is a database-state concern. Content: cfg_behaviour_rule (sqlite, writes-must-be-replayable). | boundary decision -- backup/durability class placement, escalation #715 cycle 3 |
| governance | governance.behaviour_boundary.git_commit | Git/commit discipline is classified under the `terminal` behaviour class (command/script-execution discipline), not a separate class -- committing and pushing is itself a terminal operation with a definable 'done' state. Content: cfg_behaviour_rule (terminal, git-commit-and-push-together). | boundary decision -- git/commit class placement, escalation #715 cycle 3 |
| governance | governance.build_md_on_code_change | any code change under iba/app/** must update iba/app/BUILD.md in the same unit of work — BUILD.md is the build record, not a one-time snapshot | researcher ruling 2026-07-22: BUILD.md/GOVERNANCE.md must stay current, not just be written once |
| governance | governance.config_control | every configuration entry in any cfg_* table is controlled by the cfg.configmaint rules |  |
| governance | governance.confmaint_configs | all the rules that govern the maintenance operations of the configs are set in cfg_* under the configmaint module |  |
| governance | governance.engineering_documentation_folder | iba/docs/ is the home for IBA-side engineering and design notes not tied to one escalation (cfg_control_home kind engineering_note). An escalation's own deliverable goes under outputs/escalation/ (rule 60). | boundary/location decision -- engineering documentation folder, escalation #732 cycle 4 |
| governance | governance.escalation.scope | all open items, discovery of anomalies, clarifications and other forms of escalation must be recorded in escalation using escalation rules |  |
| governance | governance.escalation_worksheet_path | iba/docs/escalation actions worksheet.xlsx | the researchers own model worksheet, checked by configmaint.validate (find_escalation_worksheet_drift) -- every live Escalation.ps1 parameter must appear as a -Flag header somewhere in it |
| governance | governance.governance_md_on_rule_change | A change to how config governs the code (a new kind of config table, a new change path, a new check, a new session routine) updates GOVERNANCE.md's current description in the same unit of work, and its change record goes to BUILD.md. A single rule or setting change is set in cfg_* (configmaint.propose, or apply_logged in Developer Mode) and recorded in cfg_change_detail; it needs no GOVERNANCE.md entry. GOVERNANCE.md never holds a rule the config does not. | researcher ruling 2026-07-22: no rule should exist only in GOVERNANCE.md; the config is the source of truth, GOVERNANCE.md is the overview of it |
| governance | governance.module.config | each operating module must have a config table (or tables) in the cfg_* series to control all aspects of the module's operation |  |
| governance | governance.module_utility_test_plan | From now on, case-by-case as development happens (not retrofitted): every module/utility design must include a test plan covering all its meaningful interaction/parameter/option combinations; the test plan is kept current (updated in the same unit of work whenever the functional component changes); it is RUN after the approved design is built, as a required stage of the existing plan/propose/design -> approve -> build -> approve cycle; and its actual results are included in the build's escalation resolution, not just asserted. Full rationale and origin: cfg_behaviour_rule (development/test-plan-per-module-utility). | Read explicitly every session by init.py's governance-rules printout (Start-Iba.ps1) -- the only real enforcement a process rule like this has. Applies project-wide, not IBA-only, same as governance.operational_behaviour_control. |
| governance | governance.narrative_home | The inner-being narrative is kept in iba.db with its claims: each chapter as blocks (narrative_section.block_text, a heading and its text) and each claim told by a block (narrative_claim_telling). The chapter files in narrative.copy_source_dir are exports written from the database; the narrative is written through Strand-Reading.ps1 -Step Rewrite and the block actions of Narrative-Register.ps1, never in a chapter file. bible_research.db prose_section keeps the programme and glossary prose, which stay live. | researcher 2026-10-22 on escalation #2172 (reading process design v2, option B, approved: "sounds good to proceed with the build"; prose_section's programme and glossary prose are not dead) |
| governance | governance.new_utility_registration_timing | Any new script or routine, anywhere in the project, must be registered in cfg_utility (and cfg_step/cfg_write_grant if it writes data) in the same unit of work it is created -- operationalizes governance.scripts_and_routines with a timing rule and a real enforcement check (configmaint.validate: find_unregistered_project_scripts). |  |
| governance | governance.no_direct_github_publish | Bible_study_projects never publishes to GitHub itself (no Actions workflow, no push to a site repo). Narrative files reach learning4comfort only by Copy-NarrativeToLearning4Comfort.ps1, run on completion of a section of work, on request, and at /session-close when a chapter changed in the session (SC12). | Escalation #1941, researcher verbatim 2026-10-04: "A) this project (bible_study_projects) does not publish directly to github b) on completion of a section of work or on request, the current ...inner-being-narrative files are copied to C:\\learning4comfort\\publication-inbox\\... c) session-close trigger the copy in b)". See CLAUDE.md section 12 and GOVERNANCE.md. |
| governance | governance.oneoff_report_archive_dir | archive | archive subfolder (relative to governance.oneoff_report_dir) that oneoff_path() moves a superseded one-off report version into before writing the next one -- same shape as write_report/cfg_report.archive_dir, added 2026-08-08 (BUILD.md sec83) once oneoff_path was found to have versioned without ever archiving. |
| governance | governance.oneoff_report_dir | outputs/ | folder for one-off/investigatory reports — read by lib/reportkit.oneoff_path() |
| governance | governance.oneoff_report_format | md | default file extension for one-off reports |
| governance | governance.oneoff_report_naming_pattern | {topic}-{YYYYMMDD}.{format} | filename pattern for one-off reports ({topic}/{YYYYMMDD}/{format} substituted); same-day collisions get -v2/-v3/... appended by oneoff_path() itself |
| governance | governance.operational_behaviour_control | Project operational behaviour is governed by cfg_behaviour_class + cfg_behaviour_rule, one class per kind of behaviour (the classes in cfg_behaviour_class) -- scope is the whole project, not iba/app/** only. A rule lives in exactly one place: once captured here, its document version is replaced with a pointer, never left standing alongside it. Where a class boundary is unclear, the boundary is defined explicitly as a governance.behaviour_boundary.<topic> setting rather than left implicit. | entry-point anchor for the operational-behaviour cfg layer -- part (a) of escalation #715 |
| governance | governance.past_precedent_investigation_signals_missing_config | If executing an already-registered standard instruction (a cfg_work_package/cfg_step routine) requires FIRST INVESTIGATING HOW IT WAS DONE IN THE PAST -- reading BUILD.md/session-log history, diffing prior/archived output files, or otherwise reverse-engineering a missing step from precedent -- rather than being told directly by a live cfg_step/cfg_setting row what to run and what rules apply, that investigation is itself the signal that a required config/mechanism is MISSING, not a puzzle to solve from precedent. STOP the instruction immediately the moment this is recognised -- do not proceed by reconstructing the missing rule from historical output and presenting it as the standard process. The gap must be closed first: the missing step/setting registered in cfg_* and its code built (governance.build_md_on_code_change/governance.governance_md_on_rule_change both apply), config validated clean, and only then may the original instruction be resubmitted. | researcher ruling 2026-07-30: a live session investigated BUILD.md history and archived output files to infer an undocumented passage.debate_status filled transition (report.passage_debate has no registered mechanism for marking a manually-filled scaffold complete) instead of finding that transition in cfg_step/cfg_setting -- doc/output archaeology substituting for a missing config is exactly the inconsistency pattern blamed for this study lacking repeatable results over its 7-month history |
| governance | governance.primary_responsibility | Claude is responsible for the coding of, and maintenance of the integrity to ensure that all project operations are coded, controlled and maintained in the IBA application. This includes back-filling operations currently outside the application. |  |
| governance | governance.procedural_document_taxonomy | A procedural document (going forward) is exactly one of: (a) planning/investigatory -- plans, explorations, decision docs; (b) config-extract -- generated (not hand-authored) from cfg_* for easier digesting, e.g. CONFIG-REPORT.md, cfg-rules-overview-*; (c) history-of-changes -- BUILD.md-shaped change records, arguably DB/engine-resident rather than a document long-term; (d) guidance/baseline instructions -- GOVERNANCE.md, USER-GUIDE.md, CLAUDE.md-shaped. Researcher's own framing, 2026-08-18 (comments-operational-behaviour-plan). Applying this taxonomy to the full existing document set is not done here -- a follow-on cycle. | the 4-way procedural-document taxonomy named directly by the researcher, escalation #715 cycle 3 -- applying it to the existing document set is deferred to a follow-on cycle |
| governance | governance.programme_stages | The research programme has three main stages: Base_data (STEP through lexical); Analysis (deriving understanding of the inner being); Publishing (essays and output for the results). Previously referred to as Session A (base data), Session B/D (analytics), Session C (publishing) -- methodologies and processes have changed materially over time across all three. |  |
| governance | governance.project_change_rule | Any change of operations, methodologies or approach must channel through the IBA App. Any operation defined in the past that is not in the IBA app must be migrated to the app. |  |
| governance | governance.project_databases | bible_research.db (aka research_db) lives in database/; iba.db lives in iba/app/db/ -- both paths are project-root-relative |  |
| governance | governance.project_lookups_and_naming_convensions | Project-specific naming in lookups, stages, and terms with specific meaning must be defined in cfg_enum (see cfg_setting naming.*). Terminology must be checked whenever an operation is executed to ensure it is used in accordance with its definition; a missing definition must be escalated. |  |
| governance | governance.project_operations | A project operation is any activity to perform research, development, exploration, investigation, or running scripts related to achieving the project objectives. |  |
| governance | governance.prose_canonical_authority | The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about. cfg_prose_concept points a key project concept (e.g. verse primacy, the inner-being definition) at the prose section that defines it, rather than restating the definition as a separate rule. Chapter-level review status is not tracked in cfg_*: it lives in prose_section.status (cfg_enum prose_section_status), set per section via Prose.ps1 -Step SetStatus, rolled up per chapter via prose_section_type.chapter_no. A methodology/approach change that touches a concept named in cfg_prose_concept should flag whether the prose needs updating (the flagging mechanism is a deferred build; this setting states the principle only). | entry-point anchor for the prose-as-canonical-authority work -- part (a) of escalation #714 |
| governance | governance.ps_worksheet_path | iba/docs/ps tools worksheet.xlsx | the ps-tools worksheet checked by configmaint.validate (find_ps_worksheet_drift) against every iba/app/ps/*.ps1 script live param() list |
| governance | governance.ps_worksheet_sync_on_change | any change to a PS scripts declared parameters (added, removed, or renamed) under iba/app/ps/** must be reflected in the same unit of work in iba/docs/ps tools worksheet.xlsx (its own tab), and for Escalation.ps1 specifically also in iba/docs/escalation actions worksheet.xlsx (the researchers model sheet) -- enforced by configmaint.validate (find_ps_worksheet_drift, find_escalation_worksheet_drift), not just stated | researcher ruling 2026-08-29: the two Excel worksheets are the live CLI interface to iba/app/ps and must not silently drift from the scripts they describe |
| governance | governance.redundancy_archiving | One-off reports, scripts, or other artifacts no longer in use or relevant must be archived on a daily basis. |  |
| governance | governance.reports_must_persist | every quality-check or report-producing step must persist its output to a config-defined report path — a terminal print + an escalation row is not sufficient; enforced by lib/cfgquality.find_missing_report_paths, checked in configmaint.validate | the researcher's 2026-07-21 standard: deviations are bugs, not judgement calls — fix, don't ask |
| governance | governance.rules_must_be_config_driven | no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or memory without a referenced cfg_* row recording it as the evidence that the configuration control is in operation. Any deviation discovered requires escalation. On a new instruction, the first thing to establish is that the rules governing the instruction are fully captured and interpreted correctly in the configs -- if not, it requires escalation. | the researchers 2026-07-26 standard, raised after an unconfigured rule (STEP required) was silently violated |
| governance | governance.scope_iba_app | IBA App is the central process control mechanism for all operations in the entire project |  |
| governance | governance.scope_iba_db | The iba_db is the home for all project process control and base data, including all related tables from STEP through Strongs, verses, meaning, and lexicals. It is now primary for all processes and base data; a few analysis tables (debate/passage control) are expected to migrate back to research_db. |  |
| governance | governance.scope_project | the config's scope is the entire project, with all of its parts, not a sub-section of the project |  |
| governance | governance.scope_research_db | bible_research.db (research_db) is prose-only -- the canonical, foundational authority on the programme's own governing concepts (governance.prose_canonical_authority). Findings/observations are fully owned by iba.db's ib_observation/ib_node pipeline; the old finding/analysis/legacy-cluster tables in bible_research.db are inactive, not a live parallel store. |  |
| governance | governance.scripts_and_routines | All scripts and routines must belong to a module, utility, library, or be a temporary script. Temporary scripts must be prefixed with temp_. |  |
| governance | governance.scripts_ps_dir | iba/app/ps |  |
| governance | governance.scripts_python_dir | iba/app/tools |  |
| governance | governance.session_log_dir | Logs/ | where every SESSION-LOG-*.md narrative work-session record lives -- consolidated 2026-08-17 (escalation #682) from 5 scattered locations (iba/logs/, outputs/session-logs/, Workflow/Sessionlogs/, repo root) into this one, case-insensitive-filesystem-safe existing folder. |
| governance | governance.session_log_required_content | Every session has a session log in governance.session_log_dir (SESSION-LOG-<date>-<topic>.md) naming the session id and carrying six sections, headed as in session_close.log_sections: (1) date and a one-line scope summary of the session; (2) every escalation touched, by id, with its outcome (raised/updated/resolved/rejected) -- the actual ids, not narrative paraphrase; (3) every file or deliverable created or changed, with its path; (4) decisions made, distinguishing the researcher's own decisions from self_correctable fixes Claude made and closed, each naming where it was recorded (a file path, a cfg_* table, or #nnnn vN) -- checked by session-close SC9; (5) open items carried into the next session -- what is left, and for whom, by OT-nn.n or #nnnn; (6) the git state of the session's commit (governance.session_log_triggers_commit): branch, commit hash and the push output, from the actual git output, written after the first commit and committed alone. A log missing any of these is incomplete; session-close (SC8) fails without it. | Answers escalation #911 (2026-08-27): the content a session log must carry, previously unstated anywhere in cfg_* or governance prose -- only governance.session_log_dir (where) and governance.session_log_triggers_commit (the commit consequence) existed. Derived from the log's own stated purpose (continuity across sessions) and the existing patch/escalation convention of naming ids and files explicitly rather than narrating them, not from reading prior logs for precedent (governance.past_precedent_investigation_signals_missing_config). |
| governance | governance.session_log_triggers_commit | A /session-close cycle (.claude/commands/session-close.md) includes writing the session's log (governance.session_log_required_content) and ends in the full commit-and-push cycle in the same unit of work: the log is written, Session-Close.ps1 shows no open finding, everything outstanding is staged and committed with a proper message and pushed, then the log's git section (item 6) is written and committed alone ('session log git confirmation') and pushed; confirm clean/pushed from the actual git output. |  |
| governance | governance.study_status | ON HOLD since 2026-10-22. Researcher, verbatim: 'I am again placing the study on hold because you are not ready and did not build the code as expected.' No study work (readings, weaves, strands, audits) is started, continued or proposed until the researcher re-opens it. Reason: escalation #2228 (the reading process forces a whole-strand rebuild for any subset, does not start from work already done, and cannot take its scope from the request); it is to be broken down and fixed in a Developer Mode session first. | Whether the study is active or on hold, and why. Read at session start (module governance). Changed only on the researcher's instruction. Moved from the CLAUDE.md banner 2026-10-21 (escalation #2181). |
| governance | governance.table_columns | each column in each table in the project must be listed in cfg_column with a proper use text. This applies to all databases and all tables. Updating a column in any routine must validate the use of the column against this config. Deviation from the rules must be escalated. |  |
| governance | governance.tables | each table in the project must be listed in cfg_table with a proper use text. This applies to all databases. Tables no longer in use must be set as inactive. |  |
| governance | governance.utility.config | each utility must have its own config table in the cfg_* series to control all aspects of the utility |  |
| governance | governance.verse_gap_by_design | A verse missing from iba.db's verse table (no `verse` row for that osisId) is BY DESIGN, not a data-integrity error. Verse-existence is gated on prior term discovery (concordance-driven per-Strong's onboarding, iba/app/handlers/raw.py:verses) -- do not escalate, flag, or attempt to backfill a missing verse as a bug. Extent measured 2026-07-29: 2,049/31,086 verses (6.59%) missing, concentrated in genealogy/list-heavy books (1Chr 44%, Ezra 40%, Neh 31%, Josh 23%, Num 17%); a sample read of the missing verses judged the risk within tolerance for this study (iba/app/reports/verse-existence-census-20260729.md). The spine check never looks for a missing verse. | researcher ruling 2026-07-29, after measuring the full-Bible extent of the term-discovery verse gap (see project_iba_verse_existence_gated_on_term_discovery memory + iba/app/reports/verse-existence-census-20260729.md) |
| governance | narrative.inner_being_style_guide_path | Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md | Authoritative style, format and evidence guide for all IBA-line reader-facing narrative (inner-being narrative chapters, strand write-ups, book narratives). Consolidates the 2026-04..07 prose/essay/narrative guides with the researcher rulings to 2026-10-01: first-person voice, weave not fit, change of character, let Scripture speak for itself, prose supported by bullets, titles name the subject only, external parties dealt with per phenomenon (#1921, #1924). Read before writing or revising any narrative text. |
| governance | registry.folder_naming_convention | _analytics/registry/word_registry per-word subfolders (report.strong_verse_output_dir) must be named {word_registry.id zero-padded 3 digits}_{word, lowercase, spaces as hyphens} -- e.g. 020_compassion. id comes from the LIVE iba.db word_registry table, never bible_research.db's legacy numbering (the two differ). | the folder-naming rule for per-word registry output, so it stays config-governed rather than a one-off manual cleanup that can silently drift again |
| governance | report.book_folder_naming_convention | _analytics/Bible_Books subfolders (report.verse_analysis_output_dir and every book-scoped report) must be named EXACTLY as cfg_book_order.book (the OSIS abbreviation verse.osisId itself uses, e.g. Gen, 1Chr, Song) -- never a full book name or a lowercase variant. | the folder-naming rule for per-book output, keyed to the same book identifier verse references use, so there is no mis-filing risk working with verse references |
| governance | report.cluster_folder_naming_convention | _analytics/Clusters holds one subfolder for EVERY row of cluster (deleted=0) -- M-, T- and FLAG codes alike; a folder is created whenever a cluster row is added. ALL output relating to a cluster (analysis, readings, handoffs, inputs/extract CSVs, decisions) is filed in that cluster's subfolder, prior versions in its archive/ subfolder. Name = {cluster.cluster_code} - {cluster.short_name lowercased, & and all other punctuation dropped, spaces as single hyphens} -- e.g. M02 - anger-wrath, M47 - inner-seat, M81 - memory-act, T7 - party-divine. Cross-cluster/all-cluster files (report.cluster_path, cluster.quality_report_path) stay at the _analytics/Clusters root. Single-cluster verse analysis -- including a fan-out strand, unit ledgers, cross-ledger overviews and proposals that read one cluster's vocabulary -- is filed in that cluster's subfolder, never in _analytics/cross-cluster-web/. Only TRUE multi-cluster work (a strand whose subject spans clusters, such as origin-of-thought, or the cross-cluster analyses) is filed in _analytics/cross-cluster-web/. | the filing rule for all per-cluster output: one subfolder per cluster under _analytics/Clusters, keyed to cluster.cluster_code, so cluster work never drifts into outputs/ or research/ |
| lexical | lexical.llm_api_url | https://api.anthropic.com/v1/messages |  |
| lexical | lexical.llm_api_version | 2023-06-01 |  |
| lexical | lexical.llm_chars_per_token | 4 |  |
| lexical | lexical.llm_max_cost_per_batch | 1.0 |  |
| lexical | lexical.llm_max_output_tokens | 40000 |  |
| lexical | lexical.llm_model | claude-sonnet-5 |  |
| lexical | lexical.llm_rate_input_per_million | 3.0 |  |
| lexical | lexical.llm_rate_output_per_million | 15.0 |  |
| lexical | lexical.llm_usage_log_path | _analytics/lexicon/lexical-extracts/lexical-llm-usage.csv |  |
| lexical | lexical.meaning_max_strongs_per_batch | 8 | SUPERSEDED 2026-09-22 (escalation #1842), researcher instruction verbatim: batching based on strongs is inappropriate, the units of operation is verses not strongs. Replaced by lexical.meaning_max_verses_per_batch (reactivated). No live code reads this key anymore -- _chunk_verses_fixed_size() replaced _chunk_verses_by_strong_density() as meaning() own chunker (iba/app/handlers/lexical.py). Marked inactive, not removed -- auditable history, same pattern this key own use-text already documents for its own predecessor. |
| lexical | lexical.meaning_max_verses_per_batch | 1 | Cap on verses per lexical.meaning batch -- REACTIVATED 2026-09-22 (escalation #1842), researcher instruction verbatim: "batching based on strongs is inappropriate, the units of operation is verses not strongs." Reverts the 2026-09-21 supersession by lexical.meaning_max_strongs_per_batch (now inactive): that switch was made because a fixed verse count was found unsafe when strong-density varies (M67 5-verse chunks ranged 6-21 strongs) -- but the strong-density approach own failure that triggered this reversal (M49, 2026-09-22) was a 3-verse chunk (union of 8 strongs), not an unusually dense one, so it was not actually delivering the safety its adoption assumed. Value set to 1 (not the old 5): live per-verse M-tagged strong density across M49 own 193-verse scope ranges 1-10 (median 3) -- a single-verse batch bounds each call to one verse own inherent content, isolating any remaining density outlier to one retryable batch instead of an unpredictable multi-verse one. Read by _chunk_verses_fixed_size() (iba/app/handlers/lexical.py). |
| lexical | lexical.relational_max_verses_per_batch | 1 | Cap on verses per lexical.relational batch (#1860, 2026-09-23 split) -- mirrors lexical.meaning_max_verses_per_batch's own value and rationale (single-verse batches bound each call to one verse's own inherent content). Read by _chunk_verses_fixed_size() via handlers/lexical.py:relational. |
| lexicon | lexicon.bracket_pairs | {'(': ')', '[': ']', '{': '}'} | open->close bracket pairs classify_row/strip_bracketed treat as nestable — a gloss that is wholly one bracketed aside (e.g. '(obsolete)') classifies as 'not applicable'. |
| lexicon | lexicon.classify_lookup_max_words | 3 | classify_row: a gloss/description with at most this many space-separated words is 'lookup', more is 'description' — same shape as candidate.tag_max_words's word-count threshold. |
| lexicon | lexicon.header_pos_tags | ['v', 'vb', 'n', 'a', 'adj', 'adv', 'prep', 'subst', 'conj', 'interj', 'pron', 'num', 'part', 'n m', 'n f', 'n c', 'nm', 'nf', 'nc', 'n pr m', 'n pr f', 'n pr loc'] | meaning_tree_rows()/is_header_only_line(): a strong_meaning_tree row with no sense_code of its own, whose entire (tag-stripped) text exact-matches one of these bare part-of-speech abbreviations, is a STEP-source section header for the numbered sense group that follows, not a sense itself — excluded before it ever becomes a strong_meaning_parsed row. Escalation #1668, 2026-09-10. |
| lexicon | lexicon.linebreak_pattern | [\r\n]+ | the only recognised sense-separator in strong_meaning_tree.sense_text/strong_lexicon.lsj/mounce — commas/semicolons/colons are NOT separators (STEP itself displays them as one sense). |
| lexicon | lexicon.lsj_level_tags | ['level1', 'level2', 'level3', 'level4'] | LSJ's own HTML tag names marking an explicit outline-level boundary (<LevelN>). |
| lexicon | lexicon.lsj_sublabel_pattern | ^\d+[a-z]*$ | LSJ sublabels are a bare number + optional letter (e.g. '2', '2a') — combined with the current top-level Roman numeral into 'I.2a'. |
| lexicon | lexicon.lsj_top_level_label_pattern | ^[IVXLCDM]+$ | LSJ top-level sense labels are Roman numerals (I, II, III, ...) — matched to track the current top-level for building compound sublabels like 'I.2'. |
| lexicon | lexicon.non_latin_script_pattern | [Ͱ-Ͽἀ-῿֐-׿] | classify_row: any match forces 'description' regardless of word count — Greek/Hebrew Unicode block ranges STEP's lexicon text uses. |
| lexicon | lexicon.outline_code_pattern | ^(\d+[a-zA-Z0-9]*\))\s*(.*)$ | strong_meaning_tree.sense_text: matches a leading outline code (e.g. '1)', '2a)') when sense_code itself is empty, splitting it from the remaining gloss text. |
| lexicon | lexicon.quality_report_path | research/discovery/lexicon-parse.md | where lexicon.validate persists its findings |
| lexicon | lexicon.ref_tag_pattern | <ref=['"]([^'"]*)['"]> | matches STEP's <ref='Act.14.17'>display</ref> markup (a nameless '=value' pseudo-attribute HTMLParser can't parse as a real attribute) so it can be rewritten to a well-formed <ref key="..."> before parsing. |
| manifest | manifest.exclude_exts | ['.pyc', '.pyo', '.pyd', '.tmp', '.swp', '.lock'] | file extensions excluded from a manifest.rebuild scan (compiled/transient junk only) |
| manifest | manifest.report_path | research/discovery/file-manifest.md | where manifest.rebuild writes its summary report |
| manifest | manifest.skip_dirs | ['.git', '__pycache__', 'venv', '.venv', 'env', 'node_modules', '.claude', '.idea', '.vscode', '.pytest_cache', '.mypy_cache', '.ruff_cache'] | directories excluded from a manifest.rebuild scan (VCS/build/cache machinery only — everything else in the project tree, including every archive/ folder, is indexed) |
| method | lexical.run_max_verses | 5000 |  |
| method | method.inner_being_narrative_guidance_path | workflow/instructions/WA-inner-being-narrative-guidance-v1-2026-07-28.md | current version of the inner-being-narrative guidance (the three-channel scope requirement + the required Scope self-check section) — report.book_narrative_validate and any AI writing such a narrative must follow this exact file; bump this setting (not memory) when the guidance revises |
| method | method.interpretation_questions_path | workflow/instructions/WA-interpretation-questions-v1.4-2026-08-02.md | current version of the Q1-Q10 interrogative + Part B guidance of interpretation — the passage-debate scaffold and any AI applying it must follow this exact file |
| method | method.passage_read_guidance_path | workflow/instructions/WA-passage-read-guidance-v1.5-2026-08-02.md | current version of the passage read guidance (steps 1-5 + notes, incl. step 2 note (f)) — the passage-debate scaffold and any AI applying it must follow this exact file; bump this setting (not the debates' memory) when the guidance revises |
| narrative | method.narrative_hard_constraints_path | workflow/instructions/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md | current version of the book-agnostic hard constraints (nothing invented, open threads stay open, no forced unity, plain language, no self-reference) every generated narrative must follow — bump this setting (not memory) when the doc revises |
| narrative | narrative.book_alias_map | {'1ch': '1Ch', '1chr': '1Ch', '1chron': '1Ch', '1chronicles': '1Ch', '1co': '1Cor', '1cor': '1Cor', '1corinthians': '1Cor', '1jn': '1Jo', '1jo': '1Jo', '1john': '1Jo', '1kgs': '1Ki', '1ki': '1Ki', '1kin': '1Ki', '1kings': '1Ki', '1pe': '1Pe', '1pet': '1Pe', '1peter': '1Pe', '1sa': '1Sa', '1sam': '1Sa', '1samuel': '1Sa', '1th': '1Th', '1thes': '1Th', '1thess': '1Th', '1thessalonians': '1Th', '1ti': '1Ti', '1tim': '1Ti', '1timothy': '1Ti', '2ch': '2Ch', '2chr': '2Ch', '2chron': '2Ch', '2chronicles': '2Ch', '2co': '2Cor', '2cor': '2Cor', '2corinthians': '2Cor', '2jn': '2Jo', '2jo': '2Jo', '2john': '2Jo', '2kgs': '2Ki', '2ki': '2Ki', '2kin': '2Ki', '2kings': '2Ki', '2pe': '2Pe', '2pet': '2Pe', '2peter': '2Pe', '2sa': '2Sa', '2sam': '2Sa', '2samuel': '2Sa', '2th': '2Th', '2thes': '2Th', '2thess': '2Th', '2thessalonians': '2Th', '2ti': '2Ti', '2tim': '2Ti', '2timothy': '2Ti', '3jn': '3Jo', '3jo': '3Jo', '3john': '3Jo', 'act': 'Act', 'acts': 'Act', 'amo': 'Amo', 'amos': 'Amo', 'canticles': 'Song', 'col': 'Col', 'colossians': 'Col', 'dan': 'Dan', 'daniel': 'Dan', 'deu': 'Deu', 'deut': 'Deu', 'deuteronomy': 'Deu', 'dt': 'Deu', 'ecc': 'Ecc', 'eccl': 'Ecc', 'ecclesiastes': 'Ecc', 'eph': 'Eph', 'ephesians': 'Eph', 'est': 'Est', 'esth': 'Est', 'esther': 'Est', 'ex': 'Exo', 'exo': 'Exo', 'exod': 'Exo', 'exodus': 'Exo', 'eze': 'Eze', 'ezek': 'Eze', 'ezekiel': 'Eze', 'ezk': 'Eze', 'ezr': 'Ezr', 'ezra': 'Ezr', 'gal': 'Gal', 'galatians': 'Gal', 'gen': 'Gen', 'genesis': 'Gen', 'hab': 'Hab', 'habakkuk': 'Hab', 'hag': 'Hag', 'haggai': 'Hag', 'heb': 'Heb', 'hebrews': 'Heb', 'hos': 'Hos', 'hosea': 'Hos', 'isa': 'Isa', 'isaiah': 'Isa', 'jam': 'Jam', 'james': 'Jam', 'jas': 'Jam', 'jdg': 'Judg', 'jdgs': 'Judg', 'jer': 'Jer', 'jeremiah': 'Jer', 'jhn': 'Joh', 'jn': 'Joh', 'job': 'Job', 'joe': 'Joe', 'joel': 'Joe', 'joh': 'Joh', 'john': 'Joh', 'jol': 'Joe', 'jon': 'Jon', 'jonah': 'Jon', 'jos': 'Jos', 'josh': 'Jos', 'joshua': 'Jos', 'jud': 'Jude', 'jude': 'Jude', 'judg': 'Judg', 'judges': 'Judg', 'lam': 'Lam', 'lamentations': 'Lam', 'lev': 'Lev', 'leviticus': 'Lev', 'lk': 'Luk', 'luk': 'Luk', 'luke': 'Luk', 'mal': 'Mal', 'malachi': 'Mal', 'mar': 'Mar', 'mark': 'Mar', 'mat': 'Mat', 'matt': 'Mat', 'matthew': 'Mat', 'mic': 'Mic', 'micah': 'Mic', 'mk': 'Mar', 'mrk': 'Mar', 'mt': 'Mat', 'nah': 'Nah', 'nahum': 'Nah', 'neh': 'Neh', 'nehemiah': 'Neh', 'num': 'Num', 'numbers': 'Num', 'oba': 'Obd', 'obad': 'Obd', 'obadiah': 'Obd', 'obd': 'Obd', 'phi': 'Phili', 'phil': 'Phili', 'phile': 'Phile', 'philemon': 'Phile', 'phili': 'Phili', 'philippians': 'Phili', 'phlm': 'Phile', 'phm': 'Phile', 'php': 'Phili', 'pro': 'Pro', 'prov': 'Pro', 'proverbs': 'Pro', 'prv': 'Pro', 'ps': 'Psa', 'psa': 'Psa', 'psalm': 'Psa', 'psalms': 'Psa', 'pss': 'Psa', 'qoh': 'Ecc', 'rev': 'Rev', 'revelation': 'Rev', 'rom': 'Rom', 'romans': 'Rom', 'rut': 'Rut', 'ruth': 'Rut', 'rv': 'Rev', 'sng': 'Song', 'song': 'Song', 'songofsolomon': 'Song', 'songofsongs': 'Song', 'sos': 'Song', 'tit': 'Tit', 'titus': 'Tit', 'zec': 'Zec', 'zech': 'Zec', 'zechariah': 'Zec', 'zep': 'Zep', 'zeph': 'Zep', 'zephaniah': 'Zep'} | book name or abbreviation -> the book code iba.db verse.reference uses. Keys are lower case with spaces and dots removed (lib/narrativeregister.py parse_refs normalises the same way). The chapters write full names (2 Corinthians), the register short codes (2Co), verse uses its own (2Cor) -- escalation #2110, spec sec1, sec3.8 |
| narrative | narrative.chapter_kinds_without_file | ['part heading', 'deferred'] | Escalation #2155: the narrative_chapter kinds that have no chapter file of their own (a part heading, a deferred placeholder). Narrative-Register.ps1 AddChapter accepts these with no -CurrentFile; every other kind needs a file on disk. |
| narrative | narrative.citation_index_path | _analytics/essay/spirit_soul_body/narrative-citation-index.md | the published citation index: every verse cited in the narrative, in canonical order, with where it is cited and which claims rest on it (Export; escalation #2110, spec sec8) |
| narrative | narrative.claim_changes_path | _analytics/essay/spirit_soul_body/narrative-claim-changes.md | the published change log, by update, newest first, and the Structure log (Export; escalation #2110, spec sec8) |
| narrative | narrative.claim_register_path | _analytics/essay/spirit_soul_body/narrative-claim-register.md | the published claim register (Narrative-Register.ps1 -Action Export): index notes, chapters with their sections and the claims told there, the original essay claims, the claims not in the narrative, the Tally. One fixed name, outside inner-being-narrative/, so it is never copied to learning4comfort (escalation #2110, spec sec8) |
| narrative | narrative.copy_source_dir | _analytics/essay/spirit_soul_body/inner-being-narrative | Escalation #1941 (researcher, 2026-10-04): the folder whose current top-level .md files Copy-NarrativeToLearning4Comfort.ps1 copies to the learning4comfort inbox. archive/ is never copied. |
| narrative | narrative.generate_max_cost | 3.0 | USD cost cap (from the pre-call ESTIMATE) — over this, report.book_narrative_generate refuses outright (cost-cap-exceeded) rather than pausing for approval; raise it deliberately for a book large enough to need it |
| narrative | narrative.generate_max_output_tokens | 16000 | max_tokens on the Messages API call — the ceiling on how long the generated narrative can be |
| narrative | narrative.generate_model | claude-sonnet-5 | the Anthropic model narrative.generate submits the package to |
| narrative | narrative.learning4comfort_inbox_dir | C:/learning4comfort/publication-inbox/the_inner_being | Escalation #1941 (researcher, 2026-10-04: folder the_inner_being): where Copy-NarrativeToLearning4Comfort.ps1 copies the current narrative files. Local-only staging owned by the learning4comfort repo, which prepares, reviews and publishes. |
| narrative | narrative.output_pattern | WA-{book}-inner-being-narrative.md | filename pattern for the generated narrative, written under report.verse_analysis_output_dir/<book_label>/ — same folder its source debates live in |
| narrative | narrative.quote_min_words | 2 | #2173 G14: quoted parts shorter than this many words are not quote-checked |
| narrative | narrative.rate_input_per_million | 3.0 | USD per million input tokens, at narrative.generate_model's current rate — used for both the pre-call estimate and the real post-call cost; edit if the model default changes to a different price tier |
| narrative | narrative.rate_output_per_million | 15.0 | USD per million output tokens, at narrative.generate_model's current rate |
| narrative | narrative.register_report_dir | outputs/narrative-register | where Narrative-Register.ps1 -Action Find/History/Check write their dated reports (escalation #2110) |
| narrative | narrative.scope_check_report_path | _analytics/essay/book-narrative-scope-check.md | where report.book_narrative_validate persists its findings |
| narrative | narrative.usage_log_path | _analytics/essay/narrative-generate-usage.csv | append-only on-disk ledger of every LIVE call's real tokens/cost — scripts/cost_ledger.py (repo root) only ingests Console CSV exports, not this app's own calls, so this is the audit trail for those |
| notification | notification.header_run_id | run_id       : {run_id} | run-header line — the run's id, for Escalation.ps1 -RunId |
| notification | notification.header_runs_over | runs over    : {runs_over} | run-header line (only book/word-scoped work packages print this) |
| notification | notification.header_step | step         : {step} | run-header line 2 (only scripts with a selectable step print this) |
| notification | notification.header_work_package | work package : {work_package} | run-header line 1 — which work package is running |
| notification | notification.not_initialised | The app is not initialised. Run first:  iba\app\ps\Start-Iba.ps1 | shown by every PS script's readiness guard when the app/DB isn't initialised |
| notification | notification.paused_banner_guided | PAUSED — awaiting your decision. Answer with:   .\Escalation.ps1 -Action AnswerRun -RunId {run_id} -Decision <Approve\|Reject\|Revise\|Hold\|Noted> [-Comment ...] then re-run this exact command with -RunId {run_id} to act on the answer. | non-chained single-step work packages' PAUSED banner (candidate-quality, candidate-curation, configuration-maintenance, passage-quality) |
| notification | notification.paused_banner_passthrough | PAUSED — {message} | chained work packages' default PAUSED banner (build-passages, set-candidates) — overridden per work package by cfg_work_package.paused_message when set (e.g. new-word) |
| notification | notification.step_result_line |   {0,-20} {1,-14} {2} | per-step result line format (PowerShell -f) — step/path/message, colour by outcome |
| notification | notification.stopped_banner | STOPPED — {message} | chained work packages' STOPPED banner — uniform across build-passages/set-candidates/new-word |
| pathaudit | pathaudit.report_path | outputs/configs/path-audit.md | where pathaudit.scan writes its full findings report |
| raw | discovery.follow_related | False | relatedNos is root-family noise (H2519 -> 'to divide', 'Mount Halak'). Not followed. |
| raw | language.greek_prefix | G | a strong starting with this is Greek; else Hebrew |
| raw | meaning.head_marker | :  | a mediumDef starting with this is a SENSE: head + the lemma's tree. Else the code is its own lemma. |
| raw | raw.meaning_tree_clean_pattern | ^(?:[^<]\|<(?!(?i:br\b))[^>]*>)*$ | a clean strong_meaning_tree.sense_text: any text plus complete <ref>...</ref> spans (STEP's own citation markup, tolerated -- BUILD.md notes Greek mediumDef is prose with <ref> tags); any OTHER leftover markup (<br>, <b>, ...) fails -- the same <br> parser bug as strong_sense.head, one level deeper |
| raw | raw.strong_base_pattern | ^([HG]\d+)([A-Z]?)$ | Strongs-code base/sub-letter split - single home for this fact (2026-07-29), replacing three independent copies (handlers/raw.py, lib/versespanmeaningreport.py, and the retired candidate.lemma_base_pattern) |
| raw | raw.zero_strongs_action | reject | What discover() does when a word resolves to zero strongs: 'reject' (default, researcher 2026-08-22 -- 'it should not happen', treated as anomalous every time until decided otherwise for a specific case) or 'proceed' (register the word anyway with zero strongs, no escalation). |
| registry | registry.duplicate_shared_threshold | 1.0 | fraction of a new words seed strongs an existing word must already hold for registry.create to warn it may be a duplicate/typo (1.0 = must share ALL strongs) |
| registry | registry.strip_ends_pattern | [^A-Za-z] | on entry, strip runs of these from BOTH ends of the word ('[hypocrisy]' -> 'hypocrisy'); internal hyphens/spaces kept. Word matching is case-insensitive. |
| report | report.auto_backfill_before_render | True | report.verse_span_meaning auto-runs raw.backfill_meaning_for() for any span whose strong is not yet registered, for the exact book+range being rendered, before writing the report -- researchers direct 2026-07-26 instruction (do not leave partial-coverage reports as a silent manual follow-up step) |
| report | report.batch_progress_path | iba/app/reports/batch-progress.md |  |
| report | report.cluster_path | _analytics/Clusters/cluster.md | where report.cluster persists its output |
| report | report.cluster_stem_prefix_len | 4 | prefix length used as the final grouping key after suffix-stripping, report.cluster's meaning-stemming aid |
| report | report.cluster_stem_suffixes | ['ically', 'iously', 'ously', 'ingly', 'edness', 'fulness', 'tion', 'sion', 'ness', 'ings', 'ing', 'edly', 'ed', 'ly', 'ies', 'es', 's', 'able', 'ible', 'tive', 'ive', 'ful', 'ous', 'al', 'ic'] | one-pass longest-match suffix strip for report.cluster's meaning-stemming grouping aid (grace/gracious/graciously -> one group) |
| report | report.cluster_top_meanings | 10 | how many stem-grouped meaning groups to show per cluster in report.cluster's new summary section |
| report | report.lexical_extract_output_dir | _analytics/lexicon/lexical-extracts | output directory for report.lexical_extract's JSON output (governance.reports_must_persist) |
| report | report.lexical_extract_output_pattern | lexical-extract-{run_id}.json | filename pattern for report.lexical_extract's JSON output |
| report | report.lexical_notes_output_pattern | lexical-notes-{run_id}.json |  |
| report | report.obs_catalogue_path | Workflow/Catalogue/obs-catalogue.md | where report.obs_catalogue persists its output |
| report | report.output_dir | _analytics/registry | where report.word writes its output |
| report | report.output_pattern | report-{word}.md | filename pattern for report.word's output ({word} substituted) |
| report | report.passage_debate_naming_pattern | WA-{book}-{range}-debate.md | filename pattern for report.passage_debate ({book}/{range} substituted); stable scheme — reportkit archives the prior version on regenerate, no -vN-/date in the name itself |
| report | report.registry_path | _analytics/registry/registry.md |  |
| report | report.sample_verses | 3 | how many sample verses to show the span layer for |
| report | report.schema_overview_bible_research_path | workflow/schema/bible_research/schema-overview.md | where report.schema_overview_bible_research persists its output |
| report | report.schema_overview_path | workflow/schema/schema-overview.md | where report.schema_overview persists its output |
| report | report.seed_candidate_path | research/discovery/seed-candidate.md | where report.seed_candidate persists its output |
| report | report.show_validation | True | show the validation results (util.validation) for the word |
| report | report.show_verse_text | True | show the verse's plain text above its spans |
| report | report.span_analysis_path | research/discovery/span-analysis.md | where report.span_analysis persists its output |
| report | report.span_fields | ['position', 'surface', 'strong_variant', 'morph_code', 'is_particle', 'sense'] | which columns the span table shows |
| report | report.stage1_coverage_validation_pattern | outputs/stage1-coverage-validation-{cluster_code}-{run_id}.csv | Where lexical.meaning's own per-run coverage-validation report (stage1coverage.validate_coverage, BUILD #315) is written, every live call -- {cluster_code}/{run_id} substituted by the caller. Was a hardcoded f-string in iba/app/handlers/lexical.py; governance.reports_must_persist's own "config-defined report path" requirement (matching the established report.batch_progress_path / report.lexical_notes_output_pattern precedent) means it should have been this from the start -- found live 2026-09-22, escalation #1824 governance audit. |
| report | report.strong_fields | ['stepGloss', 'accentedUnicode', 'stepTransliteration', 'head', 'count', 'verses'] | which columns the L1->L2 strong table shows |
| report | report.strong_meaning_path | research/discovery/strong-meaning.md | where report.strong_meaning persists its output |
| report | report.strong_verse_output_dir | _analytics/registry/word_registry | base folder for report.strong_verse output -- one file per word/strong pair, filed under <base>/<word>/ |
| report | report.verse_analysis_output_dir | _analytics/Bible_Books | base folder for report.verse_span_meaning, sub-foldered per book at write time |
| report | report.verse_analysis_output_pattern | {book}-{range}-verse-span-meaning.md | filename pattern for report.verse_span_meaning ({book}/{range} substituted) |
| report | report.verse_gap_note | **Verse gap -- by design.** `{ref}` has no verse row in iba.db (no onboarded term's concordance search ever surfaced it -- see governance.verse_gap_by_design). Not an error; continuing with the next available verse. | inline note both report.verse_span_meaning and report.passage_debate insert into their output wherever a verse is structurally known to be missing from iba.db within the rendered range (lib.versespanmeaningreport.detect_verse_gaps) -- {ref} substituted |
| report | report.verse_lexical_output_pattern | {book}-{range}-verse-lexical.md | filename pattern for report.verse_lexical ({book}/{range} substituted) — reuses report.verse_analysis_output_dir for the base folder, same as report.verse_span_meaning did |
| report | report.version_on_regenerate | True | app-wide: when true, reportkit.write_report never overwrites or archives-and-replaces an existing report -- every write gets a fresh, never-reused filename (stem-v{n}-{date}.ext, n = 1 + the highest existing version for that exact stem). Set false to fall back to the old archive-before-overwrite behaviour. Researcher direction 2026-08-05 (debate-analytic-process-digest, B2/Q6): reports must never be overwritten, and this must be one app-wide setting, not a per-step convention. |
| report | report.whole_book_read_naming_pattern | WA-{book}-whole-book-read.md | filename pattern for report.whole_book_read ({book} substituted); stable scheme — reportkit archives the prior version on regenerate, same convention report.passage_debate_naming_pattern already uses |
| report | report.word_registry_span_output_dir | _analytics/registry | base folder for report.word_registry_span output — one file per registry word |
| retention | retention.report_path | research/discovery/log-retention.md | where the run/escalation/validation_result log-retention & run-health report is written |
| retention | retention.snapshot_keep_count | 5 | how many pre-run DB snapshots to keep (oldest pruned first) -- lib/dbsnapshot.py, wired into run.py so every NEW run gets a rollback point; built 2026-07-22 after a candidate.load bug corrupted 1029 candidate_seed rows with no fine-grained rollback available |
| step | discovery.particle_pattern | ^[HG]9\d{3}$ | grammar-particle codes; excluded from discovery, flagged on a span |
| step | step.cap | 60 | STEP's hard result cap; > this triggers the forward-walk |
| step | step.expect_gloss_contains | God | STEP preflight known-answer probe |
| step | step.expect_min_verses | 1000 | STEP preflight known-answer probe |
| step | step.probe_strong | H0430 | STEP preflight known-answer probe |
| step | step.required_for_runs | True | STEP is mandatory infra, not optional -- initpys startup preflight and every STEP-dependent tool/handler must refuse rather than degrade when this is true and STEP is down |
| step | step.span_html | <span(?: var='[^']*')?(?: morph='([^']*)')? strong='([^']*)'>([^<]*)</span> | how STEP formats an interlinear span in a verse preview: (morph, strong, surface). The forward-walk and the span parse read it. |
| step | step.walk_end | Rev.22.21 | forward-walk upper bound |
| step | step.walk_max_iter | 400 | forward-walk safety bound |
| step | step.walk_start | Gen.1.1 | forward-walk lower bound |
| strand_reading | strand_reading.output_dir | outputs/strand-reading | where Strand-Reading.ps1 writes each strand's context, gather and account files, one folder per strand (escalation #2172) |
| table_export | table_export.output_dir | {'iba': 'Workflow/schema/iba', 'bible_research': 'Workflow/schema/bible_research'} | where table.export writes its CSVs |
| validation | lexical.readiness_report_path | research/discovery/lexical-readiness.md | where lexical.readiness persists its findings -- #1606/#1706 Phase A |
| validation | purge.audit_report_path | research/discovery/purge-audit.md | where purge.audit persists its findings -- escalation #1766 |
| validation | purge.execute_report_path | research/discovery/purge-execute.md | where purge.execute persists its findings -- escalation #1766/#1868 |
| validation | purge.retire_database_report_path | research/discovery/purge-retire-database.md | where purge.retire_database persists its findings -- escalation #1868/#1872/#1873 |
| validation | purge.unsafe_check_min_soft_deleted | 10 | a table with more than this many soft-deleted rows gets a live-dependency check before being listed as safe to purge -- escalation #1766 v2, researcher's own threshold ('for each table with > 10 softdelete records check the dependencies'). Was a hardcoded constant in the escalation's own ad-hoc audit; made config-driven here per the same pattern already fixed twice this session (#1753 B3, #1761). |
| validation | session_close.always_read_max_bytes | 10000 | SC15: the size limit, in bytes, for a control file read every conversation (CLAUDE.md, the memory index). Escalation #2186. |
| validation | session_close.build_scope | ['iba/app/*.py', 'iba/app/*.ps1', 'iba/config/*', '.claude/hooks/*', '.claude/commands/*'] | #2173 SC10 (C3): code and config files that must be named in what BUILD.md gained |
| validation | session_close.build_scope_exclude | ['iba/app/reports/*', '*/__pycache__/*', '*.pyc'] | #2173 SC10: excluded from build_scope |
| validation | session_close.control_kinds | ['session_entry', 'objective', 'mechanism', 'session_procedure', 'claude_memory', 'tool_usage'] | The cfg_control_home kinds whose files session-close SC15 checks (cfgquality.find_control_file_problems). Escalations #2186, #2187. |
| validation | session_close.final_commit_marker | session log git confirmation | #2173 S6/SC13: the message text of a session-close's final (second) commit; at start, a newest commit without it means the last session did not complete its close |
| validation | session_close.held_words | ['hold', 'held', 'later', 'park', 'parked', 'defer', 'postpone', 'come back', 'revisit', 'check', 'clarify', 'follow-up', 'follow up', 'not done here'] | #2173 SC4(b): a researcher message with one of these words holds, defers or asks to check something; it needs its register item named (or 'not held: reason') |
| validation | session_close.history_markers | ['~~', '\\bSUPERSEDED\\b', '\\b(?:Superseded\|Corrected\|CORRECTED\|Restated\|REWRITTEN\|Amended\|Rebuilt) 20\\d\\d-\\d\\d-\\d\\d'] | SC15: regular expressions for replaced-history text that may not stand in a control file (struck-through text, superseded/corrected/amended notes; rule 96). Escalation #2186. |
| validation | session_close.history_pointer_word | history | SC15: a line in a control file that points into an archive/ folder must carry this word, marking it as a pointer to history read deliberately (rule 96). Escalation #2186. |
| validation | session_close.log_sections | ['1. Scope', '2. Escalations', '3. Files', '4. Decisions', '5. Open items', '6. Git'] | #2173 SC8/SC9: the six section headings of a session log, in the order of governance.session_log_required_content; section 4 lines name their targets (SC9); section 6 is written after the first commit (SC13) |
| validation | session_close.message_min_words | 4 | #2173 SC3: a researcher message shorter than this many words is never matched by text (it would be found inside almost any comment); it always needs its disposition |
| validation | session_close.no_record_messages | ['/start-project', '/session-close', '/developer-mode', '/exit-developer-mode'] | #2173 SC3: session-start/close command names that are researcher messages needing no escalation record (compared normalised, with up to 12 characters of arguments) |
| validation | session_close.open_items_exclude | ['iba/app/reports/*', 'outputs/escalation/*', 'outputs/narrative-register/*', 'research/discovery/*'] | #2173 SC4(a): generated report folders whose headings are not authored Open items sections (the close report itself has one named 'Open items in the register') |
| validation | session_close.placement_kinds | ['told', 'claim', 'data', 'forward', 'held', 'parked', 'context'] | #2173 SC5(d), Q2: the first word of a verse's placement in a reading file; forward/held name an open OT-nn.n or #nnnn; told is checked against the narrative |
| validation | session_close.reading_file_pattern | (reading\|account\|ledger\|weave) | #2173 SC5(d): a changed file in reading_scope whose name matches this is a reading file and needs a placement per verse it names |
| validation | session_close.reading_scope | ['_analytics/Clusters/*', '_analytics/cross-cluster-web/*'] | #2173 SC5(d): where reading files live (fnmatch; * crosses folders) |
| validation | session_close.report_path | iba/app/reports/session-close.md | where session.close persists its findings -- escalation #1875 |
| validation | session_close.state_path | iba/app/reports/session-close-state.json | #2173 SC5(c): the register-check findings at the previous session's last close (the baseline that tells a new finding from a standing one) |
| validation | spine.meaning_lexicon_languages | ['Greek'] | #2173 P3: languages whose strongs are checked for a strong_lexicon row (lsj, mounce). Evidence 2026-10-20: 25 Hebrew strongs sampled at random from STEP returned no lsjDefs and no shortDefMounce (LSJ and Mounce are Greek lexicons); every Greek strong has a row. |
| validation | spine.quality_report_path | research/discovery/spine-check.md | where spine.check persists its findings |
| validation | validation.output_dir | outputs/validations | where validation.word/validation.book write their output |
| validation | validation.show_candidate | False | book report: include the candidate (L4b) section |
| validation | validation.show_delta | True | word report: include the pre/post run-delta section |
| validation | validation.show_expectations | True | word report: include the semantic-expectations section |
| validation | validation.show_health | True | word/book report: include the App & DB health section |
| validation | validation.show_integrity | True | word report: include the config-derived integrity section |
| validation | validation.show_passages | True | book report: include the passages section |
| validation | validation.show_references | True | word report: include the FK-resolvability section |
| validation | validation.show_value_quality | True | word/book report: include the value-quality section (cfg_column.expectation checks, scoped to this word/book) |

<a id="5-step-apis"></a>
## 5. STEP apis

| name | route | input | returns |
| --- | --- | --- | --- |
| call1_meanings | rest/search/masterSearch/version={version}\|meanings={word} | the English word | definitions[] (the seed strongs) + results[] (verses) |
| call2_getInfo | rest/module/getInfo/{version}//{strong}// | a strong | vocabInfos[0] — the detail and the meaning |
| call3_strong | rest/search/masterSearch/strong={strong}\|version={version} | a strong | results[] — verses, each preview a full interlinear |

<a id="6-work-packages-steps-the-sequence"></a>
## 6. Work packages & steps (the sequence)

**batch-progress-report** — runs over `none` · script `iba/app/ps/BatchProgress.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.batch_progress | iba.app.handlers.reports:batch_progress_report | none | Read-only live progress over run_batch (#1756) -- -FilterRunId/-Step/-SelectorKey all optional, combine with AND; no filters = every currently-running batch DB-wide, the live-right-now view. |

**behaviour** — runs over `none` · script `iba/app/ps/Behaviour.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | behaviour.list | iba.app.handlers.reports:behaviour_list | none | every active cfg_behaviour_rule, optionally one -Class, to behaviour.list_report_path -- read-only (#2207: through run.py) |

**book-narrative** — runs over `book` · script `iba/app/ps/archive/Book-Narrative.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_generate | iba.app.handlers.archive.narrative:generate | book | live Anthropic API narrative generation -- same handler as the standalone book-narrative-generate work package (kept active for standalone reruns); ordinal 0 of book-narrative, chained with report.book_narrative_validate which runs automatically against this steps own output path once it completes. |
| 1 | report.book_narrative_validate | iba.app.handlers.archive.narrative:validate | none | structural validation of the just-generated narrative file -- same handler as the standalone book-narrative-validate work package (kept active for standalone reruns); ordinal 1 of book-narrative, receives its -Path from ordinal 0s own output automatically via the scripts custom orchestration. |

**book-narrative-generate** — runs over `book` · script `iba/app/ps/archive/BookNarrative-Generate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_generate | iba.app.handlers.archive.narrative:generate | book | assembles every filled report.passage_debate output for a book plus the hard-constraints and three-channel guidance docs, submits the package to the Anthropic Messages API (researcher approval required first, pause-continue on the estimated cost), and files the returned narrative under report.verse_analysis_output_dir/<book_label>/ — see lib/narrativegenerate.py |

**book-narrative-validate** — runs over `none` · script `iba/app/ps/archive/BookNarrative-Validate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_validate | iba.app.handlers.archive.narrative:validate | none | structural presence check on an inner-being narrative file — confirms a '## Scope self-check' section exists and all three required channel labels (non-human<->human, human<->human, physical world<->human) are present with non-empty content; a presence check only, not a judgment of citation quality or content accuracy — see WA-inner-being-narrative-guidance-v1-2026-07-28.md section 4 |

**build-passages** — runs over `book` · script `iba/app/ps/Build-Passages.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.build | iba.app.handlers.passage:build | book | recompute the book's passages from verse_hib (hib-continuity\|maximal); flag >review_over as needs_review. Redefined 2026-08-05 (B4) from the retired candidate-stamp/char-continuity rule -- see debate-analytic-process-digest-20260805.md Step 2. |
| 1 | passage.suggest_boundary | iba.app.handlers.passage:suggest_boundary | verse | Proposes the next candidate passage boundary (≤20 verses) from the next un-passaged verse, using cheap mechanical proxy signals only (narrative_morph density, legacy book-level genre tag, paragraph/chapter markers) — NOT a genre determination. Output is a proposal for the PS entry point to surface for researcher confirm/adjust; never auto-registers. |

**candidate-curation** — runs over `none` · script `iba/app/ps/archive/Candidate-Curate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.curate | iba.app.handlers.archive.candidate:curate | none | single-row, approval-gated correction on candidate_seed (tag or decision) -- adding a brand-new candidate lemma is the existing cfg_candidate_rule accept route via configmaint.propose |
| 1 | candidate.load | iba.app.handlers.archive.candidate:load | none | JSON-batch create/update/validate for candidate_seed -- derives lemma/strong_variant from an input English word (no lemma_key in the input), auto-loads items that pass every config-driven check, writes anything that doesn't as an inspectable decision='exception' row, then revalidates the whole existing seed the same way; one escalation total if unresolved exceptions remain |

**candidate-quality** — runs over `none` · script `iba/app/ps/archive/Candidate-Quality.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.validate | iba.app.handlers.archive.candidate:validate | none | read-only quality check: candidate_tag null/format, lemma_key/strong resolution — one escalation per invocation, standalone (not part of seed/set) |

**catalogue-report** — runs over `none` · script `iba/app/ps/Catalogue-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.obs_catalogue | iba.app.handlers.reports:obs_catalogue_report | none | structural review of wa_obs_question_catalogue (bible_research.db) on its own -- no join to finding/finding_question_link -- status/deleted lifecycle conflicts, section/tier/question_code/catalogue_version/date_added naming inconsistencies, the live tiered question set for review, and untiered integration candidates |

**catalogue-update** — runs over `none` · script `iba/app/ps/Catalogue-Update.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | obs_catalogue.update | iba.app.handlers.catalogue:update | none | Partial UPDATE of one wa_obs_question_catalogue row (bible_research.db), keyed by obs_id. Every column except obs_id is settable; columns not named in -Set are left untouched. Auto-fills last_modified (now, UTC) and catalogue_version (v2-<today>) when the caller doesn't supply them explicitly -- either is still overridable by naming it in -Set. No history/audit table -- researcher's own call, escalation #1007: 'I dont think there is any history control on this table and I don't think it is necessary.' |

**chapter-generate** — runs over `book` · script `iba/app/ps/archive/Chapter-Generate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.verse_span_meaning | iba.app.handlers.reports:verse_span_meaning_report | book | verse:span:meaning base extract -- same handler as the standalone verse-analysis-report work package (kept active for recovery reruns); ordinal 0 of chapter-generate, chained with report.passage_debate as ordinal 1. |
| 1 | report.passage_debate | iba.app.handlers.reports:passage_debate_report | book | passage-debate SCAFFOLD generator -- same handler as the standalone passage-debate-report work package (kept active for recovery reruns); ordinal 1 of chapter-generate. Manual fill-in of the written scaffold happens after this script exits, then PassageDebate-Sync.ps1 (unchanged, separate) is run once -- kept OUT of this chain because re-invoking a chained work package re-runs every ordinal from the top, which would silently overwrite a filled scaffold with a blank one. |

**cluster-assign** — runs over `none` · script `iba/app/ps/Cluster-Assign.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | cluster.assign | iba.app.handlers.cluster:assign | none | DB-wide sweep: lib.strongreconcile.reconcile() per strong — mechanical HIGH-precedent classification + backfill-to-word promotion cascade where warranted. No network beyond what a promotion cascade itself needs (a real STEP verse fetch). |
| 1 | cluster.validate | iba.app.handlers.cluster:validate | none | Read-only DB-wide coverage + exception report: unclassified strongs, backfill non-T2 not yet promoted, and the two named exception shapes (cluster with no word; backfill with an already-active/clustered sibling). Persists a report every run. UPDATED 2026-09-15 (escalation #1606): escalates if EITHER an unclassified strong exists OR either named exception shape exists -- previously only escalated on the two named exception shapes, leaving a plain unclassified count unescalated indefinitely. UPDATED 2026-09-15 (escalation #1707): before escalating, checks whether the current findings already fall within a PRIOR run's approved baseline (escalation.answered_baseline_for_step, cross-run, not just this run) -- a known, already-signed-off backlog is acknowledged automatically instead of raising a fresh escalation every run; a genuine increase in any count still escalates. |

**cluster-reading** — runs over `cluster` · script `iba/app/ps/ClusterSubgroup.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | cluster.subgroup | iba.app.handlers.cluster:subgroup | cluster | The char-subgroup stage (#1690/#1693, process b): reads a cluster's full member-strong list -- gloss/surface plus its already-captured verse-reading (Stage 1) observations -- in ONE session (never streamed/batched, rule a requires the whole cluster read before any assignment), and groups strongs into meaning-based subgroups (max 10, FLAG excluded). Writes cluster_subgroup/cluster_subgroup_strong via the recording pass; advances cluster.status from ready_for_subgroup_allocation to ready_for_reading on success. |
| 1 | cluster.reading | iba.app.handlers.cluster:reading | subgroup | The char-reading stage (#1682/#1706 Phase F, process c): given one subgroup's member strongs, reads every occurrence corpus-wide (no sampling) plus all meaning sources, using Stage 1 (verse-reading) and Stage 2 (char-subgroup) observations as grounding, and synergises the similar/different contextual meaning of the subgroup's OWN member strongs against each other. Writes ib_observation/ib_node via the recording pass (stage='char-reading'); per-strong completeness is computed by code, not LLM-self-reported; advances cluster_subgroup.status from ready_for_reading to ready_for_answer on success. |
| 2 | cluster.answer | iba.app.handlers.cluster:answer | subgroup | The char-answers stage (#1682 §4A / #1706 Phase F, process d): given one subgroup's member strongs and Stage 1/2/3's own accumulated observations, answers the catalogue's characteristic-grain question battery (52 live questions, science-extract-dependent and Stage-1-owned D7.7.1 excluded), multiple slants where the evidence genuinely differs. Writes ib_observation/ib_node via the recording pass (stage='char-answers'); per-question completeness is computed by code; advances cluster_subgroup.status from ready_for_answer to answer_complete on success. |

**cluster-report** — runs over `none` · script `iba/app/ps/Cluster-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.cluster | iba.app.handlers.reports:cluster_report | none | evaluate/review the cluster taxonomy and cluster_strong assignment coverage, scoped to strong.origin=word |

**configuration-maintenance** — runs over `none` · script `iba/app/ps/Config-Maintenance.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | configmaint.validate | iba.app.handlers.configmaint:validate | none | coherence-check the live cfg_* tables — read-only, no approval needed |
| 1 | configmaint.propose | iba.app.handlers.configmaint:propose | none | the only path that may change a cfg_* row — approval-gated (escalation, 3-way) |
| 2 | configmaint.report | iba.app.handlers.configmaint:report | none | regenerate CONFIG-REPORT.md from the live cfg_* tables — read-only |

**content-index-rebuild** — runs over `none` · script `iba/app/ps/archive/ContentIndex-Rebuild.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | content_index.rebuild | iba.app.handlers.reports:content_index_rebuild | none | full rescan of every .md file in file_manifest — clears and rebuilds content_index + content_index_scan from scratch; see lib/contentindex.py -- PAUSED 2026-09-03, escalation #1385 (redesign needed: prior real run wrote 14.1M rows / grew iba.db to 8GB). Do not run until #1385 resolves. |

**content-index-search** — runs over `none` · script `iba/app/ps/ContentIndex-Search.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | content_index.search | iba.app.handlers.reports:content_index_search | none | incremental refresh (mtime-based, only changed .md files) then a key_type:value or bare-value lookup against content_index, enriched with file_manifest metadata; results persisted via reportkit.oneoff_path, per governance.reports_must_persist |

**content-index-size-profile** — runs over `none` · script `iba/app/ps/ContentIndex-SizeProfile.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | content_index.size_profile | iba.app.handlers.reports:content_index_size_profile | none | read-only report of every .md file in file_manifest by size, largest first — file name, folder, size — for visual review before adding to cfg_content_index_exclude; see lib/contentindex.py |

**escalation-reporting** — runs over `none` · script `iba/app/ps/Escalation.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | escalation.list | iba.app.handlers.reports:escalation_list | none | every escalation not yet closed (open: raised/in-progress/re-assigned; parked: on-hold -- cfg_enum escalation_state_open/_parked, #2173 G1), each with its full history inline, then the in-progress threads and the last 15 resolved -- see lib/escalation.py:write_list_report. On demand only (not run at start, #2173 P0). |
| 1 | escalation.history | iba.app.handlers.reports:escalation_history | none | deep history for ONE item (-Id), plus its downward chain (from_id children) and every related_activity-named item -- see lib/escalation.py:write_history_report |
| 2 | escalation.thread | iba.app.handlers.reports:escalation_thread | none | open threads (type=thread): alias, id, title, open items; -State in-progress narrows; -Id OT-nn shows one thread's items with their responses -- see lib/escalation.py:write_thread_report |
| 3 | escalation.thread_export | iba.app.handlers.reports:escalation_thread_export | none | regenerates the open threads register (.md) from the escalation table, OT-nn · #id per row -- see lib/escalation.py:write_thread_register |
| 4 | escalation.context | iba.app.handlers.reports:escalation_context | none | #2173 P1: every file each open escalation (raised, in-progress, re-assigned) names in any field of any version, resolved to its latest live version; findings missing / bare -- see lib/escalationcontext.py |
| 5 | escalation.thread_audit | iba.app.handlers.reports:escalation_thread_audit | none | #2173 P5: thread quality, validity and integrity, T-a to T-g, each finding by thread item -- see lib/threadaudit.py |

**file-manifest-rebuild** — runs over `none` · script `iba/app/ps/Manifest-Rebuild.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | manifest.rebuild | iba.app.handlers.reports:manifest_rebuild | none | full rescan of the whole project tree (filename/path metadata only, no file content) — replaces file_manifest's contents; see lib/manifest.py |

**file-manifest-search** — runs over `none` · script `iba/app/ps/Manifest-Search.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | manifest.search | iba.app.handlers.reports:manifest_search | none | read-only query against file_manifest (field:value or free-text path match); results persisted via reportkit.oneoff_path, per governance.reports_must_persist |

**folder-purpose** — runs over `none` · script `iba/app/ps/FolderPurpose.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | folderpurpose.seed | iba.app.handlers.folderpurpose:folder_purpose_seed | none | Method A -- full reconciliation of folder_purpose against the live directory tree: new folders inserted, missing folders soft-deleted, disk-derived columns refreshed for every row. |
| 1 | folderpurpose.crosscheck | iba.app.handlers.folderpurpose:folder_purpose_crosscheck | none | Method B -- syncs governed_by_setting from live cfg_setting values, pre-fills type/status where unambiguous, reports the operations-needs-a-setting invariant's anomalies. |
| 2 | folderpurpose.set | iba.app.handlers.folderpurpose:folder_purpose_set | none | Method C -- hand-set type/status/usage_description for one folder. |
| 3 | folderpurpose.list | iba.app.handlers.folderpurpose:folder_purpose_list | none | Method C -- list folder_purpose rows, optionally filtered. |
| 4 | folderpurpose.show | iba.app.handlers.folderpurpose:folder_purpose_show | none | Method C -- full detail for one folder. |
| 5 | folderpurpose.autoassess | iba.app.handlers.folderpurpose:folder_purpose_autoassess | none | Method D -- fills type/status for every row missing either, from Methods A/B's own gathered facts only (governed_by_setting, manifest_category/currency, file counts, mtime). Never guesses mixed/reallocate or a category-less folder's type -- those stay for Method C. |

**lexicon-parse** — runs over `none` · script `iba/app/ps/Lexicon-Parse.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | lexicon.parse | iba.app.handlers.lexicon:parse | none | strong_meaning_tree + strong_lexicon -> strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed (corrected 2026-07-25 parse); no network, deterministic, clears and rebuilds |
| 1 | lexicon.related | iba.app.handlers.lexicon:related | none | strong -> strong_related; one live STEP getInfo call per row (relatedNos) |
| 2 | lexicon.validate | iba.app.handlers.lexicon:validate | none | read-only coverage + value-quality check across all 4 tables; persists lexicon.quality_report_path every run; escalates only if findings exist |

**log-retention** — runs over `none` · script `iba/app/ps/Log-Retention.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | retention.report | iba.app.handlers.reports:retention_report | none | run/escalation/validation_result log-retention & run-health report — read-only, no pruning |

**narrative-register** — runs over `none` · script `iba/app/ps/Narrative-Register.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | narrative_register.add_claim | iba.app.handlers.narrativeregister:add_claim | none | a new claim with its sources (-Text -BeyondText -Source) -- see lib/narrativeregister.py (escalation #2110) |
| 1 | narrative_register.edit | iba.app.handlers.narrativeregister:edit | none | changes a claim's wording, verdict or sources; the trigger logs it -- see lib/narrativeregister.py (escalation #2110) |
| 2 | narrative_register.tell | iba.app.handlers.narrativeregister:tell | none | links a claim to the block that tells it (-Chapter -Section <heading>\|<Parent > Heading>) -- see lib/narrativeregister.py (escalation #2110, #2172) |
| 3 | narrative_register.untell | iba.app.handlers.narrativeregister:untell | none | removes a claim's telling from a block (status removed; the row stays) -- see lib/narrativeregister.py (escalation #2110, #2172) |
| 4 | narrative_register.withdraw | iba.app.handlers.narrativeregister:withdraw | none | withdraws a claim (the row stays, with its history) -- see lib/narrativeregister.py (escalation #2110) |
| 5 | narrative_register.edit_note | iba.app.handlers.narrativeregister:edit_note | none | edits one block of the index text -- see lib/narrativeregister.py (escalation #2110) |
| 6 | narrative_register.edit_chapter | iba.app.handlers.narrativeregister:edit_chapter | none | edits a chapter row (number, title, kind, purpose, ruling, state, current file, place); a structural change is logged in the Structure log -- see lib/narrativeregister.py (escalation #2110, #2155) |
| 7 | narrative_register.edit_section | iba.app.handlers.narrativeregister:edit_section | none | edits a section row (heading, level, parent, order); a rename keeps the old row and moves its current passages to the new one -- see lib/narrativeregister.py (escalation #2110) |
| 8 | narrative_register.record | iba.app.handlers.narrativeregister:record | none | records a weave's whole update from a JSON file, then compares the chapter versions passage by passage and lists what the JSON does not account for -- see lib/narrativeregister.py (escalation #2110) |
| 9 | narrative_register.find | iba.app.handlers.narrativeregister:find | none | read-only search (-Verse -Chapter -Section -Claim -Text -Escalation -Thread -Verdict -NotInNarrative -ToldInMoreThanOne) -- see lib/narrativeregister.py (escalation #2110) |
| 10 | narrative_register.history | iba.app.handlers.narrativeregister:history | none | read-only: every change to a claim and to the passages that tell it -- see lib/narrativeregister.py (escalation #2110) |
| 11 | narrative_register.check | iba.app.handlers.narrativeregister:check | none | read-only: chapters, sections and passage anchors against the files on disk; chapters with no kind or purpose, duplicate reading orders, stray files, direct-edit rows -- see lib/narrativeregister.py (escalation #2110, #2155) |
| 12 | narrative_register.export | iba.app.handlers.narrativeregister:export | none | regenerates the three published files (spec sec8), the register opening with the Chapters table -- see lib/narrativeregister.py (escalation #2110, #2155) |
| 13 | narrative_register.add_chapter | iba.app.handlers.narrativeregister:add_chapter | none | adds a chapter row (-Chapter -Title -Kind -Purpose -PurposeRef -After\|-ReadingOrder -CurrentFile), moves the later chapters down, writes its section rows from the file and a Structure log entry -- see lib/narrativeregister.py (escalation #2155) |
| 14 | narrative_register.quote_check | iba.app.handlers.narrativeregister:quote_check | none | #2173 G14: every quotation in -File (or in the lines it added against -Against) must be in the ESV text -- see lib/quotecheck.py |

**new-word** — runs over `word` · script `iba/app/ps/New-Word.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | registry.exists | iba.app.handlers.registry:exists | word | stop if the word already exists (a refresh run handles that) |
| 1 | registry.create | iba.app.handlers.registry:create | word | create the word, status proposed->approved |
| 2 | raw.discover | iba.app.handlers.raw:discover | word | CALL 1 meanings= -> word_strong (the seed strongs) |
| 3 | raw.detail | iba.app.handlers.raw:detail | word | CALL 2 getInfo per strong -> strong + sense + tree + lexicon (the meaning) |
| 4 | raw.verses | iba.app.handlers.raw:verses | word | CALL 3 per strong -> strong_verse + verse + span (span parsed from preview) |
| 5 | raw.write | iba.app.handlers.raw:write | word | commit; mark raw-complete |
| 6 | raw.validate | iba.app.handlers.raw:validate | word | the parse-check: span vs strong_verse must agree |
| 7 | strong.reconcile | iba.app.handlers.raw:reconcile | word | Cluster-classify and, where warranted, promote every one of the word's own codes (lib.strongreconcile.reconcile() per code) -- runs last, after raw.validate, so verses/spans are already validated before classification. Point (c), backfill-cluster-triage-plan-v3-20260812.md: new-word must complete through verse_lexical for qualifying strongs. UPDATED 2026-09-15 (escalation #1606): fails (condition='unclassified') if any of the word's own codes got no cluster assignment at all, rather than always returning ok() -- an automatic classification attempt runs on every code either way, but a failed attempt is now surfaced, not silently absorbed. |

**observation-enhancer** — runs over `none` · script `iba/app/ps/Observation-Enhancer.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | observation_enhancer.apply | iba.app.handlers.observationenhancer:apply | none | Given -RuleKey, refuses unless the rule's status is confirmed/active (the researcher's own per-rule confirmation gate, escalation #1778 -- run -Action Preview and confirm via configmaint.propose first). Runs selector_sql, applies update_json to every matched row via UPDATE, logs each (observation, field) change to ib_observation_enhancer_log, and promotes a first-time confirmed rule to active. |
| 0 | observation_enhancer.preview | iba.app.handlers.observationenhancer:preview | none | Read-only. Given -RuleKey, runs that rule's selector_sql against live ib_observation and returns the match count plus a sample of matched rows (id/cluster_code/stage/tag/strong/status/obs_text, up to 10) and the update_json that would be applied. Any rule status -- does not require confirmed. No write. |

**operations-ingest** — runs over `book` · script `iba/app/ps/Operations-Ingest.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | hib.set | iba.app.handlers.operations:hib_set | book | Step 1's HIB register for a whole book -- writes hib/hib_referent_option/verse_hib from a JSON payload (-PayloadPath). Clean re-derivation per book (soft-delete existing, insert fresh), same convention passage.build uses for passage. Fails cleanly (unknown-verse/bad-payload) rather than partially writing. |
| 1 | phenomenon.set | iba.app.handlers.operations:phenomenon_set | book | Step 3's phenomena register for one already-tracked passage (needs -Chapters/-Range), from a JSON payload. Clean re-derivation per passage. Sets passage.phenomena_complete_at itself once the register is complete against verse_hib -- the phase gate operation.set checks. Fails cleanly (no-passage/unresolved-reference/bad-payload). |
| 2 | operation.set | iba.app.handlers.operations:operation_set | book | Step 4-5's operations + parties for the same passage, from a JSON payload. REFUSES (phenomena-incomplete) if passage.phenomena_complete_at is still NULL -- the actual code enforcement of WA-interpretation-questions Part B.12 / the debate digest's Step 3 phase gate. Clean re-derivation per phenomenon set. Fails cleanly on any unresolved reference. |
| 3 | closing.set | iba.app.handlers.operations:closing_set | book | Step 7 (digest) / WA-interpretation-questions-v1.4 Part C sections 4-8 for one already-tracked hib-continuity passage -- writes passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note + passage.open_decisions_note from a JSON payload. Refuses (operations-incomplete) until every live phenomenon in the passage has a live operation. Reconciliation-gated per list (BUILD.md ??64 pattern), same as hib.set/phenomenon.set/operation.set. |

**passage-debate-report** — runs over `book` · script `iba/app/ps/archive/PassageDebate-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.passage_debate | iba.app.handlers.reports:passage_debate_report | book | passage-debate scaffold generator — verifies the base verse-span-meaning extract and the current method docs (method.passage_read_guidance_path / method.interpretation_questions_path) exist, resolves output path/naming, and writes a debate-document SKELETON (front-matter, per-verse Observation/Operation/Subject-Source-Target/Interrogative/Decision placeholders, standard closing sections) for the researcher/AI to fill in; does not generate interpretive content itself |

**passage-debate-sync** — runs over `book` · script `iba/app/ps/archive/PassageDebate-Sync.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.debate_sync | iba.app.handlers.passage:debate_sync | book | re-syncs `passage.debate_status` for an already-generated `report.passage_debate` scaffold against its CURRENT on-disk content — read-only against the debate file (does not rewrite or regenerate it), DB-write only to the tracked `passage` row's `debate_status`/`debate_written_at` via the existing `passagetrack.record_debate`; the missing half of the report.passage_debate lifecycle before this (write_scaffold writes, nothing re-checked status after manual fill-in) — GOVERNANCE.md §3B |

**passage-quality** — runs over `none` · script `iba/app/ps/Passage-Quality.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.validate | iba.app.handlers.passage:validate | none | read-only quality check: passage verse_count distribution — one escalation per invocation, standalone (not part of build-passages) |

**path-audit** — runs over `none` · script `iba/app/ps/PathAudit.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | pathaudit.scan | iba.app.handlers.pathaudit:path_audit_scan | none | Project-wide scan (every .py file except cfg_utility.inactive=1 ones) for a string literal that looks like a project-relative path under a live top-level folder, with no live cfg accessor on the same line -- ADVISORY, needs a look per finding, not an auto-fix. |

**prose** — runs over `none` · script `iba/app/ps/Prose.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | prose.extract | iba.app.handlers.prose:extract | none | Programme-prose extract (JSON/MD/DOCX) |
| 1 | prose.search | iba.app.handlers.prose:search | none | FTS/plain search over prose_section |
| 2 | prose.export_chapter | iba.app.handlers.prose:export_chapter | none | Export a chapter to editable .md |
| 3 | prose.import_chapter | iba.app.handlers.prose:import_chapter | none | Turn an edited .md into a patch file (writes no DB row itself) |
| 4 | prose.flag | iba.app.handlers.prose:flag | none | Raise one wa_data_quality_flags instance (escalation #829 sec12.4, angle a) -- --flag-code, --description (required), no prose-section reference |
| 5 | prose.flag_fix_propose | iba.app.handlers.prose:flag_fix_propose | none | Search active prose for a literal match, write a review report of proposed replacements (escalation #890 D5, flag-fix angle b, propose step -- no DB write) |
| 6 | prose.flag_fix_apply | iba.app.handlers.prose:flag_fix_apply | none | Generate a PROSE supersede patch for researcher-approved section ids from a flag_fix_propose report (escalation #890 D5, angle b, apply step -- no DB write, apply via scripts/apply_session_patch.py) |
| 7 | prose.set_status | iba.app.handlers.prose:set_status | none | Set/reset prose_section.status directly for one or more -SectionIds, no body change (escalation #918, 2026-08-27 -- the reviewer's own set/reset action, superseding cfg_prose_chapter's removed chapter-status tracking); writes no DB row itself, generates a PROSE patch, same as export_chapter/import_chapter/flag_fix_propose/flag_fix_apply |

**purge-audit** — runs over `none` · script `iba/app/ps/Purge-SoftDeletes.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | purge.audit | iba.app.handlers.purge:audit | none | Read-only, app-wide: for every table with a registered soft-delete column (cfg_column.name IN deleted/delete_flagged, both databases), counts soft-deleted rows; for any table over purge.unsafe_check_min_soft_deleted, checks cfg_column.fk for a live row elsewhere still referencing one of its soft-deleted PKs and flags the table UNSAFE if so. Persists a report every run (governance.reports_must_persist). Does not remove any row -- audit only. |
| 1 | purge.execute | iba.app.handlers.purge:execute | none | Recomputes the safe/unsafe split fresh (never trusts a cached audit), intersects with cfg_write_grant (writer='purge.execute') so only explicitly allow-listed tables are ever touched. -Preview (default true) counts only, nothing written. -Live actually deletes every soft-deleted row in each granted-and-currently-safe table, one transaction per database, and verifies each table reads back 0 soft-deleted rows afterward. A table that is UNSAFE or ungranted is always skipped and reported, never silently included. |
| 2 | purge.retire_database | iba.app.handlers.purge:retire_database | none | Physically clears every row from every table cfg_table marks inactive=1 for the given -Database (default bible_research) -- scope read live from cfg_table every run, never a hardcoded list. Before clearing, nulls known FK columns on RETAINED active tables that point into the cleared set, so no kept row is left dangling. -Preview (default true) counts only, nothing written. -Live actually deletes, one transaction, verifying each table reads back 0 rows afterward. |

**raw-backfill** — runs over `book` · script `iba/app/ps/Raw-Backfill.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | raw.backfill_meaning | iba.app.handlers.raw:backfill_meaning | book | for a book (optionally narrowed to one chapter's verse range via -Range C:V-V), find every distinct strong its spans reference that has no strong row yet, and pull ONLY the meaning (STEP getInfo -> strong/strong_sense/strong_meaning_tree/strong_lexicon) -- not verses. Reuses raw.detail_one() unchanged. Progressive, passage-driven DB coverage growth, not a full-Bible bulk pull. Cluster-reconciles every newly-backfilled code inline (the only chain these codes ever pass through). UPDATED 2026-09-15 (escalation #1606): fails (condition='unclassified') if any newly-backfilled code got no cluster assignment at all, rather than always returning ok(). |

**registry-report** — runs over `none` · script `iba/app/ps/Registry-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.registry | iba.app.handlers.reports:registry_report | none | evaluate/review word_registry -- summary, join to strong, sense report grouped by gloss |

**reports** — runs over `none` · script `iba/app/ps/Reports.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.word | iba.app.handlers.reports:word_report | word | the word-raw report (report.py) — content governed by report.* settings |
| 1 | validation.word | iba.app.handlers.reports:validation_word | word | the raw-layer validation report (validation.py) — sections governed by validation.show_* |
| 2 | validation.book | iba.app.handlers.reports:validation_book | book | the base-layer validation report (validation.py) — sections governed by validation.show_* |

**schema-overview-report** — runs over `none` · script `iba/app/ps/SchemaOverview-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.schema_overview | iba.app.handlers.reports:schema_overview_report | none | the IBA app's own data-schema snapshot — every data table, columns, types, PK/FK, indexes, row counts |

**schema-overview-report-bible-research** — runs over `none` · script `iba/app/ps/SchemaOverview-BibleResearch-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.schema_overview_bible_research | iba.app.handlers.reports:schema_overview_bible_research_report | none | bible_research.db data-schema snapshot -- every table, columns, types, PK/FK, indexes, row counts |

**seed-candidate-report** — runs over `none` · script `iba/app/ps/archive/SeedCandidate-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.seed_candidate | iba.app.handlers.reports:seed_candidate_report | none | whole-seed candidate_seed analysis — counts by decision/layer/role, tag/lemma distribution, busiest lemmas, open-vs-resolved over time |

**session-close** — runs over `none` · script `iba/app/ps/Session-Close.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | session.close | iba.app.handlers.session_close:check | none | read-only session-close detection (#1875, rebuilt #2173 SC1-SC14): session and window (fails without them); spine FATAL first; researcher's words recorded in escalation comments; open items in the register; analysis integrity (chapter changes recorded, quotes checked, register findings new or standing on touched chapters, reading placements); rule compliance evidence; session log and its decisions' targets; BUILD.md naming every changed code/config file; publish flags. Findings are cleared only by a fix or a checked disposition; Session-Close.ps1 exits 3 (commit blocked) while any is open. |

**session-compliance** — runs over `none` · script `iba/app/ps/Compliance.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | compliance.template | iba.app.handlers.compliance:template | none | #2173 P2: writes this session's compliance file, one row per active governance setting, behaviour rule and escalation rule (never overwrites) |
| 1 | compliance.check_start | iba.app.handlers.compliance:check_start | none | #2173 P2 B/C: every rule restated or 'not engaged' with a reason, none copied, the acknowledgement, every rule naming a retired thing named in the conflicts section |

**set-candidates** — runs over `book` · script `iba/app/ps/archive/Set-Candidates.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.seed | iba.app.handlers.archive.candidate:seed | global | refresh candidate_seed over lemma_inventory (independent net + registry-direct + config); recompute registry_match (the double control) |
| 1 | candidate.set | iba.app.handlers.archive.candidate:set | book | stamp span_candidate on the book's spans whose base-strong is a candidate |

**span-analysis-report** — runs over `none` · script `iba/app/ps/SpanAnalysis-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.span_analysis | iba.app.handlers.reports:span_analysis_report | none | span layer coverage per book, confirmed (span) vs candidate (span_candidate) counts, morph-code distribution |

**spine-check** — runs over `none` · script `iba/app/ps/Spine-Check.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | spine.check | iba.app.handlers.spine:check | none | read-only check of the base-data spine (governance.base_data_spine): span -> strong, verse <-> span, strong -> cluster, and strong -> meaning (strong_sense, strong_meaning_tree, strong_lexicon; each local gap asked of STEP: content in STEP that the table lacks is FATAL, nothing in STEP is a gap by design). Persists a report every run; escalates only on a FATAL finding. Run by session-close (SC2), not at start (#2173 P3). The parse tables stay retired. See handlers/spine.py. |

**strand-reading** — runs over `none` · script `iba/app/ps/Strand-Reading.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | strand_reading.define | iba.app.handlers.strandreading:define | none | a strand: its code, title, cluster, escalation and word family (-Strongs); adds words to an open strand -- see lib/strandreading.py (escalation #2172) |
| 1 | strand_reading.context | iba.app.handlers.strandreading:context | none | step 1: every hit with its text and lexical data, the observations already on those words and verses, each verse's coverage; every open thread item matching the strand's words, their clusters, its verses or its code recorded as an item to answer -> the context file -- see lib/strandreading.py (escalation #2172, #2219) |
| 2 | strand_reading.record | iba.app.handlers.strandreading:record | none | step 2: the reading recorded -- observations (grounded, quote-checked), a face or a reason per hit read, new open items found (raised on the strand's thread); read verses marked analysed -- see lib/strandreading.py (escalation #2172, #2219) |
| 3 | strand_reading.gather | iba.app.handlers.strandreading:gather | none | step 3: every narrative block related to the strand, with its text and tellings (read-only) -- see lib/strandreading.py (escalation #2172) |
| 4 | strand_reading.map | iba.app.handlers.strandreading:map_blocks | none | step 4: each related block's statements mapped to the claims register; an unclaimed statement becomes a new claim or an open item on the strand's thread -- see lib/strandreading.py (escalation #2172, #2219) |
| 5 | strand_reading.derive | iba.app.handlers.strandreading:derive | none | step 5: new, adjusted and withdrawn claims, each resting on observations or verses; each observation's disposition (held: an existing open item or a new one raised on the strand's thread) -- see lib/strandreading.py (escalation #2172, #2219) |
| 6 | strand_reading.rewrite | iba.app.handlers.strandreading:rewrite | none | step 6: blocks written anew, whole (every claim a block told accounted for); the chapters published from the database; cited verses marked citated -- see lib/strandreading.py (escalation #2172) |
| 7 | strand_reading.account | iba.app.handlers.strandreading:account | none | step 7: the strand from the tables, gaps as text (read-only), its open items with their answers; the same facts are the close gate -- see lib/strandreading.py (escalation #2172, #2219) |

**strong-meaning-report** — runs over `none` · script `iba/app/ps/StrongMeaning-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.strong_meaning | iba.app.handlers.reports:strong_meaning_report | none | meaning-parse layer coverage — strong/strong_sense/strong_meaning_tree/strong_lexicon gap list, sense-count distribution, lexicon completeness |

**strong-verse-report** — runs over `word` · script `iba/app/ps/StrongVerse-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.strong_verse | iba.app.handlers.reports:strong_verse_report | word | on-demand verse restatement for one Strongs reference (verse_lexical.strong exact match, whole Bible) in the context of a registry word -- inline-annotated, exact-variant senses only, combined-tag/empty-surface spans and unresolved collisions explicitly handled, never silently guessed |

**table-export** — runs over `none` · script `iba/app/ps/Export-Tables.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | table.export | iba.app.handlers.reports:table_export | none | CSV dump of every data table, verbatim — excludes cfg_* (configmaint.report already owns that content) |

**verse-analysis-report** — runs over `book` · script `iba/app/ps/archive/VerseSpanMeaning-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.verse_span_meaning | iba.app.handlers.reports:verse_span_meaning_report | book | verse : span : meaning extract for a book/chapter-range — per-span meaning from all three parse tables (meaning_tree/lsj/mounce), live STEP disambiguation for AMBIGUOUS (sibling-shared-base) spans |

**verse-lexical** — runs over `book` · script `iba/app/ps/VerseLexical.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | lexical.build | iba.app.handlers.lexical:build | book | verse : verse_lexical extract — mechanical T1-T3 engine: for every code in a span's (possibly compound) strong_variant, classifies role (content lexical entry vs. grammatical formative), stem/voice-selects the operative sense from strong_meaning_parsed via morph_code (not the whole six-stem/voice paradigm), and flags — never resolves — the sibling/base-fallback ambiguity case versespanmeaningreport.meaning_for_code already detects. Runs independent of T4-T9/passage_debate. Version-aware: soft-deletes the superseded row and inserts fresh on rewrite, same convention every other iba.db table already uses. Replaces report.verse_span_meaning (retired, see BUILD.md).; from this build onward, also denormalizes position/surface/language/testament and computes is_negator/narrative_morph/gloss_consistent_in_verse/party_kind via cfg_lexical_code_class lookups, unconditionally for every row, no selection (method-and-drift-mitigation doc §2 Layer 1). Also applies the H0853 classify_role exception (design doc §4). |
| 0 | lexical.readiness | iba.app.handlers.lexical:readiness | none | 3-leg read-only precondition check for the Layer 1 rebuild (#1606): Leg1 every live verse has >=1 live span; Leg2 every live span's strong_variant code resolves to a live strong row (duplicates spine.check's own desync check deliberately -- #1606's own framing is one cohesive 3-leg check); Leg3 every live strong that actually occurs in a live span has >=1 live cluster_strong allocation (the precondition Layer 1's redesigned role column, a JSON array of cluster_strong.cluster_code, depends on directly). Persists a report every run (governance.reports_must_persist), fails on any FATAL finding. |
| 1 | report.verse_lexical | iba.app.handlers.reports:lexical_report | book | on-demand MD report, generated from verse_lexical (never an independent write) — EV verse text and the resolved lexical reading placed together, per book/passage range. Requires verse_lexical.build to have already run for this exact range. |
| 2 | lexical.enrich | iba.app.handlers.lexical:enrich | passage | Stage 1 Layer 2 — JSON-payload-driven, one passage-block at a time (≤20 verses). Writes verse_lexical_note rows and passage.genre; sets passage.lexical_complete_at once every applicable code in the block has a disposition. Requires lexical.build to have already run for every verse in the block. RETIRED 2026-09-16 (#1706 Phase B): this verse_lexical_note-based mechanism is superseded by the new ib_observation architecture (#1597 resolution-by-architecture, #1691/#1692 design-complete). Code kept, not deleted — lexicalenrichgenerate.py's LLM-calling infrastructure is being adapted for the new Layer 2 verse_meaning stage (#1711), not thrown away. |
| 3 | report.lexical_exceptions | iba.app.handlers.reports:lexical_exceptions_report | passage | Per-run exception report — every unresolved/unclassified/checked_empty/UNCLASSIFIED-connective disposition and every genuine judgement call from the most recent lexical.enrich run for this passage, laid out for researcher review. Read-only against verse_lexical/verse_lexical_note, never an independent write. |
| 4 | report.lexical_extract | iba.app.handlers.reports:lexical_extract | none | Multi-filter JSON extract over verse_lexical/verse_lexical_note — passage/verse/surface/strong/lemma filters, each accepting a list or range. Read-only, JSON output, feeds Phase 2 (Stage 2) input assembly. |
| 5 | lexical.run | iba.app.handlers.lexical:run | verse | The real front door for Window 1 (escalation #1549 rework, 2026-09-07 -- researcher: 'it is fundamentally built on books and passages which contradicts the analytic operation for clusters and groups of strongs'). Exactly one selector (-ClusterCode via cluster_strong, -StrongList direct, -Word via word_strong, or -VerseList a known OSIS list) resolves to a strong-list then a verse-list via span.strong_variant (exact-token match, NOT strong_verse -- that table undercounts, verified live). -Mode picks the work: Layer1AndLayer2, Layer1Only, or Layer2Only -- verse-list resolution happens once regardless of mode; Layer 2 always sources its scope from Layer 1's own resolved ids, never re-resolves. Layer 1's write (build_for_verse_ids) is identity-stable -- safe no-op on unchanged verses, never orphans a live Layer 2 note. Whenever -Mode includes Layer 2, the lexical.notes briefing pack is produced by default before any write is attempted (-SuppressNotes opts out). If -PayloadPath is given, that payload is written. If NOT given (and -NoAutoLLM is NOT given), lexical.run now AUTOMATICALLY calls an LLM to produce the payload -- researcher instruction 2026-09-07: 'layer 2 will consume llm and it must be part of the routine, rather than parking it'. Batched by passage.max_verses per live API call, each call cost-estimated and hard-capped by lexical.llm_max_cost_per_batch before it fires, real usage logged to lexical.llm_usage_log_path. -NoAutoLLM opts out to the old notes-briefing-only behaviour. lexical.run_max_verses caps the whole resolved scope before any work starts. |
| 6 | lexical.meaning | iba.app.handlers.lexical:meaning | cluster | The verse-reading stage, WORD-LEVEL HALF (#1711 original build; narrowed to word-level-only by the #1860 split, 2026-09-23): per-cluster, pre-subgroup Layer 2. Reads all 3 meaning sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) as complementary evidence for every strong the cluster's role-annotated word list covers (verse_lexical.role, including currently-unwired role-T2/T6/T10-T15 tags, not just the mechanically-wired subset), and answers M0.1 (Name and Naming) and M0.5 (Lexical and Semantic Analysis, incl. M0.5.11) from wa_obs_question_catalogue -- word-level only now; the relational family (M0.6.5/M0.6.6/D7.7.1/M0.7/M0.8.1) moved to the new lexical.relational step, which requires this step's own output as a precondition (readiness gate). Assembles the LLM payload and estimates cost; the live API call and the DB write are separate, explicit steps (cost preview before spend, never silent). |
| 7 | lexical.relational | iba.app.handlers.lexical:relational | cluster | The verse-reading stage, RELATIONAL HALF (#1860 split, 2026-09-23 -- researcher, verbatim: 'we must split the word questions and answers and the relational answers into separate processes. the relational process depends on the word work, and doing it in the same session can only result in errors.'). Per-cluster, pre-subgroup Layer 2, run AFTER lexical.meaning has covered the same verses -- a hard readiness gate refuses to run against any verse whose M-code words don't all have a committed word-level (M0.1/M0.5) observation yet. Answers M0.6.5 (relational, single-vantage), M0.6.6 (whole-network synthesis), D7.7.1 (operation-anchored permeability), M0.7.1-16 (verse substantiation), M0.8.1 (T2/T3 elevation flag), cluster-agnostic (every M-code word in the verse, not just this cluster's own home strong(s)). Grounds on the COMMITTED word-level ib_observation rows for each verse+strong (the researcher's own approval, #1860 v3: 'the base data must in any case be included for relational phase to be successful' -- so the raw lexicon (meaning_sources_by_strong) is ALSO sent alongside the committed findings, never one instead of the other). This is the true final stage of verse-reading -- the cluster.status t_cluster_assignment_completed -> ready_for_subgroup_allocation transition check runs here now, not in lexical.meaning. |

**verse-meta** — runs over `none` · script `iba/app/ps/VerseMeta.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | verse_meta.set_status | iba.app.handlers.versemeta:set_status | none | sets verse_meta.status (cfg_enum verse_meta_status) for a comma-delimited list of verse references; stamps status_changed_at only on a real change (#1661; #2207: through run.py) |

**whole-book-read** — runs over `book` · script `iba/app/ps/WholeBookRead-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.whole_book_read | iba.app.handlers.reports:whole_book_read_report | book | whole-book-read gathering report — for a book whose passage debates are (wholly or partly) filled, pulls every debate_status='filled' passage row in reading order, reads each debate file, extracts its Emergent-questions and Passage-level-linkages sections (tolerant heading match, explicit NOT-FOUND if a file's headings don't match), and lays them out per-passage with an empty Resolution slot for the researcher/AI to fill in; does not decide how any emergent question actually resolves itself |

**word-audit** — runs over `word` · script `None`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | word.load_json | iba.app.handlers.archive.wordaudit:load_json | word | Load + validate latest Step 1 JSON + structural completeness check (merged from old A2/A3) |
| 1 | word.confirm | iba.app.handlers.archive.wordaudit:confirm | word | Registry display + CONFIRM prompt |
| 2 | word.gap_report | iba.app.handlers.archive.wordaudit:gap_report | word | Build gap report (Term/Related/Verse/VTL streams) |
| 3 | word.gap_display | iba.app.handlers.archive.wordaudit:gap_display | word | Display gap report (+ interactive approve gate) |
| 4 | word.apply_changes | iba.app.handlers.archive.wordaudit:apply_changes | word | Apply changes, one transaction per stream |
| 5 | word.meaning | iba.app.handlers.archive.wordaudit:meaning | word | Meaning handler -- parse + migrate legacy fields |
| 6 | word.flag_reset | iba.app.handlers.archive.wordaudit:flag_reset | word | Quality flag reset (DATA_COVERAGE), re-derive |
| 7 | word.audit_checks | iba.app.handlers.archive.wordaudit:audit_checks | word | WR-01-WR-20 + write word_run_state (PROVISIONAL) |
| 8 | word.registry_close | iba.app.handlers.archive.wordaudit:registry_close | word | Registry + file-index update, last_automation_run='AUDITED' |
| 9 | word.export | iba.app.handlers.archive.wordaudit:export | word | Full-word JSON export |

**word-registry-span-report** — runs over `word` · script `iba/app/ps/archive/WordRegistrySpan-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.word_registry_span | iba.app.handlers.reports:word_registry_span_report | word | word_registry : word_strong : strong : strong_meaning_parsed : verse_lexical : span analysis, for one registry word — every linked Strong's with its parse-meaning breakdown and unique surface-span applications (with an example verse) — read-only |

<a id="7-on-fail-condition-path-the-fork-rules"></a>
## 7. on_fail — condition -> path (the fork rules)

**20 of 105 conditions ESCALATE** (pause-continue — the researcher is asked); the rest either stop the run outright (report-stop) or continue with a logged warning (report-continue). Per the researcher's 2026-07-21 rule: any finding that needs a judgement call must be in the first group, not silently in the second or third.

### 5a. Escalates (pause-continue) — the researcher is asked, every time
| step | condition | message |
| --- | --- | --- |
| candidate.curate | needs-approval | a candidate_seed correction needs researcher approval |
| candidate.load | needs-review | candidate.load has unresolved exception row(s) in candidate_seed needing researcher judgement |
| candidate.validate | needs-review | span_candidate has tag/lemma_key quality findings needing researcher judgement |
| cluster.validate | needs-review | cluster-assignment exceptions need researcher judgement |
| configmaint.propose | needs-approval | a config change needs researcher approval |
| configmaint.validate | needs-review | cfg_* has advisory findings (orphans/needs-justification) needing researcher judgement |
| lexicon.validate | needs-review | lexicon-parse coverage/value-quality findings need researcher judgement |
| passage.validate | needs-review | passage verse_count distribution needs researcher judgement |
| raw.backfill_meaning | unclassified | a backfilled strong got no cluster assignment at all -- same class of gap as strong.reconcile, must not silently continue (escalation #1606). |
| raw.detail | no-vocab | a strong returned no vocab from STEP — missing lexical data, worth a decision, not a silent continue |
| raw.discover | zero-strongs | the word maps to no strongs — a researcher question |
| raw.verses | shortfall | STEP returned fewer rows than its own reported total — the exact class of bug BUILD.md §5 found; must not silently continue |
| registry.create | needs-approval | a new word needs researcher approval |
| report.book_narrative_generate | needs-approval | researcher approval required before the live API call is made |
| spine.check | spine-fatal-found | spine has FATAL findings needing researcher judgement |
| strong.reconcile | unclassified | a strong got no cluster assignment at all (no HIGH-confidence precedent match) -- a researcher/Claude classification decision, not silently continuing (escalation #1606). |
| validation.book | needs-review | validation findings need researcher judgement |
| validation.word | needs-review | validation findings need researcher judgement |
| word.confirm | needs-confirmation | word display shown; confirm to proceed |
| word.gap_display | needs-approval | gap report shown; approve to apply (only when run --interactive) |

### 5b. Does not escalate — report-stop (hard fail) or report-continue (logged, no ask)
| step | condition | path | message |
| --- | --- | --- | --- |
| candidate.curate | change-rejected | report-stop | researcher rejected the proposed candidate_seed correction |
| candidate.curate | invalid-proposal | report-stop | the proposed correction failed validation -- never escalated |
| candidate.curate | needs-revision | report-stop | researcher asked for revision (see comment) and resubmission |
| candidate.seed | no-inventory | report-stop | lemma_inventory is empty — run the seed migration first |
| candidate.set | no-spans | report-stop | the book has no spans — build its words first |
| candidate.validate | findings-rejected | report-stop | researcher flagged candidate quality findings as needing action |
| candidate.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| cluster.validate | findings-rejected | report-stop | researcher flagged cluster-assignment exceptions as needing action |
| cluster.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| compliance.check_start | findings-open | report-continue | the compliance file does not pass the start check -- fix it and re-run (Compliance.ps1 exits 3) |
| compliance.check_start | no-session | report-continue | the session could not be identified -- see the message |
| compliance.template | no-session | report-continue | the session could not be identified -- see the message |
| configmaint.propose | change-rejected | report-stop | the researcher rejected the proposed change |
| configmaint.propose | invalid-proposal | report-stop | the proposed change fails a coherence check — never escalated |
| configmaint.propose | needs-revision | report-stop | the researcher asked for the proposal to be revised (see the comment) and resubmitted |
| configmaint.validate | findings-rejected | report-stop | researcher flagged advisory findings as needing action, not acknowledgement |
| configmaint.validate | invalid | report-stop | the live cfg_* store is incoherent |
| configmaint.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| escalation.history | bad-parameter | report-continue | usage error, not recorded as an escalation -- check -Id (id or OT-nn) |
| escalation.thread | bad-parameter | report-continue | usage error, not recorded as an escalation -- check -Id (id or OT-nn) and -State (on-hold\|in-progress) |
| lexical.build | unreachable | report-stop | STEP is down and step.required_for_runs is true — cannot resolve any content-role code's sense without it. |
| lexicon.related | unreachable | report-stop | STEP is not reachable — lexicon.related cannot fetch relatedNos at all |
| lexicon.validate | findings-rejected | report-stop | researcher flagged lexicon-parse quality findings as needing action |
| lexicon.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| narrative_register.add_chapter | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.add_claim | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.check | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.edit | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.edit_chapter | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.edit_note | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.edit_section | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.export | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.find | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.history | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.quote_check | quotes-failing | report-continue | quotations not found in the ESV text -- correct them, or disposition each at session-close |
| narrative_register.quote_check | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.record | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.tell | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.untell | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| narrative_register.withdraw | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| passage.build | no-candidates | report-stop | the book has no candidate spans — run set-candidates first |
| passage.validate | findings-rejected | report-stop | researcher flagged the passage distribution as needing the rule revisited |
| passage.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| raw.backfill_meaning | invalid-range | report-stop | the -Range value could not be parsed |
| raw.backfill_meaning | unreachable | report-stop | STEP is not reachable — cannot pull any meaning |
| raw.discover | follow-related-not-built | report-stop | discovery.follow_related is true but relatedNos expansion was never implemented |
| raw.validate | parse-mismatch | report-stop | span does not recover strong_verse |
| registry.create | word-rejected | report-stop | the researcher rejected the word |
| registry.exists | word-exists | report-stop | the word already exists; use a refresh run, not new-word |
| report.book_narrative_generate | api-error | report-stop | the Messages API returned a non-2xx response |
| report.book_narrative_generate | api-key-missing | report-stop | ANTHROPIC_API_KEY not found in the environment or repo-root .env |
| report.book_narrative_generate | cost-cap-exceeded | report-stop | the pre-call cost estimate exceeds narrative.generate_max_cost |
| report.book_narrative_generate | declined | report-stop | researcher rejected the escalation |
| report.book_narrative_generate | guidance-doc-missing | report-stop | a method.* cfg_setting points to a file that does not exist on disk |
| report.book_narrative_generate | needs-revision | report-stop | researcher asked for a change first (see comment) |
| report.book_narrative_generate | no-debates-found | report-stop | no filled report.passage_debate exists yet for this book |
| report.book_narrative_validate | guidance-doc-missing | report-stop | method.inner_being_narrative_guidance_path points to a file that does not exist on disk — the config is stale relative to iba/docs/ |
| report.book_narrative_validate | narrative-file-missing | report-stop | the given -Path does not exist on disk |
| report.book_narrative_validate | no-path-given | report-stop | -Path is required — the narrative file to check |
| report.book_narrative_validate | scope-check-incomplete | report-stop | one or more required channel labels are missing or left as an unfilled placeholder |
| report.book_narrative_validate | scope-check-missing | report-stop | no '## Scope self-check' section found — add one per the guidance doc section 3 |
| report.strong_verse | strong-not-linked | report-stop | the requested Strongs code is not linked to this registry word (word_strong) |
| report.strong_verse | word-not-found | report-stop | the requested word is not in the registry |
| report.verse_lexical | no-readings | report-stop | no verse_lexical rows exist yet for this exact book/range — run lexical.build first (it is ordinal 0 of this same work package, run automatically before this step unless called standalone). |
| report.whole_book_read | no-debates-found | report-stop | no debate_status='filled' passage row exists yet for this book — run at least one report.passage_debate pass and fill it in first |
| report.word | word-not-found | report-stop | the requested word is not in the registry |
| report.word_registry_span | word-not-found | report-stop | the requested word is not in the registry |
| session.close | findings-open | report-continue | session-close found open findings -- the commit is blocked until each is fixed or carried (Session-Close.ps1 exits 3); remediation is Claude's, not an approval cycle |
| session.close | gaps-found | report-continue | session-close detected one or more gaps — see report for detail; remediation is Claude's own follow-up via .claude/commands/session-close.md, not a blocking approval cycle |
| spine.check | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| spine.check | spine-fatal-rejected | report-stop | researcher flagged FATAL spine findings as needing action |
| strand_reading.account | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.context | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.define | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.derive | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.gather | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.map | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.record | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| strand_reading.rewrite | refused | report-continue | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |
| validation.book | findings-rejected | report-stop | researcher flagged the validation findings as needing action, not just acknowledgement |
| validation.book | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| validation.word | findings-rejected | report-stop | researcher flagged the validation findings as needing action, not just acknowledgement |
| validation.word | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| verse_meta.set_status | bad-parameter | report-continue | usage error, nothing written, not recorded as an escalation -- -Status must be a live value of cfg_enum verse_meta_status |
| verse_meta.set_status | not-found | report-continue | one or more references not found (the rest were set), not recorded as an escalation -- check the references listed |

<a id="8-write-grants-who-may-write-what"></a>
## 8. Write grants — who may write what

| writer | tables |
| --- | --- |
| call1_meanings | word_strong |
| call2_getInfo | strong, strong_lexicon, strong_meaning_tree, strong_sense |
| call3_strong | span, strong_verse, verse |
| candidate.curate | candidate_seed |
| candidate.load | candidate_seed |
| candidate.seed | candidate_seed, lemma_inventory |
| candidate.set | span_candidate |
| closing.set | debate_change_detail, passage, passage_emergent_question, passage_insufficiency, passage_linkage, passage_validation_note |
| cluster.answer | ib_node, ib_observation, run_batch |
| cluster.assign | cluster_strong |
| cluster.reading | ib_node, ib_observation, run_batch |
| cluster.subgroup | cluster_subgroup, cluster_subgroup_strong, ib_node, ib_observation, run_batch |
| configmaint.propose | cfg_api, cfg_behaviour_class, cfg_behaviour_rule, cfg_book_order, cfg_candidate_rule, cfg_change_detail, cfg_change_log, cfg_column, cfg_connection, cfg_content_index_exclude, cfg_content_index_size_override, cfg_control_home, cfg_enum, cfg_escalation, cfg_escalation_requirement, cfg_escalation_transition, cfg_index, cfg_lexical_code_class, cfg_meta, cfg_method_rule, cfg_observation_enhancer_rule, cfg_on_fail, cfg_passage, cfg_prose, cfg_prose_concept, cfg_quality_check, cfg_report, cfg_report_csv_table, cfg_report_section, cfg_rule_scope, cfg_setting, cfg_status_flow, cfg_step, cfg_table, cfg_table_purpose, cfg_trigger, cfg_unique, cfg_utility, cfg_work_package, cfg_write_grant |
| escalation | escalation, escalation_history, escalation_thread_item, escalation_thread_item_response, word_registry |
| hib.set | debate_change_detail, hib, hib_referent_option, verse_hib |
| lexical.build | verse_lexical |
| lexical.enrich | passage, verse_lexical_note |
| lexical.meaning | ib_node, ib_observation, run_batch |
| lexical.relational | ib_node, ib_observation, run_batch |
| lexical.run | verse_lexical, verse_lexical_note |
| lexicon.parse | strong_lsj_parsed, strong_meaning_parsed, strong_mounce_parsed |
| lexicon.related | strong_related |
| migration | candidate_seed, cluster, cluster_strong, lemma_inventory, narrative_chapter, narrative_citation, narrative_claim, narrative_claim_change, narrative_claim_source, narrative_claim_telling, narrative_index_note, narrative_passage, narrative_section, narrative_update, narrative_update_ref, span, strong, strong_lexicon, strong_lsj_parsed, strong_meaning_parsed, strong_meaning_tree, strong_mounce_parsed, strong_related, strong_sense, word_registry, word_strong |
| narrative_register.add_chapter | narrative_chapter, narrative_claim_change, narrative_section, narrative_update |
| narrative_register.add_claim | narrative_claim, narrative_claim_change, narrative_claim_source |
| narrative_register.edit | narrative_claim, narrative_claim_change, narrative_claim_source |
| narrative_register.edit_chapter | narrative_chapter, narrative_claim_change, narrative_update |
| narrative_register.edit_note | narrative_index_note |
| narrative_register.edit_section | narrative_chapter, narrative_claim_change, narrative_claim_telling, narrative_passage, narrative_section |
| narrative_register.record | narrative_chapter, narrative_citation, narrative_claim, narrative_claim_change, narrative_claim_source, narrative_claim_telling, narrative_passage, narrative_section, narrative_update, narrative_update_ref |
| narrative_register.tell | narrative_claim, narrative_claim_change, narrative_claim_telling, narrative_passage |
| narrative_register.untell | narrative_claim, narrative_claim_change, narrative_claim_telling |
| narrative_register.withdraw | narrative_claim, narrative_claim_change |
| observation_enhancer.apply | cfg_observation_enhancer_rule, ib_observation, ib_observation_enhancer_log |
| operation.set | debate_change_detail, operation, operation_party |
| passage.build | debate_change_detail, passage, verse_passage |
| phenomenon.set | debate_change_detail, passage, phenomenon |
| purge.execute | candidate_seed, cluster, cluster_strong, hib, hib_referent_option, operation, operation_party, passage, passage_emergent_question, phenomenon, span, strong, strong_lexicon, strong_meaning_tree, strong_related, strong_sense, verse_hib, verse_passage, wa_obs_question_catalogue, word_strong |
| raw.validate | validation_result |
| raw.write | word_registry |
| registry.create | word_registry |
| report.debate | passage |
| run | escalation, run, validation_result, word_registry |
| strand_reading.context | reading_strand_hit, reading_strand_item |
| strand_reading.define | reading_strand, reading_strand_strong |
| strand_reading.derive | ib_observation, narrative_claim, narrative_claim_change, narrative_claim_source, narrative_claim_telling, reading_strand, reading_strand_item |
| strand_reading.map | narrative_claim, narrative_claim_change, narrative_claim_source, narrative_claim_telling, reading_strand, reading_strand_item |
| strand_reading.record | ib_node, ib_observation, reading_strand, reading_strand_hit, reading_strand_item, verse_meta |
| strand_reading.rewrite | narrative_chapter, narrative_citation, narrative_claim_change, narrative_claim_telling, narrative_section, narrative_update, narrative_update_ref, verse_meta |
| strong.reconcile | strong |
| verse_meta.set_status | verse_meta |

<a id="9-status-flow"></a>
## 9. Status flow

| entity | order | status | set_by |
| --- | --- | --- | --- |
| escalation | 0 | raised | initial state at Raise (escalation.raise_/raise_new) |
| escalation | 1 | in-progress | either party directly (Update state=in-progress); OR system: next_action=revise; OR dispatcher-tied answer_for_run decision=revise (escalation #795 fix, 2026-08-22); OR system (thread, T3/T5): an open escalation item references in-progress work (escalation #2000) |
| escalation | 2 | on-hold | either party directly (Update state=on-hold); OR dispatcher-tied answer_for_run decision=hold; OR system (thread, T6): items partly settled (closed, withdrawn or superseded) and no in-progress work references the thread (escalation #2000) |
| escalation | 3 | re-assigned | system: next_action_assigned_to changed, no more specific rule matched (Update); OR: manual next_action=approved+needs_claude_followup flag set -- routes back to Claude instead of completed (escalation #1075) |
| escalation | 4 | closed | either party directly (Update state=closed); OR system: next_action=noted (manual) or decision=noted (dispatcher-tied) |
| escalation | 5 | withdraw | party's explicit choice at Update: next_action=reject, state=withdraw; OR: dispatcher-tied answer_for_run decision=reject (escalation #795 fix, 2026-08-22) |
| escalation | 6 | supersede | party's explicit choice at Update: next_action=reject, state=supersede |
| escalation | 7 | completed | system: manual next_action=approved+resolution present; OR: dispatcher-tied answer_for_run decision=approve; OR system (thread: every item settled -- closed, withdrawn or superseded -- after an item change; escalation #2000 lifecycle) |
| prose_section | 0 | draft | apply_session_patch.py: prose_section insert/supersede/bulk_supersede (caller-supplied, the default when omitted) |
| prose_section | 1 | in_review | apply_session_patch.py: prose_section insert/supersede (caller-supplied status -- no dedicated transition op exists; 0 rows currently at this status) |
| prose_section | 2 | approved | apply_session_patch.py: prose_section approve (the one dedicated transition op -- also stamps approved_at/approved_by) |
| prose_section | 3 | archived | apply_session_patch.py: prose_section insert (caller-supplied status only -- 11 existing rows were archived at insert time, not via a transition op) |
| word | 0 | proposed | registry (on new word, before approval) |
| word | 1 | approved | registry.create |
| word | 2 | raw-complete | raw.write |
| word | 3 | signed-off | registry.signoff (not in this slice) |
| word | 4 | rejected | escalation (researcher declines) |

<a id="10-schema-data-tables-built-from-config"></a>
## 10. Schema — data tables built from config

### word_registry
_one row per English inner-being word_ — the study's entry point; scope of a new-word run
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| word | TEXT |  | ✓ | ✓ |  | the English word | run.param.Word |
| source | TEXT |  |  |  |  | why it was registered — the growth trigger | run.param.Source |
| status | TEXT |  |  |  |  | registry processing stage | registry+raw+signoff |
| created_at | TEXT |  |  |  |  | when registered | registry.create |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### word_strong
_one row per (word, strong) the STEP word-search returned_ — L1 — the discovery record: which strongs a word maps to. These strongs are the basis for L2. Carries the link only, no strong detail.
dedup key: `word_id, strong`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| word_id | INTEGER |  | ✓ |  | word_registry.id | the word | run.context.word_id |
| strong | TEXT |  | ✓ |  | strong.strongNumber | a strong the word returned | call1.definitions[].strongNumber |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong
_one row per strong — unique, global to the study_ — L2 — the strong's identity. The meaning is normalised out (O4): it lives in strong_sense / strong_meaning_tree / strong_lexicon.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strongNumber | TEXT | ✓ |  |  |  | the resolved Strong's code — the key | call2.vocabInfos[0].strongNumber |
| accentedUnicode | TEXT |  |  |  |  | the actual Hebrew/Greek word | call2.vocabInfos[0].accentedUnicode |
| stepGloss | TEXT |  |  |  |  | short English sense | call2.vocabInfos[0].stepGloss |
| stepTransliteration | TEXT |  |  |  |  | romanised form; never shown without the gloss | call2.vocabInfos[0].stepTransliteration |
| language | TEXT |  |  |  |  | Hebrew/Greek from the code prefix | derived:call2.strongNumber |
| count | INTEGER |  |  |  |  | STEP token frequency — NOT a verse count, may be capped | call2.vocabInfos[0].count |
| freqList | TEXT |  |  |  |  | raw frequency distribution | call2.vocabInfos[0].freqList |
| created_at | TEXT |  |  |  |  | when first fetched | raw.detail |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| origin | TEXT |  | ✓ |  |  | 'word' = deliberately onboarded for a registry word (raw.discover -> word_strong -> raw.detail); must carry the full raw-data-integrity chain. 'backfill' = onboarded by raw.backfill_meaning's book-scoped completeness sweep, independent of any word; not in scope for cluster/meaning-relevance mapping, used only to support lexical resolution. Sticky: an upgrade backfill->word can happen (a later word legitimately claims the code); never downgraded. | migrated:one-time classification, then stamped by detail_one() going forward |

### strong_sense
_one row per strong — the sense HEAD_ — the span's meaning, read constantly. The head is the first line of mediumDef (the sense); is_own_lemma marks a code that is its own lemma, where the gloss carries the sense.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  |  | strong.strongNumber | the strong |  |
| head | TEXT |  |  |  |  | the sense — THE SPAN'S MEANING | derived:call2.mediumDef.head |
| is_own_lemma | INTEGER |  |  |  |  | 1 = no ': ' head; the code is its own lemma and the gloss is the sense | derived:call2.mediumDef |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_meaning_tree
_one row per sense-node of a LEMMA's definition tree_ — the lemma's full range — read rarely, only when the broader context is needed. Keyed on the lemma (shared across its senses, which the prototype proved).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  |  | the base code the tree belongs to | derived:call2.strongNumber.base |
| sense_code | TEXT |  |  |  |  | the tree position: 1), 1a), 1b1) | derived:call2.mediumDef.tree |
| sense_text | TEXT |  |  |  |  | the sense line | derived:call2.mediumDef.tree |
| sort | INTEGER |  |  |  |  | order within the tree | derived:call2.mediumDef.tree |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| strong_variant |  |  |  |  | strong.strongNumber |  |  |

### strong_lexicon
_one row per strong that has LSJ/Mounce (Greek)_ — the large lexicon text — separate because rarely scanned
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  |  | strong.strongNumber | the strong |  |
| lsj | TEXT |  |  |  |  | LSJ entry (Greek) | call2.vocabInfos[0].lsjDefs |
| mounce | TEXT |  |  |  |  | Mounce short def (Greek) | call2.vocabInfos[0].shortDefMounce |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### verse
_one row per verse — unique. Does NOT belong to a strong._ — L3 — the addressable verse. preview is the full interlinear, kept verbatim so span is re-derivable.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| osisId | TEXT |  | ✓ | ✓ |  | the machine key, e.g. Matt.23.28 | call3.results[].osisId |
| reference | TEXT |  |  |  |  | human reference, e.g. Mat 23:28 | call3.results[].key |
| preview | TEXT |  |  |  |  | the full interlinear HTML — the source of span | call3.results[].preview |
| step_version | TEXT |  |  |  |  | provenance — which STEP module | run.context.step_version |
| created_at | TEXT |  |  |  |  | when first built | raw.verses |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| text | TEXT |  |  |  |  | The verse full text (ESV_th per Start-Iba.ps1 STEP tag) -- the base extract every span/verse_lexical/report.verse_span_meaning read builds against. Escalation #1063. | escalation #1063, 2026-08-30 |

### strong_verse
_one row per (strong, verse) — unique. The m:m index._ — the source's assertion 'this strong is in this verse'. The check side against span (what the parse found).
dedup key: `strong, verse_id`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the strong searched | call3.query.strong |
| verse_id | INTEGER |  | ✓ |  | verse.id | the verse returned | call3.results[].osisId |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### span
_ONE ROW PER HTML <span> TAG of a verse (O3) - a tag's codes are a combined unit as STEP itself presents them_ — L4a - SOURCE, immutable. A parse of verse.preview. position is the running TAG index; (verse, position) is the key. strong_variant/morph_code may hold more than one space-separated code when STEP's own HTML combines them on one tag (corrected 2026-07-25 - see migration/rebuild_span_combined_units.py; the old one-row-per-code model split a combined unit and misattributed surface text).
dedup key: `verse_id, position`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| verse_id | INTEGER |  | ✓ |  | verse.id | the verse | parse:verse.preview |
| position | INTEGER |  | ✓ |  |  | running code index in the verse — the key with verse_id | parse:verse.preview |
| surface | TEXT |  |  |  |  | the English word this code belongs to; repeats across a word's codes | parse:verse.preview |
| strong_variant | TEXT |  |  |  |  | one or more strong codes, space-separated - STEP's HTML <span> tag as-is (e.g. G1722 G0054 for one preposition+noun unit); was wrongly declared as ONE code with an FK to strong.strongNumber, which does not hold for a combined value | parse:verse.preview |
| morph_code | TEXT |  |  |  |  | the grammatical layer — one, aligned with the code | parse:verse.preview |
| is_particle | INTEGER |  |  |  |  | 1 only if EVERY code on the tag is a grammar-particle code (H9xxx/G9xxx) - a tag mixing a real content word with attached particles is not itself a pure particle | derived:strong_variant |
| built_at | TEXT |  |  |  |  | raw time | raw.verses |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### run
_one row per work-package run — the control record_ — what ran, pinned to a config version, and RESUMABLE (O7): state + resume_point persisted so a pause survives the process.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ | ✓ |  | the run identifier | run.start |
| work_package | TEXT |  |  |  |  | which package | run.start |
| params | TEXT |  |  |  |  | JSON of the run params | run.start |
| runs_over | TEXT |  |  |  |  | the scope value, e.g. the word | run.start |
| config_version | TEXT |  |  |  |  | the config that ran — pinned before any work | run.start |
| state | TEXT |  |  |  |  | running \| paused \| done \| failed | run |
| resume_point | TEXT |  |  |  |  | the step to resume at on continue | run |
| started_at | TEXT |  |  |  |  | start | run.start |
| ended_at | TEXT |  |  |  |  | end | run.end |
| outcome | TEXT |  |  |  |  | the final result | run.end |

### validation_result
_one row per check a validate step ran_ — util.validation — the outcome of a check, persisted so it can be inspected and reported. A passed check is a recorded fact, not just an advancing run.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | run.run_id | the run that ran the check |  |
| word | TEXT |  |  |  |  | the word the check was over | validate |
| step | TEXT |  |  |  |  | the step that ran it | validate |
| check_name | TEXT |  |  |  |  | which check | validate |
| result | TEXT |  |  |  |  | pass \| fail | validate |
| detail | TEXT |  |  |  |  | the specifics — counts, what failed | validate |
| ran_at | TEXT |  |  |  |  | when | validate |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### escalations_old
_one row per researcher interaction — the pause_ — Historical escalation data, frozen at the 2026-08-20 redesign cutover (v2, corrected retry of the rolled-back 2026-08-19 v1) -- 723 rows, pre-dates escalation_history entirely. Read-only reference only, excluded from all new validation/correction (researcher instruction, 2026-08-19). Superseded by escalation + escalation_history.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | run.run_id | the paused run |  |
| source | TEXT |  | ✓ |  |  | the source of the escalation -- 'new-word: <word>' for a word-registration decision, the generating module name for a code-raised finding, or 'claude'/'researcher' for a manually-raised item. Required. | escalation.raise |
| at_step | TEXT |  |  |  |  | where to resume — makes it a pause not a fork | escalation.raise |
| type | TEXT |  |  |  |  | task \| run_error \| issue \| notice \| config | escalation.raise |
| short_description | TEXT |  |  |  |  | the short description of what's being escalated | escalation.raise |
| context | TEXT |  |  |  |  | the context that lets it be answered (JSON) | escalation.raise |
| tried | TEXT |  |  |  |  | what the app attempted before asking | escalation.raise |
| state | TEXT |  |  |  |  | raised \| re-assign \| on-hold \| closed \| withdraw \| completed | escalation |
| next_action | TEXT |  |  |  |  | the decision/next action taken: approve \| reject \| revise \| hold \| noted | escalation.answer |
| answered_at | TEXT |  |  |  |  | when | escalation.answer |
| raised_at | TEXT |  |  |  |  | when raised | escalation.raise |
| comment | TEXT |  |  |  |  | researcher feedback on a 'revise' answer (or any answer) | escalation.answer_for_run |
| resolution | TEXT |  |  |  |  | what was actually done to resolve the item -- a short description or reference. NOT the decision itself (see next_action) -- records the outcome, which nothing previously captured. | escalation.answer_for_run / manual close |
| related_activity | TEXT |  |  |  |  | the process, module, or activity this row relates to -- defaults to at_step for code-raised rows; set explicitly for manual/task items | escalation.raise / escalation.raise_manual |
| next_action_assigned_to | TEXT |  |  |  |  | who should act on this next -- Claude or Researcher | escalation.raise / re-assignment |
| answered_by | TEXT |  |  |  |  | who recorded the decision/resolution -- Claude or Researcher. Required BY CONVENTION whenever a row reaches a terminal state (completed/closed/withdraw) -- enforced in escalation.py's answer/retract functions, not a DB-level NOT NULL (a raised/on-hold row has none yet). | escalation.answer_for_run / answer_for_word / retract_run |

### lemma_inventory
_one row per corpus lemma (base Strong's) — the INDEPENDENT substrate the seed net runs over_ — L4b seed substrate; imported from the old study, NOT derived from the registry, so the seed is a real completeness control
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ | ✓ |  | base Strong's, sub-letters stripped | import:lemma-inventory |
| gloss | TEXT |  |  |  |  | the lemma's English gloss — the meaning the net matches on | import:lemma-inventory |
| language | TEXT |  |  |  |  | Hebrew/Greek | derived:lemma_key |
| source | TEXT |  |  |  |  | import provenance | migration |
| created_at | TEXT |  |  |  |  | when imported | migration |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### candidate_seed
_one row per assessed lemma — the over-inclusive Axis-A candidate assessment_ — L4b seed decision (potential, not definite); the lexical stage is the real test. registry_match NULL on a candidate = a candidate MISSING registry word (the double control) -- REMOVED from the system 2026-09-10 (researcher instruction, verbatim: candidate_seed is removed from the system, it should be marked inactive and no active table should be referencing it or depend on it). All 2026-07-23 DORMANT columns confirmed still dormant; the two live dependents found this pass (cfg_write_grant writer=migration, and validation.book's cfg_report_csv_table/cfg_report_section/cfg_setting wiring) corrected same turn.
dedup key: `lemma_key, strong_variant, sense_seq`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  | lemma_inventory.lemma_key | the assessed lemma |  |
| decision | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| layer | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| registry_match | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| tag | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| assessed_at | TEXT |  |  |  |  | DORMANT - candidate.seed retired 2026-07-23; no active mechanism populates this column |  |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| strong_variant | TEXT |  | ✓ |  | strong.strongNumber | the specific sub-lettered Strongs variant this row's tag reflects (e.g. H0639G), or the lemma_key itself when the tag applies to the whole base lemma (no sub-strong split decided yet -- the default for existing rows) | candidate.seed / candidate.curate |
| sense_seq | INTEGER |  | ✓ | ✓ |  | DORMANT - candidate.load retired 2026-07-23; no active mechanism populates this column |  |
| step_status | TEXT |  |  |  |  | DORMANT - candidate.load retired 2026-07-23; no active mechanism populates this column |  |
| ib_referent_type | TEXT |  |  |  |  | DORMANT - candidate.load retired 2026-07-23; no active mechanism populates this column |  |

### span_candidate
_one row per CANDIDATE span (existence = candidate) — the L4b stamp over the L4a span_ — over-inclusive candidate stamp; the lexical stage later tests each in context
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| span_id | INTEGER |  | ✓ | ✓ | span.id | the L4a span stamped |  |
| lemma_key | TEXT |  |  |  |  | base Strong's of the span (denormalised for continuity/join) | derived:span.strong_variant |
| candidate_tag | TEXT |  |  |  |  | the IB label from the seed | candidate_seed.tag |
| seed_source | TEXT |  |  |  |  | DORMANT - candidate.set retired 2026-07-23; no active mechanism populates this column |  |
| set_at | TEXT |  |  |  |  | DORMANT - candidate.set retired 2026-07-23; no active mechanism populates this column |  |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### passage
_one row per passage — a reading frame (global, per book)_ — extends a characteristic's context to adjacent verses for assessing movement/process/qualifying spans; NOT a thematic unit
dedup key: `book, start_chapter, start_verse, end_chapter, end_verse`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| feasibility_note | TEXT |  |  |  |  | Step 2's own self-assessment record: why this scope was judged readable as a whole without quality loss (or, if the call was refused, why not -- though a refused call writes no passage row at all, so a live row's feasibility_note is always the 'yes, and here's why' case). | passage.build |
| open_decisions_note | TEXT |  |  |  |  | Part C section 8 -- short free-text summary of open decisions/next steps for this passage. Stays a single field, not its own table (design doc: normally short prose, not a repeating structured list, unlike sections 4-7). |  |
| phenomena_complete_at | TEXT |  |  |  |  | NULL until the debate digest Step 3 phase gate is confirmed complete for the whole passage (every verse_hib pair for this passage has a matching phenomenon row); set only by an explicit control check, never by trust. operation writes are blocked in code while this is NULL (schema built, gate-enforcing writer not yet built -- see b3-b5-operations-schema-design-20260805.md). |  |
| story_summary | TEXT |  |  |  |  | Step 2's high-level story synthesis for this passage's scope, read in light of the identified HIBs -- the researcher's own 2026-08-06 redefinition of what Step 2 actually produces. Written once per passage registration, updated only via reconciliation. | passage.build |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| book | TEXT |  | ✓ |  |  | OSIS book code | derived:verse.osisId |
| anchor_verse_id | INTEGER |  | ✓ |  | verse.id | first verse of the run — the anchor |  |
| start_chapter | INTEGER |  |  |  |  | range start chapter - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| start_verse | INTEGER |  |  |  |  | range start verse - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| end_chapter | INTEGER |  |  |  |  | range end chapter - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| end_verse | INTEGER |  |  |  |  | range end verse - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| ref | TEXT |  |  |  |  | human range - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| verse_count | INTEGER |  |  |  |  | count of verses in the range - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| rule | TEXT |  |  |  |  | char-continuity \| maximal - DORMANT since passage.build retired 2026-07-26; NULL on every live row; no active mechanism populates this column |  |
| source | TEXT |  |  |  |  | passage-build \| single-verse-emergent - DORMANT since passage.build retired 2026-07-26; NULL on every live row; no active mechanism populates this column |  |
| needs_review | INTEGER |  |  |  |  | 1 when verse_count > passage.review_over (passage.build only) - DORMANT since passage.build retired 2026-07-26; NULL on every live row; passage.validate reports the live distribution directly instead |  |
| created_at | TEXT |  |  |  |  | when this passage row was created - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| book_label | TEXT |  |  |  |  | human-facing subfolder name (e.g. 'Daniel') used by the verse-analysis report writers; defaults to `book` if the caller never supplied one | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| verse_span_meaning_path | TEXT |  |  |  |  | path to this range's report.verse_span_meaning output, written by that step on success | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| verse_span_meaning_written_at | TEXT |  |  |  |  | UTC timestamp of the last report.verse_span_meaning write for this range | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| debate_path | TEXT |  |  |  |  | path to this range's report.passage_debate output (scaffold or filled — see debate_status), written by that step on success | report.passage_debate (legacy, passage.rule IS NULL) or report.debate (new-model, passage.rule='input-scope' -- tools/build_debate_report.py) |
| debate_written_at | TEXT |  |  |  |  | UTC timestamp of the last report.passage_debate write for this range | report.passage_debate (legacy, passage.rule IS NULL) or report.debate (new-model, passage.rule='input-scope' -- tools/build_debate_report.py) |
| debate_status | TEXT |  |  |  |  | 'scaffold' (auto-generated, still has unreplaced <!-- fill in --> placeholders) or 'filled' (none remain) — a coarse, mechanically-derived completion signal only; NOT a digestion of the debate's analytical content, which is a separate, not-yet-designed question | report.passage_debate (legacy, passage.rule IS NULL: scaffold\|filled) or report.debate (new-model, passage.rule='input-scope': empty\|in-progress\|complete) -- tools/build_debate_report.py |
| genre | TEXT |  |  |  |  | RETIRED 2026-09-09, researcher verdict, escalation #1608: genre has no role in this study's lexical analysis -- reading beyond the current verse is to resolve a characteristic's 'reach', not to classify literary genre; char-movement isn't under consideration even in Layer 2 yet, and Window 2's own future discovery process (read the char/movement first, expand to surrounding verses only when a movement can't close) doesn't need genre either. Was: manual, set as part of lexical.enrich's own first move for this passage; no controlled vocabulary yet — free text this round. NOT ported from bible_research.db.verse.genre (book-level, confirmed too coarse). | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| lexical_complete_at | TEXT |  |  |  |  | NULL until every verse in this passage has a verse_lexical row for every code AND (for judgement-bearing codes) a verse_lexical_note disposition — set only by an explicit control check (mirrors phenomena_complete_at) | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |

### verse_passage
_one row per verse-in-a-passage — passage membership (L4b), keeps the raw verse pristine_ — which passage a verse belongs to; a verse is in at most one passage
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| passage_id | INTEGER |  | ✓ |  | passage.id | the passage |  |
| verse_id | INTEGER |  | ✓ | ✓ | verse.id | the verse (unique — one passage per verse) |  |
| is_anchor | INTEGER |  |  |  |  | 1 on the anchor verse - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| created_at | TEXT |  |  |  |  | when this link was created - now populated by the verse-fanout tracking mechanism, not passage.build | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### cfg_change_detail
_one row per configmaint.propose write_ — row-level audit of every cfg_* change actually applied — what cfg_change_log's whole-reload shape could not record
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| run_id | TEXT |  | ✓ |  | run.run_id | the run that made the change | configmaint.propose |
| table_name | TEXT |  | ✓ |  |  | which cfg_* table changed | configmaint.propose |
| op | TEXT |  | ✓ |  |  | insert \| update \| delete | configmaint.propose |
| where_json | TEXT |  |  |  |  | the row's natural key (JSON) | configmaint.propose |
| set_json | TEXT |  |  |  |  | the new values written (JSON) | configmaint.propose |
| before_json | TEXT |  |  |  |  | the row's prior state, for update/delete (JSON, null for insert) | configmaint.propose |
| applied_at | TEXT |  | ✓ |  |  | when the write committed | configmaint.propose |

### strong_meaning_parsed
_one row per gloss segment of a strong_meaning_tree lemma (2026-07-25 corrected parse)_ — L2b — the parsed meaning layer over strong_meaning_tree (raw). Segment-scoped: refs/note belong to the exact <b> span they followed, not pooled across the whole source row (the original extract's bug, fixed before this table existed). Comma/semicolon are NOT sense separators here — only a literal line break splits a gloss further.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| lemma_key | TEXT |  | ✓ |  |  | the base code this parsed sense belongs to (never a sub-entry letter) | derived:strong_meaning_tree.lemma_key |
| sort | INTEGER |  |  |  |  | order within the source sense tree | parsed:strong_meaning_tree.sort |
| sense_code | TEXT |  |  |  |  | the tree position, e.g. 1a1a) — or the sense_code column value verbatim | parsed:strong_meaning_tree.sense_code |
| gloss | TEXT |  |  |  |  | one exploded gloss term, kept whole (no comma/semicolon splitting) | parsed:strong_meaning_tree.sense_text |
| verse_refs | TEXT |  |  |  |  | verse citations scoped to this gloss's own <b> span, semicolon-joined | parsed:strong_meaning_tree.sense_text |
| note | TEXT |  |  |  |  | commentary scoped to this gloss's own segment, not pooled across the row | parsed:strong_meaning_tree.sense_text |
| row_type | TEXT |  |  |  |  | lookup / description / not applicable — lexicon_split_common.classify_row() | derived:gloss |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| strong_variant |  |  |  |  | strong.strongNumber |  |  |

### strong_lsj_parsed
_one row per LSJ sense of a strong_lexicon.lsj entry (2026-07-25 corrected parse)_ — L2b — the parsed classical-Greek lexicon layer over strong_lexicon.lsj (raw). Sense blocks split on LSJ's own <LevelN>/<br> structure; gloss kept whole within a block, not exploded on internal commas.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full strong code this LSJ sense belongs to | derived:strong_lexicon.strong |
| sense_label | TEXT |  |  |  |  | LSJ sense position, e.g. I / I.2 / II.2.b, or 'headword' | parsed:strong_lexicon.lsj |
| gloss | TEXT |  |  |  |  | the sense's bold-span gloss text, kept whole (no comma splitting); may legitimately be blank when a block carries only dialect/citation notes | parsed:strong_lexicon.lsj |
| note | TEXT |  |  |  |  | dialect/grammar labels, connective prose — everything in the block but the gloss | parsed:strong_lexicon.lsj |
| row_type | TEXT |  |  |  |  | headword for the entry's own headword row(s), lookup for every sense row | derived:sense_label |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_mounce_parsed
_one row per Mounce sense of a strong_lexicon.mounce entry (2026-07-25 corrected parse)_ — L2b — the parsed Greek lexicon layer over strong_lexicon.mounce (raw). Split ONLY on <br> (the source's real line breaks); comma/semicolon within one line are punctuation inside a sense, not sense separators.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full strong code this Mounce line belongs to | derived:strong_lexicon.strong |
| mounce_parsed | TEXT |  |  |  |  | one <br>-delimited line of Mounce's entry, kept whole (no comma splitting) | parsed:strong_lexicon.mounce |
| row_type | TEXT |  |  |  |  | lookup / description — lexicon_split_common.classify_row() | derived:mounce_parsed |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### strong_related
_one row per (strong, related strong) pair STEP's getInfo returned (fetched 2026-07-25)_ — L2b — NOT derived from any raw table; fetched live from STEP per full strong code (lib.stepapi.Step.call2_getInfo, vocabInfos[0].relatedNos) since no raw table captures this. related_strong is unconstrained — STEP can name a code this app has never onboarded via raw.detail.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full code of the SOURCE term STEP was asked about | fetched:STEP.getInfo |
| related_strong | TEXT |  | ✓ |  |  | the full code of the RELATED term — may have no strong row of its own yet | fetched:STEP.getInfo.relatedNos.strongNumber |
| related_form | TEXT |  |  |  |  | the related term's native-script form | fetched:STEP.getInfo.relatedNos.matchingForm |
| related_transliteration | TEXT |  |  |  |  | the related term's transliteration | fetched:STEP.getInfo.relatedNos.stepTransliteration |
| related_gloss | TEXT |  |  |  |  | the related term's own short gloss | fetched:STEP.getInfo.relatedNos.gloss |
| deleted | INTEGER |  |  |  |  | soft delete |  |

### verse_lexical
_one row per Strong's code within a span (span_id, code_ordinal) — a compound span yields several rows, one per component code_ — L4b — DERIVED, version-aware. The mechanical T1-T3 reading: role classification + stem/voice-selected sense + named-not-resolved ambiguity, per code. Read by report.verse_lexical and, downstream, by T4-T9 — never by re-deriving from span/strong/strong_meaning_parsed directly.
dedup key: `span_id, code_ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | migration/bootstrap_span_reading.py |
| span_id | INTEGER |  | ✓ |  | span.id | which span this reading is for — a span may carry several code_ordinal rows here (one per code in its compound strong_variant) | migration/bootstrap_span_reading.py |
| verse_id | INTEGER |  | ✓ |  | verse.id | denormalized from span, matches verse_passage's own precedent — query without joining through span | migration/bootstrap_span_reading.py |
| code_ordinal | INTEGER |  | ✓ |  |  | position of this code within the span's space-joined strong_variant, 0-based | migration/bootstrap_span_reading.py |
| strong | TEXT |  |  |  | strong.strongNumber | the single code this row resolves — may be NULL only if strong_variant itself is empty (should not occur in practice) | migration/bootstrap_span_reading.py |
| morph_code | TEXT |  |  |  |  | this code's own morph slice (space-split from span.morph_code in the same order) | migration/bootstrap_span_reading.py |
| role | TEXT |  | ✓ |  |  | REDESIGNED 2026-09-16 (#1706 Phase B item 3, #1607 D1/D4) — bare JSON array of every live cluster_strong.cluster_code for this strong (T-codes AND M-codes, e.g. '["T5","M12"]'), not an array of objects. Replaces the old content/function morph-tag classifier (escalation #1590's bug — Greek article tag 'T' misclassified content instead of function — is retired-by-design, not patched: the whole classify_role() mechanism is deleted, not fixed). Also the base-data readiness signal itself (#1606 D1): an empty array means zero cluster_strong allocation, the exact FATAL condition `lexical.readiness` Leg 3 and the pre-run unready_codes_in_scope() validator both check for. | migration/bootstrap_span_reading.py |
| status | TEXT |  | ✓ |  |  | 'resolved' (strong row found, sense pulled -- content or function role alike) or 'unregistered' (no strong row yet -- a genuine coverage gap, regardless of role). | migration/bootstrap_span_reading.py |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC | migration/bootstrap_span_reading.py |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete — rewriting a (span_id, code_ordinal) inserts a fresh row and flips the superseded row's deleted to 1, same convention as verse/span/strong | migration/bootstrap_span_reading.py |
| position | INTEGER |  | ✓ |  |  | span.position, denormalized — mechanical, no judgement | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| surface | TEXT |  |  |  |  | span.surface, denormalized — the literal text at this span, independent of sense (never confused with resolved_sense) | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| testament | TEXT |  | ✓ |  |  | derived: 'OT' if cfg_book_order.ordinal<=38 else 'NT' (Mal=38/Matt=39 boundary) — pure ordinal derivation, no reference table | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| is_negator | INTEGER |  |  |  |  | 1 if strong is in cluster_strong WHERE cluster_code='T5' AND deleted=0, else NULL (never 0 -- NULL means 'not in the T5 lexicon'). cfg_lexical_code_class is dead code, never read by load_code_classes() -- corrected, escalation #1607/CA-5, 2026-09-10. | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| narrative_morph | TEXT |  |  |  |  | Hebrew wayyiqtol / az+imperfect flag, derived from morph_code pattern — NULL unconditionally for language != 'Hebrew' | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| gloss_consistent_in_verse | INTEGER |  | ✓ |  |  | 1 unless this (strong, morph_code) pair carries >1 distinct SURFACE value among this verse's own rows — mechanical data-quality check. CORRECTED 2026-09-16 (#1706 Phase B migration): this row previously said 'resolved_sense', stale since escalation #1527 (2026-09-06) rekeyed the actual check to `surface` — resolved_sense is a pure function of (strong, morph_code) with no per-occurrence signal, so a same-code-different-sense check against it could never fire; `surface` (the aligned translation word) genuinely does vary by occurrence. | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| party_kind | TEXT |  |  |  |  | 'divine'/'human'/'non_human' -- set ONLY when this code IS ITSELF a name in cluster_strong WHERE cluster_code IN ('T4','T7','T8','T9') AND deleted=0 (T4=adversarial->non_human, T7=divine, T8=human, T9=angelic->non_human); a pronoun's own party_kind is NOT stored here, it derives via its entity_link note's target_verse_lexical_id (two-hop join, Window 2's own future join). cfg_lexical_code_class is dead code, never read by load_code_classes(); the previous text also omitted T4/party_adversarial from its source list -- both corrected, escalation #1607/CA-6, 2026-09-10. | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| updated_at | TEXT |  |  |  |  | Timestamp of the row's last real content correction (post-insert), set by write_readings_for_span whenever a live row's content actually changes -- INSERT never populates it (CA-7, escalation #1607/#1605: 20/21 live columns were registered, this one never was, since the #1520 identity-stable-write redesign added it). 113,684/544,572 (20.9%) live rows are currently non-NULL, matching 'only rows corrected since #1520 get it set' exactly. | 1607-layer1-layer2-six-point-column-map-v1-20260909.md (CA-7) |

### hib
_hib_ — one row per Human Inner Being identified in a scope (debate digest Step 1) -- scope-wide, not passage-scoped: the same HIB recurs across many passages of a book.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| book | TEXT |  | ✓ |  |  | OSIS book code, same convention as verse.osisId's book segment |  |
| label | TEXT |  | ✓ |  |  | e.g. 'Daniel', 'the four youths', 'King Belshazzar' |  |
| kind | TEXT |  | ✓ |  |  | named_individual \| unnamed_individual \| named_collection \| unnamed_collection \| implicit_individual \| implicit_collection -- six types, two orthogonal axes: plurality (individual\|collection) x specificity (named\|unnamed\|implicit). Researcher training pass nahum-1-inner-being-training-20260803.md; debate digest Step 1 (presumptive-candidate / collective / referential rules). |  |
| first_verse_id | INTEGER |  |  |  | verse.id | anchor -- where this HIB was first identified |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete, standard convention |  |

### hib_referent_option
_hib_referent_option_ — one row per grammatically-live referent-crux reading (T4), child of hib.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| hib_id | INTEGER |  | ✓ |  | hib.id | the HIB this referent-crux reading belongs to |  |
| reading_text | TEXT |  | ✓ |  |  | one grammatically-live candidate reading (T4) -- e.g. one option for 'we' in Obad 1 |  |
| textual_grounds | TEXT |  |  |  |  | why this reading is live |  |
| adopted | INTEGER |  | ✓ |  |  | exactly one row per hib_id should be 1 -- the explicit choice (T4: 'adopt one explicitly') |  |
| ordinal | INTEGER |  | ✓ |  |  |  |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### verse_hib
_verse_hib_ — one row per HIB present/a presumptive candidate in a given verse (Step 1's per-verse sweep) -- the input B4's future HIB-continuity passage-boundary rule reads from.
dedup key: `verse_id, hib_id`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| verse_id | INTEGER |  | ✓ |  | verse.id |  |  |
| hib_id | INTEGER |  | ✓ |  | hib.id | this HIB is present/a presumptive candidate in this verse (debate digest Step 1) -- also the table B4's future HIB-continuity passage-boundary rule reads from |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### phenomenon
_phenomenon_ — the phenomena register (Step 3 output) -- one row per HIB per verse per passage.
dedup key: `passage_id, verse_id, hib_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| verse_id | INTEGER |  | ✓ |  | verse.id |  |  |
| hib_id | INTEGER |  | ✓ |  | hib.id |  |  |
| description | TEXT |  | ✓ |  |  | the phenomenon: a state, disposition, or characteristic of this HIB's inner life (debate digest Step 3) |  |
| textual_warrant | TEXT |  |  |  |  | the verb/clause/stated-silence that grounds it (WA-passage-read-guidance step 3b) |  |
| status | TEXT |  | ✓ |  |  | 'stated' \| 'inferred' \| 'silent' -- 'no phenomenon found, silent' is itself a valid row (WA-interpretation-questions Part B.4), never an omitted one |  |
| ordinal | INTEGER |  | ✓ |  |  | allows more than one phenomenon for the same HIB in the same verse (v1.5 step3 note c) |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### operation
_operation_ — the operation for a registered phenomenon (Step 4-5 output) -- phenomenon_id NOT NULL enforces Part B.12 at the DB level.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| phenomenon_id | INTEGER |  | ✓ |  | phenomenon.id | NOT NULL by design -- the DB-level enforcement of WA-interpretation-questions Part B.12: an operation may only originate from an already-registered phenomenon |  |
| process | TEXT |  |  |  |  | state/status, or a movement (come from/go to/impact on/emerge/go away/become evident) -- v1.4 Q6 |  |
| action_type | TEXT |  |  |  |  | short verb-based label (Q11) -- a label, not a controlled vocabulary (Part B.10) |  |
| decision | TEXT |  |  |  |  | 'retain' \| 'set_aside' \| 'retain_referential' \| 'recorded_silence' |  |
| observation_text | TEXT |  |  |  |  | what the text/span-data states, Strong's codes cited |  |
| description_text | TEXT |  |  |  |  | debate digest Step 5's descriptive write-up |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### operation_party
_operation_party_ — one row per source/target of an operation (plural-capable, v1.5 step1 note a), child of operation.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| operation_id | INTEGER |  | ✓ |  | operation.id |  |  |
| role | TEXT |  | ✓ |  |  | 'source' \| 'target' |  |
| kind | TEXT |  | ✓ |  |  | 'self' \| 'human' \| 'non_human' \| 'object_situation' \| 'none' |  |
| detail | TEXT |  |  |  |  | which human/object, if named |  |
| enablement_only | INTEGER |  | ✓ |  |  | role='source' rows only -- Part B.5's source-of-state vs source-of-enablement distinction, kept structurally separate rather than folded into kind |  |
| ordinal | INTEGER |  | ✓ |  |  | a phenomenon's operation can have multiple sources/targets (v1.5 step1 note a) |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| hib_id | INTEGER |  |  |  | hib.id | which registered HIB this source/target party IS, when it is one -- nullable: self/non_human/object_situation/none parties genuinely have no HIB to link. Added 2026-08-07 (Finding 2, debate-schema-traceability-gap-findings-20260807.md): 'detail' alone gave no structural traceability back to the hib register. |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_linkage
_passage_linkage_ — Part C section 4 (Q7) -- linkages between two specific, already-registered operations in the same passage, and surfaced non-linkages.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| from_operation_id | INTEGER |  | ✓ |  | operation.id | Part C section 4 / Q7 -- a linkage connects two SPECIFIC, already-registered operations in the same passage, never a pattern across a range |  |
| to_operation_id | INTEGER |  | ✓ |  | operation.id |  |  |
| note | TEXT |  | ✓ |  |  | what the linkage is -- also where a Q7 SURFACED ABSENCE gets recorded (row with from=to=the same operation, note explains the absence) rather than passed over silently |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_insufficiency
_passage_insufficiency_ — Part C section 5 (Q9/B.7) -- data the base extract does not carry, named not filled.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| verse_id | INTEGER |  |  |  | verse.id | nullable -- an insufficiency can be passage-wide, not always tied to one verse |  |
| note | TEXT |  | ✓ |  |  | Part C section 5 / Q9 / Part B.7 -- data the base extract does not carry, named not filled from outside knowledge |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_emergent_question
_passage_emergent_question_ — Part C section 6 (Q10/B.9/B.12) -- interpretive forks and genuine literary/structural observations, tracked per passage, never merged across passages.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| verse_id | INTEGER |  |  |  | verse.id | nullable -- an emergent question can span the whole passage |  |
| question_text | TEXT |  | ✓ |  |  | Part C section 6 / Q10 -- interpretive forks (Part B.9) and genuine literary/structural observations (Part B.12, T5) both land here, never in the phenomena register or an operation |  |
| kind | TEXT |  | ✓ |  |  | 'interpretive_fork' \| 'literary_structural' \| 'other' |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### passage_validation_note
_passage_validation_note_ — Part C section 7 (Phase 3) -- the closing re-examination of the passage's own phenomena/operations, corrected before the debate is considered filled.
dedup key: `passage_id, ordinal`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| passage_id | INTEGER |  | ✓ |  | passage.id |  |  |
| phenomenon_id | INTEGER |  |  |  | phenomenon.id | nullable -- a validation finding can be about the passage's debate generally, not always one phenomenon |  |
| finding_text | TEXT |  | ✓ |  |  | Part C section 7 / Phase 3 step 6 -- is this genuinely an inner-being phenomenon, does its Phase 1 justification warrant it, does its Phase 2 operation track faithfully back to it |  |
| corrected | INTEGER |  | ✓ |  |  | WA-passage-read-guidance v1.5 step 6: a failure found here is corrected before the debate is considered filled, not merely logged for later -- this flag records that the correction actually happened, not just that a finding was noted |  |
| ordinal | INTEGER |  | ✓ |  |  | natural key within passage_id for the reconciliation writer |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete |  |

### cfg_method_rule
_cfg_method_rule_ — One row per discrete, nameable analytical rule governing a debate-pipeline step -- config, not only prose docs (researcher, 2026-08-06).
dedup key: `step, rule_key`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| step | TEXT |  | ✓ |  |  | which pipeline step this rule governs, e.g. 'hib.set', 'phenomenon.set' |  |
| rule_key | TEXT |  | ✓ |  |  | short slug, unique within a step, e.g. 'presumptive-candidate' |  |
| rule_text | TEXT |  | ✓ |  |  | the rule's own exact wording -- the operational source of truth from here on |  |
| source_doc | TEXT |  |  |  |  | provenance -- which doc/section this was transcribed from |  |
| enforced_by | TEXT |  |  |  |  | code location that mechanically checks this rule, if any -- NULL if it's analyst judgement, not a SQL-checkable condition |  |
| ordinal | INTEGER |  | ✓ |  |  | display order within a step |  |
| active | INTEGER |  | ✓ |  |  | supersede by setting 0 and inserting a new row, rather than editing/deleting -- history kept |  |

### cfg_quality_check
_cfg_quality_check_ — Config-defined reasonability/existence self-check questions per debate-pipeline step (researcher, 2026-08-06). Draft content, not yet wired to any writer's enforcement.
dedup key: `step, check_key`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| step | TEXT |  | ✓ |  |  | which pipeline step this check applies to |  |
| check_key | TEXT |  | ✓ |  |  | short slug, unique within a step |  |
| question | TEXT |  | ✓ |  |  | the actual self-check question a reading pass must ask itself for each candidate item |  |
| test_kind | TEXT |  | ✓ |  |  | 'existence' \| 'non_existence' \| 'reasonableness' (researcher's own three kinds, 2026-08-06) |  |
| required | INTEGER |  | ✓ |  |  | 1 = should eventually block a write until answered; 0 = advisory only. NOT YET ENFORCED for any row by any writer -- see module docstring |  |
| enforced_by | TEXT |  |  |  |  | code location that mechanically checks this, if any |  |
| ordinal | INTEGER |  | ✓ |  |  |  |  |
| active | INTEGER |  | ✓ |  |  | supersede by setting 0 and inserting a new row -- history kept |  |

### cfg_index
_cfg_index_ — Secondary (non-unique) indexes to build per data table -- closes the gap left by build_data_tables() only ever emitting FK/UNIQUE, never plain indexes (schema-remediation-design-20260807.md).
dedup key: `table_name, name, col`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| table_name | TEXT |  | ✓ |  |  | which data table this index is built on |  |
| name | TEXT |  | ✓ |  |  | index name (unique DB-wide, SQLite requirement) -- convention: idx_{table}_{col} |  |
| col | TEXT |  | ✓ |  |  | one column of this index; multiple rows sharing (table_name, name) form one composite index |  |
| ordinal | INTEGER |  | ✓ |  |  | column order within a composite index |  |

### debate_change_detail
_hib_change_detail_ — one row per hib/hib_referent_option/verse_hib/passage/verse_passage/phenomenon/operation/operation_party/passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note row inserted, updated, or soft-deleted by hib.set/passage.build/phenomenon.set/operation.set/closing.set -- the per-run CRUD audit trail shared by every debate writer (researcher direction 2026-08-08).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| run_id | TEXT |  | ✓ |  | run.run_id | which run made this change -- same fk convention as escalation.run_id/validation_result.run_id |  |
| table_name | TEXT |  | ✓ |  |  | 'hib' \| 'hib_referent_option' \| 'verse_hib' -- which table this row's change touched |  |
| op | TEXT |  | ✓ |  |  | 'insert' \| 'update' \| 'delete' -- free text, matching cfg_change_detail.op's own precedent |  |
| where_json | TEXT |  |  |  |  | identifies the row touched, e.g. {"id": 47} |  |
| set_json | TEXT |  |  |  |  | the new values written (insert/update only) |  |
| before_json | TEXT |  |  |  |  | prior row state (update/delete only), NULL on insert |  |
| applied_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| writer | TEXT |  | ✓ |  |  | which step made this change -- 'hib.set' \| 'passage.build' \| 'phenomenon.set' \| 'operation.set' \| 'closing.set' | migration/add_debate_change_detail_writer_column_20260808.py |

### cluster
_one row per cluster (M01-M46 + FLAG + T2) — the inner-being dimension taxonomy_ — Migrated from the old project's bible_research.db `cluster` table, 2026-08-11. cluster_code is the canonical key referenced everywhere else (cluster_strong, and any future dimension work). T2 is the landing zone for codes not included in analysis; FLAG is unresolved/needs-review; M01-M46 are the named inner-being characteristics.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cluster_code | TEXT | ✓ |  |  |  | canonical key, e.g. M01, FLAG, T2 | migrated:bible_research.db.cluster |
| short_name | TEXT |  |  |  |  | short display name, e.g. 'Fear' | migrated:bible_research.db.cluster |
| description | TEXT |  |  |  |  | one-line description, e.g. 'Fear, Dread and Terror' | migrated:bible_research.db.cluster |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| status | TEXT |  |  |  |  | Cluster-level lifecycle, cfg_enum-governed (#1697). Ordinals 1-2 historical/one-off (the T/M-code cluster_strong classification work, already complete for all 95 live clusters) — no gating code needed for these. Ordinals 3-8 are the real active lifecycle, rolled up from cluster_subgroup.status (#1690 SS3a): can only progress past ready_for_reading/ready_for_observations/ready_for_synthesis once EVERY subgroup in the cluster (excluding FLAG) has itself reached the matching level. strongs_reassigned raises a real escalation (decision_required) at the moment it fires -- no automatic resubmission of process (b). |  |
| status_changed_at | TEXT |  |  |  |  | Timestamp of the last cluster.status transition. |  |

### cluster_strong
_one row per (strong, cluster_code) assignment_ — The strong<->cluster link. Cluster membership is a property of the Strong's code itself, independent of word_strong/word_registry — deliberately has no FK/dependency on either. `source` tracks provenance (old-system-migration now; future allocation passes get their own source value, never overwriting a prior row in place).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key |  |
| strong | TEXT |  | ✓ |  | strong.strongNumber | the full Strong's code this assignment is for |  |
| cluster_code | TEXT |  | ✓ |  | cluster.cluster_code | the assigned cluster |  |
| source | TEXT |  | ✓ |  |  | provenance: 'old-system-migration' \| (future) an LLM-allocation pass identifier |  |
| created_at | TEXT |  |  |  |  | ISO-8601 UTC |  |
| deleted | INTEGER |  |  |  |  | soft delete |  |
| confidence | TEXT |  |  |  |  | 'high' \| 'medium' \| 'low' -- an allocation pass's own confidence in this assignment; NULL for old-system-migration rows (no equivalent signal). |  |
| operation | INTEGER |  |  |  |  | 1 if the code denotes a human operation/movement (a T3 'Operations' candidate), 0/NULL otherwise. |  |
| alt_clusters | TEXT |  |  |  |  | JSON list of alternate cluster_code candidates an allocation pass considered besides the one it picked. |  |
| review_flag | INTEGER |  |  |  |  | 1 if this specific assignment needs researcher review before being trusted as final. |  |
| rationale | TEXT |  |  |  |  | free-text reasoning for the assignment, as given by whatever process produced it. |  |

### cfg_escalation
_cfg_escalation_ — One row per discrete, nameable rule governing the escalation utility itself -- config, not prose (researcher, 2026-08-16 iba-table-review reset). Parallel to cfg_method_rule but scoped to escalation.py, not the debate pipeline.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| rule_key | TEXT |  | ✓ | ✓ |  | short slug, unique -- e.g. 'duplicate_suppression' |  |
| rule_text | TEXT |  | ✓ |  |  | the rule's own exact wording -- the operational source of truth |  |
| enforced_by | TEXT |  |  |  |  | code location that mechanically checks this rule, if any -- NULL/'not yet wired' if it is process discipline, not yet a SQL/code-checkable condition |  |
| active | INTEGER |  | ✓ |  |  | supersede by setting 0 and inserting a new row, rather than editing/deleting -- history kept |  |

### cfg_content_index_exclude
_one row per exclude pattern_ — governs content_index.rebuild/.refresh's file scope: any .md file whose path starts with an ACTIVE pattern here is skipped. Default is 'include all .md except' -- an empty table excludes nothing.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | TEXT | ✓ | ✓ |  |  | a file path or folder-path prefix (posix-style, project-root-relative) -- e.g. 'iba/app/verse-analysis/' excludes the whole folder, a full file path excludes just that file | migration/bootstrap_content_index.py |
| reason | TEXT |  | ✓ |  |  | why this is excluded -- required, not a bare flag | migration/bootstrap_content_index.py |
| added_at | TEXT |  | ✓ |  |  | when the pattern was added | migration/bootstrap_content_index.py |
| inactive | INTEGER |  | ✓ |  |  | 0=active (excludes), 1=retired (no longer excludes, kept for history per governance.tables' own convention) | migration/bootstrap_content_index.py |

### cfg_content_index_size_override
_one row per manually-released large file/folder_ — overrides content_index.exclude_size_threshold_bytes: a .md file matching an ACTIVE pattern here is included even if it's at or above the size threshold. 'Manually released if needed' (researcher, 2026-08-17) -- empty by default, nothing released until named here.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | TEXT | ✓ | ✓ |  |  | a file path or folder-path prefix (posix-style, project-root-relative), same matching rule as cfg_content_index_exclude | migration/bootstrap_content_index.py |
| reason | TEXT |  | ✓ |  |  | why this large file is still wanted in the index | migration/bootstrap_content_index.py |
| added_at | TEXT |  | ✓ |  |  | when the override was added | migration/bootstrap_content_index.py |
| inactive | INTEGER |  | ✓ |  |  | 0=active (releases it), 1=retired | migration/bootstrap_content_index.py |

### cfg_behaviour_class
_one row per operational-behaviour class_ — the taxonomy for governance.operational_behaviour_control -- chat, terminal, sqlite, documentation, llm_output, and any further class identified in later consolidation cycles.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| class | TEXT | ✓ | ✓ |  |  | the behaviour-class key (e.g. 'sqlite') -- referenced by cfg_behaviour_rule.class | migration/bootstrap_behaviour_rules_v1_20260818.py |
| authoritative_doc | TEXT |  |  |  |  | the single document authoritative for this class's non-cfg content, once decided (single-authority discipline, class='documentation' rule) -- NULL until the doc-mapping consolidation cycle runs; not guessed | migration/bootstrap_behaviour_rules_v1_20260818.py |
| description | TEXT |  | ✓ |  |  | what this behaviour class covers and how it's distinct from its neighbours | migration/bootstrap_behaviour_rules_v1_20260818.py |
| added_at | TEXT |  | ✓ |  |  | when the class was registered | migration/bootstrap_behaviour_rules_v1_20260818.py |
| inactive | INTEGER |  | ✓ |  |  | 0=active, 1=retired (kept for history) | migration/bootstrap_behaviour_rules_v1_20260818.py |

### cfg_behaviour_rule
_one row per rule within a behaviour class_ — the actual rule content per class -- worded as definitive statements, not open for interpretation (researcher instruction 2026-08-18). Replaces prose-only rules in CLAUDE.md/memory/wa_rule_registry as they're migrated in through later consolidation cycles.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate key | migration/bootstrap_behaviour_rules_v1_20260818.py |
| class | TEXT |  | ✓ |  |  | which cfg_behaviour_class this rule belongs to | migration/bootstrap_behaviour_rules_v1_20260818.py |
| rule_key | TEXT |  | ✓ |  |  | short kebab-case identifier, unique within its class | migration/bootstrap_behaviour_rules_v1_20260818.py |
| rule_text | TEXT |  | ✓ |  |  | the rule itself, as a definitive statement -- if the rule involves a choice, the choices and which applies when are spelled out here, not left implicit | migration/bootstrap_behaviour_rules_v1_20260818.py |
| source | TEXT |  | ✓ |  |  | provenance -- which prior rule/doc/researcher statement this was derived from | migration/bootstrap_behaviour_rules_v1_20260818.py |
| enforced_by | TEXT |  |  |  |  | the mechanical check that flags deviation from this rule, if one exists yet -- honestly NULL/'not yet' where none does (researcher instruction: deviation must be monitored ongoing, a follow-on build item) | migration/bootstrap_behaviour_rules_v1_20260818.py |
| added_at | TEXT |  | ✓ |  |  | when the rule was registered | migration/bootstrap_behaviour_rules_v1_20260818.py |
| active | INTEGER |  | ✓ |  |  | 0=retired, 1=live | migration/bootstrap_behaviour_rules_v1_20260818.py |
| enforcement_status | TEXT |  |  |  |  | Structured classification of HOW (or whether) this rule is actually enforced -- cfg_enum behaviour_rule_enforcement_status. Replaces free-text hedge-phrase matching in enforced_by (which let 44/64 active rows silently drift to "not yet mechanically checked" for weeks, escalation #1384) with a queryable field configmaint.validate can report on directly. | researcher audit instruction, this chat, 2026-09-03 |
| deliver_when | TEXT |  | ✓ |  |  | When the rule is delivered at session start and restated in the compliance file (lib/compliance.deliver_set): always; study_active (only while behaviour.study_state is 'active'); developer_mode (only in a Developer Mode session's compliance file). Escalation #2185. | migration/rule_delivery_scope_v1_20261021.py |

### cfg_meta
_one row per top-level app-identity key_ — core app-identity facts (which database this cfg_* store belongs to, the seeded config_version) — read once at startup to confirm identity before anything else runs.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| key | TEXT | ✓ |  |  |  | the identity fact's name, e.g. 'database', 'config_version' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| value | TEXT |  |  |  |  | the fact's value | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_table
_one row per registered table (database, name) — this row_ — the table-level half of governance.tables — every table across both project databases (bible_research/research_db and iba), what one row of it represents, and its overall purpose. Self-referential: this table registers itself.
dedup key: `database, name`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| database | TEXT |  | ✓ |  |  | which physical database this row describes -- part of the primary key (escalation #653: iba.db and bible_research.db genuinely share table names like word_registry/cluster/passage/verse for DIFFERENT tables). | migration/add_cfg_table_database_column.py |
| inactive | INTEGER |  | ✓ |  |  | a data table no longer in use (superseded, retired, or abandoned scaffolding) is marked inactive=1 here rather than deleted from cfg_table — governance.tables' own requirement, unsupported by schema until escalation #678's full table review made the gap concrete. Reverses bootstrap_inactive_column.py's (#310) earlier exclusion of cfg_table as 'schema-of-schema, not toggleable' — cfg_column/cfg_unique remain excluded, no comparable review driving a need for it there yet. | migration/add_cfg_table_inactive_column.py |
| name | TEXT |  | ✓ |  |  | the table's name | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| grain | TEXT |  |  |  |  | what one row of this table represents | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| use | TEXT |  |  |  |  | the table's purpose — why it exists, how it's used | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| category | TEXT |  |  |  |  | rule (a genuine cfg_* configuration table) \| data (a real data table, either database) \| log (an audit-log table sharing the cfg_ prefix by convention only, e.g. cfg_change_detail/cfg_change_log -- never a configmaint.propose write target). | escalation #1146, 2026-08-31 |

### cfg_column
_one row per column of a registered table (database, table_name, name)_ — the column-level half of governance.table_columns — every column's type, key/nullability flags, use text, and (for data-driven-enforced settings) the expectation pattern lib/valuequality.py checks it against. Self-referential: this table registers its own columns via the rows this very migration writes.
dedup key: `database, table_name, name`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| database | TEXT |  | ✓ |  |  | which physical database this row describes -- part of the primary key (escalation #653: iba.db and bible_research.db genuinely share table names like word_registry/cluster/passage/verse for DIFFERENT tables). | migration/add_cfg_table_database_column.py |
| table_name | TEXT |  |  |  |  | the table this column belongs to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| name | TEXT |  |  |  |  | the column's name | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| ordinal | INTEGER |  |  |  |  | declaration order within the table | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| type | TEXT |  |  |  |  | the column's SQL type (TEXT/INTEGER/...) | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| is_pk | INTEGER |  |  |  |  | 1 if part of the table's primary key | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| notnull | INTEGER |  |  |  |  | 1 if the column has a NOT NULL constraint | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| is_unique | INTEGER |  |  |  |  | 1 if the column has its own UNIQUE constraint (compound uniqueness across columns is cfg_unique's job instead) | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| dflt | TEXT |  |  |  |  | the column's declared SQL default, if any | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| fk | TEXT |  |  |  |  | the table.column this column references, if it's a foreign key | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| use | TEXT |  |  |  |  | what this column holds and how it's used | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| expectation | TEXT |  |  |  |  | for a data-driven-enforced value: 'pattern:<cfg_setting key>' or 'enum.<cfg_enum name>' — lib/valuequality.py's engine checks live values against this instead of a hardcoded rule | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| source | TEXT |  |  |  |  | where this column's value originates, if not obvious | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| filled_by | TEXT |  |  |  |  | the script/migration that populates this column | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| inactive | INTEGER |  | ✓ |  |  | a column that is declared but dead (never populated, or the concept it served is retired) is marked inactive=1 here -- symmetric with cfg_table.inactive (escalation #678), not DB-enforced (nothing stops a write to it), but makes the fact config-known and queryable. Escalation #833, researcher: 'this may not be DB enforceable, but at least it sets the config that the column is not used.' | migration/flag_management_build_v1_20260823.py |

### cfg_unique
_one row per column participating in a named table's compound-uniqueness rule_ — documents a compound (multi-column) uniqueness expectation for a table — table_name plus one row per participating column, ordinal giving the compound-key column order. A documentation/validation aid, not itself an enforced DB constraint.
dedup key: `database, table_name, col`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| database | TEXT |  | ✓ |  |  | which physical database table_name refers to -- part of the primary key (iba.db and bible_research.db share table names, e.g. 'passage', for different tables; escalations #653/#680 widened cfg_table/cfg_write_grant the same way, this closes the same gap for cfg_unique). Config differentiation only. | migration/add_cfg_unique_database_column_v1_20260818.py |
| table_name | TEXT |  |  |  |  | the table the uniqueness rule applies to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| col | TEXT |  |  |  |  | one column participating in the compound unique key | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| ordinal | INTEGER |  |  |  |  | this column's position within the compound key | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_enum
_one row per (name, value) enum membership_ — named controlled-vocabulary groups — lookups/options queried BY NAME at runtime (cfg.enum(name) or the equivalent raw SQL) rather than hardcoded as string literals in code, so a membership change is something the app actually notices.
dedup key: `name, value`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| name | TEXT |  |  |  |  | the enum group's name, e.g. 'config_module' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| value | TEXT |  |  |  |  | one member of the group | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| ordinal | INTEGER |  |  |  |  | display/insertion order within the group | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_connection
_one row per STEP-server connection parameter_ — STEP Bible local-server connection parameters (base_url, version, ...) — read at startup to build the live connection used by every raw.* STEP call.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| key | TEXT | ✓ |  |  |  | the parameter's name, e.g. 'base_url', 'version' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| value | TEXT |  |  |  |  | the parameter's value | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_api
_one row per named STEP REST API call this app is coded to use_ — the catalogue of STEP Bible REST API calls the app actually issues — route template (with {placeholders}), what input the caller supplies, and what shape the response returns. The IBA-side equivalent of scripts/analytics/step_client.py's method list.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| name | TEXT | ✓ |  |  |  | the call's short identifier, e.g. 'call1_meanings' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| route | TEXT |  |  |  |  | the REST route template, with {placeholder} segments | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| input | TEXT |  |  |  |  | what the caller must supply | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| returns | TEXT |  |  |  |  | what shape the response gives back | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_book_order
_one row per Bible book_ — canonical book ordering (Gen=0 .. Rev=65) for sorting/sequencing verse references app-wide — the IBA-side equivalent of research_db's books/book_code_variants tables.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| book | TEXT | ✓ |  |  |  | the book's short code, e.g. 'Gen' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| ordinal | INTEGER |  |  |  |  | 0-based canonical Bible order | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_candidate_rule
_one row per (kind, value) candidate-inclusion override_ — accept/reject overrides for candidate Strong's numbers considered during term/HIB candidate onboarding — kind names the rule type (currently only 'accept' is live), value is the Strong's number the rule applies to. -- INACTIVE 2026-08-18 (escalation #734): entire candidate subsystem (4 work packages, 6 steps, this table's 289 rows) retracted 2026-07-23, still fully inactive, no replacement landed. Table registration itself was never flipped until now.
dedup key: `kind, value`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| kind | TEXT |  |  |  |  | the rule type — currently only 'accept' is a live value | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| value | TEXT |  |  |  |  | the Strong's number (or other matched value) the rule covers | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_write_grant
_one row per (writer, table_name, database) write permission_ — governance.config_control's write-grant registry — which writer (a step name, or 'configmaint.propose' for the sanctioned manual-change gate) may write which table in which database. configmaint.validate's coherence check confirms every cfg_* table has at least one grant, or nothing could legitimately maintain it.
dedup key: `writer, table_name, database`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| writer | TEXT |  |  |  |  | the step/mechanism permitted to write — a dispatcher step name, or 'configmaint.propose' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| table_name | TEXT |  |  |  |  | the table this writer may write to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| database | TEXT |  | ✓ |  |  | which physical database table_name refers to -- part of the primary key (escalation #680: iba.db and bible_research.db share table names for different tables). Config differentiation only -- no runtime cross-database write mechanism exists yet, see handlers/wordaudit.py's module docstring. | migration/add_cfg_write_grant_database_column.py |

### cfg_work_package
_one row per top-level invokable work package_ — the dispatcher's top-level package registry — its PowerShell entry script, what it runs over (a word, a book, 'none', ...), whether its steps chain automatically once triggered, and the user-facing complete/paused/next-step messages a PS wrapper shows.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| name | TEXT | ✓ |  |  |  | the work package's name, e.g. 'configuration-maintenance' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| ps_script | TEXT |  |  |  |  | the PowerShell entry-point script for this package | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| runs_over | TEXT |  |  |  |  | what one invocation operates over — a word, a book, a run, 'none', etc. | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| chained | INTEGER |  |  |  |  | 1 if this package's steps run automatically in sequence once triggered, 0 if each step is invoked independently | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| complete_message | TEXT |  |  |  |  | message shown to the researcher on successful completion | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| next_step_hint | TEXT |  |  |  |  | suggested next action shown after completion | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| paused_message | TEXT |  |  |  |  | message shown when a step pauses awaiting a decision | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_step
_one row per (work_package, step)_ — the dispatcher's step registry — which handler function runs for a named step within a work package, what scope it needs, a human description of what it does, and its kind ('utility' = this app's own running; 'operations' = substantive analytic/study content).
dedup key: `work_package, step`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| work_package | TEXT |  |  |  |  | the owning work package | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| kind | TEXT |  | ✓ |  |  | operations (does the study work — raw/registry/lexicon/passage-debate-prep/narrative) or utility (supports the app's own running — configmaint, general reporting). REQUIRED for dispatch — run.py refuses a step with no kind (escalation, 2026-07-30). | migration/bootstrap_step_kind.py |
| ordinal | INTEGER |  |  |  |  | this step's position within its package | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| step | TEXT |  |  |  |  | the step's dotted name, e.g. 'configmaint.validate' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| handler | TEXT |  |  |  |  | the Python handler function this step dispatches to, as 'module:function' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| scope | TEXT |  |  |  |  | what this step needs scoped to it to run — a word, 'none', etc. | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| does | TEXT |  |  |  |  | a human-readable description of what this step actually does | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_status_flow
_one row per (entity, status) lifecycle stage_ — the ordered status lifecycle for a named entity (e.g. 'word') — which step sets each status, and its position in the sequence, so a status transition can be validated against a declared order rather than assumed.
dedup key: `entity, status`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| entity | TEXT |  |  |  |  | the entity whose lifecycle this describes, e.g. 'word' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| status | TEXT |  |  |  |  | one status value in that entity's lifecycle | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| set_by | TEXT |  |  |  |  | which step/mechanism sets this status | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| ordinal | INTEGER |  |  |  |  | this status's position in the lifecycle sequence | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_on_fail
_one row per (step, condition) failure-routing rule_ — how a named step should react to a named failure condition — path (the actual routing outcome: 'report-stop' or 'pause-continue'), an optional resolver, the message shown, and route (a routing category — currently always 'terminal', reserved for future non-terminal routing types).
dedup key: `step, condition`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| step | TEXT |  |  |  |  | the step this failure-routing rule applies to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| condition | TEXT |  |  |  |  | the named failure condition, e.g. 'word-exists' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| path | TEXT |  |  |  |  | the actual routing outcome — 'report-stop' (hard stop) or 'pause-continue' (escalate and wait for a decision) | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| resolver | TEXT |  |  |  |  | an optional handler that can auto-resolve this condition, if one exists | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| message | TEXT |  |  |  |  | the message shown to the researcher/Claude for this condition | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| route | TEXT |  | ✓ |  |  | a routing category — currently always 'terminal' across every live row; reserved for a future non-terminal routing type | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_report
_one row per report-producing step's report shape_ — report-generation shape for a step per governance.reports_must_persist — title, whether to show a table of contents, output format(s) (md/md+csv), naming scheme (stable = fixed filename, dated = versioned per governance.oneoff_report_naming_pattern), and archive folder for superseded versions.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| step | TEXT | ✓ |  |  |  | the report-producing step this shape applies to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| title | TEXT |  | ✓ |  |  | the report's title | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| show_toc | INTEGER |  | ✓ |  |  | 1 if the report includes a table of contents | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| footer_text | TEXT |  |  |  |  | optional footer text appended to the report | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| output_kind | TEXT |  | ✓ |  |  | the output format(s) produced — 'md' or 'md+csv' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| naming_scheme | TEXT |  | ✓ |  |  | 'stable' (fixed filename, overwritten/archived on regenerate) or 'dated' (versioned filename per report) | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| archive_dir | TEXT |  | ✓ |  |  | where a superseded 'stable'-scheme report is archived | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_report_section
_one row per (step, section_key) report section_ — the section layout of a generated report — ordinal position, the markdown heading text, an optional shorter table-of-contents label, and whether the section is actually included in a live regenerate.
dedup key: `step, section_key`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| step | TEXT |  | ✓ |  |  | the report-producing step this section belongs to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| ordinal | INTEGER |  | ✓ |  |  | the section's position in the report | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| section_key | TEXT |  | ✓ |  |  | the section's stable identifier | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| heading | TEXT |  | ✓ |  |  | the markdown heading text rendered for this section | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| toc_label | TEXT |  |  |  |  | a shorter label for the table of contents, if different from the heading | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| include | INTEGER |  | ✓ |  |  | 1 if this section is actually rendered | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_report_csv_table
_one row per (step, table_name) CSV-export target within a report_ — which table(s) a report step's CSV output covers — join_note describes a multi-table join in plain language where table_name isn't a literal single table, and virtual=1 flags a computed/derived result set (a name that doesn't resolve to a literal live table — escalation #642 found two such rows naming non-existent tables, left open for researcher judgement, not fixed by this backfill).
dedup key: `step, table_name`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| step | TEXT |  | ✓ |  |  | the report-producing step this CSV export belongs to | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| table_name | TEXT |  | ✓ |  |  | the table (or, if virtual=1, the named derived result set) this CSV covers | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| join_note | TEXT |  |  |  |  | plain-language description of a multi-table join, if the export isn't a single verbatim table | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| virtual | INTEGER |  | ✓ |  |  | 1 if table_name is a computed/derived name rather than a literal live table | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_change_log
_one row per whole-store config reload/load event_ — audit trail of cfg_* seed reloads — config_version and seed_hash (change-detection fingerprint), when the load happened, and whether it validated clean. Whole-reload events only; row-level individual changes are cfg_change_detail instead.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate key | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| config_version | TEXT |  |  |  |  | the app's config_version string at the time of this load | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| seed_hash | TEXT |  |  |  |  | a hash of the seed content, for change detection | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| loaded_at | TEXT |  |  |  |  | when this load happened | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| validated | INTEGER |  |  |  |  | 1 if this load passed validation | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_setting
_one row per named setting key_ — flat key/value application settings, grouped by module (cfg_setting.module) — the app's primary tunable-configuration store, read at runtime via cfg.setting(key). module='governance' rows are the special case: process rules for the AI/researcher workflow, not runtime-applied values.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| key | TEXT | ✓ |  |  |  | the setting's dotted key, e.g. 'governance.reports_must_persist' | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| module | TEXT |  | ✓ |  |  | which module/utility owns this setting — every setting must have one, per the researcher's 2026-07-21 rule against cfg_setting becoming a catch-all | configmaint.propose |
| inactive | INTEGER |  | ✓ |  |  | deactivate this config row without deleting it — excluded from configmaint.validate's coherence/orphan/justification checks, listed separately (not silently dropped) in configmaint.report. Set via the normal configmaint.propose update path, same as any other cfg_* value. | configmaint.propose |
| value | TEXT |  |  |  |  | the setting's value, JSON-encoded | migration/backfill_foundational_cfg_tables_v1_20260818.py |
| use | TEXT |  |  |  |  | what this setting controls and why | migration/backfill_foundational_cfg_tables_v1_20260818.py |

### cfg_utility
_one row per registered script/library module_ — the registry of every script/routine in the project per governance.scripts_and_routines — its file path, purpose (usually from the file's own docstring), whether retired, and whether it's exempt from the config-usage completeness check (config_exempt=1, with a required reason) for a legitimate structural reason — e.g. it IS the config reader, or it writes cfg_* directly via raw sqlite3 rather than reading it.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| module | TEXT | ✓ | ✓ |  |  | the lib module's own name (no .py, no package prefix) | migration/bootstrap_cfg_utility.py |
| file_path | TEXT |  | ✓ |  |  | path from the repo root, e.g. iba/app/lib/stepapi.py | migration/bootstrap_cfg_utility.py |
| purpose | TEXT |  |  |  |  | first line of the module's own docstring, verbatim | migration/bootstrap_cfg_utility.py |
| inactive | INTEGER |  | ✓ |  |  | deactivate this registry row without deleting it (module removed/merged) — same convention as every other cfg_* table's inactive column | migration/bootstrap_cfg_utility.py |
| config_exempt | INTEGER |  | ✓ |  |  | 1 = a legitimate zero for config-setting/enum usage (caller resolves it, or this module IS the config layer) — declared, not re-derived every validate run. 0 = subject to the usual finding. | migration/add_cfg_utility_config_exempt.py |
| config_exempt_reason | TEXT |  |  |  |  | why this module is exempt — required whenever config_exempt=1 so the flag never sits undocumented. | migration/add_cfg_utility_config_exempt.py |
| crash_escalation_reviewed | INTEGER |  | ✓ |  |  | 1 once this module's crash-recovery behaviour (does a mid-write failure roll back cleanly, does it record itself) has been genuinely reviewed, not bulk-defaulted (D3, register v9). 0 = not yet reviewed. |  |
| crash_escalation_note | TEXT |  |  |  |  | The genuine finding from that review -- what actually happens if this module's write crashes mid-transaction. NULL until crash_escalation_reviewed=1. |  |

### cfg_prose_concept
_one row per key project concept pointed at its defining prose location_ — a pointer index: 'this concept is DEFINED at this chapter/section of the prose' -- not a copy of the definition. Direct replacement mechanism for wa_rule_registry rows like GR-PROG-001/GR-PROG-002 that used to restate a definition as rule text; this points at the authoritative prose instead, per cfg_behaviour_rule 'documentation.single-authority-pointer-not-copy'.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| concept_key | TEXT | ✓ | ✓ |  |  | short kebab/snake-case identifier, e.g. 'verse_primacy' | migration/bootstrap_prose_authority_v1_20260818.py |
| chapter | INTEGER |  | ✓ |  |  | which chapter (0-6) this concept belongs to, per prose_section_type.chapter_no in bible_research.db -- no longer FK'd to a table; cfg_prose_chapter removed 2026-08-27, escalation #918 | migration/bootstrap_prose_authority_v1_20260818.py |
| section_hint | TEXT |  | ✓ |  |  | which section(s) within the chapter, in plain language (prose sections aren't independently keyed yet) | migration/bootstrap_prose_authority_v1_20260818.py |
| description | TEXT |  | ✓ |  |  | a short gloss of the concept, for discoverability -- the prose itself remains authoritative for the full definition | migration/bootstrap_prose_authority_v1_20260818.py |
| source | TEXT |  | ✓ |  |  | provenance -- which prior rule/decision this concept pointer replaces or derives from | migration/bootstrap_prose_authority_v1_20260818.py |
| added_at | TEXT |  | ✓ |  |  | when this concept was registered | migration/bootstrap_prose_authority_v1_20260818.py |

### escalation
_one row per item, current status_ — One row per item, CURRENT STATE ONLY. NOT redundant with escalation_history -- history stores true per-version deltas (most fields NULL per row); escalation is the only place the full current state is materialised. Ids continue from escalations_old's max (735) once D1's rebuild lands (register v9, escalation-design-decision-register-v9-20260821).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | serial PK, 4-digit display; continues from escalations_old's max (735) so ids stay unambiguous across the cutover |  |
| version | INTEGER |  | ✓ |  |  | current version number for this id -- count of its escalation_history rows; the NNNN-NN display format is id+version, not a stored key | escalation.raise_new/update |
| run_id | TEXT |  |  |  |  | restored 2026-08-20 (v1 dropped it, broke dispatch, rolled back -- BUILD.md §152/§153). Set for a DISPATCHER-TIED item (a real run.py pause, correlates back to the run being resumed) or a synthetic MANUAL-<timestamp> for a manual item. NULL for neither. | escalation.raise_/raise_new |
| source | TEXT |  | ✓ |  |  | what triggered the item: script name \| module \| issue area. Immutable after Raise. | escalation.raise_new |
| at_step | TEXT |  |  |  |  | pipeline reference, only set if code-generated/run-error. Immutable after Raise. | escalation.raise_new |
| type | TEXT |  | ✓ |  |  | differentiates the kind of item | escalation.raise_new |
| short_description | TEXT |  | ✓ |  |  | label/title -- what this item is about. IMMUTABLE after Raise (plan v3 §3) -- a wrong title is corrected by raising a new item with state=supersede on the old one (plan v3 §4), never edited in place. | escalation.raise_new |
| context | TEXT |  |  |  |  | what must be done or the error message, plus links to external documents. Cumulative: an Update's input is the increment, appended onto the current value (plan v3 §2). | escalation.raise_new/update |
| comment | TEXT |  |  |  |  | additional information for the assigned party. Cumulative, same rule as context. | escalation.raise_new/update |
| tried | TEXT |  |  |  |  | the corrective action taken -- REQUIRED when next_action_assigned_to=Claude and a prior corrective action failed (plan v3 §6/v2 §6). | escalation.update |
| state | TEXT |  | ✓ |  |  | current status -- raised at Raise; mostly logic-derived on Update per the auto-state rules (plan v3 §3), some values either-party-settable (on-hold/in-progress/closed). | escalation.raise_new/update |
| next_action | TEXT |  |  |  |  | what's expected of the current reader (incoming) / what the next reader should do (outgoing) -- TWO vocabularies share this column: dispatcher-tied (approve/reject/revise/hold/noted, unchanged) and manual (ready_for_approval/approved/reject/revise/noted/review) -- see lib/escalation.py module docstring, 2026-08-20. | escalation.raise_new/update |
| next_action_assigned_to | TEXT |  |  |  |  | Claude \| Researcher | escalation.raise_new/update |
| originator | TEXT |  |  |  |  | who created the latest escalation_history row -- auto-populated, replaces `answered_by`. Not caller-supplied. | escalation.raise_new/update |
| resolution | TEXT |  |  |  |  | what was actually done -- REQUIRED when next_action=approved (validity check, plan v3 §3). | escalation.update |
| raised_at | TEXT |  | ✓ |  |  | first creation datetime -- set once, immutable | escalation.raise_new |
| answered_at | TEXT |  |  |  |  | mirrors the latest escalation_history row's timestamp | escalation.update |
| resolution_kind | TEXT |  |  |  |  | decision_required or self_correctable (cfg_enum resolution_kind) -- required at Raise, escalation #798/#799. decision_required is terminal and routes to design; self_correctable is fixed directly by Claude, no approval gate. Mutable in one direction only: self_correctable -> decision_required via escalate_to_decision(), never the reverse. | iba/app/migration/add_resolution_kind_column_v1_20260822.py |
| needs_claude_followup | INTEGER |  | ✓ |  |  | Set by Claude at Raise or at the ready_for_approval Update: this item still needs a further action from Claude AFTER the researcher approves it (a config apply, a build step) before it is genuinely done. Consumed by cfg_escalation_transition (escalation #1075) so approved+this flag routes back to Claude (re-assigned) instead of straight to completed. | escalation #1075, 2026-08-30 |
| alias | TEXT |  |  | ✓ |  | OT-nn for type='thread' (assigned automatically at Raise: the next OT number); NULL for other types. Unique where set (index idx_escalation_alias). Escalation.ps1 -Id accepts it anywhere an id is taken. Immutable after Raise. escalation #2000 | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| comes_back_when | TEXT |  |  |  |  | the thread's 'comes back when' text, whole, as a person reads it; the matchable parts are escalation_thread_item rows. Replace column (Update -ComesBackWhen). escalation #2000 | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |

### escalation_history
_one row per update to an item, ever_ — One row per update to an item, ever -- append-only, a TRUE DELTA per version (most fields NULL per row unless that version's own transaction set them), not a full snapshot. Envelope fields (state/next_action/next_action_assigned_to/originator/answered_at) always populated; content fields (comment/context/resolution/tried/short_description/related_activity) NULL unless touched this version. escalation is the current-state materialisation of the latest row here, not the reverse.
dedup key: `escalation_id, version`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK, row order = write order |  |
| escalation_id | INTEGER |  | ✓ |  | escalation.id | which item this snapshot belongs to | escalation.raise_new/update |
| version | INTEGER |  | ✓ |  |  | this item's version number at the time of this snapshot -- matches escalation.version at the moment this row was the latest | escalation.raise_new/update |
| run_id | TEXT |  |  |  |  | snapshot of escalation.run_id (constant per item) |  |
| source | TEXT |  |  |  |  | delta: NULL after v1 unless source is corrected (it normally never changes after creation) -- was wrongly NOT NULL under the retired full-snapshot design |  |
| at_step | TEXT |  |  |  |  | snapshot of escalation.at_step at this version |  |
| type | TEXT |  |  |  |  | delta: NULL after v1 unless type is corrected -- was wrongly NOT NULL under the retired full-snapshot design |  |
| short_description | TEXT |  |  |  |  | delta: NULL after v1 unless the title is explicitly corrected (rare, exceptional) -- was wrongly NOT NULL under the retired full-snapshot design |  |
| context | TEXT |  |  |  |  | delta: the raw increment THIS version added, NULL if this version didn't touch it -- same correction as comment, above |  |
| comment | TEXT |  |  |  |  | delta: the raw increment THIS version added, NULL if this version didn't touch it -- was wrongly 'full cumulative text' under the retired full-snapshot design (that design wiped 2026-08-20, researcher: 'the cumulative is only in escalation') |  |
| tried | TEXT |  |  |  |  | snapshot of escalation.tried at this version |  |
| state | TEXT |  | ✓ |  |  | snapshot of escalation.state at this version |  |
| next_action | TEXT |  |  |  |  | snapshot of escalation.next_action at this version |  |
| next_action_assigned_to | TEXT |  |  |  |  | snapshot of escalation.next_action_assigned_to at this version |  |
| originator | TEXT |  |  |  |  | who created THIS specific snapshot -- the real per-update author, never overwritten by a later row (this is the fix for #715's loss) | escalation.raise_new/update |
| resolution | TEXT |  |  |  |  | snapshot of escalation.resolution at this version |  |
| raised_at | TEXT |  |  |  |  | delta, structural: only ever set at v1 (the item's true creation time; never changes) -- was wrongly NOT NULL every version under the retired full-snapshot design |  |
| answered_at | TEXT |  | ✓ |  |  | THIS row's own write timestamp -- the real per-update datetime | escalation.raise_new/update |
| needs_claude_followup | INTEGER |  | ✓ |  |  | Mirrors escalation.needs_claude_followup -- envelope column, always populated per version, same as state/next_action/resolution_kind. | escalation #1075, 2026-08-30 |
| resolution_kind | TEXT |  |  |  |  | per-version snapshot of escalation.resolution_kind at that version. | iba/app/migration/add_resolution_kind_column_v1_20260822.py |
| alias | TEXT |  |  |  |  | per-version copy of escalation.alias (set at v1 only -- immutable). escalation #2000 | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| comes_back_when | TEXT |  |  |  |  | delta: set only on the version that set it. escalation #2000 | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |

### cfg_escalation_transition
_one row per (shape, priority) state-derivation rule_ — The escalation state-derivation rule engine, evaluated in priority order per shape -- replaces the hardcoded if/elif chain _derive_state()/_terminal_state_for() used to be. Built 2026-08-20 as part of the post-reset rebuild (escalation-rebuild-design-v1).
dedup key: `shape, priority`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| priority | INTEGER |  | ✓ |  |  | evaluation order within its shape, ascending, first match wins |  |
| shape | TEXT |  | ✓ |  |  | 'manual' or 'dispatcher' -- which vocabulary/function this rule belongs to |  |
| next_action | TEXT |  |  |  |  | which next_action this rule matches, or NULL to match any |  |
| condition_key | TEXT |  | ✓ |  |  | named condition the code evaluates (escalation-rebuild-design-v1 sec2.4) -- a fixed small vocabulary, not a general expression language |  |
| resulting_status_key | TEXT |  | ✓ |  |  | substring matched against cfg_status_flow.set_by (entity=escalation) to resolve the target status |  |
| notes | TEXT |  |  |  |  | why this rule exists / provenance |  |
| active | INTEGER |  | ✓ |  |  | inactive rows are skipped during evaluation |  |

### cfg_escalation_requirement
_one row per (action, field) validation rule_ — Which fields are required for which escalation action (comment@raise, resolution@approved, etc), and under what named condition. Built 2026-08-20, same rebuild.
dedup key: `action, field, check_kind`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| action | TEXT |  | ✓ |  |  | 'raise', or a next_action value -- which transaction this requirement applies to |  |
| field | TEXT |  | ✓ |  |  | the escalation column that must be filled in |  |
| condition_key | TEXT |  | ✓ |  |  | 'always', or a named condition gating when the requirement applies |  |
| message | TEXT |  | ✓ |  |  | shown to the caller when the requirement is violated |  |
| active | INTEGER |  | ✓ |  |  | inactive rows are skipped |  |
| check_kind | TEXT |  | ✓ |  |  | which comparison lib/escalation.py._check_requirements runs: 'field_required' (value must be truthy -- the original, only, implicit behaviour before this column existed), 'not_raised_with_content' (value must NOT be 'raised'), 'exists' (value, if set, must reference a real escalation id), 'not_self' (value, if set, must not equal the item's own id). Added 2026-08-21, register v9 D14/D25/D26. |  |

### cfg_passage
_one row per key_ — Module-specific settings for the passage module (governance.module.config) -- replaces module=passage rows formerly in the shared cfg_setting table.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| key | TEXT | ✓ | ✓ |  |  | the setting's key, e.g. 'passage.quality_report_path' -- kept identical to the prior cfg_setting key text so no caller string changes, only the table read from | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py |
| value | TEXT |  |  |  |  | JSON-encoded value, same convention as cfg_setting.value | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py |
| use | TEXT |  |  |  |  | what the setting controls and why | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py |
| inactive | INTEGER |  | ✓ |  |  | soft-disable flag, same convention as cfg_setting | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py |

### cfg_prose
_one row per key_ — Module-specific settings for the prose module (governance.module.config) -- chapter_names/book_stage_map/search_default_limit/edit_file_dir, escalation #829.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| key | TEXT | ✓ | ✓ |  |  | the setting's key, e.g. 'prose.book_stage_map' -- kept identical to the pre-#829 cfg_setting key text so no caller string changes, only the table read from | migration/prose_first_layer_build_v1_20260824.py |
| value | TEXT |  | ✓ |  |  | JSON-encoded value, same convention as cfg_setting.value | migration/prose_first_layer_build_v1_20260824.py |
| use | TEXT |  | ✓ |  |  | what the setting controls and why | migration/prose_first_layer_build_v1_20260824.py |
| inactive | INTEGER |  | ✓ |  |  | soft-disable flag, same convention as cfg_setting | migration/prose_first_layer_build_v1_20260824.py |

### file_manifest
_one row per file_ — Filename/path metadata for every file in the project tree (18,653 rows at registration time, 2026-08-28) -- built by lib/manifest.py:rebuild(), a full-tree walk. Content is never read, only path/name/size/mtime facts. Was live and populated for 13 days before being registered here (escalation #972's own orphan check caught the gap while grounding escalation #971).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| path | TEXT | ✓ |  | ✓ |  | Project-root-relative path (POSIX slashes) of the file. Primary key -- one row per file. |  |
| category | TEXT |  | ✓ |  |  | Coarse classification (iba/session/script/cluster/discovery/workflow/investigation/patch/report/doc/log/directive/code/export/import/backup/other) -- computed by lib/manifest.py:classify_category() from the path's leading folder segments, project-naming FACT not cfg_setting. folder_purpose.manifest_category (escalation #971) will become the primary source once built, this classifier the fallback for any folder not yet registered. |  |
| file_type | TEXT |  | ✓ |  |  | Finer-grained type within category, e.g. 'iba-lib', 'analysis-patch' -- lib/manifest.py:classify_type(). |  |
| currency | TEXT |  | ✓ |  |  | current/archived/cross-reference/historical/backup/other -- lib/manifest.py:compute_currency(), same fallback relationship to folder_purpose. |  |
| archived | INTEGER |  | ✓ |  |  | 1 iff currency='archived' (path contains an archive/ segment) -- redundant with currency, kept for cheap WHERE archived=1 filtering. |  |
| registry | INTEGER |  |  |  |  | word_registry id extracted from the filename, when the naming pattern carries one -- NULL for files not tied to a specific word registry. |  |
| word | TEXT |  |  |  |  | English word extracted from the filename, when present. |  |
| cluster | TEXT |  |  |  |  | M-code cluster extracted from the filename, when present. |  |
| vcb_batch | INTEGER |  |  |  |  | Verse-context-batch number extracted from the filename, when present -- legacy Session B naming. |  |
| version | TEXT |  |  |  |  | The -v{n} version suffix extracted from the filename, when present. |  |
| date | TEXT |  |  |  |  | Date extracted from the filename (compact or hyphenated), when present. |  |
| ext | TEXT |  |  |  |  | File extension, lowercase, including the leading dot. |  |
| size_bytes | INTEGER |  | ✓ |  |  | File size in bytes at scan time. |  |
| modified_at | TEXT |  | ✓ |  |  | The file's own filesystem mtime, UTC ISO-8601. |  |
| scanned_at | TEXT |  | ✓ |  |  | When this row was written by manifest.rebuild() -- identical across every row from the same run; a full rebuild replaces the table's contents rather than updating in place. |  |

### folder_purpose
_one row per governed folder_ — Reference/data table (like bible_research.db's books, NOT a cfg_* rule table) -- one row per folder in the project tree, seeded from a full census (outputs/folder-census-20260828.csv, 793 folders). Gives the researcher visibility into every live folder's purpose/status and lets folder-classifying code (lib/manifest.py) read a governed source instead of hardcoded prefix rules. Escalation #971, iba/docs/971-folder-purpose-governance-plan-v5-20260828.md.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| folder_path | TEXT | ✓ |  | ✓ |  | Project-root-relative folder prefix, POSIX slashes, no trailing slash. Primary key -- one row per governed folder, seeded from a full census of every directory in the tree. |  |
| top_level_root | TEXT |  | ✓ |  |  | First path segment (or '(repo root)' for the root itself) -- cheap grouping/filter key. |  |
| depth | INTEGER |  | ✓ |  |  | Path segment count; 0 = repo root. |  |
| parent_path | TEXT |  | ✓ |  |  | This folder's immediate parent's folder_path. |  |
| direct_file_count | INTEGER |  | ✓ |  |  | Files directly in this folder, not counting subfolders -- refreshed by the manifest-validate method (Method A) on every manifest rebuild, never hand-edited. |  |
| recursive_file_count | INTEGER |  | ✓ |  |  | Files in this folder and everything under it -- Method A-refreshed. |  |
| direct_subfolder_count | INTEGER |  | ✓ |  |  | Immediate child folders -- Method A-refreshed. |  |
| top_ext_direct | TEXT |  |  |  |  | Up to 5 file extensions by count among this folder's direct files -- Method A-refreshed. |  |
| last_modified_direct | TEXT |  |  |  |  | Latest mtime among this folder's direct files, UTC ISO-8601 -- Method A-refreshed. |  |
| governed_by_setting | TEXT |  |  |  |  | Which cfg_setting key(s) already point at this exact folder path (semicolon-joined if more than one) -- refreshed by the configmaint cross-check (Method B), config-side truth, distinct from Method A's disk-side truth because a setting can change with no file moving. |  |
| manifest_category | TEXT |  |  |  |  | What file_manifest.category a file in this folder should get once folder_purpose becomes the manifest's primary classification source (escalation #971 Part D) -- NULL until set. |  |
| manifest_currency | TEXT |  |  |  |  | Same, for file_manifest.currency -- NULL until set. |  |
| type | TEXT |  |  |  |  | archive\|operations\|results (cfg_enum folder_purpose_type) -- the researcher-facing coarse classification, hand-set via FolderPurpose.ps1 (Method C), never touched by Methods A/B. |  |
| status | TEXT |  |  |  |  | authoritative\|mixed\|reallocate\|stale\|deleted (cfg_enum folder_purpose_status) -- 'deleted' is set by Method A when a folder no longer exists on disk (soft delete, row never removed); the other four values are hand-set via Method C. |  |
| usage_description | TEXT |  |  |  |  | Free-text description of what this folder is actually for, in the cfg_table.use/cfg_column.use style, scoped to a folder -- hand-set via Method C. |  |
| added_at | TEXT |  | ✓ |  |  | When this row was first created. |  |
| last_reviewed_at | TEXT |  |  |  |  | When type/status/usage_description were last confirmed accurate via Method C -- lets Method A/B flag a row whose judgement fields haven't been reviewed since its disk facts changed. |  |

### content_index
_one row per (key_type, key_value, file_path, line_number)_ — Content-index search: one row per indexed hit -- a key (e.g. an escalation id, a Strong number) found at a specific file/line, with a text snippet. Currently 0 rows -- report.content_index_search/rebuild exist but escalation #770 (on-hold) judged the current design unsupportable at scale; not yet populated.
dedup key: `key_type, key_value, file_path, line_number`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| key_type | TEXT |  | ✓ |  |  | Kind of key indexed (e.g. escalation id, Strong number) -- part of the composite PK. | escalation #1063 followup, 2026-08-30 |
| key_value | TEXT |  | ✓ |  |  | The actual key value indexed -- part of the composite PK. | escalation #1063 followup, 2026-08-30 |
| file_path | TEXT |  | ✓ |  |  | File the key was found in -- part of the composite PK. | escalation #1063 followup, 2026-08-30 |
| line_number | INTEGER |  | ✓ |  |  | Line the key was found at -- part of the composite PK. | escalation #1063 followup, 2026-08-30 |
| snippet | TEXT |  | ✓ |  |  | Text snippet around the match, for display. | escalation #1063 followup, 2026-08-30 |
| indexed_at | TEXT |  | ✓ |  |  | When this hit was indexed. | escalation #1063 followup, 2026-08-30 |

### content_index_scan
_one row per file_path_ — Content-index incremental-scan state: last-scanned mtime per file, so a rebuild only re-indexes changed files. Currently 0 rows, same status as content_index (escalation #770, on-hold).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| file_path | TEXT | ✓ |  |  |  | File path, primary key -- one row per scanned file. | escalation #1063 followup, 2026-08-30 |
| mtime | TEXT |  | ✓ |  |  | File modification time at last scan, so a rebuild only re-indexes changed files. | escalation #1063 followup, 2026-08-30 |
| scanned_at | TEXT |  | ✓ |  |  | When this file was last scanned. | escalation #1063 followup, 2026-08-30 |

### cfg_table_purpose
_one row per (table_name, kind)_ — Per genuine cfg_* RULE table (never a data table, never a demoted log table like cfg_change_detail/cfg_change_log), exactly 2 rows: purpose (why it exists, what it does, its scope) and success (the falsifiable test for whether it is working). Defined before investigating a table, not derived after the fact -- a working reminder for Claude, escalation #1130.
dedup key: `table_name, kind`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| table_name | TEXT |  | ✓ |  |  | cfg_table.name of the rule table this entry is about. | escalation #1130, 2026-08-30 |
| kind | TEXT |  | ✓ |  |  | purpose \| success. | escalation #1130, 2026-08-30 |
| text | TEXT |  |  |  |  | The actual statement -- one sentence to a short paragraph. | escalation #1130, 2026-08-30 |

### verse_lexical_note
_one row per (verse_lexical_id, note_type) — the judgement-bearing Layer-2 finding for one code, one test_ — Stage 1 Layer 2 output. Written by lexical.enrich, one passage-block at a time. FK to verse_lexical; passage_id/verse_id denormalized matching phenomenon's own precedent. NOT read by Window 2's phenomenon/operation writers (no FK link this increment — Window 2's own future design decision, #1383 v23).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER PK |  | ✓ |  |  | surrogate PK | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| verse_lexical_id | INTEGER |  | ✓ |  | verse_lexical.id | the code-row this note is about | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| verse_id | INTEGER |  | ✓ |  | verse.id | denormalized, matches phenomenon's own precedent | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| passage_id | INTEGER |  | ✓ |  | passage.id | denormalized, matches phenomenon's own precedent | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| note_type | TEXT |  | ✓ |  |  | cfg_enum note_type -- idiom / pronoun_resolution / noun_relational / noun_severity / chain / connective / related_word / polarity / entity_link / inert / structural_pattern / recurrence_role_shift / cross_lemma_shared_gloss / verb_argument / compound_unit | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| resolution_status | TEXT |  | ✓ |  |  | cfg_enum resolution_status — resolved / unresolved / unclassified / not_supported_this_language / checked_empty | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| target_verse_lexical_id | INTEGER |  |  |  | verse_lexical.id | same-verse OR cross-verse (within the loaded passage-block) resolution target (pronoun/noun/entity-link), NULL if unresolved. Also used by verb_argument notes as the agent/trigger of a movement (e.g. note id 346, Gen H5414G 'gave': target=Laban, the giver) -- a third, distinct use beyond the original pronoun/entity-link framing, added escalation #1607/D9, 2026-09-10. | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| related_verse_lexical_ids | TEXT |  |  |  |  | JSON array of ids -- structural_pattern/recurrence_role_shift rows only, PLUS verb_argument's recipient/impact use (e.g. note id 346, Gen H5414G 'gave': related=Leah, the recipient) -- a third, distinct use added escalation #1607/D9, 2026-09-10. | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| value_text | TEXT |  |  |  |  | the finding itself, free text — content shape varies too much by note_type for typed columns yet | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| evidence_text | TEXT |  |  |  |  | what in the verse's own data supports it (morph marker, related-word pull, etc.) | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete, same convention as every other iba.db table | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |

### cfg_lexical_code_class
_one row per (strong_code, class) — a code-classification lexicon entry_ — The single home for every mechanical code-classification lookup this build needs (negator, connective-type, party-kind lexicons) — governance.rules_must_be_config_driven; queried by lexical.build/lexicalenrich.py, never hardcoded. Rows are configmaint.propose-gated, same as every other cfg_* table.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER PK |  | ✓ |  |  | surrogate PK | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| strong_code | TEXT |  | ✓ |  | strong.strongNumber | the code this classification applies to | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| class | TEXT |  | ✓ |  |  | cfg_enum lexical_code_class — negator / connective_causal / connective_coordinating / connective_purpose / party_divine / party_human / party_angelic | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| evidence_note | TEXT |  | ✓ |  |  | why this code is classed this way — traceable-by-construction, never a bare assertion | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |
| active | INTEGER |  | ✓ |  |  | 1 = live lookup row; 0 = retired classification, kept for history | 1383-verse-lexical-window1-full-build-specification-v1-20260904.md |

### verse_meta
_one row per verse (1:1 with verse.id)_ — Verse-level base-data companion to `verse` -- collates language/testament/chapter/verse_num/passage linkage once at the right grain, instead of denormalizing per-code (the old `language` source) or leaving facts homeless (`genre`, `lexical_complete_at`). Auto-synced via 4 triggers on verse/verse_lexical/verse_passage inserts and verse.deleted updates -- never written to directly by application code. Escalation #1608, 2026-09-09.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |  | surrogate PK | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| verse_id | INTEGER |  | ✓ | ✓ | verse.id | the verse this row is about -- unique, one row per verse | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| testament | TEXT |  |  |  |  | 'OT'/'NT', derived from cfg_book_order.ordinal<=38 -- pure function of the verse's own book, no dependency on any other table. Set by verse_meta_on_verse_insert, immutable thereafter (a verse never changes book). | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| language | TEXT |  |  |  |  | 'Hebrew'/'Greek' in practice (domain also allows 'Aramaic' for forward-compatibility, but strong.language never carries it corpus-wide -- checked live 2026-09-09, even H0762 'Aramaic' itself is tagged Hebrew, so this column CANNOT distinguish genuine Aramaic portions). Majority vote across the verse's own live verse_lexical rows (verse_meta_on_lexical_change), testament-based default when none exist yet. Real value: surfaces a per-code language OUTLIER as a data-quality signal (e.g. John.1.18/H5207, a mistagged code) that a testament-only guess would never catch, not language diversity. | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| chapter | INTEGER |  |  |  |  | parsed once from osisId (Book.NN.NN) | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| verse_num | INTEGER |  |  |  |  | parsed once from osisId (Book.NN.NN) | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| passage_id | INTEGER |  |  |  | passage.id | via the verse_passage junction (verse_id unique, one passage per verse) -- NULL if this verse isn't in a passage yet. Synced by verse_meta_on_passage_change. | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| is_passage_anchor | INTEGER |  |  |  |  | via the same verse_passage junction, same trigger as passage_id | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| lexical_complete_at | TEXT |  |  |  |  | NOT populated as of #1608 -- home for CA-12 (`passage.lexical_complete_at`, orphaned by #1451's verse-scoped redesign). Giving it a verse-level home is #1608's job; the completeness-CHECK logic that would populate it is separate, future work. | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC, set once at row creation | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| updated_at | TEXT |  |  |  |  | ISO-8601 UTC, set by any of the 3 refresh triggers (deleted/language/passage_id change) -- NULL means never refreshed since creation | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| deleted | INTEGER |  | ✓ |  |  | soft delete, kept in sync with verse.deleted via verse_meta_on_verse_deleted | 1608-verse-meta-table (escalation #1608, spawned from #1607/D13) |
| status | TEXT |  |  |  |  | Researcher-set verse status, one of cfg_enum verse_meta_status (exclude/citated/analysed). NULL = not yet set. Deliberately excludes 'anchor' -- that's already verse_meta.is_passage_anchor, per the researcher's own instruction. Written only by VerseMeta.ps1 -Step SetStatus, never by application code. | 1661-verse-meta-status-column (escalation #1661) |
| status_changed_at | TEXT |  |  |  |  | ISO-8601 UTC, set ONLY when `status` actually changes value (not touched on every write) -- the researcher's own 'stamped if the status change' requirement. NULL means status has never been set. | 1661-verse-meta-status-column (escalation #1661) |

### cluster_subgroup_strong
_one row per strong-to-subgroup placement (membership)_ — The cluster-reading pack's own subgroup-membership table (#1690, was mti_term_subgroup, renamed 2026-09-13, design-complete). UNIQUE(strong) enforces one strong, one family, structurally.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK, assigned by the recording pass (#1693) |  |
| strong | TEXT |  | ✓ | ✓ | strong.strongNumber | the Strong's code, resolved to strong.strongNumber (was mti_term_id/mti_terms.id pre-DB-fork). UNIQUE -- one strong, one family, structurally enforced |  |
| cluster_subgroup_id | INTEGER |  | ✓ |  | cluster_subgroup.id | which subgroup this strong belongs to |  |
| placement_note | TEXT |  |  |  |  | free text -- REQUIRED for FLAG placements (the signpost's rationale); optional but available for any ordinary placement, captures whatever observation the LLM made while assigning that strong |  |
| delete_flagged | INTEGER |  | ✓ |  |  | soft-delete |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| last_updated_date | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |

### ib_node
_one row per grounding element an ib_observation cites (strong/verse/subgroup/cluster/question/another observation)_ — The cluster-reading pack's own grounding table (#1692, design-complete 2026-09-14). Makes 'no way to check a finding's grounding' structurally impossible via the CHECK constraint + the mandatory coverage self-check (#1692 SS2: every strong/verse in a subgroup's membership must be grounded by >=1 ib_node row, checked at LLM generation time and independently re-checked by the recording pass at load time).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK, assigned by the recording pass |  |
| observation_id | INTEGER |  | ✓ |  | ib_observation.id | which observation this grounding element belongs to |  |
| cluster_code | TEXT |  | ✓ |  |  | a VALUE, not necessarily a copy of the parent observation's own cluster -- THE cluster this row references. One row per cluster when an observation touches multiple clusters. |  |
| cluster_subgroup_code | TEXT |  |  |  |  | was family_key -- THE subgroup this row references (usually the observation's own, but can differ) |  |
| strong | TEXT |  |  |  |  | denormalized copy |  |
| verse_reference | TEXT |  |  |  |  | resolved FRESH against iba.db.verse.osisId at load time (recordingpass.py:resolve_occurrence returns v.osisId, never v.reference), never trusted from the LLM's JSON directly (#1693's own fix). CORRECTED 2026-09-22 (escalation #1824) -- this text previously said 'verse.reference', which was factually wrong (verse.reference is a different, space-separated STEP-abbreviated format, e.g. 'Mar 6:25', vs. osisId's dotted 'Mark.6.25'; confirmed live: 0 of 10,115 non-null ib_node.verse_reference values fail to join against verse.osisId) and is the likely cause of a real hand-written query bug this same session that joined against verse.reference expecting the dotted format. |  |
| surface | TEXT |  |  |  |  | was span_surface -- matches span.surface |  |
| morph_code | TEXT |  |  |  |  | was span_morph -- matches span.morph_code |  |
| question_code | TEXT |  |  |  |  | catalogue-question grounding -- not yet an enforced FK, restore once #1696 lands the catalogue into iba.db |  |
| traced_observation_id | INTEGER |  |  |  | ib_observation.id | set when grounded in ANOTHER observation instead of a verse |  |
| source_stage | TEXT |  | ✓ |  |  | reading \| answer \| synthesis |  |
| seq | INTEGER |  | ✓ |  |  | a plain per-observation ordinal -- ties together every ib_node row sharing one observation_id, in reading order when meaningful. UNIQUE(observation_id, seq) is the real natural key. |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |

### wa_obs_question_catalogue
_one row per catalogue question, the analytic-event question bank for the cluster-reading pipeline_ — Migrated from bible_research.db 2026-09-16 (#1696, #1706 Phase D item 19) -- 92 rows (98 source - 8 dropped per Phase 5 content review + 2 new T2.11 rows). ib_observation.question_code/ib_node.question_code both intend a real FK here once their tables' write paths are built (Phase F) -- not enforced yet, SQLite FKs are declare-at-create-time only.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| data_mechanism | TEXT |  |  |  |  | What data actually answers this question, checked live against the DB, not asserted: a role-cluster tag (cluster.cluster_code T2-T15), a specific table/cluster (e.g. M47), an existing reading-stage tag (e.g. surface-gloss-divergence), a per-cluster science-extract file (Workflow/Sciences/science_files/), or direct LLM reading of base verse/lexical text with no special tag needed. |  |
| dimension | TEXT |  |  |  |  | One of the 12 goal-derived dimensions (D1-D12, escalation #1712) this question serves, or M0 (lexical/textual evidence, feeds the 12 but is not itself one), X0 (cross-characteristic synthesis, synergy-stage), or a plus-joined list (e.g. D1+D2+D3+D4) for a deliberately consolidated question. Derived from the programme prose definition (Ch.1), independently cross-checked via a blind second derivation, 2026-09-17. |  |
| window |  |  |  |  |  | 11-window analytical-angle taxonomy tag for this catalogue question (e.g. relational, action-impact, origin, meaning, operational, constitutional, literary, faculty, cognitive, affective) -- applied catalogue-wide 2026-09-18. |  |
| obs_id | INTEGER | ✓ | ✓ |  |  | surrogate PK, fresh sequence (not copied from source) |  |
| question_code | TEXT |  | ✓ |  |  | e.g. T1.1.1 -- unique, the catalogue's own stable key |  |
| section | TEXT |  | ✓ |  |  | SUPERSEDED 2026-09-21, escalation #1818 -- redundant with `dimension` (#1712, 2026-09-17). Carries the OLD pre-realignment T0-T7 scheme label for 92 of 103 live rows; `dimension` already carries the live D1-D12/M0/X0/F0 classification for every row, confirmed clean. Checked live before deciding this: no stage-generator module (verse-reading/char-subgroup/char-reading/char-answers) ever reads `section` -- its only live reader is cataloguereport.py, which treats it purely as a documented data-quality finding ('two competing section-naming schemes'), not a working classification. Same verdict already applied in this table to `pattern_type`/`source_word`/`source_registry_no` -- kept for historical/audit value, not read as authoritative by any live code. Use `dimension` for the live classification instead. |  |
| source_word | TEXT |  |  |  |  | provenance -- DROPPED 2026-09-17, escalation #1712: confirmed relic (source_word was the constant Programme on all rows, source_registry_no was NULL on all rows). |  |
| source_registry_no | INTEGER |  |  |  |  | provenance -- DROPPED 2026-09-17, escalation #1712: confirmed relic (source_word was the constant Programme on all rows, source_registry_no was NULL on all rows). |  |
| question_text | TEXT |  | ✓ |  |  | the actual catalogue question text |  |
| pattern_type | TEXT |  |  |  |  | event-cross-reference column, ready-to-apply crosswalk per #1704 Phase 3 -- write now vs fold into this same migration was a sequencing question, resolved: folded in -- DROPPED 2026-09-17, escalation #1712: superseded by dimension/data_mechanism, which do the event-cross-reference job pattern_type never actually got filled in for (90/92 NULL). |  |
| scope | TEXT |  | ✓ |  |  | The stage-selection bucket a question answers at -- checked live against every stage-generator module's own selection query, 2026-09-21 (escalation #1806 coverage audit): 'Characteristic (HIB behaviour)'/'Characteristic relational'/'The HIB'/'Other non-human beings' select Stage 4 (char-answers); 'Word/term (lexical)'/'Verse-context'/'The verse' are NOT selected by any live stage's query at all (escalation #1806's own still-open ask -- 27 of 103 questions are structurally unreachable on this basis, tracked there, not a defect in this column itself). Registered as cfg_enum wa_obs_question_catalogue.scope, 2026-09-21. |  |
| status | TEXT |  | ✓ |  |  | Lifecycle state: 'active' (live, presented to a stage per its scope/mechanism) or 'retired' (superseded, `deleted` should also be 1 -- checked live 2026-09-21, escalation #1818: found and fixed 4 rows, the T7.3.x family, that had deleted=1 but status still 'active', the exact status/deleted-disagreement defect class this table's own migration history already flagged as a known risk). Registered as cfg_enum wa_obs_question_catalogue.status, 2026-09-21. |  |
| deleted | INTEGER |  | ✓ |  |  | soft-delete |  |
| date_added | TEXT |  | ✓ |  |  | ISO-8601 UTC, set at migration/insert time |  |
| catalogue_version | TEXT |  | ✓ |  |  | e.g. v2-2026-09-16 |  |
| review_note | TEXT |  |  |  |  | free text |  |
| tier | TEXT |  |  |  |  | The live analytical bucket a question belongs to, post-#1712 realignment (2026-09-17): M0 (word-level battery), D1-D12 (the 12 goal-derived dimensions), X0 (cross-characteristic synergy-stage synthesis), F0 (faculty engagement), or T7 (legacy, retired-only -- the 4 deleted T7.3.x rows, never migrated since they're superseded, not live). Registered as cfg_enum wa_obs_question_catalogue.tier, 2026-09-21. |  |
| component_code | TEXT |  |  |  |  | e.g. T2.11 |  |
| component_title | TEXT |  |  |  |  | e.g. Faculty Engagement |  |
| prompt_seq | INTEGER |  |  |  |  | Display-ordering only within (tier, component_code) -- confirmed live consumer: cataloguereport.py's own tiered listing (`ORDER BY tier, component_code, prompt_seq, obs_id`). NOT read by any of the 4 live LLM-calling stages (verse-reading/char-subgroup/char-reading/char-answers select question_code/question_text/scope only, never prompt_seq) -- it has zero effect on which questions get asked or in what order the LLM actually sees them within a stage's own prompt; it only affects this one human-facing report's display order. NULL sorts first in SQLite ASC order, so a NULL row displays out of its intended sequence, not absent -- checked and fixed for all 9 rows that had it (2026-09-21, escalation #1818). |  |
| source | TEXT |  |  |  |  | descriptive provenance, not an invented code |  |
| last_modified | TEXT |  |  |  |  | ISO-8601 UTC |  |

### cluster_subgroup
__ — Cluster-reading subgroup: a curated group of Strong-numbered codes within one cluster (M-code), the unit of per-subgroup reading/answering in the cluster-reading pipeline (Stage 3, cluster.subgroup step). Built 2026-09 for the synergy-build pipeline; a differently-shaped legacy table of the same name predates it in bible_research.db (M-code cluster model) -- same name, different table, different database.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK, assigned by the recording pass (#1693) |  |
| cluster_code | TEXT |  | ✓ |  | cluster.cluster_code | required, singular -- a family is structurally one-cluster-only by construction |  |
| subgroup_code | TEXT |  | ✓ |  |  | the family's stable code, unique per (cluster_code, subgroup_code) -- expected to repeat as 'FLAG' across clusters, never otherwise |  |
| label | TEXT |  | ✓ |  |  | short human title |  |
| core_description | TEXT |  |  |  |  | one sentence on the family's shared commonality |  |
| anchor_verse_reference | TEXT |  |  |  |  | ADDED 2026-09-16 (#1526). One representative verse per subgroup, selected by process (b)'s own LLM session as the verse that best describes the subgroup's shared characteristic (researcher, verbatim). Resolved fresh against iba.db.verse.osisId (CORRECTED 2026-09-22, escalation #1824 -- previously said verse.reference, the same wrong claim ib_node.verse_reference carried, inherited via this text's own 'same convention as' reference; confirmed live: 0 of 13 non-null values fail to join against verse.osisId), same convention as ib_node.verse_reference; written in the SAME DB update as the rest of the subgroup row (#1693's recording pass), never a separate pass or left null-then-backfilled. |  |
| sort_order | INTEGER |  |  |  |  | display order |  |
| status | TEXT |  |  |  |  | subgroup-level lifecycle, cfg_enum-governed (cluster_subgroup.status, #1690 SS3a). Distinct from cluster.status (#1697) -- coarser grain, separate enum. NULL for the FLAG subgroup (never enters this lifecycle). |  |
| version | TEXT |  |  |  |  | reused as-is from the legacy table convention |  |
| source | TEXT |  |  |  |  | descriptive provenance text, not an invented code |  |
| notes | TEXT |  |  |  |  | free text |  |
| delete_flagged | INTEGER |  |  |  |  | soft-delete |  |
| created_at | TEXT |  |  |  |  | ISO-8601 UTC |  |
| last_updated_date | TEXT |  |  |  |  | ISO-8601 UTC |  |

### ib_observation
__ — Cluster-reading pipeline observation: one typed finding produced while reading/answering a cluster_subgroup (stage, tag, question_code, obs_text, meaning_source), the unit ib_node traces back to. Built 2026-09 for the synergy-build pipeline; a differently-shaped legacy table of the same name predates it in bible_research.db -- same name, different table, different database.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| meaning_keywords | TEXT |  |  |  |  | JSON array of short key terms/concepts the LLM extracts alongside obs_text, used by recordingpass.py's structured-key same/broaden/new matching (surface+morph+keywords) -- escalation #1824, 2026-09-21. NULL for stages/questions not yet using this path (everything except the new M0.7 family so far); the existing text-similarity path remains the fallback wherever this is NULL. | escalation #1824, researcher instruction 2026-09-21 |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK, assigned by the recording pass, never the LLM session |  |
| cluster_code | TEXT |  |  |  | cluster.cluster_code | NULL for stage=synthesis (cross-cluster; the actual cluster(s) are recorded via ib_node rows instead) AND for word-level (M0.1.x/M0.5.x) questions in stage=verse-reading (2026-09-23: cluster has no role in these -- the observation is a fact about the strong+span alone, keyed on strong and verse, never a cluster). Required for every other stage/question type. |  |
| cluster_subgroup_id | INTEGER |  |  |  | cluster_subgroup.id | NULL for stage=synthesis and process (b)'s own cluster-level observations (both above single-subgroup scope) |  |
| stage | TEXT |  | ✓ |  |  | cfg_enum-governed (ib_observation.stage): verse-reading (pre-subgroup Layer 2, #1711) \| char-subgroup (subgroup/family formation, process b) \| char-reading (process c) \| char-answers (process d) \| char-synergy (process e, cross-cluster). Renamed 2026-09-17, escalation #1706, completing the naming scheme -- every value now names an activity at a grain (verse vs. characteristic), subgroup formation included. |  |
| tag | TEXT |  | ✓ |  |  | enum, cfg_enum-governed (ib_observation.tag) -- shared across all stages, not partitioned per stage; most tags apply wherever the relevant condition arises (e.g. data-error, cross-cluster-significance, could-not-resolve are not reading-exclusive). Corrected 2026-09-17, escalation #1706: previously read 'stage-specific enum', which the researcher identified as the wrong model -- ib_observation is one unified record set populated across stages, not fragmented enum groups per stage. |  |
| strong | TEXT |  |  |  |  | the strong this claim is grounded in |  |
| question_code | TEXT |  |  |  |  | answer/verse_meaning stages -- not yet an enforced FK; restore once the catalogue migration (#1696) lands wa_obs_question_catalogue into iba.db |  |
| window | TEXT |  |  |  |  | The analytical angle this row looks through -- meaning / action-impact / relational (cfg_enum ib_observation.window). Populated FROM wa_obs_question_catalogue.window at write time (recordingpass.py), never invented ad hoc. Redefined #1723, 2026-09-17 -- was a 4-value pipeline-stage enum (#1691) that duplicated `stage`. |  |
| obs_text | TEXT |  | ✓ |  |  | self-standing claim text, no join required |  |
| meaning_source | TEXT |  |  |  |  | which of the 3 meaning tables/columns (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) an observation drew its data from -- any meaning-reading stage (verse_meaning and reading both read all 3 as complementary evidence), not reading-only. Corrected 2026-09-17, escalation #1706: previously read 'reading stage only', the same stage-scoping mistake corrected for `tag`. |  |
| status | TEXT |  |  |  |  | Where the observation stands (6-value lifecycle, researcher-defined 2026-09-20, escalation #1782): draft (just written or edited by the pipeline, not yet looked at by the observation_enhancer or a human -- the write-time default as of this round) \| needs-corroboration (observation detail is incomplete or needs revision) \| open (not yet confirmed -- NOTE: no current writer sets this since draft was introduced; kept live pending the researchers call on whether to retire it) \| silent (captured but not included in any subsequent analysis) \| withdrawn (observation is incorrect or not useful) \| resolved (set only once the observation is cleared for inclusion in analysis). |  |
| supersedes_observation_id | INTEGER |  |  |  | ib_observation.id | synthesis stage only, self-referencing, the append-only supersedes chain |  |
| stable_key | TEXT |  |  |  |  | the generating JSON file's own name; for a strand-reading observation imported from a ledger (#2172 catch-up), '<strand>:<ledger ID>' |  |
| revisit_note | TEXT |  |  |  |  | synthesis stage; for a strand-reading observation, its disposition note (#2172): the October disposition and the row's touches until step C sets the status, then the claim, item or reason |  |
| source_json_serial | INTEGER |  |  |  |  | the LLM session's own local numbering within its JSON, distinct from id |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| updated_at | TEXT |  |  |  |  | set whenever obs_text is broadened in place |  |
| setting | TEXT |  |  |  |  | the key statement's setting: who speaks, the verses around it, the genre (October ledger part) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| meaning | TEXT |  |  |  |  | what the statement means in its setting (October ledger part) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| implication | TEXT |  |  |  |  | what it implies for the inner being (October ledger part) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| chain | TEXT |  |  |  |  | the link the verse itself states to another act or state; NULL where the verse states none | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| basis | TEXT |  |  |  |  | cfg_enum ib_observation.basis: stated (the verse states it) or read (Claude's reading, 'I read') | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| parties | TEXT |  |  |  |  | who acts, toward whom, and who else is named | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| run_id | TEXT |  |  |  |  | the Strand-Reading run that wrote or last changed the row | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |

### run_batch
_one row per batch/chunk attempt of a live multi-batch (or single-call) run_ — The batch/step-level control table (escalation #1756, researcher-approved design 2026-09-18) -- resume/skip (a new run_id skips any batch a PRIOR run_id already committed, via UNIQUE(step, selector_key, batch_content_key)), crash safeguard (a 'running' row with no terminal update proves a dead run), and live progress monitoring (BatchProgress.ps1) for every long-running LLM-calling step. lib/batchcontrol.py is the sole writer. Prompted directly by M49's Stage 1 verse-reading run needing two full from-scratch restarts this session with no way to skip already-paid-for batches.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| run_id | TEXT |  | ✓ |  |  | the run.run_id that attempted this batch (informational/audit -- NOT part of the resume/skip key, deliberately, so a later run_id can still see an earlier run_id's committed work) |  |
| work_package | TEXT |  | ✓ |  |  | e.g. verse-lexical, cluster-reading |  |
| step | TEXT |  | ✓ |  |  | e.g. lexical.meaning, cluster.subgroup -- part of the resume/skip key |  |
| selector_key | TEXT |  | ✓ |  |  | what this run was scoped to -- cluster_code alone, or cluster_code\|subgroup_code for a subgroup-scoped step. Part of the resume/skip key. |  |
| batch_ordinal | INTEGER |  | ✓ |  |  | this batch's 1-based position within its own run -- display/ordering only, NOT part of the resume/skip key (batch_content_key is, since ordinal position can drift between runs if the selector's own item list changes) |  |
| batch_content_key | TEXT |  | ✓ |  |  | stable hash (batchcontrol.content_key) of the batch's own actual item list (verse ids, or member strongs) -- content-keyed, not position-keyed, so resume is correct even if the underlying item list shifts between runs. Indexed together with step/selector_key for lookup performance, but NOT unique -- the resume/skip guarantee lives in batchcontrol.already_committed()'s own WHERE status='committed' check, consulted before start_batch() runs, not in a schema constraint (a UNIQUE constraint here was tried first and found live, #1758, to incorrectly block a legitimate retry after a failed attempt at the same content). |  |
| status | TEXT |  | ✓ |  |  | cfg_enum-governed (run_batch.status): running (written before the API call) \| committed (written after record_batch's own commit succeeds) \| failed (written in an exception handler before re-raising -- the crash safeguard). A 'running' row with no later committed/failed row for the same id is live proof of a dead run. |  |
| started_at | TEXT |  | ✓ |  |  | ISO-8601 UTC, set when status='running' is written |  |
| ended_at | TEXT |  |  |  |  | ISO-8601 UTC, set when status becomes committed/failed |  |
| error_message | TEXT |  |  |  |  | set only when status='failed' |  |
| cost_usd | REAL |  |  |  |  | set only when status='committed', the real spent cost |  |

### cfg_observation_enhancer_rule
_one row per researcher-authored rule_ — Rule storage for the observation_enhancer utility (escalation #1778) -- pairs a selector_sql (SELECT returning ib_observation.id) with an update_json (column->value) applied via direct UPDATE. Added/edited via configmaint.propose like any other cfg_* row -- NOT a bespoke add/confirm mechanism. status is the researcher's own per-rule confirmation gate (draft -> confirmed, after reviewing a real -Action Preview run -> active, set automatically on first successful apply -> retired).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| rule_key | TEXT |  | ✓ | ✓ |  | stable human-chosen identifier, e.g. '1769-placeholder-filler' -- what -Action Preview/-Action Apply take as -RuleKey |  |
| description | TEXT |  | ✓ |  |  | what the rule does and why, for a future reader -- not re-derivable from the SQL alone |  |
| selector_sql | TEXT |  | ✓ |  |  | a single SELECT (no ';', no INSERT/UPDATE/DELETE/DROP/ATTACH/PRAGMA/ALTER) against ib_observation returning an 'id' column -- checked live by handlers/observationenhancer.py before every run, not just at authoring time |  |
| update_json | TEXT |  | ✓ |  |  | JSON object of ib_observation column -> new value, applied via UPDATE to every row selector_sql matches. Column names checked against ib_observation's real columns live; the primary key column cannot be targeted. |  |
| status | TEXT |  | ✓ |  |  | cfg_enum-governed (cfg_observation_enhancer_rule.status): draft (authored, not yet reviewed against real data) \| confirmed (researcher has run -Action Preview and approved -- -Action Apply now permitted) \| active (has been applied at least once) \| retired (no longer applied). -Action Apply refuses any rule not confirmed/active. |  |
| confirmed_at | TEXT |  |  |  |  | ISO-8601 UTC, set when status first becomes confirmed |  |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC, set at insert (configmaint.propose) |  |
| ordinal | INTEGER |  | ✓ |  |  | display/authoring order only |  |
| active | INTEGER |  | ✓ |  |  | soft-delete flag distinct from status='retired' -- 0 hides a rule entirely (e.g. authored in error), matching this app's standard active convention |  |

### ib_observation_enhancer_log
_one row per (observation, field) actually changed by a rule application_ — Audit trail for the observation_enhancer utility (escalation #1778) -- answers 'which rule touched this row, and what did it change' months later, the same kind of traceability ib_node's own traced_observation_id/source_stage already gives the write-time pipeline. Written only by handlers/observationenhancer.py:apply.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK |  |
| rule_id | INTEGER |  | ✓ |  | cfg_observation_enhancer_rule.id | which rule made this change |  |
| rule_key | TEXT |  | ✓ |  |  | denormalised copy of the rule's own key at apply time -- readable even if the rule row is later retired/edited |  |
| observation_id | INTEGER |  | ✓ |  | ib_observation.id | which observation was changed |  |
| field_changed | TEXT |  | ✓ |  |  | the ib_observation column that was updated |  |
| before_value | TEXT |  |  |  |  | the field's value immediately before this change (stringified) |  |
| after_value | TEXT |  | ✓ |  |  | the value written (stringified) |  |
| applied_at | TEXT |  | ✓ |  |  | ISO-8601 UTC |  |
| run_id | TEXT |  |  |  |  | the run.run_id of the -Action Apply call that made this change |  |

### escalation_thread_item
_one row per thread item_ — One row per item of a thread (type='thread' escalation): what a strand or task is matched against, and the item's current status only: open, or settled as closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread). Every response, including each settlement, is a row in escalation_thread_item_response. escalation #2000 (proposal v3 sec3.2, sec3.4; thread lifecycle, BUILD.md s338).
dedup key: `escalation_id, item_no`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| escalation_id | INTEGER |  | ✓ |  | escalation.id | the thread | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| item_no | INTEGER |  | ✓ |  |  | the item's place in its thread; the reference is {alias}.{item_no}, e.g. OT-16.1. Never renumbered; a new item takes the next number (proposal sec3.4) | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| kind | TEXT |  | ✓ |  |  | cfg_enum escalation_thread_item_kind: cluster, strong, verse, strand, chapter, event, researcher, escalation | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| value | TEXT |  | ✓ |  |  | e.g. M72, M10c, H5782, Rom 7:15-21, 10.13, #1993 (kind escalation: the task or issue that references the thread) | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| status | TEXT |  | ✓ |  |  | cfg_enum escalation_thread_item_status: open, closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread) -- current state only; every change is a response row | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| note | TEXT |  |  |  |  | what this item asks for, e.g. '7 verses' | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| opened_at | TEXT |  | ✓ |  |  | when the item was added (ISO-8601 UTC) | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| opened_by | INTEGER |  |  |  | escalation.id | the escalation under which the item was added: a task or issue (e.g. a forward under #1998), or the superseded thread an item was carried over from; NULL when added with the thread itself | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |

### escalation_thread_item_response
_one row per response to a thread item_ — One row per response to a thread item: touched, narrowed, forward, ruling, note, closed, reopened, withdrawn, superseded. Nothing is overwritten; each response is also written in full to the thread's history. escalation #2000 (proposal v3 sec3.3, approved round 5; thread lifecycle, BUILD.md s338).
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| item_id | INTEGER |  | ✓ |  | escalation_thread_item.id | the item answered | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| escalation_id | INTEGER |  | ✓ |  | escalation.id | the thread (repeated from the item, for easy querying) | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| kind | TEXT |  | ✓ |  |  | cfg_enum escalation_thread_item_response_kind. 'closed', 'withdrawn' and 'superseded' settle an open item (status = kind; 'superseded' names its successor OT-nn[.n] or #nnnn in the text), 'reopened' opens a settled item again, 'forward' comes with at least one new item on the same thread | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| text | TEXT |  | ✓ |  |  | the response; a researcher's response is quoted verbatim (cfg_escalation 5) | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| via_escalation | INTEGER |  |  |  | escalation.id | the escalation whose work gave the response, e.g. 1998; for a task's own ending, that task; for an item carried over on supersede, the other thread | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| responded_by | TEXT |  | ✓ |  |  | Claude or Researcher | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| responded_at | TEXT |  | ✓ |  |  | ISO-8601 UTC | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |
| files | TEXT |  |  |  |  | JSON list of full repo-relative paths (cfg_escalation 7) | escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md) |

### cfg_trigger
_one row per trigger_ — Every SQLite trigger in either database, with its full CREATE TRIGGER statement. A trigger is schema exactly like a column or an index: lib/db.py:trigger_ddl() rebuilds it from here, and cfgquality.find_unregistered_triggers (configmaint.validate) checks the live databases against it. escalation #2110, 2026-10-13
dedup key: `database, name`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| database | TEXT |  | ✓ |  |  | iba or bible_research | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| table_name | TEXT |  | ✓ |  |  | the table the trigger is on | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| name | TEXT |  | ✓ |  |  | the trigger name (unique per database) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ordinal | INTEGER |  | ✓ |  |  | creation order within a table | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| sql | TEXT |  | ✓ |  |  | the full CREATE TRIGGER statement | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| use | TEXT |  |  |  |  | what the trigger does and why | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| inactive | INTEGER |  | ✓ |  |  | 1 for a retired trigger | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_chapter
_one row per chapter or sub-chapter_ — One row per chapter or sub-chapter of the inner-being narrative, and the authority for which chapters exist, their reading order and what each is for (kind, purpose, purpose_ref). Changed only through Narrative-Register.ps1 (AddChapter, EditChapter); every structural change is logged in the Structure log. A renumbering changes chapter_no on the row; every record keeps its link to the chapter, so the history follows the chapter, not the number. The copy to learning4comfort publishes the active chapters' current files. escalation #2110 spec sec3.1; #2155
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_no | TEXT |  | ✓ |  |  | 02, 10.7, 13.1 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| title | TEXT |  | ✓ |  |  | the chapter heading, e.g. Choosing and setting direction | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| reading_order | INTEGER |  | ✓ |  |  | order in the book | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| file_stem | TEXT |  | ✓ |  |  | e.g. 10-07-choosing-and-setting-direction | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| current_version | INTEGER |  |  |  |  | the current chapter file's version, e.g. 27 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| current_file | TEXT |  |  |  |  | the current chapter file name | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| state | TEXT |  | ✓ |  |  | cfg_enum narrative_chapter_state | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| replaces_original | TEXT |  |  |  |  | the index column 'Replaces or absorbs (original)' | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| built_from | TEXT |  |  |  |  | the index column 'Built from' | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| inactive | INTEGER |  | ✓ |  |  | 1 for a retired chapter number (old Ch 13 Under God's anger) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| kind | TEXT |  |  |  |  | cfg_enum narrative_chapter_kind: what sort of chapter this is (front matter, activity, key characteristic, ...) | escalation #2155, proposal v1 (wa-essay-narrative-chapter-table-proposal-v1-20261018.md) |
| purpose | TEXT |  |  |  |  | what the chapter holds, what belongs in it and what goes elsewhere, in plain words | escalation #2155, proposal v1 (wa-essay-narrative-chapter-table-proposal-v1-20261018.md) |
| purpose_ref | TEXT |  |  |  |  | the rulings that set the purpose: escalation numbers and dates | escalation #2155, proposal v1 (wa-essay-narrative-chapter-table-proposal-v1-20261018.md) |

### narrative_section
_one row per section heading in a chapter_ — One row per section heading in a chapter, current or past. A chapter's opening, before any heading, has its own row (level 0). escalation #2110, spec sec3.2
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_id | INTEGER |  | ✓ |  | narrative_chapter.id | the chapter | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| heading | TEXT |  | ✓ |  |  | the heading text as written; '(opening)' for the opening | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| level | INTEGER |  | ✓ |  |  | heading level 2-4; 0 for the opening | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| parent_section_id | INTEGER |  |  |  | narrative_section.id | the section it sits in | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ordinal | INTEGER |  | ✓ |  |  | order in the chapter | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| first_version | INTEGER |  |  |  |  | the first chapter version that has the heading | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| last_version | INTEGER |  |  |  |  | the last chapter version that has it; NULL while current | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| renamed_from_id | INTEGER |  |  |  | narrative_section.id | when a heading is renamed, the old row | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| block_text | TEXT |  |  |  |  | the section's block of the chapter, verbatim: its heading line and every line up to the next heading (the opening row: the title line and the opening). The chapters render from these blocks in ordinal order (narrativeregister.render_chapter); NULL on a row that is no longer current | escalation #2172, reading process design v2 (option B) |

### narrative_claim
_one row per claim_ — The register: one row per claim. A claim is a statement derived from sources (verses, later science) that goes beyond their mere text, held in its own plain wording. A quotation is not a claim. escalation #2110, spec sec3.3 (researcher, round 3)
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_ref | TEXT |  |  | ✓ |  | original claims keep the register's id (I-1, 2-5, K-2); new claims are C-{id}, set by trigger trg_narrative_claim_ref_ai when left empty | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| origin | TEXT |  | ✓ |  |  | cfg_enum narrative_claim_origin | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_text | TEXT |  | ✓ |  |  | the claim in its own plain wording, apart from how the narrative tells it | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| beyond_text | TEXT |  |  |  |  | what the claim adds to its sources: why it is a claim and not a quotation | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| i_read | INTEGER |  | ✓ |  |  | 1 when the narrative marks it as the narrator's reading ('I read') | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| verdict | TEXT |  |  |  |  | cfg_enum narrative_claim_verdict, the register's own words | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| part_verdict | TEXT |  |  |  |  | the second verdict of a split verdict, e.g. Held in 9-1 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| part_scope | TEXT |  |  |  |  | what each part of a split verdict covers | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| original_chapter | TEXT |  |  |  |  | for original claims: the essay chapter heading | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| original_wording | TEXT |  |  |  |  | for original claims: the claim as the essay made it | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| main_chapter_id | INTEGER |  |  |  | narrative_chapter.id | the chapter that tells the claim most fully | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| main_section_id | INTEGER |  |  |  | narrative_section.id | the section that tells it most fully | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| in_narrative | INTEGER |  | ✓ |  |  | 1 if at least one current passage tells the claim (a pointer does not count); 0 if none. The filter for claims not included | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| status | TEXT |  | ✓ |  |  | cfg_enum narrative_claim_status | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_claim_source
_one row per source of a claim_ — What a claim rests on: a verse (one row per verse; ranges and lists expanded), a lexical source, science (later), or a study file. escalation #2110, spec sec3.4
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_id | INTEGER |  | ✓ |  | narrative_claim.id | the claim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| source_kind | TEXT |  | ✓ |  |  | cfg_enum narrative_claim_source_kind | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| verse_id | INTEGER |  |  |  | verse.id | for kind verse; NULL where the verse has no row | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ref_as_written | TEXT |  |  |  |  | the reference as written, e.g. 1 Samuel 24:5 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ref_normalised | TEXT |  |  |  |  | in verse.reference form, e.g. 1Sa 24:5 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| source_text | TEXT |  |  |  |  | for the other kinds: the word with its gloss, the science reference, or the file path | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| note | TEXT |  |  |  |  | how the source bears on the claim, where it is not plain | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| observation_id | INTEGER |  |  |  | ib_observation.id | the observation the claim rests on, when source_kind is 'observation' (#2172 design decision 4) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |

### narrative_passage
_one row per passage that tells at least one claim_ — History since #2172: the paragraphs that told claims before the narrative was held as blocks (narrative_section.block_text). No longer written; a claim is told by a block (narrative_claim_telling.section_id). escalation #2110, spec sec3.2
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_id | INTEGER |  | ✓ |  | narrative_chapter.id | the chapter | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| section_id | INTEGER |  |  |  | narrative_section.id | the section | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ordinal | INTEGER |  | ✓ |  |  | its place in the section | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| anchor_text | TEXT |  | ✓ |  |  | its opening words, so the tool can find it in the file | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| passage_text | TEXT |  | ✓ |  |  | the passage as it now reads | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| first_version | INTEGER |  |  |  |  | the first chapter version that holds it | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| last_version | INTEGER |  |  |  |  | the last chapter version that holds it; NULL while current | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_claim_telling
_one row per claim told in a block (passage rows before #2172 are history)_ — The link between a claim and the block (narrative_section) that tells it, many to many. escalation #2110, spec sec3.5; per block since #2172
dedup key: `claim_id, section_id, passage_id`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_id | INTEGER |  | ✓ |  | narrative_claim.id | the claim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| section_id | INTEGER |  | ✓ |  | narrative_section.id | the block (narrative_section) that tells the claim; one current telling per claim and block (#2172) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| passage_id | INTEGER |  |  |  | narrative_passage.id | the passage that told the claim before #2172 (history, status superseded); NULL on a block telling | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| kind | TEXT |  | ✓ |  |  | cfg_enum narrative_telling_kind: in full, in part, pointer | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| part_told | TEXT |  |  |  |  | which part of the claim this passage tells | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| status | TEXT |  | ✓ |  |  | cfg_enum narrative_telling_status: current, removed, superseded (a passage telling carried by its block's telling, #2172) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_update
_one row per weave or recorded pass_ — One row per weave or recorded pass on the narrative, with its instruction, sources, notes and quote check. Imported updates keep the register version that added them. escalation #2110, spec sec3.6
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| update_date | TEXT |  | ✓ |  |  | ISO date of the update | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| title | TEXT |  | ✓ |  |  | the update's heading | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| strand | TEXT |  |  |  |  | e.g. anger (M02) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| researcher_instruction | TEXT |  |  |  |  | verbatim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| method | TEXT |  |  |  |  | method or rule named (e.g. rule 73) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| source_files | TEXT |  |  |  |  | one path per line | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| scripts | TEXT |  |  |  |  | one path per line | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claims_changed_note | TEXT |  |  |  |  | 'Original claims changed', verbatim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| not_woven_note | TEXT |  |  |  |  | 'Not woven' / 'Kept out', verbatim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| structure_change | TEXT |  |  |  |  | filled when the book's shape changed (the Structure log) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| structure_reason | TEXT |  |  |  |  | the reason for the structure change | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| quote_parts | INTEGER |  |  |  |  | the quote check: parts checked | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| quote_failures | INTEGER |  |  |  |  | the quote check: failures | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| quote_note | TEXT |  |  |  |  | the quote check note, verbatim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| notes | TEXT |  |  |  |  | any other paragraph, verbatim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| legacy_register_version | INTEGER |  |  |  |  | for imported updates, the register version that added it | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_update_ref
_one row per escalation or thread an update names_ — The escalations, threads and thread items an update names. escalation #2110, spec sec3.6
dedup key: `update_id, kind, value`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| update_id | INTEGER |  | ✓ |  | narrative_update.id | the update | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| kind | TEXT |  | ✓ |  |  | cfg_enum narrative_update_ref_kind | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| value | TEXT |  | ✓ |  |  | 1998, OT-29, OT-29.1 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_claim_change
_one row per change to a claim or to a passage that tells it_ — The change log, many rows per claim: every change to a claim, and to each passage that tells it, with enough before and after to review the impact without opening another file (Q-F). A change to one passage that tells three claims writes three rows. escalation #2110, spec sec3.7
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_id | INTEGER |  | ✓ |  | narrative_claim.id | the claim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| passage_id | INTEGER |  |  |  | narrative_passage.id | the passage, for a change in how the claim is told | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| update_id | INTEGER |  |  |  | narrative_update.id | the update that made it; NULL for a direct edit | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| change_date | TEXT |  | ✓ |  |  | ISO date | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| change_kind | TEXT |  | ✓ |  |  | cfg_enum narrative_claim_change_kind | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_before | TEXT |  |  |  |  | the claim's wording before | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| claim_after | TEXT |  |  |  |  | the claim's wording after | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| verdict_before | TEXT |  |  |  |  | the verdict before | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| verdict_after | TEXT |  |  |  |  | the verdict after | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| passage_before | TEXT |  |  |  |  | the full passage before, as it read in the chapter | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| passage_after | TEXT |  |  |  |  | the full passage after | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_id | INTEGER |  |  |  | narrative_chapter.id | where | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| section_id | INTEGER |  |  |  | narrative_section.id | where | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| section_before_id | INTEGER |  |  |  | narrative_section.id | where from, for a move | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_version_from | INTEGER |  |  |  |  | e.g. 7 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_version_to | INTEGER |  |  |  |  | e.g. 8 | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| file_before | TEXT |  |  |  |  | the chapter file before | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| file_after | TEXT |  |  |  |  | the chapter file after | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| note | TEXT |  |  |  |  | the verdict cell verbatim, or any remark | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| basis | TEXT |  | ✓ |  |  | cfg_enum narrative_change_basis: recorded, reconstructed, direct edit | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| provenance | TEXT |  |  |  |  | the file(s) the row came from, or the trigger that wrote it | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_citation
_one row per verse cited in a passage of the story_ — The citation index: every verse cited anywhere in the story, by passage. With narrative_claim_source it answers, for any verse, where it is cited and which claims rest on it. A reference that cannot be resolved is kept with verse_id NULL, never dropped. escalation #2110, spec sec3.8
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| chapter_id | INTEGER |  | ✓ |  | narrative_chapter.id | where it is cited | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| section_id | INTEGER |  |  |  | narrative_section.id | where it is cited | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| passage_id | INTEGER |  |  |  | narrative_passage.id | NULL if the passage tells no claim | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| verse_id | INTEGER |  |  |  | verse.id | NULL where the verse has no row | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ref_as_written | TEXT |  | ✓ |  |  | as written in the chapter | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ref_normalised | TEXT |  |  |  |  | in verse.reference form | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| quoted | INTEGER |  | ✓ |  |  | 1 when the verse's words are quoted, 0 when it is only referred to | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| first_version | INTEGER |  |  |  |  | the first chapter version that cites it | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| last_version | INTEGER |  |  |  |  | the last chapter version that cites it; NULL while current | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### narrative_index_note
_one row per block of index text_ — The parts of the old narrative index that are text, not tables (researcher direction, theme and frame, rules applied, how later work updates the narrative, source files, verse check), one row per block, editable. escalation #2110, spec sec3.9
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| heading | TEXT |  | ✓ |  |  | the block heading | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| text | TEXT |  | ✓ |  |  | the block text (markdown) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| ordinal | INTEGER |  | ✓ |  |  | order in the published register | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md) |

### cfg_control_home
_one row per kind of control content_ — The control map: for each kind of control content, its ONE home, when that home is read, and where replaced versions go so they are not read routinely. Escalation #2180.
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kind | TEXT | ✓ | ✓ |  |  | the kind of control content (e.g. behaviour_rule, tool_usage) -- one row each | migration/control_map_v1_20261021.py |
| description | TEXT |  | ✓ |  |  | what content of this kind is, and what its home holds and does not hold | migration/control_map_v1_20261021.py |
| home_type | TEXT |  | ✓ |  |  | cfg_enum control_home_type: cfg_table, db_table, document, folder or harness | migration/control_map_v1_20261021.py |
| home | TEXT |  | ✓ |  |  | the ONE place content of this kind lives; every other place names it, never restates it | migration/control_map_v1_20261021.py |
| read_when | TEXT |  | ✓ |  |  | cfg_enum control_read_when: when the home is read (always, session_start, when_invoked, when_needed, history_only) | migration/control_map_v1_20261021.py |
| history_home | TEXT |  | ✓ |  |  | where a replaced or changed version of this content goes: out of the routine read path, kept for deliberate reading of a past state | migration/control_map_v1_20261021.py |
| source | TEXT |  | ✓ |  |  | the ruling or escalation the row comes from | migration/control_map_v1_20261021.py |
| added_at | TEXT |  | ✓ |  |  | when the row was added (ISO-8601 UTC) | migration/control_map_v1_20261021.py |
| inactive | INTEGER |  | ✓ |  |  | 0=active, 1=retired (kept as history) | migration/control_map_v1_20261021.py |

### cfg_rule_scope
_one row per link between a rule and an operation it governs_ — #2209: which operations each rule governs, so the rules of an operation are put in front of Claude when it is used (.claude/hooks/rules_at_point_of_use.py) and configmaint.validate can check every rule and every operation is linked
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate key | migration/archive/rule_scope_2209_v1_20261021.py |
| rule_ref | TEXT |  | ✓ |  |  | the rule: B:<cfg_behaviour_rule.id>, E:<cfg_escalation.id> or G:<cfg_setting.key of a governance rule> | migration/archive/rule_scope_2209_v1_20261021.py |
| scope_kind | TEXT |  | ✓ |  |  | what kind of operation the rule governs: general (all work, delivered at start), ps (a PS tool), command (git, migration, sqlite), path (a file written) | migration/archive/rule_scope_2209_v1_20261021.py |
| scope_value | TEXT |  | ✓ |  |  | the operation: a PS script name with an optional -Action/-Step (Escalation.ps1 -Action Update), a command family (git, migration, sqlite), a repo-relative path glob (iba/app/**, **), or * for general | migration/archive/rule_scope_2209_v1_20261021.py |
| inactive | INTEGER |  | ✓ |  |  | 1 = link no longer in force | migration/archive/rule_scope_2209_v1_20261021.py |

### reading_strand
_one row per strand_ — #2172: a strand read through the reading process (Strand-Reading.ps1): its word family (reading_strand_strong), its hits (reading_strand_hit) and the escalation that is its record
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| code | TEXT |  | ✓ |  |  | the strand's short name, lowercase-hyphenated (e.g. flesh-body) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| title | TEXT |  | ✓ |  |  | the strand in words | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| cluster_code | TEXT |  | ✓ |  | cluster.cluster_code | the strand's home cluster (its ib_node rows carry it) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| escalation_id | INTEGER |  | ✓ |  | escalation.id | the escalation that is the strand's record; it cannot close while the account has a gap (cfg_escalation_requirement strand_account_clean) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| state | TEXT |  | ✓ |  |  | cfg_enum reading_strand_state | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| note | TEXT |  |  |  |  | free note | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| thread_id | INTEGER |  |  |  | escalation.id | the strand's own thread (type thread) for the open items its reading raises; set when the first is raised, and again if that thread has completed (#2219) | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |

### reading_strand_strong
_one row per strong in a strand's word family_ — #2172: the word family a strand reads; its hits are every live verse_lexical occurrence of these strongs
dedup key: `strand_id, strong`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| strand_id | INTEGER |  | ✓ |  | reading_strand.id | the strand | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| strong | TEXT |  | ✓ |  |  | the exact Strong's code (suffixed, zero-padded: H0639G) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| note | TEXT |  |  |  |  | why the word is in the family, or which sense | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |

### reading_strand_hit
_one row per hit: a strand strong in a verse_ — #2172 safeguard 1: every hit has a face, or a stated reason it has none, before the strand can close; the observation the hit went into
dedup key: `strand_id, verse_id, strong`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| strand_id | INTEGER |  | ✓ |  | reading_strand.id | the strand | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| verse_id | INTEGER |  | ✓ |  | verse.id | the verse | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| strong | TEXT |  | ✓ |  |  | the strong as in verse_lexical | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| surface | TEXT |  |  |  |  | the English surface of the hit (verse_lexical) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| face | TEXT |  |  |  |  | the face the reading gives the hit: its label and words (e.g. 'A. With his people as a whole'); NULL until read | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| parties | TEXT |  |  |  |  | who acts in the hit, toward whom | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| reason | TEXT |  |  |  |  | why the hit has no face (e.g. another sense of the word); a read hit has a face or a reason | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| observation_id | INTEGER |  |  |  | ib_observation.id | the observation the hit went into, if any | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| run_id | TEXT |  |  |  |  | the Strand-Reading run that read the hit | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| created_at | TEXT |  | ✓ |  |  | when the row was written (ISO-8601 UTC) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md) |

### reading_strand_item
_one row per open thread item a strand must answer or has raised_ — #2219: the open items of a strand -- 'matched' (Strand-Reading Context: an open item matching the strand's words, their clusters, its verses or its code; the close gate refuses while one has no thread response since it was matched) or 'raised' (found in the strand's reading, on its own thread)
dedup key: `strand_id, item_id`
| column | type | pk | notnull | unique | fk | use | source/filled_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |  | surrogate PK | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |
| strand_id | INTEGER |  | ✓ |  | reading_strand.id | the strand | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |
| item_id | INTEGER |  | ✓ |  | escalation_thread_item.id | the open item (escalation_thread_item) | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |
| source | TEXT |  | ✓ |  |  | cfg_enum reading_strand_item_source: matched (to answer) or raised (found in the reading) | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |
| matched_on | TEXT |  |  |  |  | matched: the strand's words, clusters, verses or code it matched; raised: the step that raised it | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |
| created_at | TEXT |  | ✓ |  |  | when the item was recorded against the strand (ISO-8601 UTC); a matched item is answered by a thread response at or after this | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |
| created_by | TEXT |  | ✓ |  |  | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md) |

<a id="11-enums"></a>
## 11. Enums

| enum | values |
| --- | --- |
| behaviour_rule_deliver_when | always, study_active, developer_mode |
| behaviour_rule_enforcement_status | mechanically_enforced, partially_enforced, buildable_not_built, judgment_call_pending, not_mechanically_checkable, deliberately_deferred, context_delivered |
| candidate_decision | candidate, rejected, undecided, exception |
| candidate_ib_referent | characteristic, other_being, body_part |
| candidate_source | registry-direct, curated-synonym, ib-judgement, read-emergent |
| candidate_step_status | in_strong, step_no_verses, not_in_step, step_has_verses_pending |
| cfg_change_op | insert, update, delete |
| cfg_observation_enhancer_rule.status | draft, confirmed, active, retired |
| cluster.status | strong_assignment_in_progress, t_cluster_assignment_completed, ready_for_subgroup_allocation, ready_for_reading, ready_for_observations, ready_for_synthesis, completed, strongs_reassigned |
| cluster_subgroup.status | allocated, ready_for_reading, ready_for_answer, answer_complete, completed, re_read_needed |
| compliance_rule_status | engaged, not engaged |
| config_module | registry, raw, step, report, candidate, passage, configmaint, validation, governance, retention, notification, table_export, escalation, lexicon, method, narrative, cluster, manifest, backup, content_index, behaviour, database, prose, pathaudit, lexical, strand_reading |
| control_home_type | cfg_table, db_table, document, folder, harness |
| control_read_when | always, session_start, when_invoked, when_needed, history_only |
| escalation_answer | approve, reject, revise |
| escalation_assignee | Claude, Researcher |
| escalation_next_action | approve, reject, revise, noted, hold, review, ready_for_approval, approved |
| escalation_next_action_dispatcher | approve, reject, revise, hold, noted |
| escalation_next_action_manual | ready_for_approval, approved, reject, revise, noted, review |
| escalation_raise_state | raised, on-hold, in-progress |
| escalation_requirement_check_kind | field_required, not_raised_with_content, exists, not_self, requires_prior_ready_for_approval_if_decision_required, actor_must_be_assignee, decision_required_approval_requires_researcher, requires_current_ready_for_approval_if_decision_required, reassign_to_researcher_requires_ready_for_approval, no_open_thread_items, must_be_self_correctable, strand_account_clean |
| escalation_shape | manual, dispatcher |
| escalation_state | raised, answered, re-assign, on-hold, paused, closed, retracted, withdraw, completed, in-progress, supersede, re-assigned |
| escalation_state_open | raised, in-progress, re-assigned |
| escalation_state_parked | on-hold |
| escalation_state_terminal | completed, closed, withdraw, supersede |
| escalation_thread_item_kind | cluster, strong, verse, strand, chapter, event, researcher, escalation |
| escalation_thread_item_response_kind | touched, narrowed, forward, ruling, note, closed, reopened, withdrawn, superseded |
| escalation_thread_item_status | open, closed, withdrawn, superseded |
| escalation_type | prompted, task, interactive, run_error, issue, report-stop, crash, notice, config, note, thread |
| folder_purpose_status | authoritative, mixed, reallocate, stale, deleted |
| folder_purpose_type | archive, operations, results |
| hib_kind | named_individual, unnamed_individual, named_collection, unnamed_collection, implicit_individual, implicit_collection |
| ib_observation.basis | read, stated |
| ib_observation.meaning_source | strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce, strong_lexicon, verse-text, role-tags, cluster, observations, n/a |
| ib_observation.stage | verse-reading, char-subgroup, char-reading, char-answers, char-synergy, strand-reading |
| ib_observation.status | resolved, needs-corroboration, open, silent, withdrawn, draft |
| ib_observation.tag | instance-meaning, verse-grouping, difference-inference, surface-gloss-divergence, no-human-context, cross-cluster-significance, data-error, alternative-meaning, could-not-resolve, answered-no-flag, tightly-related, no-direct-connection, qualifier-for-term, no-impact, not-related-to-meaningful-word, sole-mcode-in-verse, cluster-pole-negative, cluster-pole-positive, attested-pre-nt, nt-coinage, needs_adjacent_verse_context, elevation-candidate, key-statement |
| ib_observation.window | meaning, action-impact, relational, literary, cognitive, affective, operational, constitutional, origin, scientific, Subgroup, faculty |
| lexical_code_class | negator, connective_causal, connective_coordinating, connective_purpose, party_divine, party_human, party_angelic |
| narrative_change_basis | recorded, reconstructed, direct edit |
| narrative_chapter_kind | front matter, chapter, part heading, opening, activity, key characteristic, other beings, deferred |
| narrative_chapter_state | draft, draft + held, empty, deferred |
| narrative_claim_change_kind | claim created, claim restated, verdict changed, claim withdrawn, telling added, telling changed, telling removed, passage moved, renumbered, edited |
| narrative_claim_origin | original essay, narrative |
| narrative_claim_source_kind | verse, lexical, science, study file, observation |
| narrative_claim_status | current, withdrawn, held |
| narrative_claim_verdict | Stands, Widened, Restated, Withdrawn, Held, Added, New, Removed, Corrected |
| narrative_required_channel | Non-human ↔ human, Human ↔ human, Physical world ↔ human |
| narrative_telling_kind | in full, in part, pointer |
| narrative_telling_status | current, removed, superseded |
| narrative_update_ref_kind | escalation, thread, thread item |
| note_type | idiom, pronoun_resolution, noun_relational, noun_severity, chain, connective, related_word, polarity, entity_link, inert, structural_pattern, recurrence_role_shift, cross_lemma_shared_gloss, verb_argument, compound_unit |
| on_fail | report-continue, pause-continue, report-stop, self-heal |
| operation_decision | retain, set_aside, retain_referential, recorded_silence |
| party_kind | divine, human, non_human |
| passage_debate_status | scaffold, filled, empty, in-progress, complete |
| passage_source | passage-build, single-verse-emergent |
| project_database | iba, bible_research |
| prose_section_author | claude_ai, claude_code, researcher |
| prose_section_status | draft, in_review, approved, archived |
| prose_section_type_book_label | Programme, Detail design, Findings, Essays, Word Index and Glossary |
| prose_section_type_lifecycle_tag | source, v1, v2, v3 |
| prose_section_type_source_stage | programme, session_a, session_b, session_b_phase9, session_c, session_d, synthesis, verse-analysis, findings, essay, contributor |
| reading_strand_item_source | matched, raised |
| reading_strand_state | closed, open, withdrawn |
| record_change_log_change_type | insert, change, delete |
| record_change_log_status | change_proposed, change_applied, declined |
| resolution_kind | decision_required, self_correctable |
| resolution_status | resolved, unresolved, unclassified, not_supported_this_language, checked_empty |
| rule_scope_kind | general, ps, command, path |
| run_batch.status | running, committed, failed |
| run_state | running, paused, done, failed |
| step_kind | operations, utility |
| study_state | active, on_hold |
| table_category | rule, data, log |
| table_purpose_kind | purpose, success |
| verse_meta_status | exclude, citated, analysed |
| wa_obs_question_catalogue.scope | Word/term (lexical), Verse-context, The verse, Characteristic (HIB behaviour), Characteristic relational, The HIB, Other non-human beings |
| wa_obs_question_catalogue.status | active, retired |
| wa_obs_question_catalogue.tier | M0, D1, D2, D3, D4, D5, D6, D7, D9, D10, D11, D12, X0, F0, T7 |
| word_status | proposed, approved, raw-complete, signed-off, rejected |
| word_status_built | raw-complete, signed-off |
| writer_identity | run, escalation, migration, call1_meanings, call2_getInfo, call3_strong, report.debate |

<a id="12-book-order"></a>
## 12. Book order

66 books, canonical order — first `Gen`, last `Rev`.

<a id="13-change-log-every-accepted-load-audit"></a>
## 13. Change-log — every accepted load (audit)

| # | loaded_at | config_version | seed_hash | validated |
| --- | --- | --- | --- | --- |
| 1 | 2026-07-18T03:26:55Z | app-0.1.0 | 6d99b2d0554df65e | 1 |
| 2 | 2026-07-18T03:27:45Z | app-0.1.0 | 6d99b2d0554df65e | 1 |
| 3 | 2026-07-18T03:27:46Z | app-0.1.0 | 6d99b2d0554df65e | 1 |
| 4 | 2026-07-18T07:30:27Z | app-0.1.0 | 6fb4416dec799109 | 1 |
| 5 | 2026-07-18T09:28:06Z | app-0.1.0 | 3fb2bd8ae7d47887 | 1 |
| 6 | 2026-07-18T15:36:16Z | app-0.1.0 | 7d5d2ff1c8ba067f | 1 |
| 7 | 2026-07-18T17:41:53Z | app-0.1.0 | 86468beaae09fe28 | 1 |
| 8 | 2026-07-21T14:20:25Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 9 | 2026-07-21T14:20:30Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 10 | 2026-07-21T14:22:11Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 11 | 2026-07-21T14:24:17Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |
| 12 | 2026-07-21T14:25:14Z | app-0.1.0 | bootstrap:configuration-maintenance-2026-07-21 | 1 |

<a id="14-reports-full-governance-per-report"></a>
## 14. Reports — full governance per report

_One block per registered report — everything that governs it, joined from `cfg_report`, `cfg_report_section`, `cfg_report_csv_table`, `cfg_work_package`, and `cfg_on_fail`. The ownership ledger (which config item governs what) is in GOVERNANCE.md._

### `candidate.load`
**candidate.load report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `candidate-curation` → `iba/app/ps/archive/Candidate-Curate.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | duplicates | ## Duplicates skipped (not written) | Duplicates skipped (not written) | ✓ |
| 1 | exceptions | ## Exception rows | Exception rows | ✓ |
CSV pairing: `candidate_seed` (this run's decision='exception' rows)

| condition | path | route | message |
| --- | --- | --- | --- |
| needs-review | pause-continue | terminal | candidate.load has unresolved exception row(s) in candidate_seed needing researcher judgement |

### `candidate.validate`
**Candidate quality report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `candidate-quality` → `iba/app/ps/archive/Candidate-Quality.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | span_tag | ## span_candidate.candidate_tag (the stamp) | span_candidate.candidate_tag (the stamp) | ✓ |
| 1 | seed_tag | ## candidate_seed.tag (the seed decision — a worklist, not a verdict) | candidate_seed.tag (the seed decision — a worklist, not a verdict) | ✓ |
| 2 | gloss | ## lemma_inventory.gloss (the independent substrate) | lemma_inventory.gloss (the independent substrate) | ✓ |
| 3 | orphan_lemmas | ## Lemmas with no strong entry yet (by frequency) | Lemmas with no strong entry yet (by frequency) | ✓ |
CSV pairing: `candidate_seed`; `lemma_inventory`; `span_candidate`

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged candidate quality findings as needing action |
| needs-review | pause-continue | terminal | span_candidate has tag/lemma_key quality findings needing researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `cluster.validate`
**Cluster-assignment quality report** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `cluster-assign` → `iba/app/ps/Cluster-Assign.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | exceptions_no_word | ## Exception -- non-T2 cluster, no word_registry link | Exception - no word | ✓ |
| 2 | exceptions_sibling_conflict | ## Exception -- backfill code with an active/clustered sibling | Exception - sibling conflict | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged cluster-assignment exceptions as needing action |
| needs-review | pause-continue | terminal | cluster-assignment exceptions need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `configmaint.report`
**IBA app — configuration report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `configuration-maintenance` → `iba/app/ps/Config-Maintenance.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | findings | ## 0. Findings — needing researcher judgement | 0. Findings — needing researcher judgement | ✓ |
| 1 | inactive_configs | ## 1. Inactive configs — historical record, not a decision | 1. Inactive configs — historical record, not a decision | ✓ |
| 2 | utilities | ## 2. Utilities registry | 2. Utilities registry | ✓ |
| 3 | connection | ## 3. Connection (STEP) | 3. Connection (STEP) | ✓ |
| 4 | settings | ## 4. Settings — every rule / threshold, grouped by owning module | 4. Settings — every rule / threshold, grouped by owning module | ✓ |
| 5 | apis | ## 5. STEP apis | 5. STEP apis | ✓ |
| 6 | work_packages | ## 6. Work packages & steps (the sequence) | 6. Work packages & steps (the sequence) | ✓ |
| 7 | on_fail | ## 7. on_fail — condition -> path (the fork rules) | 7. on_fail — condition -> path (the fork rules) | ✓ |
| 8 | write_grants | ## 8. Write grants — who may write what | 8. Write grants — who may write what | ✓ |
| 9 | status_flow | ## 9. Status flow | 9. Status flow | ✓ |
| 10 | schema | ## 10. Schema — data tables built from config | 10. Schema — data tables built from config | ✓ |
| 11 | enums | ## 11. Enums | 11. Enums | ✓ |
| 12 | book_order | ## 12. Book order | 12. Book order | ✓ |
| 13 | change_log | ## 13. Change-log — every accepted load (audit) | 13. Change-log — every accepted load (audit) | ✓ |
| 14 | report_governance | ## 14. Reports — full governance per report | Reports — full governance per report | ✓ |
| 15 | control_map | ## 15. Control map — one home per kind of control | 15. Control map — one home per kind of control | ✓ |
CSV pairing: `cfg_*` (every cfg_* table, one CSV per table — the config store's own verbatim dump)

### `escalation.context`
**What the open escalations point to** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | items | ## Open escalations and their files | Escalations | ✓ |

### `escalation.history`
**Escalation deep history** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | item_history | ## #<id> — <short_description> | Item history | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| bad-parameter | report-continue | terminal | usage error, not recorded as an escalation -- check -Id (id or OT-nn) |

### `escalation.list`
**Open escalations** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | open_items | # Open escalations | Open items | ✓ |
| 6 | recently_resolved | ## Recently resolved (last 15) | Recently resolved | ✓ |
CSV pairing: `escalation` (raw, unprocessed dump of the escalation table itself -- NOT the exception-category findings (those are markdown-only report sections, D4 correction from v4's original, wrong claim that the CSV was the flagged-exception rows).)

### `escalation.thread`
**Open threads** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| bad-parameter | report-continue | terminal | usage error, not recorded as an escalation -- check -Id (id or OT-nn) and -State (on-hold\|in-progress) |

### `escalation.thread_audit`
**Thread audit** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | findings | ## Findings by check | Findings | ✓ |

### `escalation.thread_export`
**Open threads register** — output `md` · naming `stable` · archived to `archive/` · ToC off · footer: Generated from the escalation table (type=thread) by Escalation.ps1 -Action Export -Type thread. Do not edit by hand: respond through Escalation.ps1 -Action Update.
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

### `lexical.readiness`
**Lexical readiness check (3-leg, #1606)** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `verse-lexical` → `iba/app/ps/VerseLexical.ps1` (chained=1)
- on completion: _lexical built and rendered for '{book}'._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | detail | ## Detail | Detail | ✓ |

### `lexicon.validate`
**Lexicon-parse quality report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `lexicon-parse` → `iba/app/ps/Lexicon-Parse.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | coverage | ## Coverage — strong_lexicon/strong rows with no parsed/related output | Coverage — strong_lexicon/strong rows with no parsed/related output | ✓ |
| 2 | value_quality | ## Value quality — gloss findings | Value quality — gloss findings | ✓ |
CSV pairing: `strong` (the raw table this report analyzes for its coverage check); `strong_lexicon` (the raw table this report analyzes for lexicon-detail coverage); `strong_lsj_parsed`; `strong_meaning_parsed`; `strong_mounce_parsed`; `strong_related`

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged lexicon-parse quality findings as needing action |
| needs-review | pause-continue | terminal | lexicon-parse coverage/value-quality findings need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `manifest.rebuild`
**Project file manifest — rebuild summary** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `file-manifest-rebuild` → `iba/app/ps/Manifest-Rebuild.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | by_category | ## By category | By category | ✓ |
| 2 | by_currency | ## By currency | By currency | ✓ |

### `narrative_register.check`
**Narrative register check** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `narrative-register` → `iba/app/ps/Narrative-Register.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `narrative_register.find`
**Narrative register search** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `narrative-register` → `iba/app/ps/Narrative-Register.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `narrative_register.history`
**Narrative claim history** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `narrative-register` → `iba/app/ps/Narrative-Register.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `narrative_register.quote_check`
**Quote check** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `narrative-register` → `iba/app/ps/Narrative-Register.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| quotes-failing | report-continue | terminal | quotations not found in the ESV text -- correct them, or disposition each at session-close |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `passage.validate`
**Passage quality report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `passage-quality` → `iba/app/ps/Passage-Quality.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | dist | ## verse_count distribution | verse_count distribution | ✓ |
| 1 | by_book | ## By book | By book | ✓ |
CSV pairing: `passage`; `verse_passage`

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged the passage distribution as needing the rule revisited |
| needs-review | pause-continue | terminal | passage verse_count distribution needs researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `pathaudit.scan`
**Project-wide hardcoded-location-literal scan** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `path-audit` → `iba/app/ps/PathAudit.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | findings | ## Findings | Findings | ✓ |

### `purge.audit`
**Soft-delete purge audit (app-wide, #1766)** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `purge-audit` → `iba/app/ps/Purge-SoftDeletes.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | safe | ## Safe to purge | Safe to purge | ✓ |
| 2 | unsafe | ## Unsafe -- live dependency risk | Unsafe -- live dependency risk | ✓ |

### `purge.execute`
**Soft-delete purge execute (app-wide, #1766/#1868)** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `purge-audit` → `iba/app/ps/Purge-SoftDeletes.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | purged | ## Purged | Purged | ✓ |
| 2 | skipped | ## Skipped | Skipped | ✓ |

### `purge.retire_database`
**Database retirement — inactive tables cleared (#1868/#1872/#1873)** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `purge-audit` → `iba/app/ps/Purge-SoftDeletes.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | fk-cleanup | ## Dangling FK cleanup on retained tables | Dangling FK cleanup on retained tables | ✓ |
| 2 | purged | ## Cleared | Cleared | ✓ |

### `report.batch_progress`
**Batch progress monitor** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `batch-progress-report` → `iba/app/ps/BatchProgress.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | running_now | ## Currently running | Running now | ✓ |
| 2 | recent_failures | ## Recent failures | Recent failures | ✓ |
| 3 | recent_committed | ## Recent committed batches | Recent committed | ✓ |

### `report.book_narrative_generate`
**{book_label} — Inner-Being Narrative** — output `md` · naming `stable` · archived to `archive/` · ToC off · footer: *Generated by `report.book_narrative_generate` from the book's filled passage debates — see `WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` and `WA-inner-being-narrative-guidance-v1-2026-07-28.md` for the governing instructions. Run `BookNarrative-Validate.ps1` against this file next.*
work package `book-narrative` → `iba/app/ps/archive/Book-Narrative.ps1` (chained=1)
- on completion: _narrative generated and structurally validated._
- next-step hint: _none -- narrative + validation both complete_
- paused override: _cost/token estimate printed above -- answer the escalation (Approve/Reject/Revise) then re-run this exact command with the same -RunId to make the live API call and continue automatically to validation._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| api-error | report-stop | terminal | the Messages API returned a non-2xx response |
| api-key-missing | report-stop | terminal | ANTHROPIC_API_KEY not found in the environment or repo-root .env |
| cost-cap-exceeded | report-stop | terminal | the pre-call cost estimate exceeds narrative.generate_max_cost |
| declined | report-stop | terminal | researcher rejected the escalation |
| guidance-doc-missing | report-stop | terminal | a method.* cfg_setting points to a file that does not exist on disk |
| needs-approval | pause-continue | terminal | researcher approval required before the live API call is made |
| needs-revision | report-stop | terminal | researcher asked for a change first (see comment) |
| no-debates-found | report-stop | terminal | no filled report.passage_debate exists yet for this book |

### `report.book_narrative_validate`
**Book-Narrative Scope Self-Check — {path}** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `book-narrative` → `iba/app/ps/archive/Book-Narrative.ps1` (chained=1)
- on completion: _narrative generated and structurally validated._
- next-step hint: _none -- narrative + validation both complete_
- paused override: _cost/token estimate printed above -- answer the escalation (Approve/Reject/Revise) then re-run this exact command with the same -RunId to make the live API call and continue automatically to validation._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | findings | ## Findings | Findings | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| guidance-doc-missing | report-stop | terminal | method.inner_being_narrative_guidance_path points to a file that does not exist on disk — the config is stale relative to iba/docs/ |
| narrative-file-missing | report-stop | terminal | the given -Path does not exist on disk |
| no-path-given | report-stop | terminal | -Path is required — the narrative file to check |
| scope-check-incomplete | report-stop | terminal | one or more required channel labels are missing or left as an unfilled placeholder |
| scope-check-missing | report-stop | terminal | no '## Scope self-check' section found — add one per the guidance doc section 3 |

### `report.cluster`
**Cluster taxonomy and strong-assignment coverage** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `cluster-report` → `iba/app/ps/Cluster-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | clusters | ## Cluster taxonomy | Cluster taxonomy | ✓ |
| 1 | by_cluster | ## Word-origin strong count per cluster | Word-origin count per cluster | ✓ |
| 2 | gap_list | ## Word-origin gap list | Word-origin gap list | ✓ |
| 3 | cluster_summary | ## Cluster summary -- every origin | Cluster summary (all origins) | ✓ |
| 4 | backfill_typology | ## Backfill vocabulary outside the cluster taxonomy | Backfill vocabulary (outside clusters) | ✓ |
CSV pairing: `backfill_crossmatch` (untagged backfill strongs whose gloss keywords match a clustered strong's or a registry word's); `backfill_residual` (untagged backfill strongs with no cross-match, with their gloss stem key); `backfill_typology` (every untagged backfill strong with its heuristic type (proper_noun / grammatical_marker / closed_class / candidate_vocabulary)); `cluster`; `cluster_strong` (joined to strong.stepGloss/language and cluster.short_name); `strong_without_cluster` (word-origin strong rows with no cluster_strong assignment -- the LLM-allocation target set)

### `report.lexical_exceptions`
**{book} {range} — lexical.enrich exception report** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `verse-lexical` → `iba/app/ps/VerseLexical.ps1` (chained=1)
- on completion: _lexical built and rendered for '{book}'._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | layer1_tally | ## Layer 1 tally (mechanical, complete enumeration) | Layer 1 tally (mechanical) | ✓ |
| 1 | layer2_dispositions | ## Layer 2 dispositions (judgement, complete against Layer 1's total) | Layer 2 dispositions | ✓ |
| 2 | judgement_calls | ## Judgement calls made this run, each labelled | Judgement calls | ✓ |
| 3 | integrity | ## Integrity check (dangling verse_lexical_note references) | Integrity check | ✓ |

### `report.obs_catalogue`
**Observation question catalogue — structural review** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `catalogue-report` → `iba/app/ps/Catalogue-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | overview | ## Overview — lifecycle breakdown | Overview — lifecycle breakdown | ✓ |
| 1 | lifecycle_conflicts | ## Lifecycle conflicts (status vs deleted) | Lifecycle conflicts (status vs deleted) | ✓ |
| 2 | naming_schemes | ## Naming schemes and format inconsistencies | Naming schemes and format inconsistencies | ✓ |
| 3 | tier_structure | ## Tier structure — live, tiered questions | Tier structure — live, tiered questions | ✓ |
| 4 | unclassified | ## Unclassified — live questions with no tier | Unclassified — live questions with no tier | ✓ |

### `report.registry`
**Registry evaluation report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `registry-report` → `iba/app/ps/Registry-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | by_strong | ## Registry word joined to strong | Registry word joined to strong | ✓ |
| 2 | sense_report | ## Sense report -- registry word by gloss/broad meaning | Sense report by gloss | ✓ |
| 3 | listing | ## Registry listing (all words) | Registry listing (all words) | ✓ |
CSV pairing: `word_registry` (plain word_registry listing, no join -- one row per registry word regardless of word_strong linkage; CSV mirror of the listing report section (BUILD.md sec89)); `word_registry_strong_pairing` (joined to word_strong/strong/strong_sense); `word_strong` (the raw junction table itself, not just its joined pairing export)

### `report.schema_overview`
**Schema overview** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `schema-overview-report` → `iba/app/ps/SchemaOverview-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | overview | ## Table inventory | Table inventory | ✓ |
| 1 | tables | ## Every data table, in full | Every data table, in full | ✓ |

### `report.schema_overview_bible_research`
**Schema overview - bible_research** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `schema-overview-report-bible-research` → `iba/app/ps/SchemaOverview-BibleResearch-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | overview | ## Table inventory | Table inventory | ✓ |
| 1 | tables | ## Every table, in full | Every table, in full | ✓ |

### `report.seed_candidate`
**Seed-candidate report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `seed-candidate-report` → `iba/app/ps/archive/SeedCandidate-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | distribution | ## Distribution — tag length and rows per lemma | Distribution — tag length and rows per lemma | ✓ |
| 2 | top_lemmas | ## Top lemmas by candidate-row count | Top lemmas by candidate-row count | ✓ |
| 3 | over_time | ## Open vs resolved over time | Open vs resolved over time | ✓ |
CSV pairing: `candidate_seed` (joined to lemma_inventory.gloss)

### `report.span_analysis`
**Span-analysis report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `span-analysis-report` → `iba/app/ps/SpanAnalysis-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | by_book | ## Coverage by book | Coverage by book | ✓ |
| 1 | morph_distribution | ## morph_code distribution | morph_code distribution | ✓ |
| 2 | particle_split | ## Particle vs non-particle spans | Particle vs non-particle spans | ✓ |
CSV pairing: `span`; `span_candidate`; `verse` (read for preview text in the sample-verses section)

### `report.strong_meaning`
**Strong-meaning report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `strong-meaning-report` → `iba/app/ps/StrongMeaning-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | gap_list | ## strong rows with no strong_sense yet (by usage count) | strong rows with no strong_sense yet (by usage count) | ✓ |
| 1 | sense_distribution | ## Sense-count distribution (strong_meaning_tree) | Sense-count distribution (strong_meaning_tree) | ✓ |
| 2 | sense_by_registry | ## Sense distribution by registered word (with gloss) | Sense distribution by registered word (with gloss) | ✓ |
| 3 | lexicon_completeness | ## Lexicon completeness (lsj / mounce) | Lexicon completeness (lsj / mounce) | ✓ |
CSV pairing: `strong` (the raw table this report analyzes for lexicon-completeness/gap-list sections); `strong_lexicon` (the raw table this report analyzes for lexicon-completeness sections); `strong_meaning_tree` (joined to strong.stepGloss via lemma_key); `strong_sense` (joined to strong.stepGloss)

### `report.strong_verse`
**{word} -- {strong} -- verse restatement by Strongs reference** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `strong-verse-report` → `iba/app/ps/StrongVerse-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | senses | ## Exact-variant senses | Exact-variant senses | ✓ |
| 1 | verses | ## Verses | Verses | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| strong-not-linked | report-stop | terminal | the requested Strongs code is not linked to this registry word (word_strong) |
| word-not-found | report-stop | terminal | the requested word is not in the registry |

### `report.verse_lexical`
**{book} {range} — verse : verse_lexical extract** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `verse-lexical` → `iba/app/ps/VerseLexical.ps1` (chained=1)
- on completion: _lexical built and rendered for '{book}'._

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | coverage | ## Reading coverage (content-role codes, this range) | Reading coverage (content-role codes, this range) | ✓ |
| 1 | verses | ## Verses | Verses | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| no-readings | report-stop | terminal | no verse_lexical rows exist yet for this exact book/range — run lexical.build first (it is ordinal 0 of this same work package, run automatically before this step unless called standalone). |

### `report.whole_book_read`
**{book} -- Whole-Book Read** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `whole-book-read` → `iba/app/ps/WholeBookRead-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | coverage | ## Coverage | Coverage | ✓ |
| 1 | carried_forward | ## Carried forward per passage | Carried forward per passage | ✓ |
| 2 | not_found | ## Sections not found — verify heading | Sections not found — verify heading | ✓ |
| 3 | closing | ## Closing synthesis | Closing synthesis | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| no-debates-found | report-stop | terminal | no debate_status='filled' passage row exists yet for this book — run at least one report.passage_debate pass and fill it in first |

### `report.word`
**Raw layer — `{word}`** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | validation | ## Validation | Validation | ✓ |
| 1 | strongs | ## The strongs and their meaning (L1 → L2) | The strongs and their meaning (L1 → L2) | ✓ |
| 2 | sample_verses | ## Sample verses — the span layer (one row per code) | Sample verses — the span layer (one row per code) | ✓ |
CSV pairing: `span` (word-scoped); `word_strong` (word-scoped)

| condition | path | route | message |
| --- | --- | --- | --- |
| word-not-found | report-stop | terminal | the requested word is not in the registry |

### `report.word_registry_span`
**{word} — linked Strong's, parse meaning, span analysis** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `word-registry-span-report` → `iba/app/ps/archive/WordRegistrySpan-Report.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | overview | ## Overview | Overview | ✓ |
| 1 | strongs | ## Linked Strong's — parse meaning & span analysis | Linked Strong's — parse meaning & span analysis | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| word-not-found | report-stop | terminal | the requested word is not in the registry |

### `retention.report`
**Log retention & run-health report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `log-retention` → `iba/app/ps/Log-Retention.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | stuck_chained | ## Stuck chained runs (archival candidates — not relabelled; see lib/retention.py) | Stuck chained runs (archival candidates — not relabelled; see lib/retention.py) | ✓ |
| 2 | open_escalations | ## Open escalations (oldest first) | Open escalations (oldest first) | ✓ |
| 3 | recent_failed | ## Recent failed runs (last 50) | Recent failed runs (last 50) | ✓ |
| 4 | stuck_nonchained | ## Stuck non-chained runs (unambiguous crash signal -- safe to re-submit; see lib/retention.py) | Stuck non-chained runs (unambiguous crash signal -- safe to re-submit; see lib/retention.py) | ✓ |
CSV pairing: `escalation`; `run`; `validation_result`

### `session.close`
**Session close (#1875, rebuilt #2173)** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `session-close` → `iba/app/ps/Session-Close.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | escalation_gaps | ## Escalation update coverage | Escalation update coverage | ✓ |
| 1 | sc1 | ## SC1 Session and window | SC1 | ✓ |
| 2 | governance_gaps | ## Governance / config / doc drift | Governance / config / doc drift | ✓ |
| 2 | sc2 | ## SC2 Spine (FATAL) | SC2 | ✓ |
| 3 | build_gaps | ## BUILD.md coverage | BUILD.md coverage | ✓ |
| 3 | sc3 | ## SC3 Researcher's words recorded | SC3 | ✓ |
| 4 | sc4 | ## SC4 Open items in the register | SC4 | ✓ |
| 5 | sc5 | ## SC5 Analysis integrity | SC5 | ✓ |
| 6 | sc6 | ## SC6 Rule compliance | SC6 | ✓ |
| 7 | sc8 | ## SC8 Session log | SC8 | ✓ |
| 8 | sc9 | ## SC9 Decisions reached their targets | SC9 | ✓ |
| 9 | sc10 | ## SC10 BUILD.md coverage | SC10 | ✓ |
| 10 | sc12 | ## SC12 Publish | SC12 | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-open | report-continue | terminal | session-close found open findings -- the commit is blocked until each is fixed or carried (Session-Close.ps1 exits 3); remediation is Claude's, not an approval cycle |
| gaps-found | report-continue | terminal | session-close detected one or more gaps — see report for detail; remediation is Claude's own follow-up via .claude/commands/session-close.md, not a blocking approval cycle |

### `spine.check`
**Base-data spine integrity check** — output `md` · naming `stable` · archived to `archive/` · ToC on
work package `spine-check` → `iba/app/ps/Spine-Check.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | summary | ## Summary | Summary | ✓ |
| 1 | integrity | ## Integrity (FATAL) | Integrity (FATAL) | ✓ |
| 2 | discoverability | ## Discoverability | Discoverability | ✓ |
| 3 | meaning_by_design | ## Meaning gaps by design (STEP holds nothing) | Meaning gaps by design | ✓ |

| condition | path | route | message |
| --- | --- | --- | --- |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |
| spine-fatal-found | pause-continue | terminal | spine has FATAL findings needing researcher judgement |
| spine-fatal-rejected | report-stop | terminal | researcher flagged FATAL spine findings as needing action |

### `strand_reading.account`
**Strand account** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `strand-reading` → `iba/app/ps/Strand-Reading.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `strand_reading.context`
**Strand context** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `strand-reading` → `iba/app/ps/Strand-Reading.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `strand_reading.gather`
**Strand gather** — output `md` · naming `dated` · archived to `archive/` · ToC off
work package `strand-reading` → `iba/app/ps/Strand-Reading.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| _(none)_ | _(none)_ | _(none)_ | _(none)_ | _(none)_ |

| condition | path | route | message |
| --- | --- | --- | --- |
| refused | report-continue | terminal | refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation) |

### `validation.book`
**Base validation report — book '{book}'** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | app_db | ## 1. App & DB | 1. App & DB | ✓ |
| 1 | candidate | ## 3. Candidate (L4b) | 3. Candidate (L4b) |  |
| 2 | passages | ## 4. Passages | 4. Passages | ✓ |
| 3 | value_quality | ## 6. Value quality | 6. Value quality | ✓ |
CSV pairing: `candidate_seed` (book-scoped); `passage` (book-scoped); `verse_passage` (book-scoped)

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged the validation findings as needing action, not just acknowledgement |
| needs-review | pause-continue | terminal | validation findings need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

### `validation.word`
**Validation report — '{word}'** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | app_db | ## 1. App & DB | 1. App & DB | ✓ |
| 1 | pre_post | ## 2. Pre/post | 2. Pre/post | ✓ |
| 2 | integrity | ## 3. Integrity | 3. Integrity | ✓ |
| 3 | references | ## 4. References | 4. References | ✓ |
| 4 | expectations | ## 5. Expectations | 5. Expectations | ✓ |
| 5 | value_quality | ## 6. Value quality | 6. Value quality | ✓ |
CSV pairing: `span` (word-scoped, same slice report.word checks); `word_strong` (word-scoped)

| condition | path | route | message |
| --- | --- | --- | --- |
| findings-rejected | report-stop | terminal | researcher flagged the validation findings as needing action, not just acknowledgement |
| needs-review | pause-continue | terminal | validation findings need researcher judgement |
| needs-revision | report-stop | terminal | researcher asked for more specific investigation (see comment) |

<a id="15-control-map-one-home-per-kind-of-control"></a>
## 15. Control map — one home per kind of control

| kind | home_type | home | read_when | history_home | description |
| --- | --- | --- | --- | --- | --- |
| session_entry | document | CLAUDE.md | always | git history of CLAUDE.md | What the Claude Code harness loads into every conversation. Holds only: what the project is, how a session starts (/start-project or /developer-mode), and pointers to this map, CHARTER.md and USER-GUIDE.md. No rule text, no study or work state, no history (#2181). |
| objective | document | iba/app/CHARTER.md | when_needed | git history of CHARTER.md | What the IBA app is for, in the researcher's words. Changed only on the researcher's direct instruction. |
| behaviour_rule | cfg_table | cfg_behaviour_rule | session_start | cfg_change_detail (prior row state); retired rows inactive=1 | How Claude and the app must act: every operational, process, interaction, filing and study-method rule. A rule exists here once; every other place names it by rule_key and does not restate it (rule 3). |
| escalation_rule | cfg_table | cfg_escalation, with cfg_escalation_requirement, cfg_escalation_transition, cfg_status_flow | session_start | cfg_change_detail (prior row state); retired rows inactive | How escalations are raised, moved and closed. |
| setting | cfg_table | cfg_setting | when_needed | cfg_change_detail (prior row state); retired rows inactive=1 | Named values the code and routines read: paths, thresholds, governance settings. |
| enum | cfg_table | cfg_enum | when_needed | cfg_change_detail; retired members inactive=1 | The allowed values of every controlled field. |
| schema | cfg_table | cfg_table, cfg_column, cfg_table_purpose, cfg_unique, cfg_index | when_needed | cfg_change_detail; retired rows inactive=1 | What each table and column is, holds and is for. |
| app_procedure | cfg_table | cfg_work_package, cfg_step, cfg_utility, cfg_on_fail, cfg_write_grant, cfg_report | when_needed | cfg_change_detail; retired rows inactive | What the app runs, in what order, what happens on failure, and who may write what. |
| session_procedure | document | .claude/commands/ (start-project.md, session-close.md, developer-mode.md, exit-developer-mode.md) | when_invoked | git history of .claude/commands/ | The order of calls of each session routine. Names rules by key; holds no rule text. |
| harness_control | harness | .claude/settings.json and .claude/hooks/ | always | git history of .claude/ | Hooks, permissions and the statusline that the Claude Code harness enforces. .claude/settings.local.json and the user-level ~/.claude/settings.json hold no project rule. |
| mechanism | document | iba/app/GOVERNANCE.md | when_needed | iba/app/BUILD.md; GOVERNANCE.md's dated sections to 2026-10-21 at archive/docs/governance-md-history-to-20261021.md | How the config governs the code, as it is now: the config store, the change path, the two modes, what is enforced and what is not. Current state only; names rules by key; no dated history (history goes to BUILD.md). |
| tool_usage | document | iba/app/USER-GUIDE.md | when_needed | git history of USER-GUIDE.md | How to run each tool, as it is now. Current state only. |
| change_history | document | iba/app/BUILD.md | history_only | BUILD.md is itself history; with cfg_change_detail, escalation_history and git | The dated record of what changed in the app (code, config, control documents) and why. Read only deliberately, to assess a past state; never the source for how things are now. |
| open_item | db_table | escalation | session_start | escalation_history | Every open item, task, issue, decision or thread (rule 40). No other task ledger. |
| researcher_ruling | db_table | escalation_history (the comment on the escalation the ruling answers) | when_needed | escalation_history is itself history | The researcher's decisions, verbatim. A rule that results goes to its cfg row, with the ruling in that row's source. |
| study_state | db_table | escalation (strand escalations and type=thread items), narrative_chapter, the narrative claim register tables, the narrative's blocks (narrative_section.block_text; governance.narrative_home), the reading_strand tables | when_needed | escalation_history; the register's change records | Where the study stands: strands, what is read, woven, held or forwarded, the chapters and their claims. Not held in CLAUDE.md or memory. |
| study_method | folder | Workflow/Instructions/ -- one live file per subject, named by a cfg_setting path | when_needed | Workflow/Instructions/archive/ | How study work is done (reading, weaving, writing). Rules drawn from a method file live in cfg_behaviour_rule; the file explains, it does not restate. |
| claude_memory | harness | Claude Code project memory (~/.claude/projects/C--Bible-study-projects/memory/) | always | the memory folder's archive files | Only what config cannot hold (who the researcher is; pointers). Never a rule held in config (#2184 settles the contents). |
| generated_report | folder | the path a *.report_path cfg_setting names | when_needed | the report folder's archive/ | Output a tool writes. Never edited by hand and never a source; regenerated, not maintained. |
| escalation_deliverable | folder | outputs/escalation/ ({id}- prefix) | when_needed | outputs/escalation/archive/ | An authored document produced for one escalation's work (rules 60, 64). |
| engineering_note | folder | iba/docs/ | when_needed | iba/docs/archive/ | Engineering or design notes not tied to one escalation (rule 60). |
| session_record | folder | Logs/ (governance.session_log_dir) | history_only | Logs/ is itself history | One log per session: what the session did and decided. |
| study_output | folder | _analytics/ (cluster folders per report.cluster_folder_naming_convention; the exported narrative chapters in _analytics/essay/spirit_soul_body/inner-being-narrative/); outputs/strand-reading/ (each strand's context, gather and account files) | when_needed | each folder's archive/ | The study's working files, and the narrative chapters as exported from iba.db (governance.narrative_home). |
