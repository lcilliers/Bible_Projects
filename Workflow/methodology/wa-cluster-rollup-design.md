# The Roll-Up — verse relevance to cluster (data-flow & lifecycle design)

> **Living document · Doc version: 2 · 2026-06-06 · DRAFT for review.** *(v2: completeness pass — open-items
> section expanded from 5 to ~30, themed, after reviewing the session notes/foundations/memory.)* Articulates the **roll-up effect**
> of the reshaped pipeline, from the first step (establishing verse relevance) up to the cluster, before it
> is encapsulated in an instruction. Each level is described as **Source → Process → Outcome → Output**, and
> every **auxiliary table** that is augmented / updated / disposed along the way is mapped. Governed by
> `wa-verse-analysis-methodology.md`, `wa-cluster-phase-reshape-v3_1-proposal.md`, and the memory set
> (`feedback_phase_a_light_meaning_at_vcg`, `…_emergent_aggregate_questions`, `…_external_pole_not_inner_state`,
> `…_span_pairing_and_reciprocal_findings`).

---

## 0. The spine — what rolls up into what

```
L1 Relevance   →  L2 Similarity  →  L3 VCG + meaning  →  L4 VCG-emergent
(verse)           (verse)            (verse → VCG)        (verses → VCG)
                                                          │
                                                          ▼
                                   L5 Sub-group / CHARACTERISTIC-emergent  (VCGs → sub-group)
                                                          │
                                                          ▼
                                   L6 Cluster-emergent                      (sub-groups → cluster)
                                                          │
                                                          ▼
                                   L7 Findings + pointer adoption           (tier Q&A; cite; close)
```

The **unit of work** rises one rung at a time: verse → VCG → sub-group → cluster. Meaning is derived at L3
(not before). Structure (characteristics) **emerges** at L5/L6, it is not pre-designed.

---

## The four governing disciplines (apply at every level)

1. **No overlap — one home per statement.** Every analytical statement is placed at the **level where it
   first becomes true** (its *emergence level*) and is **not restated** at other levels. A single-verse
   reading lives on the verse; a truth-of-the-collection lives on the VCG / sub-group / cluster. Lower
   levels *feed* upper; upper levels do **not** duplicate lower. *This is the cure for the old
   "general observation" drift — every emergent statement now has exactly one anchored home.*
2. **Mop-up — every member consumed.** At each rung, **every object of the level below is accounted for**:
   no verse without a VCG, no VCG without a sub-group, no sub-group outside the cluster account. The
   **aggregate question** at each rung is the mop-up mechanism (it forces all members into view); a **gate**
   enforces zero left behind.
3. **No orphans — every object reaches a home.** In-scope → its level. Out-of-scope is *named as such and
   linked*, never dropped: external/physical pole → **cross-reference** to the inner counterpart;
   no-inner-being → **set-aside** (still feeds the term's semantic record); non-evidenced pointer →
   **set-aside with reason**. Nothing is silently ignored.
4. **Refinement is forward enrichment, not silent rework.** As understanding rises, lower objects are
   **enriched** (keywords light→rich, gloss compiled, anchors set, citations added) — additive, traceable.
   A **material change** (a re-read that alters a verse's meaning) **re-opens** the affected level
   (`feedback_verse_change_revalidation`); identity-preserving enrichment does not.

---

## Per-level — Source → Process → Outcome → Output (+ auxiliary tables, + mop-up/orphan rule)

### L1 · Establish verse relevance
- **Source:** `verse_context` rows for the cluster's terms (one per span) + `wa_verse_records` (text, span,
  context) + `mti_terms` (gloss).
- **Process:** classify each span-in-verse — inner-being-relevant, or set-aside (`no_inner_being |
  physical_only | spatial_only | unclear`). Light touch; no meaning derived.
- **Outcome:** every span classified.
- **Output:** `verse_context.is_relevant`, `.set_aside_reason`.
- **Aux tables:** none created. Set-aside reasons are **evidence-based** (feed the term's semantic record).
- **Mop-up / orphans:** *every* span classified (gate: no NULL `is_relevant`); set-asides are **not orphans**
  — they remain part of the term's meaning record (`feedback_setaside_verses_inform_word_meaning`).

### L2 · Light similarity
- **Source:** the `is_relevant=1` spans + their term / root / span features.
- **Process:** emit a **light similarity signal** sufficient to pre-group similar verses (atomic keywords /
  lexical-root features). **No interpretive meaning.**
- **Outcome:** each relevant verse carries a similarity tag; provisional groupings suggested.
- **Output:** `verse_context.keywords` (**light / atomic**, first pass) — *or* a dedicated similarity field
  〔open decision〕.
- **Aux tables:** keywords (light tier).
- **Refinement hook:** these are **deliberately thin** — they are *enriched* at L3. Phase A's only job.

### L3 · VCG formation + verse meaning (the core read)
- **Source:** the **actual verse texts** of the population (sub-group), spans tagged **T1 / T2 / FLAG**, the
  **term corpus** (for valence/sense clarification), the light groupings (L2), and the **surfaced
  pointers/flags** on these terms.
- **Process:** read the actual verses **together**; apply the verse-meaning discipline — span-focal Seven
  Principles · span **influence-test** (weave T2/T1 only when it influences; independent siblings flow
  through) · surroundings (from/to) · **clarify-by-corpus** · **3-pole scope** (inner / external / physical)
  · **open questions**. Form / refine **VCGs** by *sense-in-context*; designate **anchors**.
- **Outcome:** VCGs formed; each verse's **meaning-in-context**; scope classified; anchors set; open
  questions raised; pointers' validating evidence captured.
- **Output:**
  - `verse_context.analysis_note` — the **meaning, derived here** (not before).
  - `verse_context.group_id` → **`verse_context_group`** (VCG row; `group_code`, `context_description`).
  - `verse_context.is_anchor` — anchor designation(s) per VCG.
  - `verse_context.keywords` — **ENRICHED** (descriptive: span gloss + every T1 gloss + principle-bearing
    tokens) — the L2 light set is upgraded here.
  - scope-pole **cross-references** (external/physical → counterpart registry).
  - **open questions** (the corroboration worklist) 〔home: a column / observation type — open〕.
- **Aux tables:** `verse_context_group` **created**; `verse_context.keywords` **enriched**; **gloss compiled**
  into keywords/meaning (drawing on `mti_terms.gloss` + `wa_meaning_sense`/`_stem`/`_parsed`); pointers
  **surfaced** (not adopted).
- **Mop-up / orphans:** every `is_relevant` verse lands in exactly one VCG; every VCG has ≥1 anchor
  (gates B5/B7 analogues). External/physical-pole verses are **cross-referenced**, not housed as inner.

### L4 · VCG-emergent observation  (verses → VCG)
- **Source:** the VCG's verses + their L3 meanings.
- **Process:** the **aggregate question** — *what does this collection of verses jointly say about the VCG
  that no single verse captures?*
- **Outcome:** the VCG's **emergent meaning** (more than the sum of its verses).
- **Output:** the VCG's `context_description` — and/or `cluster_observation` 〔**DATA GAP:** no VCG/`group_id`
  anchor on `cluster_observation`; add a `group_id` column or record on `verse_context_group`〕.
- **No-overlap rule:** this statement is **VCG-level** — it is *not* duplicated onto the individual verses.

### L5 · Sub-group + CHARACTERISTIC-emergent  (VCGs → sub-group)
- **Source:** the sub-group's VCGs + their L4 emergent meanings; `mti_term_subgroup` (term placements).
- **Process:** the **aggregate question** — *what do these VCGs jointly say about the sub-group — how do its
  dimensions operate together?* The answer **is the characteristic** — it **emerges here**.
- **Outcome:** the sub-group's emergent meaning; the **characteristic** (named, defined).
- **Output:** `cluster_subgroup.core_description` (firmed); **`characteristic`** (`short_name`, `definition`)
  **created/refined**; **`characteristic_subgroup`** link; `cluster_observation` (sub-group level,
  `INTER_RELATIONSHIP` / `CLUSTER_SYNTHESIS`).
- **No-overlap rule:** characteristic-level truth lives here, not restated on each VCG.
- **Mop-up:** every VCG of the sub-group is in view; every non-BOUNDARY sub-group maps to a characteristic.

### L6 · Cluster-emergent  (sub-groups → cluster)
- **Source:** the cluster's sub-groups + characteristics (L5).
- **Process:** the **aggregate question** — *what do these sub-groups jointly say about the cluster — how do
  they operate together?*
- **Outcome:** the cluster's emergent account; the characteristic **structure** (`cluster.char_structure`).
- **Output:** `cluster_observation` (cluster level); `cluster.description` / `.char_structure` firmed.
- **Mop-up:** every sub-group is accounted for in the cluster account.

### L7 · Findings + pointer adoption  (the output layer)
- **Source:** the VCGs, characteristics, surfaced pointers, the L3–L6 meanings/observations.
- **Process:** answer the **189 tier questions** per sub-group (silence valid); **validate + adopt** the
  surfaced pointers; **cite** the evidence (anchors/verses).
- **Outcome:** evidenced findings; pointers resolved (adopted or set-aside non-evidenced).
- **Output:** **`cluster_finding`** (`characteristic_id`, `cluster_subgroup_id`, `vcg_scope`, `obs_id`);
  **`finding_citation`** (anchor/verse citations); `wa_session_research_flags.resolved` set + cross-ref;
  reciprocal findings for influencing multi-T1 siblings.
- **Mop-up / orphans:** every surfaced pointer is resolved (audit A6/A7/D2); every characteristic has
  findings (gate A3); every anchor verse is cited (gate B7).

---

## Auxiliary-table lifecycle matrix

Legend: **C** create · **E** enrich/refine · **U** update/firm · **R** reference (read-only) · **X** dispose
(soft-delete / supersede) · — none.

| Table | L1 relev. | L2 sim. | L3 VCG+meaning | L4 VCG-em | L5 subgrp/char | L6 cluster | L7 findings |
|---|---|---|---|---|---|---|---|
| `verse_context` (is_relevant, set_aside) | **C/U** | — | R | R | R | R | R |
| `verse_context.keywords` | — | **C** (light) | **E** (rich) | R | R | — | R |
| `verse_context.analysis_note` (meaning) | — | — | **C** | R | R | R | R |
| `verse_context.is_anchor` | — | — | **C** | R | R | — | R (cited) |
| `verse_context.group_id` | — | — | **C** | — | R | — | R |
| `verse_context_group` (VCG) | — | — | **C** | **E** (`context_description`) | R | R | R |
| `cluster_subgroup` | R | R | R | R | **U** (`core_description`) | R | R |
| `mti_term_subgroup` | — | — | R/U | — | **R/U** | — | R |
| `characteristic` | — | — | — | — | **C/E** (emerges) | U | R |
| `characteristic_subgroup` | — | — | — | — | **C** | — | R |
| `cluster_observation` | — | — | — | **C** (VCG-em*) | **C** (subgrp) | **C** (cluster) | R/U |
| `cluster.char_structure` / `.description` | — | — | — | — | — | **U** | R |
| `mti_terms` (gloss/`anchor_note`) | R | R | **R** (gloss compiled) | — | — | — | R |
| `wa_meaning_parsed/_sense/_stem` | R | R | **R** (gloss/sense compiled) | — | — | — | R |
| `wa_session_research_flags` (pointers) | — | — | **surface (R)** | — | — | — | **U** (adopt/resolve) |
| `cluster_finding` | — | — | — | — | — | — | **C** |
| `finding_citation` | — | — | — | — | — | — | **C** |

\* VCG-em row needs the `group_id` anchor gap resolved (L4).

---

## The cross-cutting refinement threads (the ones to watch)

- **Keywords — two tiers, forward-enriched.** L2 emits **light/atomic** keywords (the *clustering* signal);
  L3 **enriches** them to descriptive (span gloss + every T1 gloss + principle tokens). One field, two
  passes; the enrichment is additive and traceable. *(Resolves the keyword "wrong direction" worry.)*
- **Gloss compilation.** At L3 the term's `gloss` + structured senses (`wa_meaning_sense/_stem/_parsed`) +
  every T1 sibling's gloss are **compiled** into the meaning + enriched keywords — and feed the term's
  semantic record (incl. set-asides).
- **Anchors → citations.** Anchors are **designated at L3** (per VCG); they become **citations at L7**
  (`finding_citation`). Anchor designations on `verse_context.is_anchor`; the `mti_terms.anchor_note` may
  carry a term-level anchor note.
- **Emerging characteristics.** **Created at L5** from the aggregate answer (not pre-designed); refined at L6.
  This is the heart of the bottom-up structure.
- **Pointers/flags.** **Surfaced at L3**, **adopted/resolved at L7** (validate → finding + xref + close, or
  set-aside non-evidenced). Data flags (`PH2_*`) and BOUNDARY resolve in structural cleanup / constitution
  (outside this roll-up).
- **Emergent observations.** Recorded **level-anchored** in `cluster_observation` at L4/L5/L6 — the
  structured replacement for the old unstructured "general observation".

---

## Disposal / supersession (closing the loop, avoiding orphans)

- **Soft-delete only** (`delete_flagged=1`) — nothing physically removed.
- **Superseded VCGs / sub-groups / characteristics** (from a re-read that re-groups) are soft-deleted; their
  members are **re-homed** in the same pass (mop-up) — never left dangling.
- **Stale findings:** a material verse-meaning change **re-opens** the affected VCG/sub-group and stales its
  findings (`feedback_verse_change_revalidation`); identity-preserving enrichment does not.
- **Set-aside & external/physical-pole** material is **retained and linked** (term semantic record /
  counterpart cross-ref) — out of the inner-being analysis, never out of the data.

---

## Open items surfaced by this design (for the review)

*Expanded 2026-06-06 (completeness pass over the session notes, foundations and memory). Grouped by theme;
priority in **bold** where it touches the gravest risk or a missing layer.*

### A. Soundness & validation — the gravest risk runs *through* the roll-up
- **A1 · Verse-meaning corroboration is not yet a roll-up step.** L3 has *clarify-by-corpus* + *open
  questions*, but **no external corroboration** — anchoring each meaning to its **STEP lexical sense** and
  to **several translations**, flagging where the AI reading diverges. This is the gravest data risk and the
  queued audit-expansion (`project_next_action_audit_surface_verses`, foundations §b). *Where/how does
  corroboration enter L3?*
- **A2 · Where does the AUDIT sit in the roll-up?** The self-critical audit (aspect-spec Groups A–E + the new
  PA-1…16) currently runs at end of Phase D before prose (`feedback_audit_before_prose`). Does it gate
  **per level** (L3 / L5 / L7) or only at the end? The roll-up shows no audit gates.
- **A3 · Researcher review / sign-off gates are missing.** The roll-up reads mechanical, but findings are
  **drafts**, sifted iteratively, and a cluster is done only by **non-mechanical sign-off**
  (foundations §c; `feedback_remediation_stop_points`). *Where are the human stop-points at each level?*
- **A4 · Finding lifecycle (draft → reviewed → confirmed).** `cluster_finding.finding_status` exists, but the
  **iterative sift** (foundations §c-Q1) isn't a step in the roll-up. Where is the sift loop?

### B. Cross-cluster & whole-study — the roll-up stops one level too early
- **B1 · There is no L8.** The roll-up ends at the single cluster (L6/L7), but §d says the end-state
  **dissolves clusters into cross-cluster groupings**. A **whole-study synthesis level (L8)** is missing —
  it is where reciprocal findings reconcile and the cross-cluster characteristics form.
- **B2 · Interdependent clusters finalise together.** `feedback_interdependent_clusters_finalise_together` —
  synergy-clusters must be signed off **together**, not in isolation; the roll-up treats one cluster alone.
  *How do their roll-ups coordinate before sign-off?*
- **B3 · The reciprocal-finding loop has no consumer.** L7 *seeds* a candidate finding in sibling cluster Y;
  *when/how does Y consume it?* Cross-cluster ordering/dependency is unspecified.

### C. The term-corpus tension — clarification crosses the roll-up's boundaries
- **C1 · Clarify-by-corpus needs verses the roll-up unit doesn't hold.** L3 reads **this sub-group's**
  verses, but `feedback_term_corpus_anchors_meaning` says valence/sense is settled by the term's **other
  occurrences** — which may sit in other sub-groups, other clusters, or set-aside. *How is the term's full
  corpus surfaced at L3 without re-importing the cross-cluster boundary problem?*
- **C2 · A reuse / consistency store is implied but undefined.** Multi-T1 "**reuse if the combination was
  seen before**" (verse-analysis methodology) needs a memo of prior term/combination meanings so L3 reuses
  rather than redesigns. *Where does that consistency store live?*

### D. Process, ownership & cost
- **D1 · Owner per level is unspecified.** CC-API vs AI-chat vs researcher (`feedback_cc_only_pipeline_verdict`:
  prose→chat, findings→CC; `feedback_chat_vs_api_for_classification`). Is the **L3 deep read** an AI-chat
  analytical session or an API pass? This drives cost *and* quality.
- **D2 · Cost model at scale.** L3 deep read × sub-groups × 48 clusters, net of the triage savings — needs a
  rough budget (`feedback_methodology_cycle_cost`).
- **D3 · The complexity triage as routing.** How do the 4 groups (set-aside / single / T2+T1 / multi-T1)
  **route** verses through L1–L7? (set-aside stops at L1; single-span takes a light L3; multi-T1 the full path).

### E. Bootstrapping, re-runs & the data model
- **E1 · L3 population for *fresh* clusters.** A not-started cluster has **no sub-groups** yet — so what is
  the L3 read-population (the light-similarity groups from L2)? The bootstrapping path differs from re-doing
  an existing cluster.
- **E2 · Re-run / idempotency mechanics.** Partial re-run of a level and how upper levels react — the
  re-open rule is stated, the mechanics aren't.
- **E3 · What is an *anchor* for now?** We read **all** verses, not just the anchor — so does the anchor
  still privilege a verse, or is it only a citation seed for L7? Redefine or retire.
- **E4 · Retire/clarify legacy `verse_context` fields** in the new model: `is_related`, `vertical_pass_flag`
  (the vertical-pass experiment), and the `is_anchor` semantics (E3).
- **E5 · BOUNDARY handling.** Where BOUNDARY terms/verses (undecided placement) sit in the roll-up
  (constitution, upstream) — and how a BOUNDARY resolution re-enters.
- **E6 (carried) · VCG-level observation home** — `group_id` on `cluster_observation` vs `verse_context_group`.
- **E7 (carried) · Open-questions home** — column vs observation-type vs flag.
- **E8 (carried) · Phase-A similarity signal** — atomic keywords vs lexical/root features.
- **E9 (carried) · Field-name reconciliations** — `analysis_note` vs `meaning_pass_a`; `is_relevant`+
  `set_aside_reason` vs `ut_class`.
- **E10 (carried) · B.1 constitution / B.2 sub-group without an early meaning** — and the note that L5 now
  has characteristics *emerging*, so "design" becomes "emergence".

### F. Adjacent layers (scope boundary — name them so they aren't forgotten)
- **F1 · The science layer.** Scripture primary, then a **light-touch** correlation with the per-cluster
  science extract (`Workflow/Sciences/…scienceextract`). *Where does it enter — after L6, as a separate lens?*
  (`feedback_phase9_science_extract_required`.)
- **F2 · Findings → prose / publication.** The end products (essays, guides) render from findings (Session C
  cluster publication) — downstream of L7; note the boundary so the roll-up's output contract is clear.
