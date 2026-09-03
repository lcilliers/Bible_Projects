# Verse-lexical Window 1 — measured against the observation-question catalogue

**Filename:** 1383-verse-lexical-window1-catalogue-question-coverage-v1-20260903.md
**Escalation:** #1383
**The question this answers, verbatim (researcher):** the verses were never written to describe
the inner being directly — what it is and how it works is *inferred* from what the verses say and
don't say. Measure the enriched (proposed) lexical against the catalogue questions: can we, and
what would be necessary to, answer every question with the lexical data at hand.
**Catalogue used**: `wa_obs_question_catalogue` (`database/bible_research.db`), 239 active rows.
Not the newer VE-lexical catalogue or the retired tier docs — this is the one #1007 (closed this
week, same lineage as #1378) actively worked against and concluded was "structurally deficient" in
its question/window/answer/next-phase-role shape; that conclusion is the right starting point here,
not a fresh catalogue pick. Filtered to the two scopes that are actually candidates for Window-1-
sourced answers: **`Word/term (lexical)`** (16 questions) and **`The verse`** (6 questions) — every
one of the 22 covered below, none selected out.

**Every question got the same treatment, per this session's own drift-mitigation discipline** — no
question skipped because it looked like an obvious yes or an obvious no.

---

## 1. Grain mismatch, named up front — this is the main finding

Most of these questions are not verse-level at all. They ask about a **characteristic's entire
vocabulary arc** — every term that expresses it, across every verse those terms occur in, across
both Testaments. Window 1, correctly scoped ("a verse's own words from its own span/morph/lexicon
data... never resolved by reaching into another verse"), cannot and should not try to answer a
cross-verse, cross-testament question from inside a single verse's own read. **The real test isn't
"does Window 1 answer this" — it's "does Window 1, run across every verse a term occurs in, produce
raw material an aggregation step could correctly answer this from."** That's the standard applied
below, question by question.

## 2. `The verse` scope (6 questions) — genuinely single-verse grain, the direct test

| Code | Question | Verdict | Basis |
|---|---|---|---|
| T7.2.1 | Function of the primary term within its primary verse — role in the sentence *and the argument* | **PARTIAL.** "Role in the sentence": yes — role(content/function), noun-classification (relational/severity), verb (triggered-by/impacts) answer this directly. "Role in the argument": only as far as the connective test's local edges (causal/coordinating/purpose) go — no mechanism assembles those edges into an actual argument structure (see T7.2.3). |
| T7.2.2 | Literary form (narrative, psalm, wisdom, prophecy, epistle, apocalyptic) | **YES.** Directly `passage.genre`, Window 1's own process gate, first move of the read. |
| T7.2.3 | Logical structure — premises and conclusions | **NOT CAPTURED, no current owner.** The connective test tags local clause-linkage type at the code level; nothing assembles those into a verse's actual argument (which clause is the premise, which the conclusion). This is a real gap this catalogue check surfaces that neither #1383's design nor the drift-mitigation plan named — it needs a home (Window 1 extension, Window 2, or a dedicated synthesis step), not silently left to fall through. |
| T7.2.4 | Contextual setting (judicial, liturgical, covenantal, communal, eschatological) | **NOT CAPTURED, no current owner.** Not lexical data — real-world/institutional classification. Legitimately outside Window 1's own defined scope, but nothing else in the live pipeline claims it either. |
| T7.2.5 | Does any verse function as the primary anchor for the characteristic | **OUT OF WINDOW-1 GRAIN.** Cross-verse comparison across a whole characteristic's evidence base — a synthesis-stage question by nature, not fixable at the single-verse layer. |
| T7.2.6 | What the primary anchor verse shows that no other verse shows | **OUT OF WINDOW-1 GRAIN.** Same as T7.2.5 — needs every candidate verse's own Window-1 read to already exist, then a comparison step on top. |

## 3. `Word/term (lexical)` scope (16 questions) — term/characteristic grain

| Code | Question | Verdict | Basis |
|---|---|---|---|
| T1.1.1 | What the characteristic is called in the programme, what the name signals | **DIFFERENT OWNER, not a gap.** A programme-definition/naming question, not a lexical-data question — the glossary work (#1377) is the natural home, already built for exactly this. |
| T1.1.2 | What the primary Hebrew/Greek terms show at the definitional level | **ANSWERABLE VIA AGGREGATION, not yet built.** Needs every occurrence's `resolved_sense` for the term's primary Strong's codes, rolled up — Window 1 supplies the per-occurrence senses (subject to §5's open question about whether `resolved_sense` is actually narrowing or falling back), nothing currently rolls them up per term. |
| T1.1.3 | Directional/relational/constitutional implication of the name | **DIFFERENT OWNER.** Same class as T1.1.1 — programme-naming, not lexical-data. |
| T6.4.1 | Vocabulary shared with other characteristics | **ANSWERABLE VIA AGGREGATION, not yet built — the strongest positive result in this check.** This is exactly what the related-words step supplies, mechanically, *if run exhaustively for every content code* (this session's own correction) *and* rolled up across every term/verse belonging to a characteristic. Real evidence from this session's own validation run: `H1870G`(Prov 3:6)/`H1870L`(Deut 6:7) sharing a root across two different passages, surfaced by the plain related-words pull, unprompted. The mechanism exists and works — only the aggregation layer (roll every characteristic's terms' related-word pulls into one place) is missing. |
| T6.4.2 | Root-level sharing across characteristics | Same as T6.4.1 — same mechanism, same missing aggregation layer. |
| T6.4.3 | What the sharing shows about the conceptual relationship | **JUDGEMENT-BEARING, on top of T6.4.1/2's raw material once aggregated.** Not mechanical — the same sorting discipline (same-concept vs. coincidental) the related-words step already applies verse-locally, just needed at the rolled-up scale too. |
| T7.1.1 | Primary Hebrew/Greek terms, what their root meanings show | Same class as T1.1.2 — answerable via aggregation, not yet built. |
| T7.1.2 | Grammatical range of the primary term (noun/verb/adjective/participle) | **ANSWERABLE VIA AGGREGATION, cheaply.** Directly derivable by aggregating `morph_code`'s part-of-speech prefix across every `verse_lexical` row for a given Strong's code — Window 1 already captures this per-occurrence; the rollup is a plain `GROUP BY`, not new capture. |
| T7.1.3 | Semantic range — breadth of meaning | **NOT a Window-1 aggregation question at all — it's a property of the base lexicon.** `strong_meaning_tree`/`strong_meaning_parsed` (40,315 rows, already live, already consumed by Window 2's own `full-lexical-weight-in-description` rule) carries this independent of any specific verse. Window 1 should be *drawing on* this resource correctly (§5's open question), not re-deriving it. |
| T7.1.4 | Disposition-vs-act, received-vs-given, condition-vs-quality distinctions in the vocabulary | **REAL GAP, no current owner.** Needs a term-family-level semantic classification nothing in the live pipeline currently produces — not Window 1's per-verse noun-classification (that's verse-local: is *this occurrence* relational or a quality-modifier), a different, term-wide question. |
| T7.1.5 | Structural opposite / absence term | **REAL GAP, no current owner.** `strong_related` doesn't distinguish synonym from antonym relations — checked live in this session's own related-word pulls, every relation returned reads as same-root/same-concept, never flagged as an opposite. |
| T7.1.6 | Person-type term (one who habitually exercises the characteristic) | **ANSWERABLE VIA AGGREGATION, if characteristic-membership is known.** Same mechanism as T7.1.2 (grammatical-range rollup) could surface candidate person-nouns within a characteristic's term family — but needs the term-to-characteristic linkage (`mti_terms.cluster_code`/`cluster_subgroup`), which is outside Window 1 entirely. |
| T7.1.7 | Supplication/seeking term | Same class as T7.1.6 — same mechanism, same missing linkage. |
| T7.1.8 | OT/NT vocabulary relationship — continuity or development | **ANSWERABLE VIA AGGREGATION, once built — #1383's own proposed schema already supplies the key.** The `testament` column §1383 §5.1 already proposes (denormalized, mechanical, OT/NT from `cfg_book_order.ordinal`) is exactly what a cross-testament rollup needs. Not yet built, but not a new requirement either — already in the design. |
| T7.1.9 | Newly-coined-in-NT term | **ANSWERABLE VIA AGGREGATION, same mechanism as T7.1.8** (a Greek term with zero Hebrew-side occurrences across the whole corpus) — same missing rollup layer, no new capture needed. |
| T7.1.10 | Full vocabulary arc | A roll-up of T7.1.1–T7.1.9 together — inherits every gap and every answerable-via-aggregation item above; not a separate question in practice. |

## 4. What this means, stated plainly

- **9 of 22** (T1.1.2, T6.4.1, T6.4.2, T7.1.1, T7.1.2, T7.1.6, T7.1.7, T7.1.8, T7.1.9) are answerable
  via an aggregation/rollup layer Window 1's *already-proposed* design (related-words, testament/
  language columns, morph capture) genuinely supports — that layer doesn't exist yet, but nothing
  new needs to be captured to build it. **Plus 2 related, not double-counted**: T6.4.3 needs the
  same judgement-sorting discipline the related-words step already applies verse-locally, just
  applied again once rolled up; T7.1.10 is a pure roll-up of the T7.1.x items above it, not a
  separate question in practice.
- **1** (T7.2.2, genre) is answered directly, today, by Window 1's own process gate.
- **1** (T7.2.1) is partially answered; the missing half (argument-role) is the same gap as T7.2.3.
- **3** (T1.1.1, T1.1.3, T7.1.3) have a different, already-existing owner — not gaps, just not
  Window 1's job.
- **4 real gaps with no current owner anywhere in the live pipeline**, not just "not yet built" but
  genuinely unclaimed: T7.2.3 (argument structure), T7.2.4 (contextual setting), T7.1.4
  (disposition/act-type distinctions), T7.1.5 (structural opposites). These don't block Window 1's
  own build — they're outside its scope by design — but they need a decision about where they get
  answered, or an explicit decision that they don't get answered at all, rather than silently
  falling through every stage's own "not my scope" boundary.
- **2** (T7.2.5, T7.2.6) are correctly out of Window 1's grain entirely — genuine characteristic-
  level synthesis questions, not a gap in Window 1's design.

## 5. The remaining 159 active questions — added per your request, all of them, none skipped

**Count correction, checked live, not assumed**: `wa_obs_question_catalogue` has 181 active,
non-deleted rows total (a separate 58 rows are marked `status='active'` but `deleted=1` — an
inconsistency in the table itself, not counted here). 181 − 22 (§2/§3 above) = **159** remaining,
not 126 — noted plainly rather than silently matching a number that didn't reconcile.

**The single biggest new finding in this batch, stated up front**: 26 of these 159 questions
(`T2.1.1`/`T2.7.1`/`T2.9.1`/`T2.10.1` plus all 22 `T3.1.1`–`T3.11.2` faculty-engagement pairs) ask
about a **specific, named, controlled list** — either the constitutional level a characteristic
operates at (spirit / soul / heart / mind / other soul-subset / a named body part) or which of 11
named inner faculties (perception, cognition, memory, affect, creativity, volition, agency, moral
evaluation, conscience, relational capacity, conscientiousness) it engages, per verse. **Checked
live: no structured field for either exists anywhere in the live pipeline.** `hib`/`phenomenon`/
`operation`/`operation_party` were already fully inspected in the capture-design document (§3
there) and none of them carry anything like it. The one thing that superficially looks like an
answer, `bible_research.db.lemma_faculty_map`, is the wrong grain (per-**lemma**, not per-verse —
so it can't show a word engaging different faculties in different verses, which is exactly what
these questions ask) and its own `cfg_column.use` entry records it as uncontrolled free text (36
distinct values, no enum behind them, 815 of 1,717 rows empty) — not a working answer to point at,
a stale, disconnected attempt. **This is a real gap, same shape as the 4 already named in §4, now
with the largest single block of catalogue questions (26) sitting behind it.**

Grouped by scope below, every question given its own verdict — grouping only shares the reasoning
paragraph where it's genuinely the same reasoning, never the verdict itself.

### `Verse-context` (41) — the scope closest to Window 1's own grain, so the most differentiated

Single-verse, so the right comparison is Window 2 (`hib`/`phenomenon`/`operation`, already live),
not Window 1 directly — Window 1 supplies raw material (entity-linking, chain, connective,
relational/severity noun classification) that a per-verse HIB/phenomenon/operation judgement draws
on, same relationship established in the capture-design document.

| Code | Question | Verdict | Basis |
|---|---|---|---|
| T0.1.1 | Is the characteristic predicated of God / related to God, in what relation, this verse | **CORRECTED — ANSWERABLE VIA AGGREGATION, Window 1 alone, mechanical.** (Researcher correction: this is directly derivable from the lexical data — across every verse containing the characteristic's terms, is a divine name ever mentioned, and is the characteristic-word grammatically attributed to God or to the human/IB.) | Checked live: divine-name codes are a small, identifiable, evidence-buildable set (`H0430G`/`H0410G`/`H3068G` "God"/"LORD", `G2316`/`G2962G`/`G5547`/`G2424G` "God"/"lord:God"/"Christ"/"Jesus" — distinguishable from lowercase generic `H0113`/`H0426`/`H0433` "lord"/"god"), same shape as the connective/negator lexicons already prototyped this session. Window 1's own entity-linking test already resolves a term's grammatical subject/possessor; checking whether that resolved subject's code is in the divine-name lexicon is a mechanical lookup on top, not a new capability. My earlier verdict wrongly assumed this had to wait on Window 2's manual `operation_party.kind` — it doesn't; it's cheaper and earlier than that, and could even help bootstrap Window 2 rather than only follow it. |
| T0.2.1 | Does this verse state a purpose/role/effect | Window 2 today, free-text only | `operation.observation_text`/`description_text` capture it narratively; no structured field distinguishes "stated" from "inferred." |
| T0.4.1 | Typological use (christological/eschatological), and direction | **REAL GAP.** | No controlled vocabulary for "typological use" or its direction anywhere live — free-text only, genuinely uncaptured as a distinct fact. |
| T1.4.1 | Distinct modes in this verse — grammatical/stem form *and* manner of functioning | **PARTIAL, Window 1 directly for half.** | "Grammatical/stem form" = `morph_code`, already in Window 1's baseline, answerable today. "Manner of functioning" is Window 2/free-text. |
| T1.5.1 | First/most immediate inner-being response, this verse | Window 2 today | `operation.process` (state-or-movement) is built for exactly this. |
| T1.6.1 | What the characteristic produces over time, this verse | Window 2 today | Same as T1.5.1 — `operation.process`/`description_text`. |
| T2.1.1 | Constitutional level(s): spirit/soul/heart/mind/other/body-part, each engaged | **REAL GAP** — part of the 26-question faculty/level finding above. | No structured field; not even loosely covered by anything free-text either (unlike T0.2.1/T1.5.1, which at least have a prose home). |
| T2.9.1 | Where the verse says the characteristic originates (generated/received/bestowed/carried/introduced-by-spirit) | **REAL GAP.** | A controlled-list question, no field. |
| T3.1.1 / T3.1.2 | Perception faculty — engaged? how? effect? | **REAL GAP**, part of the 26. | No field; `lemma_faculty_map` wrong grain and uncontrolled. |
| T3.2.1 / T3.2.2 | Cognition — engaged? effect? | **REAL GAP**, same block. | — |
| T3.3.1 / T3.3.2 | Memory — engaged? effect? | **REAL GAP**, same block. | — |
| T3.4.1 / T3.4.2 | Affect — engaged? effect? | **REAL GAP**, same block. | — |
| T3.5.1 / T3.5.2 | Creativity — engaged? effect? | **REAL GAP**, same block. | — |
| T3.6.1 / T3.6.2 | Volition — engaged? effect (capacity, interaction, constraints)? | **REAL GAP**, same block. | — |
| T3.7.1 / T3.7.2 | Agency — engaged? effect? | **REAL GAP**, same block. | — |
| T3.8.1 / T3.8.2 | Moral evaluation — engaged? effect? | **REAL GAP**, same block. | — |
| T3.9.1 / T3.9.2 | Conscience — engaged? effect? | **REAL GAP**, same block. | — |
| T3.10.1 / T3.10.2 | Conscientiousness — engaged? effect? | **REAL GAP**, same block. | — |
| T3.11.1 / T3.11.2 | Relational capacity — engaged? effect? | **REAL GAP**, same block. | — |
| T4.1.1 | Operates from God toward the person, this verse | **CORRECTED — ANSWERABLE VIA AGGREGATION, Window 1 alone, mechanical**, same fix as T0.1.1, not left as a one-off. | Divine-name lexicon + entity-linking's own subject/object resolution already tell you whether the characteristic-word's grammatical *source* is a divine-name code and its *target* a human party — directly, without waiting on `operation_party.kind` to have been set by the manual Window-2 pass. `operation_party.kind` can still confirm it later; it isn't the only or the first way to answer this. |
| T4.2.1 | Operates in the person's movement toward God | Same correction. | Reversed direction (subject = human, target-code = divine-name). |
| T4.3.1 | Extended person-to-person | Same mechanism, needs a slightly larger lexicon. | Needs the mirror-image lexicon (a small "human-name/person-noun" class, not just divine names) — a bigger build than T4.1.1/T4.2.1, not assumed free. |
| T4.4.1 | Taken up by a person from another | Same as T4.3.1. | Same basis. |
| T4.6.1 | Operates in relation to angelic/adversarial beings | Same mechanism, NOT yet verified live. | Needs a third small lexicon (angelic/spirit-being codes) not yet built or checked here — flagged as the one of this group not yet proven the way the divine-name lexicon was. |
| T5.1.1 | Produces transformation — condition, orientation, or both | Window 2 today, free-text only | `operation.process`/`description_text`; no structured condition-vs-orientation flag. |
| T5.2.1 | Before/during/after sequence of inner states | **REAL GAP.** | No structured sequence field; free text can narrate it but nothing makes it queryable as a sequence. |
| T5.3.1 | Mechanism of change (discipline/encounter/gradual/sudden/other) | **REAL GAP.** | Controlled-list-shaped, no field — same class as T2/T3, smaller. |
| T5.4.1 | Relation to suffering/affliction | Window 2 today, free-text only | `observation_text`/`description_text`. |
| T5.5.1 | Participates in the sanctification arc | **OUT OF SINGLE-VERSE GRAIN.** | "Arc" is inherently cross-verse by the question's own wording — a synthesis question even at Window 2's own layer. |
| T5.6.1 | Eschatological-fullness orientation | Window 2 today, free-text only, same class as T0.4.1 | No controlled vocabulary, but at least a prose home exists. |

### `The HIB` (15) and `Characteristic (HIB behaviour)` (15) — cross-verse rollups of the above, correctly out of single-verse grain

Both scopes ask "**across the verses**" — explicitly the rolled-up, whole-characteristic form of
the `Verse-context` questions just covered. **Every one of these inherits its single-verse
counterpart's gap or coverage status, plus needs an aggregation layer that doesn't exist for any of
them** (the same missing layer named in the first 22-question check, extended here to Window 2's
output, not just Window 1's).

| Code | Question | Verdict |
|---|---|---|
| T1.7.3 | Inner-being state when characteristic present but doesn't take hold | Out of single-verse grain — needs cross-verse comparison of "took hold" vs "didn't," itself not a tracked distinction anywhere yet. |
| T2.1.2 | Pattern of engaged/absent constitutional levels across verses | Out of grain, and inherits T2.1.1's real gap underneath it — nothing to roll up yet. |
| T2.10.1 | Movement across constitutional levels, cross-verse sequence/pattern | Out of grain — and inherits the same real gap as T2.1.1/T2.9.1 above (no level field exists to move across). Verified live: this code exists once, under `The HIB` only — not a duplicate of a `Verse-context` row. |
| T2.7.1 | Body-link direction (soul→body, body→soul, both), cross-verse | Out of grain, same inherited gap. Verified live: `The HIB` only, not duplicated. |
| T3.1.3 – T3.11.3 (10 items, one per faculty) | Cross-verse engagement pattern per faculty | Out of grain, every one inherits the corresponding `Verse-context` faculty gap. |
| T1.2.1 | Kind of phenomenon — act/disposition/condition/quality | Out of grain — a definitional classification needing the whole verse-evidence set, not stated anywhere per-verse today. |
| T1.2.2 | Simple or compound structure | Out of grain, same class. |
| T1.3.1 – T1.3.3 | Structural opposite; what it excludes; where it ends | Out of grain — same shape as the already-named T7.1.5 gap (§3), at the characteristic level. |
| T1.4.2 | Mode variation by context/direction/level | Out of grain, rollup of T1.4.1. |
| T1.4.3 | Communicative/speech-based mode | Out of grain — no field distinguishes this at any layer yet. |
| T1.5.2 | Consistency of immediate response across verses | Out of grain, rollup of T1.5.1. |
| T1.6.3 | Sustained effect vs. immediate response | Out of grain, rollup of T1.5.1/T1.6.1. |
| T1.7.1 / T1.7.2 | Conditions under which it takes hold / is blocked | Out of grain — genuine synthesis, no per-verse field tracks "blocked" as distinct from "absent." |
| T2.9.2 | Origin — single/multiple, changes with context | Out of grain, rollup of T2.9.1. |
| T5.1.2 | Transformation reversible/irreversible | Out of grain — needs comparing multiple verses' outcomes, nothing tracks this. |
| T5.3.2 | Mechanism varies by context | Out of grain, rollup of T5.3.1. |
| T5.4.2 | What suffering does to the characteristic | Out of grain, rollup of T5.4.1. |

### `Characteristic relational` (17) and `Other non-human beings` (12) — whole-characteristic, cross-verse, mostly theological synthesis

| Code | Question | Verdict |
|---|---|---|
| T4.3.2 / T4.3.3 | Giver's inner conditions; what must be received before extending | Out of grain — synthesis across every "extension" instance of the characteristic. |
| T4.4.2 / T4.4.3 | Conditions for uptake; state of one who doesn't take it up | Out of grain, same class. |
| T4.5.1 – T4.5.3 | Operation within vs. across relational bonds/covenant; relational scope | Out of grain — cross-verse comparison, no tracked distinction. |
| T6.1.1 / T6.1.2 | Co-occurring characteristics; what the pattern shows | **ANSWERABLE VIA AGGREGATION**, same mechanism as T6.4.1/T6.4.2 (§3) — if which-verses-name-which-characteristics is tracked (it already is, via `cluster`/`mti_terms.cluster_code`), co-occurrence is a plain join, not new capture. |
| T6.2.1 / T6.2.2 | Sequencing between characteristics; causal/developmental/correlational | Out of grain — sequencing between *characteristics* (not codes within one verse) is a different, higher-level relation than anything Window 1 or the chain test tracks. |
| T6.3.1 – T6.3.3 | One characteristic producing/produced-by/constituent-of another | Out of grain — genuine theological-structural synthesis. |
| T6.5.1 – T6.5.3 | Nearest-neighbour distinction | Out of grain, same class as T6.3.x. |
| T0.1.2, T0.2.2, T0.2.3, T0.3.1 – T0.3.3 | Borne by God; created-design vs. fallen; future orientation; divine-image aspect | Out of grain — explicit theological synthesis across the whole evidence base, several stages beyond any lexical or per-verse capture. |
| T4.1.2 / T4.1.3 | Basis of God's extension; what it shows of his disposition | Out of grain, cross-verse synthesis on top of the (already answerable via Window-1 aggregation, per §above, corrected) per-verse T4.1.1 facts. |
| T4.2.2 / T4.2.3 | Inner posture required; what it shows of the relationship | Out of grain, same class. |
| T4.6.2 / T4.6.3 | Site of adversarial attack; mediated through angelic ministry | Out of grain — cross-verse pattern, built on the already-answerable T4.6.1 per-verse fact. |

### `Science` (4) — a different kind of research activity entirely

| Code | Question | Verdict |
|---|---|---|
| T7.3.1 – T7.3.4 | Which human-science framework applies; where it illuminates/diverges; what it surfaces the verses haven't | **OUT OF SCOPE FOR THIS WHOLE PIPELINE, not just Window 1.** These apply an external interpretive framework (psychology, sociology, etc.) *to* the verse-grounded findings — a distinct research step downstream of everything Window 1/Window 2 produce, not answerable from lexical or per-verse HIB data at all, by the questions' own design. |

### `leviticus` (12) — book-specific, mixed grain

| Code | Question | Verdict |
|---|---|---|
| LEV-CLN-01 | Why is cleanness necessary | Out of grain — whole-book theological synthesis. |
| LEV-CLN-02 | Where "unclean" comes from — source + root sense | **ANSWERABLE VIA AGGREGATION** — a term-etymology question, same class as T7.1.1 (§3): rolled-up `resolved_sense`/`strong_meaning_tree` data for the relevant Hebrew term. |
| LEV-CLN-03 – LEV-CLN-06 | Cover vs. scrub; IB-desire vs. external; awareness; past-only vs. forward-standing | Out of grain — each requires whole-book pattern synthesis, not lexical or per-verse fact. |
| LEV-GEN-01 | Seat/locus of inner being in Leviticus (nephesh vs. heart) | **ANSWERABLE VIA AGGREGATION** — a vocabulary-distribution question (which term, which verses), same mechanism as T7.1.2. |
| LEV-GEN-02 – LEV-GEN-06 | Atonement mechanism; divine interior; book synthesis; inner being's own act; redemption vocabulary | Out of grain — whole-book theological synthesis, several stages beyond Window 1/2. |

### `universal` (43) — almost entirely deep, whole-characteristic synthesis; a handful genuinely lexical

The `Compassion`/`Forgiveness`/`Goodness`/`Love`/`Mercy` "Extensions" questions read as sophisticated
theological-synthesis material (Session D/C territory) — checked individually, not assumed as a
block, because a few are genuinely lexical and shouldn't be lumped in with the rest.

| Code | Question | Verdict |
|---|---|---|
| C-001 – C-003, C-006, C-007 | Prohibition-frequency default status; winning an inner contest; permanence vs. a rival's momentariness; violation by its own bearer; institutionalised social form | Out of grain — each is a cross-verse pattern claim requiring the whole evidence base, several stages beyond Window 1. |
| F-001 – F-004, F-006 – F-010, F-012 – F-014 | Outer limit; misuse/inversion; vertical-horizontal interdependence; subject restriction; conditionality; single-vs-compound act; relational unlocking; prerequisite status; proportionality; divine-possession naming; sustaining practices; terminal-vs-transitional state | Out of grain — same class, whole-characteristic synthesis. |
| F-005 | Mechanism of administration/conveyance | Out of grain — but note the *shape* (mechanism-type) is the same controlled-list gap already named for T5.3.1; worth building once, reused by both if it's ever built. |
| F-011 | Shares vocabulary with adjacent characteristics, or isolated | **ANSWERABLE VIA AGGREGATION** — the same T6.4.1/T6.1.1 mechanism exactly. |
| WS-001, WS-003, WS-004, WS-006 | Comparative-idiom mode; the Haman instance; liturgical refrain; tri-registry-distribution coherence | Out of grain — specific-passage and whole-programme synthesis questions. |
| WS-002 | Analytical relationship between two named Greek terms (G0019/G5544) as co-OWNER registry terms | **ANSWERABLE VIA AGGREGATION** — directly the T7.1.1/T6.4.3 mechanism, two specific codes named already. |
| L-001 – L-005, L-007 – L-014 (17 items) | Foundational position; simultaneity of modes; directionality/object; identity-diagnostic function; below-conscious operation; misdirected-form taxonomy; growth mechanism; definitional outward form; divine-essence naming; symmetry of the opposite; disposition-vs-act relationship; epistemic dimension; public-signal function; social reorganisation | Out of grain — whole-characteristic synthesis, none reducible to lexical or per-verse fact. |
| L-006 | Vocabulary includes a systematic taxonomy of misdirected forms | **PARTIAL — answerable via aggregation for the vocabulary-inventory half**, same T6.4.x mechanism; "systematic taxonomy" (the organising logic) is synthesis on top. |
| M-002, M-006 – M-007, M-009 – M-010 | Giver/receiver asymmetry; architectural/material realisation in worship; shared logic with a contrary reality; disposition-vs-mechanism causality; directional-reversal significance | Out of grain — whole-characteristic theological synthesis. |

## 6. Revised summary — all 181 active, non-deleted questions now accounted for

- **~20** answerable via the aggregation/rollup layer Window 1's design already supports (§3's 9,
  plus §5's T6.1.1/T6.1.2, F-011, L-006 partial, WS-002, LEV-CLN-02, LEV-GEN-01, plus T0.1.1/T4.1.1/
  T4.2.1 — corrected per the researcher's live correction, §2/§5, mechanical from a small
  divine-name lexicon + entity-linking, not dependent on Window 2's manual pass at all).
  **Materially cheaper than the Window-2-dependent items below**: this bucket doesn't wait on the
  manual HIB/phenomenon/operation pass ever having run for a given verse — direct relevance to the
  standing scale concern (#1379 v1).
- **~7** answerable via the same mechanism, one step larger (needs a human-party or angelic-party
  lexicon, not yet built/verified) — T4.3.1, T4.4.1, T4.6.1.
- **~5** already answerable today, structurally, by Window 2's existing `operation`/`operation_party`
  schema once the manual pass has run for that verse (T1.5.1, T1.6.1, T0.2.1, T5.4.1, T5.6.1).
- **~30 real, unowned gaps** — the original 4 (§4) plus the 26-question constitutional-level/
  faculty-engagement block (§5's headline finding) plus a handful of smaller controlled-list gaps
  (T0.4.1, T5.2.1, T5.3.1).
- **The remaining majority (well over 100)** are correctly out of single-verse grain entirely —
  whole-characteristic, cross-verse, or whole-book theological/interpretive synthesis, several
  stages beyond either Window 1 or Window 2 by the questions' own design, not a gap in either.

## 7. The T0.2.1 class — behavior-synthesis questions, must not be attempted at Level 2

**Researcher's ruling, verbatim, the criterion applied below:** only a small percentage of a
characteristic's verses ever directly state something feeding purpose/role/effect — the real
answer is derived by observing *behaviour* across multiple or all the related verses. This is a
distinct class of question: it cannot be supported from Level 1 (lexical) alone, and it needs a
level of *synthesising the described behaviour* before it can rightfully be answered at all — which
means it must not be proposed as a Level 2 target either (Level 2 = per-verse behaviour
description, `hib`/`phenomenon`/`operation` — still single-verse grain, one HIB, one verse, one
reading). T0.2.1-class questions need a level *above* Level 2: synthesis across a characteristic's
whole verse set, not per-verse capture at any level.

**The distinction that matters, stated precisely** (several items in §5/§6 above collapse two
different things that need to stay separate):

- **Mechanical aggregation** — every contributing per-verse fact is independently well-supported
  (a code is present or it isn't; two verses share a Strong's code or they don't); the cross-verse
  step is a plain rollup/count/join, not an interpretive act. T6.4.1, T7.1.2, T7.1.8, etc. (§3/§5)
  stay in this bucket — nothing here changes for them.
- **T0.2.1-class (behaviour-synthesis)** — most individual verses have nothing directly on point;
  the answer is a pattern judgement over the whole body of evidence, genuinely interpretive, not a
  count. This is the class this section isolates.

A few questions are **hybrid** — a mechanical fact sits inside them alongside a genuinely
interpretive second half. Flagged as such below, not forced into either bucket whole.

### `Characteristic (HIB behaviour)` (15) — all T0.2.1-class

| Code | Why it's this class |
|---|---|
| T1.2.1 | "Kind of phenomenon — act/disposition/condition/quality" is essentially never stated directly; it's read off the pattern of how the characteristic behaves across every occurrence. |
| T1.2.2 | Simple-vs-compound structure — same reasoning. |
| T1.3.1 – T1.3.3 | Structural opposite / exclusion boundary — inferred from contrastive patterns across many verses, not a stated fact. |
| T1.4.2 | Mode-variation-by-context — requires comparing behaviour across contexts. |
| T1.4.3 | Communicative/speech-based mode — needs confirming the pattern recurs, not one instance. |
| T1.5.2 | Consistency of immediate response across verses — a comparison judgement over T1.5.1's own per-verse answers, not a rollup of them. |
| T1.6.3 | Sustained effect vs. immediate response — same shape of comparison. |
| T1.7.1 / T1.7.2 | Conditions under which it takes hold / is blocked — classic behaviour-synthesis, rarely stated. |
| T2.9.2 | Origin single/multiple, changes with context — comparison across instances. |
| T5.1.2 | Reversible/irreversible — read off outcomes across multiple instances. |
| T5.3.2 | Mechanism differs by context — comparison. |
| T5.4.2 | What suffering does to the characteristic — synthesis across every suffering-adjacent instance. |

### `The HIB` (15) — all T0.2.1-class, several also inherit the real per-verse gap from §5

| Code | Why it's this class |
|---|---|
| T1.7.3 | State when present but doesn't take hold — needs comparing "took hold" vs. "didn't" instances. |
| T2.1.2 | "Pattern of engaged/absent levels *indicates*" — the question's own wording names the synthesis; also inherits T2.1.1's real gap (§5) underneath it. |
| T2.7.1 (HIB) | Body-link direction, cross-verse — needs comparing direction across every instance to call it consistent. |
| T2.10.1 (HIB) | Movement/sequence across levels — detecting a pattern, not stating one. |
| T3.1.3 – T3.11.3 (10 items) | "What the pattern of engagement/non-engagement *indicates* about the characteristic's nature" — explicitly interpretive per the question's own wording; each also inherits the corresponding faculty-field gap from §5. |

### `Characteristic relational` (17) — mostly T0.2.1-class, one clean split

| Code | Verdict | Why |
|---|---|---|
| T4.3.2 / T4.3.3 | T0.2.1-class | Giver's inner conditions; what precedes extension — behaviour pattern, not a stated fact. |
| T4.4.2 / T4.4.3 | T0.2.1-class | Uptake conditions; state of one who doesn't take it up — same reasoning. |
| T4.5.1 – T4.5.3 | T0.2.1-class | "As the evidence shows" — explicit pattern-reading across the whole relational-instance set. |
| T6.1.1 | **Stays mechanical aggregation, not this class** | Which characteristics co-occur, how often — a plain count/join over already-tracked `cluster_code` membership, no interpretation needed for the count itself. |
| T6.1.2 | **T0.2.1-class — split from T6.1.1 above** | "What the co-occurrence pattern *shows*" is a genuinely interpretive act on top of T6.1.1's count — the count and its meaning are two different questions, wrongly treated as one pair in §5. |
| T6.2.1 / T6.2.2 | T0.2.1-class | Detecting a consistent sequence, and what it shows (causal/developmental/correlational) — both interpretive. |
| T6.3.1 – T6.3.3 | T0.2.1-class | Produces/produced-by/constituent-of — theological-structural inference from behaviour, not a countable fact. |
| T6.5.1 – T6.5.3 | T0.2.1-class | Nearest-neighbour distinction — comparative judgement across two characteristics' full evidence bases. |

### `Other non-human beings` (12) — mostly T0.2.1-class, two genuine hybrids

| Code | Verdict | Why |
|---|---|---|
| T0.1.2 | **HYBRID** | The raw fact ("is it ever borne by God") is mechanical — same divine-name-lexicon + entity-linking mechanism as the corrected T0.1.1 (§2/§5), aggregated as a count across the characteristic's verses. "What that pattern of presence/absence *indicates* for its place in the human person and the divine image" is T0.2.1-class synthesis on top — the two halves need to be answered by different mechanisms, not one. |
| T0.2.2 | **T0.2.1-class — the direct sibling of T0.2.1 itself**, confirmed by the old findings: one sampled answer literally says "see T0.2.2." | Created-design-vs-fallen-condition classification is exactly the same kind of judgement as T0.2.1's purpose question, over the same evidence. |
| T0.2.3, T0.3.1 – T0.3.3 | T0.2.1-class | Future orientation; divine-likeness aspect; shared-vs-analogue; image-condition indication — all deep theological synthesis over the whole evidence base. |
| T4.1.2 / T4.1.3 | T0.2.1-class | Basis/pattern of God's extension, what it shows of his disposition — classification requiring synthesis across many instances, not one. |
| T4.2.2 / T4.2.3 | T0.2.1-class | Same reasoning, human-to-God direction. |
| T4.6.2 | **HYBRID** | Whether an adversarial-being code ever co-occurs as an acting party is mechanically checkable (same lexicon-lookup shape as T0.1.1, once an angelic/adversarial-code lexicon exists — not yet verified, per §2's own honesty note on T4.6.1). Whether that makes the characteristic "a site of adversarial activity" as a *pattern* is T0.2.1-class synthesis on top. |
| T4.6.3 | **HYBRID**, same split as T4.6.2 | Mediated-through-angelic-ministry — same two-part shape. |

### `leviticus` (12) — split, not a block

| Code | Verdict | Why |
|---|---|---|
| LEV-CLN-02, LEV-GEN-01 | **Stays mechanical aggregation** (§5, unchanged) | Term-etymology/vocabulary-distribution questions, not behaviour-pattern questions. |
| LEV-CLN-01, LEV-CLN-03 – LEV-CLN-06, LEV-GEN-02 – LEV-GEN-06 | **T0.2.1-class** | Whole-book behaviour/theological synthesis (why cleanness matters, atonement mechanism, book-level synthesis, redemption vocabulary's operation) — none stated verse-by-verse, all read off the pattern across Leviticus as a whole. |

### `universal` (43) — split, not a block

| Code | Verdict | Why |
|---|---|---|
| F-011, WS-002, L-006 (vocabulary-inventory half only) | **Stays mechanical aggregation** (§5, unchanged) | Vocabulary-sharing/inventory facts, same T6.4.x mechanism. |
| Every other `C-`/`F-`/`L-`/`M-`/`WS-` question (37 items: C-001–003/006/007, F-001–004/006–010/012–014, WS-001/003/004/006, L-001–005/007–014, M-002/006/007/009/010, plus L-006's "systematic taxonomy" half) | **T0.2.1-class, all of them** | Every one of these asks what a word's behaviour *shows*, *reveals*, or *implies* across its whole usage (outer limits, misuse potential, subject restriction, proportionality, identity-diagnostic function, and so on) — the defining shape of this class, at its most concentrated in the whole catalogue. |

### Summary of this section

- **~85 of the 181 active questions are T0.2.1-class** — genuine behaviour-synthesis over a
  characteristic's whole evidence base, not answerable at Level 1 (lexical) or Level 2 (per-verse
  behaviour capture), and must not be designed as if they were either. This is the single largest
  bucket in the entire catalogue, larger than the mechanical-aggregation, real-gap, and
  directly-answerable buckets combined.
- **~7 hybrids** (T0.1.2, T4.6.2, T4.6.3, T6.1.1/T6.1.2 as a pair) need to be split into their
  mechanical half and their T0.2.1-class half explicitly — treating either half as covering the
  whole question would misrepresent what's actually been answered.
- This doesn't change §4's or §5's real-gap or mechanical-aggregation findings — it corrects how
  the remaining "out of grain" material was framed: not a vague "synthesis, someday," but a named,
  bounded class with its own explicit exclusion rule (never proposed at Level 2) and its own
  future home (a Level 3 / characteristic-synthesis stage, not yet designed, not this document's
  job to design).

## 8. Open items for your decision

1. The 4 real, unowned gaps (§4) — assign a home (which stage answers them), or explicitly decide
   the study doesn't need them answered, rather than leaving them unclaimed.
2. The aggregation/rollup layer itself (needed for 8 of the 22 questions) is not part of #1383's
   current build plan at all — worth scoping as its own explicit build item, not assumed to follow
   automatically once Window 1's schema exists.
3. Confirm `wa_obs_question_catalogue` is the right ongoing reference for this kind of check —
   #1007 already flagged its own question/window/answer/next-phase-role structure as deficient;
   this check used it as-is rather than waiting on that redesign, since the questions themselves
   are still the clearest live statement of what the study needs answered, structure aside.
4. §7's T0.2.1 class (~85 questions, the largest single bucket in the catalogue) has no assigned
   stage at all yet — confirmed to need a synthesis level above Level 2, but that level isn't
   designed. Worth its own scoping thread once Level 1/Level 2 are further along, not solved here.
