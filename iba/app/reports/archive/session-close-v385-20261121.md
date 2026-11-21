# Session close (#1875, rebuilt #2173)

> Generated 2026-11-21T05:51:16Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `19e3337e-aea1-4434-b72a-e90cdff0b1d6` (CLAUDE_CODE_SESSION_ID); started 2026-11-20T13:55:48Z; window base commit `5a04e37069cf09b799b9645ed2b25a4a780bf1d5`
- compliance file: `Logs/compliance/COMPLIANCE-20261120-19e3337e.md`; session log: `--`
- **open findings: 66**; cleared by disposition: 0


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

66 open finding(s); SC2 6, SC3 12, SC4 6, SC6 40, SC8 1, SC16 1

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

- **OPEN** `SC3:a6cb58ac`: researcher message 2026-11-20T14:04 is in no escalation comment written this session: "resolve 2511, 2513, 2512, 2514.  2510 : create a new escalation with the open item list, and then close 2510 as completed."
- **OPEN** `SC3:d6cfe434`: researcher message 2026-11-20T14:13 is in no escalation comment written this session: "2515 Question 27 - escalation history export anomaly.  the following is the content of the comment column of 2510. Reconcile this with history report of this es"
- **OPEN** `SC3:89214c94`: researcher message 2026-11-20T16:26 is too short to be matched; name where it is recorded: "Not yet"
- **OPEN** `SC3:d5fcf43f`: researcher message 2026-11-20T16:49 is in no escalation comment written this session: "is this the document I must approve Workflow\Programme\programme_prose\wa-programme-prose-extract-20261120.md"
- **OPEN** `SC3:71a34c86`: researcher message 2026-11-20T17:58 is in no escalation comment written this session: "did you read back the 2510 outputs to check the prose?  Did you check you history md to see what sections of prose should not be included.  I was not sure where"
- **OPEN** `SC3:2e28d40f`: researcher message 2026-11-20T17:44 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:35916d27`: researcher message 2026-11-20T18:02 is in no escalation comment written this session: "where do I find the stages 3 and 4 and 5 in the programme prose"
- **OPEN** `SC3:d3a7b670`: researcher message 2026-11-20T18:04 is in no escalation comment written this session: "so how can you say the prose is complete. what are you measuring it against?"
- **OPEN** `SC3:8adb07e8`: researcher message 2026-11-20T18:28 is in no escalation comment written this session: "did you include everything in the one book - programme, or did you make updates in the detail design book."
- **OPEN** `SC3:0c0750eb`: researcher message 2026-11-20T18:36 is too short to be matched; name where it is recorded: "Approved"
- **OPEN** `SC3:ee7b67ac`: researcher message 2026-11-21T03:56 is too short to be matched; name where it is recorded: "Approve all three"
- **OPEN** `SC3:2cd70d95`: researcher message 2026-11-20T19:45 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:d6cfe434`: researcher message 2026-11-20T14:13 holds, defers or asks to check something; name its register item: "2515 Question 27 - escalation history export anomaly.  the following is the content of the comment column of 2510. Reconcile this with history report of this es"
- **OPEN** `SC4b:71a34c86`: researcher message 2026-11-20T17:58 holds, defers or asks to check something; name its register item: "did you read back the 2510 outputs to check the prose?  Did you check you history md to see what sections of prose should not be included.  I was not sure where"
- **OPEN** `SC4b:2e28d40f`: researcher message 2026-11-20T17:44 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:a236e4c8`: researcher message 2026-11-20T18:07 holds, defers or asks to check something; name its register item: "listen carefully - you going around and around.  I just asked you to readback all the 2510 md files into prose to check if you have taken everything into accoun"
- **OPEN** `SC4b:c1910312`: researcher message 2026-11-20T18:41 holds, defers or asks to check something; name its register item: "2516 approved for your follow up action; resolve 2518.  2515 can be finalised, 2509 should now be clear, 2508 have previously been ruled on, is 2507 still open."
- **OPEN** `SC4b:2cd70d95`: researcher message 2026-11-20T19:45 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


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
- **OPEN** `SC6:B:123`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (19e3337e-aea1-4434-b72a-e90cdff0b1d6); write it (governance.session_log_required_content)

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

- **OPEN** `SC16:Escalation.ps1_-Action_Update`: Escalation.ps1 -Action Update failed 3 times this session: [31;1mEscalation.ps1: [31;1mCannot validate argument on parameter 'State'. The argument "approved" does not belong to ; Update needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default p; error: decision_required items may only move to approved from a CURRENT next_action of ready_for_approval -- no shortcut

_no finding_
