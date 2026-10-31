# Session compliance -- 20261031 -- session eccac799-3ff6-4472-8f87-3785606317c2

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or clarification I meet while building or fixing is recorded as an escalation, not left in chat or a comment. |  |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a registered routine can only be run by digging through BUILD.md or old outputs, I stop and treat that as a missing config row, not a puzzle. |  |
| G:governance.primary_responsibility | engaged | Developer Mode work is this duty itself: operations must be coded, controlled and kept intact inside the IBA app. |  |
| G:governance.programme_stages | not engaged | Describes the three research stages; no stage work is in hand before a task is named. |  |
| G:governance.project_change_rule | engaged | Any change of operation or method I build goes through the app; operations still outside it are migrated, not left. |  |
| G:governance.project_operations | not engaged | A definition of the term project operation; it asks nothing of me until a task is named. |  |
| G:governance.rules_must_be_config_driven | engaged | No rule I introduce lives only in a document or memory; it needs a cfg row, and a new instruction first gets its governing rules checked in config. |  |
| G:governance.scope_iba_app | engaged | The app is the central control for all operations, so what I build must route through it. |  |
| G:governance.scope_project | engaged | Config scope is the whole project, so a fix is not limited to one sub-area. |  |
| G:governance.study_status | not engaged | Study is ACTIVE but this is a Developer Mode session; no reading, weave or audit is started here. |  |
| B:1 | engaged | Before any step that depends on database state I query the live database rather than rely on what was reported earlier. |  |
| B:2 | engaged | I call a build step done only after confirming its file, write or report exists and matches what was intended. |  |
| B:4 | engaged | Anything I or a subagent produce that is not grounded in source data is labelled inferential until cited evidence exists. |  |
| B:10 | engaged | The API key value is never printed, logged or committed; I will not read it into output. |  |
| B:16 | engaged | I do not use AskUserQuestion; real judgement calls go to a review file, small clarifications are asked in plain chat. |  |
| B:17 | engaged | For any non-trivial build task I restate it, state the plan and files, and wait for approval before starting. |  |
| B:18 | engaged | Substantive workings go to a md file with only a pointer and brief summary in chat; the startup report is a short alert list. |  |
| B:19 | engaged | I proceed only from verified facts; missing information stops the work and is asked in plain chat. |  |
| B:20 | engaged | I flag cheaper paths: targeted reads over whole files, direct queries over subagents, dry run before live. |  |
| B:21 | engaged | Any open item or judgement call raised in chat is recorded as an escalation in the same turn. |  |
| B:22 | engaged | Once a plan is approved I run its steps to the end without re-confirming each. |  |
| B:23 | engaged | A fix task ends with the fix built, verified and its verified outcome reported, not just a finding. |  |
| B:24 | engaged | When I report database state I show the actual query and sample rows, and separate structural checks from fitness of values. |  |
| B:25 | engaged | Read-only checks run without asking; changes stay within the scope of an approved task. |  |
| B:27 | engaged | Multi-line command arguments use PowerShell here-string syntax, not Bash heredocs; I used a Bash heredoc twice this start and will not again. |  |
| B:28 | engaged | An error the researcher pastes is diagnosed and fixed, not routed around. |  |
| B:31 | engaged | New guidance given this session is put in a cfg row or the owning document the same session, not left in memory. |  |
| B:34 | engaged | Claims about project state or past decisions are cited to files, database or manifest, not recalled. |  |
| B:36 | engaged | I write no superlative unless every candidate was checked. |  |
| B:40 | engaged | Findings from code review, validation or sweeps in this build work are registered as escalations, not left in reports. |  |
| B:44 | engaged | A new decision met while building stops the work and becomes an open item; only slips against an approved design I fix and record. |  |
| B:83 | engaged | Only the C: drive project folder is authoritative; other copies are used only when the researcher names them. |  |
| B:97 | engaged | Each task is checked against the Developer Mode boundary; only the configmaint.propose gate is lifted, every development task has an escalation, and work is tested against a copy. |  |
| B:98 | engaged | A deviation from a settled standard is fixed at once, not asked about. |  |
| B:99 | engaged | When the researcher gives a build instruction, I weigh it with everything said earlier in this session, so an earlier limit on scope still holds. |  |
| B:100 | engaged | Codes are shown with their names and glosses in every report and design. |  |
| B:101 | engaged | When the researcher must run a command I give the full ready-to-run PowerShell in chat. |  |
| B:102 | engaged | Reports state checked facts with context, concise, limits stated and open items put in the register. |  |
| B:105 | engaged | Diagnosing a gap does not authorise building the fix: a design goes to the researcher as decision_required first. |  |
| B:114 | not engaged | Study synergy work from tables; no study work is in hand in this session. |  |
| B:116 | not engaged | Reading verses first applies to study work; none is started in this session. |  |
| E:4 | engaged | Items assigned to Claude are addressed before other work; the two in-progress items assigned to Claude are named at the start. |  |
| E:5 | engaged | Next actions come from escalations and the actions I identify are recorded there, including judgement calls mentioned only in chat. |  |

## Conflicts and rules not followed

- B:27: not followed at start: I ran two read-only Python checks through Bash heredoc syntax before using PowerShell here-strings; no changes were made and PowerShell is used from here.

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

