# The raw process — its 4 tables · v2

> **v2 · 2026-07-17.** Rebuilt from the researcher's inline replies to v1. v1 had L1 wrong.
> **All the work is in this document. No config created or loaded.**

---

## 1. What v1 got wrong

I built **L1 as the columns of the word search** (`definitions[]`). The researcher's model is
different and better:

> *"L1 does not carry any columns about the strong, except the strong number. It is practically
> just the index to show the origin of the strongs per STEP — either the word or another strong.
> The key for this table is the unique strong number with two additional columns, the word, and
> another strong. This is derived from the related numbers of the strongs, where a related number
> references a strong that is already in this list linked to a word, it is not duplicated, but
> ignored."*

**L1 is not the search output. L1 is the strong-origin index** — the deduplicated list of every
strong in play for this word, and where each one came from.

---

## 2. The shape

```
  registry word
        │  meanings=<word>  →  seed strongs
        ▼
  ┌──────────────┐   L1 · strong_origin     one row per STRONG (unique) · origin: word or from_strong
  │ strong_origin│        relatedNos expand here; a strong already listed is IGNORED
  └────┬─────────┘
       │  one L1 : one L2
  ┌────▼─────────┐   L2 · strong             all the strong's detail · relatedNos EXCLUDED (it is L1)
  │   strong     │        no duplicate strong
  └────┬─────────┘
       │
  ┌────▼─────────┐   ── strong_verse         m:m index · NOT part of L3 (researcher)
  │ strong_verse │        no duplicate (strong, verse)
  └────┬─────────┘
       │
  ┌────▼─────────┐   L3 · verse              verses for ALL strongs in L1 · no duplicate verse
  │    verse     │        does not belong to a strong
  └────┬─────────┘
       │
  ┌────▼─────────┐   L4 · span               THE OLD MASTER · key = (verse, position)
  │    span      │        + candidate_char (post-seed) + role (post-analytics)
  └──────────────┘
```

---

## 3. L1 · `strong_origin` — the index

**What it is:** every strong in play for this word, deduplicated, with where it came from.
**Built by:** seed from `meanings=<word>`, then expand each strong's `relatedNos`. A related code
**already in the list is ignored**, not duplicated.
**Grain:** one row per strong · **the strong number is the key (unique)**

| column | notes |
|---|---|
| `id` | ours |
| `strong` | **the key — unique** |
| `word_fk` | the registry word this strong traces to (null if it entered via a related strong) |
| `from_strong_fk` | the strong whose `relatedNos` brought it in (null if it came straight from the word) |
| `deleted` | ours |

**No column about the strong except its number.** All of that is L2. L1 is *origin only*: this
strong is here because the word found it, or because that strong is related to it.

**This is where `relatedNos` is captured** (researcher, Q2) — as new rows, not as a column in L2.

### ⚠ The one thing that must be ruled: how deep does `relatedNos` expand?

Measured on `hypocrisy`:

| depth | L1 size | what it is |
|---|---|---|
| **one level** — seed strongs + their direct `relatedNos` | **23** | the concept: hypocrisy · hypocrite · pretend · genuine · profane · smooth |
| **recursive** — keep expanding until nothing new | **87 and still growing at round 6** | drifts into `H2585` (Enoch), `H4256` (a temple division), phonetically-adjacent roots — no longer the concept |

The dedup rule prevents *loops*, but not *sprawl* — it stops revisiting, not wandering. **One
level is bounded and on-concept. Recursive is not.** Which does the spec mean?

*(`relatedNos` returns resolved codes, so this is a clean lexical web — distinct from the
co-occurrence web of L4's strongs, which the researcher already gated behind candidacy.)*

---

## 4. L2 · `strong` — the detail · **the meaning**

**Source:** `getInfo/<v>//<strong>//` → `vocabInfos[]`
**Relationship:** FK → L1 · **each L1 has exactly one L2** (researcher, Q2)
**Grain:** one row per strong · no duplicate

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `l1_fk` | — | ours · FK → `strong_origin` |
| `deleted` | — | ours |
| `strongNumber` | API | |
| `accentedUnicode` | API | the actual Hebrew/Greek word |
| `stepGloss` | API | |
| `stepTransliteration` | API | |
| **`mediumDef`** | API | **★ the meaning** — `': head' + tree` |
| `lsjDefs` | API | Greek only |
| `shortDefMounce` | API | Greek only |
| `rawRelatedNumbers` | API | the related codes as a string |
| `count` | API | **the frequency lives HERE only** (Q6) |
| `freqList` | API | here only (Q6) |
| `_step_Type` · `_vi/_es/_zh` definitions and glosses | API | |

**`relatedNos[]` EXCLUDED** (Q2) — it is captured in L1. This resolves v1's Q2: the repeating
group does not need a 5th table, because its content becomes L1 rows.

⚠ **`rawRelatedNumbers` stays as a string.** It is the same codes as `relatedNos`, minus their
glosses. It is redundant with L1's rows — keep it as verbatim provenance, or drop it? (Minor.)

---

## 5. `strong_verse` — the m:m index

**Researcher, Q3:** *"strong_verse is an index many to many relationship. it cannot be part of
L3."* So it is its own table.

**Source:** which verses `masterSearch strong=<strong>` returned.
**Grain:** one row per (strong, verse) · no duplicate

| column | notes |
|---|---|
| `id` | ours |
| `strong_fk` | FK → `strong` |
| `verse_fk` | FK → `verse` |
| `deleted` | ours |

---

## 6. L3 · `verse`

**Researcher:** *"L3 have verses for all the strong in L1 and L2 (by implication all related
strongs also)."* So a verse is pulled for **every** strong in L1, and stored once.

**Source:** `masterSearch strong=<strong>` → `results[]`
**Grain:** one row per verse · no duplicate · does not belong to a strong

| column | from | notes |
|---|---|---|
| `id` | — | ours |
| `deleted` | — | ours |
| `key` | API | `Mat 23:28` |
| `osisId` | API | the key |
| `preview` | API | the verse's full interlinear HTML — the source of L4 |

---

## 7. L4 · `span` — "the old master"

**Researcher, Q4:** *"L4 is the old master. The API data is position, span number (strong
variant), span, gloss, transliteration, also include verse_id, candidate_char (after seeding
process), role (after analytics), status, deleted."*

**This is a decision I had wrong twice.** I kept insisting the analytical overlay
(`role`, `char_candidate`) must be stripped from the span master — because that is what
`gate.base.no-judgement` and the old-DB migration do. **The researcher rules the opposite:** L4
**is** the master, and the overlay is added to it in place, after the later stages.

**Source:** a parse of `verse.preview`, then enriched by later stages.
**Grain:** one row per span · **key = (verse, position)**

| column | from | when | notes |
|---|---|---|---|
| `id` | — | — | ours |
| `verse_fk` | parse | raw | ours · FK → `verse` |
| `position` | parse | raw | **part of the key** |
| `strong_variant` | parse | raw | the span's strong code — "span number (strong variant)" |
| `span` | parse | raw | the surface word(s) |
| `gloss` | strong | raw | from the span's strong |
| `transliteration` | strong | raw | from the span's strong |
| `count` | — | raw | ⚠ Q7 — see below |
| `candidate_char` | — | **after seeding** | ⚠ filled by the seeding stage, which runs after ALL registry words are built |
| `role` | — | **after analytics** | ⚠ filled by the lexical analysis stage |
| `status` | — | — | |
| `deleted` | — | — | ours |

⚠ **`candidate_char` and `role` are written by later stages, not by raw.** Raw creates the row and
leaves them null. This is the researcher's earlier ruling made concrete: *"backtrack on layer for
missing strongs only happens after candidate char seeding, and only for chars. Seeding takes place
after all registry words have been built."* So the span master is built empty of judgement by raw,
and the judgement columns are filled in place later — **not a separate table.**

⚠ **`gloss` and `transliteration` on the span come from its strong.** So L4 references L2 (via the
strong_variant), or they are copied in at build. Which?

⚠ **Q7 — the count column.** Researcher: *"span is stored once in L4 for the verse. I suggest we
add a column to show the count."* I need this pinned: count of **what**? Options — the number of
times this strong occurs in this verse; the number of strongs this verse was returned by; the
number of L1 strongs that name this span. **State which.**

⚠ **`strong_variant` may be several codes.** The preview gives `strong='H7307G H9002'` — the word
plus its attached particles. Is `strong_variant` the head code only (`H7307G`), with the particles
dropped or held elsewhere? "**And** the Spirit" vs "the Spirit" is `H9002`, and that is meaning.

---

## 8. Answers logged

| Q (v1) | researcher | effect |
|---|---|---|
| Q1 | L1 is an index: strong (key) + word + from_strong. No strong columns. | §3 — L1 rebuilt |
| Q2 | L2 has all detail, FK→L1, 1:1. Exclude relatedNos — it is in L1. | §4 — no 5th table for relatedNos |
| Q3 | strong_verse is m:m, cannot be part of L3. | §5 — its own table |
| Q4 | L4 is the old master + candidate_char + role + status. | §7 — overlay stays IN the master |
| Q5 | "I don't understand the issue." | **Dropped** — a non-issue: relatedNos and meanings= both return resolved codes, so getInfo always returns the code asked. The base-vs-resolved trap needs a base code as input, which never happens here. |
| Q6 | count/freqList — L2 only. | §4 |
| Q7 | span stored once; add a count column. | §7 — ⚠ count of what? |

---

## 9. Still open

| # | question | §|
|---|---|---|
| **O1** | **`relatedNos` depth — one level (23) or recursive (87+, sprawling)?** | §3 |
| **O2** | **Q7 — the count column counts what?** | §7 |
| **O3** | `strong_variant` — head code only, or the particles too? | §7 |
| **O4** | L4's `gloss`/`transliteration` — a reference to L2, or copied at build? | §7 |
| **O5** | `rawRelatedNumbers` — keep as verbatim string, or drop (redundant with L1)? | §4 |
