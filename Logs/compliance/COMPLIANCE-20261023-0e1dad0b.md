# Session compliance -- 20261023 -- session 0e1dad0b-9f09-4558-ae0f-a900ebc06b67

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Any anomaly, open question or clarification I meet while starting up or in the task the researcher picks goes into the escalation table, not just chat. | #2240 v2 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine this session makes me dig through BUILD.md, old logs or prior outputs to work out how to do it, I stop and raise the missing config instead of rebuilding the step from history. | #2205 v3 (the spine check run from its registered step, no precedent needed) |
| G:governance.primary_responsibility | engaged | I own keeping every operation I touch this session inside the IBA app; anything I find running outside it is mine to bring in (via escalation and approval in standard mode). | iba/app/lib/threadaudit.py |
| G:governance.programme_stages | not engaged | No work in this session was placed or described by programme stage; it was app maintenance and escalation work. |  |
| G:governance.project_change_rule | engaged | Any change of method or approach that comes up this session is routed through the app (config row plus code), and any legacy operation I rely on must be migrated rather than run ad hoc. | #2246 v5 |
| G:governance.project_operations | engaged | I treat every research, scripting or investigative action this session as a project operation, so the app-control rules apply to all of it, not only to coding. | research/discovery/spine-check-v67-20261023.md |
| G:governance.rules_must_be_config_driven | engaged | When the researcher gives me an instruction, I first confirm the rules for it exist as cfg rows and read them correctly; a rule found only in a document or memory is escalated. | #2246 v4 (T-d reads cfg_setting escalation.worked_strand_escalations) |
| G:governance.scope_iba_app | engaged | I run operations through the app's registered PS steps (Reading.ps1, Escalation.ps1 and so on), not through loose scripts. | research/discovery/spine-check-v67-20261023.md |
| G:governance.scope_project | engaged | I apply config control to every part of the project I work in this session, not just the app folder. | .claude/commands/start-project.md |
| G:governance.study_status | engaged | The study is active again since today; any study work this session goes through Reading.ps1 (open, record, check, synergy, apply, publish) with the narrative held in iba.db, and never through the retired strand steps. | #2218 v18 (the five items clear through Reading.ps1) |
| B:1 | engaged | Before I act on any row count, flag or record, I query the live database for it in that moment instead of trusting an earlier report or memory. | live query: escalation id 729 absent, max id 2245 before and after the fix |
| B:2 | engaged | I call a step finished only after I have looked at the file or rows it was meant to produce, as with this compliance file and the escalation and thread reports. | outputs/escalation/2240-escalation-history-v2-20261023.md |
| B:4 | not engaged | No LLM, API or subagent output was produced; every claim came from a database query or a tool report. |  |
| B:10 | not engaged | No Claude API call was made and no key was handled. |  |
| B:16 | engaged | I do not use AskUserQuestion; I answer what I can from data, put real judgement calls in a review .md with options, and ask any short question in plain chat. | outputs/escalation/2246-thread-audit-td-review-v1-20261023.md |
| B:17 | engaged | Before starting whatever non-trivial task the researcher chooses after startup, I summarise it, state scope and files, and wait for a yes. | #2246 v3 |
| B:18 | engaged | Substantive analysis, plans or reports go into a .md file first; chat holds only alerts, a short summary and the path. | outputs/escalation/2246-thread-audit-td-review-v1-20261023.md |
| B:19 | engaged | I proceed only on verified facts; where something is missing I stop and ask a real question rather than guess. | #2246 v1 |
| B:20 | not engaged | No costlier route came up; every check was a targeted query or a registered step. |  |
| B:21 | engaged | An open item or judgement call that comes up in chat is raised as an escalation in that same turn. | #2246 v1 |
| B:22 | engaged | Once the researcher approves a plan this session, I carry it through without asking again at each step. | #2246 v3 to v4 |
| B:23 | engaged | If the task is a review or investigation, I take it through fix and verification and report the checked result, unless it is scoped as investigation only. | outputs/escalation/2246-td-test-results-v1-20261023.md |
| B:24 | engaged | When I report database state I show the actual query and rows, and keep a structural pass apart from fitness of the values. | iba/app/BUILD.md sec 401 |
| B:25 | engaged | I run read-only checks freely; anything that writes to the database or code stays inside an approved task. | #2246 v3 |
| B:27 | engaged | Multi-line arguments in commands I run or give use PowerShell single-quoted here-strings, never bash heredocs. | iba/app/BUILD.md sec 402 |
| B:28 | not engaged | The researcher pasted no console error this session. |  |
| B:31 | engaged | New guidance or corrections the researcher gives this session are written into a cfg row or the owning document before the session ends. | OT-108 v18 (note on items 3, 4, 5, 6, 8) |
| B:34 | engaged | Claims I make about past decisions or project state cite the file, row or commit they rest on. | iba/app/BUILD.md sec 401 |
| B:36 | not engaged | No superlative was written. |  |
| B:40 | engaged | Any open item I find in reports, checks or code this session gets an escalation row rather than a silent fix or a buried mention. | #2246 v1 |
| B:44 | engaged | A point needing a new decision stops the work and goes back as an open item; my own slips against an approved design I fix, record and continue. | #2240 v2 |
| B:83 | not engaged | No file from outside C:\Bible_study_projects was used. |  |
| B:98 | engaged | Where my work departs from an established pattern I fix it straight away instead of asking whether to. | iba/app/handlers/reports.py escalation_history |
| B:99 | engaged | I read each instruction against the whole conversation and the full scope of the escalation it concerns. | #2218 v18 |
| B:100 | engaged | In chat and files I name codes with their meaning (cluster with its name, transliteration with gloss), including in this startup report. | outputs/escalation/2246-thread-audit-td-review-v1-20261023.md |
| B:101 | engaged | Whenever the researcher must run something (an approval, a PS step), I give the full PowerShell command ready to paste. | #2205 v4 |
| B:102 | engaged | The startup report and any later summary carry only checked facts with context, grouped by the researcher's question, with no bare numbers. | #2205 v3 |
| B:105 | engaged | If I diagnose a gap this session, I send the design to the researcher as decision_required before any build, and never log build work as self_correctable. | #2246 v2, outputs/escalation/2246-thread-audit-td-review-v1-20261023.md |
| B:114 | not engaged | No reading or synergy work was done; the five catch-up readings are carried on OT-108. |  |
| E:4 | engaged | Open escalations assigned to me come before any other work; I name them first and treat only in-progress threads as work-first. | #2240 v2 |
| E:5 | engaged | The next task comes from an escalation, and anything the researcher or I raise in chat about an item is recorded in an escalation the same turn, with the instruction quoted verbatim. | #2246 v3 |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

- SC3:21e17e86 :: no record needed: a bare instruction to start work on #2240, carried out and recorded in #2240 v2
- SC3:bdda1f4a :: recorded in #2246 v1
- SC3:ec04d068 :: no record needed: the instruction to run this registered close, carried out by run RUN-20261023_174346_869-SESSION-CLOSE

