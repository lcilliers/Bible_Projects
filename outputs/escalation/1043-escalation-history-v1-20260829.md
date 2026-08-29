# Escalation deep history

## #1043 — Register the completed one-off finding-verse-term-index mig…
type=issue source=configmaint

**v1** (2026-08-29T09:11:37Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Register the completed one-off finding-verse-term-index mig…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_utility", "op": "insert", "where": {}, "set": {"module": "scripts_apply_finding_verse_term_index_v1_20260829", "file_path": "scripts/_apply_finding_verse_term_index_v1_20260829.py", "purpose": "ONE-OFF migration, researcher-directed 2026-08-29 (finding verse/term index plan) -- creates finding_verse_index (M:N, direct to iba.verse.id) via 3 passes (structural, finding_verse_link migration, text-mined), backfills finding.strong_number via mti_terms.strongs_number -> iba.strong.strongNumber. Run and verified live 2026-08-29 -- one-off, not a reusable routine.", "inactive": 1}, "full_message": "Register the completed one-off finding-verse-term-index migration script in cfg_utility, inactive=1, per governance.new_utility_registration_timing."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T09:12:47Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision.
> **resolution (set this version):** Proposed: register scripts/_apply_finding_verse_term_index_v1_20260829.py in cfg_utility, inactive=1. Not yet applied -- re-run Config-Maintenance.ps1 Propose with -RunId RUN-20260829_101136_625-CONFIGMAINT to apply once approved.

**v3** (2026-08-29T10:05:44Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted 
