# Escalation deep history

## #1009 — table_export.output_dir was a single flat folder (Workflow/…
type=issue source=configmaint

**v1** (2026-08-29T04:03:02Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** table_export.output_dir was a single flat folder (Workflow/…
> **comment (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply
> **context (set this version):** {"table": "cfg_setting", "op": "update", "where": {"key": "table_export.output_dir"}, "set": {"value": "{\"iba\":\"Workflow/schema/iba\",\"bible_research\":\"Workflow/schema/bible_research\"}"}, "full_message": "table_export.output_dir was a single flat folder (Workflow/schema); now that table.export can dump either project database (escalation #1007, today), a bible_research.db run just landed its CSVs in the same folder as iba.db's, undifferentiated. Change it to a per-database map -- Workflow/schema/iba and Workflow/schema/bible_research -- same JSON-map shape prose.book_output_dir already uses. The handler (iba/app/handlers/reports.py:table_export) is already updated to read the map and raise on an unregistered database rather than guess."}
> **tried (set this version):** coherence-checked against the live cfg_* schema — awaiting researcher decision via `Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval` then `-NextAction approved` (or reject/revise), then re-run this exact Config-Maintenance.ps1 command with -RunId to apply

**v2** (2026-08-29T04:03:48Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Ready for your decision -- Approve / Not-approve / Resubmit.
> **resolution (set this version):** Proposed change: cfg_setting table_export.output_dir, from a single flat Workflow/schema to a per-database JSON map -- iba maps to Workflow/schema/iba, bible_research maps to Workflow/schema/bible_research. Handler code already updated (iba/app/handlers/reports.py table_export) to read the map and raise on an unregistered database. Not yet applied -- awaiting approval, then re-run Config-Maintenance.ps1 Propose with -RunId to apply.

**v3** (2026-08-29T04:06:11Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted correction 
