# Evidence pack — the 261 orphans, the 18 passage-less spans, and where the char model is going

> Generated 2026-07-11 directly from `database/bible_research.db` (schema 3.40.0). Real schemas + real records, plus my recent chat analysis reproduced verbatim for you to annotate. Nothing here is conceptual-only.

---
## PART 1 — my recent chat analysis, reproduced for your comment

*(This is what I said across the last few turns. Mark it up where the thinking is wrong / mixes old and new.)*

**On the 261:** The master index is `wa_verse_records`, built **per registered term** via STEP ("for term X, here are its verses and spans"). A char-span is an "orphan" when no such record points to it. Of the 261: **192** have a word that is **not a registered study term** (e.g. `stands` H5975, `Kiss` H5401, `ponder` H0559 — the study never registered these); **69** are registered terms whose verse-record for that span was never built. By seed-source: **140 READ-EMERGENT**, 93 registry, 28 IB. I called this the per-book method's **step (d)** work ("the term must be recorded, the verses pulled, the links built — a STEP action"), hence engine onboarding, not a SQL patch.

**On the 18:** `passage` is the reading-unit layer; the 18 are char-spans in verses that were **never assigned a passage**. The words are mostly emergent (`sojourn`, `mixed`, `learned`, `breath`, `abide`, `fly away`, `rest`, `slipped`) — the passage layer was built from the seed *before* the reading found characteristics in these verses.

**My architecture claim (the part you flagged as full-circle / mixing old+new):** both gaps share one root — the reading outran the up-front scaffolding. Three layers fell out of step, and I tabled them like this:

| layer | keyed by | emergent chars covered? |
|---|---|---|
| seed | lemma list | fixed this turn (seed-extension file) |
| master index `wa_verse_records` | **registered term** | 261 orphans (step d) |
| passage layer | seed-time verses | 18 gaps |
| new `ib_characteristic` index (built this turn) | **lemma** | all 2,168 covered incl. these |

**The model question I put to you:** either (i) make every characteristic word a registered term (register the ~192 + pull verses via engine onboarding, extend passages) so the old term-backbone matches the reading; or (ii) treat the new lemma-based `ib_characteristic` index as the primary backbone and relax the term-registry requirement for emergent chars. **This is the decision I could not resolve and where the old/new architecture collides.**

---
## PART 2 — the 18 passage-less char-spans (EXACT records)

Columns straight from `verse_span_index` (+ `verse.passage_id`). `has_vr` = does a master-index row exist for it.

| span_id | reference | surface | primary_strong | characteristic | char_candidate | char_candidate_tag | ib_char_id | passage_id | has_vr |
|---|---|---|---|---|---|---|---|---|---|
| 307358 | Psa 105:12 | sojourners | H1481 | sojourners (gur) | 1 | READ-EMERGENT-2026 | 63 | None | 1 |
| 307386 | Psa 105:23 | sojourned | H1481 | sojourn (gur) | 1 | READ-EMERGENT-2026 | 63 | None | 1 |
| 307474 | Psa 106:35 | mixed | H6148 | mix (arab) | 1 | READ-EMERGENT-2026 | 326 | None | 0 |
| 307476 | Psa 106:35 | learned | H3925 | learn (lamad) | 1 | READ-EMERGENT-2026 | 222 | None | 0 |
| 307478 | Psa 106:37 | sacrificed | H2076 | sacrifice (zabach) | 1 | READ-EMERGENT-2026 | 95 | None | 0 |
| 307631 | Psa 116:12 | render | H7725 | render (shuv) | 1 | READ-EMERGENT-2026 | 429 | None | 1 |
| 307704 | Psa 119:33 | keep | H5341 | keep / guard (natsar) | 1 | READ-EMERGENT-2026 | 275 | None | 2 |
| 307783 | Psa 120:5 | sojourn | H1481 | sojourn (gur) | 1 | READ-EMERGENT-2026 | 63 | None | 1 |
| 308114 | Psa 141:3 | mouth | H6310 | guard over the mouth | 1 | READ-EMERGENT-2026 | 338 | None | 1 |
| 308122 | Psa 144:4 | breath | H1892 | man like a breath | 1 | READ-EMERGENT-2026 | 84 | None | 0 |
| 306042 | Psa 17:5 | slipped | H4131 | feet held fast, not slipped | 1 | READ-EMERGENT-2026 | 233 | None | 0 |
| 306194 | Psa 27:10 | forsaken | H5800 | though parents forsake, God takes me in | 1 | READ-EMERGENT-2026 | 302 | None | 2 |
| 305964 | Psa 2:3 | cast | H7993 | cast off the cords | 1 | READ-EMERGENT-2026 | 458 | None | 0 |
| 306384 | Psa 55:6 | fly away | H5774 | fly away (uph - I would fly away) | 1 | READ-EMERGENT-2026 | 298 | None | 0 |
| 306385 | Psa 55:6 | rest | H7931 | be at rest / settle (shakan - and be at rest) | 1 | READ-EMERGENT-2026 | 455 | None | 0 |
| 284392 | Psa 87:4 | know | H3045 | know (yada) | 1 | Reg 100 knowledge | 172 | None | 1 |
| 307010 | Psa 87:7 | Singers | H7891 | singers (shir) | 1 | Reg 121 praise | 448 | None | 2 |
| 307084 | Psa 91:1 | abide | H3885 | abide (lun) | 1 | READ-EMERGENT-2026 | 218 | None | 0 |

Note: every one has `passage_id = None` (that's the defect), most have `has_vr = 0` (so they're *also* in the 261), and every one has an `ib_char_id` (they ARE in the new char index).

---
## PART 3 — the 261 orphans

**Breakdown:** total 261 · not-a-registered-term **192** · registered-but-unlinked **69** · by seed-source {'IB': 28, 'READ-EMERGENT': 140, 'Reg': 93}

### 3.1 The contrast — one ORPHAN vs one LINKED char-span (same verse, Ps 1:1)

**ORPHAN — `verse_span_index` row for 'stands' (H5975):**
```
  id                   = 275348
  reference            = Psa 1:1
  surface              = stands
  strongs              = H5975G
  primary_strong       = H5975
  role                 = characteristic
  char_candidate       = 1
  char_candidate_tag   = READ-EMERGENT-2026
  characteristic       = stands not in sinners' way
  ib_char_id           = 312
  verse_id             = 20938
  wa_verse_records rows pointing here = 0   <-- THE MISSING LINK
  mti_terms rows for H5975         = 0   <-- not a registered term
```

**LINKED — `verse_span_index` row for 'Blessed' (H0835), same verse:**
```
  id                   = 275341
  reference            = Psa 1:1
  surface              = Blessed
  strongs              = H0835
  primary_strong       = H0835
  role                 = characteristic
  char_candidate       = 1
  char_candidate_tag   = IB:blessed
  characteristic       = blessed is the man
  ib_char_id           = 29
  verse_id             = 20938
  wa_verse_records rows pointing here = 2   <-- present
  mti_terms rows for H0835         = 1   <-- registered term
```

**The master-index rows that the LINKED span has (and the orphan lacks):**
```
  {"id": 240629, "term_id": "H0835", "term_inv_id": 7777, "mti_term_id": 7642, "reference": "Psa 1:1", "verse_id": 20938, "verse_span_id": 275341, "target_word": "Blessed", "span_strong_match": 1, "delete_flagged": 0}
  {"id": 242695, "term_id": "H0835", "term_inv_id": 7777, "mti_term_id": 7642, "reference": "Psa 1:1", "verse_id": 20938, "verse_span_id": 275341, "target_word": "Blessed", "span_strong_match": 1, "delete_flagged": 0}
```

### 3.2 Examples — the 192 not-registered-term orphans
| span_id | reference | surface | primary_strong | characteristic (read) | tag |
|---|---|---|---|---|---|
| 275348 | Psa 1:1 | stands | H5975 | stands not in sinners' way | READ-EMERGENT-2026 |
| 276507 | Psa 2:12 | Kiss | H5401 | kiss the Son | READ-EMERGENT-2026 |
| 305964 | Psa 2:3 | cast | H7993 | cast off the cords | READ-EMERGENT-2026 |
| 278177 | Psa 3:5 | lay | H7901 | lie down and sleep in trust | READ-EMERGENT-2026 |
| 279472 | Psa 4:8 | lie down | H7901 | in peace lie down and sleep | READ-EMERGENT-2026 |

### 3.3 Examples — the 69 registered-but-unlinked orphans
| span_id | reference | surface | primary_strong | characteristic (read) | tag |
|---|---|---|---|---|---|
| 279450 | Psa 4:4 | ponder | H0559 | ponder in your heart, be silent | READ-EMERGENT-2026 |
| 270364 | Psa 10:11 | says | H0559 | 'God has forgotten, he won't see' | READ-EMERGENT-2026 |
| 270469 | Psa 10:6 | says | H0559 | 'I shall not be moved' | READ-EMERGENT-2026 |
| 274716 | Psa 16:4 | pour out | H5258 | refuse the idolaters' offerings | READ-EMERGENT-2026 |
| 275489 | Psa 21:11 | plan | H5186 | the enemies devise doomed evil | READ-EMERGENT-2026 |

---
## PART 4 — the actual schema of every table in the chain

### `verse_span_index`
```
  id                       INTEGER
  verse_id                 INTEGER
  reference                TEXT
  word_index               INTEGER
  surface                  TEXT
  pos                      TEXT
  morph_code               TEXT
  stem                     TEXT
  language                 TEXT
  strongs                  TEXT
  primary_strong           TEXT
  source                   TEXT
  built_at                 TEXT
  role                     TEXT
  role_provenance          TEXT
  role_set_at              TEXT
  role_source_ve_id        INTEGER
  char_candidate           INTEGER
  char_candidate_tag       TEXT
  characteristic           TEXT
  ib_char_id               INTEGER
```

### `wa_verse_records`
```
  id                       INTEGER
  file_id                  INTEGER
  term_inv_id              INTEGER
  term_id                  TEXT
  transliteration          TEXT
  testament                TEXT
  reference                TEXT
  verse_text               TEXT
  last_changed             TEXT
  book_id                  INTEGER
  chapter                  INTEGER
  verse_num                INTEGER
  translation              TEXT
  note                     TEXT
  claude_output            TEXT
  created_at               TEXT
  updated_at               TEXT
  target_word              TEXT
  span_strong_match        INTEGER
  context_before           TEXT
  context_after            TEXT
  delete_flagged           INTEGER
  mti_term_id              INTEGER
  morph_code               TEXT
  stem                     TEXT
  word_registry_fk         INTEGER
  verse_id                 INTEGER
  analysis_marker          TEXT
  incorporated_in          TEXT
  verse_span_id            INTEGER
```

### `mti_terms`
```
  id                       INTEGER
  strongs_number           TEXT
  transliteration          TEXT
  gloss                    TEXT
  language                 TEXT
  owning_registry          TEXT
  owning_registry_fk       INTEGER
  owning_word              TEXT
  owning_part              TEXT
  word_data_reference      TEXT
  word_data_ref_fk         INTEGER
  status                   TEXT
  exclusion_reason         TEXT
  extraction_date          TEXT
  strongs_reconciled       INTEGER
  anchor_note              TEXT
  last_changed             TEXT
  delete_flagged           INTEGER
  vc_status                TEXT
  vc_instruction_version   TEXT
  vc_status_updated_at     TEXT
  vc_status_note           TEXT
  md_version               INTEGER
  cluster_code             TEXT
```

### `verse`
```
  id                       INTEGER
  osis_id                  TEXT
  reference                TEXT
  book_id                  INTEGER
  chapter                  INTEGER
  verse_num                INTEGER
  testament                TEXT
  verse_text               TEXT
  created_at               TEXT
  passage_id               INTEGER
  is_passage_anchor        INTEGER
  process_marker           TEXT
  genre                    TEXT
```

### `passage`
```
  id                       INTEGER
  ref                      TEXT
  anchor_verse_id          INTEGER
  book_id                  INTEGER
  start_chapter            INTEGER
  start_verse              INTEGER
  end_chapter              INTEGER
  end_verse                INTEGER
  verse_count              INTEGER
  source                   TEXT
  review_flag              TEXT
  notes                    TEXT
  created_at               TEXT
```

### `ib_characteristic`
```
  id                       INTEGER
  code                     TEXT
  name                     TEXT
  aka                      TEXT
  family                   TEXT
  status                   TEXT
  books                    TEXT
  gist                     TEXT
  colour_range             TEXT
  junctions                TEXT
  open_questions           TEXT
  discovery_doc            TEXT
  provenance               TEXT
  created_at               TEXT
  updated_at               TEXT
  char_key                 TEXT
  key_word                 TEXT
  key_span_id              INTEGER
  operation                TEXT
  ledger                   TEXT
  instance_count           INTEGER
  book_scope               TEXT
```
