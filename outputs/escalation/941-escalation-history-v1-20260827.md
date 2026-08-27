# Escalation deep history

## #941 — Folder-destination realignment (escalation #929/#736): repo…
type=issue source=configmaint

**v1** (2026-08-27T19:08:29Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Folder-destination realignment (escalation #929/#736): repo…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "content_index.report_path"}, "set": {"value": "\"outputs/content_index/content-index-rebuild.md\""}, "full_message": "Folder-destination realignment (escalation #929/#736): repoint content_index.report_path to outputs/content_index/content-index-rebuild.md."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-27T19:11:05Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Folder-destination realignment batch (escalation #929/#736) -- diff confirmed, ready for your approval.

**v3** (2026-08-27T19:12:36Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** proceed to prepare for approval 
