# Tier catalogue → IBA raw-data mapping

> Escalation #1007. Purpose: for each live Tn.n.n tier question in `wa_obs_question_catalogue`
> (bible_research.db), determine whether it is directly answerable from IBA's own raw data tables
> (iba.db) — and if so, from which table/field — or whether it is not.
>
> **v2 — corrects a significant miss in v1** (archived:
> [`archive/tier-catalogue-iba-raw-data-mapping-v1-20260829.md`](archive/tier-catalogue-iba-raw-data-mapping-v1-20260831.md)).
> v1 required a pre-classified, controlled-vocabulary FIELD to count a question as answerable, and
> on that basis marked almost every "in this verse" question No. That standard was too strict: for
> most tier questions, IBA holds no such field, but it does hold the complete raw evidentiary
> material — `verse.text` plus the full word-by-word gloss chain
> (`verse_lexical.resolved_sense`/`strong_meaning_parsed`) — that a reader (researcher or AI) uses
> to determine the answer, verse by verse, for every verse in the DB. That is in fact how the live
> method is meant to work (`wa-verse-analysis-method-v1-20260702.md`: verse-first, read-back).
> Re-scored on that corrected basis, **43 questions move from No to Partial** (see each entry's
> note for the reasoning). Part 1 is unchanged; Part 2 gains a new subsection below; Part 3 is
> fully re-tabulated.

---

## Part 1 — The tier questions, isolated

Source: `database/bible_research.db`, table `wa_obs_question_catalogue`, filtered to
`status='active' AND deleted=0 AND question_code` matching the pattern `Tn.n.n` (one question per
tiered code). **126 rows** — this matches the live tiered-question count in
[`obs-catalogue-v2-20260829.md`](obs-catalogue-v2-20260829.md)'s "Tier structure" section, pulled
fresh here directly from the table rather than from that report. 63 further `Tn.n.n`-shaped rows
exist in the catalogue but are non-live (`dropped` or soft-deleted `active` rows superseded by a
`folded_into=` note — see that report's "Lifecycle conflicts" section) and are excluded here.

| Tier | Code | Component | Question |
|---|---|---|---|
| T0 | `T0.1.1` | Divine Nature Reflected | In this verse, is the characteristic predicated of God or otherwise related to God; if so, in what relation (God as the one who bears it, acts, gives it, or is its object)? Record the relation, or record that it is not related to God here. |
| T0 | `T0.1.2` | Divine Nature Reflected | Across the characteristic's verses, is it ever borne by God himself or only by the creature, and what does that pattern of presence or absence indicate for its place in the human person and in the divine image? |
| T0 | `T0.2.1` | Created Purpose | Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none. |
| T0 | `T0.2.2` | Created Purpose | Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable? |
| T0 | `T0.2.3` | Created Purpose | Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none. |
| T0 | `T0.3.1` | Image-Bearer Expression | From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none. |
| T0 | `T0.3.2` | Image-Bearer Expression | Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God? |
| T0 | `T0.3.3` | Image-Bearer Expression | Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced? |
| T0 | `T0.4.1` | Typological Significance | Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none. |
| T1 | `T1.1.1` | Name and Naming | What is the characteristic called in the programme, and what does the name signal about its essential nature? |
| T1 | `T1.1.2` | Name and Naming | What do the primary Hebrew and Greek terms show at the definitional level? |
| T1 | `T1.1.3` | Name and Naming | What directional, relational, or constitutional implication does the name carry? |
| T1 | `T1.2.1` | Kind | What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else? |
| T1 | `T1.2.2` | Kind | Is the characteristic simple in structure, or does it combine constituent elements; if compound, which? |
| T1 | `T1.3.1` | Boundary | What stands against the characteristic as its structural opposite — the inner-being reality that excludes it? |
| T1 | `T1.3.2` | Boundary | What does the characteristic exclude or resist at its edge? |
| T1 | `T1.3.3` | Boundary | Where does the characteristic end and another thing begin — what is it not? |
| T1 | `T1.4.1` | Modes of Operation | In what distinct mode(s) does the characteristic operate within the inner person in this verse — including its grammatical/stem form and the manner of functioning? |
| T1 | `T1.4.2` | Modes of Operation | Does the mode of operation vary by context, direction, or constitutional level; if so, how? |
| T1 | `T1.4.3` | Modes of Operation | Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none. |
| T1 | `T1.5.1` | Immediate Response | What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none. |
| T1 | `T1.5.2` | Immediate Response | Across the verses, is that immediate response consistent or varied? |
| T1 | `T1.6.1` | Sustained Effect | What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none. |
| T1 | `T1.6.3` | Sustained Effect | How does the sustained effect differ from the immediate response (T1.5)? |
| T1 | `T1.7.1` | Conditions of Reception | Under what inner conditions does the characteristic take hold or operate rightly? |
| T1 | `T1.7.2` | Conditions of Reception | Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)? |
| T1 | `T1.7.3` | Conditions of Reception | What is the inner-being state of the person in whom the characteristic is present but does not take hold? |
| T2 | `T2.1.1` | Spirit-Level Location | At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none. |
| T2 | `T2.1.2` | Spirit-Level Location | Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating? |
| T2 | `T2.7.1` | Body — Direction | Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none. |
| T2 | `T2.9.1` | Origin and Source | Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated? |
| T2 | `T2.9.2` | Origin and Source | Across the verses, is the origin single or multiple, and does it change with context? |
| T2 | `T2.10.1` | Constitutional Movement | Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none. |
| T3 | `T3.1.1` | Perception | In this verse, does the characteristic engage the perceptive faculty — the inner senses (hearing, sight, taste, touch, smell) and spiritual discernment — and if so, which inner sense and how? Record none if it does not. |
| T3 | `T3.1.2` | Perception | How does the characteristic affect perception in the person here — and record no effect if none is evidenced. |
| T3 | `T3.1.3` | Perception | Across the verses, what does the pattern of engagement and non-engagement with perception indicate about the characteristic's nature? |
| T3 | `T3.2.1` | Cognition | In this verse, does the characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how? Record none if it does not. |
| T3 | `T3.2.2` | Cognition | How does the characteristic affect cognition in the person here — and record no effect if none is evidenced. |
| T3 | `T3.2.3` | Cognition | Across the verses, what does the pattern of engagement and non-engagement with cognition indicate about the characteristic's nature? |
| T3 | `T3.3.1` | Memory | In this verse, does the characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how? Record none if it does not. |
| T3 | `T3.3.2` | Memory | How does the characteristic affect memory in the person here — and record no effect if none is evidenced. |
| T3 | `T3.3.3` | Memory | Across the verses, what does the pattern of engagement and non-engagement with memory indicate about the characteristic's nature? |
| T3 | `T3.4.1` | Affect | In this verse, does the characteristic engage the affective faculty — feeling and emotional experience — and if so, how? Record none if it does not. |
| T3 | `T3.4.2` | Affect | How does the characteristic affect the affective faculty in the person here — and record no effect if none is evidenced. |
| T3 | `T3.4.3` | Affect | Across the verses, what does the pattern of engagement and non-engagement with affect indicate about the characteristic's nature? |
| T3 | `T3.5.1` | Creativity | In this verse, does the characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how? Record none if it does not. |
| T3 | `T3.5.2` | Creativity | How does the characteristic affect creativity in the person here — and record no effect if none is evidenced. |
| T3 | `T3.5.3` | Creativity | Across the verses, what does the pattern of engagement and non-engagement with creativity indicate about the characteristic's nature? |
| T3 | `T3.6.1` | Volition | In this verse, does the characteristic engage the volitional faculty — the capacity to choose — and if so, how? Record none if it does not. |
| T3 | `T3.6.2` | Volition | How does the characteristic affect volition in the person here — including its capacity, its interaction with other characteristics, and the constraints under which it operates — and record no effect if none is evidenced. |
| T3 | `T3.6.3` | Volition | Across the verses, what does the pattern of engagement and non-engagement with volition indicate about the characteristic's nature? |
| T3 | `T3.7.1` | Agency | In this verse, does the characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how? Record none if it does not. |
| T3 | `T3.7.2` | Agency | How does the characteristic affect agency in the person here — and record no effect if none is evidenced. |
| T3 | `T3.7.3` | Agency | Across the verses, what does the pattern of engagement and non-engagement with agency indicate about the characteristic's nature? |
| T3 | `T3.8.1` | Moral Evaluation | In this verse, does the characteristic engage the moral-evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how? Record none if it does not. |
| T3 | `T3.8.2` | Moral Evaluation | How does the characteristic affect moral evaluation in the person here — and record no effect if none is evidenced. |
| T3 | `T3.8.3` | Moral Evaluation | Across the verses, what does the pattern of engagement and non-engagement with moral evaluation indicate about the characteristic's nature? |
| T3 | `T3.9.1` | Conscience | In this verse, does the characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how? Record none if it does not. |
| T3 | `T3.9.2` | Conscience | How does the characteristic affect conscience in the person here — and record no effect if none is evidenced. |
| T3 | `T3.9.3` | Conscience | Across the verses, what does the pattern of engagement and non-engagement with conscience indicate about the characteristic's nature? |
| T3 | `T3.10.1` | Conscientiousness | In this verse, does the characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how? Record none if it does not. |
| T3 | `T3.10.2` | Conscientiousness | How does the characteristic affect conscientiousness in the person here — and record no effect if none is evidenced. |
| T3 | `T3.10.3` | Conscientiousness | Across the verses, what does the pattern of engagement and non-engagement with conscientiousness indicate about the characteristic's nature? |
| T3 | `T3.11.1` | Relational Capacity | In this verse, does the characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how? Record none if it does not. |
| T3 | `T3.11.2` | Relational Capacity | How does the characteristic affect relational capacity in the person here — and record no effect if none is evidenced. |
| T3 | `T3.11.3` | Relational Capacity | Across the verses, what does the pattern of engagement and non-engagement with relational capacity indicate about the characteristic's nature? |
| T4 | `T4.1.1` | Divine Interface — God to Human | In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not. |
| T4 | `T4.1.2` | Divine Interface — God to Human | On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows? |
| T4 | `T4.1.3` | Divine Interface — God to Human | What does God's extension of the characteristic show about his disposition toward the human person? |
| T4 | `T4.2.1` | Divine Interface — Human to God | In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not. |
| T4 | `T4.2.2` | Divine Interface — Human to God | What inner posture does this movement require, as the evidence shows? |
| T4 | `T4.2.3` | Divine Interface — Human to God | What does the human-to-God direction of the characteristic show about the person's relationship with God? |
| T4 | `T4.3.1` | Human Interface — Giving | In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not. |
| T4 | `T4.3.2` | Human Interface — Giving | What inner conditions or orientations in the giver accompany genuine extension of the characteristic? |
| T4 | `T4.3.3` | Human Interface — Giving | What does the evidence show a person must have received or become before they extend the characteristic? |
| T4 | `T4.4.1` | Human Interface — Receiving | In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not. |
| T4 | `T4.4.2` | Human Interface — Receiving | What inner conditions accompany or block uptake of the characteristic from another person? |
| T4 | `T4.4.3` | Human Interface — Receiving | What is the inner-being state of the person who meets the characteristic from another but does not take it up? |
| T4 | `T4.5.1` | Human Interface — Boundaries | Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how? |
| T4 | `T4.5.2` | Human Interface — Boundaries | Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows? |
| T4 | `T4.5.3` | Human Interface — Boundaries | What does the evidence show about the relational scope of the characteristic — who is included and who is not? |
| T4 | `T4.6.1` | Spiritual Beings Interface | In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not. |
| T4 | `T4.6.2` | Spiritual Beings Interface | Is the characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial powers — as the evidence shows? |
| T4 | `T4.6.3` | Spiritual Beings Interface | Is the characteristic communicated, strengthened, or mediated through angelic ministry in the evidence? |
| T5 | `T5.1.1` | Nature of Transformation | In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown. |
| T5 | `T5.1.2` | Nature of Transformation | Is the transformation reversible or irreversible in the evidence? |
| T5 | `T5.2.1` | Sequence of Inner States | Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown. |
| T5 | `T5.3.1` | Mechanism of Change | In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown. |
| T5 | `T5.3.2` | Mechanism of Change | Does the mechanism differ across contexts in the evidence; if so, how? |
| T5 | `T5.4.1` | Suffering and Affliction | In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown. |
| T5 | `T5.4.2` | Suffering and Affliction | What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown. |
| T5 | `T5.5.1` | Formation and Sanctification | In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown. |
| T5 | `T5.6.1` | Eschatological Trajectory | In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown. |
| T6 | `T6.1.1` | Co-occurrence | Which adjacent characteristics appear alongside this one in the verse evidence, and how frequently? Record none if no significant co-occurrence appears. |
| T6 | `T6.1.2` | Co-occurrence | What does the co-occurrence pattern show about this characteristic's place in the inner-being landscape? |
| T6 | `T6.2.1` | Sequential Relationships | Does the evidence show this characteristic consistently preceding, following, or accompanying another in a sequence; if so, which and how? Record none if no sequence appears. |
| T6 | `T6.2.2` | Sequential Relationships | What does the sequence show — is the relationship causal, developmental, or correlational? |
| T6 | `T6.3.1` | Causal and Constitutive Relationships | Does this characteristic produce another in the evidence, and if so which, and by what mechanism? Record none if none is shown. |
| T6 | `T6.3.2` | Causal and Constitutive Relationships | Is this characteristic produced by another, and if so which? |
| T6 | `T6.3.3` | Causal and Constitutive Relationships | Is this characteristic a constituent element of another, or another a constituent of this one? |
| T6 | `T6.4.1` | Vocabulary and Root Sharing | Which vocabulary terms, if any, does this characteristic share with other characteristics in the programme? Record none if none is shown. |
| T6 | `T6.4.2` | Vocabulary and Root Sharing | Does the sharing extend to root-level architecture — a shared root generating terms across two or more characteristics? |
| T6 | `T6.4.3` | Vocabulary and Root Sharing | What does the vocabulary sharing show about the conceptual relationship between the characteristics? |
| T6 | `T6.5.1` | Distinctions | Which adjacent characteristic most closely resembles this one, and what precisely distinguishes them? |
| T6 | `T6.5.2` | Distinctions | Where the evidence shows apparent overlap, what is the precise boundary? |
| T6 | `T6.5.3` | Distinctions | Is the distinction from the nearest neighbour one of degree, kind, direction, or constitutional level? |
| T7 | `T7.1.1` | Lexical and Semantic Analysis | What are the primary Hebrew and Greek terms for this characteristic, and what do their root meanings show? |
| T7 | `T7.1.2` | Lexical and Semantic Analysis | What is the grammatical range of the primary term (noun, verb, adjective, participle), and what does that range show about how the characteristic operates? |
| T7 | `T7.1.3` | Lexical and Semantic Analysis | What is the semantic range of the primary term — across what breadth of meaning does it operate? |
| T7 | `T7.1.4` | Lexical and Semantic Analysis | Does the vocabulary include terms distinguishing distinct aspects — disposition versus act, received versus given, condition versus quality? Record which, or none. |
| T7 | `T7.1.5` | Lexical and Semantic Analysis | Does the vocabulary include a term for the structural opposite or absence of this characteristic? Record it, or none. |
| T7 | `T7.1.6` | Lexical and Semantic Analysis | Does the vocabulary include a person-type term — one for the person who habitually possesses or exercises this characteristic? Record it, or none. |
| T7 | `T7.1.7` | Lexical and Semantic Analysis | Does the vocabulary include a supplication or seeking term — one for the act of seeking this characteristic from another? Record it, or none. |
| T7 | `T7.1.8` | Lexical and Semantic Analysis | What does the relationship between the OT Hebrew and NT Greek vocabulary show about continuity or development of the characteristic across the Testaments? |
| T7 | `T7.1.9` | Lexical and Semantic Analysis | Is there a term newly coined in the NT period for this characteristic; if so, what does the coinage show? Record it, or none. |
| T7 | `T7.1.10` | Lexical and Semantic Analysis | What does the full vocabulary arc show about the characteristic's complete semantic range? |
| T7 | `T7.2.1` | Verse and Literary Interpretation | What is the function of the primary term within its primary verse — what role does it play in the sentence and argument? |
| T7 | `T7.2.2` | Verse and Literary Interpretation | What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic), and what does that form require for responsible interpretation? |
| T7 | `T7.2.3` | Verse and Literary Interpretation | What is the logical structure of the key arguments in the verse evidence — premises and conclusions? |
| T7 | `T7.2.4` | Verse and Literary Interpretation | What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological), and what does that setting show? |
| T7 | `T7.2.5` | Verse and Literary Interpretation | Does any verse function as the primary anchor — the one most fully and directly expressing the characteristic's essential character? Record it, or none. |
| T7 | `T7.2.6` | Verse and Literary Interpretation | What does the primary anchor verse show that no other verse shows? |
| T7 | `T7.3.1` | Human Science Frameworks | Which human-science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) serves as the most useful interpretive lens for this characteristic? |
| T7 | `T7.3.2` | Human Science Frameworks | Where the framework illuminates the verse evidence — making a finding more coherent or complete — what does it show? |
| T7 | `T7.3.3` | Human Science Frameworks | Where the verse evidence and the framework diverge, what does the divergence show? |
| T7 | `T7.3.4` | Human Science Frameworks | Does the framework surface any aspect of the characteristic the verse evidence has not yet addressed, and does that absence call for further verse investigation? |

---

## Part 2 — How the IBA raw data that touches "the lexical" actually fits together

Two structurally separate layers exist in `iba.db`. Understanding the seam between them is the
whole basis for Part 3's verdicts.

### Layer A — the base lexical layer (rich, fully populated, word/Strong's-keyed)

```
verse (29,759 rows)                         word_registry (180 English words)
  │  .text = full ESV_th verse text                │
  │  .osisId = Matt.23.28 etc.                      ▼
  ▼                                            word_strong (4,874 rows)
span (391,417 rows)                                 │  word_id → word_registry.id
  │  one row per interlinear "tag" in a verse        │  strong → strong.strongNumber
  │  .surface = the English word                     │
  │  .strong_variant = space-joined Strong's          ▼
  │    codes for that tag, e.g. "H7760A H5921A     cluster_strong (7,609 rows)
  │    H3820A" for one English word                   │  strong → strong.strongNumber
  │  .morph_code = space-joined morph parse,           │  cluster_code → cluster.cluster_code
  │    aligned 1:1 with strong_variant                 ▼
  ▼                                             cluster (51 rows: M01…M47 + FLAG/T2)
verse_lexical (960,627 rows)                          .short_name, .description, .gloss
  │  ONE ROW PER CODE, not per span —
  │  span.strong_variant "H7760A H5921A H3820A"
  │  becomes 3 verse_lexical rows (code_ordinal 0,1,2)
  │  .strong, .morph_code = that code's own slice
  │  .role = content | function
  │  .status = resolved | unregistered
  │  .resolved_sense = the stem/voice-selected gloss
  ▼
strong (15,293 rows) ── strong_sense / strong_meaning_parsed / strong_meaning_tree /
  .stepGloss, .accentedUnicode,        strong_lsj_parsed (Greek) / strong_mounce_parsed (Greek) /
  .stepTransliteration, .language      strong_lexicon — full lexicon-entry chain per lemma_key
  │
  ▼
strong_related (87,535 rows) — STEP's "related terms" per Strong's, UNDIFFERENTIATED
  (no relation-type column — cognate, derivative, and cross-reference all look the same)
strong_verse (132,718 rows) — concordance: every verse a Strong's occurs in
```

**Worked, verified example** (Dan 1:8, "Daniel resolved…"): `span` position 1, surface
`"resolved"`, `strong_variant = "H7760A H5921A H3820A"`, `morph_code = "HVqw3ms HR HNcmsc"`. That
produces three `verse_lexical` rows; the H3820A one carries `resolved_sense = "stepGloss: heart —
inner man, mind, will, heart, understanding…"` — pulled straight from `strong_meaning_parsed`.
This chain is exhaustive, current, and cleanly keyed all the way from an English `word_registry`
word down to a specific grammatical form in a specific verse.

### Layer A, in full, is a per-verse reading base — not just a per-word lookup table

v1 under-used this. Pulling the **complete** `verse_lexical` result set for Dan 1:8 — every span,
every code, every gloss, not just the one Strong's I originally cherry-picked — shows what's
actually there:

```
pos=1 'resolved'  H7760A  "to set: make — to put, place, set, appoint, make; ... to set, direct,
                            direct toward; to extend (compassion) (fig); ..."
pos=1 'resolved'  H5921A  "upon — prep; upon, on the ground of, ..."
pos=1 'resolved'  H3820A  "heart — inner man, mind, will, heart, understanding; ... inclination,
                            resolution, determination (of will); conscience; ..."
pos=4 'defile'    H1351   "to defile — to defile, pollute, desecrate; to defile oneself"
pos=9 'asked'     H1245   "to seek — to seek, require, desire, exact, request; ..."
                                                                       [25 rows total, this verse]
```

This is a **complete, word-by-word, context-fitted gloss reading of the entire verse** — every
verse in the DB has this (960,627 `verse_lexical` rows total). It is exactly the material a
researcher (or an AI reading on the researcher's behalf) uses to answer an "in this verse, does
the characteristic do X" question: read the verse's own text (`verse.text`) alongside the gloss of
every word in it, and judge. This consumption pattern isn't hypothetical — it's what
`report.verse_span_meaning` (a real, registered step,
`iba.app.handlers.reports:verse_span_meaning_report`, 45 passages already rendered under
`iba/app/verse-analysis/`) exists to assemble and hand to a reader.

**This changes the answerability standard.** v1 asked "is there a pre-classified field?" and
mostly got No. The right question is "is the raw evidentiary material present, complete, and
verse-keyed, such that a reader can determine the answer from it?" — and for the very large
majority of the catalogue's *single-verse* sub-questions ("in this verse, does…", "…here"), the
answer is yes: `verse.text` + `verse_lexical.resolved_sense` (+ `strong_meaning_parsed` for
deeper lexical detail where needed) supply that material, completely, for every verse. The
catalogue's own classification label (which faculty, which relation-type, which mechanism) is
still a judgment call on top of the reading — so these move to **Partial**, not Yes — but Partial
grounded in complete, universal, verse-keyed raw data is a materially different, and much
stronger, answer than "No, nothing here."

**What does NOT change under this correction:** cross-verse synthesis questions ("across the
verses, what does the pattern show…"), questions explicitly framed "as the evidence shows" (T4's
second- and third-order questions), and questions asking for an external classification framework
that a single verse's own words can't supply (typology, eschatology, literary genre, human-science
lenses, argument structure) all remain No — the miss corrected here is specifically the
single-verse, first-order reading questions, not the whole catalogue.

### Layer B — the "debate" / phenomenology layer (schema built, minimally populated, HIB/passage-keyed — NOT word/Strong's-keyed)

```
passage (18,558 rows) — maximal verse-runs, registered broadly across the whole Bible
  │  .story_summary, .feasibility_note, .open_decisions_note (Step 2 narrative)
  ▼
verse_passage (25,690) ── verse
hib (63 rows) — a NAMED OR IMPLICIT PERSON appearing in a passage's narrative
  │  .kind = named_individual | unnamed_individual | named_collection |
  │          unnamed_collection | implicit_individual | implicit_collection
  │  .label = "Daniel", "Ashpenaz", "the four youths"...
  ▼
verse_hib (485) — this HIB is present/candidate in this verse
  ▼
phenomenon (177 rows, 121 LIVE — see below)
  │  .hib_id, .verse_id, .passage_id
  │  .description = a state/disposition/characteristic OF THIS HIB in this verse
  │  .textual_warrant = the grounding clause, Strong's sometimes cited IN FREE TEXT
  │  .status = stated | inferred | silent
  ▼
operation (177 rows, mirrors phenomenon 1:1)
  │  .process = intended small controlled vocabulary (come from/go to/impact on/
  │             emerge/go away/become evident) — SEE FINDING 6, this is not how it's
  │             actually populated
  │  .decision = retain | set_aside | retain_referential | recorded_silence
  ▼
operation_party (250 rows) — who/what is source/target of the operation
  .role = source | target
  .kind = self | human | non_human | object_situation | none  — NO "divine" value
  .hib_id → hib.id (nullable)

passage_linkage (3 rows) / passage_emergent_question (4) / passage_insufficiency (1) /
passage_validation_note (4) — all essentially unpopulated pilot data
```

**Worked, verified example, same verse** (Dan 1:8): `verse_hib` lists two HIBs present — Daniel
(id 47) and Ashpenaz (id 50). Daniel's `phenomenon` (id 100): *"Daniel's own deliberate resolve of
will not to defile himself… a fixed inner purpose, not a passing preference"*, `status='stated'`,
`textual_warrant` citing `H7760A`/`H3820A` explicitly. Its `operation` (id 159): `process='emerge'`,
`operation_party` rows: source `kind='self', detail="Daniel's own will/resolve"`; target
`kind='object_situation', detail="the king's food and the wine"`. This is rich, real content — and,
notably, its `textual_warrant`/`observation_text` draw on **exactly the same Layer A lexical
evidence** (the same `H7760A`/`H3820A` glosses) that Layer A alone already exposes for every verse.
Layer B is a *pre-digested reading* of a HIB's phenomenon, done by hand for Daniel; Layer A is the
*raw material that reading was made from*, present everywhere.

### The seam that still matters for the No verdicts

**Layer B has no foreign key to a Strong's code, a `cluster_code`, or a `word_registry` row**, and
its live population is Daniel-only (121 phenomena). Where a tier question genuinely needs Layer
B's *pre-digested, HIB-scoped* content specifically (not just the underlying lexical evidence) —
or needs cross-verse synthesis, an external classification scheme, or a comparison across two
different characteristics — the seam from Part 2 v1 still applies in full and the verdict is still
No. The correction here is that far more of the catalogue than v1 credited can be answered from
Layer A's reading material directly, without needing Layer B at all.

### Concrete findings behind the No verdicts that remain

1. **No FK from Layer B to a characteristic/Strong's/cluster.**
2. — (folded into 1)
3. **Layer B's live population is Daniel only** — 121 live `phenomenon` rows (56 more soft-deleted),
   all under `Dan` passages.
4. **No constitutional-level, faculty, "kind of phenomenon," transformation/mechanism, or
   relational-interface enum exists anywhere in IBA.** Checked `cfg_enum` in full (37 distinct
   enum names) — none map to T2's spirit/soul/heart/mind/body-part categories, T3's eleven
   faculties, T1.2's act/disposition/condition/quality, or T5's transformation vocabulary. There is
   no pre-computed *classification*, even though (per the correction above) the raw material to
   make that classification by reading is present and complete.
5. **`strong_related` (87,535 rows) carries no relation-type column.** Sampled `H3820A` (leb):
   its 10 related rows mix true cognates (`H3824` levav, `H3826` libbah — "heart"), a homonym root
   (`H3823B` "to bake"), and an apparently unrelated cross-reference (`H6965B` "to arise") with no
   flag distinguishing them. Antonym/opposite, person-type, and aspect-marking vocabulary
   questions (T1.3, T7.1.4-7) fail on this gap even under the corrected reading standard, because
   they ask about the WHOLE root/vocabulary family, not one verse's words.
6. **`operation.process` is not actually a controlled vocabulary in the live data.** Of 177
   `operation` rows, 61 are NULL; the documented small vocabulary (come from/go to/impact
   on/emerge/go away/become evident) appears only ~19 times combined; the remaining ~90-plus rows
   hold full prose sentences written straight into the `process` field instead of
   `description_text`.
7. **`operation_party.kind` has no "divine" value.** God, angelic beings, and the vision-source
   itself are all sampled as `non_human` alike in Dan 8, distinguished only by free-text `detail`.
8. **`span_candidate.candidate_tag`** (83,914 rows, English-phrase labels including many literal
   "heart"/"soul"/body-part tags) is frozen legacy output — its writer (`candidate.set`) was
   retired 2026-07-23. Not counted as a live input anywhere below (consistent with programme
   convention on inactive writers).
9. **T6.1 (co-occurrence)** is answerable by a clean structural join independent of both the
   reading correction and Layer B: `verse_lexical.strong` joined through `cluster_strong` on
   `verse_lexical.verse_id`.

---

## Part 3 — The mapping, tier by tier

**Answerable? key** — **Yes**: a real field/join in IBA raw data directly supplies the answer.
**Partial**: raw data supplies part of the answer, a genuine structured proxy, or (per the
correction above) the complete evidentiary material for a grounded single-verse reading, with a
real remaining interpretive/classification gap. **No**: nothing in IBA raw data answers this; it
requires cross-verse synthesis with no structural aggregation, an external classification
framework, or a comparison across characteristics that isn't tracked anywhere.

**Totals: 5 Yes · 50 Partial · 71 No** (of 126) — up from v1's 5 Yes / 7 Partial / 114 No.

### T0

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T0.1.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Is God the subject/agent/giver/object here -- readable directly from `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T0.1.2` | **No** | — | Cross-verse synthesis over many T0.1.1 readings -- not itself stored or computed anywhere; would need every verse's T0.1.1 reading compiled by hand. |
| `T0.2.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T0.2.2` | **No** | — | Cross-verse theological-category synthesis (created-design vs fallen; future-fullness orientation) -- not stored, not a single-verse reading. |
| `T0.2.3` | **No** | — | Cross-verse theological-category synthesis (created-design vs fallen; future-fullness orientation) -- not stored, not a single-verse reading. |
| `T0.3.1` | **No** | — | Built from T0.1/T0.2 readings plus a further theological-category judgment (divine-likeness aspect, shared-vs-analogue, image condition) -- synthesis, not stored. |
| `T0.3.2` | **No** | — | Built from T0.1/T0.2 readings plus a further theological-category judgment (divine-likeness aspect, shared-vs-analogue, image condition) -- synthesis, not stored. |
| `T0.3.3` | **No** | — | Built from T0.1/T0.2 readings plus a further theological-category judgment (divine-likeness aspect, shared-vs-analogue, image condition) -- synthesis, not stored. |
| `T0.4.1` | **No** | — | Typological/covenantal/eschatological/christological classification is a canon-wide theological framework applied to the verse, not recoverable from this verse's own text/lexicon alone -- same category as T5.6's eschatology and T7.2.2's genre. |

### T1

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T1.1.1` | **Partial** | `word_registry.word` | Gives the English name as registered. The second half of the question ("what the name signals about essential nature") is interpretation, not a stored value. |
| `T1.1.2` | **Yes** | `word_strong.strong` -> `strong.stepGloss/accentedUnicode/stepTransliteration`, `strong_sense.head`, `strong_meaning_parsed`, `strong_meaning_tree`, `strong_lsj_parsed`, `strong_mounce_parsed` | Full definitional lexicon chain for every Hebrew/Greek code onboarded for the word. `word_strong` does not flag which code is "primary" (that OWNER/XREF distinction lives only in bible_research.db) -- a human/process choice is still needed to pick the primary term(s). |
| `T1.1.3` | **No** | — | Directional/relational/constitutional implication of the name is interpretive synthesis over the definitional data (T1.1.2), not a stored field. |
| `T1.2.1` | **Partial** | `span.morph_code` / `verse_lexical.morph_code` (part of speech) + `verse_lexical.resolved_sense` gloss text | Grammatical category (verb/noun/adjective/participle) plus the gloss's own wording (a gloss reading "act of..." vs "state of..." is common in `strong_meaning_parsed`) are real, structured signal that constrain but do not equal the catalogue's own act/disposition/condition/quality classification -- that mapping is still a judgment call. |
| `T1.2.2` | **No** | — | Simple-vs-compound is about the conceptual structure of the characteristic, not the morphology of any one span; not tracked. |
| `T1.3.1` | **No** | — | `strong_related` lists STEP's "related terms" but carries no relation-type column (Finding 5) -- antonym, derivative, and root-cognate are all indistinguishable, so a structural opposite cannot be isolated. |
| `T1.3.2` | **No** | — | `strong_related` lists STEP's "related terms" but carries no relation-type column (Finding 5) -- antonym, derivative, and root-cognate are all indistinguishable, so a structural opposite cannot be isolated. |
| `T1.3.3` | **No** | — | `strong_related` lists STEP's "related terms" but carries no relation-type column (Finding 5) -- antonym, derivative, and root-cognate are all indistinguishable, so a structural opposite cannot be isolated. |
| `T1.4.1` | **Partial** | `span.morph_code` / `verse_lexical.morph_code` | The grammatical/stem-form half is directly sourced (e.g. Dan 1:8's `H7760A` "sim" parses `HVqw3ms` -- Qal wayyiqtol). "Manner of functioning" beyond the parse is not stored. |
| `T1.4.2` | **Partial** | `verse_lexical.morph_code` compared across `strong_verse` occurrences; `verse.osisId` (book) for context | Whether the attested grammatical forms vary is computable by aggregation. "Constitutional level" is not tracked at all (Finding 4), so that half of the comparison is unavailable. |
| `T1.4.3` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | A speech/command verb governing the characteristic would show directly in the verse's own text and its neighbouring word glosses. Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T1.5.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. This is exactly what Layer B's `phenomenon`/`operation` were built to capture in free text for Daniel (Part 2) -- the same evidentiary base underlies both, but this reading path works for every verse in the DB, not only Daniel. |
| `T1.5.2` | **No** | — | Cross-verse consistency check over many T1.5.1 readings -- not itself stored. |
| `T1.6.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T1.6.3` | **No** | — | Comparative synthesis between two already-derived readings (T1.5 vs T1.6) -- not stored. |
| `T1.7.1` | **No** | — | Framed as a cross-verse/general-condition question ("under what inner conditions"), not tied to one verse -- requires compiling and generalising over every occurrence, not a single reading. |
| `T1.7.2` | **No** | — | Framed as a cross-verse/general-condition question ("under what inner conditions"), not tied to one verse -- requires compiling and generalising over every occurrence, not a single reading. |
| `T1.7.3` | **No** | — | Framed as a cross-verse/general-condition question ("under what inner conditions"), not tied to one verse -- requires compiling and generalising over every occurrence, not a single reading. |

### T2

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T2.1.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | When the constitutional term itself is literally named in the verse (e.g. Dan 1:8's own `H3820A` leb/"heart" span, glossed "inner man, mind, will, heart..."), that's directly visible in the reading. No structured level-tag exists (Finding 4), so this is reading-grounded, not a field lookup -- and silent/implicit-only engagement (no matching vocabulary literally present) would be missed by this reading path. |
| `T2.1.2` | **No** | — | Cross-verse pattern over every T2.1.1 reading, including a judgment about which levels are DEPTH/seat vs merely mentioned -- not stored. |
| `T2.7.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Weaker than T2.1.1: direction of a body-link (soul-to-body vs body-to-soul) requires reading the verse's clause structure, not just spotting a body-part word. Still grounded in the same base extract, no structured field. |
| `T2.9.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Origin is often stated plainly in the verse text (e.g. "the LORD gave") -- readable directly. Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T2.9.2` | **No** | — | Cross-verse synthesis (single vs multiple origin, context-dependence) over many T2.9.1 readings -- not stored. |
| `T2.10.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Movement/sequence description is often present in the verse's own text (this is exactly the content Layer B's `operation.process` was capturing as free prose for Daniel -- Finding 6/Part 2). The same evidentiary base is available for every verse via Layer A, not just Daniel. |

### T3

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T3.1.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the perceptive faculty (inner senses, spiritual discernment) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to see/hear/perceive" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.1.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.1.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.1.3` | **No** | — | Cross-verse pattern over every T3.1.1/T3.1.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.2.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the cognitive faculty (knowing, understanding, discerning) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to understand/discern" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.2.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.2.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.2.3` | **No** | — | Cross-verse pattern over every T3.2.1/T3.2.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.3.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the memory faculty is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to remember/call to mind" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.3.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.3.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.3.3` | **No** | — | Cross-verse pattern over every T3.3.1/T3.3.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.4.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the affective faculty (feeling, emotion) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to feel/grieve/rejoice" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.4.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.4.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.4.3` | **No** | — | Cross-verse pattern over every T3.4.1/T3.4.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.5.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the creative faculty (imagination, capacity to originate) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to devise/fashion/imagine" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.5.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.5.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.5.3` | **No** | — | Cross-verse pattern over every T3.5.1/T3.5.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.6.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the volitional faculty (capacity to choose) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to choose/resolve/will" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.6.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.6.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.6.3` | **No** | — | Cross-verse pattern over every T3.6.1/T3.6.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.7.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the agency faculty (capacity to act, initiate) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to do/act/perform" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.7.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.7.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.7.3` | **No** | — | Cross-verse pattern over every T3.7.1/T3.7.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.8.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the moral-evaluation faculty is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to judge/discern right from wrong" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.8.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.8.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.8.3` | **No** | — | Cross-verse pattern over every T3.8.1/T3.8.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.9.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the conscience is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to be ashamed/convicted" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.9.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.9.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.9.3` | **No** | — | Cross-verse pattern over every T3.9.1/T3.9.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.10.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the conscientiousness (integrated moral awareness/volition/action) is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to take heed/watch carefully" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.10.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.10.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.10.3` | **No** | — | Cross-verse pattern over every T3.10.1/T3.10.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |
| `T3.11.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the relational capacity is engaged is often visible directly in the verse's own vocabulary and its neighbouring word glosses (e.g. a "to know/cleave to/be joined to" gloss beside the characteristic-word). No faculty enum exists anywhere (Finding 4) -- this is a reading judgment grounded in real, complete raw data, not a field lookup, and silence (no matching vocabulary) is itself ambiguous under this method. |
| `T3.11.2` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Same reading basis as T3.11.1, one step further (how it affects the faculty, not just whether). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T3.11.3` | **No** | — | Cross-verse pattern over every T3.11.1/T3.11.2 reading for this characteristic, synthesised into what it shows about the characteristic's nature -- not stored or computed anywhere; the faculty engagement judgment itself has no enum to aggregate against (Finding 4). |

### T4

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T4.1.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the characteristic operates from God toward the human person is often readable directly from the verse's own text (who does what to whom). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T4.1.2` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.1.3` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.2.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the characteristic operates in the person's movement toward God is often readable directly from the verse's own text (who does what to whom). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T4.2.2` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.2.3` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.3.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the characteristic operates extended by one person toward another is often readable directly from the verse's own text (who does what to whom). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T4.3.2` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.3.3` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.4.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the characteristic operates taken up by a person from another is often readable directly from the verse's own text (who does what to whom). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T4.4.2` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.4.3` | **No** | — | Explicitly cross-verse/pattern-framed ("as the evidence shows", "what the evidence shows a person must have...") -- not a single-verse reading, and no structured field aggregates it. |
| `T4.5.1` | **No** | — | Framed as a cross-verse comparison from the outset ("does the evidence show... operating differently within bonds vs across distance") -- not tied to one verse. |
| `T4.5.2` | **No** | — | Explicitly cross-verse ("as the evidence shows") -- covenantal-scope classification is not tracked. |
| `T4.5.3` | **No** | — | Explicitly cross-verse ("as the evidence shows") -- covenantal-scope classification is not tracked. |
| `T4.6.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Whether the verse mentions angelic/adversarial activity is often readable directly from the verse text (e.g. Dan 8's "holy ones", Gabriel). Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T4.6.2` | **No** | — | Explicitly cross-verse ("as the evidence shows", "in the evidence") -- adversarial-site/angelic-mediation classification is not tracked. |
| `T4.6.3` | **No** | — | Explicitly cross-verse ("as the evidence shows", "in the evidence") -- adversarial-site/angelic-mediation classification is not tracked. |

### T5

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T5.1.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T5.1.2` | **No** | — | "in the evidence" -- cross-verse, reversibility judged across the whole occurrence set, not one verse. |
| `T5.2.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | A before/during/after sequence described within one verse is readable directly from its text. Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T5.3.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T5.3.2` | **No** | — | "in the evidence" -- cross-context comparison, not one verse. |
| `T5.4.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T5.4.2` | **No** | — | "what does the evidence show" -- cross-verse, not one verse. |
| `T5.5.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Single-verse, empirically framed ("in this verse..."). The full evidentiary base is present and complete for EVERY verse in the DB (not Daniel-limited) -- a reader determines the answer from the verse's own text and its word-by-word gloss chain. The catalogue's specific classification label is still a judgment call on top of that reading, so this is Partial, not Yes. |
| `T5.6.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders | Weaker than the others: "eschatological fullness" is itself a theological category (like T0.4.1's typology), but a verse's own forward-looking language (hope, promise, "will be") is often directly readable as the grounding textual signal. |

### T6

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T6.1.1` | **Yes** | `verse_lexical.strong` joined through `cluster_strong.strong -> cluster_strong.cluster_code`, grouped by `verse_lexical.verse_id` | Genuinely computable: for every verse containing a Strong's code assigned to characteristic-cluster A, find every OTHER cluster_code whose Strong's codes also land in that verse, and count. This is a real structural join IBA supports end to end. |
| `T6.1.2` | **No** | — | Interpreting what a co-occurrence pattern shows about the characteristic's place in the landscape is synthesis over the T6.1.1 output, not itself stored. |
| `T6.2.1` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). Not single-verse framed -- these compare across a characteristic's whole evidence set. |
| `T6.2.2` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). Not single-verse framed -- these compare across a characteristic's whole evidence set. |
| `T6.3.1` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). Not single-verse framed -- these compare across a characteristic's whole evidence set. |
| `T6.3.2` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). Not single-verse framed -- these compare across a characteristic's whole evidence set. |
| `T6.3.3` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). Not single-verse framed -- these compare across a characteristic's whole evidence set. |
| `T6.4.1` | **Partial** | `cluster_strong` (a Strong's assigned to >1 `cluster_code` -- 77 live cases) and `strong_related` (STEP's root/cognate list per Strong's) | Both give a real, computable proxy for vocabulary overlap between characteristics, but neither is actually a "shared vocabulary" judgment -- `cluster_strong` overlap may just as easily be an unresolved allocation call, and `strong_related` mixes cognates, derivatives, and unrelated STEP cross-refs with no relation-type flag (Finding 5). |
| `T6.4.2` | **Partial** | `strong_meaning_parsed.lemma_key` / `strong_related` root forms | Root-level grouping is visible in the data (e.g. `H3820A` leb related to `H3824` levav, `H3826` libbah) but is not itself flagged as "shared root generating terms across two-or-more characteristics" -- that comparison has to be built. |
| `T6.4.3` | **No** | — | Interpretation of what sharing shows conceptually -- synthesis, not stored. |
| `T6.5.1` | **No** | — | Nearest-neighbour distinction between characteristics is not tracked anywhere; would require comparing two characteristics' full evidence sets by hand. |
| `T6.5.2` | **No** | — | Nearest-neighbour distinction between characteristics is not tracked anywhere; would require comparing two characteristics' full evidence sets by hand. |
| `T6.5.3` | **No** | — | Nearest-neighbour distinction between characteristics is not tracked anywhere; would require comparing two characteristics' full evidence sets by hand. |

### T7

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T7.1.1` | **Yes** | `word_strong.strong -> strong.accentedUnicode/stepGloss/stepTransliteration`, `strong_meaning_parsed`, `strong_meaning_tree` | Direct: the primary Hebrew/Greek terms and their root-meaning sense trees are exactly what this table chain holds. |
| `T7.1.2` | **Yes** | `verse_lexical.strong` + `verse_lexical.morph_code`, aggregated across every occurrence (via `strong_verse`) | The attested grammatical range (noun/verb/adjective/participle forms actually used) is directly computable by aggregating the morph parse over every occurrence of the term. |
| `T7.1.3` | **Yes** | `strong_meaning_parsed` (sense_code/gloss rows) and `strong_meaning_tree`, per `lemma_key` | The sense tree literally enumerates the term's semantic range; that IS the raw answer, though "breadth" as a summary judgment is a thin layer on top. |
| `T7.1.4` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). (A full read of every gloss in `strong_meaning_parsed` for the word's whole root family COULD surface these by hand, same reading-based logic as T1-T5 above -- but unlike those, this is a search across the WHOLE vocabulary/root family, not one verse, so it is left No rather than Partial.) |
| `T7.1.5` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). (A full read of every gloss in `strong_meaning_parsed` for the word's whole root family COULD surface these by hand, same reading-based logic as T1-T5 above -- but unlike those, this is a search across the WHOLE vocabulary/root family, not one verse, so it is left No rather than Partial.) |
| `T7.1.6` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). (A full read of every gloss in `strong_meaning_parsed` for the word's whole root family COULD surface these by hand, same reading-based logic as T1-T5 above -- but unlike those, this is a search across the WHOLE vocabulary/root family, not one verse, so it is left No rather than Partial.) |
| `T7.1.7` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). (A full read of every gloss in `strong_meaning_parsed` for the word's whole root family COULD surface these by hand, same reading-based logic as T1-T5 above -- but unlike those, this is a search across the WHOLE vocabulary/root family, not one verse, so it is left No rather than Partial.) |
| `T7.1.8` | **Partial** | `word_strong.strong` filtered by `strong.language` (Hebrew vs Greek) | Gives the raw OT/NT vocabulary sets to compare side by side. Judging what the relationship "shows about continuity or development" is interpretation. |
| `T7.1.9` | **No** | — | Detecting NT-period coinage needs a wider Koine corpus comparison outside this DB; `strong.created_at` records only when IBA first fetched the code, not when the word entered the language. |
| `T7.1.10` | **No** | — | Full-arc synthesis over T7.1.1-9, not itself stored. |
| `T7.2.1` | **Partial** | `verse.text` (full verse) + `verse_lexical.resolved_sense` per word/code (via `span`), the same base-extract chain `report.verse_span_meaning` renders + `span.position` for word order | The word's role in the sentence is readable directly from the verse's own text (subject/verb/object, clause position) even without a formal dependency parse -- the same base-extract reading, not a structured field. |
| `T7.2.2` | **No** | — | No literary-form/genre field exists on any book or verse table (checked `cfg_book_order` -- canonical order only, no genre column). Unlike faculty engagement, genre is a whole-book/section literary judgment, not recoverable from one verse's own words -- `verse.osisId` (book) is a real but external proxy a knowledgeable reader would use, not itself the raw material. |
| `T7.2.3` | **No** | — | Logical argument structure and contextual setting (judicial/liturgical/covenantal/etc.) span the passage's argument, not one verse's word list, and are not tracked fields. |
| `T7.2.4` | **No** | — | Logical argument structure and contextual setting (judicial/liturgical/covenantal/etc.) span the passage's argument, not one verse's word list, and are not tracked fields. |
| `T7.2.5` | **No** | — | Primary-anchor-verse selection is an editorial judgment across the WHOLE evidence set; nothing marks a verse as such. `passage.story_summary` is passage-level narrative prose (Daniel-only, debate layer) and not a per-characteristic anchor designation. |
| `T7.2.6` | **No** | — | Primary-anchor-verse selection is an editorial judgment across the WHOLE evidence set; nothing marks a verse as such. `passage.story_summary` is passage-level narrative prose (Daniel-only, debate layer) and not a per-characteristic anchor designation. |
| `T7.3.1` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |
| `T7.3.2` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |
| `T7.3.3` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |
| `T7.3.4` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |


---

## Summary

The **base lexical layer** (`word_registry`→`word_strong`→`strong`/`strong_meaning_parsed`/
`strong_related`→`verse_lexical`/`span`→`strong_verse`, plus `cluster`/`cluster_strong`) is the
real workhorse. It directly or partially answers:

- **T1.1–T1.6 (definition/kind/modes/response/effect)** and **T2.1/T2.7/T2.9/T2.10** (constitutional
  location/movement) — mostly Partial, via a grounded single-verse reading of `verse.text` +
  `verse_lexical.resolved_sense`.
- **All of T3** (perception through relational capacity) — every `.1`/`.2` sub-question Partial on
  the same reading basis; only the `.3` cross-verse-pattern sub-questions stay No.
- **T4's and T5's first-order, single-verse sub-questions** — Partial; their second/third-order
  "as the evidence shows" sub-questions stay No.
- **T6.1** (co-occurrence, a genuine structural join) and **T6.4** (vocabulary/root overlap, a
  proxy).
- **T7.1** (lexical/semantic analysis) and **T7.2.1** (verse function) — the lexical layer's
  strongest ground.

What remains **No** (71 of 126) is now concentrated in a smaller, more coherent set: pure
cross-verse/cross-characteristic synthesis with no structural aggregation mechanism (most `.2`/`.3`
sub-questions across every tier), external classification frameworks a single verse's words can't
supply on their own (T0's divine-image/typology theology, T5.6's eschatology, T7.2.2's literary
genre, T7.3's human-science lenses), and vocabulary-family questions that need a relation-type
distinction `strong_related` doesn't carry (T1.3, T7.1.4-7).
