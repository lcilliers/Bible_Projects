# wa-099-kindness — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-05-01T09:47:25Z · schema 3.17.0_

_Strategy: vc-corrective-strategy-v2 §4 · sections aligned with `wa-sessionb-analysis-output-v1_1` reading units 1-9._

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

- **Registry no:** `99` · **word:** `kindness`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v1.9-2026-04-09`)
- **cluster_assignment:** `C17`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Relational/Social`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 61  (programme-wide aggregate including XREF and historical terms — current OWNER count is 22, XREF 34)
- `phase1_verse_count`: 3363  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 1 unresolved · **Existing session_b_findings:** 0

**Description:**

> Kindness is the quality of treating others well — not from obligation but from genuine care, warmth, and good will. The Hebrew hesed is one of the most important words in the entire biblical vocabulary: it covers steadfast love, loyal kindness, and covenant faithfulness. It is the word most often used for what God shows to his people. Human kindness is both an imitation of and a response to divine kindness. It moves outward, toward others, and it tends to seek the practical good of the person rather than stopping at good feelings.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-01T09:47:25Z`
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
| `H0120G` | a.dam | man | H | `extracted` | **`not_done`** | 1 | 162 | 4/0 | 48/0 | 8 |
| `H1454` | geh | this | H | `extracted` | **`not_done`** | 1 | 1 | 0/0 | 0/0 | 0 |
| `H1668` | da | this | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 1/0 | 1 |
| `H1791` | dekh | this | H | `extracted` | **`not_done`** | 1 | 11 | 0/0 | 0/0 | 0 |
| `H1797` | dik.ken | this | H | `extracted` | **`not_done`** | 1 | 3 | 0/0 | 0/0 | 0 |
| `H1976` | hal.la.zeh | this | H | `extracted` | **`not_done`** | 1 | 2 | 0/0 | 0/0 | 0 |
| `H2090` | zoh | this | H | `extracted` | **`not_done`** | 1 | 11 | 1/0 | 6/0 | 2 |
| `H2097` | zo | this | H | `extracted` | **`not_done`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `H2098` | zu | this | H | `extracted` | **`not_done`** | 1 | 15 | 1/0 | 12/0 | 2 |
| `H5971B` | am | kinsman | H | `extracted` | **`not_done`** | 1 | 30 | 1/0 | 20/0 | 2 |
| `H5971H` | am | People's [Gate] | H | `extracted` | **`not_done`** | 1 | 430 | 3/0 | 430/0 | 5 |
| `H5971I` | am | [Ibleam]-am | H | `extracted` | **`not_done`** | 1 | 430 | 3/0 | 430/0 | 5 |
| `H5971K` | am | people: soldiers | H | `extracted` | **`not_done`** | 1 | 69 | 1/0 | 5/0 | 2 |
| `H5971L` | am | people: creatures | H | `extracted` | **`not_done`** | 1 | 430 | 3/0 | 430/0 | 5 |
| `H5973B` | me.im | from with | H | `extracted` | **`not_done`** | 1 | 70 | 1/0 | 3/0 | 2 |
| `H5974` | im | with | H | `extracted` | **`not_done`** | 1 | 20 | 1/0 | 8/0 | 2 |
| `H5978` | im.ma.di | with me | H | `extracted` | **`not_done`** | 1 | 42 | 3/0 | 18/0 | 6 |
| `H5980` | um.mah | close | H | `extracted` | **`not_done`** | 1 | 28 | 0/0 | 0/0 | 0 |
| `H6004` | a.mam | to darken | H | `extracted` | **`not_done`** | 1 | 3 | 0/0 | 0/0 | 0 |
| `G5541` | chrēsteuomai | be kind | G | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G5542` | chrēstologia | smooth talk | G | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G5543` | chrēstos | good/kind | G | `extracted` | **`not_done`** | 1 | 7 | 1/0 | 6/0 | 2 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H0120G` — a.dam "man"

**Identity:** mti=953 · ti=1008 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:19): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: man, mankind

Sub-senses (depth > 1): 4 entries — present in DB; first 15:
  - `1a` (under `None`): man, human being
  - `1b` (under `None`): man, mankind (much more frequently intended sense in OT)
  - `1c` (under `None`): Adam, first man
  - `1d` (under `None`): city in Jordan valley

**Root family:**
- `ADAM` (Hebrew): man — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (14 total; sample of 14):**
- `H0119` a.dom "to redden"
- `H0120H` ha.a.dam "the man [Adam]"
- `H0121G` a.dam "Adam"
- `H0121H` a.dam "Adam"
- `H0122A` a.dom "red"
- `H0122B` e.dom "red stuff"
- `H0124` o.dem "sardius"
- `H0126` ad.mah "Admah"
- `H0127G` a.da.mah "land: soil"
- `H0127H` a.da.mah "land: country"
- `H0127I` a.da.mah "land: planet"
- `H0128` a.da.mah "Adamah"
- `H0129` a.da.mi "Adami"
- `H0582` e.nosh "human"

### `H1454` — geh "this"

**Identity:** mti=5776 · ti=5882 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: this, such
Aramaic equivalent: da (דָּא "this" H1668)

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H1430A` ga.dish "stack"
- `H1430B` ga.dish "tomb"
- `H1668` da "this"
- `H2088` zeh "this"

### `H1668` — da "this"

**Identity:** mti=5772 · ti=5878 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: this, one ... to ... another
Aramaic of geh (גֵּה "this" H1454)

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H1454` geh "this"
- `H1678` dov "bear"
- `H1768` di "that"
- `H1791` dekh "this"
- `H2088` zeh "this"

### `H1791` — dekh "this"

**Identity:** mti=5770 · ti=5876 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: this
Aramaic of zeh (זֶה "this" H2088)

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H1668` da "this"
- `H1768` di "that"
- `H1797` dik.ken "this"
- `H1836` de.nah "this"
- `H2088` zeh "this"

### `H1797` — dik.ken "this"

**Identity:** mti=5773 · ti=5879 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: this, that
Aramaic of zeh (זֶה "this" H2088)

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H1768` di "that"
- `H1791` dekh "this"
- `H1836` de.nah "this"
- `H2088` zeh "this"

### `H1976` — hal.la.zeh "this"

**Identity:** mti=5774 · ti=5880 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: this, this one (without subst), yonder

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H1973` ha.le.ah "further"
- `H1975` hal.laz "this"
- `H1977` hal.le.zu "this"
- `H2088` zeh "this"

### `H2090` — zoh "this"

**Identity:** mti=5771 · ti=5877 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: this

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `H2088` zeh "this"

### `H2097` — zo "this"

**Identity:** mti=5775 · ti=5881 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: demons pron
1) this, such rel pron f
2) which

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `H2088` zeh "this"

### `H2098` — zu "this"

**Identity:** mti=5769 · ti=5875 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: demons pron
1) this, such rel pron
2) (of) which, (of) whom

**Root family:**
- `DA` (Hebrew): this — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `H2088` zeh "this"

### `H5971B` — am "kinsman"

**Identity:** mti=5733 · ti=5839 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: kinsman, kindred

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (31 total; sample of 30):**
- `H5971A` am "people"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971K` am "people: soldiers"
- `H5971L` am "people: creatures"
- `H5972` am "people"
- `H5973A` im "with"
- `H5973B` me.im "from with"
- `H5978` im.ma.di "with me"
- `H5980` um.mah "close"
- `H5981` um.mah "Ummah"
- `H5983` am.mon "Ammon"
- `H5984G` am.mo.ni "Meunite"
- `H5984H` am.mo.ni "Ammon"
- `H5988G` am.mi.el "Ammiel"
- … and 15 more shown of 31 total

### `H5971H` — am "People's [Gate]"

**Identity:** mti=5737 · ti=5843 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: A location in Jerusalem only mentioned at Jer.17.19; 
only referred to as People's_Gate (עַם). § kinsman, kindred

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

### `H5971I` — am "[Ibleam]-am"

**Identity:** mti=5738 · ti=5844 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: § kinsman, kindred

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (11 total; sample of 11):**
- `H1109A` bil.am "Balaam"
- `H1109B` bil.am "Bileam"
- `H1667G` gat-rim.mon "Gath-rimmon"
- `H1667H` gat-rim.mon "Gath-rimmon"
- `H2991` yiv.le.am "Ibleam"
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971K` am "people: soldiers"
- `H5971L` am "people: creatures"
- `H6905H` qa.val "before"

### `H5971K` — am "people: soldiers"

**Identity:** mti=5732 · ti=5838 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: : soldiers/army
1) nation, people
1a) people, nation
1b) persons, members of one's people, compatriots, country-men

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971L` am "people: creatures"
- `H5972` am "people"
- `H6004` a.mam "to darken"

### `H5971L` — am "people: creatures"

**Identity:** mti=5739 · ti=5845 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: : creatures
1) nation, people
1a) people, nation
1b) persons, members of one's people, compatriots, country-men

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971K` am "people: soldiers"
- `H5972` am "people"
- `H6004` a.mam "to darken"

### `H5973B` — me.im "from with"

**Identity:** mti=5731 · ti=5837 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 0 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): beside, except
  - `1b` (under `None`): in spite of

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (31 total; sample of 30):**
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971K` am "people: soldiers"
- `H5971L` am "people: creatures"
- `H5973A` im "with"
- `H5974` im "with"
- `H5978` im.ma.di "with me"
- `H5980` um.mah "close"
- `H5981` um.mah "Ummah"
- `H5983` am.mon "Ammon"
- `H5984G` am.mo.ni "Meunite"
- `H5984H` am.mo.ni "Ammon"
- `H5988G` am.mi.el "Ammiel"
- … and 15 more shown of 31 total

### `H5974` — im "with"

**Identity:** mti=5735 · ti=5841 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: with

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): together with, with
  - `1b` (under `None`): with, during

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H5973A` im "with"
- `H5973B` me.im "from with"
- `H5978` im.ma.di "with me"
- `H5994` a.miq "deep"
- `H6015` a.mar "wool"

### `H5978` — im.ma.di "with me"

**Identity:** mti=952 · ti=1007 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:19): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: with
A grammatical form of im (עִם "with" H5973A) 
§ 1) with

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (30 total; sample of 30):**
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971K` am "people: soldiers"
- `H5971L` am "people: creatures"
- `H5973A` im "with"
- `H5973B` me.im "from with"
- `H5974` im "with"
- `H5980` um.mah "close"
- `H5981` um.mah "Ummah"
- `H5983` am.mon "Ammon"
- `H5984G` am.mo.ni "Meunite"
- `H5984H` am.mo.ni "Ammon"
- `H5988G` am.mi.el "Ammiel"
- … and 15 more shown of 30 total

### `H5980` — um.mah "close"

**Identity:** mti=5734 · ti=5840 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: juxtaposition

Sub-senses (depth > 1): 4 entries — present in DB; first 15:
  - `1a` (under `None`): used only as a prep
  - `1a1` (under `None`): close by, side by side with, alongside of, parallel with
  - `1a2` (under `None`): agreeing with, corresponding to, exactly as, close beside
  - `1a3` (under `None`): correspondingly to

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (30 total; sample of 30):**
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971K` am "people: soldiers"
- `H5971L` am "people: creatures"
- `H5973A` im "with"
- `H5973B` me.im "from with"
- `H5978` im.ma.di "with me"
- `H5981` um.mah "Ummah"
- `H5983` am.mon "Ammon"
- `H5984G` am.mo.ni "Meunite"
- `H5984H` am.mo.ni "Ammon"
- `H5988G` am.mi.el "Ammiel"
- `H5988H` am.mi.el "Ammiel"
- … and 15 more shown of 30 total

### `H6004` — a.mam "to darken"

**Identity:** mti=5736 · ti=5842 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to dim, darken, grow dark

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal) to dim, eclipse, be held dark
  - `1b` (under `None`): (Hophal) to be dimmed, grow dark

**Root family:**
- `AM` (Hebrew): with — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H5971A` am "people"
- `H5971B` am "kinsman"
- `H5971H` am "People's [Gate]"
- `H5971I` am "[Ibleam]-am"
- `H5971K` am "people: soldiers"
- `H5971L` am "people: creatures"
- `H5973A` im "with"
- `H5973B` me.im "from with"
- `H5980` um.mah "close"

### `G5541` — chrēsteuomai "be kind"

**Identity:** mti=5729 · ti=5835 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to be kind 
to be gentle, benign, kind, 1Cor. 13:4*

**Root family:**
- `CHRĒS` (Greek): be kind — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G5542` chrēstologia "smooth talk"
- `G5543` chrēstos "good/kind"
- `G5544` chrēstotēs "kindness"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G5542` — chrēstologia "smooth talk"

**Identity:** mti=5730 · ti=5836 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: smooth talk, attractive speech 
bland address, attractive speech, fair speaking, Rom. 16:18*

**Root family:**
- `CHRĒS` (Greek): be kind — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G3004G` legō "to say: says"
- `G3004H` legō "to say: name"
- `G5541` chrēsteuomai "be kind"
- `G5543` chrēstos "good/kind"
- `G5544` chrēstotēs "kindness"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G5543` — chrēstos "good/kind"

**Identity:** mti=954 · ti=1010 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:09:20): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: easy, good; kind, loving, benevolent 
useful, profitable; good, agreeable, Lk. 5:39; easy, as a yoke, Mt. 11:30; gentle, benign, kind, obliging, gracious, benign Lk. 6:35; Eph. 4:32; Rom. 2:4; 1Pet. 2:3; good in character, disposition, etc., virtuous, 1Cor. 15:33*

**Root family:**
- `CHRĒS` (Greek): be kind — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0888` achreios "worthless"
- `G2173` euchrēstos "helpful"
- `G5536` chrēma "money"
- `G5539` chrēsimos "profitable"
- `G5544` chrēstotēs "kindness"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (34)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `G0866` | afilarguros | not greedy | G | 103 love | `extracted` | 2 |
| `G2705` | katafileō | to kiss | G | 103 love | `extracted` | 6 |
| `G4375` | prosfilēs | lovely | G | 103 love | `extracted` | 1 |
| `G5360` | filadelfia | brotherly love | G | 103 love | `extracted` | 5 |
| `G5361` | filadelfos | loving the brothers | G | 103 love | `extracted` | 1 |
| `G5362` | filandros | husband-loving | G | 103 love | `extracted` | 1 |
| `G5363` | filanthrōpia | benevolence | G | 103 love | `extracted` | 2 |
| `G5364` | filanthrōpōs | benevolently | G | 3 ambition | `extracted_thin` | 1 |
| `G5365` | filarguria | love of money | G | 103 love | `extracted` | 1 |
| `G5366` | filarguros | money-loving | G | 103 love | `extracted` | 2 |
| `G5367` | filautos | selfish | G | 3 ambition | `extracted_thin` | 1 |
| `G5368` | fileō | to love | G | 103 love | `extracted` | 21 |
| `G5369` | filēdonos | pleasure-loving | G | 103 love | `extracted` | 1 |
| `G5370` | filēma | kiss | G | 103 love | `extracted` | 7 |
| `G5373` | filia | friendship | G | 103 love | `extracted` | 1 |
| `G5379` | filoneikia | love of dispute | G | 103 love | `extracted` | 1 |
| `G5380` | filoneikos | dispute-loving | G | 103 love | `extracted` | 1 |
| `G5381` | filoxenia | hospitality | G | 3 ambition | `extracted` | 2 |
| `G5382` | filoxenos | hospitable | G | 3 ambition | `extracted` | 3 |
| `G5384` | filos | friendly/friend | G | 103 love | `extracted` | 27 |
| `G5387` | filostorgos | affectionate | G | 103 love | `extracted` | 1 |
| `G5388` | filoteknos | child loving | G | 103 love | `extracted` | 1 |
| `G5389` | filotimeomai | to aspire | G | 3 ambition | `extracted_thin` | 3 |
| `G5390` | filofronōs | hospitably | G | 3 ambition | `extracted_thin` | 1 |
| `G5391` | filofrōn | friendly | G | 112 mind | `extracted_thin` | 1 |
| `G5544` | chrēstotēs | kindness | G | 67 goodness | `extracted` | 7 |
| `H1768` | di | that | H | 198 might | `extracted` | 60 |
| `H1836` | de.nah | this | H | 173 will | `extracted` | 33 |
| `H2616A` | cha.sad | be kind | H | 23 compassion | `extracted_thin` | 2 |
| `H2616B` | cha.sad | to shame | H | 146 shame | `extracted_thin` | 2 |
| `H2617A` | che.sed | kindness | H | 103 love | `extracted` | 169 |
| `H2617B` | che.sed | shame | H | 23 compassion | `extracted_thin` | 169 |
| `H2623` | cha.sid | pious | H | 103 love | `extracted` | 33 |
| `H7356A` | ra.cham | womb | H | 23 compassion | `extracted` | 5 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H0120G` — 4 groups

- **`953-001`** — 16 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Inner moral condition characteristic of humanity — evil inclination of the heart, capacity for wickedness*
- **`953-002`** — 11 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Human frailty and dependence before God — inner limitation and creaturely orientation defining adam*
- **`953-003`** — 11 relevant · 2 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C17`
  - *Humanity as object of God's purposeful action — created in God's image, known, called to reflect divine character*
- **`953-004`** — 10 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Specific inner dispositions of individual persons as representative human qualities — meekness, wisdom, contrition, humility*

### `H1454` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H1668` — 1 groups

- **`5772-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term directs and intensifies expression of inner pride — pointing to object of self-glorification*

### `H1791` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H1797` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H1976` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H2090` — 1 groups

- **`5771-001`** — 6 relevant · 2 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C17`
  - *Term frames inner reflection on meaning and worth of human experience — wisdom on joy, futility, divine gifting*

### `H2097` — 1 groups

- **`5775-001`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term directs attention to consequence of inner moral orientation — outcome of covenant faithfulness or spiritual infidelity*

### `H2098` — 1 groups

- **`5769-001`** — 12 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Spiritual faintness and trust — the inner person in extremity, directing its cry and its trust toward God as the one who knows the way*
  - notes: Revised during Dimension Review Phase B.5: characteristic-perspective rewrite. Old: Term connects and qualifies inner-being content — directing attention to persons or conditions where inner life is expressed

### `H5971B` — 1 groups

- **`5733-001`** — 20 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Relational community of belonging — gathered to or cut off from one's people as inner belonging, covenant faithfulness, or moral transgression*

### `H5971H` — 3 groups

- **`5737-001`** — 427 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Covenant community as object of God's relational love and moral claim — 'my people' as relational partner of the divine*
- **`5737-002`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Corporate inner spiritual condition of the people — rebellion, fear, trust, shame, orientation toward God*
- **`5737-003`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *People as bearer of communal inner identity — shared moral-spiritual character defining who 'the people' are*

### `H5971I` — 3 groups

- **`5738-001`** — 427 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Covenant community as object of God's relational love and moral claim — 'my people' as relational partner of the divine*
- **`5738-002`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Corporate inner spiritual condition of the people — rebellion, fear, trust, shame, orientation toward God*
- **`5738-003`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *People as bearer of communal inner identity — shared moral-spiritual character defining who 'the people' are*

### `H5971K` — 1 groups

- **`5732-001`** — 5 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C17`
  - *Military force as communal subject of inner responses to battle — fear, courage, trust in God, inner orientation required at war*

### `H5971L` — 3 groups

- **`5739-001`** — 427 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Covenant community as object of God's relational love and moral claim — 'my people' as relational partner of the divine*
- **`5739-002`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Corporate inner spiritual condition of the people — rebellion, fear, trust, shame, orientation toward God*
- **`5739-003`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *People as bearer of communal inner identity — shared moral-spiritual character defining who 'the people' are*

### `H5973B` — 1 groups

- **`5731-001`** — 3 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C17`
  - *Departure from relational presence expressing inner relational states — grief at loss, guilt, inner fear of separation*

### `H5974` — 1 groups

- **`5735-001`** — 8 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Relational presence of God or companions as context for inner experience — worship, petition, strengthening, or humbling*

### `H5978` — 3 groups

- **`952-001`** — 7 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term frames divine presence as the condition of inner trust, security, and confident orientation toward God*
- **`952-002`** — 6 relevant · 2 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C17`
  - *Term marks the zone of direct divine encounter with the self — whether affliction or care — as shaping the person's inner state*
- **`952-003`** — 5 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term frames a relational/covenantal bond expressing inner orientation of faithfulness, loyalty, or dependence*

### `H5980` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H6004` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `G5541` — 1 groups

- **`5729-001`** — 1 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Kindness as inner quality of love — outward expression of love's inner character toward others*

### `G5542` — 1 groups

- **`5730-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Deceptive inner disposition expressed as flattering speech — false kindness targeting the naive*

### `G5543` — 1 groups

- **`954-001`** — 6 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Goodness/kindness as inner quality of God or persons — disposition of gracious favour expressed toward others*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 177 worth | 8 | `H2098,H1791,H2090,H1668,H1797,H1976,H2097,H1454` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 197 authority | 111 |
| 187 strength | 100 |
| 176 worship | 64 |
| 61 fear | 63 |
| 51 distress | 57 |
| 100 knowledge | 53 |
| 183 heart | 46 |
| 194 blessing | 45 |
| 196 power | 43 |
| 213 listen | 43 |
| 57 evil | 38 |
| 73 guilt | 38 |
| 121 praise | 38 |
| 173 will | 38 |
| 97 joy | 36 |
| 43 desire | 35 |
| 44 despair | 34 |
| 91 insight | 30 |
| 112 mind | 30 |
| 147 sin | 30 |
| 166 understanding | 30 |
| 188 weeping | 30 |
| 103 love | 29 |
| 60 faithfulness | 28 |
| 98 justice | 27 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 4 anger | Num 14:11 |
| 8 appetite | Dan 4:34 |
| 23 compassion | Mic 6:8 |
| 24 condemnation | Mic 6:8 |
| 44 despair | Num 14:11 |
| 51 distress | Gen 44:29 |
| 51 distress | Gen 6:5 |
| 52 division | Ecc 5:19 |
| 57 evil | Gen 6:5 |
| 58 experience | Gen 6:5 |
| 67 goodness | Mic 6:8 |
| 68 grace | Eph 4:32 |
| 78 hope | Jer 17:5 |
| 80 humility | Isa 2:11 |
| 80 humility | Mic 6:8 |
| 89 iniquity | Jer 17:5 |
| 93 intention | Gen 6:5 |
| 100 knowledge | Dan 4:34 |
| 103 love | 1Cor 13:4 |
| 103 love | Mic 6:8 |
| 111 mercy | Dan 2:18 |
| 116 patience | 1Cor 13:4 |
| 123 pride | 1Cor 13:4 |
| 123 pride | Isa 2:11 |
| 126 purpose | Gen 6:5 |
| 135 repentance | Psa 23:4 |
| 158 terror | Gen 6:5 |
| 167 unity | Psa 23:4 |
| 173 will | Mic 6:8 |
| 177 worth | Job 6:4 |
| 183 heart | Eph 4:32 |
| 183 heart | Gen 6:5 |
| 185 flesh | Jer 17:5 |
| 187 strength | Jer 17:5 |
| 187 strength | Num 14:19 |
| 197 authority | Dan 4:30 |
| 197 authority | Gen 1:26 |
| 199 dominion | Dan 4:34 |
| 201 image | Gen 1:26 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (0)

_None._

### H.2 Open SD pointers + research flags (1)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `DIMREVIEW_SESSION_D` | DIM-99-SD001 | MEDIUM | D | 2026-04-11 |

#### DIM-99-SD001

> The am-variant groups in Reg 99 (H5971H/I/L, each with three sub-groups) produce a large corpus (427 verses each for the -001 groups) where Moses's inner orientation of solidarity and advocacy appears as the primary inner-being content of the anchor verses. This raises a structural question: why are "people/am" terms placed in Reg 99 (kindness)? The intercessory solidarity of Moses (Num 14:19 — appealing to God's steadfast love on behalf of the people) may be the inner-being connection — Moses's advocacy for the people is itself an expression of kindness/solidarity as an inner orientation. Session D should examine whether the community-solidarity vocabulary of Reg 99 (the am-terms, the im.ma.di terms, the im-terms) encodes a dimension of kindness that is specifically communal and intercessory, rather than individual. The hypothesis: Reg 99 may contain a communal or social-solidarity sub-pattern that is distinct from the dyadic relational orientation of the love/compassion/mercy registries.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `G5543` (3 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`21`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`SPAN_RESOLUTION_CONFLICT`** — Queried Strong's not found in any verse span after suffix resolution. Verse set is empty. Manual STEP UI verification required.
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H0120G` — 48/162 classified · 8 anchor verse(s)

**Group `953-001`** (16 verses — anchors: Gen 6:5, Jer 17:5)

- **Gen 6:5** 🔵 (✓) *target: man*
  > Gen 6:5 The Lord saw that the wickedness of man was great in the earth , and that every intention of the thoughts of his heart was only evil continually .
- **Jer 17:5** 🔵 (✓) *target: man*
  > Jer 17:5 Thus says the Lord : “ Cursed is the man who trusts in man and makes flesh his strength , whose heart turns away from the Lord .
- **Gen 6:6** (✓) *target: man*
  > Gen 6:6 And the Lord regretted that he had made man on the earth , and it grieved him to his heart .
  - notes: dual_context: also 953-003
- **Gen 8:21** (✓) *target: man*
  > Gen 8:21 And when the Lord smelled the pleasing aroma , the Lord said in his heart , “I will never again curse the ground because of man , for the intention of man’s heart is evil from his youth . Neither will I ever again strike down every living creature as I have done .
- **Job 5:7** (✓) *target: man*
  > Job 5:7 but man is born to trouble as the sparks fly upward .
- **Job 14:1** (✓) *target: Man*
  > Job 14:1 “ Man who is born of a woman is few of days and full of trouble .
- **Job 15:7** (✓) *target: man*
  > Job 15:7 “Are you the first man who was born ? Or were you brought forth before the hills ?
- **Job 25:6** (✓) *target: man*
  > Job 25:6 how much less man , who is a maggot , and the son of man , who is a worm !”
- **Isa 2:9** (✓) *target: man*
  > Isa 2:9 So man is humbled , and each one is brought low — do not forgive them !
- **Isa 2:17** (✓) *target: man*
  > Isa 2:17 And the haughtiness of man shall be humbled , and the lofty pride of men shall be brought low , and the Lord alone will be exalted in that day .
- **Isa 5:15** (✓) *target: Man*
  > Isa 5:15 Man is humbled , and each one is brought low , and the eyes of the haughty are brought low .
- **Isa 29:21** (✓) *target: man*
  > Isa 29:21 who by a word make a man out to be an offender , and lay a snare for him who reproves in the gate , and with an empty plea turn aside him who is in the right .
- **Jer 10:14** (✓) *target: man*
  > Jer 10:14 Every man is stupid and without knowledge ; every goldsmith is put to shame by his idols , for his images are false , and there is no breath in them .
- **Jer 51:17** (✓) *target: man*
  > Jer 51:17 Every man is stupid and without knowledge ; every goldsmith is put to shame by his idols , for his images are false , and there is no breath in them .
- **Lam 3:39** (✓) *target: man*
  > Lam 3:39 Why should a living man complain , a man , about the punishment of his sins ?
- **Mic 7:2** (✓) *target: mankind*
  > Mic 7:2 The godly has perished from the earth , and there is no one upright among mankind ; they all lie in wait for blood , and each hunts the other with a net .

**Group `953-002`** (11 verses — anchors: Isa 2:11, Jer 10:23)

- **Isa 2:11** 🔵 (✓) *target: men*
  > Isa 2:11 The haughty looks of man shall be brought low , and the lofty pride of men shall be humbled , and the Lord alone will be exalted in that day .
- **Jer 10:23** 🔵 (✓) *target: man*
  > Jer 10:23 I know , O Lord , that the way of man is not in himself, that it is not in man who walks to direct his steps .
- **Num 23:19** (✓) *target: man*
  > Num 23:19 God is not man , that he should lie , or a son of man , that he should change his mind . Has he said , and will he not do it? Or has he spoken , and will he not fulfill it ?
- **Job 7:20** (✓) *target: mankind*
  > Job 7:20 If I sin , what do I do to you, you watcher of mankind ? Why have you made me your mark ? Why have I become a burden to you?
- **Job 34:29** (✓) *target: man*
  > Job 34:29 When he is quiet , who can condemn ? When he hides his face , who can behold him, whether it be a nation or a man ?—
- **Isa 31:3** (✓) *target: man*
  > Isa 31:3 The Egyptians are man , and not God , and their horses are flesh , and not spirit . When the Lord stretches out his hand , the helper will stumble , and he who is helped will fall , and they will all perish together .
- **Isa 38:11** (✓) *target: man*
  > Isa 38:11 I said , I shall not see the Lord , the Lord in the land of the living ; I shall look on man no more among the inhabitants of the world .
- **Isa 51:12** (✓) *target: man*
  > Isa 51:12 “ I , I am he who comforts you; who are you that you are afraid of man who dies , of the son of man who is made like grass ,
- **Jer 32:19** (✓) *target: man*
  > Jer 32:19 great in counsel and mighty in deed , whose eyes are open to all the ways of the children of man , rewarding each one according to his ways and according to the fruit of his deeds .
- **Lam 3:36** (✓) *target: man*
  > Lam 3:36 to subvert a man in his lawsuit , the Lord does not approve .
- **Hab 1:14** (✓) *target: mankind*
  > Hab 1:14 You make mankind like the fish of the sea , like crawling things that have no ruler .

**Group `953-003`** (11 verses — anchors: Gen 1:26, Mic 6:8)

- **Gen 1:26** 🔵 (✓) *target: man*
  > Gen 1:26 Then God said , “Let us make man in our image , after our likeness . And let them have dominion over the fish of the sea and over the birds of the heavens and over the livestock and over all the earth and over every creeping thing that creeps on the earth .”
- **Mic 6:8** 🔵 (✓) *target: man*
  > Mic 6:8 He has told you , O man , what is good ; and what does the Lord require of you but to do justice , and to love kindness , and to walk humbly with your God ?
- **Gen 1:27** (✓) *target: man*
  > Gen 1:27 So God created man in his own image , in the image of God he created him; male and female he created them .
- **Gen 5:1** (✓) *target: man*
  > Gen 5:1 This is the book of the generations of Adam . When God created man , he made him in the likeness of God .
- **Gen 9:6** (✓) *target: man*
  > Gen 9:6 “Whoever sheds the blood of man , by man shall his blood be shed , for God made man in his own image .
- **Job 16:21** (✓) *target: man*
  > Job 16:21 that he would argue the case of a man with God , as a son of man does with his neighbor .
- **Job 28:28** (✓) *target: man*
  > Job 28:28 And he said to man , ‘ Behold , the fear of the Lord , that is wisdom , and to turn away from evil is understanding .’”
- **Job 33:23** (✓) *target: man*
  > Job 33:23 If there be for him an angel , a mediator , one of the thousand , to declare to man what is right for him,
- **Job 37:7** (✓) *target: man*
  > Job 37:7 He seals up the hand of every man , that all men whom he made may know it.
- **Isa 43:4** (✓) *target: men*
  > Isa 43:4 Because you are precious in my eyes , and honored , and I love you, I give men in return for you , peoples in exchange for your life .
- **Jer 32:20** (✓) *target: mankind*
  > Jer 32:20 You have shown signs and wonders in the land of Egypt , and to this day in Israel and among all mankind , and have made a name for yourself, as at this day .

**Group `953-004`** (10 verses — anchors: Num 12:3, Isa 29:19)

- **Num 12:3** 🔵 (✓) *target: people*
  > Num 12:3 Now the man Moses was very meek , more than all people who were on the face of the earth .
- **Isa 29:19** 🔵 (✓) *target: mankind*
  > Isa 29:19 The meek shall obtain fresh joy in the Lord , and the poor among mankind shall exult in the Holy One of Israel .
- **Neh 2:12** (✓) *target: one*
  > Neh 2:12 Then I arose in the night , I and a few men with me. And I told no one what my God had put into my heart to do for Jerusalem . There was no animal with me but the one on which I rode .
- **Job 33:17** (✓) *target: man*
  > Job 33:17 that he may turn man aside from his deed and conceal pride from a man ;
- **Job 34:30** (✓) *target: man*
  > Job 34:30 that a godless man should not reign , that he should not ensnare the people .
- **Job 35:8** (✓) *target: man*
  > Job 35:8 Your wickedness concerns a man like yourself, and your righteousness a son of man .
- **Isa 17:7** (✓) *target: man*
  > Isa 17:7 In that day man will look to his Maker , and his eyes will look on the Holy One of Israel .
- **Isa 56:2** (✓) *target: man*
  > Isa 56:2 Blessed is the man who does this , and the son of man who holds it fast , who keeps the Sabbath , not profaning it, and keeps his hand from doing any evil .”
- **Isa 58:5** (✓) *target: person*
  > Isa 58:5 Is such the fast that I choose , a day for a person to humble himself ? Is it to bow down his head like a reed , and to spread sackcloth and ashes under him? Will you call this a fast , and a day acceptable to the Lord ?
- **Hos 11:4** (✓) *target: kindness*
  > Hos 11:4 I led them with cords of kindness , with the bands of love , and I became to them as one who eases the yoke on their jaws , and I bent down to them and fed them.

**Group `UNCLASSIFIED`** (114 verses)

- **Gen 2:5** (—) *target: man*
  > Gen 2:5 When no bush of the field was yet in the land and no small plant of the field had yet sprung up— for the Lord God had not caused it to rain on the land , and there was no man to work the ground ,
- **Gen 5:2** (—) *target: Man*
  > Gen 5:2 Male and female he created them, and he blessed them and named them Man when they were created .
- **Gen 6:1** (—) *target: man*
  > Gen 6:1 When man began to multiply on the face of the land and daughters were born to them ,
- **Gen 6:2** (—) *target: man*
  > Gen 6:2 the sons of God saw that the daughters of man were attractive . And they took as their wives any they chose .
- **Gen 6:3** (—) *target: man*
  > Gen 6:3 Then the Lord said , “My Spirit shall not abide in man forever , for he is flesh : his days shall be 120 years .”
- **Gen 6:4** (—) *target: man*
  > Gen 6:4 The Nephilim were on the earth in those days , and also afterward , when the sons of God came in to the daughters of man and they bore children to them . These were the mighty men who were of old , the men of renown .
- **Gen 6:7** (—) *target: man*
  > Gen 6:7 So the Lord said , “I will blot out man whom I have created from the face of the land , man and animals and creeping things and birds of the heavens , for I am sorry that I have made them .”
- **Gen 7:21** (—) *target: mankind*
  > Gen 7:21 And all flesh died that moved on the earth , birds , livestock , beasts , all swarming creatures that swarm on the earth , and all mankind .
- **Gen 7:23** (—) *target: man*
  > Gen 7:23 He blotted out every living thing that was on the face of the ground , man and animals and creeping things and birds of the heavens . They were blotted out from the earth . Only Noah was left , and those who were with him in the ark .
- **Gen 9:5** (—) *target: man*
  > Gen 9:5 And for your lifeblood I will require a reckoning : from every beast I will require it and from man . From his fellow man I will require a reckoning for the life of man .
- **Gen 11:5** (—) *target: man*
  > Gen 11:5 And the Lord came down to see the city and the tower , which the children of man had built .
- **Gen 16:12** (—) *target: man*
  > Gen 16:12 He shall be a wild donkey of a man , his hand against everyone and everyone’s hand against him, and he shall dwell over against all his kinsmen .”
- **Lev 1:2** (—) *target: one*
  > Lev 1:2 “ Speak to the people of Israel and say to them, When any one of you brings an offering to the Lord , you shall bring your offering of livestock from the herd or from the flock .
- **Lev 5:3** (—) *target: human*
  > Lev 5:3 or if he touches human uncleanness , of whatever sort the uncleanness may be with which one becomes unclean , and it is hidden from him , when he comes to know it, and realizes his guilt ;
- **Lev 5:4** (—) *target: people*
  > Lev 5:4 or if anyone utters with his lips a rash oath to do evil or to do good , any sort of rash oath that people swear , and it is hidden from him , when he comes to know it, and he realizes his guilt in any of these ;
- **Lev 6:3** (—) *target: people*
  > Lev 6:3 or has found something lost and lied about it, swearing falsely —in any of all the things that people do and sin thereby —
- **Lev 7:21** (—) *target: human*
  > Lev 7:21 And if anyone touches an unclean thing , whether human uncleanness or an unclean beast or any unclean detestable creature, and then eats some flesh from the sacrifice of the Lord’s peace offerings , that person shall be cut off from his people .”
- **Lev 13:2** (—) *target: person*
  > Lev 13:2 “When a person has on the skin of his body a swelling or an eruption or a spot , and it turns into a case of leprous disease on the skin of his body , then he shall be brought to Aaron the priest or to one of his sons the priests ,
- **Lev 13:9** (—) *target: man*
  > Lev 13:9 “When a man is afflicted with a leprous disease , he shall be brought to the priest ,
- **Lev 16:17** (—) *target: one*
  > Lev 16:17 No one may be in the tent of meeting from the time he enters to make atonement in the Holy Place until he comes out and has made atonement for himself and for his house and for all the assembly of Israel .
- **Lev 18:5** (—) *target: person*
  > Lev 18:5 You shall therefore keep my statutes and my rules ; if a person does them, he shall live by them: I am the Lord .
- **Lev 22:5** (—) *target: person*
  > Lev 22:5 and whoever touches a swarming thing by which he may be made unclean or a person from whom he may take uncleanness , whatever his uncleanness may be—
- **Lev 24:17** (—) *target: human*
  > Lev 24:17 “ Whoever takes a human life shall surely be put to death .
- **Lev 24:20** (—) *target: person*
  > Lev 24:20 fracture for fracture , eye for eye , tooth for tooth ; whatever injury he has given a person shall be given to him .
- **Lev 24:21** (—) *target: person*
  > Lev 24:21 Whoever kills an animal shall make it good , and whoever kills a person shall be put to death .
- **Lev 27:28** (—) *target: man*
  > Lev 27:28 “ But no devoted thing that a man devotes to the Lord , of anything that he has, whether man or beast , or of his inherited field , shall be sold or redeemed ; every devoted thing is most holy to the Lord .
- **Lev 27:29** (—) *target: mankind*
  > Lev 27:29 No one devoted , who is to be devoted for destruction from mankind , shall be ransomed ; he shall surely be put to death .
- **Num 3:13** (—) *target: man*
  > Num 3:13 for all the firstborn are mine. On the day that I struck down all the firstborn in the land of Egypt , I consecrated for my own all the firstborn in Israel , both of man and of beast . They shall be mine: I am the Lord .”
- **Num 5:6** (—) *target: people*
  > Num 5:6 “ Speak to the people of Israel , When a man or woman commits any of the sins that people commit by breaking faith with the Lord , and that person realizes his guilt ,
- **Num 8:17** (—) *target: man*
  > Num 8:17 For all the firstborn among the people of Israel are mine, both of man and of beast . On the day that I struck down all the firstborn in the land of Egypt I consecrated them for myself ,
- **Num 9:6** (—) *target: dead body*
  > Num 9:6 And there were certain men who were unclean through touching a dead body , so that they could not keep the Passover on that day , and they came before Moses and Aaron on that day .
- **Num 9:7** (—) *target: dead body*
  > Num 9:7 And those men said to him, “ We are unclean through touching a dead body . Why are we kept from bringing the Lord’s offering at its appointed time among the people of Israel ?”
- **Num 16:29** (—) *target: men*
  > Num 16:29 If these men die as all men die , or if they are visited by the fate of all mankind , then the Lord has not sent me .
- **Num 16:32** (—) *target: people*
  > Num 16:32 And the earth opened its mouth and swallowed them up, with their households and all the people who belonged to Korah and all their goods .
- **Num 18:15** (—) *target: man*
  > Num 18:15 Everything that opens the womb of all flesh , whether man or beast , which they offer to the Lord , shall be yours. Nevertheless, the firstborn of man you shall redeem , and the firstborn of unclean animals you shall redeem .
- **Num 19:11** (—) *target: person*
  > Num 19:11 “Whoever touches the dead body of any person shall be unclean seven days .
- **Num 19:13** (—) *target: anyone*
  > Num 19:13 Whoever touches a dead person, the body of anyone who has died , and does not cleanse himself, defiles the tabernacle of the Lord , and that person shall be cut off from Israel ; because the water for impurity was not thrown on him, he shall be unclean . His uncleanness is still on him .
- **Num 19:14** (—) *target: someone*
  > Num 19:14 “This is the law when someone dies in a tent : everyone who comes into the tent and everyone who is in the tent shall be unclean seven days .
- **Num 19:16** (—) *target: human*
  > Num 19:16 Whoever in the open field touches someone who was killed with a sword or who died naturally , or touches a human bone or a grave , shall be unclean seven days .
- **Num 31:11** (—) *target: man*
  > Num 31:11 and took all the spoil and all the plunder , both of man and of beast .
- **Num 31:26** (—) *target: man*
  > Num 31:26 “ Take the count of the plunder that was taken , both of man and of beast , you and Eleazar the priest and the heads of the fathers’ houses of the congregation ,
- **Num 31:28** (—) *target: people*
  > Num 31:28 And levy for the Lord a tribute from the men of war who went out to battle , one out of five hundred , of the people and of the oxen and of the donkeys and of the flocks .
- **Num 31:30** (—) *target: people*
  > Num 31:30 And from the people of Israel’s half you shall take one drawn out of every fifty , of the people , of the oxen , of the donkeys , and of the flocks , of all the cattle , and give them to the Levites who keep guard over the tabernacle of the Lord .”
- **Num 31:35** (—) *target: persons*
  > Num 31:35 and 32,000 persons in all , women who had not known man by lying with him.
- **Num 31:40** (—) *target: persons*
  > Num 31:40 The persons were 16,000 , of which the Lord’s tribute was 32 persons .
- **Num 31:46** (—) *target: persons*
  > Num 31:46 and 16,000 persons —
- **Num 31:47** (—) *target: persons*
  > Num 31:47 from the people of Israel’s half Moses took one of every 50 , both of persons and of beasts , and gave them to the Levites who kept guard over the tabernacle of the Lord , as the Lord commanded Moses .
- **Judg 16:7** (—) *target: man*
  > Judg 16:7 Samson said to her, “ If they bind me with seven fresh bowstrings that have not been dried , then I shall become weak and be like any other man .”
- **Judg 16:11** (—) *target: man*
  > Judg 16:11 And he said to her, “ If they bind me with new ropes that have not been used , then I shall become weak and be like any other man .”
- **Judg 16:13** (—) *target: man*
  > Judg 16:13 Then Delilah said to Samson , “ Until now you have mocked me and told me lies . Tell me how you might be bound .” And he said to her, “ If you weave the seven locks of my head with the web and fasten it tight with the pin ^ , then I shall become weak and be like any other man .”
- **Judg 16:17** (—) *target: man*
  > Judg 16:17 And he told her all his heart , and said to her, “A razor has never come upon my head , for I have been a Nazirite to God from my mother’s womb . If my head is shaved , then my strength will leave me, and I shall become weak and be like any other man .”
- **Judg 18:7** (—) *target: anyone*
  > Judg 18:7 Then the five men departed and came to Laish and saw the people who were there , how they lived in security , after the manner of the Sidonians , quiet and unsuspecting , lacking nothing that is in the earth and possessing wealth , and how they were far from the Sidonians and had no dealings with anyone .
- **Judg 18:28** (—) *target: anyone*
  > Judg 18:28 And there was no deliverer because it was far from Sidon , and they had no dealings with anyone . It was in the valley that belongs to Beth-rehob . Then they rebuilt the city and lived in it .
- **Neh 2:10** (—) *target: someone*
  > Neh 2:10 But when Sanballat the Horonite and Tobiah the Ammonite servant heard this, it displeased them greatly that someone had come to seek the welfare of the people of Israel .
- **Neh 9:29** (—) *target: person*
  > Neh 9:29 And you warned them in order to turn them back to your law . Yet they acted presumptuously and did not obey your commandments , but sinned against your rules , which if a person does them, he shall live by them, and they turned a stubborn shoulder and stiffened their neck and would not obey .
- **Job 11:12** (—) *target: man*
  > Job 11:12 But a stupid man will get understanding when a wild donkey’s colt is born a man !
- **Job 14:10** (—) *target: man*
  > Job 14:10 But a man dies and is laid low ; man breathes his last , and where is he ?
- **Job 20:4** (—) *target: man*
  > Job 20:4 Do you not know this from of old , since man was placed on earth ,
- **Job 20:29** (—) *target: man’s*
  > Job 20:29 This is the wicked man’s portion from God , the heritage decreed for him by God .”
- **Job 21:4** (—) *target: man*
  > Job 21:4 As for me, is my complaint against man ? Why should I not be impatient ?
- **Job 21:33** (—) *target: mankind*
  > Job 21:33 The clods of the valley are sweet to him; all mankind follows after him, and those who go before him are innumerable .
- **Job 27:13** (—) *target: man*
  > Job 27:13 “ This is the portion of a wicked man with God , and the heritage that oppressors receive from the Almighty :
- **Job 32:21** (—) *target: person*
  > Job 32:21 I will not show partiality to any man or use flattery toward any person .
- **Job 34:11** (—) *target: man*
  > Job 34:11 For according to the work of a man he will repay him, and according to his ways he will make it befall him .
- **Job 34:15** (—) *target: man*
  > Job 34:15 all flesh would perish together , and man would return to dust .
- **Job 36:25** (—) *target: mankind*
  > Job 36:25 All mankind has looked on it; man beholds it from afar .
- **Job 36:28** (—) *target: mankind*
  > Job 36:28 which the skies pour down and drop on mankind abundantly .
- **Job 38:26** (—) *target: man*
  > Job 38:26 to bring rain on a land where no man is, on the desert in which there is no man ,
- **Isa 2:20** (—) *target: mankind*
  > Isa 2:20 In that day mankind will cast away their idols of silver and their idols of gold , which they made for themselves to worship , to the moles and to the bats ,
- **Isa 2:22** (—) *target: man*
  > Isa 2:22 Stop regarding man in whose nostrils is breath , for of what account is he ?
- **Isa 6:11** (—) *target: people*
  > Isa 6:11 Then I said , “How long , O Lord ?” And he said : “ Until cities lie waste without inhabitant , and houses without people , and the land is a desolate waste ,
- **Isa 6:12** (—) *target: people*
  > Isa 6:12 and the Lord removes people far away, and the forsaken places are many in the midst of the land .
- **Isa 13:12** (—) *target: mankind*
  > Isa 13:12 I will make people more rare than fine gold , and mankind than the gold of Ophir .
- **Isa 22:6** (—) *target: horsemen*
  > Isa 22:6 And Elam bore the quiver with chariots and horsemen , and Kir uncovered the shield .
- **Isa 31:8** (—) *target: man*
  > Isa 31:8 “And the Assyrian shall fall by a sword , not of man ; and a sword , not of man , shall devour him; and he shall flee from the sword , and his young men shall be put to forced labor .
- **Isa 37:19** (—) *target: men’s*
  > Isa 37:19 and have cast their gods into the fire . For they were no gods , but the work of men’s hands , wood and stone . Therefore they were destroyed .
- **Isa 44:11** (—) *target: human*
  > Isa 44:11 Behold , all his companions shall be put to shame , and the craftsmen are only human . Let them all assemble , let them stand forth . They shall be terrified ; they shall be put to shame together .
- **Isa 44:13** (—) *target: man*
  > Isa 44:13 The carpenter stretches a line ; he marks it out with a pencil . He shapes it with planes and marks it with a compass . He shapes it into the figure of a man , with the beauty of a man , to dwell in a house .
- **Isa 44:15** (—) *target: man*
  > Isa 44:15 Then it becomes fuel for a man . He takes a part of it and warms himself ; he kindles a fire and bakes bread . Also he makes a god and worships it; he makes it an idol and falls down before it .
- **Isa 45:12** (—) *target: man*
  > Isa 45:12 I made the earth and created man on it; it was my hands that stretched out the heavens , and I commanded all their host .
- **Isa 47:3** (—) *target: one*
  > Isa 47:3 Your nakedness shall be uncovered , and your disgrace shall be seen . I will take vengeance , and I will spare no one .
- **Isa 52:14** (—) *target: mankind*
  > Isa 52:14 As many were astonished at you— his appearance was so marred , beyond human semblance, and his form beyond that of the children of mankind —
- **Jer 2:6** (—) *target: man*
  > Jer 2:6 They did not say , ‘ Where is the Lord who brought us up from the land of Egypt , who led us in the wilderness , in a land of deserts and pits , in a land of drought and deep darkness , in a land that none passes through , where no man dwells ?’
- **Jer 4:25** (—) *target: man*
  > Jer 4:25 I looked , and behold , there was no man , and all the birds of the air had fled .
- **Jer 7:20** (—) *target: man*
  > Jer 7:20 Therefore thus says the Lord God : Behold , my anger and my wrath will be poured out on this place , upon man and beast , upon the trees of the field and the fruit of the ground ; it will burn and not be quenched .”
- **Jer 9:22** (—) *target: men*
  > Jer 9:22 Speak : “ Thus declares the Lord , ‘The dead bodies of men shall fall like dung upon the open field , like sheaves after the reaper , and none shall gather them.’”
- **Jer 16:20** (—) *target: man*
  > Jer 16:20 Can man make for himself gods ? Such are not gods !”
- **Jer 21:6** (—) *target: man*
  > Jer 21:6 And I will strike down the inhabitants of this city , both man and beast . They shall die of a great pestilence .
- **Jer 27:5** (—) *target: men*
  > Jer 27:5 “It is I who by my great power and my outstretched arm have made the earth , with the men and animals that are on the earth , and I give it to whomever it seems right to me.
- **Jer 31:27** (—) *target: man*
  > Jer 31:27 “ Behold , the days are coming , declares the Lord , when I will sow the house of Israel and the house of Judah with the seed of man and the seed of beast .
- **Jer 31:30** (—) *target: man*
  > Jer 31:30 But everyone shall die for his own iniquity . Each man who eats sour grapes , his teeth shall be set on edge .
- **Jer 32:43** (—) *target: man*
  > Jer 32:43 Fields shall be bought in this land of which you are saying , ‘It is a desolation , without man or beast ; it is given into the hand of the Chaldeans .’
- **Jer 33:5** (—) *target: men*
  > Jer 33:5 They are coming in to fight against the Chaldeans and to fill them with the dead bodies of men whom I shall strike down in my anger and my wrath , for I have hidden my face from this city because of all their evil .
- **Jer 33:10** (—) *target: man*
  > Jer 33:10 “ Thus says the Lord : In this place of which you say , ‘It is a waste without man or beast ,’ in the cities of Judah and the streets of Jerusalem that are desolate , without man or inhabitant or beast , there shall be heard again
- **Jer 33:12** (—) *target: man*
  > Jer 33:12 “ Thus says the Lord of hosts : In this place that is waste , without man or beast , and in all of its cities , there shall again be habitations of shepherds resting their flocks .
- **Jer 36:29** (—) *target: man*
  > Jer 36:29 And concerning Jehoiakim king of Judah you shall say , ‘ Thus says the Lord , You have burned this scroll , saying , “ Why have you written in it that the king of Babylon will certainly come and destroy this land , and will cut off from it man and beast ?”
- **Jer 47:2** (—) *target: Men*
  > Jer 47:2 “ Thus says the Lord : Behold , waters are rising out of the north , and shall become an overflowing torrent ; they shall overflow the land and all that fills it, the city and those who dwell in it. Men shall cry out , and every inhabitant of the land shall wail .
- **Jer 49:15** (—) *target: mankind*
  > Jer 49:15 For behold , I will make you small among the nations , despised among mankind .
- **Jer 49:18** (—) *target: man*
  > Jer 49:18 As when Sodom and Gomorrah and their neighboring cities were overthrown , says the Lord , no man shall dwell there , no man shall sojourn in her.
- **Jer 49:33** (—) *target: man*
  > Jer 49:33 Hazor shall become a haunt of jackals , an everlasting waste ; no man shall dwell there ; no man shall sojourn in her.”
- **Jer 50:3** (—) *target: man*
  > Jer 50:3 “ For out of the north a nation has come up against her, which shall make her land a desolation , and none shall dwell in it; both man and beast shall flee away .
- **Jer 50:40** (—) *target: man*
  > Jer 50:40 As when God overthrew Sodom and Gomorrah and their neighboring cities, declares the Lord , so no man shall dwell there , and no son of man shall sojourn in her.
- **Jer 51:14** (—) *target: men*
  > Jer 51:14 The Lord of hosts has sworn by himself : Surely I will fill you with men , as many as locusts , and they shall raise the shout of victory over you.
- **Jer 51:43** (—) *target: man*
  > Jer 51:43 Her cities have become a horror , a land of drought and a desert , a land in which no one dwells , and through which no son of man passes .
- **Jer 51:62** (—) *target: man*
  > Jer 51:62 and say , ‘O Lord , you have said concerning this place that you will cut it off , so that nothing shall dwell in it, neither man nor beast , and it shall be desolate forever .’
- **Hos 9:12** (—) *target: none*
  > Hos 9:12 Even if they bring up children , I will bereave them till none is left. Woe to them when I depart from them !
- **Hos 13:2** (—) *target: human*
  > Hos 13:2 And now they sin more and more , and make for themselves metal images , idols skillfully made of their silver , all of them the work of craftsmen . It is said of them, “Those who offer human sacrifice kiss calves !”
- **Mic 2:12** (—) *target: men*
  > Mic 2:12 I will surely assemble all of you, O Jacob ; I will gather the remnant of Israel ; I will set them together like sheep in a fold , like a flock in its pasture , a noisy multitude of men .
- **Mic 5:5** (—) *target: men*
  > Mic 5:5 And he shall be their peace . When the Assyrian comes into our land and treads in our palaces , then we will raise against him seven shepherds and eight princes of men ;
- **Mic 5:7** (—) *target: man*
  > Mic 5:7 Then the remnant of Jacob shall be in the midst of many peoples like dew from the Lord , like showers on the grass , which delay not for a man nor wait for the children of man .
- **Hab 2:8** (—) *target: man*
  > Hab 2:8 Because you have plundered many nations , all the remnant of the peoples shall plunder you, for the blood of man and violence to the earth , to cities and all who dwell in them .
- **Hab 2:17** (—) *target: man*
  > Hab 2:17 The violence done to Lebanon will overwhelm you, as will the destruction of the beasts that terrified them, for the blood of man and violence to the earth , to cities and all who dwell in them .
- **Hag 1:11** (—) *target: man*
  > Hag 1:11 And I have called for a drought on the land and the hills , on the grain , the new wine , the oil , on what the ground brings forth , on man and beast , and on all their labors .”
- **Mal 3:8** (—) *target: man*
  > Mal 3:8 Will man rob God ? Yet you are robbing me. But you say , ‘ How have we robbed you?’ In your tithes and contributions .

### `H1454` — 0/1 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (1 verse)

- **Eze 47:13** (—) *target: This*
  > Eze 47:13 Thus says the Lord God : “ This is the boundary by which you shall divide the land for inheritance among the twelve tribes of Israel . Joseph shall have two portions .

### `H1668` — 1/4 classified · 1 anchor verse(s)

**Group `5772-001`** (1 verse — anchors: Dan 4:30)

- **Dan 4:30** 🔵 (✓) *target: this*
  > Dan 4:30 and the king answered and said , “Is not this great Babylon , which I have built by my mighty power as a royal residence and for the glory of my majesty ?”

**Group `UNCLASSIFIED`** (3 verses)

- **Dan 5:6** (—) *target: together*
  > Dan 5:6 Then the king’s color changed , and his thoughts alarmed him; his limbs gave way , and his knees knocked together .
- **Dan 7:3** (—) *target: one*
  > Dan 7:3 And four great beasts came up out of the sea , different from one another .
- **Dan 7:8** (—) *target: in this*
  > Dan 7:8 I considered the horns , and behold , there came up among them another horn , a little one, before which three of the first horns were plucked up by the roots . And behold , in this horn were eyes like the eyes of a man , and a mouth speaking great things .

### `H1791` — 0/11 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (11 verses)

- **Ezr 4:13** (—) *target: this*
  > Ezr 4:13 Now be it known to the king that if this city is rebuilt and the walls finished , they will not pay tribute , custom , or toll , and the royal revenue will be impaired .
- **Ezr 4:15** (—) *target: this*
  > Ezr 4:15 in order that search may be made in the book of the records of your fathers . You will find in the book of the records and learn that this city is a rebellious city , hurtful to kings and provinces , and that sedition was stirred up in it from of old . That was why this city was laid waste .
- **Ezr 4:16** (—) *target: this*
  > Ezr 4:16 We make known to the king that if this city is rebuilt and its walls finished , you will then have no possession in the province Beyond the River .”
- **Ezr 4:19** (—) *target: this*
  > Ezr 4:19 And I made a decree , and search has been made, and it has been found that this city from of old has risen against kings , and that rebellion and sedition have been made in it .
- **Ezr 4:21** (—) *target: this*
  > Ezr 4:21 Therefore make a decree that these men be made to cease , and that this city be not rebuilt , until a decree is made by me.
- **Ezr 5:8** (—) *target: This*
  > Ezr 5:8 Be it known to the king that we went to the province of Judah , to the house of the great God . It is being built with huge stones , and timber is laid in the walls . This work goes on diligently and prospers in their hands .
- **Ezr 5:16** (—) *target: this*
  > Ezr 5:16 Then this Sheshbazzar came and laid the foundations of the house of God that is in Jerusalem , and from that time until now it has been in building , and it is not yet finished .’
- **Ezr 5:17** (—) *target: this*
  > Ezr 5:17 Therefore , if it seems good to the king , let search be made in the royal archives there in Babylon , to see whether a decree was issued by Cyrus the king for the rebuilding of this house of God in Jerusalem . And let the king send us his pleasure in this matter .”
- **Ezr 6:7** (—) *target: this*
  > Ezr 6:7 Let the work on this house of God alone . Let the governor of the Jews and the elders of the Jews rebuild this house of God on its site .
- **Ezr 6:8** (—) *target: this*
  > Ezr 6:8 Moreover, I make a decree regarding what you shall do for these elders of the Jews for the rebuilding of this house of God . The cost is to be paid to these men in full and without delay from the royal revenue , the tribute of the province from Beyond the River .
- **Ezr 6:12** (—) *target: this*
  > Ezr 6:12 May the God who has caused his name to dwell there overthrow any king or people who shall put out a hand to alter this, or to destroy this house of God that is in Jerusalem . I Darius make a decree ; let it be done with all diligence .”

### `H1797` — 0/3 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (3 verses)

- **Dan 2:31** (—) *target: This*
  > Dan 2:31 “ You saw , O king , and behold , a great image . This image , mighty and of exceeding brightness , stood before you, and its appearance was frightening .
- **Dan 7:20** (—) *target: that*
  > Dan 7:20 and about the ten horns that were on its head , and the other horn that came up and before which three of them fell , the horn that had eyes and a mouth that spoke great things , and that seemed greater than its companions .
- **Dan 7:21** (—) *target: this*
  > Dan 7:21 As I looked , this horn made war with the saints and prevailed over them ,

### `H1976` — 0/2 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (2 verses)

- **Gen 24:65** (—) *target: that*
  > Gen 24:65 and said to the servant , “ Who is that man , walking in the field to meet us ?” The servant said , “ It is my master .” So she took her veil and covered herself.
- **Gen 37:19** (—) *target: this*
  > Gen 37:19 They said to one another , “ Here comes this dreamer .

### `H2090` — 6/11 classified · 2 anchor verse(s)

**Group `5771-001`** (6 verses — anchors: Ecc 2:24, Ecc 5:19)

- **Ecc 2:24** 🔵 (✓) *target: This*
  > Ecc 2:24 There is nothing better for a person than that he should eat and drink and find enjoyment in his toil . This also , I saw , is from the hand of God ,
- **Ecc 5:19** 🔵 (✓) *target: this*
  > Ecc 5:19 Everyone also to whom God has given wealth and possessions and power to enjoy them , and to accept his lot and rejoice in his toil — this is the gift of God .
- **Ecc 2:2** (✓) *target: it*
  > Ecc 2:2 I said of laughter , “It is mad ,” and of pleasure , “ What use is it ?”
- **Ecc 5:16** (✓) *target: This*
  > Ecc 5:16 This also is a grievous evil : just as he came , so shall he go , and what gain is there to him who toils for the wind ?
- **Ecc 7:23** (✓) *target: this*
  > Ecc 7:23 All this I have tested by wisdom . I said , “I will be wise ,” but it was far from me .
- **Ecc 9:13** (✓) *target: this*
  > Ecc 9:13 I have also seen this example of wisdom under the sun , and it seemed great to me .

**Group `UNCLASSIFIED`** (5 verses)

- **Judg 18:4** (—) *target: This*
  > Judg 18:4 And he said to them, “ This is how Micah dealt with me: he has hired me, and I have become his priest .”
- **2Sa 11:25** (—) *target: another*
  > 2Sa 11:25 David said to the messenger , “ Thus shall you say to Joab , ‘Do not let this matter displease you , for the sword devours now one and now another . Strengthen your attack against the city and overthrow it.’ And encourage him .”
- **1Ki 14:5** (—) *target: Thus*
  > 1Ki 14:5 And the Lord said to Ahijah , “ Behold , the wife of Jeroboam is coming to inquire of you concerning her son , for he is sick . Thus and thus shall you say to her.” When she came , she pretended to be another woman.
- **2Ki 6:19** (—) *target: This*
  > 2Ki 6:19 And Elisha said to them, “ This is not the way , and this is not the city . Follow me, and I will bring you to the man whom you seek .” And he led them to Samaria .
- **Eze 40:45** (—) *target: This*
  > Eze 40:45 And he said to me, “ This chamber that faces south is for the priests who have charge of the temple ,

### `H2097` — 2/2 classified · 2 anchor verse(s)

**Group `5775-001`** (2 verses — anchors: Psa 132:12, Hos 7:16)

- **Psa 132:12** 🔵 (✓) *target: that*
  > Psa 132:12 If your sons keep my covenant and my testimonies that I shall teach them, their sons also forever shall sit on your throne .”
- **Hos 7:16** 🔵 (✓) *target: This*
  > Hos 7:16 They return , but not upward ; they are like a treacherous bow ; their princes shall fall by the sword because of the insolence of their tongue . This shall be their derision in the land of Egypt .

### `H2098` — 12/15 classified · 2 anchor verse(s)

**Group `5769-001`** (12 verses — anchors: Psa 142:3, Psa 143:8)

- **Psa 142:3** 🔵 (✓) *target: where*
  > Psa 142:3 When my spirit faints within me, you know my way ! In the path where I walk they have hidden a trap for me .
- **Psa 143:8** 🔵 (✓) *target: you*
  > Psa 143:8 Let me hear in the morning of your steadfast love , for in you I trust . Make me know the way I should go , for to you I lift up my soul .
- **Exo 15:13** (✓) *target: whom*
  > Exo 15:13 “You have led in your steadfast love the people whom you have redeemed ; you have guided them by your strength to your holy abode .
- **Exo 15:16** (✓) *target: whom*
  > Exo 15:16 Terror and dread fall upon them; because of the greatness of your arm , they are still as a stone , till your people , O Lord , pass by , till the people pass by whom you have purchased .
- **Psa 10:2** (✓) *target: that*
  > Psa 10:2 In arrogance the wicked hotly pursue the poor ; let them be caught in the schemes that they have devised .
- **Psa 12:7** (✓) *target: this*
  > Psa 12:7 You , O Lord , will keep them; you will guard us from this generation forever .
- **Psa 31:4** (✓) *target: hidden*
  > Psa 31:4 you take me out of the net they have hidden for me, for you are my refuge .
- **Psa 32:8** (✓) *target: way*
  > Psa 32:8 I will instruct you and teach you in the way you should go ; I will counsel you with my eye upon you.
- **Psa 62:11** (✓) *target: this*
  > Psa 62:11 Once God has spoken ; twice have I heard this : that power belongs to God ,
- **Isa 42:24** (✓) *target: whom*
  > Isa 42:24 Who gave up Jacob to the looter , and Israel to the plunderers ? Was it not the Lord , against whom we have sinned , in whose ways they would not walk , and whose law they would not obey ?
- **Isa 43:21** (✓) *target: the*
  > Isa 43:21 the people whom I formed for myself that they might declare my praise .
- **Hab 1:11** (✓) *target: whose*
  > Hab 1:11 Then they sweep by like the wind and go on, guilty men, whose own might is their god !”

**Group `UNCLASSIFIED`** (3 verses)

- **Psa 9:15** (—) *target: that*
  > Psa 9:15 The nations have sunk in the pit that they made ; in the net that they hid , their own foot has been caught .
- **Psa 17:9** (—) *target: who*
  > Psa 17:9 from the wicked who do me violence , my deadly enemies who surround me .
- **Psa 68:28** (—) *target: which*
  > Psa 68:28 Summon your power , O God , the power , O God , by which you have worked for us .

### `H5971B` — 20/30 classified · 2 anchor verse(s)

**Group `5733-001`** (20 verses — anchors: Gen 25:8, Lev 17:10)

- **Gen 25:8** 🔵 (✓) *target: people*
  > Gen 25:8 Abraham breathed his last and died in a good old age , an old man and full of years, and was gathered to his people .
- **Lev 17:10** 🔵 (✓) *target: people*
  > Lev 17:10 “If any one of the house of Israel or of the strangers who sojourn among them eats any blood , I will set my face against that person who eats blood and will cut him off from among his people .
- **Gen 17:14** (✓) *target: people*
  > Gen 17:14 Any uncircumcised male who is not circumcised in the flesh of his foreskin shall be cut off from his people ; he has broken my covenant .”
- **Gen 25:17** (✓) *target: people*
  > Gen 25:17 (These are the years of the life of Ishmael : 137 years . He breathed his last and died , and was gathered to his people .)
- **Gen 35:29** (✓) *target: people*
  > Gen 35:29 And Isaac breathed his last , and he died and was gathered to his people , old and full of days . And his sons Esau and Jacob buried him.
- **Gen 49:29** (✓) *target: people*
  > Gen 49:29 Then he commanded them and said to them, “ I am to be gathered to my people ; bury me with my fathers in the cave that is in the field of Ephron the Hittite ,
- **Gen 49:33** (✓) *target: people*
  > Gen 49:33 When Jacob finished commanding his sons , he drew up his feet into the bed and breathed his last and was gathered to his people .
- **Exo 31:14** (✓) *target: people*
  > Exo 31:14 You shall keep the Sabbath , because it is holy for you. Everyone who profanes it shall be put to death . Whoever does any work on it, that soul shall be cut off from among his people .
- **Lev 7:20** (✓) *target: people*
  > Lev 7:20 but the person who eats of the flesh of the sacrifice of the Lord’s peace offerings while an uncleanness is on him, that person shall be cut off from his people .
- **Lev 7:21** (✓) *target: people*
  > Lev 7:21 And if anyone touches an unclean thing , whether human uncleanness or an unclean beast or any unclean detestable creature, and then eats some flesh from the sacrifice of the Lord’s peace offerings , that person shall be cut off from his people .”
- **Lev 7:25** (✓) *target: people*
  > Lev 7:25 For every person who eats of the fat of an animal of which a food offering may be made to the Lord shall be cut off from his people .
- **Lev 7:27** (✓) *target: people*
  > Lev 7:27 Whoever eats any blood , that person shall be cut off from his people .”
- **Lev 17:4** (✓) *target: people*
  > Lev 17:4 and does not bring it to the entrance of the tent of meeting to offer it as a gift to the Lord in front of the tabernacle of the Lord , bloodguilt shall be imputed to that man . He has shed blood , and that man shall be cut off from among his people .
- **Lev 17:9** (✓) *target: people*
  > Lev 17:9 and does not bring it to the entrance of the tent of meeting to offer it to the Lord , that man shall be cut off from his people .
- **Lev 18:29** (✓) *target: people*
  > Lev 18:29 For everyone who does any of these abominations , the persons who do them shall be cut off from among their people .
- **Lev 19:8** (✓) *target: people*
  > Lev 19:8 and everyone who eats it shall bear his iniquity , because he has profaned what is holy to the Lord , and that person shall be cut off from his people .
- **Lev 23:29** (✓) *target: people*
  > Lev 23:29 For whoever is not afflicted on that very day shall be cut off from his people .
- **Num 9:13** (✓) *target: people*
  > Num 9:13 But if anyone who is clean and is not on a journey fails to keep the Passover , that person shall be cut off from his people because he did not bring the Lord’s offering at its appointed time ; that man shall bear his sin .
- **Num 20:24** (✓) *target: people*
  > Num 20:24 “Let Aaron be gathered to his people , for he shall not enter the land that I have given to the people of Israel , because you rebelled against my command at the waters of Meribah .
- **Deu 32:50** (✓) *target: people*
  > Deu 32:50 And die on the mountain which you go up , and be gathered to your people , as Aaron your brother died in Mount Hor and was gathered to his people ,

**Group `UNCLASSIFIED`** (10 verses)

- **Lev 21:1** (—) *target: people*
  > Lev 21:1 And the Lord said to Moses , “ Speak to the priests , the sons of Aaron , and say to them, No one shall make himself unclean for the dead among his people ,
- **Lev 21:4** (—) *target: people*
  > Lev 21:4 He shall not make himself unclean as a husband among his people and so profane himself.
- **Lev 21:14** (—) *target: people*
  > Lev 21:14 A widow , or a divorced woman , or a woman who has been defiled , or a prostitute , these he shall not marry . But he shall take as his wife a virgin of his own people ,
- **Lev 21:15** (—) *target: people*
  > Lev 21:15 that he may not profane his offspring among his people , for I am the Lord who sanctifies him .”
- **Num 27:13** (—) *target: people*
  > Num 27:13 When you have seen it, you also shall be gathered to your people , as your brother Aaron was ,
- **Num 31:2** (—) *target: people*
  > Num 31:2 “ Avenge the people of Israel on the Midianites . Afterward you shall be gathered to your people .”
- **Judg 5:14** (—) *target: kinsmen*
  > Judg 5:14 From Ephraim their root they marched down into the valley , following you, Benjamin , with your kinsmen ; from Machir marched down the commanders , and from Zebulun those who bear the lieutenant’s staff ;
- **Judg 14:3** (—) *target: people*
  > Judg 14:3 But his father and mother said to him, “Is there not a woman among the daughters of your relatives , or among all our people , that you must go to take a wife from the uncircumcised Philistines ?” But Samson said to his father , “ Get her for me, for she is right in my eyes .”
- **2Ki 4:13** (—) *target: people*
  > 2Ki 4:13 And he said to him, “ Say now to her, ‘ See , you have taken all this trouble for us; what is to be done for you? Would you have a word spoken on your behalf to the king or to the commander of the army ?’” She answered , “ I dwell among my own people .”
- **Eze 18:18** (—) *target: people*
  > Eze 18:18 As for his father , because he practiced extortion , robbed his brother , and did what is not good among his people , behold , he shall die for his iniquity .

### `H5971H` — 430/430 classified · 5 anchor verse(s)

**Group `5737-001`** (427 verses — anchors: Num 11:29, Num 14:19)

- **Num 11:29** 🔵 (✓) *target: people*
  > Num 11:29 But Moses said to him, “Are you jealous for my sake? Would that all the Lord’s people were prophets , that the Lord would put his Spirit on them !”
- **Num 14:19** 🔵 (✓) *target: people*
  > Num 14:19 Please pardon the iniquity of this people , according to the greatness of your steadfast love , just as you have forgiven this people , from Egypt until now .”
- **Gen 11:6** (✓) *target: people*
  > Gen 11:6 And the Lord said , “Behold, they are one people , and they have all one language , and this is only the beginning of what they will do . And nothing that they propose to do will now be impossible for them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 14:16** (✓) *target: people*
  > Gen 14:16 Then he brought back all the possessions , and also brought back his kinsman Lot with his possessions , and the women and the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 17:16** (✓) *target: peoples*
  > Gen 17:16 I will bless her , and moreover , I will give you a son by her. I will bless her, and she shall become nations ; kings of peoples shall come from her .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 19:4** (✓) *target: people*
  > Gen 19:4 But before they lay down , the men of the city , the men of Sodom , both young and old , all the people to the last man , surrounded the house .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:7** (✓) *target: people*
  > Gen 23:7 Abraham rose and bowed to the Hittites , the people of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:11** (✓) *target: people*
  > Gen 23:11 “ No , my lord , hear me : I give you the field , and I give you the cave that is in it. In the sight of the sons of my people I give it to you. Bury your dead .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:12** (✓) *target: people*
  > Gen 23:12 Then Abraham bowed down before the people of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:13** (✓) *target: people*
  > Gen 23:13 And he said to Ephron in the hearing of the people of the land , “But if you will, hear me: I give the price of the field . Accept it from me, that I may bury my dead there .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 26:10** (✓) *target: people*
  > Gen 26:10 Abimelech said , “ What is this you have done to us? One of the people might easily have lain with your wife , and you would have brought guilt upon us.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 26:11** (✓) *target: people*
  > Gen 26:11 So Abimelech warned all the people , saying , “Whoever touches this man or his wife shall surely be put to death .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 27:29** (✓) *target: peoples*
  > Gen 27:29 Let peoples serve you, and nations bow down to you. Be lord over your brothers , and may your mother’s sons bow down to you. Cursed be everyone who curses you, and blessed be everyone who blesses you!”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 28:3** (✓) *target: peoples*
  > Gen 28:3 God Almighty bless you and make you fruitful and multiply you, that you may become a company of peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 32:7** (✓) *target: people*
  > Gen 32:7 Then Jacob was greatly afraid and distressed . He divided the people who were with him, and the flocks and herds and camels , into two camps ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 33:15** (✓) *target: people*
  > Gen 33:15 So Esau said , “ Let me leave with you some of the people who are with me.” But he said , “ What need is there ? Let me find favor in the sight of my lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 34:16** (✓) *target: people*
  > Gen 34:16 Then we will give our daughters to you, and we will take your daughters to ourselves, and we will dwell with you and become one people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 34:22** (✓) *target: people*
  > Gen 34:22 Only on this condition will the men agree to dwell with us to become one people —when every male among us is circumcised as they are circumcised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 35:6** (✓) *target: people*
  > Gen 35:6 And Jacob came to Luz (that is, Bethel ), which is in the land of Canaan , he and all the people who were with him ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 41:40** (✓) *target: people*
  > Gen 41:40 You shall be over my house , and all my people shall order themselves as you command . Only as regards the throne will I be greater than you .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 41:55** (✓) *target: people*
  > Gen 41:55 When all the land of Egypt was famished , the people cried to Pharaoh for bread . Pharaoh said to all the Egyptians , “ Go to Joseph . What he says to you, do .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 42:6** (✓) *target: people*
  > Gen 42:6 Now Joseph was governor over the land . He was the one who sold to all the people of the land . And Joseph’s brothers came and bowed themselves before him with their faces to the ground .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 47:21** (✓) *target: people*
  > Gen 47:21 As for the people , he made servants of them from one end of Egypt to the other .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 47:23** (✓) *target: people*
  > Gen 47:23 Then Joseph said to the people , “ Behold , I have this day bought you and your land for Pharaoh . Now here is seed for you, and you shall sow the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 48:4** (✓) *target: peoples*
  > Gen 48:4 and said to me, ‘ Behold , I will make you fruitful and multiply you, and I will make of you a company of peoples and will give this land to your offspring after you for an everlasting possession .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 48:19** (✓) *target: people*
  > Gen 48:19 But his father refused and said , “I know , my son , I know . He also shall become a people , and he also shall be great . Nevertheless , his younger brother shall be greater than he, and his offspring shall become a multitude of nations .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 49:10** (✓) *target: peoples*
  > Gen 49:10 The scepter shall not depart from Judah , nor the ruler’s staff from between his feet , until tribute comes to him; and to him shall be the obedience of the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 49:16** (✓) *target: people*
  > Gen 49:16 “ Dan shall judge his people as one of the tribes of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 50:20** (✓) *target: people*
  > Gen 50:20 As for you , you meant evil against me, but God meant it for good , to bring it about that many people should be kept alive , as they are today .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:9** (✓) *target: people*
  > Exo 1:9 And he said to his people , “ Behold , the people of Israel are too many and too mighty for us .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:20** (✓) *target: people*
  > Exo 1:20 So God dealt well with the midwives . And the people multiplied and grew very strong .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:22** (✓) *target: people*
  > Exo 1:22 Then Pharaoh commanded all his people , “ Every son that is born to the Hebrews you shall cast into the Nile , but you shall let every daughter live .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:7** (✓) *target: people*
  > Exo 3:7 Then the Lord said , “I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters . I know their sufferings ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:10** (✓) *target: people*
  > Exo 3:10 Come , I will send you to Pharaoh that you may bring my people , the children of Israel , out of Egypt .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:12** (✓) *target: people*
  > Exo 3:12 He said , “ But I will be with you, and this shall be the sign for you, that I have sent you: when you have brought the people out of Egypt , you shall serve God on this mountain .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:21** (✓) *target: people*
  > Exo 3:21 And I will give this people favor in the sight of the Egyptians ; and when you go , you shall not go empty ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:16** (✓) *target: people*
  > Exo 4:16 He shall speak for you to the people , and he shall be your mouth , and you shall be as God to him.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:21** (✓) *target: people*
  > Exo 4:21 And the Lord said to Moses , “ When you go back to Egypt , see that you do before Pharaoh all the miracles that I have put in your power . But I will harden his heart , so that he will not let the people go .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:30** (✓) *target: people*
  > Exo 4:30 Aaron spoke all the words that the Lord had spoken to Moses and did the signs in the sight of the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:31** (✓) *target: people*
  > Exo 4:31 And the people believed ; and when they heard that the Lord had visited the people of Israel and that he had seen their affliction , they bowed their heads and worshiped .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:1** (✓) *target: people*
  > Exo 5:1 Afterward Moses and Aaron went and said to Pharaoh , “Thus says the Lord , the God of Israel , ‘Let my people go , that they may hold a feast to me in the wilderness .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:4** (✓) *target: people*
  > Exo 5:4 But the king of Egypt said to them, “ Moses and Aaron , why do you take the people away from their work ? Get back to your burdens .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:5** (✓) *target: people*
  > Exo 5:5 And Pharaoh said , “ Behold , the people of the land are now many , and you make them rest from their burdens !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:6** (✓) *target: people*
  > Exo 5:6 The same day Pharaoh commanded the taskmasters of the people and their foremen ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:7** (✓) *target: people*
  > Exo 5:7 “You shall no longer give the people straw to make bricks , as in the past ; let them go and gather straw for themselves.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:10** (✓) *target: people*
  > Exo 5:10 So the taskmasters and the foremen of the people went out and said to the people , “Thus says Pharaoh , ‘ I will not give you straw .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:12** (✓) *target: people*
  > Exo 5:12 So the people were scattered throughout all the land of Egypt to gather stubble for straw .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:16** (✓) *target: people*
  > Exo 5:16 No straw is given to your servants , yet they say to us, ‘ Make bricks !’ And behold, your servants are beaten ; but the fault is in your own people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:22** (✓) *target: people*
  > Exo 5:22 Then Moses turned to the Lord and said , “O Lord , why have you done evil to this people ? Why did you ever send me ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:23** (✓) *target: people*
  > Exo 5:23 For since I came to Pharaoh to speak in your name , he has done evil to this people , and you have not delivered your people at all .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 6:7** (✓) *target: people*
  > Exo 6:7 I will take you to be my people , and I will be your God , and you shall know that I am the Lord your God , who has brought you out from under the burdens of the Egyptians .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 7:4** (✓) *target: people*
  > Exo 7:4 Pharaoh will not listen to you. Then I will lay my hand on Egypt and bring my hosts , my people the children of Israel , out of the land of Egypt by great acts of judgment .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 7:16** (✓) *target: people*
  > Exo 7:16 And you shall say to him, ‘The Lord , the God of the Hebrews , sent me to you, saying , “Let my people go , that they may serve me in the wilderness .” But so far , you have not obeyed .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:1** (✓) *target: people*
  > Exo 8:1 Then the Lord said to Moses , “ Go in to Pharaoh and say to him, ‘ Thus says the Lord , “Let my people go , that they may serve me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:3** (✓) *target: people*
  > Exo 8:3 The Nile shall swarm with frogs that shall come up into your house and into your bedroom and on your bed and into the houses of your servants and your people , and into your ovens and your kneading bowls .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:4** (✓) *target: people*
  > Exo 8:4 The frogs shall come up on you and on your people and on all your servants .”’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:8** (✓) *target: people*
  > Exo 8:8 Then Pharaoh called Moses and Aaron and said , “ Plead with the Lord to take away the frogs from me and from my people , and I will let the people go to sacrifice to the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:9** (✓) *target: people*
  > Exo 8:9 Moses said to Pharaoh , “Be pleased to command me when I am to plead for you and for your servants and for your people , that the frogs be cut off from you and your houses and be left only in the Nile .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:11** (✓) *target: people*
  > Exo 8:11 The frogs shall go away from you and your houses and your servants and your people . They shall be left only in the Nile .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:20** (✓) *target: people*
  > Exo 8:20 Then the Lord said to Moses , “Rise up early in the morning and present yourself to Pharaoh , as he goes out to the water , and say to him, ‘ Thus says the Lord , “Let my people go , that they may serve me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:21** (✓) *target: people*
  > Exo 8:21 Or else, if you will not let my people go , behold, I will send swarms of flies on you and your servants and your people , and into your houses . And the houses of the Egyptians shall be filled with swarms of flies , and also the ground on which they stand.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 5:21** (✓) *target: people*
  > Num 5:21 then’ (let the priest make the woman take the oath of the curse , and say to the woman ) ‘the Lord make you a curse and an oath among your people , when the Lord makes your thigh fall away and your body swell .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 5:27** (✓) *target: people*
  > Num 5:27 And when he has made her drink the water , then, if she has defiled herself and has broken faith with her husband , the water that brings the curse shall enter into her and cause bitter pain , and her womb shall swell , and her thigh shall fall away , and the woman shall become a curse among her people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:1** (✓) *target: people*
  > Num 11:1 And the people complained in the hearing of the Lord about their misfortunes , and when the Lord heard it, his anger was kindled , and the fire of the Lord burned among them and consumed some outlying parts of the camp .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:2** (✓) *target: people*
  > Num 11:2 Then the people cried out to Moses , and Moses prayed to the Lord , and the fire died down .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:8** (✓) *target: people*
  > Num 11:8 The people went about and gathered it and ground it in handmills or beat it in mortars and boiled it in pots and made cakes of it. And the taste of it was like the taste of cakes baked with oil .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:10** (✓) *target: people*
  > Num 11:10 Moses heard the people weeping throughout their clans , everyone at the door of his tent . And the anger of the Lord blazed hotly , and Moses was displeased .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:11** (✓) *target: people*
  > Num 11:11 Moses said to the Lord , “ Why have you dealt ill with your servant ? And why have I not found favor in your sight , that you lay the burden of all this people on me ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:12** (✓) *target: people*
  > Num 11:12 Did I conceive all this people ? Did I give them birth , that you should say to me, ‘ Carry them in your bosom , as a nurse carries a nursing child ,’ to the land that you swore to give their fathers ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:13** (✓) *target: people*
  > Num 11:13 Where am I to get meat to give to all this people ? For they weep before me and say , ‘ Give us meat , that we may eat .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:14** (✓) *target: people*
  > Num 11:14 I am not able to carry all this people alone ; the burden is too heavy for me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:16** (✓) *target: people*
  > Num 11:16 Then the Lord said to Moses , “ Gather for me seventy men of the elders of Israel , whom you know to be the elders of the people and officers over them, and bring them to the tent of meeting , and let them take their stand there with you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:17** (✓) *target: people*
  > Num 11:17 And I will come down and talk with you there . And I will take some of the Spirit that is on you and put it on them, and they shall bear the burden of the people with you, so that you may not bear it yourself alone .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:18** (✓) *target: people*
  > Num 11:18 And say to the people , ‘ Consecrate yourselves for tomorrow , and you shall eat meat , for you have wept in the hearing of the Lord , saying , “ Who will give us meat to eat ? For it was better for us in Egypt .” Therefore the Lord will give you meat , and you shall eat .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:21** (✓) *target: people*
  > Num 11:21 But Moses said , “The people among whom I am number six hundred thousand on foot , and you have said , ‘I will give them meat , that they may eat a whole month !’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:24** (✓) *target: people*
  > Num 11:24 So Moses went out and told the people the words of the Lord . And he gathered seventy men of the elders of the people and placed them around the tent .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:32** (✓) *target: people*
  > Num 11:32 And the people rose all that day and all night and all the next day , and gathered the quail . Those who gathered least gathered ten homers . And they spread them out for themselves all around the camp .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:33** (✓) *target: people*
  > Num 11:33 While the meat was yet between their teeth , before it was consumed , the anger of the Lord was kindled against the people , and the Lord struck down the people with a very great plague .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:34** (✓) *target: people*
  > Num 11:34 Therefore the name of that place was called Kibroth-hattaavah , because there they buried the people who had the craving .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:35** (✓) *target: people*
  > Num 11:35 From Kibroth-hattaavah the people journeyed to Hazeroth , and they remained at Hazeroth .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 12:15** (✓) *target: people*
  > Num 12:15 So Miriam was shut outside the camp seven days , and the people did not set out on the march till Miriam was brought in again.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 12:16** (✓) *target: people*
  > Num 12:16 After that the people set out from Hazeroth , and camped in the wilderness of Paran .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:18** (✓) *target: people*
  > Num 13:18 and see what the land is, and whether the people who dwell in it are strong or weak , whether they are few or many ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:28** (✓) *target: people*
  > Num 13:28 However , the people who dwell in the land are strong , and the cities are fortified and very large . And besides , we saw the descendants of Anak there .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:30** (✓) *target: people*
  > Num 13:30 But Caleb quieted the people before Moses and said , “Let us go up at once and occupy it, for we are well able to overcome it .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:31** (✓) *target: people*
  > Num 13:31 Then the men who had gone up with him said , “We are not able to go up against the people , for they are stronger than we are.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:32** (✓) *target: people*
  > Num 13:32 So they brought to the people of Israel a bad report of the land that they had spied out , saying , “The land , through which we have gone to spy it out , is a land that devours its inhabitants , and all the people that we saw in it are of great height .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:1** (✓) *target: people*
  > Num 14:1 Then all the congregation raised a loud cry , and the people wept that night .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:13** (✓) *target: people*
  > Num 14:13 But Moses said to the Lord , “Then the Egyptians will hear of it, for you brought up this people in your might from among them,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:14** (✓) *target: people*
  > Num 14:14 and they will tell the inhabitants of this land . They have heard that you , O Lord , are in the midst of this people . For you , O Lord , are seen face to face , and your cloud stands over them and you go before them, in a pillar of cloud by day and in a pillar of fire by night .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:15** (✓) *target: people*
  > Num 14:15 Now if you kill this people as one man , then the nations who have heard your fame will say ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:16** (✓) *target: people*
  > Num 14:16 ‘It is because the Lord was not able to bring this people into the land that he swore to give to them that he has killed them in the wilderness .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:39** (✓) *target: people*
  > Num 14:39 When Moses told these words to all the people of Israel , the people mourned greatly .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 15:26** (✓) *target: population*
  > Num 15:26 And all the congregation of the people of Israel shall be forgiven , and the stranger who sojourns among them, because the whole population was involved in the mistake .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 15:30** (✓) *target: people*
  > Num 15:30 But the person who does anything with a high hand , whether he is native or a sojourner , reviles the Lord , and that person shall be cut off from among his people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 16:41** (✓) *target: people*
  > Num 16:41 But on the next day all the congregation of the people of Israel grumbled against Moses and against Aaron , saying , “ You have killed the people of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 16:47** (✓) *target: people*
  > Num 16:47 So Aaron took it as Moses said and ran into the midst of the assembly . And behold , the plague had already begun among the people . And he put on the incense and made atonement for the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 20:1** (✓) *target: people*
  > Num 20:1 And the people of Israel , the whole congregation , came into the wilderness of Zin in the first month , and the people stayed in Kadesh . And Miriam died there and was buried there .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 20:3** (✓) *target: people*
  > Num 20:3 And the people quarreled with Moses and said , “Would that we had perished when our brothers perished before the Lord !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:2** (✓) *target: people*
  > Num 21:2 And Israel vowed a vow to the Lord and said , “ If you will indeed give this people into my hand , then I will devote their cities to destruction.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:4** (✓) *target: people*
  > Num 21:4 From Mount Hor they set out by the way to the Red Sea , to go around the land of Edom . And the people became impatient on the way .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:5** (✓) *target: people*
  > Num 21:5 And the people spoke against God and against Moses , “ Why have you brought us up out of Egypt to die in the wilderness ? For there is no food and no water , and we loathe this worthless food .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:6** (✓) *target: people*
  > Num 21:6 Then the Lord sent fiery serpents among the people , and they bit the people , so that many people of Israel died .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:7** (✓) *target: people*
  > Num 21:7 And the people came to Moses and said , “We have sinned , for we have spoken against the Lord and against you. Pray to the Lord , that he take away the serpents from us.” So Moses prayed for the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:16** (✓) *target: people*
  > Num 21:16 And from there they continued to Beer ; that is the well of which the Lord said to Moses , “ Gather the people together, so that I may give them water .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:18** (✓) *target: people*
  > Num 21:18 the well that the princes made , that the nobles of the people dug , with the scepter and with their staffs .” And from the wilderness they went on to Mattanah ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:23** (✓) *target: people*
  > Num 21:23 But Sihon would not allow Israel to pass through his territory . He gathered all his people together and went out against Israel to the wilderness and came to Jahaz and fought against Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:29** (✓) *target: people*
  > Num 21:29 Woe to you, O Moab ! You are undone , O people of Chemosh ! He has made his sons fugitives , and his daughters captives , to an Amorite king , Sihon .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:33** (✓) *target: people*
  > Num 21:33 Then they turned and went up by the way to Bashan . And Og the king of Bashan came out against them , he and all his people , to battle at Edrei .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:34** (✓) *target: people*
  > Num 21:34 But the Lord said to Moses , “Do not fear him, for I have given him into your hand , and all his people , and his land . And you shall do to him as you did to Sihon king of the Amorites , who lived at Heshbon .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:35** (✓) *target: people*
  > Num 21:35 So they defeated him and his sons and all his people , until he had no survivor left . And they possessed his land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:3** (✓) *target: people*
  > Num 22:3 And Moab was in great dread of the people , because they were many . Moab was overcome with fear of the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:5** (✓) *target: Amaw*
  > Num 22:5 sent messengers to Balaam the son of Beor at Pethor , which is near the River in the land of the people of Amaw , to call him, saying , “ Behold , a people has come out of Egypt . They cover the face of the earth , and they are dwelling opposite me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:6** (✓) *target: people*
  > Num 22:6 Come now , curse this people for me, since they are too mighty for me. Perhaps I shall be able to defeat them and drive them from the land , for I know that he whom you bless is blessed , and he whom you curse is cursed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:11** (✓) *target: people*
  > Num 22:11 ‘ Behold , a people has come out of Egypt , and it covers the face of the earth . Now come , curse them for me. Perhaps I shall be able to fight against them and drive them out.’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:12** (✓) *target: people*
  > Num 22:12 God said to Balaam , “You shall not go with them. You shall not curse the people , for they are blessed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:17** (✓) *target: people*
  > Num 22:17 for I will surely do you great honor, and whatever you say to me I will do. Come , curse this people for me.’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:2** (✓) *target: people*
  > Jos 1:2 “ Moses my servant is dead . Now therefore arise , go over this Jordan , you and all this people , into the land that I am giving to them, to the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:6** (✓) *target: people*
  > Jos 1:6 Be strong and courageous , for you shall cause this people to inherit the land that I swore to their fathers to give them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:10** (✓) *target: people*
  > Jos 1:10 And Joshua commanded the officers of the people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:11** (✓) *target: people*
  > Jos 1:11 “ Pass through the midst of the camp and command the people , ‘ Prepare your provisions , for within three days you are to pass over this Jordan to go in to take possession of the land that the Lord your God is giving you to possess .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:3** (✓) *target: people*
  > Jos 3:3 and commanded the people , “ As soon as you see the ark of the covenant of the Lord your God being carried by the Levitical priests , then you shall set out from your place and follow it .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:5** (✓) *target: people*
  > Jos 3:5 Then Joshua said to the people , “ Consecrate yourselves, for tomorrow the Lord will do wonders among you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:6** (✓) *target: people*
  > Jos 3:6 And Joshua said to the priests , “Take up the ark of the covenant and pass on before the people .” So they took up the ark of the covenant and went before the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:14** (✓) *target: people*
  > Jos 3:14 So when the people set out from their tents to pass over the Jordan with the priests bearing the ark of the covenant before the people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:16** (✓) *target: people*
  > Jos 3:16 the waters coming down from above stood and rose up in a heap very far away, at Adam , the city that is beside Zarethan , and those flowing down toward the Sea of the Arabah , the Salt Sea , were completely cut off . And the people passed over opposite Jericho .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:2** (✓) *target: people*
  > Jos 4:2 “ Take twelve men from the people , from each tribe a man ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:10** (✓) *target: people*
  > Jos 4:10 For the priests bearing the ark stood in the midst of the Jordan until everything was finished that the Lord commanded Joshua to tell the people , according to all that Moses had commanded Joshua . The people passed over in haste .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:11** (✓) *target: people*
  > Jos 4:11 And when all the people had finished passing over , the ark of the Lord and the priests passed over before the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:19** (✓) *target: people*
  > Jos 4:19 The people came up out of the Jordan on the tenth day of the first month , and they encamped at Gilgal on the east border of Jericho .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:24** (✓) *target: peoples*
  > Jos 4:24 so that all the peoples of the earth may know that the hand of the Lord is mighty , that you may fear the Lord your God forever .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 5:4** (✓) *target: people*
  > Jos 5:4 And this is the reason why Joshua circumcised them: all the males of the people who came out of Egypt , all the men of war , had died in the wilderness on the way after they had come out of Egypt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 5:5** (✓) *target: people*
  > Jos 5:5 Though all the people who came out had been circumcised , yet all the people who were born on the way in the wilderness after they had come out of Egypt had not been circumcised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:5** (✓) *target: people*
  > Jos 6:5 And when they make a long blast with the ram’s horn , when you hear the sound of the trumpet , then all the people shall shout with a great shout , and the wall of the city will fall down flat , and the people shall go up , everyone straight before him .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:7** (✓) *target: people*
  > Jos 6:7 And he said to the people , “Go forward . March around the city and let the armed men pass on before the ark of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:8** (✓) *target: people*
  > Jos 6:8 And just as Joshua had commanded the people , the seven priests bearing the seven trumpets of rams’ horns before the Lord went forward , blowing the trumpets , with the ark of the covenant of the Lord following them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:10** (✓) *target: people*
  > Jos 6:10 But Joshua commanded the people , “You shall not shout or make your voice heard , neither shall any word go out of your mouth , until the day I tell you to shout . Then you shall shout .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:16** (✓) *target: people*
  > Jos 6:16 And at the seventh time , when the priests had blown the trumpets , Joshua said to the people , “ Shout , for the Lord has given you the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:20** (✓) *target: people*
  > Jos 6:20 So the people shouted , and the trumpets were blown . As soon as the people heard the sound of the trumpet , the people shouted a great shout , and the wall fell down flat , so that the people went up into the city , every man straight before him, and they captured the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:3** (✓) *target: people*
  > Jos 7:3 And they returned to Joshua and said to him, “Do not have all the people go up , but let about two or three thousand men go up and attack Ai . Do not make the whole people toil up there , for they are few .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:4** (✓) *target: people*
  > Jos 7:4 So about three thousand men went up there from the people . And they fled before the men of Ai ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:5** (✓) *target: people*
  > Jos 7:5 and the men of Ai killed about thirty-six of their men and chased them before the gate as far as Shebarim and struck them at the descent . And the hearts of the people melted and became as water .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:7** (✓) *target: people*
  > Jos 7:7 And Joshua said , “ Alas , O Lord God , why have you brought this people over the Jordan at all, to give us into the hands of the Amorites , to destroy us? Would that we had been content to dwell beyond the Jordan !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:13** (✓) *target: people*
  > Jos 7:13 Get up ! Consecrate the people and say , ‘ Consecrate yourselves for tomorrow ; for thus says the Lord , God of Israel , “There are devoted things in your midst , O Israel . You cannot stand before your enemies until you take away the devoted things from among you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:1** (✓) *target: men*
  > Jos 8:1 And the Lord said to Joshua , “Do not fear and do not be dismayed . Take all the fighting men with you, and arise , go up to Ai . See , I have given into your hand the king of Ai , and his people , his city , and his land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:5** (✓) *target: people*
  > Jos 8:5 And I and all the people who are with me will approach the city . And when they come out against us just as before , we shall flee before them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:9** (✓) *target: people*
  > Jos 8:9 So Joshua sent them out . And they went to the place of ambush and lay between Bethel and Ai , to the west of Ai , but Joshua spent that night among the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:10** (✓) *target: people*
  > Jos 8:10 Joshua arose early in the morning and mustered the people and went up , he and the elders of Israel , before the people to Ai .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:14** (✓) *target: people*
  > Jos 8:14 And as soon as the king of Ai saw this, he and all his people , the men of the city , hurried and went out early to the appointed place toward the Arabah to meet Israel in battle . But he did not know that there was an ambush against him behind the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:16** (✓) *target: people*
  > Jos 8:16 So all the people who were in the city were called together to pursue them, and as they pursued Joshua they were drawn away from the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:20** (✓) *target: people*
  > Jos 8:20 So when the men of Ai looked back , behold , the smoke of the city went up to heaven , and they had no power to flee this way or that, for the people who fled to the wilderness turned back against the pursuers .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:33** (✓) *target: people*
  > Jos 8:33 And all Israel , sojourner as well as native born , with their elders and officers and their judges , stood on opposite sides of the ark before the Levitical priests who carried the ark of the covenant of the Lord , half of them in front of Mount Gerizim and half of them in front of Mount Ebal , just as Moses the servant of the Lord had commanded at the first, to bless the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:7** (✓) *target: people*
  > Jos 10:7 So Joshua went up from Gilgal , he and all the people of war with him, and all the mighty men of valor .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:21** (✓) *target: people*
  > Jos 10:21 then all the people returned safe to Joshua in the camp at Makkedah . Not a man moved his tongue against any of the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:33** (✓) *target: people*
  > Jos 10:33 Then Horam king of Gezer came up to help Lachish . And Joshua struck him and his people , until he left none remaining .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 14:8** (✓) *target: people*
  > Jos 14:8 But my brothers who went up with me made the heart of the people melt ; yet I wholly followed the Lord my God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:14** (✓) *target: people*
  > Jos 17:14 Then the people of Joseph spoke to Joshua , saying , “ Why have you given me but one lot and one portion as an inheritance , although I am a numerous people , since all along the Lord has blessed me?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:15** (✓) *target: people*
  > Jos 17:15 And Joshua said to them, “ If you are a numerous people , go up by yourselves to the forest , and there clear ground for yourselves in the land of the Perizzites and the Rephaim , since the hill country of Ephraim is too narrow for you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:17** (✓) *target: people*
  > Jos 17:17 Then Joshua said to the house of Joseph , to Ephraim and Manasseh , “You are a numerous people and have great power . You shall not have one allotment only,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:2** (✓) *target: people*
  > Jos 24:2 And Joshua said to all the people , “Thus says the Lord , the God of Israel , ‘ Long ago , your fathers lived beyond the Euphrates , Terah , the father of Abraham and of Nahor ; and they served other gods .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:16** (✓) *target: people*
  > Jos 24:16 Then the people answered , “Far be it from us that we should forsake the Lord to serve other gods ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:17** (✓) *target: peoples*
  > Jos 24:17 for it is the Lord our God who brought us and our fathers up from the land of Egypt , out of the house of slavery , and who did those great signs in our sight and preserved us in all the way that we went , and among all the peoples through whom we passed .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:18** (✓) *target: peoples*
  > Jos 24:18 And the Lord drove out before us all the peoples , the Amorites who lived in the land . Therefore we also will serve the Lord , for he is our God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:19** (✓) *target: people*
  > Jos 24:19 But Joshua said to the people , “You are not able to serve the Lord , for he is a holy God . He is a jealous God ; he will not forgive your transgressions or your sins .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:21** (✓) *target: people*
  > Jos 24:21 And the people said to Joshua , “No, but we will serve the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:22** (✓) *target: people*
  > Jos 24:22 Then Joshua said to the people , “You are witnesses against yourselves that you have chosen the Lord , to serve him.” And they said , “We are witnesses .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:24** (✓) *target: people*
  > Jos 24:24 And the people said to Joshua , “The Lord our God we will serve , and his voice we will obey .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:25** (✓) *target: people*
  > Jos 24:25 So Joshua made a covenant with the people that day , and put in place statutes and rules for them at Shechem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:27** (✓) *target: people*
  > Jos 24:27 And Joshua said to all the people , “Behold, this stone shall be a witness against us, for it has heard all the words of the Lord that he spoke to us. Therefore it shall be a witness against you, lest you deal falsely with your God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:28** (✓) *target: people*
  > Jos 24:28 So Joshua sent the people away, every man to his inheritance .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 1:16** (✓) *target: people*
  > Judg 1:16 And the descendants of the Kenite , Moses ’ father-in-law , went up with the people of Judah from the city of palms into the wilderness of Judah , which lies in the Negeb near Arad , and they went and settled with the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:4** (✓) *target: people*
  > Judg 2:4 As soon as the angel of the Lord spoke these words to all the people of Israel , the people lifted up their voices and wept .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:6** (✓) *target: people*
  > Judg 2:6 When Joshua dismissed the people , the people of Israel went each to his inheritance to take possession of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:7** (✓) *target: people*
  > Judg 2:7 And the people served the Lord all the days of Joshua , and all the days of the elders who outlived Joshua , who had seen all the great work that the Lord had done for Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:12** (✓) *target: peoples*
  > Judg 2:12 And they abandoned the Lord , the God of their fathers , who had brought them out of the land of Egypt . They went after other gods , from among the gods of the peoples who were around them, and bowed down to them. And they provoked the Lord to anger.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 3:18** (✓) *target: people*
  > Judg 3:18 And when Ehud had finished presenting the tribute , he sent away the people who carried the tribute .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 5:2** (✓) *target: people*
  > Judg 5:2 “That the leaders took the lead in Israel , that the people offered themselves willingly , bless the Lord !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 1:3** (✓) *target: people*
  > Ezr 1:3 Whoever is among you of all his people , may his God be with him, and let him go up to Jerusalem , which is in Judah , and rebuild the house of the Lord , the God of Israel — he is the God who is in Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 2:2** (✓) *target: people*
  > Ezr 2:2 They came with Zerubbabel , Jeshua , Nehemiah , Seraiah , Reelaiah , Mordecai , Bilshan , Mispar , Bigvai , Rehum , and Baanah . The number of the men of the people of Israel :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 2:70** (✓) *target: people*
  > Ezr 2:70 Now the priests , the Levites , some of the people , the singers , the gatekeepers , and the temple servants lived in their towns , and all the rest of Israel in their towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:1** (✓) *target: people*
  > Ezr 3:1 When the seventh month came , and the children of Israel were in the towns , the people gathered as one man to Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:3** (✓) *target: peoples*
  > Ezr 3:3 They set the altar in its place , for fear was on them because of the peoples of the lands , and they offered burnt offerings on it to the Lord , burnt offerings morning and evening .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:11** (✓) *target: people*
  > Ezr 3:11 And they sang responsively , praising and giving thanks to the Lord , “ For he is good , for his steadfast love endures forever toward Israel .” And all the people shouted with a great shout when they praised the Lord , because the foundation of the house of the Lord was laid.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:13** (✓) *target: people*
  > Ezr 3:13 so that the people could not distinguish the sound of the joyful shout from the sound of the people’s weeping , for the people shouted with a great shout , and the sound was heard far away .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 4:4** (✓) *target: people*
  > Ezr 4:4 Then the people of the land discouraged the people of Judah and made them afraid to build
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 8:15** (✓) *target: people*
  > Ezr 8:15 I gathered them to the river that runs to Ahava , and there we camped three days . As I reviewed the people and the priests , I found there none of the sons of Levi .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 8:36** (✓) *target: people*
  > Ezr 8:36 They also delivered the king’s commissions to the king’s satraps and to the governors of the province Beyond the River , and they aided the people and the house of God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:1** (✓) *target: people*
  > Ezr 9:1 After these things had been done , the officials approached me and said , “The people of Israel and the priests and the Levites have not separated themselves from the peoples of the lands with their abominations , from the Canaanites , the Hittites , the Perizzites , the Jebusites , the Ammonites , the Moabites , the Egyptians , and the Amorites .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:2** (✓) *target: peoples*
  > Ezr 9:2 For they have taken some of their daughters to be wives for themselves and for their sons , so that the holy race has mixed itself with the peoples of the lands . And in this faithlessness the hand of the officials and chief men has been foremost .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:11** (✓) *target: peoples*
  > Ezr 9:11 which you commanded by your servants the prophets , saying , ‘The land that you are entering , to take possession of it, is a land impure with the impurity of the peoples of the lands , with their abominations that have filled it from end to end with their uncleanness .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:14** (✓) *target: peoples*
  > Ezr 9:14 shall we break your commandments again and intermarry with the peoples who practice these abominations ? Would you not be angry with us until you consumed us, so that there should be no remnant , nor any to escape ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:1** (✓) *target: people*
  > Ezr 10:1 While Ezra prayed and made confession , weeping and casting himself down before the house of God , a very great assembly of men , women , and children , gathered to him out of Israel , for the people wept bitterly .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:2** (✓) *target: peoples*
  > Ezr 10:2 And Shecaniah the son of Jehiel , of the sons of Elam , addressed Ezra : “ We have broken faith with our God and have married foreign women from the peoples of the land , but even now there is hope for Israel in spite of this .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:9** (✓) *target: people*
  > Ezr 10:9 Then all the men of Judah and Benjamin assembled at Jerusalem within the three days . It was the ninth month , on the twentieth day of the month . And all the people sat in the open square before the house of God , trembling because of this matter and because of the heavy rain .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:11** (✓) *target: peoples*
  > Ezr 10:11 Now then make confession to the Lord , the God of your fathers and do his will . Separate yourselves from the peoples of the land and from the foreign wives .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:13** (✓) *target: people*
  > Ezr 10:13 But the people are many , and it is a time of heavy rain ; we cannot stand in the open . Nor is this a task for one day or for two , for we have greatly transgressed in this matter .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 1:8** (✓) *target: among the peoples*
  > Neh 1:8 Remember the word that you commanded your servant Moses , saying , ‘If you are unfaithful , I will scatter you among the peoples ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 1:10** (✓) *target: people*
  > Neh 1:10 They are your servants and your people , whom you have redeemed by your great power and by your strong hand .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:6** (✓) *target: people*
  > Neh 4:6 So we built the wall . And all the wall was joined together to half its height, for the people had a mind to work .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:13** (✓) *target: people*
  > Neh 4:13 So in the lowest parts of the space behind the wall , in open places , I stationed the people by their clans , with their swords , their spears , and their bows .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:14** (✓) *target: people*
  > Neh 4:14 And I looked and arose and said to the nobles and to the officials and to the rest of the people , “Do not be afraid of them . Remember the Lord , who is great and awesome , and fight for your brothers , your sons , your daughters , your wives , and your homes .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:19** (✓) *target: people*
  > Neh 4:19 And I said to the nobles and to the officials and to the rest of the people , “The work is great and widely spread , and we are separated on the wall , far from one another .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:22** (✓) *target: people*
  > Neh 4:22 I also said to the people at that time , “Let every man and his servant pass the night within Jerusalem , that they may be a guard for us by night and may labor by day .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:1** (✓) *target: people*
  > Neh 5:1 Now there arose a great outcry of the people and of their wives against their Jewish brothers .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:13** (✓) *target: people*
  > Neh 5:13 I also shook out the fold of my garment and said , “ So may God shake out every man from his house and from his labor who does not keep this promise . So may he be shaken out and emptied .” And all the assembly said “ Amen ” and praised the Lord . And the people did as they had promised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:15** (✓) *target: people*
  > Neh 5:15 The former governors who were before me laid heavy burdens on the people and took from them for their daily ration forty shekels of silver . Even their servants lorded it over the people . But I did not do so , because of the fear of God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:18** (✓) *target: people*
  > Neh 5:18 Now what was prepared at my expense for each day was one ox and six choice sheep and birds , and every ten days all kinds of wine in abundance . Yet for all this I did not demand the food allowance of the governor , because the service was too heavy on this people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:19** (✓) *target: people*
  > Neh 5:19 Remember for my good , O my God , all that I have done for this people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:4** (✓) *target: people*
  > Neh 7:4 The city was wide and large , but the people within it were few , and no houses had been rebuilt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:5** (✓) *target: people*
  > Neh 7:5 Then my God put it into my heart to assemble the nobles and the officials and the people to be enrolled by genealogy . And I found the book of the genealogy of those who came up at the first , and I found written in it :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:7** (✓) *target: people*
  > Neh 7:7 They came with Zerubbabel , Jeshua , Nehemiah , Azariah , Raamiah , Nahamani , Mordecai , Bilshan , Mispereth , Bigvai , Nehum , Baanah . The number of the men of the people of Israel :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:72** (✓) *target: people*
  > Neh 7:72 And what the rest of the people gave was 20,000 darics of gold , 2,000 minas of silver , and 67 priests ’ garments .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:73** (✓) *target: people*
  > Neh 7:73 So the priests , the Levites , the gatekeepers , the singers , some of the people , the temple servants , and all Israel , lived in their towns . And when the seventh month had come , the people of Israel were in their towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:1** (✓) *target: people*
  > Neh 8:1 And all the people gathered as one man into the square before the Water Gate . And they told Ezra the scribe to bring the Book of the Law of Moses that the Lord had commanded Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:3** (✓) *target: people*
  > Neh 8:3 And he read from it facing the square before the Water Gate from early morning until midday , in the presence of the men and the women and those who could understand . And the ears of all the people were attentive to the Book of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:5** (✓) *target: people*
  > Neh 8:5 And Ezra opened the book in the sight of all the people , for he was above all the people , and as he opened it all the people stood .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:6** (✓) *target: people*
  > Neh 8:6 And Ezra blessed the Lord , the great God , and all the people answered , “ Amen , Amen ,” lifting up their hands . And they bowed their heads and worshiped the Lord with their faces to the ground .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:7** (✓) *target: people*
  > Neh 8:7 Also Jeshua , Bani , Sherebiah , Jamin , Akkub , Shabbethai , Hodiah , Maaseiah , Kelita , Azariah , Jozabad , Hanan , Pelaiah , the Levites , helped the people to understand the Law , while the people remained in their places .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:9** (✓) *target: people*
  > Neh 8:9 And Nehemiah , who was the governor , and Ezra the priest and scribe , and the Levites who taught the people said to all the people , “This day is holy to the Lord your God ; do not mourn or weep .” For all the people wept as they heard the words of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:11** (✓) *target: people*
  > Neh 8:11 So the Levites calmed all the people , saying , “Be quiet , for this day is holy ; do not be grieved .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:12** (✓) *target: people*
  > Neh 8:12 And all the people went their way to eat and drink and to send portions and to make great rejoicing , because they had understood the words that were declared to them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:13** (✓) *target: people*
  > Neh 8:13 On the second day the heads of fathers’ houses of all the people , with the priests and the Levites , came together to Ezra the scribe in order to study the words of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:16** (✓) *target: people*
  > Neh 8:16 So the people went out and brought them and made booths for themselves, each on his roof , and in their courts and in the courts of the house of God , and in the square at the Water Gate and in the square at the Gate of Ephraim .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:10** (✓) *target: people*
  > Neh 9:10 and performed signs and wonders against Pharaoh and all his servants and all the people of his land , for you knew that they acted arrogantly against our fathers. And you made a name for yourself, as it is to this day .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:22** (✓) *target: peoples*
  > Neh 9:22 “And you gave them kingdoms and peoples and allotted to them every corner . So they took possession of the land of Sihon king of Heshbon and the land of Og king of Bashan .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:24** (✓) *target: peoples*
  > Neh 9:24 So the descendants went in and possessed the land , and you subdued before them the inhabitants of the land , the Canaanites , and gave them into their hand , with their kings and the peoples of the land , that they might do with them as they would .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:30** (✓) *target: peoples*
  > Neh 9:30 Many years you bore with them and warned them by your Spirit through your prophets . Yet they would not give ear . Therefore you gave them into the hand of the peoples of the lands .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:32** (✓) *target: people*
  > Neh 9:32 “ Now , therefore, our God , the great , the mighty , and the awesome God , who keeps covenant and steadfast love , let not all the hardship seem little to you that has come upon us, upon our kings , our princes , our priests , our prophets , our fathers , and all your people , since the time of the kings of Assyria until this day .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:14** (✓) *target: people*
  > Neh 10:14 The chiefs of the people : Parosh , Pahath-moab , Elam , Zattu , Bani ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:28** (✓) *target: people*
  > Neh 10:28 “The rest of the people , the priests , the Levites , the gatekeepers , the singers , the temple servants , and all who have separated themselves from the peoples of the lands to the Law of God , their wives , their sons , their daughters , all who have knowledge and understanding ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:30** (✓) *target: peoples*
  > Neh 10:30 We will not give our daughters to the peoples of the land or take their daughters for our sons .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:31** (✓) *target: peoples*
  > Neh 10:31 And if the peoples of the land bring in goods or any grain on the Sabbath day to sell , we will not buy from them on the Sabbath or on a holy day . And we will forgo the crops of the seventh year and the exaction of every debt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:34** (✓) *target: people*
  > Neh 10:34 We, the priests , the Levites , and the people , have likewise cast lots for the wood offering , to bring it into the house of our God , according to our fathers ’ houses , at times appointed , year by year , to burn on the altar of the Lord our God , as it is written in the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:1** (✓) *target: people*
  > Neh 11:1 Now the leaders of the people lived in Jerusalem . And the rest of the people cast lots to bring one out of ten to live in Jerusalem the holy city , while nine out of ten remained in the other towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:2** (✓) *target: people*
  > Neh 11:2 And the people blessed all the men who willingly offered to live in Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:24** (✓) *target: people*
  > Neh 11:24 And Pethahiah the son of Meshezabel , of the sons of Zerah the son of Judah , was at the king’s side in all matters concerning the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 12:30** (✓) *target: people*
  > Neh 12:30 And the priests and the Levites purified themselves, and they purified the people and the gates and the wall .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 12:2** (✓) *target: people*
  > Job 12:2 “No doubt you are the people , and wisdom will die with you.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 12:24** (✓) *target: people*
  > Job 12:24 He takes away understanding from the chiefs of the people of the earth and makes them wander in a trackless waste .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 17:6** (✓) *target: peoples*
  > Job 17:6 “He has made me a byword of the peoples , and I am one before whom men spit .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 18:19** (✓) *target: people*
  > Job 18:19 He has no posterity or progeny among his people , and no survivor where he used to live .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 34:20** (✓) *target: people*
  > Job 34:20 In a moment they die ; at midnight the people are shaken and pass away , and the mighty are taken away by no human hand .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 34:30** (✓) *target: people*
  > Job 34:30 that a godless man should not reign , that he should not ensnare the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 36:20** (✓) *target: peoples*
  > Job 36:20 Do not long for the night , when peoples vanish in their place .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 36:31** (✓) *target: peoples*
  > Job 36:31 For by these he judges peoples ; he gives food in abundance .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 3:6** (✓) *target: people*
  > Psa 3:6 I will not be afraid of many thousands of people who have set themselves against me all around .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 3:8** (✓) *target: people*
  > Psa 3:8 Salvation belongs to the Lord ; your blessing be on your people ! Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 7:8** (✓) *target: peoples*
  > Psa 7:8 The Lord judges the peoples ; judge me, O Lord , according to my righteousness and according to the integrity that is in me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 9:11** (✓) *target: peoples*
  > Psa 9:11 Sing praises to the Lord , who sits enthroned in Zion ! Tell among the peoples his deeds !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 14:4** (✓) *target: people*
  > Psa 14:4 Have they no knowledge , all the evildoers who eat up my people as they eat bread and do not call upon the Lord ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 14:7** (✓) *target: people*
  > Psa 14:7 Oh, that salvation for Israel would come out of Zion ! When the Lord restores the fortunes of his people , let Jacob rejoice , let Israel be glad .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:27** (✓) *target: people*
  > Psa 18:27 For you save a humble people , but the haughty eyes you bring down .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:43** (✓) *target: people*
  > Psa 18:43 You delivered me from strife with the people ; you made me the head of the nations ; people whom I had not known served me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:47** (✓) *target: peoples*
  > Psa 18:47 the God who gave me vengeance and subdued peoples under me ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 22:6** (✓) *target: people*
  > Psa 22:6 But I am a worm and not a man , scorned by mankind and despised by the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 22:31** (✓) *target: people*
  > Psa 22:31 they shall come and proclaim his righteousness to a people yet unborn, that he has done it.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 28:9** (✓) *target: people*
  > Psa 28:9 Oh, save your people and bless your heritage ! Be their shepherd and carry them forever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 29:11** (✓) *target: people*
  > Psa 29:11 May the Lord give strength to his people ! May the Lord bless his people with peace !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 33:10** (✓) *target: peoples*
  > Psa 33:10 The Lord brings the counsel of the nations to nothing ; he frustrates the plans of the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 33:12** (✓) *target: people*
  > Psa 33:12 Blessed is the nation whose God is the Lord , the people whom he has chosen as his heritage !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 35:18** (✓) *target: throng*
  > Psa 35:18 I will thank you in the great congregation ; in the mighty throng I will praise you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 44:12** (✓) *target: people*
  > Psa 44:12 You have sold your people for a trifle , demanding no high price for them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:5** (✓) *target: peoples*
  > Psa 45:5 Your arrows are sharp in the heart of the king’s enemies ; the peoples fall under you.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:10** (✓) *target: people*
  > Psa 45:10 Hear , O daughter , and consider , and incline your ear : forget your people and your father’s house ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:12** (✓) *target: people*
  > Psa 45:12 The people of Tyre will seek your favor with gifts , the richest of the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:17** (✓) *target: nations*
  > Psa 45:17 I will cause your name to be remembered in all generations ; therefore nations will praise you forever and ever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:1** (✓) *target: peoples*
  > To the choirmaster . A Psalm of the Sons of Korah . Psa 47:1 Clap your hands , all peoples ! Shout to God with loud songs of joy !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:3** (✓) *target: peoples*
  > Psa 47:3 He subdued peoples under us, and nations under our feet .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:9** (✓) *target: peoples*
  > Psa 47:9 The princes of the peoples gather as the people of the God of Abraham . For the shields of the earth belong to God ; he is highly exalted !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 49:1** (✓) *target: peoples*
  > To the choirmaster . A Psalm of the Sons of Korah . Psa 49:1 Hear this , all peoples ! Give ear , all inhabitants of the world ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 50:4** (✓) *target: people*
  > Psa 50:4 He calls to the heavens above and to the earth , that he may judge his people :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 50:7** (✓) *target: people*
  > Psa 50:7 “ Hear , O my people , and I will speak ; O Israel , I will testify against you. I am God , your God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 53:4** (✓) *target: people*
  > Psa 53:4 Have those who work evil no knowledge , who eat up my people as they eat bread , and do not call upon God ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 53:6** (✓) *target: people*
  > Psa 53:6 Oh , that salvation for Israel would come out of Zion ! When God restores the fortunes of his people , let Jacob rejoice , let Israel be glad .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 56:7** (✓) *target: peoples*
  > Psa 56:7 For their crime ^ will they escape ? In wrath cast down the peoples , O God !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 57:9** (✓) *target: peoples*
  > Psa 57:9 I will give thanks to you, O Lord , among the peoples ; I will sing praises to you among the nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 59:11** (✓) *target: people*
  > Psa 59:11 Kill them not , lest my people forget ; make them totter by your power and bring them down , O Lord , our shield !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 60:3** (✓) *target: people*
  > Psa 60:3 You have made your people see hard things ; you have given us wine to drink that made us stagger .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 62:8** (✓) *target: people*
  > Psa 62:8 Trust in him at all times , O people ; pour out your heart before him; God is a refuge for us. Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 66:8** (✓) *target: peoples*
  > Psa 66:8 Bless our God , O peoples ; let the sound of his praise be heard ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:3** (✓) *target: peoples*
  > Psa 67:3 Let the peoples praise you, O God ; let all the peoples praise you!
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:4** (✓) *target: peoples*
  > Psa 67:4 Let the nations be glad and sing for joy , for you judge the peoples with equity and guide the nations upon earth . Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:5** (✓) *target: peoples*
  > Psa 67:5 Let the peoples praise you, O God ; let all the peoples praise you!
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:7** (✓) *target: people*
  > Psa 68:7 O God , when you went out before your people , when you marched through the wilderness , Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:30** (✓) *target: peoples*
  > Psa 68:30 Rebuke the beasts that dwell among the reeds , the herd of bulls with the calves of the peoples . Trample underfoot those who lust after tribute ; scatter the peoples who delight in war .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:35** (✓) *target: people*
  > Psa 68:35 Awesome is God from his sanctuary ; the God of Israel — he is the one who gives power and strength to his people . Blessed be God !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:2** (✓) *target: people*
  > Psa 72:2 May he judge your people with righteousness , and your poor with justice !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:3** (✓) *target: people*
  > Psa 72:3 Let the mountains bear prosperity for the people , and the hills , in righteousness !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:4** (✓) *target: people*
  > Psa 72:4 May he defend the cause of the poor of the people , give deliverance to the children of the needy , and crush the oppressor !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 73:10** (✓) *target: people*
  > Psa 73:10 Therefore his people turn back to them , and find no fault in them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 74:18** (✓) *target: people*
  > Psa 74:18 Remember this , O Lord , how the enemy scoffs , and a foolish people reviles your name .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:14** (✓) *target: peoples*
  > Psa 77:14 You are the God who works wonders ; you have made known your might among the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:15** (✓) *target: people*
  > Psa 77:15 You with your arm redeemed your people , the children of Jacob and Joseph . Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:20** (✓) *target: people*
  > Psa 77:20 You led your people like a flock by the hand of Moses and Aaron .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:1** (✓) *target: people*
  > A Maskil of Asaph . Psa 78:1 Give ear , O my people , to my teaching ; incline your ears to the words of my mouth !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:20** (✓) *target: people*
  > Psa 78:20 He struck the rock so that water gushed out and streams overflowed . Can he also give bread or provide meat for his people ?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:52** (✓) *target: people*
  > Psa 78:52 Then he led out his people like sheep and guided them in the wilderness like a flock .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 11:14** (✓) *target: people*
  > Pro 11:14 Where there is no guidance , a people falls , but in an abundance of counselors there is safety .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 14:28** (✓) *target: people*
  > Pro 14:28 In a multitude of people is the glory of a king , but without people a prince is ruined .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 24:24** (✓) *target: peoples*
  > Pro 24:24 Whoever says to the wicked , “You are in the right ,” will be cursed by peoples , abhorred by nations ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 28:15** (✓) *target: people*
  > Pro 28:15 Like a roaring lion or a charging bear is a wicked ruler over a poor people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 29:2** (✓) *target: people*
  > Pro 29:2 When the righteous increase , the people rejoice , but when the wicked rule , the people groan .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 29:18** (✓) *target: people*
  > Pro 29:18 Where there is no prophetic vision the people cast off restraint , but blessed is he who keeps the law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 30:25** (✓) *target: people*
  > Pro 30:25 the ants are a people not strong , yet they provide their food in the summer ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 30:26** (✓) *target: people*
  > Pro 30:26 the rock badgers are a people not mighty , yet they make their homes in the cliffs ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ecc 4:16** (✓) *target: people*
  > Ecc 4:16 There was no end of all the people , all of whom he led . Yet those who come later will not rejoice in him. Surely this also is vanity and a striving after wind .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ecc 12:9** (✓) *target: people*
  > Ecc 12:9 Besides being wise , the Preacher also taught the people knowledge , weighing and studying and arranging many proverbs with great care.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:3** (✓) *target: people*
  > Isa 1:3 The ox knows its owner , and the donkey its master’s crib , but Israel does not know , my people do not understand .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:4** (✓) *target: people*
  > Isa 1:4 Ah , sinful nation , a people laden with iniquity , offspring of evildoers , children who deal corruptly ! They have forsaken the Lord , they have despised the Holy One of Israel , they are utterly estranged.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:10** (✓) *target: people*
  > Isa 1:10 Hear the word of the Lord , you rulers of , Sodom ! Give ear to the teaching of our God , you people of Gomorrah !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:3** (✓) *target: peoples*
  > Isa 2:3 and many peoples shall come , and say : “ Come , let us go up to the mountain of the Lord , to the house of the God of Jacob , that he may teach us his ways and that we may walk in his paths .” For out of Zion shall go forth the law , and the word of the Lord from Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:4** (✓) *target: peoples*
  > Isa 2:4 He shall judge between the nations , and shall decide disputes for many peoples ; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:6** (✓) *target: people*
  > Isa 2:6 For you have rejected your people , the house of Jacob , because they are full of things from the east and of fortune-tellers like the Philistines , and they strike hands with the children of foreigners .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:5** (✓) *target: people*
  > Isa 3:5 And the people will oppress one another, every one his fellow and every one his neighbor ; the youth will be insolent to the elder , and the despised to the honorable .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:7** (✓) *target: people*
  > Isa 3:7 in that day he will speak out , saying : “I will not be a healer ; in my house there is neither bread nor cloak ; you shall not make me leader of the people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:12** (✓) *target: people*
  > Isa 3:12 My people — infants are their oppressors , and women rule over them. O my people , your guides mislead you and they have swallowed up the course of your paths .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:13** (✓) *target: peoples*
  > Isa 3:13 The Lord has taken his place to contend ; he stands to judge peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:14** (✓) *target: people*
  > Isa 3:14 The Lord will enter into judgment with the elders and princes of his people : “ It is you who have devoured the vineyard , the spoil of the poor is in your houses .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:15** (✓) *target: people*
  > Isa 3:15 What do you mean by crushing my people , by grinding the face of the poor ?” declares the Lord God of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 5:13** (✓) *target: people*
  > Isa 5:13 Therefore my people go into exile for lack of knowledge ; their honored men go hungry , and their multitude is parched with thirst .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 5:25** (✓) *target: people*
  > Isa 5:25 Therefore the anger of the Lord was kindled against his people , and he stretched out his hand against them and struck them, and the mountains quaked ; and their corpses were as refuse in the midst of the streets . For all this his anger has not turned away , and his hand is stretched out still .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:5** (✓) *target: people*
  > Isa 6:5 And I said : “ Woe is me! For I am lost ; for I am a man of unclean lips , and I dwell in the midst of a people of unclean lips ; for my eyes have seen the King , the Lord of hosts !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:9** (✓) *target: people*
  > Isa 6:9 And he said , “ Go , and say to this people : “‘Keep on hearing , but do not understand ; keep on seeing , but do not perceive .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:10** (✓) *target: people*
  > Isa 6:10 Make the heart of this people dull , and their ears heavy , and blind their eyes ; lest they see with their eyes , and hear with their ears , and understand with their hearts , and turn and be healed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:2** (✓) *target: people*
  > Isa 7:2 When the house of David was told , “ Syria is in league with Ephraim ,” the heart of Ahaz and the heart of his people shook as the trees of the forest shake before the wind .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:8** (✓) *target: people*
  > Isa 7:8 For the head of Syria is Damascus , and the head of Damascus is Rezin . And within sixty-five years Ephraim will be shattered from being a people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:17** (✓) *target: people*
  > Isa 7:17 The Lord will bring upon you and upon your people and upon your father’s house such days as have not come since the day that Ephraim departed from Judah —the king of Assyria !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:6** (✓) *target: people*
  > Isa 8:6 “ Because this people has refused the waters of Shiloah that flow gently , and rejoice over Rezin and the son of Remaliah ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:9** (✓) *target: peoples*
  > Isa 8:9 Be broken , you peoples , and be shattered ; give ear , all you far countries ; strap on your armor and be shattered ; strap on your armor and be shattered .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:11** (✓) *target: people*
  > Isa 8:11 For the Lord spoke thus to me with his strong hand upon me, and warned me not to walk in the way of this people , saying :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:12** (✓) *target: people*
  > Isa 8:12 “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:19** (✓) *target: people*
  > Isa 8:19 And when they say to you, “ Inquire of the mediums and the necromancers who chirp and mutter ,” should not a people inquire of their God ? Should they inquire of the dead on behalf of the living ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:2** (✓) *target: people*
  > Isa 9:2 The people who walked in darkness have seen a great light ; those who dwelt in a land of deep darkness , on them has light shone .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:9** (✓) *target: people*
  > Isa 9:9 and all the people will know , Ephraim and the inhabitants of Samaria , who say in pride and in arrogance of heart :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:13** (✓) *target: people*
  > Isa 9:13 The people did not turn to him who struck them, nor inquire of the Lord of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:16** (✓) *target: people*
  > Isa 9:16 for those who guide this people have been leading them astray , and those who are guided by them are swallowed up .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:19** (✓) *target: people*
  > Isa 9:19 Through the wrath of the Lord of hosts the land is scorched , and the people are like fuel for the fire ; no one spares another .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:2** (✓) *target: people*
  > Isa 10:2 to turn aside the needy from justice and to rob the poor of my people of their right , that widows may be their spoil , and that they may make the fatherless their prey !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:6** (✓) *target: people*
  > Isa 10:6 Against a godless nation I send him, and against the people of my wrath I command him, to take spoil and seize plunder , and to tread them down like the mire of the streets .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:13** (✓) *target: peoples*
  > Isa 10:13 For he says : “ By the strength of my hand I have done it, and by my wisdom , for I have understanding ; I remove the boundaries of peoples , and plunder their treasures; like a bull I bring down those who sit on thrones.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:14** (✓) *target: peoples*
  > Isa 10:14 My hand has found like a nest the wealth of the peoples ; and as one gathers eggs that have been forsaken , so I have gathered all the earth ; and there was none that moved a wing or opened the mouth or chirped .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:22** (✓) *target: people*
  > Isa 10:22 For though your people Israel be as the sand of the sea , only a remnant of them will return . Destruction is decreed , overflowing with righteousness .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:24** (✓) *target: people*
  > Isa 10:24 Therefore thus says the Lord God of hosts : “O my people , who dwell in Zion , be not afraid of the Assyrians when they strike with the rod and lift up their staff against you as the Egyptians did.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:10** (✓) *target: peoples*
  > Isa 11:10 In that day the root of Jesse , who shall stand as a signal for the peoples —of him shall the nations inquire , and his resting place shall be glorious .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:11** (✓) *target: people*
  > Isa 11:11 In that day the Lord will extend his hand yet a second time to recover the remnant that remains of his people , from Assyria , from Egypt , from Pathros , from Cush , from Elam , from Shinar , from Hamath , and from the coastlands of the sea .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:16** (✓) *target: people*
  > Isa 11:16 And there will be a highway from Assyria for the remnant that remains of his people , as there was for Israel when they came up from the land of Egypt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 12:4** (✓) *target: peoples*
  > Isa 12:4 And you will say in that day : “Give thanks to the Lord , call upon his name , make known his deeds among the peoples , proclaim that his name is exalted .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 13:4** (✓) *target: multitude*
  > Isa 13:4 The sound of a tumult is on the mountains as of a great multitude ! The sound of an uproar of kingdoms , of nations gathering together ! The Lord of hosts is mustering a host for battle .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 13:14** (✓) *target: people*
  > Isa 13:14 And like a hunted gazelle , or like sheep with none to gather them, each will turn to his own people , and each will flee to his own land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:2** (✓) *target: peoples*
  > Isa 14:2 And the peoples will take them and bring them to their place , and the house of Israel will possess them in the Lord’s land as male and female slaves . They will take captive those who were their captors , and rule over those who oppressed them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:6** (✓) *target: peoples*
  > Isa 14:6 that struck the peoples in wrath with unceasing blows , that ruled the nations in anger with unrelenting persecution .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:20** (✓) *target: people*
  > Isa 14:20 You will not be joined with them in burial , because you have destroyed your land , you have slain your people . “May the offspring of evildoers nevermore be named !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:32** (✓) *target: people*
  > Isa 14:32 What will one answer the messengers of the nation ? “The Lord has founded Zion , and in her the afflicted of his people find refuge .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 17:12** (✓) *target: peoples*
  > Isa 17:12 Ah , the thunder of many peoples ; they thunder like the thundering of the sea ! Ah, the roar of nations ; they roar like the roaring of mighty waters !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 18:2** (✓) *target: people*
  > Isa 18:2 which sends ambassadors by the sea , in vessels of papyrus on the waters ! Go , you swift messengers , to a nation tall and smooth , to a people feared near and far , a nation mighty and conquering , whose land the rivers divide .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 18:7** (✓) *target: people*
  > Isa 18:7 At that time tribute will be brought to the Lord of hosts from a people tall and smooth , from a people feared near and far , a nation mighty and conquering , whose land the rivers divide , to Mount Zion , the place of the name of the Lord of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 19:25** (✓) *target: people*
  > Isa 19:25 whom the Lord of hosts has blessed , saying , “ Blessed be Egypt my people , and Assyria the work of my hands , and Israel my inheritance .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 22:4** (✓) *target: people*
  > Isa 22:4 Therefore I said : “Look away from me; let me weep bitter tears ; do not labor to comfort me concerning the destruction of the daughter of my people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 23:13** (✓) *target: people*
  > Isa 23:13 Behold the land of the Chaldeans ! This is the people that was not ; Assyria destined it for wild beasts . They erected their siege towers , they stripped her palaces bare, they made her a ruin .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:2** (✓) *target: people*
  > Isa 24:2 And it shall be , as with the people , so with the priest ; as with the slave , so with his master ; as with the maid , so with her mistress ; as with the buyer , so with the seller ; as with the lender , so with the borrower ; as with the creditor , so with the debtor .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:4** (✓) *target: people*
  > Isa 24:4 The earth mourns and withers ; the world languishes and withers ; the highest people of the earth languish .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:13** (✓) *target: nations*
  > Isa 24:13 For thus it shall be in the midst of the earth among the nations , as when an olive tree is beaten , as at the gleaning when the grape harvest is done .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:3** (✓) *target: peoples*
  > Isa 25:3 Therefore strong peoples will glorify you; cities of ruthless nations will fear you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:6** (✓) *target: peoples*
  > Isa 25:6 On this mountain the Lord of hosts will make for all peoples a feast of rich food , a feast of well-aged wine , of rich food full of marrow , of aged wine well refined .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:7** (✓) *target: peoples*
  > Isa 25:7 And he will swallow up on this mountain the covering that is cast over all peoples , the veil that is spread over all nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:8** (✓) *target: people*
  > Isa 25:8 He will swallow up death forever ; and the Lord God will wipe away tears from all faces , and the reproach of his people he will take away from all the earth , for the Lord has spoken .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 26:11** (✓) *target: people*
  > Isa 26:11 O Lord , your hand is lifted up , but they do not see it. Let them see your zeal for your people , and be ashamed . Let the fire for your adversaries consume them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 1:9** (✓) *target: people*
  > Hos 1:9 And the Lord said , “ Call his name Not My People , for you are not my people , and I am not your God.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 1:10** (✓) *target: people*
  > Hos 1:10 Yet the number of the children of Israel shall be like the sand of the sea , which cannot be measured or numbered . And in the place where it was said to them, “You are not my people ,” it shall be said to them, “ Children of the living God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 2:1** (✓) *target: people*
  > Hos 2:1 Say to your brothers , “ You are my people ,” and to your sisters , “ You have received mercy .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 2:23** (✓) *target: People*
  > Hos 2:23 and I will sow her for myself in the land . And I will have mercy on No Mercy , and I will say to Not My People , ‘You are my people ’; and he shall say , ‘You are my God .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:4** (✓) *target: with you*
  > Hos 4:4 Yet let no one contend , and let none accuse , for with you is my contention , O priest .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:6** (✓) *target: people*
  > Hos 4:6 My people are destroyed for lack of knowledge ; because you have rejected knowledge , I reject you from being a priest to me. And since you have forgotten the law of your God , I also will forget your children .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:8** (✓) *target: people*
  > Hos 4:8 They feed on the sin of my people ; they are greedy for their iniquity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:9** (✓) *target: people*
  > Hos 4:9 And it shall be like people , like priest ; I will punish them for their ways and repay them for their deeds .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:12** (✓) *target: people*
  > Hos 4:12 My people inquire of a piece of wood , and their walking staff gives them oracles . For a spirit of whoredom has led them astray , and they have left their God to play the whore .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:14** (✓) *target: people*
  > Hos 4:14 I will not punish your daughters when they play the whore , nor your brides when they commit adultery ; for the men themselves go aside with prostitutes and sacrifice with cult prostitutes , and a people without understanding shall come to ruin .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 6:11** (✓) *target: people*
  > Hos 6:11 For you also , O Judah , a harvest is appointed . When I restore the fortunes of my people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 7:8** (✓) *target: peoples*
  > Hos 7:8 Ephraim mixes himself with the peoples ; Ephraim is a cake not turned .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 9:1** (✓) *target: peoples*
  > Hos 9:1 Rejoice not, O Israel ! Exult not like the peoples ; for you have played the whore , forsaking your God . You have loved a prostitute’s wages on all threshing floors .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:5** (✓) *target: people*
  > Hos 10:5 The inhabitants of Samaria tremble for the calf of Beth-aven . Its people mourn for it, and so do its idolatrous priests — those who rejoiced over it and over its glory — for it has departed from them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:10** (✓) *target: nations*
  > Hos 10:10 When I please , I will discipline them, and nations shall be gathered against them when they are bound up for their double iniquity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:14** (✓) *target: people*
  > Hos 10:14 therefore the tumult of war shall arise among your people , and all your fortresses shall be destroyed , as Shalman destroyed Beth-arbel on the day of battle ; mothers were dashed in pieces with their children .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 11:7** (✓) *target: people*
  > Hos 11:7 My people are bent on turning away from me, and though they call out to the Most High , he shall not raise them up at all .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:2** (✓) *target: people*
  > Joe 2:2 a day of darkness and gloom , a day of clouds and thick darkness ! Like blackness there is spread upon the mountains a great and powerful people ; their like has never been before , nor will be again after them through the years of all generations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:6** (✓) *target: peoples*
  > Joe 2:6 Before them peoples are in anguish ; all faces grow pale .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:16** (✓) *target: people*
  > Joe 2:16 gather the people . Consecrate the congregation ; assemble the elders ; gather the children , even nursing infants. Let the bridegroom leave his room , and the bride her chamber .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:17** (✓) *target: people*
  > Joe 2:17 Between the vestibule and the altar let the priests , the ministers of the Lord , weep and say , “ Spare your people , O Lord , and make not your heritage a reproach , a byword among the nations . Why should they say among the peoples , ‘ Where is their God ?’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:18** (✓) *target: people*
  > Joe 2:18 Then the Lord became jealous for his land and had pity on his people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:19** (✓) *target: people*
  > Joe 2:19 The Lord answered and said to his people , “ Behold , I am sending to you grain , wine , and oil , and you will be satisfied ; and I will no more make you a reproach among the nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:26** (✓) *target: people*
  > Joe 2:26 “You shall eat in plenty and be satisfied , and praise the name of the Lord your God , who has dealt wondrously with you. And my people shall never again be put to shame .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:27** (✓) *target: people*
  > Joe 2:27 You shall know that I am in the midst of Israel , and that I am the Lord your God and there is none else . And my people shall never again be put to shame .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:2** (✓) *target: people*
  > Joe 3:2 I will gather all the nations and bring them down to the Valley of Jehoshaphat . And I will enter into judgment with them there , on behalf of my people and my heritage Israel , because they have scattered them among the nations and have divided up my land ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:3** (✓) *target: people*
  > Joe 3:3 and have cast lots for my people , and have traded a boy for a prostitute , and have sold a girl for wine and have drunk it.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:16** (✓) *target: people*
  > Joe 3:16 The Lord roars from Zion , and utters his voice from Jerusalem , and the heavens and the earth quake . But the Lord is a refuge to his people , a stronghold to the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 1:5** (✓) *target: people*
  > Amo 1:5 I will break the gate-bar of Damascus , and cut off the inhabitants from the Valley of Aven , and him who holds the scepter from Beth-eden ; and the people of Syria shall go into exile to Kir ,” says the Lord .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 3:6** (✓) *target: people*
  > Amo 3:6 Is a trumpet blown in a city , and the people are not afraid ? Does disaster come to a city , unless the Lord has done it?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 7:8** (✓) *target: people*
  > Amo 7:8 And the Lord said to me, “ Amos , what do you see ?” And I said , “A plumb line .” Then the Lord said , “ Behold , I am setting a plumb line in the midst of my people Israel ; I will never again pass by them ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 7:15** (✓) *target: people*
  > Amo 7:15 But the Lord took me from following the flock , and the Lord said to me, ‘ Go , prophesy to my people Israel .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 8:2** (✓) *target: people*
  > Amo 8:2 And he said , “ Amos , what do you see ?” And I said , “A basket of summer fruit .” Then the Lord said to me , “The end has come upon my people Israel ; I will never again pass by them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 9:10** (✓) *target: people*
  > Amo 9:10 All the sinners of my people shall die by the sword , who say , ‘ Disaster shall not overtake or meet us.’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 9:14** (✓) *target: people*
  > Amo 9:14 I will restore the fortunes of my people Israel , and they shall rebuild the ruined cities and inhabit them; they shall plant vineyards and drink their wine , and they shall make gardens and eat their fruit .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Obd 13** (✓) *target: people*
  > Obd 13 Do not enter the gate of my people in the day of their calamity ; do not gloat over his disaster in the day of his calamity ; do not loot his wealth in the day of his calamity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jon 1:8** (✓) *target: people*
  > Jon 1:8 Then they said to him, “ Tell us on whose account this evil has come upon us. What is your occupation ? And where do you come from? What is your country ? And of what people are you ?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 1:2** (✓) *target: peoples*
  > Mic 1:2 Hear , you peoples , all of you; pay attention , O earth , and all that is in it, and let the Lord God be a witness against you, the Lord from his holy temple .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 1:9** (✓) *target: people*
  > Mic 1:9 For her wound is incurable , and it has come to Judah ; it has reached to the gate of my people , to Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:4** (✓) *target: people*
  > Mic 2:4 In that day they shall take up a taunt song against you and moan bitterly , and say , “We are utterly ruined ; he changes the portion of my people ; how he removes it from me! To an apostate he allots our fields .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:8** (✓) *target: people*
  > Mic 2:8 But lately my people have risen up as an enemy ; you strip the rich robe from those who pass by trustingly with no thought of war .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:9** (✓) *target: people*
  > Mic 2:9 The women of my people you drive out from their delightful houses ; from their young children you take away my splendor forever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:11** (✓) *target: people*
  > Mic 2:11 If a man should go about and utter wind and lies , saying, “I will preach to you of wine and strong drink ,” he would be the preacher for this people !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 3:3** (✓) *target: people*
  > Mic 3:3 who eat the flesh of my people , and flay their skin from off them, and break their bones in pieces and chop them up like meat in a pot , like flesh in a cauldron .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 3:5** (✓) *target: people*
  > Mic 3:5 Thus says the Lord concerning the prophets who lead my people astray , who cry “ Peace ” when they have something to eat , but declare war against him who puts nothing into their mouths .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:1** (✓) *target: peoples*
  > Mic 4:1 It shall come to pass in the latter days that the mountain of the house of the Lord shall be established as the highest of the mountains , and it shall be lifted up above the hills ; and peoples shall flow to it,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:3** (✓) *target: peoples*
  > Mic 4:3 He shall judge between many peoples , and shall decide disputes for strong nations far away; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:5** (✓) *target: peoples*
  > Mic 4:5 For all the peoples walk each in the name of its god , but we will walk in the name of the Lord our God forever and ever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:13** (✓) *target: peoples*
  > Mic 4:13 Arise and thresh , O daughter of Zion , for I will make your horn iron , and I will make your hoofs bronze ; you shall beat in pieces many peoples ; and shall devote their gain to the Lord , their wealth to the Lord of the whole earth .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 5:7** (✓) *target: peoples*
  > Mic 5:7 Then the remnant of Jacob shall be in the midst of many peoples like dew from the Lord , like showers on the grass , which delay not for a man nor wait for the children of man .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 5:8** (✓) *target: peoples*
  > Mic 5:8 And the remnant of Jacob shall be among the nations , in the midst of many peoples , like a lion among the beasts of the forest , like a young lion among the flocks of sheep , which , when it goes through, treads down and tears in pieces, and there is none to deliver .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:2** (✓) *target: people*
  > Mic 6:2 Hear , you mountains , the indictment of the Lord , and you enduring foundations of the earth , for the Lord has an indictment against his people , and he will contend with Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:3** (✓) *target: people*
  > Mic 6:3 “O my people , what have I done to you? How have I wearied you? Answer me !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:5** (✓) *target: people*
  > Mic 6:5 O my people , remember what Balak king of Moab devised , and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal , that you may know the righteous acts of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:16** (✓) *target: people*
  > Mic 6:16 For you have kept the statutes of Omri , and all the works of the house of Ahab ; and you have walked in their counsels , that I may make you a desolation , and your inhabitants a hissing ; so you shall bear the scorn of my people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 7:14** (✓) *target: people*
  > Mic 7:14 Shepherd your people with your staff , the flock of your inheritance , who dwell alone in a forest in the midst of a garden land ; let them graze in Bashan and Gilead as in the days of old .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Nah 3:18** (✓) *target: people*
  > Nah 3:18 Your shepherds are asleep , O king of Assyria ; your nobles slumber . Your people are scattered on the mountains with none to gather them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:5** (✓) *target: peoples*
  > Hab 2:5 “ Moreover , wine is a traitor , an arrogant man who is never at rest . His greed is as wide as Sheol ; like death he has never enough . He gathers for himself all nations and collects as his own all peoples .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:8** (✓) *target: peoples*
  > Hab 2:8 Because you have plundered many nations , all the remnant of the peoples shall plunder you, for the blood of man and violence to the earth , to cities and all who dwell in them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:10** (✓) *target: peoples*
  > Hab 2:10 You have devised shame for your house by cutting off many peoples ; you have forfeited your life .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2

**Group `5737-002`** (2 verses — anchors: Num 14:9, Num 14:11)

- **Num 14:9** 🔵 (✓) *target: people*
  > Num 14:9 Only do not rebel against the Lord . And do not fear the people of the land , for they are bread for us. Their protection is removed from them, and the Lord is with us; do not fear them .”
- **Num 14:11** 🔵 (✓) *target: people*
  > Num 14:11 And the Lord said to Moses , “ How long will this people despise me? And how long will they not believe in me, in spite of all the signs that I have done among them?

**Group `5737-003`** (1 verse — anchors: Exo 7:14)

- **Exo 7:14** 🔵 (✓) *target: people*
  > Exo 7:14 Then the Lord said to Moses , “ Pharaoh’s heart is hardened ; he refuses to let the people go .

### `H5971I` — 430/430 classified · 5 anchor verse(s)

**Group `5738-001`** (427 verses — anchors: Num 11:29, Num 14:19)

- **Num 11:29** 🔵 (✓) *target: people*
  > Num 11:29 But Moses said to him, “Are you jealous for my sake? Would that all the Lord’s people were prophets , that the Lord would put his Spirit on them !”
- **Num 14:19** 🔵 (✓) *target: people*
  > Num 14:19 Please pardon the iniquity of this people , according to the greatness of your steadfast love , just as you have forgiven this people , from Egypt until now .”
- **Gen 11:6** (✓) *target: people*
  > Gen 11:6 And the Lord said , “Behold, they are one people , and they have all one language , and this is only the beginning of what they will do . And nothing that they propose to do will now be impossible for them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 14:16** (✓) *target: people*
  > Gen 14:16 Then he brought back all the possessions , and also brought back his kinsman Lot with his possessions , and the women and the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 17:16** (✓) *target: peoples*
  > Gen 17:16 I will bless her , and moreover , I will give you a son by her. I will bless her, and she shall become nations ; kings of peoples shall come from her .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 19:4** (✓) *target: people*
  > Gen 19:4 But before they lay down , the men of the city , the men of Sodom , both young and old , all the people to the last man , surrounded the house .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:7** (✓) *target: people*
  > Gen 23:7 Abraham rose and bowed to the Hittites , the people of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:11** (✓) *target: people*
  > Gen 23:11 “ No , my lord , hear me : I give you the field , and I give you the cave that is in it. In the sight of the sons of my people I give it to you. Bury your dead .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:12** (✓) *target: people*
  > Gen 23:12 Then Abraham bowed down before the people of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:13** (✓) *target: people*
  > Gen 23:13 And he said to Ephron in the hearing of the people of the land , “But if you will, hear me: I give the price of the field . Accept it from me, that I may bury my dead there .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 26:10** (✓) *target: people*
  > Gen 26:10 Abimelech said , “ What is this you have done to us? One of the people might easily have lain with your wife , and you would have brought guilt upon us.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 26:11** (✓) *target: people*
  > Gen 26:11 So Abimelech warned all the people , saying , “Whoever touches this man or his wife shall surely be put to death .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 27:29** (✓) *target: peoples*
  > Gen 27:29 Let peoples serve you, and nations bow down to you. Be lord over your brothers , and may your mother’s sons bow down to you. Cursed be everyone who curses you, and blessed be everyone who blesses you!”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 28:3** (✓) *target: peoples*
  > Gen 28:3 God Almighty bless you and make you fruitful and multiply you, that you may become a company of peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 32:7** (✓) *target: people*
  > Gen 32:7 Then Jacob was greatly afraid and distressed . He divided the people who were with him, and the flocks and herds and camels , into two camps ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 33:15** (✓) *target: people*
  > Gen 33:15 So Esau said , “ Let me leave with you some of the people who are with me.” But he said , “ What need is there ? Let me find favor in the sight of my lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 34:16** (✓) *target: people*
  > Gen 34:16 Then we will give our daughters to you, and we will take your daughters to ourselves, and we will dwell with you and become one people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 34:22** (✓) *target: people*
  > Gen 34:22 Only on this condition will the men agree to dwell with us to become one people —when every male among us is circumcised as they are circumcised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 35:6** (✓) *target: people*
  > Gen 35:6 And Jacob came to Luz (that is, Bethel ), which is in the land of Canaan , he and all the people who were with him ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 41:40** (✓) *target: people*
  > Gen 41:40 You shall be over my house , and all my people shall order themselves as you command . Only as regards the throne will I be greater than you .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 41:55** (✓) *target: people*
  > Gen 41:55 When all the land of Egypt was famished , the people cried to Pharaoh for bread . Pharaoh said to all the Egyptians , “ Go to Joseph . What he says to you, do .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 42:6** (✓) *target: people*
  > Gen 42:6 Now Joseph was governor over the land . He was the one who sold to all the people of the land . And Joseph’s brothers came and bowed themselves before him with their faces to the ground .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 47:21** (✓) *target: people*
  > Gen 47:21 As for the people , he made servants of them from one end of Egypt to the other .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 47:23** (✓) *target: people*
  > Gen 47:23 Then Joseph said to the people , “ Behold , I have this day bought you and your land for Pharaoh . Now here is seed for you, and you shall sow the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 48:4** (✓) *target: peoples*
  > Gen 48:4 and said to me, ‘ Behold , I will make you fruitful and multiply you, and I will make of you a company of peoples and will give this land to your offspring after you for an everlasting possession .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 48:19** (✓) *target: people*
  > Gen 48:19 But his father refused and said , “I know , my son , I know . He also shall become a people , and he also shall be great . Nevertheless , his younger brother shall be greater than he, and his offspring shall become a multitude of nations .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 49:10** (✓) *target: peoples*
  > Gen 49:10 The scepter shall not depart from Judah , nor the ruler’s staff from between his feet , until tribute comes to him; and to him shall be the obedience of the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 49:16** (✓) *target: people*
  > Gen 49:16 “ Dan shall judge his people as one of the tribes of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 50:20** (✓) *target: people*
  > Gen 50:20 As for you , you meant evil against me, but God meant it for good , to bring it about that many people should be kept alive , as they are today .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:9** (✓) *target: people*
  > Exo 1:9 And he said to his people , “ Behold , the people of Israel are too many and too mighty for us .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:20** (✓) *target: people*
  > Exo 1:20 So God dealt well with the midwives . And the people multiplied and grew very strong .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:22** (✓) *target: people*
  > Exo 1:22 Then Pharaoh commanded all his people , “ Every son that is born to the Hebrews you shall cast into the Nile , but you shall let every daughter live .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:7** (✓) *target: people*
  > Exo 3:7 Then the Lord said , “I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters . I know their sufferings ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:10** (✓) *target: people*
  > Exo 3:10 Come , I will send you to Pharaoh that you may bring my people , the children of Israel , out of Egypt .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:12** (✓) *target: people*
  > Exo 3:12 He said , “ But I will be with you, and this shall be the sign for you, that I have sent you: when you have brought the people out of Egypt , you shall serve God on this mountain .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:21** (✓) *target: people*
  > Exo 3:21 And I will give this people favor in the sight of the Egyptians ; and when you go , you shall not go empty ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:16** (✓) *target: people*
  > Exo 4:16 He shall speak for you to the people , and he shall be your mouth , and you shall be as God to him.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:21** (✓) *target: people*
  > Exo 4:21 And the Lord said to Moses , “ When you go back to Egypt , see that you do before Pharaoh all the miracles that I have put in your power . But I will harden his heart , so that he will not let the people go .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:30** (✓) *target: people*
  > Exo 4:30 Aaron spoke all the words that the Lord had spoken to Moses and did the signs in the sight of the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:31** (✓) *target: people*
  > Exo 4:31 And the people believed ; and when they heard that the Lord had visited the people of Israel and that he had seen their affliction , they bowed their heads and worshiped .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:1** (✓) *target: people*
  > Exo 5:1 Afterward Moses and Aaron went and said to Pharaoh , “Thus says the Lord , the God of Israel , ‘Let my people go , that they may hold a feast to me in the wilderness .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:4** (✓) *target: people*
  > Exo 5:4 But the king of Egypt said to them, “ Moses and Aaron , why do you take the people away from their work ? Get back to your burdens .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:5** (✓) *target: people*
  > Exo 5:5 And Pharaoh said , “ Behold , the people of the land are now many , and you make them rest from their burdens !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:6** (✓) *target: people*
  > Exo 5:6 The same day Pharaoh commanded the taskmasters of the people and their foremen ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:7** (✓) *target: people*
  > Exo 5:7 “You shall no longer give the people straw to make bricks , as in the past ; let them go and gather straw for themselves.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:10** (✓) *target: people*
  > Exo 5:10 So the taskmasters and the foremen of the people went out and said to the people , “Thus says Pharaoh , ‘ I will not give you straw .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:12** (✓) *target: people*
  > Exo 5:12 So the people were scattered throughout all the land of Egypt to gather stubble for straw .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:16** (✓) *target: people*
  > Exo 5:16 No straw is given to your servants , yet they say to us, ‘ Make bricks !’ And behold, your servants are beaten ; but the fault is in your own people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:22** (✓) *target: people*
  > Exo 5:22 Then Moses turned to the Lord and said , “O Lord , why have you done evil to this people ? Why did you ever send me ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:23** (✓) *target: people*
  > Exo 5:23 For since I came to Pharaoh to speak in your name , he has done evil to this people , and you have not delivered your people at all .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 6:7** (✓) *target: people*
  > Exo 6:7 I will take you to be my people , and I will be your God , and you shall know that I am the Lord your God , who has brought you out from under the burdens of the Egyptians .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 7:4** (✓) *target: people*
  > Exo 7:4 Pharaoh will not listen to you. Then I will lay my hand on Egypt and bring my hosts , my people the children of Israel , out of the land of Egypt by great acts of judgment .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 7:16** (✓) *target: people*
  > Exo 7:16 And you shall say to him, ‘The Lord , the God of the Hebrews , sent me to you, saying , “Let my people go , that they may serve me in the wilderness .” But so far , you have not obeyed .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:1** (✓) *target: people*
  > Exo 8:1 Then the Lord said to Moses , “ Go in to Pharaoh and say to him, ‘ Thus says the Lord , “Let my people go , that they may serve me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:3** (✓) *target: people*
  > Exo 8:3 The Nile shall swarm with frogs that shall come up into your house and into your bedroom and on your bed and into the houses of your servants and your people , and into your ovens and your kneading bowls .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:4** (✓) *target: people*
  > Exo 8:4 The frogs shall come up on you and on your people and on all your servants .”’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:8** (✓) *target: people*
  > Exo 8:8 Then Pharaoh called Moses and Aaron and said , “ Plead with the Lord to take away the frogs from me and from my people , and I will let the people go to sacrifice to the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:9** (✓) *target: people*
  > Exo 8:9 Moses said to Pharaoh , “Be pleased to command me when I am to plead for you and for your servants and for your people , that the frogs be cut off from you and your houses and be left only in the Nile .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:11** (✓) *target: people*
  > Exo 8:11 The frogs shall go away from you and your houses and your servants and your people . They shall be left only in the Nile .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:20** (✓) *target: people*
  > Exo 8:20 Then the Lord said to Moses , “Rise up early in the morning and present yourself to Pharaoh , as he goes out to the water , and say to him, ‘ Thus says the Lord , “Let my people go , that they may serve me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:21** (✓) *target: people*
  > Exo 8:21 Or else, if you will not let my people go , behold, I will send swarms of flies on you and your servants and your people , and into your houses . And the houses of the Egyptians shall be filled with swarms of flies , and also the ground on which they stand.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 5:21** (✓) *target: people*
  > Num 5:21 then’ (let the priest make the woman take the oath of the curse , and say to the woman ) ‘the Lord make you a curse and an oath among your people , when the Lord makes your thigh fall away and your body swell .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 5:27** (✓) *target: people*
  > Num 5:27 And when he has made her drink the water , then, if she has defiled herself and has broken faith with her husband , the water that brings the curse shall enter into her and cause bitter pain , and her womb shall swell , and her thigh shall fall away , and the woman shall become a curse among her people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:1** (✓) *target: people*
  > Num 11:1 And the people complained in the hearing of the Lord about their misfortunes , and when the Lord heard it, his anger was kindled , and the fire of the Lord burned among them and consumed some outlying parts of the camp .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:2** (✓) *target: people*
  > Num 11:2 Then the people cried out to Moses , and Moses prayed to the Lord , and the fire died down .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:8** (✓) *target: people*
  > Num 11:8 The people went about and gathered it and ground it in handmills or beat it in mortars and boiled it in pots and made cakes of it. And the taste of it was like the taste of cakes baked with oil .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:10** (✓) *target: people*
  > Num 11:10 Moses heard the people weeping throughout their clans , everyone at the door of his tent . And the anger of the Lord blazed hotly , and Moses was displeased .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:11** (✓) *target: people*
  > Num 11:11 Moses said to the Lord , “ Why have you dealt ill with your servant ? And why have I not found favor in your sight , that you lay the burden of all this people on me ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:12** (✓) *target: people*
  > Num 11:12 Did I conceive all this people ? Did I give them birth , that you should say to me, ‘ Carry them in your bosom , as a nurse carries a nursing child ,’ to the land that you swore to give their fathers ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:13** (✓) *target: people*
  > Num 11:13 Where am I to get meat to give to all this people ? For they weep before me and say , ‘ Give us meat , that we may eat .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:14** (✓) *target: people*
  > Num 11:14 I am not able to carry all this people alone ; the burden is too heavy for me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:16** (✓) *target: people*
  > Num 11:16 Then the Lord said to Moses , “ Gather for me seventy men of the elders of Israel , whom you know to be the elders of the people and officers over them, and bring them to the tent of meeting , and let them take their stand there with you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:17** (✓) *target: people*
  > Num 11:17 And I will come down and talk with you there . And I will take some of the Spirit that is on you and put it on them, and they shall bear the burden of the people with you, so that you may not bear it yourself alone .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:18** (✓) *target: people*
  > Num 11:18 And say to the people , ‘ Consecrate yourselves for tomorrow , and you shall eat meat , for you have wept in the hearing of the Lord , saying , “ Who will give us meat to eat ? For it was better for us in Egypt .” Therefore the Lord will give you meat , and you shall eat .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:21** (✓) *target: people*
  > Num 11:21 But Moses said , “The people among whom I am number six hundred thousand on foot , and you have said , ‘I will give them meat , that they may eat a whole month !’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:24** (✓) *target: people*
  > Num 11:24 So Moses went out and told the people the words of the Lord . And he gathered seventy men of the elders of the people and placed them around the tent .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:32** (✓) *target: people*
  > Num 11:32 And the people rose all that day and all night and all the next day , and gathered the quail . Those who gathered least gathered ten homers . And they spread them out for themselves all around the camp .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:33** (✓) *target: people*
  > Num 11:33 While the meat was yet between their teeth , before it was consumed , the anger of the Lord was kindled against the people , and the Lord struck down the people with a very great plague .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:34** (✓) *target: people*
  > Num 11:34 Therefore the name of that place was called Kibroth-hattaavah , because there they buried the people who had the craving .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:35** (✓) *target: people*
  > Num 11:35 From Kibroth-hattaavah the people journeyed to Hazeroth , and they remained at Hazeroth .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 12:15** (✓) *target: people*
  > Num 12:15 So Miriam was shut outside the camp seven days , and the people did not set out on the march till Miriam was brought in again.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 12:16** (✓) *target: people*
  > Num 12:16 After that the people set out from Hazeroth , and camped in the wilderness of Paran .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:18** (✓) *target: people*
  > Num 13:18 and see what the land is, and whether the people who dwell in it are strong or weak , whether they are few or many ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:28** (✓) *target: people*
  > Num 13:28 However , the people who dwell in the land are strong , and the cities are fortified and very large . And besides , we saw the descendants of Anak there .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:30** (✓) *target: people*
  > Num 13:30 But Caleb quieted the people before Moses and said , “Let us go up at once and occupy it, for we are well able to overcome it .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:31** (✓) *target: people*
  > Num 13:31 Then the men who had gone up with him said , “We are not able to go up against the people , for they are stronger than we are.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:32** (✓) *target: people*
  > Num 13:32 So they brought to the people of Israel a bad report of the land that they had spied out , saying , “The land , through which we have gone to spy it out , is a land that devours its inhabitants , and all the people that we saw in it are of great height .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:1** (✓) *target: people*
  > Num 14:1 Then all the congregation raised a loud cry , and the people wept that night .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:13** (✓) *target: people*
  > Num 14:13 But Moses said to the Lord , “Then the Egyptians will hear of it, for you brought up this people in your might from among them,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:14** (✓) *target: people*
  > Num 14:14 and they will tell the inhabitants of this land . They have heard that you , O Lord , are in the midst of this people . For you , O Lord , are seen face to face , and your cloud stands over them and you go before them, in a pillar of cloud by day and in a pillar of fire by night .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:15** (✓) *target: people*
  > Num 14:15 Now if you kill this people as one man , then the nations who have heard your fame will say ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:16** (✓) *target: people*
  > Num 14:16 ‘It is because the Lord was not able to bring this people into the land that he swore to give to them that he has killed them in the wilderness .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:39** (✓) *target: people*
  > Num 14:39 When Moses told these words to all the people of Israel , the people mourned greatly .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 15:26** (✓) *target: population*
  > Num 15:26 And all the congregation of the people of Israel shall be forgiven , and the stranger who sojourns among them, because the whole population was involved in the mistake .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 15:30** (✓) *target: people*
  > Num 15:30 But the person who does anything with a high hand , whether he is native or a sojourner , reviles the Lord , and that person shall be cut off from among his people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 16:41** (✓) *target: people*
  > Num 16:41 But on the next day all the congregation of the people of Israel grumbled against Moses and against Aaron , saying , “ You have killed the people of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 16:47** (✓) *target: people*
  > Num 16:47 So Aaron took it as Moses said and ran into the midst of the assembly . And behold , the plague had already begun among the people . And he put on the incense and made atonement for the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 20:1** (✓) *target: people*
  > Num 20:1 And the people of Israel , the whole congregation , came into the wilderness of Zin in the first month , and the people stayed in Kadesh . And Miriam died there and was buried there .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 20:3** (✓) *target: people*
  > Num 20:3 And the people quarreled with Moses and said , “Would that we had perished when our brothers perished before the Lord !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:2** (✓) *target: people*
  > Num 21:2 And Israel vowed a vow to the Lord and said , “ If you will indeed give this people into my hand , then I will devote their cities to destruction.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:4** (✓) *target: people*
  > Num 21:4 From Mount Hor they set out by the way to the Red Sea , to go around the land of Edom . And the people became impatient on the way .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:5** (✓) *target: people*
  > Num 21:5 And the people spoke against God and against Moses , “ Why have you brought us up out of Egypt to die in the wilderness ? For there is no food and no water , and we loathe this worthless food .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:6** (✓) *target: people*
  > Num 21:6 Then the Lord sent fiery serpents among the people , and they bit the people , so that many people of Israel died .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:7** (✓) *target: people*
  > Num 21:7 And the people came to Moses and said , “We have sinned , for we have spoken against the Lord and against you. Pray to the Lord , that he take away the serpents from us.” So Moses prayed for the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:16** (✓) *target: people*
  > Num 21:16 And from there they continued to Beer ; that is the well of which the Lord said to Moses , “ Gather the people together, so that I may give them water .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:18** (✓) *target: people*
  > Num 21:18 the well that the princes made , that the nobles of the people dug , with the scepter and with their staffs .” And from the wilderness they went on to Mattanah ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:23** (✓) *target: people*
  > Num 21:23 But Sihon would not allow Israel to pass through his territory . He gathered all his people together and went out against Israel to the wilderness and came to Jahaz and fought against Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:29** (✓) *target: people*
  > Num 21:29 Woe to you, O Moab ! You are undone , O people of Chemosh ! He has made his sons fugitives , and his daughters captives , to an Amorite king , Sihon .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:33** (✓) *target: people*
  > Num 21:33 Then they turned and went up by the way to Bashan . And Og the king of Bashan came out against them , he and all his people , to battle at Edrei .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:34** (✓) *target: people*
  > Num 21:34 But the Lord said to Moses , “Do not fear him, for I have given him into your hand , and all his people , and his land . And you shall do to him as you did to Sihon king of the Amorites , who lived at Heshbon .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:35** (✓) *target: people*
  > Num 21:35 So they defeated him and his sons and all his people , until he had no survivor left . And they possessed his land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:3** (✓) *target: people*
  > Num 22:3 And Moab was in great dread of the people , because they were many . Moab was overcome with fear of the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:5** (✓) *target: Amaw*
  > Num 22:5 sent messengers to Balaam the son of Beor at Pethor , which is near the River in the land of the people of Amaw , to call him, saying , “ Behold , a people has come out of Egypt . They cover the face of the earth , and they are dwelling opposite me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:6** (✓) *target: people*
  > Num 22:6 Come now , curse this people for me, since they are too mighty for me. Perhaps I shall be able to defeat them and drive them from the land , for I know that he whom you bless is blessed , and he whom you curse is cursed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:11** (✓) *target: people*
  > Num 22:11 ‘ Behold , a people has come out of Egypt , and it covers the face of the earth . Now come , curse them for me. Perhaps I shall be able to fight against them and drive them out.’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:12** (✓) *target: people*
  > Num 22:12 God said to Balaam , “You shall not go with them. You shall not curse the people , for they are blessed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:17** (✓) *target: people*
  > Num 22:17 for I will surely do you great honor, and whatever you say to me I will do. Come , curse this people for me.’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:2** (✓) *target: people*
  > Jos 1:2 “ Moses my servant is dead . Now therefore arise , go over this Jordan , you and all this people , into the land that I am giving to them, to the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:6** (✓) *target: people*
  > Jos 1:6 Be strong and courageous , for you shall cause this people to inherit the land that I swore to their fathers to give them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:10** (✓) *target: people*
  > Jos 1:10 And Joshua commanded the officers of the people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:11** (✓) *target: people*
  > Jos 1:11 “ Pass through the midst of the camp and command the people , ‘ Prepare your provisions , for within three days you are to pass over this Jordan to go in to take possession of the land that the Lord your God is giving you to possess .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:3** (✓) *target: people*
  > Jos 3:3 and commanded the people , “ As soon as you see the ark of the covenant of the Lord your God being carried by the Levitical priests , then you shall set out from your place and follow it .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:5** (✓) *target: people*
  > Jos 3:5 Then Joshua said to the people , “ Consecrate yourselves, for tomorrow the Lord will do wonders among you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:6** (✓) *target: people*
  > Jos 3:6 And Joshua said to the priests , “Take up the ark of the covenant and pass on before the people .” So they took up the ark of the covenant and went before the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:14** (✓) *target: people*
  > Jos 3:14 So when the people set out from their tents to pass over the Jordan with the priests bearing the ark of the covenant before the people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:16** (✓) *target: people*
  > Jos 3:16 the waters coming down from above stood and rose up in a heap very far away, at Adam , the city that is beside Zarethan , and those flowing down toward the Sea of the Arabah , the Salt Sea , were completely cut off . And the people passed over opposite Jericho .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:2** (✓) *target: people*
  > Jos 4:2 “ Take twelve men from the people , from each tribe a man ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:10** (✓) *target: people*
  > Jos 4:10 For the priests bearing the ark stood in the midst of the Jordan until everything was finished that the Lord commanded Joshua to tell the people , according to all that Moses had commanded Joshua . The people passed over in haste .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:11** (✓) *target: people*
  > Jos 4:11 And when all the people had finished passing over , the ark of the Lord and the priests passed over before the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:19** (✓) *target: people*
  > Jos 4:19 The people came up out of the Jordan on the tenth day of the first month , and they encamped at Gilgal on the east border of Jericho .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:24** (✓) *target: peoples*
  > Jos 4:24 so that all the peoples of the earth may know that the hand of the Lord is mighty , that you may fear the Lord your God forever .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 5:4** (✓) *target: people*
  > Jos 5:4 And this is the reason why Joshua circumcised them: all the males of the people who came out of Egypt , all the men of war , had died in the wilderness on the way after they had come out of Egypt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 5:5** (✓) *target: people*
  > Jos 5:5 Though all the people who came out had been circumcised , yet all the people who were born on the way in the wilderness after they had come out of Egypt had not been circumcised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:5** (✓) *target: people*
  > Jos 6:5 And when they make a long blast with the ram’s horn , when you hear the sound of the trumpet , then all the people shall shout with a great shout , and the wall of the city will fall down flat , and the people shall go up , everyone straight before him .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:7** (✓) *target: people*
  > Jos 6:7 And he said to the people , “Go forward . March around the city and let the armed men pass on before the ark of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:8** (✓) *target: people*
  > Jos 6:8 And just as Joshua had commanded the people , the seven priests bearing the seven trumpets of rams’ horns before the Lord went forward , blowing the trumpets , with the ark of the covenant of the Lord following them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:10** (✓) *target: people*
  > Jos 6:10 But Joshua commanded the people , “You shall not shout or make your voice heard , neither shall any word go out of your mouth , until the day I tell you to shout . Then you shall shout .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:16** (✓) *target: people*
  > Jos 6:16 And at the seventh time , when the priests had blown the trumpets , Joshua said to the people , “ Shout , for the Lord has given you the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:20** (✓) *target: people*
  > Jos 6:20 So the people shouted , and the trumpets were blown . As soon as the people heard the sound of the trumpet , the people shouted a great shout , and the wall fell down flat , so that the people went up into the city , every man straight before him, and they captured the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:3** (✓) *target: people*
  > Jos 7:3 And they returned to Joshua and said to him, “Do not have all the people go up , but let about two or three thousand men go up and attack Ai . Do not make the whole people toil up there , for they are few .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:4** (✓) *target: people*
  > Jos 7:4 So about three thousand men went up there from the people . And they fled before the men of Ai ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:5** (✓) *target: people*
  > Jos 7:5 and the men of Ai killed about thirty-six of their men and chased them before the gate as far as Shebarim and struck them at the descent . And the hearts of the people melted and became as water .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:7** (✓) *target: people*
  > Jos 7:7 And Joshua said , “ Alas , O Lord God , why have you brought this people over the Jordan at all, to give us into the hands of the Amorites , to destroy us? Would that we had been content to dwell beyond the Jordan !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:13** (✓) *target: people*
  > Jos 7:13 Get up ! Consecrate the people and say , ‘ Consecrate yourselves for tomorrow ; for thus says the Lord , God of Israel , “There are devoted things in your midst , O Israel . You cannot stand before your enemies until you take away the devoted things from among you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:1** (✓) *target: men*
  > Jos 8:1 And the Lord said to Joshua , “Do not fear and do not be dismayed . Take all the fighting men with you, and arise , go up to Ai . See , I have given into your hand the king of Ai , and his people , his city , and his land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:5** (✓) *target: people*
  > Jos 8:5 And I and all the people who are with me will approach the city . And when they come out against us just as before , we shall flee before them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:9** (✓) *target: people*
  > Jos 8:9 So Joshua sent them out . And they went to the place of ambush and lay between Bethel and Ai , to the west of Ai , but Joshua spent that night among the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:10** (✓) *target: people*
  > Jos 8:10 Joshua arose early in the morning and mustered the people and went up , he and the elders of Israel , before the people to Ai .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:14** (✓) *target: people*
  > Jos 8:14 And as soon as the king of Ai saw this, he and all his people , the men of the city , hurried and went out early to the appointed place toward the Arabah to meet Israel in battle . But he did not know that there was an ambush against him behind the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:16** (✓) *target: people*
  > Jos 8:16 So all the people who were in the city were called together to pursue them, and as they pursued Joshua they were drawn away from the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:20** (✓) *target: people*
  > Jos 8:20 So when the men of Ai looked back , behold , the smoke of the city went up to heaven , and they had no power to flee this way or that, for the people who fled to the wilderness turned back against the pursuers .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:33** (✓) *target: people*
  > Jos 8:33 And all Israel , sojourner as well as native born , with their elders and officers and their judges , stood on opposite sides of the ark before the Levitical priests who carried the ark of the covenant of the Lord , half of them in front of Mount Gerizim and half of them in front of Mount Ebal , just as Moses the servant of the Lord had commanded at the first, to bless the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:7** (✓) *target: people*
  > Jos 10:7 So Joshua went up from Gilgal , he and all the people of war with him, and all the mighty men of valor .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:21** (✓) *target: people*
  > Jos 10:21 then all the people returned safe to Joshua in the camp at Makkedah . Not a man moved his tongue against any of the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:33** (✓) *target: people*
  > Jos 10:33 Then Horam king of Gezer came up to help Lachish . And Joshua struck him and his people , until he left none remaining .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 14:8** (✓) *target: people*
  > Jos 14:8 But my brothers who went up with me made the heart of the people melt ; yet I wholly followed the Lord my God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:14** (✓) *target: people*
  > Jos 17:14 Then the people of Joseph spoke to Joshua , saying , “ Why have you given me but one lot and one portion as an inheritance , although I am a numerous people , since all along the Lord has blessed me?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:15** (✓) *target: people*
  > Jos 17:15 And Joshua said to them, “ If you are a numerous people , go up by yourselves to the forest , and there clear ground for yourselves in the land of the Perizzites and the Rephaim , since the hill country of Ephraim is too narrow for you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:17** (✓) *target: people*
  > Jos 17:17 Then Joshua said to the house of Joseph , to Ephraim and Manasseh , “You are a numerous people and have great power . You shall not have one allotment only,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:2** (✓) *target: people*
  > Jos 24:2 And Joshua said to all the people , “Thus says the Lord , the God of Israel , ‘ Long ago , your fathers lived beyond the Euphrates , Terah , the father of Abraham and of Nahor ; and they served other gods .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:16** (✓) *target: people*
  > Jos 24:16 Then the people answered , “Far be it from us that we should forsake the Lord to serve other gods ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:17** (✓) *target: peoples*
  > Jos 24:17 for it is the Lord our God who brought us and our fathers up from the land of Egypt , out of the house of slavery , and who did those great signs in our sight and preserved us in all the way that we went , and among all the peoples through whom we passed .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:18** (✓) *target: peoples*
  > Jos 24:18 And the Lord drove out before us all the peoples , the Amorites who lived in the land . Therefore we also will serve the Lord , for he is our God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:19** (✓) *target: people*
  > Jos 24:19 But Joshua said to the people , “You are not able to serve the Lord , for he is a holy God . He is a jealous God ; he will not forgive your transgressions or your sins .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:21** (✓) *target: people*
  > Jos 24:21 And the people said to Joshua , “No, but we will serve the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:22** (✓) *target: people*
  > Jos 24:22 Then Joshua said to the people , “You are witnesses against yourselves that you have chosen the Lord , to serve him.” And they said , “We are witnesses .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:24** (✓) *target: people*
  > Jos 24:24 And the people said to Joshua , “The Lord our God we will serve , and his voice we will obey .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:25** (✓) *target: people*
  > Jos 24:25 So Joshua made a covenant with the people that day , and put in place statutes and rules for them at Shechem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:27** (✓) *target: people*
  > Jos 24:27 And Joshua said to all the people , “Behold, this stone shall be a witness against us, for it has heard all the words of the Lord that he spoke to us. Therefore it shall be a witness against you, lest you deal falsely with your God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:28** (✓) *target: people*
  > Jos 24:28 So Joshua sent the people away, every man to his inheritance .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 1:16** (✓) *target: people*
  > Judg 1:16 And the descendants of the Kenite , Moses ’ father-in-law , went up with the people of Judah from the city of palms into the wilderness of Judah , which lies in the Negeb near Arad , and they went and settled with the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:4** (✓) *target: people*
  > Judg 2:4 As soon as the angel of the Lord spoke these words to all the people of Israel , the people lifted up their voices and wept .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:6** (✓) *target: people*
  > Judg 2:6 When Joshua dismissed the people , the people of Israel went each to his inheritance to take possession of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:7** (✓) *target: people*
  > Judg 2:7 And the people served the Lord all the days of Joshua , and all the days of the elders who outlived Joshua , who had seen all the great work that the Lord had done for Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:12** (✓) *target: peoples*
  > Judg 2:12 And they abandoned the Lord , the God of their fathers , who had brought them out of the land of Egypt . They went after other gods , from among the gods of the peoples who were around them, and bowed down to them. And they provoked the Lord to anger.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 3:18** (✓) *target: people*
  > Judg 3:18 And when Ehud had finished presenting the tribute , he sent away the people who carried the tribute .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 5:2** (✓) *target: people*
  > Judg 5:2 “That the leaders took the lead in Israel , that the people offered themselves willingly , bless the Lord !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 1:3** (✓) *target: people*
  > Ezr 1:3 Whoever is among you of all his people , may his God be with him, and let him go up to Jerusalem , which is in Judah , and rebuild the house of the Lord , the God of Israel — he is the God who is in Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 2:2** (✓) *target: people*
  > Ezr 2:2 They came with Zerubbabel , Jeshua , Nehemiah , Seraiah , Reelaiah , Mordecai , Bilshan , Mispar , Bigvai , Rehum , and Baanah . The number of the men of the people of Israel :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 2:70** (✓) *target: people*
  > Ezr 2:70 Now the priests , the Levites , some of the people , the singers , the gatekeepers , and the temple servants lived in their towns , and all the rest of Israel in their towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:1** (✓) *target: people*
  > Ezr 3:1 When the seventh month came , and the children of Israel were in the towns , the people gathered as one man to Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:3** (✓) *target: peoples*
  > Ezr 3:3 They set the altar in its place , for fear was on them because of the peoples of the lands , and they offered burnt offerings on it to the Lord , burnt offerings morning and evening .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:11** (✓) *target: people*
  > Ezr 3:11 And they sang responsively , praising and giving thanks to the Lord , “ For he is good , for his steadfast love endures forever toward Israel .” And all the people shouted with a great shout when they praised the Lord , because the foundation of the house of the Lord was laid.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:13** (✓) *target: people*
  > Ezr 3:13 so that the people could not distinguish the sound of the joyful shout from the sound of the people’s weeping , for the people shouted with a great shout , and the sound was heard far away .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 4:4** (✓) *target: people*
  > Ezr 4:4 Then the people of the land discouraged the people of Judah and made them afraid to build
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 8:15** (✓) *target: people*
  > Ezr 8:15 I gathered them to the river that runs to Ahava , and there we camped three days . As I reviewed the people and the priests , I found there none of the sons of Levi .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 8:36** (✓) *target: people*
  > Ezr 8:36 They also delivered the king’s commissions to the king’s satraps and to the governors of the province Beyond the River , and they aided the people and the house of God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:1** (✓) *target: people*
  > Ezr 9:1 After these things had been done , the officials approached me and said , “The people of Israel and the priests and the Levites have not separated themselves from the peoples of the lands with their abominations , from the Canaanites , the Hittites , the Perizzites , the Jebusites , the Ammonites , the Moabites , the Egyptians , and the Amorites .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:2** (✓) *target: peoples*
  > Ezr 9:2 For they have taken some of their daughters to be wives for themselves and for their sons , so that the holy race has mixed itself with the peoples of the lands . And in this faithlessness the hand of the officials and chief men has been foremost .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:11** (✓) *target: peoples*
  > Ezr 9:11 which you commanded by your servants the prophets , saying , ‘The land that you are entering , to take possession of it, is a land impure with the impurity of the peoples of the lands , with their abominations that have filled it from end to end with their uncleanness .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:14** (✓) *target: peoples*
  > Ezr 9:14 shall we break your commandments again and intermarry with the peoples who practice these abominations ? Would you not be angry with us until you consumed us, so that there should be no remnant , nor any to escape ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:1** (✓) *target: people*
  > Ezr 10:1 While Ezra prayed and made confession , weeping and casting himself down before the house of God , a very great assembly of men , women , and children , gathered to him out of Israel , for the people wept bitterly .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:2** (✓) *target: peoples*
  > Ezr 10:2 And Shecaniah the son of Jehiel , of the sons of Elam , addressed Ezra : “ We have broken faith with our God and have married foreign women from the peoples of the land , but even now there is hope for Israel in spite of this .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:9** (✓) *target: people*
  > Ezr 10:9 Then all the men of Judah and Benjamin assembled at Jerusalem within the three days . It was the ninth month , on the twentieth day of the month . And all the people sat in the open square before the house of God , trembling because of this matter and because of the heavy rain .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:11** (✓) *target: peoples*
  > Ezr 10:11 Now then make confession to the Lord , the God of your fathers and do his will . Separate yourselves from the peoples of the land and from the foreign wives .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:13** (✓) *target: people*
  > Ezr 10:13 But the people are many , and it is a time of heavy rain ; we cannot stand in the open . Nor is this a task for one day or for two , for we have greatly transgressed in this matter .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 1:8** (✓) *target: among the peoples*
  > Neh 1:8 Remember the word that you commanded your servant Moses , saying , ‘If you are unfaithful , I will scatter you among the peoples ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 1:10** (✓) *target: people*
  > Neh 1:10 They are your servants and your people , whom you have redeemed by your great power and by your strong hand .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:6** (✓) *target: people*
  > Neh 4:6 So we built the wall . And all the wall was joined together to half its height, for the people had a mind to work .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:13** (✓) *target: people*
  > Neh 4:13 So in the lowest parts of the space behind the wall , in open places , I stationed the people by their clans , with their swords , their spears , and their bows .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:14** (✓) *target: people*
  > Neh 4:14 And I looked and arose and said to the nobles and to the officials and to the rest of the people , “Do not be afraid of them . Remember the Lord , who is great and awesome , and fight for your brothers , your sons , your daughters , your wives , and your homes .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:19** (✓) *target: people*
  > Neh 4:19 And I said to the nobles and to the officials and to the rest of the people , “The work is great and widely spread , and we are separated on the wall , far from one another .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:22** (✓) *target: people*
  > Neh 4:22 I also said to the people at that time , “Let every man and his servant pass the night within Jerusalem , that they may be a guard for us by night and may labor by day .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:1** (✓) *target: people*
  > Neh 5:1 Now there arose a great outcry of the people and of their wives against their Jewish brothers .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:13** (✓) *target: people*
  > Neh 5:13 I also shook out the fold of my garment and said , “ So may God shake out every man from his house and from his labor who does not keep this promise . So may he be shaken out and emptied .” And all the assembly said “ Amen ” and praised the Lord . And the people did as they had promised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:15** (✓) *target: people*
  > Neh 5:15 The former governors who were before me laid heavy burdens on the people and took from them for their daily ration forty shekels of silver . Even their servants lorded it over the people . But I did not do so , because of the fear of God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:18** (✓) *target: people*
  > Neh 5:18 Now what was prepared at my expense for each day was one ox and six choice sheep and birds , and every ten days all kinds of wine in abundance . Yet for all this I did not demand the food allowance of the governor , because the service was too heavy on this people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:19** (✓) *target: people*
  > Neh 5:19 Remember for my good , O my God , all that I have done for this people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:4** (✓) *target: people*
  > Neh 7:4 The city was wide and large , but the people within it were few , and no houses had been rebuilt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:5** (✓) *target: people*
  > Neh 7:5 Then my God put it into my heart to assemble the nobles and the officials and the people to be enrolled by genealogy . And I found the book of the genealogy of those who came up at the first , and I found written in it :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:7** (✓) *target: people*
  > Neh 7:7 They came with Zerubbabel , Jeshua , Nehemiah , Azariah , Raamiah , Nahamani , Mordecai , Bilshan , Mispereth , Bigvai , Nehum , Baanah . The number of the men of the people of Israel :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:72** (✓) *target: people*
  > Neh 7:72 And what the rest of the people gave was 20,000 darics of gold , 2,000 minas of silver , and 67 priests ’ garments .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:73** (✓) *target: people*
  > Neh 7:73 So the priests , the Levites , the gatekeepers , the singers , some of the people , the temple servants , and all Israel , lived in their towns . And when the seventh month had come , the people of Israel were in their towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:1** (✓) *target: people*
  > Neh 8:1 And all the people gathered as one man into the square before the Water Gate . And they told Ezra the scribe to bring the Book of the Law of Moses that the Lord had commanded Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:3** (✓) *target: people*
  > Neh 8:3 And he read from it facing the square before the Water Gate from early morning until midday , in the presence of the men and the women and those who could understand . And the ears of all the people were attentive to the Book of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:5** (✓) *target: people*
  > Neh 8:5 And Ezra opened the book in the sight of all the people , for he was above all the people , and as he opened it all the people stood .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:6** (✓) *target: people*
  > Neh 8:6 And Ezra blessed the Lord , the great God , and all the people answered , “ Amen , Amen ,” lifting up their hands . And they bowed their heads and worshiped the Lord with their faces to the ground .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:7** (✓) *target: people*
  > Neh 8:7 Also Jeshua , Bani , Sherebiah , Jamin , Akkub , Shabbethai , Hodiah , Maaseiah , Kelita , Azariah , Jozabad , Hanan , Pelaiah , the Levites , helped the people to understand the Law , while the people remained in their places .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:9** (✓) *target: people*
  > Neh 8:9 And Nehemiah , who was the governor , and Ezra the priest and scribe , and the Levites who taught the people said to all the people , “This day is holy to the Lord your God ; do not mourn or weep .” For all the people wept as they heard the words of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:11** (✓) *target: people*
  > Neh 8:11 So the Levites calmed all the people , saying , “Be quiet , for this day is holy ; do not be grieved .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:12** (✓) *target: people*
  > Neh 8:12 And all the people went their way to eat and drink and to send portions and to make great rejoicing , because they had understood the words that were declared to them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:13** (✓) *target: people*
  > Neh 8:13 On the second day the heads of fathers’ houses of all the people , with the priests and the Levites , came together to Ezra the scribe in order to study the words of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:16** (✓) *target: people*
  > Neh 8:16 So the people went out and brought them and made booths for themselves, each on his roof , and in their courts and in the courts of the house of God , and in the square at the Water Gate and in the square at the Gate of Ephraim .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:10** (✓) *target: people*
  > Neh 9:10 and performed signs and wonders against Pharaoh and all his servants and all the people of his land , for you knew that they acted arrogantly against our fathers. And you made a name for yourself, as it is to this day .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:22** (✓) *target: peoples*
  > Neh 9:22 “And you gave them kingdoms and peoples and allotted to them every corner . So they took possession of the land of Sihon king of Heshbon and the land of Og king of Bashan .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:24** (✓) *target: peoples*
  > Neh 9:24 So the descendants went in and possessed the land , and you subdued before them the inhabitants of the land , the Canaanites , and gave them into their hand , with their kings and the peoples of the land , that they might do with them as they would .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:30** (✓) *target: peoples*
  > Neh 9:30 Many years you bore with them and warned them by your Spirit through your prophets . Yet they would not give ear . Therefore you gave them into the hand of the peoples of the lands .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:32** (✓) *target: people*
  > Neh 9:32 “ Now , therefore, our God , the great , the mighty , and the awesome God , who keeps covenant and steadfast love , let not all the hardship seem little to you that has come upon us, upon our kings , our princes , our priests , our prophets , our fathers , and all your people , since the time of the kings of Assyria until this day .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:14** (✓) *target: people*
  > Neh 10:14 The chiefs of the people : Parosh , Pahath-moab , Elam , Zattu , Bani ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:28** (✓) *target: people*
  > Neh 10:28 “The rest of the people , the priests , the Levites , the gatekeepers , the singers , the temple servants , and all who have separated themselves from the peoples of the lands to the Law of God , their wives , their sons , their daughters , all who have knowledge and understanding ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:30** (✓) *target: peoples*
  > Neh 10:30 We will not give our daughters to the peoples of the land or take their daughters for our sons .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:31** (✓) *target: peoples*
  > Neh 10:31 And if the peoples of the land bring in goods or any grain on the Sabbath day to sell , we will not buy from them on the Sabbath or on a holy day . And we will forgo the crops of the seventh year and the exaction of every debt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:34** (✓) *target: people*
  > Neh 10:34 We, the priests , the Levites , and the people , have likewise cast lots for the wood offering , to bring it into the house of our God , according to our fathers ’ houses , at times appointed , year by year , to burn on the altar of the Lord our God , as it is written in the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:1** (✓) *target: people*
  > Neh 11:1 Now the leaders of the people lived in Jerusalem . And the rest of the people cast lots to bring one out of ten to live in Jerusalem the holy city , while nine out of ten remained in the other towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:2** (✓) *target: people*
  > Neh 11:2 And the people blessed all the men who willingly offered to live in Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:24** (✓) *target: people*
  > Neh 11:24 And Pethahiah the son of Meshezabel , of the sons of Zerah the son of Judah , was at the king’s side in all matters concerning the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 12:30** (✓) *target: people*
  > Neh 12:30 And the priests and the Levites purified themselves, and they purified the people and the gates and the wall .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 12:2** (✓) *target: people*
  > Job 12:2 “No doubt you are the people , and wisdom will die with you.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 12:24** (✓) *target: people*
  > Job 12:24 He takes away understanding from the chiefs of the people of the earth and makes them wander in a trackless waste .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 17:6** (✓) *target: peoples*
  > Job 17:6 “He has made me a byword of the peoples , and I am one before whom men spit .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 18:19** (✓) *target: people*
  > Job 18:19 He has no posterity or progeny among his people , and no survivor where he used to live .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 34:20** (✓) *target: people*
  > Job 34:20 In a moment they die ; at midnight the people are shaken and pass away , and the mighty are taken away by no human hand .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 34:30** (✓) *target: people*
  > Job 34:30 that a godless man should not reign , that he should not ensnare the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 36:20** (✓) *target: peoples*
  > Job 36:20 Do not long for the night , when peoples vanish in their place .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 36:31** (✓) *target: peoples*
  > Job 36:31 For by these he judges peoples ; he gives food in abundance .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 3:6** (✓) *target: people*
  > Psa 3:6 I will not be afraid of many thousands of people who have set themselves against me all around .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 3:8** (✓) *target: people*
  > Psa 3:8 Salvation belongs to the Lord ; your blessing be on your people ! Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 7:8** (✓) *target: peoples*
  > Psa 7:8 The Lord judges the peoples ; judge me, O Lord , according to my righteousness and according to the integrity that is in me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 9:11** (✓) *target: peoples*
  > Psa 9:11 Sing praises to the Lord , who sits enthroned in Zion ! Tell among the peoples his deeds !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 14:4** (✓) *target: people*
  > Psa 14:4 Have they no knowledge , all the evildoers who eat up my people as they eat bread and do not call upon the Lord ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 14:7** (✓) *target: people*
  > Psa 14:7 Oh, that salvation for Israel would come out of Zion ! When the Lord restores the fortunes of his people , let Jacob rejoice , let Israel be glad .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:27** (✓) *target: people*
  > Psa 18:27 For you save a humble people , but the haughty eyes you bring down .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:43** (✓) *target: people*
  > Psa 18:43 You delivered me from strife with the people ; you made me the head of the nations ; people whom I had not known served me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:47** (✓) *target: peoples*
  > Psa 18:47 the God who gave me vengeance and subdued peoples under me ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 22:6** (✓) *target: people*
  > Psa 22:6 But I am a worm and not a man , scorned by mankind and despised by the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 22:31** (✓) *target: people*
  > Psa 22:31 they shall come and proclaim his righteousness to a people yet unborn, that he has done it.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 28:9** (✓) *target: people*
  > Psa 28:9 Oh, save your people and bless your heritage ! Be their shepherd and carry them forever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 29:11** (✓) *target: people*
  > Psa 29:11 May the Lord give strength to his people ! May the Lord bless his people with peace !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 33:10** (✓) *target: peoples*
  > Psa 33:10 The Lord brings the counsel of the nations to nothing ; he frustrates the plans of the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 33:12** (✓) *target: people*
  > Psa 33:12 Blessed is the nation whose God is the Lord , the people whom he has chosen as his heritage !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 35:18** (✓) *target: throng*
  > Psa 35:18 I will thank you in the great congregation ; in the mighty throng I will praise you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 44:12** (✓) *target: people*
  > Psa 44:12 You have sold your people for a trifle , demanding no high price for them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:5** (✓) *target: peoples*
  > Psa 45:5 Your arrows are sharp in the heart of the king’s enemies ; the peoples fall under you.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:10** (✓) *target: people*
  > Psa 45:10 Hear , O daughter , and consider , and incline your ear : forget your people and your father’s house ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:12** (✓) *target: people*
  > Psa 45:12 The people of Tyre will seek your favor with gifts , the richest of the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:17** (✓) *target: nations*
  > Psa 45:17 I will cause your name to be remembered in all generations ; therefore nations will praise you forever and ever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:1** (✓) *target: peoples*
  > To the choirmaster . A Psalm of the Sons of Korah . Psa 47:1 Clap your hands , all peoples ! Shout to God with loud songs of joy !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:3** (✓) *target: peoples*
  > Psa 47:3 He subdued peoples under us, and nations under our feet .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:9** (✓) *target: peoples*
  > Psa 47:9 The princes of the peoples gather as the people of the God of Abraham . For the shields of the earth belong to God ; he is highly exalted !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 49:1** (✓) *target: peoples*
  > To the choirmaster . A Psalm of the Sons of Korah . Psa 49:1 Hear this , all peoples ! Give ear , all inhabitants of the world ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 50:4** (✓) *target: people*
  > Psa 50:4 He calls to the heavens above and to the earth , that he may judge his people :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 50:7** (✓) *target: people*
  > Psa 50:7 “ Hear , O my people , and I will speak ; O Israel , I will testify against you. I am God , your God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 53:4** (✓) *target: people*
  > Psa 53:4 Have those who work evil no knowledge , who eat up my people as they eat bread , and do not call upon God ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 53:6** (✓) *target: people*
  > Psa 53:6 Oh , that salvation for Israel would come out of Zion ! When God restores the fortunes of his people , let Jacob rejoice , let Israel be glad .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 56:7** (✓) *target: peoples*
  > Psa 56:7 For their crime ^ will they escape ? In wrath cast down the peoples , O God !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 57:9** (✓) *target: peoples*
  > Psa 57:9 I will give thanks to you, O Lord , among the peoples ; I will sing praises to you among the nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 59:11** (✓) *target: people*
  > Psa 59:11 Kill them not , lest my people forget ; make them totter by your power and bring them down , O Lord , our shield !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 60:3** (✓) *target: people*
  > Psa 60:3 You have made your people see hard things ; you have given us wine to drink that made us stagger .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 62:8** (✓) *target: people*
  > Psa 62:8 Trust in him at all times , O people ; pour out your heart before him; God is a refuge for us. Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 66:8** (✓) *target: peoples*
  > Psa 66:8 Bless our God , O peoples ; let the sound of his praise be heard ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:3** (✓) *target: peoples*
  > Psa 67:3 Let the peoples praise you, O God ; let all the peoples praise you!
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:4** (✓) *target: peoples*
  > Psa 67:4 Let the nations be glad and sing for joy , for you judge the peoples with equity and guide the nations upon earth . Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:5** (✓) *target: peoples*
  > Psa 67:5 Let the peoples praise you, O God ; let all the peoples praise you!
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:7** (✓) *target: people*
  > Psa 68:7 O God , when you went out before your people , when you marched through the wilderness , Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:30** (✓) *target: peoples*
  > Psa 68:30 Rebuke the beasts that dwell among the reeds , the herd of bulls with the calves of the peoples . Trample underfoot those who lust after tribute ; scatter the peoples who delight in war .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:35** (✓) *target: people*
  > Psa 68:35 Awesome is God from his sanctuary ; the God of Israel — he is the one who gives power and strength to his people . Blessed be God !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:2** (✓) *target: people*
  > Psa 72:2 May he judge your people with righteousness , and your poor with justice !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:3** (✓) *target: people*
  > Psa 72:3 Let the mountains bear prosperity for the people , and the hills , in righteousness !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:4** (✓) *target: people*
  > Psa 72:4 May he defend the cause of the poor of the people , give deliverance to the children of the needy , and crush the oppressor !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 73:10** (✓) *target: people*
  > Psa 73:10 Therefore his people turn back to them , and find no fault in them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 74:18** (✓) *target: people*
  > Psa 74:18 Remember this , O Lord , how the enemy scoffs , and a foolish people reviles your name .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:14** (✓) *target: peoples*
  > Psa 77:14 You are the God who works wonders ; you have made known your might among the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:15** (✓) *target: people*
  > Psa 77:15 You with your arm redeemed your people , the children of Jacob and Joseph . Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:20** (✓) *target: people*
  > Psa 77:20 You led your people like a flock by the hand of Moses and Aaron .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:1** (✓) *target: people*
  > A Maskil of Asaph . Psa 78:1 Give ear , O my people , to my teaching ; incline your ears to the words of my mouth !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:20** (✓) *target: people*
  > Psa 78:20 He struck the rock so that water gushed out and streams overflowed . Can he also give bread or provide meat for his people ?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:52** (✓) *target: people*
  > Psa 78:52 Then he led out his people like sheep and guided them in the wilderness like a flock .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 11:14** (✓) *target: people*
  > Pro 11:14 Where there is no guidance , a people falls , but in an abundance of counselors there is safety .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 14:28** (✓) *target: people*
  > Pro 14:28 In a multitude of people is the glory of a king , but without people a prince is ruined .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 24:24** (✓) *target: peoples*
  > Pro 24:24 Whoever says to the wicked , “You are in the right ,” will be cursed by peoples , abhorred by nations ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 28:15** (✓) *target: people*
  > Pro 28:15 Like a roaring lion or a charging bear is a wicked ruler over a poor people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 29:2** (✓) *target: people*
  > Pro 29:2 When the righteous increase , the people rejoice , but when the wicked rule , the people groan .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 29:18** (✓) *target: people*
  > Pro 29:18 Where there is no prophetic vision the people cast off restraint , but blessed is he who keeps the law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 30:25** (✓) *target: people*
  > Pro 30:25 the ants are a people not strong , yet they provide their food in the summer ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 30:26** (✓) *target: people*
  > Pro 30:26 the rock badgers are a people not mighty , yet they make their homes in the cliffs ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ecc 4:16** (✓) *target: people*
  > Ecc 4:16 There was no end of all the people , all of whom he led . Yet those who come later will not rejoice in him. Surely this also is vanity and a striving after wind .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ecc 12:9** (✓) *target: people*
  > Ecc 12:9 Besides being wise , the Preacher also taught the people knowledge , weighing and studying and arranging many proverbs with great care.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:3** (✓) *target: people*
  > Isa 1:3 The ox knows its owner , and the donkey its master’s crib , but Israel does not know , my people do not understand .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:4** (✓) *target: people*
  > Isa 1:4 Ah , sinful nation , a people laden with iniquity , offspring of evildoers , children who deal corruptly ! They have forsaken the Lord , they have despised the Holy One of Israel , they are utterly estranged.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:10** (✓) *target: people*
  > Isa 1:10 Hear the word of the Lord , you rulers of , Sodom ! Give ear to the teaching of our God , you people of Gomorrah !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:3** (✓) *target: peoples*
  > Isa 2:3 and many peoples shall come , and say : “ Come , let us go up to the mountain of the Lord , to the house of the God of Jacob , that he may teach us his ways and that we may walk in his paths .” For out of Zion shall go forth the law , and the word of the Lord from Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:4** (✓) *target: peoples*
  > Isa 2:4 He shall judge between the nations , and shall decide disputes for many peoples ; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:6** (✓) *target: people*
  > Isa 2:6 For you have rejected your people , the house of Jacob , because they are full of things from the east and of fortune-tellers like the Philistines , and they strike hands with the children of foreigners .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:5** (✓) *target: people*
  > Isa 3:5 And the people will oppress one another, every one his fellow and every one his neighbor ; the youth will be insolent to the elder , and the despised to the honorable .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:7** (✓) *target: people*
  > Isa 3:7 in that day he will speak out , saying : “I will not be a healer ; in my house there is neither bread nor cloak ; you shall not make me leader of the people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:12** (✓) *target: people*
  > Isa 3:12 My people — infants are their oppressors , and women rule over them. O my people , your guides mislead you and they have swallowed up the course of your paths .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:13** (✓) *target: peoples*
  > Isa 3:13 The Lord has taken his place to contend ; he stands to judge peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:14** (✓) *target: people*
  > Isa 3:14 The Lord will enter into judgment with the elders and princes of his people : “ It is you who have devoured the vineyard , the spoil of the poor is in your houses .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:15** (✓) *target: people*
  > Isa 3:15 What do you mean by crushing my people , by grinding the face of the poor ?” declares the Lord God of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 5:13** (✓) *target: people*
  > Isa 5:13 Therefore my people go into exile for lack of knowledge ; their honored men go hungry , and their multitude is parched with thirst .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 5:25** (✓) *target: people*
  > Isa 5:25 Therefore the anger of the Lord was kindled against his people , and he stretched out his hand against them and struck them, and the mountains quaked ; and their corpses were as refuse in the midst of the streets . For all this his anger has not turned away , and his hand is stretched out still .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:5** (✓) *target: people*
  > Isa 6:5 And I said : “ Woe is me! For I am lost ; for I am a man of unclean lips , and I dwell in the midst of a people of unclean lips ; for my eyes have seen the King , the Lord of hosts !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:9** (✓) *target: people*
  > Isa 6:9 And he said , “ Go , and say to this people : “‘Keep on hearing , but do not understand ; keep on seeing , but do not perceive .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:10** (✓) *target: people*
  > Isa 6:10 Make the heart of this people dull , and their ears heavy , and blind their eyes ; lest they see with their eyes , and hear with their ears , and understand with their hearts , and turn and be healed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:2** (✓) *target: people*
  > Isa 7:2 When the house of David was told , “ Syria is in league with Ephraim ,” the heart of Ahaz and the heart of his people shook as the trees of the forest shake before the wind .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:8** (✓) *target: people*
  > Isa 7:8 For the head of Syria is Damascus , and the head of Damascus is Rezin . And within sixty-five years Ephraim will be shattered from being a people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:17** (✓) *target: people*
  > Isa 7:17 The Lord will bring upon you and upon your people and upon your father’s house such days as have not come since the day that Ephraim departed from Judah —the king of Assyria !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:6** (✓) *target: people*
  > Isa 8:6 “ Because this people has refused the waters of Shiloah that flow gently , and rejoice over Rezin and the son of Remaliah ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:9** (✓) *target: peoples*
  > Isa 8:9 Be broken , you peoples , and be shattered ; give ear , all you far countries ; strap on your armor and be shattered ; strap on your armor and be shattered .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:11** (✓) *target: people*
  > Isa 8:11 For the Lord spoke thus to me with his strong hand upon me, and warned me not to walk in the way of this people , saying :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:12** (✓) *target: people*
  > Isa 8:12 “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:19** (✓) *target: people*
  > Isa 8:19 And when they say to you, “ Inquire of the mediums and the necromancers who chirp and mutter ,” should not a people inquire of their God ? Should they inquire of the dead on behalf of the living ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:2** (✓) *target: people*
  > Isa 9:2 The people who walked in darkness have seen a great light ; those who dwelt in a land of deep darkness , on them has light shone .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:9** (✓) *target: people*
  > Isa 9:9 and all the people will know , Ephraim and the inhabitants of Samaria , who say in pride and in arrogance of heart :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:13** (✓) *target: people*
  > Isa 9:13 The people did not turn to him who struck them, nor inquire of the Lord of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:16** (✓) *target: people*
  > Isa 9:16 for those who guide this people have been leading them astray , and those who are guided by them are swallowed up .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:19** (✓) *target: people*
  > Isa 9:19 Through the wrath of the Lord of hosts the land is scorched , and the people are like fuel for the fire ; no one spares another .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:2** (✓) *target: people*
  > Isa 10:2 to turn aside the needy from justice and to rob the poor of my people of their right , that widows may be their spoil , and that they may make the fatherless their prey !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:6** (✓) *target: people*
  > Isa 10:6 Against a godless nation I send him, and against the people of my wrath I command him, to take spoil and seize plunder , and to tread them down like the mire of the streets .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:13** (✓) *target: peoples*
  > Isa 10:13 For he says : “ By the strength of my hand I have done it, and by my wisdom , for I have understanding ; I remove the boundaries of peoples , and plunder their treasures; like a bull I bring down those who sit on thrones.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:14** (✓) *target: peoples*
  > Isa 10:14 My hand has found like a nest the wealth of the peoples ; and as one gathers eggs that have been forsaken , so I have gathered all the earth ; and there was none that moved a wing or opened the mouth or chirped .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:22** (✓) *target: people*
  > Isa 10:22 For though your people Israel be as the sand of the sea , only a remnant of them will return . Destruction is decreed , overflowing with righteousness .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:24** (✓) *target: people*
  > Isa 10:24 Therefore thus says the Lord God of hosts : “O my people , who dwell in Zion , be not afraid of the Assyrians when they strike with the rod and lift up their staff against you as the Egyptians did.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:10** (✓) *target: peoples*
  > Isa 11:10 In that day the root of Jesse , who shall stand as a signal for the peoples —of him shall the nations inquire , and his resting place shall be glorious .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:11** (✓) *target: people*
  > Isa 11:11 In that day the Lord will extend his hand yet a second time to recover the remnant that remains of his people , from Assyria , from Egypt , from Pathros , from Cush , from Elam , from Shinar , from Hamath , and from the coastlands of the sea .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:16** (✓) *target: people*
  > Isa 11:16 And there will be a highway from Assyria for the remnant that remains of his people , as there was for Israel when they came up from the land of Egypt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 12:4** (✓) *target: peoples*
  > Isa 12:4 And you will say in that day : “Give thanks to the Lord , call upon his name , make known his deeds among the peoples , proclaim that his name is exalted .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 13:4** (✓) *target: multitude*
  > Isa 13:4 The sound of a tumult is on the mountains as of a great multitude ! The sound of an uproar of kingdoms , of nations gathering together ! The Lord of hosts is mustering a host for battle .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 13:14** (✓) *target: people*
  > Isa 13:14 And like a hunted gazelle , or like sheep with none to gather them, each will turn to his own people , and each will flee to his own land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:2** (✓) *target: peoples*
  > Isa 14:2 And the peoples will take them and bring them to their place , and the house of Israel will possess them in the Lord’s land as male and female slaves . They will take captive those who were their captors , and rule over those who oppressed them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:6** (✓) *target: peoples*
  > Isa 14:6 that struck the peoples in wrath with unceasing blows , that ruled the nations in anger with unrelenting persecution .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:20** (✓) *target: people*
  > Isa 14:20 You will not be joined with them in burial , because you have destroyed your land , you have slain your people . “May the offspring of evildoers nevermore be named !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:32** (✓) *target: people*
  > Isa 14:32 What will one answer the messengers of the nation ? “The Lord has founded Zion , and in her the afflicted of his people find refuge .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 17:12** (✓) *target: peoples*
  > Isa 17:12 Ah , the thunder of many peoples ; they thunder like the thundering of the sea ! Ah, the roar of nations ; they roar like the roaring of mighty waters !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 18:2** (✓) *target: people*
  > Isa 18:2 which sends ambassadors by the sea , in vessels of papyrus on the waters ! Go , you swift messengers , to a nation tall and smooth , to a people feared near and far , a nation mighty and conquering , whose land the rivers divide .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 18:7** (✓) *target: people*
  > Isa 18:7 At that time tribute will be brought to the Lord of hosts from a people tall and smooth , from a people feared near and far , a nation mighty and conquering , whose land the rivers divide , to Mount Zion , the place of the name of the Lord of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 19:25** (✓) *target: people*
  > Isa 19:25 whom the Lord of hosts has blessed , saying , “ Blessed be Egypt my people , and Assyria the work of my hands , and Israel my inheritance .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 22:4** (✓) *target: people*
  > Isa 22:4 Therefore I said : “Look away from me; let me weep bitter tears ; do not labor to comfort me concerning the destruction of the daughter of my people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 23:13** (✓) *target: people*
  > Isa 23:13 Behold the land of the Chaldeans ! This is the people that was not ; Assyria destined it for wild beasts . They erected their siege towers , they stripped her palaces bare, they made her a ruin .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:2** (✓) *target: people*
  > Isa 24:2 And it shall be , as with the people , so with the priest ; as with the slave , so with his master ; as with the maid , so with her mistress ; as with the buyer , so with the seller ; as with the lender , so with the borrower ; as with the creditor , so with the debtor .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:4** (✓) *target: people*
  > Isa 24:4 The earth mourns and withers ; the world languishes and withers ; the highest people of the earth languish .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:13** (✓) *target: nations*
  > Isa 24:13 For thus it shall be in the midst of the earth among the nations , as when an olive tree is beaten , as at the gleaning when the grape harvest is done .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:3** (✓) *target: peoples*
  > Isa 25:3 Therefore strong peoples will glorify you; cities of ruthless nations will fear you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:6** (✓) *target: peoples*
  > Isa 25:6 On this mountain the Lord of hosts will make for all peoples a feast of rich food , a feast of well-aged wine , of rich food full of marrow , of aged wine well refined .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:7** (✓) *target: peoples*
  > Isa 25:7 And he will swallow up on this mountain the covering that is cast over all peoples , the veil that is spread over all nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:8** (✓) *target: people*
  > Isa 25:8 He will swallow up death forever ; and the Lord God will wipe away tears from all faces , and the reproach of his people he will take away from all the earth , for the Lord has spoken .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 26:11** (✓) *target: people*
  > Isa 26:11 O Lord , your hand is lifted up , but they do not see it. Let them see your zeal for your people , and be ashamed . Let the fire for your adversaries consume them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 1:9** (✓) *target: people*
  > Hos 1:9 And the Lord said , “ Call his name Not My People , for you are not my people , and I am not your God.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 1:10** (✓) *target: people*
  > Hos 1:10 Yet the number of the children of Israel shall be like the sand of the sea , which cannot be measured or numbered . And in the place where it was said to them, “You are not my people ,” it shall be said to them, “ Children of the living God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 2:1** (✓) *target: people*
  > Hos 2:1 Say to your brothers , “ You are my people ,” and to your sisters , “ You have received mercy .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 2:23** (✓) *target: People*
  > Hos 2:23 and I will sow her for myself in the land . And I will have mercy on No Mercy , and I will say to Not My People , ‘You are my people ’; and he shall say , ‘You are my God .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:4** (✓) *target: with you*
  > Hos 4:4 Yet let no one contend , and let none accuse , for with you is my contention , O priest .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:6** (✓) *target: people*
  > Hos 4:6 My people are destroyed for lack of knowledge ; because you have rejected knowledge , I reject you from being a priest to me. And since you have forgotten the law of your God , I also will forget your children .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:8** (✓) *target: people*
  > Hos 4:8 They feed on the sin of my people ; they are greedy for their iniquity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:9** (✓) *target: people*
  > Hos 4:9 And it shall be like people , like priest ; I will punish them for their ways and repay them for their deeds .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:12** (✓) *target: people*
  > Hos 4:12 My people inquire of a piece of wood , and their walking staff gives them oracles . For a spirit of whoredom has led them astray , and they have left their God to play the whore .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:14** (✓) *target: people*
  > Hos 4:14 I will not punish your daughters when they play the whore , nor your brides when they commit adultery ; for the men themselves go aside with prostitutes and sacrifice with cult prostitutes , and a people without understanding shall come to ruin .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 6:11** (✓) *target: people*
  > Hos 6:11 For you also , O Judah , a harvest is appointed . When I restore the fortunes of my people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 7:8** (✓) *target: peoples*
  > Hos 7:8 Ephraim mixes himself with the peoples ; Ephraim is a cake not turned .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 9:1** (✓) *target: peoples*
  > Hos 9:1 Rejoice not, O Israel ! Exult not like the peoples ; for you have played the whore , forsaking your God . You have loved a prostitute’s wages on all threshing floors .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:5** (✓) *target: people*
  > Hos 10:5 The inhabitants of Samaria tremble for the calf of Beth-aven . Its people mourn for it, and so do its idolatrous priests — those who rejoiced over it and over its glory — for it has departed from them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:10** (✓) *target: nations*
  > Hos 10:10 When I please , I will discipline them, and nations shall be gathered against them when they are bound up for their double iniquity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:14** (✓) *target: people*
  > Hos 10:14 therefore the tumult of war shall arise among your people , and all your fortresses shall be destroyed , as Shalman destroyed Beth-arbel on the day of battle ; mothers were dashed in pieces with their children .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 11:7** (✓) *target: people*
  > Hos 11:7 My people are bent on turning away from me, and though they call out to the Most High , he shall not raise them up at all .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:2** (✓) *target: people*
  > Joe 2:2 a day of darkness and gloom , a day of clouds and thick darkness ! Like blackness there is spread upon the mountains a great and powerful people ; their like has never been before , nor will be again after them through the years of all generations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:6** (✓) *target: peoples*
  > Joe 2:6 Before them peoples are in anguish ; all faces grow pale .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:16** (✓) *target: people*
  > Joe 2:16 gather the people . Consecrate the congregation ; assemble the elders ; gather the children , even nursing infants. Let the bridegroom leave his room , and the bride her chamber .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:17** (✓) *target: people*
  > Joe 2:17 Between the vestibule and the altar let the priests , the ministers of the Lord , weep and say , “ Spare your people , O Lord , and make not your heritage a reproach , a byword among the nations . Why should they say among the peoples , ‘ Where is their God ?’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:18** (✓) *target: people*
  > Joe 2:18 Then the Lord became jealous for his land and had pity on his people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:19** (✓) *target: people*
  > Joe 2:19 The Lord answered and said to his people , “ Behold , I am sending to you grain , wine , and oil , and you will be satisfied ; and I will no more make you a reproach among the nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:26** (✓) *target: people*
  > Joe 2:26 “You shall eat in plenty and be satisfied , and praise the name of the Lord your God , who has dealt wondrously with you. And my people shall never again be put to shame .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:27** (✓) *target: people*
  > Joe 2:27 You shall know that I am in the midst of Israel , and that I am the Lord your God and there is none else . And my people shall never again be put to shame .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:2** (✓) *target: people*
  > Joe 3:2 I will gather all the nations and bring them down to the Valley of Jehoshaphat . And I will enter into judgment with them there , on behalf of my people and my heritage Israel , because they have scattered them among the nations and have divided up my land ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:3** (✓) *target: people*
  > Joe 3:3 and have cast lots for my people , and have traded a boy for a prostitute , and have sold a girl for wine and have drunk it.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:16** (✓) *target: people*
  > Joe 3:16 The Lord roars from Zion , and utters his voice from Jerusalem , and the heavens and the earth quake . But the Lord is a refuge to his people , a stronghold to the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 1:5** (✓) *target: people*
  > Amo 1:5 I will break the gate-bar of Damascus , and cut off the inhabitants from the Valley of Aven , and him who holds the scepter from Beth-eden ; and the people of Syria shall go into exile to Kir ,” says the Lord .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 3:6** (✓) *target: people*
  > Amo 3:6 Is a trumpet blown in a city , and the people are not afraid ? Does disaster come to a city , unless the Lord has done it?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 7:8** (✓) *target: people*
  > Amo 7:8 And the Lord said to me, “ Amos , what do you see ?” And I said , “A plumb line .” Then the Lord said , “ Behold , I am setting a plumb line in the midst of my people Israel ; I will never again pass by them ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 7:15** (✓) *target: people*
  > Amo 7:15 But the Lord took me from following the flock , and the Lord said to me, ‘ Go , prophesy to my people Israel .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 8:2** (✓) *target: people*
  > Amo 8:2 And he said , “ Amos , what do you see ?” And I said , “A basket of summer fruit .” Then the Lord said to me , “The end has come upon my people Israel ; I will never again pass by them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 9:10** (✓) *target: people*
  > Amo 9:10 All the sinners of my people shall die by the sword , who say , ‘ Disaster shall not overtake or meet us.’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 9:14** (✓) *target: people*
  > Amo 9:14 I will restore the fortunes of my people Israel , and they shall rebuild the ruined cities and inhabit them; they shall plant vineyards and drink their wine , and they shall make gardens and eat their fruit .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Obd 13** (✓) *target: people*
  > Obd 13 Do not enter the gate of my people in the day of their calamity ; do not gloat over his disaster in the day of his calamity ; do not loot his wealth in the day of his calamity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jon 1:8** (✓) *target: people*
  > Jon 1:8 Then they said to him, “ Tell us on whose account this evil has come upon us. What is your occupation ? And where do you come from? What is your country ? And of what people are you ?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 1:2** (✓) *target: peoples*
  > Mic 1:2 Hear , you peoples , all of you; pay attention , O earth , and all that is in it, and let the Lord God be a witness against you, the Lord from his holy temple .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 1:9** (✓) *target: people*
  > Mic 1:9 For her wound is incurable , and it has come to Judah ; it has reached to the gate of my people , to Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:4** (✓) *target: people*
  > Mic 2:4 In that day they shall take up a taunt song against you and moan bitterly , and say , “We are utterly ruined ; he changes the portion of my people ; how he removes it from me! To an apostate he allots our fields .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:8** (✓) *target: people*
  > Mic 2:8 But lately my people have risen up as an enemy ; you strip the rich robe from those who pass by trustingly with no thought of war .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:9** (✓) *target: people*
  > Mic 2:9 The women of my people you drive out from their delightful houses ; from their young children you take away my splendor forever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:11** (✓) *target: people*
  > Mic 2:11 If a man should go about and utter wind and lies , saying, “I will preach to you of wine and strong drink ,” he would be the preacher for this people !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 3:3** (✓) *target: people*
  > Mic 3:3 who eat the flesh of my people , and flay their skin from off them, and break their bones in pieces and chop them up like meat in a pot , like flesh in a cauldron .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 3:5** (✓) *target: people*
  > Mic 3:5 Thus says the Lord concerning the prophets who lead my people astray , who cry “ Peace ” when they have something to eat , but declare war against him who puts nothing into their mouths .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:1** (✓) *target: peoples*
  > Mic 4:1 It shall come to pass in the latter days that the mountain of the house of the Lord shall be established as the highest of the mountains , and it shall be lifted up above the hills ; and peoples shall flow to it,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:3** (✓) *target: peoples*
  > Mic 4:3 He shall judge between many peoples , and shall decide disputes for strong nations far away; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:5** (✓) *target: peoples*
  > Mic 4:5 For all the peoples walk each in the name of its god , but we will walk in the name of the Lord our God forever and ever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:13** (✓) *target: peoples*
  > Mic 4:13 Arise and thresh , O daughter of Zion , for I will make your horn iron , and I will make your hoofs bronze ; you shall beat in pieces many peoples ; and shall devote their gain to the Lord , their wealth to the Lord of the whole earth .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 5:7** (✓) *target: peoples*
  > Mic 5:7 Then the remnant of Jacob shall be in the midst of many peoples like dew from the Lord , like showers on the grass , which delay not for a man nor wait for the children of man .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 5:8** (✓) *target: peoples*
  > Mic 5:8 And the remnant of Jacob shall be among the nations , in the midst of many peoples , like a lion among the beasts of the forest , like a young lion among the flocks of sheep , which , when it goes through, treads down and tears in pieces, and there is none to deliver .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:2** (✓) *target: people*
  > Mic 6:2 Hear , you mountains , the indictment of the Lord , and you enduring foundations of the earth , for the Lord has an indictment against his people , and he will contend with Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:3** (✓) *target: people*
  > Mic 6:3 “O my people , what have I done to you? How have I wearied you? Answer me !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:5** (✓) *target: people*
  > Mic 6:5 O my people , remember what Balak king of Moab devised , and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal , that you may know the righteous acts of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:16** (✓) *target: people*
  > Mic 6:16 For you have kept the statutes of Omri , and all the works of the house of Ahab ; and you have walked in their counsels , that I may make you a desolation , and your inhabitants a hissing ; so you shall bear the scorn of my people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 7:14** (✓) *target: people*
  > Mic 7:14 Shepherd your people with your staff , the flock of your inheritance , who dwell alone in a forest in the midst of a garden land ; let them graze in Bashan and Gilead as in the days of old .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Nah 3:18** (✓) *target: people*
  > Nah 3:18 Your shepherds are asleep , O king of Assyria ; your nobles slumber . Your people are scattered on the mountains with none to gather them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:5** (✓) *target: peoples*
  > Hab 2:5 “ Moreover , wine is a traitor , an arrogant man who is never at rest . His greed is as wide as Sheol ; like death he has never enough . He gathers for himself all nations and collects as his own all peoples .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:8** (✓) *target: peoples*
  > Hab 2:8 Because you have plundered many nations , all the remnant of the peoples shall plunder you, for the blood of man and violence to the earth , to cities and all who dwell in them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:10** (✓) *target: peoples*
  > Hab 2:10 You have devised shame for your house by cutting off many peoples ; you have forfeited your life .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2

**Group `5738-002`** (2 verses — anchors: Num 14:9, Num 14:11)

- **Num 14:9** 🔵 (✓) *target: people*
  > Num 14:9 Only do not rebel against the Lord . And do not fear the people of the land , for they are bread for us. Their protection is removed from them, and the Lord is with us; do not fear them .”
- **Num 14:11** 🔵 (✓) *target: people*
  > Num 14:11 And the Lord said to Moses , “ How long will this people despise me? And how long will they not believe in me, in spite of all the signs that I have done among them?

**Group `5738-003`** (1 verse — anchors: Exo 7:14)

- **Exo 7:14** 🔵 (✓) *target: people*
  > Exo 7:14 Then the Lord said to Moses , “ Pharaoh’s heart is hardened ; he refuses to let the people go .

### `H5971K` — 5/69 classified · 2 anchor verse(s)

**Group `5732-001`** (5 verses — anchors: Deu 20:1, Jos 8:1)

- **Deu 20:1** 🔵 (✓) *target: army*
  > Deu 20:1 “When you go out to war against your enemies , and see horses and chariots and an army larger than your own, you shall not be afraid of them, for the Lord your God is with you, who brought you up out of the land of Egypt .
- **Jos 8:1** 🔵 (✓) *target: men*
  > Jos 8:1 And the Lord said to Joshua , “Do not fear and do not be dismayed . Take all the fighting men with you, and arise , go up to Ai . See , I have given into your hand the king of Ai , and his people , his city , and his land .
- **Judg 7:3** (✓) *target: people*
  > Judg 7:3 Now therefore proclaim in the ears of the people , saying , ‘ Whoever is fearful and trembling , let him return home and hurry away from Mount Gilead .’” Then 22,000 of the people returned , and 10,000 remained .
- **Judg 11:20** (✓) *target: people*
  > Judg 11:20 but Sihon did not trust Israel to pass through his territory , so Sihon gathered all his people together and encamped at Jahaz and fought with Israel .
- **Judg 20:22** (✓) *target: people*
  > Judg 20:22 But the people , the men of Israel , took courage , and again formed the battle line in the same place where they had formed it on the first day .

**Group `UNCLASSIFIED`** (64 verses)

- **Exo 14:6** (—) *target: army*
  > Exo 14:6 So he made ready his chariot and took his army with him ,
- **Num 20:20** (—) *target: army*
  > Num 20:20 But he said , “You shall not pass through .” And Edom came out against them with a large army and with a strong force .
- **Num 31:32** (—) *target: army*
  > Num 31:32 Now the plunder remaining of the spoil that the army took was 675,000 sheep ,
- **Jos 8:3** (—) *target: men*
  > Jos 8:3 So Joshua and all the fighting men arose to go up to Ai . And Joshua chose 30,000 mighty men of valor and sent them out by night .
- **Jos 8:11** (—) *target: men*
  > Jos 8:11 And all the fighting men who were with him went up and drew near before the city and encamped on the north side of Ai , with a ravine between them and Ai .
- **Jos 8:13** (—) *target: forces*
  > Jos 8:13 So they stationed the forces , the main encampment that was north of the city and its rear guard west of the city . But Joshua spent that night in the valley .
- **Jos 11:4** (—) *target: horde*
  > Jos 11:4 And they came out with all their troops , a great horde , in number like the sand that is on the seashore , with very many horses and chariots .
- **Jos 11:7** (—) *target: warriors*
  > Jos 11:7 So Joshua and all his warriors came suddenly against them by the waters of Merom and fell upon them .
- **Judg 4:13** (—) *target: men*
  > Judg 4:13 Sisera called out all his chariots , 900 chariots of iron , and all the men who were with him, from Harosheth-hagoyim to the river Kishon .
- **Judg 7:1** (—) *target: people*
  > Judg 7:1 Then Jerubbaal (that is, Gideon ) and all the people who were with him rose early and encamped beside the spring of Harod . And the camp of Midian was north of them, by the hill of Moreh , in the valley .
- **Judg 7:2** (—) *target: people*
  > Judg 7:2 The Lord said to Gideon , “The people with you are too many for me to give the Midianites into their hand , lest Israel boast over me, saying , ‘My own hand has saved me .’
- **Judg 7:4** (—) *target: people*
  > Judg 7:4 And the Lord said to Gideon , “The people are still too many . Take them down to the water , and I will test them for you there , and anyone of whom I say to you, ‘ This one shall go with you,’ shall go with you, and anyone of whom I say to you, ‘ This one shall not go with you,’ shall not go .”
- **Judg 7:5** (—) *target: people*
  > Judg 7:5 So he brought the people down to the water . And the Lord said to Gideon , “Every one who laps the water with his tongue , as a dog laps , you shall set by himself . Likewise, every one who kneels down to drink .”
- **Judg 7:6** (—) *target: people*
  > Judg 7:6 And the number of those who lapped , putting their hands to their mouths , was 300 men , but all the rest of the people knelt down to drink water .
- **Judg 7:7** (—) *target: others*
  > Judg 7:7 And the Lord said to Gideon , “ With the 300 men who lapped I will save you and give the Midianites into your hand , and let all the others go every man to his home .”
- **Judg 7:8** (—) *target: people*
  > Judg 7:8 So the people took provisions in their hands , and their trumpets . And he sent all the rest of Israel every man to his tent , but retained the 300 men . And the camp of Midian was below him in the valley .
- **Judg 8:5** (—) *target: people*
  > Judg 8:5 So he said to the men of Succoth , “ Please give loaves of bread to the people who follow me, for they are exhausted , and I am pursuing after Zebah and Zalmunna , the kings of Midian .”
- **Judg 9:32** (—) *target: people*
  > Judg 9:32 Now therefore, go by night , you and the people who are with you, and set an ambush in the field .
- **Judg 9:33** (—) *target: people*
  > Judg 9:33 Then in the morning , as soon as the sun is up , rise early and rush upon the city . And when he and the people who are with him come out against you, you may do to them as your hand finds to do.”
- **Judg 9:34** (—) *target: men*
  > Judg 9:34 So Abimelech and all the men who were with him rose up by night and set an ambush against Shechem in four companies .
- **Judg 9:35** (—) *target: people*
  > Judg 9:35 And Gaal the son of Ebed went out and stood in the entrance of the gate of the city , and Abimelech and the people who were with him rose from the ambush .
- **Judg 9:36** (—) *target: people*
  > Judg 9:36 And when Gaal saw the people , he said to Zebul , “ Look , people are coming down from the mountaintops !” And Zebul said to him, “ You mistake the shadow of the mountains for men .”
- **Judg 9:37** (—) *target: people*
  > Judg 9:37 Gaal spoke again and said , “ Look , people are coming down from the center of the land , and one company is coming from the direction of the Diviners ’ Oak .”
- **Judg 9:38** (—) *target: people*
  > Judg 9:38 Then Zebul said to him, “Where is your mouth now , you who said , ‘Who is Abimelech , that we should serve him?’ Are not these the people whom you despised ? Go out now and fight with them .”
- **Judg 9:42** (—) *target: people*
  > Judg 9:42 On the following day , the people went out into the field , and Abimelech was told .
- **Judg 9:43** (—) *target: people*
  > Judg 9:43 He took his people and divided them into three companies and set an ambush in the fields . And he looked and saw the people coming out of the city . So he rose against them and killed them .
- **Judg 9:48** (—) *target: people*
  > Judg 9:48 And Abimelech went up to Mount Zalmon , he and all the people who were with him. And Abimelech took an axe in his hand and cut down a bundle of brushwood and took it up and laid it on his shoulder . And he said to the men who were with him, “ What you have seen me do , hurry and do as I have done .”
- **Judg 9:49** (—) *target: people*
  > Judg 9:49 So every one of the people cut down his bundle and following Abimelech put it against the stronghold , and they set the stronghold on fire over them, so that all the people of the Tower of Shechem also died , about 1,000 men and women .
- **Judg 11:21** (—) *target: people*
  > Judg 11:21 And the Lord , the God of Israel , gave Sihon and all his people into the hand of Israel , and they defeated them. So Israel took possession of all the land of the Amorites , who inhabited that country .
- **Judg 20:10** (—) *target: people*
  > Judg 20:10 and we will take ten men of a hundred throughout all the tribes of Israel , and a hundred of a thousand , and a thousand of ten thousand , to bring provisions for the people , that when they come they may repay Gibeah of Benjamin for all the outrage that they have committed in Israel .”
- **Judg 20:16** (—) *target: these*
  > Judg 20:16 Among all these were 700 chosen men who were left-handed ; every one could sling a stone at a hair and not miss .
- **Judg 20:26** (—) *target: army*
  > Judg 20:26 Then all the people of Israel , the whole army , went up and came to Bethel and wept . They sat there before the Lord and fasted that day until evening , and offered burnt offerings and peace offerings before the Lord .
- **Judg 20:31** (—) *target: people*
  > Judg 20:31 And the people of Benjamin went out against the people and were drawn away from the city . And as at other times they began to strike and kill some of the people in the highways , one of which goes up to Bethel and the other to Gibeah , and in the open country , about thirty men of Israel .
- **Judg 21:9** (—) *target: people*
  > Judg 21:9 For when the people were mustered , behold , not one of the inhabitants of Jabesh-gilead was there.
- **1Sa 13:5** (—) *target: troops*
  > 1Sa 13:5 And the Philistines mustered to fight with Israel , thirty thousand chariots and six thousand horsemen and troops like the sand on the seashore in multitude . They came up and encamped in Michmash , to the east of Beth-aven .
- **1Sa 26:5** (—) *target: army*
  > 1Sa 26:5 Then David rose and came to the place where Saul had encamped . And David saw the place where Saul lay , with Abner the son of Ner , the commander of his army . Saul was lying within the encampment , while the army was encamped around him .
- **1Sa 26:7** (—) *target: army*
  > 1Sa 26:7 So David and Abishai went to the army by night . And there lay Saul sleeping within the encampment , with his spear stuck in the ground at his head , and Abner and the army lay around him .
- **1Sa 26:14** (—) *target: army*
  > 1Sa 26:14 And David called to the army , and to Abner the son of Ner , saying , “Will you not answer , Abner ?” Then Abner answered , “ Who are you who calls to the king ?”
- **2Sa 2:27** (—) *target: men*
  > 2Sa 2:27 And Joab said , “As God lives , if you had not spoken , surely the men would not have given up the pursuit of their brothers until the morning .”
- **2Sa 2:28** (—) *target: men*
  > 2Sa 2:28 So Joab blew the trumpet , and all the men stopped and pursued Israel no more, nor did they fight anymore .
- **2Sa 10:10** (—) *target: men*
  > 2Sa 10:10 The rest of his men he put in the charge of Abishai his brother , and he arrayed them against the Ammonites .
- **2Sa 18:1** (—) *target: men*
  > 2Sa 18:1 Then David mustered the men who were with him and set over them commanders of thousands and commanders of hundreds .
- **2Sa 18:2** (—) *target: army*
  > 2Sa 18:2 And David sent out the army , one third under the command of Joab , one third under the command of Abishai the son of Zeruiah , Joab’s brother , and one third under the command of Ittai the Gittite . And the king said to the men , “I myself will also go out with you .”
- **2Sa 18:3** (—) *target: men*
  > 2Sa 18:3 But the men said , “You shall not go out . For if we flee , they will not care about us. If half of us die , they will not care about us. But you are worth ten thousand of us. Therefore it is better that you send us help from the city .”
- **2Sa 18:4** (—) *target: army*
  > 2Sa 18:4 The king said to them, “ Whatever seems best to you I will do .” So the king stood at the side of the gate , while all the army marched out by hundreds and by thousands .
- **2Sa 18:6** (—) *target: army*
  > 2Sa 18:6 So the army went out into the field against Israel , and the battle was fought in the forest of Ephraim .
- **2Sa 18:7** (—) *target: men*
  > 2Sa 18:7 And the men of Israel were defeated there by the servants of David , and the loss there was great on that day , twenty thousand men.
- **2Sa 18:16** (—) *target: troops*
  > 2Sa 18:16 Then Joab blew the trumpet , and the troops came back from pursuing Israel , for Joab restrained them .
- **2Sa 20:15** (—) *target: men*
  > 2Sa 20:15 And all the men who were with Joab came and besieged him in Abel of Beth-maacah . They cast up a mound against the city , and it stood against the rampart , and they were battering the wall to throw it down .
- **2Sa 23:10** (—) *target: men*
  > 2Sa 23:10 He rose and struck down the Philistines until his hand was weary , and his hand clung to the sword . And the Lord brought about a great victory that day , and the men returned after him only to strip the slain.
- **2Sa 23:11** (—) *target: men*
  > 2Sa 23:11 And next to him was Shammah , the son of Agee the Hararite . The Philistines gathered together at Lehi , where there was a plot of ground full of lentils , and the men fled from the Philistines .
- **1Ki 16:15** (—) *target: troops*
  > 1Ki 16:15 In the twenty-seventh year of Asa king of Judah , Zimri reigned seven days in Tirzah . Now the troops were encamped against Gibbethon , which belonged to the Philistines ,
- **1Ki 16:16** (—) *target: troops*
  > 1Ki 16:16 and the troops who were encamped heard it said , “ Zimri has conspired , and he has killed the king .” Therefore all Israel made Omri , the commander of the army , king over Israel that day in the camp .
- **2Ki 8:21** (—) *target: army*
  > 2Ki 8:21 Then Joram passed over to Zair with all his chariots and rose by night , and he and his chariot commanders struck the Edomites who had surrounded him, but his army fled home .
- **2Ki 13:7** (—) *target: army*
  > 2Ki 13:7 For there was not left to Jehoahaz an army of more than fifty horsemen and ten chariots and ten thousand footmen , for the king of Syria had destroyed them and made them like the dust at threshing .
- **1Ch 11:13** (—) *target: men*
  > 1Ch 11:13 He was with David at Pas-dammim when the Philistines were gathered there for battle . There was a plot of ground full of barley , and the men fled from the Philistines .
- **1Ch 19:7** (—) *target: army*
  > 1Ch 19:7 They hired 32,000 chariots and the king of Maacah with his army , who came and encamped before Medeba . And the Ammonites were mustered from their cities and came to battle .
- **1Ch 19:11** (—) *target: men*
  > 1Ch 19:11 The rest of his men he put in the charge of Abishai his brother , and they were arrayed against the Ammonites .
- **1Ch 21:2** (—) *target: army*
  > 1Ch 21:2 So David said to Joab and the commanders of the army , “ Go , number Israel , from Beersheba to Dan , and bring me a report, that I may know their number .”
- **Eze 17:15** (—) *target: army*
  > Eze 17:15 But he rebelled against him by sending his ambassadors to Egypt , that they might give him horses and a large army . Will he thrive ? Can one escape who does such things ? Can he break the covenant and yet escape ?
- **Eze 26:7** (—) *target: soldiers*
  > Eze 26:7 “ For thus says the Lord God : Behold , I will bring against Tyre from the north Nebuchadnezzar king of Babylon , king of kings , with horses and chariots , and with horsemen and a host of many soldiers .
- **Dan 11:15** (—) *target: troops*
  > Dan 11:15 Then the king of the north shall come and throw up siegeworks and take a well-fortified city . And the forces of the south shall not stand , or even his best troops , for there shall be no strength to stand .
- **Joe 2:5** (—) *target: army*
  > Joe 2:5 As with the rumbling of chariots , they leap on the tops of the mountains , like the crackling of a flame of fire devouring the stubble , like a powerful army drawn up for battle .
- **Nah 3:13** (—) *target: troops*
  > Nah 3:13 Behold , your troops are women in your midst . The gates of your land are wide open to your enemies ; fire has devoured your bars .

### `H5971L` — 430/430 classified · 5 anchor verse(s)

**Group `5739-001`** (427 verses — anchors: Num 11:29, Num 14:19)

- **Num 11:29** 🔵 (✓) *target: people*
  > Num 11:29 But Moses said to him, “Are you jealous for my sake? Would that all the Lord’s people were prophets , that the Lord would put his Spirit on them !”
- **Num 14:19** 🔵 (✓) *target: people*
  > Num 14:19 Please pardon the iniquity of this people , according to the greatness of your steadfast love , just as you have forgiven this people , from Egypt until now .”
- **Gen 11:6** (✓) *target: people*
  > Gen 11:6 And the Lord said , “Behold, they are one people , and they have all one language , and this is only the beginning of what they will do . And nothing that they propose to do will now be impossible for them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 14:16** (✓) *target: people*
  > Gen 14:16 Then he brought back all the possessions , and also brought back his kinsman Lot with his possessions , and the women and the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 17:16** (✓) *target: peoples*
  > Gen 17:16 I will bless her , and moreover , I will give you a son by her. I will bless her, and she shall become nations ; kings of peoples shall come from her .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 19:4** (✓) *target: people*
  > Gen 19:4 But before they lay down , the men of the city , the men of Sodom , both young and old , all the people to the last man , surrounded the house .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:7** (✓) *target: people*
  > Gen 23:7 Abraham rose and bowed to the Hittites , the people of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:11** (✓) *target: people*
  > Gen 23:11 “ No , my lord , hear me : I give you the field , and I give you the cave that is in it. In the sight of the sons of my people I give it to you. Bury your dead .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:12** (✓) *target: people*
  > Gen 23:12 Then Abraham bowed down before the people of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 23:13** (✓) *target: people*
  > Gen 23:13 And he said to Ephron in the hearing of the people of the land , “But if you will, hear me: I give the price of the field . Accept it from me, that I may bury my dead there .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 26:10** (✓) *target: people*
  > Gen 26:10 Abimelech said , “ What is this you have done to us? One of the people might easily have lain with your wife , and you would have brought guilt upon us.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 26:11** (✓) *target: people*
  > Gen 26:11 So Abimelech warned all the people , saying , “Whoever touches this man or his wife shall surely be put to death .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 27:29** (✓) *target: peoples*
  > Gen 27:29 Let peoples serve you, and nations bow down to you. Be lord over your brothers , and may your mother’s sons bow down to you. Cursed be everyone who curses you, and blessed be everyone who blesses you!”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 28:3** (✓) *target: peoples*
  > Gen 28:3 God Almighty bless you and make you fruitful and multiply you, that you may become a company of peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 32:7** (✓) *target: people*
  > Gen 32:7 Then Jacob was greatly afraid and distressed . He divided the people who were with him, and the flocks and herds and camels , into two camps ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 33:15** (✓) *target: people*
  > Gen 33:15 So Esau said , “ Let me leave with you some of the people who are with me.” But he said , “ What need is there ? Let me find favor in the sight of my lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 34:16** (✓) *target: people*
  > Gen 34:16 Then we will give our daughters to you, and we will take your daughters to ourselves, and we will dwell with you and become one people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 34:22** (✓) *target: people*
  > Gen 34:22 Only on this condition will the men agree to dwell with us to become one people —when every male among us is circumcised as they are circumcised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 35:6** (✓) *target: people*
  > Gen 35:6 And Jacob came to Luz (that is, Bethel ), which is in the land of Canaan , he and all the people who were with him ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 41:40** (✓) *target: people*
  > Gen 41:40 You shall be over my house , and all my people shall order themselves as you command . Only as regards the throne will I be greater than you .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 41:55** (✓) *target: people*
  > Gen 41:55 When all the land of Egypt was famished , the people cried to Pharaoh for bread . Pharaoh said to all the Egyptians , “ Go to Joseph . What he says to you, do .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 42:6** (✓) *target: people*
  > Gen 42:6 Now Joseph was governor over the land . He was the one who sold to all the people of the land . And Joseph’s brothers came and bowed themselves before him with their faces to the ground .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 47:21** (✓) *target: people*
  > Gen 47:21 As for the people , he made servants of them from one end of Egypt to the other .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 47:23** (✓) *target: people*
  > Gen 47:23 Then Joseph said to the people , “ Behold , I have this day bought you and your land for Pharaoh . Now here is seed for you, and you shall sow the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 48:4** (✓) *target: peoples*
  > Gen 48:4 and said to me, ‘ Behold , I will make you fruitful and multiply you, and I will make of you a company of peoples and will give this land to your offspring after you for an everlasting possession .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 48:19** (✓) *target: people*
  > Gen 48:19 But his father refused and said , “I know , my son , I know . He also shall become a people , and he also shall be great . Nevertheless , his younger brother shall be greater than he, and his offspring shall become a multitude of nations .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 49:10** (✓) *target: peoples*
  > Gen 49:10 The scepter shall not depart from Judah , nor the ruler’s staff from between his feet , until tribute comes to him; and to him shall be the obedience of the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 49:16** (✓) *target: people*
  > Gen 49:16 “ Dan shall judge his people as one of the tribes of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Gen 50:20** (✓) *target: people*
  > Gen 50:20 As for you , you meant evil against me, but God meant it for good , to bring it about that many people should be kept alive , as they are today .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:9** (✓) *target: people*
  > Exo 1:9 And he said to his people , “ Behold , the people of Israel are too many and too mighty for us .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:20** (✓) *target: people*
  > Exo 1:20 So God dealt well with the midwives . And the people multiplied and grew very strong .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 1:22** (✓) *target: people*
  > Exo 1:22 Then Pharaoh commanded all his people , “ Every son that is born to the Hebrews you shall cast into the Nile , but you shall let every daughter live .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:7** (✓) *target: people*
  > Exo 3:7 Then the Lord said , “I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters . I know their sufferings ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:10** (✓) *target: people*
  > Exo 3:10 Come , I will send you to Pharaoh that you may bring my people , the children of Israel , out of Egypt .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:12** (✓) *target: people*
  > Exo 3:12 He said , “ But I will be with you, and this shall be the sign for you, that I have sent you: when you have brought the people out of Egypt , you shall serve God on this mountain .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 3:21** (✓) *target: people*
  > Exo 3:21 And I will give this people favor in the sight of the Egyptians ; and when you go , you shall not go empty ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:16** (✓) *target: people*
  > Exo 4:16 He shall speak for you to the people , and he shall be your mouth , and you shall be as God to him.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:21** (✓) *target: people*
  > Exo 4:21 And the Lord said to Moses , “ When you go back to Egypt , see that you do before Pharaoh all the miracles that I have put in your power . But I will harden his heart , so that he will not let the people go .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:30** (✓) *target: people*
  > Exo 4:30 Aaron spoke all the words that the Lord had spoken to Moses and did the signs in the sight of the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 4:31** (✓) *target: people*
  > Exo 4:31 And the people believed ; and when they heard that the Lord had visited the people of Israel and that he had seen their affliction , they bowed their heads and worshiped .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:1** (✓) *target: people*
  > Exo 5:1 Afterward Moses and Aaron went and said to Pharaoh , “Thus says the Lord , the God of Israel , ‘Let my people go , that they may hold a feast to me in the wilderness .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:4** (✓) *target: people*
  > Exo 5:4 But the king of Egypt said to them, “ Moses and Aaron , why do you take the people away from their work ? Get back to your burdens .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:5** (✓) *target: people*
  > Exo 5:5 And Pharaoh said , “ Behold , the people of the land are now many , and you make them rest from their burdens !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:6** (✓) *target: people*
  > Exo 5:6 The same day Pharaoh commanded the taskmasters of the people and their foremen ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:7** (✓) *target: people*
  > Exo 5:7 “You shall no longer give the people straw to make bricks , as in the past ; let them go and gather straw for themselves.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:10** (✓) *target: people*
  > Exo 5:10 So the taskmasters and the foremen of the people went out and said to the people , “Thus says Pharaoh , ‘ I will not give you straw .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:12** (✓) *target: people*
  > Exo 5:12 So the people were scattered throughout all the land of Egypt to gather stubble for straw .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:16** (✓) *target: people*
  > Exo 5:16 No straw is given to your servants , yet they say to us, ‘ Make bricks !’ And behold, your servants are beaten ; but the fault is in your own people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:22** (✓) *target: people*
  > Exo 5:22 Then Moses turned to the Lord and said , “O Lord , why have you done evil to this people ? Why did you ever send me ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 5:23** (✓) *target: people*
  > Exo 5:23 For since I came to Pharaoh to speak in your name , he has done evil to this people , and you have not delivered your people at all .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 6:7** (✓) *target: people*
  > Exo 6:7 I will take you to be my people , and I will be your God , and you shall know that I am the Lord your God , who has brought you out from under the burdens of the Egyptians .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 7:4** (✓) *target: people*
  > Exo 7:4 Pharaoh will not listen to you. Then I will lay my hand on Egypt and bring my hosts , my people the children of Israel , out of the land of Egypt by great acts of judgment .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 7:16** (✓) *target: people*
  > Exo 7:16 And you shall say to him, ‘The Lord , the God of the Hebrews , sent me to you, saying , “Let my people go , that they may serve me in the wilderness .” But so far , you have not obeyed .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:1** (✓) *target: people*
  > Exo 8:1 Then the Lord said to Moses , “ Go in to Pharaoh and say to him, ‘ Thus says the Lord , “Let my people go , that they may serve me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:3** (✓) *target: people*
  > Exo 8:3 The Nile shall swarm with frogs that shall come up into your house and into your bedroom and on your bed and into the houses of your servants and your people , and into your ovens and your kneading bowls .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:4** (✓) *target: people*
  > Exo 8:4 The frogs shall come up on you and on your people and on all your servants .”’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:8** (✓) *target: people*
  > Exo 8:8 Then Pharaoh called Moses and Aaron and said , “ Plead with the Lord to take away the frogs from me and from my people , and I will let the people go to sacrifice to the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:9** (✓) *target: people*
  > Exo 8:9 Moses said to Pharaoh , “Be pleased to command me when I am to plead for you and for your servants and for your people , that the frogs be cut off from you and your houses and be left only in the Nile .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:11** (✓) *target: people*
  > Exo 8:11 The frogs shall go away from you and your houses and your servants and your people . They shall be left only in the Nile .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:20** (✓) *target: people*
  > Exo 8:20 Then the Lord said to Moses , “Rise up early in the morning and present yourself to Pharaoh , as he goes out to the water , and say to him, ‘ Thus says the Lord , “Let my people go , that they may serve me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Exo 8:21** (✓) *target: people*
  > Exo 8:21 Or else, if you will not let my people go , behold, I will send swarms of flies on you and your servants and your people , and into your houses . And the houses of the Egyptians shall be filled with swarms of flies , and also the ground on which they stand.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 5:21** (✓) *target: people*
  > Num 5:21 then’ (let the priest make the woman take the oath of the curse , and say to the woman ) ‘the Lord make you a curse and an oath among your people , when the Lord makes your thigh fall away and your body swell .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 5:27** (✓) *target: people*
  > Num 5:27 And when he has made her drink the water , then, if she has defiled herself and has broken faith with her husband , the water that brings the curse shall enter into her and cause bitter pain , and her womb shall swell , and her thigh shall fall away , and the woman shall become a curse among her people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:1** (✓) *target: people*
  > Num 11:1 And the people complained in the hearing of the Lord about their misfortunes , and when the Lord heard it, his anger was kindled , and the fire of the Lord burned among them and consumed some outlying parts of the camp .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:2** (✓) *target: people*
  > Num 11:2 Then the people cried out to Moses , and Moses prayed to the Lord , and the fire died down .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:8** (✓) *target: people*
  > Num 11:8 The people went about and gathered it and ground it in handmills or beat it in mortars and boiled it in pots and made cakes of it. And the taste of it was like the taste of cakes baked with oil .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:10** (✓) *target: people*
  > Num 11:10 Moses heard the people weeping throughout their clans , everyone at the door of his tent . And the anger of the Lord blazed hotly , and Moses was displeased .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:11** (✓) *target: people*
  > Num 11:11 Moses said to the Lord , “ Why have you dealt ill with your servant ? And why have I not found favor in your sight , that you lay the burden of all this people on me ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:12** (✓) *target: people*
  > Num 11:12 Did I conceive all this people ? Did I give them birth , that you should say to me, ‘ Carry them in your bosom , as a nurse carries a nursing child ,’ to the land that you swore to give their fathers ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:13** (✓) *target: people*
  > Num 11:13 Where am I to get meat to give to all this people ? For they weep before me and say , ‘ Give us meat , that we may eat .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:14** (✓) *target: people*
  > Num 11:14 I am not able to carry all this people alone ; the burden is too heavy for me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:16** (✓) *target: people*
  > Num 11:16 Then the Lord said to Moses , “ Gather for me seventy men of the elders of Israel , whom you know to be the elders of the people and officers over them, and bring them to the tent of meeting , and let them take their stand there with you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:17** (✓) *target: people*
  > Num 11:17 And I will come down and talk with you there . And I will take some of the Spirit that is on you and put it on them, and they shall bear the burden of the people with you, so that you may not bear it yourself alone .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:18** (✓) *target: people*
  > Num 11:18 And say to the people , ‘ Consecrate yourselves for tomorrow , and you shall eat meat , for you have wept in the hearing of the Lord , saying , “ Who will give us meat to eat ? For it was better for us in Egypt .” Therefore the Lord will give you meat , and you shall eat .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:21** (✓) *target: people*
  > Num 11:21 But Moses said , “The people among whom I am number six hundred thousand on foot , and you have said , ‘I will give them meat , that they may eat a whole month !’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:24** (✓) *target: people*
  > Num 11:24 So Moses went out and told the people the words of the Lord . And he gathered seventy men of the elders of the people and placed them around the tent .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:32** (✓) *target: people*
  > Num 11:32 And the people rose all that day and all night and all the next day , and gathered the quail . Those who gathered least gathered ten homers . And they spread them out for themselves all around the camp .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:33** (✓) *target: people*
  > Num 11:33 While the meat was yet between their teeth , before it was consumed , the anger of the Lord was kindled against the people , and the Lord struck down the people with a very great plague .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:34** (✓) *target: people*
  > Num 11:34 Therefore the name of that place was called Kibroth-hattaavah , because there they buried the people who had the craving .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 11:35** (✓) *target: people*
  > Num 11:35 From Kibroth-hattaavah the people journeyed to Hazeroth , and they remained at Hazeroth .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 12:15** (✓) *target: people*
  > Num 12:15 So Miriam was shut outside the camp seven days , and the people did not set out on the march till Miriam was brought in again.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 12:16** (✓) *target: people*
  > Num 12:16 After that the people set out from Hazeroth , and camped in the wilderness of Paran .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:18** (✓) *target: people*
  > Num 13:18 and see what the land is, and whether the people who dwell in it are strong or weak , whether they are few or many ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:28** (✓) *target: people*
  > Num 13:28 However , the people who dwell in the land are strong , and the cities are fortified and very large . And besides , we saw the descendants of Anak there .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:30** (✓) *target: people*
  > Num 13:30 But Caleb quieted the people before Moses and said , “Let us go up at once and occupy it, for we are well able to overcome it .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:31** (✓) *target: people*
  > Num 13:31 Then the men who had gone up with him said , “We are not able to go up against the people , for they are stronger than we are.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 13:32** (✓) *target: people*
  > Num 13:32 So they brought to the people of Israel a bad report of the land that they had spied out , saying , “The land , through which we have gone to spy it out , is a land that devours its inhabitants , and all the people that we saw in it are of great height .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:1** (✓) *target: people*
  > Num 14:1 Then all the congregation raised a loud cry , and the people wept that night .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:13** (✓) *target: people*
  > Num 14:13 But Moses said to the Lord , “Then the Egyptians will hear of it, for you brought up this people in your might from among them,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:14** (✓) *target: people*
  > Num 14:14 and they will tell the inhabitants of this land . They have heard that you , O Lord , are in the midst of this people . For you , O Lord , are seen face to face , and your cloud stands over them and you go before them, in a pillar of cloud by day and in a pillar of fire by night .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:15** (✓) *target: people*
  > Num 14:15 Now if you kill this people as one man , then the nations who have heard your fame will say ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:16** (✓) *target: people*
  > Num 14:16 ‘It is because the Lord was not able to bring this people into the land that he swore to give to them that he has killed them in the wilderness .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 14:39** (✓) *target: people*
  > Num 14:39 When Moses told these words to all the people of Israel , the people mourned greatly .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 15:26** (✓) *target: population*
  > Num 15:26 And all the congregation of the people of Israel shall be forgiven , and the stranger who sojourns among them, because the whole population was involved in the mistake .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 15:30** (✓) *target: people*
  > Num 15:30 But the person who does anything with a high hand , whether he is native or a sojourner , reviles the Lord , and that person shall be cut off from among his people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 16:41** (✓) *target: people*
  > Num 16:41 But on the next day all the congregation of the people of Israel grumbled against Moses and against Aaron , saying , “ You have killed the people of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 16:47** (✓) *target: people*
  > Num 16:47 So Aaron took it as Moses said and ran into the midst of the assembly . And behold , the plague had already begun among the people . And he put on the incense and made atonement for the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 20:1** (✓) *target: people*
  > Num 20:1 And the people of Israel , the whole congregation , came into the wilderness of Zin in the first month , and the people stayed in Kadesh . And Miriam died there and was buried there .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 20:3** (✓) *target: people*
  > Num 20:3 And the people quarreled with Moses and said , “Would that we had perished when our brothers perished before the Lord !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:2** (✓) *target: people*
  > Num 21:2 And Israel vowed a vow to the Lord and said , “ If you will indeed give this people into my hand , then I will devote their cities to destruction.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:4** (✓) *target: people*
  > Num 21:4 From Mount Hor they set out by the way to the Red Sea , to go around the land of Edom . And the people became impatient on the way .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:5** (✓) *target: people*
  > Num 21:5 And the people spoke against God and against Moses , “ Why have you brought us up out of Egypt to die in the wilderness ? For there is no food and no water , and we loathe this worthless food .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:6** (✓) *target: people*
  > Num 21:6 Then the Lord sent fiery serpents among the people , and they bit the people , so that many people of Israel died .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:7** (✓) *target: people*
  > Num 21:7 And the people came to Moses and said , “We have sinned , for we have spoken against the Lord and against you. Pray to the Lord , that he take away the serpents from us.” So Moses prayed for the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:16** (✓) *target: people*
  > Num 21:16 And from there they continued to Beer ; that is the well of which the Lord said to Moses , “ Gather the people together, so that I may give them water .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:18** (✓) *target: people*
  > Num 21:18 the well that the princes made , that the nobles of the people dug , with the scepter and with their staffs .” And from the wilderness they went on to Mattanah ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:23** (✓) *target: people*
  > Num 21:23 But Sihon would not allow Israel to pass through his territory . He gathered all his people together and went out against Israel to the wilderness and came to Jahaz and fought against Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:29** (✓) *target: people*
  > Num 21:29 Woe to you, O Moab ! You are undone , O people of Chemosh ! He has made his sons fugitives , and his daughters captives , to an Amorite king , Sihon .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:33** (✓) *target: people*
  > Num 21:33 Then they turned and went up by the way to Bashan . And Og the king of Bashan came out against them , he and all his people , to battle at Edrei .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:34** (✓) *target: people*
  > Num 21:34 But the Lord said to Moses , “Do not fear him, for I have given him into your hand , and all his people , and his land . And you shall do to him as you did to Sihon king of the Amorites , who lived at Heshbon .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 21:35** (✓) *target: people*
  > Num 21:35 So they defeated him and his sons and all his people , until he had no survivor left . And they possessed his land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:3** (✓) *target: people*
  > Num 22:3 And Moab was in great dread of the people , because they were many . Moab was overcome with fear of the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:5** (✓) *target: Amaw*
  > Num 22:5 sent messengers to Balaam the son of Beor at Pethor , which is near the River in the land of the people of Amaw , to call him, saying , “ Behold , a people has come out of Egypt . They cover the face of the earth , and they are dwelling opposite me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:6** (✓) *target: people*
  > Num 22:6 Come now , curse this people for me, since they are too mighty for me. Perhaps I shall be able to defeat them and drive them from the land , for I know that he whom you bless is blessed , and he whom you curse is cursed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:11** (✓) *target: people*
  > Num 22:11 ‘ Behold , a people has come out of Egypt , and it covers the face of the earth . Now come , curse them for me. Perhaps I shall be able to fight against them and drive them out.’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:12** (✓) *target: people*
  > Num 22:12 God said to Balaam , “You shall not go with them. You shall not curse the people , for they are blessed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Num 22:17** (✓) *target: people*
  > Num 22:17 for I will surely do you great honor, and whatever you say to me I will do. Come , curse this people for me.’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:2** (✓) *target: people*
  > Jos 1:2 “ Moses my servant is dead . Now therefore arise , go over this Jordan , you and all this people , into the land that I am giving to them, to the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:6** (✓) *target: people*
  > Jos 1:6 Be strong and courageous , for you shall cause this people to inherit the land that I swore to their fathers to give them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:10** (✓) *target: people*
  > Jos 1:10 And Joshua commanded the officers of the people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 1:11** (✓) *target: people*
  > Jos 1:11 “ Pass through the midst of the camp and command the people , ‘ Prepare your provisions , for within three days you are to pass over this Jordan to go in to take possession of the land that the Lord your God is giving you to possess .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:3** (✓) *target: people*
  > Jos 3:3 and commanded the people , “ As soon as you see the ark of the covenant of the Lord your God being carried by the Levitical priests , then you shall set out from your place and follow it .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:5** (✓) *target: people*
  > Jos 3:5 Then Joshua said to the people , “ Consecrate yourselves, for tomorrow the Lord will do wonders among you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:6** (✓) *target: people*
  > Jos 3:6 And Joshua said to the priests , “Take up the ark of the covenant and pass on before the people .” So they took up the ark of the covenant and went before the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:14** (✓) *target: people*
  > Jos 3:14 So when the people set out from their tents to pass over the Jordan with the priests bearing the ark of the covenant before the people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 3:16** (✓) *target: people*
  > Jos 3:16 the waters coming down from above stood and rose up in a heap very far away, at Adam , the city that is beside Zarethan , and those flowing down toward the Sea of the Arabah , the Salt Sea , were completely cut off . And the people passed over opposite Jericho .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:2** (✓) *target: people*
  > Jos 4:2 “ Take twelve men from the people , from each tribe a man ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:10** (✓) *target: people*
  > Jos 4:10 For the priests bearing the ark stood in the midst of the Jordan until everything was finished that the Lord commanded Joshua to tell the people , according to all that Moses had commanded Joshua . The people passed over in haste .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:11** (✓) *target: people*
  > Jos 4:11 And when all the people had finished passing over , the ark of the Lord and the priests passed over before the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:19** (✓) *target: people*
  > Jos 4:19 The people came up out of the Jordan on the tenth day of the first month , and they encamped at Gilgal on the east border of Jericho .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 4:24** (✓) *target: peoples*
  > Jos 4:24 so that all the peoples of the earth may know that the hand of the Lord is mighty , that you may fear the Lord your God forever .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 5:4** (✓) *target: people*
  > Jos 5:4 And this is the reason why Joshua circumcised them: all the males of the people who came out of Egypt , all the men of war , had died in the wilderness on the way after they had come out of Egypt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 5:5** (✓) *target: people*
  > Jos 5:5 Though all the people who came out had been circumcised , yet all the people who were born on the way in the wilderness after they had come out of Egypt had not been circumcised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:5** (✓) *target: people*
  > Jos 6:5 And when they make a long blast with the ram’s horn , when you hear the sound of the trumpet , then all the people shall shout with a great shout , and the wall of the city will fall down flat , and the people shall go up , everyone straight before him .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:7** (✓) *target: people*
  > Jos 6:7 And he said to the people , “Go forward . March around the city and let the armed men pass on before the ark of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:8** (✓) *target: people*
  > Jos 6:8 And just as Joshua had commanded the people , the seven priests bearing the seven trumpets of rams’ horns before the Lord went forward , blowing the trumpets , with the ark of the covenant of the Lord following them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:10** (✓) *target: people*
  > Jos 6:10 But Joshua commanded the people , “You shall not shout or make your voice heard , neither shall any word go out of your mouth , until the day I tell you to shout . Then you shall shout .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:16** (✓) *target: people*
  > Jos 6:16 And at the seventh time , when the priests had blown the trumpets , Joshua said to the people , “ Shout , for the Lord has given you the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 6:20** (✓) *target: people*
  > Jos 6:20 So the people shouted , and the trumpets were blown . As soon as the people heard the sound of the trumpet , the people shouted a great shout , and the wall fell down flat , so that the people went up into the city , every man straight before him, and they captured the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:3** (✓) *target: people*
  > Jos 7:3 And they returned to Joshua and said to him, “Do not have all the people go up , but let about two or three thousand men go up and attack Ai . Do not make the whole people toil up there , for they are few .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:4** (✓) *target: people*
  > Jos 7:4 So about three thousand men went up there from the people . And they fled before the men of Ai ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:5** (✓) *target: people*
  > Jos 7:5 and the men of Ai killed about thirty-six of their men and chased them before the gate as far as Shebarim and struck them at the descent . And the hearts of the people melted and became as water .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:7** (✓) *target: people*
  > Jos 7:7 And Joshua said , “ Alas , O Lord God , why have you brought this people over the Jordan at all, to give us into the hands of the Amorites , to destroy us? Would that we had been content to dwell beyond the Jordan !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 7:13** (✓) *target: people*
  > Jos 7:13 Get up ! Consecrate the people and say , ‘ Consecrate yourselves for tomorrow ; for thus says the Lord , God of Israel , “There are devoted things in your midst , O Israel . You cannot stand before your enemies until you take away the devoted things from among you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:1** (✓) *target: men*
  > Jos 8:1 And the Lord said to Joshua , “Do not fear and do not be dismayed . Take all the fighting men with you, and arise , go up to Ai . See , I have given into your hand the king of Ai , and his people , his city , and his land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:5** (✓) *target: people*
  > Jos 8:5 And I and all the people who are with me will approach the city . And when they come out against us just as before , we shall flee before them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:9** (✓) *target: people*
  > Jos 8:9 So Joshua sent them out . And they went to the place of ambush and lay between Bethel and Ai , to the west of Ai , but Joshua spent that night among the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:10** (✓) *target: people*
  > Jos 8:10 Joshua arose early in the morning and mustered the people and went up , he and the elders of Israel , before the people to Ai .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:14** (✓) *target: people*
  > Jos 8:14 And as soon as the king of Ai saw this, he and all his people , the men of the city , hurried and went out early to the appointed place toward the Arabah to meet Israel in battle . But he did not know that there was an ambush against him behind the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:16** (✓) *target: people*
  > Jos 8:16 So all the people who were in the city were called together to pursue them, and as they pursued Joshua they were drawn away from the city .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:20** (✓) *target: people*
  > Jos 8:20 So when the men of Ai looked back , behold , the smoke of the city went up to heaven , and they had no power to flee this way or that, for the people who fled to the wilderness turned back against the pursuers .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 8:33** (✓) *target: people*
  > Jos 8:33 And all Israel , sojourner as well as native born , with their elders and officers and their judges , stood on opposite sides of the ark before the Levitical priests who carried the ark of the covenant of the Lord , half of them in front of Mount Gerizim and half of them in front of Mount Ebal , just as Moses the servant of the Lord had commanded at the first, to bless the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:7** (✓) *target: people*
  > Jos 10:7 So Joshua went up from Gilgal , he and all the people of war with him, and all the mighty men of valor .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:21** (✓) *target: people*
  > Jos 10:21 then all the people returned safe to Joshua in the camp at Makkedah . Not a man moved his tongue against any of the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 10:33** (✓) *target: people*
  > Jos 10:33 Then Horam king of Gezer came up to help Lachish . And Joshua struck him and his people , until he left none remaining .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 14:8** (✓) *target: people*
  > Jos 14:8 But my brothers who went up with me made the heart of the people melt ; yet I wholly followed the Lord my God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:14** (✓) *target: people*
  > Jos 17:14 Then the people of Joseph spoke to Joshua , saying , “ Why have you given me but one lot and one portion as an inheritance , although I am a numerous people , since all along the Lord has blessed me?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:15** (✓) *target: people*
  > Jos 17:15 And Joshua said to them, “ If you are a numerous people , go up by yourselves to the forest , and there clear ground for yourselves in the land of the Perizzites and the Rephaim , since the hill country of Ephraim is too narrow for you.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 17:17** (✓) *target: people*
  > Jos 17:17 Then Joshua said to the house of Joseph , to Ephraim and Manasseh , “You are a numerous people and have great power . You shall not have one allotment only,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:2** (✓) *target: people*
  > Jos 24:2 And Joshua said to all the people , “Thus says the Lord , the God of Israel , ‘ Long ago , your fathers lived beyond the Euphrates , Terah , the father of Abraham and of Nahor ; and they served other gods .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:16** (✓) *target: people*
  > Jos 24:16 Then the people answered , “Far be it from us that we should forsake the Lord to serve other gods ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:17** (✓) *target: peoples*
  > Jos 24:17 for it is the Lord our God who brought us and our fathers up from the land of Egypt , out of the house of slavery , and who did those great signs in our sight and preserved us in all the way that we went , and among all the peoples through whom we passed .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:18** (✓) *target: peoples*
  > Jos 24:18 And the Lord drove out before us all the peoples , the Amorites who lived in the land . Therefore we also will serve the Lord , for he is our God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:19** (✓) *target: people*
  > Jos 24:19 But Joshua said to the people , “You are not able to serve the Lord , for he is a holy God . He is a jealous God ; he will not forgive your transgressions or your sins .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:21** (✓) *target: people*
  > Jos 24:21 And the people said to Joshua , “No, but we will serve the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:22** (✓) *target: people*
  > Jos 24:22 Then Joshua said to the people , “You are witnesses against yourselves that you have chosen the Lord , to serve him.” And they said , “We are witnesses .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:24** (✓) *target: people*
  > Jos 24:24 And the people said to Joshua , “The Lord our God we will serve , and his voice we will obey .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:25** (✓) *target: people*
  > Jos 24:25 So Joshua made a covenant with the people that day , and put in place statutes and rules for them at Shechem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:27** (✓) *target: people*
  > Jos 24:27 And Joshua said to all the people , “Behold, this stone shall be a witness against us, for it has heard all the words of the Lord that he spoke to us. Therefore it shall be a witness against you, lest you deal falsely with your God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jos 24:28** (✓) *target: people*
  > Jos 24:28 So Joshua sent the people away, every man to his inheritance .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 1:16** (✓) *target: people*
  > Judg 1:16 And the descendants of the Kenite , Moses ’ father-in-law , went up with the people of Judah from the city of palms into the wilderness of Judah , which lies in the Negeb near Arad , and they went and settled with the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:4** (✓) *target: people*
  > Judg 2:4 As soon as the angel of the Lord spoke these words to all the people of Israel , the people lifted up their voices and wept .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:6** (✓) *target: people*
  > Judg 2:6 When Joshua dismissed the people , the people of Israel went each to his inheritance to take possession of the land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:7** (✓) *target: people*
  > Judg 2:7 And the people served the Lord all the days of Joshua , and all the days of the elders who outlived Joshua , who had seen all the great work that the Lord had done for Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 2:12** (✓) *target: peoples*
  > Judg 2:12 And they abandoned the Lord , the God of their fathers , who had brought them out of the land of Egypt . They went after other gods , from among the gods of the peoples who were around them, and bowed down to them. And they provoked the Lord to anger.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 3:18** (✓) *target: people*
  > Judg 3:18 And when Ehud had finished presenting the tribute , he sent away the people who carried the tribute .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Judg 5:2** (✓) *target: people*
  > Judg 5:2 “That the leaders took the lead in Israel , that the people offered themselves willingly , bless the Lord !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 1:3** (✓) *target: people*
  > Ezr 1:3 Whoever is among you of all his people , may his God be with him, and let him go up to Jerusalem , which is in Judah , and rebuild the house of the Lord , the God of Israel — he is the God who is in Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 2:2** (✓) *target: people*
  > Ezr 2:2 They came with Zerubbabel , Jeshua , Nehemiah , Seraiah , Reelaiah , Mordecai , Bilshan , Mispar , Bigvai , Rehum , and Baanah . The number of the men of the people of Israel :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 2:70** (✓) *target: people*
  > Ezr 2:70 Now the priests , the Levites , some of the people , the singers , the gatekeepers , and the temple servants lived in their towns , and all the rest of Israel in their towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:1** (✓) *target: people*
  > Ezr 3:1 When the seventh month came , and the children of Israel were in the towns , the people gathered as one man to Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:3** (✓) *target: peoples*
  > Ezr 3:3 They set the altar in its place , for fear was on them because of the peoples of the lands , and they offered burnt offerings on it to the Lord , burnt offerings morning and evening .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:11** (✓) *target: people*
  > Ezr 3:11 And they sang responsively , praising and giving thanks to the Lord , “ For he is good , for his steadfast love endures forever toward Israel .” And all the people shouted with a great shout when they praised the Lord , because the foundation of the house of the Lord was laid.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 3:13** (✓) *target: people*
  > Ezr 3:13 so that the people could not distinguish the sound of the joyful shout from the sound of the people’s weeping , for the people shouted with a great shout , and the sound was heard far away .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 4:4** (✓) *target: people*
  > Ezr 4:4 Then the people of the land discouraged the people of Judah and made them afraid to build
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 8:15** (✓) *target: people*
  > Ezr 8:15 I gathered them to the river that runs to Ahava , and there we camped three days . As I reviewed the people and the priests , I found there none of the sons of Levi .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 8:36** (✓) *target: people*
  > Ezr 8:36 They also delivered the king’s commissions to the king’s satraps and to the governors of the province Beyond the River , and they aided the people and the house of God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:1** (✓) *target: people*
  > Ezr 9:1 After these things had been done , the officials approached me and said , “The people of Israel and the priests and the Levites have not separated themselves from the peoples of the lands with their abominations , from the Canaanites , the Hittites , the Perizzites , the Jebusites , the Ammonites , the Moabites , the Egyptians , and the Amorites .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:2** (✓) *target: peoples*
  > Ezr 9:2 For they have taken some of their daughters to be wives for themselves and for their sons , so that the holy race has mixed itself with the peoples of the lands . And in this faithlessness the hand of the officials and chief men has been foremost .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:11** (✓) *target: peoples*
  > Ezr 9:11 which you commanded by your servants the prophets , saying , ‘The land that you are entering , to take possession of it, is a land impure with the impurity of the peoples of the lands , with their abominations that have filled it from end to end with their uncleanness .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 9:14** (✓) *target: peoples*
  > Ezr 9:14 shall we break your commandments again and intermarry with the peoples who practice these abominations ? Would you not be angry with us until you consumed us, so that there should be no remnant , nor any to escape ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:1** (✓) *target: people*
  > Ezr 10:1 While Ezra prayed and made confession , weeping and casting himself down before the house of God , a very great assembly of men , women , and children , gathered to him out of Israel , for the people wept bitterly .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:2** (✓) *target: peoples*
  > Ezr 10:2 And Shecaniah the son of Jehiel , of the sons of Elam , addressed Ezra : “ We have broken faith with our God and have married foreign women from the peoples of the land , but even now there is hope for Israel in spite of this .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:9** (✓) *target: people*
  > Ezr 10:9 Then all the men of Judah and Benjamin assembled at Jerusalem within the three days . It was the ninth month , on the twentieth day of the month . And all the people sat in the open square before the house of God , trembling because of this matter and because of the heavy rain .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:11** (✓) *target: peoples*
  > Ezr 10:11 Now then make confession to the Lord , the God of your fathers and do his will . Separate yourselves from the peoples of the land and from the foreign wives .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ezr 10:13** (✓) *target: people*
  > Ezr 10:13 But the people are many , and it is a time of heavy rain ; we cannot stand in the open . Nor is this a task for one day or for two , for we have greatly transgressed in this matter .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 1:8** (✓) *target: among the peoples*
  > Neh 1:8 Remember the word that you commanded your servant Moses , saying , ‘If you are unfaithful , I will scatter you among the peoples ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 1:10** (✓) *target: people*
  > Neh 1:10 They are your servants and your people , whom you have redeemed by your great power and by your strong hand .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:6** (✓) *target: people*
  > Neh 4:6 So we built the wall . And all the wall was joined together to half its height, for the people had a mind to work .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:13** (✓) *target: people*
  > Neh 4:13 So in the lowest parts of the space behind the wall , in open places , I stationed the people by their clans , with their swords , their spears , and their bows .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:14** (✓) *target: people*
  > Neh 4:14 And I looked and arose and said to the nobles and to the officials and to the rest of the people , “Do not be afraid of them . Remember the Lord , who is great and awesome , and fight for your brothers , your sons , your daughters , your wives , and your homes .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:19** (✓) *target: people*
  > Neh 4:19 And I said to the nobles and to the officials and to the rest of the people , “The work is great and widely spread , and we are separated on the wall , far from one another .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 4:22** (✓) *target: people*
  > Neh 4:22 I also said to the people at that time , “Let every man and his servant pass the night within Jerusalem , that they may be a guard for us by night and may labor by day .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:1** (✓) *target: people*
  > Neh 5:1 Now there arose a great outcry of the people and of their wives against their Jewish brothers .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:13** (✓) *target: people*
  > Neh 5:13 I also shook out the fold of my garment and said , “ So may God shake out every man from his house and from his labor who does not keep this promise . So may he be shaken out and emptied .” And all the assembly said “ Amen ” and praised the Lord . And the people did as they had promised .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:15** (✓) *target: people*
  > Neh 5:15 The former governors who were before me laid heavy burdens on the people and took from them for their daily ration forty shekels of silver . Even their servants lorded it over the people . But I did not do so , because of the fear of God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:18** (✓) *target: people*
  > Neh 5:18 Now what was prepared at my expense for each day was one ox and six choice sheep and birds , and every ten days all kinds of wine in abundance . Yet for all this I did not demand the food allowance of the governor , because the service was too heavy on this people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 5:19** (✓) *target: people*
  > Neh 5:19 Remember for my good , O my God , all that I have done for this people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:4** (✓) *target: people*
  > Neh 7:4 The city was wide and large , but the people within it were few , and no houses had been rebuilt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:5** (✓) *target: people*
  > Neh 7:5 Then my God put it into my heart to assemble the nobles and the officials and the people to be enrolled by genealogy . And I found the book of the genealogy of those who came up at the first , and I found written in it :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:7** (✓) *target: people*
  > Neh 7:7 They came with Zerubbabel , Jeshua , Nehemiah , Azariah , Raamiah , Nahamani , Mordecai , Bilshan , Mispereth , Bigvai , Nehum , Baanah . The number of the men of the people of Israel :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:72** (✓) *target: people*
  > Neh 7:72 And what the rest of the people gave was 20,000 darics of gold , 2,000 minas of silver , and 67 priests ’ garments .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 7:73** (✓) *target: people*
  > Neh 7:73 So the priests , the Levites , the gatekeepers , the singers , some of the people , the temple servants , and all Israel , lived in their towns . And when the seventh month had come , the people of Israel were in their towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:1** (✓) *target: people*
  > Neh 8:1 And all the people gathered as one man into the square before the Water Gate . And they told Ezra the scribe to bring the Book of the Law of Moses that the Lord had commanded Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:3** (✓) *target: people*
  > Neh 8:3 And he read from it facing the square before the Water Gate from early morning until midday , in the presence of the men and the women and those who could understand . And the ears of all the people were attentive to the Book of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:5** (✓) *target: people*
  > Neh 8:5 And Ezra opened the book in the sight of all the people , for he was above all the people , and as he opened it all the people stood .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:6** (✓) *target: people*
  > Neh 8:6 And Ezra blessed the Lord , the great God , and all the people answered , “ Amen , Amen ,” lifting up their hands . And they bowed their heads and worshiped the Lord with their faces to the ground .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:7** (✓) *target: people*
  > Neh 8:7 Also Jeshua , Bani , Sherebiah , Jamin , Akkub , Shabbethai , Hodiah , Maaseiah , Kelita , Azariah , Jozabad , Hanan , Pelaiah , the Levites , helped the people to understand the Law , while the people remained in their places .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:9** (✓) *target: people*
  > Neh 8:9 And Nehemiah , who was the governor , and Ezra the priest and scribe , and the Levites who taught the people said to all the people , “This day is holy to the Lord your God ; do not mourn or weep .” For all the people wept as they heard the words of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:11** (✓) *target: people*
  > Neh 8:11 So the Levites calmed all the people , saying , “Be quiet , for this day is holy ; do not be grieved .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:12** (✓) *target: people*
  > Neh 8:12 And all the people went their way to eat and drink and to send portions and to make great rejoicing , because they had understood the words that were declared to them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:13** (✓) *target: people*
  > Neh 8:13 On the second day the heads of fathers’ houses of all the people , with the priests and the Levites , came together to Ezra the scribe in order to study the words of the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 8:16** (✓) *target: people*
  > Neh 8:16 So the people went out and brought them and made booths for themselves, each on his roof , and in their courts and in the courts of the house of God , and in the square at the Water Gate and in the square at the Gate of Ephraim .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:10** (✓) *target: people*
  > Neh 9:10 and performed signs and wonders against Pharaoh and all his servants and all the people of his land , for you knew that they acted arrogantly against our fathers. And you made a name for yourself, as it is to this day .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:22** (✓) *target: peoples*
  > Neh 9:22 “And you gave them kingdoms and peoples and allotted to them every corner . So they took possession of the land of Sihon king of Heshbon and the land of Og king of Bashan .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:24** (✓) *target: peoples*
  > Neh 9:24 So the descendants went in and possessed the land , and you subdued before them the inhabitants of the land , the Canaanites , and gave them into their hand , with their kings and the peoples of the land , that they might do with them as they would .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:30** (✓) *target: peoples*
  > Neh 9:30 Many years you bore with them and warned them by your Spirit through your prophets . Yet they would not give ear . Therefore you gave them into the hand of the peoples of the lands .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 9:32** (✓) *target: people*
  > Neh 9:32 “ Now , therefore, our God , the great , the mighty , and the awesome God , who keeps covenant and steadfast love , let not all the hardship seem little to you that has come upon us, upon our kings , our princes , our priests , our prophets , our fathers , and all your people , since the time of the kings of Assyria until this day .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:14** (✓) *target: people*
  > Neh 10:14 The chiefs of the people : Parosh , Pahath-moab , Elam , Zattu , Bani ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:28** (✓) *target: people*
  > Neh 10:28 “The rest of the people , the priests , the Levites , the gatekeepers , the singers , the temple servants , and all who have separated themselves from the peoples of the lands to the Law of God , their wives , their sons , their daughters , all who have knowledge and understanding ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:30** (✓) *target: peoples*
  > Neh 10:30 We will not give our daughters to the peoples of the land or take their daughters for our sons .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:31** (✓) *target: peoples*
  > Neh 10:31 And if the peoples of the land bring in goods or any grain on the Sabbath day to sell , we will not buy from them on the Sabbath or on a holy day . And we will forgo the crops of the seventh year and the exaction of every debt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 10:34** (✓) *target: people*
  > Neh 10:34 We, the priests , the Levites , and the people , have likewise cast lots for the wood offering , to bring it into the house of our God , according to our fathers ’ houses , at times appointed , year by year , to burn on the altar of the Lord our God , as it is written in the Law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:1** (✓) *target: people*
  > Neh 11:1 Now the leaders of the people lived in Jerusalem . And the rest of the people cast lots to bring one out of ten to live in Jerusalem the holy city , while nine out of ten remained in the other towns .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:2** (✓) *target: people*
  > Neh 11:2 And the people blessed all the men who willingly offered to live in Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 11:24** (✓) *target: people*
  > Neh 11:24 And Pethahiah the son of Meshezabel , of the sons of Zerah the son of Judah , was at the king’s side in all matters concerning the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Neh 12:30** (✓) *target: people*
  > Neh 12:30 And the priests and the Levites purified themselves, and they purified the people and the gates and the wall .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 12:2** (✓) *target: people*
  > Job 12:2 “No doubt you are the people , and wisdom will die with you.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 12:24** (✓) *target: people*
  > Job 12:24 He takes away understanding from the chiefs of the people of the earth and makes them wander in a trackless waste .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 17:6** (✓) *target: peoples*
  > Job 17:6 “He has made me a byword of the peoples , and I am one before whom men spit .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 18:19** (✓) *target: people*
  > Job 18:19 He has no posterity or progeny among his people , and no survivor where he used to live .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 34:20** (✓) *target: people*
  > Job 34:20 In a moment they die ; at midnight the people are shaken and pass away , and the mighty are taken away by no human hand .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 34:30** (✓) *target: people*
  > Job 34:30 that a godless man should not reign , that he should not ensnare the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 36:20** (✓) *target: peoples*
  > Job 36:20 Do not long for the night , when peoples vanish in their place .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Job 36:31** (✓) *target: peoples*
  > Job 36:31 For by these he judges peoples ; he gives food in abundance .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 3:6** (✓) *target: people*
  > Psa 3:6 I will not be afraid of many thousands of people who have set themselves against me all around .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 3:8** (✓) *target: people*
  > Psa 3:8 Salvation belongs to the Lord ; your blessing be on your people ! Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 7:8** (✓) *target: peoples*
  > Psa 7:8 The Lord judges the peoples ; judge me, O Lord , according to my righteousness and according to the integrity that is in me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 9:11** (✓) *target: peoples*
  > Psa 9:11 Sing praises to the Lord , who sits enthroned in Zion ! Tell among the peoples his deeds !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 14:4** (✓) *target: people*
  > Psa 14:4 Have they no knowledge , all the evildoers who eat up my people as they eat bread and do not call upon the Lord ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 14:7** (✓) *target: people*
  > Psa 14:7 Oh, that salvation for Israel would come out of Zion ! When the Lord restores the fortunes of his people , let Jacob rejoice , let Israel be glad .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:27** (✓) *target: people*
  > Psa 18:27 For you save a humble people , but the haughty eyes you bring down .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:43** (✓) *target: people*
  > Psa 18:43 You delivered me from strife with the people ; you made me the head of the nations ; people whom I had not known served me .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 18:47** (✓) *target: peoples*
  > Psa 18:47 the God who gave me vengeance and subdued peoples under me ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 22:6** (✓) *target: people*
  > Psa 22:6 But I am a worm and not a man , scorned by mankind and despised by the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 22:31** (✓) *target: people*
  > Psa 22:31 they shall come and proclaim his righteousness to a people yet unborn, that he has done it.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 28:9** (✓) *target: people*
  > Psa 28:9 Oh, save your people and bless your heritage ! Be their shepherd and carry them forever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 29:11** (✓) *target: people*
  > Psa 29:11 May the Lord give strength to his people ! May the Lord bless his people with peace !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 33:10** (✓) *target: peoples*
  > Psa 33:10 The Lord brings the counsel of the nations to nothing ; he frustrates the plans of the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 33:12** (✓) *target: people*
  > Psa 33:12 Blessed is the nation whose God is the Lord , the people whom he has chosen as his heritage !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 35:18** (✓) *target: throng*
  > Psa 35:18 I will thank you in the great congregation ; in the mighty throng I will praise you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 44:12** (✓) *target: people*
  > Psa 44:12 You have sold your people for a trifle , demanding no high price for them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:5** (✓) *target: peoples*
  > Psa 45:5 Your arrows are sharp in the heart of the king’s enemies ; the peoples fall under you.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:10** (✓) *target: people*
  > Psa 45:10 Hear , O daughter , and consider , and incline your ear : forget your people and your father’s house ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:12** (✓) *target: people*
  > Psa 45:12 The people of Tyre will seek your favor with gifts , the richest of the people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 45:17** (✓) *target: nations*
  > Psa 45:17 I will cause your name to be remembered in all generations ; therefore nations will praise you forever and ever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:1** (✓) *target: peoples*
  > To the choirmaster . A Psalm of the Sons of Korah . Psa 47:1 Clap your hands , all peoples ! Shout to God with loud songs of joy !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:3** (✓) *target: peoples*
  > Psa 47:3 He subdued peoples under us, and nations under our feet .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 47:9** (✓) *target: peoples*
  > Psa 47:9 The princes of the peoples gather as the people of the God of Abraham . For the shields of the earth belong to God ; he is highly exalted !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 49:1** (✓) *target: peoples*
  > To the choirmaster . A Psalm of the Sons of Korah . Psa 49:1 Hear this , all peoples ! Give ear , all inhabitants of the world ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 50:4** (✓) *target: people*
  > Psa 50:4 He calls to the heavens above and to the earth , that he may judge his people :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 50:7** (✓) *target: people*
  > Psa 50:7 “ Hear , O my people , and I will speak ; O Israel , I will testify against you. I am God , your God .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 53:4** (✓) *target: people*
  > Psa 53:4 Have those who work evil no knowledge , who eat up my people as they eat bread , and do not call upon God ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 53:6** (✓) *target: people*
  > Psa 53:6 Oh , that salvation for Israel would come out of Zion ! When God restores the fortunes of his people , let Jacob rejoice , let Israel be glad .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 56:7** (✓) *target: peoples*
  > Psa 56:7 For their crime ^ will they escape ? In wrath cast down the peoples , O God !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 57:9** (✓) *target: peoples*
  > Psa 57:9 I will give thanks to you, O Lord , among the peoples ; I will sing praises to you among the nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 59:11** (✓) *target: people*
  > Psa 59:11 Kill them not , lest my people forget ; make them totter by your power and bring them down , O Lord , our shield !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 60:3** (✓) *target: people*
  > Psa 60:3 You have made your people see hard things ; you have given us wine to drink that made us stagger .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 62:8** (✓) *target: people*
  > Psa 62:8 Trust in him at all times , O people ; pour out your heart before him; God is a refuge for us. Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 66:8** (✓) *target: peoples*
  > Psa 66:8 Bless our God , O peoples ; let the sound of his praise be heard ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:3** (✓) *target: peoples*
  > Psa 67:3 Let the peoples praise you, O God ; let all the peoples praise you!
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:4** (✓) *target: peoples*
  > Psa 67:4 Let the nations be glad and sing for joy , for you judge the peoples with equity and guide the nations upon earth . Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 67:5** (✓) *target: peoples*
  > Psa 67:5 Let the peoples praise you, O God ; let all the peoples praise you!
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:7** (✓) *target: people*
  > Psa 68:7 O God , when you went out before your people , when you marched through the wilderness , Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:30** (✓) *target: peoples*
  > Psa 68:30 Rebuke the beasts that dwell among the reeds , the herd of bulls with the calves of the peoples . Trample underfoot those who lust after tribute ; scatter the peoples who delight in war .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 68:35** (✓) *target: people*
  > Psa 68:35 Awesome is God from his sanctuary ; the God of Israel — he is the one who gives power and strength to his people . Blessed be God !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:2** (✓) *target: people*
  > Psa 72:2 May he judge your people with righteousness , and your poor with justice !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:3** (✓) *target: people*
  > Psa 72:3 Let the mountains bear prosperity for the people , and the hills , in righteousness !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 72:4** (✓) *target: people*
  > Psa 72:4 May he defend the cause of the poor of the people , give deliverance to the children of the needy , and crush the oppressor !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 73:10** (✓) *target: people*
  > Psa 73:10 Therefore his people turn back to them , and find no fault in them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 74:18** (✓) *target: people*
  > Psa 74:18 Remember this , O Lord , how the enemy scoffs , and a foolish people reviles your name .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:14** (✓) *target: peoples*
  > Psa 77:14 You are the God who works wonders ; you have made known your might among the peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:15** (✓) *target: people*
  > Psa 77:15 You with your arm redeemed your people , the children of Jacob and Joseph . Selah
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 77:20** (✓) *target: people*
  > Psa 77:20 You led your people like a flock by the hand of Moses and Aaron .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:1** (✓) *target: people*
  > A Maskil of Asaph . Psa 78:1 Give ear , O my people , to my teaching ; incline your ears to the words of my mouth !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:20** (✓) *target: people*
  > Psa 78:20 He struck the rock so that water gushed out and streams overflowed . Can he also give bread or provide meat for his people ?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Psa 78:52** (✓) *target: people*
  > Psa 78:52 Then he led out his people like sheep and guided them in the wilderness like a flock .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 11:14** (✓) *target: people*
  > Pro 11:14 Where there is no guidance , a people falls , but in an abundance of counselors there is safety .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 14:28** (✓) *target: people*
  > Pro 14:28 In a multitude of people is the glory of a king , but without people a prince is ruined .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 24:24** (✓) *target: peoples*
  > Pro 24:24 Whoever says to the wicked , “You are in the right ,” will be cursed by peoples , abhorred by nations ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 28:15** (✓) *target: people*
  > Pro 28:15 Like a roaring lion or a charging bear is a wicked ruler over a poor people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 29:2** (✓) *target: people*
  > Pro 29:2 When the righteous increase , the people rejoice , but when the wicked rule , the people groan .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 29:18** (✓) *target: people*
  > Pro 29:18 Where there is no prophetic vision the people cast off restraint , but blessed is he who keeps the law .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 30:25** (✓) *target: people*
  > Pro 30:25 the ants are a people not strong , yet they provide their food in the summer ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Pro 30:26** (✓) *target: people*
  > Pro 30:26 the rock badgers are a people not mighty , yet they make their homes in the cliffs ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ecc 4:16** (✓) *target: people*
  > Ecc 4:16 There was no end of all the people , all of whom he led . Yet those who come later will not rejoice in him. Surely this also is vanity and a striving after wind .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Ecc 12:9** (✓) *target: people*
  > Ecc 12:9 Besides being wise , the Preacher also taught the people knowledge , weighing and studying and arranging many proverbs with great care.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:3** (✓) *target: people*
  > Isa 1:3 The ox knows its owner , and the donkey its master’s crib , but Israel does not know , my people do not understand .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:4** (✓) *target: people*
  > Isa 1:4 Ah , sinful nation , a people laden with iniquity , offspring of evildoers , children who deal corruptly ! They have forsaken the Lord , they have despised the Holy One of Israel , they are utterly estranged.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 1:10** (✓) *target: people*
  > Isa 1:10 Hear the word of the Lord , you rulers of , Sodom ! Give ear to the teaching of our God , you people of Gomorrah !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:3** (✓) *target: peoples*
  > Isa 2:3 and many peoples shall come , and say : “ Come , let us go up to the mountain of the Lord , to the house of the God of Jacob , that he may teach us his ways and that we may walk in his paths .” For out of Zion shall go forth the law , and the word of the Lord from Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:4** (✓) *target: peoples*
  > Isa 2:4 He shall judge between the nations , and shall decide disputes for many peoples ; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 2:6** (✓) *target: people*
  > Isa 2:6 For you have rejected your people , the house of Jacob , because they are full of things from the east and of fortune-tellers like the Philistines , and they strike hands with the children of foreigners .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:5** (✓) *target: people*
  > Isa 3:5 And the people will oppress one another, every one his fellow and every one his neighbor ; the youth will be insolent to the elder , and the despised to the honorable .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:7** (✓) *target: people*
  > Isa 3:7 in that day he will speak out , saying : “I will not be a healer ; in my house there is neither bread nor cloak ; you shall not make me leader of the people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:12** (✓) *target: people*
  > Isa 3:12 My people — infants are their oppressors , and women rule over them. O my people , your guides mislead you and they have swallowed up the course of your paths .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:13** (✓) *target: peoples*
  > Isa 3:13 The Lord has taken his place to contend ; he stands to judge peoples .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:14** (✓) *target: people*
  > Isa 3:14 The Lord will enter into judgment with the elders and princes of his people : “ It is you who have devoured the vineyard , the spoil of the poor is in your houses .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 3:15** (✓) *target: people*
  > Isa 3:15 What do you mean by crushing my people , by grinding the face of the poor ?” declares the Lord God of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 5:13** (✓) *target: people*
  > Isa 5:13 Therefore my people go into exile for lack of knowledge ; their honored men go hungry , and their multitude is parched with thirst .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 5:25** (✓) *target: people*
  > Isa 5:25 Therefore the anger of the Lord was kindled against his people , and he stretched out his hand against them and struck them, and the mountains quaked ; and their corpses were as refuse in the midst of the streets . For all this his anger has not turned away , and his hand is stretched out still .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:5** (✓) *target: people*
  > Isa 6:5 And I said : “ Woe is me! For I am lost ; for I am a man of unclean lips , and I dwell in the midst of a people of unclean lips ; for my eyes have seen the King , the Lord of hosts !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:9** (✓) *target: people*
  > Isa 6:9 And he said , “ Go , and say to this people : “‘Keep on hearing , but do not understand ; keep on seeing , but do not perceive .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 6:10** (✓) *target: people*
  > Isa 6:10 Make the heart of this people dull , and their ears heavy , and blind their eyes ; lest they see with their eyes , and hear with their ears , and understand with their hearts , and turn and be healed .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:2** (✓) *target: people*
  > Isa 7:2 When the house of David was told , “ Syria is in league with Ephraim ,” the heart of Ahaz and the heart of his people shook as the trees of the forest shake before the wind .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:8** (✓) *target: people*
  > Isa 7:8 For the head of Syria is Damascus , and the head of Damascus is Rezin . And within sixty-five years Ephraim will be shattered from being a people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 7:17** (✓) *target: people*
  > Isa 7:17 The Lord will bring upon you and upon your people and upon your father’s house such days as have not come since the day that Ephraim departed from Judah —the king of Assyria !”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:6** (✓) *target: people*
  > Isa 8:6 “ Because this people has refused the waters of Shiloah that flow gently , and rejoice over Rezin and the son of Remaliah ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:9** (✓) *target: peoples*
  > Isa 8:9 Be broken , you peoples , and be shattered ; give ear , all you far countries ; strap on your armor and be shattered ; strap on your armor and be shattered .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:11** (✓) *target: people*
  > Isa 8:11 For the Lord spoke thus to me with his strong hand upon me, and warned me not to walk in the way of this people , saying :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:12** (✓) *target: people*
  > Isa 8:12 “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 8:19** (✓) *target: people*
  > Isa 8:19 And when they say to you, “ Inquire of the mediums and the necromancers who chirp and mutter ,” should not a people inquire of their God ? Should they inquire of the dead on behalf of the living ?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:2** (✓) *target: people*
  > Isa 9:2 The people who walked in darkness have seen a great light ; those who dwelt in a land of deep darkness , on them has light shone .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:9** (✓) *target: people*
  > Isa 9:9 and all the people will know , Ephraim and the inhabitants of Samaria , who say in pride and in arrogance of heart :
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:13** (✓) *target: people*
  > Isa 9:13 The people did not turn to him who struck them, nor inquire of the Lord of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:16** (✓) *target: people*
  > Isa 9:16 for those who guide this people have been leading them astray , and those who are guided by them are swallowed up .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 9:19** (✓) *target: people*
  > Isa 9:19 Through the wrath of the Lord of hosts the land is scorched , and the people are like fuel for the fire ; no one spares another .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:2** (✓) *target: people*
  > Isa 10:2 to turn aside the needy from justice and to rob the poor of my people of their right , that widows may be their spoil , and that they may make the fatherless their prey !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:6** (✓) *target: people*
  > Isa 10:6 Against a godless nation I send him, and against the people of my wrath I command him, to take spoil and seize plunder , and to tread them down like the mire of the streets .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:13** (✓) *target: peoples*
  > Isa 10:13 For he says : “ By the strength of my hand I have done it, and by my wisdom , for I have understanding ; I remove the boundaries of peoples , and plunder their treasures; like a bull I bring down those who sit on thrones.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:14** (✓) *target: peoples*
  > Isa 10:14 My hand has found like a nest the wealth of the peoples ; and as one gathers eggs that have been forsaken , so I have gathered all the earth ; and there was none that moved a wing or opened the mouth or chirped .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:22** (✓) *target: people*
  > Isa 10:22 For though your people Israel be as the sand of the sea , only a remnant of them will return . Destruction is decreed , overflowing with righteousness .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 10:24** (✓) *target: people*
  > Isa 10:24 Therefore thus says the Lord God of hosts : “O my people , who dwell in Zion , be not afraid of the Assyrians when they strike with the rod and lift up their staff against you as the Egyptians did.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:10** (✓) *target: peoples*
  > Isa 11:10 In that day the root of Jesse , who shall stand as a signal for the peoples —of him shall the nations inquire , and his resting place shall be glorious .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:11** (✓) *target: people*
  > Isa 11:11 In that day the Lord will extend his hand yet a second time to recover the remnant that remains of his people , from Assyria , from Egypt , from Pathros , from Cush , from Elam , from Shinar , from Hamath , and from the coastlands of the sea .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 11:16** (✓) *target: people*
  > Isa 11:16 And there will be a highway from Assyria for the remnant that remains of his people , as there was for Israel when they came up from the land of Egypt .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 12:4** (✓) *target: peoples*
  > Isa 12:4 And you will say in that day : “Give thanks to the Lord , call upon his name , make known his deeds among the peoples , proclaim that his name is exalted .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 13:4** (✓) *target: multitude*
  > Isa 13:4 The sound of a tumult is on the mountains as of a great multitude ! The sound of an uproar of kingdoms , of nations gathering together ! The Lord of hosts is mustering a host for battle .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 13:14** (✓) *target: people*
  > Isa 13:14 And like a hunted gazelle , or like sheep with none to gather them, each will turn to his own people , and each will flee to his own land .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:2** (✓) *target: peoples*
  > Isa 14:2 And the peoples will take them and bring them to their place , and the house of Israel will possess them in the Lord’s land as male and female slaves . They will take captive those who were their captors , and rule over those who oppressed them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:6** (✓) *target: peoples*
  > Isa 14:6 that struck the peoples in wrath with unceasing blows , that ruled the nations in anger with unrelenting persecution .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:20** (✓) *target: people*
  > Isa 14:20 You will not be joined with them in burial , because you have destroyed your land , you have slain your people . “May the offspring of evildoers nevermore be named !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 14:32** (✓) *target: people*
  > Isa 14:32 What will one answer the messengers of the nation ? “The Lord has founded Zion , and in her the afflicted of his people find refuge .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 17:12** (✓) *target: peoples*
  > Isa 17:12 Ah , the thunder of many peoples ; they thunder like the thundering of the sea ! Ah, the roar of nations ; they roar like the roaring of mighty waters !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 18:2** (✓) *target: people*
  > Isa 18:2 which sends ambassadors by the sea , in vessels of papyrus on the waters ! Go , you swift messengers , to a nation tall and smooth , to a people feared near and far , a nation mighty and conquering , whose land the rivers divide .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 18:7** (✓) *target: people*
  > Isa 18:7 At that time tribute will be brought to the Lord of hosts from a people tall and smooth , from a people feared near and far , a nation mighty and conquering , whose land the rivers divide , to Mount Zion , the place of the name of the Lord of hosts .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 19:25** (✓) *target: people*
  > Isa 19:25 whom the Lord of hosts has blessed , saying , “ Blessed be Egypt my people , and Assyria the work of my hands , and Israel my inheritance .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 22:4** (✓) *target: people*
  > Isa 22:4 Therefore I said : “Look away from me; let me weep bitter tears ; do not labor to comfort me concerning the destruction of the daughter of my people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 23:13** (✓) *target: people*
  > Isa 23:13 Behold the land of the Chaldeans ! This is the people that was not ; Assyria destined it for wild beasts . They erected their siege towers , they stripped her palaces bare, they made her a ruin .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:2** (✓) *target: people*
  > Isa 24:2 And it shall be , as with the people , so with the priest ; as with the slave , so with his master ; as with the maid , so with her mistress ; as with the buyer , so with the seller ; as with the lender , so with the borrower ; as with the creditor , so with the debtor .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:4** (✓) *target: people*
  > Isa 24:4 The earth mourns and withers ; the world languishes and withers ; the highest people of the earth languish .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 24:13** (✓) *target: nations*
  > Isa 24:13 For thus it shall be in the midst of the earth among the nations , as when an olive tree is beaten , as at the gleaning when the grape harvest is done .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:3** (✓) *target: peoples*
  > Isa 25:3 Therefore strong peoples will glorify you; cities of ruthless nations will fear you .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:6** (✓) *target: peoples*
  > Isa 25:6 On this mountain the Lord of hosts will make for all peoples a feast of rich food , a feast of well-aged wine , of rich food full of marrow , of aged wine well refined .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:7** (✓) *target: peoples*
  > Isa 25:7 And he will swallow up on this mountain the covering that is cast over all peoples , the veil that is spread over all nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 25:8** (✓) *target: people*
  > Isa 25:8 He will swallow up death forever ; and the Lord God will wipe away tears from all faces , and the reproach of his people he will take away from all the earth , for the Lord has spoken .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Isa 26:11** (✓) *target: people*
  > Isa 26:11 O Lord , your hand is lifted up , but they do not see it. Let them see your zeal for your people , and be ashamed . Let the fire for your adversaries consume them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 1:9** (✓) *target: people*
  > Hos 1:9 And the Lord said , “ Call his name Not My People , for you are not my people , and I am not your God.”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 1:10** (✓) *target: people*
  > Hos 1:10 Yet the number of the children of Israel shall be like the sand of the sea , which cannot be measured or numbered . And in the place where it was said to them, “You are not my people ,” it shall be said to them, “ Children of the living God .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 2:1** (✓) *target: people*
  > Hos 2:1 Say to your brothers , “ You are my people ,” and to your sisters , “ You have received mercy .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 2:23** (✓) *target: People*
  > Hos 2:23 and I will sow her for myself in the land . And I will have mercy on No Mercy , and I will say to Not My People , ‘You are my people ’; and he shall say , ‘You are my God .’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:4** (✓) *target: with you*
  > Hos 4:4 Yet let no one contend , and let none accuse , for with you is my contention , O priest .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:6** (✓) *target: people*
  > Hos 4:6 My people are destroyed for lack of knowledge ; because you have rejected knowledge , I reject you from being a priest to me. And since you have forgotten the law of your God , I also will forget your children .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:8** (✓) *target: people*
  > Hos 4:8 They feed on the sin of my people ; they are greedy for their iniquity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:9** (✓) *target: people*
  > Hos 4:9 And it shall be like people , like priest ; I will punish them for their ways and repay them for their deeds .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:12** (✓) *target: people*
  > Hos 4:12 My people inquire of a piece of wood , and their walking staff gives them oracles . For a spirit of whoredom has led them astray , and they have left their God to play the whore .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 4:14** (✓) *target: people*
  > Hos 4:14 I will not punish your daughters when they play the whore , nor your brides when they commit adultery ; for the men themselves go aside with prostitutes and sacrifice with cult prostitutes , and a people without understanding shall come to ruin .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 6:11** (✓) *target: people*
  > Hos 6:11 For you also , O Judah , a harvest is appointed . When I restore the fortunes of my people ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 7:8** (✓) *target: peoples*
  > Hos 7:8 Ephraim mixes himself with the peoples ; Ephraim is a cake not turned .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 9:1** (✓) *target: peoples*
  > Hos 9:1 Rejoice not, O Israel ! Exult not like the peoples ; for you have played the whore , forsaking your God . You have loved a prostitute’s wages on all threshing floors .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:5** (✓) *target: people*
  > Hos 10:5 The inhabitants of Samaria tremble for the calf of Beth-aven . Its people mourn for it, and so do its idolatrous priests — those who rejoiced over it and over its glory — for it has departed from them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:10** (✓) *target: nations*
  > Hos 10:10 When I please , I will discipline them, and nations shall be gathered against them when they are bound up for their double iniquity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 10:14** (✓) *target: people*
  > Hos 10:14 therefore the tumult of war shall arise among your people , and all your fortresses shall be destroyed , as Shalman destroyed Beth-arbel on the day of battle ; mothers were dashed in pieces with their children .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hos 11:7** (✓) *target: people*
  > Hos 11:7 My people are bent on turning away from me, and though they call out to the Most High , he shall not raise them up at all .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:2** (✓) *target: people*
  > Joe 2:2 a day of darkness and gloom , a day of clouds and thick darkness ! Like blackness there is spread upon the mountains a great and powerful people ; their like has never been before , nor will be again after them through the years of all generations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:6** (✓) *target: peoples*
  > Joe 2:6 Before them peoples are in anguish ; all faces grow pale .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:16** (✓) *target: people*
  > Joe 2:16 gather the people . Consecrate the congregation ; assemble the elders ; gather the children , even nursing infants. Let the bridegroom leave his room , and the bride her chamber .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:17** (✓) *target: people*
  > Joe 2:17 Between the vestibule and the altar let the priests , the ministers of the Lord , weep and say , “ Spare your people , O Lord , and make not your heritage a reproach , a byword among the nations . Why should they say among the peoples , ‘ Where is their God ?’”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:18** (✓) *target: people*
  > Joe 2:18 Then the Lord became jealous for his land and had pity on his people .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:19** (✓) *target: people*
  > Joe 2:19 The Lord answered and said to his people , “ Behold , I am sending to you grain , wine , and oil , and you will be satisfied ; and I will no more make you a reproach among the nations .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:26** (✓) *target: people*
  > Joe 2:26 “You shall eat in plenty and be satisfied , and praise the name of the Lord your God , who has dealt wondrously with you. And my people shall never again be put to shame .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 2:27** (✓) *target: people*
  > Joe 2:27 You shall know that I am in the midst of Israel , and that I am the Lord your God and there is none else . And my people shall never again be put to shame .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:2** (✓) *target: people*
  > Joe 3:2 I will gather all the nations and bring them down to the Valley of Jehoshaphat . And I will enter into judgment with them there , on behalf of my people and my heritage Israel , because they have scattered them among the nations and have divided up my land ,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:3** (✓) *target: people*
  > Joe 3:3 and have cast lots for my people , and have traded a boy for a prostitute , and have sold a girl for wine and have drunk it.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Joe 3:16** (✓) *target: people*
  > Joe 3:16 The Lord roars from Zion , and utters his voice from Jerusalem , and the heavens and the earth quake . But the Lord is a refuge to his people , a stronghold to the people of Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 1:5** (✓) *target: people*
  > Amo 1:5 I will break the gate-bar of Damascus , and cut off the inhabitants from the Valley of Aven , and him who holds the scepter from Beth-eden ; and the people of Syria shall go into exile to Kir ,” says the Lord .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 3:6** (✓) *target: people*
  > Amo 3:6 Is a trumpet blown in a city , and the people are not afraid ? Does disaster come to a city , unless the Lord has done it?
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 7:8** (✓) *target: people*
  > Amo 7:8 And the Lord said to me, “ Amos , what do you see ?” And I said , “A plumb line .” Then the Lord said , “ Behold , I am setting a plumb line in the midst of my people Israel ; I will never again pass by them ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 7:15** (✓) *target: people*
  > Amo 7:15 But the Lord took me from following the flock , and the Lord said to me, ‘ Go , prophesy to my people Israel .’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 8:2** (✓) *target: people*
  > Amo 8:2 And he said , “ Amos , what do you see ?” And I said , “A basket of summer fruit .” Then the Lord said to me , “The end has come upon my people Israel ; I will never again pass by them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 9:10** (✓) *target: people*
  > Amo 9:10 All the sinners of my people shall die by the sword , who say , ‘ Disaster shall not overtake or meet us.’
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Amo 9:14** (✓) *target: people*
  > Amo 9:14 I will restore the fortunes of my people Israel , and they shall rebuild the ruined cities and inhabit them; they shall plant vineyards and drink their wine , and they shall make gardens and eat their fruit .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Obd 13** (✓) *target: people*
  > Obd 13 Do not enter the gate of my people in the day of their calamity ; do not gloat over his disaster in the day of his calamity ; do not loot his wealth in the day of his calamity .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Jon 1:8** (✓) *target: people*
  > Jon 1:8 Then they said to him, “ Tell us on whose account this evil has come upon us. What is your occupation ? And where do you come from? What is your country ? And of what people are you ?”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 1:2** (✓) *target: peoples*
  > Mic 1:2 Hear , you peoples , all of you; pay attention , O earth , and all that is in it, and let the Lord God be a witness against you, the Lord from his holy temple .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 1:9** (✓) *target: people*
  > Mic 1:9 For her wound is incurable , and it has come to Judah ; it has reached to the gate of my people , to Jerusalem .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:4** (✓) *target: people*
  > Mic 2:4 In that day they shall take up a taunt song against you and moan bitterly , and say , “We are utterly ruined ; he changes the portion of my people ; how he removes it from me! To an apostate he allots our fields .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:8** (✓) *target: people*
  > Mic 2:8 But lately my people have risen up as an enemy ; you strip the rich robe from those who pass by trustingly with no thought of war .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:9** (✓) *target: people*
  > Mic 2:9 The women of my people you drive out from their delightful houses ; from their young children you take away my splendor forever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 2:11** (✓) *target: people*
  > Mic 2:11 If a man should go about and utter wind and lies , saying, “I will preach to you of wine and strong drink ,” he would be the preacher for this people !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 3:3** (✓) *target: people*
  > Mic 3:3 who eat the flesh of my people , and flay their skin from off them, and break their bones in pieces and chop them up like meat in a pot , like flesh in a cauldron .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 3:5** (✓) *target: people*
  > Mic 3:5 Thus says the Lord concerning the prophets who lead my people astray , who cry “ Peace ” when they have something to eat , but declare war against him who puts nothing into their mouths .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:1** (✓) *target: peoples*
  > Mic 4:1 It shall come to pass in the latter days that the mountain of the house of the Lord shall be established as the highest of the mountains , and it shall be lifted up above the hills ; and peoples shall flow to it,
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:3** (✓) *target: peoples*
  > Mic 4:3 He shall judge between many peoples , and shall decide disputes for strong nations far away; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore ;
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:5** (✓) *target: peoples*
  > Mic 4:5 For all the peoples walk each in the name of its god , but we will walk in the name of the Lord our God forever and ever .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 4:13** (✓) *target: peoples*
  > Mic 4:13 Arise and thresh , O daughter of Zion , for I will make your horn iron , and I will make your hoofs bronze ; you shall beat in pieces many peoples ; and shall devote their gain to the Lord , their wealth to the Lord of the whole earth .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 5:7** (✓) *target: peoples*
  > Mic 5:7 Then the remnant of Jacob shall be in the midst of many peoples like dew from the Lord , like showers on the grass , which delay not for a man nor wait for the children of man .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 5:8** (✓) *target: peoples*
  > Mic 5:8 And the remnant of Jacob shall be among the nations , in the midst of many peoples , like a lion among the beasts of the forest , like a young lion among the flocks of sheep , which , when it goes through, treads down and tears in pieces, and there is none to deliver .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:2** (✓) *target: people*
  > Mic 6:2 Hear , you mountains , the indictment of the Lord , and you enduring foundations of the earth , for the Lord has an indictment against his people , and he will contend with Israel .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:3** (✓) *target: people*
  > Mic 6:3 “O my people , what have I done to you? How have I wearied you? Answer me !
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:5** (✓) *target: people*
  > Mic 6:5 O my people , remember what Balak king of Moab devised , and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal , that you may know the righteous acts of the Lord .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 6:16** (✓) *target: people*
  > Mic 6:16 For you have kept the statutes of Omri , and all the works of the house of Ahab ; and you have walked in their counsels , that I may make you a desolation , and your inhabitants a hissing ; so you shall bear the scorn of my people .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Mic 7:14** (✓) *target: people*
  > Mic 7:14 Shepherd your people with your staff , the flock of your inheritance , who dwell alone in a forest in the midst of a garden land ; let them graze in Bashan and Gilead as in the days of old .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Nah 3:18** (✓) *target: people*
  > Nah 3:18 Your shepherds are asleep , O king of Assyria ; your nobles slumber . Your people are scattered on the mountains with none to gather them.
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:5** (✓) *target: peoples*
  > Hab 2:5 “ Moreover , wine is a traitor , an arrogant man who is never at rest . His greed is as wide as Sheol ; like death he has never enough . He gathers for himself all nations and collects as his own all peoples .”
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:8** (✓) *target: peoples*
  > Hab 2:8 Because you have plundered many nations , all the remnant of the peoples shall plunder you, for the blood of man and violence to the earth , to cities and all who dwell in them .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2
- **Hab 2:10** (✓) *target: peoples*
  > Hab 2:10 You have devised shame for your house by cutting off many peoples ; you have forfeited your life .
  - notes: bulk_pending: individual verse review required per governing instruction s.6.2

**Group `5739-002`** (2 verses — anchors: Num 14:9, Num 14:11)

- **Num 14:9** 🔵 (✓) *target: people*
  > Num 14:9 Only do not rebel against the Lord . And do not fear the people of the land , for they are bread for us. Their protection is removed from them, and the Lord is with us; do not fear them .”
- **Num 14:11** 🔵 (✓) *target: people*
  > Num 14:11 And the Lord said to Moses , “ How long will this people despise me? And how long will they not believe in me, in spite of all the signs that I have done among them?

**Group `5739-003`** (1 verse — anchors: Exo 7:14)

- **Exo 7:14** 🔵 (✓) *target: people*
  > Exo 7:14 Then the Lord said to Moses , “ Pharaoh’s heart is hardened ; he refuses to let the people go .

### `H5973B` — 3/70 classified · 2 anchor verse(s)

**Group `5731-001`** (3 verses — anchors: Gen 44:29, Gen 44:32)

- **Gen 44:29** 🔵 (✓) *target: from*
  > Gen 44:29 If you take this one also from me , and harm happens to him , you will bring down my gray hairs in evil to Sheol .’
- **Gen 44:32** 🔵 (✓) *target: to*
  > Gen 44:32 For your servant became a pledge of safety for the boy to my father , saying , ‘ If I do not bring him back to you, then I shall bear the blame before my father all my life .’
- **Gen 41:32** (✓) *target: by*
  > Gen 41:32 And the doubling of Pharaoh’s dream means that the thing is fixed by God , and God will shortly bring it about .

**Group `UNCLASSIFIED`** (67 verses)

- **Gen 13:14** (—) *target: up*
  > Gen 13:14 The Lord said to Abram , after Lot had separated from him, “Lift up your eyes and look from the place where you are, northward and southward and eastward and westward ,
- **Gen 24:27** (—) *target: toward*
  > Gen 24:27 and said , “ Blessed be the Lord , the God of my master Abraham , who has not forsaken his steadfast love and his faithfulness toward my master . As for me, the Lord has led me in the way to the house of my master’s kinsmen .”
- **Gen 26:16** (—) *target: mightier*
  > Gen 26:16 And Abimelech said to Isaac , “ Go away from us, for you are much mightier than we.”
- **Gen 31:31** (—) *target: from*
  > Gen 31:31 Jacob answered and said to Laban , “ Because I was afraid , for I thought that you would take your daughters from me by force .
- **Gen 48:12** (—) *target: from*
  > Gen 48:12 Then Joseph removed them from his knees , and he bowed himself with his face to the earth .
- **Exo 8:12** (—) *target: Pharaoh*
  > Exo 8:12 So Moses and Aaron went out from Pharaoh , and Moses cried to the Lord about the frogs , as he had agreed with Pharaoh .
- **Exo 8:29** (—) *target: plead*
  > Exo 8:29 Then Moses said , “ Behold , I am going out from you and I will plead with the Lord that the swarms of flies may depart from Pharaoh , from his servants , and from his people , tomorrow . Only let not Pharaoh cheat again by not letting the people go to sacrifice to the Lord .”
- **Exo 8:30** (—) *target: Pharaoh*
  > Exo 8:30 So Moses went out from Pharaoh and prayed to the Lord .
- **Exo 9:33** (—) *target: Pharaoh*
  > Exo 9:33 So Moses went out of the city from Pharaoh and stretched out his hands to the Lord , and the thunder and the hail ceased , and the rain no longer poured upon the earth .
- **Exo 10:6** (—) *target: Pharaoh*
  > Exo 10:6 and they shall fill your houses and the houses of all your servants and of all the Egyptians , as neither your fathers nor your grandfathers have seen , from the day they came on earth to this day .’” Then he turned and went out from Pharaoh .
- **Exo 10:18** (—) *target: Pharaoh*
  > Exo 10:18 So he went out from Pharaoh and pleaded with the Lord .
- **Exo 11:8** (—) *target: Pharaoh*
  > Exo 11:8 And all these your servants shall come down to me and bow down to me, saying , ‘ Get out , you and all the people who follow you.’ And after that I will go out .” And he went out from Pharaoh in hot anger .
- **Exo 21:14** (—) *target: altar*
  > Exo 21:14 But if a man willfully attacks another to kill him by cunning , you shall take him from my altar , that he may die .
- **Exo 22:12** (—) *target: make restitution*
  > Exo 22:12 But if it is stolen from him, he shall make restitution to its owner .
- **Exo 22:14** (—) *target: it*
  > Exo 22:14 “ If a man borrows anything of his neighbor , and it is injured or dies , the owner not being with it , he shall make full restitution .
- **Lev 25:41** (—) *target: children*
  > Lev 25:41 Then he shall go out from you, he and his children with him, and go back to his own clan and return to the possession of his fathers .
- **Deu 10:12** (—) *target: but*
  > Deu 10:12 “And now , Israel , what does the Lord your God require of you, but to fear the Lord your God , to walk in all his ways , to love him, to serve the Lord your God with all your heart and with all your soul ,
- **Deu 15:12** (—) *target: you*
  > Deu 15:12 “ If your brother , a Hebrew man or a Hebrew woman , is sold to you, he shall serve you six years , and in the seventh year you shall let him go free from you .
- **Deu 15:13** (—) *target: not*
  > Deu 15:13 And when you let him go free from you, you shall not let him go empty-handed .
- **Deu 15:16** (—) *target: from*
  > Deu 15:16 But if he says to you, ‘I will not go out from you,’ because he loves you and your household , since he is well-off with you ,
- **Deu 15:18** (—) *target: for*
  > Deu 15:18 It shall not seem hard to you when you let him go free from you, for at half the cost of a hired worker he has served you six years . So the Lord your God will bless you in all that you do .
- **Deu 18:16** (—) *target: Lord*
  > Deu 18:16 just as you desired of the Lord your God at Horeb on the day of the assembly , when you said , ‘Let me not hear again the voice of the Lord my God or see this great fire any more , lest I die .’
- **Deu 18:19** (—) *target: of*
  > Deu 18:19 And whoever will not listen to my words that he shall speak in my name , I myself will require it of him .
- **Deu 23:15** (—) *target: master*
  > Deu 23:15 “You shall not give up to his master a slave who has escaped from his master to you.
- **Deu 23:21** (—) *target: sin*
  > Deu 23:21 “If you make a vow to the Lord your God , you shall not delay fulfilling it, for the Lord your God will surely require it of you, and you will be guilty of sin .
- **Deu 29:18** (—) *target: from*
  > Deu 29:18 Beware lest there be among you a man or woman or clan or tribe whose heart is turning away today from the Lord our God to go and serve the gods of those nations . Beware lest there be among you a root bearing poisonous and bitter fruit ,
- **Judg 9:37** (—) *target: center*
  > Judg 9:37 Gaal spoke again and said , “ Look , people are coming down from the center of the land , and one company is coming from the direction of the Diviners ’ Oak .”
- **Rut 2:12** (—) *target: Lord*
  > Rut 2:12 The Lord repay you for what you have done , and a full reward be given you by the Lord , the God of Israel , under whose wings you have come to take refuge !”
- **Rut 4:10** (—) *target: among*
  > Rut 4:10 Also Ruth the Moabite , the widow of Mahlon , I have bought to be my wife , to perpetuate the name of the dead in his inheritance , that the name of the dead may not be cut off from among his brothers and from the gate of his native place . You are witnesses this day .”
- **1Sa 1:17** (—) *target: to*
  > 1Sa 1:17 Then Eli answered , “ Go in peace , and the God of Israel grant your petition that you have made to him .”
- **1Sa 1:27** (—) *target: to*
  > 1Sa 1:27 For this child I prayed , and the Lord has granted me my petition that I made to him .
- **1Sa 2:33** (—) *target: altar*
  > 1Sa 2:33 The only one of you whom I shall not cut off from my altar shall be spared to weep his eyes out to grieve his heart , and all the descendants of your house shall die by the sword of men .
- **1Sa 10:9** (—) *target: Samuel*
  > 1Sa 10:9 When he turned his back to leave Samuel , God gave him another heart . And all these signs came to pass that day .
- **1Sa 14:17** (—) *target: from*
  > 1Sa 14:17 Then Saul said to the people who were with him, “ Count and see who has gone from us.” And when they had counted , behold , Jonathan and his armor-bearer were not there.
- **1Sa 16:14** (—) *target: Saul*
  > 1Sa 16:14 Now the Spirit of the Lord departed from Saul , and a harmful spirit from the Lord tormented him.
- **1Sa 18:12** (—) *target: with*
  > 1Sa 18:12 Saul was afraid of David because the Lord was with him but had departed from Saul .
- **1Sa 18:13** (—) *target: presence*
  > 1Sa 18:13 So Saul removed him from his presence and made him a commander of a thousand . And he went out and came in before the people .
- **1Sa 20:7** (—) *target: by*
  > 1Sa 20:7 If he says , ‘ Good !’ it will be well with your servant , but if he is angry , then know that harm is determined by him .
- **1Sa 20:9** (—) *target: father*
  > 1Sa 20:9 And Jonathan said , “ Far be it from you! If I knew that it was determined by my father that harm should come to you, would I not tell you ?”
- **1Sa 20:15** (—) *target: from*
  > 1Sa 20:15 and do not cut off your steadfast love from my house forever , when the Lord cuts off every one of the enemies of David from the face of the earth .”
- **1Sa 20:33** (—) *target: father*
  > 1Sa 20:33 But Saul hurled his spear at him to strike him. So Jonathan knew that his father was determined to put David to death .
- **1Sa 20:34** (—) *target: from*
  > 1Sa 20:34 And Jonathan rose from the table in fierce anger and ate no food the second day of the month , for he was grieved for David , because his father had disgraced him .
- **2Sa 1:2** (—) *target: Saul’s*
  > 2Sa 1:2 And on the third day , behold , a man came from Saul’s camp , with his clothes torn and dirt on his head . And when he came to David , he fell to the ground and paid homage .
- **2Sa 3:15** (—) *target: husband*
  > 2Sa 3:15 And Ish-bosheth sent and took her from her husband Paltiel the son of Laish .
- **2Sa 3:26** (—) *target: David’s*
  > 2Sa 3:26 When Joab came out from David’s presence, he sent messengers after Abner , and they brought him back from the cistern of Sirah . But David did not know about it.
- **2Sa 3:28** (—) *target: Lord*
  > 2Sa 3:28 Afterward , when David heard of it, he said , “ I and my kingdom are forever guiltless before the Lord for the blood of Abner the son of Ner .
- **2Sa 7:15** (—) *target: Saul*
  > 2Sa 7:15 but my steadfast love will not depart from him, as I took it from Saul , whom I put away from before you.
- **2Sa 15:28** (—) *target: from*
  > 2Sa 15:28 See , I will wait at the fords of the wilderness until word comes from you to inform me .”
- **2Sa 24:21** (—) *target: threshing floor*
  > 2Sa 24:21 And Araunah said , “Why has my lord the king come to his servant ?” David said , “ To buy the threshing floor from you, in order to build an altar to the Lord , that the plague may be averted from the people .”
- **1Ki 2:33** (—) *target: from*
  > 1Ki 2:33 So shall their blood come back on the head of Joab and on the head of his descendants forever . But for David and for his descendants and for his house and for his throne there shall be peace from the Lord forevermore .”
- **1Ki 11:9** (—) *target: Lord*
  > 1Ki 11:9 And the Lord was angry with Solomon , because his heart had turned away from the Lord , the God of Israel , who had appeared to him twice
- **1Ki 12:15** (—) *target: by*
  > 1Ki 12:15 So the king did not listen to the people , for it was a turn of affairs brought about by the Lord that he might fulfill his word , which the Lord spoke by Ahijah the Shilonite to Jeroboam the son of Nebat .
- **1Ki 14:5** (—) *target: of*
  > 1Ki 14:5 And the Lord said to Ahijah , “ Behold , the wife of Jeroboam is coming to inquire of you concerning her son , for he is sick . Thus and thus shall you say to her.” When she came , she pretended to be another woman.
- **2Ki 2:9** (—) *target: from*
  > 2Ki 2:9 When they had crossed , Elijah said to Elisha , “ Ask what I shall do for you, before I am taken from you.” And Elisha said , “ Please let there be a double portion of your spirit on me .”
- **1Ch 17:13** (—) *target: who*
  > 1Ch 17:13 I will be to him a father , and he shall be to me a son . I will not take my steadfast love from him, as I took it from him who was before you,
- **2Ch 10:15** (—) *target: by*
  > 2Ch 10:15 So the king did not listen to the people , for it was a turn of affairs brought about by God that the Lord might fulfill his word , which he spoke by Ahijah the Shilonite to Jeroboam the son of Nebat .
- **2Ch 32:7** (—) *target: more*
  > 2Ch 32:7 “Be strong and courageous . Do not be afraid or dismayed before the king of Assyria and all the horde that is with him, for there are more with us than with him .
- **Job 1:12** (—) *target: presence*
  > Job 1:12 And the Lord said to Satan , “ Behold , all that he has is in your hand . Only against him do not stretch out your hand .” So Satan went out from the presence of the Lord .
- **Job 28:4** (—) *target: where*
  > Job 28:4 He opens shafts in a valley away from where anyone lives ; they are forgotten by travelers ; they hang in the air , far away from mankind ; they swing to and fro .
- **Job 34:33** (—) *target: repayment*
  > Job 34:33 Will he then make repayment to suit you, because you reject it? For you must choose , and not I; therefore declare what you know .
- **Psa 89:33** (—) *target: him*
  > Psa 89:33 but I will not remove from him my steadfast love or be false to my faithfulness .
- **Psa 121:2** (—) *target: from*
  > Psa 121:2 My help comes from the Lord , who made heaven and earth .
- **Isa 7:11** (—) *target: Lord*
  > Isa 7:11 “ Ask a sign of the Lord your God ; let it be deep as Sheol or high as heaven .”
- **Isa 8:18** (—) *target: from*
  > Isa 8:18 Behold , I and the children whom the Lord has given me are signs and portents in Israel from the Lord of hosts , who dwells on Mount Zion .
- **Isa 28:29** (—) *target: from*
  > Isa 28:29 This also comes from the Lord of hosts ; he is wonderful in counsel and excellent in wisdom .
- **Isa 29:6** (—) *target: Lord*
  > Isa 29:6 you will be visited by the Lord of hosts with thunder and with earthquake and great noise , with whirlwind and tempest , and the flame of a devouring fire .
- **Jer 34:14** (—) *target: service*
  > Jer 34:14 ‘At the end of seven years each of you must set free the fellow Hebrew who has been sold to you and has served you six years ; you must set him free from your service .’ But your fathers did not listen to me or incline their ears to me.

### `H5974` — 8/20 classified · 2 anchor verse(s)

**Group `5735-001`** (8 verses — anchors: Dan 2:18, Dan 4:34)

- **Dan 2:18** 🔵 (✓) *target: with*
  > Dan 2:18 and told them to seek mercy from the God of heaven concerning this mystery , so that Daniel and his companions might not be destroyed with the rest of the wise men of Babylon .
- **Dan 4:34** 🔵 (✓) *target: endures from*
  > Dan 4:34 At the end of the days I , Nebuchadnezzar , lifted my eyes to heaven , and my reason returned to me, and I blessed the Most High , and praised and honored him who lives forever , for his dominion is an everlasting dominion , and his kingdom endures from generation to generation ;
- **Ezr 5:2** (✓) *target: with*
  > Ezr 5:2 Then Zerubbabel the son of Shealtiel and Jeshua the son of Jozadak arose and began to rebuild the house of God that is in Jerusalem , and the prophets of God were with them, supporting them .
- **Dan 2:22** (✓) *target: with him*
  > Dan 2:22 he reveals deep and hidden things ; he knows what is in the darkness , and the light dwells with him .
- **Dan 4:2** (✓) *target: for me*
  > Dan 4:2 It has seemed good to me to show the signs and wonders that the Most High God has done for me .
- **Dan 4:3** (✓) *target: endures from*
  > Dan 4:3 How great are his signs , how mighty his wonders ! His kingdom is an everlasting kingdom , and his dominion endures from generation to generation .
- **Dan 4:25** (✓) *target: with*
  > Dan 4:25 that you shall be driven from among men , and your dwelling shall be with the beasts of the field . You shall be made to eat grass like an ox , and you shall be wet with the dew of heaven , and seven periods of time shall pass over you, till you know that the Most High rules the kingdom of men and gives it to whom he will .
- **Dan 4:32** (✓) *target: with*
  > Dan 4:32 and you shall be driven from among men , and your dwelling shall be with the beasts of the field . And you shall be made to eat grass like an ox , and seven periods of time shall pass over you, until you know that the Most High rules the kingdom of men and gives it to whom he will .”

**Group `UNCLASSIFIED`** (12 verses)

- **Ezr 6:8** (—) *target: for*
  > Ezr 6:8 Moreover, I make a decree regarding what you shall do for these elders of the Jews for the rebuilding of this house of God . The cost is to be paid to these men in full and without delay from the royal revenue , the tribute of the province from Beyond the River .
- **Ezr 7:13** (—) *target: with*
  > Ezr 7:13 I make a decree that anyone of the people of Israel or their priests or Levites in my kingdom , who freely offers to go to Jerusalem , may go with you.
- **Ezr 7:16** (—) *target: with*
  > Ezr 7:16 with all the silver and gold that you shall find in the whole province of Babylonia , and with the freewill offerings of the people and the priests , vowed willingly for the house of their God that is in Jerusalem .
- **Dan 2:11** (—) *target: with*
  > Dan 2:11 The thing that the king asks is difficult , and no one can show it to the king except the gods , whose dwelling is not with flesh .”
- **Dan 2:43** (—) *target: together*
  > Dan 2:43 As you saw the iron mixed with soft clay , so they will mix with one another in marriage, but they will not hold together , just as iron does not mix with clay .
- **Dan 4:15** (—) *target: with*
  > Dan 4:15 But leave the stump of its roots in the earth , bound with a band of iron and bronze , amid the tender grass of the field . Let him be wet with the dew of heaven . Let his portion be with the beasts in the grass of the earth .
- **Dan 4:23** (—) *target: with*
  > Dan 4:23 And because the king saw a watcher , a holy one , coming down from heaven and saying , ‘ Chop down the tree and destroy it, but leave the stump of its roots in the earth , bound with a band of iron and bronze , in the tender grass of the field , and let him be wet with the dew of heaven , and let his portion be with the beasts of the field , till seven periods of time pass over him ,’
- **Dan 5:21** (—) *target: like*
  > Dan 5:21 He was driven from among the children of mankind , and his mind was made like that of a beast , and his dwelling was with the wild donkeys . He was fed grass like an ox , and his body was wet with the dew of heaven , until he knew that the Most High God rules the kingdom of mankind and sets over it whom he will .
- **Dan 6:21** (—) *target: to*
  > Dan 6:21 Then Daniel said to the king , “O king , live forever !
- **Dan 7:2** (—) *target: by*
  > Dan 7:2 Daniel declared , “I saw in my vision by night , and behold , the four winds of heaven were stirring up the great sea .
- **Dan 7:13** (—) *target: with*
  > Dan 7:13 “I saw in the night visions , and behold , with the clouds of heaven there came one like a son of man , and he came to the Ancient of Days and was presented before him .
- **Dan 7:21** (—) *target: with*
  > Dan 7:21 As I looked , this horn made war with the saints and prevailed over them ,

### `H5978` — 18/42 classified · 6 anchor verse(s)

**Group `952-001`** (7 verses — anchors: Gen 28:20, Psa 23:4)

- **Gen 28:20** 🔵 (✓) *target: keep me*
  > Gen 28:20 Then Jacob made a vow , saying , “ If God will be with me and will keep me in this way that I go , and will give me bread to eat and clothing to wear ,
- **Psa 23:4** 🔵 (✓) *target: with*
  > Psa 23:4 Even though I walk through the valley of the shadow of death , I will fear no evil , for you are with me; your rod and your staff , they comfort me .
- **Gen 31:5** (✓) *target: with*
  > Gen 31:5 and said to them, “I see that your father does not regard me with favor as he did before . But the God of my father has been with me .
- **Gen 35:3** (✓) *target: wherever*
  > Gen 35:3 Then let us arise and go up to Bethel , so that I may make there an altar to the God who answers me in the day of my distress and has been with me wherever I have gone .”
- **Lev 25:23** (✓) *target: with*
  > Lev 25:23 “The land shall not be sold in perpetuity , for the land is mine. For you are strangers and sojourners with me .
- **1Sa 22:23** (✓) *target: With*
  > 1Sa 22:23 Stay with me; do not be afraid , for he who seeks my life seeks your life . With me you shall be in safekeeping .”
- **Job 29:5** (✓) *target: around*
  > Job 29:5 when the Almighty was yet with me, when my children were all around me,

**Group `952-002`** (6 verses — anchors: Job 6:4, Job 9:35)

- **Job 6:4** 🔵 (✓) *target: in*
  > Job 6:4 For the arrows of the Almighty are in me; my spirit drinks their poison ; the terrors of God are arrayed against me .
- **Job 9:35** 🔵 (✓) *target: in*
  > Job 9:35 Then I would speak without fear of him, for I am not so in myself .
- **Job 10:12** (✓) *target: care*
  > Job 10:12 You have granted me life and steadfast love, and your care has preserved my spirit .
- **Job 23:6** (✓) *target: with*
  > Job 23:6 Would he contend with me in the greatness of his power ? No ; he would pay attention to me .
- **Job 23:10** (✓) *target: take*
  > Job 23:10 But he knows the way that I take ; when he has tried me, I shall come out as gold .
- **Job 29:20** (✓) *target: with*
  > Job 29:20 my glory fresh with me, and my bow ever new in my hand .’

**Group `952-003`** (5 verses — anchors: 1Sa 20:14, 2Sa 10:2)

- **1Sa 20:14** 🔵 (✓) *target: steadfast love*
  > 1Sa 20:14 If I am still alive , show me the steadfast love of the Lord , that I may not die ;
- **2Sa 10:2** 🔵 (✓) *target: loyally*
  > 2Sa 10:2 And David said , “I will deal loyally with Hanun the son of Nahash , as his father dealt loyally with me.” So David sent by his servants to console him concerning his father . And David’s servants came into the land of the Ammonites .
- **Gen 47:29** (✓) *target: kindly*
  > Gen 47:29 And when the time drew near that Israel must die , he called his son Joseph and said to him, “ If now I have found favor in your sight , put your hand under my thigh and promise to deal kindly and truly with me. Do not bury me in Egypt ,
- **Job 13:20** (✓) *target: face*
  > Job 13:20 Only grant me two things, then I will not hide myself from your face :
- **Psa 101:6** (✓) *target: with*
  > Psa 101:6 I will look with favor on the faithful in the land , that they may dwell with me; he who walks in the way that is blameless shall minister to me .

**Group `UNCLASSIFIED`** (24 verses)

- **Gen 3:12** (—) *target: with*
  > Gen 3:12 The man said , “The woman whom you gave to be with me, she gave me fruit of the tree , and I ate .”
- **Gen 19:19** (—) *target: me*
  > Gen 19:19 Behold , your servant has found favor in your sight , and you have shown me great kindness in saving my life . But I cannot escape to the hills , lest the disaster overtake me and I die .
- **Gen 20:9** (—) *target: to*
  > Gen 20:9 Then Abimelech called Abraham and said to him, “What have you done to us? And how have I sinned against you, that you have brought on me and my kingdom a great sin ? You have done to me things that ought not to be done .”
- **Gen 20:13** (—) *target: place*
  > Gen 20:13 And when God caused me to wander from my father’s house , I said to her, ‘This is the kindness you must do me: at every place to which we come , say of me, “ He is my brother .”’”
- **Gen 21:23** (—) *target: land*
  > Gen 21:23 Now therefore swear to me here by God that you will not deal falsely with me or with my descendants or with my posterity , but as I have dealt kindly with you, so you will deal with me and with the land where you have sojourned .”
- **Gen 29:19** (—) *target: with*
  > Gen 29:19 Laban said , “It is better that I give her to you than that I should give her to any other man ; stay with me .”
- **Gen 29:27** (—) *target: seven*
  > Gen 29:27 Complete the week of this one, and we will give you the other also in return for serving me another seven years .”
- **Gen 31:7** (—) *target: me*
  > Gen 31:7 yet your father has cheated me and changed my wages ten times . But God did not permit him to harm me .
- **Gen 31:32** (—) *target: have*
  > Gen 31:32 Anyone with whom you find your gods shall not live . In the presence of our kinsmen point out what I have that is yours, and take it.” Now Jacob did not know that Rachel had stolen them .
- **Gen 40:14** (—) *target: kindness*
  > Gen 40:14 Only remember me, when it is well with you, and please do me the kindness to mention me to Pharaoh , and so get me out of this house .
- **Exo 17:2** (—) *target: test*
  > Exo 17:2 Therefore the people quarreled with Moses and said , “ Give us water to drink .” And Moses said to them, “ Why do you quarrel with me? Why do you test the Lord ?”
- **Deu 5:31** (—) *target: me*
  > Deu 5:31 But you, stand here by me , and I will tell you the whole commandment and the statutes and the rules that you shall teach them, that they may do them in the land that I am giving them to possess .’
- **Judg 17:10** (—) *target: father*
  > Judg 17:10 And Micah said to him, “ Stay with me, and be to me a father and a priest , and I will give you ten pieces of silver a year and a suit of clothes and your living .” And the Levite went in .
- **1Sa 10:2** (—) *target: meet*
  > 1Sa 10:2 When you depart from me today , you will meet two men by Rachel’s tomb in the territory of Benjamin at Zelzah , and they will say to you, ‘The donkeys that you went to seek are found , and now your father has ceased to care about the donkeys and is anxious about you, saying , “ What shall I do about my son ?”’
- **1Sa 20:28** (—) *target: to*
  > 1Sa 20:28 Jonathan answered Saul , “ David earnestly asked leave of me to go to Bethlehem .
- **2Sa 19:33** (—) *target: with*
  > 2Sa 19:33 And the king said to Barzillai , “Come over with me, and I will provide for you with me in Jerusalem .”
- **Job 10:17** (—) *target: toward*
  > Job 10:17 You renew your witnesses against me and increase your vexation toward me; you bring fresh troops against me .
- **Job 13:19** (—) *target: silent*
  > Job 13:19 Who is there who will contend with me? For then I would be silent and die .
- **Job 17:2** (—) *target: Surely*
  > Job 17:2 Surely there are mockers about me, and my eye dwells on their provocation .
- **Job 28:14** (—) *target: with*
  > Job 28:14 The deep says , ‘It is not in me,’ and the sea says , ‘It is not with me .’
- **Job 29:6** (—) *target: streams*
  > Job 29:6 when my steps were washed with butter , and the rock poured out for me streams of oil !
- **Job 31:13** (—) *target: against*
  > Job 31:13 “ If I have rejected the cause of my manservant or my maidservant , when they brought a complaint against me ,
- **Psa 50:11** (—) *target: mine*
  > Psa 50:11 I know all the birds of the hills , and all that moves in the field is mine .
- **Psa 55:18** (—) *target: me*
  > Psa 55:18 He redeems my soul in safety from the battle that I wage , for many are arrayed against me .

### `H5980` — 0/28 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (28 verses)

- **Exo 25:27** (—) *target: Close to*
  > Exo 25:27 Close to the frame the rings shall lie, as holders for the poles to carry the table .
- **Exo 28:27** (—) *target: at*
  > Exo 28:27 And you shall make two rings of gold , and attach them in front to the lower part of the two shoulder pieces of the ephod , at its seam above the skillfully woven band of the ephod .
- **Exo 37:14** (—) *target: Close*
  > Exo 37:14 Close to the frame were the rings , as holders for the poles to carry the table .
- **Exo 38:18** (—) *target: corresponding*
  > Exo 38:18 And the screen for the gate of the court was embroidered with needlework in blue and purple and scarlet yarns and fine twined linen . It was twenty cubits long and five cubits high in its breadth , corresponding to the hangings of the court .
- **Exo 39:20** (—) *target: at*
  > Exo 39:20 And they made two rings of gold , and attached them in front to the lower part of the two shoulder pieces of the ephod , at its seam above the skillfully woven band of the ephod .
- **Lev 3:9** (—) *target: close to*
  > Lev 3:9 Then from the sacrifice of the peace offering he shall offer as a food offering to the Lord its fat ; he shall remove the whole fat tail , cut off close to the backbone , and the fat that covers the entrails and all the fat that is on the entrails
- **2Sa 16:13** (—) *target: opposite*
  > 2Sa 16:13 So David and his men went on the road , while Shimei went along on the hillside opposite him and cursed as he went and threw stones at him and flung dust .
- **1Ki 7:20** (—) *target: rounded projection*
  > 1Ki 7:20 The capitals were on the two pillars and also above the rounded projection which was beside the latticework . There were two hundred pomegranates in two rows all around , and so with the other capital .
- **1Ch 24:31** (—) *target: alike*
  > 1Ch 24:31 These also , the head of each father’s house and his younger brother alike , cast lots , just as their brothers the sons of Aaron , in the presence of King David , Zadok , Ahimelech , and the heads of fathers’ houses of the priests and of the Levites .
- **1Ch 25:8** (—) *target: alike*
  > 1Ch 25:8 And they cast lots for their duties , small and great , teacher and pupil alike .
- **1Ch 26:12** (—) *target: just as*
  > 1Ch 26:12 These divisions of the gatekeepers , corresponding to their chief men , had duties , just as their brothers did, ministering in the house of the Lord .
- **1Ch 26:16** (—) *target: corresponded to*
  > 1Ch 26:16 For Shuppim and Hosah it came out for the west , at the gate of Shallecheth on the road that goes up . Watch corresponded to watch .
- **Neh 12:24** (—) *target: stood*
  > Neh 12:24 And the chiefs of the Levites : Hashabiah , Sherebiah , and Jeshua the son of Kadmiel , with their brothers who stood opposite them, to praise and to give thanks , according to the commandment of David the man of God , watch by watch .
- **Ecc 5:16** (—) *target: just*
  > Ecc 5:16 This also is a grievous evil : just as he came , so shall he go , and what gain is there to him who toils for the wind ?
- **Ecc 7:14** (—) *target: well as*
  > Ecc 7:14 In the day of prosperity be joyful , and in the day of adversity consider : God has made the one as well as the other , so that man may not find out anything that will be after him.
- **Eze 1:20** (—) *target: along with*
  > Eze 1:20 Wherever the spirit wanted to go , they went , and the wheels rose along with them, for the spirit of the living creatures was in the wheels .
- **Eze 1:21** (—) *target: along with*
  > Eze 1:21 When those went , these went ; and when those stood , these stood ; and when those rose from the earth , the wheels rose along with them, for the spirit of the living creatures was in the wheels .
- **Eze 3:8** (—) *target: as*
  > Eze 3:8 Behold , I have made your face as hard as their faces , and your forehead as hard as their foreheads .
- **Eze 3:13** (—) *target: beside*
  > Eze 3:13 It was the sound of the wings of the living creatures as they touched one another , and the sound of the wheels beside them, and the sound of a great earthquake .
- **Eze 10:19** (—) *target: beside*
  > Eze 10:19 And the cherubim lifted up their wings and mounted up from the earth before my eyes as they went out , with the wheels beside them. And they stood at the entrance of the east gate of the house of the Lord , and the glory of the God of Israel was over them.
- **Eze 11:22** (—) *target: beside*
  > Eze 11:22 Then the cherubim lifted up their wings , with the wheels beside them, and the glory of the God of Israel was over them.
- **Eze 40:18** (—) *target: corresponding to*
  > Eze 40:18 And the pavement ran along the side of the gates , corresponding to the length of the gates . This was the lower pavement .
- **Eze 42:7** (—) *target: parallel*
  > Eze 42:7 And there was a wall outside parallel to the chambers , toward the outer court , opposite the chambers , fifty cubits long .
- **Eze 45:6** (—) *target: assign*
  > Eze 45:6 “Alongside the portion set apart as the holy district you shall assign for the property of the city an area 5,000 cubits broad and 25,000 cubits long . It shall belong to the whole house of Israel .
- **Eze 45:7** (—) *target: corresponding*
  > Eze 45:7 “And to the prince shall belong the land on both sides of the holy district and the property of the city , alongside the holy district and the property of the city , on the west and on the east , corresponding in length to one of the tribal portions , and extending from the western to the eastern boundary
- **Eze 48:13** (—) *target: alongside*
  > Eze 48:13 And alongside the territory of the priests , the Levites shall have an allotment 25,000 cubits in length and 10,000 in breadth . The whole length shall be 25,000 cubits and the breadth 20,000 .
- **Eze 48:18** (—) *target: alongside*
  > Eze 48:18 The remainder of the length alongside the holy portion shall be 10,000 cubits to the east , and 10,000 to the west , and it shall be alongside the holy portion . Its produce shall be food for the workers of the city .
- **Eze 48:21** (—) *target: parallel*
  > Eze 48:21 “What remains on both sides of the holy portion and of the property of the city shall belong to the prince. Extending from the 25,000 cubits of the holy portion to the east border , and westward from the 25,000 cubits to the west border , parallel to the tribal portions , it shall belong to the prince . The holy portion with the sanctuary of the temple shall be in its midst .

### `H6004` — 0/3 classified · 0 anchor verse(s)

**Group `UNCLASSIFIED`** (3 verses)

- **Lam 4:1** (—) *target: grown dim*
  > Lam 4:1 How the gold has grown dim , how the pure gold is changed ! The holy stones lie scattered at the head of every street .
- **Eze 28:3** (—) *target: hidden*
  > Eze 28:3 you are indeed wiser than Daniel ; no secret is hidden from you ;
- **Eze 31:8** (—) *target: rival*
  > Eze 31:8 The cedars in the garden of God could not rival it, nor the fir trees equal its boughs ; neither were the plane trees like its branches ; no tree in the garden of God was its equal in beauty .

### `G5541` — 1/1 classified · 1 anchor verse(s)

**Group `5729-001`** (1 verse — anchors: 1Cor 13:4)

- **1Cor 13:4** 🔵 (✓) *target: kind*
  > 1Cor 13:4 Love is patient and kind ; love does not envy or boast ; it is not arrogant

### `G5542` — 1/1 classified · 1 anchor verse(s)

**Group `5730-001`** (1 verse — anchors: Rom 16:18)

- **Rom 16:18** 🔵 (✓) *target: smooth talk*
  > Rom 16:18 For such persons do not serve our Lord Christ , but their own appetites , and by smooth talk and flattery they deceive the hearts of the naive .

### `G5543` — 6/7 classified · 2 anchor verse(s)

**Group `954-001`** (6 verses — anchors: Rom 2:4, Eph 4:32)

- **Rom 2:4** 🔵 (✓) *target: kindness*
  > Rom 2:4 Or do you presume on the riches of his kindness and forbearance and patience , not knowing that God’s kindness is meant to lead you to repentance ?
- **Eph 4:32** 🔵 (✓) *target: kind*
  > Eph 4:32 Be kind to one another , tenderhearted , forgiving one another , as God in Christ forgave you .
- **Mat 11:30** (✓) *target: easy*
  > Mat 11:30 For my yoke is easy , and my burden is light .”
- **Luk 6:35** (✓) *target: kind*
  > Luk 6:35 But love your enemies , and do good , and lend , expecting nothing in return , and your reward will be great , and you will be sons of the Most High , for he is kind to the ungrateful and the evil .
- **1Cor 15:33** (✓) *target: good*
  > 1Cor 15:33 Do not be deceived : “ Bad company ruins good morals .”
- **1Pe 2:3** (✓) *target: good*
  > 1Pe 2:3 if indeed you have tasted that the Lord is good .

**Group `UNCLASSIFIED`** (1 verse)

- **Luk 5:39** (—) *target: good*
  > Luk 5:39 And no one after drinking old wine desires new , for he says , ‘The old is good .’”

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**22 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H0120G` | man | `not_done` | 162 | 4 | 48 |
| `H1454` | this | `not_done` | 1 | 0 | 0 |
| `H1668` | this | `not_done` | 4 | 1 | 1 |
| `H1791` | this | `not_done` | 11 | 0 | 0 |
| `H1797` | this | `not_done` | 3 | 0 | 0 |
| `H1976` | this | `not_done` | 2 | 0 | 0 |
| `H2090` | this | `not_done` | 11 | 1 | 6 |
| `H2097` | this | `not_done` | 2 | 1 | 2 |
| `H2098` | this | `not_done` | 15 | 1 | 12 |
| `H5971B` | kinsman | `not_done` | 30 | 1 | 20 |
| `H5971H` | People's [Gate] | `not_done` | 430 | 3 | 430 |
| `H5971I` | [Ibleam]-am | `not_done` | 430 | 3 | 430 |
| `H5971K` | people: soldiers | `not_done` | 69 | 1 | 5 |
| `H5971L` | people: creatures | `not_done` | 430 | 3 | 430 |
| `H5973B` | from with | `not_done` | 70 | 1 | 3 |
| `H5974` | with | `not_done` | 20 | 1 | 8 |
| `H5978` | with me | `not_done` | 42 | 3 | 18 |
| `H5980` | close | `not_done` | 28 | 0 | 0 |
| `H6004` | to darken | `not_done` | 3 | 0 | 0 |
| `G5541` | be kind | `not_done` | 1 | 1 | 1 |
| `G5542` | smooth talk | `not_done` | 1 | 1 | 1 |
| `G5543` | good/kind | `not_done` | 7 | 1 | 6 |

---

## L. Stage 2b Foundational Input — Observation Question Catalogue

**Generic questions: 0** across 0 sections. The section grouping IS the Stage 2b chapter structure — Stage 2b works through the catalogue section-by-section, producing answers grouped by section.

### Section summary (generic)

| Section | n questions |
|---|---:|

### Generic questions (JSON, grouped by section)

Format: JSON. Structure: as-is from `wa_obs_question_catalogue`. Apply to every word.

```json
{
  "total": 0,
  "section_count": 0,
  "sections": {}
}
```

### Registry-specific questions for 099 kindness

_None._ No questions in `wa_obs_question_catalogue` are sourced from registry 99 (kindness).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-01T09:47:25Z`
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

*End of readiness output v3 — wa-099-kindness.*