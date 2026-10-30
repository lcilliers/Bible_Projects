# Session compliance -- 20261030 -- session 61bbf6ea-69e3-4266-8d2f-fc138b710afe

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or question that turns up while I build or fix the app gets an escalation row, not a code comment or a line in a report. | #2330 raised by validate and resolved; #2329 v4 to v6 carry the build and the trial routing |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If a registered routine can only be run by digging through old logs or archived outputs to see how it was done, I stop and treat that as a missing cfg step to register and build first. | no routine run from precedent; the #2329 design and cfg rows were the source (outputs/escalation/2329-phase-1-fit-for-purpose-design-v1-20261030.md) |
| G:governance.primary_responsibility | engaged | Keeping every project operation coded, controlled and maintained inside the IBA app is my job this session, including moving anything still outside it into the app. | the change is coded and held in the app: iba/app/lib/reading.py, iba/app/lib/observationrecord.py, run DEVMODE-2329-PHASE1-FIT-FOR-PURPOSE-20261030 |
| G:governance.programme_stages | engaged | The programme has Base_data, Analysis and Publishing stages; the build work in hand is named against the right stage and old Session A to D labels are not used. | BUILD entry 433 in iba/app/BUILD.md names the work as Analysis_phase_1 (Analysis stage) |
| G:governance.project_change_rule | engaged | Any change in operation, method or approach goes through the IBA app, and a past operation that lives outside it is migrated in. | change made through the IBA app config and reading code (BUILD entry 433) |
| G:governance.project_operations | engaged | Building, fixing, exploring and running scripts all count as project operations, so each is controlled and recorded by the app. | build, test and migration all run through the app's scripts: iba/app/tools/temp_2329_fit_for_purpose_test_run.py |
| G:governance.rules_must_be_config_driven | engaged | On each new instruction I first check that its governing rules are in cfg rows and read correctly; a rule that sits only in a document or memory is escalated. | reading.observation_parts party_form, reading.sheet_meaning (run DEVMODE-2329-PHASE1-FIT-FOR-PURPOSE-20261030) |
| G:governance.scope_iba_app | engaged | The IBA app is the central process control for everything, so a task that bypasses it is a deviation to escalate rather than carry out. | no operation done outside the app: config via apply_logged, escalation via Escalation.ps1 (#2329 v6) |
| G:governance.scope_project | engaged | Config covers the whole project, not only iba/app, so I do not narrow a check or a rule to one sub-folder. | specification v5 and references outside iba/app updated: outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md |
| G:governance.study_status | engaged | The study is ACTIVE since 2026-10-23, read at the start; study work goes through Reading.ps1, and this session builds the app rather than doing readings. | read at start (ACTIVE); no study work done; the trial routed to a standard session (#2329 v6) |
| B:1 | engaged | Before acting on any database state (counts, flags, existence of rows) I query the live database in this session rather than rely on a remembered or reported figure. | live DB queried for meaning tables, party_kind, cfg rows before and after the migration (BUILD entry 433) |
| B:2 | engaged | A build step is done only when I have checked its file, write or report exists and matches what it was meant to produce. | 23 of 23 cases pass: iba/app/tools/temp_2329_fit_for_purpose_test_run.py; live config re-read after migration |
| B:4 | engaged | Anything I or a subagent derive that is not grounded in source data is labelled inferential, and is not called confirmed without citable evidence. | no inferential claim recorded as confirmed; the trial reading is not run (#2329 v5) |
| B:10 | engaged | The API key value is never printed, logged, written or committed anywhere, including in reports, escalations and chat. | no key value printed or written; none read this session |
| B:16 | engaged | I do not use AskUserQuestion; real decisions go in a review file with options and a blank, and a simple clarifier is asked in plain chat. | AskUserQuestion not used; settings.json permissions.deny |
| B:17 | engaged | For each non-trivial build or fix I state what I understood, the approach and the files affected, and wait for approval before starting. | design approved on #2329 (outputs/escalation/2329-phase-1-fit-for-purpose-design-v1-20261030.md), then the researcher's '#2329 build' (#2329 v4) |
| B:18 | engaged | Plans, workings and reports are written to a .md file first; chat carries only alerts, a short summary and a pointer. | workings in files: iba/app/BUILD.md entry 433, Logs/SESSION-LOG-20261030-analysis-phase-1-fit-for-purpose-2329.md |
| B:19 | engaged | I work from verified facts only; where something is missing I stop and ask in plain chat instead of guessing. | no guess: the party shape and sheet fields were read from the code and tables before the build (iba/app/lib/reading.py) |
| B:20 | engaged | I flag a cheaper route before acting, such as a targeted read instead of a whole file, a direct query instead of a subagent, or a dry run before a live one. | cheaper path used: targeted reads and a result file read instead of whole files; tests on a copy |
| B:21 | engaged | Any open item or judgement call surfaced in chat, mine or the researcher's, is recorded as an escalation in that same turn with the operative words quoted verbatim. | researcher words recorded: #2329 v4 and #2329 v6 |
| B:22 | engaged | Once a plan is approved and stable I run it to completion without re-confirming each step. | approved plan run to the end without per-step confirmation: #2329 v5 |
| B:23 | engaged | A fix or investigation is finished only when the fix is built, verified and the verified outcome reported, unless it was scoped as investigation only. | #2329 v5: built, tested, documented; trial named as not done |
| B:24 | engaged | I show the actual query and sample rows when reporting database state, and do not treat a passing structural check as proof the values fit their purpose. | test output shows the case results per id; #2329 v5 comment |
| B:25 | engaged | Read-only checks need no permission; writes stay inside the scope of the task already approved. | read-only queries ran without asking; writes stayed in the approved scope (#2329 v5) |
| B:27 | engaged | A multi-line string argument is written as a PowerShell here-string, never Bash heredoc syntax, when I use the PowerShell tool. | PowerShell calls used no heredoc; one Bash heredoc for read-only queries is named in the compliance conflicts section |
| B:28 | engaged | A reported error is diagnosed and fixed or explained, not routed around while the step is called done. | the T21 failure and the #2330 validate error were diagnosed and fixed, not routed around (#2330 v2; iba/app/tools/temp_2329_fit_for_purpose_test_run.py) |
| B:31 | engaged | New guidance or decisions from the researcher this session are put into the authoritative record, a cfg row where config-governable or else the owning document, in the same session. | outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md; reading.observation_parts; iba/app/USER-GUIDE.md |
| B:34 | engaged | Claims about project state or past decisions are cited to files, the database or the manifest, not asserted from memory. | claims cite files and ids: Logs/SESSION-LOG-20261030-analysis-phase-1-fit-for-purpose-2329.md |
| B:36 | engaged | I write no most, best or clearest style claim unless every candidate was checked. | no superlative written without checking |
| B:40 | engaged | Every open item found in review, validation or a sweep is recorded in the escalation table, not left as a silent fix or a buried mention. | the one open item found, #2330, was recorded and resolved; the trial is carried on #2329 v6 |
| B:44 | engaged | A point needing a new decision during a build stops work and goes back to design as an open item; only my own slips against an approved design are corrected directly and recorded. | #2329 design approved; trial left to the researcher, not run inline |
| B:83 | engaged | C:\Bible_study_projects is the only source I rely on; copies on G:\My Drive, Zotero storage and elsewhere are ignored unless the researcher names one and approves bringing it in. | only C:\Bible_study_projects files read or written |
| B:97 | engaged | Each task is checked against the Developer Mode boundary; only the configmaint.propose gate is lifted, every task has an escalation, work is tested on a copy made with dbsnapshot.copy_db, rollback points are named snapshots, cfg writes go through apply_logged, and every reply opens with the banner. | #2329 v4 and v5; test on copy via copy_db; named snapshot iba/app/db/snapshots/kept/iba-20261030T050043Z-before-migration-analysis-phase-1-2329-v.db; apply_logged runs DEVMODE-2329-* |
| B:98 | engaged | Where my work departs from an established documented standard I fix it at once and do not ask whether to. | the unarchived migrations were fixed at once (#2330 v2), not asked about |
| B:99 | engaged | Each instruction is read against the whole conversation and the full history of the escalation it concerns, not just the latest message. | #2329 design and the 2320 usefulness test read whole before the build |
| B:100 | engaged | Cluster, dimension and step codes appear with their names, and transliterations with glosses, in everything I write; design documents use descriptive names. | codes shown with names in the reports: iba/app/BUILD.md entry 433 |
| B:101 | engaged | When the researcher must run a command I give the complete PowerShell command in chat, not a pointer to the Excel sheet. | no command was handed to the researcher to run apart from /start-project and 'run the #2329 trial' (#2329 v6) |
| B:102 | engaged | Status and close-out reports carry only checked facts, each with context, grouped by the researcher's framing, with limits stated and open items registered. | final reports gave checked results with cases per id: #2329 v5 |
| B:105 | engaged | Diagnosing a gap does not authorise me to design and build its fix; a design goes to the researcher as decision_required first, and new mechanisms are never self_correctable. | design approved by the researcher before build: #2329 v4 |
| B:114 | not engaged | This is a build and fix session with no study work in hand; if claims or narrative work is requested I will read the tables for the scope first. | |
| B:116 | not engaged | No verse reading is in hand this session; if study work starts I will read each verse with its recorded observations first. | |
| E:4 | engaged | Open escalations assigned to Claude come before other work: #2161, #2259, #2268, #2320 and #2329 are listed, and I start nothing until the researcher says which to take. | #2329 taken first at the researcher's word; #2329 v4 in-progress |
| E:5 | engaged | The next action arrives from an escalation, and chat feedback or judgement calls that are open are captured on an escalation in the same turn with verbatim quotes. | #2329 v4 comment quotes '#2329 build' verbatim |

## Conflicts and rules not followed

- B:27: I used a Bash heredoc once, for a read-only python query of cfg tables via the Bash tool; the rule bars it for PowerShell arguments, so this is noted as a deviation in spirit and I will use PowerShell here-strings from now on.
- B:97: settings.json shows no elevated permissions beyond two named allow entries, so the approval gate is not treated as bypassed until the researcher confirms.

## Close dispositions

- SC3:842363fd :: recorded in #2329 v4
- SC3:1137699c :: recorded in #2329 v6

