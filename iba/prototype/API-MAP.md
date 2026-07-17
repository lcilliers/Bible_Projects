# What each STEP call takes and returns — and what the layers actually are

> **2026-07-17.** Written because the prototype's layer naming was wrong and confusing.
> Measured live, not remembered.

---

## 1. There are THREE calls, not two — and two of them are the same API

| # | input | route | what it answers |
|---|---|---|---|
| **1** | **the English word** | `masterSearch  version=<v>\|meanings=<word>` | which strongs relate to this word — **and their verses** |
| **2** | **a strong** | `module.getInfo/<v>//<strong>//` | the strong's **lexicon entry** — its meaning |
| **3** | **a strong** | `masterSearch  strong=<strong>\|version=<v>` | the strong's **verses** |

**Calls 1 and 3 are the same API** — `masterSearch` — with a different query. That is why both return
the same shape. **Call 2 is a different API entirely.**

### What each returns, verbatim

**CALL 1** — `masterSearch version=ESV_th|meanings=hypocrisy`

| | |
|---|---|
| scalars | `time · signature · searchType(ORIGINAL_MEANING) · masterVersion · extraVersions · interlinearMode · timeTookTotal · query · total(17) · timeTookToRetrieveScripture · order · pageSize(60) · pageNumber(1) · searchRestriction` |
| `definitions[5]` | `strongNumber · matchingForm · stepTransliteration · gloss · type · popularity · popularityList · _zh_Gloss · _es_Gloss · _zh_tw_Gloss` |
| `strongHighlights[5]` | the same 5 codes, flat |
| `results[17]` | `key · osisId · preview` ← **the verses, with the full interlinear in `preview`** |
| `searchTokens[2]` | `enhancedTokenInfo · token · tokenType` |
| `languageCode[1]` | `en` |

**CALL 2** — `module.getInfo/ESV_th//G5272//`

| | |
|---|---|
| scalars | **none** |
| `vocabInfos[1]` | `strongNumber · accentedUnicode · stepGloss · stepTransliteration · **mediumDef** · lsjDefs · shortDefMounce · rawRelatedNumbers · count · freqList · relatedNos[] · _step_Type · _vi/_es/_zh definitions and glosses` |
| `morphInfos[0]` | empty for every code tried |

**CALL 3** — `masterSearch strong=G5272|version=ESV_th`

| | |
|---|---|
| scalars | as call 1, plus `searchType(ORIGINAL_GREEK_RELATED)` |
| `definitions[5]` | ← **call 3 returns the related lexicon too**, same shape as call 1 |
| `strongHighlights[1]` | the searched code |
| `results[6]` | `key · osisId · preview` |

---

## 2. The basis of each call — what feeds what

```
  the English word
        │
        ▼
  CALL 1  masterSearch meanings=<word>
        │
        ├── definitions[].strongNumber   ─┐   the same 5 codes
        ├── strongHighlights[]           ─┘   (either can be the input)
        │        │
        │        ├──────────────► CALL 2  getInfo//<strong>//      → the MEANING
        │        │
        │        └──────────────► CALL 3  masterSearch strong=<strong>  → the VERSES
        │
        └── results[].preview  ──┐
                                 ├──► (a PARSE, not a call) ──► the spans
        CALL 3 results[].preview ┘
```

**The input to calls 2 and 3 is the same field:** `strongHighlights[]` (identical to
`definitions[].strongNumber` — I checked; same 5 codes). The prototype used
`definitions[].strongNumber`; `strongHighlights` gives the same answer.

**`preview` is where the spans come from**, and **both** call 1 and call 3 return it. So the
spans can be parsed from either.

---

## 3. What was wrong in the prototype

| I called it | it actually is | verdict |
|---|---|---|
| `layer1_search` `layer1_strong` `layer1_verse` | CALL 1's three parts | **correct** — one call, three tables |
| `layer2_strong` `layer2_related` `layer2_morph` | **CALL 2** (getInfo) | mis-named — it is a different layer from below |
| `layer2_search` `layer2_verse` | **CALL 3** (masterSearch strong=) | **mis-named** — I put two different APIs under "layer 2" |
| `layer3_occurrence` | **not an API output at all** — derived | **DELETE** |
| `layer4_span` | a **parse** of `preview` — not an API output | keep, but it is not an API layer |

**You are right that layer 3 and layer 4 are the same thing.** Every field of
`layer3_occurrence` is either copied from `layer2_verse` or counted from `layer4_span`. It
adds nothing. I introduced it because you described an occurrence layer, and I built it as a
table instead of recognising it was already there.

**And you are right that "layer 2" is multiple pulls for different things.** `layer2_strong` is
`getInfo`; `layer2_search`/`layer2_verse` is `masterSearch`. Two APIs, one layer number. That is
my error, not a property of STEP.

---

## 4. The corrected naming — by the call, not by a number

Since a layer must be *the exact output of one API call*:

| table | call | is |
|---|---|---|
| `c1_word_search` | 1 | the search itself |
| `c1_strong` | 1 | `definitions[]` — word → strong |
| `c1_verse` | 1 | `results[]` — the word's verses |
| `c2_strong_detail` | 2 | `vocabInfos[]` — **the meaning** |
| `c2_related` | 2 | `relatedNos[]` — a repeating group |
| `c2_morph` | 2 | `morphInfos[]` — empty so far |
| `c3_strong_search` | 3 | the search itself |
| `c3_verse` | 3 | `results[]` — the strong's verses |
| `c3_definitions` | 3 | `definitions[]` — **call 3 returns the related lexicon too, and the prototype throws it away** |
| `d_span` | — | **DERIVED**: a parse of `preview`. The first thing that is ours. |

⚠ **The `d_` prefix matters.** Calls 1–3 are what STEP said. `d_span` is what *we read out of the
HTML STEP sent*. It is the first place the study can be wrong on its own account, and it should
never sit in the same numbering as the source.

---

## 5. Your question: are 1, 2 and 3 discovery layers for the span?

**No — and this is the important part.**

| call | discovery? | data the study keeps? |
|---|---|---|
| **1** word → strong | **yes** — it is how the word finds its terms | its `results[]` verses are the same verses call 3 returns; its `definitions[]` are the same codes |
| **2** getInfo | **no** | **★ THE MEANING LIVES HERE.** `mediumDef`, `stepGloss`, `accentedUnicode`, `lsjDefs`, `relatedNos`. Nothing else returns it. This is not a discovery layer — it is the lexicon |
| **3** strong → verses | **no** | **the verses and their previews** — the evidence |
| `d_span` | **no** | the analytical unit |

So: **call 1 is discovery. Calls 2 and 3 are the data.** Call 2 is the meaning; call 3 is the
evidence; the span is what the study reads.

**Which answers "the generation of the meaning of a verse and its span":**

- the **span's** meaning = its code's entry from **call 2** (`stepGloss` / the head of `mediumDef`)
- the **term's** full range = **call 2**'s `mediumDef` tree
- the **verse's** text = **call 3**'s `preview`, stripped
- the **verse's** spans = a **parse** of that same `preview`

**Call 1 contributes nothing the others do not.** Its verses duplicate call 3's; its definitions
duplicate call 3's `definitions[]`. It exists to answer *which strongs*, and after that it is
spent.

---

## 6. Two measured facts that bear on your reading

**Each verse appears once — but a verse can be returned by more than one strong.**

```
CALL 1 (word)       returned 17 verses, 17 distinct
CALL 3 (per strong) returned 18 verses, 17 distinct
    Gal.2.13 was returned by BOTH G5272 and G4942
```

So a `verse` table is keyed by the verse and holds it once. The **(strong, verse)** pair is the
thing that repeats — which is what you meant by *"layer4 is by verse, so raw will only create new
layer4 entries if it has not been done by a prior term cascade"*. Gal 2:13 proves it inside one
word, before any cascade.

**Call 3 returns `definitions[]` and the prototype discards it.** Every verse fetch hands back the
related lexicon for free, and `build_layers.py` only stores it from call 2.

---

## 7. Prototype outputs that are no longer valid

| path | status |
|---|---|
| `layers/*/layer3_occurrence.json` | **INVALID** — derived, duplicates layer 4 |
| `layers/*/layer2_search.json` · `layer2_verse.json` | **MIS-NAMED** — these are call 3, not call 2 |
| `layers/*/layer4_span.json` | **MIS-NAMED** — a derivation, not an API layer |
| `data/peace/*` · `data/hypocrisy/*` (from `build_prototype.py`) | **A DIFFERENT MODEL** — term/sense/span, built before the layer approach. Not wrong, but not this |
| `tables-peace.md` · `tables-hypocrisy.md` | render the above |

**Not deleted.** Renaming and deleting is a decision, and §4 is a proposal, not a ruling.
