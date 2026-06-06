---
name: Term-anchor reset (2026-05-04 pivot)
description: Pipeline pivot — registry dropped as clustering driver, dimensions dropped, verse_context_group dropped from clustering inputs. Terms anchored into 55H + 33G clusters.
type: project
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
On 2026-05-04 the researcher pivoted the pipeline away from registry-as-driver. The cluster assessment showed registries dominate their own cluster only ~50% of the time at k=120; 76/120 clusters cross-cut 3+ registries.

Three things were dropped from the analytical pipeline:
- **Registry-as-clustering-driver** (registry retains only surface/collation role).
- **Dimension review** (judged "noise built on wrong assumptions").
- **`verse_context_group`** as clustering input (judged "limited and incomplete in value").

New structure (exploratory — not in DB, no instruction docs updated yet):
- 2,491 OWNER terms bucketed: T1 (1,752 primary) / T2 (491 secondary) / FLAG (24) / EXTRACTION-NOISE (37).
- 55 Hebrew clusters (`H001`..`H055`) + 33 Greek clusters (`G001`..`G033`).
- Per-verse classification (not per term-pair); brief plain-English meaning + unresolved-interpretation pointers.

**Why:** Registry-driven analysis was producing unreliable verse-context grouping, dimensions built on wrong premises, and analytics skewed toward boundary hallucinations rather than core meaning. See [research/notes/program reset.md](g:/My%20Drive/Bible_study_projects/research/notes/program%20reset.md).

**How to apply:** Do NOT assume registry-driven Session B / VC pipeline is the live model when assisting with new analytical work. Check the latest session log under `Workflow/Sessionlogs/` and `tasks.md` before proposing pipeline-shaped changes. Instruction docs (`wa-sessionb-analysis-readiness`, `wa-sessionb-analysis-output`, `wa-versecontext-instruction`, `wa-registry-management-guide`) describe the OLD model and have not yet been rewritten — flag this if the user asks to apply them. Open items listed in §4 of [Workflow/Sessionlogs/wa-sessionlog-term-anchor-reset-v1-20260504.md](g:/My%20Drive/Bible_study_projects/Workflow/Sessionlogs/wa-sessionlog-term-anchor-reset-v1-20260504.md).
