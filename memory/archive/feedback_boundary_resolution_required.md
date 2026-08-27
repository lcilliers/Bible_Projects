---
name: feedback-boundary-resolution-required
description: "BOUNDARY-pending is NOT a valid cluster closure state. Only three valid resolutions: set aside (no inner-being involvement), move to another cluster, or move to a sub-group."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

BOUNDARY is a working state for verses where the disposition is unresolved. **Closure of a cluster cannot proceed while BOUNDARY decisions are merely parked.** Every BOUNDARY-flagged verse must be resolved into one of exactly three outcomes:

1. **No inner-being involvement** → set aside (verse leaves the cluster permanently with explicit reasoning)
2. **Move to another cluster** → route to the destination cluster (subject to the cross-cluster co-occurrence check — see [[feedback-cross-cluster-co-occurrence]])
3. **Move to an existing or new sub-group** → keep the verse in the current cluster under a defined sub-group

**Why:** M01 (7), M02 (4), M03 (28), and incoming M04 (~322) accumulated BOUNDARY_DECISION_PENDING flags that were not resolved before Phase 12 closure. The user identified this as a methodology defect: parking a verse with a flag is not a decision, and a "closed" cluster carrying unresolved BOUNDARY counts is not actually closed. Combined with [[feedback-inner-being-full-scope]], this also creates a backlog of mis-set-aside verses that need re-examination.

**How to apply:**
- Cluster-instruction Phase 12 (closure) precondition must explicitly require BOUNDARY_DECISION_PENDING count = 0 for the cluster.
- Add a new Phase (11.5 or equivalent — "BOUNDARY resolution pass") that runs after Phase 9/10/11 catalogue work and before Phase 12 closure. Workflow: cross-cluster co-occurrence check → AI disposition proposal (one of the three outcomes per verse) → researcher approval → CC apply.
- For already-closed clusters carrying unresolved BOUNDARY (M01, M02, M03, M15 audit), trigger the re-examination workflow rather than ignoring.
- Reject AI Phase 5/7/8 outputs that propose to "park" verses indefinitely — push back to a real disposition.

Related: [[feedback-inner-being-full-scope]], [[feedback-cross-cluster-co-occurrence]], [[feedback-re-examination-workflow]].
