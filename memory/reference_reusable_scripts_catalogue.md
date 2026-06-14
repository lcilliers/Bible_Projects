---
name: reusable-scripts-catalogue
description: Canonical reusable report generators / extract builders / process scripts live in docs/reusable-scripts-catalogue.md — reuse don't recreate; never silently change a report's shape (comparability); _integrity_full_check points at dead Drive path; no DB-resident script registry yet (open item)
metadata:
  type: reference
---

REFERENCE (2026-06-14): the non-task-specific **reusable scripts** (report generators, extract builders, process scripts) are catalogued in `docs/reusable-scripts-catalogue.md`. Use it to avoid (a) recreating a script that exists, (b) silently changing a report so it is no longer comparable to prior runs, (c) errors/omissions. Canonical examples: `generate_programme_snapshot` · `generate_registry_overview` · `audit_cluster_v1_20260601` (the reusable cluster auditor) · `generate_full_cluster_audit` / `generate_cluster_summary` · `build_complete_extract` · `build_cluster_findings_digest` · `export_database_schema` · `build_file_manifest` · the reference-as-DB builders · verse-read `_apply_verse_read_meaning` / `_cc_verse_read` · `apply_session_patch` · `backup_db_to_nas` / `mirror_to_nas` · the `scripts/analytics/` library.

**Rules:** check the catalogue + `build_file_manifest.py --search` BEFORE writing a new script; if a report format must change, version the script `-vN` and flag it — never mutate a generator in place (comparability).

**Known issues:** `_integrity_full_check.py` hardcodes the dead `G:\My Drive\...` DB path (fix); no canonical/DB-resident script registry — heavy proliferation (~25 `_generate_cluster_*`, ~40 `_exploratory_*`) with no superseded markers (open item). Part of the governance-layers checklist — [[check-governance-layers-not-just-pipeline]] · [[reference-core-memory-orientation-map]].
