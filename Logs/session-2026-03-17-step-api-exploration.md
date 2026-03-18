# STEP API Exploration — Working Log
**Session date:** 2026-03-17  
**Goal:** Discover whether the locally-running STEP Bible (localhost:8989) exposes a REST API that can replace manual copy-paste of word analysis data in Session A.

---

## Status summary (updated in place)

| Item | Status |
|---|---|
| REST endpoint discovery | ✅ Done |
| Vocab/lexicon endpoint | ✅ Working |
| Verse search endpoint | ✅ Working |
| >60 verse pagination | ✅ Solved (section-range workaround) |
| Torah sub-split (3 missing verses) | ✅ Fixed (2-layer section splits) |
| Non-canonical Strong's | ✅ Characterised |
| Multi-gloss / suffixed Strong's | ✅ Characterised + fixed |
| `step_client.py` rewrite | ✅ Done |
| `lsjDefs` / `shortDefMounce` extraction | ✅ Done |
| `meaning_numbered` / `causative_form_present` derivation | ✅ Done |
| `testament` / `book_code` / `chapter` / `verse_num` in verse records | ✅ Done |
| Complete Session A field mapping | ✅ Done (see §8) |
| End-to-end test | ✅ Passing (all 4 cases) |

---

## 1. How STEP's REST API was found

STEP's web UI at `http://localhost:8989/` works fine, but every documented `/rest/` endpoint was returning:
```json
{"errorMessage": "An unexpected error has occurred..."}
```

**Root cause hunt path:**
- Checked JS bundle (`step.26.1.2.min.js`) — URL patterns fully obfuscated into variables, no extractable strings
- Inspected the install dir: `C:\Program Files (x86)\STEP\step-web\WEB-INF\classes\`
- Found controller `.class` files in `...rest\controllers\`
- Parsed the Java bytecode constant-pool strings from `StepRequest.class`
- This revealed the routing logic string:  
  `'module' → ' getInfo getQuickInfo getAllModules ...'`  
  `'search' → ' suggest masterSearch getSubjectVerses getExactForms'`
- Format confirmed: `rest/<controller>/<method>/<pipe-separated-args>`

---

## 2. Working REST endpoints (confirmed)

### Vocab / Lexicon
```
GET /rest/module/getInfo/{version}//{STRONG}//
e.g. /rest/module/getInfo/ESV_th//H8057//
```
Returns `vocabInfos[]` with:
- `strongNumber` — the resolved STEP identifier (may differ from input, see §5)
- `accentedUnicode` — Hebrew/Greek script
- `stepTransliteration` — e.g. `sim.chah`
- `stepGloss` — primary English gloss
- `count` — occurrence count (token-based, not verse-based)
- `mediumDef` — multi-line HTML definition with sub-senses
- `relatedNos[]` — related Strong's with their forms and glosses
- `rawRelatedNumbers` — comma-separated string
- `freqList` — raw frequency-distribution string

**Example output for H8057 (simkhah):**
```json
{
  "strongNumber": "H8057",
  "accentedUnicode": "שִׂמְחָה",
  "stepTransliteration": "sim.chah",
  "stepGloss": "joy",
  "count": 94,
  "mediumDef": "1) joy, mirth, gladness<br>1a) mirth, gladness...",
  "relatedNos": [
    {"strongNumber":"H8055","gloss":"to rejoice","stepTransliteration":"sa.mach"},
    {"strongNumber":"H8056","gloss":"glad","stepTransliteration":"sa.me.ach"},
    {"strongNumber":"H8063","gloss":"rug","stepTransliteration":"se.mi.khah"}
  ]
}
```

### Verse search
```
GET /rest/search/masterSearch/strong={STRONG}|version={VERSION}
e.g. /rest/search/masterSearch/strong=H8057|version=ESV_th
```
Returns `results[]` each with:
- `key` — display ref, e.g. `"Gen 31:27"`
- `osisId` — machine ref, e.g. `"Gen.31.27"`
- `preview` — HTML of the verse with `<span strong='...' morph='...'>` tagging

**Clean ESV text** is obtained by stripping HTML tags from `preview`.  
**Target word** (the specific English word rendering H8057) is extracted by finding the `<span>` whose `strong` attribute contains the target Strong's number.

Example from Gen 31:27:
```html
<span morph='HNcfsa HR HSp2ms' strong='H8057 H9003 H9031'>mirth</span>
```
→ target_word = `mirth`

---

## 3. The 60-result page cap — and the solution

`masterSearch` returns **maximum 60 results** regardless of `pageSize` or `pageNumber` parameters. All pagination token formats tested return the same first page.

**Workaround:** restrict search to canonical Bible sections using the `reference=` token. Each emotional/theological vocabulary word has fewer than 60 occurrences per section.

Sections used:
| Section | Range |
|---|---|
| Torah | Gen.1.1 – Deut.34.12 |
| History | Josh.1.1 – Esth.10.3 |
| Poetry | Job.1.1 – Song.8.14 |
| Prophets | Isa.1.1 – Mal.4.6 |
| NT | Matt.1.1 – Rev.22.21 |

**Verified for H8057 (94 tokens, 89 verses):**
- Without range: returns 60 results, misses 3 Ecc + 26 Song-Mal
- With Torah + History + Poetry + Prophets + NT: returns all 89 unique verses ✅

---

## 4. Non-canonical STEP Strong's numbers

Several terms in the word analysis pipeline have STEP-internal Strong's numbers that do not match the standard Kohlenberger/Goodrick system:

| Strong's | STEP gloss | Vocab data | Verse search |
|---|---|---|---|
| G9559 | to procrastinate | ✅ Returns | ❌ 0 results |
| G9073 | strength (physical) | ✅ Returns | ❌ 0 results |
| G6347 | without strength | ✅ Returns | ❌ 0 results |
| H9002 | and (conjunctive vav) | ✅ Returns | ✅ Returns (14,359 verses!) |
| H9001 | & (verbal vav) | ✅ Returns | ❌ 0 results |

**Finding:** G9xxx numbers are STEP-internal semantic/grammatical markers not tagged in verse text. H9xxx covers STEP's vav-prefix tagging — H9002 (conjunctive vav) is fully verse-tagged. No canonical verse tagging exists for G9559/G9073/G6347.

**Implication for the pipeline:** When a word study contains Greek G9xxx terms, those terms can return vocab data (gloss, definition) but no verse list. The `step_client.py` detects this and adds a warning note in the returned data.

---

## 5. STEP-suffixed Strong's numbers and multi-gloss handling

Some base Strong's numbers resolve to **suffixed** forms inside STEP:

| Input | STEP resolves to | Example |
|---|---|---|
| H2428 (chayil) | H2428A | "strength: soldiers" — the primary/ambiguous form |
| H0157 (ahab) | H0157G | "to love: lover" |

**Why this matters:** Verse search using `H2428` returns 0 results. Verse search using `H2428A` returns 101 results. The vocab endpoint exposes the resolved identifier in `vocabInfos[0].strongNumber`.

**The cha.yil multi-gloss case:**  
`H2428` → resolves to `H2428A` (strength/soldiers) with `count=110`  
Definition: `1) strength, might, efficiency, wealth, army`  
This is a genuinely multi-sense word. STEP's `stepGloss` gives the primary gloss; the `mediumDef` gives the full multi-sense structure.

**Fix in `step_client.py`:** `get_verse_records()` now calls `_resolved_strong()` which does a lightweight vocab lookup to get the canonical form before submitting the verse search.

---

## 6. What the verse preview HTML gives us

Each `preview` field in the verse results is fully inline-tagged HTML:
```html
<span morph='HNcfsa HR HSp2ms' strong='H8057 H9003 H9031'>mirth</span>
```

This tells us:
- `strong='H8057 H9003 H9031'` — the Hebrew word is tagged with H8057 (our target) + H9003 (preposition ב) + H9031 (pronominal suffix)
- `morph='HNcfsa...'` — morphology code (noun, feminine, singular, absolute)
- The ESV rendering for this specific word instance is `mirth`

The **exact English rendering per verse** is extracted automatically. For H8057 across 89 verses, the renderings include: `joy`, `mirth`, `gladness`, `rejoicing`, `joyously` — this is directly usable for the translation-diversity analysis in Session A.

---

## 7. What `step_client.py` now provides

The rewritten `analytics/step_client.py` exposes three methods:

### `get_vocab_info(strong) → dict`
Returns:
```python
{
  "strong_number":          "H8057",       # resolved STEP form
  "language":               "Hebrew",      # 'Hebrew' or 'Greek'
  "hebrew_unicode":         "שִׂמְחָה",
  "transliteration":        "sim.chah",
  "gloss":                  "joy",         # = step_search_gloss
  "occurrence_count":       94,            # tokens (not verses)
  "medium_def":             "1) joy, mirth, gladness\n1a) ...",
  "meaning_numbered":       True,          # contains 1), 1a)... sub-senses
  "causative_form_present": False,         # True if Hiphil or Piel in def
  "lsj_entry":              "",            # LSJ text for Greek; "" for Hebrew
  "short_def_mounce":       "",            # Mounce short def for Greek; "" for Hebrew
  "related_words":          [{"strong":"H8055","form":"שָׂמַח","gloss":"to rejoice","translit":"sa.mach"}, ...],
  "raw_related_numbers":    "H8055, H8056, H8063",
  "freq_list":              "94@89;..."
}
```

### `get_verse_records(strong) → list[dict]`
Returns (fully paginated, deduplicated, sorted):
```python
[
  {
    "osisId":      "1Chr.12.40",
    "ref":         "1Ch 12:40",
    "esv_text":    "...for there was joy in Israel.",
    "target_word": "joy",
    "testament":   "OT",         # 'OT' or 'NT'
    "book_code":   "1Chr",       # OSIS book code
    "chapter":     12,
    "verse_num":   40,
  },
  ...
]
```

### `extract_word_data(strong) → dict`
Returns the complete package:
```python
{
  "strong":        "H8057",
  "vocab":         {...},          # from get_vocab_info
  "verse_records": [...],          # from get_verse_records
  "verse_count":   89,
  "testament":     "OT",           # 'OT', 'NT', 'both', or None
  "notes":         []              # warnings if any
}
```

---

## 8. Complete mapping: Session A fields → STEP API

This table covers every field Session A Phase 2 writes to the database.  
Fields are listed by database table/block in patch import order.

### `wa_term_inventory` — core term record

| Session A field | API source | Extraction method | Notes |
|---|---|---|---|
| `strongs_number` | `vocab.strong_number` | Direct | Resolved form (e.g. H0157G not H0157) |
| `transliteration` | `vocab.transliteration` | Direct | STEP romanisation |
| `step_search_gloss` | `vocab.gloss` | Direct | The gloss in the STEP verses header |
| `word_analysis_gloss` | `vocab.gloss` | Direct | Same field; may be reformatted in source file heading |
| `language` | `vocab.language` | Derived: H-prefix → Hebrew, G → Greek | Returned by `get_vocab_info()` |
| `occurrence_count` | `vocab.occurrence_count` | Direct integer | Token count; NOT verse count |
| `occurrence_count_qualifier` | ❌ Not in API | — | STEP UI only. Set `null`; fill from source file if STEP shows "about N" |
| `meaning` | `vocab.medium_def` | HTML-stripped, newlines preserved | Full multi-line definition |
| `meaning_numbered` | `vocab.meaning_numbered` | Derived: regex for `1)`, `1a)` etc. | Hebrew rows only; omit for Greek |
| `also_spelled` | ❌ Not in API | — | STEP UI "Also means:" display only. Fill from source file. Hebrew only |
| `lsj_entry` | `vocab.lsj_entry` | `lsjDefs` field, HTML-stripped | Greek only; `""` for Hebrew |
| `testament` | `data.testament` | Derived from verse_records book codes | `'OT'`, `'NT'`, or `'both'` |
| `god_as_subject` | Partial: meaning text | Keyword search for "God" as subject | Final judgment is researcher's (0/1) |
| `somatic_link` | Partial: meaning text | Keyword search for body-organ terms | Final judgment is researcher's (0/1) |
| `causative_form_present` | `vocab.causative_form_present` | Derived: Hiphil or Piel in `medium_def` | Returns bool |
| `status_note` | `data.notes` | Join warning strings | Includes suffix resolution, mismatch notes |

### `wa_term_related_words` — one row per related word

| Field | API source | Extraction method |
|---|---|---|
| `gloss` | `vocab.related_words[i].gloss` | Direct |
| `transliteration` | `vocab.related_words[i].translit` | Direct |

### `wa_verse_records` — one row per verse

| Field | API source | Extraction method |
|---|---|---|
| `reference` | `verse_records[i].ref` | Direct (e.g. `"Gen 31:27"`) |
| `verse_text` | `verse_records[i].esv_text` | HTML-stripped preview |
| `testament` | `verse_records[i].testament` | Derived from `book_code` vs `_NT_BOOKS` |
| `book_id` | `verse_records[i].book_code` | DB query: `book_code_variants WHERE code = book_code` |
| `chapter` | `verse_records[i].chapter` | Parsed from osisId (middle segment) |
| `verse_num` | `verse_records[i].verse_num` | Parsed from osisId (last segment) |
| `translation` | Constant `'ESV'` | Always ESV_th module |
| `term_id` | `vocab.strong_number` | Direct |
| `transliteration` | `vocab.transliteration` | Direct |

> **Note on `target_word`:** The specific English rendering per verse is extracted into `verse_records[i].target_word` and is available for translation-diversity analysis. It is not a column in `wa_verse_records` (schema has no such column). This field can be used for review but is not persisted.

### Automatically derivable phase2 flags

These flags can be set programmatically from API data alone:

| Flag | Condition | Source |
|---|---|---|
| `HIGH_FREQUENCY_ANCHOR` | `occurrence_count >= 200` | `vocab.occurrence_count` |
| `CAUSATIVE_OF_INNER_STATE` | `causative_form_present = True` | `vocab.causative_form_present` |
| `THIN_DATA` | `verse_count < 5` | `data.verse_count` |
| `SMALL_VERSE_SAMPLE` | `verse_count / occurrence_count < 0.2` and `occurrence_count >= 20` | Ratio |
| `NO_WORD_ANALYSIS` | `medium_def` is empty | `vocab.medium_def` |
| `SEMANTIC_RANGE_BREADTH` | Meaning contains 4+ distinct numbered top-senses | Parse `medium_def` |

### Flags requiring researcher judgment (cannot derive from API)

`GOD_AS_SUBJECT`, `SOMATIC_INNER_LINK`, `BODY_INNER_EXPRESSION`, `SOMATIC_EXPRESSION`,  
`NT_FACULTY_NAMING`, `DIVINE_HUMAN_PARALLEL`, `ESCHATOLOGICAL_USAGE`,  
`WISDOM_LITERATURE_CONCENTRATION`, `METAPHOR_ROOT`, `RELATIONAL_DIRECTION`,  
`VOLITIONAL_COMPONENT`, `CROSS_TESTAMENT_SHIFT`, `MULTI_REGISTRY_ANCHOR`,  
`GENERATION_RESOLUTION_PAIR`, `ARAMAIC_FORM`, `THEOLOGICAL_ANCHOR`, `CONSOLIDATION_CANDIDATE`

---

## 9. Known limitations / gaps

1. **`occurrence_count_qualifier` not in API.**  
   The "about N times" qualifier shown in the STEP UI is a display convention only. The API returns the raw integer `count` with no qualifier flag. Set to `null` unless the source file explicitly shows "about".

2. **`also_spelled` not in API.**  
   The "Also means: form (script 'gloss' Strong's)" line in the STEP word analysis display is a UI-generated cross-reference. It does not appear in `mediumDef` or any other API field. This field must be filled from the researcher's source file.

3. **Non-canonical G9xxx verse retrieval.**  
   G9559 / G9073 / G6347 return vocab data but no verse records — these are STEP-internal SEMR identifiers not used in verse tagging. Terms with these numbers need manual handling.

4. **Multi-gloss dispatch.**  
   cha.yil (H2428) resolves to H2428A. If the word study intends to differentiate H2428 (base form) from its suffixed sub-entries, that would need explicit handling beyond what the current client does.

5. **`freq_list` encoding undocumented.**  
   The `freqList` field (e.g. `"94@89;94@89;..."`) appears to encode frequency distributions but the format is not documented by STEP. Not used in current extraction.

6. **Section sub-splits have one level of recursion.**  
   If a half-section exceeds 60 results (would require ~120+ occurrences in half the OT), the current code would miss verses. No word in the current Soul Word pipeline reaches this threshold — but very high-frequency terms (e.g. H2896 `tov` = good, ~750 occurrences) would need further subdivision.

---

## 10. Next steps

- [x] Fix the 3-missing-verse edge case (Torah sub-split — resolved ✅)
- [x] Complete Session A field mapping (resolved ✅)
- [ ] Update `docs/step_setup.md` to document the local API and `step_client.py` usage
- [ ] Consider a `step_client.get_word_analysis_block()` that returns a structured dict ready for patch JSON production, mapping all extractable Session A fields into their target columns
