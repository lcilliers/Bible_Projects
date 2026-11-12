# Session compliance -- 20261112 -- session 8aa10d3c-e70b-4026-80d0-402cd5576939

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or clarification goes into the escalation table by its rules. | session start |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If I have to dig through BUILD.md or old outputs to learn how a registered step was done, I stop: the config is missing and is built first. | session start |
| G:governance.primary_responsibility | engaged | I am responsible for coding and keeping every project operation in the app, including back-filling operations outside it. | session start |
| G:governance.programme_stages | not engaged | Describes the three programme stages; no instruction to act on. |  |
| G:governance.project_change_rule | engaged | Any change of operation or method goes through the app; past operations outside it are migrated into it. | session start |
| G:governance.project_operations | not engaged | Definition of a project operation; nothing to act on. |  |
| G:governance.rules_must_be_config_driven | engaged | No rule lives only in a document or memory: each has a cfg_* row; a deviation found is escalated; on a new instruction I first check its rules are in config. | session start |
| G:governance.scope_iba_app | not engaged | States the app is the central process control; scope statement only. |  |
| G:governance.scope_project | not engaged | States config scope is the whole project; scope statement only. |  |
| G:governance.study_status | not engaged | Study is ACTIVE since 2026-10-23 with study work via Reading.ps1; this session builds or fixes the app, no study work unless asked. |  |
| B:1 | engaged | Verify DB state live before any operation that depends on it. | session start |
| B:2 | engaged | A step is done only when its output is confirmed to exist and match. | session start |
| B:4 | engaged | Anything from an LLM, subagent or classifier not grounded in source data is labelled inferential. | session start |
| B:10 | engaged | Never print or write the API key value anywhere. | session start |
| B:16 | engaged | Never use AskUserQuestion; judgement calls go in a .md review file, short clarifications in plain chat. | session start |
| B:17 | engaged | Summarise a non-trivial instruction, state plan and files, wait for approval; trivial tasks exempt. | session start |
| B:18 | engaged | Substantive output goes to a .md file; chat has alerts, summary and a pointer. | session start |
| B:19 | engaged | No guessing; if facts are missing I stop and ask in plain chat. | session start |
| B:20 | engaged | Advise the cheaper path before acting where one exists. | session start |
| B:21 | engaged | Any open item or judgement call surfaced in chat is recorded as an escalation the same turn. | session start |
| B:22 | engaged | Once a plan is approved, run its steps without re-confirming each. | session start |
| B:23 | engaged | Review tasks end with the fix implemented and verified, not just a finding. | session start |
| B:24 | engaged | Show the actual query or sample as evidence; structural passes are not fitness of values. | session start |
| B:25 | engaged | Read-only commands need no permission; writes stay inside approved scope. | session start |
| B:27 | engaged | Multi-line strings in PowerShell here-string syntax, never Bash heredoc, when passing command arguments. | session start |
| B:28 | engaged | A pasted error is diagnosed and fixed, not routed around. | session start |
| B:31 | engaged | New guidance is captured in the authoritative record (cfg_* row or owning doc) the same session. | session start |
| B:34 | engaged | Claims about state or past decisions are cited from the written record, not memory. | session start |
| B:36 | engaged | No superlatives unless every candidate was checked. | session start |
| B:40 | engaged | Every open item found anywhere is recorded in the escalation table. | session start |
| B:44 | engaged | A new decision point is terminal: record it as an open item and return to design; only execution slips against settled design are self-corrected. | session start |
| B:83 | engaged | Only the project folder counts as source; a file from Drive or elsewhere is used if the researcher names it, with a note and approval first. | session start |
| B:97 | engaged | Developer Mode: only configmaint.propose gate removed; each task checked against the boundary, has an escalation, is tested on a copy, rollback via named snapshot, cfg writes via apply_logged, banner on every reply. | session start |
| B:98 | engaged | Deviations from a settled standard are fixed at once, not asked about. | session start |
| B:99 | engaged | Read each instruction against the whole conversation. | session start |
| B:100 | engaged | Never show bare codes; give names and glosses. | session start |
| B:101 | engaged | If the researcher must run something, I hand over the whole PowerShell line in chat rather than send them to the Excel sheet. | session start |
| B:102 | engaged | Reports state only checked facts with context, concisely, limits stated, open items registered. | session start |
| B:105 | engaged | Diagnosing a gap is not licence to build; a design goes to the researcher first. | session start |
| B:114 | not engaged | Study-work phases; this session is app development, not study work. |  |
| B:116 | not engaged | Study starts by reading the verse; no study work in this session unless asked. |  |
| B:123 | engaged | Before using a table or column I read its recorded meaning (cfg_table.use, cfg_column) and name it in my first message on that work. | session start |
| B:124 | engaged | External services (Ollama) are reached via cfg_setting and checked before first call; read settings and record for prior routes first. | session start |
| B:125 | engaged | Jobs longer than a few minutes launch through Win32_Process Create with a log under Logs, never as a child of the session. | session start |
| B:127 | not engaged | Collection study path with the researcher; this session is app development, not study. |  |
| E:4 | engaged | Escalation resolution comes first: items assigned to Claude are addressed before other work, noted at start. | session start |
| E:5 | engaged | Chat items and researcher feedback are captured in escalations the same turn, with verbatim quotes. | session start |

## Conflicts and rules not followed

- none: no conflict found; no rule at start names a retired thing.

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_



- SC3:d2045678 :: recorded in #2484 v6
- SC3:3ce85427 :: recorded in #2487 v9
- SC3:808417f6 :: no record needed: the system's context-continuation summary, not a message the researcher wrote
- SC3:93baaf79 :: no record needed: an automatic background-task notification, not a message the researcher wrote
- SC3:3baafb5a :: recorded in #2488 v14
- SC4b:0f7b30fb :: in register #2484
- SC4b:c0a56565 :: in register #2487
- SC4b:808417f6 :: not held: the system's context-continuation summary, not a researcher message
- SC4b:4d568227 :: in register #2488
- SC4b:21177f17 :: in register #2488
- SC4b:f659a436 :: in register #2488
- SC4b:0380817f :: in register #2488
