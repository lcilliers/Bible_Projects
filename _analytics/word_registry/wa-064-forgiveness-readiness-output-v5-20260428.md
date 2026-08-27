# wa-064-forgiveness — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-04-28T06:24:55Z · schema 3.17.0_

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

- **Registry no:** `64` · **word:** `forgiveness`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v1.9-2026-04-09`)
- **cluster_assignment:** `C17`
- **sb_classification:** `Spirit-soul interface`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Relational/Social`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 7  (programme-wide aggregate including XREF and historical terms — current OWNER count is 7, XREF 0)
- `phase1_verse_count`: 190  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 23 unresolved · **Existing session_b_findings:** 1

**Description:**

> Forgiveness is the release of a legitimate claim against someone who has wronged you — the decision not to hold the debt against them, to cancel the account of injury. The Hebrew and Greek vocabulary covers sending away, releasing, covering over. Forgiveness in Scripture is consistently modelled on what God does: he forgives by genuinely releasing the debt, not by pretending the wrong did not happen. Human forgiveness is called for as a response to having been forgiven, and its absence poisons the inner life of the one who withholds it.

**sb_classification_reasoning:**

> Forgiveness at its fullest expression is a spirit-level characteristic — originated in God's own disposition (Psa 86:5), received as a divine act (H5545 exclusively divine subject), capable of producing transformative inner states (love in Luk 7:47; reverential fear in Psa 130:4) that exceed natural capacity. At the practical exercise level it operates as a soul-level decision of the relational will, within human reach when commanded (Luk 17:3-4). The spirit is the source; the soul is the exercise ground. Confidence: Medium.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-04-28T06:24:55Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 7
- **OWNER terms legacy-VC (not_done):** 7 / 7

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 7 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H5545` | sa.lach | to forgive | H | `extracted` | **`to_revise`** | 1 | 45 | 3/0 | 45/0 | 3 |
| `H5546` | sal.lach | forgiving | H | `extracted` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H5547` | se.li.chah | forgiveness | H | `extracted` | **`to_revise`** | 1 | 3 | 1/0 | 3/0 | 1 |
| `G0859` | afesis | forgiveness | G | `extracted` | **`to_revise`** | 1 | 16 | 2/0 | 16/0 | 2 |
| `G0863G` | afiēmi | to release: leave | G | `extracted` | **`to_revise`** | 1 | 66 | 3/0 | 32/0 | 3 |
| `G0863H` | afiēmi | to release: forgive | G | `extracted` | **`to_revise`** | 1 | 37 | 2/0 | 37/0 | 2 |
| `G0863I` | afiēmi | to release: permit | G | `extracted` | **`to_revise`** | 1 | 22 | 2/0 | 18/0 | 2 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H5545` — sa.lach "to forgive"

**Identity:** mti=5379 · ti=5493 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to forgive, pardon

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal) to forgive, pardon
  - `1b` (under `None`): (Niphal) to be forgiven

**Root family:**
- `SALACH` (Hebrew): forgiving — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `H5546` sal.lach "forgiving"
- `H5547` se.li.chah "forgiveness"
- `H5548` sal.khah "Salecah"

### `H5546` — sal.lach "forgiving"

**Identity:** mti=5380 · ti=5494 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: ready to forgive, forgiving

**Root family:**
- `SALACH` (Hebrew): forgiving — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `H5545` sa.lach "to forgive"
- `H5547` se.li.chah "forgiveness"
- `H5548` sal.khah "Salecah"

### `H5547` — se.li.chah "forgiveness"

**Identity:** mti=880 · ti=918 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: forgiveness

**Root family:**
- `SALACH` (Hebrew): forgiving — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `H5545` sa.lach "to forgive"
- `H5546` sal.lach "forgiving"
- `H5548` sal.khah "Salecah"

### `G0859` — afesis "forgiveness"

**Identity:** mti=879 · ti=917 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: forgiveness, pardon, release, cancellation of a debt 
dismission, deliverance, from captivity, Lk. 4:18 (2x); remission, forgiveness, pardon, Mt. 26:28

**Root family:**
- `AFE` (Greek): forgiveness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G0863G` afiēmi "to release: leave"
- `G0863H` afiēmi "to release: forgive"
- `G0863I` afiēmi "to release: permit"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0863G` — afiēmi "to release: leave"

**Identity:** mti=5376 · ti=5490 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to forgive, pardon, remit, cancel; to leave, abandon; to allow, permit, tolerate 
to send away, dismiss, suffer to depart; to emit, send forth;, τὴν φωνήν, the voice, to cry out, utter an exclamation, Mk. 15:37; τὸ πνεῦμα, the spirit, to expire, Mt. 27:50; to omit, pass over or by; to let alone, care not for, Mt. 15:14; 23:23; Heb. 6:1; to permit, suffer, allow, tolerate, let, forbid not; to give up, yield, resign, Mt. 5:40; to remit, forgive, pardon; to relax, suffer to become less intense, Rev. 2:4; to leave, depart from; to desert, abandon, forsake; to leave remaining or alone; to leave behind, i.e. at one's death, Mk. 12:19, 20, 21, 22; Jn. 14:27

**Root family:**
- `AFE` (Greek): forgiveness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0859` afesis "forgiveness"
- `G0863G` afiēmi "to release: leave"
- `G0863H` afiēmi "to release: forgive"
- `G0863I` afiēmi "to release: permit"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0863H` — afiēmi "to release: forgive"

**Identity:** mti=5377 · ti=5491 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to forgive, pardon, remit, cancel; to leave, abandon; to allow, permit, tolerate 
to send away, dismiss, suffer to depart; to emit, send forth;, τὴν φωνήν, the voice, to cry out, utter an exclamation, Mk. 15:37; τὸ πνεῦμα, the spirit, to expire, Mt. 27:50; to omit, pass over or by; to let alone, care not for, Mt. 15:14; 23:23; Heb. 6:1; to permit, suffer, allow, tolerate, let, forbid not; to give up, yield, resign, Mt. 5:40; to remit, forgive, pardon; to relax, suffer to become less intense, Rev. 2:4; to leave, depart from; to desert, abandon, forsake; to leave remaining or alone; to leave behind, i.e. at one's death, Mk. 12:19, 20, 21, 22; Jn. 14:27

**Root family:**
- `AFE` (Greek): forgiveness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0859` afesis "forgiveness"
- `G0863G` afiēmi "to release: leave"
- `G0863H` afiēmi "to release: forgive"
- `G0863I` afiēmi "to release: permit"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0863I` — afiēmi "to release: permit"

**Identity:** mti=5378 · ti=5492 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:12): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to forgive, pardon, remit, cancel; to leave, abandon; to allow, permit, tolerate 
to send away, dismiss, suffer to depart; to emit, send forth;, τὴν φωνήν, the voice, to cry out, utter an exclamation, Mk. 15:37; τὸ πνεῦμα, the spirit, to expire, Mt. 27:50; to omit, pass over or by; to let alone, care not for, Mt. 15:14; 23:23; Heb. 6:1; to permit, suffer, allow, tolerate, let, forbid not; to give up, yield, resign, Mt. 5:40; to remit, forgive, pardon; to relax, suffer to become less intense, Rev. 2:4; to leave, depart from; to desert, abandon, forsake; to leave remaining or alone; to leave behind, i.e. at one's death, Mk. 12:19, 20, 21, 22; Jn. 14:27

**Root family:**
- `AFE` (Greek): forgiveness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0859` afesis "forgiveness"
- `G0863G` afiēmi "to release: leave"
- `G0863H` afiēmi "to release: forgive"
- `G0863I` afiēmi "to release: permit"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (0)

_None._

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H5545` — 3 groups

- **`5379-001`** — 13 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's act of forgiving sin as the outcome of atonement — the cultic and covenantal restoration of the person's standing before God through sacrifice and priestly mediation*
- **`5379-002`** — 17 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C17`
  - *Term names the intercession for divine forgiveness — the act of seeking God's pardon on behalf of oneself or others, and God's response of pardoning or withholding*
- **`5379-003`** — 15 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's promised and proclaimed forgiveness in the new covenant context — the unconditional covenantal act by which God forgives iniquity and remembers sin no more*

### `H5546` — 1 groups

- **`5380-001`** — 1 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names forgiveness as a characteristic attribute of God's inner being — the disposition of readiness to pardon that belongs to his essential goodness and steadfast love*

### `H5547` — 1 groups

- **`880-001`** — 3 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names forgiveness as a divine attribute and possession — a quality that belongs to God's character, that grounds the possibility of the human-divine relationship, and that evokes reverential fear*

### `G0859` — 2 groups

- **`879-001`** — 13 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names forgiveness of sins as the spiritual transaction through which the inner person is released from guilt and restored to right standing before God — received through repentance, faith, and Christ's atoning blood*
- **`879-002`** — 3 relevant · 1 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C17`
  - *Term names the absolute limit of forgiveness — the unforgivable sin against the Holy Spirit, and the conditions under which forgiveness is withheld or inaccessible*

### `G0863G` — 3 groups

- **`5376-001`** — 13 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C17`
  - *Term names the deliberate inner act of leaving — forsaking possessions, family, or prior obligations for the sake of discipleship — as the outward expression of an inner reordering of priorities*
- **`5376-002`** — 9 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the abandonment of what is owed — leaving a spouse, neglecting the weightier matters of the law, or forsaking first love — as an inner failure of loyalty and relational commitment*
- **`5376-003`** — 10 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the relational priority inherent in the leave/stay act — leaving a gift to seek reconciliation first, leaving the many for the one, the Father's not leaving the Son alone*

### `G0863H` — 2 groups

- **`5377-001`** — 26 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names God's act of releasing a person from the guilt and penalty of sin — the vertical forgiveness that restores the inner standing of the person before God*
- **`5377-002`** — 11 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the human act of forgiving another — the horizontal release of an offender from the inner claim of the offended, commanded as the pattern for those who have received divine forgiveness*

### `G0863I` — 2 groups

- **`5378-001`** — 12 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Term names the act of permitting or granting access as an inner-being posture — the receptivity, welcome, or restraint that reflects an inner orientation of priority, reverence, or obedience*
- **`5378-002`** — 6 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Term names the withholding of permission as an act reflecting the inner-being condition of the actor — whether as spiritual authority, obstruction of others, or the inner abandonment of proper orientation*

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
| 73 guilt | 51 |
| 111 mercy | 15 |
| 135 repentance | 12 |
| 59 faith | 9 |
| 187 strength | 9 |
| 197 authority | 9 |
| 103 love | 8 |
| 184 spirit | 7 |
| 43 desire | 6 |
| 147 sin | 5 |
| 23 compassion | 4 |
| 56 envy | 4 |
| 128 rebellion | 4 |
| 149 slander | 4 |
| 204 name | 4 |
| 19 calling | 3 |
| 57 evil | 3 |
| 68 grace | 3 |
| 81 hypocrisy | 3 |
| 122 prayer | 3 |
| 126 purpose | 3 |
| 160 thought | 3 |
| 180 yielding | 3 |
| 182 Soul | 3 |
| 207 blindness (spiritual) | 3 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 73 guilt | Jer 31:34 |
| 103 love | Jer 31:34 |
| 111 mercy | Lev 4:20 |
| 130 reconciliation | Mat 5:24 |
| 147 sin | Mar 3:29 |
| 160 thought | Jer 31:34 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-64-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-11 · **term_id:** -

> Luk 7:47 (anchor for group 5377-001) establishes an explicit inner-being grammar of forgiveness: the quantity of forgiveness received determines the intensity of the inner orientation of love produced — "she loved much because she was forgiven much; he who is forgiven little loves little." This is not merely a motivational claim but an inner-being causal chain: divine forgiveness (vertical release) → inner love-orientation (relational disposition). Session B for Reg 64 should examine whether this causal chain — forgiveness received → love orientation produced — is a recurring inner-being pattern across the forgiveness corpus, and how it relates to the grace-supplication chain already identified in Reg 68 (grace given → supplication produced, from DIM-068 Session C data). The hypothesis: forgiveness and grace both operate as inner-being generators that produce specific downstream inner orientations (love and supplication respectively).

### H.2 Open SD pointers + research flags (23)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `DIMREVIEW_SESSION_D` | DIM-64-SD001 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | DIM-064-SD001 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD005 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD007 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD008 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD009 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD010 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD018 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD019 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD021 | MEDIUM | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD012 | LOW | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD013 | LOW | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD015 | LOW | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD022 | LOW | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD002 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD003 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD004 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD006 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD011 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD014 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD016 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD017 | HIGH | D | 2026-04-12 |
| `SD_POINTER` | DIM-064-SD020 | HIGH | D | 2026-04-12 |

#### DIM-64-SD001

> Group 879-002 (afesis — the unforgivable sin, Mar 3:29) defines the absolute limit of forgiveness. Session D should examine whether the forgiveness vocabulary of Reg 64 encodes a structural polarity: at one end, God's unconditional new-covenant forgiveness that remembers sin no more (5379-003, Jer 31:34); at the other end, the permanent condition of unforgiven guilt (879-002, Mar 3:29). Between these poles, the registry maps the full spectrum of forgiveness experience — cultic atonement, divine mercy, human horizontal forgiveness, intercessory plea. This polarity — absolute forgiveness / absolute non-forgiveness — may be a unique structural feature of the forgiveness vocabulary compared to the other C17 relational registries (compassion, mercy, love) which do not have an analogous absolute limit.

#### DIM-064-SD001

> Luk 5:20 (Mar 2:5 parallel) — when Jesus saw the faith of those who brought the paralytic, he pronounced forgiveness. Corporate faith mediates individual forgiveness in this account. The verse raises the question of whether communal intercession has a structural role in the transmission of forgiveness. This connects to the listen/prayer/intercession function represented by registry 213 (listen, C02). Why cannot this be resolved within registry 064 alone: the forgiveness corpus names the mechanism of the paralytic's healing but not the inner-being structure of corporate faith as a forgiveness-channel. That question requires the listen corpus to be read alongside the forgiveness corpus.

#### DIM-064-SD005

> Acts 26:18 presents a structured inner-being conversion sequence: 'open their eyes, so that they may turn from darkness to light and from the power of Satan to God, that they may receive forgiveness of sins and a place among those who are sanctified by faith.' The sequence is: spiritual blindness → sight → turning → forgiveness of sins → sanctification. This sequence implicates spiritual blindness (207), calling (019), forgiveness (064), and sanctification. Session D question: is this conversion sequence a reproducible inner-being grammar across the NT corpus, and does forgiveness consistently function as a gateway state (received, then leading to further transformation) rather than a terminal one? Cannot be resolved within registry 064 alone.

#### DIM-064-SD007

> The Synoptic forgiveness pronouncements (Luk 5:20-24; Mar 2:5-10; Mat 9:2-6) generate a Christological argument: Jesus claims authority to forgive sins that is challenged as belonging exclusively to God ('who can forgive sins but God alone?' Mar 2:7). Jesus' response is to demonstrate the authority through a healing. The authority to forgive is here presented as equivalent to divine authority. Session D question: does the authority corpus (197, C20) address the relationship between divine authority and the capacity to forgive at scale? Is forgiveness structurally dependent on authority in a way that the C20 analysis should examine? Confirmed by cooccurrence (10 shared verses) and dimension overlap (5). Cannot be resolved within registry 064 alone.

#### DIM-064-SD008

> Mat 6:14-15 establishes a reciprocal relational coherence requirement: 'if you forgive others their trespasses, your heavenly Father will also forgive you; but if you do not forgive others their trespasses, neither will your Father forgive your trespasses.' This is not a simple quid pro quo but a structural congruence condition: the person who occupies the position of one who has been forgiven cannot simultaneously occupy the position of one who refuses to forgive. Session D question: is there a programme-wide pattern where a received inner-being gift (grace, forgiveness) is structured so that its retention requires its exercise? Does this relational-congruence logic appear in the grace, mercy, or love corpora? Cannot be resolved within registry 064 alone — requires cross-registry reading.

#### DIM-064-SD009

> Mar 10:29 (anchor for group 5376-001) — Jesus validates the disciples' act of leaving home, family, and lands for the gospel. The deliberate leaving of what is legitimately held, driven by a higher loyalty, is the same act-structure as forgiveness. The verse places this leaving-act within the discipleship response to calling. Session D question: does the calling corpus (019) address the inner-being cost of the leaving-act as a dimension of vocation — the reordering of attachments that calling requires? Does the volitional dimension of forgiveness connect to the volitional dimension of responding to calling through the shared act-structure of releasing what is legitimately held? Cannot be resolved within registry 064 alone.

#### DIM-064-SD010

> Rev 2:4 (anchor for group 5376-002) — 'you have abandoned the love you had at first.' The Ephesian church maintains orthodox practice and doctrinal vigilance while abandoning first love. This pattern names a potential inner-being dissociation: religious conduct continuing while the relational inner disposition (love, forgiveness) atrophies. The same *aphiēmi* that names forgiveness (right release of a claim) names this wrong release (abandonment of love). Session D question: does the programme's treatment of love (103) and fellowship (062) address the inner-being failure mode of religious formalism — where the relational disposition is lost while religious conduct continues? This is the inner-being dynamic underlying the Pharisee-pattern observed in multiple passages.

#### DIM-064-SD018

> Mar 3:29 — 'whoever blasphemes against the Holy Spirit never has forgiveness, but is guilty of an eternal sin.' The absolute limit of forgiveness names a state in which the characteristic is permanently inaccessible. Session D question: what is the inner-being grammar of the condition for which forgiveness is permanently unavailable? Is it a volitional state (final and irreversible refusal), a cognitive state (final darkening — spiritual blindness, registry 207), or a spiritual state (complete severance from the Spirit — implicating spiritual deadness, registry 210)? The Mar 3:29 verse is shared with sin (147). The inner-being precondition of the unforgivable sin requires cross-registry reading of sin, blindness, deadness, and rebellion (128) to characterise.

#### DIM-064-SD019

> 19 shared verses between forgiveness (064) and strength (187) is the second-highest cooccurrence signal in this registry's corpus. The forgiveness passages frequently invoke divine power, exaltation, and authority in the same context as forgiveness: Acts 5:31 ('God exalted him at his right hand as Leader and Savior to give repentance and forgiveness of sins'), Num 14:19 ('according to the greatness of your steadfast love'). Session D question: does the programme's strength/power cluster (C20) address the relationship between divine omnipotence and the capacity to forgive at the scale Scripture describes? Is there an inner-being statement about divine power embedded in the forgiveness corpus that the C20 synthesis should address? Confirmed by 19 shared verses (strongest unexpected cooccurrence signal in this registry).

#### DIM-064-SD021

> 8 shared verses between forgiveness (064) and desire (043). The leave/abandon groups (5376) contain verses about leaving behind earthly attachments for discipleship — an act that implies a reordering of desire. When forgiveness is extended, the offended party must forgo the inner satisfaction of retained grievance — itself a form of desire (the desire for vindication, the desire for the account to be settled). Session D question: does the desire corpus (043) address the inner-being act of relinquishing a desire as a dimension of forgiveness? When forgiveness requires releasing the satisfaction of the retained claim, is there a desire-level reordering taking place that the programme should map? Confirmed by cooccurrence (8 shared verses).

#### DIM-064-SD012

> Mat 18:35 — 'if you do not forgive your brother from your heart' (*ek tēs kardias*). The heart is named as the required inner locus of genuine forgiveness, distinguishing it from verbal or legal declaration alone. Session D question: does the programme's treatment of heart as an inner-being faculty consistently require heart-level engagement for genuine inner-being acts? Does the forgiveness-from-the-heart qualifier connect structurally to other heart-locus inner-being requirements (love from the heart, obedience from the heart) in a way that Session D should map? Registered as lower priority pending programme-wide heart-faculty analysis.

#### DIM-064-SD013

> The permitting/welcome sense of *aphiēmi* (group 5378-001) names the inner posture of non-obstruction and openness — letting someone come, granting access, refusing to hinder. This is structurally parallel to the inner posture of forgiveness (releasing a claim, opening the relational space). Session D question: is there a common inner-being disposition underlying both forgiveness and welcome/hospitality — a posture of opening rather than closing — that connects the forgiveness corpus to hospitality or compassion registries? Lower priority pending other more strongly signalled connections.

#### DIM-064-SD015

> The OT intercession corpus (group 5379-002) includes multiple cases of communal forgiveness-seeking: Daniel praying for the nation (Dan 9:19), Moses interceding for Israel (Num 14:19), Amos interceding (Amos 7:2), Solomon's prayer covering multiple scenarios of national sin (1Ki 8). This raises the question of whether forgiveness has a collective inner-being dimension — what does it mean for a community to receive forgiveness, and is the inner-being grammar different from individual forgiveness? Lower priority given limited programme focus on corporate inner-being states.

#### DIM-064-SD022

> 6 shared verses between forgiveness (064) and evil (057). Forgiveness is structurally the response to evil done — the two registries are counterparts. Session D question: does the evil corpus (057) address the inner experience of the perpetrator who has committed evil and received forgiveness — specifically, what the inner-being grammar is for the one who has done wrong and has been released? The forgiveness corpus addresses the inner state of the forgiver and the recipient, but the inner-being experience of moving from evildoer to forgiven person has its own grammar. Lower priority given the cooccurrence strength and structural rather than dynamic nature of the connection.

#### DIM-064-SD002

> Mat 18:27 — the master forgave the servant's debt 'out of pity' (*splagchnizomai*), a word naming visceral compassion as a body-involving inner state. This is the most direct somatic entry point for the act of forgiving in the NT: the compassion that generates the forgiving act is itself visceral in its origin. The question for Session D: does compassion (registry 023, C17) function as a necessary inner-being precondition of forgiveness, or is it one pathway among several? This connection is confirmed by dimension overlap (4 shared dimensions) and by the direct vocabulary bridge in this verse. Cannot be resolved within registry 064 alone: whether the compassion-forgiveness relationship is constitutive or merely common requires the compassion corpus to be read.

#### DIM-064-SD003

> The Levitical forgiveness corpus (group 5379-001) presents forgiveness as covenantally objective: correct ritual execution produces forgiveness without specifying inner-being prerequisites in the worshipper. The NT corpus consistently pairs forgiveness with repentance and faith as inner-being preconditions. These represent two distinct covenantal grammars of receiving forgiveness. Session D question: are these structurally sequential (OT type fulfilled and replaced by NT type) or parallel (different aspects of the same underlying inner-being grammar)? Implicates guilt (073) and repentance (135). Cannot be resolved within registry 064 alone: the grammar-shift question requires comparative reading of the guilt and repentance corpora.

#### DIM-064-SD004

> Jer 31:34 is a shared anchor verse with guilt (073), thought/knowledge (160), and love (103). The new covenant promise joins together: direct knowledge of God (cognitive), forgiveness of iniquity (relational), and God's cessation of memory of sin (cognitive-relational). The 'remember no more' clause introduces a cognitive dimension to forgiveness — the removal of the basis for future charges. Session D question: does forgiveness in the new covenant context involve a cognitive component (the removal or transformation of the guilt-state's cognitive content) that connects it to the thought and knowledge registries? Three registries share this anchor; their convergence at this verse may name a structural inner-being cluster within the new covenant promise. Cannot be resolved within registry 064 alone.

#### DIM-064-SD006

> Psa 130:4 ('with you there is forgiveness, that you may be feared') establishes reverential fear as a downstream inner state produced by the encounter with divine forgiveness. Luk 7:47 establishes love as a downstream inner state produced by forgiveness received. Two distinct inner-being states are named in the corpus as downstream consequences of forgiveness. Session D question: are these the same inner-being response named differently in different cultural and covenantal contexts, or are they two distinct states that forgiveness produces depending on context or depth? This question also connects to the grace-supplication pattern in registry 068 (DIM-068 established: grace given → supplication produced). The hypothesis: divine gifts operate as inner-being generators producing specific downstream orientations. Session D must examine whether this is a structural pattern. Implicates reverence (138), love (103), grace (068).

#### DIM-064-SD011

> Luk 7:47 states an explicit inner-being causal chain: the woman's many sins are forgiven (not because she loved, but because she was forgiven), and therefore she loved much; the one forgiven little loves little. The causal direction is unambiguous: forgiveness received → love produced. This chain implicates guilt (073) as the prior state that forgiveness addresses. The full three-registry sequence: guilt (prior state) → forgiveness received (release of guilt) → love produced (downstream orientation). Session D must determine: (1) Is this three-registry causal chain reproducible across the programme corpus? (2) Is forgiveness a transitional state in the inner-being landscape — one that characteristically transforms the person from one orientation to another — rather than a stable state? This is the highest-priority cross-registry question arising from this registry.

#### DIM-064-SD014

> The Levitical corpus (group 5379-001) presents forgiveness as covenantally objective: sacrifice + priestly atonement → 'they shall be forgiven' (passive). The mechanism is outward and ritual; the inner-being prerequisite is not specified. The NT corpus requires repentance and faith. Hebrews (Heb 9:22, Heb 10:18) bridges the two: 'without the shedding of blood there is no forgiveness.' Session D question: does the contrast between OT covenantal-objective forgiveness and NT experiential forgiveness reflect two distinct inner-being grammars of receiving forgiveness, or does one fulfil the other in a way that resolves them into a single structure? Implicates repentance (135), guilt (073), faith (059), and the programme's treatment of covenant structure. Cannot be resolved within registry 064.

#### DIM-064-SD016

> Psa 86:5 places forgiveness (*sallāch*) in direct apposition with goodness and *hesed* (steadfast love/mercy) as co-equal divine attributes: 'you, O Lord, are good and forgiving, abounding in steadfast love.' This is the most concentrated single verse in the corpus for the forgiveness-mercy-kindness cluster. Session D question: does the programme's treatment of mercy (111) and kindness (099) situate them in the same divine-attribute cluster as forgiveness, and does their co-location in Psa 86:5 suggest a systematic relationship where forgiveness is the specific relational act that mercy and *hesed* generate? This is a Session D priority for the C17 cluster synthesis. Confirmed by cooccurrence (16), dimension overlap (3), and shared anchor (Lev 4:20).

#### DIM-064-SD017

> Eph 1:7 — 'in him we have redemption through his blood, the forgiveness of our trespasses, according to the riches of his grace.' Grace is the upstream disposition from which forgiveness flows: 'according to grace' names grace as the source and standard of the forgiveness act. Session D question: does the grace corpus (registry 068) consistently present grace as the source-disposition from which forgiveness and other specific relational acts flow? If so, do grace and forgiveness occupy structurally different positions in an inner-being hierarchy (grace = dispositional; forgiveness = specific relational act derived from the disposition)? This question is the most direct structural question connecting the two most theologically important registries in C17. Confirmed by dimension overlap (3 shared dimensions).

#### DIM-064-SD020

> 9 shared verses between forgiveness (064) and faith (059). The NT pattern is consistent: forgiveness is received through faith (Acts 10:43 'everyone who believes receives forgiveness through his name'; Acts 2:38 repent and be baptised for forgiveness; Acts 26:18 forgiveness for those sanctified by faith). Faith appears as the human instrument through which divine forgiveness is accessed. Session D question: is the faith-forgiveness relationship causal (faith creates the inner-being conditions for forgiveness to be received) or sequential (faith is the posture in which forgiveness is recognised and received)? The distinction matters for understanding whether faith is a necessary inner-being precondition or a concomitant state. Implicates repentance (135) as a parallel access-condition. Confirmed by cooccurrence (9 shared verses).

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

_No phase2 flags on any OWNER term._

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H5545` — 45/45 classified · 3 anchor verse(s)

**Group `5379-001`** (13 verses — anchors: Lev 4:20)

- **Lev 4:20** 🔵 (✓) *target: forgiven*
  > Lev 4:20 Thus shall he do with the bull . As he did with the bull of the sin offering , so shall he do with this. And the priest shall make atonement for them , and they shall be forgiven .
- **Lev 4:26** (✓) *target: forgiven*
  > Lev 4:26 And all its fat he shall burn on the altar , like the fat of the sacrifice of peace offerings . So the priest shall make atonement for him for his sin , and he shall be forgiven .
- **Lev 4:31** (✓) *target: forgiven*
  > Lev 4:31 And all its fat he shall remove , as the fat is removed from the peace offerings , and the priest shall burn it on the altar for a pleasing aroma to the Lord . And the priest shall make atonement for him, and he shall be forgiven .
- **Lev 4:35** (✓) *target: forgiven*
  > Lev 4:35 And all its fat he shall remove as the fat of the lamb is removed from the sacrifice of peace offerings , and the priest shall burn it on the altar , on top of the Lord’s food offerings . And the priest shall make atonement for him for the sin which he has committed , and he shall be forgiven .
- **Lev 5:10** (✓) *target: forgiven*
  > Lev 5:10 Then he shall offer the second for a burnt offering according to the rule . And the priest shall make atonement for him for the sin that he has committed , and he shall be forgiven .
- **Lev 5:13** (✓) *target: forgiven*
  > Lev 5:13 Thus the priest shall make atonement for him for the sin which he has committed in any one of these things, and he shall be forgiven . And the remainder shall be for the priest , as in the grain offering .”
- **Lev 5:16** (✓) *target: forgiven*
  > Lev 5:16 He shall also make restitution for what he has done amiss in the holy thing and shall add a fifth to it and give it to the priest . And the priest shall make atonement for him with the ram of the guilt offering , and he shall be forgiven .
- **Lev 5:18** (✓) *target: forgiven*
  > Lev 5:18 He shall bring to the priest a ram without blemish out of the flock , or its equivalent , for a guilt offering , and the priest shall make atonement for him for the mistake that he made unintentionally , and he shall be forgiven .
- **Lev 6:7** (✓) *target: forgiven*
  > Lev 6:7 And the priest shall make atonement for him before the Lord , and he shall be forgiven for any of the things that one may do and thereby become guilty.”
- **Lev 19:22** (✓) *target: forgiven*
  > Lev 19:22 And the priest shall make atonement for him with the ram of the guilt offering before the Lord for his sin that he has committed , and he shall be forgiven for the sin that he has committed .
- **Num 15:25** (✓) *target: forgiven*
  > Num 15:25 And the priest shall make atonement for all the congregation of the people of Israel , and they shall be forgiven , because it was a mistake , and they have brought their offering , a food offering to the Lord , and their sin offering before the Lord for their mistake .
- **Num 15:26** (✓) *target: forgiven*
  > Num 15:26 And all the congregation of the people of Israel shall be forgiven , and the stranger who sojourns among them, because the whole population was involved in the mistake .
- **Num 15:28** (✓) *target: forgiven*
  > Num 15:28 And the priest shall make atonement before the Lord for the person who makes a mistake , when he sins unintentionally , to make atonement for him , and he shall be forgiven .

**Group `5379-002`** (17 verses — anchors: Dan 9:19)

- **Dan 9:19** 🔵 (✓) *target: forgive*
  > Dan 9:19 O Lord , hear ; O Lord , forgive . O Lord , pay attention and act . Delay not , for your own sake , O my God , because your city and your people are called by your name .”
- **Exo 34:9** (✓) *target: pardon*
  > Exo 34:9 And he said , “ If now I have found favor in your sight , O Lord , please let the Lord go in the midst of us, for it is a stiff-necked people , and pardon our iniquity and our sin , and take us for your inheritance .”
- **Num 14:19** (✓) *target: pardon*
  > Num 14:19 Please pardon the iniquity of this people , according to the greatness of your steadfast love , just as you have forgiven this people , from Egypt until now .”
- **Num 14:20** (✓) *target: pardoned*
  > Num 14:20 Then the Lord said , “I have pardoned , according to your word .
- **Num 30:5** (✓) *target: forgive*
  > Num 30:5 But if her father opposes her on the day that he hears of it, no vow of hers, no pledge by which she has bound herself shall stand . And the Lord will forgive her, because her father opposed her .
- **Num 30:8** (✓) *target: forgive*
  > Num 30:8 But if , on the day that her husband comes to hear of it, he opposes her, then he makes void her vow that was on her, and the thoughtless utterance of her lips by which she bound herself . And the Lord will forgive her .
- **Num 30:12** (✓) *target: forgive*
  > Num 30:12 But if her husband makes them null and void on the day that he hears them, then whatever proceeds out of her lips concerning her vows or concerning her pledge of herself shall not stand . Her husband has made them void , and the Lord will forgive her .
- **Deu 29:20** (✓) *target: forgive*
  > Deu 29:20 The Lord will not be willing to forgive him, but rather the anger of the Lord and his jealousy will smoke against that man , and the curses written in this book will settle upon him, and the Lord will blot out his name from under heaven .
- **2Ki 5:18** (✓) *target: pardon*
  > 2Ki 5:18 In this matter may the Lord pardon your servant : when my master goes into the house of Rimmon to worship there , leaning on my arm , and I bow myself in the house of Rimmon , when I bow myself in the house of Rimmon , the Lord pardon your servant in this matter .”
- **2Ki 24:4** (✓) *target: pardon*
  > 2Ki 24:4 and also for the innocent blood that he had shed . For he filled Jerusalem with innocent blood , and the Lord would not pardon .
- **Psa 25:11** (✓) *target: pardon*
  > Psa 25:11 For your name’s sake , O Lord , pardon my guilt , for it is great .
- **Isa 55:7** (✓) *target: pardon*
  > Isa 55:7 let the wicked forsake his way , and the unrighteous man his thoughts ; let him return to the Lord , that he may have compassion on him, and to our God , for he will abundantly pardon .
- **Jer 5:1** (✓) *target: pardon*
  > Jer 5:1 Run to and fro through the streets of Jerusalem , look and take note ! Search her squares to see if you can find a man , one who does justice and seeks truth , that I may pardon her .
- **Jer 5:7** (✓) *target: pardon*
  > Jer 5:7 “ How can I pardon you ? Your children have forsaken me and have sworn by those who are no gods . When I fed them to the full , they committed adultery and trooped to the houses of whores .
- **Jer 36:3** (✓) *target: forgive*
  > Jer 36:3 It may be that the house of Judah will hear all the disaster that I intend to do to them, so that every one may turn from his evil way , and that I may forgive their iniquity and their sin .”
- **Lam 3:42** (✓) *target: forgiven*
  > Lam 3:42 “ We have transgressed and rebelled , and you have not forgiven .
- **Amo 7:2** (✓) *target: forgive*
  > Amo 7:2 When they had finished eating the grass of the land , I said , “O Lord God , please forgive ! How can Jacob stand ? He is so small !”

**Group `5379-003`** (15 verses — anchors: Jer 31:34)

- **Jer 31:34** 🔵 (✓) *target: forgive*
  > Jer 31:34 And no longer shall each one teach his neighbor and each his brother , saying , ‘ Know the Lord ,’ for they shall all know me, from the least of them to the greatest , declares the Lord . For I will forgive their iniquity , and I will remember their sin no more .”
- **1Ki 8:30** (✓) *target: forgive*
  > 1Ki 8:30 And listen to the plea of your servant and of your people Israel , when they pray toward this place . And listen in heaven your dwelling place , and when you hear , forgive .
- **1Ki 8:34** (✓) *target: forgive*
  > 1Ki 8:34 then hear in heaven and forgive the sin of your people Israel and bring them again to the land that you gave to their fathers .
- **1Ki 8:36** (✓) *target: forgive*
  > 1Ki 8:36 then hear in heaven and forgive the sin of your servants , your people Israel , when you teach them the good way in which they should walk , and grant rain upon your land , which you have given to your people as an inheritance .
- **1Ki 8:39** (✓) *target: forgive*
  > 1Ki 8:39 then hear in heaven your dwelling place and forgive and act and render to each whose heart you know , according to all his ways ( for you , you only, know the hearts of all the children of mankind ),
- **1Ki 8:50** (✓) *target: forgive*
  > 1Ki 8:50 and forgive your people who have sinned against you, and all their transgressions that they have committed against you, and grant them compassion in the sight of those who carried them captive , that they may have compassion on them
- **2Ch 6:21** (✓) *target: forgive*
  > 2Ch 6:21 And listen to the pleas of your servant and of your people Israel , when they pray toward this place . And listen from heaven your dwelling place , and when you hear , forgive .
- **2Ch 6:25** (✓) *target: forgive*
  > 2Ch 6:25 then hear from heaven and forgive the sin of your people Israel and bring them again to the land that you gave to them and to their fathers .
- **2Ch 6:27** (✓) *target: forgive*
  > 2Ch 6:27 then hear in heaven and forgive the sin of your servants , your people Israel , when you teach them the good way in which they should walk , and grant rain upon your land , which you have given to your people as an inheritance .
- **2Ch 6:30** (✓) *target: forgive*
  > 2Ch 6:30 then hear from heaven your dwelling place and forgive and render to each whose heart you know , according to all his ways , for you , you only , know the hearts of the children of mankind ,
- **2Ch 6:39** (✓) *target: forgive*
  > 2Ch 6:39 then hear from heaven your dwelling place their prayer and their pleas , and maintain their cause and forgive your people who have sinned against you .
- **2Ch 7:14** (✓) *target: forgive*
  > 2Ch 7:14 if my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways , then I will hear from heaven and will forgive their sin and heal their land .
- **Psa 103:3** (✓) *target: forgives*
  > Psa 103:3 who forgives all your iniquity , who heals all your diseases ,
- **Jer 33:8** (✓) *target: forgive*
  > Jer 33:8 I will cleanse them from all the guilt of their sin against me, and I will forgive all the guilt of their sin and rebellion against me .
- **Jer 50:20** (✓) *target: pardon*
  > Jer 50:20 In those days and in that time , declares the Lord , iniquity shall be sought in Israel , and there shall be none , and sin in Judah , and none shall be found , for I will pardon those whom I leave as a remnant .

### `H5546` — 1/1 classified · 1 anchor verse(s)

**Group `5380-001`** (1 verse — anchors: Psa 86:5)

- **Psa 86:5** 🔵 (✓) *target: forgiving*
  > Psa 86:5 For you , O Lord , are good and forgiving , abounding in steadfast love to all who call upon you .

### `H5547` — 3/3 classified · 1 anchor verse(s)

**Group `880-001`** (3 verses — anchors: Psa 130:4)

- **Psa 130:4** 🔵 (✓) *target: forgiveness*
  > Psa 130:4 But with you there is forgiveness , that you may be feared .
- **Neh 9:17** (✓) *target: forgive*
  > Neh 9:17 They refused to obey and were not mindful of the wonders that you performed among them, but they stiffened their neck and appointed a leader to return to their slavery in Egypt . But you are a God ready to forgive , gracious and merciful , slow to anger and abounding in steadfast love , and did not forsake them .
- **Dan 9:9** (✓) *target: forgiveness*
  > Dan 9:9 To the Lord our God belong mercy and forgiveness , for we have rebelled against him

### `G0859` — 16/16 classified · 2 anchor verse(s)

**Group `879-001`** (13 verses — anchors: Eph 1:7)

- **Eph 1:7** 🔵 (✓) *target: forgiveness*
  > Eph 1:7 In him we have redemption through his blood , the forgiveness of our trespasses , according to the riches of his grace ,
- **Mat 26:28** (✓) *target: forgiveness*
  > Mat 26:28 for this is my blood of the covenant , which is poured out for many for the forgiveness of sins .
- **Mar 1:4** (✓) *target: forgiveness*
  > Mar 1:4 John appeared , baptizing in the wilderness and proclaiming a baptism of repentance for the forgiveness of sins .
- **Luk 1:77** (✓) *target: forgiveness*
  > Luk 1:77 to give knowledge of salvation to his people in the forgiveness of their sins ,
- **Luk 3:3** (✓) *target: forgiveness*
  > Luk 3:3 And he went into all the region around the Jordan , proclaiming a baptism of repentance for the forgiveness of sins .
- **Luk 4:18** (✓) *target: liberty*
  > Luk 4:18 “The Spirit of the Lord is upon me , because he has anointed me to proclaim good news to the poor . He has sent me to proclaim liberty to the captives and recovering of sight to the blind , to set at liberty those who are oppressed ,
- **Luk 24:47** (✓) *target: forgiveness*
  > Luk 24:47 and that repentance for the forgiveness of sins should be proclaimed in his name to all nations , beginning from Jerusalem .
- **Act 2:38** (✓) *target: forgiveness*
  > Act 2:38 And Peter said to them , “ Repent and be baptized every one of you in the name of Jesus Christ for the forgiveness of your sins , and you will receive the gift of the Holy Spirit .
- **Act 5:31** (✓) *target: forgiveness*
  > Act 5:31 God exalted him at his right hand as Leader and Savior , to give repentance to Israel and forgiveness of sins .
- **Act 10:43** (✓) *target: forgiveness*
  > Act 10:43 To him all the prophets bear witness that everyone who believes in him receives forgiveness of sins through his name .”
- **Act 13:38** (✓) *target: forgiveness*
  > Act 13:38 Let it be known to you therefore , brothers , that through this man forgiveness of sins is proclaimed to you ,
- **Act 26:18** (✓) *target: forgiveness*
  > Act 26:18 to open their eyes , so that they may turn from darkness to light and from the power of Satan to God , that they may receive forgiveness of sins and a place among those who are sanctified by faith in me .’
- **Col 1:14** (✓) *target: forgiveness*
  > Col 1:14 in whom we have redemption , the forgiveness of sins .

**Group `879-002`** (3 verses — anchors: Mar 3:29)

- **Mar 3:29** 🔵 (✓) *target: forgiveness*
  > Mar 3:29 but whoever blasphemes against the Holy Spirit never has forgiveness , but is guilty of an eternal sin ” —
- **Heb 9:22** (✓) *target: forgiveness of sins*
  > Heb 9:22 Indeed , under the law almost everything is purified with blood , and without the shedding of blood there is no forgiveness of sins .
- **Heb 10:18** (✓) *target: forgiveness*
  > Heb 10:18 Where there is forgiveness of these , there is no longer any offering for sin .

### `G0863G` — 32/66 classified · 3 anchor verse(s)

**Group `5376-001`** (13 verses — anchors: Mar 10:29)

- **Mar 10:29** 🔵 (✓) *target: left*
  > Mar 10:29 Jesus said , “ Truly , I say to you , there is no one who has left house or brothers or sisters or mother or father or children or lands , for my sake and for the gospel ,
- **Mat 4:20** (✓) *target: left*
  > Mat 4:20 Immediately they left their nets and followed him .
- **Mat 4:22** (✓) *target: left*
  > Mat 4:22 Immediately they left the boat and their father and followed him .
- **Mat 8:22** (✓) *target: leave*
  > Mat 8:22 And Jesus said to him , “ Follow me , and leave the dead to bury their own dead .”
- **Mat 19:27** (✓) *target: left*
  > Mat 19:27 Then Peter said in reply , “ See , we have left everything and followed you . What then will we have ?”
- **Mat 19:29** (✓) *target: left*
  > Mat 19:29 And everyone who has left houses or brothers or sisters or father or mother or children or lands , for my name’s sake , will receive a hundredfold and will inherit eternal life .
- **Mar 1:18** (✓) *target: left*
  > Mar 1:18 And immediately they left their nets and followed him .
- **Mar 1:20** (✓) *target: left*
  > Mar 1:20 And immediately he called them , and they left their father Zebedee in the boat with the hired servants and followed him .
- **Mar 10:28** (✓) *target: left*
  > Mar 10:28 Peter began to say to him , “ See , we have left everything and followed you .”
- **Luk 5:11** (✓) *target: left*
  > Luk 5:11 And when they had brought their boats to land , they left everything and followed him .
- **Luk 9:60** (✓) *target: Leave*
  > Luk 9:60 And Jesus said to him , “ Leave the dead to bury their own dead . But as for you , go and proclaim the kingdom of God .”
- **Luk 18:28** (✓) *target: left*
  > Luk 18:28 And Peter said , “ See , we have left our homes and followed you .”
- **Luk 18:29** (✓) *target: left*
  > Luk 18:29 And he said to them , “ Truly , I say to you , there is no one who has left house or wife or brothers or parents or children , for the sake of the kingdom of God ,

**Group `5376-002`** (9 verses — anchors: Rev 2:4)

- **Rev 2:4** 🔵 (✓) *target: abandoned*
  > Rev 2:4 But I have this against you , that you have abandoned the love you had at first .
- **Mat 23:23** (✓) *target: neglected*
  > Mat 23:23 “ Woe to you , scribes and Pharisees , hypocrites ! For you tithe mint and dill and cumin , and have neglected the weightier matters of the law : justice and mercy and faithfulness . These you ought to have done , without neglecting the others .
- **Mat 26:56** (✓) *target: left*
  > Mat 26:56 But all this has taken place that the Scriptures of the prophets might be fulfilled .” Then all the disciples left him and fled .
- **Mar 7:8** (✓) *target: leave*
  > Mar 7:8 You leave the commandment of God and hold to the tradition of men .”
- **Mar 14:50** (✓) *target: left*
  > Mar 14:50 And they all left him and fled .
- **Joh 10:12** (✓) *target: leaves*
  > Joh 10:12 He who is a hired hand and not a shepherd , who does not own the sheep , sees the wolf coming and leaves the sheep and flees , and the wolf snatches them and scatters them.
- **1Cor 7:11** (✓) *target: divorce*
  > 1Cor 7:11 ( but if she does , she should remain unmarried or else be reconciled to her husband ), and the husband should not divorce his wife .
- **1Cor 7:12** (✓) *target: divorce*
  > 1Cor 7:12 To the rest I say ( I , not the Lord ) that if any brother has a wife who is an unbeliever , and she consents to live with him , he should not divorce her .
- **1Cor 7:13** (✓) *target: divorce*
  > 1Cor 7:13 If any woman has a husband who is an unbeliever , and he consents to live with her , she should not divorce him .

**Group `5376-003`** (10 verses — anchors: Mat 5:24)

- **Mat 5:24** 🔵 (✓) *target: leave*
  > Mat 5:24 leave your gift there before the altar and go . First be reconciled to your brother , and then come and offer your gift .
- **Mat 15:14** (✓) *target: alone*
  > Mat 15:14 Let them alone ; they are blind guides . And if the blind lead the blind , both will fall into a pit .”
- **Mat 18:12** (✓) *target: leave*
  > Mat 18:12 What do you think ? If a man has a hundred sheep , and one of them has gone astray , does he not leave the ninety-nine on the mountains and go in search of the one that went astray ?
- **Mat 24:40** (✓) *target: left*
  > Mat 24:40 Then two men will be in the field ; one will be taken and one left .
- **Mat 24:41** (✓) *target: left*
  > Mat 24:41 Two women will be grinding at the mill ; one will be taken and one left .
- **Luk 13:35** (✓) *target: forsaken*
  > Luk 13:35 Behold , your house is forsaken . And I tell you , you will not see me until you say , ‘ Blessed is he who comes in the name of the Lord !’”
- **Luk 17:34** (✓) *target: left*
  > Luk 17:34 I tell you , in that night there will be two in one bed . One will be taken and the other left .
- **Luk 17:35** (✓) *target: left*
  > Luk 17:35 There will be two women grinding together . One will be taken and the other left .”
- **Joh 8:29** (✓) *target: left*
  > Joh 8:29 And he who sent me is with me . He has not left me alone , for I always do the things that are pleasing to him .”
- **Heb 6:1** (✓) *target: leave*
  > Heb 6:1 Therefore let us leave the elementary doctrine of Christ and go on to maturity , not laying again a foundation of repentance from dead works and of faith toward God ,

**Group `UNCLASSIFIED`** (34 verses)

- **Mat 4:11** (—) *target: left*
  > Mat 4:11 Then the devil left him , and behold , angels came and were ministering to him .
- **Mat 8:15** (—) *target: left*
  > Mat 8:15 He touched her hand , and the fever left her , and she rose and began to serve him .
- **Mat 13:36** (—) *target: left*
  > Mat 13:36 Then he left the crowds and went into the house . And his disciples came to him , saying , “ Explain to us the parable of the weeds of the field .”
- **Mat 22:22** (—) *target: left*
  > Mat 22:22 When they heard it, they marveled . And they left him and went away .
- **Mat 22:25** (—) *target: left*
  > Mat 22:25 Now there were seven brothers among us . The first married and died , and having no offspring left his wife to his brother .
- **Mat 23:38** (—) *target: left*
  > Mat 23:38 See , your house is left to you desolate .
- **Mat 24:2** (—) *target: left*
  > Mat 24:2 But he answered them , “You see all these , do you not ? Truly , I say to you , there will not be left here one stone upon another that will not be thrown down .”
- **Mat 26:44** (—) *target: leaving*
  > Mat 26:44 So , leaving them again , he went away and prayed for the third time , saying the same words again .
- **Mat 27:49** (—) *target: Wait*
  > Mat 27:49 But the others said , “ Wait , let us see whether Elijah will come to save him .”
- **Mar 1:31** (—) *target: left*
  > Mar 1:31 And he came and took her by the hand and lifted her up, and the fever left her , and she began to serve them .
- **Mar 4:36** (—) *target: leaving*
  > Mar 4:36 And leaving the crowd , they took him with them in the boat , just as he was . And other boats were with him .
- **Mar 8:13** (—) *target: left*
  > Mar 8:13 And he left them , got into the boat again , and went to the other side .
- **Mar 11:6** (—) *target: go*
  > Mar 11:6 And they told them what Jesus had said , and they let them go .
- **Mar 12:12** (—) *target: left*
  > Mar 12:12 And they were seeking to arrest him but feared the people , for they perceived that he had told the parable against them . So they left him and went away .
- **Mar 12:19** (—) *target: leaves*
  > Mar 12:19 “ Teacher , Moses wrote for us that if a man’s brother dies and leaves a wife , but leaves no child , the man must take the widow and raise up offspring for his brother .
- **Mar 12:20** (—) *target: left*
  > Mar 12:20 There were seven brothers ; the first took a wife , and when he died left no offspring .
- **Mar 12:22** (—) *target: left*
  > Mar 12:22 And the seven left no offspring . Last of all the woman also died .
- **Mar 13:2** (—) *target: left*
  > Mar 13:2 And Jesus said to him , “Do you see these great buildings ? There will not be left here one stone upon another that will not be thrown down .”
- **Mar 13:34** (—) *target: leaves*
  > Mar 13:34 It is like a man going on a journey , when he leaves home and puts his servants in charge , each with his work , and commands the doorkeeper to stay awake .
- **Mar 14:6** (—) *target: alone*
  > Mar 14:6 But Jesus said , “Leave her alone . Why do you trouble her ? She has done a beautiful thing to me .
- **Mar 15:36** (—) *target: Wait*
  > Mar 15:36 And someone ran and filled a sponge with sour wine , put it on a reed and gave it to him to drink , saying , “ Wait , let us see whether Elijah will come to take him down .”
- **Mar 15:37** (—) *target: uttered*
  > Mar 15:37 And Jesus uttered a loud cry and breathed his last .
- **Luk 4:39** (—) *target: left*
  > Luk 4:39 And he stood over her and rebuked the fever , and it left her , and immediately she rose and began to serve them .
- **Luk 10:30** (—) *target: leaving*
  > Luk 10:30 Jesus replied , “ A man was going down from Jerusalem to Jericho , and he fell among robbers , who stripped him and beat him and departed , leaving him half dead .
- **Luk 12:39** (—) *target: left*
  > Luk 12:39 But know this , that if the master of the house had known at what hour the thief was coming , he would not have left his house to be broken into .
- **Luk 13:8** (—) *target: alone*
  > Luk 13:8 And he answered him , ‘ Sir , let it alone this year also , until I dig around it and put on manure .
- **Luk 19:44** (—) *target: leave*
  > Luk 19:44 and tear you down to the ground , you and your children within you . And they will not leave one stone upon another in you , because you did not know the time of your visitation .”
- **Luk 21:6** (—) *target: left*
  > Luk 21:6 “As for these things that you see , the days will come when there will not be left here one stone upon another that will not be thrown down .”
- **Joh 4:3** (—) *target: left*
  > Joh 4:3 he left Judea and departed again for Galilee .
- **Joh 4:28** (—) *target: left*
  > Joh 4:28 So the woman left her water jar and went away into town and said to the people ,
- **Joh 4:52** (—) *target: left*
  > Joh 4:52 So he asked them the hour when he began to get better , and they said to him , “ Yesterday at the seventh hour the fever left him .”
- **Joh 11:48** (—) *target: go on*
  > Joh 11:48 If we let him go on like this , everyone will believe in him , and the Romans will come and take away both our place and our nation .”
- **Joh 12:7** (—) *target: alone*
  > Joh 12:7 Jesus said , “Leave her alone , so that she may keep it for the day of my burial .
- **Heb 2:8** (—) *target: left*
  > Heb 2:8 putting everything in subjection under his feet .” Now in putting everything in subjection to him , he left nothing outside his control . At present , we do not yet see everything in subjection to him .

### `G0863H` — 37/37 classified · 2 anchor verse(s)

**Group `5377-001`** (26 verses — anchors: Luk 7:47)

- **Luk 7:47** 🔵 (✓) *target: forgiven*
  > Luk 7:47 Therefore I tell you , her sins , which are many , are forgiven — for she loved much . But he who is forgiven little , loves little .”
- **Mat 9:2** (✓) *target: forgiven*
  > Mat 9:2 And behold , some people brought to him a paralytic , lying on a bed . And when Jesus saw their faith , he said to the paralytic , “Take heart , my son ; your sins are forgiven .”
- **Mat 9:5** (✓) *target: forgiven*
  > Mat 9:5 For which is easier , to say , ‘Your sins are forgiven ,’ or to say , ‘ Rise and walk ’?
- **Mat 9:6** (✓) *target: forgive*
  > Mat 9:6 But that you may know that the Son of Man has authority on earth to forgive sins ” —he then said to the paralytic — “ Rise , pick up your bed and go home .”
- **Mat 12:31** (✓) *target: forgiven*
  > Mat 12:31 Therefore I tell you , every sin and blasphemy will be forgiven people , but the blasphemy against the Spirit will not be forgiven .
- **Mat 12:32** (✓) *target: forgiven*
  > Mat 12:32 And whoever speaks a word against the Son of Man will be forgiven , but whoever speaks against the Holy Spirit will not be forgiven , either in this age or in the age to come .
- **Mar 2:5** (✓) *target: forgiven*
  > Mar 2:5 And when Jesus saw their faith , he said to the paralytic , “ Son , your sins are forgiven .”
- **Mar 2:7** (✓) *target: forgive*
  > Mar 2:7 “ Why does this man speak like that? He is blaspheming ! Who can forgive sins but God alone ?”
- **Mar 2:9** (✓) *target: forgiven*
  > Mar 2:9 Which is easier , to say to the paralytic , ‘ Your sins are forgiven ,’ or to say , ‘ Rise , take up your bed and walk ’?
- **Mar 2:10** (✓) *target: forgive*
  > Mar 2:10 But that you may know that the Son of Man has authority on earth to forgive sins ” —he said to the paralytic —
- **Mar 3:28** (✓) *target: forgiven*
  > Mar 3:28 “ Truly , I say to you , all sins will be forgiven the children of man , and whatever blasphemies they utter ,
- **Mar 4:12** (✓) *target: forgiven*
  > Mar 4:12 so that “'they may indeed see but not perceive , and may indeed hear but not understand , lest they should turn and be forgiven .'”
- **Luk 5:20** (✓) *target: forgiven*
  > Luk 5:20 And when he saw their faith , he said , “ Man , your sins are forgiven you .”
- **Luk 5:21** (✓) *target: forgive*
  > Luk 5:21 And the scribes and the Pharisees began to question , saying , “ Who is this who speaks blasphemies ? Who can forgive sins but God alone ?”
- **Luk 5:23** (✓) *target: forgiven*
  > Luk 5:23 Which is easier , to say , ‘ Your sins are forgiven you ,’ or to say , ‘ Rise and walk ’?
- **Luk 5:24** (✓) *target: forgive*
  > Luk 5:24 But that you may know that the Son of Man has authority on earth to forgive sins ” —he said to the man who was paralyzed — “I say to you , rise , pick up your bed and go home.”
- **Luk 7:48** (✓) *target: forgiven*
  > Luk 7:48 And he said to her , “ Your sins are forgiven .”
- **Luk 7:49** (✓) *target: forgives*
  > Luk 7:49 Then those who were at table with him began to say among themselves , “ Who is this , who even forgives sins ?”
- **Luk 12:10** (✓) *target: forgiven*
  > Luk 12:10 And everyone who speaks a word against the Son of Man will be forgiven , but the one who blasphemes against the Holy Spirit will not be forgiven .
- **Luk 23:34** (✓) *target: forgive*
  > Luk 23:34 And Jesus said , “ Father , forgive them , for they know not what they do .” And they cast lots to divide his garments .
- **Joh 20:23** (✓) *target: forgive*
  > Joh 20:23 If you forgive the sins of any , they are forgiven them ; if you withhold forgiveness from any , it is withheld .”
- **Act 8:22** (✓) *target: forgiven*
  > Act 8:22 Repent , therefore , of this wickedness of yours , and pray to the Lord that, if possible , the intent of your heart may be forgiven you .
- **Rom 4:7** (✓) *target: forgiven*
  > Rom 4:7 “ Blessed are those whose lawless deeds are forgiven , and whose sins are covered ;
- **Jam 5:15** (✓) *target: forgiven*
  > Jam 5:15 And the prayer of faith will save the one who is sick , and the Lord will raise him up . And if he has committed sins , he will be forgiven .
- **1Jo 1:9** (✓) *target: forgive*
  > 1Jo 1:9 If we confess our sins , he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness .
- **1Jo 2:12** (✓) *target: forgiven*
  > 1Jo 2:12 I am writing to you , little children , because your sins are forgiven for his name’s sake .

**Group `5377-002`** (11 verses — anchors: Mat 18:35)

- **Mat 18:35** 🔵 (✓) *target: forgive*
  > Mat 18:35 So also my heavenly Father will do to every one of you , if you do not forgive your brother from your heart .”
- **Mat 6:12** (✓) *target: forgive*
  > Mat 6:12 and forgive us our debts , as we also have forgiven our debtors .
- **Mat 6:14** (✓) *target: forgive*
  > Mat 6:14 For if you forgive others their trespasses , your heavenly Father will also forgive you ,
- **Mat 6:15** (✓) *target: forgive*
  > Mat 6:15 but if you do not forgive others their trespasses , neither will your Father forgive your trespasses .
- **Mat 18:21** (✓) *target: forgive*
  > Mat 18:21 Then Peter came up and said to him , “ Lord , how often will my brother sin against me , and I forgive him ? As many as seven times ?”
- **Mat 18:27** (✓) *target: forgave*
  > Mat 18:27 And out of pity for him, the master of that servant released him and forgave him the debt .
- **Mat 18:32** (✓) *target: forgave*
  > Mat 18:32 Then his master summoned him and said to him , ‘You wicked servant ! I forgave you all that debt because you pleaded with me .
- **Mar 11:25** (✓) *target: forgive*
  > Mar 11:25 And whenever you stand praying , forgive , if you have anything against anyone , so that your Father also who is in heaven may forgive you your trespasses .”
- **Luk 11:4** (✓) *target: forgive*
  > Luk 11:4 and forgive us our sins , for we ourselves forgive everyone who is indebted to us . And lead us not into temptation .”
- **Luk 17:3** (✓) *target: forgive*
  > Luk 17:3 Pay attention to yourselves ! If your brother sins , rebuke him , and if he repents , forgive him ,
- **Luk 17:4** (✓) *target: forgive*
  > Luk 17:4 and if he sins against you seven times in the day , and turns to you seven times , saying , ‘I repent ,’ you must forgive him .”

### `G0863I` — 18/22 classified · 2 anchor verse(s)

**Group `5378-001`** (12 verses — anchors: Mar 10:14)

- **Mar 10:14** 🔵 (✓) *target: Let*
  > Mar 10:14 But when Jesus saw it, he was indignant and said to them , “ Let the children come to me ; do not hinder them , for to such belongs the kingdom of God .
- **Mat 3:15** (✓) *target: Let*
  > Mat 3:15 But Jesus answered him , “ Let it be so now , for thus it is fitting for us to fulfill all righteousness .” Then he consented .
- **Mat 5:40** (✓) *target: have*
  > Mat 5:40 And if anyone would sue you and take your tunic , let him have your cloak as well .
- **Mat 7:4** (✓) *target: Let*
  > Mat 7:4 Or how can you say to your brother , ‘ Let me take the speck out of your eye ,’ when there is the log in your own eye ?
- **Mat 19:14** (✓) *target: Let*
  > Mat 19:14 but Jesus said , “ Let the little children come to me and do not hinder them , for to such belongs the kingdom of heaven .”
- **Mar 5:19** (✓) *target: permit*
  > Mar 5:19 And he did not permit him but said to him , “ Go home to your friends and tell them how much the Lord has done for you , and how he has had mercy on you .”
- **Mar 7:27** (✓) *target: Let*
  > Mar 7:27 And he said to her , “ Let the children be fed first , for it is not right to take the children’s bread and throw it to the dogs .”
- **Mar 11:16** (✓) *target: allow*
  > Mar 11:16 And he would not allow anyone to carry anything through the temple .
- **Luk 6:42** (✓) *target: let*
  > Luk 6:42 How can you say to your brother , ‘ Brother , let me take out the speck that is in your eye ,’ when you yourself do not see the log that is in your own eye ? You hypocrite , first take the log out of your own eye , and then you will see clearly to take out the speck that is in your brother’s eye .
- **Luk 18:16** (✓) *target: Let*
  > Luk 18:16 But Jesus called them to him, saying , “ Let the children come to me , and do not hinder them , for to such belongs the kingdom of God .
- **Joh 18:8** (✓) *target: let*
  > Joh 18:8 Jesus answered , “I told you that I am he. So , if you seek me , let these men go .”
- **Act 5:38** (✓) *target: let*
  > Act 5:38 So in the present case I tell you , keep away from these men and let them alone, for if this plan or this undertaking is of man , it will fail ;

**Group `5378-002`** (6 verses — anchors: Mat 23:13)

- **Mat 23:13** 🔵 (✓) *target: allow*
  > Mat 23:13 “ But woe to you , scribes and Pharisees , hypocrites ! For you shut the kingdom of heaven in people’s faces . For you neither enter yourselves nor allow those who would enter to go in .
- **Mat 27:50** (✓) *target: yielded up*
  > Mat 27:50 And Jesus cried out again with a loud voice and yielded up his spirit .
- **Mar 1:34** (✓) *target: permit*
  > Mar 1:34 And he healed many who were sick with various diseases , and cast out many demons . And he would not permit the demons to speak , because they knew him .
- **Mar 7:12** (✓) *target: permit*
  > Mar 7:12 then you no longer permit him to do anything for his father or mother ,
- **Rom 1:27** (✓) *target: gave up*
  > Rom 1:27 and the men likewise gave up natural relations with women and were consumed with passion for one another , men committing shameless acts with men and receiving in themselves the due penalty for their error .
- **Rev 11:9** (✓) *target: let*
  > Rev 11:9 For three and a half days some from the peoples and tribes and languages and nations will gaze at their dead bodies and refuse to let them be placed in a tomb ,

**Group `UNCLASSIFIED`** (4 verses)

- **Mat 13:30** (—) *target: Let*
  > Mat 13:30 Let both grow together until the harvest , and at harvest time I will tell the reapers , " Gather the weeds first and bind them in bundles to be burned , but gather the wheat into my barn ."’”
- **Mar 5:37** (—) *target: allowed*
  > Mar 5:37 And he allowed no one to follow him except Peter and James and John the brother of James .
- **Luk 8:51** (—) *target: allowed*
  > Luk 8:51 And when he came to the house , he allowed no one to enter with him, except Peter and John and James , and the father and mother of the child .
- **Joh 11:44** (—) *target: let*
  > Joh 11:44 The man who had died came out , his hands and feet bound with linen strips , and his face wrapped with a cloth . Jesus said to them , “ Unbind him , and let him go .”

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**7 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H5545` | to forgive | `to_revise` | 45 | 3 | 45 |
| `H5546` | forgiving | `to_revise` | 1 | 1 | 1 |
| `H5547` | forgiveness | `to_revise` | 3 | 1 | 3 |
| `G0859` | forgiveness | `to_revise` | 16 | 2 | 16 |
| `G0863G` | to release: leave | `to_revise` | 66 | 3 | 32 |
| `G0863H` | to release: forgive | `to_revise` | 37 | 2 | 37 |
| `G0863I` | to release: permit | `to_revise` | 22 | 2 | 18 |

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

### Registry-specific questions for 064 forgiveness

**14 question(s)** sourced from this registry's prior work. Include in Stage 2b alongside the generic questions.

```json
{
  "registry_no": 64,
  "registry_word": "forgiveness",
  "total": 14,
  "questions": [
    {
      "obs_id": 148,
      "question_code": "F-001",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Does the word have an outer limit — a condition or state in which it is explicitly withheld or cannot operate — and what does that outer limit reveal about the word's nature?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 149,
      "question_code": "F-002",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Can the structure of the word's action be misused or inverted — can the same act-structure produce a wrong result — and what is the evidence?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 150,
      "question_code": "F-003",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Is there a vertical-horizontal structural interdependence in the word's operation — does reception from God structurally enable extension toward others?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 151,
      "question_code": "F-004",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Is the word's primary grammatical subject restricted — is it used exclusively or primarily with one type of subject (divine, human, or other)?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 152,
      "question_code": "F-005",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "What is the mechanism through which the word is administered or conveyed — and what is the relationship between the outward mechanism and the inner reality it produces?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 153,
      "question_code": "F-006",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Does the word operate unconditionally — or does it have stated conditions under which it is granted or withheld?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 154,
      "question_code": "F-007",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Is the word a single act or a compound of distinct component acts — and if compound, what are the components and are they always simultaneous?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 155,
      "question_code": "F-008",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "What does the word make possible in a relationship that would otherwise be closed or broken — and what relational cycle does it break?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 156,
      "question_code": "F-009",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Does the word function as a prerequisite or enabling condition for another spiritual act or practice — and if so, which one and why?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 157,
      "question_code": "F-010",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Are the downstream inner-being effects of the word proportional to the degree or magnitude of the word received — does more of the word produce more of the effect?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 158,
      "question_code": "F-011",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Does the word share vocabulary with adjacent characteristics — or does it occupy an isolated lexical space? What does the degree of sharing or isolation suggest about the word's relationship to adjacent characteristics?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 159,
      "question_code": "F-012",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Is the word named in Scripture as a divine possession or attribute — something that belongs to God — distinct from an act God performs? What does that naming imply about access to the word?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 160,
      "question_code": "F-013",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "What practices, disciplines, or ongoing inner acts feed or sustain the human capacity to extend the word to others?",
      "pattern_type": null,
      "scope": "universal",
      "status": "active"
    },
    {
      "obs_id": 161,
      "question_code": "F-014",
      "section": "Forgiveness Extensions",
      "source_word": "Forgiveness",
      "source_registry_no": 64,
      "question_text": "Is the word a terminal inner-being state — one in which the person rests — or a transitional one that characteristically produces movement to a further state? What is the evidence either way?",
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

- **Generated at:** `2026-04-28T06:24:55Z`
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

*End of readiness output v3 — wa-064-forgiveness.*