# wa-034-covenant — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-05-01T09:47:16Z · schema 3.17.0_

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

- **Registry no:** `34` · **word:** `covenant`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v1.9-2026-04-09`)
- **cluster_assignment:** `C17`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Relational/Social`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 60  (programme-wide aggregate including XREF and historical terms — current OWNER count is 15, XREF 4)
- `phase1_verse_count`: 2140  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 6 unresolved · **Existing session_b_findings:** 1

**Description:**

> Covenant is the binding agreement that structures the relationship between God and his people — not a contract between equals but a formal, solemn bond in which God commits himself to his people and calls them to commitment in return. The Hebrew vocabulary is built around the cutting of a covenant, which alludes to the ancient practice of walking through divided animals to seal a promise. Covenant is the backbone of the biblical narrative: creation, fall, Abraham, Moses, David, and the new covenant in Christ are all covenant events.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-01T09:47:16Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 15
- **OWNER terms legacy-VC (not_done):** 15 / 15

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 15 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H0423` | a.lah | oath | H | `extracted` | **`not_done`** | 1 | 14 | 2/0 | 14/0 | 2 |
| `H0548` | a.ma.nah | sure | H | `extracted_thin` | **`not_done`** | 1 | 2 | 1/0 | 1/0 | 1 |
| `H1285` | be.rit | covenant | H | `extracted` | **`not_done`** | 1 | 236 | 5/0 | 161/0 | 5 |
| `H1286` | be.rit | [Baal]-berith | H | `extracted_thin` | **`not_done`** | 1 | 1 | 0/0 | 0/0 | 0 |
| `H3748` | ke.ri.tut | divorce | H | `extracted_thin` | **`not_done`** | 1 | 4 | 2/0 | 4/0 | 2 |
| `H3772G` | ka.rat | to cut: cut | H | `extracted` | **`not_done`** | 1 | 50 | 2/0 | 5/0 | 2 |
| `H3772H` | ka.rat | to cut: make [covenant] | H | `extracted` | **`not_done`** | 1 | 87 | 4/0 | 85/0 | 4 |
| `H3772J` | ka.rat | to cut: lack | H | `extracted_thin` | **`not_done`** | 1 | 10 | 1/0 | 9/0 | 1 |
| `H7620I` | sha.vu.a | week | H | `extracted_thin` | **`not_done`** | 1 | 6 | 2/0 | 6/0 | 2 |
| `H7650` | sha.va | to swear | H | `extracted` | **`not_done`** | 1 | 175 | 4/0 | 131/0 | 4 |
| `G0802` | asunthetos | untrustworthy | G | `extracted_thin` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G1242` | diathēkē | covenant | G | `extracted` | **`not_done`** | 1 | 30 | 3/0 | 27/0 | 3 |
| `G2537` | kainos | new | G | `extracted` | **`not_done`** | 1 | 16 | 3/0 | 16/0 | 3 |
| `G2787G` | kibōtos | ark: covenant | G | `extracted_thin` | **`not_done`** | 1 | 3 | 1/0 | 2/0 | 1 |
| `G2787H` | kibōtos | ark: Noah | G | `extracted_thin` | **`not_done`** | 1 | 3 | 1/0 | 1/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H0423` — a.lah "oath"

**Identity:** mti=772 · ti=791 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:39:17): 4 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: oath
- `2`: oath of covenant
- `3`: curse
- `4`: execration

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `3a` (under `None`): from God
  - `3b` (under `None`): from men

**Root family:**
- `ALAH` (Hebrew): oath — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `H0422` a.lah "to swear"
- `H8381` ta.a.lah "curse"

### `H0548` — a.ma.nah "sure"

**Identity:** mti=774 · ti=793 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:39:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: faith, support, sure, certain

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): of a covenant
  - `1b` (under `None`): of financial support

**Root family:**
- `AMANAH` (Hebrew): sure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (29 total; sample of 29):**
- `H0071` a.va.nah "Abana"
- `H0525` a.mon "artisan"
- `H0526G` a.mon "Amon"
- `H0526H` a.mon "Amon"
- `H0526I` a.mon "Amon"
- `H0529` e.mun "faithful"
- `H0530` e.mu.nah "faithfulness"
- `H0539` a.man "be faithful"
- `H0540` a.man "to trust"
- `H0542` am.man "artisan"
- `H0543` a.men "amen"
- `H0544` o.men "faithfulness"
- `H0545` om.nah "brought up"
- `H0546` om.nah "truly"
- `H0547` o.me.nah "pillar"
- … and 14 more shown of 29 total

### `H1285` — be.rit "covenant"

**Identity:** mti=765 · ti=784 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 2 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: covenant, alliance, pledge
- `2`: (phrases)

Sub-senses (depth > 1): 12 entries — present in DB; first 15:
  - `1a` (under `None`): between men
  - `1a1` (under `None`): treaty, alliance, league (man to man)
  - `1a2` (under `None`): constitution, ordinance (monarch to subjects)
  - `1a3` (under `None`): agreement, pledge (man to man)
  - `1a4` (under `None`): alliance (of friendship)
  - `1a5` (under `None`): alliance (of marriage)
  - `1b` (under `None`): between God and man
  - `1b1` (under `None`): alliance (of friendship)
  - `1b2` (under `None`): covenant (divine ordinance with signs or pledges)
  - `2a` (under `None`): covenant making
  - `2b` (under `None`): covenant keeping
  - `2c` (under `None`): covenant violation

**Root family:**
- `BARA` (Hebrew): to eat — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `H1254A` ba.ra "to create"
- `H1254B` ba.ra "to fatten"
- `H1262` ba.rah "to eat"
- `H1286` be.rit "[Baal]-berith"

### `H1286` — be.rit "[Baal]-berith"

**Identity:** mti=3276 · ti=3411 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: § Berith = "covenant"
in the name of Baal-berith, a foreign deity worshipped in Shechem

**Root family:**
- `BARA` (Hebrew): to eat — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H0410G` el "God"
- `H0410H` el "El [Berith]"
- `H0410I` el "El [Elohe]"
- `H0410K` el "god"
- `H0410L` el "god: power"

### `H3748` — ke.ri.tut "divorce"

**Identity:** mti=3306 · ti=3441 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: divorce, dismissal, divorcement

**Root family:**
- `KARAT` (Hebrew): beam — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (10 total; sample of 10):**
- `H3747` ke.rit "Cherith"
- `H3772G` ka.rat "to cut: cut"
- `H3772H` ka.rat "to cut: make [covenant]"
- `H3772I` ka.rat "to cut: eliminate"
- `H3772J` ka.rat "to cut: lack"
- `H3773` ka.ru.tah "beam"
- `H3774G` ke.re.ti "Cherethite"
- `H3774H` ke.re.ti "Cherethite"
- `H3777` ke.sed "Chesed"
- `H3778` kas.dim "Chaldea"

### `H3772G` — ka.rat "to cut: cut"

**Identity:** mti=767 · ti=786 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: : cut/fell
1) to cut, cut off, cut down, cut off a body part, cut out, eliminate, kill, cut a covenant
1a) (Qal)
1a1) to cut off
1a1a) to cut off a body part, behead
1a2) to cut down
1a3) to hew
1a4) to cut or make a covenant
1b) (Niphal)
1b1) to be cut off
1b2) to be cut down
1b3) to be chewed
1b4) to be cut off, fail
1c) (Pual)
1c1) to be cut off
1c2) to be cut down
1d) (Hiphil)
1d1) to cut off
1d2) to cut off, destroy
1d3) to cut down, destroy
1d4) to take away
1d5) to permit to perish
1e) (Hophal) cut off

**Root family:**
- `KARAT` (Hebrew): beam — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (10 total; sample of 10):**
- `H3747` ke.rit "Cherith"
- `H3748` ke.ri.tut "divorce"
- `H3772H` ka.rat "to cut: make [covenant]"
- `H3772I` ka.rat "to cut: eliminate"
- `H3772J` ka.rat "to cut: lack"
- `H3773` ka.ru.tah "beam"
- `H3774G` ke.re.ti "Cherethite"
- `H3774H` ke.re.ti "Cherethite"
- `H3777` ke.sed "Chesed"
- `H3778` kas.dim "Chaldea"

### `H3772H` — ka.rat "to cut: make [covenant]"

**Identity:** mti=3304 · ti=3439 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: : make(covenant)
1) to cut, cut off, cut down, cut off a body part, cut out, eliminate, kill, cut a covenant
1a) (Qal)
1a1) to cut off
1a1a) to cut off a body part, behead
1a2) to cut down
1a3) to hew
1a4) to cut or make a covenant
1b) (Niphal)
1b1) to be cut off
1b2) to be cut down
1b3) to be chewed
1b4) to be cut off, fail
1c) (Pual)
1c1) to be cut off
1c2) to be cut down
1d) (Hiphil)
1d1) to cut off
1d2) to cut off, destroy
1d3) to cut down, destroy
1d4) to take away
1d5) to permit to perish
1e) (Hophal) cut off

**Root family:**
- `KARAT` (Hebrew): beam — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (10 total; sample of 10):**
- `H3747` ke.rit "Cherith"
- `H3748` ke.ri.tut "divorce"
- `H3772G` ka.rat "to cut: cut"
- `H3772I` ka.rat "to cut: eliminate"
- `H3772J` ka.rat "to cut: lack"
- `H3773` ka.ru.tah "beam"
- `H3774G` ke.re.ti "Cherethite"
- `H3774H` ke.re.ti "Cherethite"
- `H3777` ke.sed "Chesed"
- `H3778` kas.dim "Chaldea"

### `H3772J` — ka.rat "to cut: lack"

**Identity:** mti=3303 · ti=3438 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: : lack
1) to cut, cut off, cut down, cut off a body part, cut out, eliminate, kill, cut a covenant
1a) (Qal)
1a1) to cut off
1a1a) to cut off a body part, behead
1a2) to cut down
1a3) to hew
1a4) to cut or make a covenant
1b) (Niphal)
1b1) to be cut off
1b2) to be cut down
1b3) to be chewed
1b4) to be cut off, fail
1c) (Pual)
1c1) to be cut off
1c2) to be cut down
1d) (Hiphil)
1d1) to cut off
1d2) to cut off, destroy
1d3) to cut down, destroy
1d4) to take away
1d5) to permit to perish
1e) (Hophal) cut off

**Root family:**
- `KARAT` (Hebrew): beam — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (10 total; sample of 10):**
- `H3747` ke.rit "Cherith"
- `H3748` ke.ri.tut "divorce"
- `H3772G` ka.rat "to cut: cut"
- `H3772H` ka.rat "to cut: make [covenant]"
- `H3772I` ka.rat "to cut: eliminate"
- `H3773` ka.ru.tah "beam"
- `H3774G` ke.re.ti "Cherethite"
- `H3774H` ke.re.ti "Cherethite"
- `H3777` ke.sed "Chesed"
- `H3778` kas.dim "Chaldea"

### `H7620I` — sha.vu.a "week"

**Identity:** mti=3314 · ti=3449 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: seven, period of seven (days or years), heptad, week

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): period of seven days, a week
  - `1a1` (under `None`): Feast of Weeks
  - `1b` (under `None`): heptad, seven (of years)

**Root family:**
- `SHAVA` (Hebrew): week — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (14 total; sample of 14):**
- `H7620G` sha.vu.a "Weeks"
- `H7620H` sha.vu.a "week"
- `H7621` she.vu.ah "oath"
- `H7637` she.vi.i "seventh"
- `H7650` sha.va "to swear"
- `H7651` she.va "seven"
- `H7652A` she.va "Sheba"
- `H7652B` she.va "Sheba"
- `H7652G` she.va "Sheba"
- `H7655` shiv.ah "seven"
- `H7656` shiv.ah "Shibah"
- `H7657` shiv.im "seventy"
- `H7658` shiv.a.nah "seven"
- `H7659` shiv.a.ta.yim "sevenfold"

### `H7650` — sha.va "to swear"

**Identity:** mti=3308 · ti=3443 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to swear, adjure

Sub-senses (depth > 1): 8 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal) sworn (participle)
  - `1b` (under `None`): (Niphal)
  - `1b1` (under `None`): to swear, take an oath
  - `1b2` (under `None`): to swear (of Jehovah by Himself)
  - `1b3` (under `None`): to curse
  - `1c` (under `None`): (Hiphil)
  - `1c1` (under `None`): to cause to take an oath
  - `1c2` (under `None`): to adjure

**Root family:**
- `SHAVA` (Hebrew): week — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (14 total; sample of 14):**
- `H7620G` sha.vu.a "Weeks"
- `H7620H` sha.vu.a "week"
- `H7620I` sha.vu.a "week"
- `H7621` she.vu.ah "oath"
- `H7637` she.vi.i "seventh"
- `H7651` she.va "seven"
- `H7652A` she.va "Sheba"
- `H7652B` she.va "Sheba"
- `H7652G` she.va "Sheba"
- `H7655` shiv.ah "seven"
- `H7656` shiv.ah "Shibah"
- `H7657` shiv.im "seventy"
- `H7658` shiv.a.nah "seven"
- `H7659` shiv.a.ta.yim "sevenfold"

### `G0802` — asunthetos "untrustworthy"

**Identity:** mti=3284 · ti=3419 · language=Greek · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: faithless, untrustworthy 
unable to be trusted, undutiful. faithless Rom. 1:31*

**Root family:**
- `ASUNTHE` (Greek): untrustworthy — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G4934` suntithēmi "to agree"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G1242` — diathēkē "covenant"

**Identity:** mti=766 · ti=785 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: covenant, a solemn agreement between two parties; will, testament, a legal document by which property is transferred to heirs, usually upon death (Heb 9:16) 
a testamentary disposition, will; a covenant, Heb. 9:16, 17; Gal. 3:15; in NT, a covenant of God with men, Gal. 3:17; 4:24; Heb. 9:4; Mt. 26:28; the writings of the old covenant, 2Cor. 3:14

**Root family:**
- `DIATHĒK` (Greek): covenant — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G1303` diatithēmi "to make a covenant"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2537` — kainos "new"

**Identity:** mti=777 · ti=796 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T09:39:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: new, latest, anew; in some contexts new is superior to old (Mt 9:17; Heb 8) 
new, recently made, Mt. 9:17; Mk. 2:22; new in species, character, or mode, Mt. 26:28, 29; Mk. 14:24, 25; Lk. 22:20; Jn. 13:34; 2Cor. 5:17; Gal. 6:15; Eph. 2:15; 4:24; 1Jn. 2:7; Rev. 3:12; novel, strange, Mk. 1:27; Acts 17:19; new to the possessor, Mk. 16:17; unheard of, unusual, Mk. 1:27; Acts 17:19; metaphorically renovated, better, of higher excellence, 2Cor. 5:17; Rev. 5:9

**Root family:**
- `KAIN` (Greek): new — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0340` anakainizō "to restore"
- `G0341` anakainoō "to renew"
- `G2538` kainotēs "newness"
- `G3501` neos "new"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2787G` — kibōtos "ark: covenant"

**Identity:** mti=3270 · ti=3405 · language=Greek · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: ark, box, chest 
a chest, coffer; the ark, of the covenant, Heb. 9:4; Rev. 11:19; the ark of Noah, Mt. 24:38; Lk. 17:27; Heb. 11:7; 1Pet. 3:20*

**Root family:**
- `KIBŌ` (Greek): ark: Noah — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G2787G` kibōtos "ark: covenant"
- `G2787H` kibōtos "ark: Noah"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2787H` — kibōtos "ark: Noah"

**Identity:** mti=3271 · ti=3406 · language=Greek · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T11:15:17): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: ark, box, chest 
a chest, coffer; the ark, of the covenant, Heb. 9:4; Rev. 11:19; the ark of Noah, Mt. 24:38; Lk. 17:27; Heb. 11:7; 1Pet. 3:20*

**Root family:**
- `KIBŌ` (Greek): ark: Noah — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G2787G` kibōtos "ark: covenant"
- `G2787H` kibōtos "ark: Noah"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (4)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `G1303` | diatithēmi | to make a covenant | G | 1 abomination | `extracted` | 6 |
| `G4388` | protithēmi | to plan/present | G | 1 abomination | `extracted` | 3 |
| `H5715` | e.dut | testimony | H | 159 testimony | `extracted` | 59 |
| `H7621` | she.vu.ah | oath | H | 19 calling | `extracted` | 14 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H0423` — 2 groups

- **`772-001`** — 8 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Oath as solemn inner-being binding commitment*
- **`772-002`** — 6 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Covenant curse as consequence of inner moral failure*

### `H0548` — 1 groups

- **`774-001`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Firm covenant — the inner-being act of solemn communal commitment*

### `H1285` — 5 groups

- **`765-001`** — 40 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *God's covenant with creation and the patriarchs — unconditional divine inner commitment*
- **`765-002`** — 76 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *The Sinai/Mosaic covenant — bilateral covenant of law and obedience*
- **`765-003`** — 15 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *The new covenant — inner transformation through God's law written on the heart*
- **`765-004`** — 17 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *The Davidic covenant — everlasting covenant of steadfast love and kingship*
- **`765-005`** — 13 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Covenant as bond of relational loyalty between persons — friendship, marriage, and inner moral integrity*

### `H1286` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H3748` — 2 groups

- **`3306-001`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Legal dissolution of the marriage covenant — formal relational rupture*
- **`3306-002`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Divorce as metaphor for God's covenantal rupture with Israel — inner-being severity of apostasy*

### `H3772G` — 2 groups

- **`767-001`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Inner commitment under solemn self-curse — the cutting ritual as the enactment of the will's binding to covenant terms, with transgression named as the inner failure it judges*
  - notes: Revised during Dimension Review Phase B.5: characteristic-perspective rewrite. Old: The covenantal cutting ritual — self-imprecatory act underlying oath
- **`767-002`** — 4 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Cutting as moral consequence — cutting off of wickedness*

### `H3772H` — 4 groups

- **`3304-001`** — 67 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Divine covenant initiated by God — the relational framework of his commitment*
- **`3304-002`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Covenant made before God with all-heart commitment*
- **`3304-003`** — 8 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Prohibited covenant — binding to false loyalties*
- **`3304-004`** — 9 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Covenant of intimate personal loyalty — friendship and inner-being commitment between persons*

### `H3772J` — 1 groups

- **`3303-001`** — 9 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Divine covenantal faithfulness — God's unbroken inner commitment expressed through the promise of dynastic continuity*
  - notes: Revised during Dimension Review Phase B.5: characteristic-perspective rewrite. Old: Covenant promise of unbroken continuation — no lack of faithful persons in God's covenantal line

### `H7620I` — 2 groups

- **`3314-001`** — 4 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *Prophetic weeks as the divinely appointed schedule for covenant fulfillment*
- **`3314-002`** — 2 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C17`
  - *Weeks as the measure of inner-being mourning and self-denial*

### `H7650` — 4 groups

- **`3308-001`** — 30 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Divine oath as expression of God's inner commitment to his covenant promise*
- **`3308-002`** — 79 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Human oath as the binding of inner will and loyalty*
- **`3308-003`** — 17 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Swearing by God's name — oath as expression of inner-being allegiance or its corruption*
- **`3308-004`** — 5 relevant · 1 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C17`
  - *Adjuration — invoking in the context of intense inner longing and love*

### `G0802` — 1 groups

- **`3284-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Faithlessness as an inner-being character quality — covenant-breaking disposition*

### `G1242` — 3 groups

- **`766-001`** — 17 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Covenant as God's relational bond through Christ's blood*
- **`766-002`** — 5 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *New covenant written on hearts — inner transformation*
- **`766-003`** — 5 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C17`
  - *Covenantal standing — identity defined by inclusion or exclusion*

### `G2537` — 3 groups

- **`777-001`** — 5 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *New covenant — unprecedented inner transformation through Spirit*
- **`777-002`** — 4 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *New self / new creation — inner-being renewal of the person in Christ*
  - notes: Session D flag: groups 777-002 and 777-003 extend beyond covenant concept proper
- **`777-003`** — 7 relevant · 1 anchor verse(s) · dimension: `07 — Vitality / Existence` · cluster: `C17`
  - *New name, song, Jerusalem — eschatological inner-being identity, worship, and hope*
  - notes: Session D flag: extends beyond covenant concept proper to eschatological new realities

### `G2787G` — 1 groups

- **`3270-001`** — 2 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Reverential awe before the holy — the ark as the mediating sign that orients the inner person toward the presence and faithfulness of God*
  - notes: Revised during Dimension Review Phase B.5: characteristic-perspective rewrite. Old: The ark as the visible sign of God's covenant presence and faithfulness

### `G2787H` — 1 groups

- **`3271-001`** — 1 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Obedience under judgment — the ark as the instrument that separates the inner orientation of faithful response from heedless disregard*
  - notes: Revised during Dimension Review Phase B.5: characteristic-perspective rewrite. Old: The ark as means of preservation amid judgment — framing inner-being contrast of obedience and heedlessness

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 44 despair | 1 | `H0548` |
| 59 faith | 1 | `H0548` |
| 60 faithfulness | 1 | `H0548` |
| 134 renewal | 1 | `G2537` |
| 163 trust | 1 | `H0548` |
| 191 doubt | 1 | `H0548` |
| 202 transformation | 1 | `G2537` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 112 mind | 39 |
| 103 love | 37 |
| 197 authority | 23 |
| 73 guilt | 20 |
| 160 thought | 20 |
| 180 yielding | 19 |
| 182 Soul | 19 |
| 23 compassion | 17 |
| 176 worship | 17 |
| 187 strength | 15 |
| 11 awe | 14 |
| 44 despair | 14 |
| 183 heart | 14 |
| 19 calling | 13 |
| 59 faith | 13 |
| 61 fear | 13 |
| 213 listen | 13 |
| 40 deceit | 12 |
| 204 name | 12 |
| 60 faithfulness | 10 |
| 99 kindness | 10 |
| 43 desire | 9 |
| 98 justice | 8 |
| 128 rebellion | 8 |
| 151 sorrow | 8 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 1 abomination | Heb 8:10 |
| 19 calling | Neh 10:29 |
| 76 holiness | Eph 4:24 |
| 78 hope | Eph 2:12 |
| 78 hope | Isa 28:15 |
| 111 mercy | Rom 1:31 |
| 112 mind | Heb 8:10 |
| 147 sin | Dan 9:24 |
| 159 testimony | 2Ki 23:3 |
| 177 worth | 2Sa 23:5 |
| 197 authority | Eph 2:12 |
| 204 name | Rev 2:17 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-34-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-08 · **term_id:** -

> Three groups within the covenant registry show the new covenant as inner transformation (765-003, 766-002, 777-001 — law written on heart, new covenant through Spirit, new self/creation in Christ). Session B should examine the covenant registry's inner transformation dimension: how the trajectory from the Sinai covenant (obedience required externally, inner-being orientation demanded) to the new covenant (transformation from within, law on heart) is encoded in the Dimension Review data and what this discloses about the inner person as the site of covenantal fulfilment.

**Anchor verses cited:** Jer 31:31-34; 2 Cor 3; Eph 4:24

### H.2 Open SD pointers + research flags (6)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `VERSE_EVIDENCE_BREADTH_NOTE` | PH2-34-001 | MEDIUM | D | 2026-03-26 |
| `VERSE_EVIDENCE_BREADTH_NOTE` | PH2-34-002 | MEDIUM | D | 2026-03-26 |
| `VERSE_EVIDENCE_BREADTH_NOTE` | PH2-34-003 | MEDIUM | D | 2026-03-26 |
| `PH2_CROSS_REGISTRY_REQUIRED` | PH2-34-004 | MEDIUM | D | 2026-03-26 |
| `DIMREVIEW_SESSION_D` | DIM-34-SD001 | MEDIUM | D | 2026-04-11 |
| `PH2_DATA_ERROR` | PH2-34-005 | HIGH | B | 2026-03-26 |

#### PH2-34-001

> G1242 (covenant) — 340 occurrences, only 30 verses in export (9% coverage). Analysis draws on available sample. Full verse set required before synthesis-level conclusions on this term.

#### PH2-34-002

> G1303 (to make a covenant) — 92 occurrences, only 6 verses in export (7% coverage). Analysis draws on available sample. Full verse set required before synthesis-level conclusions on this term.

#### PH2-34-003

> G2787G (ark: covenant) — 230 occurrences, only 3 verses in export (1% coverage). Analysis draws on available sample. Full verse set required before synthesis-level conclusions on this term.

#### PH2-34-004

> Ten shalom-family terms classified xref_peace (registry 117): H7965G (shalom, peace, 164 occ), H7965H (shalom, Peace [God], 1 occ), H7965I (shalom, well-being, 54 occ), H7965J (shalom, friendship, 5 occ), H7965K (shalom, greeting, 12 occ), H7965L (shalom, completely, 1 occ), H7999A (shalem, to complete/repay, 103 occ), H7999B (shalam, to ally, 13 occ), H8002 (shelem, peace offering, 87 occ), H8003 (shalem, complete, 28 occ). Peace is extensively covered in registry 117. However, the covenant-peace nexus (berit shalom — covenant of peace, Num 25:12; Isa 54:10; Eze 34:25; 37:26) is a specific OT theological category where the two registries intersect directly. Session D must assess whether the peace registry analysis captures this covenant dimension, and if not, initiate a cross-registry pass for the berit-shalom passages.

#### DIM-34-SD001

> The covenant vocabulary of Reg 34 spans at least four distinct dimension categories across the be.rit and ka.rat groups: Relational Disposition (unconditional divine commitment, relational bond), Transformation (new covenant, heart-writing), Volition (bilateral obligation, obedience-commitment), and Moral Character (oath-keeping, integrity). This multi-dimensional structure is not a grouping failure — it reflects the genuine inner-being complexity of covenant as a category that encompasses relational bond, inner transformation, volitional commitment, and moral integrity simultaneously. Session D should examine whether the covenant vocabulary of Reg 34 serves as a structural backbone for the other C17 registries: whether love (Reg 103), mercy (Reg 111), compassion (Reg 23) and peace (Reg 117) can be understood as facets of the single inner-being architecture that covenant names. The hypothesis is that covenant in Reg 34 is not merely one registry among equals in C17 but the structural container within which the other relational-disposition registries operate.

#### PH2-34-005

> EXTRACTION ANOMALY — Phase 1 source list incorrectly included 7 high-frequency grammatical function words as covenant vocabulary: H0637 (aph, also, 134 occ), H0859A (attah, you m.s., 745 occ), H1697G (davar, word, 920 occ), H1961 (hayah, to be, 3612 occ), H2063 (zot, this, 607 occ), H5973A (im, with, 979 occ), H8033G (sham, there, 838 occ). Total: 7,835 occurrences of grammatical particles misidentified as covenant terms. Diagnostic overlap analysis: 0-6% of their exported verses co-occur with berith/diatheke verses. Likely cause: Phase 1 extraction used a broad concordance sweep of covenant-context verses and captured all Strong's numbers present, including grammatical co-occurrents. Claude Code should audit the Phase 1 extraction source list for registry 34 and review whether other registries may have the same systematic error.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `H0423` (1 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `H3772G` (1 flag(s))

- **`THIN_DATA`** — Fewer verse occurrences than expected; analysis may be limited
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G1242` (2 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`SPAN_RESOLUTION_CONFLICT`** — Queried Strong's not found in any verse span after suffix resolution. Verse set is empty. Manual STEP UI verification required.
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G2537` (1 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H0423` — 14/14 classified · 2 anchor verse(s)

**Group `772-001`** (8 verses — anchors: Neh 10:29)

- **Neh 10:29** 🔵 (✓) *target: curse*
  > Neh 10:29 join with their brothers , their nobles , and enter into a curse and an oath to walk in God’s Law that was given by Moses the servant of God , and to observe and do all the commandments of the Lord our Lord and his rules and his statutes .
- **Gen 24:41** (✓) *target: oath*
  > Gen 24:41 Then you will be free from my oath , when you come to my clan . And if they will not give her to you, you will be free from my oath .’
- **Gen 26:28** (✓) *target: sworn pact*
  > Gen 26:28 They said , “We see plainly that the Lord has been with you. So we said , let there be a sworn pact between us, between you and us, and let us make a covenant with you ,
- **Lev 5:1** (✓) *target: public*
  > Lev 5:1 “If anyone sins in that he hears a public adjuration to testify, and though he is a witness , whether he has seen or come to know the matter, yet does not speak , he shall bear his iniquity ;
- **Num 5:21** (✓) *target: curse*
  > Num 5:21 then’ (let the priest make the woman take the oath of the curse , and say to the woman ) ‘the Lord make you a curse and an oath among your people , when the Lord makes your thigh fall away and your body swell .
- **Num 5:23** (✓) *target: curses*
  > Num 5:23 “Then the priest shall write these curses in a book and wash them off into the water of bitterness .
- **Num 5:27** (✓) *target: curse*
  > Num 5:27 And when he has made her drink the water , then, if she has defiled herself and has broken faith with her husband , the water that brings the curse shall enter into her and cause bitter pain , and her womb shall swell , and her thigh shall fall away , and the woman shall become a curse among her people .
- **Job 31:30** (✓) *target: curse*
  > Job 31:30 ( I have not let my mouth sin by asking for his life with a curse ),

**Group `772-002`** (6 verses — anchors: Dan 9:11)

- **Dan 9:11** 🔵 (✓) *target: curse*
  > Dan 9:11 All Israel has transgressed your law and turned aside , refusing to obey your voice . And the curse and oath that are written in the Law of Moses the servant of God have been poured out upon us, because we have sinned against him .
- **Isa 24:6** (✓) *target: curse*
  > Isa 24:6 Therefore a curse devours the earth , and its inhabitants suffer for their guilt ; therefore the inhabitants of the earth are scorched , and few men are left .
- **Jer 23:10** (✓) *target: curse*
  > Jer 23:10 For the land is full of adulterers ; because of the curse the land mourns , and the pastures of the wilderness are dried up . Their course is evil , and their might is not right .
- **Jer 29:18** (✓) *target: curse*
  > Jer 29:18 I will pursue them with sword , famine , and pestilence , and will make them a horror to all the kingdoms of the earth , to be a curse , a terror , a hissing , and a reproach among all the nations where I have driven them,
- **Jer 42:18** (✓) *target: execration*
  > Jer 42:18 “ For thus says the Lord of hosts , the God of Israel : As my anger and my wrath were poured out on the inhabitants of Jerusalem , so my wrath will be poured out on you when you go to Egypt . You shall become an execration , a horror , a curse , and a taunt . You shall see this place no more .
- **Jer 44:12** (✓) *target: oath*
  > Jer 44:12 I will take the remnant of Judah who have set their faces to come to the land of Egypt to live , and they shall all be consumed . In the land of Egypt they shall fall ; by the sword and by famine they shall be consumed . From the least to the greatest , they shall die by the sword and by famine , and they shall become an oath , a horror , a curse , and a taunt .

### `H0548` — 1/2 classified · 1 anchor verse(s)

**Group `774-001`** (1 verse — anchors: Neh 9:38)

- **Neh 9:38** 🔵 (✓) *target: firm covenant*
  > Neh 9:38 “Because of all this we make a firm covenant in writing ; on the sealed document are the names of our princes , our Levites , and our priests .

**Group `UNCLASSIFIED`** (1 verse)

- **Neh 11:23** (—) *target: fixed provision*
  > Neh 11:23 For there was a command from the king concerning them, and a fixed provision for the singers , as every day required .

### `H1285` — 160/239 classified · 5 anchor verse(s)

**Group `765-001`** (40 verses — anchors: Gen 9:15)

- **Gen 9:15** 🔵 (✓) *target: covenant*
  > Gen 9:15 I will remember my covenant that is between me and you and every living creature of all flesh . And the waters shall never again become a flood to destroy all flesh .
- **Gen 6:18** (✓) *target: covenant*
  > Gen 6:18 But I will establish my covenant with you, and you shall come into the ark , you, your sons , your wife , and your sons ’ wives with you .
- **Gen 9:9** (✓) *target: covenant*
  > Gen 9:9 “ Behold , I establish my covenant with you and your offspring after you ,
- **Gen 9:11** (✓) *target: covenant*
  > Gen 9:11 I establish my covenant with you, that never again shall all flesh be cut off by the waters of the flood , and never again shall there be a flood to destroy the earth .”
- **Gen 9:12** (✓) *target: covenant*
  > Gen 9:12 And God said , “ This is the sign of the covenant that I make between me and you and every living creature that is with you, for all future generations :
- **Gen 9:13** (✓) *target: covenant*
  > Gen 9:13 I have set my bow in the cloud , and it shall be a sign of the covenant between me and the earth .
- **Gen 9:16** (✓) *target: covenant*
  > Gen 9:16 When the bow is in the clouds , I will see it and remember the everlasting covenant between God and every living creature of all flesh that is on the earth .”
- **Gen 9:17** (✓) *target: covenant*
  > Gen 9:17 God said to Noah , “ This is the sign of the covenant that I have established between me and all flesh that is on the earth .”
- **Gen 15:18** (✓) *target: covenant*
  > Gen 15:18 On that day the Lord made a covenant with Abram , saying , “ To your offspring I give this land , from the river of Egypt to the great river , the river Euphrates ,
- **Gen 17:2** (✓) *target: covenant*
  > Gen 17:2 that I may make my covenant between me and you, and may multiply you greatly .”
- **Gen 17:4** (✓) *target: covenant*
  > Gen 17:4 “ Behold , my covenant is with you, and you shall be the father of a multitude of nations .
- **Gen 17:7** (✓) *target: covenant*
  > Gen 17:7 And I will establish my covenant between me and you and your offspring after you throughout their generations for an everlasting covenant , to be God to you and to your offspring after you .
- **Gen 17:9** (✓) *target: covenant*
  > Gen 17:9 And God said to Abraham , “As for you, you shall keep my covenant , you and your offspring after you throughout their generations .
- **Gen 17:10** (✓) *target: covenant*
  > Gen 17:10 This is my covenant , which you shall keep , between me and you and your offspring after you: Every male among you shall be circumcised .
- **Gen 17:11** (✓) *target: covenant*
  > Gen 17:11 You shall be circumcised in the flesh of your foreskins , and it shall be a sign of the covenant between me and you .
- **Gen 17:13** (✓) *target: covenant*
  > Gen 17:13 both he who is born in your house and he who is bought with your money , shall surely be circumcised . So shall my covenant be in your flesh an everlasting covenant .
- **Gen 17:14** (✓) *target: covenant*
  > Gen 17:14 Any uncircumcised male who is not circumcised in the flesh of his foreskin shall be cut off from his people ; he has broken my covenant .”
- **Gen 17:19** (✓) *target: covenant*
  > Gen 17:19 God said , “ No , but Sarah your wife shall bear you a son , and you shall call his name Isaac . I will establish my covenant with him as an everlasting covenant for his offspring after him .
- **Gen 17:21** (✓) *target: covenant*
  > Gen 17:21 But I will establish my covenant with Isaac , whom Sarah shall bear to you at this time next year .”
- **Exo 2:24** (✓) *target: covenant*
  > Exo 2:24 And God heard their groaning , and God remembered his covenant with Abraham , with Isaac , and with Jacob .
- **Exo 6:4** (✓) *target: covenant*
  > Exo 6:4 I also established my covenant with them to give them the land of Canaan , the land in which they lived as sojourners .
- **Exo 6:5** (✓) *target: covenant*
  > Exo 6:5 Moreover , I have heard the groaning of the people of Israel whom the Egyptians hold as slaves , and I have remembered my covenant .
- **Lev 26:42** (✓) *target: covenant*
  > Lev 26:42 then I will remember my covenant with Jacob , and I will remember my covenant with Isaac and my covenant with Abraham , and I will remember the land .
- **Lev 26:44** (✓) *target: covenant*
  > Lev 26:44 Yet for all that , when they are in the land of their enemies , I will not spurn them, neither will I abhor them so as to destroy them utterly and break my covenant with them , for I am the Lord their God .
- **Lev 26:45** (✓) *target: covenant*
  > Lev 26:45 But I will for their sake remember the covenant with their forefathers , whom I brought out of the land of Egypt in the sight of the nations , that I might be their God : I am the Lord .”
- **Num 18:19** (✓) *target: covenant*
  > Num 18:19 All the holy contributions that the people of Israel present to the Lord I give to you, and to your sons and daughters with you, as a perpetual due . It is a covenant of salt forever before the Lord for you and for your offspring with you .”
- **Deu 4:31** (✓) *target: covenant*
  > Deu 4:31 For the Lord your God is a merciful God . He will not leave you or destroy you or forget the covenant with your fathers that he swore to them .
- **Deu 7:9** (✓) *target: covenant*
  > Deu 7:9 Know therefore that the Lord your God is God , the faithful God who keeps covenant and steadfast love with those who love him and keep his commandments , to a thousand generations ,
  - notes: Dual-context Deu 7:9: also Group 765-002; primary 765-002
- **Deu 7:12** (✓) *target: covenant*
  > Deu 7:12 “And because you listen to these rules and keep and do them, the Lord your God will keep with you the covenant and the steadfast love that he swore to your fathers .
- **Deu 8:18** (✓) *target: covenant*
  > Deu 8:18 You shall remember the Lord your God , for it is he who gives you power to get wealth , that he may confirm his covenant that he swore to your fathers , as it is this day .
- **2Ki 13:23** (✓) *target: covenant*
  > 2Ki 13:23 But the Lord was gracious to them and had compassion on them, and he turned toward them, because of his covenant with Abraham , Isaac , and Jacob , and would not destroy them, nor has he cast them from his presence until now .
- **Neh 9:8** (✓) *target: covenant*
  > Neh 9:8 You found his heart faithful before you, and made with him the covenant to give to his offspring the land of the Canaanite , the Hittite , the Amorite , the Perizzite , the Jebusite , and the Girgashite . And you have kept your promise , for you are righteous .
- **Neh 9:32** (✓) *target: covenant*
  > Neh 9:32 “ Now , therefore, our God , the great , the mighty , and the awesome God , who keeps covenant and steadfast love , let not all the hardship seem little to you that has come upon us, upon our kings , our princes , our priests , our prophets , our fathers , and all your people , since the time of the kings of Assyria until this day .
- **Psa 105:8** (✓) *target: covenant*
  > Psa 105:8 He remembers his covenant forever , the word that he commanded , for a thousand generations ,
- **Psa 105:10** (✓) *target: covenant*
  > Psa 105:10 which he confirmed to Jacob as a statute , to Israel as an everlasting covenant ,
- **Psa 106:45** (✓) *target: covenant*
  > Psa 106:45 For their sake he remembered his covenant , and relented according to the abundance of his steadfast love .
- **Psa 111:5** (✓) *target: covenant*
  > Psa 111:5 He provides food for those who fear him; he remembers his covenant forever .
- **Psa 111:9** (✓) *target: covenant*
  > Psa 111:9 He sent redemption to his people ; he has commanded his covenant forever . Holy and awesome is his name !
- **Dan 9:4** (✓) *target: covenant*
  > Dan 9:4 I prayed to the Lord my God and made confession , saying , “ O Lord , the great and awesome God , who keeps covenant and steadfast love with those who love him and keep his commandments ,
- **Mal 2:5** (✓) *target: covenant*
  > Mal 2:5 My covenant with him was one of life and peace , and I gave them to him. It was a covenant of fear , and he feared me. He stood in awe of my name .

**Group `765-002`** (76 verses — anchors: Deu 7:9)

- **Deu 7:9** 🔵 (✓) *target: covenant*
  > Deu 7:9 Know therefore that the Lord your God is God , the faithful God who keeps covenant and steadfast love with those who love him and keep his commandments , to a thousand generations ,
  - notes: Dual-context Deu 7:9: primary 765-002, secondary 765-001
- **Exo 19:5** (✓) *target: covenant*
  > Exo 19:5 Now therefore, if you will indeed obey my voice and keep my covenant , you shall be my treasured possession among all peoples , for all the earth is mine;
- **Exo 24:7** (✓) *target: Covenant*
  > Exo 24:7 Then he took the Book of the Covenant and read it in the hearing of the people . And they said , “ All that the Lord has spoken we will do , and we will be obedient .”
- **Exo 24:8** (✓) *target: covenant*
  > Exo 24:8 And Moses took the blood and threw it on the people and said , “ Behold the blood of the covenant that the Lord has made with you in accordance with all these words .”
- **Exo 31:16** (✓) *target: covenant*
  > Exo 31:16 Therefore the people of Israel shall keep the Sabbath , observing the Sabbath throughout their generations , as a covenant forever .
- **Exo 34:10** (✓) *target: covenant*
  > Exo 34:10 And he said , “ Behold , I am making a covenant . Before all your people I will do marvels , such as have not been created in all the earth or in any nation . And all the people among whom you are shall see the work of the Lord , for it is an awesome thing that I will do with you .
- **Exo 34:12** (✓) *target: covenant*
  > Exo 34:12 Take care , lest you make a covenant with the inhabitants of the land to which you go , lest it become a snare in your midst .
- **Exo 34:15** (✓) *target: covenant*
  > Exo 34:15 lest you make a covenant with the inhabitants of the land , and when they whore after their gods and sacrifice to their gods and you are invited , you eat of his sacrifice ,
- **Exo 34:27** (✓) *target: covenant*
  > Exo 34:27 And the Lord said to Moses , “ Write these words , for in accordance with these words I have made a covenant with you and with Israel .”
- **Exo 34:28** (✓) *target: covenant*
  > Exo 34:28 So he was there with the Lord forty days and forty nights . He neither ate bread nor drank water . And he wrote on the tablets the words of the covenant , the Ten Commandments .
- **Deu 4:13** (✓) *target: covenant*
  > Deu 4:13 And he declared to you his covenant , which he commanded you to perform , that is, the Ten Commandments , and he wrote them on two tablets of stone .
- **Deu 4:23** (✓) *target: covenant*
  > Deu 4:23 Take care , lest you forget the covenant of the Lord your God , which he made with you, and make a carved image , the form of anything that the Lord your God has forbidden you.
- **Deu 5:2** (✓) *target: covenant*
  > Deu 5:2 The Lord our God made a covenant with us in Horeb .
- **Deu 5:3** (✓) *target: covenant*
  > Deu 5:3 Not with our fathers did the Lord make this covenant , but with us , who are all of us here alive today .
- **Deu 9:9** (✓) *target: covenant*
  > Deu 9:9 When I went up the mountain to receive the tablets of stone , the tablets of the covenant that the Lord made with you, I remained on the mountain forty days and forty nights . I neither ate bread nor drank water .
- **Deu 17:2** (✓) *target: covenant*
  > Deu 17:2 “ If there is found among you, within any of your towns that the Lord your God is giving you, a man or woman who does what is evil in the sight of the Lord your God , in transgressing his covenant ,
- **Deu 29:1** (✓) *target: covenant*
  > Deu 29:1 These are the words of the covenant that the Lord commanded Moses to make with the people of Israel in the land of Moab , besides the covenant that he had made with them at Horeb .
- **Deu 29:9** (✓) *target: covenant*
  > Deu 29:9 Therefore keep the words of this covenant and do them, that you may prosper in all that you do .
- **Deu 29:12** (✓) *target: covenant*
  > Deu 29:12 so that you may enter into the sworn covenant of the Lord your God , which the Lord your God is making with you today ,
- **Deu 29:14** (✓) *target: covenant*
  > Deu 29:14 It is not with you alone that I am making this sworn covenant ,
- **Deu 29:21** (✓) *target: covenant*
  > Deu 29:21 And the Lord will single him out from all the tribes of Israel for calamity , in accordance with all the curses of the covenant written in this Book of the Law .
- **Deu 29:25** (✓) *target: covenant*
  > Deu 29:25 Then people will say , ‘It is because they abandoned the covenant of the Lord , the God of their fathers , which he made with them when he brought them out of the land of Egypt ,
- **Deu 31:9** (✓) *target: covenant*
  > Deu 31:9 Then Moses wrote this law and gave it to the priests , the sons of Levi , who carried the ark of the covenant of the Lord , and to all the elders of Israel .
- **Deu 31:16** (✓) *target: covenant*
  > Deu 31:16 And the Lord said to Moses , “ Behold , you are about to lie down with your fathers . Then this people will rise and whore after the foreign gods among them in the land that they are entering , and they will forsake me and break my covenant that I have made with them .
- **Deu 31:20** (✓) *target: covenant*
  > Deu 31:20 For when I have brought them into the land flowing with milk and honey , which I swore to give to their fathers , and they have eaten and are full and grown fat , they will turn to other gods and serve them, and despise me and break my covenant .
- **Deu 31:26** (✓) *target: covenant*
  > Deu 31:26 “ Take this Book of the Law and put it by the side of the ark of the covenant of the Lord your God , that it may be there for a witness against you.
- **Deu 33:9** (✓) *target: covenant*
  > Deu 33:9 who said of his father and mother , ‘I regard them not ’; he disowned his brothers and ignored his children . For they observed your word and kept your covenant .
- **Jos 7:11** (✓) *target: covenant*
  > Jos 7:11 Israel has sinned ; they have transgressed my covenant that I commanded them; they have taken some of the devoted things ; they have stolen and lied and put them among their own belongings .
- **Jos 7:15** (✓) *target: covenant*
  > Jos 7:15 And he who is taken with the devoted things shall be burned with fire , he and all that he has, because he has transgressed the covenant of the Lord , and because he has done an outrageous thing in Israel .’”
- **Jos 23:16** (✓) *target: covenant*
  > Jos 23:16 if you transgress the covenant of the Lord your God , which he commanded you, and go and serve other gods and bow down to them. Then the anger of the Lord will be kindled against you, and you shall perish quickly from off the good land that he has given to you .”
- **Jos 24:25** (✓) *target: covenant*
  > Jos 24:25 So Joshua made a covenant with the people that day , and put in place statutes and rules for them at Shechem .
- **Judg 2:1** (✓) *target: covenant*
  > Judg 2:1 Now the angel of the Lord went up from Gilgal to Bochim . And he said , “I brought you up from Egypt and brought you into the land that I swore to give to your fathers . I said , ‘I will never break my covenant with you ,
- **Judg 2:2** (✓) *target: covenant*
  > Judg 2:2 and you shall make no covenant with the inhabitants of this land ; you shall break down their altars .’ But you have not obeyed my voice . What is this you have done ?
- **Judg 2:20** (✓) *target: covenant*
  > Judg 2:20 So the anger of the Lord was kindled against Israel , and he said , “ Because this people have transgressed my covenant that I commanded their fathers and have not obeyed my voice ,
- **2Ki 17:15** (✓) *target: covenant*
  > 2Ki 17:15 They despised his statutes and his covenant that he made with their fathers and the warnings that he gave them. They went after false idols and became false , and they followed the nations that were around them, concerning whom the Lord had commanded them that they should not do like them .
- **2Ki 17:35** (✓) *target: covenant*
  > 2Ki 17:35 The Lord made a covenant with them and commanded them, “You shall not fear other gods or bow yourselves to them or serve them or sacrifice to them ,
- **2Ki 17:38** (✓) *target: covenant*
  > 2Ki 17:38 and you shall not forget the covenant that I have made with you. You shall not fear other gods ,
- **2Ki 18:12** (✓) *target: covenant*
  > 2Ki 18:12 because they did not obey the voice of the Lord their God but transgressed his covenant , even all that Moses the servant of the Lord commanded . They neither listened nor obeyed .
- **2Ki 23:2** (✓) *target: Covenant*
  > 2Ki 23:2 And the king went up to the house of the Lord , and with him all the men of Judah and all the inhabitants of Jerusalem and the priests and the prophets , all the people , both small and great . And he read in their hearing all the words of the Book of the Covenant that had been found in the house of the Lord .
- **2Ki 23:3** (✓) *target: covenant*
  > 2Ki 23:3 And the king stood by the pillar and made a covenant before the Lord , to walk after the Lord and to keep his commandments and his testimonies and his statutes with all his heart and all his soul , to perform the words of this covenant that were written in this book . And all the people joined in the covenant .
- **2Ki 23:21** (✓) *target: Covenant*
  > 2Ki 23:21 And the king commanded all the people , “ Keep the Passover to the Lord your God , as it is written in this Book of the Covenant .”
- **Psa 25:10** (✓) *target: covenant*
  > Psa 25:10 All the paths of the Lord are steadfast love and faithfulness , for those who keep his covenant and his testimonies .
- **Psa 25:14** (✓) *target: covenant*
  > Psa 25:14 The friendship of the Lord is for those who fear him, and he makes known to them his covenant .
- **Psa 44:17** (✓) *target: covenant*
  > Psa 44:17 All this has come upon us, though we have not forgotten you, and we have not been false to your covenant .
- **Psa 50:5** (✓) *target: covenant*
  > Psa 50:5 “ Gather to me my faithful ones , who made a covenant with me by sacrifice !”
- **Psa 50:16** (✓) *target: covenant*
  > Psa 50:16 But to the wicked God says : “ What right have you to recite my statutes or take my covenant on your lips ?
- **Psa 78:10** (✓) *target: covenant*
  > Psa 78:10 They did not keep God’s covenant , but refused to walk according to his law .
- **Psa 78:37** (✓) *target: covenant*
  > Psa 78:37 Their heart was not steadfast toward him; they were not faithful to his covenant .
- **Psa 103:18** (✓) *target: covenant*
  > Psa 103:18 to those who keep his covenant and remember to do his commandments .
- **Isa 24:5** (✓) *target: covenant*
  > Isa 24:5 The earth lies defiled under its inhabitants ; for they have transgressed the laws , violated the statutes , broken the everlasting covenant .
- **Isa 56:4** (✓) *target: covenant*
  > Isa 56:4 For thus says the Lord : “ To the eunuchs who keep my Sabbaths , who choose the things that please me and hold fast my covenant ,
- **Isa 56:6** (✓) *target: covenant*
  > Isa 56:6 “And the foreigners who join themselves to the Lord , to minister to him, to love the name of the Lord , and to be his servants , everyone who keeps the Sabbath and does not profane it, and holds fast my covenant —
- **Isa 59:21** (✓) *target: covenant*
  > Isa 59:21 “And as for me , this is my covenant with them,” says the Lord : “My Spirit that is upon you, and my words that I have put in your mouth , shall not depart out of your mouth , or out of the mouth of your offspring , or out of the mouth of your children’s offspring ,” says the Lord , “ from this time forth and forevermore .”
  - notes: Dual-context Isa 59:21: also Group 765-003
- **Jer 11:2** (✓) *target: covenant*
  > Jer 11:2 “ Hear the words of this covenant , and speak to the men of Judah and the inhabitants of Jerusalem .
- **Jer 11:3** (✓) *target: covenant*
  > Jer 11:3 You shall say to them, Thus says the Lord , the God of Israel : Cursed be the man who does not hear the words of this covenant
- **Jer 11:6** (✓) *target: covenant*
  > Jer 11:6 And the Lord said to me, “ Proclaim all these words in the cities of Judah and in the streets of Jerusalem : Hear the words of this covenant and do them .
- **Jer 11:8** (✓) *target: covenant*
  > Jer 11:8 Yet they did not obey or incline their ear , but everyone walked in the stubbornness of his evil heart . Therefore I brought upon them all the words of this covenant , which I commanded them to do , but they did not .”
- **Jer 11:10** (✓) *target: covenant*
  > Jer 11:10 They have turned back to the iniquities of their forefathers , who refused to hear my words . They have gone after other gods to serve them. The house of Israel and the house of Judah have broken my covenant that I made with their fathers .
- **Jer 14:21** (✓) *target: covenant*
  > Jer 14:21 Do not spurn us, for your name’s sake ; do not dishonor your glorious throne ; remember and do not break your covenant with us .
- **Jer 22:9** (✓) *target: covenant*
  > Jer 22:9 And they will answer , “ Because they have forsaken the covenant of the Lord their God and worshiped other gods and served them .”’”
- **Jer 31:32** (✓) *target: covenant*
  > Jer 31:32 not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt , my covenant that they broke , though I was their husband , declares the Lord .
- **Jer 34:8** (✓) *target: covenant*
  > Jer 34:8 The word that came to Jeremiah from the Lord , after King Zedekiah had made a covenant with all the people in Jerusalem to make a proclamation of liberty to them,
- **Jer 34:10** (✓) *target: covenant*
  > Jer 34:10 And they obeyed , all the officials and all the people who had entered into the covenant that everyone would set free his slave , male or female , so that they would not be enslaved again . They obeyed and set them free .
- **Jer 34:13** (✓) *target: covenant*
  > Jer 34:13 “ Thus says the Lord , the God of Israel : I myself made a covenant with your fathers when I brought them out of the land of Egypt , out of the house of slavery , saying ,
- **Jer 34:15** (✓) *target: covenant*
  > Jer 34:15 You recently repented and did what was right in my eyes by proclaiming liberty , each to his neighbor , and you made a covenant before me in the house that is called by my name ,
- **Jer 34:18** (✓) *target: covenant*
  > Jer 34:18 And the men who transgressed my covenant and did not keep the terms of the covenant that they made before me, I will make them like the calf that they cut in two and passed between its parts —
- **Eze 16:59** (✓) *target: covenant*
  > Eze 16:59 “ For thus says the Lord God : I will deal with you as you have done , you who have despised the oath in breaking the covenant ,
- **Eze 20:37** (✓) *target: covenant*
  > Eze 20:37 I will make you pass under the rod , and I will bring you into the bond of the covenant .
- **Eze 44:7** (✓) *target: covenant*
  > Eze 44:7 in admitting foreigners , uncircumcised in heart and flesh , to be in my sanctuary , profaning my temple , when you offer to me my food , the fat and the blood . You have broken my covenant , in addition to all your abominations .
- **Hos 6:7** (✓) *target: covenant*
  > Hos 6:7 But like Adam they transgressed the covenant ; there they dealt faithlessly with me .
- **Hos 8:1** (✓) *target: covenant*
  > Hos 8:1 Set the trumpet to your lips ! One like a vulture is over the house of the Lord , because they have transgressed my covenant and rebelled against my law .
- **Hos 10:4** (✓) *target: covenants*
  > Hos 10:4 They utter mere words ; with empty oaths they make covenants ; so judgment springs up like poisonous weeds in the furrows of the field .
- **Hos 12:1** (✓) *target: covenant*
  > Hos 12:1 Ephraim feeds on the wind and pursues the east wind all day long; they multiply falsehood and violence ; they make a covenant with Assyria , and oil is carried to Egypt .
- **Mal 2:4** (✓) *target: covenant*
  > Mal 2:4 So shall you know that I have sent this command to you, that my covenant with Levi may stand, says the Lord of hosts .
- **Mal 2:8** (✓) *target: covenant*
  > Mal 2:8 But you have turned aside from the way . You have caused many to stumble by your instruction . You have corrupted the covenant of Levi , says the Lord of hosts ,
- **Mal 2:10** (✓) *target: covenant*
  > Mal 2:10 Have we not all one Father ? Has not one God created us? Why then are we faithless to one another , profaning the covenant of our fathers ?

**Group `765-003`** (15 verses — anchors: Jer 31:33)

- **Jer 31:33** 🔵 (✓) *target: covenant*
  > Jer 31:33 For this is the covenant that I will make with the house of Israel after those days , declares the Lord : I will put my law within them, and I will write it on their hearts . And I will be their God , and they shall be my people .
- **Isa 54:10** (✓) *target: covenant*
  > Isa 54:10 For the mountains may depart and the hills be removed , but my steadfast love shall not depart from you, and my covenant of peace shall not be removed ,” says the Lord , who has compassion on you.
- **Isa 55:3** (✓) *target: covenant*
  > Isa 55:3 Incline your ear , and come to me; hear , that your soul may live ; and I will make with you an everlasting covenant , my steadfast , sure love for David .
- **Isa 59:21** (✓) *target: covenant*
  > Isa 59:21 “And as for me , this is my covenant with them,” says the Lord : “My Spirit that is upon you, and my words that I have put in your mouth , shall not depart out of your mouth , or out of the mouth of your offspring , or out of the mouth of your children’s offspring ,” says the Lord , “ from this time forth and forevermore .”
  - notes: Dual-context Isa 59:21: also Group 765-002
- **Isa 61:8** (✓) *target: covenant*
  > Isa 61:8 For I the Lord love justice ; I hate robbery and wrong ; I will faithfully give them their recompense , and I will make an everlasting covenant with them .
- **Jer 31:31** (✓) *target: covenant*
  > Jer 31:31 “ Behold , the days are coming , declares the Lord , when I will make a new covenant with the house of Israel and the house of Judah ,
- **Jer 32:40** (✓) *target: covenant*
  > Jer 32:40 I will make with them an everlasting covenant , that I will not turn away from doing good to them . And I will put the fear of me in their hearts , that they may not turn from me .
- **Jer 50:5** (✓) *target: covenant*
  > Jer 50:5 They shall ask the way to Zion , with faces turned toward it , saying, ‘ Come , let us join ourselves to the Lord in an everlasting covenant that will never be forgotten .’
- **Eze 16:8** (✓) *target: covenant*
  > Eze 16:8 “When I passed by you again and saw you, behold , you were at the age for love , and I spread the corner of my garment over you and covered your nakedness ; I made my vow to you and entered into a covenant with you, declares the Lord God , and you became mine .
- **Eze 16:60** (✓) *target: covenant*
  > Eze 16:60 yet I will remember my covenant with you in the days of your youth , and I will establish for you an everlasting covenant .
- **Eze 16:62** (✓) *target: covenant*
  > Eze 16:62 I will establish my covenant with you, and you shall know that I am the Lord ,
- **Eze 34:25** (✓) *target: covenant*
  > Eze 34:25 “I will make with them a covenant of peace and banish wild beasts from the land , so that they may dwell securely in the wilderness and sleep in the woods .
- **Eze 37:26** (✓) *target: covenant*
  > Eze 37:26 I will make a covenant of peace with them. It shall be an everlasting covenant with them. And I will set them in their land and multiply them, and will set my sanctuary in their midst forevermore .
- **Zec 9:11** (✓) *target: covenant*
  > Zec 9:11 As for you also , because of the blood of my covenant with you, I will set your prisoners free from the waterless pit .
- **Mal 3:1** (✓) *target: covenant*
  > Mal 3:1 “ Behold , I send my messenger , and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple ; and the messenger of the covenant in whom you delight , behold , he is coming , says the Lord of hosts .

**Group `765-004`** (16 verses — anchors: 2Sa 23:5)

- **2Sa 23:5** 🔵 (✓) *target: covenant*
  > 2Sa 23:5 “ For does not my house stand so with God ? For he has made with me an everlasting covenant , ordered in all things and secure . For will he not cause to prosper all my help and my desire ?
- **1Ki 8:23** (✓) *target: covenant*
  > 1Ki 8:23 and said , “O Lord , God of Israel , there is no God like you, in heaven above or on earth beneath, keeping covenant and showing steadfast love to your servants who walk before you with all their heart ;
- **1Ki 11:11** (✓) *target: covenant*
  > 1Ki 11:11 Therefore the Lord said to Solomon , “ Since this has been your practice and you have not kept my covenant and my statutes that I have commanded you, I will surely tear the kingdom from you and will give it to your servant .
- **Psa 89:3** (✓) *target: covenant*
  > Psa 89:3 You have said, “I have made a covenant with my chosen one ; I have sworn to David my servant :
- **Psa 89:28** (✓) *target: covenant*
  > Psa 89:28 My steadfast love I will keep for him forever , and my covenant will stand firm for him .
- **Psa 89:34** (✓) *target: covenant*
  > Psa 89:34 I will not violate my covenant or alter the word that went forth from my lips .
- **Psa 89:39** (✓) *target: covenant*
  > Psa 89:39 You have renounced the covenant with your servant ; you have defiled his crown in the dust .
- **Psa 132:12** (✓) *target: covenant*
  > Psa 132:12 If your sons keep my covenant and my testimonies that I shall teach them, their sons also forever shall sit on your throne .”
- **Jer 33:20** (✓) *target: covenant*
  > Jer 33:20 “ Thus says the Lord : If you can break my covenant with the day and my covenant with the night , so that day and night will not come at their appointed time ,
- **Jer 33:21** (✓) *target: covenant*
  > Jer 33:21 then also my covenant with David my servant may be broken , so that he shall not have a son to reign on his throne , and my covenant with the Levitical priests my ministers .
- **Jer 33:25** (✓) *target: covenant*
  > Jer 33:25 Thus says the Lord : If I have not established my covenant with day and night and the fixed order of heaven and earth ,
- **Dan 9:27** (✓) *target: covenant*
  > Dan 9:27 And he shall make a strong covenant with many for one week , and for half of the week he shall put an end to sacrifice and offering . And on the wing of abominations shall come one who makes desolate , until the decreed end is poured out on the desolator .”
- **Dan 11:22** (✓) *target: covenant*
  > Dan 11:22 Armies shall be utterly swept away before him and broken , even the prince of the covenant .
- **Dan 11:28** (✓) *target: covenant*
  > Dan 11:28 And he shall return to his land with great wealth , but his heart shall be set against the holy covenant . And he shall work his will and return to his own land .
- **Dan 11:30** (✓) *target: covenant*
  > Dan 11:30 For ships of Kittim shall come against him, and he shall be afraid and withdraw, and shall turn back and be enraged and take action against the holy covenant . He shall turn back and pay attention to those who forsake the holy covenant .
- **Dan 11:32** (✓) *target: covenant*
  > Dan 11:32 He shall seduce with flattery those who violate the covenant , but the people who know their God shall stand firm and take action .

**Group `765-005`** (13 verses — anchors: Job 31:1)

- **Job 31:1** 🔵 (✓) *target: covenant*
  > Job 31:1 “I have made a covenant with my eyes ; how then could I gaze at a virgin ?
- **1Sa 18:3** (✓) *target: covenant*
  > 1Sa 18:3 Then Jonathan made a covenant with David , because he loved him as his own soul .
- **1Sa 20:8** (✓) *target: covenant*
  > 1Sa 20:8 Therefore deal kindly with your servant , for you have brought your servant into a covenant of the Lord with you. But if there is guilt in me, kill me yourself, for why should you bring me to your father ?”
- **1Sa 23:18** (✓) *target: covenant*
  > 1Sa 23:18 And the two of them made a covenant before the Lord . David remained at Horesh , and Jonathan went home .
- **1Ki 3:15** (✓) *target: covenant*
  > 1Ki 3:15 And Solomon awoke , and behold , it was a dream . Then he came to Jerusalem and stood before the ark of the covenant of the Lord , and offered up burnt offerings and peace offerings , and made a feast for all his servants .
- **Neh 1:5** (✓) *target: covenant*
  > Neh 1:5 And I said , “ O Lord God of heaven , the great and awesome God who keeps covenant and steadfast love with those who love him and keep his commandments ,
- **Job 5:23** (✓) *target: league*
  > Job 5:23 For you shall be in league with the stones of the field , and the beasts of the field shall be at peace with you .
- **Psa 55:20** (✓) *target: covenant*
  > Psa 55:20 My companion stretched out his hand against his friends ; he violated his covenant .
- **Psa 83:5** (✓) *target: covenant*
  > Psa 83:5 For they conspire with one accord ; against you they make a covenant —
- **Pro 2:17** (✓) *target: covenant*
  > Pro 2:17 who forsakes the companion of her youth and forgets the covenant of her God ;
- **Amo 1:9** (✓) *target: covenant*
  > Amo 1:9 Thus says the Lord : “For three transgressions of Tyre , and for four , I will not revoke the punishment , because they delivered up a whole people to Edom , and did not remember the covenant of brotherhood .
- **Mal 2:10** (✓) *target: covenant*
  > Mal 2:10 Have we not all one Father ? Has not one God created us? Why then are we faithless to one another , profaning the covenant of our fathers ?
- **Mal 2:14** (✓) *target: covenant*
  > Mal 2:14 But you say , “ Why does he not?” Because the Lord was witness between you and the wife of your youth , to whom you have been faithless , though she is your companion and your wife by covenant .

**Group `UNCLASSIFIED`** (79 verses)

- **Gen 14:13** (—) *target: of*
  > Gen 14:13 Then one who had escaped came and told Abram the Hebrew , who was living by the oaks of Mamre the Amorite , brother of Eshcol and of Aner . These were allies of Abram .
- **Gen 21:27** (—) *target: covenant*
  > Gen 21:27 So Abraham took sheep and oxen and gave them to Abimelech , and the two men made a covenant .
- **Gen 21:32** (—) *target: covenant*
  > Gen 21:32 So they made a covenant at Beersheba . Then Abimelech and Phicol the commander of his army rose up and returned to the land of the Philistines .
- **Gen 26:28** (—) *target: covenant*
  > Gen 26:28 They said , “We see plainly that the Lord has been with you. So we said , let there be a sworn pact between us, between you and us, and let us make a covenant with you ,
- **Gen 31:44** (—) *target: covenant*
  > Gen 31:44 Come now , let us make a covenant , you and I. And let it be a witness between you and me .”
- **Exo 23:32** (—) *target: covenant*
  > Exo 23:32 You shall make no covenant with them and their gods .
- **Lev 2:13** (—) *target: covenant*
  > Lev 2:13 You shall season all your grain offerings with salt . You shall not let the salt of the covenant with your God be missing from your grain offering ; with all your offerings you shall offer salt .
- **Lev 24:8** (—) *target: covenant*
  > Lev 24:8 Every Sabbath day Aaron shall arrange it before the Lord regularly ; it is from the people of Israel as a covenant forever .
- **Lev 26:9** (—) *target: covenant*
  > Lev 26:9 I will turn to you and make you fruitful and multiply you and will confirm my covenant with you .
- **Lev 26:15** (—) *target: covenant*
  > Lev 26:15 if you spurn my statutes , and if your soul abhors my rules , so that you will not do all my commandments , but break my covenant ,
- **Lev 26:25** (—) *target: covenant*
  > Lev 26:25 And I will bring a sword upon you, that shall execute vengeance for the covenant . And if you gather within your cities , I will send pestilence among you, and you shall be delivered into the hand of the enemy .
- **Num 10:33** (—) *target: covenant*
  > Num 10:33 So they set out from the mount of the Lord three days ’ journey . And the ark of the covenant of the Lord went before them three days ’ journey , to seek out a resting place for them.
- **Num 14:44** (—) *target: covenant*
  > Num 14:44 But they presumed to go up to the heights of the hill country , although neither the ark of the covenant of the Lord nor Moses departed out of the camp .
- **Num 25:12** (—) *target: covenant*
  > Num 25:12 Therefore say , ‘ Behold , I give to him my covenant of peace ,
- **Num 25:13** (—) *target: covenant*
  > Num 25:13 and it shall be to him and to his descendants after him the covenant of a perpetual priesthood , because he was jealous for his God and made atonement for the people of Israel .’”
- **Deu 7:2** (—) *target: covenant*
  > Deu 7:2 and when the Lord your God gives them over to you, and you defeat them, then you must devote them to complete destruction . You shall make no covenant with them and show no mercy to them .
- **Deu 9:11** (—) *target: covenant*
  > Deu 9:11 And at the end of forty days and forty nights the Lord gave me the two tablets of stone , the tablets of the covenant .
- **Deu 9:15** (—) *target: covenant*
  > Deu 9:15 So I turned and came down from the mountain , and the mountain was burning with fire . And the two tablets of the covenant were in my two hands .
- **Deu 10:8** (—) *target: covenant*
  > Deu 10:8 At that time the Lord set apart the tribe of Levi to carry the ark of the covenant of the Lord to stand before the Lord to minister to him and to bless in his name , to this day .
- **Deu 31:25** (—) *target: covenant*
  > Deu 31:25 Moses commanded the Levites who carried the ark of the covenant of the Lord ,
- **Jos 3:3** (—) *target: covenant*
  > Jos 3:3 and commanded the people , “ As soon as you see the ark of the covenant of the Lord your God being carried by the Levitical priests , then you shall set out from your place and follow it .
- **Jos 3:6** (—) *target: covenant*
  > Jos 3:6 And Joshua said to the priests , “Take up the ark of the covenant and pass on before the people .” So they took up the ark of the covenant and went before the people .
- **Jos 3:8** (—) *target: covenant*
  > Jos 3:8 And as for you , command the priests who bear the ark of the covenant , ‘When you come to the brink of the waters of the Jordan , you shall stand still in the Jordan .’”
- **Jos 3:11** (—) *target: covenant*
  > Jos 3:11 Behold , the ark of the covenant of the Lord of all the earth is passing over before you into the Jordan .
- **Jos 3:14** (—) *target: covenant*
  > Jos 3:14 So when the people set out from their tents to pass over the Jordan with the priests bearing the ark of the covenant before the people ,
- **Jos 3:17** (—) *target: covenant*
  > Jos 3:17 Now the priests bearing the ark of the covenant of the Lord stood firmly on dry ground in the midst of the Jordan , and all Israel was passing over on dry ground until all the nation finished passing over the Jordan .
- **Jos 4:7** (—) *target: covenant*
  > Jos 4:7 then you shall tell them that the waters of the Jordan were cut off before the ark of the covenant of the Lord . When it passed over the Jordan , the waters of the Jordan were cut off . So these stones shall be to the people of Israel a memorial forever .”
- **Jos 4:9** (—) *target: covenant*
  > Jos 4:9 And Joshua set up twelve stones in the midst of the Jordan , in the place where the feet of the priests bearing the ark of the covenant had stood ; and they are there to this day .
- **Jos 4:18** (—) *target: covenant*
  > Jos 4:18 And when the priests bearing the ark of the covenant of the Lord came up from the midst of the Jordan , and the soles of the priests ’ feet were lifted up on dry ground , the waters of the Jordan returned to their place and overflowed all its banks , as before .
- **Jos 6:6** (—) *target: covenant*
  > Jos 6:6 So Joshua the son of Nun called the priests and said to them, “Take up the ark of the covenant and let seven priests bear seven trumpets of rams’ horns before the ark of the Lord .”
- **Jos 6:8** (—) *target: covenant*
  > Jos 6:8 And just as Joshua had commanded the people , the seven priests bearing the seven trumpets of rams’ horns before the Lord went forward , blowing the trumpets , with the ark of the covenant of the Lord following them .
- **Jos 8:33** (—) *target: covenant*
  > Jos 8:33 And all Israel , sojourner as well as native born , with their elders and officers and their judges , stood on opposite sides of the ark before the Levitical priests who carried the ark of the covenant of the Lord , half of them in front of Mount Gerizim and half of them in front of Mount Ebal , just as Moses the servant of the Lord had commanded at the first, to bless the people of Israel .
- **Jos 9:6** (—) *target: covenant*
  > Jos 9:6 And they went to Joshua in the camp at Gilgal and said to him and to the men of Israel , “We have come from a distant country , so now make a covenant with us.”
- **Jos 9:7** (—) *target: covenant*
  > Jos 9:7 But the men of Israel said to the Hivites , “ Perhaps you live among us; then how can we make a covenant with you?”
- **Jos 9:11** (—) *target: covenant*
  > Jos 9:11 So our elders and all the inhabitants of our country said to us, ‘ Take provisions in your hand for the journey and go to meet them and say to them, “We are your servants . Come now , make a covenant with us.”’
- **Jos 9:15** (—) *target: covenant*
  > Jos 9:15 And Joshua made peace with them and made a covenant with them, to let them live , and the leaders of the congregation swore to them.
- **Jos 9:16** (—) *target: covenant*
  > Jos 9:16 At the end of three days after they had made a covenant with them, they heard that they were their neighbors and that they lived among them.
- **Judg 20:27** (—) *target: covenant*
  > Judg 20:27 And the people of Israel inquired of the Lord (for the ark of the covenant of God was there in those days ,
- **1Sa 4:3** (—) *target: covenant*
  > 1Sa 4:3 And when the people came to the camp , the elders of Israel said , “ Why has the Lord defeated us today before the Philistines ? Let us bring the ark of the covenant of the Lord here from Shiloh , that it may come among us and save us from the power of our enemies .”
- **1Sa 4:4** (—) *target: covenant*
  > 1Sa 4:4 So the people sent to Shiloh and brought from there the ark of the covenant of the Lord of hosts , who is enthroned on the cherubim . And the two sons of Eli , Hophni and Phinehas , were there with the ark of the covenant of God .
- **1Sa 4:5** (—) *target: covenant*
  > 1Sa 4:5 As soon as the ark of the covenant of the Lord came into the camp , all Israel gave a mighty shout , so that the earth resounded .
- **1Sa 11:1** (—) *target: treaty*
  > 1Sa 11:1 Then Nahash the Ammonite went up and besieged Jabesh - gilead , and all the men of Jabesh said to Nahash , “ Make a treaty with us, and we will serve you .”
- **2Sa 3:12** (—) *target: covenant*
  > 2Sa 3:12 And Abner sent messengers to David on his behalf, saying , “ To whom does the land belong? Make your covenant with me, and behold , my hand shall be with you to bring over all Israel to you.”
- **2Sa 3:13** (—) *target: covenant*
  > 2Sa 3:13 And he said , “ Good ; I will make a covenant with you. But one thing I require of you; that is , you shall not see my face unless you first bring Michal , Saul’s daughter , when you come to see my face .”
- **2Sa 3:21** (—) *target: covenant*
  > 2Sa 3:21 And Abner said to David , “I will arise and go and will gather all Israel to my lord the king , that they may make a covenant with you, and that you may reign over all that your heart desires .” So David sent Abner away, and he went in peace .
- **2Sa 5:3** (—) *target: covenant*
  > 2Sa 5:3 So all the elders of Israel came to the king at Hebron , and King David made a covenant with them at Hebron before the Lord , and they anointed David king over Israel .
- **2Sa 15:24** (—) *target: covenant*
  > 2Sa 15:24 And Abiathar came up , and behold , Zadok came also with all the Levites , bearing the ark of the covenant of God . And they set down the ark of God until the people had all passed out of the city .
- **1Ki 5:12** (—) *target: treaty*
  > 1Ki 5:12 And the Lord gave Solomon wisdom , as he promised him. And there was peace between Hiram and Solomon , and the two of them made a treaty .
- **1Ki 6:19** (—) *target: covenant*
  > 1Ki 6:19 The inner sanctuary he prepared in the innermost part of the house , to set there the ark of the covenant of the Lord .
- **1Ki 8:1** (—) *target: covenant*
  > 1Ki 8:1 Then Solomon assembled the elders of Israel and all the heads of the tribes , the leaders of the fathers’ houses of the people of Israel , before King Solomon in Jerusalem , to bring up the ark of the covenant of the Lord out of the city of David , which is Zion .
- **1Ki 8:6** (—) *target: covenant*
  > 1Ki 8:6 Then the priests brought the ark of the covenant of the Lord to its place in the inner sanctuary of the house , in the Most Holy Place , underneath the wings of the cherubim .
- **1Ki 8:21** (—) *target: covenant*
  > 1Ki 8:21 And there I have provided a place for the ark , in which is the covenant of the Lord that he made with our fathers , when he brought them out of the land of Egypt .”
- **1Ki 15:19** (—) *target: covenant*
  > 1Ki 15:19 “Let there be a covenant between me and you, as there was between my father and your father . Behold , I am sending to you a present of silver and gold . Go , break your covenant with Baasha king of Israel , that he may withdraw from me .”
- **1Ki 19:10** (—) *target: covenant*
  > 1Ki 19:10 He said , “I have been very jealous for the Lord , the God of hosts . For the people of Israel have forsaken your covenant , thrown down your altars , and killed your prophets with the sword , and I , even I only , am left , and they seek my life , to take it away .”
- **1Ki 19:14** (—) *target: covenant*
  > 1Ki 19:14 He said , “I have been very jealous for the Lord , the God of hosts . For the people of Israel have forsaken your covenant , thrown down your altars , and killed your prophets with the sword , and I , even I only , am left , and they seek my life , to take it away .”
- **1Ki 20:34** (—) *target: terms*
  > 1Ki 20:34 And Ben-hadad said to him, “The cities that my father took from your father I will restore , and you may establish bazaars for yourself in Damascus , as my father did in Samaria .” And Ahab said, “I will let you go on these terms .” So he made a covenant with him and let him go .
- **2Ki 11:4** (—) *target: covenant*
  > 2Ki 11:4 But in the seventh year Jehoiada sent and brought the captains of the Carites and of the guards , and had them come to him in the house of the Lord . And he made a covenant with them and put them under oath in the house of the Lord , and he showed them the king’s son .
- **2Ki 11:17** (—) *target: covenant*
  > 2Ki 11:17 And Jehoiada made a covenant between the Lord and the king and people , that they should be the Lord’s people , and also between the king and the people .
- **Ezr 10:3** (—) *target: covenant*
  > Ezr 10:3 Therefore let us make a covenant with our God to put away all these wives and their children , according to the counsel of my lord and of those who tremble at the commandment of our God , and let it be done according to the Law .
- **Neh 13:29** (—) *target: covenant*
  > Neh 13:29 Remember them, O my God , because they have desecrated the priesthood and the covenant of the priesthood and the Levites .
- **Job 41:4** (—) *target: covenant*
  > Job 41:4 Will he make a covenant with you to take him for your servant forever ?
- **Psa 74:20** (—) *target: covenant*
  > Psa 74:20 Have regard for the covenant , for the dark places of the land are full of the habitations of violence .
- **Isa 28:15** (—) *target: covenant*
  > Isa 28:15 Because you have said , “We have made a covenant with death , and with Sheol we have an agreement , when the overwhelming whip passes through it will not come to us, for we have made lies our refuge , and in falsehood we have taken shelter ”;
- **Isa 28:18** (—) *target: covenant*
  > Isa 28:18 Then your covenant with death will be annulled , and your agreement with Sheol will not stand ; when the overwhelming scourge passes through , you will be beaten down by it.
- **Isa 33:8** (—) *target: Covenants*
  > Isa 33:8 The highways lie waste ; the traveler ceases . Covenants are broken ; cities are despised ; there is no regard for man .
- **Isa 42:6** (—) *target: covenant*
  > Isa 42:6 “ I am the Lord ; I have called you in righteousness ; I will take you by the hand and keep you; I will give you as a covenant for the people , a light for the nations ,
- **Isa 49:8** (—) *target: covenant*
  > Isa 49:8 Thus says the Lord : “ In a time of favor I have answered you; in a day of salvation I have helped you; I will keep you and give you as a covenant to the people , to establish the land , to apportion the desolate heritages ,
- **Jer 3:16** (—) *target: covenant*
  > Jer 3:16 And when you have multiplied and been fruitful in the land , in those days , declares the Lord , they shall no more say , “The ark of the covenant of the Lord .” It shall not come to mind or be remembered or missed ; it shall not be made again .
- **Eze 16:61** (—) *target: covenant*
  > Eze 16:61 Then you will remember your ways and be ashamed when you take your sisters , both your elder and your younger , and I give them to you as daughters , but not on account of the covenant with you.
- **Eze 17:13** (—) *target: covenant*
  > Eze 17:13 And he took one of the royal offspring and made a covenant with him, putting him under oath ( the chief men of the land he had taken away ),
- **Eze 17:14** (—) *target: covenant*
  > Eze 17:14 that the kingdom might be humble and not lift itself up , and keep his covenant that it might stand .
- **Eze 17:15** (—) *target: covenant*
  > Eze 17:15 But he rebelled against him by sending his ambassadors to Egypt , that they might give him horses and a large army . Will he thrive ? Can one escape who does such things ? Can he break the covenant and yet escape ?
- **Eze 17:16** (—) *target: covenant*
  > Eze 17:16 “As I live , declares the Lord God , surely in the place where the king dwells who made him king , whose oath he despised , and whose covenant with him he broke , in Babylon he shall die .
- **Eze 17:18** (—) *target: covenant*
  > Eze 17:18 He despised the oath in breaking the covenant , and behold , he gave his hand and did all these things ; he shall not escape .
- **Eze 17:19** (—) *target: covenant*
  > Eze 17:19 Therefore thus says the Lord God : As I live , surely it is my oath that he despised , and my covenant that he broke . I will return it upon his head .
- **Eze 30:5** (—) *target: league*
  > Eze 30:5 Cush , and Put , and Lud , and all Arabia , and Libya , and the people of the land that is in league , shall fall with them by the sword .
- **Hos 2:18** (—) *target: covenant*
  > Hos 2:18 And I will make for them a covenant on that day with the beasts of the field , the birds of the heavens , and the creeping things of the ground . And I will abolish the bow , the sword , and war from the land , and I will make you lie down in safety .
- **Obd 7** (—) *target: allies*
  > Obd 7 All your allies have driven you to your border ; those at peace with you have deceived you; they have prevailed against you; those who eat your bread have set a trap beneath you— you have no understanding .
- **Zec 11:10** (—) *target: covenant*
  > Zec 11:10 And I took my staff Favor , and I broke it, annulling the covenant that I had made with all the peoples .

### `H1286` — 1/1 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (1 verse)

- **Judg 9:46** (✗) *target: El-berith*
  > Judg 9:46 When all the leaders of the Tower of Shechem heard of it, they entered the stronghold of the house of El-berith .
  - notes: All-set-aside: place name/pagan temple reference, no inner-being engagement

### `H3748` — 4/4 classified · 2 anchor verse(s)

**Group `3306-001`** (2 verses — anchors: Deu 24:1)

- **Deu 24:1** 🔵 (✓) *target: divorce*
  > Deu 24:1 “When a man takes a wife and marries her, if then she finds no favor in his eyes because he has found some indecency in her, and he writes her a certificate of divorce and puts it in her hand and sends her out of his house , and she departs out of his house,
- **Deu 24:3** (✓) *target: divorce*
  > Deu 24:3 and the latter man hates her and writes her a certificate of divorce and puts it in her hand and sends her out of his house , or if the latter man dies , who took her to be his wife ,

**Group `3306-002`** (2 verses — anchors: Isa 50:1)

- **Isa 50:1** 🔵 (✓) *target: divorce*
  > Isa 50:1 Thus says the Lord : “ Where is your mother’s certificate of divorce , with which I sent her away ? Or which of my creditors is it to whom I have sold you? Behold , for your iniquities you were sold , and for your transgressions your mother was sent away .
- **Jer 3:8** (✓) *target: divorce*
  > Jer 3:8 She saw that for all the adulteries of that faithless one, Israel , I had sent her away with a decree of divorce . Yet her treacherous sister Judah did not fear , but she too went and played the whore .

### `H3772G` — 50/50 classified · 2 anchor verse(s)

**Group `767-001`** (1 verse — anchors: Jer 34:18)

- **Jer 34:18** 🔵 (✓) *target: made*
  > Jer 34:18 And the men who transgressed my covenant and did not keep the terms of the covenant that they made before me, I will make them like the calf that they cut in two and passed between its parts —

**Group `767-002`** (4 verses — anchors: Pro 10:31)

- **Pro 10:31** 🔵 (✓) *target: cut off*
  > Pro 10:31 The mouth of the righteous brings forth wisdom , but the perverse tongue will be cut off .
- **Lev 26:30** (✓) *target: cut down*
  > Lev 26:30 And I will destroy your high places and cut down your incense altars and cast your dead bodies upon the dead bodies of your idols , and my soul will abhor you .
- **1Sa 24:11** (✓) *target: cut*
  > 1Sa 24:11 See , my father , see the corner of your robe in my hand . For by the fact that I cut off the corner of your robe and did not kill you, you may know and see that there is no wrong or treason in my hands . I have not sinned against you , though you hunt my life to take it .
- **Job 14:7** (✓) *target: cut down*
  > Job 14:7 “For there is hope for a tree , if it be cut down , that it will sprout again , and that its shoots will not cease .

**Group `SET-ASIDE`** (45 verses)

- **Exo 4:25** (✗) *target: cut off*
  > Exo 4:25 Then Zipporah took a flint and cut off her son’s foreskin and touched Moses’ feet with it and said , “ Surely you are a bridegroom of blood to me !”
  - notes: Physical cutting with no inner-being engagement at term level
- **Exo 34:13** (✗) *target: cut down*
  > Exo 34:13 You shall tear down their altars and break their pillars and cut down their Asherim
  - notes: Physical cutting with no inner-being engagement at term level
- **Lev 22:24** (✗) *target: cut*
  > Lev 22:24 Any animal that has its testicles bruised or crushed or torn or cut you shall not offer to the Lord ; you shall not do it within your land ,
  - notes: Physical cutting with no inner-being engagement at term level
- **Num 13:23** (✗) *target: down*
  > Num 13:23 And they came to the Valley of Eshcol and cut down from there a branch with a single cluster of grapes , and they carried it on a pole between two of them; they also brought some pomegranates and figs .
  - notes: Physical cutting with no inner-being engagement at term level
- **Num 13:24** (✗) *target: down*
  > Num 13:24 That place was called the Valley of Eshcol , because of the cluster that the people of Israel cut down from there .
  - notes: Physical cutting with no inner-being engagement at term level
- **Deu 19:5** (✗) *target: cut down*
  > Deu 19:5 as when someone goes into the forest with his neighbor to cut wood , and his hand swings the axe to cut down a tree , and the head slips from the handle and strikes his neighbor so that he dies — he may flee to one of these cities and live ,
  - notes: Physical cutting with no inner-being engagement at term level
- **Deu 20:19** (✗) *target: cut them down*
  > Deu 20:19 “When you besiege a city for a long time , making war against it in order to take it, you shall not destroy its trees by wielding an axe against them. You may eat from them, but you shall not cut them down . Are the trees in the field human , that they should be besieged by you ?
  - notes: Physical cutting with no inner-being engagement at term level
- **Deu 20:20** (✗) *target: cut down*
  > Deu 20:20 Only the trees that you know are not trees for food you may destroy and cut down , that you may build siegeworks against the city that makes war with you, until it falls .
  - notes: Physical cutting with no inner-being engagement at term level
- **Deu 23:1** (✗) *target: cut off*
  > Deu 23:1 “No one whose testicles are crushed or whose male organ is cut off shall enter the assembly of the Lord .
  - notes: Physical cutting with no inner-being engagement at term level
- **Jos 3:13** (✗) *target: cut off*
  > Jos 3:13 And when the soles of the feet of the priests bearing the ark of the Lord , the Lord of all the earth , shall rest in the waters of the Jordan , the waters of the Jordan shall be cut off from flowing, and the waters coming down from above shall stand in one heap .”
  - notes: Physical cutting with no inner-being engagement at term level
- **Jos 3:16** (✗) *target: cut off*
  > Jos 3:16 the waters coming down from above stood and rose up in a heap very far away, at Adam , the city that is beside Zarethan , and those flowing down toward the Sea of the Arabah , the Salt Sea , were completely cut off . And the people passed over opposite Jericho .
  - notes: Physical cutting with no inner-being engagement at term level
- **Jos 4:7** (✗) *target: cut off*
  > Jos 4:7 then you shall tell them that the waters of the Jordan were cut off before the ark of the covenant of the Lord . When it passed over the Jordan , the waters of the Jordan were cut off . So these stones shall be to the people of Israel a memorial forever .”
  - notes: Physical cutting with no inner-being engagement at term level
- **Jos 9:23** (✗) *target: but*
  > Jos 9:23 Now therefore you are cursed , and some of you shall never be anything but servants , cutters of wood and drawers of water for the house of my God .”
  - notes: Physical cutting with no inner-being engagement at term level
- **Judg 6:25** (✗) *target: cut down*
  > Judg 6:25 That night the Lord said to him, “ Take your father’s bull , and the second bull seven years old , and pull down the altar of Baal that your father has, and cut down the Asherah that is beside it
  - notes: Physical cutting with no inner-being engagement at term level
- **Judg 6:26** (✗) *target: cut down*
  > Judg 6:26 and build an altar to the Lord your God on the top of the stronghold here , with stones laid in due order . Then take the second bull and offer it as a burnt offering with the wood of the Asherah that you shall cut down .”
  - notes: Physical cutting with no inner-being engagement at term level
- **Judg 6:28** (✗) *target: cut down*
  > Judg 6:28 When the men of the town rose early in the morning , behold , the altar of Baal was broken down , and the Asherah beside it was cut down , and the second bull was offered on the altar that had been built .
  - notes: Physical cutting with no inner-being engagement at term level
- **Judg 6:30** (✗) *target: cut down*
  > Judg 6:30 Then the men of the town said to Joash , “ Bring out your son , that he may die , for he has broken down the altar of Baal and cut down the Asherah beside it .”
  - notes: Physical cutting with no inner-being engagement at term level
- **Judg 9:48** (✗) *target: cut down*
  > Judg 9:48 And Abimelech went up to Mount Zalmon , he and all the people who were with him. And Abimelech took an axe in his hand and cut down a bundle of brushwood and took it up and laid it on his shoulder . And he said to the men who were with him, “ What you have seen me do , hurry and do as I have done .”
  - notes: Physical cutting with no inner-being engagement at term level
- **Judg 9:49** (✗) *target: cut down*
  > Judg 9:49 So every one of the people cut down his bundle and following Abimelech put it against the stronghold , and they set the stronghold on fire over them, so that all the people of the Tower of Shechem also died , about 1,000 men and women .
  - notes: Physical cutting with no inner-being engagement at term level
- **2Sa 10:4** (✗) *target: cut off*
  > 2Sa 10:4 So Hanun took David’s servants and shaved off half the beard of each and cut off their garments in the middle , at their hips , and sent them away .
  - notes: Physical cutting with no inner-being engagement at term level
- **2Sa 20:22** (✗) *target: cut off*
  > 2Sa 20:22 Then the woman went to all the people in her wisdom . And they cut off the head of Sheba the son of Bichri and threw it out to Joab . So he blew the trumpet , and they dispersed from the city , every man to his home . And Joab returned to Jerusalem to the king .
  - notes: Physical cutting with no inner-being engagement at term level
- **1Ki 5:6** (✗) *target: cut*
  > 1Ki 5:6 Now therefore command that cedars of Lebanon be cut for me. And my servants will join your servants , and I will pay you for your servants such wages as you set , for you know that there is no one among us who knows how to cut timber like the Sidonians .”
  - notes: Physical cutting with no inner-being engagement at term level
- **1Ki 15:13** (✗) *target: cut down*
  > 1Ki 15:13 He also removed Maacah his mother from being queen mother because she had made an abominable image for Asherah . And Asa cut down her image and burned it at the brook Kidron .
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ki 18:4** (✗) *target: cut down*
  > 2Ki 18:4 He removed the high places and broke the pillars and cut down the Asherah . And he broke in pieces the bronze serpent that Moses had made , for until those days the people of Israel had made offerings to it (it was called Nehushtan ).
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ki 19:23** (✗) *target: felled*
  > 2Ki 19:23 By your messengers you have mocked the Lord , and you have said , ‘ With my many chariots I have gone up the heights of the mountains , to the far recesses of Lebanon ; I felled its tallest cedars , its choicest cypresses ; I entered its farthest lodging place , its most fruitful forest .
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ki 23:14** (✗) *target: cut down*
  > 2Ki 23:14 And he broke in pieces the pillars and cut down the Asherim and filled their places with the bones of men .
  - notes: Physical cutting with no inner-being engagement at term level
- **1Ch 19:4** (✗) *target: cut off*
  > 1Ch 19:4 So Hanun took David’s servants and shaved them and cut off their garments in the middle , at their hips , and sent them away ;
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ch 2:8** (✗) *target: cut*
  > 2Ch 2:8 Send me also cedar , cypress , and algum timber from Lebanon , for I know that your servants know how to cut timber in Lebanon . And my servants will be with your servants ,
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ch 2:10** (✗) *target: cut*
  > 2Ch 2:10 I will give for your servants , the woodsmen who cut timber , 20,000 cors of crushed wheat , 20,000 cors of barley , 20,000 baths of wine , and 20,000 baths of oil .”
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ch 2:16** (✗) *target: cut*
  > 2Ch 2:16 And we will cut whatever timber you need from Lebanon and bring it to you in rafts by sea to Joppa , so that you may take it up to Jerusalem .”
  - notes: Physical cutting with no inner-being engagement at term level
- **2Ch 15:16** (✗) *target: cut down*
  > 2Ch 15:16 Even Maacah , his mother , King Asa removed from being queen mother because she had made a detestable image for Asherah . Asa cut down her image , crushed it, and burned it at the brook Kidron .
  - notes: Physical cutting with no inner-being engagement at term level
- **Isa 9:14** (✗) *target: cut off*
  > Isa 9:14 So the Lord cut off from Israel head and tail , palm branch and reed in one day —
  - notes: Physical cutting with no inner-being engagement at term level
- **Isa 14:8** (✗) *target: woodcutter*
  > Isa 14:8 , The cypresses rejoice at you, the cedars of Lebanon , saying, ‘Since you were laid low , no woodcutter comes up against us .’
  - notes: Physical cutting with no inner-being engagement at term level
- **Isa 18:5** (✗) *target: off*
  > Isa 18:5 For before the harvest , when the blossom is over , and the flower becomes a ripening grape , he cuts off the shoots with pruning hooks , and the spreading branches he lops off and clears away .
  - notes: Physical cutting with no inner-being engagement at term level
- **Isa 37:24** (✗) *target: cut down*
  > Isa 37:24 By your servants you have mocked the Lord , and you have said , With my many chariots I have gone up the heights of the mountains , to the far recesses of Lebanon , to cut down its tallest cedars , its choicest cypresses , to come to its remotest height , its most fruitful forest .
  - notes: Physical cutting with no inner-being engagement at term level
- **Isa 44:14** (✗) *target: down*
  > Isa 44:14 He cuts down cedars , or he chooses a cypress tree or an oak and lets it grow strong among the trees of the forest . He plants a cedar and the rain nourishes it.
  - notes: Physical cutting with no inner-being engagement at term level
- **Jer 6:6** (✗) *target: down*
  > Jer 6:6 For thus says the Lord of hosts : “Cut down her trees ; cast up a siege mound against Jerusalem . This is the city that must be punished ; there is nothing but oppression within her.
  - notes: Physical cutting with no inner-being engagement at term level
- **Jer 10:3** (✗) *target: cut down*
  > Jer 10:3 for the customs of the peoples are vanity . A tree from the forest is cut down and worked with an axe by the hands of a craftsman .
  - notes: Physical cutting with no inner-being engagement at term level
- **Jer 22:7** (✗) *target: cut down*
  > Jer 22:7 I will prepare destroyers against you, each with his weapons , and they shall cut down your choicest cedars and cast them into the fire .
  - notes: Physical cutting with no inner-being engagement at term level
- **Jer 46:23** (✗) *target: cut down*
  > Jer 46:23 They shall cut down her forest , declares the Lord , though it is impenetrable , because they are more numerous than locusts ; they are without number .
  - notes: Physical cutting with no inner-being engagement at term level
- **Eze 16:4** (✗) *target: cut*
  > Eze 16:4 And as for your birth , on the day you were born your cord was not cut , nor were you washed with water to cleanse you, nor rubbed with salt , nor wrapped in swaddling cloths .
  - notes: Physical cutting with no inner-being engagement at term level
- **Eze 31:12** (✗) *target: down*
  > Eze 31:12 Foreigners , the most ruthless of nations , have cut it down and left it. On the mountains and in all the valleys its branches have fallen , and its boughs have been broken in all the ravines of the land , and all the peoples of the earth have gone away from its shadow and left it .
  - notes: Physical cutting with no inner-being engagement at term level
- **Nah 2:13** (✗) *target: cut*
  > Nah 2:13 Behold , I am against you, declares the Lord of hosts , and I will burn your chariots in smoke , and the sword shall devour your young lions . I will cut off your prey from the earth , and the voice of your messengers shall no longer be heard .
  - notes: Physical cutting with no inner-being engagement at term level
- **Nah 3:15** (✗) *target: cut*
  > Nah 3:15 There will the fire devour you; the sword will cut you off. It will devour you like the locust . Multiply yourselves like the locust ; multiply like the grasshopper !
  - notes: Physical cutting with no inner-being engagement at term level
- **Zep 1:4** (✗) *target: cut*
  > Zep 1:4 “I will stretch out my hand against Judah and against all the inhabitants of Jerusalem ; and I will cut off from this place the remnant of Baal and the name of the idolatrous priests along with the priests ,
  - notes: Physical cutting with no inner-being engagement at term level

### `H3772H` — 85/95 classified · 4 anchor verse(s)

**Group `3304-001`** (67 verses — anchors: Jer 31:33)

- **Jer 31:33** 🔵 (✓) *target: make*
  > Jer 31:33 For this is the covenant that I will make with the house of Israel after those days , declares the Lord : I will put my law within them, and I will write it on their hearts . And I will be their God , and they shall be my people .
- **Gen 15:18** (✓) *target: made*
  > Gen 15:18 On that day the Lord made a covenant with Abram , saying , “ To your offspring I give this land , from the river of Egypt to the great river , the river Euphrates ,
- **Gen 21:27** (✓) *target: made*
  > Gen 21:27 So Abraham took sheep and oxen and gave them to Abimelech , and the two men made a covenant .
- **Gen 21:32** (✓) *target: made*
  > Gen 21:32 So they made a covenant at Beersheba . Then Abimelech and Phicol the commander of his army rose up and returned to the land of the Philistines .
- **Gen 26:28** (✓) *target: make*
  > Gen 26:28 They said , “We see plainly that the Lord has been with you. So we said , let there be a sworn pact between us, between you and us, and let us make a covenant with you ,
- **Gen 31:44** (✓) *target: make*
  > Gen 31:44 Come now , let us make a covenant , you and I. And let it be a witness between you and me .”
- **Exo 23:32** (✓) *target: make*
  > Exo 23:32 You shall make no covenant with them and their gods .
- **Exo 24:8** (✓) *target: made*
  > Exo 24:8 And Moses took the blood and threw it on the people and said , “ Behold the blood of the covenant that the Lord has made with you in accordance with all these words .”
- **Exo 34:10** (✓) *target: making*
  > Exo 34:10 And he said , “ Behold , I am making a covenant . Before all your people I will do marvels , such as have not been created in all the earth or in any nation . And all the people among whom you are shall see the work of the Lord , for it is an awesome thing that I will do with you .
- **Exo 34:12** (✓) *target: make*
  > Exo 34:12 Take care , lest you make a covenant with the inhabitants of the land to which you go , lest it become a snare in your midst .
- **Exo 34:15** (✓) *target: make*
  > Exo 34:15 lest you make a covenant with the inhabitants of the land , and when they whore after their gods and sacrifice to their gods and you are invited , you eat of his sacrifice ,
- **Exo 34:27** (✓) *target: made*
  > Exo 34:27 And the Lord said to Moses , “ Write these words , for in accordance with these words I have made a covenant with you and with Israel .”
- **Deu 4:23** (✓) *target: made*
  > Deu 4:23 Take care , lest you forget the covenant of the Lord your God , which he made with you, and make a carved image , the form of anything that the Lord your God has forbidden you.
- **Deu 5:2** (✓) *target: made*
  > Deu 5:2 The Lord our God made a covenant with us in Horeb .
- **Deu 5:3** (✓) *target: make*
  > Deu 5:3 Not with our fathers did the Lord make this covenant , but with us , who are all of us here alive today .
- **Deu 7:2** (✓) *target: make*
  > Deu 7:2 and when the Lord your God gives them over to you, and you defeat them, then you must devote them to complete destruction . You shall make no covenant with them and show no mercy to them .
- **Deu 9:9** (✓) *target: made*
  > Deu 9:9 When I went up the mountain to receive the tablets of stone , the tablets of the covenant that the Lord made with you, I remained on the mountain forty days and forty nights . I neither ate bread nor drank water .
- **Deu 29:1** (✓) *target: make*
  > Deu 29:1 These are the words of the covenant that the Lord commanded Moses to make with the people of Israel in the land of Moab , besides the covenant that he had made with them at Horeb .
- **Deu 29:12** (✓) *target: making*
  > Deu 29:12 so that you may enter into the sworn covenant of the Lord your God , which the Lord your God is making with you today ,
- **Deu 29:14** (✓) *target: making*
  > Deu 29:14 It is not with you alone that I am making this sworn covenant ,
- **Deu 29:25** (✓) *target: made*
  > Deu 29:25 Then people will say , ‘It is because they abandoned the covenant of the Lord , the God of their fathers , which he made with them when he brought them out of the land of Egypt ,
- **Deu 31:16** (✓) *target: made*
  > Deu 31:16 And the Lord said to Moses , “ Behold , you are about to lie down with your fathers . Then this people will rise and whore after the foreign gods among them in the land that they are entering , and they will forsake me and break my covenant that I have made with them .
- **Jos 9:6** (✓) *target: make*
  > Jos 9:6 And they went to Joshua in the camp at Gilgal and said to him and to the men of Israel , “We have come from a distant country , so now make a covenant with us.”
- **Jos 9:7** (✓) *target: make*
  > Jos 9:7 But the men of Israel said to the Hivites , “ Perhaps you live among us; then how can we make a covenant with you?”
- **Jos 9:11** (✓) *target: make*
  > Jos 9:11 So our elders and all the inhabitants of our country said to us, ‘ Take provisions in your hand for the journey and go to meet them and say to them, “We are your servants . Come now , make a covenant with us.”’
- **Jos 9:15** (✓) *target: made*
  > Jos 9:15 And Joshua made peace with them and made a covenant with them, to let them live , and the leaders of the congregation swore to them.
- **Jos 9:16** (✓) *target: made*
  > Jos 9:16 At the end of three days after they had made a covenant with them, they heard that they were their neighbors and that they lived among them.
- **Jos 24:25** (✓) *target: made*
  > Jos 24:25 So Joshua made a covenant with the people that day , and put in place statutes and rules for them at Shechem .
- **Judg 2:2** (✓) *target: make*
  > Judg 2:2 and you shall make no covenant with the inhabitants of this land ; you shall break down their altars .’ But you have not obeyed my voice . What is this you have done ?
- **2Ki 11:17** (✓) *target: made*
  > 2Ki 11:17 And Jehoiada made a covenant between the Lord and the king and people , that they should be the Lord’s people , and also between the king and the people .
- **2Ki 17:15** (✓) *target: made*
  > 2Ki 17:15 They despised his statutes and his covenant that he made with their fathers and the warnings that he gave them. They went after false idols and became false , and they followed the nations that were around them, concerning whom the Lord had commanded them that they should not do like them .
- **2Ki 17:35** (✓) *target: made*
  > 2Ki 17:35 The Lord made a covenant with them and commanded them, “You shall not fear other gods or bow yourselves to them or serve them or sacrifice to them ,
- **2Ki 17:38** (✓) *target: made*
  > 2Ki 17:38 and you shall not forget the covenant that I have made with you. You shall not fear other gods ,
- **2Ki 23:3** (✓) *target: made*
  > 2Ki 23:3 And the king stood by the pillar and made a covenant before the Lord , to walk after the Lord and to keep his commandments and his testimonies and his statutes with all his heart and all his soul , to perform the words of this covenant that were written in this book . And all the people joined in the covenant .
- **1Ch 11:3** (✓) *target: made*
  > 1Ch 11:3 So all the elders of Israel came to the king at Hebron , and David made a covenant with them at Hebron before the Lord . And they anointed David king over Israel , according to the word of the Lord by Samuel .
- **1Ch 16:16** (✓) *target: made*
  > 1Ch 16:16 the covenant that he made with Abraham , his sworn promise to Isaac ,
- **2Ch 5:10** (✓) *target: covenant*
  > 2Ch 5:10 There was nothing in the ark except the two tablets that Moses put there at Horeb , where the Lord made a covenant with the people of Israel , when they came out of Egypt .
- **2Ch 6:11** (✓) *target: made*
  > 2Ch 6:11 And there I have set the ark , in which is the covenant of the Lord that he made with the people of Israel .”
- **2Ch 21:7** (✓) *target: made*
  > 2Ch 21:7 Yet the Lord was not willing to destroy the house of David , because of the covenant that he had made with David , and since he had promised to give a lamp to him and to his sons forever .
- **2Ch 23:3** (✓) *target: made*
  > 2Ch 23:3 And all the assembly made a covenant with the king in the house of God . And Jehoiada said to them, “ Behold , the king’s son ! Let him reign , as the Lord spoke concerning the sons of David .
- **2Ch 23:16** (✓) *target: made*
  > 2Ch 23:16 And Jehoiada made a covenant between himself and all the people and the king that they should be the Lord’s people .
- **2Ch 29:10** (✓) *target: make*
  > 2Ch 29:10 Now it is in my heart to make a covenant with the Lord , the God of Israel , in order that his fierce anger may turn away from us.
- **2Ch 34:31** (✓) *target: made*
  > 2Ch 34:31 And the king stood in his place and made a covenant before the Lord , to walk after the Lord and to keep his commandments and his testimonies and his statutes , with all his heart and all his soul , to perform the words of the covenant that were written in this book .
- **Ezr 10:3** (✓) *target: make*
  > Ezr 10:3 Therefore let us make a covenant with our God to put away all these wives and their children , according to the counsel of my lord and of those who tremble at the commandment of our God , and let it be done according to the Law .
- **Neh 9:8** (✓) *target: made*
  > Neh 9:8 You found his heart faithful before you, and made with him the covenant to give to his offspring the land of the Canaanite , the Hittite , the Amorite , the Perizzite , the Jebusite , and the Girgashite . And you have kept your promise , for you are righteous .
- **Neh 9:38** (✓) *target: make*
  > Neh 9:38 “Because of all this we make a firm covenant in writing ; on the sealed document are the names of our princes , our Levites , and our priests .
- **Psa 50:5** (✓) *target: made*
  > Psa 50:5 “ Gather to me my faithful ones , who made a covenant with me by sacrifice !”
- **Psa 89:3** (✓) *target: made*
  > Psa 89:3 You have said, “I have made a covenant with my chosen one ; I have sworn to David my servant :
- **Psa 105:9** (✓) *target: made*
  > Psa 105:9 the covenant that he made with Abraham , his sworn promise to Isaac ,
- **Isa 55:3** (✓) *target: make*
  > Isa 55:3 Incline your ear , and come to me; hear , that your soul may live ; and I will make with you an everlasting covenant , my steadfast , sure love for David .
- **Isa 57:8** (✓) *target: covenant*
  > Isa 57:8 Behind the door and the doorpost you have set up your memorial ; for , deserting me, you have uncovered your bed , you have gone up to it, you have made it wide ; and you have made a covenant for yourself with them, you have loved their bed , you have looked on nakedness .
- **Isa 61:8** (✓) *target: make*
  > Isa 61:8 For I the Lord love justice ; I hate robbery and wrong ; I will faithfully give them their recompense , and I will make an everlasting covenant with them .
- **Jer 31:31** (✓) *target: make*
  > Jer 31:31 “ Behold , the days are coming , declares the Lord , when I will make a new covenant with the house of Israel and the house of Judah ,
- **Jer 31:32** (✓) *target: made*
  > Jer 31:32 not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt , my covenant that they broke , though I was their husband , declares the Lord .
- **Jer 32:40** (✓) *target: make*
  > Jer 32:40 I will make with them an everlasting covenant , that I will not turn away from doing good to them . And I will put the fear of me in their hearts , that they may not turn from me .
- **Jer 34:8** (✓) *target: made*
  > Jer 34:8 The word that came to Jeremiah from the Lord , after King Zedekiah had made a covenant with all the people in Jerusalem to make a proclamation of liberty to them,
- **Jer 34:13** (✓) *target: made*
  > Jer 34:13 “ Thus says the Lord , the God of Israel : I myself made a covenant with your fathers when I brought them out of the land of Egypt , out of the house of slavery , saying ,
- **Jer 34:15** (✓) *target: made*
  > Jer 34:15 You recently repented and did what was right in my eyes by proclaiming liberty , each to his neighbor , and you made a covenant before me in the house that is called by my name ,
- **Jer 34:18** (✓) *target: made*
  > Jer 34:18 And the men who transgressed my covenant and did not keep the terms of the covenant that they made before me, I will make them like the calf that they cut in two and passed between its parts —
- **Eze 17:13** (✓) *target: made*
  > Eze 17:13 And he took one of the royal offspring and made a covenant with him, putting him under oath ( the chief men of the land he had taken away ),
- **Eze 34:25** (✓) *target: make*
  > Eze 34:25 “I will make with them a covenant of peace and banish wild beasts from the land , so that they may dwell securely in the wilderness and sleep in the woods .
- **Eze 37:26** (✓) *target: make*
  > Eze 37:26 I will make a covenant of peace with them. It shall be an everlasting covenant with them. And I will set them in their land and multiply them, and will set my sanctuary in their midst forevermore .
- **Hos 2:18** (✓) *target: make*
  > Hos 2:18 And I will make for them a covenant on that day with the beasts of the field , the birds of the heavens , and the creeping things of the ground . And I will abolish the bow , the sword , and war from the land , and I will make you lie down in safety .
- **Hos 10:4** (✓) *target: make*
  > Hos 10:4 They utter mere words ; with empty oaths they make covenants ; so judgment springs up like poisonous weeds in the furrows of the field .
- **Hos 12:1** (✓) *target: make*
  > Hos 12:1 Ephraim feeds on the wind and pursues the east wind all day long; they multiply falsehood and violence ; they make a covenant with Assyria , and oil is carried to Egypt .
- **Hag 2:5** (✓) *target: made*
  > Hag 2:5 according to the covenant that I made with you when you came out of Egypt . My Spirit remains in your midst . Fear not .
- **Zec 11:10** (✓) *target: made*
  > Zec 11:10 And I took my staff Favor , and I broke it, annulling the covenant that I had made with all the peoples .

**Group `3304-002`** (1 verse — anchors: 2Ki 23:3)

- **2Ki 23:3** 🔵 (✓) *target: made*
  > 2Ki 23:3 And the king stood by the pillar and made a covenant before the Lord , to walk after the Lord and to keep his commandments and his testimonies and his statutes with all his heart and all his soul , to perform the words of this covenant that were written in this book . And all the people joined in the covenant .
  - notes: Anchor: 2Ki 23:3 — all-heart covenant renewal; primary here for inner-being emphasis

**Group `3304-003`** (8 verses — anchors: Isa 28:15)

- **Isa 28:15** 🔵 (✓) *target: made*
  > Isa 28:15 Because you have said , “We have made a covenant with death , and with Sheol we have an agreement , when the overwhelming whip passes through it will not come to us, for we have made lies our refuge , and in falsehood we have taken shelter ”;
- **Exo 23:32** (✓) *target: make*
  > Exo 23:32 You shall make no covenant with them and their gods .
- **Exo 34:12** (✓) *target: make*
  > Exo 34:12 Take care , lest you make a covenant with the inhabitants of the land to which you go , lest it become a snare in your midst .
- **Exo 34:15** (✓) *target: make*
  > Exo 34:15 lest you make a covenant with the inhabitants of the land , and when they whore after their gods and sacrifice to their gods and you are invited , you eat of his sacrifice ,
- **Deu 7:2** (✓) *target: make*
  > Deu 7:2 and when the Lord your God gives them over to you, and you defeat them, then you must devote them to complete destruction . You shall make no covenant with them and show no mercy to them .
- **Judg 2:2** (✓) *target: make*
  > Judg 2:2 and you shall make no covenant with the inhabitants of this land ; you shall break down their altars .’ But you have not obeyed my voice . What is this you have done ?
- **Hos 10:4** (✓) *target: make*
  > Hos 10:4 They utter mere words ; with empty oaths they make covenants ; so judgment springs up like poisonous weeds in the furrows of the field .
- **Hos 12:1** (✓) *target: make*
  > Hos 12:1 Ephraim feeds on the wind and pursues the east wind all day long; they multiply falsehood and violence ; they make a covenant with Assyria , and oil is carried to Egypt .

**Group `3304-004`** (9 verses — anchors: 1Sa 18:3)

- **1Sa 18:3** 🔵 (✓) *target: made*
  > 1Sa 18:3 Then Jonathan made a covenant with David , because he loved him as his own soul .
- **1Sa 20:16** (✓) *target: covenant*
  > 1Sa 20:16 And Jonathan made a covenant with the house of David , saying, “May the Lord take vengeance on David’s enemies .”
- **1Sa 22:8** (✓) *target: covenant*
  > 1Sa 22:8 that all of you have conspired against me? No one discloses to me when my son makes a covenant with the son of Jesse . None of you is sorry for me or discloses to me that my son has stirred up my servant against me, to lie in wait , as at this day .”
- **1Sa 23:18** (✓) *target: made*
  > 1Sa 23:18 And the two of them made a covenant before the Lord . David remained at Horesh , and Jonathan went home .
- **2Sa 5:3** (✓) *target: made*
  > 2Sa 5:3 So all the elders of Israel came to the king at Hebron , and King David made a covenant with them at Hebron before the Lord , and they anointed David king over Israel .
- **1Ki 5:12** (✓) *target: made*
  > 1Ki 5:12 And the Lord gave Solomon wisdom , as he promised him. And there was peace between Hiram and Solomon , and the two of them made a treaty .
- **2Ki 11:4** (✓) *target: made*
  > 2Ki 11:4 But in the seventh year Jehoiada sent and brought the captains of the Carites and of the guards , and had them come to him in the house of the Lord . And he made a covenant with them and put them under oath in the house of the Lord , and he showed them the king’s son .
- **Job 31:1** (✓) *target: made*
  > Job 31:1 “I have made a covenant with my eyes ; how then could I gaze at a virgin ?
- **Psa 83:5** (✓) *target: make*
  > Psa 83:5 For they conspire with one accord ; against you they make a covenant —

**Group `UNCLASSIFIED`** (10 verses)

- **1Sa 11:1** (—) *target: Make*
  > 1Sa 11:1 Then Nahash the Ammonite went up and besieged Jabesh - gilead , and all the men of Jabesh said to Nahash , “ Make a treaty with us, and we will serve you .”
- **1Sa 11:2** (—) *target: make*
  > 1Sa 11:2 But Nahash the Ammonite said to them, “ On this condition I will make a treaty with you, that I gouge out all your right eyes , and thus bring disgrace on all Israel .”
- **2Sa 3:12** (—) *target: Make*
  > 2Sa 3:12 And Abner sent messengers to David on his behalf, saying , “ To whom does the land belong? Make your covenant with me, and behold , my hand shall be with you to bring over all Israel to you.”
- **2Sa 3:13** (—) *target: make*
  > 2Sa 3:13 And he said , “ Good ; I will make a covenant with you. But one thing I require of you; that is , you shall not see my face unless you first bring Michal , Saul’s daughter , when you come to see my face .”
- **2Sa 3:21** (—) *target: make*
  > 2Sa 3:21 And Abner said to David , “I will arise and go and will gather all Israel to my lord the king , that they may make a covenant with you, and that you may reign over all that your heart desires .” So David sent Abner away, and he went in peace .
- **1Ki 8:9** (—) *target: made*
  > 1Ki 8:9 There was nothing in the ark except the two tablets of stone that Moses put there at Horeb , where the Lord made a covenant with the people of Israel , when they came out of the land of Egypt .
- **1Ki 8:21** (—) *target: made*
  > 1Ki 8:21 And there I have provided a place for the ark , in which is the covenant of the Lord that he made with our fathers , when he brought them out of the land of Egypt .”
- **1Ki 20:34** (—) *target: made*
  > 1Ki 20:34 And Ben-hadad said to him, “The cities that my father took from your father I will restore , and you may establish bazaars for yourself in Damascus , as my father did in Samaria .” And Ahab said, “I will let you go on these terms .” So he made a covenant with him and let him go .
- **Job 41:4** (—) *target: make*
  > Job 41:4 Will he make a covenant with you to take him for your servant forever ?
- **Jer 11:10** (—) *target: made*
  > Jer 11:10 They have turned back to the iniquities of their forefathers , who refused to hear my words . They have gone after other gods to serve them. The house of Israel and the house of Judah have broken my covenant that I made with their fathers .

### `H3772J` — 9/10 classified · 1 anchor verse(s)

**Group `3303-001`** (9 verses — anchors: Jer 33:17)

- **Jer 33:17** 🔵 (✓) *target: lack*
  > Jer 33:17 “ For thus says the Lord : David shall never lack a man to sit on the throne of the house of Israel ,
- **2Sa 3:29** (✓) *target: without*
  > 2Sa 3:29 May it fall upon the head of Joab and upon all his father’s house , and may the house of Joab never be without one who has a discharge or who is leprous or who holds a spindle or who falls by the sword or who lacks bread !”
- **1Ki 2:4** (✓) *target: lack*
  > 1Ki 2:4 that the Lord may establish his word that he spoke concerning me, saying , ‘ If your sons pay close attention to their way , to walk before me in faithfulness with all their heart and with all their soul , you shall not lack a man on the throne of Israel .’
- **1Ki 8:25** (✓) *target: lack*
  > 1Ki 8:25 Now therefore, O Lord , God of Israel , keep for your servant David my father what you have promised him, saying , ‘You shall not lack a man to sit before me on the throne of Israel , if only your sons pay close attention to their way , to walk before me as you have walked before me.’
- **1Ki 9:5** (✓) *target: lack*
  > 1Ki 9:5 then I will establish your royal throne over Israel forever , as I promised David your father , saying , ‘You shall not lack a man on the throne of Israel .’
- **2Ch 6:16** (✓) *target: lack*
  > 2Ch 6:16 Now therefore, O Lord , God of Israel , keep for your servant David my father what you have promised him, saying , ‘You shall not lack a man to sit before me on the throne of Israel , if only your sons pay close attention to their way , to walk in my law as you have walked before me.’
- **2Ch 7:18** (✓) *target: covenanted*
  > 2Ch 7:18 then I will establish your royal throne , as I covenanted with David your father , saying , ‘You shall not lack a man to rule Israel .’
- **Jer 33:18** (✓) *target: lack*
  > Jer 33:18 and the Levitical priests shall never lack a man in my presence to offer burnt offerings , to burn grain offerings , and to make sacrifices forever .”
- **Jer 35:19** (✓) *target: lack*
  > Jer 35:19 therefore thus says the Lord of hosts , the God of Israel : Jonadab the son of Rechab shall never lack a man to stand before me.”

**Group `UNCLASSIFIED`** (1 verse)

- **1Ki 18:5** (—) *target: lose*
  > 1Ki 18:5 And Ahab said to Obadiah , “ Go through the land to all the springs of water and to all the valleys . Perhaps we may find grass and save the horses and mules alive, and not lose some of the animals .”

### `H7620I` — 6/6 classified · 2 anchor verse(s)

**Group `3314-001`** (4 verses — anchors: Dan 9:24)

- **Dan 9:24** 🔵 (✓) *target: weeks*
  > Dan 9:24 “ Seventy weeks are decreed about your people and your holy city , to finish the transgression , to put an end to sin , and to atone for iniquity , to bring in everlasting righteousness , to seal both vision and prophet , and to anoint a most holy place .
- **Dan 9:25** (✓) *target: weeks*
  > Dan 9:25 Know therefore and understand that from the going out of the word to restore and build Jerusalem to the coming of an anointed one , a prince , there shall be seven weeks . And for sixty-two weeks it shall be built again with squares and moat , but in a troubled time .
- **Dan 9:26** (✓) *target: weeks*
  > Dan 9:26 And after the sixty-two weeks , an anointed one shall be cut off and shall have nothing . And the people of the prince who is to come shall destroy the city and the sanctuary . Its end shall come with a flood , and to the end there shall be war . Desolations are decreed .
- **Dan 9:27** (✓) *target: week*
  > Dan 9:27 And he shall make a strong covenant with many for one week , and for half of the week he shall put an end to sacrifice and offering . And on the wing of abominations shall come one who makes desolate , until the decreed end is poured out on the desolator .”

**Group `3314-002`** (2 verses — anchors: Dan 10:2)

- **Dan 10:2** 🔵 (✓) *target: weeks*
  > Dan 10:2 In those days I , Daniel , was mourning for three weeks .
- **Dan 10:3** (✓) *target: weeks*
  > Dan 10:3 I ate no delicacies , no meat or wine entered my mouth , nor did I anoint myself at all , for the full three weeks .

### `H7650` — 131/176 classified · 4 anchor verse(s)

**Group `3308-001`** (30 verses — anchors: Deu 7:8)

- **Deu 7:8** 🔵 (✓) *target: swore*
  > Deu 7:8 but it is because the Lord loves you and is keeping the oath that he swore to your fathers , that the Lord has brought you out with a mighty hand and redeemed you from the house of slavery , from the hand of Pharaoh king of Egypt .
- **Gen 22:16** (✓) *target: sworn*
  > Gen 22:16 and said , “ By myself I have sworn , declares the Lord , because you have done this and have not withheld your son , your only son,
- **Gen 26:3** (✓) *target: swore*
  > Gen 26:3 Sojourn in this land , and I will be with you and will bless you, for to you and to your offspring I will give all these lands , and I will establish the oath that I swore to Abraham your father .
- **Gen 50:24** (✓) *target: swore*
  > Gen 50:24 And Joseph said to his brothers , “ I am about to die , but God will visit you and bring you up out of this land to the land that he swore to Abraham , to Isaac , and to Jacob .”
- **Exo 13:5** (✓) *target: swore*
  > Exo 13:5 And when the Lord brings you into the land of the Canaanites , the Hittites , the Amorites , the Hivites , and the Jebusites , which he swore to your fathers to give you, a land flowing with milk and honey , you shall keep this service in this month .
- **Exo 13:11** (✓) *target: swore*
  > Exo 13:11 “When the Lord brings you into the land of the Canaanites , as he swore to you and your fathers , and shall give it to you ,
- **Exo 32:13** (✓) *target: swore*
  > Exo 32:13 Remember Abraham , Isaac , and Israel , your servants , to whom you swore by your own self, and said to them, ‘I will multiply your offspring as the stars of heaven , and all this land that I have promised I will give to your offspring , and they shall inherit it forever .’”
- **Exo 33:1** (✓) *target: swore*
  > Exo 33:1 The Lord said to Moses , “ Depart ; go up from here , you and the people whom you have brought up out of the land of Egypt , to the land of which I swore to Abraham , Isaac , and Jacob , saying , ‘ To your offspring I will give it .’
- **Num 11:12** (✓) *target: swore*
  > Num 11:12 Did I conceive all this people ? Did I give them birth , that you should say to me, ‘ Carry them in your bosom , as a nurse carries a nursing child ,’ to the land that you swore to give their fathers ?
- **Num 14:16** (✓) *target: swore*
  > Num 14:16 ‘It is because the Lord was not able to bring this people into the land that he swore to give to them that he has killed them in the wilderness .’
- **Num 14:23** (✓) *target: swore*
  > Num 14:23 shall see the land that I swore to give to their fathers . And none of those who despised me shall see it .
- **Num 32:10** (✓) *target: swore*
  > Num 32:10 And the Lord’s anger was kindled on that day , and he swore , saying ,
- **Num 32:11** (✓) *target: swore*
  > Num 32:11 ‘ Surely none of the men who came up out of Egypt , from twenty years old and upward , shall see the land that I swore to give to Abraham , to Isaac , and to Jacob , because they have not wholly followed me ,
- **Psa 89:3** (✓) *target: sworn*
  > Psa 89:3 You have said, “I have made a covenant with my chosen one ; I have sworn to David my servant :
- **Psa 89:35** (✓) *target: sworn*
  > Psa 89:35 Once for all I have sworn by my holiness ; I will not lie to David .
- **Psa 89:49** (✓) *target: swore*
  > Psa 89:49 Lord , where is your steadfast love of old , which by your faithfulness you swore to David ?
- **Psa 95:11** (✓) *target: swore*
  > Psa 95:11 Therefore I swore in my wrath , “They shall not enter my rest .”
- **Psa 110:4** (✓) *target: sworn*
  > Psa 110:4 The Lord has sworn and will not change his mind , “ You are a priest forever after the order of Melchizedek .”
- **Psa 132:2** (✓) *target: swore*
  > Psa 132:2 how he swore to the Lord and vowed to the Mighty One of Jacob ,
- **Psa 132:11** (✓) *target: swore*
  > Psa 132:11 The Lord swore to David a sure oath from which he will not turn back : “One of the sons of your body I will set on your throne .
- **Isa 45:23** (✓) *target: sworn*
  > Isa 45:23 By myself I have sworn ; from my mouth has gone out in righteousness a word that shall not return : ‘ To me every knee shall bow , every tongue shall swear allegiance.’
- **Isa 54:9** (✓) *target: swore*
  > Isa 54:9 “ This is like the days of Noah to me: as I swore that the waters of Noah should no more go over the earth , so I have sworn that I will not be angry with you, and will not rebuke you .
- **Isa 62:8** (✓) *target: sworn*
  > Isa 62:8 The Lord has sworn by his right hand and by his mighty arm : “I will not again give your grain to be food for your enemies , and foreigners shall not drink your wine for which you have labored ;
- **Jer 11:5** (✓) *target: swore*
  > Jer 11:5 that I may confirm the oath that I swore to your fathers , to give them a land flowing with milk and honey , as at this day .” Then I answered , “So be it , Lord .”
- **Jer 32:22** (✓) *target: swore*
  > Jer 32:22 And you gave them this land , which you swore to their fathers to give them, a land flowing with milk and honey .
- **Dan 12:7** (✓) *target: swore*
  > Dan 12:7 And I heard the man clothed in linen , who was above the waters of the stream ; he raised his right hand and his left hand toward heaven and swore by him who lives forever that it would be for a time, times , and half a time, and that when the shattering of the power of the holy people comes to an end all these things would be finished .
- **Amo 4:2** (✓) *target: sworn*
  > Amo 4:2 The Lord God has sworn by his holiness that , behold , the days are coming upon you, when they shall take you away with hooks , even the last of you with fishhooks .
- **Amo 6:8** (✓) *target: sworn*
  > Amo 6:8 The Lord God has sworn by himself , declares the Lord , the God of hosts : “I abhor the pride of Jacob and hate his strongholds , and I will deliver up the city and all that is in it.”
- **Amo 8:7** (✓) *target: sworn*
  > Amo 8:7 The Lord has sworn by the pride of Jacob : “Surely I will never forget any of their deeds .
- **Mic 7:20** (✓) *target: sworn*
  > Mic 7:20 You will show faithfulness to Jacob and steadfast love to Abraham , as you have sworn to our fathers from the days of old .

**Group `3308-002`** (79 verses — anchors: Psa 15:4)

- **Psa 15:4** 🔵 (✓) *target: swears*
  > Psa 15:4 in whose eyes a vile person is despised , but who honors those who fear the Lord ; who swears to his own hurt and does not change ;
- **Gen 21:23** (✓) *target: swear*
  > Gen 21:23 Now therefore swear to me here by God that you will not deal falsely with me or with my descendants or with my posterity , but as I have dealt kindly with you, so you will deal with me and with the land where you have sojourned .”
- **Gen 21:24** (✓) *target: swear*
  > Gen 21:24 And Abraham said , “ I will swear .”
- **Gen 21:31** (✓) *target: swore an oath*
  > Gen 21:31 Therefore that place was called Beersheba , because there both of them swore an oath .
- **Gen 24:3** (✓) *target: swear*
  > Gen 24:3 that I may make you swear by the Lord , the God of heaven and God of the earth , that you will not take a wife for my son from the daughters of the Canaanites , among whom I dwell ,
- **Gen 24:7** (✓) *target: swore*
  > Gen 24:7 The Lord , the God of heaven , who took me from my father’s house and from the land of my kindred , and who spoke to me and swore to me, ‘ To your offspring I will give this land ,’ he will send his angel before you , and you shall take a wife for my son from there .
- **Gen 24:9** (✓) *target: swore*
  > Gen 24:9 So the servant put his hand under the thigh of Abraham his master and swore to him concerning this matter .
- **Gen 24:37** (✓) *target: swear*
  > Gen 24:37 My master made me swear , saying , ‘You shall not take a wife for my son from the daughters of the Canaanites , in whose land I dwell ,
- **Gen 25:33** (✓) *target: Swear*
  > Gen 25:33 Jacob said , “ Swear to me now .” So he swore to him and sold his birthright to Jacob .
- **Gen 26:31** (✓) *target: oaths*
  > Gen 26:31 In the morning they rose early and exchanged oaths . And Isaac sent them on their way, and they departed from him in peace .
- **Gen 31:53** (✓) *target: swore*
  > Gen 31:53 The God of Abraham and the God of Nahor , the God of their father , judge between us .” So Jacob swore by the Fear of his father Isaac ,
- **Gen 47:31** (✓) *target: Swear*
  > Gen 47:31 And he said , “ Swear to me”; and he swore to him. Then Israel bowed himself upon the head of his bed .
- **Gen 50:5** (✓) *target: swear*
  > Gen 50:5 ‘My father made me swear , saying , “I am about to die : in my tomb that I hewed out for myself in the land of Canaan , there shall you bury me .” Now therefore, let me please go up and bury my father . Then I will return .’”
- **Gen 50:6** (✓) *target: swear*
  > Gen 50:6 And Pharaoh answered , “Go up , and bury your father , as he made you swear .”
- **Gen 50:25** (✓) *target: swear*
  > Gen 50:25 Then Joseph made the sons of Israel swear , saying , “ God will surely visit you, and you shall carry up my bones from here .”
- **Lev 5:4** (✓) *target: oath*
  > Lev 5:4 or if anyone utters with his lips a rash oath to do evil or to do good , any sort of rash oath that people swear , and it is hidden from him , when he comes to know it, and he realizes his guilt in any of these ;
- **Lev 6:3** (✓) *target: swearing*
  > Lev 6:3 or has found something lost and lied about it, swearing falsely —in any of all the things that people do and sin thereby —
- **Lev 6:5** (✓) *target: sworn*
  > Lev 6:5 or anything about which he has sworn falsely , he shall restore it in full and shall add a fifth to it , and give it to him to whom it belongs on the day he realizes his guilt .
- **Lev 19:12** (✓) *target: swear*
  > Lev 19:12 You shall not swear by my name falsely , and so profane the name of your God : I am the Lord .
- **Num 5:19** (✓) *target: oath*
  > Num 5:19 Then the priest shall make her take an oath , saying , ‘ If no man has lain with you, and if you have not turned aside to uncleanness while you were under your husband’s authority, be free from this water of bitterness that brings the curse .
- **Num 5:21** (✓) *target: take*
  > Num 5:21 then’ (let the priest make the woman take the oath of the curse , and say to the woman ) ‘the Lord make you a curse and an oath among your people , when the Lord makes your thigh fall away and your body swell .
- **Num 30:2** (✓) *target: swears*
  > Num 30:2 If a man vows a vow to the Lord , or swears an oath to bind himself by a pledge , he shall not break his word . He shall do according to all that proceeds out of his mouth .
- **Jos 2:12** (✓) *target: swear*
  > Jos 2:12 Now then, please swear to me by the Lord that, as I have dealt kindly with you, you also will deal kindly with my father’s house , and give me a sure sign
- **Jos 2:17** (✓) *target: swear*
  > Jos 2:17 The men said to her, “We will be guiltless with respect to this oath of yours that you have made us swear .
- **Jos 2:20** (✓) *target: swear*
  > Jos 2:20 But if you tell this business of ours, then we shall be guiltless with respect to your oath that you have made us swear .”
- **Jos 6:22** (✓) *target: swore*
  > Jos 6:22 But to the two men who had spied out the land , Joshua said , “ Go into the prostitute’s house and bring out from there the woman and all who belong to her, as you swore to her .”
- **Jos 6:26** (✓) *target: oath*
  > Jos 6:26 Joshua laid an oath on them at that time , saying , “ Cursed before the Lord be the man who rises up and rebuilds this city , Jericho . “At the cost of his firstborn shall he lay its foundation , and at the cost of his youngest son shall he set up its gates .”
- **Jos 9:15** (✓) *target: swore*
  > Jos 9:15 And Joshua made peace with them and made a covenant with them, to let them live , and the leaders of the congregation swore to them.
- **Jos 9:18** (✓) *target: sworn*
  > Jos 9:18 But the people of Israel did not attack them, because the leaders of the congregation had sworn to them by the Lord , the God of Israel . Then all the congregation murmured against the leaders .
- **Jos 9:19** (✓) *target: sworn*
  > Jos 9:19 But all the leaders said to all the congregation , “ We have sworn to them by the Lord , the God of Israel , and now we may not touch them .
- **Jos 9:20** (✓) *target: swore*
  > Jos 9:20 This we will do to them: let them live , lest wrath be upon us, because of the oath that we swore to them .”
- **Jos 14:9** (✓) *target: swore*
  > Jos 14:9 And Moses swore on that day , saying , ‘ Surely the land on which your foot has trodden shall be an inheritance for you and your children forever , because you have wholly followed the Lord my God .’
- **Jos 23:7** (✓) *target: swear*
  > Jos 23:7 that you may not mix with these nations remaining among you or make mention of the names of their gods or swear by them or serve them or bow down to them ,
- **Judg 15:12** (✓) *target: Swear*
  > Judg 15:12 And they said to him, “We have come down to bind you, that we may give you into the hands of the Philistines .” And Samson said to them, “ Swear to me that you will not attack me yourselves .”
- **Judg 21:1** (✓) *target: sworn*
  > Judg 21:1 Now the men of Israel had sworn at Mizpah , “ No one of us shall give his daughter in marriage to Benjamin .”
- **Judg 21:7** (✓) *target: sworn*
  > Judg 21:7 What shall we do for wives for those who are left , since we have sworn by the Lord that we will not give them any of our daughters for wives ?”
- **Judg 21:18** (✓) *target: sworn*
  > Judg 21:18 Yet we cannot give them wives from our daughters .” For the people of Israel had sworn , “ Cursed be he who gives a wife to Benjamin .”
- **1Sa 3:14** (✓) *target: swear*
  > 1Sa 3:14 Therefore I swear to the house of Eli that the iniquity of Eli’s house shall not be atoned for by sacrifice or offering forever .”
- **1Sa 14:27** (✓) *target: oath*
  > 1Sa 14:27 But Jonathan had not heard his father charge the people with the oath , so he put out the tip of the staff that was in his hand and dipped it in the honeycomb and put his hand to his mouth , and his eyes became bright .
- **1Sa 14:28** (✓) *target: strictly*
  > 1Sa 14:28 Then one of the people said , “Your father strictly charged the people with an oath , saying , ‘ Cursed be the man who eats food this day .’” And the people were faint .
- **1Sa 19:6** (✓) *target: swore*
  > 1Sa 19:6 And Saul listened to the voice of Jonathan . Saul swore , “As the Lord lives , he shall not be put to death .”
- **1Sa 20:3** (✓) *target: vowed*
  > 1Sa 20:3 But David vowed again , saying , “Your father knows well that I have found favor in your eyes , and he thinks , ‘Do not let Jonathan know this , lest he be grieved .’ But truly , as the Lord lives and as your soul lives , there is but a step between me and death .”
- **1Sa 20:17** (✓) *target: swear*
  > 1Sa 20:17 And Jonathan made David swear again by his love for him, for he loved him as he loved his own soul .
- **1Sa 20:42** (✓) *target: sworn*
  > 1Sa 20:42 Then Jonathan said to David , “ Go in peace , because we have sworn both of us in the name of the Lord , saying , ‘The Lord shall be between me and you, and between my offspring and your offspring , forever .’” And he rose and departed , and Jonathan went into the city .
- **1Sa 24:21** (✓) *target: Swear*
  > 1Sa 24:21 Swear to me therefore by the Lord that you will not cut off my offspring after me, and that you will not destroy my name out of my father’s house .”
- **1Sa 24:22** (✓) *target: swore*
  > 1Sa 24:22 And David swore this to Saul . Then Saul went home , but David and his men went up to the stronghold .
- **1Sa 28:10** (✓) *target: swore*
  > 1Sa 28:10 But Saul swore to her by the Lord , “As the Lord lives , no punishment shall come upon you for this thing .”
- **1Sa 30:15** (✓) *target: Swear*
  > 1Sa 30:15 And David said to him, “Will you take me down to this band ?” And he said , “ Swear to me by God that you will not kill me or deliver me into the hands of my master , and I will take you down to this band .”
- **2Sa 3:9** (✓) *target: sworn*
  > 2Sa 3:9 God do so to Abner and more also , if I do not accomplish for David what the Lord has sworn to him ,
- **2Sa 3:35** (✓) *target: swore*
  > 2Sa 3:35 Then all the people came to persuade David to eat bread while it was yet day . But David swore , saying , “ God do so to me and more also , if I taste bread or anything else till the sun goes down !”
- **2Sa 19:7** (✓) *target: swear*
  > 2Sa 19:7 Now therefore arise , go out and speak kindly to your servants , for I swear by the Lord , if you do not go , not a man will stay with you this night , and this will be worse for you than all the evil that has come upon you from your youth until now .”
- **2Sa 19:23** (✓) *target: oath*
  > 2Sa 19:23 And the king said to Shimei , “You shall not die .” And the king gave him his oath .
- **2Sa 21:2** (✓) *target: sworn*
  > 2Sa 21:2 So the king called the Gibeonites and spoke to them. Now the Gibeonites were not of the people of Israel but of the remnant of the Amorites . Although the people of Israel had sworn to spare them, Saul had sought to strike them down in his zeal for the people of Israel and Judah .
- **2Sa 21:17** (✓) *target: swore*
  > 2Sa 21:17 But Abishai the son of Zeruiah came to his aid and attacked the Philistine and killed him. Then David’s men swore to him, “You shall no longer go out with us to battle , lest you quench the lamp of Israel .”
- **1Ki 1:13** (✓) *target: swear*
  > 1Ki 1:13 Go in at once to King David , and say to him, ‘Did you not , my lord the king , swear to your servant , saying , “ Solomon your son shall reign after me, and he shall sit on my throne ”? Why then is Adonijah king ?’
- **1Ki 1:17** (✓) *target: swore*
  > 1Ki 1:17 She said to him, “My lord , you swore to your servant by the Lord your God , saying, ‘ Solomon your son shall reign after me, and he shall sit on my throne .’
- **1Ki 1:29** (✓) *target: king*
  > 1Ki 1:29 And the king swore, saying , “As the Lord lives , who has redeemed my soul out of every adversity ,
- **1Ki 1:30** (✓) *target: swore*
  > 1Ki 1:30 as I swore to you by the Lord , the God of Israel , saying , ‘ Solomon your son shall reign after me, and he shall sit on my throne in my place ,’ even so will I do this day .”
- **1Ki 1:51** (✓) *target: swear*
  > 1Ki 1:51 Then it was told Solomon , “ Behold , Adonijah fears King Solomon , for behold , he has laid hold of the horns of the altar , saying , ‘Let King Solomon swear to me first that he will not put his servant to death with the sword .’”
- **1Ki 2:8** (✓) *target: swore*
  > 1Ki 2:8 And there is also with you Shimei the son of Gera , the Benjaminite from Bahurim , who cursed me with a grievous curse on the day when I went to Mahanaim . But when he came down to meet me at the Jordan , I swore to him by the Lord , saying , ‘I will not put you to death with the sword .’
- **1Ki 2:23** (✓) *target: swore*
  > 1Ki 2:23 Then King Solomon swore by the Lord , saying , “ God do so to me and more also if this word does not cost Adonijah his life !
- **1Ki 2:42** (✓) *target: swear*
  > 1Ki 2:42 the king sent and summoned Shimei and said to him, “Did I not make you swear by the Lord and solemnly warn you, saying , ‘ Know for certain that on the day you go out and go to any place whatever , you shall die ’? And you said to me, ‘What you say is good ; I will obey .’
- **1Ki 18:10** (✓) *target: oath*
  > 1Ki 18:10 As the Lord your God lives , there is no nation or kingdom where my lord has not sent to seek you. And when they would say , ‘He is not here ,’ he would take an oath of the kingdom or nation , that they had not found you.
- **1Ki 22:16** (✓) *target: swear*
  > 1Ki 22:16 But the king said to him, “How many times shall I make you swear that you speak to me nothing but the truth in the name of the Lord ?”
- **2Ki 11:4** (✓) *target: oath*
  > 2Ki 11:4 But in the seventh year Jehoiada sent and brought the captains of the Carites and of the guards , and had them come to him in the house of the Lord . And he made a covenant with them and put them under oath in the house of the Lord , and he showed them the king’s son .
- **2Ki 25:24** (✓) *target: swore*
  > 2Ki 25:24 And Gedaliah swore to them and their men , saying , “Do not be afraid because of the Chaldean officials . Live in the land and serve the king of Babylon , and it shall be well with you .”
- **2Ch 15:14** (✓) *target: oath*
  > 2Ch 15:14 They swore an oath to the Lord with a loud voice and with shouting and with trumpets and with horns .
- **2Ch 15:15** (✓) *target: sworn*
  > 2Ch 15:15 And all Judah rejoiced over the oath , for they had sworn with all their heart and had sought him with their whole desire , and he was found by them, and the Lord gave them rest all around .
- **2Ch 18:15** (✓) *target: swear*
  > 2Ch 18:15 But the king said to him, “ How many times shall I make you swear that you speak to me nothing but the truth in the name of the Lord ?”
- **2Ch 36:13** (✓) *target: made him swear*
  > 2Ch 36:13 He also rebelled against King Nebuchadnezzar , who had made him swear by God . He stiffened his neck and hardened his heart against turning to the Lord , the God of Israel .
- **Ezr 10:5** (✓) *target: oath*
  > Ezr 10:5 Then Ezra arose and made the leading priests and Levites and all Israel take an oath that they would do as had been said . So they took the oath .
- **Neh 5:12** (✓) *target: made them swear*
  > Neh 5:12 Then they said , “We will restore these and require nothing from them. We will do as you say .” And I called the priests and made them swear to do as they had promised .
- **Neh 13:25** (✓) *target: oath*
  > Neh 13:25 And I confronted them and cursed them and beat some of them and pulled out their hair . And I made them take an oath in the name of God , saying, “You shall not give your daughters to their sons , or take their daughters for your sons or for yourselves .
- **Psa 24:4** (✓) *target: swear*
  > Psa 24:4 He who has clean hands and a pure heart , who does not lift up his soul to what is false and does not swear deceitfully .
- **Psa 63:11** (✓) *target: swear*
  > Psa 63:11 But the king shall rejoice in God ; all who swear by him shall exult , for the mouths of liars will be stopped .
- **Psa 119:106** (✓) *target: oath*
  > Psa 119:106 I have sworn an oath and confirmed it, to keep your righteous rules .
- **Ecc 9:2** (✓) *target: swears*
  > Ecc 9:2 It is the same for all , since the same event happens to the righteous and the wicked , to the good and the evil , to the clean and the unclean , to him who sacrifices and him who does not sacrifice . As the good one is, so is the sinner , and he who swears is as he who shuns an oath .
- **Eze 16:8** (✓) *target: vow*
  > Eze 16:8 “When I passed by you again and saw you, behold , you were at the age for love , and I spread the corner of my garment over you and covered your nakedness ; I made my vow to you and entered into a covenant with you, declares the Lord God , and you became mine .
- **Eze 21:23** (✓) *target: sworn*
  > Eze 21:23 But to them it will seem like a false divination . They have sworn solemn oaths , but he brings their guilt to remembrance , that they may be taken .

**Group `3308-003`** (17 verses — anchors: Jer 4:2)

- **Jer 4:2** 🔵 (✓) *target: swear*
  > Jer 4:2 and if you swear , ‘As the Lord lives ,’ in truth , in justice , and in righteousness , then nations shall bless themselves in him, and in him shall they glory .”
- **Deu 6:13** (✓) *target: swear*
  > Deu 6:13 It is the Lord your God you shall fear . Him you shall serve and by his name you shall swear .
- **Deu 10:20** (✓) *target: swear*
  > Deu 10:20 You shall fear the Lord your God . You shall serve him and hold fast to him, and by his name you shall swear .
- **Isa 19:18** (✓) *target: swear allegiance*
  > Isa 19:18 In that day there will be five cities in the land of Egypt that speak the language of Canaan and swear allegiance to the Lord of hosts . One of these will be called the City of Destruction .
- **Isa 45:23** (✓) *target: sworn*
  > Isa 45:23 By myself I have sworn ; from my mouth has gone out in righteousness a word that shall not return : ‘ To me every knee shall bow , every tongue shall swear allegiance.’
- **Isa 48:1** (✓) *target: swear*
  > Isa 48:1 Hear this , O house of Jacob , who are called by the name of Israel , and who came from the waters of Judah , who swear by the name of the Lord and confess the God of Israel , but not in truth or right .
- **Isa 65:16** (✓) *target: oath*
  > Isa 65:16 so that he who blesses himself in the land shall bless himself by the God of truth , and he who takes an oath in the land shall swear by the God of truth ; because the former troubles are forgotten and are hidden from my eyes .
- **Jer 5:2** (✓) *target: swear*
  > Jer 5:2 Though they say , “As the Lord lives ,” yet they swear falsely .
- **Jer 5:7** (✓) *target: sworn*
  > Jer 5:7 “ How can I pardon you ? Your children have forsaken me and have sworn by those who are no gods . When I fed them to the full , they committed adultery and trooped to the houses of whores .
- **Jer 7:9** (✓) *target: swear*
  > Jer 7:9 Will you steal , murder , commit adultery , swear falsely , make offerings to Baal , and go after other gods that you have not known ,
- **Jer 12:16** (✓) *target: swear*
  > Jer 12:16 And it shall come to pass, if they will diligently learn the ways of my people , to swear by my name , ‘As the Lord lives ,’ even as they taught my people to swear by Baal , then they shall be built up in the midst of my people .
- **Hos 4:15** (✓) *target: swear*
  > Hos 4:15 Though you play the whore , O Israel , let not Judah become guilty . Enter not into Gilgal , nor go up to Beth-aven , and swear not, “As the Lord lives .”
- **Amo 8:14** (✓) *target: swear*
  > Amo 8:14 Those who swear by the Guilt of Samaria , and say , ‘As your god lives , O Dan ,’ and, ‘As the Way of Beersheba lives ,’ they shall fall , and never rise again .”
- **Zep 1:5** (✓) *target: swear*
  > Zep 1:5 those who bow down on the roofs to the host of the heavens , those who bow down and swear to the Lord and yet swear by Milcom ,
- **Zec 5:3** (✓) *target: swears*
  > Zec 5:3 Then he said to me, “ This is the curse that goes out over the face of the whole land . For everyone who steals shall be cleaned out according to what is on one side , and everyone who swears falsely shall be cleaned out according to what is on the other side .
- **Zec 5:4** (✓) *target: who swears*
  > Zec 5:4 I will send it out , declares the Lord of hosts , and it shall enter the house of the thief , and the house of him who swears falsely by my name . And it shall remain in his house and consume it, both timber and stones .”
- **Mal 3:5** (✓) *target: swear*
  > Mal 3:5 “Then I will draw near to you for judgment . I will be a swift witness against the sorcerers , against the adulterers , against those who swear falsely , against those who oppress the hired worker in his wages , the widow and the fatherless , against those who thrust aside the sojourner , and do not fear me, says the Lord of hosts .

**Group `3308-004`** (5 verses — anchors: Song 5:8)

- **Song 5:8** 🔵 (✓) *target: adjure*
  > Song 5:8 I adjure you, O daughters of Jerusalem , if you find my beloved , that you tell him I am sick with love .
- **Song 2:7** (✓) *target: adjure*
  > Song 2:7 I adjure you, O daughters of Jerusalem , by the gazelles or the does of the field , that you not stir up or awaken love until it pleases .
- **Song 3:5** (✓) *target: adjure*
  > Song 3:5 I adjure you, O daughters of Jerusalem , by the gazelles or the does of the field , that you not stir up or awaken love until it pleases .
- **Song 5:9** (✓) *target: adjure*
  > Song 5:9 What is your beloved more than another beloved , O most beautiful among women ? What is your beloved more than another beloved , that you thus adjure us ?
- **Song 8:4** (✓) *target: adjure*
  > Song 8:4 I adjure you, O daughters of Jerusalem , that you not stir up or awaken love until it pleases .

**Group `UNCLASSIFIED`** (45 verses)

- **Exo 13:19** (—) *target: solemnly*
  > Exo 13:19 Moses took the bones of Joseph with him, for Joseph had made the sons of Israel solemnly swear , saying , “ God will surely visit you, and you shall carry up my bones with you from here .”
- **Deu 1:8** (—) *target: swore*
  > Deu 1:8 See , I have set the land before you. Go in and take possession of the land that the Lord swore to your fathers , to Abraham , to Isaac , and to Jacob , to give to them and to their offspring after them .’
- **Deu 1:34** (—) *target: swore*
  > Deu 1:34 “And the Lord heard your words and was angered , and he swore ,
- **Deu 1:35** (—) *target: swore*
  > Deu 1:35 ‘ Not one of these men of this evil generation shall see the good land that I swore to give to your fathers ,
- **Deu 2:14** (—) *target: sworn*
  > Deu 2:14 And the time from our leaving Kadesh-barnea until we crossed the brook Zered was thirty-eight years , until the entire generation , that is, the men of war , had perished from the camp , as the Lord had sworn to them .
- **Deu 4:21** (—) *target: swore*
  > Deu 4:21 Furthermore, the Lord was angry with me because of you , and he swore that I should not cross the Jordan , and that I should not enter the good land that the Lord your God is giving you for an inheritance .
- **Deu 4:31** (—) *target: swore*
  > Deu 4:31 For the Lord your God is a merciful God . He will not leave you or destroy you or forget the covenant with your fathers that he swore to them .
- **Deu 6:10** (—) *target: swore*
  > Deu 6:10 “And when the Lord your God brings you into the land that he swore to your fathers , to Abraham , to Isaac , and to Jacob , to give you—with great and good cities that you did not build ,
- **Deu 6:18** (—) *target: swore*
  > Deu 6:18 And you shall do what is right and good in the sight of the Lord , that it may go well with you, and that you may go in and take possession of the good land that the Lord swore to give to your fathers
- **Deu 6:23** (—) *target: swore*
  > Deu 6:23 And he brought us out from there , that he might bring us in and give us the land that he swore to give to our fathers .
- **Deu 7:12** (—) *target: swore*
  > Deu 7:12 “And because you listen to these rules and keep and do them, the Lord your God will keep with you the covenant and the steadfast love that he swore to your fathers .
- **Deu 7:13** (—) *target: swore*
  > Deu 7:13 He will love you, bless you, and multiply you. He will also bless the fruit of your womb and the fruit of your ground , your grain and your wine and your oil , the increase of your herds and the young of your flock , in the land that he swore to your fathers to give you .
- **Deu 8:1** (—) *target: swore*
  > Deu 8:1 “The whole commandment that I command you today you shall be careful to do , that you may live and multiply , and go in and possess the land that the Lord swore to give to your fathers .
- **Deu 8:18** (—) *target: swore*
  > Deu 8:18 You shall remember the Lord your God , for it is he who gives you power to get wealth , that he may confirm his covenant that he swore to your fathers , as it is this day .
- **Deu 9:5** (—) *target: swore*
  > Deu 9:5 Not because of your righteousness or the uprightness of your heart are you going in to possess their land , but because of the wickedness of these nations the Lord your God is driving them out from before you, and that he may confirm the word that the Lord swore to your fathers , to Abraham , to Isaac , and to Jacob .
- **Deu 10:11** (—) *target: swore*
  > Deu 10:11 And the Lord said to me, ‘ Arise , go on your journey at the head of the people , so that they may go in and possess the land , which I swore to their fathers to give them .’
- **Deu 11:9** (—) *target: swore*
  > Deu 11:9 and that you may live long in the land that the Lord swore to your fathers to give to them and to their offspring , a land flowing with milk and honey .
- **Deu 11:21** (—) *target: swore*
  > Deu 11:21 that your days and the days of your children may be multiplied in the land that the Lord swore to your fathers to give them, as long as the heavens are above the earth .
- **Deu 13:17** (—) *target: swore*
  > Deu 13:17 None of the devoted things shall stick to your hand , that the Lord may turn from the fierceness of his anger and show you mercy and have compassion on you and multiply you, as he swore to your fathers ,
- **Deu 19:8** (—) *target: sworn*
  > Deu 19:8 And if the Lord your God enlarges your territory , as he has sworn to your fathers , and gives you all the land that he promised to give to your fathers —
- **Deu 26:3** (—) *target: swore*
  > Deu 26:3 And you shall go to the priest who is in office at that time and say to him, ‘I declare today to the Lord your God that I have come into the land that the Lord swore to our fathers to give us .’
- **Deu 26:15** (—) *target: swore*
  > Deu 26:15 Look down from your holy habitation , from heaven , and bless your people Israel and the ground that you have given us, as you swore to our fathers , a land flowing with milk and honey .’
- **Deu 28:9** (—) *target: sworn*
  > Deu 28:9 The Lord will establish you as a people holy to himself, as he has sworn to you, if you keep the commandments of the Lord your God and walk in his ways .
- **Deu 28:11** (—) *target: swore*
  > Deu 28:11 And the Lord will make you abound in prosperity , in the fruit of your womb and in the fruit of your livestock and in the fruit of your ground , within the land that the Lord swore to your fathers to give you .
- **Deu 29:13** (—) *target: swore*
  > Deu 29:13 that he may establish you today as his people , and that he may be your God , as he promised you, and as he swore to your fathers , to Abraham , to Isaac , and to Jacob .
- **Deu 30:20** (—) *target: swore*
  > Deu 30:20 loving the Lord your God , obeying his voice and holding fast to him, for he is your life and length of days , that you may dwell in the land that the Lord swore to your fathers , to Abraham , to Isaac , and to Jacob , to give them .”
- **Deu 31:7** (—) *target: sworn*
  > Deu 31:7 Then Moses summoned Joshua and said to him in the sight of all Israel , “Be strong and courageous , for you shall go with this people into the land that the Lord has sworn to their fathers to give them , and you shall put them in possession of it .
- **Deu 31:20** (—) *target: swore*
  > Deu 31:20 For when I have brought them into the land flowing with milk and honey , which I swore to give to their fathers , and they have eaten and are full and grown fat , they will turn to other gods and serve them, and despise me and break my covenant .
- **Deu 31:21** (—) *target: swore*
  > Deu 31:21 And when many evils and troubles have come upon them, this song shall confront them as a witness ( for it will live unforgotten in the mouths of their offspring ). For I know what they are inclined to do even today , before I have brought them into the land that I swore to give.”
- **Deu 31:23** (—) *target: swore*
  > Deu 31:23 And the Lord commissioned Joshua the son of Nun and said , “Be strong and courageous , for you shall bring the people of Israel into the land that I swore to give them. I will be with you .”
- **Deu 34:4** (—) *target: swore*
  > Deu 34:4 And the Lord said to him, “ This is the land of which I swore to Abraham , to Isaac , and to Jacob , ‘I will give it to your offspring .’ I have let you see it with your eyes , but you shall not go over there .”
- **Jos 1:6** (—) *target: swore*
  > Jos 1:6 Be strong and courageous , for you shall cause this people to inherit the land that I swore to their fathers to give them .
- **Jos 5:6** (—) *target: swore*
  > Jos 5:6 For the people of Israel walked forty years in the wilderness , until all the nation , the men of war who came out of Egypt , perished , because they did not obey the voice of the Lord ; the Lord swore to them that he would not let them see the land that the Lord had sworn to their fathers to give to us, a land flowing with milk and honey .
- **Jos 21:43** (—) *target: swore*
  > Jos 21:43 Thus the Lord gave to Israel all the land that he swore to give to their fathers . And they took possession of it , and they settled there.
- **Jos 21:44** (—) *target: sworn*
  > Jos 21:44 And the Lord gave them rest on every side just as he had sworn to their fathers . Not one of all their enemies had withstood them, for the Lord had given all their enemies into their hands .
- **Judg 2:1** (—) *target: swore*
  > Judg 2:1 Now the angel of the Lord went up from Gilgal to Bochim . And he said , “I brought you up from Egypt and brought you into the land that I swore to give to your fathers . I said , ‘I will never break my covenant with you ,
- **Judg 2:15** (—) *target: sworn*
  > Judg 2:15 Whenever they marched out , the hand of the Lord was against them for harm , as the Lord had warned , and as the Lord had sworn to them. And they were in terrible distress .
- **Psa 102:8** (—) *target: curse*
  > Psa 102:8 All the day my enemies taunt me; those who deride me use my name for a curse .
- **Isa 14:24** (—) *target: sworn*
  > Isa 14:24 The Lord of hosts has sworn : “ As I have planned , so shall it be, and as I have purposed , so shall it stand ,
- **Jer 22:5** (—) *target: swear*
  > Jer 22:5 But if you will not obey these words , I swear by myself, declares the Lord , that this house shall become a desolation .
- **Jer 38:16** (—) *target: swore*
  > Jer 38:16 Then King Zedekiah swore secretly to Jeremiah , “As the Lord lives , who made our souls , I will not put you to death or deliver you into the hand of these men who seek your life .”
- **Jer 40:9** (—) *target: swore*
  > Jer 40:9 Gedaliah the son of Ahikam , son of Shaphan , swore to them and their men , saying , “Do not be afraid to serve the Chaldeans . Dwell in the land and serve the king of Babylon , and it shall be well with you .
- **Jer 44:26** (—) *target: sworn*
  > Jer 44:26 Therefore hear the word of the Lord , all you of Judah who dwell in the land of Egypt : Behold , I have sworn by my great name , says the Lord , that my name shall no more be invoked by the mouth of any man of Judah in all the land of Egypt , saying , ‘As the Lord God lives .’
- **Jer 49:13** (—) *target: sworn*
  > Jer 49:13 For I have sworn by myself, declares the Lord , that Bozrah shall become a horror , a taunt , a waste , and a curse , and all her cities shall be perpetual wastes .”
- **Jer 51:14** (—) *target: sworn*
  > Jer 51:14 The Lord of hosts has sworn by himself : Surely I will fill you with men , as many as locusts , and they shall raise the shout of victory over you.

### `G0802` — 1/1 classified · 1 anchor verse(s)

**Group `3284-001`** (1 verse — anchors: Rom 1:31)

- **Rom 1:31** 🔵 (✓) *target: faithless*
  > Rom 1:31 foolish , faithless , heartless , ruthless .

### `G1242` — 27/30 classified · 3 anchor verse(s)

**Group `766-001`** (17 verses — anchors: Mat 26:28)

- **Mat 26:28** 🔵 (✓) *target: covenant*
  > Mat 26:28 for this is my blood of the covenant , which is poured out for many for the forgiveness of sins .
- **Mar 14:24** (✓) *target: covenant*
  > Mar 14:24 And he said to them , “ This is my blood of the covenant , which is poured out for many .
- **Luk 1:72** (✓) *target: covenant*
  > Luk 1:72 to show the mercy promised to our fathers and to remember his holy covenant ,
- **Luk 22:20** (✓) *target: covenant*
  > Luk 22:20 And likewise the cup after they had eaten , saying , “ This cup that is poured out for you is the new covenant in my blood .
- **Act 3:25** (✓) *target: covenant*
  > Act 3:25 You are the sons of the prophets and of the covenant that God made with your fathers , saying to Abraham , ‘ And in your offspring shall all the families of the earth be blessed .’
- **Act 7:8** (✓) *target: covenant*
  > Act 7:8 And he gave him the covenant of circumcision . And so Abraham became the father of Isaac , and circumcised him on the eighth day , and Isaac became the father of Jacob , and Jacob of the twelve patriarchs .
- **Rom 11:27** (✓) *target: covenant*
  > Rom 11:27 “ and this will be my covenant with them when I take away their sins .”
- **1Cor 11:25** (✓) *target: covenant*
  > 1Cor 11:25 In the same way also he took the cup , after supper , saying , “ This cup is the new covenant in my blood . Do this , as often as you drink it, in remembrance of me .”
- **Heb 7:22** (✓) *target: covenant*
  > Heb 7:22 This makes Jesus the guarantor of a better covenant .
- **Heb 8:6** (✓) *target: covenant*
  > Heb 8:6 But as it is , Christ has obtained a ministry that is as much more excellent than the old as the covenant he mediates is better , since it is enacted on better promises .
- **Heb 8:9** (✓) *target: covenant*
  > Heb 8:9 not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt . For they did not continue in my covenant , and so I showed no concern for them , declares the Lord .
- **Heb 9:15** (✓) *target: covenant*
  > Heb 9:15 Therefore he is the mediator of a new covenant , so that those who are called may receive the promised eternal inheritance , since a death has occurred that redeems them from the transgressions committed under the first covenant .
- **Heb 9:20** (✓) *target: covenant*
  > Heb 9:20 saying , “ This is the blood of the covenant that God commanded for you .”
- **Heb 10:29** (✓) *target: covenant*
  > Heb 10:29 How much worse punishment , do you think , will be deserved by the one who has trampled underfoot the Son of God , and has profaned the blood of the covenant by which he was sanctified , and has outraged the Spirit of grace ?
- **Heb 12:24** (✓) *target: covenant*
  > Heb 12:24 and to Jesus , the mediator of a new covenant , and to the sprinkled blood that speaks a better word than the blood of Abel .
- **Heb 13:20** (✓) *target: covenant*
  > Heb 13:20 Now may the God of peace who brought again from the dead our Lord Jesus , the great shepherd of the sheep , by the blood of the eternal covenant ,
- **Rev 11:19** (✓) *target: covenant*
  > Rev 11:19 Then God’s temple in heaven was opened , and the ark of his covenant was seen within his temple . There were flashes of lightning , rumblings , peals of thunder , an earthquake , and heavy hail .

**Group `766-002`** (5 verses — anchors: Heb 8:10)

- **Heb 8:10** 🔵 (✓) *target: covenant*
  > Heb 8:10 For this is the covenant that I will make with the house of Israel after those days , declares the Lord : I will put my laws into their minds , and write them on their hearts , and I will be their God , and they shall be my people .
- **2Cor 3:6** (✓) *target: covenant*
  > 2Cor 3:6 who has made us sufficient to be ministers of a new covenant , not of the letter but of the Spirit . For the letter kills , but the Spirit gives life .
- **2Cor 3:14** (✓) *target: covenant*
  > 2Cor 3:14 But their minds were hardened . For to this day , when they read the old covenant , that same veil remains unlifted , because only through Christ is it taken away .
- **Heb 8:8** (✓) *target: covenant*
  > Heb 8:8 For he finds fault with them when he says : “ Behold , the days are coming , declares the Lord , when I will establish a new covenant with the house of Israel and with the house of Judah ,
- **Heb 10:16** (✓) *target: covenant*
  > Heb 10:16 “ This is the covenant that I will make with them after those days , declares the Lord : I will put my laws on their hearts , and write them on their minds ,”

**Group `766-003`** (5 verses — anchors: Eph 2:12)

- **Eph 2:12** 🔵 (✓) *target: covenants*
  > Eph 2:12 remember that you were at that time separated from Christ , alienated from the commonwealth of Israel and strangers to the covenants of promise , having no hope and without God in the world .
- **Rom 9:4** (✓) *target: covenants*
  > Rom 9:4 They are Israelites , and to them belong the adoption , the glory , the covenants , the giving of the law , the worship , and the promises .
- **Gal 3:15** (✓) *target: covenant*
  > Gal 3:15 To give a human example , brothers : even with a man-made covenant , no one annuls it or adds to it once it has been ratified .
- **Gal 3:17** (✓) *target: covenant*
  > Gal 3:17 This is what I mean : the law , which came 430 years afterward , does not annul a covenant previously ratified by God , so as to make the promise void .
- **Gal 4:24** (✓) *target: covenants*
  > Gal 4:24 Now this may be interpreted allegorically : these women are two covenants . One is from Mount Sinai , bearing children for slavery ; she is Hagar .

**Group `UNCLASSIFIED`** (3 verses)

- **Heb 9:4** (—) *target: covenant*
  > Heb 9:4 having the golden altar of incense and the ark of the covenant covered on all sides with gold , in which was a golden urn holding the manna , and Aaron’s staff that budded , and the tablets of the covenant .
- **Heb 9:16** (—) *target: will*
  > Heb 9:16 For where a will is involved, the death of the one who made it must be established .
- **Heb 9:17** (—) *target: will*
  > Heb 9:17 For a will takes effect only at death , since it is not in force as long as the one who made it is alive .

### `G2537` — 16/16 classified · 3 anchor verse(s)

**Group `777-001`** (5 verses — anchors: 2Cor 3:6)

- **2Cor 3:6** 🔵 (✓) *target: new*
  > 2Cor 3:6 who has made us sufficient to be ministers of a new covenant , not of the letter but of the Spirit . For the letter kills , but the Spirit gives life .
- **1Cor 11:25** (✓) *target: new*
  > 1Cor 11:25 In the same way also he took the cup , after supper , saying , “ This cup is the new covenant in my blood . Do this , as often as you drink it, in remembrance of me .”
- **Heb 8:8** (✓) *target: new*
  > Heb 8:8 For he finds fault with them when he says : “ Behold , the days are coming , declares the Lord , when I will establish a new covenant with the house of Israel and with the house of Judah ,
- **Heb 8:13** (✓) *target: new*
  > Heb 8:13 In speaking of a new covenant, he makes the first one obsolete . And what is becoming obsolete and growing old is ready to vanish away .
- **Heb 9:15** (✓) *target: new*
  > Heb 9:15 Therefore he is the mediator of a new covenant , so that those who are called may receive the promised eternal inheritance , since a death has occurred that redeems them from the transgressions committed under the first covenant .

**Group `777-002`** (4 verses — anchors: Eph 4:24)

- **Eph 4:24** 🔵 (✓) *target: new*
  > Eph 4:24 and to put on the new self , created after the likeness of God in true righteousness and holiness .
- **2Cor 5:17** (✓) *target: new*
  > 2Cor 5:17 Therefore , if anyone is in Christ , he is a new creation . The old has passed away ; behold , the new has come .
- **Gal 6:15** (✓) *target: new*
  > Gal 6:15 For neither circumcision counts for anything , nor uncircumcision , but a new creation .
- **Eph 2:15** (✓) *target: new*
  > Eph 2:15 by abolishing the law of commandments expressed in ordinances , that he might create in himself one new man in place of the two , so making peace ,

**Group `777-003`** (7 verses — anchors: Rev 2:17)

- **Rev 2:17** 🔵 (✓) *target: new*
  > Rev 2:17 He who has an ear , let him hear what the Spirit says to the churches . To the one who conquers I will give some of the hidden manna , and I will give him a white stone , with a new name written on the stone that no one knows except the one who receives it.’
- **Rev 3:12** (✓) *target: new*
  > Rev 3:12 The one who conquers , I will make him a pillar in the temple of my God . Never shall he go out of it, and I will write on him the name of my God , and the name of the city of my God , the new Jerusalem , which comes down from my God out of heaven , and my own new name .
- **Rev 5:9** (✓) *target: new*
  > Rev 5:9 And they sang a new song , saying , “ Worthy are you to take the scroll and to open its seals , for you were slain , and by your blood you ransomed people for God from every tribe and language and people and nation ,
- **Rev 14:3** (✓) *target: new*
  > Rev 14:3 and they were singing a new song before the throne and before the four living creatures and before the elders . No one could learn that song except the 144,000 who had been redeemed from the earth .
- **Rev 21:1** (✓) *target: new*
  > Rev 21:1 Then I saw a new heaven and a new earth , for the first heaven and the first earth had passed away , and the sea was no more .
- **Rev 21:2** (✓) *target: new*
  > Rev 21:2 And I saw the holy city , new Jerusalem , coming down out of heaven from God , prepared as a bride adorned for her husband .
- **Rev 21:5** (✓) *target: new*
  > Rev 21:5 And he who was seated on the throne said , “ Behold , I am making all things new .” Also he said , “ Write this down, for these words are trustworthy and true .”

### `G2787G` — 2/3 classified · 1 anchor verse(s)

**Group `3270-001`** (2 verses — anchors: Rev 11:19)

- **Rev 11:19** 🔵 (✓) *target: ark*
  > Rev 11:19 Then God’s temple in heaven was opened , and the ark of his covenant was seen within his temple . There were flashes of lightning , rumblings , peals of thunder , an earthquake , and heavy hail .
- **Heb 9:4** (✓) *target: ark*
  > Heb 9:4 having the golden altar of incense and the ark of the covenant covered on all sides with gold , in which was a golden urn holding the manna , and Aaron’s staff that budded , and the tablets of the covenant .

**Group `UNCLASSIFIED`** (1 verse)

- **Heb 11:7** (—) *target: ark*
  > Heb 11:7 By faith Noah , being warned by God concerning events as yet unseen , in reverent fear constructed an ark for the saving of his household . By this he condemned the world and became an heir of the righteousness that comes by faith .

### `G2787H` — 1/3 classified · 1 anchor verse(s)

**Group `3271-001`** (1 verse — anchors: 1Pe 3:20)

- **1Pe 3:20** 🔵 (✓) *target: ark*
  > 1Pe 3:20 because they formerly did not obey , when God’s patience waited in the days of Noah , while the ark was being prepared , in which a few , that is , eight persons , were brought safely through water .

**Group `UNCLASSIFIED`** (2 verses)

- **Mat 24:38** (—) *target: ark*
  > Mat 24:38 For as in those days before the flood they were eating and drinking , marrying and giving in marriage , until the day when Noah entered the ark ,
- **Luk 17:27** (—) *target: ark*
  > Luk 17:27 They were eating and drinking and marrying and being given in marriage , until the day when Noah entered the ark , and the flood came and destroyed them all .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**15 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H0423` | oath | `not_done` | 14 | 2 | 14 |
| `H0548` | sure | `not_done` | 2 | 1 | 1 |
| `H1285` | covenant | `not_done` | 236 | 5 | 161 |
| `H1286` | [Baal]-berith | `not_done` | 1 | 0 | 1 |
| `H3748` | divorce | `not_done` | 4 | 2 | 4 |
| `H3772G` | to cut: cut | `not_done` | 50 | 2 | 50 |
| `H3772H` | to cut: make [covenant] | `not_done` | 87 | 4 | 85 |
| `H3772J` | to cut: lack | `not_done` | 10 | 1 | 9 |
| `H7620I` | week | `not_done` | 6 | 2 | 6 |
| `H7650` | to swear | `not_done` | 175 | 4 | 131 |
| `G0802` | untrustworthy | `not_done` | 1 | 1 | 1 |
| `G1242` | covenant | `not_done` | 30 | 3 | 27 |
| `G2537` | new | `not_done` | 16 | 3 | 16 |
| `G2787G` | ark: covenant | `not_done` | 3 | 1 | 2 |
| `G2787H` | ark: Noah | `not_done` | 3 | 1 | 1 |

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

### Registry-specific questions for 034 covenant

_None._ No questions in `wa_obs_question_catalogue` are sourced from registry 34 (covenant).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-01T09:47:16Z`
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

*End of readiness output v3 — wa-034-covenant.*