---
name: feedback-three-cluster-types
description: "The term-anchor → characteristic-anchor drift produced three distinct cluster types; M11 surfaced that some clusters' characteristic corpora are scattered across other clusters' verses"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

The programme drifted from **term-anchored** clustering (each verse belongs to the cluster owning its Strong's number) toward **characteristic-anchored** analysis (since v2_6 the analytical unit is the inner-being characteristic, not the term-group). The drift was deliberate and right — the whole programme is about inner-being characteristics, not lexical inventories. But it produced three different cluster types that the old term-anchor architecture obscures:

1. **Clusters that fit one characteristic cleanly** — the term-grouping happens to align with one inner-being faculty. Example candidates: M07 (Shame), M02 (Sorrow), M10c (Defilement post-split). The "clean" case the Phase 5 sub-group / Phase 8.7 mapping was designed for.

2. **Clusters that are status-aspects** — the cluster captures aspects/dimensions of one larger status. M10 is the explicit case: 22 aspect-characteristics around the single characteristic "sin." Recorded via [[project_characteristic_backfill_backlog]] `char_structure='aspect_based'` (M10 closure 2026-05-26). Other candidates the user named in 2026-05-26 M11 discussion: life, atonement.

3. **Clusters with characteristic-legs in many other clusters** — the cluster captures only some of its characteristic's verses; the rest are anchored to non-cluster terms elsewhere. **M11 is the canonical example**: 421 verses in the DB contain "forgive" in English text; only 103 sit in M11; 246 are tagged primary to other clusters (M10 88, M05 19, M38 17, M45 10, etc.) because the verse's anchor Strong's is sin/love/etc., not a forgiveness verb. The same pattern likely applies to atonement, repentance, restoration.

**Why:** The term-anchor model gives each verse exactly one cluster home (the cluster of its anchor Strong's). The characteristic-driven analysis since v2_6 assumes each verse can be analyzed under whichever cluster's characteristic-lens applies. The two models cohabit but tension surfaces when a characteristic's evidence is highly distributed across anchor-terms (the M11 case).

**How to apply:** When proposing or evaluating cluster work, ask which of the three types the cluster is — the work shape differs:
- Type 1: Phase 5 sub-group mapping is 1:1 to characteristics; the clean v2_8 pipeline applies as-is.
- Type 2: Use `char_structure='aspect_based'`; exclude from cross-cluster characteristic analytics per [[project_characteristic_backfill_backlog]].
- Type 3: Acknowledge the cluster captures only the term-anchored subset of its characteristics' corpora; cross-cluster characteristic analytics (Phase 9 T6, Session D synthesis) must integrate verses anchored elsewhere.

For Type-3 clusters, "moving verses to the cluster" in the legacy sense isn't possible without re-anchoring (which the term-anchor system doesn't support). The realistic options are:
- Reclassify some non-cluster Strong's into the cluster (e.g. consider whether H5375 nasa "to bear/lift away" should sit in M11 alongside its current location, given its use in "bearing iniquity")
- Surface the characteristic-distribution at Phase 9 T6 findings (cross-cluster relationships)
- Recognize the cluster's analytical scope is narrower than its characteristic's corpus and design Session C/D accordingly

**Triggered by:** Researcher direction 2026-05-26 in M11 Phase 3 review. The marginal ud verdict opened a deeper inquiry; programme-wide forgive-language scan (421 verses, 103 in M11, 246 elsewhere) revealed the pattern.
