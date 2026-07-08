# Characteristic → Candidate → Role → Lexical — AUTHORITATIVE CYCLE INSTRUCTION (v1)

> **Status: AUTHORITATIVE. This is the single governing instruction for how the study determines characteristics, seeds candidates, sets roles, and generates lexicals.** It **supersedes all prior attempts** at this sub-process — including the qualifier-as-a-role framing, the per-span role-reassessment method, the strongs-list / 277-table candidate attempts, and any earlier "characteristic determination" notes. Where any older document conflicts with this on *characteristic identity, role, candidacy, or lexical generation*, **this document wins.** It does **not** replace the study's foundations (scripture-as-data, the master-index architecture, the dimension catalogue mechanics) — it sits on top of them and makes the cycle unambiguous. Set 2026-07-08.

---

## 0. Why this exists
The characteristic/role/lexical question has been mis-understood and re-attempted many times, each partial, each drifting. The recurring errors were: (a) treating a *role* as a fourth thing ("qualifier") when it is really a dimension; (b) matching candidates on incidental association (co-occurring strongs, phrasal characteristic-names) instead of meaning; (c) treating raw "missing lexical" counts as the worklist; (d) letting the seed act as a verdict instead of a filter; (e) trying to derive *role* from morphology. This instruction fixes all five and defines the cycle end-to-end.

## 1. The object and the definitions (fixed vocabulary)
- **Characteristic** = an inner-being disposition/faculty/operation that the verse (in its passage) *turns on* — decided by the **use and meaning of the span in the verse/passage**, and that it does/says something about the inner being. **Never** by a lookup table; the registry/lists only *validate* (verse→list), they never *impute*.
- **Master index** (`verse_span_index`) = the term-verse-span substrate: one row per morphological word, built 1:1 from `verse_morphology`. A span is **uniquely** identified by its `id` (equivalently `verse_id,word_index`). **The strong is NOT unique** — it repeats within a verse and across the corpus — so everything keys on the **span id**, never on the strong.
- **Role** — the per-span classification, restricted to **exactly**: `characteristic` · `standalone` · `uncertain`. **"qualifier" is RETIRED as a role.** A word that elaborates, qualifies, or names an object/source is **not a characteristic and gets no role** — it is carried by its **dimension** (§3). `uncertain` = the read could not decide (write the reason to the discovery dimension).
- **Standalone** = a span that is neither a characteristic nor a dimensional member of any characteristic in its verse (binds to nothing). Function words (particles, prepositions, connectives, pronouns) are standalone.

## 2. The TWO ORTHOGONAL AXES (the distinction that removes the confusion)
Everything in this cycle is one of two independent questions. Do not conflate them.

- **Axis A — Is the *lemma* a candidate characteristic?** A **lemma-level, corpus-wide** property. Answered by the **seed** (§4). Over-inclusive on purpose. This is `char_candidate` on the master.
- **Axis B — In *this occurrence*, what role/dimension does the span fill?** A **per-verse** property. Answered only by the **lexical read** (§5–6). This is `role` + the dimension pairs.

A word can be **both** — e.g. "he set his heart on *wisdom*": *wisdom* is a characteristic **and** the target of the heart-setting. Axis A candidacy never overrides Axis B; Axis B never rewrites Axis A. `char_candidate` and `role` are **different columns for different questions**.

## 3. The 16 dimensions (per-span) and what morphology can give
Every span is described across the 16 per-span dimensions (`ve_lexical`, `ve_nr` 101–116). A dimension value is a **VALUE**, a **PAIR** (`from_span → to_span`, with `resolution`), an **EVENT**, or a **FLAG**. **Relational person/thing words (objects/sources/seats) live here as pair members — that is why they need no role.**

| ve_nr | dim | from morphology? |
|--:|---|---|
| 101 sense · 102 type | value | ✅ derivable (sub-gloss; POS) |
| 106 operation | event | ✅ derivable (the verb) |
| 104 seat · 108 manner · 109 intensity · 112 coupling · 113 prohibition | pair/flag | ✅ derivable (construct / prep-marker / *kol·me'od* / weld / negation) |
| 103 source · 105 bearer · 107 target · 110 specifier · 111 effect · 116 locus | pair | ⚠ partial (morph flags the slot; the binding + type need the read) |
| 115 **role** | value | ❌ **NOT derivable — requires the verse read** |
| 114 discovery | note | n/a (uncertainty channel, written during read-back) |

**Consequence:** a morphology pass can honestly build **8 dimensions reliably and approximate 6 more**, but it **cannot assign role or identify the characteristic**. Morphology gives the mechanical substrate; **meaning gives the characteristic and the role.**

## 4. STAGE 1 — Candidate seeding (Axis A, lemma-level, corpus-wide)
Purpose: **isolate the lemmas that *could* be a characteristic**, to seed the verse read. **Over-inclusive and non-exhaustive by design.**

Method (three layers, in order; only meaning-based routes are permitted):
1. **Registry direct match** — the lemma's English **gloss** equals a `word_registry` inner-being word (221 words), stemmed/normalised.
2. **Curated synonyms** — the gloss equals a **curated synonym** of a registry word (`outputs/data/registry-synonyms-curated-*.json`, reviewable/editable — the "dictionary"). Domain-curated, not generic thesaurus.
3. **IB judgement** — a broad inner-being semantic net over the still-unmatched lemmas, then a **manual accept/reject** (physical/object/agent/adverb false positives rejected; genuine inner-being lemmas accepted).

**REJECTED routes (never use):** the registry `strongs_list` (matches every *co-occurring* strong — LORD→lust), and the 277 `characteristic` table (phrasal short_names → incidental-word noise — dwell→Security). Both match on **association, not meaning**.

Output: the lemma-inventory JSON (`char_matched` = registry/synonym; `ib_candidate` = judged) and the **`char_candidate` flag stamped on the master** (`verse_span_index.char_candidate` / `char_candidate_tag`), non-destructive (leaves `role` intact).

**Self-learning (mandatory):** when a verse read discovers a real characteristic the seed missed (e.g. *hear*→listen, H8085), or a false positive, **feed it back** — add the synonym / IB lemma (or prune it) in the curated dictionary, re-match the JSON, and **re-stamp the master**. The seed improves every cycle; it is never frozen.

## 5. STAGE 2 — Role determination (Axis B, per-verse, in the read)
Done **only by reading the verse and its passage** (genre-aware; a passage = a maximal run of consecutive verses). For each candidate span, and with freedom to look beyond the candidates:
- **Confirm** → `role = characteristic` (the span is the operative inner-being disposition here), **or**
- **Demote** → `role = standalone` (in this verse it is an object/source/manner of something else, or binds to nothing), **or**
- **`uncertain`** → could not decide; record why in the discovery dimension.

Two overrides the read **must** be free to make (the seed is a filter, not a verdict):
- **Upward** — mark a characteristic the seed did **not** flag (then feed it back, §4).
- **Downward** — demote a seeded candidate that is an object/source in this verse.

## 6. STAGE 3 — Lexical generation (only for confirmed characteristics)
- **Only a characteristic gets its own lexical.** Standalone spans and function words get **no lexical**.
- A characteristic's lexical is the **dimensional read**: build D1 (mechanical, from morphology) and then the pairs — **source, target (with object-type), seat, bearer, manner, intensity, coupling, effect, prohibition** — by reading the verse/passage.
- **Relational person/thing words are captured *here*, as the `to_span`/`from_span` of the characteristic's pairs** — not as their own lexical, and **never ignored.** "Doesn't need its own lexical" must never become "dropped." If a nearby object binds to *no* characteristic, only then is it standalone.
- Morphology seeds the mechanical layer; the **read** supplies role, the characteristic identity, and the pair bindings.

## 7. STAGE 4 — Feedback & re-stamp
Every read that finds a seed miss or false positive updates the curated dictionary / IB set, re-matches the JSON, and re-stamps the master `char_candidate`. Record the change. The cycle is **self-correcting**.

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
- Master: `verse_span_index` — `role` (M64), `char_candidate`/`char_candidate_tag` (M65).
- Per-span lexical: `ve_lexical` (`ve_nr` 101–116; pair columns `from_span/to_span/resolution/pair_kind`).
- Seed artefacts (`outputs/data/`): `lemma-inventory-master-no-particles-*.json` (the seed), `registry-synonyms-curated-*.json` (the dictionary — reviewable), `ib-judgement-*`.
- Scripts: `_apply_add_role_to_master_index_*` (role column), `_apply_stamp_char_candidate_on_master_*` (seed → master; idempotent, re-run after any seed change).

## 11. The non-negotiable rules (the "do-not-mess-up" checklist)
1. Characteristic by **meaning in the verse**, never by lookup. Lists **validate**, never impute.
2. Role ∈ {characteristic, standalone, uncertain}. **No "qualifier" role.**
3. Relational words (object/source/seat/manner) are **dimensions, not roles** — and are **captured, never dropped**.
4. Seed = Axis A (lemma, over-inclusive, corpus-wide); role/dimension = Axis B (per-verse). **Never conflate.**
5. Seed is a **filter, not a verdict** — the read overrides it **both** ways, and misses feed back.
6. **Only characteristics get their own lexical.** Function words get nothing.
7. **Worklist = candidate spans missing/wrong lexical**, never raw missing-lexical counts.
8. Morphology gives the mechanical dimensions; **role and characteristic identity need the read.**
9. Per book only; integrity-gated; index-tracked; legacy = untrusted working surface.
10. Every cycle is **self-correcting** — improve the seed, re-stamp, record.

*Filed 2026-07-08. Authoritative for the characteristic→candidate→role→lexical cycle. Supersedes prior attempts on this sub-process.*
