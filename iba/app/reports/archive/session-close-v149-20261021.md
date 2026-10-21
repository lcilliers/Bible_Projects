# Session close (#1875, rebuilt #2173)

> Generated 2026-10-21T11:09:53Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `3cea0e6c-e050-4cb4-9290-4e4885f10990` (CLAUDE_CODE_SESSION_ID); started 2026-10-21T08:55:05Z; window base commit `fdc0baa2e08abe418b2e6e28e855a329a788314a`
- compliance file: `Logs/compliance/COMPLIANCE-20261021-3cea0e6c.md`; session log: `--`
- **open findings: 441**; cleared by disposition: 0


## Contents

- [Summary](#summary)
- [SC1](#sc1-session-and-window)
- [SC2](#sc2-spine-fatal)
- [SC3](#sc3-researchers-words-recorded)
- [SC4](#sc4-open-items-in-the-register)
- [SC5](#sc5-analysis-integrity)
- [SC6](#sc6-rule-compliance)
- [SC8](#sc8-session-log)
- [SC9](#sc9-decisions-reached-their-targets)
- [SC10](#sc10-buildmd-coverage)
- [SC12](#sc12-publish)
- sc15

<a id="summary"></a>
## Summary

441 open finding(s); SC2 6, SC3 1, SC6 68, SC8 1, SC10 365

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

- **OPEN** `SC2:unverified:G0001G`: G0001G: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:G4528H`: G4528H: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:G6094`: G6094: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H0430H`: H0430H: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H1121A`: H1121A: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H5945H`: H5945H: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:e694ab28`: researcher message 2026-10-21T09:42 is in no escalation comment written this session: "2188 - pause this work until the study is restarted and the narration can be aligned between the rules. 2191  Prose store - architecture document is superceded "

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

_no finding_

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 46.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.behaviour_boundary.git_commit`: engaged, with no evidence
- **OPEN** `SC6:G:governance.config_control`: engaged, with no evidence
- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.no_direct_github_publish`: engaged, with no evidence
- **OPEN** `SC6:G:governance.operational_behaviour_control`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
- **OPEN** `SC6:G:governance.primary_responsibility`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_databases`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_operations`: engaged, with no evidence
- **OPEN** `SC6:G:governance.redundancy_archiving`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_iba_app`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_iba_db`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_project`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scripts_and_routines`: engaged, with no evidence
- **OPEN** `SC6:G:governance.session_log_dir`: engaged, with no evidence
- **OPEN** `SC6:G:governance.session_log_required_content`: engaged, with no evidence
- **OPEN** `SC6:G:governance.session_log_triggers_commit`: engaged, with no evidence
- **OPEN** `SC6:G:governance.study_status`: engaged, with no evidence
- **OPEN** `SC6:B:2`: engaged, with no evidence
- **OPEN** `SC6:B:3`: engaged, with no evidence
- **OPEN** `SC6:B:4`: engaged, with no evidence
- **OPEN** `SC6:B:10`: engaged, with no evidence
- **OPEN** `SC6:B:11`: engaged, with no evidence
- **OPEN** `SC6:B:13`: engaged, with no evidence
- **OPEN** `SC6:B:16`: engaged, with no evidence
- **OPEN** `SC6:B:19`: engaged, with no evidence
- **OPEN** `SC6:B:20`: engaged, with no evidence
- **OPEN** `SC6:B:22`: engaged, with no evidence
- **OPEN** `SC6:B:23`: engaged, with no evidence
- **OPEN** `SC6:B:24`: engaged, with no evidence
- **OPEN** `SC6:B:25`: engaged, with no evidence
- **OPEN** `SC6:B:27`: engaged, with no evidence
- **OPEN** `SC6:B:28`: engaged, with no evidence
- **OPEN** `SC6:B:31`: engaged, with no evidence
- **OPEN** `SC6:B:32`: engaged, with no evidence
- **OPEN** `SC6:B:33`: engaged, with no evidence
- **OPEN** `SC6:B:34`: engaged, with no evidence
- **OPEN** `SC6:B:36`: engaged, with no evidence
- **OPEN** `SC6:B:44`: engaged, with no evidence
- **OPEN** `SC6:B:45`: engaged, with no evidence
- **OPEN** `SC6:B:51`: engaged, with no evidence
- **OPEN** `SC6:B:56`: engaged, with no evidence
- **OPEN** `SC6:B:57`: engaged, with no evidence
- **OPEN** `SC6:B:58`: engaged, with no evidence
- **OPEN** `SC6:B:59`: engaged, with no evidence
- **OPEN** `SC6:B:60`: engaged, with no evidence
- **OPEN** `SC6:B:62`: evidence does not check: file iba/app/migration/register_20261021_migrations_v1_20261021.py does not exist
- **OPEN** `SC6:B:63`: engaged, with no evidence
- **OPEN** `SC6:B:67`: engaged, with no evidence
- **OPEN** `SC6:B:80`: engaged, with no evidence
- **OPEN** `SC6:B:82`: engaged, with no evidence
- **OPEN** `SC6:B:83`: engaged, with no evidence
- **OPEN** `SC6:B:99`: engaged, with no evidence
- **OPEN** `SC6:B:100`: engaged, with no evidence
- **OPEN** `SC6:B:101`: engaged, with no evidence
- **OPEN** `SC6:B:102`: engaged, with no evidence
- **OPEN** `SC6:B:103`: engaged, with no evidence
- **OPEN** `SC6:B:108`: engaged, with no evidence
- **OPEN** `SC6:E:1`: engaged, with no evidence
- **OPEN** `SC6:E:2`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:7`: engaged, with no evidence
- **OPEN** `SC6:E:12`: engaged, with no evidence
- **OPEN** `SC6:E:15`: engaged, with no evidence
- **OPEN** `SC6:E:16`: engaged, with no evidence
- **OPEN** `SC6:E:17`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (3cea0e6c-e050-4cb4-9290-4e4885f10990); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:.claude/hooks/gate_developer_mode_entry.py`: `.claude/hooks/gate_developer_mode_entry.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:.claude/hooks/session_boundary_track.py`: `.claude/hooks/session_boundary_track.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:.claude/hooks/stop_check_escalation_backlog.py`: `.claude/hooks/stop_check_escalation_backlog.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:.claude/hooks/track_prompt_submit.py`: `.claude/hooks/track_prompt_submit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/archive/candidate.py`: `iba/app/handlers/archive/candidate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/cluster.py`: `iba/app/handlers/cluster.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/compliance.py`: `iba/app/handlers/compliance.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/configmaint.py`: `iba/app/handlers/configmaint.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/lexical.py`: `iba/app/handlers/lexical.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/lexicon.py`: `iba/app/handlers/lexicon.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/narrative.py`: `iba/app/handlers/narrative.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/narrativeregister.py`: `iba/app/handlers/narrativeregister.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/observationenhancer.py`: `iba/app/handlers/observationenhancer.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/operations.py`: `iba/app/handlers/operations.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/passage.py`: `iba/app/handlers/passage.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/prose.py`: `iba/app/handlers/prose.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/purge.py`: `iba/app/handlers/purge.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/raw.py`: `iba/app/handlers/raw.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/registry.py`: `iba/app/handlers/registry.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/reports.py`: `iba/app/handlers/reports.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/session_close.py`: `iba/app/handlers/session_close.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/spine.py`: `iba/app/handlers/spine.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/wordaudit.py`: `iba/app/handlers/wordaudit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/batchcontrol.py`: `iba/app/lib/batchcontrol.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/batchprogressreport.py`: `iba/app/lib/batchprogressreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/behaviour.py`: `iba/app/lib/behaviour.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cataloguereport.py`: `iba/app/lib/cataloguereport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cataloguewrite.py`: `iba/app/lib/cataloguewrite.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cfg.py`: `iba/app/lib/cfg.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cfgload.py`: `iba/app/lib/cfgload.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cfgquality.py`: `iba/app/lib/cfgquality.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cfgreport.py`: `iba/app/lib/cfgreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/charanswergenerate.py`: `iba/app/lib/charanswergenerate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/charreadinggenerate.py`: `iba/app/lib/charreadinggenerate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/clusterassign.py`: `iba/app/lib/clusterassign.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/clusterreport.py`: `iba/app/lib/clusterreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/clusterstatus.py`: `iba/app/lib/clusterstatus.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/compliance.py`: `iba/app/lib/compliance.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/contentindex.py`: `iba/app/lib/contentindex.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/db.py`: `iba/app/lib/db.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/debateaudit.py`: `iba/app/lib/debateaudit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/debaterun.py`: `iba/app/lib/debaterun.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/escalation.py`: `iba/app/lib/escalation.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/escalationcontext.py`: `iba/app/lib/escalationcontext.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/filingkit.py`: `iba/app/lib/filingkit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/folderpurpose.py`: `iba/app/lib/folderpurpose.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexical.py`: `iba/app/lib/lexical.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexicalenrich.py`: `iba/app/lib/lexicalenrich.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexicalenrichgenerate.py`: `iba/app/lib/lexicalenrichgenerate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexicalscope.py`: `iba/app/lib/lexicalscope.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexiconparse.py`: `iba/app/lib/lexiconparse.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/manifest.py`: `iba/app/lib/manifest.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/narrativecopy.py`: `iba/app/lib/narrativecopy.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/narrativegenerate.py`: `iba/app/lib/narrativegenerate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/narrativeregister.py`: `iba/app/lib/narrativeregister.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/passagedebatereport.py`: `iba/app/lib/passagedebatereport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/passagetrack.py`: `iba/app/lib/passagetrack.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/pathaudit.py`: `iba/app/lib/pathaudit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/quotecheck.py`: `iba/app/lib/quotecheck.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/recordingpass.py`: `iba/app/lib/recordingpass.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/registryreport.py`: `iba/app/lib/registryreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/reportkit.py`: `iba/app/lib/reportkit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/retention.py`: `iba/app/lib/retention.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/schemareport.py`: `iba/app/lib/schemareport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/seedreport.py`: `iba/app/lib/seedreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/sessionwindow.py`: `iba/app/lib/sessionwindow.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/stage1coverage.py`: `iba/app/lib/stage1coverage.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/stepapi.py`: `iba/app/lib/stepapi.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/strongreconcile.py`: `iba/app/lib/strongreconcile.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/strongreport.py`: `iba/app/lib/strongreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/strongversereport.py`: `iba/app/lib/strongversereport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/subgroupgenerate.py`: `iba/app/lib/subgroupgenerate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/taggingguidance.py`: `iba/app/lib/taggingguidance.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/threadaudit.py`: `iba/app/lib/threadaudit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/valuequality.py`: `iba/app/lib/valuequality.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/versemeta.py`: `iba/app/lib/versemeta.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/versereadinggenerate.py`: `iba/app/lib/versereadinggenerate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/versespanmeaningreport.py`: `iba/app/lib/versespanmeaningreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/wholebookread.py`: `iba/app/lib/wholebookread.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/wordregistryspanreport.py`: `iba/app/lib/wordregistryspanreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/words.py`: `iba/app/lib/words.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/Import-LegacyRegistry.ps1`: `iba/app/migration/archive/Import-LegacyRegistry.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_adversarial_cluster_v1_20260905.py`: `iba/app/migration/archive/add_adversarial_cluster_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_candidate_seed_referent_columns.py`: `iba/app/migration/archive/add_candidate_seed_referent_columns.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_candidate_seed_strong_variant.py`: `iba/app/migration/archive/add_candidate_seed_strong_variant.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_table_category_column_20260831.py`: `iba/app/migration/archive/add_cfg_table_category_column_20260831.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_table_database_column.py`: `iba/app/migration/archive/add_cfg_table_database_column.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_table_inactive_column.py`: `iba/app/migration/archive/add_cfg_table_inactive_column.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_table_purpose_and_success_columns_20260830.py`: `iba/app/migration/archive/add_cfg_table_purpose_and_success_columns_20260830.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_table_purpose_review_20260830.py`: `iba/app/migration/archive/add_cfg_table_purpose_review_20260830.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_unique_database_column_v1_20260818.py`: `iba/app/migration/archive/add_cfg_unique_database_column_v1_20260818.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_utility_config_exempt.py`: `iba/app/migration/archive/add_cfg_utility_config_exempt.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_cfg_write_grant_database_column.py`: `iba/app/migration/archive/add_cfg_write_grant_database_column.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_concise_verse_specific_rule_v1_20260921.py`: `iba/app/migration/archive/add_concise_verse_specific_rule_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_debate_change_detail_writer_column_20260808.py`: `iba/app/migration/archive/add_debate_change_detail_writer_column_20260808.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_elevation_candidate_question_v1_20260922.py`: `iba/app/migration/archive/add_elevation_candidate_question_v1_20260922.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_escalation_needs_followup_column_20260830.py`: `iba/app/migration/archive/add_escalation_needs_followup_column_20260830.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_escalation_state_in_progress.py`: `iba/app/migration/archive/add_escalation_state_in_progress.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_healing_word_strong_20260810.py`: `iba/app/migration/archive/add_healing_word_strong_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_hib_centric_traversal_method_rules_20260807.py`: `iba/app/migration/archive/add_hib_centric_traversal_method_rules_20260807.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_lexical_weight_and_closing_checks_20260807.py`: `iba/app/migration/archive/add_lexical_weight_and_closing_checks_20260807.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_lexicon_parse_settings.py`: `iba/app/migration/archive/add_lexicon_parse_settings.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_meaning_keywords_column_v1_20260921.py`: `iba/app/migration/archive/add_meaning_keywords_column_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_negator_connective_partydivine_clusters_v1_20260905.py`: `iba/app/migration/archive/add_negator_connective_partydivine_clusters_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py`: `iba/app/migration/archive/add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_party_human_angelic_clusters_v1_20260905.py`: `iba/app/migration/archive/add_party_human_angelic_clusters_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_passage_story_columns.py`: `iba/app/migration/archive/add_passage_story_columns.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_verse_lexical_updated_at_v1_20260905.py`: `iba/app/migration/archive/add_verse_lexical_updated_at_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_verse_substantiation_questions_v1_20260921.py`: `iba/app/migration/archive/add_verse_substantiation_questions_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/add_work_package_chained_column.py`: `iba/app/migration/archive/add_work_package_chained_column.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/allocate_strongs.py`: `iba/app/migration/archive/allocate_strongs.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/apply_catalogue_wording_v1_20260921.py`: `iba/app/migration/archive/apply_catalogue_wording_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/apply_cluster_alloc_v1_3_20260812.py`: `iba/app/migration/archive/apply_cluster_alloc_v1_3_20260812.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/apply_m47_reallocation_1880_v1_20260928.py`: `iba/app/migration/archive/apply_m47_reallocation_1880_v1_20260928.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/apply_prior_reassignments_v1_1_20260812.py`: `iba/app/migration/archive/apply_prior_reassignments_v1_1_20260812.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/apply_semantic_allocation.py`: `iba/app/migration/archive/apply_semantic_allocation.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/archive_oneoff_report_clutter_20260808.py`: `iba/app/migration/archive/archive_oneoff_report_clutter_20260808.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/assign_1807_unmapped_strongs_v1_20260921.py`: `iba/app/migration/archive/assign_1807_unmapped_strongs_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/assign_leg3_orphan_strongs_v1_20260915.py`: `iba/app/migration/archive/assign_leg3_orphan_strongs_v1_20260915.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_all_strong_meaning_tree_gaps_v1_20260910.py`: `iba/app/migration/archive/backfill_all_strong_meaning_tree_gaps_v1_20260910.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_cfg_change_detail_2000_v1_20261012.py`: `iba/app/migration/archive/backfill_cfg_change_detail_2000_v1_20261012.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_foundational_cfg_tables_v1_20260818.py`: `iba/app/migration/archive/backfill_foundational_cfg_tables_v1_20260818.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_healing_exact_variant_meaning_20260810.py`: `iba/app/migration/archive/backfill_healing_exact_variant_meaning_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_morphless_span_fix_20260810.py`: `iba/app/migration/archive/backfill_morphless_span_fix_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_passage_tracking_daniel.py`: `iba/app/migration/archive/backfill_passage_tracking_daniel.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_receive_exact_variant_meaning_20260810.py`: `iba/app/migration/archive/backfill_receive_exact_variant_meaning_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/backfill_subgroup_columns_char_reading_answers_v1_20260918.py`: `iba/app/migration/archive/backfill_subgroup_columns_char_reading_answers_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_book_narrative_generate.py`: `iba/app/migration/archive/bootstrap_book_narrative_generate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_book_narrative_validate.py`: `iba/app/migration/archive/bootstrap_book_narrative_validate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_catalogue_overview_report_v1_20260829.py`: `iba/app/migration/archive/bootstrap_catalogue_overview_report_v1_20260829.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_cfg_utility.py`: `iba/app/migration/archive/bootstrap_cfg_utility.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_cluster_strong_evidence_columns_20260812.py`: `iba/app/migration/archive/bootstrap_cluster_strong_evidence_columns_20260812.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_cluster_tables_20260811.py`: `iba/app/migration/archive/bootstrap_cluster_tables_20260811.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_configuration_maintenance.py`: `iba/app/migration/archive/bootstrap_configuration_maintenance.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_content_index.py`: `iba/app/migration/archive/bootstrap_content_index.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_file_manifest.py`: `iba/app/migration/archive/bootstrap_file_manifest.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_inactive_column.py`: `iba/app/migration/archive/bootstrap_inactive_column.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_lexicon_parsed_layer.py`: `iba/app/migration/archive/bootstrap_lexicon_parsed_layer.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_new_reports_phase1.py`: `iba/app/migration/archive/bootstrap_new_reports_phase1.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_oneoff_report_naming.py`: `iba/app/migration/archive/bootstrap_oneoff_report_naming.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_passage_debate_report.py`: `iba/app/migration/archive/bootstrap_passage_debate_report.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_passage_debate_sync.py`: `iba/app/migration/archive/bootstrap_passage_debate_sync.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_project_database_enum_v1_20260818.py`: `iba/app/migration/archive/bootstrap_project_database_enum_v1_20260818.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_prose_authority_v1_20260818.py`: `iba/app/migration/archive/bootstrap_prose_authority_v1_20260818.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_quality_validate_steps.py`: `iba/app/migration/archive/bootstrap_quality_validate_steps.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_raw_backfill.py`: `iba/app/migration/archive/bootstrap_raw_backfill.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_report_content_governance.py`: `iba/app/migration/archive/bootstrap_report_content_governance.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_report_csv_virtual_table.py`: `iba/app/migration/archive/bootstrap_report_csv_virtual_table.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_report_persistence_governance.py`: `iba/app/migration/archive/bootstrap_report_persistence_governance.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_reports_registration.py`: `iba/app/migration/archive/bootstrap_reports_registration.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_research_db_cfg_table.py`: `iba/app/migration/archive/bootstrap_research_db_cfg_table.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_retention_table_export_registration.py`: `iba/app/migration/archive/bootstrap_retention_table_export_registration.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_setting_module_column.py`: `iba/app/migration/archive/bootstrap_setting_module_column.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_span_reading.py`: `iba/app/migration/archive/bootstrap_span_reading.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_step_kind.py`: `iba/app/migration/archive/bootstrap_step_kind.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_strong_origin_column_20260811.py`: `iba/app/migration/archive/bootstrap_strong_origin_column_20260811.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_verse_analysis_report.py`: `iba/app/migration/archive/bootstrap_verse_analysis_report.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_whole_book_read.py`: `iba/app/migration/archive/bootstrap_whole_book_read.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_word_audit.py`: `iba/app/migration/archive/bootstrap_word_audit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/bootstrap_word_registry_span_report.py`: `iba/app/migration/archive/bootstrap_word_registry_span_report.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_base_all_books.py`: `iba/app/migration/archive/build_base_all_books.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_cfg_index_table.py`: `iba/app/migration/archive/build_cfg_index_table.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_closing_sections_schema.py`: `iba/app/migration/archive/build_closing_sections_schema.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_hib_change_detail_table_20260808.py`: `iba/app/migration/archive/build_hib_change_detail_table_20260808.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_method_rule_table.py`: `iba/app/migration/archive/build_method_rule_table.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_operations_schema.py`: `iba/app/migration/archive/build_operations_schema.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_quality_check_table.py`: `iba/app/migration/archive/build_quality_check_table.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/build_verse_lexical_window1_layer1_layer2_v1_20260904.py`: `iba/app/migration/archive/build_verse_lexical_window1_layer1_layer2_v1_20260904.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/catalogue_cleanup_v2_20260917.py`: `iba/app/migration/archive/catalogue_cleanup_v2_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/catalogue_column_governance_v1_20260921.py`: `iba/app/migration/archive/catalogue_column_governance_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/claude_md_rules_to_config_v1_20261021.py`: `iba/app/migration/archive/claude_md_rules_to_config_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/clean_invalid_question_code_observations_v1_20260917.py`: `iba/app/migration/archive/clean_invalid_question_code_observations_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/cleanout_retired_chapter_generate_config.py`: `iba/app/migration/archive/cleanout_retired_chapter_generate_config.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/cleanout_retired_passage_config.py`: `iba/app/migration/archive/cleanout_retired_passage_config.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/cleanout_retired_verse_span_meaning_config.py`: `iba/app/migration/archive/cleanout_retired_verse_span_meaning_config.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/clear_dan1_stale_passage_20260807.py`: `iba/app/migration/archive/clear_dan1_stale_passage_20260807.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/complete_method_config_20260807.py`: `iba/app/migration/archive/complete_method_config_20260807.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/control_file_check_v1_20261021.py`: `iba/app/migration/archive/control_file_check_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/control_kinds_add_tool_usage_v1_20261021.py`: `iba/app/migration/archive/control_kinds_add_tool_usage_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/control_map_v1_20261021.py`: `iba/app/migration/archive/control_map_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/correct_dan_1_boundary_range.py`: `iba/app/migration/archive/correct_dan_1_boundary_range.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/create_cluster_reading_pipeline_tables_v1_20260916.py`: `iba/app/migration/archive/create_cluster_reading_pipeline_tables_v1_20260916.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/create_observation_enhancer_tables_v1_20260920.py`: `iba/app/migration/archive/create_observation_enhancer_tables_v1_20260920.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/create_run_batch_table_v1_20260918.py`: `iba/app/migration/archive/create_run_batch_table_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/create_vw_strong_gloss_v1_20260910.py`: `iba/app/migration/archive/create_vw_strong_gloss_v1_20260910.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/dedupe_ib_node_2verses_v1_20260923.py`: `iba/app/migration/archive/dedupe_ib_node_2verses_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/delete_blank_tag_candidates.py`: `iba/app/migration/archive/delete_blank_tag_candidates.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/delete_strongs_not_in_verses_v1_20260910.py`: `iba/app/migration/archive/delete_strongs_not_in_verses_v1_20260910.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/design_and_backfill_char_windows_v1_20260918.py`: `iba/app/migration/archive/design_and_backfill_char_windows_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/devmode_rule_from_command_v1_20261021.py`: `iba/app/migration/archive/devmode_rule_from_command_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/docs_archive_pointers_v1_20261021.py`: `iba/app/migration/archive/docs_archive_pointers_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/drop_cluster_gloss_v1_20260917.py`: `iba/app/migration/archive/drop_cluster_gloss_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/enforce_span_grounding_word_level_v1_20260923.py`: `iba/app/migration/archive/enforce_span_grounding_word_level_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/enrich_verse_relational_reading_v1_20260921.py`: `iba/app/migration/archive/enrich_verse_relational_reading_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_crash_review_rollout_20260821.py`: `iba/app/migration/archive/escalation_crash_review_rollout_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_explicit_state_priority_fix_20260821.py`: `iba/app/migration/archive/escalation_explicit_state_priority_fix_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_open_threads_import_v1_20261012.py`: `iba/app/migration/archive/escalation_open_threads_import_v1_20261012.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_open_threads_v1_20261012.py`: `iba/app/migration/archive/escalation_open_threads_v1_20261012.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_redesign_v1_20260819.py`: `iba/app/migration/archive/escalation_redesign_v1_20260819.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_redesign_v1_20260819_ROLLBACK.py`: `iba/app/migration/archive/escalation_redesign_v1_20260819_ROLLBACK.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_redesign_v2_20260820.py`: `iba/app/migration/archive/escalation_redesign_v2_20260820.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_register_v9_build_20260821.py`: `iba/app/migration/archive/escalation_register_v9_build_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_reset_v1_20260816.py`: `iba/app/migration/archive/escalation_reset_v1_20260816.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_thread_config_corrections_v1_20261012.py`: `iba/app/migration/archive/escalation_thread_config_corrections_v1_20261012.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_thread_lifecycle_v1_20261012.py`: `iba/app/migration/archive/escalation_thread_lifecycle_v1_20261012.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_thread_reassign_keeps_state_v1_20261012.py`: `iba/app/migration/archive/escalation_thread_reassign_keeps_state_v1_20261012.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_v1_load_20260821.py`: `iba/app/migration/archive/escalation_v1_load_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/escalation_v1_snapshot_20260821.py`: `iba/app/migration/archive/escalation_v1_snapshot_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/extend_tag_vocabulary_v1_20260917.py`: `iba/app/migration/archive/extend_tag_vocabulary_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/family_reallocation_v1_20260905.py`: `iba/app/migration/archive/family_reallocation_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/filingkit_build_v1_20260828.py`: `iba/app/migration/archive/filingkit_build_v1_20260828.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_cfg_column_fk_gaps.py`: `iba/app/migration/archive/fix_cfg_column_fk_gaps.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_characteristic_terminology_stage1_v1_20260923.py`: `iba/app/migration/archive/fix_characteristic_terminology_stage1_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_cluster_anomalies_v2_20260917.py`: `iba/app/migration/archive/fix_cluster_anomalies_v2_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_cluster_keyword_collisions_v1_20260917.py`: `iba/app/migration/archive/fix_cluster_keyword_collisions_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_cluster_subgroup_unique_constraints_v1_20260917.py`: `iba/app/migration/archive/fix_cluster_subgroup_unique_constraints_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_compound_pk_registration_v1_20260818.py`: `iba/app/migration/archive/fix_compound_pk_registration_v1_20260818.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_dead_gate_citations_v1_20260921.py`: `iba/app/migration/archive/fix_dead_gate_citations_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_escalation_history_write_grant_20260820.py`: `iba/app/migration/archive/fix_escalation_history_write_grant_20260820.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_escalation_short_description_and_columns_20260820.py`: `iba/app/migration/archive/fix_escalation_short_description_and_columns_20260820.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_escalation_titles_v2_20260820.py`: `iba/app/migration/archive/fix_escalation_titles_v2_20260820.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_from_id_mutability_20260821.py`: `iba/app/migration/archive/fix_from_id_mutability_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_hib_is_human_only_method_rule.py`: `iba/app/migration/archive/fix_hib_is_human_only_method_rule.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_ib_node_verse_reference_doc_v1_20260922.py`: `iba/app/migration/archive/fix_ib_node_verse_reference_doc_v1_20260922.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_lexical_meaning_batch_scaling_v1_20260917.py`: `iba/app/migration/archive/fix_lexical_meaning_batch_scaling_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_missing_write_grants_v1_20260818.py`: `iba/app/migration/archive/fix_missing_write_grants_v1_20260818.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_module_blocking_enforced_by_20260821.py`: `iba/app/migration/archive/fix_module_blocking_enforced_by_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_no_vocab_shells_v1_20260910.py`: `iba/app/migration/archive/fix_no_vocab_shells_v1_20260910.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_nonhuman_scope_method_rule.py`: `iba/app/migration/archive/fix_nonhuman_scope_method_rule.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_primary_term_terminology_v1_20260921.py`: `iba/app/migration/archive/fix_primary_term_terminology_v1_20260921.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_run_batch_unique_constraint_v1_20260918.py`: `iba/app/migration/archive/fix_run_batch_unique_constraint_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_stage1_governance_gaps_v1_20260922.py`: `iba/app/migration/archive/fix_stage1_governance_gaps_v1_20260922.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_strong_meaning_tree_collapse.py`: `iba/app/migration/archive/fix_strong_meaning_tree_collapse.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/fix_stuck_run_states.py`: `iba/app/migration/archive/fix_stuck_run_states.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/flag_management_build_v1_20260823.py`: `iba/app/migration/archive/flag_management_build_v1_20260823.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/folder_purpose_autoassess_build_v1_20260828.py`: `iba/app/migration/archive/folder_purpose_autoassess_build_v1_20260828.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/folder_purpose_build_v1_20260828.py`: `iba/app/migration/archive/folder_purpose_build_v1_20260828.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/history_out_of_read_path_v1_20261021.py`: `iba/app/migration/archive/history_out_of_read_path_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/import_seed.py`: `iba/app/migration/archive/import_seed.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/legacy_import.py`: `iba/app/migration/archive/legacy_import.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/m0_5_11_surface_cue_v1_20260923.py`: `iba/app/migration/archive/m0_5_11_surface_cue_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/make_verse_lexical_note_passage_id_nullable_v1_20260905.py`: `iba/app/migration/archive/make_verse_lexical_note_passage_id_nullable_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/mark_bible_research_findings_inactive_v1_20260924.py`: `iba/app/migration/archive/mark_bible_research_findings_inactive_v1_20260924.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/memory_rules_to_config_v1_20261021.py`: `iba/app/migration/archive/memory_rules_to_config_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/merge_m17_into_m16_v1_20260906.py`: `iba/app/migration/archive/merge_m17_into_m16_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/merge_m27_into_m55_v1_20260906.py`: `iba/app/migration/archive/merge_m27_into_m55_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/merge_m29_into_m18_v1_20260906.py`: `iba/app/migration/archive/merge_m29_into_m18_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/merge_m38_into_m45_v1_20260906.py`: `iba/app/migration/archive/merge_m38_into_m45_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/migrate_obs_question_catalogue_to_iba_v1_20260916.py`: `iba/app/migration/archive/migrate_obs_question_catalogue_to_iba_v1_20260916.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/move_g2983_suffering_to_receive_20260810.py`: `iba/app/migration/archive/move_g2983_suffering_to_receive_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/narrative_chapter_table_config_v1_20261018.py`: `iba/app/migration/archive/narrative_chapter_table_config_v1_20261018.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/narrative_claim_register_config_v1_20261013.py`: `iba/app/migration/archive/narrative_claim_register_config_v1_20261013.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/narrative_claim_register_import_v1_20261013.py`: `iba/app/migration/archive/narrative_claim_register_import_v1_20261013.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/pathaudit_build_v1_20260828.py`: `iba/app/migration/archive/pathaudit_build_v1_20260828.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/populate_cfg_index_rows.py`: `iba/app/migration/archive/populate_cfg_index_rows.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/progressive_relational_verse_reading_v1_20260917.py`: `iba/app/migration/archive/progressive_relational_verse_reading_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/prose_add_edit_rules_build_v1_20260826.py`: `iba/app/migration/archive/prose_add_edit_rules_build_v1_20260826.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/prose_change_log_build_v1_20260824.py`: `iba/app/migration/archive/prose_change_log_build_v1_20260824.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/prose_first_layer_build_v1_20260824.py`: `iba/app/migration/archive/prose_first_layer_build_v1_20260824.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/prose_orphan_enum_fix_v1_20260826.py`: `iba/app/migration/archive/prose_orphan_enum_fix_v1_20260826.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/prose_output_dirs_build_v1_20260828.py`: `iba/app/migration/archive/prose_output_dirs_build_v1_20260828.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reactivate_passage_quality.py`: `iba/app/migration/archive/reactivate_passage_quality.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/realign_catalogue_to_dimensions_v1_20260917.py`: `iba/app/migration/archive/realign_catalogue_to_dimensions_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rebuild_escalation_from_export_20260821.py`: `iba/app/migration/archive/rebuild_escalation_from_export_20260821.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rebuild_escalation_rules_config_20260820.py`: `iba/app/migration/archive/rebuild_escalation_rules_config_20260820.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rebuild_prose_section_fk_v1_20260905.py`: `iba/app/migration/archive/rebuild_prose_section_fk_v1_20260905.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rebuild_span_combined_units.py`: `iba/app/migration/archive/rebuild_span_combined_units.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rebuild_verse_lexical_layer1_v1_20260916.py`: `iba/app/migration/archive/rebuild_verse_lexical_layer1_v1_20260916.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reclassify_g0627_to_t3_v1_20260917.py`: `iba/app/migration/archive/reclassify_g0627_to_t3_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reconcile_daniel_debate_paths.py`: `iba/app/migration/archive/reconcile_daniel_debate_paths.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reconcile_daniel_debate_paths_20260808.py`: `iba/app/migration/archive/reconcile_daniel_debate_paths_20260808.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reframe_what_is_to_what_does_show_v1_20260923.py`: `iba/app/migration/archive/reframe_what_is_to_what_does_show_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_20261021_migrations_v1_20261021.py`: `iba/app/migration/archive/register_20261021_migrations_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_cluster_answer_step_v1_20260918.py`: `iba/app/migration/archive/register_cluster_answer_step_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_cluster_reading_step_v1_20260918.py`: `iba/app/migration/archive/register_cluster_reading_step_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_cluster_subgroup_step_v1_20260917.py`: `iba/app/migration/archive/register_cluster_subgroup_step_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_ib_observation_enums_v1_20260917.py`: `iba/app/migration/archive/register_ib_observation_enums_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_lexical_meaning_step_v1_20260917.py`: `iba/app/migration/archive/register_lexical_meaning_step_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_lexical_readiness_check_v1_20260916.py`: `iba/app/migration/archive/register_lexical_readiness_check_v1_20260916.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_needs_adjacent_verse_context_tag_v1_20260918.py`: `iba/app/migration/archive/register_needs_adjacent_verse_context_tag_v1_20260918.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_prose_set_status_v1_20260827.py`: `iba/app/migration/archive/register_prose_set_status_v1_20260827.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_purge_audit_step_v1_20260919.py`: `iba/app/migration/archive/register_purge_audit_step_v1_20260919.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_purge_execute_step_v1_20260924.py`: `iba/app/migration/archive/register_purge_execute_step_v1_20260924.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_purge_retire_database_step_v1_20260924.py`: `iba/app/migration/archive/register_purge_retire_database_step_v1_20260924.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/register_session_close_step_v1_20260924.py`: `iba/app/migration/archive/register_session_close_step_v1_20260924.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rehome_multi_chapter_vigilance_rule_20260807.py`: `iba/app/migration/archive/rehome_multi_chapter_vigilance_rule_20260807.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rename_hib_change_detail_to_debate_change_detail_20260808.py`: `iba/app/migration/archive/rename_hib_change_detail_to_debate_change_detail_20260808.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rename_span_reading_to_lexical.py`: `iba/app/migration/archive/rename_span_reading_to_lexical.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/repair_dan8_daniel_phenomenon_hib_id_20260808.py`: `iba/app/migration/archive/repair_dan8_daniel_phenomenon_hib_id_20260808.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/repair_strong_sense_head.py`: `iba/app/migration/archive/repair_strong_sense_head.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/repurpose_incurability_to_suffering_20260810.py`: `iba/app/migration/archive/repurpose_incurability_to_suffering_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/repurpose_passage_tracking.py`: `iba/app/migration/archive/repurpose_passage_tracking.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reset_escalation_tables_20260820.py`: `iba/app/migration/archive/reset_escalation_tables_20260820.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reset_m67_for_progressive_reading_v1_20260917.py`: `iba/app/migration/archive/reset_m67_for_progressive_reading_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolve_mcode_conflicts_by_name_match_v1_20260906.py`: `iba/app/migration/archive/resolve_mcode_conflicts_by_name_match_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolve_mcode_conflicts_heuristic_wins_v1_20260906.py`: `iba/app/migration/archive/resolve_mcode_conflicts_heuristic_wins_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolve_mcode_conflicts_review_flag_v1_20260906.py`: `iba/app/migration/archive/resolve_mcode_conflicts_review_flag_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolve_mcode_conflicts_synonym_match_v1_20260906.py`: `iba/app/migration/archive/resolve_mcode_conflicts_synonym_match_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolve_old_migration_self_duplicates_v1_20260906.py`: `iba/app/migration/archive/resolve_old_migration_self_duplicates_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolved_sense_mcode_only_v1_20260906.py`: `iba/app/migration/archive/resolved_sense_mcode_only_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolved_sense_removed_v1_20260907.py`: `iba/app/migration/archive/resolved_sense_removed_v1_20260907.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/resolved_sense_revived_v1_20260910.py`: `iba/app/migration/archive/resolved_sense_revived_v1_20260910.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/restore_incurability_legacy_word_strong_20260810.py`: `iba/app/migration/archive/restore_incurability_legacy_word_strong_20260810.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/restructure_configmaint_report_sections.py`: `iba/app/migration/archive/restructure_configmaint_report_sections.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retag_answered_no_flag_v1_20260917.py`: `iba/app/migration/archive/retag_answered_no_flag_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retire_cfg_prose_chapter_v1_20260827.py`: `iba/app/migration/archive/retire_cfg_prose_chapter_v1_20260827.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retire_from_id_related_activity_v1_20260827.py`: `iba/app/migration/archive/retire_from_id_related_activity_v1_20260827.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retire_m10b_into_m58_v1_20260906.py`: `iba/app/migration/archive/retire_m10b_into_m58_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retire_old_layer2_lexical_enrich_v1_20260917.py`: `iba/app/migration/archive/retire_old_layer2_lexical_enrich_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retire_old_migration_mcode_conflicts_v1_20260906.py`: `iba/app/migration/archive/retire_old_migration_mcode_conflicts_v1_20260906.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retract_candidate_system.py`: `iba/app/migration/archive/retract_candidate_system.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retract_passage_system.py`: `iba/app/migration/archive/retract_passage_system.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/retrofit_debate_lexicon_tables.py`: `iba/app/migration/archive/retrofit_debate_lexicon_tables.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/reword_word_level_questions_strong_keyed_v1_20260923.py`: `iba/app/migration/archive/reword_word_level_questions_strong_keyed_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rule59_drop_dead_pointer_v1_20261021.py`: `iba/app/migration/archive/rule59_drop_dead_pointer_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rule63_approval_handover_checks_v1_20261021.py`: `iba/app/migration/archive/rule63_approval_handover_checks_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rule97_copy_with_backup_api_v1_20261021.py`: `iba/app/migration/archive/rule97_copy_with_backup_api_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/rule_delivery_scope_v1_20261021.py`: `iba/app/migration/archive/rule_delivery_scope_v1_20261021.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/run_verse_lexical_layer1_rebuild_v1_20260916.py`: `iba/app/migration/archive/run_verse_lexical_layer1_rebuild_v1_20260916.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/seed_method_rules.py`: `iba/app/migration/archive/seed_method_rules.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/simplify_M0_8_1_elevation_flag_v1_20260923.py`: `iba/app/migration/archive/simplify_M0_8_1_elevation_flag_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/split_lexical_meaning_word_relational_v1_20260923.py`: `iba/app/migration/archive/split_lexical_meaning_word_relational_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py`: `iba/app/migration/archive/split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/stage_rename_and_baseline_tag_v1_20260917.py`: `iba/app/migration/archive/stage_rename_and_baseline_tag_v1_20260917.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/strengthen_closing_set_rules_20260807.py`: `iba/app/migration/archive/strengthen_closing_set_rules_20260807.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/withdraw_stale_word_level_observations_v1_20260923.py`: `iba/app/migration/archive/withdraw_stale_word_level_observations_v1_20260923.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/BookNarrative-Generate.ps1`: `iba/app/ps/archive/BookNarrative-Generate.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/BookNarrative-Validate.ps1`: `iba/app/ps/archive/BookNarrative-Validate.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/Candidate-Curate.ps1`: `iba/app/ps/archive/Candidate-Curate.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/Candidate-Quality.ps1`: `iba/app/ps/archive/Candidate-Quality.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/Chapter-Generate.ps1`: `iba/app/ps/archive/Chapter-Generate.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/ContentIndex-Rebuild.ps1`: `iba/app/ps/archive/ContentIndex-Rebuild.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/PassageDebate-Report.ps1`: `iba/app/ps/archive/PassageDebate-Report.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/PassageDebate-Sync.ps1`: `iba/app/ps/archive/PassageDebate-Sync.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/SeedCandidate-Report.ps1`: `iba/app/ps/archive/SeedCandidate-Report.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/Set-Candidates.ps1`: `iba/app/ps/archive/Set-Candidates.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/VerseSpanMeaning-Report.ps1`: `iba/app/ps/archive/VerseSpanMeaning-Report.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/create-iba-view-template.ps1`: `iba/app/ps/archive/create-iba-view-template.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/create-passage-view-and-export.ps1`: `iba/app/ps/archive/create-passage-view-and-export.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/create-passages-by-book-view-and-export.ps1`: `iba/app/ps/archive/create-passages-by-book-view-and-export.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/export-iba-config-tables.ps1`: `iba/app/ps/archive/export-iba-config-tables.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/generate-iba-db-schema-report.ps1`: `iba/app/ps/archive/generate-iba-db-schema-report.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/_check_ib_related_span_step_coverage.py`: `iba/app/tools/archive/_check_ib_related_span_step_coverage.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/_check_missing_strongs_in_step.py`: `iba/app/tools/archive/_check_missing_strongs_in_step.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/_check_span_unmatched_lexicon_json.py`: `iba/app/tools/archive/_check_span_unmatched_lexicon_json.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_lexicon_combined_extract.py`: `iba/app/tools/archive/build_lexicon_combined_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_lexicon_lookup_extract.py`: `iba/app/tools/archive/build_lexicon_lookup_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_lsj_sense_extract.py`: `iba/app/tools/archive/build_lsj_sense_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_meaning_tree_extract.py`: `iba/app/tools/archive/build_meaning_tree_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_mounce_lexicon_extract.py`: `iba/app/tools/archive/build_mounce_lexicon_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_span_heatmap_v1.py`: `iba/app/tools/archive/build_span_heatmap_v1.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_span_term_reconciliation.py`: `iba/app/tools/archive/build_span_term_reconciliation.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_strong_info_extract.py`: `iba/app/tools/archive/build_strong_info_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_strong_related_extract.py`: `iba/app/tools/archive/build_strong_related_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_verse_span_meaning_extract.py`: `iba/app/tools/archive/build_verse_span_meaning_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/build_verse_span_strongtree_extract.py`: `iba/app/tools/archive/build_verse_span_strongtree_extract.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/ib_relevance_classifier.py`: `iba/app/tools/archive/ib_relevance_classifier.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/lexicon_split_common.py`: `iba/app/tools/archive/lexicon_split_common.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/log_retention.py`: `iba/app/tools/archive/log_retention.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/purge_word.py`: `iba/app/tools/archive/purge_word.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/temp_2192_active_reach.py`: `iba/app/tools/archive/temp_2192_active_reach.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/temp_2192_apply.py`: `iba/app/tools/archive/temp_2192_apply.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/word_strong_span_report.py`: `iba/app/tools/archive/word_strong_span_report.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/build_debate_report.py`: `iba/app/tools/build_debate_report.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/export_tables_csv.py`: `iba/app/tools/export_tables_csv.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_
