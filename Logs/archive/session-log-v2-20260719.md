# IBA Session Log — v2 — 2026-07-19

**Session focus:** Build a reusable passage/verse export view for the IBA app DB; a
byproduct of reviewing its output surfaced a **material flaw in candidate-char seeding**
that distorts passage generation. Session closed here for the researcher to fix seeding
in a fresh session.

- **DB:** `iba/app/db/iba.db`
- **Test book:** Romans (`book = 'Rom'`)

---

## 1. What was delivered this session

### 1.1 Reusable view + export — `vw_passages_by_book`
- Script: [create-passages-by-book-view-and-export.ps1](../scripts/create-passages-by-book-view-and-export.ps1)
- Generic, book-agnostic SQLite view `vw_passages_by_book`, grained **one row per
  verse-within-passage**, ordered book → chapter → verse.
- Columns: `book`, all `passage.*`, `verse_reference`, `verse_text`, and
  `candidate_chars` (comma-delimited **DISTINCT** candidate tags for that verse, via
  `span → span_candidate`).
- Export is per-book (`-Book`, default `Rom`); `-DryRun` previews without writing.
- Romans export: **424 verse-rows** → [vw_passages_by_book-Rom.csv](../app/config/views/vw_passages_by_book-Rom.csv)

### 1.2 One-time DB correction — plain-text verse column
- `verse.preview` holds **STEP HTML** (word spans + a leading verse-number span); it was a
  mistake to treat that as the verse text.
- **Non-destructive fix:** added a new column **`verse.text`** (clean, tag-free text) and
  populated all **29,037** rows once from the HTML. `preview` retained — the HTML carries
  the strong/morph word-span linkage that `span`/`span_candidate` derive from.
- Script (idempotent, re-runnable): [_apply_verse_plaintext_column.py](../scripts/_apply_verse_plaintext_column.py)
- View now reads `v.text`. Note: `verse.text` is a **snapshot** of `preview`; re-run the
  script if STEP HTML is ever re-imported.

---

## 2. THE FLAW — candidate-char seeding pollutes passage generation

**Discovered via** the `candidate_chars` column of the new view: for Romans, the per-verse
candidate lists are dominated by grammatical/function words and generic verbs, not
inner-being characteristics.

### 2.1 Evidence (Romans)
- **All 1,961 span-candidates are `seed_source = 'registry-direct'`** — 365 distinct tags.
  There is **no `ib-judgement` and no `read-emergent` seeding at all** for this book. Romans
  candidate chars are therefore purely mechanical registry-lemma matches.
- Top candidate tags by verse-count are exactly the function/generic words:

  | verses | candidate_tag | seed_source |
  |---|---|---|
  | 133 | God | registry-direct |
  | 91 | to be | registry-direct |
  | 69 | through/because of | registry-direct |
  | 66 | but | registry-direct |
  | 66 | Christ | registry-direct |
  | 40 | sin | registry-direct |
  | 35 | faith | registry-direct |
  | 33 | to say: says | registry-direct |
  | 23 | to do/make: do | registry-direct |
  | 20 | to have/be | registry-direct |

- Passage size distribution is lopsided — 155 singletons vs a long tail of 11–15-verse
  passages:

  | size | passages |
  |---|---|
  | 1 | 155 |
  | 2 | 31 |
  | 3 | 22 |
  | 4 | 6 |
  | 5 | 7 |
  | 6 | 5 |
  | 7–8 | 2 |
  | 11 | 2 |
  | 15 | 1 |

### 2.2 Why it matters (material impact on passage generation)
- Passages are built with **`rule = 'char-continuity'`** — consecutive verses are chained
  into a passage when they share a candidate characteristic.
- When function words ("to be", "but", "through/because of") and ubiquitous nouns ("God",
  "Christ") are seeded as candidate chars, char-continuity is driven by **grammatical noise**
  rather than genuine characteristic continuity. Passage boundaries become arbitrary — a few
  verses balloon on a shared "to be"/"God", most fall to singletons.
- This contradicts the study's own rules:
  - candidate seed should be **independent of the registry** and over-inclusive, then
    filtered by the lexical stage — here it is registry-direct *only*, unfiltered
    (memory `feedback_candidate_seed_independent_over_inclusive_control`);
  - the characteristic list should **validate** verse→list, never impute
    (memory `feedback_characteristic_list_validates_not_imputes`);
  - function words / generic lemmas are not inner-being characteristics.

### 2.3 Suspected root cause (to confirm next session)
- The `registry-direct` seeding path maps registry lemmas straight onto spans as candidate
  chars with **no inner-being screen and no stop-list** for function words / high-frequency
  generic lemmas.
- The `ib-judgement` / `read-emergent` seeding paths appear **not to have been run for
  Romans** (and possibly the whole NT), leaving only the mechanical path.

---

## 3. Handoff — next session scope (fix seeding & chars)

The researcher will start a fresh session to fix the seeding and chars. Suggested scope:

1. **Decide the seeding model** for `span_candidate`: registry-direct alone is insufficient
   and noisy. Add the IB screen + a function-word/high-frequency stop-list; confirm whether
   `ib-judgement` / `read-emergent` paths must run for NT books.
2. **Re-seed** candidate chars (rebuild `span_candidate`) under the corrected rules.
3. **Re-run passage generation** (`char-continuity`) so passage boundaries reflect genuine
   characteristic continuity, then re-inspect via `vw_passages_by_book -Book Rom`.
4. Cross-check other books (the flaw is likely programme-wide, not Romans-specific).

**Regression harness already in place:** re-running
`create-passages-by-book-view-and-export.ps1 -Book <X>` after any seeding/passage rebuild
gives an immediate, readable per-verse view of candidate chars vs passage grouping.

---

## 4. Files touched
- `iba/scripts/create-passages-by-book-view-and-export.ps1` (new)
- `iba/scripts/_apply_verse_plaintext_column.py` (new; one-time correction, idempotent)
- `iba/app/config/views/vw_passages_by_book-Rom.csv` (new export)
- `iba/app/db/iba.db` — added `verse.text` column (+ populated); created view `vw_passages_by_book`
