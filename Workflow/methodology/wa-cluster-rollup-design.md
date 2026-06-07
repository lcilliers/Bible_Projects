# The Roll-Up — verse → cluster → study (the V3_2 base design)

> **Living document · Doc version: 4 — V3_2 BASE (clarity rewrite) · 2026-06-07.**
> *The authoritative design the V3_2 instruction is built from.* Sharpened from v3 (resequencing + A1/A2/A3/A4
> + open-item resolution + the M01/M02 L1 prototype). **This is a joint document:** every genuine doubt is
> tagged **〔CONSULT〕** inline and collected in §12 — those are the researcher's calls, not CC's.
>
> Each level follows one uniform pattern — **Needs · Does · Updates · Output→next · Gate** — so the handoff
> chains rung to rung (`Output→next`(Lₙ) = `Needs`(Lₙ₊₁)). Governed by `wa-verse-analysis-methodology.md`,
> `wa-phase1-mechanical-meaning-reframe-v1-20260607.md`, and the memory set. Audited by the per-level
> compliance check `wa-cluster-audit-design-v1-20260607.md` (A2). Empirical base (all 2026-06-07,
> `research/investigations/`): `wa-a1-corroboration-m01-…`, `wa-step-morphology-…`, `wa-t2-relevance-…`,
> **`wa-l1-prototype-findings-and-r-decisions-v1`** (M01+M02 L1 prototype).

---

## 1. The spine

```text
L1  Verse establishment (MECHANICAL = old Phase 1 + A1 STEP-meaning)     [per verse]
      │   → A3 gate: run audit; if clean & no residue → researcher review
      ▼
L2  Sub-group formation (PROVISIONAL partition of the cluster)           [cluster → sub-groups]
      │
      ▼   ┌──────────────── iterate PER SUB-GROUP ────────────────┐
L3    VCG formation + DEEP verse reading                            [verses → VCGs]
      ▼
L4    VCG-emergent observation                                      [verses → one VCG]
      ▼
L5    Sub-group-emergent observation + CHARACTERISTIC + FINDINGS    [VCGs → sub-group]
      │   → A4 gate: sub-group findings submitted DRAFT for review
      └───────────────────── next sub-group ─────────────────────┘
      ▼   (after all sub-groups)
L6  Cross-sub-group observation + ORPHAN-CHECK closure               [sub-groups → cluster]
      ▼
L7  Cluster synthesis                                                [cluster]
      │   → A4 gate: all findings submitted as a group → CONFIRMED (cluster sign-off)
      ▼
L8a Cross-cluster finding generation (at each cluster's close)       [cluster → other clusters]
      ▼   (once ALL clusters complete)
L8b Study-level cross-cluster reconciliation + SCIENCE layer         [clusters → study]
```

**Unit of work rises one rung at a time:** verse → (provisional sub-group) → VCG → sub-group → cluster →
study. Meaning enters **mechanically at L1**; the **deep read is organised by sub-group**, iterating L3–L5;
**characteristics emerge at L5** (the L2 partition is provisional and is refined by the read).

**Old→new map (v2):** old L1 relevance + L2 similarity + mechanical-L3 → **L1**; sub-group formation moved
*before* the read → **L2**; old L3 → **L3**; old L4 → **L4**; old L5 → **L5**; old L6 → **L6 + L7**;
whole-study → **L8a/L8b**.

---

## 2. Governing disciplines (apply at every level)

1. **Meaning is STEP-anchored by construction.** A verse's meaning is *built from* the term's STEP sense-set,
   so it **cannot diverge** from the lexicon. Corroboration is generation, not a later audit. Interpretation
   is spent only where the lexicon runs out.
2. **Provisional structure, emergent characteristic.** L2 sub-groups are a *provisional* partition (from L1's
   light signal) that *organises* the read — not a pre-imposed characteristic. The **characteristic emerges**
   at L5; the **boundary is refinable** through L3–L5.
3. **No overlap — one home, findings level-anchored.** Every statement lives at the level where it *first
   becomes true* and is not restated. Findings are submitted at the right level (most L5; some L6/L7-only).
4. **Mop-up — every member consumed.** At each rung every object below is accounted for; the aggregate
   question forces all members into view; a gate enforces zero left behind. **L6 is the cluster-wide closing
   orphan-check.**
5. **No orphans — every object reaches a home.** In-scope → its level. Out-of-scope is *named and linked*:
   external/physical pole → cross-reference; no-inner-being → set-aside (still feeds the term's semantic
   record); non-evidenced pointer → set-aside with reason; parked **T2** term → surfaced to a candidate
   cluster.
6. **Refinement is forward enrichment; prior findings are inputs.** Lower objects are enriched additively.
   **Existing findings from a previous analysis are pulled in for evaluation + refinement** (not discarded).
   A **material change re-opens** the affected level; identity-preserving enrichment does not.

---

## 3. Per-level specification

### L1 · Verse establishment (mechanical)
Replaces old Phase 1 **in full** — retains every Phase-1 step (relevance · **UT-verse classification** ·
related-pass · light similarity/keyword grouping) and **adds** the A1 mechanical STEP-meaning. **No free AI
meaning-derivation.** Owner: **CC** (with a light AI select sub-step). Validated on M01+M02 (the prototype).

- **Needs:** `verse_context` spans · `wa_verse_records` (text, span, context, **STEP morphology**) · the
  term's **STEP sense-set** (`mti_terms.gloss` + `wa_term_inventory` + parsed `wa_meaning_sense`).
- **Does:**
  1. **Phase-1 classification** — relevance (relevant vs set-aside: `no_inner_being | physical_only |
     spatial_only | unclear`) · **UT classification** · related-pass · light similarity/keywords.
  2. **Attach** the STEP **sense-set + pole map + STEP-capture keywords**.
  3. **Stem-narrow** — the verse's morphology (binyan/stem) narrows the sense-set to the stem's branch.
     *(Hebrew only; Greek morphology is not sense-branching — Greek multi-sense stays for select/L2.)*
  4. **Assign / select / flag** — one sense left → **assign**; within-stem multi-sense → **select** (light AI,
     candidates given); metaphor / novel-combination → **flag residue** for L2.
     **〔CONSULT〕** the L1-select vs L2-residue boundary: the prototype shows within-stem ambiguity (Qal
     `ya.re` = fear / awe / reverence) is **~80% of stem-conditioned verses** and often needs verse context.
     *Decision: does L1 do a light per-verse select on these, or defer them all to the L2 deep read?*
- **Updates:** `verse_context` **C/U** — `is_relevant`, `set_aside_reason`, UT-class / `is_related`,
  `step_meaning_applied` + `sense_id`, `sense_multiplicity`, `step_envelope_note`, `pole`,
  **`pole_is_metaphor`**, `keywords`, `residue_flag`; `analysis_note` **preserved** (dual meaning).
  `wa_verse_records.morph_code` / `stem` **C**; `wa_meaning_sense.stem_label` **populated**.
- **Output→next:** every relevant span = a **STEP-anchored, corroborated meaning** + sense + pole + keywords,
  residue flagged. *(→ L2.)*
- **Gate (+ A3):** no NULL `is_relevant`; every relevant span has `step_meaning_applied` + `keywords`. Run
  the audit → **clean & no residue → researcher review → proceed**; **clean & residue → L2 proceeds**;
  **FAIL → remediation**. **No `DIVERGENT` can arise at L1** (meaning *is* the STEP sense; M01: 0 divergent).

### L2 · Sub-group formation (provisional)
- **Needs — PRE-L2 completeness (the whole cluster in focus):** every cluster element gathered — **terms ·
  verses · flags · pointers · existing VCGs · previous findings** (+ L1 establishments, similarity signal,
  term ontology). Nothing left out.
- **Does:** partition the relevant verses/terms into **provisional sub-groups** from the L1 similarity/keyword
  signal + term structure — a working container, *not* the final characteristic. Terms not yet placeable are
  marked **BOUNDARY** (undecided), deferred to resolve by end of sub-group processing (E5).
- **Updates:** `cluster_subgroup` **C** (provisional); `mti_term_subgroup` (placements); BOUNDARY marks.
- **Output→next:** the provisional partition — each sub-group a set of verses/terms to deep-read. *(→ L3.)*
- **Gate — post-L2 completeness:** every in-focus item is in a sub-group **OR** marked cluster-level **OR**
  marked BOUNDARY (or held for routing/set-aside). Nothing unaccounted.

### L3 · VCG formation + deep verse reading  *(per sub-group)*
- **Needs:** the sub-group's verses + L1 establishments + residue flags; spans **T1/T2/FLAG**; the **term
  corpus**; surfaced pointers; prior VCGs if re-running.
- **Does:** read the verses **deeply, together** — span-focal Seven Principles · influence-test ·
  clarify-by-corpus · 3-pole · open questions; form/refine **VCGs** by sense-in-context; derive the **rich
  contextual meaning** (the AI `analysis_note`); designate **anchors**. May **revise sub-group allocation,
  reroute, or set aside** (§4 dynamics).
- **Updates:** `verse_context_group` **C**; `verse_context` **U** — `group_id`, `is_anchor`, `analysis_note`
  (rich), `keywords` **E**; pole cross-references; reroute/set-aside flags; open questions (→ findings, E7).
- **Output→next:** the sub-group's formed VCGs (members, anchors, rich meanings). *(→ L4.)*
- **Gate:** every sub-group verse in exactly one VCG (or rerouted/set-aside); every VCG ≥1 anchor.

### L4 · VCG-emergent observation  *(per sub-group)*
- **Needs:** each VCG + its verses' L3 meanings.
- **Does:** the **aggregate question** — *what do this VCG's verses jointly say that no single verse captures?*
- **Updates:** the VCG-emergent observation at the **VCG-group level** (keyed to `verse_context_group`).
  **〔CONSULT〕 (E6)** *field choice: reuse `context_description`, or a new VCG-group observation field?* —
  **not** `cluster_observation` (which is cluster-level).
- **Output→next:** each VCG's emergent meaning. *(→ L5.)*
- **Gate:** every VCG has an emergent observation; **no-overlap** (not duplicated onto verses).

### L5 · Sub-group-emergent observation + characteristic + findings  *(per sub-group)*
- **Needs:** the sub-group's VCGs + L4 emergent meanings; **prior findings for this sub-group**; pointers
  routed here.
- **Does:** the **aggregate question** — *what do these VCGs jointly say about the sub-group?* The
  **characteristic emerges**. **Submit findings (most land here):** answer the **tier questions**
  **〔CONSULT〕** *(confirm the tier-question framework is retained as-is under V3_2)*; validate/adopt
  pointers; **evaluate + refine prior findings**; create findings, incl. **into other clusters** (§4-c). Firm
  / revise the sub-group (provisional → confirmed; may re-allocate).
- **Updates:** `cluster_subgroup.core_description` **U**; **`characteristic`** **C/E** (emerges);
  **`characteristic_subgroup`** **C**; `cluster_observation` (sub-group) **C**; **`cluster_finding`** **C**
  (most — with `finding_type`, scope anchor = cluster+sub-group, `finding_status`=**draft**) +
  **`finding_citation`** **C**; `wa_session_research_flags.resolved` **U**; prior findings `finding_status`
  **U** (refined); cross-cluster findings **C** (other clusters).
- **Output→next:** the sub-group's emergent meaning + **characteristic** + its **findings**. *(→ L6; and to
  other clusters where routed.)*
- **Gate (+ A4):** every VCG in view; characteristic assigned (or BOUNDARY); every pointer / prior-finding
  evaluated; **findings submitted as `draft` for researcher review → `reviewed` before the next sub-group.**
  **↻ next sub-group → L3.**

### L6 · Cross-sub-group observation + closure
- **Needs:** all sub-groups' L5 emergent meanings + characteristics + findings.
- **Does:** the **aggregate question** — *what do these sub-groups jointly say about the cluster?*
  (cluster-emergent). **Submit cross-sub-group findings** (true only across sub-groups); adopt remaining
  pointers; **run the orphan check**.
- **Updates:** `cluster_observation` (cluster) **C**; **`cluster_finding`** **C** (cross-sub-group);
  pointers `resolved` **U**.
- **Output→next:** the cluster-emergent account + cross-sub-group findings; a **clean (no-orphan) cluster**.
  *(→ L7.)*
- **Gate — closing completeness cross-check (all must hold):**
  1. **Citations cover all verses** — every verse cited in a finding, or set-aside / rerouted with reason.
  2. **Every finding has ≥1 anchor; every anchor used ≥1** (each `is_anchor` verse in ≥1 `finding_citation`).
  3. **No orphaned VCGs or sub-groups** — every VCG in a sub-group + observed; every sub-group has a
     characteristic + cluster-account home.
  4. **All BOUNDARY terms resolved (E5)** — placed / rerouted / set aside; the audit reveals any orphaned term.
  5. **Zero orphans overall** — every verse / flag / pointer / prior observation / prior finding accounted for.

### L7 · Cluster synthesis
- **Needs:** L6's cluster-emergent account + all findings + characteristics.
- **Does:** firm the cluster's account; **submit cluster-level-only findings** (`finding_type`=intra-cluster);
  consolidate the **characteristic structure**.
- **Updates:** `cluster.description` / `.char_structure` **U**; **`cluster_finding`** **C** (intra-cluster);
  `cluster.status` **U**.
- **Output→next:** the firmed cluster account. *(→ L8a.)*
- **Gate (+ A4 cluster confirmation):** cluster account complete; characteristic structure firmed; **all
  findings submitted as a group → `confirmed`** = the **cluster sign-off**.

### L8a · Cross-cluster finding generation  *(at each cluster's close)*
- **Needs:** all of *this* cluster's findings (L5/L6/L7).
- **Does:** **re-evaluate every finding** to confirm **every cross-cluster finding it should generate has
  been generated** (outbound completeness — reciprocal / dual-cluster findings into the other clusters).
- **Updates:** any missing cross-cluster `cluster_finding` **C** (into the other cluster).
- **Output→next:** the cluster's outbound cross-cluster findings — **and the cluster is now ready for
  publication input-folder generation** (F2).
- **Gate:** no finding implying a cross-cluster finding is left without one.

### L8b · Study-level cross-cluster reconciliation + science  *(once all clusters complete)*
- **Needs:** **all clusters'** cluster-level findings + characteristics + every L8a's cross-cluster findings.
- **Does:** a **single pass over all cluster-level findings** to **resolve additional cross-cluster findings
  / adjustments**; clusters **dissolve into cross-cluster groupings**; **interdependent clusters finalise
  together (B2)**. **The science layer is introduced here (F1)** — correlate with the per-cluster science
  extracts and **develop science-derived findings**. **〔CONSULT〕 (B3 / F1)** *the cross-cluster
  ordering/dependency mechanics and the science-correlation method are the most open part of the design.*
- **Updates:** cross-cluster grouping / finding structures **C**; finding adjustments **U**; science-derived
  findings **C** 〔schema TBD — §10〕.
- **Output→next:** the whole-study account → products (F2). *(Terminal.)*

---

## 4. The L2–L5 dynamics (what the per-sub-group read may do)

Because L2 sub-groups are provisional, L3–L5 is also where the cluster's **boundaries are tested**:

- **(a) revise sub-group allocation** — move a verse/term; split / merge a provisional sub-group as the
  characteristic clarifies.
- **(b) reroute to other clusters, or set aside** — the **term is the unit of movement** (carries its
  verses/VCGs). **Set-aside is layered:** verses at **L1**, BOUNDARY terms at **L2**, terms-to-other-clusters
  at **L3**.
- **(c) create findings into *other* clusters** — where a verse/term has meaning elsewhere, the finding is
  created **there** (reciprocal / dual-cluster).
- **(d) evaluate + refine prior findings** — re-assess existing findings (confirm / refine / set-aside
  non-evidenced), not regenerate.
- **(e) reuse vs re-create (C2 rule)** — re-deriving an existing item: **identical content → reuse**;
  **differs → (1) surface the *why* to the researcher**, then **(2) create new + soft-delete old**.

---

## 5. Sign-off gates & finding lifecycle (A3 + A4)

Findings are **drafts**; a cluster is done only by **non-mechanical sign-off**. The audit (A2) is the
**precondition** for sign-off, not a substitute. Lifecycle (`cluster_finding.finding_status`):
**draft → reviewed → confirmed**.

- **L1→L2 gate.** Audit → clean & no residue → researcher review → proceed; clean & residue → L2 proceeds;
  FAIL → remediation.
- **Sub-group gate (switching sub-groups is a gate).** End of each sub-group's L5: findings → **draft**,
  submitted for review → **reviewed**; the next sub-group starts only past this gate. Mid-cycle, **specific
  clarifications may be put to the researcher**.
- **Cluster confirmation gate.** After all sub-groups: **all findings submitted as a group → confirmed** =
  the cluster sign-off (with the L6 closure + L7 synthesis). Cross-cluster finalisation is **B2 at L8b**, not
  here.

---

## 6. Finding types, scope & the cluster-minimum rule

**Every finding belongs to at least a cluster.** Non-tier (observation) findings carry a **`finding_type`**
(the observation's scope) and a **scope anchor** (the object they belong to):

| `finding_type` | Observes across | Emerges at | Scope anchor |
|---|---|---|---|
| **tier** | a tier question | L5 | cluster + sub-group (+ VCG/verse) |
| **cross-VCG** | the VCGs of one sub-group | L5 | cluster + sub-group |
| **cross-sub-group** | the sub-groups of a cluster | L6 | cluster |
| **intra-cluster** | the cluster as a whole | L7 | cluster |
| **cross-cluster** | two or more clusters | L8 | ≥2 clusters |

*(VCG-emergent statements (L4) are recorded as VCG-level observations and roll into cross-VCG findings at L5.)*

**Rules:** (1) every finding has a `finding_type`; (2) every finding names its cluster (+ sub-group / VCG per
its type); (3) **no finding without a cluster**; (4) **every open question is a finding** flagged
**`needs_research`**.

---

## 7. Auxiliary-table lifecycle matrix

Legend: **C** create · **E** enrich · **U** firm · **R** reference · — none.

| Table | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 |
|---|---|---|---|---|---|---|---|---|
| `verse_context` (relevance, set_aside, UT, step fields) | **C/U** | R | **U** (reroute) | R | R | R | R | R |
| `verse_context.analysis_note` (AI, dual) | R (kept) | — | **C** (rich) | R | R | R | R | R |
| `verse_context.keywords` | **C** (STEP) | R | **E** | R | R | — | — | — |
| `wa_verse_records.morph`/`stem`; `wa_meaning_sense.stem_label` | **C** | — | R | — | — | — | — | — |
| `cluster_subgroup` | — | **C** (prov.) | U (revise) | — | **U** (firm) | R | R | R |
| `mti_term_subgroup` | — | **C** | U (reroute) | — | U | R | — | — |
| `verse_context_group` (VCG) | — | — | **C** | **E** (VCG-em) | R | R | R | R |
| `characteristic` / `characteristic_subgroup` | — | — | — | — | **C/E** | U | U | R |
| `cluster_observation` | — | — | — | — | **C** (subgrp) | **C** (cluster) | R | R |
| `cluster_finding` / `finding_citation` | — | — | — | — | **C** (most) | **C** | **C** | **C** (L8) |
| `wa_session_research_flags` (pointers) | — | — | surface (R) | — | **U** (adopt) | **U** | R | R |
| `cluster.description` / `.char_structure` / `.status` | — | — | — | — | — | — | **U** | R |

---

## 8. Cross-cutting threads

- **Meaning, two layers.** L1 = terse STEP-applied meaning (`step_meaning_applied`); L3 = rich contextual
  reading (`analysis_note`, AI). **Dual — never overwrite.** Existing M01 `analysis_note`s are the L3 layer
  produced early; re-homed.
- **Keywords — STEP-capture.** L1 emits sense-token keywords (traceable, not interpretive) — needs the
  **noise + homonym filters** (prototype §3); L3 enriches the residue.
- **Morphology → sense.** Per-verse stem selects the BDB branch at L1 — a **partial** resolver (settles
  ~14–22% incl. stem-conditioned pole/voice splits; ~80% within-stem residue stays L2). Hebrew only.
- **Pole.** Default **inner**; literal-physical + external lexicons assign those poles; **heat / tremble /
  melt flagged `pole_is_metaphor`** for judgement — *not* auto-assigned (prototype §4: M02 burning-anger =
  metaphor, not physical).
- **Findings — level-anchored + prior-as-inputs.** Submitted where they first become true; prior findings
  re-evaluated; cross-cluster findings created in the other cluster.
- **T2 surfacing.** Parked T2 terms scored against cluster sense-envelopes → candidate homes; enter as
  candidates feeding L1 of the receiving cluster.
- **Anchors → citations.** Designated at L3 (per VCG); the **only reference that survives into findings**
  (E3); become citations at L5/L6/L7.

---

## 9. Disposal / supersession · Ownership · Cost

- **Soft-delete only** (`delete_flagged=1`). Superseded VCGs / sub-groups / characteristics are soft-deleted;
  members **re-homed** in the same pass. A material verse-meaning change re-opens the affected level &
  **stales its findings**. Set-aside / external / physical-pole material is **retained and linked**.
- **Retire `vertical_pass_flag`** (legacy "vertical pass" experiment, VCB-031) — **〔CONSULT〕** confirm
  soft-retire. `is_related` + UT classification are **retained**.
- **Ownership (D1):** run by **CC with researcher input**, **referring select operations to AI** (API or
  chat — whichever is best). L1 mechanical = CC; L1-select + L3–L5 deep read = AI; findings write = CC;
  gates = researcher.
- **Cost (D2):** **costing for any API operation > \$2**; researcher monitors cumulative cost otherwise.

---

## 10. Schema-change catalogue (the V3_2 schema seed)

New / changed fields the design requires. **〔CONSULT〕** items are design decisions, not yet settled.

| Table | Field | Purpose | Status |
|---|---|---|---|
| `verse_context` | `step_meaning_applied` | the terse STEP-applied meaning (L1) | new **〔CONSULT R3/E9〕** new field vs re-home `analysis_note` |
| `verse_context` | `sense_id` | which listed STEP sub-sense the verse realises | new |
| `verse_context` | `sense_multiplicity` | single / multi indicator | new |
| `verse_context` | `step_envelope_note` | the full STEP sense-set, for further analysis | new |
| `verse_context` | `pole` | inner / external / physical | new |
| `verse_context` | `pole_is_metaphor` | flag heat/tremble/melt metaphor for judgement (R6) | new |
| `verse_context` | `keywords` | STEP-capture keywords (exists; re-purpose + filters) | change |
| `verse_context` | `residue_flag` | needs-advanced (within-stem / metaphor / novel) | new |
| `verse_context` | UT-class field | the retained UT classification | **〔CONSULT E9〕** identify the live field/representation |
| `verse_context` | `vertical_pass_flag` | legacy | **retire** |
| `wa_verse_records` | `morph_code` / `stem` | per-verse morphology (R7) | new |
| `wa_meaning_sense` | `stem_label` / `is_stem_label` | populate the stem→branch map (R7) | populate (cols exist) |
| `wa_meaning_sense` | homonym / biblical-sense filter | exclude `che.mah`-bottle, `ya.re`-shoot from the sense-set | new |
| `verse_context_group` | VCG-emergent observation home | the L4 observation (E6) | **〔CONSULT E6〕** `context_description` vs new field |
| `cluster_finding` | `finding_type` | tier / cross-VCG / cross-sub-group / intra-cluster / cross-cluster | new |
| `cluster_finding` | scope anchors | cluster (required) + sub-group / VCG | new/confirm |
| `cluster_finding` | `needs_research` | open-question findings (E7) | new |
| `cluster_finding` | `finding_status` | draft → reviewed → confirmed (A4) | confirm exists |
| (study layer) | cross-cluster grouping / finding structures | L8b | **〔CONSULT B3〕** schema TBD |

---

## 11. Decisions log (resolved)

- **A1** corroboration = generation principle (M01 949/949, 0 divergent). · **A2** audit designed. ·
  **A3** sign-off gates designed (L1→L2; sub-group; cluster). · **A4** finding lifecycle draft→reviewed→
  confirmed; findings typed + scope-anchored; ≥1 cluster.
- **B1** L8a/L8b added. · **B2** interdependent clusters finalise at L8b. · **Q2** L8a (within-cluster) /
  L8b (study-level).
- **B3** consume on Y's run, else at final L8b. · **C1** clarify-by-corpus = surface-to-researcher
  case-by-case. · **C2** reuse-if-identical else surface-why + new + soft-delete. · **D1/D2** CC-governed,
  refer to AI, cost API > \$2. · **D3** set-aside layered (L1/L2/L3).
- **E1** fresh clusters bootstrap from L1 groups (AI-chat fallback). · **E2** V3_2 re-runs respecting done
  work. · **E3** anchors survive into findings. · **E5** BOUNDARY = undecided terms, resolve by end of
  sub-groups. · **E6** VCG-emergent at VCG-group level. · **E7** open questions = `needs_research` findings.
  · **E8** similarity rolled into STEP.
- **R1–R7** resolved via the M01+M02 L1 prototype (R2 detector + homonym filter; R4 keywords + noise filter;
  R6 default-inner + `pole_is_metaphor`; R7 morph/stem partial resolver). · **F1** science at L8b. ·
  **F2** publication input folder after L8a.

---

## 12. Open questions for the researcher (the 〔CONSULT〕 collection)

1. **L1-select vs L2-residue boundary** (§3 L1) — does L1 do a light per-verse select on within-stem
   multi-sense (~80% of stem-conditioned verses), or defer them all to the L2 deep read?
2. **Dual-meaning field** (R3/E9, §10) — new `step_meaning_applied` field, or re-home `analysis_note`?
3. **UT field** (E9, §10) — identify the live field/representation for the UT classification.
4. **VCG-emergent observation home** (E6, §3 L4) — reuse `context_description` or a new VCG-group field?
5. **Tier-question framework** (§3 L5) — confirm it is retained as-is under V3_2.
6. **`pole_is_metaphor`** (R6, §8) — confirm the default-inner + metaphor-flag approach.
7. **`vertical_pass_flag` retirement** (E4, §9) — confirm soft-retire.
8. **L8b cross-cluster mechanics + science (B3 / F1)** (§3 L8b) — the ordering/dependency and
   science-correlation method (the most open part).
9. **R5** (§10) — treat existing M01 `analysis_note`s as the L3 rich layer (re-home) vs regenerate terse.

> **Process note:** with these settled, V3_2 (the instruction) is written from §1–§9, and the schema is
> migrated per §10.
