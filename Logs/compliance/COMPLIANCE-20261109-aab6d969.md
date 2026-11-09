# Session compliance -- 20261109 -- session aab6d969-cdd9-4d13-a43e-99ed3e216279

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything open or anomalous found while working on #2406 goes into an escalation row, not into prose or a code comment. | #2409 v1 (anomaly raised), #2411 v5, #2410 v2 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine forces me to dig through BUILD.md or old outputs to learn what to do, I stop and treat it as missing config. | #2406 v12 (the build followed the approved design and live config, no precedent reverse-engineered) |
| G:governance.primary_responsibility | engaged | Anything I build for #2406 must live inside the app, coded, controlled and maintained there. | iba/app/ps/Engagement.ps1; iba/app/lib/engagement.py |
| G:governance.programme_stages | not engaged | Names the three research stages; no stage-specific work is requested at declaration. |  |
| G:governance.project_change_rule | engaged | A change of operation or method in #2406 is channelled through the IBA app, and a past operation outside it is migrated. | iba/app/migration/archive/engagement_2406_v1_20261109.py |
| G:governance.project_operations | not engaged | Definition of a project operation; sets no action for this declaration. |  |
| G:governance.rules_must_be_config_driven | engaged | Any rule the #2406 work introduces needs a cfg_* row; on the new instruction I first confirm its governing rules are captured in config. | iba/app/migration/archive/engagement_2406_v1_20261109.py |
| G:governance.scope_iba_app | not engaged | Statement of scope; no separate action required. |  |
| G:governance.scope_project | not engaged | Statement of scope; no separate action required. |  |
| G:governance.study_status | not engaged | No study work was done: the session built and tested app tooling and did not read, weave or publish any verse reading. |  |
| B:1 | engaged | Database state is checked live before any step depends on it, never from earlier reports. | iba/app/tools/temp_2406_engagement_test_run.py (state read live from the copy before each step); #2411 v5 |
| B:2 | engaged | A step counts as done only after its output is confirmed to exist and match. | outputs/reports/engagement/engagement-aloud-check-20261109.md (output confirmed to exist); #2406 v10 |
| B:4 | engaged | Anything from an LLM, subagent or Ollama call is labelled inferential until sourced. | outputs/escalation/2406-engagement-step-detailed-design-v1-20261109.md |
| B:10 | not engaged | No API key was handled, logged or printed in this session. |  |
| B:16 | not engaged | The question tool was not needed: every question was put in plain chat text. |  |
| B:17 | engaged | For non-trivial #2406 work I state my understanding, plan and files, and wait for approval. | outputs/escalation/2406-engagement-step-detailed-design-v1-20261109.md |
| B:18 | engaged | Substantive output goes to a .md file; chat carries a summary and a pointer. | outputs/escalation/2406-engagement-step-detailed-design-v1-20261109.md |
| B:19 | engaged | I work only from verified facts and stop with a plain question when something is unclear. | #2406 v13 (asked which option on #2411 instead of guessing) |
| B:20 | engaged | I advise a cheaper path where one exists, such as targeted reads and dry runs first. | outputs/escalation/2406-engagement-step-detailed-design-v1-20261109.md |
| B:21 | engaged | Any open item raised in chat is recorded as an escalation in the same turn. | #2409 v1; #2411 v1 |
| B:22 | engaged | Once a plan is approved I run it through without re-confirming each step. | #2406 v12 |
| B:23 | engaged | A review or investigation ends with the fix made and verified unless scoped as investigation only. | #2406 v10 (built, tested and verified before hand-over) |
| B:24 | engaged | I show the actual query output and samples, and keep a structural pass distinct from fitness. | #2406 v10 (the per-case test results shown in the resolution) |
| B:25 | engaged | Read-only checks run without asking; writes stay inside an approved task. | iba/app/tools/temp_2406_engagement_test_run.py |
| B:27 | engaged | Multi-line strings in PowerShell use here-string syntax, never Bash heredoc, in any command meant for PowerShell. | #2406 v10 (resolution written through a PowerShell here-string) |
| B:28 | not engaged | No researcher-pasted error is in hand yet; applies if one arrives. |  |
| B:31 | engaged | Guidance given during #2406 is recorded the same session in a cfg row or the owning document. | #2406 v11; #2411 v5 |
| B:34 | engaged | Claims about project state or history are cited from the record, not from memory. | iba/app/BUILD.md |
| B:36 | engaged | No superlative is written unless every candidate was checked. | iba/app/BUILD.md |
| B:40 | engaged | Open items found anywhere in #2406 work, such as review findings, are recorded in escalation. | #2409 v1; #2411 v1 |
| B:44 | engaged | A new decision point in #2406 is terminal: recorded and routed to design, while my own slips against an approved design are fixed and recorded. | #2411 v5 |
| B:83 | not engaged | No file outside the project folder was used. |  |
| B:97 | engaged | This session is Developer Mode; only the configmaint.propose gate is lifted, and each new task is checked against the mode boundary. | Logs/compliance/COMPLIANCE-20261109-aab6d969.md |
| B:98 | engaged | A deviation from an established standard is fixed at once, not asked about. | #2410 v2 (the migration slip fixed at once) |
| B:99 | engaged | Each instruction on #2406 is read against the whole conversation and the escalation history. | #2406 v13 |
| B:100 | engaged | Codes are always shown with their names in anything I write. | outputs/escalation/2406-engagement-step-detailed-design-v1-20261109.md |
| B:101 | engaged | Commands the researcher must run are given complete and ready to run in PowerShell. | iba/app/USER-GUIDE.md |
| B:102 | engaged | Reports state only checked facts with context, grouped by the researcher's framing, open items in the register. | iba/app/BUILD.md |
| B:105 | engaged | Diagnosing a gap in #2406 does not license building the fix; the design goes to the researcher as decision_required first. | #2411 v1 (design to the researcher before the review step was built) |
| B:114 | not engaged | Governs study synergy phases; no study work in this session. |  |
| B:116 | not engaged | Governs reading verses in study work; none in this session. |  |
| B:123 | engaged | Before using any table or column in #2406, I read its recorded meaning in cfg_table and cfg_column and name it in my first message on that work. | outputs/escalation/2406-engagement-step-detailed-design-v1-20261109.md |
| B:124 | not engaged | No call to the Ollama server was made in this session. |  |
| B:125 | not engaged | No job running more than a few minutes was started. |  |
| E:4 | engaged | Open items assigned to Claude come first; I listed them at start and report them. | outputs/escalation/escalation-list-v249-20261109.md |
| E:5 | engaged | The next action comes from an escalation, and steps identified in chat are recorded there, such as on #2406. | #2411 v5; #2409 v1 |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

- SC3:cba5ccba :: recorded in #2406 v13
- SC3:b08ddeed :: recorded in #2406 v13
- SC3:b830baad :: recorded in #2406 v13
- SC3:3b9d798c :: recorded in #2406 v13
- SC3:cec01463 :: no record needed: an automated background-task notification (a stopped compliance-file command), not researcher words
- SC16:Collection-Build.ps1 :: fixed: the two failures were my own mistaken reads of Collection-Build.ps1 and handlers/base.py from a shell whose working folder had moved; the files were read again by full path, no tool failed
- SC16:Escalation.ps1_-Action_Update :: fixed: both refusals were my calls out of order (approving #2411 from a next_action other than ready_for_approval, and approving without a resolution); I put the item through ready_for_approval with its resolution first and the update then passed
- SC4b:cec01463 :: not held: an automated background-task notification, not researcher words

