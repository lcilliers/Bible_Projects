# Session close (#1875, rebuilt #2173)

> Generated 2026-10-22T09:11:11Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `691d410b-cdfa-4fe4-a9ed-d36cfccc293d` (CLAUDE_CODE_SESSION_ID); started 2026-10-22T06:44:16Z; window base commit `55975aa71006f1b9d1f05f6aacc7ad5f3202c949`
- compliance file: `Logs/compliance/COMPLIANCE-20261022-691d410b.md`; session log: `--`
- **open findings: 106**; cleared by disposition: 0


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
- sc16

<a id="summary"></a>
## Summary

106 open finding(s); SC2 6, SC3 2, SC4 1, SC5 46, SC6 41, SC8 1, SC10 8, SC16 1

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

- **OPEN** `SC3:09c02bbc`: researcher message 2026-10-22T07:57 is in no escalation comment written this session: "I don't understand why the building of the tools require hours of work"
- **OPEN** `SC3:a0b8dd54`: researcher message 2026-10-22T09:09 is in no escalation comment written this session: "should we do a session-close before this"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:18be20a0`: researcher message 2026-10-22T08:59 holds, defers or asks to check something; name its register item: "approved 2172 for your follow up"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 46.

- **OPEN** `SC5c:new:90dd8120`: register check, new since the previous close: claim I-2 is current but no current block tells it
- **OPEN** `SC5c:new:4a70ffd7`: register check, new since the previous close: claim I-3 is current but no current block tells it
- **OPEN** `SC5c:new:7d50cf16`: register check, new since the previous close: claim I-4 is current but no current block tells it
- **OPEN** `SC5c:new:cabff5c8`: register check, new since the previous close: claim I-6 is current but no current block tells it
- **OPEN** `SC5c:new:f8d94264`: register check, new since the previous close: claim 1-1 is current but no current block tells it
- **OPEN** `SC5c:new:2b6d2e04`: register check, new since the previous close: claim 1-2 is current but no current block tells it
- **OPEN** `SC5c:new:a695e99e`: register check, new since the previous close: claim 1-3 is current but no current block tells it
- **OPEN** `SC5c:new:197d991b`: register check, new since the previous close: claim 1-5 is current but no current block tells it
- **OPEN** `SC5c:new:914f1f76`: register check, new since the previous close: claim 1-6 is current but no current block tells it
- **OPEN** `SC5c:new:15e95e80`: register check, new since the previous close: claim 2-1 is current but no current block tells it
- **OPEN** `SC5c:new:08b47cd0`: register check, new since the previous close: claim 2-4 is current but no current block tells it
- **OPEN** `SC5c:new:6932beb2`: register check, new since the previous close: claim 2-8 is current but no current block tells it
- **OPEN** `SC5c:new:d142f0a0`: register check, new since the previous close: claim 2-10 is current but no current block tells it
- **OPEN** `SC5c:new:514231da`: register check, new since the previous close: claim 2-11 is current but no current block tells it
- **OPEN** `SC5c:new:8bcbe147`: register check, new since the previous close: claim 2-12 is current but no current block tells it
- **OPEN** `SC5c:new:e3b5916a`: register check, new since the previous close: claim 2-14 is current but no current block tells it
- **OPEN** `SC5c:new:59eadfe8`: register check, new since the previous close: claim 2-16 is current but no current block tells it
- **OPEN** `SC5c:new:9289905b`: register check, new since the previous close: claim 3-1 is current but no current block tells it
- **OPEN** `SC5c:new:2ad7d665`: register check, new since the previous close: claim 3-2 is current but no current block tells it
- **OPEN** `SC5c:new:2118ecb8`: register check, new since the previous close: claim 3-3 is current but no current block tells it
- **OPEN** `SC5c:new:43d17a18`: register check, new since the previous close: claim 3-4 is current but no current block tells it
- **OPEN** `SC5c:new:d8e5cc12`: register check, new since the previous close: claim 3-5 is current but no current block tells it
- **OPEN** `SC5c:new:85b7a240`: register check, new since the previous close: claim 3-8 is current but no current block tells it
- **OPEN** `SC5c:new:8f073986`: register check, new since the previous close: claim 3-11 is current but no current block tells it
- **OPEN** `SC5c:new:93edb327`: register check, new since the previous close: claim 3-14 is current but no current block tells it
- **OPEN** `SC5c:new:aec228fc`: register check, new since the previous close: claim 4-1 is current but no current block tells it
- **OPEN** `SC5c:new:35f6c1e5`: register check, new since the previous close: claim 4-2 is current but no current block tells it
- **OPEN** `SC5c:new:551af1ee`: register check, new since the previous close: claim 4-3 is current but no current block tells it
- **OPEN** `SC5c:new:a72de27d`: register check, new since the previous close: claim 4-4 is current but no current block tells it
- **OPEN** `SC5c:new:8caccf68`: register check, new since the previous close: claim 4-5 is current but no current block tells it
- **OPEN** `SC5c:new:b8884c49`: register check, new since the previous close: claim 4-7 is current but no current block tells it
- **OPEN** `SC5c:new:1e1ed93e`: register check, new since the previous close: claim 4-9 is current but no current block tells it
- **OPEN** `SC5c:new:478d8b49`: register check, new since the previous close: claim 4-10 is current but no current block tells it
- **OPEN** `SC5c:new:f1e1bc22`: register check, new since the previous close: claim 5-1 is current but no current block tells it
- **OPEN** `SC5c:new:eb323497`: register check, new since the previous close: claim 5-3 is current but no current block tells it
- **OPEN** `SC5c:new:99dbfcb0`: register check, new since the previous close: claim 6-1 is current but no current block tells it
- **OPEN** `SC5c:new:da4a3a52`: register check, new since the previous close: claim 6-3 is current but no current block tells it
- **OPEN** `SC5c:new:563f3525`: register check, new since the previous close: claim 8-1 is current but no current block tells it
- **OPEN** `SC5c:new:784e7308`: register check, new since the previous close: claim 9-1 is current but no current block tells it
- **OPEN** `SC5c:new:fdffc28a`: register check, new since the previous close: claim 9-3 is current but no current block tells it
- **OPEN** `SC5c:new:5c3aee2f`: register check, new since the previous close: claim 9-4 is current but no current block tells it
- **OPEN** `SC5c:new:10e313a7`: register check, new since the previous close: claim 9-5 is current but no current block tells it
- **OPEN** `SC5c:new:f2044af3`: register check, new since the previous close: claim 10-1 is current but no current block tells it
- **OPEN** `SC5c:new:0a2c9d99`: register check, new since the previous close: claim 10-2 is current but no current block tells it
- **OPEN** `SC5c:new:6fee5eb5`: register check, new since the previous close: claim 10-3 is current but no current block tells it
- **OPEN** `SC5c:new:dcd8372e`: register check, new since the previous close: claim 10-7 is current but no current block tells it

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
- **OPEN** `SC6:G:governance.primary_responsibility`: engaged, with no evidence
- **OPEN** `SC6:G:governance.programme_stages`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_operations`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_iba_app`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_project`: engaged, with no evidence
- **OPEN** `SC6:G:governance.study_status`: engaged, with no evidence
- **OPEN** `SC6:B:1`: engaged, with no evidence
- **OPEN** `SC6:B:2`: engaged, with no evidence
- **OPEN** `SC6:B:4`: engaged, with no evidence
- **OPEN** `SC6:B:10`: engaged, with no evidence
- **OPEN** `SC6:B:16`: engaged, with no evidence
- **OPEN** `SC6:B:17`: engaged, with no evidence
- **OPEN** `SC6:B:18`: engaged, with no evidence
- **OPEN** `SC6:B:19`: engaged, with no evidence
- **OPEN** `SC6:B:20`: engaged, with no evidence
- **OPEN** `SC6:B:21`: engaged, with no evidence
- **OPEN** `SC6:B:22`: engaged, with no evidence
- **OPEN** `SC6:B:23`: engaged, with no evidence
- **OPEN** `SC6:B:24`: engaged, with no evidence
- **OPEN** `SC6:B:25`: engaged, with no evidence
- **OPEN** `SC6:B:27`: engaged, with no evidence
- **OPEN** `SC6:B:28`: engaged, with no evidence
- **OPEN** `SC6:B:31`: engaged, with no evidence
- **OPEN** `SC6:B:34`: engaged, with no evidence
- **OPEN** `SC6:B:36`: engaged, with no evidence
- **OPEN** `SC6:B:40`: engaged, with no evidence
- **OPEN** `SC6:B:44`: engaged, with no evidence
- **OPEN** `SC6:B:83`: engaged, with no evidence
- **OPEN** `SC6:B:97`: engaged, with no evidence
- **OPEN** `SC6:B:98`: engaged, with no evidence
- **OPEN** `SC6:B:99`: engaged, with no evidence
- **OPEN** `SC6:B:100`: engaged, with no evidence
- **OPEN** `SC6:B:101`: engaged, with no evidence
- **OPEN** `SC6:B:102`: engaged, with no evidence
- **OPEN** `SC6:B:105`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (691d410b-cdfa-4fe4-a9ed-d36cfccc293d); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/migration/archive/narrative_home_2172_v1_20261022.py`: `iba/app/migration/archive/narrative_home_2172_v1_20261022.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/record_retire_onfail_2172_v1_20261022.py`: `iba/app/migration/archive/record_retire_onfail_2172_v1_20261022.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/strand_reading_enums_2172_v1_20261022.py`: `iba/app/migration/archive/strand_reading_enums_2172_v1_20261022.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/strand_reading_steps_2172_v1_20261022.py`: `iba/app/migration/archive/strand_reading_steps_2172_v1_20261022.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_map_handler_test_run.py`: `iba/app/tools/temp_2172_map_handler_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_register_test_run.py`: `iba/app/tools/temp_2172_register_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_rewrite_test_run.py`: `iba/app/tools/temp_2172_rewrite_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_strand_test_run.py`: `iba/app/tools/temp_2172_strand_test_run.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

- **OPEN** `SC16:Config-Maintenance.ps1_-Step_Validate`: Config-Maintenance.ps1 -Step Validate failed 2 times this session: work package : configuration-maintenance
