# Session compliance -- 20261023 -- session 79edf1db-f44d-46de-aaef-ec5371e7e5c3

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | Anything I find open, odd or unclear while starting up or in the work the researcher picks goes into the escalation table under its rules, not only into chat. | #2247 v6; OT-108.25, OT-108.26, OT-108.27 (RUN-20261023_202056_879-OPENITEM) |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | If running a registered routine this session needs me to dig through BUILD.md, old logs or old outputs to learn how it was done, I stop, name the missing config row, and get it registered and built before running the routine. | #2256 v1 (the gate 2 gap raised instead of rebuilding batch A order from precedent) |
| G:governance.primary_responsibility | engaged | I own keeping the app the controller of the work: whatever I do this session runs through IBA tools, and any operation I find living outside the app I flag to be brought in. | #2256 v1; #2254 v2 |
| G:governance.programme_stages | engaged | I place the chosen work in the right stage (base data, analysis or publishing) and use the current methods of that stage, not the old Session A-D ways. | outputs/reading/m64-dedicate/m64-dedicate-account-v1-20261024.md |
| G:governance.project_change_rule | engaged | Any change of method or approach that comes up this session goes through the app as config and code; an old operation found outside it is listed for migration. | #2255 v4 (rule through configmaint.propose) |
| G:governance.project_operations | engaged | I treat every research, development or script-running activity this session, the startup routine included, as an operation the app governs. | outputs/reading/m64-plan/m64-plan-account-v1-20261023.md |
| G:governance.rules_must_be_config_driven | engaged | When the researcher gives the next instruction I first check the rules for it exist as cfg rows and read them correctly; a rule found only in a document or memory is escalated. | #2253 v5 (the guidance captured as cfg_behaviour_rule 116) |
| G:governance.scope_iba_app | engaged | I run the session's work through the IBA app scripts (Start-Iba, Compliance, Escalation, Reading and the like) rather than ad hoc steps. | RUN-20261023_201133_101-READING to RUN-20261023_202207_749-READING (Reading.ps1 Open to Account) |
| G:governance.scope_project | engaged | Config questions I meet are judged against the whole project, not only the app folder or the piece in hand. | outputs/escalation/2188-instruction-files-to-config-mapping-v1-20261024.md |
| G:governance.study_status | engaged | The study is active again since today, so study work the researcher asks for is done only through Reading.ps1 and its three gates with the narrative in iba.db; no strand steps. | outputs/reading/m64-willing/m64-willing-account-v1-20261023.md (published, 0 gaps) |
| B:1 | engaged | Before I act on any count, flag or row this session I query the live iba.db for it, not what a report or earlier session said. | read-only queries of reading, narrative_claim, ib_observation before Apply and after Publish (reading m64-willing published 2026-10-23T19:21:57Z) |
| B:2 | engaged | I call a step done only after I have looked at the file, row or report it was meant to produce, e.g. the escalation list and thread audit reports written at start. | gate checks RUN-20261023_201612_747-READING (gate 1) and RUN-20261023_202137_130-READING (gate 2); C-346 to C-355 current, verified in iba.db |
| B:4 | engaged | Anything I or a subagent conclude without a source behind it is marked inferential in what I write, and stays so until a citation backs it. | outputs/escalation/2247-batch-d-verses-in-context-v1-20261024.md (readings marked I read) |
| B:10 | engaged | Should any step touch the Claude API key, its value never appears in my output, logs, escalations or commits. | Logs/SESSION-LOG-20261024-2247-m64-reading-b-to-d.md (no Claude API call made this session) |
| B:16 | engaged | I do not use AskUserQuestion; a judgement call goes to a .md review file with options, and a short clarification is asked in plain chat. | outputs/escalation/2247-batch-d-decision-v2-20261024.md |
| B:17 | engaged | Once the researcher names the work, if it is more than a single step I summarise it, state scope and files, and wait for a yes before doing it. | #2253 v2 (rule proposed, built only after approval) |
| B:18 | engaged | Substantial findings or plans from this session go into a .md file first; chat gets a short summary and the pointer. | outputs/escalation/2253-reading-before-process-rules-v1-20261024.md |
| B:19 | engaged | Where a fact I need is missing I stop and ask a real question instead of filling the gap with a guess. | #2247 v8 |
| B:20 | engaged | I point out a cheaper way to do the chosen work when one gives the same result, e.g. a targeted query instead of a whole-file read or a subagent. | Logs/SESSION-LOG-20261024-2247-m64-reading-b-to-d.md |
| B:21 | engaged | An open item or judgement call that comes up in chat this session is put into an escalation in the same turn. | #2253 v1; #2256 v1 |
| B:22 | engaged | Once the researcher approves a plan I carry its steps through without asking again at each one. | #2247 batch B run Open to Publish under approved plan outputs/escalation/2247-ot108-3-reading-plan-v1-20261023.md decision 1a |
| B:23 | engaged | For any review or investigation I am given, I fix, verify and report the verified result unless told it is investigation only. | #2256 v4 |
| B:24 | engaged | When I report database or check results I show the actual rows or output, and keep structural passes separate from fitness of the values. | #2247 v6 |
| B:25 | engaged | Read-only checks such as the start scripts and queries I run without asking; anything that writes stays inside work the researcher has approved. | #2247 v6 |
| B:27 | engaged | Multi-line arguments in my commands use PowerShell here-strings, not Bash heredocs. | #2247 v7 |
| B:28 | engaged | If the researcher pastes an error this session, I diagnose and fix that error rather than reaching the result another way. | Logs/SESSION-LOG-20261024-2247-m64-reading-b-to-d.md (no error pasted by the researcher this session) |
| B:31 | engaged | Any new guidance or correction from the researcher this session I write into a cfg row, or the owning document where it is not config, before the session ends. | #2253 v5 |
| B:34 | engaged | Statements I make about past decisions or state are cited to files or database rows, not recalled. | outputs/escalation/2253-reading-before-process-rules-v1-20261024.md |
| B:36 | engaged | I write no most, strongest or clearest claim unless I have checked every candidate. | outputs/escalation/2247-batch-d-verses-in-context-v1-20261024.md |
| B:40 | engaged | Any open item that surfaces from a check, review or report this session, e.g. a thread audit finding, gets an escalation row rather than a silent fix or a buried mention. | OT-108.25, OT-108.26, OT-108.27 raised for the held drafts |
| B:44 | engaged | While working, a point needing a new decision stops that work and goes to an open item; a slip of my own against an approved design I fix, record and continue. | #2256 v1 |
| B:83 | engaged | I use only files under C:\Bible_study_projects; a file from Drive, Zotero or elsewhere is used only when the researcher names it and after it is brought into the project with approval. | outputs/escalation/2188-instruction-files-to-config-mapping-v1-20261024.md |
| B:98 | engaged | Where my work departs from an established pattern I fix it at once rather than asking whether to. | #2254 v2 |
| B:99 | engaged | I read each instruction the researcher gives against the whole of this conversation and the escalation it relates to. | #2188 v9 |
| B:100 | engaged | In chat and files I give cluster, step and dimension codes with their names and transliterations with glosses, e.g. OT-108 with its title when I report open items. | outputs/escalation/2247-batch-d-verses-in-context-v1-20261024.md |
| B:101 | engaged | When the researcher must run a command, such as an approval, I give the full PowerShell line ready to paste. | #2255 v3 |
| B:102 | engaged | The start report and any later status report carry only checked facts with context, grouped the researcher's way, no bare numbers, open items placed in the register. | Logs/SESSION-LOG-20261024-2247-m64-reading-b-to-d.md |
| B:105 | engaged | If I diagnose a gap this session I take a design to the researcher as decision_required before building anything; build work is never marked self_correctable. | #2256 v1 |
| B:114 | engaged | If study work is chosen, I resolve scope, collate what is known, record the gaps in the tables, and only then synergise from the tables, never from memory of earlier readings. | RUN-20261023_201634_282-READING (synergy built from the tables after gate 1) |
| E:4 | engaged | Open items assigned to Claude are worked before anything else the researcher does not override; on-hold threads do not count as work first. | #2247 v6 (the Claude-assigned item worked first) |
| E:5 | engaged | The next work comes from an escalation, and anything the researcher or I raise in chat that is open is captured in an escalation the same turn, quoting the operative words verbatim. | #2247 v6 quotes the instruction verbatim |

## Conflicts and rules not followed

- None found at start.

## Close dispositions

- SC3:f7a9c321 :: no record needed: a bare go-ahead for batch D under the approved plan decision 1a, acted on from #2247 v8
- SC3:72c6d543 :: no record needed: a bare approval of #2255, which the researcher recorded in #2255 v3
- SC3:61781cd5 :: no record needed: a bare approval of #2257 and #2258, which the researcher recorded in #2257 v3 and #2258 v3
- SC3:fcee670e :: no record needed: a bare approval of #2188's mapping step, which the researcher recorded in #2188 v7
- SC4b:386954eb :: in register OT-91.11
- SC4b:61781cd5 :: not held: an approval, applied in #2257 v4 and #2258 v4
- SC4b:fcee670e :: not held: an approval of the #2188 mapping step, done in #2188 v8 and closed in #2188 v10

_(session-close: one line per finding still open: `- <finding key> :: fixed` | `:: carried OT-nn.n` / `:: carried #nnnn` | `:: no record needed: <reason>` (SC3 only) | `:: in register OT-nn.n` / `#nnnn` (SC4))_

