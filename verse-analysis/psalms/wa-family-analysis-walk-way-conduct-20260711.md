# Family analysis — Psalms · `walk-way-conduct` (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__walk-way-conduct.json` only. Scope strictly that file. 24 meanings · 47 instances · 38 passages (meta). Every finding cited `reference · span · Dnnn(label)`. Dimension legend from the file: 101 sense · 102 type · 103 source · 104 seat · 105 bearer · 106 operation · 107 target · 108 manner · 109 intensity · 110 specifier · 111 effect · 112 coupling · 113 prohibition · 114 discovery · 115 role · 116 locus.

---

## 0. Data-integrity screen (done first)

### 0.1 D112 (coupling) / D116 (locus) field-swap
Method rule: correct order = **D116 holds a code** (`internal:`/`external:`), **D112 holds a phrase**. Where D116 holds a prose phrase and D112 holds the code, the two are transposed and must be read corrected.

**13 instances are swapped** (D112 carries the code, D116 the phrase) — read them corrected:

| # | reference · span | D112 (as stored) | D116 (as stored) | corrected coupling / locus |
|---|---|---|---|---|
| 1 | Psa 101:2 · 268819 | `internal:ib-state` | "paired with integrity of heart" | coupling = integrity of heart · locus = internal |
| 2 | Psa 101:6 · 268860 | `internal:ib-state` | "paired with being blameless" | coupling = blamelessness · locus = internal |
| 3 | Psa 116:9 · 271017 | `external:god` | "paired with the delivered soul" | coupling = delivered soul · locus = external:god |
| 4 | Psa 128:1 · 272652 | `external:god` | "paired with the fear of God" | coupling = fear of God · locus = external:god |
| 5 | Psa 138:7 · 273357 | `internal:ib-state` | "paired with God preserving his life" | coupling = God preserving life · locus = internal |
| 6 | Psa 89:15 · 307042 | `external:god` | "paired with the festal shout" | coupling = festal shout · locus = external:god |
| 7 | Psa 99:7 · 285846 | `external:god` | "paired with calling upon God" | coupling = calling on God · locus = external:god |
| 8 | Psa 95:10 · 285455 | `internal:ib-state` | "paired with not knowing God's ways" | coupling = not knowing God's ways · locus = internal |
| 9 | Psa 107:4 · 270011 | `internal:ib-state` | "paired with the fainting soul" | coupling = fainting soul · locus = internal |
| 10 | Psa 107:40 · 270022 | `internal:ib-state` | "paired with the contempt poured on them" | coupling = contempt on them · locus = internal |
| 11 | Psa 131:1 · 272865 | `internal:ib-state` | "paired with the marvelous things beyond him" | coupling = things too great · locus = internal |
| 12 | Psa 107:17 · 269898 | `internal:ib-state` | "paired with their iniquities" | coupling = their iniquities · locus = internal |
| 13 | Psa 125:3 · 272542 | `internal:ib-state` | "paired with the righteous so tempted" | coupling = tempted righteous · locus = internal |

The remaining 34 instances are stored in the correct order (D116 a code, D112 a phrase) — e.g. Psa 119:1 · 271197 · D116(locus)=`external:god`, D112(coupling)="paired within its char-arc across the psalm"; Psa 1:1 · 275344 · D116(locus)=`internal:ib-state`, D112(coupling)="walk-not". One correct-order instance leaves **D112 coupling unfilled** (`none`): Psa 68:21 · 281528 · D112(coupling)="none".

### 0.2 Self-loop "edges" are not real links
Almost every instance's `edges[]` consists of D105 bearer / D107 target / D112 coupling entries with `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span:` = **the span's own id**. These are self-loops, **not** network links (e.g. Psa 119:1 · 271197 · all three edges `to_span:"271197"`). They carry no relational information.

**Genuine `pair` edges** (`resolution:"span"`, from_span → a *different* to_span) exist on only **9 of 47 instances**:

- Psa 56:13 · 280259 · D112(coupling) → 280251
- Psa 58:3 (go astray) · 280487 · D108(manner) → 280491 · D112(coupling) → 280484
- Psa 53:3 · 279908 · D112(coupling) → 279886
- Psa 76:11 · 282796 · D107(target) → 282799 · D112(coupling) → 282790
- Psa 58:3 (estranged) · 280484 · D108(manner) → 280486 · D112(coupling) → 280487
- Psa 68:21 · 281528 · D103(source) → 281521
- Psa 55:2 · 280122 · D108(manner) → 280124 · D112(coupling) → 280125
- Psa 55:20 · 280126 · D107(target) → 280128 · D112(coupling) → 280130
- Psa 56:8 · 280316 · D112(coupling) → 280318

Only **one genuine edge is intra-family** (both ends in this file): Psa 58:3 · 280484(estranged) → 280487(go astray) on D112, reciprocated by 280487 → 280484. Every other genuine edge points to a span **not present in this file** (another word in the same verse), so the network is not resolvable within-source.

### 0.3 seat (D104) / manner (D108) = "none"
- **D104 seat = "none" for all 47 instances.** The interior organ is never localised anywhere in the family.
- **D108 manner = "none" for 40 of 47.** Filled on only 7: Psa 56:13 · 280259 ("in the light of life"); Psa 58:3 · 280487 ("from birth, speaking lies"); Psa 53:3 · 279908 ("together, as one"); Psa 58:3 · 280484 ("from the womb, from birth"); Psa 76:11 · 282796 ("as homage, with gifts"); Psa 55:2 · 280122 ("in his complaint"); Psa 56:8 · 280316 ("counted by God").

### 0.4 Absent dimensions
Across **all 47 instances**, these never appear in any `lexical[]` ledger:
- **D109 intensity** — absent (no gradation captured).
- **D110 specifier** — absent.
- **D111 effect** — absent (no downstream effect captured).
- **D113 prohibition** — absent.
- **D103 source** — present on **one** instance only: Psa 68:21 · 281528 · D103(source)="whose head God strikes (v21)".

### 0.5 Cluster NULL / T2
The family's own core verb is **untyped by the term-cluster**:
- **Null cluster, `T2(Supplementary)` candidate only:** `H1980:walk` (all 19), `H1980:occupy` (Psa 131:1 · 272865), `H7300:restless` (Psa 55:2 · 280122). = **21 instances**.
- **Null cluster, null candidates:** `bring`, `estranged`, `flee`, `follow`, `run`, `slipped`, `stands`, `stretch out`, `stretched`, `tossings` = **10 instances**.
- **M30 (Obedience):** `kept` (3), `go astray`/`wander`/`wandered`/`astray`×2/`stray`/`went astray` (10) = **13 instances**.
- **M10 (Sin):** `become corrupt`, `guilty ways`, `sinful ways` = **3 instances**.

So **31 of 47 (66%) carry no real M-cluster**, including the whole `halak` "walk" core (40% of the family). Only 16/47 are cluster-typed.

---

## 1. Coherence — does the label fit its data?

**Partly. The label fits a ~35/47 core; ~12/47 are keyword-fused intruders.**

**Genuine `walk-way-conduct` core (~35):**
- **Walking the way / conduct-as-path (25):** `halak` walk (19), `shamar` kept-the-way (Psa 119:4 · 271827; Psa 18:21 · 274987; Psa 99:7 · 285846), `ruts` run in the way (Psa 119:32 · 302604), `amad` stands-not (Psa 1:1 · 275348), `mot` feet-held-fast/not-slipped (Psa 17:5 · 306042). These are one coherent movement: conduct pictured as a course walked, mostly in God's ways/law/faithfulness/integrity (Psa 26:1 · 276111 · D114 "walked in my INTEGRITY … a consistent, undivided manner of life"; Psa 119:1 · 271197 · D114 "the blessed who walk in the law").
- **Deviation — the negative pole of the same path (10, all M30):** `taah`/`shagah`/`shagag` wander / go astray / stray (Psa 119:10 · 271205; 119:21 · 271724; 119:118 · 271320; 119:176 · 271692; 119:110 · 271284; 119:67 · 272000; 58:3 · 280487; 95:10 · 285455; 107:4 · 270011; 107:40 · 270022). Straying-from-the-path is the exact antonym of walking-the-path; coheres tightly (Psa 119:176 · 271692 · D114 "gone ASTRAY like a lost sheep").

**Keyword-fused intruders (~12) — distinct movements the grouping has swept in:**
- **Moral-status corruption, grouped by the "way(s)" gloss (4):** `alach` become corrupt (Psa 53:3 · 279908 · D102 status), `zur` estranged-from-the-womb (Psa 58:3 · 280484 · D102 status), `asham` guilty ways (Psa 68:21 · 281528 · D102 status), `pesha` sinful ways (Psa 107:17 · 269898 · D102 disposition). These are states/status of depravity, not locomotion; "ways" is the surface hook.
- **Inner agitation / restlessness (2):** `rud` restless (Psa 55:2 · 280122 · D102 status · D114 "the churning that cannot settle"), `nod` tossings (Psa 56:8 · 280316 · D102 status · D114 "the sleepless, restless wandering of grief"). Roaming metaphor, but the movement is emotional turmoil, not conduct.
- **Hand-reaching acts (2):** `shalach` stretch out the hands to do wrong (Psa 125:3 · 272542), stretched out his hand against friends (Psa 55:20 · 280126 · D116 corrected locus=`external:person`). Gesture of wrongdoing/betrayal, not way-walking.
- **Flight (1):** `barach` flee God's presence (Psa 139:7 · 308070 · D114 "the tested urge to get away … omnipresence forecloses flight"). Locomotion but the vector is escape.
- **Pursuit / homage (2):** `radaph` goodness-and-mercy follow/pursue me (Psa 23:6 · 275854 · D102 affect), `yabal` bring/present tribute (Psa 76:11 · 282796 · lexical_gloss "to conduct" — a literal keyword collision). Neither is the human IB walking a way.

**First-class finding:** the fusion is driven by lexical-gloss/keyword overlap ("way/ways", "conduct", "wander/roam"), not by shared inner-being motion. The two poles that genuinely belong (walk-the-way + stray-from-the-way) are strongly coherent and mutually defining; the corruption-status, agitation, hand-reach, flight and homage senses are separable and should be read as their own movements.

---

## 2. The movements / operations evidenced

### 2.1 Walking the way (halak, 19 — the family's heart)
The dominant operation is D106="walk" (event) with a target (D107) that is almost always God or his revelation:
- **Toward God / his word:** Psa 119:1 · 271197 · D107="God's word"; Psa 119:3 · 271775 · D107="God's word"; Psa 128:1 · 272652 · D107="in God's ways"; Psa 86:11 · 284256 · D107="in God's truth"; Psa 89:15 · 307042 · D107="in the light of God's face"; Psa 89:30 · 284677 · D106="fail to walk" · D107="in God's rules" (negated disobedience); Psa 81:13 · 306922 · D107="in God's ways"; Psa 116:9 · 271017 · D107="before the LORD"; Psa 84:11 · 284064 · D107="before God"; Psa 56:13 · 280259 · D107="before God, in the light of life".
- **In integrity / one's own uprightness:** Psa 101:2 · 268819 · D107="with integrity of heart" · D114 "integrity not merely pondered but practised at home"; Psa 101:6 · 268860 · D107="in the blameless way"; Psa 26:1 · 276111 · D102 volition · D107="integrity-of-life"; Psa 26:11 · 276124 · D114 "the future pledge, the interior committing to keep its course"; Psa 26:3 · 276147 · D107="God-oriented-walk"; Psa 15:2 · 274617 · D102 volition · D114 "the life itself is the first qualification".
- **Through affliction (preservation-in-passage):** Psa 138:7 · 273357 · D114 "not spared trouble but kept alive through it"; Psa 119:45 · 271856 · D114 "walking freely in the wide place the word gives".

Type (D102) splits `halak` between **action** (11) and **volition** (Psa 1:1, 15:2, 26:1/11/3) — the same verb read as bare conduct or as a willed commitment.

### 2.2 Refusal as the first act of conduct (Psa 1:1)
The passage-anchor Psa 1:1 stages conduct as a graded set of refusals: Psa 1:1 · 275344 (walks) · D106="the first refusal … declining the casual first association" · D107="refusal-1" · D114 "the mildest, most casual involvement … already refused; the interior sets its first boundary"; deepened by Psa 1:1 · 275348 (stands) · D106="the second, deeper refusal … declining to settle among them" · D107="refusal-2" · D114 "standing is more settled than walking; the refusal deepens from passing-by to taking-a-position." Two spans in one verse trace an escalation of withdrawal.

### 2.3 Keeping / holding the course (shamar, mot)
- Psa 18:21 · 274987 · D106="kept God's ways and not wickedly departed … sustained fidelity" · D107="fidelity".
- Psa 99:7 · 285846 · D106="keep" · D107="God's testimonies" · bearer="the intercessors".
- Psa 119:4 · 271827 · D106="keep / observe" · the psalm's premise ("the charge to keep").
- Psa 17:5 · 306042 · D106="steps have held fast … feet have not slipped" · D107="steadfast-walk" · D114 "kept its footing on God's tracks".

### 2.4 Straying from the path (M30 — the negative pole)
- Deliberate/dispositional straying refused: Psa 119:10 · 271205 · D106="not wander"; Psa 119:110 · 271284 · D106="not stray … though snared".
- Straying enacted by the wicked/proud: Psa 119:21 · 271724 · bearer="the insolent"; Psa 119:118 · 271320 · bearer="the strayers"; Psa 58:3 · 280487 · D106="go astray / wander" · D108(manner) pair → "from birth, speaking lies"; Psa 95:10 · 285455 · D102 disposition · D107="in heart" · "the wandering heart of the wilderness generation".
- Straying as lost-state: Psa 107:4 · 270011 · D102 state · "homeless in the wilderness"; Psa 107:40 · 270022 · "the princes … made to wander like the lost"; Psa 119:176 · 271692 · "gone astray like a lost sheep"; Psa 119:67 · 272000 · D106="go astray" corrected by affliction.

### 2.5 Corruption / estrangement of the inner being (M10 + zur)
- Psa 53:3 · 279908 · D106="become corrupt / go sour" · D108="together, as one" · D114 "the whole turned rancid … corporate rottenness, none exempt"; genuine edge D112 → 279886 ("restates the corruption of v1, shachat").
- Psa 58:3 · 280484 · D106="be estranged / go one's own way" · D108 pair → "from the womb" · D114 "innate estrangement … depravity as old as they are"; genuine edge D112 → 280487 (reciprocal with go-astray).
- Psa 68:21 · 281528 · D103(source) pair → 281521 ("whose head God strikes") · D106="walk / persist in guilt".
- Psa 107:17 · 269898 · D106="walk in sinful ways" · D107="against God".

### 2.6 Agitation, flight, reaching, pursuit, homage (the intruder movements)
- Psa 55:2 · 280122 · D106="be restless / wander in agitation" · D108 pair → "in his complaint" · D112 pair → "moaning aloud".
- Psa 56:8 · 280316 · D106="toss / wander restlessly" · D108="counted by God" · D112 pair → "the tears God keeps" · D114 "God has numbered every turn."
- Psa 139:7 · 308070 · D106="the impulse to escape God's presence … finds no exit" · D107="inescapable presence".
- Psa 125:3 · 272542 · D106="reach toward wrong" · D114 "oppression drawn out until even the upright reach for wrongdoing."
- Psa 55:20 · 280126 · D106="stretch out the hand (in violence)" · D107 pair → "against those at peace with him" · D112 pair → "violating his covenant."
- Psa 23:6 · 275854 · D102 affect · D106="goodness and mercy will pursue it … chased by good, not evil."
- Psa 76:11 · 282796 · D106="bring / present tribute" · D107 pair → "to him who is to be feared" · homage.

---

## 3. The network (genuine pair edges only)

Self-loops excluded (see §0.2). Genuine relational structure is thin and mostly points outside the file:

- **Only intra-family edge:** Psa 58:3 · 280484 (estranged) ↔ 280487 (go astray) on **D112 coupling**, reciprocated both directions — within one verse the depravity-status "estranged from the womb" and the act "go astray from birth" are welded. This is the single link resolvable inside the source.
- **Edges to spans outside this file** (other words in the same verse; not resolvable here): 56:13 · 280259 → 280251 (D112, "the soul's deliverance"); 58:3 · 280487 → 280491 (D108, "speaking lies"); 53:3 · 279908 → 279886 (D112, prior corruption); 76:11 · 282796 → 282799 (D107 target) & → 282790 (D112, the vows); 68:21 · 281528 → 281521 (D103 source, God's strike); 55:2 · 280122 → 280124 (D108) & → 280125 (D112, moaning); 55:20 · 280126 → 280128 (D107) & → 280130 (D112, covenant); 56:8 · 280316 → 280318 (D112, tears).

**Verdict:** as a within-family network the data is effectively a single isolated pair plus 38 unconnected nodes. The "cross-verse" relational life of these terms lives in spans this file does not contain, so it cannot be described from this source.

---

## 4. The interior anatomy the data actually names

- **Seat: never.** D104 = "none" on all 47 — the family localises nothing in a named organ (heart, soul, ruach, eye). Where the interior is evoked it is carried by the **target/locus**, not a seat: "integrity of heart" (Psa 101:2 · 268819, in D107); "in heart" (Psa 95:10 · 285455 · D107); the delivered/fainting soul (corrected coupling of Psa 116:9 · 271017, Psa 107:4 · 270011); feet/steps (Psa 17:5 · 306042; Psa 56:13 · 280259). These are the interior the data gestures at, but formally as targets/couplings, never as D104 seats.
- **Locus (D116, corrected):** the family divides between **internal:ib-state** (self-referential conduct/integrity/corruption — Psa 1:1, 15:2, 17:5, 18:21, 26:1/3/11, 53:3, 55:2, 56:8, 58:3, 95:10, 101:2/6, 107:4/17/40, 116:9, 125:3, 131:1, 138:7, 139:7) and **external:god** (conduct oriented toward God/his word — Psa 76:11, 81:13, 84:11, 86:11, 89:15/30, 99:7, 119:*, 128:1, 56:13). One **external:person** (Psa 55:20 · 280126, the betrayer's hand).
- **Bearer (D105): all inferred, all human.** Individual (the psalmist/David — majority; the blessed man Psa 1:1 · 275344; the God-fearer Psa 128:1 · 272652; the betrayer Psa 55:20 · 280126) and corporate (the people Psa 89:15 · 307042; Israel Psa 81:13 · 306922; David's children Psa 89:30 · 284677; the wicked Psa 58:3 · 280487; the insolent Psa 119:21 · 271724; the fools Psa 107:17 · 269898; that generation Psa 95:10 · 285455; the princes Psa 107:40 · 270022; all mankind Psa 53:3 · 279908; the intercessors Psa 99:7 · 285846). No God-as-bearer — Screen 0 clean, with one caveat (§5).
- **Role (D115): uniformly "characteristic"** on all 47 — no qualifier or standalone is used, even where a D114 note calls a term "the qualifier" (Psa 68:21 · 281528 · D114 "…meeting God's strike (the qualifier)" yet D115="characteristic").

---

## 5. What could not be derived (flagged)

- **No seat anywhere** (D104 all "none") — the family cannot say *where* in the interior walking/straying is seated.
- **Four dimensions wholly absent** (D109 intensity, D110 specifier, D111 effect, D113 prohibition) — no gradation, specifier, downstream effect, or prohibition is recoverable; D103 source appears once only (Psa 68:21 · 281528).
- **Manner mostly empty** (40/47 D108="none").
- **Two-thirds untyped** (31/47 null cluster; the entire 19-strong `halak` core is `T2(Supplementary)` only) — the term-cluster cannot type the family's own defining verb.
- **13-instance D112/D116 swap** — coupling/locus are unusable until corrected (§0.1).
- **Network unrecoverable in-file** — genuine edges are 9 instances, all but one pointing to spans absent from this source; only the Psa 58:3 estranged↔go-astray pair (280484↔280487) resolves here.
- **Label fusion** — ~12/47 senses (corruption-status, agitation, hand-reach, flight, homage) are keyword/gloss intrusions, not walk-way-conduct movements (§1).
- **Screen 0 caveat, one instance:** Psa 23:6 · 275854 (follow) — bearer is the psalmist but the operating agents are "goodness and mercy" (God's attributes pursuing him); the movement is the human's *assurance* (D102 affect), not a human walking. Read as an affect *about* God's action, not a conduct-of-the-IB.
- **Bearers all inferred** — no bearer is surface-explicit via a possessive on a named seat; ownership of each inner movement is a read, not a datum.

---

## Summary
`walk-way-conduct` is anchored by a strong, coherent bipolar core — **walking the way** (halak/shamar/ruts/amad/mot, 25) and its exact antonym **straying from the way** (taah/shagah/shagag, 10, M30) — into which the keyword grouping has fused ~12 unrelated movements (corruption-status, restlessness, hand-reach, flight, homage). The interior is never seated (D104 all "none"); it is evoked only through targets/loci (integrity, heart, soul, feet) oriented `internal:ib-state` or `external:god`. Four dimensions are absent, two-thirds of instances are untyped (the whole halak core is T2-only), 13 instances need the D112/D116 swap corrected, and the relational network collapses to self-loops plus a single intra-family pair (Psa 58:3 estranged↔go-astray). All 47 bearers are inferred human IBs; all roles are "characteristic".
