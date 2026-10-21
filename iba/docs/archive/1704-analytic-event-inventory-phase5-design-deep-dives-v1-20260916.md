# Analytic Event Inventory — Phase 5: Design Deep-Dives

**Escalation:** #1704 · **Phase:** 5 (Discovery → Match → Corrective Actions → Crosswalk →
**Design Deep-Dives**) · **Date:** 2026-09-16

**Purpose, per researcher instruction, verbatim:** *"you have a number of design questions and
rough generalisations in 1704. we now need to take each of the outstanding design elements and dig
into it. provide me with the framework, suggestions, pros and cons for each element. I cannot
design these in isolation with a one liner."* Eight items — Phase 3's Group B (5), Group C (2), and
`idiom` — each with what's already grounded (not re-argued), real options, and a recommendation
clearly marked as a recommendation, not a decision. Nothing here is built or approved.

---

## 1. Purpose-clause-detection (feeds T0.2.1)

**What's asked:** does created purpose show for this characteristic — grammatically, a Hebrew
lə+infinitive or Greek hina/hopos telic construction.

**Options:**

| | Mechanism | Pro | Con |
|---|---|---|---|
| A | Layer 1 mechanical column — `morph_code` pattern match for lə+infinitive / hina+subjunctive | Cheap, deterministic, reusable | Hebrew lə+infinitive is grammatically ambiguous (also marks simple infinitive uses) — real false-positive risk from a bare pattern match |
| B | Layer 2 `note_type` (new, e.g. `purpose_clause`) — LLM judges at reading time whether a construction is genuinely purposive, not just pattern-matched | Judgment-based, catches implicit purpose statements a regex would miss; reuses the existing, working Layer 2 architecture (same shape as `chain`/`connective`) | One more `note_type` to register and maintain; single-question consumer (T0.2.1 only) — a fair amount of infrastructure for one question |
| C | No mechanism — pure LLM reading of `verse_text` at answer time | Zero build cost | Repeats the exact failure mode that closed the original study (#1607 v14) — reading raw text instead of using structured signals, for a question that DOES have a real grammatical signal available |

**Recommendation: B**, scoped narrowly. It's the same shape as two mechanisms already proven to
work (`chain`, `connective`) — not a new kind of infrastructure, just one more instance of it.
Option C is only acceptable if the researcher judges one question isn't worth a dedicated
`note_type` — a legitimate cost call, not a design flaw either way.

---

## 2. Post-occurrence / characteristic-level sequence (feeds T1.5, T1.6, T5.2, T5.5 — 4 consumers)

**What's asked:** what precedes/follows the characteristic across a family's own verses — a
**cross-verse** grain nothing in the current design produces (reading stage is per-verse/per-
occurrence; this needs a temporal/developmental arc across a whole family).

**Options:**

| | Mechanism | Pro | Con |
|---|---|---|---|
| A | Mechanical canon-order scaffold — order a family's occurrences by book/chapter/verse and let the LLM reason against that ordering at answer time | Cheap, deterministic starting point | Canon order ≠ narrative/developmental order — two verses in different books can have a real before/after relationship canon order doesn't capture; risks being a false signal presented as structure |
| B | No new mechanism — feed the LLM all the subgroup's occurrences already available and let it reason about sequence cold, at answer time | No build cost, same shape as the confirmed-fine T0.2.2/T0.3 "pure synthesis" questions | Four separate consumer questions each re-deriving sequence from scratch with zero scaffolding — the exact "ignores the enriched data" risk this rebuild exists to avoid |
| C | A `sequence` observation at reading stage — the LLM notes explicit before/after signals as it already reads each occurrence, answer stage aggregates | Captures the signal at the point the LLM is already reading closely, not cold at answer time; produces a reusable observation | Reading stage already carries real per-strong verification load (#1682 §2 rule 10) — one more thing to track while reading |

**Recommendation: C, but not as new infrastructure — extend `chain`.** The temporal/sequential
signal this needs (wayyiqtol chains, "then"/"after this"/etc.) is exactly what `chain`'s own live
detection already looks for *within* one verse. The real design move is: when `chain` fires on an
occurrence, also ask whether that sequencing signal extends *across* the family's other occurrences
of the same root pattern — a scope extension of an existing, working mechanism, not a new one. Where
no such signal exists (most characteristics, honestly), the answer is "no clear sequence evidenced"
— a calibrated terse answer already validated as correct behaviour elsewhere in this catalogue
(#1700's own finding).

---

## 3. Future-orientation marker (feeds T5.6, partially T0.4)

**What's asked:** eschatological trajectory — verb tense/aspect plus lexical markers ("last days,"
"day of the LORD," etc.)

**Options:**

| | Mechanism | Pro | Con |
|---|---|---|---|
| A | Layer 1 `morph_code`-derived tense/aspect flag | Cheap, uses existing live data | Future tense alone doesn't mean "eschatological" — most future-tense verbs are ordinary future statements, not end-times language |
| B | A small, maintained lexical-marker list (`related_word`-shaped) checked against a fixed eschatological-vocabulary set | Targeted, low false-positive rate, cheap to build and to extend | Needs a maintained list — someone has to decide what belongs on it, and it can miss genuinely eschatological content that doesn't use the "expected" vocabulary |
| C | No mechanism, pure LLM reading | Zero cost | Same raw-reading risk as items 1/2 above |

**Recommendation: B, with A as a secondary confirming signal, not the primary trigger.** Tense
alone is too noisy to lead; a real vocabulary list is the actual signal, tense corroborates it.

---

## 4. Genre/contextual-setting classification (feeds T7.2.2, T7.2.4) — **different in kind from 1–3**

**This is not a "how to detect it" question — it's a base-data question the researcher has already
ruled on once.** Checked live before writing this: `cfg_method_rule` (`one-integrated-read-genre-
first`), corrected 2026-09-09 under escalation #1608: *"genre dropped from this rule — researcher
verdict, genre has no role in verse-focused lexical analysis."* `verse_meta.genre` was dropped as a
column for exactly this reason (#1607 D12/D13).

**The nuance worth surfacing, not deciding here:** that ruling was about genre's role in the
*lexical read* (Layer 1/2) — whether a verse's literary form should shape how its words get read
mechanically. It's a narrower claim than "T7.2.2/T7.2.4 should go unanswered." Those two catalogue
questions ask about literary form directly, as their own subject — a different question from
whether genre should gate lexical reading.

**Options, given that constraint:**

| | Mechanism | Pro | Con |
|---|---|---|---|
| A | Rebuild `verse_meta.genre` after all — reopens the 2026-09-09 ruling | Would answer T7.2.2/T7.2.4 directly | Directly contradicts a researcher verdict already on record; the ruling reads as a considered call, not an oversight |
| B | Accept T7.2.2/T7.2.4 as questions with **no mechanism, by design** — same disposition as the 12 "no mechanism needed" questions in Phase 4 (pure interpretive reading, if answered at all) | Consistent with the standing ruling, zero new build | The question stays genuinely unanswerable at any real signal-driven quality — it becomes pure guesswork if the answer-stage LLM attempts it cold |
| C | Retire T7.2.2/T7.2.4 from the live catalogue — if genre has no role in the method, a question built entirely around detecting genre may not belong in an active catalogue at all | Coherent with the 2026-09-09 ruling taken to its logical conclusion | A content/catalogue-curation decision, not a technical one — not mine to make |

**Recommendation: don't design a detection mechanism here.** This is a question for the
researcher about whether T7.2.2/T7.2.4 stay live at all, not a design gap to fill — flagged as
such rather than presented as a build item.

---

## 5. Typological-link (feeds T0.4.1) — feasibility question, not a design question

**What's asked:** OT-quotation/type-antitype significance. **No design options presented** — this
needs an external cross-reference resource (a maintained OT-in-NT quotation/typology dataset) this
project does not currently have. What *would* be needed if pursued: a structured cross-reference
table (verse → verse, with a typed relationship: quotation/allusion/type-antitype), sourced from an
existing scholarly cross-reference dataset, not built from this project's own data. **Recommend:
park, not design** — the real decision is whether acquiring such a dataset is worth it for one
question, not how to build a detector from data that doesn't exist.

---

## 6. T3-operation-surfacing (feeds T5.1, T5.3) — folds into #1701's resumption, framework for when it does

**What's asked:** the verb/operation itself as the primary analytical subject — the deepest
structural gap in the catalogue (#1702).

**Options for #1701's eventual resumption (not decided here, framework only):**

| | Mechanism | Pro | Con |
|---|---|---|---|
| A | Revive `cluster_strong.operation` (exists, confirmed dead) and wire it directly to T5.1/T5.3 | Minimal — the flag already exists, this is pure wiring | Doesn't actually change what the LLM is asked to do with a T3-tagged word beyond noticing it — thin fix for a "deepest gap" finding |
| B | Fold entirely into #1711's Layer 2 design — T3-operation questions become part of the earmarked-question set the LLM works through for T3-tagged strongs, no separate mechanism | Consistent with the #1705 closure's own direction (guide with data+questions, don't force structure); avoids building two overlapping mechanisms | Ties this item's resolution to #1711's own timeline, deliberately deferred behind Layer 1 |
| C | A structural reframe of T5's own questions — subject-as-process rather than subject-as-characteristic, a genuinely new catalogue design | Addresses the "deepest gap" at its actual root, per #1702's own diagnosis | Large scope, a real content-design project, not a mechanism to wire |

**Recommendation: B**, consistent with #1705's own resolution and #1701's explicit "fold in, don't
design standalone" instruction — but flag C's framing for whenever #1701 resumes in earnest, since
A alone would likely under-deliver against what #1702 actually found missing.

---

## 7. Constitutional-level vocabulary detection (feeds T2.1) — folds into #1701's resumption, framework for when it does

**What's asked:** spirit/soul/heart/mind referent-identity — no T-code covers this class at all.
The one prior attempt (the old T3 Inner-Faculties tier) was retired as "conceptually wrong" for
treating faculties as fixed entities to tag.

**The distinction worth making explicit, not yet decided:** the retired tier's error was tagging
**which faculty operates** (perception/cognition/etc. — a claim about *function*). This gap is about
**which constitutional referent is named** (spirit/soul/heart/mind — a claim about *identity*,
closer in kind to T10 Places or T14 Body-Parts than to the retired faculty-tagging). That distinction
may mean this gap doesn't carry the same "conceptually wrong" risk — worth the researcher's own
judgment, not assumed here.

**Options:**

| | Mechanism | Pro | Con |
|---|---|---|---|
| A | A genuine new referent-identity T-code (e.g. `T16` Constitutional-Level) — same mechanism as T10–T15, a `cluster_strong` classification | Consistent with `role`'s own design (the complete `cluster_strong.cluster_code` array, D1) — this class becomes visible to Layer 1/2 the same way every other referent class already is | A new T-code is a real classification project (sweep the corpus, tag every spirit/soul/heart/mind occurrence) — not a small addition |
| B | A fixed lexical-marker list (same shape as item 3's future-orientation marker) | Cheap, no new T-code needed | Weaker signal than a proper referent-identity tag; doesn't integrate with `role`'s own completeness discipline |
| C | Leave as-is — pure LLM reading, no mechanism (status quo) | Zero cost | The gap #1704 Phase 1c itself flagged as a genuine "no referent class exists" finding stays unaddressed |

**Recommendation: A**, but explicitly as its own scoped classification project (same shape as the
T4/T5/T6/T7/T9/T15 by-hand work already done), not folded silently into general Layer 1 work —
worth a real go/no-go call from the researcher given the sweep cost, not assumed cheap.

---

## 8. `idiom` note_type — genuinely unmatched to any catalogue question

**What it tests:** is a span part of a multi-code compound whose combined gloss diverges from a
literal code-by-code reading.

**Options:**

| | Disposition | Pro | Con |
|---|---|---|---|
| A | Match to T1.1 (Name/Naming, term-grain) — an idiom is itself a distinct sense worth naming | Gives it a catalogue home | Forced fit — T1.1 asks about primary terms, not compound idiomatic readings specifically |
| B | Match to T7.1.3 (semantic range) — an idiom is exactly a case where combined meaning diverges from literal reading, matching T7.1.3's "breadth of meaning" question directly | Genuinely on-topic, not forced | Still a secondary signal feeding a broader question, not a clean 1:1 |
| C | No catalogue-question link — `idiom` stays a Window-1/reading-stage infrastructure signal (ensures the LLM doesn't misread a compound as a literal sum of parts), same disposition already given to `entity_link`/`pronoun_resolution` earlier today | Consistent with how those two were just resolved; closes the item cleanly | Doesn't give `idiom` a "purpose" in the catalogue-answering sense some might expect every note_type to have |

**Recommendation: C**, by direct analogy with `entity_link`/`pronoun_resolution` (§0 rule 5a-
adjacent reasoning from today's session) — `idiom` is infrastructure that makes other readings
accurate, not itself a fact that answers one catalogue question. Still needs its `cfg_method_rule`
definition written (Group A, cheap) — this only resolves its *purpose*, not its build status.

---

## What's still genuinely open after this pass

None of the eight are decided — every recommendation above is a recommendation, `decision_required`
per the project's own axis. The two folded into #1701 (items 6/7) don't need action until that
escalation resumes. Item 4 (genre) is the one that most needs the researcher's own call before any
build work happens, since the recommendation there is explicitly "don't build," not "build this way."
