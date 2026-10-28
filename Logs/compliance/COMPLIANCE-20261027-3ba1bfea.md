# Session compliance -- 20261027 -- session 3ba1bfea-7b08-4bf4-b97f-9ab0f5edfb0a

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything open, odd or unclear that I meet this session goes into the escalation table, not only chat. | #2327 v1 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a registered routine cannot be run from live cfg rows and I find myself digging through history to work out the step, I stop and report the config gap. | #2328 v1 |
| G:governance.primary_responsibility | not engaged | No app coding or back-filling is in hand at startup; it applies if the researcher asks for app work. |  |
| G:governance.programme_stages | not engaged | Background description of the three stages; no stage work is in hand at startup. |  |
| G:governance.project_change_rule | engaged | Any change of method I might propose goes through the IBA app, and old out-of-app operations get migrated rather than run ad hoc. | #2328 v1 |
| G:governance.project_operations | not engaged | Definition only; it sets no action for startup. |  |
| G:governance.rules_must_be_config_driven | engaged | On a new instruction I first check that its governing rules exist as cfg rows; a rule living only in a document or memory gets escalated. | #2323 v12 |
| G:governance.scope_iba_app | engaged | Operations are run through the IBA app tools, not by hand outside it. | _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking-batch-times-v1-20261028.md |
| G:governance.scope_project | not engaged | Scope statement only; no action at startup. |  |
| G:governance.study_status | engaged | Study is ACTIVE since 2026-10-23; any study work goes through Reading.ps1 and its three gates, and the strand steps are retired. | #2320 v22 |
| B:1 | engaged | Before relying on database state I query the live database, never earlier reports. | #2301 v11 |
| B:2 | engaged | I confirm each output file or write exists and is right before calling a step done; the compliance file is checked by its Check command. | #2327 v1 |
| B:4 | engaged | Anything I or a subagent produce without source grounding is labelled inferential. | #2320 v13 |
| B:10 | not engaged | No API key was used or printed in this session. |  |
| B:16 | engaged | I never use AskUserQuestion; questions go in plain chat or a review file. | .claude/settings.json |
| B:17 | engaged | For non-trivial work I summarise my understanding and plan, then wait for approval; at startup I ask what to work on. | #2320 v14 |
| B:18 | engaged | Substantive output goes into a md file with chat carrying a short pointer; the startup report is brief findings only. | _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking-batch-times-v1-20261028.md |
| B:19 | engaged | I work only from verified facts and ask in plain chat when something is missing. | #2328 v1 |
| B:20 | engaged | I flag a cheaper path, such as targeted queries over whole-file reads, before acting. | #2320 v22 |
| B:21 | engaged | Any open item or judgement call raised in chat is recorded as an escalation in the same turn. | #2328 v1 |
| B:22 | engaged | Once a plan is approved I run it through without re-confirming each step. | #2320 v16 |
| B:23 | engaged | A requested investigation ends with the fix implemented and verified, unless scoped as investigation only. | #2301 v11 |
| B:24 | engaged | I show actual query output and sample data, not smoothed summaries. | #2323 v12 |
| B:25 | engaged | Read-only checks run without asking permission. | #2301 v11 |
| B:27 | not engaged | No multi-line command argument was written; the PowerShell tool ran single commands and Python came from the Bash tool. |  |
| B:28 | engaged | A pasted error from the researcher is diagnosed and fixed, not routed around. | #2327 v1 |
| B:31 | engaged | New guidance from the researcher is recorded in the cfg row or owning document the same session, not only in memory. | #2325 v2 |
| B:34 | engaged | Claims about project state or past decisions cite the written record. | #2323 v12 |
| B:36 | engaged | I write no superlative unless every candidate was checked. | #2320 v17 |
| B:40 | engaged | Open items found anywhere, including in checks, go into the escalation table. | #2327 v1 |
| B:44 | engaged | A point needing a new decision is recorded as open and sent back to design, not answered inline; slips against settled design I fix directly. | #2327 v1 |
| B:83 | engaged | Only C:\Bible_study_projects is authoritative; files elsewhere are used only when named and then brought in with approval. | _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking.json |
| B:98 | engaged | Deviations from an established standard are fixed at once, not offered as a question. | #2323 v12 |
| B:99 | engaged | When the researcher answers my startup question, I weigh the answer together with everything said earlier in this session before acting on it. | #2320 v22 |
| B:100 | engaged | Codes are always shown with their names or glosses. | _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking-batch-times-v1-20261028.md |
| B:101 | not engaged | The researcher was not asked to run a command this session. |  |
| B:102 | engaged | Status reports state checked facts only, with context, concise, limits stated. | _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking-batch-times-v1-20261028.md |
| B:105 | engaged | Diagnosing a gap is not leave to build the fix; designs go to the researcher as decision_required first. | #2327 v1 |
| B:114 | not engaged | No study synergy or narrative work is in hand at startup; it applies when a reading is worked. |  |
| B:116 | not engaged | No verse reading is in hand at startup; when one begins I read the verse first. |  |
| E:4 | engaged | Open escalations assigned to Claude are addressed before other work; I name them first in the report. | #2301 v11 |
| E:5 | engaged | Chat items and researcher feedback tied to escalations are captured in one with verbatim quotes in the same turn. | #2320 v22 |

## Conflicts and rules not followed

None.

## Close dispositions

- SC3:34f4ce8a :: recorded in #2320 v14
- SC3:20b08089 :: recorded in #2320 v16
- SC3:b9040bac :: recorded in #2305 v23
- SC3:dde7b771 :: no record needed: it is the command that starts this close
- SC3:5b61c6c5 :: recorded in #2320 v23
- SC3:a5cb8a08 :: recorded in #2320 v23
- SC4b:9b605790 :: in register #2315
- SC4b:0204a808 :: not held: recorded as the approval on #2320 and acted on in the same turn
- SC4b:d64159df :: not held: acted on in the same turn (#2301 closed, v11)
- SC16:Escalation.ps1_-Action_Update :: carried #2320

