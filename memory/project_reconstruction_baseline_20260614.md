---
name: project_reconstruction_baseline_20260614
description: 2026-06-14 manifest-driven reconstruction of true project status/failures/table-relevancy/open-loops; CLAUDE.md+memory were drift-stale; use the reconstruction as truth until CLAUDE.md is refreshed
metadata:
  type: project
---

DONE (2026-06-14): built a full reconstruction of the project FROM THE WRITTEN RECORD because CLAUDE.md (last refresh 2026-04-27) and memory had DRIFTED from reality — CLAUDE.md claimed schema v3.11/3.17 (live is **3.31.0**), omitted the finding-centric architecture (`finding` 343k rows = the live unit; plus `cluster`/`characteristic`/`cluster_subgroup`/`cluster_finding`/`vcg_term`/`mti_term_subgroup`), and framed `word_registry` as "the 214-word anchor" when it is now scaffolding/entry-point — C-codes (C01–C22, dimension-review layer) COEXIST with the live M-code `cluster` table and are NOT dead.

Deliverables in `outputs/markdown/project-reconstruction/`: `00` spine-index · `01` status (ascending) · `02` failures/rework (~55 items; two roots = **over-structuring an integrated subject** + **decision↔artefact drift**) · `03` table-relevancy (usage/last-write view) · `04` open-loops & incomplete methodology.

Key open items: master register `Workflow/Programme/Program_reports/wa-programme-open-items.md` (127 items) BUT it predates the 2026-06-03 DB loss + 2026-06-04 foundations reset — currency uncertain. v3_2 cluster-rollup instruction is DRAFT (open item B3); catalogue refit approved but not in the DB; ~12 docs silently superseded (the v3_0 set still cited by CLAUDE.md). Until CLAUDE.md is refreshed (Plan B, approved), this reconstruction is the truth baseline. See [[source-of-truth-is-written-record]] · [[reference-core-memory-orientation-map]].
