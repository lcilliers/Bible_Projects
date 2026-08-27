# Escalation deep history

## #929 — Folder analysis - analysis
type=task source=researcher

**v1** (2026-08-27T08:59:23Z, Researcher) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Folder analysis - analysis
> **comment (set this version):** Extract to md a report that include an analysis of every folder in the project that have analytic files included - the aim of this analysis is to consolidate all the different variations of file managament of analytic files (include archives)

**v2** (2026-08-27T09:00:20Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Prepare the analysis and report

**v3** (2026-08-27T09:10:57Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Delivered: outputs/markdown/folder-analytic-file-management-analysis-v1-20260827.md. Walked every top-level directory (Sessions, Sessions-v2's 49 cluster folders, Workflow, archive, docs, outputs, research, verse-analysis's 23 book folders, iba/docs, iba/app/reports, Logs, memory, database/archive), grouped analytic-file-bearing folders into 13 groups (A-M) by structural convention rather than listing every leaf folder separately (most of Sessions-v2/verse-analysis share one convention each). Found 7 distinct filename conventions in live use and, more materially for consolidation, at least 4 different archiving shapes coexisting with no rule anywhere naming which a given file should use: a local archive/ sibling per folder, one shared outputs/archive/ for a whole tree, a separate project-root archive/ mirroring the whole tree, and no archiving at all in several areas. Only one of the 13 groups (iba/app/reports) has any of this actually declared in config (governance.oneoff_report_dir/_archive_dir/_naming_pattern) -- everything else runs on inherited convention alone. Report deliberately does not recommend which convention should become the standard -- that's the consolidation decision, not something to pre-empt here.

**v4** (2026-08-27T09:23:16Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** This is a good extract, now combine the actual files in folders of the entire project and map it to this what is should be
