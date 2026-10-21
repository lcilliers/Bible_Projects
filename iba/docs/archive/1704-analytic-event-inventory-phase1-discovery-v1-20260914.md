# Analytic Event Inventory — Phase 1: Discovery

**Escalation:** #1704 · **Phase:** 1 of 3 (Discovery → Match → Corrective Actions) · **Date:** 2026-09-14

Per researcher instruction: `note_type` is one instance of a broader concept — an **analytic event**, any
distinct, named signal the lexical/cluster-reading pipeline can produce. Every event needs four things:
(1) a proper name, (2) a config definition, (3) a code home where it's triggered, (4) a purpose tying it
to the catalogue question(s) it serves. This phase assembles every candidate event found from the three
discovery vectors named — nothing is matched or decided here, that's Phase 2.

---

## Vector A — Backtrack from the catalogue questions

`wa_obs_question_catalogue.pattern_type` — a column that looks purpose-built for exactly this
classification — is **100% NULL** across every live row checked. A vestige of an earlier, never-populated
attempt at the same idea this escalation now exists to do properly.

**The a/b split pattern.** 5 question-pairs in the live catalogue split a mechanical detection half from
an interpretive follow-up half (`...a` detects, `...b` interprets the pattern `...a` found):

| Pair | `...a` (implied mechanical event) | `...b` (interpretation) | Live mechanism? |
|---|---|---|---|
| T0.1.2a/2b | "is the characteristic ever predicated of God" | what that pattern indicates | Likely `party_kind='divine'`/T7 — **unconfirmed**, not checked live this pass |
| T1.4.1a/1b | "grammatical/stem form of the term" | what mode(s) it operates in | **= `morph_code` directly** — Layer 1, already populated for every row. Cleanest possible wire, zero new mechanism needed |
| T4.6.2a/2b | "adversarial-being code appears as acting party" | what that shows | `party_kind`+T4 exists (#1702) — **wired in principle, zero findings ever** (#1700) |
| T4.6.3a/3b | "angelic-being code appears as acting party" | what that shows | `party_kind`+T9, same shape as above |
| T7.2.2a/2b | "what literary form carries the evidence" | what that form requires for interpretation | **No data source at all** — genre has no verse-level home in iba.db (#1607 D12/D13); currently unanswerable mechanically |

A full component-by-component backtrack of the remaining ~230 active catalogue questions (which implied
event, if any, each one needs) is a large undertaking and overlaps #1700's own section-by-section quality
review. Not duplicated here — recommend running that fuller sweep as part of Phase 2, against #1700's
findings rather than starting fresh.

---

## Vector B — Config sweep (`cfg_enum`, `cfg_method_rule`)

Full live `cfg_enum` landscape checked. Relevant groups:

- **`note_type`** (15 values) — this escalation's origin point, see #1589.
- **`party_kind`** (divine/human/non_human) — a live, working example of a *mostly*-complete event: named,
  config-defined, code-triggered (`lib/lexical.py`), purpose documented (#1607: escalates T0.1/T4.1–4.4).
  Worth using as the template for what "done" looks like.
- **`lexical_code_class`** (negator/connective_causal/connective_coordinating/connective_purpose/
  party_divine/party_human/party_angelic — 7 values) — the **retired precursor** to the current T4–T9
  cluster codes, migrated out and left orphaned (#1665's finding). One open question worth carrying into
  Phase 2: did the finer `connective_causal`/`connective_coordinating`/`connective_purpose` granularity
  survive the migration into the single flat `T6` (Connective) bucket, or was it lost? Not checked here.
- **`hib_kind`**, **`narrative_required_channel`**, **`candidate_ib_referent`**, **`passage_debate_status`**,
  **`passage_source`** — all live exclusively in `handlers/narrative.py`/`handlers/operations.py`, the
  **gated #737 debate pipeline**. Checked: zero references in `lib/`. **Out of scope** — not candidate
  events for the live lexical/cluster-reading pipeline, regardless of how event-shaped they look.
- `cfg_method_rule` coverage for `note_type` already fully mapped under #1589 (5 of 15 defined; `chain`/
  `idiom` code-covered with no config row at all — see #1589 v2).

---

## Vector C — Pipeline-stage escalation sweep

**Reading stage (process c)** — 8 live tag values, actually exercised across the full M10 prototype
(15 families, all `process-c-*-v2` files), **zero config or DB home** (no `cfg_enum` row, no table —
`ib_observation` doesn't exist yet, still #1691):

| Tag | Occurrences in M10 test |
|---|---|
| `instance-meaning` | 145 |
| `verse-grouping` | 110 |
| `difference-inference` | 39 |
| `surface-gloss-divergence` | 32 |
| `no-human-context` | 23 |
| `cross-family` | 20 |
| `data-error` | 17 |
| `alternative-meaning` | 8 |

**Answer stage (process d)** — 2 flag-events, exercised, structured (not boolean — each carries real
evidence), **zero config or DB home**:

- `needs_adjacent_verse_context` — array of `{verse, why}`. This is #1703's own subject.
- `cross_family_or_cluster_flags` — array of `{statement, related_family, related_cluster}`.

**Subgroup stage (process b)** — per this session's confirmed pipeline shape (§1 of
`outputs/markdown/lexical-verse-lexical-status-and-open-items-20260914.md`), process (b) now also
produces catalogue-question-driven `ib_observations`. Separately, the M10 prototype already showed
process (b) producing *ad hoc* strong-scoped and cluster-wide observations with "no current DB home"
(#1691 v16) — **not even named as distinct events yet**, the least-formed vocabulary of the four stages.

**Layer 1 mechanical columns** — candidate events by the same 4-part test, though scalar (one value per
row) rather than repeatable (many notes per row) like `note_type`: `role`, `party_kind`, `is_negator`,
`narrative_morph`, `gloss_consistent_in_verse`. Whether these count as "events" under the researcher's
redefinition, or stay a distinct category (columns vs. notes), is a Phase 2 scoping question — flagged,
not decided.

---

## Consolidated tally (candidates only — nothing matched yet)

| Vocabulary | Count | Config home? | Code home? | Catalogue link? |
|---|---|---|---|---|
| Layer 2 `note_type` | 15 | 5 of 15 (#1589) | 7 of 15, 2 undocumented (#1589) | 0 of 15 |
| Layer 1 mechanical columns | 5 (candidate, scope TBD) | partial | yes | partial (`party_kind` only, confirmed) |
| Reading-stage tags (process c) | 8 | 0 | prototype only, no DB table yet | 0 |
| Answer-stage flags (process d) | 2 | 0 | prototype only | 0 (structurally — but this *is* the mechanism that would carry catalogue evidence) |
| Subgroup-stage observations (process b) | ≥2 shapes, unnamed | 0 | prototype only | 0 |
| Catalogue-implied mechanical events (a/b split) | 5 pairs | n/a (these are the *demand* side) | 2 of 5 have any live mechanism, 0 of those 2 actually connected | n/a |

Five separate, non-communicating vocabularies for what is, per the researcher's framing, one underlying
concept. Phase 2 is where each of these gets checked against the real 4-part test (name / config / code /
purpose) and the genuine gaps get separated from the ones that are actually fine and just haven't been
looked at together before.

---

## Phase 1b — corrected pass: role (T3–T15) and movement/web events

**Researcher correction, verbatim:** *"I am missing events to tackle the implications of the roles (T3 -
T15). Think of the event as the step/activity/focus that need to trigger the discovery of something in
the data and formulate it in such a way that the question can be answered by llm by looking at all the
elements to arrive at an answer. The event is not generating the answer, it is surfacing the relevant
data."*

The first pass leaned on the a/b question-code suffix as a shortcut and missed this entirely. Actually
reading the full T1.4/T2.7/T2.10/T4/T5/T6/T7 question text (63 questions) against the T3–T15 role
descriptions surfaces a much richer, and much more consequential, set of gaps — because these are the
questions that ask about *movement* and *relationship*, the study's actual object.

### T4 (Divine/Human Interfaces) — the largest miss, 15 questions, effectively zero mechanism

T4.1 (God→Human), T4.2 (Human→God), T4.3 (Human giving), T4.4 (Human receiving), T4.5 (Boundaries) are
**all directional relational-frame questions** — who acts, who receives, which way does it move. Only
T4.6 (spiritual beings) has any live mechanism at all (`party_kind`+T4/T9, and per #1700 that one has
zero findings ever). T4.1–T4.5 have **no surfacing mechanism whatsoever**.

The missing event has a natural shape already sitting in the design, just never built out: **`verb_argument`**
(config id 63, a real `note_type`) is defined exactly as trigger (agent, `target_verse_lexical_id`) +
impact (patient, `related_verse_lexical_ids`). Pair each side's `party_kind` and the direction falls out
mechanically — trigger=divine/impact=human surfaces T4.1, trigger=human/impact=divine surfaces T4.2,
trigger=human/impact=human surfaces T4.3/T4.4. This is a real, previously-unnamed event —
call it **directional-party-frame** — that would let the LLM answering T4.1–T4.5 see who-does-what-to-whom
laid out, instead of re-deriving it from plain verse text (the exact failure #1607 v14 already diagnosed).
Its ingredients (`verb_argument`, `party_kind`) exist by name; the event that *combines* them does not.
And `verb_argument` itself is barely more than a name today — **1 live example ever**, no trigger logic
built (#1606/#1607) — so even the base ingredient is unbuilt in practice, not just unconnected.

### T2.7 / T2.10 (Body-Direction, Constitutional Movement) — confirmed T14 dependency

Both explicitly ask about movement *through the body* (spirit→soul→body direction, body-link direction).
Both depend on T14 (Body-Parts) detection. #1702 already found T14 has no lexicon-assist column — this
reading confirms that gap is not abstract, it directly blocks two specific, live, active questions.

### T5 (Formative/Developmental, the whole tier) — points straight at T3, the deepest gap

T5.3 ("by what mechanism does the characteristic produce change — discipline, encounter, gradual
formation, sudden transformation, or other") is asking for a mechanism-type classification that should be
surfaced from **T3 (Operations)** — the verb/movement referent-identity code #1702 already named as the
deepest gap ("no question treats operation/movement as primary subject"). This reading ties that general
finding to a specific, live question rather than leaving it a general observation. T5.2 ("sequence of
inner states... a before, during, and after") wants a temporal/process-sequence event at the
**characteristic level across multiple verses** — a different grain from `chain`/`recurrence_role_shift`,
which operate within one verse/span. Genuinely unnamed, not yet even a candidate.

### T6 (Structural Relationships) — literally "the web," and its own mechanism already existed once

T6.1 (co-occurrence: "which adjacent characteristics appear alongside this one") is the single most
web-shaped question in the whole catalogue — and has **zero live mechanism**. Checked live: a script that
did exactly this, `_assess_cross_cluster_cooccurrence.py` ("the cross-cluster co-occurrence matrix"),
**already exists and is switched off** — escalation #729, zero `cfg_method` call sites, inactive since
2026-08-18. This mechanism was not merely never built; it was built, then retired. T6.4 (vocabulary/root
sharing) is in better shape — it already has real building blocks (`related_word`, `cross_lemma_shared_gloss`)
that just need cross-characteristic aggregation wired on top, not a fresh mechanism.

### T10 / T11 / T12 / T13 — re-checked, genuinely no catalogue demand (not a missed search)

Full-text keyword sweep of all 98 live active questions for place/location, corporate/collective,
object/instrument, and natural-world language, to check whether #1702's "genuinely open, no evaluated
question-need" verdict was itself too quick. It wasn't: 0 genuine hits for corporate/collective or
object/instrument; the handful of place/natural-world keyword matches (e.g. T0.3.3, T6.3.3) are generic
usage ("where," "constituent"), not real T10/T12/T13 relevance, confirmed by reading each in full. This is
a real, checked finding, not an unexamined gap — T10–T13 stay open questions for the researcher (does the
catalogue need new questions for these referent classes, or do they genuinely not matter to the study),
not events I failed to find.

### T7 (catalogue tier, not to be confused with cluster T7/Party-Divine) — mostly lexical, already covered

Full tier read (14 questions). T7.1 (lexical/semantic) and T7.1.5 (structural opposite) map cleanly onto
existing `related_word`/`cross_lemma_shared_gloss` note_types. T7.2.1 explicitly names "connective/chain
edge" — direct existing-note_type territory. T7.2.2a/b is the already-identified genre gap (Vector A). No
new events found in this tier beyond what's already listed.

### Consequence for Phase 2

The event list from Phase 1a undercounted the highest-value gaps. Add to the candidate set: **directional-party-frame**
(T4.1–T4.5, built from `verb_argument`+`party_kind`, currently unbuilt in practice), **T3-operation-surfacing**
(feeds T5.3 and is the deepest structural gap per #1702), **T14-body-part-surfacing** (feeds T2.7/T2.10,
already named by #1702, now confirmed load-bearing), and **cross-characteristic co-occurrence** (T6.1 —
a mechanism that already existed once and was retired, the cheapest of these four to reconsider since the
code is not gone, only switched off).

---

## Phase 1c — full catalogue sweep, every live question, no sampling

**Researcher instruction, verbatim:** *"I dont understand why you are continuing to compromise and stop
short. We are not busy with a game, we are not looking for samples. you are suppose to map events for
every question eventuallity, ensure that the data will be surfaced before the question is asked. so keep
going."*

Every one of the 98 live, active catalogue questions read in full (T0/T1/T2/T4/T5/T6/T7 — the catalogue
carries no live T3 tier; that slot is the retired Inner-Faculties tier, #1598). Grouped by component,
since most questions in one component share the same underlying event need — the table names the event
each component actually needs, not each question in isolation, but every question has been read and is
accounted for.

### T0 — Divine Nature Reflected / Created Purpose / Image-Bearer / Typological (10 questions)

| Component | Questions | Event needed | Status |
|---|---|---|---|
| T0.1 Divine Nature Reflected | 1.1, 1.2a, 1.2b | **directional-party-frame** (relation = bears/acts/gives/is-object — the exact same trigger/impact shape as T4.1–T4.5) | Same gap as T4 — see Phase 1b |
| T0.2 Created Purpose | 2.1, 2.2, 2.3 | 2.1 needs a **purpose-clause-detection** event (Hebrew lə+infinitive, Greek hina/hopos telic markers) — genuinely new, no existing mechanism. 2.2/2.3 are pure theological judgement on already-surfaced data, no event needed | 2.1: new gap. 2.2/2.3: no event needed |
| T0.3 Image-Bearer Expression | 3.1, 3.2, 3.3 | None — explicitly derivative of T0.1+T0.2 ("from the characteristic's God-relation and its role") | Synthesis only, no new event |
| T0.4 Typological Significance | 4.1 | **typological-link** event — OT quotation/type-antitype marker. No mechanism exists; likely needs a cross-reference resource this project doesn't currently have, not a Layer 1/2 fix | New gap, low feasibility without a cross-reference data source |

### T1 — Name/Naming, Kind, Boundary, Modes of Operation, Immediate Response, Sustained Effect, Conditions of Reception (19 questions)

| Component | Questions | Event needed | Status |
|---|---|---|---|
| T1.1 Name and Naming | 1.1, 1.2, 1.3 | Term-level (not verse-level) aggregation of `related_word`/gloss data — a grain mismatch, not a missing event | Existing mechanism, wrong grain — flag for Phase 2 |
| T1.2 Kind | 2.1 | **kind-classification** event, mechanical from `morph_code`'s part-of-speech (verb→act, adjective→quality, noun→condition/disposition) | New, cheap — direct morph_code derivation, unconnected |
| | 2.2 | `compound_unit` note_type — direct consumer | Note_type exists, **undefined** (#1589's 6-gap list) — this is its purpose |
| T1.3 Boundary | 3.1, 3.2, 3.3 | "structural opposite term" detection — **same demand as T7.1.5**, not a separate event | Duplicate consumer, single event to design |
| T1.4 Modes of Operation | 4.1a, 4.1b, 4.2, 4.3 | Covered in Phase 1b — 4.1a = `morph_code` directly | See Phase 1b |
| T1.5 Immediate Response | 5.1, 5.2 | **post-occurrence sequence** event — what follows the characteristic in the verse/passage | Loosely related to reading-stage tags (`instance-meaning`/`difference-inference`), not formally connected |
| T1.6 Sustained Effect | 6.1, 6.3 | Same **sequence** event as T1.5, extended over time | Same gap as T1.5 |
| T1.7 Conditions of Reception | 7.1, 7.2, 7.3 | `polarity` note_type (blocked/distorted/resisted) + `party_kind`/T4/T9 (adversarial/angelic interference — same mechanism as T4.6) | `polarity` exists, **undefined** (#1589) — this reading gives it a real purpose; party_kind mechanism same as T4.6 |

### T2 — Spirit-Level Location, Body-Direction, Constitutional Movement, Origin/Source (6 questions)

| Component | Questions | Event needed | Status |
|---|---|---|---|
| T2.1 Spirit-Level Location | 1.1, 1.2 | **constitutional-level vocabulary detection** (spirit/soul/heart/mind/named body part) | **No T-code covers this at all.** T14 covers body parts only. Constitutional-level terms (ruach/nephesh/lev/nous) have no referent class in T2–T15. The one prior attempt at modelling this (catalogue T3, Inner Faculties) was retired as conceptually wrong (#1598, #1701's entity-vs-process critique) — this question may itself need re-examination in light of that critique, not just a mechanical fix. **Flagging as a design tension for the researcher, not resolving it here.** |
| T2.7 Body — Direction | 7.1 | Covered in Phase 1b — T14 dependency | See Phase 1b |
| T2.9 Origin and Source | 9.1, 9.2 | **directional-party-frame** again (generated-within/received-from-person/bestowed-by-God/introduced-by-spirit — the same trigger shape as T4.1–T4.4, reframed as "origin") | Same event as T0.1/T4 — third confirmed consumer |
| T2.10 Constitutional Movement | 10.1 | Covered in Phase 1b — T14 + sequence | See Phase 1b |

### T4 — Divine/Human Interfaces, Spiritual Beings (20 questions)

Fully covered in Phase 1b — **directional-party-frame** (T4.1–T4.5) and existing `party_kind`+T4/T9 mechanism (T4.6, unconnected per #1700).

### T5 — Formative/Developmental (9 questions)

| Component | Questions | Event needed | Status |
|---|---|---|---|
| T5.1 Nature of Transformation | 1.1, 1.2 | **T3-operation-surfacing** (transformation tracking — same event as T5.3) | Same gap as T5.3, see Phase 1b |
| T5.2 Sequence of Inner States | 2.1 | **characteristic-level sequence** event (before/during/after across a family's verses) | New, unnamed — see Phase 1b |
| T5.3 Mechanism of Change | 3.1, 3.2 | **T3-operation-surfacing** | Deepest gap, #1702 — see Phase 1b |
| T5.4 Suffering and Affliction | 4.1, 4.2 | **cross-characteristic co-occurrence** (does a "suffering" cluster/M-code co-occur in the same verse) — same mechanism as T6.1 | Retired script, see Phase 1b — third confirmed consumer |
| T5.5 Formation and Sanctification | 5.1 | Same **characteristic-level sequence** event as T5.2, longitudinal | Same gap as T5.2 |
| T5.6 Eschatological Trajectory | 6.1 | **future-orientation marker** — verb tense/aspect (`morph_code`) + lexical markers ("last days" etc., `related_word`-shaped) | New, lighter-weight — feasible from existing Layer 1 data, unconnected |

### T6 — Structural Relationships (13 questions)

| Component | Questions | Event needed | Status |
|---|---|---|---|
| T6.1 Co-occurrence | 1.1, 1.2 | **cross-characteristic co-occurrence** | Retired script (`_assess_cross_cluster_cooccurrence.py`, #729) — see Phase 1b |
| T6.2 Sequential Relationships | 2.1, 2.2 | Same event as T6.1, extended with corpus-wide ordering | Refinement of T6.1's gap, not new |
| T6.3 Causal/Constitutive Relationships | 3.1, 3.2, 3.3 | Cross-characteristic co-occurrence **+ causal-connective detection** | This is exactly where `lexical_code_class`'s retired `connective_causal` granularity (flagged in Phase 1a Vector B as "worth checking, not checked") becomes load-bearing — **elevating that from a curiosity to a confirmed dependency, needs checking now** |
| T6.4 Vocabulary and Root Sharing | 4.1, 4.2, 4.3 | `related_word` + `cross_lemma_shared_gloss`, cross-characteristic aggregation | Building blocks exist — see Phase 1b |
| T6.5 Distinctions | 5.1, 5.2, 5.3 | Synthesis of T6.1+T6.4 | No new event |

### T7 — Lexical/Semantic, Verse/Literary, Human Science (21 questions)

| Component | Questions | Event needed | Status |
|---|---|---|---|
| T7.1 Lexical and Semantic Analysis | 1.1–1.10 | `related_word`, `cross_lemma_shared_gloss` — term-level (same grain issue as T1.1) | Existing mechanism, term-grain not verse-grain |
| T7.2.1 Verse function | 2.1 | `connective`/`chain` note_types directly named in the question text | Existing, already covered |
| T7.2.2 Literary form | 2.2a, 2.2b | Genre detection | **No data source in iba.db** — #1607 D12/D13, Vector A finding |
| T7.2.3 Logical structure | 2.3 | Argument-structure (premises/conclusions) | Interpretive only — not a Layer 1/2-surfaceable event, direct LLM reading of `verse_text` |
| T7.2.4 Contextual setting | 2.4 | Setting classification (judicial/liturgical/covenantal/communal/eschatological) | Same class of gap as genre — no data source |
| T7.2.5/2.6 Primary anchor verse | 2.5, 2.6 | **anchor-verse ranking** event — which verse most fully expresses the characteristic | Direct connection to #1526's own resolved_sense-collapse/anchor-verse work, already in progress |
| T7.3 Human Science Frameworks | 3.1–3.4 | None — external interpretive lens applied to already-surfaced evidence | No event needed, pure interpretation |

### Full-sweep summary — every genuinely new or newly-confirmed event, all traceable to a specific question

1. **directional-party-frame** — `verb_argument`+`party_kind` combined. Feeds T0.1, T2.9, T4.1–T4.5 (18 questions total). Highest-value gap in the whole catalogue by question count.
2. **T3-operation-surfacing** — feeds T5.1, T5.3 (deepest structural gap, #1702).
3. **T14-body-part-surfacing** — feeds T2.7, T2.10 (already named #1702, now confirmed).
4. **cross-characteristic co-occurrence** — feeds T5.4, T6.1, T6.2, T6.3 (partial). Mechanism already built once, retired (#729) — cheapest to recover.
5. **causal-connective detection** (`connective_causal`, from the retired `lexical_code_class` granularity) — feeds T6.3 specifically. Needs checking whether this granularity survived the migration into flat `T6`.
6. **purpose-clause-detection** — feeds T0.2.1. New, no existing mechanism.
7. **kind-classification** — feeds T1.2.1. New, cheap (direct `morph_code` derivation).
8. **`compound_unit`** note_type — feeds T1.2.2. Name exists (#1589), undefined.
9. **structural-opposite-term detection** — feeds T1.3, T7.1.5 (duplicate demand, one event).
10. **`polarity`** note_type — feeds T1.7 directly, gives it a real purpose. Name exists (#1589), undefined.
11. **post-occurrence / characteristic-level sequence** — feeds T1.5, T1.6, T5.2, T5.5. New, unnamed, four consumers.
12. **future-orientation marker** — feeds T5.6, T0.4 (typological, partial overlap). New, lightweight, feasible from existing Layer 1 data.
13. **constitutional-level vocabulary detection** — feeds T2.1. **No T-code exists for this referent class at all** — and its one prior attempt (catalogue T3, Inner Faculties) was retired as conceptually wrong. Flagged as a design tension for the researcher's own decision, not a mechanical gap to just fill.
14. **typological-link** (T0.4) — likely needs an external cross-reference resource, not answerable from this project's current data model.
15. **genre / contextual-setting classification** — feeds T7.2.2, T7.2.4. No data source in iba.db (#1607 D12/D13).
16. **anchor-verse ranking** — feeds T7.2.5/2.6. Already in progress at #1526.
17. **term-grain aggregation** (not a new event, a grain correction) — T1.1, T7.1 want term-level, not verse-level, output from `related_word`/gloss mechanisms already covered.

Confirmed with no event needed at all (pure synthesis or pure external interpretation, verified by reading
every question in the component, not assumed): T0.2.2/2.3, T0.3 (all), T7.2.3, T7.2.4's interpretive half,
T7.3 (all), T6.5 (all).

This is the full, exhaustive Phase 1 result — every one of the 98 live catalogue questions has been read
and is accounted for above, either mapped to an event or confirmed to need none. Phase 2 (match each event
against the 4-part test) is next.
