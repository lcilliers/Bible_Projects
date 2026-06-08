---
name: project_p2_l2_decision_architecture
description: P2/L2 design settled on M01 evidence (2026-06-08). L1 = verse-aware TYPING + relevance gate (settles only ~4% clean-single); L2 = decision MODULES not disjoint passes. 6 scenarios (S0 set-aside · S1 clean · S2 sense-resolution · S3 same-cluster-pair · S4 qualifier-route · S5 cross-cluster). 74% of verses are COMPOUND (>1 decision) → type→modules→synthesise. STEP morph backfill (morph 0% populated) is the prerequisite for S2 (84% of verses).
metadata:
  type: project
---

**Settled by M01 evidence, 2026-06-08** (`scripts/_assess_p2_verse_scenarios.py`; design
`research/investigations/wa-p2-l2-decision-design-v1-20260608.md`). The qualifier "pull-through" lives in
**L2** (researcher confirmed).

**L1 = verse-aware TYPING, not meaning-stamp.** Per occurrence: apply STEP sense, relevance-in-context gate
(set aside Song-6 class), single/multi-sense flag, and assign a **type-vector** (counts of in-cluster /
other-cluster / qualifier occurrences). L1 settles only the **clean-single** case mechanically — on M01 that
is **~4% of verses**. The first L1 build failed because it stamped meaning on the other 96% (see
[[feedback_l1_must_be_verse_aware]]).

**Scenario taxonomy** (a verse can trigger several — they COMPOSE):
- S0 set-aside/relevance · S1 clean single (pure L1) · **S2 sense-resolution** (which STEP top-level sense) ·
  **S3 same-cluster multi** (sibling-span *pair* vs distinct) · **S4 qualifier+char** (route the qualifier
  *occurrence* in — see [[feedback_qualifier_routes_per_verse_occurrence]]) · **S5 cross-cluster** (reciprocal
  finding each + multi-belong) · S6 qualifier-orphan (bookkeeping).
- The researcher's named three = S4/S3/S5. Evidence ADDS S2 + S0 as decisions.

**M01 distribution (930 verses):** S1 4% · S0 8% · S2 84% · S3 10% · S4 45% · S5 64% · **COMPOUND 74%**.

**Architecture (the key call):** because **74% of verses trigger >1 decision**, L2 is **NOT three disjoint
passes** over separate verse-sets. It is **type → apply each applicable MODULE (M-sense/M-pair/M-qual/M-cross)
→ SYNTHESISE one combined verse contribution + spawned routes/findings**. The researcher's "split into three"
is honoured at the *module* level (distinct logic/writes), co-resident in one verse-pass.

**STEP-sufficiency is asymmetric:** `span_strong_match` = **100%** populated → S3 pairing + S4
qualifier-attach are STEP-decidable now. `morph_code`/`stem` = **0%** populated (M55 added columns, no
backfill) → **S2 sense-resolution (84% of verses) is NOT STEP-automated until a STEP morph backfill runs** —
the single highest-leverage data task before any L2 build. S5 cross-cluster *relation* is not in STEP → needs
a read. Refines [[project_a1_resolved_rollup_v3_audit_design]].

**Researcher decisions (2026-06-08):** §6.1 architecture (type→modules→synthesise), §6.2 scenario set
(S0+S2 added), §6.3 morph-backfill-first — **all AGREED**. §6.4 (is `span_strong_match` equality a sufficient
signal for qualifier-enhances-this-char, or must M-qual always read?) — **UNSURE, to be tested**; fold the
span-share measurement into the morph-backfill prototype. **Next prototype = STEP morph backfill** (read STEP
per verse → populate `wa_verse_records.morph_code`/`stem`, validate on M01), carrying the §6.4 span-attach
measurement. P1 keyword rebuild can run in parallel (independent).
