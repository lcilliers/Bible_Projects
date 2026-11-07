# Escalation deep history

## #2375 — Link glossary rule B:126 to Prose.ps1
type=issue source=configmaint

**v1** (2026-11-07T04:20:03Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Link glossary rule B:126 to Prose.ps1
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_rule_scope", "op": "insert", "where": {}, "set": {"rule_ref": "B:126", "scope_kind": "ps", "scope_value": "Prose.ps1", "inactive": 0}, "full_message": "#2373: the approved rule B:126 (glossary kept up to date without approval) reaches Claude at the first use of Prose.ps1, as B:53 and B:55 do. Researcher approved the rule; the link is its delivery, not a new decision."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-11-07T04:20:18Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Approval sought: link rule B:126 (glossary kept up to date without approval, approved in #2373) to Prose.ps1 in cfg_rule_scope, so it is delivered at the first use of Prose.ps1 as B:53 and B:55 are. Without the link the rule exists but reaches no operation, and configmaint.validate reports a rule with no scope as a coherence error. After approval, re-run the Propose command with -RunId RUN-20261107_042003_131-CONFIGMAINT.

**v3** (2026-11-07T04:21:56Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** approve B:126

**v4** (2026-11-07T04:34:22Z, Claude) state=completed next_action=approved assigned_to=Claude
> **resolution (set this version):** Committed: cfg_rule_scope row links B:126 (glossary kept up to date without approval) to Prose.ps1, scope_kind ps (run RUN-20261107_042003_131-CONFIGMAINT); checked live. The rule now reaches me at the first use of Prose.ps1 in a session.
