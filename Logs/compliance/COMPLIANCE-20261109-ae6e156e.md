# Session compliance -- 20261109 -- session ae6e156e-cc29-46d1-88e6-6f1d37bb4c59

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Every open item, anomaly or clarification I meet this session gets an escalation row, never only a chat remark. |  |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If I have to dig through history to learn how a registered routine runs, I stop and report a config gap instead of reconstructing it. |  |
| G:governance.primary_responsibility | not engaged | No app-building or back-filling work is in hand at start; applies if the researcher asks for development. |  |
| G:governance.programme_stages | not engaged | Background definition of the three stages; no task requires acting on it yet. |  |
| G:governance.project_change_rule | engaged | Any change of method I am asked for goes through the IBA app rather than ad hoc scripts. |  |
| G:governance.project_operations | not engaged | A definition of what counts as an operation; nothing to act on at start. |  |
| G:governance.rules_must_be_config_driven | engaged | Before acting on a new instruction I check its governing rules exist as cfg rows, and escalate if one lives only in a document. |  |
| G:governance.scope_iba_app | not engaged | Statement of scope; no separate action. |  |
| G:governance.scope_project | not engaged | Statement of scope; no separate action. |  |
| G:governance.study_status | engaged | Study is active, so study work goes through Reading.ps1 and the narrative lives in iba.db; no hold applies. |  |
| B:1 | engaged | Check live database state directly before relying on counts or flags, not on earlier reports. |  |
| B:2 | engaged | Confirm each file or database output exists and matches before calling a step done. |  |
| B:4 | engaged | Label anything model-derived and ungrounded as inferential until sourced. |  |
| B:10 | engaged | Never print or log the API key in any output. |  |
| B:16 | engaged | Do not use the AskUserQuestion tool; ask plainly in chat or write a review file. |  |
| B:17 | engaged | Before non-trivial work, restate the instruction and plan and wait for approval. |  |
| B:18 | engaged | Put substantial output in a .md file and keep chat to a pointer and summary. |  |
| B:19 | engaged | Work only from verified facts and stop to ask when facts are missing. |  |
| B:20 | engaged | Flag a cheaper route before acting where one exists. |  |
| B:21 | engaged | Open items raised in chat are recorded as escalations the same turn. |  |
| B:22 | engaged | Once a plan is approved, run it through without re-confirming each step. |  |
| B:23 | engaged | Investigations end with the fix implemented and verified unless scoped as investigation-only. |  |
| B:24 | engaged | Show actual query output and samples rather than smoothed summaries. |  |
| B:25 | engaged | Read-only checks run without asking; writes stay inside approved scope. |  |
| B:27 | engaged | Multi-line strings in PowerShell use at-sign quote here-strings, never Bash heredocs. |  |
| B:28 | engaged | A pasted error is diagnosed and fixed, not routed around. |  |
| B:31 | engaged | New researcher guidance is recorded in the proper cfg row or owning document in the same session. |  |
| B:34 | engaged | State claims about project state only with a cited written record. |  |
| B:36 | engaged | No superlatives unless every candidate was checked. |  |
| B:40 | engaged | Open items found anywhere go into the escalation table. |  |
| B:44 | engaged | A new decision point stops work and is recorded; only slips against settled design are self-corrected. |  |
| B:83 | engaged | Use only the project folder as authority; outside copies only when named, and flagged. |  |
| B:98 | engaged | Deviations from settled standards are fixed at once, not offered as questions. |  |
| B:99 | engaged | Read each instruction against the whole conversation. |  |
| B:100 | engaged | Show codes with their names, never bare. |  |
| B:101 | engaged | When the researcher must run something, give the full ready PowerShell command. |  |
| B:102 | engaged | Status reports contain checked facts only, with context and stated limits. |  |
| B:105 | engaged | Diagnosis does not authorise building; designs go to the researcher first. |  |
| B:114 | not engaged | No study reading in hand at start. |  |
| B:116 | not engaged | No study reading in hand at start. |  |
| B:123 | engaged | Read recorded table and column meaning before using them, and name what I read. |  |
| B:124 | not engaged | No external service such as Ollama is used at start. |  |
| B:125 | not engaged | No long-running job in hand at start. |  |
| E:4 | engaged | Open escalations assigned to Claude come before other work. |  |
| E:5 | engaged | Next actions come from escalations, and researcher comments are captured in them verbatim the same turn. |  |

## Conflicts and rules not followed

none

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

