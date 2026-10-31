# Session compliance -- 20261031 -- session eccac799-3ff6-4472-8f87-3785606317c2

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or clarification I meet while building or fixing is recorded as an escalation, not left in chat or a comment. | #2343 v1; #2342 v1 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a registered routine can only be run by digging through BUILD.md or old outputs, I stop and treat that as a missing config row, not a puzzle. | #2340 v3 |
| G:governance.primary_responsibility | engaged | Developer Mode work is this duty itself: operations must be coded, controlled and kept intact inside the IBA app. | iba/app/BUILD.md entry 439 |
| G:governance.programme_stages | not engaged | Describes the three research stages; no stage work is in hand before a task is named. |  |
| G:governance.project_change_rule | engaged | Any change of operation or method I build goes through the app; operations still outside it are migrated, not left. | iba/app/migration/archive/concept_tables_2339_v1_20261031.py |
| G:governance.project_operations | not engaged | A definition of the term project operation; it asks nothing of me until a task is named. |  |
| G:governance.rules_must_be_config_driven | engaged | No rule I introduce lives only in a document or memory; it needs a cfg row, and a new instruction first gets its governing rules checked in config. | #2339 v15; #2340 v1 |
| G:governance.scope_iba_app | engaged | The app is the central control for all operations, so what I build must route through it. | #2339 v15 |
| G:governance.scope_project | engaged | Config scope is the whole project, so a fix is not limited to one sub-area. | #2339 v15 |
| G:governance.study_status | not engaged | Study is ACTIVE but this is a Developer Mode session; no reading, weave or audit is started here. |  |
| B:1 | engaged | Before any step that depends on database state I query the live database rather than rely on what was reported earlier. | #2339 v12 |
| B:2 | engaged | I call a build step done only after confirming its file, write or report exists and matches what was intended. | iba/app/tools/temp_2339_concept_tables_test_run.py; #2339 v15 |
| B:4 | engaged | Anything I or a subagent produce that is not grounded in source data is labelled inferential until cited evidence exists. | outputs/concept-mapping/pilot-surfaces-result-v1-20261031.md; #2339 v6 |
| B:10 | engaged | The API key value is never printed, logged or committed; I will not read it into output. | outputs/concept-mapping/pilot-surfaces-result-v1-20261031.md |
| B:16 | engaged | I do not use AskUserQuestion; real judgement calls go to a review file, small clarifications are asked in plain chat. | #2339 v3; #2339 v4 |
| B:17 | engaged | For any non-trivial build task I restate it, state the plan and files, and wait for approval before starting. | #2339 v14; #2339 v7 |
| B:18 | engaged | Substantive workings go to a md file with only a pointer and brief summary in chat; the startup report is a short alert list. | outputs/concept-mapping/pilot-surfaces-result-v1-20261031.md; Logs/SESSION-LOG-20261031-concept-tables-2339.md |
| B:19 | engaged | I proceed only from verified facts; missing information stops the work and is asked in plain chat. | #2339 v13; #2339 v7 |
| B:20 | engaged | I flag cheaper paths: targeted reads over whole files, direct queries over subagents, dry run before live. | #2339 v7 |
| B:21 | engaged | Any open item or judgement call raised in chat is recorded as an escalation in the same turn. | #2342 v1; #2343 v1 |
| B:22 | engaged | Once a plan is approved I run its steps to the end without re-confirming each. | #2339 v15 |
| B:23 | engaged | A fix task ends with the fix built, verified and its verified outcome reported, not just a finding. | #2339 v15; iba/app/BUILD.md entry 439 |
| B:24 | engaged | When I report database state I show the actual query and sample rows, and separate structural checks from fitness of values. | outputs/concept-mapping/pilot-surfaces-result-v1-20261031.md; #2339 v12 |
| B:25 | engaged | Read-only checks run without asking; changes stay within the scope of an approved task. | #2339 v10 |
| B:27 | engaged | Multi-line command arguments use PowerShell here-string syntax, not Bash heredocs; I used a Bash heredoc twice this start and will not again. | Logs/compliance/COMPLIANCE-20261031-eccac799.md |
| B:28 | not engaged | The researcher pasted no console or terminal error this session. |  |
| B:31 | engaged | New guidance given this session is put in a cfg row or the owning document the same session, not left in memory. | #2340 v1; #2339 v14 |
| B:34 | engaged | Claims about project state or past decisions are cited to files, database or manifest, not recalled. | #2339 v12; #2339 v11 |
| B:36 | engaged | I write no superlative unless every candidate was checked. | #2339 v8 |
| B:40 | engaged | Findings from code review, validation or sweeps in this build work are registered as escalations, not left in reports. | #2341 v1; #2343 v1 |
| B:44 | engaged | A new decision met while building stops the work and becomes an open item; only slips against an approved design I fix and record. | #2339 v4; #2339 v6 |
| B:83 | engaged | Only the C: drive project folder is authoritative; other copies are used only when the researcher names them. | outputs/concept-mapping/concepts-v1-20261031.md |
| B:97 | engaged | Each task is checked against the Developer Mode boundary; only the configmaint.propose gate is lifted, every development task has an escalation, and work is tested against a copy. | #2339 v14; iba/app/BUILD.md entry 439 |
| B:98 | engaged | A deviation from a settled standard is fixed at once, not asked about. | iba/app/migration/archive/apply_other_beings_m85_v1_20261031.py; iba/app/BUILD.md entry 439 |
| B:99 | engaged | When the researcher gives a build instruction, I weigh it with everything said earlier in this session, so an earlier limit on scope still holds. | #2339 v14; #2339 v3 |
| B:100 | engaged | Codes are shown with their names and glosses in every report and design. | outputs/concept-mapping/pilot-surfaces-result-v1-20261031.md |
| B:101 | not engaged | The researcher was asked to run no command this session. |  |
| B:102 | engaged | Reports state checked facts with context, concise, limits stated and open items put in the register. | Logs/SESSION-LOG-20261031-concept-tables-2339.md; #2339 v15 |
| B:105 | engaged | Diagnosing a gap does not authorise building the fix: a design goes to the researcher as decision_required first. | #2339 v4; #2339 v6 |
| B:114 | not engaged | Study synergy work from tables; no study work is in hand in this session. |  |
| B:116 | not engaged | Reading verses first applies to study work; none is started in this session. |  |
| E:4 | engaged | Items assigned to Claude are addressed before other work; the two in-progress items assigned to Claude are named at the start. | #2338 v3; #2339 v17 |
| E:5 | engaged | Next actions come from escalations and the actions I identify are recorded there, including judgement calls mentioned only in chat. | #2339 v1; #2340 v1 |

## Conflicts and rules not followed

- B:27: not followed at start: I ran two read-only Python checks through Bash heredoc syntax before using PowerShell here-strings; no changes were made and PowerShell is used from here.
- G:governance.past_precedent_investigation_signals_missing_config: not followed in building the concept tables: the table-build convention was taken from the archived migration iba/app/migration/archive/surface_subgroup_schema_2292_v1_20261025.py without first checking iba/app/USER-GUIDE.md or iba/app/GOVERNANCE.md for a stated way; whether one exists is not known; recorded in #2340 v3.

## Close dispositions

- SC3:16f43e75 :: recorded in #2339 v1
- SC3:2050397b :: recorded in #2339 v2
- SC3:bcdeeb1a :: recorded in #2339 v4
- SC3:2379ec45 :: recorded in #2339 v5
- SC3:e5a48e8b :: no record needed: a status question about the pilot, answered in chat; the pilot result is in #2339 v6
- SC3:e2f8fa23 :: no record needed: a status remark about the pilot, answered in chat; the result is in #2339 v6
- SC3:1c844911 :: no record needed: an automated background-task notification, not a researcher message
- SC3:e68344f7 :: no record needed: a question about the surface table count, answered in chat; the counts are in #2339 v7
- SC3:e41c43e5 :: no record needed: a question answered in chat; the M-code finding and the researcher's ruling are in #2339 v7
- SC3:487375d9 :: no record needed: a question about deleted rows, answered in chat; the correction is in #2339 v12
- SC3:d15d8391 :: no record needed: a question about where the concept tables are, answered in chat (not yet created); the grouping history is in #2343 v1
- SC3:c7abf280 :: no record needed: the researcher's confirmation that the tables were not yet created; the state is in #2339 v14
- SC3:117da3ff :: recorded in #2339 v14
- SC3:ff2c15ff :: recorded in #2339 v14
- SC3:f57bb68f :: recorded in #2339 v16
- SC3:6263dafb :: recorded in #2338 v3

