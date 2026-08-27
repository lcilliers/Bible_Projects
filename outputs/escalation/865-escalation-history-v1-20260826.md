# Escalation deep history

## #865 — escalation.history is a per-id point-in-time snapshot (like…
type=issue source=configmaint related_activity=configmaint.propose from_id=-1

**v1** (2026-08-26T10:13:45Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** escalation.history is a per-id point-in-time snapshot (like…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_report", "op": "update", "where": {"step": "escalation.history"}, "set": {"naming_scheme": "dated"}, "full_message": "escalation.history is a per-id point-in-time snapshot (like the word/strong reports), not a living doc anything links to by fixed name -- CONFIG-REPORT.md/GOVERNANCE.md style. Its report script was found (researcher instruction, #857) still producing a redundant plain-named duplicate (857-escalation-history.md) alongside the versioned file (857-escalation-history-v3-20260826.md), identical content. Fix: reportkit.write_report() now honours naming_scheme='dated' by skipping the plain-name write (code already changed, lib/reportkit.py). This flips escalation.history's own naming_scheme from stable to dated so that fix actually applies to it -- approve to activate; the code change is inert until this flips."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **related activity (set this version):** configmaint.propose

**v2** (2026-08-26T10:17:34Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **resolution (set this version):** Approved -- flip escalation.history's naming_scheme to 'dated' and apply the same fix to escalation.list. Nothing else without checking first.
