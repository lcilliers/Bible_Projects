---
name: project_pointer_lifecycle_model
description: "Session B/D pointers are inputs to cluster analysis — routed to cluster(s), validated during analysis, adopted into a tier-question/characteristic/cluster finding + cross-ref + closed, or set aside as non-evidenced."
metadata: 
  node_type: memory
  type: project
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Session B & D pointers (`wa_session_b_findings` + `wa_session_research_flags` SD_POINTER/SB_FINDING/SB_INNER_BEING) are **inputs to cluster analysis, not findings themselves**. Lifecycle (researcher, 2026-06-01):

1. **Route** to cluster(s) — confirmed **many-to-many**; link is multi-value.
2. **Validate during that cluster's analysis**, then **adopt** into one of: a **tier-question finding** (most common — the tier/observation catalogue should cover most term findings); a **separate characteristic finding** (rare); or a **cluster finding**.
3. **Cross-reference** the original pointer to that finding and **close** it.
4. **Unconverted → set aside as non-evidenced.**

Routing must be **precise**: link a pointer to the cluster of its *subject* term (named Strong's / transliteration), NOT to every cluster whose terms merely appear in its cited verses (verse refs are broad and would flood each cluster). Clusters are **agnostic to registries** — registry is not a cluster route; only term/verse/gloss are. See [[feedback_findings_marginal_value]] and [[project_term_anchor_reset]].

**How to apply:** the cluster link routes pointers into the right cluster's analysis; disposition (adopt+xref+close, or set-aside-non-evidenced) happens per-cluster during analysis, reusing existing fields (flags: `resolved`/`resolved_note`; findings: `status` + `related_finding_id`). Working analysis: `research/investigations/session-bd-pointers-linking-20260601.md`.
