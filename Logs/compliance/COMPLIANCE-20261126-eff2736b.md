# Session compliance -- 20261126 -- session eff2736b-f065-4715-b721-1291b41f95d4

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Any open item or anomaly I find while building the app goes into the escalation table through Escalation.ps1, not left in chat or code. |  |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine needs me to dig through BUILD.md or old outputs to work out how it was done, I stop and escalate the missing config instead of reconstructing it. |  |
| G:governance.primary_responsibility | engaged | I own the code and integrity of the IBA app; whatever I build this session lives inside the app and is controlled by it. |  |
| G:governance.programme_stages | engaged | When app work touches a stage of the programme I place it correctly among base data, analysis stages 1-5 and publishing, and treat stage 5 as undefined. |  |
| G:governance.project_change_rule | engaged | Any change of method I make goes through the app; no side scripts or one-off procedures left outside it. |  |
| G:governance.project_operations | engaged | Everything I run this session, scripts and investigations included, counts as a project operation and falls under app control. |  |
| G:governance.rules_must_be_config_driven | engaged | Any rule I add or change gets a cfg_* row; before acting on an instruction I check its governing rules are in config, else escalate. |  |
| G:governance.scope_iba_app | engaged | The app is the controller of all operations; I build fixes into it rather than around it. |  |
| G:governance.scope_project | engaged | Config covers the whole project, so a fix anywhere in the project is in scope for config, not only the app folder. |  |
| G:governance.study_status | engaged | Study is active; any study work goes through Reading.ps1. Developer Mode work here is app-building, not study, unless a task says otherwise. |  |
| B:1 | engaged | Before any change that depends on DB state I query iba.db live for that state rather than trusting earlier reports or the last session log. |  |
| B:2 | engaged | I call a build step done only after I have checked its file, DB write or report actually exists and is right. |  |
| B:4 | engaged | Anything I or a subagent infer without source grounding I label inferential, and only upgrade it with cited evidence. |  |
| B:10 | engaged | I never print, log or commit the Claude API key value, including in test output or escalation payloads. |  |
| B:16 | engaged | I do not use AskUserQuestion; real judgement calls go to a .md review file, a simple clarification goes in plain chat. |  |
| B:17 | engaged | For each non-trivial build or fix the researcher asks for, I state my understanding, plan and files touched and wait for a yes before starting. |  |
| B:18 | engaged | Substantive plans, analyses and reports go into a .md file first; chat carries a short summary and the path. |  |
| B:19 | engaged | I work only from checked facts; where something is missing I stop and ask in plain chat instead of guessing. |  |
| B:20 | engaged | I take the cheaper route by default: targeted reads and queries, no subagent unless needed, dry run then run, failing-only test re-runs; I say why if I go dearer. |  |
| B:21 | engaged | An open item raised in our chat gets its escalation row in the same turn. |  |
| B:22 | engaged | Once the researcher approves a plan I run it through without re-confirming each step. |  |
| B:23 | engaged | A fix task ends with the fix built and verified and the verified result reported, not just the diagnosis, unless scoped as investigation only. |  |
| B:24 | engaged | When reporting DB state or test results I show the actual query and output, and keep structural passes distinct from fitness of values. |  |
| B:25 | engaged | Read-only checks I run without asking; DB or code changes only within the approved task. |  |
| B:27 | engaged | Multi-line command arguments in PowerShell use the single-quoted here-string form, not bash heredocs. |  |
| B:28 | engaged | If the researcher pastes an error I diagnose and fix that error, never complete the step another way and call it done. |  |
| B:31 | engaged | New guidance the researcher gives this session is written into a cfg_* row or its owning document in this session. |  |
| B:34 | engaged | Claims about past state or decisions I ground in the record (DB, files, BUILD.md, escalations) and cite. |  |
| B:36 | engaged | I avoid superlatives unless I checked every candidate. |  |
| B:40 | engaged | Findings from code review, test runs or checks during the build become escalation rows, not silent fixes or comments. |  |
| B:44 | engaged | A new decision point met while building stops that line of work and is routed back as an open item; my own slips against an approved design I fix and record. |  |
| B:83 | engaged | I work only in C:\Bible_study_projects; files elsewhere are used only when the researcher names them, and are brought in with approval. |  |
| B:97 | engaged | This session is Developer Mode by the researcher choice at start; only the configmaint.propose approval gate is lifted; I check each new task belongs to dev mode and keep all other rules. |  |
| B:98 | engaged | Where my work deviates from an established standard I fix it straight away instead of asking. |  |
| B:99 | engaged | I read each instruction against the whole conversation and the escalation record and session logs before asking anything. |  |
| B:100 | engaged | I never show a code bare; each code in chat or docs carries its name. |  |
| B:101 | engaged | Any command the researcher must run I give as a complete ready-to-run PowerShell line in chat. |  |
| B:102 | engaged | Status reports I give hold only checked facts with context, are concise, state limits and put open items in the register. |  |
| B:105 | engaged | Diagnosing a gap does not license me to design and build its fix; a design goes to the researcher as decision_required first. |  |
| B:114 | not engaged | No study phase work is in hand; this is an app-building session. Engages if a task becomes study work. |  |
| B:116 | not engaged | No verse reading is planned in this Developer Mode session. |  |
| B:123 | engaged | Before I use a table or column for a count, design or code, I read its cfg_table and cfg_column meaning and name what I read. |  |
| B:124 | not engaged | No routine using Ollama or another outside service is in hand yet; engages if the build touches one. |  |
| B:125 | not engaged | No job longer than a few minutes is planned; if one arises I start it through Win32_Process Create with a log under Logs. |  |
| B:127 | not engaged | No collection is being taken through the study path in this session. |  |
| B:129 | not engaged | No collection membership is being built or changed; engages if app code touching collections is in the task. |  |
| B:130 | not engaged | No node creation or node logic change is planned yet; engages if the build touches nodes. |  |
| B:131 | not engaged | No observations are being written; engages if the build changes observation handling. |  |
| B:132 | not engaged | No collection reading is run; engages if I change the layered reading routines. |  |
| B:133 | not engaged | No lexical or inner-being reading is run; engages if I change how S1 and step 1.1 gate each other. |  |
| B:134 | not engaged | No layer step ledger work is planned; engages if the build touches collection_layer_item. |  |
| B:136 | not engaged | No collection validation is run; engages if the build changes the validation routines. |  |
| B:137 | engaged | Any intervention I make outside the app packages is coded back into them as repeatable code or config before I call the work done. |  |
| B:138 | not engaged | No analytic reading routine is being built yet; if one is, I call it complete only after an unaided run on a fresh unit on a dbsnapshot copy. |  |
| E:4 | engaged | Open escalations assigned to Claude come before other work; only in-progress threads count. |  |
| E:5 | engaged | Work arrives from and is recorded in escalations; any deferred or left-as-is judgement I mention in chat gets its own escalation that turn. |  |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

