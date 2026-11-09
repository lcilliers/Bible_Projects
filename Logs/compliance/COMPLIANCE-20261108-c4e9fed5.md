# Session compliance -- 20261108 -- session c4e9fed5-12df-4346-8851-c74151f8675c

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or clarification I meet goes into the escalation table, not just chat. | Work and the stop-hook backlog recorded on #2393 v4; the held validate errors and the unregistered long-run files stay on #2404. |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If I have to dig through history to learn how a registered routine runs, I stop and treat it as a missing config to register first. | The exports had no registered routine; found by matching the old files, then registered as steps by iba/app/migration/archive/collection_export_2393_v1_20261108.py. |
| G:governance.primary_responsibility | engaged | I am responsible for keeping every project operation coded, controlled and maintained inside the IBA app, including back-filling. | The two inline exports are now coded steps in iba/app/lib/collectionexport.py and the config rows of iba/app/migration/archive/collection_export_2393_v1_20261108.py. |
| G:governance.programme_stages | not engaged | Only describes the three research stages; no instruction for this session start. | |
| G:governance.project_change_rule | engaged | Any change of operation or method goes through the app; old out-of-app operations get migrated. | Out-of-app export operation migrated into the app: iba/app/handlers/collectionbuild.py and iba/app/ps/Collection-Build.ps1 (ExportMembers, ExportSurfaces); BUILD.md section 473. |
| G:governance.project_operations | not engaged | Definition of what a project operation is; no action required. | |
| G:governance.rules_must_be_config_driven | engaged | Operational rules live in cfg rows, not only in docs or memory; on each new instruction I first check the governing rules are in config, else escalate. | Tiers and groups are cfg_setting rows (collection.export_tiers, surfaces.export_groups) written in iba/app/migration/archive/collection_export_2393_v1_20261108.py. |
| G:governance.scope_iba_app | not engaged | Statement of scope; no action required. | |
| G:governance.scope_project | not engaged | Statement of scope; no action required. | |
| G:governance.study_status | engaged | Study is ACTIVE since 2026-10-23; study work runs only through Reading.ps1. This is a Developer Mode build session, so no study work is started unless asked. | Read at start: study ACTIVE; Developer Mode build session, no study work started. |
| B:1 | engaged | Verify database state against the live DB before acting on it. | Join rules checked against the live tables on a copy of the DB in iba/app/tools/temp_2393_export_test_run.py. |
| B:2 | engaged | A step is done only when its output is confirmed to exist and match. | Outputs exist: _analytics/surfaces/exports/collection-members-verses-v1-20261108.csv (35,063 rows) and _analytics/surfaces/exports/behaviour-and-inner-state-surfaces-v1-20261108.csv (106,796 rows), counted after the live runs. |
| B:4 | engaged | Anything from an LLM, subagent or my own inference is labelled inferential until grounded. | BUILD.md section 473 states plainly that a full row-for-row match to the old files is not claimed, with the reasons. |
| B:10 | engaged | Never print or write an API key value anywhere. | No API key was read, printed or written in this session's work. |
| B:16 | engaged | AskUserQuestion is never used; judgement calls go to a review file, short clarifications in plain chat. | AskUserQuestion not used; the handover and open questions are on #2393 v4. |
| B:17 | engaged | Non-trivial work: state understanding, plan and files, wait for approval before starting. | Scope was the researcher's instruction recorded on #2393 v3; the plan and files are in BUILD.md section 473. |
| B:18 | engaged | Substantive output goes to a .md file; chat has only a brief summary and pointer. | Full account in iba/app/BUILD.md (section 473) and outputs/escalation/2393-escalation-history-v1-20261108.md; chat carried short summaries. |
| B:19 | engaged | No guessing; stop and ask in plain chat when facts are missing. | Where facts were missing the old files were matched, not guessed; the limit is stated in iba/app/BUILD.md section 473. |
| B:20 | engaged | Flag a cheaper path before using an expensive one (subagents, whole-file reads, live runs). | Tests ran on a copy of the DB, and the two live runs were done once each, in iba/app/tools/temp_2393_export_test_run.py and the front door. |
| B:21 | engaged | Open items raised in chat become escalations in the same turn. | The #2393 handover and the held validate errors went to escalations the same turn (#2393 v4, #2404). |
| B:22 | engaged | Once a plan is approved, run its steps to completion without re-confirming each. | After the instruction on #2393 v3 the build, tests, docs and handover ran to completion without re-confirming each step. |
| B:23 | engaged | Investigations end with the fix made and verified, unless scoped investigation-only. | The investigation ended in a built and tested fix: iba/app/tools/temp_2393_export_test_run.py passes H1 to H8. |
| B:24 | engaged | Show actual query results and samples, not smoothed summaries. | Actual row counts and match counts (19,632 and 89,902 rows each side, 0 and 0 only-old/only-new) are in iba/app/BUILD.md section 473. |
| B:25 | engaged | Read-only commands need no permission; writes stay within approved task scope. | Writes stayed within #2393; config writes only through the migration iba/app/migration/archive/collection_export_2393_v1_20261108.py. |
| B:27 | engaged | Multi-line string arguments use PowerShell here-strings; avoid Bash heredoc in this environment. | Multi-line content written with files and here-strings; the helper script iba/app/tools/temp_2393_export_test_run.py holds the test, not Bash heredocs for PowerShell. |
| B:28 | engaged | Reported errors are diagnosed and fixed, not routed around. | Errors met (copy_db signature, misplaced migration, regex over paths) were diagnosed and fixed; see iba/app/BUILD.md section 473. |
| B:31 | engaged | Researcher guidance is recorded in cfg rows or the owning document the same session. | The researcher's instruction is recorded on #2393 v3 and the rules found are in iba/app/lib/collectionexport.py docstring. |
| B:34 | engaged | Claims about project state are grounded in and cite the written record. | State claims cite the written record: iba/app/BUILD.md section 473 and #2393 v4. |
| B:36 | engaged | No superlatives unless every candidate was checked. | No superlatives used; comparisons stated with counts in iba/app/BUILD.md section 473. |
| B:40 | engaged | Every open item found anywhere is recorded in the escalation table. | Open items found (old files not retired, worksheet rows, manifest) are on #2393 v4; validate errors on #2404. |
| B:44 | engaged | New decisions are terminal: record and route to design; only execution slips against settled designs are self-corrected. | No new design decision taken: retirement of the old files and the worksheet rows were left to the researcher on #2393 v4. |
| B:83 | engaged | Only C:\Bible_study_projects is authoritative; other copies are ignored unless the researcher names one. | Only C:\Bible_study_projects was used; no other copy was read or written. |
| B:97 | engaged | Developer Mode removes only the configmaint.propose gate; each task checked against the mode boundary, has an escalation, is tested on a copy with the result recorded, uses named snapshots for rollback, writes cfg via apply_logged, and replies open with the banner. | Banner on every reply; config through apply_logged in iba/app/migration/archive/collection_export_2393_v1_20261108.py; snapshot iba/app/db/snapshots/kept/iba-20261108T093654Z-pre-2393-collection-export.db; test on a copy in iba/app/tools/temp_2393_export_test_run.py; escalation #2393 v4. |
| B:98 | engaged | Deviations from an established standard are fixed at once, not asked about. | Deviations from the standard were fixed at once (B:99 evidence wording, migration moved to archive); see iba/app/BUILD.md section 473. |
| B:99 | engaged | I interpret every request in light of everything said so far in the chat, and an escalation takes its scope from all the researcher has said on it. | The request was read with the earlier exchange on #2393 (v1, v2, v3): the two files named there are the specification. |
| B:100 | engaged | Codes are shown with their names, never bare. | Codes shown with names in the account in iba/app/BUILD.md section 473 (steps, settings and collections named). |
| B:101 | engaged | Commands for the researcher are given complete and ready-to-run in PowerShell. | Commands in iba/app/USER-GUIDE.md (Collection-Build block) are complete PowerShell lines. |
| B:102 | engaged | Status reports state checked facts only, with context, limits and open items registered. | Status reports state checked facts with limits and open items, recorded on #2393 v4. |
| B:105 | engaged | Diagnosing a gap does not license building the fix; designs go to the researcher as decision_required first. | The researcher instructed the build on #2393 v3; the open design points (retire the old files, worksheet) went back as a handover on #2393 v4. |
| B:114 | not engaged | Governs study synergise phases; no study work in this session unless requested. | |
| B:116 | not engaged | Governs starting study work by reading verses; no study work unless requested. | |
| B:123 | engaged | Before using a table or column I read its recorded meaning in cfg_table and cfg_column and name it in my first message on that work. | cfg_table and cfg_column meanings of verse_lexical, surface_term, collection_link and cluster_strong read before use; named in iba/app/lib/collectionexport.py docstring. |
| B:124 | engaged | External service routines (Ollama) read access from cfg_setting and check the service first; I check settings and written record before trying a route. | Not used: no Ollama or other external service was called in this work (iba/app/lib/collectionexport.py reads tables only). |
| B:125 | engaged | Jobs longer than a few minutes start via Win32_Process Create with a log under Logs, and the start is verified; not as a child of the session. | No long job started; the two exports run in seconds, and the batch of #2388 was not touched (see #2393 v4). |
| E:4 | engaged | Open items assigned to Claude are addressed before other work; the backlog is listed at start. | Backlog listed at start; items assigned to Claude acknowledged one by one, #2393 first and handed over on #2393 v4. |
| E:5 | engaged | Chat discussion and researcher feedback are actioned through escalations in the same turn, with verbatim quotes. | The researcher's words are recorded verbatim on #2393 v3 and #2393 v4. |
## Conflicts and rules not followed

_(none at session start)_

## Close dispositions

- SC3:b7e107fb :: recorded in #2393 v5
- SC3:affc46fc :: no record needed: bare command to run session-close, nothing to record
- SC3:85cc414d :: no record needed: automatic context-compaction summary, its content is recorded on #2393 v3 and v4
- SC4b:b7e107fb :: not held: a PowerShell usage error answered in chat with the full-path command, nothing deferred (recorded on #2393 v5)
- SC4b:85cc414d :: not held: automatic context-compaction summary, no holding request in it
- SC16:Config-Maintenance.ps1_-Step_Validate :: fixed: the validate errors were the unregistered long-run files, registered by the approved #2399 to #2402; #2404 completed with no coherence errors after

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

