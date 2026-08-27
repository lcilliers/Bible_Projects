---
name: feedback_span_pairing_and_reciprocal_findings
description: A verse's sibling spans must NEVER be silently ignored. T2 spans are paired explicitly into the T1 span's Pass A meaning (they expand its definition). A multi-T1 verse — the cluster under review names the other T1 span in its meaning + keywords + finding, and the system auto-creates a candidate finding in the other cluster(s) for their consideration.
metadata:
  type: feedback
---

Researcher direction 2026-06-05, governing how span co-occurrence is handled in verse meaning and findings.
Builds on [[feedback_t1_vs_t2_ontology]] (T1 = characteristic in operation; T2 = recipient/effect/modifier)
and the span investigation (`research/investigations/verse-span-cross-cluster-usage-20260605.md`).

**The governing rule: a sibling span in the verse is never silently ignored.**

1. **T2 siblings are paired into the T1 meaning — explicitly.** When deriving the Pass A meaning of a
   cluster's T1 span, the verse's **T2 spans** (recipient / object / trigger / locus / qualifier) are
   **fundamentally paired with it** and taken into account as part of the verse-meaning rules. T2 *expands
   the definition* of the associated T1 span (e.g. fear's object = "the Most High"; dread's locus = "hand").
   This must be **explicit in the meaning**, not assumed.

2. **Multi-T1 verses (a span in ≥2 named clusters) — apply the INFLUENCE TEST first** (refined 2026-06-05,
   Lev 19:3): does the sibling T1 span **influence** the target span in this verse?
   - **If it influences** (the two characteristics interact): the cluster under review's **meaning and
     keywords name the other T1 span**; the **finding mentions it**; and the system **auto-creates a
     candidate finding in the other cluster(s)**.
   - **If it is independent** (co-located but not interacting — e.g. Lev 19:3 "revere parents" ∥ "keep
     sabbaths"): do **NOT** weave it into the target meaning/keywords (that *clouds* the cluster). The
     sibling simply **flows through to its own cluster** (gets analysed there; a reciprocal/cross-ref
     finding), but the target meaning stays focused on its own span.
   - The verse is **not moved** in either case. **"Never silently ignore" ≠ "always weave in"** — independent
     siblings are acknowledged via flow-through, not by clouding the target.

3. **Forbidden:** silently ignoring the other span in the verse. Every sibling span is either paired-in (T2)
   or named + reciprocally-seeded (T1).

**Why:** 63% of M01 verses are genuinely cross-functional (carry another named-cluster span); reading a
verse through one span while ignoring its siblings loses real inner-being content and breaks the
"all-observations-recorded" principle ([[feedback_two_governing_principles]] P2). Pairing T2 in deepens the
meaning; naming + reciprocal-seeding T1 preserves multi-belonging without lossy reassignment.

**How to apply:**
- **Pass A input** = full verse + ALL sibling spans (per-verse classifier shape), inherited *structure*
  still suppressed. Classify each sibling as T1 (named cluster) / T2 (supplementary) / FLAG (pending).
- **Pass A meaning rubric:** pair T2 siblings in explicitly; for multi-T1, name the other T1 span in meaning
  + keywords.
- **Findings (Phase D):** a finding on a multi-T1 verse names the sibling span; pipeline auto-seeds a
  candidate finding in each sibling cluster (`create_finding` per cluster — consistent with
  [[feedback_route_dual_cluster_findings]] and [[feedback_remediation_is_analysis_not_reassignment]]).
- **Audit:** a cross-cluster check flags any multi-T1 verse whose target meaning/keywords/finding does NOT
  reference the sibling (silently ignored), and any missing reciprocal finding.

Related: [[feedback_cross_cluster_co_occurrence]], [[project_pointer_lifecycle_model]],
[[reference_analysis_rules_finding_lifecycle]].
