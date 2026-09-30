# wa-111-mercy — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-04-28T06:25:08Z · schema 3.17.0_

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

- **Registry no:** `111` · **word:** `mercy`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v1.9-2026-04-09`)
- **cluster_assignment:** `C17`
- **sb_classification:** `Spirit-soul interface`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Relational/Social`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 65  (programme-wide aggregate including XREF and historical terms — current OWNER count is 25, XREF 26)
- `phase1_verse_count`: 1748  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 16 unresolved · **Existing session_b_findings:** 1

**Description:**

> Mercy is the compassionate response to someone in need or distress — the willingness to help, relieve, or spare those who have no claim on one's help. The Hebrew and Greek vocabulary is rich: racham (tender compassion, womb-love), chesed (steadfast loving-kindness), eleos (merciful concern). God's mercy is one of the most-repeated themes in Scripture: he is described as rich in mercy, slow to anger, abounding in steadfast love. Mercy has a direction — it always moves toward the one who is suffering or guilty — and it always costs the one who shows it something.

**sb_classification_reasoning:**

> Mercy is received at spirit level -- it originates in God and is mediated through the propitiation mechanism (a divine provision, not human achievement). It is expressed at soul level as compassion toward the other, directed in supplication toward God, and enacted in concrete acts of favour. The body mediates both directions: atoning blood provides the spirit-level covering (Lev 17:11); supplication posture expresses the soul-level appeal (Luk 18:13, 1Ki 8:38). Confidence: medium. Trichotomy-spanning alternative considered: the atonement sub-vocabulary has deep somatic involvement, but this operates instrumentally rather than as primary locus. Spirit-soul interface holds unless Session D corpus evidence indicates body-level transformation as an independent outcome of mercy.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-04-28T06:25:08Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 25
- **OWNER terms legacy-VC (not_done):** 25 / 25

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 25 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H2603A` | cha.nan | be gracious | H | `extracted` | **`to_revise`** | 1 | 72 | 1/0 | 71/0 | 2 |
| `H2604` | cha.nan | be gracious | H | `extracted_thin` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `H3722A` | kip.per | to atone | H | `extracted` | **`to_revise`** | 1 | 93 | 3/0 | 81/0 | 6 |
| `H3722B` | ka.phar | to cover | H | `extracted_thin` | **`to_revise`** | 1 | 93 | 3/0 | 81/0 | 6 |
| `H3724A` | ko.pher | ransom | H | `extracted` | **`to_revise`** | 1 | 13 | 2/0 | 13/0 | 3 |
| `H3725` | kip.pu.rim | atonement | H | `extracted` | **`to_revise`** | 1 | 8 | 1/0 | 8/0 | 1 |
| `H3727` | kap.po.ret | mercy seat | H | `extracted` | **`to_revise`** | 1 | 22 | 1/0 | 22/0 | 2 |
| `H3819` | lo ru.cha.mah | No Mercy | H | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 1 |
| `H5750` | od | still | H | `extracted` | **`to_revise`** | 1 | 170 | 2/0 | 14/0 | 4 |
| `H6279` | a.tar | to pray | H | `extracted` | **`to_revise`** | 1 | 19 | 2/0 | 19/0 | 4 |
| `H7359` | ra.cha.min | compassion | H | `extracted_thin` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H8467` | te.chin.nah | supplication | H | `extracted_thin` | **`to_revise`** | 1 | 24 | 2/0 | 24/0 | 3 |
| `G0415` | aneleēmōn | merciless | G | `extracted` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G0448` | anileōs | merciless | G | `extracted` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G0462` | anosios | unholy | G | `extracted_thin` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `G1653` | eleeō | to have mercy | G | `extracted` | **`to_revise`** | 1 | 28 | 3/0 | 28/0 | 6 |
| `G1655` | eleēmōn | merciful | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `G1656` | eleos | mercy | G | `extracted` | **`to_revise`** | 1 | 26 | 2/0 | 27/0 | 4 |
| `G2433` | hilaskomai | to propitiate | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `G2434` | hilasmos | propitiation | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `G2435` | hilastērios | propitiation | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `G2436` | hileōs | propitious/gracious | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 1 |
| `G3628` | oiktirmos | compassion | G | `extracted` | **`to_revise`** | 1 | 5 | 1/0 | 5/0 | 2 |
| `G3629` | oiktirmōn | compassionate | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 2 |
| `G3743` | hosiōs | devoutly | G | `extracted_thin` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H2603A` — cha.nan "be gracious"

**Identity:** mti=984 · ti=1045 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to be gracious, show favour, pity

Sub-senses (depth > 1): 6 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal) to show favour, be gracious
  - `1b` (under `None`): (Niphal) to be pitied
  - `1c` (under `None`): (Piel) to make gracious, make favourable, be gracious
  - `1d` (under `None`): (Poel) to direct favour to, have mercy on
  - `1e` (under `None`): (Hophal) to be shown favour, be shown consideration
  - `1f` (under `None`): (Hithpael) to seek favour, implore favour

**Root family:**
- `CHANAN` (Hebrew): be gracious — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (52 total; sample of 30):**
- `H2433` chin "beauty"
- `H2580` chen "favor"
- `H2581` chen "Hen"
- `H2582G` che.na.dad "Henadad"
- `H2582H` che.na.dad "Henadad"
- `H2582I` che.na.dad "Henadad"
- `H2584` chan.nah "Hannah"
- `H2586G` cha.nun "Hanun"
- `H2586H` cha.nun "Hanun"
- `H2586I` cha.nun "Hanun"
- `H2587` chan.nun "gracious"
- `H2592G` chan.ni.el "Hanniel"
- `H2592H` chan.ni.el "Hanniel"
- `H2594` cha.ni.nah "favor"
- `H2600` chin.nam "for nothing"
- … and 15 more shown of 52 total

### `H2604` — cha.nan "be gracious"

**Identity:** mti=989 · ti=1053 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to show favour

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): (P'al) to show favour
  - `1b` (under `None`): (Ithpael) to implore favour

**Root family:**
- `CHANAN` (Hebrew): be gracious — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (18 total; sample of 18):**
- `H2603A` cha.nan "be gracious"
- `H2603B` cha.nan "be loathsome"
- `H2608A` cha.nan.ya.hu "Hananiah"
- `H2608B` cha.nan.yah "Hananiah"
- `H2608G` cha.nan.ya.hu "Hananiah"
- `H2608H` cha.nan.ya.hu "Hananiah"
- `H2608I` cha.nan.ya.hu "Hananiah"
- `H2608J` cha.nan.ya.hu "Hananiah"
- `H2608K` cha.nan.ya.hu "Hananiah"
- `H2608L` cha.nan.ya.hu "Hananiah"
- `H2608M` cha.nan.ya.hu "Hananiah"
- `H2608N` cha.nan.ya.hu "Hananiah"
- `H2608O` cha.nan.ya.hu "Hananiah"
- `H2608P` cha.nan.ya.hu "Hananiah"
- `H2608Q` cha.nan.ya.hu "Hananiah"
- … and 3 more shown of 18 total

### `H3722A` — kip.per "to atone"

**Identity:** mti=3169 · ti=3304 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to cover, purge, make an atonement, make reconciliation

Sub-senses (depth > 1): 8 entries — present in DB; first 15:
  - `1a` (under `None`): (Piel)
  - `1a1` (under `None`): to cover over, pacify, propitiate
  - `1a2` (under `None`): to cover over, atone for sin, make atonement for
  - `1a3` (under `None`): to cover over, atone for sin and persons by legal rites
  - `1b` (under `None`): (Pual)
  - `1b1` (under `None`): to be covered over
  - `1b2` (under `None`): to be atoned for
  - `1c` (under `None`): (Hithpael) to be covered

**Root family:**
- `KIPPER` (Hebrew): pitch — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (14 total; sample of 14):**
- `H3713A` ke.phor "bowl"
- `H3713B` ke.phor "frost"
- `H3715A` ke.phir "lion"
- `H3715B` ke.phi.rim "Hakkephirim"
- `H3715M` ke.phi.rim "villages"
- `H3722B` ka.phar "to cover"
- `H3723G` ka.phar "Chephar"
- `H3723H` ka.phar "village"
- `H3724A` ko.pher "ransom"
- `H3724B` ko.pher "pitch"
- `H3724C` ko.pher "henna"
- `H3724D` ko.pher "village"
- `H3725` kip.pu.rim "atonement"
- `H3727` kap.po.ret "mercy seat"

### `H3722B` — ka.phar "to cover"

**Identity:** mti=3173 · ti=3308 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: (Qal) to coat or cover with pitch

**Root family:**
- `KIPPER` (Hebrew): pitch — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (14 total; sample of 14):**
- `H3713A` ke.phor "bowl"
- `H3713B` ke.phor "frost"
- `H3715A` ke.phir "lion"
- `H3715B` ke.phi.rim "Hakkephirim"
- `H3715M` ke.phi.rim "villages"
- `H3722A` kip.per "to atone"
- `H3723G` ka.phar "Chephar"
- `H3723H` ka.phar "village"
- `H3724A` ko.pher "ransom"
- `H3724B` ko.pher "pitch"
- `H3724C` ko.pher "henna"
- `H3724D` ko.pher "village"
- `H3725` kip.pu.rim "atonement"
- `H3727` kap.po.ret "mercy seat"

### `H3724A` — ko.pher "ransom"

**Identity:** mti=3170 · ti=3305 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: price of a life, ransom, bribe

**Root family:**
- `KIPPER` (Hebrew): pitch — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H3722A` kip.per "to atone"
- `H3722B` ka.phar "to cover"
- `H3724B` ko.pher "pitch"
- `H3724C` ko.pher "henna"
- `H3724D` ko.pher "village"
- `H3725` kip.pu.rim "atonement"
- `H3727` kap.po.ret "mercy seat"

### `H3725` — kip.pu.rim "atonement"

**Identity:** mti=3171 · ti=3306 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: atonement

**Root family:**
- `KIPPER` (Hebrew): pitch — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H3722A` kip.per "to atone"
- `H3722B` ka.phar "to cover"
- `H3724A` ko.pher "ransom"
- `H3724B` ko.pher "pitch"
- `H3724C` ko.pher "henna"
- `H3724D` ko.pher "village"
- `H3727` kap.po.ret "mercy seat"

### `H3727` — kap.po.ret "mercy seat"

**Identity:** mti=982 · ti=1042 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: mercy-seat, place of atonement

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): the golden plate of propitiation on which the High Priest sprinkled the seat 7 times on the Day of Atonement symbolically reconciling Jehovah and His chosen people
  - `1a1` (under `None`): the slab of gold on top of the ark of the covenant which measured 2.5 by 1.5 cubits; on it and part of it were the two golden cherubim facing each other whose outstretched wings came together above and constituted the throne of God

**Root family:**
- `KIPPER` (Hebrew): pitch — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `H3722A` kip.per "to atone"
- `H3722B` ka.phar "to cover"
- `H3724A` ko.pher "ransom"
- `H3724B` ko.pher "pitch"
- `H3724C` ko.pher "henna"
- `H3724D` ko.pher "village"
- `H3725` kip.pu.rim "atonement"

### `H3819` — lo ru.cha.mah "No Mercy"

**Identity:** mti=986 · ti=1048 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: A woman living at the time of Divided Monarchy, first mentioned at Hos.1.6; 
only referred to as Lo-ruhamah (לֹא רֻחָ֫מָה); 
daughter of Hosea and Gomer; 
a sister of Jezreel, Lo-ammi H3818). § (Pual) symbolic name given by the prophet Hosea to his daughter

**Root family:**
- `LO RUCHA` (Hebrew): No Mercy — Backfilled 2026-04-09 from wa_term_related_words clustering

### `H5750` — od "still"

**Identity:** mti=990 · ti=1054 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T08:26:01): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: subst
1) a going round, continuance
adv
2) still, yet, again, besides
2a) still, yet (of continuance or persistence)
2b) still, yet, more (of addition or repetition)
2c) again
2d) still, moreover, besides
Aramaic equivalent: od (עוֹד "still" H5751)

**Root family:**
- `OD` (Hebrew): still — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (10 total; sample of 10):**
- `H5707` ed "witness"
- `H5713A` e.dah "witness"
- `H5713B` e.dah "testimony"
- `H5715` e.dut "testimony"
- `H5749A` ud "to return"
- `H5749B` ud "to testify"
- `H5751` od "still"
- `H5752G` o.ded "Oded"
- `H5752H` o.ded "Oded"
- `H8584` te.u.dah "testimony"

### `H6279` — a.tar "to pray"

**Identity:** mti=987 · ti=1051 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to pray, entreat, supplicate

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal) to pray, entreat
  - `1b` (under `None`): (Niphal) to be supplicated, be entreated
  - `1c` (under `None`): (Hiphil) to make supplication, plead

**Root family:**
- `ATAR` (Hebrew): odour — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `H6281` e.ter "Ether"
- `H6282A` a.tar "worshiper"
- `H6282B` a.tar "odour"

### `H7359` — ra.cha.min "compassion"

**Identity:** mti=988 · ti=1052 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: compassion
Aramaic of ra.cha.mim (רַחֲמִים "compassion" H7356B)

**Root family:**
- `RACHAMIN` (Hebrew): compassion — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H7313` rum "to rise"
- `H7314` rum "height"
- `H7328` raz "mystery"
- `H7348A` re.chum "Rehum"
- `H7348B` re.chum "Rehum"
- `H7348G` re.chum "Rehum"
- `H7348H` re.chum "Rehum"
- `H7356A` ra.cham "womb"
- `H7356B` ra.cha.mim "compassion"

### `H8467` — te.chin.nah "supplication"

**Identity:** mti=985 · ti=1046 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: favour, supplication, supplication for favour

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): favour
  - `1b` (under `None`): supplication for favour

**Root family:**
- `CHANAN` (Hebrew): be gracious — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (51 total; sample of 30):**
- `H2433` chin "beauty"
- `H2580` chen "favor"
- `H2581` chen "Hen"
- `H2582G` che.na.dad "Henadad"
- `H2582H` che.na.dad "Henadad"
- `H2582I` che.na.dad "Henadad"
- `H2584` chan.nah "Hannah"
- `H2586G` cha.nun "Hanun"
- `H2586H` cha.nun "Hanun"
- `H2586I` cha.nun "Hanun"
- `H2587` chan.nun "gracious"
- `H2592G` chan.ni.el "Hanniel"
- `H2592H` chan.ni.el "Hanniel"
- `H2594` cha.ni.nah "favor"
- `H2600` chin.nam "for nothing"
- … and 15 more shown of 51 total

### `G0415` — aneleēmōn "merciless"

**Identity:** mti=3165 · ti=3300 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: ruthless, merciless 
unmerciful, uncompassionate, cruel Rom. 1:31*

**Root family:**
- `ELE` (Greek): mercy — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G1655` eleēmōn "merciful"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0448` — anileōs "merciless"

**Identity:** mti=993 · ti=1058 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: merciless

**Root family:**
- `HILEŌS` (Greek): merciless — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G2436` hileōs "propitious/gracious"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0462` — anosios "unholy"

**Identity:** mti=3179 · ti=3314 · language=Greek · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: impious, unholy, wicked 1Tim. 1:9; 2Tim. 3:2*

**Root family:**
- `ANOSI` (Greek): unholy — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G3741` hosios "sacred"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G1653` — eleeō "to have mercy"

**Identity:** mti=981 · ti=1041 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to show mercy, be merciful 
see ἐλεέω, have mercy on, show mercy Rom. 9:16; 12:8; Jude 22, 23*

**Root family:**
- `ELE` (Greek): mercy — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G1653` eleeō "to have mercy"
- `G1655` eleēmōn "merciful"
- `G1656` eleos "mercy"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G1655` — eleēmōn "merciful"

**Identity:** mti=3164 · ti=3299 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: merciful, including feelings of pity, with a focus of showing compassion to those in serious need 
merciful, pitiful, compassionate, Mt. 5:7; Heb. 2:17*

**Root family:**
- `ELE` (Greek): mercy — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G0415` aneleēmōn "merciless"
- `G1653` eleeō "to have mercy"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G1656` — eleos "mercy"

**Identity:** mti=983 · ti=1043 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: mercy, pity; the moral quality of feeling compassion and especially of showing kindness toward someone in need. This can refer to a human kindness and to God’s kindness to humankind 
pity, mercy, compassion, Mt. 9:13; 12:7; Lk. 1:50, 78; metonymy benefit which results from compassion, kindness, mercies, blessing, Lk. 1:54, 58, 72; 10:37; Rom. 9:23

**Root family:**
- `ELE` (Greek): mercy — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G1652` eleeinos "pitiful"
- `G1653` eleeō "to have mercy"
- `G1654` eleēmosunē "charity"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2433` — hilaskomai "to propitiate"

**Identity:** mti=3176 · ti=3311 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: (middle voice) to make atonement for; to propitiate -- the human act of providing the means for forgiveness, resulting in reconciliation (Heb 2:17: "to make propitiation for the sins of the people")
- `2`: (passive voice) to receive mercy; to be forgiven; to have propitiation applied (Luk 18:13: "God, be merciful to me, a sinner" -- the sinners cry for propitiation to be turned toward him)

**Root family:**
- `HILEŌS` (Greek): merciless — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G2434` hilasmos "propitiation"
- `G2435` hilastērios "propitiation"
- `G2436` hileōs "propitious/gracious"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2434` — hilasmos "propitiation"

**Identity:** mti=3177 · ti=3312 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: atoning sacrifice, the means of forgiveness; traditionally propitiation 
atoning sacrifice, sin offering, propitiation, expiation; one who makes propitiation/expiation, 1Jn. 2:2; 4:10*

**Root family:**
- `HILEŌS` (Greek): merciless — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G2433` hilaskomai "to propitiate"
- `G2435` hilastērios "propitiation"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2435` — hilastērios "propitiation"

**Identity:** mti=991 · ti=1056 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: atoning sacrifice; atonement cover, the place where sins are forgiven; traditionally propitiation or mercy seat 
the cover of the ark of the covenant, the mercy-seat, the place of propitiation, Rom. 3:25; Heb. 9:5*

**Root family:**
- `HILEŌS` (Greek): merciless — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G2433` hilaskomai "to propitiate"
- `G2434` hilasmos "propitiation"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2436` — hileōs "propitious/gracious"

**Identity:** mti=3166 · ti=3301 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: forgiving, gracious; (may God be) gracious!, God forbid! 
propitious, favorable, merciful, gracious, forgiving Heb. 8:12; from the Hebrew, ἵλεως σοι (ὁ θεός) God have mercy on thee, God forbid, far be it from thee, God forbid Mt. 16:22*

**Root family:**
- `HILEŌS` (Greek): merciless — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G0448` anileōs "merciless"
- `G2431` hilaros "cheerful"
- `G2433` hilaskomai "to propitiate"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G3628` — oiktirmos "compassion"

**Identity:** mti=992 · ti=1057 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: compassion, mercy, pity 
compassion; kindness, pity in relieving sorrow and want, Phil. 2:1; Col. 3:12; Heb. 10:28; favor, grace, mercy, Rom. 12:1; 2Cor. 1:3*

**Root family:**
- `OIKTIR` (Greek): compassion — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G3627` oikteirō "to have compassion"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G3629` — oiktirmōn "compassionate"

**Identity:** mti=3158 · ti=3293 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: merciful, compassionate 
compassionate, merciful, Lk. 6:36; Jas. 5:11*

**Root family:**
- `OIKTIRMŌN` (Greek): compassionate — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G3627` oikteirō "to have compassion"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G3743` — hosiōs "devoutly"

**Identity:** mti=3181 · ti=3316 · language=Greek · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:20:57): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: - piously

**Root family:**
- `HOSIŌS` (Greek): devoutly — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G3741` hosios "sacred"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (26)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `G1652` | eleeinos | pitiful | G | 23 compassion | `extracted_thin` | 2 |
| `G1654` | eleēmosunē | charity | G | 23 compassion | `extracted_thin` | 13 |
| `G3627` | oikteirō | to have compassion | G | 23 compassion | `extracted` | 1 |
| `G3741` | hosios | sacred | G | 76 holiness | `extracted` | 8 |
| `G3742` | hosiotēs | holiness | G | 76 holiness | `extracted_thin` | 2 |
| `H2347` | chus | to pity | H | 23 compassion | `extracted` | 24 |
| `H2550` | cha.mal | to spare | H | 43 desire | `extracted` | 40 |
| `H2551` | chem.lah | compassion | H | 23 compassion | `extracted_thin` | 2 |
| `H2580` | chen | favor | H | 68 grace | `extracted` | 67 |
| `H2587` | chan.nun | gracious | H | 23 compassion | `extracted` | 13 |
| `H2594` | cha.ni.nah | favor | H | 23 compassion | `extracted_thin` | 0 |
| `H2600` | chin.nam | for nothing | H | ? | `extracted` | 0 |
| `H2616A` | cha.sad | be kind | H | 23 compassion | `extracted_thin` | 2 |
| `H2616B` | cha.sad | to shame | H | 146 shame | `extracted_thin` | 2 |
| `H2617A` | che.sed | kindness | H | 103 love | `extracted` | 169 |
| `H2617B` | che.sed | shame | H | 23 compassion | `extracted_thin` | 169 |
| `H2623` | cha.sid | pious | H | 103 love | `extracted` | 33 |
| `H4263` | mach.mal | compassion | H | 179 yearning | `extracted_thin` | 1 |
| `H4480A` | min- | from | H | 89 iniquity | `extracted` | 284 |
| `H7349` | ra.chum | compassionate | H | 103 love | `extracted` | 13 |
| `H7355` | ra.cham | to have compassion | H | 103 love | `extracted` | 43 |
| `H7356A` | ra.cham | womb | H | 23 compassion | `extracted` | 5 |
| `H7356B` | ra.cha.mim | compassion | H | 103 love | `extracted` | 39 |
| `H7358` | re.chem | womb | H | 23 compassion | `extracted` | 25 |
| `H7362` | ra.cha.ma.ni | compassionate | H | 23 compassion | `extracted_thin` | 1 |
| `H8469` | ta.cha.nun | supplication | H | 68 grace | `extracted_thin` | 18 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H2603A` — 1 groups

- **`984-001`** — 71 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the act of being gracious or showing favour — God's inner disposition of grace toward the supplicant, and the human cry that turns to God in petition and dependence*

### `H2604` — 1 groups

- **`989-001`** — 2 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names mercy shown in moral action and the plea of prayer — the practice of mercy toward the oppressed and the inner posture of petition before God*

### `H3722A` — 3 groups

- **`3169-001`** — 60 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the priestly/ritual act by which human guilt is covered before God and forgiveness granted — atonement as the mechanism addressing the person's moral condition*
- **`3169-002`** — 12 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's direct act of forgiving and covering iniquity — atonement as divine grace beyond or fulfilling the ritual mechanism*
- **`3169-003`** — 9 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names interpersonal or communal appeasement — covering relational offence or bloodguilt between persons or before God on communal grounds*

### `H3722B` — 3 groups

- **`3173-001`** — 60 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the priestly/ritual act by which human guilt is covered before God and forgiveness granted*
- **`3173-002`** — 12 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's direct act of forgiving and covering iniquity*
- **`3173-003`** — 9 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names interpersonal or communal appeasement — covering relational offence or bloodguilt*

### `H3724A` — 2 groups

- **`3170-001`** — 10 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names a substitutionary price paid for a life — ransom as the means by which moral accountability for life is addressed before God or human authority*
- **`3170-002`** — 3 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names illicit payment that corrupts the inner moral vision of the recipient — a bribe that blinds or deflects justice*

### `H3725` — 1 groups

- **`3171-001`** — 8 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the formal atonement institution — the Day of Atonement and its offerings — as the sacred structure addressing Israel's collective moral condition before God*

### `H3727` — 1 groups

- **`982-001`** — 22 relevant · 2 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C17`
  - *Term names the mercy seat as the physical locus of divine-human encounter — the point where God's presence meets human representation and atonement is effected*

### `H3819` — 1 groups

- **`986-001`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the prophetic withdrawal of divine compassion — the name embodies God's inner-being relational stance of withheld mercy toward a covenant-breaking people*

### `H5750` — 2 groups

- **`990-001`** — 7 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Persistence and turning — the duration of inner moral orientation, whether integrity maintained under affliction or stubbornness that must cease*
  - notes: Revised during Dimension Review Phase B.5: characteristic-perspective rewrite. Old: Term intensifies or marks the persistence/cessation of a human inner-being state — amplifying the force of an inner disposition or qualifying the duration of inner orientation
- **`990-002`** — 7 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term marks the ongoing or continuing character of a divine inner disposition — God's sustained relational stance toward a people*

### `H6279` — 2 groups

- **`987-001`** — 14 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the act of intercessory prayer — pleading with God on behalf of another's need or the removal of a burden from others*
- **`987-002`** — 5 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names personal prayer — the inner act of bringing one's own need, trust, or longing to God and receiving divine response*

### `H7359` — 1 groups

- **`988-001`** — 1 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names divine compassion as the ground of appeal — the inner-being disposition of God toward persons in extremity*

### `H8467` — 2 groups

- **`985-001`** — 21 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names supplication to God — the inner act of pleading for mercy, rooted in recognition of one's own need and God's disposition to hear and forgive*
- **`985-002`** — 3 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names supplication to human authority — the humble inner posture of plea before one with power over the supplicant's life or freedom*

### `G0415` — 1 groups

- **`3165-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names mercilessness as an inner character failure — one of the marks of those whose inner moral fabric has collapsed*

### `G0448` — 1 groups

- **`993-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names mercilessness as the inner orientation that forfeits mercy — and mercy as the disposition that triumphs over judgment*

### `G0462` — 1 groups

- **`3179-001`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names unholiness as an inner character disposition — among the catalogue of inner moral failures marking those outside covenant fidelity*

### `G1653` — 3 groups

- **`981-001`** — 12 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the act of divine mercy — God having mercy on whom he wills as the ground of salvation and sovereign grace*
- **`981-002`** — 11 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the cry for mercy — the supplicant's inner anguish and hope directed toward Jesus as healer and Saviour*
- **`981-003`** — 5 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the human act of mercy as the inner disposition that receives mercy in return*

### `G1655` — 1 groups

- **`3164-001`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names mercifulness as an inner character quality — the blessed disposition of those who show mercy and the defining character of Christ as high priest*

### `G1656` — 2 groups

- **`983-001`** — 14 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's mercy as his defining inner attribute — the ground of salvation, the content of covenant faithfulness, and the wellspring of new life*
- **`983-002`** — 13 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names mercy as the inner-being virtue and judicial reality — what God desires above ritual, what the wise show, what triumphs over judgment*

### `G2433` — 1 groups

- **`3176-001`** — 2 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the act of propitiation — the sinner's inner cry for God to turn his face in mercy, and Christ's atoning act that makes this possible*

### `G2434` — 1 groups

- **`3177-001`** — 2 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the propitiation — Christ as the atoning covering for sin that restores the inner relationship between God and the person*

### `G2435` — 1 groups

- **`991-001`** — 2 relevant · 2 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C17`
  - *Term names the mercy seat — the place of propitiation fulfilled in Christ as the living propitiation received by faith*

### `G2436` — 1 groups

- **`3166-001`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the propitious disposition of God — the mercy that forgives iniquity and remembers sin no more under the new covenant*

### `G3628` — 1 groups

- **`992-001`** — 5 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the compassions of God as his defining inner character — the mercies that motivate holy living and compassionate hearts as the inner garment of the new humanity*

### `G3629` — 1 groups

- **`3158-001`** — 2 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names compassion as the inner character of God and the standard for human inner disposition — to be merciful as God is merciful*

### `G3743` — 1 groups

- **`3181-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names devout holiness as an inner character quality — the holy conduct of the apostle as a witness to inner moral integrity*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 130 reconciliation | 9 | `H3727,G2435,G2436,H3722A,H3724A,H3725,H3722B,G2433,G2434` |
| 23 compassion | 7 | `G1653,G1656,H2603A,H8467,H7359,H2604,G3628` |
| 212 pray | 4 | `H2603A,H8467,H6279,H2604` |
| 68 grace | 2 | `H2603A,H8467` |
| 73 guilt | 2 | `H2603A,H8467` |
| 44 despair | 1 | `H3819` |
| 49 discernment | 1 | `H3819` |
| 103 love | 1 | `H7359` |
| 159 testimony | 1 | `H5750` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 73 guilt | 67 |
| 23 compassion | 34 |
| 64 forgiveness | 27 |
| 103 love | 26 |
| 197 authority | 24 |
| 125 purity | 21 |
| 182 Soul | 20 |
| 128 rebellion | 15 |
| 187 strength | 15 |
| 117 peace | 13 |
| 59 faith | 12 |
| 183 heart | 12 |
| 98 justice | 11 |
| 43 desire | 10 |
| 126 purpose | 10 |
| 196 power | 10 |
| 121 praise | 9 |
| 34 covenant | 8 |
| 57 evil | 8 |
| 90 innocence | 8 |
| 32 counsel | 7 |
| 112 mind | 7 |
| 135 repentance | 7 |
| 172 wickedness | 7 |
| 176 worship | 7 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 3 ambition | 2Ti 3:2 |
| 23 compassion | Jam 5:11 |
| 23 compassion | Num 6:25 |
| 23 compassion | Rom 9:15 |
| 31 corruption | Job 33:24 |
| 34 covenant | Rom 1:31 |
| 43 desire | Dan 6:11 |
| 64 forgiveness | Lev 4:20 |
| 66 gentleness | Jam 3:17 |
| 90 innocence | 1Sa 12:3 |
| 92 integrity | Job 2:3 |
| 99 kindness | Dan 2:18 |
| 103 love | 2Ti 3:2 |
| 103 love | Psa 78:38 |
| 112 mind | Heb 8:12 |
| 116 patience | Col 3:12 |
| 117 peace | Jam 3:17 |
| 123 pride | 2Ti 3:2 |
| 125 purity | Jam 3:17 |
| 182 Soul | Lev 23:27 |
| 183 heart | Col 3:12 |
| 183 heart | Luk 1:78 |
| 191 doubt | Jam 3:17 |
| 192 comfort | 2Cor 1:3 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-111-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-08 · **term_id:** -

> The atonement/propitiation vocabulary (kipper, kaphar, kapporet, hilasmos, hilastērios) within the mercy registry produces a cluster of Transformation/GOD groups where moral standing is transformed through atoning acts. Session B should examine the relationship between mercy as divine inner disposition (Relational Disposition/GOD) and atonement as its structural mechanism — how God's inner relational orientation of mercy is expressed in and through transformative acts that alter the person's standing.

### H.2 Open SD pointers + research flags (16)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `DIMREVIEW_SESSION_D` | DIM-111-SD000 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD005 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD006 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD007 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD008 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD009 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD010 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD011 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD012 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD013 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD014 | LOW | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD015 | LOW | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD001 | HIGH | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD002 | HIGH | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD003 | HIGH | D | 2026-04-11 |
| `SD_POINTER` | DIM-111-SD004 | HIGH | D | 2026-04-11 |

#### DIM-111-SD000

> Reg 111 (mercy) contains a structural polarity that parallels but differs from the forgiveness polarity in Reg 64. Here the polarity is: the mercy seat (982-001 — the physical locus of divine-human meeting in mercy) at one end, and No Mercy (986-001 — the prophetic name embodying withdrawn mercy) at the other. Between these poles, the registry maps the full range of the mercy-atonement complex: divine compassion, priestly atonement, propitiatory cries, supplication, and human mercy. Session D should examine whether this polarity — the mercy seat as the locus of mercy granted, and No Mercy as the embodiment of mercy withdrawn — encodes the fundamental structure of the divine-human relationship as mercy-constituted: the human person stands before God at the mercy seat or faces the No Mercy verdict. No neutral ground exists. This may connect to the forgiveness polarity in Reg 64 (absolute forgiveness vs. permanent non-forgiveness) as a structural feature of C17 more broadly.

#### DIM-111-SD005

> H5750 od names sustained divine dispositions in opposite directions: mercy endures (Hab 2:3); anger stretched out still (Isa 5:25). Do mercy and wrath share persistence structure as expressions of divine faithfulness? Session D.

#### DIM-111-SD006

> Eze 16:63: shame as inner experience of receiving comprehensive mercy for the unforgivable. Mercy-induced shame distinct from judgment-shame. Session D to examine with Reg 146 (shame).

#### DIM-111-SD007

> 2Ch 33:13: Niphal of a.tar for both prayer and divine response. Same root names human act and divine inner movement. Theology of divine responsiveness. Session D to examine across prayer and mercy registries.

#### DIM-111-SD008

> 2Cor 1:3: Father of mercies + God of all comfort. Is comfort the pastoral output of received mercy? Mercy-comfort-Spirit triangle. Session D.

#### DIM-111-SD009

> Blood as dominant somatic element in atonement sub-vocabulary. Lev 17:11: life of flesh in blood, blood makes atonement for soul. Mercy-through-blood mechanism. Session D with Reg 185 (flesh).

#### DIM-111-SD010

> 1Ki 8:38: knowing affliction of own heart as supplication prerequisite. Self-knowledge as structural feature of authentic mercy-seeking. Session D.

#### DIM-111-SD011

> Job 2:3: chinnam (H2600, from cha.nan root) -- gratuitous suffering and gratuitous grace share the same root. Structural relationship between unmerited suffering and unmerited favour. Session D.

#### DIM-111-SD012

> Rom 3:25: Christ as hilasterios to be received by faith. Faith as mode of accessing mercy seat. Session D to examine faith-mercy-seat connection across Reg 59 and Reg 111.

#### DIM-111-SD013

> Reg 117 (peace) shares 3 dimensions with mercy. Isa 54:10: covenant of peace alongside steadfast love/mercy. Is peace the relational state mercy produces? Session D.

#### DIM-111-SD014

> Exo 25:22: from above mercy seat I will speak with you. Mercy seat as locus of divine communication. Does mercy provide structural ground for divine-human communication? Session D.

#### DIM-111-SD015

> Reg 179 (yearning), 43 (desire), 42 (delight) share terms with mercy via H2550 chamad root covering both desire and pity. Is mercy related to longing? Session D.

#### DIM-111-SD001

> Strength/power/authority/dominion registries (Reg 187/196/197/198/199) share all 4 of mercy dimensions. Structural question: is mercy the moral direction of power toward the vulnerable? Session D to examine whether power and mercy form a structural inner-being pair.

#### DIM-111-SD002

> Reg 73 (guilt) shares 9 terms with mercy -- primarily supplication vocabulary. Guilt as inner condition generating authentic mercy-seeking. Dan 9:20, Luk 18:13, Psa 51:1. Session D to examine the guilt-mercy sequence.

#### DIM-111-SD003

> Jam 2:13 and Mat 23:23 encode mercy-justice structural relationship. Mercy triumphing over judgment. Justice, mercy, faithfulness as weightier matters of the law. Session D to examine mercy-justice-faithfulness cluster.

#### DIM-111-SD004

> 1Jo 4:10: divine love -> sending of Son -> propitiation -> mercy received. Eph 2:4: God rich in mercy because of great love. Structural question: is mercy a form of love (love toward the undeserving)? Session D.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `H2603A` (4 flag(s))

- **`THIN_DATA`** — Fewer verse occurrences than expected; analysis may be limited
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`VERSE_EVIDENCE_CONCENTRATED`** — Term has fewer than 20 confirmed verse records (threshold from THIN_DATA_THRESHOLD). Merged: incorporates prior THIN_DATA semantic. Informational — verse count does not indicate analytical value. Research actions: investigate STEP capture completeness + AI wider-context exploration.
  - Face/eye/soul/fasting/weeping -- grace mediated through face-direction (Num 6:25), sought through bodily self-denial (2Sa 12:22, Isa 30:19).
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11
- **`NO_WORD_ANALYSIS`** — No word-level analysis is available for this term
  - Fasting/weeping as bodily expression of mercy-seeking inner state (2Sa 12:22, Isa 30:19). H2603A receives both SOMATIC_INNER_LINK and BODY_INNER_EXPRESSION.
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11
- **`22`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `H3722A` (1 flag(s))

- **`VERSE_EVIDENCE_CONCENTRATED`** — Term has fewer than 20 confirmed verse records (threshold from THIN_DATA_THRESHOLD). Merged: incorporates prior THIN_DATA semantic. Informational — verse count does not indicate analytical value. Research actions: investigate STEP capture completeness + AI wider-context exploration.
  - Blood/hand/soul/face -- body is instrument and recipient of atoning act. Lev 17:11 (blood-for-soul), Lev 1:4 (laying on of hand), Gen 32:20 (cover the face).
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11

### `H3727` (2 flag(s))

- **`VERSE_EVIDENCE_CONCENTRATED`** — Term has fewer than 20 confirmed verse records (threshold from THIN_DATA_THRESHOLD). Merged: incorporates prior THIN_DATA semantic. Informational — verse count does not indicate analytical value. Research actions: investigate STEP capture completeness + AI wider-context exploration.
  - Blood/face -- blood sprinkled on mercy seat (Lev 16:14); cherubim faces overshadowing (Exo 25:20). Body and its products are the ritual instrument.
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11
- **`13`** — None
  - Divine-human relationship directly shapes spirit-soul-body classification for this term.
  - source: Session B v4.7 Pass 2 · raised: 2026-04-11

### `H5750` (1 flag(s))

- **`6`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `H6279` (1 flag(s))

- **`THIN_DATA`** — Fewer verse occurrences than expected; analysis may be limited
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `H8467` (2 flag(s))

- **`VERSE_EVIDENCE_CONCENTRATED`** — Term has fewer than 20 confirmed verse records (threshold from THIN_DATA_THRESHOLD). Merged: incorporates prior THIN_DATA semantic. Informational — verse count does not indicate analytical value. Research actions: investigate STEP capture completeness + AI wider-context exploration.
  - Heart/hand/eyes -- supplication posture: knowing affliction of heart (1Ki 8:38), stretched hands toward temple, eyes open to plea (1Ki 8:52).
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11
- **`NO_WORD_ANALYSIS`** — No word-level analysis is available for this term
  - Stretched hands (1Ki 8:38/54) as bodily expression of supplication inner posture. H8467 receives both SOMATIC_INNER_LINK and BODY_INNER_EXPRESSION.
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11

### `G1656` (3 flag(s))

- **`13`** — None
  - Divine-human relationship directly shapes spirit-soul-body classification for this term.
  - source: Session B v4.7 Pass 2 · raised: 2026-04-11
- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`22`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G2433` (2 flag(s))

- **`NO_WORD_ANALYSIS`** — No word-level analysis is available for this term
  - Eyes/breast/beating (Luk 18:13) -- tax collector enacts inner posture of total humility through three simultaneous somatic gestures: distance, downcast eyes, chest-beating.
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11
- **`13`** — None
  - Divine-human relationship directly shapes spirit-soul-body classification for this term.
  - source: Session B v4.7 Pass 2 · raised: 2026-04-11

### `G2434` (1 flag(s))

- **`13`** — None
  - Divine-human relationship directly shapes spirit-soul-body classification for this term.
  - source: Session B v4.7 Pass 2 · raised: 2026-04-11

### `G2435` (2 flag(s))

- **`13`** — None
  - Divine-human relationship directly shapes spirit-soul-body classification for this term.
  - source: Session B v4.7 Pass 2 · raised: 2026-04-11
- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G3628` (2 flag(s))

- **`NO_WORD_ANALYSIS`** — No word-level analysis is available for this term
  - Body/bodies (Rom 12:1) -- presenting bodies as response to oiktirmos of God; splagchna oiktirmou (Col 3:12) -- compassionate hearts as inner garment expressed through conduct.
  - source: Session B v4.7 Pass 4 · raised: 2026-04-11
- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H2603A` — 71/72 classified · 2 anchor verse(s)

**Group `984-001`** (71 verses — anchors: Num 6:25, Psa 51:1)

- **Num 6:25** 🔵 (✓) *target: gracious*
  > Num 6:25 the Lord make his face to shine upon you and be gracious to you ;
- **Psa 51:1** 🔵 (✓) *target: mercy*
  > To the choirmaster . A Psalm of David , when Nathan the prophet went to him, after he had gone in to Bathsheba . Psa 51:1 Have mercy on me, O God , according to your steadfast love ; according to your abundant mercy blot out my transgressions .
- **Gen 33:5** (✓) *target: graciously given*
  > Gen 33:5 And when Esau lifted up his eyes and saw the women and children , he said , “ Who are these with you?” Jacob said , “The children whom God has graciously given your servant .”
- **Gen 33:11** (✓) *target: graciously*
  > Gen 33:11 Please accept my blessing that is brought to you, because God has dealt graciously with me, and because I have enough .” Thus he urged him, and he took it.
- **Gen 42:21** (✓) *target: begged*
  > Gen 42:21 Then they said to one another , “In truth we are guilty concerning our brother , in that we saw the distress of his soul , when he begged us and we did not listen . That is why this distress has come upon us.”
- **Gen 43:29** (✓) *target: gracious*
  > Gen 43:29 And he lifted up his eyes and saw his brother Benjamin , his mother’s son , and said , “Is this your youngest brother , of whom you spoke to me? God be gracious to you, my son !”
- **Exo 33:19** (✓) *target: gracious*
  > Exo 33:19 And he said , “I will make all my goodness pass before you and will proclaim before you my name ‘The Lord .’ And I will be gracious to whom I will be gracious , and will show mercy on whom I will show mercy .
- **Deu 3:23** (✓) *target: pleaded*
  > Deu 3:23 “And I pleaded with the Lord at that time , saying ,
- **Deu 7:2** (✓) *target: mercy*
  > Deu 7:2 and when the Lord your God gives them over to you, and you defeat them, then you must devote them to complete destruction . You shall make no covenant with them and show no mercy to them .
- **Deu 28:50** (✓) *target: show mercy*
  > Deu 28:50 a hard-faced nation who shall not respect the old or show mercy to the young .
- **Judg 21:22** (✓) *target: graciously*
  > Judg 21:22 And when their fathers or their brothers come to complain to us, we will say to them, ‘Grant them graciously to us, because we did not take for each man of them his wife in battle , neither did you give them to them, else you would now be guilty .’”
- **2Sa 12:22** (✓) *target: gracious*
  > 2Sa 12:22 He said , “While the child was still alive , I fasted and wept , for I said , ‘ Who knows whether the Lord will be gracious to me, that the child may live ?’
- **1Ki 8:33** (✓) *target: plead*
  > 1Ki 8:33 “When your people Israel are defeated before the enemy because they have sinned against you, and if they turn again to you and acknowledge your name and pray and plead with you in this house ,
- **1Ki 8:47** (✓) *target: plead*
  > 1Ki 8:47 yet if they turn their heart in the land to which they have been carried captive , and repent and plead with you in the land of their captors , saying , ‘We have sinned and have acted perversely and wickedly ,’
- **1Ki 8:59** (✓) *target: pleaded*
  > 1Ki 8:59 Let these words of mine, with which I have pleaded before the Lord , be near to the Lord our God day and night , and may he maintain the cause of his servant and the cause of his people Israel , as each day requires ,
- **1Ki 9:3** (✓) *target: made*
  > 1Ki 9:3 And the Lord said to him, “I have heard your prayer and your plea , which you have made before me. I have consecrated this house that you have built , by putting my name there forever . My eyes and my heart will be there for all time .
- **2Ki 1:13** (✓) *target: entreated*
  > 2Ki 1:13 Again the king sent the captain of a third fifty with his fifty . And the third captain of fifty went up and came and fell on his knees before Elijah and entreated him, “O man of God , please let my life , and the life of these fifty servants of yours, be precious in your sight .
- **2Ki 13:23** (✓) *target: gracious*
  > 2Ki 13:23 But the Lord was gracious to them and had compassion on them, and he turned toward them, because of his covenant with Abraham , Isaac , and Jacob , and would not destroy them, nor has he cast them from his presence until now .
- **2Ch 6:24** (✓) *target: plead*
  > 2Ch 6:24 “ If your people Israel are defeated before the enemy because they have sinned against you, and they turn again and acknowledge your name and pray and plead with you in this house ,
- **2Ch 6:37** (✓) *target: plead*
  > 2Ch 6:37 yet if they turn their heart in the land to which they have been carried captive , and repent and plead with you in the land of their captivity , saying , ‘We have sinned and have acted perversely and wickedly ,’
- **Est 8:3** (✓) *target: pleaded*
  > Est 8:3 Then Esther spoke again to the king . She fell at his feet and wept and pleaded with him to avert the evil plan of Haman the Agagite and the plot that he had devised against the Jews .
- **Job 8:5** (✓) *target: plead*
  > Job 8:5 If you will seek God and plead with the Almighty for mercy,
- **Job 9:15** (✓) *target: mercy*
  > Job 9:15 Though I am in the right , I cannot answer him; I must appeal for mercy to my accuser .
- **Job 19:16** (✓) *target: must plead*
  > Job 19:16 I call to my servant , but he gives me no answer ; I must plead with him with my mouth for mercy.
- **Job 19:21** (✓) *target: mercy*
  > Job 19:21 Have mercy on me, have mercy on me, O you my friends , for the hand of God has touched me !
- **Job 33:24** (✓) *target: merciful*
  > Job 33:24 and he is merciful to him, and says , ‘ Deliver him from going down into the pit ; I have found a ransom ;
- **Psa 4:1** (✓) *target: gracious*
  > To the choirmaster : with stringed instruments . A Psalm of David . Psa 4:1 Answer me when I call , O God of my righteousness ! You have given me relief when I was in distress . Be gracious to me and hear my prayer !
- **Psa 6:2** (✓) *target: gracious*
  > Psa 6:2 Be gracious to me, O Lord , for I am languishing ; heal me, O Lord , for my bones are troubled .
- **Psa 9:13** (✓) *target: gracious*
  > Psa 9:13 Be gracious to me, O Lord ! See my affliction from those who hate me, O you who lift me up from the gates of death ,
- **Psa 25:16** (✓) *target: gracious*
  > Psa 25:16 Turn to me and be gracious to me, for I am lonely and afflicted .
- **Psa 26:11** (✓) *target: gracious*
  > Psa 26:11 But as for me , I shall walk in my integrity ; redeem me, and be gracious to me .
- **Psa 27:7** (✓) *target: gracious*
  > Psa 27:7 Hear , O Lord , when I cry aloud ; be gracious to me and answer me !
- **Psa 30:8** (✓) *target: plead*
  > Psa 30:8 To you, O Lord , I cry , and to the Lord I plead for mercy:
- **Psa 30:10** (✓) *target: merciful*
  > Psa 30:10 Hear , O Lord , and be merciful to me! O Lord , be my helper !”
- **Psa 31:9** (✓) *target: gracious*
  > Psa 31:9 Be gracious to me, O Lord , for I am in distress ; my eye is wasted from grief ; my soul and my body also.
- **Psa 37:21** (✓) *target: generous*
  > Psa 37:21 The wicked borrows but does not pay back, but the righteous is generous and gives ;
- **Psa 37:26** (✓) *target: generously*
  > Psa 37:26 He is ever lending generously , and his children become a blessing .
- **Psa 41:4** (✓) *target: gracious*
  > Psa 41:4 As for me , I said , “O Lord , be gracious to me; heal me , for I have sinned against you !”
- **Psa 41:10** (✓) *target: gracious*
  > Psa 41:10 But you , O Lord , be gracious to me, and raise me up, that I may repay them !
- **Psa 56:1** (✓) *target: gracious*
  > To the choirmaster : according to The Dove on Far-off Terebinths . A Miktam of David , when the Philistines seized him in Gath . Psa 56:1 Be gracious to me, O God , for man tramples on me; all day long an attacker oppresses me ;
- **Psa 57:1** (✓) *target: merciful*
  > To the choirmaster : according to Do Not Destroy . A Miktam of David , when he fled from Saul , in the cave . Psa 57:1 Be merciful to me, O God , be merciful to me, for in you my soul takes refuge ; in the shadow of your wings I will take refuge , till the storms of destruction pass by .
- **Psa 59:5** (✓) *target: spare*
  > Psa 59:5 You , Lord God of hosts , are God of Israel . Rouse yourself to punish all the nations ; spare none of those who treacherously plot evil . Selah
- **Psa 67:1** (✓) *target: gracious*
  > To the choirmaster : with stringed instruments . A Psalm . A Song . Psa 67:1 May God be gracious to us and bless us and make his face to shine upon us, Selah
- **Psa 77:9** (✓) *target: gracious*
  > Psa 77:9 Has God forgotten to be gracious ? Has he in anger shut up his compassion ?” Selah
- **Psa 86:3** (✓) *target: gracious*
  > Psa 86:3 Be gracious to me, O Lord , for to you do I cry all the day .
- **Psa 86:16** (✓) *target: gracious*
  > Psa 86:16 Turn to me and be gracious to me; give your strength to your servant , and save the son of your maidservant .
- **Psa 102:13** (✓) *target: favor*
  > Psa 102:13 You will arise and have pity on Zion ; it is the time to favor her; the appointed time has come .
- **Psa 102:14** (✓) *target: pity*
  > Psa 102:14 For your servants hold her stones dear and have pity on her dust .
- **Psa 109:12** (✓) *target: pity*
  > Psa 109:12 Let there be none to extend kindness to him, nor any to pity his fatherless children !
- **Psa 112:5** (✓) *target: deals generously*
  > Psa 112:5 It is well with the man who deals generously and lends ; who conducts his affairs with justice .
- **Psa 119:29** (✓) *target: graciously*
  > Psa 119:29 Put false ways far from me and graciously teach me your law !
- **Psa 119:58** (✓) *target: gracious*
  > Psa 119:58 I entreat your favor with all my heart ; be gracious to me according to your promise .
- **Psa 119:132** (✓) *target: gracious*
  > Psa 119:132 Turn to me and be gracious to me, as is your way with those who love your name .
- **Psa 123:2** (✓) *target: mercy*
  > Psa 123:2 Behold , as the eyes of servants look to the hand of their master , as the eyes of a maidservant to the hand of her mistress , so our eyes look to the Lord our God , till he has mercy upon us .
- **Psa 123:3** (✓) *target: mercy*
  > Psa 123:3 Have mercy upon us, O Lord , have mercy upon us, for we have had more than enough of contempt .
- **Psa 142:1** (✓) *target: mercy*
  > A Maskil of David , when he was in the cave . A Prayer . Psa 142:1 With my voice I cry out to the Lord ; with my voice I plead for mercy to the Lord .
- **Pro 14:21** (✓) *target: generous*
  > Pro 14:21 Whoever despises his neighbor is a sinner , but blessed is he who is generous to the poor .
- **Pro 14:31** (✓) *target: generous*
  > Pro 14:31 Whoever oppresses a poor man insults his Maker , but he who is generous to the needy honors him.
- **Pro 19:17** (✓) *target: generous*
  > Pro 19:17 Whoever is generous to the poor lends to the Lord , and he will repay him for his deed .
- **Pro 21:10** (✓) *target: mercy*
  > Pro 21:10 The soul of the wicked desires evil ; his neighbor finds no mercy in his eyes .
- **Pro 26:25** (✓) *target: graciously*
  > Pro 26:25 when he speaks graciously , believe him not , for there are seven abominations in his heart ;
- **Pro 28:8** (✓) *target: generous*
  > Pro 28:8 Whoever multiplies his wealth by interest and profit gathers it for him who is generous to the poor .
- **Isa 26:10** (✓) *target: shown*
  > Isa 26:10 If favor is shown to the wicked , he does not learn righteousness ; in the land of uprightness he deals corruptly and does not see the majesty of the Lord .
- **Isa 27:11** (✓) *target: favor*
  > Isa 27:11 When its boughs are dry , they are broken ; women come and make a fire of them. For this is a people without discernment ; therefore he who made them will not have compassion on them; he who formed them will show them no favor .
- **Isa 30:18** (✓) *target: gracious*
  > Isa 30:18 Therefore the Lord waits to be gracious to you, and therefore he exalts himself to show mercy to you. For the Lord is a God of justice ; blessed are all those who wait for him .
- **Isa 30:19** (✓) *target: surely*
  > Isa 30:19 For a people shall dwell in Zion , in Jerusalem ; you shall weep no more . He will surely be gracious to you at the sound of your cry . As soon as he hears it, he answers you .
- **Isa 33:2** (✓) *target: gracious*
  > Isa 33:2 O Lord , be gracious to us; we wait for you. Be our arm every morning , our salvation in the time of trouble .
- **Lam 4:16** (✓) *target: favor*
  > Lam 4:16 The Lord himself has scattered them; he will regard them no more ; no honor was shown to the priests , no favor to the elders .
- **Hos 12:4** (✓) *target: favor*
  > Hos 12:4 He strove with the angel and prevailed ; he wept and sought his favor . He met God at Bethel , and there God spoke with us —
- **Amo 5:15** (✓) *target: gracious*
  > Amo 5:15 Hate evil , and love good , and establish justice in the gate ; it may be that the Lord , the God of hosts , will be gracious to the remnant of Joseph .
- **Mal 1:9** (✓) *target: gracious*
  > Mal 1:9 And now entreat the favor of God , that he may be gracious to us. With such a gift from your hand , will he show favor to any of you? says the Lord of hosts .

**Group `UNCLASSIFIED`** (1 verse)

- **Est 4:8** (—) *target: favor*
  > Est 4:8 Mordecai also gave him a copy of the written decree issued in Susa for their destruction , that he might show it to Esther and explain it to her and command her to go to the king to beg his favor and plead with him on behalf of her people .

### `H2604` — 2/2 classified · 2 anchor verse(s)

**Group `989-001`** (2 verses — anchors: Dan 4:27, Dan 6:11)

- **Dan 4:27** 🔵 (✓) *target: showing mercy*
  > Dan 4:27 Therefore , O king , let my counsel be acceptable to you : break off your sins by practicing righteousness , and your iniquities by showing mercy to the oppressed , that there may perhaps be a lengthening of your prosperity .”
- **Dan 6:11** 🔵 (✓) *target: plea*
  > Dan 6:11 Then these men came by agreement and found Daniel making petition and plea before his God .

### `H3722A` — 81/93 classified · 6 anchor verse(s)

**Group `3169-001`** (60 verses — anchors: Lev 4:20, Lev 17:11)

- **Lev 4:20** 🔵 (✓) *target: make atonement*
  > Lev 4:20 Thus shall he do with the bull . As he did with the bull of the sin offering , so shall he do with this. And the priest shall make atonement for them , and they shall be forgiven .
- **Lev 17:11** 🔵 (✓) *target: make atonement*
  > Lev 17:11 For the life of the flesh is in the blood , and I have given it for you on the altar to make atonement for your souls , for it is the blood that makes atonement by the life .
- **Exo 29:33** (✓) *target: atonement*
  > Exo 29:33 They shall eat those things with which atonement was made at their ordination and consecration , but an outsider shall not eat of them, because they are holy .
- **Exo 30:15** (✓) *target: make atonement*
  > Exo 30:15 The rich shall not give more , and the poor shall not give less , than the half shekel , when you give the Lord’s offering to make atonement for your lives .
- **Exo 30:16** (✓) *target: make atonement*
  > Exo 30:16 You shall take the atonement money from the people of Israel and shall give it for the service of the tent of meeting , that it may bring the people of Israel to remembrance before the Lord , so as to make atonement for your lives .”
- **Lev 1:4** (✓) *target: make atonement*
  > Lev 1:4 He shall lay his hand on the head of the burnt offering , and it shall be accepted for him to make atonement for him .
- **Lev 4:26** (✓) *target: make atonement*
  > Lev 4:26 And all its fat he shall burn on the altar , like the fat of the sacrifice of peace offerings . So the priest shall make atonement for him for his sin , and he shall be forgiven .
- **Lev 4:31** (✓) *target: make atonement*
  > Lev 4:31 And all its fat he shall remove , as the fat is removed from the peace offerings , and the priest shall burn it on the altar for a pleasing aroma to the Lord . And the priest shall make atonement for him, and he shall be forgiven .
- **Lev 4:35** (✓) *target: make atonement*
  > Lev 4:35 And all its fat he shall remove as the fat of the lamb is removed from the sacrifice of peace offerings , and the priest shall burn it on the altar , on top of the Lord’s food offerings . And the priest shall make atonement for him for the sin which he has committed , and he shall be forgiven .
- **Lev 5:6** (✓) *target: make atonement*
  > Lev 5:6 he shall bring to the Lord as his compensation for the sin that he has committed , a female from the flock , a lamb or a goat , for a sin offering . And the priest shall make atonement for him for his sin .
- **Lev 5:10** (✓) *target: make atonement*
  > Lev 5:10 Then he shall offer the second for a burnt offering according to the rule . And the priest shall make atonement for him for the sin that he has committed , and he shall be forgiven .
- **Lev 5:13** (✓) *target: make atonement*
  > Lev 5:13 Thus the priest shall make atonement for him for the sin which he has committed in any one of these things, and he shall be forgiven . And the remainder shall be for the priest , as in the grain offering .”
- **Lev 5:16** (✓) *target: make atonement*
  > Lev 5:16 He shall also make restitution for what he has done amiss in the holy thing and shall add a fifth to it and give it to the priest . And the priest shall make atonement for him with the ram of the guilt offering , and he shall be forgiven .
- **Lev 5:18** (✓) *target: make atonement*
  > Lev 5:18 He shall bring to the priest a ram without blemish out of the flock , or its equivalent , for a guilt offering , and the priest shall make atonement for him for the mistake that he made unintentionally , and he shall be forgiven .
- **Lev 6:7** (✓) *target: make atonement*
  > Lev 6:7 And the priest shall make atonement for him before the Lord , and he shall be forgiven for any of the things that one may do and thereby become guilty.”
- **Lev 6:30** (✓) *target: make atonement*
  > Lev 6:30 But no sin offering shall be eaten from which any blood is brought into the tent of meeting to make atonement in the Holy Place ; it shall be burned up with fire .
- **Lev 7:7** (✓) *target: atonement*
  > Lev 7:7 The guilt offering is just like the sin offering ; there is one law for them. The priest who makes atonement with it shall have it .
- **Lev 8:34** (✓) *target: make atonement*
  > Lev 8:34 As has been done today , the Lord has commanded to be done to make atonement for you .
- **Lev 9:7** (✓) *target: make atonement*
  > Lev 9:7 Then Moses said to Aaron , “Draw near to the altar and offer your sin offering and your burnt offering and make atonement for yourself and for the people , and bring the offering of the people and make atonement for them , as the Lord has commanded .”
- **Lev 10:17** (✓) *target: make atonement*
  > Lev 10:17 “ Why have you not eaten the sin offering in the place of the sanctuary, since it is a thing most holy and has been given to you that you may bear the iniquity of the congregation , to make atonement for them before the Lord ?
- **Lev 12:7** (✓) *target: make atonement*
  > Lev 12:7 and he shall offer it before the Lord and make atonement for her. Then she shall be clean from the flow of her blood . This is the law for her who bears a child, either male or female .
- **Lev 12:8** (✓) *target: make atonement*
  > Lev 12:8 And if she cannot afford a lamb , then she shall take two turtledoves or two pigeons , one for a burnt offering and the other for a sin offering . And the priest shall make atonement for her, and she shall be clean .”
- **Lev 14:18** (✓) *target: make atonement*
  > Lev 14:18 And the rest of the oil that is in the priest’s hand he shall put on the head of him who is to be cleansed . Then the priest shall make atonement for him before the Lord .
- **Lev 14:19** (✓) *target: make atonement*
  > Lev 14:19 The priest shall offer the sin offering , to make atonement for him who is to be cleansed from his uncleanness . And afterward he shall kill the burnt offering .
- **Lev 14:20** (✓) *target: make atonement*
  > Lev 14:20 And the priest shall offer the burnt offering and the grain offering on the altar . Thus the priest shall make atonement for him, and he shall be clean .
- **Lev 14:21** (✓) *target: make atonement*
  > Lev 14:21 “But if he is poor and cannot afford so much , then he shall take one male lamb for a guilt offering to be waved , to make atonement for him, and a tenth of an ephah of fine flour mixed with oil for a grain offering , and a log of oil ;
- **Lev 14:29** (✓) *target: make atonement*
  > Lev 14:29 And the rest of the oil that is in the priest’s hand he shall put on the head of him who is to be cleansed , to make atonement for him before the Lord .
- **Lev 14:31** (✓) *target: make atonement*
  > Lev 14:31 one for a sin offering and the other for a burnt offering , along with a grain offering . And the priest shall make atonement before the Lord for him who is being cleansed .
- **Lev 15:15** (✓) *target: make atonement*
  > Lev 15:15 And the priest shall use them, one for a sin offering and the other for a burnt offering . And the priest shall make atonement for him before the Lord for his discharge .
- **Lev 15:30** (✓) *target: make atonement*
  > Lev 15:30 And the priest shall use one for a sin offering and the other for a burnt offering . And the priest shall make atonement for her before the Lord for her unclean discharge .
- **Lev 16:6** (✓) *target: make atonement*
  > Lev 16:6 “ Aaron shall offer the bull as a sin offering for himself and shall make atonement for himself and for his house .
- **Lev 16:10** (✓) *target: make atonement*
  > Lev 16:10 but the goat on which the lot fell for Azazel shall be presented alive before the Lord to make atonement over it, that it may be sent away into the wilderness to Azazel .
- **Lev 16:11** (✓) *target: make atonement*
  > Lev 16:11 “ Aaron shall present the bull as a sin offering for himself, and shall make atonement for himself and for his house . He shall kill the bull as a sin offering for himself .
- **Lev 16:16** (✓) *target: make atonement*
  > Lev 16:16 Thus he shall make atonement for the Holy Place , because of the uncleannesses of the people of Israel and because of their transgressions , all their sins . And so he shall do for the tent of meeting , which dwells with them in the midst of their uncleannesses .
- **Lev 16:17** (✓) *target: make atonement*
  > Lev 16:17 No one may be in the tent of meeting from the time he enters to make atonement in the Holy Place until he comes out and has made atonement for himself and for his house and for all the assembly of Israel .
- **Lev 16:24** (✓) *target: make atonement*
  > Lev 16:24 And he shall bathe his body in water in a holy place and put on his garments and come out and offer his burnt offering and the burnt offering of the people and make atonement for himself and for the people .
- **Lev 16:30** (✓) *target: atonement*
  > Lev 16:30 For on this day shall atonement be made for you to cleanse you. You shall be clean before the Lord from all your sins .
- **Lev 16:32** (✓) *target: make atonement*
  > Lev 16:32 And the priest who is anointed and consecrated as priest in his father’s place shall make atonement , wearing the holy linen garments .
- **Lev 16:33** (✓) *target: make atonement*
  > Lev 16:33 He shall make atonement for the holy sanctuary , and he shall make atonement for the tent of meeting and for the altar , and he shall make atonement for the priests and for all the people of the assembly .
- **Lev 16:34** (✓) *target: atonement*
  > Lev 16:34 And this shall be a statute forever for you, that atonement may be made for the people of Israel once in the year because of all their sins .” And Aaron did as the Lord commanded Moses .
- **Lev 19:22** (✓) *target: make atonement*
  > Lev 19:22 And the priest shall make atonement for him with the ram of the guilt offering before the Lord for his sin that he has committed , and he shall be forgiven for the sin that he has committed .
- **Lev 23:28** (✓) *target: make atonement*
  > Lev 23:28 And you shall not do any work on that very day , for it is a Day of Atonement , to make atonement for you before the Lord your God .
- **Num 5:8** (✓) *target: atonement*
  > Num 5:8 But if the man has no next of kin to whom restitution may be made for the wrong , the restitution for wrong shall go to the Lord for the priest , in addition to the ram of atonement with which atonement is made for him .
- **Num 6:11** (✓) *target: atonement*
  > Num 6:11 and the priest shall offer one for a sin offering and the other for a burnt offering , and make atonement for him, because he sinned by reason of the dead body . And he shall consecrate his head that same day
- **Num 8:12** (✓) *target: atonement*
  > Num 8:12 Then the Levites shall lay their hands on the heads of the bulls , and you shall offer the one for a sin offering and the other for a burnt offering to the Lord to make atonement for the Levites .
- **Num 8:19** (✓) *target: atonement*
  > Num 8:19 And I have given the Levites as a gift to Aaron and his sons from among the people of Israel , to do the service for the people of Israel at the tent of meeting and to make atonement for the people of Israel , that there may be no plague among the people of Israel when the people of Israel come near the sanctuary .”
- **Num 8:21** (✓) *target: atonement*
  > Num 8:21 And the Levites purified themselves from sin and washed their clothes , and Aaron offered them as a wave offering before the Lord , and Aaron made atonement for them to cleanse them .
- **Num 15:25** (✓) *target: atonement*
  > Num 15:25 And the priest shall make atonement for all the congregation of the people of Israel , and they shall be forgiven , because it was a mistake , and they have brought their offering , a food offering to the Lord , and their sin offering before the Lord for their mistake .
- **Num 15:28** (✓) *target: atonement*
  > Num 15:28 And the priest shall make atonement before the Lord for the person who makes a mistake , when he sins unintentionally , to make atonement for him , and he shall be forgiven .
- **Num 16:46** (✓) *target: atonement*
  > Num 16:46 And Moses said to Aaron , “ Take your censer , and put fire on it from off the altar and lay incense on it and carry it quickly to the congregation and make atonement for them, for wrath has gone out from the Lord ; the plague has begun .”
- **Num 16:47** (✓) *target: atonement*
  > Num 16:47 So Aaron took it as Moses said and ran into the midst of the assembly . And behold , the plague had already begun among the people . And he put on the incense and made atonement for the people .
- **Num 25:13** (✓) *target: atonement*
  > Num 25:13 and it shall be to him and to his descendants after him the covenant of a perpetual priesthood , because he was jealous for his God and made atonement for the people of Israel .’”
- **Num 28:22** (✓) *target: atonement*
  > Num 28:22 also one male goat for a sin offering , to make atonement for you .
- **Num 28:30** (✓) *target: atonement*
  > Num 28:30 with one male goat , to make atonement for you .
- **Num 29:5** (✓) *target: atonement*
  > Num 29:5 with one male goat for a sin offering , to make atonement for you ;
- **1Ch 6:49** (✓) *target: make atonement*
  > 1Ch 6:49 But Aaron and his sons made offerings on the altar of burnt offering and on the altar of incense for all the work of the Most Holy Place , and to make atonement for Israel , according to all that Moses the servant of God had commanded .
- **2Ch 29:24** (✓) *target: make atonement*
  > 2Ch 29:24 and the priests slaughtered them and made a sin offering with their blood on the altar , to make atonement for all Israel . For the king commanded that the burnt offering and the sin offering should be made for all Israel .
- **Neh 10:33** (✓) *target: make atonement*
  > Neh 10:33 for the showbread , the regular grain offering , the regular burnt offering , the Sabbaths , the new moons , the appointed feasts , the holy things , and the sin offerings to make atonement for Israel , and for all the work of the house of our God .
- **Eze 45:15** (✓) *target: make atonement*
  > Eze 45:15 And one sheep from every flock of two hundred , from the watering places of Israel for grain offering , burnt offering , and peace offerings , to make atonement for them, declares the Lord God .
- **Eze 45:17** (✓) *target: make atonement*
  > Eze 45:17 It shall be the prince’s duty to furnish the burnt offerings , grain offerings , and drink offerings , at the feasts , the new moons , and the Sabbaths , all the appointed feasts of the house of Israel : he shall provide the sin offerings , grain offerings , burnt offerings , and peace offerings , to make atonement on behalf of the house of Israel .

**Group `3169-002`** (12 verses — anchors: Psa 78:38, Eze 16:63)

- **Psa 78:38** 🔵 (✓) *target: atoned*
  > Psa 78:38 Yet he , being compassionate , atoned for their iniquity and did not destroy them; he restrained his anger often and did not stir up all his wrath .
- **Eze 16:63** 🔵 (✓) *target: atone*
  > Eze 16:63 that you may remember and be confounded , and never open your mouth again because of your shame , when I atone for you for all that you have done , declares the Lord God .”
- **Deu 32:43** (✓) *target: cleanses*
  > Deu 32:43 “ Rejoice with him, O heavens ; bow down to him, all gods, for he avenges the blood of his children and takes vengeance on his adversaries . He repays those who hate him and cleanses his people’s land .”
- **1Sa 3:14** (✓) *target: atoned*
  > 1Sa 3:14 Therefore I swear to the house of Eli that the iniquity of Eli’s house shall not be atoned for by sacrifice or offering forever .”
- **Psa 65:3** (✓) *target: atone*
  > Psa 65:3 When iniquities prevail against me, you atone for our transgressions .
- **Psa 79:9** (✓) *target: atone*
  > Psa 79:9 Help us, O God of our salvation , for the glory of your name ; deliver us, and atone for our sins , for your name’s sake!
- **Pro 16:6** (✓) *target: atoned for*
  > Pro 16:6 By steadfast love and faithfulness iniquity is atoned for , and by the fear of the Lord one turns away from evil .
- **Isa 6:7** (✓) *target: atoned for*
  > Isa 6:7 And he touched my mouth and said : “ Behold , this has touched your lips ; your guilt is taken away , and your sin atoned for .”
- **Isa 22:14** (✓) *target: atoned*
  > Isa 22:14 The Lord of hosts has revealed himself in my ears : “Surely this iniquity will not be atoned for you until you die ,” says the Lord God of hosts .
- **Isa 27:9** (✓) *target: atoned*
  > Isa 27:9 Therefore by this the guilt of Jacob will be atoned for, and this will be the full fruit of the removal of his sin : when he makes all the stones of the altars like chalkstones crushed to pieces , no Asherim or incense altars will remain standing .
- **Isa 47:11** (✓) *target: atone*
  > Isa 47:11 But evil shall come upon you, which you will not know how to charm away ; disaster shall fall upon you, for which you will not be able to atone ; and ruin shall come upon you suddenly , of which you know nothing .
- **Dan 9:24** (✓) *target: atone*
  > Dan 9:24 “ Seventy weeks are decreed about your people and your holy city , to finish the transgression , to put an end to sin , and to atone for iniquity , to bring in everlasting righteousness , to seal both vision and prophet , and to anoint a most holy place .

**Group `3169-003`** (9 verses — anchors: Gen 32:20, Deu 21:8)

- **Gen 32:20** 🔵 (✓) *target: appease*
  > Gen 32:20 and you shall say , ‘ Moreover , your servant Jacob is behind us .’” For he thought , “I may appease him with the present that goes ahead of me , and afterward I shall see his face . Perhaps he will accept me .”
- **Deu 21:8** 🔵 (✓) *target: atonement*
  > Deu 21:8 Accept atonement , O Lord , for your people Israel , whom you have redeemed , and do not set the guilt of innocent blood in the midst of your people Israel , so that their blood guilt be atoned for.’
- **Exo 32:30** (✓) *target: make atonement*
  > Exo 32:30 The next day Moses said to the people , “ You have sinned a great sin . And now I will go up to the Lord ; perhaps I can make atonement for your sin .”
- **Num 31:50** (✓) *target: atonement*
  > Num 31:50 And we have brought the Lord’s offering , what each man found , articles of gold , armlets and bracelets , signet rings , earrings , and beads , to make atonement for ourselves before the Lord .”
- **2Sa 21:3** (✓) *target: make atonement*
  > 2Sa 21:3 And David said to the Gibeonites , “ What shall I do for you? And how shall I make atonement , that you may bless the heritage of the Lord ?”
- **2Ch 30:18** (✓) *target: pardon*
  > 2Ch 30:18 For a majority of the people , many of them from Ephraim , Manasseh , Issachar , and Zebulun , had not cleansed themselves, yet they ate the Passover otherwise than as prescribed . For Hezekiah had prayed for them, saying , “ May the good Lord pardon everyone
- **Pro 16:14** (✓) *target: appease*
  > Pro 16:14 A king’s wrath is a messenger of death , and a wise man will appease it .
- **Isa 28:18** (✓) *target: annulled*
  > Isa 28:18 Then your covenant with death will be annulled , and your agreement with Sheol will not stand ; when the overwhelming scourge passes through , you will be beaten down by it.
- **Jer 18:23** (✓) *target: Forgive*
  > Jer 18:23 Yet you , O Lord , know all their plotting to kill me. Forgive not their iniquity , nor blot out their sin from your sight . Let them be overthrown before you; deal with them in the time of your anger .

**Group `UNCLASSIFIED`** (12 verses)

- **Exo 29:36** (—) *target: make atonement*
  > Exo 29:36 and every day you shall offer a bull as a sin offering for atonement . Also you shall purify the altar , when you make atonement for it, and shall anoint it to consecrate it .
- **Exo 29:37** (—) *target: make atonement*
  > Exo 29:37 Seven days you shall make atonement for the altar and consecrate it, and the altar shall be most holy . Whatever touches the altar shall become holy .
- **Exo 30:10** (—) *target: make atonement*
  > Exo 30:10 Aaron shall make atonement on its horns once a year . With the blood of the sin offering of atonement he shall make atonement for it once in the year throughout your generations . It is most holy to the Lord .”
- **Lev 8:15** (—) *target: make atonement*
  > Lev 8:15 And he killed it, and Moses took the blood , and with his finger put it on the horns of the altar around it and purified the altar and poured out the blood at the base of the altar and consecrated it to make atonement for it .
- **Lev 14:53** (—) *target: make atonement*
  > Lev 14:53 And he shall let the live bird go out of the city into the open country . So he shall make atonement for the house , and it shall be clean .”
- **Lev 16:18** (—) *target: make atonement*
  > Lev 16:18 Then he shall go out to the altar that is before the Lord and make atonement for it, and shall take some of the blood of the bull and some of the blood of the goat , and put it on the horns of the altar all around .
- **Lev 16:20** (—) *target: atoning*
  > Lev 16:20 “And when he has made an end of atoning for the Holy Place and the tent of meeting and the altar , he shall present the live goat .
- **Lev 16:27** (—) *target: make atonement*
  > Lev 16:27 And the bull for the sin offering and the goat for the sin offering , whose blood was brought in to make atonement in the Holy Place , shall be carried outside the camp . Their skin and their flesh and their dung shall be burned up with fire .
- **Num 35:33** (—) *target: made*
  > Num 35:33 You shall not pollute the land in which you live, for blood pollutes the land , and no atonement can be made for the land for the blood that is shed in it, except by the blood of the one who shed it .
- **Eze 43:20** (—) *target: make atonement*
  > Eze 43:20 And you shall take some of its blood and put it on the four horns of the altar and on the four corners of the ledge and upon the rim all around . Thus you shall purify the altar and make atonement for it .
- **Eze 43:26** (—) *target: make atonement*
  > Eze 43:26 Seven days shall they make atonement for the altar and cleanse it, and so consecrate it.
- **Eze 45:20** (—) *target: make atonement*
  > Eze 45:20 You shall do the same on the seventh day of the month for anyone who has sinned through error or ignorance ; so you shall make atonement for the temple .

### `H3722B` — 81/93 classified · 6 anchor verse(s)

**Group `3173-001`** (60 verses — anchors: Lev 4:20, Lev 17:11)

- **Lev 4:20** 🔵 (✓) *target: make atonement*
  > Lev 4:20 Thus shall he do with the bull . As he did with the bull of the sin offering , so shall he do with this. And the priest shall make atonement for them , and they shall be forgiven .
- **Lev 17:11** 🔵 (✓) *target: make atonement*
  > Lev 17:11 For the life of the flesh is in the blood , and I have given it for you on the altar to make atonement for your souls , for it is the blood that makes atonement by the life .
- **Exo 29:33** (✓) *target: atonement*
  > Exo 29:33 They shall eat those things with which atonement was made at their ordination and consecration , but an outsider shall not eat of them, because they are holy .
- **Exo 30:15** (✓) *target: make atonement*
  > Exo 30:15 The rich shall not give more , and the poor shall not give less , than the half shekel , when you give the Lord’s offering to make atonement for your lives .
- **Exo 30:16** (✓) *target: make atonement*
  > Exo 30:16 You shall take the atonement money from the people of Israel and shall give it for the service of the tent of meeting , that it may bring the people of Israel to remembrance before the Lord , so as to make atonement for your lives .”
- **Lev 1:4** (✓) *target: make atonement*
  > Lev 1:4 He shall lay his hand on the head of the burnt offering , and it shall be accepted for him to make atonement for him .
- **Lev 4:26** (✓) *target: make atonement*
  > Lev 4:26 And all its fat he shall burn on the altar , like the fat of the sacrifice of peace offerings . So the priest shall make atonement for him for his sin , and he shall be forgiven .
- **Lev 4:31** (✓) *target: make atonement*
  > Lev 4:31 And all its fat he shall remove , as the fat is removed from the peace offerings , and the priest shall burn it on the altar for a pleasing aroma to the Lord . And the priest shall make atonement for him, and he shall be forgiven .
- **Lev 4:35** (✓) *target: make atonement*
  > Lev 4:35 And all its fat he shall remove as the fat of the lamb is removed from the sacrifice of peace offerings , and the priest shall burn it on the altar , on top of the Lord’s food offerings . And the priest shall make atonement for him for the sin which he has committed , and he shall be forgiven .
- **Lev 5:6** (✓) *target: make atonement*
  > Lev 5:6 he shall bring to the Lord as his compensation for the sin that he has committed , a female from the flock , a lamb or a goat , for a sin offering . And the priest shall make atonement for him for his sin .
- **Lev 5:10** (✓) *target: make atonement*
  > Lev 5:10 Then he shall offer the second for a burnt offering according to the rule . And the priest shall make atonement for him for the sin that he has committed , and he shall be forgiven .
- **Lev 5:13** (✓) *target: make atonement*
  > Lev 5:13 Thus the priest shall make atonement for him for the sin which he has committed in any one of these things, and he shall be forgiven . And the remainder shall be for the priest , as in the grain offering .”
- **Lev 5:16** (✓) *target: make atonement*
  > Lev 5:16 He shall also make restitution for what he has done amiss in the holy thing and shall add a fifth to it and give it to the priest . And the priest shall make atonement for him with the ram of the guilt offering , and he shall be forgiven .
- **Lev 5:18** (✓) *target: make atonement*
  > Lev 5:18 He shall bring to the priest a ram without blemish out of the flock , or its equivalent , for a guilt offering , and the priest shall make atonement for him for the mistake that he made unintentionally , and he shall be forgiven .
- **Lev 6:7** (✓) *target: make atonement*
  > Lev 6:7 And the priest shall make atonement for him before the Lord , and he shall be forgiven for any of the things that one may do and thereby become guilty.”
- **Lev 6:30** (✓) *target: make atonement*
  > Lev 6:30 But no sin offering shall be eaten from which any blood is brought into the tent of meeting to make atonement in the Holy Place ; it shall be burned up with fire .
- **Lev 7:7** (✓) *target: atonement*
  > Lev 7:7 The guilt offering is just like the sin offering ; there is one law for them. The priest who makes atonement with it shall have it .
- **Lev 8:34** (✓) *target: make atonement*
  > Lev 8:34 As has been done today , the Lord has commanded to be done to make atonement for you .
- **Lev 9:7** (✓) *target: make atonement*
  > Lev 9:7 Then Moses said to Aaron , “Draw near to the altar and offer your sin offering and your burnt offering and make atonement for yourself and for the people , and bring the offering of the people and make atonement for them , as the Lord has commanded .”
- **Lev 10:17** (✓) *target: make atonement*
  > Lev 10:17 “ Why have you not eaten the sin offering in the place of the sanctuary, since it is a thing most holy and has been given to you that you may bear the iniquity of the congregation , to make atonement for them before the Lord ?
- **Lev 12:7** (✓) *target: make atonement*
  > Lev 12:7 and he shall offer it before the Lord and make atonement for her. Then she shall be clean from the flow of her blood . This is the law for her who bears a child, either male or female .
- **Lev 12:8** (✓) *target: make atonement*
  > Lev 12:8 And if she cannot afford a lamb , then she shall take two turtledoves or two pigeons , one for a burnt offering and the other for a sin offering . And the priest shall make atonement for her, and she shall be clean .”
- **Lev 14:18** (✓) *target: make atonement*
  > Lev 14:18 And the rest of the oil that is in the priest’s hand he shall put on the head of him who is to be cleansed . Then the priest shall make atonement for him before the Lord .
- **Lev 14:19** (✓) *target: make atonement*
  > Lev 14:19 The priest shall offer the sin offering , to make atonement for him who is to be cleansed from his uncleanness . And afterward he shall kill the burnt offering .
- **Lev 14:20** (✓) *target: make atonement*
  > Lev 14:20 And the priest shall offer the burnt offering and the grain offering on the altar . Thus the priest shall make atonement for him, and he shall be clean .
- **Lev 14:21** (✓) *target: make atonement*
  > Lev 14:21 “But if he is poor and cannot afford so much , then he shall take one male lamb for a guilt offering to be waved , to make atonement for him, and a tenth of an ephah of fine flour mixed with oil for a grain offering , and a log of oil ;
- **Lev 14:29** (✓) *target: make atonement*
  > Lev 14:29 And the rest of the oil that is in the priest’s hand he shall put on the head of him who is to be cleansed , to make atonement for him before the Lord .
- **Lev 14:31** (✓) *target: make atonement*
  > Lev 14:31 one for a sin offering and the other for a burnt offering , along with a grain offering . And the priest shall make atonement before the Lord for him who is being cleansed .
- **Lev 15:15** (✓) *target: make atonement*
  > Lev 15:15 And the priest shall use them, one for a sin offering and the other for a burnt offering . And the priest shall make atonement for him before the Lord for his discharge .
- **Lev 15:30** (✓) *target: make atonement*
  > Lev 15:30 And the priest shall use one for a sin offering and the other for a burnt offering . And the priest shall make atonement for her before the Lord for her unclean discharge .
- **Lev 16:6** (✓) *target: make atonement*
  > Lev 16:6 “ Aaron shall offer the bull as a sin offering for himself and shall make atonement for himself and for his house .
- **Lev 16:10** (✓) *target: make atonement*
  > Lev 16:10 but the goat on which the lot fell for Azazel shall be presented alive before the Lord to make atonement over it, that it may be sent away into the wilderness to Azazel .
- **Lev 16:11** (✓) *target: make atonement*
  > Lev 16:11 “ Aaron shall present the bull as a sin offering for himself, and shall make atonement for himself and for his house . He shall kill the bull as a sin offering for himself .
- **Lev 16:16** (✓) *target: make atonement*
  > Lev 16:16 Thus he shall make atonement for the Holy Place , because of the uncleannesses of the people of Israel and because of their transgressions , all their sins . And so he shall do for the tent of meeting , which dwells with them in the midst of their uncleannesses .
- **Lev 16:17** (✓) *target: make atonement*
  > Lev 16:17 No one may be in the tent of meeting from the time he enters to make atonement in the Holy Place until he comes out and has made atonement for himself and for his house and for all the assembly of Israel .
- **Lev 16:24** (✓) *target: make atonement*
  > Lev 16:24 And he shall bathe his body in water in a holy place and put on his garments and come out and offer his burnt offering and the burnt offering of the people and make atonement for himself and for the people .
- **Lev 16:30** (✓) *target: atonement*
  > Lev 16:30 For on this day shall atonement be made for you to cleanse you. You shall be clean before the Lord from all your sins .
- **Lev 16:32** (✓) *target: make atonement*
  > Lev 16:32 And the priest who is anointed and consecrated as priest in his father’s place shall make atonement , wearing the holy linen garments .
- **Lev 16:33** (✓) *target: make atonement*
  > Lev 16:33 He shall make atonement for the holy sanctuary , and he shall make atonement for the tent of meeting and for the altar , and he shall make atonement for the priests and for all the people of the assembly .
- **Lev 16:34** (✓) *target: atonement*
  > Lev 16:34 And this shall be a statute forever for you, that atonement may be made for the people of Israel once in the year because of all their sins .” And Aaron did as the Lord commanded Moses .
- **Lev 19:22** (✓) *target: make atonement*
  > Lev 19:22 And the priest shall make atonement for him with the ram of the guilt offering before the Lord for his sin that he has committed , and he shall be forgiven for the sin that he has committed .
- **Lev 23:28** (✓) *target: make atonement*
  > Lev 23:28 And you shall not do any work on that very day , for it is a Day of Atonement , to make atonement for you before the Lord your God .
- **Num 5:8** (✓) *target: atonement*
  > Num 5:8 But if the man has no next of kin to whom restitution may be made for the wrong , the restitution for wrong shall go to the Lord for the priest , in addition to the ram of atonement with which atonement is made for him .
- **Num 6:11** (✓) *target: atonement*
  > Num 6:11 and the priest shall offer one for a sin offering and the other for a burnt offering , and make atonement for him, because he sinned by reason of the dead body . And he shall consecrate his head that same day
- **Num 8:12** (✓) *target: atonement*
  > Num 8:12 Then the Levites shall lay their hands on the heads of the bulls , and you shall offer the one for a sin offering and the other for a burnt offering to the Lord to make atonement for the Levites .
- **Num 8:19** (✓) *target: atonement*
  > Num 8:19 And I have given the Levites as a gift to Aaron and his sons from among the people of Israel , to do the service for the people of Israel at the tent of meeting and to make atonement for the people of Israel , that there may be no plague among the people of Israel when the people of Israel come near the sanctuary .”
- **Num 8:21** (✓) *target: atonement*
  > Num 8:21 And the Levites purified themselves from sin and washed their clothes , and Aaron offered them as a wave offering before the Lord , and Aaron made atonement for them to cleanse them .
- **Num 15:25** (✓) *target: atonement*
  > Num 15:25 And the priest shall make atonement for all the congregation of the people of Israel , and they shall be forgiven , because it was a mistake , and they have brought their offering , a food offering to the Lord , and their sin offering before the Lord for their mistake .
- **Num 15:28** (✓) *target: atonement*
  > Num 15:28 And the priest shall make atonement before the Lord for the person who makes a mistake , when he sins unintentionally , to make atonement for him , and he shall be forgiven .
- **Num 16:46** (✓) *target: atonement*
  > Num 16:46 And Moses said to Aaron , “ Take your censer , and put fire on it from off the altar and lay incense on it and carry it quickly to the congregation and make atonement for them, for wrath has gone out from the Lord ; the plague has begun .”
- **Num 16:47** (✓) *target: atonement*
  > Num 16:47 So Aaron took it as Moses said and ran into the midst of the assembly . And behold , the plague had already begun among the people . And he put on the incense and made atonement for the people .
- **Num 25:13** (✓) *target: atonement*
  > Num 25:13 and it shall be to him and to his descendants after him the covenant of a perpetual priesthood , because he was jealous for his God and made atonement for the people of Israel .’”
- **Num 28:22** (✓) *target: atonement*
  > Num 28:22 also one male goat for a sin offering , to make atonement for you .
- **Num 28:30** (✓) *target: atonement*
  > Num 28:30 with one male goat , to make atonement for you .
- **Num 29:5** (✓) *target: atonement*
  > Num 29:5 with one male goat for a sin offering , to make atonement for you ;
- **1Ch 6:49** (✓) *target: make atonement*
  > 1Ch 6:49 But Aaron and his sons made offerings on the altar of burnt offering and on the altar of incense for all the work of the Most Holy Place , and to make atonement for Israel , according to all that Moses the servant of God had commanded .
- **2Ch 29:24** (✓) *target: make atonement*
  > 2Ch 29:24 and the priests slaughtered them and made a sin offering with their blood on the altar , to make atonement for all Israel . For the king commanded that the burnt offering and the sin offering should be made for all Israel .
- **Neh 10:33** (✓) *target: make atonement*
  > Neh 10:33 for the showbread , the regular grain offering , the regular burnt offering , the Sabbaths , the new moons , the appointed feasts , the holy things , and the sin offerings to make atonement for Israel , and for all the work of the house of our God .
- **Eze 45:15** (✓) *target: make atonement*
  > Eze 45:15 And one sheep from every flock of two hundred , from the watering places of Israel for grain offering , burnt offering , and peace offerings , to make atonement for them, declares the Lord God .
- **Eze 45:17** (✓) *target: make atonement*
  > Eze 45:17 It shall be the prince’s duty to furnish the burnt offerings , grain offerings , and drink offerings , at the feasts , the new moons , and the Sabbaths , all the appointed feasts of the house of Israel : he shall provide the sin offerings , grain offerings , burnt offerings , and peace offerings , to make atonement on behalf of the house of Israel .

**Group `3173-002`** (12 verses — anchors: Psa 78:38, Eze 16:63)

- **Psa 78:38** 🔵 (✓) *target: atoned*
  > Psa 78:38 Yet he , being compassionate , atoned for their iniquity and did not destroy them; he restrained his anger often and did not stir up all his wrath .
- **Eze 16:63** 🔵 (✓) *target: atone*
  > Eze 16:63 that you may remember and be confounded , and never open your mouth again because of your shame , when I atone for you for all that you have done , declares the Lord God .”
- **Deu 32:43** (✓) *target: cleanses*
  > Deu 32:43 “ Rejoice with him, O heavens ; bow down to him, all gods, for he avenges the blood of his children and takes vengeance on his adversaries . He repays those who hate him and cleanses his people’s land .”
- **1Sa 3:14** (✓) *target: atoned*
  > 1Sa 3:14 Therefore I swear to the house of Eli that the iniquity of Eli’s house shall not be atoned for by sacrifice or offering forever .”
- **Psa 65:3** (✓) *target: atone*
  > Psa 65:3 When iniquities prevail against me, you atone for our transgressions .
- **Psa 79:9** (✓) *target: atone*
  > Psa 79:9 Help us, O God of our salvation , for the glory of your name ; deliver us, and atone for our sins , for your name’s sake!
- **Pro 16:6** (✓) *target: atoned for*
  > Pro 16:6 By steadfast love and faithfulness iniquity is atoned for , and by the fear of the Lord one turns away from evil .
- **Isa 6:7** (✓) *target: atoned for*
  > Isa 6:7 And he touched my mouth and said : “ Behold , this has touched your lips ; your guilt is taken away , and your sin atoned for .”
- **Isa 22:14** (✓) *target: atoned*
  > Isa 22:14 The Lord of hosts has revealed himself in my ears : “Surely this iniquity will not be atoned for you until you die ,” says the Lord God of hosts .
- **Isa 27:9** (✓) *target: atoned*
  > Isa 27:9 Therefore by this the guilt of Jacob will be atoned for, and this will be the full fruit of the removal of his sin : when he makes all the stones of the altars like chalkstones crushed to pieces , no Asherim or incense altars will remain standing .
- **Isa 47:11** (✓) *target: atone*
  > Isa 47:11 But evil shall come upon you, which you will not know how to charm away ; disaster shall fall upon you, for which you will not be able to atone ; and ruin shall come upon you suddenly , of which you know nothing .
- **Dan 9:24** (✓) *target: atone*
  > Dan 9:24 “ Seventy weeks are decreed about your people and your holy city , to finish the transgression , to put an end to sin , and to atone for iniquity , to bring in everlasting righteousness , to seal both vision and prophet , and to anoint a most holy place .

**Group `3173-003`** (9 verses — anchors: Gen 32:20, Deu 21:8)

- **Gen 32:20** 🔵 (✓) *target: appease*
  > Gen 32:20 and you shall say , ‘ Moreover , your servant Jacob is behind us .’” For he thought , “I may appease him with the present that goes ahead of me , and afterward I shall see his face . Perhaps he will accept me .”
- **Deu 21:8** 🔵 (✓) *target: atonement*
  > Deu 21:8 Accept atonement , O Lord , for your people Israel , whom you have redeemed , and do not set the guilt of innocent blood in the midst of your people Israel , so that their blood guilt be atoned for.’
- **Exo 32:30** (✓) *target: make atonement*
  > Exo 32:30 The next day Moses said to the people , “ You have sinned a great sin . And now I will go up to the Lord ; perhaps I can make atonement for your sin .”
- **Num 31:50** (✓) *target: atonement*
  > Num 31:50 And we have brought the Lord’s offering , what each man found , articles of gold , armlets and bracelets , signet rings , earrings , and beads , to make atonement for ourselves before the Lord .”
- **2Sa 21:3** (✓) *target: make atonement*
  > 2Sa 21:3 And David said to the Gibeonites , “ What shall I do for you? And how shall I make atonement , that you may bless the heritage of the Lord ?”
- **2Ch 30:18** (✓) *target: pardon*
  > 2Ch 30:18 For a majority of the people , many of them from Ephraim , Manasseh , Issachar , and Zebulun , had not cleansed themselves, yet they ate the Passover otherwise than as prescribed . For Hezekiah had prayed for them, saying , “ May the good Lord pardon everyone
- **Pro 16:14** (✓) *target: appease*
  > Pro 16:14 A king’s wrath is a messenger of death , and a wise man will appease it .
- **Isa 28:18** (✓) *target: annulled*
  > Isa 28:18 Then your covenant with death will be annulled , and your agreement with Sheol will not stand ; when the overwhelming scourge passes through , you will be beaten down by it.
- **Jer 18:23** (✓) *target: Forgive*
  > Jer 18:23 Yet you , O Lord , know all their plotting to kill me. Forgive not their iniquity , nor blot out their sin from your sight . Let them be overthrown before you; deal with them in the time of your anger .

**Group `UNCLASSIFIED`** (12 verses)

- **Exo 29:36** (—) *target: make atonement*
  > Exo 29:36 and every day you shall offer a bull as a sin offering for atonement . Also you shall purify the altar , when you make atonement for it, and shall anoint it to consecrate it .
- **Exo 29:37** (—) *target: make atonement*
  > Exo 29:37 Seven days you shall make atonement for the altar and consecrate it, and the altar shall be most holy . Whatever touches the altar shall become holy .
- **Exo 30:10** (—) *target: make atonement*
  > Exo 30:10 Aaron shall make atonement on its horns once a year . With the blood of the sin offering of atonement he shall make atonement for it once in the year throughout your generations . It is most holy to the Lord .”
- **Lev 8:15** (—) *target: make atonement*
  > Lev 8:15 And he killed it, and Moses took the blood , and with his finger put it on the horns of the altar around it and purified the altar and poured out the blood at the base of the altar and consecrated it to make atonement for it .
- **Lev 14:53** (—) *target: make atonement*
  > Lev 14:53 And he shall let the live bird go out of the city into the open country . So he shall make atonement for the house , and it shall be clean .”
- **Lev 16:18** (—) *target: make atonement*
  > Lev 16:18 Then he shall go out to the altar that is before the Lord and make atonement for it, and shall take some of the blood of the bull and some of the blood of the goat , and put it on the horns of the altar all around .
- **Lev 16:20** (—) *target: atoning*
  > Lev 16:20 “And when he has made an end of atoning for the Holy Place and the tent of meeting and the altar , he shall present the live goat .
- **Lev 16:27** (—) *target: make atonement*
  > Lev 16:27 And the bull for the sin offering and the goat for the sin offering , whose blood was brought in to make atonement in the Holy Place , shall be carried outside the camp . Their skin and their flesh and their dung shall be burned up with fire .
- **Num 35:33** (—) *target: made*
  > Num 35:33 You shall not pollute the land in which you live, for blood pollutes the land , and no atonement can be made for the land for the blood that is shed in it, except by the blood of the one who shed it .
- **Eze 43:20** (—) *target: make atonement*
  > Eze 43:20 And you shall take some of its blood and put it on the four horns of the altar and on the four corners of the ledge and upon the rim all around . Thus you shall purify the altar and make atonement for it .
- **Eze 43:26** (—) *target: make atonement*
  > Eze 43:26 Seven days shall they make atonement for the altar and cleanse it, and so consecrate it.
- **Eze 45:20** (—) *target: make atonement*
  > Eze 45:20 You shall do the same on the seventh day of the month for anyone who has sinned through error or ignorance ; so you shall make atonement for the temple .

### `H3724A` — 13/13 classified · 3 anchor verse(s)

**Group `3170-001`** (10 verses — anchors: Job 33:24, Psa 49:7)

- **Job 33:24** 🔵 (✓) *target: ransom*
  > Job 33:24 and he is merciful to him, and says , ‘ Deliver him from going down into the pit ; I have found a ransom ;
- **Psa 49:7** 🔵 (✓) *target: life*
  > Psa 49:7 Truly no man can ransom another , or give to God the price of his life ,
- **Exo 21:30** (✓) *target: ransom*
  > Exo 21:30 If a ransom is imposed on him, then he shall give for the redemption of his life whatever is imposed on him .
- **Exo 30:12** (✓) *target: ransom*
  > Exo 30:12 “When you take the census of the people of Israel , then each shall give a ransom for his life to the Lord when you number them, that there be no plague among them when you number them .
- **Num 35:31** (✓) *target: ransom*
  > Num 35:31 Moreover, you shall accept no ransom for the life of a murderer , who is guilty of death , but he shall be put to death .
- **Num 35:32** (✓) *target: ransom*
  > Num 35:32 And you shall accept no ransom for him who has fled to his city of refuge , that he may return to dwell in the land before the death of the high priest .
- **Job 36:18** (✓) *target: ransom*
  > Job 36:18 Beware lest wrath entice you into scoffing , and let not the greatness of the ransom turn you aside .
- **Pro 13:8** (✓) *target: ransom*
  > Pro 13:8 The ransom of a man’s life is his wealth , but a poor man hears no threat .
- **Pro 21:18** (✓) *target: ransom*
  > Pro 21:18 The wicked is a ransom for the righteous , and the traitor for the upright .
- **Isa 43:3** (✓) *target: ransom*
  > Isa 43:3 For I am the Lord your God , the Holy One of Israel , your Savior . I give Egypt as your ransom , Cush and Seba in exchange for you .

**Group `3170-002`** (3 verses — anchors: 1Sa 12:3)

- **1Sa 12:3** 🔵 (✓) *target: bribe*
  > 1Sa 12:3 Here I am; testify against me before the Lord and before his anointed . Whose ox have I taken ? Or whose donkey have I taken ? Or whom have I defrauded ? Whom have I oppressed ? Or from whose hand have I taken a bribe to blind my eyes with it? Testify against me and I will restore it to you .”
- **Pro 6:35** (✓) *target: compensation*
  > Pro 6:35 He will accept no compensation ; he will refuse though you multiply gifts .
- **Amo 5:12** (✓) *target: bribe*
  > Amo 5:12 For I know how many are your transgressions and how great are your sins — you who afflict the righteous , who take a bribe , and turn aside the needy in the gate .

### `H3725` — 8/8 classified · 1 anchor verse(s)

**Group `3171-001`** (8 verses — anchors: Lev 23:27)

- **Lev 23:27** 🔵 (✓) *target: Atonement*
  > Lev 23:27 “ Now on the tenth day of this seventh month is the Day of Atonement . It shall be for you a time of holy convocation , and you shall afflict yourselves and present a food offering to the Lord .
- **Exo 29:36** (✓) *target: atonement*
  > Exo 29:36 and every day you shall offer a bull as a sin offering for atonement . Also you shall purify the altar , when you make atonement for it, and shall anoint it to consecrate it .
- **Exo 30:10** (✓) *target: atonement*
  > Exo 30:10 Aaron shall make atonement on its horns once a year . With the blood of the sin offering of atonement he shall make atonement for it once in the year throughout your generations . It is most holy to the Lord .”
- **Exo 30:16** (✓) *target: atonement*
  > Exo 30:16 You shall take the atonement money from the people of Israel and shall give it for the service of the tent of meeting , that it may bring the people of Israel to remembrance before the Lord , so as to make atonement for your lives .”
- **Lev 23:28** (✓) *target: Atonement*
  > Lev 23:28 And you shall not do any work on that very day , for it is a Day of Atonement , to make atonement for you before the Lord your God .
- **Lev 25:9** (✓) *target: Atonement*
  > Lev 25:9 Then you shall sound the loud trumpet on the tenth day of the seventh month . On the Day of Atonement you shall sound the trumpet throughout all your land .
- **Num 5:8** (✓) *target: atonement*
  > Num 5:8 But if the man has no next of kin to whom restitution may be made for the wrong , the restitution for wrong shall go to the Lord for the priest , in addition to the ram of atonement with which atonement is made for him .
- **Num 29:11** (✓) *target: atonement*
  > Num 29:11 also one male goat for a sin offering , besides the sin offering of atonement , and the regular burnt offering and its grain offering , and their drink offerings .

### `H3727` — 22/22 classified · 2 anchor verse(s)

**Group `982-001`** (22 verses — anchors: Exo 25:22, Lev 16:14)

- **Exo 25:22** 🔵 (✓) *target: mercy seat*
  > Exo 25:22 There I will meet with you, and from above the mercy seat , from between the two cherubim that are on the ark of the testimony , I will speak with you about all that I will give you in commandment for the people of Israel .
- **Lev 16:14** 🔵 (✓) *target: mercy seat*
  > Lev 16:14 And he shall take some of the blood of the bull and sprinkle it with his finger on the front of the mercy seat on the east side , and in front of the mercy seat he shall sprinkle some of the blood with his finger seven times .
- **Exo 25:17** (✓) *target: mercy seat*
  > Exo 25:17 “You shall make a mercy seat of pure gold . Two cubits and a half shall be its length , and a cubit and a half its breadth .
- **Exo 25:18** (✓) *target: mercy seat*
  > Exo 25:18 And you shall make two cherubim of gold ; of hammered work shall you make them, on the two ends of the mercy seat .
- **Exo 25:19** (✓) *target: mercy seat*
  > Exo 25:19 Make one cherub on the one end , and one cherub on the other end . Of one piece with the mercy seat shall you make the cherubim on its two ends .
- **Exo 25:20** (✓) *target: mercy seat*
  > Exo 25:20 The cherubim shall spread out their wings above , overshadowing the mercy seat with their wings , their faces one to another ; toward the mercy seat shall the faces of the cherubim be.
- **Exo 25:21** (✓) *target: mercy seat*
  > Exo 25:21 And you shall put the mercy seat on the top of the ark , and in the ark you shall put the testimony that I shall give you .
- **Exo 26:34** (✓) *target: mercy seat*
  > Exo 26:34 You shall put the mercy seat on the ark of the testimony in the Most Holy Place.
- **Exo 30:6** (✓) *target: mercy seat*
  > Exo 30:6 And you shall put it in front of the veil that is above the ark of the testimony , in front of the mercy seat that is above the testimony , where I will meet with you .
- **Exo 31:7** (✓) *target: mercy seat*
  > Exo 31:7 the tent of meeting , and the ark of the testimony , and the mercy seat that is on it, and all the furnishings of the tent ,
- **Exo 35:12** (✓) *target: mercy seat*
  > Exo 35:12 the ark with its poles , the mercy seat , and the veil of the screen ;
- **Exo 37:6** (✓) *target: mercy seat*
  > Exo 37:6 And he made a mercy seat of pure gold . Two cubits and a half was its length , and a cubit and a half its breadth .
- **Exo 37:7** (✓) *target: mercy seat*
  > Exo 37:7 And he made two cherubim of gold . He made them of hammered work on the two ends of the mercy seat ,
- **Exo 37:8** (✓) *target: mercy seat*
  > Exo 37:8 one cherub on the one end , and one cherub on the other end . Of one piece with the mercy seat he made the cherubim on its two ends .
- **Exo 37:9** (✓) *target: mercy seat*
  > Exo 37:9 The cherubim spread out their wings above , overshadowing the mercy seat with their wings , with their faces one to another ; toward the mercy seat were the faces of the cherubim .
- **Exo 39:35** (✓) *target: mercy seat*
  > Exo 39:35 the ark of the testimony with its poles and the mercy seat ;
- **Exo 40:20** (✓) *target: mercy seat*
  > Exo 40:20 He took the testimony and put it into the ark , and put the poles on the ark and set the mercy seat above on the ark .
- **Lev 16:2** (✓) *target: mercy seat*
  > Lev 16:2 and the Lord said to Moses , “ Tell Aaron your brother not to come at any time into the Holy Place inside the veil , before the mercy seat that is on the ark , so that he may not die . For I will appear in the cloud over the mercy seat.
- **Lev 16:13** (✓) *target: mercy seat*
  > Lev 16:13 and put the incense on the fire before the Lord , that the cloud of the incense may cover the mercy seat that is over the testimony , so that he does not die .
- **Lev 16:15** (✓) *target: mercy seat*
  > Lev 16:15 “Then he shall kill the goat of the sin offering that is for the people and bring its blood inside the veil and do with its blood as he did with the blood of the bull , sprinkling it over the mercy seat and in front of the mercy seat .
- **Num 7:89** (✓) *target: mercy seat*
  > Num 7:89 And when Moses went into the tent of meeting to speak with the Lord , he heard the voice speaking to him from above the mercy seat that was on the ark of the testimony , from between the two cherubim ; and it spoke to him .
- **1Ch 28:11** (✓) *target: mercy seat*
  > 1Ch 28:11 Then David gave Solomon his son the plan of the vestibule of the temple, and of its houses , its treasuries , its upper rooms , and its inner chambers , and of the room for the mercy seat ;

### `H3819` — 2/2 classified · 1 anchor verse(s)

**Group `986-001`** (2 verses — anchors: Hos 1:6)

- **Hos 1:6** 🔵 (✓) *target: No Mercy*
  > Hos 1:6 She conceived again and bore a daughter . And the Lord said to him, “ Call her name No Mercy , for I will no more have mercy on the house of Israel , to forgive them at all .
- **Hos 1:8** (✓) *target: No Mercy*
  > Hos 1:8 When she had weaned No Mercy , she conceived and bore a son .

### `H5750` — 14/170 classified · 4 anchor verse(s)

**Group `990-001`** (7 verses — anchors: Job 2:3, Jer 3:17)

- **Job 2:3** 🔵 (✓) *target: still*
  > Job 2:3 And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and turns away from evil ? He still holds fast his integrity , although you incited me against him to destroy him without reason .”
- **Jer 3:17** 🔵 (✓) *target: more*
  > Jer 3:17 At that time Jerusalem shall be called the throne of the Lord , and all nations shall gather to it, to the presence of the Lord in Jerusalem , and they shall no more stubbornly follow their own evil heart .
- **Gen 37:5** (✓) *target: hated*
  > Gen 37:5 Now Joseph had a dream , and when he told it to his brothers they hated him even more .
- **Gen 37:8** (✓) *target: hated*
  > Gen 37:8 His brothers said to him, “Are you indeed to reign over us? Or are you indeed to rule over us?” So they hated him even more for his dreams and for his words .
- **Job 2:9** (✓) *target: still*
  > Job 2:9 Then his wife said to him, “Do you still hold fast your integrity ? Curse God and die .”
- **Isa 1:5** (✓) *target: continue*
  > Isa 1:5 Why will you still be struck down ? Why will you continue to rebel ? The whole head is sick , and the whole heart faint .
- **Hos 11:12** (✓) *target: walks*
  > Hos 11:12 Ephraim has surrounded me with lies , and the house of Israel with deceit , but Judah still walks with God and is faithful to the Holy One.

**Group `990-002`** (7 verses — anchors: Isa 5:25, Hab 2:3)

- **Isa 5:25** 🔵 (✓) *target: still*
  > Isa 5:25 Therefore the anger of the Lord was kindled against his people , and he stretched out his hand against them and struck them, and the mountains quaked ; and their corpses were as refuse in the midst of the streets . For all this his anger has not turned away , and his hand is stretched out still .
- **Hab 2:3** 🔵 (✓) *target: still*
  > Hab 2:3 For still the vision awaits its appointed time ; it hastens to the end —it will not lie . If it seems slow , wait for it; it will surely come ; it will not delay .
- **Job 27:3** (✓) *target: long as*
  > Job 27:3 as long as my breath is in me, and the spirit of God is in my nostrils ,
- **Isa 9:12** (✓) *target: still*
  > Isa 9:12 The Syrians on the east and the Philistines on the west devour Israel with open mouth . For all this his anger has not turned away , and his hand is stretched out still .
- **Isa 9:17** (✓) *target: still*
  > Isa 9:17 Therefore the Lord does not rejoice over their young men , and has no compassion on their fatherless and widows ; for everyone is godless and an evildoer , and every mouth speaks folly . For all this his anger has not turned away , and his hand is stretched out still .
- **Isa 9:21** (✓) *target: still*
  > Isa 9:21 Manasseh devours Ephraim , and Ephraim devours Manasseh ; together they are against Judah . For all this his anger has not turned away , and his hand is stretched out still .
- **Isa 10:4** (✓) *target: still*
  > Isa 10:4 Nothing remains but to crouch among the prisoners or fall among the slain . For all this his anger has not turned away , and his hand is stretched out still .

**Group `UNCLASSIFIED`** (156 verses)

- **Gen 4:25** (—) *target: again*
  > Gen 4:25 And Adam knew his wife again , and she bore a son and called his name Seth , for she said, “ God has appointed for me another offspring instead of Abel , for Cain killed him.”
- **Gen 7:4** (—) *target: in*
  > Gen 7:4 For in seven days I will send rain on the earth forty days and forty nights , and every living thing that I have made I will blot out from the face of the ground .”
- **Gen 8:10** (—) *target: seven*
  > Gen 8:10 He waited another seven days , and again he sent forth the dove out of the ark .
- **Gen 8:12** (—) *target: another*
  > Gen 8:12 Then he waited another seven days and sent forth the dove , and she did not return to him anymore .
- **Gen 8:21** (—) *target: again*
  > Gen 8:21 And when the Lord smelled the pleasing aroma , the Lord said in his heart , “I will never again curse the ground because of man , for the intention of man’s heart is evil from his youth . Neither will I ever again strike down every living creature as I have done .
- **Gen 8:22** (—) *target: While*
  > Gen 8:22 While the earth remains , seedtime and harvest , cold and heat , summer and winter , day and night , shall not cease .”
- **Gen 9:11** (—) *target: again*
  > Gen 9:11 I establish my covenant with you, that never again shall all flesh be cut off by the waters of the flood , and never again shall there be a flood to destroy the earth .”
- **Gen 9:15** (—) *target: again*
  > Gen 9:15 I will remember my covenant that is between me and you and every living creature of all flesh . And the waters shall never again become a flood to destroy all flesh .
- **Gen 17:5** (—) *target: longer*
  > Gen 17:5 No longer shall your name be called Abram , but your name shall be Abraham , for I have made you the father of a multitude of nations .
- **Gen 18:22** (—) *target: still*
  > Gen 18:22 So the men turned from there and went toward Sodom , but Abraham still stood before the Lord .
- **Gen 18:29** (—) *target: spoke*
  > Gen 18:29 Again he spoke to him and said , “ Suppose forty are found there .” He answered , “ For the sake of forty I will not do it.”
- **Gen 19:12** (—) *target: else*
  > Gen 19:12 Then the men said to Lot , “ Have you anyone else here ? Sons-in-law , sons , daughters , or anyone you have in the city , bring them out of the place .
- **Gen 24:20** (—) *target: again*
  > Gen 24:20 So she quickly emptied her jar into the trough and ran again to the well to draw water, and she drew for all his camels .
- **Gen 25:6** (—) *target: living*
  > Gen 25:6 But to the sons of his concubines Abraham gave gifts , and while he was still living he sent them away from his son Isaac , eastward to the east country .
- **Gen 29:7** (—) *target: still*
  > Gen 29:7 He said , “ Behold , it is still high day ; it is not time for the livestock to be gathered together . Water the sheep and go , pasture them.”
- **Gen 29:9** (—) *target: still*
  > Gen 29:9 While he was still speaking with them, Rachel came with her father’s sheep , for she was a shepherdess .
- **Gen 29:27** (—) *target: seven*
  > Gen 29:27 Complete the week of this one, and we will give you the other also in return for serving me another seven years .”
- **Gen 29:30** (—) *target: seven*
  > Gen 29:30 So Jacob went in to Rachel also , and he loved Rachel more than Leah , and served Laban for another seven years .
- **Gen 29:33** (—) *target: again*
  > Gen 29:33 She conceived again and bore a son , and said , “ Because the Lord has heard that I am hated , he has given me this son also .” And she called his name Simeon .
- **Gen 29:34** (—) *target: Again*
  > Gen 29:34 Again she conceived and bore a son , and said , “ Now this time my husband will be attached to me, because I have borne him three sons .” Therefore his name was called Levi .
- **Gen 29:35** (—) *target: again*
  > Gen 29:35 And she conceived again and bore a son , and said , “This time I will praise the Lord .” Therefore she called his name Judah . Then she ceased bearing .
- **Gen 30:7** (—) *target: bore*
  > Gen 30:7 Rachel’s servant Bilhah conceived again and bore Jacob a second son .
- **Gen 30:19** (—) *target: Leah*
  > Gen 30:19 And Leah conceived again, and she bore Jacob a sixth son .
- **Gen 31:14** (—) *target: us*
  > Gen 31:14 Then Rachel and Leah answered and said to him, “Is there any portion or inheritance left to us in our father’s house ?
- **Gen 32:28** (—) *target: longer*
  > Gen 32:28 Then he said , “Your name shall no longer be called Jacob , but Israel , for you have striven with God and with men , and have prevailed .”
- **Gen 35:9** (—) *target: came*
  > Gen 35:9 God appeared to Jacob again, when he came from Paddan-aram , and blessed him .
- **Gen 35:10** (—) *target: longer*
  > Gen 35:10 And God said to him, “Your name is Jacob ; no longer shall your name be called Jacob , but Israel shall be your name .” So he called his name Israel .
- **Gen 35:16** (—) *target: still*
  > Gen 35:16 Then they journeyed from Bethel . When they were still some distance from Ephrath , Rachel went into labor , and she had hard labor .
- **Gen 37:9** (—) *target: another*
  > Gen 37:9 Then he dreamed another dream and told it to his brothers and said , “ Behold , I have dreamed another dream . Behold , the sun , the moon , and eleven stars were bowing down to me .”
- **Gen 38:4** (—) *target: again*
  > Gen 38:4 She conceived again and bore a son , and she called his name Onan .
- **Gen 38:5** (—) *target: again*
  > Gen 38:5 Yet again she bore a son , and she called his name Shelah . Judah was in Chezib when she bore him .
- **Gen 38:26** (—) *target: know her*
  > Gen 38:26 Then Judah identified them and said , “She is more righteous than I, since I did not give her to my son Shelah .” And he did not know her again .
- **Gen 40:13** (—) *target: In*
  > Gen 40:13 In three days Pharaoh will lift up your head and restore you to your office , and you shall place Pharaoh’s cup in his hand as formerly , when you were his cupbearer .
- **Gen 40:19** (—) *target: three*
  > Gen 40:19 In three days Pharaoh will lift up your head — from you!—and hang you on a tree . And the birds will eat the flesh from you .”
- **Gen 43:6** (—) *target: another*
  > Gen 43:6 Israel said , “ Why did you treat me so badly as to tell the man that you had another brother ?”
- **Gen 43:7** (—) *target: father*
  > Gen 43:7 They replied , “The man questioned us carefully about ourselves and our kindred , saying , ‘Is your father still alive ? Do you have another brother ?’ What we told him was in answer to these questions . Could we in any way know that he would say , ‘Bring your brother down ’?”
- **Gen 43:27** (—) *target: alive*
  > Gen 43:27 And he inquired about their welfare and said , “Is your father well , the old man of whom you spoke ? Is he still alive ?”
- **Gen 43:28** (—) *target: still*
  > Gen 43:28 They said , “Your servant our father is well ; he is still alive .” And they bowed their heads and prostrated themselves.
- **Gen 44:14** (—) *target: still*
  > Gen 44:14 When Judah and his brothers came to Joseph’s house , he was still there . They fell before him to the ground .
- **Gen 45:3** (—) *target: still*
  > Gen 45:3 And Joseph said to his brothers , “ I am Joseph ! Is my father still alive ?” But his brothers could not answer him, for they were dismayed at his presence .
- **Gen 45:6** (—) *target: yet*
  > Gen 45:6 For the famine has been in the land these two years , and there are yet five years in which there will be neither plowing nor harvest .
- **Gen 45:11** (—) *target: yet*
  > Gen 45:11 There I will provide for you, for there are yet five years of famine to come, so that you and your household , and all that you have, do not come to poverty .’
- **Gen 45:26** (—) *target: still*
  > Gen 45:26 And they told him, “ Joseph is still alive , and he is ruler over all the land of Egypt .” And his heart became numb , for he did not believe them .
- **Gen 45:28** (—) *target: still*
  > Gen 45:28 And Israel said , “It is enough ; Joseph my son is still alive . I will go and see him before I die .”
- **Gen 46:29** (—) *target: good while*
  > Gen 46:29 Then Joseph prepared his chariot and went up to meet Israel his father in Goshen . He presented himself to him and fell on his neck and wept on his neck a good while .
- **Gen 46:30** (—) *target: still*
  > Gen 46:30 Israel said to Joseph , “ Now let me die , since I have seen your face and know that you are still alive .”
- **Gen 48:7** (—) *target: when*
  > Gen 48:7 As for me , when I came from Paddan , to my sorrow Rachel died in the land of Canaan on the way , when there was still some distance to go to Ephrath , and I buried her there on the way to Ephrath (that is, Bethlehem ).”
- **Gen 48:15** (—) *target: life long*
  > Gen 48:15 And he blessed Joseph and said , “The God before whom my fathers Abraham and Isaac walked , the God who has been my shepherd all my life long to this day ,
- **Num 8:25** (—) *target: more*
  > Num 8:25 And from the age of fifty years they shall withdraw from the duty of the service and serve no more .
- **Num 11:33** (—) *target: yet*
  > Num 11:33 While the meat was yet between their teeth , before it was consumed , the anger of the Lord was kindled against the people , and the Lord struck down the people with a very great plague .
- **Num 18:5** (—) *target: again*
  > Num 18:5 And you shall keep guard over the sanctuary and over the altar , that there may never again be wrath on the people of Israel .
- **Num 18:22** (—) *target: not*
  > Num 18:22 so that the people of Israel do not come near the tent of meeting , lest they bear sin and die .
- **Num 19:13** (—) *target: uncleanness*
  > Num 19:13 Whoever touches a dead person, the body of anyone who has died , and does not cleanse himself, defiles the tabernacle of the Lord , and that person shall be cut off from Israel ; because the water for impurity was not thrown on him, he shall be unclean . His uncleanness is still on him .
- **Num 22:15** (—) *target: Balak*
  > Num 22:15 Once again Balak sent princes , more in number and more honorable than these .
- **Num 22:30** (—) *target: long*
  > Num 22:30 And the donkey said to Balaam , “Am I not your donkey , on which you have ridden all your life long to this day ? Is it my habit to treat you this way ?” And he said , “ No .”
- **Num 32:14** (—) *target: fierce*
  > Num 32:14 And behold , you have risen in your fathers ’ place , a brood of sinful men , to increase still more the fierce anger of the Lord against Israel !
- **Num 32:15** (—) *target: abandon*
  > Num 32:15 For if you turn away from following him, he will again abandon them in the wilderness , and you will destroy all this people .”
- **Judg 2:14** (—) *target: longer*
  > Judg 2:14 So the anger of the Lord was kindled against Israel , and he gave them over to plunderers , who plundered them. And he sold them into the hand of their surrounding enemies , so that they could no longer withstand their enemies .
- **Judg 6:24** (—) *target: still*
  > Judg 6:24 Then Gideon built an altar there to the Lord and called it, The Lord Is Peace . To this day it still stands at Ophrah , which belongs to the Abiezrites .
- **Judg 7:4** (—) *target: still*
  > Judg 7:4 And the Lord said to Gideon , “The people are still too many . Take them down to the water , and I will test them for you there , and anyone of whom I say to you, ‘ This one shall go with you,’ shall go with you, and anyone of whom I say to you, ‘ This one shall not go with you,’ shall not go .”
- **Judg 8:20** (—) *target: still*
  > Judg 8:20 So he said to Jether his firstborn , “ Rise and kill them!” But the young man did not draw his sword , for he was afraid , because he was still a young man .
- **Judg 9:37** (—) *target: Gaal*
  > Judg 9:37 Gaal spoke again and said , “ Look , people are coming down from the center of the land , and one company is coming from the direction of the Diviners ’ Oak .”
- **Judg 11:14** (—) *target: Jephthah*
  > Judg 11:14 Jephthah again sent messengers to the king of the Ammonites
- **Judg 13:8** (—) *target: teach*
  > Judg 13:8 Then Manoah prayed to the Lord and said , “ O Lord , please let the man of God whom you sent come again to us and teach us what we are to do with the child who will be born .”
- **Judg 13:9** (—) *target: woman*
  > Judg 13:9 And God listened to the voice of Manoah , and the angel of God came again to the woman as she sat in the field . But Manoah her husband was not with her .
- **Judg 13:21** (—) *target: angel*
  > Judg 13:21 The angel of the Lord appeared no more to Manoah and to his wife . Then Manoah knew that he was the angel of the Lord .
- **Judg 18:24** (—) *target: left*
  > Judg 18:24 And he said , “You take my gods that I made and the priest , and go away , and what have I left ? How then do you ask me , ‘ What is the matter with you ?’”
- **Judg 20:25** (—) *target: 18,000*
  > Judg 20:25 And Benjamin went against them out of Gibeah the second day , and destroyed 18,000 men of the people of Israel . All these were men who drew the sword .
- **Judg 20:28** (—) *target: go out*
  > Judg 20:28 and Phinehas the son of Eleazar , son of Aaron , ministered before it in those days ), saying , “Shall we go out once more to battle against our brothers , the people of Benjamin , or shall we cease ?” And the Lord said , “Go up , for tomorrow I will give them into your hand .”
- **Neh 2:17** (—) *target: longer*
  > Neh 2:17 Then I said to them, “ You see the trouble we are in, how Jerusalem lies in ruins with its gates burned . Come , let us build the wall of Jerusalem , that we may no longer suffer derision .”
- **Job 1:16** (—) *target: speaking*
  > Job 1:16 While he was yet speaking , there came another and said , “The fire of God fell from heaven and burned up the sheep and the servants and consumed them, and I alone have escaped to tell you .”
- **Job 1:17** (—) *target: speaking*
  > Job 1:17 While he was yet speaking , there came another and said , “The Chaldeans formed three groups and made a raid on the camels and took them and struck down the servants with the edge of the sword , and I alone have escaped to tell you .”
- **Job 6:10** (—) *target: This would*
  > Job 6:10 This would be my comfort ; I would even exult in pain unsparing , for I have not denied the words of the Holy One .
- **Job 6:29** (—) *target: stake*
  > Job 6:29 Please turn ; let no injustice be done. Turn now; my vindication is at stake .
- **Job 7:10** (—) *target: more*
  > Job 7:10 he returns no more to his house , nor does his place know him anymore .
- **Job 8:12** (—) *target: yet*
  > Job 8:12 While yet in flower and not cut down , they wither before any other plant .
- **Job 14:7** (—) *target: again*
  > Job 14:7 “For there is hope for a tree , if it be cut down , that it will sprout again , and that its shoots will not cease .
- **Job 20:9** (—) *target: more*
  > Job 20:9 The eye that saw him will see him no more , nor will his place any more behold him.
- **Job 24:20** (—) *target: longer*
  > Job 24:20 The womb forgets them; the worm finds them sweet ; they are no longer remembered , so wickedness is broken like a tree .’
- **Job 29:5** (—) *target: yet*
  > Job 29:5 when the Almighty was yet with me, when my children were all around me,
- **Job 32:15** (—) *target: more*
  > Job 32:15 “They are dismayed ; they answer no more ; they have not a word to say .
- **Job 32:16** (—) *target: more*
  > Job 32:16 And shall I wait , because they do not speak , because they stand there, and answer no more ?
- **Job 34:23** (—) *target: further*
  > Job 34:23 For God has no need to consider a man further , that he should go before God in judgment .
- **Job 36:2** (—) *target: yet*
  > Job 36:2 “Bear with me a little , and I will show you, for I have yet something to say on God’s behalf.
- **Isa 2:4** (—) *target: anymore*
  > Isa 2:4 He shall judge between the nations , and shall decide disputes for many peoples ; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore .
- **Isa 5:4** (—) *target: more*
  > Isa 5:4 What more was there to do for my vineyard , that I have not done in it? When I looked for it to yield grapes , why did it yield wild grapes ?
- **Isa 6:13** (—) *target: remain*
  > Isa 6:13 And though a tenth remain in it, it will be burned again , like a terebinth or an oak , whose stump remains when it is felled .” The holy seed is its stump .
- **Isa 7:8** (—) *target: sixty-five*
  > Isa 7:8 For the head of Syria is Damascus , and the head of Damascus is Rezin . And within sixty-five years Ephraim will be shattered from being a people .
- **Isa 8:5** (—) *target: again*
  > Isa 8:5 The Lord spoke to me again :
- **Isa 10:20** (—) *target: more*
  > Isa 10:20 In that day the remnant of Israel and the survivors of the house of Jacob will no more lean on him who struck them, but will lean on the Lord , the Holy One of Israel , in truth .
- **Isa 10:25** (—) *target: in*
  > Isa 10:25 For in a very little while my fury will come to an end , and my anger will be directed to their destruction .
- **Isa 10:32** (—) *target: This*
  > Isa 10:32 This very day he will halt at Nob ; he will shake his fist at the mount of the daughter of Zion , the hill of Jerusalem .
- **Isa 14:1** (—) *target: again*
  > Isa 14:1 For the Lord will have compassion on Jacob and will again choose Israel , and will set them in their own land , and sojourners will join them and will attach themselves to the house of Jacob .
- **Isa 21:16** (—) *target: year*
  > Isa 21:16 For thus the Lord said to me, “Within a year , according to the years of a hired worker , all the glory of Kedar will come to an end .
- **Isa 23:10** (—) *target: anymore*
  > Isa 23:10 Cross over your land like the Nile , O daughter of Tarshish ; there is no restraint anymore .
- **Isa 23:12** (—) *target: more*
  > Isa 23:12 And he said : “You will no more exult , O oppressed virgin daughter of Sidon ; arise , cross over to Cyprus , even there you will have no rest .”
- **Isa 26:21** (—) *target: more*
  > Isa 26:21 For behold , the Lord is coming out from his place to punish the inhabitants of the earth for their iniquity , and the earth will disclose the blood shed on it, and will no more cover its slain .
- **Isa 28:4** (—) *target: soon*
  > Isa 28:4 and the fading flower of its glorious beauty , which is on the head of the rich valley , will be like a first-ripe fig before the summer : when someone sees it, he swallows it as soon as it is in his hand .
- **Isa 29:17** (—) *target: yet*
  > Isa 29:17 Is it not yet a very little while until Lebanon shall be turned into a fruitful field , and the fruitful field shall be regarded as a forest ?
- **Isa 30:20** (—) *target: anymore*
  > Isa 30:20 And though the Lord give you the bread of adversity and the water of affliction , yet your Teacher will not hide himself anymore , but your eyes shall see your Teacher .
- **Isa 32:5** (—) *target: fool*
  > Isa 32:5 The fool will no more be called noble , nor the scoundrel said to be honorable .
- **Isa 38:11** (—) *target: inhabitants*
  > Isa 38:11 I said , I shall not see the Lord , the Lord in the land of the living ; I shall look on man no more among the inhabitants of the world .
- **Isa 45:5** (—) *target: other*
  > Isa 45:5 I am the Lord , and there is no other , besides me there is no God ; I equip you, though you do not know me ,
- **Isa 45:6** (—) *target: other*
  > Isa 45:6 that people may know , from the rising of the sun and from the west , that there is none besides me; I am the Lord , and there is no other .
- **Isa 45:14** (—) *target: other*
  > Isa 45:14 Thus says the Lord : “The wealth of Egypt and the merchandise of Cush , and the Sabeans , men of stature , shall come over to you and be yours; they shall follow you; they shall come over in chains and bow down to you. They will plead with you, saying: ‘ Surely God is in you, and there is no other , no god besides him.’”
- **Isa 45:18** (—) *target: other*
  > Isa 45:18 For thus says the Lord , who created the heavens ( he is God !), who formed the earth and made it ( he established it; he did not create it empty , he formed it to be inhabited !): “ I am the Lord , and there is no other .
- **Isa 45:21** (—) *target: other*
  > Isa 45:21 Declare and present your case; let them take counsel together ! Who told this long ago ? Who declared it of old ? Was it not I , the Lord ? And there is no other god besides me, a righteous God and a Savior ; there is none besides me .
- **Isa 45:22** (—) *target: other*
  > Isa 45:22 “ Turn to me and be saved , all the ends of the earth ! For I am God , and there is no other .
- **Isa 46:9** (—) *target: other*
  > Isa 46:9 remember the former things of old ; for I am God , and there is no other ; I am God , and there is none like me ,
- **Isa 47:8** (—) *target: besides*
  > Isa 47:8 Now therefore hear this , you lover of pleasures , who sit securely , who say in your heart , “ I am, and there is no one besides me; I shall not sit as a widow or know the loss of children ”:
- **Isa 47:10** (—) *target: besides*
  > Isa 47:10 You felt secure in your wickedness ; you said , “No one sees me”; your wisdom and your knowledge led you astray , and you said in your heart , “ I am, and there is no one besides me.”
- **Isa 49:20** (—) *target: yet*
  > Isa 49:20 The children of your bereavement will yet say in your ears : ‘The place is too narrow for me; make room for me to dwell in.’
- **Isa 51:22** (—) *target: more*
  > Isa 51:22 Thus says your Lord , the Lord , your God who pleads the cause of his people : “ Behold , I have taken from your hand the cup of staggering ; the bowl of my wrath you shall drink no more ;
- **Isa 52:1** (—) *target: more*
  > Isa 52:1 Awake , awake , put on your strength , O Zion ; put on your beautiful garments , O Jerusalem , the holy city ; for there shall no more come into you the uncircumcised and the unclean .
- **Isa 54:4** (—) *target: more*
  > Isa 54:4 “ Fear not , for you will not be ashamed ; be not confounded , for you will not be disgraced ; for you will forget the shame of your youth , and the reproach of your widowhood you will remember no more .
- **Isa 54:9** (—) *target: more*
  > Isa 54:9 “ This is like the days of Noah to me: as I swore that the waters of Noah should no more go over the earth , so I have sworn that I will not be angry with you, and will not rebuke you .
- **Isa 56:8** (—) *target: yet*
  > Isa 56:8 The Lord God , who gathers the outcasts of Israel , declares , “I will gather yet others to him besides those already gathered .”
- **Isa 60:18** (—) *target: more*
  > Isa 60:18 Violence shall no more be heard in your land , devastation or destruction within your borders ; you shall call your walls Salvation , and your gates Praise .
- **Isa 60:19** (—) *target: sun*
  > Isa 60:19 The sun shall be no more your light by day , nor for brightness shall the moon give you light ; but the Lord will be your everlasting light , and your God will be your glory .
- **Isa 60:20** (—) *target: sun*
  > Isa 60:20 Your sun shall no more go down , nor your moon withdraw itself; for the Lord will be your everlasting light , and your days of mourning shall be ended .
- **Isa 62:4** (—) *target: more*
  > Isa 62:4 You shall no more be termed Forsaken , and your land shall no more be termed Desolate , but you shall be called My Delight Is in Her , and your land Married ; for the Lord delights in you, and your land shall be married .
- **Isa 62:8** (—) *target: again*
  > Isa 62:8 The Lord has sworn by his right hand and by his mighty arm : “I will not again give your grain to be food for your enemies , and foreigners shall not drink your wine for which you have labored ;
- **Isa 65:19** (—) *target: more*
  > Isa 65:19 I will rejoice in Jerusalem and be glad in my people ; no more shall be heard in it the sound of weeping and the cry of distress .
- **Isa 65:20** (—) *target: more*
  > Isa 65:20 No more shall there be in it an infant who lives but a few days , or an old man who does not fill out his days , for the young man shall die a hundred years old , and the sinner a hundred years old shall be accursed .
- **Isa 65:24** (—) *target: yet*
  > Isa 65:24 Before they call I will answer ; while they are yet speaking I will hear .
- **Jer 2:9** (—) *target: still*
  > Jer 2:9 “ Therefore I still contend with you, declares the Lord , and with your children’s children I will contend .
- **Jer 2:31** (—) *target: more*
  > Jer 2:31 And you, O generation , behold the word of the Lord . Have I been a wilderness to Israel , or a land of thick darkness ? Why then do my people say , ‘We are free , we will come no more to you ’?
- **Jer 3:1** (—) *target: return*
  > Jer 3:1 “ If a man divorces his wife and she goes from him and becomes another man’s wife, will he return to her? Would not that land be greatly polluted ? You have played the whore with many lovers ; and would you return to me? declares the Lord .
- **Jer 3:16** (—) *target: more*
  > Jer 3:16 And when you have multiplied and been fruitful in the land , in those days , declares the Lord , they shall no more say , “The ark of the covenant of the Lord .” It shall not come to mind or be remembered or missed ; it shall not be made again .
- **Jer 7:32** (—) *target: more*
  > Jer 7:32 Therefore , behold , the days are coming , declares the Lord , when it will no more be called Topheth , or the Valley of the Son of Hinnom , but the Valley of Slaughter ; for they will bury in Topheth , because there is no room elsewhere .
- **Jer 10:20** (—) *target: again*
  > Jer 10:20 My tent is destroyed , and all my cords are broken ; my children have gone from me, and they are not ; there is no one to spread my tent again and to set up my curtains .
- **Jer 11:19** (—) *target: more*
  > Jer 11:19 But I was like a gentle lamb led to the slaughter . I did not know it was against me they devised schemes , saying, “Let us destroy the tree with its fruit , let us cut him off from the land of the living , that his name be remembered no more .”
- **Jer 13:27** (—) *target: long*
  > Jer 13:27 I have seen your abominations , your adulteries and neighings , your lewd whorings , on the hills in the field . Woe to you, O Jerusalem ! How long will it be before you are made clean ?”
- **Jer 15:9** (—) *target: yet*
  > Jer 15:9 She who bore seven has grown feeble ; she has fainted away ; her sun went down while it was yet day; she has been shamed and disgraced . And the rest of them I will give to the sword before their enemies , declares the Lord .”
- **Jer 16:14** (—) *target: lives*
  > Jer 16:14 “ Therefore , behold , the days are coming , declares the Lord , when it shall no longer be said , ‘As the Lord lives who brought up the people of Israel out of the land of Egypt ,’
- **Jer 19:6** (—) *target: more*
  > Jer 19:6 therefore , behold , days are coming , declares the Lord , when this place shall no more be called Topheth , or the Valley of the Son of Hinnom , but the Valley of Slaughter .
- **Jer 19:11** (—) *target: Topheth*
  > Jer 19:11 and shall say to them, ‘ Thus says the Lord of hosts : So will I break this people and this city , as one breaks a potter’s vessel , so that it can never be mended . Men shall bury in Topheth because there will be no place else to bury .
- **Hos 1:4** (—) *target: while*
  > Hos 1:4 And the Lord said to him, “ Call his name Jezreel , for in just a little while I will punish the house of Jehu for the blood of Jezreel , and I will put an end to the kingdom of the house of Israel .
- **Hos 1:6** (—) *target: again*
  > Hos 1:6 She conceived again and bore a daughter . And the Lord said to him, “ Call her name No Mercy , for I will no more have mercy on the house of Israel , to forgive them at all .
- **Hos 2:16** (—) *target: Baal*
  > Hos 2:16 “And in that day , declares the Lord , you will call me ‘My Husband ,’ and no longer will you call me ‘ My Baal .’
- **Hos 2:17** (—) *target: more*
  > Hos 2:17 For I will remove the names of the Baals from her mouth , and they shall be remembered by name no more .
- **Hos 3:1** (—) *target: again*
  > Hos 3:1 And the Lord said to me, “ Go again , love a woman who is loved by another man and is an adulteress , even as the Lord loves the children of Israel , though they turn to other gods and love cakes of raisins .”
- **Hos 12:9** (—) *target: dwell*
  > Hos 12:9 I am the Lord your God from the land of Egypt ; I will again make you dwell in tents , as in the days of the appointed feast.
- **Hos 14:3** (—) *target: God*
  > Hos 14:3 Assyria shall not save us; we will not ride on horses ; and we will say no more, ‘Our God ,’ to the work of our hands . In you the orphan finds mercy .”
- **Hos 14:8** (—) *target: what*
  > Hos 14:8 O Ephraim , what have I to do with idols ? It is I who answer and look after you. I am like an evergreen cypress ; from me comes your fruit .
- **Mic 1:15** (—) *target: again*
  > Mic 1:15 I will again bring a conqueror to you, inhabitants of Mareshah ; the glory of Israel shall come to Adullam .
- **Mic 4:3** (—) *target: anymore*
  > Mic 4:3 He shall judge between many peoples , and shall decide disputes for strong nations far away; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore ;
- **Mic 5:13** (—) *target: more*
  > Mic 5:13 and I will cut off your carved images and your pillars from among you, and you shall bow down no more to the work of your hands ;
- **Mic 6:10** (—) *target: Can*
  > Mic 6:10 Can I forget any longer the treasures of wickedness in the house of the wicked , and the scant measure that is accursed ?
- **Nah 1:12** (—) *target: more*
  > Nah 1:12 Thus says the Lord , “ Though they are at full strength and many , they will be cut down and pass away. Though I have afflicted you, I will afflict you no more .
- **Nah 1:14** (—) *target: house*
  > Nah 1:14 The Lord has given commandment about you: “No more shall your name be perpetuated ; from the house of your gods I will cut off the carved image and the metal image. I will make your grave , for you are vile .”
- **Nah 1:15** (—) *target: never*
  > Nah 1:15 Behold , upon the mountains , the feet of him who brings good news , who publishes peace ! Keep your feasts , O Judah ; fulfill your vows , for never again shall the worthless pass through you; he is utterly cut off .
- **Nah 2:13** (—) *target: longer*
  > Nah 2:13 Behold , I am against you, declares the Lord of hosts , and I will burn your chariots in smoke , and the sword shall devour your young lions . I will cut off your prey from the earth , and the voice of your messengers shall no longer be heard .
- **Hag 2:6** (—) *target: Yet*
  > Hag 2:6 For thus says the Lord of hosts : Yet once more, in a little while , I will shake the heavens and the earth and the sea and the dry land .
- **Hag 2:19** (—) *target: yet*
  > Hag 2:19 Is the seed yet in the barn ? Indeed , the vine , the fig tree , the pomegranate , and the olive tree have yielded nothing . But from this day on I will bless you.”
- **Mal 2:13** (—) *target: longer regards*
  > Mal 2:13 And this second thing you do . You cover the Lord’s altar with tears , with weeping and groaning because he no longer regards the offering or accepts it with favor from your hand .

### `H6279` — 19/19 classified · 4 anchor verse(s)

**Group `987-001`** (14 verses — anchors: Exo 8:30, 2Ch 33:13)

- **Exo 8:30** 🔵 (✓) *target: prayed to*
  > Exo 8:30 So Moses went out from Pharaoh and prayed to the Lord .
- **2Ch 33:13** 🔵 (✓) *target: entreaty*
  > 2Ch 33:13 He prayed to him, and God was moved by his entreaty and heard his plea and brought him again to Jerusalem into his kingdom . Then Manasseh knew that the Lord was God .
- **Exo 8:8** (✓) *target: Plead*
  > Exo 8:8 Then Pharaoh called Moses and Aaron and said , “ Plead with the Lord to take away the frogs from me and from my people , and I will let the people go to sacrifice to the Lord .”
- **Exo 8:9** (✓) *target: plead*
  > Exo 8:9 Moses said to Pharaoh , “Be pleased to command me when I am to plead for you and for your servants and for your people , that the frogs be cut off from you and your houses and be left only in the Nile .”
- **Exo 8:28** (✓) *target: Plead*
  > Exo 8:28 So Pharaoh said , “ I will let you go to sacrifice to the Lord your God in the wilderness ; only you must not go very far away . Plead for me .”
- **Exo 8:29** (✓) *target: plead*
  > Exo 8:29 Then Moses said , “ Behold , I am going out from you and I will plead with the Lord that the swarms of flies may depart from Pharaoh , from his servants , and from his people , tomorrow . Only let not Pharaoh cheat again by not letting the people go to sacrifice to the Lord .”
- **Exo 9:28** (✓) *target: Plead*
  > Exo 9:28 Plead with the Lord , for there has been enough of God’s thunder and hail . I will let you go , and you shall stay no longer .”
- **Exo 10:17** (✓) *target: plead*
  > Exo 10:17 Now therefore, forgive my sin , please , only this once , and plead with the Lord your God only to remove this death from me.”
- **Exo 10:18** (✓) *target: pleaded*
  > Exo 10:18 So he went out from Pharaoh and pleaded with the Lord .
- **Judg 13:8** (✓) *target: prayed*
  > Judg 13:8 Then Manoah prayed to the Lord and said , “ O Lord , please let the man of God whom you sent come again to us and teach us what we are to do with the child who will be born .”
- **2Sa 21:14** (✓) *target: plea*
  > 2Sa 21:14 And they buried the bones of Saul and his son Jonathan in the land of Benjamin in Zela , in the tomb of Kish his father . And they did all that the king commanded . And after that God responded to the plea for the land .
- **2Sa 24:25** (✓) *target: plea*
  > 2Sa 24:25 And David built there an altar to the Lord and offered burnt offerings and peace offerings . So the Lord responded to the plea for the land , and the plague was averted from Israel .
- **2Ch 33:19** (✓) *target: entreaty*
  > 2Ch 33:19 And his prayer , and how God was moved by his entreaty , and all his sin and his faithlessness , and the sites on which he built high places and set up the Asherim and the images , before he humbled himself, behold , they are written in the Chronicles of the Seers .
- **Ezr 8:23** (✓) *target: entreaty*
  > Ezr 8:23 So we fasted and implored our God for this , and he listened to our entreaty .

**Group `987-002`** (5 verses — anchors: Gen 25:21, Job 33:26)

- **Gen 25:21** 🔵 (✓) *target: prayed*
  > Gen 25:21 And Isaac prayed to the Lord for his wife , because she was barren . And the Lord granted his prayer , and Rebekah his wife conceived .
- **Job 33:26** 🔵 (✓) *target: prays*
  > Job 33:26 then man prays to God , and he accepts him; he sees his face with a shout of joy , and he restores to man his righteousness .
- **1Ch 5:20** (✓) *target: plea*
  > 1Ch 5:20 And when they prevailed over them, the Hagrites and all who were with them were given into their hands , for they cried out to God in the battle , and he granted their urgent plea because they trusted in him .
- **Job 22:27** (✓) *target: prayer*
  > Job 22:27 You will make your prayer to him, and he will hear you, and you will pay your vows .
- **Isa 19:22** (✓) *target: mercy*
  > Isa 19:22 And the Lord will strike Egypt , striking and healing , and they will return to the Lord , and he will listen to their pleas for mercy and heal them .

### `H7359` — 1/1 classified · 1 anchor verse(s)

**Group `988-001`** (1 verse — anchors: Dan 2:18)

- **Dan 2:18** 🔵 (✓) *target: mercy*
  > Dan 2:18 and told them to seek mercy from the God of heaven concerning this mystery , so that Daniel and his companions might not be destroyed with the rest of the wise men of Babylon .

### `H8467` — 24/24 classified · 3 anchor verse(s)

**Group `985-001`** (21 verses — anchors: 1Ki 8:38, Dan 9:20)

- **1Ki 8:38** 🔵 (✓) *target: plea*
  > 1Ki 8:38 whatever prayer , whatever plea is made by any man or by all your people Israel , each knowing the affliction of his own heart and stretching out his hands toward this house ,
- **Dan 9:20** 🔵 (✓) *target: plea*
  > Dan 9:20 While I was speaking and praying , confessing my sin and the sin of my people Israel , and presenting my plea before the Lord my God for the holy hill of my God ,
- **1Ki 8:28** (✓) *target: plea*
  > 1Ki 8:28 Yet have regard to the prayer of your servant and to his plea , O Lord my God , listening to the cry and to the prayer that your servant prays before you this day ,
- **1Ki 8:30** (✓) *target: plea*
  > 1Ki 8:30 And listen to the plea of your servant and of your people Israel , when they pray toward this place . And listen in heaven your dwelling place , and when you hear , forgive .
- **1Ki 8:45** (✓) *target: plea*
  > 1Ki 8:45 then hear in heaven their prayer and their plea , and maintain their cause .
- **1Ki 8:49** (✓) *target: plea*
  > 1Ki 8:49 then hear in heaven your dwelling place their prayer and their plea , and maintain their cause
- **1Ki 8:52** (✓) *target: plea*
  > 1Ki 8:52 Let your eyes be open to the plea of your servant and to the plea of your people Israel , giving ear to them whenever they call to you .
- **1Ki 8:54** (✓) *target: plea*
  > 1Ki 8:54 Now as Solomon finished offering all this prayer and plea to the Lord , he arose from before the altar of the Lord , where he had knelt with hands outstretched toward heaven .
- **1Ki 9:3** (✓) *target: plea*
  > 1Ki 9:3 And the Lord said to him, “I have heard your prayer and your plea , which you have made before me. I have consecrated this house that you have built , by putting my name there forever . My eyes and my heart will be there for all time .
- **2Ch 6:19** (✓) *target: plea*
  > 2Ch 6:19 Yet have regard to the prayer of your servant and to his plea , O Lord my God , listening to the cry and to the prayer that your servant prays before you,
- **2Ch 6:29** (✓) *target: plea*
  > 2Ch 6:29 whatever prayer , whatever plea is made by any man or by all your people Israel , each knowing his own affliction and his own sorrow and stretching out his hands toward this house ,
- **2Ch 6:35** (✓) *target: plea*
  > 2Ch 6:35 then hear from heaven their prayer and their plea , and maintain their cause .
- **2Ch 6:39** (✓) *target: pleas*
  > 2Ch 6:39 then hear from heaven your dwelling place their prayer and their pleas , and maintain their cause and forgive your people who have sinned against you .
- **2Ch 33:13** (✓) *target: plea*
  > 2Ch 33:13 He prayed to him, and God was moved by his entreaty and heard his plea and brought him again to Jerusalem into his kingdom . Then Manasseh knew that the Lord was God .
- **Ezr 9:8** (✓) *target: favor*
  > Ezr 9:8 But now for a brief moment favor has been shown by the Lord our God , to leave us a remnant and to give us a secure hold within his holy place , that our God may brighten our eyes and grant us a little reviving in our slavery .
- **Psa 6:9** (✓) *target: plea*
  > Psa 6:9 The Lord has heard my plea ; the Lord accepts my prayer .
- **Psa 55:1** (✓) *target: mercy*
  > To the choirmaster : with stringed instruments . A Maskil of David . Psa 55:1 Give ear to my prayer , O God , and hide not yourself from my plea for mercy !
- **Psa 119:170** (✓) *target: plea*
  > Psa 119:170 Let my plea come before you; deliver me according to your word .
- **Jer 36:7** (✓) *target: plea for mercy*
  > Jer 36:7 It may be that their plea for mercy will come before the Lord , and that every one will turn from his evil way , for great is the anger and wrath that the Lord has pronounced against this people .”
- **Jer 42:2** (✓) *target: plea for mercy*
  > Jer 42:2 and said to Jeremiah the prophet , “ Let our plea for mercy come before you, and pray to the Lord your God for us, for all this remnant — because we are left with but a few , as your eyes see us —
- **Jer 42:9** (✓) *target: plea for mercy*
  > Jer 42:9 and said to them, “ Thus says the Lord , the God of Israel , to whom you sent me to present your plea for mercy before him:

**Group `985-002`** (3 verses — anchors: Jer 37:20)

- **Jer 37:20** 🔵 (✓) *target: humble plea*
  > Jer 37:20 Now hear , please , O my lord the king : let my humble plea come before you and do not send me back to the house of Jonathan the secretary , lest I die there .”
- **Jos 11:20** (✓) *target: mercy*
  > Jos 11:20 For it was the Lord’s doing to harden their hearts that they should come against Israel in battle , in order that they should be devoted to destruction and should receive no mercy but be destroyed , just as the Lord commanded Moses .
- **Jer 38:26** (✓) *target: humble plea*
  > Jer 38:26 then you shall say to them, ‘ I made a humble plea to the king that he would not send me back to the house of Jonathan to die there .’”

### `G0415` — 1/1 classified · 1 anchor verse(s)

**Group `3165-001`** (1 verse — anchors: Rom 1:31)

- **Rom 1:31** 🔵 (✓) *target: ruthless*
  > Rom 1:31 foolish , faithless , heartless , ruthless .

### `G0448` — 1/1 classified · 1 anchor verse(s)

**Group `993-001`** (1 verse — anchors: Jam 2:13)

- **Jam 2:13** 🔵 (✓) *target: mercy*
  > Jam 2:13 For judgment is without mercy to one who has shown no mercy . Mercy triumphs over judgment .

### `G0462` — 2/2 classified · 2 anchor verse(s)

**Group `3179-001`** (2 verses — anchors: 1Ti 1:9, 2Ti 3:2)

- **1Ti 1:9** 🔵 (✓) *target: unholy*
  > 1Ti 1:9 understanding this , that the law is not laid down for the just but for the lawless and disobedient , for the ungodly and sinners , for the unholy and profane , for those who strike their fathers and mothers , for murderers ,
- **2Ti 3:2** 🔵 (✓) *target: unholy*
  > 2Ti 3:2 For people will be lovers of self , lovers of money , proud , arrogant , abusive , disobedient to their parents , ungrateful , unholy ,

### `G1653` — 28/29 classified · 6 anchor verse(s)

**Group `981-001`** (12 verses — anchors: Rom 9:15, 1Pe 2:10)

- **Rom 9:15** 🔵 (✓) *target: mercy*
  > Rom 9:15 For he says to Moses , “I will have mercy on whom I have mercy , and I will have compassion on whom I have compassion .”
- **1Pe 2:10** 🔵 (✓) *target: mercy*
  > 1Pe 2:10 Once you were not a people , but now you are God’s people ; once you had not received mercy , but now you have received mercy .
- **Rom 9:16** (✓) *target: mercy*
  > Rom 9:16 So then it depends not on human will or exertion , but on God , who has mercy .
- **Rom 9:18** (✓) *target: mercy*
  > Rom 9:18 So then he has mercy on whomever he wills , and he hardens whomever he wills .
- **Rom 11:30** (✓) *target: mercy*
  > Rom 11:30 For just as you were at one time disobedient to God but now have received mercy because of their disobedience ,
- **Rom 11:31** (✓) *target: mercy*
  > Rom 11:31 so they too have now been disobedient in order that by the mercy shown to you they also may now receive mercy .
- **Rom 11:32** (✓) *target: mercy*
  > Rom 11:32 For God has consigned all to disobedience , that he may have mercy on all .
- **1Cor 7:25** (✓) *target: mercy*
  > 1Cor 7:25 Now concerning the betrothed , I have no command from the Lord , but I give my judgment as one who by the Lord’s mercy is trustworthy .
- **2Cor 4:1** (✓) *target: mercy*
  > 2Cor 4:1 Therefore , having this ministry by the mercy of God, we do not lose heart .
- **Phili 2:27** (✓) *target: mercy*
  > Phili 2:27 Indeed he was ill , near to death . But God had mercy on him , and not only on him but on me also , lest I should have sorrow upon sorrow .
  - notes: Dual-context verse
- **1Ti 1:13** (✓) *target: mercy*
  > 1Ti 1:13 though formerly I was a blasphemer , persecutor , and insolent opponent . But I received mercy because I had acted ignorantly in unbelief ,
- **1Ti 1:16** (✓) *target: mercy*
  > 1Ti 1:16 But I received mercy for this reason , that in me , as the foremost , Jesus Christ might display his perfect patience as an example to those who were to believe in him for eternal life .

**Group `981-002`** (11 verses — anchors: Mar 10:48, Luk 18:38)

- **Mar 10:48** 🔵 (✓) *target: mercy*
  > Mar 10:48 And many rebuked him , telling him to be silent . But he cried out all the more , “ Son of David , have mercy on me !”
- **Luk 18:38** 🔵 (✓) *target: mercy on*
  > Luk 18:38 And he cried out , “ Jesus , Son of David , have mercy on me !”
- **Mat 9:27** (✓) *target: mercy*
  > Mat 9:27 And as Jesus passed on from there , two blind men followed him , crying aloud , “Have mercy on us , Son of David .”
- **Mat 15:22** (✓) *target: mercy*
  > Mat 15:22 And behold , a Canaanite woman from that region came out and was crying , “Have mercy on me , O Lord , Son of David ; my daughter is severely oppressed by a demon .”
- **Mat 17:15** (✓) *target: mercy*
  > Mat 17:15 said , “ Lord , have mercy on my son , for he has seizures and he suffers terribly . For often he falls into the fire , and often into the water .
- **Mat 20:30** (✓) *target: mercy*
  > Mat 20:30 And behold , there were two blind men sitting by the roadside , and when they heard that Jesus was passing by , they cried out , “ Lord , have mercy on us , Son of David !”
- **Mat 20:31** (✓) *target: mercy*
  > Mat 20:31 The crowd rebuked them , telling them to be silent , but they cried out all the more , “ Lord , have mercy on us , Son of David !”
- **Mar 10:47** (✓) *target: mercy*
  > Mar 10:47 And when he heard that it was Jesus of Nazareth , he began to cry out and say , “ Jesus , Son of David , have mercy on me !”
- **Luk 16:24** (✓) *target: mercy*
  > Luk 16:24 And he called out , ‘ Father Abraham , have mercy on me , and send Lazarus to dip the end of his finger in water and cool my tongue , for I am in anguish in this flame .’
- **Luk 17:13** (✓) *target: mercy*
  > Luk 17:13 and lifted up their voices , saying , “ Jesus , Master , have mercy on us .”
- **Luk 18:39** (✓) *target: mercy on*
  > Luk 18:39 And those who were in front rebuked him, telling him to be silent . But he cried out all the more , “ Son of David , have mercy on me !”

**Group `981-003`** (5 verses — anchors: Mat 5:7, Mat 18:33)

- **Mat 5:7** 🔵 (✓) *target: mercy*
  > Mat 5:7 “ Blessed are the merciful , for they shall receive mercy .
- **Mat 18:33** 🔵 (✓) *target: mercy*
  > Mat 18:33 And should not you have had mercy on your fellow servant , as I had mercy on you ?’
- **Rom 12:8** (✓) *target: mercy*
  > Rom 12:8 the one who exhorts , in his exhortation ; the one who contributes , in generosity ; the one who leads , with zeal ; the one who does acts of mercy , with cheerfulness .
- **Phili 2:27** (✓) *target: mercy*
  > Phili 2:27 Indeed he was ill , near to death . But God had mercy on him , and not only on him but on me also , lest I should have sorrow upon sorrow .
  - notes: Dual-context verse
- **Jude 22** (✓) *target: mercy*
  > Jude 22 And have mercy on those who doubt ;

**Group `UNCLASSIFIED`** (1 verse)

- **Mar 5:19** (—) *target: mercy*
  > Mar 5:19 And he did not permit him but said to him , “ Go home to your friends and tell them how much the Lord has done for you , and how he has had mercy on you .”

### `G1655` — 2/2 classified · 2 anchor verse(s)

**Group `3164-001`** (2 verses — anchors: Mat 5:7, Heb 2:17)

- **Mat 5:7** 🔵 (✓) *target: merciful*
  > Mat 5:7 “ Blessed are the merciful , for they shall receive mercy .
- **Heb 2:17** 🔵 (✓) *target: merciful*
  > Heb 2:17 Therefore he had to be made like his brothers in every respect, so that he might become a merciful and faithful high priest in the service of God , to make propitiation for the sins of the people .

### `G1656` — 27/27 classified · 4 anchor verse(s)

**Group `983-001`** (14 verses — anchors: Luk 1:78, Eph 2:4)

- **Luk 1:78** 🔵 (✓) *target: mercy*
  > Luk 1:78 because of the tender mercy of our God , whereby the sunrise shall visit us from on high
- **Eph 2:4** 🔵 (✓) *target: mercy*
  > Eph 2:4 But God , being rich in mercy , because of the great love with which he loved us ,
- **Luk 1:50** (✓) *target: mercy*
  > Luk 1:50 And his mercy is for those who fear him from generation to generation .
- **Luk 1:54** (✓) *target: mercy*
  > Luk 1:54 He has helped his servant Israel , in remembrance of his mercy ,
- **Luk 1:58** (✓) *target: mercy*
  > Luk 1:58 And her neighbors and relatives heard that the Lord had shown great mercy to her , and they rejoiced with her .
- **Luk 1:72** (✓) *target: mercy*
  > Luk 1:72 to show the mercy promised to our fathers and to remember his holy covenant ,
- **Luk 10:37** (✓) *target: mercy*
  > Luk 10:37 He said , “The one who showed him mercy .” And Jesus said to him , “ You go , and do likewise .”
  - notes: Dual-context verse
- **Rom 9:23** (✓) *target: mercy*
  > Rom 9:23 in order to make known the riches of his glory for vessels of mercy , which he has prepared beforehand for glory —
- **Rom 11:31** (✓) *target: mercy*
  > Rom 11:31 so they too have now been disobedient in order that by the mercy shown to you they also may now receive mercy .
- **Rom 15:9** (✓) *target: mercy*
  > Rom 15:9 and in order that the Gentiles might glorify God for his mercy . As it is written , “ Therefore I will praise you among the Gentiles , and sing to your name .”
- **Gal 6:16** (✓) *target: mercy*
  > Gal 6:16 And as for all who walk by this rule , peace and mercy be upon them , and upon the Israel of God .
- **Tit 3:5** (✓) *target: mercy*
  > Tit 3:5 he saved us , not because of works done by us in righteousness , but according to his own mercy , by the washing of regeneration and renewal of the Holy Spirit ,
- **1Pe 1:3** (✓) *target: mercy*
  > 1Pe 1:3 Blessed be the God and Father of our Lord Jesus Christ ! According to his great mercy , he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead ,
- **Jude 21** (✓) *target: mercy*
  > Jude 21 keep yourselves in the love of God , waiting for the mercy of our Lord Jesus Christ that leads to eternal life .

**Group `983-002`** (13 verses — anchors: Mat 23:23, Jam 3:17)

- **Mat 23:23** 🔵 (✓) *target: mercy*
  > Mat 23:23 “ Woe to you , scribes and Pharisees , hypocrites ! For you tithe mint and dill and cumin , and have neglected the weightier matters of the law : justice and mercy and faithfulness . These you ought to have done , without neglecting the others .
- **Jam 3:17** 🔵 (✓) *target: mercy*
  > Jam 3:17 But the wisdom from above is first pure , then peaceable , gentle , open to reason , full of mercy and good fruits , impartial and sincere .
- **Mat 9:13** (✓) *target: mercy*
  > Mat 9:13 Go and learn what this means : ‘I desire mercy , and not sacrifice .’ For I came not to call the righteous , but sinners .”
- **Mat 12:7** (✓) *target: mercy*
  > Mat 12:7 And if you had known what this means , ‘I desire mercy , and not sacrifice ,’ you would not have condemned the guiltless .
- **Luk 10:37** (✓) *target: mercy*
  > Luk 10:37 He said , “The one who showed him mercy .” And Jesus said to him , “ You go , and do likewise .”
  - notes: Dual-context verse
- **1Ti 1:2** (✓) *target: mercy*
  > 1Ti 1:2 To Timothy , my true child in the faith : Grace , mercy , and peace from God the Father and Christ Jesus our Lord .
- **2Ti 1:2** (✓) *target: mercy*
  > 2Ti 1:2 To Timothy , my beloved child : Grace , mercy , and peace from God the Father and Christ Jesus our Lord .
- **2Ti 1:16** (✓) *target: mercy*
  > 2Ti 1:16 May the Lord grant mercy to the household of Onesiphorus , for he often refreshed me and was not ashamed of my chains ,
- **2Ti 1:18** (✓) *target: mercy*
  > 2Ti 1:18 may the Lord grant him to find mercy from the Lord on that day !— and you well know all the service he rendered at Ephesus .
- **Heb 4:16** (✓) *target: mercy*
  > Heb 4:16 Let us then with confidence draw near to the throne of grace , that we may receive mercy and find grace to help in time of need .
- **Jam 2:13** (✓) *target: mercy*
  > Jam 2:13 For judgment is without mercy to one who has shown no mercy . Mercy triumphs over judgment .
- **2Jo 3** (✓) *target: mercy*
  > 2Jo 3 Grace , mercy , and peace will be with us , from God the Father and from Jesus Christ the Father’s Son , in truth and love .
- **Jude 2** (✓) *target: mercy*
  > Jude 2 May mercy , peace , and love be multiplied to you .

### `G2433` — 2/2 classified · 2 anchor verse(s)

**Group `3176-001`** (2 verses — anchors: Luk 18:13, Heb 2:17)

- **Luk 18:13** 🔵 (✓) *target: merciful*
  > Luk 18:13 But the tax collector , standing far off , would not even lift up his eyes to heaven , but beat his breast , saying , ‘ God , be merciful to me , a sinner !’
- **Heb 2:17** 🔵 (✓) *target: propitiation for*
  > Heb 2:17 Therefore he had to be made like his brothers in every respect, so that he might become a merciful and faithful high priest in the service of God , to make propitiation for the sins of the people .

### `G2434` — 2/2 classified · 2 anchor verse(s)

**Group `3177-001`** (2 verses — anchors: 1Jo 2:2, 1Jo 4:10)

- **1Jo 2:2** 🔵 (✓) *target: propitiation*
  > 1Jo 2:2 He is the propitiation for our sins , and not for ours only but also for the sins of the whole world .
- **1Jo 4:10** 🔵 (✓) *target: propitiation*
  > 1Jo 4:10 In this is love , not that we have loved God but that he loved us and sent his Son to be the propitiation for our sins .

### `G2435` — 2/2 classified · 2 anchor verse(s)

**Group `991-001`** (2 verses — anchors: Rom 3:25, Heb 9:5)

- **Rom 3:25** 🔵 (✓) *target: propitiation*
  > Rom 3:25 whom God put forward as a propitiation by his blood , to be received by faith . This was to show God’s righteousness , because in his divine forbearance he had passed over former sins .
- **Heb 9:5** 🔵 (✓) *target: mercy seat*
  > Heb 9:5 Above it were the cherubim of glory overshadowing the mercy seat . Of these things we cannot now speak in detail .

### `G2436` — 2/2 classified · 1 anchor verse(s)

**Group `3166-001`** (2 verses — anchors: Heb 8:12)

- **Heb 8:12** 🔵 (✓) *target: merciful*
  > Heb 8:12 For I will be merciful toward their iniquities , and I will remember their sins no more .”
- **Mat 16:22** (✓) *target: Far be it*
  > Mat 16:22 And Peter took him aside and began to rebuke him , saying , “ Far be it from you , Lord ! This shall never happen to you .”

### `G3628` — 5/5 classified · 2 anchor verse(s)

**Group `992-001`** (5 verses — anchors: 2Cor 1:3, Col 3:12)

- **2Cor 1:3** 🔵 (✓) *target: mercies*
  > 2Cor 1:3 Blessed be the God and Father of our Lord Jesus Christ , the Father of mercies and God of all comfort ,
- **Col 3:12** 🔵 (✓) *target: compassionate*
  > Col 3:12 Put on then , as God’s chosen ones , holy and beloved , compassionate hearts , kindness , humility , meekness , and patience ,
- **Rom 12:1** (✓) *target: mercies*
  > Rom 12:1 I appeal to you therefore , brothers , by the mercies of God , to present your bodies as a living sacrifice , holy and acceptable to God , which is your spiritual worship .
- **Phili 2:1** (✓) *target: sympathy*
  > Phili 2:1 So if there is any encouragement in Christ , any comfort from love , any participation in the Spirit , any affection and sympathy ,
- **Heb 10:28** (✓) *target: mercy*
  > Heb 10:28 Anyone who has set aside the law of Moses dies without mercy on the evidence of two or three witnesses .

### `G3629` — 2/2 classified · 2 anchor verse(s)

**Group `3158-001`** (2 verses — anchors: Luk 6:36, Jam 5:11)

- **Luk 6:36** 🔵 (✓) *target: merciful*
  > Luk 6:36 Be merciful , even as your Father is merciful .
- **Jam 5:11** 🔵 (✓) *target: merciful*
  > Jam 5:11 Behold , we consider those blessed who remained steadfast . You have heard of the steadfastness of Job , and you have seen the purpose of the Lord , how the Lord is compassionate and merciful .

### `G3743` — 1/1 classified · 1 anchor verse(s)

**Group `3181-001`** (1 verse — anchors: 1Th 2:10)

- **1Th 2:10** 🔵 (✓) *target: holy*
  > 1Th 2:10 You are witnesses , and God also, how holy and righteous and blameless was our conduct toward you believers .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**25 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H2603A` | be gracious | `to_revise` | 72 | 1 | 71 |
| `H2604` | be gracious | `to_revise` | 2 | 1 | 2 |
| `H3722A` | to atone | `to_revise` | 93 | 3 | 81 |
| `H3722B` | to cover | `to_revise` | 93 | 3 | 81 |
| `H3724A` | ransom | `to_revise` | 13 | 2 | 13 |
| `H3725` | atonement | `to_revise` | 8 | 1 | 8 |
| `H3727` | mercy seat | `to_revise` | 22 | 1 | 22 |
| `H3819` | No Mercy | `to_revise` | 2 | 1 | 2 |
| `H5750` | still | `to_revise` | 170 | 2 | 14 |
| `H6279` | to pray | `to_revise` | 19 | 2 | 19 |
| `H7359` | compassion | `to_revise` | 1 | 1 | 1 |
| `H8467` | supplication | `to_revise` | 24 | 2 | 24 |
| `G0415` | merciless | `to_revise` | 1 | 1 | 1 |
| `G0448` | merciless | `to_revise` | 1 | 1 | 1 |
| `G0462` | unholy | `to_revise` | 2 | 1 | 2 |
| `G1653` | to have mercy | `to_revise` | 28 | 3 | 28 |
| `G1655` | merciful | `to_revise` | 2 | 1 | 2 |
| `G1656` | mercy | `to_revise` | 26 | 2 | 27 |
| `G2433` | to propitiate | `to_revise` | 2 | 1 | 2 |
| `G2434` | propitiation | `to_revise` | 2 | 1 | 2 |
| `G2435` | propitiation | `to_revise` | 2 | 1 | 2 |
| `G2436` | propitious/gracious | `to_revise` | 2 | 1 | 2 |
| `G3628` | compassion | `to_revise` | 5 | 1 | 5 |
| `G3629` | compassionate | `to_revise` | 2 | 1 | 2 |
| `G3743` | devoutly | `to_revise` | 1 | 1 | 1 |

---

## L. Stage 2b Foundational Input — Observation Question Catalogue

**Generic questions: 158** across 11 sections. The section grouping IS the Stage 2b chapter structure — Stage 2b works through the catalogue section-by-section, producing answers grouped by section.

### Section summary (generic)

| Section | n questions |
|---|---:|
| Section 1 — Generic (gap addition R067 obslog v3) | 3 |
| Section 1 — Generic (gap addition R067) | 2 |
| Section 1 — Word Characteristic Summary | 20 |
| Section 2 — Generic (gap addition R067) | 2 |
| Section 2 — Word Impact Description | 21 |
| Section 3 — Annotated Verse Evidence | 44 |
| Section 3 — Generic (gap addition R067) | 2 |
| Section 4 — Generic (gap addition R067) | 1 |
| Section 4 — Original Language Vocabulary | 36 |
| Section 5 — Connections and Research Pointers | 26 |
| Section 5 — Generic (gap addition R067) | 1 |

### Generic questions (JSON, grouped by section)

Format: JSON. Structure: as-is from `wa_obs_question_catalogue`. Apply to every word.

```json
{
  "total": 158,
  "section_count": 11,
  "sections": {
    "Section 1 — Generic (gap addition R067 obslog v3)": [
      {
        "obs_id": 221,
        "question_code": "GAP-N-001",
        "section": "Section 1 — Generic (gap addition R067 obslog v3)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "For registries where verse context groups carry affective inner-being states (gladness, well-being, shalom-condition) that do not fit Moral Character, Cognition, or Volition, what dimension should be assigned? The current 10-dimension vocabulary may require an Experiential/Affective category for these groups.",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 222,
        "question_code": "GAP-N-002",
        "section": "Section 1 — Generic (gap addition R067 obslog v3)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "For verse context groups that name inner affective well-being states (glad of heart, shalom-condition, prospering inwardly) that are not primarily moral assessments, cognitive evaluations, or volitional acts, should the dimension be Emotion — Positive or Vitality / Existence? The two dimensions need clearer boundary criteria for these borderline cases.",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 223,
        "question_code": "GAP-N-003",
        "section": "Section 1 — Generic (gap addition R067 obslog v3)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "For verse context groups where God's inner-being engagement is a creative-constitutive evaluative act (declaring creation good, establishing ontological goodness) rather than a relational disposition toward humanity, should Dimension 11 (Divine-Human Correspondence) apply, or should the dimension review introduce a distinct label for this ontological-creative register?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 1 — Generic (gap addition R067)": [
      {
        "obs_id": 207,
        "question_code": "GAP-S1-001",
        "section": "Section 1 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where the word has multiple distinct semantic modes, does the verse evidence reveal a unified inner logic that holds the modes together — or are they genuinely independent phenomena?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 208,
        "question_code": "GAP-S1-002",
        "section": "Section 1 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Does the word carry a structural negative or absence form — and if so, does the negative form engage the same inner-being faculty as the positive?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 1 — Word Characteristic Summary": [
      {
        "obs_id": 1,
        "question_code": "Q001",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the structural disposition of the word — where does it originate?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 2,
        "question_code": "Q002",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What determines whether the word is extended or withheld?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 3,
        "question_code": "Q003",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What are the distinct modes of operation of the word in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 4,
        "question_code": "Q004",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word produce in the inner being of the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 5,
        "question_code": "Q005",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word produce in the relational position of the recipient toward another?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 6,
        "question_code": "Q006",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the disposition of God toward the human being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 7,
        "question_code": "Q007",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the basis on which God's disposition toward a person is established?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 8,
        "question_code": "Q008",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where, somatically or relationally, does the word locate the reality of its operation in the giver and in the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 9,
        "question_code": "Q009",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word describe a one-time act or an ongoing condition — and how are these distinguished?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 10,
        "question_code": "Q010",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What spatial or directional language is used to describe the ongoing condition the word produces?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 11,
        "question_code": "Q011",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word produce enabling capacity in the inner being — and if so, what kind?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 12,
        "question_code": "Q012",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What character quality does the word produce in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 13,
        "question_code": "Q013",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the word express itself in relation to others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 14,
        "question_code": "Q014",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner condition or orientation is identified as the ground of genuine expression of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 15,
        "question_code": "Q015",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Is there a discernible sequence or movement in the way the word operates through the inner person?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 16,
        "question_code": "Q016",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What direction of movement does the word follow within and through the inner person?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 17,
        "question_code": "Q017",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word identify as its originating source?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 18,
        "question_code": "Q018",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the origin of the human capacity to seek it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 19,
        "question_code": "Q019",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word share an etymological root with another inner-being characteristic — and if so, what is that characteristic?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 20,
        "question_code": "Q020",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word produce as a natural inner response in the one who receives it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 2 — Generic (gap addition R067)": [
      {
        "obs_id": 209,
        "question_code": "GAP-S2-001",
        "section": "Section 2 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where the word has both a positive (presence) and negative (absence/not-word) register, what does the negative register reveal about the inner-being mechanisms of the positive?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 210,
        "question_code": "GAP-S2-002",
        "section": "Section 2 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Does the verse evidence distinguish between the inner quality of goodness and the external assessment of conduct as good — and what is the relationship between them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 2 — Word Impact Description": [
      {
        "obs_id": 21,
        "question_code": "Q021",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being logic or orientation functions as the structural opposite of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 22,
        "question_code": "Q022",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What effect does the logic of merit have on the inner being's capacity to receive the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 23,
        "question_code": "Q023",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What effect does the logic of merit have on the inner being's capacity to extend the word to others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 24,
        "question_code": "Q024",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the inner-being condition of the person who has received the word but failed to recognise it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 25,
        "question_code": "Q025",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being experience cultivates the capacity to extend the word to others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 26,
        "question_code": "Q026",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being posture does the act of earnest appeal express?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 27,
        "question_code": "Q027",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What somatic forms does the inner act of seeking the word take?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 28,
        "question_code": "Q028",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being orientation closes off the reception of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 29,
        "question_code": "Q029",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What relational orientation toward others diminishes the operation of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 30,
        "question_code": "Q030",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between the word and conditions of weakness in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 31,
        "question_code": "Q031",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What kind of inner-being transformation does the word produce — does it change the condition or the person's orientation to the condition?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 32,
        "question_code": "Q032",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the first inner-being response to receiving the word unexpectedly?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 33,
        "question_code": "Q033",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the sequence of inner-being states as the word takes hold in the person?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 34,
        "question_code": "Q034",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "In the eschatological context, what is the first inner-being response to the full outpouring of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 35,
        "question_code": "Q035",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between mourning and the full reception of the word in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 36,
        "question_code": "Q036",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What quality of inner-being stability does the word produce?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 37,
        "question_code": "Q037",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What orientation does the stability produced by the word carry?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 38,
        "question_code": "Q038",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What capacity toward others does the word produce in the inner being of the one who has received it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 39,
        "question_code": "Q039",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the inner-being source of the capacity to extend the word to others — is it discipline or transformation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 40,
        "question_code": "Q040",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the word relate to genuine human effort — does it displace it, supplement it, or reconstitute it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 41,
        "question_code": "Q041",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the inner-being condition of the person who does not receive it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 3 — Annotated Verse Evidence": [
      {
        "obs_id": 42,
        "question_code": "Q042",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word's primary verse reveal about its essential character?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 43,
        "question_code": "Q043",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the primary verse identify as the relationship between the human version and the divine version of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 44,
        "question_code": "Q044",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the primary verse identify as the primary subject of the word — who exercises it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 45,
        "question_code": "Q045",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the primary verse name more than one function or dimension of the word — and if so, what is the relationship between them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 46,
        "question_code": "Q046",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the primary verse reveal about the breadth of those toward whom the word operates?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 47,
        "question_code": "Q047",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the direction of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 48,
        "question_code": "Q048",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the word's relationship to suffering or affliction?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 49,
        "question_code": "Q049",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the word's relationship to moral failure or guilt?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 50,
        "question_code": "Q050",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the word's relationship to covenantal relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 51,
        "question_code": "Q051",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What reason does a key verse give for the extension of the word — in the recipient's actions, or in the character of the one who gives it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 52,
        "question_code": "Q052",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where does a key verse locate the reality of the word — in a specific faculty, organ, or location of the giver?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 53,
        "question_code": "Q053",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What practical outcome does a key verse show the word producing for the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 54,
        "question_code": "Q054",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner state does a key verse identify as the first response to receiving the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 55,
        "question_code": "Q055",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What comes first in a key verse — the establishment of the relationship or standing the word confers, or the commission or responsibility that follows from it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 56,
        "question_code": "Q056",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a key verse identify as the concrete content of what the word gives?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 57,
        "question_code": "Q057",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What spatial or directional language does a key verse use for the reality of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 58,
        "question_code": "Q058",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse distinguish between the means of entry into the word and the condition the word produces?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 59,
        "question_code": "Q059",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse describe the present condition produced by the word as carrying a forward orientation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 60,
        "question_code": "Q060",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a key verse identify as the ground of the speaker's or recipient's identity — achievement, reception, or something else?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 61,
        "question_code": "Q061",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does a key verse handle the co-presence of genuine human effort and prior divine initiative?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 62,
        "question_code": "Q062",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "In what form does a key verse present the word — and what does that form enable?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 63,
        "question_code": "Q063",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What effect does the word in communicative form produce in those who receive it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 64,
        "question_code": "Q064",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does a key verse describe the word's work as directed toward the present only, or toward a future state?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 65,
        "question_code": "Q065",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse distinguish between a performed version and a genuine version of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 66,
        "question_code": "Q066",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner orientation does a key verse identify as the source of the genuine quality?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 67,
        "question_code": "Q067",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the sequence of somatic and verbal response in a key verse — which comes first?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 68,
        "question_code": "Q068",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a recipient's response in a key verse reveal about their inner experience of receiving the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 69,
        "question_code": "Q069",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What structural condition in a key verse establishes the recipient as having no basis for the word they receive?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 70,
        "question_code": "Q070",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "In a key verse, does the word operate within or across existing relational, covenantal, or social boundaries?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 71,
        "question_code": "Q071",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the logical structure of a key argument about the word — and what is its premise and conclusion?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 72,
        "question_code": "Q072",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being state does the argument structure in a key verse produce in the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 73,
        "question_code": "Q073",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between the divine act and the human act in a key verse — illustrative or causal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 74,
        "question_code": "Q074",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where does a key verse locate the inner quality from which the word's outward act flows?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 75,
        "question_code": "Q075",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the withdrawal or absence of the word reveal about the word's role?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 76,
        "question_code": "Q076",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in extremity reveal about its depth of operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 77,
        "question_code": "Q077",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the judicial or accountability context reveal about its function?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 78,
        "question_code": "Q078",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the supplication context reveal about what the inner person knows about itself?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 79,
        "question_code": "Q079",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the worship or liturgical context reveal about the word's function in ordered relationship with God?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 80,
        "question_code": "Q080",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word at the level of covenantal promise reveal about its scope and duration?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 81,
        "question_code": "Q081",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of moral collapse reveal about the word's place in the structure of the inner life?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 82,
        "question_code": "Q082",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of formation or sanctification reveal about how the word shapes the person over time?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 83,
        "question_code": "Q083",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of community or fellowship reveal about the word's social dimension?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 84,
        "question_code": "Q084",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of eschatology or final things reveal about the word's ultimate trajectory?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 85,
        "question_code": "Q085",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word's physical or somatic expression reveal about the inner-outer relationship in the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 3 — Generic (gap addition R067)": [
      {
        "obs_id": 211,
        "question_code": "GAP-S3-001",
        "section": "Section 3 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where a registry contains multiple anchor verses across multiple groups, is there a primary or controlling anchor — and how is it identified?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 212,
        "question_code": "GAP-S3-002",
        "section": "Section 3 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Does the comparative or evaluative mode of the word (where the word functions as a ranking operator rather than naming a characteristic) constitute a distinct analytical case requiring separate treatment?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 4 — Generic (gap addition R067)": [
      {
        "obs_id": 213,
        "question_code": "GAP-S4-001",
        "section": "Section 4 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where the programme has distributed a root family across multiple registries, what does that distribution reveal about the programme's analytical framework, and does the distribution reflect genuine semantic distinctions or is it a programme boundary decision requiring Session D review?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 4 — Original Language Vocabulary": [
      {
        "obs_id": 86,
        "question_code": "Q086",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the total number of terms in this registry, and how are they distributed between Hebrew and Greek?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 87,
        "question_code": "Q087",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the sharing ratio — what proportion of terms are shared with adjacent word studies?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 88,
        "question_code": "Q088",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the primary Hebrew term, and what does its root meaning reveal about the word's essential character?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 89,
        "question_code": "Q089",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the primary Greek term, and what does its range of use reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 90,
        "question_code": "Q090",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary distinguish between the word as an inner disposition and the word as an outward act — and how?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 91,
        "question_code": "Q091",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the word as a settled character quality?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 92,
        "question_code": "Q092",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the one who habitually exercises the word — a person-type term?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 93,
        "question_code": "Q093",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the word's absence or structural opposite?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 94,
        "question_code": "Q094",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the relationship between the root meaning and the primary sense reveal about the word's conceptual origin?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 95,
        "question_code": "Q095",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include terms that name the word as something received passively and terms that name it as something actively exercised?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 96,
        "question_code": "Q096",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term in the vocabulary carry both the sense of the word in its human expression and its divine expression?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 97,
        "question_code": "Q097",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the LXX use of the vocabulary reveal about the continuity or development of the word across the Testaments?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 98,
        "question_code": "Q098",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Is there a named failure-mode term in the vocabulary — a term for the person who has received the word but withholds it from others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 99,
        "question_code": "Q099",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term newly coined in the NT period for this word — and if so, what does the coinage reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 100,
        "question_code": "Q100",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verbal form of the primary term reveal about the word's mode of operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 101,
        "question_code": "Q101",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a spatial or architectural term — a place or structure associated with the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 102,
        "question_code": "Q102",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the semantic range of the primary term reveal about the breadth of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 103,
        "question_code": "Q103",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term carry a somatic or physiological dimension — naming an inner organ or physical site as the word's location?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 104,
        "question_code": "Q104",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the grammatical range of the primary term (noun, verb, adjective) reveal about how the word is conceptualised — as object, action, or quality?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 105,
        "question_code": "Q105",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a supplication term — a term for the act of seeking the word from another?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 106,
        "question_code": "Q106",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the supplication term reveal about the inner posture required to seek the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 107,
        "question_code": "Q107",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the mechanism by which the word is administered or conveyed?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 108,
        "question_code": "Q108",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the atonement or propitiation vocabulary (if present) reveal about the structural conditions under which the word operates?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 109,
        "question_code": "Q109",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term reveal a classical-to-NT directional reversal — a term whose direction of operation changes between its classical use and its NT use?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 110,
        "question_code": "Q110",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the vocabulary reveal about whether the word operates primarily within or across relational boundaries?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 111,
        "question_code": "Q111",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the vocabulary reveal about the word's relationship to covenant — is it bounded by covenant or can it extend beyond?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 112,
        "question_code": "Q112",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term in the vocabulary name the word as a divine possession — something that belongs to God and is located with him?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 113,
        "question_code": "Q113",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the root architecture of the vocabulary reveal about the word's conceptual relationship to adjacent characteristics?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 114,
        "question_code": "Q114",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include compound terms — and if so, what do the compounds reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 115,
        "question_code": "Q115",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the vocabulary reveal about the word's temporal character — is it punctiliar, durative, or both?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 116,
        "question_code": "Q116",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary reveal whether the word operates as a judicial category, a relational one, or both?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 117,
        "question_code": "Q117",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the most intensive or plural form of the vocabulary term reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 118,
        "question_code": "Q118",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include terms that name the word's expression in speech?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 119,
        "question_code": "Q119",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include terms whose etymology connects to the body — and if so, to which part?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 120,
        "question_code": "Q120",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the full vocabulary arc reveal about the word's complete semantic range — from its most intimate to its most structural expression?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 121,
        "question_code": "Q121",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term that names the word's operation at the intersection of the human and divine — a term that holds both simultaneously?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 5 — Connections and Research Pointers": [
      {
        "obs_id": 122,
        "question_code": "Q122",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the strongest co-occurrence connection for this word — which adjacent characteristic appears most frequently in the same verses — and what does the co-occurrence pattern reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 123,
        "question_code": "Q123",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse indicate that this word and its most closely connected adjacent characteristic operate simultaneously in the same inner-being moment — and what would that simultaneity imply?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 124,
        "question_code": "Q124",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What are the three highest vocabulary-sharing registries for this word — and what does the pattern of sharing reveal about the word's structural position in the programme?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 125,
        "question_code": "Q125",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary overlap with any adjacent characteristic extend to root-level architecture — a shared root rather than only shared individual terms?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 126,
        "question_code": "Q126",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How many of this word's confirmed analytical dimensions are shared with another cluster or characteristic — and is there any cluster that shares all confirmed dimensions?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 127,
        "question_code": "Q127",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any single verse make an explicit structural relationship between this word and an adjacent characteristic — naming the connection rather than merely exemplifying it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 128,
        "question_code": "Q128",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the co-occurrence count between this word and the characteristic with which it shares the most anchor verses — and what does that shared anchoring reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 129,
        "question_code": "Q129",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where this word and an adjacent characteristic share a dominant directionality (such as both being primarily divine-to-human), what does the shared directionality reveal about their structural relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 130,
        "question_code": "Q130",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between this word and human will in the verse evidence — does the word displace, bypass, or reconstitute the will?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 131,
        "question_code": "Q131",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the study describe the relationship between this word and calling — is calling a consequence, an expression, or a distinct phenomenon?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 132,
        "question_code": "Q132",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being posture connects this word and listening — and is that posture described as a precondition or an expression of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 133,
        "question_code": "Q133",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the study distinguish this word from faith — and what is their structural relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 134,
        "question_code": "Q134",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the described sequence from the word to peace — and what comes between them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 135,
        "question_code": "Q135",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the vocabulary overlap and co-occurrence count between this word and guilt?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 136,
        "question_code": "Q136",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between this word and mourning — does mourning precede, follow, or accompany the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 137,
        "question_code": "Q137",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the study present this word and hope as two separate phenomena or as aspects of a single inner-being posture?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 138,
        "question_code": "Q138",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse function as a primary anchor in both this word's study and another word's study — and what does that dual membership reveal about their relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 139,
        "question_code": "Q139",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse anchor both this word and another word — and what shared inner-being posture does that dual anchoring reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 140,
        "question_code": "Q140",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse present adjacent qualities as aspects of a unified inner-being posture — and if so, what is their common source?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 141,
        "question_code": "Q141",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What functional overlap does the verse evidence suggest between this word and wisdom?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 142,
        "question_code": "Q142",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word operate only in relation to moral conditions (guilt) or also in relation to conditions of incapacity — and what is the evidence?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 143,
        "question_code": "Q143",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the co-occurrence count between this word and goodness — and in what literary context does the pairing appear?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 144,
        "question_code": "Q144",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the co-occurrence count between this word and anointing, and between this word and blessing?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 145,
        "question_code": "Q145",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Is the connection between this word and forgiveness established through contextual inference or through the lexical form of the term itself?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 146,
        "question_code": "Q146",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the verse evidence in this study point toward a connection with repentance — and is that connection sufficiently examined or deferred?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 147,
        "question_code": "Q147",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does a recurring posture appear across the word-seeking scenes in the study — and is its relationship to an adjacent characteristic examined or deferred?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 5 — Generic (gap addition R067)": [
      {
        "obs_id": 214,
        "question_code": "GAP-S5-001",
        "section": "Section 5 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where a registry's word functions in more than one dimension (both as a character attribute and as a comparative/evaluative operator), does the co-occurrence and correlation data reveal different connection patterns for different modes of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ]
  }
}
```

### Registry-specific questions for 111 mercy

**11 question(s)** sourced from this registry's prior work. Include in Stage 2b alongside the generic questions.

```json
{
  "registry_no": 111,
  "registry_word": "mercy",
  "total": 11,
  "questions": [
    {
      "obs_id": 176,
      "question_code": "M-001",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "How does the word distinguish itself from its nearest near-synonym — what is the threshold or constitutive difference between them?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 177,
      "question_code": "M-002",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Does the word require a structural asymmetry between giver and receiver — is the positional difference (greater-to-lesser, strong-to-weak) a precondition of the word's operation, or can it operate between equals?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 178,
      "question_code": "M-003",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "At what level of the inner being is the word received, and at what level is it expressed — does the word follow a named pathway through the spirit-soul-body structure?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 179,
      "question_code": "M-004",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Is the absence of the word described as a diminishment of what it means to be human — is the word presented as constitutive of humanness rather than merely as a virtue the human person may or may not possess?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 180,
      "question_code": "M-005",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Does the word produce a pastoral capacity in the one who has received it — a specific capacity to minister to others in the condition in which the person themselves was once ministered to?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 181,
      "question_code": "M-006",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Has the word been given an architectural or material realisation in Israel's worship — a physical structure in which the word is spatially located — and if so, what does that materialisation reveal about the word's character and the nature of access to it?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 182,
      "question_code": "M-007",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Does the word share its structural logic (such as gratuitousness or disproportionality) with an apparently contrary reality — does the same principle that governs the word also appear in something that seems to contradict it?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 183,
      "question_code": "M-008",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Does the word's operation involve the face — as the site of favour, judgment, recognition, or relational access — and what does that face-language reveal about the inner-outer structure of the word?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 184,
      "question_code": "M-009",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "What is the causal relationship between the word as an inner disposition and the structural mechanism through which it operates — does the disposition produce the mechanism, or does the mechanism produce the disposition?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 185,
      "question_code": "M-010",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "What does a documented directional reversal in a key vocabulary term reveal about the word's theological significance — what claim about the nature of the divine-human relationship is encoded in the reversal?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 186,
      "question_code": "M-011",
      "section": "Mercy Extensions",
      "source_word": "Mercy",
      "source_registry_no": 111,
      "question_text": "Does the word's operation traverse all three levels of the inner being — spirit, soul, and body — and if so, what is the function at each level?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    }
  ]
}
```

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-04-28T06:25:08Z`
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

*End of readiness output v3 — wa-111-mercy.*