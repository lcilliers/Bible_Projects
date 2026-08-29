# Escalation deep history

## #1013 — New setting governance.escalation_worksheet_path - location…
type=issue source=configmaint

**v1** (2026-08-29T04:13:22Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** New setting governance.escalation_worksheet_path - location…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "insert", "where": {}, "set": {"key": "governance.escalation_worksheet_path", "value": "\"iba/docs/escalation actions worksheet.xlsx\"", "use": "the researcher own model worksheet, checked by configmaint.validate (find_escalation_worksheet_drift) -- every live Escalation.ps1 parameter must appear as a -Flag header somewhere in it", "module": "governance"}, "full_message": "New setting governance.escalation_worksheet_path -- location anchor for find_escalation_worksheet_drift, the subset-check half of the PS-worksheet-sync rule (Escalation.ps1 own model sheet, checked separately from the generic ps-tools worksheet since it is hand-built around fixed action-shapes, not one row per param)."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T04:15:47Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision -- Approve / Not-approve / Resubmit.
> **resolution (set this version):** Proposed: insert cfg_setting governance.escalation_worksheet_path = iba/docs/escalation actions worksheet.xlsx. Backs find_escalation_worksheet_drift (already built and tested). Not yet applied -- re-run Config-Maintenance.ps1 Propose with -RunId RUN-20260829_051321_649-CONFIGMAINT to apply once approved.

**v3** (2026-08-29T04:17:50Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted  
