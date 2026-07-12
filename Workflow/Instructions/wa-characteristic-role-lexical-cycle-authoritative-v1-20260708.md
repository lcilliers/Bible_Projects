# Characteristic → Candidate → Role → Lexical — AUTHORITATIVE CYCLE INSTRUCTION (v1)

> **Status: AUTHORITATIVE. This is the single governing instruction for how the study determines characteristics, seeds candidates, sets roles, and generates lexicals.** It **supersedes all prior attempts** at this sub-process — including the qualifier-as-a-role framing, the per-span role-reassessment method, the strongs-list / 277-table candidate attempts, and any earlier "characteristic determination" notes. Where any older document conflicts with this on *characteristic identity, role, candidacy, or lexical generation*, **this document wins.** It does **not** replace the study's foundations (scripture-as-data, the master-index architecture, the dimension catalogue mechanics) — it sits on top of them and makes the cycle unambiguous. Set 2026-07-08.
>
> **Amendment 2026-07-08 (same-day completion).** Three sections added to finalise the cycle: **§4A Stage 0 — Passage prerequisite** (no verse read outside a passage; passage driven by the candidate characteristic; whole-book layout precomputed), **§7A DB updates & index maintenance** (the per-verse write ledger; the candidate⇒verse-record integrity invariant; `verse_evidence_index` deprecated for lexicals), and **§7B Transition & changeover** (`role_provenance` two-state model). Resolves the three open decisions in `verse-analysis/_reports/wa-cycle-db-updates-indexes-transition-passage-analysis-20260708.md`: (1) `verse_evidence_index.lexical` = **deprecated/defunct**; (2) read-vs-legacy marked by **`role_provenance = 'read-2026'`**; (3) passage scope = **candidate characteristic**, with candidate-without-verse-record treated as an **integrity violation to repair**, not a scope union. Companion passage rule bumped to `wa-passage-completeness-rule-v2-20260708.md`.
>
> ---
> ## ★ THIS IS THE SINGLE ENTRY POINT — read this before any book work (consolidated 2026-07-11)
> **One process, one set of tables, one set of validations. Do NOT create parallel scripts or side docs for any part of it.** This doc owns the end-to-end process; four sub-domain docs own their detail and nothing else (no overlap). Everything below is *this* set:
>
> | domain | THE authoritative doc | used by |
> |---|---|---|
> | **The end-to-end cycle (process)** | **this doc** — Stages 0→3, §7A tables, §7C completion | the whole per-book run |
> | **Adding/updating a term** (register→extract→audit_word; every field) | `wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md` | §7C(a) verse-record fix / onboarding |
> | **Passage build** (incl. single-verse passages) | `wa-passage-completeness-rule-v2-20260708.md` | §4A Stage 0 |
> | **DB integrity — the validations (I1–I11)** | `wa-db-integrity-definition-authoritative-v1-20260711.md` | §7C(d) completion = these checks |
>
> **Superseded / do not use as a parallel spec:** `wa-corrected-charac-arc-reread-repeatable-process-v1` (its reading discipline is already §5 here; kept only as worked-example notes), any per-session `_apply_*` one-offs (`_apply_charfix_master`, `_apply_build_ib_char_index`, `_apply_stamp_char_candidate…`) — these are the **implementation** of the steps below, not a second method. If a step is unclear, the answer is in **this doc + its four sub-docs**, never in a new structure.
>
> **Amendment 2026-07-11.** Folded in three settled items: **single-verse passages** (§4A / passage-rule-v2 — an isolated char stands as its own passage); the **char-on-master write** (`verse_span_index.characteristic` = the read char in words — §7A row 6, §7C(c)/(d)); and the **`ib_characteristic` normalised index** (one record per characteristic word, every char-span linked via `verse_span_index.ib_char_id` — §7A row 7, new §7D, §7C(d) book-level). Integrity is now the **I1–I11** set in the integrity doc; §7C(d)'s queries are those invariants.

---

## 0. Why this exists
The characteristic/role/lexical question has been mis-understood and re-attempted many times, each partial, each drifting. The recurring errors were: (a) treating a *qualifier* as span requiring a lexical or characteristic when it is really part of dimension on a characteristic; (b) matching candidates on incidental association (co-occurring strongs, phrasal characteristic-names) instead of meaning; (c) treating raw "missing lexical" counts as the worklist; (d) letting the seed act as a verdict instead of a filter; (e) trying to derive *role* from morphology. This instruction fixes all five and defines the cycle end-to-end.

Putting it in perspective - The ultimate goal of the study is to document and describe how the characteristics of the Inner Being work, based on the verses in the bible. This is derived by dissecting the morphology of each verse and via the lemma do a provisional assessment of the lemma to set it as a candidate characteristic. Every verse with a lemma that have a candidate characteristic is then read in the context of the passage around the verse to create a lexical decomposition around 16 dimensions. Verses with multiple lemmas as candidate characteristic will have a lexical analysis for each char-lemma.  This forms the basis of further analysis and synergies accross lexicals and passages to describe how to characteristics operate in the inner being.

## 1. The object and the definitions (fixed vocabulary)
- **Lemma** = the meaning in english of the word in the context of the verse.  The Lemma is interchangeably referred to the *span* of the word.
- **Characteristic** = an inner-being disposition/faculty/operation that the verse (in its passage) *turns on* — decided by the **use and meaning of the span in the verse/passage**, and that it does/says something about the inner being. **Never** by a lookup table; the registry/lists only *validate* (verse→list), they never *impute*.
- **Master index** (`verse_span_index`) = the term-verse-span substrate: one row per morphological word, built 1:1 from `verse_morphology`. A span is **uniquely** identified by its `id` (equivalently `verse_id,word_index`). **The strong is NOT unique** — it repeats within a verse and across the corpus — so everything keys on the **span id**, never on the strong.
- **Role** — The role is one of the dimensions of the lexical analysis and is assigned/confirmed when the lexical for the lemma in the verse is processed. It is the per-span classification, restricted to **exactly**: `characteristic` · `standalone` · `qualifier` · `undecided`. A word that elaborates, qualifies, or names an object/source is **not a characteristic and is assigned the role of qualifier**, it does not get a separate lexical analysis and it application is carried by the associated characteristic's **dimensions** (§3). `undecided` = the read could not decide (write the reason to the discovery dimension of the associated characteristic).
- **Standalone** = a span that is neither a characteristic nor a dimensional member of any characteristic in its verse (binds to nothing). Function words (particles, prepositions, connectives, pronouns) are standalone.

## 2. The TWO ORTHOGONAL AXES (the distinction that removes the confusion)
Everything in this cycle is one of two independent questions. Do not conflate them.

- **Axis A — Is the *lemma* a candidate characteristic?** A **lemma-level, corpus-wide** property. Answered by the **seed** (§4). Over-inclusive on purpose. This is `char_candidate` on the master.
- **Axis B — In *this occurrence*, what role/dimension does the span fill?** A **per-verse** property. Answered only by the **lexical read** (§5–6). This is `role` + the dimension pairs.

A word can be **both** — e.g. "he set his heart on *wisdom*": *wisdom* is a characteristic **and** the target of the heart-setting. Axis A candidacy never overrides Axis B; Axis B never rewrites Axis A. `char_candidate` and `role` are **different columns for different questions**.

## 3. The 16 dimensions (per-span) and what morphology can give
> **Authoritative dimension source:** the **VE-lexical catalogue** — `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` — defines each dimension's shape, derivation rule, resolution states and D↔ve_nr numbering. The table below is the **ve_nr summary** for this cycle and must stay in step with the catalogue; on any conflict the catalogue wins for *dimension definition*, this instruction wins for *how the cycle uses them*.

Every span is described across the 16 per-span dimensions (`ve_lexical`, `ve_nr` 101–116). A dimension value is a **VALUE**, a **PAIR** (`from_span → to_span`, with `resolution`), an **EVENT**, or a **FLAG**. **Relational person/thing words (objects/sources/seats) live here as pair members — that is why they need no separate lexical.**

| ve_nr | dim | from morphology? |
|--:|---|---|
| 101 sense · 102 type | value | ✅ derivable (sub-gloss; POS) |
| 106 operation | event | ✅ derivable (the verb) |
| 104 seat · 108 manner · 109 intensity · 112 coupling · 113 prohibition | pair/flag | ✅ derivable (construct / prep-marker / *kol·me'od* / weld / negation) |
| 103 source · 105 bearer · 107 target · 110 specifier · 111 effect · 116 locus | pair | ⚠ partial (morph flags the slot; the binding + type need the read) |
| 115 **role** | value | ❌ **NOT derivable — requires the verse read** |
| 114 discovery | note | n/a (uncertainty channel, written during read-back) |

**Consequence:** a morphology pass can honestly build **8 dimensions reliably and approximate 6 more**, but it **cannot assign role or identify the characteristic**. Morphology gives the mechanical substrate; **meaning gives the characteristic and the role.**

## 3A. Derivation principles (how every dimension value is arrived at)
*(Absorbed 2026-07-08 from the retired `wa-lexical-analysis-rules-reset-v1` — the "parts → process" reframe that these dimensions obey. The reset is closed; these principles are its surviving core and are authoritative here.)* Every dimension value below is produced under these rules:

- **P0 — Measurement informs the eye; it never decides.** Count, co-occurrence, distribution and association strength surface candidates and show shape — they **never** gate a value's existence, inclusion, exclusion or validity. A phenomenon attested **once exists** (the singleton rule); nothing is recorded *because* it is frequent nor dropped *because* it is rare.
- **P1 — Observe, don't impose.** Record what the verse **states or implies**; never sort a span into a pre-decided category. Mechanical where the measure layer allows; else a grounded read; else `unresolved`.
- **Functional-first.** The primary record is **what the word DOES** in the verse (its relations and movements — cause, operation, object, manner, effect, transition, binding, direction), not what it *is*. Categories/patterns are **outcomes**, never inputs.
- **P4 — Three states per dimension** (= the catalogue's resolution states): **resolved** (a value the verse gives) · **none / silent** (the verse says nothing about it → **never impute**) · **unresolved** (the verse signals a value is expected but it can't be settled → goes to the worklist / discovery). **Silence ≠ unresolved.**
- **P5 — Citation.** Every resolved value cites the measure / word / clause that forced it — back-traceable by construction (aligns with §2 original-language grounding: read off lemma + morphology + tagged co-terms, never the English string).
- **P7 — Patterns emerge, held loosely.** Recurring functional shapes are named **when observed**, revisable, never a pre-set grid imposed up front.
- **P8 — Discovery-lookout is mandatory** (the emergence engine, dimension 114). Every read runs: *"what does this verse state or imply about the inner being that the current dimensions do NOT capture?"* A verse with nothing to flag records **discovery: none** (so we know it was looked for, not skipped). A flag that recurs becomes a new dimension and is **back-propagated** to all verses (§7 feedback). A flag pointing at an unseeded inner-being operation triggers the §5 discovery/promotion path.

## 4. STAGE 1 — Candidate seeding (Axis A, lemma-level, corpus-wide)
Purpose: **isolate the lemmas that *could* be a characteristic**, to seed the verse read. **Over-inclusive and non-exhaustive by design.**

Method (three layers, in order; only meaning-based routes are permitted):
1. **Registry direct match** — the lemma's English **gloss** equals a `word_registry` inner-being word (221 words), stemmed/normalised.
2. **Curated synonyms** — the gloss equals a **curated synonym** of a registry word (`research/discovery/registry-synonyms-curated-*.json`, reviewable/editable — the "dictionary"). Domain-curated, not generic thesaurus.
3. **IB judgement** — a broad inner-being semantic net over the still-unmatched lemmas, then a **manual accept/reject** (physical/object/agent/adverb false positives rejected; genuine inner-being lemmas accepted).
4. **Discovery** - is it likely that further characteristic seeding my be discovered when a verse is read and the lexical is built. This is a deliberate additional objective of a verse read when the lexical is revised or created. It will become evident when the different dimensions is being built in it is evident that the span is qualifying another IB phenomena that is not included as a candidate characteristic. This must not be confused with trying to elevate a qualifier to a characteristic. A word that operates as a qualifier is not a characteristic, but the discovery that the qualifies a IB related operation that is not set as a candidate in the morphology triggers a discovery and must elevated **Self-Learning**.

**Self-learning (mandatory):** when a verse read discovers a real characteristic the seed missed (e.g. *hear*→listen, H8085), or a false positive, **feed it back** — add the synonym / IB lemma (or prune it) in the curated dictionary, re-match the JSON, and **re-stamp the master**. The seed improves every cycle; it is never frozen.

**REJECTED routes (never use):** the registry `strongs_list` (matches every *co-occurring* strong — LORD→lust), and the 277 `characteristic` table (phrasal short_names → incidental-word noise — dwell→Security). Both match on **association, not meaning**.

Output: the lemma-inventory JSON (`char_matched` = registry/synonym; `ib_candidate` = judged) and the **`char_candidate` flag stamped on the master** (`verse_span_index.char_candidate` / `char_candidate_tag`), non-destructive (leaves `role` intact).

## 4A. STAGE 0 — Passage prerequisite (per book, before any read)
**No lexical is generated or updated outside the context of a passage.** Between the seed (§4, corpus-wide) and the read (§5, per verse) sits Stage 0: build the book's passages. Governed by **`wa-passage-completeness-rule-v2-20260708.md`** — read it as part of this cycle. Its essentials:

- **The candidate characteristic span is the heart of the passage.** IB-relevance is `char_candidate = 1` on the master, **not** the verse-record. A verse with no candidate carries nothing to read — it is outside every passage and is **never read**. We do not read whole chapters.
- **A passage = a maximal run of consecutive candidate-bearing verses.** It grows from the heart verse through its pre- and post- neighbours for as long as each neighbour also carries a candidate; the first non-candidate verse closes it. Anchor = first verse.
- **The verse-record is the entry/anchor, not the scope test.** A book is swept from its first verse-record verse; the passage then grows by candidate adjacency; then the sweep moves to the next unpassaged verse-record verse.
- **Integrity invariant (see §7A): every `char_candidate` span must have a verse-record.** A candidate without one is a **DB integrity violation** — restore the verse-record and its relations **first**, then passage and read.
- **The whole-book passage layout is designed up front, before any lexical read** — the passage ↔ verse-record ↔ master relationship is deterministic once `char_candidate` is stamped. Stage 0 outputs the complete start/finish list for the book; §5 then walks it, pulling the morphology of each whole passage before reading.

## 5. STAGE 2 — Building the lexical (the read; role is fixed inside it)
Stage 1 has flagged which lemmas *could* be characteristics. Stage 2 resolves each flagged occurrence by reading the verse, and in doing so produces the lexical. Role is not settled beforehand and is not a separate step: it is dimension 115, fixed **as the decomposition is made**. This is one stage, not two.

**Precondition (hard).** No verse is read until its passage exists (Stage 0, §4A) and every candidate in that passage has a verse-record (the integrity invariant, §7A). The read walks the passage list Stage 0 produced; it never starts a passage that is unbuilt or that still has an unresolved candidate-without-record.

**Unit and reading frame.** The unit of work is a single candidate char-lemma in a single verse. A verse carrying several candidate char-lemmas is worked once per char-lemma and yields one lexical each (§0). The verse is always read together with its passage — the surrounding run of consecutive verses, treated according to genre — because source, target, bearer and the wider movement resolve only in that context, not in the clause alone.

**Reading discipline — CHAR-DRIVEN, not span-sweep (authoritative, 2026-07-09).** Whether the reading unit is a passage (collection of verses) or a genre-unit (a whole poem), the discipline is the same:
1. **The characteristic is the lens.** Work **one char at a time** — take the char and read *for it*.
2. **Resolve that char's pairs by reading across the passage/section, using the morphology of the related verses.** The char's counterparts (its object/target, source, bearer, seat, manner, coupling…) are found by reading the passage *for this char*, grounded in the related verses' morphology.
3. **It is NOT** a general decomposition of all the spans of all the verses followed by pairing them up. Pairs are **read for the char**, never auto-assembled by proximity from a span-sweep. (A span-sweep + proximity-pairing is precisely what produced the earlier defective auto-pairs.)
Every pair endpoint is a **span-id** (§7A), resolved by this char-driven read.

**Screen 0 — IB-relevance (mandatory, BEFORE role; God is the arena, not the subject) (authoritative, 2026-07-09).** The lens is the **human inner being**. Before deciding a candidate's role, ask the prior question: *is this span about the human inner being at all?* God's own **attributes, qualities and actions are not characteristics** — his `chesed`, `emunah`, `kavod`/`hadar`, his righteousness/goodness, his wrath (`aph`), his saving/redeeming/judging acts. God enters analysis only as a **source (D3)**, a **target (D7)**, or a **quality/manner** bearing on a human char. So:

- span whose bearer/subject is a **human** inner faculty, state, disposition or inner-driven act (the psalmist, the wicked, mankind) → passes the screen → proceed to the role test (step 1);
- span that is **wholly God's** (his attribute/quality/action, no human inner content) → **fails the screen → qualifier**. It carries no lexical of its own; it is captured as the **source (D3)**, **target (D7)** or **quality** of the human IB char it works on. **A qualifier only operates ON a characteristic — so a God-qualifier is never standalone.** For it to be recorded, the human IB char it impacts must be found — read **across the passage**, not just the clause (God's acts typically ground a disposition an adjacent verse names: his acting grounds *trust*, his upholding grounds the righteous's *security*, his laughing at the wicked grounds the reader's *fret-not*). If a God-span appears to attach to nothing, the **passage is mis-scoped — widen it** until the IB char it impacts appears. A verse of pure God-content yields **no characteristic of its own**, but its God-span still attaches as a qualifier to the IB char of its passage; **we never manufacture a characteristic for God, and we never leave a God-act as a free-standing characteristic or standalone.**
- the human's **response to God** (trust, fear, hope, love, take-refuge, rejoice, cry, wait; the soul/heart/spirit) **is** IB — it passes, with God as its target/source.

Consequence for scope: after Screen 0, the reading is anchored on the surviving **human** IB chars only. Build each such char's **passage** (its related verses) and read *those together* (§4A) — **never** the whole chapter or a chapter-block. A candidate that fails Screen 0 is demoted (§ *Demotion* below), not read as a characteristic.

**Procedure, for each candidate char-lemma that passes Screen 0:**
1. Establish what the lemma *does* in this verse. Read the clause within its passage and decide whether the lemma here expresses an inner-being operation (it does or says something about the inner being itself), or only names/qualifies the object, source or circumstance of some *other* operation, or stands clear of any inner-being operation. This settles its role:
   - operative inner-being operation → **characteristic** — go to step 2;
   - relational to another operation → **qualifier** — no lexical of its own; it will be captured under the characteristic it serves (step 2 of that characteristic); move to the next char-lemma;
   - clear of any operation → **standalone** — no lexical; move on;
   - genuinely undecidable → **undecided** — record why in the discovery dimension and leave it on the worklist.
2. For a confirmed characteristic, decompose it across the sixteen dimensions (§3). Take the mechanical dimensions from the morphology — building them where the span has no lexical yet, correcting them where it carries a legacy one — and read the relational dimensions (source, target with object-type, bearer, seat, manner, intensity, coupling, effect, specifier, locus, prohibition) from the verse and passage. Wherever a dimension's value is another span in the verse, store it as a pair (`from_span → to_span`); that span is now a member of this characteristic's lexical.
3. Let the other spans' roles follow from step 2. Any span drawn into this characteristic as one of its dimensions is a **qualifier** of it. Once every characteristic in the verse is decomposed, any real-strong span not drawn into any of them is **standalone**. Roles are the by-product of the decomposition, never a separate labelling pass.

**Two departures from the seed the read must make** (the seed guides, it does not decide):
- *Discovery (§4.4).* If a qualifier is found to qualify an inner-being operation that is **not** among the seeded candidates, that operation is a characteristic the seed missed: raise it to a characteristic, build its lexical, and return the lemma to the seed (§7). This does **not** promote the qualifier — the qualifier remains a qualifier; it is the *operation it points at* that is now recognised.
- *Demotion.* A seeded candidate that proves, in this verse, to be only relational is set to qualifier or standalone. Being flagged by the seed never forces a span to characteristic.

## 6. Where each role lives, and when a verse is complete
*(the second half of STAGE 2)* The four roles are not interchangeable; each has one home in the data, and producing all four correctly is what "the verse is done" means.

- **characteristic** — holds a full sixteen-dimension lexical. It keeps this role even when it also appears as a dimension of another characteristic; it remains a characteristic in its own right and is nobody's qualifier (the two-axes rule, §2: in "he set his heart on wisdom", *wisdom* has its own lexical **and** is the target within the heart-setting's decomposition).
- **qualifier** — holds no lexical of its own. It exists only *inside* the characteristic it serves, as the span on the far side of a dimension pair — that characteristic's object, source, seat, bearer, manner, instrument or outcome. It is fully recorded there and stays traceable; giving it no lexical never means discarding it. A relational-looking span that attaches to no characteristic in the verse is standalone, not qualifier.
- **standalone** — holds nothing: no lexical, no dimensional membership. Function words, and any span no characteristic in the verse reaches.
- **undecided** — holds no lexical yet; its reason sits in the discovery dimension and it stays on the worklist for a later read.

A verse is complete when every real-strong span carries exactly one of the four roles, every characteristic carries its full lexical, and every qualifier is captured as a pair member within at least one of those lexicals — with nothing the read touched left unassigned. Each span's role is then written back to the master (§7), which is what makes this completeness auditable. A verse may hold several characteristics, and one span may be captured within more than one of their lexicals.

## 7. STAGE 3 — Write-back, feedback & re-stamp
**Write-back (the completeness ledger).** On completion of the lexical generation/revision, the role of **every span in the verse** is written back to the master (`verse_span_index.role`) — not only the characteristics but **all** four states: `characteristic`, `qualifier`, `standalone`, `undecided`. This is what makes the work **auditable and back-trackable from the master alone**: because every element of a read verse carries a role, any span still `role IS NULL` marks a verse (or a span within it) not yet accounted for. The read-derived role **supersedes** the legacy backfill; `char_candidate` is left in place as the seed provenance, so the master shows both what was *flagged* (`char_candidate`) and what the read *decided* (`role`).

**Feedback / self-learning.** Every read that finds a seed miss (a discovered characteristic, §5) or a false positive updates the curated dictionary / IB set, re-matches the seed JSON, and **re-stamps** the master `char_candidate`. Record the change. The cycle is self-correcting — the seed tightens with each pass, and the master stays a complete, queryable account of every span.

## 7A. DB updates & index maintenance (the integrity ledger)
**There are no triggers on `ve_lexical`, `verse_span_index`, `verse`, or `verse_evidence_index` — every table update is manual and is the read's responsibility.** A verse read is not complete until all of these are written. This is the concrete form of "all related tables updated, DB integrity maintained".

| # | table · column | what the read writes | when |
|---|---|---|---|
| 1 | `ve_lexical` (`verse_span_id` → master, `ve_nr` 101–116, pairs) | create/revise the 16-dimension rows for each characteristic + its pairs | core of the read (§5) |
| 2 | `verse_span_index.role` (+ `role_provenance`, `role_set_at`, `role_source_ve_id`) | write back **every** span's role — all four states | on completion (§7) |
| 3 | `verse.process_marker` | mark the verse read (completion ledger) | on completion |
| 4 | `verse_span_index.char_candidate` / `char_candidate_tag` | re-stamp on self-learning (seed change) | Stage 3 feedback (§7) |
| 5 | `verse.passage_id` / `is_passage_anchor` / `genre` | **prerequisite** — set by Stage 0 *before* the read | Stage 0 (§4A) |
| 6 | `verse_span_index.characteristic` | write the **read char in words** onto the master (the `ve_nr=101 sense` value) for every `role='characteristic'` span — the char lives on the master, not only in the lexical (integrity I11) | on completion (§7) |
| 7 | `verse_span_index.ib_char_id` | link every char-span to its normalised `ib_characteristic` record (§7D; integrity I7) | Stage 3, on book close |
| — | `verse_term_index`, `verse_morphology`, `verse_span_index` *rows* | **not written** — derived from morphology, upstream of this cycle | — |

**The integrity invariant (candidate ⇒ verse-record).** Every `char_candidate = 1` master span **must** resolve to an active `wa_verse_records` (via `verse_span_id`) with its term (`mti_terms`) and links intact. A candidate **without** a verse-record is a **DB integrity violation**, not a coverage gap: **halt the passage, restore the verse-record and all its relations first** (engine onboarding / per-book gate-1 corrective path), then read. This is the invariant Stage 0 (§4A) enforces before passaging.

**Keys and propagation.** Everything joins on the **master span `id`** (equivalently `verse_id,word_index`), **never on the strong** (the strong repeats within a verse and across the corpus). The passage is carried **only** by `verse.passage_id`; `ve_lexical` / `wa_verse_records` / `verse_span_index` carry no passage column and inherit it automatically — so a passage change never needs a downstream rewrite.

**`verse_evidence_index` is deprecated for lexicals (Decision 1).** Its `lexical` entries are 100% stale (they point at pre-M63 archived `ve_lexical` ids; 0 resolve to a live row). This cycle **does not read or maintain it** — forward/back tracking is done directly on the master (`role`, `char_candidate`, `verse_span_id`) and `ve_lexical`. If it is ever to become the canonical evidence ledger it needs a separate rebuild; that is out of scope here.

## 7B. Transition & changeover (legacy → read-derived)
Two legacy layers coexist with the read output and must change over cleanly, **per book**:
- **Roles:** `verse_span_index.role` currently holds the **M64 backfill** (old `ve_nr=115` roles, ~50% wrong). The read **overwrites** these verse-by-verse (§7).
- **Lexicals:** live `ve_lexical` holds the mechanical/legacy rows (incl. the NULL-pair mechanical pass); `ve_lexical_legacy` is the archived pre-M63 set. The read **revises** the live rows for a characteristic, or builds them where missing.

**Two-state model.** A span/verse is in exactly one of two states: **legacy (untrusted)** until its verse is read, or **read-derived (authoritative)** once its lexical is built, roles are written back, and `verse.process_marker` is set. Mark the change on the master with **`role_provenance = 'read-2026'`** (Decision 2) so a query can always separate trusted read-derived roles from the untrusted backfill during the multi-book changeover. `char_candidate` is left in place as seed provenance — the master then shows both what was *flagged* (`char_candidate`) and what the read *decided* (`role` + `role_provenance`).

**The completeness ledger.** `role IS NULL` on any real-strong span ⇒ that verse is not yet read. Combined with `role_provenance`, the master alone answers "what is done, and is it trusted?" — no side ledger needed.

**Changeover order.** Per book, never across books; mark each read verse `role_provenance = 'read-2026'`. First tranche: **Psalms + Proverbs 1–6** (already partly worked), then outward by book.

## 7C. Pipeline dependencies, DB updates per intervention, and the definition of completion
**The ordered pipeline (each step gates the next).**
`Stage 1 seed (corpus-wide) → Stage 0 passage build (per book) ─[integrity gate: verse-record fix]→ Stage 2 lexical read (per passage) → Stage 3 write-back → completion verify`.
No step may begin before its predecessor is complete for that scope: no passage is built on an unstamped seed; no verse is read until its passages are built **and** every candidate in it has a verse-record; no verse is marked complete until Stage 3 write-back is done. The four interventions below are exactly the points where the DB changes.

**(a) Verse-record fix — integrity repair, triggered inside Stage 0 when a candidate has no verse-record.**
Trigger: a `char_candidate = 1` master span with no active `wa_verse_records` (via `verse_span_id`). Restore via the engine onboarding / per-book gate-1 corrective path. Expected DB end-state:
- `mti_terms` — the term exists, status-clean, owned (`owning_registry_fk` set); created/restored where OT-DBR-009 over-deleted it.
- `wa_term_inventory` — the term-in-file row exists with `term_owner_type` (OWNER/XREF).
- `wa_verse_records` — an **active** row (`delete_flagged = 0`) for the (reference, term) with `verse_span_id` → master span, plus `verse_id`, `mti_term_id`/`term_id`, `word_registry_fk`, `span_strong_match` set.
- master `verse_span_index` rows are **not** created here — they are morphology-derived; the fix links a record *to* an existing span.
Gate: 0 candidates in the passage without a verse-record. Only then does the passage proceed.

**(b) Passage preparation — Stage 0, per book, precomputed (passage rule v2).**
Writes: `passage` (one row per reading unit — `anchor_verse_id`, `start_*`/`end_*`, `ref`, `verse_count`, `source='passage-build-2026'`); `verse.passage_id` for every verse in each run; `verse.is_passage_anchor` on each anchor; `verse.genre` set/confirmed.
Not written: `ve_lexical`, `wa_verse_records`, `verse_span_index` — no passage column; they inherit via `verse.passage_id`.
Gate: 0 candidate-bearing verses with `passage_id IS NULL`; 0 `char_candidate` without a verse-record (all (a) fixes done).

**(c) Lexical completion — Stage 2 read + Stage 3 write-back, per verse in the passage.**
Writes: `ve_lexical` — 16-dimension rows (`ve_nr` 101–116) for each characteristic + its pairs (`from_span/to_span/resolution/pair_kind`), `verse_span_id` → master, `delete_flagged=0` (legacy rows revised or superseded); `verse_span_index.role` (+ `role_provenance='read-2026'`, `role_set_at`, `role_source_ve_id`) for **every** real-strong span (all four states); `verse.process_marker` set when the verse is done; `verse_span_index.char_candidate`/`char_candidate_tag` re-stamped **only** on self-learning, then re-match the seed JSON.

**(d) Definition of completion, and how it is verified.** Completion is defined and checked at three nested levels; each is an integrity-gated **query**, never a judgement:

| level | complete when (all hold) | verification |
|---|---|---|
| **verse** | every real-strong span has exactly one `role`; every characteristic span has its full `ve_lexical`; every qualifier is a pair member in ≥1 lexical; `process_marker` set; roles carry `role_provenance='read-2026'` | no span in the verse with `role IS NULL`; each `role='characteristic'` span has ≥1 active `ve_lexical` row |
| **passage** | every verse in it is verse-complete; every candidate in it has a verse-record | verse-incomplete count = 0; `char_candidate` without verse-record = 0 |
| **book** | every candidate-bearing verse is in a passage; every passage complete | `char_candidate=1 AND passage_id IS NULL` = 0; `char_candidate=1 AND` no-verse-record = 0; any candidate-bearing verse holding a `role IS NULL` span = 0 |

Governance: every intervention is backed up and integrity-gated (`_check_integrity_controls --snapshot` pre → apply → post → `--compare`); the **book-level** checks are the changeover **acceptance test** — a book is not marked read until all its counts are 0.

**The validations are the I1–I11 set** in `wa-db-integrity-definition-authoritative-v1-20260711.md` — that is the *one* validation set; the queries above are those invariants. Book-close must pass **all of I1–I11**, which includes, beyond the verse/passage checks above: **I2** every char-span has a `wa_verse_records`; **I7** every char-span has an `ib_char_id`; **I10** every `role='characteristic'` span has `char_candidate=1`; **I11** every char-span has `verse_span_index.characteristic` populated.

## 7D. STAGE 3 (book close) — the normalised characteristic index (`ib_characteristic`)
After a book's verses are read and written back, build/refresh the normalised index so the many per-span characteristic instances roll up to the recurring characteristics they belong to.

> **v3 (2026-07-11) — MEANING-KEYED, not lemma-keyed.** The original lemma-grain (base Strong's) was found to **merge distinct meanings of one word** (halal → praise + boast + deride under one record; gur → sojourn + strife). Investigation established (a) the lemma is only an identifier, not the meaning; (b) `stem` helps but is insufficient (one form can carry two senses); (c) the read-sense field `ve_nr 101` is often a *contextual phrase*, not the word's meaning, so it over-splits. **The true meaning-in-context is carried by the ESV rendering**, cross-checked by stem/morph/attested-gloss. Builder: `scripts/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py`.

- **Grain (identity):** one record per **(base-lemma, normalised-ESV-rendering)** = the word in *one meaning*. `char_key = "{lemma}:{normalised_esv}"`; `name` / `key_word` = the modal raw ESV word (readable). This separates praise from boast/deride, and sojourn from strife — the ESV even splits homographs that `stem` alone cannot.
- **Evidence columns (mandatory, so any grouping is auditable and no bad merge is hidden):** `stems` · `morph_codes` · `esv_words` (distinct renderings) · `lexical_gloss` (the attested sense-inventory from `mti_terms` for the base lemma — the dictionary English of the Hebrew) · `read_sense_variants` (the read `ve_nr 101` phrases, **preserved** — the contextual reads are never lost). Plus `key_span_id` · `operation` (modal 106) · `ledger` · `instance_count` · `family` (nullable — later cross-characteristic grouping) · `status` · `provenance = ib-char-index-v3-meaning-keyed-2026` · `book_scope`.
- **Normalisation** of the ESV key: lowercase, strip non-alpha, collapse doubled artifacts ("soul soul"→soul), light inflection strip + silent-e fold (praise/praised/praises → one). Errs toward **over-split (safe)**, never over-merge. Known residue: irregular inflections (keep/kept) and multi-word ESV targets ("give thanks to") leave near-duplicate records — flagged by shared evidence, mergeable in a later canonicalisation pass. **Never in the key:** the free-text read-sense phrase (it is contextual, not lexical) or the bare lemma (it merges meanings).
- **Link:** set `verse_span_index.ib_char_id` on every char-span to its record (integrity **I7**).
- **Source:** built **from the master + the lexical + the verse-record morphology** (no new reading) — `verse_span_index` char-spans × `ve_lexical` 101/106 × `wa_verse_records` stem/morph/target_word × `mti_terms` gloss. Legacy pre-read rows and the superseded v2 records are archived to `ib_characteristic_legacy` / exported to `verse-analysis/psalms/_model/ib_characteristic_v2_*` before rebuild (reversible).
- **Runs on every book**, idempotent per `book_scope`. Validation (must all be 0): char-spans with NULL `ib_char_id`; char-spans → dangling record; records with no linked span.

## 8. THE WORKLIST — how to scope work per book (critical)
**The raw "missing lexical" count is NOT the worklist — it massively overstates the work.** Most missing-lexical spans are function words (need nothing) or objects (captured by a characteristic's dimensions). The worklist is defined on **candidates**:

- **Missing-lexical worklist** = `char_candidate = 1 AND has no active ve_lexical`. *(Ch7 example: 2, not 28. Proverbs: ~40, not 696.)*
- **Incorrect-lexical worklist** = spans whose existing role/lexical disagrees with the read — operationally, start from `role = 'characteristic' AND char_candidate = 0` (roled characteristic but the seed does not flag → suspect over-call) **and** candidate spans carrying a known-imperfect legacy lexical.

Drive the per-book pass off these two, **never** off raw span counts.

## 9. Order, granularity, integrity
- Work **per book**, never across books. Within a book, by passage/chapter. Read **verse + passage** before setting any role.
- Every DB write is **integrity-gated** and backed up. Tracking is **by index/FK** (`char_candidate`, `role`, `verse_span_id`), never by text-scanning.
- Existing roles/lexicals are the **known-imperfect legacy** (~50% of old roles wrong) — a working surface, overwritten by this cycle's read, never trusted as-is.

## 10. Data & schema anchors
- Master: `verse_span_index` — `role` (M64), `char_candidate`/`char_candidate_tag` (M65), **`characteristic`** = read char in words + **`ib_char_id`** = link to the normalised index (M66).
- Per-span lexical: `ve_lexical` (`ve_nr` 101–116; pair columns `from_span/to_span/resolution/pair_kind`).
- Normalised index: **`ib_characteristic`** (§7D) — one record per characteristic word; `ib_characteristic_legacy` = archived pre-read rows.
- Seed artefacts (`verse-analysis/psalms/_model/`): `lemma-inventory-master-no-particles-*.json` (the seed), `registry-synonyms-curated-*.json` (the dictionary — reviewable), `ib-judgement-*`, `char-seed-extension-read-emergent-*.json` (self-learning feedback record, §7).
- Master-index → term/verse-record onboarding: see `wa-term-add-update-AUTHORITATIVE-pipeline-v1` (the ONLY way to add/update a term). Retired: `new_word.py` (deleted). Validations: `wa-db-integrity-definition-authoritative-v1` (I1–I11).

## 11. The non-negotiable rules (the "do-not-mess-up" checklist)
0. **Screen 0 first (§5): the lens is the HUMAN inner being. God is arena, not subject.** God's own attribute/quality/action → **qualifier** (source/target/quality), never a characteristic. **A qualifier operates ON a characteristic — so a God-qualifier is never standalone; the human IB char it works on must be found (read across the passage).** A verse of pure God-content yields **no** characteristic of its own — do not manufacture one — but its God-span still attaches as a qualifier to the IB char of its passage. Anchor on human IB chars and read each char's **passage** — never a whole chapter or chapter-block.
1. Characteristic by **meaning in the verse**, never by lookup. Lists **validate**, never impute.
2. Role ∈ {characteristic, qualifier,standalone, uncertain}. **qualifiers always pair with a characteristic**
3. Relational words (object/source/seat/manner) are **qualifiers** — and are **captured, never dropped**.
4. Seed = Axis A (lemma, over-inclusive, corpus-wide); role/dimension = Axis B (per-verse). **Never conflate.**
5. Seed is a **filter, not a verdict** — the read overrides it **both** ways, and misses feed back.
6. **Only characteristics get their own lexical.** Function words get nothing.
7. **Worklist = candidate spans missing/wrong lexical**, never raw missing-lexical counts.
8. Morphology gives the mechanical dimensions; **role and characteristic identity need the read.**
9. Per book only; integrity-gated; index-tracked; legacy = untrusted working surface.
10. Every cycle is **self-correcting** — improve the seed, re-stamp, record.

*Filed 2026-07-08. Authoritative for the characteristic→candidate→role→lexical cycle. Supersedes prior attempts on this sub-process.*
