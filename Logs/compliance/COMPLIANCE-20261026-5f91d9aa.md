# Session compliance -- 20261026 -- session 5f91d9aa-a797-4494-9f64-f2137d5a6103

Mode: standard

> Escalation #2173 P2. Written by Claude at session start, checked by `Compliance.ps1 -Action Check -Phase Start`; evidence added during the session and checked at close (`Session-Close.ps1`, SC6). One row per rule: what it requires of me in THIS session, in my own words, or `not engaged` with the reason. Never copy the rule text. The `|` character may not be used inside a cell.

## Acknowledgement

I have read the governance settings, behaviour rules and escalation rules, and will comply with them.

## Rules

| id | status | requires / reason | evidence |
|---|---|---|---|
| G:governance.escalation.scope | engaged | The #2305 work and every question or ruling on it is kept on its escalation row through Escalation.ps1, not left in chat. | #2305 v10 |
| G:governance.past_precedent_investigation_signals_missing_config | engaged | Where working out how something was done needs old outputs, the gap is named for config; here the capture's stage, tag and write grant are named as config to build, not improvised. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| G:governance.primary_responsibility | engaged | The capture is to run inside the app (its tools, config and write grant), so the design puts Prepare and Record in the app rather than loose scripts. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| G:governance.programme_stages | engaged | The migration records prior analysis into the tables; it does not advance the analysis itself, and the design says so. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| G:governance.project_change_rule | engaged | The new stage, tag and writer are to go in through the app's config in a Developer Mode build, not by editing the tables directly. | #2305 v5 |
| G:governance.project_operations | engaged | Building the document index from the reading index tables is a project operation, done read-only through the app's own library. | iba/app/tools/temp_2305_document_index.py |
| G:governance.rules_must_be_config_driven | engaged | The capture design rests on the cfg rows that govern observations (RO11, RW-02 to RW-10, B:69 to B:122), read fresh from the database. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| G:governance.scope_iba_app | engaged | The temp index builder imports the app's readingindex library and reads its settings, so the index uses the app's own definition of the document set. | iba/app/tools/temp_2305_document_index.py |
| G:governance.scope_project | engaged | The capture is judged against the whole study's record (the October imports, #2266, the reading process), not only the files. | #2305 v4 |
| G:governance.study_status | engaged | The study is active; the capture is a migration outside the standard analytic process and nothing in the reading process is changed. | #2305 v2 |
| B:1 | engaged | Every count I gave (235 documents, 662 imports, 19,034 lines) came from a fresh query, and the stale 717 was replaced by a live count. | outputs/escalation/2305-prior-work-document-index-v1-20261026.json |
| B:2 | engaged | I checked the index JSON against the tables (file list, import counts) before calling it done. | outputs/escalation/2305-prior-work-document-index-v1-20261026.json |
| B:4 | engaged | The API cost estimate is labelled inferential where it is recorded. | #2305 v6 |
| B:10 | not engaged | No task touched the API key; the API question was answered without any call. |  |
| B:16 | engaged | Decisions went into an md design with options; clarifications were asked in plain chat. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| B:17 | engaged | The capture was restated and designed, and the design approved, before any build. | #2305 v5 |
| B:18 | engaged | The design went into an md file first, with a short chat summary and its path. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| B:19 | engaged | Where the agreed structure was unclear I read the design and config rather than guess, and left open points as decisions. | #2305 v4 |
| B:20 | engaged | I flagged the cheaper route on the API question: measure on the pilot before deciding. | #2305 v6 |
| B:21 | engaged | Each open point raised in chat went onto #2305 in the same reply. | #2305 v9 |
| B:22 | engaged | After approval I carried the work forward without asking again at each step. | #2305 v5 |
| B:23 | not engaged | No fix task this session; the work was an index and a design. |  |
| B:24 | engaged | Results reported with their queries and counts, structural checks kept apart from fitness. | outputs/escalation/2305-prior-work-document-index-v1-20261026.json |
| B:25 | engaged | Inspection ran read-only; writes stayed inside the approved #2305 task (escalation updates, the index, the design). | #2305 v3 |
| B:27 | engaged | PowerShell multi-line arguments were passed as single-quoted strings. | #2305 v9 |
| B:28 | not engaged | The researcher pasted no error this session. |  |
| B:31 | engaged | Each ruling (Q1 to Q7, chat on Sonnet, no duplicate check) was written onto #2305 and into the design in this session. | #2305 v8 |
| B:34 | engaged | Statements about past work cite their file or escalation (the October import, #2266, the #2228 index). | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| B:36 | engaged | I used no uncounted most or best; counts are given as counts. | outputs/escalation/2305-prior-work-capture-design-v2-20261026.md |
| B:40 | engaged | The findings of building the index (stale import counts, the gone and new files) were recorded on #2305, not fixed silently. | #2305 v2 |
| B:44 | engaged | The new choices the capture needs were routed to the researcher as Q1 to Q7 rather than decided by me. | #2305 v4 |
| B:83 | engaged | All work stayed in C:\Bible_study_projects. | outputs/escalation/2305-prior-work-document-index-v1-20261026.json |
| B:98 | engaged | The temp script follows the #2304 temp_ convention in iba/app/tools. | iba/app/tools/temp_2305_document_index.py |
| B:99 | engaged | Each instruction was read against the whole conversation, for example the duplicates ruling against the earlier splitting ruling. | #2305 v8 |
| B:100 | engaged | Codes shown carry their names (cluster codes with names in the index). | outputs/escalation/2305-prior-work-document-index-v1-20261026.json |
| B:101 | engaged | Commands the researcher may run were given as full commands. | #2305 v5 |
| B:102 | engaged | Reports carried verified facts only, with their limits and open items named by id. | #2305 v4 |
| B:105 | engaged | The capture fix was designed and decided before anything is built; the build waits for Developer Mode. | #2305 v5 |
| B:114 | not engaged | No study phase was run; the capture is a migration and only designed this session. |  |
| B:116 | not engaged | No verse was read for study work this session. |  |
| E:4 | engaged | The researcher named #2305 as the task; the other Claude-assigned items were acknowledged at each stop with why each is untouched. | #2305 v2 |
| E:5 | engaged | Every step and remark, the researcher's verbatim, was captured on #2305 in the same turn. | #2305 v10 |

## Conflicts and rules not followed

- B:81: the compliance file was not written at session start, since start-project was not run; it is written at close, from the session's record.
- RO11 and RW-03 (no second observation for the same finding): the #2305 capture departs from them across documents, by the researcher's ruling recorded on #2305 v8; within a document they still apply.

## Close dispositions

- SC6:file :: fixed
