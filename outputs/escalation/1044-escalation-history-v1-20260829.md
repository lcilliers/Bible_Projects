# Escalation deep history

## #1044 — New sqlite behaviour-class rule: inactive tables/columns ar…
type=issue source=configmaint

**v1** (2026-08-29T09:11:50Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** New sqlite behaviour-class rule: inactive tables/columns ar…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_behaviour_rule", "op": "insert", "where": {}, "set": {"class": "sqlite", "rule_key": "inactive-tables-never-active-inputs", "rule_text": "A table (or column) marked inactive=1 in cfg_table/cfg_column must never be factored into any report, analysis, or other active/ongoing process -- reading it as a one-time migration SOURCE to backfill a new live structure, once, is not the same thing and remains fine. Inactive data is retained in the database solely to aid investigation when an error or historical question arises -- to clarify and reach back into the past -- not as a live input.", "source": "researcher, 2026-08-29"}, "full_message": "New sqlite behaviour-class rule: inactive tables/columns are never live inputs to reports/analysis/ongoing processes -- retained only for historical investigation. One-time migration reads (already this sessions established pattern) are explicitly not a violation of this rule. governance.tables already requires marking inactive; this states what inactive actually MEANS in terms of usage, which nothing previously captured."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T09:12:50Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision.
> **resolution (set this version):** Proposed: new cfg_behaviour_rule (class=sqlite, rule_key=inactive-tables-never-active-inputs) -- inactive tables/columns are never live inputs to reports/analysis/ongoing processes, retained only for historical investigation; one-time migration reads are explicitly exempted. Not yet applied -- re-run Config-Maintenance.ps1 Propose with -RunId RUN-20260829_101150_015-CONFIGMAINT to apply once approved.

**v3** (2026-08-29T10:05:58Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted 
