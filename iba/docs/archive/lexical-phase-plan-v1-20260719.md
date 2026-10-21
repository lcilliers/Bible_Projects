# Plan: the lexical compilation & analysis phase (the reading)

> **Status: DESIGN FOR CONFIRMATION. No DB changes / no build until approved.** Directed 2026-07-19.
> The next phase after the base layer: read each passage for the inner-being it expresses, using the
> API, and record it so the corpus becomes a queryable, validated evidence base.

---

## 1. Scope & the shape of this phase

- **Reading unit = the passage** (the base layer already built it). A passage is read *whole* — the
  IB role of a span is only assessable in the full passage (researcher, 2026-07-19).
- **Long passages excluded from the general run.** Passages with `verse_count > 10` (`needs_review`,
  47 of them) are **held out** of the general lexical run and handled **separately, after** it (§8).
- **The API does the reading;** deterministic code does the mechanical substrate and the validation.
- **Store both** the holistic passage meaning **and** the decomposed dimensional lexical (§5) — they
  are two views of one read, produced in one call and cross-checked.

The study's two standing bars govern: **comprehensiveness** (nothing understated — silence is an
explicit finding) and **robustness** (the read withstands deeper questioning). The design below is
built to defend both against the four risks you named (§6).

---

## 2. The dimensions (from the old DB) and the mechanical / read split

The old system's authoritative dimension set is the **VE-lexical catalogue** (`ve_nr` 101–118 +
verse-level). The cycle doc §3 gives the split: *morphology builds ~8 reliably and approximates ~6,
but cannot identify the characteristic or assign the role — meaning does.* Applying that:

### A. MECHANICAL — deterministic from the morphology we already hold (compute, don't read)

| ve_nr | dim | shape | basis |
| --- | --- | --- | --- |
| 101 | sense | value | STEP sub-gloss for the span |
| 102 | type | value | part-of-speech → action / status / quality |
| 106 | operation | event | the governing verb/predicate |
| 104 | seat | pair | construct morphology (construct-gated) |
| 108 | manner | pair | preposition-marked adverbial |
| 109 | intensity | pair/flag | `kol` / `me'od` / doubled verb / emphatic |
| 112 | coupling | pair | construct / preposition weld |
| 113 | prohibition | flag | negation / prohibition particle |
| 116 | locus | value | IB-internal vs external, from morphology + lemma |
| — | genre / passage | verse | `verse.genre`, `verse.passage_id` (passage already built) |

### B. HYBRID — morphology flags the *slot*, the read binds it and types it

| ve_nr | dim | shape | what morph gives / what the read must add |
| --- | --- | --- | --- |
| 103 | source | pair | morph flags an antecedent slot; read binds it + splits **driver vs restraint** |
| 105 | bearer | pair | morph flags the subject; read confirms the experiencer |
| 107 | target | pair | morph flags an object; read binds it + types the object |
| 110 | specifier | pair | morph flags a genitive/"of the LORD"; read interprets which/whose |
| 111 | effect | pair | morph flags a result clause; read binds the produced-state |

### C. READING-REQUIRED — only meaning-in-passage gives these

| ve_nr | dim | basis |
| --- | --- | --- |
| — | **the characteristic** (identity) | the IB disposition the passage turns on — meaning, never a lookup |
| 115 | **role** | characteristic / qualifier / standalone / uncertain (the sanity screen) |
| 114 | reading | the evidence-anchored read note (translit + verse-quote + meaning + finding) |
| 117 | device | literary device (metaphor / simile / personification / …; vehicle span for comparisons) |
| 118 | direction | movement vector (toward-god / from-god / inward / outward / reciprocal / static) |
| D7 | process | the passage-level movement/process (the whole-passage read — fits the unit exactly) |

**So:** ~9 dimensions are mechanical, ~5 are hybrid (slot pre-filled mechanically, bound by the
read), and ~6 are reading-only — including the characteristic identity and the role, which is where
all the value and all the risk live.

---

## 3. Why compute the mechanical layer at all (your question)

You asked: *if we pass the whole passage to the API anyway, why do a mechanical morph breakdown
first?* The mechanical layer is **not a pre-read that the API repeats** — it does three things the
read should not:

1. **It is free and exact.** The morphology is already parsed on every span. Person, POS, construct,
   preposition, negation, intensifier are *deterministic*. Asking the API to re-derive grammar it
   can get wrong — when the morph states it exactly — spends tokens to *add* error.
2. **It grounds the read.** The mechanical facts are passed **into** the prompt, so the API reads
   *meaning on a known grammatical skeleton* — it is told the verb, the object slot, the genitive;
   it does not guess them. This is the single biggest reducer of hallucination.
3. **It validates the read (convergence).** The mechanical values are an objective floor. When the
   read asserts something the morphology contradicts (a source where there is no antecedent slot; a
   target the grammar doesn't support), the disagreement is a **flag**, not a silent acceptance.
   This is the deterministic gate the whole app exists to provide.

So the mechanical pass is the **floor and the anchor**, computed once, passed in, and used to check
the read — never a duplicate of it.

---

## 4. The reading, config-governed (your proposal — yes)

Your instinct is right and it is how the app should work: **the rule-set is config, applied to each
unit passed to the API.** Per passage (≤10 verses):

1. **Assemble the reading payload** (deterministic): the passage's verses in order, each verse's
   spans in position order (surface · Strong's · gloss · morph), the **pre-computed mechanical
   dimensions**, the candidate stamps, and the **rules** (dimension definitions, the screens, the
   output schema, the provenance requirement). Everything the base layer already produces.
2. **One API call** reads the passage and returns **two coupled things**:
   - the **holistic passage meaning** — the integrated account of the inner-being process the
     passage expresses (D7 process, read whole); and
   - for **each IB characteristic** the passage turns on, its **dimensional decomposition** — the
     reading-required + hybrid dimension values, each **self-interpretable** (carries its trigger),
     **citing the text**, marked **STATED vs INFERRED**, and **value-or-explicit-`none`** (silence
     is a finding, never a blank).
3. **Screens run in the read** (config): Screen-0 *the human inner being is the subject; God is the
   arena, not a characteristic* (so the over-inclusive God/function-word candidates are demoted
   here, not in the seed — this is where they belong); role assignment; the validate/none rule.
4. **Validate + store** (deterministic): convergence against the mechanical floor, completeness
   (every mandatory dimension present or `none`), citation present, provenance set. Then persist.

The rules — the dimension catalogue, the screens, the output schema, the model tier — all live in
config, so the reading is *consistently applied* to every passage and changeable without code.

---

## 5. Should the meaning be saved in components (the lexical)? — the crux

**Yes — decompose, and also keep the holistic read. Both, layered.** This is the heart of your
question, so here is the reasoning, tied directly to what you're worried about.

**Why decomposition is not optional — it is the whole point of a database:**
- **Cross-passage / cross-book analytics (your concern).** A holistic paragraph per passage cannot
  be aggregated. "How does *fear* move from source to target across the prophets?" · "Which
  characteristics cohabit with *anger*?" · "The intensity distribution of *joy* in the Psalter?" —
  every one of these needs **structured, queryable dimension values**. Holistic-only meaning makes
  cross-passage and cross-book analysis **impossible**; you'd have 18k prose summaries, not an
  evidence base. Decomposition is what turns the corpus into something you can *query and prove
  from*.
- **Completeness (your concern).** The dimensions are a **checklist**. Requiring each to be
  answered — value or explicit `none` — fights silent omission. A free-text read can quietly skip
  the effect or the source; the dimensional schema makes the gap *visible* and records the silence
  as a finding.
- **Drift & bias (your concern).** Structured values are **checkable**: against the mechanical
  floor (convergence), against the rules (every value must cite its trigger), and across the corpus
  (band-tests — does a dimension's value distribution track reading-*order* rather than the text?).
  Free-text meaning cannot be checked this way. **Decomposition is precisely what enables the gates
  that catch drift and bias.** Holistic-only is the prior, failed method — un-checkable.

**Why keep the holistic read too (don't over-fragment):**
- The passage's integrated sense — the *process* — is real and is lost if only fragments are stored.
  The holistic read is the human-readable record, the provenance the decomposition is *derived from*
  and *checked against*, and the D7 process itself.

**The safeguard against the study's #1 failure (over-structuring / eisegesis):** decompose
**read-first, not grid-first.** The model reads the passage's IB movement *whole*, then **expresses
each characteristic in the dimensional structure**, citing the text — the dimensions are **outputs
of the read, never boxes filled before understanding**. "Patterns emerge; they are not imposed."
Every value carries STATED/INFERRED + a citation, so a decomposed value is always traceable back to
the passage. This is what makes decomposition safe rather than the grid that failed before.

**Net:** one API call → the holistic passage meaning **and** its dimensional decomposition, stored
together and cross-checked. You lose nothing (the whole meaning is kept) and gain everything the
database is for (analytics + validation).

---

## 6. Your four risks, and how each side handles them

| risk | holistic-only (read, store prose) | **decomposed + mechanically grounded (recommended)** |
| --- | --- | --- |
| **drift** | un-catchable — no structured values to band-test | caught: convergence vs the mechanical floor + citation rule + corpus band-tests |
| **bias** | invisible | visible: each value cites its trigger; STATED vs INFERRED marked |
| **incomplete** | silent omission | dimensional checklist forces value-or-`none`; silence recorded |
| **cross-passage / book** | impossible (prose can't aggregate) | enabled: queryable dimension values |

The decomposed+grounded design is the **only** one that defends all four. Holistic-only incurs all
four — it is the method that already failed. (And decomposition *without* the read-first safeguard
risks the over-structuring failure — which is why §5's read-first rule is not optional.)

---

## 7. Data model & operation (high level — for the build after confirmation)

- **New tables** (mirroring the proven old model, app-native): `ib_characteristic` (the
  characteristic identity, keyed on meaning-in-context = lemma + normalised ESV), `ve_lexical` (the
  per-characteristic dimension values: `ve_nr · label · value · notes · provenance` + the pair
  columns `from_span · to_span · direction · resolution · pair_kind`), and `passage_read` (the
  holistic passage meaning + the D7 process + the read's provenance/model/version).
- **Config** (the reading rule-set, all in the cfg store): the **dimension catalogue** (the 18 dims,
  their shape, derivation rule, resolution states, mandatory-or-`none` flag), the **screens**
  (Screen-0 God-is-arena, role rules), the **output schema** the API must return, and the **API
  config** (model tier — the cheapest that passes validation, re-selectable; prompt template).
- **New operation** `read-passage` (runs over a passage): mechanical pre-fill → assemble payload →
  API read → validate (convergence / completeness / citation / provenance) → store; on validation
  failure, retry per config, else flag. Batch runner over all short passages, resumable, per-book.
- **Validation** extends the existing report: convergence rate (read vs mechanical), completeness
  (dims answered or `none`), provenance coverage, and drift band-tests per dimension.

---

## 8. The long passages (>10 verses) — held out, handled after

The 47 `needs_review` passages are **excluded from the general run** and processed in a **separate
pass afterward**, because they need special care (whole-passage reading with more context, and a
decision on whether a long run is truly one movement or several). Deferring them keeps the general
run clean and lets us tune the method on the ~17,777 normal passages first, then bring a proven
method to the hard cases.

---

## 9. Open decisions — please confirm

1. **Decompose + keep holistic, read-first** (recommended, §5) vs holistic-only vs grid-first
   decomposition. Recommend the first — it is the only option that gives analytics *and* survives
   the drift/bias/completeness tests without re-incurring the over-structuring failure.
2. **The dimension set** — adopt the old `ve_nr` catalogue (101–118 + process/genre/passage) as the
   target, with the §2 mechanical/hybrid/reading split. Confirm, or prune/extend the set.
3. **Mechanical layer computed and passed in as grounding + validation** (recommended, §3) vs let
   the API derive everything. Recommend computing it — free, exact, and it is the validation anchor.
4. **One coupled call per passage** (holistic + decomposition together) vs two calls (read, then
   decompose). Recommend one — the decomposition must be *of* that read, and it is cheaper.
5. **Long passages deferred** (recommended, §8). Confirm.
6. **Model tier** — start with the cheapest model that passes the validation gate, re-selectable via
   config. Confirm the "validation carries quality, tier is a setting" stance.

**On confirmation** I will write the plan into the app: the tables + the dimension-catalogue config +
the `read-passage` operation + the validation extension — built and tested on a few passages before
any corpus run. **Nothing touches the DB until you confirm.**

> **Note — API budget:** this phase *uses* the Claude API for the reading, and the research call for
> this very plan hit the account's **monthly spend limit**. Before the reading run, that limit needs
> raising (claude.ai → settings → usage). The base layer and all validation are local and unaffected.
