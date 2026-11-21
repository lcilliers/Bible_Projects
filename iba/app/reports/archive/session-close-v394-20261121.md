# Session close (#1875, rebuilt #2173)

> Generated 2026-11-21T19:10:45Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `2278afec-65aa-4ba0-aa26-832ef494faed` (CLAUDE_CODE_SESSION_ID); started 2026-11-21T13:23:53Z; window base commit `3e6623cc6ec427047aaeee342975f3676075ac2e`
- compliance file: `Logs/compliance/COMPLIANCE-20261121-2278afec.md`; session log: `--`
- **open findings: 60**; cleared by disposition: 0


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
- sc17

<a id="summary"></a>
## Summary

60 open finding(s); SC2 6, SC3 10, SC4 1, SC6 40, SC8 1, SC16 2

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

- **OPEN** `SC3:cbe60a18`: researcher message 2026-11-21T13:25 is too short to be matched; name where it is recorded: "Work #2527"
- **OPEN** `SC3:f4e95711`: researcher message 2026-11-21T14:22 is too short to be matched; name where it is recorded: "Start step 2"
- **OPEN** `SC3:2f5fb818`: researcher message 2026-11-21T17:31 is too short to be matched; name where it is recorded: "Open 3.3"
- **OPEN** `SC3:214b5e88`: researcher message 2026-11-21T18:42 is too short to be matched; name where it is recorded: "Approve"
- **OPEN** `SC3:483cc8a0`: researcher message 2026-11-21T18:36 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:4fa658eb`: researcher message 2026-11-21T18:52 is too short to be matched; name where it is recorded: "Approve A"
- **OPEN** `SC3:2fd57c83`: researcher message 2026-11-21T18:54 is in no escalation comment written this session: "can you prepare a report showing me the observations for each surface group of thought"
- **OPEN** `SC3:1ae45666`: researcher message 2026-11-21T19:00 is in no escalation comment written this session: "before we close. are there anything that you did for thought, that is not properly set in configs, and is the code used repeatable. do you need to generate new "
- **OPEN** `SC3:10b4b3af`: researcher message 2026-11-21T19:05 is in no escalation comment written this session: "I definetely do not want you to re-create any helpers each time an analysis is done.  the analysis process must be codified in such a way that it can run 169 ti"
- **OPEN** `SC3:387b545c`: researcher message 2026-11-21T19:10 is too short to be matched; name where it is recorded: "run session-close"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:483cc8a0`: researcher message 2026-11-21T18:36 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

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

- **OPEN** `SC8:log`: no session log in Logs/ names this session (2278afec-65aa-4ba0-aa26-832ef494faed); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

_no finding_

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

- **OPEN** `SC16:Escalation.ps1_-Action_Raise`: Escalation.ps1 -Action Raise failed 3 times this session: -ShortDescription has no effect on -Action Raise (only -Action Correction reads it) -- Raise's title comes from -Questio; Raise needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default pr; Raise needs -Question and -Comment (minimum: what this item is about).
- **OPEN** `SC16:Escalation.ps1_-Action_Update`: Escalation.ps1 -Action Update failed 3 times this session: Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Undermining Oversight]. If you h; error: decision_required items may only move to approved from a CURRENT next_action of ready_for_approval -- no shortcut; error: next_action='approved' requires resolution to be filled in (plan v3 sec3)

_no finding_
