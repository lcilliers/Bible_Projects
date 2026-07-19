# The raw process — its 4 tables

> **v1 · 2026-07-17.** The config build-out for `module.raw`, from the researcher's
> specification. **All the work is in this document. No config created or loaded.**
>
> **The spec:** *"the raw process will produce 4 tables (no duplicates on any level) for each
> registry word. layer 1 table — word-strong table. layer 2 Strong table (old term table) is
> strong meaning — no duplicate strongs. layer 3 (verse record) no duplicate verse. The verse
> does not belong to a strong. There is a many to many index between strong and verse. layer 4
> (span per verse) parsing the span of the verse. verse-span position is the key. The columns of
> each of the 4 tables is exactly the output of the search, plus the additional columns such as
> id, FK, Deleted."*
>
> Every column below is **measured from the live API**, not remembered.

---

## 1. The shape

```
  registry word
        │
   ┌────▼─────────┐   L1 · word_strong        which strongs this word maps to
   │ word_strong  │        no duplicate (word, strong)
   └────┬─────────┘
        │
   ┌────▼─────────┐   L2 · strong             the strong AND ITS MEANING
   │   strong     │        no duplicate strong
   └────┬─────────┘
        │
   ┌────▼─────────┐   ── strong_verse         the m:m index
   │ strong_verse │        "STEP says this strong is in this verse"
   └────┬─────────┘        no duplicate (strong, verse)
        │
   ┌────▼─────────┐   L3 · verse              the verse itself
   │    verse     │        no duplicate verse · DOES NOT BELONG TO A STRONG
   └────┬─────────┘
        │
   ┌────▼─────────┐   L4 · span               the verse parsed into its words
   │    span      │        key = (verse, position)
   └──────────────┘
```

**The verse does not belong to a strong.** `strong_verse` carries that relationship, and it is
many-to-many in both directions: one strong is in many verses; **one verse holds many strongs**.

⚠ **Measured, in one word, before any cascade:** `Gal.2.13` was returned by the search for
`G5272` **and** by the search for `G4942`. Two strongs, one verse. If the verse belonged to a
strong it would be stored twice — which is what the old DB does.

---

## 2. L1 · `word_strong`

**Source:** CALL 1 · `masterSearch version=<v>|meanings=<word>` → `definitions[]`
**Grain:** one row per (word, strong) · **no duplicate (word, strong)**

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `word_fk` | the run | ours · FK → the registry word |
| `strong_fk` | — | ours · FK → `strong` |
| `deleted` | — | ours |
| `strongNumber` | API | the code the word maps to |
| `matchingForm` | API | the script form, as this search reports it |
| `stepTransliteration` | API | |
| `gloss` | API | |
| `type` | API | `word` / `verb` |
| `popularity` | API | ⚠ **equals CALL 2's `count`** — the same fact from two calls |
| `popularityList` | API | ⚠ **equals CALL 2's `freqList`** |
| `_zh_Gloss` `_es_Gloss` `_zh_tw_Gloss` | API | translations |

**All 10 API fields kept.** ⚠ **Seven of them are facts about the STRONG, not about the pair** —
`matchingForm`, `stepTransliteration`, `gloss`, `type`, `popularity`, `popularityList`, and the
translations all reappear in L2. Keeping them here means the same fact is stored once per word
that finds the strong. **That is the old `wa_term_inventory` defect exactly** — `H3588A` stored 18
times, once per word.

**Decision needed.** Either:
- **(a)** L1 holds only `word_fk · strong_fk` + the fields that are genuinely about the *pair*
  (which, on this evidence, is **none**) — and everything else lives in L2; or
- **(b)** L1 holds the full search output verbatim, per the spec, and is understood as **a record
  of what the word search returned**, not as term data. L2 remains the only place a strong's facts
  are read from.

**(b) is what the spec says** — *"the columns are exactly the output of the search"* — and it is
defensible: L1 is the answer to *"what did the word search say"*, which is provenance, and
provenance is per-search. But then **nothing may ever read a gloss from L1.**

---

## 3. L2 · `strong` — "the old term table" · **the meaning**

**Source:** CALL 2 · `module.getInfo/<v>//<strong>//` → `vocabInfos[]`
**Grain:** one row per strong · **no duplicate strong**

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `deleted` | — | ours |
| `strongNumber` | API | **the key** · ⚠ may differ from what was requested — see §7 |
| `accentedUnicode` | API | **the actual Hebrew/Greek word.** No column for this exists in the old DB's term tables |
| `stepGloss` | API | |
| `stepTransliteration` | API | |
| **`mediumDef`** | API | **★ THE MEANING.** `': <head>' + newline + the lemma's tree` where the code is a sense; the lemma's own definition where it is not |
| `lsjDefs` | API | LSJ, Greek only |
| `shortDefMounce` | API | Mounce, Greek only |
| `rawRelatedNumbers` | API | the related codes, as a string |
| `count` | API | ⚠ **a token count, and it does not reconcile with the tagging** — `G5272` count 7, 6 verses, 6 spans. It is STEP's own frequency figure, not a count of ESV_th occurrences |
| `freqList` | API | |
| `_step_Type` | API | |
| `_zh_tw_Definition` `_vi_Definition` `_es_Definition` `_zh_Definition` | API | |
| `_zh_Gloss` `_es_Gloss` `_zh_tw_Gloss` | API | |

**All 18 API fields kept.** This is the table the study has never had: **the meaning, once per
strong.**

⚠ **`relatedNos[]` is a repeating group** and cannot be a column. It is either a 5th table
(`strong_related`, FK → `strong`) or it is dropped in favour of `rawRelatedNumbers` (the same
codes, as a string, minus their glosses). **The spec says 4 tables. This is the one thing in the
API output that does not fit in 4.**

---

## 4. `strong_verse` — the m:m index

**Source:** CALL 3 · `masterSearch strong=<strong>|version=<v>` → which verses came back
**Grain:** one row per (strong, verse) · **no duplicate (strong, verse)**

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `strong_fk` | the call's input | ours · FK → `strong` |
| `verse_fk` | API `osisId` | ours · FK → `verse` |
| `deleted` | — | ours |

**This is the table that makes "the verse does not belong to a strong" true.** It is also the
only record of *what STEP asserted* — as distinct from what our span parse found. Keeping both
lets one check the other. **Measured: they agree, 35/35 senses on `peace`, 0 missed, 0 invented.**

⚠ **Is this a 5th table, or part of L3?** The spec says 4 tables and then names this index. It has
no API fields of its own — it is pure relationship — so it may be what you meant by L3 carrying
it.

---

## 5. L3 · `verse`

**Source:** CALL 3 · `results[]`
**Grain:** one row per verse · **no duplicate verse** · **does not belong to a strong**

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `deleted` | — | ours |
| `key` | API | `Mat 23:28` — the human reference |
| `osisId` | API | `Matt.23.28` — **the key** |
| `preview` | API | the verse's **full interlinear HTML** — every word, with its strong and morph |

**Only 3 API fields.** `preview` is the whole verse, not just the searched strong's word — which
is why L4 can exist without another call.

⚠ **`preview` is HTML, and it is the source of L4.** Keeping it verbatim is what makes L4
re-derivable — the same reason `verse_morphology_raw` exists in the old DB (25,634 rows, one per
verse). Without it, a parse fix means re-fetching the canon.

⚠ **Two verses, two previews, one truth?** `Gal.2.13` came back from both `G5272`'s and `G4942`'s
search. Both carry a `preview`. They should be byte-identical — **not verified**. If they are not,
"no duplicate verse" needs a rule for which wins.

---

## 6. L4 · `span`

**Source:** a **PARSE** of `verse.preview`. **Not a call.**
**Grain:** one row per word of a verse · **key = (verse, position)**

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `verse_fk` | — | ours · FK → `verse` |
| `position` | the parse | **★ part of the key** — the word's index in the verse |
| `deleted` | — | ours |
| `surface` | parsed | the English word(s) the span covers |
| `strong` | parsed | ⚠ **may name SEVERAL codes**: `'H7307G H9002'` — the word *and its attached particles* |
| `morph` | parsed | ⚠ **positionally aligned with `strong`**: `'HNcfsc HC'` |

**Only 3 parsed fields**, and two of them are lists in a string.

⚠ **This is the only table that is OURS.** L1–L3 are what STEP said. L4 is what we read out of the
HTML STEP sent — the first place the study can be wrong on its own account. It earned that
warning: the span regex was silently corrupt (a literal `0x08` where `\b` belonged) and produced
0 rows while printing identically to the correct pattern.

⚠ **`strong` and `morph` hold multiple values.** `'H7307G H9002'` = *ruach* + the attached waw
("**and** the Spirit"). Either the span row keeps them as lists, or a span decomposes into one row
per code — which would break "verse-span position is the key", because two codes share a position.
**Not decided.**

---

## 7. What must be ruled before this is authored

| # | question | why |
|---|---|---|
| **Q1** | **L1: full search output, or just the pair?** (§2) | 7 of its 10 fields are facts about the *strong*, and repeat per word. Storing them per-word is the exact `wa_term_inventory` defect. The spec says keep them; then nothing may read a gloss from L1 |
| **Q2** | **`relatedNos[]` — a 5th table, or dropped?** (§3) | a repeating group cannot be a column. `rawRelatedNumbers` has the codes but not their glosses. **This is the signal cluster assignment compares against**, so dropping the glosses has a cost |
| **Q3** | **`strong_verse` — a 5th table, or part of L3?** (§4) | it has no API fields; it is pure relationship |
| **Q4** | **L4: `strong`/`morph` as lists, or one row per code?** (§6) | one row per code breaks (verse, position) as the key |
| **Q5** | **CALL 2 can answer about a different code than the one asked.** | `getInfo//H7307//` returns `H7307G`. So `strong.strongNumber` ≠ the requested code. **Which is the key?** The old `lexicon` table filed the answer under the *request* and thereby stored `H7307G`'s meaning under `H7307` — one arbitrary sense per lemma, mislabelled |
| **Q6** | **`popularity`/`popularityList` (L1) == `count`/`freqList` (L2).** | the same fact from two calls. Which is authoritative? |
| **Q7** | **Is `preview` stored twice for a verse two strongs found?** (§5) | not verified byte-identical |

---

## 8. Against the old DB

The researcher: *"this is actually very similar to what the old DB already have, just with a bit
more rigidity and predictability and more concise."* Measured:

| new | old | difference |
|---|---|---|
| `word_strong` | `wa_term_inventory` (7,844) + `mti_terms` (7,861) | **two tables did this job**, and both also held the strong's facts, per word. `H3588A` appears 18×. The new L1 does the linking only |
| `strong` | `lexicon` (11,666) | old: base codes only — **0 of 11,666 end in a letter** — and each holds one arbitrary sense's payload under the base key. New: one row per strong, sense codes included |
| `verse` | `verse` (25,634) + `wa_verse_records` (247,046) | ★ `wa_verse_records` is **one row per term-in-verse** — the verse stored once per strong that found it. The new `verse` + `strong_verse` split is exactly the correction |
| `strong_verse` | `wa_verse_term_links` (237,531) · `verse_term_index` (275,593) | **two tables, one fact**, both derivable |
| `span` | `verse_morphology` (325,507) + `verse_span_index` (325,474) | old: two copies, and `verse_span_index` carries an analytical overlay (`role`, `char_candidate`, `characteristic`) stamped onto a mechanical table. The new `span` is the mechanical half only |
| `verse.preview` | `verse_morphology_raw` (25,634) | the same idea, already proven: keep the raw HTML so the parse is re-derivable |

**247,046 → 25,634.** `wa_verse_records` stores the verse once per term-in-verse. The
`verse` + `strong_verse` split stores it once and indexes the rest. That is the concision.

Researcher comments

Q1+Q2
L1 does not carry any columns about the strong, except the strong number, it is practically just the index to show the origin of the strongs per STEP either the word or another strong.The key for this table is the unique strong number with two additional columns, the word, and another strong. This is derived from the related numbers of the strongs , where a related number references a strong that is already in this list linked to a word, it is not duplicated, but ignored. 
L2 carries all the detail for a strong and the FK is L1 with each L1 requiring only 1 L2.  Exclude related no as a column. it is captured in L1.
L3 have verses for all the strong in L1 and L2 (by implication all related strongs also)
Q3 - strong_verse is an index many to many relationship. it cannot be part of L3.
Q4 - L4 is the old master. The API data is position, span number (strong variant), span, gloss, transliteration, also include verse_id, candidate_char (after seeding process), role (after analytics), status, deleted
Q5 - I dont understand the issue
Q6 - L2 only.
Q7 - span is stored once in L4 for the verse. I suggest we add a column to show the count.
