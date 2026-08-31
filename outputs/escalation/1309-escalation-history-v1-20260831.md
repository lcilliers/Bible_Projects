# Escalation deep history

## #1309 — Escalation #1146: revoke configmaint.propose write access t…
type=issue source=configmaint

**v1** (2026-08-31T05:04:28Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Escalation #1146: revoke configmaint.propose write access t…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_write_grant", "op": "update", "where": {"writer": "configmaint.propose", "table_name": "cfg_change_detail", "database": "iba"}, "set": {"inactive": 1}, "full_message": "Escalation #1146: revoke configmaint.propose write access to cfg_change_detail (an audit-log table, not a rule table -- category=log per the new classification column). It must only ever be written by its own dedicated code path (handlers/configmaint.py propose()'s own INSERT), never hand-edited through the sanctioned config gate."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-31T05:31:47Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed 
> **context (set this version):**   
