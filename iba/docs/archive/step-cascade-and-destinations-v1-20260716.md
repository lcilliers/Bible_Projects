# STEP → DB: the cascade, its API calls, and where the data lands — v1, 2026-07-16

> **What this answers.** Which data comes from STEP, which table and column each field
> lands in, how the cascade works (word → terms → related terms → verses), and the API
> call sequence that produces it.
>
> **Traced from the code that actually runs**, not from documentation:
> `scripts/word_study_extract.py` (the pull), `engine/audit_word.py` (the DB write),
> `scripts/analytics/step_client.py` (the calls), and the live schema register
> `iba/config/DBSchema/DBSchema.json`. Call counts are measured, not estimated.
>
> **Two programs, not one.** `word_study_extract.py` calls STEP and writes **no DB** —
> it produces an artefact. `audit_word.py` reads that artefact and writes the DB. Nothing
> goes STEP → DB directly. Every field below therefore survives two hops, and things are
> lost at both.

---

## 1. The cascade

Four levels. The word is the entry; verses are the leaves.

```
WORD  ("spirit")                      word_registry (pre-existing; not written by the pull)
 │
 ├─ L1  meanings= search ─────────────▶ the PRIMARY TERMS (candidate anchors)
 │         search.masterSearch.meanings
 │         → definitions[].strongNumber        e.g. H7307G, H5397, G4151 …
 │         particle codes H9xxx/G9xxx dropped
 │
 └─ for each primary term:
     │
     ├─ L2  cluster ────────────────────▶ SUB-GLOSSES + RELATED TERMS
     │         get_related_term_cluster(code)
     │           · module.getInfo (the code itself)
     │           · module.getInfo × A..Z suffix probe   ← stops at first miss
     │           · module.getInfo + masterSearch.strong  per related code
     │         → primary_vocab · sub_glosses[] · related_terms[]
     │
     ├─ L3  full vocab per term ────────▶ wa_term_inventory · mti_terms · wa_term_related_words
     │         module.getInfo per sub-gloss and per related term
     │         then filters F0–F5 → include / exclude
     │
     ├─ L3b MEANING EXTRACTION ─────────▶ wa_meaning_parsed · wa_meaning_sense
     │         NO STEP CALL — parses text already pulled       · wa_meaning_stem · wa_lsj_parsed
     │         mediumDef → numbered senses / stems / domains
     │         lsjDefs   → LSJ gloss, domains, etymology
     │         engine/meaning_parser.py, run from audit_word
     │
     └─ L4  verses, INCLUDED terms only ▶ wa_verse_records · wa_verse_term_links
               get_verse_records_with_html(variant) per morphology variant
                 · module.getInfo        (resolve)
                 · masterSearch.strong   (read total)
                 · masterSearch.strong   (duplicate — see §5)
                 · masterSearch.strong × ceil(total/60)   forward-walk
```

### When a TERM is the input, not a word

Already implemented: `--anchors H7307G`. `build_clusters` skips the `meanings=` search
entirely and uses the given codes as the candidate list
(`word_study_extract.py:162-167`). **L1 disappears; L2/L3/L4 are identical.** That is
exactly the behaviour you described — the multiple primary terms are a word-search
concern only, and the rest of the cascade is untouched.

One consequence worth seeing: `definition_codes` is then empty, so **filter F0 never
fires**. F0 is the rule that promotes a term to `include` because STEP curated it as
semantically relevant. With a term as input, terms are judged only by F1–F5
(proper-noun, particle ceiling, section type, root confirmation). **The same term can
therefore be included via a word entry and excluded via a term entry.** That is a real
behavioural fork between your two entry points.

---

## 2. What lands, per level

### L3 — the term → `wa_term_inventory` (`audit_word.py:781`)

| STEP field (raw) | via client key | → column |
|---|---|---|
| `vocabInfos[].strongNumber` | `strong_number` | `term_id`, `strongs_number` |
| `vocabInfos[].stepTransliteration` | `transliteration` | `transliteration` |
| `vocabInfos[].stepGloss` | `gloss` | `step_search_gloss`, `word_analysis_gloss` (**both**) |
| `vocabInfos[].count` | `occurrence_count` | `occurrence_count` |
| `vocabInfos[].mediumDef` | `medium_def` | `meaning` |
| *(derived: regex on mediumDef)* | `meaning_numbered` | `meaning_numbered` |
| `vocabInfos[].lsjDefs` | `lsj_entry` | `lsj_entry` |
| `vocabInfos[].shortDefMounce` | `short_def_mounce` | `short_def_mounce` |
| *(derived from code prefix)* | `language` | `language` |

### L3 — the term → `mti_terms` (`audit_word.py:815`)

`strongs_number` · `transliteration` · `gloss` · `language` · `owning_registry` ·
`owning_registry_fk` · `owning_word` · `extraction_date`.

Only four of these are STEP data; the rest is registry linkage.

### L3 — related terms → `wa_term_related_words` (`audit_word.py:763`)

| STEP field | → column |
|---|---|
| `relatedNos[].strongNumber` | `strongs_number` |
| `relatedNos[].gloss` | `gloss` |
| `relatedNos[].stepTransliteration` | `transliteration` |
| `relatedNos[].matchingForm` | **nowhere** — the script form is dropped |

### L3b — the meaning → four tables (`engine/meaning_parser.py`)

**No STEP call.** This level re-reads text already pulled at L3 and turns it into
structure. It is the study's D101 sense authority, so it is not an afterthought — a thin
meaning starves the dimension that already failed acceptance.

`parse_term(vocab)` reads exactly four fields (`meaning_parser.py:219`):
`language` · `medium_def` · `lsj_entry` · `strong_number`.

| STEP field | parsed into | → table.column |
|---|---|---|
| `mediumDef` | numbered sense tree (`1)`, `1a)`, `1b1)`) | `wa_meaning_sense.level_code`, `.level_depth`, `.parent_level_code`, `.sense_text`, `.sort_order` |
| `mediumDef` | Hebrew stem labels (Hiphil / Piel …) | `wa_meaning_stem.stem_name`, `.stem_type`, `.sense_count`, `.top_sense_text`; `wa_meaning_sense.is_stem_label`, `.stem_label` |
| `mediumDef` | domain tags | `wa_meaning_sense.domain_tag` |
| *(derived)* | counts + flags | `wa_meaning_parsed.top_sense_count`, `.stem_count`, `.has_causative_stem`, `.has_domain_tags`, `.parse_warnings`, `.parse_version` |
| `lsjDefs` | LSJ structure | `wa_lsj_parsed.raw_lsj`, `.lsj_gloss`, `.lsj_domains`, `.lsj_philosophical_note`, `.lsj_etymology_note`, `.lsj_cognate_forms` |
| *(link)* | | `wa_term_inventory.parsed_meaning_id` ← `wa_meaning_parsed.id` |

### ★ L3b is starved by one line, and it explains three defects at once

`audit_word` does not hand the parser the vocab. It rebuilds a **`medium_def`-only** dict
— at `audit_word.py:1263` from the artefact, and at `:1274` from the DB:

```python
vocab_map[jt["code"]] = {"medium_def": md}          # the artefact HAS language, lsj_entry, code
vocab_map[code] = {"medium_def": row["meaning"]}    # the DB row has strongs_number too
```

`parse_term` then reads four fields and finds one. The other three silently take their
defaults:

| parser reads | gets | consequence |
|---|---|---|
| `vocab.get("language", "Hebrew")` | **"Hebrew", always** | every Greek term is parsed by the Hebrew parser |
| `vocab.get("medium_def", "")` | present | the only thing that works |
| `vocab.get("lsj_entry", "")` | **"", always** | `wa_lsj_parsed` never populated |
| `vocab.get("strong_number", "")` | **"", always** | the parsed meaning cannot name its own term |

**Measured against the live DB, 2026-07-16:**

```
wa_meaning_parsed.language        Greek 9    |  Hebrew 7,739
wa_meaning_parsed.strongs_number  populated 12  |  empty 7,736
wa_lsj_parsed                     9 rows     |  2,211 terms hold an lsj_entry
```

And the correct rows are **the same rows on every axis** — 9 Greek, all with a populated
Strong's, all with an LSJ entry (G4273, G2118, G4145–G4149, G4433, G4434), plus 3 Hebrew
(H6223, H6238, H6239). Those 12 came through **`gap_fill.py`**, which calls
`run_parser_for_file` with real vocab straight from `StepClient` (`gap_fill.py:43`).
Everything else came through `audit_word`.

So `wa_meaning_parsed.language` is not "wrong on 31% of rows" — **it was never a
classification.** It is a default that fired 7,739 times. Same for `strongs_number`. And
`wa_lsj_parsed` has not "stalled" — it was never fed. The parser is not at fault; its
caller is.

⚠ The Hebrew parser running on Greek text means the **sense trees for every Greek term in
the study were built by the wrong parser.** That is `wa_meaning_sense`, 17,125 rows, and
it is D101's evidence base. Not assessed here.

### L4 — verses → `wa_verse_records` (`audit_word.py:1082`)

| STEP field | → column |
|---|---|
| `results[].key` | `reference` |
| `results[].osisId` | *(parsed)* → `book_id`, `chapter`, `verse_num`, `testament` |
| `results[].preview` | *(HTML stripped)* → `verse_text` |
| `results[].preview` | *(span parsed)* → `target_word`, `span_strong_match` |
| `results[].preview` | *(morph parsed)* → `morph_code`, and `stem` derived from it |
| *(computed)* | `context_before`, `context_after` |
| *(hard-coded `'ESV'`)* | `translation` |

### L4 — the span link → `wa_verse_term_links` (`audit_word.py:1110`)

`step_subgloss_code` ← `span_code_found` · `step_subgloss_label` ← `span_label_found` ·
`span_strong_match` · `target_word`.

---

## 3. Pulled from STEP and never landed

Checked against every column in the live schema, not assumed:

| STEP field | status |
|---|---|
| `vocabInfos[].accentedUnicode` — **the Hebrew/Greek script form** (`רוּחַ`) | in the artefact; **no column in `wa_term_inventory` or `mti_terms`**. Only `lexicon.original_unicode` exists, in a different table on a different path. |
| `vocabInfos[].freqList` | in the artefact; **no column anywhere** |
| `vocabInfos[].rawRelatedNumbers` | in the artefact; **no column anywhere** |
| `relatedNos[].matchingForm` | **not even in the artefact** |
| `definitions[]` on `masterSearch.strong` — related terms + `popularity` | **never read at all** (see §4) |
| `definitions[].popularity` | **no column anywhere** |
| `_step_Type`, `_zh_*`, `_es_*`, timings, `signature` | correctly ignored — noise |

**And one that is worse than missing:** `causative_form_present` **has a column**
(`wa_term_inventory.causative_form_present`), **is computed by the client**, **is carried
in the artefact** — and the INSERT at `audit_word.py:781` does not include it. Pulled,
homed, and dropped on the floor. (`wa_meaning_parsed.has_causative_stem` is a *second*
home for the same fact, derived independently by the parser — so the concept has two
columns, one never written and one written from a Hebrew-only parse.)

**`lsjDefs` is pulled twice and used never.** It reaches `wa_term_inventory.lsj_entry`
(2,211 terms hold one) via the L3 insert, and it is *supposed* to reach `wa_lsj_parsed`
via L3b — but the parser is never given it. So the raw text is stored and the structure it
exists to produce is not.

`occurrence_count_qualifier` and `also_spelled` also have columns and are documented in
`step_client.py` as unavailable from the API — those are honest gaps, not defects.

---

## 4. The finding that bears on the cascade

`search.masterSearch.strong` returns a **`definitions[]` array** alongside the verses —
for `H7307G`, 7 related terms, each with `strongNumber`, `matchingForm`,
`stepTransliteration`, `gloss`, `type`, `popularity`. The client reads only `total` and
`results` (`step_client.py`), so this is discarded on **every verse fetch**.

`getInfo`'s `relatedNos` for the same term is also 7 entries. **If those two sets are the
same, a single `masterSearch.strong` already returns both the verses and the related
terms, and part of the L2/L3 cluster walk is buying what L4 was given free.** I have not
compared them field-by-field — the dumps to do it are in
`outputs/step-api-probe-20260716/`, and it needs no new calls.

This is your "recycle the response" question, and it is answerable from data already on
disk.

---

## 5. Measured call cost

For `H7307` (194 verses), instrumented, preflight excluded:

| operation | calls |
|---|---|
| `get_vocab_info` | 1 |
| `get_verse_records` | 7 |
| `extract_word_data` | 8 |

Of those 8, **2 are exact duplicates**: `getInfo` is issued by `get_vocab_info` and again
by `_resolved_strong` inside `get_verse_records` (the resolved code is already sitting in
the vocab dict as `strong_number`); and the unranged `masterSearch` is issued once to
read `total` and immediately again by `_paginate_all` for the same purpose.

**A whole word is far larger.** Per primary term the cluster walk costs 1 `getInfo`, up to
26 suffix-probe `getInfo` calls, then a `getInfo` **plus** a `masterSearch` per related
code — and `H0430` listed 46 related codes. Then L3 re-fetches `getInfo` for every
sub-gloss and related term already probed in L2. Then L4 costs ~7 per included term.
A word with several primaries and dozens of related terms runs to **hundreds of calls**,
a large share of them repeats.

The forward-walk is unavoidable: STEP reports `pageSize: 60`/`pageNumber: 1` but honours
neither — four syntaxes tested, all returned page 1.

---

## 6. Open — not decided here

- **★ The `vocab_map` starvation** (§2, L3b) — one line, three defects, 7,739 rows of
  wrong-parser output. The fix is to pass the vocab the artefact already carries. Not
  touched. Re-parsing is possible without STEP: `scripts/_realign_meaning_tables.py`
  already exists and states "no STEP API needed" — the `mediumDef` and `lsj_entry` are
  in `wa_term_inventory`, so the meaning layer can be rebuilt from the DB once the caller
  is fixed.
- **The Greek sense trees** — 17,125 `wa_meaning_sense` rows built by the Hebrew parser
  for every Greek term. Extent unassessed.
- **The L2/L4 overlap** (§4) — compare `relatedNos` against `definitions[]`. Cheap, no calls.
- **The two duplicate calls** (§5) — real, unfixed. Flagged, not touched.
- **`causative_form_present`** — column exists, value exists, INSERT omits it; and the
  concept has a second home in `wa_meaning_parsed.has_causative_stem`.
- **The script form has no home** — `accentedUnicode` is the actual Hebrew/Greek word and
  it is not stored with the term.
- **F0 fires only on word entry** (§1) — the same term can be included via one entry
  point and excluded via the other.
- **`bible.getBibleText`** — unprobed; the only capped-free verse route.
