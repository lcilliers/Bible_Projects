---
name: feedback-cluster-publish-outputs
description: "Cluster publication artefacts (combined chapter docx, etc.) live in the cluster's own Published folder, not in outputs/"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

Combined / final publication artefacts for a cluster (docx of combined chapters, PDFs, exports for the researcher to share) belong in the cluster's `Sessions/Session_Clusters/{CODE}/Published/` folder — **not** in `outputs/docx/`. Filename follows the canonical convention: `wa-cluster-{CODE}-{ShortName}-combined-v{N}-{YYYYMMDD}.docx` (lowercase `wa-cluster` prefix, uppercase cluster code, short-name from `cluster.short_name`, ISO yyyymmdd).

**Why:** the Published folder is the published-artefact home; the cluster's draft markdowns live there too, so combined outputs sit alongside their sources. `outputs/docx/` is for ad-hoc / programme-wide exports, not cluster-publication artefacts.

**How to apply:** when building a derivative (combined doc, PDF, etc.) of a cluster's chapter drafts, write to `Sessions/Session_Clusters/{CODE}/Published/` using the canonical naming. The reusable script is `scripts/combine_cluster_published_to_docx.py --cluster {CODE}` — it auto-discovers the latest version per chapter and emits to the right folder. Related: [[feedback-cluster-file-naming-canonical]].

**All Published/ files belong in git.** Chapter drafts (`wa-cluster-{CODE}-ch{N}-draft-v{V}-...md`), appendices, and combined publication docx are key documents — when committing publication work, include the chapter MD files, not just the docx. Don't assume the user has already tracked their own drafts; if `git status` shows them untracked, add them as part of the same commit.
