# Tier Catalogue — Restructured (Two-Layer Slice) · v2 · 2026-06-11

> **Supersedes v1** ([`wa-tier-catalogue-restructured-v1-20260610.md`](archive/wa-tier-catalogue-restructured-v1-20260610.md)) and the original flat extract ([`wa-tier-questions-extract-v1-20260604.md`](wa-tier-questions-extract-v1-20260604.md)).
> **v2 adds the consolidated VE questions.** For each verse-extraction field, the originating tier questions are **analysed and merged into a single verse-level question that the field answers**, with **every combined aspect retained** (the multi-select option sets keep their glosses; only the cross-verse *reveal/pattern/over-time* clauses are routed to SYNTH, noted per field).
> **For approval — DB not yet modified.** Old T-codes remain the reference key (numbering expected to change); `VE-nn` IDs are provisional.

---

## 0. The two layers

| Layer | grain | what it is | where it lives |
|---|---|---|---|
| **A · Verse-Extraction (L1/L2)** | one typed term-in-verse | structured fields with **closed option-lists** — the *evidence*, state-not-induce (NONE/SILENT/not-stated first-class) | the L2 read → `finding` (l2_api) → **`v_l2_tier`** |
| **B · SYNTH** | characteristic / cross-verse / cross-term / cross-cluster | the *"what does X reveal"*, *over-time*, *pattern*, *relationship* questions — **computed by rolling up** Layer A | the synthesis pass |

Every old question is dispositioned **→ Layer A** · **SYNTH** · **DROP** · **DEFER** (§5 indexes all 189).

---

## 1. Layer A — Verse-Extraction fields, each as **one consolidated question**

Each block: **VE-id · field** — the single **consolidated verse-level question** (what the field answers) — option-list · `M/R` · live? — **originating old codes** (the questions merged) — **aspect(s) routed to SYNTH** (so nothing is lost).

### VE-01 · `sense_applied`
**Q — "Which specific sense of the primary Hebrew/Greek term is operative in this verse — the meaning it carries here, and where that sits within the term's semantic range?"**
- option-list: clean sense phrase · `M` · **live**
- merges: **T7.1.3** (semantic range) + the definitional read of the H/G term as used here (T1.1.2)
- → SYNTH: the full vocabulary arc & root-meaning synthesis (T7.1.1, T7.1.4–.10)

### VE-02 · `type`
**Q — "What kind of inner-being phenomenon is the term in this verse — an action (an act done), a status (a condition or disposition borne), or a quality (an attribute)?"**
- option-list: `action · status · quality` · `M` · **live**
- merges: **T1.2.1** (act / disposition / condition / quality — *disposition* and *condition* fold into `status`)

### VE-03 · `compound`
**Q — "Is the term, as it operates here, simple, or compound — does it appear with or as constituent elements, and if so which parts combine?"**
- option-list: `simple · compound:<parts>` · `R` · **live**
- merges: **T1.2.2** (simple vs constituent elements)

### VE-04 · `mode`
**Q — "In what mode does the term operate in this verse — its operative grammatical/stem form and the distinct manner in which it functions in the inner person here, including any context-, direction-, or constitutional-level dependence visible in the verse?"**
- option-list: short mode phrase · `M` · **live**
- merges: **T1.4.1** (the distinct way it operates — *this verse's instance*) + T1.4.2 (context/direction/level variation) + grammatical range (T7.1.2)
- → SYNTH: the full **mode-set** across the corpus (T1.4.1 as a roll-up), the speech-based mode (T1.4.3)

### VE-05 · `constitutional_location` *(multi)*
**Q — "Where, if anywhere, does this verse explicitly locate the term constitutionally — at the spirit level, the soul level, the heart, the mind, another soul-subset, or a specific body part (naming which) — recording every level evidenced, or NONE if unlocated?"**
- option-list: `spirit · soul · heart · mind · other-soul:<x> · body-part:<x> · NONE` · `M-keyword + R` · **live**
- merges: **T2.1.1** (spirit) · **T2.2.1** (soul) · **T2.3.1** (heart) · **T2.4.1** (mind) · **T2.5.1** (other soul-subset) · **T2.6.1** (specific body part)
- → SYNTH: what each location *reveals* (the `.2`s); spirit-origin/primacy (T2.1.2); constitutional movement across levels (T2.10); body↔soul direction (T2.7)

### VE-06 · `origin`
**Q — "Where does the term originate constitutionally in this verse — generated within the person, received from outside, bestowed by God, carried generationally [proposed: or from other spirits] — or not-stated?"**
- option-list: `within-person · received-from-outside · bestowed-by-God · carried-generationally · not-stated` (proposed `+ from-other-spirits`) · `R` · **live**
- merges: **T2.9.1** (within / from-outside / from-God / generational)
- → SYNTH: origin singular vs multiple (T2.9.2); origin changing across contexts (T2.9.3)

### VE-07 · `faculty` *(multi)*
**Q — "Which inner faculty(ies) does the term engage in this verse, and how — recording each that applies: perception (the inner senses — hearing, sight, taste, touch, smell — and spiritual discernment), cognition (knowing, understanding, discerning), memory (holding and retrieving inner reality across time), affect (feeling and emotional experience), creativity (imagination and the capacity to originate), volition (the capacity to choose), agency (the capacity to act, initiate, make happen), moral-evaluation (assessing against right, wrong, good, true), conscience (the inner witness of sin, guilt, conviction), or relational (the equipment for genuine connection with another) — or NONE?"**
- option-list: the 10 faculties above · `NONE` · `R` · **live**
- merges: **T3.1.1 · T3.2.1 · T3.3.1 · T3.4.1 · T3.5.1 · T3.6.1 · T3.7.1 · T3.8.1 · T3.9.1 · T3.11.1** (each "does it engage faculty X — and how", with its gloss retained verbatim above)
- → SYNTH: does it **enable / deepen / bypass / impair** each faculty (the `.2`s); what the pattern reveals (the `.3`s); **T3.10 Conscientiousness** (the integrated moral-awareness+volition+action composite — a roll-up of the primitives)

### VE-08 · `attributed_to_God`
**Q — "Is the term predicated of or related to God in this verse — yes or no — and if yes, how is it related to him here?"**
- option-list: `yes · no` (+ how-note) · `R` · **live**
- merges: **T0.1.2** (is it attributed to God) — de-forced from "…and what does that attribution reveal"
- → SYNTH: what the attribution / its silence reveals about the characteristic's significance in the human person and the divine image (T0.1.1, T0.1.2 clause 2, T0.1.3, T0.3.x)

### VE-09 · `purpose_equips`
**Q — "What does this verse indicate the term equips the person to be, do, or become — the purpose it serves here — or not-stated?"**
- option-list: text · `not-stated` · `R` · **live**
- merges: **T0.2.1** (purpose it serves; what it equips the person to be/do/become)
- → SYNTH: created-design vs response-to-the-fall (T0.2.2); orientation to future fullness (T0.2.3)

### VE-10 · `typology_direction`
**Q — "If this verse uses the term typologically, in which direction does the typology run — human→divine (the human instance pointing toward the divine) or divine→human (the divine instance establishing the pattern for the human) — or none?"**
- option-list: `human→divine · divine→human · none` · `R` · **live**
- merges: **T0.4.2** (direction) + T0.4.1 (is it typological, at the verse) + T0.4.3 (if none)
- → SYNTH: whether Scripture uses the characteristic typologically as a body (T0.4.1 across)

### VE-11 · `immediate_response`
**Q — "What is the first or most immediate inner-being response shown in this verse to encountering or bearing the term — or is the verse silent (SILENT)?"**
- option-list: text · `SILENT` · `R` · **live**
- merges: **T1.5.1** (first/most immediate inner response) + T1.5.3 (silence → `SILENT`)
- → SYNTH: whether the response is consistent or varies across the evidence (T1.5.2)

### VE-12 · `produces_effect`
**Q — "What does the term produce in the inner being in this verse — the effect it brings about here?"**
- option-list: text · `R` · **live**
- merges: **T1.6.1** (what it produces in the inner being — the verse's immediate effect)
- → SYNTH: the **sustained / over-time** effect and the states, qualities, capacities it establishes (T1.6.1 over-time, T1.6.2, T1.6.3)

### VE-13 · `relational_implication`
**Q — "What directional, relational, or constitutional implication or force does the term carry in this verse?"**
- option-list: text · `R` · **live**
- merges: **T1.1.3** (directional / relational / constitutional implications the term carries)

### VE-14 · `literary_setting`
**Q — "What literary form carries this verse — narrative, poetry/psalm, law, prophecy, wisdom, epistle, gospel, or apocalyptic — and, where evident, its contextual setting (judicial, liturgical, covenantal, communal, eschatological)?"**
- option-list: `narrative · poetry · law · prophecy · wisdom · epistle · gospel · apocalyptic …` · `R` · **live**
- merges: **T7.2.2** (literary form) + T7.2.4 (contextual setting)
- → SYNTH: what the form requires for responsible interpretation (T7.2.2 clause 2); the verse's function/argument/anchor (T7.2.1, T7.2.3, T7.2.5, T7.2.6)

### VE-15 · `relational_direction` *(multi — proposed)*
**Q — "In which relational direction does the term operate in this verse, and how — from God toward the person (divine→human), in the person's movement toward God (human→divine: seeking, supplication, worship, covenant), extended from one person to another (giving), received by a person from another (receiving), or in relation to other spiritual beings (angelic or adversarial) — recording each that applies, or NONE?"**
- option-list: `divine→human · human→divine · give · receive · spirit-beings · NONE` · `R` · **proposed (D4)**
- merges: **T4.1.1 · T4.2.1 · T4.3.1 · T4.4.1 · T4.6.1** (the interface `.1`s, each retained above)
- → SYNTH: the basis / disposition / inner-conditions of each interface (the `.2/.3`s); relational boundaries & scope (T4.5); adversarial-site & angelic-mediation (T4.6.2/.3)

### VE-16 · `suffering_context` *(flag — proposed)*
**Q — "Does this verse place the term in relation to suffering or affliction — and in what role: as a response to it, a product of it, or a context for it — or NONE?"**
- option-list: `response · product · context · NONE` · `R` · **proposed**
- merges: **T5.4.1**
- → SYNTH: does suffering deepen / test / reveal / produce it (T5.4.2)

### VE-17 · `co_occurrence_array` *(proposed)*
**Q — "Which other in-scope inner-being terms co-occur with this one in this verse (the verse's term-array)?"**
- format: list of co-occurring typed terms · auto from the verse-complete read · **proposed**
- merges: **T6.1.1**
- → SYNTH: the co-occurrence **pattern** and what it reveals (T6.1.2/.3); the **typed** relationship between co-occurring terms is a separate gap (see verse-extraction-gaps reflection)

> **Cross-reference is exact and live in the DB:** every `l2_api` finding links to its old code via `finding_question_link → wa_obs_question_catalogue.question_code` (the `v_l2_tier.question_code` column). VE-05/07/15 are multi-select — each present value is one linked finding; absence = `NONE`.

---

## 2. Layer B — SYNTH (roll-up / relationship / dynamic)

Computed across verses / terms / clusters; never asked at the verse. Grouped by old tier (codes are the reference; final SYNTH numbering TBD). "Fed by" names the Layer-A field(s) the roll-up consumes.

| old code(s) | SYNTH question (de-forced where noted) | fed by |
|---|---|---|
| T0.1.1 · T0.1.3 | What the God-attribution / its silence reveals about the characteristic's nature & divine-image significance | VE-08 |
| T0.2.2 · T0.2.3 | Original-design vs response-to-the-fall; orientation to future fullness | VE-09, VE-12 |
| T0.3.1–.3 | Image-bearer expression — how it instantiates the divine likeness; shared vs analogue; presence/absence & image condition | VE-08, corpus |
| T0.4.1 | Whether Scripture uses the characteristic typologically at all | VE-10 |
| T1.1.1 · T1.1.2 | Programme name & what it signals; definitional read of the H/G terms | VE-01 across |
| T1.3.1–.3 | Boundary — structural opposite; what it excludes/resists; where it ends | VE-01, vocabulary |
| T1.4.1 · T1.4.3 | The full **mode-set**; the speech-based mode | VE-04 across |
| T1.5.2 | Is the immediate response consistent or variable? | VE-11 across |
| T1.6.2 · T1.6.3 | States/qualities established over time; sustained vs immediate | VE-12 across |
| T1.7.1–.3 | Conditions of reception — enabling / blocking / non-receiver state | VE-09, VE-12, corpus |
| T2.1.2/.3 · T2.2.2 · T2.3.2 · T2.4.2 · T2.5.2 · T2.6.2 | What each location **reveals** | VE-05 across |
| T2.7.1/.2 | Body↔soul direction & consequence | VE-05 (body) |
| T2.9.2/.3 | Origin singular vs multiple; origin changing across contexts | VE-06 across |
| T2.10.1–.3 | Constitutional **movement** across levels | VE-05 across |
| T3.x.2 (×11) | Does it **enable / deepen / bypass / impair** faculty X? | VE-07 across |
| T3.x.3 (×11) | What the **pattern** of engagement reveals | VE-07 across |
| T3.10.1–.3 | **Conscientiousness** (integrated composite) | VE-07 (affect/volition/agency/moral-eval/conscience) |
| T4.1–4.4 .2/.3 · T4.5.x · T4.6.2/.3 | Basis / disposition / conditions of each interface; relational scope; adversarial & angelic | VE-13, VE-15 |
| T5.1.x · T5.2.x · T5.3.x | Nature of transformation; sequence of inner states; mechanism of change | VE-11, VE-12 across |
| T5.4.2/.3 | Does suffering deepen/test/reveal/produce it? | VE-16 across |
| T5.5.x · T5.6.x | Formation & sanctification arc; eschatological trajectory | VE-09, VE-12 across |
| T6.1.2/.3 | Co-occurrence pattern & what it reveals | VE-17 across |
| T6.2.x · T6.3.x · T6.4.x · T6.5.x | Sequential / causal-constitutive / vocabulary-root / distinction relationships | VE-12, VE-17, VE-01 |
| T7.1.1/.2 · T7.1.4–.10 | Primary terms & root meanings; grammatical range; the full vocabulary arc | VE-01, VE-04 across |
| T7.2.1 · T7.2.3 · T7.2.5 · T7.2.6 | Function in verse; argument structure; primary anchor & what it uniquely reveals | VE-14, corpus |

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

**Defer (not dropped):** **T7.3.1–.4** Human Science Frameworks — external lens, not inner-being verse evidence; revisited in synthesis.

---

## 4. DE-FORCE — forcing questions rephrased to neutral checks (silence first-class)

The tell is *"what does X reveal / suggest"* or *"in what way does it express Z"* — these prompt a finding that may not exist. Rephrased to *"is there evidence of X here? — record it; if not, silent."* The verse check lands in a Layer-A field (now the consolidated question above); the original "reveal" becomes SYNTH.

| old code | original (forcing) | de-forced verse check → field |
|---|---|---|
| T0.1.2 | "what does the attribution reveal about its significance…" | **Is the term related to God here?** → VE-08 |
| T0.2.2 | "original design *or* response to the fall?" | **note only if the verse states a purpose** → VE-09 |
| T0.3.1/.3 | "in what way does it express the divine image… presence/absence reveal" | **Does the verse tie the term to the image of God?** (rare) → SYNTH |
| T2.x.2 | "what does X-location reveal" | **Is it located at X here?** → VE-05 |
| T3.x.2 | "does it enable/deepen/bypass/impair faculty X" | **Which faculty(ies) does it engage here?** → VE-07 |
| T3.x.3 · T1.5.2 · T1.6.x | "what does the pattern reveal" | — (SYNTH only) |
| T5.4.x | "does suffering deepen/test/reveal/produce it" | **Does the verse place the term in suffering?** (+ role) → VE-16 |

---

## 5. Complete disposition index — all 189 old questions accounted for

`→VE-nn` = Layer A · `SYNTH` = Layer B · `DROP` · *(folds = the `.x "if silent, note"` sub-question folds into its field's NONE/SILENT token)*.

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
| T1.4.2 / .3 | **→VE-04** / SYNTH | | T6.1.1 | **→VE-17** (proposed) |
| T1.5.1 | **→VE-11** | | T6.1.2 / .3 | SYNTH |
| T1.5.2 / .3 | SYNTH / folds | | T6.2.x · T6.3.x · T6.4.x · T6.5.x | SYNTH |
| T1.6.1 | **→VE-12** | | T6.6.1–.3 | **DROP** |
| T1.6.2 / .3 | SYNTH | | T6.7.1–.3 | **DROP** |
| T1.7.1–.3 | SYNTH | | T7.1.3 | **→VE-01** |
| T1.8.1–.3 | **DROP** | | T7.1.1 / .2 | SYNTH (VE-01/04 feed) |
| T2.1.1 / .2 / .3 / .4 | **→VE-05** / SYNTH / SYNTH / folds | | T7.1.4–.10 | SYNTH |
| T2.2.1 / .2 / .3 | **→VE-05** / SYNTH / folds | | T7.2.1 | SYNTH |
| T2.3.1 / .2 / .3 | **→VE-05** / SYNTH / folds | | T7.2.2 | **→VE-14** |
| T2.4.1 / .2 / .3 | **→VE-05** / SYNTH / folds | | T7.2.3 / .5 / .6 | SYNTH |
| T2.5.1 / .2 / .3 | **→VE-05** (other-soul) / SYNTH / folds | | T7.2.4 | **→VE-14** (setting) |
| | | | T7.3.1–.4 | **DEFER** |

**Tally:** of 189 — **14 → Layer A (implemented, each now one consolidated question)** · **+3 proposed (VE-15/16/17)** · **~118 → SYNTH** · **18 DROP** · **4 DEFER** · the `.x "if silent"` sub-questions **fold** into null tokens.

---

## 6. Open decisions (for your markup)

| # | decision | recommendation |
|---|---|---|
| **D1** | Confirm the **DROP** list (T1.2.3, T1.8, T2.8, T5.7, T6.6, T6.7) | adopt |
| **D2** | `origin` **+ `from-other-spirits`** (VE-06) | adopt — real constitutional source, currently excluded |
| **D3** | `faculty` as the per-term multi-select from the 10 (T3 restructure); T3.10 Conscientiousness stays SYNTH-composite | adopt (already live) |
| **D4** | `constitutional_location` level list (VE-05) **+** `relational_direction` (VE-15) as a verse field vs SYNTH | confirm levels; recommend VE-15 **as a verse field** |
| **D5** | Confirm the **M/R** split per §1 | per the `M/R` tags |
| **D6** | New numbering — keep T-codes, or assign `VE-nn` + `S-…`? | retain old T-codes as the reference key; assign new IDs on sign-off |
| **D7** *(new)* | Approve the **consolidated VE questions** in §1 as *the* verse-level questions the read answers | review wording; these supersede asking the originating sub-questions individually |

---

### Provenance
- Supersedes: `wa-tier-catalogue-restructured-v1-20260610.md` (no consolidated questions) and `wa-tier-questions-extract-v1-20260604.md` (flat 189).
- Designs applied: `wa-verse-level-extraction-spec-v1-20260609.md`, `wa-catalogue-refit-two-layer-v1-20260609.md`; gaps flagged in `wa-verse-extraction-gaps-v1-20260610.md` (cause-side fields are a *separate, additive* proposal, not folded here).
- Live cross-reference: VE-01..14 ↔ old codes are linked in the DB via `finding_question_link`; queryable through `v_l2_tier.question_code`.
- **DB unchanged.** On approval: migration to tag `wa_obs_question_catalogue` with `layer` (A/SYNTH/DROP/DEFER), store each VE's consolidated question + its originating-code set, and apply the de-force rewordings.
