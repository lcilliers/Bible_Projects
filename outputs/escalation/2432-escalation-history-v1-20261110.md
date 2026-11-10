# Escalation deep history

## #2432 — Register step collection.gather
type=issue source=configmaint

**v1** (2026-11-10T09:35:39Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Register step collection.gather
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_step", "op": "insert", "where": {}, "set": {"kind": "operations", "ordinal": 10, "handler": "iba.app.handlers.collectionbuild:gather", "inactive": 0, "work_package": "collection-build", "scope": "none", "does": "make one collection of the surfaces the researcher names (tier gathered), without the AI and without a judged core; -Name, -Surface, -Reason, -Check -- see lib/collectionbuild.py (escalation #2388)", "step": "collection.gather"}, "full_message": "Register the step collection.gather for the new action Collection-Build.ps1 -Action Gather (escalation #2388, researcher 2026-11-10: Approve Gather): one collection of the surfaces the researcher names, tier gathered, without the AI. Tested 13 of 13 on a scratch copy (iba/app/tools/temp_2388_gather_test_run.py). Handler iba/app/handlers/collectionbuild.py, logic iba/app/lib/collectionbuild.py. One approval covers this row, the matching refusal route and the change to the list of tiers (the next two proposals)."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-11-10T09:36:37Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Approval sought: register the step collection.gather (and, for 2433, its refusal route) for the new action Collection-Build.ps1 -Action Gather in iba/app/ps/Collection-Build.ps1, covered by the researcher's approval of the Gather design in chat 2026-11-10: Approve Gather (recorded in #2388 v21). Ready: tested 13 of 13 by iba/app/tools/temp_2388_gather_test_run.py. Claude applies the row by re-running its Propose with -RunId.

**v3** (2026-11-10T09:36:37Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher in chat 2026-11-10: Approve Gather (the registration is part of the design approved in #2388 v21)

**v4** (2026-11-10T09:37:40Z, Claude) state=completed next_action=approved assigned_to=Claude
> **resolution (set this version):** Applied 2026-11-10 by re-running its Propose with its run id, on the researcher's Approve Gather (#2388 v21).
