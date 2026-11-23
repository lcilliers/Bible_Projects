# Session close (#1875, rebuilt #2173)

> Generated 2026-11-23T11:20:08Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `75860879-bfa6-45ce-834d-0a11cbae93a6` (CLAUDE_CODE_SESSION_ID); started 2026-11-23T04:13:54Z; window base commit `217c02032f3f588aec546b853d3fe810967dc099`
- compliance file: `Logs/compliance/COMPLIANCE-20261123-75860879.md`; session log: `--`
- **open findings: 78**; cleared by disposition: 0


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

78 open finding(s); SC3 29, SC4 3, SC6 41, SC8 1, SC10 3, SC16 1

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:e271abbf`: researcher message 2026-11-23T04:22 is in no escalation comment written this session: "locate the reporting method that output the collection's base data"
- **OPEN** `SC3:90e6be40`: researcher message 2026-11-23T04:30 is in no escalation comment written this session: "the evidence report runs for an extended time without generating the report.  I assume this collection-build is not a reporting tool but is trying to build and "
- **OPEN** `SC3:714c41f0`: researcher message 2026-11-23T04:31 is in no escalation comment written this session: "iba\app\ps\Collection-Build.ps1 -Action Evidence -Collection thought"
- **OPEN** `SC3:9bcb632c`: researcher message 2026-11-23T04:42 is in no escalation comment written this session: "yes, make the fix and test it on thought"
- **OPEN** `SC3:22b1a6af`: researcher message 2026-11-23T04:58 is in no escalation comment written this session: "locate the report that provides an overview of collections"
- **OPEN** `SC3:151179d8`: researcher message 2026-11-23T05:05 is in no escalation comment written this session: "action export is sufficient for my purposes for now. no further action needed for this request"
- **OPEN** `SC3:ccfab835`: researcher message 2026-11-23T05:12 is in no escalation comment written this session: "using "C:\Bible_study_projects\_analytics\surfaces\exports\collections-v3-20261123.csv" only - produce a network diagram based on the base column for words that"
- **OPEN** `SC3:eb0ac828`: researcher message 2026-11-23T05:12 is too short to be matched; name where it is recorded: "core"
- **OPEN** `SC3:b5ff585e`: researcher message 2026-11-23T05:54 is in no escalation comment written this session: "do a network diagram with these words as focus, and the cluster to collections and the associations of the core column with it"
- **OPEN** `SC3:5d8c01a5`: researcher message 2026-11-23T06:02 is in no escalation comment written this session: "for you information, you associating temperance with self-control is fine.  I take it that your network diagrams does not have all the collections on the sheet."
- **OPEN** `SC3:7a5eda90`: researcher message 2026-11-23T06:04 is in no escalation comment written this session: "can you add all the collections in the second diagram, the associations you build in the first diagram should help to make the links"
- **OPEN** `SC3:3056a987`: researcher message 2026-11-23T06:11 is in no escalation comment written this session: "this is a very telling picture.  I still need to think through the implications, but it certainly paints a very different picture of the how to inner being work"
- **OPEN** `SC3:c574e0e8`: researcher message 2026-11-23T07:41 is in no escalation comment written this session: "look back into the rules of collection building then motivate why the following collections are not in one collection: stumble, change, astray,turn, return, rep"
- **OPEN** `SC3:a9c3326e`: researcher message 2026-11-23T07:08 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:2f52fd90`: researcher message 2026-11-23T07:49 is in no escalation comment written this session: "noted. no action for you on this.    can you convert the data behind the two diagrams in 2425 into a excel spreadsheet."
- **OPEN** `SC3:697401e3`: researcher message 2026-11-23T09:14 is in no escalation comment written this session: "what is the scientific basis you are using to do the pairing"
- **OPEN** `SC3:6c31d9fd`: researcher message 2026-11-23T09:16 is in no escalation comment written this session: "are there any open source english dictionary"
- **OPEN** `SC3:4c3e6cc8`: researcher message 2026-11-23T09:18 is in no escalation comment written this session: "how is wordnet used?"
- **OPEN** `SC3:03adacf7`: researcher message 2026-11-23T09:26 is in no escalation comment written this session: "I am envisaging you take each surface work, and list each other surface word that is paired by wordnet. this process should not introduce new words but only wor"
- **OPEN** `SC3:a37dcb36`: researcher message 2026-11-23T09:31 is in no escalation comment written this session: "yes, download it, single words only"
- **OPEN** `SC3:493b4f6e`: researcher message 2026-11-23T09:52 is in no escalation comment written this session: "add wordnet as a plugin for the project, dont leave it in the scratch pad.  part of the intent is to pull words with the same base together, so do not put them "
- **OPEN** `SC3:bb93895d`: researcher message 2026-11-23T10:11 is in no escalation comment written this session: "there are a number of words I can spot that is not pairing because they actually do not belong in the list, they should have been defined as another surface gro"
- **OPEN** `SC3:a70cd5bb`: researcher message 2026-11-23T10:17 is in no escalation comment written this session: "add the missing relations and rebuild the diagram and matrices"
- **OPEN** `SC3:3adda1ac`: researcher message 2026-11-23T10:27 is in no escalation comment written this session: "I do not understand group 1"
- **OPEN** `SC3:69767756`: researcher message 2026-11-23T10:42 is in no escalation comment written this session: "why is certainty not binding with certain. fickle not with mislead.   I think you need to critically work through the pairs = 0 list and determine a) are they c"
- **OPEN** `SC3:255ef038`: researcher message 2026-11-23T10:52 is in no escalation comment written this session: "add a column in the excel to quantify/separate the items that will need manual intervention (e.g. reallocate surface to other; need decision, conflicitng sense,"
- **OPEN** `SC3:b1475d4d`: researcher message 2026-11-23T11:09 is in no escalation comment written this session: "the surface grouping has 86 groups + 1 odds and ends group.  Why would these groupings not be the collections.  what does the old collections do that the surfac"
- **OPEN** `SC3:db1a3061`: researcher message 2026-11-23T11:18 is in no escalation comment written this session: "group 1 is ignored - it is actually most of the surfaces. and the 154 will be dealt with manually. so 85 groups. you answered me with a list of objections witho"
- **OPEN** `SC3:cfa4ff03`: researcher message 2026-11-23T11:19 is in no escalation comment written this session: "you can do a session close."

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:c2477cf3`: researcher message 2026-11-23T04:21 holds, defers or asks to check something; name its register item: "Park #2538, #2541 #2542 #2543 for now"
- **OPEN** `SC4b:a9c3326e`: researcher message 2026-11-23T07:08 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC4b:255ef038`: researcher message 2026-11-23T10:52 holds, defers or asks to check something; name its register item: "add a column in the excel to quantify/separate the items that will need manual intervention (e.g. reallocate surface to other; need decision, conflicitng sense,"

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
- **OPEN** `SC6:B:123`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (75860879-bfa6-45ce-834d-0a11cbae93a6); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/tools/temp_2545_core_word_network.py`: `iba/app/tools/temp_2545_core_word_network.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2545_focus_words_network.py`: `iba/app/tools/temp_2545_focus_words_network.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2545_wordnet_surface_pairs.py`: `iba/app/tools/temp_2545_wordnet_surface_pairs.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

- **OPEN** `SC16:Escalation.ps1_-Action_Raise`: Escalation.ps1 -Action Raise failed 3 times this session: error: short_description is 61 chars, over the 60-char title limit. It must read like a title/subject naming the topic -

_no finding_
