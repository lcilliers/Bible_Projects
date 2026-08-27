---
name: feedback_emergent_aggregate_questions
description: The structured fix for the historic "cluster-level / general observation" drift. Ask an explicit EMERGENT question at each aggregation rung (verses→VCG, VCGs→sub-group, sub-groups→cluster) — "what does the collection jointly say that the parts don't / how do they operate together" — and record the answer anchored to that level. Characteristics EMERGE bottom-up from the sub-group/cluster aggregate answers.
metadata:
  type: feedback
---

**Researcher direction 2026-06-06.** Much of the historic **misses and drift** came from "cluster-level"
or "general observation" being an **unstructured catch-all**: an observation true of a *collection* (not of
any single member) had **no specific home**, so it drifted, was mis-assigned, or lost.

**The fix — an emergent-question ladder, asked explicitly at each aggregation rung, recorded level-anchored:**
1. **Verses → VCG:** *what does this collection of verses jointly say about the VCG that no single verse
   captures?* (not every verse gives the complete picture) → recorded on the VCG.
2. **VCGs → sub-group:** *what do these VCGs jointly say about the sub-group — how do its dimensions operate
   together?* → recorded at sub-group level.
3. **Sub-groups → cluster:** *what do these sub-groups jointly say about the cluster — how do they operate
   together?* → recorded at cluster level.

Each answer is an **emergent observation** (true of the whole, not reducible to the parts) and now has a
**definite home** — no drift. Runs **up** the ladder as the VCG read completes and structure firms.

**The payoff — characteristics EMERGE.** The sub-group/cluster aggregate questions ("how do these operate
together") are exactly the questions whose answers *are* the characteristics. So the characteristic structure
**crystallises bottom-up from the data — discovered, not imposed** (resolves foundations §c-Q4; the real
mechanism behind [[feedback_phase5_subgroups_represent_characteristics]], instead of pre-designing and
back-filling). Aligns with [[feedback_no_forced_structure_audit_surfaces_analysis_compensates]] and the
meaning-centric direction.

**Recording surface:** `cluster_observation` (anchors at `cluster_code` / `characteristic_id` /
`cluster_subgroup_id`); its existing types (`CLUSTER_SYNTHESIS`, `INTER_RELATIONSHIP`, `INTEGRATION_NOTE`)
*are* these emergent observations — they were just unstructured by level. **Data gap:** no VCG (`group_id`)
anchor — a VCG-level emergent observation needs a `group_id` column or a home on `verse_context_group`.

Built into the reshape: `Workflow/methodology/wa-cluster-phase-reshape-v3_1-proposal.md`. Honours
[[feedback_two_governing_principles]] P2 (all observations recorded) by giving each its level-anchored home.
