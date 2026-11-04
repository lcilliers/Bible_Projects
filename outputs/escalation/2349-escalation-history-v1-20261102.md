# Escalation deep history

## #2349 — Register local LLM pilot PS wrapper
type=issue source=configmaint

**v1** (2026-11-01T09:18:25Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Register local LLM pilot PS wrapper
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_utility", "op": "insert", "where": {}, "set": {"module": "pilot_local_llm_run", "file_path": "iba/app/staging/pilot_local_llm/Pilot-LocalLLM.ps1", "purpose": "Local LLM pilot (BUILD 438, #2337): PowerShell wrapper that runs the pilot against the local model.", "inactive": 0, "config_exempt": 1, "config_exempt_reason": "staging pilot wrapper; no tunable settings yet (#2337)", "crash_escalation_reviewed": 0}, "full_message": "Register the local LLM pilot PS wrapper in cfg_utility. Researcher instruction, chat 2026-11-01: 'you can register the local llm'. Clears the second coherence error in #2341."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-11-01T09:25:54Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** Researcher, chat 2026-11-01, verbatim: 'I am not ready to deal with 2350, 2349, and 2348 - the local llm deployment is on hold.'
