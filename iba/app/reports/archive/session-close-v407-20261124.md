# Session close (#1875, rebuilt #2173)

> Generated 2026-11-24T07:47:06Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `4e495962-a220-410b-b915-3cc04c7961e3` (CLAUDE_CODE_SESSION_ID); started 2026-11-24T05:28:20Z; window base commit `205249e3f95938b4c836c56efef4f9ad261df48a`
- compliance file: `Logs/compliance/COMPLIANCE-20261124-4e495962.md`; session log: `--`
- **open findings: 48**; cleared by disposition: 0


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

48 open finding(s); SC3 2, SC4 1, SC6 37, SC8 1, SC10 4, SC17 3

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:5eb5f227`: researcher message 2026-11-24T07:46 is too short to be matched; name where it is recorded: "Approve, then commit"
- **OPEN** `SC3:d2b57727`: researcher message 2026-11-24T06:57 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:d2b57727`: researcher message 2026-11-24T06:57 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
- **OPEN** `SC6:G:governance.primary_responsibility`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
- **OPEN** `SC6:B:1`: engaged, with no evidence
- **OPEN** `SC6:B:2`: engaged, with no evidence
- **OPEN** `SC6:B:4`: engaged, with no evidence
- **OPEN** `SC6:B:16`: engaged, with no evidence
- **OPEN** `SC6:B:17`: engaged, with no evidence
- **OPEN** `SC6:B:18`: engaged, with no evidence
- **OPEN** `SC6:B:19`: engaged, with no evidence
- **OPEN** `SC6:B:20`: engaged, with no evidence
- **OPEN** `SC6:B:21`: engaged, with no evidence
- **OPEN** `SC6:B:22`: engaged, with no evidence
- **OPEN** `SC6:B:23`: engaged, with no evidence
- **OPEN** `SC6:B:24`: engaged, with no evidence
- **OPEN** `SC6:B:25`: engaged, with no evidence
- **OPEN** `SC6:B:27`: engaged, with no evidence
- **OPEN** `SC6:B:28`: engaged, with no evidence
- **OPEN** `SC6:B:31`: engaged, with no evidence
- **OPEN** `SC6:B:34`: engaged, with no evidence
- **OPEN** `SC6:B:36`: engaged, with no evidence
- **OPEN** `SC6:B:40`: engaged, with no evidence
- **OPEN** `SC6:B:44`: engaged, with no evidence
- **OPEN** `SC6:B:83`: engaged, with no evidence
- **OPEN** `SC6:B:97`: engaged, with no evidence
- **OPEN** `SC6:B:98`: engaged, with no evidence
- **OPEN** `SC6:B:99`: engaged, with no evidence
- **OPEN** `SC6:B:100`: engaged, with no evidence
- **OPEN** `SC6:B:101`: engaged, with no evidence
- **OPEN** `SC6:B:102`: engaged, with no evidence
- **OPEN** `SC6:B:105`: engaged, with no evidence
- **OPEN** `SC6:B:123`: engaged, with no evidence
- **OPEN** `SC6:B:125`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (4e495962-a220-410b-b915-3cc04c7961e3); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/tools/archive/temp_2545_nopair_review.py`: `iba/app/tools/archive/temp_2545_nopair_review.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/temp_2545_wordnet_surface_pairs.py`: `iba/app/tools/archive/temp_2545_wordnet_surface_pairs.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2545_nopair_review.py`: `iba/app/tools/temp_2545_nopair_review.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/temp_2545_wordnet_surface_pairs.py`: `iba/app/tools/temp_2545_wordnet_surface_pairs.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

_no finding_

_no finding_

- **OPEN** `SC17:table_added`: a table added to cfg_table, and `iba/docs/project-map.md` did not change: cfg_table insert {"database": "iba", "name": "surface_relation", "grain": "one row per unordered ; cfg_table insert {"database": "iba", "name": "surface_network_group", "grain": "one row per surfa
- **OPEN** `SC17:mechanism_task_completed`: a task completed that BUILD.md names as built this session, and `iba/docs/project-map.md` did not change: #2548 Surface relations: WordNet network held in iba.db
- **OPEN** `SC17:programme_book_section`: a Programme book section the map rests on was changed, and `iba/docs/project-map.md` did not change: Programme book section 'Surfaces, collections and the registry'
