# Tier Catalogue — Restructured (Two-Layer Slice) · v1 · 2026-06-10

> **Supersedes** [`wa-tier-questions-extract-v1-20260604.md`](wa-tier-questions-extract-v1-20260604.md) (the flat 189-question characteristic-level catalogue, T0–T7).
> **For approval — DB not yet modified.** This document restructures the catalogue around the **two-layer slice** designed 2026-06-09
> ([verse-level extraction spec](../../research/investigations/wa-verse-level-extraction-spec-v1-20260609.md) · [catalogue refit](../../research/investigations/wa-catalogue-refit-two-layer-v1-20260609.md)).
> Once approved, the structure lands in `wa_obs_question_catalogue` via migration (new `layer` tag, drop flags, field↔question cross-ref).
>
> **Numbering note (per researcher):** the **old T-codes are retained as a reference column everywhere** because the numbering is expected to change. New verse-field IDs (`VE-nn`) are provisional. Nothing here renumbers the live catalogue yet — old codes are the stable anchor until a new scheme is signed off.

---

## 0. The two layers (and why)

The old catalogue asks every question about *"this characteristic"* at the **distilled / synthesis** grain (the cluster's overall nature). Verse-level analysis can't answer most of them at one verse — but it **feeds** them. So the catalogue splits:

| Layer | grain | what it is | where it lives |
|---|---|---|---|
| **A · Verse-Extraction (L1/L2)** | one typed term-in-verse | structured fields with **closed option-lists** — the *evidence*, state-not-induce (NONE/SILENT/not-stated first-class) | the L2 read → `finding` (l2_api) → **`v_l2_tier`** |
| **B · SYNTH** | characteristic / cross-verse / cross-term / cross-cluster | the *"what does X reveal"*, *over-time*, *pattern*, *relationship* questions — **computed by rolling up** Layer A, never asked at the verse | the synthesis pass (later) |

**Disposition of every old question** is one of: **→ Layer A field** · **→ SYNTH** · **DROP** · **DE-FORCE** (rephrased forcing question, which then lands in A or B). All 189 are accounted for in §5.

---

## 1. Layer A — The Verse-Extraction Record (L1/L2)

Per **typed term-in-verse**. `M` = mechanical (L1 / morphology / lexical pre-fill) · `R` = read. **Live** = currently emitted by the L2 writer and queryable in `v_l2_tier`.

### 1a. Implemented fields — the **14** the L2 read produces today (the "14 tier questions")

| VE | field | option-list / format | M/R | **old code(s) realized** | live in `v_l2_tier` |
|---|---|---|---|---|---|
| **VE-01** | `sense_applied` | the verse-specific sense (clean phrase) | M | **T7.1.3** (also feeds T1.1.2 · T7.1.1–.2) | ✓ |
| **VE-02** | `type` | `action · status · quality` | M | **T1.2.1** | ✓ |
| **VE-03** | `compound` | `simple` · `compound:<parts>` | R | **T1.2.2** | ✓ |
| **VE-04** | `mode` | the operative stem / contextual mode (this verse) | M | **T1.4.1** (per-verse instance of T1.4) | ✓ |
| **VE-05** | `constitutional_location` *(multi)* | `spirit · soul · heart · mind · body-part:<x> · other-soul:<x> · NONE` | M-keyword + R | **T2.1.1 · T2.2.1 · T2.3.1 · T2.4.1 · T2.6.1** (T2.5.1 other-soul) | ✓ |
| **VE-06** | `origin` | `within-person · received-from-outside · bestowed-by-God · carried-generationally · not-stated` | R | **T2.9.1** | ✓ |
| **VE-07** | `faculty` *(multi)* | `perception · cognition · memory · affect · creativity · volition · agency · moral-evaluation · conscience · relational · NONE` | R | **T3.1.1 · T3.2.1 · T3.3.1 · T3.4.1 · T3.5.1 · T3.6.1 · T3.7.1 · T3.8.1 · T3.9.1 · T3.11.1** | ✓ |
| **VE-08** | `attributed_to_God` | `yes · no` (+ note) | R | **T0.1.2** | ✓ |
| **VE-09** | `purpose_equips` | text — what it equips the person to be/do/become, or `not-stated` | R | **T0.2.1** | ✓ |
| **VE-10** | `typology_direction` | `human→divine · divine→human · none` | R | **T0.4.2** | ✓ |
| **VE-11** | `immediate_response` | text · `SILENT` | R | **T1.5.1** | ✓ |
| **VE-12** | `produces_effect` | text — what it produces here (immediate) | R | **T1.6.1** | ✓ |
| **VE-13** | `relational_implication` | text — directional/relational force the term carries here | R | **T1.1.3** | ✓ |
| **VE-14** | `literary_setting` | `narrative · poetry · law · prophecy · wisdom · epistle · gospel · …` | R | **T7.2.2** | ✓ |

> Cross-reference is exact and already in the DB: every `l2_api` finding links to its old code via `finding_question_link → wa_obs_question_catalogue.question_code` (the `v_l2_tier.question_code` column). VE-05 and VE-07 are multi-select — each present value is one linked finding; absence = `NONE`/not-linked.
>
> **Faculty note:** the read uses **10** faculties; old **T3.10 Conscientiousness** is *not* one of them (it was the "integrated moral-awareness+volition+action" composite — a SYNTH roll-up of affect/volition/agency/moral-evaluation/conscience, not a primitive). See §5.

### 1b. Proposed additions / extensions (design D-decisions — **not yet in `v_l2_tier`**)

| VE | field | option-list / format | old code(s) it would realize | status |
|---|---|---|---|---|
| **VE-06+** | `origin` **+ `from-other-spirits`** | add to VE-06 list | T2.9.1 (gap) + draws on **T4.6** | **D2** — angelic/adversarial origin currently excluded; design says add |
| **VE-05+** | `constitutional_location` **+ `will · conscience`** levels | extend VE-05 list across all constitutional levels | **T2.1–T2.5** fuller | **D4** — confirm the level list |
| **VE-15** | `relational_direction` *(multi)* | `divine→human · human→divine · give · receive · spirit-beings` | **T4.1.1 · T4.2.1 · T4.3.1 · T4.4.1 · T4.6.1** (the interface *.1*s) | **D4** — make a verse field, or keep SYNTH? |
| **VE-16** | `suffering_context` *(flag)* | `present:<role>` · `NONE` | **T5.4.1** | proposed — verse places the term in suffering? |
| **VE-17** | `co_occurrence_array` | the verse's set of other in-scope typed terms | **T6.1.1** | already recorded as the verse term-set (verse-complete read); surface it as a field |

---

## 2. Layer B — SYNTH (roll-up / relationship / dynamic)

Computed across verses / terms / clusters; **never asked at the verse**. Grouped by old tier (codes retained as reference; final SYNTH numbering TBD). "Fed by" names the Layer-A field(s) the roll-up consumes.

### T0 — Divine Image & Created Design
| old code | SYNTH question (de-forced where noted) | fed by |
|---|---|---|
| T0.1.1 | What does the God-attribution reveal about God's nature this characteristic reflects? *(de-forced: the verse only flags presence)* | VE-08 |
| T0.1.3 | Where God-attribution is consistently absent, what does that silence suggest? | VE-08 (no across corpus) |
| T0.2.2 | Original-design vs response-to-the-fall (the binary) | VE-09, corpus |
| T0.2.3 | Oriented toward a future fullness? | VE-09, VE-12 |
| T0.3.1–.3 | Image-bearer expression — how it instantiates the divine likeness; shared vs analogue; presence/absence & image condition | VE-08, corpus |
| T0.4.1 / .3 | Whether Scripture uses it typologically at all (the corpus judgement) | VE-10 |

### T1 — Definition
| old code | SYNTH question | fed by |
|---|---|---|
| T1.1.1 | Programme name & what the name signals (cluster-level) | VE-01 across |
| T1.1.2 | Definitional read of the H/G terms (before deep lexical) | VE-01 across |
| T1.3.1–.3 | Boundary — structural opposite; what it excludes/resists; where it ends | VE-01, vocabulary |
| T1.4.1 / .2 / .3 | The full **mode-set**; context/direction/level variation; speech-based mode | VE-04 across |
| T1.5.2 | Is the immediate response consistent or variable? | VE-11 across |
| T1.6.2 / .3 | States/qualities established over time; sustained vs immediate | VE-12 across |
| T1.7.1–.3 | Conditions of reception — enabling / blocking / non-receiver state | VE-09, VE-12, corpus |

### T2 — Constitutional Location & Boundaries
| old code | SYNTH question | fed by |
|---|---|---|
| T2.1.2/.3 · T2.2.2 · T2.3.2 · T2.4.2 · T2.5.2 · T2.6.2 | What each location **reveals** (the `.2`/origin-of-level reveal) | VE-05 across |
| T2.7.1/.2 | Body↔soul direction & its consequence (where a body link exists) | VE-05 (body) |
| T2.9.2/.3 | Origin singular vs multiple; origin changing across contexts | VE-06 across |
| T2.10.1–.3 | Constitutional **movement** across levels (sequence/pattern) | VE-05 across |

### T3 — The Inner Faculties
| old code | SYNTH question | fed by |
|---|---|---|
| T3.x.2 (×11) | Does it **enable / deepen / bypass / impair** faculty X? (effect) | VE-07 across |
| T3.x.3 (×11) | What the **pattern** of engagement/non-engagement reveals | VE-07 across |
| T3.10.1–.3 | **Conscientiousness** (integrated moral-awareness+volition+action) — a composite roll-up | VE-07 (affect/volition/agency/moral-eval/conscience) |

### T4 — Relational Interfaces
| old code | SYNTH question | fed by |
|---|---|---|
| T4.1.2/.3 · T4.2.2/.3 · T4.3.2/.3 · T4.4.2/.3 | Basis / disposition / inner-conditions of each interface | VE-13, VE-15(proposed) |
| T4.5.1–.4 | Relational boundaries — within-bond vs across-distance; covenantal scope; who's included | VE-13, VE-15 across |
| T4.6.2/.3 | Adversarial-site & angelic-mediation | VE-06+ (from-other-spirits), VE-15 |

### T5 — Formative & Developmental
| old code | SYNTH question | fed by |
|---|---|---|
| T5.1.1–.3 | Nature of transformation (condition / orientation; reversible?) | VE-12 across |
| T5.2.1–.3 | Sequence of inner states (before/during/after) | VE-11, VE-12 across |
| T5.3.1–.3 | Mechanism of change (discipline/encounter/gradual/sudden) | VE-12, corpus |
| T5.4.2/.3 | Does suffering deepen/test/reveal/produce it? | VE-16(proposed) across |
| T5.5.1–.3 | Formation & sanctification arc | VE-12 across |
| T5.6.1–.3 | Eschatological trajectory | VE-09, VE-12 across |

### T6 — Structural Relationships with Other Characteristics
| old code | SYNTH question | fed by |
|---|---|---|
| T6.1.2/.3 | Co-occurrence **pattern** & what it reveals | VE-17 across |
| T6.2.1–.3 | Sequential relationships (precede/follow/accompany; causal/developmental) | VE-17, VE-12 |
| T6.3.1–.4 | Causal & constitutive (produces / produced-by / constituent) | VE-12, VE-17 |
| T6.4.1–.4 | Vocabulary & root sharing | VE-01, term root-family |
| T6.5.1–.4 | Distinctions from nearest neighbour | VE-01, VE-02, corpus |

### T7 — Evidential & Methodological
| old code | SYNTH question | fed by |
|---|---|---|
| T7.1.1/.2 | Primary terms & root meanings; grammatical range | VE-01, VE-04 across |
| T7.1.4–.10 | The vocabulary **arc** — distinguishing terms, opposite, person-type, supplication, OT↔NT continuity, NT coinage, full range | VE-01 across, vocabulary |
| T7.2.1 / .3 / .5 / .6 | Function in verse; argument structure; primary anchor & what it uniquely reveals | VE-14, corpus |
| T7.2.4 | Contextual setting (judicial/liturgical/covenantal/…) | VE-14 (could extend) |

---

## 3. DROP — removed (programme constructs / no verse referent)

| old code(s) | question | reason |
|---|---|---|
| **T1.2.3** | "best working description" | a programme write-up step, not an observation |
| **T1.8.1–.3** | Dimension Classification | the *dimension* construct is retired |
| **T2.8.1–.3** | Body-Deposit (DNA / generational) | speculative construct — extracts something not in the evidence |
| **T5.7.1–.3** | Deposit Consequence | depends on the dropped T2.8 |
| **T6.6.1–.3** | Shared Verse Anchors | "anchor" is a VCG/programme construct; co-occurrence (T6.1 → VE-17) covers it |
| **T6.7.1–.3** | Dimensional Sharing | dimension construct |

**Defer (not dropped):** **T7.3.1–.4** Human Science Frameworks — an external interpretive lens, not inner-being verse evidence; kept out of the core verse layer, revisited in synthesis.

---

## 4. DE-FORCE — forcing questions rephrased to neutral checks (silence first-class)

The tell is *"what does X reveal / suggest"* or *"in what way does it express Z"* — these **prompt a finding that may not exist**. Rephrased to *"is there evidence of X here? — record it; if not, silent."* The verse-level check lands in a Layer-A field; the original "reveal" becomes SYNTH.

| old code | original (forcing) | de-forced verse check | lands in |
|---|---|---|---|
| T0.1.2 | "what does the attribution reveal about its significance…" | **Is the term predicated of / related to God here?** (yes/no) | VE-08 |
| T0.1.1 / .3 | "what does it reveal / what does silence suggest about God's nature" | — (the reveal is SYNTH) | B/T0 |
| T0.2.2 | "original design *or* response to the fall?" | drop the binary; **note only if the verse states a purpose** | VE-09 |
| T0.3.1/.3 | "in what way does it express the divine image… presence/absence reveal" | **Does the verse tie the term to the image of God?** (rare; mostly silent) | B/T0 |
| T2.x.2 | "what does X-location reveal" | **Is it located at X here?** | VE-05 |
| T3.x.2 | "does it enable/deepen/bypass/impair faculty X" | **Which faculty(ies) does the term engage here?** | VE-07 |
| T3.x.3 · T1.5.2 · T1.6.x | "what does the pattern reveal" | — (SYNTH only) | B |
| T5.4.x | "does suffering deepen/test/reveal/produce it" | **Does the verse place the term in suffering?** (+ role) | VE-16 |

---

## 5. Complete disposition index — all 189 old questions accounted for

`→VE-nn` = Layer A field · `SYNTH` = Layer B · `DROP` · *(silence folds = the `.x.N "if silent, note"` sub-question folds into its field's NONE/SILENT token, not a separate question)*.

| old code | disposition | | old code | disposition |
|---|---|---|---|---|
| T0.1.1 | SYNTH | | T2.6.1 / .2 / .3 | **→VE-05** / SYNTH / folds |
| T0.1.2 | **→VE-08** (de-forced) | | T2.7.1 / .2 / .3 | SYNTH / SYNTH / folds |
| T0.1.3 | SYNTH | | T2.8.1–.3 | **DROP** |
| T0.2.1 | **→VE-09** | | T2.9.1 / .2 / .3 | **→VE-06** / SYNTH / SYNTH |
| T0.2.2 / .3 | SYNTH | | T2.10.1–.3 | SYNTH |
| T0.3.1–.3 | SYNTH | | T3.1–T3.9, T3.11 (×10) .1 | **→VE-07** |
| T0.4.1 | SYNTH | | T3.x.2 / .3 (×11) | SYNTH |
| T0.4.2 | **→VE-10** | | T3.10.1–.3 (Conscientiousness) | SYNTH (composite) |
| T0.4.3 | folds (→none) | | T4.1.1 · T4.2.1 · T4.3.1 · T4.4.1 · T4.6.1 | **→VE-15** (proposed) |
| T1.1.1 / .2 | SYNTH | | T4.1–4.4 .2/.3 · T4.5.x · T4.6.2/.3 | SYNTH |
| T1.1.3 | **→VE-13** | | T4.x.4 ("if silent") | folds |
| T1.2.1 | **→VE-02** | | T5.1.x · T5.2.x · T5.3.x | SYNTH |
| T1.2.2 | **→VE-03** | | T5.4.1 | **→VE-16** (proposed) |
| T1.2.3 | **DROP** | | T5.4.2 / .3 | SYNTH / folds |
| T1.3.1–.3 | SYNTH | | T5.5.x · T5.6.x | SYNTH |
| T1.4.1 | **→VE-04** (verse) / SYNTH (mode-set) | | T5.7.1–.3 | **DROP** |
| T1.4.2 / .3 | SYNTH | | T6.1.1 | **→VE-17** (proposed) |
| T1.5.1 | **→VE-11** | | T6.1.2 / .3 | SYNTH |
| T1.5.2 / .3 | SYNTH / folds | | T6.2.x · T6.3.x · T6.4.x · T6.5.x | SYNTH |
| T1.6.1 | **→VE-12** | | T6.6.1–.3 | **DROP** |
| T1.6.2 / .3 | SYNTH | | T6.7.1–.3 | **DROP** |
| T1.7.1–.3 | SYNTH | | T7.1.3 | **→VE-01** |
| T1.8.1–.3 | **DROP** | | T7.1.1 / .2 | SYNTH (VE-01/04 feed) |
| T2.1.1 / .2 / .3 / .4 | **→VE-05** / SYNTH / SYNTH / folds | | T7.1.4–.10 | SYNTH |
| T2.2.1 / .2 / .3 | **→VE-05** / SYNTH / folds | | T7.2.1 | SYNTH |
| T2.3.1 / .2 / .3 | **→VE-05** / SYNTH / folds | | T7.2.2 | **→VE-14** |
| T2.4.1 / .2 / .3 | **→VE-05** / SYNTH / folds | | T7.2.3 / .4 / .5 / .6 | SYNTH |
| T2.5.1 / .2 / .3 | **→VE-05** (other-soul) / SYNTH / folds | | T7.3.1–.4 | **DEFER** |

**Tally:** of 189 — **14 → Layer A (implemented)** · **+3 proposed Layer A (VE-15/16/17, with T2.5/T2.6 other-soul + origin/location extensions)** · **~118 → SYNTH** · **18 DROP** · **4 DEFER (T7.3)** · the remaining `.x "if silent, note"` sub-questions **fold** into their field's null token.

---

## 6. Open decisions (carried forward from the design docs — for your markup)

| # | decision | recommendation |
|---|---|---|
| **D1** | Confirm the **DROP** list (T1.2.3, T1.8, T2.8, T5.7, T6.6, T6.7) | adopt |
| **D2** | `origin` **+ `from-other-spirits`** (VE-06+) | adopt — real constitutional source, currently excluded |
| **D3** | `faculty` as the per-term multi-select from the 10 (the T3 restructure) | adopt (already live); decide T3.10 Conscientiousness stays SYNTH-composite |
| **D4** | `constitutional_location` level list (VE-05) **+** whether `relational_direction` (VE-15) is a verse field or SYNTH | confirm level list; recommend VE-15 **as a verse field** (the interface direction is verse-readable) |
| **D5** | Confirm the **M/R** split (which fields mechanical-mandatory vs read) | per §1a M/R column |
| **D6** *(new)* | New numbering scheme — keep T-codes, or renumber Layer A as `VE-nn` + SYNTH as `S-…`? | retain old T-codes as the reference key (this doc); assign new IDs only on sign-off |

---

### Provenance
- Supersedes: `wa-tier-questions-extract-v1-20260604.md` (flat 189, characteristic-level).
- Designs applied: `wa-verse-level-extraction-spec-v1-20260609.md`, `wa-catalogue-refit-two-layer-v1-20260609.md`.
- Live cross-reference: implemented fields VE-01..VE-14 ↔ old codes are already linked in the DB via `finding_question_link`; queryable through the `v_l2_tier` view (`question_code` column).
- **DB unchanged.** On approval: migration to tag `wa_obs_question_catalogue` rows with `layer` (A/SYNTH/DROP/DEFER), record the VE field↔question cross-ref, and (separately) apply the de-force rewordings.
