# Escalation deep history

## #2519 — Retire orphan cluster.recording_similarity_threshold
type=issue source=configmaint

**v1** (2026-11-20T18:46:11Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Retire orphan cluster.recording_similarity_threshold
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "cluster.recording_similarity_threshold"}, "set": {"inactive": 1}, "full_message": "#2506 orphan finding: no code reads this setting since the cluster generators were retired (#2507, BUILD 536); recordingpass.py keeps a 0.85 fallback. Set inactive; nothing else reads it."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-11-21T03:58:31Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Config change proposed for approval; see the proposal question.

**v3** (2026-11-21T03:58:31Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **resolution (set this version):** Researcher approved in chat on 2026-11-21, verbatim: 'Approve all three'
