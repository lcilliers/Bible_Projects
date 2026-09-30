# wa-030-contrition — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-04-27T20:05:03Z · schema 3.17.0_

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

- **Registry no:** `30` · **word:** `contrition`
- **verse_context_status:** `Complete`
- **session_b_status:** `Ready for Analysis`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v2.2-2026-04-11`)
- **cluster_assignment:** `C13`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Affective/Emotional`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 22  (programme-wide aggregate including XREF and historical terms — current OWNER count is 10, XREF 3)
- `phase1_verse_count`: 752  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 1 unresolved · **Existing session_b_findings:** 0

**Description:**

> Contrition is the genuine, deep sorrow of someone who has done wrong and knows it — not the surface shame of being caught but the interior grief of having actually caused harm or broken trust. The biblical vocabulary gives this its strongest expression in the psalms of repentance: the broken and contrite heart, the crushed spirit. Contrition is the inner precondition for genuine repentance: without it, repentance is merely a change of strategy rather than a change of heart. [Covered by repentance (#135), brokenness (#18).]

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-04-27T20:05:03Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 10
- **OWNER terms legacy-VC (not_done):** 10 / 10

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 10 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H1792` | da.kha | to crush | H | `extracted` | **`not_done`** | 1 | 18 | 3/0 | 7/11 | 3 |
| `H1793A` | dak.ka | contrite | H | `extracted` | **`not_done`** | 1 | 2 | 1/0 | 2/0 | 1 |
| `H1793B` | dak.ka | dust | H | `extracted` | **`not_done`** | 1 | 2 | 1/0 | 2/0 | 1 |
| `H1794` | da.khah | to crush | H | `extracted` | **`not_done`** | 1 | 5 | 2/0 | 4/1 | 2 |
| `H1795` | dak.kah | crushing | H | `extracted` | **`not_done`** | 1 | 1 | 0/0 | 0/1 | 0 |
| `H3795` | ka.tit | beaten | H | `extracted` | **`not_done`** | 1 | 5 | 0/0 | 0/5 | 0 |
| `H3807` | ka.tat | to crush | H | `extracted` | **`not_done`** | 1 | 17 | 1/0 | 1/16 | 1 |
| `H4386` | me.khit.tah | fragment | H | `extracted` | **`not_done`** | 1 | 1 | 0/0 | 0/1 | 0 |
| `H5222` | ne.kheh | smitten | H | `extracted` | **`not_done`** | 1 | 1 | 0/0 | 0/1 | 0 |
| `H5223` | na.kheh | crippled | H | `extracted` | **`not_done`** | 1 | 3 | 1/0 | 1/2 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H1792` — da.kha "to crush"

**Identity:** mti=7552 · ti=7707 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to crush, be crushed, be contrite, be broken

Sub-senses (depth > 1): 8 entries — present in DB; first 15:
  - `1a` (under `None`): (Niphal)
  - `1a1` (under `None`): to be crushed
  - `1a2` (under `None`): to be contrite (fig.)
  - `1b` (under `None`): (Piel) to crush
  - `1c` (under `None`): (Pual)
  - `1c1` (under `None`): to be crushed, be shattered
  - `1c2` (under `None`): to be made contrite
  - `1d` (under `None`): (Hithpael) to allow oneself to be crushed

**Related words (3 total; sample of 3):**
- `H1793A` dak.ka "contrite"
- `H1793B` dak.ka "dust"
- `H1794` da.khah "to crush"

### `H1793A` — dak.ka "contrite"

**Identity:** mti=7553 · ti=7708 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: adj
contrite

**Related words (3 total; sample of 3):**
- `H1792` da.kha "to crush"
- `H1793B` dak.ka "dust"
- `H1795` dak.kah "crushing"

### `H1793B` — dak.ka "dust"

**Identity:** mti=7557 · ti=7712 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: dust

**Related words (3 total; sample of 3):**
- `H1792` da.kha "to crush"
- `H1793A` dak.ka "contrite"
- `H1795` dak.kah "crushing"

### `H1794` — da.khah "to crush"

**Identity:** mti=7554 · ti=7709 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to crush, be crushed, be contrite, be broken

Sub-senses (depth > 1): 5 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal) to be crushed, collapse
  - `1b` (under `None`): (Niphal) to be crushed, be contrite, be broken
  - `1c` (under `None`): (Piel)
  - `1c1` (under `None`): to crush down
  - `1c2` (under `None`): to crush to pieces

**Related words (4 total; sample of 4):**
- `H1790` dakh "crushed"
- `H1792` da.kha "to crush"
- `H1795` dak.kah "crushing"
- `H1796` do.khi "pounding"

### `H1795` — dak.kah "crushing"

**Identity:** mti=7558 · ti=7713 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: a crushing

**Related words (4 total; sample of 4):**
- `H1790` dakh "crushed"
- `H1793A` dak.ka "contrite"
- `H1793B` dak.ka "dust"
- `H1794` da.khah "to crush"

### `H3795` — ka.tit "beaten"

**Identity:** mti=7563 · ti=7727 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: beaten out, pure, pounded fine (in a mortar), costly

Sub-senses (depth > 1): 1 entries — present in DB; first 15:
  - `1a` (under `None`): of olive oil

**Related words (2 total; sample of 2):**
- `H3807` ka.tat "to crush"
- `H4386` me.khit.tah "fragment"

### `H3807` — ka.tat "to crush"

**Identity:** mti=7556 · ti=7711 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to beat, crush by beating, crush to pieces, crush fine

Sub-senses (depth > 1): 9 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal)
  - `1a1` (under `None`): to beat or crush fine
  - `1a2` (under `None`): to beat, hammer
  - `1b` (under `None`): (Piel)
  - `1b1` (under `None`): to beat or crush fine
  - `1b2` (under `None`): to beat, hammer
  - `1c` (under `None`): (Pual) to be beaten
  - `1d` (under `None`): (Hiphil) to beat in pieces, shatter
  - `1e` (under `None`): (Hophal) to be beaten, be crushed

**Related words (2 total; sample of 2):**
- `H3795` ka.tit "beaten"
- `H4386` me.khit.tah "fragment"

### `H4386` — me.khit.tah "fragment"

**Identity:** mti=7564 · ti=7728 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: crushed or pulverised fragments

**Related words (2 total; sample of 2):**
- `H3795` ka.tit "beaten"
- `H3807` ka.tat "to crush"

### `H5222` — ne.kheh "smitten"

**Identity:** mti=7562 · ti=7723 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: stricken, smitten

**Related words (11 total; sample of 11):**
- `H3559A` kun "to establish: prepare"
- `H3559B` na.khon "blow"
- `H3559H` kun "to establish: establish"
- `H3559I` kun "to establish: make"
- `H3559J` kun "to establish: commit"
- `H3559K` kun "to establish: right"
- `H4347` mak.kah "wound"
- `H5221` na.khah "to smite"
- `H5223` na.kheh "crippled"
- `H5224G` ne.kho "Neco"
- `H5224H` ne.kho "[Pharaoh] Neco"

### `H5223` — na.kheh "crippled"

**Identity:** mti=7555 · ti=7710 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T04:52:08): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: stricken, smitten

**Related words (11 total; sample of 11):**
- `H3559A` kun "to establish: prepare"
- `H3559B` na.khon "blow"
- `H3559H` kun "to establish: establish"
- `H3559I` kun "to establish: make"
- `H3559J` kun "to establish: commit"
- `H3559K` kun "to establish: right"
- `H4347` mak.kah "wound"
- `H5221` na.khah "to smite"
- `H5222` ne.kheh "smitten"
- `H5224G` ne.kho "Neco"
- `H5224H` ne.kho "[Pharaoh] Neco"

---

## E. XREF Terms [Unit 2] (3)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `H4835` | me.ru.tsah | oppression | H | 105 lust | `extracted` | 1 |
| `H7518` | rats | piece | H | 105 lust | `extracted` | 1 |
| `H7533` | ra.tsats | to crush | H | 105 lust | `extracted` | 18 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H1792` — 3 groups

- **`7552-001`** — 3 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C13`
  - *inner-being anguish — the crushing of the person by suffering, adversity, or hostile words*
- **`7552-002`** — 2 relevant · 1 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C13`
  - *substitutionary crushing — the Servant's inner person crushed for iniquity, producing peace and healing*
- **`7552-003`** — 2 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C13`
  - *the contrite and crushed inner spirit — the condition of brokenness before God that occasions divine presence, and its refusal*

### `H1793A` — 1 groups

- **`7553-001`** — 2 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C13`
  - *the crushed and contrite inner spirit — the broken posture before God that draws divine nearness and revival*

### `H1793B` — 1 groups

- **`7557-001`** — 2 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C13`
  - *the crushed/contrite inner spirit — brokenness before God drawing divine nearness*
  - notes: Homograph sub-entry of H1793A dak.ka (contrite). Same verses — Psa 34:18 and Isa 57:15. See SBF-036-001 for Session B assessment of whether this sub-entry carries a distinct inner-being nuance.

### `H1794` — 2 groups

- **`7554-001`** — 3 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C13`
  - *the broken and contrite heart as the inner sacrifice acceptable to God — inner brokenness in penitence and suffering*
- **`7554-002`** — 1 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C13`
  - *corporate inner desolation under divine crushing — the community broken by God in distress*

### `H1795` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H3795` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H3807` — 1 groups

- **`7556-001`** — 1 relevant · 1 anchor verse(s) · dimension: `02 — Emotion — Negative` · cluster: `C13`
  - *inner terror and panic — the inner state of dismay accompanying devastating defeat*

### `H4386` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H5222` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H5223` — 1 groups

- **`7555-001`** — 1 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C13`
  - *the humble and contrite spirit — the broken inner posture before God that receives divine attention*

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
| 183 heart | 6 |
| 8 appetite | 3 |
| 76 holiness | 3 |
| 123 pride | 3 |
| 197 authority | 3 |
| 204 name | 3 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 8 appetite | Isa 57:15 |
| 61 fear | Isa 66:2 |
| 61 fear | Jer 46:5 |
| 62 fellowship | Isa 53:5 |
| 123 pride | Isa 57:15 |
| 151 sorrow | Isa 53:5 |
| 204 name | Isa 57:15 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (0)

_None._

### H.2 Open SD pointers + research flags (1)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SD_POINTER` | DIM-30-SD001 | MEDIUM | D | 2026-04-13 |

#### DIM-30-SD001

> Registry 30 (contrition) produces strong convergence: 5 of 9 groups assign Dependence / Creatureliness (7552-003, 7553-001, 7554-001, 7555-001, 7557-001). This convergence suggests contrition is the penitential sub-form of Dependence / Creatureliness — brokenness before God arising from moral self-awareness and recognition of unworthiness. Session D should examine whether the programme vocabulary needs a finer distinction between general dependence/trust and specifically penitential dependence (contrition). Connect with Reg 10 (dependence/trust) and Reg 80 (trust) in the programme.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

_No phase2 flags on any OWNER term._

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H1792` — 18/18 classified · 3 anchor verse(s)

**Group `7552-001`** (3 verses — anchors: Psa 143:3)

- **Psa 143:3** 🔵 (✓) *target: crushed*
  > Psa 143:3 For the enemy has pursued my soul ; he has crushed my life to the ground ; he has made me sit in darkness like those long dead .
- **Job 6:9** (✓) *target: crush*
  > Job 6:9 that it would please God to crush me, that he would let loose his hand and cut me off !
  - notes: Job's longing for God to crush and end his suffering — existential anguish
- **Job 19:2** (✓) *target: pieces*
  > Job 19:2 “ How long will you torment me and break me in pieces with words ?
  - notes: Broken in pieces by words — inner torment from verbal assault

**Group `7552-002`** (2 verses — anchors: Isa 53:5)

- **Isa 53:5** 🔵 (✓) *target: crushed*
  > Isa 53:5 But he was pierced for our transgressions ; he was crushed for our iniquities ; upon him was the chastisement that brought us peace , and with his wounds we are healed .
- **Isa 53:10** (✓) *target: crush*
  > Isa 53:10 Yet it was the will of the Lord to crush him; he has put him to grief ; when his soul makes an offering for guilt , he shall see his offspring ; he shall prolong his days ; the will of the Lord shall prosper in his hand .
  - notes: Will of Lord to crush him; soul as guilt offering

**Group `7552-003`** (2 verses — anchors: Isa 57:15)

- **Isa 57:15** 🔵 (✓) *target: contrite*
  > Isa 57:15 For thus says the One who is high and lifted up, who inhabits eternity , whose name is Holy : “I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit , to revive the spirit of the lowly , and to revive the heart of the contrite .
- **Jer 44:10** (✓) *target: humbled*
  > Jer 44:10 They have not humbled themselves even to this day , nor have they feared , nor walked in my law and my statutes that I set before you and before your fathers .
  - notes: Failure to humble — the unbroken inner posture refusing contrition

**Group `SET-ASIDE`** (11 verses)

- **Job 4:19** (✗) [set_aside: physical_only] *target: crushed*
  > Job 4:19 how much more those who dwell in houses of clay , whose foundation is in the dust , who are crushed like the moth .
  - notes: Crushed like the moth — mortal frailty metaphor
- **Job 5:4** (✗) [set_aside: no_inner_being] *target: crushed*
  > Job 5:4 His children are far from safety ; they are crushed in the gate , and there is no one to deliver them.
  - notes: Children crushed in the gate — external fate/oppression
- **Job 22:9** (✗) [set_aside: no_inner_being] *target: crushed*
  > Job 22:9 You have sent widows away empty , and the arms of the fatherless were crushed .
  - notes: Arms of the fatherless crushed — external oppression
- **Job 34:25** (✗) [set_aside: no_inner_being] *target: crushed*
  > Job 34:25 Thus , knowing their works , he overturns them in the night , and they are crushed .
  - notes: Divine judgment overturning the wicked — external judicial act
- **Psa 72:4** (✗) [set_aside: no_inner_being] *target: crush*
  > Psa 72:4 May he defend the cause of the poor of the people , give deliverance to the children of the needy , and crush the oppressor !
  - notes: Messianic king crushing the oppressor — external judicial act
- **Psa 89:10** (✗) [set_aside: no_inner_being] *target: crushed*
  > Psa 89:10 You crushed Rahab like a carcass ; you scattered your enemies with your mighty arm .
  - notes: God crushing Rahab — cosmic/mythological crushing
- **Psa 94:5** (✗) [set_aside: no_inner_being] *target: crush*
  > Psa 94:5 They crush your people , O Lord , and afflict your heritage .
  - notes: External oppression of God's people
- **Pro 22:22** (✗) [set_aside: no_inner_being] *target: crush*
  > Pro 22:22 Do not rob the poor , because he is poor , or crush the afflicted at the gate ,
  - notes: Prohibition against crushing the afflicted — external act
- **Isa 3:15** (✗) [set_aside: no_inner_being] *target: crushing*
  > Isa 3:15 What do you mean by crushing my people , by grinding the face of the poor ?” declares the Lord God of hosts .
  - notes: Crushing the poor — social oppression
- **Isa 19:10** (✗) [set_aside: no_inner_being] *target: crushed*
  > Isa 19:10 Those who are the pillars of the land will be crushed , and all who work for pay will be grieved .
  - notes: Pillars of the land crushed — societal/structural crushing
- **Lam 3:34** (✗) [set_aside: no_inner_being] *target: crush*
  > Lam 3:34 To crush underfoot all the prisoners of the earth ,
  - notes: To crush underfoot all the prisoners — external crushing

### `H1793A` — 2/2 classified · 1 anchor verse(s)

**Group `7553-001`** (2 verses — anchors: Psa 34:18)

- **Psa 34:18** 🔵 (✓) *target: crushed*
  > Psa 34:18 The Lord is near to the brokenhearted and saves the crushed in spirit .
- **Isa 57:15** (✓) *target: contrite*
  > Isa 57:15 For thus says the One who is high and lifted up, who inhabits eternity , whose name is Holy : “I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit , to revive the spirit of the lowly , and to revive the heart of the contrite .
  - notes: God dwells with the contrite and lowly spirit

### `H1793B` — 2/2 classified · 1 anchor verse(s)

**Group `7557-001`** (2 verses — anchors: Psa 34:18)

- **Psa 34:18** 🔵 (✓) *target: crushed*
  > Psa 34:18 The Lord is near to the brokenhearted and saves the crushed in spirit .
- **Isa 57:15** (✓) *target: contrite*
  > Isa 57:15 For thus says the One who is high and lifted up, who inhabits eternity , whose name is Holy : “I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit , to revive the spirit of the lowly , and to revive the heart of the contrite .

### `H1794` — 5/5 classified · 2 anchor verse(s)

**Group `7554-001`** (3 verses — anchors: Psa 51:17)

- **Psa 51:17** 🔵 (✓) *target: contrite*
  > Psa 51:17 The sacrifices of God are a broken spirit ; a broken and contrite heart , O God , you will not despise .
- **Psa 38:8** (✓) *target: crushed*
  > Psa 38:8 I am feeble and crushed ; I groan because of the tumult of my heart .
  - notes: Feeble and crushed; groaning because of the tumult of the heart
- **Psa 51:8** (✓) *target: broken*
  > Psa 51:8 Let me hear joy and gladness ; let the bones that you have broken rejoice .
  - notes: Bones broken by God; seeking joy and gladness after inner brokenness

**Group `7554-002`** (1 verse — anchors: Psa 44:19)

- **Psa 44:19** 🔵 (✓) *target: broken*
  > Psa 44:19 yet you have broken us in the place of jackals and covered us with the shadow of death .

**Group `SET-ASIDE`** (1 verse)

- **Psa 10:10** (✗) [set_aside: no_inner_being] *target: crushed*
  > Psa 10:10 The helpless are crushed , sink down, and fall by his might .
  - notes: Helpless crushed by the wicked — external oppression

### `H1795` — 1/1 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (1 verse)

- **Deu 23:1** (✗) [set_aside: physical_only] *target: crushed*
  > Deu 23:1 “No one whose testicles are crushed or whose male organ is cut off shall enter the assembly of the Lord .
  - notes: Crushed testicles — physical/cultic exclusion criterion

### `H3795` — 5/5 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (5 verses)

- **Exo 27:20** (✗) [set_aside: physical_only] *target: beaten*
  > Exo 27:20 “ You shall command the people of Israel that they bring to you pure beaten olive oil for the light , that a lamp may regularly be set up to burn .
  - notes: Beaten olive oil for the lamp — cultic/agricultural
- **Exo 29:40** (✗) [set_aside: physical_only] *target: beaten*
  > Exo 29:40 And with the first lamb a tenth measure of fine flour mingled with a fourth of a hin of beaten oil , and a fourth of a hin of wine for a drink offering .
  - notes: Beaten oil in grain offering — cultic/agricultural
- **Lev 24:2** (✗) [set_aside: physical_only] *target: beaten*
  > Lev 24:2 “ Command the people of Israel to bring you pure oil from beaten olives for the lamp , that a light may be kept burning regularly .
  - notes: Pure oil from beaten olives for lamp — cultic
- **Num 28:5** (✗) [set_aside: physical_only] *target: beaten*
  > Num 28:5 also a tenth of an ephah of fine flour for a grain offering , mixed with a quarter of a hin of beaten oil .
  - notes: Beaten oil in grain offering — cultic
- **1Ki 5:11** (✗) [set_aside: physical_only] *target: beaten*
  > 1Ki 5:11 while Solomon gave Hiram 20,000 cors of wheat as food for his household , and 20,000 cors of beaten oil . Solomon gave this to Hiram year by year .
  - notes: 20,000 cors of beaten oil — commercial

### `H3807` — 17/17 classified · 1 anchor verse(s)

**Group `7556-001`** (1 verse — anchors: Jer 46:5)

- **Jer 46:5** 🔵 (✓) *target: beaten down*
  > Jer 46:5 Why have I seen it? They are dismayed and have turned backward . Their warriors are beaten down and have fled in haste ; they look not back — terror on every side ! declares the Lord .

**Group `SET-ASIDE`** (16 verses)

- **Lev 22:24** (✗) [set_aside: physical_only] *target: crushed*
  > Lev 22:24 Any animal that has its testicles bruised or crushed or torn or cut you shall not offer to the Lord ; you shall not do it within your land ,
  - notes: Crushed animal — cultic exclusion criterion
- **Num 14:45** (✗) [set_aside: no_inner_being] *target: pursued*
  > Num 14:45 Then the Amalekites and the Canaanites who lived in that hill country came down and defeated them and pursued them, even to Hormah .
  - notes: Military defeat — external
- **Deu 1:44** (✗) [set_aside: no_inner_being] *target: down*
  > Deu 1:44 Then the Amorites who lived in that hill country came out against you and chased you as bees do and beat you down in Seir as far as Hormah .
  - notes: Military defeat
- **Deu 9:21** (✗) [set_aside: physical_only] *target: crushed*
  > Deu 9:21 Then I took the sinful thing, the calf that you had made , and burned it with fire and crushed it, grinding it very small , until it was as fine as dust . And I threw the dust of it into the brook that ran down from the mountain .
  - notes: Moses crushing the golden calf to dust — physical destruction
- **2Ki 18:4** (✗) [set_aside: physical_only] *target: pieces*
  > 2Ki 18:4 He removed the high places and broke the pillars and cut down the Asherah . And he broke in pieces the bronze serpent that Moses had made , for until those days the people of Israel had made offerings to it (it was called Nehushtan ).
  - notes: Hezekiah breaking the bronze serpent — physical destruction of idol
- **2Ch 15:6** (✗) [set_aside: no_inner_being] *target: crushed*
  > 2Ch 15:6 They were broken in pieces. Nation was crushed by nation and city by city , for God troubled them with every sort of distress .
  - notes: Nation crushed by nation — societal/military devastation
- **2Ch 34:7** (✗) [set_aside: physical_only] *target: beat*
  > 2Ch 34:7 he broke down the altars and beat the Asherim and the images into powder and cut down all the incense altars throughout all the land of Israel . Then he returned to Jerusalem .
  - notes: Josiah crushing idols to powder — physical destruction
- **Job 4:20** (✗) [set_aside: physical_only] *target: pieces*
  > Job 4:20 Between morning and evening they are beaten to pieces ; they perish forever without anyone regarding it.
  - notes: Beaten to pieces — human frailty/mortality image
- **Psa 89:23** (✗) [set_aside: no_inner_being] *target: crush*
  > Psa 89:23 I will crush his foes before him and strike down those who hate him.
  - notes: God crushing enemies — external divine act
- **Isa 2:4** (✗) [set_aside: no_inner_being] *target: beat*
  > Isa 2:4 He shall judge between the nations , and shall decide disputes for many peoples ; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore .
  - notes: Swords into plowshares — ka.tat carries mechanical transformation; inner peace orientation carried by passage context, not term
- **Isa 24:12** (✗) [set_aside: no_inner_being] *target: battered*
  > Isa 24:12 Desolation is left in the city ; the gates are battered into ruins .
  - notes: Gates battered into ruins — structural destruction
- **Isa 30:14** (✗) [set_aside: physical_only] *target: smashed*
  > Isa 30:14 and its breaking is like that of a potter’s vessel that is smashed so ruthlessly that among its fragments not a shard is found with which to take fire from the hearth , or to dip up water out of the cistern .”
  - notes: Potter's vessel smashed — physical destruction metaphor
- **Joe 3:10** (✗) [set_aside: no_inner_being] *target: Beat*
  > Joe 3:10 Beat your plowshares into swords , and your pruning hooks into spears ; let the weak say , “ I am a warrior .”
  - notes: Beat plowshares into swords — inverse mobilisation; same logic as Isa 2:4
- **Mic 1:7** (✗) [set_aside: physical_only] *target: beaten*
  > Mic 1:7 All her carved images shall be beaten to pieces, all her wages shall be burned with fire , and all her idols I will lay waste , for from the fee of a prostitute she gathered them, and to the fee of a prostitute they shall return .
  - notes: Carved images beaten to pieces — physical idol destruction
- **Mic 4:3** (✗) [set_aside: no_inner_being] *target: beat*
  > Mic 4:3 He shall judge between many peoples , and shall decide disputes for strong nations far away; and they shall beat their swords into plowshares , and their spears into pruning hooks ; nation shall not lift up sword against nation , neither shall they learn war anymore ;
  - notes: Swords into plowshares (Mic 4:3) — same logic as Isa 2:4
- **Zec 11:6** (✗) [set_aside: no_inner_being] *target: crush*
  > Zec 11:6 For I will no longer have pity on the inhabitants of this land , declares the Lord . Behold , I will cause each of them to fall into the hand of his neighbor , and each into the hand of his king , and they shall crush the land , and I will deliver none from their hand .”
  - notes: Crushing the land through judgment — external

### `H4386` — 1/1 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (1 verse)

- **Isa 30:14** (✗) [set_aside: physical_only] *target: fragments*
  > Isa 30:14 and its breaking is like that of a potter’s vessel that is smashed so ruthlessly that among its fragments not a shard is found with which to take fire from the hearth , or to dip up water out of the cistern .”
  - notes: Physical fragments of broken vessel — no inner-being content

### `H5222` — 1/1 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (1 verse)

- **Psa 35:15** (✗) [set_aside: no_inner_being] *target: wretches*
  > Psa 35:15 But at my stumbling they rejoiced and gathered ; they gathered together against me; wretches whom I did not know tore at me without ceasing ;
  - notes: Enemies gathering against the psalmist — ne.kheh inner-being relevance not evident

### `H5223` — 3/3 classified · 1 anchor verse(s)

**Group `7555-001`** (1 verse — anchors: Isa 66:2)

- **Isa 66:2** 🔵 (✓) *target: contrite*
  > Isa 66:2 All these things my hand has made , and so all these things came to be, declares the Lord . But this is the one to whom I will look : he who is humble and contrite in spirit and trembles at my word .

**Group `SET-ASIDE`** (2 verses)

- **2Sa 4:4** (✗) [set_aside: physical_only] *target: crippled*
  > 2Sa 4:4 Jonathan , the son of Saul , had a son who was crippled in his feet . He was five years old when the news about Saul and Jonathan came from Jezreel , and his nurse took him up and fled , and as she fled in her haste , he fell and became lame . And his name was Mephibosheth .
  - notes: Mephibosheth crippled in his feet — physical disability
- **2Sa 9:3** (✗) [set_aside: physical_only] *target: crippled*
  > 2Sa 9:3 And the king said , “Is there not still someone of the house of Saul , that I may show the kindness of God to him?” Ziba said to the king , “There is still a son of Jonathan ; he is crippled in his feet .”
  - notes: Mephibosheth crippled in his feet — physical disability

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**10 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H1792` | to crush | `not_done` | 18 | 3 | 18 |
| `H1793A` | contrite | `not_done` | 2 | 1 | 2 |
| `H1793B` | dust | `not_done` | 2 | 1 | 2 |
| `H1794` | to crush | `not_done` | 5 | 2 | 5 |
| `H1795` | crushing | `not_done` | 1 | 0 | 1 |
| `H3795` | beaten | `not_done` | 5 | 0 | 5 |
| `H3807` | to crush | `not_done` | 17 | 1 | 17 |
| `H4386` | fragment | `not_done` | 1 | 0 | 1 |
| `H5222` | smitten | `not_done` | 1 | 0 | 1 |
| `H5223` | crippled | `not_done` | 3 | 1 | 3 |

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

### Registry-specific questions for 030 contrition

_None._ No questions in `wa_obs_question_catalogue` are sourced from registry 30 (contrition).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-04-27T20:05:03Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`

**Stage 1 quick checks:**

- Registry status fields populated: ✓
- OWNER term inventory non-empty: ✓
- All OWNER terms have at least 1 verse: ✓
- Researcher fields preserved: absent — researcher narrative not yet written

---

*End of readiness output v3 — wa-030-contrition.*