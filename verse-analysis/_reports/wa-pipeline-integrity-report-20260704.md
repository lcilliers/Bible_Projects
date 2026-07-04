# Pipeline-integrity diagnostic — verse-analysis chain (live from DB)

> Read-only trace generated 2026-07-04 05:37 UTC by `scripts/_assess_pipeline_integrity_v1_20260704.py`. Scope: the 5 wisdom/poetry books. Tracks issues across `verse → morphology/span-index → ve_lexical → segment_unit → lexical_prose_chapter` + the parallel `wa_verse_records`. **A clean line = 0.** Bold non-zero = rows to chase (examples capped at 25).

## 0. Lexical→verse→prose funnel (per book)
`present/canon`=verse rows vs canonical · `Ph1`=process_marker set · `has_lex`=≥1 ve_lexical · `in_unit`=covered by a segment_unit (Psalms = chapter-driven, no units) · `ch_prose`=chapters with a filed reading · `v→noProse`=verses whose chapter has no reading.

| Book | present/canon | Ph1 | has_lex | in_unit | ch_prose | v→noProse |
|---|---|---|---|---|---|---|
| Psalms | 2461/2461 | 2461 | 2461 | — (chapter-driven) | 150 | 0 |
| Proverbs | 915/915 | 915 | 915 | 857 | 31 | 0 |
| Ecclesiastes | 222/222 | 222 | 222 | 221 | 12 | 0 |
| Job | 1070/1070 | 1070 | 1070 | 1070 | 42 | 0 |
| Lamentations | 154/154 | 154 | 154 | 154 | 5 | 0 |

## 1. Verse-record completeness — `wa_verse_records`
**Verses analysed (Phase-1 marked) but absent from `wa_verse_records`** — the expected gap for STEP-*backfilled* verses (backfill writes `verse`+morphology+span-index, **not** `wa_verse_records`).

| Book | Ph1-marked | in wa_verse_records | **analysed NOT in verse-record** | orphaned records |
|---|---|---|---|---|
| Psalms | 2461 | 2144 | **317** | 0 |
| Proverbs | 915 | 839 | **76** | 0 |
| Ecclesiastes | 222 | 202 | **20** | 0 |
| Job | 1070 | 962 | **108** | 0 |
| Lamentations | 154 | 134 | **20** | 0 |

- **Psalms** — 317 analysed verses not in `wa_verse_records`: Psa 2:3, Psa 2:4, Psa 4:6, Psa 8:3, Psa 8:8, Psa 9:20, Psa 10:9, Psa 12:5, Psa 13:6, Psa 17:5, Psa 17:11, Psa 18:8, Psa 18:10, Psa 18:11, Psa 18:12, Psa 18:14, Psa 18:26, Psa 18:29, Psa 18:36, Psa 18:41, Psa 18:42, Psa 19:4, Psa 19:6, Psa 21:12, Psa 22:7 … (+292 more)
- **Proverbs** — 76 analysed verses not in `wa_verse_records`: Pro 1:1, Pro 1:14, Pro 1:32, Pro 2:1, Pro 2:16, Pro 3:10, Pro 3:11, Pro 4:15, Pro 4:17, Pro 5:8, Pro 5:14, Pro 5:15, Pro 5:16, Pro 5:17, Pro 6:2, Pro 6:8, Pro 6:15, Pro 6:20, Pro 6:27, Pro 7:6, Pro 7:8, Pro 7:9, Pro 7:12, Pro 7:14, Pro 7:16 … (+51 more)
- **Ecclesiastes** — 20 analysed verses not in `wa_verse_records`: Ecc 1:1, Ecc 1:2, Ecc 1:6, Ecc 1:9, Ecc 1:10, Ecc 1:15, Ecc 2:6, Ecc 2:25, Ecc 3:3, Ecc 3:5, Ecc 3:9, Ecc 7:13, Ecc 9:14, Ecc 10:7, Ecc 10:8, Ecc 10:11, Ecc 10:16, Ecc 11:7, Ecc 12:2, Ecc 12:8
- **Job** — 108 analysed verses not in `wa_verse_records`: Job 1:2, Job 1:13, Job 3:2, Job 3:5, Job 4:1, Job 5:14, Job 6:1, Job 6:18, Job 8:1, Job 8:17, Job 9:1, Job 9:8, Job 9:9, Job 11:1, Job 11:4, Job 11:17, Job 12:1, Job 12:18, Job 12:23, Job 12:25, Job 14:2, Job 14:5, Job 15:1, Job 15:3, Job 15:27 … (+83 more)
- **Lamentations** — 20 analysed verses not in `wa_verse_records`: Lam 1:1, Lam 3:2, Lam 3:6, Lam 3:10, Lam 3:14, Lam 3:16, Lam 3:37, Lam 3:40, Lam 3:44, Lam 3:45, Lam 3:50, Lam 3:54, Lam 3:64, Lam 4:18, Lam 4:19, Lam 5:3, Lam 5:4, Lam 5:13, Lam 5:14, Lam 5:21

## 2. Term-verse-span-index & morphology completeness
A verse with 0 spans **cannot be lexicalised**. `span≠morph` = span-index and morphology word-counts disagree.

| Book | verses | no span-index | no morphology | span≠morph |
|---|---|---|---|---|
| Psalms | 2461 | 0 | 0 | 0 |
| Proverbs | 915 | 0 | 0 | 0 |
| Ecclesiastes | 222 | 0 | 0 | 0 |
| Job | 1070 | 0 | 0 | 0 |
| Lamentations | 154 | 0 | 0 | 0 |

- *(no gaps — every verse has span-index and morphology)*

## 3. Lexical completeness & dimensions that fell by the wayside
### 3a. Phase-1-marked verses producing ZERO `ve_lexical` (lexical silently failed)

| Book | Ph1-marked | with ≥1 lexical | **marked but 0 lexical** |
|---|---|---|---|
| Psalms | 2461 | 2461 | **0** |
| Proverbs | 915 | 915 | **0** |
| Ecclesiastes | 222 | 222 | **0** |
| Job | 1070 | 1070 | **0** |
| Lamentations | 154 | 154 | **0** |

- *(no gaps — every Phase-1-marked verse produced lexical rows)*

### 3b. Dimension (ve_nr) coverage per book — thin or absent items
`·` = 0 rows. Cross-verse items (`source` D2, `effect`) are OFF by design in poetic mode → expect ~0. Dropped-by-design (**D10 valence, D12 hidden, D13 cohabitation, related_tier**) are absent programme-wide — correct. A *core* item (`sense`/`type`/`role`) going thin would be a real failure.

| Book | sense​(101) | type​(102) | source​(103) | seat​(104) | bearer​(105) | operation​(106) | target​(107) | manner​(108) | intensity​(109) | specifier​(110) | effect​(111) | coupling​(112) | prohibition​(113) | discovery​(114) | role​(115) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Psalms | 14974 | 14974 | · | 401 | 3170 | 7187 | 986 | 1784 | 1860 | 1821 | · | 1784 | 1262 | 3887 | 14974 |
| Proverbs | 5610 | 5610 | · | 206 | 264 | 2249 | 461 | 461 | 412 | 584 | · | 461 | 698 | 694 | 5610 |
| Ecclesiastes | 2063 | 2063 | · | 104 | 11 | 830 | 273 | 195 | 427 | 229 | · | 195 | 250 | 121 | 2063 |
| Job | 5450 | 5450 | · | 131 | 381 | 2789 | 416 | 597 | 280 | 505 | · | 597 | 858 | 719 | 5450 |
| Lamentations | 1175 | 1175 | · | 28 | 253 | 548 | 79 | 117 | 184 | 169 | · | 117 | 156 | 308 | 1175 |

### 3c. Gate-1 tagged terms missing a CORE item (sense/type/role expected on every tagged term)

| Book | gate-1 spans | missing sense | missing type | missing role |
|---|---|---|---|---|
| Psalms | 3925 | 0 | 0 | 0 |
| Proverbs | 1796 | 0 | 0 | 0 |
| Ecclesiastes | 464 | 0 | 0 | 0 |
| Job | 1275 | 0 | 0 | 0 |
| Lamentations | 270 | 0 | 0 | 0 |

## 4. Verses / units that never reached prose
### 4a. Phase-1 verses whose chapter has NO prose reading (broken chain)

- *(none — every Phase-1 chapter has a filed reading)*

### 4b. Verses covered by NO segment_unit (segmented books; Psalms excluded)
Expected non-zero only for intended skips (bare superscriptions, e.g. `Job 1:1`, `Ecc 1:1`). Anything else = a missed verse.

- **Proverbs** — 58 verse(s) in no unit: Pro 6:1, Pro 6:2, Pro 6:5, Pro 8:22, Pro 8:23, Pro 8:25, Pro 8:26, Pro 8:27, Pro 8:29, Pro 17:6, Pro 17:24, Pro 18:16, Pro 20:1, Pro 20:13, Pro 20:20, Pro 20:30, Pro 22:26, Pro 22:27, Pro 22:28, Pro 22:29, Pro 23:10, Pro 23:13, Pro 23:21, Pro 24:27, Pro 24:28 … (+33 more)
- **Ecclesiastes** — 1 verse(s) in no unit: Ecc 1:1

### 4c. Prose chapters with NO Phase-1 verses (reverse orphan)

- *(none — every filed reading rests on Phase-1 verses)*

---
*Chase any **bold non-zero** above. Re-run: `python scripts/_assess_pipeline_integrity_v1_20260704.py`.*
