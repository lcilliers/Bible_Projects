# Session close (#1875, rebuilt #2173)

> Generated 2026-11-26T07:19:11Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `760131f7-a5d4-44b5-92a0-7c28ca0a4683` (CLAUDE_CODE_SESSION_ID); started 2026-11-25T16:27:19Z; window base commit `cbd46aa8dcb46fb95e5ee10283311450498641a6`
- compliance file: `Logs/compliance/COMPLIANCE-20261125-760131f7.md`; session log: `--`
- **open findings: 80**; cleared by disposition: 0


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

80 open finding(s); SC3 15, SC4 3, SC6 35, SC8 1, SC10 16, SC15 1, SC16 7, SC17 2

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:38b4ad81`: researcher message 2026-11-25T16:31 is too short to be matched; name where it is recorded: "proceed with 2538"
- **OPEN** `SC3:5cdbd3c9`: researcher message 2026-11-25T18:08 is too short to be matched; name where it is recorded: "Approve, build ReadWords"
- **OPEN** `SC3:8ccfdc30`: researcher message 2026-11-25T19:27 is too short to be matched; name where it is recorded: "Approve #2560"
- **OPEN** `SC3:a3cc2902`: researcher message 2026-11-25T19:13 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:7ab57526`: researcher message 2026-11-25T20:46 is too short to be matched; name where it is recorded: "Approve, apply live"
- **OPEN** `SC3:8bd33e0a`: researcher message 2026-11-26T04:16 is too short to be matched; name where it is recorded: "Approve, apply live"
- **OPEN** `SC3:807110f6`: researcher message 2026-11-26T04:24 is too short to be matched; name where it is recorded: "Approve #2565"
- **OPEN** `SC3:9f79b12d`: researcher message 2026-11-26T04:28 is too short to be matched; name where it is recorded: "Approve, apply live"
- **OPEN** `SC3:f7f15649`: researcher message 2026-11-26T04:31 is too short to be matched; name where it is recorded: "Approve #2568"
- **OPEN** `SC3:a150c851`: researcher message 2026-11-26T04:39 is too short to be matched; name where it is recorded: "Approve, apply live"
- **OPEN** `SC3:9e756be8`: researcher message 2026-11-26T05:07 is too short to be matched; name where it is recorded: "Approve, apply live"
- **OPEN** `SC3:b93e0dc4`: researcher message 2026-11-26T05:14 is too short to be matched; name where it is recorded: "Build ReadElements"
- **OPEN** `SC3:d434d501`: researcher message 2026-11-26T05:22 is too short to be matched; name where it is recorded: "Approve, apply live"
- **OPEN** `SC3:a0700d87`: researcher message 2026-11-26T05:49 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:c849bb38`: researcher message 2026-11-26T07:07 is too short to be matched; name where it is recorded: "Approve, apply live"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:60449823`: researcher message 2026-11-25T17:49 holds, defers or asks to check something; name its register item: "my biggest problem is that you have time and time again ran away with processes that runs for a long time without a check, that you can scans that should take s"
- **OPEN** `SC4b:a3cc2902`: researcher message 2026-11-25T19:13 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:a0700d87`: researcher message 2026-11-26T05:49 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


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
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_operations`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_iba_app`: engaged, with no evidence
- **OPEN** `SC6:G:governance.scope_project`: engaged, with no evidence
- **OPEN** `SC6:G:governance.study_status`: engaged, with no evidence
- **OPEN** `SC6:B:1`: engaged, with no evidence
- **OPEN** `SC6:B:2`: engaged, with no evidence
- **OPEN** `SC6:B:4`: evidence does not check: file outputs/escalation/2538-one-command-what-code-computes-and-the-reader-v1-20261125.md does not exist
- **OPEN** `SC6:B:10`: engaged, with no evidence
- **OPEN** `SC6:B:16`: engaged, with no evidence
- **OPEN** `SC6:B:18`: evidence does not check: file outputs/escalation/2538-one-command-what-code-computes-and-the-reader-v1-20261125.md does not exist
- **OPEN** `SC6:B:19`: engaged, with no evidence
- **OPEN** `SC6:B:20`: engaged, with no evidence
- **OPEN** `SC6:B:21`: engaged, with no evidence
- **OPEN** `SC6:B:22`: engaged, with no evidence
- **OPEN** `SC6:B:23`: engaged, with no evidence
- **OPEN** `SC6:B:24`: evidence does not check: file outputs/escalation/2538-one-command-what-code-computes-and-the-reader-v1-20261125.md does not exist
- **OPEN** `SC6:B:25`: engaged, with no evidence
- **OPEN** `SC6:B:27`: engaged, with no evidence
- **OPEN** `SC6:B:28`: engaged, with no evidence
- **OPEN** `SC6:B:31`: engaged, with no evidence
- **OPEN** `SC6:B:34`: evidence does not check: file outputs/escalation/2538-one-command-what-code-computes-and-the-reader-v1-20261125.md does not exist
- **OPEN** `SC6:B:34`: evidence does not check: commit 43742f37 does not exist
- **OPEN** `SC6:B:36`: engaged, with no evidence
- **OPEN** `SC6:B:40`: engaged, with no evidence
- **OPEN** `SC6:B:83`: engaged, with no evidence
- **OPEN** `SC6:B:98`: engaged, with no evidence
- **OPEN** `SC6:B:100`: engaged, with no evidence
- **OPEN** `SC6:B:101`: engaged, with no evidence
- **OPEN** `SC6:B:102`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (760131f7-a5d4-44b5-92a0-7c28ca0a4683); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/handlers/collectionbuild.py`: `iba/app/handlers/collectionbuild.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/collectionvalidate.py`: `iba/app/lib/collectionvalidate.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/layerloop.py`: `iba/app/lib/layerloop.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/layerreading.py`: `iba/app/lib/layerreading.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/lexicalalignment.py`: `iba/app/lib/lexicalalignment.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/strandreading.py`: `iba/app/lib/strandreading.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/elementscap_2538_v1_20261126.py`: `iba/app/migration/archive/elementscap_2538_v1_20261126.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/Collection-Build.ps1`: `iba/app/ps/Collection-Build.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2509_grouping_test_run.py`: `iba/app/tools/temp_2509_grouping_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_elements_test_run.py`: `iba/app/tools/temp_2538_elements_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_gates_test_run.py`: `iba/app/tools/temp_2538_gates_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_loop_order_test_run.py`: `iba/app/tools/temp_2538_loop_order_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_readenrichment_test_run.py`: `iba/app/tools/temp_2538_readenrichment_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_readsenses_test_run.py`: `iba/app/tools/temp_2538_readsenses_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_readstructure_test_run.py`: `iba/app/tools/temp_2538_readstructure_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2538_readwords_test_run.py`: `iba/app/tools/temp_2538_readwords_test_run.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

- **OPEN** `SC15:iba/app/USER-GUIDE.md:980:outputs/escalation/2538-read-commands-design-v1-20261125.md`: `iba/app/USER-GUIDE.md` line 980 names `outputs/escalation/2538-read-commands-design-v1-20261125.md`, which does not resolve

- **OPEN** `SC16:Bash:_cd:e29939cc`: Bash: cd failed 4 times this session: /usr/bin/bash: -c: line 108: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 46: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 57: unexpected EOF while looking for matching `''; /usr/bin/bash: -c: line 73: unexpected EOF while looking for matching `''
- **OPEN** `SC16:Escalation.ps1_-Action_ResolveSelfCorrectable`: Escalation.ps1 -Action ResolveSelfCorrectable failed 2 times this session: [31;1mInvoke-Expression: [31;1mMissing argument in parameter list.[0m; ResolveSelfCorrectable needs -Id and -Resolution (what was wrong, what changed).
- **OPEN** `SC16:Collection-Build.ps1_-Action_ReadEnrichment`: Collection-Build.ps1 -Action ReadEnrichment failed 2 times this session: work package : collection-build
- **OPEN** `SC16:Collection-Build.ps1_-Action_RecordStructure`: Collection-Build.ps1 -Action RecordStructure failed 18 times this session: work package : collection-build
- **OPEN** `SC16:Collection-Build.ps1_-Action_RecordElements`: Collection-Build.ps1 -Action RecordElements failed 5 times this session: work package : collection-build
- **OPEN** `SC16:step.ps1`: step.ps1 failed 13 times this session: 12291 key-statement -> defer die inner_being | Death named inside a living person.; 12895 face -> defer evildoer evidence | Face of aph (H0639), The face lifted in pride: The face/nose raised (Psa 10:4 ("; 13006 statement -> defer destruction inner_being | The one who carries it out: "Woe to Assyria, the rod of my anger … bu; 13139 link -> defer heart inner_being | Sequence in Isa 9:8–10:7: pride in rebuilding → struck → "did not turn" → leader; 16492 statement -> defer heart inner_being | 13. Cross-cutting observations for Batch E [Claude reading]: Unclean spirit; 18226 statement -> defer trust inner_being | 2Ch 32:11 | "Is not Hezekiah misleading you …?" with "On what are you trust; 1928 tightly-related -> defer thank inner_being | G2168 (thanksgiving withheld) co-occurs with knowledge (M15, G1097), h; step         : collection.record_structure
- **OPEN** `SC16:evstep.ps1`: evstep.ps1 failed 2 times this session: step         : collection.record_evidence

- **OPEN** `SC17:layer_reading_setting`: the stages or layers of the collection reading changed, and `iba/docs/project-map.md` did not change: cfg_setting update layer.reading
- **OPEN** `SC17:mechanism_task_completed`: a task completed that BUILD.md names as built this session, and `iba/docs/project-map.md` did not change: #2560 Run two archived migrations on a test copy (#2538); #2565 Run archived senses migration on a test copy
