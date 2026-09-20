# Escalation deep history

## #1797 — Mark legacy bible_research ib_observation inactive
type=issue source=configmaint

**v1** (2026-09-20T12:20:37Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Mark legacy bible_research ib_observation inactive
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_table", "op": "update", "where": {"database": "bible_research", "name": "ib_observation"}, "set": {"inactive": 1}, "full_message": "escalation #1783: this table is a small 81-row pre-IBA transitional store, its own cfg_table.use text already says it folds into ve_lexical items per the method reset and is not linked to current lexical tables -- exactly governance.tables criteria for inactive=1. Recommending this over withdrawing the finding, since the collision is real, just low-priority."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-09-20T12:20:54Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** My recommendation for #1783: mark cfg_table(database=bible_research, name=ib_observation).inactive=1, don't withdraw the finding (it's real, just low-priority/historical). Waiting on your actual approval -- this one's a judgment call, not something you've already dictated verbatim.
> **resolution (set this version):** Update cfg_table SET inactive=1 WHERE database='bible_research' AND name='ib_observation'.

**v3** (2026-09-20T12:24:39Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):**  approve excluding research db. 
