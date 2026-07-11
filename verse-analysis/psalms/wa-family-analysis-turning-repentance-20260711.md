# Family analysis — `turning-repentance` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__turning-repentance.json` only. Scope strictly that one file. Counts declared: 12 meanings · 14 instances · 14 passages (verified: instance total 2+2+1+1+1+1+1+1+1+1+1+1 = 14). All genre `poetic/wisdom`; every `is_passage_anchor` = false (no span in the family sits on a passage anchor).

Instance roster (span · ref · lemma · read-sense · cluster):
- 283158 · Psa 78:34 · H7725 · repent/turn (shuv) · M45
- 283588 · Psa 7:12 · H7725 · the wicked will not repent · M45
- 271951 · Psa 119:59 · H7725 · turn (shuv) · M45
- 272090 · Psa 119:79 · H7725 · turn (shuv) · M45
- 271002 · Psa 116:7 · H7725 · return (shuv) · M45
- 273449 · Psa 139:18 · H6974 · awake (qits) still with God · cluster null
- 280116 · Psa 55:19 · H2487 · change (chaliphah — they do not change) · M45
- 279906 · Psa 53:3 · H5472 · fall away (sug) · cluster null
- 271226 · Psa 119:102 · H5493 · turn aside (sur, negated) · M30
- 272552 · Psa 125:5 · H5186 · turn aside (natah) · cluster null
- 283738 · Psa 80:18 · H5472 · turn back (sug, negated) · cluster null
- 284237 · Psa 85:8 · H7725 · turn back (shuv) · M45
- 276583 · Psa 30:11 · H2015 · you turned my mourning into dancing (haphak) · cluster null / all_candidates T2
- 283330 · Psa 78:57 · H5472 · turn away/back (sug) · cluster null

---

## 0. Data-integrity screen

### 0.1 D112(coupling)/D116(locus) field-swap
Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. **Two instances are transposed** (D116 holds a phrase, D112 holds a code):

- **Psa 116:7 · span 271002** — D112(coupling)=`internal:ib-state` (code), D116(locus)=`paired with the soul at rest` (phrase). **Read corrected:** D116 locus = `internal:ib-state`; D112 coupling = "paired with the soul at rest".
- **Psa 125:5 · span 272552** — D112(coupling)=`internal:ib-state` (code), D116(locus)=`paired with the evildoers led away` (phrase). **Read corrected:** D116 locus = `internal:ib-state`; D112 coupling = "paired with the evildoers led away".

The other 12 are in correct order (D116 code, D112 phrase). All locus/coupling reads below use the corrected values.

### 0.2 Self-loop "edges" vs genuine network
Every instance carries three `edges` on D105/D107/D112 that are `item_type:"flag"`, `from_span:null`, `resolution:"inferred"`, `to_span` = the span's own id — **self-loops, not network links** (e.g. Psa 78:34 · span 283158 · D105/D107/D112 all `to_span:"283158"`). These are discarded.

**Genuine `pair` edges (`resolution:"span"`, to a different span): exactly two —**
- Psa 55:19 · span 280116 · D112(coupling) → `to_span 280118` ("paired with their not fearing God").
- Psa 53:3 · span 279906 · D112(coupling) → `to_span 279908` ("paired with becoming corrupt together").

**Both target spans (280118, 279908) are NOT present in this file.** Therefore the intra-family network is **empty**: no genuine edge links two spans that both belong to this family. (Psa 53:3 · span 279906 also carries a D108 self-loop; Psa 55:19 · span 280116 a D106 self-loop — both discarded.)

### 0.3 seat(D104)/manner(D108) = "none"
- **D104 seat = "none" in 14/14** instances (flag). The interior "where" is **never** named for any turning.
- **D108 manner = "none" in 13/14.** Only Psa 53:3 · span 279906 · D108(manner) is filled ("all together, without exception", inferred).

### 0.4 Absent dimensions (across all 14)
No instance carries: **D103 source, D109 intensity, D110 specifier, D111 effect, D113 prohibition.** (D103 source is absent although it is a core dimension, not in the method's expected-absent list — flagged.) Present per instance: 101, 102, 104(=none), 105, 106, 107, 108(mostly none), 112, 114, 115, 116.

### 0.5 Cluster NULL / T2
Six of 14 cannot be typed by the term-cluster:
- **cluster null (5):** Psa 139:18 · span 273449 (H6974); Psa 53:3 · span 279906 (H5472); Psa 125:5 · span 272552 (H5186); Psa 80:18 · span 283738 (H5472); Psa 78:57 · span 283330 (H5472).
- **T2 (1):** Psa 30:11 · span 276583 (H2015) — `cluster.code`=null, `all_candidates`="T2(Supplementary)".
- Typed: **M45 Transformation = 7** (283158, 283588, 271951, 272090, 271002, 280116, 284237); **M30 Obedience = 1** (Psa 119:102 · span 271226).

Note: `is_outlier` = false on **all** 12 meanings, yet §1 shows at least one genuine semantic outlier (Psa 139:18 awake) — the file's outlier flag does not capture it.

### 0.6 Minor source inconsistencies (non-blocking)
- `passage_ref` vs `verse_refs` mismatches: passage 1621 ref "Psa 30:3-12" but verse_refs list 30:1–12; passage 1718 ref "Psa 78:29-35" but refs run to 78:36; passage 1812 ref "Psa 116:1-10" but refs to 116:11. Text is present; only the ref-label window is narrow.
- Aggregate `evidence.stems`/`morph_codes` null on several records (e.g. H6974 awak) while the instance `morphology` is filled (Psa 139:18 · span 273449 morph "HVhp1cs HSn", Hiphil). Read morphology off the instance.

---

## 1. Coherence — does "turning-repentance" fit its data?

**Partly.** The grouping is a sound *lexical* net — every span is a "turn"-type verb: shuv (H7725), sug (H5472), sur (H5493), natah (H5186), haphak (H2015), plus chaliphah (H2487, "change") and qits (H6974, "awake"). But as an **inner-being movement** the label **fuses opposite and unrelated motions**. The decisive axis the keyword collapses is **direction** (toward vs away from God) and **polarity** (turning vs refusal-to-turn). Distinct movements:

1. **Penitent / God-ward turning (5).** Psa 78:34 · span 283158 · D106(operation)="turn back", D107(target)="to God" (but D114 flags it "proved shallow"); Psa 119:59 · span 271951 · D107(target)="God's word"; Psa 116:7 · span 271002 · D114(discovery) "self-summons to peace, the soul called home"; Psa 80:18 · span 283738 (vowed fidelity, negated); Psa 85:8 · span 284237 (negated, "not turn back to folly"). Positive/protective turning.
2. **Apostasy / defection — turning *away* (3).** Psa 53:3 · span 279906 · D114 "the universal human defection from God"; Psa 78:57 · span 283330 · D114 "apostasy inherited from the fathers"; Psa 125:5 · span 272552 · D114 "veering off the straight path onto crooked byways". Negative turning.
3. **Settled impenitence / moral fixity — refusal to turn (2).** Psa 7:12 · span 283588 · D102(type)="volition", D106 "impenitence as the wicked's settled refusal"; Psa 55:19 · span 280116 · D102="status", D114 "moral fixity of the wicked … obstinacy in evil". The *absence* of turning.
4. **Perseverance / non-relapse & interpersonal turning.** Psa 119:102 · span 271226 (not turn aside from the rules); and — off the God-axis entirely — Psa 119:79 · span 272090 · D116(locus)="external:person", D106="turn to the psalmist": the God-fearers turning **to a person**, not repentance.
5. **Non-family outliers (2).**
   - **Psa 139:18 · span 273449 · D101(sense)="awake (qits) still with God"** — waking from sleep, "seamless continuity of the God-ward self across the break of sleep" (D114). This is not a turning-of-will at all; grouped only because qits glosses "to awake". Clearest mis-fit (yet `is_outlier`=false, `cluster` null).
   - **Psa 30:11 · span 276583 · D102(type)="affect"** — haphak, "you turned my mourning into dancing": a **divine reversal of the psalmist's affect** ("God turned the self's mourning … the received reversal", D106/D114), not the human's own turning. Cluster T2/null; belongs to affect-reversal, not repentance.

**Finding:** the family is a directional-verb bundle, not one movement. It holds at least four inner-being movements plus two out-of-scope spans. Any downstream synthesis must split by direction/polarity (God-ward vs away vs refusal) and must exclude the awake-continuity (273449) and divine-affect-reversal (276583) spans from a "repentance" reading.

---

## 2. The movements evidenced (cited)

### 2.1 Turning *to* God (penitence, real or hoped)
- Psa 78:34 · span 283158 · D101 "repent/turn (shuv)", D102="action", D106="turn back", D107="to God", D112(coupling)="paired with the seeking", D116(locus)=external:god. D114: turning-back that "proved shallow" (v37) — a movement the data itself qualifies as unstable.
- Psa 119:59 · span 271951 · D101 "turn (shuv)", D106="turn the feet", D107="God's word", D114 "reflection that redirects the feet to the word" — turning driven by self-examination ("when I think on my ways").
- Psa 116:7 · span 271002 · D101 "return (shuv)", D106="return", D107="his soul to rest"; corrected D116 locus=internal:ib-state, D112 coupling="paired with the soul at rest". D114 "self-summons to peace, the soul called home to quiet after deliverance" — the only turning addressed by the self *to* the self (soul).
- Psa 80:18 · span 283738 · D101 "turn back (sug, negated)", D102="disposition", D106="not turn away", D107="from God", D112="paired with calling on his name" — vowed non-defection, conditional on restoration.

### 2.2 Turning *from* God (apostasy / defection)
- Psa 53:3 · span 279906 · D101 "fall away (sug)", D106="turn back / fall away", D107="from God", D108(manner)="all together, without exception" (the **only** filled manner), D112(pair)→279908 "becoming corrupt together". D114 "universal human defection … not one seeks him".
- Psa 78:57 · span 283330 · D101 "turn away/back (sug)", D106="turn away", D107="from God", D112="paired with acting treacherously" — inherited apostasy.
- Psa 125:5 · span 272552 · D101 "turn aside (natah)", D106="turn aside", D107="to crooked ways"; corrected D116 locus=internal:ib-state, D112 coupling="paired with the evildoers led away". D114 "veering off the straight path onto crooked byways".

### 2.3 Refusal to turn (impenitence, fixity)
- Psa 7:12 · span 283588 · D101 "the wicked will not repent", D102="volition", D106 "impenitence as the wicked's settled refusal", D107(target)="impenitence", D112="refuse-to-repent", D116=internal:ib-state. D114 "the wicked's interior … read as a refusal to turn; the judgment hangs on that unrelenting inner posture."
- Psa 55:19 · span 280116 · D101 "change (chaliphah — they do not change)", D102="status", D106 "do not change / will not repent", D107="none", D112(pair)→280118 "not fearing God", D116=internal:ib-state. D114 "moral fixity … obstinacy in evil … unrepentance rooted in having no fear of God."

### 2.4 Perseverance / guarded non-relapse
- Psa 119:102 · span 271226 · D101 "turn aside (sur, negated)", D102="disposition", D106 "not turn aside from the rules", D107="God's word", cluster M30 Obedience. D114 "not swerving from the rules God himself taught."
- Psa 85:8 · span 284237 · D101 "turn back (shuv)", D102="disposition", D106 "not turn back", D107="to folly", D116=internal:ib-state. D114 "the relapse guarded against … the danger that the restored might revert."

### 2.5 Off-axis / non-repentance
- Psa 119:79 · span 272090 · D101 "turn (shuv)", D106 "turn to the psalmist", D107="the psalmist", D116(locus)=external:person. Interpersonal turning of the God-fearers toward the psalmist — not a God-ward or penitential motion.
- Psa 139:18 · span 273449 · D101 "awake (qits) still with God", D102="state", D106 "consciousness returns from sleep and finds the God-presence unbroken", D107="continuity of presence", D112="waking-still-with", D116=internal:ib-state. Continuity of consciousness, not turning.
- Psa 30:11 · span 276583 · D101 "you turned my mourning into dancing", D102="affect", D106 "God turned the self's mourning into dancing … the received reversal", D107="transformation", D112="mourning-to-dancing", D116=internal:ib-state. Divine reversal of the interior's felt state (bearer human, agent God).

---

## 3. Dimensional cross-cut

- **D102 type (14):** action 7 (283158, 271951, 272090, 271002, 279906, 272552, 283330); disposition 3 (271226, 283738, 284237); volition 1 (283588); state 1 (273449); status 1 (280116); affect 1 (276583). The turning is predominantly *acted* (action) but hardens into *disposition/volition/status* precisely where it is negated or refused — the family's grammar tracks the polarity.
- **D105 bearer (14, all `inferred`, all human):** psalmist/soul (271951, 271002, 273449, 276583, 271226), "they"/"the saints"/"we the people" (283158, 283330, 283738, 284237), "the wicked"/"enemies"/"crooked"/"all mankind" (283588, 280116, 272552, 279906), "those who fear God" (272090). Human IB confirmed throughout; no bearer stated on the surface (all inferred).
- **D107 target (13/14 filled):** God / God's word (283158, 271951, 271226, 279906, 283330, 283738), a person (272090), interior conditions — impenitence, transformation, continuity, folly, rest, crooked ways (283588, 276583, 273449, 284237, 271002, 272552). Only Psa 55:19 · span 280116 · D107="none".
- **D116 locus (corrected, 14):** internal:ib-state 7 (283588, 273449, 280116, 284237, 276583, 271002, 272552), external:god 6 (283158, 271951, 271226, 283738, 283330, 279906), external:person 1 (272090). Turning is read as roughly half an internal state, half a movement oriented on an external (chiefly God).
- **D115 role:** `characteristic` in all 14. No qualifier/standalone in the family.

---

## 4. The network

**Intra-family network = empty.** The only two genuine `pair` edges (Psa 55:19 · span 280116 · D112 → 280118; Psa 53:3 · span 279906 · D112 → 279908) both point to spans **outside this file**, so nothing links two family members. All 42 remaining edge-rows (3 per instance × 14) are D105/D107/D112 self-loops and are not links. The "web" the method looks for cannot be drawn from this source alone; the two outward couplings say only that impenitence is welded to *not-fearing-God* (280116→280118) and that falling-away is welded to *becoming-corrupt* (279906→279908) — both bindings retrievable only against spans not supplied here.

---

## 5. The interior anatomy the data actually names

- **Seat (D104):** none — 14/14. The family names **no interior organ** (no heart, soul-as-seat, ruach, eye). The one "soul" that appears is a *target/addressee* ("Return, O my soul", Psa 116:7 · span 271002 · D106/D107), not a coded seat.
- **Source (D103):** absent — 14/14. What *moves* the turning is never captured dimensionally. The nearest source-signals live only in prose D114 (self-reflection at Psa 119:59 · span 271951; "no fear of God" at Psa 55:19 · span 280116) — not derivable as D103.
- **Coupling (D112, corrected):** the interior bonds the data does name — turning⇄seeking (283158), turning⇄not-fearing-God (280116), fall-away⇄corruption (279906), turn-away⇄treachery (283330), turn-back⇄folly (284237), return⇄soul-at-rest (271002), waking⇄still-with-God (273449), mourning⇄dancing (276583). These couplings, not any seat, are the only "anatomy" present.

---

## 6. What could not be derived

- **No seat and no source anywhere** (D104 none ×14; D103 absent ×14): the family cannot say *where in the interior* turning happens or *what drives* it.
- **No intensity, specifier, effect, prohibition** (D109/D110/D111/D113 absent ×14): degree, qualification, consequence and any "do-not" framing are unavailable — even where the sense is a negated turning (Psa 85:8, 80:18, 119:102), the prohibition dimension D113 is not coded.
- **No usable network:** both genuine edges leave the file (§4); intra-family relations are not derivable here.
- **Manner blank except one** (D108 none ×13; only Psa 53:3 · span 279906).
- **Six spans un-typed** by cluster (§0.5); the T2/null spans (esp. Psa 139:18 awake · span 273449 and Psa 30:11 affect-reversal · span 276583) sit in the family only by lexical accident and should not feed a "repentance" synthesis.
- **All bearers inferred, none surfaced** (§3): identity of the turning subject rests on inference, not stated text.
- **Direction/polarity is carried only in D106/D107/D114**, not in a single dimension — so "toward vs away from God", the family's most important distinction, is not itself a coded field and must be reconstructed per instance.

---

## 7. Summary
`turning-repentance` is a lexically tidy but movement-heterogeneous bundle of 14 Psalms "turn"-verbs (M45×7, M30×1, null×5, T2×1). Corrected for the D112/D116 swap at Psa 116:7 (span 271002) and Psa 125:5 (span 272552), it resolves into **four inner-being movements — God-ward penitence, apostate turning-away, settled impenitence, and guarded perseverance — plus two out-of-scope spans** (Psa 139:18 waking-continuity · span 273449; Psa 30:11 divine affect-reversal · span 276583) and one interpersonal turn (Psa 119:79 · span 272090). The data names **no seat, no source, no intensity/effect/prohibition, and no intra-family network** (both real pair-edges exit the file); its only interior anatomy is the D112 couplings and the polarity of direction reconstructed per verse.
