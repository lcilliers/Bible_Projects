# Session close (#1875, rebuilt #2173)

> Generated 2026-10-22T12:02:57Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `6c511f74-b972-40bd-beb3-c64ce8d4b665` (CLAUDE_CODE_SESSION_ID); started 2026-10-22T09:55:56Z; window base commit `17a8c612a531454d87f430598a84ca211c0cf79e`
- compliance file: `Logs/compliance/COMPLIANCE-20261022-6c511f74.md`; session log: `--`
- **open findings: 59**; cleared by disposition: 0


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

59 open finding(s); SC2 6, SC3 5, SC4 4, SC6 41, SC8 1, SC10 2

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

- **OPEN** `SC3:89f94c5b`: researcher message 2026-10-22T09:58 is in no escalation comment written this session: "continue with 2177 - you had unanswered questions at the end of the last session?"
- **OPEN** `SC3:671b57d0`: researcher message 2026-10-22T10:53 is in no escalation comment written this session: "<task-notification>
<task-id>bp70epqhe</task-id>
<tool-use-id>toolu_0137gbTjSkdtsCfvV5BqCais</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:5c1f5ded`: researcher message 2026-10-22T11:07 is in no escalation comment written this session: "<task-notification>
<task-id>buxh5cvs9</task-id>
<tool-use-id>toolu_01BesyEzuf483uZevj2E9JjT</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:d75ddab1`: researcher message 2026-10-22T11:20 is in no escalation comment written this session: "<task-notification>
<task-id>b16xpgdj3</task-id>
<tool-use-id>toolu_019sC7XbKVx1s5guAKCdeEKz</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:5129f1d2`: researcher message 2026-10-22T12:01 is too short to be matched; name where it is recorded: "/exit-development-mode"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4a:8331e8a6`: `iba/app/BUILD.md` line 18837: open item names no OT-nn.n or #nnnn: "- `iba/app/lib/strandreading.py`: Context records every matching open item against the strand (`match_items`: its words, every cluster they "
- **OPEN** `SC4a:dc5cb062`: `iba/app/BUILD.md` line 18844: open item names no OT-nn.n or #nnnn: "- `iba/app/handlers/strandreading.py`: Map no longer writes held statements as a comment on the strand's escalation; they are open items."
- **OPEN** `SC4a:1e658796`: `iba/app/BUILD.md` line 18846: open item names no OT-nn.n or #nnnn: "- `iba/app/ps/Strand-Reading.ps1`: help text (no parameter change)."
- **OPEN** `SC4b:d6b14aa0`: researcher message 2026-10-22T10:04 holds, defers or asks to check something; name its register item: "Q1 M63 is likely to closest. Did you check the location of associated strongs?  Q2 - this should not happen. report it to investigate.  Use open items to raise "

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 46.

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

- **OPEN** `SC8:log`: no session log in Logs/ names this session (6c511f74-b972-40bd-beb3-c64ce8d4b665); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/tools/temp_2172_map_handler_test_run.py`: `iba/app/tools/temp_2172_map_handler_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2172_strand_test_run.py`: `iba/app/tools/temp_2172_strand_test_run.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: RUN (a thread row changed)

_no finding_

_no finding_
