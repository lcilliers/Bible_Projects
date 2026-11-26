# Session compliance -- 20261126 -- session 1dc61df3-3564-4325-94ae-0a36c7540ce9

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Any open item, anomaly or question found while building goes into the escalation table through Escalation.ps1, not only into chat. || every item of the session on #2637 v4 to v10 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a build task makes me dig through BUILD.md, old logs or archived outputs to learn how a routine runs, the missing step or setting is raised as its own item. || the routines needing hand work were raised as the build of #2637 v5 (outputs/escalation/2637-build-plan-v3-20261126.md) |
| G:governance.primary_responsibility | engaged | I own the app code and its integrity; anything I build this session is built into the IBA app, not beside it. || #2637 v9: the failure trapping built into iba/app/handlers/collectionbuild.py |
| G:governance.programme_stages | engaged | Any app change I make is placed against the stage it serves (base data, analysis stages 1-5, publishing), and stage 5 claim formulation stays undecided. || the build is placed on stages 1 to 4 (grouping to 3.2) in outputs/escalation/2637-build-plan-v3-20261126.md |
| G:governance.project_change_rule | engaged | A change of method is made through cfg rows and app code, never as a side process, even with the approval gate lifted. || the method change made through cfg rows and code: iba/app/migration/archive/encode_2637_failure_log_v1_20261126.py |
| G:governance.project_operations | engaged | Builds, scripts, migrations and tests in this session are project operations and fall under every rule here. || the migrations and tests ran as project operations: iba/app/migration/archive/encode_2637_done_test_v1_20261126.py |
| G:governance.rules_must_be_config_driven | engaged | A rule I build into code is held in a cfg row and read from it; a rule found only in a document or memory is escalated. || the done-test held as cfg_behaviour_rule 138 (iba/app/migration/archive/encode_2637_done_test_v1_20261126.py); refusal routing in cfg_on_fail |
| G:governance.scope_iba_app | engaged | Operations run through the app tools and run.py dispatch; any new hand-run module gets a PS entry point. || operations through Compliance.ps1, Escalation.ps1 and registered migrations; #2637 v9 |
| G:governance.scope_project | engaged | A gap found anywhere in the project while building is in scope for config and escalation. || the gap across every read routine taken into config scope: outputs/escalation/2637-build-plan-v3-20261126.md |
| G:governance.study_status | engaged | The study is active, but this is a Developer Mode session, so I do no study readings here; study work belongs in a standard session through Reading.ps1. || no study work done in this Developer Mode session; #2620 left for the standard session (#2637 v6) |
| B:1 | engaged | Before any build step that depends on a count, flag or row, I query the live iba.db first, never the last session log or memory. || live counts queried before use: the refusal history of outputs/escalation/2637-known-failures-catalogue-v1-20261126.md |
| B:2 | engaged | I report a build step done only after checking its file, row, test output or report exists with the expected content. || the rule row, the table and the routing read back after each apply; iba/app/tools/temp_2637_failure_log_test_run.py 11 of 11 |
| B:4 | engaged | Any conclusion I or a subagent reach without a direct source in code or data is labelled inferential. || the realism limit and the B2 reading stated as such in outputs/escalation/2637-build-plan-v3-20261126.md |
| B:10 | engaged | The API key value never appears in my output, logs, escalations or commits. || no key handled in this session; nothing in iba/app/BUILD.md entries 598 and 599 names one |
| B:16 | engaged | I do not use AskUserQuestion; I look facts up, put a real judgement call in a .md review file, and ask one simple question in plain chat. || no AskUserQuestion used; the G3 decision asked in chat and recorded on #2637 v7 |
| B:17 | engaged | Before the non-trivial build the researcher names after this declaration, I state the plan, scope and files and wait for approval. || #2637 v5 plan sent for approval before the build; approved #2637 v7 |
| B:18 | engaged | Substantive results go to a .md file or the app report files first, with a short chat summary and pointer. || results written to outputs/escalation/2637-build-plan-v3-20261126.md and outputs/escalation/2637-known-failures-catalogue-v1-20261126.md first |
| B:19 | engaged | If a fact needed for a build is missing, I stop and ask rather than assume. || the G3 decision was asked, not assumed: #2637 v6 |
| B:20 | engaged | I point out a cheaper route where one exists, such as a targeted query, a dry run or a test on a copy before a live run. || #2637 v10: the cheaper route for X4 (a config map and a scan in place of hand edits) and a fresh session for it |
| B:21 | engaged | Any open item raised in chat today is recorded as an escalation in the same turn. || each researcher message recorded on #2637 v4, v5, v7 and v11 |
| B:22 | engaged | Once a build plan is approved I run it to the end without re-asking at each step. || #2637 v8 to v9: the approved plan built without re-asking at each step |
| B:23 | engaged | For a fix task I implement, test on a copy and report the verified result, not just the finding. || the failure trapping built and tested, not only found: iba/app/tools/temp_2637_failure_log_test_run.py |
| B:24 | engaged | When I report database state I show the query and rows, and keep a structural pass apart from fitness for use. || the queries shown with their rows in outputs/escalation/2637-known-failures-catalogue-v1-20261126.md |
| B:25 | engaged | Read-only checks run without asking; writes to the db or code stay inside an approved task. || writes made only inside the approved #2637 (v7); reads ran freely |
| B:27 | engaged | Multi-line arguments in PowerShell commands use here-strings, not bash heredocs. || the multi-line escalation comments of #2637 v4 to v10 passed as PowerShell here-strings |
| B:28 | engaged | If the researcher pastes an error, I diagnose and fix that error rather than route around it. || no error pasted by the researcher this session; the tool-layer errors met were fixed at once (iba/app/BUILD.md entry 599) |
| B:31 | engaged | Guidance or corrections given today are written into a cfg row or the owning document in this session. || the researcher guidance written to cfg_behaviour_rule 138 and the G3 decision to #2637 v7 |
| B:34 | engaged | Statements about history or state cite the file, table row or commit they come from. || statements cite rows and files: outputs/escalation/2637-known-failures-catalogue-v1-20261126.md |
| B:36 | engaged | No superlative unless every candidate has been checked. || no superlative used without checking every case; the class counts in outputs/escalation/2637-known-failures-catalogue-v1-20261126.md are complete counts |
| B:40 | engaged | Findings from tests, validation runs or reviews become escalation rows, not silent fixes. || test findings recorded on #2637 v9; iba/app/tools/temp_2637_failure_log_test_run.py |
| B:44 | engaged | A point needing a new decision stops the work and becomes an open item; only my own slips against a settled design are fixed directly and recorded. || B2 and C4 settled from config, G3 stopped for the researcher: #2637 v6 |
| B:83 | engaged | I work only from C:\Bible_study_projects; outside files are used only if the researcher names them and they are brought in with approval. || every file of the session under C:/Bible_study_projects: outputs/escalation/2637-build-plan-v3-20261126.md |
| B:97 | engaged | Each task in this session is checked against the Developer Mode boundary; only the configmaint.propose per-row gate is lifted; each task has an escalation, is tested on a copy_db copy with the result on its escalation, has a named snapshot before migrations or bulk changes, and every cfg write goes through apply_logged; every reply opens with the banner. || each migration tested on a copy_db copy then applied under a named snapshot through apply_logged; iba/app/tools/temp_2637_failure_log_test_run.py; banner on every reply |
| B:98 | engaged | Where work departs from an established standard I conform it at once without asking. || C4 conformed to the instruction without asking: #2637 v6 |
| B:99 | engaged | I read each instruction against the whole conversation and the escalation record and do not ask what the record already answers. || B2 answered from GP-01 and GP-04 rather than asked: #2637 v6 |
| B:100 | engaged | Codes I show (steps, packages, collections, Strongs) carry their names or glosses. || rule and step codes named with their meaning in outputs/escalation/2637-build-plan-v3-20261126.md |
| B:101 | engaged | Any command the researcher is to run is given as a complete PowerShell line in chat. || no command was given to the researcher to run this session; the close commands are run by Claude (#2637 v10) |
| B:102 | engaged | This declaration and later status reports state only checked facts with context and limits, and no bare numbers. || counts reported with their source: 68 failures, 11 classes, 557 fragments (#2637 v10) |
| B:105 | engaged | A gap I diagnose that is not the named task goes to the researcher as decision_required with a design; I do not build it in the same pass. || #2637 v10: X4 sized and designed, not built in the same pass |
| B:114 | not engaged | No study work in a Developer Mode session, so no claims or narrative are written. |  |
| B:116 | not engaged | No study work in a Developer Mode session, so no verse is read for a ruling. |  |
| B:123 | engaged | Before using a table or column in a build or count, I read its cfg_table and cfg_column meaning and name it in my first message on that work. || cfg_table and cfg_column of escalation and collection_layer_item read before use; read_failure registered with its use text (iba/app/migration/archive/encode_2637_failure_log_v1_20261126.py) |
| B:124 | not engaged | No Ollama or outside-service routine is planned at this start; if one is built or run, I read its cfg settings and check the service first. |  |
| B:125 | not engaged | No long-running job is planned at this start; if one is needed it runs through Win32_Process Create with a log under Logs/. |  |
| B:127 | not engaged | No collection is worked in a Developer Mode session. |  |
| B:129 | engaged | If a build touches collection membership, it follows the one-surface-one-collection rule and change procedure, on a copy, under a snapshot, with counts predicted and checked. || not touched: the build changed the refusal routing only (iba/app/BUILD.md entry 599), no reading code of this step |
| B:130 | engaged | If a build writes or repairs nodes, they carry all indexing columns and their collection, tied to a live observation, with withdrawals as soft deletes with a reason. || not touched: the build changed the refusal routing only (iba/app/BUILD.md entry 599), no reading code of this step |
| B:131 | not engaged | No observations are recorded in a Developer Mode session. |  |
| B:132 | engaged | Any change to the collection-reading code keeps the stage and step order (grouping, S1, 1.1, 1.2, 2.1, 3.1 per subgroup, 3.2, 3.3) with each step closed before the next. || not touched: the build changed the refusal routing only (iba/app/BUILD.md entry 599), no reading code of this step |
| B:133 | engaged | Any change to the reading code keeps lexical reading and inner-being analysis in separate processes, with the inner-being layer opening only after evidence passes. || not touched: the build changed the refusal routing only (iba/app/BUILD.md entry 599), no reading code of this step |
| B:134 | engaged | Any change to the layer code keeps every collection_layer_item aspect closed by an observation or a permitted none. || not touched: the build changed the refusal routing only (iba/app/BUILD.md entry 599), no reading code of this step |
| B:136 | engaged | Any change to post-stage-4 validation keeps evidence first and inner being second, repair before delete, each finding acted on or deferred to a named collection. || not touched: the build changed the refusal routing only (iba/app/BUILD.md entry 599), no reading code of this step |
| B:137 | engaged | Anything done outside the package methods today is encoded back into package code or config before the work is called done. || the session interventions encoded as config and code: outputs/escalation/2637-build-plan-v3-20261126.md and iba/app/handlers/collectionbuild.py |
| B:138 | engaged | No routine of the read package up to 3.2 is called complete until a subgroup not read before runs from first command to gate on a copy with only the packets and package commands, no file of mine beside the output packet, and no refusal for an unstated rule. | cfg_behaviour_rule 138 written this session (DEVMODE-2637-DONETEST-20261126) |
| E:4 | engaged | Open escalations assigned to Claude are listed in this declaration and come before other work, counting only in-progress threads. || the Claude-assigned items listed at the declaration and each acknowledged at every stop; #2637 v8 |
| E:5 | engaged | Work comes from escalations; comments or open items today are captured into an escalation in the same turn with the operative words quoted verbatim. || the researcher words quoted verbatim on #2637 v4, v5, v7 and v11 |

## Conflicts and rules not followed

- G:governance.study_status vs B:97: study_status says the study is active and study work may be taken up; B:97 says Developer Mode covers only work where the app controls get in the way, so study readings are standard-mode work. Resolved for this session by doing no study work here.

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

