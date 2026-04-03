# STEP API Findings — Version, Sub-Gloss Counts, and Term Discovery

Generated: 2026-03-23 (post-summary session recovery)

---

## 1. Version Parameter: `ESV_th`

`ESV_th` is the only ESV module installed in this STEP instance.

| Component | Meaning |
|-----------|---------|
| `ESV` | English Standard Version 2025 |
| `_th` | Tagged Hebrew — Strong's-tagged for entireBible (OT and NT) |

It is a **single version** that handles both OT (H-codes, Hebrew) and NT (G-codes, Greek) Strong's tagging. No separate version is needed for NT queries.

---

## 2. The `count` Field vs Verse Count (Important Distinction)

The `count` field returned by the vocab `getInfo` endpoint is **not the verse count in ESV_th**.

It is the occurrence count across **all tagged texts in the entire STEP installation** (multiple versions combined). It is useful as a relative frequency indicator but must not be used as a verse count for extraction.

To get the actual verse count in ESV_th, use the search API:
`/rest/search/masterSearch/strong={code}|version=ESV_th`

This distinction matters significantly for G5590 where `count=825` but the actual ESV_th verse count is only 46.

---

## 3. H5315 (nephesh) — Complete Sub-Gloss Map

All 8 sibling sub-codes, reachable via `relatedNos` on H5315G:

| Code | STEP Gloss | vocab_count (all versions) | verse_count (ESV_th) |
|------|-----------|---------------------------|----------------------|
| H5315G | soul | 249 | 230 |
| H5315H | soul: life | 211 | 180 |
| H5315I | soul: myself | 133 | 126 |
| H5315J | soul: person | 96 | 83 |
| H5315K | soul: animal | 13 | 12 |
| H5315L | soul: appetite | 47 | 45 |
| H5315M | soul: dead | 13 | 13 |
| H5315N | soul: neck | 2 | 2 |
| **TOTAL** | | **764** | **691** (with possible cross-verse overlaps) |

The DB currently only contains verses registered against the H5315G–N sub-glosses as extracted to date. The base code `H5315` (without letter suffix) resolves to H5315G only — it does **not** return all 8 sub-glosses in a single call.

### H5315 Related (non-sibling) terms from `relatedNos` on H5315G:
- `H5305` (Naphish — proper noun, related by root)
- `H5314` (nāphash — "be refreshed")
- `H5317` (nōpheth — "honeycomb/drippings" — edge case, may be separate root)

---

## 4. G5590 (psuchē) — Complete Sub-Gloss Map

All 5 sub-codes, reachable via `relatedNos` on G5590G:

| Code | STEP Gloss | vocab_count (all versions) | verse_count (ESV_th) |
|------|-----------|---------------------------|----------------------|
| G5590G | soul | 825 | 46 |
| G5590H | soul: life | 42 | 33 |
| G5590I | soul: myself | 6 | 6 |
| G5590J | soul: person | 10 | 8 |
| G5590K | soul: animal | 1 | 0 |
| **TOTAL** | | **884** | **93** (with possible overlaps) |

Against NT concordance expectation of ~103 occurrences of ψυχή — 93 is plausible if ~10 verses use untagged or differently-tagged forms.

### G5590 Related (non-sibling) terms from `relatedNos` on G5590G:
8 Greek compound words:
- `G0674` (apsuchós — faint-hearted)
- `G0895` (apsuchos — lifeless/inanimate)
- `G1374` (dipsuchos — double-minded)
- `G1634` (ekpsuchō — give up the ghost / expire)
- `G2174` (eusucheō — be encouraged)
- `G2473` (isopsuchos — like-minded, same soul)
- `G3642` (oligopsuchos — faint-hearted/timid)
- `G4861` (sumpsuchos — united in spirit)
- `G5591` (psuchikos — natural/unspiritual/soulish)

---

## 5. The `soul~` Fuzzy Search Is NOT the Semantic Cluster

Running `text=soul~` against STEP returns 649 verses via Lucene fuzzy text matching. This is **not appropriate** for term discovery. The results include:
- H0853 (direct object marker ʾet) — 57 occurrences (pure grammatical particle)
- H7586 (Šāʾûl = the name Saul) — 32 occurrences
- H3605 (kōl = "all/every") — numerous
- 250+ total distinct Strong's codes

These are co-occurring tokens in verses that happen to contain the English word "soul" (fuzzy), not semantically related concepts.

**The correct mechanism for term discovery is the `relatedNos` field in the vocab response.**

---

## 6. Proposed Phase 1 Discovery Script Architecture

### Input
`--english=soul` (or any English anchor word)

### Process
1. Run English text search (`text=+soul`) → identify primary Strong's codes (H5315, G5590)
2. For each primary code, call `getInfo` for the base code → read `relatedNos`
3. For each code in `relatedNos`:
   - Fetch vocab (gloss, mediumDef, count, stepTransliteration)
   - Run verse search → get verse_count in ESV_th
4. Separately enumerate sub-siblings (letter-suffix codes) if not already in relatedNos
5. Structure all data into a term map

### Outputs (no DB writes)
- `data/discovery/soul_term_map_YYYYMMDD.json` — full structured term data
- `data/discovery/soul_triage_YYYYMMDD.md` — researcher decision table:
  - Columns: `code | gloss | translit | verse_count | medium_def | include? | notes`
  - Blank `include?` and `notes` columns for researcher to fill in

### What it does NOT do
- No DB writes
- No verse extraction
- No flag evaluation
- No existing data modification

---

## 7. Current DB Gaps for Soul (registry 182)

| Problem | Detail |
|---------|--------|
| G5590 only 46 verses | Only G5590G was searchd; G5590H–J adds ~47 more verses |
| H5315 base not in DB | H5315 (no letter suffix) resolves to H5315G; approach: use sub-codes only |
| WR-08 | G5590 returns 0 verses flag — suppressed by status_note (not yet patched) |
| WR-19 | G5590 parse warning — under investigation |
