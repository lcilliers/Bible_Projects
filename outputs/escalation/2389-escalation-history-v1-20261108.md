# Escalation deep history

## #2389 — Register step group.set
type=issue source=configmaint

**v1** (2026-11-07T18:15:28Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Register step group.set
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_step", "op": "insert", "where": {}, "set": {"work_package": "surface-group", "ordinal": 3, "step": "group.set", "handler": "iba.app.handlers.surfacegroup:set_group", "scope": "none", "does": "set the group of named surfaces by the researcher ruling, stored confirmed with a surface_event each; -Group, -Surface, -Reason, -Check previews -- see lib/surfacegroup.py (escalation #2388)", "inactive": 0, "kind": "operations"}, "full_message": "Register the Set action of the group step (approved on #2388 v5): step group.set in work package surface-group, handler iba.app.handlers.surfacegroup:set_group. Tested on a copy: 13 cases pass."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
