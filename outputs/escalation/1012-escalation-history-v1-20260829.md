# Escalation deep history

## #1012 — New setting governance.ps_worksheet_path = iba/docs/ps tool…
type=issue source=configmaint

**v1** (2026-08-29T04:13:03Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** New setting governance.ps_worksheet_path = iba/docs/ps tool…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "insert", "where": {}, "set": {"key": "governance.ps_worksheet_path", "value": "\"iba/docs/ps tools worksheet.xlsx\"", "use": "the ps-tools worksheet checked by configmaint.validate (find_ps_worksheet_drift) against every iba/app/ps/*.ps1 script live param() list", "module": "governance"}, "full_message": "New setting governance.ps_worksheet_path = iba/docs/ps tools worksheet.xlsx -- the location anchor for the new drift check (find_ps_worksheet_drift) that enforces your instruction: any change to a PS script's parameters must show up in this worksheet, or configmaint.validate now flags it. Part of a 3-setting group for this rule (this one, the escalation worksheet's own path, and the rule statement itself)."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T04:15:42Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision -- Approve / Not-approve / Resubmit.
> **resolution (set this version):** Proposed: insert cfg_setting governance.ps_worksheet_path = iba/docs/ps tools worksheet.xlsx. Backs find_ps_worksheet_drift (already built and tested, degrades to a not-set finding until this exists). Not yet applied -- re-run Config-Maintenance.ps1 Propose with -RunId RUN-20260829_051302_095-CONFIGMAINT to apply once approved.

**v3** (2026-08-29T04:17:35Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted  
