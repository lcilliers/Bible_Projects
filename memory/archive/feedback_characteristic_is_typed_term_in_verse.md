---
name: feedback_characteristic_is_typed_term_in_verse
description: GOVERNING redefinition (2026-06-09). "Characteristic" no longer means the cluster — it means the TERM(S) IN THE VERSE in the context of the term's TYPE (type derived from lexical meaning). So catalogue/tier questions are asked at the typed-term-in-verse grain. L2 output = the TIER FINDINGS per term per verse (lexically-answerable tiers), mechanical-first + API where needed. A multi-term verse is completed in ONE read: tier findings for ALL in-scope terms, each saved to its own cluster; the process augments existing cluster tier-findings AND corrects them as it goes.
metadata:
  type: feedback
---

**Researcher refinements (2026-06-09), building on [[feedback_ontology_typed_relationships]].**

**1. "Characteristic" redefined = the typed term-in-verse.** Not the cluster. It means **the term(s) within
the context of the verse, in the context of the term's TYPE** (status/action/quality — derived from the
lexical meaning, [[project_p2_l2_decision_architecture]]). So the catalogue's tier questions (T0–T7), which
were written at the cluster/characteristic level, are now asked at the **typed-term-in-verse** grain. This
**resolves the L2-vs-catalogue grain mismatch** — L2's verse-level finding now matches the question grain.

**2. L2 output = the TIER FINDINGS per term, per verse** — not just "lexical meaning," but the
lexically-answerable tier findings *derived from* the lexical meaning + type. Mechanical first (STEP
sense-branch via morph); **API call only where the mechanical doesn't settle it.** Still **not cross-term**
(the relationships between terms are the layer above).

**3. A multi-term verse is completed in ONE read.** If the entry term co-occurs with other in-scope terms in
the same verse, the verse analysis **completes the tier findings for ALL the terms in the verse**; the output
is **the tier findings for every term, saved to each term's own cluster** (one read → many clusters
populated). Implements verse-coverage / no-double-work ([[feedback_l1_l2_is_multi_angle_report_then_synthesise]]).

**4. Augment + correct.** The process **augments** the tier findings that already exist for the clusters and
does **corrective work at the same time** — later verse-reads refine/fix earlier findings. So a cluster's
tier-finding picture accumulates and self-corrects through verse coverage.

**Coverage consequence (updates `wa-l2-findings-catalogue-coverage-v1-20260609.md`):** because the grain now
matches, the **identification tiers move to DIRECT per-verse**: T7.1 (lexical), T1.2 (kind = type), T1.4
(modes = morph stem), **T2 (constitutional location — does this term name a locus here)**, **T3 (faculties —
which faculty this term engages here)**, T1.3 (boundary). The **dynamic / cross-term / theological tiers stay
in the layer above**: T1.5–1.7 (response/effect/conditions), T4 (interfaces), T5 (transformation), **T6
(relationships = the cross-term tier)**, T0 (theology). Within T2/T3 the *identify* sub-question is DIRECT;
the *effect/what-it-reveals* sub-question is still synthesis.
