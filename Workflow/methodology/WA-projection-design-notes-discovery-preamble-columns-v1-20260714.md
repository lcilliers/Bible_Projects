# WA — Projection design notes: the `discovery` dimension, a preamble document, and additional columns

- **Date:** 2026-07-14
- **Responds to:** `WA-projection-spec-1.2-2026-07-13.md` (the flattened reading view).
- **Purpose of the projection (researcher framing):** give AI Chat a data substrate to run **book-level inner-being analysis** — the movement/reading analysis done for Psalms — reading-by-reading, with the *evidence travelling with the data*.
- **Method:** investigated the **live DB** (Psalms reread `reread-psalms-2026` + Proverbs reread `reread-proverbs-2026`, **4,137 read-2026 characteristics**), not the Psalms-only JSON emit the spec was built on. Nothing below is inferred; all counts are queried.

---

## 1. The `discovery` dimension (ve_nr 114) — reconsidered

### 1.1 Intended vs actual (evidence)
- **Catalogue intent** (`wa-ve-lexical-catalogue-v1`, D11 / 114): *"the uncertainty / discovery-notes channel — when unsure, write here; also the span-completeness lookout."* I.e. a **lookout for the unexpected** + an uncertainty scratchpad (aligned with the "revelation test" / "find the gems" principle).
- **Actual content** (sampled, both books): 114 has become the **evidence-anchored lexical reading** — transliteration + the capitalised verse-quote + the meaning + the "so-what" finding + cross-refs. It is the **longest free-text column (~60 % of the read budget, per the spec)**. Examples:
  - Pro 21:6 `114`: *"sheqer (falsehood) — 'the getting of treasures by a LYING tongue is a fleeting vapour and a snare of death'; wealth amassed by lies vanishes like vapour…"*
  - Psa 37:15 `114`: *"v15: 'their bows shall be BROKEN (shabar)' — physical outcome of the wicked's violence recoiling; **not a human IB operation**…"* ← here it **still does genuine discovery** (distinguishing a physical outcome from an IB operation).

### 1.2 Diagnosis
114 now **conflates three distinct jobs**: (a) the **evidence anchor** (translit + verse-quote), (b) the **meaning-narrative** (the "story"), (c) **genuine discovery / uncertainty** (occasional, esp. in Psalms). It is **mislabelled**: an analyst reading a column called "discovery" expects *surprises*, but gets the meaning-story. The spec's worry is correct — *the single largest thing being read is not doing the job its name claims* — **but the content itself is the most valuable text in the row** (it carries the primary, verse-grounded evidence).

### 1.3 Corrected model (proposal)
1. **Relabel 114 → `reading`** (the evidence-anchored lexical note) in the projection + preamble + method. Keep it as-is in the DB; it is the analyst's primary evidence text. This resolves the mislabelling at zero data cost.
2. **Promote `translit` to its own column** (spec-requested) — extract the leading `<translit> (<gloss>)` token that opens most 114/101 notes.
3. **Reinstate a true `discovery` channel** — a short, honest field answering *"what did the verse reveal that was unexpected / any uncertainty? — else `none`"*, per the catalogue's original intent and the revelation-test. Bake into the read method going forward.

### 1.4 Backfill options for Psalms + Proverbs — with recommendation
| id | backfill | feasibility | recommend |
|---|---|---|---|
| **B1** | extract `translit` into a column (parse `word (gloss)` at the head of 114/101; embedded `WORD (translit)` fallback) | feasible; **Proverbs clean, Psalms noisier** — carry a `translit_confidence` flag | ✅ **do** (cheap, spec-requested, reversible) |
| **B2** | **relabel** 114 → `reading` (projection + preamble only; no DB write) | trivial | ✅ **do** |
| **B3** | author a genuine per-char `discovery` retrospectively | **heavy** — a true fill needs a re-read | **defer**: bake into the method for the *next* book; for Psalms/Proverbs, a **light heuristic flag** only — mark chars whose 114 already contains a discovery marker (`not a`, `NOT`, `against`, `the finding is`, `cf`, `physical outcome`) as `discovery=present`, else `absent` — an honest "which readings already carry a surfaced finding" signal without re-reading |

**Recommendation:** do B1 + B2 now (on approval); implement the true `discovery` channel in the method (v-next) and apply only the **light B3 flag** to the two existing books, clearly marked as heuristic, not authored.

---

## 2. A preamble document to accompany the projection

### 2.1 Why it is needed
The projection is coded strings + prose. Without a contract, a downstream analyst **mis-derives**: reads "discovery" as surprises (§1), collapses `NONE`/`ABSENT` (the load-bearing distinction), or treats `target: "to God"` as an object rather than a direction. The preamble is that contract — **how each column is derived and how it must be read.**

### 2.2 Design — one row per column
`column · source (table.field / ve_nr) · class (coded | free-text | derived) · derivation · interpretation · NONE vs ABSENT meaning · caution`

### 2.3 First-cut of the key rows (to be completed into the full preamble)
| column | source | class | interpretation / caution |
|---|---|---|---|
| `reading_id` | `char_key` + occurrence | coded | one row = one reading (a lemma-in-context on a span) |
| `span_id` | `verse_span_index.id` | coded | **the true discriminator** between readings of one lemma (spec §1) |
| `morph` | `verse_span_index.morph_code` | coded | the Hebrew parse; **is in the DB (100 %)** though it never travelled in the emit |
| `hebrew_form` | — | **GAP** | `verse_span_index.surface` is the **English ESV word**, not Hebrew; the Hebrew form is derivable via STEP + morph but **not stored** — flag as a genuine gap |
| `translit` | parsed from `114`/`101` | derived | promoted per §1; carry `translit_confidence` |
| `sense`(101) | ve_lexical 101 `value` | free | short sense summary |
| `operation`(106) | 106 | free | what the characteristic *does* in the verse |
| `reading`(114) | 114 | free | **evidence-anchored note** (translit + verse-quote + meaning + finding) — renamed from "discovery" (§1) |
| `seat`(104)/`manner`(108) | 104/108 | coded-ish | often `NONE` (reader-determined absence) |
| `coupling`(112) | 112 `value` + `to_span` | free + edge | the pairing **phrase**; the **edge** lives in `from_span/to_span` (see §3.1) |
| `role`(115) | 115 / `verse_span_index.role` | coded | characteristic / qualifier / standalone |
| `locus`(116) | 116 | coded | `internal:ib-state` / `external:god` / `external:person` |
| `NONE` | `value='none'` | state | **reader looked, found none — evidence of silence** |
| `ABSENT` | no row for that ve_nr | state | **never read — NOT evidence of silence** |

---

## 3. Additional columns — so the analyst cannot say "inconclusive" for want of data

The spec's flat file is **node-centric** (one row per reading). Book-level **movement** analysis needs more than nodes.

### 3.1 ★ The biggest gap — the relational EDGES (the movement web)
The study's object is *"movements, associations, interlocking, emergence."* The flat file carries `coupling` as **prose** but **not the graph edges** — yet **4,154 span-id pair edges already exist** in the data (`ve_lexical.from_span/to_span`, `resolution='span'`). **Propose a companion edge-list projection:** `from_span, to_span, edge_type (coupling|bearer|target), direction, pair_kind, phrase`. Without it the analyst **literally cannot build the web** and would rightly report movement analysis as impossible. This is the single most important addition.

### 3.2 Grouping / context columns
`genre` (verse.genre — drives how to read), `book`, `chapter`, `corpus`/testament (OT/NT), `passage_id` (the **reading frame** — the spec drops `passage_ref`, but movement lives *within* passages).

### 3.3 Provenance / discovery-tracking columns
`char_candidate_tag` (`emergent-read-2026` / `orphan-reread-2026` / seeded — **which chars the old model missed is itself a finding**), `role_provenance` (the read layer).

### 3.4 Salience columns
`lemma_freq_in_book` (major vs minor characteristic), `ib_char.instance_count`, `family`, `cluster` (M-code) + subgroup — lets the analyst weight and group.

### 3.5 Evidence-on-tap
`verse_text` — the spec drops `passage_text` ("I can read the Psalm"), but an AI analyst **not** reading the whole book wants the verse beside the reading. Offer as an **optional column** (or a lookup keyed on `verse_ref`), the analyst's choice per read-budget.

### 3.6 The spec's own new columns — feasibility check (from the live DB)
| spec column | status |
|---|---|
| `span_id`, `morph` | **already in DB, 100 %** (morph via `morph_code` — the spec assumed it "does not travel"; it does, in the span index) |
| `char_key`, `ib_char`, `family`, `role`, `locus` | present |
| `hebrew_form` | **genuine gap** (surface = English) |
| `translit` | derivable (§1, B1) |
| `direction` | **null everywhere** — a genuine gap; bake into the method (E4: direction may *constitute* the movement) |
| `object_kind` | needs authoring — a **light backfill** from `target` + `bearer` (god/person/self/thing/abstraction/null) |

---

## 4. What I can execute on approval
1. **The projection generator** — the node flat-file (spec column set, with `reading`/`translit` per §1) **+ the companion edge-list** (§3.1), straight from `ve_lexical` + `verse_span_index` + `ib_characteristic`, for Psalms + Proverbs.
2. **The preamble / data-dictionary** (§2, completed).
3. **B1 translit backfill** + **B2 relabel** (§1.4).
4. *(optional, heavier)* `object_kind` light backfill; the true `discovery` method change + the light B3 flag.

**For sign-off:** (a) confirm the `discovery` corrected model (relabel + translit + reinstate true discovery going forward); (b) confirm the **edge-list** as a first-class companion; (c) confirm which additional columns (§3) to include; (d) confirm whether to author `object_kind`/`direction` now (light backfill) or bake into the next book's method.
