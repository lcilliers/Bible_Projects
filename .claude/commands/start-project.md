---
description: Session-startup procedure — git check, IBA app bootstrap, orientation, status report
---

# Start Project — Session Startup

Run this procedure in full, in order, every time it's invoked — even if a prior session in this
conversation seems recent. Do not skip steps. Do not infer a task from the results and start
executing it — this command ends in a status report and a question, not in work.

## 1. Git state check

Run `git status` and `git log -1 --format="%H %ci"`.

- If the working tree isn't clean, say what's changed — don't commit anything unasked.
- If there's an uncommitted `SESSION-LOG-*.md` (anywhere, including `iba/app/`), flag it
  immediately: per CLAUDE.md §12, completing a session log means the full commit-and-push cycle
  happens in the same unit of work, and an uncommitted one left over from a prior session is a
  known recurring gap (see `feedback_commit_incrementally`), not something to carry forward
  silently.

## 2. Start STEP if it isn't already up

STEP (the local STEP Bible server, `http://localhost:8989`) is a standalone desktop app, not part
of this repo: `C:\Program Files (x86)\STEP\step.exe`. Check first, don't blindly relaunch:

```powershell
Get-NetTCPConnection -LocalPort 8989 -State Listen -ErrorAction SilentlyContinue
```

If nothing is listening, start it and wait for it to come up before moving on:

```powershell
Start-Process "C:\Program Files (x86)\STEP\step.exe"
$deadline = (Get-Date).AddSeconds(90)
do {
    Start-Sleep -Seconds 5
    $up = Get-NetTCPConnection -LocalPort 8989 -State Listen -ErrorAction SilentlyContinue
} while (-not $up -and (Get-Date) -lt $deadline)
```

It's a GUI app under the researcher's own local install — launching it is expected to pop its
window; that's normal, not a fault. If it still isn't listening after the 90s poll window, stop
polling and say so plainly in the step-5 report — don't loop indefinitely and don't claim READY
without the port actually confirmed open.

## 3. Bootstrap the IBA app

Run `iba/app/ps/Start-Iba.ps1` via the PowerShell tool (not Bash — it's a `.ps1`).

Per CLAUDE.md, this is mandatory on opening the project, before any IBA work — run it regardless
of whether this session turns out to touch IBA. It validates/loads config into `iba.db`, builds
data tables if missing, pre-flights the local STEP server (a second, authoritative check beyond
the port probe in step 2 — it confirms STEP is not just up but answering with the tagged module),
and prints pointers to `iba/app/BUILD.md` (what's built) and `iba/app/GOVERNANCE.md` (how config
governs the code).

Report plainly whether it reached READY. If STEP still isn't reachable, a dependency is missing,
or the script errors, say so as-is — do not proceed as though it passed.

## 4. Orient on open threads

Read from the live system, not from memory — per `feedback_iba_session_start_read_live_docs_not_memory`.
The escalation table is the project's single authoritative open-item/task system
(`governance.escalation.scope`, project-wide, not IBA-only — `docs/governance-alignment-register.md`
was retired 2026-08-18 in favour of it):

- Run `iba/app/ps/Escalation.ps1 -Action List` and read the report it writes
  (`iba/app/reports/escalation-list.md` by default) — note anything `raised`/`in-progress`/
  `on-hold`/`re-assign` that's relevant to this session, especially rows `next_action_assigned_to`
  Claude.
- The most recent file(s) under `outputs/markdown/` and `outputs/session-logs/` if an open
  escalation or the last commit message points to an in-progress thread worth naming.

## 5. Report and stop

Summarise, briefly, in chat (not a new `.md` file — this is a status check, not a deliverable):

- Git state (clean/dirty; anything uncommitted flagged).
- STEP (was it already up, or did this command start it — and did it come up in time).
- IBA bootstrap result (READY or what went wrong).
- Open escalations relevant to this session, and any other loose end found.

Then stop and ask what to work on this session. Do not start a task on your own initiative.
