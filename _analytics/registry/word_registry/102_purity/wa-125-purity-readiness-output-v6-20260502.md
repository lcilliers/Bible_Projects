# wa-125-purity — Analysis Readiness Output (v6)

_v6 generation · 2026-05-02T15:24:55Z · schema 3.17.0 · catalogue v2-2026-04-29 (T0–T7)_

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

- **Registry no:** `125` · **word:** `purity`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `wa-dimensionreview-instruction-v3_3-20260418`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 12  (programme-wide aggregate including XREF and historical terms — current OWNER count is 12, XREF 0)
- `phase1_verse_count`: 206  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 1 unresolved · **Existing session_b_findings:** 1

**Description:**

> Purity is the quality of being unmixed — single, uncontaminated, devoted to one thing without internal division or compromise. The Hebrew and Greek vocabulary covers both the ritual purity required for approach to God and the moral-inner purity that makes a person's motives and desires clean. Jesus radically internalises purity: blessed are the pure in heart. Purity of heart in the biblical sense is not innocence of experience but the absence of duplicity — wanting one thing, being directed toward one end.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-02T15:24:55Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 12
- **OWNER terms legacy-VC (not_done):** 12 / 12

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 12 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H2889` | ta.hor | pure | H | `extracted` | **`not_done`** | 1 | 87 | 4/0 | 58/0 | 4 |
| `H2890` | te.hor | pureness | H | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H2891` | ta.her | be pure | H | `extracted` | **`not_done`** | 1 | 79 | 3/0 | 71/0 | 3 |
| `H2892A` | to.har | purity | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 3/0 | 1 |
| `H2892B` | to.har | clearness | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 3/0 | 1 |
| `H2893` | to.ho.rah | purifying | H | `extracted` | **`not_done`** | 1 | 11 | 2/0 | 11/0 | 2 |
| `G0047` | hagneia | purity | G | `extracted` | **`not_done`** | 1 | 2 | 1/0 | 2/0 | 1 |
| `G0048` | hagnizō | to purify | G | `extracted` | **`not_done`** | 1 | 7 | 2/0 | 7/0 | 2 |
| `G0049` | hagnismos | purification | G | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G0053` | hagnos | pure | G | `extracted` | **`not_done`** | 1 | 8 | 2/0 | 8/0 | 2 |
| `G0054` | hagnotēs | purity | G | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `G0055` | hagnōs | purely | G | `extracted` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H2889` — ta.hor "pure"

**Identity:** mti=1063 · ti=1141 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: pure, clean

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): clean (ceremonially-of animals)
  - `1b` (under `None`): pure (physically)
  - `1c` (under `None`): pure, clean (morally, ethically)

**Root family:**
- `TAHOR` (Hebrew): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H2890` te.hor "pureness"
- `H2891` ta.her "be pure"
- `H2892A` to.har "purity"
- `H2892B` to.har "clearness"
- `H2893` to.ho.rah "purifying"

### `H2890` — te.hor "pureness"

**Identity:** mti=6060 · ti=6165 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: pureness, cleanness, clean, pure

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): clean (ceremonially-of animals)
  - `1b` (under `None`): pure (physically)
  - `1c` (under `None`): pure, clean (morally, ethically)

**Root family:**
- `TAHOR` (Hebrew): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H2889` ta.hor "pure"
- `H2891` ta.her "be pure"
- `H2892A` to.har "purity"
- `H2892B` to.har "clearness"
- `H2893` to.ho.rah "purifying"

### `H2891` — ta.her "be pure"

**Identity:** mti=6057 · ti=6162 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to be clean, be pure

Sub-senses (depth > 1): 17 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal)
  - `1a1` (under `None`): to be clean (physically-of disease)
  - `1a2` (under `None`): to be clean ceremonially
  - `1a3` (under `None`): to purify, be clean morally, made clean
  - `1b` (under `None`): (Piel)
  - `1b1` (under `None`): to cleanse, purify
  - `1b1a` (under `1b`): physically
  - `1b1b` (under `1b`): ceremonially
  - `1b1c` (under `1b`): morally
  - `1b2` (under `None`): to pronounce clean
  - `1b3` (under `None`): to perform the ceremony of cleansing
  - `1c` (under `None`): (Pual) to be cleansed, be pronounced clean
  - `1d` (under `None`): (Hithpael)
  - `1d1` (under `None`): to purify oneself
  - `1d1a` (under `1d`): ceremonially

**Root family:**
- `TAHOR` (Hebrew): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H2889` ta.hor "pure"
- `H2890` te.hor "pureness"
- `H2892A` to.har "purity"
- `H2892B` to.har "clearness"
- `H2893` to.ho.rah "purifying"

### `H2892A` — to.har "purity"

**Identity:** mti=6059 · ti=6164 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: purity, purification, purifying

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): purity
  - `1b` (under `None`): purifying

**Root family:**
- `TAHOR` (Hebrew): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H2889` ta.hor "pure"
- `H2890` te.hor "pureness"
- `H2891` ta.her "be pure"
- `H2892B` to.har "clearness"
- `H2893` to.ho.rah "purifying"

### `H2892B` — to.har "clearness"

**Identity:** mti=6061 · ti=6166 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: clearness, lustre

**Root family:**
- `TAHOR` (Hebrew): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H2889` ta.hor "pure"
- `H2890` te.hor "pureness"
- `H2891` ta.her "be pure"
- `H2892A` to.har "purity"
- `H2893` to.ho.rah "purifying"

### `H2893` — to.ho.rah "purifying"

**Identity:** mti=6058 · ti=6163 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: purifying, cleansing, purification, purity, cleanness

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): purifying, menstruation
  - `1b` (under `None`): cleansing, purification

**Root family:**
- `TAHOR` (Hebrew): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `H2889` ta.hor "pure"
- `H2890` te.hor "pureness"
- `H2891` ta.her "be pure"
- `H2892A` to.har "purity"
- `H2892B` to.har "clearness"

### `G0047` — hagneia "purity"

**Identity:** mti=1062 · ti=1140 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: purity, in the sense of moral purity and proper sexual conduct 
chastity, 1Tim. 4:12; 5:2*

**Root family:**
- `HAGN` (Greek): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0048` hagnizō "to purify"
- `G0049` hagnismos "purification"
- `G0053` hagnos "pure"
- `G0054` hagnotēs "purity"
- `G0055` hagnōs "purely"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0048` — hagnizō "to purify"

**Identity:** mti=6054 · ti=6159 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to purify, ceremonially cleanse 
to purify morally, reform, to live like one under a vow of abstinence, as the Nazarites

**Root family:**
- `HAGN` (Greek): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0047` hagneia "purity"
- `G0049` hagnismos "purification"
- `G0053` hagnos "pure"
- `G0054` hagnotēs "purity"
- `G0055` hagnōs "purely"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0049` — hagnismos "purification"

**Identity:** mti=6055 · ti=6160 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: purification, abstinence, Acts 21:26*

**Root family:**
- `HAGN` (Greek): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0047` hagneia "purity"
- `G0048` hagnizō "to purify"
- `G0053` hagnos "pure"
- `G0054` hagnotēs "purity"
- `G0055` hagnōs "purely"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0053` — hagnos "pure"

**Identity:** mti=6053 · ti=6158 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: pure (in some contexts morally pure), innocent 
chaste, modest, blameless

**Root family:**
- `HAGN` (Greek): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `G0040G` hagios "holy"
- `G0040H` hagios "holy: saint"
- `G0047` hagneia "purity"
- `G0048` hagnizō "to purify"
- `G0049` hagnismos "purification"
- `G0054` hagnotēs "purity"
- `G0055` hagnōs "purely"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0054` — hagnotēs "purity"

**Identity:** mti=1064 · ti=1142 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: purity, life of purity, 2Cor. 6:6; 11:3*

**Root family:**
- `HAGN` (Greek): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0047` hagneia "purity"
- `G0048` hagnizō "to purify"
- `G0049` hagnismos "purification"
- `G0053` hagnos "pure"
- `G0055` hagnōs "purely"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0055` — hagnōs "purely"

**Identity:** mti=6056 · ti=6161 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:11:22): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: - purely, i.e. honestly, with pure motives: Php.1.17. 
purely, sincerely

**Root family:**
- `HAGN` (Greek): pure — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0047` hagneia "purity"
- `G0048` hagnizō "to purify"
- `G0049` hagnismos "purification"
- `G0053` hagnos "pure"
- `G0054` hagnotēs "purity"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (0)

_None._

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H2889` — 4 groups

- **`1063-001`** — 6 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term describes the purity of the heart and inner person as moral and spiritual integrity before God — an inner life free from corruption and oriented toward God*
- **`1063-002`** — 3 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term describes purity attributed to God's word and the fear of the Lord — the quality of inner spiritual integrity that characterises divine revelation and right orientation toward God*
- **`1063-003`** — 6 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term describes the covenantal and spiritual restoration of the inner person — being made clean before God through divine action, removing inner defilement and renewing covenantal relationship*
- **`1063-004`** — 43 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term describes ritual/levitical cleanness as a covenantal condition governing access to God and sacred space — the state of being clean as prerequisite for worship and community life*

### `H2890` — 1 groups

- **`6060-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term describes the absolute moral purity of God's character — an inner quality of divine nature that is incompatible with evil or wrongdoing*

### `H2891` — 3 groups

- **`6057-001`** — 11 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term describes the purification of the inner person from sin and moral defilement — the heart and soul made pure through divine cleansing, repentance, and spiritual renewal*
- **`6057-002`** — 43 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term describes ritual cleansing as a covenantal act of transition — the person made ritually clean through prescribed acts, enabling restored participation in sacred community*
- **`6057-003`** — 17 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term describes God's purifying action upon priests, Levites, and people — cleansing for restored covenantal service and communal life*

### `H2892A` — 1 groups

- **`6059-001`** — 3 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term names the ritual period of purification following childbirth — the covenantal state of the post-partum woman and her transition back to full community participation*

### `H2892B` — 1 groups

- **`6061-001`** — 3 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term names the ritual purification period as a state of cleansing — the post-partum woman's covenantal condition during and after the prescribed period of purification*

### `H2893` — 2 groups

- **`6058-001`** — 8 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term names the prescribed purification procedure as the covenantal pathway governing a person's return to community and sacred participation*
- **`6058-002`** — 3 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term names purification as a covenantal service and inner-oriented commitment — the person setting their heart toward God even where external cleanness requirements are imperfectly met*

### `G0047` — 1 groups

- **`1062-001`** — 2 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names moral and relational purity as an inner character disposition — the quality of heart and motivation governing conduct and relationships*

### `G0048` — 2 groups

- **`6054-001`** — 3 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term names the act of inner moral and spiritual purification — soul, heart, and self purified through obedience, hope, and turning toward God*
- **`6054-002`** — 4 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term names ritual purification as an act of preparation expressing inner orientation of readiness and covenantal reverence toward God*

### `G0049` — 1 groups

- **`6055-001`** — 1 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Term names the structured purification process as an act of ritual preparation expressing inner readiness and covenantal participation*

### `G0053` — 2 groups

- **`6053-001`** — 5 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term describes the morally pure inner character — the quality of heart, mind, and motivation that is free from defilement and moral corruption*
- **`6053-002`** — 3 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term describes relational and covenantal purity — inner disposition of fidelity and undivided orientation in relationship to Christ or within human relationships*

### `G0054` — 1 groups

- **`1064-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names purity as an inner character quality among the dispositions through which authentic apostolic ministry is expressed*

### `G0055` — 1 groups

- **`6056-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term qualifies inner motivation — names pure and sincere motivation as the inner disposition from which authentic action ought to flow, in contrast to selfish ambition*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

_No XREF sharing._

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 86 impurity | 26 |
| 73 guilt | 11 |
| 111 mercy | 11 |
| 103 love | 6 |
| 76 holiness | 4 |
| 98 justice | 4 |
| 112 mind | 4 |
| 117 peace | 4 |
| 187 strength | 4 |
| 197 authority | 4 |
| 1 abomination | 3 |
| 61 fear | 3 |
| 77 honesty | 3 |
| 78 hope | 3 |
| 81 hypocrisy | 3 |
| 128 rebellion | 3 |
| 177 worth | 3 |
| 180 yielding | 3 |
| 182 Soul | 3 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 44 despair | Psa 19:9 |
| 56 envy | 2Cor 11:2 |
| 61 fear | Psa 19:9 |
| 66 gentleness | Jam 3:17 |
| 76 holiness | Lev 10:10 |
| 86 impurity | Eze 36:25 |
| 111 mercy | Jam 3:17 |
| 117 peace | Jam 3:17 |
| 191 doubt | Jam 3:17 |
| 196 power | Hab 1:13 |
| 197 authority | Psa 51:2 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-125-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> The tahor/taher word family in the purity registry spans ritual cleansing (external covenantal state), moral purification (inner), and divine restorative action. Session B should map how the ritual and moral dimensions relate — and whether the programme treats purity primarily as an inner character quality or as a covenantal status granted and maintained through prescribed practice.

### H.2 Open SD pointers + research flags (1)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SD_POINTER` | DIM-125-SD001 | HIGH | Session D | 2026-05-02 |

#### DIM-125-SD001

> R125 (purity) reveals a persistent structural distinction within the concept of purity: (1) Moral Character — purity as inner character quality (stable); (2) Transformation — purification as inner change process; (3) Dependence/Creatureliness — ritual cleanness as creaturely dependence on divinely-specified conditions for access; (4) Relational Disposition — covenantal fidelity and heart-orientation toward God. The ritual-purity vocabulary (Hebrew H2891 taher, H2893 tohorah, H2892 tohar) is almost entirely Dependence/Creatureliness or Transformation — it does not primarily name moral character but covenantal standing and access. The moral-character vocabulary (Greek G0047 hagneia, G0054 hagnotēs, G0053 hagnos) belongs to NT Greek. Session D should explore whether purity/cleanness and moral character are being conflated in popular usage, and whether the OT covenantal-access concept and the NT inner-moral concept represent distinct contributions to the super-concept.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

_No phase2 flags on any OWNER term._

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H2889` — 58/87 classified · 4 anchor verse(s)

**Group `1063-001`** (6 verses — anchors: Psa 51:10)

- **Psa 51:10** 🔵 (✓) *target: clean*
  > Psa 51:10 Create in me a clean heart , O God , and renew a right spirit within me.
- **1Sa 20:26** (✓) *target: clean*
  > 1Sa 20:26 Yet Saul did not say anything that day , for he thought , “Something has happened to him . He is not clean ; surely he is not clean .”
- **Job 14:4** (✓) *target: clean thing*
  > Job 14:4 Who can bring a clean thing out of an unclean ? There is not one .
- **Job 17:9** (✓) *target: clean*
  > Job 17:9 Yet the righteous holds to his way , and he who has clean hands grows stronger and stronger .
- **Pro 22:11** (✓) *target: purity*
  > Pro 22:11 He who loves purity of heart , and whose speech is gracious , will have the king as his friend .
- **Pro 30:12** (✓) *target: clean*
  > Pro 30:12 There are those who are clean in their own eyes but are not washed of their filth .

**Group `1063-002`** (3 verses — anchors: Psa 19:9)

- **Psa 19:9** 🔵 (✓) *target: clean*
  > Psa 19:9 the fear of the Lord is clean , enduring forever ; the rules of the Lord are true , and righteous altogether .
- **Psa 12:6** (✓) *target: pure*
  > Psa 12:6 The words of the Lord are pure words , like silver refined in a furnace on the ground , purified seven times .
- **Pro 15:26** (✓) *target: pure*
  > Pro 15:26 The thoughts of the wicked are an abomination to the Lord , but gracious words are pure .

**Group `1063-003`** (6 verses — anchors: Eze 36:25)

- **Eze 36:25** 🔵 (✓) *target: clean*
  > Eze 36:25 I will sprinkle clean water on you, and you shall be clean from all your uncleannesses , and from all your idols I will cleanse you .
- **Ezr 6:20** (✓) *target: clean*
  > Ezr 6:20 For the priests and the Levites had purified themselves together ; all of them were clean . So they slaughtered the Passover lamb for all the returned exiles , for their fellow priests , and for themselves .
- **Eze 22:26** (✓) *target: clean*
  > Eze 22:26 Her priests have done violence to my law and have profaned my holy things . They have made no distinction between the holy and the common , neither have they taught the difference between the unclean and the clean , and they have disregarded my Sabbaths , so that I am profaned among them.
- **Eze 44:23** (✓) *target: clean*
  > Eze 44:23 They shall teach my people the difference between the holy and the common , and show them how to distinguish between the unclean and the clean .
- **Zec 3:5** (✓) *target: clean*
  > Zec 3:5 And I said , “Let them put a clean turban on his head .” So they put a clean turban on his head and clothed him with garments . And the angel of the Lord was standing by.
- **Mal 1:11** (✓) *target: pure*
  > Mal 1:11 For from the rising of the sun to its setting my name will be great among the nations , and in every place incense will be offered to my name , and a pure offering . For my name will be great among the nations , says the Lord of hosts .

**Group `1063-004`** (43 verses — anchors: Lev 10:10)

- **Lev 10:10** 🔵 (✓) *target: clean*
  > Lev 10:10 You are to distinguish between the holy and the common , and between the unclean and the clean ,
- **Gen 7:2** (✓) *target: clean*
  > Gen 7:2 Take with you seven pairs of all clean animals , the male and his mate , and a pair of the animals that are not clean , the male and his mate ,
- **Gen 7:8** (✓) *target: clean*
  > Gen 7:8 Of clean animals , and of animals that are not clean , and of birds , and of everything that creeps on the ground ,
- **Gen 8:20** (✓) *target: clean*
  > Gen 8:20 Then Noah built an altar to the Lord and took some of every clean animal and some of every clean bird and offered burnt offerings on the altar .
- **Lev 4:12** (✓) *target: clean*
  > Lev 4:12 all the rest of the bull —he shall carry outside the camp to a clean place , to the ash heap , and shall burn it up on a fire of wood . On the ash heap it shall be burned up .
- **Lev 6:11** (✓) *target: clean*
  > Lev 6:11 Then he shall take off his garments and put on other garments and carry the ashes outside the camp to a clean place .
- **Lev 7:19** (✓) *target: clean*
  > Lev 7:19 “ Flesh that touches any unclean thing shall not be eaten . It shall be burned up with fire . All who are clean may eat flesh ,
- **Lev 10:14** (✓) *target: clean*
  > Lev 10:14 But the breast that is waved and the thigh that is contributed you shall eat in a clean place , you and your sons and your daughters with you, for they are given as your due and your sons ’ due from the sacrifices of the peace offerings of the people of Israel .
- **Lev 11:36** (✓) *target: clean*
  > Lev 11:36 Nevertheless , a spring or a cistern holding water shall be clean , but whoever touches a carcass in them shall be unclean .
- **Lev 11:37** (✓) *target: clean*
  > Lev 11:37 And if any part of their carcass falls upon any seed grain that is to be sown , it is clean ,
- **Lev 11:47** (✓) *target: clean*
  > Lev 11:47 to make a distinction between the unclean and the clean and between the living creature that may be eaten and the living creature that may not be eaten .
- **Lev 13:13** (✓) *target: clean*
  > Lev 13:13 then the priest shall look , and if the leprous disease has covered all his body , he shall pronounce him clean of the disease ; it has all turned white , and he is clean .
- **Lev 13:17** (✓) *target: clean*
  > Lev 13:17 and the priest shall examine him, and if the disease has turned white , then the priest shall pronounce the diseased person clean ; he is clean .
- **Lev 13:37** (✓) *target: clean*
  > Lev 13:37 But if in his eyes the itch is unchanged and black hair has grown in it, the itch is healed and he is clean , and the priest shall pronounce him clean .
- **Lev 13:39** (✓) *target: clean*
  > Lev 13:39 the priest shall look , and if the spots on the skin of the body are of a dull white , it is leukoderma that has broken out in the skin ; he is clean .
- **Lev 13:40** (✓) *target: clean*
  > Lev 13:40 “ If a man’s hair falls out from his head , he is bald ; he is clean .
- **Lev 13:41** (✓) *target: clean*
  > Lev 13:41 And if a man’s hair falls out from his forehead , he has baldness of the forehead; he is clean .
- **Lev 14:4** (✓) *target: clean*
  > Lev 14:4 the priest shall command them to take for him who is to be cleansed two live clean birds and cedarwood and scarlet yarn and hyssop .
- **Lev 14:57** (✓) *target: clean*
  > Lev 14:57 to show when it is unclean and when it is clean . This is the law for leprous disease .
- **Lev 15:8** (✓) *target: clean*
  > Lev 15:8 And if the one with the discharge spits on someone who is clean , then he shall wash his clothes and bathe himself in water and be unclean until the evening .
- **Lev 20:25** (✓) *target: clean*
  > Lev 20:25 You shall therefore separate the clean beast from the unclean , and the unclean bird from the clean . You shall not make yourselves detestable by beast or by bird or by anything with which the ground crawls , which I have set apart for you to hold unclean .
- **Lev 24:4** (✓) *target: pure*
  > Lev 24:4 He shall arrange the lamps on the lampstand of pure gold before the Lord regularly .
- **Lev 24:6** (✓) *target: pure*
  > Lev 24:6 And you shall set them in two piles , six in a pile , on the table of pure gold before the Lord .
- **Num 5:28** (✓) *target: clean*
  > Num 5:28 But if the woman has not defiled herself and is clean , then she shall be free and shall conceive children .
- **Num 9:13** (✓) *target: clean*
  > Num 9:13 But if anyone who is clean and is not on a journey fails to keep the Passover , that person shall be cut off from his people because he did not bring the Lord’s offering at its appointed time ; that man shall bear his sin .
- **Num 18:11** (✓) *target: clean*
  > Num 18:11 This also is yours: the contribution of their gift , all the wave offerings of the people of Israel . I have given them to you, and to your sons and daughters with you, as a perpetual due . Everyone who is clean in your house may eat it .
- **Num 18:13** (✓) *target: clean*
  > Num 18:13 The first ripe fruits of all that is in their land , which they bring to the Lord , shall be yours. Everyone who is clean in your house may eat it .
- **Num 19:9** (✓) *target: clean*
  > Num 19:9 And a man who is clean shall gather up the ashes of the heifer and deposit them outside the camp in a clean place . And they shall be kept for the water for impurity for the congregation of the people of Israel ; it is a sin offering .
- **Num 19:18** (✓) *target: clean*
  > Num 19:18 Then a clean person shall take hyssop and dip it in the water and sprinkle it on the tent and on all the furnishings and on the persons who were there and on whoever touched the bone , or the slain or the dead or the grave .
- **Num 19:19** (✓) *target: clean person*
  > Num 19:19 And the clean person shall sprinkle it on the unclean on the third day and on the seventh day . Thus on the seventh day he shall cleanse him, and he shall wash his clothes and bathe himself in water , and at evening he shall be clean .
- **Deu 12:15** (✓) *target: clean*
  > Deu 12:15 “ However , you may slaughter and eat meat within any of your towns , as much as you desire , according to the blessing of the Lord your God that he has given you. The unclean and the clean may eat of it, as of the gazelle and as of the deer .
- **Deu 12:22** (✓) *target: clean*
  > Deu 12:22 Just as the gazelle or the deer is eaten , so you may eat of it. The unclean and the clean alike may eat of it .
- **Deu 14:11** (✓) *target: clean*
  > Deu 14:11 “You may eat all clean birds .
- **Deu 14:20** (✓) *target: clean*
  > Deu 14:20 All clean winged things you may eat .
- **Deu 15:22** (✓) *target: clean*
  > Deu 15:22 You shall eat it within your towns . The unclean and the clean alike may eat it, as though it were a gazelle or a deer .
- **Deu 23:10** (✓) *target: becomes*
  > Deu 23:10 “ If any man among you becomes unclean because of a nocturnal emission , then he shall go outside the camp . He shall not come inside the camp ,
- **1Ch 28:17** (✓) *target: pure*
  > 1Ch 28:17 and pure gold for the forks , the basins and the cups ; for the golden bowls and the weight of each; for the silver bowls and the weight of each;
- **2Ch 3:4** (✓) *target: pure*
  > 2Ch 3:4 The vestibule in front of the nave of the house was twenty cubits long , equal to the width of the house , and its height was 120 cubits. He overlaid it on the inside with pure gold .
- **2Ch 9:17** (✓) *target: pure*
  > 2Ch 9:17 The king also made a great ivory throne and overlaid it with pure gold .
- **2Ch 13:11** (✓) *target: pure*
  > 2Ch 13:11 They offer to the Lord every morning and every evening burnt offerings and incense of sweet spices , set out the showbread on the table of pure gold , and care for the golden lampstand that its lamps may burn every evening . For we keep the charge of the Lord our God , but you have forsaken him .
- **2Ch 30:17** (✓) *target: clean*
  > 2Ch 30:17 For there were many in the assembly who had not consecrated themselves. Therefore the Levites had to slaughter the Passover lamb for everyone who was not clean , to consecrate it to the Lord .
- **Ecc 9:2** (✓) *target: clean*
  > Ecc 9:2 It is the same for all , since the same event happens to the righteous and the wicked , to the good and the evil , to the clean and the unclean , to him who sacrifices and him who does not sacrifice . As the good one is, so is the sinner , and he who swears is as he who shuns an oath .
- **Isa 66:20** (✓) *target: clean*
  > Isa 66:20 And they shall bring all your brothers from all the nations as an offering to the Lord , on horses and in chariots and in litters and on mules and on dromedaries , to my holy mountain Jerusalem , says the Lord , just as the Israelites bring their grain offering in a clean vessel to the house of the Lord .

**Group `UNCLASSIFIED`** (29 verses)

- **Exo 25:11** (—) *target: pure*
  > Exo 25:11 You shall overlay it with pure gold , inside and outside shall you overlay it, and you shall make on it a molding of gold around it.
- **Exo 25:17** (—) *target: pure*
  > Exo 25:17 “You shall make a mercy seat of pure gold . Two cubits and a half shall be its length , and a cubit and a half its breadth .
- **Exo 25:24** (—) *target: pure*
  > Exo 25:24 You shall overlay it with pure gold and make a molding of gold around it.
- **Exo 25:29** (—) *target: pure*
  > Exo 25:29 And you shall make its plates and dishes for incense, and its flagons and bowls with which to pour drink offerings ; you shall make them of pure gold .
- **Exo 25:31** (—) *target: pure*
  > Exo 25:31 “You shall make a lampstand of pure gold . The lampstand shall be made of hammered work : its base , its stem , its cups , its calyxes , and its flowers shall be of one piece with it .
- **Exo 25:36** (—) *target: pure*
  > Exo 25:36 Their calyxes and their branches shall be of one piece with it, the whole of it a single piece of hammered work of pure gold .
- **Exo 25:38** (—) *target: pure*
  > Exo 25:38 Its tongs and their trays shall be of pure gold .
- **Exo 25:39** (—) *target: pure*
  > Exo 25:39 It shall be made , with all these utensils , out of a talent of pure gold .
- **Exo 28:14** (—) *target: pure*
  > Exo 28:14 and two chains of pure gold , twisted like cords ; and you shall attach the corded chains to the settings .
- **Exo 28:22** (—) *target: pure*
  > Exo 28:22 You shall make for the breastpiece twisted chains like cords , of pure gold .
- **Exo 28:36** (—) *target: pure*
  > Exo 28:36 “You shall make a plate of pure gold and engrave on it, like the engraving of a signet , ‘ Holy to the Lord .’
- **Exo 30:3** (—) *target: pure*
  > Exo 30:3 You shall overlay it with pure gold , its top and around its sides and its horns . And you shall make a molding of gold around it.
- **Exo 30:35** (—) *target: pure*
  > Exo 30:35 and make an incense blended as by the perfumer , seasoned with salt , pure and holy .
- **Exo 31:8** (—) *target: pure*
  > Exo 31:8 the table and its utensils , and the pure lampstand with all its utensils , and the altar of incense ,
- **Exo 37:2** (—) *target: pure*
  > Exo 37:2 And he overlaid it with pure gold inside and outside , and made a molding of gold around it.
- **Exo 37:6** (—) *target: pure*
  > Exo 37:6 And he made a mercy seat of pure gold . Two cubits and a half was its length , and a cubit and a half its breadth .
- **Exo 37:11** (—) *target: pure*
  > Exo 37:11 And he overlaid it with pure gold , and made a molding of gold around it.
- **Exo 37:16** (—) *target: pure*
  > Exo 37:16 And he made the vessels of pure gold that were to be on the table , its plates and dishes for incense, and its bowls and flagons with which to pour drink offerings .
- **Exo 37:17** (—) *target: pure*
  > Exo 37:17 He also made the lampstand of pure gold . He made the lampstand of hammered work . Its base , its stem , its cups , its calyxes , and its flowers were of one piece with it .
- **Exo 37:22** (—) *target: pure*
  > Exo 37:22 Their calyxes and their branches were of one piece with it . The whole of it was a single piece of hammered work of pure gold .
- **Exo 37:23** (—) *target: pure*
  > Exo 37:23 And he made its seven lamps and its tongs and its trays of pure gold .
- **Exo 37:24** (—) *target: pure*
  > Exo 37:24 He made it and all its utensils out of a talent of pure gold .
- **Exo 37:26** (—) *target: pure*
  > Exo 37:26 He overlaid it with pure gold , its top and around its sides and its horns . And he made a molding of gold around it,
- **Exo 37:29** (—) *target: pure*
  > Exo 37:29 He made the holy anointing oil also, and the pure fragrant incense , blended as by the perfumer .
- **Exo 39:15** (—) *target: pure*
  > Exo 39:15 And they made on the breastpiece twisted chains like cords , of pure gold .
- **Exo 39:25** (—) *target: pure*
  > Exo 39:25 They also made bells of pure gold , and put the bells between the pomegranates all around the hem of the robe , between the pomegranates —
- **Exo 39:30** (—) *target: pure*
  > Exo 39:30 They made the plate of the holy crown of pure gold , and wrote on it an inscription , like the engraving of a signet , “ Holy to the Lord .”
- **Exo 39:37** (—) *target: pure gold*
  > Exo 39:37 the lampstand of pure gold and its lamps with the lamps set and all its utensils , and the oil for the light ;
- **Job 28:19** (—) *target: pure*
  > Job 28:19 The topaz of Ethiopia cannot equal it, nor can it be valued in pure gold .

### `H2890` — 1/1 classified · 1 anchor verse(s)

**Group `6060-001`** (1 verse — anchors: Hab 1:13)

- **Hab 1:13** 🔵 (✓) *target: purer*
  > Hab 1:13 You who are of purer eyes than to see evil and cannot look at wrong , why do you idly look at traitors and remain silent when the wicked swallows up the man more righteous than he ?

### `H2891` — 71/79 classified · 3 anchor verse(s)

**Group `6057-001`** (11 verses — anchors: Psa 51:2)

- **Psa 51:2** 🔵 (✓) *target: cleanse*
  > Psa 51:2 Wash me thoroughly from my iniquity , and cleanse me from my sin !
- **Jos 22:17** (✓) *target: cleansed*
  > Jos 22:17 Have we not had enough of the sin at Peor from which even yet we have not cleansed ourselves, and for which there came a plague upon the congregation of the Lord ,
- **Psa 51:7** (✓) *target: clean*
  > Psa 51:7 Purge me with hyssop , and I shall be clean ; wash me, and I shall be whiter than snow .
- **Pro 20:9** (✓) *target: clean*
  > Pro 20:9 Who can say , “I have made my heart pure ; I am clean from my sin ”?
- **Isa 66:17** (✓) *target: purify themselves*
  > Isa 66:17 “Those who sanctify and purify themselves to go into the gardens , following one in the midst , eating pig’s flesh and the abomination and mice , shall come to an end together , declares the Lord .
- **Jer 13:27** (✓) *target: made clean*
  > Jer 13:27 I have seen your abominations , your adulteries and neighings , your lewd whorings , on the hills in the field . Woe to you, O Jerusalem ! How long will it be before you are made clean ?”
- **Jer 33:8** (✓) *target: cleanse*
  > Jer 33:8 I will cleanse them from all the guilt of their sin against me, and I will forgive all the guilt of their sin and rebellion against me .
- **Eze 24:13** (✓) *target: cleansed*
  > Eze 24:13 On account of your unclean lewdness , because I would have cleansed you and you were not cleansed from your uncleanness , you shall not be cleansed anymore till I have satisfied my fury upon you .
- **Eze 36:25** (✓) *target: clean*
  > Eze 36:25 I will sprinkle clean water on you, and you shall be clean from all your uncleannesses , and from all your idols I will cleanse you .
- **Eze 36:33** (✓) *target: cleanse*
  > Eze 36:33 “ Thus says the Lord God : On the day that I cleanse you from all your iniquities , I will cause the cities to be inhabited , and the waste places shall be rebuilt .
- **Eze 37:23** (✓) *target: cleanse*
  > Eze 37:23 They shall not defile themselves anymore with their idols and their detestable things , or with any of their transgressions . But I will save them from all the backslidings in which they have sinned , and will cleanse them; and they shall be my people , and I will be their God .

**Group `6057-002`** (43 verses — anchors: 2Ki 5:10)

- **2Ki 5:10** 🔵 (✓) *target: clean*
  > 2Ki 5:10 And Elisha sent a messenger to him, saying , “ Go and wash in the Jordan seven times , and your flesh shall be restored , and you shall be clean .”
- **Gen 35:2** (✓) *target: purify yourselves*
  > Gen 35:2 So Jacob said to his household and to all who were with him, “Put away the foreign gods that are among you and purify yourselves and change your garments .
- **Lev 11:32** (✓) *target: clean*
  > Lev 11:32 And anything on which any of them falls when they are dead shall be unclean , whether it is an article of wood or a garment or a skin or a sack , any article that is used for any purpose . It must be put into water , and it shall be unclean until the evening ; then it shall be clean .
- **Lev 12:7** (✓) *target: clean*
  > Lev 12:7 and he shall offer it before the Lord and make atonement for her. Then she shall be clean from the flow of her blood . This is the law for her who bears a child, either male or female .
- **Lev 12:8** (✓) *target: clean*
  > Lev 12:8 And if she cannot afford a lamb , then she shall take two turtledoves or two pigeons , one for a burnt offering and the other for a sin offering . And the priest shall make atonement for her, and she shall be clean .”
- **Lev 13:6** (✓) *target: clean*
  > Lev 13:6 And the priest shall examine him again on the seventh day , and if the diseased area has faded and the disease has not spread in the skin , then the priest shall pronounce him clean ; it is only an eruption . And he shall wash his clothes and be clean .
- **Lev 13:13** (✓) *target: pronounce*
  > Lev 13:13 then the priest shall look , and if the leprous disease has covered all his body , he shall pronounce him clean of the disease ; it has all turned white , and he is clean .
- **Lev 13:17** (✓) *target: clean*
  > Lev 13:17 and the priest shall examine him, and if the disease has turned white , then the priest shall pronounce the diseased person clean ; he is clean .
- **Lev 13:23** (✓) *target: clean*
  > Lev 13:23 But if the spot remains in one place and does not spread , it is the scar of the boil , and the priest shall pronounce him clean .
- **Lev 13:28** (✓) *target: clean*
  > Lev 13:28 But if the spot remains in one place and does not spread in the skin , but has faded , it is a swelling from the burn , and the priest shall pronounce him clean , for it is the scar of the burn .
- **Lev 13:34** (✓) *target: clean*
  > Lev 13:34 And on the seventh day the priest shall examine the itch , and if the itch has not spread in the skin and it appears to be no deeper than the skin , then the priest shall pronounce him clean . And he shall wash his clothes and be clean .
- **Lev 13:37** (✓) *target: clean*
  > Lev 13:37 But if in his eyes the itch is unchanged and black hair has grown in it, the itch is healed and he is clean , and the priest shall pronounce him clean .
- **Lev 13:58** (✓) *target: clean*
  > Lev 13:58 But the garment , or the warp or the woof , or any article made of skin from which the disease departs when you have washed it, shall then be washed a second time, and be clean .”
- **Lev 13:59** (✓) *target: clean*
  > Lev 13:59 This is the law for a case of leprous disease in a garment of wool or linen , either in the warp or the woof , or in any article made of skin , to determine whether it is clean or unclean .
- **Lev 14:4** (✓) *target: cleansed*
  > Lev 14:4 the priest shall command them to take for him who is to be cleansed two live clean birds and cedarwood and scarlet yarn and hyssop .
- **Lev 14:7** (✓) *target: cleansed*
  > Lev 14:7 And he shall sprinkle it seven times on him who is to be cleansed of the leprous disease . Then he shall pronounce him clean and shall let the living bird go into the open field .
- **Lev 14:8** (✓) *target: cleansed*
  > Lev 14:8 And he who is to be cleansed shall wash his clothes and shave off all his hair and bathe himself in water , and he shall be clean . And after that he may come into the camp , but live outside his tent seven days .
- **Lev 14:9** (✓) *target: clean*
  > Lev 14:9 And on the seventh day he shall shave off all his hair from his head , his beard , and his eyebrows . He shall shave off all his hair , and then he shall wash his clothes and bathe his body in water , and he shall be clean .
- **Lev 14:11** (✓) *target: cleanses*
  > Lev 14:11 And the priest who cleanses him shall set the man who is to be cleansed and these things before the Lord , at the entrance of the tent of meeting .
- **Lev 14:14** (✓) *target: cleansed*
  > Lev 14:14 The priest shall take some of the blood of the guilt offering , and the priest shall put it on the lobe of the right ear of him who is to be cleansed and on the thumb of his right hand and on the big toe of his right foot .
- **Lev 14:17** (✓) *target: cleansed*
  > Lev 14:17 And some of the oil that remains in his hand the priest shall put on the lobe of the right ear of him who is to be cleansed and on the thumb of his right hand and on the big toe of his right foot , on top of the blood of the guilt offering .
- **Lev 14:18** (✓) *target: cleansed*
  > Lev 14:18 And the rest of the oil that is in the priest’s hand he shall put on the head of him who is to be cleansed . Then the priest shall make atonement for him before the Lord .
- **Lev 14:19** (✓) *target: cleansed*
  > Lev 14:19 The priest shall offer the sin offering , to make atonement for him who is to be cleansed from his uncleanness . And afterward he shall kill the burnt offering .
- **Lev 14:20** (✓) *target: clean*
  > Lev 14:20 And the priest shall offer the burnt offering and the grain offering on the altar . Thus the priest shall make atonement for him, and he shall be clean .
- **Lev 14:25** (✓) *target: cleansed*
  > Lev 14:25 And he shall kill the lamb of the guilt offering . And the priest shall take some of the blood of the guilt offering and put it on the lobe of the right ear of him who is to be cleansed , and on the thumb of his right hand and on the big toe of his right foot .
- **Lev 14:28** (✓) *target: cleansed*
  > Lev 14:28 And the priest shall put some of the oil that is in his hand on the lobe of the right ear of him who is to be cleansed and on the thumb of his right hand and on the big toe of his right foot , in the place where the blood of the guilt offering was put.
- **Lev 14:29** (✓) *target: cleansed*
  > Lev 14:29 And the rest of the oil that is in the priest’s hand he shall put on the head of him who is to be cleansed , to make atonement for him before the Lord .
- **Lev 14:31** (✓) *target: cleansed*
  > Lev 14:31 one for a sin offering and the other for a burnt offering , along with a grain offering . And the priest shall make atonement before the Lord for him who is being cleansed .
- **Lev 14:48** (✓) *target: clean*
  > Lev 14:48 “But if the priest comes and looks , and if the disease has not spread in the house after the house was plastered , then the priest shall pronounce the house clean , for the disease is healed .
- **Lev 14:53** (✓) *target: clean*
  > Lev 14:53 And he shall let the live bird go out of the city into the open country . So he shall make atonement for the house , and it shall be clean .”
- **Lev 15:13** (✓) *target: cleansed*
  > Lev 15:13 “And when the one with a discharge is cleansed of his discharge , then he shall count for himself seven days for his cleansing , and wash his clothes . And he shall bathe his body in fresh water and shall be clean .
- **Lev 15:28** (✓) *target: cleansed*
  > Lev 15:28 But if she is cleansed of her discharge , she shall count for herself seven days , and after that she shall be clean .
- **Lev 16:19** (✓) *target: cleanse*
  > Lev 16:19 And he shall sprinkle some of the blood on it with his finger seven times , and cleanse it and consecrate it from the uncleannesses of the people of Israel .
- **Lev 16:30** (✓) *target: cleanse*
  > Lev 16:30 For on this day shall atonement be made for you to cleanse you. You shall be clean before the Lord from all your sins .
- **Lev 17:15** (✓) *target: clean*
  > Lev 17:15 And every person who eats what dies of itself or what is torn by beasts, whether he is a native or a sojourner , shall wash his clothes and bathe himself in water and be unclean until the evening ; then he shall be clean .
- **Lev 22:4** (✓) *target: clean*
  > Lev 22:4 None of the offspring of Aaron who has a leprous disease or a discharge may eat of the holy things until he is clean . Whoever touches anything that is unclean through contact with the dead or a man who has had an emission of semen ,
- **Lev 22:7** (✓) *target: clean*
  > Lev 22:7 When the sun goes down he shall be clean , and afterward he may eat of the holy things , because they are his food .
- **Num 19:12** (✓) *target: clean*
  > Num 19:12 He shall cleanse himself with the water on the third day and on the seventh day , and so be clean . But if he does not cleanse himself on the third day and on the seventh day , he will not become clean .
- **Num 19:19** (✓) *target: clean*
  > Num 19:19 And the clean person shall sprinkle it on the unclean on the third day and on the seventh day . Thus on the seventh day he shall cleanse him, and he shall wash his clothes and bathe himself in water , and at evening he shall be clean .
- **2Ki 5:12** (✓) *target: clean*
  > 2Ki 5:12 Are not Abana and Pharpar , the rivers of Damascus , better than all the waters of Israel ? Could I not wash in them and be clean ?” So he turned and went away in a rage .
- **2Ki 5:13** (✓) *target: clean*
  > 2Ki 5:13 But his servants came near and said to him, “My father , it is a great word the prophet has spoken to you; will you not do it ? Has he actually said to you, ‘ Wash , and be clean ’?”
- **2Ki 5:14** (✓) *target: clean*
  > 2Ki 5:14 So he went down and dipped himself seven times in the Jordan , according to the word of the man of God , and his flesh was restored like the flesh of a little child , and he was clean .
- **Ezr 6:20** (✓) *target: purified*
  > Ezr 6:20 For the priests and the Levites had purified themselves together ; all of them were clean . So they slaughtered the Passover lamb for all the returned exiles , for their fellow priests , and for themselves .

**Group `6057-003`** (17 verses — anchors: Mal 3:3)

- **Mal 3:3** 🔵 (✓) *target: purifier*
  > Mal 3:3 He will sit as a refiner and purifier of silver , and he will purify the sons of Levi and refine them like gold and silver , and they will bring offerings in righteousness to the Lord .
- **Num 8:6** (✓) *target: cleanse*
  > Num 8:6 “ Take the Levites from among the people of Israel and cleanse them .
- **Num 8:7** (✓) *target: cleanse*
  > Num 8:7 Thus you shall do to them to cleanse them: sprinkle the water of purification upon them, and let them go with a razor over all their body , and wash their clothes and cleanse themselves.
- **Num 8:15** (✓) *target: cleansed*
  > Num 8:15 And after that the Levites shall go in to serve at the tent of meeting , when you have cleansed them and offered them as a wave offering .
- **Num 8:21** (✓) *target: cleanse*
  > Num 8:21 And the Levites purified themselves from sin and washed their clothes , and Aaron offered them as a wave offering before the Lord , and Aaron made atonement for them to cleanse them .
- **2Ch 29:15** (✓) *target: cleanse*
  > 2Ch 29:15 They gathered their brothers and consecrated themselves and went in as the king had commanded , by the words of the Lord , to cleanse the house of the Lord .
- **2Ch 29:16** (✓) *target: cleanse*
  > 2Ch 29:16 The priests went into the inner part of the house of the Lord to cleanse it, and they brought out all the uncleanness that they found in the temple of the Lord into the court of the house of the Lord . And the Levites took it and carried it out to the brook Kidron .
- **2Ch 29:18** (✓) *target: cleansed*
  > 2Ch 29:18 Then they went in to Hezekiah the king and said , “We have cleansed all the house of the Lord , the altar of burnt offering and all its utensils , and the table for the showbread and all its utensils .
- **2Ch 30:18** (✓) *target: cleansed*
  > 2Ch 30:18 For a majority of the people , many of them from Ephraim , Manasseh , Issachar , and Zebulun , had not cleansed themselves, yet they ate the Passover otherwise than as prescribed . For Hezekiah had prayed for them, saying , “ May the good Lord pardon everyone
- **2Ch 34:3** (✓) *target: purge*
  > 2Ch 34:3 For in the eighth year of his reign , while he was yet a boy , he began to seek the God of David his father , and in the twelfth year he began to purge Judah and Jerusalem of the high places , the Asherim , and the carved and the metal images .
- **2Ch 34:5** (✓) *target: cleansed*
  > 2Ch 34:5 He also burned the bones of the priests on their altars and cleansed Judah and Jerusalem .
- **2Ch 34:8** (✓) *target: cleansed*
  > 2Ch 34:8 Now in the eighteenth year of his reign , when he had cleansed the land and the house , he sent Shaphan the son of Azaliah , and Maaseiah the governor of the city , and Joah the son of Joahaz , the recorder , to repair the house of the Lord his God .
- **Neh 12:30** (✓) *target: purified*
  > Neh 12:30 And the priests and the Levites purified themselves, and they purified the people and the gates and the wall .
- **Neh 13:9** (✓) *target: cleansed*
  > Neh 13:9 Then I gave orders , and they cleansed the chambers , and I brought back there the vessels of the house of God , with the grain offering and the frankincense .
- **Neh 13:22** (✓) *target: purify themselves*
  > Neh 13:22 Then I commanded the Levites that they should purify themselves and come and guard the gates , to keep the Sabbath day holy . Remember this also in my favor, O my God , and spare me according to the greatness of your steadfast love .
- **Neh 13:30** (✓) *target: cleansed*
  > Neh 13:30 Thus I cleansed them from everything foreign , and I established the duties of the priests and Levites , each in his work ;
- **Job 4:17** (✓) *target: pure*
  > Job 4:17 ‘Can mortal man be in the right before God ? Can a man be pure before his Maker ?

**Group `UNCLASSIFIED`** (8 verses)

- **Num 31:23** (—) *target: clean*
  > Num 31:23 everything that can stand the fire , you shall pass through the fire , and it shall be clean . Nevertheless , it shall also be purified with the water for impurity . And whatever cannot stand the fire , you shall pass through the water .
- **Num 31:24** (—) *target: clean*
  > Num 31:24 You must wash your clothes on the seventh day , and you shall be clean . And afterward you may come into the camp .”
- **Job 37:21** (—) *target: cleared*
  > Job 37:21 “And now no one looks on the light when it is bright in the skies , when the wind has passed and cleared them .
- **Eze 22:24** (—) *target: cleansed*
  > Eze 22:24 “ Son of man , say to her, You are a land that is not cleansed or rained upon in the day of indignation .
- **Eze 39:12** (—) *target: cleanse*
  > Eze 39:12 For seven months the house of Israel will be burying them, in order to cleanse the land .
- **Eze 39:14** (—) *target: cleanse*
  > Eze 39:14 They will set apart men to travel through the land regularly and bury those travelers remaining on the face of the land , so as to cleanse it. At the end of seven months they will make their search .
- **Eze 39:16** (—) *target: cleanse*
  > Eze 39:16 ( Hamonah is also the name of the city .) Thus shall they cleanse the land .
- **Eze 43:26** (—) *target: cleanse*
  > Eze 43:26 Seven days shall they make atonement for the altar and cleanse it, and so consecrate it.

### `H2892A` — 3/4 classified · 1 anchor verse(s)

**Group `6059-001`** (3 verses — anchors: Lev 12:4)

- **Lev 12:4** 🔵 (✓) *target: purifying*
  > Lev 12:4 Then she shall continue for thirty-three days in the blood of her purifying . She shall not touch anything holy , nor come into the sanctuary , until the days of her purifying are completed .
- **Lev 12:5** (✓) *target: purifying*
  > Lev 12:5 But if she bears a female child , then she shall be unclean two weeks , as in her menstruation . And she shall continue in the blood of her purifying for sixty-six days .
- **Lev 12:6** (✓) *target: purifying*
  > Lev 12:6 “And when the days of her purifying are completed , whether for a son or for a daughter , she shall bring to the priest at the entrance of the tent of meeting a lamb a year old for a burnt offering , and a pigeon or a turtledove for a sin offering ,

**Group `UNCLASSIFIED`** (1 verse)

- **Exo 24:10** (—) *target: clearness*
  > Exo 24:10 and they saw the God of Israel . There was under his feet as it were a pavement of sapphire stone , like the very heaven for clearness .

### `H2892B` — 3/4 classified · 1 anchor verse(s)

**Group `6061-001`** (3 verses — anchors: Lev 12:4)

- **Lev 12:4** 🔵 (✓) *target: purifying*
  > Lev 12:4 Then she shall continue for thirty-three days in the blood of her purifying . She shall not touch anything holy , nor come into the sanctuary , until the days of her purifying are completed .
- **Lev 12:5** (✓) *target: purifying*
  > Lev 12:5 But if she bears a female child , then she shall be unclean two weeks , as in her menstruation . And she shall continue in the blood of her purifying for sixty-six days .
- **Lev 12:6** (✓) *target: purifying*
  > Lev 12:6 “And when the days of her purifying are completed , whether for a son or for a daughter , she shall bring to the priest at the entrance of the tent of meeting a lamb a year old for a burnt offering , and a pigeon or a turtledove for a sin offering ,

**Group `UNCLASSIFIED`** (1 verse)

- **Exo 24:10** (—) *target: clearness*
  > Exo 24:10 and they saw the God of Israel . There was under his feet as it were a pavement of sapphire stone , like the very heaven for clearness .

### `H2893` — 11/11 classified · 2 anchor verse(s)

**Group `6058-001`** (8 verses — anchors: Lev 14:2)

- **Lev 14:2** 🔵 (✓) *target: cleansing*
  > Lev 14:2 “This shall be the law of the leprous person for the day of his cleansing . He shall be brought to the priest ,
- **Lev 13:7** (✓) *target: cleansing*
  > Lev 13:7 But if the eruption spreads in the skin , after he has shown himself to the priest for his cleansing , he shall appear again before the priest .
- **Lev 13:35** (✓) *target: cleansing*
  > Lev 13:35 But if the itch spreads in the skin after his cleansing ,
- **Lev 14:23** (✓) *target: cleansing*
  > Lev 14:23 And on the eighth day he shall bring them for his cleansing to the priest , to the entrance of the tent of meeting , before the Lord .
- **Lev 14:32** (✓) *target: cleansing*
  > Lev 14:32 This is the law for him in whom is a case of leprous disease , who cannot afford the offerings for his cleansing .”
- **Lev 15:13** (✓) *target: cleansing*
  > Lev 15:13 “And when the one with a discharge is cleansed of his discharge , then he shall count for himself seven days for his cleansing , and wash his clothes . And he shall bathe his body in fresh water and shall be clean .
- **Num 6:9** (✓) *target: cleansing*
  > Num 6:9 “And if any man dies very suddenly beside him and he defiles his consecrated head , then he shall shave his head on the day of his cleansing ; on the seventh day he shall shave it .
- **Eze 44:26** (✓) *target: become clean*
  > Eze 44:26 After he has become clean , they shall count seven days for him .

**Group `6058-002`** (3 verses — anchors: 2Ch 30:19)

- **2Ch 30:19** 🔵 (✓) *target: cleanness*
  > 2Ch 30:19 who sets his heart to seek God , the Lord , the God of his fathers , even though not according to the sanctuary’s rules of cleanness .”
- **1Ch 23:28** (✓) *target: cleansing*
  > 1Ch 23:28 For their duty was to assist the sons of Aaron for the service of the house of the Lord , having the care of the courts and the chambers , the cleansing of all that is holy , and any work for the service of the house of God .
- **Neh 12:45** (✓) *target: purification*
  > Neh 12:45 And they performed the service of their God and the service of purification , as did the singers and the gatekeepers , according to the command of David and his son Solomon .

### `G0047` — 2/2 classified · 1 anchor verse(s)

**Group `1062-001`** (2 verses — anchors: 1Ti 4:12)

- **1Ti 4:12** 🔵 (✓) *target: purity*
  > 1Ti 4:12 Let no one despise you for your youth , but set the believers an example in speech , in conduct , in love , in faith , in purity .
- **1Ti 5:2** (✓) *target: purity*
  > 1Ti 5:2 older women as mothers , younger women as sisters , in all purity .

### `G0048` — 7/7 classified · 2 anchor verse(s)

**Group `6054-001`** (3 verses — anchors: 1Jo 3:3)

- **1Jo 3:3** 🔵 (✓) *target: purifies*
  > 1Jo 3:3 And everyone who thus hopes in him purifies himself as he is pure .
- **Jam 4:8** (✓) *target: purify*
  > Jam 4:8 Draw near to God , and he will draw near to you . Cleanse your hands , you sinners , and purify your hearts , you double-minded .
- **1Pe 1:22** (✓) *target: purified*
  > 1Pe 1:22 Having purified your souls by your obedience to the truth for a sincere brotherly love, love one another earnestly from a pure heart ,

**Group `6054-002`** (4 verses — anchors: Act 21:26)

- **Act 21:26** 🔵 (✓) *target: purified himself*
  > Act 21:26 Then Paul took the men , and the next day he purified himself along with them and went into the temple , giving notice when the days of purification would be fulfilled and the offering presented for each one of them .
- **Joh 11:55** (✓) *target: purify*
  > Joh 11:55 Now the Passover of the Jews was at hand , and many went up from the country to Jerusalem before the Passover to purify themselves .
- **Act 21:24** (✓) *target: purify yourself*
  > Act 21:24 take these men and purify yourself along with them and pay their expenses , so that they may shave their heads . Thus all will know that there is nothing in what they have been told about you , but that you yourself also live in observance of the law .
- **Act 24:18** (✓) *target: purified*
  > Act 24:18 While I was doing this, they found me purified in the temple , without any crowd or tumult . But some Jews from Asia —

### `G0049` — 1/1 classified · 1 anchor verse(s)

**Group `6055-001`** (1 verse — anchors: Act 21:26)

- **Act 21:26** 🔵 (✓) *target: purification*
  > Act 21:26 Then Paul took the men , and the next day he purified himself along with them and went into the temple , giving notice when the days of purification would be fulfilled and the offering presented for each one of them .

### `G0053` — 8/8 classified · 2 anchor verse(s)

**Group `6053-001`** (5 verses — anchors: Jam 3:17)

- **Jam 3:17** 🔵 (✓) *target: pure*
  > Jam 3:17 But the wisdom from above is first pure , then peaceable , gentle , open to reason , full of mercy and good fruits , impartial and sincere .
- **2Cor 7:11** (✓) *target: innocent*
  > 2Cor 7:11 For see what earnestness this godly grief has produced in you , but also what eagerness to clear yourselves, what indignation , what fear , what longing , what zeal , what punishment ! At every point you have proved yourselves innocent in the matter .
- **Phili 4:8** (✓) *target: pure*
  > Phili 4:8 Finally , brothers , whatever is true , whatever is honorable , whatever is just , whatever is pure , whatever is lovely , whatever is commendable , if there is any excellence , if there is anything worthy of praise , think about these things .
- **1Ti 5:22** (✓) *target: pure*
  > 1Ti 5:22 Do not be hasty in the laying on of hands , nor take part in the sins of others ; keep yourself pure .
- **1Jo 3:3** (✓) *target: pure*
  > 1Jo 3:3 And everyone who thus hopes in him purifies himself as he is pure .

**Group `6053-002`** (3 verses — anchors: 2Cor 11:2)

- **2Cor 11:2** 🔵 (✓) *target: pure*
  > 2Cor 11:2 For I feel a divine jealousy for you , since I betrothed you to one husband , to present you as a pure virgin to Christ .
- **Tit 2:5** (✓) *target: pure*
  > Tit 2:5 to be self-controlled , pure , working at home , kind , and submissive to their own husbands , that the word of God may not be reviled .
- **1Pe 3:2** (✓) *target: pure*
  > 1Pe 3:2 when they see your respectful and pure conduct .

### `G0054` — 1/1 classified · 1 anchor verse(s)

**Group `1064-001`** (1 verse — anchors: 2Cor 6:6)

- **2Cor 6:6** 🔵 (✓) *target: purity*
  > 2Cor 6:6 by purity , knowledge , patience , kindness , the Holy Spirit , genuine love ;

### `G0055` — 1/1 classified · 1 anchor verse(s)

**Group `6056-001`** (1 verse — anchors: Phili 1:17)

- **Phili 1:17** 🔵 (✓) *target: sincerely*
  > Phili 1:17 The former proclaim Christ out of selfish ambition , not sincerely but thinking to afflict me in my imprisonment .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**12 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H2889` | pure | `not_done` | 87 | 4 | 58 |
| `H2890` | pureness | `not_done` | 1 | 1 | 1 |
| `H2891` | be pure | `not_done` | 79 | 3 | 71 |
| `H2892A` | purity | `not_done` | 4 | 1 | 3 |
| `H2892B` | clearness | `not_done` | 4 | 1 | 3 |
| `H2893` | purifying | `not_done` | 11 | 2 | 11 |
| `G0047` | purity | `not_done` | 2 | 1 | 2 |
| `G0048` | to purify | `not_done` | 7 | 2 | 7 |
| `G0049` | purification | `not_done` | 1 | 1 | 1 |
| `G0053` | pure | `not_done` | 8 | 2 | 8 |
| `G0054` | purity | `not_done` | 1 | 1 | 1 |
| `G0055` | purely | `not_done` | 1 | 1 | 1 |

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

### Registry-specific extensions for R125 purity

_None._ No active non-tiered extensions in `wa_obs_question_catalogue` are sourced from registry 125 (purity).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-02T15:24:55Z`
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

*End of readiness output v3 — wa-125-purity.*