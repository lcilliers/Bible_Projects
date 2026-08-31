# Escalation deep history

## #1350 — configmaint.propose crashed: propose requires -Title - a sh…
type=run_error source=configmaint

**v1** (2026-08-31T12:39:32Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** configmaint.propose crashed: propose requires -Title - a sh…
> **comment (set this version):** uncaught exception — not a routed fail()/escalate() Outcome
> **context (set this version):** {"traceback": "Traceback (most recent call last):\n  File \"C:\\Bible_study_projects\\iba\\app\\run.py\", line 179, in run_step\n    outcome: Outcome = handler(ctx)\n                       ~~~~~~~^^^^^\n  File \"C:\\Bible_study_projects\\iba\\app\\handlers\\configmaint.py\", line 643, in propose\n    raise ValueError(\n    ...<2 lines>...\n        \"-Question is the fuller representative description (what/why/effect), not the title.\")\nValueError: propose requires -Title -- a short, title-shaped name for this change (<=60 chars, no clause-stitching, e.g. 'Add configmaint.csv_export_on_auto_report setting'). -Question is the fuller representative description (what/why/effect), not the title.\n", "full_message": "configmaint.propose crashed: propose requires -Title -- a short, title-shaped name for this change (<=60 chars, no clause-stitching, e.g. 'Add configmaint.csv_export_on_auto_report setting'). -Question is the fuller representative description (what/why/effect), not the title."}
> **tried (set this version):** uncaught exception — not a routed fail()/escalate() Outcome
