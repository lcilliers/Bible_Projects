# wa-077-honesty — Analysis Readiness Output (v6)

_v6 generation · 2026-05-02T15:24:44Z · schema 3.17.0 · catalogue v2-2026-04-29 (T0–T7)_

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

- **Registry no:** `77` · **word:** `honesty`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `wa-dimensionreview-instruction-v3_3-20260418`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 6  (programme-wide aggregate including XREF and historical terms — current OWNER count is 2, XREF 3)
- `phase1_verse_count`: 485  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 2 unresolved · **Existing session_b_findings:** 1

**Description:**

> Honesty is the inner commitment to correspondence between reality and what one says — speaking and acting in a way that does not misrepresent what is true. The Hebrew vocabulary here (tsedaqah, righteousness) is broader than honesty in the narrow sense, but the commitment to truthful speech is embedded throughout. Scripture treats honesty as a relational virtue: it honours the other person by giving them accurate access to reality. Dishonesty deforms relationship; honesty is one of the foundational conditions for genuine community.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-05-02T15:24:44Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 2
- **OWNER terms legacy-VC (not_done):** 2 / 2

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 2 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H6662` | tsad.diq | righteous | H | `extracted` | **`not_done`** | 1 | 184 | 3/0 | 174/0 | 4 |
| `H6666` | tse.da.qah | righteousness | H | `extracted` | **`not_done`** | 1 | 148 | 3/0 | 148/0 | 3 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H6662` — tsad.diq "righteous"

**Identity:** mti=3246 · ti=5651 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:07): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: just, lawful, righteous

Sub-senses (depth > 1): 5 entries — present in DB; first 15:
  - `1a` (under `None`): just, righteous (in government)
  - `1b` (under `None`): just, right (in one's cause)
  - `1c` (under `None`): just, righteous (in conduct and character)
  - `1d` (under `None`): righteous (as justified and vindicated by God)
  - `1e` (under `None`): right, correct, lawful

**Root family:**
- `TSADDIQ` (Hebrew): righteous — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (17 total; sample of 17):**
- `H6659G` tsa.doq "Zadok"
- `H6659H` tsa.doq "Zadok"
- `H6659I` tsa.doq "Zadok"
- `H6659J` tsa.doq "Zadok"
- `H6659K` tsa.doq "Zadok"
- `H6659L` tsa.doq "Zadok"
- `H6659M` tsa.doq "Zadok"
- `H6663` tsa.deq "to justify"
- `H6664G` tse.deq "righteousness"
- `H6664H` tse.deq "Righteousness [God]"
- `H6666` tse.da.qah "righteousness"
- `H6667G` tsid.qiy.ya.hu "Zedekiah"
- `H6667H` tsid.qiy.ya.hu "Zedekiah"
- `H6667I` tsid.qiy.ya.hu "Zedekiah"
- `H6667J` tsid.qiy.ya.hu "Zedekiah"
- … and 2 more shown of 17 total

### `H6666` — tse.da.qah "righteousness"

**Identity:** mti=911 · ti=952 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:08:07): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: justice, righteousness

Sub-senses (depth > 1): 12 entries — present in DB; first 15:
  - `1a` (under `None`): righteousness (in government)
  - `1a1` (under `None`): of judge, ruler, king
  - `1a2` (under `None`): of law
  - `1a3` (under `None`): of Davidic king Messiah
  - `1b` (under `None`): righteousness (of God's attribute)
  - `1c` (under `None`): righteousness (in a case or cause)
  - `1d` (under `None`): righteousness, truthfulness
  - `1e` (under `None`): righteousness (as ethically right)
  - `1f` (under `None`): righteousness (as vindicated), justification, salvation
  - `1f1` (under `None`): of God
  - `1f2` (under `None`): prosperity (of people)
  - `1g` (under `None`): righteous acts Aramaic equivalent: tsid.qah (צִדְקָה "righteousness" H6665)

**Root family:**
- `TSADDIQ` (Hebrew): righteous — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (18 total; sample of 18):**
- `H6659G` tsa.doq "Zadok"
- `H6659H` tsa.doq "Zadok"
- `H6659I` tsa.doq "Zadok"
- `H6659J` tsa.doq "Zadok"
- `H6659K` tsa.doq "Zadok"
- `H6659L` tsa.doq "Zadok"
- `H6659M` tsa.doq "Zadok"
- `H6662` tsad.diq "righteous"
- `H6663` tsa.deq "to justify"
- `H6664G` tse.deq "righteousness"
- `H6664H` tse.deq "Righteousness [God]"
- `H6665` tsid.qah "righteousness"
- `H6667G` tsid.qiy.ya.hu "Zedekiah"
- `H6667H` tsid.qiy.ya.hu "Zedekiah"
- `H6667I` tsid.qiy.ya.hu "Zedekiah"
- … and 3 more shown of 18 total

---

## E. XREF Terms [Unit 2] (3)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `H6663` | tsa.deq | to justify | H | 98 justice | `extracted` | 40 |
| `H6664G` | tse.deq | righteousness | H | 98 justice | `extracted` | 110 |
| `H6664H` | tse.deq | righteousness | H | 117 peace | `extracted_theological_anchor` | 2 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H6662` — 3 groups

- **`3246-001`** — 112 relevant · 2 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names the righteous person's inner moral character — the constitutive orientation of the whole inner being toward what is right before God and others*
- **`3246-002`** — 47 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names righteousness as the standard by which God tests and vindicates — the inner moral condition God sees, approves, rewards, and which may be abandoned*
- **`3246-003`** — 15 relevant · 1 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C10`
  - *Term names the inner response of the righteous person toward God — orientation of trust, joy, and praise*

### `H6666` — 3 groups

- **`911-001`** — 73 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names righteousness as the inner moral character of the person — right relationship with God and others expressed in just conduct, faithful dealing, and integrity*
- **`911-002`** — 25 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names righteousness as the status credited to or vindicated in the person by God — moral standing before God, including imputation*
- **`911-003`** — 50 relevant · 1 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C10`
  - *Term names righteousness as the divine character quality received, longed for, and responded to — gift, stream of salvation, ground of inner hope and exultation*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 98 justice | 2 | `H6666,H6662` |
| 139 righteousness | 2 | `H6666,H6662` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 172 wickedness | 79 |
| 73 guilt | 29 |
| 98 justice | 29 |
| 97 joy | 20 |
| 103 love | 19 |
| 168 uprightness | 19 |
| 187 strength | 19 |
| 135 repentance | 17 |
| 183 heart | 17 |
| 59 faith | 16 |
| 90 innocence | 16 |
| 182 Soul | 16 |
| 43 desire | 15 |
| 78 hope | 14 |
| 112 mind | 13 |
| 89 iniquity | 12 |
| 100 knowledge | 12 |
| 197 authority | 12 |
| 117 peace | 11 |
| 67 goodness | 10 |
| 160 thought | 10 |
| 8 appetite | 9 |
| 23 compassion | 9 |
| 123 pride | 9 |
| 174 wisdom | 9 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 44 despair | Gen 15:6 |
| 90 innocence | Hab 2:4 |
| 97 joy | Isa 61:10 |
| 98 justice | Hab 2:4 |
| 98 justice | Isa 53:11 |
| 112 mind | Gen 15:6 |
| 183 heart | Psa 7:9 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-77-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> Group 911-002 (tsedeqah) is the only group in C10 explicitly engaging imputed righteousness — moral standing credited to the person by God. Session B should examine the theological significance of credited moral standing as a distinct inner-being category, and how it relates to the possessed moral character described in adjacent groups.

### H.2 Open SD pointers + research flags (2)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SD_POINTER` | DIM-77-SD001 | MEDIUM | D | 2026-04-07 |
| `SD_POINTER` | DIM-77-SD002 | MEDIUM | Session D | 2026-05-02 |

#### DIM-77-SD001

> Registry 77 is named 'honesty' but all its terms are standard Hebrew righteousness vocabulary (tsaddiq H6662 and tsedeqah H6666). The registry label does not match its actual lexical content. Session D should address whether Registry 77 should be renamed 'righteousness' to accurately reflect its vocabulary, and how this relates to Registry 139 (righteousness, dikaioma G1345).

#### DIM-77-SD002

> R077 (tsaddiq/tsedeqah vocabulary) shows that Hebrew righteousness operates across two distinct inner-being registers in the same verse corpus: (1) Moral Character — the stable quality of the righteous person and the standard God applies; (2) Emotion-Positive — the joyful, responsive orientation of the person who receives righteousness as gift. This internal split is analytically significant for Session D: righteousness is simultaneously a moral constitution and an affective posture. The asymmetry of dominant subjects (GOD as assessor/creditor; HUMAN as bearer and responder) should be noted in any Session D synthesis of the righteousness concept.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `H6666` (1 flag(s))

- **`6`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H6662` — 174/184 classified · 4 anchor verse(s)

**Group `3246-001`** (112 verses — anchors: Isa 53:11, Hab 2:4)

- **Isa 53:11** 🔵 (✓) *target: righteous one*
  > Isa 53:11 Out of the anguish of his soul he shall see and be satisfied ; by his knowledge shall the righteous one , my servant , make many to be accounted righteous , and he shall bear their iniquities .
- **Hab 2:4** 🔵 (✓) *target: righteous*
  > Hab 2:4 “ Behold , his soul is puffed up ; it is not upright within him, but the righteous shall live by his faith .
- **Gen 6:9** (✓) *target: righteous*
  > Gen 6:9 These are the generations of Noah . Noah was a righteous man , blameless in his generation . Noah walked with God .
- **Exo 23:7** (✓) *target: righteous*
  > Exo 23:7 Keep far from a false charge , and do not kill the innocent and righteous , for I will not acquit the wicked .
- **Deu 4:8** (✓) *target: righteous*
  > Deu 4:8 And what great nation is there, that has statutes and rules so righteous as all this law that I set before you today ?
- **1Sa 24:17** (✓) *target: righteous*
  > 1Sa 24:17 He said to David , “You are more righteous than I, for you have repaid me good , whereas I have repaid you evil .
- **2Sa 4:11** (✓) *target: righteous*
  > 2Sa 4:11 How much more, when wicked men have killed a righteous man in his own house on his bed , shall I not now require his blood at your hand and destroy you from the earth ?”
- **2Sa 23:3** (✓) *target: justly*
  > 2Sa 23:3 The God of Israel has spoken ; the Rock of Israel has said to me: When one rules justly over men , ruling in the fear of God ,
- **1Ki 2:32** (✓) *target: righteous*
  > 1Ki 2:32 The Lord will bring back his bloody deeds on his own head , because , without the knowledge of my father David , he attacked and killed with the sword two men more righteous and better than himself, Abner the son of Ner , commander of the army of Israel , and Amasa the son of Jether , commander of the army of Judah .
- **Job 12:4** (✓) *target: just*
  > Job 12:4 I am a laughingstock to my friends ; I, who called to God and he answered me, a just and blameless man, am a laughingstock .
- **Job 17:9** (✓) *target: righteous*
  > Job 17:9 Yet the righteous holds to his way , and he who has clean hands grows stronger and stronger .
- **Job 27:17** (✓) *target: righteous*
  > Job 27:17 he may pile it up , but the righteous will wear it, and the innocent will divide the silver .
- **Job 32:1** (✓) *target: righteous*
  > Job 32:1 So these three men ceased to answer Job , because he was righteous in his own eyes .
- **Psa 1:5** (✓) *target: righteous*
  > Psa 1:5 Therefore the wicked will not stand in the judgment , nor sinners in the congregation of the righteous ;
- **Psa 11:3** (✓) *target: righteous*
  > Psa 11:3 if the foundations are destroyed , what can the righteous do ?
- **Psa 14:5** (✓) *target: righteous*
  > Psa 14:5 There they are in great terror , for God is with the generation of the righteous .
- **Psa 31:18** (✓) *target: righteous*
  > Psa 31:18 Let the lying lips be mute , which speak insolently against the righteous in pride and contempt .
- **Psa 34:21** (✓) *target: righteous*
  > Psa 34:21 Affliction will slay the wicked , and those who hate the righteous will be condemned .
- **Psa 37:12** (✓) *target: righteous*
  > Psa 37:12 The wicked plots against the righteous and gnashes his teeth at him,
- **Psa 37:16** (✓) *target: righteous*
  > Psa 37:16 Better is the little that the righteous has than the abundance of many wicked .
- **Psa 37:21** (✓) *target: righteous*
  > Psa 37:21 The wicked borrows but does not pay back, but the righteous is generous and gives ;
- **Psa 37:25** (✓) *target: righteous*
  > Psa 37:25 I have been young , and now am old , yet I have not seen the righteous forsaken or his children begging for bread .
- **Psa 37:29** (✓) *target: righteous*
  > Psa 37:29 The righteous shall inherit the land and dwell upon it forever .
- **Psa 37:30** (✓) *target: righteous*
  > Psa 37:30 The mouth of the righteous utters wisdom , and his tongue speaks justice .
- **Psa 37:32** (✓) *target: righteous*
  > Psa 37:32 The wicked watches for the righteous and seeks to put him to death .
- **Psa 69:28** (✓) *target: righteous*
  > Psa 69:28 Let them be blotted out of the book of the living ; let them not be enrolled among the righteous .
- **Psa 72:7** (✓) *target: righteous*
  > Psa 72:7 In his days may the righteous flourish , and peace abound , till the moon be no more !
- **Psa 75:10** (✓) *target: righteous*
  > Psa 75:10 All the horns of the wicked I will cut off , but the horns of the righteous shall be lifted up .
- **Psa 92:12** (✓) *target: righteous*
  > Psa 92:12 The righteous flourish like the palm tree and grow like a cedar in Lebanon .
- **Psa 94:21** (✓) *target: righteous*
  > Psa 94:21 They band together against the life of the righteous and condemn the innocent to death .
- **Psa 112:4** (✓) *target: righteous*
  > Psa 112:4 Light dawns in the darkness for the upright ; he is gracious , merciful , and righteous .
- **Psa 112:6** (✓) *target: righteous*
  > Psa 112:6 For the righteous will never be moved ; he will be remembered forever .
- **Psa 118:20** (✓) *target: righteous*
  > Psa 118:20 This is the gate of the Lord ; the righteous shall enter through it .
- **Psa 125:3** (✓) *target: righteous*
  > Psa 125:3 For the scepter of wickedness shall not rest on the land allotted to the righteous , lest the righteous stretch out their hands to do wrong .
- **Psa 141:5** (✓) *target: righteous man*
  > Psa 141:5 Let a righteous man strike me—it is a kindness ; let him rebuke me—it is oil for my head ; let my head not refuse it. Yet my prayer is continually against their evil deeds .
- **Pro 2:20** (✓) *target: righteous*
  > Pro 2:20 So you will walk in the way of the good and keep to the paths of the righteous .
- **Pro 3:33** (✓) *target: righteous*
  > Pro 3:33 The Lord’s curse is on the house of the wicked , but he blesses the dwelling of the righteous .
- **Pro 4:18** (✓) *target: righteous*
  > Pro 4:18 But the path of the righteous is like the light of dawn , which shines brighter and brighter until full day .
- **Pro 9:9** (✓) *target: righteous*
  > Pro 9:9 Give instruction to a wise man , and he will be still wiser ; teach a righteous man, and he will increase in learning .
- **Pro 10:3** (✓) *target: righteous*
  > Pro 10:3 The Lord does not let the righteous go hungry , but he thwarts the craving of the wicked .
- **Pro 10:6** (✓) *target: righteous*
  > Pro 10:6 Blessings are on the head of the righteous , but the mouth of the wicked conceals violence .
- **Pro 10:7** (✓) *target: righteous*
  > Pro 10:7 The memory of the righteous is a blessing , but the name of the wicked will rot .
- **Pro 10:11** (✓) *target: righteous*
  > Pro 10:11 The mouth of the righteous is a fountain of life , but the mouth of the wicked conceals violence .
- **Pro 10:16** (✓) *target: righteous*
  > Pro 10:16 The wage of the righteous leads to life , the gain of the wicked to sin .
- **Pro 10:20** (✓) *target: righteous*
  > Pro 10:20 The tongue of the righteous is choice silver ; the heart of the wicked is of little worth.
- **Pro 10:21** (✓) *target: righteous*
  > Pro 10:21 The lips of the righteous feed many , but fools die for lack of sense .
- **Pro 10:24** (✓) *target: righteous*
  > Pro 10:24 What the wicked dreads will come upon him, but the desire of the righteous will be granted .
- **Pro 10:25** (✓) *target: righteous*
  > Pro 10:25 When the tempest passes , the wicked is no more , but the righteous is established forever .
- **Pro 10:28** (✓) *target: righteous*
  > Pro 10:28 The hope of the righteous brings joy , but the expectation of the wicked will perish .
- **Pro 10:30** (✓) *target: righteous*
  > Pro 10:30 The righteous will never be removed , but the wicked will not dwell in the land .
- **Pro 10:31** (✓) *target: righteous*
  > Pro 10:31 The mouth of the righteous brings forth wisdom , but the perverse tongue will be cut off .
- **Pro 10:32** (✓) *target: righteous*
  > Pro 10:32 The lips of the righteous know what is acceptable , but the mouth of the wicked , what is perverse .
- **Pro 11:8** (✓) *target: righteous*
  > Pro 11:8 The righteous is delivered from trouble , and the wicked walks into it instead .
- **Pro 11:9** (✓) *target: righteous*
  > Pro 11:9 With his mouth the godless man would destroy his neighbor , but by knowledge the righteous are delivered .
- **Pro 11:10** (✓) *target: righteous*
  > Pro 11:10 When it goes well with the righteous , the city rejoices , and when the wicked perish there are shouts of gladness .
- **Pro 11:21** (✓) *target: righteous*
  > Pro 11:21 Be assured , an evil person will not go unpunished , but the offspring of the righteous will be delivered .
- **Pro 11:23** (✓) *target: righteous*
  > Pro 11:23 The desire of the righteous ends only in good , the expectation of the wicked in wrath .
- **Pro 11:28** (✓) *target: righteous*
  > Pro 11:28 Whoever trusts in his riches will fall , but the righteous will flourish like a green leaf .
- **Pro 11:30** (✓) *target: righteous*
  > Pro 11:30 The fruit of the righteous is a tree of life , and whoever captures souls is wise .
- **Pro 12:3** (✓) *target: righteous*
  > Pro 12:3 No one is established by wickedness , but the root of the righteous will never be moved .
- **Pro 12:5** (✓) *target: righteous*
  > Pro 12:5 The thoughts of the righteous are just ; the counsels of the wicked are deceitful .
- **Pro 12:7** (✓) *target: righteous*
  > Pro 12:7 The wicked are overthrown and are no more, but the house of the righteous will stand .
- **Pro 12:10** (✓) *target: righteous*
  > Pro 12:10 Whoever is righteous has regard for the life of his beast , but the mercy of the wicked is cruel .
- **Pro 12:12** (✓) *target: righteous*
  > Pro 12:12 Whoever is wicked covets the spoil of evildoers , but the root of the righteous bears fruit.
- **Pro 12:13** (✓) *target: righteous*
  > Pro 12:13 An evil man is ensnared by the transgression of his lips , but the righteous escapes from trouble .
- **Pro 12:21** (✓) *target: righteous*
  > Pro 12:21 No ill befalls the righteous , but the wicked are filled with trouble .
- **Pro 12:26** (✓) *target: righteous*
  > Pro 12:26 One who is righteous is a guide to his neighbor , but the way of the wicked leads them astray .
- **Pro 13:5** (✓) *target: righteous*
  > Pro 13:5 The righteous hates falsehood , but the wicked brings shame and disgrace .
- **Pro 13:9** (✓) *target: righteous*
  > Pro 13:9 The light of the righteous rejoices , but the lamp of the wicked will be put out .
- **Pro 13:21** (✓) *target: righteous*
  > Pro 13:21 Disaster pursues sinners , but the righteous are rewarded with good .
- **Pro 13:22** (✓) *target: righteous*
  > Pro 13:22 A good man leaves an inheritance to his children’s children , but the sinner’s wealth is laid up for the righteous .
- **Pro 13:25** (✓) *target: righteous*
  > Pro 13:25 The righteous has enough to satisfy his appetite , but the belly of the wicked suffers want .
- **Pro 14:19** (✓) *target: righteous*
  > Pro 14:19 The evil bow down before the good , the wicked at the gates of the righteous .
- **Pro 14:32** (✓) *target: righteous*
  > Pro 14:32 The wicked is overthrown through his evildoing , but the righteous finds refuge in his death .
- **Pro 15:6** (✓) *target: righteous*
  > Pro 15:6 In the house of the righteous there is much treasure , but trouble befalls the income of the wicked .
- **Pro 15:28** (✓) *target: righteous*
  > Pro 15:28 The heart of the righteous ponders how to answer , but the mouth of the wicked pours out evil things .
- **Pro 17:26** (✓) *target: righteous*
  > Pro 17:26 To impose a fine on a righteous man is not good , nor to strike the noble for their uprightness .
- **Pro 20:7** (✓) *target: righteous*
  > Pro 20:7 The righteous who walks in his integrity — blessed are his children after him !
- **Pro 21:18** (✓) *target: righteous*
  > Pro 21:18 The wicked is a ransom for the righteous , and the traitor for the upright .
- **Pro 21:26** (✓) *target: righteous*
  > Pro 21:26 All day long he craves and craves , but the righteous gives and does not hold back .
- **Pro 24:15** (✓) *target: righteous*
  > Pro 24:15 Lie not in wait as a wicked man against the dwelling of the righteous ; do no violence to his home ;
- **Pro 24:16** (✓) *target: righteous*
  > Pro 24:16 for the righteous falls seven times and rises again , but the wicked stumble in times of calamity .
- **Pro 25:26** (✓) *target: righteous man*
  > Pro 25:26 Like a muddied spring or a polluted fountain is a righteous man who gives way before the wicked .
- **Pro 28:1** (✓) *target: righteous*
  > Pro 28:1 The wicked flee when no one pursues , but the righteous are bold as a lion .
- **Pro 28:12** (✓) *target: righteous*
  > Pro 28:12 When the righteous triumph , there is great glory , but when the wicked rise , people hide themselves .
- **Isa 3:10** (✓) *target: righteous*
  > Isa 3:10 Tell the righteous that it shall be well with them, for they shall eat the fruit of their deeds .
- **Isa 24:16** (✓) *target: Righteous One*
  > Isa 24:16 From the ends of the earth we hear songs of praise , of glory to the Righteous One . But I say , “I waste away , I waste away . Woe is me! For the traitors have betrayed , with betrayal the traitors have betrayed .”
- **Isa 26:2** (✓) *target: righteous*
  > Isa 26:2 Open the gates , that the righteous nation that keeps faith may enter in .
- **Isa 26:7** (✓) *target: righteous*
  > Isa 26:7 The path of the righteous is level ; you make level the way of the righteous .
- **Isa 57:1** (✓) *target: righteous man*
  > Isa 57:1 The righteous man perishes , and no one lays it to heart ; devout men are taken away , while no one understands . For the righteous man is taken away from calamity ;
- **Isa 60:21** (✓) *target: righteous*
  > Isa 60:21 Your people shall all be righteous ; they shall possess the land forever , the branch of my planting , the work of my hands , that I might be glorified .
- **Jer 23:5** (✓) *target: righteous*
  > Jer 23:5 “ Behold , the days are coming , declares the Lord , when I will raise up for David a righteous Branch , and he shall reign as king and deal wisely , and shall execute justice and righteousness in the land .
- **Lam 4:13** (✓) *target: righteous*
  > Lam 4:13 This was for the sins of her prophets and the iniquities of her priests , who shed in the midst of her the blood of the righteous .
- **Eze 3:20** (✓) *target: righteous*
  > Eze 3:20 Again, if a righteous person turns from his righteousness and commits injustice , and I lay a stumbling block before him , he shall die . Because you have not warned him , he shall die for his sin , and his righteous deeds that he has done shall not be remembered , but his blood I will require at your hand .
- **Eze 3:21** (✓) *target: righteous person*
  > Eze 3:21 But if you warn the righteous person not to sin , and he does not sin , he shall surely live , because he took warning, and you will have delivered your soul .”
- **Eze 13:22** (✓) *target: righteous*
  > Eze 13:22 Because you have disheartened the righteous falsely , although I have not grieved him, and you have encouraged the wicked , that he should not turn from his evil way to save his life ,
- **Eze 18:5** (✓) *target: righteous*
  > Eze 18:5 “ If a man is righteous and does what is just and right —
- **Eze 18:9** (✓) *target: righteous*
  > Eze 18:9 walks in my statutes , and keeps my rules by acting faithfully —he is righteous ; he shall surely live , declares the Lord God .
- **Eze 18:20** (✓) *target: righteous*
  > Eze 18:20 The soul who sins shall die . The son shall not suffer for the iniquity of the father , nor the father suffer for the iniquity of the son . The righteousness of the righteous shall be upon himself, and the wickedness of the wicked shall be upon himself.
- **Eze 18:24** (✓) *target: righteous person*
  > Eze 18:24 But when a righteous person turns away from his righteousness and does injustice and does the same abominations that the wicked person does , shall he live ? None of the righteous deeds that he has done shall be remembered ; for the treachery of which he is guilty and the sin he has committed , for them he shall die .
- **Eze 18:26** (✓) *target: righteous person*
  > Eze 18:26 When a righteous person turns away from his righteousness and does injustice , he shall die for it; for the injustice that he has done he shall die .
- **Eze 21:3** (✓) *target: righteous*
  > Eze 21:3 and say to the land of Israel , Thus says the Lord : Behold , I am against you and will draw my sword from its sheath and will cut off from you both righteous and wicked .
- **Eze 21:4** (✓) *target: righteous*
  > Eze 21:4 Because I will cut off from you both righteous and wicked , therefore my sword shall be drawn from its sheath against all flesh from south to north .
- **Eze 33:12** (✓) *target: righteous*
  > Eze 33:12 “And you , son of man , say to your people , The righteousness of the righteous shall not deliver him when he transgresses , and as for the wickedness of the wicked , he shall not fall by it when he turns from his wickedness , and the righteous shall not be able to live by his righteousness when he sins .
- **Eze 33:13** (✓) *target: righteous*
  > Eze 33:13 Though I say to the righteous that he shall surely live , yet if he trusts in his righteousness and does injustice , none of his righteous deeds shall be remembered , but in his injustice that he has done he shall die .
- **Eze 33:18** (✓) *target: righteous*
  > Eze 33:18 When the righteous turns from his righteousness and does injustice , he shall die for it .
- **Hos 14:9** (✓) *target: upright*
  > Hos 14:9 Whoever is wise , let him understand these things; whoever is discerning , let him know them; for the ways of the Lord are right , and the upright walk in them, but transgressors stumble in them .
- **Amo 2:6** (✓) *target: righteous*
  > Amo 2:6 Thus says the Lord : “For three transgressions of Israel , and for four , I will not revoke the punishment , because they sell the righteous for silver , and the needy for a pair of sandals —
- **Amo 5:12** (✓) *target: righteous*
  > Amo 5:12 For I know how many are your transgressions and how great are your sins — you who afflict the righteous , who take a bribe , and turn aside the needy in the gate .
- **Hab 1:4** (✓) *target: righteous*
  > Hab 1:4 So the law is paralyzed , and justice never goes forth . For the wicked surround the righteous ; so justice goes forth perverted .
- **Zec 9:9** (✓) *target: righteous*
  > Zec 9:9 Rejoice greatly , O daughter of Zion ! Shout aloud, O daughter of Jerusalem ! Behold , your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey , on a colt , the foal of a donkey .
- **Mal 3:18** (✓) *target: righteous*
  > Mal 3:18 Then once more you shall see the distinction between the righteous and the wicked , between one who serves God and one who does not serve him .

**Group `3246-002`** (47 verses — anchors: Psa 7:9)

- **Psa 7:9** 🔵 (✓) *target: righteous*
  > Psa 7:9 Oh, let the evil of the wicked come to an end , and may you establish the righteous — you who test the minds and hearts , O righteous God !
- **Gen 7:1** (✓) *target: righteous*
  > Gen 7:1 Then the Lord said to Noah , “ Go into the ark , you and all your household , for I have seen that you are righteous before me in this generation .
- **Gen 18:23** (✓) *target: righteous*
  > Gen 18:23 Then Abraham drew near and said , “Will you indeed sweep away the righteous with the wicked ?
- **Gen 18:24** (✓) *target: righteous*
  > Gen 18:24 Suppose there are fifty righteous within the city . Will you then sweep away the place and not spare it for the fifty righteous who are in it ?
- **Gen 18:25** (✓) *target: righteous*
  > Gen 18:25 Far be it from you to do such a thing , to put the righteous to death with the wicked , so that the righteous fare as the wicked ! Far be that from you! Shall not the Judge of all the earth do what is just ?”
- **Gen 18:26** (✓) *target: righteous*
  > Gen 18:26 And the Lord said , “ If I find at Sodom fifty righteous in the city , I will spare the whole place for their sake .”
- **Gen 18:28** (✓) *target: righteous*
  > Gen 18:28 Suppose five of the fifty righteous are lacking . Will you destroy the whole city for lack of five ?” And he said , “I will not destroy it if I find forty-five there .”
- **Gen 20:4** (✓) *target: innocent*
  > Gen 20:4 Now Abimelech had not approached her. So he said , “ Lord , will you kill an innocent people ?
- **Exo 9:27** (✓) *target: right*
  > Exo 9:27 Then Pharaoh sent and called Moses and Aaron and said to them, “This time I have sinned ; the Lord is in the right , and I and my people are in the wrong .
- **Exo 23:8** (✓) *target: right*
  > Exo 23:8 And you shall take no bribe , for a bribe blinds the clear-sighted and subverts the cause of those who are in the right .
- **Deu 16:19** (✓) *target: righteous*
  > Deu 16:19 You shall not pervert justice . You shall not show partiality , and you shall not accept a bribe , for a bribe blinds the eyes of the wise and subverts the cause of the righteous .
- **Deu 25:1** (✓) *target: innocent*
  > Deu 25:1 “ If there is a dispute between men and they come into court and the judges decide between them, acquitting the innocent and condemning the guilty ,
- **1Ki 8:32** (✓) *target: righteous*
  > 1Ki 8:32 then hear in heaven and act and judge your servants , condemning the guilty by bringing his conduct on his own head , and vindicating the righteous by rewarding him according to his righteousness .
- **2Ki 10:9** (✓) *target: innocent*
  > 2Ki 10:9 Then in the morning , when he went out , he stood and said to all the people , “You are innocent . It was I who conspired against my master and killed him, but who struck down all these ?
- **2Ch 6:23** (✓) *target: righteous*
  > 2Ch 6:23 then hear from heaven and act and judge your servants , repaying the guilty by bringing his conduct on his own head , and vindicating the righteous by rewarding him according to his righteousness .
- **Ezr 9:15** (✓) *target: just*
  > Ezr 9:15 O Lord , the God of Israel , you are just , for we are left a remnant that has escaped , as it is today . Behold , we are before you in our guilt , for none can stand before you because of this .”
- **Neh 9:8** (✓) *target: righteous*
  > Neh 9:8 You found his heart faithful before you, and made with him the covenant to give to his offspring the land of the Canaanite , the Hittite , the Amorite , the Perizzite , the Jebusite , and the Girgashite . And you have kept your promise , for you are righteous .
- **Job 34:17** (✓) *target: righteous*
  > Job 34:17 Shall one who hates justice govern ? Will you condemn him who is righteous and mighty ,
- **Job 36:7** (✓) *target: righteous*
  > Job 36:7 He does not withdraw his eyes from the righteous , but with kings on the throne he sets them forever , and they are exalted .
- **Psa 1:6** (✓) *target: righteous*
  > Psa 1:6 for the Lord knows the way of the righteous , but the way of the wicked will perish .
- **Psa 5:12** (✓) *target: righteous*
  > Psa 5:12 For you bless the righteous , O Lord ; you cover him with favor as with a shield .
- **Psa 11:5** (✓) *target: righteous*
  > Psa 11:5 The Lord tests the righteous , but his soul hates the wicked and the one who loves violence .
- **Psa 11:7** (✓) *target: righteous*
  > Psa 11:7 For the Lord is righteous ; he loves righteous deeds; the upright shall behold his face .
- **Psa 34:15** (✓) *target: righteous*
  > Psa 34:15 The eyes of the Lord are toward the righteous and his ears toward their cry .
- **Psa 34:19** (✓) *target: righteous*
  > Psa 34:19 Many are the afflictions of the righteous , but the Lord delivers him out of them all .
- **Psa 37:17** (✓) *target: righteous*
  > Psa 37:17 For the arms of the wicked shall be broken , but the Lord upholds the righteous .
- **Psa 37:39** (✓) *target: righteous*
  > Psa 37:39 The salvation of the righteous is from the Lord ; he is their stronghold in the time of trouble .
- **Psa 55:22** (✓) *target: righteous*
  > Psa 55:22 Cast your burden on the Lord , and he will sustain you; he will never permit the righteous to be moved .
- **Psa 58:11** (✓) *target: righteous*
  > Psa 58:11 Mankind will say , “ Surely there is a reward for the righteous ; surely there is a God who judges on earth .”
- **Psa 146:8** (✓) *target: righteous*
  > Psa 146:8 the Lord opens the eyes of the blind . The Lord lifts up those who are bowed down ; the Lord loves the righteous .
- **Pro 11:31** (✓) *target: righteous*
  > Pro 11:31 If the righteous is repaid on earth , how much more the wicked and the sinner !
- **Pro 15:29** (✓) *target: righteous*
  > Pro 15:29 The Lord is far from the wicked , but he hears the prayer of the righteous .
- **Pro 17:15** (✓) *target: righteous*
  > Pro 17:15 He who justifies the wicked and he who condemns the righteous are both alike an abomination to the Lord .
- **Pro 18:5** (✓) *target: righteous*
  > Pro 18:5 It is not good to be partial to the wicked or to deprive the righteous of justice .
- **Pro 18:17** (✓) *target: seems right*
  > Pro 18:17 The one who states his case first seems right , until the other comes and examines him .
- **Pro 21:12** (✓) *target: Righteous One*
  > Pro 21:12 The Righteous One observes the house of the wicked ; he throws the wicked down to ruin .
- **Pro 24:24** (✓) *target: right*
  > Pro 24:24 Whoever says to the wicked , “You are in the right ,” will be cursed by peoples , abhorred by nations ,
- **Isa 5:23** (✓) *target: right*
  > Isa 5:23 who acquit the guilty for a bribe , and deprive the innocent of his right !
- **Isa 29:21** (✓) *target: right*
  > Isa 29:21 who by a word make a man out to be an offender , and lay a snare for him who reproves in the gate , and with an empty plea turn aside him who is in the right .
- **Isa 41:26** (✓) *target: right*
  > Isa 41:26 Who declared it from the beginning , that we might know , and beforehand , that we might say , “He is right ”? There was none who declared it, none who proclaimed , none who heard your words .
- **Isa 45:21** (✓) *target: righteous*
  > Isa 45:21 Declare and present your case; let them take counsel together ! Who told this long ago ? Who declared it of old ? Was it not I , the Lord ? And there is no other god besides me, a righteous God and a Savior ; there is none besides me .
- **Isa 49:24** (✓) *target: tyrant*
  > Isa 49:24 Can the prey be taken from the mighty , or the captives of a tyrant be rescued ?
- **Jer 12:1** (✓) *target: Righteous*
  > Jer 12:1 Righteous are you , O Lord , when I complain to you; yet I would plead my case before you. Why does the way of the wicked prosper ? Why do all who are treacherous thrive ?
- **Jer 20:12** (✓) *target: righteous*
  > Jer 20:12 O Lord of hosts , who tests the righteous , who sees the heart and the mind , let me see your vengeance upon them, for to you have I committed my cause .
- **Lam 1:18** (✓) *target: right*
  > Lam 1:18 “The Lord is in the right , for I have rebelled against his word ; but hear , all you peoples , and see my suffering ; my young women and my young men have gone into captivity .
- **Eze 23:45** (✓) *target: righteous*
  > Eze 23:45 But righteous men shall pass judgment on them with the sentence of adulteresses , and with the sentence of women who shed blood , because they are adulteresses , and blood is on their hands .”
- **Hab 1:13** (✓) *target: righteous*
  > Hab 1:13 You who are of purer eyes than to see evil and cannot look at wrong , why do you idly look at traitors and remain silent when the wicked swallows up the man more righteous than he ?

**Group `3246-003`** (15 verses — anchors: Psa 64:10)

- **Psa 64:10** 🔵 (✓) *target: righteous*
  > Psa 64:10 Let the righteous one rejoice in the Lord and take refuge in him! Let all the upright in heart exult !
- **Job 22:19** (✓) *target: righteous*
  > Job 22:19 The righteous see it and are glad ; the innocent one mocks at them ,
- **Psa 32:11** (✓) *target: righteous*
  > Psa 32:11 Be glad in the Lord , and rejoice , O righteous , and shout for joy , all you upright in heart !
- **Psa 33:1** (✓) *target: righteous*
  > Psa 33:1 Shout for joy in the Lord , O you righteous ! Praise befits the upright .
- **Psa 52:6** (✓) *target: righteous*
  > Psa 52:6 The righteous shall see and fear , and shall laugh at him, saying,
- **Psa 58:10** (✓) *target: righteous*
  > Psa 58:10 The righteous will rejoice when he sees the vengeance ; he will bathe his feet in the blood of the wicked .
- **Psa 68:3** (✓) *target: righteous*
  > Psa 68:3 But the righteous shall be glad ; they shall exult before God ; they shall be jubilant with joy !
- **Psa 97:11** (✓) *target: righteous*
  > Psa 97:11 Light is sown for the righteous , and joy for the upright in heart .
- **Psa 97:12** (✓) *target: righteous*
  > Psa 97:12 Rejoice in the Lord , O you righteous , and give thanks to his holy name !
- **Psa 118:15** (✓) *target: righteous*
  > Psa 118:15 Glad songs of salvation are in the tents of the righteous : “The right hand of the Lord does valiantly ,
- **Psa 140:13** (✓) *target: righteous*
  > Psa 140:13 Surely the righteous shall give thanks to your name ; the upright shall dwell in your presence .
- **Psa 142:7** (✓) *target: righteous*
  > Psa 142:7 Bring me out of prison , that I may give thanks to your name ! The righteous will surround me, for you will deal bountifully with me .
- **Pro 18:10** (✓) *target: righteous man*
  > Pro 18:10 The name of the Lord is a strong tower ; the righteous man runs into it and is safe .
- **Pro 21:15** (✓) *target: righteous*
  > Pro 21:15 When justice is done , it is a joy to the righteous but terror to evildoers .
- **Pro 23:24** (✓) *target: righteous*
  > Pro 23:24 The father of the righteous will greatly rejoice ; he who fathers a wise son will be glad in him.

**Group `UNCLASSIFIED`** (10 verses)

- **Deu 32:4** (—) *target: just*
  > Deu 32:4 “The Rock , his work is perfect , for all his ways are justice . A God of faithfulness and without iniquity , just and upright is he .
- **2Ch 12:6** (—) *target: righteous*
  > 2Ch 12:6 Then the princes of Israel and the king humbled themselves and said , “The Lord is righteous .”
- **Neh 9:33** (—) *target: righteous*
  > Neh 9:33 Yet you have been righteous in all that has come upon us, for you have dealt faithfully and we have acted wickedly .
- **Psa 7:11** (—) *target: righteous*
  > Psa 7:11 God is a righteous judge , and a God who feels indignation every day .
- **Psa 116:5** (—) *target: righteous*
  > Psa 116:5 Gracious is the Lord , and righteous ; our God is merciful .
- **Psa 119:137** (—) *target: Righteous*
  > Tsadhe Psa 119:137 Righteous are you , O Lord , and right are your rules .
- **Psa 129:4** (—) *target: righteous*
  > Psa 129:4 The Lord is righteous ; he has cut the cords of the wicked .
- **Psa 145:17** (—) *target: righteous*
  > Psa 145:17 The Lord is righteous in all his ways and kind in all his works .
- **Dan 9:14** (—) *target: righteous*
  > Dan 9:14 Therefore the Lord has kept ready the calamity and has brought it upon us, for the Lord our God is righteous in all the works that he has done , and we have not obeyed his voice .
- **Zep 3:5** (—) *target: righteous*
  > Zep 3:5 The Lord within her is righteous ; he does no injustice ; every morning he shows forth his justice ; each dawn he does not fail ; but the unjust knows no shame .

### `H6666` — 148/148 classified · 3 anchor verse(s)

**Group `911-001`** (73 verses — anchors: Pro 21:3)

- **Pro 21:3** 🔵 (✓) *target: righteousness*
  > Pro 21:3 To do righteousness and justice is more acceptable to the Lord than sacrifice .
- **Gen 18:19** (✓) *target: righteousness*
  > Gen 18:19 For I have chosen him, that he may command his children and his household after him to keep the way of the Lord by doing righteousness and justice , so that the Lord may bring to Abraham what he has promised him .”
- **Gen 30:33** (✓) *target: honesty*
  > Gen 30:33 So my honesty will answer for me later , when you come to look into my wages with you . Every one that is not speckled and spotted among the goats and black among the lambs , if found with me , shall be counted stolen .”
- **Deu 33:21** (✓) *target: justice*
  > Deu 33:21 He chose the best of the land for himself, for there a commander’s portion was reserved ; and he came with the heads of the people , with Israel he executed the justice of the Lord , and his judgments for Israel .”
- **2Sa 8:15** (✓) *target: equity*
  > 2Sa 8:15 So David reigned over all Israel . And David administered justice and equity to all his people .
- **1Ki 3:6** (✓) *target: righteousness*
  > 1Ki 3:6 And Solomon said , “ You have shown great and steadfast love to your servant David my father , because he walked before you in faithfulness , in righteousness , and in uprightness of heart toward you. And you have kept for him this great and steadfast love and have given him a son to sit on his throne this day .
- **1Ki 10:9** (✓) *target: righteousness*
  > 1Ki 10:9 Blessed be the Lord your God , who has delighted in you and set you on the throne of Israel ! Because the Lord loved Israel forever , he has made you king , that you may execute justice and righteousness .”
- **1Ch 18:14** (✓) *target: equity*
  > 1Ch 18:14 So David reigned over all Israel , and he administered justice and equity to all his people .
- **2Ch 9:8** (✓) *target: justice*
  > 2Ch 9:8 Blessed be the Lord your God , who has delighted in you and set you on his throne as king for the Lord your God ! Because your God loved Israel and would establish them forever , he has made you king over them, that you may execute justice and righteousness .”
- **Job 27:6** (✓) *target: righteousness*
  > Job 27:6 I hold fast my righteousness and will not let it go ; my heart does not reproach me for any of my days .
- **Job 35:8** (✓) *target: righteousness*
  > Job 35:8 Your wickedness concerns a man like yourself, and your righteousness a son of man .
- **Psa 72:3** (✓) *target: righteousness*
  > Psa 72:3 Let the mountains bear prosperity for the people , and the hills , in righteousness !
- **Psa 99:4** (✓) *target: righteousness*
  > Psa 99:4 The King in his might loves justice . You have established equity ; you have executed justice and righteousness in Jacob .
- **Psa 106:3** (✓) *target: righteousness*
  > Psa 106:3 Blessed are they who observe justice , who do righteousness at all times !
- **Psa 112:3** (✓) *target: righteousness*
  > Psa 112:3 Wealth and riches are in his house , and his righteousness endures forever .
- **Psa 112:9** (✓) *target: righteousness*
  > Psa 112:9 He has distributed freely; he has given to the poor ; his righteousness endures forever ; his horn is exalted in honor .
- **Pro 8:18** (✓) *target: righteousness*
  > Pro 8:18 Riches and honor are with me, enduring wealth and righteousness .
- **Pro 8:20** (✓) *target: righteousness*
  > Pro 8:20 I walk in the way of righteousness , in the paths of justice ,
- **Pro 10:2** (✓) *target: righteousness*
  > Pro 10:2 Treasures gained by wickedness do not profit , but righteousness delivers from death .
- **Pro 11:4** (✓) *target: righteousness*
  > Pro 11:4 Riches do not profit in the day of wrath , but righteousness delivers from death .
- **Pro 11:5** (✓) *target: righteousness*
  > Pro 11:5 The righteousness of the blameless keeps his way straight , but the wicked falls by his own wickedness .
- **Pro 11:6** (✓) *target: righteousness*
  > Pro 11:6 The righteousness of the upright delivers them, but the treacherous are taken captive by their lust .
- **Pro 11:18** (✓) *target: righteousness*
  > Pro 11:18 The wicked earns deceptive wages , but one who sows righteousness gets a sure reward .
- **Pro 11:19** (✓) *target: righteousness*
  > Pro 11:19 Whoever is steadfast in righteousness will live , but he who pursues evil will die .
- **Pro 12:28** (✓) *target: righteousness*
  > Pro 12:28 In the path of righteousness is life , and in its pathway there is no death .
- **Pro 13:6** (✓) *target: Righteousness*
  > Pro 13:6 Righteousness guards him whose way is blameless , but sin overthrows the wicked .
- **Pro 14:34** (✓) *target: Righteousness*
  > Pro 14:34 Righteousness exalts a nation , but sin is a reproach to any people .
- **Pro 15:9** (✓) *target: righteousness*
  > Pro 15:9 The way of the wicked is an abomination to the Lord , but he loves him who pursues righteousness .
- **Pro 16:8** (✓) *target: righteousness*
  > Pro 16:8 Better is a little with righteousness than great revenues with injustice .
- **Pro 16:12** (✓) *target: righteousness*
  > Pro 16:12 It is an abomination to kings to do evil , for the throne is established by righteousness .
- **Pro 16:31** (✓) *target: righteous*
  > Pro 16:31 Gray hair is a crown of glory ; it is gained in a righteous life .
- **Pro 21:21** (✓) *target: righteousness*
  > Pro 21:21 Whoever pursues righteousness and kindness will find life , righteousness , and honor .
- **Isa 1:27** (✓) *target: righteousness*
  > Isa 1:27 Zion shall be redeemed by justice , and those in her who repent , by righteousness .
- **Isa 5:7** (✓) *target: righteousness*
  > Isa 5:7 For the vineyard of the Lord of hosts is the house of Israel , and the men of Judah are his pleasant planting ; and he looked for justice , but behold , bloodshed ; for righteousness , but behold , an outcry !
- **Isa 5:16** (✓) *target: righteousness*
  > Isa 5:16 But the Lord of hosts is exalted in justice , and the Holy God shows himself holy in righteousness .
- **Isa 9:7** (✓) *target: righteousness*
  > Isa 9:7 Of the increase of his government and of peace there will be no end , on the throne of David and over his kingdom , to establish it and to uphold it with justice and with righteousness from this time forth and forevermore . The zeal of the Lord of hosts will do this .
- **Isa 32:16** (✓) *target: righteousness*
  > Isa 32:16 Then justice will dwell in the wilderness , and righteousness abide in the fruitful field .
- **Isa 32:17** (✓) *target: righteousness*
  > Isa 32:17 And the effect of righteousness will be peace , and the result of righteousness , quietness and trust forever .
- **Isa 33:5** (✓) *target: righteousness*
  > Isa 33:5 The Lord is exalted , for he dwells on high ; he will fill Zion with justice and righteousness ,
- **Isa 33:15** (✓) *target: righteously*
  > Isa 33:15 He who walks righteously and speaks uprightly , who despises the gain of oppressions , who shakes his hands , lest they hold a bribe , who stops his ears from hearing of bloodshed and shuts his eyes from looking on evil ,
- **Isa 48:1** (✓) *target: right*
  > Isa 48:1 Hear this , O house of Jacob , who are called by the name of Israel , and who came from the waters of Judah , who swear by the name of the Lord and confess the God of Israel , but not in truth or right .
- **Isa 48:18** (✓) *target: righteousness*
  > Isa 48:18 Oh that you had paid attention to my commandments ! Then your peace would have been like a river , and your righteousness like the waves of the sea ;
- **Isa 54:14** (✓) *target: righteousness*
  > Isa 54:14 In righteousness you shall be established ; you shall be far from oppression , for you shall not fear ; and from terror , for it shall not come near you .
- **Isa 56:1** (✓) *target: righteousness*
  > Isa 56:1 Thus says the Lord : “ Keep justice , and do righteousness , for soon my salvation will come , and my righteousness be revealed .
- **Isa 58:2** (✓) *target: righteousness*
  > Isa 58:2 Yet they seek me daily and delight to know my ways , as if they were a nation that did righteousness and did not forsake the judgment of their God ; they ask of me righteous judgments ; they delight to draw near to God .
- **Isa 59:14** (✓) *target: righteousness*
  > Isa 59:14 Justice is turned back , and righteousness stands far away ; for truth has stumbled in the public squares , and uprightness cannot enter .
- **Isa 60:17** (✓) *target: righteousness*
  > Isa 60:17 Instead of bronze I will bring gold , and instead of iron I will bring silver ; instead of wood , bronze , instead of stones , iron . I will make your overseers peace and your taskmasters righteousness .
- **Isa 64:6** (✓) *target: righteous deeds*
  > Isa 64:6 We have all become like one who is unclean , and all our righteous deeds are like a polluted garment . We all fade like a leaf , and our iniquities , like the wind , take us away .
- **Jer 4:2** (✓) *target: righteousness*
  > Jer 4:2 and if you swear , ‘As the Lord lives ,’ in truth , in justice , and in righteousness , then nations shall bless themselves in him, and in him shall they glory .”
- **Jer 22:3** (✓) *target: righteousness*
  > Jer 22:3 Thus says the Lord : Do justice and righteousness , and deliver from the hand of the oppressor him who has been robbed . And do no wrong or violence to the resident alien , the fatherless , and the widow , nor shed innocent blood in this place .
- **Jer 22:15** (✓) *target: righteousness*
  > Jer 22:15 Do you think you are a king because you compete in cedar ? Did not your father eat and drink and do justice and righteousness ? Then it was well with him .
- **Jer 23:5** (✓) *target: righteousness*
  > Jer 23:5 “ Behold , the days are coming , declares the Lord , when I will raise up for David a righteous Branch , and he shall reign as king and deal wisely , and shall execute justice and righteousness in the land .
- **Jer 33:15** (✓) *target: righteous*
  > Jer 33:15 In those days and at that time I will cause a righteous Branch to spring up for David , and he shall execute justice and righteousness in the land .
- **Eze 3:20** (✓) *target: righteous deeds*
  > Eze 3:20 Again, if a righteous person turns from his righteousness and commits injustice , and I lay a stumbling block before him , he shall die . Because you have not warned him , he shall die for his sin , and his righteous deeds that he has done shall not be remembered , but his blood I will require at your hand .
- **Eze 18:5** (✓) *target: right*
  > Eze 18:5 “ If a man is righteous and does what is just and right —
- **Eze 18:19** (✓) *target: right*
  > Eze 18:19 “Yet you say , ‘ Why should not the son suffer for the iniquity of the father ?’ When the son has done what is just and right , and has been careful to observe all my statutes , he shall surely live .
- **Eze 18:21** (✓) *target: right*
  > Eze 18:21 “But if a wicked person turns away from all his sins that he has committed and keeps all my statutes and does what is just and right , he shall surely live ; he shall not die .
- **Eze 18:24** (✓) *target: righteousness*
  > Eze 18:24 But when a righteous person turns away from his righteousness and does injustice and does the same abominations that the wicked person does , shall he live ? None of the righteous deeds that he has done shall be remembered ; for the treachery of which he is guilty and the sin he has committed , for them he shall die .
- **Eze 18:26** (✓) *target: righteousness*
  > Eze 18:26 When a righteous person turns away from his righteousness and does injustice , he shall die for it; for the injustice that he has done he shall die .
- **Eze 18:27** (✓) *target: right*
  > Eze 18:27 Again, when a wicked person turns away from the wickedness he has committed and does what is just and right , he shall save his life .
- **Eze 33:12** (✓) *target: righteousness*
  > Eze 33:12 “And you , son of man , say to your people , The righteousness of the righteous shall not deliver him when he transgresses , and as for the wickedness of the wicked , he shall not fall by it when he turns from his wickedness , and the righteous shall not be able to live by his righteousness when he sins .
- **Eze 33:13** (✓) *target: righteousness*
  > Eze 33:13 Though I say to the righteous that he shall surely live , yet if he trusts in his righteousness and does injustice , none of his righteous deeds shall be remembered , but in his injustice that he has done he shall die .
- **Eze 33:14** (✓) *target: right*
  > Eze 33:14 Again, though I say to the wicked , ‘You shall surely die ,’ yet if he turns from his sin and does what is just and right ,
- **Eze 33:16** (✓) *target: right*
  > Eze 33:16 None of the sins that he has committed shall be remembered against him. He has done what is just and right ; he shall surely live .
- **Eze 33:18** (✓) *target: righteousness*
  > Eze 33:18 When the righteous turns from his righteousness and does injustice , he shall die for it .
- **Eze 33:19** (✓) *target: right*
  > Eze 33:19 And when the wicked turns from his wickedness and does what is just and right , he shall live by this.
- **Eze 45:9** (✓) *target: justice*
  > Eze 45:9 “ Thus says the Lord God : Enough , O princes of Israel ! Put away violence and oppression , and execute justice and righteousness . Cease your evictions of my people , declares the Lord God .
- **Hos 10:12** (✓) *target: righteousness*
  > Hos 10:12 Sow for yourselves righteousness ; reap steadfast love ; break up your fallow ground , for it is the time to seek the Lord , that he may come and rain righteousness upon you .
- **Amo 5:7** (✓) *target: righteousness*
  > Amo 5:7 O you who turn justice to wormwood and cast down righteousness to the earth !
- **Amo 5:24** (✓) *target: righteousness*
  > Amo 5:24 But let justice roll down like waters , and righteousness like an ever-flowing stream .
- **Amo 6:12** (✓) *target: righteousness*
  > Amo 6:12 Do horses run on rocks ? Does one plow there with oxen ? But you have turned justice into poison and the fruit of righteousness into wormwood —
- **Zec 8:8** (✓) *target: righteousness*
  > Zec 8:8 and I will bring them to dwell in the midst of Jerusalem . And they shall be my people , and I will be their God , in faithfulness and in righteousness .”
- **Mal 3:3** (✓) *target: righteousness*
  > Mal 3:3 He will sit as a refiner and purifier of silver , and he will purify the sons of Levi and refine them like gold and silver , and they will bring offerings in righteousness to the Lord .

**Group `911-002`** (25 verses — anchors: Gen 15:6)

- **Gen 15:6** 🔵 (✓) *target: righteousness*
  > Gen 15:6 And he believed the Lord , and he counted it to him as righteousness .
- **Deu 6:25** (✓) *target: righteousness*
  > Deu 6:25 And it will be righteousness for us, if we are careful to do all this commandment before the Lord our God , as he has commanded us .’
- **Deu 9:4** (✓) *target: righteousness*
  > Deu 9:4 “Do not say in your heart , after the Lord your God has thrust them out before you, ‘It is because of my righteousness that the Lord has brought me in to possess this land ,’ whereas it is because of the wickedness of these nations that the Lord is driving them out before you.
- **Deu 9:5** (✓) *target: righteousness*
  > Deu 9:5 Not because of your righteousness or the uprightness of your heart are you going in to possess their land , but because of the wickedness of these nations the Lord your God is driving them out from before you, and that he may confirm the word that the Lord swore to your fathers , to Abraham , to Isaac , and to Jacob .
- **Deu 9:6** (✓) *target: righteousness*
  > Deu 9:6 “ Know , therefore, that the Lord your God is not giving you this good land to possess because of your righteousness , for you are a stubborn people .
- **Deu 24:13** (✓) *target: righteousness*
  > Deu 24:13 You shall restore to him the pledge as the sun sets , that he may sleep in his cloak and bless you. And it shall be righteousness for you before the Lord your God .
- **Judg 5:11** (✓) *target: righteous triumphs*
  > Judg 5:11 To the sound of musicians at the watering places , there they repeat the righteous triumphs of the Lord , the righteous triumphs of his villagers in Israel . “Then down to the gates marched the people of the Lord .
- **1Sa 26:23** (✓) *target: righteousness*
  > 1Sa 26:23 The Lord rewards every man for his righteousness and his faithfulness , for the Lord gave you into my hand today , and I would not put out my hand against the Lord’s anointed .
- **2Sa 19:28** (✓) *target: right*
  > 2Sa 19:28 For all my father’s house were but men doomed to death before my lord the king , but you set your servant among those who eat at your table . What further right have I, then, to cry to the king ?”
- **2Sa 22:21** (✓) *target: righteousness*
  > 2Sa 22:21 “The Lord dealt with me according to my righteousness ; according to the cleanness of my hands he rewarded me .
- **2Sa 22:25** (✓) *target: righteousness*
  > 2Sa 22:25 And the Lord has rewarded me according to my righteousness , according to my cleanness in his sight .
- **1Ki 8:32** (✓) *target: righteousness*
  > 1Ki 8:32 then hear in heaven and act and judge your servants , condemning the guilty by bringing his conduct on his own head , and vindicating the righteous by rewarding him according to his righteousness .
- **2Ch 6:23** (✓) *target: righteousness*
  > 2Ch 6:23 then hear from heaven and act and judge your servants , repaying the guilty by bringing his conduct on his own head , and vindicating the righteous by rewarding him according to his righteousness .
- **Neh 2:20** (✓) *target: right*
  > Neh 2:20 Then I replied to them, “The God of heaven will make us prosper , and we his servants will arise and build , but you have no portion or right or claim in Jerusalem .”
- **Job 33:26** (✓) *target: righteousness*
  > Job 33:26 then man prays to God , and he accepts him; he sees his face with a shout of joy , and he restores to man his righteousness .
- **Psa 24:5** (✓) *target: righteousness*
  > Psa 24:5 He will receive blessing from the Lord and righteousness from the God of his salvation .
- **Psa 69:27** (✓) *target: acquittal*
  > Psa 69:27 Add to them punishment upon punishment ; may they have no acquittal from you.
- **Psa 106:31** (✓) *target: righteousness*
  > Psa 106:31 And that was counted to him as righteousness from generation to generation forever .
- **Isa 5:23** (✓) *target: innocent*
  > Isa 5:23 who acquit the guilty for a bribe , and deprive the innocent of his right !
- **Isa 54:17** (✓) *target: vindication*
  > Isa 54:17 no weapon that is fashioned against you shall succeed , and you shall refute every tongue that rises against you in judgment . This is the heritage of the servants of the Lord and their vindication from me, declares the Lord .”
- **Isa 57:12** (✓) *target: righteousness*
  > Isa 57:12 I will declare your righteousness and your deeds , but they will not profit you .
- **Eze 14:14** (✓) *target: righteousness*
  > Eze 14:14 even if these three men , Noah , Daniel , and Job , were in it , they would deliver but their own lives by their righteousness , declares the Lord God .
- **Eze 14:20** (✓) *target: righteousness*
  > Eze 14:20 even if Noah , Daniel , and Job were in it , as I live , declares the Lord God , they would deliver neither son nor daughter . They would deliver but their own lives by their righteousness .
- **Eze 18:20** (✓) *target: righteousness*
  > Eze 18:20 The soul who sins shall die . The son shall not suffer for the iniquity of the father , nor the father suffer for the iniquity of the son . The righteousness of the righteous shall be upon himself, and the wickedness of the wicked shall be upon himself.
- **Eze 18:22** (✓) *target: righteousness*
  > Eze 18:22 None of the transgressions that he has committed shall be remembered against him; for the righteousness that he has done he shall live .

**Group `911-003`** (50 verses — anchors: Isa 61:10)

- **Isa 61:10** 🔵 (✓) *target: righteousness*
  > Isa 61:10 I will greatly rejoice in the Lord ; my soul shall exult in my God , for he has clothed me with the garments of salvation ; he has covered me with the robe of righteousness , as a bridegroom decks himself like a priest with a beautiful headdress , and as a bride adorns herself with her jewels .
- **1Sa 12:7** (✓) *target: righteous deeds*
  > 1Sa 12:7 Now therefore stand still that I may plead with you before the Lord concerning all the righteous deeds of the Lord that he performed for you and for your fathers .
- **Job 37:23** (✓) *target: righteousness*
  > Job 37:23 The Almighty —we cannot find him; he is great in power ; justice and abundant righteousness he will not violate .
- **Psa 5:8** (✓) *target: righteousness*
  > Psa 5:8 Lead me, O Lord , in your righteousness because of my enemies ; make your way straight before me.
- **Psa 11:7** (✓) *target: righteous*
  > Psa 11:7 For the Lord is righteous ; he loves righteous deeds; the upright shall behold his face .
- **Psa 22:31** (✓) *target: righteousness*
  > Psa 22:31 they shall come and proclaim his righteousness to a people yet unborn, that he has done it.
- **Psa 31:1** (✓) *target: righteousness*
  > To the choirmaster . A Psalm of David . Psa 31:1 In you, O Lord , do I take refuge ; let me never be put to shame ; in your righteousness deliver me !
- **Psa 33:5** (✓) *target: righteousness*
  > Psa 33:5 He loves righteousness and justice ; the earth is full of the steadfast love of the Lord .
- **Psa 36:6** (✓) *target: righteousness*
  > Psa 36:6 Your righteousness is like the mountains of God ; your judgments are like the great deep ; man and beast you save , O Lord .
- **Psa 36:10** (✓) *target: righteousness*
  > Psa 36:10 Oh, continue your steadfast love to those who know you, and your righteousness to the upright of heart !
- **Psa 40:10** (✓) *target: deliverance*
  > Psa 40:10 I have not hidden your deliverance within my heart ; I have spoken of your faithfulness and your salvation ; I have not concealed your steadfast love and your faithfulness from the great congregation .
- **Psa 51:14** (✓) *target: righteousness*
  > Psa 51:14 Deliver me from bloodguiltiness , O God , O God of my salvation , and my tongue will sing aloud of your righteousness .
- **Psa 71:2** (✓) *target: righteousness*
  > Psa 71:2 In your righteousness deliver me and rescue me; incline your ear to me, and save me !
- **Psa 71:15** (✓) *target: righteous acts*
  > Psa 71:15 My mouth will tell of your righteous acts , of your deeds of salvation all the day , for their number is past my knowledge .
- **Psa 71:16** (✓) *target: righteousness*
  > Psa 71:16 With the mighty deeds of the Lord God I will come ; I will remind them of your righteousness , yours alone .
- **Psa 71:19** (✓) *target: righteousness*
  > Psa 71:19 Your righteousness , O God , reaches the high heavens . You who have done great things , O God , who is like you ?
- **Psa 71:24** (✓) *target: righteous*
  > Psa 71:24 And my tongue will talk of your righteous help all the day long, for they have been put to shame and disappointed who sought to do me hurt .
- **Psa 72:1** (✓) *target: righteousness*
  > Of Solomon . Psa 72:1 Give the king your justice , O God , and your righteousness to the royal son !
- **Psa 88:12** (✓) *target: righteousness*
  > Psa 88:12 Are your wonders known in the darkness , or your righteousness in the land of forgetfulness ?
- **Psa 89:16** (✓) *target: righteousness*
  > Psa 89:16 who exult in your name all the day and in your righteousness are exalted .
- **Psa 98:2** (✓) *target: righteousness*
  > Psa 98:2 The Lord has made known his salvation ; he has revealed his righteousness in the sight of the nations .
- **Psa 103:6** (✓) *target: righteousness*
  > Psa 103:6 The Lord works righteousness and justice for all who are oppressed .
- **Psa 103:17** (✓) *target: righteousness*
  > Psa 103:17 But the steadfast love of the Lord is from everlasting to everlasting on those who fear him, and his righteousness to children’s children ,
- **Psa 111:3** (✓) *target: righteousness*
  > Psa 111:3 Full of splendor and majesty is his work , and his righteousness endures forever .
- **Psa 119:40** (✓) *target: righteousness*
  > Psa 119:40 Behold , I long for your precepts ; in your righteousness give me life !
- **Psa 119:142** (✓) *target: righteousness*
  > Psa 119:142 Your righteousness is righteous forever , and your law is true .
- **Psa 143:1** (✓) *target: righteousness*
  > A Psalm of David . Psa 143:1 Hear my prayer , O Lord ; give ear to my pleas for mercy ! In your faithfulness answer me, in your righteousness !
- **Psa 143:11** (✓) *target: righteousness*
  > Psa 143:11 For your name’s sake , O Lord , preserve my life ! In your righteousness bring my soul out of trouble !
- **Psa 145:7** (✓) *target: righteousness*
  > Psa 145:7 They shall pour forth the fame of your abundant goodness and shall sing aloud of your righteousness .
- **Isa 10:22** (✓) *target: righteousness*
  > Isa 10:22 For though your people Israel be as the sand of the sea , only a remnant of them will return . Destruction is decreed , overflowing with righteousness .
- **Isa 28:17** (✓) *target: righteousness*
  > Isa 28:17 And I will make justice the line , and righteousness the plumb line ; and hail will sweep away the refuge of lies , and waters will overwhelm the shelter .”
- **Isa 45:8** (✓) *target: righteousness*
  > Isa 45:8 “ Shower , O heavens , from above , and let the clouds rain down righteousness ; let the earth open , that salvation and righteousness may bear fruit ; let the earth cause them both to sprout ; I the Lord have created it .
- **Isa 45:23** (✓) *target: righteousness*
  > Isa 45:23 By myself I have sworn ; from my mouth has gone out in righteousness a word that shall not return : ‘ To me every knee shall bow , every tongue shall swear allegiance.’
- **Isa 45:24** (✓) *target: righteousness*
  > Isa 45:24 “ Only in the Lord , it shall be said of me, are righteousness and strength ; to him shall come and be ashamed all who were incensed against him .
- **Isa 46:12** (✓) *target: righteousness*
  > Isa 46:12 “ Listen to me, you stubborn of heart , you who are far from righteousness :
- **Isa 46:13** (✓) *target: righteousness*
  > Isa 46:13 I bring near my righteousness ; it is not far off , and my salvation will not delay ; I will put salvation in Zion , for Israel my glory .”
- **Isa 51:6** (✓) *target: righteousness*
  > Isa 51:6 Lift up your eyes to the heavens , and look at the earth beneath ; for the heavens vanish like smoke , the earth will wear out like a garment , and they who dwell in it will die in like manner ; but my salvation will be forever , and my righteousness will never be dismayed .
- **Isa 51:8** (✓) *target: righteousness*
  > Isa 51:8 For the moth will eat them up like a garment , and the worm will eat them like wool , but my righteousness will be forever , and my salvation to all generations .”
- **Isa 59:9** (✓) *target: righteousness*
  > Isa 59:9 Therefore justice is far from us, and righteousness does not overtake us; we hope for light , and behold , darkness , and for brightness , but we walk in gloom .
- **Isa 59:16** (✓) *target: righteousness*
  > Isa 59:16 He saw that there was no man , and wondered that there was no one to intercede ; then his own arm brought him salvation , and his righteousness upheld him .
- **Isa 59:17** (✓) *target: righteousness*
  > Isa 59:17 He put on righteousness as a breastplate , and a helmet of salvation on his head ; he put on garments of vengeance for clothing , and wrapped himself in zeal as a cloak .
- **Isa 61:11** (✓) *target: righteousness*
  > Isa 61:11 For as the earth brings forth its sprouts , and as a garden causes what is sown in it to sprout up , so the Lord God will cause righteousness and praise to sprout up before all the nations .
- **Isa 63:1** (✓) *target: righteousness*
  > Isa 63:1 Who is this who comes from Edom , in crimsoned garments from Bozrah , he who is splendid in his apparel , marching in the greatness of his strength ? “ It is I , speaking in righteousness , mighty to save .”
- **Jer 9:24** (✓) *target: righteousness*
  > Jer 9:24 but let him who boasts boast in this , that he understands and knows me, that I am the Lord who practices steadfast love , justice , and righteousness in the earth . For in these things I delight , declares the Lord .”
- **Jer 51:10** (✓) *target: vindication*
  > Jer 51:10 The Lord has brought about our vindication ; come , let us declare in Zion the work of the Lord our God .
- **Dan 9:7** (✓) *target: righteousness*
  > Dan 9:7 To you, O Lord , belongs righteousness , but to us open shame , as at this day , to the men of Judah , to the inhabitants of Jerusalem , and to all Israel , those who are near and those who are far away , in all the lands to which you have driven them, because of the treachery that they have committed against you .
- **Joe 2:23** (✓) *target: vindication*
  > Joe 2:23 “Be glad , O children of Zion , and rejoice in the Lord your God , for he has given the early rain for your vindication ; he has poured down for you abundant rain , the early and the latter rain, as before .
- **Mic 6:5** (✓) *target: righteous acts*
  > Mic 6:5 O my people , remember what Balak king of Moab devised , and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal , that you may know the righteous acts of the Lord .”
- **Mic 7:9** (✓) *target: vindication*
  > Mic 7:9 I will bear the indignation of the Lord because I have sinned against him, until he pleads my cause and executes judgment for me. He will bring me out to the light ; I shall look upon his vindication .
- **Mal 4:2** (✓) *target: righteousness*
  > Mal 4:2 But for you who fear my name , the sun of righteousness shall rise with healing in its wings . You shall go out leaping like calves from the stall .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**2 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H6662` | righteous | `not_done` | 184 | 3 | 174 |
| `H6666` | righteousness | `not_done` | 148 | 3 | 148 |

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

### Registry-specific extensions for R077 honesty

_None._ No active non-tiered extensions in `wa_obs_question_catalogue` are sourced from registry 77 (honesty).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-05-02T15:24:44Z`
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

*End of readiness output v3 — wa-077-honesty.*