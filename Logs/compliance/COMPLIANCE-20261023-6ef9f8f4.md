# Session compliance -- 20261023 -- session 6ef9f8f4-37a3-4adc-82f4-ac33f357e65b

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything I find open or odd this session, including at startup, goes into the escalation table through Escalation.ps1, not only into chat or a report. | #2239 raised through configmaint.propose; #2216 v8, #2217 v7 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a registered routine I am asked to run leaves me digging through BUILD.md or old logs to learn how to run it, I stop there and raise the missing config instead of rebuilding the step from history. | outputs/escalation/2216-2217-plan-v1-20261023.md (every step run from live config and USER-GUIDE commands; no past precedent reconstructed) |
| G:governance.primary_responsibility | engaged | Whatever operation this session performs must run through the IBA app; if I meet one that sits outside the app, I own getting it brought in (via an escalation). | #2239 v4 (config change and index rebuild through Config-Maintenance.ps1 and Reading-Index.ps1) |
| G:governance.programme_stages | engaged | I place the work the researcher chooses in its stage (base data, analysis or publishing) and use the current methods of that stage, not the old Session A-D processes. | outputs/escalation/2216-2217-plan-v1-20261023.md (analysis-stage gaps routed to the reading process) |
| G:governance.project_change_rule | engaged | Any change of method or approach I make this session goes through the app (config rows plus code), never as a side process. | #2239 v4 (index scope changed through the app, configmaint.propose) |
| G:governance.project_operations | engaged | Startup scripts, queries and any study or build task this session all count as project operations and fall under the app's control. | Logs/compliance/COMPLIANCE-20261023-6ef9f8f4.md and #2218 v17 (startup, checks and study-control work all run through IBA tools) |
| G:governance.rules_must_be_config_driven | engaged | When a new instruction arrives I first confirm its governing rules exist as cfg rows; a rule found only in a doc or memory gets an escalation. | #2239 (reading_index.roots change through configmaint.propose) |
| G:governance.scope_iba_app | engaged | I treat the IBA app as the controller for every step of this session's work, startup included. | #2218 v17 (OT-108.18 registered through Open-Item.ps1) |
| G:governance.scope_project | engaged | Config applies to the whole project folder, so no part of today's work is outside it. | #2239 v4 (a folder outside _analytics/Clusters brought under config control) |
| G:governance.study_status | engaged | The study is active, so any study work this session goes through Reading.ps1 and its three gates, with the narrative kept in iba.db; no strand steps. | #2217 v7 (unread hits left to the reading process, Reading.ps1, not a strand pass) |
| B:1 | engaged | Before acting on any database fact (counts, flags, whether a row exists) I query iba.db live rather than trusting earlier reports or the last session log. | read-only queries of reading_strand_hit and escalation_thread_item_verse, outputs/escalation/2216-2217-plan-v1-20261023.md |
| B:2 | engaged | I call a step done only after checking its output exists and is right, e.g. the compliance file passing its check and the list and audit reports existing. | coverage re-check after OT-108.18 add: 358 of 358 unread hits on an open OT-108 item verse |
| B:4 | engaged | Anything I or a subagent conclude that is not read straight from source data is marked inferential and stays so until citable evidence backs it. | #2216 v8: the read_in_files_only claim of v5 (inferential) checked against reading_ref and ib_node before stating it |
| B:10 | engaged | If any task touches the Claude API, its key never appears in output, files, payloads or commits. | #2216 v8 (no API step run this session; no key in any payload, file or commit) |
| B:16 | engaged | I never use AskUserQuestion; I answer from the DB or code where I can, put real choices in a .md review file, and ask simple questions in plain chat. | #2216 v5 (A/B decision put in outputs/escalation/2216-2217-plan-v1-20261023.md, not AskUserQuestion) |
| B:17 | engaged | Once the researcher picks a task, I restate it, give my plan, scope and files, and wait for a yes before doing non-trivial work. | outputs/escalation/2216-2217-plan-v1-20261023.md (plan put before work) |
| B:18 | engaged | Substantive analysis or plans I produce go to a .md file first; chat gets a short summary and the path. | outputs/escalation/2216-2217-plan-v1-20261023.md |
| B:19 | engaged | I work only from checked facts and stop with a real question when something is missing rather than filling it in. | #2218 v17 (the #2239 apply stopped when its approval was not in the database) |
| B:20 | engaged | Where a cheaper route gives the same result (targeted reads, direct queries rather than subagents, dry runs), I say so and take it. | #2216 v5 (option B named as the cheaper path) |
| B:21 | engaged | Any open item or judgement call that comes up in chat is put into an escalation in the same turn (pointer to E:5). | #2218 v17 (researcher instructions recorded verbatim) |
| B:22 | engaged | After the researcher approves a plan I run it through without asking again at each step. | #2217 plan run through: OT-108.18 added, coverage checked, #2217 v7 superseded |
| B:23 | engaged | For any review or investigation I take up, I finish by fixing and verifying, unless it was scoped as investigation only. | #2216 v8 closed after #2239 applied and the index rebuilt and checked |
| B:24 | engaged | When I report DB or investigation results I show the real query output, and keep structural passes separate from whether the values are sound. | #2216 v8 and #2239 v4 state the actual counts per strand |
| B:25 | engaged | Read-only checks I run freely; writes to the DB or code only inside an approved task. | #2239 v4 (DB write only inside the approved task; all checks read-only connections) |
| B:27 | engaged | Multi-line strings I pass in PowerShell use single-quoted here-strings, never bash heredoc form. | #2239 v4 (PowerShell single-quoted strings used for every multi-line argument) |
| B:28 | engaged | If the researcher pastes an error, I diagnose and fix that error itself rather than getting the result some other way. | #2218 v17 (no researcher-pasted error this session; the missing #2239 approval was reported, not routed around) |
| B:31 | engaged | Any new guidance or correction the researcher gives today is recorded the same session in a cfg row or its owning document. | #2216 v6 researcher ruling Option B recorded; cfg_setting reading_index.roots (#2239) |
| B:34 | engaged | Claims I make about past decisions or project state cite the file, row or commit they come from. | #2216 v8 (claims cite files, rows and runs) |
| B:36 | engaged | I avoid words like most or strongest unless I have checked every candidate. | #2216 v8 (no superlative written) |
| B:40 | engaged | Open items found by any check this session (thread audit, validation output, reviews) become escalation rows, not silent fixes or report footnotes. | #2218 v17 (OT-108.18 raised for the 78 uncovered hits) |
| B:44 | engaged | A point needing a new decision stops the work and goes back to design as an open item; a slip against an agreed design I fix myself and record. | #2217 v6 (v5 slip self-corrected) and #2216 v5 (new decision routed to the researcher) |
| B:83 | engaged | I use only files under C:\Bible_study_projects; a file from Google Drive, Zotero or elsewhere is used only if the researcher names it, and is brought in with approval first. | outputs/escalation/2216-2217-plan-v1-20261023.md (only files under C:\Bible_study_projects used) |
| B:98 | engaged | If my work strays from an established standard I correct it straight away without asking. | #2217 v6 (bare Reading.ps1 named by full path) |
| B:99 | engaged | I read each instruction against the whole conversation so far, and scope escalations by everything said about them. | #2218 v17 (each instruction read against the earlier plan and approval) |
| B:100 | engaged | In chat I name every code I mention, cluster and step codes with their names and transliterations with glosses. | outputs/escalation/2216-2217-plan-v1-20261023.md (codes with names and glosses) |
| B:101 | engaged | When the researcher needs to run something, I give the full PowerShell command in chat. | #2216 v5 (ready-to-run approval commands given in chat for #2216 and #2239) |
| B:102 | engaged | The startup report and any summaries carry only checked facts with their context, grouped as the researcher frames them, no bare numbers. | #2216 v8 (counts reported with their context per strand) |
| B:105 | engaged | Finding a gap does not let me build its fix; a design goes to the researcher as decision_required first. | #2216 v5 (A/B decision handed over, not built) |
| B:114 | engaged | If study work is chosen, I run scope, collate and record into the tables before synergising, and synergise only from what the app reads back from the tables. | #2217 v7 (no synergy or narrative this session; gaps left to the reading tables) |
| E:4 | engaged | Open escalations assigned to Claude come before any other work, and only in-progress threads count as work-first. | #2216 v7, #2217 v7 worked first |
| E:5 | engaged | The next task comes from an escalation, and any researcher comment or open judgement call in chat is captured in an escalation that same turn, quoting the operative words verbatim. | #2216 v5, #2217 v6 |

## Conflicts and rules not followed

## Close dispositions

- SC3:13593f80 :: no record needed: a bare instruction to run the close procedure, carried out by this close
- SC4b:0352dd8a :: not held: an instruction to act, carried out the same session (#2217 v7, OT-108.18)
- SC4b:a885d58a :: not held: an instruction to act, carried out once #2239 was approved (#2239 v4, #2216 v8)
- SC16:Escalation.ps1_-Action_Update :: fixed: two parameter slips, each corrected on the next call (#2217 v7 written without -NextAction noted; the reject call was moot as #2217 was already closed)
