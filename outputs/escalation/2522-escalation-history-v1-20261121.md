# Escalation deep history

## #2522 — programme_stages: stage 5 follow-up named
type=issue source=configmaint

**v1** (2026-11-20T18:47:11Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** programme_stages: stage 5 follow-up named
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "governance.programme_stages"}, "set": {"value": "\"The research programme has three main stages: Base_data (STEP, the spine and verse_lexical, Window 1 Layer 1); Analysis (deriving understanding of the inner being: the lexical analysis of the words by collection, Window 1 Layer 2 and stage 1 of the collection reading; the grouping of the surfaces, stage 2; the verse-lexical observations, stage 3; the inner-being analysis, stage 4; the claim formulation, stage 5, which is undecided and stated as such in the programme prose, section Programme flow, what is not yet defined); Publishing (essays and output for the results). Previously referred to as Session A (base data), Session B/D (analytics), Session C (publishing) -- methodologies and processes have changed materially over time across all three.\""}, "full_message": "#2506 hedge-phrase finding: the value says stage 5 is 'not yet decided' with no follow-up. Reword to point at the programme prose section that states it as undecided. Meaning unchanged."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-11-21T03:58:32Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Config change proposed for approval; see the proposal question.

**v3** (2026-11-21T03:58:32Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **resolution (set this version):** Researcher approved in chat on 2026-11-21, verbatim: 'Approve all three'
