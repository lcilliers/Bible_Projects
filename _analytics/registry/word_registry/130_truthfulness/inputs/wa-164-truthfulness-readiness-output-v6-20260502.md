# wa-164-truthfulness — Analysis Readiness Output (v6)

_v6 generation · 2026-05-02T15:25:01Z · schema 3.17.0 · catalogue v2-2026-04-29 (T0–T7)_

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

- **Registry no:** `164` · **word:** `truthfulness`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `wa-dimensionreview-instruction-v3_3-20260418`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 5  (programme-wide aggregate including XREF and historical terms — current OWNER count is 5, XREF 0)
- `phase1_verse_count`: 161  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 2 unresolved · **Existing session_b_findings:** 1

**Description:**

> Truthfulness is the commitment to correspondence between what one says and what is actually the case — the quality of the person whose word is reliable and whose account of things can be trusted. The Greek vocabulary here (alētheia) covers truth in the deepest sense: not just accurate information but the genuine, unveiled reality of things. Truthfulness is both a character quality (the truthful person) and a relational practice (speaking truth to one another). It is grounded in the character of God, who cannot lie.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-02T15:25:01Z`
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
| `G0225` | alētheia | truth | G | `extracted` | **`not_done`** | 1 | 90 | 6/0 | 76/0 | 6 |
| `G0226` | alētheuō | be truthful | G | `extracted` | **`not_done`** | 1 | 2 | 1/0 | 2/0 | 1 |
| `G0227` | alēthēs | true | G | `extracted` | **`not_done`** | 1 | 25 | 1/0 | 8/0 | 1 |
| `G0228` | alēthinos | true | G | `extracted` | **`not_done`** | 1 | 26 | 1/0 | 6/0 | 1 |
| `G0230` | alēthōs | truly | G | `extracted` | **`not_done`** | 1 | 18 | 1/0 | 13/0 | 1 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `G0225` — alētheia "truth"

**Identity:** mti=1197 · ti=1315 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:15:42): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: truth, truthfulness; corresponding to reality 
truth, Mk. 5:33; love of truth, sincerity 1Cor. 5:8; divine truth revealed to man, Jn. 1:17; practice in accordance with Gospel truth, Jn. 3:21; 2Jn. 4

**Root family:**
- `ALĒTHĒS` (Greek): true — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0226` alētheuō "be truthful"
- `G0227` alēthēs "true"
- `G0228` alēthinos "true"
- `G0230` alēthōs "truly"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0226` — alētheuō "be truthful"

**Identity:** mti=6590 · ti=6663 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:15:42): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: to be truthful, tell the truth 
to speak, or maintain the truth; to act truly or sincerely, Gal. 4:16; Eph. 4:15*

**Root family:**
- `ALĒTHĒS` (Greek): true — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0225` alētheia "truth"
- `G0227` alēthēs "true"
- `G0228` alēthinos "true"
- `G0230` alēthōs "truly"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0227` — alēthēs "true"

**Identity:** mti=6588 · ti=6661 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:15:42): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: true, Jn. 4:18; worthy of credit, trustworthy, valid Jn. 5:31; truthful, genuine, reliable Jn. 7:18

**Root family:**
- `ALĒTHĒS` (Greek): true — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (5 total; sample of 5):**
- `G0225` alētheia "truth"
- `G0226` alētheuō "be truthful"
- `G0228` alēthinos "true"
- `G0230` alēthōs "truly"
- `G2990` lanthanō "be hidden"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0228` — alēthinos "true"

**Identity:** mti=6587 · ti=6660 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:15:42): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: sterling, Lk. 16:11; real, genuine Jn. 6:32; 1Thess. 1:9; unfeigned, trustworthy, true, Jn. 19:35

**Root family:**
- `ALĒTHĒS` (Greek): true — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0225` alētheia "truth"
- `G0226` alētheuō "be truthful"
- `G0227` alēthēs "true"
- `G0230` alēthōs "truly"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G0230` — alēthōs "truly"

**Identity:** mti=6589 · ti=6662 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:15:42): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: truly, really, surely Mt. 14:33; certainly, of a truth, Jn. 17:8; Acts 12:11: truly, actually, Jn. 4:18

**Root family:**
- `ALĒTHĒS` (Greek): true — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (4 total; sample of 4):**
- `G0225` alētheia "truth"
- `G0226` alētheuō "be truthful"
- `G0227` alēthēs "true"
- `G0228` alēthinos "true"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (0)

_None._

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `G0225` — 6 groups

- **`1197-001`** — 8 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Truth as transforming/shaping force on the inner person — sanctification, purification, self-orientation*
- **`1197-002`** — 18 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C10`
  - *Truth as the proper object of the will — accepting, obeying, refusing, or rejecting truth as inner act*
- **`1197-003`** — 18 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Truth as inner quality of character — integrity, authenticity, living and speaking truthfully*
- **`1197-004`** — 6 relevant · 1 anchor verse(s) · dimension: `10 — Dependence / Creatureliness` · cluster: `C10`
  - *Truth as the Spirit's identity and work in the inner person — Spirit of truth*
- **`1197-005`** — 12 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Truth as relational/theological identity — who Christ is; worship in spirit and truth*
- **`1197-006`** — 14 relevant · 1 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C10`
  - *Truth as the gospel received inwardly — knowledge of truth as saving and formational event*

### `G0226` — 1 groups

- **`6590-001`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Truthful speech as inner act of integrity — in relationship and spiritual growth*

### `G0227` — 1 groups

- **`6588-001`** — 8 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Truthfulness as inner character quality — integrity, genuineness, the true heart*

### `G0228` — 1 groups

- **`6587-001`** — 6 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Genuineness as inner-being orientation — true worship, turning to the true God, inner fidelity*

### `G0230` — 1 groups

- **`6589-001`** — 13 relevant · 1 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C10`
  - *"Truly" as qualifier of inner-being recognition, knowing, confession, and reception*

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
| 43 desire | 7 |
| 59 faith | 7 |
| 98 justice | 7 |
| 103 love | 7 |
| 57 evil | 5 |
| 73 guilt | 5 |
| 176 worship | 5 |
| 187 strength | 5 |
| 197 authority | 5 |
| 112 mind | 4 |
| 39 debauchery | 3 |
| 69 gratitude | 3 |
| 163 trust | 3 |
| 173 will | 3 |
| 207 blindness (spiritual) | 3 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 40 deceit | Joh 1:47 |
| 43 desire | 1Ti 2:4 |
| 43 desire | Joh 4:23 |
| 47 dignity | Phili 4:8 |
| 73 guilt | Heb 10:22 |
| 103 love | Phili 4:8 |
| 121 praise | Phili 4:8 |
| 160 thought | Phili 4:8 |
| 165 unbelief | Rom 2:8 |
| 176 worship | Joh 4:23 |
| 180 yielding | Heb 10:22 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-164-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> The aletheia word family spans five distinct inner-being dimensions across 10 groups: Spiritual/God-ward, Volitional/Will, Character/Disposition, Theological/Divine-Human, Cognitive/Mind. No single dimension captures the full range. Session B should examine whether 'truthfulness' is the right registry label, and whether the term's biblical range is better described as 'truth-orientation' or another formulation that captures both the character quality and the transformational/pneumatological dimensions.

### H.2 Open SD pointers + research flags (2)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SD_POINTER` | DIM-164-SD001 | MEDIUM | D | 2026-04-07 |
| `SD_POINTER` | DIM-164-SD002 | MEDIUM | Session D | 2026-05-02 |

#### DIM-164-SD001

> The aletheia word family spans five distinct inner-being dimensions — the widest dimensional range of any single word family reviewed in C10. This raises the question of whether 'truthfulness' is a sufficiently narrow or accurate registry label for what these terms express in their biblical usage. Session D should address the vocabulary fit and whether a broader label such as 'truth-orientation' or a restructured approach to this registry is warranted.

#### DIM-164-SD002

> R164 (alētheia family) shows truth operating across five inner-being dimensions: Transformation (sanctification), Volition (will toward/against truth), Moral Character (integrity/authenticity), Dependence/Creatureliness (receptivity to Spirit of truth), Relational Disposition (worship in truth; truthful speech), and Cognition (knowledge of truth as saving event). This breadth is itself a finding: truth in the NT is not a single inner-being category but a force engaging the whole person. Supplementary to pre-existing DIM-164-SD001 (registry label-fit question); this pointer adds the dimension-breadth observation for Session D synthesis.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `G0225` (1 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `G0225` — 76/90 classified · 6 anchor verse(s)

**Group `1197-001`** (8 verses — anchors: Joh 17:17)

- **Joh 17:17** 🔵 (✓) *target: truth*
  > Joh 17:17 Sanctify them in the truth ; your word is truth .
- **Joh 8:32** (✓) *target: truth*
  > Joh 8:32 and you will know the truth , and the truth will set you free .”
- **Joh 17:19** (✓) *target: truth*
  > Joh 17:19 And for their sake I consecrate myself , that they also may be sanctified in truth .
- **Eph 4:21** (✓) *target: truth*
  > Eph 4:21 assuming that you have heard about him and were taught in him , as the truth is in Jesus ,
- **Eph 4:24** (✓) *target: true*
  > Eph 4:24 and to put on the new self , created after the likeness of God in true righteousness and holiness .
- **Col 1:6** (✓) *target: truth*
  > Col 1:6 which has come to you , as indeed in the whole world it is bearing fruit and increasing — as it also does among you , since the day you heard it and understood the grace of God in truth ,
- **2Th 2:13** (✓) *target: truth*
  > 2Th 2:13 But we ought always to give thanks to God for you , brothers beloved by the Lord , because God chose you as the firstfruits to be saved , through sanctification by the Spirit and belief in the truth .
- **1Pe 1:22** (✓) *target: truth*
  > 1Pe 1:22 Having purified your souls by your obedience to the truth for a sincere brotherly love, love one another earnestly from a pure heart ,

**Group `1197-002`** (18 verses — anchors: Rom 2:8)

- **Rom 2:8** 🔵 (✓) *target: truth*
  > Rom 2:8 but for those who are self-seeking and do not obey the truth , but obey unrighteousness , there will be wrath and fury .
- **Joh 8:44** (✓) *target: truth*
  > Joh 8:44 You are of your father the devil , and your will is to do your father’s desires . He was a murderer from the beginning , and does not stand in the truth , because there is no truth in him . When he lies , he speaks out of his own character, for he is a liar and the father of lies .
- **Joh 8:45** (✓) *target: truth*
  > Joh 8:45 But because I tell the truth , you do not believe me .
- **Joh 8:46** (✓) *target: truth*
  > Joh 8:46 Which one of you convicts me of sin ? If I tell the truth , why do you not believe me ?
- **Rom 1:18** (✓) *target: truth*
  > Rom 1:18 For the wrath of God is revealed from heaven against all ungodliness and unrighteousness of men , who by their unrighteousness suppress the truth .
- **1Cor 13:6** (✓) *target: truth*
  > 1Cor 13:6 it does not rejoice at wrongdoing , but rejoices with the truth .
- **2Cor 13:8** (✓) *target: truth*
  > 2Cor 13:8 For we cannot do anything against the truth , but only for the truth .
- **Gal 5:7** (✓) *target: truth*
  > Gal 5:7 You were running well . Who hindered you from obeying the truth ?
- **2Th 2:10** (✓) *target: truth*
  > 2Th 2:10 and with all wicked deception for those who are perishing , because they refused to love the truth and so be saved .
- **2Th 2:12** (✓) *target: truth*
  > 2Th 2:12 in order that all may be condemned who did not believe the truth but had pleasure in unrighteousness .
- **1Ti 4:3** (✓) *target: truth*
  > 1Ti 4:3 who forbid marriage and require abstinence from foods that God created to be received with thanksgiving by those who believe and know the truth .
- **1Ti 6:5** (✓) *target: truth*
  > 1Ti 6:5 and constant friction among people who are depraved in mind and deprived of the truth , imagining that godliness is a means of gain .
- **2Ti 2:18** (✓) *target: truth*
  > 2Ti 2:18 who have swerved from the truth , saying that the resurrection has already happened . They are upsetting the faith of some .
- **2Ti 3:8** (✓) *target: truth*
  > 2Ti 3:8 Just as Jannes and Jambres opposed Moses , so these men also oppose the truth , men corrupted in mind and disqualified regarding the faith .
- **2Ti 4:4** (✓) *target: truth*
  > 2Ti 4:4 and will turn away from listening to the truth and wander off into myths .
- **Tit 1:14** (✓) *target: truth*
  > Tit 1:14 not devoting themselves to Jewish myths and the commands of people who turn away from the truth .
- **Heb 10:26** (✓) *target: truth*
  > Heb 10:26 For if we go on sinning deliberately after receiving the knowledge of the truth , there no longer remains a sacrifice for sins ,
- **Jam 5:19** (✓) *target: truth*
  > Jam 5:19 My brothers , if anyone among you wanders from the truth and someone brings him back ,

**Group `1197-003`** (18 verses — anchors: 1Jo 1:6)

- **1Jo 1:6** 🔵 (✓) *target: truth*
  > 1Jo 1:6 If we say we have fellowship with him while we walk in darkness , we lie and do not practice the truth .
- **Joh 3:21** (✓) *target: true*
  > Joh 3:21 But whoever does what is true comes to the light , so that it may be clearly seen that his works have been carried out in God .”
- **Joh 5:33** (✓) *target: truth*
  > Joh 5:33 You sent to John , and he has borne witness to the truth .
- **Joh 8:40** (✓) *target: truth*
  > Joh 8:40 but now you seek to kill me , a man who has told you the truth that I heard from God . This is not what Abraham did .
- **Rom 9:1** (✓) *target: truth*
  > Rom 9:1 I am speaking the truth in Christ —I am not lying ; my conscience bears me witness in the Holy Spirit —
- **1Cor 5:8** (✓) *target: truth*
  > 1Cor 5:8 Let us therefore celebrate the festival , not with the old leaven , the leaven of malice and evil , but with the unleavened bread of sincerity and truth .
- **2Cor 4:2** (✓) *target: truth*
  > 2Cor 4:2 But we have renounced disgraceful , underhanded ways. We refuse to practice cunning or to tamper with God’s word , but by the open statement of the truth we would commend ourselves to everyone’s conscience in the sight of God .
- **2Cor 6:7** (✓) *target: truthful*
  > 2Cor 6:7 by truthful speech , and the power of God ; with the weapons of righteousness for the right hand and for the left ;
- **2Cor 11:10** (✓) *target: truth*
  > 2Cor 11:10 As the truth of Christ is in me , this boasting of mine will not be silenced in the regions of Achaia .
- **Eph 4:25** (✓) *target: truth*
  > Eph 4:25 Therefore , having put away falsehood , let each one of you speak the truth with his neighbor , for we are members one of another .
- **Eph 5:9** (✓) *target: true*
  > Eph 5:9 ( for the fruit of light is found in all that is good and right and true ),
- **Eph 6:14** (✓) *target: truth*
  > Eph 6:14 Stand therefore , having fastened on the belt of truth , and having put on the breastplate of righteousness ,
- **1Ti 2:7** (✓) *target: truth*
  > 1Ti 2:7 For this I was appointed a preacher and an apostle ( I am telling the truth , I am not lying ), a teacher of the Gentiles in faith and truth .
- **Jam 3:14** (✓) *target: truth*
  > Jam 3:14 But if you have bitter jealousy and selfish ambition in your hearts , do not boast and be false to the truth .
- **1Jo 1:8** (✓) *target: truth*
  > 1Jo 1:8 If we say we have no sin , we deceive ourselves , and the truth is not in us .
- **1Jo 2:4** (✓) *target: truth*
  > 1Jo 2:4 Whoever says “I know him ” but does not keep his commandments is a liar , and the truth is not in him ,
- **1Jo 3:18** (✓) *target: truth*
  > 1Jo 3:18 Little children , let us not love in word or talk but in deed and in truth .
- **1Jo 3:19** (✓) *target: truth*
  > 1Jo 3:19 By this we shall know that we are of the truth and reassure our heart before him ;

**Group `1197-004`** (6 verses — anchors: Joh 14:17)

- **Joh 14:17** 🔵 (✓) *target: truth*
  > Joh 14:17 even the Spirit of truth , whom the world cannot receive , because it neither sees him nor knows him . You know him , for he dwells with you and will be in you .
- **Joh 15:26** (✓) *target: truth*
  > Joh 15:26 “But when the Helper comes , whom I will send to you from the Father , the Spirit of truth , who proceeds from the Father , he will bear witness about me .
- **Joh 16:7** (✓) *target: truth*
  > Joh 16:7 Nevertheless , I tell you the truth : it is to your advantage that I go away , for if I do not go away , the Helper will not come to you . But if I go , I will send him to you .
- **Joh 16:13** (✓) *target: truth*
  > Joh 16:13 When the Spirit of truth comes , he will guide you into all the truth , for he will not speak on his own authority, but whatever he hears he will speak , and he will declare to you the things that are to come .
- **1Jo 4:6** (✓) *target: truth*
  > 1Jo 4:6 We are from God . Whoever knows God listens to us ; whoever is not from God does not listen to us . By this we know the Spirit of truth and the spirit of error .
- **1Jo 5:6** (✓) *target: truth*
  > 1Jo 5:6 This is he who came by water and blood — Jesus Christ ; not by the water only but by the water and the blood . And the Spirit is the one who testifies , because the Spirit is the truth .

**Group `1197-005`** (12 verses — anchors: Joh 4:23)

- **Joh 4:23** 🔵 (✓) *target: truth*
  > Joh 4:23 But the hour is coming , and is now here, when the true worshipers will worship the Father in spirit and truth , for the Father is seeking such people to worship him .
- **Joh 1:14** (✓) *target: truth*
  > Joh 1:14 And the Word became flesh and dwelt among us , and we have seen his glory , glory as of the only Son from the Father , full of grace and truth .
- **Joh 1:17** (✓) *target: truth*
  > Joh 1:17 For the law was given through Moses ; grace and truth came through Jesus Christ .
- **Joh 4:24** (✓) *target: truth*
  > Joh 4:24 God is spirit , and those who worship him must worship in spirit and truth .”
- **Joh 14:6** (✓) *target: truth*
  > Joh 14:6 Jesus said to him , “ I am the way , and the truth , and the life . No one comes to the Father except through me .
- **Joh 18:37** (✓) *target: truth*
  > Joh 18:37 Then Pilate said to him , “ So you are a king ?” Jesus answered , “ You say that I am a king . For this purpose I was born and for this purpose I have come into the world — to bear witness to the truth . Everyone who is of the truth listens to my voice .”
- **Rom 3:7** (✓) *target: truth*
  > Rom 3:7 But if through my lie God’s truth abounds to his glory , why am I still being condemned as a sinner ?
- **Rom 15:8** (✓) *target: truthfulness*
  > Rom 15:8 For I tell you that Christ became a servant to the circumcised to show God’s truthfulness , in order to confirm the promises given to the patriarchs ,
- **2Pe 2:2** (✓) *target: truth*
  > 2Pe 2:2 And many will follow their sensuality , and because of them the way of truth will be blasphemed .
- **1Jo 2:21** (✓) *target: truth*
  > 1Jo 2:21 I write to you , not because you do not know the truth , but because you know it , and because no lie is of the truth .
- **2Jo 1** (✓) *target: truth*
  > 2Jo 1 The elder to the elect lady and her children , whom I love in truth , and not only I , but also all who know the truth ,
- **2Jo 2** (✓) *target: truth*
  > 2Jo 2 because of the truth that abides in us and will be with us forever :

**Group `1197-006`** (14 verses — anchors: 1Ti 2:4)

- **1Ti 2:4** 🔵 (✓) *target: truth*
  > 1Ti 2:4 who desires all people to be saved and to come to the knowledge of the truth .
- **Rom 1:25** (✓) *target: truth*
  > Rom 1:25 because they exchanged the truth about God for a lie and worshiped and served the creature rather than the Creator , who is blessed forever ! Amen .
- **Rom 2:20** (✓) *target: truth*
  > Rom 2:20 an instructor of the foolish , a teacher of children , having in the law the embodiment of knowledge and truth —
- **Gal 2:5** (✓) *target: truth*
  > Gal 2:5 to them we did not yield in submission even for a moment , so that the truth of the gospel might be preserved for you .
- **Gal 2:14** (✓) *target: truth*
  > Gal 2:14 But when I saw that their conduct was not in step with the truth of the gospel , I said to Cephas before them all , “ If you , though a Jew , live like a Gentile and not like a Jew , how can you force the Gentiles to live like Jews ?”
- **Eph 1:13** (✓) *target: truth*
  > Eph 1:13 In him you also , when you heard the word of truth , the gospel of your salvation , and believed in him , were sealed with the promised Holy Spirit ,
- **Col 1:5** (✓) *target: truth*
  > Col 1:5 because of the hope laid up for you in heaven . Of this you have heard before in the word of the truth , the gospel ,
- **1Ti 3:15** (✓) *target: truth*
  > 1Ti 3:15 if I delay , you may know how one ought to behave in the household of God , which is the church of the living God , a pillar and buttress of the truth .
- **2Ti 2:15** (✓) *target: truth*
  > 2Ti 2:15 Do your best to present yourself to God as one approved , a worker who has no need to be ashamed , rightly handling the word of truth .
- **2Ti 2:25** (✓) *target: truth*
  > 2Ti 2:25 correcting his opponents with gentleness . God may perhaps grant them repentance leading to a knowledge of the truth ,
- **2Ti 3:7** (✓) *target: truth*
  > 2Ti 3:7 always learning and never able to arrive at a knowledge of the truth .
- **Tit 1:1** (✓) *target: truth*
  > Tit 1:1 Paul , a servant of God and an apostle of Jesus Christ , for the sake of the faith of God’s elect and their knowledge of the truth , which accords with godliness ,
- **Jam 1:18** (✓) *target: truth*
  > Jam 1:18 Of his own will he brought us forth by the word of truth , that we should be a kind of firstfruits of his creatures .
- **2Pe 1:12** (✓) *target: truth*
  > 2Pe 1:12 Therefore I intend always to remind you of these qualities, though you know them and are established in the truth that you have .

**Group `UNCLASSIFIED`** (14 verses)

- **Mat 22:16** (—) *target: truthfully*
  > Mat 22:16 And they sent their disciples to him , along with the Herodians , saying , “ Teacher , we know that you are true and teach the way of God truthfully , and you do not care about anyone’s opinion , for you are not swayed by appearances .
- **Mar 5:33** (—) *target: truth*
  > Mar 5:33 But the woman , knowing what had happened to her , came in fear and trembling and fell down before him and told him the whole truth .
- **Mar 12:14** (—) *target: truly*
  > Mar 12:14 And they came and said to him , “ Teacher , we know that you are true and do not care about anyone’s opinion . For you are not swayed by appearances , but truly teach the way of God . Is it lawful to pay taxes to Caesar , or not ? Should we pay them, or should we not ?”
- **Mar 12:32** (—) *target: truly*
  > Mar 12:32 And the scribe said to him , “You are right , Teacher . You have truly said that he is one , and there is no other besides him .
- **Luk 4:25** (—) *target: truth*
  > Luk 4:25 But in truth , I tell you , there were many widows in Israel in the days of Elijah , when the heavens were shut up three years and six months , and a great famine came over all the land ,
- **Luk 20:21** (—) *target: truly*
  > Luk 20:21 So they asked him , “ Teacher , we know that you speak and teach rightly , and show no partiality , but truly teach the way of God .
- **Luk 22:59** (—) *target: Certainly*
  > Luk 22:59 And after an interval of about an hour still another insisted , saying , “ Certainly this man also was with him , for he too is a Galilean .”
- **Joh 18:38** (—) *target: truth*
  > Joh 18:38 Pilate said to him , “ What is truth ?” After he had said this , he went back outside to the Jews and told them , “ I find no guilt in him .
- **Act 4:27** (—) *target: truly*
  > Act 4:27 for truly in this city there were gathered together against your holy servant Jesus , whom you anointed , both Herod and Pontius Pilate , along with the Gentiles and the peoples of Israel ,
- **Act 10:34** (—) *target: Truly*
  > Act 10:34 So Peter opened his mouth and said : “ Truly I understand that God shows no partiality ,
- **Act 26:25** (—) *target: true*
  > Act 26:25 But Paul said , “I am not out of my mind , most excellent Festus , but I am speaking true and rational words .
- **2Cor 7:14** (—) *target: true*
  > 2Cor 7:14 For whatever boasts I made to him about you , I was not put to shame . But just as everything we said to you was true , so also our boasting before Titus has proved true .
- **2Cor 12:6** (—) *target: truth*
  > 2Cor 12:6 though if I should wish to boast , I would not be a fool , for I would be speaking the truth ; but I refrain from it, so that no one may think more of me than he sees in me or hears from me .
- **Phili 1:18** (—) *target: truth*
  > Phili 1:18 What then ? Only that in every way , whether in pretense or in truth , Christ is proclaimed , and in that I rejoice . Yes , and I will rejoice ,

### `G0226` — 2/2 classified · 1 anchor verse(s)

**Group `6590-001`** (2 verses — anchors: Eph 4:15)

- **Eph 4:15** 🔵 (✓) *target: truth*
  > Eph 4:15 Rather , speaking the truth in love , we are to grow up in every way into him who is the head , into Christ ,
- **Gal 4:16** (✓) *target: truth*
  > Gal 4:16 Have I then become your enemy by telling you the truth ?

### `G0227` — 8/25 classified · 1 anchor verse(s)

**Group `6588-001`** (8 verses — anchors: Phili 4:8)

- **Phili 4:8** 🔵 (✓) *target: true*
  > Phili 4:8 Finally , brothers , whatever is true , whatever is honorable , whatever is just , whatever is pure , whatever is lovely , whatever is commendable , if there is any excellence , if there is anything worthy of praise , think about these things .
- **Joh 7:18** (✓) *target: true*
  > Joh 7:18 The one who speaks on his own authority seeks his own glory ; but the one who seeks the glory of him who sent him is true , and in him there is no falsehood .
- **Act 12:9** (✓) *target: real*
  > Act 12:9 And he went out and followed him . He did not know that what was being done by the angel was real , but thought he was seeing a vision .
- **Rom 3:4** (✓) *target: true*
  > Rom 3:4 By no means ! Let God be true though every one were a liar , as it is written , “ That you may be justified in your words , and prevail when you are judged .”
- **2Cor 6:8** (✓) *target: true*
  > 2Cor 6:8 through honor and dishonor , through slander and praise . We are treated as impostors , and yet are true ;
- **1Pe 5:12** (✓) *target: true*
  > 1Pe 5:12 By Silvanus , a faithful brother as I regard him, I have written briefly to you, exhorting and declaring that this is the true grace of God . Stand firm in it.
- **1Jo 2:8** (✓) *target: true*
  > 1Jo 2:8 At the same time , it is a new commandment that I am writing to you , which is true in him and in you , because the darkness is passing away and the true light is already shining .
- **1Jo 2:27** (✓) *target: true*
  > 1Jo 2:27 But the anointing that you received from him abides in you , and you have no need that anyone should teach you . But as his anointing teaches you about everything , and is true , and is no lie — just as it has taught you , abide in him .

**Group `UNCLASSIFIED`** (17 verses)

- **Mat 22:16** (—) *target: true*
  > Mat 22:16 And they sent their disciples to him , along with the Herodians , saying , “ Teacher , we know that you are true and teach the way of God truthfully , and you do not care about anyone’s opinion , for you are not swayed by appearances .
- **Mar 12:14** (—) *target: true*
  > Mar 12:14 And they came and said to him , “ Teacher , we know that you are true and do not care about anyone’s opinion . For you are not swayed by appearances , but truly teach the way of God . Is it lawful to pay taxes to Caesar , or not ? Should we pay them, or should we not ?”
- **Joh 3:33** (—) *target: true*
  > Joh 3:33 Whoever receives his testimony sets his seal to this, that God is true .
- **Joh 4:18** (—) *target: true*
  > Joh 4:18 for you have had five husbands , and the one you now have is not your husband . What you have said is true .”
- **Joh 5:31** (—) *target: true*
  > Joh 5:31 If I alone bear witness about myself , my testimony is not true .
- **Joh 5:32** (—) *target: true*
  > Joh 5:32 There is another who bears witness about me , and I know that the testimony that he bears about me is true .
- **Joh 6:55** (—) *target: true*
  > Joh 6:55 For my flesh is true food , and my blood is true drink .
- **Joh 8:13** (—) *target: true*
  > Joh 8:13 So the Pharisees said to him , “ You are bearing witness about yourself ; your testimony is not true .”
- **Joh 8:14** (—) *target: true*
  > Joh 8:14 Jesus answered , “ Even if I do bear witness about myself , my testimony is true , for I know where I came from and where I am going , but you do not know where I come from or where I am going .
- **Joh 8:17** (—) *target: true*
  > Joh 8:17 In your Law it is written that the testimony of two people is true .
- **Joh 8:26** (—) *target: true*
  > Joh 8:26 I have much to say about you and much to judge , but he who sent me is true , and I declare to the world what I have heard from him .”
- **Joh 10:41** (—) *target: true*
  > Joh 10:41 And many came to him . And they said , “ John did no sign , but everything that John said about this man was true .”
- **Joh 19:35** (—) *target: truth*
  > Joh 19:35 He who saw it has borne witness — his testimony is true , and he knows that he is telling the truth — that you also may believe .
- **Joh 21:24** (—) *target: true*
  > Joh 21:24 This is the disciple who is bearing witness about these things , and who has written these things , and we know that his testimony is true .
- **Tit 1:13** (—) *target: true*
  > Tit 1:13 This testimony is true . Therefore rebuke them sharply , that they may be sound in the faith ,
- **2Pe 2:22** (—) *target: true*
  > 2Pe 2:22 What the true proverb says has happened to them : “The dog returns to its own vomit , and the sow , after washing herself, returns to wallow in the mire .”
- **3Jo 12** (—) *target: true*
  > 3Jo 12 Demetrius has received a good testimony from everyone , and from the truth itself . We also add our testimony , and you know that our testimony is true .

### `G0228` — 6/26 classified · 1 anchor verse(s)

**Group `6587-001`** (6 verses — anchors: Heb 10:22)

- **Heb 10:22** 🔵 (✓) *target: true*
  > Heb 10:22 let us draw near with a true heart in full assurance of faith , with our hearts sprinkled clean from an evil conscience and our bodies washed with pure water .
- **Luk 16:11** (✓) *target: true*
  > Luk 16:11 If then you have not been faithful in the unrighteous wealth , who will entrust to you the true riches?
- **Joh 4:23** (✓) *target: true*
  > Joh 4:23 But the hour is coming , and is now here, when the true worshipers will worship the Father in spirit and truth , for the Father is seeking such people to worship him .
- **1Th 1:9** (✓) *target: true*
  > 1Th 1:9 For they themselves report concerning us the kind of reception we had among you , and how you turned to God from idols to serve the living and true God ,
- **1Jo 2:8** (✓) *target: true*
  > 1Jo 2:8 At the same time , it is a new commandment that I am writing to you , which is true in him and in you , because the darkness is passing away and the true light is already shining .
- **1Jo 5:20** (✓) *target: true*
  > 1Jo 5:20 And we know that the Son of God has come and has given us understanding , so that we may know him who is true ; and we are in him who is true , in his Son Jesus Christ . He is the true God and eternal life .

**Group `UNCLASSIFIED`** (20 verses)

- **Joh 1:9** (—) *target: true*
  > Joh 1:9 The true light , which gives light to everyone , was coming into the world .
- **Joh 4:37** (—) *target: true*
  > Joh 4:37 For here the saying holds true , ‘ One sows and another reaps .’
- **Joh 6:32** (—) *target: true*
  > Joh 6:32 Jesus then said to them , “ Truly , truly , I say to you , it was not Moses who gave you the bread from heaven , but my Father gives you the true bread from heaven .
- **Joh 7:28** (—) *target: true*
  > Joh 7:28 So Jesus proclaimed , as he taught in the temple , “You know me , and you know where I come from. But I have not come of my own accord. He who sent me is true , and him you do not know .
- **Joh 8:16** (—) *target: true*
  > Joh 8:16 Yet even if I do judge , my judgment is true , for it is not I alone who judge, but I and the Father who sent me .
- **Joh 15:1** (—) *target: true*
  > Joh 15:1 “ I am the true vine , and my Father is the vinedresser .
- **Joh 17:3** (—) *target: true*
  > Joh 17:3 And this is eternal life , that they know you , the only true God , and Jesus Christ whom you have sent .
- **Joh 19:35** (—) *target: true*
  > Joh 19:35 He who saw it has borne witness — his testimony is true , and he knows that he is telling the truth — that you also may believe .
- **Heb 8:2** (—) *target: true*
  > Heb 8:2 a minister in the holy places , in the true tent that the Lord set up , not man .
- **Heb 9:24** (—) *target: true things*
  > Heb 9:24 For Christ has entered , not into holy places made with hands , which are copies of the true things , but into heaven itself , now to appear in the presence of God on our behalf .
- **Rev 3:7** (—) *target: true*
  > Rev 3:7 “ And to the angel of the church in Philadelphia write : ‘ The words of the holy one, the true one, who has the key of David , who opens and no one will shut , who shuts and no one opens .
- **Rev 3:14** (—) *target: true*
  > Rev 3:14 “ And to the angel of the church in Laodicea write : ‘ The words of the Amen , the faithful and true witness , the beginning of God’s creation .
- **Rev 6:10** (—) *target: true*
  > Rev 6:10 They cried out with a loud voice , “O Sovereign Lord , holy and true , how long before you will judge and avenge our blood on those who dwell on the earth ?”
- **Rev 15:3** (—) *target: true*
  > Rev 15:3 And they sing the song of Moses , the servant of God , and the song of the Lamb , saying , “ Great and amazing are your deeds , O Lord God the Almighty ! Just and true are your ways , O King of the nations !
- **Rev 16:7** (—) *target: true*
  > Rev 16:7 And I heard the altar saying , “ Yes , Lord God the Almighty , true and just are your judgments !”
- **Rev 19:2** (—) *target: true*
  > Rev 19:2 for his judgments are true and just ; for he has judged the great prostitute who corrupted the earth with her immorality , and has avenged on her the blood of his servants .”
- **Rev 19:9** (—) *target: true*
  > Rev 19:9 And the angel said to me , “ Write this: Blessed are those who are invited to the marriage supper of the Lamb .” And he said to me , “ These are the true words of God .”
- **Rev 19:11** (—) *target: True*
  > Rev 19:11 Then I saw heaven opened , and behold , a white horse ! The one sitting on it is called Faithful and True , and in righteousness he judges and makes war .
- **Rev 21:5** (—) *target: true*
  > Rev 21:5 And he who was seated on the throne said , “ Behold , I am making all things new .” Also he said , “ Write this down, for these words are trustworthy and true .”
- **Rev 22:6** (—) *target: true*
  > Rev 22:6 And he said to me , “ These words are trustworthy and true . And the Lord , the God of the spirits of the prophets , has sent his angel to show his servants what must soon take place .”

### `G0230` — 13/18 classified · 1 anchor verse(s)

**Group `6589-001`** (13 verses — anchors: Joh 1:47)

- **Joh 1:47** 🔵 (✓) *target: indeed*
  > Joh 1:47 Jesus saw Nathanael coming toward him and said of him , “ Behold , an Israelite indeed , in whom there is no deceit !”
- **Mat 14:33** (✓) *target: Truly*
  > Mat 14:33 And those in the boat worshiped him , saying , “ Truly you are the Son of God .”
- **Mat 27:54** (✓) *target: Truly*
  > Mat 27:54 When the centurion and those who were with him , keeping watch over Jesus , saw the earthquake and what took place , they were filled with awe and said , “ Truly this was the Son of God !”
- **Mar 15:39** (✓) *target: Truly*
  > Mar 15:39 And when the centurion , who stood facing him , saw that in this way he breathed his last , he said , “ Truly this man was the Son of God !”
- **Joh 4:42** (✓) *target: indeed*
  > Joh 4:42 They said to the woman , “It is no longer because of what you said that we believe , for we have heard for ourselves , and we know that this is indeed the Savior of the world .”
- **Joh 6:14** (✓) *target: indeed*
  > Joh 6:14 When the people saw the sign that he had done , they said , “ This is indeed the Prophet who is to come into the world !”
- **Joh 7:26** (✓) *target: really*
  > Joh 7:26 And here he is, speaking openly , and they say nothing to him ! Can it be that the authorities really know that this is the Christ ?
- **Joh 7:40** (✓) *target: really*
  > Joh 7:40 When they heard these words , some of the people said , “ This really is the Prophet .”
- **Joh 8:31** (✓) *target: truly*
  > Joh 8:31 So Jesus said to the Jews who had believed him , “ If you abide in my word , you are truly my disciples ,
- **Joh 17:8** (✓) *target: truth*
  > Joh 17:8 For I have given them the words that you gave me , and they have received them and have come to know in truth that I came from you ; and they have believed that you sent me .
- **Act 12:11** (✓) *target: sure*
  > Act 12:11 When Peter came to himself , he said , “ Now I am sure that the Lord has sent his angel and rescued me from the hand of Herod and from all that the Jewish people were expecting .”
- **1Th 2:13** (✓) *target: really*
  > 1Th 2:13 And we also thank God constantly for this , that when you received the word of God , which you heard from us , you accepted it not as the word of men but as what it really is , the word of God , which is at work in you believers .
- **1Jo 2:5** (✓) *target: truly*
  > 1Jo 2:5 but whoever keeps his word , in him truly the love of God is perfected . By this we may know that we are in him :

**Group `UNCLASSIFIED`** (5 verses)

- **Mat 26:73** (—) *target: Certainly*
  > Mat 26:73 After a little while the bystanders came up and said to Peter , “ Certainly you too are one of them , for your accent betrays you .”
- **Mar 14:70** (—) *target: Certainly*
  > Mar 14:70 But again he denied it. And after a little while the bystanders again said to Peter , “ Certainly you are one of them , for you are a Galilean .”
- **Luk 9:27** (—) *target: truly*
  > Luk 9:27 But I tell you truly , there are some standing here who will not taste death until they see the kingdom of God .”
- **Luk 12:44** (—) *target: Truly*
  > Luk 12:44 Truly , I say to you , he will set him over all his possessions .
- **Luk 21:3** (—) *target: Truly*
  > Luk 21:3 And he said , “ Truly , I tell you , this poor widow has put in more than all of them.

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**5 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `G0225` | truth | `not_done` | 90 | 6 | 76 |
| `G0226` | be truthful | `not_done` | 2 | 1 | 2 |
| `G0227` | true | `not_done` | 25 | 1 | 8 |
| `G0228` | true | `not_done` | 26 | 1 | 6 |
| `G0230` | truly | `not_done` | 18 | 1 | 13 |

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

### Registry-specific extensions for R164 truthfulness

_None._ No active non-tiered extensions in `wa_obs_question_catalogue` are sourced from registry 164 (truthfulness).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-02T15:25:01Z`
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

*End of readiness output v3 — wa-164-truthfulness.*