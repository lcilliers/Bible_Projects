# wa-168-uprightness — Analysis Readiness Output (v6)

_v6 generation · 2026-05-02T15:25:03Z · schema 3.17.0 · catalogue v2-2026-04-29 (T0–T7)_

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

- **Registry no:** `168` · **word:** `uprightness`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `wa-dimensionreview-instruction-v3_3-20260418`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 11  (programme-wide aggregate including XREF and historical terms — current OWNER count is 8, XREF 2)
- `phase1_verse_count`: 232  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 0 unresolved · **Existing session_b_findings:** 1

**Description:**

> Uprightness is the quality of the person who is straight — morally and relationally aligned with what is true and right, without the crooked turns of duplicity or self-interest. The Hebrew vocabulary covers the plain, the level, the path that does not deviate. Uprightness is related to integrity and righteousness but has a particular flavour: it is the quality of the person who goes straight, who does not take the roundabout path of manipulation or self-deception. The upright person is one in whose inner and outer life there is no hidden bend.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-02T15:25:03Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 8
- **OWNER terms legacy-VC (not_done):** 8 / 8

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 8 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H3476` | yo.sher | uprightness | H | `extracted` | **`not_done`** | 1 | 14 | 3/0 | 12/0 | 3 |
| `H3477G` | ya.shar | upright:right | H | `extracted` | **`not_done`** | 1 | 113 | 6/0 | 107/0 | 6 |
| `H3483` | ye.sha.rah | uprightness | H | `extracted_thin` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H4339` | me.shar | uprightness | H | `extracted` | **`not_done`** | 1 | 19 | 2/0 | 16/0 | 2 |
| `H5227` | no.khach | before | H | `extracted` | **`not_done`** | 1 | 24 | 3/0 | 7/0 | 3 |
| `H5228` | na.kho.ach | straightforward | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 4/0 | 1 |
| `H5229` | ne.kho.chah | upright | H | `extracted` | **`not_done`** | 1 | 4 | 1/0 | 4/0 | 1 |
| `G2118` | euthutēs | righteousness | G | `extracted_thin` | **`not_done`** | 1 | 1 | 1/0 | 1/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H3476` — yo.sher "uprightness"

**Identity:** mti=1211 · ti=1333 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-18T14:05:53): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: straightness, uprightness

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): straightness, evenness (moral implications)
  - `1b` (under `None`): rightness, uprightness
  - `1c` (under `None`): what is right, what is due

**Root family:**
- `YOSHER` (Hebrew): plain — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (13 total; sample of 13):**
- `H3474` ya.shar "to smooth"
- `H3475` ye.sher "Jesher"
- `H3477G` ya.shar "upright:right"
- `H3477H` ya.shar "Jashar"
- `H3477I` ya.shar "upright:straight"
- `H3483` ye.sha.rah "uprightness"
- `H3484` ye.shu.run "Jeshurun"
- `H4334` mi.shor "plain"
- `H4339` me.shar "uprightness"
- `H8289G` sha.ron "Lasharon"
- `H8289H` sha.ron "Sharon"
- `H8289I` sha.ron "Sharon"
- `H8290` sha.ro.ni "Sharonite"

### `H3477G` — ya.shar "upright:right"

**Identity:** mti=1216 · ti=1338 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-18T14:05:53): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: straight, upright, correct, right

Sub-senses (depth > 1): 5 entries — present in DB; first 15:
  - `1a` (under `None`): straight, level
  - `1b` (under `None`): right, pleasing, correct
  - `1c` (under `None`): straightforward, just, upright, fitting, proper
  - `1d` (under `None`): uprightness, righteous, upright
  - `1e` (under `None`): that which is upright (subst) Also means: ya.shar (יָשָׁר "upright" H3477I)

**Root family:**
- `YOSHER` (Hebrew): plain — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (13 total; sample of 13):**
- `H3474` ya.shar "to smooth"
- `H3475` ye.sher "Jesher"
- `H3476` yo.sher "uprightness"
- `H3477H` ya.shar "Jashar"
- `H3477I` ya.shar "upright:straight"
- `H3483` ye.sha.rah "uprightness"
- `H3484` ye.shu.run "Jeshurun"
- `H4334` mi.shor "plain"
- `H4339` me.shar "uprightness"
- `H8289G` sha.ron "Lasharon"
- `H8289H` sha.ron "Sharon"
- `H8289I` sha.ron "Sharon"
- `H8290` sha.ro.ni "Sharonite"

### `H3483` — ye.sha.rah "uprightness"

**Identity:** mti=1215 · ti=1337 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-18T14:05:53): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: uprightness

**Root family:**
- `YOSHER` (Hebrew): plain — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (13 total; sample of 13):**
- `H3474` ya.shar "to smooth"
- `H3475` ye.sher "Jesher"
- `H3476` yo.sher "uprightness"
- `H3477G` ya.shar "upright:right"
- `H3477H` ya.shar "Jashar"
- `H3477I` ya.shar "upright:straight"
- `H3484` ye.shu.run "Jeshurun"
- `H4334` mi.shor "plain"
- `H4339` me.shar "uprightness"
- `H8289G` sha.ron "Lasharon"
- `H8289H` sha.ron "Sharon"
- `H8289I` sha.ron "Sharon"
- `H8290` sha.ro.ni "Sharonite"

### `H4339` — me.shar "uprightness"

**Identity:** mti=1212 · ti=1334 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-18T14:05:53): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: evenness, uprightness, straightness, equity

Sub-senses (depth > 1): 3 entries — present in DB; first 15:
  - `1a` (under `None`): evenness, level, smoothness
  - `1b` (under `None`): uprightness, equity
  - `1c` (under `None`): rightly (as adv)

**Root family:**
- `YOSHER` (Hebrew): plain — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (13 total; sample of 13):**
- `H3474` ya.shar "to smooth"
- `H3475` ye.sher "Jesher"
- `H3476` yo.sher "uprightness"
- `H3477G` ya.shar "upright:right"
- `H3477H` ya.shar "Jashar"
- `H3477I` ya.shar "upright:straight"
- `H3483` ye.sha.rah "uprightness"
- `H3484` ye.shu.run "Jeshurun"
- `H4334` mi.shor "plain"
- `H8289G` sha.ron "Lasharon"
- `H8289H` sha.ron "Sharon"
- `H8289I` sha.ron "Sharon"
- `H8290` sha.ro.ni "Sharonite"

### `H5227` — no.khach "before"

**Identity:** mti=7492 · ti=7546 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse:** _no parsed meaning row found in `wa_meaning_parsed` for this term._ Lexical work proceeds from gloss + group descriptions + verse evidence.

**Root family:**
- `NOKHACH` (Hebrew): before — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `H5228` na.kho.ach "straightforward"
- `H5229` ne.kho.chah "upright"

### `H5228` — na.kho.ach "straightforward"

**Identity:** mti=1217 · ti=1340 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-18T14:05:53): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: straight, right, straightness, be in front of

**Root family:**
- `NOKHACH` (Hebrew): before — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `H5227` no.khach "before"
- `H5229` ne.kho.chah "upright"

### `H5229` — ne.kho.chah "upright"

**Identity:** mti=1214 · ti=1336 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-18T14:05:53): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: straight in front, be in front of, straight, right, straightness

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): true things (of prophecy)
  - `1b` (under `None`): rectitude (subst)

**Root family:**
- `NOKHACH` (Hebrew): before — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `H5227` no.khach "before"
- `H5228` na.kho.ach "straightforward"

### `G2118` — euthutēs "righteousness"

**Identity:** mti=1218 · ti=1341 · language=Greek · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-19T17:05:06): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: righteousness, uprightness, a figurative extension of a straight (not crooked) object, not found in the NT 
righteousness, uprightness, equity, Heb. 1:8*

**Root family:**
- `EUTHU` (Greek): righteousness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G2117` euthus "Straight"

**LSJ (Greek lexicon):**
- gloss: εὐθύτης [ῠ], ητος, ἡ, 
(εὐθύς) straightness, opposed to καμπυλότης, [Refs 4th c.BC+]; opposed to περιφέρεια, [Refs]; εὐ
- domains: ["Refs", "Refs", "LXX"]

---

## E. XREF Terms [Unit 2] (2)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `H3474` | ya.shar | to smooth | H | 98 justice | `extracted_thin` | 25 |
| `H3477I` | ya.shar | upright:straight | H | 98 justice | `extracted_thin` | 4 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H3476` — 3 groups

- **`1211-001`** — 5 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness as an inner quality of the heart — tested by God, contrasted with wickedness, invoked as protection*
- **`1211-002`** — 5 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness as the path/way — inner orientation expressed in the direction of life*
- **`1211-003`** — 2 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness expressed in speech — words as disclosure of inner integrity*

### `H3477G` — 6 groups

- **`1216-001`** — 37 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Regnal moral assessment — "did right/what was right in the eyes of the Lord" — moral orientation of the will under divine evaluation*
- **`1216-002`** — 8 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C10`
  - *"Right in his own eyes" — moral self-determination; inner conscience as its own arbiter*
- **`1216-003`** — 46 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *"The upright" / "upright in heart" — uprightness as stable inner moral character, especially in Psalms and Proverbs*
- **`1216-004`** — 6 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness as divine character — God and his word described as upright/right*
- **`1216-005`** — 9 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Job as the upright man — blameless and upright as defining inner character under testing*
- **`1216-006`** — 1 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *"God made man upright, but they have sought out many schemes" — original moral constitution and its departure*

### `H3483` — 1 groups

- **`1215-001`** — 1 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Uprightness of heart directed toward God — inner moral orientation of relational fidelity*

### `H4339` — 2 groups

- **`1212-001`** — 8 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness as the standard and quality of right judgment — divine and demanded of human authorities*
- **`1212-002`** — 8 relevant · 1 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C10`
  - *Uprightness as inner character formation — wisdom's goal; the inmost being rejoices at rightness*

### `H5227` — 3 groups

- **`7492-001`** — 3 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *"Before the face/presence of the Lord" — relational orientation of prayer, lament, and honest speech toward God*
- **`7492-002`** — 3 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C10`
  - *"Before their faces" — the stumbling block of iniquity as the primary object of inner attention (Ezekiel)*
- **`7492-003`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *"Directly forward" — inner directedness; focused and undistracted attention*

### `H5228` — 1 groups

- **`1217-001`** — 4 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Straightforwardness as honest inner character — rightness of speech, claims, and conduct*

### `H5229` — 1 groups

- **`1214-001`** — 4 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness resisted, absent, or refused — the inner being's failure to receive or produce what is right*

### `G2118` — 1 groups

- **`1218-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Uprightness as the defining moral character of Christ's kingship — inner quality expressed in sovereign rule*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 98 justice | 5 | `H3476,H4339,H3483,H3477G,G2118` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 183 heart | 20 |
| 98 justice | 19 |
| 77 honesty | 18 |
| 90 innocence | 15 |
| 67 goodness | 13 |
| 112 mind | 12 |
| 172 wickedness | 12 |
| 97 joy | 10 |
| 103 love | 10 |
| 43 desire | 9 |
| 59 faith | 8 |
| 128 rebellion | 8 |
| 73 guilt | 7 |
| 197 authority | 7 |
| 44 despair | 5 |
| 89 iniquity | 5 |
| 91 insight | 5 |
| 100 knowledge | 5 |
| 140 seeking | 5 |
| 186 gladness | 5 |
| 11 awe | 4 |
| 120 perverseness | 4 |
| 174 wisdom | 4 |
| 182 Soul | 4 |
| 210 deadness | 4 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 11 awe | Job 1:1 |
| 24 condemnation | Deu 32:4 |
| 26 conscience | Pro 23:16 |
| 42 delight | 1Ch 29:17 |
| 90 innocence | Job 1:1 |
| 92 integrity | Deu 32:4 |
| 112 mind | Ecc 7:29 |
| 120 perverseness | Pro 14:2 |
| 183 heart | 1Ch 29:17 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-168-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> Group 1216-006 (ya.shar — 'God made man upright, but they have sought out many schemes', Eccl. 7:29) is the only group in C10 explicitly addressing the original moral constitution of the human person and its departure. Session B should treat this as a significant anthropological statement and examine its implications for understanding uprightness as a creational category within the inner-being framework.

**Anchor verses cited:** Eccl 7:29

### H.2 Open SD pointers + research flags (0)

_None._
---

## I. Thin-Evidence Phase2 Flags [Unit 8]

_No phase2 flags on any OWNER term._

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H3476` — 12/14 classified · 3 anchor verse(s)

**Group `1211-001`** (5 verses — anchors: 1Ch 29:17)

- **1Ch 29:17** 🔵 (✓) *target: uprightness*
  > 1Ch 29:17 I know , my God , that you test the heart and have pleasure in uprightness . In the uprightness of my heart I have freely offered all these things , and now I have seen your people , who are present here, offering freely and joyously to you .
- **Deu 9:5** (✓) *target: uprightness*
  > Deu 9:5 Not because of your righteousness or the uprightness of your heart are you going in to possess their land , but because of the wickedness of these nations the Lord your God is driving them out from before you, and that he may confirm the word that the Lord swore to your fathers , to Abraham , to Isaac , and to Jacob .
- **1Ki 9:4** (✓) *target: uprightness*
  > 1Ki 9:4 And as for you , if you will walk before me, as David your father walked , with integrity of heart and uprightness , doing according to all that I have commanded you, and keeping my statutes and my rules ,
- **Psa 25:21** (✓) *target: uprightness*
  > Psa 25:21 May integrity and uprightness preserve me, for I wait for you ^ .
- **Psa 119:7** (✓) *target: upright*
  > Psa 119:7 I will praise you with an upright heart , when I learn your righteous rules .

**Group `1211-002`** (5 verses — anchors: Pro 14:2)

- **Pro 14:2** 🔵 (✓) *target: uprightness*
  > Pro 14:2 Whoever walks in uprightness fears the Lord , but he who is devious in his ways despises him .
- **Pro 2:13** (✓) *target: uprightness*
  > Pro 2:13 who forsake the paths of uprightness to walk in the ways of darkness ,
- **Pro 4:11** (✓) *target: uprightness*
  > Pro 4:11 I have taught you the way of wisdom ; I have led you in the paths of uprightness .
- **Pro 17:26** (✓) *target: uprightness*
  > Pro 17:26 To impose a fine on a righteous man is not good , nor to strike the noble for their uprightness .
- **Ecc 12:10** (✓) *target: uprightly*
  > Ecc 12:10 The Preacher sought to find words of delight , and uprightly he wrote words of truth .

**Group `1211-003`** (2 verses — anchors: Job 33:3)

- **Job 33:3** 🔵 (✓) *target: uprightness*
  > Job 33:3 My words declare the uprightness of my heart , and what my lips know they speak sincerely .
- **Job 6:25** (✓) *target: upright*
  > Job 6:25 How forceful are upright words ! But what does reproof from you reprove ?

**Group `UNCLASSIFIED`** (2 verses)

- **Job 33:23** (—) *target: right*
  > Job 33:23 If there be for him an angel , a mediator , one of the thousand , to declare to man what is right for him,
- **Pro 11:24** (—) *target: give*
  > Pro 11:24 One gives freely, yet grows all the richer ; another withholds what he should give , and only suffers want .

### `H3477G` — 107/113 classified · 6 anchor verse(s)

**Group `1216-001`** (37 verses — anchors: 1Ki 15:5)

- **1Ki 15:5** 🔵 (✓) *target: right*
  > 1Ki 15:5 because David did what was right in the eyes of the Lord and did not turn aside from anything that he commanded him all the days of his life , except in the matter of Uriah the Hittite .
- **Exo 15:26** (✓) *target: right*
  > Exo 15:26 saying , “ If you will diligently listen to the voice of the Lord your God , and do that which is right in his eyes , and give ear to his commandments and keep all his statutes , I will put none of the diseases on you that I put on the Egyptians , for I am the Lord , your healer .”
- **Deu 6:18** (✓) *target: right*
  > Deu 6:18 And you shall do what is right and good in the sight of the Lord , that it may go well with you, and that you may go in and take possession of the good land that the Lord swore to give to your fathers
- **Deu 12:25** (✓) *target: right*
  > Deu 12:25 You shall not eat it, that all may go well with you and with your children after you, when you do what is right in the sight of the Lord .
- **Deu 12:28** (✓) *target: right*
  > Deu 12:28 Be careful to obey all these words that I command you, that it may go well with you and with your children after you forever , when you do what is good and right in the sight of the Lord your God .
- **Deu 13:18** (✓) *target: right*
  > Deu 13:18 if you obey the voice of the Lord your God , keeping all his commandments that I am commanding you today , and doing what is right in the sight of the Lord your God .
- **Deu 21:9** (✓) *target: right*
  > Deu 21:9 So you shall purge the guilt of innocent blood from your midst , when you do what is right in the sight of the Lord .
- **Jos 9:25** (✓) *target: right*
  > Jos 9:25 And now , behold , we are in your hand . Whatever seems good and right in your sight to do to us, do it.”
- **1Sa 12:23** (✓) *target: right*
  > 1Sa 12:23 Moreover , as for me , far be it from me that I should sin against the Lord by ceasing to pray for you, and I will instruct you in the good and the right way .
- **1Ki 11:33** (✓) *target: right*
  > 1Ki 11:33 because they have forsaken me and worshiped Ashtoreth the goddess of the Sidonians , Chemosh the god of Moab , and Milcom the god of the Ammonites , and they have not walked in my ways , doing what is right in my sight and keeping my statutes and my rules , as David his father did.
- **1Ki 11:38** (✓) *target: right*
  > 1Ki 11:38 And if you will listen to all that I command you, and will walk in my ways , and do what is right in my eyes by keeping my statutes and my commandments , as David my servant did , I will be with you and will build you a sure house , as I built for David , and I will give Israel to you.
- **1Ki 14:8** (✓) *target: right*
  > 1Ki 14:8 and tore the kingdom away from the house of David and gave it to you, and yet you have not been like my servant David , who kept my commandments and followed me with all his heart , doing only that which was right in my eyes ,
- **1Ki 15:11** (✓) *target: right*
  > 1Ki 15:11 And Asa did what was right in the eyes of the Lord , as David his father had done.
- **1Ki 22:43** (✓) *target: right*
  > 1Ki 22:43 He walked in all the way of Asa his father . He did not turn aside from it, doing what was right in the sight of the Lord . Yet the high places were not taken away , and the people still sacrificed and made offerings on the high places .
- **2Ki 10:15** (✓) *target: true*
  > 2Ki 10:15 And when he departed from there , he met Jehonadab the son of Rechab coming to meet him. And he greeted him and said to him, “ Is your heart true to my heart as mine is to yours ?” And Jehonadab answered , “It is .” Jehu said, “If it is , give me your hand .” So he gave him his hand . And Jehu took him up with him into the chariot .
- **2Ki 10:30** (✓) *target: right*
  > 2Ki 10:30 And the Lord said to Jehu , “ Because you have done well in carrying out what is right in my eyes , and have done to the house of Ahab according to all that was in my heart , your sons of the fourth generation shall sit on the throne of Israel .”
- **2Ki 12:2** (✓) *target: right*
  > 2Ki 12:2 And Jehoash did what was right in the eyes of the Lord all his days , because Jehoiada the priest instructed him.
- **2Ki 14:3** (✓) *target: right*
  > 2Ki 14:3 And he did what was right in the eyes of the Lord , yet not like David his father . He did in all things as Joash his father had done .
- **2Ki 15:3** (✓) *target: right*
  > 2Ki 15:3 And he did what was right in the eyes of the Lord , according to all that his father Amaziah had done .
- **2Ki 15:34** (✓) *target: right*
  > 2Ki 15:34 And he did what was right in the eyes of the Lord , according to all that his father Uzziah had done .
- **2Ki 16:2** (✓) *target: right*
  > 2Ki 16:2 Ahaz was twenty years old when he began to reign , and he reigned sixteen years in Jerusalem . And he did not do what was right in the eyes of the Lord his God , as his father David had done,
- **2Ki 18:3** (✓) *target: right*
  > 2Ki 18:3 And he did what was right in the eyes of the Lord , according to all that David his father had done .
- **2Ki 22:2** (✓) *target: right*
  > 2Ki 22:2 And he did what was right in the eyes of the Lord and walked in all the way of David his father , and he did not turn aside to the right or to the left .
- **2Ch 14:2** (✓) *target: right*
  > 2Ch 14:2 And Asa did what was good and right in the eyes of the Lord his God .
- **2Ch 20:32** (✓) *target: right*
  > 2Ch 20:32 He walked in the way of Asa his father and did not turn aside from it, doing what was right in the sight of the Lord .
- **2Ch 24:2** (✓) *target: right*
  > 2Ch 24:2 And Joash did what was right in the eyes of the Lord all the days of Jehoiada the priest .
- **2Ch 25:2** (✓) *target: right*
  > 2Ch 25:2 And he did what was right in the eyes of the Lord , yet not with a whole heart .
- **2Ch 26:4** (✓) *target: right*
  > 2Ch 26:4 And he did what was right in the eyes of the Lord , according to all that his father Amaziah had done .
- **2Ch 27:2** (✓) *target: right*
  > 2Ch 27:2 And he did what was right in the eyes of the Lord according to all that his father Uzziah had done , except he did not enter the temple of the Lord . But the people still followed corrupt practices .
- **2Ch 28:1** (✓) *target: right*
  > 2Ch 28:1 Ahaz was twenty years old when he began to reign , and he reigned sixteen years in Jerusalem . And he did not do what was right in the eyes of the Lord , as his father David had done,
- **2Ch 29:2** (✓) *target: right*
  > 2Ch 29:2 And he did what was right in the eyes of the Lord , according to all that David his father had done .
- **2Ch 31:20** (✓) *target: right*
  > 2Ch 31:20 Thus Hezekiah did throughout all Judah , and he did what was good and right and faithful before the Lord his God .
- **2Ch 34:2** (✓) *target: right*
  > 2Ch 34:2 And he did what was right in the eyes of the Lord , and walked in the ways of David his father ; and he did not turn aside to the right hand or to the left .
- **Jer 26:14** (✓) *target: right*
  > Jer 26:14 But as for me , behold , I am in your hands . Do with me as seems good and right to you .
- **Jer 34:15** (✓) *target: right*
  > Jer 34:15 You recently repented and did what was right in my eyes by proclaiming liberty , each to his neighbor , and you made a covenant before me in the house that is called by my name ,
- **Jer 40:4** (✓) *target: right*
  > Jer 40:4 Now , behold , I release you today from the chains on your hands . If it seems good to you to come with me to Babylon , come , and I will look after you well , but if it seems wrong to you to come with me to Babylon , do not come . See , the whole land is before you; go wherever you think it good and right to go .
- **Jer 40:5** (✓) *target: right*
  > Jer 40:5 If you remain , then return to Gedaliah the son of Ahikam , son of Shaphan , whom the king of Babylon appointed governor of the cities of Judah , and dwell with him among the people . Or go wherever you think it right to go .” So the captain of the guard gave him an allowance of food and a present , and let him go .

**Group `1216-002`** (8 verses — anchors: Judg 17:6)

- **Judg 17:6** 🔵 (✓) *target: right*
  > Judg 17:6 In those days there was no king in Israel . Everyone did what was right in his own eyes .
- **Deu 12:8** (✓) *target: right*
  > Deu 12:8 “You shall not do according to all that we are doing here today , everyone doing whatever is right in his own eyes ,
- **Judg 21:25** (✓) *target: right*
  > Judg 21:25 In those days there was no king in Israel . Everyone did what was right in his own eyes .
- **2Sa 19:6** (✓) *target: pleased*
  > 2Sa 19:6 because you love those who hate you and hate those who love you. For you have made it clear today that commanders and servants are nothing to you, for today I know that if Absalom were alive and all of us were dead today , then you would be pleased .
- **Pro 12:15** (✓) *target: right*
  > Pro 12:15 The way of a fool is right in his own eyes , but a wise man listens to advice .
- **Pro 14:12** (✓) *target: right*
  > Pro 14:12 There is a way that seems right to a man , but its end is the way to death .
- **Pro 16:25** (✓) *target: right*
  > Pro 16:25 There is a way that seems right to a man , but its end is the way to death .
- **Pro 21:2** (✓) *target: right*
  > Pro 21:2 Every way of a man is right in his own eyes , but the Lord weighs the heart .

**Group `1216-003`** (46 verses — anchors: Psa 7:10)

- **Psa 7:10** 🔵 (✓) *target: upright*
  > Psa 7:10 My shield is with God , who saves the upright in heart .
- **1Sa 29:6** (✓) *target: honest*
  > 1Sa 29:6 Then Achish called David and said to him, “As the Lord lives , you have been honest , and to me it seems right that you should march out and in with me in the campaign . For I have found nothing wrong in you from the day of your coming to me to this day . Nevertheless, the lords do not approve of you .
- **2Ch 29:34** (✓) *target: more upright*
  > 2Ch 29:34 But the priests were too few and could not flay all the burnt offerings , so until other priests had consecrated themselves, their brothers the Levites helped them, until the work was finished — for the Levites were more upright in heart than the priests in consecrating themselves.
- **Neh 9:13** (✓) *target: right*
  > Neh 9:13 You came down on Mount Sinai and spoke with them from heaven and gave them right rules and true laws , good statutes and commandments ,
- **Psa 11:2** (✓) *target: upright*
  > Psa 11:2 for behold , the wicked bend the bow ; they have fitted their arrow to the string to shoot in the dark at the upright in heart ;
- **Psa 11:7** (✓) *target: upright*
  > Psa 11:7 For the Lord is righteous ; he loves righteous deeds; the upright shall behold his face .
- **Psa 32:11** (✓) *target: upright*
  > Psa 32:11 Be glad in the Lord , and rejoice , O righteous , and shout for joy , all you upright in heart !
- **Psa 33:1** (✓) *target: upright*
  > Psa 33:1 Shout for joy in the Lord , O you righteous ! Praise befits the upright .
- **Psa 36:10** (✓) *target: upright*
  > Psa 36:10 Oh, continue your steadfast love to those who know you, and your righteousness to the upright of heart !
- **Psa 37:14** (✓) *target: upright*
  > Psa 37:14 The wicked draw the sword and bend their bows to bring down the poor and needy , to slay those whose way is upright ;
- **Psa 37:37** (✓) *target: upright*
  > Psa 37:37 Mark the blameless and behold the upright , for there is a future for the man of peace .
- **Psa 49:14** (✓) *target: upright*
  > Psa 49:14 Like sheep they are appointed for Sheol ; death shall be their shepherd , and the upright shall rule over them in the morning . Their form shall be consumed in Sheol , with no place to dwell .
- **Psa 64:10** (✓) *target: upright*
  > Psa 64:10 Let the righteous one rejoice in the Lord and take refuge in him! Let all the upright in heart exult !
- **Psa 94:15** (✓) *target: upright*
  > Psa 94:15 for justice will return to the righteous , and all the upright in heart will follow it.
- **Psa 97:11** (✓) *target: upright*
  > Psa 97:11 Light is sown for the righteous , and joy for the upright in heart .
- **Psa 107:42** (✓) *target: upright*
  > Psa 107:42 The upright see it and are glad , and all wickedness shuts its mouth .
- **Psa 111:1** (✓) *target: upright*
  > Psa 111:1 Praise the Lord ! I will give thanks to the Lord with my whole heart , in the company of the upright , in the congregation .
- **Psa 111:8** (✓) *target: uprightness*
  > Psa 111:8 they are established forever and ever , to be performed with faithfulness and uprightness .
- **Psa 112:2** (✓) *target: upright*
  > Psa 112:2 His offspring will be mighty in the land ; the generation of the upright will be blessed .
- **Psa 112:4** (✓) *target: upright*
  > Psa 112:4 Light dawns in the darkness for the upright ; he is gracious , merciful , and righteous .
- **Psa 125:4** (✓) *target: upright*
  > Psa 125:4 Do good , O Lord , to those who are good , and to those who are upright in their hearts !
- **Psa 140:13** (✓) *target: upright*
  > Psa 140:13 Surely the righteous shall give thanks to your name ; the upright shall dwell in your presence .
- **Pro 2:7** (✓) *target: upright*
  > Pro 2:7 he stores up sound wisdom for the upright ; he is a shield to those who walk in integrity ,
- **Pro 2:21** (✓) *target: upright*
  > Pro 2:21 For the upright will inhabit the land , and those with integrity will remain in it ,
- **Pro 3:32** (✓) *target: upright*
  > Pro 3:32 for the devious person is an abomination to the Lord , but the upright are in his confidence .
- **Pro 8:9** (✓) *target: right*
  > Pro 8:9 They are all straight to him who understands , and right to those who find knowledge .
- **Pro 11:3** (✓) *target: upright*
  > Pro 11:3 The integrity of the upright guides them, but the crookedness of the treacherous destroys them .
- **Pro 11:6** (✓) *target: upright*
  > Pro 11:6 The righteousness of the upright delivers them, but the treacherous are taken captive by their lust .
- **Pro 11:11** (✓) *target: upright*
  > Pro 11:11 By the blessing of the upright a city is exalted , but by the mouth of the wicked it is overthrown .
- **Pro 12:6** (✓) *target: upright*
  > Pro 12:6 The words of the wicked lie in wait for blood , but the mouth of the upright delivers them .
- **Pro 14:9** (✓) *target: upright*
  > Pro 14:9 Fools mock at the guilt offering , but the upright enjoy acceptance .
- **Pro 14:11** (✓) *target: upright*
  > Pro 14:11 The house of the wicked will be destroyed , but the tent of the upright will flourish .
- **Pro 15:8** (✓) *target: upright*
  > Pro 15:8 The sacrifice of the wicked is an abomination to the Lord , but the prayer of the upright is acceptable to him .
- **Pro 16:13** (✓) *target: right*
  > Pro 16:13 Righteous lips are the delight of a king , and he loves him who speaks what is right .
- **Pro 16:17** (✓) *target: upright*
  > Pro 16:17 The highway of the upright turns aside from evil ; whoever guards his way preserves his life .
- **Pro 20:11** (✓) *target: upright*
  > Pro 20:11 Even a child makes himself known by his acts , by whether his conduct is pure and upright .
- **Pro 21:8** (✓) *target: upright*
  > Pro 21:8 The way of the guilty is crooked , but the conduct of the pure is upright .
- **Pro 21:18** (✓) *target: upright*
  > Pro 21:18 The wicked is a ransom for the righteous , and the traitor for the upright .
- **Pro 21:29** (✓) *target: upright*
  > Pro 21:29 A wicked man puts on a bold face , but the upright gives thought to his ways .
- **Pro 28:10** (✓) *target: upright*
  > Pro 28:10 Whoever misleads the upright into an evil way will fall into his own pit , but the blameless will have a goodly inheritance .
- **Pro 29:10** (✓) *target: upright*
  > Pro 29:10 Bloodthirsty men hate one who is blameless and seek the life of the upright .
- **Pro 29:27** (✓) *target: straight*
  > Pro 29:27 An unjust man is an abomination to the righteous , but one whose way is straight is an abomination to the wicked .
- **Hos 14:9** (✓) *target: right*
  > Hos 14:9 Whoever is wise , let him understand these things; whoever is discerning , let him know them; for the ways of the Lord are right , and the upright walk in them, but transgressors stumble in them .
- **Mic 2:7** (✓) *target: uprightly*
  > Mic 2:7 Should this be said , O house of Jacob ? Has the Lord grown impatient ? Are these his deeds ? Do not my words do good to him who walks uprightly ?
- **Mic 7:2** (✓) *target: upright*
  > Mic 7:2 The godly has perished from the earth , and there is no one upright among mankind ; they all lie in wait for blood , and each hunts the other with a net .
- **Mic 7:4** (✓) *target: upright*
  > Mic 7:4 The best of them is like a brier , the most upright of them a thorn hedge . The day of your watchmen , of your punishment , has come ; now their confusion is at hand.

**Group `1216-004`** (6 verses — anchors: Deu 32:4)

- **Deu 32:4** 🔵 (✓) *target: upright is*
  > Deu 32:4 “The Rock , his work is perfect , for all his ways are justice . A God of faithfulness and without iniquity , just and upright is he .
- **Psa 19:8** (✓) *target: right*
  > Psa 19:8 the precepts of the Lord are right , rejoicing the heart ; the commandment of the Lord is pure , enlightening the eyes ;
- **Psa 25:8** (✓) *target: upright*
  > Psa 25:8 Good and upright is the Lord ; therefore he instructs sinners in the way .
- **Psa 33:4** (✓) *target: upright*
  > Psa 33:4 For the word of the Lord is upright , and all his work is done in faithfulness .
- **Psa 92:15** (✓) *target: upright*
  > Psa 92:15 to declare that the Lord is upright ; he is my rock , and there is no unrighteousness in him .
- **Psa 119:137** (✓) *target: right*
  > Tsadhe Psa 119:137 Righteous are you , O Lord , and right are your rules .

**Group `1216-005`** (9 verses — anchors: Job 1:1)

- **Job 1:1** 🔵 (✓) *target: upright*
  > Job 1:1 There was a man in the land of Uz whose name was Job , and that man was blameless and upright , one who feared God and turned away from evil .
- **Num 23:10** (✓) *target: upright*
  > Num 23:10 Who can count the dust of Jacob or number the fourth part of Israel ? Let me die the death of the upright , and let my end be like his !”
- **Job 1:8** (✓) *target: upright*
  > Job 1:8 And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and turns away from evil ?”
- **Job 2:3** (✓) *target: upright*
  > Job 2:3 And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and turns away from evil ? He still holds fast his integrity , although you incited me against him to destroy him without reason .”
- **Job 4:7** (✓) *target: upright*
  > Job 4:7 “ Remember : who that was innocent ever perished ? Or where were the upright cut off ?
- **Job 8:6** (✓) *target: upright*
  > Job 8:6 if you are pure and upright , surely then he will rouse himself for you and restore your rightful habitation .
- **Job 17:8** (✓) *target: upright*
  > Job 17:8 The upright are appalled at this , and the innocent stirs himself up against the godless .
- **Job 23:7** (✓) *target: upright man*
  > Job 23:7 There an upright man could argue with him, and I would be acquitted forever by my judge .
- **Job 33:27** (✓) *target: right*
  > Job 33:27 He sings before men and says : ‘I sinned and perverted what was right , and it was not repaid to me .

**Group `1216-006`** (1 verse — anchors: Ecc 7:29)

- **Ecc 7:29** 🔵 (✓) *target: upright*
  > Ecc 7:29 See , this alone I found , that God made man upright , but they have sought out many schemes .

**Group `UNCLASSIFIED`** (6 verses)

- **2Ki 10:3** (—) *target: fittest*
  > 2Ki 10:3 select the best and fittest of your master’s sons and set him on his father’s throne and fight for your master’s house .”
- **Psa 107:7** (—) *target: straight*
  > Psa 107:7 He led them by a straight way till they reached a city to dwell in .
- **Pro 15:19** (—) *target: upright*
  > Pro 15:19 The way of a sluggard is like a hedge of thorns , but the path of the upright is a level highway .
- **Isa 26:7** (—) *target: level*
  > Isa 26:7 The path of the righteous is level ; you make level the way of the righteous .
- **Eze 1:7** (—) *target: straight*
  > Eze 1:7 Their legs were straight , and the soles of their feet were like the sole of a calf’s foot . And they sparkled like burnished bronze .
- **Dan 11:17** (—) *target: agreement*
  > Dan 11:17 He shall set his face to come with the strength of his whole kingdom , and he shall bring terms of an agreement and perform them. He shall give him the daughter of women to destroy the kingdom, but it shall not stand or be to his advantage.

### `H3483` — 1/1 classified · 1 anchor verse(s)

**Group `1215-001`** (1 verse — anchors: 1Ki 3:6)

- **1Ki 3:6** 🔵 (✓) *target: uprightness*
  > 1Ki 3:6 And Solomon said , “ You have shown great and steadfast love to your servant David my father , because he walked before you in faithfulness , in righteousness , and in uprightness of heart toward you. And you have kept for him this great and steadfast love and have given him a son to sit on his throne this day .

### `H4339` — 16/19 classified · 2 anchor verse(s)

**Group `1212-001`** (8 verses — anchors: Psa 9:8)

- **Psa 9:8** 🔵 (✓) *target: uprightness*
  > Psa 9:8 and he judges the world with righteousness ; he judges the peoples with uprightness .
- **Psa 17:2** (✓) *target: right*
  > Psa 17:2 From your presence let my vindication come ! Let your eyes behold the right !
- **Psa 58:1** (✓) *target: uprightly*
  > To the choirmaster : according to Do Not Destroy . A Miktam of David . Psa 58:1 Do you indeed decree what is right , you gods ? Do you judge the children of man uprightly ?
- **Psa 75:2** (✓) *target: equity*
  > Psa 75:2 “ At the set time that I appoint I will judge with equity .
- **Psa 96:10** (✓) *target: equity*
  > Psa 96:10 Say among the nations , “The Lord reigns ! Yes , the world is established ; it shall never be moved ; he will judge the peoples with equity .”
- **Psa 98:9** (✓) *target: equity*
  > Psa 98:9 before the Lord , for he comes to judge the earth . He will judge the world with righteousness , and the peoples with equity .
- **Psa 99:4** (✓) *target: equity*
  > Psa 99:4 The King in his might loves justice . You have established equity ; you have executed justice and righteousness in Jacob .
- **Isa 45:19** (✓) *target: right*
  > Isa 45:19 I did not speak in secret , in a land of darkness ; I did not say to the offspring of Jacob , ‘ Seek me in vain .’ I the Lord speak the truth ; I declare what is right .

**Group `1212-002`** (8 verses — anchors: Pro 23:16)

- **Pro 23:16** 🔵 (✓) *target: right*
  > Pro 23:16 My inmost being will exult when your lips speak what is right .
- **1Ch 29:17** (✓) *target: uprightness*
  > 1Ch 29:17 I know , my God , that you test the heart and have pleasure in uprightness . In the uprightness of my heart I have freely offered all these things , and now I have seen your people , who are present here, offering freely and joyously to you .
- **Pro 1:3** (✓) *target: equity*
  > Pro 1:3 to receive instruction in wise dealing , in righteousness , justice , and equity ;
- **Pro 2:9** (✓) *target: equity*
  > Pro 2:9 Then you will understand righteousness and justice and equity , every good path ;
- **Pro 8:6** (✓) *target: right*
  > Pro 8:6 Hear , for I will speak noble things , and from my lips will come what is right ,
- **Song 1:4** (✓) *target: rightly*
  > Song 1:4 Draw me after you; let us run . The king has brought me into his chambers . We will exult and rejoice in you; we will extol your love more than wine ; rightly do they love you .
- **Isa 26:7** (✓) *target: level*
  > Isa 26:7 The path of the righteous is level ; you make level the way of the righteous .
- **Isa 33:15** (✓) *target: uprightly*
  > Isa 33:15 He who walks righteously and speaks uprightly , who despises the gain of oppressions , who shakes his hands , lest they hold a bribe , who stops his ears from hearing of bloodshed and shuts his eyes from looking on evil ,

**Group `UNCLASSIFIED`** (3 verses)

- **Pro 23:31** (—) *target: smoothly*
  > Pro 23:31 Do not look at wine when it is red , when it sparkles in the cup and goes down smoothly .
- **Song 7:9** (—) *target: down smoothly*
  > Song 7:9 and your mouth like the best wine . It goes down smoothly for my beloved , gliding over lips and teeth .
- **Dan 11:6** (—) *target: agreement*
  > Dan 11:6 After some years they shall make an alliance , and the daughter of the king of the south shall come to the king of the north to make an agreement . But she shall not retain the strength of her arm , and he and his arm shall not endure , but she shall be given up , and her attendants , he who fathered her, and he who supported her in those times .

### `H5227` — 7/24 classified · 3 anchor verse(s)

**Group `7492-001`** (3 verses — anchors: Lam 2:19)

- **Lam 2:19** 🔵 (✓) *target: before*
  > Lam 2:19 “ Arise , cry out in the night , at the beginning of the night watches ! Pour out your heart like water before the presence of the Lord ! Lift your hands to him for the lives of your children , who faint for hunger at the head of every street .”
- **Pro 5:21** (✓) *target: before*
  > Pro 5:21 For a man’s ways are before the eyes of the Lord , and he ponders all his paths .
- **Jer 17:16** (✓) *target: before*
  > Jer 17:16 I have not run away from being your shepherd , nor have I desired the day of sickness . You know what came out of my lips ; it was before your face .

**Group `7492-002`** (3 verses — anchors: Eze 14:3)

- **Eze 14:3** 🔵 (✓) *target: before*
  > Eze 14:3 “ Son of man , these men have taken their idols into their hearts , and set the stumbling block of their iniquity before their faces . Should I indeed let myself be consulted by them ?
- **Eze 14:4** (✓) *target: before*
  > Eze 14:4 Therefore speak to them and say to them, Thus says the Lord God : Any one of the house of Israel who takes his idols into his heart and sets the stumbling block of his iniquity before his face , and yet comes to the prophet , I the Lord will answer him as he comes with the multitude of his idols ,
- **Eze 14:7** (✓) *target: before*
  > Eze 14:7 For any one of the house of Israel , or of the strangers who sojourn in Israel , who separates himself from me , taking his idols into his heart and putting the stumbling block of his iniquity before his face , and yet comes to a prophet to consult me through him, I the Lord will answer him myself .

**Group `7492-003`** (1 verse — anchors: Pro 4:25)

- **Pro 4:25** 🔵 (✓) *target: directly forward*
  > Pro 4:25 Let your eyes look directly forward , and your gaze be straight before you .

**Group `UNCLASSIFIED`** (17 verses)

- **Gen 25:21** (—) *target: for*
  > Gen 25:21 And Isaac prayed to the Lord for his wife , because she was barren . And the Lord granted his prayer , and Rebekah his wife conceived .
- **Gen 30:38** (—) *target: front*
  > Gen 30:38 He set the sticks that he had peeled in front of the flocks in the troughs , that is, the watering places , where the flocks came to drink . And since they bred when they came to drink ,
- **Exo 14:2** (—) *target: facing*
  > Exo 14:2 “ Tell the people of Israel to turn back and encamp in front of Pi-hahiroth , between Migdol and the sea , in front of Baal-zephon ; you shall encamp facing it, by the sea .
- **Exo 26:35** (—) *target: opposite*
  > Exo 26:35 And you shall set the table outside the veil , and the lampstand on the south side of the tabernacle opposite the table , and you shall put the table on the north side .
- **Exo 40:24** (—) *target: opposite*
  > Exo 40:24 He put the lampstand in the tent of meeting , opposite the table on the south side of the tabernacle ,
- **Num 19:4** (—) *target: toward*
  > Num 19:4 And Eleazar the priest shall take some of its blood with his finger , and sprinkle some of its blood toward the front of the tent of meeting seven times .
- **Jos 15:7** (—) *target: opposite*
  > Jos 15:7 And the boundary goes up to Debir from the Valley of Achor , and so northward , turning toward Gilgal , which is opposite the ascent of Adummim , which is on the south side of the valley . And the boundary passes along to the waters of En-shemesh and ends at En-rogel .
- **Jos 18:17** (—) *target: opposite*
  > Jos 18:17 Then it bends in a northerly direction going on to En-shemesh , and from there goes to Geliloth , which is opposite the ascent of Adummim . Then it goes down to the stone of Bohan the son of Reuben ,
- **Judg 18:6** (—) *target: eye*
  > Judg 18:6 And the priest said to them, “ Go in peace . The journey on which you go is under the eye of the Lord .”
- **Judg 19:10** (—) *target: opposite*
  > Judg 19:10 But the man would not spend the night . He rose up and departed and arrived opposite Jebus (that is, Jerusalem ). He had with him a couple of saddled donkeys , and his concubine was with him .
- **Judg 20:43** (—) *target: opposite*
  > Judg 20:43 Surrounding the Benjaminites , they pursued them and trod them down from Nohah as far as opposite Gibeah on the east .
- **1Ki 20:29** (—) *target: opposite*
  > 1Ki 20:29 And they encamped opposite one another seven days . Then on the seventh day the battle was joined . And the people of Israel struck down of the Syrians 100,000 foot soldiers in one day .
- **1Ki 22:35** (—) *target: facing*
  > 1Ki 22:35 And the battle continued that day , and the king was propped up in his chariot facing the Syrians , until at evening he died . And the blood of the wound flowed into the bottom of the chariot .
- **2Ch 18:34** (—) *target: facing*
  > 2Ch 18:34 And the battle continued that day , and the king of Israel was propped up in his chariot facing the Syrians until evening . Then at sunset he died .
- **Est 5:1** (—) *target: front*
  > Est 5:1 On the third day Esther put on her royal robes and stood in the inner court of the king’s palace , in front of the king’s quarters , while the king was sitting on his royal throne inside the throne room opposite the entrance to the palace .
- **Eze 46:9** (—) *target: straight ahead*
  > Eze 46:9 “When the people of the land come before the Lord at the appointed feasts , he who enters by the north gate to worship shall go out by the south gate , and he who enters by the south gate shall go out by the north gate : no one shall return by way of the gate by which he entered , but each shall go out straight ahead .
- **Eze 47:20** (—) *target: point*
  > Eze 47:20 “On the west side , the Great Sea shall be the boundary to a point opposite Lebo-hamath . This shall be the west side .

### `H5228` — 4/4 classified · 1 anchor verse(s)

**Group `1217-001`** (4 verses — anchors: Pro 24:26)

- **Pro 24:26** 🔵 (✓) *target: honest*
  > Pro 24:26 Whoever gives an honest answer kisses the lips .
- **2Sa 15:3** (✓) *target: right*
  > 2Sa 15:3 Absalom would say to him, “ See , your claims are good and right , but there is no man designated by the king to hear you.”
- **Pro 8:9** (✓) *target: straight*
  > Pro 8:9 They are all straight to him who understands , and right to those who find knowledge .
- **Isa 57:2** (✓) *target: uprightness*
  > Isa 57:2 he enters into peace ; they rest in their beds who walk in their uprightness .

### `H5229` — 4/4 classified · 1 anchor verse(s)

**Group `1214-001`** (4 verses — anchors: Isa 30:10)

- **Isa 30:10** 🔵 (✓) *target: right*
  > Isa 30:10 who say to the seers , “Do not see ,” and to the prophets , “Do not prophesy to us what is right ; speak to us smooth things , prophesy illusions ,
- **Isa 26:10** (✓) *target: uprightness*
  > Isa 26:10 If favor is shown to the wicked , he does not learn righteousness ; in the land of uprightness he deals corruptly and does not see the majesty of the Lord .
- **Isa 59:14** (✓) *target: uprightness*
  > Isa 59:14 Justice is turned back , and righteousness stands far away ; for truth has stumbled in the public squares , and uprightness cannot enter .
- **Amo 3:10** (✓) *target: right*
  > Amo 3:10 “They do not know how to do right ,” declares the Lord , “those who store up violence and robbery in their strongholds .”

### `G2118` — 1/1 classified · 1 anchor verse(s)

**Group `1218-001`** (1 verse — anchors: Heb 1:8)

- **Heb 1:8** 🔵 (✓) *target: uprightness*
  > Heb 1:8 But of the Son he says, “ Your throne , O God , is forever and ever , the scepter of uprightness is the scepter of your kingdom .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**8 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H3476` | uprightness | `not_done` | 14 | 3 | 12 |
| `H3477G` | upright:right | `not_done` | 113 | 6 | 107 |
| `H3483` | uprightness | `not_done` | 1 | 1 | 1 |
| `H4339` | uprightness | `not_done` | 19 | 2 | 16 |
| `H5227` | before | `not_done` | 24 | 3 | 7 |
| `H5228` | straightforward | `not_done` | 4 | 1 | 4 |
| `H5229` | upright | `not_done` | 4 | 1 | 4 |
| `G2118` | righteousness | `not_done` | 1 | 1 | 1 |

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

### Registry-specific extensions for R168 uprightness

_None._ No active non-tiered extensions in `wa_obs_question_catalogue` are sourced from registry 168 (uprightness).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-02T15:25:03Z`
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

*End of readiness output v3 — wa-168-uprightness.*