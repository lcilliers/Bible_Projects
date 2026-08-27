---
name: feedback-two-governing-principles
description: Two researcher-stated principles governing all programme analytics (2026-05-27)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

After a period of reflection following the M11 architectural question (see [[feedback-three-cluster-types]] and `Workflow/Sessionlogs/wa-sessionlog-20260526-cluster-architecture-question-v1.md`), the researcher decided to continue with the designed term-based methodology — complete the term-based window into scripture and meaning — and articulated two governing principles for all analytics from this point forward.

**Principle 1 — The verse meaning and context is the data and rules on all analytics.**

The verse text and its Pass A meaning are the ground truth. Cluster structure, characteristic labels, sub-groups, VCGs, and any analytical frame defer to what the verse actually says. When a cluster lens and a verse meaning conflict, the verse meaning wins. Analytical conveniences do not override the data.

**Principle 2 — All observations, however uncomfortable or disjointed, that come from the data must be recorded in the database.**

Bias-screening is forbidden. When an AI reads a verse and sees something that doesn't fit the cluster's primary frame — cross-register content, secondary inner-being content, surprise findings, content that contradicts the cluster's characteristic statement — the observation must be captured, not compressed into the cluster's lens. Disjointed observations are valid data. The current pipeline's `cluster_observation` table (`INTEGRATION_NOTE`, `CROSS_CLUSTER_HANDOFF`, `SELF_CHECK_OBSERVATION`, etc.) is the recording surface; analysts must use it generously.

**Why:** the M11 review (2026-05-26) surfaced that bias compounds through Pass A → sub-group placement → VCG description → Phase 9 findings. By Phase 9 the verse has been read through the cluster lens three times and the multi-faceted content of the verse is systematically deprioritised. The two principles arrest this — they require analysts to honour what the verse actually says and to record what doesn't fit, rather than fit it into the frame.

**How to apply:**
- **Pass A:** when writing a verse meaning under a cluster's anchor term, if the verse evidences additional inner-being content beyond the cluster's characteristic, name it explicitly in the meaning. Do not compress for cluster-frame.
- **Phase 3 verdicts:** if the AI's term verdict feels forced (the M11 ud "structural opposite" pattern), flag it explicitly as marginal rather than smoothing it into STAYS.
- **Phase 5 / 7 design:** sub-group and VCG descriptions must accurately reflect the verse evidence, not the cluster's preferred analytical shape. If verses don't cleanly fit a sub-group's frame, the sub-group description widens or a new sub-group is created — not the verses bent.
- **Phase 9 findings:** when a tier prompt surfaces evidence that exceeds the characteristic's scope, record it as a finding *and* seed a `cluster_observation` row (`INTEGRATION_NOTE` or `CROSS_CLUSTER_HANDOFF`) for downstream analytical use.
- **Session D / cross-cluster:** the cumulative cluster_observation corpus across all clusters becomes the substrate for cross-cluster synthesis. Observations are not noise to suppress; they are the raw material for the next layer of analysis.

**Triggered by:** researcher direction 2026-05-27 reopening M11 work after reflection. The M11 dilemma is held as evidence the principles are needed; the resolution is principle-based discipline, not architectural restructure.

Authoritative status: these principles govern all clusters in any phase from 2026-05-27 forward. If a future instruction-doc rev codifies them as numbered rules in v2_10+, this memory entry remains the canonical statement of intent.
