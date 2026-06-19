# Tier Catalogue Update — Instruction for Claude Code · v1_0 · 2026-06-19

**File:** WA-tier-catalogue-cc-update-v1_0-2026-06-19.md
**Date:** 2026-06-19 · **Prefix:** WA · **Type:** CC update instruction (markdown)
**Companion (decision source):** `WA-tier-catalogue-rewrite-v2_1-2026-06-19.md` — full rewritten T0–T7 with per-code dispositions and `absorbs:` provenance. This document is the executable distillation; where the two differ, the rewrite document governs the wording and this document governs the operation set.
**Target table:** `wa_obs_question_catalogue`
**Source of truth for current rows:** `WA-tier-catalogue-current-state-v1-20260617.md` (173 active codes, `deleted=0 AND tier IS NOT NULL`).

---

## What this update does

Two operation types, applied to the 173 currently-active tiered questions:

1. **TEXT-UPDATE** — for each `keep` code: set `question_text` to the de-biased rewritten form. **126 codes.**
2. **SOFT-DELETE** — for each `obsolete` code: set `deleted = 1` (and record the fold target). **47 codes.**

No rows are inserted. No code is renumbered. No hard delete. Every `obsolete` code is folded into a named primary whose text already carries the absorbed content, so the soft-delete is reversible and loses no aspect.

**Counts (verify after run):** 126 text-updates + 47 soft-deletes = 173 codes touched. Post-run active tiered count = 126.

---

## Operation A — TEXT-UPDATE (keep codes)

For each code below, set `question_text` to the quoted string. Codes are grouped by tier for review; order of execution within Operation A does not matter.

> **Note for CC:** the three codes **T1.7.2**, **T2.9.1**, **T2.10.1** carry the *other-spirits* edit (v2_1). The two codes **T2.1.1** and **T2.1.2** are materially repurposed (single-level → consolidated grid / synthesis); treat their text change as deliberate, not a wording tidy.

### T0
- **T0.1.1** → "In this verse, is the characteristic predicated of God or otherwise related to God; if so, in what relation (God as the one who bears it, acts, gives it, or is its object)? Record the relation, or record that it is not related to God here."
- **T0.1.2** → "Across the characteristic's verses, is it ever borne by God himself or only by the creature, and what does that pattern of presence or absence indicate for its place in the human person and in the divine image?"
- **T0.2.1** → "Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none."
- **T0.2.2** → "Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable?"
- **T0.2.3** → "Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none."
- **T0.3.1** → "From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none."
- **T0.3.2** → "Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God?"
- **T0.3.3** → "Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced?"
- **T0.4.1** → "Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none."

### T1
- **T1.1.1** → "What is the characteristic called in the programme, and what does the name signal about its essential nature?"
- **T1.1.2** → "What do the primary Hebrew and Greek terms show at the definitional level?"
- **T1.1.3** → "What directional, relational, or constitutional implication does the name carry?"
- **T1.2.1** → "What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else?"
- **T1.2.2** → "Is the characteristic simple in structure, or does it combine constituent elements; if compound, which?"
- **T1.3.1** → "What stands against the characteristic as its structural opposite — the inner-being reality that excludes it?"
- **T1.3.2** → "What does the characteristic exclude or resist at its edge?"
- **T1.3.3** → "Where does the characteristic end and another thing begin — what is it not?"
- **T1.4.1** → "In what distinct mode(s) does the characteristic operate within the inner person in this verse — including its grammatical/stem form and the manner of functioning?"
- **T1.4.2** → "Does the mode of operation vary by context, direction, or constitutional level; if so, how?"
- **T1.4.3** → "Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none."
- **T1.5.1** → "What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none."
- **T1.5.2** → "Across the verses, is that immediate response consistent or varied?"
- **T1.6.1** → "What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none."
- **T1.6.3** → "How does the sustained effect differ from the immediate response (T1.5)?"
- **T1.7.1** → "Under what inner conditions does the characteristic take hold or operate rightly?"
- **T1.7.2** → "Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)?"
- **T1.7.3** → "What is the inner-being state of the person in whom the characteristic is present but does not take hold?"

### T2
- **T2.1.1** → "At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none."
- **T2.1.2** → "Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating?"
- **T2.7.1** → "Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none."
- **T2.9.1** → "Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated?"
- **T2.9.2** → "Across the verses, is the origin single or multiple, and does it change with context?"
- **T2.10.1** → "Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none."

### T3
- **T3.1.1** → "In this verse, does the characteristic engage the perceptive faculty — the inner senses (hearing, sight, taste, touch, smell) and spiritual discernment — and if so, which inner sense and how? Record none if it does not."
- **T3.1.2** → "How does the characteristic affect perception in the person here — and record no effect if none is evidenced."
- **T3.1.3** → "Across the verses, what does the pattern of engagement and non-engagement with perception indicate about the characteristic's nature?"
- **T3.2.1** → "In this verse, does the characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how? Record none if it does not."
- **T3.2.2** → "How does the characteristic affect cognition in the person here — and record no effect if none is evidenced."
- **T3.2.3** → "Across the verses, what does the pattern of engagement and non-engagement with cognition indicate about the characteristic's nature?"
- **T3.3.1** → "In this verse, does the characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how? Record none if it does not."
- **T3.3.2** → "How does the characteristic affect memory in the person here — and record no effect if none is evidenced."
- **T3.3.3** → "Across the verses, what does the pattern of engagement and non-engagement with memory indicate about the characteristic's nature?"
- **T3.4.1** → "In this verse, does the characteristic engage the affective faculty — feeling and emotional experience — and if so, how? Record none if it does not."
- **T3.4.2** → "How does the characteristic affect the affective faculty in the person here — and record no effect if none is evidenced."
- **T3.4.3** → "Across the verses, what does the pattern of engagement and non-engagement with affect indicate about the characteristic's nature?"
- **T3.5.1** → "In this verse, does the characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how? Record none if it does not."
- **T3.5.2** → "How does the characteristic affect creativity in the person here — and record no effect if none is evidenced."
- **T3.5.3** → "Across the verses, what does the pattern of engagement and non-engagement with creativity indicate about the characteristic's nature?"
- **T3.6.1** → "In this verse, does the characteristic engage the volitional faculty — the capacity to choose — and if so, how? Record none if it does not."
- **T3.6.2** → "How does the characteristic affect volition in the person here — including its capacity, its interaction with other characteristics, and the constraints under which it operates — and record no effect if none is evidenced."
- **T3.6.3** → "Across the verses, what does the pattern of engagement and non-engagement with volition indicate about the characteristic's nature?"
- **T3.7.1** → "In this verse, does the characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how? Record none if it does not."
- **T3.7.2** → "How does the characteristic affect agency in the person here — and record no effect if none is evidenced."
- **T3.7.3** → "Across the verses, what does the pattern of engagement and non-engagement with agency indicate about the characteristic's nature?"
- **T3.8.1** → "In this verse, does the characteristic engage the moral-evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how? Record none if it does not."
- **T3.8.2** → "How does the characteristic affect moral evaluation in the person here — and record no effect if none is evidenced."
- **T3.8.3** → "Across the verses, what does the pattern of engagement and non-engagement with moral evaluation indicate about the characteristic's nature?"
- **T3.9.1** → "In this verse, does the characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how? Record none if it does not."
- **T3.9.2** → "How does the characteristic affect conscience in the person here — and record no effect if none is evidenced."
- **T3.9.3** → "Across the verses, what does the pattern of engagement and non-engagement with conscience indicate about the characteristic's nature?"
- **T3.10.1** → "In this verse, does the characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how? Record none if it does not."
- **T3.10.2** → "How does the characteristic affect conscientiousness in the person here — and record no effect if none is evidenced."
- **T3.10.3** → "Across the verses, what does the pattern of engagement and non-engagement with conscientiousness indicate about the characteristic's nature?"
- **T3.11.1** → "In this verse, does the characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how? Record none if it does not."
- **T3.11.2** → "How does the characteristic affect relational capacity in the person here — and record no effect if none is evidenced."
- **T3.11.3** → "Across the verses, what does the pattern of engagement and non-engagement with relational capacity indicate about the characteristic's nature?"

### T4
- **T4.1.1** → "In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not."
- **T4.1.2** → "On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows?"
- **T4.1.3** → "What does God's extension of the characteristic show about his disposition toward the human person?"
- **T4.2.1** → "In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not."
- **T4.2.2** → "What inner posture does this movement require, as the evidence shows?"
- **T4.2.3** → "What does the human-to-God direction of the characteristic show about the person's relationship with God?"
- **T4.3.1** → "In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not."
- **T4.3.2** → "What inner conditions or orientations in the giver accompany genuine extension of the characteristic?"
- **T4.3.3** → "What does the evidence show a person must have received or become before they extend the characteristic?"
- **T4.4.1** → "In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not."
- **T4.4.2** → "What inner conditions accompany or block uptake of the characteristic from another person?"
- **T4.4.3** → "What is the inner-being state of the person who meets the characteristic from another but does not take it up?"
- **T4.5.1** → "Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how?"
- **T4.5.2** → "Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows?"
- **T4.5.3** → "What does the evidence show about the relational scope of the characteristic — who is included and who is not?"
- **T4.6.1** → "In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not."
- **T4.6.2** → "Is the characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial powers — as the evidence shows?"
- **T4.6.3** → "Is the characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?"

### T5
- **T5.1.1** → "In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown."
- **T5.1.2** → "Is the transformation reversible or irreversible in the evidence?"
- **T5.2.1** → "Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown."
- **T5.3.1** → "In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown."
- **T5.3.2** → "Does the mechanism differ across contexts in the evidence; if so, how?"
- **T5.4.1** → "In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown."
- **T5.4.2** → "What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown."
- **T5.5.1** → "In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown."
- **T5.6.1** → "In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown."

### T6
- **T6.1.1** → "Which adjacent characteristics appear alongside this one in the verse evidence, and how frequently? Record none if no significant co-occurrence appears."
- **T6.1.2** → "What does the co-occurrence pattern show about this characteristic's place in the inner-being landscape?"
- **T6.2.1** → "Does the evidence show this characteristic consistently preceding, following, or accompanying another in a sequence; if so, which and how? Record none if no sequence appears."
- **T6.2.2** → "What does the sequence show — is the relationship causal, developmental, or correlational?"
- **T6.3.1** → "Does this characteristic produce another in the evidence, and if so which, and by what mechanism? Record none if none is shown."
- **T6.3.2** → "Is this characteristic produced by another, and if so which?"
- **T6.3.3** → "Is this characteristic a constituent element of another, or another a constituent of this one?"
- **T6.4.1** → "Which vocabulary terms, if any, does this characteristic share with other characteristics in the programme? Record none if none is shown."
- **T6.4.2** → "Does the sharing extend to root-level architecture — a shared root generating terms across two or more characteristics?"
- **T6.4.3** → "What does the vocabulary sharing show about the conceptual relationship between the characteristics?"
- **T6.5.1** → "Which adjacent characteristic most closely resembles this one, and what precisely distinguishes them?"
- **T6.5.2** → "Where the evidence shows apparent overlap, what is the precise boundary?"
- **T6.5.3** → "Is the distinction from the nearest neighbour one of degree, kind, direction, or constitutional level?"

### T7
- **T7.1.1** → "What are the primary Hebrew and Greek terms for this characteristic, and what do their root meanings show?"
- **T7.1.2** → "What is the grammatical range of the primary term (noun, verb, adjective, participle), and what does that range show about how the characteristic operates?"
- **T7.1.3** → "What is the semantic range of the primary term — across what breadth of meaning does it operate?"
- **T7.1.4** → "Does the vocabulary include terms distinguishing distinct aspects — disposition versus act, received versus given, condition versus quality? Record which, or none."
- **T7.1.5** → "Does the vocabulary include a term for the structural opposite or absence of this characteristic? Record it, or none."
- **T7.1.6** → "Does the vocabulary include a person-type term — one for the person who habitually possesses or exercises this characteristic? Record it, or none."
- **T7.1.7** → "Does the vocabulary include a supplication or seeking term — one for the act of seeking this characteristic from another? Record it, or none."
- **T7.1.8** → "What does the relationship between the OT Hebrew and NT Greek vocabulary show about continuity or development of the characteristic across the Testaments?"
- **T7.1.9** → "Is there a term newly coined in the NT period for this characteristic; if so, what does the coinage show? Record it, or none."
- **T7.1.10** → "What does the full vocabulary arc show about the characteristic's complete semantic range?"
- **T7.2.1** → "What is the function of the primary term within its primary verse — what role does it play in the sentence and argument?"
- **T7.2.2** → "What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic), and what does that form require for responsible interpretation?"
- **T7.2.3** → "What is the logical structure of the key arguments in the verse evidence — premises and conclusions?"
- **T7.2.4** → "What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological), and what does that setting show?"
- **T7.2.5** → "Does any verse function as the primary anchor — the one most fully and directly expressing the characteristic's essential character? Record it, or none."
- **T7.2.6** → "What does the primary anchor verse show that no other verse shows?"
- **T7.3.1** → "Which human-science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) serves as the most useful interpretive lens for this characteristic?"
- **T7.3.2** → "Where the framework illuminates the verse evidence — making a finding more coherent or complete — what does it show?"
- **T7.3.3** → "Where the verse evidence and the framework diverge, what does the divergence show?"
- **T7.3.4** → "Does the framework surface any aspect of the characteristic the verse evidence has not yet addressed, and does that absence call for further verse investigation?"

---

## Operation B — SOFT-DELETE (obsolete codes)

For each code below, set `deleted = 1`. The **→ primary** column records where the question's content now lives (the primary's rewritten text in Operation A already carries it). If `wa_obs_question_catalogue` has a fold-provenance column (e.g. `folded_into` / `superseded_by`), set it to the primary code; if not, the mapping is held in this document and the companion rewrite's `absorbs:` lines.

| Code | → primary | Reason |
|---|---|---|
| T0.1.3 | T0.1.2 | silence first-class (God-possession silence read in the presence/absence pattern) |
| T0.4.2 | T0.4.1 | typological direction folded into the typology question |
| T0.4.3 | T0.4.1 | "note none" — silence first-class |
| T1.5.3 | T1.5.1 | "note silence" — silence first-class |
| T1.6.2 | T1.6.1 | states/qualities-established merged into what-it-produces |
| T2.1.3 | T2.1.2 | spirit-level "reveal" folded into location synthesis |
| T2.1.4 | T2.1.1 | spirit-level "note silence" absorbed by answer-set audit |
| T2.2.1 | T2.1.1 | soul-level presence folded into consolidated location question |
| T2.2.2 | T2.1.2 | soul-level "reveal" folded into location synthesis |
| T2.2.3 | T2.1.1 | soul-level "note silence" absorbed by answer-set audit |
| T2.3.1 | T2.1.1 | heart presence folded into consolidated location question |
| T2.3.2 | T2.1.2 | heart-function "reveal" folded into location synthesis |
| T2.3.3 | T2.1.1 | heart "note silence" absorbed by answer-set audit |
| T2.4.1 | T2.1.1 | mind presence folded into consolidated location question |
| T2.4.2 | T2.1.2 | mind-function "reveal" folded into location synthesis |
| T2.4.3 | T2.1.1 | mind "note silence" absorbed by answer-set audit |
| T2.5.1 | T2.1.1 | other-subset presence folded into consolidated location question |
| T2.5.2 | T2.1.2 | other-subset "reveal" folded into location synthesis |
| T2.5.3 | T2.1.1 | other-subset "note silence" absorbed by answer-set audit |
| T2.6.1 | T2.1.1 | body-part presence folded into consolidated location question |
| T2.6.2 | T2.1.2 | body-link function ("reveal") folded into location synthesis |
| T2.6.3 | T2.1.1 | body-part "note silence" absorbed by answer-set audit |
| T2.7.2 | T2.7.1 | body-direction consequence folded into the direction question |
| T2.7.3 | T2.7.1 | body-direction "note silence" — silence first-class |
| T2.9.3 | T2.9.2 | origin context-variation folded into single/multiple question |
| T2.10.2 | T2.10.1 | movement sequence/pattern folded into the movement question |
| T2.10.3 | T2.10.1 | movement "note silence" — silence first-class |
| T4.1.4 | T4.1.1 | "note silence" — silence first-class |
| T4.2.4 | T4.2.1 | "note silence" — silence first-class |
| T4.3.4 | T4.3.1 | "note silence" — silence first-class |
| T4.4.4 | T4.4.1 | "note silence" — silence first-class |
| T4.5.4 | T4.5.1 | "note silence" — silence first-class |
| T4.6.4 | T4.6.1 | "note silence" — silence first-class |
| T5.1.3 | T5.1.1 | "note silence" — silence first-class |
| T5.2.2 | T5.2.1 | states-and-what-the-sequence-reveals folded into the sequence question |
| T5.2.3 | T5.2.1 | "note silence" — silence first-class |
| T5.3.3 | T5.3.1 | "note silence" — silence first-class |
| T5.4.3 | T5.4.1 | "note silence" — silence first-class |
| T5.5.2 | T5.5.1 | role-in-arc folded into the participation question |
| T5.5.3 | T5.5.1 | "note silence" — silence first-class |
| T5.6.2 | T5.6.1 | anticipation folded into the orientation question |
| T5.6.3 | T5.6.1 | "note silence" — silence first-class |
| T6.1.3 | T6.1.1 | "no significant pattern" note — silence first-class |
| T6.2.3 | T6.2.1 | "no pattern" note — silence first-class |
| T6.3.4 | T6.3.1 | "note silence" — silence first-class |
| T6.4.4 | T6.4.1 | "note silence" — silence first-class |
| T6.5.4 | T6.5.1 | "no distinction work required" note — silence first-class |

**Total soft-deletes: 47.**

---

## Post-run verification (CC reports back)

1. `SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE deleted = 0 AND tier IS NOT NULL;` → expect **126**.
2. `SELECT COUNT(*) ... WHERE deleted = 1 AND <code IN the 47 list>;` → expect **47** newly soft-deleted (confirm none were already deleted before this run).
3. Spot-check the five repurposed/edited keep codes carry the new text: **T2.1.1, T2.1.2** (repurposed) and **T1.7.2, T2.9.1, T2.10.1** (other-spirits edit).
4. Confirm no code was both text-updated and soft-deleted (the keep and obsolete sets are disjoint; 126 + 47 = 173, no overlap).
5. Confirm no INSERT and no renumber occurred.

Per GR-PROG-005 and GR-PROC-004, CC builds the JSON patch from this document and presents it for researcher review before applying. This document states the intended operations; it is not itself the patch.

*End of v1_0.*
