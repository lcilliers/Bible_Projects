# Plan (v2): the IBA application — building the growing **Inner-Being Concordance**

> **Status: DESIGN FOR CONFIRMATION. Authoritative construction guide once approved. No DB
> changes / no build until confirmed.** Directed 2026-07-20.
>
> **What this is.** The rewritten, authoritative build plan for the IBA application. It **supersedes**
> `iba-application-plan-v1-20260715.md` as the top-level guide, folding in the shift the researcher
> set on 2026-07-19–20 (`outputs/markdown/reading-unit-method-characteristic-cluster-v2.md` — the
> growing Inner-Being Concordance, **including its open questions**) and the unit critique
> (`iba/app/docs/iba-foundation-outcome-and-unit-position-v1-20260719.md`). v1's architecture
> (PowerShell framework → Python core → DB configurator → layered DB → gated runs) is **kept and
> restated**; what changes is the **endpoint, the output layer, and the reading unit**. Where v1's
> appendices (A configurator, B schema, C content inventory) are unchanged they are **carried by
> reference**, not reproduced.
>
> **Provenance of supersession.** This document supersedes: v1's endpoint framing (§1.1 "findings
> corpus" → *the concordance*); the base-processes passage unit
> (`base-processes-plan-v1-20260718.md` §2.2 mechanical run → *movement segment*, §11 here); and the
> lexical-phase storage model (`lexical-phase-plan-v1-20260719.md` §7 → *the concordance layer*,
> §6 here). Those documents remain valid for the parts not changed and are cited throughout.

---

## 0. The decisions folded in (read first)

The attached v2 concordance doc left five open questions, and the foundation doc left the unit
question. This plan **takes a position on each** so construction has one target; every one is the
researcher's to overturn — that correction is more valuable than the code.

| # | Question | Researcher's answer (2026-07-20) | Where |
|---|---|---|---|
| Q1 | Grain / shape of the output | **Not one concordance — a spiderweb** of distinct things: evidence · three concordances (IB · other-beings · body) · lexical · index. Grain = a *distinct observation of a characteristic in operation*, cross-referenced not duplicated | §13.1 |
| Q2 | Fresh-vs-prior on re-read | **Observe the verse context first, then reconcile against prior** — and **recording ≠ reconciling** (two separate actions, with defined rules / surfacing / repair) | §13.4 |
| Q3 | Lexical deliverable depth | **Every reference verse/passage has a lexical** (several verses may share one if they belong together); it encapsulates the lexicon dimensions that apply to the verse's meaning | §13.1 |
| Q4 | Who runs consolidation | **Agree — LLM proposes, researcher reviews**; the reconciliation output must surface the changes + related data so the *next* reconciliation can review them | §13.4 |
| Q5 | First scope / next steps | **John 1 to test**; next = the operation build-out list | §13.6 |
| U | The reading unit | **Varies by operation**: chapter for prepare-read → candidate list; Strong(s) for analyse; the passage is an *output*; resumable; multi-phase | §13.3 |

> **Governing note (2026-07-20).** The answers above are consolidated in **§13**, which reflects the
> researcher's actual direction from discussion. **§§2–12 are the first-pass reasoning; where §13
> differs, §13 governs** — and the guts (§§4–8: the loop, the unit, the schema) are **reworked once
> *the process* is nailed** (the immediate next discussion). §13 is the current trace of where we head.

---

## 1. The shift — from a findings corpus to a growing concordance

### 1.1 The endpoint, restated

**The study's output is one integrated, progressively-growing concordance of the Bible on the inner
being.** Not a pile of per-verse findings, not prose essays as the primary artefact — a **concordance**:
one entry per inner-being characteristic (at the grain of *meaning-in-context*), each entry
accumulating everything the study has learned about that characteristic and taken further with every
chapter read. Essays, study guides, and books are **drawn from** the concordance; they are products,
not the corpus. *(This sharpens v1 §1.1's "materially-evidenced findings corpus" into a definite
object — the thing every earlier reset was circling but never named. Source: the attached v2 doc §"What
the concordance is"; RESET milestone: the object is movements/associations/emergence, not a list.)*

The concordance honours the study's five stated principles (attached doc §"The principles"): progressive
learning not stereotyping; learning persists (corrections carried forward, not lost in chat); a home that
**grows**; prior findings **visible on re-read**; lexical analysis **retained** as a deliverable.

### 1.2 The operating model (the researcher's framing, made structural)

Four statements govern the whole build. They are not aspirational — each becomes an enforced property
of the application.

1. **The study uses the app.** The researcher does not touch the data by hand, by chat, or by ad-hoc
   script. The app is the instrument.
2. **The body of knowledge lives in the IBA DB.** The concordance — every entry, occurrence, finding,
   lexical value, relation — is in `iba/app/db/iba.db`. If it is not in the DB it does not exist
   (v1 §3.4). No parallel documents, no model memory, no chat transcript as a store.
3. **Interaction with the body of knowledge is *only* through the app.** Reading the concordance,
   querying it, growing it, correcting it, consolidating it, producing a product from it — **every one
   is an app operation.** There is no back door. This is what makes the knowledge trustworthy: every
   change and every read is mediated, logged, and rule-governed.
4. **Every knowledge operation is a *run* (an operation unit):** orchestrated in **PowerShell**,
   with the **core logic in Python**, and **all rules, settings, and variables in config** (the
   `cfg_*` store, DB-authoritative). A run is scoped, gated, tracked, resumable, and replayable
   (v1 §2.1, §2.2, §3.2). Nothing the code "decides" is in the code; it is a config row.

**Consequence for the plan:** the application is not "a pipeline that fills a database." It is **the
sole interface to a growing body of knowledge**, and the concordance is that body. Every module in
v1's pipeline is re-read in this light: it is an *operation on the concordance* (build its substrate,
grow it, validate it, consolidate it, or read from it).

### 1.3 What was already right, and is kept

v1 got the **machine** right, and it stands unchanged:

- **PowerShell orchestrates; Python works; config decides** — proven in the raw slice
  (`iba/app/GOVERNANCE.md`: one run = 1,041 config reads; `may_source` enforced; behaviour changes
  by editing a DB row, no code touched).
- **The layered DB with immutable raw + provenance + replayable writes** (v1 §3.4).
- **The configurator as the DB-resident rulebook** (v1 Appendix A) — the encoded rules that stop the
  model "doing its own thing."
- **Deterministic gates carry quality; the API is used only for genuine inference; the cheapest model
  that passes the gate, re-selectable** (v1 §2.5, §3.7).
- **The base layer already built** — 178 words, 534k spans, 29k verses, candidate seed, the raw slice
  proven (`iba/app/BUILD.md`).

The shift is **not** a re-architecture. It is: name the endpoint (the concordance), build the missing
output layer that holds it, and fix the one foundation that is on the wrong unit.

---

## 2. What the concordance IS — the output object

**One entry per meaning-in-context.** An entry is keyed on a characteristic *as it means in context*
(e.g. *perception/knowing that opens onto trust*), **not** on a registry word and **not** on a Strong's
number (§3 explains why the Strong's cannot be the key). Each entry accumulates **five facets** (attached
doc §"What the concordance is"):

| Facet | Holds | Grows by | DB home (Layer 3, §6) |
|---|---|---|---|
| **Working definition** | the characteristic's sense as currently understood; status *emerging / established / under-revision* | revised as evidence accrues | `ib_entry` (current) + `ib_entry_revision` (trail) |
| **Occurrences** | every verse + span where it was read — a true concordance list | one row per reading | `ib_occurrence` |
| **Findings** | observations of what it *does* — movements, associations, seats, expressions, tensions | appended; **adjustments are new revisions, never overwrites** | `ib_finding` + `ib_finding_revision` |
| **Lexical profile** | the lemmas / Strong's / senses / morphology that realise it, with glosses + the `ve_nr` dimension values (§4, Q3) | folded in per unit read | `ve_lexical` (per-occurrence) + a rolled-up profile view |
| **Relations** | edges to other characteristics — co-occurs / welds / triggers / opposes | one per observed pairing | `ib_relation` |

**Persistence of learning** lives in *Definition* + *Findings*: a correction is a **revision record**
that supersedes but never erases its predecessor, so the reasoning trail survives and the current view
is always the latest revision (attached doc; and the study's "all-findings-are-drafts / baseline-then-delta"
discipline, v1 C.10). This directly answers failure-cause *"learning lost in chat"* (v1 §1.2).

---

## 3. The three-layer identity model — how Strong's ↔ sense is dissolved

The hard problem the researcher named: **many Strong's flow into each other** (`strong_meaning_tree`
proves it runs both ways — one Strong bundles many senses; many Strongs collapse to one sense). So a
Strong's number **can never be the unit of identity**. The resolution (attached doc §"The Strong↔sense
flow") is a three-layer model, and it is also the data model of Layer 3:

1. **Occurrence (facts).** Each read span → `(verse, Strong, morph, lexicon-sense-code,
   meaning-in-context judged from the verse)`. The Strong is *one attribute* of an occurrence, never its
   key. — table `ib_occurrence`.
2. **Entry (identity = meaning-in-context).** An entry gathers occurrences that share a
   meaning-in-context. It therefore links to **many Strongs** (as evidence) and any one Strong appears in
   **many entries** — a clean many-to-many *mediated by the occurrence layer*, with **no forced partition
   of Strongs**. — table `ib_entry`, linked via `ib_occurrence`.
3. **Neighbourhood (soft edges).** Entries connect to *adjacent* entries by **"flows-into / borders"**
   edges — a graph, not a merge (`perceive-recognise` borders `perceive-understand` borders
   `discernment`). — table `ib_neighbour` (distinct from `ib_relation`, which is characteristic↔characteristic
   *in a verse*; `ib_neighbour` is entry↔entry *sense-adjacency*).

**Why this dissolves the unknown:** "many Strongs flow into each other" is only a problem if a Strong
defines a boundary. Here it never does — identity is the meaning-in-context, *evidenced by (not defined
by)* Strongs, and the flow itself is recorded as a border edge rather than forcing a decision.
`strong_meaning_tree` (already in the DB, already fanning a Strong into senses and already showing
cross-Strong sense-sharing) becomes the **scaffold that proposes the initial neighbourhood graph** — a
Layer-2 input to seeding, never the authority over meaning-in-context.

---

## 4. The reading loop (v2) — the interpretive run

The unit of interpretive work is **one contextual unit** (§5) read for the characteristics it turns on.
The loop below is the `read-unit` operation — a run (PS-orchestrated, Python core, config-governed). It
merges the attached doc's five-step loop with the lexical-phase-plan's mechanical-floor-plus-API design.

```
run: read-unit(unit)                                   [one API call per unit; genre-routed by config]
  0. ASSEMBLE (deterministic).  the unit's verses in order; each span (surface·Strong·gloss·morph);
     the PRE-COMPUTED mechanical dimensions (§6, the free/exact morphology floor); candidate stamps;
     and the RULES from config (dimension catalogue, screens, output schema, provenance requirement).
  1. LOAD (deterministic).  for each characteristic the unit's candidates point at, load its concordance
     ENTRY summary — definition, prior findings, lexis, relations.  ── held BACK from the read (Q2).
  2. READ FRESH (API).  the unit is read whole for its own witness — find the gems; the prior entry must
     NOT pre-decide what the text says.  Screen-0 runs here (human inner being = subject; God = arena);
     role assignment runs here (characteristic / qualifier / standalone / uncertain).
  3. RECONCILE (API, same call).  the fresh read is set against each loaded entry: confirm / extend /
     adjust / contradict — each becomes a FINDING (adjustments as revisions).  THIS is where prior
     knowledge enters — as the thing the fresh read confirms or revises, never as the read's input.
  4. LEXICAL (API, same call).  the unit's characteristics decomposed into the ve_nr dimensions (Q3):
     each value self-interpretable, citing the text, STATED-vs-INFERRED, value-or-explicit-`none`
     (silence is a finding, never a blank).
  5. VALIDATE + WRITE BACK (deterministic).  convergence against the mechanical floor; completeness
     (every mandatory dim present or `none`); citation + provenance present; then match-on-write (§7)
     and persist: occurrences, findings (revisioned), lexical profile, relations.  The entry is richer.
```

**Steps 2–4 are one coupled API call** (Q4 in the lexical-phase-plan, confirmed): the decomposition must
be *of* that read, and one call is cheaper and self-consistent. **Step-2-before-1-informs-2** is the guard
that resolves "read each chapter as if the first" with "prior findings visible on re-read": the *text* is
read fresh; the *concordance* enters only at RECONCILE (§0 Q2).

**Why the mechanical floor at all** (the researcher's earlier question, answered in the lexical-phase-plan
§3, kept): it is free and exact (morphology is already parsed); it **grounds** the read (passed into the
prompt, so the model reads meaning on a known grammatical skeleton, not guessed grammar — the single
biggest hallucination reducer); and it **validates** the read (a read asserting what the morphology
contradicts is a flag, not a silent accept). The mechanical/hybrid/reading split of the ~18 dimensions is
in the lexical-phase-plan §2 and becomes config (§6).

---

## 5. The contextual unit — the movement segment (settling the foundation question)

The foundation doc's finding stands: **the mechanical candidate-run passage is built on the wrong
principle.** It groups only consecutive candidate-bearing verses and breaks whenever adjacent verses
don't repeat the same base-Strong — in Romans that shattered the text (83% single-verse passages, 96% of
them next to a candidate verse whose context was thrown away). A characteristic's *movement* (trigger →
operation → effect) and its *interrelations* cannot be read off a unit defined by lexical accident.

**Decision (U):** the reading unit is the **inner-being movement segment** — the discourse-scoped span
over which one movement (or several held together) and its interlocking characteristics are legible.
This is what the study's own method already worked out for every book-type (foundation doc §3):

| Book-type | Unit | Config route |
|---|---|---|
| narrative | scene / episode | `segment:narrative` |
| poetic (Psalms) | chapter-driven (Phase-1 per-verse → Phase-2 whole chapter) | `segment:poetic-two-phase` |
| wisdom / discourse (Prov, Ecc, Job, Lam) | inner-being unit — a run carrying one movement (or several via `multi`) | `segment:discourse` |
| prophetic (Malachi) | oracle, crossing chapter lines | `segment:oracle` |
| **epistle (Romans)** | **argument segment** — the letter's argument structure, *not* a mechanical run | `segment:argument` (new) |

**Fitness test for a unit** (replaces v1/base-plan's verse-count check): does the unit contain the
movement's **arc** (trigger → operation → effect) and the **other characteristics it interlocks with**,
*without* diluting focus into unrelated material? A unit that cuts off a movement's cause or effect, or
isolates a verse from its argument, **fails**. Structural checks (verse-count, `needs_review`) stay but
are never again reported as quality assurance (foundation doc §4.3, §5).

**Build consequence:** the base-processes `passage.build` (`base-processes-plan-v1` §2.2) is **revised**,
not merely re-parameterised. The candidate stamp still marks *where* to look (it is a good over-inclusive
filter); but the segment boundary is set by **discourse structure**, genre-routed by config, with the
long-run review control kept. Poetry/oracle already use whole-unit rules and are least affected; narrative
and epistle need the segment logic. *(This is the one place the existing base layer must change; the raw
and candidate layers are untouched.)*

---

## 6. The data model — five layers, the concordance at the centre

v1's four data layers (§3.4) become **five**, by naming the concordance as its own layer. Raw and Base
are unchanged; the old "Interpretation" layer is **reorganised as the concordance** (keyed by
meaning-in-context, not scattered per-verse rows); Prose becomes *Products*, drawn from the concordance.

```
Layer 1  RAW        immutable, from STEP            verse · verse_morphology · lexicon · strong* · strong_meaning_tree
Layer 2  BASE        deterministic substrate         span · span_candidate · candidate_seed · lemma_inventory · stem_master
                     + the CONTEXTUAL UNIT (§5)      segment (was: passage) · verse_segment · segment membership
Layer 3  CONCORDANCE the growing body of knowledge   ib_entry (+revision) · ib_occurrence · ib_finding (+revision)
         (the output) meaning-in-context identity     · ve_lexical (per-occurrence dims) · ib_relation · ib_neighbour
Layer 4  PRODUCTS    derived, human-facing           narratives · study guides · exports — regenerable, never a source
—        CONFIG      cfg_* (Appendix A, v1)          rules · settings · dependencies · the dimension catalogue
—        CONTROL     app_* (v1 §3.5)                 runs · steps · checkpoints · worklist · validation_result · consolidation queue
```

**Layer 3 tables (the new build) — mapped straight from §2–§3:**

- **`ib_entry`** — one row per meaning-in-context characteristic: `char_key` (base-lemma + normalised
  gloss/ESV, the meaning-in-context key), current `definition`, `status` (emerging/established/under-revision),
  `registry_word` (nullable link — the double-control: an entry with no registry word = a registry gap).
- **`ib_entry_revision`** — the definition trail (supersede, never overwrite).
- **`ib_occurrence`** — the fact layer (§3.1): `entry_id · verse_id · span_id · strong · morph ·
  lexicon_sense_code · meaning_in_context · read_run_id · provenance`. **This is the many-to-many pivot**
  between entries and Strongs.
- **`ib_finding`** + **`ib_finding_revision`** — observations of what the characteristic *does*;
  `finding_type` (movement/association/seat/expression/tension), `stated_or_inferred`, citation,
  `supersedes` (the revision trail).
- **`ve_lexical`** — the per-occurrence dimension values (the lexical-phase-plan §7 shape, app-native):
  `ve_nr · label · value · notes · provenance` + pair columns `from_span · to_span · direction ·
  resolution · pair_kind`. The *lexical-profile facet* is a rollup view over these per entry (Q3).
- **`ib_relation`** — characteristic↔characteristic edges observed *in a unit* (co-occurs/welds/triggers/opposes).
- **`ib_neighbour`** — entry↔entry sense-adjacency (the soft "flows-into/borders" graph, §3.3), seeded from
  `strong_meaning_tree`, grown by consolidation.

**Principles carried from v1 §3.4.2 (unchanged):** one authoritative home per fact; raw immutable;
provenance on every derived row (source·method·run·version + STATED/INFERRED); real FKs with the span-id
as the join key; config and control first-class; **every write a replayable patch** (the DB-loss lesson);
no analytical values stamped on mechanical tables.

**The lexical deliverable is not lost or lightened (Q3):** the full `ve_nr` dimensions are stored per
occurrence in `ve_lexical` *and* rolled into the entry's lexical-profile facet. Decomposition is what
makes the corpus queryable and drift-checkable (lexical-phase-plan §5); the holistic unit read (the D7
process) is kept alongside as the human-readable record the decomposition is derived from and checked
against.

---

## 7. Consolidation — no near-duplicates (and how legacy findings collate in)

Fine grain (meaning-in-context) *will* generate near-duplicate entries. The discipline (attached doc
§"Consolidation"), applied on **every write, including migrating legacy findings in**, is itself a run:

1. **Match on write (deterministic).** Fingerprint the proposed entry — registry word + Strong set +
   lexicon sense-codes + gloss terms — and search existing entries; surface near-matches. Runs inside
   `read-unit` step 5 and inside migration.
2. **A *considered* decision, never silent (Q4).** **Auto-attach** only on an *exact* fingerprint match
   (same key). Everything else — **merge** two entries, or **keep-distinct + neighbour-link** — is a
   **considered** decision: an **LLM judge proposes**, and the **researcher approves the non-obvious**
   via a `consolidation_queue` in Layer Control. Nothing merges on a guess.
3. **Merge =** union of occurrences / lexis / relations; findings combined with the revision trail; the
   losing entry becomes an **alias / redirect** (never deleted — old citations still resolve).
4. **"Keep-distinct + neighbour-link" is the release valve.** When two senses are close but you're not
   ready to decide, record an `ib_neighbour` edge instead of forcing the call — then revisit. *You never
   have to decide boundaries up front; you record adjacency and consolidate later.*
5. **Periodic consolidation pass (run).** `consolidate` sweeps tight neighbourhoods; the LLM judge
   proposes merges/links; the researcher approves. Continuous, not one-time — this is where progressive
   learning tightens the concordance.

**The key insight (attached doc):** de-duplication and the Strong-flow are the **same mechanism** —
identity-as-meaning-in-context + soft neighbour edges + a considered merge/attach/link decision + periodic
consolidation. The structure lets boundaries stay provisional and improve, which is exactly the
"no-forced-structure / patterns-emerge" guardrail (v1 C.9) made operational.

---

## 8. Build sequence — simple steps, John first

Held to *simple incremental steps, rigour in the verification* (not a machinery-heavy design). Each step
is built, run on John, and shown before the next. **Nothing touches the DB until the target here is
confirmed.**

- **Step 0 — confirm this plan** (the target, the unit U, the five Q-decisions). One correction here is
  worth more than any code.
- **Step 1 — Layer 3 schema.** Add the `ib_entry (+revision) · ib_occurrence · ib_finding (+revision) ·
  ve_lexical · ib_relation · ib_neighbour` tables via the config path (schema in `cfg_*`, `db --reset`).
  Seed `ib_neighbour` from `strong_meaning_tree`. No reads yet.
- **Step 2 — the movement-unit for John (§5).** Add the `segment` route for narrative + argument; build
  John's units; verify against the fitness test (arc + interlocks inside the unit), not verse-count.
- **Step 3 — the dimension catalogue + screens in config.** The `ve_nr` 101–118 rules, the mechanical/
  hybrid/reading split (lexical-phase-plan §2), Screen-0, role rules, the output schema — all `cfg_*`.
- **Step 4 — the `read-unit` run (§4)** on John 1: mechanical floor → assemble → one API call → validate →
  match-on-write → persist. Prove the loop end to end on one chapter; inspect the entries produced.
- **Step 5 — grow + reconcile (§4 RECONCILE)** on John 3: prove that reading a second chapter *loads,
  reconciles, and grows* the same entries (definition revised, findings appended, lexis folded, relations
  added) — the whole point.
- **Step 6 — consolidation (§7)** across John 1–3: match-on-write + the `consolidate` run + the
  researcher-approval queue. Prove near-duplicates are caught and the neighbour graph forms.
- **Step 7 — read-back / validation gates.** Convergence, completeness, citation/provenance,
  and the fitness gates (completeness of the char set; independence of the seed; per-occurrence role
  correctness; unit-carries-the-movement — foundation doc §5). Only now is John "done = validity."
- **Step 8 — sustainability go/no-go** (v1 §2.3.4) on the John result *before* any corpus run. Then, and
  only then, roll the proven loop across books.

**Long units (>N verses) are deferred** to a separate pass after the general run is tuned
(lexical-phase-plan §8), kept for the John test as the special case.

---

## 9. The runs (operation units) and the interface

Every operation on the body of knowledge is a run in `run.json`/`cfg_step`, PS-entry + Python-handler +
config-governed (v1 §3.3.1). The set, re-read as *concordance operations*:

| run | layer | grows/reads | notes |
|---|---|---|---|
| `set-candidates` / `build-segments` | Base | substrate | base-processes-plan, **segment revised per §5** |
| `read-unit` | Concordance | **grows** | the reading loop §4 — the core interpretive run |
| `consolidate` | Concordance | **tightens** | §7; the researcher-approval queue |
| `validate` | all | reads | the gate battery + scoreboard (v1 §3.7); dual-role pre/post gate |
| `query` / `concordance` | Concordance | **reads** | the read interface to the body of knowledge — entry lookup, cross-book/characteristic queries, "show me *fear* from source to target across the prophets" |
| `produce` | Products | reads | narratives/guides drawn *from* the concordance (Layer 4) |
| `migrate` | all | one-off | old-DB clean data in (v1 §3.4.1); legacy findings collate in **via §7** |

Principle (v1 §3.3.1): the interface only *expresses intent*; **what happens is decided by config.** The
`query`/`concordance` run is the structural realisation of "interaction with the body of knowledge is only
through the app" — even *reading* the concordance is a gated, logged, config-governed operation, not a raw
SQL poke.

---

## 10. What this fixes (traceable to the failure record)

Each folds a named failure cause (v1 §1.2) into a structural fix:

- *Learning lost in chat* → the concordance persists it; corrections are revisions with a trail (§2).
- *Method instability / over-structuring* → identity-as-meaning-in-context + soft edges + defer-the-boundary
  (§3, §7): boundaries stay provisional by design, so a reset does not shatter prior work.
- *Ungrounded frames read as findings (eisegesis)* → read-fresh-then-reconcile + STATED/INFERRED + cite-the-text
  + the mechanical convergence floor (§4).
- *Extraction mistaken for inference* → the API reads only meaning; grammar is the deterministic floor,
  not an API guess (§4).
- *Completeness checked, not validity* → the fitness gates (§8 Step 7), not verse-count.
- *Rules in the model's memory* → every rule a `cfg_*` row (§1.2.4), proven enforceable (GOVERNANCE.md).
- *The wrong unit* → the movement segment (§5).
- *Chat loop / DB fragility* → runs are autonomous, gated, resumable, replayable (§1.2.4; v1 §3.5).

---

## 11. Open items carried forward (not decided here)

- **Segment logic for epistle/narrative** — §5 sets the *principle* (argument/scene segment); the exact
  boundary heuristics (how the argument structure is detected — cue words? the API proposing segment
  breaks? a supplied outline?) are a Step-2 design pass on John.
- **The `ib_entry` key normalisation** — base-lemma + normalised ESV is the grain (Q1); the exact
  normalisation (casing, stemming, gloss-term set) is fixed empirically in Step 4 against real
  near-duplicates.
- **Migration of legacy findings** — the old DB's `ib_characteristic`/`ve_lexical` collate in through §7's
  consolidation (match/merge/link), not a blind copy; the mapping pass is scheduled after the John proof.
- **Product layer (Layer 4)** — narratives/guides drawn from the concordance are real but out of the first
  build's scope; flagged so they are not forgotten (v1 §3.6).
- **API budget** — the reading run uses the Claude API; the account hit its monthly limit producing prior
  research (lexical-phase-plan note). Raise the limit before the corpus run; the John proof is small and
  affordable.

---

## 12. What I need from you (Step 0)

1. **The endpoint (§1.1)** — is *one integrated, growing concordance of the Bible on the inner being* the
   right statement of what the study produces?
2. **The operating model (§1.2)** — knowledge in the DB, interaction only through the app, every operation
   a PS+Python+config run: confirmed as the governing model?
3. **The unit (§5, U)** — the inner-being **movement segment** (genre/discourse-aware), superseding the
   mechanical candidate-run passage?
4. **The five Q-decisions (§0)** — read-fresh-then-reconcile (Q2), full dimensions in the profile (Q3),
   LLM-proposes/researcher-approves consolidation (Q4), John-first (Q5). Overturn any.

On confirmation this document becomes the authoritative construction guide; `iba-application-plan-v1`
is archived as provenance, and Step 1 (the Layer-3 schema) is the first build — on John, nothing corpus-wide.

---

## 13. Where we are heading — consolidation (2026-07-20)

> This section captures the direction that emerged in discussion on 2026-07-20 and **governs where it
> differs from §§2–12** (the first-pass reasoning). It is deliberately kept at the level of *direction*,
> not schema — **the concordance schema is not settled and will not be until the process is nailed.**
> The immediate next discussion is **the process** (§13.2); everything else follows from it.
>
> **★ Advanced by §14 (2026-07-20, later same day).** The process discussion §13.2 called for has now
> happened: the researcher's own working-through of the loop is consolidated in **§14**, which is the
> current authoritative trace of the process and **governs §13 where it differs**. §14 settles the
> entry-point model (study units), the completeness definition, the bulk-vs-local split, and names the
> two new core tables (`operation`, `meaning`). Config-rule extraction is the next focus.

### 13.1 The output is a spiderweb, not one concordance

What the study produces is not a single concordance but a set of **distinct, linked things** on different
layers:

- **Evidence (built).** *Strong occurrence in verses* — the span/Strong table. The raw grid.
- **The core study act.** Decide whether a Strong, **in context**, is inner-being or not — an
  **inclusion decision**. The IB concordance is essentially the span table with the non-IB elements
  removed, plus what each retained Strong-in-context *does*.
- **Three concordances** (parallel bodies):
  1. **IB characteristics** in operation;
  2. **Other beings** in operation with the IB — God, Jesus, Holy Spirit, Satan, other spirits, angels,
     objects (idols) — read **from the other being's perspective toward the inner being**;
  3. **The human physical body** in operation with the IB — hands, eyes, feet, etc. and their
     interaction with the inner being.
- **The lexical layer.** Every reference verse/passage carries a **lexical** — its decomposition into a
  preset set of lexicon **dimensions**, grounded at the **original-language** level (several verses may
  share one lexical when they belong together).
- **A searchable index (still very undefined).** A groupable **view** over the concordances — by
  strong-family, by strongs-working-together, by operation-type, etc. It *emerges* from the data; it is
  not designed up front.

**The grain.** A grain is a **distinct observation of a characteristic in operation** (not merely what it
*is*), evidenced by a verse/passage, **anchored on the main verse** with the passage reference, and
**cross-referenced, never duplicated** across verses. Each grain links to: its verse, other verses of
similar meaning, the other characteristics it relates to, and its lexical decomposition.

### 13.2 The process is the real discovery — locality over bulk *(the next discussion)*

The genuine redefinition of the past day is **not the output but the process** — *how we read / digest /
augment / refine* — which has been the study's **most elusive part**. The shift:

> **Away from bulk-update** — decide one rule, sweep it across everything —
> **toward locality** — start somewhere, build the output deeply for a **specific unit**, then
> **back-fill / augment** work already done in the same area as you return to it.

Why this is the crux: bulk-update is the **most-repeated failure** in the study's own record (the method
rebuilt 4–5 times, each global sweep discarding what the last learned). The growing concordance exists
**precisely to make augment-in-place possible** — its revisions, cross-refs, neighbour edges and
reconciliation trail are all the machinery a bulk sweep never needed and never had. **The output
structure and the process are one idea.** Nailing this loop is the immediate next task.

### 13.3 The reading unit varies by operation

There is no single "unit". It depends on the operation:

- **`prepare-for-read`** — unit = **a book chapter** → output = a **list of candidate characteristics**
  to focus on.
- **`analyse-characteristic`** — unit = **a Strong (or list of Strongs)** within the chapter, over its
  **operating passage** (the adjacent verses where it operates — itself an *output*, anchored on the main
  verse). **Resumable per characteristic** (not all in a chapter are done together — "get back where I
  left off" must be designed). **Multi-phase:** prepare-lexicon → assemble-meaning → reconcile (and
  possibly others).

The chapter frames **screening**; the passage frames the **deep read** — which honours the standing rule
*read by passage, never a whole chapter at once*.

### 13.4 Recording ≠ reconciling (two separate actions)

Recording an observation and reconciling it against prior findings are **distinct operations**. The rule:
**observe the verse context first, then** reconcile against related prior findings. Reconciliation needs
its own **defined rules**, a way to **surface** the changes, and a **repair** process — and it must emit a
**reviewable output** (the changes + their related data) so the *next* reconciliation can see what the
last one did.

### 13.5 The operating model binds Claude Code too

§1.2 applies to **CC as well**: interaction with the body of knowledge is **only through the app's
operations** — no direct SQL reads/writes to `iba.db` outside a defined operation, by the researcher *or*
by CC.

### 13.6 Next steps (researcher)

1. **Build the individual app operations.**
2. **Repurpose the current passages table** for the concordance's purpose; remove redundant records;
   expect it to be built **progressively, as work starts on a chapter** (not pre-computed corpus-wide).
3. **Package the operations** so the researcher runs them as part of the study; **build the rules + config
   files.**
4. **Design how the researcher interacts with the DB** to make their own observations, modify existing
   ones, etc.
5. **Test the new process** (John 1 is fine).
6. **Build an operation that reaches into the old database** and scrapes all existing observations and
   findings **for the characteristic in focus**.

### 13.7 Still open (deferred until the process is settled)

- **The process loop itself** (§13.2) — the next discussion; everything below waits on it.
- **The concordance schema** — held open (per §2 note); shaped by the process, not before it.
- **The three-bodies structure** — parallel entry-types in one concordance vs separate sub-concordances.
- **The reconciliation output** shape (§13.4).
- **The searchable index** (§13.1) — undefined by intent.

### 13.8 considerations for naming the output collectively

The study is building and encyplopedia of the inner being as described by the bible

next is a bit of research to substantiate this as a good description of the work.

**Etymology**

From the Greek phrase *ἐγκύκλιος παιδεία* (*enkyklios paideia*) — "the circle of learning" or "general education": the rounded course of instruction a free citizen was expected to complete. The single-word Latin form *encyclopaedia* arose in the sixteenth century, partly through a scribal running-together of the Greek phrase. The root sense is therefore **the whole circuit of knowledge**, not a book at all.

**Strict definition**

A comprehensive reference work that presents *organised summaries of knowledge* — the substance of subjects — either across all fields (general) or exhaustively within one (specialised), arranged for retrieval, typically alphabetically or thematically, with articles written by identified contributors and each article standing as a self-contained treatment of its topic.

**The defining criterion**

An encyclopaedia is about **things**; a dictionary is about **words**. This is the standard and load-bearing distinction. A dictionary entry for *helium* tells you the word's meaning, pronunciation, and etymology; an encyclopaedia entry tells you about the element — its discovery, properties, uses. The unit of an encyclopaedia is the **subject or article**; the unit of a lexicon or dictionary is the **lexeme**.

**Against its neighbours**

| Work | Unit | Delivers |
|---|---|---|
| **Encyclopaedia** | subject/topic | expository summary of knowledge about the thing |
| **Lexicon / dictionary** | lexeme | sense, range, usage of the word |
| **Concordance** | word-form | occurrences and addresses |
| **Handbook / manual** | task or domain | practical guidance for doing |
| **Catalogue** | item | identification and location, no exposition |
| **Bibliography** | source | what has been written, not what is known |
| **Compendium / digest** | topic | abridgement, without the claim to coverage |

**Three properties usually treated as essential**

1. **Comprehensiveness within a declared scope** — the scope may be everything or one field, but the claim to *cover* it is constitutive. This is what the "circle" in the etymology carries.
2. **Synthesis, not primary research** — an encyclopaedia reports established knowledge; it is tertiary literature. An article advancing a new thesis is not functioning encyclopaedically.
3. **Systematic arrangement for retrieval** — alphabetical since Chambers (1728) and the *Encyclopédie* (1751–72); earlier works were arranged thematically, by the supposed structure of knowledge itself.

**Contested and extended uses**

The alphabetical/thematic question is genuinely disputed: thematic arrangement asserts a *structure* of knowledge and so makes a philosophical claim, while alphabetical arrangement disclaims one and optimises for lookup. The *Britannica* has at times attempted both simultaneously (Propædia/Micropædia/Macropædia).

Two extended senses are worth naming because they depart from the definition above:

- **Encyclopaedia as exhaustive catalogue**, where the "knowledge" is really a classification — the *Encyclopaedia of Chess Openings* from your previous question is this: it is a coded index of variations, not a set of expository articles. The word here borrows only the comprehensiveness claim.
- **Encyclopaedia as continuously edited corpus** (Wikipedia), which abandons identified authorship and fixed edition, both traditionally treated as definitional. Whether this is the same kind of object is a live argument in library science rather than a settled matter.

**Sources and assumptions**: the etymology, the words-vs-things criterion, and the Chambers/*Encyclopédie* alphabetical turn are standard and uncontested. The three "essential properties" are my synthesis of how the term is conventionally used rather than a quotation of any single authority — treat the framing as mine. Dates given from general knowledge; I have not searched or checked a specific reference-theory text. If you want the formal definition as used in library and information science (where encyclopaedias sit in a defined hierarchy of tertiary sources), that is a narrower technical treatment and I'd answer it separately.

---

## 14. The process loop, consolidated from discussion (2026-07-20) — governs §13

> This section digests the researcher's own working-through of the loop (recorded in
> `iba-process-loop-steps-to-flesh-out-v1-20260720.md`, §"researcher comments"). It is the **current
> authoritative trace of the process** and **governs §13 and §§2–12 where it differs**. It settles four
> things §13 held open — the entry point, completeness, the bulk/local split, and the core tables — and
> hands off to the config-rule work (§14.9). Still deliberately *direction, not final schema*; the exact
> columns are fixed empirically on John.

### 14.1 There is no single entry point — every entry point is a *study unit*

The loop is not entered only "at a chapter." An **entry point is a study unit**, and study units come in
types. What kind of unit you get is **derived from the request + the book's genre**:

| Entry request | Study-unit rule | Yields |
|---|---|---|
| **Book + poem, short** | the whole poem is one unit | 1 study unit |
| **Book + poem, long** | divide the poem into logical units | many study units |
| **Book + narrative** | split the book into narratives (scenes/episodes) | one unit per narrative |
| **Book + chapter** | split the chapter into sections | one unit per section |
| **Verse** | take the study unit already assigned to that verse; if none, read its genre and apply the book+genre rule | the containing unit |
| **Characteristic** (cross-verse extract from the three concordances) | pull its verses + report; researcher selects which verses to study, then each follows the **verse** rule | researcher-chosen units |

This is the **study-unit derivation ruleset** — pure config (§14.9). It supersedes both the single
"chapter" assumption of §13.3 and the genre table of §5 by unifying them: §5's genre→unit routing is
*how* these rows are computed, but the *entry* is always "give me a study unit for X."

### 14.2 Completeness — when a thing is "done"

A characteristic/verse is **done** when **all three hold**:

1. **all its verses are covered in the concordance**, AND
2. **it is encapsulated by a lexicon** (its lexical decomposition exists), AND
3. **it has a meaning that is signed off** — or is **cross-referenced to an already signed-off meaning**.

Completion is tracked **per verse, across all characteristics in that verse**, on **three parallel axes**
plus two whole-verse states:

- whole-verse: **Not started** · **Not relevant** (verse excluded from all output indexes)
- in-progress overall: **In progress** (some evidence, incomplete)
- the three axes, each *in progress* / *complete*: **Concordance** · **Lexical** · **Meaning**

So "In progress" is the union while any axis is unfinished; "done" is all three axes complete (or
Not-relevant). This is the completeness model the fitness gates (§8 Step 7) test against, and it becomes
a `cfg_status_flow` per entity (verse, study-unit-char). *(This replaces the flat worklist enum sketched
in the agenda's step 2.)*

### 14.3 Bulk vs local — the split is explicit, and both are legitimate

§13.2's "locality over bulk" does **not** ban bulk operations — it says *the meaning work* is local.
Several operations **are** bulk by nature, and that is correct:

| Bulk operation | Layer | State |
|---|---|---|
| STEP initial pull | Raw | done |
| STEP pull for a Strong (on discovering a Strong / new word) — **`new-word`** | Raw | built |
| Initial seed assembly | Base | done (manual) |
| **Seed update** — add/withdraw a seed → *automatically re-runs `set-characteristics`* | Base | to build |
| `set-characteristic` (initialise candidate characteristic) | Base | done |
| **Initialise concordances** — one-off, creates the first version of the three concordances (must resolve *how a span splits across the three*) | Concordance | to build |
| **Update candidate characteristic** — any change to a span's char-state **must flow through all related tables and references** | Concordance | to build |

**Rule refinements** sit *across* the split and need their own definition (§14.8 / Thread D): the app must
**trigger the need to refine completed work**, and the implications can be diverse (one rule change may
touch many worked areas). This is the one place locality and propagation collide — held open.

### 14.4 The two new core tables — `operation` and `meaning`

The meaning loop (§14.6) is the heart, and it writes two tables that did not exist in the §6 model:

- **`operation`** — *the characteristic in motion.* For a char under analysis, it **is affected by /
  affects / has a status / comes from / goes to / interacts with / co-exists with** other characteristics
  — i.e. **the dimensions, expressed as edges/events**. The `operation` table lists each such operation;
  **collectively the operations describe the characteristic in motion.** This is the live realisation of
  the "movements/associations/interlocking/emergence" object (RESET) — and it replaces the earlier
  `ib_finding`/"grain" framing as the primary analytical row. (`ve_lexical` remains the per-occurrence
  *lexical* decomposition; `operation` is the per-analysis *motion* record. They are distinct.)
- **`meaning`** — the generated, human-readable **meaning paragraph** for the characteristic-in-context;
  **signed off** or cross-referenced to a signed-off meaning (§14.2 axis 3). One meaning may be shared by
  cross-reference rather than duplicated.

The meaning loop touches, in one analysis: **span** (update role) · **the three concordances** ·
**passages = study unit** (status) · **lexicals** · **`operation`** · **`meaning`**.

### 14.5 The concordance — probably a view; three bodies; organised by register

- **The concordance may not be a physical table but a view.** Its display columns:
  **Gloss · Strong · transliteration · related words** (initially the registry word) **· verse
  references.**
- **Three concordances in parallel** (§13.1): IB characteristics · other-beings-toward-IB · physical-body-with-IB. Open build issue: **how one span is split across the three.**
- **The register is re-introduced as a collection**, by **organising the concordance by register**. Caveat:
  register **item naming may need to change** where the detail no longer coincides with the current name.
  **Alternative:** organise around **clusters** instead of registers. *(Decision deferred — §14.8.)*

### 14.6 The refined operation specs (supersede the agenda's A1/A2)

**`prepare-for-read`** (entry → study unit + candidate list):
1. Resolve the study unit by the **§14.1 derivation rule** for the request+genre.
2. Produce a **report**: the study-unit verses' **text** + the **candidate characteristic list**
   (*including any existing analysis* already held for those characteristics).
3. DB writes: **study-unit ↔ char ↔ analytic-status** (new table); **verse ↔ study-unit** index (new).
4. If the study unit is **already started**, offer: **create new / revise / select next char** (showing
   each char's status) — this is the resume surface.

**`analyse-characteristic`** (the meaning loop — researcher picks the focus):
1. Researcher **selects a char to focus** (a **list** is allowed as input).
2. **Deep-read the study unit with that char in focus.**
3. **Load existing** info from (a) the concordances, (b) the lexicals, (c) the operations.
4. If none exists, **generate lexicals for *all* chars in the study unit** (not only the focus char) —
   the `analyse-operation` sub-step.
5. **Screen-inclusion:** check which *other* chars in the context **interrelate** with the focus char;
   the deep analysis then runs for the focus char **and any char in direct relation to it**.
6. **Synergise the operations** (write/merge `operation` rows — the char-in-motion edges).
7. **Reconcile:** validate the loaded existing info against the fresh read.
8. **Generate the meaning paragraph** (`meaning`).
9. **Record (DB update):** span role · study-unit status · concordances *validated* (did roles change?) ·
   lexicals (update / delete-if-replaced-or-invalid / save-new) · operations (update existing + create
   new) · meaning (save if changed).
10. **`refine-rule`** if the read exposed a rule gap.

Two shifts from the agenda worth flagging: **(a)** lexicals are generated for **all chars in the unit**,
not just the focus char; **(b)** `select-next` is **researcher-driven focus selection**, not an automatic
queue — the resume/worklist still exists (§14.6 prepare step 4) but the human picks the next char.

### 14.7 Researcher operations — the interaction surface

Every researcher action is an app operation (§13.5 binds CC too). The set:

- **Bulk:** `new-word` · `set-characteristic` · `initialise-concordances`.
- **Specific:** add/remove seed · add/remove candidate characteristic · **reassign a Strong to another
  registry** · start a new study unit · interactively work a study unit · start a new char focus ·
  interactive feedback *(uncertain — flagged)* · get reports.
- **Reports & extracts:** the concordance (from all three; with options *exclude verse references* /
  *exclude related words* — a view to be tested) · study-unit status · char status · register status ·
  book status · **validations & errors**.

### 14.8 What §14 leaves open

- **Span → three-concordance split** (§14.5): how one span is allocated/duplicated across IB /
  other-being / body.
- **Register vs cluster** as the concordance's organising collection (§14.5), and the register
  item-renaming that register-organisation implies.
- **Rule-refinement propagation** (§14.3 / Thread D): how the app triggers re-work of completed areas
  without a bulk sweep — the hardest open item.
- **`operation` vs `ve_lexical` vs `ib_relation`** exact boundaries — §6's `ib_*` sketch must be
  reconciled with the researcher's `operation`/`meaning` naming (do §6's tables survive, or are they
  renamed to these?). Settled when the schema is cut, after the config rules.
- **"interactive feedback"** as a distinct researcher operation (§14.7) — researcher unsure.

### 14.9 Hand-off to the config-rule work (the next focus)

Everything above is **rules and structure that must land in the `cfg_*` store** before any build. The
config is **DB-authoritative** — it lives in `iba/app/db/iba.db` as 16 `cfg_*` tables (`iba/app/config/*.csv`
is a current export, validated row-for-row against the DB on 2026-07-20, not the store itself). Today it
holds only the three Base work packages (`new-word`, `set-candidates`, `build-passages`). The process loop
adds, as config: the **study-unit derivation ruleset** (§14.1), the **completeness status-flows**
(§14.2), the **bulk/local operation classification** (§14.3), the **operation-type (dimension) catalogue**
(§14.4), the **screen/role/inclusion rules** (§14.6 step 5), the **reconciliation rules**, and the
**report definitions** (§14.7). Extracting and straightening these into concrete `cfg_*` rows is the
immediate next task — tracked in its own working document.
