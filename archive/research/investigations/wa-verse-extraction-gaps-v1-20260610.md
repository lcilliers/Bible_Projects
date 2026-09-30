# Verse-extraction gaps — what the synthesis/synergy layer needs that the verse read isn't capturing

> **Reflection · v1 · 2026-06-10 · CC.** Prep for the catalogue session. Re-reads the original 189 tier questions
> against (a) the 14 implemented VE fields, (b) the VE-by-cluster results
> ([ve-by-cluster-20260610.md](../../outputs/markdown/ve-by-cluster-20260610.md)), and (c) the meaning prose.
> **Governing principle (researcher):** *if the evidence isn't captured at the verse, the analysis phase cannot
> recover it.* "It'll be dealt with in synthesis" is empty when the data was never teased out. Cause-and-effect
> is the headline hole; this hunts for the others too.

---

## 0. Method & a key distinction

Two kinds of gap — they need different fixes:

- **Type A — NOT CAPTURED at all** (not in any field *and* not reliably in the prose). Only a fresh/attentive read can supply it.
- **Type B — IN THE PROSE but NOT STRUCTURED.** The meaning paragraph states it, but no queryable field holds it, so cross-corpus analysis (thousands of verses) can't reach it without re-reading. **Recoverable by a structured second-pass extraction over the existing 8,367 meanings — cheap, no Bible re-read.**

Evidence the prose already holds a lot (M02 meanings): **cause markers 39% · object/target 48% · valence words 9% (more implicit) · inter-term links 15%** — all currently 0% structured. So much of the "missing" data is Type B, recoverable, not lost. That is the good news; the design choice is *which gaps become fields, and whether to backfill from prose or augment the read*.

## 1. What the verse read already captures well (the baseline)

The VE-by-cluster results prove these discriminate sharply and are well-populated, so they are NOT gaps:
`produces_effect` (~90–100% answered) · `faculty` (the cleanest separator) · `type` · `origin` (constitutional class) · `attributed_to_God` · `constitutional_location` · `typology_direction` · `literary_setting` · and the rich `sense_applied` / `relational_implication` (≈100%). The **effect** side and the **identity/constitution** side are covered.

## 2. The CAUSE side — the biggest hole (the user's focus)

The catalogue asks *why* and *from what* (T5.3 mechanism, T6.3 "produced by another", the "why did it happen"); the VE record answers almost none of it. `origin` only classes the *constitutional* source (within / outside / God) — **not the situational cause**.

| gap | catalogue refs | captured? | type | proposed field |
|---|---|---|---|---|
| **Eliciting cause / trigger** — *why did it arise here* (offence, injustice, threat, loss, command, provocation) | T5.3, T6.3.2, T1.5 | ✗ field · **39% in prose** | **B** | `eliciting_cause` (text + class: offence/injustice/threat/loss/command/jealousy/…) |
| **Object / target** — fear *of* X, anger *at* Y, wisdom *about* Z | T4.x, T1.4 | ✗ field · **48% in prose** | **B** | `object` (+ object-type: God/person/self/sin/enemy/situation/…) |
| **Experiencer / subject-type** — *who* has it (God / righteous / wicked / king / prophet / nation / everyman) | T0.1, T4 | only `attributed_to_God` (binary) | **B** | `experiencer_type` |

Without these, "why did it happen?" and "how does it differ across scenarios?" have **no structured evidence to roll up** — the synergy phase would be guessing or re-reading.

## 3. Cause & effect BETWEEN characteristics — the synergy core (a structural hole)

This is the deepest gap and the one most directly about *synergy*.

- The verse-complete read **sees every co-occurring term** but records **no typed relationship between them**. `produces_effect` is *characteristic → its own effect*, never *characteristic-A → characteristic-B*.
- The proposed `co_occurrence_array` (VE-17) would list *which* terms co-occur — but **un-typed**. Co-occurrence is only a *candidate-finder* ([[project_cross_cluster_three_link_classes]]); the prize is the **typed relationship + its differential effect** (A[type] —rel[effect]→ B[type], [[feedback_ontology_typed_relationships]]).
- So the entire inter-characteristic causal web — *fear → trembling*, *anger → murder*, *grief + anger → withdrawal*, *jealousy → wrath*, *wisdom → right action* — is in the prose (15% show explicit link verbs; many more implicit) but **not structured**.

**Proposed:** for each ordered pair of co-occurring in-scope terms in a verse, a **typed link** {`causes` · `produces` · `intensifies` · `opposes` · `accompanies` · `responds-to` · `precedes/follows` · `constitutes`} **+ the effect/differential**. Heavier than a flag, but it *is* the substrate the synergy phase consumes. Type **B** (in prose) for the explicit cases; **A** for the implicit ones a fresh read must judge.

## 4. The DIFFERENTIATION & EXCEPTION axes (the user's "how does it differ / exceptions")

To answer *how does this differ from other scenarios* and *what are the exceptions*, the verse must record the axes that separate instances. Three are missing:

| gap | why it matters | catalogue refs | type | proposed field |
|---|---|---|---|---|
| **Valence / normative status** — *righteous vs sinful, commanded vs forbidden, appropriate vs distorted* | THE exception axis: righteous anger vs sinful anger; fear-of-God vs cowardice; "be angry and sin not". `moral-evaluation` (faculty engaged) ≠ the valence of *this* instance | T0.2.2, T1.7, T5.1 | **B** (9% explicit, more implicit) | `valence` {righteous/appropriate · sinful/distorted · commanded · forbidden · neutral · mixed} |
| **Scenario / situation type** — battle, worship, judgment, family-conflict, court, covenant, temptation | differentiation needs the *situation*, not just the genre (`literary_setting`) | T7.2.4 | **A/B** | `scenario_type` (controlled list) |
| **Intensity / degree** — mild ↔ extreme | distinguishes a flash of irritation from consuming wrath (Anger's compound-heaping hints at it, unstructured) | T1.6, T5.1 | **A/B** | `intensity` {low · moderate · high · extreme} |

Valence especially: **without it, "the exceptions" cannot be queried at all** — they're the whole point of the differentiation, and right now they live only in adjectives inside the prose.

## 5. The DYNAMIC / sequence axis (secondary, but real)

- **T5.2 Sequence of inner states** (before → during → after) and **T5.3 Mechanism of change** (discipline / encounter / gradual / sudden). `immediate_response` + `produces_effect` are two snapshots, not an ordered sequence or a named mechanism.
- Mostly **Type B** (the prose narrates the sequence). Lower priority than §2–4, but note: `immediate_response` is *mostly SILENT* (62–87% across clusters) — the "during" reaction is the most under-captured of the snapshots.

## 6. Smaller structured gaps (catalogue items with no verse evidence yet)

- **Relational direction, typed** (VE-15 proposed) — currently only free-text `relational_implication`; T4 interface direction (God↔human / give / receive / spirit-beings) is not a closed field.
- **Suffering context** (VE-16 proposed) — T5.4.
- **Antonym / contrast present** — T1.3 boundary: does the verse invoke the opposite (light vs dark, wisdom vs folly)? Not flagged.
- **Temporal aspect** — momentary / habitual / sustained; `mode` carries the stem but not the durative aspect explicitly.

## 7. Recoverability & recommendation (for tomorrow)

| gap | priority | type | fix |
|---|---|---|---|
| Eliciting cause / trigger | **high** | B | new field; **backfill from existing meanings** |
| Object / target (+ type) | **high** | B | new field; backfill from meanings |
| Valence / normative status | **high** | B | new field; backfill from meanings |
| Typed inter-characteristic link (+ effect) | **high** | B/A | new pair-relationship record; backfill explicit cases, augment read for implicit |
| Experiencer / subject-type | medium | B | new field; backfill |
| Scenario / situation type | medium | A/B | augment read (genre ≠ situation) |
| Intensity / degree | medium | A/B | augment read; partial backfill |
| Sequence / mechanism of change | medium | B | mostly synthesis-derivable from cause+effect+response once those exist |
| Relational direction typed · suffering · antonym · aspect | low | mixed | as the catalogue D-decisions land |

**The headline for the catalogue session:**
1. **The effect side is captured; the cause side is not.** Add `eliciting_cause`, `object`, `valence`, `experiencer_type`, and a **typed inter-term relationship** — these four-plus are what "why / how-differs / exceptions / cause-and-effect" actually need.
2. **Most of it is Type B** — already sitting in the 8,367 meaning paragraphs (39–48% show the markers). So the first move can be a **structured extraction pass over existing meanings** (no Bible re-read, cheap) to populate the new fields, *then* augment the live read going forward for the Type-A residue (scenario, intensity, implicit links).
3. This slots straight into the restructured catalogue as **new Layer-A fields** (extending VE-15/16/17 with `eliciting_cause` · `object` · `valence` · `experiencer_type` · `typed_relationship`), each cross-referenced to the SYNTH questions it would feed (T5.3, T6.2/6.3, T0.2.2, T1.7, T4.x).

> Net: we are *largely on the right track* — identity, constitution, faculty, and effect are solid. The systematic blind spot is **causation and differentiation**: *why* it happened, *at/of what*, *with what valence*, and *how characteristics act on each other*. That is recoverable — much of it is already in the prose — but only if we decide to structure it now, before synthesis assumes it exists.
