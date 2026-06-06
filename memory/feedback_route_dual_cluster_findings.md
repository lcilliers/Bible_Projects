---
name: feedback_route_dual_cluster_findings
description: When routing/re-homing a pointer or finding from one cluster to another, inspect its content — if it refers to BOTH clusters, create a finding in each, don't just move it
metadata:
  type: feedback
---

When a COMMENT_EVALUATION disposition would **move** an item from one cluster to another (route / rehome / re-assign), you must **inspect its actual content first**. If the content refers to **both** clusters (the source it currently sits under AND the destination), **a finding must be created for both clusters** — do not perform a one-way move that drops the source-cluster relationship.

**Why:** routing is lossy. An item often carries genuine analytical content for more than one cluster; moving it wholesale to the "primary" destination silently discards its relevance to the source. (Researcher rule, 2026-06-03, applied to pointer routing.) This is the pointer-level expression of [[feedback_cross_cluster_co_occurrence]] and the 2026-05-17 methodology-pivot directive (e).

**How to apply:**
- For every route/rehome candidate, read the full pointer/finding text — not just the gloss or the mechanical `cluster_link`.
- Single-cluster content (e.g. a superseded registry-structural `DIMENSION_REVIEW` that surfaced under a cluster only via a non-exclusive term→subgroup link) → route/set-aside as appropriate; no dual finding.
- Genuinely dual-cluster content → create a finding (or observation) in **each** cluster capturing that cluster's facet of the relationship, then close the source pointer.
- Watch borderline pairs where the concepts overlap (e.g. boldness↔pride, righteousness↔wickedness) — these are the ones most likely to be genuinely dual.
- Verify, don't assume single-cluster: inspect before deciding it's a one-way move.
