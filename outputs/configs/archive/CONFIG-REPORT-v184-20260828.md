# IBA app — configuration report

> **Generated snapshot of the live config store** (`iba/app/db/iba.db`, tables `cfg_*`). The DB is master — do not hand-edit this file. Change config only via `configmaint.propose` (approval-gated; see GOVERNANCE.md §5A); this report regenerates automatically after an approved change and is overwritten in place.

| field | value |
| --- | --- |
| database | iba |
| config_version | app-0.1.0 |
| generated_at | 2026-08-28T10:55:45Z |
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

**Stale governance docs** (0) — GOVERNANCE.md older than the newest applied config change:
_(none)_

**Unregistered lib modules** (0) — iba/app/lib/*.py with no cfg_utility row:
_(none)_

**Low config-density utilities** (1) — NON-EXEMPT cfg_utility module with zero real Cfg-method call sites of its own (see §2 Utilities registry for the full module list, including the 11 already declared config_exempt):
1. cfg_utility 'reportkit' (iba\app\lib\reportkit.py) has zero Cfg-method call sites (.setting()/.enum()/.tables()/... under any variable name) — confirm this is a legitimate zero (mark `cfg_utility.config_exempt=1` via `configmaint.propose`) or a real completeness gap

**Orphan book_order** (0) — cfg.book_order() unused, or a duplicate book/ordinal:
_(none)_

**Orphan connection keys** (0) — a cfg_connection key not read via cfg.connection(...) anywhere:
_(none)_

**Orphan candidate rules** (0) — a kind called with zero active rows, or active rows no code asks for:
_(none)_

**Report version clutter** (0) — more than one version of a one-off report simultaneously live in governance.oneoff_report_dir (oneoff_path() found 2026-08-08 to version without archiving, BUILD.md §83) — the rest belong in archive/:
_(none)_

**Unresolvable location settings** (1) — a *_dir/*_path/*_folder value (cfg_setting or any per-module table shaped like it) that does not resolve to a real folder on disk:
2. cfg_prose.prose.patch_output_dir = '"Sessions/Patches"' — 'sessions/patches' does not exist as a folder on disk (project-root-relative)

**Escalation.ps1 ValidateSet drift** (0) — a -Parameter's [ValidateSet(...)] values not matching the live cfg_enum group it's supposed to mirror:
_(none)_

**FolderPurpose.ps1 ValidateSet drift** (0) — same check, for -Type/-Status against folder_purpose_type/folder_purpose_status:
_(none)_

**Hand-rolled versioning** (3) — a script building a -v{n} filename by hand instead of via filingkit.versioned_path()/reportkit.oneoff_path():
3. engine/migrate.py builds a -v{n} filename by hand — no filingkit.versioned_path()/reportkit.oneoff_path() call site in the same file
4. iba/app/lib/escalation.py builds a -v{n} filename by hand — no filingkit.versioned_path()/reportkit.oneoff_path() call site in the same file
5. iba/app/lib/prosestore.py builds a -v{n} filename by hand — no filingkit.versioned_path()/reportkit.oneoff_path() call site in the same file

<a id="1-inactive-configs-historical-record-not-a-decision"></a>
## 1. Inactive configs — historical record, not a decision

**Inactive configs** (392 row(s) across 10 table(s)) — deactivated, not deleted; excluded from validation above. 355 from the candidate-system retraction, 2026-07-23 (GOVERNANCE.md §15D; migration/retract_candidate_system.py); 8 from the passage-system retirement, 2026-07-26 (reports/archive/passage-system-retirement-record-20260726.md); **29 UNATTRIBUTED** (not part of a known retirement — needs a look): cfg_step.book-narrative-generate/report.book_narrative_generate, cfg_step.book-narrative-validate/report.book_narrative_validate, cfg_step.chapter-generate/report.verse_span_meaning, cfg_step.verse-analysis-report/report.verse_span_meaning, cfg_work_package.book-narrative-generate, cfg_work_package.book-narrative-validate, cfg_work_package.chapter-generate, cfg_work_package.verse-analysis-report, cfg_write_grant.escalation -> word_registry, cfg_write_grant.run -> escalation, cfg_enum.escalation_answer=approve, cfg_enum.escalation_answer=reject, cfg_enum.escalation_answer=revise, cfg_enum.escalation_next_action=approve, cfg_enum.escalation_next_action=approved, cfg_enum.escalation_next_action=hold, cfg_enum.escalation_next_action=noted, cfg_enum.escalation_next_action=ready_for_approval, cfg_enum.escalation_next_action=reject, cfg_enum.escalation_next_action=review, cfg_enum.escalation_next_action=revise, cfg_enum.escalation_state=answered, cfg_enum.escalation_state=paused, cfg_enum.escalation_state=re-assign, cfg_enum.escalation_state=retracted, cfg_enum.escalation_type=crash, cfg_enum.escalation_type=interactive, cfg_enum.escalation_type=prompted, cfg_enum.escalation_type=report-stop.
- **cfg_setting** (7): `candidate.concept_delimiter_pattern`, `candidate.lemma_base_pattern`, `candidate.load_report_path`, `candidate.quality_report_path`, `candidate.tag_clean_pattern`, `candidate.tag_max_words`, `candidate.transliteration_pattern`
- **cfg_step** (13): `book-narrative-generate/report.book_narrative_generate`, `book-narrative-validate/report.book_narrative_validate`, `candidate-curation/candidate.curate`, `candidate-curation/candidate.load`, `candidate-quality/candidate.validate`, `chapter-generate/report.passage_debate`, `chapter-generate/report.verse_span_meaning`, `passage-debate-report/report.passage_debate`, `passage-debate-sync/passage.debate_sync`, `seed-candidate-report/report.seed_candidate`, `set-candidates/candidate.seed`, `set-candidates/candidate.set`, `verse-analysis-report/report.verse_span_meaning`
- **cfg_work_package** (10): `book-narrative-generate`, `book-narrative-validate`, `candidate-curation`, `candidate-quality`, `chapter-generate`, `passage-debate-report`, `passage-debate-sync`, `seed-candidate-report`, `set-candidates`, `verse-analysis-report`
- **cfg_write_grant** (8): `candidate.curate -> candidate_seed`, `candidate.load -> candidate_seed`, `candidate.seed -> candidate_seed`, `candidate.seed -> lemma_inventory`, `candidate.set -> span_candidate`, `escalation -> word_registry`, `report.debate -> passage`, `run -> escalation`
- **cfg_report** (3): `candidate.load`, `candidate.validate`, `report.seed_candidate`
- **cfg_report_section** (10): `candidate.load/duplicates`, `candidate.load/exceptions`, `candidate.validate/gloss`, `candidate.validate/orphan_lemmas`, `candidate.validate/seed_tag`, `candidate.validate/span_tag`, `report.seed_candidate/distribution`, `report.seed_candidate/over_time`, `report.seed_candidate/summary`, `report.seed_candidate/top_lemmas`
- **cfg_report_csv_table** (5): `candidate.load/candidate_seed`, `candidate.validate/candidate_seed`, `candidate.validate/lemma_inventory`, `candidate.validate/span_candidate`, `report.seed_candidate/candidate_seed`
- **cfg_enum** (36): `candidate_decision=candidate`, `candidate_decision=exception`, `candidate_decision=rejected`, `candidate_decision=undecided`, `candidate_ib_referent=body_part`, `candidate_ib_referent=characteristic`, `candidate_ib_referent=other_being`, `candidate_source=curated-synonym`, `candidate_source=ib-judgement`, `candidate_source=read-emergent`, `candidate_source=registry-direct`, `candidate_step_status=in_strong`, `candidate_step_status=not_in_step`, `candidate_step_status=step_has_verses_pending`, `candidate_step_status=step_no_verses`, `escalation_answer=approve`, `escalation_answer=reject`, `escalation_answer=revise`, `escalation_next_action=approve`, `escalation_next_action=approved`, `escalation_next_action=hold`, `escalation_next_action=noted`, `escalation_next_action=ready_for_approval`, `escalation_next_action=reject`, `escalation_next_action=review`, `escalation_next_action=revise`, `escalation_state=answered`, `escalation_state=paused`, `escalation_state=re-assign`, `escalation_state=retracted`, `escalation_type=crash`, `escalation_type=interactive`, `escalation_type=prompted`, `escalation_type=report-stop`, `passage_source=passage-build`, `passage_source=single-verse-emergent`
- **cfg_on_fail** (11): `candidate.curate/change-rejected`, `candidate.curate/invalid-proposal`, `candidate.curate/needs-approval`, `candidate.curate/needs-revision`, `candidate.load/needs-review`, `candidate.seed/no-inventory`, `candidate.set/no-spans`, `candidate.validate/findings-rejected`, `candidate.validate/needs-review`, `candidate.validate/needs-revision`, `passage.build/no-candidates`
- **cfg_candidate_rule** (by kind): accept=289

<a id="2-utilities-registry"></a>
## 2. Utilities registry

**415** registered module(s) — **32** declared `config_exempt` (a legitimate zero for config-setting/enum usage, not a completeness gap), **361** inactive (module removed/merged). See §0 "Low config-density utilities" for any NON-exempt module still flagged.

| module | file | purpose | active | exempt | exempt reason |
| --- | --- | --- | --- | --- | --- |
| add_ps_scripts_dispatch_through_run_py_rule | iba/app/migration/add_ps_scripts_dispatch_through_run_py_rule_20260821.py | One-off migration: escalation #8 -- adds cfg_behaviour_rule (development, every-active-ps-script-dispatches-through-run-py). | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| add_resolution_kind_column | iba/app/migration/add_resolution_kind_column_v1_20260822.py | One-off migration: escalation #798/#799 Stage 2 (schema half) -- adds the resolution_kind column to escalation/escalation_history, closing a gap left by Stage 1's config-only pass. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| anchor_test_plan_governance_rule | iba/app/migration/anchor_test_plan_governance_rule_20260822.py | Anchors the researcher's 2026-08-22 test-plan-per-module/utility instruction in governance (cfg_behaviour_rule + governance.* cfg_setting), escalation #795. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| behaviour | iba/app/lib/behaviour.py | Read-only query/report front end for cfg_behaviour_class/cfg_behaviour_rule (escalations #715/#732/#733) -- writes the live rule set to a report path. Content is written by the bootstrap_behaviour_rules_* migration scripts, never by this module. | ✓ |  |  |
| bootstrap_behaviour_rules | iba/app/migration/bootstrap_behaviour_rules_v1_20260818.py | One-off migration: creates cfg_behaviour_class/cfg_behaviour_rule and seeds cycle-1 ('the obvious ones') content -- GR-DB-001/GR-PROC-001/GR-REF-001/GR-PROG-009 reworded as definitive statements. Escalation #715. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3 (creates + populates them), same class as cfgload.py, already exempted from usage-checks for the same reason. |
| bootstrap_behaviour_rules_cycle2 | iba/app/migration/bootstrap_behaviour_rules_cycle2_v1_20260818.py | One-off migration: escalation #715 cycle 2 -- seeds cfg_behaviour_rule content from the Workflow/Claude_API, Workflow/SQLite, Workflow/Obsidian usage guides (2026-08-15, never previously folded in). Found unregistered during cycle 3's sweep (governance.new_utility_registration_timing gap) and registered retroactively. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| bootstrap_behaviour_rules_cycle3 | iba/app/migration/bootstrap_behaviour_rules_cycle3_v1_20260818.py | One-off migration: escalation #715 cycle 3 -- seeds cfg_behaviour_rule content from docs/interaction-preferences.md, CLAUDE.md sec9, the orphaned wa-operational-governance-v1_0 doc, cfg_escalation.chat_routing (cross-referenced), and confirmed feedback_* memory rules; adds governance.behaviour_boundary.* + governance.procedural_document_taxonomy settings. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| bootstrap_behaviour_rules_cycle4 | iba/app/migration/bootstrap_behaviour_rules_cycle4_v1_20260818.py | One-off migration: escalation #715 cycle 4 -- adds the development behaviour class (escalation #732) after a structural read-through (#733) of cycles 1-3. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| bootstrap_decision_vs_defect_axis | iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py | One-off migration: escalation #798/#799 Stage 1 -- cfg_behaviour_rule 'decision-points-are-terminal-not-inline', cfg_enum resolution_kind, the raise-time requirement, the new cfg_passage module table (with governance registration and 6 rows, replacing 4 cfg_setting.passage.* rows), and raw.zero_strongs_action. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| cfg | iba/app/lib/cfg.py | cfg.py — the runtime config reader. THE ONLY WAY THE APP READS CONFIG. | ✓ | ✓ | defines .setting()/.enum() itself — the config reader; cannot call its own accessor. |
| cfgcheck | iba/app/lib/cfgcheck.py | cfgcheck.py — the config-maintenance / validation utility for the app config. | ✓ | ✓ | validates the raw seed dict before any Cfg/DB object exists — structurally cannot call .setting()/.enum(). |
| cfgload | iba/app/lib/cfgload.py | cfgload.py — load the JSON SEEDS into the config tables in the DATABASE. | ✓ | ✓ | writes the seed INTO the cfg_* tables (creates + populates them) — same class as migration/ scripts, already excluded from usage-checks for the same reason. |
| cfgquality | iba/app/lib/cfgquality.py | cfgquality.py — shared config-quality checks, used by BOTH handlers/configmaint.py (the | ✓ | ✓ | works directly against a raw sqlite3.Connection (not a Cfg wrapper), by design — usable from both configmaint.py (has a Cfg) and cfgreport.py (doesn't); queries cfg_setting/cfg_enum via raw SQL, not Cfg's convenience methods. Found 2026-07-30 only after fixing this same check's own text-collision false negative for this file — same class of legitimate zero as the other 11, not an oversight. |
| cfgreport | iba/app/lib/cfgreport.py | cfgreport.py — full-visibility config report, generated FROM the config store. | ✓ | ✓ | generates reports by querying cfg_* tables directly; the paths it needs (out_path/db_path) are resolved by its caller (configmaint.report), not read here. |
| clear_content_index | iba/app/migration/clear_content_index_20260821.py | One-off migration: escalation #758 -- empties content_index + content_index_scan (the current design judged unsupportable, decommissioned pending redesign #770). | ✓ | ✓ | one-off migration script -- writes directly into content_index/content_index_scan via raw sqlite3, same class as cfgload.py |
| clusterassign | iba/app/lib/clusterassign.py | cluster.assign -- allocates strongs to M-code clusters | ✓ |  |  |
| clusterreport | iba/app/lib/clusterreport.py | report.cluster -- cluster content/quality report | ✓ |  |  |
| contentindex | iba/app/lib/contentindex.py | contentindex.py — file-content concordance search over .md files, keyed on Strong's numbers/glosses/words sourced from strong/word_registry. Round 2 of the manifest + content-search plan; file_manifest (round 1) is its coverage baseline. | ✓ |  |  |
| db | iba/app/lib/db.py | db.py — the DATA layer. Built FROM the config in the database. | ✓ |  |  |
| dbsnapshot | iba/app/lib/dbsnapshot.py | dbsnapshot.py — pre-write DB snapshots. THE GAP FOUND 2026-07-22: this app had no rollback | ✓ |  |  |
| debateaudit | iba/app/lib/debateaudit.py | debateaudit.py — the shared per-row CRUD audit trail for every debate writer (`hib.set`, | ✓ | ✓ | writes to a fixed table name (debate_change_detail) only -- no cfg.setting()/cfg.enum() usage by design, same shape as other pure DB-write utilities already exempt |
| debaterun | iba/app/lib/debaterun.py | Debate-Run.ps1 readiness checks (mirrors each operations-ingest/build-passages handler own gate) + staging-payload path resolution (passage.debate_staging_path_pattern) | ✓ |  |  |
| engine_audit | engine/audit.py | Audit framework -- WR-01 through WR-20, run after all writes. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_audit_word | engine/audit_word.py | AUDIT_WORD mode (v4) -- Pre-A1 through A11, unified new-word + re-audit pipeline. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_backup | engine/backup.py | DB backup management (SG-01, SG-12, SG-13) -- timestamped pre-run backup, abort if it fails. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_cli | engine/engine.py | CLI entry point (python -m engine.engine). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_constants | engine/constants.py | Shared constants. | ✓ | ✓ | values move to cfg_setting instead |
| engine_db | engine/db.py | DB access helpers (wraps analytics/db_client.py). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_flag | engine/flag_engine.py | Derivable flag evaluation (S5/N16/A7). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_gap_fill | engine/gap_fill.py | GAP_FILL mode (S1-S8), superseded by audit_word. |  |  |  |
| engine_meaning_parser | engine/meaning_parser.py | Meaning text parser -> wa_meaning_parsed/_sense/_stem, wa_lsj_parsed. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_migrate | engine/migrate.py | Schema migration runner v2.2->v3.0 (M01-M10). | ✓ | ✓ | one-shot historical, same class as iba/app/migration/* |
| engine_register | engine/register.py | REGISTER subcommand -- new word_registry row. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_report | engine/report.py | Word overview report. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_run_log | engine/run_log.py | engine_run_log/word_run_state write helpers. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_softdelete | engine/softdelete.py | Shared soft-delete cascade helpers (H1-H3, H5). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| engine_span_filter | engine/span_filter.py | STEP masterSearch HTML span filtering (Sec5.2 v4). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| escalation | iba/app/lib/escalation.py | escalation.py -- util.escalation. The authoritative record of open items in the project: errors, issues, and building tasks. All runtime errors are reported in it; both Claude and Researcher record emerging issues, tasks, followups as feedback or to get feedback. It pauses a running process and allows it to resume at resume_point when answered (dispatcher-tied), or tracks a backlog item through raise/update/correction (manual -- correction is error-correction only, escalation #774). Five types (task/issue/notice/run_error/config), each a distinct shape of life -- see USER-GUIDE.md sec4. | ✓ |  |  |
| filingkit | iba/app/lib/filingkit.py | filingkit.py -- the project-wide filing utility: naming-shape, same-day -v{n} versioning, archive-before-overwrite, for any writer. Generalises reportkit.oneoff_path(), which now delegates here. Escalation #863/#971/#992. Calls cfg.setting() directly (governance.oneoff_* fallback defaults) -- not config_exempt, a real call site. | ✓ |  |  |
| fix_dispatcher_answerrun_795 | iba/app/migration/fix_dispatcher_answerrun_795_20260822.py | Escalation #795: split the dispatcher shape's collapsed approve/reject/revise transition into 3 distinct rules, and retargeted cfg_status_flow to match. | ✓ | ✓ | one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same class as cfgload.py |
| fix_from_id_closed_items | iba/app/migration/fix_from_id_closed_items_20260821.py | One-off data repair: escalation #767 v3 -- corrects from_id on 10 closed/completed escalation rows where the correct spawn parent was discoverable from the item's own recorded text; update() cannot touch closed items, so this calls _snapshot() directly. | ✓ | ✓ | one-off migration script -- calls the real escalation._snapshot() mechanism directly, same class as fix_escalation_short_description_and_columns_20260820.py |
| flag_management_build_v1_20260823 | iba/app/migration/flag_management_build_v1_20260823.py | ONE-OFF migration, escalation #833 (Flag Management) -- repurposes wa_quality_flag_types/wa_data_quality_flags for prose-quality checks, adds cfg_column.inactive, retires phase2_flag_types, marks 2 dead columns inactive, records wa_session_research_flags' retention. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| folderpurpose | iba/app/lib/folderpurpose.py | folderpurpose.py -- folder_purpose table: seed/refresh from a live directory scan (Method A), cross-check against cfg_setting *_dir/*_path values (Method B), and hand-edit type/status/usage_description (Method C). Escalation #971. | ✓ |  |  |
| iba_prototype_build_layers | iba/prototype/build_layers.py | build_layers.py — the STEP pull as SEARCH LAYERS, one table per layer. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| iba_prototype_build_prototype | iba/prototype/build_prototype.py | build_prototype.py — test the term -> sense -> span model against real STEP data. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| iba_prototype_export_md | iba/prototype/export_md.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). export_md.py — render the prototype's JSON "tables" as markdown for review. |  |  |  |
| iba_prototype_inspect_verse | iba/prototype/inspect_verse.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). inspect_verse.py — select a verse; watch the backtrack; see what emerges. |  |  |  |
| iba_scripts_build_dbschema | iba/scripts/build_dbschema.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_dbschema.py -- capture a database's schema into its DBSchema register. |  |  |  |
| iba_scripts_cfg_apply | iba/scripts/cfg_apply.py | cfg_apply.py — the configurator-maintenance utility's WRITE PATH. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| iba_scripts_cfg_helper | iba/scripts/cfg_helper.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). cfg_helper.py -- export each config json to a configuration component helper (.md). |  |  |  |
| iba_scripts_cfg_kernel | iba/scripts/cfg_kernel.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). cfg_kernel.py — the envelope-validator KERNEL for the IBA configurator. |  |  |  |
| iba_scripts_probe_step_api | iba/scripts/probe_step_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). probe_step_api.py — dump the FULL raw response of each STEP API, unmodified. |  |  |  |
| lexical | iba/app/lib/lexical.py | lexical.py — the the lexical (`verse_lexical`) engine: T1-T3 of the verse-lexical technique | ✓ |  |  |
| lexiconparse | iba/app/lib/lexiconparse.py | lexiconparse.py — the governed parse of the raw lexicon layer (strong_meaning_tree.sense_text, | ✓ |  |  |
| manifest | iba/app/lib/manifest.py | manifest.py — the project-wide file manifest (rebuild + search). Filename/path metadata only; the baseline lib/contentindex.py (round 2) cross-checks file-content search coverage against. | ✓ |  |  |
| narrativegenerate | iba/app/lib/narrativegenerate.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). report.book_narrative_generate's assembly (debates + governing docs), cost estimate/cap, Anthropic Messages API call, and narrative filing |  |  |  |
| passagedebatereport | iba/app/lib/passagedebatereport.py | passagedebatereport.py — registers the passage-debate method (`WA-passage-read-guidance` + | ✓ |  |  |
| passagetrack | iba/app/lib/passagetrack.py | passagetrack.py — the completion-tracking record for the verse-fanout method (`report. | ✓ | ✓ | receives an already-open cfg/connection from its caller; only checks cfg.may_write(), no settings/enums of its own. |
| pathaudit | iba/app/lib/pathaudit.py | pathaudit.py -- project-wide scan for hardcoded folder/file-path string literals not backed by a live cfg accessor. Escalation #971/#976, the automated successor to the one-off #648 sweep for the location subset specifically. | ✓ | ✓ | legitimate zero, same shape as retention.py/seedreport.py: lib/pathaudit.py takes a pre-opened Cfg object and calls .conn.execute()/normalize_setting_value() directly -- its caller (handlers/pathaudit.py) is the one that calls cfg.setting("pathaudit.report_path", ...); the lib module itself resolves no config of its own. |
| prose_add_edit_rules_build_v1_20260826 | iba/app/migration/prose_add_edit_rules_build_v1_20260826.py | ONE-OFF migration, escalation #890 (Prose add/edit operational rules layer) -- cfg_behaviour_rule (D2, prose_section_type creation gate), prose_section_verse_link table + cfg_table/cfg_column/cfg_write_grant (D4), cfg_step for prose.flag_fix_propose/.flag_fix_apply (D5), cfg_prose.book_stage_map use-text correction (D6, no filtering bug found). D1 (leave prose_section_finding_link's FK as-is), D3 (edit-file delete refusal) are code-only, not this migration. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prose_change_log_build_v1_20260824 | iba/app/migration/prose_change_log_build_v1_20260824.py | ONE-OFF migration, escalation #836 (Prose change log design) -- creates record_change_log, moves prose_section/prose_section_type to Model A (mutate-in-place) versioning, migrates the 91 existing superseded prose_section rows into the log then hard-deletes them, baseline-backfills version pointers for every surviving row, and registers the full cfg_table/cfg_column/cfg_enum/cfg_write_grant/cfg_behaviour_rule content. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prose_first_layer_build_v1_20260824 | iba/app/migration/prose_first_layer_build_v1_20260824.py | ONE-OFF migration, escalation #829 (Prose management IBA first-layer) -- builds cfg_prose, fills/corrects cfg_column use text, cfg_enum (5 groups), cfg_status_flow, cfg_behaviour_rule (3 rows), cfg_write_grant (3 rows), the prose work package + 5 cfg_step rows, reactivates the 4 original scripts. D10 (book_stage_map vs. book_label) deliberately deferred, not built here. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prose_orphan_enum_fix_v1_20260826 | iba/app/migration/prose_orphan_enum_fix_v1_20260826.py | ONE-OFF migration, escalations #896/#900/#901/#902 -- closes the 7 orphan cfg_enum findings per the researcher's own rule: fix the validator for the 4 already-CHECK-enforced groups (cfg_column.expectation wired); fix the code for the 3 genuinely unenforced prose_section_type groups (real CHECK constraints added, then the same expectation wiring). inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| prosestore | iba/app/lib/prosestore.py | The DB-canonical prose store: extract, search, chapter export/import. Escalation #784, 2026-08-21 -- incorporates operations previously standalone in scripts/build_programme_prose_extract.py, scripts/search_prose.py, scripts/export_prose_chapter_edit.py, scripts/import_prose_chapter_edit.py into the app. | ✓ |  |  |
| query_db | query_db.py | prose_section_type joined to active current prose_section rows -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| registryreport | iba/app/lib/registryreport.py | registryreport.py — evaluate/review the `word_registry`: a summary, its join to `strong` (via | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| reportkit | iba/app/lib/reportkit.py | reportkit.py — shared report scaffold (title/ToC/sections/footer) + archive-on-write, reading | ✓ |  |  |
| research_VE_lexical_faculty_map_build_build_batch4 | research/VE-lexical/faculty-map-build/_build_batch4.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). -*- coding: utf-8 -*- |  |  |  |
| research_VE_lexical_faculty_map_build_classify_batch1 | research/VE-lexical/faculty-map-build/_classify_batch1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Faculty classification for inventory slice 0..343. Decisions grounded in gloss+senses, original-language aware. |  |  |  |
| retention | iba/app/lib/retention.py | retention.py — log growth / run-health visibility for the append-only audit tables | ✓ | ✓ | receives cfg.conn from its caller; its own setting (retention.snapshot_keep_count) is read by dbsnapshot.py, not here. |
| retire_from_id_related_activity_v1_20260827 | iba/app/migration/retire_from_id_related_activity_v1_20260827.py | ONE-OFF migration, escalation #909 -- full removal of D14 (from_id) and D15 (related_activity's pairing/graph role): 6 cfg_escalation_requirement rows, 6 cfg_report_section rows, 4 cfg_column rows deleted; from_id/related_activity columns physically dropped from escalation/escalation_history. Researcher decision after two live audits found the mechanism unreliable and unused. inactive=1 once applied -- a one-off, not a reusable routine. |  |  |  |
| schemareport | iba/app/lib/schemareport.py | schemareport.py — the IBA app's own DATA-schema snapshot, one of the four "missing reports" | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| scripts_analytics_bible_analytics | scripts/analytics/bible_analytics.py | bible_analytics.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_db_client | scripts/analytics/db_client.py | db_client.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_morph_util | scripts/analytics/morph_util.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). morph_util.py — canonical morphology-code helpers (STEP / OSHB + Robinson Greek). |  |  |  |
| scripts_analytics_step_client | scripts/analytics/step_client.py | step_client.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_word_export | scripts/analytics/word_export.py | word_export.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_analytics_zotero_client | scripts/analytics/zotero_client.py | zotero_client.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_add_role_to_master_index_v1_20260707 | scripts/_apply_add_role_to_master_index_v1_20260707.py | _apply_add_role_to_master_index_v1_20260707.py — M64: add per-span `role` to the master index |  |  |  |
| scripts_apply_backfill_chapter_verses_v1_20260702 | scripts/_apply_backfill_chapter_verses_v1_20260702.py | _apply_backfill_chapter_verses_v1_20260702.py |  |  |  |
| scripts_apply_backfill_verse_id_active_20260701 | scripts/_apply_backfill_verse_id_active_20260701.py | _apply_backfill_verse_id_active_20260701.py |  |  |  |
| scripts_apply_build_ib_char_index_v1_20260711 | scripts/_apply_build_ib_char_index_v1_20260711.py | (c) Build ib_characteristic into the normalised characteristic index, from the sources |  |  |  |
| scripts_apply_cause_from_api | scripts/_apply_cause_from_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_cause_from_api.py (2026-06-16) — apply the cause-resolution API output back into ve_lexical. |  |  |  |
| scripts_apply_charfix_master_v1_20260711 | scripts/_apply_charfix_master_v1_20260711.py | Fix (a) the emergent-characteristic seed failure + (b) populate the char on the master. |  |  |  |
| scripts_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701 | scripts/_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py | _apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py |  |  |  |
| scripts_apply_cluster_schema_v1_20260505 | scripts/_apply_cluster_schema_v1_20260505.py | _apply_cluster_schema_v1_20260505.py — DB-modifying. |  |  |  |
| scripts_apply_comment_findings_v1_20260602 | scripts/_apply_comment_findings_v1_20260602.py | Applier for COMMENT_EVALUATION outcomes (per cluster). |  |  |  |
| scripts_apply_create_and_populate_passages_20260701 | scripts/_apply_create_and_populate_passages_20260701.py | _apply_create_and_populate_passages_20260701.py |  |  |  |
| scripts_apply_create_constitution_cluster | scripts/_apply_create_constitution_cluster.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_create_constitution_cluster.py — WRITES. Creates the new M47 'Constitution' cluster (the inner-being |  |  |  |
| scripts_apply_create_vc_for_onboarded | scripts/_apply_create_vc_for_onboarded.py | Create verse_context units for engine-onboarded terms (post-onboard catch-up step). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_d6_capture_contributor_source | scripts/_apply_d6_capture_contributor_source.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). D6 — capture a contributor source (Logos / AI-Chat) into prose_section, strip it |  |  |  |
| scripts_apply_descriptions_patch | scripts/_apply_descriptions_patch.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_dq01_locus_coupling_swap_v1_20260714 | scripts/_apply_dq01_locus_coupling_swap_v1_20260714.py | DQ-01 source fix: un-transpose coupling(112) <-> locus(116) for Psalms read-2026 (v1, 2026-07-14). |  |  |  |
| scripts_apply_drop_code_softdelete | scripts/_apply_drop_code_softdelete.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_drop_code_softdelete.py — MODIFIES DB. Soft-delete every finding referencing the §3 DROP tier codes |  |  |  |
| scripts_apply_excluded_registry_cascade | scripts/_apply_excluded_registry_cascade.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_excluded_registry_cascade.py — D1 rule (2026-06-15): when a registry is phase1_status='Excluded', |  |  |  |
| scripts_apply_extend_characteristic_baseline_v1_20260703 | scripts/_apply_extend_characteristic_baseline_v1_20260703.py | Extend the `characteristic` baseline (199 rows, 17 clusters) to the Ps/Pro-raised |  |  |  |
| scripts_apply_faculty_map_rederive_20260624 | scripts/_apply_faculty_map_rederive_20260624.py | Re-found FACULTY on a curated Strong's-lemma->faculty MAP (P2-compliant, replacing |  |  |  |
| scripts_apply_faculty_rederive_v1 | scripts/_apply_faculty_rederive_v1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_faculty_rederive_v1.py (2026-06-15) — re-derive VE7 (faculty) against the actual faculty |  |  |  |
| scripts_apply_field_from_api | scripts/_apply_field_from_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_field_from_api.py (2026-06-16) — apply a field read API output back into ve_lexical. |  |  |  |
| scripts_apply_file_chapter_lexical_prose_v1_20260702 | scripts/_apply_file_chapter_lexical_prose_v1_20260702.py | _apply_file_chapter_lexical_prose_v1_20260702.py |  |  |  |
| scripts_apply_file_passage_lexical_prose_v1_20260704 | scripts/_apply_file_passage_lexical_prose_v1_20260704.py | _apply_file_passage_lexical_prose_v1_20260704.py |  |  |  |
| scripts_apply_file_ruthlessness_lexical_prose_20260702 | scripts/_apply_file_ruthlessness_lexical_prose_20260702.py | _apply_file_ruthlessness_lexical_prose_20260702.py |  |  |  |
| scripts_apply_file_synthesis_prose_v1_20260703 | scripts/_apply_file_synthesis_prose_v1_20260703.py | File a cross-chapter SYNTHESIS document as a DB-canonical prose_section |  |  |  |
| scripts_apply_fix_8_mti_mismatches_percase_20260701 | scripts/_apply_fix_8_mti_mismatches_percase_20260701.py | _apply_fix_8_mti_mismatches_percase_20260701.py |  |  |  |
| scripts_apply_fix_verse_context_mti_mismatch_20260701 | scripts/_apply_fix_verse_context_mti_mismatch_20260701.py | _apply_fix_verse_context_mti_mismatch_20260701.py |  |  |  |
| scripts_apply_flag_empty_to_t2 | scripts/_apply_flag_empty_to_t2.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_flag_empty_to_t2.py — empties FLAG: every remaining FLAG term -> T2 (the catch-all reference bucket; |  |  |  |
| scripts_apply_flag_triage_moves | scripts/_apply_flag_triage_moves.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_flag_triage_moves.py — classify FLAG terms by gloss and move the confident ones: clear characteristic |  |  |  |
| scripts_apply_gate1_term_onboard_v1_20260705 | scripts/_apply_gate1_term_onboard_v1_20260705.py | *** RETIRED 2026-07-12 (researcher direction). DO NOT USE. *** |  |  |  |
| scripts_apply_generate_collection_lexical_20260624 | scripts/_apply_generate_collection_lexical_20260624.py | Collection-lexical GENERATOR (01b Part C, the term-scope layer). |  |  |  |
| scripts_apply_generate_ve_lexical_v2 | scripts/_apply_generate_ve_lexical_v2.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_generate_ve_lexical_v2.py (2026-06-16) — generate the v2 verse-lexical for ALL analysed |  |  |  |
| scripts_apply_generic_characteristic_backfill_20260527 | scripts/_apply_generic_characteristic_backfill_20260527.py | Generic 1:1 characteristic backfill for pre-v2_6 closed clusters. |  |  |  |
| scripts_apply_ib_char_cluster_assign_v1_20260711 | scripts/_apply_ib_char_cluster_assign_v1_20260711.py | Assign each ib_characteristic record (Psalms) to a CLUSTER based on its term. |  |  |  |
| scripts_apply_ib_char_cluster_assign_v2_20260711 | scripts/_apply_ib_char_cluster_assign_v2_20260711.py | Assign CLUSTER via the deterministic chain: master -> its 1 mti_term -> its 1 |  |  |  |
| scripts_apply_ib_char_family_grouping_v1_20260711 | scripts/_apply_ib_char_family_grouping_v1_20260711.py | Group meaning-records (ib_characteristic, a given book_scope) into <=50 semantic |  |  |  |
| scripts_apply_ingest_verse_morphology | scripts/_apply_ingest_verse_morphology.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_ingest_verse_morphology.py (2026-06-16) — populate the persisted MEASURE LAYER (M60). |  |  |  |
| scripts_apply_l2_rollup | scripts/_apply_l2_rollup.py | _apply_l2_rollup.py — roll the VERSE-level L2 findings up to CLUSTER-level findings (the "characteristic = -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_l2_write | scripts/_apply_l2_write.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_l2_write.py — the L2 WRITER (verse-complete). Enters by --cluster (the verses that contain a |  |  |  |
| scripts_apply_l2_write_refit | scripts/_apply_l2_write_refit.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_l2_write_refit.py — L2 writer on the REFIT basis (wa-catalogue-refit-two-layer / verse-extraction |  |  |  |
| scripts_apply_language_reconcile | scripts/_apply_language_reconcile.py | _apply_language_reconcile.py — make mti_terms.language / wa_term_inventory.language -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_lev_study_v1_20260705 | scripts/_apply_lev_study_v1_20260705.py | _apply_lev_study_v1_20260705.py  — Leviticus terminology study loader (corpus-native). |  |  |  |
| scripts_apply_link_mti_term_id | scripts/_apply_link_mti_term_id.py | _apply_link_mti_term_id.py — D2a (2026-06-15): populate the missing wa_verse_records.mti_term_id link -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_load_segmentation_v1_20260703 | scripts/_apply_load_segmentation_v1_20260703.py | Load an inner-being SEGMENTATION (units) into the generic segment store. |  |  |  |
| scripts_apply_locus_dimension_v1_20260704 | scripts/_apply_locus_dimension_v1_20260704.py | Derive a LOCUS dimension (ve_nr 116) on target/bearer spans: IB-internal vs external. |  |  |  |
| scripts_apply_m03_characteristic_backfill_20260527 | scripts/_apply_m03_characteristic_backfill_20260527.py | M03 characteristic backfill (test cluster for pre-v2_6 characteristic retrofit). |  |  |  |
| scripts_apply_m03_findings_capture_20260620 | scripts/_apply_m03_findings_capture_20260620.py | _apply_m03_findings_capture_20260620.py — capture M03 (Grief) findings, in line with M02. |  |  |  |
| scripts_apply_master_index_backfill_v1_20260706 | scripts/_apply_master_index_backfill_v1_20260706.py | Master-index -> wa_verse_records backfill (per book). |  |  |  |
| scripts_apply_merge_m10bc_into_m10_20260623 | scripts/_apply_merge_m10bc_into_m10_20260623.py | Merge M10b + M10c into M10 (researcher decision 2026-06-23): the three-way split |  |  |  |
| scripts_apply_migrate_sb_findings | scripts/_apply_migrate_sb_findings.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_migrate_sb_findings.py — migrate Session B findings (wa_session_b_findings) into the universal |  |  |  |
| scripts_apply_migrate_ve_findings_to_lexical | scripts/_apply_migrate_ve_findings_to_lexical.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_migrate_ve_findings_to_lexical.py (2026-06-15) — retrofit the VE field-value findings OUT of |  |  |  |
| scripts_apply_morph_backfill | scripts/_apply_morph_backfill.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_morph_backfill.py — L0 of the L1 sweep. Populates wa_verse_records.morph_code / stem from STEP |  |  |  |
| scripts_apply_mti_dedup_active_duplicates_v1_20260713 | scripts/_apply_mti_dedup_active_duplicates_v1_20260713.py | Isolate duplicate ACTIVE mti_terms rows — one active row per Strong's (OT-DBR-009). |  |  |  |
| scripts_apply_passage_build_v2_20260713 | scripts/_apply_passage_build_v2_20260713.py | Passage build v2 — candidate-driven, per book (Stage 0 of the cycle). |  |  |  |
| scripts_apply_passage_completeness_v1_20260707 | scripts/_apply_passage_completeness_v1_20260707.py | Passage completeness (reading-unit repair) — per book, reusable. |  |  |  |
| scripts_apply_passage_process_markers_v1_20260701 | scripts/_apply_passage_process_markers_v1_20260701.py | _apply_passage_process_markers_v1_20260701.py |  |  |  |
| scripts_apply_persist_narration_finding_v1 | scripts/_apply_persist_narration_finding_v1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_persist_narration_finding_v1.py (2026-06-15) — persist the templated narration as the single |  |  |  |
| scripts_apply_phase2_flags_patch | scripts/_apply_phase2_flags_patch.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Apply phase2-flag-reassessment-20260319-v1.json |  |  |  |
| scripts_apply_poetic_chapter_lexical_v1_20260702 | scripts/_apply_poetic_chapter_lexical_v1_20260702.py | _apply_poetic_chapter_lexical_v1_20260702.py |  |  |  |
| scripts_apply_prose_programme_chapter01 | scripts/_apply_prose_programme_chapter01.py | _apply_prose_programme_chapter01.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_psalm_role_reassess_v1_20260706 | scripts/_apply_psalm_role_reassess_v1_20260706.py | _apply_psalm_role_reassess_v1_20260706.py — Step 2: re-assess the role dimension for a psalm. |  |  |  |
| scripts_apply_psalms_gate1_completeness_v1_20260706 | scripts/_apply_psalms_gate1_completeness_v1_20260706.py | _apply_psalms_gate1_completeness_v1_20260706.py — Step (d) Gate-1 completeness for PSALMS. |  |  |  |
| scripts_apply_psalms_gate1_reactivate_v1_20260706 | scripts/_apply_psalms_gate1_reactivate_v1_20260706.py | _apply_psalms_gate1_reactivate_v1_20260706.py — finish Step (d) for Psalms. |  |  |  |
| scripts_apply_psalms_linkage_fix_v1_20260706 | scripts/_apply_psalms_linkage_fix_v1_20260706.py | _apply_psalms_linkage_fix_v1_20260706.py — Step 1 (linkages) for PSALMS only. |  |  |  |
| scripts_apply_rebuild_ib_char_meaning_keyed_v3_20260711 | scripts/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py | (v3) Rebuild ib_characteristic keyed on MEANING-IN-CONTEXT, not base lemma. |  |  |  |
| scripts_apply_rebuild_passages_consecutive_v2_20260701 | scripts/_apply_rebuild_passages_consecutive_v2_20260701.py | _apply_rebuild_passages_consecutive_v2_20260701.py |  |  |  |
| scripts_apply_recode_sessionb_m10_findings_20260623 | scripts/_apply_recode_sessionb_m10_findings_20260623.py | Recode mis-migrated session_b CLUSTER-level findings off M10 to their correct |  |  |  |
| scripts_apply_registry_metadata_patch | scripts/_apply_registry_metadata_patch.py | _apply_registry_metadata_patch.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_reread_lexical_v1_20260709 | scripts/_apply_reread_lexical_v1_20260709.py | Apply a char-driven re-read lexical JSON to ve_lexical. REUSABLE per chapter/book. |  |  |  |
| scripts_apply_reread_roles_from_velexical_v1_20260709 | scripts/_apply_reread_roles_from_velexical_v1_20260709.py | _apply_reread_roles_from_velexical_v1_20260709.py |  |  |  |
| scripts_apply_reset_l2_meaning_flags | scripts/_apply_reset_l2_meaning_flags.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_reset_l2_meaning_flags.py — WRITES. Recomputes finding.flagged_for_review for ALL l2_meaning |  |  |  |
| scripts_apply_retrofit_dims_v1_20260714 | scripts/_apply_retrofit_dims_v1_20260714.py | Retrofit-authoring apply for the new/reinstated dimensions (v1, 2026-07-14). |  |  |  |
| scripts_apply_role_reassess_v1_20260707 | scripts/_apply_role_reassess_v1_20260707.py | _apply_role_reassess_v1_20260707.py — Step (c) role reassessment, generalised per book. |  |  |  |
| scripts_apply_ruthlessness_sanitycheck_rerun_v4_20260702 | scripts/_apply_ruthlessness_sanitycheck_rerun_v4_20260702.py | _apply_ruthlessness_sanitycheck_rerun_v4_20260702.py |  |  |  |
| scripts_apply_schema_ve_pairmodel_genre_v1_20260702 | scripts/_apply_schema_ve_pairmodel_genre_v1_20260702.py | _apply_schema_ve_pairmodel_genre_v1_20260702.py |  |  |  |
| scripts_apply_seed_ib_characteristic_registry_v1_20260703 | scripts/_apply_seed_ib_characteristic_registry_v1_20260703.py | Create + seed the inner-being CHARACTERISTIC control registry (ib_characteristic). |  |  |  |
| scripts_apply_sense_from_subgloss | scripts/_apply_sense_from_subgloss.py | _apply_sense_from_subgloss.py (2026-06-15) — set VE1 (sense) in ve_lexical to the PER-OCCURRENCE STEP -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_session_patch | scripts/apply_session_patch.py | apply_session_patch.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_softdelete_excluded_empty_terms | scripts/_apply_softdelete_excluded_empty_terms.py | _apply_softdelete_excluded_empty_terms.py (2026-06-15) — ground the canonical term list: -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_softdelete_orphan_verses | scripts/_apply_softdelete_orphan_verses.py | _apply_softdelete_orphan_verses.py — D2b option A (2026-06-15): soft-delete ACTIVE verses that are -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_stamp_char_candidate_on_master_v1_20260708 | scripts/_apply_stamp_char_candidate_on_master_v1_20260708.py | _apply_stamp_char_candidate_on_master_v1_20260708.py — M65: stamp the candidate-characteristic |  |  |  |
| scripts_apply_stem_patch | scripts/_apply_stem_patch.py | Apply stem-extraction-patch-20260319-v1.json -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_supersede_old_mechanical | scripts/_apply_supersede_old_mechanical.py | _apply_supersede_old_mechanical.py — WRITES (reversible soft-delete). Supersedes the old l2_mechanical -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_t2_soft_delete | scripts/_apply_t2_soft_delete.py | _apply_t2_soft_delete.py — soft-delete Parked (T2) terms that NEVER co-occur with a characteristic. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_term_decisions | scripts/_apply_term_decisions.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_term_decisions.py |  |  |  |
| scripts_apply_term_driven_lexical_ruthlessness_v7_20260702 | scripts/_apply_term_driven_lexical_ruthlessness_v7_20260702.py | _apply_term_driven_lexical_ruthlessness_v7_20260702.py |  |  |  |
| scripts_apply_ve_lexical_phase1_archive_legacy_20260702 | scripts/_apply_ve_lexical_phase1_archive_legacy_20260702.py | _apply_ve_lexical_phase1_archive_legacy_20260702.py  (M63, schema -> 3.37.0) |  |  |  |
| scripts_apply_ve_lexical_span_keyable_v1_20260702 | scripts/_apply_ve_lexical_span_keyable_v1_20260702.py | _apply_ve_lexical_span_keyable_v1_20260702.py |  |  |  |
| scripts_apply_ve_rebuild_mechanical_v1 | scripts/_apply_ve_rebuild_mechanical_v1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_ve_rebuild_mechanical_v1.py (2026-06-15) — mechanical rebuild of ve_lexical fields |  |  |  |
| scripts_apply_verse_read_meaning | scripts/_apply_verse_read_meaning.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _apply_verse_read_meaning.py — L2 VERSE-READ = MEANING pipeline (verse-complete, term-driven). |  |  |  |
| scripts_apply_verse_record_link_repair_all_ot_v1_20260708 | scripts/_apply_verse_record_link_repair_all_ot_v1_20260708.py | Verse-record -> verse / master-index link repair, WHOLE OT in one pass. |  |  |  |
| scripts_apply_verse_record_link_repair_v1_20260707 | scripts/_apply_verse_record_link_repair_v1_20260707.py | Verse-record -> verse / master-index link repair (per book, reusable). |  |  |  |
| scripts_apply_verse_record_structural_backfill_v1_20260705 | scripts/_apply_verse_record_structural_backfill_v1_20260705.py | _apply_verse_record_structural_backfill_v1_20260705.py — safe, determinate structural backfill. |  |  |  |
| scripts_apply_verse_record_traceability_v1_20260704 | scripts/_apply_verse_record_traceability_v1_20260704.py | Add analysis-traceability columns to wa_verse_records (the primary control table). |  |  |  |
| scripts_apply_verse_uniqueness_cleanup | scripts/_apply_verse_uniqueness_cleanup.py | _apply_verse_uniqueness_cleanup.py (2026-06-15) — move wa_verse_records toward "one active row per -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_vr_link_targetword_and_flag_v1_20260708 | scripts/_apply_vr_link_targetword_and_flag_v1_20260708.py | Second-pass verse-record link repair for the multi-span (ambiguous) OT residual. |  |  |  |
| scripts_apply_wipe_ve_lexical_v1 | scripts/_apply_wipe_ve_lexical_v1.py | _apply_wipe_ve_lexical_v1.py (2026-06-15) — PERMANENTLY remove all rows from ve_lexical. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_apply_write_ruthlessness_index_driven_v3_20260702 | scripts/_apply_write_ruthlessness_index_driven_v3_20260702.py | _apply_write_ruthlessness_index_driven_v3_20260702.py |  |  |  |
| scripts_apply_write_ruthlessness_lexical_v1_20260702 | scripts/_apply_write_ruthlessness_lexical_v1_20260702.py | _apply_write_ruthlessness_lexical_v1_20260702.py |  |  |  |
| scripts_apply_write_ruthlessness_passages_full_v2_20260702 | scripts/_apply_write_ruthlessness_passages_full_v2_20260702.py | _apply_write_ruthlessness_passages_full_v2_20260702.py |  |  |  |
| scripts_assess_cluster_profiles | scripts/_assess_cluster_profiles.py | _assess_cluster_profiles.py — READ-ONLY. Per-cluster L1 profile correlated to the co-occurrence matrix: -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_cluster_v3_2_preeval | scripts/_assess_cluster_v3_2_preeval.py | _assess_cluster_v3_2_preeval.py  — READ-ONLY V3_2 cluster pre-evaluation. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_corpus_keyword_map | scripts/_assess_corpus_keyword_map.py | _assess_corpus_keyword_map.py — READ-ONLY. Corpus-wide PRELIMINARY keyword allocation: runs the validated -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_corpus_keyword_typed | scripts/_assess_corpus_keyword_typed.py | _assess_corpus_keyword_typed.py — READ-ONLY. Corpus keyword map v2: each term gets its THING-TYPE -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_cross_cluster_cooccurrence | scripts/_assess_cross_cluster_cooccurrence.py | _assess_cross_cluster_cooccurrence.py — READ-ONLY. The cross-cluster co-occurrence matrix: which -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_keyword_corpus_report | scripts/_assess_keyword_corpus_report.py | _assess_keyword_corpus_report.py — READ-ONLY. Directional assessment of the corpus-wide keyword -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_keyword_overlap | scripts/_assess_keyword_overlap.py | _assess_keyword_overlap.py — READ-ONLY. Cluster-level keyword overlap (angle 5). Builds each cluster's -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_l2_findings_view | scripts/_assess_l2_findings_view.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_l2_findings_view.py — READ-ONLY. For each requested cluster, shows the L1 + L2 results per verse: |  |  |  |
| scripts_assess_l2_triage | scripts/_assess_l2_triage.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_l2_triage.py — READ-ONLY. Runs the L2 MECHANICAL pass + ADEQUACY TRIAGE on every verse of a term: |  |  |  |
| scripts_assess_link_correlation | scripts/_assess_link_correlation.py | _assess_link_correlation.py — READ-ONLY. The correlated roll-up: ties angle 1 (co-occurrence = CONTEXTUAL -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_meaning_tables | scripts/_assess_meaning_tables.py | _assess_meaning_tables.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_mti_duplicate_terms | scripts/_assess_mti_duplicate_terms.py | _assess_mti_duplicate_terms.py — READ-ONLY. Re-surfaces OT-DBR-009 (mti_terms duplication) from the -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_p2_verse_scenarios | scripts/_assess_p2_verse_scenarios.py | _assess_p2_verse_scenarios.py — READ-ONLY. Types every verse of a cluster into the L2 decision-scenario -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_pipeline_integrity_v1_20260704 | scripts/_assess_pipeline_integrity_v1_20260704.py | Read-only PIPELINE-INTEGRITY diagnostic for the verse-analysis (inner-being lexical) chain. |  |  |  |
| scripts_assess_qa_method_effectiveness | scripts/_assess_qa_method_effectiveness.py | _assess_qa_method_effectiveness.py — read-only Q&A coverage extraction. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_qa_method_quality_review | scripts/_assess_qa_method_quality_review.py | _assess_qa_method_quality_review.py — qualitative-review-oriented Q&A coverage. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_read_dedup | scripts/_assess_read_dedup.py | _assess_read_dedup.py — READ-ONLY. Estimates how much the (expensive) read layer would DUPLICATE across -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_registry_grounding | scripts/_assess_registry_grounding.py | _assess_registry_grounding.py — READ-ONLY. Tests the researcher's expectation: does every registry (anchor) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_registry_vs_keywords | scripts/_assess_registry_vs_keywords.py | _assess_registry_vs_keywords.py — READ-ONLY. Diagnoses WHY some of the 214 registry (anchor) words are -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_relationship_probe | scripts/_assess_relationship_probe.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_relationship_probe.py — READ-ONLY. For a cluster PAIR, pull the verses where both co-occur and |  |  |  |
| scripts_assess_shared_forms | scripts/_assess_shared_forms.py | _assess_shared_forms.py — READ-ONLY. Shared-form / homonym index: transliterations whose terms are -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_study_state | scripts/_assess_study_state.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Read-only: render the live state of the verse-lexical study to ONE page (verse-analysis/_STATE.md). |  |  |  |
| scripts_assess_t2_cleanup | scripts/_assess_t2_cleanup.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_t2_cleanup.py  — READ-ONLY. Proposes a disposition for every Parked (T2) cluster term. |  |  |  |
| scripts_assess_t2_relevance_surface | scripts/_assess_t2_relevance_surface.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_t2_relevance_surface.py  — READ-ONLY. |  |  |  |
| scripts_assess_termsense_ranking | scripts/_assess_termsense_ranking.py | _assess_termsense_ranking.py — READ-ONLY. Reasonability check on the read-dedup: ranks every (term, sense) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_verse_assembly | scripts/_assess_verse_assembly.py | _assess_verse_assembly.py — READ-ONLY. L1 establishment per verse for a cluster: assembles each verse's -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_assess_verse_corroboration | scripts/_assess_verse_corroboration.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _assess_verse_corroboration.py  — READ-ONLY (A1 verse-meaning corroboration scan). |  |  |  |
| scripts_assess_verse_raw_data | scripts/_assess_verse_raw_data.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Read-only: assemble the FULL raw study evidence for a verse -> markdown. |  |  |  |
| scripts_audit_cluster_against_instruction_v25_v1_20260518 | scripts/_audit_cluster_against_instruction_v25_v1_20260518.py | Audit a cluster against v2_5 instruction compliance. |  |  |  |
| scripts_audit_cluster_v1_20260601 | scripts/audit_cluster_v1_20260601.py | Consolidated, reusable cluster auditor (read-only). |  |  |  |
| scripts_audit_findings_v1_20260621 | scripts/_audit_findings_v1_20260621.py | _audit_findings_v1_20260621.py — read-only findings audit (wa-findings-audit-spec-v1_0). |  |  |  |
| scripts_audit_gate1_additions_v1_20260706 | scripts/_audit_gate1_additions_v1_20260706.py | Gate-1 onboarding audit — pre/post accountability for the orphan-term additions. |  |  |  |
| scripts_audit_step_extract_archiving | scripts/_audit_step_extract_archiving.py | Auditor + applicator for STEP Extracts archiving. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_backfill_root_families | scripts/backfill_root_families.py | backfill_root_families.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_backfill_span_match | scripts/_backfill_span_match.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _backfill_span_match.py |  |  |  |
| scripts_backup_db_to_nas | scripts/backup_db_to_nas.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). backup_db_to_nas.py — consistent off-Drive backup of bible_research.db to the NAS. |  |  |  |
| scripts_batch_audit | scripts/_batch_audit.py | _batch_audit.py — Run audit_word on all registries that need it. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_batch_extract | scripts/_batch_extract.py | _batch_extract.py — Run STEP extraction for all words that need a discovery JSON. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_M01_verse_read_review | scripts/_build_M01_verse_read_review.py | _build_M01_verse_read_review.py — READ-ONLY. Full M01 verse-complete run review: coverage, cross-cluster -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_cause_api_package | scripts/build_cause_api_package.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_cause_api_package.py (2026-06-16) — Alt 2: prepare a focused, single-purpose API run that does |  |  |  |
| scripts_build_cluster_findings_digest | scripts/build_cluster_findings_digest.py | Read-only: dump a cluster's active findings as a navigable markdown digest. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_cluster_verse_read_gate | scripts/_build_cluster_verse_read_gate.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_cluster_verse_read_gate.py — READ-ONLY. The standard PER-CLUSTER GATE report produced as each |  |  |  |
| scripts_build_complete_extract | scripts/build_complete_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_complete_extract.py |  |  |  |
| scripts_build_corpus_prose | scripts/build_corpus_prose.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_corpus_prose.py — Compile completed word-analysis chapters into a book. |  |  |  |
| scripts_build_correlation_extract | scripts/build_correlation_extract.py | build_correlation_extract.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_dimension_extract | scripts/build_dimension_extract.py | build_dimension_extract.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_field_api_package | scripts/build_field_api_package.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_field_api_package.py (2026-06-16) — Alt 3: prepare a focused, single-instruction API read for ANY |  |  |  |
| scripts_build_file_manifest | archive/scripts/build_file_manifest.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_file_manifest.py — Generates database/file_manifest.json -- RETIRED 2026-08-18 (escalation #730): superseded by iba.db manifest.rebuild/manifest.search (escalation #691, applied 2026-08-15); moved to archive/, database/file_manifest.json moved to database/archive/. |  |  |  |
| scripts_build_file_patterns_extract | scripts/build_file_patterns_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_file_patterns_extract.py — File-name pattern registry extract (M35). |  |  |  |
| scripts_build_flag_classification_package_v1_20260601 | scripts/build_flag_classification_package_v1_20260601.py | Assemble the FLAG-cluster classification package for Claude AI (chat). |  |  |  |
| scripts_build_gate1_registry_final_map_v1_20260706 | scripts/_build_gate1_registry_final_map_v1_20260706.py | Read-only: render the FINAL single-home-per-term registry mapping for the 97 gate1 orphans, |  |  |  |
| scripts_build_label_patterns_extract | scripts/build_label_patterns_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_label_patterns_extract.py — Label pattern registry extract (M35). |  |  |  |
| scripts_build_m01_by_characteristic | scripts/build_m01_by_characteristic.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_m01_by_characteristic.py (2026-06-18) — emit M01 verse-records grouped BY characteristic. |  |  |  |
| scripts_build_m01_findings_oldnew_extract | scripts/build_m01_findings_oldnew_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_m01_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M01 findings: |  |  |  |
| scripts_build_m02_findings_oldnew_extract | scripts/build_m02_findings_oldnew_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_m02_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M02 findings: |  |  |  |
| scripts_build_m04_characteristic_phase9_bundle_20260519 | scripts/_build_m04_characteristic_phase9_bundle_20260519.py | Build a multi-characteristic Phase 9 AI package (bundle). |  |  |  |
| scripts_build_m04_characteristic_phase9_package_20260518 | scripts/_build_m04_characteristic_phase9_package_20260518.py | Build a per-characteristic Phase 9 AI package for M04. |  |  |  |
| scripts_build_m08_characteristic_phase9_bundle_20260521 | scripts/_build_m08_characteristic_phase9_bundle_20260521.py | Build a multi-characteristic Phase 9 AI package (bundle). |  |  |  |
| scripts_build_m08_characteristic_phase9_package_20260521 | scripts/_build_m08_characteristic_phase9_package_20260521.py | Build a per-characteristic Phase 9 AI package for M08. |  |  |  |
| scripts_build_m10_unit_verse_evidence_20260623 | scripts/_build_m10_unit_verse_evidence_20260623.py | Emit the PER-VERSE structured evidence section for an M10 unit, from the on-disk |  |  |  |
| scripts_build_obs_catalogue_export | scripts/build_obs_catalogue_export.py | build_obs_catalogue_export.py — generic Observation Question Catalogue export. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_obs_catalogue_tiered_extract | scripts/build_obs_catalogue_tiered_extract.py | build_obs_catalogue_tiered_extract.py — read-only. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_patch_types_extract | scripts/build_patch_types_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_patch_types_extract.py — Patch type registry extract (M35 scope). |  |  |  |
| scripts_build_programme_prose_extract | scripts/build_programme_prose_extract.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.extract (Prose.ps1 -Step Extract). Kept as the documented CLI entry point (docs/prose-store-architecture.md sec8), reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_build_projection_v2_20260714 | scripts/_build_projection_v2_20260714.py | Build the flattened reading projection + technical data layer for a re-read book (v2, 2026-07-14). |  |  |  |
| scripts_build_ps119 | scripts/_build_ps119.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Persistent char-by-char builder for Ps 119 (641 candidates, 176 verses). |  |  |  |
| scripts_build_reference_snapshot | scripts/build_reference_snapshot.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_reference_snapshot.py — Reference-as-Database snapshot extractor. |  |  |  |
| scripts_build_rules_extract | scripts/build_rules_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_rules_extract.py — Global rules + addenda JSON extract. |  |  |  |
| scripts_build_script_registry | scripts/build_script_registry.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_script_registry.py — canonical, regenerable registry of the project's scripts. |  |  |  |
| scripts_build_session_a_prose | scripts/build_session_a_prose.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Render per-word Session A prose as a self-contained `.md` for Verse Context input. |  |  |  |
| scripts_build_t2_flag_sample | scripts/_build_t2_flag_sample.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_t2_flag_sample.py — READ-ONLY. Shows real verses + meaning paragraphs from the T2 and FLAG buckets, |  |  |  |
| scripts_build_term_verse_findings_report | scripts/_build_term_verse_findings_report.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_term_verse_findings_report.py — READ-ONLY. For N terms, show up to K verses each with the verse |  |  |  |
| scripts_build_tier_catalogue_update_patch_20260619 | scripts/build_tier_catalogue_update_patch_20260619.py | build_tier_catalogue_update_patch_20260619.py — emit the tier-catalogue refit as a reviewable JSON patch. |  |  |  |
| scripts_build_vc_batch | scripts/_build_vc_batch.py | _build_vc_batch.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_build_vc_revision_ledger | scripts/_build_vc_revision_ledger.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Build the VC revision ledger from VCB-7..11 patches. |  |  |  |
| scripts_build_ve_lexical_extract | scripts/build_ve_lexical_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_ve_lexical_extract.py (2026-06-16) — emit a cluster's v2 verse-lexical as JSON for AI Chat. |  |  |  |
| scripts_build_verse_read_pilot_review | scripts/_build_verse_read_pilot_review.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _build_verse_read_pilot_review.py — READ-ONLY. Assembles the M01 verse-read pilot review: |  |  |  |
| scripts_build_vocab_extract | scripts/build_vocab_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_vocab_extract.py — Controlled vocabulary extract (M32 scope). |  |  |  |
| scripts_build_word_relationship_report | scripts/build_word_relationship_report.py | build_word_relationship_report.py — READ-ONLY. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_cc_verse_read | scripts/_cc_verse_read.py | _cc_verse_read.py — CC-GENERATION mode of the verse-read = meaning layer. Same output as the API pipeline -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_book_lexical_readiness_v1_20260712 | scripts/_check_book_lexical_readiness_v1_20260712.py | Book lexical-rework READINESS assessment (read-only). |  |  |  |
| scripts_check_dimension_band_drift_v1_20260714 | scripts/_check_dimension_band_drift_v1_20260714.py | Reader-drift diagnostic for every ve dimension (v1, 2026-07-14). |  |  |  |
| scripts_check_doc_versions | scripts/_check_doc_versions.py | GR-FILE-003 compliance check for instruction documents. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_family_narratives_20260712 | scripts/_check_family_narratives_20260712.py | Verify a family's narrative JSON against its base source WORK_CONTRACT. |  |  |  |
| scripts_check_fi_ti_chain | scripts/_check_fi_ti_chain.py | 1. wa_term_inventory rows with no parent in wa_file_index (orphaned terms) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_ib_char_i7_v1_20260714 | scripts/_check_ib_char_i7_v1_20260714.py | Cheap I7 check (v1, 2026-07-14) — read-2026 characteristics with NO ib_char link. |  |  |  |
| scripts_check_integrity_controls | scripts/_check_integrity_controls.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _check_integrity_controls.py (2026-06-28) — DB integrity anchor for the term-orphan build (READ-ONLY). |  |  |  |
| scripts_check_lexical_content_validity_v1_20260714 | scripts/_check_lexical_content_validity_v1_20260714.py | CONTENT-VALIDITY gate for a re-read book (v1, 2026-07-14). |  |  |  |
| scripts_check_m10_cross_cluster_bonds_20260623 | scripts/_check_m10_cross_cluster_bonds_20260623.py | Cross-cluster BONDS for the M10-family logical units (read-only). |  |  |  |
| scripts_check_mti_terms | scripts/_check_mti_terms.py | Consistency check for mti_terms table. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_passage_reading_coverage_v1_20260704 | scripts/_check_passage_reading_coverage_v1_20260704.py | _check_passage_reading_coverage_v1_20260704.py |  |  |  |
| scripts_check_psalms_reread_progress_v1_20260709 | scripts/_check_psalms_reread_progress_v1_20260709.py | Psalms re-read progress monitor — READ-ONLY. Run anytime to see how far the re-read has got. |  |  |  |
| scripts_check_reread_conformance_v1_20260714 | scripts/_check_reread_conformance_v1_20260714.py | Reusable per-cycle re-read conformance check (v1, 2026-07-14). |  |  |  |
| scripts_check_reread_measures_v3_20260709 | scripts/_check_reread_measures_v3_20260709.py | Re-read success measures (G0-G10) — READ-ONLY, BOOK-GENERAL. v3 (2026-07-09). |  |  |  |
| scripts_check_softdelete_integrity | scripts/_check_softdelete_integrity.py | _check_softdelete_integrity.py — H5 (2026-06-15): the standing soft-delete integrity check, and the -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_ve_seat_completeness | scripts/_check_ve_seat_completeness.py | _check_ve_seat_completeness.py — standing guard: is the location SEAT vocabulary complete? -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_check_ve_signal_lists | scripts/_check_ve_signal_lists.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _check_ve_signal_lists.py — completeness audit of EVERY seed/signal list in the VE engine. |  |  |  |
| scripts_classify_term_introduction_source | scripts/classify_term_introduction_source.py | classify_term_introduction_source.py — Heuristic classifier for M30 backfill. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_combine_cluster_published_to_docx | scripts/combine_cluster_published_to_docx.py | Combine the latest chapter drafts in a cluster's Published/ folder into one .docx. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_cost_ledger | scripts/cost_ledger.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). cost_ledger.py — ONE combined cost ledger across all three Claude surfaces. |  |  |  |
| scripts_db_introspect | scripts/_db_introspect.py | Temporary introspection script — outputs JSON for report generation. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_delete_empty_fi | scripts/_delete_empty_fi.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). fi.id rows to KEEP (backlog words with strongs_list, awaiting new-word import) |  |  |  |
| scripts_derive_retrofit_dims_v1_20260714 | scripts/_derive_retrofit_dims_v1_20260714.py | Derive the 5 retrofit dims (intensity/specifier/effect/device/direction) for read-2026 chars, |  |  |  |
| scripts_discover_word_terms | scripts/_discover_word_terms.py | _discover_word_terms.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_exploratory_brief_meaning_router_v1_20260504 | scripts/_exploratory_brief_meaning_router_v1_20260504.py | _exploratory_brief_meaning_router_v1_20260504.py — read-only. |  |  |  |
| scripts_exploratory_brief_verse_router_v1_20260504 | scripts/_exploratory_brief_verse_router_v1_20260504.py | _exploratory_brief_verse_router_v1_20260504.py — read-only. |  |  |  |
| scripts_exploratory_unclassified_verse_sample_v1_20260504 | scripts/_exploratory_unclassified_verse_sample_v1_20260504.py | _exploratory_unclassified_verse_sample_v1_20260504.py — read-only. |  |  |  |
| scripts_explore_cluster_timing | scripts/_explore_cluster_timing.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_cluster_timing.py — READ-ONLY timing analysis of completed L2 verse-read clusters. |  |  |  |
| scripts_explore_drop_code_findings | scripts/_explore_drop_code_findings.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_drop_code_findings.py — READ-ONLY extract of every finding referencing the §3 DROP tier codes. |  |  |  |
| scripts_explore_m_vs_r_divergence | scripts/_explore_m_vs_r_divergence.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_m_vs_r_divergence.py — READ-ONLY. For VE-01 (obs 395), compare the MECHANICAL term-gloss (M) |  |  |  |
| scripts_explore_tier_findings | scripts/_explore_tier_findings.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_tier_findings.py — READ-ONLY explorer/export for the L2 verse-read tier findings. |  |  |  |
| scripts_explore_ve_by_cluster | scripts/_explore_ve_by_cluster.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _explore_ve_by_cluster.py — READ-ONLY: VE field x cluster x value comparison across clusters. |  |  |  |
| scripts_export_database_schema | scripts/export_database_schema.py | export_database_schema.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_export_md_to_pdf_v1_20260703 | scripts/_export_md_to_pdf_v1_20260703.py | Reusable Markdown -> PDF exporter (reportlab; no external binaries). |  |  |  |
| scripts_export_prose_chapter_edit | scripts/export_prose_chapter_edit.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.export_chapter (Prose.ps1 -Step ExportChapter). Kept as the documented CLI entry point, reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_export_prose_to_md_v1_20260703 | scripts/_export_prose_to_md_v1_20260703.py | Regenerate folder .md documents FROM the DB corpus (prose_section is canonical), |  |  |  |
| scripts_export_tier_catalogue | scripts/export_tier_catalogue.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). export_tier_catalogue.py (2026-06-17) — read-only export of the Tier Catalogue |  |  |  |
| scripts_export_ve_status_reports | scripts/export_ve_status_reports.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). export_ve_status_reports.py (2026-06-17) — two read-only status reports over `ve_lexical`: |  |  |  |
| scripts_export_word_json | scripts/export_word_json.py | export_word_json.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_extract_m10_core_group_20260623 | scripts/_extract_m10_core_group_20260623.py | Mechanical assembly of an M10 CORE reading group from the on-disk corpus |  |  |  |
| scripts_extract_term_data | scripts/extract_term_data.py | extract_term_data.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_cluster_findings_report_v1_20260506 | scripts/_generate_cluster_findings_report_v1_20260506.py | _generate_cluster_findings_report_v1_20260506.py — read-only. |  |  |  |
| scripts_generate_cluster_gate | scripts/_generate_cluster_gate.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _generate_cluster_gate.py  — READ-ONLY per-cluster gate report for the L2 verse-read. |  |  |  |
| scripts_generate_cluster_keyword_analytics_v1_20260523 | scripts/_generate_cluster_keyword_analytics_v1_20260523.py | Generate a cluster-level keyword analytics report from verse_context.keywords. |  |  |  |
| scripts_generate_cluster_overview_v1_20260508 | scripts/_generate_cluster_overview_v1_20260508.py | _generate_cluster_overview_v1_20260508.py — read-only. |  |  |  |
| scripts_generate_cluster_summary_v1_20260603 | scripts/generate_cluster_summary_v1_20260603.py | generate_cluster_summary_v1_20260603.py |  |  |  |
| scripts_generate_cluster_term_report_v1_20260505 | scripts/_generate_cluster_term_report_v1_20260505.py | _generate_cluster_term_report_v1_20260505.py — read-only. |  |  |  |
| scripts_generate_dimension_report | scripts/_generate_dimension_report.py | Generate a dimension index summary report. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_full_cluster_audit_v1_20260603 | scripts/generate_full_cluster_audit_v1_20260603.py | generate_full_cluster_audit_v1_20260603.py  (READ-ONLY) |  |  |  |
| scripts_generate_meaning_quality_check | scripts/_generate_meaning_quality_check.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Read-only quality-check report: N random covered verses per term, showing the |  |  |  |
| scripts_generate_programme_report | scripts/_generate_programme_report.py | Generate a comprehensive programme status report. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_programme_snapshot | scripts/generate_programme_snapshot.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Generate a programme snapshot report. |  |  |  |
| scripts_generate_registry_overview | scripts/generate_registry_overview.py | generate_registry_overview.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_generate_session_a_extract | scripts/generate_session_a_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). generate_session_a_extract.py — Mechanical Session A extract generator. |  |  |  |
| scripts_generate_verse_meanings_export | scripts/_generate_verse_meanings_export.py | Read-only export of verse MEANINGS (l2_meaning paragraphs only) for a cluster. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_harvest_characteristic_evidence_v1_20260703 | scripts/_harvest_characteristic_evidence_v1_20260703.py | Read-only harvest: scan the 150 Psalm Phase-2 readings for the recurring |  |  |  |
| scripts_import_prose_chapter_edit | scripts/import_prose_chapter_edit.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.import_chapter (Prose.ps1 -Step ImportChapter). Kept as the documented CLI entry point, reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_inspect_db_only_terms | scripts/inspect_db_only_terms.py | Detail query for DB_ONLY terms flagged during soul audit. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_inspect_unit_lexical_v1_20260703 | scripts/_inspect_unit_lexical_v1_20260703.py | Read-back inspector: lay a segmentation UNIT's verse text alongside its Phase-1 |  |  |  |
| scripts_integrity_full_check | scripts/_integrity_full_check.py | DB path resolved relative to this script (project moved off Google Drive 2026-06-03; see CLAUDE.md §13) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_keyword_cluster_analysis_v1_20260523 | scripts/_keyword_cluster_analysis_v1_20260523.py | Stage 2 keyword clustering analysis for the discovery pass. |  |  |  |
| scripts_keyword_discovery_subgroup_v1_20260523 | scripts/_keyword_discovery_subgroup_v1_20260523.py | Interim keyword-discovery pass for an under-digested sub-group. |  |  |  |
| scripts_lexical_revelation_test_20260624 | scripts/_lexical_revelation_test_20260624.py | Lexical-Revelation Test (LRT) — runs DURING deep evidence gathering (step 3) to |  |  |  |
| scripts_list_shared_words | scripts/_list_shared_words.py | List all 100%-shared words with their terms and cross-registry links. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_list_tables | scripts/list_tables.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_load_keywords_to_db_v1_20260523 | scripts/_load_keywords_to_db_v1_20260523.py | Load inner-being keywords from discovery JSONs into verse_context.keywords. |  |  |  |
| scripts_onboard_satan_h7854_v1_20260706 | scripts/_onboard_satan_h7854_v1_20260706.py | Force-onboard H7854 (Satan) into the 'spiritual powers' registry (195) as a third-party |  |  |  |
| scripts_patch_report | scripts/_patch_report.py | Apply all corrections and additions to the programme report in one pass. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_populate_dimension_index | scripts/populate_dimension_index.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). populate_dimension_index.py |  |  |  |
| scripts_preflight_m20_dir_005_M20_A_mapping | scripts/_preflight_m20_dir_005_M20_A_mapping.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Pre-flight for DIR-20260513-005 (M20-A mapping apply). |  |  |  |
| scripts_pro_read_lib | scripts/_pro_read_lib.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Compact builder for Proverbs char-driven readings (Stage-4). |  |  |  |
| scripts_probe_gate1_registry_homes_v1_20260706 | scripts/_probe_gate1_registry_homes_v1_20260706.py | Read-only: for each of the 97 gate1 orphan strongs, find its natural registry home. |  |  |  |
| scripts_probe_gate1_span_orphans_v1_20260705 | scripts/_probe_gate1_span_orphans_v1_20260705.py | _probe_gate1_span_orphans_v1_20260705.py  — Gate-1 span-orphan audit (reusable, read-only). |  |  |  |
| scripts_probe_isa43_validation_dump_v1_20260705 | scripts/_probe_isa43_validation_dump_v1_20260705.py | _probe_isa43_validation_dump_v1_20260705.py — full DB dump for Isa 43:1-2 (read-only). |  |  |  |
| scripts_probe_lexical_all14_v8_20260702 | scripts/_probe_lexical_all14_v8_20260702.py | _probe_lexical_all14_v8_20260702.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_all14_v5_20260701 | scripts/_probe_lexical_derivation_all14_v5_20260701.py | _probe_lexical_derivation_all14_v5_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_all14_v6_20260701 | scripts/_probe_lexical_derivation_all14_v6_20260701.py | _probe_lexical_derivation_all14_v6_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_end_to_end_v4_20260701 | scripts/_probe_lexical_derivation_end_to_end_v4_20260701.py | _probe_lexical_derivation_end_to_end_v4_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_lexical_derivation_harness_v1_20260701 | scripts/_probe_lexical_derivation_harness_v1_20260701.py | _probe_lexical_derivation_harness_v1_20260701.py  (READ-ONLY validation harness) |  |  |  |
| scripts_probe_lexical_derivation_harness_v2_passage_20260701 | scripts/_probe_lexical_derivation_harness_v2_passage_20260701.py | _probe_lexical_derivation_harness_v2_passage_20260701.py  (READ-ONLY, PASSAGE-AWARE) |  |  |  |
| scripts_probe_lexical_derivation_harness_v3_startup_20260701 | scripts/_probe_lexical_derivation_harness_v3_startup_20260701.py | _probe_lexical_derivation_harness_v3_startup_20260701.py  (READ-ONLY) |  |  |  |
| scripts_probe_passage_material_v1_20260704 | scripts/_probe_passage_material_v1_20260704.py | Read-only: pull the raw material for one narrative passage (segment_unit) so the |  |  |  |
| scripts_probe_primary_span_prose_reference_v1_20260705 | scripts/_probe_primary_span_prose_reference_v1_20260705.py | _probe_primary_span_prose_reference_v1_20260705.py — per book: primary spans + how many are |  |  |  |
| scripts_probe_psalms_gate1_completeness_v1_20260706 | scripts/_probe_psalms_gate1_completeness_v1_20260706.py | _probe_psalms_gate1_completeness_v1_20260706.py — Step (d) diagnostic (read-only). |  |  |  |
| scripts_probe_psalms_gate1_validate_v1_20260706 | scripts/_probe_psalms_gate1_validate_v1_20260706.py | _probe_psalms_gate1_validate_v1_20260706.py — Step (e) full-integrity validation (read-only). |  |  |  |
| scripts_probe_ve_lexical_per_book_census_v1_20260705 | scripts/_probe_ve_lexical_per_book_census_v1_20260705.py | _probe_ve_lexical_per_book_census_v1_20260705.py — per-book ve_lexical extraction (read-only, DB only). |  |  |  |
| scripts_probe_verse_record_orphan_census_v1_20260705 | scripts/_probe_verse_record_orphan_census_v1_20260705.py | _probe_verse_record_orphan_census_v1_20260705.py — per-book IB span-orphan census (read-only). |  |  |  |
| scripts_produce_family_base_source_json_20260711 | scripts/_produce_family_base_source_json_20260711.py | Produce a JSON BASE SOURCE per family (+ one OUTLIERS file) for Psalms. |  |  |  |
| scripts_produce_family_cluster_comparison_20260711 | scripts/_produce_family_cluster_comparison_20260711.py | Read-only: compare the FAMILY grouping (meaning/keyword-based) with the CLUSTER |  |  |  |
| scripts_produce_family_passage_base_source_v2_20260712 | scripts/_produce_family_passage_base_source_v2_20260712.py | Base source per family — WORK-CONTRACT + PASSAGE-UNIT + RAW-COMPLETE + ANCHORED. |  |  |  |
| scripts_produce_final_extract | scripts/_produce_final_extract.py | _produce_final_extract.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_produce_grain_index_v1_20260702 | scripts/_produce_grain_index_v1_20260702.py | _produce_grain_index_v1_20260702.py  (READ-ONLY) |  |  |  |
| scripts_produce_registry_full_extract | scripts/_produce_registry_full_extract.py | Produce a FULL markdown extract of a single registry word: every term and -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_produce_term_evidence_digest_v1_20260702 | scripts/_produce_term_evidence_digest_v1_20260702.py | _produce_term_evidence_digest_v1_20260702.py  (READ-ONLY) |  |  |  |
| scripts_produce_vc_word_report | scripts/_produce_vc_word_report.py | Produce a Verse Context word report — shows the full classification result -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_produce_ve_narration_v1 | scripts/_produce_ve_narration_v1.py | _produce_ve_narration_v1.py (2026-06-15) — compose the TEMPLATED NARRATION for a term-in-verse -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_prototype_finding_lifecycle | scripts/_prototype_finding_lifecycle.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_finding_lifecycle.py — READ-ONLY prototype of the finding correction cycle. Loads a findings |  |  |  |
| scripts_prototype_l1_mechanical | scripts/_prototype_l1_mechanical.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_l1_mechanical.py  — READ-ONLY L1-mechanical prototype (resolves R2/R4/R6; R7 via --morph). |  |  |  |
| scripts_prototype_l1_morph | scripts/_prototype_l1_morph.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_l1_morph.py  — READ-ONLY R7 morphology pass (STEP + DB). |  |  |  |
| scripts_prototype_meaning_run | scripts/_prototype_meaning_run.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_meaning_run.py — READ-ONLY prototype of the L1 verse-level MEANING RUN. For a term, parses its |  |  |  |
| scripts_prototype_p1_keywords | scripts/_prototype_p1_keywords.py | _prototype_p1_keywords.py — READ-ONLY prototype. Rebuilds the L1 keyword set from a term's STEP meaning -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_prototype_step_morph | scripts/_prototype_step_morph.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _prototype_step_morph.py — READ-ONLY prototype. Pulls STEP preview HTML per verse and extracts the |  |  |  |
| scripts_pull_reread_passage_input_v1_20260714 | scripts/_pull_reread_passage_input_v1_20260714.py | Leaner re-read passage-input pull (v1, 2026-07-14). |  |  |  |
| scripts_pull_verify_batch_v1_20260714 | scripts/_pull_verify_batch_v1_20260714.py | Pull a batch of lexicals for MANUAL source-verification of one dimension (read-only, v1 2026-07-14). |  |  |  |
| scripts_purge_softdeleted_velexical_v1_20260714 | scripts/_purge_softdeleted_velexical_v1_20260714.py | Hard-purge ANCIENT soft-deleted ve_lexical rows to reclaim DB space (v1, 2026-07-14). |  |  |  |
| scripts_query_h2734 | scripts/query_h2734.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_readiness_sweep_pilot | scripts/readiness_sweep_pilot.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Readiness Sweep Pilot — read-only inspection for a single registry. |  |  |  |
| scripts_readiness_sweep_programme_scan | scripts/readiness_sweep_programme_scan.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Programme-wide readiness sweep scan. |  |  |  |
| scripts_realign_meaning_tables | scripts/_realign_meaning_tables.py | _realign_meaning_tables.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_realign_quality_flags | scripts/_realign_quality_flags.py | _realign_quality_flags.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_remediate_cluster_v1_20260602 | scripts/_remediate_cluster_v1_20260602.py | Master cluster-remediation orchestrator (one cluster, packaged). |  |  |  |
| scripts_render_narratives_to_md_20260712 | scripts/_render_narratives_to_md_20260712.py | Render a family's narrative output to readable markdown: each passage, then the |  |  |  |
| scripts_repair_02_zero_padding | scripts/_repair_02_zero_padding.py | Fix 2 — Normalise zero-padded registry IDs in 4 tables. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_repair_03_wa_file_index | scripts/_repair_03_wa_file_index.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 3 — Recreate wa_file_index to register FK to word_registry(id). |  |  |  |
| scripts_repair_05_wa_term_related_words | scripts/_repair_05_wa_term_related_words.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 5 — Recreate wa_term_related_words to register FK to wa_term_inventory(id). |  |  |  |
| scripts_repair_06_wa_term_root_family | scripts/_repair_06_wa_term_root_family.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 6 — Recreate wa_term_root_family to register FK to wa_term_inventory(id). |  |  |  |
| scripts_repair_07_wa_verse_records | scripts/_repair_07_wa_verse_records.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Fix 7 — Recreate wa_verse_records to register FKs to wa_file_index(id) |  |  |  |
| scripts_repair_step_missing_verses_v1_20260713 | scripts/_repair_step_missing_verses_v1_20260713.py | Repair STEP-missing verse-records — morphology-anchored (researcher direction 2026-07-13). |  |  |  |
| scripts_reread_finish_v1_20260709 | scripts/_reread_finish_v1_20260709.py | _reread_finish_v1_20260709.py -- finish one re-read chapter: apply -> gate -> commit -> close -> stamp. |  |  |  |
| scripts_reread_ledger_lib | scripts/_reread_ledger_lib.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Reusable ledger-scaffolding helpers for the corrected-method Psalms reread. |  |  |  |
| scripts_reread_worklist_v1_20260709 | scripts/_reread_worklist_v1_20260709.py | _reread_worklist_v1_20260709.py  --  control table for the isolated-per-chapter re-read loop. |  |  |  |
| scripts_reset_registry_status | scripts/_reset_registry_status.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). One-off: reset word_registry.phase1_status for all 170 'In Progress' words. |  |  |  |
| scripts_reverse_findings_stageC_restrict_20260619 | scripts/_reverse_findings_stageC_restrict_20260619.py | _reverse_findings_stageC_restrict_20260619.py — REVERSE Stage C (un-restrict the OLD findings). |  |  |  |
| scripts_roll_retrofit_v1_20260714 | scripts/_roll_retrofit_v1_20260714.py | Roll the retrofit-dim derivation across a chapter batch: derive -> apply(live) -> READ-BACK (v1, 2026-07-14). |  |  |  |
| scripts_run_cause_api | scripts/_run_cause_api.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _run_cause_api.py (2026-06-16) — run the focused cause-resolution API package and save the output. |  |  |  |
| scripts_run_gate1_onboard_batch_v1_20260706 | scripts/_run_gate1_onboard_batch_v1_20260706.py | Gate-1 orphan onboarding orchestrator (Group C — clean adds to existing/new registries). |  |  |  |
| scripts_run_passa_via_api_v1_20260515 | scripts/_run_passa_via_api_v1_20260515.py | Pass A meaning record via Claude API (cluster-agnostic). |  |  |  |
| scripts_run_proverbs_stage1_onboard_v1_20260712 | scripts/_run_proverbs_stage1_onboard_v1_20260712.py | Proverbs Stage-1 onboarding (registry path) — the 30 candidate terms absent from |  |  |  |
| scripts_run_ve_reads_governed | scripts/_run_ve_reads_governed.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _run_ve_reads_governed.py (2026-06-17) — governed corpus API read for ONE VE field. |  |  |  |
| scripts_schema_dump | scripts/_schema_dump.py | (no module docstring or leading comment found -- needs a manual purpose write-up) -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_search_prose | scripts/search_prose.py | Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, exercised via prose.search (Prose.ps1 -Step Search). Kept as the documented CLI entry point, reactivated (escalation #829). | ✓ | ✓ | Thin CLI wrapper delegating entirely to iba/app/lib/prosestore.py (escalation #784/#829) -- no cfg.setting()/cfg.enum() call site of its own by design, same class as the other already-exempt pass-through scripts. Verified live: no duplicate logic, imports and calls prosestore.run_*() directly. |
| scripts_snapshot_db_v1_20260714 | scripts/_snapshot_db_v1_20260714.py | Cadence-aware DB snapshot + prune helper (v1, 2026-07-14). |  |  |  |
| scripts_term_sharing_spider | scripts/_term_sharing_spider.py | Generate term-sharing spider/network diagram showing pools of connected words. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_tmp_read_cycle2_rest | scripts/_tmp_read_cycle2_rest.py | Build the remaining cycle-2 passage readings (Pro 1:24 - 2:3) via _pro_read_lib. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_tmp_read_cycle3 | scripts/_tmp_read_cycle3.py | Build cycle-3 passage readings (Pro 2:4 - 2:20) via _pro_read_lib. Each in isolation. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_token_cost_history | scripts/token_cost_history.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). token_cost_history.py — an auditable history of token consumption and estimated cost. |  |  |  |
| scripts_update_claude_code_instructions | scripts/_update_claude_code_instructions.py | Update WA-SessionB-ClaudeCode-Instructions.md with all post-v5 changes. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_update_reference_doc | scripts/_update_reference_doc.py | Update WA-Reference-v5.1 to v5.2 with new columns from housekeeping. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_update_registry_guide | scripts/_update_registry_guide.py | Update Registry Management Guide with new fields, queries, and terminology. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_v3_2_l1 | scripts/v3_2_l1.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). v3_2_l1.py  — V3_2 Level 1 (verse establishment) command. |  |  |  |
| scripts_ve_engine_v2 | scripts/_ve_engine_v2.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). _ve_engine_v2.py (2026-06-16) — FIRST working build of the verse-lexical engine per 01b v2. |  |  |  |
| scripts_verify_soul | scripts/verify_soul.py | Quick post-audit verification for soul (registry 182). -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_verse_vertical_pass | scripts/verse_vertical_pass.py | verse_vertical_pass.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |  |  |  |
| scripts_word_full_extract | scripts/word_full_extract.py | CORRUPTED (pasted chat text after the SQL string, confirmed via tokenizer crash) -- escalation #701, never valid since its only commit 2026-03-19 |  |  |  |
| scripts_word_study_extract | scripts/word_study_extract.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). word_study_extract.py |  |  |  |
| seedreport | iba/app/lib/seedreport.py | seedreport.py — analysis of `candidate_seed`, one of the four "missing reports" from | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| spanreport | iba/app/lib/spanreport.py | spanreport.py — analysis of the span layer (`span` + `span_candidate`), one of the four | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| stepapi | iba/app/lib/stepapi.py | stepapi.py — the three STEP calls. Governed by config, fully. | ✓ |  |  |
| strongreconcile | iba/app/lib/strongreconcile.py | strong reconciliation utility | ✓ |  |  |
| strongreport | iba/app/lib/strongreport.py | strongreport.py — analysis of the meaning-parse layer (`strong` + `strong_lexicon` + | ✓ | ✓ | receives cfg.conn from its caller; no settings/enums of its own. |
| strongversereport | iba/app/lib/strongversereport.py | on-demand verse restatement, by ONE Strongs reference -- formalises the G2128/G2127 preview samples | ✓ | ✓ | receives cfg.conn from its caller; the one setting it reads (report.strong_verse_output_dir) belongs to module report, matching registryreport.py precedent |
| valuequality | iba/app/lib/valuequality.py | valuequality.py — the generic column-level VALUE-QUALITY engine. | ✓ |  |  |
| versespanmeaningreport | iba/app/lib/versespanmeaningreport.py | versespanmeaningreport.py — the governed copy of `tools/build_verse_span_meaning_extract.py`'s | ✓ |  |  |
| wholebookread | iba/app/lib/wholebookread.py | wholebookread.py — registers the whole-book-read step (`report.whole_book_read`) as a real | ✓ |  |  |
| word_strong_span_report | iba/app/tools/word_strong_span_report.py | SUPERSEDED 2026-08-09 (own module docstring) -- promoted the same day into a real registered report, WordRegistrySpan-Report.ps1 / report.word_registry_span / lib/wordregistryspanreport.py. Kept for history only, never registered until now (the gap path-audit escalation #971/#976 found: a hardcoded iba/app/db/iba.db default with zero cfg_utility row at all). Registered inactive rather than fixed, since fixing a hardcoded path in dead code is wasted effort -- use the live replacement instead. |  |  |  |
| wordregistryspanreport | iba/app/lib/wordregistryspanreport.py | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). wordregistryspanreport.py — word_registry -> word_strong -> strong -> parse-meaning -> unique |  |  |  |
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
| backup | backup.nas_db_backup_schedule | database/bible_research.db backed up daily 18:00 (Windows scheduled task 'BibleResearch DB Backup to NAS', scripts/backup_db_to_nas.py) to \LSUK-SYNRACK\HomeMedia\bible_study_projects\db_backups\. iba/app/db/iba.db has NO equivalent dedicated backup+alerting script -- see backup.iba_db_gap. |  |
| backup | backup.nas_full_mirror_schedule | whole project folder + memory mirrored daily 18:30 (Windows scheduled task 'BibleResearch Full Mirror to NAS', scripts/mirror_to_nas.ps1, robocopy /MIR) to \LSUK-SYNRACK\HomeMedia\bible_study_projects\mirror\ + claude-backup\ -- this DOES include iba/app/db/iba.db as a side effect of mirroring the whole tree, but with no DB-specific integrity check the way backup_db_to_nas.py gives bible_research.db. |  |
| backup | backup.pre_run_snapshot_policy | a full DB file snapshot (WAL-checkpointed first) is taken automatically before every NEW run (run.py:_ensure_run -> lib/dbsnapshot.snapshot()), never on resume -- this already covers every step in every pipeline; retention.snapshot_keep_count controls how many are kept (oldest pruned first). IBA_NO_SNAPSHOT=1 skips it for a tight loop. |  |
| backup | backup.write_atomicity_guarantee | every DB write happens inside one atomic transaction -- sqlite3 default deferred-transaction isolation, nothing commits until a handler's own single final commit(). A hard kill (power loss, session breakdown, process death) at any point before that commits NOTHING -- the DB file is left exactly as it was before the call started, and re-submitting the identical call is always safe. |  |
| behaviour | behaviour.list_report_path | outputs/configs/behaviour-rules-list.md | output path for Behaviour.ps1 -Action List / python -m iba.app.lib.behaviour list |
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
| configmaint | configmaint.auto_report | True | whether an approved configmaint.propose automatically chains to configmaint.report |
| configmaint | configmaint.csv_export_dir | workflow/schema | folder for the per-cfg_*-table CSV pairing that accompanies CONFIG-REPORT.md (reportkit.write_csv_pairing) -- independently repointable, no longer hardcoded as a sibling of configmaint.report_path |
| configmaint | configmaint.report_path | outputs/configs/CONFIG-REPORT.md | where configmaint.report writes the snapshot |
| content_index | content_index.exclude_size_threshold_bytes | 52428800 | a .md file this size or larger (bytes; default 50MB) is excluded from content_index.rebuild/.refresh by default, unless it matches an active cfg_content_index_size_override pattern |
| content_index | content_index.report_path | outputs/content_index/content-index-rebuild.md | where content_index.rebuild writes its summary report |
| content_index | content_index.size_profile_report_path | outputs/content_index/content-index-size-profile.md | where content_index.size_profile writes its .md-file-size report |
| database | database.bible_research.path | database/bible_research.db | bible_research.db's file path, project-root-relative (aka research_db in prose elsewhere -- that alias isn't repeated here, see governance.project_databases). Structured counterpart, escalation #723. |
| database | database.iba.path | iba/app/db/iba.db | iba.db's file path, project-root-relative -- structured counterpart to governance.project_databases' prose, part of escalation #723's project_database enum + path settings. |
| escalation | escalation.control_objectives | the escalation table manages all open items, irrespective of source or reason -- AI or researcher raise the escalation when discovered or raised, using the escalation module |  |
| escalation | escalation.control_process | escalations are raised, processed, and completed using the escalation utility module |  |
| escalation | escalation.history_report_dir | outputs/escalation |  |
| escalation | escalation.list_report_path | outputs/escalation/escalation-list.md |  |
| governance | governance.User_Guide_scope | The user guide must reflect the latest state of all the tools and details on the use of the tools, geared towards user interaction for the entire project. |  |
| governance | governance.behaviour_boundary.backup_recovery | Backup/recovery and data-durability discipline is classified under the `sqlite` behaviour class (database-interaction discipline), not a separate class -- ensuring a write is replayable/captured is a database-state concern. Content: cfg_behaviour_rule (sqlite, writes-must-be-replayable). | boundary decision -- backup/durability class placement, escalation #715 cycle 3 |
| governance | governance.behaviour_boundary.git_commit | Git/commit discipline is classified under the `terminal` behaviour class (command/script-execution discipline), not a separate class -- committing and pushing is itself a terminal operation with a definable 'done' state. Content: cfg_behaviour_rule (terminal, git-commit-and-push-together). | boundary decision -- git/commit class placement, escalation #715 cycle 3 |
| governance | governance.build_md_on_code_change | any code change under iba/app/** must update iba/app/BUILD.md in the same unit of work — BUILD.md is the build record, not a one-time snapshot | researcher ruling 2026-07-22: BUILD.md/GOVERNANCE.md must stay current, not just be written once |
| governance | governance.config_control | every configuration entry in any cfg_* table is controlled by the cfg.configmaint rules |  |
| governance | governance.confmaint_configs | all the rules that govern the maintenance operations of the configs are set in cfg_* under the configmaint module |  |
| governance | governance.engineering_documentation_folder | iba/docs/ is the designated home for IBA-side engineering/planning documentation (design docs, plans, gap analyses, investigation write-ups) -- procedural_document_taxonomy category (a). Already functioning as this in practice (30+ files); this setting states it as governance rather than leaving it implicit. Main-project-side consolidation of the equivalent scattered content (docs/, research/investigations/, Workflow/methodology/) is a separate, larger, not-yet-decided item, parked alongside escalation #650's filing review -- not resolved here. | boundary/location decision -- engineering documentation folder, escalation #732 cycle 4 |
| governance | governance.escalation.scope | all open items, discovery of anomalies, clarifications and other forms of escalation must be recorded in escalation using escalation rules |  |
| governance | governance.governance_md_on_rule_change | any governance/process rule change must be set in cfg_* first (via configmaint.propose), then GOVERNANCE.md updated to reflect it in the same unit of work -- GOVERNANCE.md documents the config, it never holds a rule the config does not, and the config should hold a record of every change or new rule set via the chat. | researcher ruling 2026-07-22: no rule should exist only in GOVERNANCE.md; the config is the source of truth, GOVERNANCE.md is the overview of it |
| governance | governance.module.config | each operating module must have a config table (or tables) in the cfg_* series to control all aspects of the module's operation |  |
| governance | governance.module_utility_test_plan | From now on, case-by-case as development happens (not retrofitted): every module/utility design must include a test plan covering all its meaningful interaction/parameter/option combinations; the test plan is kept current (updated in the same unit of work whenever the functional component changes); it is RUN after the approved design is built, as a required stage of the existing plan/propose/design -> approve -> build -> approve cycle; and its actual results are included in the build's escalation resolution, not just asserted. Full rationale and origin: cfg_behaviour_rule (development/test-plan-per-module-utility). | Read explicitly every session by init.py's governance-rules printout (Start-Iba.ps1) -- the only real enforcement a process rule like this has. Applies project-wide, not IBA-only, same as governance.operational_behaviour_control. |
| governance | governance.new_utility_registration_timing | Any new script or routine, anywhere in the project, must be registered in cfg_utility (and cfg_step/cfg_write_grant if it writes data) in the same unit of work it is created -- operationalizes governance.scripts_and_routines with a timing rule and a real enforcement check (configmaint.validate: find_unregistered_project_scripts). |  |
| governance | governance.oneoff_report_archive_dir | archive | archive subfolder (relative to governance.oneoff_report_dir) that oneoff_path() moves a superseded one-off report version into before writing the next one -- same shape as write_report/cfg_report.archive_dir, added 2026-08-08 (BUILD.md sec83) once oneoff_path was found to have versioned without ever archiving. |
| governance | governance.oneoff_report_dir | outputs/ | folder for one-off/investigatory reports — read by lib/reportkit.oneoff_path() |
| governance | governance.oneoff_report_format | md | default file extension for one-off reports |
| governance | governance.oneoff_report_naming_pattern | {topic}-{YYYYMMDD}.{format} | filename pattern for one-off reports ({topic}/{YYYYMMDD}/{format} substituted) — same-day collisions get -v2/-v3/... appended by oneoff_path() itself, per the Bible-study side's docs/file-organisation-rules.md §2.3 convention |
| governance | governance.operational_behaviour_control | Project operational behaviour (chat, terminal, sqlite, documentation, llm_output, and any further class identified) is governed by cfg_behaviour_class + cfg_behaviour_rule -- scope is the WHOLE PROJECT, not iba/app/** only (researcher, 2026-08-18). A rule lives in exactly one place: once captured here, its document version is replaced with a pointer, never left standing alongside it. Where a class boundary is unclear, the boundary is defined explicitly as a governance.behaviour_boundary.<topic> setting rather than left implicit. | entry-point anchor for the operational-behaviour cfg layer -- part (a) of escalation #715 |
| governance | governance.past_precedent_investigation_signals_missing_config | If executing an already-registered standard instruction (a cfg_work_package/cfg_step routine) requires FIRST INVESTIGATING HOW IT WAS DONE IN THE PAST -- reading BUILD.md/session-log history, diffing prior/archived output files, or otherwise reverse-engineering a missing step from precedent -- rather than being told directly by a live cfg_step/cfg_setting row what to run and what rules apply, that investigation is itself the signal that a required config/mechanism is MISSING, not a puzzle to solve from precedent. STOP the instruction immediately the moment this is recognised -- do not proceed by reconstructing the missing rule from historical output and presenting it as the standard process. The gap must be closed first: the missing step/setting registered in cfg_* and its code built (governance.build_md_on_code_change/governance.governance_md_on_rule_change both apply), config validated clean, and only then may the original instruction be resubmitted. | researcher ruling 2026-07-30: a live session investigated BUILD.md history and archived output files to infer an undocumented passage.debate_status filled transition (report.passage_debate has no registered mechanism for marking a manually-filled scaffold complete) instead of finding that transition in cfg_step/cfg_setting -- doc/output archaeology substituting for a missing config is exactly the inconsistency pattern blamed for this study lacking repeatable results over its 7-month history |
| governance | governance.primary_responsibility | Claude is responsible for the coding of, and maintenance of the integrity to ensure that all project operations are coded, controlled and maintained in the IBA application. This includes back-filling operations currently outside the application. |  |
| governance | governance.procedural_document_taxonomy | A procedural document (going forward) is exactly one of: (a) planning/investigatory -- plans, explorations, decision docs; (b) config-extract -- generated (not hand-authored) from cfg_* for easier digesting, e.g. CONFIG-REPORT.md, cfg-rules-overview-*; (c) history-of-changes -- BUILD.md-shaped change records, arguably DB/engine-resident rather than a document long-term; (d) guidance/baseline instructions -- GOVERNANCE.md, USER-GUIDE.md, CLAUDE.md-shaped. Researcher's own framing, 2026-08-18 (comments-operational-behaviour-plan). Applying this taxonomy to the full existing document set is not done here -- a follow-on cycle. | the 4-way procedural-document taxonomy named directly by the researcher, escalation #715 cycle 3 -- not yet applied to the existing document set |
| governance | governance.programme_stages | The research programme has three main stages: Base_data (STEP through lexical); Analysis (deriving understanding of the inner being); Publishing (essays and output for the results). Previously referred to as Session A (base data), Session B/D (analytics), Session C (publishing) -- methodologies and processes have changed materially over time across all three. |  |
| governance | governance.project_change_rule | Any change of operations, methodologies or approach must channel through the IBA App. Any operation defined in the past that is not in the IBA app must be migrated to the app. |  |
| governance | governance.project_databases | bible_research.db (aka research_db) lives in database/; iba.db lives in iba/app/db/ -- both paths are project-root-relative |  |
| governance | governance.project_lookups_and_naming_convensions | Project-specific naming in lookups, stages, and terms with specific meaning must be defined in cfg_enum (see cfg_setting naming.*). Terminology must be checked whenever an operation is executed to ensure it is used in accordance with its definition; a missing definition must be escalated. |  |
| governance | governance.project_operations | A project operation is any activity to perform research, development, exploration, investigation, or running scripts related to achieving the project objectives. |  |
| governance | governance.prose_canonical_authority | The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about -- researcher, 2026-08-18. Chapters 0-3 are reviewed and final; chapters 4-6 were realigned 2026-08-27 (escalations #739/#786). cfg_prose_concept points a key project concept (e.g. verse primacy, the inner-being definition) at the prose section that defines it, rather than restating the definition as a separate rule. Chapter-level review status is NOT tracked in cfg_* (cfg_prose_chapter was removed 2026-08-27, escalation #918 -- it was workflow DATA about content state, not a rule, and required the full config-approval cycle for what is an ordinary content edit) -- it lives where content state belongs: prose_section.status (cfg_enum prose_section_status), set per section via Prose.ps1 -Step SetStatus, rolled up per chapter via prose_section_type.chapter_no. A methodology/approach change that touches a concept named in cfg_prose_concept should flag whether the prose needs updating (part (f) -- the flagging MECHANISM is not yet built, this states the principle only). | entry-point anchor for the prose-as-canonical-authority work -- part (a) of escalation #714 |
| governance | governance.redundancy_archiving | One-off reports, scripts, or other artifacts no longer in use or relevant must be archived on a daily basis. |  |
| governance | governance.reports_must_persist | every quality-check or report-producing step must persist its output to a config-defined report path — a terminal print + an escalation row is not sufficient; enforced by lib/cfgquality.find_missing_report_paths, checked in configmaint.validate | the researcher's 2026-07-21 standard: deviations are bugs, not judgement calls — fix, don't ask |
| governance | governance.rules_must_be_config_driven | no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or memory without a referenced cfg_* row recording it as the evidence that the configuration control is in operation. Any deviation discovered requires escalation. On a new instruction, the first thing to establish is that the rules governing the instruction are fully captured and interpreted correctly in the configs -- if not, it requires escalation. | the researchers 2026-07-26 standard, raised after an unconfigured rule (STEP required) was silently violated |
| governance | governance.scope_iba_app | IBA App is the central process control mechanism for all operations in the entire project |  |
| governance | governance.scope_iba_db | The iba_db is the home for all project process control and base data, including all related tables from STEP through Strongs, verses, meaning, and lexicals. It is now primary for all processes and base data; a few analysis tables (debate/passage control) are expected to migrate back to research_db. |  |
| governance | governance.scope_project | the config's scope is the entire project, with all of its parts, not a sub-section of the project |  |
| governance | governance.scope_research_db | The research_db (bible_research.db) is the home for prose and findings with all the related enabling tables. |  |
| governance | governance.scripts_and_routines | All scripts and routines must belong to a module, utility, library, or be a temporary script. Temporary scripts must be prefixed with temp_. |  |
| governance | governance.scripts_ps_dir | iba/app/ps |  |
| governance | governance.scripts_python_dir | iba/app/tools |  |
| governance | governance.session_log_dir | Logs/ | where every SESSION-LOG-*.md narrative work-session record lives -- consolidated 2026-08-17 (escalation #682) from 5 scattered locations (iba/logs/, outputs/session-logs/, Workflow/Sessionlogs/, repo root) into this one, case-insensitive-filesystem-safe existing folder. |
| governance | governance.session_log_required_content | A session log (Logs/SESSION-LOG-*.md) must, at minimum, carry: (1) date and a one-line scope summary of the session; (2) every escalation touched, by id, with its outcome (raised/updated/resolved/rejected) -- not narrative paraphrase, the actual ids; (3) every file or deliverable created or changed, with its path; (4) decisions made, distinguishing which were the researcher's own decision vs a self_correctable fix Claude made and closed directly; (5) open items carried into the next session -- what is left, and for whom; (6) confirmation of the git state this log's own completion triggers (governance.session_log_triggers_commit): branch, commit hash, and that the push succeeded -- not asserted, the actual git status/log output. A log missing any of these is incomplete, not merely terse. | Answers escalation #911 (2026-08-27): the content a session log must carry, previously unstated anywhere in cfg_* or governance prose -- only governance.session_log_dir (where) and governance.session_log_triggers_commit (the commit consequence) existed. Derived from the log's own stated purpose (continuity across sessions) and the existing patch/escalation convention of naming ids and files explicitly rather than narrating them, not from reading prior logs for precedent (governance.past_precedent_investigation_signals_missing_config). |
| governance | governance.session_log_triggers_commit | completing a session log (any SESSION-LOG-*.md) means the full commit-and-push cycle happens in the same unit of work -- stage the real changes, commit with a proper message, push, confirm clean/pushed. See CLAUDE.md section 12. |  |
| governance | governance.table_columns | each column in each table in the project must be listed in cfg_column with a proper use text. This applies to all databases and all tables. Updating a column in any routine must validate the use of the column against this config. Deviation from the rules must be escalated. |  |
| governance | governance.tables | each table in the project must be listed in cfg_table with a proper use text. This applies to all databases. Tables no longer in use must be set as inactive. |  |
| governance | governance.utility.config | each utility must have its own config table in the cfg_* series to control all aspects of the utility |  |
| governance | governance.verse_gap_by_design | Researcher ruling 2026-07-29: a verse missing from iba.db's verse table (no `verse` row for that osisId) is BY DESIGN, not a data-integrity error. Verse-existence is gated on prior term discovery (concordance-driven per-Strong's onboarding, iba/app/handlers/raw.py:verses) -- do not escalate, flag, or attempt to backfill a missing verse as a bug. Full extent measured 2026-07-29: 2,049/31,086 verses (6.59%) missing, concentrated in genealogy/list-heavy books (1Chr 44%, Ezra 40%, Neh 31%, Josh 23%, Num 17%); sample read of the missing verses' actual content judged the risk within tolerance for this study (see iba/app/reports/verse-existence-census-20260729.md). Both report.verse_span_meaning (the base extract) and report.passage_debate note each detectable gap inline (report.verse_gap_note) and skip straight to the next available verse -- the missing verses are not pulled into the study. | researcher ruling 2026-07-29, after measuring the full-Bible extent of the term-discovery verse gap (see project_iba_verse_existence_gated_on_term_discovery memory + iba/app/reports/verse-existence-census-20260729.md) |
| governance | registry.folder_naming_convention | _analytics/Registry per-word subfolders (report.strong_verse_output_dir) must be named {word_registry.id zero-padded 3 digits}_{word, lowercase, spaces as hyphens} -- e.g. 020_compassion. id comes from the LIVE iba.db word_registry table, never bible_research.dbs legacy numbering (the two differ; confirmed live 2026-08-28 while reorganising 27 stale/unnumbered folders and 249 loose files under _analytics/word_registry). | the folder-naming rule for per-word registry output, so it stays config-governed rather than a one-off manual cleanup that can silently drift again |
| governance | report.book_folder_naming_convention | _analytics/Bible_Books subfolders (report.verse_analysis_output_dir and every book-scoped report) must be named EXACTLY as cfg_book_order.book (the OSIS abbreviation verse.osisId itself uses, e.g. Gen, 1Chr, Song) -- never a full book name or a lowercase variant. Confirmed live 2026-08-28: all 66 canonical books present, 35 folders renamed off full-name/lowercase variants to match. | the folder-naming rule for per-book output, keyed to the same book identifier verse references use, so there is no mis-filing risk working with verse references |
| lexicon | lexicon.bracket_pairs | {'(': ')', '[': ']', '{': '}'} | open->close bracket pairs classify_row/strip_bracketed treat as nestable — a gloss that is wholly one bracketed aside (e.g. '(obsolete)') classifies as 'not applicable'. |
| lexicon | lexicon.classify_lookup_max_words | 3 | classify_row: a gloss/description with at most this many space-separated words is 'lookup', more is 'description' — same shape as candidate.tag_max_words's word-count threshold. |
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
| method | method.inner_being_narrative_guidance_path | workflow/instructions/WA-inner-being-narrative-guidance-v1-2026-07-28.md | current version of the inner-being-narrative guidance (the three-channel scope requirement + the required Scope self-check section) — report.book_narrative_validate and any AI writing such a narrative must follow this exact file; bump this setting (not memory) when the guidance revises |
| method | method.interpretation_questions_path | workflow/instructions/WA-interpretation-questions-v1.4-2026-08-02.md | current version of the Q1-Q10 interrogative + Part B guidance of interpretation — the passage-debate scaffold and any AI applying it must follow this exact file |
| method | method.passage_read_guidance_path | workflow/instructions/WA-passage-read-guidance-v1.5-2026-08-02.md | current version of the passage read guidance (steps 1-5 + notes, incl. step 2 note (f)) — the passage-debate scaffold and any AI applying it must follow this exact file; bump this setting (not the debates' memory) when the guidance revises |
| narrative | method.narrative_hard_constraints_path | workflow/instructions/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md | current version of the book-agnostic hard constraints (nothing invented, open threads stay open, no forced unity, plain language, no self-reference) every generated narrative must follow — bump this setting (not memory) when the doc revises |
| narrative | narrative.generate_max_cost | 3.0 | USD cost cap (from the pre-call ESTIMATE) — over this, report.book_narrative_generate refuses outright (cost-cap-exceeded) rather than pausing for approval; raise it deliberately for a book large enough to need it |
| narrative | narrative.generate_max_output_tokens | 16000 | max_tokens on the Messages API call — the ceiling on how long the generated narrative can be |
| narrative | narrative.generate_model | claude-sonnet-5 | the Anthropic model narrative.generate submits the package to |
| narrative | narrative.output_pattern | WA-{book}-inner-being-narrative.md | filename pattern for the generated narrative, written under report.verse_analysis_output_dir/<book_label>/ — same folder its source debates live in |
| narrative | narrative.rate_input_per_million | 3.0 | USD per million input tokens, at narrative.generate_model's current rate — used for both the pre-call estimate and the real post-call cost; edit if the model default changes to a different price tier |
| narrative | narrative.rate_output_per_million | 15.0 | USD per million output tokens, at narrative.generate_model's current rate |
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
| report | report.cluster_path | _analytics/Clusters/cluster.md | where report.cluster persists its output |
| report | report.cluster_stem_prefix_len | 4 | prefix length used as the final grouping key after suffix-stripping, report.cluster's meaning-stemming aid |
| report | report.cluster_stem_suffixes | ['ically', 'iously', 'ously', 'ingly', 'edness', 'fulness', 'tion', 'sion', 'ness', 'ings', 'ing', 'edly', 'ed', 'ly', 'ies', 'es', 's', 'able', 'ible', 'tive', 'ive', 'ful', 'ous', 'al', 'ic'] | one-pass longest-match suffix strip for report.cluster's meaning-stemming grouping aid (grace/gracious/graciously -> one group) |
| report | report.cluster_top_meanings | 10 | how many stem-grouped meaning groups to show per cluster in report.cluster's new summary section |
| report | report.output_dir | _analytics/Registry | where report.word writes its output |
| report | report.output_pattern | report-{word}.md | filename pattern for report.word's output ({word} substituted) |
| report | report.passage_debate_naming_pattern | WA-{book}-{range}-debate.md | filename pattern for report.passage_debate ({book}/{range} substituted); stable scheme — reportkit archives the prior version on regenerate, no -vN-/date in the name itself |
| report | report.registry_path | _analytics/Registry/registry.md |  |
| report | report.sample_verses | 3 | how many sample verses to show the span layer for |
| report | report.schema_overview_path | workflow/schema/schema-overview.md | where report.schema_overview persists its output |
| report | report.seed_candidate_path | research/discovery/seed-candidate.md | where report.seed_candidate persists its output |
| report | report.show_validation | True | show the validation results (util.validation) for the word |
| report | report.show_verse_text | True | show the verse's plain text above its spans |
| report | report.span_analysis_path | research/discovery/span-analysis.md | where report.span_analysis persists its output |
| report | report.span_fields | ['position', 'surface', 'strong_variant', 'morph_code', 'is_particle', 'sense'] | which columns the span table shows |
| report | report.strong_fields | ['stepGloss', 'accentedUnicode', 'stepTransliteration', 'head', 'count', 'verses'] | which columns the L1->L2 strong table shows |
| report | report.strong_meaning_path | research/discovery/strong-meaning.md | where report.strong_meaning persists its output |
| report | report.strong_verse_output_dir | _analytics/Registry | base folder for report.strong_verse output -- one file per word/strong pair, filed under <base>/<word>/ |
| report | report.verse_analysis_output_dir | _analytics/Bible_Books | base folder for report.verse_span_meaning, sub-foldered per book at write time |
| report | report.verse_analysis_output_pattern | {book}-{range}-verse-span-meaning.md | filename pattern for report.verse_span_meaning ({book}/{range} substituted) |
| report | report.verse_gap_note | **Verse gap -- by design.** `{ref}` has no verse row in iba.db (no onboarded term's concordance search ever surfaced it -- see governance.verse_gap_by_design). Not an error; continuing with the next available verse. | inline note both report.verse_span_meaning and report.passage_debate insert into their output wherever a verse is structurally known to be missing from iba.db within the rendered range (lib.versespanmeaningreport.detect_verse_gaps) -- {ref} substituted |
| report | report.verse_lexical_output_pattern | {book}-{range}-verse-lexical.md | filename pattern for report.verse_lexical ({book}/{range} substituted) — reuses report.verse_analysis_output_dir for the base folder, same as report.verse_span_meaning did |
| report | report.version_on_regenerate | True | app-wide: when true, reportkit.write_report never overwrites or archives-and-replaces an existing report -- every write gets a fresh, never-reused filename (stem-v{n}-{date}.ext, n = 1 + the highest existing version for that exact stem). Set false to fall back to the old archive-before-overwrite behaviour. Researcher direction 2026-08-05 (debate-analytic-process-digest, B2/Q6): reports must never be overwritten, and this must be one app-wide setting, not a per-step convention. |
| report | report.whole_book_read_naming_pattern | WA-{book}-whole-book-read.md | filename pattern for report.whole_book_read ({book} substituted); stable scheme — reportkit archives the prior version on regenerate, same convention report.passage_debate_naming_pattern already uses |
| report | report.word_registry_span_output_dir | _analytics/Registry | base folder for report.word_registry_span output — one file per registry word |
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
| table_export | table_export.output_dir | workflow/schema | where table.export writes its CSVs |
| validation | validation.output_dir | outputs/validations | where validation.word/validation.book write their output |
| validation | validation.show_candidate | True | book report: include the candidate (L4b) section |
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

**book-narrative** — runs over `book` · script `iba/app/ps/Book-Narrative.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_generate | iba.app.handlers.narrative:generate | book | live Anthropic API narrative generation -- same handler as the standalone book-narrative-generate work package (kept active for standalone reruns); ordinal 0 of book-narrative, chained with report.book_narrative_validate which runs automatically against this steps own output path once it completes. |
| 1 | report.book_narrative_validate | iba.app.handlers.narrative:validate | none | structural validation of the just-generated narrative file -- same handler as the standalone book-narrative-validate work package (kept active for standalone reruns); ordinal 1 of book-narrative, receives its -Path from ordinal 0s own output automatically via the scripts custom orchestration. |

**book-narrative-generate** — runs over `book` · script `iba/app/ps/BookNarrative-Generate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_generate | iba.app.handlers.narrative:generate | book | assembles every filled report.passage_debate output for a book plus the hard-constraints and three-channel guidance docs, submits the package to the Anthropic Messages API (researcher approval required first, pause-continue on the estimated cost), and files the returned narrative under report.verse_analysis_output_dir/<book_label>/ — see lib/narrativegenerate.py |

**book-narrative-validate** — runs over `none` · script `iba/app/ps/BookNarrative-Validate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.book_narrative_validate | iba.app.handlers.narrative:validate | none | structural presence check on an inner-being narrative file — confirms a '## Scope self-check' section exists and all three required channel labels (non-human<->human, human<->human, physical world<->human) are present with non-empty content; a presence check only, not a judgment of citation quality or content accuracy — see WA-inner-being-narrative-guidance-v1-2026-07-28.md section 4 |

**build-passages** — runs over `book` · script `iba/app/ps/Build-Passages.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | passage.build | iba.app.handlers.passage:build | book | recompute the book's passages from verse_hib (hib-continuity\|maximal); flag >review_over as needs_review. Redefined 2026-08-05 (B4) from the retired candidate-stamp/char-continuity rule -- see debate-analytic-process-digest-20260805.md Step 2. |

**candidate-curation** — runs over `none` · script `iba/app/ps/Candidate-Curate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.curate | iba.app.handlers.candidate:curate | none | single-row, approval-gated correction on candidate_seed (tag or decision) -- adding a brand-new candidate lemma is the existing cfg_candidate_rule accept route via configmaint.propose |
| 1 | candidate.load | iba.app.handlers.candidate:load | none | JSON-batch create/update/validate for candidate_seed -- derives lemma/strong_variant from an input English word (no lemma_key in the input), auto-loads items that pass every config-driven check, writes anything that doesn't as an inspectable decision='exception' row, then revalidates the whole existing seed the same way; one escalation total if unresolved exceptions remain |

**candidate-quality** — runs over `none` · script `iba/app/ps/Candidate-Quality.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.validate | iba.app.handlers.candidate:validate | none | read-only quality check: candidate_tag null/format, lemma_key/strong resolution — one escalation per invocation, standalone (not part of seed/set) |

**chapter-generate** — runs over `book` · script `iba/app/ps/Chapter-Generate.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.verse_span_meaning | iba.app.handlers.reports:verse_span_meaning_report | book | verse:span:meaning base extract -- same handler as the standalone verse-analysis-report work package (kept active for recovery reruns); ordinal 0 of chapter-generate, chained with report.passage_debate as ordinal 1. |
| 1 | report.passage_debate | iba.app.handlers.reports:passage_debate_report | book | passage-debate SCAFFOLD generator -- same handler as the standalone passage-debate-report work package (kept active for recovery reruns); ordinal 1 of chapter-generate. Manual fill-in of the written scaffold happens after this script exits, then PassageDebate-Sync.ps1 (unchanged, separate) is run once -- kept OUT of this chain because re-invoking a chained work package re-runs every ordinal from the top, which would silently overwrite a filled scaffold with a blank one. |

**cluster-assign** — runs over `none` · script `iba/app/ps/Cluster-Assign.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | cluster.assign | iba.app.handlers.cluster:assign | none | DB-wide sweep: lib.strongreconcile.reconcile() per strong — mechanical HIGH-precedent classification + backfill-to-word promotion cascade where warranted. No network beyond what a promotion cascade itself needs (a real STEP verse fetch). |
| 1 | cluster.validate | iba.app.handlers.cluster:validate | none | Read-only DB-wide coverage + exception report: unclassified strongs, backfill non-T2 not yet promoted, and the two named exception shapes (cluster with no word; backfill with an already-active/clustered sibling). Persists a report every run; escalates only if exception findings exist. |

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

**content-index-rebuild** — runs over `none` · script `iba/app/ps/ContentIndex-Rebuild.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | content_index.rebuild | iba.app.handlers.reports:content_index_rebuild | none | full rescan of every .md file in file_manifest — clears and rebuilds content_index + content_index_scan from scratch; see lib/contentindex.py |

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
| 0 | escalation.list | iba.app.handlers.reports:escalation_list | none | every open escalation, with full history inline, grouped by related_activity, plus the D15 exception sections (cycle/dangling/mismatched_pairing/missing_link/incoherent_link) -- see lib/escalation.py:write_list_report |
| 1 | escalation.history | iba.app.handlers.reports:escalation_history | none | deep history for ONE item (-Id), plus its downward chain (from_id children) and every related_activity-named item -- see lib/escalation.py:write_history_report |

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
| 7 | strong.reconcile | iba.app.handlers.raw:reconcile | word | Cluster-classify and, where warranted, promote every one of the word own codes (lib.strongreconcile.reconcile() per code) — runs last, after raw.validate, so verses/spans are already validated before classification. Point (c), backfill-cluster-triage-plan-v3-20260812.md: new-word must complete through verse_lexical for qualifying strongs. |

**operations-ingest** — runs over `book` · script `iba/app/ps/Operations-Ingest.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | hib.set | iba.app.handlers.operations:hib_set | book | Step 1's HIB register for a whole book -- writes hib/hib_referent_option/verse_hib from a JSON payload (-PayloadPath). Clean re-derivation per book (soft-delete existing, insert fresh), same convention passage.build uses for passage. Fails cleanly (unknown-verse/bad-payload) rather than partially writing. |
| 1 | phenomenon.set | iba.app.handlers.operations:phenomenon_set | book | Step 3's phenomena register for one already-tracked passage (needs -Chapters/-Range), from a JSON payload. Clean re-derivation per passage. Sets passage.phenomena_complete_at itself once the register is complete against verse_hib -- the phase gate operation.set checks. Fails cleanly (no-passage/unresolved-reference/bad-payload). |
| 2 | operation.set | iba.app.handlers.operations:operation_set | book | Step 4-5's operations + parties for the same passage, from a JSON payload. REFUSES (phenomena-incomplete) if passage.phenomena_complete_at is still NULL -- the actual code enforcement of WA-interpretation-questions Part B.12 / the debate digest's Step 3 phase gate. Clean re-derivation per phenomenon set. Fails cleanly on any unresolved reference. |
| 3 | closing.set | iba.app.handlers.operations:closing_set | book | Step 7 (digest) / WA-interpretation-questions-v1.4 Part C sections 4-8 for one already-tracked hib-continuity passage -- writes passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note + passage.open_decisions_note from a JSON payload. Refuses (operations-incomplete) until every live phenomenon in the passage has a live operation. Reconciliation-gated per list (BUILD.md ??64 pattern), same as hib.set/phenomenon.set/operation.set. |

**passage-debate-report** — runs over `book` · script `iba/app/ps/PassageDebate-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.passage_debate | iba.app.handlers.reports:passage_debate_report | book | passage-debate scaffold generator — verifies the base verse-span-meaning extract and the current method docs (method.passage_read_guidance_path / method.interpretation_questions_path) exist, resolves output path/naming, and writes a debate-document SKELETON (front-matter, per-verse Observation/Operation/Subject-Source-Target/Interrogative/Decision placeholders, standard closing sections) for the researcher/AI to fill in; does not generate interpretive content itself |

**passage-debate-sync** — runs over `book` · script `iba/app/ps/PassageDebate-Sync.ps1`
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

**raw-backfill** — runs over `book` · script `iba/app/ps/Raw-Backfill.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | raw.backfill_meaning | iba.app.handlers.raw:backfill_meaning | book | for a book (optionally narrowed to one chapter's verse range via -Range C:V-V), find every distinct strong its spans reference that has no `strong` row yet, and pull ONLY the meaning (STEP getInfo -> strong/strong_sense/strong_meaning_tree/strong_lexicon) — not verses. Reuses raw.detail_one() unchanged. Progressive, passage-driven DB coverage growth, not a full-Bible bulk pull. |

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

**seed-candidate-report** — runs over `none` · script `iba/app/ps/SeedCandidate-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.seed_candidate | iba.app.handlers.reports:seed_candidate_report | none | whole-seed candidate_seed analysis — counts by decision/layer/role, tag/lemma distribution, busiest lemmas, open-vs-resolved over time |

**set-candidates** — runs over `book` · script `iba/app/ps/Set-Candidates.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | candidate.seed | iba.app.handlers.candidate:seed | global | refresh candidate_seed over lemma_inventory (independent net + registry-direct + config); recompute registry_match (the double control) |
| 1 | candidate.set | iba.app.handlers.candidate:set | book | stamp span_candidate on the book's spans whose base-strong is a candidate |

**span-analysis-report** — runs over `none` · script `iba/app/ps/SpanAnalysis-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.span_analysis | iba.app.handlers.reports:span_analysis_report | none | span layer coverage per book, confirmed (span) vs candidate (span_candidate) counts, morph-code distribution |

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

**verse-analysis-report** — runs over `book` · script `iba/app/ps/VerseSpanMeaning-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.verse_span_meaning | iba.app.handlers.reports:verse_span_meaning_report | book | verse : span : meaning extract for a book/chapter-range — per-span meaning from all three parse tables (meaning_tree/lsj/mounce), live STEP disambiguation for AMBIGUOUS (sibling-shared-base) spans |

**verse-lexical** — runs over `book` · script `iba/app/ps/VerseLexical.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | lexical.build | iba.app.handlers.lexical:build | book | verse : verse_lexical extract — mechanical T1-T3 engine: for every code in a span's (possibly compound) strong_variant, classifies role (content lexical entry vs. grammatical formative), stem/voice-selects the operative sense from strong_meaning_parsed via morph_code (not the whole six-stem/voice paradigm), and flags — never resolves — the sibling/base-fallback ambiguity case versespanmeaningreport.meaning_for_code already detects. Runs independent of T4-T9/passage_debate. Version-aware: soft-deletes the superseded row and inserts fresh on rewrite, same convention every other iba.db table already uses. Replaces report.verse_span_meaning (retired, see BUILD.md). |
| 1 | report.verse_lexical | iba.app.handlers.reports:lexical_report | book | on-demand MD report, generated from verse_lexical (never an independent write) — EV verse text and the resolved lexical reading placed together, per book/passage range. Requires verse_lexical.build to have already run for this exact range. |

**whole-book-read** — runs over `book` · script `iba/app/ps/WholeBookRead-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.whole_book_read | iba.app.handlers.reports:whole_book_read_report | book | whole-book-read gathering report — for a book whose passage debates are (wholly or partly) filled, pulls every debate_status='filled' passage row in reading order, reads each debate file, extracts its Emergent-questions and Passage-level-linkages sections (tolerant heading match, explicit NOT-FOUND if a file's headings don't match), and lays them out per-passage with an empty Resolution slot for the researcher/AI to fill in; does not decide how any emergent question actually resolves itself |

**word-audit** — runs over `word` · script `iba/app/ps/Word-Audit.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | word.load_json | iba.app.handlers.wordaudit:load_json | word | Load + validate latest Step 1 JSON + structural completeness check (merged from old A2/A3) |
| 1 | word.confirm | iba.app.handlers.wordaudit:confirm | word | Registry display + CONFIRM prompt |
| 2 | word.gap_report | iba.app.handlers.wordaudit:gap_report | word | Build gap report (Term/Related/Verse/VTL streams) |
| 3 | word.gap_display | iba.app.handlers.wordaudit:gap_display | word | Display gap report (+ interactive approve gate) |
| 4 | word.apply_changes | iba.app.handlers.wordaudit:apply_changes | word | Apply changes, one transaction per stream |
| 5 | word.meaning | iba.app.handlers.wordaudit:meaning | word | Meaning handler -- parse + migrate legacy fields |
| 6 | word.flag_reset | iba.app.handlers.wordaudit:flag_reset | word | Quality flag reset (DATA_COVERAGE), re-derive |
| 7 | word.audit_checks | iba.app.handlers.wordaudit:audit_checks | word | WR-01-WR-20 + write word_run_state (PROVISIONAL) |
| 8 | word.registry_close | iba.app.handlers.wordaudit:registry_close | word | Registry + file-index update, last_automation_run='AUDITED' |
| 9 | word.export | iba.app.handlers.wordaudit:export | word | Full-word JSON export |

**word-registry-span-report** — runs over `word` · script `iba/app/ps/WordRegistrySpan-Report.ps1`
| # | step | handler | scope | does |
| --- | --- | --- | --- | --- |
| 0 | report.word_registry_span | iba.app.handlers.reports:word_registry_span_report | word | word_registry : word_strong : strong : strong_meaning_parsed : verse_lexical : span analysis, for one registry word — every linked Strong's with its parse-meaning breakdown and unique surface-span applications (with an example verse) — read-only |

<a id="7-on-fail-condition-path-the-fork-rules"></a>
## 7. on_fail — condition -> path (the fork rules)

**17 of 67 conditions ESCALATE** (pause-continue — the researcher is asked); the rest either stop the run outright (report-stop) or continue with a logged warning (report-continue). Per the researcher's 2026-07-21 rule: any finding that needs a judgement call must be in the first group, not silently in the second or third.

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
| raw.detail | no-vocab | a strong returned no vocab from STEP — missing lexical data, worth a decision, not a silent continue |
| raw.discover | zero-strongs | the word maps to no strongs — a researcher question |
| raw.verses | shortfall | STEP returned fewer rows than its own reported total — the exact class of bug BUILD.md §5 found; must not silently continue |
| registry.create | needs-approval | a new word needs researcher approval |
| report.book_narrative_generate | needs-approval | researcher approval required before the live API call is made |
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
| configmaint.propose | change-rejected | report-stop | the researcher rejected the proposed change |
| configmaint.propose | invalid-proposal | report-stop | the proposed change fails a coherence check — never escalated |
| configmaint.propose | needs-revision | report-stop | the researcher asked for the proposal to be revised (see the comment) and resubmitted |
| configmaint.validate | findings-rejected | report-stop | researcher flagged advisory findings as needing action, not acknowledgement |
| configmaint.validate | invalid | report-stop | the live cfg_* store is incoherent |
| configmaint.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| lexical.build | unreachable | report-stop | STEP is down and step.required_for_runs is true — cannot resolve any content-role code's sense without it. |
| lexicon.related | unreachable | report-stop | STEP is not reachable — lexicon.related cannot fetch relatedNos at all |
| lexicon.validate | findings-rejected | report-stop | researcher flagged lexicon-parse quality findings as needing action |
| lexicon.validate | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
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
| validation.book | findings-rejected | report-stop | researcher flagged the validation findings as needing action, not just acknowledgement |
| validation.book | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |
| validation.word | findings-rejected | report-stop | researcher flagged the validation findings as needing action, not just acknowledgement |
| validation.word | needs-revision | report-stop | researcher asked for more specific investigation (see comment) |

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
| cluster.assign | cluster_strong |
| configmaint.propose | cfg_api, cfg_behaviour_class, cfg_behaviour_rule, cfg_book_order, cfg_candidate_rule, cfg_change_detail, cfg_change_log, cfg_column, cfg_connection, cfg_content_index_exclude, cfg_content_index_size_override, cfg_enum, cfg_escalation, cfg_escalation_requirement, cfg_escalation_transition, cfg_index, cfg_meta, cfg_method_rule, cfg_on_fail, cfg_passage, cfg_prose, cfg_prose_concept, cfg_quality_check, cfg_report, cfg_report_csv_table, cfg_report_section, cfg_setting, cfg_status_flow, cfg_step, cfg_table, cfg_unique, cfg_utility, cfg_work_package, cfg_write_grant |
| escalation | escalation, escalation_history, word_registry |
| hib.set | debate_change_detail, hib, hib_referent_option, verse_hib |
| lexical.build | verse_lexical |
| lexicon.parse | strong_lsj_parsed, strong_meaning_parsed, strong_mounce_parsed |
| lexicon.related | strong_related |
| migration | candidate_seed, cluster, cluster_strong, lemma_inventory, span, word_registry, word_strong |
| operation.set | debate_change_detail, operation, operation_party |
| passage.build | debate_change_detail, passage, verse_passage |
| phenomenon.set | debate_change_detail, passage, phenomenon |
| raw.validate | validation_result |
| raw.write | word_registry |
| registry.create | word_registry |
| report.debate | passage |
| run | escalation, run, validation_result, word_registry |
| strong.reconcile | strong |

<a id="9-status-flow"></a>
## 9. Status flow

| entity | order | status | set_by |
| --- | --- | --- | --- |
| escalation | 0 | raised | initial state at Raise (escalation.raise_/raise_new) |
| escalation | 1 | in-progress | either party directly (Update state=in-progress); OR system: next_action=revise; OR dispatcher-tied answer_for_run decision=revise (escalation #795 fix, 2026-08-22) |
| escalation | 2 | on-hold | either party directly (Update state=on-hold); OR dispatcher-tied answer_for_run decision=hold |
| escalation | 3 | re-assigned | system: next_action_assigned_to changed, no more specific rule matched (Update) |
| escalation | 4 | closed | either party directly (Update state=closed); OR system: next_action=noted (manual) or decision=noted (dispatcher-tied) |
| escalation | 5 | withdraw | party's explicit choice at Update: next_action=reject, state=withdraw; OR: dispatcher-tied answer_for_run decision=reject (escalation #795 fix, 2026-08-22) |
| escalation | 6 | supersede | party's explicit choice at Update: next_action=reject, state=supersede |
| escalation | 7 | completed | system: manual next_action=approved+resolution present; OR: dispatcher-tied answer_for_run decision=approve |
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
_one row per assessed lemma — the over-inclusive Axis-A candidate assessment_ — L4b seed decision (potential, not definite); the lexical stage is the real test. registry_match NULL on a candidate = a candidate MISSING registry word (the double control)
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
| role | TEXT |  | ✓ |  |  | 'content' (independent lexical item) or 'function' (grammatical formative, e.g. Hebrew H9xxx). Classification metadata only -- does NOT gate resolution (corrected 2026-08-05: H9xxx codes DO carry a real stepGloss/strong_meaning_parsed row, an earlier version wrongly skipped resolving them). | migration/bootstrap_span_reading.py |
| status | TEXT |  | ✓ |  |  | 'resolved' (strong row found, sense pulled -- content or function role alike) or 'unregistered' (no strong row yet -- a genuine coverage gap, regardless of role). | migration/bootstrap_span_reading.py |
| resolved_sense | TEXT |  |  |  |  | stem/voice-selected sense text for 'resolved' rows (content or function role alike); NULL only for 'unregistered' rows -- a real gap, not a hedge. | migration/bootstrap_span_reading.py |
| ambiguity_note | TEXT |  |  |  |  | set only when the sibling/base-fallback ambiguity check fires — live senses named, not resolved (T4's job, not this table's) | migration/bootstrap_span_reading.py |
| created_at | TEXT |  | ✓ |  |  | ISO-8601 UTC | migration/bootstrap_span_reading.py |
| deleted | INTEGER |  | ✓ |  |  | version-aware soft-delete — rewriting a (span_id, code_ordinal) inserts a fresh row and flips the superseded row's deleted to 1, same convention as verse/span/strong | migration/bootstrap_span_reading.py |

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
| gloss | TEXT |  |  |  |  | worked-example term list for this cluster (comma-joined gloss(transliteration) pairs) — the associative signal for allocating an unmatched code | migrated:bible_research.db.cluster |
| deleted | INTEGER |  |  |  |  | soft delete |  |

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
| resolution_kind | TEXT |  |  |  |  | per-version snapshot of escalation.resolution_kind at that version. | iba/app/migration/add_resolution_kind_column_v1_20260822.py |

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
_one row per governed folder_ — Reference/data table (like bible_research.db's books, NOT a cfg_* rule table) -- one row per folder in the project tree, seeded from a full census (outputs/folder-census-20260828.csv, 793 folders). Gives the researcher visibility into every live folder's purpose/status and lets folder-classifying code (lib/manifest.py) read a governed source instead of hardcoded prefix rules. Escalation #971, iba/docs/folder-purpose-governance-plan-v5-20260828.md.
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

<a id="11-enums"></a>
## 11. Enums

| enum | values |
| --- | --- |
| candidate_decision | candidate, rejected, undecided, exception |
| candidate_ib_referent | characteristic, other_being, body_part |
| candidate_source | registry-direct, curated-synonym, ib-judgement, read-emergent |
| candidate_step_status | in_strong, step_no_verses, not_in_step, step_has_verses_pending |
| cfg_change_op | insert, update, delete |
| config_module | registry, raw, step, report, candidate, passage, configmaint, validation, governance, retention, notification, table_export, escalation, lexicon, method, narrative, cluster, manifest, backup, content_index, behaviour, database, prose, pathaudit |
| escalation_answer | approve, reject, revise |
| escalation_assignee | Claude, Researcher |
| escalation_next_action | approve, reject, revise, noted, hold, review, ready_for_approval, approved |
| escalation_next_action_dispatcher | approve, reject, revise, hold, noted |
| escalation_next_action_manual | ready_for_approval, approved, reject, revise, noted, review |
| escalation_requirement_check_kind | field_required, not_raised_with_content, exists, not_self, requires_prior_ready_for_approval_if_decision_required |
| escalation_shape | manual, dispatcher |
| escalation_state | raised, answered, re-assign, on-hold, paused, closed, retracted, withdraw, completed, in-progress, supersede, re-assigned |
| escalation_type | prompted, task, interactive, run_error, issue, report-stop, crash, notice, config, note |
| folder_purpose_status | authoritative, mixed, reallocate, stale, deleted |
| folder_purpose_type | archive, operations, results |
| hib_kind | named_individual, unnamed_individual, named_collection, unnamed_collection, implicit_individual, implicit_collection |
| narrative_required_channel | Non-human ↔ human, Human ↔ human, Physical world ↔ human |
| on_fail | report-continue, pause-continue, report-stop, self-heal |
| operation_decision | retain, set_aside, retain_referential, recorded_silence |
| passage_debate_status | scaffold, filled, empty, in-progress, complete |
| passage_source | passage-build, single-verse-emergent |
| project_database | iba, bible_research |
| prose_section_author | claude_ai, claude_code, researcher |
| prose_section_status | draft, in_review, approved, archived |
| prose_section_type_book_label | Programme, Detail design, Findings, Essays |
| prose_section_type_lifecycle_tag | source, v1, v2, v3 |
| prose_section_type_source_stage | programme, session_a, session_b, session_b_phase9, session_c, session_d, synthesis, verse-analysis, findings, essay, contributor |
| record_change_log_change_type | insert, change, delete |
| record_change_log_status | change_proposed, change_applied, declined |
| resolution_kind | decision_required, self_correctable |
| run_state | running, paused, done, failed |
| step_kind | operations, utility |
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
work package `candidate-curation` → `iba/app/ps/Candidate-Curate.ps1` (chained=0)

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
work package `candidate-quality` → `iba/app/ps/Candidate-Quality.ps1` (chained=0)

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
CSV pairing: `cfg_*` (every cfg_* table, one CSV per table — the config store's own verbatim dump)

### `escalation.history`
**Escalation deep history** — output `md` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | item_history | ## #<id> — <short_description> | Item history | ✓ |

### `escalation.list`
**Open escalations** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `escalation-reporting` → `iba/app/ps/Escalation.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | open_items | # Open escalations | Open items | ✓ |
| 6 | recently_resolved | ## Recently resolved (last 15) | Recently resolved | ✓ |
CSV pairing: `escalation` (raw, unprocessed dump of the escalation table itself -- NOT the exception-category findings (those are markdown-only report sections, D4 correction from v4's original, wrong claim that the CSV was the flagged-exception rows).)

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

### `report.book_narrative_generate`
**{book_label} — Inner-Being Narrative** — output `md` · naming `stable` · archived to `archive/` · ToC off · footer: *Generated by `report.book_narrative_generate` from the book's filled passage debates — see `WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` and `WA-inner-being-narrative-guidance-v1-2026-07-28.md` for the governing instructions. Run `BookNarrative-Validate.ps1` against this file next.*
work package `book-narrative` → `iba/app/ps/Book-Narrative.ps1` (chained=1)
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
work package `book-narrative` → `iba/app/ps/Book-Narrative.ps1` (chained=1)
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
CSV pairing: `cluster`; `cluster_strong` (joined to strong.stepGloss/language and cluster.short_name); `strong_without_cluster` (word-origin strong rows with no cluster_strong assignment -- the LLM-allocation target set)

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

### `report.seed_candidate`
**Seed-candidate report** — output `md+csv` · naming `stable` · archived to `archive/` · ToC on
work package `seed-candidate-report` → `iba/app/ps/SeedCandidate-Report.ps1` (chained=0)

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
work package `word-registry-span-report` → `iba/app/ps/WordRegistrySpan-Report.ps1` (chained=0)

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

### `validation.book`
**Base validation report — book '{book}'** — output `md+csv` · naming `dated` · archived to `archive/` · ToC on
work package `reports` → `iba/app/ps/Reports.ps1` (chained=0)

| # | section | heading | toc label | in ToC |
| --- | --- | --- | --- | --- |
| 0 | app_db | ## 1. App & DB | 1. App & DB | ✓ |
| 1 | candidate | ## 3. Candidate (L4b) | 3. Candidate (L4b) | ✓ |
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
