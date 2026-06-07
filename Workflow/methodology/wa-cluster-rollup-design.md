# The Roll-Up — verse relevance to cluster (data-flow & lifecycle design)

> **Living document · Doc version: 3 · 2026-06-07 · DRAFT for review.**
> *(v3: reworked to incorporate the **A1 verse-meaning work** of 2026-06-07 — corroboration becomes the
> generation principle; the verse level is now **mechanical STEP-sense application**, not AI
> meaning-derivation. **Only the bottom is consolidated:** old Phase 1 (relevance + UT-verse classification +
> similarity) **plus** the new A1 focused-meaning step become a single **L1**. The **upper levels stay as
> distinct roll-up rungs** — forming VCGs, deriving meaning, VCG-emergent, sub-group/characteristic, cluster,
> findings are each their own stage, as v2 had them. Old→new map in §0.)*
> Each level follows one uniform pattern — **Needs · Does · Updates · Output→next** (+ a mop-up gate), so the
> handoff chains rung to rung (`Output→next`(Lₙ) = `Needs`(Lₙ₊₁)). Governed by
> `wa-verse-analysis-methodology.md`, `wa-cluster-phase-reshape-v3_1-proposal.md`,
> **`wa-phase1-mechanical-meaning-reframe-v1-20260607.md`**, and the memory set. Audited by the per-level
> compliance check — `wa-cluster-audit-design-v1-20260607.md` (open item A2).
>
> **Evidence base for v3 (all 2026-06-07, `research/investigations/`):**
> `wa-a1-corroboration-m01-results-and-method-v1` · `wa-step-morphology-sense-disambiguation-v1` ·
> `wa-t2-relevance-surface-v1`.

---

## 0. The spine — what rolls up into what

```text
L1 Verse establishment (= old Phase 1 + A1 mechanical meaning)
   relevance · UT-verse classification · STEP-sense applied · keywords · corroboration-by-construction
        │  (one verse)
        ▼
L2 VCG formation + meaning derivation     (verses → VCG; residue read together; sense-in-context)
        │
        ▼
L3 VCG-emergent observation               (verses → VCG: what the collection jointly says)
        │
        ▼
L4 Sub-group + CHARACTERISTIC-emergent     (VCGs → sub-group; the characteristic emerges)
        │
        ▼
L5 Cluster-emergent                        (sub-groups → cluster)
        │
        ▼
L6 Findings + pointer adoption             (tier Q&A; cite; close)
        │
        ▼
L7 Whole-study synthesis                   (clusters → study; cross-cluster groupings)
```

The **unit of work** rises one rung at a time: verse → VCG → sub-group → cluster → study. **Meaning now
enters at L1 mechanically** (the STEP sense, applied) and is only *deepened* at L2 for the residue the
lexicon can't settle. Structure (characteristics) **emerges** at L4/L5; it is not pre-designed.

**Old→new level map (v2 → v3):** old L1 relevance + old L2 similarity + the *mechanical* part of old L3 →
**new L1** *(the only consolidation)*; old L3 VCG+meaning (advanced part) → **L2**; old L4 VCG-emergent →
**L3**; old L5 sub-group/char → **L4**; old L6 cluster → **L5**; old L7 findings → **L6**; the
previously-missing whole-study level (open item B1) → **new L7**.

---

## The five governing disciplines (apply at every level)

1. **Meaning is STEP-anchored by construction (NEW — the A1 principle).** A verse's meaning is *built from*
   the term's STEP sense-set, so it **cannot diverge** from the lexicon. Corroboration is not a downstream
   audit — it is how the meaning is generated. Interpretation is spent only where the lexicon runs out
   (within-stem multi-sense, metaphor, novel combination). *Cure for "cold per-verse AI bias."*
2. **No overlap — one home per statement.** Every analytical statement is placed at the **level where it
   first becomes true** and is **not restated** elsewhere. Lower levels feed upper; upper do not duplicate
   lower. *Cure for the old "general observation" drift.*
3. **Mop-up — every member consumed.** At each rung, **every object below is accounted for**. The
   **aggregate question** forces all members into view; a **gate** enforces zero left behind.
4. **No orphans — every object reaches a home.** In-scope → its level. Out-of-scope is *named and linked*,
   never dropped: external/physical pole → **cross-reference**; no-inner-being → **set-aside** (still feeds
   the term's semantic record); non-evidenced pointer → **set-aside with reason**; parked **T2** terms →
   surfaced to a candidate cluster (`wa-t2-relevance-surface-v1`).
5. **Refinement is forward enrichment, not silent rework.** Lower objects are **enriched** as understanding
   rises — additive, traceable. A **material change** **re-opens** the affected level
   (`feedback_verse_change_revalidation`); identity-preserving enrichment does not.

---

## Per-level — the uniform pattern

**Every rung follows the same four-part pattern, plus a gate:**

- **Needs** — what it *consumes* (the rung below's **Output→next**, plus reference / aux data).
- **Does** — what it *does* (the process).
- **Updates** — what it *writes* (tables/fields: **C** create · **E** enrich · **U** firm · **X** dispose).
- **Output→next** — what the *next rung consumes* (the roll-up handoff). **By construction,
  `Output→next`(Lₙ) = `Needs`(Lₙ₊₁).**
- **Gate (mop-up)** — what must be true before rolling up: nothing of the level below left unconsumed.

---

### L1 · Verse establishment = old Phase 1 + A1 mechanical meaning *(the audited "L1")*
**Replaces the old Phase 1 in full** — it **retains every existing Phase-1 verse step** (relevance, the
**UT-verse classification**, the related-pass, similarity/keyword grouping) **and adds** the A1 mechanical
STEP-sense meaning. No free AI meaning-derivation. *(The exact Phase-1 step inventory — incl. UT — is carried
verbatim from the current Phase-1 / Verse-Context instruction when v3 is encapsulated.)*

- **Needs:** `verse_context` (one row per span) + `wa_verse_records` (text, span, context, **STEP
  morphology**) + the term's **STEP sense-set** (`mti_terms.gloss` + `wa_term_inventory.step_search_gloss`,
  `.short_def_mounce`, `.meaning` + parsed `wa_meaning_sense`). *(For a receiving cluster: surfaced T2
  candidates.)*
- **Does:**
  1. **Phase-1 verse classification (retained):** relevance (inner-being-relevant vs set-aside:
     `no_inner_being | physical_only | spatial_only | unclear`) · the **UT-verse classification** · the
     related-pass (`is_related`) · the existing light similarity/keyword grouping. *Light touch.*
  2. **Attach (A1):** the term's STEP **sense-set (envelope) + pole map + STEP-capture keywords**.
  3. **Stem-narrow (A1):** verse **morphology → binyan/stem** narrows the sense-set to the stem's branch
     (Qal/Niphal/Piel → its BDB sub-senses) — free disambiguation (`wa-step-morphology-…-v1`).
  4. **Assign / Select (A1):** one sense remains → **assign** (mechanical, CC). Within-stem multi-sense →
     **select** the listed sense (+ pole), bounded light-analytic choice. Unsettled (metaphor / novel) →
     **flag residue** for L2.
- **Updates:** `verse_context` **C/U** — `is_relevant`, `set_aside_reason`, UT-class/`is_related` (retained);
  `step_meaning_applied` + `sense_id`, `sense_multiplicity`, `step_envelope_note`, `pole`, `keywords`
  (STEP-capture), `residue_flag` (NEW); `analysis_note` **preserved** (never overwritten). `wa_verse_records`
  **C** — `morph_code`/`stem` (at extraction). `wa_meaning_sense.stem_label`/`is_stem_label` **populated**.
- **Output→next:** every relevant span = a **STEP-anchored, corroborated-by-construction meaning** + selected
  sense + pole + STEP-capture keywords, with the **residue flagged**. *(→ L2 consumes the residue + the
  VCG-candidate set.)*
- **Gate:** no NULL `is_relevant`; every relevant span has `step_meaning_applied` + `keywords`; set-asides
  keep `set_aside_reason` (still feed the semantic record). **No `DIVERGENT` can arise here** (meaning *is*
  the STEP sense; M01: 949/949 corroborated, 0 divergent) — DIVERGENT can only surface at L2.

### L2 · VCG formation + meaning derivation  (verses → VCG)
- **Needs:** L1's **Output→next** — the verse establishments (sense, keywords, residue flags) — plus the
  **residue** verses' actual texts, spans tagged **T1 / T2 / FLAG**, the **term corpus**, surfaced pointers.
- **Does:** read the **residue / VCG-candidate verses together**; apply the verse-meaning discipline —
  span-focal Seven Principles · span **influence-test** · surroundings (from/to) · **clarify-by-corpus** ·
  3-pole scope · **open questions**. Form/refine **VCGs** by *sense-in-context*; designate **anchors**; derive
  the **rich contextual meaning**.
- **Updates:** `verse_context_group` **C** (`group_code`, `context_description`); `verse_context` **U** —
  `group_id`, `is_anchor`, `analysis_note` (**rich, VCG-layer** — distinct from L1's `step_meaning_applied`),
  `keywords` **E** (residue); scope-pole **cross-references**; **open questions** 〔home E7〕; pointers
  **surfaced (R)**.
- **Output→next:** the **formed VCGs** — each with its members, anchor(s) and rich meanings. *(→ L3 consumes
  each VCG + its verses.)*
- **Gate:** every relevant verse lands in exactly one VCG; every VCG has ≥1 anchor; external/physical-pole
  verses **cross-referenced**, not housed as inner.

### L3 · VCG-emergent observation  (verses → VCG)
- **Needs:** L2's **Output→next** — each VCG + its verses' L2 meanings.
- **Does:** the **aggregate question** — *what does this collection jointly say about the VCG that no single
  verse captures?*
- **Updates:** `verse_context_group.context_description` **E** — and/or `cluster_observation` (VCG-em level)
  **C** 〔E6: needs a `group_id` anchor on `cluster_observation`〕.
- **Output→next:** each VCG's **emergent meaning** (more than the sum of its verses). *(→ L4 consumes the
  VCGs' emergent meanings within a sub-group.)*
- **Gate:** every VCG has an emergent observation; **no-overlap** — the VCG-level statement is not duplicated
  onto the individual verses.

### L4 · Sub-group + CHARACTERISTIC-emergent  (VCGs → sub-group)
- **Needs:** L3's **Output→next** — the sub-group's VCGs + their emergent meanings; `mti_term_subgroup`
  (placements).
- **Does:** the **aggregate question** — *what do these VCGs jointly say about the sub-group — how do its
  dimensions operate together?* The answer **is the characteristic** — it **emerges here**.
- **Updates:** `cluster_subgroup.core_description` **U**; **`characteristic`** (`short_name`, `definition`)
  **C/E**; **`characteristic_subgroup`** **C**; `cluster_observation` (sub-group level) **C**.
- **Output→next:** the sub-group's **emergent meaning + its characteristic** (named, defined). *(→ L5
  consumes the sub-groups + characteristics.)*
- **Gate:** every VCG of the sub-group in view; every non-BOUNDARY sub-group maps to a characteristic;
  characteristic-level truth lives here, **not** restated on each VCG (no-overlap).

### L5 · Cluster-emergent  (sub-groups → cluster)
- **Needs:** L4's **Output→next** — the cluster's sub-groups + characteristics.
- **Does:** the **aggregate question** — *what do these sub-groups jointly say about the cluster — how do
  they operate together?*
- **Updates:** `cluster_observation` (cluster level) **C**; `cluster.description` / `.char_structure` **U**.
- **Output→next:** the cluster's **emergent account + characteristic structure**. *(→ L6 consumes these +
  the VCGs + pointers to form findings.)*
- **Gate:** every sub-group accounted for in the cluster account.

### L6 · Findings + pointer adoption  (the output layer)
- **Needs:** L5's **Output→next** — the cluster account + characteristics — plus the VCGs, surfaced
  pointers, and the L2–L5 meanings/observations.
- **Does:** answer the **tier questions** per sub-group (silence valid); **validate + adopt** surfaced
  pointers; **cite** the evidence (anchors/verses).
- **Updates:** **`cluster_finding`** **C** (`characteristic_id`, `cluster_subgroup_id`, `vcg_scope`,
  `obs_id`); **`finding_citation`** **C**; `wa_session_research_flags.resolved` **U** + cross-ref; reciprocal
  findings for influencing multi-T1 siblings.
- **Output→next:** the cluster's **evidenced findings + characteristics + reciprocal seeds**. *(→ L7
  consumes all clusters' findings.)*
- **Gate:** every surfaced pointer resolved; every characteristic has findings; every anchor verse cited.

### L7 · Whole-study synthesis  (clusters → study)  *(NEW — resolves open item B1)*
- **Needs:** all clusters' L6 **Output→next** — findings + characteristics; reciprocal/cross-cluster
  findings; surfaced **T2** candidates.
- **Does:** clusters **dissolve into cross-cluster groupings** (foundations §d); reciprocal findings
  reconcile; cross-cluster characteristics form; **interdependent clusters finalise together**.
- **Updates:** cross-cluster grouping/finding structures **C** 〔schema TBD〕.
- **Output→next:** the **whole-study account** — inner-life vocabulary, structure, relationships → products
  (F2). *(Terminal rung.)*
- **Gate / status:** **the most open level** — cross-cluster ordering/dependency unspecified (B2/B3).

---

## Auxiliary-table lifecycle matrix

Legend: **C** create · **E** enrich · **U** update/firm · **R** reference · **X** dispose · — none.

| Table | L1 verse | L2 VCG+mean | L3 VCG-em | L4 subgrp/char | L5 cluster | L6 findings | L7 study |
|---|---|---|---|---|---|---|---|
| `verse_context` (is_relevant, set_aside, UT) | **C/U** | R | R | R | R | R | R |
| `verse_context` step fields (`step_meaning_applied`/`sense_id`/`pole`/`stem`) NEW | **C** | R | R | R | R | R | R |
| `verse_context.keywords` | **C** (STEP-capture) | **E** (rich) | R | R | — | R | — |
| `verse_context.analysis_note` (AI meaning — dual) | **R** (preserved) | **C** (rich) | R | R | R | R | R |
| `verse_context.is_anchor` | — | **C** | R | R | — | R (cited) | R |
| `verse_context.group_id` | — | **C** | R | R | — | R | R |
| `wa_verse_records.morph_code`/`stem` NEW | **C** | R | — | — | — | — | — |
| `wa_meaning_sense.stem_label` (populate) | **C** | R | — | — | — | — | — |
| `verse_context_group` (VCG) | — | **C** | **E** (context_desc) | R | R | R | R |
| `cluster_subgroup` | R | R | R | **U** | R | R | R |
| `characteristic` / `characteristic_subgroup` | — | — | — | **C/E** (emerges) | U | R | R |
| `cluster_observation` | — | — | **C** (VCG-em) | **C** (subgrp) | **C** (cluster) | R/U | R |
| `cluster.char_structure` / `.description` | — | — | — | — | **U** | R | R |
| `mti_terms` (gloss/`anchor_note`) | **R** (sense-set) | R | — | — | — | R | R |
| `wa_session_research_flags` (pointers) | — | **surface (R)** | — | — | — | **U** (adopt) | R |
| `cluster_finding` / `finding_citation` | — | — | — | — | — | **C** | R |

---

## The cross-cutting refinement threads (the ones to watch)

- **Meaning, two layers (NEW).** L1 holds the **terse STEP-applied meaning** (`step_meaning_applied`,
  corroborated by construction); L2 holds the **rich contextual reading** (`analysis_note`, AI). **Both
  carried — dual meaning, never overwrite.** Existing M01 `analysis_note`s are the L2 layer produced early;
  under v3 they are re-homed as VCG-layer.
- **Keywords — STEP-capture, then enriched.** L1 emits keywords as a **brief capture of the STEP meaning**
  (sense tokens + selected sense + pole) — traceable, not interpretive; likely **dissolves the parked
  keyword-bias problem** (`project_keyword_analytics_revision_parked`). L2 enriches the residue set.
- **Morphology → sense (NEW).** Per-verse stem selects the BDB sense-branch — free mechanical disambiguation
  captured at L1.
- **Gloss compilation.** At L1 the term's gloss + structured senses compiled into the sense-set; at L2 every
  T1 sibling's gloss feeds the rich reading and the term's semantic record (incl. set-asides).
- **Anchors → citations.** Designated at L2 (per VCG); become citations at L6 (`finding_citation`).
- **Emerging characteristics.** Created at L4 from the aggregate answer; refined at L5.
- **Pointers/flags.** Surfaced at L2, adopted/resolved at L6.
- **T2 surfacing (NEW).** Parked T2 terms scored against cluster sense-envelopes → candidate homes; enter
  normal analysis as candidates (term-as-unit-of-movement), feeding L1 of the receiving cluster.
- **Emergent observations.** Recorded **level-anchored** in `cluster_observation` at L3/L4/L5.

---

## Disposal / supersession (closing the loop, avoiding orphans)

- **Soft-delete only** (`delete_flagged=1`) — nothing physically removed.
- **Superseded VCGs / sub-groups / characteristics** are soft-deleted; their members **re-homed** in the
  same pass (mop-up) — never dangling.
- **Stale findings:** a material verse-meaning change **re-opens** the affected VCG/sub-group and stales its
  findings; identity-preserving enrichment does not.
- **Set-aside & external/physical-pole** material is **retained and linked** — out of the inner-being
  analysis, never out of the data.

---

## Open items (for the review)

### Resolved / incorporated in v3
- **A1 · Verse-meaning corroboration — RESOLVED.** Corroboration is now the **generation principle** (L1
  meaning STEP-anchored by construction). Validated on M01 (949/949 corroborate, 0 divergent). See
  `wa-a1-corroboration-m01-…-v1`.
- **L8 gap (B1) — addressed** by adding **L7 whole-study synthesis** (mechanics still open: B2/B3).

### A. Soundness & validation
- **A2 · The audit — DESIGNED.** A per-level **compliance check** (PASS/FAIL vs the v3 standard), *not* a
  remedial program; remediation = pointed intervention or re-run of the v3 instruction. Two check classes per
  level: **(a) field-completeness**, **(b) instruction-adherence spot checks**. **L1 check spec complete.**
  `wa-cluster-audit-design-v1-20260607.md`.
- **A3 · Researcher review / sign-off gates** — human stop-points per level (findings are drafts; a cluster
  is done only by non-mechanical sign-off).
- **A4 · Finding lifecycle (draft → reviewed → confirmed)** — the iterative sift isn't yet a roll-up step.

### B. Cross-cluster & whole-study
- **B2 · Interdependent clusters finalise together** (now L7). · **B3 · Reciprocal-finding loop consumer.**

### C. The term-corpus tension
- **C1 · Clarify-by-corpus needs verses the roll-up unit doesn't hold** (eased by L1 stem-narrow + sense-set).
- **C2 · A reuse / consistency store** for multi-T1 "reuse if seen before".

### D. Process, ownership & cost
- **D1 · Owner per level** — L1 mechanical = CC + light AI select; L2 advanced = AI chat; findings = CC.
- **D2 · Cost model at scale.** · **D3 · Complexity triage as routing** (set-aside stops at L1; single-sense
  done at L1; multi-T1 to L2).

### E. Bootstrapping, re-runs & the data model
- **E1 · L1 population for *fresh* clusters.** · **E2 · Re-run / idempotency.** · **E3 · What is an *anchor*
  now.** · **E4 · Retire/clarify legacy `verse_context` fields** (`is_related`, `vertical_pass_flag`, UT,
  `is_anchor`) — reconcile with the retained Phase-1 steps. · **E5 · BOUNDARY.** · **E6 · VCG-observation
  home.** · **E7 · Open-questions home.** · **E8 · Phase-A similarity** (now STEP-capture keywords —
  largely resolved). · **E9 · Field-name reconciliations** (`analysis_note`/L2 vs `step_meaning_applied`/L1;
  `ut_class`).

### NEW decisions from the A1 work (R1–R7 — `wa-phase1-mechanical-meaning-reframe-v1`)
- **R1** confirm the mechanical-L1 reframe · **R2** single/multi-sense detector · **R3** dual-meaning field
  layout · **R4** keyword STEP-capture spec · **R5** treatment of existing M01 notes · **R6** pole
  mechanical-vs-judgement · **R7** capture morphology + parse stem branches.

### F. Adjacent layers
- **F1 · Science layer** (light-touch, after L5). · **F2 · Findings → prose / publication** (downstream L6).
