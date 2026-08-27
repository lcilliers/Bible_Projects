---
name: feedback-cross-cluster-co-occurrence
description: "Before routing a verse to another cluster, analytics must confirm the verse has no secondary impact/clarification/role/relationship in the source cluster."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

Before a verse is routed from cluster X to cluster Y, the analytics must perform a **cross-cluster co-occurrence assessment**: does the verse contain terms from cluster X that have a meaningful secondary role even when the primary register belongs to Y? If so, the verse should not be merely transferred — it needs combined-meaning analysis recorded in cluster X before (or instead of) routing.

**Concrete example (the one the user gave):** A verse with both *joy* (M04) and *grace* (M05) terms must not be silently routed to M05. The analytics must ask: why do joy and grace co-occur here? Does the joint presence have a special joined meaning (e.g., "joy as the experiential face of grace")? That joined-meaning observation belongs to M04's record even if the verse's centre of gravity is M05.

**Why:** M04 BOUNDARY analysis showed 180 of 322 verses (56%) co-occur with terms from other clusters. Naive routing would silently transfer this co-occurrence evidence out of the source cluster, losing the cross-cluster relationships that the Observation Catalogue T6 prompts are designed to surface. T6 prompts run at Phase 9 — *after* routing decisions in the current Phase 4/5/6 — so co-occurrence has to be assessed earlier in the pipeline, not after the fact.

**How to apply:**
- New §17 (Cross-Cluster Co-occurrence Assessment) in the cluster instruction: before any Phase 6 routing or Phase 11.5 BOUNDARY resolution that targets ROUTE-TO-CLUSTER, AI must check whether each candidate verse contains terms from the source cluster and explicitly assess their role in the verse.
- Output: either (a) "no secondary role — route freely" or (b) "co-occurrence has joined meaning — record observation in source cluster, then route" or (c) "co-occurrence is structurally significant — verse stays in source cluster as primary, destination becomes XREF."
- The check is a Phase 4/5/6 input AND a Phase 11.5 BOUNDARY-resolution input.
- This is not a T6 substitute — T6 still runs at Phase 9 for evidence-flag routing. The co-occurrence check is a routing-time guard, not a finding-generation step.

Related: [[feedback-boundary-resolution-required]], [[feedback-inner-being-full-scope]].
