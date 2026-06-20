# Tier Catalogue — Restructured (Two-Layer Slice) · v2 · 2026-06-11

> **Supersedes v1** ([`wa-tier-catalogue-restructured-v1-20260610.md`](archive/wa-tier-catalogue-restructured-v1-20260610.md)) and the original flat extract ([`wa-tier-questions-extract-v1-20260604.md`](wa-tier-questions-extract-v1-20260604.md)).
> **v2 adds the consolidated VE questions + the full source-question text.** For each verse-extraction field, the originating tier questions are **analysed and merged into a single verse-level question that the field answers**, with **every combined aspect retained**. Each block now also quotes the **originating tier questions in full** so the consolidation can be evaluated against its source as a whole. Only the cross-verse *reveal/pattern/over-time* clauses route to SYNTH (noted per field).
> **For approval — DB not yet modified.** Old T-codes remain the reference key (numbering expected to change); `VE-nn` IDs are provisional.
>
> **⚠ Reconciliation note (updated 2026-06-20).** This is the 2026-06-11 VE/SYNTH *design*, built against the then-189-question catalogue. The catalogue has since been **refit (v2_1, applied to the DB 2026-06-19)**: the live set is now **126 active questions**. Two corrections have been made here to agree with the DB: (1) **Appendix A (§7) has been replaced with the clean live list of 126 active questions** — the retired questions are no longer listed; (2) the **science questions (T7.3.1–.4) are ACTIVE, not deferred** — the earlier "DEFER/park" disposition is removed. The design dispositions in §1–§5 still reference the original code set; where a code there is now folded or retired in the DB, that is the refit's doing. The authoritative current question list is Appendix A.

---

## 0. The two layers

| Layer | grain | what it is | where it lives |
|---|---|---|---|
| **A · Verse-Extraction (L1/L2)** | one typed term-in-verse | structured fields with **closed option-lists** — the *evidence*, state-not-induce (NONE/SILENT/not-stated first-class) | the L2 read → `finding` (l2_api) → **`v_l2_tier`** |
| **B · SYNTH** | characteristic / cross-verse / cross-term / cross-cluster | the *"what does X reveal"*, *over-time*, *pattern*, *relationship* questions — **computed by rolling up** Layer A | the synthesis pass |

Every old question is dispositioned **→ Layer A** · **SYNTH** · **DROP** (§5 indexes all 189; nothing is deferred — the science lens T7.3 is **SYNTH**).

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

**Science — ACTIVE (the earlier DEFER/park is removed):** **T7.3.1–.4** Human Science Frameworks are **live in the DB** and treated as a **synthesis lens** — the cross-Scripture "view from outside" (the science section of each cluster essay). They are not deferred and not dropped.

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
| | | | T7.3.1–.4 | **SYNTH** (active science lens) |

**Tally:** of the original 189 — **14 → Layer A (implemented, each now one consolidated question)** · **+3 proposed (VE-15/16/17)** · **~122 → SYNTH** (including the active science lens T7.3) · **18 DROP** · the `.x "if silent"` sub-questions **fold** into null tokens. *(No DEFER — science is active.)* **Live catalogue today: 126 active questions** — see Appendix A.

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

## 7. Appendix A — the live question catalogue (current active set, from the DB)

> Regenerated from `wa_obs_question_catalogue` (`deleted=0` AND tier set), **2026-06-20** — **126 active questions**, after the v2_1 refit (applied 2026-06-19). **Retired questions are not listed** (this replaces the earlier verbatim 189-question extract, which mixed in now-retired questions and was the source of the confusion). `obs_id` is the DB key; `question_code` (Tn.c.q) is the reference used throughout. The science questions **T7.3.1–.4 appear here as active**.

### T0 — Divine Image and Created Design

**T0.1 · Divine Nature Reflected**

- **T0.1.1** *(obs 224)* — In this verse, is the characteristic predicated of God or otherwise related to God; if so, in what relation (God as the one who bears it, acts, gives it, or is its object)? Record the relation, or record that it is not related to God here.
- **T0.1.2** *(obs 225)* — Across the characteristic's verses, is it ever borne by God himself or only by the creature, and what does that pattern of presence or absence indicate for its place in the human person and in the divine image?
**T0.2 · Created Purpose**

- **T0.2.1** *(obs 227)* — Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none.
- **T0.2.2** *(obs 228)* — Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable?
- **T0.2.3** *(obs 229)* — Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none.
**T0.3 · Image-Bearer Expression**

- **T0.3.1** *(obs 230)* — From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none.
- **T0.3.2** *(obs 231)* — Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God?
- **T0.3.3** *(obs 232)* — Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced?
**T0.4 · Typological Significance**

- **T0.4.1** *(obs 233)* — Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none.

### T1 — Definition

**T1.1 · Name and Naming**

- **T1.1.1** *(obs 236)* — What is the characteristic called in the programme, and what does the name signal about its essential nature?
- **T1.1.2** *(obs 237)* — What do the primary Hebrew and Greek terms show at the definitional level?
- **T1.1.3** *(obs 238)* — What directional, relational, or constitutional implication does the name carry?
**T1.2 · Kind**

- **T1.2.1** *(obs 239)* — What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else?
- **T1.2.2** *(obs 240)* — Is the characteristic simple in structure, or does it combine constituent elements; if compound, which?
**T1.3 · Boundary**

- **T1.3.1** *(obs 242)* — What stands against the characteristic as its structural opposite — the inner-being reality that excludes it?
- **T1.3.2** *(obs 243)* — What does the characteristic exclude or resist at its edge?
- **T1.3.3** *(obs 244)* — Where does the characteristic end and another thing begin — what is it not?
**T1.4 · Modes of Operation**

- **T1.4.1** *(obs 245)* — In what distinct mode(s) does the characteristic operate within the inner person in this verse — including its grammatical/stem form and the manner of functioning?
- **T1.4.2** *(obs 246)* — Does the mode of operation vary by context, direction, or constitutional level; if so, how?
- **T1.4.3** *(obs 247)* — Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none.
**T1.5 · Immediate Response**

- **T1.5.1** *(obs 248)* — What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none.
- **T1.5.2** *(obs 249)* — Across the verses, is that immediate response consistent or varied?
**T1.6 · Sustained Effect**

- **T1.6.1** *(obs 251)* — What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none.
- **T1.6.3** *(obs 253)* — How does the sustained effect differ from the immediate response (T1.5)?
**T1.7 · Conditions of Reception**

- **T1.7.1** *(obs 254)* — Under what inner conditions does the characteristic take hold or operate rightly?
- **T1.7.2** *(obs 255)* — Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)?
- **T1.7.3** *(obs 256)* — What is the inner-being state of the person in whom the characteristic is present but does not take hold?

### T2 — Constitutional Location and Boundaries

**T2.1 · Spirit-Level Location**

- **T2.1.1** *(obs 260)* — At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none.
- **T2.1.2** *(obs 261)* — Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating?
**T2.7 · Body — Direction**

- **T2.7.1** *(obs 279)* — Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none.
**T2.9 · Origin and Source**

- **T2.9.1** *(obs 285)* — Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated?
- **T2.9.2** *(obs 286)* — Across the verses, is the origin single or multiple, and does it change with context?
**T2.10 · Constitutional Movement**

- **T2.10.1** *(obs 288)* — Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none.

### T3 — The Inner Faculties

**T3.1 · Perception**

- **T3.1.1** *(obs 291)* — In this verse, does the characteristic engage the perceptive faculty — the inner senses (hearing, sight, taste, touch, smell) and spiritual discernment — and if so, which inner sense and how? Record none if it does not.
- **T3.1.2** *(obs 292)* — How does the characteristic affect perception in the person here — and record no effect if none is evidenced.
- **T3.1.3** *(obs 293)* — Across the verses, what does the pattern of engagement and non-engagement with perception indicate about the characteristic's nature?
**T3.2 · Cognition**

- **T3.2.1** *(obs 294)* — In this verse, does the characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how? Record none if it does not.
- **T3.2.2** *(obs 295)* — How does the characteristic affect cognition in the person here — and record no effect if none is evidenced.
- **T3.2.3** *(obs 296)* — Across the verses, what does the pattern of engagement and non-engagement with cognition indicate about the characteristic's nature?
**T3.3 · Memory**

- **T3.3.1** *(obs 297)* — In this verse, does the characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how? Record none if it does not.
- **T3.3.2** *(obs 298)* — How does the characteristic affect memory in the person here — and record no effect if none is evidenced.
- **T3.3.3** *(obs 299)* — Across the verses, what does the pattern of engagement and non-engagement with memory indicate about the characteristic's nature?
**T3.4 · Affect**

- **T3.4.1** *(obs 300)* — In this verse, does the characteristic engage the affective faculty — feeling and emotional experience — and if so, how? Record none if it does not.
- **T3.4.2** *(obs 301)* — How does the characteristic affect the affective faculty in the person here — and record no effect if none is evidenced.
- **T3.4.3** *(obs 302)* — Across the verses, what does the pattern of engagement and non-engagement with affect indicate about the characteristic's nature?
**T3.5 · Creativity**

- **T3.5.1** *(obs 303)* — In this verse, does the characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how? Record none if it does not.
- **T3.5.2** *(obs 304)* — How does the characteristic affect creativity in the person here — and record no effect if none is evidenced.
- **T3.5.3** *(obs 305)* — Across the verses, what does the pattern of engagement and non-engagement with creativity indicate about the characteristic's nature?
**T3.6 · Volition**

- **T3.6.1** *(obs 306)* — In this verse, does the characteristic engage the volitional faculty — the capacity to choose — and if so, how? Record none if it does not.
- **T3.6.2** *(obs 307)* — How does the characteristic affect volition in the person here — including its capacity, its interaction with other characteristics, and the constraints under which it operates — and record no effect if none is evidenced.
- **T3.6.3** *(obs 308)* — Across the verses, what does the pattern of engagement and non-engagement with volition indicate about the characteristic's nature?
**T3.7 · Agency**

- **T3.7.1** *(obs 309)* — In this verse, does the characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how? Record none if it does not.
- **T3.7.2** *(obs 310)* — How does the characteristic affect agency in the person here — and record no effect if none is evidenced.
- **T3.7.3** *(obs 311)* — Across the verses, what does the pattern of engagement and non-engagement with agency indicate about the characteristic's nature?
**T3.8 · Moral Evaluation**

- **T3.8.1** *(obs 312)* — In this verse, does the characteristic engage the moral-evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how? Record none if it does not.
- **T3.8.2** *(obs 313)* — How does the characteristic affect moral evaluation in the person here — and record no effect if none is evidenced.
- **T3.8.3** *(obs 314)* — Across the verses, what does the pattern of engagement and non-engagement with moral evaluation indicate about the characteristic's nature?
**T3.9 · Conscience**

- **T3.9.1** *(obs 315)* — In this verse, does the characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how? Record none if it does not.
- **T3.9.2** *(obs 316)* — How does the characteristic affect conscience in the person here — and record no effect if none is evidenced.
- **T3.9.3** *(obs 317)* — Across the verses, what does the pattern of engagement and non-engagement with conscience indicate about the characteristic's nature?
**T3.10 · Conscientiousness**

- **T3.10.1** *(obs 318)* — In this verse, does the characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how? Record none if it does not.
- **T3.10.2** *(obs 319)* — How does the characteristic affect conscientiousness in the person here — and record no effect if none is evidenced.
- **T3.10.3** *(obs 320)* — Across the verses, what does the pattern of engagement and non-engagement with conscientiousness indicate about the characteristic's nature?
**T3.11 · Relational Capacity**

- **T3.11.1** *(obs 321)* — In this verse, does the characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how? Record none if it does not.
- **T3.11.2** *(obs 322)* — How does the characteristic affect relational capacity in the person here — and record no effect if none is evidenced.
- **T3.11.3** *(obs 323)* — Across the verses, what does the pattern of engagement and non-engagement with relational capacity indicate about the characteristic's nature?

### T4 — Relational Interfaces

**T4.1 · Divine Interface — God to Human**

- **T4.1.1** *(obs 324)* — In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not.
- **T4.1.2** *(obs 325)* — On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows?
- **T4.1.3** *(obs 326)* — What does God's extension of the characteristic show about his disposition toward the human person?
**T4.2 · Divine Interface — Human to God**

- **T4.2.1** *(obs 328)* — In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not.
- **T4.2.2** *(obs 329)* — What inner posture does this movement require, as the evidence shows?
- **T4.2.3** *(obs 330)* — What does the human-to-God direction of the characteristic show about the person's relationship with God?
**T4.3 · Human Interface — Giving**

- **T4.3.1** *(obs 332)* — In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not.
- **T4.3.2** *(obs 333)* — What inner conditions or orientations in the giver accompany genuine extension of the characteristic?
- **T4.3.3** *(obs 334)* — What does the evidence show a person must have received or become before they extend the characteristic?
**T4.4 · Human Interface — Receiving**

- **T4.4.1** *(obs 336)* — In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not.
- **T4.4.2** *(obs 337)* — What inner conditions accompany or block uptake of the characteristic from another person?
- **T4.4.3** *(obs 338)* — What is the inner-being state of the person who meets the characteristic from another but does not take it up?
**T4.5 · Human Interface — Boundaries**

- **T4.5.1** *(obs 340)* — Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how?
- **T4.5.2** *(obs 341)* — Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows?
- **T4.5.3** *(obs 342)* — What does the evidence show about the relational scope of the characteristic — who is included and who is not?
**T4.6 · Spiritual Beings Interface**

- **T4.6.1** *(obs 344)* — In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not.
- **T4.6.2** *(obs 345)* — Is the characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial powers — as the evidence shows?
- **T4.6.3** *(obs 346)* — Is the characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?

### T5 — Formative and Developmental Dimension

**T5.1 · Nature of Transformation**

- **T5.1.1** *(obs 348)* — In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown.
- **T5.1.2** *(obs 349)* — Is the transformation reversible or irreversible in the evidence?
**T5.2 · Sequence of Inner States**

- **T5.2.1** *(obs 351)* — Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown.
**T5.3 · Mechanism of Change**

- **T5.3.1** *(obs 354)* — In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown.
- **T5.3.2** *(obs 355)* — Does the mechanism differ across contexts in the evidence; if so, how?
**T5.4 · Suffering and Affliction**

- **T5.4.1** *(obs 357)* — In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown.
- **T5.4.2** *(obs 358)* — What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown.
**T5.5 · Formation and Sanctification**

- **T5.5.1** *(obs 360)* — In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown.
**T5.6 · Eschatological Trajectory**

- **T5.6.1** *(obs 363)* — In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown.

### T6 — Structural Relationships with Other Characteristics

**T6.1 · Co-occurrence**

- **T6.1.1** *(obs 369)* — Which adjacent characteristics appear alongside this one in the verse evidence, and how frequently? Record none if no significant co-occurrence appears.
- **T6.1.2** *(obs 370)* — What does the co-occurrence pattern show about this characteristic's place in the inner-being landscape?
**T6.2 · Sequential Relationships**

- **T6.2.1** *(obs 372)* — Does the evidence show this characteristic consistently preceding, following, or accompanying another in a sequence; if so, which and how? Record none if no sequence appears.
- **T6.2.2** *(obs 373)* — What does the sequence show — is the relationship causal, developmental, or correlational?
**T6.3 · Causal and Constitutive Relationships**

- **T6.3.1** *(obs 375)* — Does this characteristic produce another in the evidence, and if so which, and by what mechanism? Record none if none is shown.
- **T6.3.2** *(obs 376)* — Is this characteristic produced by another, and if so which?
- **T6.3.3** *(obs 377)* — Is this characteristic a constituent element of another, or another a constituent of this one?
**T6.4 · Vocabulary and Root Sharing**

- **T6.4.1** *(obs 379)* — Which vocabulary terms, if any, does this characteristic share with other characteristics in the programme? Record none if none is shown.
- **T6.4.2** *(obs 380)* — Does the sharing extend to root-level architecture — a shared root generating terms across two or more characteristics?
- **T6.4.3** *(obs 381)* — What does the vocabulary sharing show about the conceptual relationship between the characteristics?
**T6.5 · Distinctions**

- **T6.5.1** *(obs 383)* — Which adjacent characteristic most closely resembles this one, and what precisely distinguishes them?
- **T6.5.2** *(obs 384)* — Where the evidence shows apparent overlap, what is the precise boundary?
- **T6.5.3** *(obs 385)* — Is the distinction from the nearest neighbour one of degree, kind, direction, or constitutional level?

### T7 — Evidential and Methodological Foundation

**T7.1 · Lexical and Semantic Analysis**

- **T7.1.1** *(obs 393)* — What are the primary Hebrew and Greek terms for this characteristic, and what do their root meanings show?
- **T7.1.2** *(obs 394)* — What is the grammatical range of the primary term (noun, verb, adjective, participle), and what does that range show about how the characteristic operates?
- **T7.1.3** *(obs 395)* — What is the semantic range of the primary term — across what breadth of meaning does it operate?
- **T7.1.4** *(obs 396)* — Does the vocabulary include terms distinguishing distinct aspects — disposition versus act, received versus given, condition versus quality? Record which, or none.
- **T7.1.5** *(obs 397)* — Does the vocabulary include a term for the structural opposite or absence of this characteristic? Record it, or none.
- **T7.1.6** *(obs 398)* — Does the vocabulary include a person-type term — one for the person who habitually possesses or exercises this characteristic? Record it, or none.
- **T7.1.7** *(obs 399)* — Does the vocabulary include a supplication or seeking term — one for the act of seeking this characteristic from another? Record it, or none.
- **T7.1.8** *(obs 400)* — What does the relationship between the OT Hebrew and NT Greek vocabulary show about continuity or development of the characteristic across the Testaments?
- **T7.1.9** *(obs 401)* — Is there a term newly coined in the NT period for this characteristic; if so, what does the coinage show? Record it, or none.
- **T7.1.10** *(obs 402)* — What does the full vocabulary arc show about the characteristic's complete semantic range?
**T7.2 · Verse and Literary Interpretation**

- **T7.2.1** *(obs 403)* — What is the function of the primary term within its primary verse — what role does it play in the sentence and argument?
- **T7.2.2** *(obs 404)* — What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic), and what does that form require for responsible interpretation?
- **T7.2.3** *(obs 405)* — What is the logical structure of the key arguments in the verse evidence — premises and conclusions?
- **T7.2.4** *(obs 406)* — What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological), and what does that setting show?
- **T7.2.5** *(obs 407)* — Does any verse function as the primary anchor — the one most fully and directly expressing the characteristic's essential character? Record it, or none.
- **T7.2.6** *(obs 408)* — What does the primary anchor verse show that no other verse shows?
**T7.3 · Human Science Frameworks**

- **T7.3.1** *(obs 409)* — Which human-science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) serves as the most useful interpretive lens for this characteristic?
- **T7.3.2** *(obs 410)* — Where the framework illuminates the verse evidence — making a finding more coherent or complete — what does it show?
- **T7.3.3** *(obs 411)* — Where the verse evidence and the framework diverge, what does the divergence show?
- **T7.3.4** *(obs 412)* — Does the framework surface any aspect of the characteristic the verse evidence has not yet addressed, and does that absence call for further verse investigation?

---

### Provenance
- Supersedes: `wa-tier-catalogue-restructured-v1-20260610.md` (no consolidated questions / no source text) and `wa-tier-questions-extract-v1-20260604.md` (flat 189).
- Designs applied: `wa-verse-level-extraction-spec-v1-20260609.md`, `wa-catalogue-refit-two-layer-v1-20260609.md`; gaps flagged in `wa-verse-extraction-gaps-v1-20260610.md` (cause-side fields are a *separate, additive* proposal, not folded here).
- Source-question text quoted in §1 is pulled verbatim from `wa_obs_question_catalogue` (live, 2026-06-11).
- Live cross-reference: VE-01..14 ↔ old codes are linked in the DB via `finding_question_link`; queryable through `v_l2_tier.question_code`.
- **VE/SYNTH design DB-unchanged.** On approval: migration to tag `wa_obs_question_catalogue` with `layer` (A/SYNTH/DROP), store each VE's consolidated question + its originating-code set, and apply the de-force rewordings. *(Separately, the v2_1 de-bias refit — folding/rewording — was already applied 2026-06-19; this document's Appendix A reflects that live state.)*
