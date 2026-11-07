# Session close (#1875, rebuilt #2173)

> Generated 2026-11-07T04:35:29Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `d41a94c7-0638-41c1-9edf-a1bc3177d568` (CLAUDE_CODE_SESSION_ID); started 2026-11-06T17:46:11Z; window base commit `dd1f15b12cbd77e62d070f43697f54fd1cc6a7c0`
- compliance file: `Logs/compliance/COMPLIANCE-20261106-d41a94c7.md`; session log: `--`
- **open findings: 49**; cleared by disposition: 0


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

49 open finding(s); SC3 9, SC4 1, SC6 36, SC8 1, SC15 1, SC16 1

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:94207cd5`: researcher message 2026-11-06T17:46 is too short to be matched; name where it is recorded: "project-start"
- **OPEN** `SC3:2bf2dcaa`: researcher message 2026-11-06T18:31 is too short to be matched; name where it is recorded: "#2364 coherence"
- **OPEN** `SC3:fcc508a6`: researcher message 2026-11-06T18:52 is in no escalation comment written this session: "it looks like you in a mode to just roll things forward into another escalation rather that doing the work and resolving the escalation."
- **OPEN** `SC3:a2f9ccda`: researcher message 2026-11-06T18:56 is in no escalation comment written this session: "strange that you ask about the glossary - there should be configs about it to point you to the correct process and its destination. lets see if you can find it "
- **OPEN** `SC3:5f9dec1f`: researcher message 2026-11-06T18:59 is too short to be matched; name where it is recorded: "Yes, draft them"
- **OPEN** `SC3:b78a86c1`: researcher message 2026-11-07T04:05 is too short to be matched; name where it is recorded: "Yes, flag draft"
- **OPEN** `SC3:0d6253b6`: researcher message 2026-11-07T04:25 is too short to be matched; name where it is recorded: "Close #2361"
- **OPEN** `SC3:04c8d44e`: researcher message 2026-11-07T04:32 is in no escalation comment written this session: "supersede 2354, 2360 and 2359 with new escalations a) rebuild narrative (2354) b) assemble narration chapter scope (2360 and  2350)  all three these streams of "
- **OPEN** `SC3:90a8800a`: researcher message 2026-11-07T04:33 is in no escalation comment written this session: "2375 approved and ready for your action"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:636c3a16`: researcher message 2026-11-06T18:46 holds, defers or asks to check something; name its register item: "orphan settings: 1) whole cluster reading is still relevant, but the rules for it will change. setup a escalation for it, as it cannot be resolved now.  2) glos"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
- **OPEN** `SC6:G:governance.primary_responsibility`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
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

- **OPEN** `SC8:log`: no session log in Logs/ names this session (d41a94c7-0638-41c1-9edf-a1bc3177d568); write it (governance.session_log_required_content)

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

- **OPEN** `SC15:iba/app/USER-GUIDE.md:317:Prose.ps1`: `iba/app/USER-GUIDE.md` line 317 names `Prose.ps1`, which does not resolve

- **OPEN** `SC16:Config-Maintenance.ps1_-Step_Propose`: Config-Maintenance.ps1 -Step Propose failed 2 times this session: Propose needs -Title on a fresh call -- a short, title-shaped name for the change (<=60 chars, no '--'). -Question is th; work package : configuration-maintenance
