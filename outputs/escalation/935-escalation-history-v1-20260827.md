# Escalation deep history

## #935 — Repoint escalation.history_report_dir from iba/app/reports…
type=issue source=configmaint

**v1** (2026-08-27T15:09:25Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Repoint escalation.history_report_dir from iba/app/reports…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "escalation.history_report_dir"}, "set": {"value": "\"outputs/escalation\""}, "full_message": "Repoint escalation.history_report_dir from iba/app/reports to outputs/escalation -- same rationale as escalation.list_report_path (companion change, same instruction, escalation #929/#736)."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-27T15:13:38Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** proceed to prepare for approval -Context 
