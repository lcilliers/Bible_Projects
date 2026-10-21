# Session compliance -- 20261021 -- session ac12e7c5-9668-4a70-ac93-a5627fd602c4

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.User_Guide_scope | engaged | The guide reflects the changed list, validate and compliance behaviour. | iba/app/USER-GUIDE.md |
| G:governance.base_data_spine | not engaged | Verse, span, strong and parse must agree; no base-data work is in hand. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.behaviour_boundary.backup_recovery | not engaged | Placement ruling only: durability falls under the sqlite class. Nothing written to a DB yet. |  |
| G:governance.behaviour_boundary.git_commit | engaged | Commit and push count as terminal discipline; any commit this session follows the terminal rule. |  |
| G:governance.build_md_on_code_change | engaged | The #2206 code edits under iba/app get their BUILD.md section in the same pass. | iba/app/BUILD.md sec 372 and 373 sec 374 |
| G:governance.config_control | engaged | The new compliance setting goes in through the audited configmaint write. | run DEVMODE-2206-READING-WASTE-20261021 iba/app/migration/archive/reading_waste_2206_v1_20261021.py |
| G:governance.confmaint_configs | not engaged | Config-maintenance behaviour comes from configmaint-module settings. No cfg write yet. |  |
| G:governance.engineering_documentation_folder | not engaged | Cross-cutting design notes go in iba/docs, escalation deliverables in outputs/escalation. No note written yet. |  |
| G:governance.escalation.scope | engaged | Anything open or anomalous I find this session gets an escalation row, starting with the backlog read. | #2206 v1 #2177 v20 |
| G:governance.governance_md_on_rule_change | engaged | Changed checks (validate asks only new findings, delivery trimmed) are described in GOVERNANCE.md now. | iba/app/GOVERNANCE.md |
| G:governance.module.config | not engaged | A module needs cfg tables steering it; relevant only if a module is built. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.module_utility_test_plan | engaged | The #2206 changes have a test plan run on a copy with per-case results on the escalation. | outputs/escalation/2206-reading-waste-test-results-v1-20261021.md |
| G:governance.new_utility_registration_timing | engaged | The migration I wrote registers its own cfg_utility row as it runs. | iba/app/migration/archive/reading_waste_2206_v1_20261021.py |
| G:governance.no_direct_github_publish | not engaged | Nothing goes to GitHub pages from here; narrative copy only via the copy script. No narrative work in Developer Mode. |  |
| G:governance.operational_behaviour_control | engaged | Behaviour rules come from cfg_behaviour_rule across the project; I follow the rows loaded into this file, not memory. |  |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | Reading BUILD history was the researcher's ask (why each control exists), not filling a missing step. | outputs/escalation/2177-reading-waste-options-v2-20261021.md |
| G:governance.primary_responsibility | engaged | I own coding and integrity of the app; this session is app work in Developer Mode. |  |
| G:governance.programme_stages | not engaged | Names the three stages (base data, analysis, publishing). Background only; no stage work in hand. |  |
| G:governance.project_change_rule | not engaged | Method changes go through the app, and legacy operations are migrated into it. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.project_databases | engaged | iba.db sits in iba/app/db and research_db in database; I opened iba.db by that path. |  |
| G:governance.project_lookups_and_naming_convensions | not engaged | Project terms must be defined in cfg_enum and checked when used. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.project_operations | not engaged | Definition of what counts as a project operation; nothing to act on by itself. |  |
| G:governance.prose_canonical_authority | not engaged | The programme prose is the source for core concepts; no concept or prose work in hand. |  |
| G:governance.ps_worksheet_sync_on_change | not engaged | A changed ps parameter list must be mirrored in the Excel sheets in the same pass. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.redundancy_archiving | not engaged | Stale one-offs are archived daily; nothing made redundant yet. |  |
| G:governance.reports_must_persist | not engaged | A check that reports must write to its configured path. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.rules_must_be_config_driven | engaged | On the coming instruction I first confirm the rules for it are in cfg rows, and escalate any that live only in a document. | #2208 v7 iba/app/lib/cfgquality.py |
| G:governance.scope_iba_app | engaged | The app is the controller for all work; the developer task will be done inside it. |  |
| G:governance.scope_iba_db | engaged | Process control and base data live in iba.db; I query there. |  |
| G:governance.scope_project | not engaged | States config covers the whole project; nothing specific to do yet. |  |
| G:governance.scope_research_db | not engaged | research_db holds prose only; I have no reason to open it. |  |
| G:governance.scripts_and_routines | not engaged | Every script belongs to a module, utility or library, else is temp_ prefixed. None created yet. |  |
| G:governance.scripts_python_dir | not engaged | Python tools live in iba/app/tools; matters if I add one. |  |
| G:governance.session_log_required_content | engaged | At close I write a log with the six required sections, real ids, paths and git output. |  |
| G:governance.session_log_triggers_commit | engaged | Session close writes the log, clears findings, commits and pushes, then commits the git section alone. |  |
| G:governance.study_status | engaged | Study is on hold since 19 Oct; I start, continue or propose no study work, only app work. |  |
| G:governance.table_columns | not engaged | Every column needs a cfg_column use text; matters if schema changes. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.tables | not engaged | Every table needs a cfg_table row; matters if schema changes. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.utility.config | not engaged | Each utility gets its own cfg table; matters if a utility is built. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.verse_gap_by_design | not engaged | A verse absent from the verse table is intended, not a bug; no verse work in hand. |  |
| G:narrative.inner_being_style_guide_path | not engaged | Style guide for narrative text; no narrative writing in Developer Mode, study on hold. |  |
| G:registry.folder_naming_convention | not engaged | Per-word registry folders use padded id and word; no registry output in hand. |  |
| G:report.book_folder_naming_convention | not engaged | Book folders use the OSIS book code; no book output in hand. |  |
| G:report.cluster_folder_naming_convention | not engaged | Cluster output files in its own code-named folder; no cluster output in hand. |  |
| B:1 | engaged | Backlog and state I report come from a live query this session, not recall. |  |
| B:2 | engaged | I confirm the compliance file passes and the marker file exists before calling those steps done. | #2206 v6 outputs/escalation/escalation-list-v186-20261021.md |
| B:3 | engaged | I point at the rule homes rather than restate them in any doc I touch. |  |
| B:4 | not engaged | Labels LLM-derived claims as inferential; no analytic claims produced in this setup. |  |
| B:5 | not engaged | Adding the anthropic SDK is its own decision; no such change planned. |  |
| B:6 | not engaged | API call parameters belong in cfg_setting; no API-calling step in hand. |  |
| B:7 | not engaged | Cost estimate and cap check before any live API call; none planned. |  |
| B:8 | not engaged | Usage of every live API call goes to the CSV ledger; none planned. |  |
| B:9 | not engaged | Sonnet for bulk analytic calls; no analytic API work in hand. |  |
| B:10 | engaged | I never print or write the API key anywhere, including chat and commits. |  |
| B:11 | engaged | My checking queries open iba.db read-only (mode=ro URI). |  |
| B:13 | engaged | I check which DB holds a table before querying; rules came from iba.db. |  |
| B:14 | not engaged | Kept SQL scratch files go in scripts/SQLite by DB; none written. |  |
| B:16 | engaged | No AskUserQuestion; I ask what to build in plain chat. |  |
| B:17 | engaged | Before any build I restate the task, scope and files and wait for a yes. | #2206 v4 |
| B:18 | engaged | Plans and findings go to a md file first; chat carries a pointer and summary. | outputs/escalation/2177-reading-waste-options-v2-20261021.md |
| B:19 | engaged | I act only on checked facts and ask in chat when something is missing. |  |
| B:20 | engaged | I flag a cheaper route where one exists, e.g. targeted reads over full ones. |  |
| B:21 | engaged | Any open item raised in chat is made an escalation in that turn. | #2206 v1 #2177 v20 |
| B:22 | not engaged | Run an approved plan through without re-asking per step; no plan approved yet. |  |
| B:23 | engaged | The approved build is done, tested and its live effect checked, not left as a write-up. | outputs/escalation/2206-reading-waste-test-results-v1-20261021.md #2207 v1 |
| B:24 | engaged | I show the actual backlog rows and check output, not a smoothed summary. | outputs/escalation/2206-reading-waste-test-results-v1-20261021.md |
| B:25 | engaged | Read-only checks run without asking; writes stay inside an approved task. |  |
| B:26 | engaged | Any commit I make is pushed right away, and commits come as work units finish. |  |
| B:27 | engaged | Multi-line arguments to commands use PowerShell here-strings, not bash heredocs. |  |
| B:28 | not engaged | A pasted error gets diagnosed, never sidestepped; none pasted. |  |
| B:29 | engaged | Each change tested with synthetic cases and on a copy of real data. | outputs/escalation/2206-reading-waste-test-results-v1-20261021.md |
| B:31 | engaged | New guidance from the researcher this session goes into its cfg row or owning doc the same session. |  |
| B:32 | not engaged | No hedged pointers in records marked complete; none written yet. |  |
| B:33 | not engaged | One living register per tracked set, updated in place; none touched. |  |
| B:34 | engaged | Claims about past state cite the record (git, DB, files). |  |
| B:36 | engaged | I avoid superlatives I have not checked against all candidates. |  |
| B:37 | not engaged | Analytic work comes from instructions, not prior unreviewed outputs; no analytic work. |  |
| B:38 | engaged | The duplicate-match defect found in testing was fixed in the shared validate path. | iba/app/BUILD.md sec 372 |
| B:39 | engaged | Builds are kept to simple direct steps without speculative framework. |  |
| B:40 | engaged | Any open item I discover is put in the escalation table. | #2206 v1 #2177 v20 |
| B:41 | not engaged | Hand-run modules need a ps entry point; matters if a module is built. |  |
| B:42 | engaged | USER-GUIDE.md updated for the list, validate and compliance changes in this pass. | iba/app/USER-GUIDE.md |
| B:43 | not engaged | New ps scripts dispatch through run.py except the two named exceptions. No build task chosen yet; re-assessed when the researcher names one. |  |
| B:44 | engaged | A new decision met while building stops the work and goes back for design; my own slips I fix and record. | #2208 v1 outputs/escalation/2206-low-config-density-utilities-v1-20261021.md |
| B:45 | not engaged | Answering decision items uses Update, self-correctables use ResolveSelfCorrectable; no answers made yet. |  |
| B:46 | engaged | The #2206 test plan covers every changed path, is run, and its results go on #2206. | outputs/escalation/2206-reading-waste-test-results-v1-20261021.md outputs/escalation/2208-ps-dir-setting-test-results-v1-20261021.md outputs/escalation/2209-rule-scope-test-results-v1-20261021.md |
| B:48 | not engaged | Prose-section writes need a change-log row in the same transaction; no prose writes. |  |
| B:49 | not engaged | Version column on covered rows points to its log row; no prose writes. |  |
| B:50 | not engaged | Log payload holds the prior state; no prose writes. |  |
| B:51 | not engaged | Hard deletes only on a specific researcher instruction each time; none given. |  |
| B:52 | not engaged | session_a_replace is author-gated to claude_code mechanical extracts; not used. |  |
| B:53 | not engaged | Catalogue patch before prose patch for a new chapter; not used. |  |
| B:55 | not engaged | New prose_section_type rows only on researcher instruction; not used. |  |
| B:56 | not engaged | File names lowercase, hyphenated, compact dates; no new file yet besides tool-made ones. |  |
| B:57 | not engaged | Snapshots versioned and archived, living docs kept stable; no file written yet. |  |
| B:58 | engaged | The v1 options file moved to archive when v2 replaced it. | outputs/escalation/archive/2177-reading-waste-options-v1-20261021.md |
| B:59 | engaged | New files filed by convention: escalation deliverables under outputs/escalation with id prefix. | outputs/escalation/2206-low-config-density-utilities-v1-20261021.md |
| B:60 | not engaged | Tool reports stay at their configured path, escalation write-ups under outputs/escalation; none yet. |  |
| B:61 | engaged | I leave inactive tables, columns and rows out of anything I report. |  |
| B:62 | engaged | The new setting and the migration register in cfg the same pass. | iba/app/migration/archive/reading_waste_2206_v1_20261021.py |
| B:63 | engaged | Claude-held backlog items either progress or are handed back with ready_for_approval and a stated resolution in one call. |  |
| B:64 | engaged | Escalation working files carry the escalation number first. | outputs/escalation/2206-reading-waste-test-results-v1-20261021.md |
| B:65 | not engaged | Audit deliverables cross-checked against open queue, term definitions and self-consistency; no audit in hand. |  |
| B:66 | not engaged | Cluster labels revisited when membership changes; no cluster changes. |  |
| B:67 | engaged | I keep research_db out of any IBA result except prose and maintenance utilities. |  |
| B:68 | not engaged | ib_observation changes only via a real fresh LLM answer; no observation work. |  |
| B:75 | engaged | The cfg write in this session went through apply_logged under a DEVMODE run id. | run DEVMODE-2206-READING-WASTE-20261021 and DEVMODE-2208-PS-DIR-SETTING-20261021 DEVMODE-2209-RULE-SCOPE-20261021 |
| B:80 | not engaged | Open-items lines in files carry a live handle; none written yet. |  |
| B:81 | engaged | This file: each rule restated in my words, ack given, conflicts listed, start check passing, evidence added later. |  |
| B:82 | engaged | At close nothing is committed while Session-Close shows an open finding. |  |
| B:83 | engaged | I work only from C:/Bible_study_projects and ignore other copies unless named. |  |
| B:96 | not engaged | Replaced content goes to its history home, the live home stays clean; nothing replaced yet. |  |
| B:97 | engaged | Each task here is checked against the Developer Mode boundary, has an escalation, is tested on a copy made with copy_db, and cfg writes use apply_logged; banner on every reply. | #2206 v6 outputs/escalation/2206-reading-waste-test-results-v1-20261021.md |
| B:98 | engaged | The sec 42 deviation (full lists stored in escalations) was fixed without asking. | iba/app/BUILD.md sec 372 |
| B:99 | engaged | I read each instruction against the whole conversation. |  |
| B:100 | engaged | Codes I mention come with their names. |  |
| B:101 | engaged | Any command the researcher must run is given complete in chat. |  |
| B:102 | engaged | The start report gives only checked facts with context, grouped by what the researcher asked. |  |
| B:103 | not engaged | New items in an established structure follow its convention; nothing added yet. |  |
| B:104 | not engaged | Search the live rules before proposing a new one; none proposed. |  |
| B:105 | engaged | A diagnosed gap goes to the researcher as a decision_required design before I build. | #2206 v4 |
| B:106 | not engaged | Designs I make avoid default per-item approval gates; no design yet. |  |
| B:107 | not engaged | Enumerate link tables before calling anything orphaned; no such verdict in hand. |  |
| B:108 | engaged | Text I write through tools is checked for escaping damage (0x08, dollar signs, here-strings). | iba/app/USER-GUIDE.md |
| E:1 | not engaged | Escalation source is code module, Claude or researcher; applies when I raise one. |  |
| E:2 | not engaged | No re-raising the same issue in the same state; applies when I raise one. |  |
| E:3 | not engaged | Module blocking gate is switched off pending redesign; nothing to do. |  |
| E:4 | engaged | Claude-assigned open items come before other work; I list them in the start report. |  |
| E:5 | engaged | Chat work items and researcher feedback get captured in escalations the same turn, quoted verbatim. | #2206 v1 #2177 v20 |
| E:7 | not engaged | Files named in escalation text use repo-relative paths; applies when I write one. |  |
| E:11 | not engaged | Standing items re-raised before any escalation table wipe; no wipe planned. |  |
| E:12 | engaged | Approved behaviour changes carried their GOVERNANCE.md and USER-GUIDE.md updates in the same build. | iba/app/GOVERNANCE.md iba/app/USER-GUIDE.md |
| E:13 | engaged | The approved item moved to in-progress before work was added. | #2206 v6 |
| E:15 | not engaged | Hand-back to researcher only for a real decision with evidence; none made yet. |  |
| E:16 | not engaged | Match a task against open threads before starting it; no task started. |  |
| E:17 | not engaged | Manual raises default to raised, threads to on-hold; applies when I raise one. |  |
| E:18 | not engaged | I run thread lifecycles to completion and write responses to history; no thread touched. |  |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

- none: the start check lists no rule naming a retired thing, and reading the rules found no conflict.

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

