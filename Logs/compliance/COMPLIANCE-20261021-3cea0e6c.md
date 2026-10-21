# Session compliance -- 20261021 -- session 3cea0e6c-e050-4cb4-9290-4e4885f10990

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

"I have read the governance settings, behaviour rules and escalation rules, and will comply with them."

## Rules

At the time of writing no development task has been chosen. Rows marked `not engaged` because the task is unknown are re-assessed, and switched to `engaged`, as soon as the researcher names the task.

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.User_Guide_scope | not engaged | no tool has been changed yet; if one is, USER-GUIDE.md must describe the tool as it now stands |  |
| G:governance.base_data_spine | not engaged | no base-data work is in scope; study on hold and no task touches verse, span, strong or cluster data yet |  |
| G:governance.behaviour_boundary.backup_recovery | not engaged | a classification decision only; it tells me where durability rules live, nothing to do unless I write data |  |
| G:governance.behaviour_boundary.git_commit | engaged | my commits follow the terminal-class commit discipline, so B:26 is the rule I apply when I commit |  |
| G:governance.build_md_on_code_change | engaged | if I change anything under iba/app, I add the change record to iba/app/BUILD.md in that same piece of work | iba/app/BUILD.md |
| G:governance.config_control | engaged | any cfg row I touch is subject to the configmaint rules; in this mode that means apply_logged, see B:75 |  |
| G:governance.confmaint_configs | not engaged | I will not alter the configmaint module's own rules unless the task is exactly that |  |
| G:governance.engineering_documentation_folder | not engaged | no engineering note written yet; a general design note would go to iba/docs, an escalation deliverable to outputs/escalation |  |
| G:governance.escalation.scope | engaged | anything open, odd or needing clarification that I find this session goes into the escalation table |  |
| G:governance.escalation_worksheet_path | not engaged | only relevant if Escalation.ps1 parameters change, which no task asks for yet |  |
| G:governance.governance_md_on_rule_change | not engaged | no change to how config governs code is planned; if one is built, GOVERNANCE.md current text and BUILD.md change record are updated together |  |
| G:governance.module.config | not engaged | no new module yet; a new one would get its own cfg table(s) |  |
| G:governance.module_utility_test_plan | not engaged | applies once I design a module or utility; the test plan is then written, run after build, and its results put on the escalation |  |
| G:governance.new_utility_registration_timing | not engaged | no script created yet; any I create is registered in cfg_utility (plus cfg_step and write grant if it writes) in the same piece of work |  |
| G:governance.no_direct_github_publish | engaged | I push only this repo to its own remote and never publish narrative files to GitHub; no narrative copy is expected while the study is on hold |  |
| G:governance.oneoff_report_archive_dir | not engaged | no one-off report written yet; an older version would be moved into outputs/archive |  |
| G:governance.oneoff_report_dir | not engaged | no one-off report written yet; one would go in outputs/ |  |
| G:governance.oneoff_report_format | not engaged | no one-off report written yet; markdown is the default |  |
| G:governance.oneoff_report_naming_pattern | not engaged | no one-off report written yet; name would be topic then date then extension |  |
| G:governance.operational_behaviour_control | engaged | the behaviour rules I follow are the cfg_behaviour_rule rows restated here, not document copies |  |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | if running a registered routine forces me to dig through history to know how, I stop and raise the missing config instead |  |
| G:governance.primary_responsibility | engaged | as the developer this session I own keeping what I build coded and controlled inside the IBA app |  |
| G:governance.programme_stages | not engaged | background vocabulary; no stage work is in scope while the study is on hold |  |
| G:governance.project_change_rule | engaged | any process change I make is built into the IBA app, not left as an outside script |  |
| G:governance.project_databases | engaged | I open the research database from database/ and iba.db from iba/app/db/, both relative to the project root |  |
| G:governance.project_lookups_and_naming_convensions | not engaged | no new project term introduced yet; one would need a cfg_enum definition, a missing one gets escalated |  |
| G:governance.project_operations | engaged | the development work in this session counts as a project operation and so falls under the app's control |  |
| G:governance.prose_canonical_authority | not engaged | no prose or prose concept is touched by any known task |  |
| G:governance.ps_worksheet_path | not engaged | only relevant if a PS script's parameters change |  |
| G:governance.ps_worksheet_sync_on_change | not engaged | no PS parameter change planned; if one happens the ps tools worksheet (and for Escalation.ps1 the escalation worksheet) is updated alongside |  |
| G:governance.redundancy_archiving | engaged | anything I make obsolete today (scripts, reports, temp files) is archived today, not left live |  |
| G:governance.reports_must_persist | not engaged | no report-producing step is being built yet; if one is, it writes to a configured report path |  |
| G:governance.rules_must_be_config_driven | engaged | for whatever task arrives I first check that the governing rules are in cfg rows and raise an escalation if they are not |  |
| G:governance.scope_iba_app | engaged | the app is where control for everything lives, so any fix I make goes through it |  |
| G:governance.scope_iba_db | engaged | process control and base data questions are answered from iba.db |  |
| G:governance.scope_project | engaged | config covers the whole project, so a change outside iba/app still needs its cfg registration |  |
| G:governance.scope_research_db | not engaged | no task reads bible_research.db; if one did, only its prose tables are live |  |
| G:governance.scripts_and_routines | engaged | any script I write belongs to a module, utility or library, or is named temp_ and archived after use |  |
| G:governance.scripts_ps_dir | not engaged | no PS script added yet; one would go in iba/app/ps |  |
| G:governance.scripts_python_dir | not engaged | no Python tool added yet; one would go in iba/app/tools |  |
| G:governance.session_log_dir | engaged | my session log is written into Logs/ at close |  |
| G:governance.session_log_required_content | engaged | at close my log names the session id and has the six required sections, including the git section after the first commit |  |
| G:governance.session_log_triggers_commit | engaged | session close writes the log, clears Session-Close findings, commits and pushes, then commits the git confirmation alone |  |
| G:governance.study_status | engaged | the study is on hold since 19 October, so I start, continue or propose no study work this session |  |
| G:governance.table_columns | not engaged | no schema change planned; any new column would get a cfg_column row with a use text |  |
| G:governance.tables | not engaged | no schema change planned; any new table would get a cfg_table row |  |
| G:governance.utility.config | not engaged | no new utility yet; one would get its own cfg table |  |
| G:governance.verse_gap_by_design | not engaged | no verse data work in scope; if I meet a missing verse row I treat it as normal and raise nothing |  |
| G:narrative.inner_being_style_guide_path | not engaged | no narrative writing; study on hold |  |
| G:registry.folder_naming_convention | not engaged | no per-word registry output produced |  |
| G:report.book_folder_naming_convention | not engaged | no per-book output produced |  |
| G:report.cluster_folder_naming_convention | not engaged | no per-cluster output produced |  |
| B:1 | engaged | before acting on any database fact I query the live database for it rather than trusting memory or an earlier report | #2198 v1 |
| B:2 | engaged | I call a step finished only after I have looked at the file or rows it was meant to produce |  |
| B:3 | engaged | where content already has a home I point to it instead of repeating it in another file or reply |  |
| B:4 | engaged | anything I conclude that is not grounded in source data is marked inferential |  |
| B:5 | not engaged | no Claude API dependency is being added; if one were, it would be raised as its own decision first |  |
| B:6 | not engaged | no API-calling handler is being written; its model, limits, costs and paths would sit in cfg_setting |  |
| B:7 | not engaged | no live Claude API call is planned; one would need an estimate and cap check first |  |
| B:8 | not engaged | no live Claude API call is planned; one would need its usage logged to the CSV |  |
| B:9 | not engaged | no analytic batch run planned; Sonnet would be the default for one |  |
| B:10 | engaged | I never print, log or commit the API key value |  |
| B:11 | engaged | my database checks use read-only connections; I open for write only for an approved change |  |
| B:13 | engaged | I confirm which database holds a table before querying it |  |
| B:14 | not engaged | no SQL scratch file kept yet; one would go under scripts/SQLite in its database's folder |  |
| B:16 | engaged | I never use AskUserQuestion; judgement calls go into a review md file, short questions in plain chat |  |
| B:17 | engaged | before doing any non-trivial build I state my understanding, approach and affected files, and wait for a yes | outputs/escalation/2177-reset-backlog-plan-v1-20261021.md |
| B:18 | engaged | substantial plans or analysis go into an md file first; chat gets a summary and the path | outputs/escalation/2177-reset-backlog-plan-v1-20261021.md |
| B:19 | engaged | where a fact is missing I stop and ask rather than fill the gap with a guess |  |
| B:20 | engaged | I point out a cheaper route (targeted reads, dry runs, no needless subagents) before taking a costly one |  |
| B:21 | engaged | an open item or judgement call that comes up in chat becomes an escalation in that same turn |  |
| B:22 | engaged | once the researcher approves a plan I carry it through without asking again at each step |  |
| B:23 | engaged | a fix task ends with the fix built and verified, not just a finding written up |  |
| B:24 | engaged | when I report state I show the actual query output, and keep structural passes separate from fitness claims |  |
| B:25 | engaged | read-only checks I just run; writes stay inside the approved task |  |
| B:26 | engaged | each commit I make is pushed straight away, and I commit as units finish rather than all at the end | commit 17e202a9 |
| B:27 | engaged | multi-line strings for commands are PowerShell here-strings, never bash heredocs |  |
| B:28 | engaged | if the researcher pastes an error I fix or explain that error, never sidestep it |  |
| B:29 | engaged | each fix is tested on a made-up bad case and on real data, and each site separately | #2195 v4 |
| B:31 | engaged | any new guidance the researcher gives today is written into its cfg row or owning document today |  |
| B:32 | engaged | a record I mark complete either resolves each point or flags it as unresolved, no vague pointers |  |
| B:33 | engaged | I update existing registers in place and never start a rival one |  |
| B:34 | engaged | claims about past decisions or state cite the file, table or commit they come from |  |
| B:36 | engaged | I write no superlative unless I checked every candidate |  |
| B:37 | not engaged | no new analytical work in a dev session with the study on hold |  |
| B:38 | engaged | a bug that belongs to a class is fixed in the shared code, not item by item |  |
| B:39 | engaged | I build the simplest thing that solves the problem, no speculative frameworks |  |
| B:40 | engaged | findings from reviews, validation runs or checks get an escalation row, never a silent fix or code comment | #2195 v1 |
| B:41 | not engaged | no new hand-operated module yet; one would get a PS entry point in iba/app/ps |  |
| B:42 | not engaged | no tool change yet; when one is made USER-GUIDE.md changes with it |  |
| B:43 | not engaged | no PS script added or changed yet; any real operation script would call run.py |  |
| B:44 | engaged | when building, a point needing a new decision stops the work and goes back as an open item; my own slips against an approved design I fix and record |  |
| B:45 | engaged | on escalations I use Update for decision items and ResolveSelfCorrectable or EscalateToDecision for self-correctable ones, never AnswerRun |  |
| B:46 | not engaged | no module or utility designed yet; one would carry a test plan, run after build, with results on its escalation |  |
| B:48 | not engaged | no writes to prose_section or prose_section_type planned |  |
| B:49 | not engaged | no writes to versioned tables planned |  |
| B:50 | not engaged | no writes to versioned tables planned |  |
| B:51 | engaged | I make no physical row deletions unless the researcher instructs that specific one |  |
| B:52 | not engaged | no prose_section replace planned |  |
| B:53 | not engaged | no new prose chapter planned |  |
| B:55 | not engaged | no new prose section type planned |  |
| B:56 | engaged | any file I create gets a lowercase hyphenated name, compact date and plain version number |  |
| B:57 | engaged | snapshots I write are versioned by filename and older ones archived; living documents keep one name |  |
| B:58 | engaged | when I supersede a snapshot I move the old one to archive in the same piece of work |  |
| B:59 | engaged | before creating a file I decide its proper folder, follow naming rules, archive what it replaces, and ask if the place is unclear |  |
| B:60 | engaged | tool report output stays at its configured path; authored escalation deliverables go to outputs/escalation |  |
| B:61 | engaged | I leave inactive tables, columns and rows out of anything I report unless asked for history |  |
| B:62 | engaged | any schema, step or setting change I make registers itself in the matching cfg table in the same piece of work | iba/app/migration/register_20261021_migrations_v1_20261021.py; #2196 v2 |
| B:63 | engaged | to hand an item I hold to the researcher I set ready_for_approval, assign it and write the resolution in one call, only when it is truly ready |  |
| B:64 | not engaged | no escalation deliverable file created yet; one would start with the escalation id |  |
| B:65 | not engaged | no audit deliverable planned; one would be checked against the open queue, scope definitions and itself first |  |
| B:66 | not engaged | no cluster membership change planned |  |
| B:67 | engaged | I do not draw on bible_research.db for any IBA result outside its prose tables |  |
| B:68 | not engaged | no ib_observation correction work; study on hold |  |
| B:75 | engaged | any cfg write I make in this mode goes through configmaint.apply_logged with a DEVMODE run id | cfg_change_detail runs DEVMODE-2195-RULE59-POINTER-20261021, DEVMODE-2196-REGISTER-MIGRATIONS-20261021 |
| B:80 | engaged | any Open items line I write names a live OT or escalation handle |  |
| B:81 | engaged | this file is my restatement; I add evidence for each engaged row as I produce it | RUN-20261021_095727_933-COMPLIANCE check_start ok |
| B:82 | engaged | at close I commit nothing until Session-Close.ps1 is clean or each finding is properly dispositioned here |  |
| B:83 | engaged | I work only from C:\Bible_study_projects and ignore other copies unless the researcher names one |  |
| B:96 | engaged | when I change content its live home keeps only the new version; old text goes to its history home |  |
| B:97 | engaged | each task this session is checked against the Developer Mode boundary, gets an escalation, is tested on a copy, and every reply opens with the banner | #2195 v4; #2196 v2 |
| B:98 | engaged | if I find work off an established standard I fix it rather than ask | #2196 v2 |
| B:99 | engaged | I read each instruction against the whole conversation so far |  |
| B:100 | engaged | I show any code together with its name or gloss |  |
| B:101 | engaged | where the researcher must run something I give the full PowerShell command |  |
| B:102 | engaged | my reports state only checked facts with their context, grouped as the researcher framed the question |  |
| B:103 | engaged | anything I add to an established structure follows its existing convention |  |
| B:104 | not engaged | no new rule proposed yet; before one I would search the rule set for overlap |  |
| B:105 | engaged | a diagnosed gap goes to the researcher as a decision before I design or build its fix | outputs/escalation/2177-reset-backlog-plan-v1-20261021.md |
| B:106 | not engaged | no workflow being designed; if one is, no per-item approval steps by default |  |
| B:107 | not engaged | no orphan or unlinked verdict planned; before one I would check every link table |  |
| B:108 | engaged | text written through tools is checked for escape damage (backslash-b, dollar signs, here-strings) |  |
| E:1 | engaged | escalations I raise carry the right source, raised-by-Claude or the module name |  |
| E:2 | engaged | before raising an item I check that the same issue in the same state is not already open |  |
| E:3 | not engaged | the gate is switched off pending redesign, so nothing blocks runs this session |  |
| E:4 | engaged | open items assigned to Claude come before any new work; on-hold threads do not count |  |
| E:5 | engaged | chat items become escalations in the same turn, with the operative words quoted verbatim |  |
| E:7 | engaged | files named in escalation text use their full repo-relative path |  |
| E:11 | not engaged | no export and wipe of the escalation table planned |  |
| E:12 | engaged | if I close an issue that changes a rule or app behaviour I raise the documentation task in the same turn |  |
| E:13 | engaged | when the researcher says start work on an item, my next Update moves it to in-progress first | #2195 v3; #2188 v3; #2191 v2; #2192 v2; #2193 v2 |
| E:15 | engaged | I reassign to the researcher only for a real decision, with the evidence and options included |  |
| E:16 | engaged | before starting an issue or task I match it against open threads |  |
| E:17 | engaged | items I raise default to raised; threads go in at on-hold |  |
| E:18 | not engaged | no thread lifecycle work planned |  |

## Conflicts and rules not followed

- B:59: names docs/interaction-preferences.md as the protocol for confirming a file's destination; that file is not on disk (archived as archive/docs/interaction-preferences-history-to-20261021.md), so the pointer leads nowhere. I follow the rule's own instruction (ask when the destination is unclear) without that document. Carried as #2195.

## Close dispositions

