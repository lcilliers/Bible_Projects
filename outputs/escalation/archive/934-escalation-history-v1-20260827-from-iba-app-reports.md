# Escalation deep history

## #934 — Repoint escalation.list_report_path from iba/app/reports/ t…
type=issue source=configmaint

**v1** (2026-08-27T15:09:13Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Repoint escalation.list_report_path from iba/app/reports/ t…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "escalation.list_report_path"}, "set": {"value": "\"outputs/escalation/escalation-list.md\""}, "full_message": "Repoint escalation.list_report_path from iba/app/reports/ to outputs/escalation/ -- researcher instruction this session (escalation #929/#736, iba/app/reports being discontinued as a filing destination; outputs/escalation is the stated canonical folder for escalation reports and investigations). First concrete step of the folder-destination realignment; archive_dir stays relative (archive/), so archived versions will land in outputs/escalation/archive/ automatically."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-27T15:13:22Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** proceed to prepare for approval -Context 
