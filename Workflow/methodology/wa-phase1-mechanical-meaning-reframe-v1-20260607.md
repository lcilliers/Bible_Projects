# Phase 1 meaning + keywords — mechanical STEP application (reframe proposal)

> **Methodology proposal · v1 · 2026-06-07 · CC.** A proposed refinement to **L1/L2** of
> `wa-cluster-rollup-design.md` and `wa-cluster-phase-reshape-v3_1-proposal.md`, prompted by the A1 / M01
> corroboration finding (97% of derived meanings already corroborate to STEP mechanically — see
> `research/investigations/wa-a1-corroboration-m01-results-and-method-v1-20260607.md`). **To be folded into
> the design docs if confirmed.** Anchors: rollup-design open items **A1**, **E8**, **B.2/L2**; memory
> `feedback_phase_a_light_meaning_at_vcg`, `feedback_term_corpus_anchors_meaning`,
> `project_keyword_analytics_revision_parked`.

---

## The reframe

- **Old framing:** Phase 1 passes each verse to AI → AI **derives** an interpretive meaning + interpretive
  keywords.
- **New framing:** Phase 1 **applies the term's STEP sense mechanically**. The Phase-1 meaning *is* the STEP
  sense realised at that occurrence; the keywords are a **brief capture of the STEP meaning** (sense tokens +
  pole), **not** derived interpretive values. The step's real product is to **surface the residue** — the
  verses STEP cannot settle — for advanced analysis.

**Why it follows from the finding.** The M01 A1 test showed **949/949** meanings corroborate to the term's
STEP sense-set, **97% mechanically**. On that corroborating mass, the AI "derivation" was effectively
**re-stating the lexicon in prose** — cost and bias-risk with no interpretive gain. Removing AI latitude
where there is nothing to interpret is **both cheaper and less biased** — it directly answers the bias
problem the whole reshape was built around (cold per-verse AI bakes in bias; the corpus/lexicon anchors
meaning).

This is the **inversion**: corroboration stops being a downstream audit and becomes the **generation
principle**. A Phase-1 meaning built *from* the STEP sense **cannot diverge** from it by construction.

---

## The one boundary — single-sense vs multi-sense terms

Mechanical application is clean only where the term has **one** sense. A term carries a **sense-set**, and
*which* sense a verse realises can require context.

- **Single-sense terms** (e.g. `adēmoneō` = distress / anguish): the meaning is assigned **outright** —
  fully mechanical.
- **Multi-sense terms** (`ya.re`, `ra.gaz`, `cha.tat`): the **sense-set (envelope) is mechanical**, but
  **sense-selection per verse is the analysis.**

**Evidence — `ya.re` (H3372) across its poles:**

| Ref | Target | Sense realised (from the derived note) |
|---|---|---|
| Gen 3:10 | afraid | shame-triggered **dread** of divine presence |
| Gen 15:1 | Fear | inward **anxiety** about the future |
| **Exo 20:20** | fear | **one verse explicitly contrasts** "panic-fear" vs "**reverential** fear" |
| 1Ki 18:3 | feared | lifelong **reverence** (defining character) |
| 1Ch 17:21 | awesome | **reverent awe** at God's acts |

Same lemma, opposite poles (threat-dread ↔ reverence-awe). Sense-selection is real work — **but bounded:**
choose among the *listed* STEP senses (+ pole), not invent a reading. That is a far lighter, far less
bias-prone task than free interpretation, and the candidates are given.

---

## The resulting Phase-1, in four layers

| Layer | Who | What | Output |
|---|---|---|---|
| **0 · Attach** | CC (script) | To every relevant verse, attach the term's **STEP sense-set (envelope) + pole map + STEP-capture keywords**. | candidates + keywords |
| **0b · Stem-narrow** | CC (script) | Read the verse's **STEP morphology** (the `morph` attribute → binyan/stem) and **narrow the sense-set to the stem's branch** (Qal/Niphal/Piel → its BDB sub-senses). *Free mechanical disambiguation — see `research/investigations/wa-step-morphology-sense-disambiguation-v1`.* | narrowed sense-set |
| **1 · Assign** | CC (script) | Where Attach+Stem-narrow leave **one sense** → meaning = that sense. Done (covers all single-sense terms and stem-resolved multi-sense verses). | applied STEP meaning |
| **2 · Select** | AI / researcher (light) | **Within-stem multi-sense** (e.g. Qal `ya.re` = fear *or* reverence) → **select** which listed sense (+ pole) the verse realises. Bounded choice. | applied STEP meaning |
| **→ Residue** | advanced (VCG-stage) | Verses the sense-set itself can't settle — genuine valence ambiguity, **metaphor / pole** (`mish.bar` sea-waves → inner crushing), novel combination. | read-verses-together |

Layer **0b** is the new lever from the STEP exploration: the per-verse **stem** mechanically picks the
sense-branch, so much multi-sense work is done for free and the residue for *advanced* analysis is **narrow
and well-marked** — interpretive effort is spent only where the lexicon genuinely runs out.

---

## What "meaning" and "keywords" become

- **`analysis_note` (Phase 1):** terse and STEP-anchored — *"distress / anguish (inner pole)"* — **not** a
  contextual narrative. Cannot diverge from STEP.
- **`keywords`:** the **STEP capture** — sense tokens + selected sense + pole tag; mechanical and **traceable
  to the lexical source**. (The A1 scanner already extracts exactly these tokens, so the keyword generator is
  most of the way built.) This may **resolve the parked keyword-bias problem**
  (`project_keyword_analytics_revision_parked`): replacing the interpretive `[faculty][predicate]` phrase —
  whose **qualifier axis was where bias lived** — with a lexical-sense capture removes the bias surface.
- **The rich contextual reading** (e.g. *"Jesus in Gethsemane facing suffering, anguished heaviness of
  spirit"*) is **not Phase-1 output** — it is VCG / aggregate / findings-layer content. The **existing M01
  `analysis_note`s are that richer layer, produced early** — the very thing the reshape warned against. Under
  this model they would be recognised as **VCG-layer** (kept and re-homed), and Phase 1 holds the terse STEP
  statement.

---

## Implications

1. **De-risking.** Phase-1 meaning can't drift from the lexicon. A1's **DIVERGENT** verdict can now only
   arise at the **sense-selection / advanced** layer — a much smaller, explicitly-flagged surface.
2. **Cost.** The bulk is a script; AI touches only multi-sense selection + residue. (Verse-weighted, the
   multi-sense share is larger than the term-count suggests, because the high-frequency terms — `ya.re`,
   `fobeō`, `ra.gaz` — are the polysemous ones. A real estimate needs the single/multi detector below.)
3. **Data model — the verse record must carry the whole finding** (researcher markers, 2026-06-07):

   | Field (new/role) | Holds | Source |
   |---|---|---|
   | `step_meaning_applied` | the **applied STEP meaning** — the selected sense, terse | Layers 1/2 |
   | `sense_id` | which listed STEP sub-sense was selected | sense tree |
   | `sense_multiplicity` | **single / multi** indicator (the term's envelope shape) | detector (R2) |
   | `step_envelope_note` | the **STEP-derived comments / full sense-set** — kept *for further analysis* | sense tree |
   | `morph_code` / `stem` | per-occurrence morphology + binyan | STEP `morph` |
   | `pole` | inner / external / physical | sense→pole + judgement |
   | `analysis_note` (existing) | **the AI meaning — NOT overwritten, carried alongside** | unchanged |

   **Dual meaning is explicit:** the STEP-applied meaning is recorded *in addition to* the AI meaning, never
   over it — both are worth carrying (the AI note becomes the VCG-layer reading; the STEP meaning is the
   lexically-anchored Phase-1 value). This *is* the A1 verdict-home decision (D-A1-a) — design together.
4. **T2 = the parked "Supplementary" cluster — STEP sense surfaces its mis-parked inner-being terms.**
   T2 holds **620 parked terms** (status "Not started"); most are genuinely out of scope (particles, body
   parts, objects), but several were pulled under inner-life words and parked anyway (`ya.tsar` "be
   distressed", `mar` "bitter"/anguish, `anankē` "distress", `aph` "anger", `a.voy` "pain!"/sorrow). The
   **STEP sense-set overlap machinery (the A1 scanner) points cross-cluster**: score each T2 term's sense
   tokens against every real cluster's sense-envelope → **surface candidate home clusters** for the eventual
   T2 rework. This is the *no-orphans / mop-up* discipline applied to the parked pool. Demonstration:
   `research/investigations/wa-t2-relevance-surface-v1-20260607.md`.
5. **Existing data.** M01's rich notes are VCG-layer; a mechanical Phase-1 re-run produces terse STEP
   meanings **alongside** them (dual meaning, point 3) — so nothing is lost; decide whether the AI note is
   formally **re-homed as VCG-layer** or kept in place.

---

## Open decisions (to confirm before folding into the design)

- **R1 · Confirm the reframe direction** (Phase 1 = mechanical STEP application + residue surfacing; not AI
  meaning-derivation).
- **R2 · Single/multi-sense detector.** How a term is mechanically classified single vs multi-sense — the
  parsed-sense **row count undercounts** (one row often enumerates several senses). Likely signals: gloss
  split (the registry already splits `ya.re` G/H), sense_text enumeration, pole-span detection.
- **R3 · Where the terse Phase-1 meaning lives vs the VCG-layer rich meaning** — two fields (`analysis_note`
  terse + a new `vcg_meaning` rich), or reuse one and re-home?
- **R4 · Keyword spec** — exact STEP-capture format (sense tokens + sense id + pole), reconciled with
  `feedback_phase2_passa_emits_keywords` and the parked `[faculty][predicate]` finding.
- **R5 · Treatment of existing M01 notes** (retain as VCG-layer vs regenerate terse).
- **R6 · Pole assignment** — how much pole is mechanical (sense→pole map) vs judgement (metaphor like
  `mish.bar`).
- **R7 · Capture morphology + parse stem branches** (from the STEP exploration) — add `morph_code`/`stem`
  to `wa_verse_records` at extraction, and populate the waiting `wa_meaning_sense.stem_label` /
  `is_stem_label`, to enable Layer 0b. Detail + evidence:
  `research/investigations/wa-step-morphology-sense-disambiguation-v1-20260607.md`.

---

## Recommendation

Adopt the reframe in principle — it is well-supported by the M01 evidence and it **strengthens** the
existing design rather than replacing it (it makes L1/L2 concretely mechanical and pushes interpretation to
where the lexicon genuinely runs out). The cheapest validating next step is to **build the single/multi-sense
detector** and run it on M01, which converts R2 into a real number and shows exactly how large the
"advanced analysis" residue actually is — before committing any of this to the v3_1 instruction.
