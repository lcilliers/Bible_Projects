# Session compliance -- 20261102 -- session c8d7b83e-8348-40d9-8688-8c11e1524408

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything open, odd or unclear that I meet goes into the escalation table, never only into chat. |  |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If I must dig through history to learn how a registered routine runs, I treat that as a missing config and escalate it instead of reverse-engineering. |  |
| G:governance.primary_responsibility | engaged | Building and keeping the app whole is my job; work outside the app is to be brought in, not left loose. |  |
| G:governance.programme_stages | not engaged | Describes the three research stages; background only for app-building work this session. |  |
| G:governance.project_change_rule | engaged | Any change of method I make goes through the app; past out-of-app operations are migrated in. |  |
| G:governance.project_operations | not engaged | Definition of a project operation; no separate action required. |  |
| G:governance.rules_must_be_config_driven | engaged | Every rule I add lives in a cfg row; on a new instruction I first check the governing rules are in config and escalate if not. |  |
| G:governance.scope_iba_app | not engaged | Statement of scope; nothing to do beyond the other rules. |  |
| G:governance.scope_project | not engaged | Statement of scope; nothing to do beyond the other rules. |  |
| G:governance.study_status | engaged | Read it before any study work; it says ACTIVE since 2026-10-23. This session builds the app and starts no study work. |  |
| B:1 | engaged | Check database state live before relying on it; no remembered counts or flags. |  |
| B:2 | engaged | A step is done only when its output is confirmed to exist and be right. |  |
| B:4 | engaged | My own conclusions and subagent reports are labelled inferential until grounded in citable source data. |  |
| B:10 | engaged | Never print, log or commit the API key value. |  |
| B:16 | engaged | No AskUserQuestion; real judgement calls go to a review md file, simple clarifications in plain chat. |  |
| B:17 | engaged | Before non-trivial work I state what I understood, the plan and the files affected, then wait for approval. |  |
| B:18 | engaged | Substantive output goes to an md file; chat carries a short summary and a pointer. |  |
| B:19 | engaged | No guessing; if a fact is missing I stop and ask in plain chat. |  |
| B:20 | engaged | Say so when a cheaper route exists: targeted reads, direct queries, dry run before live. |  |
| B:21 | engaged | An open item raised in chat is escalated in the same turn. |  |
| B:22 | engaged | Once a plan is approved I run it through without re-asking at each step. |  |
| B:23 | engaged | A fix is built, verified and reported with its outcome, not left as a finding, unless scoped as investigation only. |  |
| B:24 | engaged | Show the actual queries and sample rows; do not mix a structural pass with fitness of the values. |  |
| B:25 | engaged | Read-only checks run without asking; changes stay inside the approved task. |  |
| B:27 | engaged | Multi-line strings in PowerShell use here-string syntax; bash heredocs only in the Bash tool. |  |
| B:28 | engaged | A pasted error is diagnosed and fixed, not bypassed. |  |
| B:31 | engaged | New guidance from the researcher is written into the authoritative record (a cfg row or owning doc) the same session. |  |
| B:34 | engaged | Claims about project state or past decisions are cited from files or the database. |  |
| B:36 | engaged | No superlatives unless every candidate was checked. |  |
| B:40 | engaged | Any open item found during development is recorded in the escalation table, not a silent fix or comment. |  |
| B:44 | engaged | A new decision point stops work and is routed back to design; only slips against an approved design are self-corrected and recorded. |  |
| B:83 | engaged | Only C:\Bible_study_projects is authoritative; other copies are used only when the researcher names them, with a note. |  |
| B:97 | engaged | Developer Mode is declared for this session. Only the configmaint.propose gate is lifted; each task is checked against the boundary, has an escalation, and is tested on a copy. |  |
| B:98 | engaged | A deviation from a settled standard is fixed at once, not asked about. |  |
| B:99 | engaged | I interpret every researcher message in light of everything said earlier on that topic, including how an escalation was scoped. |  |
| B:100 | engaged | Codes are shown with their names; design docs use descriptive names. |  |
| B:101 | engaged | When the researcher must run something, I give the full ready-to-run PowerShell command in chat. |  |
| B:102 | engaged | Reports state only checked facts with context, concise, limits stated, open items registered. |  |
| B:105 | engaged | Diagnosing a gap is not leave to build the fix; a design goes to the researcher as decision_required first. |  |
| B:114 | not engaged | Concerns study phases and claims from tables; no study work is planned this session. |  |
| B:116 | not engaged | Concerns reading verses first in study work; none planned this session. |  |
| B:123 | engaged | Before using any table or column I read its recorded meaning in cfg_table and cfg_column and name it in my first message on that work. |  |
| E:4 | engaged | Open items assigned to Claude come before other work; I list them at declaration. |  |
| E:5 | engaged | Next actions come from escalations; judgement calls surfaced in chat get an escalation the same turn. |  |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

