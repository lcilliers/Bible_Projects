# Session compliance -- 20261101 -- session 308b6ecc-0410-4861-af76-5db073cd98a1

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or clarification I meet goes into the escalation table, not just chat. | #2356 v2 and #2355 v3: the validate error and the build were recorded as escalations |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a registered routine can only be run by digging through history, treat that as missing config and escalate it. | not triggered: no registered routine needed past-precedent digging; iba/app/BUILD.md section 442 |
| G:governance.primary_responsibility | engaged | I own coding and integrity of project operations inside the IBA app, including back-filling outside ones. | iba/app/ps/Concept-Edit.ps1: the edit is coded and registered in the app |
| G:governance.programme_stages | not engaged | stage names only orient the work; no stage-specific task is set yet. |  |
| G:governance.project_change_rule | engaged | Any change of operation or method I make goes through the IBA app, not around it. | iba/app/ps/Concept-Edit.ps1: the change runs through the app, not around it |
| G:governance.project_operations | engaged | Defines project operations broadly (research, development, scripts); anything I run counts and falls under the app. | iba/app/BUILD.md section 442 |
| G:governance.rules_must_be_config_driven | engaged | No rule lives only in docs or memory; any rule I add or find needs a cfg_* row, deviations are escalated. | #2356 v2: rule B:123 linked in cfg_rule_scope; no rule added only in a document |
| G:governance.scope_iba_app | engaged | The IBA app is the central control for all operations; I work through it. | iba/app/ps/Concept-Edit.ps1 dispatches through run.py, work package concept-edit |
| G:governance.scope_project | engaged | Config scope is the whole project, so my changes consider all parts. | iba/app/BUILD.md section 442 |
| G:governance.study_status | engaged | Study is ACTIVE since 2026-10-23; this session builds the app, so I start no study work and run study work only via Reading.ps1 if asked. | no study work done: iba/app/BUILD.md section 442 |
| B:1 | engaged | Verify database state live before acting on it; never rely on remembered state. | iba/app/tools/temp_2355_concept_edit_test_run.py: live table state read before each change; iba/app/BUILD.md section 442 |
| B:2 | engaged | A step is done only when its output is confirmed to exist and to match. | iba/app/BUILD.md section 442: 35 of 35 checks on a copy, live List and three refusals read back |
| B:4 | engaged | Label LLM-derived claims inferential unless grounded in citable source data. | no model-derived claim made: iba/app/BUILD.md section 442 |
| B:10 | engaged | Never write, print or log the API key. | no key touched: iba/app/lib/conceptedit.py |
| B:16 | engaged | Never use AskUserQuestion; answer from DB/code or write a review file, plain-chat questions only where a rule allows. | AskUserQuestion not used; the permission question was asked in plain chat, see the conflicts section of this file |
| B:17 | engaged | For non-trivial work, state understanding, plan and files, then wait for approval; trivial steps exempt. | #2355 v3: understanding and approach stated before the build, approval recorded at v4 |
| B:18 | engaged | Substantive output goes to a .md file; chat carries alerts, summary and pointer only. | iba/app/BUILD.md section 442 and Logs/SESSION-LOG-20261101-concept-edit-tool.md hold the substance |
| B:19 | engaged | No guessing; where facts are missing I stop and ask in chat. | #2355 v3: the open points (link table scope, delete rule) were asked or stated, not guessed |
| B:20 | engaged | Flag cheaper paths (targeted reads, dry-run first, no needless subagents) before acting. | iba/app/tools/temp_2355_concept_edit_test_run.py: dry run then a copy, before the live change |
| B:21 | engaged | Any open item or judgement call raised in chat becomes an escalation in the same turn. | #2356 v2 and #2355 v3: items surfaced in chat were recorded the same turn |
| B:22 | engaged | Once a plan is approved I run it through without re-confirming each step. | #2355 v3: the approved scope was run through without re-confirming each step |
| B:23 | engaged | Investigations end with the fix implemented, verified and reported, unless scoped as investigation-only. | #2356 v2: the validate error was fixed and re-verified, not only reported |
| B:24 | engaged | Show actual query output and samples, and do not equate a structural check with fitness of values. | iba/app/BUILD.md section 442: the test results listed by check, with the refusal text |
| B:25 | engaged | Read-only commands need no permission; writes stay within the approved task. | read-only checks run without asking; every write stayed in the #2355 scope, iba/app/BUILD.md |
| B:27 | engaged | Multi-line strings in PowerShell use @'...'@, never Bash heredoc, in PowerShell calls. | no multi-line PowerShell string was needed; shell scripts used Bash syntax in Bash calls only |
| B:28 | engaged | A reported error is diagnosed and fixed or explained, never routed around. | iba/app/BUILD.md section 442: the copy-test failure (write-ahead log) was diagnosed and the copy method fixed, not routed around |
| B:31 | engaged | New guidance given this session is recorded the same session in a cfg_* row or owning document, not memory only. | #2355 v3: the researcher guidance of this session is quoted in the item |
| B:34 | engaged | Claims about project state or history cite the written record, not recollection. | #2355 v3: claims cite the record, with files in the context |
| B:36 | engaged | No superlatives unless every candidate was checked. | no superlative claims written: iba/app/BUILD.md section 442 |
| B:40 | engaged | Every open item found anywhere is recorded in escalation, not silently fixed or buried in a report. | #2356 v2 and #2355 v3: findings went into the escalation table |
| B:44 | engaged | A new decision point is terminal: record it as an open item and route to design, do not answer inline. | iba/app/lib/conceptedit.py: deleting a domain that holds live concepts is refused, not decided inline |
| B:83 | engaged | Only C:\Bible_study_projects is authoritative; other copies are ignored. | all work under the project root; iba/app/BUILD.md section 442 |
| B:97 | engaged | Developer Mode is only for adjusting the app's controls; each new task is checked against that boundary and only the configmaint.propose gate is bypassed. | #2355 v3: the task was checked against the Developer Mode boundary (schema and app build) |
| B:98 | engaged | Deviations from a settled standard are fixed at once, not offered as questions. | #2356 v2: the missing rule link was fixed at once, not asked about |
| B:99 | engaged | Read each instruction against the whole conversation, not just the last message. | #2355 v3: the three researcher instructions are read together and quoted |
| B:100 | engaged | Show codes with names and glosses, never bare; descriptive names in design docs. | iba/app/USER-GUIDE.md section 8.7: the actions and fields are named, no bare codes |
| B:101 | engaged | When the researcher must run a command, give the full ready-to-run PowerShell in chat. | iba/app/USER-GUIDE.md section 8.7: complete ready-to-run PowerShell commands |
| B:102 | engaged | Reports state checked facts only, with context, concise, limits and open items stated. | iba/app/BUILD.md section 442: checked facts with their context, the limits under Not done |
| B:105 | engaged | Diagnosing a gap does not authorise building the fix; designs go to the researcher as decision_required first. | #2355 v3: the cascade on delete was left as a refusal for the researcher to decide; the build followed the researcher instruction |
| B:114 | not engaged | study synthesis rule; no study work in this session. |  |
| B:116 | not engaged | study reading rule; no study work in this session. |  |
| B:123 | engaged | Before using a table or column, read its recorded meaning (cfg_table.use, cfg_column) and name it in my first message on that work. | iba/app/migration/archive/add_concept_descriptions_2355_v1_20261101.py: cfg_table and cfg_column meaning read first |
| E:4 | engaged | Open items assigned to Claude come before other work; I list them at start and the researcher decides order. | #2356 v2: the item assigned to Claude was resolved; #2354 is acknowledged in Logs/SESSION-LOG-20261101-concept-edit-tool.md |
| E:5 | engaged | Actions arising from chat are recorded in escalations, optionally via a planning document. | #2355 v3: the chat actions are recorded in the escalation |

## Conflicts and rules not followed

- B:16: the dev-mode declaration asks me to ask the researcher to confirm permissions; I do that in plain chat, not AskUserQuestion, which stays denied.

## Close dispositions

- SC3:015334bf :: no record needed: a one-word confirmation of the permission mode, answered in chat and stated in the developer-mode report
- SC3:5ad035e9 :: recorded in #2355 v4
- SC16:Config-Maintenance.ps1_-Step_Validate :: fixed: both runs reported real findings (rule B:123 without a scope link, #2356 v2; two utility modules without a config exemption, set in cfg_utility); the next run reported no new findings

