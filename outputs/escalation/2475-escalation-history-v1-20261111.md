# Escalation deep history

## #2475 — Analytic reports and extracts belong in _analytics
type=task source=researcher

**v1** (2026-11-11T11:27:38Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Analytic reports and extracts belong in _analytics
> **comment (set this version):** Raised from #2463. Researcher, verbatim (2026-11-11): 'the instructions should be very clear - all analytic reports and extracts should be filed in analytics'. Found in config (read 2026-11-11): collection.evidence_path = outputs/reports/collection-evidence (#2464) and engagement.report_path = outputs/reports/engagement (#2406) sit under outputs/reports/, not _analytics/. The control map (cfg_control_home kind study_output) names _analytics/ as the home of study working files, but its text does not state that all analytic reports and extracts go there, and kind generated_report points tools to a *.report_path setting under outputs/. To settle: which tools count as analytic, where their folders go, the clear rule wording in cfg_control_home / cfg_behaviour_rule / iba/app/GOVERNANCE.md / iba/app/USER-GUIDE.md, and what happens to files already written. Nothing designed or changed here (B:105); the change is Developer Mode work.

**v2** (2026-11-11T11:29:40Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, verbatim (2026-11-11): 'i will fix your error in an separate developer session. just very disappointed that you stray from governance.' Claude lapses this session: stated the state of #2464 and the contents of the user guide without reading the record (B:1, B:34), and did not check report folders against the filing rule. The fix is the researcher's, in a separate Developer Mode session.
