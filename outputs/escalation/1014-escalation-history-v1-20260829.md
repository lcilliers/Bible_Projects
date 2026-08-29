# Escalation deep history

## #1014 — New setting governance.ps_worksheet_sync_on_change - the ru…
type=issue source=configmaint

**v1** (2026-08-29T04:13:34Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** New setting governance.ps_worksheet_sync_on_change - the ru…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "insert", "where": {}, "set": {"key": "governance.ps_worksheet_sync_on_change", "value": "\"any change to a PS scripts declared parameters (added, removed, or renamed) under iba/app/ps/** must be reflected in the same unit of work in iba/docs/ps tools worksheet.xlsx (its own tab), and for Escalation.ps1 specifically also in iba/docs/escalation actions worksheet.xlsx (the researchers model sheet) -- enforced by configmaint.validate (find_ps_worksheet_drift, find_escalation_worksheet_drift), not just stated\"", "use": "researcher ruling 2026-08-29: the two Excel worksheets are the live CLI interface to iba/app/ps and must not silently drift from the scripts they describe", "module": "governance"}, "full_message": "New setting governance.ps_worksheet_sync_on_change -- the rule statement itself (shown at every Start-Iba.ps1 session start alongside the other governance.* rules), backing the two new drift checks just proposed."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T04:15:50Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision -- Approve / Not-approve / Resubmit.
> **resolution (set this version):** Proposed: insert cfg_setting governance.ps_worksheet_sync_on_change = the rule statement (shown at every Start-Iba.ps1 session start). Not yet applied -- re-run Config-Maintenance.ps1 Propose with -RunId RUN-20260829_051333_114-CONFIGMAINT to apply once approved.

**v3** (2026-08-29T04:18:02Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted  
