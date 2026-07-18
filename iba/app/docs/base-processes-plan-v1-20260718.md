# Plan: the base-layer processes — candidate characteristics (L4b) + passages

> **Status: DESIGN FOR CONFIRMATION. No DB changes until approved.** Directed 2026-07-18.
> Two processes, run as two separate manual steps; passages depend on the candidate
> characteristics and are re-run after each change to them. Sources: the old study's
> authoritative cycle, passage rule v2, verse-analysis method, and the captured old-DB schema.

---

## 1. Scope

Design the next processes on the **base** layer, above the raw slice already built:

- **(a) Candidate characteristics — the span L4b layer.** *Seed* the set of inner-being
  candidate lemmas, and *set* (stamp) that candidacy onto each qualifying span.
- **(b) Passage preparation.** Derive passages — the reading frames — from the candidate
  stamp, per book.

Both were modelled and used in the old DB; this reproduces their **intent** in the app's
config-governed shape. They run **manually**, as **two separate operations**. Passages are a
deterministic function of the candidate layer, so **build-passages runs after set-candidates**
and is re-run whenever candidates change. Neither is automatic.

Layer names: **L4a = `span`** (raw, immutable — one row per code of a verse). **L4b = the
interpretive layer over the span**: first the *candidate* stamp (this plan), later the *role /
lexical* read (Axis B — a **later** process, not in this plan).

---

## 2. What the old study did (the how / what)

### 2.1 Candidate characteristics — two orthogonal axes
*(cycle §1–§7; seeding session log; catalogue)*

- **Axis A — "is the *lemma* a candidate characteristic?"** Lemma-level, corpus-wide,
  deliberately over-inclusive. This is the **seed** → stamped as `char_candidate` (+ a
  `char_candidate_tag` like `IB:be gracious`) on the master span index. **This plan = Axis A.**
- **Axis B — "in *this* occurrence, what role does the span fill?"** Per-verse, decided only by
  the read → `role ∈ {characteristic, standalone, qualifier, undecided}` + the 16 lexical
  dimensions. **Later process, not here.**
- The read **overrides the seed both ways** (a seeded span can be demoted; an un-seeded span can
  surface a characteristic — "emergent"). Seed = a filter, not a verdict. Lists **validate,
  never impute**.

**How the old seed was built (~824 OT candidate lemmas over an 11,804-lemma inventory):**
three **meaning-only** layers — (1) lemma gloss == a registry inner-being word (221 words);
(2) gloss == a curated synonym (an editable dictionary); (3) broad IB judgement with manual
accept/reject. **Rejected routes** (never use): the registry `strongs_list` (matches
*co-occurring* strongs — "LORD" → "lust") and the phrasal `characteristic` table — both match on
*association*, not meaning. **Self-learning:** reads that find seed misses append to a
`char-seed-extension-read-emergent` list that the seed process **must consume on every run** and
re-stamp.

### 2.2 Passages — the reading frame *(passage rule v2, 2026-07-08 + 2026-07-13 amendment)*

- A passage is the frame in which a candidate characteristic is read. **IB-relevance is decided
  by the candidate stamp** (`char_candidate=1`), *not* by the verse-record. A verse with no
  candidate is in no passage and is never read.
- Mechanically a **maximal run of consecutive candidate-bearing verses**; **anchor = first
  verse**. **Single-verse passages are allowed** (incl. the emergent-char case).
- **Char-continuity amendment (2026-07-13):** a plain "maximal run" is genre-blind and bundles
  independent proverbs. Corrected: the run continues only while consecutive verses **share ≥1
  candidate base-Strong's**; a change of char focus breaks it. Two selectable rules —
  `char-continuity` (default; sentence/wisdom collections) vs `maximal` (discourse/poetry where
  consecutive verses form one movement). Passages **do not cross a chapter boundary** in practice.
- **Deterministic once the candidate stamp exists**, computed per book up front. **Therefore any
  change to candidates makes the passages stale → recompute the book.**
- **Integrity invariant:** every candidate span must resolve to an active verse-record; a
  candidate **without** one is a **DB integrity violation** (repair first, not a coverage gap).
- **Completion gates (per book):** 0 candidate-bearing verses with no passage; 0 candidates
  without a verse-record.

### 2.3 Old-DB modelling (for reference)

- `verse_span_index` (master): `char_candidate`, `char_candidate_tag`, plus Axis-B `role`,
  `characteristic`, `ib_char_id` columns — **all stamped as columns on the master**.
- `passage` table (id, ref, `anchor_verse_id`, book_id, start/end chapter+verse, `verse_count`,
  `source`) **and** passage fields on `verse` (`passage_id`, `is_passage_anchor`, `process_marker`,
  `genre`). Membership carried **only** by `verse.passage_id`; downstream tables inherit via the
  join. **No FK constraints** were declared — integrity was left to governance gates (a weakness
  to fix here).
- `ib_characteristic` — the normalised, **meaning-keyed** index (`char_key = lemma:reading`) —
  is written by the **read** (Axis B), so it is **out of scope** for this plan; noted for later.

---

## 3. New-app design

### 3.1 The seed is INDEPENDENT of the registry — an over-inclusive control

> **Corrected 2026-07-18 (researcher).** An earlier draft grounded the seed in `word_strong`
> (registry→strong). That is wrong: it makes the seed a mirror of the registry.

The seed must **not** be derived from the registry, for three reasons:

- **The registry is incomplete** and new inner-being words are still discovered. A registry-derived
  seed can only reflect the registry — it can never reveal what the registry is *missing*.
- **The independent seed is a double control on registry completeness.** Its whole value is that it
  is assessed *independently*: a lemma the net judges inner-being but that **no registry word
  carries is a candidate missing registry word** — a signal to grow the registry. Grounding the
  seed in the registry destroys that control.
- **The seed is over-inclusive by design — potential, not definite.** It marks lemmas that *could*
  be a characteristic *in some context*, not only those that definitely are. The **actual test is
  the lexical stage** (Axis B — each span's role re-evaluated in context), and the seed must stay
  open to **continuous learning**: reads that surface new IB strongs feed back into it.

So the seed runs an **over-inclusive meaning net over an independent corpus lemma inventory**, in
the old study's three layers — (1) registry-direct match (the registry as *one* evidence layer,
**and** the thing being checked, not the source), (2) curated synonyms (editable dictionary),
(3) broad IB judgement + manual accept/reject — deliberately generous. The hard-won artifacts
already exist (the ~11,804-lemma inventory, curated synonyms, IB-judgement, read-emergent
extension); the app **imports them as the starting substrate** and maintains them (plan §1.5). The
registry is one input and, simultaneously, the thing the seed **audits for completeness**.

### 3.2 New tables (proposed — schema.json additions)

**`lemma_inventory`** — the **independent** corpus lemma substrate the net runs over (imported;
not derived from the registry). This is what makes the seed an independent control.

| column | type | notes |
| --- | --- | --- |
| id | INTEGER pk | |
| lemma_key | TEXT notnull **unique** | base Strong's (sub-letters stripped, e.g. `H2603`) |
| gloss | TEXT | the lemma's English gloss (the meaning the net matches on) |
| language | TEXT | Hebrew / Greek |
| source | TEXT | import provenance (e.g. `lemma-inventory-master-2026`) |
| created_at | TEXT | |

**`candidate_seed`** — the **assessment** of each inventory lemma (over-inclusive; potential, not
definite). One row per assessed lemma.

| column | type | notes |
| --- | --- | --- |
| id | INTEGER pk | |
| lemma_key | TEXT notnull **unique** **fk → lemma_inventory.lemma_key** | the assessed lemma |
| decision | TEXT | `candidate` (potential — could be a char in some context) \| `rejected` \| `undecided` (enum `candidate_decision`) |
| layer | TEXT | which layer decided it: `registry-direct` \| `curated-synonym` \| `ib-judgement` \| `read-emergent` (enum `candidate_source`) |
| registry_match | TEXT | the registry word whose gloss matched, or NULL. **`decision=candidate` + NULL = a candidate missing registry word** (the double-control signal) |
| tag | TEXT | IB label carried onto the stamp |
| assessed_at | TEXT | |

> `decision=candidate` means **potential**, deliberately over-inclusive — the definitive per-
> occurrence test is the later lexical (role) stage, not this seed.

**`span_candidate`** — the **L4b** stamp (one row per candidate span; existence = candidate).

| column | type | notes |
| --- | --- | --- |
| id | INTEGER pk | |
| span_id | INTEGER notnull **fk → span.id** | the L4a span stamped |
| lemma_key | TEXT | base Strong's of the span (denormalised for continuity/join) |
| candidate_tag | TEXT | the IB label carried from the seed |
| seed_source | TEXT | which seed layer (enum `candidate_source`) |
| set_at | TEXT | |
| *unique* | | `span_id` — at most one candidate stamp per span |

**`passage`** — the reading frame (global, per book).

| column | type | notes |
| --- | --- | --- |
| id | INTEGER pk | |
| book | TEXT notnull | OSIS book code (e.g. `Prov`) — from `verse.osisId` |
| anchor_verse_id | INTEGER notnull **fk → verse.id** | first verse of the run |
| start_chapter / start_verse / end_chapter / end_verse | INTEGER | |
| ref | TEXT | human range, e.g. `Prov 3:5-8` |
| verse_count | INTEGER | ≥1 |
| rule | TEXT | `char-continuity` \| `maximal` (enum `passage_rule`) |
| source | TEXT | `passage-build` \| `single-verse-emergent` (enum `passage_source`) |
| created_at | TEXT | |

**`verse_passage`** — passage membership (**L4b**; keeps the raw `verse` table pristine).

| column | type | notes |
| --- | --- | --- |
| id | INTEGER pk | |
| passage_id | INTEGER notnull **fk → passage.id** | |
| verse_id | INTEGER notnull **fk → verse.id** | |
| is_anchor | INTEGER | 1 on the anchor verse |
| created_at | TEXT | |
| *unique* | | `verse_id` — a verse belongs to at most one passage |

> FKs are **declared** (the old DB declared none — a stated weakness). As in the raw slice the app
> won't hard-enforce them at the pragma level, but the validation report checks resolvability.

### 3.3 The two processes (config-governed steps)

Two work packages in `run.json`, each with its own PowerShell entry, both **running over a book**
(`runs_over: "book"`; param `Book` = OSIS code; the book's verses are selected by `osisId` prefix
against `cfg_book_order` — no book table needed).

**Process (a) — `set-candidates` (manual).**  `Set-Candidates.ps1 -Book Prov`
1. **`candidate.seed`** — refresh the global assessment (idempotent), **independently of the
   registry**: ensure `lemma_inventory` is loaded (imported once), run the three-layer meaning net
   over it — registry-direct match, curated synonyms, IB judgement (over-inclusive) — plus consume
   any `read-emergent` extensions, and write `candidate_seed` decisions with the deciding `layer`
   and `registry_match`. Emits the **double-control signal**: `decision=candidate` lemmas with
   `registry_match IS NULL` = potential missing registry words. Writes `lemma_inventory` (first
   run) + `candidate_seed`.
2. **`candidate.set`** — for every `span` in the book's verses whose base-Strong's is a
   `decision=candidate` lemma in `candidate_seed`, (re)write its `span_candidate` row (delete the
   book's rows first, then restamp — clean re-derivation). Over-inclusive by intent; the lexical
   stage later tests each in context. Writes `span_candidate`.

**Process (b) — `build-passages` (manual, after (a)).**  `Build-Passages.ps1 -Book Prov [-Rule char-continuity|maximal]`
1. **`passage.build`** — recompute the book's passages from `span_candidate`: sweep verses in
   canonical order; a verse is *candidate-bearing* if it has ≥1 `span_candidate`; grow a run
   through consecutive same-chapter candidate-bearing verses while they **share ≥1 candidate
   base-Strong's** (char-continuity) or unconditionally (maximal); anchor = first verse;
   single-verse runs allowed. Delete the book's passages first, then rebuild. Writes `passage` +
   `verse_passage`.

### 3.4 Config rules (proposed)

- **settings (`rules.json`):** `candidate.lemma_base_pattern` = `^([HG]\d+)([A-Z]?)$` (capture the
  base — the app's "if the code reads it, it's config" principle); `passage.default_rule` =
  `char-continuity`; `passage.cross_chapter` = `false`; `passage.min_shared_strongs` = `1`.
- **imported substrate (read-only, from the old study — plan §1.5):** the lemma inventory
  (`lemma-inventory-master-no-particles-20260707.json`, ~11,804 lemmas) → `lemma_inventory`; the
  curated synonyms and the IB-judgement accept/reject lists → the net's config; the
  `char-seed-extension-read-emergent-*` lists → consumed each seed run.
- **editable dictionary (`config/candidate.json`, new seed):** `{ "synonyms": [], "accept": [],
  "reject": [] }` — the editable meaning-net inputs (curated synonyms + manual IB accept/reject),
  grown as reads surface misses (the self-learning path). Loaded into a `cfg_candidate_rule` table
  by `cfgload`. **Not** the registry — an independent dictionary.
- **write grants:** `candidate.seed → [lemma_inventory, candidate_seed]` ·
  `candidate.set → [span_candidate]` · `passage.build → [passage, verse_passage]`.
- **enums:** `candidate_decision` (candidate, rejected, undecided) · `candidate_source`
  (registry-direct, curated-synonym, ib-judgement, read-emergent) · `passage_rule`
  (char-continuity, maximal) · `passage_source` (passage-build, single-verse-emergent).
- **on_fail:** `candidate.set / no-spans` → report-stop ("no spans for the book — build its words
  first"); `passage.build / candidate-unpassaged` → report-stop (the completeness gate);
  `passage.build / candidate-orphan` → report-stop (a candidate span with no verse — integrity).

### 3.5 Integrity + validation (extends the existing validation report)

New checks, book-scoped, added to the validation report so success is visible:
- **span_candidate → span** resolves (0 orphans) — the new-app form of the "candidate must have a
  verse-record" invariant (a span always belongs to a verse by construction).
- every `span_candidate` verse ends up **in a passage** after build (0 candidate-bearing verses
  unpassaged) — the completeness gate.
- `verse_passage` unique per verse; anchors = passage count; passages don't cross chapters.
- every `candidate_seed.lemma_key` resolves to `lemma_inventory` (the net ran over the real
  substrate); `decision` in the enum.

**The double control (registry completeness) — a first-class output, not just a check.** The seed
run reports the `decision=candidate` lemmas with `registry_match IS NULL` as **candidate missing
registry words** (with gloss + layer), so the researcher can grow the registry. This is
informational/WARN, never a failure — it is the point of an independent seed. Over-inclusiveness is
expected: `span_candidate` count will far exceed the eventual confirmed characteristics, which the
lexical stage resolves later.

### 3.6 Dependency & ordering

`set-candidates(book)` → `build-passages(book)`. Both manual. Re-running `set-candidates` (e.g.
after more words are built, or a curated/emergent change) makes the book's passages stale — the
researcher then re-runs `build-passages`. The validation report flags a book whose candidates
changed after its passages were last built (compare `set_at` vs passage `created_at`).

---

## 4. Open decisions — please confirm (recommendation first)

1. **span_candidate as a separate L4b table** (recommended) vs columns on `span`. Recommend
   separate: keeps the raw L4a span immutable, matches the app's layered model, and lets a clean
   re-derivation just delete+rebuild the L4b rows.
2. **Passage membership as a `verse_passage` table** (recommended) vs `verse.passage_id` +
   `is_passage_anchor` columns as the old DB did. Recommend the table: keeps the raw `verse`
   pristine; the old column approach mutated the base verse.
3. **Boundary rule via a `-Rule` flag now** (recommended), defaulting to `char-continuity`, with
   genre-driven auto-selection deferred (no `verse.genre` yet). Recommend the flag; add genre later.
4. **Candidate seed INDEPENDENT of the registry** (recommended; corrects the earlier
   word_strong-grounded draft — see §3.1). An over-inclusive meaning net over an imported corpus
   lemma inventory (registry-direct + curated synonyms + IB judgement), serving as a double-control
   on registry completeness; the lexical stage is the definitive test. Recommend this.
5. **Import the old study's seed artifacts as the starting substrate** (recommended): the lemma
   inventory, curated synonyms, IB-judgement lists, and read-emergent extension — read-only from
   the old study files (plan §1.5). The alternative (rebuild the inventory from STEP/morphology) is
   more work and less faithful. Recommend importing.
6. **Scope = per book, derived from `osisId`** (recommended) — no book table; `Book` = OSIS code.
7. **Out of scope here (confirm):** the Axis-B *role / lexical* read and the `ib_characteristic`
   meaning-keyed index — a later process. This plan stops at the candidate stamp + passages. It is
   also where the seed's continuous learning closes the loop (read-emergent feeds `candidate_seed`).

**On confirmation** I will add the five tables (`lemma_inventory`, `candidate_seed`,
`span_candidate`, `passage`, `verse_passage`) + enums to `schema.json`, the two work packages and
their steps to `run.json`, the settings/grants to `rules.json`, and the `candidate.json` seed —
all through the config utility (validate → load) — then build the two handlers and their
PowerShell entries, and extend the validation report. **Nothing touches the DB until you confirm.**
