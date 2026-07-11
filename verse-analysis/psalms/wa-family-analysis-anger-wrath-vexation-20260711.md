# Family analysis — `anger-wrath-vexation` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__anger-wrath-vexation.json` only. 14 meanings · 15 instances · 14 passages. Every claim cited `reference · span_id · Dnnn(label)`. British spelling. Nothing imported from outside this file.

Instance roster (span · ref · sense · cluster):
- 272488 · Psa 124:3 · anger (aph) · null/T2
- 280178 · Psa 55:3 · anger (aph, grudge) · null/T2
- 277585 · Psa 37:1 · fret not / be not envious · M02(Anger)
- 283337 · Psa 78:58 · provoke to anger (kaas) · M02(Anger)
- 269716 · Psa 106:32 · anger (qatsaph) · M02(Anger)
- 270654 · Psa 112:10 · angry (kaas) · M02(Anger)
- 279448 · Psa 4:4 · be angry and do not sin · **M01(Fear) — outlier**
- 280604 · Psa 59:3 · fierce/strong men (az) · **M23(Strength) — outlier**
- 269694 · Psa 106:29 · provoke (kaas) · M02(Anger)
- 283216 · Psa 78:41 · provoke / pain (tavah) · **M03(Grief) — outlier**
- 276492 · Psa 2:1 · nations rage · null
- 271913 · Psa 119:53 · seize / hot indignation (achaz) · null
- 280492 · Psa 58:4 · venom / poison-wrath (chemah) · M02(Anger)
- 273364 · Psa 138:7 · wrath (aph) · null/T2
- 282784 · Psa 76:10 · wrath / fury (chemah, wrath of man) · M02(Anger)

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap
Correct order = D116 holds an `internal:`/`external:` **code**, D112 holds a **phrase**. Five instances are **transposed** (D112 holds the code, D116 holds a prose phrase) — read them corrected:

| span | reference | D112(coupling) as stored | D116(locus) as stored | corrected |
|---|---|---|---|---|
| 272488 | Psa 124:3 | `internal:ib-state` | "paired with the swallowing alive" | locus=`internal:ib-state`; coupling="paired with the swallowing alive" |
| 269716 | Psa 106:32 | `external:god` | "paired with Moses' embittered spirit" | locus=`external:god`; coupling="paired with Moses' embittered spirit" |
| 270654 | Psa 112:10 | `internal:ib-state` | "paired with gnashing and melting" | locus=`internal:ib-state`; coupling="paired with gnashing and melting" |
| 269694 | Psa 106:29 | `external:god` | "paired with the plague and Phinehas' intervention" | locus=`external:god`; coupling="paired with the plague and Phinehas' intervention" |
| 273364 | Psa 138:7 | `internal:ib-state` | "paired with God's delivering hand" | locus=`internal:ib-state`; coupling="paired with God's delivering hand" |

The remaining 10 instances carry the correct order (D116 = code, D112 = phrase/token) and need no correction — e.g. `Psa 78:58 · span 283337 · D116(locus)=external:god` + `D112(coupling)="paired with moving him to jealousy by idols"`. All locus/coupling readings below use the **corrected** values.

### 0.2 Self-loop "edges" are not real links
Almost every `edges[]` entry is a self-loop: `from_span:null`, `to_span` = the span's own id, `item_type:"flag"`, `resolution:"inferred"` (on D105 bearer, D107 target, D112 coupling, D108 manner). These are **not** network links and are excluded from the network below. Only `pair`/`event` edges with `resolution:"span"` pointing to a **different** span are genuine — there are **5** such edges from **4** spans:
- `Psa 55:3 · span 280178 · D112(coupling)` → 280179
- `Psa 59:3 · span 280604 · D112(coupling)` → 280605
- `Psa 58:4 · span 280492 · D112(coupling)` → 280502
- `Psa 76:10 · span 282784 · D106(operation)` → 282786 **and** `D112(coupling)` → 282786

Every genuine target span (280179, 280605, 280502, 282786) lies **outside** this file's 15 masters — so there is **no within-family internal link at all** (see §The network).

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in 15/15 instances** — no instance names an interior seat (heart/soul/ruach/eye). The interior anatomy is never located anywhere in this family.
- **D108 manner = "none" in 13/15.** Manner is filled only at `Psa 58:4 · span 280492 · D108(manner)="like the venom of a serpent, a deaf adder"` and `Psa 76:10 · span 282784 · D108(manner)="even hostile rage made to serve God's glory"`.

### 0.4 Absent dimensions (across all 15 instances)
Never present in any ledger: **D103 source**, **D109 intensity**, **D110 specifier**, **D111 effect**, **D113 prohibition**. So what *moves* the anger (D103), how *strong* it is (D109), what it *does downstream* (D111) and whether it is *forbidden* (D113) are nowhere coded — even where the verse text plainly invites them (e.g. "be angry and do not sin", Psa 4:4, reads as a prohibition but D113 is empty).

### 0.5 Cluster NULL / T2 (term-cluster cannot type the instance)
Untyped: **4 meanings / 5 instances**.
- `T2(Supplementary)`, code null: H0639:anger (`Psa 124:3 · 272488`, `Psa 55:3 · 280178`); H0639:wrath (`Psa 138:7 · 273364`). The `aph` ("nose/anger") lexeme is left as a supplementary qualifier, not a standalone cluster.
- Fully null (code + candidates null): H7283:rage (`Psa 2:1 · 276492`); H0270:seiz (`Psa 119:53 · 271913`). The term-cluster layer offers no typing for "rage" or "seize (hot indignation)".

### 0.6 Outliers (term-cluster ≠ the family's expected M02(Anger))
Three, self-declared by `is_outlier`/`outlier_note`:
- `Psa 4:4 · span 279448` → **M01(Fear)** (gloss "to tremble", ragaz).
- `Psa 59:3 · span 280604` → **M23(Strength)** (gloss "strength; strong", az).
- `Psa 78:41 · span 283216` → **M03(Grief)** (gloss "to wound", tavah).

---

## 1. Coherence — does the label fit its data?

Partly. The keyword grouping "anger-wrath-vexation" is lexically broad (`aph`, `kaas`, `qatsaph`, `chemah`, `charah`-kindled, `ragaz`, `tavah`, `ragash`-rage, `achaz`-seize, `az`), and the assembled instances **fuse at least four distinct inner-being movements**. Critically, the *bearer* is almost never the worshipping "I"; screening whose IB is in view (D105) splits the set:

**(a) Hostile fury of enemies / the wicked, aimed at the righteous — ~7 instances.**
`Psa 124:3 · 272488 · D105(bearer)=the enemies` (anger kindled to swallow alive); `Psa 55:3 · 280178 · D105=the enemies` (anger settled into grudge); `Psa 112:10 · 270654 · D105=the wicked man` (angry, gnashes, melts); `Psa 58:4 · 280492 · D105=the wicked` (venom like a serpent's); `Psa 138:7 · 273364 · D105=the enemies` (their wrath, over which God's hand stretches); `Psa 2:1 · 276492 · D105=the nations` (collective raging uproar); and the outlier `Psa 59:3 · 280604 · D105=the fierce enemies` (fierce men stir up strife). This is aggression **outward toward the psalmist** — a movement of others' interiors, not the reader's.

**(b) Human provocation that rouses God's anger — 4 instances.** Here the affect is God's; the human inner-being element is the rebellious *provoking act*. `Psa 78:58 · 283337 · D106(operation)="provoke to anger"`, D107(target)=God; `Psa 106:32 · 269716 · D107=God at Meribah`; `Psa 106:29 · 269694 · D107=the LORD by their deeds`; `Psa 78:41 · 283216 · D107=the Holy One of Israel` (outlier, M03 Grief — coded as *wounding* God, not anger). Corrected locus for two of these is `external:god` (269716, 269694; §0.1) and for 283337/283216 D116=external:god as stored — i.e. the file itself locates these *outside* the human IB.

**(c) The godly's own disciplined / zealous anger — 3 instances.** `Psa 37:1 · 277585 · D102(type)=volition` (fret not / refuse envy of the wicked's success); `Psa 4:4 · 279448 · D102=volition` (be angry and do not sin — anger permitted but fenced; outlier M01 Fear); `Psa 119:53 · 271913 · D105(bearer)=the psalmist` (hot indignation *seizes* the psalmist at the wicked's lawlessness). This is **self-governance / righteous zeal** — the opposite operational shape from (a).

**(d) Wrath of man overruled to praise — 1 instance.** `Psa 76:10 · 282784 · D106(operation)="turned to praise God"`, D105(bearer)=man/humanity — generalised human fury made to serve God's glory.

**Finding:** the label is *broadly* coherent as "anger phenomena", but it is **not one inner-being movement**. It welds outward enemy-aggression (a), rebellion-that-provokes-God (b, where the anger is not even human), self-disciplining/zealous anger of the godly (c), and a theological over-ruling of human wrath (d). Only strand (c) — plus the human *bearer* of (d) — is the reader's own inner life; the bulk describes the interiors of enemies, nations, and rebellious "fathers". The keyword sweep has fused these because they share the anger-lexeme, not because they share an operation.

---

## 2. The movements / operations evidenced (cited)

**Ignition / kindling of hostile anger.** `Psa 124:3 · 272488 · D106(operation)="have anger ignite"`, D102(type)=state, D114(discovery): "when their ANGER (aph) was kindled against us — wrath flaring to the point of swallowing its victim alive." Anger as a flaring event that consumes.

**Anger congealed into settled grudge.** `Psa 55:3 · 280178 · D102(type)=status`, D114(discovery): "aph the burning resentment out of which they cherish enmity — anger settled into grudge." D106 operation="none": the coding treats it as a *standing state* rather than an event, coupled (genuine pair, §0.2) to the grudge itself (→280179).

**Anger as innate toxicity.** `Psa 58:4 · 280492 · D102(type)=status`, D108(manner)="like the venom of a serpent, a deaf adder", D114: "chemah (heat/venom/wrath) the wicked's inner toxicity … venom joined to incorrigibility." Anger not as reaction but as constitutional poison.

**Anger visible in the body, self-consuming.** `Psa 112:10 · 270654 · D102(type)=state`, coupling (corrected)="paired with gnashing and melting", D114: "the fury of the wicked at the God-fearer's good, envy turned to rage." The angry wicked "melts away".

**Collective raging uproar.** `Psa 2:1 · 276492 · D102(type)=affect`, D106(operation)="the peoples seethe in tumultuous uproar … collective fury", D114: "the raw heat of revolt … emotion, not yet plan." The only instance typed `affect` — the massed interior as churning heat.

**Provoking / rousing another's (God's) anger.** `Psa 78:58 · 283337` and `Psa 106:29 · 269694 · D106="provoke to anger"`; `Psa 106:32 · 269716 · D106="anger / provoke"`. D102=action throughout — the movement is an *act done to* God, not an affect felt. `Psa 78:41 · 283216 · D106="provoke / wound"` recodes the same act as grief/wounding (M03).

**Disciplined / restrained anger.** `Psa 4:4 · 279448 · D106(operation)="anger is permitted but fenced — to feel it without letting it spill into sin"`, D102=volition, D107(target)="disciplined-anger". `Psa 37:1 · 277585 · D106="the self is told not to fret over evildoers … refusing the corrosive envy of the wicked's prosperity"`, D107="refusing-envy". Both are **volitional governance** of the inner heat.

**Zeal-indignation gripping the godly.** `Psa 119:53 · 271913 · D106(operation)="be seized with indignation"`, D102=state, D114: "the zeal-indignation that grips him at the wicked's lawlessness." Anger here is righteous and involuntary ("seizes me").

**Wrath over-ruled to praise.** `Psa 76:10 · 282784 · D106(operation)="turned to praise God"` (genuine event edge → 282786), D108(manner)="even hostile rage made to serve God's glory", D114: "human fury, even in its rebellion, God turns to his own honour … the residue God restrains." The one instance where anger's *outcome* is coded — and it is redemptive/overruled.

**Type (D102) distribution:** state ×5 (272488, 270654, 271913, 273364, 282784); action ×4 (283337, 269716, 269694, 283216); status ×3 (280178, 280604, 280492); volition ×2 (277585, 279448); affect ×1 (276492). So the family is read predominantly as **standing state/status** (8) and outward **action** (4), with only 2 volitional (the disciplined-anger strand) and a single affect.

---

## 3. The network (genuine edges only)

Sparse to the point of absence *within the family*. The 5 genuine span-resolution edges (§0.2) all exit the described set:
- `Psa 55:3 · 280178 · D112(coupling)` → 280179 (the cherished grudge).
- `Psa 59:3 · 280604 · D112(coupling)` → 280605 (the stirring-up of strife).
- `Psa 58:4 · 280492 · D112(coupling)` → 280502 (the wilful refusal to hear, v5).
- `Psa 76:10 · 282784 · D106(operation)` → 282786 **and** `D112(coupling)` → 282786 (the praise the wrath is made to render).

No instance links to another instance in this file; there is **no internal anger-to-anger network**. Every relational tie binds an anger-term to a *neighbouring non-anger span* (grudge, strife, refusal, praise) that is not itself part of the family. All bearer (D105) and target (D107) "edges" are self-loops and carry no network information — they merely restate the inferred bearer/target already in the ledger.

---

## 4. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seat (D104): nothing.** 15/15 "none". This family never localises anger in heart, soul, ruach, or any organ — even where verse text offers one (Psa 4:4 "ponder in your own **hearts**"; Psa 106:33 "made his **spirit** bitter" in the passage text) the seat is left uncoded.
- **Source (D103): nothing** (absent throughout, §0.4). What kindles the anger is never coded, though D114 discovery notes gesture at causes (the wicked's prosperity → envy at Psa 37:1 · 277585; idolatry → provocation at Psa 78:58 · 283337).
- **Locus (D116, corrected):** `internal:ib-state` for the enemy/wicked/psalmist affect-states (272488, 280178, 270654, 273364, 276492, 271913, 280492, 282784, 277585, 279448); `external:god` where the movement is provoking God (283337, 269716, 269694, 283216); `external:person` once (280604, the fierce men). So the anatomy that *is* named is a binary internal-state vs. external-directed split, not an organ map.
- **Coupling (D112, corrected):** anger is bound to — a grudge (280178), stirred strife (280604), refusal-to-hear (280492), rendered praise (282784), the swallowing-alive (272488), gnashing/melting (270654), Moses' embittered spirit (269716), a plague + Phinehas' intervention (269694), God's delivering hand (273364). Anger is consistently coupled to a **downstream act or consequence**, never to an interior faculty.
- **Role (D115): "characteristic" for all 15.** No instance is coded qualifier or standalone.
- **Bearer (D105): inferred for all 15**, never explicit — and mostly *not* the worshipper (enemies/wicked/nations/fathers: 11; the psalmist or the hearer/godly: 277585, 279448, 271913; man/humanity generically: 282784).

---

## 5. What could not be derived

1. **Seat of anger — never.** No interior locus anywhere (§0.3, §4). The family cannot say *where* anger sits.
2. **Source (D103), intensity (D109), specifier (D110), effect (D111), prohibition (D113) — wholly uncoded** (§0.4). Downstream effect is recoverable only at Psa 76:10 (282784) via D106, and even the plain prohibition of Psa 4:4 ("do not sin") is not captured in D113.
3. **Manner — 13/15 unstated** (§0.3); only the serpent-venom simile (280492) and the overruled-to-praise gloss (282784) are filled.
4. **Bearer always inferred, never asserted** (§4); and the human inner-being under study is present in only ~4 of 15 (the disciplined/zealous strand + generic "man"), the rest being enemies', nations', or "fathers'" interiors, or God's own provoked anger.
5. **No internal network** (§3): every genuine edge points outside the 15 masters, so the family's own anger-movements are not shown relating to one another.
6. **Cluster typing missing for 5 instances** (§0.5): "rage" (276492) and "seize/hot-indignation" (271913) have no cluster at all; the three `aph` instances (272488, 280178, 273364) are only T2-supplementary.
7. **Three outliers** (§0.6) sit in Fear (279448), Strength (280604), and Grief (283216) — i.e. the term-cluster layer disputes that ~20% of the set is "anger" at all: Psa 4:4's verb is *tremble* (ragaz), Psa 59:3's is *strength* (az), Psa 78:41's is *wound* (tavah).
8. **Five D112/D116 swaps** had to be corrected before any locus/coupling reading was trustworthy (§0.1) — an uncorrected read would have mislabelled the internal/external locus of Psa 124:3, 106:29, 106:32, 112:10, and 138:7.

---

## Summary

`anger-wrath-vexation` (Psalms) = 14 meanings / 15 instances, all role=characteristic, all seat=none, all bearer-inferred, genre poetic/wisdom. The label is only broadly coherent: it fuses **four distinct movements** — enemy/wicked hostile fury aimed at the righteous (~7), human provocation that rouses *God's* anger (4, where the affect is not human), the godly's disciplined/zealous anger (3), and human wrath overruled to praise (1). The interior is never located (D104, D103, D109–D111, D113 all empty), the network is empty within the family (5 genuine edges, all exiting the set), 5 instances are cluster-untyped and 3 are cross-cluster outliers (Fear/Strength/Grief), and 5 instances required a D112/D116 swap-correction before locus could be read.
