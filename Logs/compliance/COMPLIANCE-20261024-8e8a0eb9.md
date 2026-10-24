# Session compliance -- 20261024 -- session 8e8a0eb9-e5eb-4c11-9e80-1516940a35ed

Mode: developer

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything left open, any anomaly I find and any clarification I need while building or fixing the app goes into the escalation table through Escalation.ps1, not into chat or a code comment. | #2266 v3 (findings recorded); #2268 v24 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine this session would need me to work out from BUILD.md, old logs or old outputs how it used to be done, I stop and raise the missing config as a gap instead of rebuilding the step from history. | not triggered: the build followed live config and the 2228 migration as a template; #2273 v4 |
| G:governance.primary_responsibility | engaged | I own the code and integrity of whatever I build or fix this session, so the operation it covers ends up coded and controlled inside the IBA app, including pulling in anything that still runs outside it. | iba/app/lib/observationrecord.py; iba/app/migration/archive/reading_phases_2273_v1_20261024.py |
| G:governance.programme_stages | engaged | I place any app change against the stage it serves (base data, analysis or publishing) and do not use the old Session A to D labels as if they described the current method. | outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md |
| G:governance.project_change_rule | engaged | Any change of process I make this session is made through the app (cfg rows and app code), and any old operation I touch that lives outside the app is migrated in, not patched outside it. | iba/app/migration/archive/reading_phases_2273_v1_20261024.py |
| G:governance.project_operations | engaged | I treat every script run, investigation and build step this session as a project operation, so each one falls under the app controls and rules. | outputs/escalation/2273-2274-test-results-v1-20261024.md |
| G:governance.rules_must_be_config_driven | engaged | Before acting on the instruction the researcher gives, I first check that the rules governing it are captured in cfg rows and read correctly there; a rule found only in a document or memory is escalated. | iba/app/migration/archive/reading_phases_2273_v1_20261024.py (reading.focus_words, reading.observe_prompts as cfg_setting) |
| G:governance.scope_iba_app | engaged | The app is the control point for all of my work this session; I do not run side processes that bypass it. | iba/app/ps/Reading.ps1 |
| G:governance.scope_project | engaged | When I change config I treat it as covering the whole project, not only the part of the app I am working on, and check knock-on effects elsewhere. | iba/app/BUILD.md (408: B:76 and narrative_home repointed) |
| G:governance.study_status | engaged | The study is active since 2026-10-23, so study work goes through Reading.ps1; in this Developer Mode session I do no study work, and any app change must not break the reading process. | iba/app/lib/reading.py (the reading process kept working; no study work done) |
| B:1 | engaged | Before any change that depends on what the database holds (counts, flags, presence of rows) I query the live iba.db first rather than relying on earlier reports or the commit log. | outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md |
| B:2 | engaged | I do not call a build or fix step done until I have checked that the file, write or report it was meant to produce exists and is right. | outputs/escalation/2273-2274-test-results-v1-20261024.md |
| B:4 | engaged | Anything I or a subagent conclude without a source I can point to is labelled inferential in reports and escalations, and stays so until evidence is cited. | outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md (arrangements marked as mine) |
| B:10 | engaged | If any work touches the Claude API configuration, the key value is never printed, logged, committed or put into an escalation. | no key handled; outputs/escalation/2273-2274-test-results-v1-20261024.md |
| B:16 | engaged | I never use AskUserQuestion (denied in settings.json); real judgement calls go to a md review file with options, and a short plain question goes in chat text. | outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md section 5 (decisions with options) |
| B:17 | engaged | For each non-trivial build or fix the researcher gives me, I first restate it, give the approach, scope and files, and wait for an explicit yes before starting. | #2273 v4; #2273 v10 |
| B:18 | engaged | Designs, plans, test results and findings from this session go into a md file first; chat gives a short summary and the file path. | outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md; outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md; outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md |
| B:19 | engaged | If a fact needed for the build is missing or unclear I stop and ask a real question in plain chat rather than assume. | #2273 v10 (plan put before the comparison) |
| B:20 | engaged | Where a cheaper route gives the same result (targeted queries instead of whole files, no subagent where a query is enough, dry run before live) I say so before acting. | outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md (read directly, no subagent) |
| B:21 | engaged | Any open item or judgement call that comes up in our chat is raised as an escalation in the same turn. | #2273 v6; #2273 v8; #2273 v12; #2273 v14 |
| B:22 | engaged | Once the researcher approves a build plan I carry it through to the end without asking again at each step. | #2273 v16 (built through after approval) |
| B:23 | engaged | A fix task ends with the fix built, tested on a copy and the tested result reported, not with a findings note, unless the researcher scoped it as investigation only. | outputs/escalation/2273-2274-test-results-v1-20261024.md |
| B:24 | engaged | When I report database or test results I show the actual query and rows or output, and keep a structural pass separate from whether the values are fit for use. | outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md (queries in section 5) |
| B:25 | engaged | I run read-only checks freely; writes to the database or code stay inside the task the researcher has approved. | outputs/escalation/2273-2274-test-results-v1-20261024.md |
| B:27 | engaged | Multi-line strings passed to PowerShell commands use the single-quoted here-string form; I do not use Bash heredocs in PowerShell calls. | #2273 v12 (here-strings in the PowerShell updates) |
| B:28 | engaged | If the researcher pastes an error I diagnose and fix that error, and never complete the step another way and call it done. | no error pasted by the researcher; outputs/escalation/2273-2274-test-results-v1-20261024.md |
| B:31 | engaged | New guidance or corrections from the researcher this session are written into a cfg row (or the owning document where config cannot hold it) in the same session. | iba/app/migration/archive/reading_phases_2273_v1_20261024.py (RG-04 restated from the D9 ruling) |
| B:34 | engaged | Statements I make about project state or earlier decisions cite the file, table row or escalation they come from. | outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md |
| B:36 | engaged | I write no superlative about code, data or options unless I have checked every candidate. | outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md |
| B:40 | engaged | Every open item I come across, from tests, validation runs or reading code, gets an escalation row, not a silent fix or a buried note. | #2266 v3 |
| B:44 | engaged | A point during a build that needs a new decision stops that work and goes back as an open item for design; a slip of my own against an approved design I fix, record and continue. | #2273 v6; #2274 v6 (design returned on each correction) |
| B:83 | engaged | I work only from C:\Bible_study_projects; a file elsewhere is used only if the researcher names it, and then brought into the project with their approval first. | outputs/escalation/2273-2274-test-results-v1-20261024.md |
| B:97 | engaged | Developer Mode is only for work where the app controls must be adjusted or get in the way; each task is checked against that and has an escalation, is tested on a dbsnapshot copy (never live), every cfg write goes through apply_logged and registers itself, and every reply opens with the banner. | outputs/escalation/2273-2274-test-results-v1-20261024.md (on a copy); iba/app/BUILD.md (408) |
| B:98 | engaged | Where my work drifts from an established pattern in the app code or config, I correct it straight away rather than asking whether to. | iba/app/BUILD.md (408: stale rows and worksheet comment fixed) |
| B:99 | engaged | I read each instruction against the whole conversation and scope its escalation by everything said about it. | #2273 v4 (read with the 14:26 instruction) |
| B:100 | engaged | In reports and designs I give every code with its name and I do not invent short codes. | outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md |
| B:101 | engaged | Where the researcher needs to run something (an approval, a PS step) I give the full ready-to-run PowerShell command in chat. | #2273 v17 (no command for the researcher to run) |
| B:102 | engaged | My status and close reports state only checked facts with context, grouped the way the researcher framed the question, with limits stated and open items in the register. | #2273 v17 |
| B:105 | engaged | Finding a gap does not let me build its fix in the same pass: the design goes to the researcher as decision_required first, and build work is never raised as self_correctable. | #2273 v6; #2273 v16 (built only after approval) |
| B:114 | not engaged | This session builds or fixes the app and does no study phase work; if a change touches the reading phases the tables stay the only source for claims and narrative. |  |
| B:116 | not engaged | No verse reading is done in this Developer Mode session; app changes must not hold back or gate the reading of a verse. |  |
| E:4 | engaged | Open items assigned to Claude come before other work, so I list them from the backlog check and put them to the researcher before starting anything new; on-hold threads do not count. | #2268 v24 |
| E:5 | engaged | The work I do this session comes from an escalation and the steps I find are recorded on one, with any researcher instruction or correction quoted word for word in the same turn. | #2273 v14; #2274 v14 |

## Conflicts and rules not followed

_(one line per rule: `- <id>: <the conflict, both sides named / why it is not or cannot be followed>`; every rule listed by the start check as naming a retired thing must be here)_

## Close dispositions

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

