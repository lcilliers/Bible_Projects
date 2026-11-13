# Session close (#1875, rebuilt #2173)

> Generated 2026-11-13T14:55:25Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `92d853ef-815a-4baa-9714-7fb3744fb09d` (CLAUDE_CODE_SESSION_ID); started 2026-11-13T12:30:15Z; window base commit `d2526343f49e80f8908523e27fc8f288940f2205`
- compliance file: `Logs/compliance/COMPLIANCE-20261113-92d853ef.md`; session log: `--`
- **open findings: 4**; cleared by disposition: 4


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

4 open finding(s); SC8 1, SC15 3

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

_no finding_

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- cleared `SC3:9650c0c0`: researcher message 2026-11-13T12:30 is in no escalation comment written this session: "Task (from the session that started this one):
Background (from the session that started this one):
The researcher is a sole Bible-study researcher; the IBA app" -- disposition: no record needed: the task brief of the session that started this one, recorded as #2498 v1
- cleared `SC3:839f07b8`: researcher message 2026-11-13T13:49 is too short to be matched; name where it is recorded: "Run it live" -- disposition: recorded in #2498 v8 ('Run it live', answering the live-run decision)
- cleared `SC3:6b560b3f`: researcher message 2026-11-13T13:57 is too short to be matched; name where it is recorded: "Apply live" -- disposition: recorded in #2498 v10 ('Apply live', answering the fear-roles decision)

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- cleared `SC4b:9650c0c0`: researcher message 2026-11-13T12:30 holds, defers or asks to check something; name its register item: "Task (from the session that started this one):
Background (from the session that started this one):
The researcher is a sole Bible-study researcher; the IBA app" -- disposition: not held: the task brief, carried as #2498

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

_no finding_

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (92d853ef-815a-4baa-9714-7fb3744fb09d); write it (governance.session_log_required_content)

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

- **OPEN** `SC15:iba/app/USER-GUIDE.md:439:Draft-Apply.ps1`: `iba/app/USER-GUIDE.md` line 439 names `Draft-Apply.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:439:Node-Check.ps1`: `iba/app/USER-GUIDE.md` line 439 names `Node-Check.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:467:outputs/escalation/2498-prior-reread-by-collection-design-v3-20261113.md`: `iba/app/USER-GUIDE.md` line 467 names `outputs/escalation/2498-prior-reread-by-collection-design-v3-20261113.md`, which does not resolve

_no finding_
