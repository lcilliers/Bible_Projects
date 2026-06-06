---
name: feedback-phase5-subgroups-represent-characteristics
description: Phase 5 (sub-group formation) — sub-groups MUST be designed to represent characteristics (inner-being faculties/states). One sub-group = one characteristic is the default. Multiple sub-groups for one characteristic is allowed ONLY when verse volume forces a split. The objective is upstream of clustering-by-meaning.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

Researcher direction 2026-05-19 (post-M07 Phase 4):

> *"you clearly need to include the objective that the sub groups should represent characteristics, but volume could mean that a characteristic is split in multiple sub groups. We did deal with this logic extensively."*

**Why:** The "extensive" prior work was the M04 retrofit (2026-05-18). At Phase 8.7 we discovered that M04's pre-existing sub-groups did **not** cleanly map to characteristics — one characteristic spanned multiple sub-groups (Joy spanned M04-B, C, D, E; Delight spanned M04-G, H, M, N, P), forcing a 4-version characteristic mapping debate to integrate them. The root cause: Phase 5 (the original sub-group formation) clustered by raw meaning similarity without the characteristic-as-objective frame.

For M07 starting fresh under v2_7, Phase 5 should bake in the characteristic objective from the start. This is the upstream fix to the M04 retrofit problem.

**The rule:**

1. **Sub-groups exist to represent characteristics.** The Phase 5 design begins by asking: "What inner-being characteristics does this cluster's meaning corpus express?" — then designs sub-groups to carry those characteristics.
2. **One sub-group = one characteristic is the default.** A clean 1:1 mapping is the target.
3. **Multiple sub-groups for one characteristic is the volume-split exception.** When a single characteristic's verse corpus exceeds the §8.6 distribution gate (40% of substantive verses), the characteristic is split into sub-groups by a documented split-axis (vertical vs horizontal, OT vs NT-distinctive, present vs eschatological, etc.). The characteristic identity is preserved across the splits; Phase 8.7 will bind them back via `characteristic_subgroup` rows.
4. **A sub-group serving two characteristics (SPLIT_SUBGROUP) is rare and must be flagged.** It arises when the same lexical sub-group contains different VCG registers serving different characteristics — e.g. M04-E carried `sa.s.von` (Joy register) and `agalliao` (Suffering-Joy register) in different VCGs. At Phase 5 this should be noted; at Phase 7 VCG design separates the registers; at Phase 8.7 the SPLIT_SUBGROUP observation is loaded.

**How to apply:**

- Phase 5 brief explicitly directs the AI to identify characteristics first, then design sub-groups around them.
- Phase 5 process step 1 reads as: *"Identify the inner-being characteristics the cluster's meaning corpus expresses."* Step 2: *"Design sub-groups to carry those characteristics."* Step 3 onward is the meaning-clustering refinement.
- The cross-register flags from Phase 3 v2 (per [[feedback_phase3_verse_level_relationship_test]]) are part of the characteristic identification at Phase 5: flagged terms suggest characteristics that the cluster's primary register doesn't fully cover.
- The §8.6 distribution gate is reframed: a >40% sub-group is not "one register dominating" — it's "one characteristic with too much verse volume to handle as a single sub-group". The fix is the same (split the sub-group) but the analytical frame is that a characteristic has been identified and its volume requires structural splitting, not that the cluster was under-decomposed at the characteristic level.
- Phase 8.7 (Characteristic mapping) becomes a confirmation step rather than a retrofit: the sub-group structure should already reflect the characteristic map; Phase 8.7 just loads it formally and surfaces any SPLIT_SUBGROUP cases.

Related:
- [[project_characteristic_backfill_backlog]] — closed clusters need analogous mapping; their Phase 5 was done before this principle.
- [[feedback_phase3_verse_level_relationship_test]] — cross-register flags feed Phase 5 characteristic identification.
- [[feedback_no_rework_paid_twice]] — adopt the principle upstream rather than retrofit downstream.
