---
name: source-of-truth-is-written-record
description: Establish project truth from the written record via the file manifest (ascending date); never reconstruct state from the DB or ask the researcher to re-derive what's already written; CLAUDE.md is the entry point, fan out from it
metadata:
  type: feedback
---

GOVERNING (2026-06-14): the project's authoritative state lives in the WRITTEN RECORD the researcher authored — session logs, docs, instructions, methodology, archive — not in the summaries. The **core entry point is CLAUDE.md; from there it fans out** (instructions → reconstruction → open-items → memory; see [[reference-core-memory-orientation-map]]). To establish "what is current / core / stale-but-relevant / dead": drive from `database/file_manifest.json` (rebuild first with `scripts/build_file_manifest.py`) and read the dated narrative spine in **ascending date order**.

**Why:** twice in one session I produced wrong answers by (1) reconstructing architecture from the DB (row counts ≠ relevance — that is fabrication, the [[project_meaning_duplicates_then_fabricates]] failure applied to structure), and (2) proposing the researcher re-classify by hand work he had already written down. Both ignore the record he deliberately kept.

**How to apply:** read and CITE the source doc for every claim; treat row-count/last-write as *evidence*, not verdict; where the record is silent, flag it as an open question — never fill the gap with a guess. CLAUDE.md itself is currently drift-stale (schema/architecture) — cross-check against [[project_reconstruction_baseline_20260614]].
