# Escalation deep history

## #1306 — Schema overview report
type=issue source=researcher

**v1** (2026-08-31T04:53:16Z, Researcher) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Schema overview report
> **comment (set this version):** There is no schema overview report for Bible_research_DB

**v2** (2026-08-31T04:54:28Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed to create report, also check if the IBA report is actually up to date and compliant 
> **context (set this version):**   

**v3** (2026-08-31T05:48:54Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Both parts done: (1) IBA report currency check -- the DBSchema register (iba/config/DBSchema/DBSchema.json) WAS stale: captured 2026-08-24 with 111 tables, live DB has 113 (--verify failed). Rebuilt it live (python iba/scripts/build_dbschema.py --db bible_research), re-verified PASS (113/113, all prior 1171 column descriptions preserved by name-match, 0 retired), and reconciled the config hash (cfg_apply.py --sync, 0.1.10 -> 0.1.11). (2) New schema overview report built and run: iba/app/tools/build_schema_overview_report.py, output at outputs/schema-overview-bible-research-20260831.md -- 113 tables, per-table description/rows/cols/PK/FKs/indexes, flags 3 undescribed tables + 45 undescribed columns for follow-up. Registered in cfg_utility per governance.new_utility_registration_timing -- proposed as escalation #1316, pending your approval (same class of pending item as #1315). Please review the report content itself (outputs/schema-overview-bible-research-20260831.md) and approve #1316 when ready.
> **context (set this version):** Deliverable: outputs/schema-overview-bible-research-20260831.md. Script: iba/app/tools/build_schema_overview_report.py. Pending: escalation #1316 (cfg_utility registration).

**v4** (2026-08-31T08:31:45Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Both parts complete: (1) the DBSchema register was genuinely stale (111 vs live 113 tables) -- rebuilt, re-verified PASS, config hash reconciled. (2) New report built and run: outputs/schema-overview-bible-research-20260831.md (per-table description/rows/cols/PK/FKs/indexes, flags 3 undescribed tables + 45 undescribed columns). Please review the report content itself; the script's cfg_utility registration is separately pending as escalation #1316.

**v5** (2026-08-31T08:48:27Z, Researcher) state=in-progress next_action=revise assigned_to=Claude
> **comment (set this version):** request for approval is denied. The schema report for IBA is simply wrong and incomplete.  There is no report for Bible_Research_db and no handle in the excel tools for this report.
