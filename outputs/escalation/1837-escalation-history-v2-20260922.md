# Escalation deep history

## #1837 — Restore translit-never-without-gloss rule for Stage 1
type=issue source=configmaint

**v1** (2026-09-22T15:44:02Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Restore translit-never-without-gloss rule for Stage 1
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_method_rule", "op": "insert", "where": {}, "set": {"step": "lexical.meaning", "rule_key": "translit-never-without-gloss", "rule_text": "A Greek or Hebrew transliteration or script term is never rendered in obs_text without its own gloss alongside it (e.g. spoude \"earnestness\" not bare spoude) -- the gloss is what carries the sense for a reader without Greek/Hebrew literacy, the bare form alone is unreadable. Restores a real, previously-decided rule (researcher, 2026-06-15, pre-IBA ve_lexical narration review) that never carried forward into this pipeline when it was rebuilt under IBA -- escalation #1836.", "source_doc": "researcher 2026-06-15 review, restored via escalation #1836 (2026-09-22)", "ordinal": 0, "active": 1}, "full_message": "A real, previously-decided style rule (researcher, 2026-06-15) never carried forward into the IBA Stage 1 rebuild -- Greek/Hebrew terms in obs_text are appearing without their gloss, confirmed live in the M67 5-verse review. Registers it as a cfg_method_rule for lexical.meaning so it flows automatically into the prompt's existing 'Method rules governing this task' section, config-driven rather than hand-added prose."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-09-22T18:10:17Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  process and prepare for approval 
> **context (set this version):**   

**v3** (2026-09-22T18:13:37Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Claude
> **comment (set this version):** Processed per your instruction. Substance already decided (escalation #1836 diagnosed the gap, this restores the 2026-06-15 rule verbatim as cfg_method_rule for lexical.meaning). Coherence-checked against live cfg_* schema, no conflicts found. Moving straight to ready_for_approval -- no separate judgment call needed, just your approve/reject/revise.
> **resolution (set this version):** Pending insert (unapplied): cfg_method_rule step=lexical.meaning rule_key=translit-never-without-gloss, active=1. On approval: re-run Config-Maintenance.ps1 -Step Propose with this RunId to apply, per the standard configmaint cycle.

**v4** (2026-09-22T18:25:35Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Correction: my prior update (v2) set next_action=ready_for_approval but left assigned_to=Claude, so this never actually reached you -- reassigning now.

**v5** (2026-09-22T18:29:18Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):**  noted 
