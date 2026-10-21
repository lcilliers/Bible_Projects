# Session log — 2026-10-20 — Build of the rebuilt start-project and session-close (#2173, #2174)

Session `d7696d1d-b5aa-4ccf-a85e-a48878417161`, Developer Mode (started 2026-10-20T14:51Z).

## 1. Scope

2026-10-20. Built every part of the two #2173 proposals (start-project P0-P5 and S1-S6;
session-close SC1-SC14; contradictions G1-G14) as app code and config, decided and applied #2174,
tested on a copy of iba.db, then ran the rebuilt start and close on this session as the
acceptance test. Continued 2026-10-21: cost estimate of the two routines; the researcher did not
approve the build but kept it, and named the cause as a process that re-reads documents instead
of recording in iba.db. Researcher, verbatim: *"This is your domain, I am expecting you to do a
professional, complete, with proper controls, self audit job of preparing the code and updating
the tables and documentation."* The study stays on hold; no reading or narrative change.

## 2. Escalations

- **#2173** (task): v12 researcher's instruction recorded verbatim; v13 build recorded; v14
  ready_for_approval, assigned Researcher, with the resolution; v15-v16 acceptance faults; v17 cost
  question and estimate; v18 researcher's objection to self-checking; v19 not approved; v20 build
  kept, sequence fault acknowledged, decision 2 (diagnosis only) open with the researcher.
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
Cost estimate: `outputs/markdown/2173-session-routine-cost-estimate-v1-20261021.md`.
Records: `Logs/compliance/COMPLIANCE-20261020-d7696d1d.md`,
`outputs/markdown/2173-narrative-quote-check-all-chapters-v1-20261020.md`, and the reports the new
steps wrote (`outputs/escalation/escalation-context-v1-20261020.md`,
`outputs/escalation/escalation-thread-audit-v1-20261020.md`, the list, spine and close reports).

## 4. Decisions

Researcher's decisions:
- Do the whole of #2173 in this session and include #2174; Claude owns rule coherence (#2173 v12).
- The build is not approved (#2173 v19) but is kept in place, no revert (#2173 v20).

Claude's, within the approved design (none needed a new researcher decision):
- #2174: escalation rule 6 retired; rules 7 and 12 restated (`iba/app/migration/session_routines_2173_v1_20261020.py`, recorded in #2174 v3).
- "Open" is raised, in-progress, re-assigned; on-hold is parked (`cfg_enum`, migration; `iba/app/lib/escalation.py`).
- Rules naming retired things or the disabled gate restated or retired: behaviour 43, 47, 54, 62, 74; escalation 3, 12, 17; governance verse_gap_by_design, no_direct_github_publish (migration; `iba/app/GOVERNANCE.md`).
- New settings filed under the existing modules behaviour and validation, so no new `config_module` value (`iba/app/migration/session_routines_2173_v1_20261020.py`).
- SC12 also exports the threads register when the file differs from the table, because it embeds rule 74 (`iba/app/handlers/session_close.py`).
- Acceptance faults fixed at the root: `compliance.copy_min_words`, the commit-in-file-name fix, `session_close.message_min_words`, wrapped bullets read whole, generated reports excluded from SC4a (`iba/app/lib/compliance.py`, `iba/app/handlers/session_close.py`, recorded in #2173 v14 and v15).
- The test runner stays live as the plan's executable form; the one-off worksheet sync is archived (`iba/app/tools/archive/temp_2173_ps_worksheet_sync.py`).

## 5. Open items

- #2173: not approved, build kept; the researcher decides whether Claude writes a diagnosis (no
  build) of where working state lives in documents instead of iba.db (#2173 v20).
- #2174: rule 6 retired as part of the kept build; for the researcher (#2174).
- #2175 and #2176: on hold until the study re-opens (researcher).
- Not done in the build (named in BUILD.md section 353): a mechanical evidence check per
  context-delivered rule; it stays part of #2173's record for the researcher's direction.

## 6. Git

_Second close, 2026-10-21:_ branch `main`, commit pushed (output of `git push`, `git log -1`,
`git status -sb`; `Session-Close.ps1` 0 open findings, `iba/app/reports/session-close-v145-20261021.md`):

```
To https://github.com/lcilliers/Bible_Projects.git
   4e814058..25d1e67a  main -> main
25d1e67a19d57b92e1cd108d786665341e3d9048 2026-10-21 04:35:27 +0100 session 20261021: #2173 cost estimate; build not approved, kept
## main...origin/main
```

_First close, 2026-10-20 (kept as written):_

Branch `main`. Session commit, pushed (output of `git push`, `git log -1` and `git status -sb`):

```
To https://github.com/lcilliers/Bible_Projects.git
   7d3e33ac..b9c01f6a  main -> main
b9c01f6a593a1a105ae1498a4219daade5f09b47 2026-10-20 16:58:49 +0100 session 20261020 (2): #2173 build - start-project and session-close rebuilt; #2174 decided
## main...origin/main
```

Before the commit, `Session-Close.ps1` reported 0 open findings
(`iba/app/reports/session-close-v143-20261020.md`). This section is committed alone as "session
log git confirmation" (`session_close.final_commit_marker`); the next start checks for it.
