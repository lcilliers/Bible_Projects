# Escalation deep history

## #2521 — glossary.currency_check: drop retired concept terms
type=issue source=configmaint

**v1** (2026-11-20T18:46:32Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** glossary.currency_check: drop retired concept terms
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "glossary.currency_check"}, "set": {"value": "[\"role\", \"characteristic\", \"operation\", \"M-Code cluster\", \"T2\", \"T3\", \"inner being\", \"base\", \"inflection\", \"derivation\", \"surface group\", \"subgroup\", \"collection\"]"}, "full_message": "#2506 glossary currency finding: concept and concept domain were retired on 2026-11-15 (#2505; the collection took their place, researcher on #2515 Q5). Their glossary entries say Retired, so they are removed from the currency check list."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-11-21T03:58:31Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Config change proposed for approval; see the proposal question.

**v3** (2026-11-21T03:58:32Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **resolution (set this version):** Researcher approved in chat on 2026-11-21, verbatim: 'Approve all three'
