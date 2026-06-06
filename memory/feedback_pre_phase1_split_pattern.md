---
name: feedback-pre-phase1-split-pattern
description: "A too-large cluster with status='Not started' can be split along ontological lines before Phase 1 begins, at low cost"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

When a cluster (e.g. M10 with 88 OWNER terms, 26 registries) is heterogeneous enough to span multiple ontological tracks, splitting it BEFORE Phase 1 work begins is a valid cheap move. Apply when `cluster.status='Not started'`.

**Why:** Splitting later (mid-pipeline) is far more expensive — it invalidates Phase 1/3/5 outputs, forces re-runs of UT reviews and constitution debates. Splitting at the metadata stage is just `INSERT cluster + UPDATE mti_terms.cluster_code` plus a design record. M10 precedent (2026-05-22): split into M10 (Sin/Guilt/Transgression — act/state), M10b (Wickedness/Evil/Abomination — character), M10c (Defilement/Impurity — ritual/moral).

**How to apply:**
1. Confirm `cluster.status='Not started'` (no derivative work to invalidate).
2. Identify the ontological tracks the cluster spans — these are usually the question the lexemes collectively answer: "what did I do?" vs "what kind of person?" vs "what state am I in?".
3. Make registry-level cuts where possible (keeps the script simple); record borderline terms for new-cluster Phase 1 to revisit.
4. Apply via one script: INSERT new cluster rows, UPDATE old cluster row's description/short_name, UPDATE `mti_terms.cluster_code` in batch, regenerate gloss from members.
5. Always pair with a `wa-cluster-{CODE}-split-design-v{n}-{date}.md` record giving rationale + assignment table + borderline term notes.

Related: [[feedback-phase5-subgroups-represent-characteristics]] — once you're past Phase 1, sub-group splits are the right tool; pre-Phase-1 cluster splits address a more fundamental ontological mismatch.
