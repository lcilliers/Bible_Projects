# Escalation deep history

## #1305 — cfg_* is structurally coherent, but has findings needing yo…
type=issue source=configmaint

**v1** (2026-08-31T04:52:49Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** cfg_* is structurally coherent, but has findings needing yo…
> **comment (set this version):** coherence checks passed; these are advisory findings, not errors — approve to acknowledge as known/acceptable, reject to flag for action, or revise with a comment on what to check
> **context (set this version):** {"orphans": [], "needs_justification": ["cfg_setting 'candidate.quality_report_path' (module 'candidate') \u2014 candidate already has its own dedicated table (cfg_candidate_rule); confirm this belongs in shared cfg_setting rather than there", "cfg_setting 'candidate.load_report_path' (module 'candidate') \u2014 candidate already has its own dedicated table (cfg_candidate_rule); confirm this belongs in shared cfg_setting rather than there"], "stale_filled_by": [], "stale_docs": ["GOVERNANCE.md was last modified 2026-08-30T06:38:06Z, before the newest applied cfg_change_detail row (2026-08-31T04:52:24Z) \u2014 check whether that change needs an entry (GOVERNANCE.md \u00a78's own rule)"], "unregistered_lib_modules": [], "unregistered_project_scripts": [], "low_config_density_utilities": [], "orphan_book_order": [], "orphan_connection": [], "orphan_candidate_rule": [], "report_version_clutter": [], "escalation_ps_validateset_drift": [], "unresolvable_locations": [], "folderpurpose_ps_validateset_drift": [], "hand_rolled_versioning": ["iba/app/lib/prosestore.py builds a -v{n} filename by hand \u2014 no filingkit.versioned_path()/reportkit.oneoff_path() call site in the same file"], "ps_worksheet_drift": [], "escalation_worksheet_drift": [], "report_path": "outputs\\configs\\CONFIG-REPORT-v363-20260831.md", "full_message": "cfg_* is structurally coherent, but has findings needing your judgement: 2 setting(s) needing justification, 1 stale-doc finding(s), 1 script(s) building a -v{n} filename by hand instead of via filingkit. Full detail (every item, by category) written to outputs\\configs\\CONFIG-REPORT-v363-20260831.md \u2014 see the \"findings\" section."}
> **tried (set this version):** coherence checks passed; these are advisory findings, not errors — approve to acknowledge as known/acceptable, reject to flag for action, or revise with a comment on what to check

**v2** (2026-08-31T05:31:19Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed 
> **context (set this version):**   
