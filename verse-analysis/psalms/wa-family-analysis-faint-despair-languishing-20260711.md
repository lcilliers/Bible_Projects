# Family analysis — `faint-despair-languishing` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__faint-despair-languishing.json` (only). Provenance: ib_characteristic v3 (meaning-keyed) + family grouping v1 + term-based cluster v2. Counts in `meta`: **33 meanings · 55 instances · 39 passages**. All 33 meanings and 55 instances are accounted for below. Every finding cites `reference · span · Dnnn(label)`. Genre of every instance = `poetic/wisdom`.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap — WIDESPREAD (19 of 55)
Correct order = D116 locus holds a code (`internal:`/`external:`), D112 coupling holds a phrase. **19 instances are transposed** (D112 holds the `internal:ib-state` code; D116 holds a `paired with …` prose phrase) and must be read corrected:

| # | reference · span |
|---|---|
| 1 | Psa 116:10 · 270930 · D112(coupling)=`internal:ib-state` / D116(locus)=`paired with believing` |
| 2 | Psa 94:5 · 285418 · D116=`paired with crushing the people` |
| 3 | Psa 107:10 · 269869 · D116=`paired with rebelling against God` |
| 4 | Psa 102:1 · 268890 (afflicted) · D116=`paired with being faint` |
| 5 | Psa 102:1 · 268892 (faint) · D116=`paired with being afflicted` |
| 6 | Psa 107:5 · 270046 · D116=`paired with the soul` |
| 7 | Psa 129:1 · 272688 · D116=`paired with the affliction not prevailing` |
| 8 | Psa 129:2 · 272695 · D116=`paired with the foes not prevailing` |
| 9 | Psa 116:3 · 270983 (anguish) · D116=`paired with the suffering` |
| 10 | Psa 116:6 · 271000 · D116=`paired with being saved` |
| 11 | Psa 132:1 · 272893 · D116=`paired with his vow to house the ark` |
| 12 | Psa 105:18 · 269408 · D116=`paired with his exaltation…` |
| 13 | Psa 116:3 · 270981 (laid hold) · D116=`paired with the anguish` |
| 14 | Psa 107:26 · 269955 · D116=`paired with the courage` |
| 15 | Psa 112:10 · 270658 · D116=`paired with the anger and gnashing` |
| 16 | Psa 129:2 · 272700 (prevail) · D116=`paired with the long affliction` |
| 17 | Psa 107:17 · 269900 · D116=`paired with the iniquities` |
| 18 | Psa 102:11 · 307200 · D116=`paired with the evening-shadow days` |
| 19 | Psa 102:4 · 302592 · D116=`paired with the struck-down heart` |

Corrected reading of these 19: locus = `internal:ib-state`; coupling = the `paired with …` phrase. The remaining 36 instances are already in correct order (D112 = phrase, D116 = code). **No `external:` locus corrections arise except the single genuine `external:god` at Psa 63:1 · 281018 · D116(locus), which is correctly ordered.**

### 0.2 Self-loop "edges" are non-edges
Every instance carries D105(bearer) — and usually D107(target) and D112(coupling) — as `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span:<its own span id>`. These are **self-loops, not network links** and are excluded from the network (§ "The network"). Example: Psa 116:10 · 270930 · D105(bearer)/D107(target)/D112(coupling) all `to_span:270930`.

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = none in 51 of 55.** Seat is filled in only 4: Psa 61:2 · 280866 · D104(seat)=`the heart`; Psa 77:3 · 282964 · D104(seat)=`the spirit (ruach)`; Psa 55:4 · 280182 · D104(seat)=`the heart`; Psa 63:1 · 281018 · D104(seat)=`the flesh`.
- **D108 manner = none in 48 of 55.** Filled in 7: Psa 69:29 · 281812 · D108=`in pain`; Psa 77:3 · 282964 · D108=`under the burden of grief`; Psa 48:6 · 279234 · D108=`as of a woman in labour`; Psa 69:3 · 281817 · D108=`with crying out, throat parched`; Psa 55:5 · 280192 · D108=`overwhelming, covering`; Psa 48:5 · 279229 · D108=`they took to flight`; Psa 77:4 · 306738 · D108=`so much that speech fails`.

### 0.4 Absent dimensions (across ALL 55 instances)
- **D109 intensity — absent everywhere.**
- **D110 specifier — absent everywhere.**
- **D111 effect — absent everywhere.**
- **D113 prohibition — absent everywhere.**
- **D103 source — near-absent: present in only 2 instances** (Psa 44:24 · 278788 · D103(source)=`unrelieved while God hides his face…`; Psa 69:29 · 281812 · D103(source)=`whom God's salvation sets on high`). The other 53 carry no D103 at all.

So the standard filled dimensions per instance are only D101, D102, D104, D105, D106, D107, D108, D112, D114, D115, D116. Intensity/specifier/effect/prohibition give the family no gradation, no effect-tracing and no proscription data.

### 0.5 Cluster NULL / T2 (term-cluster cannot type them) — 12 of 55
- **Fully NULL cluster (8 instances / 8 meanings):** Psa 79:8 · 283544 (brought); Psa 116:6 · 271000 (brought low); Psa 116:3 · 270981 (laid hold); Psa 107:26 · 269955 (melt); Psa 119:28 · 271759 (melts away, dalaph); Psa 77:4 · 306738 (troubled); Psa 102:11 · 307200 (wither away); Psa 102:4 · 302592 (withered).
- **T2(Supplementary) — code null (4 instances / 3 meanings):** Psa 129:1 · 272688 & Psa 129:2 · 272695 (afflicted, tsarar); Psa 84:2 · 284075 (faints, kalah); Psa 112:10 · 270658 (melts away, masas). Per project rule, T2 = reference/qualifier, not a standalone characteristic-cluster.

### 0.6 Other integrity notes
- **Psa 116:3 · 270981 · `esv_word`=null** (hebrew_surface `suffered`; meaning-label `laid hold`; read `suffer (matsa)`) — label/ESV mismatch.
- **Lemma H6031 (anah) is heavily multivalent** — it generates 4 distinct meaning-keys in this family: afflict (7), endured (1), hurt (1), suffered affliction (1). Likewise H0926 (bahal) → dismay (3) + panic (1); H3001 (yabesh) → wither away (1) + withered (1); H1809 (dalal) → brought (1) + brought low (1).

---

## 1. Coherence check — does the label fit its data? (FUSED — first-class finding)

The label **`faint-despair-languishing`** expects cluster **M24(Weakness)**, and M24 is genuinely dominant (**30 of 55 instances**). But the keyword grouping has **fused at least three distinct inner-being movements plus three cross-cluster collisions**. The English keywords (faint / afflicted / anguish / melts away / dismayed) collect Hebrew terms that move very differently:

- **A. Somatic depletion / weakness — M24 (30 instances) — the coherent core.** The ebbing of vital strength, felt in the body: faint (`ataph` Psa 102:1 · 268892; Psa 107:5 · 270046; Psa 61:2 · 280866; Psa 77:3 · 282964), languish (`amal` Psa 6:2 · 281933), grow dim (`daab` Psa 88:9 · 284512), be weary (`yaga` Psa 69:3 · 281817; Psa 6:6 · 281962), despair/be sick (`anash` Psa 69:20 · 281772), afflicted (`anah`/`ani`/`oni`, 18 instances), brought low (`dalal` Psa 116:6 · 271000).
- **B. Grief / pain — M03 (5 instances) — adjacent but distinct.** anguish (`yagon` Psa 116:3 · 270983; `matsoq` Psa 119:143 · 271479; `chil` Psa 48:6 · 279234; `chul` Psa 55:4 · 280182) and pain (`keeb` Psa 69:29 · 281813). Sorrow, not depletion.
- **C. Terror / panic — M01 (5 instances) — a different movement, and mostly borne by ENEMIES.** dismayed (`bahal` Psa 30:7 · 276638; Psa 83:17 · 283975; Psa 90:7 · 285044), horror (`pallatsuth` Psa 55:5 · 280192), panic (`bahal` Psa 48:5 · 279229).
- **D. Longing-faint — M29(Desire), OUTLIER (1).** Psa 63:1 · 281018 · D101(sense)=`faint / long (kamah - my flesh faints for you)`, D116(locus)=`external:god`. This is a faint of *yearning toward God*, opposite valence to collapse; flagged `is_outlier:true` with `outlier_note` (expected M24, got M29).
- **E. Resilience / prevail — M23(Strength), OUTLIER (1).** Psa 129:2 · 272700 · D101=`prevail (yakol, negated)` — the enemies' *failure* to overcome; `is_outlier:true` (expected M24, got M23). Semantically the opposite of weakness.
- **F. Bearing terrors — M19(Trust), OUTLIER (1).** Psa 88:15 · 284443 · D101=`suffer (nasa)`; `is_outlier:true` (expected M24, got M19).

**Sharpest fusion: the English "faint" alone spans three unrelated Hebrew movements** — collapse (`ataph`, M24; `kalah` "be spent", T2 Psa 84:2 · 284075), longing (`kamah`, M29 Psa 63:1 · 281018), and finishing/being-spent (`kalah`). A second fusion: **agent-affliction vs patient-weakness.** Several "afflict" instances are transitive *actions by the wicked/enemies*, not an inner faint-state: Psa 94:5 · 285418 · D102(type)=`action`, D105(bearer)=`the wicked`, D106(operation)=`afflict` (God's heritage); Psa 129:1-2 · 272688/272695 (`tsarar`, enemies afflicting Israel). These are D102=action/state done *to* the IB, grouped with the sufferer's own D102=state.

**Verdict:** the core (M24 depletion) is coherent, but the family as delivered is a keyword net, not one movement. It braids weakness (A), grief (B) and terror (C), and snags three genuine cross-cluster outliers (D/E/F) plus 12 untypeable (NULL/T2) instances (§0.5). Read strictly, this file describes **the collapse of the inner being under pressure — its depletion, grief and dread — plus a minority counter-current of longing and resilience that the keyword shares by homograph.**

---

## 2. The movements / operations evidenced (grouped, cited)

### 2.1 Affliction — the family's spine (18 instances, 3 Hebrew roots)
`anah` (H6031/H6040/H6041) dominates. It appears as **owned inner state** and as **God's/enemies' dealing**:
- Owned by the psalmist as state: Psa 116:10 · 270930 · D101=`afflicted (anah)`, D114(discovery) "the depth of the suffering the psalmist confessed even as he believed"; Psa 119:107 · 271254; Psa 119:67 · 271998 (D114: affliction "that turned him from straying to keeping"); Psa 119:71 · 272034 (D114: affliction "owned as good, the teacher of the statutes"); Psa 119:75 · 272065 (D114: "received as God's faithful dealing"); Psa 119:50 · 271895; Psa 119:92 · 272186; Psa 119:153 · 271537.
- As low estate pleaded before God: Psa 102:1 · 268890 · D102(type)=`status` (anchor of passage 1769); Psa 25:16 · 276002 · D101=`lonely and afflicted, be gracious`; Psa 88:15 · 284439 · D114 "a lifetime of suffering… affliction as the sufferer's whole history"; Psa 9:13 · 285897 · D101=`see my affliction`.
- As the community's misery: Psa 44:24 · 278788 · D102=`status`, D103(source)=`unrelieved while God hides his face and forgets` (one of only two D103s).
- As an ethical class ("the afflicted"): Psa 82:3 · 283903 · D105(bearer)=`the afflicted`, D106=`suffer oppression`.
- As **self-affliction / costly devotion** (a distinct affect): Psa 35:13 · 277330 · D102(type)=`affect`, D106(operation)="when the enemies were sick, the self wore sackcloth, afflicted itself with fasting, and prayed"; Psa 132:1 · 272893 (David "endured", `anah`, for God's house).
- As **sin's consequence**: Psa 107:17 · 269900 · D114 "the sickness endured as sin's consequence"; Psa 107:10 · 269869 (prisoners in affliction).
- As **enemy action against the IB** (agent, not patient): Psa 94:5 · 285418 · D102=`action`, D105=`the wicked`; Psa 129:1-2 · 272688/272695 (`tsarar`, T2).
- Physical affliction of a person: Psa 105:18 · 269408 · D105(bearer)=`Joseph`, "his feet were hurt with fetters".

### 2.2 Fainting / being spent (7 instances)
- Collapse under affliction: Psa 102:1 · 268892 · D101=`faint (ataph)` (passage anchor), D114 "the swooning weakness from which the lament pours"; Psa 107:5 · 270046 · D105=`the wanderers`, "their soul fainted within them".
- Seated collapse (rare seat data): Psa 61:2 · 280866 · D104(seat)=`the heart`, D101=`be faint / overwhelmed (ataph)`; Psa 77:3 · 282964 · D104(seat)=`the spirit (ruach)`, D108(manner)=`under the burden of grief`.
- Longing-faint (outlier): Psa 63:1 · 281018 · D104(seat)=`the flesh`, D107(target)=`God`, M29.
- Being spent (T2): Psa 84:2 · 284075 · D101=`faint (kalah)`, "the self spent in yearning for God".

### 2.3 Grief / anguish / pain (6 instances)
Psa 116:3 · 270983 · D101=`anguish (yagon)`, "snared by death and Sheol"; Psa 119:143 · 271479 · `matsoq`, "anguish overtaken, yet delight unshaken"; Psa 48:6 · 279234 · `chil`, D108=`as of a woman in labour`, D105=`the kings`; Psa 55:4 · 280182 · `chul`, D104(seat)=`the heart`, D116(locus)=`internal:heart` (the one non-`ib-state` internal locus); Psa 69:29 · 281813 · `keeb` pain; Psa 116:3 · 270981 · `matsa` "suffer".

### 2.4 Melting / withering / dimming — dissolution of vitality (6 instances)
Psa 107:26 · 269955 · D101=`melt (mug)`, D105=`the sailors`, "the dissolving of… nerve"; Psa 112:10 · 270658 · `masas`, D105=`the wicked man`, "dissolving in impotent frustration"; Psa 119:28 · 271759 · `dalaph`, "My soul melts away for sorrow"; Psa 88:9 · 284512 · `daab`, "my eye grows dim through sorrow"; Psa 102:11 · 307200 · `yabesh` "wither away like grass"; Psa 102:4 · 302592 · `yabesh`, D107(target)=`in heart`, "the drying-up of the heart".

### 2.5 Terror / dismay / panic / horror (5 instances)
Psa 30:7 · 276638 · D101=`you hid your face; I was dismayed`, D106 "the terror that exposed the complacency"; Psa 83:17 · 283975 · D105=`the enemies`; Psa 90:7 · 285044 · D105=`we (mankind)`, "by your wrath we are dismayed"; Psa 55:5 · 280192 · `pallatsuth` horror, D108=`overwhelming, covering`; Psa 48:5 · 279229 · `bahal` panic, D102=`action`, D108=`they took to flight`.

### 2.6 Weariness, being brought low, troubled, despair (remaining M24/NULL)
Psa 69:3 · 281817 · `yaga` weary (passage anchor), D108=`with crying out, throat parched`; Psa 6:6 · 281962 · weary with moaning; Psa 79:8 · 283544 · `dalal` "brought very low" (D105=`we (the people)`); Psa 116:6 · 271000 · brought low, "low estate met by salvation"; Psa 77:4 · 306738 · `paam` "so troubled that I cannot speak", D108=`so much that speech fails`; Psa 69:20 · 281772 · `anash` despair, "the nadir of the psalm, before the turn to praise"; Psa 6:2 · 281933 · `amal` languishing, "the trouble has gone to the bones".

### 2.7 Counter-currents (outliers, §1 D/E/F)
Longing (Psa 63:1 · 281018, M29); resilience — enemies fail to prevail (Psa 129:2 · 272700, M23, D106=`fail to prevail`); bearing God's terrors (Psa 88:15 · 284443, M19).

### D102(type) distribution
`state` (majority), `status` (Psa 102:1 · 268890; Psa 69:29 · 281812; Psa 88:15 · 284439; Psa 48:6 · 279234; Psa 55:4 · 280182; Psa 55:5 · 280192; Psa 69:3 · 281817; Psa 69:20 · 281772; Psa 63:1 · 281018; Psa 61:2 · 280866; Psa 82:3 · 283903; Psa 69:29 · 281813), `affect` (Psa 35:13 · 277330), `action` (Psa 94:5 · 285418; Psa 48:5 · 279229; Psa 88:15 · 284443). Type is the only sense-gradation available (D109/D110 absent, §0.4).

---

## 3. The network (genuine `pair` edges only)

Per §0.2, all D105-bearer / most D107-target / many D112-coupling flag edges are self-loops and are discarded. The genuine `pair` edges (`resolution:"span"`, to a **different** span) are:

| reference · from_span | on_dim | → to_span | note |
|---|---|---|---|
| Psa 44:24 · 278788 | D103 source | → 278785 | affliction bound to God hiding his face |
| Psa 69:29 · 281812 (afflicted) | D103 source | → 281814 | to God's salvation |
| Psa 69:29 · 281812 | D108 manner | → 281813 (pain) | **intra-family** |
| Psa 69:29 · 281812 | D112 coupling | → 281813 (pain) | **intra-family** |
| Psa 69:29 · 281813 (pain) | D112 coupling | → 281812 (afflicted) | **intra-family, reciprocal** |
| Psa 61:2 · 280866 | D104 seat / D112 coupling | → 280865 | faint ↔ the heart |
| Psa 77:3 · 282964 | D104 seat / D112 coupling | → 282963 | faint ↔ the spirit (ruach) |
| Psa 69:3 · 281817 | D108 manner / D112 coupling | → 281818 | weary ↔ the crying/parched throat |
| Psa 48:6 · 279234 | D112 coupling | → 279231 | anguish ↔ trembling |
| Psa 55:4 · 280182 | D104 seat | → 280181 | anguish ↔ the heart |
| Psa 55:4 · 280182 | D112 coupling | → 280184 | anguish ↔ terrors of death |
| Psa 69:20 · 281772 | D112 coupling | → 281771 | despair ↔ broken heart |
| Psa 63:1 · 281018 | D104 seat / D105 bearer | → 281017 | faint ↔ the flesh |
| Psa 63:1 · 281018 | D112 coupling | → 281016 | faint ↔ the soul's thirst |
| Psa 55:5 · 280192 | D112 coupling | → 280189 | horror ↔ fear-and-trembling climax |
| Psa 48:5 · 279229 | D112 coupling | → 279228 | panic ↔ being astounded |
| Psa 77:4 · 306738 | D108 manner → 306740 · D112 coupling → 306734 | | troubled ↔ mute speech / sleepless eyes |

**Network shape:** sparse and almost entirely **outward-facing**. The `to_span` targets (280865, 282963, 281818, 279231, 280181/280184, 281771, 281017/281016, 280189, 279228, 306740/306734, 278785, 281814) are seat/coupling partner words in the *same verse* that are **not themselves family meanings** — so they cannot be resolved within this file. **The only genuine intra-family link is Psa 69:29 · 281812(afflicted) ↔ 281813(pain)**, reciprocal on D112 coupling (plus D108 manner one-way). The family therefore has effectively **no internal web** — it is a set of parallel single-verse pairings anchoring collapse-terms to a body-seat (heart/spirit/flesh) or to a companion affect (trembling, terror, thirst), with directionality absent (`direction:null` on every edge).

---

## 4. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seats named (D104, 4 only):** the heart (Psa 61:2 · 280866; Psa 55:4 · 280182), the spirit/ruach (Psa 77:3 · 282964), the flesh (Psa 63:1 · 281018). The heart and the ruach are the organs that "faint"; the flesh is where longing is felt. 51/55 leave the interior unlocated.
- **Sources named (D103, 2 only):** God's hidden face / forgetting (Psa 44:24 · 278788) and God's salvation (Psa 69:29 · 281812). Both locate the *cause/resolution* of affliction in God's action — but this is asserted for only 2 of 55.
- **Couplings/loci (corrected, §0.1):** with the swap fixed, D116 locus is `internal:ib-state` for 53 instances, `internal:heart` for Psa 55:4 · 280182, `external:god` for Psa 63:1 · 281018. The couplings (D112 phrases) tie each collapse-term to its verse-companion: affliction↔believing (Psa 116:10), faint↔affliction (Psa 102:1), languishing↔bones (Psa 6:2 · 281933), wither↔struck-down heart (Psa 102:4 · 302592), melt↔courage (Psa 107:26 · 269955). Corporeal register recurs: bones (Psa 6:2), throat/eyes (Psa 69:3), eye (Psa 88:9), grass/withering (Psa 102:4, 102:11).

**Bearers (D105):** predominantly the psalmist, but the family also assigns inner collapse to **the nation/Israel** (Psa 44:24 · 278788; Psa 79:8 · 283544; Psa 129:1-2 · 272688/272695), **the wicked/enemies/hostile kings** (Psa 94:5 · 285418 wicked; Psa 112:10 · 270658 wicked man; Psa 83:17 · 283975 enemies; Psa 48:5-6 · 279229/279234 kings; Psa 90:7 · 285044 mankind), **named individuals** (Joseph Psa 105:18 · 269408; David Psa 132:1 · 272893), and **classes** (afflicted/destitute Psa 82:3 · 283903; prisoners Psa 107:10 · 269869; fools Psa 107:17 · 269900; wanderers Psa 107:5 · 270046; sailors Psa 107:26 · 269955; pilgrim Psa 84:2 · 284075). All are human IB (no instance makes the state God's own attribute), but the movement is not one subject's — it spans sufferer and adversary alike, and for the adversary the "collapse" (panic, melting, dismay) is narrated as *desired judgment*, not lament.

---

## 5. What could not be derived (from this source)

1. **No intensity, specifier, effect or prohibition** anywhere (D109/D110/D111/D113 absent, §0.4) — the family carries no strength-gradation, no downstream-effect tracing, no proscriptive data.
2. **Source (D103) undetermined for 53/55** — for almost every collapse the file does not say what moves it; causation is inferable only from D114 discovery prose and passage text, not from a filled D103.
3. **Interior location undetermined for 51/55** (D104 seat = none, §0.3) — the "inner being" is mostly unlocated; only heart/spirit/flesh are ever named.
4. **12 instances are un-typeable by term-cluster** (8 NULL + 4 T2, §0.5) — melt/wither/troubled/brought/laid-hold have no cluster identity in this source, so their movement-membership rests on the read alone.
5. **The network cannot be built inside the family** (§3) — every genuine edge but one points to a non-family span; direction is null throughout. Cross-verse movement is not derivable here.
6. **The family label over-collects** (§1) — weakness, grief, terror, longing, resilience and trust-bearing are braided by keyword; three are explicitly flagged outliers, the rest emerge only on reading. A single-movement description of this file would misrepresent the data.
7. **One label/ESV integrity gap** (Psa 116:3 · 270981, esv_word null; §0.6).

---

## Summary

`faint-despair-languishing` = **33 meanings / 55 instances / 39 passages**, all poetic/wisdom. Its coherent core is **M24 depletion (30/55)** — affliction (`anah`, 18×), fainting, languishing, melting, withering, weariness — the inner being emptied of vital strength and felt in bones/heart/spirit/flesh. But the delivered family is a **keyword net, not one movement**: it fuses grief (M03, 5×) and terror (M01, 5×, largely borne by enemies), and snags three genuine cross-cluster outliers (longing M29 · resilience M23 · bearing-terrors M19) plus 12 un-typeable NULL/T2 instances. Data limits are severe: **D109/D110/D111/D113 wholly absent; D103 source in 2/55; D104 seat in 4/55; a 19-of-55 D112/D116 swap; and a network with only one genuine intra-family edge** (Psa 69:29 afflicted↔pain). Everything above is cited to this file only; nothing imported.
