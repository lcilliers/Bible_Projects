# IBA foundation — what the process must PRODUCE, and where the foundation is wrong

> v1 · 2026-07-19 · written after the Romans inspection exposed that the app's "validations"
> test mechanics, not fitness, and that the passage foundation is built on the wrong unit.
> This is a **thinking / target** document — no build, no fix proposed. Its purpose is to state,
> from the study's endpoint backward, what each stage must produce and what "fit for purpose"
> means — so the target is agreed **before** any foundation is rebuilt. Grounded in
> `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md`, the RESET milestone, and the
> settled endpoint (memory `reference_study_end_point_and_milestones`). Every claim here is for the
> researcher to confirm or correct — the outcome and the unit are the researcher's to own.

---

## 1. The failure I own

- The IBA "validations" (`cfgcheck`, write-grants, seed-hash, schema build) test **mechanics** —
  is the config well-formed, may this writer write this table, did every candidate verse get a row.
  They **never test fitness**: is the characteristic set complete? is it clean? does a passage
  actually give the contextual focus needed to read a characteristic's movement? Presenting those
  green ticks as assurance was misleading — they assure structure, not suitability for the job.
- I worked **symptom-first** — inspect, find a defect, propose a patch ("extend the passage") —
  instead of **outcome-first**: what must this produce, and does the design allow it at all. The
  passage patch was a parameter tweak on a unit whose defining principle is wrong.

## 2. The outcome (worked backward from the study's endpoint)

- **Endpoint** (settled): an evidenced corpus = what Scripture says about the inner being, the
  substrate for narratives/products. **Post-RESET the object is not a list of characteristics but
  their _movements, associations, interlocking, and emergence_** — a process / relational web read
  off what each verse does.
- **Therefore the atomic unit of evidence is:** *in this context, characteristic C is doing /
  undergoing X, in relation to Y (another characteristic, a cause, an effect, an arena).*
- **So the foundation must deliver, for each characteristic occurrence:**
  1. that it is **correctly and completely identified** (seeding → characteristic);
  2. the **context over which its movement and its interrelationships are legible** (the unit);
  3. a **read of that movement and those relationships** off that context (lexical).

If any of the three is built on the wrong principle, the outcome is unreachable regardless of how
clean the code or config is.

## 3. The root error: the passage is built on the wrong unit

The study's **own method already worked out** what the right contextual unit is — and in every
book-type it is a **segment scoped to an inner-being movement**, never a mechanical verse-run:

| Book-type | Method's contextual unit | Source |
|---|---|---|
| poetic (Psalms) | chapter-driven (Phase-1 per verse → Phase-2 whole chapter) | method §14 |
| wisdom / discourse (Prov, Ecc, Job, Lam) | **segmentation into inner-being units** — "a run of verses that carries one inner-being movement (or several held together)" | method §15 |
| prophetic (Malachi) | **oracle** units, crossing chapter lines | method §15.1 |

- **Romans is an epistle — argument/discourse text.** Epistles were **never processed** under the
  new model. The method's §3 still files "epistle" under **prose = mechanical consecutive run** — an
  untested default that the later §15 / §15.1 discoveries (each book-type needed a movement-scoped
  unit, not a run) strongly suggest is **inadequate for discourse-shaped text**. Romans is arguably
  *more* discourse-shaped than the wisdom books that already forced segmentation.
- **The IBA `passage.build` is worse than even the mechanical run:** it groups only *consecutive
  candidate-bearing* verses and breaks the run whenever adjacent verses don't repeat the **same**
  base-Strong's. In Romans that shattered the text — 83% single-verse passages, 96% of them sitting
  next to a candidate verse whose context was thrown away (evidence: the v1 diagnosis doc).
- **Consequence:** "extend the passage by N verses" cannot fix this. The unit is defined by
  *lexical accident* (which verses carry a candidate; which repeat a word). It must be defined by
  *the movement* — the discourse segment over which a characteristic's behaviour and its
  interrelationships can actually be read. That is a different foundation, not a bigger window.

**The open methodology question (researcher's call):** is the right unit for Romans / epistles an
**inner-being movement segment** (the §15 `segment_unit` model — a run carrying one movement, or
several held together via the `multi` flag), scoped by the letter's argument structure, rather than
any mechanical run? My reading of the method's own trajectory says yes — but this is yours to settle,
because the whole foundation rests on it.

## 4. What each stage must PRODUCE (the target to build and to validate against)

Working backward from §2. For each stage: the product, and the **fitness test** that a real
validation would apply (contrast: what the app checks today).

### 4.1 Seeding
- **Product:** an honest, deliberately **over-inclusive but complete** draft of *where inner-being
  characteristics plausibly occur* — meaning-based and **independent of the registry**. Registry
  coverage is only a **completeness cross-check** (a candidate with no registry word = a registry
  gap to notice), never a source of candidacy.
- **Fitness test:** **completeness** (no genuine IB movement missing — e.g. thanksgiving / G2168–G2169,
  currently absent) **and independence** (no registry-imputed noise — currently 78% of the basis).
- **What the app checks instead:** that `candidate_seed` rows exist and are schema-valid. Says
  nothing about completeness or noise.

### 4.2 Characteristic identification (candidate → role → characteristic)
- **Product:** a **per-occurrence, meaning-in-context** decision — is this span, here, the
  characteristic itself, a **qualifier** of one, or a **standalone** — **confirmed by a sanity gate**,
  never imputed from the lemma (method §13: the mechanical draft is *not trusted* until read back
  and role-assigned; and [[feedback_characteristic_list_validates_not_imputes]]).
- **Fitness test:** each retained occurrence really is an IB characteristic *in that verse*; roles
  are correct per occurrence.
- **What the app checks instead:** nothing — there is no role/sanity gate in the IBA pipeline yet.

### 4.3 Contextual unit (the "passage", properly a movement segment)
- **Product:** for each characteristic movement, the **discourse-scoped span** over which that
  movement and its interrelationships are legible — one movement, or several held together —
  **genre/discourse-aware** (narrative = scene/episode; epistle = argument segment; poetry =
  strophe/chapter; prophetic = oracle).
- **Fitness test:** does the unit contain the movement's **arc** (trigger → operation → effect) and
  the **other characteristics it interlocks with**, *without* diluting the focus into unrelated
  material? A unit that cuts off a movement's cause or effect, or that isolates a single verse from
  its argument, **fails** — which is exactly what Romans shows today.
- **What the app checks instead:** verse-count and `needs_review` over a threshold. Structural only.

### 4.4 Lexical analysis
- **Product:** the movement read (the dimensions) **plus the interrelationships**, derived off the
  unit and grounded in it, stated-vs-inferred tagged.
- **Fitness test:** the read is anchored in the unit's text and captures movement **and** relations;
  it can only be as good as 4.1–4.3.

## 5. What "validated" must mean going forward

Replace mechanical gates with **fitness gates**, run as first-class steps, not afterthoughts:
- **completeness** of the characteristic set (against the text, not against the registry);
- **independence / cleanness** of the basis (no imputed noise);
- **per-occurrence role correctness** (the §13 sanity gate);
- **unit-carries-the-movement** (the arc + interrelations fall inside the unit).

Structural validators stay (they are necessary) but are never again reported as quality assurance.

## 6. What I am NOT doing

No fix, no build, no config change. This document is the **target**. Before touching the
foundation I need two confirmations, because both are yours to own and everything rests on them:

1. **The outcome** as stated in §2 — is that what the process must produce?
2. **The contextual unit** for Romans / epistles (§3) — is it an inner-being **movement segment**
   (discourse-scoped, §15-style), not a mechanical verse-run?

Once the target and the unit are agreed, the seeding and unit foundations get **redesigned to that
target** — and re-validated by the §4 fitness tests, not the mechanical ones. Correct me anywhere I
have misread the outcome; that correction is more valuable than any code I could write now.
