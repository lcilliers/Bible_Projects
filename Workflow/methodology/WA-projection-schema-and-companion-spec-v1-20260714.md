# WA — Projection: definitive column schema + companion reading-spec (v1, 2026-07-14)

- **Responds to:** `WA-projection-spec-1.2` + researcher direction (2026-07-14).
- **Governing decisions (researcher):** (a) everything here — relabel, 114 content-fix, the projection — is done **for both Psalms AND Proverbs now**, then **built into the system for the next books**; (b) the companion is the **technical data layer for the book**, not merely an edge-list; (c) I define the columns from deep DB knowledge and **backtrack to the spec** + assess completeness.
- **Grounding:** queried the live DB — **4,137 read-2026 characteristics** (Psalms 2,168 + Proverbs 1,969), **4,154 span-id relational edges**, reread dimensions **{101-108, 112-116}**.

---

## A. The two open questions — answered

### (b) Does the "discovery" want of v1.2 need a NEW dimension, or is it already there?
**It is already there — no new prose dimension is needed.** The discovery/lookout content the spec's name implies (the *surfaced finding* — "this is a physical outcome, **not** an IB operation", "the finding is…", "the summit and root of it all") **already lives inside ve_nr 114**, which the reads made the *evidence-anchored lexical note*. The correct action is:
1. **Relabel 114 → `reading`** (its true job) — content kept, applied to both books + the method.
2. **Elaborate in this companion spec** how `reading` carries evidence + finding (below).
3. Add a **lightweight derived `discovery_flag`** (present/absent) so an analyst can *filter to readings that surfaced a finding* — **derived from the `reading` text, not a newly authored dimension.**

So: the answer is "it's there; relabel + elaborate in the companion spec + a derived flag" — **not a new authored dimension.**

### (4) Are `object_kind` / `direction` the "additional dimension" of (b)?
**No — they are distinct, and not about discovery.** They refine the *movement*, not the *finding*:
- **`object_kind`** disambiguates `target` — *what KIND of thing the movement is toward* (`god / person / self / thing / abstraction / none`). **Derivable now** from `locus` + `target`/`bearer` text (reviewable rule).
- **`direction`** is the *vector of the movement* (toward-god / from-god / inward / outward / reciprocal / none). E4: direction may be *what constitutes* the movement. **A genuine gap — null in all reads** — so it is authored **going forward in the method** (and a light inference offered for the two existing books).

They are enrichments of the relational/movement model; the discovery question (b) is answered separately (above).

---

## B. The projection is TWO layers (per researcher direction (b))

1. **The READING VIEW** — analyst-facing, **one row per reading** (the v1.2 flat file, refined). For AI Chat to *read*.
2. **The TECHNICAL DATA LAYER** — the complete machine substrate for the book: **(i) nodes** (every char + all span/ib_char/verse fields), **(ii) edges** (the 4,154 span-id pairs — the movement graph), **(iii) dimensions-long** (the raw `ve_lexical` rows, for full fidelity/backtrack). Not just edges.

---

## C. READING VIEW — column schema (one row per reading)

`NONE` = `value='none'` (**reader looked, found none** — evidence of silence). `ABSENT` = no row for that ve_nr (**never read** — not evidence of silence). Applied to **every** dimension column.

### C.1 Identity & evidence (coded — zero read-budget)
| column | source | notes / backtrack to v1.2 |
|---|---|---|
| `reading_id` | `ib_characteristic.char_key` + occurrence | spec ✓ |
| `span_id` | `verse_span_index.id` | **the discriminator** (spec §1) ✓ |
| `book` / `chapter` | `verse.book_id` / `.chapter` | **new** (grouping) |
| `verse_ref` | `verse.reference` | spec ✓ |
| `corpus` | `verse.testament` (OT/NT) | **new** |
| `genre` | `verse.genre` | **new** (how to read) |
| `passage_id` | `verse.passage_id` | **new** — the reading frame (spec dropped `passage_ref`) |
| `anchor` | `verse.is_passage_anchor` | spec ✓ |
| `lemma` / `strongs` | `verse_span_index.strongs` / `primary_strong` | spec ✓ |
| `morph` | `verse_span_index.morph_code` | spec ✓ — **is in the DB (100%)**; the spec assumed it "does not travel" |
| `pos` | `verse_span_index.pos` | **new** |
| `stem` | `verse_span_index.stem` | binyan (partial, 48%) |
| `surface_en` | `verse_span_index.surface` | the **English ESV** word (spec's `hebrew_form` mislabels this) |
| `hebrew_form` | — | **GENUINE GAP** — not stored; derivable via STEP+morph; flag |
| `translit` | derived from `reading`/`sense` | spec ✓ (promote per §1); `translit_confidence` flag |
| `char_key` / `ib_char` | `ib_characteristic.char_key` / `.name` | spec ✓ — the **meaning-in-context identity** (the nuance grouping) |
| `base_gloss` | `ib_characteristic.lexical_gloss` | **new — the INVARIANT dictionary meaning of the lemma** (see §G) |
| `read_sense_variants` | `ib_characteristic.read_sense_variants` | **new — the set of verse-derived nuances this identity spans** (see §G) |
| `esv_words` / `stems` / `morph_codes` | `ib_characteristic.*` | **new** — aggregated forms behind the identity |
| `family` | `ib_characteristic.family` | spec ✓ |
| `cluster` / `cluster_all` | `verse_span_index.cluster` / `ib_characteristic.cluster_all` | spec ✓ (+all) |
| `same_as` | readings sharing `char_key` | spec ✓ |
| `role_provenance` | `verse_span_index.role_provenance` | **new** (read layer) |
| `char_candidate_tag` | `verse_span_index.char_candidate_tag` | **new** — emergent/orphan/seeded (which the old model missed = a finding) |
| `lemma_freq_book` | COUNT readings of lemma in book | **new** (salience: major vs minor char) |
| `ib_instance_count` | `ib_characteristic.instance_count` | **new** (corpus salience) |

### C.2 Dimensions (the 101-116 pivot)
| column | ve_nr | class | state | notes |
|---|---|---|---|---|
| `sense` | 101 | free | — | short sense summary |
| `type` | 102 | coded | — | small vocab (cognition/affect/disposition/action/state/…) |
| `source` | 103 | free | partial | Phase-2 for poetic; partial in reads |
| `seat` | 104 | coded | often NONE | |
| `bearer` | 105 | free | — | who bears the characteristic |
| `operation` | 106 | free | — | what it *does* in the verse |
| `target` | 107 | free | — | what it is toward/against |
| `object_kind` | derived | coded | — | **new** — god/person/self/abstraction/other/none (from locus+target+bearer) |
| `manner` | 108 | coded | often NONE | |
| `intensity` | 109 | coded/free | **NONE-or-value** | **★ ASSESSED FROM THE QUALIFIER, not ABSENT** — read the degree/modifying qualifier of the char (e.g. "greatly", "very", a doubled verb); write `none` if none. *(being reinstated — retrofit + bake-in.)* |
| `specifier` | 110 | free | **NONE-or-value** | **★ ASSESSED FROM THE QUALIFIER** — the narrowing qualifier that specifies *which* (e.g. "of the LORD", "this"); `none` if none. |
| `effect` | 111 | free | **NONE-or-value** | **★ ASSESSED FROM THE QUALIFIER / outcome** — the result the char produces via its qualifier/consequence; `none` if none. *(also recorded at Phase-2 book level.)* |
| `coupling` | 112 | free + edge | — | the pairing **phrase**; the **edge** is in the technical layer |
| `prohibition` | 113 | coded | rare (9) | |
| `reading` | 114 | free | — | **RENAMED from `discovery`** — evidence-anchored note (translit + verse-quote + meaning + finding) |
| `discovery_flag` | derived | coded | — | **new** — does `reading` carry a surfaced finding? (present/absent) — answers (b) |
| `role` | 115 = `verse_span_index.role` | coded | — | characteristic/qualifier/standalone |
| `locus` | 116 | coded | — | internal:ib-state / external:god / external:person |
| `direction` | `ve_lexical.direction` | coded | **NONE-or-value** | **★ ASSESSED FROM THE MOVEMENT/pair** (toward-god / inward / outward / reciprocal); `none` if static. *(authored forward + retrofit.)* |

**★ Anti-`ABSENT` principle (researcher, 2026-07-14):** intensity/specifier/effect/direction must **never** be shown `ABSENT` (never-assessed) — that is misleading, because the qualifier/pair evidence to assess them is present. Part of the lexical read is to **perform these assessments from the qualifier spans and the pairs** and record `NONE` (assessed, none found) or the value. After the retrofit + method bake-in, `ABSENT` on these means only "a legitimately unreadable case", not "we skipped it".

### C.3 Evidence-on-tap
| column | source | notes |
|---|---|---|
| `verse_text` | `verse.verse_text` | **optional** — spec drops `passage_text`; a non-reading analyst wants the verse. Include as an opt-in column. |

---

## D. TECHNICAL DATA LAYER — the machine substrate

- **`nodes`** — one row per reading, every column in §C **plus** raw fields (`ib_char_id`, `role_set_at`, `word_index`, `verse_context_id`, provenance dates). The complete node.
- **`edges`** — one row per span-id pair (the movement graph, 4,154 rows): `from_span, to_span, edge_type` (coupling 112 / bearer 105 / target 107, where `resolution='span'`), `direction, pair_kind, phrase` (the value), `book, from_verse_ref`. **This is what makes movement analysis possible** — without it, `coupling` is only prose and the web cannot be built.
- **`dimensions_long`** — the raw `ve_lexical` reread rows (`verse_span_id, ve_nr, ve_label, value, from_span, to_span, resolution, pair_kind, source_provenance`) — full fidelity, for any check the pivot loses.

---

## E. Completeness & representativeness assessment (backtrack to v1.2)
- **Every v1.2 column is covered** (identity/evidence + all dimensions), with the corrections: `discovery`→`reading` (relabel), `hebrew_form` flagged as a genuine gap (surface is English), `morph` confirmed available (spec was wrong that it "does not travel").
- **v1.2's ABSENT dims — corrected diagnosis (researcher insight, 2026-07-14): they are DEGRADED, not redundant — a qualifier-reading gap.** The researcher observed that intensity/specifier/effect are naturally **derivatives of reading the QUALIFIER spans around a characteristic in context.** The DB confirms it:
  - The reread reads qualifiers only **relationally** — a `qualifier`-role span (2,428 in the two books) is captured as the **span-id endpoint** of a characteristic's *coupling(112)/source(103)/target(107)/manner(108)/seat(104)/bearer(105)/operation(106)*. This is the movement graph — a real gain.
  - But the **MODIFYING** qualifiers — **intensity** ("greatly", "very"), **specifier** (a narrowing "this/of-X"), **effect** ("so that…", the result) — are **not read into dimensions.** They fall to `standalone` and survive only inside the `reading` prose. **Worked case: Pro 23:24 "GREATLY rejoice"** — `rejoice` read as the characteristic, but **"greatly" (H1523, the intensity qualifier) sits `standalone`, unlinked** — its force noted in prose only.
  - So per dimension: **`intensity`(109)** and **`effect`(111)** are **degraded** — the modifying-qualifier read that would populate them was thinned (the evidence spans still sit there, `standalone`). **`specifier`(110)** — the old *content* was bibliographic/low-value (`"of David"`), but the *concept* (a qualifier that narrows the characteristic) is valid and qualifier-derived; "redundant" was an over-call. `effect` is also legitimately Phase-2 at book level.
- **Corrected projection decision:** keep 109/110/111/direction as **ABSENT columns** (the signal is information), **do not drop specifier** (it is a degraded concept, not redundant). The real fix is **methodological** (below): read the modifying qualifiers into structured dims / typed qualifier→char edges, so the projection can carry `intensity`/`specifier`/`effect` as filterable columns and the edge-list can carry `edge_type ∈ {intensity, specifier, effect}` alongside coupling/target/bearer.
- **Method forward (bake-in):** when a characteristic has a same-verse modifying qualifier (a degree adverb, a narrowing specifier, a result clause), **read it into the corresponding dimension AND link the qualifier span to the char** (as is already done for coupling/target). The data (the `standalone` modifying-qualifier spans) is already present — it needs the *reading* to connect it. Memory: `feedback_qualifiers_carry_modifying_dimensions`.
- **Added beyond v1.2** (so the analyst cannot claim "inconclusive for want of data"): the **edges** (movement graph), `genre`/`book`/`chapter`/`corpus`/`passage_id` (context), `char_candidate_tag`/`role_provenance` (provenance), `lemma_freq_book`/`ib_instance_count` (salience), `object_kind`/`discovery_flag` (derived), optional `verse_text`.
- **Gaps that remain, honestly flagged:** `hebrew_form` (not stored), `direction` (never read), `intensity`/`specifier`/`effect` (never read). None block the current analysis; all are marked, not silently blank.

---

## G. Base meaning vs verse-derived nuance — the distinction is PRESERVED (researcher check, 2026-07-14)

The flattening does **not** collapse the base lemma meaning into the contextual nuance. The reread's whole architecture (`project_term_is_sense_not_lemma`) rests on this distinction, and the projection carries it in **three explicit, analysable layers** — one row per reading, but the columns keep the layers apart:

| layer | what it is | column(s) | invariance |
|---|---|---|---|
| **1. Lemma (base)** | the dictionary word + its base gloss | `strongs` / `lemma`, **`base_gloss`** (`ib_characteristic.lexical_gloss`) | **INVARIANT** across every occurrence |
| **2. Meaning-in-context identity** | the derived nuance the lemma takes (grouping of like readings) | `ib_char`, `char_key`, **`read_sense_variants`** | varies **per nuance** — one lemma → many identities |
| **3. Occurrence (reading)** | this specific verse's reading | **`span_id`**, `sense`(101), `operation`(106), `reading`(114), `verse_ref` | varies **per verse** — the finest grain |

**Worked proof (live data): H3045 `yada`, `base_gloss = "to know"` — INVARIANT — fans into 14 meanings-in-context** across 54 readings: *know · teach (make-known/hiphil) · knowledge · known · considers · **regard/care** ("the righteous regards his beast's life") · **perceive** · **feel/insensible** ("the drunkard senseless even to blows") · confessed-ignorance (Agur).* All three layers sit side by side in the row, so the analyst can:
- **group by `lemma`** → see the whole fan-out of nuances of one word;
- **compare `base_gloss` vs the per-reading `sense`/`reading`** → measure how far the *context* pulls the word from its base (know → *feel/insensible* is a large pull; know → *known* is small);
- **compare readings that share an `ib_char`** (same nuance) → the finer within-nuance differences live in each `span_id`'s `sense`/`reading`.

Two readings of the same lemma with the same English nuance are **still distinct rows** (different `span_id`, `verse_ref`, `reading`) — the finest grain is never lost. The `NONE`/`ABSENT` codes further keep "the reader found the base sense unshifted here" distinct from "not read". **Nothing that distinguishes base meaning from verse-derived nuance is flattened away.**

*(Optional deepening: for the fullest **lexicon** base entry — beyond the study's `base_gloss` — the lemma can be joined to `mti_terms` / `wa_meaning_parsed` on the Strong's number; offered as an enrichment, not required for the distinction above.)*

## F. Build plan (both books now + baked into the method)
1. **Projection generator** (read-only) — emits `reading_view` + `nodes` + `edges` + `dimensions_long` for Psalms + Proverbs, with `reading` (relabel), derived `translit`/`object_kind`/`discovery_flag`, and the `NONE`/`ABSENT` codes. *(no DB write)*
2. **The preamble** — this companion spec, finalised as the artifact that ships with every projection.
3. **114 content consistency** — 77% carry the full shape; the 23% (mostly Psalms + early Proverbs cyc 1-3) have the content in an older arrangement. Fix = (i) reliable `translit`/verse-anchor **extraction** (mechanical, persisted), (ii) re-author only the genuinely-thin handful; flag the style-variants rather than re-read ~900. *(scope decision below)*
4. **Method bake-in** — relabel 114→`reading` in the ve-lexical catalogue + ledger-lib; add the true `discovery` guidance; add `direction`/`object_kind` to the authored ledger for the next book. *(so future books emit consistently)*

**For sign-off before I build:** (i) confirm the two-layer split (reading-view + technical-data-layer) and the column set above; (ii) confirm the 114 fix approach (mechanical extraction + flag style-variants, vs full re-author of ~900); (iii) confirm `object_kind`/`direction` are done as **derived-now for the two books + authored-going-forward**, not a re-read.
