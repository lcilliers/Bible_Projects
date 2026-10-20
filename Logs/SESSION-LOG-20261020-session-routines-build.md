# Session log — 2026-10-20 — Build of the rebuilt start-project and session-close (#2173, #2174)

Session `d7696d1d-b5aa-4ccf-a85e-a48878417161`, Developer Mode (started 2026-10-20T14:51Z).

## 1. Scope

2026-10-20. Built every part of the two #2173 proposals (start-project P0-P5 and S1-S6;
session-close SC1-SC14; contradictions G1-G14) as app code and config, decided and applied #2174,
tested on a copy of iba.db, then ran the rebuilt start and close on this session as the
acceptance test. Researcher, verbatim: *"This is your domain, I am expecting you to do a
professional, complete, with proper controls, self audit job of preparing the code and updating
the tables and documentation."* The study stays on hold; no reading or narrative change.

## 2. Escalations

- **#2173** (task): v12 researcher's instruction recorded verbatim; v13 build recorded; v14
  ready_for_approval, assigned Researcher, with the resolution.
- **#2174** (issue): v2 in-progress (taken into #2173 on the researcher's instruction); v3
  ready_for_approval, assigned Researcher: escalation rule 6 retired, with the evidence.
- **#2175** (issue, raised, on hold): 15 of 5,571 quoted parts in the current chapters not found in
  the ESV text (found by the quote check moved into the app).
- **#2176** (issue, raised, on hold): 187 thread audit findings (T-b 141, T-e 30, T-d 11, T-c 4,
  T-g 1).

## 3. Files

Code: `iba/app/lib/escalation.py`, `iba/app/lib/escalationcontext.py` (new),
`iba/app/lib/threadaudit.py` (new), `iba/app/lib/compliance.py` (new),
`iba/app/lib/sessionwindow.py` (new), `iba/app/lib/quotecheck.py` (new), `iba/app/init.py`,
`iba/app/handlers/spine.py`, `iba/app/handlers/session_close.py`, `iba/app/handlers/reports.py`,
`iba/app/handlers/narrativeregister.py`, `iba/app/handlers/compliance.py` (new),
`iba/app/ps/Compliance.ps1` (new), `iba/app/ps/Escalation.ps1`, `iba/app/ps/Narrative-Register.ps1`,
`iba/app/ps/Session-Close.ps1`, `.claude/hooks/stop_check_escalation_backlog.py`,
`.claude/commands/start-project.md`, `.claude/commands/session-close.md`.
Config: `iba/app/migration/session_routines_2173_v1_20261020.py` (101 audited rows, run
`DEVMODE-2173-SESSION-ROUTINES-20261020`); DB backup
`iba/app/db/iba.db.pre-2173-session-routines-20261020.bak` (not in git).
Tests and tools: `iba/docs/2173-session-routines-test-plan-v1-20261020.md`,
`iba/app/tools/temp_2173_test_plan_run.py`, `iba/app/tools/archive/temp_2173_ps_worksheet_sync.py`,
`iba/docs/ps tools worksheet.xlsx`.
Docs: `iba/app/BUILD.md` (section 353), `iba/app/GOVERNANCE.md` (section 96; section 82 marked
superseded in part; the narrative copy timing), `iba/app/USER-GUIDE.md`, `CLAUDE.md` (section 12).
Records: `Logs/compliance/COMPLIANCE-20261020-d7696d1d.md`,
`outputs/markdown/2173-narrative-quote-check-all-chapters-v1-20261020.md`, and the reports the new
steps wrote (`outputs/escalation/escalation-context-v1-20261020.md`,
`outputs/escalation/escalation-thread-audit-v1-20261020.md`, the list, spine and close reports).

## 4. Decisions

Researcher's decisions:
- Do the whole of #2173 in this session and include #2174; Claude owns rule coherence (#2173 v12).

Claude's, within the approved design (none needed a new researcher decision):
- #2174: escalation rule 6 retired; rules 7 and 12 restated (`iba/app/migration/session_routines_2173_v1_20261020.py`, recorded in #2174 v3).
- "Open" is raised, in-progress, re-assigned; on-hold is parked (`cfg_enum`, migration; `iba/app/lib/escalation.py`).
- Rules naming retired things or the disabled gate restated or retired: behaviour 43, 47, 54, 62, 74; escalation 3, 12, 17; governance verse_gap_by_design, no_direct_github_publish (migration; `iba/app/GOVERNANCE.md`).
- New settings filed under the existing modules behaviour and validation, so no new `config_module` value (`iba/app/migration/session_routines_2173_v1_20261020.py`).
- SC12 also exports the threads register when the file differs from the table, because it embeds rule 74 (`iba/app/handlers/session_close.py`).
- Acceptance faults fixed at the root: `compliance.copy_min_words`, the commit-in-file-name fix, `session_close.message_min_words`, wrapped bullets read whole, generated reports excluded from SC4a (`iba/app/lib/compliance.py`, `iba/app/handlers/session_close.py`, recorded in #2173 v14 and v15).
- The test runner stays live as the plan's executable form; the one-off worksheet sync is archived (`iba/app/tools/archive/temp_2173_ps_worksheet_sync.py`).

## 5. Open items

- #2173 and #2174: for the researcher's approval.
- #2175 and #2176: on hold until the study re-opens (researcher).
- Not done in the build (named in BUILD.md section 353): a mechanical evidence check per
  context-delivered rule; it stays part of #2173's record for the researcher's direction.

## 6. Git

Written after the session commit.
