# Escalation deep history

## #2240 — escalation.history crashed: no escalation #729
type=run_error source=escalation

**v1** (2026-10-23T12:46:24Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** escalation.history crashed: no escalation #729
> **comment (set this version):** uncaught exception — not a routed fail()/escalate() Outcome
> **context (set this version):** {"traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\run.py\", line 152, in run_step\n    outcome: Outcome = handler(ctx)\n                       ~~~~~~~^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\handlers\\reports.py\", line 585, in escalation_history\n    out = esc.write_history_report(ctx.cfg, ctx.db, int(eid), path)\n  File \"C:\\Bible_study_projects\\iba\\app\\lib\\escalation.py\", line 1528, in write_history_report\n    raise ValueError(f\"no escalation #{escalation_id}\")\nValueError: no escalation #729\n"}
> **tried (set this version):** uncaught exception — not a routed fail()/escalate() Outcome
