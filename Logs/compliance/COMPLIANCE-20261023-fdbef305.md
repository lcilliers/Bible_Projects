# Session compliance -- 20261023 -- session fdbef305-1bb6-457b-888d-80a491479be6

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything I find open or anomalous during start-up or the task the researcher picks goes into the escalation table through Escalation.ps1, not left in chat or a file. | #2166 v2 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine this session makes me dig through BUILD.md, old logs or old outputs to work out a missing step, I stop that routine and raise the gap instead of rebuilding the step from history. || BUILD.md sec 151 was read only to confirm the #729 ruling; the apply was registered as a cfg_step before it was run: #2241 v4 |
| G:governance.primary_responsibility | engaged | Whatever operation I run this session must run through an IBA app tool; if I meet one that is outside the app, I own getting it registered and coded, raised as an escalation first. | #2241 v4 |
| G:governance.programme_stages | engaged | When I describe work this session I place it in the right stage (base data, analysis, publishing) and do not use the old Session A/B/C/D labels as current terms. || no stage label used as a current term; the work was app process work on the prose store: iba/app/BUILD.md sec 400 |
| G:governance.project_change_rule | engaged | If the task chosen changes how something is done, the change is made in the app (config and code), not as an ad-hoc script or a manual step. | #2241 v2 |
| G:governance.project_operations | engaged | Every script, query, reading or investigation I do this session counts as a project operation and so falls under the app-control rules above. || every operation ran through a PS tool with a run id, e.g. RUN-20261023_141514_208-PROSE, RUN-20261023_140112_982-CONFIGMAINT |
| G:governance.rules_must_be_config_driven | engaged | For the instruction the researcher gives after start-up, I first check that its governing rules exist as cfg rows; a rule I find only in a document or memory is raised as an escalation. || the rules governing #2212 were checked as cfg rows before building (cfg_write_grant apply_session_patch, B:48-50, B:53, governance.prose_canonical_authority): outputs/escalation/2212-plan-v1-20261023.md |
| G:governance.scope_iba_app | engaged | I treat the IBA app as the controller for all work this session: I use its PS tools and cfg rows rather than working around them. || the prose patch apply brought into the app as a registered step: #2241 v4 |
| G:governance.scope_project | engaged | I apply config rules to every part of the project I touch this session, not only to the app folder. || bible_research.db prose writes now go through the app: iba/app/lib/prosestore.py |
| G:governance.study_status | engaged | The study is active, so any study work picked this session goes through Reading.ps1 and its three gates with the narrative held in iba.db; I do not use the retired strand steps. || no study work was chosen this session, so no reading was opened and no retired strand step run |
| B:1 | engaged | Before I act on any count, flag or row existence this session I query the live database for it, rather than trusting the last session log or the escalation list from memory. | outputs/escalation/2166-escalation-history-v1-20261023.md |
| B:2 | engaged | I only call a step done once I have checked its output exists and is right, starting with this compliance file passing its Check and the escalation and thread reports being written. | outputs/escalation/2212-apply-patch-test-results-v1-20261023.md |
| B:4 | engaged | Any classification or link I or a subagent produce this session that is not read straight from source data I mark as inferential. || no LLM classification produced; the meaning of the researcher phrase the new method was left as worded, not inferred: #2166 v3 |
| B:10 | engaged | If any call this session touches the Claude API, its key value never appears in output, payloads, chat or commits. || no Claude API call was made this session |
| B:16 | engaged | I will not use AskUserQuestion; at the end of start-up I ask what to work on in plain chat, and any real choice with options goes into a .md review file. || AskUserQuestion not used; the #2212 decision went to a review file: outputs/escalation/2212-plan-v1-20261023.md |
| B:17 | engaged | Once the researcher names a task, if it is non-trivial I state my understanding, the plan and the files affected, and wait for approval before doing it. || the #2212 plan and options were put to the researcher before any build: #2212 v3 |
| B:18 | engaged | Any analysis, plan or report I produce this session is written to a .md file first; chat carries a short summary and the pointer. The start-up report itself is findings only, from the report files written by the tools. | outputs/escalation/2212-plan-v1-20261023.md |
| B:19 | engaged | Where a fact I need is missing I stop and ask in plain chat rather than filling it with an assumption. || which method the researcher meant on #2166 was not guessed; the record keeps their words: #2166 v3 |
| B:20 | engaged | I flag a cheaper route when one exists, such as targeted greps over whole-file reads and direct queries over subagents, before taking the costly one. || targeted greps and line-range reads of scripts/archive/apply_session_patch.py instead of a whole read; no subagent used |
| B:21 | engaged | An open item or judgement call that comes up in chat this session gets its escalation in the same turn; detail is held in E:5. || the #2212 instruction taken up in the same turn: #2212 v2; the developer-mode instruction recorded late, see conflicts section: #2212 v8 |
| B:22 | engaged | After the researcher approves a plan this session I carry it through to the end without asking again at each step. | iba/app/BUILD.md sec 400 |
| B:23 | engaged | If the task chosen is a review or investigation, I implement and verify the fix and report the verified result, unless it was scoped as investigation only. | #2212 v7 |
| B:24 | engaged | When I report database state or results I show the query and real rows, and do not present a passing structural check as proof the values are fit for use. | outputs/escalation/2212-apply-patch-test-results-v1-20261023.md |
| B:25 | engaged | I run read-only checks (start-up tools, list, audit, queries) without asking; anything that writes stays inside an approved task. || read-only checks ran unasked: Escalation List, ThreadAudit, configmaint.validate RUN-20261023_140112_982-CONFIGMAINT |
| B:27 | engaged | Any multi-line argument I pass in a command this session uses a PowerShell single-quoted here-string, not Bash heredoc. || multi-line Python for the read-only database checks passed as PowerShell here-strings; a Bash heredoc attempt failed and was replaced by an Edit |
| B:28 | engaged | If the researcher pastes an error this session I diagnose and fix that error rather than completing the step some other way. || no error was pasted by the researcher this session |
| B:31 | engaged | Any new guidance or correction the researcher gives this session I record the same session in a cfg row or the owning document, not only in memory. || the researcher guidance on developer mode recorded in iba/app/BUILD.md sec 400 and #2212 v8 |
| B:34 | engaged | Claims I make about past sessions or decisions I ground in a cited file, table row or commit, such as the session logs or the escalation table. || claims about the #729 ruling cited from iba/app/BUILD.md sec 151 |
| B:36 | engaged | I do not write a superlative such as clearest or strongest unless I have checked every candidate. || no superlative written this session |
| B:40 | engaged | Open items surfacing from tool output this session (thread audit findings, check failures) are tracked as escalation rows, not just mentioned in the report. || tool-raised items kept in the register: #2244 v2 resolved, #2245 v1 raised, #2240 left open |
| B:44 | engaged | If a point in the work needs a new decision I stop and route it as an open item for design; a slip of my own against an approved design I fix, record and continue. | #2212 v3 |
| B:83 | engaged | I work only from C:\Bible_study_projects; copies on G:\My Drive, Zotero or Documents are ignored unless the researcher names one, and then brought in with approval first. || only files under C:\Bible_study_projects were used |
| B:98 | engaged | Where something I do departs from an established standard, I conform it straight away rather than asking whether to. || line endings of iba/app/lib/prosestore.py and iba/app/BUILD.md conformed to LF at once; BUILD.md sec 400 moved into order |
| B:99 | engaged | I read each instruction the researcher gives against the whole conversation so far, including this start-up, and scope escalations accordingly. || the #2212 options were scoped against the #729 ruling and the prose rules met in the session: outputs/escalation/2212-plan-v1-20261023.md |
| B:100 | engaged | In chat I give cluster codes with their names, Strong's numbers or transliterations with their glosses, and step codes with names, never bare. || clusters named with code and name in the start report (M64 Will & Resolve, M72 Authority & Dominion, M08, M09, M18 with names) |
| B:101 | engaged | When the researcher needs to run a command, for example an approval, I give the full ready-to-run PowerShell command in chat. || a ready-to-run approval command for #2212 and its three config rows was given in chat |
| B:102 | engaged | The start-up report and any later status give only checked facts with their context, no bare counts or inferred dependencies, grouped by what the researcher asked. || the start report gave findings only, from outputs/escalation/escalation-list-v194-20261023.md and outputs/escalation/escalation-thread-audit-v7-20261023.md |
| B:105 | engaged | If I diagnose a gap this session I take a design to the researcher as decision_required before building anything, and never raise build work as self_correctable. | #2212 v3 |
| B:114 | engaged | If study work is chosen I follow scope, collate, record gaps, then synergise only from the tables through the app, never from memory of earlier readings. || no study work this session |
| E:4 | engaged | Open escalations assigned to Claude come before other work; I name them first in the report, and only threads that are in-progress count as work first. || the start report first said no item was assigned to Claude, checking only open items; the four parked Claude items were named and acknowledged in the next turn and each turn after |
| E:5 | engaged | Work comes from and is recorded in escalations; researcher comments touching an item are captured in that item the same turn with the operative words quoted verbatim. | #2166 v3 |

## Conflicts and rules not followed

- E:5: not followed in full. The researcher instruction "you do not need developer mode - prepare the changes and present them to me for approval." was quoted in iba/app/BUILD.md sec 400 but reached an escalation only at close (#2212 v8), not in the turn it was given.

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_
- SC3:66ca99a3 :: recorded in #2166 v3
- SC16:Escalation.ps1_-Action_Update :: fixed: my own slip, not a tool defect: twice I tried to close a decision item straight to approved/noted; corrected the same turn by the documented two-step (ready_for_approval then approved, #2166 v2 and v3), the path B:45 and USER-GUIDE sec 3 give at the point of use. The third line counted is a successful update from a call whose exit came from a later designed stop.
- SC16:Prose.ps1_-Step_ApplyPatch :: carried #2245
