---
name: project_iba_configmaint_escalation_self_answered_anomaly
description: "UNEXPLAINED (2026-07-29) — two configmaint.propose escalations were found state='answered', answer='approve' within ~44s of being raised, before either was genuinely answered via Escalation.ps1 AnswerRun. No self-approve code path or scheduled task found. Needs a dedicated investigation session — do not assume future configmaint.propose escalations are safe to trust at face value without checking answered_at/raised_at timing."
metadata:
  type: project
  originSessionId: bbe449d9-8c2c-4613-9770-f9e081626e61
  modified: 2026-07-29T06:35:07.521Z
---

Surfaced 2026-07-29 during the verse-gap config work (see
[[project_iba_verse_existence_gated_on_term_discovery]]). Two `configmaint.propose` insert
proposals were raised back-to-back (escalation ids 332, 333 in `iba/app/db/iba.db`). When it came
time to approve them, one `Escalation.ps1 -Action AnswerRun -Decision Approve` attempt returned
"no pending escalation for run" — and a direct DB query showed **both** rows already
`state='answered', answer='approve'`, `answered_at` ~44-45 seconds after their `raised_at`. The
second escalation was never even attempted via AnswerRun before this was noticed.

**Ruled out:**
- A self-approve code path — grepped `iba/app` for `self_approve`/`auto_approve`; the only hits
  are a docstring saying the app *cannot* self-approve a word registration, and unrelated
  docstring text.
- A scheduled task — `Get-ScheduledTask` found a task named `ReconcileConfigs`, but it's a stock
  Windows COM-handler task ("Task periodically reconciling feature configurations", ClassId
  `{15F5ECE1-4550-4A92-8E26-984FD1DA54FA}`) unrelated to this project — not a script, doesn't
  touch `iba.db`.
- `run.py`'s pause-continue path was re-read; no auto-answer logic there either.

**Not ruled out / not investigated:** whether this is a race condition in how the PowerShell tool
or its retry behavior interacts with `python -m iba.app.lib.escalation answer-run` (e.g. a command
silently executing twice, once successfully and once against already-answered state — but this
doesn't explain the SECOND escalation being answered when it was never targeted at all); whether
some other process on this machine has read/write access to `iba.db` and a matching cfg_setting
key list; whether this is specific to `configmaint.propose` escalations vs. every escalation type.

**Why this matters:** the whole IBA config-change model rests on `configmaint.propose` being
approval-gated — [[feedback_iba_config_changes_require_researcher_approval_never_silent]]. If
something in the environment is capable of auto-answering escalations, that gate is not real, even
though in this specific case the content happened to match what the researcher had already
approved in plain chat. A future session should: check whether this reproduces on a fresh
non-content-matching proposal (one the researcher has NOT already verbally approved, to rule out
any "look for a chat approval and auto-apply" pattern rather than a pure race); check the SQLite
`escalation` table's write history more forensically (WAL file, `cfg_change_detail`) around the
exact timestamps; consider whether the PowerShell tool session had any other concurrent process.
Until explained, treat any `configmaint.propose` escalation's apparent "answered" state with
suspicion if you did not personally issue the `AnswerRun` call that produced it — check
`raised_at`/`answered_at` for an implausibly short gap before trusting it.
