# Window 1 evidence-supply map — what the catalogue actually needs from Layer 1/Layer 2

**2026-09-07.** Corrects a wrong framing from earlier the same session. The question is not "which
of the 131 catalogue questions does Window 1 answer" — Window 1 (`verse_lexical`/`verse_lexical_note`)
has no concept of "a characteristic" at all; it works per code, per verse. The question is: **what
per-verse grammatical/relational evidence does Window 2 need pulled from Window 1's output to do
its own synthesis work**, and does the current note_type catalogue actually supply it. Researcher,
verbatim, correcting the first pass: *"window 1 does not have the context ready to answer any
characteristic questions directly. What it must do is do the verse analysis to allow window 2 to
have the information to do characteristic work. That is why things like chain, relationships, role
and function of words etc are all included in window 1."*

## The pipeline, confirmed against the live catalogue

`wa_obs_question_catalogue` (bible_research.db), 131 live rows (`deleted=0` — the real filter;
`status='active'` disagrees with it and is not reliable). Within nearly every component, the
pattern is explicit in the data itself:

- a **per-verse** sub-question, scope `Word/term (lexical)` / `Verse-context` / `The verse` (68
  rows, #737's own "Window 1" label) — e.g. `T3.1.1`: *"**In this verse**, does the characteristic
  engage the perceptive faculty... Record none if it does not."*
- immediately followed by a **cross-verse synthesis** sub-question, scope `The HIB` /
  `Characteristic (HIB behaviour)` / `Characteristic relational` / `Other non-human beings` (59
  rows, #737's "Window 2 / Include" label) — e.g. `T3.1.3`: *"**Across the verses**, what does the
  pattern of engagement... indicate about the characteristic's nature?"*

So even the 68 "Window 1" rows are not questions Window 1 answers as its own final output — they
are the **per-verse observation Window 2 needs before it can do the cross-verse synthesis**. The
real Window-1 job is smaller and lower-level than either bucket's question text: supply the
grammatical/relational **facts** (who is the subject, what does this verb's argument structure
show, is there a sequence/chain, which party is acting, how do two terms relate) that a reader —
human or Window 2's own LLM pass — combines into the answer.

## Per-component evidence trace

For each catalogue component (not each individual question — the evidence need is shared across a
component's per-verse/synthesis pair), what Window 2 actually needs, and whether the current Layer
1 (mechanical `verse_lexical` columns) / Layer 2 (`verse_lexical_note` note_types, split mechanical
vs LLM where the note_type itself has both) supplies it.

| Component(s) | What Window 2 needs as input | Layer 1 (mechanical) | Layer 2 — mechanical part | Layer 2 — LLM part | Verdict |
|---|---|---|---|---|---|
| T0.1 (Divine Nature Reflected) | who bears/acts/gives/receives the characteristic, and is that party God | `party_kind` (divine/human/non_human) | — | `verb_argument` (trigger=subject, impact=object), `entity_link` (party identity) | **Answerable** — mechanical party classification + two defined note_types together supply exactly this |
| T0.2 (Created Purpose) | is there a purpose/result clause attached to the characteristic | — | `related_word` pull (`strong_related`, total/unconditional) | `chain` (sequence/waw-consecutive), `connective` (clause-linking) | **Partial** — `chain` is defined; `connective` is named but has zero rule (escalation #1589) — purpose/result linking (ἵνα-clauses, "so that") is exactly a `connective` job and it's currently undefined |
| T0.3 (Image-Bearer Expression) | pure cross-verse synthesis — no new per-verse fact | (feeds from T0.1/T0.2 above) | — | — | **Window 2's own job**, no new Window-1 evidence needed beyond T0.1/T0.2 |
| T0.4 (Typological Significance) | does this verse/term echo a covenantal, eschatological, or christological pattern elsewhere in the canon | — | — | — | **Not Window 1's evidence to supply** — this needs cross-passage/cross-canon comparison, not verse-internal grammar; closer to a dedicated typology pass or Window 2's own broader reading |
| T1.1 (Name and Naming) | what the term/study-word is called, its root meaning | — | — | — | **Not verse_lexical/note at all** — `T1.1.1` is a plain `word_registry.word` lookup; `T1.1.2`/`T1.1.3` need `strong`/`strong_meaning_parsed` read at the LEXEME level (the standing term), not the per-occurrence level Layer 1/2 operate at |
| T1.2/T1.3 (Kind, Boundary) | is it an act/disposition/condition; what's its structural opposite | `morph_code` (POS: noun/verb/adjective/participle) | — | — | **Partial** — POS comes free from Layer 1; "structural opposite/antonym" has **no mechanism anywhere** in the current catalogue — real gap, same one T7.1.5 names below |
| T1.4 (Modes of Operation) | grammatical/stem form (per verse); manner of functioning | `morph_code` directly | — | possibly `noun_relational` (undefined) | **`T1.4.1a` answerable now** (pure `morph_code` read); **`T1.4.1b`/`T1.4.2`/`T1.4.3` (manner) have no dedicated note_type** — closest candidate is `noun_relational`, which is undefined |
| T1.5/T1.6 (Immediate Response, Sustained Effect) | what follows the characteristic, immediately and over time | — | — | `chain` (sequence), `verb_argument` (impact = what the action produces) | **Answerable** — both defined note_types map directly |
| T1.7 (Conditions of Reception) | what blocks/enables uptake, incl. adversarial/angelic interference | `party_kind` (coarse: human/non_human/divine only) | — | `entity_link` | **Partial** — `party_kind` cannot distinguish angelic from adversarial (`non_human` covers both); the finer distinction has to live in `entity_link`'s free-text finding, not a structured field |
| T2.1 (Spirit-Level Location) | which constitutional level (spirit/soul/heart/mind/body-part) the characteristic is linked to, and how | — | — | **`noun_relational`** (undefined) | **This is very likely `noun_relational`'s actual intended job** — the name matches exactly, and it has zero rule. Highest-priority gap to close, not a peripheral one |
| T2.9/T2.10 (Origin, Movement) | source of the characteristic; movement across levels | `party_kind` | — | `verb_argument`, `entity_link` | **Partial** — same `party_kind` coarseness gap as T1.7/T4.6 |
| **T3.1–T3.11 (the 11 inner faculties — perception, cognition, memory, affect, creativity, volition, agency, moral evaluation, conscience, conscientiousness, relational capacity)** | does a term in the verse belong to faculty X's semantic domain, and how does it relate to the characteristic | — | — | **nothing dedicated** | **The single biggest gap.** ~30 of the 131 catalogue rows live here. No note_type classifies a term against these 11 domains at all. `noun_relational`/`noun_severity` (both undefined) are the only plausible candidates by name; as built, the LLM brief gives it nothing to work from for this specific, large component family |
| T4.1/T4.2 (Divine Interface, both directions) | direction of the characteristic between God and person | `party_kind` | — | `verb_argument`, `entity_link` | **Answerable** — same good match as T0.1 |
| T4.3/T4.4 (Human Interface — Giving/Receiving) | direction between two human parties | `party_kind` | — | `verb_argument`, `entity_link` | **Answerable** |
| T4.5 (Human Interface — Boundaries) | pure cross-verse synthesis (relational scope pattern) | (feeds from T4.3/T4.4) | — | — | **Window 2's own job** |
| T4.6 (Spiritual Beings Interface) | does an angelic or adversarial party act; which | `party_kind` (same coarseness gap) | — | `entity_link` | **Partial**, confirmed gap (already found live building this: `party_kind` has only 3 values, `human`/`non_human`/`divine`) |
| T5.1/T5.2 (Transformation, Sequence) | before/during/after states; reversibility | — | — | `chain` | **Answerable** — `chain`'s defined scope covers this directly |
| T5.3 (Mechanism of Change) | discipline / encounter / gradual / sudden — classifying the triggering event | — | — | nothing dedicated | **Gap** — same semantic-domain-classification hole as T3.x, smaller scale |
| T5.4/T5.5 (Suffering, Formation) | relation to suffering; role in the sanctification arc | — | — | general LLM reading, no dedicated note_type | **Weak** — answerable only as free-text `finding` content under some other note_type, not a structured, checkable fact |
| T5.6 (Eschatological Trajectory) | present operation pointing to a future fullness | `morph_code` (aspect: perfect/imperfect/durative) | — | — | **Partial** — aspect is genuinely relevant and already mechanical; the theological "points toward eschatological fullness" judgement itself is Window 2's own reading, informed but not determined by the aspect fact |
| T6.1/T6.2/T6.3 (Co-occurrence, Sequence, Causal — BETWEEN characteristics) | which other characteristics' terms appear in the same verses, and how they relate | already queryable: `cluster_strong` × `verse_lexical.verse_id` | — | — | **Answerable, but as a report, not a note_type** — this is a cross-cluster aggregation query over data that already exists, not a new per-code finding |
| T6.4 (Vocabulary and Root Sharing) | shared vocabulary/roots across characteristics | — | `related_word` pull (`strong_related`) | `related_word` sorting (same-concept/genuine-relative/coincidental) | **Answerable** — this is exactly what `related_word` was built for, mechanical pull + LLM sort, matching the researcher's own mechanical/LLM split request precisely |
| T6.5 (Distinctions) | precise boundary vs. nearest-neighbour characteristic | (feeds from T6.1–T6.4) | — | — | **Window 2's own job** |
| T7.1 (Lexical and Semantic Analysis) | the primary term's root meaning, grammatical/semantic range, OT/NT continuity, antonym, coinage | `morph_code` (POS only) | — | — | **Not verse_lexical/note's job** — this is LEXEME-level (the standing Strong's code), not occurrence-level; needs a direct `strong`/`strong_meaning_parsed`/`strong_lsj_parsed` read for the characteristic's primary term(s), a report over existing lexicon tables, not new Layer 1/2 evidence |
| T7.2.1 (primary term's role + argument) | grammatical role; connective/chain edge in the verse's argument | `role` | — | `connective`, `chain` | **Answerable** |
| T7.2.2 (Literary Form) | genre — narrative/psalm/wisdom/prophecy/epistle/apocalyptic | — | — | — | **Confirmed gap, and exactly the genre question the researcher flagged.** `passage.genre` exists as a column but has had no per-verse home since the #1451 verse-scoping redesign (2026-09-05) — this was already an open item, not new |
| T7.2.3 (Logical Structure) | premises/conclusions in the verse's argument | — | — | `structural_pattern` | **Partial** — `structural_pattern` is defined but scoped to rhetorical figures (merism, chiasm, parallelism); a full premise/conclusion logical analysis is broader than that |
| T7.2.4 (Contextual Setting) | judicial / liturgical / covenantal / communal / eschatological register | — | — | — | **Same gap as genre** — no register/setting classification exists anywhere in the catalogue |
| T7.2.5/T7.2.6 (Primary Anchor Verse) | which verse, across the whole characteristic, is the fullest expression | (feeds from all per-verse findings) | — | — | **Window 2's own job** — a comparison across every verse's own findings |
| T7.3 (Human Science Frameworks) | which psych/philosophy/sociology lens illuminates the characteristic | — | — | — | **Not Window 1's evidence to supply at all** — explicitly flagged `Science` scope in #737's own triage, "likely out of scope entirely, unconfirmed" |

## Genre, language, and testament — taken into account, not an afterthought

- **Language/testament**: already mechanical, unconditional, on every `verse_lexical` row
  (`language` = `strong.language`; `testament` derived from `cfg_book_order.ordinal`) — directly
  feeds `T7.1.8` (OT/NT continuity) and the `related-word-sorting-language-aware` method rule
  (Hebrew families skew root-sharing, Greek families skew compound-morphology — already a live
  instruction in the LLM brief).
- **Genre**: **not** mechanical, **not** available per verse at all right now. This is a real,
  already-known gap (`iba/docs/1451-window1-layer2-verse-scoped-redesign-v1-20260905.md`'s own open
  item — dropping the `passage` dependency also dropped genre's only storage location) — it directly
  blocks `T7.2.2`/`T7.2.4` and weakens `T0.4`/`T5.6`'s theological readings, which all depend on
  knowing what kind of text is being read before drawing a conclusion from it.

## What this means, concretely

1. **The 5 already-defined note_types** (`related_word`, `structural_pattern`, `recurrence_role_shift`,
   `cross_lemma_shared_gloss`, `verb_argument`) genuinely do supply real, checkable evidence for a
   meaningful share of the catalogue — T0.1, T1.5/T1.6, T4.1–T4.4, T6.4, T7.2.1 all have a solid
   mechanical+LLM answer path already.
2. **`noun_relational` and `noun_severity` (escalation #1589, found undefined) are very likely the
   intended evidence-suppliers for T2.1 (constitutional location) and the entire T3.1–T3.11 inner-
   faculty family — the single largest, currently-weakest part of the catalogue (~30 rows).** This
   reframes #1589 from "a peripheral gap" to "the load-bearing gap" — defining these two properly is
   probably the highest-value next step, not a nice-to-have.
3. **`party_kind`'s 3-way split (human/non_human/divine) is too coarse** for every question that
   needs angelic-vs-adversarial specifically (T1.7.2, T4.6.1–T4.6.3, T2.10) — a real, narrow, fixable
   gap, not a design overhaul.
4. **Genre has no per-verse home** — confirmed, known, blocks a specific and identifiable subset of
   questions (T7.2.2, T7.2.4, weakens T0.4/T5.6).
5. **A whole family of questions (T1.1, T7.1, T6.1–T6.3) are not Layer 1/Layer 2's job at all** — they
   need LEXEME-level (`strong`/`strong_meaning_parsed`/`strong_related`) or CROSS-CLUSTER report
   queries over data that mostly already exists, not new per-occurrence findings. Building these as
   note_types would be a category error; they belong as a report step.
6. **A small number of questions (T0.4, T5.6, T7.3) are not verse-evidence-derivable at all** — they
   are Window 2's own theological/interpretive reading, which Window 1 can inform (aspect, party,
   sequence) but never settle.

## Not decided here

Which of these gaps to close, and how (define `noun_relational`/`noun_severity` properly; refine
`party_kind`; give genre a per-verse home; build the T7.1/T6.1 report mechanism) is a real set of
design decisions, the same way every other note_type's definition has been the researcher's own
call this session. Flagging the concrete, evidenced gaps here; not proposing fixes unilaterally.
