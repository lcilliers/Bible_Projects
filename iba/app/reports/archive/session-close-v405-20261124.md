# Session close (#1875, rebuilt #2173)

> Generated 2026-11-24T05:28:58Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `75860879-bfa6-45ce-834d-0a11cbae93a6` (CLAUDE_CODE_SESSION_ID); started 2026-11-23T04:13:54Z; window base commit `217c02032f3f588aec546b853d3fe810967dc099`
- compliance file: `Logs/compliance/COMPLIANCE-20261123-75860879.md`; session log: `Logs/SESSION-LOG-20261123-wordnet-surface-network.md`
- **open findings: 15**; cleared by disposition: 7


## Contents

- [Summary](#summary)
- [SC1](#sc1-session-and-window)
- [SC2](#sc2-spine-fatal)
- [SC3](#sc3-researchers-words-recorded)
- [SC4](#sc4-open-items-in-the-register)
- [SC5](#sc5-analysis-integrity)
- [SC6](#sc6-rule-compliance)
- [SC8](#sc8-session-log)
- [SC9](#sc9-decisions-reached-their-targets)
- [SC10](#sc10-buildmd-coverage)
- [SC12](#sc12-publish)
- sc15
- sc16
- sc17

<a id="summary"></a>
## Summary

15 open finding(s); SC2 6, SC3 6, SC4 2, SC16 1

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

- **OPEN** `SC2:unverified:G0001G`: G0001G: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:G4528H`: G4528H: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:G6094`: G6094: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H0430H`: H0430H: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H1121A`: H1121A: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H5945H`: H5945H: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- cleared `SC3:eb0ac828`: researcher message 2026-11-23T05:12 is too short to be matched; name where it is recorded: "core" -- disposition: recorded in #2545 v4
- cleared `SC3:a9c3326e`: researcher message 2026-11-23T07:08 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar" -- disposition: no record needed: the app's continuation summary of the earlier conversation, not the researcher's words
- cleared `SC3:bb93895d`: researcher message 2026-11-23T10:11 is in no escalation comment written this session: "there are a number of words I can spot that is not pairing because they actually do not belong in the list, they should have been defined as another surface gro" -- disposition: recorded in #2545 v4
- **OPEN** `SC3:642dd16a`: researcher message 2026-11-23T12:10 is too short to be matched; name where it is recorded: "approve #2547"
- **OPEN** `SC3:980c6dcf`: researcher message 2026-11-23T12:44 is in no escalation comment written this session: "modify "C:\Bible_study_projects\_analytics\surfaces\exports\wordnet-collection-overlay-v1-20261123.xlsx" to include the surfaces of collection a and collection "
- **OPEN** `SC3:f3260b80`: researcher message 2026-11-23T12:54 is in no escalation comment written this session: "did you include the collection allocation of each surface as per the database on the sheet"
- **OPEN** `SC3:15a20135`: researcher message 2026-11-23T12:55 is in no escalation comment written this session: "is see now you did"
- **OPEN** `SC3:715af985`: researcher message 2026-11-23T13:50 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:51e3354d`: researcher message 2026-11-24T05:13 is in no escalation comment written this session: "the work we did yesterday to study the different associations of the surfaces using wordnet is valuable and need to be captured in the database so it can live a"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4a:ffe5c5da`: `Logs/SESSION-LOG-20261123-wordnet-surface-network.md` line 49: open item #2547 is completed: "- The WordNet data folder setting waits for the researcher: #2547."
- cleared `SC4b:c2477cf3`: researcher message 2026-11-23T04:21 holds, defers or asks to check something; name its register item: "Park #2538, #2541 #2542 #2543 for now" -- disposition: in register #2538
- cleared `SC4b:a9c3326e`: researcher message 2026-11-23T07:08 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar" -- disposition: not held: the app's continuation summary, not a message of the researcher
- cleared `SC4b:255ef038`: researcher message 2026-11-23T10:52 holds, defers or asks to check something; name its register item: "add a column in the excel to quantify/separate the items that will need manual intervention (e.g. reallocate surface to other; need decision, conflicitng sense," -- disposition: not held: the overlay and the manual-intervention column were done in this session (iba/app/BUILD.md entry 557)
- **OPEN** `SC4b:715af985`: researcher message 2026-11-23T13:50 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

_no finding_

<a id="sc8-session-log"></a>
## SC8 Session log

_no finding_

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

_no finding_

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

- cleared `SC16:Escalation.ps1_-Action_Raise`: Escalation.ps1 -Action Raise failed 3 times this session: error: short_description is 61 chars, over the 60-char title limit. It must read like a title/subject naming the topic - -- disposition: fixed: the titles were shortened to 60 characters and the Raise then succeeded (#2544 and #2545)
- **OPEN** `SC16:Escalation.ps1_-Action_Update`: Escalation.ps1 -Action Update failed 3 times this session: [31;1m.\iba\app\ps\Escalation.ps1: [31;1mThe term '.\iba\app\ps\Escalation.ps1' is not recognized as a name of a cmdle; error: decision_required items may only move to approved from a CURRENT next_action of ready_for_approval -- no shortcut; error: next_action='approved' requires resolution to be filled in (plan v3 sec3)

_no finding_
