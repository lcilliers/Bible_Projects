# Lexical Analysis — RULES RESET (process/functional reframe) · v1 · 2026-06-24

> **This resets the framing of lexical analysis.** It supersedes the *taxonomic* framing of `01b-VE-field-reliability-and-rules` (Part A's part-list and Part C's object-type grid) and reframes how we arrive at each value. The **observable bedrock** of 01b (the measure layer, sense, mode) is retained and referenced. Rationale: `Workflow/methodology/inner-being-behavioural-science-discussion.md`.
>
> **Hand-in-glove pair:** this is the **decomposition** half. Its **assembly** half is `wa-synthesis-B-spec-reset-v1` — the two are designed together so the lexical produces exactly what synthesis consumes. **One requirement synthesis-B places on this dissection:** cause / effect / transition must be recorded in a **joinable** form (the node + its kind), not free text, so movements can be assembled across verses (the antecedent in one verse, the effect in another).

## 0. Why the reset

Six months of trying to bring the verses into **logical units** kept failing the same way — terms bleed across boundaries, the same word does different work in different verses, a grouping clean in one passage collapses in the next. That is not a failure of effort; it is **information about the subject**: the inner being does not decompose into clean parts. A part-sorting method applied to a non-part subject fails in exactly that boundaries-won't-hold way.

So the **"faculties / object-types / units"** lens was *miscalibrated* — those are the most part-committed frames there are; they presuppose the answer (discrete powers/bins) and ask the verses to fill boxes the text isn't filling. Biblical language (Hebrew especially) is **concrete, verbal, relational** — it shows the heart *doing*, rarely defines what the heart *is*.

**The shift (governing):** stop asking *"what part / category / faculty does this word name?"* and ask *"what does this word DO in the verse?"* — what brings it about, what it acts on, how it operates, what it produces, what it turns into, what it moves with. Record what the verse says, **from every angle**; let patterns emerge from that record rather than imposing a grid. (This is also the project's earliest insight returning: *meaning lives on the edges, not the nodes.*)

## 1. Governing principles

- **P1 — Observe, don't impose.** Record what the verse *states or implies*; never sort into a pre-decided category. Mechanical/deterministic where the measure layer allows; else a grounded read; else UNRESOLVED.
- **P2 — Original-language grounded.** Every signal is read off the lemma + morphology + co-occurring tagged terms — **never the English string** (the homograph error-class).
- **P3 — Functional-first.** The primary record is **what the word does** (its relations and movements, §3), not what it *is* (its category). Categories are outcomes (§6), never inputs.
- **P4 — Expectation test (3 states per consideration).** **resolved** = a value the verse gives · **NONE / silent** = the verse says nothing about it → never impute · **UNRESOLVED** = the verse signals a value is expected but it can't be settled → the read/research worklist. Silence ≠ UNRESOLVED.
- **P5 — Citation.** Every resolved value cites the measure/word/clause that forced it (back-traceable by construction).
- **P6 — Whole-verse unit.** The unit of (re)analysis is the verse (with its immediate context — a value may be sourced from an adjacent verse, cited as such).
- **P7 — Patterns emerge, held loosely.** Recurring functional shapes are *named when observed* (§6), revisable, never sealed.
- **P8 — Discovery-lookout is mandatory** (§5) — every analysis actively searches for what the current considerations do not capture.

## 2. The observable bedrock (retained from 01b §2)

For each verse, the **full-verse measure layer** (every word's Strong's + morph; lexicon gloss/medium_def; per-occurrence STEP sense; co-occurring tagged terms) — already persisted in `verse`/`verse_morphology`/`lexicon`. From it, the bedrock observations:
- **sense** — the per-occurrence sense the term carries here (mechanical floor = STEP subgloss).
- **mode** — the term's grammatical realisation (stem/voice/tense) — `morph_code`/`stem` columns.
These are observed, not interpreted; they anchor everything else.

## 3. The PRIMARY layer — the FUNCTIONAL / RELATIONAL considerations (what the word DOES)

Each consideration is an **observation of the verse**, arrived at as stated, with P4 states + P5 citation. This is the heart of the analysis — the verse's movement, captured from every angle.

| Consideration | The question (what we record) | How we arrive at it (the measure) |
|---|---|---|
| **antecedent / cause** | what **brings this about** | the causal clause (Hebrew *ki* / Greek *hoti/gar* + subject), or the object-of-perception preceding it |
| **operation / how** | **how it operates** — the governing predicate | the finite verb governing the term's span (lemma "gloss") |
| **object / target** | what it **acts on / toward** | the governed object by morph (accusative / construct / prepositional complement); record the object + what *kind* of object it is, **observed** (person/God/group/thing/abstract/spiritual-being) — a description of the object, not a bin for the term |
| **manner / intensity** | the **manner / how-much** | manner adverb / intensifier lemma modifying the term (e.g. freely, willingly, *me'od* "very") |
| **produces / effect** | what it **yields** (sustained result) | the result clause / consequence conjunction |
| **immediate response** | the **immediate reaction** | the coordinated/following finite verb after the term's clause |
| **transition / becomes** | what it **turns into / moves between** (its movement) | a verse (or adjacent verse) showing the state set, removed, reversed, or transformed; the trigger of the change |
| **relational web / binding** | what it **moves with** | the co-occurring tagged inner-being terms + the **relation** each holds to the head (partner · object · cause · manner · expresses · seat · pole-opposite) — read per verse |
| **direction** | **toward / from whom** | directional/relational morphology governing the term toward an object |

> These are the same "edges" the project always needed; the reset makes them **primary**. Most verses will be legitimately NONE on several (e.g. cause/effect) — that is expected (P4), not a gap.

## 4. The OBSERVABLE references (reframed from ontology to observation)

- **faculty/seat addressed** — *does the verse directly mention or address an inner-being faculty or seat, and which?* (heart · soul · spirit · mind · conscience · understanding · will · knowing · perceiving …). **Observation of presence** (a faculty/seat lemma or a faculty-operation verb is in the verse) — NOT a claim that the term *is* a faculty or that the inner being is *built of* faculties. P4 states. *(Replaces the retired intrinsic-faculty ontology.)*
- **valence / moral colour** — the moral register the verse gives the term, where stated/mechanical (term-inherent moral lemmas; prohibition particles); else routed to the read; else NONE. *(Valence is a property the verse may give; not a bin.)*

## 5. The DISCOVERY-LOOKOUT (mandatory per verse) — the emergence engine

After recording §2–§4, every analysis MUST run the **lookout**:

> **"What does this verse state or imply about the inner being that the current considerations do NOT capture?"**

- Look for: a movement, relation, cause, effect, condition, or nuance the schema has **no consideration for**; something **implied** (in the term, the clause, the adjacent context) but unrecorded; anything noteworthy about how the inner being works here that would otherwise be lost.
- **Surface each as a DISCOVERY-FLAG** — recorded (a) as a `lexical_note` typed `discovery` on the verse, and (b) in the **lexical-discovery register** (`outputs/markdown/validation/wa-lexical-discovery-register-*`), with: the verse, what was noticed, why the current considerations miss it, and a proposed consideration-name.
- **Triage + propagation:** a flag that **recurs / is adopted** becomes a **new consideration** in §3/§4 — and is then **applied to ALL verses** (back-propagation: prior verses are re-examined for it; the re-derive is idempotent). *This is how the schema grows from the material rather than from a fixed upfront grid — directive (b).*
- The lookout is **a standing field of every analysis**, not optional. A verse with nothing to flag records "discovery: none" (so we know it was looked for, not skipped).

## 6. Patterns emerge — NOT categories imposed (synthesis, post-hoc)

"States" and "characteristics" are **not inputs**. They are **recurring functional patterns** that surface *from* the §3 record — *attractors*: a cause→operation→effect shape (or a stable condition) that repeats across many verses. They are:
- **named only when observed** (the data shows the recurrence), held loosely, revisable;
- allowed to **shade into one another** (no sealed boundaries) — the text often lets them;
- never the grid we start from. The old object-types (characteristic / state / expression / identity / qualifier / bivalent) may **re-appear here as observed patterns** — but only if the functional record earns them, and they carry no authority as pre-set bins.

## 7. Carried-forward mechanics (unchanged)

- Storage: per-verse considerations in `ve_lexical`; the emergent patterns + cross-verse considerations at term/collection scope (regenerable). Researcher notes preserved.
- Re-run: mechanical considerations regenerate idempotently (a non-reproducible mechanical value = a leak to fix); read/researcher considerations are preserved; a schema growth (§5) is a versioned re-derive-with-diff across all verses.
- The narration view composes the resolved considerations into a templated, back-traceable sentence (deterministic view, not authored prose).

## 8. What changed from 01b (summary)

- **Retired as framing:** the object-type grid (Part C) and the intrinsic-faculty field, the "type=characteristic/state" bins, "logical units" as the organising move. (Retained as *possible emergent patterns*, §6.)
- **Promoted to primary:** the functional/relational considerations (§3) — cause/operation/object/manner/effect/response/transition/web/direction.
- **Reframed:** faculty → "does the verse address a faculty/seat" (observation, §4).
- **Added:** the mandatory **discovery-lookout** (§5) — the engine that lets the record grow from the verses.

*Reset — analyse what the verse DOES, from every angle; record it observably; let patterns emerge; and on every verse, look out for what we don't yet capture and feed it back. The parts→process pivot, made into method.*
