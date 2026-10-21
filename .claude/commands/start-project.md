---
description: Session-startup procedure — git and last-close check, IBA bootstrap, rule compliance file, open escalations and their files, thread audit, status report
---

# Start Project — Session Startup

Run every step,
in order, every time. Do not infer a task from the results and start it: this command ends with
the findings and a question.

**P0 (researcher, verbatim): *"stop printing reports that have no meaning. If I want to inspect
the report, I request it on demand."*** A check that passes is not reported. Report only what is
wrong or needs action, by name, with its reason. Never report a bare count or "N checks passed".
The escalation list, the threads list, the spine check and the config report are on demand only
(`Escalation.ps1 -Action List` / `-Action Thread`, `iba/app/ps/Spine-Check.ps1`, `iba/app/ps/Config-Maintenance.ps1`).

## 1. STEP

Check port 8989; if nothing listens, start STEP and wait (it only launches STEP; step 2 proves it
answers):

```powershell
if (-not (Get-NetTCPConnection -LocalPort 8989 -State Listen -ErrorAction SilentlyContinue)) {
    Start-Process "C:\Program Files (x86)\STEP\step.exe"
    $deadline = (Get-Date).AddSeconds(90)
    do { Start-Sleep -Seconds 5; $up = Get-NetTCPConnection -LocalPort 8989 -State Listen -ErrorAction SilentlyContinue } while (-not $up -and (Get-Date) -lt $deadline)
}
```

No report line unless it did not come up.

## 2. Bootstrap, last session, rules: `iba\app\ps\Start-Iba.ps1`

`python -m iba.app.init` (`iba/app/init.py`). It prints only problems, under **NEEDS ACTION**:
config reloaded, tables created, a database path that does not exist, STEP not answering the
known-answer probe, and **how the last session ended** (`lib/sessionwindow.last_close_findings`,
S6): uncommitted paths, an uncommitted session log, a newest commit that is not a session-close's
final commit (`session_close.final_commit_marker`) with the commits since the last close, and a
newest session log that names no existing commit in its git section. Then it prints **every**
active governance setting (`G:`), behaviour rule (`B:`) and escalation rule (`E:`) in full, from
the database. Read them: step 3 restates each one.

Report each NEEDS ACTION line first. NOT READY stops the start. If the last session did not end
with a completed close, say so and name the commits; read that session's log only then.

## 3. Rule compliance file (P2): `iba\app\ps\Compliance.ps1`

```powershell
.\iba\app\ps\Compliance.ps1 -Action Template
```

It writes `Logs/compliance/COMPLIANCE-<date>-<session8>.md` with one row per active rule. Fill it
(`cfg_behaviour_rule` session-compliance-restated-and-proved):

- **Acknowledgement:** the exact sentence in `compliance.acknowledgement`.
- **Rules:** per row, status `engaged` or `not engaged`, and in your own words what the rule
  requires of you **in this session** (the work in hand), or why it is not engaged. Never copy the
  rule text: a copy is a finding. No `|` inside a cell. Leave `evidence` empty for now.
- **Conflicts and rules not followed:** one `- <id>: ...` line per rule that conflicts with
  another rule, a document or memory that restates it (name both sides; control map, `cfg_control_home`), or that is not or cannot be
  followed (why). Every rule the check lists as naming a retired thing must be here.

Then:

```powershell
.\iba\app\ps\Compliance.ps1 -Action Check -Phase Start
```

It exits 3 until the file passes. **The start does not end until it passes.** During the session,
add each engaged rule's evidence (a file path, `#nnnn vN`, a commit hash, a command's output) as
you produce it; session-close checks it (SC6). The researcher may spot-check any row against its
rule: a wrong, vague or copied restatement means the rule was not understood, and the session
stops there until it is re-read.

## 4. Open escalations and what they point to (P1)

```powershell
.\iba\app\ps\Escalation.ps1 -Action Context
```

It writes `escalation.context_report_path` (versioned): for every **open** escalation (raised,
in-progress, re-assigned; `cfg_enum escalation_state_open`; on-hold is parked and is read when
taken up), every file named in any field of any version, resolved to its **latest live version**.
Findings: `missing` (no live version; the escalation points at nothing) and `bare` (a bare
filename, escalation rule 7).

Then **read the resolved latest file(s) of each open escalation** with its question in mind, and
say per escalation what they show for its next action: what is decided, what is still open, and
whether a newer file supersedes what the escalation describes. Name the `missing`/`bare`
findings. Items assigned to Claude come first (escalation rule 4).

## 5. Threads (P5)

```powershell
.\iba\app\ps\Escalation.ps1 -Action ThreadCheck -AnsweredBy Claude
.\iba\app\ps\Escalation.ps1 -Action ThreadAudit
```

ThreadCheck (rule T5) is reported only if it moved a thread or closed an item, naming each move.
ThreadAudit writes `escalation.thread_audit_report_path`: findings by thread item, T-a (handle
does not resolve), T-b (no note), T-c (referred escalation closed, item open), T-d (open on a
worked strand, `escalation.worked_strand_escalations`), T-e (verse already told), T-f (thread
shape), T-g (register file out of date). Report the findings by check with their items (the
report path for the full list); a check with none is not mentioned.

Only when a strand is in progress (none while `governance.study_status` says the study is on hold): run
`Escalation.ps1 -Action Match -Cluster .. -Strong .. -Verse ..` for it and name the threads that
bear on it. Name the threads waiting on the researcher only when their answer blocks the work in
hand.

## 6. Report and stop

In chat, in this order, findings only:

1. Everything wrong or needing action (FATAL first): NEEDS ACTION lines; the last-session check.
2. The open escalations, each with what its files show for its next action; the Context findings.
3. The compliance file: passed, and the rules named in its conflicts section.
4. The thread findings.

Then ask what to work on. Do not start a task on your own initiative.
