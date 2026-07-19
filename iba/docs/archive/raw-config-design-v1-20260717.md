# The raw run — the STEP data work, flushed into config design

> **v1 · 2026-07-17.** Consolidates the prototype findings (API map · term→sense→span ·
> the 4+2 tables · relatedNos excluded · source-vs-derived) into a config-ready walk-through of
> `module.raw`. **All the work is in this document. No config created or loaded.**
>
> This supersedes the scattered raw-tables v1/v2 as the settled column-level design. It is the
> spec the raw config entries will be authored from — the design layer is still ahead.

---

## 1. What is settled (measured, not assumed)

| finding | evidence |
|---|---|
| **term → sense → span** | every sense of a lemma shares a byte-identical definition tree; the head is the sense; the span names its sense (measured on `peace`, 35 senses) |
| **relatedNos is root-family noise** | `H2519` smoothness drags in "to divide", "portion", "Mount Halak"; **excluded from all further action** (researcher) |
| **three API calls, two are the same API** | §2 |
| **the verse does not belong to a strong** | `Gal.2.13` returned by both `G5272` and `G4942` — one verse, two strongs, before any cascade |
| **source ≠ derived** | the span (STEP, immutable) and the overlay (our judgement, volatile, re-run) split into two tables |
| **the meaning was never used** | old `D101` = the ESV surface word on 88% of rows, not the lexicon sense. The new design puts the meaning where the analytics must read it |

---

## 2. The three calls

| call | input | route | produces |
|---|---|---|---|
| **1** | the English word | `masterSearch  version=<v>\|meanings=<word>` | the seed strongs |
| **2** | a strong | `module.getInfo/<v>//<strong>//` | the strong's detail — **the meaning** |
| **3** | a strong | `masterSearch  strong=<strong>\|version=<v>` | the strong's verses, **each with its full interlinear in `preview`** |

**Call 3's `preview` is the whole verse's interlinear** — every word with its strong and morph. So
**the span comes from call 3; there is no separate morphology call for the word run.**

---

## 3. The tables — final column design

```
  word ──< word_strong >── strong ──< strong_verse >── verse ──< span ──1:1── span_analysis
   registry    L1           L2            m:m           L3        L4a          L4b
                            MEANING                    (preview)  SOURCE       DERIVED
```

### L1 · `word_strong` — the link

**Source:** call 1 `definitions[].strongNumber`. **Grain:** one row per (word, strong).

| column | from | notes |
|---|---|---|
| `id` · `word_fk` · `strong_fk` · `deleted` | ours | the m:m link, word ↔ strong |

⚠ **ONE RECONCILIATION (O1).** You defined L1's key as *"the unique strong number"* — but a strong
serves several words (`peace` and `peaceful` both find `G1515`), which is why you agreed XREF has no
place and a strong is stored once. Those two cannot both hold: a table keyed on *unique strong*
cannot also record *which several words* found it. **Resolved by relatedNos being excluded** — with
no `from_strong`, L1 is simply the **word↔strong many-to-many junction** (key = the pair), and the
unique strong lives in **L2**. Confirm this reading.

### L2 · `strong` — the detail · **the meaning**

**Source:** call 2 `vocabInfos[]`. **Grain:** one row per strong · **unique** · global to the study.

| column | from | notes |
|---|---|---|
| `id` · `deleted` | ours | |
| `strongNumber` | API | **the key** (the resolved code STEP answers with — never a base code, since seeds and searches are always resolved) |
| `accentedUnicode` | API | the actual Hebrew/Greek word |
| `stepGloss` · `stepTransliteration` | API | |
| **`mediumDef`** | API | **★ the meaning** — `': head' + tree` |
| `lsjDefs` · `shortDefMounce` | API | Greek only |
| `count` · `freqList` | API | frequency lives here only |
| `_step_Type` · `_vi/_es/_zh` | API | |

`relatedNos` **excluded**. `rawRelatedNumbers` **excluded** (it is the same codes — noise).

### `strong_verse` — the m:m index

**Source:** which verses call 3 returned for the strong. **Grain:** one per (strong, verse) · unique.

| column | notes |
|---|---|
| `id` · `strong_fk` · `verse_fk` · `deleted` | the source's assertion "this strong is in this verse" |

This is the **source side** of the parse-check: `strong_verse` = what STEP asserted; `span` = what
the parse found. Measured to agree, 35/35 senses, 0 missed.

### L3 · `verse`

**Source:** call 3 `results[]`. **Grain:** one per verse · **unique** · does not belong to a strong.

| column | from | notes |
|---|---|---|
| `id` · `deleted` | ours | |
| `osisId` | API | **the key** |
| `key` | API | human reference |
| `preview` | API | the full interlinear HTML — kept verbatim, the source of L4a (re-derivable, like `verse_morphology_raw`) |
| `step_version` | ours | provenance — which module the text is from |

### L4a · `span` — SOURCE, immutable

**Source:** a parse of `verse.preview`. **Grain:** one per (verse, position) · **the key**.

| column | from | notes |
|---|---|---|
| `id` · `verse_fk` · `deleted` | ours | |
| `position` | parse | part of the key |
| `strong_variant` | parse | the span's strong (the head code; FK → L2) |
| `surface` | parse | the English word(s) |
| **`morph_code`** | parse | **the grammatical layer** — `HNcfsc` = construct |
| `particles` | parse | the attached `H9xxx`/`G9xxx` (the "and"/"the") — kept, not dropped |
| `built_at` | ours | raw time |

`language` · `stem` · `pos` · `person` derive from `morph_code` — compute on read.
`gloss` · `transliteration` are **not here** — read from L2 via `strong_variant`.

### L4b · `span_analysis` — DERIVED, mutable · 1:1 with `span`

**Filled after later stages, never by raw.** A failed analytics run truncates and rebuilds this;
`span` is never in scope.

| column | filled by |
|---|---|
| `span_fk` · `deleted` | — |
| `candidate_char` · `char_candidate_tag` | seeding |
| `role` · `role_provenance` · `role_set_at` · `role_source_ve_id` | analytics |
| `characteristic` · `ib_char_id` · `cluster` | analytics |

---

## 4. The run, stepped through

Package `new-word`, at the raw stage, over one word.

| step | call | input | writes | on_fail |
|---|---|---|---|---|
| **1 · discover** | 1 `meanings=<word>` | the word | `word_strong` (the seeds) · `verse`+`span` from call 1's own `results[]` | zero seeds → **pause-continue** (a word mapping to nothing is a researcher question) |
| **2 · detail** | 2 `getInfo` per strong | each `word_strong.strong` | `strong` (the meaning) | no vocab → recorded STEP gap, **report-continue** |
| **3 · verses** | 3 `masterSearch strong=` per strong | each strong | `strong_verse` · `verse` (new only) · `span` (parsed from `preview`, new verses only) | rows < STEP's total → **report-stop** |
| **4 · write** | — | all of the above | commit; **`span_analysis` rows created empty** | no-null · fk-integrity · strongs-format |
| **5 · validate** | — | — | the parse-check: `span` vs `strong_verse` must agree | mismatch → **report-stop** |

**Two things this collapses from the current pipeline:**

- **`step.raw.get-related-terms` — RETIRE.** It fetched relatedNos + root family. Both are excluded.
- **`step.raw.get-morphology` — FOLD into step 3.** Call 3's `preview` is the interlinear. The
  separate `getBibleText` call was the canon-wide bulk ingest — not needed for a per-word run.

**And the global-dedup rule (researcher):** steps 3–4 create a `verse` or `span` row **only if a
prior word's run has not already made it.** `Gal.2.13` proves it inside one word; across words it is
the norm. The key is the verse/(verse,position) — the row exists once, whatever finds it.

---

## 5. What this maps to in the config

| design element | config home | change |
|---|---|---|
| the 6 tables | **schema** (`DBSchema.json` for the new DB) — table, columns, **use + expectation** | the columns above ARE the expectation entries |
| which call sources which table | `utility/step.json` — the `apis` `may_source` | `meanings`→word_strong; `getInfo`→strong; `masterSearch.strong`→verse+strong_verse+span |
| when each column is written | `process/raw.json` — a **`records` node** (the add-rules) | new node: per table, which method writes which column, when |
| the steps | `wide/pipeline.json` — `module.raw` steps | retire get-related-terms; fold get-morphology; the 5 steps above |
| the entities | `process/raw.json` — `entities` | replace `ent.raw.verse/verse-morphology/lexicon` with the 6 tables |
| source vs derived | `raw.immutable` + `gate.base.no-judgement` | `span` is raw; `span_analysis` is filled downstream — the split satisfies both, which the old master violated |
| relatedNos excluded | `raw.include-related` | its subject narrows: there is no lexical-related pull; the option, if kept, governs only candidate-triggered co-occurrence |

---

## 6. Open before the design layer

| # | question | §|
|---|---|---|
| **O1** | **L1 = word↔strong junction (key = the pair), unique strong in L2 — confirm.** | §3 |
| **O2** | the Q7 `count` column — dropped from L4a here (a span is one row per position; multiplicity is the number of `word_strong`/`strong_verse` rows, derivable). Confirm it is not needed, or say what it counts. | — |
| **O3** | `particles` on the span — a list column, or their own rows? A span at one position can carry `H7307G H9002` (word + waw). Kept as a list keeps (verse, position) as the key. | §3 L4a |
| **O4** | `word_strong` — does it carry the call-1 `definition` fields (gloss/popularity) as **provenance of the discovery**, or nothing but the link? Best-practice: nothing but the link; the strong's facts are L2. | §3 L1 |
| **O5** | does the meaning parse (`mediumDef` → sense tree) get its own table (old `wa_meaning_parsed`), or is `mediumDef` on L2 enough for the study? The prototype showed the **head** is the span's meaning and needs no parse; the **tree** may still want structuring. | — |
