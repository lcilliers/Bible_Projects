# Session close (#1875, rebuilt #2173)

> Generated 2026-11-10T16:36:58Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `77a059b4-65ef-4409-8675-22c064cc23f7` (CLAUDE_CODE_SESSION_ID); started 2026-11-10T13:09:21Z; window base commit `aa52fc5d39a8ce16f60d70348d27ce3c1a59c577`
- compliance file: `Logs/compliance/COMPLIANCE-20261110-77a059b4.md`; session log: `--`
- **open findings: 58**; cleared by disposition: 0


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

58 open finding(s); SC3 13, SC4 1, SC6 40, SC8 1, SC10 1, SC16 2

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:4617850e`: researcher message 2026-11-10T13:10 is too short to be matched; name where it is recorded: "proceed with 2437"
- **OPEN** `SC3:04cd98c0`: researcher message 2026-11-10T13:22 is in no escalation comment written this session: "add the detail of the md to a csv. I want to see the surface related to each phrase in particular, with all the other related data."
- **OPEN** `SC3:9303a93f`: researcher message 2026-11-10T13:25 is in no escalation comment written this session: "I do not see the surface in english in the csv"
- **OPEN** `SC3:f9880578`: researcher message 2026-11-10T15:49 is too short to be matched; name where it is recorded: "Approve all five"
- **OPEN** `SC3:bc225e63`: researcher message 2026-11-10T15:54 is too short to be matched; name where it is recorded: "Approve both"
- **OPEN** `SC3:73f88a9d`: researcher message 2026-11-10T15:56 is too short to be matched; name where it is recorded: "Approve closing"
- **OPEN** `SC3:0d92bc1d`: researcher message 2026-11-10T16:02 is too short to be matched; name where it is recorded: "Yes, confirm all"
- **OPEN** `SC3:2e14e80b`: researcher message 2026-11-10T16:13 is too short to be matched; name where it is recorded: "Approve closing"
- **OPEN** `SC3:e0e3da44`: researcher message 2026-11-10T16:19 is too short to be matched; name where it is recorded: "Approve all six"
- **OPEN** `SC3:44f21311`: researcher message 2026-11-10T16:25 is in no escalation comment written this session: "2448 approved.  2357 need you attention."
- **OPEN** `SC3:3428960c`: researcher message 2026-11-10T16:30 is too short to be matched; name where it is recorded: "Approve both"
- **OPEN** `SC3:734e7704`: researcher message 2026-11-10T16:33 is too short to be matched; name where it is recorded: "Approve as recommended"
- **OPEN** `SC3:484b04c2`: researcher message 2026-11-10T16:36 is in no escalation comment written this session: "session-close we will proceed with 2412 in a separate chat"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:3d10e445`: researcher message 2026-11-10T16:35 holds, defers or asks to check something; name its register item: "2448 is put on hold until 2412 is completed."

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
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
- **OPEN** `SC6:B:123`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (77a059b4-65ef-4409-8675-22c064cc23f7); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/ps/Collection-Build.ps1`: `iba/app/ps/Collection-Build.ps1` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

- **OPEN** `SC16:Escalation.ps1_-Action_Update`: Escalation.ps1 -Action Update failed 5 times this session: [31;1mEscalation.ps1: [0m; [31;1mMove-Item: [31;1mThe process cannot access the file because it is being used by another process.[0m; error: decision_required items may only move to approved from a CURRENT next_action of ready_for_approval -- no shortcut; escalation #2455 v2 -> state='re-assigned', next_action='ready_for_approval', assigned_to='Researcher'
- **OPEN** `SC16:Collection-Build.ps1`: Collection-Build.ps1 failed 2 times this session: /usr/bin/bash: -c: line 95: unexpected EOF while looking for matching `''; for lid, sh in pl["reshare"]:
