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
| `char_key` / `ib_char` | `ib_characteristic.char_key` / `.name` | spec ✓ |
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
| `object_kind` | derived | coded | — | **new** — god/person/self/thing/abstraction/none (from locus+target+bearer) |
| `manner` | 108 | coded | often NONE | |
| `intensity` | 109 | — | **ABSENT** | never read (poetic method) |
| `specifier` | 110 | — | **ABSENT** | never read |
| `effect` | 111 | — | **ABSENT** | Phase-2 |
| `coupling` | 112 | free + edge | — | the pairing **phrase**; the **edge** is in the technical layer |
| `prohibition` | 113 | coded | rare (9) | |
| `reading` | 114 | free | — | **RENAMED from `discovery`** — evidence-anchored note (translit + verse-quote + meaning + finding) |
| `discovery_flag` | derived | coded | — | **new** — does `reading` carry a surfaced finding? (present/absent) — answers (b) |
| `role` | 115 = `verse_span_index.role` | coded | — | characteristic/qualifier/standalone |
| `locus` | 116 | coded | — | internal:ib-state / external:god / external:person |
| `direction` | `ve_lexical.direction` | coded | **ABSENT** | gap; authored going forward |

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
- **v1.2's ABSENT dims confirmed from data:** `intensity`(109), `specifier`(110), `effect`(111), `direction`, `source`(partial) — these are legitimately empty in the reread (never read / Phase-2), and the `NONE`/`ABSENT` codes make that honest.
- **Added beyond v1.2** (so the analyst cannot claim "inconclusive for want of data"): the **edges** (movement graph), `genre`/`book`/`chapter`/`corpus`/`passage_id` (context), `char_candidate_tag`/`role_provenance` (provenance), `lemma_freq_book`/`ib_instance_count` (salience), `object_kind`/`discovery_flag` (derived), optional `verse_text`.
- **Gaps that remain, honestly flagged:** `hebrew_form` (not stored), `direction` (never read), `intensity`/`specifier`/`effect` (never read). None block the current analysis; all are marked, not silently blank.

---

## F. Build plan (both books now + baked into the method)
1. **Projection generator** (read-only) — emits `reading_view` + `nodes` + `edges` + `dimensions_long` for Psalms + Proverbs, with `reading` (relabel), derived `translit`/`object_kind`/`discovery_flag`, and the `NONE`/`ABSENT` codes. *(no DB write)*
2. **The preamble** — this companion spec, finalised as the artifact that ships with every projection.
3. **114 content consistency** — 77% carry the full shape; the 23% (mostly Psalms + early Proverbs cyc 1-3) have the content in an older arrangement. Fix = (i) reliable `translit`/verse-anchor **extraction** (mechanical, persisted), (ii) re-author only the genuinely-thin handful; flag the style-variants rather than re-read ~900. *(scope decision below)*
4. **Method bake-in** — relabel 114→`reading` in the ve-lexical catalogue + ledger-lib; add the true `discovery` guidance; add `direction`/`object_kind` to the authored ledger for the next book. *(so future books emit consistently)*

**For sign-off before I build:** (i) confirm the two-layer split (reading-view + technical-data-layer) and the column set above; (ii) confirm the 114 fix approach (mechanical extraction + flag style-variants, vs full re-author of ~900); (iii) confirm `object_kind`/`direction` are done as **derived-now for the two books + authored-going-forward**, not a re-read.
