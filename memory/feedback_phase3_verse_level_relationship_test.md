---
name: feedback-phase3-verse-level-relationship-test
description: "Phase 3 (cluster constitution debate) — before a TRANSFERS verdict, debate must check verse-by-verse whether any verse in the term's corpus evidences a relationship with or impact on the SOURCE cluster's characteristic. STAYS if any does (with cross-register flag). TRANSFERS confirmed only when no verse evidences any source-cluster relationship — i.e., accidental placement."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

Researcher direction 2026-05-19 (verbatim during M07 Phase 3 debate):

> *"I want to challenge the outcome. Before considering pushing terms to another cluster, the debate should clearly consider if the transferred term impacts or have a relationship with the current cluster. This can only be decided on the verse level."*

> *STAYS if any verse evidences a relationship with or impact on the cluster's characteristic, even where the term's primary register lies elsewhere. Relationship flagged in rationale for Phase 5/7 processing.*
> *TRANSFERS confirmed only if no verse evidences any source-cluster relationship — the term has landed accidentally.*
> *If a term has no meaning contexts that allude to potential impact on the source cluster, it transfers regardless.*

**Why:** Phase 3 v1 of M07 produced 10 TRANSFERS verdicts at corpus-primary-register level (e.g. `exoutheneō` → M06 because contempt is primarily M06 territory). The researcher challenged this: the question isn't "what is the term's primary register?" but "does any verse in this term's corpus carry a verse-level relationship with the source cluster?" `exoutheneō`'s contempt-dishonour dynamic produces shame in the recipient at every verse — so the term STAYS in M07 with a cross-register flag to M06, not a transfer. On the M07 v1→v2 revision, 8 of 10 original transfers moved to STAYS; only 2 (`H2616B cha.sad`, `H2617B che.sed` — the steadfast-love sense of *hesed*, 164 verses with zero shame relational content) were confirmed as transfers (accidental placement).

**How to apply:**

1. In Phase 3 the AI works through each candidate-TRANSFER term **verse by verse**, not at corpus-summary level.
2. For each verse, the test is: *does this verse evidence any relationship with or impact on the SOURCE cluster's characteristic?* "Relationship" is broad — direct impact, structural opposite, instrument-of, produced-by, response-to, protective-against. The Pass A meaning is the input; the AI reads it for any M{NN}-relational content.
3. If **any** verse in the corpus evidences a source-cluster relationship, the verdict is **STAYS** with a **cross-register flag** in the rationale naming the term's primary register destination (e.g. "Primary register is M06 contempt; M07 relationship: contempt is the active mechanism producing shame in recipient across all 11 verses. Flag for Phase 5/7."). The term stays in the cluster, the flag travels with it.
4. If **no** verse evidences any source-cluster relationship, the verdict is **TRANSFERS-TO-{cluster}** — accidental placement.
5. The cross-register flag is consumed at Phase 5 (sub-group formation) and Phase 7 (VCG design) — those phases can place the term in a sub-group/VCG that names the cross-register relationship, or use the flag to inform cross-cluster relationship findings at Phase 9 T6 prompts.
6. The corpus-primary-register check is no longer sufficient evidence for a TRANSFERS verdict — too aggressive; loses analytically-significant cross-cluster relationships.

This rule should be embedded in the v2_6 cluster instruction §6 (Phase 3 — Cluster constitution debate) and surfaced explicitly in every future Phase 3 brief. Auto-propagation: future briefs reference §6 of the active instruction; updating the instruction propagates the discipline to all subsequent briefs.

Related: [[feedback_cross_cluster_co_occurrence]] (earlier, narrower expression — combined-meaning observation pattern); [[feedback_findings_marginal_value]] (registry-level findings are shotgun; need term/verse-level grounding).
