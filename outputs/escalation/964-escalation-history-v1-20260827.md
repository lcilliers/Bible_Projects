# Escalation deep history

## #964 — Folder-destination realignment (escalation #929/#736): repo…
type=issue source=configmaint

**v1** (2026-08-27T19:30:48Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Folder-destination realignment (escalation #929/#736): repo…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "table_export.output_dir"}, "set": {"value": "\"workflow/schema\""}, "full_message": "Folder-destination realignment (escalation #929/#736): repoint table_export.output_dir to workflow/schema per researcher instruction (all table exports go to workflow/schema)."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
