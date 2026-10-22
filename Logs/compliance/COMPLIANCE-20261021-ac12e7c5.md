# Session compliance -- 20261021 -- session ac12e7c5-9668-4a70-ac93-a5627fd602c4

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything open or anomalous I find this session gets an escalation row, starting with the backlog read. | #2206 v1 #2177 v20 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | Reading BUILD history was the researcher's ask (why each control exists), not filling a missing step. | outputs/escalation/2177-reading-waste-options-v2-20261021.md |
| G:governance.primary_responsibility | engaged | I own coding and integrity of the app; this session is app work in Developer Mode. |  |
| G:governance.programme_stages | not engaged | Names the three stages (base data, analysis, publishing). Background only; no stage work in hand. |  |
| G:governance.project_change_rule | not engaged | Method changes go through the app, and legacy operations are migrated into it. No build task chosen yet; re-assessed when the researcher names one. |  |
| G:governance.project_operations | not engaged | Definition of what counts as a project operation; nothing to act on by itself. |  |
| G:governance.rules_must_be_config_driven | engaged | On the coming instruction I first confirm the rules for it are in cfg rows, and escalate any that live only in a document. | #2208 v7 iba/app/lib/cfgquality.py |
| G:governance.scope_iba_app | engaged | The app is the controller for all work; the developer task will be done inside it. |  |
| G:governance.scope_project | not engaged | States config covers the whole project; nothing specific to do yet. |  |
| G:governance.study_status | engaged | Study is on hold since 19 Oct; I start, continue or propose no study work, only app work. |  |
| B:1 | engaged | Backlog and state I report come from a live query this session, not recall. |  |
| B:2 | engaged | I confirm the compliance file passes and the marker file exists before calling those steps done. | #2206 v6 outputs/escalation/escalation-list-v186-20261021.md |
| B:4 | not engaged | Labels LLM-derived claims as inferential; no analytic claims produced in this setup. |  |
| B:10 | engaged | I never print or write the API key anywhere, including chat and commits. |  |
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
| B:27 | engaged | Multi-line arguments to commands use PowerShell here-strings, not bash heredocs. |  |
| B:28 | not engaged | A pasted error gets diagnosed, never sidestepped; none pasted. |  |
| B:31 | engaged | New guidance from the researcher this session goes into its cfg row or owning doc the same session. |  |
| B:34 | engaged | Claims about past state cite the record (git, DB, files). |  |
| B:36 | engaged | I avoid superlatives I have not checked against all candidates. |  |
| B:40 | engaged | Any open item I discover is put in the escalation table. | #2206 v1 #2177 v20 |
| B:44 | engaged | A new decision met while building stops the work and goes back for design; my own slips I fix and record. | #2208 v1 outputs/escalation/2206-low-config-density-utilities-v1-20261021.md |
| B:83 | engaged | I work only from C:/Bible_study_projects and ignore other copies unless named. |  |
| B:97 | engaged | Each task here is checked against the Developer Mode boundary, has an escalation, is tested on a copy made with copy_db, and cfg writes use apply_logged; banner on every reply. | #2206 v6 outputs/escalation/2206-reading-waste-test-results-v1-20261021.md |
| B:98 | engaged | The sec 42 deviation (full lists stored in escalations) was fixed without asking. | iba/app/BUILD.md sec 372 |
| B:99 | engaged | I read each instruction against the whole conversation. |  |
| B:100 | engaged | Codes I mention come with their names. |  |
| B:101 | engaged | Any command the researcher must run is given complete in chat. |  |
| B:102 | engaged | The start report gives only checked facts with context, grouped by what the researcher asked. |  |
| B:105 | engaged | A diagnosed gap goes to the researcher as a decision_required design before I build. | #2206 v4 |
| E:4 | engaged | Claude-assigned open items come before other work; I list them in the start report. |  |
| E:5 | engaged | Chat work items and researcher feedback get captured in escalations the same turn, quoted verbatim. | #2206 v1 #2177 v20 |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

- none: the start check lists no rule naming a retired thing, and reading the rules found no conflict.

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

