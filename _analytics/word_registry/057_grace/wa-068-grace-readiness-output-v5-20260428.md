# wa-068-grace — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-04-28T06:26:03Z · schema 3.17.0_

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

- **Registry no:** `68` · **word:** `grace`
- **verse_context_status:** `In Progress`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v1.9-2026-04-09`)
- **cluster_assignment:** `C17`
- **sb_classification:** `Spirit-soul interface`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Relational/Social`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 13  (programme-wide aggregate including XREF and historical terms — current OWNER count is 5, XREF 5)
- `phase1_verse_count`: 412  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 55 unresolved · **Existing session_b_findings:** 1

**Description:**

> Grace is undeserved gift — the giving of what is needed not because it has been earned but because the giver chooses to give it. The Hebrew vocabulary (hen, favour; chesed, steadfast love) and the Greek (charis) together carry the sense of the one who has the power to grant or withhold choosing freely to give. Grace is the fundamental mode of God's relationship with humanity in Scripture: from creation through covenant through redemption, what humans receive from God is given, not owed. Grace creates the recipient rather than rewarding them.

**sb_classification_reasoning:**

> Grace originates at the spirit level — it is the freely given disposition of God toward humanity, received as a gift from above, not self-generated. Its structure as gift requires an outside source. At the soul level grace is thoroughly expressed: the desire for it, the fear of being without it, the experience of finding it, and the transformed inner disposition of the one formed by it are all soulish states — personally felt, emotionally coloured, relationally constituted. Somatic evidence (prostration, weeping, raised hands, fasting, gracious speech) confirms that grace is enacted through the body without originating there. Body enacts and externalises what is happening at the spirit-soul level. Confidence: high — pattern consistent across 194 active verses and all nine owner terms.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-04-28T06:26:03Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 5
- **OWNER terms legacy-VC (not_done):** 5 / 5

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 5 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H2580` | chen | favor | H | `extracted` | **`to_revise`** | 1 | 67 | 3/0 | 61/0 | 4 |
| `H8469` | ta.cha.nun | supplication | H | `extracted_thin` | **`to_revise`** | 1 | 18 | 1/0 | 18/0 | 2 |
| `G5483` | charizō | to give grace | G | `extracted` | **`to_revise`** | 1 | 19 | 2/0 | 15/0 | 2 |
| `G5485` | charis | grace | G | `extracted` | **`to_revise`** | 1 | 88 | 4/0 | 84/0 | 6 |
| `G5487` | charitoō | to favor | G | `extracted` | **`to_revise`** | 1 | 2 | 1/0 | 2/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H2580` — chen "favor"

**Identity:** mti=889 · ti=928 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:36): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: favour, grace, charm

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): favour, grace, elegance
  - `1b` (under `None`): favour, acceptance

**Root family:**
- `CHEN` (Hebrew): favor — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (51 total; sample of 30):**
- `H2433` chin "beauty"
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
- `H2603A` cha.nan "be gracious"
- … and 15 more shown of 51 total

### `H8469` — ta.cha.nun "supplication"

**Identity:** mti=890 · ti=929 · language=Hebrew · status=`extracted_thin` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:36): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: supplication, supplication for favour

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): to man
  - `1b` (under `None`): to God

**Root family:**
- `CHEN` (Hebrew): favor — Backfilled 2026-04-09 from wa_term_related_words clustering

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

### `G5483` — charizō "to give grace"

**Identity:** mti=5470 · ti=5584 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:36): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to give grace; to forgive, cancel (a debt); to grant; to hand over into custody 
to gratify; to bestow, in kindness, grant as a free favor, Lk. 7:21; Rom. 8:32; to grant the deliverance of a person in favor to the desire of others, Acts 3:14; 27:24; Phlm. 22; to sacrifice a person to the demand of enemies, Acts 25:11; to remit, forgive, Lk. 7:42; 2Cor. 2:7, 10

**Root family:**
- `CHAR` (Greek): grace — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G0884` acharistos "ungrateful"
- `G5485` charis "grace"
- `G5486` charisma "gift"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G5485` — charis "grace"

**Identity:** mti=888 · ti=927 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:36): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: grace, the state of kindness and favor toward someone, often with a focus on a benefit given to the object; by extension: gift, benefit; credit; words of kindness and benefit: thanks, blessing 
pleasing show, charm; beauty, gracefulness; a pleasing circumstance, matter of approval, 1Pet. 2:19, 20; kindly bearing, graciousness, Lk. 4:22; a beneficial opportunity, benefit, 2Cor. 1:15; Eph. 4:29; a charitable act, generous gift, 1Cor. 16:3; 2Cor. 8:4, 6; an act of favor, Acts 25:3; favor, acceptance, Lk. 1:30, 52; Acts 2:47; 7:10, 46; free favor, free gift, grace, Jn. 1:14, 16, 17; Rom. 4:4, 16; 11:5, 6; Eph. 2:5, 8; 1Pet. 3:7; free favor specially manifested by God towards man in the Gospel scheme, grace, Acts 15:11; Rom. 3:24; 5:15, 17, 20, 21; 6:1; 2Cor. 4:15; a gracious provision, gracious scheme, grace, Rom. 6:14, 15; Heb. 2:9; 12:28; 13:9; gracious dealing from God, grace, Acts 14:26; 15:40; Rom. 1:7; 1Cor. 1:4; 15:10; Gal. 1:15; a commission graciously devolved by God upon a human agent, Rom. 1:5; 12:3; 15:15; 1Cor. 3:10; 2Cor. 1:12; Gal. 2:9; Eph. 3:8; grace, graciously bestowed divine endowment or influence, Lk. 2:40; Acts 4:33; 11:23; Rom. 12:6; 2Cor. 12:9; grace, Acts 11:43; Rom. 5:2; Gal. 5:4; 2Pet. 3:18; an emotion correspondent to what is pleasing or kindly; sense of obligation, Lk. 17:9; a grateful frame of mind, 1Cor. 10:30; thanks, Lk. 6:32, 33, 34; Rom. 6:17; 1Cor. 15:57; χάριν or χάριτας καταθέσθαι, to oblige, gratify, Acts 24:27; 25:9

**Root family:**
- `CHAR` (Greek): grace — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G5483` charizō "to give grace"
- `G5487` charitoō "to favor"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G5487` — charitoō "to favor"

**Identity:** mti=5471 · ti=5585 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:36): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to give graciously, to show acts of kindness by freely giving; (n.) one highly favored; see also G5485 favor 
to favor, visit with favor, to make an object of favor, to gift, Eph. 1:6; passive to be visited with free favor, be an object of gracious visitation, to give graciously Lk. 1:28*

**Root family:**
- `CHAR` (Greek): grace — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G5485` charis "grace"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (5)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `H2587` | chan.nun | gracious | H | 23 compassion | `extracted` | 13 |
| `H2594` | cha.ni.nah | favor | H | 23 compassion | `extracted_thin` | 0 |
| `H2600` | chin.nam | for nothing | H | ? | `extracted` | 0 |
| `H2603A` | cha.nan | be gracious | H | 111 mercy | `extracted` | 72 |
| `H8467` | te.chin.nah | supplication | H | 111 mercy | `extracted_thin` | 24 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H2580` — 3 groups

- **`889-001`** — 15 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the divine relational favour bestowed on a person — the inner-relational disposition of God toward those he knows by name, which creates standing, protection, and access, and which is sought, recognised, and treasured*
- **`889-002`** — 36 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names relational favour between persons — the inner-relational disposition of goodwill one person seeks and receives from another, which creates access, loyalty, and life*
- **`889-003`** — 10 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names favour as inner character quality — the gracious disposition expressed in speech, conduct, and wisdom that generates standing and blessing in community*

### `H8469` — 1 groups

- **`890-001`** — 18 relevant · 2 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the inner act of earnest supplication — the plea for mercy that arises from deep need and relational vulnerability before God, offered with the expectation that God hears and responds*

### `G5483` — 2 groups

- **`5470-001`** — 7 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's gracious giving and forgiving — the divine act of freely granting, releasing, and bestowing on the basis of grace alone, supremely in the gift of the Son and forgiveness of sins*
- **`5470-002`** — 8 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the human act of forgiving — releasing another from debt, offence, or resentment, patterned on and grounded in the divine forgiveness received, as an inner-relational act of grace extended to another*

### `G5485` — 4 groups

- **`888-001`** — 22 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names grace as the sovereign, unmerited divine disposition toward humanity — the freely given, transforming gift through which God justifies, saves, calls, and sustains, supremely displayed in Christ*
- **`888-002`** — 13 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names grace as the relational sphere and power in which the believer stands and lives — the ongoing inner-relational condition of being under grace, accessed by faith, sustained by God, and expressed in the transformed inner being*
- **`888-003`** — 13 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names grace as relational favour — the disposition of goodwill between persons or between a person and God, which opens access, creates loyalty, and reflects the character of the one granting it*
- **`888-004`** — 36 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names grace as the animating power and sphere of apostolic mission — the word of grace, the commendation to grace, the extending of grace to more people, and the inner source of ministry identity*

### `G5487` — 1 groups

- **`5471-001`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the act of bestowing grace — the divine favour poured upon a person or people as a relational act that marks and transforms the one so favoured*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 23 compassion | 2 | `H2580,H8469` |
| 73 guilt | 2 | `H2580,H8469` |
| 111 mercy | 2 | `H2580,H8469` |
| 212 pray | 2 | `H2580,H8469` |
| 132 rejoicing | 1 | `G5485` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 140 seeking | 23 |
| 103 love | 12 |
| 43 desire | 11 |
| 59 faith | 10 |
| 73 guilt | 10 |
| 121 praise | 9 |
| 180 yielding | 8 |
| 213 listen | 8 |
| 67 goodness | 7 |
| 117 peace | 7 |
| 187 strength | 7 |
| 194 blessing | 7 |
| 98 justice | 6 |
| 162 transgression | 6 |
| 173 will | 6 |
| 199 dominion | 6 |
| 210 deadness | 6 |
| 78 hope | 5 |
| 99 kindness | 5 |
| 198 might | 5 |
| 19 calling | 4 |
| 39 debauchery | 4 |
| 174 wisdom | 4 |
| 176 worship | 4 |
| 182 Soul | 4 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 39 debauchery | Eph 2:8 |
| 78 hope | Rom 5:2 |
| 99 kindness | Eph 4:32 |
| 113 mourning | Zec 12:10 |
| 121 praise | Pro 31:30 |
| 123 pride | 2Cor 12:9 |
| 180 yielding | Eph 2:8 |
| 183 heart | Eph 4:32 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-068-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-10 · **term_id:** -

> Group 890-001 (ta.cha.nun, supplication) — Dan 9:3 anchor shows earnest supplication enacted somatically: fasting, sackcloth, ashes. The body enacts what the inner person is doing — the whole person brought into alignment with the inner posture of plea. Session B should examine the somatic signature of grace-supplication: whether the body-posture vocabulary of petition (prostration, fasting, weeping, raised hands) encodes inner-being content about the Dependence/Creatureliness orientation, and how this connects to the grace registry's inner-being picture. Zec 12:10 (shared anchor with 889-001) shows that the capacity for earnest supplication is itself grace-given — the Spirit of grace produces the plea. This is the inner-being grammar of grace-response: grace first, supplication as grace-enabled response.

### H.2 Open SD pointers + research flags (55)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `PH2_CROSS_REF_ENRICHMENT` | PH2-068-004 | MEDIUM | D | 2026-04-09 |
| `PH2_CROSS_REF_ENRICHMENT` | PH2-068-005 | MEDIUM | D | 2026-04-09 |
| `SD_POINTER` | DIM-068-SD019 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD022 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD023 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD028 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD033 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD036 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD037 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD039 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD043 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD046 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD048 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD049 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD003 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD007 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD009 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD010 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD011 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD012 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD015 | MEDIUM | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD040 | LOW | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD044 | LOW | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD045 | LOW | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD050 | LOW | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD016 | LOW | D | 2026-04-10 |
| `PH2_CROSS_REF_ENRICHMENT` | PH2-068-001 | HIGH | D | 2026-04-09 |
| `PH2_CROSS_REF_ENRICHMENT` | PH2-068-002 | HIGH | D | 2026-04-09 |
| `PH2_CROSS_REF_ENRICHMENT` | PH2-068-003 | HIGH | D | 2026-04-09 |
| `SD_POINTER` | DIM-068-SD001 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD018 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD020 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD021 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD024 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD025 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD026 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD027 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD029 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD030 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD031 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD032 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD034 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD035 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD038 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD041 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD042 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD047 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD002 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD004 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD005 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD006 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD008 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD013 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD014 | HIGH | D | 2026-04-10 |
| `SD_POINTER` | DIM-068-SD017 | HIGH | D | 2026-04-10 |

#### PH2-068-004

> Grace-Identity formation signal: 1Cor 15:10 — 'by the grace of God I am what I am' — strongest statement in corpus of grace as identity-constituting. Connects to identity-formation vocabulary. Flag for cross-registry investigation.

#### PH2-068-005

> Grace-Lament connection: weeping-supplication complex (tachanum + weeping in Jer 3:21, 31:9; Zec 12:10; Est 8:3; Dan 9:3) connects grace-seeking posture to the lament tradition. Warrants investigation when lament vocabulary is processed.

#### DIM-068-SD019

> charizō's juridical sense (handing over to custody — Lk 23:25: Jesus handed over; Acts 27:24: Paul granted to those sailing) sits alongside its gift sense. Both involve giving from authority. The inner-being contrast: grace in the giving sense is free goodwill; grace in the custody sense is juridical compliance under pressure. The same term names Pilate handing Jesus over and God graciously giving all things. For Session D: does charizō's range across grace and juridical custody illuminate the inner-being conditions under which authority gives freely vs. gives under compulsion? Connects to the C20 power-authority cluster (DIM-068-SD003).

#### DIM-068-SD022

> charis means 'gracious words' in Luk 4:22 and 'speech seasoned with grace' in Col 4:6 — the chen/grace-as-speech-quality sense carried into Greek. Connects to wisdom (174, cooccurrence 8 verses), praise (121, shared anchor Pro 31:30 + cooccurrence 8 verses), and listening (213, cooccurrence 11 verses). For Session D: is there a grace-speech-hearing inner-being loop — grace received inwardly expressed in gracious speech, which when heard creates conditions for the hearer to receive grace? This would connect grace, wisdom, speech, and listening as a functional inner-being sequence.

#### DIM-068-SD023

> charitoō is a biblical coinage — it does not appear in classical Greek. The need to create a new word for 'to grace someone' (to make someone the object of divine favour as a completed, continuing state) suggests the concept of standing-in-favour exceeded what existing vocabulary could carry. The perfect passive kecharitōmenē (Lk 1:28) encodes a completed act with continuing state. For Session D: does the absence of this concept in classical Greek vocabulary reveal something about the uniqueness of the biblical inner-being claim about grace? Is the specifically biblical inner-being reality of standing-in-favour a concept that required new language to encode?

#### DIM-068-SD028

> Dan 9:23 — 'at the beginning of your pleas for mercy a word went out.' God's response to Daniel's supplication preceded the completion of his plea. Seeking and being-found, supplication and grace-response, appear simultaneous rather than sequential — the creature's orientation toward God and God's movement toward the creature happen in the same moment. For Session D: does this simultaneity pattern appear across the prayer-grace-seeking cluster? The seeking registry (Reg 140, cooccurrence 40 verses) may encode this most fully — the creature seeking and God already having moved.

#### DIM-068-SD033

> Eph 2:8 shares its anchor with both debauchery (Reg 39) and yielding (Reg 180). Debauchery sharing this anchor likely encodes the contrast-condition: grace enters into the situation of moral dissolution (Eph 2:1-5: dead in trespasses). Yielding as shared anchor encodes the inner-being posture grace requires: 'not your own doing' is the inner surrender of the merit-claim. For Session D: is the yielding/surrender inner-being posture (Reg 180, cooccurrence 8 verses) structurally connected to the reception of grace — is the surrender of self-contribution the necessary inner condition for grace to be received rather than merely encountered?

#### DIM-068-SD036

> Act 20:32 — 'the word of his grace, which is able to build you up.' Grace operates as a constructive force through the proclaimed word, building the inner person over time (oikodomeō — to construct, edify). For Session D: does the wisdom registry (Reg 174, cooccurrence 8 verses) encode the building-up function of grace through wise speech? Is there a grace-word-wisdom-formation inner-being sequence — grace expressed through wise speech as the mechanism of inner-being construction? How does this relate to the grace-speech-hearing loop (DIM-068-SD022)?

#### DIM-068-SD037

> Exo 33:17 — 'I know you by name.' Grace grounded in prior divine knowing: God's knowing of Moses precedes and grounds the favour. Being known by God is the basis of the relational standing grace creates. For Session D: does the name registry (Reg 204, cooccurrence 3 verses) encode the theological weight of the name as the locus of God's personal knowing? Is 'being known by name' the deepest form of the inner-being condition of being-in-grace? Does this connect to calling (Reg 19) — where being called by name is the inner-being experience of the prior divine knowing that grounds grace?

#### DIM-068-SD039

> Rut 2:10 — Ruth fell on her face bowing before speaking. The body's response to unexpected grace precedes the voiced question. The inner-being posture of grace-receiving is enacted somatically before it is articulated verbally: prostration before questioning. For Session D: is the prostration-before-grace pattern a consistent somatic encoding across registries? Do the worship (Reg 176), prayer (Reg 122), and seeking (Reg 140) registries show prostration as the body's form of the Dependence/Creatureliness inner orientation? Is there a programme-wide somatic grammar of the creature before grace?

#### DIM-068-SD043

> G0884 acharistos (ungrateful, graceless — related word of G5483/G5485) is the structural antithesis of grace lexically encoded in the same root family. Ingratitude is the inner failure to recognise grace as grace — receiving the gift without registering it as gift. For Session D: does the gratitude registry (Reg 69, cooccurrence 3 verses) and the pride registry (Reg 123, cooccurrence 3 verses + shared anchor) converge on acharistos as the inner condition most opposed to grace-reception? Is ingratitude — the inner failure to register grace as grace — the same inner-being condition as pride — the inner elevation of the self that excludes the logic of gift?

#### DIM-068-SD046

> Desire (Reg 43, C04) cooccurrence 12 verses. Grace and desire co-occur substantively. The inner-being question: is desire the faculty through which grace is sought and received? Does grace reorder desire — so that the person formed by grace desires differently? Or is disordered desire the counter-condition to grace-receiving? For Session D: examine the 12 co-occurring verses to determine what relationship the data shows between the disposition of desire and the reception of grace. Does grace redirect desire from within, or does desire need to be redirected before grace can operate?

#### DIM-068-SD048

> Thought (Reg 160, C02) cooccurrence 4 verses. Pass 1 identified the inference-structure of grace (Rom 8:32). For Session D: do the 4 co-occurring verses encode the inner-being act of drawing grace-inferences — thinking through what received grace implies? Is there a grace-thought pattern where right thinking about grace is itself an inner-being act enabled by grace?

#### DIM-068-SD049

> Appetite (Reg 8, C04) cooccurrence 4 verses. Appetite names the deep inner longing or craving. For Session D: do the 4 co-occurring verses show appetite as the counter-condition to grace, the channel of grace, or both? Is misdirected appetite (craving lesser goods) the pre-grace condition that grace reorders — so that the person formed by grace develops a new appetite, a hunger for God that is itself grace-given? Connects to desire (DIM-068-SD046) and seeking (Reg 140) — seeking as the rightly-directed form of appetite.

#### DIM-068-SD003

> C20 power cluster dimension overlap: strength (187), power (196), authority (197), might (198), dominion (199) — all share all 3 grace dimensions (Relational Disposition 9 groups, Moral Character 1, Dependence/Creatureliness 1). 2Cor 12:9 makes the structural connection explicit: power made perfect in weakness, grace as its modality. Session D should examine whether grace consistently names the relational mode through which divine power reaches the creature precisely where human power fails, and whether Dependence/Creatureliness is the inner condition that opens the person to both grace and power.

#### DIM-068-SD007

> C11 moral failure cluster cooccurrence: evil (57, 12 verses), sin (147, 6 verses), transgression (162, 6 verses), deceit (40, 5 verses). Also xref_sharing with guilt (73, 9 shared terms) and guilt cooccurrence (10 verses). Grace appears most fully where the creature's moral condition is most exposed. Session D should examine whether grace consistently operates in proximity to moral failure vocabulary, whether the recognition and naming of sin is a structural prerequisite for receiving grace, and what the inner-being sequence looks like — guilt named → grace extended → standing restored.

#### DIM-068-SD009

> Pray (Reg 212) xref_sharing: 10 shared Hebrew terms (entire CHEN root family plus H2600 and deleted terms). The pray-grace xref relationship reflects terms classified under both registries because they carry prayer/petition vocabulary that is simultaneously grace vocabulary. Session D should examine the structural relationship between prayer and grace as inner-being realities: whether prayer presupposes grace (grace makes the creature's approach possible), whether the CHEN root family terms show prayer and grace as two faces of the same inner-being orientation (the creature's receptivity before the greater), and how this relates to DIM-068-SD001 (Zec 12:10 grace producing supplication).

#### DIM-068-SD010

> Will (Reg 173, C14) cooccurrence: 11 verses. Grace and will co-occurring across 11 verses raises the foundational inner-being question of how grace and human volition relate. Grace is unearned and uncompelled; the will is the faculty by which a person receives or refuses it. Session D should examine what the 11 co-occurring verses show: whether grace operates with the will (enabling the will to turn), upon the will (overriding or replacing volitional resistance), or alongside the will (grace as the condition within which the will operates). This may be the most theologically contested question the grace registry raises.

#### DIM-068-SD011

> Calling (Reg 19, C19) cooccurrence: 11 verses. Grace and calling consistently paired in the Pauline corpus: 'called according to his own purpose and grace' (2Tim 1:9); 'not because of works but because of him who calls' (Rom 9:11). Session D should examine whether calling and grace are co-features of the same divine initiating act — grace as the character of the act, calling as the human inner experience of it as personal address — and whether the calling vocabulary adds specificity to how grace is received as directed toward a particular person.

#### DIM-068-SD012

> Listen (Reg 213, C02) cooccurrence: 11 verses. Receptivity of hearing is the inner-being posture through which grace is received; the hardened heart refusing to hear is the condition that closes off grace. Registry 213 was recently added to the programme (adding sha.ma — hear/listen). Session D should examine the listen-grace pairing: whether receptivity of hearing is the human inner-being correlate of divine grace-giving, how the obedience-hearing vocabulary relates to the grace-receiving vocabulary, and whether the listen corpus encodes the inner conditions under which grace is either received or refused. Cross-reference: DIM-187-SD001 (sha.ma broader validation gap).

#### DIM-068-SD015

> Goodness (Reg 67, C10) cooccurrence: 9 verses. Goodness is paired with grace in the OT divine character formula (Exo 34:6: 'abounding in steadfast love and faithfulness'; Psa 25:7: 'according to your steadfast love remember me, for the sake of your goodness'). Session D should examine whether grace and goodness name adjacent or overlapping divine character attributes, whether the inner-being experience of goodness received is distinguishable from grace received, and how the goodness of God functions as a category distinct from grace in the structure of divine inner-being disposition toward the creature.

#### DIM-068-SD040

> Pro 31:30 — charm (chen as attractiveness) is relativised against the fear of the Lord as the ground of enduring worth. The fear of the Lord is the inner-being orientation that generates lasting gracious character — not outward grace of charm but inward orientation of reverence. For Session D: does the fear-of-the-Lord vocabulary connect the grace registry (grace as character quality) to the wisdom cluster? Is the fear of the Lord the inner-being orientation that is the root of both grace-as-character and wisdom? If so, grace and wisdom share a foundational inner-being ground — the reverential orientation of the creature before God.

#### DIM-068-SD044

> Experience (Reg 58, C22) shares Moral Character and Dependence/Creatureliness dimensions with grace. For Session D: is grace what transforms raw creaturely experience into formative inner-being content? Is Dependence/Creatureliness the inner-being orientation through which experience is processed as a school of grace? Does the experience registry's content reveal whether grace is constitutively connected to the inner-being processing of lived creaturely experience?

#### DIM-068-SD045

> Foolishness (Reg 63, C22) shares Moral Character and Relational Disposition dimensions with grace. Grace extending toward the foolish person — the one who lacks the inner orientation to receive what is good — encodes the unconditional character of grace distinctively. For Session D: does the foolishness-grace dimension overlap encode that grace operates toward the morally incapacitated inner person? Is this a variant of the grace-toward-the-dead pattern (DIM-068-SD008) — grace directed not at the guilty but at the incapacitated?

#### DIM-068-SD050

> Doubt (Reg 191, C16) cooccurrence 3 verses. Doubt is the inner oscillation between trust and distrust. Grace is received through faith (Eph 2:8). For Session D: do the 3 co-occurring verses show grace encountering the doubting person — and if so, does grace precede the resolution of doubt (grace given to the doubter) or follow it (doubt must resolve before grace is received)? Connects to the faith question (SD006) and to Dan 9:23 (grace responding before the plea is complete — SD028).

#### DIM-068-SD016

> Anointing (Reg 6, C16) and blessing (Reg 194, C16) cooccurrence: 7 verses each. Grace co-occurs with both C16 registries at the same level, suggesting a possible C16-C17 connection zone. Anointing, blessing, and grace may constitute a semantic network of divine bestowal — each naming a distinct modality through which the divine disposition of favour is concretely extended to the creature. Session D should examine whether grace, anointing, and blessing share a common inner-being ground (the creature as recipient of divine favour) and what distinguishes them: grace as relational disposition freely given; blessing as the concrete content of what is given; anointing as the specific act of set-apart conferral.

#### PH2-068-001

> Grace-Forgiveness formal connection: G5483 charizō carries both 'give grace' and 'forgive/cancel debt' as primary senses. Eph 4:32 makes forgiveness the named expression of grace received. The grace-forgiveness relationship is formally embedded in the Greek term itself. Requires cross-registry analysis when forgiveness registry is complete.

#### PH2-068-002

> Grace-Chesed boundary question: H2580 chen and chesed (steadfast love) travel together in OT formulas. Key structural question: does chen name the inner disposition of which chesed is the sustained relational expression? Cannot be resolved within this registry.

#### PH2-068-003

> Grace-Repentance sequence: Zec 12:10 (H8469 anchor) and Joel 2:13 (H2587) establish that grace precedes and enables the turn — the capacity to repent is itself given as grace. Directional sequence requires confirmation against repentance registry data.

#### DIM-068-SD001

> Zec 12:10 is an anchor verse in both 889-001 (chen — divine relational favour) and 890-001 (ta.cha.nun — supplication). The same verse connects: (1) God pouring out a spirit of grace (chen — Relational Disposition, GOD), and (2) the human response of pleas for mercy (ta.cha.nun — Dependence/Creatureliness, HUMAN). This shared anchor encodes the inner-being grammar of grace-response: divine grace-disposition produces the human supplication-orientation. The causal chain — grace outpoured → mourning → supplication — is a structural insight spanning two inner-being characteristics (relational favour and creaturely dependence) within the same registry. Session D should examine whether this chain appears across other C17 registries and whether it constitutes a programmatic inner-being pattern in the divine-human relational cluster.

#### DIM-068-SD018

> charizō carries both the giving sense and the forgiving sense as primary senses of the same term — not metaphorical extension but direct lexical range. The question for Session D: is forgiving a subspecies of giving (the cancellation of debt as a form of free bestowal), or a distinct inner-being act that grace makes possible? Registry 64 (forgiveness) and Registry 68 (grace) share this term's semantic range. When God forgives, is God doing the same inner-being thing as when God gives?

#### DIM-068-SD020

> charis and chairo (to rejoice, be glad) share the lexical root χαρ-. Grace and joy are not merely theologically related — they share a root. Grace is the disposition of one who gives with gladness; receiving grace produces joy as its natural inner response. G5485 (charis) appears as the one shared xref term with rejoicing (Reg 132). For Session D: is there a structural inner-being relationship between grace and joy that the root reveals — grace as the ground of joy, joy as the inner-being response to grace? Does the rejoicing registry encode this root-level connection?

#### DIM-068-SD021

> The four semantic faces of charis suggest a possible sequential inner-being architecture: divine disposition (face 1) → relational standing created in the recipient (face 2) → specific capacity gifted into the person (face 3) → gracious character quality expressed outward (face 4). Grace received at the spirit level becomes standing at the soul level becomes capacity in the person becomes character expressed through conduct. For Session D: does the programme's data across multiple registries support this sequential inner-being model of how grace operates through the inner person? This may be the deepest structural question the grace registry raises.

#### DIM-068-SD024

> The CHEN root family (chen, chanan, chanun, tachanum, techinah, chinnam) spans the giving side (chen — favour, chanan — be gracious), the structural logic (chinnam — for nothing, without cause or cost), and the receiving/appealing side (tachanum/techinah — supplication). The entire root family encodes a complete inner-being grammar: disposition of free giving → logic of uncaused bestowal → creature's posture of appeal. For Session D: does the CHEN root family constitute the most complete encoding in Scripture of the grace-dependence inner-being circuit? H2600 chinnam specifically carries the structural logic that makes grace intelligible: grace is precisely what is given for nothing.

#### DIM-068-SD025

> chen and chesed appear together in Exo 34:6 and other divine character formulas as distinct divine attributes. Proposed semantic distinction from Pass 1: chen = the disposition that opens access (the initial movement of favour); chesed = the loyalty that sustains the relationship once opened. If correct, chen and chesed are sequential inner-being states in the divine-human relational dynamic. For Session D: does the Reg 99 (kindness/chesed) data support this sequential model — chen initiates, chesed sustains? Do the co-occurring verses of grace and kindness (7 verses) encode this pattern?

#### DIM-068-SD026

> Zec 12:10: God pours out 'a spirit of grace and supplication' — the supplication is itself outpoured by God. The act by which the creature acknowledges dependence on grace (supplication) is itself given by grace. The creature cannot supply even the posture of appeal from its own inner resources. For Session D: does this paradox appear across other registries? Does the programme corpus show a pattern where the inner-being response to grace (supplication, repentance, faith, mourning) is itself grace-enabled rather than independently generated? This is the deepest inner-being claim of Zec 12:10.

#### DIM-068-SD027

> Eph 2:7 — 'in the coming ages he might show the immeasurable riches of his grace in kindness toward us.' Grace has a built-in eschatological future-orientation: what has been received is real but partial; the fullness is promised. For Session D: does the eschatological future-orientation of grace appear consistently across the C17 cluster and beyond? Is there a programme-wide pattern where the foundational inner-being characteristics (grace, love, peace, hope) have an eschatological fullness that the present experience anticipates but does not exhaust?

#### DIM-068-SD029

> Rom 8:32 encodes grace as inference: 'He who did not spare his own Son... how will he not also with him graciously give us all things?' The supreme act of grace becomes the ground of inner-being assurance about all subsequent grace — not hoped for but logically inferred. The inner-being state produced is confidence derived from reasoning about what has already happened, not from feeling. For Session D: does the faith registry (Reg 59, cooccurrence 10 verses) carry this inference-structure? Is faith in part the inner act of drawing this grace-inference correctly? Does assurance vocabulary connect to this grace-inference pattern?

#### DIM-068-SD030

> Eph 4:32 places three inner-being states in one verse: grace/forgiveness (charizō), tenderheartedness (eusplanchnos — gut-compassion), and kindness (chrēstos). They are a causal sequence, not parallel virtues: received forgiveness → softened inner person → kindness and forgiveness expressed. eusplanchnos is the inner-being mediating state — the tenderheartedness that grace produces and through which grace flows outward. For Session D: is eusplanchnos (compassion-in-the-inner-parts) the inner-being state that mediates between grace received and grace extended? Does the compassion registry (Reg 23) encode this mediating role?

#### DIM-068-SD031

> Luk 1:28-30 shows the inner-being sequence of grace encountered: grace-announcement → fear → reassurance → receptivity. Fear is the first inner response to grace, not an obstacle to it. The creaturely recognition of the weight of divine favour produces fear before it produces peace. For Session D: does this grace-fear-peace sequence appear broadly across the programme corpus? Does fear vocabulary encode creaturely fear as the appropriate initial inner response to encountering the holy-gracious? Does the peace registry (Reg 117, cooccurrence 10 verses) encode the settled state that follows when fear is resolved by grace-assurance?

#### DIM-068-SD032

> 2Cor 12:9 — grace sufficient in weakness; power made perfect in weakness. Grace does not resolve weakness — it inhabits and operates within it. The inner-being transformation grace produces is not from weakness to strength but from weakness-as-problem to weakness-as-theatre-of-grace. For Session D: does this inhabiting-weakness pattern appear across vulnerability (206), deadness (210), despair (44), distress (51), and anguish (5)? Is there a programme-wide inner-being pattern where extreme creaturely conditions are precisely the conditions most associated with grace rather than its absence? This may be the most counterintuitive structural finding of the registry.

#### DIM-068-SD034

> 1Cor 15:10 — 'by the grace of God I am what I am... I worked harder than any of them, though it was not I, but the grace of God that is with me.' Genuine human effort and grace-as-the-agent of that effort are simultaneously true. The grace-agency paradox is the normal inner-being condition of the person formed by grace. For Session D: does the will registry (Reg 173, cooccurrence 11 verses) carry the other half of this paradox? Does the programme data support a model where grace and will are not competitive but mutually constitutive in the person shaped by grace?

#### DIM-068-SD035

> Rom 5:2 uses prosagōgē — access, approach, admission to a presence — implying a prior state of no-access and a threshold that has been opened. The seeking registry (Reg 140, cooccurrence 40 verses) may encode the movement toward this threshold. For Session D: is the seeking-grace-access sequence (creature seeks → finds access → enters standing) the inner-being grammar of the 40-verse cooccurrence? Does prosagōgē connect structurally to the prayer-access vocabulary in the pray registry (Reg 212, 10 shared terms)? Is grace precisely the relational condition that transforms the threshold from impassable to open?

#### DIM-068-SD038

> Zec 12:10 encodes the complete inner-being sequence of grace received at its deepest: outpoured grace → recognition of the pierced one → mourning → weeping → supplication. The first inner response to the full gift of grace is grief, not gladness. The mourning is the inner-being response of the person who sees clearly what grace has cost. For Session D: does the mourning registry (Reg 113) and weeping registry (Reg 188) encode this grace-produced grief as the deepest inner-being response to grace? Is there a programme-wide pattern where deepest encounters with divine grace produce grief before peace — and where that grief is itself the sign of grace's fullness rather than its absence? This may be the most counterintuitive and important finding of the registry.

#### DIM-068-SD041

> The eye is the systematic somatic encoding of grace in the Hebrew chen corpus: 'found favour in the eyes of...' appears in approximately 20 of 67 chen verses. To find favour is to be seen by the favourable gaze of God or another. Grace as being-beheld by the one whose attention constitutes standing. For Session D: does the somatic vocabulary of the eye connect the grace registry to registries where divine seeing/knowing is thematic (name, Reg 204; calling, Reg 19)? Is there a programme-wide pattern where grace and divine seeing are somatic co-expressions of the same inner-being reality — God's favourable gaze constituting the person's standing before him?

#### DIM-068-SD042

> Joh 1:14 — 'the Word became flesh, full of grace and truth.' The incarnation is the supreme somatic event of the grace registry: divine grace taking bodily form. Grace is not disembodied — at its fullest expression, grace has a body. For Session D: does the incarnation's somatic dimension (flesh as the body grace takes) connect the grace registry to the foundational soul/spirit/body registries (Soul Reg 182, spirit Reg 184, heart Reg 183)? Is the incarnation the programme's paradigm case of spirit-level grace fully and permanently expressed through bodily form — and what does this mean for the inner-being architecture of grace?

#### DIM-068-SD047

> Justice (Reg 98, C13) cooccurrence 7 verses. Grace and justice co-occurring raises the foundational inner-being tension: can a person hold both the inner orientation of justice (giving what is owed) and the inner disposition of grace (giving freely regardless of what is owed) simultaneously? For Session D: do the 7 co-occurring verses show grace and justice as complementary inner-being orientations, as competing ones that require resolution, or as synthetically unified in the person formed by both?

#### DIM-068-SD002

> Seeking (Reg 140) cooccurrence: 40 verses — the strongest cooccurrence signal in the grace registry. Grace and seeking co-occur at a structural level: seeking is the inner-being posture of the creature oriented toward what is outside itself; grace is the disposition of the greater moving toward the lesser. Session D should examine whether seeking is the necessary inner posture through which grace is received, and whether the 40-verse overlap encodes a programmatic inner-being sequence — Dependence/Creatureliness orientation (seeking) meeting divine Relational Disposition (grace).

#### DIM-068-SD004

> Pride (Reg 123) shared anchor 2Cor 12:9 (grace group 888-001 ↔ pride group 26-001): 'my grace is sufficient for you, for my power is made perfect in weakness.' Grace-in-weakness is the structural antithesis of pride. Session D should examine the grace-pride relationship as inner-being opposites: whether the grace corpus consistently appears where human self-sufficiency or pride is the counter-condition, and whether receiving grace requires or produces the inner undoing of the self-elevating orientation.

#### DIM-068-SD005

> Hope (Reg 78) shared anchor Rom 5:2 (grace group 888-002 ↔ hope group 401-001) and cooccurrence 4 verses: 'we have obtained access by faith into this grace in which we stand, and we rejoice in hope of the glory of God.' Grace and hope co-constitute the same inner standing — the condition of the person who stands in grace and lives forward toward what grace promises. Session D should examine whether grace and hope are structurally linked as co-features of a single inner-being condition, and how the standing-in-grace (present) and rejoicing-in-hope (future-oriented) relate within that condition.

#### DIM-068-SD006

> Faith (Reg 59) cooccurrence 10 verses. Eph 2:8 is programmatic: 'by grace you have been saved through faith' — grace as sphere, faith as channel. Session D should examine the inner-being architecture of the grace-faith relationship: whether grace and faith are distinguishable inner-being states operating in a structural sequence (grace precedes as divine disposition; faith responds as human orientation), and whether that sequence is consistently encoded across the 10 co-occurring verses. Also: PH2-068-004 raises the identity-formation question from 1Cor 15:10 which implicates faith alongside grace.

#### DIM-068-SD008

> Vulnerability (Reg 206, C22) and deadness (Reg 210, C21) both share all 3 grace dimensions and cooccur at 4 and 7 verses respectively. The Eph 2:1-5 pattern: 'you were dead in trespasses... but God, rich in mercy... even when we were dead, made us alive.' Grace addresses not merely the guilty person but the incapacitated person — the one without inner resource, dead, vulnerable. Session D should examine whether grace specifically constitutes the inner-being reconstitution of the person in conditions of deadness and vulnerability, and whether this represents the deepest inner-being claim of the grace registry: not favour toward the undeserving, but life toward the dead.

#### DIM-068-SD013

> Love (Reg 103, C17) cooccurrence: 14 verses — strongest within-cluster cooccurrence signal. Both grace and love are Relational Disposition registries centred on divine-to-human disposition with GOD as dominant subject in most groups. Session D should examine the boundary and relationship between love and grace: whether they name the same inner-being characteristic from different angles (love as the disposition; grace as its character of being freely given to the undeserving), whether love is broader and grace is a specific quality of love, or whether they are genuinely distinguishable inner-being realities. The 14 co-occurring verses are the primary data for this question.

#### DIM-068-SD014

> C17 cluster synthesis question: all C17 sibling registries appear in grace's cooccurrence signal — peace (117, 10), kindness (99, 7), compassion (23, 4), mercy (111) via xref, forgiveness (64, 3), fellowship (62, 3), plus love (103, 14 — covered separately). The combined cooccurrence pattern within C17 raises the primary Session D synthesis question for this cluster: what is the inner-being architecture of the relational cluster as a whole? Are grace, mercy, compassion, kindness, peace, love, forgiveness, fellowship, and reconciliation sequential (grace as ground, then the others as expressions), hierarchical (grace as the generative source), or parallel (each naming a distinct face of the same divine-human relational reality)? This question cannot be answered from any single registry — it is Session D's work.

#### DIM-068-SD017

> Mourning (Reg 113, C05) shared anchor Zec 12:10 in both grace groups 889-001 (chen — divine favour) and 890-001 (ta.cha.nun — supplication), and cooccurrence 3 verses. Extends DIM-068-SD001: the Spirit of grace poured out produces mourning (Zec 12:10: 'they shall mourn for him as one mourns for an only child'). The inner-being sequence encoded in this verse is: grace outpoured → mourning → supplication → restoration. Mourning is not the opposite of grace but its first inner response — the deep grief that arises when the one who has been pierced is finally seen. Session D should examine the grace-mourning-supplication chain as a programmatic inner-being sequence and whether it appears more broadly across the C05 (grief/lament) cluster.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `H8469` (2 flag(s))

- **`19`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`22`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G5485` (2 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z
- **`22`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H2580` — 61/67 classified · 4 anchor verse(s)

**Group `889-001`** (15 verses — anchors: Exo 33:17, Zec 12:10)

- **Exo 33:17** 🔵 (✓) *target: favor*
  > Exo 33:17 And the Lord said to Moses , “ This very thing that you have spoken I will do , for you have found favor in my sight , and I know you by name .”
- **Zec 12:10** 🔵 (✓) *target: grace*
  > Zec 12:10 “And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy , so that, when they look on me, on him whom they have pierced , they shall mourn for him, as one mourns for an only child , and weep bitterly over him, as one weeps over a firstborn .
  - notes: FLAG 2 resolved: H2580 occurrence; distinct from H8469 vr_id=167194 in same verse
- **Gen 6:8** (✓) *target: favor*
  > Gen 6:8 But Noah found favor in the eyes of the Lord .
- **Gen 39:21** (✓) *target: favor*
  > Gen 39:21 But the Lord was with Joseph and showed him steadfast love and gave him favor in the sight of the keeper of the prison .
- **Exo 3:21** (✓) *target: favor*
  > Exo 3:21 And I will give this people favor in the sight of the Egyptians ; and when you go , you shall not go empty ,
- **Exo 11:3** (✓) *target: favor*
  > Exo 11:3 And the Lord gave the people favor in the sight of the Egyptians . Moreover , the man Moses was very great in the land of Egypt , in the sight of Pharaoh’s servants and in the sight of the people .
- **Exo 12:36** (✓) *target: favor*
  > Exo 12:36 And the Lord had given the people favor in the sight of the Egyptians , so that they let them have what they asked . Thus they plundered the Egyptians .
- **Exo 33:12** (✓) *target: favor*
  > Exo 33:12 Moses said to the Lord , “ See , you say to me, ‘Bring up this people ,’ but you have not let me know whom you will send with me. Yet you have said , ‘I know you by name , and you have also found favor in my sight .’
- **Exo 33:13** (✓) *target: favor*
  > Exo 33:13 Now therefore, if I have found favor in your sight , please show me now your ways , that I may know you in order to find favor in your sight . Consider too that this nation is your people .”
- **Exo 33:16** (✓) *target: favor*
  > Exo 33:16 For how shall it be known that I have found favor in your sight , I and your people ? Is it not in your going with us, so that we are distinct , I and your people , from every other people on the face of the earth ?”
- **Exo 34:9** (✓) *target: favor*
  > Exo 34:9 And he said , “ If now I have found favor in your sight , O Lord , please let the Lord go in the midst of us, for it is a stiff-necked people , and pardon our iniquity and our sin , and take us for your inheritance .”
- **Psa 84:11** (✓) *target: favor*
  > Psa 84:11 For the Lord God is a sun and shield ; the Lord bestows favor and honor . No good thing does he withhold from those who walk uprightly .
- **Pro 3:34** (✓) *target: favor*
  > Pro 3:34 Toward the scorners he is scornful , but to the humble he gives favor .
- **Jer 31:2** (✓) *target: grace*
  > Jer 31:2 Thus says the Lord : “The people who survived the sword found grace in the wilderness ; when Israel sought for rest ,
- **Zec 4:7** (✓) *target: Grace*
  > Zec 4:7 Who are you , O great mountain ? Before Zerubbabel you shall become a plain . And he shall bring forward the top stone amid shouts of ‘ Grace , grace to it !’”

**Group `889-002`** (36 verses — anchors: Rut 2:10)

- **Rut 2:10** 🔵 (✓) *target: favor*
  > Rut 2:10 Then she fell on her face , bowing to the ground , and said to him, “ Why have I found favor in your eyes , that you should take notice of me , since I am a foreigner ?”
- **Gen 18:3** (✓) *target: favor*
  > Gen 18:3 and said , “O Lord , if I have found favor in your sight , do not pass by your servant .
- **Gen 19:19** (✓) *target: favor*
  > Gen 19:19 Behold , your servant has found favor in your sight , and you have shown me great kindness in saving my life . But I cannot escape to the hills , lest the disaster overtake me and I die .
- **Gen 30:27** (✓) *target: favor*
  > Gen 30:27 But Laban said to him, “ If I have found favor in your sight , I have learned by divination that the Lord has blessed me because of you .
- **Gen 32:5** (✓) *target: favor in your*
  > Gen 32:5 I have oxen , donkeys , flocks , male servants , and female servants . I have sent to tell my lord , in order that I may find favor in your sight .’”
- **Gen 33:8** (✓) *target: favor*
  > Gen 33:8 Esau said , “ What do you mean by all this company that I met ?” Jacob answered , “ To find favor in the sight of my lord .”
- **Gen 33:10** (✓) *target: favor*
  > Gen 33:10 Jacob said , “ No , please , if I have found favor in your sight , then accept my present from my hand . For I have seen your face , which is like seeing the face of God , and you have accepted me .
- **Gen 33:15** (✓) *target: favor*
  > Gen 33:15 So Esau said , “ Let me leave with you some of the people who are with me.” But he said , “ What need is there ? Let me find favor in the sight of my lord .”
- **Gen 34:11** (✓) *target: favor*
  > Gen 34:11 Shechem also said to her father and to her brothers , “Let me find favor in your eyes , and whatever you say to me I will give .
- **Gen 39:4** (✓) *target: favor*
  > Gen 39:4 So Joseph found favor in his sight and attended him, and he made him overseer of his house and put him in charge of all that he had .
- **Gen 47:25** (✓) *target: please*
  > Gen 47:25 And they said , “You have saved our lives ; may it please my lord , we will be servants to Pharaoh .”
- **Gen 47:29** (✓) *target: favor*
  > Gen 47:29 And when the time drew near that Israel must die , he called his son Joseph and said to him, “ If now I have found favor in your sight , put your hand under my thigh and promise to deal kindly and truly with me. Do not bury me in Egypt ,
- **Gen 50:4** (✓) *target: favor*
  > Gen 50:4 And when the days of weeping for him were past , Joseph spoke to the household of Pharaoh , saying , “ If now I have found favor in your eyes , please speak in the ears of Pharaoh , saying ,
- **Num 11:11** (✓) *target: favor*
  > Num 11:11 Moses said to the Lord , “ Why have you dealt ill with your servant ? And why have I not found favor in your sight , that you lay the burden of all this people on me ?
- **Num 11:15** (✓) *target: favor*
  > Num 11:15 If you will treat me like this, kill me at once , if I find favor in your sight , that I may not see my wretchedness .”
- **Num 32:5** (✓) *target: favor*
  > Num 32:5 And they said , “ If we have found favor in your sight , let this land be given to your servants for a possession . Do not take us across the Jordan .”
- **Deu 24:1** (✓) *target: favor*
  > Deu 24:1 “When a man takes a wife and marries her, if then she finds no favor in his eyes because he has found some indecency in her, and he writes her a certificate of divorce and puts it in her hand and sends her out of his house , and she departs out of his house,
- **Judg 6:17** (✓) *target: favor*
  > Judg 6:17 And he said to him, “ If now I have found favor in your eyes , then show me a sign that it is you who speak with me .
- **Rut 2:2** (✓) *target: favor*
  > Rut 2:2 And Ruth the Moabite said to Naomi , “ Let me go to the field and glean among the ears of grain after him in whose sight I shall find favor .” And she said to her, “ Go , my daughter .”
- **Rut 2:13** (✓) *target: favor*
  > Rut 2:13 Then she said , “I have found favor in your eyes , my lord , for you have comforted me and spoken kindly to your servant , though I am not one of your servants .”
- **1Sa 1:18** (✓) *target: favor*
  > 1Sa 1:18 And she said , “Let your servant find favor in your eyes .” Then the woman went her way and ate , and her face was no longer sad.
- **1Sa 16:22** (✓) *target: favor*
  > 1Sa 16:22 And Saul sent to Jesse , saying , “Let David remain in my service , for he has found favor in my sight .”
- **1Sa 20:3** (✓) *target: favor*
  > 1Sa 20:3 But David vowed again , saying , “Your father knows well that I have found favor in your eyes , and he thinks , ‘Do not let Jonathan know this , lest he be grieved .’ But truly , as the Lord lives and as your soul lives , there is but a step between me and death .”
- **1Sa 20:29** (✓) *target: favor*
  > 1Sa 20:29 He said , ‘Let me go , for our clan holds a sacrifice in the city , and my brother has commanded me to be there. So now , if I have found favor in your eyes , let me get away and see my brothers .’ For this reason he has not come to the king’s table .”
- **1Sa 25:8** (✓) *target: favor*
  > 1Sa 25:8 Ask your young men , and they will tell you. Therefore let my young men find favor in your eyes , for we come on a feast day . Please give whatever you have at hand to your servants and to your son David .’”
- **1Sa 27:5** (✓) *target: favor*
  > 1Sa 27:5 Then David said to Achish , “ If I have found favor in your eyes , let a place be given me in one of the country towns , that I may dwell there . For why should your servant dwell in the royal city with you ?”
- **2Sa 14:22** (✓) *target: favor*
  > 2Sa 14:22 And Joab fell on his face to the ground and paid homage and blessed the king . And Joab said , “ Today your servant knows that I have found favor in your sight , my lord the king , in that the king has granted the request of his servant .”
- **2Sa 15:25** (✓) *target: favor*
  > 2Sa 15:25 Then the king said to Zadok , “ Carry the ark of God back into the city . If I find favor in the eyes of the Lord , he will bring me back and let me see both it and his dwelling place .
- **2Sa 16:4** (✓) *target: favor*
  > 2Sa 16:4 Then the king said to Ziba , “ Behold , all that belonged to Mephibosheth is now yours.” And Ziba said , “I pay homage ; let me ever find favor in your sight , my lord the king .”
- **1Ki 11:19** (✓) *target: favor*
  > 1Ki 11:19 And Hadad found great favor in the sight of Pharaoh , so that he gave him in marriage the sister of his own wife , the sister of Tahpenes the queen .
- **Est 2:15** (✓) *target: favor*
  > Est 2:15 When the turn came for Esther the daughter of Abihail the uncle of Mordecai , who had taken her as his own daughter , to go in to the king , she asked for nothing except what Hegai the king’s eunuch , who had charge of the women , advised . Now Esther was winning favor in the eyes of all who saw her .
- **Est 2:17** (✓) *target: grace*
  > Est 2:17 the king loved Esther more than all the women , and she won grace and favor in his sight more than all the virgins , so that he set the royal crown on her head and made her queen instead of Vashti .
- **Est 5:2** (✓) *target: favor*
  > Est 5:2 And when the king saw Queen Esther standing in the court , she won favor in his sight , and he held out to Esther the golden scepter that was in his hand . Then Esther approached and touched the tip of the scepter .
- **Est 5:8** (✓) *target: favor*
  > Est 5:8 If I have found favor in the sight of the king , and if it please the king to grant my wish and fulfill my request , let the king and Haman come to the feast that I will prepare for them, and tomorrow I will do as the king has said .”
- **Est 7:3** (✓) *target: favor*
  > Est 7:3 Then Queen Esther answered , “ If I have found favor in your sight , O king , and if it please the king , let my life be granted me for my wish , and my people for my request .
- **Est 8:5** (✓) *target: favor*
  > Est 8:5 And she said , “ If it please the king , and if I have found favor in his sight , and if the thing seems right before the king , and I am pleasing in his eyes , let an order be written to revoke the letters devised by Haman the Agagite , the son of Hammedatha , which he wrote to destroy the Jews who are in all the provinces of the king .

**Group `889-003`** (10 verses — anchors: Pro 31:30)

- **Pro 31:30** 🔵 (✓) *target: Charm*
  > Pro 31:30 Charm is deceitful , and beauty is vain , but a woman who fears the Lord is to be praised .
- **Psa 45:2** (✓) *target: grace*
  > Psa 45:2 You are the most handsome of the sons of men ; grace is poured upon your lips ; therefore God has blessed you forever .
- **Pro 3:4** (✓) *target: favor*
  > Pro 3:4 So you will find favor and good success in the sight of God and man .
- **Pro 11:16** (✓) *target: gracious*
  > Pro 11:16 A gracious woman gets honor , and violent men get riches .
- **Pro 13:15** (✓) *target: favor*
  > Pro 13:15 Good sense wins favor , but the way of the treacherous is their ruin .
- **Pro 17:8** (✓) *target: magic*
  > Pro 17:8 A bribe is like a magic stone in the eyes of the one who gives it; wherever he turns he prospers .
- **Pro 22:1** (✓) *target: favor*
  > Pro 22:1 A good name is to be chosen rather than great riches , and favor is better than silver or gold .
- **Pro 22:11** (✓) *target: gracious*
  > Pro 22:11 He who loves purity of heart , and whose speech is gracious , will have the king as his friend .
- **Pro 28:23** (✓) *target: favor*
  > Pro 28:23 Whoever rebukes a man will afterward find more favor than he who flatters with his tongue .
- **Ecc 10:12** (✓) *target: favor*
  > Ecc 10:12 The words of a wise man’s mouth win him favor , but the lips of a fool consume him .

**Group `UNCLASSIFIED`** (6 verses)

- **Pro 1:9** (—) *target: graceful*
  > Pro 1:9 for they are a graceful garland for your head and pendants for your neck .
- **Pro 3:22** (—) *target: adornment*
  > Pro 3:22 and they will be life for your soul and adornment for your neck .
- **Pro 4:9** (—) *target: graceful*
  > Pro 4:9 She will place on your head a graceful garland ; she will bestow on you a beautiful crown .”
- **Pro 5:19** (—) *target: graceful*
  > Pro 5:19 a lovely deer , a graceful doe . Let her breasts fill you at all times with delight; be intoxicated always in her love .
- **Ecc 9:11** (—) *target: favor*
  > Ecc 9:11 Again I saw that under the sun the race is not to the swift , nor the battle to the strong , nor bread to the wise , nor riches to the intelligent , nor favor to those with knowledge , but time and chance happen to them all .
- **Nah 3:4** (—) *target: graceful*
  > Nah 3:4 And all for the countless whorings of the prostitute , graceful and of deadly charms , who betrays nations with her whorings , and peoples with her charms .

### `H8469` — 18/18 classified · 2 anchor verse(s)

**Group `890-001`** (18 verses — anchors: Dan 9:3, Zec 12:10)

- **Dan 9:3** 🔵 (✓) *target: pleas*
  > Dan 9:3 Then I turned my face to the Lord God , seeking him by prayer and pleas for mercy with fasting and sackcloth and ashes .
- **Zec 12:10** 🔵 (✓) *target: pleas for mercy*
  > Zec 12:10 “And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy , so that, when they look on me, on him whom they have pierced , they shall mourn for him, as one mourns for an only child , and weep bitterly over him, as one weeps over a firstborn .
  - notes: FLAG 2 resolved: H8469 occurrence; distinct from H2580 vr_id=167055 in same verse
- **2Ch 6:21** (✓) *target: pleas*
  > 2Ch 6:21 And listen to the pleas of your servant and of your people Israel , when they pray toward this place . And listen from heaven your dwelling place , and when you hear , forgive .
- **Job 41:3** (✓) *target: pleas*
  > Job 41:3 Will he make many pleas to you? Will he speak to you soft words?
- **Psa 28:2** (✓) *target: pleas*
  > Psa 28:2 Hear the voice of my pleas for mercy, when I cry to you for help, when I lift up my hands toward your most holy sanctuary .
- **Psa 28:6** (✓) *target: pleas*
  > Psa 28:6 Blessed be the Lord ! For he has heard the voice of my pleas for mercy.
- **Psa 31:22** (✓) *target: pleas*
  > Psa 31:22 I had said in my alarm , “ I am cut off from your sight .” But you heard the voice of my pleas for mercy when I cried to you for help.
- **Psa 86:6** (✓) *target: grace*
  > Psa 86:6 Give ear , O Lord , to my prayer ; listen to my plea for grace .
- **Psa 116:1** (✓) *target: pleas for mercy*
  > Psa 116:1 I love the Lord , because he has heard my voice and my pleas for mercy .
- **Psa 130:2** (✓) *target: pleas for mercy*
  > Psa 130:2 O Lord , hear my voice ! Let your ears be attentive to the voice of my pleas for mercy !
- **Psa 140:6** (✓) *target: pleas for mercy*
  > Psa 140:6 I say to the Lord , You are my God ; give ear to the voice of my pleas for mercy , O Lord !
- **Psa 143:1** (✓) *target: pleas for mercy*
  > A Psalm of David . Psa 143:1 Hear my prayer , O Lord ; give ear to my pleas for mercy ! In your faithfulness answer me, in your righteousness !
- **Pro 18:23** (✓) *target: entreaties*
  > Pro 18:23 The poor use entreaties , but the rich answer roughly .
- **Jer 3:21** (✓) *target: pleading*
  > Jer 3:21 A voice on the bare heights is heard , the weeping and pleading of Israel’s sons because they have perverted their way ; they have forgotten the Lord their God .
- **Jer 31:9** (✓) *target: pleas for mercy*
  > Jer 31:9 With weeping they shall come , and with pleas for mercy I will lead them back, I will make them walk by brooks of water , in a straight path in which they shall not stumble , for I am a father to Israel , and Ephraim is my firstborn .
- **Dan 9:17** (✓) *target: pleas for mercy*
  > Dan 9:17 Now therefore, O our God , listen to the prayer of your servant and to his pleas for mercy , and for your own sake , O Lord , make your face to shine upon your sanctuary , which is desolate .
- **Dan 9:18** (✓) *target: pleas*
  > Dan 9:18 O my God , incline your ear and hear . Open your eyes and see our desolations , and the city that is called by your name . For we do not present our pleas before you because of our righteousness , but because of your great mercy .
- **Dan 9:23** (✓) *target: pleas for mercy*
  > Dan 9:23 At the beginning of your pleas for mercy a word went out , and I have come to tell it to you, for you are greatly loved . Therefore consider the word and understand the vision .

### `G5483` — 15/19 classified · 2 anchor verse(s)

**Group `5470-001`** (7 verses — anchors: Rom 8:32)

- **Rom 8:32** 🔵 (✓) *target: graciously give*
  > Rom 8:32 He who did not spare his own Son but gave him up for us all , how will he not also with him graciously give us all things?
- **Act 27:24** (✓) *target: granted*
  > Act 27:24 and he said , ‘Do not be afraid , Paul ; you must stand before Caesar . And behold , God has granted you all those who sail with you .’
- **1Cor 2:12** (✓) *target: freely given*
  > 1Cor 2:12 Now we have received not the spirit of the world , but the Spirit who is from God , that we might understand the things freely given us by God .
- **Gal 3:18** (✓) *target: gave*
  > Gal 3:18 For if the inheritance comes by the law , it no longer comes by promise ; but God gave it to Abraham by a promise .
- **Phili 2:9** (✓) *target: bestowed on*
  > Phili 2:9 Therefore God has highly exalted him and bestowed on him the name that is above every name ,
- **Col 2:13** (✓) *target: forgiven*
  > Col 2:13 And you , who were dead in your trespasses and the uncircumcision of your flesh , God made alive together with him , having forgiven us all our trespasses ,
- **Phile 22** (✓) *target: graciously given*
  > Phile 22 At the same time , prepare a guest room for me , for I am hoping that through your prayers I will be graciously given to you .

**Group `5470-002`** (8 verses — anchors: Eph 4:32)

- **Eph 4:32** 🔵 (✓) *target: forgiving*
  > Eph 4:32 Be kind to one another , tenderhearted , forgiving one another , as God in Christ forgave you .
- **Luk 7:42** (✓) *target: cancelled*
  > Luk 7:42 When they could not pay , he cancelled the debt of both . Now which of them will love him more ?”
- **Luk 7:43** (✓) *target: cancelled*
  > Luk 7:43 Simon answered , “The one, I suppose , for whom he cancelled the larger debt .” And he said to him , “You have judged rightly .”
- **2Cor 2:7** (✓) *target: forgive*
  > 2Cor 2:7 so you should rather turn to forgive and comfort him, or he may be overwhelmed by excessive sorrow .
- **2Cor 2:10** (✓) *target: forgive*
  > 2Cor 2:10 Anyone whom you forgive , I also forgive. Indeed , what I have forgiven , if I have forgiven anything , has been for your sake in the presence of Christ ,
- **2Cor 12:13** (✓) *target: Forgive*
  > 2Cor 12:13 For in what were you less favored than the rest of the churches , except that I myself did not burden you ? Forgive me this wrong !
- **Phili 1:29** (✓) *target: granted*
  > Phili 1:29 For it has been granted to you that for the sake of Christ you should not only believe in him but also suffer for his sake ,
- **Col 3:13** (✓) *target: forgiving*
  > Col 3:13 bearing with one another and , if one has a complaint against another , forgiving each other ; as the Lord has forgiven you , so you also must forgive.

**Group `UNCLASSIFIED`** (4 verses)

- **Luk 7:21** (—) *target: bestowed*
  > Luk 7:21 In that hour he healed many people of diseases and plagues and evil spirits , and on many who were blind he bestowed sight .
- **Act 3:14** (—) *target: granted*
  > Act 3:14 But you denied the Holy and Righteous One, and asked for a murderer to be granted to you ,
- **Act 25:11** (—) *target: give*
  > Act 25:11 If then I am a wrongdoer and have committed anything for which I deserve to die , I do not seek to escape death . But if there is nothing to their charges against me , no one can give me up to them . I appeal to Caesar .”
- **Act 25:16** (—) *target: give up*
  > Act 25:16 I answered them that it was not the custom of the Romans to give up anyone before the accused met the accusers face to face and had opportunity to make his defense concerning the charge laid against him .

### `G5485` — 84/88 classified · 6 anchor verse(s)

**Group `888-001`** (22 verses — anchors: 2Cor 12:9, Eph 2:8)

- **2Cor 12:9** 🔵 (✓) *target: grace*
  > 2Cor 12:9 But he said to me , “ My grace is sufficient for you , for my power is made perfect in weakness .” Therefore I will boast all the more gladly of my weaknesses , so that the power of Christ may rest upon me .
- **Eph 2:8** 🔵 (✓) *target: grace*
  > Eph 2:8 For by grace you have been saved through faith . And this is not your own doing; it is the gift of God ,
- **Joh 1:14** (✓) *target: grace*
  > Joh 1:14 And the Word became flesh and dwelt among us , and we have seen his glory , glory as of the only Son from the Father , full of grace and truth .
- **Joh 1:16** (✓) *target: grace*
  > Joh 1:16 For from his fullness we have all received , grace upon grace .
- **Joh 1:17** (✓) *target: grace*
  > Joh 1:17 For the law was given through Moses ; grace and truth came through Jesus Christ .
- **Rom 3:24** (✓) *target: grace*
  > Rom 3:24 and are justified by his grace as a gift, through the redemption that is in Christ Jesus ,
- **Rom 4:4** (✓) *target: gift*
  > Rom 4:4 Now to the one who works , his wages are not counted as a gift but as his due .
- **Rom 4:16** (✓) *target: grace*
  > Rom 4:16 That is why it depends on faith , in order that the promise may rest on grace and be guaranteed to all his offspring — not only to the adherent of the law but also to the one who shares the faith of Abraham , who is the father of us all ,
- **Rom 5:15** (✓) *target: grace*
  > Rom 5:15 But the free gift is not like the trespass . For if many died through one man’s trespass , much more have the grace of God and the free gift by the grace of that one man Jesus Christ abounded for many .
- **Rom 5:17** (✓) *target: grace*
  > Rom 5:17 For if , because of one man’s trespass , death reigned through that one man, much more will those who receive the abundance of grace and the free gift of righteousness reign in life through the one man Jesus Christ .
- **Rom 5:20** (✓) *target: grace*
  > Rom 5:20 Now the law came in to increase the trespass , but where sin increased , grace abounded all the more ,
- **Rom 5:21** (✓) *target: grace*
  > Rom 5:21 so that , as sin reigned in death , grace also might reign through righteousness leading to eternal life through Jesus Christ our Lord .
- **Rom 11:5** (✓) *target: grace*
  > Rom 11:5 So too at the present time there is a remnant , chosen by grace .
- **Rom 11:6** (✓) *target: grace*
  > Rom 11:6 But if it is by grace , it is no longer on the basis of works ; otherwise grace would no longer be grace .
- **Gal 1:15** (✓) *target: grace*
  > Gal 1:15 But when he who had set me apart before I was born , and who called me by his grace ,
- **Gal 2:21** (✓) *target: grace*
  > Gal 2:21 I do not nullify the grace of God , for if righteousness were through the law , then Christ died for no purpose .
- **Gal 5:4** (✓) *target: grace*
  > Gal 5:4 You are severed from Christ , you who would be justified by the law ; you have fallen away from grace .
- **Eph 1:6** (✓) *target: grace*
  > Eph 1:6 to the praise of his glorious grace , with which he has blessed us in the Beloved .
- **Eph 1:7** (✓) *target: grace*
  > Eph 1:7 In him we have redemption through his blood , the forgiveness of our trespasses , according to the riches of his grace ,
- **Eph 2:5** (✓) *target: grace*
  > Eph 2:5 even when we were dead in our trespasses , made us alive together with Christ — by grace you have been saved —
- **Eph 2:7** (✓) *target: grace*
  > Eph 2:7 so that in the coming ages he might show the immeasurable riches of his grace in kindness toward us in Christ Jesus .
- **Eph 3:2** (✓) *target: grace*
  > Eph 3:2 assuming that you have heard of the stewardship of God’s grace that was given to me for you ,

**Group `888-002`** (13 verses — anchors: Rom 5:2, 1Cor 15:10)

- **Rom 5:2** 🔵 (✓) *target: grace*
  > Rom 5:2 Through him we have also obtained access by faith into this grace in which we stand , and we rejoice in hope of the glory of God .
- **1Cor 15:10** 🔵 (✓) *target: grace*
  > 1Cor 15:10 But by the grace of God I am what I am , and his grace toward me was not in vain . On the contrary , I worked harder than any of them , though it was not I , but the grace of God that is with me .
- **Rom 6:1** (✓) *target: grace*
  > Rom 6:1 What shall we say then ? Are we to continue in sin that grace may abound ?
- **Rom 6:14** (✓) *target: grace*
  > Rom 6:14 For sin will have no dominion over you , since you are not under law but under grace .
- **Rom 6:15** (✓) *target: grace*
  > Rom 6:15 What then ? Are we to sin because we are not under law but under grace ? By no means !
- **Rom 6:17** (✓) *target: thanks*
  > Rom 6:17 But thanks be to God , that you who were once slaves of sin have become obedient from the heart to the standard of teaching to which you were committed ,
- **Rom 12:3** (✓) *target: grace*
  > Rom 12:3 For by the grace given to me I say to everyone among you not to think of himself more highly than he ought to think , but to think with sober judgment , each according to the measure of faith that God has assigned .
- **Rom 12:6** (✓) *target: grace*
  > Rom 12:6 Having gifts that differ according to the grace given to us , let us use them: if prophecy , in proportion to our faith ;
- **2Cor 1:12** (✓) *target: grace*
  > 2Cor 1:12 For our boast is this , the testimony of our conscience , that we behaved in the world with simplicity and godly sincerity , not by earthly wisdom but by the grace of God , and supremely so toward you .
- **2Cor 6:1** (✓) *target: grace*
  > 2Cor 6:1 Working together with him, then , we appeal to you not to receive the grace of God in vain .
- **Gal 1:6** (✓) *target: grace*
  > Gal 1:6 I am astonished that you are so quickly deserting him who called you in the grace of Christ and are turning to a different gospel —
- **Gal 2:9** (✓) *target: grace*
  > Gal 2:9 and when James and Cephas and John , who seemed to be pillars , perceived the grace that was given to me , they gave the right hand of fellowship to Barnabas and me , that we should go to the Gentiles and they to the circumcised .
- **Gal 6:18** (✓) *target: grace*
  > Gal 6:18 The grace of our Lord Jesus Christ be with your spirit , brothers . Amen .

**Group `888-003`** (13 verses — anchors: Luk 1:30)

- **Luk 1:30** 🔵 (✓) *target: favor*
  > Luk 1:30 And the angel said to her , “Do not be afraid , Mary , for you have found favor with God .
- **Luk 2:40** (✓) *target: favor*
  > Luk 2:40 And the child grew and became strong , filled with wisdom . And the favor of God was upon him .
- **Luk 2:52** (✓) *target: favor*
  > Luk 2:52 And Jesus increased in wisdom and in stature and in favor with God and man .
- **Luk 4:22** (✓) *target: gracious*
  > Luk 4:22 And all spoke well of him and marveled at the gracious words that were coming from his mouth . And they said , “ Is not this Joseph’s son ?”
- **Luk 6:32** (✓) *target: benefit*
  > Luk 6:32 “ If you love those who love you , what benefit is that to you ? For even sinners love those who love them .
- **Luk 6:33** (✓) *target: benefit*
  > Luk 6:33 And if you do good to those who do good to you , what benefit is that to you ? For even sinners do the same .
- **Luk 6:34** (✓) *target: credit*
  > Luk 6:34 And if you lend to those from whom you expect to receive , what credit is that to you ? Even sinners lend to sinners , to get back the same amount .
- **Act 2:47** (✓) *target: favor*
  > Act 2:47 praising God and having favor with all the people . And the Lord added to their number day by day those who were being saved .
- **Act 4:33** (✓) *target: grace*
  > Act 4:33 And with great power the apostles were giving their testimony to the resurrection of the Lord Jesus , and great grace was upon them all .
- **Act 6:8** (✓) *target: grace*
  > Act 6:8 And Stephen , full of grace and power , was doing great wonders and signs among the people .
- **Act 7:10** (✓) *target: favor*
  > Act 7:10 and rescued him out of all his afflictions and gave him favor and wisdom before Pharaoh , king of Egypt , who made him ruler over Egypt and over all his household .
- **Act 7:46** (✓) *target: favor*
  > Act 7:46 who found favor in the sight of God and asked to find a dwelling place for the God of Jacob .
- **Act 11:23** (✓) *target: grace*
  > Act 11:23 When he came and saw the grace of God , he was glad , and he exhorted them all to remain faithful to the Lord with steadfast purpose ,

**Group `888-004`** (36 verses — anchors: Act 20:32)

- **Act 20:32** 🔵 (✓) *target: grace*
  > Act 20:32 And now I commend you to God and to the word of his grace , which is able to build you up and to give you the inheritance among all those who are sanctified .
- **Act 13:43** (✓) *target: grace*
  > Act 13:43 And after the meeting of the synagogue broke up , many Jews and devout converts to Judaism followed Paul and Barnabas , who , as they spoke with them , urged them to continue in the grace of God .
- **Act 14:3** (✓) *target: grace*
  > Act 14:3 So they remained for a long time , speaking boldly for the Lord , who bore witness to the word of his grace , granting signs and wonders to be done by their hands .
- **Act 14:26** (✓) *target: grace*
  > Act 14:26 and from there they sailed to Antioch , where they had been commended to the grace of God for the work that they had fulfilled .
- **Act 15:11** (✓) *target: grace*
  > Act 15:11 But we believe that we will be saved through the grace of the Lord Jesus , just as they will.”
- **Act 15:40** (✓) *target: grace*
  > Act 15:40 but Paul chose Silas and departed , having been commended by the brothers to the grace of the Lord .
- **Act 18:27** (✓) *target: grace*
  > Act 18:27 And when he wished to cross to Achaia , the brothers encouraged him and wrote to the disciples to welcome him . When he arrived , he greatly helped those who through grace had believed ,
- **Act 20:24** (✓) *target: grace*
  > Act 20:24 But I do not account my life of any value nor as precious to myself , if only I may finish my course and the ministry that I received from the Lord Jesus , to testify to the gospel of the grace of God .
- **Rom 1:5** (✓) *target: grace*
  > Rom 1:5 through whom we have received grace and apostleship to bring about the obedience of faith for the sake of his name among all the nations ,
- **Rom 1:7** (✓) *target: Grace*
  > Rom 1:7 To all those in Rome who are loved by God and called to be saints : Grace to you and peace from God our Father and the Lord Jesus Christ .
- **Rom 15:15** (✓) *target: grace*
  > Rom 15:15 But on some points I have written to you very boldly by way of reminder , because of the grace given me by God
- **Rom 16:20** (✓) *target: grace*
  > Rom 16:20 The God of peace will soon crush Satan under your feet . The grace of our Lord Jesus Christ be with you .
- **1Cor 1:3** (✓) *target: Grace*
  > 1Cor 1:3 Grace to you and peace from God our Father and the Lord Jesus Christ .
- **1Cor 1:4** (✓) *target: grace*
  > 1Cor 1:4 I give thanks to my God always for you because of the grace of God that was given you in Christ Jesus ,
- **1Cor 3:10** (✓) *target: grace*
  > 1Cor 3:10 According to the grace of God given to me , like a skilled master builder I laid a foundation , and someone else is building upon it. Let each one take care how he builds upon it.
- **1Cor 10:30** (✓) *target: thankfulness*
  > 1Cor 10:30 If I partake with thankfulness , why am I denounced because of that for which I give thanks ?
- **1Cor 15:57** (✓) *target: thanks*
  > 1Cor 15:57 But thanks be to God , who gives us the victory through our Lord Jesus Christ .
- **1Cor 16:3** (✓) *target: gift*
  > 1Cor 16:3 And when I arrive , I will send those whom you accredit by letter to carry your gift to Jerusalem .
- **1Cor 16:23** (✓) *target: grace*
  > 1Cor 16:23 The grace of the Lord Jesus be with you .
- **2Cor 1:2** (✓) *target: Grace*
  > 2Cor 1:2 Grace to you and peace from God our Father and the Lord Jesus Christ .
- **2Cor 1:15** (✓) *target: grace*
  > 2Cor 1:15 Because I was sure of this , I wanted to come to you first , so that you might have a second experience of grace .
- **2Cor 2:14** (✓) *target: thanks*
  > 2Cor 2:14 But thanks be to God , who in Christ always leads us in triumphal procession , and through us spreads the fragrance of the knowledge of him everywhere .
- **2Cor 4:15** (✓) *target: grace*
  > 2Cor 4:15 For it is all for your sake , so that as grace extends to more and more people it may increase thanksgiving , to the glory of God .
- **2Cor 8:1** (✓) *target: grace*
  > 2Cor 8:1 We want you to know , brothers , about the grace of God that has been given among the churches of Macedonia ,
- **2Cor 8:4** (✓) *target: favor*
  > 2Cor 8:4 begging us earnestly for the favor of taking part in the relief of the saints —
- **2Cor 8:6** (✓) *target: grace*
  > 2Cor 8:6 Accordingly , we urged Titus that as he had started , so he should complete among you this act of grace .
- **2Cor 8:7** (✓) *target: grace*
  > 2Cor 8:7 But as you excel in everything —in faith , in speech , in knowledge , in all earnestness , and in our love for you — see that you excel in this act of grace also .
- **2Cor 8:9** (✓) *target: grace*
  > 2Cor 8:9 For you know the grace of our Lord Jesus Christ , that though he was rich , yet for your sake he became poor , so that you by his poverty might become rich .
- **2Cor 8:16** (✓) *target: thanks*
  > 2Cor 8:16 But thanks be to God , who put into the heart of Titus the same earnest care I have for you .
- **2Cor 8:19** (✓) *target: grace*
  > 2Cor 8:19 And not only that, but he has been appointed by the churches to travel with us as we carry out this act of grace that is being ministered by us , for the glory of the Lord himself and to show our good will .
- **2Cor 9:8** (✓) *target: grace*
  > 2Cor 9:8 And God is able to make all grace abound to you , so that having all sufficiency in all things at all times , you may abound in every good work .
- **2Cor 9:14** (✓) *target: grace*
  > 2Cor 9:14 while they long for you and pray for you , because of the surpassing grace of God upon you .
- **2Cor 9:15** (✓) *target: Thanks*
  > 2Cor 9:15 Thanks be to God for his inexpressible gift !
- **2Cor 13:14** (✓) *target: grace*
  > 2Cor 13:14 The grace of the Lord Jesus Christ and the love of God and the fellowship of the Holy Spirit be with you all .
- **Gal 1:3** (✓) *target: Grace*
  > Gal 1:3 Grace to you and peace from God our Father and the Lord Jesus Christ ,
- **Eph 1:2** (✓) *target: Grace*
  > Eph 1:2 Grace to you and peace from God our Father and the Lord Jesus Christ .

**Group `UNCLASSIFIED`** (4 verses)

- **Luk 17:9** (—) *target: thank*
  > Luk 17:9 Does he thank the servant because he did what was commanded ?
- **Act 24:27** (—) *target: favor*
  > Act 24:27 When two years had elapsed , Felix was succeeded by Porcius Festus . And desiring to do the Jews a favor , Felix left Paul in prison .
- **Act 25:3** (—) *target: favor*
  > Act 25:3 asking as a favor against Paul that he summon him to Jerusalem —because they were planning an ambush to kill him on the way .
- **Act 25:9** (—) *target: favor*
  > Act 25:9 But Festus , wishing to do the Jews a favor , said to Paul , “Do you wish to go up to Jerusalem and there be tried on these charges before me ?”

### `G5487` — 2/2 classified · 1 anchor verse(s)

**Group `5471-001`** (2 verses — anchors: Luk 1:28)

- **Luk 1:28** 🔵 (✓) *target: favored one*
  > Luk 1:28 And he came to her and said , “ Greetings , O favored one , the Lord is with you !”
- **Eph 1:6** (✓) *target: blessed*
  > Eph 1:6 to the praise of his glorious grace , with which he has blessed us in the Beloved .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**5 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H2580` | favor | `to_revise` | 67 | 3 | 61 |
| `H8469` | supplication | `to_revise` | 18 | 1 | 18 |
| `G5483` | to give grace | `to_revise` | 19 | 2 | 15 |
| `G5485` | grace | `to_revise` | 88 | 4 | 84 |
| `G5487` | to favor | `to_revise` | 2 | 1 | 2 |

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

### Registry-specific questions for 068 grace

_None._ No questions in `wa_obs_question_catalogue` are sourced from registry 68 (grace).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-04-28T06:26:03Z`
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

*End of readiness output v3 — wa-068-grace.*