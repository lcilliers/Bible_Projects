# WA — Analytic Input Specification (v2.0)

**File:** WA-analytic-input-spec-2.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 2.0 — **major. Redone from scratch against the authoritative rule base.**
**Author:** le Roux Cilliers
**Purpose:** the single instruction for generating the analytic input **per book**, for AI-side analysis.

**Supersedes:** `WA-projection-spec-1.0` / `1.1` / `1.2` (all written before the rule base was read; several of their asks were wrong).
**Governed by:** `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708` · `wa-verse-analysis-method-v1-20260702` · `wa-book-lexical-readiness-assessment-AUTHORITATIVE-v1-20260712`.
**Companion:** `WA-rulebase-reconciliation-1.0-2026-07-13` (what the rule base overturned and why).
**Built from:** `psalms__grace-mercy-compassion.json` (base source, 16 readings) and `psalms__wisdom-folly-teaching__narratives.json` (meaning artefact, 39 records).

---

## PART 1 — WHY THIS VERSION EXISTS (the learnings)

Everything in Part 2 follows from five things established the hard way in this session. They are recorded first because **the shape of the deliverable is a consequence of them**, not an arbitrary preference.

### L1 — The emitted artefact is not self-describing, and must not be treated as if it were

Working from the emitted JSON alone, I drew **four structural conclusions that the rule base falsified**: that the corpus had three story-generations (it has two); that the `H2603` split was gloss-driven (it is span/meaning-keyed, per §7D v3); that `type` was a faculty bin (it is morphology-derived); and — most seriously — that **`direction` was never recorded**.

**Direction is recorded. It always was.** Cycle §3: *a dimension value is a VALUE, a **PAIR (`from_span → to_span`)**, an EVENT, or a FLAG.* **The pair is the directed edge, and the position in the pair is significant.** I called it missing because the emission shows `to_span` on 49 of 176 rows and `from_span` on 4.

**The design consequence:** the analytic input must carry **the evidence for its own structure**, not just its values. A file that shows one endpoint of a directed pair will be read as undirected by anyone who does not already know the rule.

### L2 — Three states, not two — and the corpus has a fourth it should not have

Cycle §3A **P4**: every dimension is in exactly one of **resolved · none/silent · unresolved**, and *"Silence ≠ unresolved."*

The base source honours this for `seat` — a **row** with `value: "none"`, `resolution: "none"`. But `intensity` (109), `prohibition` (113) and `specifier` (110) have **no row at all** (`present: false`) in all 16 readings — a fourth state the model does not admit. Method §14 has all three **ON** for poetic. **They are missing, and that is a real gap.**

By contrast, `source` (103) and `effect` (111) are `present: false` **by design** — method §14: for poetic genre, *"cross-verse items OFF (source-across-verses / effect / process would be noise between poetic lines)."* **Not a gap. The method working as intended.**

**The design consequence:** the analytic input must distinguish, per cell, between **resolved · none · unresolved · out-of-scope-by-genre · not-written**. Collapsing these is how a design decision becomes a false finding (see L3).

### L3 — The `story` layer launders design decisions into findings about Scripture. Measured.

Across all 39 records of `psalms__wisdom-folly-teaching__narratives.json`:

| layer | uses **record** vocabulary (*"absent"*, *"no origin is booked"*) | asserts **Scripture-silence** (*"the passage never tells us"*) |
|---|---|---|
| `narrative` (technical) | **39 / 39** | **0 / 39** |
| `story` (prose) | **0 / 39** | **8 / 39** |

The technical narrative attributes the absence to **the reading**:
> *"Source (103) is absent: no origin is booked, so **the reading** does not trace what drives the plotting"* `[Psa 2:2]`

The story attributes it to **the text**:
> *"**The passage** never tells us what is driving them, whether fear or ambition"* `[Psa 2:2]`

`source` is deliberately unread for poetic genre. **The story tells the reader that Scripture is silent about something the method chose not to look for.**

The same fault reached the combined story corpus: all 167 `inner-seat` narratives close with *"the psalm does not tell us how strong it was, or how it finally turned out"* — **intensity** (should have been read; wasn't) and **effect** (deliberately out of scope). E1's headline finding had to be split in two on this evidence.

**This is not primarily an AI problem. It is a researcher problem.** The story is the layer the researcher reads to digest findings. It is where the laundering does most damage.

**The design consequence:** the story layer's silence-vocabulary must be fixed at source (see §2.5), and — until it is — **the story is a claim to be checked, never evidence.**

### L4 — The `narrative` layer is compensating for a `discovery` field that is not working

Cycle §3A **P8**: the discovery-lookout is *"the emergence engine"* (dimension 114). Every read asks *"what does this verse state or imply about the inner being that the current dimensions do NOT capture?"* A verse with nothing to flag **records `discovery: none`** — *"so we know it was looked for, not skipped."*

**In the base source, `discovery` is populated 16 of 16 and `discovery: none` appears zero times.** Its content is the verse quotation plus a gloss — a **sense-seed**, not a lookout.

Meanwhile the *technical narrative* is doing the lookout's job in prose:
> *"the LORD's answering derision (v4) **is not filed as this operation's effect**"* `[Psa 2:2]`

That is exactly a P8 observation — the reader noticing what the frame excluded — and it is sitting in a free-text narrative instead of in field 114 where it belongs and can be aggregated.

**The design consequence:** if `discovery` is fixed, the technical narrative's unique value largely collapses into the structured data, and the token cost of the analytic input drops by ~75%. **Fixing 114 is the highest-leverage item in this specification.**

### L5 — File size is irrelevant. Only what is *read verbatim* costs anything.

There is no maximum file size. A 5 MB CSV is trivially processed on disk. The only budget is **context** — what must be read as prose because its meaning cannot be counted.

- **Coded columns** (`span_id`, `morph`, `ve_nr`, `seat`, `resolution`, `from_span`, `to_span`, `present`, `role`, `locus`…) — **never read.** Computed over. Zero context cost, corpus-wide, always.
- **Free-text columns** (`sense`, `operation`, `discovery`, `coupling`, `target`, `bearer`) — **always read.** Meaning cannot be regexed. Every attempt to do so this session produced garbage and was discarded.

**The design consequence:** optimise the deliverable for *completeness on disk*, not for compactness. Emit everything. Let the coded columns be free and the free text be paid for per family.

---

## PART 2 — THE DELIVERABLE

### 2.1 Shape: one CSV at **dimension-row grain**, per book

**Not** one row per reading. A row-per-reading destroys the pairs — and the pairs are the direction (L1). Eleven of the sixteen dimensions are pairs or pair/flags (cycle §3).

**File:** `wa-<book>-lexical-flat.csv` — one row per `ve_lexical` dimension row, reading identity **denormalised onto every row**.

| # | column | source | class |
|---|---|---|---|
| 1 | `reading_id` | base source | coded |
| 2 | `char_key` | `{lemma}:{normalised_esv}` (§7D v3) | coded |
| 3 | `lemma` | base Strong's | coded |
| 4 | **`span_id`** | `verse_span_index.id` — **the master key; everything joins on the span, never the Strong's** (§10) | coded |
| 5 | **`morph`** | `verse_morphology` — **the parse the study actually reads** | coded |
| 6 | **`hebrew_form`** | surface form in the verse | coded |
| 7 | `translit` | promote out of the free text (`pity (chanan)` → a column) | coded |
| 8 | `ib_char` | the read characteristic | coded |
| 9 | `family` | 1 of 46 | coded |
| 10 | `cluster` | | coded |
| 11 | **`verse_ref`** | **`Psa 37:21` — NOT the passage range** | coded |
| 12 | `passage_ref` | retained; the passage is the reading frame (§4A) | coded |
| 13 | `genre` | drives which dimensions are in scope (§14) | coded |
| 14 | `anchor` / `same_as` | anchor vs duplicate reading | coded |
| 15 | `ve_nr` | 101–116 | coded |
| 16 | `label` | sense…locus | coded |
| 17 | `item_type` | value / pair / event / flag / note | coded |
| 18 | `value` | | **free text** |
| 19 | **`from_span`** | **near endpoint of the directed pair** | coded |
| 20 | **`to_span`** | **far endpoint — the qualifier span** | coded |
| 21 | **`pair_kind`** | | coded |
| 22 | `resolution` | resolved / none / inferred / span / unresolved | coded |
| 23 | **`state`** | see §2.2 — **the single most important column in the file** | coded |
| 24 | `role` | always `characteristic` (§11 rule 6 — only characteristics carry a lexical) | coded |
| 25 | `provenance` | | coded |

**Volume:** 16 slots × 2,048 readings ≈ **32,768 rows** for Psalms (≈ 22,500 present + ≈ 10,000 absent). Trivial on disk. **Do not filter.**

**Emit all 16 dimensions for every reading, including the absent ones.** An absent dimension is data (L2) and its *reason* is data (§2.2).

### 2.2 The `state` column — the fix that prevents L3 recurring

Every dimension row carries exactly one:

| `state` | meaning | current representation |
|---|---|---|
| `RESOLVED` | the verse gave a value | `value` populated |
| `NONE` | **the reader looked and found nothing.** Evidence of silence. | `value: "none"`, `resolution: "none"` |
| `UNRESOLVED` | the verse signals a value is expected but it cannot be settled (P4) | *no representation today* |
| **`OUT-OF-SCOPE`** | **the dimension is deliberately not read for this genre** (§14: `source`, `effect`, `process` for poetic) | *conflated with the next row today* |
| `NOT-WRITTEN` | should have been read; was not (`intensity`, `prohibition`, `specifier` in the sample) | `present: false` |

**`OUT-OF-SCOPE` and `NOT-WRITTEN` are currently indistinguishable, and that is the root of L3.** Separating them makes the laundering fault structurally impossible: no downstream layer can report *"the psalm does not tell us"* about a cell marked `OUT-OF-SCOPE`.

### 2.3 Pairs must be emitted with **both endpoints**

The pair is the directed edge; **position in the pair is significant** (researcher, and cycle §3/§5).

- If `from_span` is **implicit** (= the characteristic's own span), **say so explicitly in the meta block** and populate it anyway. Do not leave it to be inferred.
- Emit `pair_kind` and `resolution` on every pair row.
- **Open question for CC to answer:** in the base source, `to_span` appears on 49 of 176 rows and `from_span` on 4. Is `from_span` implicit, or genuinely absent? **This determines whether the direction is recoverable from the current emission at all.**

### 2.4 The narrative layer — one JSON per book, keyed by `reading_id`

**File:** `wa-<book>-narratives.json` — the existing `__narratives.json` shape is already right. Keep **both** fields:

- **`narrative`** (technical) — **this is the layer I work against.** It is epistemically sound (L3), and it carries the boundary observations the `discovery` field should hold (L4).
- **`story`** (prose) — retained for the researcher, and read **last** by me, as a claim to be checked against the evidence.

**Where the two diverge, that is a finding, not a discrepancy to smooth over.** Two divergences were found from a single family this session, and both were substantive.

### 2.5 Required fix to the `story` layer (independent of anything AI-side)

The story's silence-vocabulary must distinguish:

| the story currently says | it should say when… |
|---|---|
| *"the passage never tells us what is driving them"* | `state = OUT-OF-SCOPE` → **say nothing**, or *"origin is outside the scope of the poetic read"* |
| *"the passage does not say how strong"* | `state = NOT-WRITTEN` → **say nothing.** Do not assert a silence that was never tested. |
| *"the psalm does not locate it in any one part"* | `state = NONE` → **correct as written.** This is a genuine reader determination and the strongest evidence in the corpus. |

**8 of 39 records in the sample commit this fault.** It is fixable at the template level.

### 2.6 What to drop

| dropped | why |
|---|---|
| `passage_text` | ~2,800 words/family — the single largest component. The Psalm is readable elsewhere. |
| `ve_lexical_ids` (11-element arrays per reading) | backtracking keys; recoverable from the DB. Keep **one** `key_span_id`. |
| `notes` (0 of 176 populated), `provenance` as a per-row constant | dead weight |

### 2.7 Evidence columns to add from `ib_characteristic`

§7D declares these **mandatory** — *"so any grouping is auditable and no bad merge is hidden."* They exist. They are simply not emitted:

`stems` · `morph_codes` · `esv_words` · `lexical_gloss` · `read_sense_variants` · `key_span_id`

**These are the evidence that the `H2603` split is span/meaning-based and not gloss-based.** Without them, every reader of the file will draw the wrong conclusion — as I did.

---

## PART 3 — TOKEN ASSESSMENT (measured, not estimated)

Measured from the two real files. `1 word ≈ 1.3 tokens`; `1 CSV byte ≈ 0.25 tokens`.

### 3.1 Per reading

| layer | per reading | note |
|---|---|---|
| CSV — **coded columns** | ~44 tok | **never read. Zero cost.** |
| CSV — **free-text columns** (`value` on sense/operation/discovery/coupling/target/bearer) | **~61 tok** | read |
| `narrative` (technical) | 307 words ≈ **399 tok** | read |
| `story` (prose) | 130 words ≈ **168 tok** | read last |

### 3.2 Corpus-wide (Psalms, 2,048 readings)

| layer | tokens | fits one pass? |
|---|---|---|
| CSV coded columns | ~90 k | **not read at all — computed on disk** |
| CSV free text | ~124 k | marginal; not needed corpus-wide |
| `narrative` | **~816 k** | **no** |
| `story` | ~345 k | **no** |

**Neither prose layer is a corpus-wide read. Both are per-family reads. This is not a limitation — it is the correct working order.**

### 3.3 Per family — the actual working unit

| | avg family (≈45 readings) | largest family (167) |
|---|---|---|
| CSV free text | ~2.7 k | ~10 k |
| `narrative` | **~18 k** | ~67 k |
| `story` | ~7.5 k | ~28 k |
| **working total (CSV + narrative)** | **~21 k** | **~77 k** |

**Comfortable. All 46 families across several passes, with room to think and write.**

### 3.4 The prize for fixing `discovery` (L4)

If field 114 carries the P8 lookout properly, the technical narrative's unique content moves into the structured data. The working load per family drops from **~21 k to ~3 k** — the narrative becomes optional rather than necessary. **That is a ~7× reduction, and it is the single highest-leverage change in this document.**

---

## PART 4 — THE WORKING ORDER (and why it is not negotiable)

1. **Compute over the coded columns**, corpus-wide, on disk. Free.
2. **Read the CSV free text** for the family in focus. Form observations **from the evidence**.
3. **Then** read the `narrative`. Check whether it says the same thing.
4. **Then** read the `story`. Check it against both.
5. **Where the layers diverge — that is a finding.**

**Rationale.** The story layer is a lossy and, in places, misleading derivative of the lexical (L3). Reading it first anchors the analysis on its conclusions, including the unsound ones. This is *plausibility ≠ truth* operating exactly as the programme's own standing lessons predict.

Two divergences were found from a single family this session — the `intensity` silence and the `effect` silence. **The seam between the layers is productive, and it only works if the evidence is read before the story.**

---

## PART 5 — WHAT CC SHOULD PRODUCE, PER BOOK

| # | artefact | grain | note |
|---|---|---|---|
| 1 | `wa-<book>-lexical-flat.csv` | one row per `ve_lexical` dimension row | §2.1. All 16 dimensions per reading, including absences. `state` column mandatory (§2.2). Both pair endpoints (§2.3). |
| 2 | `wa-<book>-narratives.json` | one record per `reading_id` | `narrative` + `story`, existing shape. |
| 3 | `wa-<book>-readings.csv` *(optional, derivable)* | one row per `reading_id` | a convenience pivot; I can build it from (1) in one line. **Do not build it instead of (1).** |

**Meta block on (1) must state:** book · genre · which dimensions are `OUT-OF-SCOPE` for that genre (§14) · whether `from_span` is implicit · generation date · source-of-truth.

---

## PART 6 — OPEN ITEMS, IN PRIORITY ORDER

| # | item | why it ranks here |
|---|---|---|
| **1** | **`discovery` (114) is not running as the emergence engine.** 16/16 populated with a sense-seed; **zero `discovery: none`.** P8 calls it *"the emergence engine."* | If it is dark, the mechanism by which new dimensions are found and back-propagated is dark. And fixing it cuts the analytic read load ~7× (§3.4). |
| **2** | **The `story` silence-vocabulary** (§2.5). 8 of 39 records launder a design decision into a claim about Scripture. | It misleads the researcher, not just the AI. |
| **3** | **`intensity` / `prohibition` / `specifier` not written**, though §14 has them ON for poetic. | A real gap, and E1's *"how strong"* silence rests on it. |
| **4** | **Is `from_span` implicit or absent?** (§2.3) | Determines whether direction is recoverable from the current emission. |
| **5** | **`coupling` ↔ `locus` swapped** in 10 of 16 rows of the sample. | Mechanical, detectable, corrupts any query on either field. |
| **6** | **Is `object-type` being recorded on `target`?** §5 step 2 calls for *"target with object-type."* Not visible in the emission. | E4 needs it. It may already exist. |

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0–1.2 | 2026-07-13 | Superseded. Written before the rule base was read; asked for a reading-grain projection (destroys the pairs), claimed `direction` was unrecorded (it is the pair), and claimed `source`/`effect` were unread (they are out of scope by genre). |
| **2.0** | 2026-07-13 | **Major — redone from scratch against the authoritative rule base.** Dimension-row grain preserving both pair endpoints. Five-state `state` column separating `OUT-OF-SCOPE` from `NOT-WRITTEN`. Technical `narrative` chosen over `story` on measured evidence (39/39 vs 8/39). Working order fixed: evidence → narrative → story, divergence = finding. Token assessment measured, not estimated. `discovery` (114) identified as the highest-leverage fix. |
