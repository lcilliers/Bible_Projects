# Session compliance -- 20261027 -- session 6dfd4a14-17d3-4cdc-936a-98f890167798

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything left open, any anomaly or clarification I meet goes into the escalation table, not just chat. | #2314 v4; #2316 v1 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine forces me to dig through history to learn what to do, I treat that as a missing config row, stop, and raise it. | #2315 v5 |
| G:governance.primary_responsibility | engaged | Building and keeping the app whole is my job: every project operation must be coded and controlled in the app, including backfilling ones outside it. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| G:governance.programme_stages | not engaged | Describes the three stages of the programme (base data, analysis, publishing); background only, it asks nothing of this session. |  |
| G:governance.project_change_rule | engaged | Any change to how the project operates is made through the IBA app, and past operations living outside it get migrated in. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| G:governance.project_operations | not engaged | A definition of what counts as a project operation; no action of its own. |  |
| G:governance.rules_must_be_config_driven | engaged | No rule may live only in a document or memory: each needs a cfg row as evidence, and I check the config captures the rules before acting on a new instruction. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| G:governance.scope_iba_app | not engaged | States the IBA app is the central controller; a statement of scope, no separate action. |  |
| G:governance.scope_project | not engaged | States config covers the whole project; a statement of scope, no separate action. |  |
| G:governance.study_status | engaged | Study is ACTIVE since 2026-10-23, so study_active rules apply; this session builds the app and does no study reading unless asked. | #2314 v4 (no study reading run this session) |
| B:1 | engaged | Before relying on any database state I query the live db myself, not what an earlier report said. | outputs/escalation/2314-0c-gap-pre-observe-clearout-table-20261027.md |
| B:2 | engaged | A step is done only after I confirm the output exists and is right, not because the command ran. | Logs/compliance/COMPLIANCE-20261027-6dfd4a14.md |
| B:4 | engaged | Anything derived by a model or subagent without source grounding is labelled inferential until new evidence is cited. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| B:10 | engaged | The API key value never appears in any output, file or commit. | #2315 v5 (no key value written) |
| B:16 | engaged | I never use AskUserQuestion; facts come from investigation, real judgement calls go into a review file, small questions in plain chat. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| B:17 | engaged | For non-trivial work I state my understanding, plan and files first and wait for explicit approval; trivial steps are exempt. | #2314 v2; outputs/escalation/2314-0c-gap-pre-observe-clearout-table-20261027.md |
| B:18 | engaged | Substantive output is written to a md file first; chat gets a short summary and the pointer. | outputs/escalation/2314-0c-gap-pre-observe-clearout-table-20261027.md |
| B:19 | engaged | I work only from verified facts and stop to ask in plain chat when something is missing, never guessing. | #2314 v2 |
| B:20 | engaged | I flag a cheaper route (targeted read, dry run first, no needless subagent) before taking a costly one. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| B:21 | engaged | Any open item or judgement call surfacing in chat is recorded as an escalation in that same turn. | #2316 v1; #2314 v1 |
| B:22 | engaged | Once a plan is approved I carry it through without reconfirming each step. | #2314 v4 |
| B:23 | engaged | An investigation is not finished at the finding: I implement and verify the fix and report the verified result, unless scoped as investigation only. | #2262 v5 |
| B:24 | engaged | I show the actual queries and sample rows, and keep structural validity distinct from fitness of the values. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| B:25 | engaged | Read-only checks need no permission; writes stay inside the approved task. | outputs/escalation/2314-0c-gap-pre-observe-clearout-table-20261027.md |
| B:27 | engaged | Multi-line string arguments in PowerShell use the single-quoted here-string form, not bash heredocs. | #2315 v5 |
| B:28 | engaged | A pasted error is diagnosed and fixed, not worked around and then reported as done. | #2317 v1 |
| B:31 | engaged | Rulings or method changes the researcher gives this session are recorded in a cfg row or the owning document the same session. | #2315 v5 |
| B:34 | engaged | Claims about project state or past decisions are cited from files or the database, not memory. | outputs/escalation/2314-three-steps-design-and-build-status-20261027.md |
| B:36 | engaged | No superlatives unless every candidate was checked. | #2314 v4 |
| B:40 | engaged | Every open item found anywhere (review, validation, sweep) gets an escalation row, not a silent fix or buried note. | #2316 v1 |
| B:44 | engaged | A point needing a new decision during a build is recorded and routed back to design, not settled inline; my own slips against an approved design I fix and record. | #2315 v4 |
| B:83 | engaged | Only C:\Bible_study_projects is authoritative; other copies are used only when named and brought in with approval. | outputs/escalation/2314-three-steps-design-and-build-status-20261027.md |
| B:97 | engaged | This session is in Developer Mode at the researcher's start; only the configmaint.propose approval gate is lifted. Each task is checked against the mode boundary, has an escalation, and is tested on a copy. | #2314 v4; #2315 v5; #2316 v1 |
| B:98 | engaged | Departures from an established pattern I fix at once instead of asking whether to. | #2262 v5 |
| B:99 | engaged | I read each instruction against the full conversation and what the researcher said about the item. | #2315 v5 |
| B:100 | engaged | Codes appear with their names and glosses, and design documents use descriptive names. | outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| B:101 | not engaged | no command was for the researcher to run this session |  |
| B:102 | engaged | Reports hold checked facts with context, grouped as the researcher framed it, limits stated, open items registered. | outputs/escalation/2314-0c-gap-pre-observe-clearout-table-20261027.md |
| B:105 | engaged | Diagnosing a gap does not license building its fix: a design goes to the researcher as decision_required first. | #2262 v5; outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md |
| B:114 | not engaged | Governs the phases of study work; this session builds the app and starts no study reading. |  |
| B:116 | not engaged | Governs how study reading begins; no verse is read in this session unless the researcher asks. |  |
| E:4 | engaged | Escalations assigned to Claude come before other work; they are listed at the start. | #2314 v4; #2262 v5 |
| E:5 | engaged | Next actions come from escalations and chat-only open questions get an escalation the same turn. | #2316 v1; #2315 v5 |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

- SC4b:7166b021 :: in register #2262
- SC4b:54180400 :: in register #2315
- SC4b:3ff90528 :: in register #2316
- SC4b:fcfd0faa :: in register #2315
- SC4b:d85f7358 :: in register #2316
- SC16:Bash:_python:70fd1ef0 :: carried #2317
- SC16:Escalation.ps1_-Action_History :: carried #2317
- SC16:Escalation.ps1_-Action_Update :: fixed: one call ran from the wrong folder and was re-run with the full path; the rest were the same transient command-check failure

