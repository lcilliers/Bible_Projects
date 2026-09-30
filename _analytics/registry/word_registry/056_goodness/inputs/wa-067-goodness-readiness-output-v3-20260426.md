# wa-067-goodness — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-04-26T18:57:10Z · schema 3.16.1_

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
- M. Readiness verification

---

## A. Registry Overview

- **Registry no:** `67` · **word:** `goodness`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `NULL` (version `-`)
- **cluster_assignment:** `C10`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Moral/Conscience`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 45  (programme-wide aggregate including XREF and historical terms — current OWNER count is 3, XREF 9)
- `phase1_verse_count`: 2216  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 1 unresolved · **Existing session_b_findings:** 1

**Description:**

> Goodness is the quality of being genuinely, structurally beneficial — not just pleasing or approved but actually doing good in the deep sense of the word. The Hebrew and Greek vocabulary runs from the aesthetic (pleasant, beautiful) through the moral (righteous, beneficial) to the relational (kind). God is described as good at the very beginning of creation: what he makes is good because it reflects his character. Human goodness is derivative: a participation in and reflection of the goodness that originates in God.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-04-26T18:57:10Z`
- **Schema version:** `3.16.1`
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
| `H2896A` | tov | pleasant | H | `extracted_thin` | **`vc_completed`** | 2 | 306 | 9/0 | 230/75 | 11 |
| `G0019` | agathōsunē | goodness | G | `extracted` | **`vc_completed`** | 2 | 4 | 1/0 | 4/0 | 1 |
| `G5544` | chrēstotēs | kindness | G | `extracted` | **`vc_completed`** | 2 | 7 | 2/0 | 7/0 | 2 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H2896A` — tov "pleasant"

**Identity:** mti=884 · ti=922 · language=Hebrew · status=`extracted_thin` · md_v=2

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:31): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: adj
1) good, pleasant, agreeable
1a) pleasant, agreeable (to the senses)
1b) pleasant (to the higher nature)
1c) good, excellent (of its kind)
1d) good, rich, valuable in estimation
1e) good, appropriate, becoming
1f) better (comparative)
1g) glad, happy, prosperous (of man's sensuous nature)
1h) good understanding (of man's intellectual nature)
1i) good, kind, benign
1j) good, right (ethical)
Aramaic equivalent: tav (טָב "fine" H2869)

**Root family:**
- `TOV` (Hebrew): pleasant — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (11 total; sample of 11):**
- `H2869` tav "fine"
- `H2895` tov "be pleasing"
- `H2896B` tov "good"
- `H2896C` to.vah "welfare"
- `H2897` tov "Tob"
- `H2898` tuv "goodness"
- `H2899` tov a.do.niy.yah "Tobadonijah"
- `H2900G` to.viy.ya.hu "Tobijah"
- `H2900H` to.viy.ya.hu "Tobiah"
- `H2900I` to.viy.ya.hu "Tobiah"
- `H2900J` to.viy.ya.hu "Tobijah"

### `G0019` — agathōsunē "goodness"

**Identity:** mti=885 · ti=923 · language=Greek · status=`extracted` · md_v=2

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:31): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: goodness, virtue, beneficence, Rom. 15:14; Eph. 5:9; 2Thess. 1:11; generosity, Gal. 5:22*

**Root family:**
- `AGATHŌSUN` (Greek): goodness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (7 total; sample of 7):**
- `G0014` agathoergeō "to do good"
- `G0015` agathopoieō "to do good"
- `G0016` agathopoiia "doing good"
- `G0017` agathopoios "doing good"
- `G0018` agathos "good"
- `G0865` afilagathos "hating good"
- `G5358` filagathos "lover of good"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G5544` — chrēstotēs "kindness"

**Identity:** mti=886 · ti=925 · language=Greek · status=`extracted` · md_v=2

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:31): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: kindness, goodness 
primarily goodness, kindness, gentleness, Rom. 2:4; 11:22(3x); 2Cor. 6:6; Gal. 5:22; Col. 3:12; Tit. 3:4; kindness shown, beneficence, Eph. 2:7; goodness, virtue, Rom. 3:12*

**Root family:**
- `CHRĒSTO` (Greek): kindness — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (3 total; sample of 3):**
- `G5541` chrēsteuomai "be kind"
- `G5542` chrēstologia "smooth talk"
- `G5543` chrēstos "good/kind"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (9)

| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |
|---|---|---|---|---|---|---:|
| `G0014` | agathoergeō | to do good | G | 65 generosity | `extracted_thin` | 2 |
| `G0015` | agathopoieō | to do good | G | 65 generosity | `extracted` | 8 |
| `G0016` | agathopoiia | doing good | G | 65 generosity | `extracted_thin` | 1 |
| `G0017` | agathopoios | doing good | G | 65 generosity | `extracted_thin` | 1 |
| `G0018` | agathos | good | G | 65 generosity | `extracted` | 90 |
| `G0865` | afilagathos | hating good | G | 65 generosity | `extracted_thin` | 1 |
| `G5358` | filagathos | lover of good | G | 103 love | `extracted` | 1 |
| `H2895` | tov | be pleasing | H | 103 love | `extracted` | 20 |
| `H2898` | tuv | goodness | H | 103 love | `extracted` | 0 |

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H2896A` — 9 groups

- **`884-001`** — 22 relevant · 2 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C10`
  - *Term declares God's inner being as good — the foundational doxological assertion that God's character, name, steadfast love, and Spirit are good, and that his goodness governs his relationship to all he has made*
- **`884-002`** — 39 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names human moral character and conduct as good — the inner quality of the person who walks uprightly, acts honestly, and whose character is recognised and assessed as good before God and others*
- **`884-003`** — 36 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names goodness as inner experiential good — what is genuinely good for the human person: proximity to God, worship, waiting, communal harmony, and the reorientation of the inner life toward what truly satisfies*
- **`884-004`** — 42 relevant · 2 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C10`
  - *Term names comparative wisdom good — the better-than sayings of wisdom literature where inner and relational qualities are ranked as the greater good above material wealth, social status, or external abundance*
- **`884-005`** — 17 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names God's good word and promise — the covenantal faithfulness through which God declares, fulfils, and sustains his promised good toward his people*
- **`884-006`** — 22 relevant · 1 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C10`
  - *Term names the moral assessment of conduct, ways, or deeds as not good — the prophetic and wisdom verdict that certain inner orientations and behavioural expressions are contrary to the good God requires*
- **`884-007`** — 7 relevant · 1 anchor verse(s) · dimension: _NULL_ · cluster: _NULL_
  - *Term names God's evaluative pronouncement on his creation — the divine inner-being action of judging-and-declaring-good in Gen 1, where the Creator inspects what he has made and pronounces it good or very good*
- **`884-008`** — 40 relevant · 1 anchor verse(s) · dimension: _NULL_ · cluster: _NULL_
  - *Term names what is good-in-the-eyes-of / pleasing to / preferred-by an actor — the volitional-preference idiom in which the term is the predicate of someone's will or evaluative agreement, naming what they choose, prefer, agree to, or judge fitting*
- **`884-009`** — 5 relevant · 1 anchor verse(s) · dimension: _NULL_ · cluster: _NULL_
  - *Term names a state of inner well-being — the shalom-condition of being-well, prospering, glad-of-heart, or well-disposed — the inner-being state experienced or sought by the human person*

### `G0019` — 1 groups

- **`885-001`** — 4 relevant · 1 anchor verse(s) · dimension: `04 — Volition` · cluster: `C10`
  - *Term names goodness as an inner-being disposition and Spirit-produced fruit — a quality that fills the person and is completed by God, expressed in righteous conduct and resolve*

### `G5544` — 2 groups

- **`886-001`** — 3 relevant · 1 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C10`
  - *Term names kindness as God's inner disposition of generous goodwill toward humanity — the divine attribute that leads to repentance, governs judgment and mercy, and is displayed supremely in Christ*
- **`886-002`** — 4 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C10`
  - *Term names kindness as a Spirit-produced inner quality of the believer — the disposition to act with goodness toward others, listed as fruit of the Spirit and garment of the renewed person*

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

| Other registry | shared OWNER strongs | strongs list |
|---|---:|---|
| 103 love | 2 | `H2896A,G0019` |
| 42 delight | 1 | `H2896A` |
| 65 generosity | 1 | `G0019` |
| 99 kindness | 1 | `G5544` |

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 103 love | 23 |
| 43 desire | 18 |
| 197 authority | 17 |
| 168 uprightness | 13 |
| 183 heart | 13 |
| 97 joy | 12 |
| 182 Soul | 12 |
| 100 knowledge | 11 |
| 187 strength | 11 |
| 77 honesty | 10 |
| 174 wisdom | 10 |
| 23 compassion | 9 |
| 73 guilt | 9 |
| 78 hope | 9 |
| 90 innocence | 8 |
| 32 counsel | 7 |
| 68 grace | 7 |
| 121 praise | 7 |
| 167 unity | 7 |
| 51 distress | 6 |
| 116 patience | 6 |
| 140 seeking | 6 |
| 173 will | 6 |
| 186 gladness | 6 |
| 213 listen | 6 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 1 abomination | Eze 36:31 |
| 4 anger | Pro 16:32 |
| 23 compassion | Mic 6:8 |
| 24 condemnation | Mic 6:8 |
| 49 discernment | Psa 34:8 |
| 58 experience | Gen 1:31 |
| 59 faith | Gal 5:22 |
| 78 hope | Psa 34:8 |
| 80 humility | Mic 6:8 |
| 97 joy | Est 5:9 |
| 97 joy | Gal 5:22 |
| 99 kindness | Mic 6:8 |
| 103 love | Gal 5:22 |
| 103 love | Mic 6:8 |
| 116 patience | Gal 5:22 |
| 116 patience | Pro 16:32 |
| 117 peace | Gal 5:22 |
| 173 will | Mic 6:8 |
| 199 dominion | Pro 16:32 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (1)

#### `DIM-67-001` — `DIMENSION_REVIEW`

- **status:** `pending` · **thin_evidence:** 0 · **raised:** 2026-04-07 · **term_id:** -

> The tov word family spans Theological/Divine-Human (divine goodness), Moral/Conscience (human moral character), Spiritual/God-ward (experiential good), and Character/Disposition (Spirit-fruit) — a very wide dimensional range for one term. Session B should analyse whether these are genuinely distinct inner-being phenomena or expressions of a unified category of 'goodness' that the English vocabulary separates but Hebrew integrates.

### H.2 Open SD pointers + research flags (1)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `SB_FINDING` | SBF-VCB013-001 chrēstotēs tripartite engagement | normal | Session B | 2026-04-25T16:30:00Z |

#### SBF-VCB013-001 chrēstotēs tripartite engagement

> G5544 chrēstotēs (kindness) shows a tripartite inner-being engagement pattern across its 7-verse active NT corpus: (1) presence — kindness as Spirit-produced quality of the renewed person (Gal 5:22, Col 3:12, 2 Cor 6:6) and as God's relational disposition toward humanity (Rom 2:4, Rom 11:22, Eph 2:7); (2) absence — Rom 3:12 'no one does kindness, not even one' (universal-depravity quotation from Ps 14:3 LXX), where the term names the moral-spiritual quality whose absence characterises fallen humanity; (3) distortion — not strongly attested in this term but cf. parallel pattern on G2168. Worth examining in Session B whether this presence/absence pole is a structural feature of moral-quality vocabulary in registry 067 (goodness) more broadly. Verse Context retained Rom 3:12 in 886-002 with notes annotation per DF-001 Option C; group description was not amended.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

### `H2896A` (1 flag(s))

- **`6`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G0019` (1 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

### `G5544` (1 flag(s))

- **`16`** — None
  - source: bulk_patch · raised: 2026-03-19T18:18:06Z

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H2896A` — 306/306 classified · 11 anchor verse(s)

**Group `884-001`** (22 verses — anchors: Psa 34:8, Psa 119:68)

- **Psa 34:8** 🔵 (✓) *target: good*
  > Psa 34:8 Oh, taste and see that the Lord is good ! Blessed is the man who takes refuge in him !
- **Psa 119:68** 🔵 (✓) *target: good*
  > Psa 119:68 You are good and do good ; teach me your statutes .
- **Ezr 3:11** (✓) *target: good*
  > Ezr 3:11 And they sang responsively , praising and giving thanks to the Lord , “ For he is good , for his steadfast love endures forever toward Israel .” And all the people shouted with a great shout when they praised the Lord , because the foundation of the house of the Lord was laid.
- **Neh 9:20** (✓) *target: good*
  > Neh 9:20 You gave your good Spirit to instruct them and did not withhold your manna from their mouth and gave them water for their thirst .
- **Psa 25:8** (✓) *target: Good*
  > Psa 25:8 Good and upright is the Lord ; therefore he instructs sinners in the way .
- **Psa 52:9** (✓) *target: good*
  > Psa 52:9 I will thank you forever , because you have done it. I will wait for your name , for it is good , in the presence of the godly .
- **Psa 54:6** (✓) *target: good*
  > Psa 54:6 With a freewill offering I will sacrifice to you; I will give thanks to your name , O Lord , for it is good .
- **Psa 69:16** (✓) *target: good*
  > Psa 69:16 Answer me, O Lord , for your steadfast love is good ; according to your abundant mercy , turn to me .
- **Psa 86:5** (✓) *target: good*
  > Psa 86:5 For you , O Lord , are good and forgiving , abounding in steadfast love to all who call upon you .
- **Psa 100:5** (✓) *target: good*
  > Psa 100:5 For the Lord is good ; his steadfast love endures forever , and his faithfulness to all generations .
- **Psa 106:1** (✓) *target: good*
  > Psa 106:1 Praise the Lord ! Oh give thanks to the Lord , for he is good , for his steadfast love endures forever !
- **Psa 107:1** (✓) *target: good*
  > Psa 107:1 Oh give thanks to the Lord , for he is good , for his steadfast love endures forever !
- **Psa 109:21** (✓) *target: good*
  > Psa 109:21 But you , O God my Lord , deal on my behalf for your name’s sake ; because your steadfast love is good , deliver me !
- **Psa 118:1** (✓) *target: good*
  > Psa 118:1 Oh give thanks to the Lord , for he is good ; for his steadfast love endures forever !
- **Psa 118:29** (✓) *target: good*
  > Psa 118:29 Oh give thanks to the Lord , for he is good ; for his steadfast love endures forever !
- **Psa 135:3** (✓) *target: good*
  > Psa 135:3 Praise the Lord , for the Lord is good ; sing to his name , for it is pleasant !
- **Psa 136:1** (✓) *target: good*
  > Psa 136:1 Give thanks to the Lord , for he is good , for his steadfast love endures forever .
- **Psa 143:10** (✓) *target: good*
  > Psa 143:10 Teach me to do your will , for you are my God ! Let your good Spirit lead me on level ground !
- **Psa 145:9** (✓) *target: good*
  > Psa 145:9 The Lord is good to all , and his mercy is over all that he has made .
- **Jer 33:11** (✓) *target: good*
  > Jer 33:11 the voice of mirth and the voice of gladness , the voice of the bridegroom and the voice of the bride , the voices of those who sing , as they bring thank offerings to the house of the Lord : “‘Give thanks to the Lord of hosts , for the Lord is good , for his steadfast love endures forever !’ For I will restore the fortunes of the land as at first , says the Lord .
- **Nah 1:7** (✓) *target: good*
  > Nah 1:7 The Lord is good , a stronghold in the day of trouble ; he knows those who take refuge in him .
- **Zec 1:13** (✓) *target: gracious*
  > Zec 1:13 And the Lord answered gracious and comforting words to the angel who talked with me.

**Group `884-002`** (39 verses — anchors: Mic 6:8)

- **Mic 6:8** 🔵 (✓) *target: good*
  > Mic 6:8 He has told you , O man , what is good ; and what does the Lord require of you but to do justice , and to love kindness , and to walk humbly with your God ?
- **Gen 2:18** (✓) *target: good*
  > Gen 2:18 Then the Lord God said , “It is not good that the man should be alone ; I will make him a helper fit for him .”
- **Gen 3:5** (✓) *target: good*
  > Gen 3:5 For God knows that when you eat of it your eyes will be opened , and you will be like God , knowing good and evil .”
- **Deu 6:18** (✓) *target: good*
  > Deu 6:18 And you shall do what is right and good in the sight of the Lord , that it may go well with you, and that you may go in and take possession of the good land that the Lord swore to give to your fathers
- **Deu 9:6** (✓) *target: good*
  > Deu 9:6 “ Know , therefore, that the Lord your God is not giving you this good land to possess because of your righteousness , for you are a stubborn people .
- **Deu 12:28** (✓) *target: good*
  > Deu 12:28 Be careful to obey all these words that I command you, that it may go well with you and with your children after you forever , when you do what is good and right in the sight of the Lord your God .
- **1Sa 12:23** (✓) *target: good*
  > 1Sa 12:23 Moreover , as for me , far be it from me that I should sin against the Lord by ceasing to pray for you, and I will instruct you in the good and the right way .
- **1Sa 15:22** (✓) *target: better*
  > 1Sa 15:22 And Samuel said , “Has the Lord as great delight in burnt offerings and sacrifices , as in obeying the voice of the Lord ? Behold , to obey is better than sacrifice , and to listen than the fat of rams .
- **1Sa 15:28** (✓) *target: better*
  > 1Sa 15:28 And Samuel said to him, “The Lord has torn the kingdom of Israel from you this day and has given it to a neighbor of yours, who is better than you .
- **1Sa 19:4** (✓) *target: well*
  > 1Sa 19:4 And Jonathan spoke well of David to Saul his father and said to him, “Let not the king sin against his servant David , because he has not sinned against you, and because his deeds have brought good to you .
- **1Sa 24:19** (✓) *target: safe*
  > 1Sa 24:19 For if a man finds his enemy , will he let him go away safe ? So may the Lord reward you with good for what you have done to me this day .
- **1Sa 25:3** (✓) *target: discerning*
  > 1Sa 25:3 Now the name of the man was Nabal , and the name of his wife Abigail . The woman was discerning and beautiful , but the man was harsh and badly behaved ; he was a Calebite .
- **1Sa 25:15** (✓) *target: good*
  > 1Sa 25:15 Yet the men were very good to us, and we suffered no harm, and we did not miss anything when we were in the fields , as long as we went with them.
- **1Sa 29:6** (✓) *target: right*
  > 1Sa 29:6 Then Achish called David and said to him, “As the Lord lives , you have been honest , and to me it seems right that you should march out and in with me in the campaign . For I have found nothing wrong in you from the day of your coming to me to this day . Nevertheless, the lords do not approve of you .
- **1Sa 29:9** (✓) *target: blameless*
  > 1Sa 29:9 And Achish answered David and said , “I know that you are as blameless in my sight as an angel of God . Nevertheless , the commanders of the Philistines have said , ‘He shall not go up with us to the battle .’
- **2Sa 18:27** (✓) *target: good*
  > 2Sa 18:27 The watchman said , “ I think the running of the first is like the running of Ahimaaz the son of Zadok .” And the king said , “ He is a good man and comes with good news .”
- **Psa 36:4** (✓) *target: good*
  > Psa 36:4 He plots trouble while on his bed ; he sets himself in a way that is not good ; he does not reject evil .
- **Psa 38:20** (✓) *target: good*
  > Psa 38:20 Those who render me evil for good accuse me because I follow after good .
- **Psa 73:1** (✓) *target: good*
  > A Psalm of Asaph . Psa 73:1 Truly God is good to Israel , to those who are pure in heart .
- **Psa 125:4** (✓) *target: good*
  > Psa 125:4 Do good , O Lord , to those who are good , and to those who are upright in their hearts !
- **Pro 2:20** (✓) *target: good*
  > Pro 2:20 So you will walk in the way of the good and keep to the paths of the righteous .
- **Pro 3:4** (✓) *target: good*
  > Pro 3:4 So you will find favor and good success in the sight of God and man .
  - notes: "Good success in sight of God and man" — names the inner-being-relational state of the upright; fits 884-002 (human moral character). Wisdom literature.
- **Pro 12:2** (✓) *target: good*
  > Pro 12:2 A good man obtains favor from the Lord , but a man of evil devices he condemns .
- **Pro 13:15** (✓) *target: Good*
  > Pro 13:15 Good sense wins favor , but the way of the treacherous is their ruin .
- **Pro 13:22** (✓) *target: good*
  > Pro 13:22 A good man leaves an inheritance to his children’s children , but the sinner’s wealth is laid up for the righteous .
- **Pro 14:14** (✓) *target: good*
  > Pro 14:14 The backslider in heart will be filled with the fruit of his ways , and a good man will be filled with the fruit of his ways.
- **Pro 14:19** (✓) *target: good*
  > Pro 14:19 The evil bow down before the good , the wicked at the gates of the righteous .
- **Pro 15:3** (✓) *target: good*
  > Pro 15:3 The eyes of the Lord are in every place , keeping watch on the evil and the good .
- **Pro 22:1** (✓) *target: better*
  > Pro 22:1 A good name is to be chosen rather than great riches , and favor is better than silver or gold .
- **Pro 22:9** (✓) *target: bountiful*
  > Pro 22:9 Whoever has a bountiful eye will be blessed , for he shares his bread with the poor .
- **Pro 27:10** (✓) *target: Better*
  > Pro 27:10 Do not forsake your friend and your father’s friend , and do not go to your brother’s house in the day of your calamity . Better is a neighbor who is near than a brother who is far away .
- **Pro 31:18** (✓) *target: profitable*
  > Pro 31:18 She perceives that her merchandise is profitable . Her lamp does not go out at night .
  - notes: "Her merchandise is profitable (good)" — Pro 31 woman's wisdom-in-action; inner-being-engaged through her industriousness
- **Isa 38:3** (✓) *target: good*
  > Isa 38:3 and said , “ Please , O Lord , remember how I have walked before you in faithfulness and with a whole heart , and have done what is good in your sight .” And Hezekiah wept bitterly .
- **Isa 65:2** (✓) *target: good*
  > Isa 65:2 I spread out my hands all the day to a rebellious people , who walk in a way that is not good , following their own devices ;
- **Jer 6:16** (✓) *target: good*
  > Jer 6:16 Thus says the Lord : “ Stand by the roads , and look , and ask for the ancient paths , where the good way is ; and walk in it, and find rest for your souls . But they said , ‘We will not walk in it.’
- **Jer 22:15** (✓) *target: well*
  > Jer 22:15 Do you think you are a king because you compete in cedar ? Did not your father eat and drink and do justice and righteousness ? Then it was well with him .
- **Jer 22:16** (✓) *target: well*
  > Jer 22:16 He judged the cause of the poor and needy ; then it was well . Is not this to know me? declares the Lord .
- **Dan 1:4** (✓) *target: good*
  > Dan 1:4 youths without blemish , of good appearance and skillful in all wisdom , endowed with knowledge , understanding learning , and competent to stand in the king’s palace , and to teach them the literature and language of the Chaldeans .
- **Mal 2:17** (✓) *target: good*
  > Mal 2:17 You have wearied the Lord with your words . But you say , “How have we wearied him?” By saying , “ Everyone who does evil is good in the sight of the Lord , and he delights in them.” Or by asking, “Where is the God of justice ?”

**Group `884-003`** (36 verses — anchors: Psa 73:28)

- **Psa 73:28** 🔵 (✓) *target: good*
  > Psa 73:28 But for me it is good to be near God ; I have made the Lord God my refuge , that I may tell of all your works .
- **Num 10:29** (✓) *target: good*
  > Num 10:29 And Moses said to Hobab the son of Reuel the Midianite , Moses ’ father-in-law , “We are setting out for the place of which the Lord said , ‘I will give it to you.’ Come with us, and we will do good to you, for the Lord has promised good to Israel .”
- **Deu 8:10** (✓) *target: good*
  > Deu 8:10 And you shall eat and be full , and you shall bless the Lord your God for the good land he has given you .
- **Rut 4:15** (✓) *target: more*
  > Rut 4:15 He shall be to you a restorer of life and a nourisher of your old age , for your daughter-in-law who loves you, who is more to you than seven sons , has given birth to him.”
- **1Sa 1:8** (✓) *target: more*
  > 1Sa 1:8 And Elkanah , her husband , said to her, “ Hannah , why do you weep ? And why do you not eat ? And why is your heart sad ? Am I not more to you than ten sons ?”
- **1Sa 16:23** (✓) *target: well*
  > 1Sa 16:23 And whenever the harmful spirit from God was upon Saul , David took the lyre and played it with his hand . So Saul was refreshed and was well , and the harmful spirit departed from him.
- **2Sa 10:12** (✓) *target: seems good*
  > 2Sa 10:12 Be of good courage , and let us be courageous for our people , and for the cities of our God , and may the Lord do what seems good to him .”
- **Job 34:4** (✓) *target: good*
  > Job 34:4 Let us choose what is right ; let us know among ourselves what is good .
- **Psa 45:1** (✓) *target: pleasing*
  > To the choirmaster : according to Lilies . A Maskil of the Sons of Korah ; a love song . Psa 45:1 My heart overflows with a pleasing theme ; I address my verses to the king ; my tongue is like the pen of a ready scribe .
- **Psa 84:10** (✓) *target: better*
  > Psa 84:10 For a day in your courts is better than a thousand elsewhere. I would rather be a doorkeeper in the house of my God than dwell in the tents of wickedness .
- **Psa 92:1** (✓) *target: good*
  > A Psalm . A Song for the Sabbath . Psa 92:1 It is good to give thanks to the Lord , to sing praises to your name , O Most High ;
- **Psa 111:10** (✓) *target: good*
  > Psa 111:10 The fear of the Lord is the beginning of wisdom ; all those who practice it have a good understanding . His praise endures forever !
- **Psa 112:5** (✓) *target: well*
  > Psa 112:5 It is well with the man who deals generously and lends ; who conducts his affairs with justice .
- **Psa 128:2** (✓) *target: well*
  > Psa 128:2 You shall eat the fruit of the labor of your hands ; you shall be blessed , and it shall be well with you .
- **Psa 133:1** (✓) *target: good*
  > A Song of Ascents . Of David . Psa 133:1 Behold, how good and pleasant it is when brothers dwell in unity !
- **Psa 147:1** (✓) *target: good*
  > Psa 147:1 Praise the Lord ! For it is good to sing praises to our God ; for it is pleasant , and a song of praise is fitting .
- **Pro 12:25** (✓) *target: good*
  > Pro 12:25 Anxiety in a man’s heart weighs him down , but a good word makes him glad .
- **Pro 15:15** (✓) *target: cheerful*
  > Pro 15:15 All the days of the afflicted are evil , but the cheerful of heart has a continual feast .
- **Pro 25:25** (✓) *target: good*
  > Pro 25:25 Like cold water to a thirsty soul , so is good news from a far country .
- **Ecc 2:3** (✓) *target: good*
  > Ecc 2:3 I searched with my heart how to cheer my body with wine —my heart still guiding me with wisdom —and how to lay hold on folly , till I might see what was good for the children of man to do under heaven during the few days of their life .
  - notes: "What was good for the children of man to do" — Qoheleth's search; experiential-good for human persons; fits 884-003
- **Ecc 2:24** (✓) *target: better*
  > Ecc 2:24 There is nothing better for a person than that he should eat and drink and find enjoyment in his toil . This also , I saw , is from the hand of God ,
- **Ecc 2:26** (✓) *target: pleases*
  > Ecc 2:26 For to the one who pleases him God has given wisdom and knowledge and joy , but to the sinner he has given the business of gathering and collecting , only to give to one who pleases God . This also is vanity and a striving after wind .
- **Ecc 3:12** (✓) *target: better*
  > Ecc 3:12 I perceived that there is nothing better for them than to be joyful and to do good as long as they live ;
- **Ecc 3:22** (✓) *target: better*
  > Ecc 3:22 So I saw that there is nothing better than that a man should rejoice in his work , for that is his lot . Who can bring him to see what will be after him ?
- **Ecc 4:9** (✓) *target: better*
  > Ecc 4:9 Two are better than one , because they have a good reward for their toil .
- **Ecc 5:18** (✓) *target: good*
  > Ecc 5:18 Behold , what I have seen to be good and fitting is to eat and drink and find enjoyment in all the toil with which one toils under the sun the few days of his life that God has given him, for this is his lot .
- **Ecc 6:12** (✓) *target: good*
  > Ecc 6:12 For who knows what is good for man while he lives the few days of his vain life , which he passes like a shadow ? For who can tell man what will be after him under the sun ?
- **Isa 52:7** (✓) *target: happiness*
  > Isa 52:7 How beautiful upon the mountains are the feet of him who brings good news , who publishes peace , who brings good news of happiness , who publishes salvation , who says to Zion , “ Your God reigns .”
- **Lam 3:25** (✓) *target: good*
  > Lam 3:25 The Lord is good to those who wait for him, to the soul who seeks him .
- **Lam 3:26** (✓) *target: good*
  > Lam 3:26 It is good that one should wait quietly for the salvation of the Lord .
- **Lam 3:27** (✓) *target: good*
  > Lam 3:27 It is good for a man that he bear the yoke in his youth .
- **Lam 3:38** (✓) *target: good*
  > Lam 3:38 Is it not from the mouth of the Most High that good and bad come ?
- **Eze 34:18** (✓) *target: good*
  > Eze 34:18 Is it not enough for you to feed on the good pasture , that you must tread down with your feet the rest of your pasture ; and to drink of clear water , that you must muddy the rest of the water with your feet ?
- **Jon 4:3** (✓) *target: better*
  > Jon 4:3 Therefore now , O Lord , please take my life from me, for it is better for me to die than to live .”
- **Jon 4:8** (✓) *target: better*
  > Jon 4:8 When the sun rose , God appointed a scorching east wind , and the sun beat down on the head of Jonah so that he was faint . And he asked that he might die and said , “It is better for me to die than to live .”
- **Zec 8:19** (✓) *target: cheerful*
  > Zec 8:19 “ Thus says the Lord of hosts : The fast of the fourth month and the fast of the fifth and the fast of the seventh and the fast of the tenth shall be to the house of Judah seasons of joy and gladness and cheerful feasts . Therefore love truth and peace .

**Group `884-004`** (42 verses — anchors: Pro 15:16, Pro 16:32)

- **Pro 15:16** 🔵 (✓) *target: Better*
  > Pro 15:16 Better is a little with the fear of the Lord than great treasure and trouble with it .
- **Pro 16:32** 🔵 (✓) *target: better*
  > Pro 16:32 Whoever is slow to anger is better than the mighty , and he who rules his spirit than he who takes a city .
- **Judg 8:2** (✓) *target: better*
  > Judg 8:2 And he said to them, “ What have I done now in comparison with you? Is not the gleaning of the grapes of Ephraim better than the grape harvest of Abiezer ?
  - notes: "Better the gleaning of Ephraim than the harvest of Abiezer" — Gideon's rhetorical comparative wisdom; fits 884-004 comparative-wisdom-good
- **Judg 9:2** (✓) *target: better*
  > Judg 9:2 “ Say in the ears of all the leaders of Shechem , ‘Which is better for you, that all seventy of the sons of Jerubbaal rule over you, or that one rule over you?’ Remember also that I am your bone and your flesh .”
  - notes: "Better seventy or one rule" — Abimelech's rhetorical comparative for political choice; volitional-evaluative
- **Judg 18:19** (✓) *target: better*
  > Judg 18:19 And they said to him, “Keep quiet ; put your hand on your mouth and come with us and be to us a father and a priest . Is it better for you to be priest to the house of one man , or to be priest to a tribe and clan in Israel ?”
  - notes: "Better priest to one man or to a tribe" — Danites' rhetorical preference; comparative
- **1Sa 27:1** (✓) *target: better*
  > 1Sa 27:1 Then David said in his heart , “ Now I shall perish one day by the hand of Saul . There is nothing better for me than that I should escape to the land of the Philistines . Then Saul will despair of seeking me any longer within the borders of Israel , and I shall escape out of his hand .”
  - notes: "Nothing better than escape" — David's inward judgement spoken in his heart; comparative-wisdom
- **2Sa 14:32** (✓) *target: better*
  > 2Sa 14:32 Absalom answered Joab , “ Behold , I sent word to you, ‘ Come here , that I may send you to the king , to ask , “ Why have I come from Geshur ? It would be better for me to be there still .” Now therefore let me go into the presence of the king , and if there is guilt in me, let him put me to death .’”
  - notes: "Better for me to be there still" — Absalom's preference; comparative
- **2Sa 17:7** (✓) *target: good*
  > 2Sa 17:7 Then Hushai said to Absalom , “ This time the counsel that Ahithophel has given is not good .”
  - notes: "Counsel of Ahithophel is not good" — Hushai's evaluative judgement on counsel
- **2Sa 17:14** (✓) *target: better*
  > 2Sa 17:14 And Absalom and all the men of Israel said , “The counsel of Hushai the Archite is better than the counsel of Ahithophel .” For the Lord had ordained to defeat the good counsel of Ahithophel , so that the Lord might bring harm upon Absalom .
  - notes: "Good counsel of Ahithophel" — narrator's evaluation; same engagement
- **2Sa 18:3** (✓) *target: better*
  > 2Sa 18:3 But the men said , “You shall not go out . For if we flee , they will not care about us. If half of us die , they will not care about us. But you are worth ten thousand of us. Therefore it is better that you send us help from the city .”
  - notes: "Better that you send help from city" — Joab's men advising; preferential
- **Psa 37:16** (✓) *target: Better*
  > Psa 37:16 Better is the little that the righteous has than the abundance of many wicked .
- **Psa 63:3** (✓) *target: better*
  > Psa 63:3 Because your steadfast love is better than life , my lips will praise you .
- **Psa 118:8** (✓) *target: better*
  > Psa 118:8 It is better to take refuge in the Lord than to trust in man .
- **Psa 118:9** (✓) *target: better*
  > Psa 118:9 It is better to take refuge in the Lord than to trust in princes .
- **Psa 119:72** (✓) *target: better*
  > Psa 119:72 The law of your mouth is better to me than thousands of gold and silver pieces.
- **Pro 3:14** (✓) *target: better*
  > Pro 3:14 for the gain from her is better than gain from silver and her profit better than gold .
- **Pro 8:11** (✓) *target: better*
  > Pro 8:11 for wisdom is better than jewels , and all that you may desire cannot compare with her .
- **Pro 8:19** (✓) *target: better*
  > Pro 8:19 My fruit is better than gold , even fine gold , and my yield than choice silver .
- **Pro 12:9** (✓) *target: Better*
  > Pro 12:9 Better to be lowly and have a servant than to play the great man and lack bread .
- **Pro 15:17** (✓) *target: Better*
  > Pro 15:17 Better is a dinner of herbs where love is than a fattened ox and hatred with it .
- **Pro 15:23** (✓) *target: good*
  > Pro 15:23 To make an apt answer is a joy to a man , and a word in season , how good it is!
- **Pro 15:30** (✓) *target: good*
  > Pro 15:30 The light of the eyes rejoices the heart , and good news refreshes the bones .
- **Pro 16:8** (✓) *target: Better*
  > Pro 16:8 Better is a little with righteousness than great revenues with injustice .
- **Pro 16:16** (✓) *target: better*
  > Pro 16:16 How much better to get wisdom than gold ! To get understanding is to be chosen rather than silver .
- **Pro 16:19** (✓) *target: better*
  > Pro 16:19 It is better to be of a lowly spirit with the poor than to divide the spoil with the proud .
- **Pro 17:1** (✓) *target: Better*
  > Pro 17:1 Better is a dry morsel with quiet than a house full of feasting with strife .
- **Pro 19:1** (✓) *target: Better*
  > Pro 19:1 Better is a poor person who walks in his integrity than one who is crooked in speech and is a fool .
- **Pro 19:22** (✓) *target: better*
  > Pro 19:22 What is desired in a man is steadfast love , and a poor man is better than a liar .
- **Pro 21:9** (✓) *target: better*
  > Pro 21:9 It is better to live in a corner of the housetop than in a house shared with a quarrelsome wife .
- **Pro 21:19** (✓) *target: better*
  > Pro 21:19 It is better to live in a desert land than with a quarrelsome and fretful woman .
- **Pro 25:7** (✓) *target: better*
  > Pro 25:7 for it is better to be told , “Come up here ,” than to be put lower in the presence of a noble . What your eyes have seen
- **Pro 25:24** (✓) *target: better*
  > Pro 25:24 It is better to live in a corner of the housetop than in a house shared with a quarrelsome wife .
- **Pro 27:5** (✓) *target: Better*
  > Pro 27:5 Better is open rebuke than hidden love .
- **Pro 28:6** (✓) *target: Better*
  > Pro 28:6 Better is a poor man who walks in his integrity than a rich man who is crooked in his ways .
- **Ecc 4:3** (✓) *target: better*
  > Ecc 4:3 But better than both is he who has not yet been and has not seen the evil deeds that are done under the sun .
- **Ecc 4:6** (✓) *target: Better*
  > Ecc 4:6 Better is a handful of quietness than two hands full of toil and a striving after wind .
- **Ecc 4:13** (✓) *target: Better*
  > Ecc 4:13 Better was a poor and wise youth than an old and foolish king who no longer knew how to take advice .
- **Ecc 5:5** (✓) *target: better*
  > Ecc 5:5 It is better that you should not vow than that you should vow and not pay .
- **Ecc 6:3** (✓) *target: good things*
  > Ecc 6:3 If a man fathers a hundred children and lives many years , so that the days of his years are many , but his soul is not satisfied with life’s good things , and he also has no burial , I say that a stillborn child is better off than he.
- **Ecc 6:9** (✓) *target: Better*
  > Ecc 6:9 Better is the sight of the eyes than the wandering of the appetite : this also is vanity and a striving after wind .
- **Lam 4:9** (✓) *target: Happier*
  > Lam 4:9 Happier were the victims of the sword than the victims of hunger , who wasted away , pierced by lack of the fruits of the field .
- **Amo 6:2** (✓) *target: better*
  > Amo 6:2 Pass over to Calneh , and see , and from there go to Hamath the great ; then go down to Gath of the Philistines . Are you better than these kingdoms ? Or is their territory greater than your territory ,
  - notes: "Are you better than these kingdoms?" — Amos' rhetorical comparative; warning to Israel; fits 884-004 (comparative wisdom good as judgement-frame)

**Group `884-005`** (17 verses — anchors: Jos 23:14)

- **Jos 23:14** 🔵 (✓) *target: good*
  > Jos 23:14 “And now I am about to go the way of all the earth , and you know in your hearts and souls , all of you, that not one word has failed of all the good things that the Lord your God promised concerning you. All have come to pass for you; not one of them has failed .
- **Num 14:3** (✓) *target: better*
  > Num 14:3 Why is the Lord bringing us into this land , to fall by the sword ? Our wives and our little ones will become a prey . Would it not be better for us to go back to Egypt ?”
- **Jos 21:45** (✓) *target: good*
  > Jos 21:45 Not one word of all the good promises that the Lord had made to the house of Israel had failed ; all came to pass .
- **Jos 23:15** (✓) *target: good*
  > Jos 23:15 But just as all the good things that the Lord your God promised concerning you have been fulfilled for you, so the Lord will bring upon you all the evil things , until he has destroyed you from off this good land that the Lord your God has given you,
- **Jos 23:16** (✓) *target: good*
  > Jos 23:16 if you transgress the covenant of the Lord your God , which he commanded you, and go and serve other gods and bow down to them. Then the anger of the Lord will be kindled against you, and you shall perish quickly from off the good land that he has given to you .”
- **Ezr 7:9** (✓) *target: good*
  > Ezr 7:9 For on the first day of the first month he began to go up from Babylonia , and on the first day of the fifth month he came to Jerusalem , for the good hand of his God was on him .
- **Ezr 8:18** (✓) *target: good*
  > Ezr 8:18 And by the good hand of our God on us, they brought us a man of discretion , of the sons of Mahli the son of Levi , son of Israel , namely Sherebiah with his sons and kinsmen , 18 ;
- **Neh 2:8** (✓) *target: good*
  > Neh 2:8 and a letter to Asaph , the keeper of the king’s forest , that he may give me timber to make beams for the gates of the fortress of the temple , and for the wall of the city , and for the house that I shall occupy .” And the king granted me what I asked, for the good hand of my God was upon me .
  - notes: "Good hand of my God was upon me" — Nehemiah's recognition of God's favorable providential action; covenantal-relational. Fits 884-005 (God's good word/promise/faithfulness)
- **Neh 2:18** (✓) *target: good*
  > Neh 2:18 And I told them of the hand of my God that had been upon me for good , and also of the words that the king had spoken to me. And they said , “Let us rise up and build .” So they strengthened their hands for the good work.
- **Neh 9:13** (✓) *target: good*
  > Neh 9:13 You came down on Mount Sinai and spoke with them from heaven and gave them right rules and true laws , good statutes and commandments ,
- **Psa 119:39** (✓) *target: good*
  > Psa 119:39 Turn away the reproach that I dread , for your rules are good .
- **Pro 4:2** (✓) *target: good*
  > Pro 4:2 for I give you good precepts ; do not forsake my teaching .
- **Isa 3:10** (✓) *target: well*
  > Isa 3:10 Tell the righteous that it shall be well with them, for they shall eat the fruit of their deeds .
- **Isa 39:8** (✓) *target: good*
  > Isa 39:8 Then Hezekiah said to Isaiah , “The word of the Lord that you have spoken is good .” For he thought , “There will be peace and security in my days .”
- **Isa 56:5** (✓) *target: better*
  > Isa 56:5 I will give in my house and within my walls a monument and a name better than sons and daughters ; I will give them an everlasting name that shall not be cut off .
- **Jer 29:10** (✓) *target: promise*
  > Jer 29:10 “ For thus says the Lord : When seventy years are completed for Babylon , I will visit you, and I will fulfill to you my promise and bring you back to this place .
- **Jer 33:14** (✓) *target: promise*
  > Jer 33:14 “ Behold , the days are coming , declares the Lord , when I will fulfill the promise I made to the house of Israel and the house of Judah .

**Group `884-006`** (22 verses — anchors: Eze 36:31)

- **Eze 36:31** 🔵 (✓) *target: good*
  > Eze 36:31 Then you will remember your evil ways , and your deeds that were not good , and you will loathe yourselves for your iniquities and your abominations .
- **Exo 14:12** (✓) *target: better*
  > Exo 14:12 Is not this what we said to you in Egypt : ‘Leave us alone that we may serve the Egyptians ’? For it would have been better for us to serve the Egyptians than to die in the wilderness .”
- **Exo 18:17** (✓) *target: good*
  > Exo 18:17 Moses ’ father-in-law said to him, “ What you are doing is not good .
- **1Sa 2:24** (✓) *target: good*
  > 1Sa 2:24 No , my sons ; it is no good report that I hear the people of the Lord spreading abroad .
- **1Sa 26:16** (✓) *target: good*
  > 1Sa 26:16 This thing that you have done is not good . As the Lord lives , you deserve to die , because you have not kept watch over your lord , the Lord’s anointed . And now see where the king’s spear is and the jar of water that was at his head .”
- **2Sa 13:22** (✓) *target: good*
  > 2Sa 13:22 But Absalom spoke to Amnon neither good nor bad , for Absalom hated Amnon , because he had violated his sister Tamar .
- **Neh 5:9** (✓) *target: good*
  > Neh 5:9 So I said , “The thing that you are doing is not good . Ought you not to walk in the fear of our God to prevent the taunts of the nations our enemies ?
- **Job 10:3** (✓) *target: good*
  > Job 10:3 Does it seem good to you to oppress , to despise the work of your hands and favor the designs of the wicked ?
- **Job 13:9** (✓) *target: searches*
  > Job 13:9 Will it be well with you when he searches you out ? Or can you deceive him , as one deceives a man ?
- **Pro 16:29** (✓) *target: good*
  > Pro 16:29 A man of violence entices his neighbor and leads him in a way that is not good .
- **Pro 17:26** (✓) *target: good*
  > Pro 17:26 To impose a fine on a righteous man is not good , nor to strike the noble for their uprightness .
- **Pro 18:5** (✓) *target: good*
  > Pro 18:5 It is not good to be partial to the wicked or to deprive the righteous of justice .
- **Pro 19:2** (✓) *target: good*
  > Pro 19:2 Desire without knowledge is not good , and whoever makes haste with his feet misses his way .
- **Pro 20:23** (✓) *target: good*
  > Pro 20:23 Unequal weights are an abomination to the Lord , and false scales are not good .
- **Pro 24:23** (✓) *target: good*
  > Pro 24:23 These also are sayings of the wise . Partiality in judging is not good .
- **Pro 25:27** (✓) *target: good*
  > Pro 25:27 It is not good to eat much honey , nor is it glorious to seek one’s own glory .
- **Pro 28:21** (✓) *target: good*
  > Pro 28:21 To show partiality is not good , but for a piece of bread a man will do wrong .
- **Jer 44:17** (✓) *target: prospered*
  > Jer 44:17 But we will do everything that we have vowed , make offerings to the queen of heaven and pour out drink offerings to her, as we did , both we and our fathers , our kings and our officials , in the cities of Judah and in the streets of Jerusalem . For then we had plenty of food , and prospered , and saw no disaster .
  - notes: "We had plenty of food and prospered" — Jeremiah's opponents recalling their false prosperity in idolatry; fits 884-006 (prophetic verdict on conduct as not-good — here ironic, the people's self-justification is itself the prophetic indictment) — borderline; could also be 884-NEW-WB. Lean: 884-006 since this is reported speech in a prophetic indictment context.
- **Eze 18:18** (✓) *target: good*
  > Eze 18:18 As for his father , because he practiced extortion , robbed his brother , and did what is not good among his people , behold , he shall die for his iniquity .
- **Eze 20:25** (✓) *target: good*
  > Eze 20:25 Moreover , I gave them statutes that were not good and rules by which they could not have life ,
- **Hos 2:7** (✓) *target: better*
  > Hos 2:7 She shall pursue her lovers but not overtake them, and she shall seek them but shall not find them. Then she shall say , ‘I will go and return to my first husband , for it was better for me then than now .’
- **Mic 7:4** (✓) *target: best*
  > Mic 7:4 The best of them is like a brier , the most upright of them a thorn hedge . The day of your watchmen , of your punishment , has come ; now their confusion is at hand.

**Group `884-007`** (7 verses — anchors: Gen 1:31)

- **Gen 1:31** 🔵 (✓) *target: good*
  > Gen 1:31 And God saw everything that he had made , and behold , it was very good . And there was evening and there was morning , the sixth day .
  - notes: Divine evaluative pronouncement on the whole creation — "very good"
- **Gen 1:4** (✓) *target: good*
  > Gen 1:4 And God saw that the light was good . And God separated the light from the darkness .
  - notes: Divine evaluative pronouncement on created light — God's inner-being action of judging-as-good
- **Gen 1:10** (✓) *target: good*
  > Gen 1:10 God called the dry land Earth , and the waters that were gathered together he called Seas . And God saw that it was good .
  - notes: Divine evaluative pronouncement on dry land/seas
- **Gen 1:12** (✓) *target: good*
  > Gen 1:12 The earth brought forth vegetation , plants yielding seed according to their own kinds , and trees bearing fruit in which is their seed , each according to its kind . And God saw that it was good .
  - notes: Divine evaluative pronouncement on vegetation
- **Gen 1:18** (✓) *target: good*
  > Gen 1:18 to rule over the day and over the night , and to separate the light from the darkness . And God saw that it was good .
  - notes: Divine evaluative pronouncement on luminaries
- **Gen 1:21** (✓) *target: good*
  > Gen 1:21 So God created the great sea creatures and every living creature that moves , with which the waters swarm , according to their kinds , and every winged bird according to its kind . And God saw that it was good .
  - notes: Divine evaluative pronouncement on sea creatures and birds
- **Gen 1:25** (✓) *target: good*
  > Gen 1:25 And God made the beasts of the earth according to their kinds and the livestock according to their kinds , and everything that creeps on the ground according to its kind . And God saw that it was good .
  - notes: Divine evaluative pronouncement on land animals

**Group `884-008`** (40 verses — anchors: Jer 26:14)

- **Jer 26:14** 🔵 (✓) *target: good*
  > Jer 26:14 But as for me , behold , I am in your hands . Do with me as seems good and right to you .
  - notes: "Do with me as seems good and right to you" — Jeremiah's submission
- **Gen 16:6** (✓) *target: please*
  > Gen 16:6 But Abram said to Sarai , “ Behold , your servant is in your power ; do to her as you please .” Then Sarai dealt harshly with her, and she fled from her .
  - notes: "Do to her as you please" (good in your eyes) — names what is good/preferred to Abram's will; volitional engagement
- **Gen 19:8** (✓) *target: please*
  > Gen 19:8 Behold , I have two daughters who have not known any man . Let me bring them out to you, and do to them as you please . Only do nothing to these men , for they have come under the shelter of my roof .”
  - notes: "Do to them as you please" — Lot offering daughters; tov as predicate of will
- **Gen 20:15** (✓) *target: pleases*
  > Gen 20:15 And Abimelech said , “Behold, my land is before you ; dwell where it pleases you .”
  - notes: "Where it pleases you" — Abimelech's permission; volitional preference
- **Gen 29:19** (✓) *target: better*
  > Gen 29:19 Laban said , “It is better that I give her to you than that I should give her to any other man ; stay with me .”
  - notes: "Better that I give her to you" — Laban's expressed preference/judgement; volitional-relational
- **Gen 40:16** (✓) *target: favorable*
  > Gen 40:16 When the chief baker saw that the interpretation was favorable , he said to Joseph , “I also had a dream : there were three cake baskets on my head ,
  - notes: "Interpretation was favorable (good)" — chief baker's evaluative judgement of Joseph's interpretation; inner-being assessment
- **Num 36:6** (✓) *target: best*
  > Num 36:6 This is what the Lord commands concerning the daughters of Zelophehad : ‘Let them marry whom they think best , only they shall marry within the clan of the tribe of their father .
  - notes: "Marry whom they think best" — Zelophehad's daughters' preference; volitional
- **Deu 1:14** (✓) *target: good*
  > Deu 1:14 And you answered me, ‘The thing that you have spoken is good for us to do .’
  - notes: "Thing you have spoken is good for us to do" — people's evaluative agreement
- **Deu 23:16** (✓) *target: suits*
  > Deu 23:16 He shall dwell with you, in your midst , in the place that he shall choose within one of your towns , wherever it suits him. You shall not wrong him .
  - notes: "Wherever it suits him" (in good in his eyes) — runaway slave's preference; volitional
- **Jos 9:25** (✓) *target: good*
  > Jos 9:25 And now , behold , we are in your hand . Whatever seems good and right in your sight to do to us, do it.”
  - notes: "Whatever seems good and right in your sight" — Gibeonites; volitional submission
- **Judg 10:15** (✓) *target: good*
  > Judg 10:15 And the people of Israel said to the Lord , “We have sinned ; do to us whatever seems good to you. Only please deliver us this day .”
  - notes: "Do to us whatever seems good to you" — Israel's repentant submission to God; volitional
- **Judg 19:24** (✓) *target: good*
  > Judg 19:24 Behold , here are my virgin daughter and his concubine . Let me bring them out now. Violate them and do with them what seems good to you, but against this man do not do this outrageous thing .”
  - notes: "Do with them what seems good to you" — Levite's host offering daughter/concubine; volitional (a deeply morally fraught instance, but tov's engagement is volitional-preference)
- **Rut 2:22** (✓) *target: good*
  > Rut 2:22 And Naomi said to Ruth , her daughter-in-law , “ It is good , my daughter , that you go out with his young women , lest in another field you be assaulted .”
  - notes: "It is good, my daughter, that you go out" — Naomi's evaluative judgement/counsel
- **Rut 3:13** (✓) *target: good*
  > Rut 3:13 Remain tonight , and in the morning , if he will redeem you, good ; let him do it . But if he is not willing to redeem you, then, as the Lord lives , I will redeem you. Lie down until the morning .”
  - notes: "If he will redeem you, good" — Boaz's conditional agreement-judgement
- **1Sa 1:23** (✓) *target: best*
  > 1Sa 1:23 Elkanah her husband said to her, “ Do what seems best to you; wait until you have weaned him; only , may the Lord establish his word .” So the woman remained and nursed her son until she weaned him .
  - notes: "Do what seems best to you" — Elkanah to Hannah; volitional submission
- **1Sa 3:18** (✓) *target: good*
  > 1Sa 3:18 So Samuel told him everything and hid nothing from him. And he said , “It is the Lord . Let him do what seems good to him.”
  - notes: "Let him do what seems good to him" — Eli's submission to God's judgement
- **1Sa 9:10** (✓) *target: Well*
  > 1Sa 9:10 And Saul said to his servant , “ Well said ; come , let us go .” So they went to the city where the man of God was.
  - notes: "Well said" — Saul's agreement to servant's suggestion
- **1Sa 11:10** (✓) *target: good*
  > 1Sa 11:10 Therefore the men of Jabesh said , “ Tomorrow we will give ourselves up to you, and you may do to us whatever seems good to you.”
  - notes: "Do whatever seems good to you" — Jabesh-gilead's submission
- **1Sa 14:36** (✓) *target: good*
  > 1Sa 14:36 Then Saul said , “Let us go down after the Philistines by night and plunder them until the morning light ; let us not leave a man of them.” And they said , “ Do whatever seems good to you.” But the priest said , “Let us draw near to God here .”
  - notes: "Do whatever seems good to you" — people to Saul
- **1Sa 14:40** (✓) *target: good*
  > 1Sa 14:40 Then he said to all Israel , “You shall be on one side , and I and Jonathan my son will be on the other side .” And the people said to Saul , “ Do what seems good to you.”
  - notes: "Do what seems good to you" — people to Saul
- **1Sa 20:7** (✓) *target: Good*
  > 1Sa 20:7 If he says , ‘ Good !’ it will be well with your servant , but if he is angry , then know that harm is determined by him .
  - notes: "If he says 'Good!'" — Saul's inner approval/agreement (cf. inner-being engagement of agreement)
- **2Sa 3:13** (✓) *target: Good*
  > 2Sa 3:13 And he said , “ Good ; I will make a covenant with you. But one thing I require of you; that is , you shall not see my face unless you first bring Michal , Saul’s daughter , when you come to see my face .”
  - notes: "Good; I will make a covenant" — David's conditional agreement
- **2Sa 15:3** (✓) *target: good*
  > 2Sa 15:3 Absalom would say to him, “ See , your claims are good and right , but there is no man designated by the king to hear you.”
  - notes: "Your claims are good and right" — Absalom's flattering evaluation
- **2Sa 19:18** (✓) *target: pleasure*
  > 2Sa 19:18 and they crossed the ford to bring over the king’s household and to do his pleasure . And Shimei the son of Gera fell down before the king , as he was about to cross the Jordan ,
  - notes: "Do his pleasure" (good in his eyes) — servants of king's preference
- **2Sa 19:27** (✓) *target: good*
  > 2Sa 19:27 He has slandered your servant to my lord the king . But my lord the king is like the angel of God ; do therefore what seems good to you .
  - notes: "Do what seems good to you" — Mephibosheth to David
- **2Sa 19:38** (✓) *target: good*
  > 2Sa 19:38 And the king answered , “ Chimham shall go over with me , and I will do for him whatever seems good to you , and all that you desire of me I will do for you .”
  - notes: "Whatever seems good to you" — David to Barzillai
- **Neh 2:5** (✓) *target: pleases*
  > Neh 2:5 And I said to the king , “ If it pleases the king , and if your servant has found favor in your sight , that you send me to Judah , to the city of my fathers ’ graves , that I may rebuild it .”
  - notes: "If it pleases the king" — Nehemiah; volitional-relational request
- **Neh 2:7** (✓) *target: pleases*
  > Neh 2:7 And I said to the king , “ If it pleases the king , let letters be given me to the governors of the province Beyond the River , that they may let me pass through until I come to Judah ,
  - notes: "If it pleases the king" — Nehemiah; same
- **Est 1:19** (✓) *target: please*
  > Est 1:19 If it please the king , let a royal order go out from him , and let it be written among the laws of the Persians and the Medes so that it may not be repealed , that Vashti is never again to come before King Ahasuerus . And let the king give her royal position to another who is better than she .
  - notes: "If it please the king" — Memucan's counsel
- **Est 3:9** (✓) *target: please*
  > Est 3:9 If it please the king , let it be decreed that they be destroyed , and I will pay 10,000 talents of silver into the hands of those who have charge of the king’s business , that they may put it into the king’s treasuries .”
  - notes: "If it please the king" — Haman's decree request
- **Est 3:11** (✓) *target: good*
  > Est 3:11 And the king said to Haman , “The money is given to you, the people also, to do with them as it seems good to you.”
  - notes: "As it seems good to you" — king's permission to Haman
- **Est 5:4** (✓) *target: please*
  > Est 5:4 And Esther said , “ If it please the king , let the king and Haman come today to a feast that I have prepared for the king .”
  - notes: "If it please the king" — Esther
- **Est 5:8** (✓) *target: please*
  > Est 5:8 If I have found favor in the sight of the king , and if it please the king to grant my wish and fulfill my request , let the king and Haman come to the feast that I will prepare for them, and tomorrow I will do as the king has said .”
  - notes: "If it please the king" — Esther
- **Est 7:3** (✓) *target: please*
  > Est 7:3 Then Queen Esther answered , “ If I have found favor in your sight , O king , and if it please the king , let my life be granted me for my wish , and my people for my request .
  - notes: "If it please the king" — Esther
- **Est 8:5** (✓) *target: please*
  > Est 8:5 And she said , “ If it please the king , and if I have found favor in his sight , and if the thing seems right before the king , and I am pleasing in his eyes , let an order be written to revoke the letters devised by Haman the Agagite , the son of Hammedatha , which he wrote to destroy the Jews who are in all the provinces of the king .
  - notes: "If it please the king" — Esther
- **Est 8:8** (✓) *target: please*
  > Est 8:8 But you may write as you please with regard to the Jews , in the name of the king , and seal it with the king’s ring , for an edict written in the name of the king and sealed with the king’s ring cannot be revoked .”
  - notes: "Write as you please" — king to Esther/Mordecai
- **Est 9:13** (✓) *target: please*
  > Est 9:13 And Esther said , “ If it please the king , let the Jews who are in Susa be allowed tomorrow also to do according to this day’s edict . And let the ten sons of Haman be hanged on the gallows .”
  - notes: "If it please the king" — Esther
- **Isa 41:7** (✓) *target: good*
  > Isa 41:7 The craftsman strengthens the goldsmith , and he who smooths with the hammer him who strikes the anvil , saying of the soldering , “It is good ”; and they strengthen it with nails so that it cannot be moved .
  - notes: "Saying of the soldering, It is good" — craftsman's evaluative judgement on workmanship; inner-being assessment
- **Jer 40:4** (✓) *target: good*
  > Jer 40:4 Now , behold , I release you today from the chains on your hands . If it seems good to you to come with me to Babylon , come , and I will look after you well , but if it seems wrong to you to come with me to Babylon , do not come . See , the whole land is before you; go wherever you think it good and right to go .
  - notes: "If it seems good to you to come" / "go wherever you think good and right" — Nebuzaradan to Jeremiah; volitional preference
- **Zec 11:12** (✓) *target: good*
  > Zec 11:12 Then I said to them, “ If it seems good to you, give me my wages ; but if not , keep them.” And they weighed out as my wages thirty pieces of silver .
  - notes: "If it seems good to you, give me my wages" — symbolic shepherd to flock; volitional preference

**Group `884-009`** (5 verses — anchors: Est 5:9)

- **Est 5:9** 🔵 (✓) *target: glad*
  > Est 5:9 And Haman went out that day joyful and glad of heart . But when Haman saw Mordecai in the king’s gate , that he neither rose nor trembled before him, he was filled with wrath against Mordecai .
  - notes: "Joyful and glad of heart" (tov-lev) — Haman's inner emotional state; explicit inner-being engagement
- **Deu 19:13** (✓) *target: well*
  > Deu 19:13 Your eye shall not pity him , but you shall purge the guilt of innocent blood from Israel , so that it may be well with you .
  - notes: "Well with you" — names the state of well-being / shalom resulting from purging guilt; relational-covenantal inner-being state
- **Deu 30:9** (✓) *target: prosperous*
  > Deu 30:9 The Lord your God will make you abundantly prosperous in all the work of your hand , in the fruit of your womb and in the fruit of your cattle and in the fruit of your ground . For the Lord will again take delight in prospering you, as he took delight in your fathers ,
  - notes: "Make you abundantly prosperous" — covenantal-relational well-being; tov names the state of being-prospered
- **1Sa 16:16** (✓) *target: well*
  > 1Sa 16:16 Let our lord now command your servants who are before you to seek out a man who is skillful in playing the lyre , and when the harmful spirit from God is upon you, he will play it, and you will be well .”
  - notes: "You will be well" (relief from harmful spirit) — names inner-being state of relief/well-being
- **1Sa 20:12** (✓) *target: well disposed*
  > 1Sa 20:12 And Jonathan said to David , “The Lord , the God of Israel , be witness ! When I have sounded out my father , about this time tomorrow , or the third day, behold , if he is well disposed toward David , shall I not then send and disclose it to you ?
  - notes: "Well disposed toward David" — Saul's relational-emotional disposition; inner-being

**Group `SET-ASIDE`** (76 verses)

- **Gen 2:9** (✗) [set_aside: physical_only] *target: good*
  > Gen 2:9 And out of the ground the Lord God made to spring up every tree that is pleasant to the sight and good for food . The tree of life was in the midst of the garden , and the tree of the knowledge of good and evil .
  - notes: "Good for food" — physical quality of trees in Eden
- **Gen 2:12** (✗) [set_aside: physical_only] *target: good*
  > Gen 2:12 And the gold of that land is good ; bdellium and onyx stone are there.
  - notes: "Gold of that land is good" — physical-quality descriptor of gold
- **Gen 6:2** (✗) [set_aside: physical_only] *target: attractive*
  > Gen 6:2 the sons of God saw that the daughters of man were attractive . And they took as their wives any they chose .
  - notes: "Daughters of man were attractive" (tovat) — physical-aesthetic descriptor
- **Gen 15:15** (✗) [set_aside: no_inner_being] *target: good*
  > Gen 15:15 As for you , you shall go to your fathers in peace ; you shall be buried in a good old age .
  - notes: "Good old age" — names completed life-quality at death; tov modifies physical-temporal age
- **Gen 18:7** (✗) [set_aside: physical_only] *target: good*
  > Gen 18:7 And Abraham ran to the herd and took a calf , tender and good , and gave it to a young man , who prepared it quickly .
  - notes: "Calf, tender and good" — physical-quality of meat
- **Gen 24:16** (✗) [set_aside: physical_only] *target: attractive*
  > Gen 24:16 The young woman was very attractive in appearance , a maiden whom no man had known . She went down to the spring and filled her jar and came up .
  - notes: "Very attractive in appearance" (Rebekah) — physical beauty
- **Gen 24:50** (✗) [set_aside: no_inner_being] *target: good*
  > Gen 24:50 Then Laban and Bethuel answered and said , “The thing has come from the Lord ; we cannot speak to you bad or good .
  - notes: "Cannot speak to you bad or good" — Hebrew merism for "anything at all"
- **Gen 25:8** (✗) [set_aside: no_inner_being] *target: good*
  > Gen 25:8 Abraham breathed his last and died in a good old age , an old man and full of years, and was gathered to his people .
  - notes: "Good old age" (Abraham's death) — names life-quality completion
- **Gen 26:7** (✗) [set_aside: physical_only] *target: attractive*
  > Gen 26:7 When the men of the place asked him about his wife , he said , “She is my sister ,” for he feared to say , “My wife ,” thinking, “lest the men of the place should kill me because of Rebekah ,” because she was attractive in appearance .
  - notes: "Attractive in appearance" (Rebekah) — physical beauty
- **Gen 27:9** (✗) [set_aside: physical_only] *target: good*
  > Gen 27:9 Go to the flock and bring me two good young goats , so that I may prepare from them delicious food for your father , such as he loves .
  - notes: "Good young goats" — physical-quality of animals for food
- **Gen 30:20** (✗) [set_aside: physical_only] *target: good*
  > Gen 30:20 Then Leah said , “ God has endowed me with a good endowment ; now my husband will honor me , because I have borne him six sons .” So she called his name Zebulun .
  - notes: "Good endowment" — names physical/material gift; Leah's claim about God's gift to her — borderline but tov here qualifies the physical endowment (sons/dowry)
- **Gen 31:24** (✗) [set_aside: no_inner_being] *target: good*
  > Gen 31:24 But God came to Laban the Aramean in a dream by night and said to him, “Be careful not to say anything to Jacob , either good or bad .”
  - notes: "Either good or bad" — merism; God's warning to Laban
- **Gen 31:29** (✗) [set_aside: no_inner_being] *target: good*
  > Gen 31:29 It is in my power to do you harm . But the God of your father spoke to me last night , saying , ‘Be careful not to say anything to Jacob , either good or bad .’
  - notes: "Either good or bad" — merism; Laban citing God's warning
- **Gen 41:5** (✗) [set_aside: physical_only] *target: good*
  > Gen 41:5 And he fell asleep and dreamed a second time . And behold , seven ears of grain , plump and good , were growing on one stalk .
  - notes: "Plump and good ears of grain" — dream-content; physical quality of grain
- **Gen 41:22** (✗) [set_aside: physical_only] *target: good*
  > Gen 41:22 I also saw in my dream seven ears growing on one stalk , full and good .
  - notes: Dream — physical quality of ears
- **Gen 41:24** (✗) [set_aside: physical_only] *target: good*
  > Gen 41:24 and the thin ears swallowed up the seven good ears . And I told it to the magicians , but there was no one who could explain it to me .”
  - notes: Dream — physical quality of ears
- **Gen 41:26** (✗) [set_aside: physical_only] *target: good*
  > Gen 41:26 The seven good cows are seven years , and the seven good ears are seven years ; the dreams are one .
  - notes: Dream interpretation — physical quality of cows/ears
- **Gen 41:35** (✗) [set_aside: physical_only] *target: good*
  > Gen 41:35 And let them gather all the food of these good years that are coming and store up grain under the authority of Pharaoh for food in the cities , and let them keep it.
  - notes: "Good years that are coming" — qualifies temporal/physical abundance years
- **Gen 49:15** (✗) [set_aside: physical_only] *target: good*
  > Gen 49:15 He saw that a resting place was good , and that the land was pleasant , so he bowed his shoulder to bear , and became a servant at forced labor .
  - notes: "Resting place was good, land was pleasant" — Issachar oracle; tov names physical-quality of place
- **Exo 2:2** (✗) [set_aside: physical_only] *target: fine*
  > Exo 2:2 The woman conceived and bore a son , and when she saw that he was a fine child, she hid him three months .
  - notes: "He was a fine child" (Moses) — physical-aesthetic of infant
- **Exo 3:8** (✗) [set_aside: physical_only] *target: good*
  > Exo 3:8 and I have come down to deliver them out of the hand of the Egyptians and to bring them up out of that land to a good and broad land , a land flowing with milk and honey , to the place of the Canaanites , the Hittites , the Amorites , the Perizzites , the Hivites , and the Jebusites .
  - notes: "Good and broad land" — covenantal-promise but tov names the physical territory
- **Lev 27:10** (✗) [set_aside: no_inner_being] *target: good*
  > Lev 27:10 He shall not exchange it or make a substitute for it, good for bad , or bad for good ; and if he does in fact substitute one animal for another , then both it and the substitute shall be holy .
  - notes: "Good for bad" merism; legal-substitution
- **Lev 27:12** (✗) [set_aside: no_inner_being] *target: good*
  > Lev 27:12 and the priest shall value it as either good or bad ; as the priest values it, so it shall be .
  - notes: "Either good or bad" — priestly valuation merism
- **Lev 27:14** (✗) [set_aside: no_inner_being] *target: good*
  > Lev 27:14 “When a man dedicates his house as a holy gift to the Lord , the priest shall value it as either good or bad ; as the priest values it, so it shall stand .
  - notes: "Either good or bad" — priestly valuation merism
- **Lev 27:33** (✗) [set_aside: no_inner_being] *target: good*
  > Lev 27:33 One shall not differentiate between good or bad , neither shall he make a substitute for it; and if he does substitute for it , then both it and the substitute shall be holy ; it shall not be redeemed .”
  - notes: "Between good or bad" — substitution merism
- **Num 13:19** (✗) [set_aside: no_inner_being] *target: good*
  > Num 13:19 and whether the land that they dwell in is good or bad , and whether the cities that they dwell in are camps or strongholds ,
  - notes: "Land is good or bad" — spies' reconnaissance question (merism for evaluation framework)
- **Num 14:7** (✗) [set_aside: physical_only] *target: good*
  > Num 14:7 and said to all the congregation of the people of Israel , “The land , which we passed through to spy it out , is an exceedingly good land .
  - notes: "Land is exceedingly good land" — Joshua/Caleb spy report; physical-territorial
- **Deu 1:25** (✗) [set_aside: physical_only] *target: good*
  > Deu 1:25 And they took in their hands some of the fruit of the land and brought it down to us, and brought us word again and said , ‘It is a good land that the Lord our God is giving us .’
  - notes: "Good land that the LORD our God is giving us" — covenantal promise; tov names land
- **Deu 1:35** (✗) [set_aside: physical_only] *target: good*
  > Deu 1:35 ‘ Not one of these men of this evil generation shall see the good land that I swore to give to your fathers ,
  - notes: "Good land swore to give to your fathers" — covenant; physical territory
- **Deu 3:25** (✗) [set_aside: physical_only] *target: good*
  > Deu 3:25 Please let me go over and see the good land beyond the Jordan , that good hill country and Lebanon .’
  - notes: "Good land beyond Jordan, good hill country" — physical territory
- **Deu 4:21** (✗) [set_aside: physical_only] *target: good*
  > Deu 4:21 Furthermore, the Lord was angry with me because of you , and he swore that I should not cross the Jordan , and that I should not enter the good land that the Lord your God is giving you for an inheritance .
  - notes: "Good land for inheritance" — covenant; physical
- **Deu 4:22** (✗) [set_aside: physical_only] *target: good*
  > Deu 4:22 For I must die in this land ; I must not go over the Jordan . But you shall go over and take possession of that good land .
  - notes: "Take possession of that good land" — physical territory
- **Deu 6:10** (✗) [set_aside: physical_only] *target: good*
  > Deu 6:10 “And when the Lord your God brings you into the land that he swore to your fathers , to Abraham , to Isaac , and to Jacob , to give you—with great and good cities that you did not build ,
  - notes: "Great and good cities" — physical-quality of cities
- **Deu 8:7** (✗) [set_aside: physical_only] *target: good*
  > Deu 8:7 For the Lord your God is bringing you into a good land , a land of brooks of water , of fountains and springs , flowing out in the valleys and hills ,
  - notes: "Good land — brooks of water, fountains" — physical territory
- **Deu 8:12** (✗) [set_aside: physical_only] *target: good*
  > Deu 8:12 lest , when you have eaten and are full and have built good houses and live in them,
  - notes: "Good houses" — physical structures
- **Deu 11:17** (✗) [set_aside: physical_only] *target: good*
  > Deu 11:17 then the anger of the Lord will be kindled against you, and he will shut up the heavens , so that there will be no rain , and the land will yield no fruit , and you will perish quickly off the good land that the Lord is giving you .
  - notes: "Good land that the LORD is giving" — physical territory
- **Deu 28:12** (✗) [set_aside: physical_only] *target: good*
  > Deu 28:12 The Lord will open to you his good treasury , the heavens , to give the rain to your land in its season and to bless all the work of your hands . And you shall lend to many nations , but you shall not borrow .
  - notes: "His good treasury, the heavens" — figurative-physical (rain/blessing source)
- **Jos 7:21** (✗) [set_aside: physical_only] *target: beautiful*
  > Jos 7:21 when I saw among the spoil a beautiful cloak from Shinar , and 200 shekels of silver , and a bar of gold weighing 50 shekels , then I coveted them and took them. And see , they are hidden in the earth inside my tent , with the silver underneath .”
  - notes: "Beautiful cloak from Shinar" — Achan's coveted item; physical-aesthetic
- **Jos 23:13** (✗) [set_aside: physical_only] *target: good*
  > Jos 23:13 know for certain that the Lord your God will no longer drive out these nations before you, but they shall be a snare and a trap for you, a whip on your sides and thorns in your eyes , until you perish from off this good ground that the Lord your God has given you.
  - notes: "This good ground that the LORD has given" — covenantal land
- **Judg 8:32** (✗) [set_aside: no_inner_being] *target: good*
  > Judg 8:32 And Gideon the son of Joash died in a good old age and was buried in the tomb of Joash his father , at Ophrah of the Abiezrites .
  - notes: "Gideon died in good old age" — completed life
- **Judg 9:11** (✗) [set_aside: physical_only] *target: good*
  > Judg 9:11 But the fig tree said to them, ‘Shall I leave my sweetness and my good fruit and go hold sway over the trees ?’
  - notes: "My sweetness and my good fruit" — fig tree parable; physical fruit-quality
- **Judg 15:2** (✗) [set_aside: physical_only] *target: more beautiful*
  > Judg 15:2 And her father said , “I really thought that you utterly hated her, so I gave her to your companion . Is not her younger sister more beautiful than she ? Please take her instead .”
  - notes: "Younger sister more beautiful" — Samson's wife's sister; physical aesthetic
- **Judg 18:9** (✗) [set_aside: physical_only] *target: good*
  > Judg 18:9 They said , “ Arise , and let us go up against them, for we have seen the land , and behold, it is very good . And will you do nothing ? Do not be slow to go , to enter in and possess the land .
  - notes: "We have seen the land, behold it is very good" — Dan's spies; physical territory
- **1Sa 8:14** (✗) [set_aside: physical_only] *target: best*
  > 1Sa 8:14 He will take the best of your fields and vineyards and olive orchards and give them to his servants .
  - notes: "Best of fields/vineyards/olives" — Samuel's warning; physical-quality property
- **1Sa 8:16** (✗) [set_aside: physical_only] *target: best*
  > 1Sa 8:16 He will take your male servants and female servants and the best of your young men and your donkeys , and put them to his work .
  - notes: "Best of young men/donkeys" — physical-extraction warning
- **1Sa 9:2** (✗) [set_aside: physical_only] *target: handsome*
  > 1Sa 9:2 And he had a son whose name was Saul , a handsome young man . There was not a man among the people of Israel more handsome than he. From his shoulders upward he was taller than any of the people .
  - notes: "Saul handsome young man, more handsome" — physical-aesthetic
- **1Sa 16:12** (✗) [set_aside: physical_only] *target: handsome*
  > 1Sa 16:12 And he sent and brought him in . Now he was ruddy and had beautiful eyes and was handsome . And the Lord said , “ Arise , anoint him, for this is he .”
  - notes: "Ruddy, beautiful eyes, handsome" (David) — physical-aesthetic
- **1Sa 25:8** (✗) [set_aside: no_inner_being] *target: feast*
  > 1Sa 25:8 Ask your young men , and they will tell you. Therefore let my young men find favor in your eyes , for we come on a feast day . Please give whatever you have at hand to your servants and to your son David .’”
  - notes: "Feast day" (yom tov) — idiomatic noun-phrase for festival day
- **2Sa 11:2** (✗) [set_aside: physical_only] *target: beautiful*
  > 2Sa 11:2 It happened, late one afternoon , when David arose from his couch and was walking on the roof of the king’s house , that he saw from the roof a woman bathing ; and the woman was very beautiful .
  - notes: "Bathsheba very beautiful" — physical-aesthetic
- **Ezr 8:27** (✗) [set_aside: physical_only] *target: fine*
  > Ezr 8:27 20 bowls of gold worth 1,000 darics , and two vessels of fine bright bronze as precious as gold .
  - notes: "Two vessels of fine bright bronze" — physical-quality of metalwork
- **Est 1:11** (✗) [set_aside: physical_only] *target: lovely*
  > Est 1:11 to bring Queen Vashti before the king with her royal crown , in order to show the peoples and the princes her beauty , for she was lovely to look at .
  - notes: "Vashti lovely to look at" — physical-aesthetic
- **Est 2:2** (✗) [set_aside: physical_only] *target: beautiful*
  > Est 2:2 Then the king’s young men who attended him said , “Let beautiful young virgins be sought out for the king .
  - notes: "Beautiful young virgins" — physical-aesthetic
- **Est 2:3** (✗) [set_aside: physical_only] *target: beautiful*
  > Est 2:3 And let the king appoint officers in all the provinces of his kingdom to gather all the beautiful young virgins to the harem in Susa the citadel , under custody of Hegai , the king’s eunuch , who is in charge of the women . Let their cosmetics be given them.
  - notes: "Beautiful young virgins" — physical-aesthetic
- **Est 2:7** (✗) [set_aside: physical_only] *target: lovely*
  > Est 2:7 He was bringing up Hadassah , that is Esther , the daughter of his uncle , for she had neither father nor mother . The young woman had a beautiful figure and was lovely to look at , and when her father and her mother died , Mordecai took her as his own daughter .
  - notes: "Esther beautiful figure, lovely to look at" — physical-aesthetic
- **Est 2:9** (✗) [set_aside: physical_only] *target: best place*
  > Est 2:9 And the young woman pleased him and won his favor . And he quickly provided her with her cosmetics and her portion of food , and with seven chosen young women from the king’s palace , and advanced her and her young women to the best place in the harem .
  - notes: "Best place in the harem" — physical-spatial advantage
- **Est 7:9** (✗) [set_aside: no_inner_being] *target: word*
  > Est 7:9 Then Harbona , one of the eunuchs in attendance on the king , said , “ Moreover , the gallows that Haman has prepared for Mordecai , whose word saved the king , is standing at Haman’s house , fifty cubits high .”
  - notes: "Whose word saved the king" (target rendered "word" — likely tov is part of phrase "good word" / spoke favorably about the king); narrative description of past action; the inner-being content of Mordecai's loyalty is in the underlying narrative, not in tov here. Borderline — flagging.
- **Est 8:17** (✗) [set_aside: no_inner_being] *target: holiday*
  > Est 8:17 And in every province and in every city , wherever the king’s command and his edict reached , there was gladness and joy among the Jews , a feast and a holiday . And many from the peoples of the country declared themselves Jews , for fear of the Jews had fallen on them .
  - notes: "Holiday" (yom tov) — idiomatic festival-day
- **Est 9:19** (✗) [set_aside: no_inner_being] *target: holiday*
  > Est 9:19 Therefore the Jews of the villages , who live in the rural towns , hold the fourteenth day of the month of Adar as a day for gladness and feasting , as a holiday , and as a day on which they send gifts of food to one another .
  - notes: "Holiday" (yom tov) — idiomatic festival-day
- **Est 9:22** (✗) [set_aside: no_inner_being] *target: holiday*
  > Est 9:22 as the days on which the Jews got relief from their enemies , and as the month that had been turned for them from sorrow into gladness and from mourning into a holiday ; that they should make them days of feasting and gladness , days for sending gifts of food to one another and gifts to the poor .
  - notes: "Holiday" — idiomatic festival-day
- **Psa 133:2** (✗) *target: precious*
  > Psa 133:2 It is like the precious oil on the head , running down on the beard , on the beard of Aaron , running down on the collar of his robes !
  - notes: physical/ornamental simile; no inner-being engagement
- **Pro 24:13** (✗) [set_aside: physical_only] *target: good*
  > Pro 24:13 My son , eat honey , for it is good , and the drippings of the honeycomb are sweet to your taste .
  - notes: "Honey is good" — physical-quality; introductory metaphor for wisdom in following verses, but tov here qualifies the physical honey
- **Isa 5:9** (✗) [set_aside: physical_only] *target: beautiful*
  > Isa 5:9 The Lord of hosts has sworn in my hearing : “ Surely many houses shall be desolate , large and beautiful houses, without inhabitant .
  - notes: "Beautiful houses desolate" — physical-aesthetic of buildings
- **Isa 39:2** (✗) [set_aside: physical_only] *target: precious*
  > Isa 39:2 And Hezekiah welcomed them gladly . And he showed them his treasure house , the silver , the gold , the spices , the precious oil , his whole armory , all that was found in his storehouses . There was nothing in his house or in all his realm that Hezekiah did not show them.
  - notes: "Precious oil" (tov) — Hezekiah's treasure; physical-quality
- **Jer 6:20** (✗) [set_aside: physical_only] *target: sweet*
  > Jer 6:20 What use to me is frankincense that comes from Sheba , or sweet cane from a distant land ? Your burnt offerings are not acceptable , nor your sacrifices pleasing to me .
  - notes: "Sweet (good) cane from distant land" — physical-quality of incense/cane offering material
- **Jer 24:2** (✗) [set_aside: physical_only] *target: good*
  > Jer 24:2 One basket had very good figs , like first-ripe figs , but the other basket had very bad figs , so bad that they could not be eaten .
  - notes: "Good figs" — physical-quality (vision content; symbolism is in the broader narrative)
- **Jer 24:3** (✗) [set_aside: physical_only] *target: good*
  > Jer 24:3 And the Lord said to me, “ What do you see , Jeremiah ?” I said , “ Figs , the good figs very good , and the bad figs very bad , so bad that they cannot be eaten .”
  - notes: "Good figs very good" — physical-quality in vision
- **Jer 24:5** (✗) [set_aside: physical_only] *target: good*
  > Jer 24:5 “ Thus says the Lord , the God of Israel : Like these good figs , so I will regard as good the exiles from Judah , whom I have sent away from this place to the land of the Chaldeans .
  - notes: "Like these good figs, so I will regard the exiles" — vehicle of metaphor; tov in vehicle qualifies physical figs (the tenor is the exiles' inner-being-relational status, but tov names the figs)
- **Lam 4:1** (✗) [set_aside: physical_only] *target: pure*
  > Lam 4:1 How the gold has grown dim , how the pure gold is changed ! The holy stones lie scattered at the head of every street .
  - notes: "Pure gold (tov) is changed" — physical-quality of gold (figurative for Zion's former glory; tov names the physical metal in the vehicle)
- **Eze 17:8** (✗) [set_aside: physical_only] *target: good*
  > Eze 17:8 It had been planted on good soil by abundant waters , that it might produce branches and bear fruit and become a noble vine .
  - notes: "Good soil" — figurative-vine; tov names physical agricultural quality in the vehicle
- **Eze 24:4** (✗) [set_aside: physical_only] *target: good*
  > Eze 24:4 put in it the pieces of meat , all the good pieces , the thigh and the shoulder ; fill it with choice bones .
  - notes: "Good pieces of meat" — Ezekiel's pot allegory; tov names physical-quality of meat in vehicle
- **Eze 31:16** (✗) [set_aside: physical_only] *target: best*
  > Eze 31:16 I made the nations quake at the sound of its fall , when I cast it down to Sheol with those who go down to the pit . And all the trees of Eden , the choice and best of Lebanon , all that drink water , were comforted in the world below .
  - notes: "Choice and best of Lebanon" (trees) — figurative; tov of physical trees
- **Eze 34:14** (✗) [set_aside: physical_only] *target: good*
  > Eze 34:14 I will feed them with good pasture , and on the mountain heights of Israel shall be their grazing land . There they shall lie down in good grazing land , and on rich pasture they shall feed on the mountains of Israel .
  - notes: "Good pasture, good grazing land" — Ezekiel's shepherd allegory; the relational tenor (God shepherding faithfully) is in the broader allegory; tov here qualifies physical pasture in the vehicle
- **Dan 1:15** (✗) [set_aside: physical_only] *target: better*
  > Dan 1:15 At the end of ten days it was seen that they were better in appearance and fatter in flesh than all the youths who ate the king’s food .
  - notes: "Better in appearance, fatter in flesh" — physical-aesthetic comparison
- **Hos 4:13** (✗) [set_aside: physical_only] *target: good*
  > Hos 4:13 They sacrifice on the tops of the mountains and burn offerings on the hills , under oak , poplar , and terebinth , because their shade is good . Therefore your daughters play the whore , and your brides commit adultery .
  - notes: "Their shade is good" (trees of high places used in idolatry) — physical-quality of shade; the verse's inner-being weight (idolatry indictment) is in the surrounding sacrificial-action verbs, not in tov
- **Joe 3:5** (✗) [set_aside: physical_only] *target: rich*
  > Joe 3:5 For you have taken my silver and my gold , and have carried my rich treasures into your temples .
  - notes: "Rich (good) treasures" — physical wealth taken into pagan temples
- **Nah 3:4** (✗) [set_aside: physical_only] *target: and*
  > Nah 3:4 And all for the countless whorings of the prostitute , graceful and of deadly charms , who betrays nations with her whorings , and peoples with her charms .
  - notes: "Graceful (tov) and of deadly charms" (prostitute Nineveh) — figurative-physical aesthetic of personification; the inner-being weight is in the figurative-political indictment, not in tov which qualifies the prostitute-figure's aesthetic

### `G0019` — 4/4 classified · 1 anchor verse(s)

**Group `885-001`** (4 verses — anchors: Gal 5:22)

- **Gal 5:22** 🔵 (✓) *target: goodness*
  > Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,
- **Rom 15:14** (✓) *target: goodness*
  > Rom 15:14 I myself am satisfied about you , my brothers , that you yourselves are full of goodness , filled with all knowledge and able to instruct one another .
- **Eph 5:9** (✓) *target: good*
  > Eph 5:9 ( for the fruit of light is found in all that is good and right and true ),
- **2Th 1:11** (✓) *target: good*
  > 2Th 1:11 To this end we always pray for you , that our God may make you worthy of his calling and may fulfill every resolve for good and every work of faith by his power ,

### `G5544` — 7/7 classified · 2 anchor verse(s)

**Group `886-001`** (3 verses — anchors: Rom 11:22)

- **Rom 11:22** 🔵 (✓) *target: kindness*
  > Rom 11:22 Note then the kindness and the severity of God : severity toward those who have fallen , but God’s kindness to you , provided you continue in his kindness . Otherwise you too will be cut off .
- **Rom 2:4** (✓) *target: kindness*
  > Rom 2:4 Or do you presume on the riches of his kindness and forbearance and patience , not knowing that God’s kindness is meant to lead you to repentance ?
- **Eph 2:7** (✓) *target: kindness*
  > Eph 2:7 so that in the coming ages he might show the immeasurable riches of his grace in kindness toward us in Christ Jesus .

**Group `886-002`** (4 verses — anchors: Gal 5:22)

- **Gal 5:22** 🔵 (✓) *target: kindness*
  > Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,
- **Rom 3:12** (✓) *target: good*
  > Rom 3:12 All have turned aside ; together they have become worthless ; no one does good , not even one .”
  - notes: Negation register — quotes Ps 14:3 LXX universal-depravity catena. Term names chrēstotēs by absence in the fallen inner being; retained in 886-002 as the human-side characteristic engaged through negation. See VCB-013 obslog DF-001 / Session B flag SBF-VCB013-001.
- **2Cor 6:6** (✓) *target: kindness*
  > 2Cor 6:6 by purity , knowledge , patience , kindness , the Holy Spirit , genuine love ;
- **Col 3:12** (✓) *target: kindness*
  > Col 3:12 Put on then , as God’s chosen ones , holy and beloved , compassionate hearts , kindness , humility , meekness , and patience ,

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**No legacy-VC terms.** All OWNER terms in this registry are `vc_status='vc_completed'` — classifications were performed under v3_x contracts.

---

## L. Stage 2b Foundational Input — Observation Question Catalogue

**Total questions: 206**, grouped into 10 sections. The section grouping is the Stage 2b chapter structure — Stage 2b works through the catalogue section-by-section, producing answers grouped by section.

### Section summary

| Section | n questions |
|---|---:|
| Compassion Extensions | 8 |
| Evidence-Flag Research Questions | 12 |
| Forgiveness Extensions | 14 |
| Love Extensions | 14 |
| Mercy Extensions | 11 |
| Section 1 — Word Characteristic Summary | 20 |
| Section 2 — Word Impact Description | 21 |
| Section 3 — Annotated Verse Evidence | 44 |
| Section 4 — Original Language Vocabulary | 36 |
| Section 5 — Connections and Research Pointers | 26 |

### Full catalogue (JSON, grouped by section)

Format: JSON. Structure: as-is from `wa_obs_question_catalogue`. Section grouping provides the chapter structure Stage 2b uses.

```json
{
  "total": 206,
  "section_count": 10,
  "sections": {
    "Compassion Extensions": [
      {
        "obs_id": 187,
        "question_code": "C-001",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Does the evidence for the word include a significant cluster of prohibition contexts — and if so, what does the frequency of the word's prohibition reveal about its default status in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 188,
        "question_code": "C-002",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Does any verse depict the word winning an inner contest with a competing disposition — and if so, what does this reveal about the word's relationship to other inner-being characteristics that it must overcome?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 189,
        "question_code": "C-003",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Does the evidence assign the word an explicitly everlasting or permanent temporal character — in direct contrast to the momentary character of a competing or opposing disposition?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 190,
        "question_code": "C-004",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Is the word's abstract meaning etymologically derived from a concrete somatic reality — and if so, what does this unusual etymological direction reveal about the relationship between the inner experience and its bodily ground?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 191,
        "question_code": "C-005",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Does the word have a participatory dimension — does it operate as genuine entry into another's experience rather than response from a safe distance — and if so, does this participation carry an eschatological trajectory?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 192,
        "question_code": "C-006",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Does any verse name the violation of the word by the very person who most characteristically bears it — and if so, what does this reveal about the word's resilience or fragility under external pressure?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 193,
        "question_code": "C-007",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Has the word acquired a standardised or institutionalised social form — a normative outward expression that names what the characteristic looks like when it is embodied in social practice?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 194,
        "question_code": "C-008",
        "section": "Compassion Extensions",
        "source_word": "Compassion",
        "source_registry_no": 23,
        "question_text": "Does the word identify a specific category of person who needs it but cannot perceive their own need — and what conditions produce the failure of need-recognition?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Evidence-Flag Research Questions": [
      {
        "obs_id": 195,
        "question_code": "Q-COV-01",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Is this term's meaning covered by another term with similar meaning in the inner-being scope?",
        "pattern_type": "VERSE_EVIDENCE_MINIMAL",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 196,
        "question_code": "Q-COV-02",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Is this term a modern concept / neologism with no substantive biblical antecedent?",
        "pattern_type": "VERSE_EVIDENCE_MINIMAL",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 197,
        "question_code": "Q-COV-03",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Does the absence of biblical evidence itself have analytical significance for the inner-being picture?",
        "pattern_type": "VERSE_EVIDENCE_MINIMAL",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 198,
        "question_code": "Q-COV-04",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Is this term simply not relevant to inner-being study? If so, should the term be deprecated from this registry?",
        "pattern_type": "VERSE_EVIDENCE_MINIMAL",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 199,
        "question_code": "Q-COV-05",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Was STEP's verse capture exhausted for this term? Was any pagination or filter step incomplete?",
        "pattern_type": "VERSE_EVIDENCE_CONCENTRATED",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 200,
        "question_code": "Q-COV-06",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "What do the few verses that exist establish about the term's inner-being contribution?",
        "pattern_type": "VERSE_EVIDENCE_CONCENTRATED",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 201,
        "question_code": "Q-COV-07",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Does the narrow verse set concentrate in a particular literary genre, historical period, or speaker?",
        "pattern_type": "VERSE_EVIDENCE_CONCENTRATED",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 202,
        "question_code": "Q-COV-08",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "VERSE_EVIDENCE_HIGH indicates that many verses in the Bible carry the same evidential value. Does the surrounding context of the verse provide any further differential value?",
        "pattern_type": "VERSE_EVIDENCE_HIGH",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 203,
        "question_code": "Q-COV-09",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Does the high frequency repeat itself in both Old and New Testament? Is there any analytic value in this finding?",
        "pattern_type": "VERSE_EVIDENCE_HIGH",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 204,
        "question_code": "Q-COV-10",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Does the high frequency correlate to the term's importance for understanding the inner being?",
        "pattern_type": "VERSE_EVIDENCE_HIGH",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 205,
        "question_code": "Q-COV-11",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "The term's usage in the verse has multiple analytic coverages - does the context around the verse impact the meaning so as to let us understand the different nuances better?",
        "pattern_type": "VERSE_EVIDENCE_BREADTH_NOTE",
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 206,
        "question_code": "Q-COV-12",
        "section": "Evidence-Flag Research Questions",
        "source_word": null,
        "source_registry_no": null,
        "question_text": "Has the breadth been captured in the inter-relationships and correlations with other terms and words?",
        "pattern_type": "VERSE_EVIDENCE_BREADTH_NOTE",
        "scope": "universal",
        "status": "active"
      }
    ],
    "Forgiveness Extensions": [
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
    ],
    "Love Extensions": [
      {
        "obs_id": 162,
        "question_code": "L-001",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word hold a foundational position relative to other inner-being characteristics — does it govern, generate, or organise them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 163,
        "question_code": "L-002",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Where the word has distinct modes of operation, are those modes held simultaneously or do they operate sequentially?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 164,
        "question_code": "L-003",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word have an inherent directionality — is it always oriented toward an object — and what does the choice of object determine about the word's moral character?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 165,
        "question_code": "L-004",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Can the word function as an identity diagnostic — does what a person does with this word reveal what kind of person they are?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 166,
        "question_code": "L-005",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word operate at a level below conscious attention or deliberate will — and if so, what does this imply about its depth in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 167,
        "question_code": "L-006",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the vocabulary of the word include a systematic taxonomy of its own misdirected forms — and if so, what structural logic organises that taxonomy?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 168,
        "question_code": "L-007",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Can the word increase or grow in the inner being — and if so, by what means?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 169,
        "question_code": "L-008",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word have a definitional outward expression — a form that constitutes what the word is rather than merely evidencing it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 170,
        "question_code": "L-009",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Is the word named in Scripture as constitutive of the divine essence — what God is — rather than merely as a divine attribute or act?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 171,
        "question_code": "L-010",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word's structural opposite operate under the same moral logic as the word itself — can the contrary also be either rightly or wrongly directed?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 172,
        "question_code": "L-011",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "What is the relationship between the word as an inner disposition and the word as an outward act — are they competitors, co-expressions, or in a different structural relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 173,
        "question_code": "L-012",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word carry an epistemic dimension — is knowing and being known a structural component of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 174,
        "question_code": "L-013",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word function as a publicly legible signal — a means by which something about the inner community or person is read by those outside?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 175,
        "question_code": "L-014",
        "section": "Love Extensions",
        "source_word": "Love",
        "source_registry_no": 103,
        "question_text": "Does the word produce a reorganisation of social dynamics — and if so, in what direction does it reorganise them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Mercy Extensions": [
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
    ]
  }
}
```

---

## M. Readiness Verification

- **Generated at:** `2026-04-26T18:57:10Z`
- **Schema version:** `3.16.1`
- **OWNER term md_versions present:** `[2]`

**Stage 1 quick checks:**

- Registry status fields populated: ✓
- OWNER term inventory non-empty: ✓
- All OWNER terms have at least 1 verse: ✓
- Researcher fields preserved: absent — researcher narrative not yet written

**Notes / concerns:**
- session_b_status='Verse Context Reset' — investigate whether this is current or stale post-VCB-13.
- dim_review_status NULL — dimensional analysis in §F will be limited to dimensions actually populated in `wa_dimension_index` for individual groups.

---

*End of readiness output v2 — wa-067-goodness.*