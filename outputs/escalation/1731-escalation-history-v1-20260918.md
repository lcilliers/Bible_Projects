# Escalation deep history

## #1731 — Fix cluster_subgroup.cluster_code FK syntax (iba)
type=issue source=configmaint

**v1** (2026-09-18T05:17:29Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Fix cluster_subgroup.cluster_code FK syntax (iba)
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_column", "op": "update", "where": {"database": "iba", "table_name": "cluster_subgroup", "name": "cluster_code"}, "set": {"fk": "cluster.cluster_code"}, "full_message": "cfg_column iba.cluster_subgroup.cluster_code has fk='cluster(cluster_code)' -- a parenthetical syntax the validator's FK check does not parse (it expects dotted table.column, the format used by all 133 other fk values in cfg_column). Fix: correct to the dotted form."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-09-18T05:20:28Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Coherence-checked against the live cfg_* schema (configmaint.propose accepted the proposal without complaint). Part of the batch closing escalation #1727's 18 coherence errors, found live by configmaint.validate right after the M67 cluster-reading pipeline build. Ready for your approve/reject/revise.

**v3** (2026-09-18T05:39:28Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):**  noted
