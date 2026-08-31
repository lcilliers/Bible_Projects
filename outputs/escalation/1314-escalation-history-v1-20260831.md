# Escalation deep history

## #1314 — CSV export should default to suppressed
type=issue source=Claude

**v1** (2026-08-31T05:11:21Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** CSV export should default to suppressed
> **comment (set this version):** Root-caused: cfgreport.py:generate() calls reportkit.write_csv_pairing() unconditionally, no flag gates it at all -- and generate() fires automatically after every single configmaint.propose write (configmaint.auto_report). Combined with the projects own never-overwrite-archive-the-prior-version convention (report.version_on_regenerate), every propose call leaves a fresh timestamped CSV per table behind rather than overwriting in place -- confirmed live: ~4700 files written to Workflow/schema/archive/ across one sessions intensive back-to-back proposals, all committed in the last session log. Researcher direction: the CSV export should be optional, defaulting to suppressed (opt-in, not automatic on every write) -- proposed shape: a new cfg_setting (e.g. configmaint.csv_export_on_auto_report, default 0) checked in generate() before calling write_csv_pairing(), so the auto-triggered post-propose regeneration skips the CSV side-output by default; an explicit configmaint.report run (or the flag set true) still produces it. Not yet built -- this is the finding + proposed shape, awaiting your approval before I touch cfgreport.py or add the setting.
> **context (set this version):** Logs/SESSION-LOG-20260831-cfg-quality-domain-review-certification-crisis-and-followup-bug.md; iba/app/lib/cfgreport.py:401-421

**v2** (2026-08-31T05:28:43Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed 
> **context (set this version):**   
