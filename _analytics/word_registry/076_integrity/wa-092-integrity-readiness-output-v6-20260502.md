# wa-092-integrity — Analysis Readiness Output (v6)

_v6 generation · 2026-05-02T15:24:53Z · schema 3.17.0 · catalogue v2-2026-04-29 (T0–T7)_

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

- **Registry no:** `92` · **word:** `integrity`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `wa-dimensionreview-instruction-v3_3-20260418`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 19  (programme-wide aggregate including XREF and historical terms — current OWNER count is 3, XREF 9)
- `phase1_verse_count`: 601  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 1 unresolved · **Existing session_b_findings:** 1

**Description:**

> Integrity is the quality of being undivided — the same throughout, with no gap between inner conviction and outer conduct. The Hebrew vocabulary here (tom, tummah) means completeness or wholeness: the person of integrity is one whose inner and outer life are not at war with each other. Integrity cannot be performed; it must be genuine. It is closely related to truthfulness, blamelessness, and uprightness, all of which describe different facets of the person whose inner and outer lives correspond.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-02T15:24:53Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[2]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 3 / 3
- **OWNER terms legacy-VC (not_done):** 0 / 3

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | ✓ |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H8538` | tum.mah | integrity | H | `extracted` | **`vc_completed`** | 2 | 5 | 1/0 | 5/0 | 2 |
| `H8549G` | ta.mim | unblemished | H | `extracted` | **`vc_completed`** | 2 | 51 | 2/0 | 6/45 | 3 |
| `G0861` | aftharsia | incorruptibility | G | `extracted` | **`vc_completed`** | 2 | 6 | 2/0 | 6/0 | 4 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H8538` — tum.mah "integrity"

**Identity:** mti=933 · ti=984 · language=Hebrew · status=`extracted` · md_v=2

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:59): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: integrity

**Root family:**
- `TAMIM` (Hebrew): integrity — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8535` tam "complete"
- `H8537` tom "integrity"
- `H8549G` ta.mim "unblemished"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549I` ta.mim "unblemished: complete"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `H8549G` — ta.mim "unblemished"

**Identity:** mti=934 · ti=985 · language=Hebrew · status=`extracted` · md_v=2

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:59): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: : unblemished/perfect
1) complete, whole, entire, sound
1a) complete, whole, entire
1b) whole, sound, healthful
1c) complete, entire (of time)
1d) sound, wholesome, unimpaired, innocent, having integrity
1e) what is complete or entirely in accord with truth and fact (neuter adj/subst)

**Root family:**
- `TAMIM` (Hebrew): integrity — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (9 total; sample of 9):**
- `H4974` me.tom "soundness"
- `H8535` tam "complete"
- `H8537` tom "integrity"
- `H8538` tum.mah "integrity"
- `H8549H` ta.mim "unblemished: blameless"
- `H8549I` ta.mim "unblemished: complete"
- `H8549J` ta.mim "unblemished: Thummim"
- `H8550` tum.mim "Thummim"
- `H8552` ta.mam "to finish"

### `G0861` — aftharsia "incorruptibility"

**Identity:** mti=935 · ti=987 · language=Greek · status=`extracted` · md_v=2

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:59): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: imperishableness, immortality 
incorruptibility, imperishableness 1Cor. 15:42, 53, 54; immortality, Rom. 2:7; 2Tim. 1:10; soundness, purity; ἐν ἀφθαρσιᾳ, purely, sincerely or constantly, unfailingly, Eph. 6:24

**Root family:**
- `AFTHARS` (Greek): incorruptibility — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (2 total; sample of 2):**
- `G0862` afthartos "incorruptible"
- `G5349` fthartos "perishable"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (9)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `H1932` | hu | he/she/it | H | 86 impurity | `extracted` | 22 |
| `H2007` | hen.nah | they [fem.] | H | 86 impurity | `extracted` | 28 |
| `H4974` | me.tom | soundness | H | 90 innocence | `extracted` | 4 |
| `H8535` | tam | complete | H | 90 innocence | `extracted` | 16 |
| `H8537` | tom | integrity | H | 90 innocence | `extracted` | 23 |
| `H8549H` | ta.mim | unblemished: blameless | H | 90 innocence | `extracted` | 27 |
| `H8549I` | ta.mim | unblemished: complete | H | 90 innocence | `extracted` | 6 |
| `H8549J` | ta.mim | unblemished: Thummim | H | 90 innocence | `extracted` | 1 |
| `H8552` | ta.mam | to finish | H | 147 sin | `extracted` | 26 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H8538` — 1 groups

- **`933-001`** — 5 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names integrity as the inner quality that the person holds fast and presents before God — the moral wholeness that defines character and guides conduct under pressure*

### `H8549G` — 2 groups

- **`934-001`** — 5 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term characterises God's way, works, and knowledge as perfect — the inner perfection of divine character and action as the ground of trust*
- **`934-002`** — 1 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term characterises the Torah as perfect — its completeness as the source of inner renewal of the soul*

### `G0861` — 2 groups

- **`935-001`** — 4 relevant · 2 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C10`
  - *Term names the eschatological transformation of the person — the putting on of incorruptibility and immortality at resurrection*
- **`935-002`** — 2 relevant · 2 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C10`
  - *Term names incorruptibility as the quality of inner love and the inner orientation of those who seek God's glory*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 90 innocence | 2 | `H8538,H8549G` |
| 148 sincerity | 2 | `H8538,H8549G` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 100 knowledge | 3 |
| 151 sorrow | 3 |
| 168 uprightness | 3 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 24 condemnation | Deu 32:4 |
| 31 corruption | 1Cor 15:42 |
| 59 faith | Pro 11:3 |
| 100 knowledge | Job 37:16 |
| 111 mercy | Job 2:3 |
| 120 perverseness | Pro 11:3 |
| 168 uprightness | Deu 32:4 |
| 175 wonder | Job 37:16 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-92-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> Group 935-001 (aftharsia — incorruptibility) introduces the eschatological transformation of the person at resurrection — a dimension not well captured by existing vocabulary labels. Assigned Theological/Divine-Human as best available fit. Session B should address whether incorruptibility belongs in the integrity domain or warrants separate treatment, and how eschatological constitution of the person relates to present moral character.

### H.2 Open SD pointers + research flags (1)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SD_POINTER` | DIM-92-SD001 | MEDIUM | D | 2026-04-07 |

#### DIM-92-SD001

> The eschatological transformation of the person (incorruptibility at resurrection, aftharsia G0861 in integrity Reg. 92; ashes to beauty, faint spirit to praise in faithfulness Reg. 60 group 872-007) is not adequately captured by existing dimension labels. Both groups are assigned Theological/Divine-Human as the best available fit. Session D should consider whether the programme needs a dedicated label for eschatological or transformational dimensions of the inner being.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `G0861` (1 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H8538` — 5/5 classified · 2 anchor verse(s)

**Group `933-001`** (5 verses — anchors: Job 2:3, Pro 11:3)

- **Job 2:3** 🔵 (✓) *target: integrity*
  > Job 2:3 And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and turns away from evil ? He still holds fast his integrity , although you incited me against him to destroy him without reason .”
- **Pro 11:3** 🔵 (✓) *target: integrity*
  > Pro 11:3 The integrity of the upright guides them, but the crookedness of the treacherous destroys them .
- **Job 2:9** (✓) *target: integrity*
  > Job 2:9 Then his wife said to him, “Do you still hold fast your integrity ? Curse God and die .”
- **Job 27:5** (✓) *target: integrity*
  > Job 27:5 Far be it from me to say that you are right ; till I die I will not put away my integrity from me .
- **Job 31:6** (✓) *target: integrity*
  > Job 31:6 (Let me be weighed in a just balance , and let God know my integrity !)

### `H8549G` — 51/51 classified · 3 anchor verse(s)

**Group `934-001`** (5 verses — anchors: Deu 32:4, Job 37:16)

- **Deu 32:4** 🔵 (✓) *target: perfect*
  > Deu 32:4 “The Rock , his work is perfect , for all his ways are justice . A God of faithfulness and without iniquity , just and upright is he .
- **Job 37:16** 🔵 (✓) *target: perfect*
  > Job 37:16 Do you know the balancings of the clouds , the wondrous works of him who is perfect in knowledge ,
- **2Sa 22:31** (✓) *target: perfect*
  > 2Sa 22:31 This God — his way is perfect ; the word of the Lord proves true ; he is a shield for all those who take refuge in him .
- **Job 36:4** (✓) *target: perfect*
  > Job 36:4 For truly my words are not false ; one who is perfect in knowledge is with you .
- **Psa 18:30** (✓) *target: perfect*
  > Psa 18:30 This God —his way is perfect ; the word of the Lord proves true ; he is a shield for all those who take refuge in him .

**Group `934-002`** (1 verse — anchors: Psa 19:7)

- **Psa 19:7** 🔵 (✓) *target: perfect*
  > Psa 19:7 The law of the Lord is perfect , reviving the soul ; the testimony of the Lord is sure , making wise the simple ;

**Group `SET-ASIDE`** (45 verses)

- **Exo 12:5** (✗) [set_aside: physical_only] *target: without blemish*
  > Exo 12:5 Your lamb shall be without blemish , a male a year old . You may take it from the sheep or from the goats ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Exo 29:1** (✗) [set_aside: physical_only] *target: without blemish*
  > Exo 29:1 “Now this is what you shall do to them to consecrate them, that they may serve me as priests . Take one bull of the herd and two rams without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 1:3** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 1:3 “If his offering is a burnt offering from the herd , he shall offer a male without blemish . He shall bring it to the entrance of the tent of meeting , that he may be accepted before the Lord .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 1:10** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 1:10 “ If his gift for a burnt offering is from the flock , from the sheep or goats , he shall bring a male without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 3:1** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 3:1 “If his offering is a sacrifice of peace offering , if he offers an animal from the herd , male or female , he shall offer it without blemish before the Lord .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 3:6** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 3:6 “If his offering for a sacrifice of peace offering to the Lord is an animal from the flock , male or female , he shall offer it without blemish .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 4:3** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 4:3 if it is the anointed priest who sins , thus bringing guilt on the people , then he shall offer for the sin that he has committed a bull from the herd without blemish to the Lord for a sin offering .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 4:23** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 4:23 or the sin which he has committed is made known to him, he shall bring as his offering a goat , a male without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 4:28** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 4:28 or the sin which he has committed is made known to him, he shall bring for his offering a goat , a female without blemish , for his sin which he has committed .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 4:32** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 4:32 “If he brings a lamb as his offering for a sin offering , he shall bring a female without blemish
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 5:15** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 5:15 “If anyone commits a breach of faith and sins unintentionally in any of the holy things of the Lord , he shall bring to the Lord as his compensation , a ram without blemish out of the flock , valued in silver shekels , according to the shekel of the sanctuary , for a guilt offering .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 5:18** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 5:18 He shall bring to the priest a ram without blemish out of the flock , or its equivalent , for a guilt offering , and the priest shall make atonement for him for the mistake that he made unintentionally , and he shall be forgiven .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 6:6** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 6:6 And he shall bring to the priest as his compensation to the Lord a ram without blemish out of the flock , or its equivalent , for a guilt offering .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 9:2** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 9:2 and he said to Aaron , “ Take for yourself a bull calf for a sin offering and a ram for a burnt offering , both without blemish , and offer them before the Lord .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 9:3** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 9:3 And say to the people of Israel , ‘ Take a male goat for a sin offering , and a calf and a lamb , both a year old without blemish , for a burnt offering ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 14:10** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 14:10 “And on the eighth day he shall take two male lambs without blemish , and one ewe lamb a year old without blemish , and a grain offering of three tenths of an ephah of fine flour mixed with oil , and one log of oil .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 22:19** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 22:19 if it is to be accepted for you it shall be a male without blemish , of the bulls or the sheep or the goats .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 22:21** (✗) [set_aside: physical_only] *target: perfect*
  > Lev 22:21 And when anyone offers a sacrifice of peace offerings to the Lord to fulfill a vow or as a freewill offering from the herd or from the flock , to be accepted it must be perfect ; there shall be no blemish in it .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 23:12** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 23:12 And on the day when you wave the sheaf , you shall offer a male lamb a year old without blemish as a burnt offering to the Lord .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Lev 23:18** (✗) [set_aside: physical_only] *target: without blemish*
  > Lev 23:18 And you shall present with the bread seven lambs a year old without blemish , and one bull from the herd and two rams . They shall be a burnt offering to the Lord , with their grain offering and their drink offerings , a food offering with a pleasing aroma to the Lord .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 6:14** (✗) [set_aside: physical_only] *target: blemish*
  > Num 6:14 and he shall bring his gift to the Lord , one male lamb a year old without blemish for a burnt offering , and one ewe lamb a year old without blemish as a sin offering , and one ram without blemish as a peace offering ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 19:2** (✗) [set_aside: physical_only] *target: defect*
  > Num 19:2 “This is the statute of the law that the Lord has commanded : Tell the people of Israel to bring you a red heifer without defect , in which there is no blemish , and on which a yoke has never come .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 28:3** (✗) [set_aside: physical_only] *target: blemish*
  > Num 28:3 And you shall say to them, This is the food offering that you shall offer to the Lord : two male lambs a year old without blemish , day by day , as a regular offering .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 28:9** (✗) [set_aside: physical_only] *target: blemish*
  > Num 28:9 “On the Sabbath day , two male lambs a year old without blemish , and two tenths of an ephah of fine flour for a grain offering , mixed with oil , and its drink offering :
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 28:11** (✗) [set_aside: physical_only] *target: blemish*
  > Num 28:11 “At the beginnings of your months , you shall offer a burnt offering to the Lord : two bulls from the herd , one ram , seven male lambs a year old without blemish ;
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 28:19** (✗) [set_aside: physical_only] *target: blemish*
  > Num 28:19 but offer a food offering , a burnt offering to the Lord : two bulls from the herd , one ram , and seven male lambs a year old ; see that they are without blemish ;
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 28:31** (✗) [set_aside: physical_only] *target: blemish*
  > Num 28:31 Besides the regular burnt offering and its grain offering , you shall offer them and their drink offering . See that they are without blemish .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:2** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:2 and you shall offer a burnt offering , for a pleasing aroma to the Lord : one bull from the herd , one ram , seven male lambs a year old without blemish ;
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:8** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:8 but you shall offer a burnt offering to the Lord , a pleasing aroma : one bull from the herd , one ram , seven male lambs a year old : see that they are without blemish .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:13** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:13 And you shall offer a burnt offering , a food offering , with a pleasing aroma to the Lord , thirteen bulls from the herd , two rams , fourteen male lambs a year old ; they shall be without blemish ;
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:17** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:17 “On the second day twelve bulls from the herd , two rams , fourteen male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:20** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:20 “On the third day eleven bulls , two rams , fourteen male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:23** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:23 “On the fourth day ten bulls , two rams , fourteen male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:26** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:26 “On the fifth day nine bulls , two rams , fourteen male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:29** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:29 “On the sixth day eight bulls , two rams , fourteen male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:32** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:32 “On the seventh day seven bulls , two rams , fourteen male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Num 29:36** (✗) [set_aside: physical_only] *target: blemish*
  > Num 29:36 but you shall offer a burnt offering , a food offering , with a pleasing aroma to the Lord : one bull , one ram , seven male lambs a year old without blemish ,
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 43:22** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 43:22 And on the second day you shall offer a male goat without blemish for a sin offering ; and the altar shall be purified , as it was purified with the bull .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 43:23** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 43:23 When you have finished purifying it, you shall offer a bull from the herd without blemish and a ram from the flock without blemish .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 43:25** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 43:25 For seven days you shall provide daily a male goat for a sin offering ; also, a bull from the herd and a ram from the flock , without blemish , shall be provided .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 45:18** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 45:18 “ Thus says the Lord God : In the first month, on the first day of the month , you shall take a bull from the herd without blemish , and purify the sanctuary .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 45:23** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 45:23 And on the seven days of the festival he shall provide as a burnt offering to the Lord seven young bulls and seven rams without blemish , on each of the seven days ; and a male goat daily for a sin offering .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 46:4** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 46:4 The burnt offering that the prince offers to the Lord on the Sabbath day shall be six lambs without blemish and a ram without blemish .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 46:6** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 46:6 On the day of the new moon he shall offer a bull from the herd without blemish , and six lambs and a ram , which shall be without blemish .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.
- **Eze 46:13** (✗) [set_aside: physical_only] *target: without blemish*
  > Eze 46:13 “You shall provide a lamb a year old without blemish for a burnt offering to the Lord daily ; morning by morning you shall provide it .
  - notes: Term qualifies a sacrificial animal as physically unblemished/perfect (without defect) — required as a precondition for cultic acceptability. The inner-being content of these verses (acceptance, atonement, covenantal standing) is carried by other vocabulary, not by ta.mim itself in this physical-cultic facet.

### `G0861` — 6/6 classified · 4 anchor verse(s)

**Group `935-001`** (4 verses — anchors: 1Cor 15:42, 1Cor 15:53)

- **1Cor 15:42** 🔵 (✓) *target: imperishable*
  > 1Cor 15:42 So is it with the resurrection of the dead . What is sown is perishable ; what is raised is imperishable .
- **1Cor 15:53** 🔵 (✓) *target: imperishable*
  > 1Cor 15:53 For this perishable body must put on the imperishable , and this mortal body must put on immortality .
- **1Cor 15:50** (✓) *target: imperishable*
  > 1Cor 15:50 I tell you this , brothers : flesh and blood cannot inherit the kingdom of God , nor does the perishable inherit the imperishable .
- **1Cor 15:54** (✓) *target: imperishable*
  > 1Cor 15:54 When the perishable puts on the imperishable , and the mortal puts on immortality , then shall come to pass the saying that is written : “ Death is swallowed up in victory .”

**Group `935-002`** (2 verses — anchors: Rom 2:7, Eph 6:24)

- **Rom 2:7** 🔵 (✓) *target: immortality*
  > Rom 2:7 to those who by patience in well-doing seek for glory and honor and immortality , he will give eternal life ;
- **Eph 6:24** 🔵 (✓) *target: incorruptible*
  > Eph 6:24 Grace be with all who love our Lord Jesus Christ with love incorruptible .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**No legacy-VC terms.** All OWNER terms in this registry are `vc_status='vc_completed'` — classifications were performed under v3_x contracts.

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

### Registry-specific extensions for R092 integrity

_None._ No active non-tiered extensions in `wa_obs_question_catalogue` are sourced from registry 92 (integrity).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-02T15:24:53Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[2]`

**Stage 1 quick checks:**

- Registry status fields populated: ✓
- OWNER term inventory non-empty: ✓
- All OWNER terms have at least 1 verse: ✓
- Researcher fields preserved: absent — researcher narrative not yet written

**Notes / concerns:**
- session_b_status='Verse Context Reset' — investigate whether this is current or stale post-VCB-13.

---

*End of readiness output v3 — wa-092-integrity.*