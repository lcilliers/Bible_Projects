# Tier Catalogue — Restructured (Two-Layer Slice) · v2 · 2026-06-11

> **Supersedes v1** ([`wa-tier-catalogue-restructured-v1-20260610.md`](archive/wa-tier-catalogue-restructured-v1-20260610.md)) and the original flat extract ([`wa-tier-questions-extract-v1-20260604.md`](wa-tier-questions-extract-v1-20260604.md)).
> **v2 adds the consolidated VE questions + the full source-question text.** For each verse-extraction field, the originating tier questions are **analysed and merged into a single verse-level question that the field answers**, with **every combined aspect retained**. Each block now also quotes the **originating tier questions in full** so the consolidation can be evaluated against its source as a whole. Only the cross-verse *reveal/pattern/over-time* clauses route to SYNTH (noted per field).
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

Each block: **VE-id · field** — the single **consolidated verse-level question** (what the field answers) — option-list · `M/R` · live? — the **originating tier questions in full** (the questions merged) — **aspect(s) routed to SYNTH** (so nothing is lost).

**On `M` and `R` — how each field's value is obtained (this is what D5 asks you to confirm):**
- **`M` (mechanical)** — the value can be **pre-filled by the L1 layer without the interpretive read**: from STEP **morphology** (stem/part-of-speech), the **lexicon / sense data**, and **keyword** matching. So `type` and `mode` come from morphology, `sense_applied` from the lexical sense, and `constitutional_location` is seeded by body/seat keywords. A verse where the in-scope evidence is fully covered by `M` fields can be **accepted mechanically — no read/API call needed** (the cheap path).
- **`R` (read)** — the value **requires reading the verse and its surrounding context and deriving meaning**; it cannot be inferred from morphology alone: `origin`, `attributed_to_God`, `purpose_equips`, `typology_direction`, `immediate_response`, `produces_effect`, `relational_implication`, plus confirmation of the multi-selects (`faculty`, `location`).
- **Why it matters:** the M/R tag of each field *is* the **mechanical-vs-read triage** — it decides which verses auto-fill and which must go to the read, and so drives cost. (`M-keyword + R` on `constitutional_location` means: keyword pre-fills a candidate, the read confirms/corrects it.)

### VE-01 · `sense_applied`
**Q — "Which specific sense of the primary Hebrew/Greek term is operative in this verse — the meaning it carries here, and where that sits within the term's semantic range?"**
- option-list: clean sense phrase · `M` · **live**
- **merges — the originating tier questions in full:**
    - **T7.1.3** — "What is the semantic range of the primary term — across what breadth of meaning does it operate?"
    - **T1.1.2** — "What do the primary Hebrew and Greek terms reveal at the definitional level — before deeper lexical analysis begins?"
- → SYNTH: the full vocabulary arc & root-meaning synthesis (T7.1.1, T7.1.4–.10)

### VE-02 · `type`
**Q — "What kind of inner-being phenomenon is the term in this verse — an action (an act done), a status (a condition or disposition borne), or a quality (an attribute)?"**
- option-list: `action · status · quality` · `M` · **live**
- **merges — the originating tier question in full:**
    - **T1.2.1** — "What kind of inner-being phenomenon does this characteristic appear to be — an act, a disposition, a condition, a quality, or something else?" *(act → `action`; disposition + condition → `status`; quality → `quality`)*

### VE-03 · `compound`
**Q — "Is the term, as it operates here, simple, or compound — does it appear with or as constituent elements, and if so which parts combine?"**
- option-list: `simple · compound:<parts>` · `R` · **live**
- **merges — the originating tier question in full:**
    - **T1.2.2** — "Is this characteristic simple in structure or does it appear to have constituent elements at first encounter?"

### VE-04 · `mode`
**Q — "In what mode does the term operate in this verse — its operative grammatical/stem form and the distinct manner in which it functions in the inner person here, including any context-, direction-, or constitutional-level dependence visible in the verse?"**
- option-list: short mode phrase · `M` · **live**
- **merges — the originating tier questions in full:**
    - **T1.4.1** — "In what distinct ways does this characteristic operate within the inner person?" *(the verse's instance)*
    - **T1.4.2** — "Does this characteristic operate differently depending on context, direction, or constitutional level?"
    - **T7.1.2** — "What is the grammatical range of the primary term (noun, verb, adjective, participle) — and what does that range reveal about how the characteristic operates?"
- → SYNTH: the full **mode-set** across the corpus (T1.4.1 as a roll-up), the speech-based mode (T1.4.3)

### VE-05 · `constitutional_location` *(multi)*
**Q — "Where, if anywhere, does this verse explicitly locate the term constitutionally — at the spirit level, the soul level, the heart, the mind, another soul-subset, or a specific body part (naming which) — recording every level evidenced, or NONE if unlocated?"**
- option-list: `spirit · soul · heart · mind · other-soul:<x> · body-part:<x> · NONE` · `M-keyword + R` · **live**
- **merges — the originating tier questions in full:**
    - **T2.1.1** — "Is this characteristic explicitly located at the spirit level in the verse evidence?"
    - **T2.2.1** — "Is this characteristic identified in the verse evidence as a soul-level phenomenon?"
    - **T2.3.1** — "Does the verse evidence locate this characteristic in the heart?"
    - **T2.4.1** — "Does the verse evidence locate this characteristic in the mind?"
    - **T2.5.1** — "Does the verse evidence surface any soul-level location beyond heart and mind for this characteristic?"
    - **T2.6.1** — "Does the verse evidence link this characteristic to a specific body part?"
- → SYNTH: what each location *reveals* (the `.2`s); spirit-origin/primacy (T2.1.2); constitutional movement across levels (T2.10); body↔soul direction (T2.7)

### VE-06 · `origin`
**Q — "Where does the term originate constitutionally in this verse — generated within the person, received from outside, bestowed by God, carried generationally [proposed: or from other spirits] — or not-stated?"**
- option-list: `within-person · received-from-outside · bestowed-by-God · carried-generationally · not-stated` (proposed `+ from-other-spirits`) · `R` · **live**
- **merges — the originating tier question in full:**
    - **T2.9.1** — "Where does this characteristic originate constitutionally — is it generated from within the person, received from outside, bestowed by God, or carried generationally?"
- → SYNTH: origin singular vs multiple (T2.9.2); origin changing across contexts (T2.9.3)

### VE-07 · `faculty` *(multi)*
**Q — "Which inner faculty(ies) does the term engage in this verse, and how — recording each that applies: perception (the inner senses — hearing, sight, taste, touch, smell — and spiritual discernment), cognition (knowing, understanding, discerning), memory (holding and retrieving inner reality across time), affect (feeling and emotional experience), creativity (imagination and the capacity to originate), volition (the capacity to choose), agency (the capacity to act, initiate, make happen), moral-evaluation (assessing against right, wrong, good, true), conscience (the inner witness of sin, guilt, conviction), or relational (the equipment for genuine connection with another) — or NONE?"**
- option-list: the 10 faculties above · `NONE` · `R` · **live**
- **merges — the originating tier questions in full:**
    - **T3.1.1** — "Does this characteristic engage the perceptive faculty — the inner senses including hearing, sight, taste, touch, smell, and spiritual discernment — and if so, which inner sense and how?"
    - **T3.2.1** — "Does this characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how?"
    - **T3.3.1** — "Does this characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how?"
    - **T3.4.1** — "Does this characteristic engage the affective faculty — feeling and emotional experience — and if so, how?"
    - **T3.5.1** — "Does this characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how?"
    - **T3.6.1** — "Does this characteristic engage the volitional faculty — the capacity to choose — and if so, how?"
    - **T3.7.1** — "Does this characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how?"
    - **T3.8.1** — "Does this characteristic engage the moral evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how?"
    - **T3.9.1** — "Does this characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how?"
    - **T3.11.1** — "Does this characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how?"
- → SYNTH: does it **enable / deepen / bypass / impair** each faculty (the `.2`s); what the pattern reveals (the `.3`s); **T3.10 Conscientiousness** (the integrated moral-awareness+volition+action composite — a roll-up of the primitives)

### VE-08 · `attributed_to_God`
**Q — "Is the term predicated of or related to God in this verse — yes or no — and if yes, how is it related to him here?"**
- option-list: `yes · no` (+ how-note) · `R` · **live**
- **merges — the originating tier question in full:**
    - **T0.1.2** — "Does Scripture explicitly attribute this characteristic to God — and if so, what does that attribution reveal about its significance in the human person?" *(verse answers the attribution; the "reveal" clause → SYNTH)*
- → SYNTH: what the attribution / its silence reveals about the characteristic's significance in the human person and the divine image (T0.1.1, T0.1.2 clause 2, T0.1.3, T0.3.x)

### VE-09 · `purpose_equips`
**Q — "What does this verse indicate the term equips the person to be, do, or become — the purpose it serves here — or not-stated?"**
- option-list: text · `not-stated` · `R` · **live**
- **merges — the originating tier question in full:**
    - **T0.2.1** — "What does the verse evidence suggest about the purpose this characteristic serves in the human person as created — what does it equip the person to be, do, or become?"
- → SYNTH: created-design vs response-to-the-fall (T0.2.2); orientation to future fullness (T0.2.3)

### VE-10 · `typology_direction`
**Q — "If this verse uses the term typologically, in which direction does the typology run — human→divine (the human instance pointing toward the divine) or divine→human (the divine instance establishing the pattern for the human) — or none?"**
- option-list: `human→divine · divine→human · none` · `R` · **live**
- **merges — the originating tier questions in full:**
    - **T0.4.2** — "If typological use is present, what is the direction of the typology — does the human instance point toward the divine, or does the divine instance establish the pattern for the human?"
    - **T0.4.1** — "Does Scripture use this characteristic typologically — deploying it to point toward or participate in a reality beyond the immediate (covenantal, eschatological, christological)?" *(at the verse: is it typological here)*
    - **T0.4.3** — "If no typological use is evidenced, note this explicitly." *(→ `none`)*
- → SYNTH: whether Scripture uses the characteristic typologically as a body (T0.4.1 across)

### VE-11 · `immediate_response`
**Q — "What is the first or most immediate inner-being response shown in this verse to encountering or bearing the term — or is the verse silent (SILENT)?"**
- option-list: text · `SILENT` · `R` · **live**
- **merges — the originating tier questions in full:**
    - **T1.5.1** — "What is the first or most immediate inner-being response to receiving or encountering this characteristic?"
    - **T1.5.3** — "Where the verse evidence is silent on immediate response, note this explicitly." *(→ `SILENT`)*
- → SYNTH: whether the response is consistent or varies across the evidence (T1.5.2)

### VE-12 · `produces_effect`
**Q — "What does the term produce in the inner being in this verse — the effect it brings about here?"**
- option-list: text · `R` · **live**
- **merges — the originating tier question in full:**
    - **T1.6.1** — "What does this characteristic produce in the inner being over time?" *(verse captures the immediate effect; the over-time roll-up → SYNTH)*
- → SYNTH: the **sustained / over-time** effect and the states, qualities, capacities it establishes (T1.6.1 over-time, T1.6.2, T1.6.3)

### VE-13 · `relational_implication`
**Q — "What directional, relational, or constitutional implication or force does the term carry in this verse?"**
- option-list: text · `R` · **live**
- **merges — the originating tier question in full:**
    - **T1.1.3** — "Does the name carry directional, relational, or constitutional implications that orient the enquiry from the outset?"

### VE-14 · `literary_setting`
**Q — "What literary form carries this verse — narrative, poetry/psalm, law, prophecy, wisdom, epistle, gospel, or apocalyptic — and, where evident, its contextual setting (judicial, liturgical, covenantal, communal, eschatological)?"**
- option-list: `narrative · poetry · law · prophecy · wisdom · epistle · gospel · apocalyptic …` · `R` · **live**
- **merges — the originating tier questions in full:**
    - **T7.2.2** — "What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic) — and what does that form require for responsible interpretation?" *(the "requires for interpretation" clause → SYNTH)*
    - **T7.2.4** — "What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological) — and what does that setting reveal?"
- → SYNTH: what the form requires for responsible interpretation (T7.2.2 clause 2); the verse's function/argument/anchor (T7.2.1, T7.2.3, T7.2.5, T7.2.6)

### VE-15 · `relational_direction` *(multi — proposed)*
**Q — "In which relational direction does the term operate in this verse, and how — from God toward the person (divine→human), in the person's movement toward God (human→divine: seeking, supplication, worship, covenant), extended from one person to another (giving), received by a person from another (receiving), or in relation to other spiritual beings (angelic or adversarial) — recording each that applies, or NONE?"**
- option-list: `divine→human · human→divine · give · receive · spirit-beings · NONE` · `R` · **proposed (D4)**
- **merges — the originating tier questions in full:**
    - **T4.1.1** — "Does the verse evidence show this characteristic operating from God toward the human person — and if so, how?"
    - **T4.2.1** — "Does the verse evidence show this characteristic operating in the human person's movement toward God — in seeking, supplication, worship, or covenant — and if so, how?"
    - **T4.3.1** — "Does the verse evidence show this characteristic being extended by one person toward another — and if so, how does it operate in that giving?"
    - **T4.4.1** — "Does the verse evidence show this characteristic being received by a person from another — and if so, how does it operate in that reception?"
    - **T4.6.1** — "Does the verse evidence show this characteristic operating in relation to other spiritual beings — angelic or adversarial — and if so, how?"
- → SYNTH: the basis / disposition / inner-conditions of each interface (the `.2/.3`s); relational boundaries & scope (T4.5); adversarial-site & angelic-mediation (T4.6.2/.3)

### VE-16 · `suffering_context` *(flag — proposed)*
**Q — "Does this verse place the term in relation to suffering or affliction — and in what role: as a response to it, a product of it, or a context for it — or NONE?"**
- option-list: `response · product · context · NONE` · `R` · **proposed**
- **merges — the originating tier question in full:**
    - **T5.4.1** — "Does the verse evidence show this characteristic operating in relation to suffering or affliction — as a response to it, a product of it, or a context for it?"
- → SYNTH: does suffering deepen / test / reveal / produce it (T5.4.2)

### VE-17 · `co_occurrence_array` *(proposed)*
**Q — "Which other in-scope inner-being terms co-occur with this one in this verse (the verse's term-array)?"**
- format: list of co-occurring typed terms · auto from the verse-complete read · **proposed**
- **merges — the originating tier question in full:**
    - **T6.1.1** — "Which adjacent characteristics appear most frequently alongside this one in the verse evidence?"
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

> **Layout note:** this is a **two-up table** — `old code | disposition` is repeated as a second pair of columns purely to fit all the rows on one screen without a very long single column. Read the **left pair top-to-bottom, then the right pair** (the blank middle column is just the separator). It is one list, not two.

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
| **D5** | Confirm the **M/R (mechanical / read)** split per §1 — see the *"On M and R"* note for how each is obtained | per the `M/R` tags; the split is the mechanical-vs-read triage and drives cost |
| **D6** | New numbering — keep T-codes, or assign `VE-nn` + `S-…`? | retain old T-codes as the reference key; assign new IDs on sign-off |
| **D7** | Approve the **consolidated VE questions** in §1 as *the* verse-level questions the read answers | review wording against the now-embedded source text; these supersede asking the originating sub-questions individually |

---

## 7. Appendix A — Exact tier extract from the database (verbatim, all 189)

> Pulled unmodified from `wa_obs_question_catalogue` (`deleted=0` AND tier set), 2026-06-11, schema 3.31.0. **189 questions.** This is the ground-truth source for the restructure in sections 1-5 above; nothing here is edited. `obs_id` is the DB key; `question_code` (Tn.c.q) is the reference used throughout this document.

### T0 — Divine Image and Created Design

**T0.1 · Divine Nature Reflected**

- **T0.1.1** *(obs 224)* — What does the verse evidence reveal about the nature or character of God that this characteristic reflects or images?
- **T0.1.2** *(obs 225)* — Does Scripture explicitly attribute this characteristic to God — and if so, what does that attribution reveal about its significance in the human person?
- **T0.1.3** *(obs 226)* — Where Scripture is silent about God's possession of this characteristic, what does that silence suggest about the characteristic's place in the divine image?

**T0.2 · Created Purpose**

- **T0.2.1** *(obs 227)* — What does the verse evidence suggest about the purpose this characteristic serves in the human person as created — what does it equip the person to be, do, or become?
- **T0.2.2** *(obs 228)* — Does the evidence indicate whether this characteristic is part of the original created design, a response to the fallen condition, or both?
- **T0.2.3** *(obs 229)* — Is there evidence that this characteristic is oriented toward a future fullness — something the person is moving toward, not only what they currently are?

**T0.3 · Image-Bearer Expression**

- **T0.3.1** *(obs 230)* — In what way does this characteristic express the divine image in the human person — what aspect of being made in God's likeness does it instantiate?
- **T0.3.2** *(obs 231)* — Does the evidence suggest that this characteristic is shared between God and the human person, or is it exclusively a creaturely analogue to something in God?
- **T0.3.3** *(obs 232)* — What does the presence or absence of this characteristic in a person reveal about the condition of the divine image in that person?

**T0.4 · Typological Significance**

- **T0.4.1** *(obs 233)* — Does Scripture use this characteristic typologically — deploying it to point toward or participate in a reality beyond the immediate (covenantal, eschatological, christological)?
- **T0.4.2** *(obs 234)* — If typological use is present, what is the direction of the typology — does the human instance point toward the divine, or does the divine instance establish the pattern for the human?
- **T0.4.3** *(obs 235)* — If no typological use is evidenced, note this explicitly.
### T1 — Definition

**T1.1 · Name and Naming**

- **T1.1.1** *(obs 236)* — What is this characteristic called in the programme — and what does the name itself signal about its essential nature?
- **T1.1.2** *(obs 237)* — What do the primary Hebrew and Greek terms reveal at the definitional level — before deeper lexical analysis begins?
- **T1.1.3** *(obs 238)* — Does the name carry directional, relational, or constitutional implications that orient the enquiry from the outset?

**T1.2 · Kind**

- **T1.2.1** *(obs 239)* — What kind of inner-being phenomenon does this characteristic appear to be — an act, a disposition, a condition, a quality, or something else?
- **T1.2.2** *(obs 240)* — Is this characteristic simple in structure or does it appear to have constituent elements at first encounter?
- **T1.2.3** *(obs 241)* — What is the current best working description of this characteristic — encapsulating its constitutional location, the faculties it primarily engages, and its impact on the person?

**T1.3 · Boundary**

- **T1.3.1** *(obs 242)* — What is the structural opposite of this characteristic — the inner-being reality that stands against or excludes it?
- **T1.3.2** *(obs 243)* — What does this characteristic explicitly exclude or resist?
- **T1.3.3** *(obs 244)* — What is this characteristic not — where does it end and something else begin?

**T1.4 · Modes of Operation**

- **T1.4.1** *(obs 245)* — In what distinct ways does this characteristic operate within the inner person?
- **T1.4.2** *(obs 246)* — Does this characteristic operate differently depending on context, direction, or constitutional level?
- **T1.4.3** *(obs 247)* — Does this characteristic have a communicative or speech-based mode of operation — and if so, how does it function?

**T1.5 · Immediate Response**

- **T1.5.1** *(obs 248)* — What is the first or most immediate inner-being response to receiving or encountering this characteristic?
- **T1.5.2** *(obs 249)* — Is the immediate response consistent across the verse evidence, or does it vary?
- **T1.5.3** *(obs 250)* — Where the verse evidence is silent on immediate response, note this explicitly.

**T1.6 · Sustained Effect**

- **T1.6.1** *(obs 251)* — What does this characteristic produce in the inner being over time?
- **T1.6.2** *(obs 252)* — What states, qualities, capacities, or orientations does sustained exposure to or possession of this characteristic establish?
- **T1.6.3** *(obs 253)* — Does the sustained effect differ from the immediate response — and if so, how?

**T1.7 · Conditions of Reception**

- **T1.7.1** *(obs 254)* — What inner conditions or orientations enable genuine reception of this characteristic?
- **T1.7.2** *(obs 255)* — What inner conditions block, distort, or prevent reception?
- **T1.7.3** *(obs 256)* — What is the inner-being state of the person who encounters this characteristic but does not receive it?

**T1.8 · Dimension Classification**

- **T1.8.1** *(obs 257)* — What is the primary inner-being dimension of this characteristic from the programme's dimension vocabulary?
- **T1.8.2** *(obs 258)* — What evidence from the verse evidence supports this classification?
- **T1.8.3** *(obs 259)* — Does this characteristic carry secondary dimensions — and if so, what are they, and do they compete with the primary classification?
### T2 — Constitutional Location and Boundaries

**T2.1 · Spirit-Level Location**

- **T2.1.1** *(obs 260)* — Is this characteristic explicitly located at the spirit level in the verse evidence?
- **T2.1.2** *(obs 261)* — Does the evidence indicate that this characteristic originates in or is primarily a spirit-level phenomenon?
- **T2.1.3** *(obs 262)* — What does spirit-level location reveal about the nature and depth of this characteristic?
- **T2.1.4** *(obs 263)* — If the evidence is silent on spirit-level location, note this explicitly.

**T2.2 · Soul-Level Location**

- **T2.2.1** *(obs 264)* — Is this characteristic identified in the verse evidence as a soul-level phenomenon?
- **T2.2.2** *(obs 265)* — What does soul-level location reveal about this characteristic's place in the innermost personal experience?
- **T2.2.3** *(obs 266)* — If the evidence is silent on soul-level location, note this explicitly.

**T2.3 · Heart**

- **T2.3.1** *(obs 267)* — Does the verse evidence locate this characteristic in the heart?
- **T2.3.2** *(obs 268)* — What does the heart-location reveal — what aspect of the heart's integrating function (knowing, willing, feeling, moral awareness) does this characteristic engage?
- **T2.3.3** *(obs 269)* — If the evidence is silent on heart-location, note this explicitly.

**T2.4 · Mind**

- **T2.4.1** *(obs 270)* — Does the verse evidence locate this characteristic in the mind?
- **T2.4.2** *(obs 271)* — What does mind-location reveal — what aspect of the mind's function (thought, discernment, understanding) does this characteristic engage?
- **T2.4.3** *(obs 272)* — If the evidence is silent on mind-location, note this explicitly.

**T2.5 · Other Soul Subsets**

- **T2.5.1** *(obs 273)* — Does the verse evidence surface any soul-level location beyond heart and mind for this characteristic?
- **T2.5.2** *(obs 274)* — If so, what is that location, and what does it reveal?
- **T2.5.3** *(obs 275)* — If the evidence is silent, note this explicitly.

**T2.6 · Body — Significance**

- **T2.6.1** *(obs 276)* — Does the verse evidence link this characteristic to a specific body part?
- **T2.6.2** *(obs 277)* — If so, what is Scripture doing by making that link — is it emphatic, functional, expressive, indicative, or mediating?
- **T2.6.3** *(obs 278)* — If no body-part link is evidenced, note this explicitly.

**T2.7 · Body — Direction**

- **T2.7.1** *(obs 279)* — Where a body-characteristic link exists, which direction does it run — does the soul express through the body, does the body feed back to the soul, or does it run in both directions?
- **T2.7.2** *(obs 280)* — What is the consequence of that directionality for understanding the characteristic?
- **T2.7.3** *(obs 281)* — If no body-characteristic link is evidenced, note this explicitly.

**T2.8 · Body — Deposit**

- **T2.8.1** *(obs 282)* — Does sustained operation of this characteristic leave a constitutional deposit in the body or its design — including DNA or generational consequence?
- **T2.8.2** *(obs 283)* — What evidence supports or contradicts this?
- **T2.8.3** *(obs 284)* — If the evidence is silent, note this explicitly. This finding feeds directly into T5.7.

**T2.9 · Origin and Source**

- **T2.9.1** *(obs 285)* — Where does this characteristic originate constitutionally — is it generated from within the person, received from outside, bestowed by God, or carried generationally?
- **T2.9.2** *(obs 286)* — What does the evidence reveal about whether the origin is singular or multiple?
- **T2.9.3** *(obs 287)* — Does the origin of this characteristic change across different contexts evidenced in Scripture?

**T2.10 · Constitutional Movement**

- **T2.10.1** *(obs 288)* — Does this characteristic move across constitutional levels — from spirit to soul, from soul to body, or across boundaries in other directions?
- **T2.10.2** *(obs 289)* — What does the evidence reveal about the sequence or pattern of that movement?
- **T2.10.3** *(obs 290)* — If no constitutional movement is evidenced, note this explicitly.
### T3 — The Inner Faculties

**T3.1 · Perception**

- **T3.1.1** *(obs 291)* — Does this characteristic engage the perceptive faculty — the inner senses including hearing, sight, taste, touch, smell, and spiritual discernment — and if so, which inner sense and how?
- **T3.1.2** *(obs 292)* — Does this characteristic enable, deepen, bypass, or impair the perceptive faculty in the person?
- **T3.1.3** *(obs 293)* — What does the pattern of engagement or non-engagement with perception reveal about the nature of this characteristic?

**T3.2 · Cognition**

- **T3.2.1** *(obs 294)* — Does this characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how?
- **T3.2.2** *(obs 295)* — Does this characteristic enable, deepen, bypass, or impair cognition in the person?
- **T3.2.3** *(obs 296)* — What does the pattern of engagement or non-engagement with cognition reveal about the nature of this characteristic?

**T3.3 · Memory**

- **T3.3.1** *(obs 297)* — Does this characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how?
- **T3.3.2** *(obs 298)* — Does this characteristic enable, deepen, bypass, or impair memory in the person?
- **T3.3.3** *(obs 299)* — What does the pattern of engagement or non-engagement with memory reveal about the nature of this characteristic?

**T3.4 · Affect**

- **T3.4.1** *(obs 300)* — Does this characteristic engage the affective faculty — feeling and emotional experience — and if so, how?
- **T3.4.2** *(obs 301)* — Does this characteristic enable, deepen, bypass, or impair affect in the person?
- **T3.4.3** *(obs 302)* — What does the pattern of engagement or non-engagement with affect reveal about the nature of this characteristic?

**T3.5 · Creativity**

- **T3.5.1** *(obs 303)* — Does this characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how?
- **T3.5.2** *(obs 304)* — Does this characteristic enable, deepen, bypass, or impair creativity in the person?
- **T3.5.3** *(obs 305)* — What does the pattern of engagement or non-engagement with creativity reveal about the nature of this characteristic?

**T3.6 · Volition**

- **T3.6.1** *(obs 306)* — Does this characteristic engage the volitional faculty — the capacity to choose — and if so, how?
- **T3.6.2** *(obs 307)* — Does this characteristic enable, deepen, bypass, or impair volition in the person — including its three aspects: capacity, interaction with other characteristics, and the constraints under which it operates?
- **T3.6.3** *(obs 308)* — What does the pattern of engagement or non-engagement with volition reveal about the nature of this characteristic?

**T3.7 · Agency**

- **T3.7.1** *(obs 309)* — Does this characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how?
- **T3.7.2** *(obs 310)* — Does this characteristic enable, deepen, bypass, or impair agency in the person?
- **T3.7.3** *(obs 311)* — What does the pattern of engagement or non-engagement with agency reveal about the nature of this characteristic?

**T3.8 · Moral Evaluation**

- **T3.8.1** *(obs 312)* — Does this characteristic engage the moral evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how?
- **T3.8.2** *(obs 313)* — Does this characteristic enable, deepen, bypass, or impair moral evaluation in the person?
- **T3.8.3** *(obs 314)* — What does the pattern of engagement or non-engagement with moral evaluation reveal about the nature of this characteristic?

**T3.9 · Conscience**

- **T3.9.1** *(obs 315)* — Does this characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how?
- **T3.9.2** *(obs 316)* — Does this characteristic enable, deepen, bypass, or impair conscience in the person?
- **T3.9.3** *(obs 317)* — What does the pattern of engagement or non-engagement with conscience reveal about the nature of this characteristic?

**T3.10 · Conscientiousness**

- **T3.10.1** *(obs 318)* — Does this characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how?
- **T3.10.2** *(obs 319)* — Does this characteristic enable, deepen, bypass, or impair conscientiousness in the person?
- **T3.10.3** *(obs 320)* — What does the pattern of engagement or non-engagement with conscientiousness reveal about the nature of this characteristic?

**T3.11 · Relational Capacity**

- **T3.11.1** *(obs 321)* — Does this characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how?
- **T3.11.2** *(obs 322)* — Does this characteristic enable, deepen, bypass, or impair relational capacity in the person?
- **T3.11.3** *(obs 323)* — What does the pattern of engagement or non-engagement with relational capacity reveal about the nature of this characteristic?
### T4 — Relational Interfaces

**T4.1 · Divine Interface — God to Human**

- **T4.1.1** *(obs 324)* — Does the verse evidence show this characteristic operating from God toward the human person — and if so, how?
- **T4.1.2** *(obs 325)* — What does the evidence reveal about the basis on which God extends this characteristic — is it conditional, unconditional, covenantal, or responsive?
- **T4.1.3** *(obs 326)* — What does God's extension of this characteristic reveal about his disposition toward the human person?
- **T4.1.4** *(obs 327)* — If the evidence is silent on God-to-human operation, note this explicitly.

**T4.2 · Divine Interface — Human to God**

- **T4.2.1** *(obs 328)* — Does the verse evidence show this characteristic operating in the human person's movement toward God — in seeking, supplication, worship, or covenant — and if so, how?
- **T4.2.2** *(obs 329)* — What does the evidence reveal about the inner posture required for this movement?
- **T4.2.3** *(obs 330)* — What does the human-to-God direction of this characteristic reveal about the person's relationship with God?
- **T4.2.4** *(obs 331)* — If the evidence is silent on human-to-God operation, note this explicitly.

**T4.3 · Human Interface — Giving**

- **T4.3.1** *(obs 332)* — Does the verse evidence show this characteristic being extended by one person toward another — and if so, how does it operate in that giving?
- **T4.3.2** *(obs 333)* — What inner conditions or orientations in the giver enable genuine extension of this characteristic?
- **T4.3.3** *(obs 334)* — What does the evidence reveal about what the person must have received or become before they can genuinely give this characteristic?
- **T4.3.4** *(obs 335)* — If the evidence is silent on the giving direction, note this explicitly.

**T4.4 · Human Interface — Receiving**

- **T4.4.1** *(obs 336)* — Does the verse evidence show this characteristic being received by a person from another — and if so, how does it operate in that reception?
- **T4.4.2** *(obs 337)* — What inner conditions enable or block reception of this characteristic from another person?
- **T4.4.3** *(obs 338)* — What is the inner-being state of the person who encounters this characteristic from another but does not receive it?
- **T4.4.4** *(obs 339)* — If the evidence is silent on the receiving direction, note this explicitly.

**T4.5 · Human Interface — Boundaries**

- **T4.5.1** *(obs 340)* — Does the evidence indicate whether this characteristic operates differently within existing relational bonds versus across relational distance or difference?
- **T4.5.2** *(obs 341)* — Does this characteristic operate within covenantal contexts only, or does it cross covenantal boundaries?
- **T4.5.3** *(obs 342)* — What does the evidence reveal about the relational scope of this characteristic — who is included and who is not?
- **T4.5.4** *(obs 343)* — If the evidence is silent on relational boundaries, note this explicitly.

**T4.6 · Spiritual Beings Interface**

- **T4.6.1** *(obs 344)* — Does the verse evidence show this characteristic operating in relation to other spiritual beings — angelic or adversarial — and if so, how?
- **T4.6.2** *(obs 345)* — Is this characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial spiritual powers?
- **T4.6.3** *(obs 346)* — Is this characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?
- **T4.6.4** *(obs 347)* — If the evidence is silent on the spiritual beings interface, note this explicitly.
### T5 — Formative and Developmental Dimension

**T5.1 · Nature of Transformation**

- **T5.1.1** *(obs 348)* — Does this characteristic produce transformation in the person — and if so, does it change the person's condition, the person's orientation to their condition, or both?
- **T5.1.2** *(obs 349)* — Is the transformation produced by this characteristic reversible or irreversible in the verse evidence?
- **T5.1.3** *(obs 350)* — If the evidence is silent on transformation, note this explicitly.

**T5.2 · Sequence of Inner States**

- **T5.2.1** *(obs 351)* — Does the verse evidence describe a sequence of inner states through which this characteristic moves the person — a before, during, and after?
- **T5.2.2** *(obs 352)* — What are those states, and what does the sequence reveal about how this characteristic works?
- **T5.2.3** *(obs 353)* — If the evidence is silent on sequence, note this explicitly.

**T5.3 · Mechanism of Change**

- **T5.3.1** *(obs 354)* — What mechanism does this characteristic use to produce change in the person — discipline, encounter, gradual formation, sudden transformation, or something else?
- **T5.3.2** *(obs 355)* — Does the evidence distinguish between mechanisms in different contexts?
- **T5.3.3** *(obs 356)* — If the evidence is silent on mechanism, note this explicitly.

**T5.4 · Suffering and Affliction**

- **T5.4.1** *(obs 357)* — Does the verse evidence show this characteristic operating in relation to suffering or affliction — as a response to it, a product of it, or a context for it?
- **T5.4.2** *(obs 358)* — Does suffering deepen, test, reveal, or produce this characteristic in the person?
- **T5.4.3** *(obs 359)* — If the evidence is silent on the relationship to suffering, note this explicitly.

**T5.5 · Formation and Sanctification**

- **T5.5.1** *(obs 360)* — Does the verse evidence show this characteristic participating in the longer arc of character formation and sanctification — shaping the person over time toward greater likeness?
- **T5.5.2** *(obs 361)* — What does the evidence reveal about the role of this characteristic in that longer arc?
- **T5.5.3** *(obs 362)* — If the evidence is silent on formation and sanctification, note this explicitly.

**T5.6 · Eschatological Trajectory**

- **T5.6.1** *(obs 363)* — Does the verse evidence point this characteristic toward an eschatological fullness — a future state toward which its present operation is oriented?
- **T5.6.2** *(obs 364)* — What does the present experience of this characteristic anticipate about its future fullness?
- **T5.6.3** *(obs 365)* — If the evidence is silent on eschatological trajectory, note this explicitly.

**T5.7 · Deposit Consequence**

- **T5.7.1** *(obs 366)* — Where T2.8 has identified a constitutional deposit from sustained operation of this characteristic, what developmental consequence does that deposit produce over time?
- **T5.7.2** *(obs 367)* — Does the evidence indicate generational consequence — a deposit carried forward beyond the individual?
- **T5.7.3** *(obs 368)* — If T2.8 found no deposit, note this explicitly and close T5.7.
### T6 — Structural Relationships with Other Characteristics

**T6.1 · Co-occurrence**

- **T6.1.1** *(obs 369)* — Which adjacent characteristics appear most frequently alongside this one in the verse evidence?
- **T6.1.2** *(obs 370)* — What does the pattern of co-occurrence reveal about this characteristic's place in the inner-being landscape?
- **T6.1.3** *(obs 371)* — If no significant co-occurrence patterns emerge, note this explicitly.

**T6.2 · Sequential Relationships**

- **T6.2.1** *(obs 372)* — Does the verse evidence show this characteristic consistently preceding, following, or accompanying another characteristic in a sequence?
- **T6.2.2** *(obs 373)* — What does the sequence reveal — is the relationship causal, developmental, or correlational?
- **T6.2.3** *(obs 374)* — If no sequential pattern is evidenced, note this explicitly.

**T6.3 · Causal and Constitutive Relationships**

- **T6.3.1** *(obs 375)* — Does this characteristic produce another characteristic in the verse evidence — and if so, which one, and by what mechanism?
- **T6.3.2** *(obs 376)* — Is this characteristic produced by another — and if so, which one?
- **T6.3.3** *(obs 377)* — Is this characteristic a constituent element of another, or does another characteristic constitute part of this one?
- **T6.3.4** *(obs 378)* — If no causal or constitutive relationship is evidenced, note this explicitly.

**T6.4 · Vocabulary and Root Sharing**

- **T6.4.1** *(obs 379)* — Does this characteristic share vocabulary terms with other characteristics in the programme?
- **T6.4.2** *(obs 380)* — Does vocabulary sharing extend to root-level architecture — a shared root that generates terms across two or more characteristics?
- **T6.4.3** *(obs 381)* — What does vocabulary sharing reveal about the conceptual relationship between characteristics?
- **T6.4.4** *(obs 382)* — If no significant vocabulary sharing is evidenced, note this explicitly.

**T6.5 · Distinctions**

- **T6.5.1** *(obs 383)* — Which adjacent characteristic most closely resembles this one — and what precisely distinguishes them?
- **T6.5.2** *(obs 384)* — Where the evidence shows apparent overlap, what is the precise boundary?
- **T6.5.3** *(obs 385)* — Is the distinction between this characteristic and its nearest neighbour one of degree, kind, direction, or constitutional level?
- **T6.5.4** *(obs 386)* — If no significant distinction work is required, note this explicitly.

**T6.6 · Shared Verse Anchors**

- **T6.6.1** *(obs 387)* — Does any verse in this characteristic's evidence base also function as a primary anchor in another characteristic's study?
- **T6.6.2** *(obs 388)* — What does the shared anchor reveal about the relationship between the two characteristics?
- **T6.6.3** *(obs 389)* — If no shared verse anchors are identified, note this explicitly.

**T6.7 · Dimensional Sharing**

- **T6.7.1** *(obs 390)* — How many of this characteristic's confirmed analytical dimensions are shared with another characteristic in the programme?
- **T6.7.2** *(obs 391)* — What does the pattern of dimensional sharing reveal about the relationship between this characteristic and those it shares dimensions with?
- **T6.7.3** *(obs 392)* — If dimensional sharing data is not yet available, note this explicitly.
### T7 — Evidential and Methodological Foundation

**T7.1 · Lexical and Semantic Analysis**

- **T7.1.1** *(obs 393)* — What are the primary Hebrew and Greek terms for this characteristic — and what do their root meanings reveal?
- **T7.1.2** *(obs 394)* — What is the grammatical range of the primary term (noun, verb, adjective, participle) — and what does that range reveal about how the characteristic operates?
- **T7.1.3** *(obs 395)* — What is the semantic range of the primary term — across what breadth of meaning does it operate?
- **T7.1.4** *(obs 396)* — Does the vocabulary include terms that distinguish distinct aspects of this characteristic — disposition versus act, received versus given, condition versus quality?
- **T7.1.5** *(obs 397)* — Does the vocabulary include a term for the structural opposite or absence of this characteristic?
- **T7.1.6** *(obs 398)* — Does the vocabulary include a person-type term — a term for the one who habitually possesses or exercises this characteristic?
- **T7.1.7** *(obs 399)* — Does the vocabulary include a supplication or seeking term — a term for the act of seeking this characteristic from another?
- **T7.1.8** *(obs 400)* — What does the relationship between the OT Hebrew vocabulary and the NT Greek vocabulary reveal about continuity or development of this characteristic across the Testaments?
- **T7.1.9** *(obs 401)* — Is there a term newly coined in the NT period for this characteristic — and if so, what does that coinage reveal?
- **T7.1.10** *(obs 402)* — What does the full vocabulary arc reveal about this characteristic's complete semantic range?

**T7.2 · Verse and Literary Interpretation**

- **T7.2.1** *(obs 403)* — What is the function of this characteristic's primary term within its primary verse — what role does it play in the sentence and argument?
- **T7.2.2** *(obs 404)* — What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic) — and what does that form require for responsible interpretation?
- **T7.2.3** *(obs 405)* — What is the logical structure of key arguments in the verse evidence — what are the premises and conclusions?
- **T7.2.4** *(obs 406)* — What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological) — and what does that setting reveal?
- **T7.2.5** *(obs 407)* — Does any verse function as the primary anchor for this characteristic — the verse that most fully and directly expresses its essential character?
- **T7.2.6** *(obs 408)* — What does the primary anchor verse reveal that no other verse reveals?

**T7.3 · Human Science Frameworks**

- **T7.3.1** *(obs 409)* — Which human science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) is most useful as an interpretive lens for this characteristic?
- **T7.3.2** *(obs 410)* — Where the human science framework illuminates the verse evidence — making a finding more coherent or complete — what does it reveal?
- **T7.3.3** *(obs 411)* — Where the verse evidence and the human science framework diverge, what does the divergence reveal?
- **T7.3.4** *(obs 412)* — Does the human science framework surface any aspect of this characteristic that the verse evidence has not yet addressed — and does that absence require further verse investigation?

---
### Provenance
- Supersedes: `wa-tier-catalogue-restructured-v1-20260610.md` (no consolidated questions / no source text) and `wa-tier-questions-extract-v1-20260604.md` (flat 189).
- Designs applied: `wa-verse-level-extraction-spec-v1-20260609.md`, `wa-catalogue-refit-two-layer-v1-20260609.md`; gaps flagged in `wa-verse-extraction-gaps-v1-20260610.md` (cause-side fields are a *separate, additive* proposal, not folded here).
- Source-question text quoted in §1 is pulled verbatim from `wa_obs_question_catalogue` (live, 2026-06-11).
- Live cross-reference: VE-01..14 ↔ old codes are linked in the DB via `finding_question_link`; queryable through `v_l2_tier.question_code`.
- **DB unchanged.** On approval: migration to tag `wa_obs_question_catalogue` with `layer` (A/SYNTH/DROP/DEFER), store each VE's consolidated question + its originating-code set, and apply the de-force rewordings.
