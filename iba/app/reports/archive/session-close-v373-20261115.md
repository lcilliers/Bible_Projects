# Session close (#1875, rebuilt #2173)

> Generated 2026-11-15T06:13:12Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `58e035fd-4cd5-440d-ba63-65b2f1a988f5` (CLAUDE_CODE_SESSION_ID); started 2026-11-15T04:00:52Z; window base commit `97b686fed8eaedc9abd46ad1acbed1e520263ac4`
- compliance file: `Logs/compliance/COMPLIANCE-20261115-58e035fd.md`; session log: `--`
- **open findings: 37**; cleared by disposition: 0


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

<a id="summary"></a>
## Summary

37 open finding(s); SC2 6, SC3 5, SC4 3, SC8 1, SC10 22

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

- **OPEN** `SC3:7e9a6b90`: researcher message 2026-11-15T04:09 is in no escalation comment written this session: "in the previous session we focussed on defining layer 1 and layer 2, defining the rules, setting what is expected, writing the different routines and method to "
- **OPEN** `SC3:a4d4c20f`: researcher message 2026-11-15T04:31 is in no escalation comment written this session: "I read through the GAPs: G1 - comply with governance, which will answer the question if the this should be done.  I can imagine that this step will call for sof"
- **OPEN** `SC3:8ef6f926`: researcher message 2026-11-15T05:13 is too short to be matched; name where it is recorded: "Approve #2505"
- **OPEN** `SC3:f65a52ee`: researcher message 2026-11-15T05:15 is in no escalation comment written this session: "if I understand the base data is sound, there is no need to revisit it. is verse lexical sound,  must the verse lexical build process be revisited.  what is the"
- **OPEN** `SC3:af774d0d`: researcher message 2026-11-15T05:39 is in no escalation comment written this session: "why are you reading 1.5 mil rows"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:7e9a6b90`: researcher message 2026-11-15T04:09 holds, defers or asks to check something; name its register item: "in the previous session we focussed on defining layer 1 and layer 2, defining the rules, setting what is expected, writing the different routines and method to "
- **OPEN** `SC4b:f65a52ee`: researcher message 2026-11-15T05:15 holds, defers or asks to check something; name its register item: "if I understand the base data is sound, there is no need to revisit it. is verse lexical sound,  must the verse lexical build process be revisited.  what is the"
- **OPEN** `SC4b:7454d01f`: researcher message 2026-11-15T06:11 holds, defers or asks to check something; name its register item: "I am out of tokens, so will come back to this point a bit later.  I believe I have answered every relevant question. some questions I did not answer, because su"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

_no finding_

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (58e035fd-4cd5-440d-ba63-65b2f1a988f5); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/handlers/archive/conceptedit.py`: `iba/app/handlers/archive/conceptedit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/collectionbuild.py`: `iba/app/handlers/collectionbuild.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/handlers/conceptedit.py`: `iba/app/handlers/conceptedit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/archive/conceptedit.py`: `iba/app/lib/archive/conceptedit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/collectionevidence.py`: `iba/app/lib/collectionevidence.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/collectionevidencereport.py`: `iba/app/lib/collectionevidencereport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/collectionexport.py`: `iba/app/lib/collectionexport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/collectionindex.py`: `iba/app/lib/collectionindex.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/conceptedit.py`: `iba/app/lib/conceptedit.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/draftapply.py`: `iba/app/lib/draftapply.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/engagement.py`: `iba/app/lib/engagement.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/layerreading.py`: `iba/app/lib/layerreading.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/observationrecord.py`: `iba/app/lib/observationrecord.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/layers_2505_v1_20261115.py`: `iba/app/migration/archive/layers_2505_v1_20261115.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/layers_housekeeping_2505_v1_20261115.py`: `iba/app/migration/archive/layers_housekeeping_2505_v1_20261115.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/layers_rule_text_2505_v2_20261115.py`: `iba/app/migration/archive/layers_rule_text_2505_v2_20261115.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/record_answers_rule_2505_v3_20261115.py`: `iba/app/migration/archive/record_answers_rule_2505_v3_20261115.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/Collection-Build.ps1`: `iba/app/ps/Collection-Build.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/Concept-Edit.ps1`: `iba/app/ps/Concept-Edit.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/archive/Concept-Edit.ps1`: `iba/app/ps/archive/Concept-Edit.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2503_collection_index_test_run.py`: `iba/app/tools/temp_2503_collection_index_test_run.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2505_layers_test_run.py`: `iba/app/tools/temp_2505_layers_test_run.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

_no finding_
