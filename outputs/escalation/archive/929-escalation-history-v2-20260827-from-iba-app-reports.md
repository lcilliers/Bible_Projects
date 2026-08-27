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

**v5** (2026-08-27T09:29:21Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** v2 delivered: outputs/markdown/folder-analytic-file-management-analysis-v2-20260827.md. Full census this time, not sampling: walked every directory in the project (1207 non-empty), filtered to analytic-file extensions (.md/.json/.docx/.pdf/.txt -- code and raw CSV table-exports excluded, matching v1's own scope statement), leaving 713 directories / 12,331 files, all real counts. Mapped against v1's 13-group taxonomy and gives full per-instance breakdowns for the two repeating-pattern areas (all 49 Sessions-v2 clusters, all of verse-analysis) rather than one sample each. 4 genuinely new findings v1's sampling missed entirely: (1) Sessions/Session_Clusters -- 2,006 files, the single largest concentration in the whole project, not named anywhere in v1; (2) a SECOND, separate per-book verse-analysis tree at iba/app/verse-analysis (308 files) using Title-Case/abbreviated book names, parallel to and inconsistent with the top-level verse-analysis/ tree's lowercase naming; (3) iba/app/config's own CONFIG-REPORT snapshot archive (310 files); (4) docs/ (36 files, flat, no subfolders, no archive, no group fit in v1's taxonomy -- a 14th pattern). Still does not recommend a standard or a disposition for the two things most obviously needing a decision (Session_Clusters' relationship to Sessions-v2; the two verse-analysis trees) -- flagged explicitly as needing your judgement on intent, not something a file count can resolve.

**v6** (2026-08-27T14:27:10Z, Researcher) state=in-progress next_action=revise assigned_to=Researcher
> **comment (set this version):** Researcher, verbatim: a significant change in folder structure has taken place. This may impact Claude's memory, renders previous folder analysis stale, and may impact folder destinations in config. Before assuming a folder for filing, Claude must check with the researcher until all baseline references have been reset.
