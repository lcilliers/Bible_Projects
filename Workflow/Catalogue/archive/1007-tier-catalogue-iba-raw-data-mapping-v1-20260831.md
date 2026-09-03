# Tier catalogue → IBA raw-data mapping

> Escalation #1007. Purpose: for each live Tn.n.n tier question in `wa_obs_question_catalogue`
> (bible_research.db), determine whether it is directly answerable from IBA's own raw data tables
> (iba.db) — and if so, from which table/field — or whether it is not.

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
`kind='object_situation', detail="the king's food and the wine"`. This is rich, real content — and
it is the *only* structural place in IBA that captures "what a stated inner-being characteristic
does" at all.

### The seam that matters for every verdict below

**Layer B has no foreign key to a Strong's code, a `cluster_code`, or a `word_registry` row.**
`phenomenon`/`operation` are keyed to `(hib_id, verse_id, passage_id)` — a *narrative person*, not
a *lexical characteristic*. The only place a Strong's code appears in Layer B is buried inside
free-text `textual_warrant`/`observation_text` (as in the Dan 1:8 example), which is not a queryable
join. So even where Layer B has real content that conceptually answers a tier question (e.g. "what
immediate response follows"), there is no mechanical way to pull "every phenomenon that is an
instance of characteristic X" — a person would have to read every phenomenon and correlate it by
hand.

The tier catalogue's own framing — "the characteristic," "across the characteristic's verses" —
matches Layer A's unit (`word_registry` → `word_strong` → `strong_verse`/`verse_lexical`, or
`cluster_strong` at the M-code level), **not** Layer B's unit (a HIB across a passage). This
mismatch, not any single missing column, is why most tier questions come back "No" below.

### Other concrete findings behind the verdicts

1. **No FK from Layer B to a characteristic/Strong's/cluster** (established above) — the single
   biggest limiter.
2. — (folded into 1)
3. **Layer B's live population is Daniel only.** `phenomenon`: 177 total rows, but 56 are
   soft-deleted (`deleted=1`) and every one of the 121 live rows belongs to a `Dan` passage. `hib`:
   63 rows, also concentrated in Daniel. The "book-by-book debate" work referenced in other
   programme memory (Jonah/Joel/Obadiah/Micah/Hosea) was done under the closed, pre-IBA method in
   `bible_research.db`, not written into this schema.
4. **No constitutional-level, faculty, "kind of phenomenon," transformation/mechanism, or
   relational-interface enum exists anywhere in IBA.** Checked `cfg_enum` in full (37 distinct
   enum names) — none map to T2's spirit/soul/heart/mind/body-part categories, T3's eleven
   faculties, T1.2's act/disposition/condition/quality, or T5's transformation vocabulary. These
   tiers have literally no schema surface to answer from, populated or not.
5. **`strong_related` (87,535 rows) carries no relation-type column.** Sampled `H3820A` (leb):
   its 10 related rows mix true cognates (`H3824` levav, `H3826` libbah — "heart"), a homonym root
   (`H3823B` "to bake"), and an apparently unrelated cross-reference (`H6965B` "to arise") with no
   flag distinguishing them. Antonym/opposite, person-type, and aspect-marking vocabulary
   questions (T1.3, T7.1.4-7) all fail on this same gap.
6. **`operation.process` is not actually a controlled vocabulary in the live data.** Of 177
   `operation` rows, 61 are NULL; the documented small vocabulary (come from/go to/impact
   on/emerge/go away/become evident) appears only ~19 times combined; the remaining ~90-plus rows
   hold full prose sentences (e.g. *"A movement: wrath fully discharged as violent action against
   the other kingdom specifically."*) written straight into the `process` field instead of
   `description_text`. Not reliably groupable/filterable even setting aside Findings 1 and 3.
7. **`operation_party.kind` has no "divine" value.** Sampled every `non_human` row for Dan 8: God,
   angelic beings ("the Prince of the host… the researcher identifies this figure with Gabriel"),
   and the vision-source itself are all tagged `non_human` alike, distinguished only by free-text
   `detail`. T4's God-vs-angelic-vs-adversarial distinctions can't be recovered from `kind` alone.
8. **`span_candidate.candidate_tag`** (83,914 rows, English-phrase labels including many literal
   "heart"/"soul"/body-part tags) looks superficially relevant to T2, but its writer
   (`candidate.set`) was retired 2026-07-23 — this is frozen legacy output from an older process,
   not a live, currently-maintained classification, and per programme convention an inactive
   writer's output is not treated as a live input. Not counted as an answering source anywhere
   below.
9. **T6.1 (co-occurrence) is the one clean exception to the seam in Finding 1** — because it asks
   about two *characteristics* (clusters) co-occurring in a verse, not a HIB's phenomenon, it can
   be built entirely from Layer A: `verse_lexical.strong` joined through `cluster_strong` on
   `verse_lexical.verse_id`, no Layer B involvement needed at all.

---

## Part 3 — The mapping, tier by tier

**Answerable? key** — **Yes**: a real field/join in IBA raw data directly supplies the answer.
**Partial**: raw data supplies part of the answer or a genuine structured proxy, with a real
remaining interpretive gap. **No**: nothing in IBA raw data answers this; it requires judgment,
external knowledge, or a layer that (whatever it conceptually captures) has no structural path to
"this characteristic."

**Totals: 5 Yes · 7 Partial · 114 No** (of 126).

### T0

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T0.1.1` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.1.2` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.2.1` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.2.2` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.2.3` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.3.1` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.3.2` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.3.3` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |
| `T0.4.1` | **No** | — | No field anywhere in IBA records a verse's God-relation, classifies a role as created-design/fallen, or tracks typological/eschatological use (Finding 4). Not representable even in principle without a characteristic-to-phenomenon join (Finding 1). |

### T1

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T1.1.1` | **Partial** | `word_registry.word` | Gives the English name as registered. The second half of the question ("what the name signals about essential nature") is interpretation, not a stored value. |
| `T1.1.2` | **Yes** | `word_strong.strong` -> `strong.stepGloss/accentedUnicode/stepTransliteration`, `strong_sense.head`, `strong_meaning_parsed`, `strong_meaning_tree`, `strong_lsj_parsed`, `strong_mounce_parsed` | Full definitional lexicon chain for every Hebrew/Greek code onboarded for the word. `word_strong` does not flag which code is "primary" (that OWNER/XREF distinction lives only in bible_research.db) -- a human/process choice is still needed to pick the primary term(s). |
| `T1.1.3` | **No** | — | Directional/relational/constitutional implication of the name is interpretive synthesis over the definitional data, not a stored field. |
| `T1.2.1` | **Partial** | `span.morph_code` / `verse_lexical.morph_code` (part of speech) | Grammatical category (verb/noun/adjective/participle) is a real, structured signal that constrains but does not equal the catalogue's own act/disposition/condition/quality classification -- that mapping is still a judgment call. |
| `T1.2.2` | **No** | — | Simple-vs-compound is about the conceptual structure of the characteristic, not the morphology of any one span; not tracked. |
| `T1.3.1` | **No** | — | `strong_related` lists STEP's "related terms" but carries no relation-type column (Finding 5) -- antonym, derivative, and root-cognate are all indistinguishable, so a structural opposite cannot be isolated. |
| `T1.3.2` | **No** | — | `strong_related` lists STEP's "related terms" but carries no relation-type column (Finding 5) -- antonym, derivative, and root-cognate are all indistinguishable, so a structural opposite cannot be isolated. |
| `T1.3.3` | **No** | — | `strong_related` lists STEP's "related terms" but carries no relation-type column (Finding 5) -- antonym, derivative, and root-cognate are all indistinguishable, so a structural opposite cannot be isolated. |
| `T1.4.1` | **Partial** | `span.morph_code` / `verse_lexical.morph_code` | The grammatical/stem-form half is directly sourced (e.g. Dan 1:8's `H7760A` "sim" parses `HVqw3ms` -- Qal wayyiqtol). "Manner of functioning" beyond the parse is not stored. |
| `T1.4.2` | **Partial** | `verse_lexical.morph_code` compared across `strong_verse` occurrences; `verse.osisId` (book) for context | Whether the attested grammatical forms vary is computable by aggregation. "Constitutional level" is not tracked at all (Finding 4), so that half of the comparison is unavailable. |
| `T1.4.3` | **No** | — | No semantic verb-class tagging (e.g. speech-act) exists in the lexical layer; would require reading the gloss text and judging. |
| `T1.5.1` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |
| `T1.5.2` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |
| `T1.6.1` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |
| `T1.6.3` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |
| `T1.7.1` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |
| `T1.7.2` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |
| `T1.7.3` | **No** | — | Conceptually this is exactly what `phenomenon`/`operation` are built to record (a stated inner-being state and what follows from it). Structurally unusable for a characteristic-level question: no FK from `phenomenon`/`operation` to a Strong's code or cluster (Finding 1), and the data that exists is Daniel-only, 121 live rows (Finding 3). |

### T2

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T2.1.1` | **No** | — | No constitutional-level (spirit/soul/heart/mind/body-part) field or enum exists anywhere in IBA -- checked `cfg_enum` in full, no such category (Finding 4). The content sometimes appears as free prose inside `phenomenon.textual_warrant`/`operation.observation_text` (e.g. Dan 1:8's "leb/heart" reading) but only where debate data exists (Daniel only) and never as a queryable field. |
| `T2.1.2` | **No** | — | No constitutional-level (spirit/soul/heart/mind/body-part) field or enum exists anywhere in IBA -- checked `cfg_enum` in full, no such category (Finding 4). The content sometimes appears as free prose inside `phenomenon.textual_warrant`/`operation.observation_text` (e.g. Dan 1:8's "leb/heart" reading) but only where debate data exists (Daniel only) and never as a queryable field. |
| `T2.7.1` | **No** | — | Body-link direction is not a tracked field; same limitation as T2.1. |
| `T2.9.1` | **No** | — | `operation_party.role/kind` (source/target; self/human/non_human/object_situation/none) is conceptually adjacent but (a) has no join to a characteristic/Strong's (Finding 1), (b) does not distinguish God from an angelic/adversarial being -- both fall under `non_human` (Finding 7), and (c) is Daniel-only (Finding 3). |
| `T2.9.2` | **No** | — | `operation_party.role/kind` (source/target; self/human/non_human/object_situation/none) is conceptually adjacent but (a) has no join to a characteristic/Strong's (Finding 1), (b) does not distinguish God from an angelic/adversarial being -- both fall under `non_human` (Finding 7), and (c) is Daniel-only (Finding 3). |
| `T2.10.1` | **No** | — | `operation.process` was designed as a small controlled vocabulary (come from/go to/impact on/emerge/go away/become evident) but in the live data 61 of 96 rows are NULL and most of the rest are full prose sentences, not the controlled values (Finding 6) -- not reliably queryable even within its Daniel-only scope. |

### T3

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T3.1.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.1.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.1.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.2.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.2.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.2.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.3.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.3.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.3.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.4.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.4.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.4.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.5.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.5.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.5.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.6.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.6.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.6.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.7.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.7.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.7.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.8.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.8.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.8.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.9.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.9.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.9.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.10.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.10.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.10.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.11.1` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.11.2` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |
| `T3.11.3` | **No** | — | No perceptual/cognitive/memory/affective/creative/volitional/agentive/moral-evaluative/conscience/conscientiousness/relational-capacity faculty field or enum exists anywhere in IBA (Finding 4) -- this entire tier has no structural representation, populated or not. |

### T4

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T4.1.1` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.1.2` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.1.3` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.2.1` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.2.2` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.2.3` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.3.1` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.3.2` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.3.3` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.4.1` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.4.2` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.4.3` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.5.1` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.5.2` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.5.3` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.6.1` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.6.2` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |
| `T4.6.3` | **No** | — | No relational-interface classification (God-to-human / human-to-God / human giving / human receiving / relational boundaries / spiritual-beings) exists. `operation_party.kind` (self/human/non_human/object_situation/none) is the nearest structural signal but does not encode direction, does not separate God from other non-human beings (Finding 7), and has no characteristic join (Finding 1). |

### T5

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T5.1.1` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.1.2` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.2.1` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.3.1` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.3.2` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.4.1` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.4.2` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.5.1` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |
| `T5.6.1` | **No** | — | No transformation / mechanism-of-change / suffering-relation / formation-arc / eschatological-trajectory field or enum exists anywhere in IBA (Finding 4). |

### T6

| Code | Answerable? | IBA raw-data source | Note |
|---|---|---|---|
| `T6.1.1` | **Yes** | `verse_lexical.strong` joined through `cluster_strong.strong -> cluster_strong.cluster_code`, grouped by `verse_lexical.verse_id` | Genuinely computable: for every verse containing a Strong's code assigned to characteristic-cluster A, find every OTHER cluster_code whose Strong's codes also land in that verse, and count. This is a real structural join IBA supports end to end. |
| `T6.1.2` | **No** | — | Interpreting what a co-occurrence pattern shows about the characteristic's place in the landscape is synthesis over the T6.1.1 output, not itself stored. |
| `T6.2.1` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). |
| `T6.2.2` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). |
| `T6.3.1` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). |
| `T6.3.2` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). |
| `T6.3.3` | **No** | — | No cross-characteristic sequential or causal relationship is tracked. `passage_linkage` (operation-to-operation link within one passage) is the nearest structural table but holds 3 live rows programme-wide and is not characteristic-keyed (Finding 1). |
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
| `T7.1.4` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). |
| `T7.1.5` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). |
| `T7.1.6` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). |
| `T7.1.7` | **No** | — | None of these vocabulary-role distinctions (aspect-marking, structural-opposite, person-type/agent-noun, supplication/seeking term) are tagged on `strong_related` or anywhere else -- same undifferentiated-list limitation as T1.3 (Finding 5). |
| `T7.1.8` | **Partial** | `word_strong.strong` filtered by `strong.language` (Hebrew vs Greek) | Gives the raw OT/NT vocabulary sets to compare side by side. Judging what the relationship "shows about continuity or development" is interpretation. |
| `T7.1.9` | **No** | — | Detecting NT-period coinage needs a wider Koine corpus comparison outside this DB; `strong.created_at` records only when IBA first fetched the code, not when the word entered the language. |
| `T7.1.10` | **No** | — | Full-arc synthesis over T7.1.1-9, not itself stored. |
| `T7.2.1` | **No** | — | Syntactic/argumentative function within the verse is not captured -- IBA has no dependency-parse or argument-structure layer, only linear span position and morph tag. |
| `T7.2.2` | **No** | — | No literary-form/genre field exists on any book or verse table (checked `cfg_book_order` -- canonical order only, no genre column). Book identity (`verse.osisId`) is available as an external proxy a researcher could reason from, but genre itself is not stored. |
| `T7.2.3` | **No** | — | Logical argument structure and contextual setting (judicial/liturgical/covenantal/etc.) are not tracked fields. |
| `T7.2.4` | **No** | — | Logical argument structure and contextual setting (judicial/liturgical/covenantal/etc.) are not tracked fields. |
| `T7.2.5` | **No** | — | Primary-anchor-verse selection is an editorial judgment; nothing marks a verse as such. `passage.story_summary` is passage-level narrative prose (Daniel-only, debate layer) and not a per-characteristic anchor designation. |
| `T7.2.6` | **No** | — | Primary-anchor-verse selection is an editorial judgment; nothing marks a verse as such. `passage.story_summary` is passage-level narrative prose (Daniel-only, debate layer) and not a per-characteristic anchor designation. |
| `T7.3.1` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |
| `T7.3.2` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |
| `T7.3.3` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |
| `T7.3.4` | **No** | — | Human-science framework selection and its fit against the evidence is external interpretive work with no counterpart in the IBA schema at all. |


---

## Summary

The base lexical layer (`word_registry`→`word_strong`→`strong`/`strong_meaning_parsed`/
`strong_related`→`verse_lexical`/`span`→`strong_verse`, plus `cluster`/`cluster_strong`) directly
or partially answers essentially all of **T1.1-T1.2 and T1.4 (lexical/grammatical half)**, **T6.1**
(co-occurrence, via cluster overlap), **T6.4** (vocabulary/root overlap, as a proxy), and most of
**T7.1** (lexical/semantic analysis). That is the full extent of direct IBA raw-data support: 5
Yes + 7 Partial = 12 of 126 questions (~10%).

The other roughly 90% — all of T0, T3, T4, T5, most of T2 and T6, and the non-lexical two-thirds
of T7 — ask about things (God-relation, faculty engagement, relational interface, transformation
mechanism, cross-characteristic sequencing, literary form, human-science framing) that have no
structural representation in IBA at all, or that the one layer built to capture inner-being
phenomenology (`hib`/`phenomenon`/`operation`) cannot answer *for a characteristic* because it has
no join key to one and is populated for Daniel only.
