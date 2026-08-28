# wa-090-innocence — Analysis Readiness Output (v6)

_v6 generation · 2026-05-02T15:24:48Z · schema 3.17.0 · catalogue v2-2026-04-29 (T0–T7)_

_Sections aligned with `wa-sessionb-analysis-output [current]` reading units 1-9 + §10 (second-tier catalogue)._

_Source of truth: live DB at generation time. Regenerate to refresh._

**Section map:**

- A. Registry overview — Unit 1
- B. Stage 1 Completion Record (synthesised) — instruction S2 prerequisite
- C. Term inventory — Unit 1 prep
- D. OWNER terms — lexical foundation — Unit 3
- E. XREF terms — Unit 2
- F. Verse context groups landscape — Unit 4 (with dimension assignments)
- G. Correlation signals — Unit 5 (computed)
- H. Existing SD pointers + session_b_findings — Units 6 + 9
- I. Thin-evidence phase2 flags — Unit 8
- J. Anchor verse material — Unit 7 (full verbatim verse text)
- K. Legacy-VC terms — UNVERIFIED — v2 strategy mandate
- L. Stage 2b reference — observation question catalogue
- N. Open Session B items (carried forward; must resolve this session)
- M. Readiness verification

---

## A. Registry Overview

- **Registry no:** `90` · **word:** `innocence`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `wa-dimensionreview-instruction-v3_3-20260418`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 27  (programme-wide aggregate including XREF and historical terms — current OWNER count is 22, XREF 4)
- `phase1_verse_count`: 1111  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 3 unresolved · **Existing session_b_findings:** 1

**Description:**

> Innocence is the condition of being genuinely free from guilt in a specific matter — not moral perfection in general but the absence of culpability for a particular wrong. The Hebrew vocabulary here covers integrity, the state of being whole and without hidden fault, and the simple declaration behold, pointing to what is plainly the case. Innocence can be declared (by God, by a judge, by the conscience) and can be established or falsely denied. It is particularly important in psalms of lament where the speaker calls on God to vindicate the innocent.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-02T15:24:48Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 22
- **OWNER terms legacy-VC (not_done):** 22 / 22

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 22 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H2005` | hen | look! | H | `extracted` | **`not_done`** | 1 | 223 | 6/0 | 77/0 | 12 |
| `H2006A` | hen | if | H | `extracted` | **`not_done`** | 1 | 11 | 0/0 | 0/0 | 0 |
| `H2006B` | la.hen | therefore | H | `extracted` | **`not_done`** | 1 | 11 | 0/0 | 0/0 | 0 |
| `H2008` | hen.nah | here/thus | H | `extracted` | **`not_done`** | 1 | 41 | 1/0 | 4/0 | 2 |
| `H2009` | hin.neh | behold | H | `extracted` | **`not_done`** | 1 | 319 | 7/0 | 98/0 | 14 |
| `H2011G` | hin.nom | [Topheth of] Hinnom | H | `extracted` | **`not_done`** | 1 | 2 | 0/0 | 0/0 | 0 |
| `H2011H` | hin.nom | [Topheth of son of] Hinnom | H | `extracted` | **`not_done`** | 1 | 10 | 1/0 | 5/0 | 2 |
| `H3681` | ka.suy | covering | H | `extracted` | **`not_done`** | 1 | 2 | 0/0 | 0/0 | 0 |
| `H3682` | ke.sut | covering | H | `extracted` | **`not_done`** | 1 | 8 | 3/0 | 6/0 | 3 |
| `H4372` | mikh.seh | covering | H | `extracted` | **`not_done`** | 1 | 12 | 0/0 | 0/0 | 0 |
| `H4374` | me.khas.seh | covering | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 1/0 | 1 |
| `H4518` | me.naq.qiy.yah | bowl | H | `extracted` | **`not_done`** | 1 | 4 | 0/0 | 0/0 | 0 |
| `H4974` | me.tom | soundness | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 3/0 | 1 |
| `H5355A` | na.qi | innocent | H | `extracted` | **`not_done`** | 1 | 40 | 3/0 | 39/0 | 6 |
| `H5355B` | na.qi | innocent | H | `extracted` | **`not_done`** | 1 | 40 | 3/0 | 39/0 | 6 |
| `H5356A` | niq.qa.von | innocence | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 4/0 | 2 |
| `H5356B` | qe.ha.von | bluntness | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 4/0 | 2 |
| `H8535` | tam | complete | H | `extracted` | **`not_done`** | 1 | 16 | 2/0 | 13/0 | 4 |
| `H8537` | tom | integrity | H | `extracted` | **`not_done`** | 1 | 23 | 1/0 | 21/0 | 2 |
| `H8549H` | ta.mim | unblemished: blameless | H | `extracted` | **`not_done`** | 1 | 27 | 1/0 | 27/0 | 2 |
| `H8549I` | ta.mim | unblemished: complete | H | `extracted` | **`not_done`** | 1 | 6 | 0/0 | 0/0 | 0 |
| `H8549J` | ta.mim | unblemished: Thummim | H | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H2005` — hen "look!"

**Identity:** mti=5629 · ti=5738 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: interj
1) behold, lo, though hypothetical part
2) if
Aramaic equivalent: hen (הֵן "look!" H2006A)

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (8 total; sample of 8):**
- `H2006A` hen "if"
- `H2006B` la.hen "therefore"
- `H2008` hen.nah "here/thus"
- `H2009` hin.neh "behold"
- `H2011G` hin.nom "[Topheth of] Hinnom"
- `H2011H` hin.nom "[Topheth of son of] Hinnom"
- `H2012` he.na "Hena"
- `H3860` la.hen "therefore"

### `H2006A` — hen "if"

**Identity:** mti=5631 · ti=5740 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: behold, if, whether
Aramaic of hen (הֵן "look!" H2005)

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H2005` hen "look!"
- `H2006B` la.hen "therefore"
- `H2008` hen.nah "here/thus"
- `H2009` hin.neh "behold"
- `H2011G` hin.nom "[Topheth of] Hinnom"
- `H2011H` hin.nom "[Topheth of son of] Hinnom"
- `H2012` he.na "Hena"

### `H2006B` — la.hen "therefore"

**Identity:** mti=5633 · ti=5742 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: therefore
Aramaic of la.hen (לָהֵן "therefore" H3860)

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (6 total; sample of 6):**
- `H2005` hen "look!"
- `H2006A` hen "if"
- `H3859` la.ham "to swallow"
- `H3860` la.hen "therefore"
- `H3861` la.hen "except"
- `H3862` la.ha.qah "company"

### `H2008` — hen.nah "here/thus"

**Identity:** mti=5630 · ti=5739 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: here, there, now, hither

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H2005` hen "look!"
- `H2006A` hen "if"
- `H2006B` la.hen "therefore"
- `H2009` hin.neh "behold"
- `H2011G` hin.nom "[Topheth of] Hinnom"
- `H2011H` hin.nom "[Topheth of son of] Hinnom"
- `H2012` he.na "Hena"

### `H2009` — hin.neh "behold"

**Identity:** mti=930 · ti=980 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: behold, lo, see, if

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H2005` hen "look!"
- `H2006A` hen "if"
- `H2006B` la.hen "therefore"
- `H2008` hen.nah "here/thus"
- `H2011G` hin.nom "[Topheth of] Hinnom"
- `H2011H` hin.nom "[Topheth of son of] Hinnom"
- `H2012` he.na "Hena"

### `H2011G` — hin.nom "[Topheth of] Hinnom"

**Identity:** mti=5634 · ti=5743 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: A location first mentioned at Jos.15.8; 
referred to as Topheth (תֹּ֫פֶת), or "burning-place" (KJV= Tophet, NIV= Topheth) (תׇּפְתֶּה), or Valley/ of Hinnom (הִנֹּם גַּיְא), or Valley/ of the Son of Hinnom (בֵּן הִנֹּם גַּיְא), or Valley/ of Slaughter (הֲרֵגָה גַּיְא), or Valley/ of Baca (NIV= Baka) (בָּכָא עֵ֫מֶק). § a valley (deep and narrow ravine) with steep, rocky sides located southwest of Jerusalem, separating Mount Zion to the north from the 'hill of evil counsel' and the sloping rocky plateau of the 'plain of Rephaim' to the south

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (31 total; sample of 30):**
- `H1056` ba.kha "[Tophet of] Baca"
- `H1516G` gay "Valley"
- `H1516H` gay "[Iphtahel] Valley"
- `H1516I` gay "[Zeboim] Valley"
- `H1516J` gay "[Salt] Valley"
- `H1516K` gay "Ge"
- `H1516L` gay "[Zephathah] Valley"
- `H1516M` gay "Valley [Gate]"
- `H1516N` gay "[Hamon-gog] Valley"
- `H1516O` gay "Valley"
- `H1516P` gay "Gath"
- `H1516Q` gay "Valley"
- `H1516R` gay "valley"
- `H1516S` gay "Valley"
- `H2011H` hin.nom "[Topheth of son of] Hinnom"
- … and 15 more shown of 31 total

### `H2011H` — hin.nom "[Topheth of son of] Hinnom"

**Identity:** mti=5632 · ti=5741 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: Hinnom = "lamentation"
a valley (deep and narrow ravine) with steep, rocky sides located southwest of Jerusalem, separating Mount Zion to the north from the 'hill of evil counsel' and the sloping rocky plateau of the 'plain of Rephaim' to the south

**Root family:**
- `HEN` (Hebrew): if — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (31 total; sample of 30):**
- `H1056` ba.kha "[Tophet of] Baca"
- `H1516G` gay "Valley"
- `H1516H` gay "[Iphtahel] Valley"
- `H1516I` gay "[Zeboim] Valley"
- `H1516J` gay "[Salt] Valley"
- `H1516K` gay "Ge"
- `H1516L` gay "[Zephathah] Valley"
- `H1516M` gay "Valley [Gate]"
- `H1516N` gay "[Hamon-gog] Valley"
- `H1516O` gay "Valley"
- `H1516P` gay "Gath"
- `H1516Q` gay "Valley"
- `H1516R` gay "valley"
- `H1516S` gay "Valley"
- `H2011G` hin.nom "[Topheth of] Hinnom"
- … and 15 more shown of 31 total

### `H3681` — ka.suy "covering"

**Identity:** mti=5628 · ti=5737 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: covering, outer covering

**Root family:**
- `KASAH` (Hebrew): to cover — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H3680` ka.sah "to cover"
- `H3682` ke.sut "covering"
- `H4372` mikh.seh "covering"
- `H4374` me.khas.seh "covering"

### `H3682` — ke.sut "covering"

**Identity:** mti=929 · ti=979 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: covering, clothing

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): covering, clothing
  - `1b` (under `None`): covering (for concealment)

**Root family:**
- `KASAH` (Hebrew): to cover — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H3680` ka.sah "to cover"
- `H3681` ka.suy "covering"
- `H4372` mikh.seh "covering"
- `H4374` me.khas.seh "covering"

### `H4372` — mikh.seh "covering"

**Identity:** mti=5626 · ti=5735 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: a covering

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): covering (of the ark)
  - `1b` (under `None`): covering (of the skins of the tabernacle)

**Root family:**
- `KASAH` (Hebrew): to cover — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H3680` ka.sah "to cover"
- `H3681` ka.suy "covering"
- `H3682` ke.sut "covering"
- `H4374` me.khas.seh "covering"

### `H4374` — me.khas.seh "covering"

**Identity:** mti=5627 · ti=5736 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: covering, that which covers

**Root family:**
- `KASAH` (Hebrew): to cover — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H3680` ka.sah "to cover"
- `H3681` ka.suy "covering"
- `H3682` ke.sut "covering"
- `H4372` mikh.seh "covering"

### `H4518` — me.naq.qiy.yah "bowl"

**Identity:** mti=5623 · ti=5732 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: sacrificial bowl or cup

**Root family:**
- `NAQI` (Hebrew): bowl — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H5352` na.qah "to clear"
- `H5355A` na.qi "innocent"
- `H5355B` na.qi "innocent"
- `H5356A` niq.qa.von "innocence"
- `H5356B` qe.ha.von "bluntness"

### `H4974` — me.tom "soundness"

**Identity:** mti=5641 · ti=5750 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: soundness, entirety, entire

**Root family:**
- `TAM` (Hebrew): complete — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H8535` tam "complete"
- `H8537` tom "integrity"
- `H8538` tum.mah "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549I` ta.mim "unblemished: complete"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `H5355A` — na.qi "innocent"

**Identity:** mti=5621 · ti=5730 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: clean, free from, exempt, clear, innocent

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): free from guilt, clean, innocent
  - `1b` (under `None`): free from punishment
  - `1c` (under `None`): free or exempt from obligations Also means: na.qi (נָקִיא "innocent" H5355B)

**Root family:**
- `NAQI` (Hebrew): bowl — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H4518` me.naq.qiy.yah "bowl"
- `H5352` na.qah "to clear"
- `H5355B` na.qi "innocent"
- `H5356A` niq.qa.von "innocence"
- `H5356B` qe.ha.von "bluntness"

### `H5355B` — na.qi "innocent"

**Identity:** mti=5624 · ti=5733 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: innocent
Another spelling of na.qi (נָקִי "innocent" H5355A)

**Root family:**
- `NAQI` (Hebrew): bowl — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H4518` me.naq.qiy.yah "bowl"
- `H5352` na.qah "to clear"
- `H5355A` na.qi "innocent"
- `H5356A` niq.qa.von "innocence"
- `H5356B` qe.ha.von "bluntness"

### `H5356A` — niq.qa.von "innocence"

**Identity:** mti=928 · ti=978 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: innocency

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): freedom from guilt, innocency
  - `1b` (under `None`): freedom from punishment
  - `1c` (under `None`): cleanness of teeth (physical sense)

**Root family:**
- `NAQI` (Hebrew): bowl — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H4518` me.naq.qiy.yah "bowl"
- `H5352` na.qah "to clear"
- `H5355A` na.qi "innocent"
- `H5355B` na.qi "innocent"
- `H5356B` qe.ha.von "bluntness"

### `H5356B` — qe.ha.von "bluntness"

**Identity:** mti=5620 · ti=5729 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: bluntness)

**Root family:**
- `NAQI` (Hebrew): bowl — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `H5352` na.qah "to clear"
- `H5356A` niq.qa.von "innocence"
- `H6949` qa.hah "be blunt"

### `H8535` — tam "complete"

**Identity:** mti=5638 · ti=5747 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: perfect, complete

Sub-senses (depth > 1): 6 entries — present in DB; first 15:
  - `1a` (under `None`): complete, perfect
  - `1a1` (under `None`): one who lacks nothing in physical strength, beauty, etc
  - `1b` (under `None`): sound, wholesome
  - `1b1` (under `None`): an ordinary, quiet sort of person
  - `1c` (under `None`): complete, morally innocent, having integrity
  - `1c1` (under `None`): one who is morally and ethically pure

**Root family:**
- `TAM` (Hebrew): complete — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8537` tom "integrity"
- `H8538` tum.mah "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549I` ta.mim "unblemished: complete"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `H8537` — tom "integrity"

**Identity:** mti=931 · ti=981 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: integrity, completeness

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): completeness, fulness
  - `1b` (under `None`): innocence, simplicity
  - `1c` (under `None`): integrity

**Root family:**
- `TAM` (Hebrew): complete — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8535` tam "complete"
- `H8538` tum.mah "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549I` ta.mim "unblemished: complete"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `H8549H` — ta.mim "unblemished: blameless"

**Identity:** mti=5637 · ti=5746 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: : blameless
1) complete, whole, entire, sound
1a) complete, whole, entire
1b) whole, sound, healthful
1c) complete, entire (of time)
1d) sound, wholesome, unimpaired, innocent, having integrity
1e) what is complete or entirely in accord with truth and fact (neuter adj/subst)

**Root family:**
- `TAM` (Hebrew): complete — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8535` tam "complete"
- `H8537` tom "integrity"
- `H8538` tum.mah "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549I` ta.mim "unblemished: complete"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `H8549I` — ta.mim "unblemished: complete"

**Identity:** mti=5639 · ti=5748 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: : complete
1) complete, whole, entire, sound
1a) complete, whole, entire
1b) whole, sound, healthful
1c) complete, entire (of time)
1d) sound, wholesome, unimpaired, innocent, having integrity
1e) what is complete or entirely in accord with truth and fact (neuter adj/subst)

**Root family:**
- `TAM` (Hebrew): complete — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8535` tam "complete"
- `H8537` tom "integrity"
- `H8538` tum.mah "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `H8549J` — ta.mim "unblemished: Thummim"

**Identity:** mti=5642 · ti=5751 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:46): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: : Thummim
1) complete, whole, entire, sound
1a) complete, whole, entire
1b) whole, sound, healthful
1c) complete, entire (of time)
1d) sound, wholesome, unimpaired, innocent, having integrity
1e) what is complete or entirely in accord with truth and fact (neuter adj/subst)

**Root family:**
- `TAM` (Hebrew): complete — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8535` tam "complete"
- `H8537` tom "integrity"
- `H8538` tum.mah "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549I` ta.mim "unblemished: complete"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

---

## E. XREF Terms [Unit 2] (4)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `H5352` | na.qah | to clear | H | 173 will | `extracted` | 16 |
| `H8538` | tum.mah | integrity | H | 92 integrity | `extracted` | 5 |
| `H8549G` | ta.mim | unblemished | H | 92 integrity | `extracted` | 51 |
| `H8552` | ta.mam | to finish | H | 147 sin | `extracted` | 26 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H2005` — 6 groups

- **`5629-001`** — 8 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term frames the self-presentation of a person before God or another — offering the self in availability, surrender, or accountability*
- **`5629-002`** — 16 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C10`
  - *Term frames a first-person or communal confessional disclosure of inner condition — guilt, fear, inadequacy, need, or grief — before God*
- **`5629-003`** — 6 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term frames a divine disclosure of God's inner orientation — election, delight, care, and relational approach toward his people*
- **`5629-004`** — 15 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term frames a moral verdict or exposure of the inner being — what God sees, seeks, or judges in the heart, will, and conduct of persons*
- **`5629-005`** — 7 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term frames a personal disclosure of the inner experience of God — searching, hiddenness, helplessness, or submission before divine power*
- **`5629-006`** — 25 relevant · 2 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C10`
  - *Term frames a disclosure of inner knowing, wisdom, awe, or affective orientation — including fear of the Lord, understanding, love, grief, and longing*

### `H2006A` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H2006B` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H2008` — 1 groups

- **`5630-001`** — 4 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C10`
  - *Term marks the temporal extent or ongoing duration of an inner-being state, divine relationship, or orientation — establishing how long the inner condition has persisted or been sustained*

### `H2009` — 7 groups

- **`930-001`** — 6 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term frames the self-presentation of a person before God in obedience, availability, or acknowledgment of inadequacy*
- **`930-002`** — 14 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C10`
  - *Term frames a first-person or communal disclosure of inner need, grief, fear, or moral condition before God*
- **`930-003`** — 5 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term introduces a theophanic vision or divine encounter — making the divine presence directly present to perception*
- **`930-004`** — 17 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term introduces a divine disclosure of God's orientation of love, promise, care, or attentiveness toward his people*
- **`930-005`** — 21 relevant · 2 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term introduces a moral verdict, exposure of inner sin or deception, or inner transformation through divine action*
- **`930-006`** — 13 relevant · 2 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C10`
  - *Term introduces inner wisdom reflection, longing, moral restraint, or the recognition of inner truth*
- **`930-007`** — 22 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C10`
  - *Term introduces the inner experience of anguish, dread, despair, hope, or emotional intensity before God or in life*

### `H2011G` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H2011H` — 1 groups

- **`5632-001`** — 5 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names the place associated with the moral abomination of child sacrifice — an act explicitly contrary to the divine inner will and a marker of the depths of human spiritual corruption*

### `H3681` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H3682` — 3 groups

- **`929-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names a metaphorical covering of moral reproach — the public declaration of innocence and vindication*
- **`929-002`** — 3 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term names the absence of covering as the condition of inner vulnerability and exposure — of the poor, and of the realm of death before God*
- **`929-003`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term frames covering as divine response to vulnerability and divine expression of grief — God's compassion for the exposed and his inner mourning made visible*

### `H4372` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H4374` — 1 groups

- **`5627-001`** — 1 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C10`
  - *Term names what covers the person in death and judgment — the inverted image of pride and pomp brought to humiliation before God*

### `H4518` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H4974` — 1 groups

- **`5641-001`** — 3 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C10`
  - *Term names the absence of soundness as the condition of the person or people under divine discipline or moral corruption — linking physical and inner brokenness*

### `H5355A` — 3 groups

- **`5621-001`** — 18 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term characterizes the person as morally innocent or free from guilt — the inner moral standing of a person before God and the human community*
- **`5621-002`** — 14 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term identifies "innocent blood" as a moral category — the shedding of which constitutes moral pollution and the protection of which is a moral obligation before God*
- **`5621-003`** — 7 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term marks freedom from moral obligation or liability — clearance from a sworn commitment, legal claim, or culpability*

### `H5355B` — 3 groups

- **`5624-001`** — 18 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term characterizes the person as morally innocent or free from guilt — the inner moral standing of a person before God and the human community*
- **`5624-002`** — 14 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term identifies "innocent blood" as a moral category — the shedding of which constitutes moral pollution and the protection of which is a moral obligation before God*
- **`5624-003`** — 7 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term marks freedom from moral obligation or liability — clearance from a sworn commitment, legal claim, or culpability*

### `H5356A` — 1 groups

- **`928-001`** — 4 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names the inner-being quality of innocence — the condition of the heart and hands being free from moral guilt before God*

### `H5356B` — 1 groups

- **`5620-001`** — 4 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names the inner-being quality of innocence — the condition of the heart and hands being free from moral guilt before God*

### `H8535` — 2 groups

- **`5638-001`** — 11 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term characterizes the person as inwardly blameless and morally whole — the quality of inner character that defines one who fears God and turns from evil*
- **`5638-002`** — 2 relevant · 2 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C10`
  - *Term characterizes the beloved as wholly complete and perfect — the wholeness that evokes delight and singular devotion*

### `H8537` — 1 groups

- **`931-001`** — 21 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names integrity as the inner moral condition of the person — the wholeness and blamelessness of heart and conduct that characterizes the one who walks rightly before God*

### `H8549H` — 1 groups

- **`5637-001`** — 27 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term characterizes the person as inwardly blameless and whole before God — the quality of heart and conduct that constitutes right standing and walking in God's presence*

### `H8549I` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H8549J` — 1 groups

- **`5642-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names the Thummim as the instrument of divine disclosure of inner moral guilt — the means by which God reveals what is hidden in the person or community*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 92 integrity | 6 | `H8537,H8549H,H8535,H8549I,H4974,H8549J` |
| 148 sincerity | 6 | `H8537,H8549H,H8535,H8549I,H4974,H8549J` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 73 guilt | 31 |
| 187 strength | 31 |
| 183 heart | 27 |
| 196 power | 27 |
| 197 authority | 26 |
| 77 honesty | 21 |
| 182 Soul | 19 |
| 44 despair | 18 |
| 168 uprightness | 18 |
| 97 joy | 17 |
| 103 love | 16 |
| 78 hope | 15 |
| 98 justice | 14 |
| 100 knowledge | 13 |
| 43 desire | 12 |
| 172 wickedness | 12 |
| 173 will | 12 |
| 34 covenant | 11 |
| 57 evil | 10 |
| 128 rebellion | 10 |
| 23 compassion | 9 |
| 67 goodness | 9 |
| 51 distress | 8 |
| 60 faithfulness | 8 |
| 61 fear | 8 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 4 anger | 1Sa 1:16 |
| 11 awe | Job 1:1 |
| 32 counsel | Job 40:4 |
| 42 delight | Psa 51:6 |
| 44 despair | Psa 15:2 |
| 44 despair | Psa 51:6 |
| 73 guilt | Isa 6:7 |
| 73 guilt | Psa 51:5 |
| 77 honesty | Hab 2:4 |
| 98 justice | Hab 2:4 |
| 103 love | Psa 133:1 |
| 103 love | Song 5:2 |
| 105 lust | Jer 22:17 |
| 111 mercy | 1Sa 12:3 |
| 168 uprightness | Job 1:1 |
| 173 will | Isa 6:8 |
| 178 wrath | Isa 49:16 |
| 180 yielding | Gen 15:3 |
| 183 heart | Hos 2:14 |
| 196 power | Gen 20:5 |
| 196 power | Isa 49:16 |
| 197 authority | Job 40:4 |
| 199 dominion | Song 6:9 |
| 202 transformation | Job 9:11 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-90-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> The functional presentational particles (hen H2005, hinneh H2009, hennah H2008) classified into the innocence registry produce a very wide group range — covering confession, theophany, moral verdict, wisdom reflection, and emotional experience. The innocence registry functions as a container for inner-being disclosure framing. Session B should assess whether this breadth is analytically productive or whether the verse context classifications for these particles should be re-examined.

### H.2 Open SD pointers + research flags (3)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SD_POINTER` | DIM-90-SD001 | HIGH | D | 2026-04-07 |
| `SD_POINTER` | DIM-90-SD002 | HIGH | Session D | 2026-05-02 |
| `SD_CLUSTER` | DIM-C10-SD001 | HIGH | Session D | 2026-05-02 |

#### DIM-90-SD001

> The programme vocabulary has no Emotional/Affective dimension. Multiple groups across C10 — particularly in innocence (930-007: anguish, dread, despair, hope) and goodness (884-003: satisfaction, longing) — describe inner states that resist classification under Moral/Conscience, Spiritual/God-ward, or Character/Disposition. Session D should assess whether the programme vocabulary requires an Emotional/Affective category to adequately map the inner-being landscape.

#### DIM-90-SD002

> R090 innocence shows the highest dimensional breadth of any C10 registry: Moral Character, Emotion-Negative, Emotion-Positive, Transformation, Dependence/Creatureliness, Relational Disposition, and Cognition. This breadth arises partly from the registry's inclusion of presentational-particle terms (hen H2005, hinneh H2009, hennah H2008) which serve as framing particles for inner-being disclosures across all dimensions. Session D should note: (1) the particle vocabulary is not itself an inner-being characteristic but a presentational frame for inner-being content of any kind; (2) pre-existing SD pointer DIM-90-SD001 noted an emotional/affective dimension gap — that gap is not confirmed here; Emotion-Negative and Emotion-Positive are both present and working. The gap question may be more precisely about the adequacy of those two labels to capture the full range of human affective experience, which remains a valid Session D question.

#### DIM-C10-SD001

> C10 cluster-wide pattern: across all 9 registries, Moral Character is the dominant dimension by group count, but the cluster consistently shows a secondary Relational Disposition signal — especially in the direction GOD-toward-HUMAN (divine compassion, election, covering) and HUMAN-toward-GOD (self-availability, fear of the Lord, worship in truth). The moral quality of C10 is never purely self-referential; it always implies a relational orientation. This supports a Session D observation that moral character in Scripture is inherently relational — constituted in and expressed through relationship with God, not as a free-standing self-achieved virtue. This is distinct from the moral character concept in Aristotle (aretē) and may be a significant finding for the programme's theological contribution.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

_No phase2 flags on any OWNER term._

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H2005` — 77/223 classified · 12 anchor verse(s)

**Group `5629-001`** (8 verses — anchors: 1Sa 12:3, Isa 6:8)

- **1Sa 12:3** 🔵 (✓) *target: Here*
  > 1Sa 12:3 Here I am; testify against me before the Lord and before his anointed . Whose ox have I taken ? Or whose donkey have I taken ? Or whom have I defrauded ? Whom have I oppressed ? Or from whose hand have I taken a bribe to blind my eyes with it? Testify against me and I will restore it to you .”
- **Isa 6:8** 🔵 (✓) *target: Here*
  > Isa 6:8 And I heard the voice of the Lord saying , “ Whom shall I send , and who will go for us?” Then I said , “ Here I am! Send me .”
- **1Sa 14:43** (✓) *target: Here*
  > 1Sa 14:43 Then Saul said to Jonathan , “ Tell me what you have done .” And Jonathan told him, “I tasted a little honey with the tip of the staff that was in my hand . Here I am; I will die .”
- **2Sa 15:26** (✓) *target: behold*
  > 2Sa 15:26 But if he says , ‘I have no pleasure in you,’ behold , here I am, let him do to me what seems good to him.”
- **Job 31:35** (✓) *target: Here*
  > Job 31:35 Oh , that I had one to hear me! ( Here is my signature ! Let the Almighty answer me!) Oh, that I had the indictment written by my adversary !
- **Isa 52:6** (✓) *target: here*
  > Isa 52:6 Therefore my people shall know my name . Therefore in that day they shall know that it is I who speak ; here I am.”
- **Isa 58:9** (✓) *target: Here*
  > Isa 58:9 Then you shall call , and the Lord will answer ; you shall cry , and he will say , ‘ Here I am.’ If you take away the yoke from your midst , the pointing of the finger , and speaking wickedness ,
- **Isa 65:1** (✓) *target: Here*
  > Isa 65:1 I was ready to be sought by those who did not ask for me; I was ready to be found by those who did not seek me. I said , “ Here I am, here I am,” to a nation that was not called by my name .

**Group `5629-002`** (16 verses — anchors: Ezr 9:15, Psa 51:5)

- **Ezr 9:15** 🔵 (✓) *target: Behold*
  > Ezr 9:15 O Lord , the God of Israel , you are just , for we are left a remnant that has escaped , as it is today . Behold , we are before you in our guilt , for none can stand before you because of this .”
- **Psa 51:5** 🔵 (✓) *target: Behold*
  > Psa 51:5 Behold , I was brought forth in iniquity , and in sin did my mother conceive me.
- **Gen 4:14** (✓) *target: Behold*
  > Gen 4:14 Behold , you have driven me today away from the ground , and from your face I shall be hidden . I shall be a fugitive and a wanderer on the earth , and whoever finds me will kill me .”
- **Gen 15:3** (✓) *target: Behold*
  > Gen 15:3 And Abram said , “ Behold , you have given me no offspring , and a member of my household will be my heir .”
- **Exo 4:1** (✓) *target: behold*
  > Exo 4:1 Then Moses answered , “But behold , they will not believe me or listen to my voice , for they will say , ‘The Lord did not appear to you.’”
- **Exo 6:12** (✓) *target: people*
  > Exo 6:12 But Moses said to the Lord , “Behold, the people of Israel have not listened to me. How then shall Pharaoh listen to me , for I am of uncircumcised lips ?”
- **Exo 6:30** (✓) *target: uncircumcised*
  > Exo 6:30 But Moses said to the Lord , “Behold, I am of uncircumcised lips . How will Pharaoh listen to me?”
- **Lev 10:19** (✓) *target: Behold*
  > Lev 10:19 And Aaron said to Moses , “ Behold , today they have offered their sin offering and their burnt offering before the Lord , and yet such things as these have happened to me! If I had eaten the sin offering today , would the Lord have approved ?”
- **Num 14:40** (✓) *target: Here*
  > Num 14:40 And they rose early in the morning and went up to the heights of the hill country , saying , “ Here we are. We will go up to the place that the Lord has promised , for we have sinned .”
- **Num 17:12** (✓) *target: Behold*
  > Num 17:12 And the people of Israel said to Moses , “ Behold , we perish , we are undone , we are all undone .
- **Jos 9:25** (✓) *target: behold*
  > Jos 9:25 And now , behold , we are in your hand . Whatever seems good and right in your sight to do to us, do it.”
- **2Sa 5:1** (✓) *target: Behold*
  > 2Sa 5:1 Then all the tribes of Israel came to David at Hebron and said , “ Behold , we are your bone and flesh .
- **1Ki 17:12** (✓) *target: now*
  > 1Ki 17:12 And she said , “As the Lord your God lives , I have nothing baked , only a handful of flour in a jar and a little oil in a jug . And now I am gathering a couple of sticks that I may go in and prepare it for myself and my son , that we may eat it and die .”
- **Isa 64:5** (✓) *target: Behold*
  > Isa 64:5 You meet him who joyfully works righteousness , those who remember you in your ways . Behold , you were angry , and we sinned ; in our sins we have been a long time , and shall we be saved ?
- **Isa 64:9** (✓) *target: Behold*
  > Isa 64:9 Be not so terribly angry , O Lord , and remember not iniquity forever . Behold , please look , we are all your people .
- **Jer 3:22** (✓) *target: Behold*
  > Jer 3:22 “ Return , O faithless sons ; I will heal your faithlessness .” “ Behold , we come to you, for you are the Lord our God .

**Group `5629-003`** (6 verses — anchors: Isa 42:1, Isa 49:16)

- **Isa 42:1** 🔵 (✓) *target: Behold*
  > Isa 42:1 Behold my servant , whom I uphold , my chosen , in whom my soul delights ; I have put my Spirit upon him; he will bring forth justice to the nations .
- **Isa 49:16** 🔵 (✓) *target: Behold*
  > Isa 49:16 Behold , I have engraved you on the palms of my hands; your walls are continually before me.
- **Isa 50:9** (✓) *target: Behold*
  > Isa 50:9 Behold , the Lord God helps me; who will declare me guilty ? Behold , all of them will wear out like a garment ; the moth will eat them up .
- **Isa 59:1** (✓) *target: Behold*
  > Isa 59:1 Behold , the Lord’s hand is not shortened , that it cannot save , or his ear dull , that it cannot hear ;
- **Zec 2:10** (✓) *target: behold*
  > Zec 2:10 Sing and rejoice , O daughter of Zion , for behold , I come and I will dwell in your midst , declares the Lord .
- **Mal 3:1** (✓) *target: behold*
  > Mal 3:1 “ Behold , I send my messenger , and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple ; and the messenger of the covenant in whom you delight , behold , he is coming , says the Lord of hosts .

**Group `5629-004`** (15 verses — anchors: Psa 51:6, Isa 58:3)

- **Psa 51:6** 🔵 (✓) *target: Behold*
  > Psa 51:6 Behold , you delight in truth in the inward being , and you teach me wisdom in the secret heart .
- **Isa 58:3** 🔵 (✓) *target: Behold*
  > Isa 58:3 ‘ Why have we fasted , and you see it not ? Why have we humbled ourselves , and you take no knowledge of it?’ Behold , in the day of your fast you seek your own pleasure , and oppress all your workers .
- **Gen 39:8** (✓) *target: Behold*
  > Gen 39:8 But he refused and said to his master’s wife , “ Behold , because of me my master has no concern about anything in the house , and he has put everything that he has in my charge .
- **Gen 44:8** (✓) *target: Behold*
  > Gen 44:8 Behold , the money that we found in the mouths of our sacks we brought back to you from the land of Canaan . How then could we steal silver or gold from your lord’s house ?
- **Gen 44:16** (✓) *target: behold*
  > Gen 44:16 And Judah said , “ What shall we say to my lord ? What shall we speak ? Or how can we clear ourselves ? God has found out the guilt of your servants ; behold , we are my lord’s servants , both we and he also in whose hand the cup has been found .”
- **Deu 31:27** (✓) *target: Behold*
  > Deu 31:27 For I know how rebellious and stubborn you are. Behold , even today while I am yet alive with you, you have been rebellious against the Lord . How much more after my death !
- **Psa 139:4** (✓) *target: behold*
  > Psa 139:4 Even before a word is on my tongue , behold , O Lord , you know it altogether .
- **Pro 24:12** (✓) *target: Behold*
  > Pro 24:12 If you say , “ Behold , we did not know this ,” does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it, and will he not repay man according to his work ?
- **Isa 41:24** (✓) *target: Behold*
  > Isa 41:24 Behold , you are nothing , and your work is less than nothing ; an abomination is he who chooses you .
- **Isa 41:29** (✓) *target: Behold*
  > Isa 41:29 Behold , they are all a delusion ; their works are nothing ; their metal images are empty wind .
- **Isa 50:1** (✓) *target: Behold*
  > Isa 50:1 Thus says the Lord : “ Where is your mother’s certificate of divorce , with which I sent her away ? Or which of my creditors is it to whom I have sold you? Behold , for your iniquities you were sold , and for your transgressions your mother was sent away .
- **Isa 58:4** (✓) *target: Behold*
  > Isa 58:4 Behold , you fast only to quarrel and to fight and to hit with a wicked fist . Fasting like yours this day will not make your voice to be heard on high .
- **Jer 2:35** (✓) *target: Behold*
  > Jer 2:35 you say , ‘I am innocent ; surely his anger has turned from me.’ Behold , I will bring you to judgment for saying , ‘I have not sinned .’
- **Jer 16:12** (✓) *target: behold*
  > Jer 16:12 and because you have done worse than your fathers , for behold , every one of you follows his stubborn , evil will , refusing to listen to me .
- **Zec 3:9** (✓) *target: engrave*
  > Zec 3:9 For behold , on the stone that I have set before Joshua , on a single stone with seven eyes , I will engrave its inscription , declares the Lord of hosts , and I will remove the iniquity of this land in a single day .

**Group `5629-005`** (7 verses — anchors: Job 9:11, Job 40:4)

- **Job 9:11** 🔵 (✓) *target: passes*
  > Job 9:11 Behold, he passes by me, and I see him not; he moves on , but I do not perceive him .
- **Job 40:4** 🔵 (✓) *target: Behold*
  > Job 40:4 “ Behold , I am of small account ; what shall I answer you? I lay my hand on my mouth .
- **Job 9:12** (✓) *target: snatches away*
  > Job 9:12 Behold, he snatches away ; who can turn him back? Who will say to him, ‘What are you doing ?’
- **Job 19:7** (✓) *target: Behold*
  > Job 19:7 Behold , I cry out , ‘ Violence !’ but I am not answered ; I call for help , but there is no justice .
- **Job 23:8** (✓) *target: Behold*
  > Job 23:8 “ Behold , I go forward , but he is not there, and backward , but I do not perceive him ;
- **Job 33:10** (✓) *target: Behold*
  > Job 33:10 Behold , he finds occasions against me, he counts me as his enemy ,
- **Job 41:9** (✓) *target: Behold*
  > Job 41:9 Behold , the hope of a man is false ; he is laid low even at the sight of him.

**Group `5629-006`** (25 verses — anchors: Job 28:28, Song 1:15)

- **Job 28:28** 🔵 (✓) *target: Behold*
  > Job 28:28 And he said to man , ‘ Behold , the fear of the Lord , that is wisdom , and to turn away from evil is understanding .’”
- **Song 1:15** 🔵 (✓) *target: Behold*
  > Song 1:15 Behold , you are beautiful , my love ; behold , you are beautiful ; your eyes are doves .
- **Deu 5:24** (✓) *target: Behold*
  > Deu 5:24 And you said , ‘ Behold , the Lord our God has shown us his glory and greatness , and we have heard his voice out of the midst of the fire . This day we have seen God speak with man , and man still live .
- **1Sa 14:7** (✓) *target: Behold*
  > 1Sa 14:7 And his armor-bearer said to him, “ Do all that is in your heart . Do as you wish . Behold , I am with you heart and soul.”
- **Job 8:20** (✓) *target: Behold*
  > Job 8:20 “ Behold , God will not reject a blameless man, nor take the hand of evildoers .
- **Job 13:1** (✓) *target: seen*
  > Job 13:1 “Behold, my eye has seen all this, my ear has heard and understood it .
- **Job 15:15** (✓) *target: Behold*
  > Job 15:15 Behold , God puts no trust in his holy ones , and the heavens are not pure in his sight ;
- **Job 21:16** (✓) *target: Behold*
  > Job 21:16 Behold , is not their prosperity in their hand ? The counsel of the wicked is far from me .
- **Job 21:27** (✓) *target: Behold*
  > Job 21:27 “ Behold , I know your thoughts and your schemes to wrong me.
- **Job 25:5** (✓) *target: Behold*
  > Job 25:5 Behold , even the moon is not bright , and the stars are not pure in his eyes ;
- **Job 26:14** (✓) *target: Behold*
  > Job 26:14 Behold , these are but the outskirts of his ways , and how small a whisper do we hear of him! But the thunder of his power who can understand ?”
- **Job 27:12** (✓) *target: Behold*
  > Job 27:12 Behold , all of you have seen it yourselves; why then have you become altogether vain ?
- **Job 32:11** (✓) *target: Behold*
  > Job 32:11 “ Behold , I waited for your words , I listened for your wise sayings , while you searched out what to say.
- **Job 33:6** (✓) *target: Behold*
  > Job 33:6 Behold , I am toward God as you are; I too was pinched off from a piece of clay .
- **Job 36:26** (✓) *target: Behold*
  > Job 36:26 Behold , God is great , and we know him not ; the number of his years is unsearchable .
- **Song 1:16** (✓) *target: Behold*
  > Song 1:16 Behold , you are beautiful , my beloved , truly delightful. Our couch is green ;
- **Song 4:1** (✓) *target: Behold*
  > Song 4:1 Behold , you are beautiful , my love , behold , you are beautiful ! Your eyes are doves behind your veil . Your hair is like a flock of goats leaping down the slopes of Gilead .
- **Isa 28:16** (✓) *target: Behold*
  > Isa 28:16 therefore thus says the Lord God , “ Behold , I am the one who has laid as a foundation in Zion , a stone , a tested stone , a precious cornerstone , of a sure foundation : ‘Whoever believes will not be in haste .’
- **Isa 29:14** (✓) *target: behold*
  > Isa 29:14 therefore , behold , I will again do wonderful things with this people , with wonder upon wonder ; and the wisdom of their wise men shall perish , and the discernment of their discerning men shall be hidden .”
- **Isa 32:1** (✓) *target: Behold*
  > Isa 32:1 Behold , a king will reign in righteousness , and princes will rule in justice .
- **Isa 33:7** (✓) *target: Behold*
  > Isa 33:7 Behold , their heroes cry in the streets ; the envoys of peace weep bitterly .
- **Isa 49:21** (✓) *target: Behold*
  > Isa 49:21 Then you will say in your heart : ‘ Who has borne me these ? I was bereaved and barren , exiled and put away , but who has brought up these ? Behold , I was left alone ; from where have these come?’”
- **Isa 56:3** (✓) *target: Behold*
  > Isa 56:3 Let not the foreigner who has joined himself to the Lord say , “The Lord will surely separate me from his people ”; and let not the eunuch say , “ Behold , I am a dry tree .”
- **Isa 65:18** (✓) *target: behold*
  > Isa 65:18 But be glad and rejoice forever in that which I create ; for behold , I create Jerusalem to be a joy , and her people to be a gladness .
- **Zep 3:19** (✓) *target: Behold*
  > Zep 3:19 Behold , at that time I will deal with all your oppressors . And I will save the lame and gather the outcast , and I will change their shame into praise and renown in all the earth .

**Group `UNCLASSIFIED`** (146 verses)

- **Gen 3:22** (—) *target: Behold*
  > Gen 3:22 Then the Lord God said , “ Behold , the man has become like one of us in knowing good and evil . Now , lest he reach out his hand and take also of the tree of life and eat , and live forever —”
- **Gen 6:13** (—) *target: Behold*
  > Gen 6:13 And God said to Noah , “I have determined to make an end of all flesh , for the earth is filled with violence through them . Behold , I will destroy them with the earth .
- **Gen 9:9** (—) *target: Behold*
  > Gen 9:9 “ Behold , I establish my covenant with you and your offspring after you ,
- **Gen 11:6** (—) *target: people*
  > Gen 11:6 And the Lord said , “Behold, they are one people , and they have all one language , and this is only the beginning of what they will do . And nothing that they propose to do will now be impossible for them.
- **Gen 19:34** (—) *target: Behold*
  > Gen 19:34 The next day , the firstborn said to the younger , “ Behold , I lay last night with my father . Let us make him drink wine tonight also . Then you go in and lie with him, that we may preserve offspring from our father .”
- **Gen 27:11** (—) *target: Behold*
  > Gen 27:11 But Jacob said to Rebekah his mother , “ Behold , my brother Esau is a hairy man , and I am a smooth man .
- **Gen 27:37** (—) *target: Behold*
  > Gen 27:37 Isaac answered and said to Esau , “ Behold , I have made him lord over you, and all his brothers I have given to him for servants , and with grain and wine I have sustained him. What then can I do for you , my son ?”
- **Gen 29:7** (—) *target: Behold*
  > Gen 29:7 He said , “ Behold , it is still high day ; it is not time for the livestock to be gathered together . Water the sheep and go , pasture them.”
- **Gen 30:34** (—) *target: Good*
  > Gen 30:34 Laban said , “ Good ! Let it be as you have said .”
- **Gen 40:6** (—) *target: troubled*
  > Gen 40:6 When Joseph came to them in the morning , he saw that they were troubled .
- **Gen 41:17** (—) *target: Behold*
  > Gen 41:17 Then Pharaoh said to Joseph , “ Behold , in my dream I was standing on the banks of the Nile .
- **Gen 47:1** (—) *target: now*
  > Gen 47:1 So Joseph went in and told Pharaoh , “My father and my brothers , with their flocks and herds and all that they possess, have come from the land of Canaan . They are now in the land of Goshen .”
- **Gen 47:23** (—) *target: Behold*
  > Gen 47:23 Then Joseph said to the people , “ Behold , I have this day bought you and your land for Pharaoh . Now here is seed for you, and you shall sow the land .
- **Gen 48:4** (—) *target: Behold*
  > Gen 48:4 and said to me, ‘ Behold , I will make you fruitful and multiply you, and I will make of you a company of peoples and will give this land to your offspring after you for an everlasting possession .’
- **Exo 5:5** (—) *target: Behold*
  > Exo 5:5 And Pharaoh said , “ Behold , the people of the land are now many , and you make them rest from their burdens !”
- **Exo 8:21** (—) *target: send*
  > Exo 8:21 Or else, if you will not let my people go , behold, I will send swarms of flies on you and your servants and your people , and into your houses . And the houses of the Egyptians shall be filled with swarms of flies , and also the ground on which they stand.
- **Exo 8:26** (—) *target: If*
  > Exo 8:26 But Moses said , “It would not be right to do so , for the offerings we shall sacrifice to the Lord our God are an abomination to the Egyptians . If we sacrifice offerings abominable to the Egyptians before their eyes , will they not stone us ?
- **Exo 9:18** (—) *target: Behold*
  > Exo 9:18 Behold , about this time tomorrow I will cause very heavy hail to fall , such as never has been in Egypt from the day it was founded until now .
- **Exo 10:4** (—) *target: behold*
  > Exo 10:4 For if you refuse to let my people go , behold , tomorrow I will bring locusts into your country ,
- **Exo 14:17** (—) *target: harden*
  > Exo 14:17 And I will harden the hearts of the Egyptians so that they shall go in after them, and I will get glory over Pharaoh and all his host , his chariots , and his horsemen .
- **Exo 16:4** (—) *target: Behold*
  > Exo 16:4 Then the Lord said to Moses , “ Behold , I am about to rain bread from heaven for you, and the people shall go out and gather a day’s portion every day , that I may test them, whether they will walk in my law or not .
- **Exo 17:6** (—) *target: Behold*
  > Exo 17:6 Behold , I will stand before you there on the rock at Horeb , and you shall strike the rock , and water shall come out of it, and the people will drink .” And Moses did so , in the sight of the elders of Israel .
- **Exo 34:11** (—) *target: Behold*
  > Exo 34:11 “ Observe what I command you this day . Behold , I will drive out before you the Amorites , the Canaanites , the Hittites , the Perizzites , the Hivites , and the Jebusites .
- **Lev 10:18** (—) *target: Behold*
  > Lev 10:18 Behold , its blood was not brought into the inner part of the sanctuary . You certainly ought to have eaten it in the sanctuary , as I commanded .”
- **Lev 25:20** (—) *target: sow*
  > Lev 25:20 And if you say , ‘What shall we eat in the seventh year , if we may not sow or gather in our crop ?’
- **Num 23:9** (—) *target: behold*
  > Num 23:9 For from the top of the crags I see him, from the hills I behold him; behold , a people dwelling alone , and not counting itself among the nations !
- **Num 23:24** (—) *target: Behold*
  > Num 23:24 Behold , a people ! As a lioness it rises up and as a lion it lifts itself; it does not lie down until it has devoured the prey and drunk the blood of the slain .”
- **Num 24:14** (—) *target: behold*
  > Num 24:14 And now , behold , I am going to my people . Come , I will let you know what this people will do to your people in the latter days .”
- **Num 25:12** (—) *target: Behold*
  > Num 25:12 Therefore say , ‘ Behold , I give to him my covenant of peace ,
- **Num 31:16** (—) *target: Behold*
  > Num 31:16 Behold , these , on Balaam’s advice , caused the people of Israel to act treacherously against the Lord in the incident of Peor , and so the plague came among the congregation of the Lord .
- **Deu 10:14** (—) *target: Behold*
  > Deu 10:14 Behold , to the Lord your God belong heaven and the heaven of heavens , the earth with all that is in it .
- **Deu 31:14** (—) *target: Behold*
  > Deu 31:14 And the Lord said to Moses , “ Behold , the days approach when you must die . Call Joshua and present yourselves in the tent of meeting , that I may commission him.” And Moses and Joshua went and presented themselves in the tent of meeting .
- **1Sa 3:4** (—) *target: Here*
  > 1Sa 3:4 Then the Lord called Samuel , and he said , “ Here I am!”
- **1Sa 3:5** (—) *target: Here*
  > 1Sa 3:5 and ran to Eli and said , “ Here I am, for you called me.” But he said , “I did not call ; lie down again .” So he went and lay down .
- **1Sa 3:6** (—) *target: Here*
  > 1Sa 3:6 And the Lord called again , “ Samuel !” and Samuel arose and went to Eli and said , “ Here I am, for you called me.” But he said , “I did not call , my son ; lie down again .”
- **1Sa 3:8** (—) *target: Here*
  > 1Sa 3:8 And the Lord called Samuel again the third time . And he arose and went to Eli and said , “ Here I am, for you called me.” Then Eli perceived that the Lord was calling the boy .
- **1Sa 3:16** (—) *target: Here*
  > 1Sa 3:16 But Eli called Samuel and said , “ Samuel , my son .” And he said , “ Here I am.”
- **1Sa 22:12** (—) *target: Here*
  > 1Sa 22:12 And Saul said , “ Hear now , son of Ahitub .” And he answered , “ Here I am, my lord .”
- **1Sa 25:19** (—) *target: behold*
  > 1Sa 25:19 And she said to her young men , “ Go on before me; behold , I come after you.” But she did not tell her husband Nabal .
- **2Sa 1:7** (—) *target: Here*
  > 2Sa 1:7 And when he looked behind him, he saw me, and called to me. And I answered , ‘ Here I am.’
- **2Sa 12:11** (—) *target: Behold*
  > 2Sa 12:11 Thus says the Lord , ‘ Behold , I will raise up evil against you out of your own house . And I will take your wives before your eyes and give them to your neighbor , and he shall lie with your wives in the sight of this sun .
- **2Sa 16:8** (—) *target: See*
  > 2Sa 16:8 The Lord has avenged on you all the blood of the house of Saul , in whose place you have reigned , and the Lord has given the kingdom into the hand of your son Absalom . See , your evil is on you, for you are a man of blood .”
- **1Ki 5:5** (—) *target: intend*
  > 1Ki 5:5 And so I intend to build a house for the name of the Lord my God , as the Lord said to David my father , ‘Your son , whom I will set on your throne in your place , shall build the house for my name .’
- **1Ki 11:22** (—) *target: you*
  > 1Ki 11:22 But Pharaoh said to him, “ What have you lacked with me that you are now seeking to go to your own country ?” And he said to him, “ Only let me depart .”
- **1Ki 11:31** (—) *target: Behold*
  > 1Ki 11:31 And he said to Jeroboam , “ Take for yourself ten pieces , for thus says the Lord , the God of Israel , ‘ Behold , I am about to tear the kingdom from the hand of Solomon and will give you ten tribes
- **1Ki 14:10** (—) *target: behold*
  > 1Ki 14:10 therefore behold , I will bring harm upon the house of Jeroboam and will cut off from Jeroboam every male , both bond and free in Israel , and will burn up the house of Jeroboam , as a man burns up dung until it is all gone .
- **1Ki 16:3** (—) *target: behold*
  > 1Ki 16:3 behold , I will utterly sweep away Baasha and his house , and I will make your house like the house of Jeroboam the son of Nebat .
- **1Ki 20:13** (—) *target: Behold*
  > 1Ki 20:13 And behold , a prophet came near to Ahab king of Israel and said , “ Thus says the Lord , Have you seen all this great multitude ? Behold , I will give it into your hand this day , and you shall know that I am the Lord .”
- **1Ki 20:36** (—) *target: behold*
  > 1Ki 20:36 Then he said to him, “ Because you have not obeyed the voice of the Lord , behold , as soon as you have gone from me, a lion shall strike you down .” And as soon as he had departed from him , a lion met him and struck him down.
- **1Ki 21:21** (—) *target: Behold*
  > 1Ki 21:21 Behold , I will bring disaster upon you. I will utterly burn you up , and will cut off from Ahab every male , bond or free , in Israel .
- **1Ki 22:25** (—) *target: Behold*
  > 1Ki 22:25 And Micaiah said , “ Behold , you shall see on that day when you go into an inner chamber to hide yourself.”
- **2Ki 7:2** (—) *target: see*
  > 2Ki 7:2 Then the captain on whose hand the king leaned said to the man of God , “ If the Lord himself should make windows in heaven , could this thing be?” But he said , “ You shall see it with your own eyes , but you shall not eat of it .”
- **2Ki 7:13** (—) *target: already perished*
  > 2Ki 7:13 And one of his servants said , “Let some men take five of the remaining horses , seeing that those who are left here will fare like the whole multitude of Israel who have already perished . Let us send and see .”
- **2Ki 7:19** (—) *target: see*
  > 2Ki 7:19 the captain had answered the man of God , “ If the Lord himself should make windows in heaven , could such a thing be?” And he had said , “ You shall see it with your own eyes , but you shall not eat of it .”
- **2Ki 19:7** (—) *target: put*
  > 2Ki 19:7 Behold, I will put a spirit in him, so that he shall hear a rumor and return to his own land , and I will make him fall by the sword in his own land .’”
- **2Ki 20:5** (—) *target: Behold*
  > 2Ki 20:5 “Turn back , and say to Hezekiah the leader of my people , Thus says the Lord , the God of David your father : I have heard your prayer ; I have seen your tears . Behold , I will heal you. On the third day you shall go up to the house of the Lord ,
- **2Ki 21:12** (—) *target: Behold*
  > 2Ki 21:12 therefore thus says the Lord , the God of Israel : Behold , I am bringing upon Jerusalem and Judah such disaster that the ears of everyone who hears of it will tingle .
- **2Ki 22:16** (—) *target: Behold*
  > 2Ki 22:16 Thus says the Lord , Behold , I will bring disaster upon this place and upon its inhabitants , all the words of the book that the king of Judah has read .
- **2Ki 22:20** (—) *target: behold*
  > 2Ki 22:20 Therefore , behold , I will gather you to your fathers , and you shall be gathered to your grave in peace , and your eyes shall not see all the disaster that I will bring upon this place .’” And they brought back word to the king .
- **1Ch 11:25** (—) *target: He*
  > 1Ch 11:25 He was renowned among the thirty , but he did not attain to the three . And David set him over his bodyguard .
- **2Ch 7:13** (—) *target: When*
  > 2Ch 7:13 When I shut up the heavens so that there is no rain , or command the locust to devour the land , or send pestilence among my people ,
- **2Ch 16:11** (—) *target: written*
  > 2Ch 16:11 The acts of Asa , from first to last , are written in the Book of the Kings of Judah and Israel .
- **2Ch 18:24** (—) *target: Behold*
  > 2Ch 18:24 And Micaiah said , “ Behold , you shall see on that day when you go into an inner chamber to hide yourself.”
- **2Ch 20:16** (—) *target: Behold*
  > 2Ch 20:16 Tomorrow go down against them. Behold , they will come up by the ascent of Ziz . You will find them at the end of the valley , east of the wilderness of Jeruel .
- **2Ch 20:24** (—) *target: behold*
  > 2Ch 20:24 When Judah came to the watchtower of the wilderness , they looked toward the horde , and behold , there were dead bodies lying on the ground ; none had escaped .
- **2Ch 20:34** (—) *target: written*
  > 2Ch 20:34 Now the rest of the acts of Jehoshaphat , from first to last , are written in the chronicles of Jehu the son of Hanani , which are recorded in the Book of the Kings of Israel .
- **2Ch 24:27** (—) *target: written*
  > 2Ch 24:27 Accounts of his sons and of the many oracles against him and of the rebuilding of the house of God are written in the Story of the Book of the Kings . And Amaziah his son reigned in his place .
- **2Ch 25:26** (—) *target: written*
  > 2Ch 25:26 Now the rest of the deeds of Amaziah , from first to last , are they not written in the Book of the Kings of Judah and Israel ?
- **2Ch 27:7** (—) *target: behold*
  > 2Ch 27:7 Now the rest of the acts of Jotham , and all his wars and his ways , behold , they are written in the Book of the Kings of Israel and Judah .
- **2Ch 28:26** (—) *target: behold*
  > 2Ch 28:26 Now the rest of his acts and all his ways , from first to last , behold , they are written in the Book of the Kings of Judah and Israel .
- **2Ch 29:19** (—) *target: behold*
  > 2Ch 29:19 All the utensils that King Ahaz discarded in his reign when he was faithless , we have made ready and consecrated , and behold , they are before the altar of the Lord .”
- **2Ch 32:32** (—) *target: behold*
  > 2Ch 32:32 Now the rest of the acts of Hezekiah and his good deeds , behold , they are written in the vision of Isaiah the prophet , the son of Amoz , in the Book of the Kings of Judah and Israel .
- **2Ch 33:18** (—) *target: behold*
  > 2Ch 33:18 Now the rest of the acts of Manasseh , and his prayer to his God , and the words of the seers who spoke to him in the name of the Lord , the God of Israel , behold , they are in the Chronicles of the Kings of Israel .
- **2Ch 33:19** (—) *target: behold*
  > 2Ch 33:19 And his prayer , and how God was moved by his entreaty , and all his sin and his faithlessness , and the sites on which he built high places and set up the Asherim and the images , before he humbled himself, behold , they are written in the Chronicles of the Seers .
- **2Ch 34:24** (—) *target: Behold*
  > 2Ch 34:24 Thus says the Lord , Behold , I will bring disaster upon this place and upon its inhabitants , all the curses that are written in the book that was read before the king of Judah .
- **2Ch 34:28** (—) *target: Behold*
  > 2Ch 34:28 Behold , I will gather you to your fathers , and you shall be gathered to your grave in peace , and your eyes shall not see all the disaster that I will bring upon this place and its inhabitants .’” And they brought back word to the king .
- **2Ch 35:25** (—) *target: behold*
  > 2Ch 35:25 Jeremiah also uttered a lament for Josiah ; and all the singing men and singing women have spoken of Josiah in their laments to this day . They made these a rule in Israel ; behold , they are written in the Laments .
- **2Ch 35:27** (—) *target: behold*
  > 2Ch 35:27 and his acts , first and last , behold , they are written in the Book of the Kings of Israel and Judah .
- **2Ch 36:8** (—) *target: behold*
  > 2Ch 36:8 Now the rest of the acts of Jehoiakim , and the abominations that he did , and what was found against him, behold , they are written in the Book of the Kings of Israel and Judah . And Jehoiachin his son reigned in his place .
- **Job 2:6** (—) *target: Behold*
  > Job 2:6 And the Lord said to Satan , “ Behold , he is in your hand ; only spare his life .”
- **Job 4:18** (—) *target: Even*
  > Job 4:18 Even in his servants he puts no trust , and his angels he charges with error ;
- **Job 8:19** (—) *target: Behold*
  > Job 8:19 Behold , this is the joy of his way , and out of the soil others will spring .
- **Job 12:14** (—) *target: tears down*
  > Job 12:14 If he tears down , none can rebuild; if he shuts a man in, none can open .
- **Job 12:15** (—) *target: withholds*
  > Job 12:15 If he withholds the waters , they dry up ; if he sends them out , they overwhelm the land .
- **Job 13:15** (—) *target: Though*
  > Job 13:15 Though he slay me, I will hope in him; yet I will argue my ways to his face .
- **Job 24:5** (—) *target: Behold*
  > Job 24:5 Behold , like wild donkeys in the desert the poor go out to their toil , seeking game ; the wasteland yields food for their children .
- **Job 33:12** (—) *target: Behold*
  > Job 33:12 “ Behold , in this you are not right . I will answer you, for God is greater than man .
- **Job 33:29** (—) *target: Behold*
  > Job 33:29 “ Behold , God does all these things , twice , three times, with a man ,
- **Job 36:5** (—) *target: Behold*
  > Job 36:5 “ Behold , God is mighty , and does not despise any; he is mighty in strength of understanding .
- **Job 36:22** (—) *target: Behold*
  > Job 36:22 Behold , God is exalted in his power ; who is a teacher like him?
- **Job 36:30** (—) *target: Behold*
  > Job 36:30 Behold , he scatters his lightning about him and covers the roots of the sea .
- **Job 38:35** (—) *target: are*
  > Job 38:35 Can you send forth lightnings , that they may go and say to you, ‘Here we are ’?
- **Job 40:23** (—) *target: Behold*
  > Job 40:23 Behold , if the river is turbulent he is not frightened ; he is confident though Jordan rushes against his mouth .
- **Psa 68:33** (—) *target: behold*
  > Psa 68:33 to him who rides in the heavens , the ancient heavens ; behold , he sends out his voice , his mighty voice .
- **Psa 78:20** (—) *target: He*
  > Psa 78:20 He struck the rock so that water gushed out and streams overflowed . Can he also give bread or provide meat for his people ?”
- **Psa 139:8** (—) *target: there*
  > Psa 139:8 If I ascend to heaven , you are there ! If I make my bed in Sheol , you are there !
- **Pro 11:31** (—) *target: If*
  > Pro 11:31 If the righteous is repaid on earth , how much more the wicked and the sinner !
- **Isa 13:17** (—) *target: Behold*
  > Isa 13:17 Behold , I am stirring up the Medes against them, who have no regard for silver and do not delight in gold .
- **Isa 23:13** (—) *target: Behold*
  > Isa 23:13 Behold the land of the Chaldeans ! This is the people that was not ; Assyria destined it for wild beasts . They erected their siege towers , they stripped her palaces bare, they made her a ruin .
- **Isa 37:7** (—) *target: Behold*
  > Isa 37:7 Behold , I will put a spirit in him, so that he shall hear a rumor and return to his own land , and I will make him fall by the sword in his own land .’”
- **Isa 38:5** (—) *target: Behold*
  > Isa 38:5 “ Go and say to Hezekiah , Thus says the Lord , the God of David your father : I have heard your prayer ; I have seen your tears . Behold , I will add fifteen years to your life .
- **Isa 38:8** (—) *target: Behold*
  > Isa 38:8 Behold , I will make the shadow cast by the declining sun on the dial of Ahaz turn back ten steps .” So the sun turned back on the dial the ten steps by which it had declined .
- **Isa 40:15** (—) *target: Behold*
  > Isa 40:15 Behold , the nations are like a drop from a bucket , and are accounted as the dust on the scales ; behold , he takes up the coastlands like fine dust .
- **Isa 41:11** (—) *target: Behold*
  > Isa 41:11 Behold , all who are incensed against you shall be put to shame and confounded ; those who strive against you shall be as nothing and shall perish .
- **Isa 41:27** (—) *target: are*
  > Isa 41:27 I was the first to say to Zion , “ Behold , here they are !” and I give to Jerusalem a herald of good news .
- **Isa 43:19** (—) *target: Behold*
  > Isa 43:19 Behold , I am doing a new thing ; now it springs forth , do you not perceive it? I will make a way in the wilderness and rivers in the desert .
- **Isa 44:11** (—) *target: Behold*
  > Isa 44:11 Behold , all his companions shall be put to shame , and the craftsmen are only human . Let them all assemble , let them stand forth . They shall be terrified ; they shall be put to shame together .
- **Isa 50:2** (—) *target: Behold*
  > Isa 50:2 Why , when I came , was there no man ; why, when I called , was there no one to answer ? Is my hand shortened , that it cannot redeem ? Or have I no power to deliver ? Behold , by my rebuke I dry up the sea , I make the rivers a desert ; their fish stink for lack of water and die of thirst .
- **Isa 50:11** (—) *target: Behold*
  > Isa 50:11 Behold , all you who kindle a fire , who equip yourselves with burning torches ! Walk by the light of your fire , and by the torches that you have kindled ! This you have from my hand : you shall lie down in torment .
- **Isa 54:15** (—) *target: If*
  > Isa 54:15 If anyone stirs up strife , it is not from me; whoever stirs up strife with you shall fall because of you.
- **Isa 55:4** (—) *target: Behold*
  > Isa 55:4 Behold , I made him a witness to the peoples , a leader and commander for the peoples .
- **Isa 55:5** (—) *target: Behold*
  > Isa 55:5 Behold , you shall call a nation that you do not know , and a nation that did not know you shall run to you, because of the Lord your God , and of the Holy One of Israel , for he has glorified you .
- **Isa 65:17** (—) *target: behold*
  > Isa 65:17 “ For behold , I create new heavens and a new earth , and the former things shall not be remembered or come into mind .
- **Isa 66:12** (—) *target: Behold*
  > Isa 66:12 For thus says the Lord : “ Behold , I will extend peace to her like a river , and the glory of the nations like an overflowing stream ; and you shall nurse , you shall be carried upon her hip , and bounced upon her knees .
- **Jer 1:15** (—) *target: behold*
  > Jer 1:15 For behold , I am calling all the tribes of the kingdoms of the north , declares the Lord , and they shall come , and every one shall set his throne at the entrance of the gates of Jerusalem , against all its walls all around and against all the cities of Judah .
- **Jer 2:10** (—) *target: if*
  > Jer 2:10 For cross to the coasts of Cyprus and see , or send to Kedar and examine with care ; see if there has been such a thing .
- **Jer 3:1** (—) *target: If*
  > Jer 3:1 “ If a man divorces his wife and she goes from him and becomes another man’s wife, will he return to her? Would not that land be greatly polluted ? You have played the whore with many lovers ; and would you return to me? declares the Lord .
- **Jer 5:14** (—) *target: behold*
  > Jer 5:14 Therefore thus says the Lord , the God of hosts : “Because you have spoken this word , behold , I am making my words in your mouth a fire , and this people wood , and the fire shall consume them .
- **Jer 5:15** (—) *target: Behold*
  > Jer 5:15 Behold , I am bringing against you a nation from afar , O house of Israel , declares the Lord . It is an enduring nation ; it is an ancient nation , a nation whose language you do not know , nor can you understand what they say .
- **Jer 6:21** (—) *target: Behold*
  > Jer 6:21 Therefore thus says the Lord : ‘ Behold , I will lay before this people stumbling blocks against which they shall stumble ; fathers and sons together , neighbor and friend shall perish .’”
- **Jer 8:17** (—) *target: behold*
  > Jer 8:17 For behold , I am sending among you serpents , adders that cannot be charmed , and they shall bite you,” declares the Lord .
- **Jer 9:7** (—) *target: Behold*
  > Jer 9:7 Therefore thus says the Lord of hosts : “ Behold , I will refine them and test them, for what else can I do , because of my people ?
- **Jer 9:15** (—) *target: Behold*
  > Jer 9:15 Therefore thus says the Lord of hosts , the God of Israel : Behold , I will feed this people with bitter food , and give them poisonous water to drink .
- **Jer 10:18** (—) *target: Behold*
  > Jer 10:18 For thus says the Lord : “ Behold , I am slinging out the inhabitants of the land at this time , and I will bring distress on them, that they may feel it.”
- **Jer 11:11** (—) *target: Behold*
  > Jer 11:11 Therefore , thus says the Lord , Behold , I am bringing disaster upon them that they cannot escape . Though they cry to me, I will not listen to them .
- **Jer 11:22** (—) *target: Behold*
  > Jer 11:22 therefore thus says the Lord of hosts : “ Behold , I will punish them . The young men shall die by the sword , their sons and their daughters shall die by famine ,
- **Jer 12:14** (—) *target: Behold*
  > Jer 12:14 Thus says the Lord concerning all my evil neighbors who touch the heritage that I have given my people Israel to inherit : “ Behold , I will pluck them up from their land , and I will pluck up the house of Judah from among them.
- **Jer 13:13** (—) *target: Behold*
  > Jer 13:13 Then you shall say to them, ‘ Thus says the Lord : Behold , I will fill with drunkenness all the inhabitants of this land : the kings who sit on David’s throne , the priests , the prophets , and all the inhabitants of Jerusalem .
- **Jer 16:9** (—) *target: Behold*
  > Jer 16:9 For thus says the Lord of hosts , the God of Israel : Behold , I will silence in this place , before your eyes and in your days , the voice of mirth and the voice of gladness , the voice of the bridegroom and the voice of the bride .
- **Jer 16:16** (—) *target: Behold*
  > Jer 16:16 “ Behold , I am sending for many fishers , declares the Lord , and they shall catch them. And afterward I will send for many hunters , and they shall hunt them from every mountain and every hill , and out of the clefts of the rocks .
- **Jer 16:21** (—) *target: behold*
  > Jer 16:21 “ Therefore , behold , I will make them know , this once I will make them know my power and my might , and they shall know that my name is the Lord .”
- **Jer 19:3** (—) *target: Behold*
  > Jer 19:3 You shall say , ‘ Hear the word of the Lord , O kings of Judah and inhabitants of Jerusalem . Thus says the Lord of hosts , the God of Israel : Behold , I am bringing such disaster upon this place that the ears of everyone who hears of it will tingle .
- **Hos 2:6** (—) *target: hedge*
  > Hos 2:6 Therefore I will hedge up her way with thorns , and I will build a wall against her, so that she cannot find her paths .
- **Joe 2:19** (—) *target: Behold*
  > Joe 2:19 The Lord answered and said to his people , “ Behold , I am sending to you grain , wine , and oil , and you will be satisfied ; and I will no more make you a reproach among the nations .
- **Joe 3:7** (—) *target: Behold*
  > Joe 3:7 Behold , I will stir them up from the place to which you have sold them, and I will return your payment on your own head .
- **Amo 6:14** (—) *target: behold*
  > Amo 6:14 “ For behold , I will raise up against you a nation , O house of Israel ,” declares the Lord , the God of hosts ; “and they shall oppress you from Lebo-hamath to the Brook of the Arabah .”
- **Amo 7:8** (—) *target: Behold*
  > Amo 7:8 And the Lord said to me, “ Amos , what do you see ?” And I said , “A plumb line .” Then the Lord said , “ Behold , I am setting a plumb line in the midst of my people Israel ; I will never again pass by them ;
- **Mic 2:3** (—) *target: behold*
  > Mic 2:3 Therefore thus says the Lord : behold , against this family I am devising disaster , from which you cannot remove your necks , and you shall not walk haughtily , for it will be a time of disaster .
- **Nah 2:13** (—) *target: Behold*
  > Nah 2:13 Behold , I am against you, declares the Lord of hosts , and I will burn your chariots in smoke , and the sword shall devour your young lions . I will cut off your prey from the earth , and the voice of your messengers shall no longer be heard .
- **Nah 3:5** (—) *target: Behold*
  > Nah 3:5 Behold , I am against you, declares the Lord of hosts , and will lift up your skirts over your face ; and I will make nations look at your nakedness and kingdoms at your shame .
- **Hab 1:6** (—) *target: behold*
  > Hab 1:6 For behold , I am raising up the Chaldeans , that bitter and hasty nation , who march through the breadth of the earth , to seize dwellings not their own.
- **Hag 2:12** (—) *target: If*
  > Hag 2:12 ‘ If someone carries holy meat in the fold of his garment and touches with his fold bread or stew or wine or oil or any kind of food , does it become holy ?’” The priests answered and said , “ No .”
- **Zec 2:9** (—) *target: Behold*
  > Zec 2:9 “ Behold , I will shake my hand over them, and they shall become plunder for those who served them. Then you will know that the Lord of hosts has sent me .
- **Zec 3:8** (—) *target: behold*
  > Zec 3:8 Hear now , O Joshua the high priest , you and your friends who sit before you, for they are men who are a sign : behold , I will bring my servant the Branch .
- **Zec 8:7** (—) *target: Behold*
  > Zec 8:7 Thus says the Lord of hosts : Behold , I will save my people from the east country and from the west country ,
- **Mal 2:3** (—) *target: Behold*
  > Mal 2:3 Behold , I will rebuke your offspring , and spread dung on your faces , the dung of your offerings , and you shall be taken away with it.

### `H2006A` — 0/11 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (11 verses)

- **Ezr 4:13** (—) *target: if*
  > Ezr 4:13 Now be it known to the king that if this city is rebuilt and the walls finished , they will not pay tribute , custom , or toll , and the royal revenue will be impaired .
- **Ezr 4:16** (—) *target: if*
  > Ezr 4:16 We make known to the king that if this city is rebuilt and its walls finished , you will then have no possession in the province Beyond the River .”
- **Ezr 5:17** (—) *target: if*
  > Ezr 5:17 Therefore , if it seems good to the king , let search be made in the royal archives there in Babylon , to see whether a decree was issued by Cyrus the king for the rebuilding of this house of God in Jerusalem . And let the king send us his pleasure in this matter .”
- **Ezr 7:26** (—) *target: whether*
  > Ezr 7:26 Whoever will not obey the law of your God and the law of the king , let judgment be strictly executed on him , whether for death or for banishment or for confiscation of his goods or for imprisonment .”
- **Dan 2:5** (—) *target: if*
  > Dan 2:5 The king answered and said to the Chaldeans , “The word from me is firm : if you do not make known to me the dream and its interpretation , you shall be torn limb from limb , and your houses shall be laid in ruins .
- **Dan 2:6** (—) *target: if*
  > Dan 2:6 But if you show the dream and its interpretation , you shall receive from me gifts and rewards and great honor . Therefore show me the dream and its interpretation .”
- **Dan 2:9** (—) *target: if*
  > Dan 2:9 if you do not make the dream known to me, there is but one sentence for you. You have agreed to speak lying and corrupt words before me till the times change . Therefore tell me the dream , and I shall know that you can show me its interpretation .”
- **Dan 3:15** (—) *target: if*
  > Dan 3:15 Now if you are ready when you hear the sound of the horn , pipe , lyre , trigon , harp , bagpipe , and every kind of music , to fall down and worship the image that I have made , well and good. But if you do not worship , you shall immediately be cast into a burning fiery furnace . And who is the god who will deliver you out of my hands ?”
- **Dan 3:17** (—) *target: If*
  > Dan 3:17 If this be so, our God whom we serve is able to deliver us from the burning fiery furnace , and he will deliver us out of your hand , O king .
- **Dan 3:18** (—) *target: if*
  > Dan 3:18 But if not , be it known to you, O king , that we will not serve your gods or worship the golden image that you have set up .”
- **Dan 5:16** (—) *target: if*
  > Dan 5:16 But I have heard that you can give interpretations and solve problems . Now if you can read the writing and make known to me its interpretation , you shall be clothed with purple and have a chain of gold around your neck and shall be the third ruler in the kingdom .”

### `H2006B` — 0/11 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (11 verses)

- **Ezr 4:13** (—) *target: if*
  > Ezr 4:13 Now be it known to the king that if this city is rebuilt and the walls finished , they will not pay tribute , custom , or toll , and the royal revenue will be impaired .
- **Ezr 4:16** (—) *target: if*
  > Ezr 4:16 We make known to the king that if this city is rebuilt and its walls finished , you will then have no possession in the province Beyond the River .”
- **Ezr 5:17** (—) *target: if*
  > Ezr 5:17 Therefore , if it seems good to the king , let search be made in the royal archives there in Babylon , to see whether a decree was issued by Cyrus the king for the rebuilding of this house of God in Jerusalem . And let the king send us his pleasure in this matter .”
- **Ezr 7:26** (—) *target: whether*
  > Ezr 7:26 Whoever will not obey the law of your God and the law of the king , let judgment be strictly executed on him , whether for death or for banishment or for confiscation of his goods or for imprisonment .”
- **Dan 2:5** (—) *target: if*
  > Dan 2:5 The king answered and said to the Chaldeans , “The word from me is firm : if you do not make known to me the dream and its interpretation , you shall be torn limb from limb , and your houses shall be laid in ruins .
- **Dan 2:6** (—) *target: if*
  > Dan 2:6 But if you show the dream and its interpretation , you shall receive from me gifts and rewards and great honor . Therefore show me the dream and its interpretation .”
- **Dan 2:9** (—) *target: if*
  > Dan 2:9 if you do not make the dream known to me, there is but one sentence for you. You have agreed to speak lying and corrupt words before me till the times change . Therefore tell me the dream , and I shall know that you can show me its interpretation .”
- **Dan 3:15** (—) *target: if*
  > Dan 3:15 Now if you are ready when you hear the sound of the horn , pipe , lyre , trigon , harp , bagpipe , and every kind of music , to fall down and worship the image that I have made , well and good. But if you do not worship , you shall immediately be cast into a burning fiery furnace . And who is the god who will deliver you out of my hands ?”
- **Dan 3:17** (—) *target: If*
  > Dan 3:17 If this be so, our God whom we serve is able to deliver us from the burning fiery furnace , and he will deliver us out of your hand , O king .
- **Dan 3:18** (—) *target: if*
  > Dan 3:18 But if not , be it known to you, O king , that we will not serve your gods or worship the golden image that you have set up .”
- **Dan 5:16** (—) *target: if*
  > Dan 5:16 But I have heard that you can give interpretations and solve problems . Now if you can read the writing and make known to me its interpretation , you shall be clothed with purple and have a chain of gold around your neck and shall be the third ruler in the kingdom .”

### `H2008` — 4/41 classified · 2 anchor verse(s)

**Group `5630-001`** (4 verses — anchors: 1Sa 1:16, Psa 71:17)

- **1Sa 1:16** 🔵 (✓) *target: along*
  > 1Sa 1:16 Do not regard your servant as a worthless woman , for all along I have been speaking out of my great anxiety and vexation .”
- **Psa 71:17** 🔵 (✓) *target: still*
  > Psa 71:17 O God , from my youth you have taught me, and I still proclaim your wondrous deeds .
- **Num 14:19** (✓) *target: now*
  > Num 14:19 Please pardon the iniquity of this people , according to the greatness of your steadfast love , just as you have forgiven this people , from Egypt until now .”
- **1Sa 7:12** (✓) *target: now*
  > 1Sa 7:12 Then Samuel took a stone and set it up between Mizpah and Shen and called its name Ebenezer ; for he said , “ Till now the Lord has helped us.”

**Group `UNCLASSIFIED`** (37 verses)

- **Gen 15:16** (—) *target: here*
  > Gen 15:16 And they shall come back here in the fourth generation , for the iniquity of the Amorites is not yet complete .”
- **Gen 21:23** (—) *target: here*
  > Gen 21:23 Now therefore swear to me here by God that you will not deal falsely with me or with my descendants or with my posterity , but as I have dealt kindly with you, so you will deal with me and with the land where you have sojourned .”
- **Gen 42:15** (—) *target: here*
  > Gen 42:15 By this you shall be tested : by the life of Pharaoh , you shall not go from this place unless your youngest brother comes here .
- **Gen 44:28** (—) *target: since*
  > Gen 44:28 One left me, and I said , “ Surely he has been torn to pieces ,” and I have never seen him since .
- **Gen 45:5** (—) *target: here*
  > Gen 45:5 And now do not be distressed or angry with yourselves because you sold me here , for God sent me before you to preserve life .
- **Gen 45:8** (—) *target: here*
  > Gen 45:8 So it was not you who sent me here , but God . He has made me a father to Pharaoh , and lord of all his house and ruler over all the land of Egypt .
- **Gen 45:13** (—) *target: here*
  > Gen 45:13 You must tell my father of all my honor in Egypt , and of all that you have seen . Hurry and bring my father down here .”
- **Jos 2:2** (—) *target: here*
  > Jos 2:2 And it was told to the king of Jericho , “ Behold , men of Israel have come here tonight to search out the land .”
- **Jos 3:9** (—) *target: listen*
  > Jos 3:9 And Joshua said to the people of Israel , “ Come here and listen to the words of the Lord your God .”
- **Jos 8:20** (—) *target: way*
  > Jos 8:20 So when the men of Ai looked back , behold , the smoke of the city went up to heaven , and they had no power to flee this way or that, for the people who fled to the wilderness turned back against the pursuers .
- **Jos 18:6** (—) *target: here*
  > Jos 18:6 And you shall describe the land in seven divisions and bring the description here to me. And I will cast lots for you here before the Lord our God .
- **Judg 16:2** (—) *target: here*
  > Judg 16:2 The Gazites were told , “ Samson has come here .” And they surrounded the place and set an ambush for him all night at the gate of the city . They kept quiet all night , saying , “Let us wait till the light of the morning ; then we will kill him .”
- **Judg 16:13** (—) *target: now*
  > Judg 16:13 Then Delilah said to Samson , “ Until now you have mocked me and told me lies . Tell me how you might be bound .” And he said to her, “ If you weave the seven locks of my head with the web and fasten it tight with the pin ^ , then I shall become weak and be like any other man .”
- **1Sa 20:21** (—) *target: then*
  > 1Sa 20:21 And behold , I will send the boy , saying, ‘ Go , find the arrows .’ If I say to the boy , ‘ Look , the arrows are on this side of you, take them,’ then you are to come , for , as the Lord lives , it is safe for you and there is no danger .
- **2Sa 1:10** (—) *target: here*
  > 2Sa 1:10 So I stood beside him and killed him, because I was sure that he could not live after he had fallen . And I took the crown that was on his head and the armlet that was on his arm , and I have brought them here to my lord .”
- **2Sa 5:6** (—) *target: here*
  > 2Sa 5:6 And the king and his men went to Jerusalem against the Jebusites , the inhabitants of the land , who said to David , “You will not come in here , but the blind and the lame will ward you off”— thinking , “ David cannot come in here .”
- **2Sa 14:32** (—) *target: here*
  > 2Sa 14:32 Absalom answered Joab , “ Behold , I sent word to you, ‘ Come here , that I may send you to the king , to ask , “ Why have I come from Geshur ? It would be better for me to be there still .” Now therefore let me go into the presence of the king , and if there is guilt in me, let him put me to death .’”
- **2Sa 20:16** (—) *target: here*
  > 2Sa 20:16 Then a wise woman called from the city , “ Listen ! Listen ! Tell Joab , ‘ Come here , that I may speak to you .’”
- **1Ki 20:40** (—) *target: here*
  > 1Ki 20:40 And as your servant was busy here and there, he was gone .” The king of Israel said to him, “ So shall your judgment be; you yourself have decided it.”
- **2Ki 2:8** (—) *target: one side*
  > 2Ki 2:8 Then Elijah took his cloak and rolled it up and struck the water , and the water was parted to the one side and to the other , till the two of them could go over on dry ground .
- **2Ki 2:14** (—) *target: one side*
  > 2Ki 2:14 Then he took the cloak of Elijah that had fallen from him and struck the water , saying , “ Where is the Lord , the God of Elijah ?” And when he had struck the water , the water was parted to the one side and to the other , and Elisha went over .
- **2Ki 4:35** (—) *target: once*
  > 2Ki 4:35 Then he got up again and walked once back and forth in the house , and went up and stretched himself upon him. The child sneezed seven times , and the child opened his eyes .
- **2Ki 8:7** (—) *target: here*
  > 2Ki 8:7 Now Elisha came to Damascus . Ben-hadad the king of Syria was sick . And when it was told him, “The man of God has come here ,”
- **1Ch 9:18** (—) *target: gate*
  > 1Ch 9:18 until then they were in the king’s gate on the east side as the gatekeepers of the camps of the Levites .
- **1Ch 11:5** (—) *target: took*
  > 1Ch 11:5 The inhabitants of Jebus said to David , “You will not come in here.” Nevertheless, David took the stronghold of Zion , that is, the city of David .
- **1Ch 12:29** (—) *target: majority*
  > 1Ch 12:29 Of the Benjaminites , the kinsmen of Saul , 3,000 , of whom the majority had to that point kept their allegiance to the house of Saul .
- **2Ch 28:13** (—) *target: here*
  > 2Ch 28:13 and said to them, “You shall not bring the captives in here , for you propose to bring upon us guilt against the Lord in addition to our present sins and guilt . For our guilt is already great , and there is fierce wrath against Israel .”
- **Pro 9:4** (—) *target: here*
  > Pro 9:4 “ Whoever is simple , let him turn in here !” To him who lacks sense she says ,
- **Pro 9:16** (—) *target: here*
  > Pro 9:16 “ Whoever is simple , let him turn in here !” And to him who lacks sense she says ,
- **Pro 25:7** (—) *target: here*
  > Pro 25:7 for it is better to be told , “Come up here ,” than to be put lower in the presence of a noble . What your eyes have seen
- **Isa 57:3** (—) *target: sons*
  > Isa 57:3 But you , draw near , sons of the sorceress , offspring of the adulterer and the loose woman .
- **Jer 31:8** (—) *target: here*
  > Jer 31:8 Behold , I will bring them from the north country and gather them from the farthest parts of the earth , among them the blind and the lame , the pregnant woman and she who is in labor , together ; a great company , they shall return here .
- **Jer 48:47** (—) *target: far*
  > Jer 48:47 Yet I will restore the fortunes of Moab in the latter days , declares the Lord .” Thus far is the judgment on Moab .
- **Jer 50:5** (—) *target: it*
  > Jer 50:5 They shall ask the way to Zion , with faces turned toward it , saying, ‘ Come , let us join ourselves to the Lord in an everlasting covenant that will never be forgotten .’
- **Jer 51:64** (—) *target: Thus*
  > Jer 51:64 and say , ‘ Thus shall Babylon sink , to rise no more, because of the disaster that I am bringing upon her, and they shall become exhausted .’” Thus far are the words of Jeremiah .
- **Eze 40:4** (—) *target: here*
  > Eze 40:4 And the man said to me, “ Son of man , look with your eyes , and hear with your ears , and set your heart upon all that I shall show you, for you were brought here in order that I might show it to you. Declare all that you see to the house of Israel .”
- **Dan 12:5** (—) *target: bank*
  > Dan 12:5 Then I , Daniel , looked , and behold , two others stood , one on this bank of the stream and one on that bank of the stream .

### `H2009` — 98/319 classified · 14 anchor verse(s)

**Group `930-001`** (6 verses — anchors: Gen 22:1, Jer 1:6)

- **Gen 22:1** 🔵 (✓) *target: Here*
  > Gen 22:1 After these things God tested Abraham and said to him, “ Abraham !” And he said , “ Here I am.”
- **Jer 1:6** 🔵 (✓) *target: Behold*
  > Jer 1:6 Then I said , “ Ah , Lord God ! Behold , I do not know how to speak , for I am only a youth .”
- **Gen 18:27** (✓) *target: Behold*
  > Gen 18:27 Abraham answered and said , “ Behold , I have undertaken to speak to the Lord , I who am but dust and ashes .
- **Gen 18:31** (✓) *target: Behold*
  > Gen 18:31 He said , “ Behold , I have undertaken to speak to the Lord . Suppose twenty are found there .” He answered , “ For the sake of twenty I will not destroy it.”
- **Gen 22:11** (✓) *target: Here*
  > Gen 22:11 But the angel of the Lord called to him from heaven and said , “ Abraham , Abraham !” And he said , “ Here I am.”
- **Num 20:16** (✓) *target: here*
  > Num 20:16 And when we cried to the Lord , he heard our voice and sent an angel and brought us out of Egypt . And here we are in Kadesh , a city on the edge of your territory .

**Group `930-002`** (14 verses — anchors: Gen 15:3, Neh 9:36)

- **Gen 15:3** 🔵 (✓) *target: member*
  > Gen 15:3 And Abram said , “ Behold , you have given me no offspring , and a member of my household will be my heir .”
- **Neh 9:36** 🔵 (✓) *target: Behold*
  > Neh 9:36 Behold , we are slaves this day ; in the land that you gave to our fathers to enjoy its fruit and its good gifts , behold , we are slaves .
- **Gen 16:2** (✓) *target: Behold*
  > Gen 16:2 And Sarai said to Abram , “ Behold now , the Lord has prevented me from bearing children. Go in to my servant ; it may be that I shall obtain children by her.” And Abram listened to the voice of Sarai .
- **Gen 19:19** (✓) *target: Behold*
  > Gen 19:19 Behold , your servant has found favor in your sight , and you have shown me great kindness in saving my life . But I cannot escape to the hills , lest the disaster overtake me and I die .
- **Gen 25:32** (✓) *target: about*
  > Gen 25:32 Esau said , “ I am about to die ; of what use is a birthright to me?”
- **Neh 5:5** (✓) *target: Yet*
  > Neh 5:5 Now our flesh is as the flesh of our brothers , our children are as their children . Yet we are forcing our sons and our daughters to be slaves , and some of our daughters have already been enslaved , but it is not in our power to help it, for other men have our fields and our vineyards .”
- **Job 13:18** (✓) *target: case*
  > Job 13:18 Behold, I have prepared my case ; I know that I shall be in the right .
- **Job 16:19** (✓) *target: heaven*
  > Job 16:19 Even now, behold, my witness is in heaven , and he who testifies for me is on high .
- **Psa 39:5** (✓) *target: Behold*
  > Psa 39:5 Behold , you have made my days a few handbreadths , and my lifetime is as nothing before you. Surely all mankind stands as a mere breath ! Selah
- **Psa 40:7** (✓) *target: Behold*
  > Psa 40:7 Then I said , “ Behold , I have come ; in the scroll of the book it is written of me :
- **Psa 40:9** (✓) *target: behold*
  > Psa 40:9 I have told the glad news of deliverance in the great congregation ; behold , I have not restrained my lips , as you know , O Lord .
- **Psa 54:4** (✓) *target: Behold*
  > Psa 54:4 Behold , God is my helper ; the Lord is the upholder of my life .
- **Psa 59:3** (✓) *target: behold*
  > Psa 59:3 For behold , they lie in wait for my life ; fierce men stir up strife against me. For no transgression or sin of mine, O Lord ,
- **Psa 119:40** (✓) *target: Behold*
  > Psa 119:40 Behold , I long for your precepts ; in your righteousness give me life !

**Group `930-003`** (5 verses — anchors: Gen 28:12, Gen 28:13)

- **Gen 28:12** 🔵 (✓) *target: behold*
  > Gen 28:12 And he dreamed , and behold , there was a ladder set up on the earth , and the top of it reached to heaven . And behold , the angels of God were ascending and descending on it !
- **Gen 28:13** 🔵 (✓) *target: behold*
  > Gen 28:13 And behold , the Lord stood above it and said , “ I am the Lord , the God of Abraham your father and the God of Isaac . The land on which you lie I will give to you and to your offspring .
- **Gen 15:12** (✓) *target: behold*
  > Gen 15:12 As the sun was going down , a deep sleep fell on Abram . And behold , dreadful and great darkness fell upon him .
- **Gen 15:17** (✓) *target: behold*
  > Gen 15:17 When the sun had gone down and it was dark , behold , a smoking fire pot and a flaming torch passed between these pieces .
- **Gen 28:15** (✓) *target: Behold*
  > Gen 28:15 Behold , I am with you and will keep you wherever you go , and will bring you back to this land . For I will not leave you until I have done what I have promised you .”

**Group `930-004`** (17 verses — anchors: Gen 16:11, Hos 2:14)

- **Gen 16:11** 🔵 (✓) *target: Behold*
  > Gen 16:11 And the angel of the Lord said to her, “ Behold , you are pregnant and shall bear a son . You shall call his name Ishmael , because the Lord has listened to your affliction .
- **Hos 2:14** 🔵 (✓) *target: behold*
  > Hos 2:14 “ Therefore , behold , I will allure her, and bring her into the wilderness , and speak tenderly to her.
- **Gen 16:6** (✓) *target: Behold*
  > Gen 16:6 But Abram said to Sarai , “ Behold , your servant is in your power ; do to her as you please .” Then Sarai dealt harshly with her, and she fled from her .
- **Gen 20:16** (✓) *target: given*
  > Gen 20:16 To Sarah he said , “Behold, I have given your brother a thousand pieces of silver . It is a sign of your innocence in the eyes of all who are with you , and before everyone you are vindicated .”
- **Psa 33:18** (✓) *target: Behold*
  > Psa 33:18 Behold , the eye of the Lord is on those who fear him, on those who hope in his steadfast love ,
- **Psa 121:4** (✓) *target: Behold*
  > Psa 121:4 Behold , he who keeps Israel will neither slumber nor sleep .
- **Psa 123:2** (✓) *target: Behold*
  > Psa 123:2 Behold , as the eyes of servants look to the hand of their master , as the eyes of a maidservant to the hand of her mistress , so our eyes look to the Lord our God , till he has mercy upon us .
- **Psa 128:4** (✓) *target: Behold*
  > Psa 128:4 Behold , thus shall the man be blessed who fears the Lord .
- **Pro 1:23** (✓) *target: behold*
  > Pro 1:23 If you turn at my reproof , behold , I will pour out my spirit to you; I will make my words known to you .
- **Isa 7:14** (✓) *target: Behold*
  > Isa 7:14 Therefore the Lord himself will give you a sign . Behold , the virgin shall conceive and bear a son , and shall call his name Immanuel .
- **Isa 12:2** (✓) *target: Behold*
  > Isa 12:2 “ Behold , God is my salvation ; I will trust , and will not be afraid ; for the Lord God is my strength and my song , and he has become my salvation .”
- **Isa 25:9** (✓) *target: Behold*
  > Isa 25:9 It will be said on that day , “ Behold , this is our God ; we have waited for him, that he might save us. This is the Lord ; we have waited for him; let us be glad and rejoice in his salvation .”
- **Isa 35:4** (✓) *target: Behold*
  > Isa 35:4 Say to those who have an anxious heart , “Be strong ; fear not ! Behold , your God will come with vengeance , with the recompense of God . He will come and save you .”
- **Isa 40:9** (✓) *target: Behold*
  > Isa 40:9 Go on up to a high mountain , O Zion , herald of good news ; lift up your voice with strength , O Jerusalem , herald of good news ; lift it up , fear not ; say to the cities of Judah , “ Behold your God !”
- **Nah 1:15** (✓) *target: Behold*
  > Nah 1:15 Behold , upon the mountains , the feet of him who brings good news , who publishes peace ! Keep your feasts , O Judah ; fulfill your vows , for never again shall the worthless pass through you; he is utterly cut off .
- **Zec 9:9** (✓) *target: Behold*
  > Zec 9:9 Rejoice greatly , O daughter of Zion ! Shout aloud, O daughter of Jerusalem ! Behold , your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey , on a colt , the foal of a donkey .
- **Mal 3:1** (✓) *target: Behold*
  > Mal 3:1 “ Behold , I send my messenger , and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple ; and the messenger of the covenant in whom you delight , behold , he is coming , says the Lord of hosts .

**Group `930-005`** (21 verses — anchors: Isa 6:7, Hab 2:4)

- **Isa 6:7** 🔵 (✓) *target: Behold*
  > Isa 6:7 And he touched my mouth and said : “ Behold , this has touched your lips ; your guilt is taken away , and your sin atoned for .”
- **Hab 2:4** 🔵 (✓) *target: Behold*
  > Hab 2:4 “ Behold , his soul is puffed up ; it is not upright within him, but the righteous shall live by his faith .
- **Gen 6:12** (✓) *target: behold*
  > Gen 6:12 And God saw the earth , and behold , it was corrupt , for all flesh had corrupted their way on the earth .
- **Gen 20:3** (✓) *target: dead man*
  > Gen 20:3 But God came to Abimelech in a dream by night and said to him, “Behold, you are a dead man because of the woman whom you have taken , for she is a man’s wife .”
- **Gen 26:9** (✓) *target: Behold*
  > Gen 26:9 So Abimelech called Isaac and said , “ Behold , she is your wife . How then could you say , ‘She is my sister ’?” Isaac said to him, “ Because I thought , ‘ Lest I die because of her .’”
- **Gen 27:42** (✓) *target: Behold*
  > Gen 27:42 But the words of Esau her older son were told to Rebekah . So she sent and called Jacob her younger son and said to him, “ Behold , your brother Esau comforts himself about you by planning to kill you .
- **Num 32:14** (✓) *target: behold*
  > Num 32:14 And behold , you have risen in your fathers ’ place , a brood of sinful men , to increase still more the fierce anger of the Lord against Israel !
- **Num 32:23** (✓) *target: behold*
  > Num 32:23 But if you will not do so , behold , you have sinned against the Lord , and be sure your sin will find you out.
- **Deu 9:13** (✓) *target: behold*
  > Deu 9:13 “Furthermore, the Lord said to me, ‘I have seen this people , and behold , it is a stubborn people .
- **Deu 9:16** (✓) *target: behold*
  > Deu 9:16 And I looked , and behold , you had sinned against the Lord your God . You had made yourselves a golden calf . You had turned aside quickly from the way that the Lord had commanded you .
- **Job 5:17** (✓) *target: Behold*
  > Job 5:17 “ Behold , blessed is the one whom God reproves ; therefore despise not the discipline of the Almighty .
- **Psa 7:14** (✓) *target: Behold*
  > Psa 7:14 Behold , the wicked man conceives evil and is pregnant with mischief and gives birth to lies .
- **Psa 11:2** (✓) *target: behold*
  > Psa 11:2 for behold , the wicked bend the bow ; they have fitted their arrow to the string to shoot in the dark at the upright in heart ;
- **Psa 52:7** (✓) *target: See*
  > Psa 52:7 “ See the man who would not make God his refuge , but trusted in the abundance of his riches and sought refuge in his own destruction !”
- **Psa 73:27** (✓) *target: behold*
  > Psa 73:27 For behold , those who are far from you shall perish ; you put an end to everyone who is unfaithful to you .
- **Psa 83:2** (✓) *target: behold*
  > Psa 83:2 For behold , your enemies make an uproar ; those who hate you have raised their heads .
- **Pro 7:10** (✓) *target: behold*
  > Pro 7:10 And behold , the woman meets him, dressed as a prostitute , wily of heart .
- **Isa 5:7** (✓) *target: behold*
  > Isa 5:7 For the vineyard of the Lord of hosts is the house of Israel , and the men of Judah are his pleasant planting ; and he looked for justice , but behold , bloodshed ; for righteousness , but behold , an outcry !
- **Isa 36:6** (✓) *target: Behold*
  > Isa 36:6 Behold , you are trusting in Egypt , that broken reed of a staff , which will pierce the hand of any man who leans on it. Such is Pharaoh king of Egypt to all who trust in him.
- **Isa 38:17** (✓) *target: Behold*
  > Isa 38:17 Behold , it was for my welfare that I had great bitterness ; but in love you have delivered my life from the pit of destruction , for you have cast all my sins behind your back .
- **Jer 3:5** (✓) *target: Behold*
  > Jer 3:5 will he be angry forever , will he be indignant to the end ?’ Behold , you have spoken , but you have done all the evil that you could .”

**Group `930-006`** (13 verses — anchors: Psa 133:1, Ecc 2:11)

- **Psa 133:1** 🔵 (✓) *target: good*
  > A Song of Ascents . Of David . Psa 133:1 Behold, how good and pleasant it is when brothers dwell in unity !
- **Ecc 2:11** 🔵 (✓) *target: behold*
  > Ecc 2:11 Then I considered all that my hands had done and the toil I had expended in doing it , and behold , all was vanity and a striving after wind , and there was nothing to be gained under the sun .
- **Gen 27:2** (✓) *target: Behold*
  > Gen 27:2 He said , “ Behold , I am old ; I do not know the day of my death .
- **Neh 6:12** (✓) *target: saw*
  > Neh 6:12 And I understood and saw that God had not sent him, but he had pronounced the prophecy against me because Tobiah and Sanballat had hired him .
- **Psa 73:15** (✓) *target: generation*
  > Psa 73:15 If I had said , “I will speak thus ,” I would have betrayed the generation of your children .
- **Ecc 1:16** (✓) *target: great*
  > Ecc 1:16 I said in my heart , “ I have acquired great wisdom , surpassing all who were over Jerusalem before me, and my heart has had great experience of wisdom and knowledge .”
- **Ecc 2:1** (✓) *target: behold*
  > Ecc 2:1 I said in my heart , “ Come now , I will test you with pleasure ; enjoy yourself.” But behold , this also was vanity .
- **Ecc 4:1** (✓) *target: behold*
  > Ecc 4:1 Again I saw all the oppressions that are done under the sun . And behold , the tears of the oppressed , and they had no one to comfort them! On the side of their oppressors there was power , and there was no one to comfort them.
- **Ecc 5:18** (✓) *target: Behold*
  > Ecc 5:18 Behold , what I have seen to be good and fitting is to eat and drink and find enjoyment in all the toil with which one toils under the sun the few days of his life that God has given him, for this is his lot .
- **Song 2:8** (✓) *target: Behold*
  > Song 2:8 The voice of my beloved ! Behold , he comes , leaping over the mountains , bounding over the hills .
- **Song 2:9** (✓) *target: Behold*
  > Song 2:9 My beloved is like a gazelle or a young stag . Behold , there he stands behind our wall , gazing through the windows , looking through the lattice .
- **Isa 8:18** (✓) *target: Behold*
  > Isa 8:18 Behold , I and the children whom the Lord has given me are signs and portents in Israel from the Lord of hosts , who dwells on Mount Zion .
- **Isa 52:13** (✓) *target: Behold*
  > Isa 52:13 Behold , my servant shall act wisely ; he shall be high and lifted up , and shall be exalted .

**Group `930-007`** (22 verses — anchors: Job 3:7, Job 32:19)

- **Job 3:7** 🔵 (✓) *target: Behold*
  > Job 3:7 Behold , let that night be barren ; let no joyful cry enter it .
- **Job 32:19** 🔵 (✓) *target: Behold*
  > Job 32:19 Behold , my belly is like wine that has no vent ; like new wineskins ready to burst .
- **Gen 19:8** (✓) *target: Behold*
  > Gen 19:8 Behold , I have two daughters who have not known any man . Let me bring them out to you, and do to them as you please . Only do nothing to these men , for they have come under the shelter of my roof .”
- **Gen 27:36** (✓) *target: behold*
  > Gen 27:36 Esau said , “Is he not rightly named Jacob ? For he has cheated me these two times . He took away my birthright , and behold , now he has taken away my blessing .” Then he said , “Have you not reserved a blessing for me?”
- **Num 24:10** (✓) *target: behold*
  > Num 24:10 And Balak’s anger was kindled against Balaam , and he struck his hands together. And Balak said to Balaam , “ I called you to curse my enemies , and behold , you have blessed them these three times .
- **Job 9:19** (✓) *target: justice*
  > Job 9:19 If it is a contest of strength , behold, he is mighty! If it is a matter of justice , who can summon him?
- **Job 33:7** (✓) *target: Behold*
  > Job 33:7 Behold , no fear of me need terrify you; my pressure will not be heavy upon you.
- **Isa 8:22** (✓) *target: behold*
  > Isa 8:22 And they will look to the earth , but behold , distress and darkness , the gloom of anguish . And they will be thrust into thick darkness .
- **Isa 20:6** (✓) *target: Behold*
  > Isa 20:6 And the inhabitants of this coastland will say in that day , ‘ Behold , this is what has happened to those in whom we hoped and to whom we fled for help to be delivered from the king of Assyria ! And we, how shall we escape ?’”
- **Isa 22:13** (✓) *target: behold*
  > Isa 22:13 and behold , joy and gladness , killing oxen and slaughtering sheep , eating flesh and drinking wine . “Let us eat and drink , for tomorrow we die .”
- **Isa 29:8** (✓) *target: is*
  > Isa 29:8 As when a hungry man dreams , and behold, he is eating , and awakes with his hunger not satisfied , or as when a thirsty man dreams , and behold, he is drinking and awakes faint , with his thirst not quenched, so shall the multitude of all the nations be that fight against Mount Zion .
- **Isa 48:10** (✓) *target: Behold*
  > Isa 48:10 Behold , I have refined you, but not as silver ; I have tried you in the furnace of affliction .
- **Isa 59:9** (✓) *target: behold*
  > Isa 59:9 Therefore justice is far from us, and righteousness does not overtake us; we hope for light , and behold , darkness , and for brightness , but we walk in gloom .
- **Isa 60:2** (✓) *target: behold*
  > Isa 60:2 For behold , darkness shall cover the earth , and thick darkness the peoples ; but the Lord will arise upon you, and his glory will be seen upon you.
- **Isa 65:13** (✓) *target: Behold*
  > Isa 65:13 Therefore thus says the Lord God : “ Behold , my servants shall eat , but you shall be hungry ; behold , my servants shall drink , but you shall be thirsty ; behold , my servants shall rejoice , but you shall be put to shame ;
- **Isa 65:14** (✓) *target: behold*
  > Isa 65:14 behold , my servants shall sing for gladness of heart , but you shall cry out for pain of heart and shall wail for breaking of spirit .
- **Amo 4:13** (✓) *target: behold*
  > Amo 4:13 For behold , he who forms the mountains and creates the wind , and declares to man what is his thought , who makes the morning darkness , and treads on the heights of the earth — the Lord , the God of hosts , is his name !
- **Amo 8:11** (✓) *target: Behold*
  > Amo 8:11 “ Behold , the days are coming ,” declares the Lord God , “when I will send a famine on the land — not a famine of bread , nor a thirst for water , but of hearing the words of the Lord .
- **Hab 2:19** (✓) *target: Behold*
  > Hab 2:19 Woe to him who says to a wooden thing, Awake ; to a silent stone , Arise ! Can this teach ? Behold , it is overlaid with gold and silver , and there is no breath at all in it.
- **Hag 1:9** (✓) *target: behold*
  > Hag 1:9 You looked for much , and behold , it came to little . And when you brought it home , I blew it away . Why ? declares the Lord of hosts . Because of my house that lies in ruins , while each of you busies himself with his own house .
- **Zec 3:9** (✓) *target: behold*
  > Zec 3:9 For behold , on the stone that I have set before Joshua , on a single stone with seven eyes , I will engrave its inscription , declares the Lord of hosts , and I will remove the iniquity of this land in a single day .
- **Mal 1:13** (✓) *target: What*
  > Mal 1:13 But you say , ‘ What a weariness this is,’ and you snort at it, says the Lord of hosts . You bring what has been taken by violence or is lame or sick , and this you bring as your offering ! Shall I accept that from your hand ? says the Lord .

**Group `UNCLASSIFIED`** (221 verses)

- **Gen 1:29** (—) *target: Behold*
  > Gen 1:29 And God said , “ Behold , I have given you every plant yielding seed that is on the face of all the earth , and every tree with seed in its fruit . You shall have them for food .
- **Gen 1:31** (—) *target: behold*
  > Gen 1:31 And God saw everything that he had made , and behold , it was very good . And there was evening and there was morning , the sixth day .
- **Gen 6:17** (—) *target: behold*
  > Gen 6:17 For behold , I will bring a flood of waters upon the earth to destroy all flesh in which is the breath of life under heaven . Everything that is on the earth shall die .
- **Gen 8:11** (—) *target: behold*
  > Gen 8:11 And the dove came back to him in the evening , and behold , in her mouth was a freshly plucked olive leaf . So Noah knew that the waters had subsided from the earth .
- **Gen 8:13** (—) *target: behold*
  > Gen 8:13 In the six hundred and first year , in the first month, the first day of the month , the waters were dried from off the earth . And Noah removed the covering of the ark and looked , and behold , the face of the ground was dry .
- **Gen 12:11** (—) *target: I*
  > Gen 12:11 When he was about to enter Egypt , he said to Sarai his wife , “ I know that you are a woman beautiful in appearance ,
- **Gen 12:19** (—) *target: wife*
  > Gen 12:19 Why did you say , ‘She is my sister ,’ so that I took her for my wife ? Now then , here is your wife ; take her, and go .”
- **Gen 15:4** (—) *target: behold*
  > Gen 15:4 And behold , the word of the Lord came to him : “ This man shall not be your heir ; your very own son shall be your heir .”
- **Gen 16:14** (—) *target: between*
  > Gen 16:14 Therefore the well was called Beer-lahai-roi ; it lies between Kadesh and Bered .
- **Gen 17:4** (—) *target: Behold*
  > Gen 17:4 “ Behold , my covenant is with you, and you shall be the father of a multitude of nations .
- **Gen 17:20** (—) *target: behold*
  > Gen 17:20 As for Ishmael , I have heard you; behold , I have blessed him and will make him fruitful and multiply him greatly . He shall father twelve princes , and I will make him into a great nation .
- **Gen 18:2** (—) *target: behold*
  > Gen 18:2 He lifted up his eyes and looked , and behold , three men were standing in front of him. When he saw them, he ran from the tent door to meet them and bowed himself to the earth
- **Gen 18:9** (—) *target: tent*
  > Gen 18:9 They said to him, “ Where is Sarah your wife ?” And he said , “She is in the tent .”
- **Gen 18:10** (—) *target: son*
  > Gen 18:10 The Lord said , “I will surely return to you about this time next year , and Sarah your wife shall have a son .” And Sarah was listening at the tent door behind him .
- **Gen 19:2** (—) *target: please*
  > Gen 19:2 and said , “My lords , please turn aside to your servant’s house and spend the night and wash your feet . Then you may rise up early and go on your way .” They said , “ No ; we will spend the night in the town square .”
- **Gen 19:20** (—) *target: Behold*
  > Gen 19:20 Behold , this city is near enough to flee to, and it is a little one . Let me escape there —is it not a little one ?—and my life will be saved !”
- **Gen 19:21** (—) *target: Behold*
  > Gen 19:21 He said to him, “ Behold , I grant you this favor also, that I will not overthrow the city of which you have spoken .
- **Gen 19:28** (—) *target: behold*
  > Gen 19:28 And he looked down toward Sodom and Gomorrah and toward all the land of the valley , and he looked and, behold , the smoke of the land went up like the smoke of a furnace .
- **Gen 20:15** (—) *target: land*
  > Gen 20:15 And Abimelech said , “Behold, my land is before you ; dwell where it pleases you .”
- **Gen 22:7** (—) *target: Here*
  > Gen 22:7 And Isaac said to his father Abraham , “My father !” And he said , “ Here I am, my son .” He said , “ Behold , the fire and the wood , but where is the lamb for a burnt offering ?”
- **Gen 22:13** (—) *target: behold*
  > Gen 22:13 And Abraham lifted up his eyes and looked , and behold , behind him was a ram , caught in a thicket by his horns . And Abraham went and took the ram and offered it up as a burnt offering instead of his son .
- **Gen 22:20** (—) *target: Behold*
  > Gen 22:20 Now after these things it was told to Abraham , “ Behold , Milcah also has borne children to your brother Nahor :
- **Gen 24:13** (—) *target: Behold*
  > Gen 24:13 Behold , I am standing by the spring of water , and the daughters of the men of the city are coming out to draw water .
- **Gen 24:15** (—) *target: behold*
  > Gen 24:15 Before he had finished speaking , behold , Rebekah , who was born to Bethuel the son of Milcah , the wife of Nahor , Abraham’s brother , came out with her water jar on her shoulder .
- **Gen 24:30** (—) *target: behold*
  > Gen 24:30 As soon as he saw the ring and the bracelets on his sister’s arms , and heard the words of Rebekah his sister , “ Thus the man spoke to me,” he went to the man . And behold , he was standing by the camels at the spring .
- **Gen 24:43** (—) *target: behold*
  > Gen 24:43 behold , I am standing by the spring of water . Let the virgin who comes out to draw water , to whom I shall say , “ Please give me a little water from your jar to drink ,”
- **Gen 24:45** (—) *target: Rebekah*
  > Gen 24:45 “ Before I had finished speaking in my heart , behold, Rebekah came out with her water jar on her shoulder , and she went down to the spring and drew water . I said to her, ‘ Please let me drink .’
- **Gen 24:51** (—) *target: Behold*
  > Gen 24:51 Behold , Rebekah is before you ; take her and go , and let her be the wife of your master’s son , as the Lord has spoken .”
- **Gen 24:63** (—) *target: behold*
  > Gen 24:63 And Isaac went out to meditate in the field toward evening . And he lifted up his eyes and saw , and behold , there were camels coming .
- **Gen 25:24** (—) *target: behold*
  > Gen 25:24 When her days to give birth were completed , behold , there were twins in her womb .
- **Gen 26:8** (—) *target: Isaac*
  > Gen 26:8 When he had been there a long time , Abimelech king of the Philistines looked out of a window and saw Isaac laughing with Rebekah his wife .
- **Gen 27:1** (—) *target: am*
  > Gen 27:1 When Isaac was old and his eyes were dim so that he could not see , he called Esau his older son and said to him, “My son ”; and he answered , “Here I am .”
- **Gen 27:6** (—) *target: heard*
  > Gen 27:6 Rebekah said to her son Jacob , “I heard your father speak to your brother Esau ,
- **Gen 27:18** (—) *target: am*
  > Gen 27:18 So he went in to his father and said , “My father .” And he said , “Here I am . Who are you, my son ?”
- **Gen 27:39** (—) *target: Behold*
  > Gen 27:39 Then Isaac his father answered and said to him: “ Behold , away from the fatness of the earth shall your dwelling be, and away from the dew of heaven on high.
- **Gen 29:2** (—) *target: saw*
  > Gen 29:2 As he looked , he saw a well in the field , and behold , three flocks of sheep lying beside it, for out of that well the flocks were watered . The stone on the well’s mouth was large ,
- **Gen 29:6** (—) *target: see*
  > Gen 29:6 He said to them, “Is it well with him?” They said , “It is well ; and see , Rachel his daughter is coming with the sheep !”
- **Num 3:12** (—) *target: Behold*
  > Num 3:12 “ Behold , I have taken the Levites from among the people of Israel instead of every firstborn who opens the womb among the people of Israel . The Levites shall be mine,
- **Num 12:10** (—) *target: behold*
  > Num 12:10 When the cloud removed from over the tent , behold , Miriam was leprous , like snow . And Aaron turned toward Miriam , and behold , she was leprous .
- **Num 16:42** (—) *target: behold*
  > Num 16:42 And when the congregation had assembled against Moses and against Aaron , they turned toward the tent of meeting . And behold , the cloud covered it, and the glory of the Lord appeared .
- **Num 16:47** (—) *target: behold*
  > Num 16:47 So Aaron took it as Moses said and ran into the midst of the assembly . And behold , the plague had already begun among the people . And he put on the incense and made atonement for the people .
- **Num 17:8** (—) *target: behold*
  > Num 17:8 On the next day Moses went into the tent of the testimony , and behold , the staff of Aaron for the house of Levi had sprouted and put forth buds and produced blossoms , and it bore ripe almonds .
- **Num 18:6** (—) *target: behold*
  > Num 18:6 And behold , I have taken your brothers the Levites from among the people of Israel . They are a gift to you, given to the Lord , to do the service of the tent of meeting .
- **Num 18:8** (—) *target: given*
  > Num 18:8 Then the Lord spoke to Aaron , “Behold, I have given you charge of the contributions made to me, all the consecrated things of the people of Israel . I have given them to you as a portion and to your sons as a perpetual due .
- **Num 18:21** (—) *target: given*
  > Num 18:21 “To the Levites I have given every tithe in Israel for an inheritance , in return for their service that they do , their service in the tent of meeting ,
- **Num 22:5** (—) *target: Behold*
  > Num 22:5 sent messengers to Balaam the son of Beor at Pethor , which is near the River in the land of the people of Amaw , to call him, saying , “ Behold , a people has come out of Egypt . They cover the face of the earth , and they are dwelling opposite me .
- **Num 22:11** (—) *target: Behold*
  > Num 22:11 ‘ Behold , a people has come out of Egypt , and it covers the face of the earth . Now come , curse them for me. Perhaps I shall be able to fight against them and drive them out.’”
- **Num 22:32** (—) *target: Behold*
  > Num 22:32 And the angel of the Lord said to him, “ Why have you struck your donkey these three times ? Behold , I have come out to oppose you because your way is perverse before me .
- **Num 22:38** (—) *target: Behold*
  > Num 22:38 Balaam said to Balak , “ Behold , I have come to you! Have I now any power of my own to speak anything ? The word that God puts in my mouth , that must I speak .”
- **Num 23:6** (—) *target: behold*
  > Num 23:6 And he returned to him, and behold , he and all the princes of Moab were standing beside his burnt offering .
- **Num 23:11** (—) *target: behold*
  > Num 23:11 And Balak said to Balaam , “ What have you done to me? I took you to curse my enemies , and behold , you have done nothing but bless them.”
- **Num 23:17** (—) *target: behold*
  > Num 23:17 And he came to him, and behold , he was standing beside his burnt offering , and the princes of Moab with him. And Balak said to him, “ What has the Lord spoken ?”
- **Num 23:20** (—) *target: Behold*
  > Num 23:20 Behold , I received a command to bless : he has blessed , and I cannot revoke it .
- **Num 24:11** (—) *target: held you back*
  > Num 24:11 Therefore now flee to your own place . I said , ‘I will certainly honor you,’ but the Lord has held you back from honor .”
- **Num 25:6** (—) *target: behold*
  > Num 25:6 And behold , one of the people of Israel came and brought a Midianite woman to his family , in the sight of Moses and in the sight of the whole congregation of the people of Israel , while they were weeping in the entrance of the tent of meeting .
- **Num 32:1** (—) *target: behold*
  > Num 32:1 Now the people of Reuben and the people of Gad had a very great number of livestock . And they saw the land of Jazer and the land of Gilead , and behold , the place was a place for livestock .
- **Deu 1:10** (—) *target: behold*
  > Deu 1:10 The Lord your God has multiplied you, and behold , you are today as numerous as the stars of heaven .
- **Deu 3:11** (—) *target: Behold*
  > Deu 3:11 (For only Og the king of Bashan was left of the remnant of the Rephaim . Behold , his bed was a bed of iron . Is it not in Rabbah of the Ammonites ? Nine cubits was its length , and four cubits its breadth , according to the common cubit .)
- **Deu 13:14** (—) *target: behold*
  > Deu 13:14 then you shall inquire and make search and ask diligently . And behold , if it be true and certain that such an abomination has been done among you,
- **Deu 17:4** (—) *target: if*
  > Deu 17:4 and it is told you and you hear of it, then you shall inquire diligently , and if it is true and certain that such an abomination has been done in Israel ,
- **Deu 19:18** (—) *target: if*
  > Deu 19:18 The judges shall inquire diligently , and if the witness is a false witness and has accused his brother falsely ,
- **Deu 22:17** (—) *target: behold*
  > Deu 22:17 and behold , he has accused her of misconduct , saying , “I did not find in your daughter evidence of virginity .” And yet this is the evidence of my daughter’s virginity .’ And they shall spread the cloak before the elders of the city .
- **Deu 26:10** (—) *target: behold*
  > Deu 26:10 And behold , now I bring the first of the fruit of the ground , which you, O Lord , have given me.’ And you shall set it down before the Lord your God and worship before the Lord your God .
- **Deu 31:16** (—) *target: Behold*
  > Deu 31:16 And the Lord said to Moses , “ Behold , you are about to lie down with your fathers . Then this people will rise and whore after the foreign gods among them in the land that they are entering , and they will forsake me and break my covenant that I have made with them .
- **Jos 2:2** (—) *target: Behold*
  > Jos 2:2 And it was told to the king of Jericho , “ Behold , men of Israel have come here tonight to search out the land .”
- **Jos 2:18** (—) *target: Behold*
  > Jos 2:18 Behold , when we come into the land , you shall tie this scarlet cord in the window through which you let us down , and you shall gather into your house your father and mother , your brothers , and all your father’s household .
- **Jos 3:11** (—) *target: Behold*
  > Jos 3:11 Behold , the ark of the covenant of the Lord of all the earth is passing over before you into the Jordan .
- **Jos 5:13** (—) *target: behold*
  > Jos 5:13 When Joshua was by Jericho , he lifted up his eyes and looked , and behold , a man was standing before him with his drawn sword in his hand . And Joshua went to him and said to him, “Are you for us, or for our adversaries ?”
- **Jos 7:21** (—) *target: see*
  > Jos 7:21 when I saw among the spoil a beautiful cloak from Shinar , and 200 shekels of silver , and a bar of gold weighing 50 shekels , then I coveted them and took them. And see , they are hidden in the earth inside my tent , with the silver underneath .”
- **Jos 7:22** (—) *target: behold*
  > Jos 7:22 So Joshua sent messengers , and they ran to the tent ; and behold , it was hidden in his tent with the silver underneath .
- **Jos 8:20** (—) *target: went up*
  > Jos 8:20 So when the men of Ai looked back , behold , the smoke of the city went up to heaven , and they had no power to flee this way or that, for the people who fled to the wilderness turned back against the pursuers .
- **Jos 9:12** (—) *target: dry*
  > Jos 9:12 Here is our bread . It was still warm when we took it from our houses as our food for the journey on the day we set out to come to you, but now , behold, it is dry and crumbly .
- **Jos 9:13** (—) *target: burst*
  > Jos 9:13 These wineskins were new when we filled them, and behold, they have burst . And these garments and sandals of ours are worn out from the very long journey .”
- **Jos 14:10** (—) *target: behold*
  > Jos 14:10 And now , behold , the Lord has kept me alive , just as he said , these forty-five years since the time that the Lord spoke this word to Moses , while Israel walked in the wilderness . And now , behold , I am this day eighty-five years old .
- **Jos 22:11** (—) *target: built*
  > Jos 22:11 And the people of Israel heard it said , “Behold, the people of Reuben and the people of Gad and the half-tribe of Manasseh have built the altar at the frontier of the land of Canaan , in the region about the Jordan , on the side that belongs to the people of Israel .”
- **Jos 23:14** (—) *target: now*
  > Jos 23:14 “And now I am about to go the way of all the earth , and you know in your hearts and souls , all of you, that not one word has failed of all the good things that the Lord your God promised concerning you. All have come to pass for you; not one of them has failed .
- **Jos 24:27** (—) *target: stone*
  > Jos 24:27 And Joshua said to all the people , “Behold, this stone shall be a witness against us, for it has heard all the words of the Lord that he spoke to us. Therefore it shall be a witness against you, lest you deal falsely with your God .”
- **Judg 1:2** (—) *target: behold*
  > Judg 1:2 The Lord said , “ Judah shall go up ; behold , I have given the land into his hand .”
- **Judg 3:24** (—) *target: Surely*
  > Judg 3:24 When he had gone , the servants came , and when they saw that the doors of the roof chamber were locked , they thought , “ Surely he is relieving himself in the closet of the cool chamber .”
- **Judg 3:25** (—) *target: when*
  > Judg 3:25 And they waited till they were embarrassed . But when he still did not open the doors of the roof chamber , they took the key and opened them, and there lay their lord dead on the floor .
- **Judg 4:22** (—) *target: behold*
  > Judg 4:22 And behold , as Barak was pursuing Sisera , Jael went out to meet him and said to him, “ Come , and I will show you the man whom you are seeking .” So he went in to her tent, and there lay Sisera dead , with the tent peg in his temple .
- **Judg 6:15** (—) *target: Behold*
  > Judg 6:15 And he said to him, “ Please , Lord , how can I save Israel ? Behold , my clan is the weakest in Manasseh , and I am the least in my father’s house .”
- **Judg 6:28** (—) *target: behold*
  > Judg 6:28 When the men of the town rose early in the morning , behold , the altar of Baal was broken down , and the Asherah beside it was cut down , and the second bull was offered on the altar that had been built .
- **Judg 6:37** (—) *target: behold*
  > Judg 6:37 behold , I am laying a fleece of wool on the threshing floor . If there is dew on the fleece alone , and it is dry on all the ground , then I shall know that you will save Israel by my hand , as you have said .”
- **Judg 7:13** (—) *target: behold*
  > Judg 7:13 When Gideon came , behold , a man was telling a dream to his comrade . And he said , “ Behold , I dreamed a dream , and behold, a cake of barley bread tumbled into the camp of Midian and came to the tent and struck it so that it fell and turned it upside down , so that the tent lay flat .”
- **Judg 7:17** (—) *target: come*
  > Judg 7:17 And he said to them, “ Look at me, and do likewise . When I come to the outskirts of the camp , do as I do .
- **Judg 8:15** (—) *target: Behold*
  > Judg 8:15 And he came to the men of Succoth and said , “ Behold Zebah and Zalmunna , about whom you taunted me, saying , ‘Are the hands of Zebah and Zalmunna already in your hand , that we should give bread to your men who are exhausted ?’”
- **Judg 9:31** (—) *target: Gaal*
  > Judg 9:31 And he sent messengers to Abimelech secretly , saying , “Behold, Gaal the son of Ebed and his relatives have come to Shechem , and they are stirring up the city against you .
- **Judg 9:33** (—) *target: people*
  > Judg 9:33 Then in the morning , as soon as the sun is up , rise early and rush upon the city . And when he and the people who are with him come out against you, you may do to them as your hand finds to do.”
- **Judg 9:36** (—) *target: people*
  > Judg 9:36 And when Gaal saw the people , he said to Zebul , “ Look , people are coming down from the mountaintops !” And Zebul said to him, “ You mistake the shadow of the mountains for men .”
- **Judg 9:37** (—) *target: people*
  > Judg 9:37 Gaal spoke again and said , “ Look , people are coming down from the center of the land , and one company is coming from the direction of the Diviners ’ Oak .”
- **Judg 9:43** (—) *target: people*
  > Judg 9:43 He took his people and divided them into three companies and set an ambush in the fields . And he looked and saw the people coming out of the city . So he rose against them and killed them .
- **Judg 11:34** (—) *target: daughter*
  > Judg 11:34 Then Jephthah came to his home at Mizpah . And behold, his daughter came out to meet him with tambourines and with dances . She was his only child ; besides her he had neither son nor daughter .
- **Judg 13:3** (—) *target: barren*
  > Judg 13:3 And the angel of the Lord appeared to the woman and said to her, “Behold, you are barren and have not borne children , but you shall conceive and bear a son .
- **Judg 13:5** (—) *target: conceive*
  > Judg 13:5 for behold, you shall conceive and bear a son . No razor shall come upon his head , for the child shall be a Nazirite to God from the womb , and he shall begin to save Israel from the hand of the Philistines .”
- **Judg 13:7** (—) *target: conceive*
  > Judg 13:7 but he said to me, ‘Behold, you shall conceive and bear a son . So then drink no wine or strong drink , and eat nothing unclean , for the child shall be a Nazirite to God from the womb to the day of his death .’”
- **Judg 13:10** (—) *target: appeared*
  > Judg 13:10 So the woman ran quickly and told her husband , “Behold, the man who came to me the other day has appeared to me .”
- **Judg 14:5** (—) *target: young*
  > Judg 14:5 Then Samson went down with his father and mother to Timnah , and they came to the vineyards of Timnah . And behold, a young lion came toward him roaring .
- **Judg 14:8** (—) *target: swarm*
  > Judg 14:8 After some days he returned to take her. And he turned aside to see the carcass of the lion , and behold, there was a swarm of bees in the body of the lion , and honey .
- **Judg 14:16** (—) *target: father*
  > Judg 14:16 And Samson’s wife wept over him and said , “You only hate me; you do not love me. You have put a riddle to my people , and you have not told me what it is.” And he said to her, “Behold, I have not told my father nor my mother , and shall I tell you?”
- **Judg 16:10** (—) *target: Behold*
  > Judg 16:10 Then Delilah said to Samson , “ Behold , you have mocked me and told me lies . Please tell me how you might be bound .”
- **Judg 17:2** (—) *target: behold*
  > Judg 17:2 And he said to his mother , “The 1,100 pieces of silver that were taken from you , about which you uttered a curse , and also spoke it in my ears , behold , the silver is with me ; I took it.” And his mother said , “ Blessed be my son by the Lord .”
- **Judg 18:9** (—) *target: good*
  > Judg 18:9 They said , “ Arise , and let us go up against them, for we have seen the land , and behold, it is very good . And will you do nothing ? Do not be slow to go , to enter in and possess the land .
- **Judg 18:12** (—) *target: west*
  > Judg 18:12 and went up and encamped at Kiriath-jearim in Judah . On this account that place is called Mahaneh-dan to this day ; behold, it is west of Kiriath-jearim .
- **Judg 19:9** (—) *target: Behold*
  > Judg 19:9 And when the man and his concubine and his servant rose up to depart , his father-in-law , the girl’s father , said to him, “ Behold , now the day has waned toward evening . Please , spend the night . Behold , the day draws to its close . Lodge here and let your heart be merry , and tomorrow you shall arise early in the morning for your journey , and go home .”
- **Judg 19:16** (—) *target: behold*
  > Judg 19:16 And behold , an old man was coming from his work in the field at evening . The man was from the hill country of Ephraim , and he was sojourning in Gibeah . The men of the place were Benjaminites .
- **Judg 19:22** (—) *target: behold*
  > Judg 19:22 As they were making their hearts merry , behold , the men of the city , worthless fellows , surrounded the house , beating on the door . And they said to the old man , the master of the house , “ Bring out the man who came into your house , that we may know him .”
- **Judg 19:24** (—) *target: Behold*
  > Judg 19:24 Behold , here are my virgin daughter and his concubine . Let me bring them out now. Violate them and do with them what seems good to you, but against this man do not do this outrageous thing .”
- **Judg 19:27** (—) *target: behold*
  > Judg 19:27 And her master rose up in the morning , and when he opened the doors of the house and went out to go on his way , behold , there was his concubine lying at the door of the house , with her hands on the threshold .
- **Judg 20:7** (—) *target: Behold*
  > Judg 20:7 Behold , you people of Israel , all of you, give your advice and counsel here .”
- **Judg 20:40** (—) *target: behold*
  > Judg 20:40 But when the signal began to rise out of the city in a column of smoke , the Benjaminites looked behind them, and behold , the whole of the city went up in smoke to heaven .
- **Judg 21:8** (—) *target: behold*
  > Judg 21:8 And they said , “ What one is there of the tribes of Israel that did not come up to the Lord to Mizpah ?” And behold , no one had come to the camp from Jabesh-gilead , to the assembly .
- **Judg 21:9** (—) *target: behold*
  > Judg 21:9 For when the people were mustered , behold , not one of the inhabitants of Jabesh-gilead was there.
- **Judg 21:19** (—) *target: Behold*
  > Judg 21:19 So they said , “ Behold , there is the yearly feast of the Lord at Shiloh , which is north of Bethel , on the east of the highway that goes up from Bethel to Shechem , and south of Lebonah .”
- **Judg 21:21** (—) *target: watch*
  > Judg 21:21 and watch . If the daughters of Shiloh come out to dance in the dances , then come out of the vineyards and snatch each man his wife from the daughters of Shiloh , and go to the land of Benjamin .
- **Rut 1:15** (—) *target: See*
  > Rut 1:15 And she said , “ See , your sister-in-law has gone back to her people and to her gods ; return after your sister-in-law .”
- **Rut 2:4** (—) *target: behold*
  > Rut 2:4 And behold , Boaz came from Bethlehem . And he said to the reapers , “The Lord be with you!” And they answered , “The Lord bless you.”
- **Rut 3:2** (—) *target: See*
  > Rut 3:2 Is not Boaz our relative , with whose young women you were? See , he is winnowing barley tonight at the threshing floor .
- **Rut 3:8** (—) *target: behold*
  > Rut 3:8 At midnight the man was startled and turned over , and behold , a woman lay at his feet !
- **Rut 4:1** (—) *target: behold*
  > Rut 4:1 Now Boaz had gone up to the gate and sat down there . And behold , the redeemer , of whom Boaz had spoken , came by . So Boaz said , “Turn aside , friend ; sit down here .” And he turned aside and sat down .
- **1Sa 2:31** (—) *target: Behold*
  > 1Sa 2:31 Behold , the days are coming when I will cut off your strength and the strength of your father’s house , so that there will not be an old man in your house .
- **1Sa 3:11** (—) *target: Behold*
  > 1Sa 3:11 Then the Lord said to Samuel , “ Behold , I am about to do a thing in Israel at which the two ears of everyone who hears it will tingle .
- **1Sa 4:13** (—) *target: Eli*
  > 1Sa 4:13 When he arrived , Eli was sitting on his seat by the road watching , for his heart trembled for the ark of God . And when the man came into the city and told the news, all the city cried out .
- **1Sa 5:3** (—) *target: behold*
  > 1Sa 5:3 And when the people of Ashdod rose early the next day , behold , Dagon had fallen face downward on the ground before the ark of the Lord . So they took Dagon and put him back in his place .
- **Est 6:5** (—) *target: Haman*
  > Est 6:5 And the king’s young men told him, “ Haman is there, standing in the court .” And the king said , “Let him come in .”
- **Est 7:9** (—) *target: Moreover*
  > Est 7:9 Then Harbona , one of the eunuchs in attendance on the king , said , “ Moreover , the gallows that Haman has prepared for Mordecai , whose word saved the king , is standing at Haman’s house , fifty cubits high .”
- **Est 8:7** (—) *target: Behold*
  > Est 8:7 Then King Ahasuerus said to Queen Esther and to Mordecai the Jew , “ Behold , I have given Esther the house of Haman , and they have hanged him on the gallows , because he intended to lay hands on the Jews .
- **Job 1:12** (—) *target: Behold*
  > Job 1:12 And the Lord said to Satan , “ Behold , all that he has is in your hand . Only against him do not stretch out your hand .” So Satan went out from the presence of the Lord .
- **Job 1:19** (—) *target: behold*
  > Job 1:19 and behold , a great wind came across the wilderness and struck the four corners of the house , and it fell upon the young people , and they are dead , and I alone have escaped to tell you .”
- **Job 4:3** (—) *target: Behold*
  > Job 4:3 Behold , you have instructed many , and you have strengthened the weak hands .
- **Job 5:27** (—) *target: Behold*
  > Job 5:27 Behold , this we have searched out ; it is true . Hear , and know it for your good.”
- **Job 32:12** (—) *target: behold*
  > Job 32:12 I gave you my attention , and, behold , there was none among you who refuted Job or who answered his words .
- **Job 33:2** (—) *target: Behold*
  > Job 33:2 Behold , I open my mouth ; the tongue in my mouth speaks .
- **Job 40:15** (—) *target: Behold*
  > Job 40:15 “ Behold , Behemoth , which I made as I made you; he eats grass like an ox .
- **Job 40:16** (—) *target: Behold*
  > Job 40:16 Behold , his strength in his loins , and his power in the muscles of his belly .
- **Psa 37:36** (—) *target: behold*
  > Psa 37:36 But he passed away, and behold , he was no more ; though I sought him, he could not be found .
- **Psa 48:4** (—) *target: behold*
  > Psa 48:4 For behold , the kings assembled ; they came on together .
- **Psa 55:7** (—) *target: yes*
  > Psa 55:7 yes , I would wander far away ; I would lodge in the wilderness ; Selah
- **Psa 59:7** (—) *target: are*
  > Psa 59:7 There they are , bellowing with their mouths with swords in their lips — for “ Who ,” they think, “will hear us?”
- **Psa 73:12** (—) *target: Behold*
  > Psa 73:12 Behold , these are the wicked ; always at ease , they increase in riches .
- **Psa 87:4** (—) *target: behold*
  > Psa 87:4 Among those who know me I mention Rahab and Babylon ; behold , Philistia and Tyre , with Cush — “ This one was born there ,” they say.
- **Psa 92:9** (—) *target: behold*
  > Psa 92:9 For behold , your enemies , O Lord , for behold , your enemies shall perish ; all evildoers shall be scattered .
- **Psa 127:3** (—) *target: Behold*
  > Psa 127:3 Behold , children are a heritage from the Lord , the fruit of the womb a reward .
- **Psa 132:6** (—) *target: Behold*
  > Psa 132:6 Behold , we heard of it in Ephrathah ; we found it in the fields of Jaar .
- **Psa 134:1** (—) *target: Come*
  > A Song of Ascents . Psa 134:1 Come , bless the Lord , all you servants of the Lord , who stand by night in the house of the Lord !
- **Pro 24:31** (—) *target: behold*
  > Pro 24:31 and behold , it was all overgrown with thorns ; the ground was covered with nettles , and its stone wall was broken down .
- **Ecc 1:14** (—) *target: behold*
  > Ecc 1:14 I have seen everything that is done under the sun , and behold , all is vanity and a striving after wind .
- **Song 2:11** (—) *target: behold*
  > Song 2:11 for behold , the winter is past ; the rain is over and gone .
- **Song 3:7** (—) *target: Behold*
  > Song 3:7 Behold , it is the litter of Solomon ! Around it are sixty mighty men , some of the mighty men of Israel ,
- **Isa 3:1** (—) *target: behold*
  > Isa 3:1 For behold , the Lord God of hosts is taking away from Jerusalem and from Judah support and supply , all support of bread , and all support of water ;
- **Isa 5:26** (—) *target: behold*
  > Isa 5:26 He will raise a signal for nations far away , and whistle for them from the ends of the earth ; and behold , quickly , speedily they come !
- **Isa 5:30** (—) *target: behold*
  > Isa 5:30 They will growl over it on that day , like the growling of the sea . And if one looks to the land , behold , darkness and distress ; and the light is darkened by its clouds .
- **Isa 8:7** (—) *target: behold*
  > Isa 8:7 therefore , behold , the Lord is bringing up against them the waters of the River , mighty and many , the king of Assyria and all his glory . And it will rise over all its channels and go over all its banks ,
- **Isa 10:33** (—) *target: Behold*
  > Isa 10:33 Behold , the Lord God of hosts will lop the boughs with terrifying power; the great in height will be hewn down , and the lofty will be brought low .
- **Isa 13:9** (—) *target: Behold*
  > Isa 13:9 Behold , the day of the Lord comes , cruel , with wrath and fierce anger , to make the land a desolation and to destroy its sinners from it .
- **Isa 17:1** (—) *target: Behold*
  > Isa 17:1 An oracle concerning Damascus . Behold , Damascus will cease to be a city and will become a heap of ruins .
- **Isa 17:14** (—) *target: behold*
  > Isa 17:14 At evening time , behold , terror ! Before morning , they are no more ! This is the portion of those who loot us, and the lot of those who plunder us .
- **Isa 19:1** (—) *target: Behold*
  > Isa 19:1 An oracle concerning Egypt . Behold , the Lord is riding on a swift cloud and comes to Egypt ; and the idols of Egypt will tremble at his presence , and the heart of the Egyptians will melt within them .
- **Isa 21:9** (—) *target: behold*
  > Isa 21:9 And behold , here come riders , horsemen in pairs !” And he answered , “ Fallen , fallen is Babylon ; and all the carved images of her gods he has shattered to the ground .”
- **Isa 22:17** (—) *target: Behold*
  > Isa 22:17 Behold , the Lord will hurl you away violently , O you strong man . He will seize firm hold on you
- **Isa 24:1** (—) *target: Behold*
  > Isa 24:1 Behold , the Lord will empty the earth and make it desolate , and he will twist its surface and scatter its inhabitants .
- **Isa 26:21** (—) *target: behold*
  > Isa 26:21 For behold , the Lord is coming out from his place to punish the inhabitants of the earth for their iniquity , and the earth will disclose the blood shed on it, and will no more cover its slain .
- **Isa 28:2** (—) *target: Behold*
  > Isa 28:2 Behold , the Lord has one who is mighty and strong ; like a storm of hail , a destroying tempest , like a storm of mighty , overflowing waters , he casts down to the earth with his hand .
- **Isa 30:27** (—) *target: Behold*
  > Isa 30:27 Behold , the name of the Lord comes from afar , burning with his anger , and in thick rising smoke ; his lips are full of fury , and his tongue is like a devouring fire ;
- **Isa 34:5** (—) *target: behold*
  > Isa 34:5 For my sword has drunk its fill in the heavens ; behold , it descends for judgment upon Edom , upon the people I have devoted to destruction .
- **Isa 37:11** (—) *target: Behold*
  > Isa 37:11 Behold , you have heard what the kings of Assyria have done to all lands , devoting them to destruction . And shall you be delivered ?
- **Isa 37:36** (—) *target: behold*
  > Isa 37:36 And the angel of the Lord went out and struck down 185,000 in the camp of the Assyrians . And when people arose early in the morning , behold , these were all dead bodies .
- **Isa 39:6** (—) *target: Behold*
  > Isa 39:6 Behold , the days are coming , when all that is in your house , and that which your fathers have stored up till this day , shall be carried to Babylon . Nothing shall be left , says the Lord .
- **Isa 40:10** (—) *target: Behold*
  > Isa 40:10 Behold , the Lord God comes with might , and his arm rules for him; behold , his reward is with him, and his recompense before him.
- **Isa 41:15** (—) *target: Behold*
  > Isa 41:15 Behold , I make of you a threshing sledge , new , sharp , and having teeth ; you shall thresh the mountains and crush them, and you shall make the hills like chaff ;
- **Isa 41:27** (—) *target: Behold*
  > Isa 41:27 I was the first to say to Zion , “ Behold , here they are !” and I give to Jerusalem a herald of good news .
- **Isa 42:9** (—) *target: Behold*
  > Isa 42:9 Behold , the former things have come to pass , and new things I now declare ; before they spring forth I tell you of them.”
- **Isa 47:14** (—) *target: Behold*
  > Isa 47:14 Behold , they are like stubble ; the fire consumes them; they cannot deliver themselves from the power of the flame . No coal for warming oneself is this, no fire to sit before !
- **Isa 48:7** (—) *target: Behold*
  > Isa 48:7 They are created now , not long ago ; before today you have never heard of them, lest you should say , ‘ Behold , I knew them .’
- **Isa 49:12** (—) *target: Behold*
  > Isa 49:12 Behold , these shall come from afar , and behold , these from the north and from the west , and these from the land of Syene .”
- **Isa 49:22** (—) *target: Behold*
  > Isa 49:22 Thus says the Lord God : “ Behold , I will lift up my hand to the nations , and raise my signal to the peoples ; and they shall bring your sons in their arms , and your daughters shall be carried on their shoulders .
- **Isa 51:22** (—) *target: Behold*
  > Isa 51:22 Thus says your Lord , the Lord , your God who pleads the cause of his people : “ Behold , I have taken from your hand the cup of staggering ; the bowl of my wrath you shall drink no more ;
- **Isa 54:11** (—) *target: behold*
  > Isa 54:11 “O afflicted one , storm-tossed and not comforted , behold , I will set your stones in antimony , and lay your foundations with sapphires .
- **Isa 54:16** (—) *target: Behold*
  > Isa 54:16 Behold , I have created the smith who blows the fire of coals and produces a weapon for its purpose . I have also created the ravager to destroy ;
- **Isa 62:11** (—) *target: Behold*
  > Isa 62:11 Behold , the Lord has proclaimed to the end of the earth : Say to the daughter of Zion , “ Behold , your salvation comes ; behold , his reward is with him, and his recompense before him.”
- **Isa 65:6** (—) *target: Behold*
  > Isa 65:6 Behold , it is written before me: “ I will not keep silent , but I will repay ; I will indeed repay into their lap
- **Isa 66:15** (—) *target: behold*
  > Isa 66:15 “ For behold , the Lord will come in fire , and his chariots like the whirlwind , to render his anger in fury , and his rebuke with flames of fire .
- **Jer 1:9** (—) *target: Behold*
  > Jer 1:9 Then the Lord put out his hand and touched my mouth . And the Lord said to me, “ Behold , I have put my words in your mouth .
- **Jer 1:18** (—) *target: behold*
  > Jer 1:18 And I , behold , I make you this day a fortified city , an iron pillar , and bronze walls , against the whole land , against the kings of Judah , its officials , its priests , and the people of the land .
- **Jer 4:13** (—) *target: Behold*
  > Jer 4:13 Behold , he comes up like clouds ; his chariots like the whirlwind ; his horses are swifter than eagles — woe to us, for we are ruined !
- **Jer 4:16** (—) *target: coming*
  > Jer 4:16 Warn the nations that he is coming ; announce to Jerusalem , “ Besiegers come from a distant land ; they shout against the cities of Judah .
- **Jer 4:23** (—) *target: behold*
  > Jer 4:23 I looked on the earth , and behold , it was without form and void ; and to the heavens , and they had no light .
- **Hos 9:6** (—) *target: going*
  > Hos 9:6 For behold , they are going away from destruction ; but Egypt shall gather them; Memphis shall bury them. Nettles shall possess their precious things of silver ; thorns shall be in their tents .
- **Joe 3:1** (—) *target: behold*
  > Joe 3:1 “ For behold , in those days and at that time , when I restore the fortunes of Judah and Jerusalem ,
- **Amo 2:13** (—) *target: Behold*
  > Amo 2:13 “ Behold , I will press you down in your place, as a cart full of sheaves presses down.
- **Amo 4:2** (—) *target: behold*
  > Amo 4:2 The Lord God has sworn by his holiness that , behold , the days are coming upon you, when they shall take you away with hooks , even the last of you with fishhooks .
- **Amo 6:11** (—) *target: behold*
  > Amo 6:11 For behold , the Lord commands , and the great house shall be struck down into fragments , and the little house into bits .
- **Amo 7:1** (—) *target: behold*
  > Amo 7:1 This is what the Lord God showed me: behold , he was forming locusts when the latter growth was just beginning to sprout , and behold , it was the latter growth after the king’s mowings .
- **Amo 7:4** (—) *target: behold*
  > Amo 7:4 This is what the Lord God showed me: behold , the Lord God was calling for a judgment by fire , and it devoured the great deep and was eating up the land .
- **Amo 7:7** (—) *target: behold*
  > Amo 7:7 This is what he showed me: behold , the Lord was standing beside a wall built with a plumb line , with a plumb line in his hand .
- **Amo 8:1** (—) *target: behold*
  > Amo 8:1 This is what the Lord God showed me: behold , a basket of summer fruit .
- **Amo 9:8** (—) *target: Behold*
  > Amo 9:8 Behold , the eyes of the Lord God are upon the sinful kingdom , and I will destroy it from the surface of the ground , except that I will not utterly destroy the house of Jacob ,” declares the Lord .
- **Amo 9:9** (—) *target: behold*
  > Amo 9:9 “ For behold , I will command , and shake the house of Israel among all the nations as one shakes with a sieve , but no pebble shall fall to the earth .
- **Amo 9:13** (—) *target: Behold*
  > Amo 9:13 “ Behold , the days are coming ,” declares the Lord , “when the plowman shall overtake the reaper and the treader of grapes him who sows the seed ; the mountains shall drip sweet wine , and all the hills shall flow with it.
- **Obd 2** (—) *target: Behold*
  > Obd 2 Behold , I will make you small among the nations ; you shall be utterly despised .
- **Mic 1:3** (—) *target: behold*
  > Mic 1:3 For behold , the Lord is coming out of his place , and will come down and tread upon the high places of the earth .
- **Nah 3:13** (—) *target: Behold*
  > Nah 3:13 Behold , your troops are women in your midst . The gates of your land are wide open to your enemies ; fire has devoured your bars .
- **Hab 2:13** (—) *target: Behold*
  > Hab 2:13 Behold , is it not from the Lord of hosts that peoples labor merely for fire , and nations weary themselves for nothing ?
- **Zec 1:8** (—) *target: behold*
  > Zec 1:8 “I saw in the night , and behold , a man riding on a red horse ! He was standing among the myrtle trees in the glen , and behind him were red , sorrel , and white horses .
- **Zec 1:11** (—) *target: behold*
  > Zec 1:11 And they answered the angel of the Lord who was standing among the myrtle trees, and said , ‘We have patrolled the earth , and behold , all the earth remains at rest .’
- **Zec 1:18** (—) *target: behold*
  > Zec 1:18 And I lifted my eyes and saw , and behold , four horns !
- **Zec 2:1** (—) *target: behold*
  > Zec 2:1 And I lifted my eyes and saw , and behold , a man with a measuring line in his hand !
- **Zec 2:3** (—) *target: behold*
  > Zec 2:3 And behold , the angel who talked with me came forward , and another angel came forward to meet him
- **Zec 4:2** (—) *target: behold*
  > Zec 4:2 And he said to me, “ What do you see ?” I said , “I see , and behold , a lampstand all of gold , with a bowl on the top of it, and seven lamps on it, with seven lips on each of the lamps that are on the top of it.
- **Zec 5:1** (—) *target: behold*
  > Zec 5:1 Again I lifted my eyes and saw , and behold , a flying scroll !
- **Zec 5:7** (—) *target: behold*
  > Zec 5:7 And behold , the leaden cover was lifted , and there was a woman sitting in the basket !
- **Zec 5:9** (—) *target: behold*
  > Zec 5:9 Then I lifted my eyes and saw , and behold , two women coming forward ! The wind was in their wings . They had wings like the wings of a stork , and they lifted up the basket between earth and heaven .
- **Zec 6:1** (—) *target: behold*
  > Zec 6:1 Again I lifted my eyes and saw , and behold , four chariots came out from between two mountains . And the mountains were mountains of bronze .
- **Zec 6:12** (—) *target: Behold*
  > Zec 6:12 And say to him, ‘ Thus says the Lord of hosts , “ Behold , the man whose name is the Branch : for he shall branch out from his place, and he shall build the temple of the Lord .
- **Zec 9:4** (—) *target: behold*
  > Zec 9:4 But behold , the Lord will strip her of her possessions and strike down her power on the sea , and she shall be devoured by fire .
- **Zec 11:6** (—) *target: Behold*
  > Zec 11:6 For I will no longer have pity on the inhabitants of this land , declares the Lord . Behold , I will cause each of them to fall into the hand of his neighbor , and each into the hand of his king , and they shall crush the land , and I will deliver none from their hand .”
- **Zec 11:16** (—) *target: behold*
  > Zec 11:16 For behold , I am raising up in the land a shepherd who does not care for those being destroyed , or seek the young or heal the maimed or nourish the healthy , but devours the flesh of the fat ones , tearing off even their hoofs .
- **Zec 12:2** (—) *target: Behold*
  > Zec 12:2 “ Behold , I am about to make Jerusalem a cup of staggering to all the surrounding peoples . The siege of Jerusalem will also be against Judah .
- **Zec 14:1** (—) *target: Behold*
  > Zec 14:1 Behold , a day is coming for the Lord , when the spoil taken from you will be divided in your midst .
- **Mal 4:1** (—) *target: behold*
  > Mal 4:1 “ For behold , the day is coming , burning like an oven , when all the arrogant and all evildoers will be stubble . The day that is coming shall set them ablaze , says the Lord of hosts , so that it will leave them neither root nor branch .
- **Mal 4:5** (—) *target: Behold*
  > Mal 4:5 “ Behold , I will send you Elijah the prophet before the great and awesome day of the Lord comes .

### `H2011G` — 0/2 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (2 verses)

- **Jos 18:16** (—) *target: Hinnom*
  > Jos 18:16 Then the boundary goes down to the border of the mountain that overlooks the Valley of the Son of Hinnom , which is at the north end of the Valley of Rephaim . And it then goes down the Valley of Hinnom , south of the shoulder of the Jebusites , and downward to En-rogel .
- **Neh 11:30** (—) *target: Hinnom*
  > Neh 11:30 Zanoah , Adullam , and their villages , Lachish and its fields , and Azekah and its villages . So they encamped from Beersheba to the Valley of Hinnom .

### `H2011H` — 5/10 classified · 2 anchor verse(s)

**Group `5632-001`** (5 verses — anchors: 2Ch 33:6, Jer 7:31)

- **2Ch 33:6** 🔵 (✓) *target: Hinnom*
  > 2Ch 33:6 And he burned his sons as an offering in the Valley of the Son of Hinnom , and used fortune-telling and omens and sorcery , and dealt with mediums and with necromancers . He did much evil in the sight of the Lord , provoking him to anger .
- **Jer 7:31** 🔵 (✓) *target: Hinnom*
  > Jer 7:31 And they have built the high places of Topheth , which is in the Valley of the Son of Hinnom , to burn their sons and their daughters in the fire , which I did not command , nor did it come into my mind .
- **2Ki 23:10** (✓) *target: Hinnom*
  > 2Ki 23:10 And he defiled Topheth , which is in the Valley of the Son of Hinnom , that no one might burn his son or his daughter as an offering to Molech .
- **2Ch 28:3** (✓) *target: Hinnom*
  > 2Ch 28:3 and he made offerings in the Valley of the Son of Hinnom and burned his sons as an offering , according to the abominations of the nations whom the Lord drove out before the people of Israel .
- **Jer 32:35** (✓) *target: Hinnom*
  > Jer 32:35 They built the high places of Baal in the Valley of the Son of Hinnom , to offer up their sons and daughters to Molech , though I did not command them, nor did it enter into my mind , that they should do this abomination , to cause Judah to sin .

**Group `UNCLASSIFIED`** (5 verses)

- **Jos 15:8** (—) *target: Hinnom*
  > Jos 15:8 Then the boundary goes up by the Valley of the Son of Hinnom at the southern shoulder of the Jebusite ( that is, Jerusalem ). And the boundary goes up to the top of the mountain that lies over against the Valley of Hinnom , on the west , at the northern end of the Valley of Rephaim .
- **Jos 18:16** (—) *target: Hinnom*
  > Jos 18:16 Then the boundary goes down to the border of the mountain that overlooks the Valley of the Son of Hinnom , which is at the north end of the Valley of Rephaim . And it then goes down the Valley of Hinnom , south of the shoulder of the Jebusites , and downward to En-rogel .
- **Jer 7:32** (—) *target: Hinnom*
  > Jer 7:32 Therefore , behold , the days are coming , declares the Lord , when it will no more be called Topheth , or the Valley of the Son of Hinnom , but the Valley of Slaughter ; for they will bury in Topheth , because there is no room elsewhere .
- **Jer 19:2** (—) *target: Hinnom*
  > Jer 19:2 and go out to the Valley of the Son of Hinnom at the entry of the Potsherd Gate , and proclaim there the words that I tell you .
- **Jer 19:6** (—) *target: Hinnom*
  > Jer 19:6 therefore , behold , days are coming , declares the Lord , when this place shall no more be called Topheth , or the Valley of the Son of Hinnom , but the Valley of Slaughter .

### `H3681` — 0/2 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (2 verses)

- **Num 4:6** (—) *target: covering*
  > Num 4:6 Then they shall put on it a covering of goatskin and spread on top of that a cloth all of blue , and shall put in its poles .
- **Num 4:14** (—) *target: covering*
  > Num 4:14 And they shall put on it all the utensils of the altar, which are used for the service there, the fire pans , the forks , the shovels , and the basins , all the utensils of the altar ; and they shall spread on it a covering of goatskin , and shall put in its poles .

### `H3682` — 6/8 classified · 3 anchor verse(s)

**Group `929-001`** (1 verse — anchors: Gen 20:16)

- **Gen 20:16** 🔵 (✓) *target: innocence*
  > Gen 20:16 To Sarah he said , “Behold, I have given your brother a thousand pieces of silver . It is a sign of your innocence in the eyes of all who are with you , and before everyone you are vindicated .”

**Group `929-002`** (3 verses — anchors: Job 26:6)

- **Job 26:6** 🔵 (✓) *target: covering*
  > Job 26:6 Sheol is naked before God, and Abaddon has no covering .
- **Job 24:7** (✓) *target: covering*
  > Job 24:7 They lie all night naked , without clothing , and have no covering in the cold .
- **Job 31:19** (✓) *target: covering*
  > Job 31:19 if I have seen anyone perish for lack of clothing , or the needy without covering ,

**Group `929-003`** (2 verses — anchors: Exo 22:27)

- **Exo 22:27** 🔵 (✓) *target: covering*
  > Exo 22:27 for that is his only covering , and it is his cloak for his body ; in what else shall he sleep ? And if he cries to me, I will hear , for I am compassionate .
- **Isa 50:3** (✓) *target: covering*
  > Isa 50:3 I clothe the heavens with blackness and make sackcloth their covering .”

**Group `UNCLASSIFIED`** (2 verses)

- **Exo 21:10** (—) *target: clothing*
  > Exo 21:10 If he takes another wife to himself, he shall not diminish her food , her clothing , or her marital rights .
- **Deu 22:12** (—) *target: garment*
  > Deu 22:12 “You shall make yourself tassels on the four corners of the garment with which you cover yourself .

### `H4372` — 0/12 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (12 verses)

- **Gen 8:13** (—) *target: covering*
  > Gen 8:13 In the six hundred and first year , in the first month, the first day of the month , the waters were dried from off the earth . And Noah removed the covering of the ark and looked , and behold , the face of the ground was dry .
- **Exo 26:14** (—) *target: covering*
  > Exo 26:14 And you shall make for the tent a covering of tanned rams ’ skins and a covering of goatskins on top .
- **Exo 35:11** (—) *target: covering*
  > Exo 35:11 the tabernacle , its tent and its covering , its hooks and its frames , its bars , its pillars , and its bases ;
- **Exo 36:19** (—) *target: covering*
  > Exo 36:19 And he made for the tent a covering of tanned rams ’ skins and goatskins .
- **Exo 39:34** (—) *target: covering*
  > Exo 39:34 the covering of tanned rams ’ skins and goatskins , and the veil of the screen ;
- **Exo 40:19** (—) *target: covering*
  > Exo 40:19 And he spread the tent over the tabernacle and put the covering of the tent over it, as the Lord had commanded Moses .
- **Num 3:25** (—) *target: covering*
  > Num 3:25 And the guard duty of the sons of Gershon in the tent of meeting involved the tabernacle , the tent with its covering , the screen for the entrance of the tent of meeting ,
- **Num 4:8** (—) *target: covering*
  > Num 4:8 Then they shall spread over them a cloth of scarlet and cover the same with a covering of goatskin , and shall put in its poles .
- **Num 4:10** (—) *target: covering*
  > Num 4:10 And they shall put it with all its utensils in a covering of goatskin and put it on the carrying frame .
- **Num 4:11** (—) *target: covering*
  > Num 4:11 And over the golden altar they shall spread a cloth of blue and cover it with a covering of goatskin , and shall put in its poles .
- **Num 4:12** (—) *target: covering*
  > Num 4:12 And they shall take all the vessels of the service that are used in the sanctuary and put them in a cloth of blue and cover them with a covering of goatskin and put them on the carrying frame .
- **Num 4:25** (—) *target: its covering*
  > Num 4:25 they shall carry the curtains of the tabernacle and the tent of meeting with its covering and the covering of goatskin that is on top of it and the screen for the entrance of the tent of meeting

### `H4374` — 1/4 classified · 1 anchor verse(s)

**Group `5627-001`** (1 verse — anchors: Isa 14:11)

- **Isa 14:11** 🔵 (✓) *target: covers*
  > Isa 14:11 Your pomp is brought down to Sheol , the sound of your harps ; maggots are laid as a bed beneath you, and worms are your covers .

**Group `UNCLASSIFIED`** (3 verses)

- **Lev 9:19** (—) *target: covers*
  > Lev 9:19 But the fat pieces of the ox and of the ram , the fat tail and that which covers the entrails and the kidneys and the long lobe of the liver —
- **Isa 23:18** (—) *target: clothing*
  > Isa 23:18 Her merchandise and her wages will be holy to the Lord . It will not be stored or hoarded , but her merchandise will supply abundant food and fine clothing for those who dwell before the Lord .
- **Eze 27:7** (—) *target: awning*
  > Eze 27:7 Of fine embroidered linen from Egypt was your sail , serving as your banner ; blue and purple from the coasts of Elishah was your awning .

### `H4518` — 0/4 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (4 verses)

- **Exo 25:29** (—) *target: bowls*
  > Exo 25:29 And you shall make its plates and dishes for incense, and its flagons and bowls with which to pour drink offerings ; you shall make them of pure gold .
- **Exo 37:16** (—) *target: bowls*
  > Exo 37:16 And he made the vessels of pure gold that were to be on the table , its plates and dishes for incense, and its bowls and flagons with which to pour drink offerings .
- **Num 4:7** (—) *target: bowls*
  > Num 4:7 And over the table of the bread of the Presence they shall spread a cloth of blue and put on it the plates , the dishes for incense , the bowls , and the flagons for the drink offering ; the regular showbread also shall be on it .
- **Jer 52:19** (—) *target: drink offerings*
  > Jer 52:19 also the small bowls and the fire pans and the basins and the pots and the lampstands and the dishes for incense and the bowls for drink offerings . What was of gold the captain of the guard took away as gold , and what was of silver , as silver .

### `H4974` — 3/4 classified · 1 anchor verse(s)

**Group `5641-001`** (3 verses — anchors: Psa 38:3)

- **Psa 38:3** 🔵 (✓) *target: soundness*
  > Psa 38:3 There is no soundness in my flesh because of your indignation ; there is no health in my bones because of my sin .
- **Psa 38:7** (✓) *target: soundness*
  > Psa 38:7 For my sides are filled with burning , and there is no soundness in my flesh .
- **Isa 1:6** (✓) *target: soundness*
  > Isa 1:6 From the sole of the foot even to the head , there is no soundness in it, but bruises and sores and raw wounds ; they are not pressed out or bound up or softened with oil .

**Group `UNCLASSIFIED`** (1 verse)

- **Judg 20:48** (—) *target: men*
  > Judg 20:48 And the men of Israel turned back against the people of Benjamin and struck them with the edge of the sword , the city , men and beasts and all that they found . And all the towns that they found they set on fire .

### `H5355A` — 39/40 classified · 6 anchor verse(s)

**Group `5621-001`** (18 verses — anchors: Exo 23:7, 2Sa 3:28)

- **Exo 23:7** 🔵 (✓) *target: innocent*
  > Exo 23:7 Keep far from a false charge , and do not kill the innocent and righteous , for I will not acquit the wicked .
- **2Sa 3:28** 🔵 (✓) *target: guiltless*
  > 2Sa 3:28 Afterward , when David heard of it, he said , “ I and my kingdom are forever guiltless before the Lord for the blood of Abner the son of Ner .
- **Exo 21:28** (✓) *target: liable*
  > Exo 21:28 “ When an ox gores a man or a woman to death , the ox shall be stoned , and its flesh shall not be eaten , but the owner of the ox shall not be liable .
- **1Sa 19:5** (✓) *target: innocent*
  > 1Sa 19:5 For he took his life in his hand and he struck down the Philistine , and the Lord worked a great salvation for all Israel . You saw it, and rejoiced . Why then will you sin against innocent blood by killing David without cause ?”
- **2Sa 14:9** (✓) *target: guiltless*
  > 2Sa 14:9 And the woman of Tekoa said to the king , “ On me be the guilt , my lord the king , and on my father’s house ; let the king and his throne be guiltless .”
- **Job 4:7** (✓) *target: innocent*
  > Job 4:7 “ Remember : who that was innocent ever perished ? Or where were the upright cut off ?
- **Job 9:23** (✓) *target: innocent*
  > Job 9:23 When disaster brings sudden death , he mocks at the calamity of the innocent .
- **Job 17:8** (✓) *target: innocent*
  > Job 17:8 The upright are appalled at this , and the innocent stirs himself up against the godless .
- **Job 22:19** (✓) *target: innocent one*
  > Job 22:19 The righteous see it and are glad ; the innocent one mocks at them ,
- **Job 22:30** (✓) *target: innocent*
  > Job 22:30 He delivers even the one who is not innocent , who will be delivered through the cleanness of your hands .”
- **Job 27:17** (✓) *target: innocent*
  > Job 27:17 he may pile it up , but the righteous will wear it, and the innocent will divide the silver .
- **Psa 10:8** (✓) *target: innocent*
  > Psa 10:8 He sits in ambush in the villages ; in hiding places he murders the innocent . His eyes stealthily watch for the helpless ;
- **Psa 15:5** (✓) *target: innocent*
  > Psa 15:5 who does not put out his money at interest and does not take a bribe against the innocent . He who does these things shall never be moved .
- **Psa 24:4** (✓) *target: clean*
  > Psa 24:4 He who has clean hands and a pure heart , who does not lift up his soul to what is false and does not swear deceitfully .
- **Psa 94:21** (✓) *target: innocent*
  > Psa 94:21 They band together against the life of the righteous and condemn the innocent to death .
- **Pro 1:11** (✓) *target: innocent*
  > Pro 1:11 If they say , “ Come with us, let us lie in wait for blood ; let us ambush the innocent without reason ;
- **Pro 6:17** (✓) *target: innocent*
  > Pro 6:17 haughty eyes , a lying tongue , and hands that shed innocent blood ,
- **Isa 59:7** (✓) *target: innocent*
  > Isa 59:7 Their feet run to evil , and they are swift to shed innocent blood ; their thoughts are thoughts of iniquity ; desolation and destruction are in their highways .

**Group `5621-002`** (14 verses — anchors: Deu 27:25, Jer 22:17)

- **Deu 27:25** 🔵 (✓) *target: innocent*
  > Deu 27:25 “‘ Cursed be anyone who takes a bribe to shed innocent blood .’ And all the people shall say , ‘ Amen .’
- **Jer 22:17** 🔵 (✓) *target: innocent*
  > Jer 22:17 But you have eyes and heart only for your dishonest gain , for shedding innocent blood , and for practicing oppression and violence .”
- **Deu 19:10** (✓) *target: innocent*
  > Deu 19:10 lest innocent blood be shed in your land that the Lord your God is giving you for an inheritance , and so the guilt of bloodshed be upon you.
- **Deu 19:13** (✓) *target: innocent*
  > Deu 19:13 Your eye shall not pity him , but you shall purge the guilt of innocent blood from Israel , so that it may be well with you .
- **Deu 21:8** (✓) *target: innocent*
  > Deu 21:8 Accept atonement , O Lord , for your people Israel , whom you have redeemed , and do not set the guilt of innocent blood in the midst of your people Israel , so that their blood guilt be atoned for.’
- **Deu 21:9** (✓) *target: innocent*
  > Deu 21:9 So you shall purge the guilt of innocent blood from your midst , when you do what is right in the sight of the Lord .
- **2Ki 21:16** (✓) *target: innocent*
  > 2Ki 21:16 Moreover , Manasseh shed very much innocent blood , till he had filled Jerusalem from one end to another , besides the sin that he made Judah to sin so that they did what was evil in the sight of the Lord .
- **2Ki 24:4** (✓) *target: innocent*
  > 2Ki 24:4 and also for the innocent blood that he had shed . For he filled Jerusalem with innocent blood , and the Lord would not pardon .
- **Psa 106:38** (✓) *target: innocent*
  > Psa 106:38 they poured out innocent blood , the blood of their sons and daughters , whom they sacrificed to the idols of Canaan , and the land was polluted with blood .
- **Jer 2:34** (✓) *target: guiltless*
  > Jer 2:34 Also on your skirts is found the lifeblood of the guiltless poor ; you did not find them breaking in . Yet in spite of all these things
- **Jer 7:6** (✓) *target: innocent*
  > Jer 7:6 if you do not oppress the sojourner , the fatherless , or the widow , or shed innocent blood in this place , and if you do not go after other gods to your own harm ,
- **Jer 19:4** (✓) *target: innocents*
  > Jer 19:4 Because the people have forsaken me and have profaned this place by making offerings in it to other gods whom neither they nor their fathers nor the kings of Judah have known ; and because they have filled this place with the blood of innocents ,
- **Jer 22:3** (✓) *target: innocent*
  > Jer 22:3 Thus says the Lord : Do justice and righteousness , and deliver from the hand of the oppressor him who has been robbed . And do no wrong or violence to the resident alien , the fatherless , and the widow , nor shed innocent blood in this place .
- **Jer 26:15** (✓) *target: innocent*
  > Jer 26:15 Only know for certain that if you put me to death , you will bring innocent blood upon yourselves and upon this city and its inhabitants , for in truth the Lord sent me to you to speak all these words in your ears .”

**Group `5621-003`** (7 verses — anchors: Gen 24:41, Jos 2:19)

- **Gen 24:41** 🔵 (✓) *target: free*
  > Gen 24:41 Then you will be free from my oath , when you come to my clan . And if they will not give her to you, you will be free from my oath .’
- **Jos 2:19** 🔵 (✓) *target: guiltless*
  > Jos 2:19 Then if anyone goes out of the doors of your house into the street , his blood shall be on his own head , and we shall be guiltless . But if a hand is laid on anyone who is with you in the house , his blood shall be on our head .
- **Gen 44:10** (✓) *target: innocent*
  > Gen 44:10 He said , “ Let it be as you say : he who is found with it shall be my servant , and the rest of you shall be innocent .”
- **Num 32:22** (✓) *target: free of obligation*
  > Num 32:22 and the land is subdued before the Lord ; then after that you shall return and be free of obligation to the Lord and to Israel , and this land shall be your possession before the Lord .
- **Deu 24:5** (✓) *target: free*
  > Deu 24:5 “When a man is newly married , he shall not go out with the army or be liable for any other public duty . He shall be free at home one year to be happy with his wife whom he has taken .
- **Jos 2:17** (✓) *target: guiltless*
  > Jos 2:17 The men said to her, “We will be guiltless with respect to this oath of yours that you have made us swear .
- **Jos 2:20** (✓) *target: guiltless*
  > Jos 2:20 But if you tell this business of ours, then we shall be guiltless with respect to your oath that you have made us swear .”

**Group `UNCLASSIFIED`** (1 verse)

- **1Ki 15:22** (—) *target: exempt*
  > 1Ki 15:22 Then King Asa made a proclamation to all Judah , none was exempt , and they carried away the stones of Ramah and its timber , with which Baasha had been building , and with them King Asa built Geba of Benjamin and Mizpah .

### `H5355B` — 39/40 classified · 6 anchor verse(s)

**Group `5624-001`** (18 verses — anchors: Exo 23:7, 2Sa 3:28)

- **Exo 23:7** 🔵 (✓) *target: innocent*
  > Exo 23:7 Keep far from a false charge , and do not kill the innocent and righteous , for I will not acquit the wicked .
- **2Sa 3:28** 🔵 (✓) *target: guiltless*
  > 2Sa 3:28 Afterward , when David heard of it, he said , “ I and my kingdom are forever guiltless before the Lord for the blood of Abner the son of Ner .
- **Exo 21:28** (✓) *target: liable*
  > Exo 21:28 “ When an ox gores a man or a woman to death , the ox shall be stoned , and its flesh shall not be eaten , but the owner of the ox shall not be liable .
- **1Sa 19:5** (✓) *target: innocent*
  > 1Sa 19:5 For he took his life in his hand and he struck down the Philistine , and the Lord worked a great salvation for all Israel . You saw it, and rejoiced . Why then will you sin against innocent blood by killing David without cause ?”
- **2Sa 14:9** (✓) *target: guiltless*
  > 2Sa 14:9 And the woman of Tekoa said to the king , “ On me be the guilt , my lord the king , and on my father’s house ; let the king and his throne be guiltless .”
- **Job 4:7** (✓) *target: innocent*
  > Job 4:7 “ Remember : who that was innocent ever perished ? Or where were the upright cut off ?
- **Job 9:23** (✓) *target: innocent*
  > Job 9:23 When disaster brings sudden death , he mocks at the calamity of the innocent .
- **Job 17:8** (✓) *target: innocent*
  > Job 17:8 The upright are appalled at this , and the innocent stirs himself up against the godless .
- **Job 22:19** (✓) *target: innocent one*
  > Job 22:19 The righteous see it and are glad ; the innocent one mocks at them ,
- **Job 22:30** (✓) *target: innocent*
  > Job 22:30 He delivers even the one who is not innocent , who will be delivered through the cleanness of your hands .”
- **Job 27:17** (✓) *target: innocent*
  > Job 27:17 he may pile it up , but the righteous will wear it, and the innocent will divide the silver .
- **Psa 10:8** (✓) *target: innocent*
  > Psa 10:8 He sits in ambush in the villages ; in hiding places he murders the innocent . His eyes stealthily watch for the helpless ;
- **Psa 15:5** (✓) *target: innocent*
  > Psa 15:5 who does not put out his money at interest and does not take a bribe against the innocent . He who does these things shall never be moved .
- **Psa 24:4** (✓) *target: clean*
  > Psa 24:4 He who has clean hands and a pure heart , who does not lift up his soul to what is false and does not swear deceitfully .
- **Psa 94:21** (✓) *target: innocent*
  > Psa 94:21 They band together against the life of the righteous and condemn the innocent to death .
- **Pro 1:11** (✓) *target: innocent*
  > Pro 1:11 If they say , “ Come with us, let us lie in wait for blood ; let us ambush the innocent without reason ;
- **Pro 6:17** (✓) *target: innocent*
  > Pro 6:17 haughty eyes , a lying tongue , and hands that shed innocent blood ,
- **Isa 59:7** (✓) *target: innocent*
  > Isa 59:7 Their feet run to evil , and they are swift to shed innocent blood ; their thoughts are thoughts of iniquity ; desolation and destruction are in their highways .

**Group `5624-002`** (14 verses — anchors: Deu 27:25, Jer 22:17)

- **Deu 27:25** 🔵 (✓) *target: innocent*
  > Deu 27:25 “‘ Cursed be anyone who takes a bribe to shed innocent blood .’ And all the people shall say , ‘ Amen .’
- **Jer 22:17** 🔵 (✓) *target: innocent*
  > Jer 22:17 But you have eyes and heart only for your dishonest gain , for shedding innocent blood , and for practicing oppression and violence .”
- **Deu 19:10** (✓) *target: innocent*
  > Deu 19:10 lest innocent blood be shed in your land that the Lord your God is giving you for an inheritance , and so the guilt of bloodshed be upon you.
- **Deu 19:13** (✓) *target: innocent*
  > Deu 19:13 Your eye shall not pity him , but you shall purge the guilt of innocent blood from Israel , so that it may be well with you .
- **Deu 21:8** (✓) *target: innocent*
  > Deu 21:8 Accept atonement , O Lord , for your people Israel , whom you have redeemed , and do not set the guilt of innocent blood in the midst of your people Israel , so that their blood guilt be atoned for.’
- **Deu 21:9** (✓) *target: innocent*
  > Deu 21:9 So you shall purge the guilt of innocent blood from your midst , when you do what is right in the sight of the Lord .
- **2Ki 21:16** (✓) *target: innocent*
  > 2Ki 21:16 Moreover , Manasseh shed very much innocent blood , till he had filled Jerusalem from one end to another , besides the sin that he made Judah to sin so that they did what was evil in the sight of the Lord .
- **2Ki 24:4** (✓) *target: innocent*
  > 2Ki 24:4 and also for the innocent blood that he had shed . For he filled Jerusalem with innocent blood , and the Lord would not pardon .
- **Psa 106:38** (✓) *target: innocent*
  > Psa 106:38 they poured out innocent blood , the blood of their sons and daughters , whom they sacrificed to the idols of Canaan , and the land was polluted with blood .
- **Jer 2:34** (✓) *target: guiltless*
  > Jer 2:34 Also on your skirts is found the lifeblood of the guiltless poor ; you did not find them breaking in . Yet in spite of all these things
- **Jer 7:6** (✓) *target: innocent*
  > Jer 7:6 if you do not oppress the sojourner , the fatherless , or the widow , or shed innocent blood in this place , and if you do not go after other gods to your own harm ,
- **Jer 19:4** (✓) *target: innocents*
  > Jer 19:4 Because the people have forsaken me and have profaned this place by making offerings in it to other gods whom neither they nor their fathers nor the kings of Judah have known ; and because they have filled this place with the blood of innocents ,
- **Jer 22:3** (✓) *target: innocent*
  > Jer 22:3 Thus says the Lord : Do justice and righteousness , and deliver from the hand of the oppressor him who has been robbed . And do no wrong or violence to the resident alien , the fatherless , and the widow , nor shed innocent blood in this place .
- **Jer 26:15** (✓) *target: innocent*
  > Jer 26:15 Only know for certain that if you put me to death , you will bring innocent blood upon yourselves and upon this city and its inhabitants , for in truth the Lord sent me to you to speak all these words in your ears .”

**Group `5624-003`** (7 verses — anchors: Gen 24:41, Jos 2:19)

- **Gen 24:41** 🔵 (✓) *target: free*
  > Gen 24:41 Then you will be free from my oath , when you come to my clan . And if they will not give her to you, you will be free from my oath .’
- **Jos 2:19** 🔵 (✓) *target: guiltless*
  > Jos 2:19 Then if anyone goes out of the doors of your house into the street , his blood shall be on his own head , and we shall be guiltless . But if a hand is laid on anyone who is with you in the house , his blood shall be on our head .
- **Gen 44:10** (✓) *target: innocent*
  > Gen 44:10 He said , “ Let it be as you say : he who is found with it shall be my servant , and the rest of you shall be innocent .”
- **Num 32:22** (✓) *target: free of obligation*
  > Num 32:22 and the land is subdued before the Lord ; then after that you shall return and be free of obligation to the Lord and to Israel , and this land shall be your possession before the Lord .
- **Deu 24:5** (✓) *target: free*
  > Deu 24:5 “When a man is newly married , he shall not go out with the army or be liable for any other public duty . He shall be free at home one year to be happy with his wife whom he has taken .
- **Jos 2:17** (✓) *target: guiltless*
  > Jos 2:17 The men said to her, “We will be guiltless with respect to this oath of yours that you have made us swear .
- **Jos 2:20** (✓) *target: guiltless*
  > Jos 2:20 But if you tell this business of ours, then we shall be guiltless with respect to your oath that you have made us swear .”

**Group `UNCLASSIFIED`** (1 verse)

- **1Ki 15:22** (—) *target: exempt*
  > 1Ki 15:22 Then King Asa made a proclamation to all Judah , none was exempt , and they carried away the stones of Ramah and its timber , with which Baasha had been building , and with them King Asa built Geba of Benjamin and Mizpah .

### `H5356A` — 4/4 classified · 2 anchor verse(s)

**Group `928-001`** (4 verses — anchors: Gen 20:5, Psa 73:13)

- **Gen 20:5** 🔵 (✓) *target: innocence*
  > Gen 20:5 Did he not himself say to me, ‘ She is my sister ’? And she herself said , ‘He is my brother .’ In the integrity of my heart and the innocence of my hands I have done this .”
- **Psa 73:13** 🔵 (✓) *target: innocence*
  > Psa 73:13 All in vain have I kept my heart clean and washed my hands in innocence .
- **Psa 26:6** (✓) *target: innocence*
  > Psa 26:6 I wash my hands in innocence and go around your altar , O Lord ,
- **Hos 8:5** (✓) *target: innocence*
  > Hos 8:5 I have spurned your calf , O Samaria . My anger burns against them. How long will they be incapable of innocence ?

### `H5356B` — 4/4 classified · 2 anchor verse(s)

**Group `5620-001`** (4 verses — anchors: Gen 20:5, Psa 73:13)

- **Gen 20:5** 🔵 (✓) *target: innocence*
  > Gen 20:5 Did he not himself say to me, ‘ She is my sister ’? And she herself said , ‘He is my brother .’ In the integrity of my heart and the innocence of my hands I have done this .”
- **Psa 73:13** 🔵 (✓) *target: innocence*
  > Psa 73:13 All in vain have I kept my heart clean and washed my hands in innocence .
- **Psa 26:6** (✓) *target: innocence*
  > Psa 26:6 I wash my hands in innocence and go around your altar , O Lord ,
- **Hos 8:5** (✓) *target: innocence*
  > Hos 8:5 I have spurned your calf , O Samaria . My anger burns against them. How long will they be incapable of innocence ?

### `H8535` — 13/16 classified · 4 anchor verse(s)

**Group `5638-001`** (11 verses — anchors: Job 1:1, Psa 37:37)

- **Job 1:1** 🔵 (✓) *target: blameless*
  > Job 1:1 There was a man in the land of Uz whose name was Job , and that man was blameless and upright , one who feared God and turned away from evil .
- **Psa 37:37** 🔵 (✓) *target: blameless*
  > Psa 37:37 Mark the blameless and behold the upright , for there is a future for the man of peace .
- **Gen 25:27** (✓) *target: quiet*
  > Gen 25:27 When the boys grew up, Esau was a skillful hunter , a man of the field , while Jacob was a quiet man , dwelling in tents .
- **Job 1:8** (✓) *target: blameless*
  > Job 1:8 And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and turns away from evil ?”
- **Job 2:3** (✓) *target: blameless*
  > Job 2:3 And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and turns away from evil ? He still holds fast his integrity , although you incited me against him to destroy him without reason .”
- **Job 8:20** (✓) *target: blameless*
  > Job 8:20 “ Behold , God will not reject a blameless man, nor take the hand of evildoers .
- **Job 9:20** (✓) *target: he would*
  > Job 9:20 Though I am in the right, my own mouth would condemn me; though I am blameless, he would prove me perverse .
- **Job 9:21** (✓) *target: blameless*
  > Job 9:21 I am blameless ; I regard not myself ; I loathe my life .
- **Job 9:22** (✓) *target: blameless*
  > Job 9:22 It is all one ; therefore I say , ‘ He destroys both the blameless and the wicked .’
- **Psa 64:4** (✓) *target: blameless*
  > Psa 64:4 shooting from ambush at the blameless , shooting at him suddenly and without fear .
- **Pro 29:10** (✓) *target: blameless*
  > Pro 29:10 Bloodthirsty men hate one who is blameless and seek the life of the upright .

**Group `5638-002`** (2 verses — anchors: Song 5:2, Song 6:9)

- **Song 5:2** 🔵 (✓) *target: perfect one*
  > Song 5:2 I slept , but my heart was awake . A sound ! My beloved is knocking . “ Open to me, my sister , my love , my dove , my perfect one , for my head is wet with dew , my locks with the drops of the night .”
- **Song 6:9** 🔵 (✓) *target: perfect one*
  > Song 6:9 My dove , my perfect one , is the only one , the only one of her mother , pure to her who bore her. The young women saw her and called her blessed ; the queens and concubines also, and they praised her .

**Group `UNCLASSIFIED`** (3 verses)

- **Exo 26:24** (—) *target: top*
  > Exo 26:24 they shall be separate beneath , but joined at the top , at the first ring . Thus shall it be with both of them; they shall form the two corners .
- **Exo 36:29** (—) *target: joined*
  > Exo 36:29 And they were separate beneath but joined at the top , at the first ring . He made two of them this way for the two corners .
- **Jer 6:29** (—) *target: consumed*
  > Jer 6:29 The bellows blow fiercely ; the lead is consumed by the fire ; in vain the refining goes on , for the wicked are not removed .

### `H8537` — 21/23 classified · 2 anchor verse(s)

**Group `931-001`** (21 verses — anchors: Gen 20:5, Psa 26:1)

- **Gen 20:5** 🔵 (✓) *target: integrity*
  > Gen 20:5 Did he not himself say to me, ‘ She is my sister ’? And she herself said , ‘He is my brother .’ In the integrity of my heart and the innocence of my hands I have done this .”
- **Psa 26:1** 🔵 (✓) *target: integrity*
  > Of David . Psa 26:1 Vindicate me, O Lord , for I have walked in my integrity , and I have trusted in the Lord without wavering .
- **Gen 20:6** (✓) *target: integrity*
  > Gen 20:6 Then God said to him in the dream , “ Yes , I know that you have done this in the integrity of your heart , and it was I who kept you from sinning against me. Therefore I did not let you touch her .
- **2Sa 15:11** (✓) *target: innocence*
  > 2Sa 15:11 With Absalom went two hundred men from Jerusalem who were invited guests, and they went in their innocence and knew nothing .
- **1Ki 9:4** (✓) *target: integrity*
  > 1Ki 9:4 And as for you , if you will walk before me, as David your father walked , with integrity of heart and uprightness , doing according to all that I have commanded you, and keeping my statutes and my rules ,
- **1Ki 22:34** (✓) *target: random*
  > 1Ki 22:34 But a certain man drew his bow at random and struck the king of Israel between the scale armor and the breastplate . Therefore he said to the driver of his chariot , “ Turn around and carry me out of the battle , for I am wounded .”
- **2Ch 18:33** (✓) *target: random*
  > 2Ch 18:33 But a certain man drew his bow at random and struck the king of Israel between the scale armor and the breastplate . Therefore he said to the driver of his chariot , “ Turn around and carry me out of the battle , for I am wounded .”
- **Job 4:6** (✓) *target: integrity*
  > Job 4:6 Is not your fear of God your confidence , and the integrity of your ways your hope ?
- **Psa 7:8** (✓) *target: integrity*
  > Psa 7:8 The Lord judges the peoples ; judge me, O Lord , according to my righteousness and according to the integrity that is in me .
- **Psa 25:21** (✓) *target: integrity*
  > Psa 25:21 May integrity and uprightness preserve me, for I wait for you ^ .
- **Psa 26:11** (✓) *target: integrity*
  > Psa 26:11 But as for me , I shall walk in my integrity ; redeem me, and be gracious to me .
- **Psa 41:12** (✓) *target: integrity*
  > Psa 41:12 But you have upheld me because of my integrity , and set me in your presence forever .
- **Psa 78:72** (✓) *target: upright*
  > Psa 78:72 With upright heart he shepherded them and guided them with his skillful hand .
- **Psa 101:2** (✓) *target: integrity*
  > Psa 101:2 I will ponder the way that is blameless . Oh when will you come to me? I will walk with integrity of heart within my house ;
- **Pro 2:7** (✓) *target: integrity*
  > Pro 2:7 he stores up sound wisdom for the upright ; he is a shield to those who walk in integrity ,
- **Pro 10:9** (✓) *target: integrity*
  > Pro 10:9 Whoever walks in integrity walks securely , but he who makes his ways crooked will be found out .
- **Pro 10:29** (✓) *target: blameless*
  > Pro 10:29 The way of the Lord is a stronghold to the blameless , but destruction to evildoers .
- **Pro 13:6** (✓) *target: blameless*
  > Pro 13:6 Righteousness guards him whose way is blameless , but sin overthrows the wicked .
- **Pro 19:1** (✓) *target: integrity*
  > Pro 19:1 Better is a poor person who walks in his integrity than one who is crooked in speech and is a fool .
- **Pro 20:7** (✓) *target: integrity*
  > Pro 20:7 The righteous who walks in his integrity — blessed are his children after him !
- **Pro 28:6** (✓) *target: integrity*
  > Pro 28:6 Better is a poor man who walks in his integrity than a rich man who is crooked in his ways .

**Group `UNCLASSIFIED`** (2 verses)

- **Job 21:23** (—) *target: full*
  > Job 21:23 One dies in his full vigor , being wholly at ease and secure ,
- **Isa 47:9** (—) *target: full measure*
  > Isa 47:9 These two things shall come to you in a moment , in one day ; the loss of children and widowhood shall come upon you in full measure , in spite of your many sorceries and the great power of your enchantments .

### `H8549H` — 27/27 classified · 2 anchor verse(s)

**Group `5637-001`** (27 verses — anchors: Gen 17:1, Psa 15:2)

- **Gen 17:1** 🔵 (✓) *target: blameless*
  > Gen 17:1 When Abram was ninety-nine years old the Lord appeared to Abram and said to him, “ I am God Almighty ; walk before me, and be blameless ,
- **Psa 15:2** 🔵 (✓) *target: blamelessly*
  > Psa 15:2 He who walks blamelessly and does what is right and speaks truth in his heart ;
- **Gen 6:9** (✓) *target: blameless*
  > Gen 6:9 These are the generations of Noah . Noah was a righteous man , blameless in his generation . Noah walked with God .
- **Deu 18:13** (✓) *target: blameless*
  > Deu 18:13 You shall be blameless before the Lord your God ,
- **Jos 24:14** (✓) *target: sincerity*
  > Jos 24:14 “ Now therefore fear the Lord and serve him in sincerity and in faithfulness . Put away the gods that your fathers served beyond the River and in Egypt , and serve the Lord .
- **Judg 9:16** (✓) *target: integrity*
  > Judg 9:16 “ Now therefore, if you acted in good faith and integrity when you made Abimelech king , and if you have dealt well with Jerubbaal and his house and have done to him as his deeds deserved —
- **Judg 9:19** (✓) *target: integrity*
  > Judg 9:19 if you then have acted in good faith and integrity with Jerubbaal and with his house this day , then rejoice in Abimelech , and let him also rejoice in you .
- **2Sa 22:24** (✓) *target: blameless*
  > 2Sa 22:24 I was blameless before him, and I kept myself from guilt .
- **2Sa 22:26** (✓) *target: blameless*
  > 2Sa 22:26 “ With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;
- **2Sa 22:33** (✓) *target: blameless*
  > 2Sa 22:33 This God is my strong refuge and has made my way blameless .
- **Job 12:4** (✓) *target: blameless*
  > Job 12:4 I am a laughingstock to my friends ; I, who called to God and he answered me, a just and blameless man, am a laughingstock .
- **Psa 18:23** (✓) *target: blameless*
  > Psa 18:23 I was blameless before him, and I kept myself from my guilt .
- **Psa 18:25** (✓) *target: blameless*
  > Psa 18:25 With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;
- **Psa 18:32** (✓) *target: blameless*
  > Psa 18:32 the God who equipped me with strength and made my way blameless .
- **Psa 37:18** (✓) *target: blameless*
  > Psa 37:18 The Lord knows the days of the blameless , and their heritage will remain forever ;
- **Psa 84:11** (✓) *target: uprightly*
  > Psa 84:11 For the Lord God is a sun and shield ; the Lord bestows favor and honor . No good thing does he withhold from those who walk uprightly .
- **Psa 101:2** (✓) *target: blameless*
  > Psa 101:2 I will ponder the way that is blameless . Oh when will you come to me? I will walk with integrity of heart within my house ;
- **Psa 101:6** (✓) *target: blameless*
  > Psa 101:6 I will look with favor on the faithful in the land , that they may dwell with me; he who walks in the way that is blameless shall minister to me .
- **Psa 119:1** (✓) *target: blameless*
  > Aleph Psa 119:1 Blessed are those whose way is blameless , who walk in the law of the Lord !
- **Psa 119:80** (✓) *target: blameless*
  > Psa 119:80 May my heart be blameless in your statutes , that I may not be put to shame !
- **Pro 2:21** (✓) *target: integrity*
  > Pro 2:21 For the upright will inhabit the land , and those with integrity will remain in it ,
- **Pro 11:5** (✓) *target: blameless*
  > Pro 11:5 The righteousness of the blameless keeps his way straight , but the wicked falls by his own wickedness .
- **Pro 11:20** (✓) *target: blameless*
  > Pro 11:20 Those of crooked heart are an abomination to the Lord , but those of blameless ways are his delight .
- **Pro 28:10** (✓) *target: blameless*
  > Pro 28:10 Whoever misleads the upright into an evil way will fall into his own pit , but the blameless will have a goodly inheritance .
- **Pro 28:18** (✓) *target: integrity*
  > Pro 28:18 Whoever walks in integrity will be delivered , but he who is crooked in his ways will suddenly fall .
- **Eze 28:15** (✓) *target: blameless*
  > Eze 28:15 You were blameless in your ways from the day you were created , till unrighteousness was found in you .
- **Amo 5:10** (✓) *target: truth*
  > Amo 5:10 They hate him who reproves in the gate , and they abhor him who speaks the truth .

### `H8549I` — 0/6 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (6 verses)

- **Lev 3:9** (—) *target: whole*
  > Lev 3:9 Then from the sacrifice of the peace offering he shall offer as a food offering to the Lord its fat ; he shall remove the whole fat tail , cut off close to the backbone , and the fat that covers the entrails and all the fat that is on the entrails
- **Lev 23:15** (—) *target: full*
  > Lev 23:15 “You shall count seven full weeks from the day after the Sabbath , from the day that you brought the sheaf of the wave offering .
- **Lev 25:30** (—) *target: full*
  > Lev 25:30 If it is not redeemed within a full year , then the house in the walled city shall belong in perpetuity to the buyer , throughout his generations ; it shall not be released in the jubilee .
- **Jos 10:13** (—) *target: whole*
  > Jos 10:13 And the sun stood still , and the moon stopped , until the nation took vengeance on their enemies . Is this not written in the Book of Jashar ? The sun stopped in the midst of heaven and did not hurry to set for about a whole day .
- **Pro 1:12** (—) *target: whole*
  > Pro 1:12 like Sheol let us swallow them alive , and whole , like those who go down to the pit ;
- **Eze 15:5** (—) *target: whole*
  > Eze 15:5 Behold , when it was whole , it was used for nothing . How much less , when the fire has consumed it and it is charred , can it ever be used for anything !

### `H8549J` — 1/1 classified · 1 anchor verse(s)

**Group `5642-001`** (1 verse — anchors: 1Sa 14:41)

- **1Sa 14:41** 🔵 (✓) *target: Thummim*
  > 1Sa 14:41 Therefore Saul said , “O Lord God of Israel , why have you not answered your servant this day ? If this guilt is in me or in Jonathan my son , O Lord , God of Israel , give Urim . But if this guilt is in your people Israel , give Thummim .” And Jonathan and Saul were taken , but the people escaped .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**22 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H2005` | look! | `not_done` | 223 | 6 | 77 |
| `H2006A` | if | `not_done` | 11 | 0 | 0 |
| `H2006B` | therefore | `not_done` | 11 | 0 | 0 |
| `H2008` | here/thus | `not_done` | 41 | 1 | 4 |
| `H2009` | behold | `not_done` | 319 | 7 | 98 |
| `H2011G` | [Topheth of] Hinnom | `not_done` | 2 | 0 | 0 |
| `H2011H` | [Topheth of son of] Hinnom | `not_done` | 10 | 1 | 5 |
| `H3681` | covering | `not_done` | 2 | 0 | 0 |
| `H3682` | covering | `not_done` | 8 | 3 | 6 |
| `H4372` | covering | `not_done` | 12 | 0 | 0 |
| `H4374` | covering | `not_done` | 4 | 1 | 1 |
| `H4518` | bowl | `not_done` | 4 | 0 | 0 |
| `H4974` | soundness | `not_done` | 4 | 1 | 3 |
| `H5355A` | innocent | `not_done` | 40 | 3 | 39 |
| `H5355B` | innocent | `not_done` | 40 | 3 | 39 |
| `H5356A` | innocence | `not_done` | 4 | 1 | 4 |
| `H5356B` | bluntness | `not_done` | 4 | 1 | 4 |
| `H8535` | complete | `not_done` | 16 | 2 | 13 |
| `H8537` | integrity | `not_done` | 23 | 1 | 21 |
| `H8549H` | unblemished: blameless | `not_done` | 27 | 1 | 27 |
| `H8549I` | unblemished: complete | `not_done` | 6 | 0 | 0 |
| `H8549J` | unblemished: Thummim | `not_done` | 1 | 1 | 1 |

---

## L. Stage 2b Foundational Input — Second-Tier Catalogue (T0–T7)

**Active prompts: 189** across **56 components** in **8 tiers (T0–T7)**. Per `wa-sessionb-analysis-output [current]` §10, this is the operative question set for Stage 2b. Tier→component→prompt grouping IS the Stage 2b structure — Stage 2b walks the catalogue tier-by-tier, component-by-component, recording one Q&A entry per prompt.

### Tier summary

| Tier | Tier label | n components | n prompts |
|---|---|---:|---:|
| `T0` | T0 — Divine Image and Created Design | 4 | 12 |
| `T1` | T1 — Definition | 8 | 24 |
| `T2` | T2 — Constitutional Location and Boundaries | 10 | 31 |
| `T3` | T3 — The Inner Faculties | 11 | 33 |
| `T4` | T4 — Relational Interfaces | 6 | 24 |
| `T5` | T5 — Formative and Developmental Dimension | 7 | 21 |
| `T6` | T6 — Structural Relationships with Other Characteristics | 7 | 24 |
| `T7` | T7 — Evidential and Methodological Foundation | 3 | 20 |

### Catalogue (JSON, grouped by tier → component → prompts)

Format: JSON. Structure: as-is from `wa_obs_question_catalogue` filtered to `tier IS NOT NULL AND status='active'`. Apply to every word — universal across registries.

```json
{
  "total_prompts": 189,
  "total_components": 56,
  "total_tiers": 8,
  "catalogue_version": "v2-2026-04-29",
  "tiers": {
    "T0": {
      "tier_label": "T0 — Divine Image and Created Design",
      "components": {
        "T0.1": {
          "component_title": "Divine Nature Reflected",
          "prompts": [
            {
              "obs_id": 224,
              "question_code": "T0.1.1",
              "tier": "T0",
              "component_code": "T0.1",
              "component_title": "Divine Nature Reflected",
              "prompt_seq": 1,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "What does the verse evidence reveal about the nature or character of God that this characteristic reflects or images?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 225,
              "question_code": "T0.1.2",
              "tier": "T0",
              "component_code": "T0.1",
              "component_title": "Divine Nature Reflected",
              "prompt_seq": 2,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "Does Scripture explicitly attribute this characteristic to God — and if so, what does that attribution reveal about its significance in the human person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 226,
              "question_code": "T0.1.3",
              "tier": "T0",
              "component_code": "T0.1",
              "component_title": "Divine Nature Reflected",
              "prompt_seq": 3,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "Where Scripture is silent about God's possession of this characteristic, what does that silence suggest about the characteristic's place in the divine image?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T0.2": {
          "component_title": "Created Purpose",
          "prompts": [
            {
              "obs_id": 227,
              "question_code": "T0.2.1",
              "tier": "T0",
              "component_code": "T0.2",
              "component_title": "Created Purpose",
              "prompt_seq": 1,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "What does the verse evidence suggest about the purpose this characteristic serves in the human person as created — what does it equip the person to be, do, or become?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 228,
              "question_code": "T0.2.2",
              "tier": "T0",
              "component_code": "T0.2",
              "component_title": "Created Purpose",
              "prompt_seq": 2,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "Does the evidence indicate whether this characteristic is part of the original created design, a response to the fallen condition, or both?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 229,
              "question_code": "T0.2.3",
              "tier": "T0",
              "component_code": "T0.2",
              "component_title": "Created Purpose",
              "prompt_seq": 3,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "Is there evidence that this characteristic is oriented toward a future fullness — something the person is moving toward, not only what they currently are?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T0.3": {
          "component_title": "Image-Bearer Expression",
          "prompts": [
            {
              "obs_id": 230,
              "question_code": "T0.3.1",
              "tier": "T0",
              "component_code": "T0.3",
              "component_title": "Image-Bearer Expression",
              "prompt_seq": 1,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "In what way does this characteristic express the divine image in the human person — what aspect of being made in God's likeness does it instantiate?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 231,
              "question_code": "T0.3.2",
              "tier": "T0",
              "component_code": "T0.3",
              "component_title": "Image-Bearer Expression",
              "prompt_seq": 2,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "Does the evidence suggest that this characteristic is shared between God and the human person, or is it exclusively a creaturely analogue to something in God?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 232,
              "question_code": "T0.3.3",
              "tier": "T0",
              "component_code": "T0.3",
              "component_title": "Image-Bearer Expression",
              "prompt_seq": 3,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "What does the presence or absence of this characteristic in a person reveal about the condition of the divine image in that person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T0.4": {
          "component_title": "Typological Significance",
          "prompts": [
            {
              "obs_id": 233,
              "question_code": "T0.4.1",
              "tier": "T0",
              "component_code": "T0.4",
              "component_title": "Typological Significance",
              "prompt_seq": 1,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "Does Scripture use this characteristic typologically — deploying it to point toward or participate in a reality beyond the immediate (covenantal, eschatological, christological)?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 234,
              "question_code": "T0.4.2",
              "tier": "T0",
              "component_code": "T0.4",
              "component_title": "Typological Significance",
              "prompt_seq": 2,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "If typological use is present, what is the direction of the typology — does the human instance point toward the divine, or does the divine instance establish the pattern for the human?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 235,
              "question_code": "T0.4.3",
              "tier": "T0",
              "component_code": "T0.4",
              "component_title": "Typological Significance",
              "prompt_seq": 3,
              "section": "T0 — Divine Image and Created Design",
              "question_text": "If no typological use is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T1": {
      "tier_label": "T1 — Definition",
      "components": {
        "T1.1": {
          "component_title": "Name and Naming",
          "prompts": [
            {
              "obs_id": 236,
              "question_code": "T1.1.1",
              "tier": "T1",
              "component_code": "T1.1",
              "component_title": "Name and Naming",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What is this characteristic called in the programme — and what does the name itself signal about its essential nature?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 237,
              "question_code": "T1.1.2",
              "tier": "T1",
              "component_code": "T1.1",
              "component_title": "Name and Naming",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "What do the primary Hebrew and Greek terms reveal at the definitional level — before deeper lexical analysis begins?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 238,
              "question_code": "T1.1.3",
              "tier": "T1",
              "component_code": "T1.1",
              "component_title": "Name and Naming",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "Does the name carry directional, relational, or constitutional implications that orient the enquiry from the outset?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.2": {
          "component_title": "Kind",
          "prompts": [
            {
              "obs_id": 239,
              "question_code": "T1.2.1",
              "tier": "T1",
              "component_code": "T1.2",
              "component_title": "Kind",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What kind of inner-being phenomenon does this characteristic appear to be — an act, a disposition, a condition, a quality, or something else?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 240,
              "question_code": "T1.2.2",
              "tier": "T1",
              "component_code": "T1.2",
              "component_title": "Kind",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "Is this characteristic simple in structure or does it appear to have constituent elements at first encounter?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 241,
              "question_code": "T1.2.3",
              "tier": "T1",
              "component_code": "T1.2",
              "component_title": "Kind",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "What is the current best working description of this characteristic — encapsulating its constitutional location, the faculties it primarily engages, and its impact on the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.3": {
          "component_title": "Boundary",
          "prompts": [
            {
              "obs_id": 242,
              "question_code": "T1.3.1",
              "tier": "T1",
              "component_code": "T1.3",
              "component_title": "Boundary",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What is the structural opposite of this characteristic — the inner-being reality that stands against or excludes it?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 243,
              "question_code": "T1.3.2",
              "tier": "T1",
              "component_code": "T1.3",
              "component_title": "Boundary",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "What does this characteristic explicitly exclude or resist?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 244,
              "question_code": "T1.3.3",
              "tier": "T1",
              "component_code": "T1.3",
              "component_title": "Boundary",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "What is this characteristic not — where does it end and something else begin?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.4": {
          "component_title": "Modes of Operation",
          "prompts": [
            {
              "obs_id": 245,
              "question_code": "T1.4.1",
              "tier": "T1",
              "component_code": "T1.4",
              "component_title": "Modes of Operation",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "In what distinct ways does this characteristic operate within the inner person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 246,
              "question_code": "T1.4.2",
              "tier": "T1",
              "component_code": "T1.4",
              "component_title": "Modes of Operation",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "Does this characteristic operate differently depending on context, direction, or constitutional level?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 247,
              "question_code": "T1.4.3",
              "tier": "T1",
              "component_code": "T1.4",
              "component_title": "Modes of Operation",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "Does this characteristic have a communicative or speech-based mode of operation — and if so, how does it function?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.5": {
          "component_title": "Immediate Response",
          "prompts": [
            {
              "obs_id": 248,
              "question_code": "T1.5.1",
              "tier": "T1",
              "component_code": "T1.5",
              "component_title": "Immediate Response",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What is the first or most immediate inner-being response to receiving or encountering this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 249,
              "question_code": "T1.5.2",
              "tier": "T1",
              "component_code": "T1.5",
              "component_title": "Immediate Response",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "Is the immediate response consistent across the verse evidence, or does it vary?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 250,
              "question_code": "T1.5.3",
              "tier": "T1",
              "component_code": "T1.5",
              "component_title": "Immediate Response",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "Where the verse evidence is silent on immediate response, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.6": {
          "component_title": "Sustained Effect",
          "prompts": [
            {
              "obs_id": 251,
              "question_code": "T1.6.1",
              "tier": "T1",
              "component_code": "T1.6",
              "component_title": "Sustained Effect",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What does this characteristic produce in the inner being over time?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 252,
              "question_code": "T1.6.2",
              "tier": "T1",
              "component_code": "T1.6",
              "component_title": "Sustained Effect",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "What states, qualities, capacities, or orientations does sustained exposure to or possession of this characteristic establish?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 253,
              "question_code": "T1.6.3",
              "tier": "T1",
              "component_code": "T1.6",
              "component_title": "Sustained Effect",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "Does the sustained effect differ from the immediate response — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.7": {
          "component_title": "Conditions of Reception",
          "prompts": [
            {
              "obs_id": 254,
              "question_code": "T1.7.1",
              "tier": "T1",
              "component_code": "T1.7",
              "component_title": "Conditions of Reception",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What inner conditions or orientations enable genuine reception of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 255,
              "question_code": "T1.7.2",
              "tier": "T1",
              "component_code": "T1.7",
              "component_title": "Conditions of Reception",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "What inner conditions block, distort, or prevent reception?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 256,
              "question_code": "T1.7.3",
              "tier": "T1",
              "component_code": "T1.7",
              "component_title": "Conditions of Reception",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "What is the inner-being state of the person who encounters this characteristic but does not receive it?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T1.8": {
          "component_title": "Dimension Classification",
          "prompts": [
            {
              "obs_id": 257,
              "question_code": "T1.8.1",
              "tier": "T1",
              "component_code": "T1.8",
              "component_title": "Dimension Classification",
              "prompt_seq": 1,
              "section": "T1 — Definition",
              "question_text": "What is the primary inner-being dimension of this characteristic from the programme's dimension vocabulary?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 258,
              "question_code": "T1.8.2",
              "tier": "T1",
              "component_code": "T1.8",
              "component_title": "Dimension Classification",
              "prompt_seq": 2,
              "section": "T1 — Definition",
              "question_text": "What evidence from the verse evidence supports this classification?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 259,
              "question_code": "T1.8.3",
              "tier": "T1",
              "component_code": "T1.8",
              "component_title": "Dimension Classification",
              "prompt_seq": 3,
              "section": "T1 — Definition",
              "question_text": "Does this characteristic carry secondary dimensions — and if so, what are they, and do they compete with the primary classification?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T2": {
      "tier_label": "T2 — Constitutional Location and Boundaries",
      "components": {
        "T2.1": {
          "component_title": "Spirit-Level Location",
          "prompts": [
            {
              "obs_id": 260,
              "question_code": "T2.1.1",
              "tier": "T2",
              "component_code": "T2.1",
              "component_title": "Spirit-Level Location",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Is this characteristic explicitly located at the spirit level in the verse evidence?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 261,
              "question_code": "T2.1.2",
              "tier": "T2",
              "component_code": "T2.1",
              "component_title": "Spirit-Level Location",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does the evidence indicate that this characteristic originates in or is primarily a spirit-level phenomenon?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 262,
              "question_code": "T2.1.3",
              "tier": "T2",
              "component_code": "T2.1",
              "component_title": "Spirit-Level Location",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What does spirit-level location reveal about the nature and depth of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 263,
              "question_code": "T2.1.4",
              "tier": "T2",
              "component_code": "T2.1",
              "component_title": "Spirit-Level Location",
              "prompt_seq": 4,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If the evidence is silent on spirit-level location, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.10": {
          "component_title": "Constitutional Movement",
          "prompts": [
            {
              "obs_id": 288,
              "question_code": "T2.10.1",
              "tier": "T2",
              "component_code": "T2.10",
              "component_title": "Constitutional Movement",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does this characteristic move across constitutional levels — from spirit to soul, from soul to body, or across boundaries in other directions?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 289,
              "question_code": "T2.10.2",
              "tier": "T2",
              "component_code": "T2.10",
              "component_title": "Constitutional Movement",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What does the evidence reveal about the sequence or pattern of that movement?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 290,
              "question_code": "T2.10.3",
              "tier": "T2",
              "component_code": "T2.10",
              "component_title": "Constitutional Movement",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If no constitutional movement is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.2": {
          "component_title": "Soul-Level Location",
          "prompts": [
            {
              "obs_id": 264,
              "question_code": "T2.2.1",
              "tier": "T2",
              "component_code": "T2.2",
              "component_title": "Soul-Level Location",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Is this characteristic identified in the verse evidence as a soul-level phenomenon?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 265,
              "question_code": "T2.2.2",
              "tier": "T2",
              "component_code": "T2.2",
              "component_title": "Soul-Level Location",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What does soul-level location reveal about this characteristic's place in the innermost personal experience?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 266,
              "question_code": "T2.2.3",
              "tier": "T2",
              "component_code": "T2.2",
              "component_title": "Soul-Level Location",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If the evidence is silent on soul-level location, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.3": {
          "component_title": "Heart",
          "prompts": [
            {
              "obs_id": 267,
              "question_code": "T2.3.1",
              "tier": "T2",
              "component_code": "T2.3",
              "component_title": "Heart",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does the verse evidence locate this characteristic in the heart?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 268,
              "question_code": "T2.3.2",
              "tier": "T2",
              "component_code": "T2.3",
              "component_title": "Heart",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What does the heart-location reveal — what aspect of the heart's integrating function (knowing, willing, feeling, moral awareness) does this characteristic engage?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 269,
              "question_code": "T2.3.3",
              "tier": "T2",
              "component_code": "T2.3",
              "component_title": "Heart",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If the evidence is silent on heart-location, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.4": {
          "component_title": "Mind",
          "prompts": [
            {
              "obs_id": 270,
              "question_code": "T2.4.1",
              "tier": "T2",
              "component_code": "T2.4",
              "component_title": "Mind",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does the verse evidence locate this characteristic in the mind?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 271,
              "question_code": "T2.4.2",
              "tier": "T2",
              "component_code": "T2.4",
              "component_title": "Mind",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What does mind-location reveal — what aspect of the mind's function (thought, discernment, understanding) does this characteristic engage?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 272,
              "question_code": "T2.4.3",
              "tier": "T2",
              "component_code": "T2.4",
              "component_title": "Mind",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If the evidence is silent on mind-location, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.5": {
          "component_title": "Other Soul Subsets",
          "prompts": [
            {
              "obs_id": 273,
              "question_code": "T2.5.1",
              "tier": "T2",
              "component_code": "T2.5",
              "component_title": "Other Soul Subsets",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does the verse evidence surface any soul-level location beyond heart and mind for this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 274,
              "question_code": "T2.5.2",
              "tier": "T2",
              "component_code": "T2.5",
              "component_title": "Other Soul Subsets",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If so, what is that location, and what does it reveal?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 275,
              "question_code": "T2.5.3",
              "tier": "T2",
              "component_code": "T2.5",
              "component_title": "Other Soul Subsets",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If the evidence is silent, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.6": {
          "component_title": "Body — Significance",
          "prompts": [
            {
              "obs_id": 276,
              "question_code": "T2.6.1",
              "tier": "T2",
              "component_code": "T2.6",
              "component_title": "Body — Significance",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does the verse evidence link this characteristic to a specific body part?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 277,
              "question_code": "T2.6.2",
              "tier": "T2",
              "component_code": "T2.6",
              "component_title": "Body — Significance",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If so, what is Scripture doing by making that link — is it emphatic, functional, expressive, indicative, or mediating?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 278,
              "question_code": "T2.6.3",
              "tier": "T2",
              "component_code": "T2.6",
              "component_title": "Body — Significance",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If no body-part link is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.7": {
          "component_title": "Body — Direction",
          "prompts": [
            {
              "obs_id": 279,
              "question_code": "T2.7.1",
              "tier": "T2",
              "component_code": "T2.7",
              "component_title": "Body — Direction",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Where a body-characteristic link exists, which direction does it run — does the soul express through the body, does the body feed back to the soul, or does it run in both directions?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 280,
              "question_code": "T2.7.2",
              "tier": "T2",
              "component_code": "T2.7",
              "component_title": "Body — Direction",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What is the consequence of that directionality for understanding the characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 281,
              "question_code": "T2.7.3",
              "tier": "T2",
              "component_code": "T2.7",
              "component_title": "Body — Direction",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If no body-characteristic link is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.8": {
          "component_title": "Body — Deposit",
          "prompts": [
            {
              "obs_id": 282,
              "question_code": "T2.8.1",
              "tier": "T2",
              "component_code": "T2.8",
              "component_title": "Body — Deposit",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does sustained operation of this characteristic leave a constitutional deposit in the body or its design — including DNA or generational consequence?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 283,
              "question_code": "T2.8.2",
              "tier": "T2",
              "component_code": "T2.8",
              "component_title": "Body — Deposit",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What evidence supports or contradicts this?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 284,
              "question_code": "T2.8.3",
              "tier": "T2",
              "component_code": "T2.8",
              "component_title": "Body — Deposit",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "If the evidence is silent, note this explicitly. This finding feeds directly into T5.7.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T2.9": {
          "component_title": "Origin and Source",
          "prompts": [
            {
              "obs_id": 285,
              "question_code": "T2.9.1",
              "tier": "T2",
              "component_code": "T2.9",
              "component_title": "Origin and Source",
              "prompt_seq": 1,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Where does this characteristic originate constitutionally — is it generated from within the person, received from outside, bestowed by God, or carried generationally?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 286,
              "question_code": "T2.9.2",
              "tier": "T2",
              "component_code": "T2.9",
              "component_title": "Origin and Source",
              "prompt_seq": 2,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "What does the evidence reveal about whether the origin is singular or multiple?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 287,
              "question_code": "T2.9.3",
              "tier": "T2",
              "component_code": "T2.9",
              "component_title": "Origin and Source",
              "prompt_seq": 3,
              "section": "T2 — Constitutional Location and Boundaries",
              "question_text": "Does the origin of this characteristic change across different contexts evidenced in Scripture?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T3": {
      "tier_label": "T3 — The Inner Faculties",
      "components": {
        "T3.1": {
          "component_title": "Perception",
          "prompts": [
            {
              "obs_id": 291,
              "question_code": "T3.1.1",
              "tier": "T3",
              "component_code": "T3.1",
              "component_title": "Perception",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the perceptive faculty — the inner senses including hearing, sight, taste, touch, smell, and spiritual discernment — and if so, which inner sense and how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 292,
              "question_code": "T3.1.2",
              "tier": "T3",
              "component_code": "T3.1",
              "component_title": "Perception",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair the perceptive faculty in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 293,
              "question_code": "T3.1.3",
              "tier": "T3",
              "component_code": "T3.1",
              "component_title": "Perception",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with perception reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.10": {
          "component_title": "Conscientiousness",
          "prompts": [
            {
              "obs_id": 318,
              "question_code": "T3.10.1",
              "tier": "T3",
              "component_code": "T3.10",
              "component_title": "Conscientiousness",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 319,
              "question_code": "T3.10.2",
              "tier": "T3",
              "component_code": "T3.10",
              "component_title": "Conscientiousness",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair conscientiousness in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 320,
              "question_code": "T3.10.3",
              "tier": "T3",
              "component_code": "T3.10",
              "component_title": "Conscientiousness",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with conscientiousness reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.11": {
          "component_title": "Relational Capacity",
          "prompts": [
            {
              "obs_id": 321,
              "question_code": "T3.11.1",
              "tier": "T3",
              "component_code": "T3.11",
              "component_title": "Relational Capacity",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 322,
              "question_code": "T3.11.2",
              "tier": "T3",
              "component_code": "T3.11",
              "component_title": "Relational Capacity",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair relational capacity in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 323,
              "question_code": "T3.11.3",
              "tier": "T3",
              "component_code": "T3.11",
              "component_title": "Relational Capacity",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with relational capacity reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.2": {
          "component_title": "Cognition",
          "prompts": [
            {
              "obs_id": 294,
              "question_code": "T3.2.1",
              "tier": "T3",
              "component_code": "T3.2",
              "component_title": "Cognition",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 295,
              "question_code": "T3.2.2",
              "tier": "T3",
              "component_code": "T3.2",
              "component_title": "Cognition",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair cognition in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 296,
              "question_code": "T3.2.3",
              "tier": "T3",
              "component_code": "T3.2",
              "component_title": "Cognition",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with cognition reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.3": {
          "component_title": "Memory",
          "prompts": [
            {
              "obs_id": 297,
              "question_code": "T3.3.1",
              "tier": "T3",
              "component_code": "T3.3",
              "component_title": "Memory",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 298,
              "question_code": "T3.3.2",
              "tier": "T3",
              "component_code": "T3.3",
              "component_title": "Memory",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair memory in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 299,
              "question_code": "T3.3.3",
              "tier": "T3",
              "component_code": "T3.3",
              "component_title": "Memory",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with memory reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.4": {
          "component_title": "Affect",
          "prompts": [
            {
              "obs_id": 300,
              "question_code": "T3.4.1",
              "tier": "T3",
              "component_code": "T3.4",
              "component_title": "Affect",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the affective faculty — feeling and emotional experience — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 301,
              "question_code": "T3.4.2",
              "tier": "T3",
              "component_code": "T3.4",
              "component_title": "Affect",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair affect in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 302,
              "question_code": "T3.4.3",
              "tier": "T3",
              "component_code": "T3.4",
              "component_title": "Affect",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with affect reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.5": {
          "component_title": "Creativity",
          "prompts": [
            {
              "obs_id": 303,
              "question_code": "T3.5.1",
              "tier": "T3",
              "component_code": "T3.5",
              "component_title": "Creativity",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 304,
              "question_code": "T3.5.2",
              "tier": "T3",
              "component_code": "T3.5",
              "component_title": "Creativity",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair creativity in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 305,
              "question_code": "T3.5.3",
              "tier": "T3",
              "component_code": "T3.5",
              "component_title": "Creativity",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with creativity reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.6": {
          "component_title": "Volition",
          "prompts": [
            {
              "obs_id": 306,
              "question_code": "T3.6.1",
              "tier": "T3",
              "component_code": "T3.6",
              "component_title": "Volition",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the volitional faculty — the capacity to choose — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 307,
              "question_code": "T3.6.2",
              "tier": "T3",
              "component_code": "T3.6",
              "component_title": "Volition",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair volition in the person — including its three aspects: capacity, interaction with other characteristics, and the constraints under which it operates?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 308,
              "question_code": "T3.6.3",
              "tier": "T3",
              "component_code": "T3.6",
              "component_title": "Volition",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with volition reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.7": {
          "component_title": "Agency",
          "prompts": [
            {
              "obs_id": 309,
              "question_code": "T3.7.1",
              "tier": "T3",
              "component_code": "T3.7",
              "component_title": "Agency",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 310,
              "question_code": "T3.7.2",
              "tier": "T3",
              "component_code": "T3.7",
              "component_title": "Agency",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair agency in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 311,
              "question_code": "T3.7.3",
              "tier": "T3",
              "component_code": "T3.7",
              "component_title": "Agency",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with agency reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.8": {
          "component_title": "Moral Evaluation",
          "prompts": [
            {
              "obs_id": 312,
              "question_code": "T3.8.1",
              "tier": "T3",
              "component_code": "T3.8",
              "component_title": "Moral Evaluation",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the moral evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 313,
              "question_code": "T3.8.2",
              "tier": "T3",
              "component_code": "T3.8",
              "component_title": "Moral Evaluation",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair moral evaluation in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 314,
              "question_code": "T3.8.3",
              "tier": "T3",
              "component_code": "T3.8",
              "component_title": "Moral Evaluation",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with moral evaluation reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T3.9": {
          "component_title": "Conscience",
          "prompts": [
            {
              "obs_id": 315,
              "question_code": "T3.9.1",
              "tier": "T3",
              "component_code": "T3.9",
              "component_title": "Conscience",
              "prompt_seq": 1,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 316,
              "question_code": "T3.9.2",
              "tier": "T3",
              "component_code": "T3.9",
              "component_title": "Conscience",
              "prompt_seq": 2,
              "section": "T3 — The Inner Faculties",
              "question_text": "Does this characteristic enable, deepen, bypass, or impair conscience in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 317,
              "question_code": "T3.9.3",
              "tier": "T3",
              "component_code": "T3.9",
              "component_title": "Conscience",
              "prompt_seq": 3,
              "section": "T3 — The Inner Faculties",
              "question_text": "What does the pattern of engagement or non-engagement with conscience reveal about the nature of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T4": {
      "tier_label": "T4 — Relational Interfaces",
      "components": {
        "T4.1": {
          "component_title": "Divine Interface — God to Human",
          "prompts": [
            {
              "obs_id": 324,
              "question_code": "T4.1.1",
              "tier": "T4",
              "component_code": "T4.1",
              "component_title": "Divine Interface — God to Human",
              "prompt_seq": 1,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does the verse evidence show this characteristic operating from God toward the human person — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 325,
              "question_code": "T4.1.2",
              "tier": "T4",
              "component_code": "T4.1",
              "component_title": "Divine Interface — God to Human",
              "prompt_seq": 2,
              "section": "T4 — Relational Interfaces",
              "question_text": "What does the evidence reveal about the basis on which God extends this characteristic — is it conditional, unconditional, covenantal, or responsive?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 326,
              "question_code": "T4.1.3",
              "tier": "T4",
              "component_code": "T4.1",
              "component_title": "Divine Interface — God to Human",
              "prompt_seq": 3,
              "section": "T4 — Relational Interfaces",
              "question_text": "What does God's extension of this characteristic reveal about his disposition toward the human person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 327,
              "question_code": "T4.1.4",
              "tier": "T4",
              "component_code": "T4.1",
              "component_title": "Divine Interface — God to Human",
              "prompt_seq": 4,
              "section": "T4 — Relational Interfaces",
              "question_text": "If the evidence is silent on God-to-human operation, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T4.2": {
          "component_title": "Divine Interface — Human to God",
          "prompts": [
            {
              "obs_id": 328,
              "question_code": "T4.2.1",
              "tier": "T4",
              "component_code": "T4.2",
              "component_title": "Divine Interface — Human to God",
              "prompt_seq": 1,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does the verse evidence show this characteristic operating in the human person's movement toward God — in seeking, supplication, worship, or covenant — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 329,
              "question_code": "T4.2.2",
              "tier": "T4",
              "component_code": "T4.2",
              "component_title": "Divine Interface — Human to God",
              "prompt_seq": 2,
              "section": "T4 — Relational Interfaces",
              "question_text": "What does the evidence reveal about the inner posture required for this movement?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 330,
              "question_code": "T4.2.3",
              "tier": "T4",
              "component_code": "T4.2",
              "component_title": "Divine Interface — Human to God",
              "prompt_seq": 3,
              "section": "T4 — Relational Interfaces",
              "question_text": "What does the human-to-God direction of this characteristic reveal about the person's relationship with God?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 331,
              "question_code": "T4.2.4",
              "tier": "T4",
              "component_code": "T4.2",
              "component_title": "Divine Interface — Human to God",
              "prompt_seq": 4,
              "section": "T4 — Relational Interfaces",
              "question_text": "If the evidence is silent on human-to-God operation, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T4.3": {
          "component_title": "Human Interface — Giving",
          "prompts": [
            {
              "obs_id": 332,
              "question_code": "T4.3.1",
              "tier": "T4",
              "component_code": "T4.3",
              "component_title": "Human Interface — Giving",
              "prompt_seq": 1,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does the verse evidence show this characteristic being extended by one person toward another — and if so, how does it operate in that giving?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 333,
              "question_code": "T4.3.2",
              "tier": "T4",
              "component_code": "T4.3",
              "component_title": "Human Interface — Giving",
              "prompt_seq": 2,
              "section": "T4 — Relational Interfaces",
              "question_text": "What inner conditions or orientations in the giver enable genuine extension of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 334,
              "question_code": "T4.3.3",
              "tier": "T4",
              "component_code": "T4.3",
              "component_title": "Human Interface — Giving",
              "prompt_seq": 3,
              "section": "T4 — Relational Interfaces",
              "question_text": "What does the evidence reveal about what the person must have received or become before they can genuinely give this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 335,
              "question_code": "T4.3.4",
              "tier": "T4",
              "component_code": "T4.3",
              "component_title": "Human Interface — Giving",
              "prompt_seq": 4,
              "section": "T4 — Relational Interfaces",
              "question_text": "If the evidence is silent on the giving direction, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T4.4": {
          "component_title": "Human Interface — Receiving",
          "prompts": [
            {
              "obs_id": 336,
              "question_code": "T4.4.1",
              "tier": "T4",
              "component_code": "T4.4",
              "component_title": "Human Interface — Receiving",
              "prompt_seq": 1,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does the verse evidence show this characteristic being received by a person from another — and if so, how does it operate in that reception?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 337,
              "question_code": "T4.4.2",
              "tier": "T4",
              "component_code": "T4.4",
              "component_title": "Human Interface — Receiving",
              "prompt_seq": 2,
              "section": "T4 — Relational Interfaces",
              "question_text": "What inner conditions enable or block reception of this characteristic from another person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 338,
              "question_code": "T4.4.3",
              "tier": "T4",
              "component_code": "T4.4",
              "component_title": "Human Interface — Receiving",
              "prompt_seq": 3,
              "section": "T4 — Relational Interfaces",
              "question_text": "What is the inner-being state of the person who encounters this characteristic from another but does not receive it?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 339,
              "question_code": "T4.4.4",
              "tier": "T4",
              "component_code": "T4.4",
              "component_title": "Human Interface — Receiving",
              "prompt_seq": 4,
              "section": "T4 — Relational Interfaces",
              "question_text": "If the evidence is silent on the receiving direction, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T4.5": {
          "component_title": "Human Interface — Boundaries",
          "prompts": [
            {
              "obs_id": 340,
              "question_code": "T4.5.1",
              "tier": "T4",
              "component_code": "T4.5",
              "component_title": "Human Interface — Boundaries",
              "prompt_seq": 1,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does the evidence indicate whether this characteristic operates differently within existing relational bonds versus across relational distance or difference?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 341,
              "question_code": "T4.5.2",
              "tier": "T4",
              "component_code": "T4.5",
              "component_title": "Human Interface — Boundaries",
              "prompt_seq": 2,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does this characteristic operate within covenantal contexts only, or does it cross covenantal boundaries?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 342,
              "question_code": "T4.5.3",
              "tier": "T4",
              "component_code": "T4.5",
              "component_title": "Human Interface — Boundaries",
              "prompt_seq": 3,
              "section": "T4 — Relational Interfaces",
              "question_text": "What does the evidence reveal about the relational scope of this characteristic — who is included and who is not?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 343,
              "question_code": "T4.5.4",
              "tier": "T4",
              "component_code": "T4.5",
              "component_title": "Human Interface — Boundaries",
              "prompt_seq": 4,
              "section": "T4 — Relational Interfaces",
              "question_text": "If the evidence is silent on relational boundaries, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T4.6": {
          "component_title": "Spiritual Beings Interface",
          "prompts": [
            {
              "obs_id": 344,
              "question_code": "T4.6.1",
              "tier": "T4",
              "component_code": "T4.6",
              "component_title": "Spiritual Beings Interface",
              "prompt_seq": 1,
              "section": "T4 — Relational Interfaces",
              "question_text": "Does the verse evidence show this characteristic operating in relation to other spiritual beings — angelic or adversarial — and if so, how?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 345,
              "question_code": "T4.6.2",
              "tier": "T4",
              "component_code": "T4.6",
              "component_title": "Spiritual Beings Interface",
              "prompt_seq": 2,
              "section": "T4 — Relational Interfaces",
              "question_text": "Is this characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial spiritual powers?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 346,
              "question_code": "T4.6.3",
              "tier": "T4",
              "component_code": "T4.6",
              "component_title": "Spiritual Beings Interface",
              "prompt_seq": 3,
              "section": "T4 — Relational Interfaces",
              "question_text": "Is this characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 347,
              "question_code": "T4.6.4",
              "tier": "T4",
              "component_code": "T4.6",
              "component_title": "Spiritual Beings Interface",
              "prompt_seq": 4,
              "section": "T4 — Relational Interfaces",
              "question_text": "If the evidence is silent on the spiritual beings interface, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T5": {
      "tier_label": "T5 — Formative and Developmental Dimension",
      "components": {
        "T5.1": {
          "component_title": "Nature of Transformation",
          "prompts": [
            {
              "obs_id": 348,
              "question_code": "T5.1.1",
              "tier": "T5",
              "component_code": "T5.1",
              "component_title": "Nature of Transformation",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does this characteristic produce transformation in the person — and if so, does it change the person's condition, the person's orientation to their condition, or both?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 349,
              "question_code": "T5.1.2",
              "tier": "T5",
              "component_code": "T5.1",
              "component_title": "Nature of Transformation",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Is the transformation produced by this characteristic reversible or irreversible in the verse evidence?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 350,
              "question_code": "T5.1.3",
              "tier": "T5",
              "component_code": "T5.1",
              "component_title": "Nature of Transformation",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If the evidence is silent on transformation, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T5.2": {
          "component_title": "Sequence of Inner States",
          "prompts": [
            {
              "obs_id": 351,
              "question_code": "T5.2.1",
              "tier": "T5",
              "component_code": "T5.2",
              "component_title": "Sequence of Inner States",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does the verse evidence describe a sequence of inner states through which this characteristic moves the person — a before, during, and after?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 352,
              "question_code": "T5.2.2",
              "tier": "T5",
              "component_code": "T5.2",
              "component_title": "Sequence of Inner States",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "What are those states, and what does the sequence reveal about how this characteristic works?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 353,
              "question_code": "T5.2.3",
              "tier": "T5",
              "component_code": "T5.2",
              "component_title": "Sequence of Inner States",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If the evidence is silent on sequence, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T5.3": {
          "component_title": "Mechanism of Change",
          "prompts": [
            {
              "obs_id": 354,
              "question_code": "T5.3.1",
              "tier": "T5",
              "component_code": "T5.3",
              "component_title": "Mechanism of Change",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "What mechanism does this characteristic use to produce change in the person — discipline, encounter, gradual formation, sudden transformation, or something else?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 355,
              "question_code": "T5.3.2",
              "tier": "T5",
              "component_code": "T5.3",
              "component_title": "Mechanism of Change",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does the evidence distinguish between mechanisms in different contexts?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 356,
              "question_code": "T5.3.3",
              "tier": "T5",
              "component_code": "T5.3",
              "component_title": "Mechanism of Change",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If the evidence is silent on mechanism, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T5.4": {
          "component_title": "Suffering and Affliction",
          "prompts": [
            {
              "obs_id": 357,
              "question_code": "T5.4.1",
              "tier": "T5",
              "component_code": "T5.4",
              "component_title": "Suffering and Affliction",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does the verse evidence show this characteristic operating in relation to suffering or affliction — as a response to it, a product of it, or a context for it?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 358,
              "question_code": "T5.4.2",
              "tier": "T5",
              "component_code": "T5.4",
              "component_title": "Suffering and Affliction",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does suffering deepen, test, reveal, or produce this characteristic in the person?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 359,
              "question_code": "T5.4.3",
              "tier": "T5",
              "component_code": "T5.4",
              "component_title": "Suffering and Affliction",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If the evidence is silent on the relationship to suffering, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T5.5": {
          "component_title": "Formation and Sanctification",
          "prompts": [
            {
              "obs_id": 360,
              "question_code": "T5.5.1",
              "tier": "T5",
              "component_code": "T5.5",
              "component_title": "Formation and Sanctification",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does the verse evidence show this characteristic participating in the longer arc of character formation and sanctification — shaping the person over time toward greater likeness?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 361,
              "question_code": "T5.5.2",
              "tier": "T5",
              "component_code": "T5.5",
              "component_title": "Formation and Sanctification",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "What does the evidence reveal about the role of this characteristic in that longer arc?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 362,
              "question_code": "T5.5.3",
              "tier": "T5",
              "component_code": "T5.5",
              "component_title": "Formation and Sanctification",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If the evidence is silent on formation and sanctification, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T5.6": {
          "component_title": "Eschatological Trajectory",
          "prompts": [
            {
              "obs_id": 363,
              "question_code": "T5.6.1",
              "tier": "T5",
              "component_code": "T5.6",
              "component_title": "Eschatological Trajectory",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does the verse evidence point this characteristic toward an eschatological fullness — a future state toward which its present operation is oriented?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 364,
              "question_code": "T5.6.2",
              "tier": "T5",
              "component_code": "T5.6",
              "component_title": "Eschatological Trajectory",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "What does the present experience of this characteristic anticipate about its future fullness?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 365,
              "question_code": "T5.6.3",
              "tier": "T5",
              "component_code": "T5.6",
              "component_title": "Eschatological Trajectory",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If the evidence is silent on eschatological trajectory, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T5.7": {
          "component_title": "Deposit Consequence",
          "prompts": [
            {
              "obs_id": 366,
              "question_code": "T5.7.1",
              "tier": "T5",
              "component_code": "T5.7",
              "component_title": "Deposit Consequence",
              "prompt_seq": 1,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Where T2.8 has identified a constitutional deposit from sustained operation of this characteristic, what developmental consequence does that deposit produce over time?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 367,
              "question_code": "T5.7.2",
              "tier": "T5",
              "component_code": "T5.7",
              "component_title": "Deposit Consequence",
              "prompt_seq": 2,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "Does the evidence indicate generational consequence — a deposit carried forward beyond the individual?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 368,
              "question_code": "T5.7.3",
              "tier": "T5",
              "component_code": "T5.7",
              "component_title": "Deposit Consequence",
              "prompt_seq": 3,
              "section": "T5 — Formative and Developmental Dimension",
              "question_text": "If T2.8 found no deposit, note this explicitly and close T5.7.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T6": {
      "tier_label": "T6 — Structural Relationships with Other Characteristics",
      "components": {
        "T6.1": {
          "component_title": "Co-occurrence",
          "prompts": [
            {
              "obs_id": 369,
              "question_code": "T6.1.1",
              "tier": "T6",
              "component_code": "T6.1",
              "component_title": "Co-occurrence",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Which adjacent characteristics appear most frequently alongside this one in the verse evidence?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 370,
              "question_code": "T6.1.2",
              "tier": "T6",
              "component_code": "T6.1",
              "component_title": "Co-occurrence",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "What does the pattern of co-occurrence reveal about this characteristic's place in the inner-being landscape?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 371,
              "question_code": "T6.1.3",
              "tier": "T6",
              "component_code": "T6.1",
              "component_title": "Co-occurrence",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If no significant co-occurrence patterns emerge, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T6.2": {
          "component_title": "Sequential Relationships",
          "prompts": [
            {
              "obs_id": 372,
              "question_code": "T6.2.1",
              "tier": "T6",
              "component_code": "T6.2",
              "component_title": "Sequential Relationships",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Does the verse evidence show this characteristic consistently preceding, following, or accompanying another characteristic in a sequence?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 373,
              "question_code": "T6.2.2",
              "tier": "T6",
              "component_code": "T6.2",
              "component_title": "Sequential Relationships",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "What does the sequence reveal — is the relationship causal, developmental, or correlational?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 374,
              "question_code": "T6.2.3",
              "tier": "T6",
              "component_code": "T6.2",
              "component_title": "Sequential Relationships",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If no sequential pattern is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T6.3": {
          "component_title": "Causal and Constitutive Relationships",
          "prompts": [
            {
              "obs_id": 375,
              "question_code": "T6.3.1",
              "tier": "T6",
              "component_code": "T6.3",
              "component_title": "Causal and Constitutive Relationships",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Does this characteristic produce another characteristic in the verse evidence — and if so, which one, and by what mechanism?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 376,
              "question_code": "T6.3.2",
              "tier": "T6",
              "component_code": "T6.3",
              "component_title": "Causal and Constitutive Relationships",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Is this characteristic produced by another — and if so, which one?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 377,
              "question_code": "T6.3.3",
              "tier": "T6",
              "component_code": "T6.3",
              "component_title": "Causal and Constitutive Relationships",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Is this characteristic a constituent element of another, or does another characteristic constitute part of this one?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 378,
              "question_code": "T6.3.4",
              "tier": "T6",
              "component_code": "T6.3",
              "component_title": "Causal and Constitutive Relationships",
              "prompt_seq": 4,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If no causal or constitutive relationship is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T6.4": {
          "component_title": "Vocabulary and Root Sharing",
          "prompts": [
            {
              "obs_id": 379,
              "question_code": "T6.4.1",
              "tier": "T6",
              "component_code": "T6.4",
              "component_title": "Vocabulary and Root Sharing",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Does this characteristic share vocabulary terms with other characteristics in the programme?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 380,
              "question_code": "T6.4.2",
              "tier": "T6",
              "component_code": "T6.4",
              "component_title": "Vocabulary and Root Sharing",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Does vocabulary sharing extend to root-level architecture — a shared root that generates terms across two or more characteristics?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 381,
              "question_code": "T6.4.3",
              "tier": "T6",
              "component_code": "T6.4",
              "component_title": "Vocabulary and Root Sharing",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "What does vocabulary sharing reveal about the conceptual relationship between characteristics?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 382,
              "question_code": "T6.4.4",
              "tier": "T6",
              "component_code": "T6.4",
              "component_title": "Vocabulary and Root Sharing",
              "prompt_seq": 4,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If no significant vocabulary sharing is evidenced, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T6.5": {
          "component_title": "Distinctions",
          "prompts": [
            {
              "obs_id": 383,
              "question_code": "T6.5.1",
              "tier": "T6",
              "component_code": "T6.5",
              "component_title": "Distinctions",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Which adjacent characteristic most closely resembles this one — and what precisely distinguishes them?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 384,
              "question_code": "T6.5.2",
              "tier": "T6",
              "component_code": "T6.5",
              "component_title": "Distinctions",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Where the evidence shows apparent overlap, what is the precise boundary?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 385,
              "question_code": "T6.5.3",
              "tier": "T6",
              "component_code": "T6.5",
              "component_title": "Distinctions",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Is the distinction between this characteristic and its nearest neighbour one of degree, kind, direction, or constitutional level?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 386,
              "question_code": "T6.5.4",
              "tier": "T6",
              "component_code": "T6.5",
              "component_title": "Distinctions",
              "prompt_seq": 4,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If no significant distinction work is required, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T6.6": {
          "component_title": "Shared Verse Anchors",
          "prompts": [
            {
              "obs_id": 387,
              "question_code": "T6.6.1",
              "tier": "T6",
              "component_code": "T6.6",
              "component_title": "Shared Verse Anchors",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "Does any verse in this characteristic's evidence base also function as a primary anchor in another characteristic's study?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 388,
              "question_code": "T6.6.2",
              "tier": "T6",
              "component_code": "T6.6",
              "component_title": "Shared Verse Anchors",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "What does the shared anchor reveal about the relationship between the two characteristics?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 389,
              "question_code": "T6.6.3",
              "tier": "T6",
              "component_code": "T6.6",
              "component_title": "Shared Verse Anchors",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If no shared verse anchors are identified, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T6.7": {
          "component_title": "Dimensional Sharing",
          "prompts": [
            {
              "obs_id": 390,
              "question_code": "T6.7.1",
              "tier": "T6",
              "component_code": "T6.7",
              "component_title": "Dimensional Sharing",
              "prompt_seq": 1,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "How many of this characteristic's confirmed analytical dimensions are shared with another characteristic in the programme?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 391,
              "question_code": "T6.7.2",
              "tier": "T6",
              "component_code": "T6.7",
              "component_title": "Dimensional Sharing",
              "prompt_seq": 2,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "What does the pattern of dimensional sharing reveal about the relationship between this characteristic and those it shares dimensions with?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 392,
              "question_code": "T6.7.3",
              "tier": "T6",
              "component_code": "T6.7",
              "component_title": "Dimensional Sharing",
              "prompt_seq": 3,
              "section": "T6 — Structural Relationships with Other Characteristics",
              "question_text": "If dimensional sharing data is not yet available, note this explicitly.",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    },
    "T7": {
      "tier_label": "T7 — Evidential and Methodological Foundation",
      "components": {
        "T7.1": {
          "component_title": "Lexical and Semantic Analysis",
          "prompts": [
            {
              "obs_id": 393,
              "question_code": "T7.1.1",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 1,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What are the primary Hebrew and Greek terms for this characteristic — and what do their root meanings reveal?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 394,
              "question_code": "T7.1.2",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 2,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What is the grammatical range of the primary term (noun, verb, adjective, participle) — and what does that range reveal about how the characteristic operates?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 395,
              "question_code": "T7.1.3",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 3,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What is the semantic range of the primary term — across what breadth of meaning does it operate?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 396,
              "question_code": "T7.1.4",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 4,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Does the vocabulary include terms that distinguish distinct aspects of this characteristic — disposition versus act, received versus given, condition versus quality?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 397,
              "question_code": "T7.1.5",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 5,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Does the vocabulary include a term for the structural opposite or absence of this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 398,
              "question_code": "T7.1.6",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 6,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Does the vocabulary include a person-type term — a term for the one who habitually possesses or exercises this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 399,
              "question_code": "T7.1.7",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 7,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Does the vocabulary include a supplication or seeking term — a term for the act of seeking this characteristic from another?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 400,
              "question_code": "T7.1.8",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 8,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What does the LXX use of the vocabulary reveal about continuity or development of this characteristic across the Testaments?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 401,
              "question_code": "T7.1.9",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 9,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Is there a term newly coined in the NT period for this characteristic — and if so, what does that coinage reveal?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 402,
              "question_code": "T7.1.10",
              "tier": "T7",
              "component_code": "T7.1",
              "component_title": "Lexical and Semantic Analysis",
              "prompt_seq": 10,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What does the full vocabulary arc reveal about this characteristic's complete semantic range?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T7.2": {
          "component_title": "Verse and Literary Interpretation",
          "prompts": [
            {
              "obs_id": 403,
              "question_code": "T7.2.1",
              "tier": "T7",
              "component_code": "T7.2",
              "component_title": "Verse and Literary Interpretation",
              "prompt_seq": 1,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What is the function of this characteristic's primary term within its primary verse — what role does it play in the sentence and argument?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 404,
              "question_code": "T7.2.2",
              "tier": "T7",
              "component_code": "T7.2",
              "component_title": "Verse and Literary Interpretation",
              "prompt_seq": 2,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic) — and what does that form require for responsible interpretation?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 405,
              "question_code": "T7.2.3",
              "tier": "T7",
              "component_code": "T7.2",
              "component_title": "Verse and Literary Interpretation",
              "prompt_seq": 3,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What is the logical structure of key arguments in the verse evidence — what are the premises and conclusions?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 406,
              "question_code": "T7.2.4",
              "tier": "T7",
              "component_code": "T7.2",
              "component_title": "Verse and Literary Interpretation",
              "prompt_seq": 4,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological) — and what does that setting reveal?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 407,
              "question_code": "T7.2.5",
              "tier": "T7",
              "component_code": "T7.2",
              "component_title": "Verse and Literary Interpretation",
              "prompt_seq": 5,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Does any verse function as the primary anchor for this characteristic — the verse that most fully and directly expresses its essential character?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 408,
              "question_code": "T7.2.6",
              "tier": "T7",
              "component_code": "T7.2",
              "component_title": "Verse and Literary Interpretation",
              "prompt_seq": 6,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "What does the primary anchor verse reveal that no other verse reveals?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        },
        "T7.3": {
          "component_title": "Human Science Frameworks",
          "prompts": [
            {
              "obs_id": 409,
              "question_code": "T7.3.1",
              "tier": "T7",
              "component_code": "T7.3",
              "component_title": "Human Science Frameworks",
              "prompt_seq": 1,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Which human science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) is most useful as an interpretive lens for this characteristic?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 410,
              "question_code": "T7.3.2",
              "tier": "T7",
              "component_code": "T7.3",
              "component_title": "Human Science Frameworks",
              "prompt_seq": 2,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Where the human science framework illuminates the verse evidence — making a finding more coherent or complete — what does it reveal?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 411,
              "question_code": "T7.3.3",
              "tier": "T7",
              "component_code": "T7.3",
              "component_title": "Human Science Frameworks",
              "prompt_seq": 3,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Where the verse evidence and the human science framework diverge, what does the divergence reveal?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            },
            {
              "obs_id": 412,
              "question_code": "T7.3.4",
              "tier": "T7",
              "component_code": "T7.3",
              "component_title": "Human Science Frameworks",
              "prompt_seq": 4,
              "section": "T7 — Evidential and Methodological Foundation",
              "question_text": "Does the human science framework surface any aspect of this characteristic that the verse evidence has not yet addressed — and does that absence require further verse investigation?",
              "pattern_type": null,
              "scope": "universal",
              "status": "active"
            }
          ]
        }
      }
    }
  }
}
```

### Registry-specific extensions for R090 innocence

_None._ No active non-tiered extensions in `wa_obs_question_catalogue` are sourced from registry 90 (innocence).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-02T15:24:48Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`

**Stage 1 quick checks:**

- Registry status fields populated: ✓
- OWNER term inventory non-empty: ✓
- All OWNER terms have at least 1 verse: ✓
- Researcher fields preserved: absent — researcher narrative not yet written

**Notes / concerns:**
- session_b_status='Verse Context Reset' — investigate whether this is current or stale post-VCB-13.

---

*End of readiness output v3 — wa-090-innocence.*