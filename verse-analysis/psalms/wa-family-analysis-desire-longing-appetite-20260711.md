# Family analysis — `desire-longing-appetite` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__desire-longing-appetite.json` only. Scope `meta.scope.family = "desire-longing-appetite"`. Counts: **49 meanings · 80 instances · 55 passages**. Every claim is cited `reference · span_id · Dnnn(label)`. Nothing outside this file.

---

## 0. Data-integrity screen (done first)

### 0.1 Dimension presence across the 80 instances
Present on all 80: D101 sense, D102 type, D104 seat, D105 bearer, D106 operation, D107 target, D108 manner, D112 coupling, D114 discovery, D115 role, D116 locus.

- **D103 source — present on only 2/80.** Filled only at `Psa 68:30 · span 281602 · D103(source)` ("whom God rebukes and scatters") and `Psa 57:3 · span 280385 · D103(source)` ("whom God will put to shame"). For the other 78 instances, what *triggers* the desire is not derivable.
- **Entirely absent across all 80:** **D109 intensity, D110 specifier, D111 effect, D113 prohibition.** No instance carries any of them. The file cannot speak to how strong a desire is, what qualifies it, what it produces, or whether it is prohibited.

### 0.2 D112(coupling)/D116(locus) field-swap — 20 instances transposed
Correct order = D116 holds the code (`internal:`/`external:`), D112 holds the prose phrase. **60/80 are correctly ordered; 20/80 are swapped** (code sits in D112, phrase in D116). Read these 20 corrected:

| reference · span | true locus (from D112) | true coupling phrase (from D116) |
|---|---|---|
| Psa 104:34 · 269332 | external:god | paired with the meditation |
| Psa 105:22 · 269436 | internal:ib-state | paired with his affliction and his teaching |
| Psa 106:14 · 269609 | internal:ib-state | paired with the craving and the testing |
| Psa 106:14 · 269610 | internal:ib-state | paired with the wanton desire |
| Psa 106:16 · 269622 | internal:ib-state | paired with the earth swallowing the rebels |
| Psa 107:5 · 270043 | internal:ib-state | paired with thirst and the fainting soul |
| Psa 107:5 · 270044 | internal:ib-state | paired with hunger |
| Psa 107:9 · 270067 | internal:ib-state | paired with the soul satisfied |
| Psa 107:9 · 270069 | internal:ib-state | paired with the hungry soul filled |
| Psa 107:30 · 269973 | internal:ib-state | paired with the gladness |
| Psa 107:36 · 307527 | internal:ib-state | paired with being settled in a city |
| Psa 109:5 · 270328 | internal:ib-state | paired with the evil returned |
| Psa 109:9 · 307549 | internal:ib-state | paired with the widow and the curse |
| Psa 109:17 · 270207 | internal:ib-state | paired with loving to curse |
| Psa 111:2 · 270588 | external:god | paired with studying them |
| Psa 112:1 · 270650 | external:god | paired with the fear of the LORD |
| Psa 112:10 · 270659 | internal:ib-state | paired with the wicked's melting away |
| Psa 125:4 · 272548 | internal:ib-state | paired with the upright in heart |
| Psa 133:1 · 272995 | internal:ib-state | paired with the pleasantness of unity |
| Psa 133:1 · 272996 | internal:ib-state | paired with the goodness of unity |

Corrected locus totals across all 80: **internal:ib-state 57 · external:god 21 · external:person 2** (`Psa 45:11 · span 278893 · D116` and `Psa 55:11 · span 280041 · D116`). Desire in this family sits overwhelmingly as an internal IB state; where it points outward it points to God (21) far more than to another person (2).

### 0.3 Self-loop "edges" are not network links
**215 flag/inferred self-loop edges** (`item_type:"flag"`, `resolution:"inferred"`, `to_span` = own span). By dimension: D105 bearer 77, D107 target 70, D112 coupling 62, D108 manner 6. These carry **no** network information and are excluded. Only **31 genuine `pair` edges** (`resolution:"span"`, linking to a different span) are real — used in §5.

### 0.4 seat / manner mostly unfilled
- **D104 seat = "none" on 79/80.** The sole filled seat: `Psa 63:1 · span 281016 · D104(seat)` = "the soul".
- **D108 manner = "none" on 71/80.** Nine filled (see §4.4).

### 0.5 Cluster typing
- **19/80 instances have `cluster.code = null`** — the term-cluster cannot type them (14 meanings: hungry H7457, "long" H3615/H2968/H8264, fatherless H3490, feast-on H7301, fly-away H5774, lines H2256, open H6473, pants H6165, pleasant H5273, straight H3474, thirsty H6771, want H2637). Several are keyword/homograph artefacts (§1).
- **T2 cluster: 0 instances.** No qualifier-only typing.

### 0.6 Role
**D115 role = "characteristic" on all 80.** No qualifier, no standalone. Every instance is asserted as a characteristic of the inner being.

### 0.7 Bearer / IB screen
All 80 bearers are human (`Screen 0` passes — God never the bearer; God appears only as locus/coupling object). Dominant bearer `the psalmist` (33). Three are span-resolved ("my soul" ×2, "the psalmist (his soul)" ×1: `Psa 42:2 · span 278535 · D105(bearer)`, `Psa 63:1 · span 281016 · D105(bearer)`); the rest are `inferred`. Bearers include the disordered as well as the godly — e.g. `Psa 73:3 · span 282483 · D105(bearer)` "they/the wicked", `Psa 106:14 · span 269609 · D105(bearer)` "the fathers", `Psa 52:2 · span 279807 · D105(bearer)` the tyrant.

---

## 1. Coherence — does the family label fit its data? (first-class finding)

**No — the keyword grouping fuses several distinct inner-being movements.** D101 sense holds **64 distinct values** across 80 instances; the eight cluster codes span Joy, Envy, Desire, Hope, Anger, Constitution, Blessing and NULL. The strands actually present:

1. **Delight / pleasure in God and his law** (M04 Joy, 14 meanings — the largest strand). e.g. `Psa 1:2 · D106(operation)` "delight is in the law", `Psa 37:4 · D106(operation)` "delight yourself in the LORD, who will give the desires of the heart". This is *joy fixed on the good*, not raw appetite.
2. **Craving / lust — disordered appetite** (M28 Envy: taavah, avah, havvah). `Psa 106:14 · span 269610 · D106(operation)` "have a wanton craving"; `Psa 78:18 · span 283056` craved food; `Psa 5:9`/`52:2` havvah "destruction / engulfing greed" (`span 279807`).
3. **Thirst / hunger / panting for God — bodily-figured longing** (M29 Desire + null: tsame, raeb, arag). `Psa 42:1 · span 278508 · D106(operation)` "pant / long" (deer simile); `Psa 63:1 · span 281016` "my soul thirsts"; `Psa 107:5 · span 270043` hungry. This is the "appetite" strand proper.
4. **Envy / jealousy / zeal — rivalrous affect** (M02 Anger crossover, all `is_outlier`). `Psa 73:3 · span 282483 · D106(operation)` "be envious"; `Psa 69:9 · span 281902` "be consumed with zeal"; `Psa 106:16 · span 269622` "jealous". A different movement (rivalry), correctly flagged outlier.
5. **Evaluative "good" (tob, H2896, 8 instances)** — the *object* valued/craved, not itself a desire. `Psa 16:2 · span 274694 · D106(operation)` "no good apart from you"; `Psa 4:6 · span 305977` "who will show us some good?".
6. **Null-cluster keyword/homograph artefacts** — desire imputed by the English rendering, not the Hebrew sense: `Psa 119:81 · D101` "long / fail" is **kalah "to end / fail / be consumed"** (H3615, gloss "to end: finish/destroy/expend"); `Psa 16:6 · span 274730` "lines" (chebel, "a pleasant lot"); `Psa 5:8 · span 280744` "straight" (yashar); `Psa 23:1 · span 275809` "I shall not want" (chaser, lack); `Psa 55:6 · span 306384` "fly away" (uph). These do not evidence "desire" at all and should be treated as grouping noise.

**Conclusion:** the label is a loose English-keyword superset over at least six movements — (a) delight/pleasure, (b) craving/lust, (c) thirst/hunger longing, (d) envy/jealousy/zeal, (e) evaluative "good", (f) null-cluster artefacts. The genuinely unified core is the God-directed *longing/delight* strand (1+3); envy (4), the "good" object (5), and the artefacts (6) are distinct.

---

## 2. Type anatomy (D102)

Across 80: **disposition 28 · status 15 · affect 12 · state 11 · action 8 · volition 4 · cognition 1 · faculty 1.** The family is read mainly as *disposition* (a settled leaning, e.g. delight-in) plus *status/state/affect* — not primarily as discrete acts. The lone **faculty** and lone **cognition** typings are the exceptions (e.g. the "reckon good / find best" operation at `Psa 73:28 · span 282471`). Volition (4) is where desire is read as an act of will, e.g. `Psa 105:22 · span 269436 · D102(type)` (nephesh "pleasure / will").

---

## 3. Sense (D101) and object

D101 is highly various (64 distinct). The recurring verbs of motion the data names in D106(operation): **delight/rejoice** (≈14), **long/yearn** (≈9), **crave/lust** (≈5), **thirst** (2), **pant** (3), **hunger** (3), **be envious/jealous/zealous** (3). The prose D106 operations frequently narrate the *whole movement* rather than a bare verb — e.g. `Psa 37:4 · span ... · D106(operation)` "the self is told to delight in the LORD, who will give the desires of the heart — joy in God that reshapes desire"; `Psa 19:10 · D106(operation)` "the rules of the LORD are more to be desired than much fine gold... a valuing that outbids treasure". These operation strings are the richest per-instance content in the file.

---

## 4. Where it moves — the filled dimensions

### 4.1 Locus (D116, corrected) — §0.2
Internal:ib-state 57 · external:god 21 · external:person 2. The desire is predominantly an internal state; when directed outward it is toward God.

### 4.2 Coupling (D112, corrected) — what the desire is bound to
Prose phrases in all 80 (once §0.2 corrected). Couplings bind desire to: God/his law (`Psa 112:1 · span 270650` fear of the LORD; `Psa 104:34 · span 269332` the meditation), to bodily lack (`Psa 107:5 · span 270043` thirst and fainting soul; `Psa 107:5 · span 270044` hunger), to the disordered self (`Psa 106:14 · span 269610` the wanton desire), and to social/evil states (`Psa 109:17 · span 270207` loving to curse).

### 4.3 Source (D103) — only 2/80 (§0.1). Not derivable elsewhere.

### 4.4 Manner (D108) — 9/80 filled
`Psa 42:1 · span 278508 · D108(manner)` "as a deer pants for streams (simile)"; `Psa 63:1 · span 281016 · D108(manner)` "as in a dry and weary land without water"; `Psa 73:28 · span 282471 · D108(manner)` "having made the Lord GOD his refuge"; `Psa 73:25 · span 282452 · D108(manner)` "whom have I in heaven but you?"; `Psa 73:3 · span 282483 · D108(manner)` "seeing the prosperity of the wicked"; `Psa 69:9 · span 281902 · D108(manner)` "consuming, all-devouring"; `Psa 55:6 · span 306384 · D108(manner)` "like a dove with wings"; `Psa 56:1 · span 280220 · D108(manner)` "all the day long"; `Psa 55:11 · span 280041 · D108(manner)` "in its midst". The two similes (deer, dry land) are the clearest data on *how* the longing is experienced.

### 4.5 Target (D107)
Filled on all 80 but mostly self-loop (§0.3); genuine cross-span targets appear only in the 31 pairs (§5).

---

## 5. The network — genuine `pair` edges only (31)

Sparse and almost entirely *coupling* links (binding a desire to its object across spans), plus a few target/bearer/manner/source links. Notable dyads:

- **Reciprocal pair — Psa 52:2↔52:7** (`span 279807 ↔ 279855`, both D112 coupling). The only bidirectional link: the tyrant's destructive-desire spans mutually coupled.
- **Psa 42:1–2 thirst cluster** — `span 278508 → 278509 · D105(bearer)` and `→ 278505 · D108(manner)` (deer simile); `Psa 42:2 · span 278535 → 278534 · D105(bearer)` + `D112(coupling)` ("my soul thirsts for God, the living God").
- **Psa 63:1** — `span 281016 → 281015` on both `D104(seat)` and `D105(bearer)` (the soul thirsts), plus `→ 281018 · D112(coupling)`. The only seat-bearing network node.
- **Psa 73:28** — `span 282471 → 282472 · D107(target)`, `→ 282477 · D108(manner)` + `D112(coupling)` ("good to be near God", refuge).
- **Psa 68:30** — `span 281602`: `→ 281590 · D103(source)`, `→ 281603 · D107(target)`, `→ 281600 · D112(coupling)` — the densest single node (3 outward edges).
- Others: `Psa 70:2`, `Psa 55:6`, `Psa 55:11`, `Psa 56:1`, `Psa 57:3`, `Psa 62:4`, `Psa 69:9`, `Psa 73:3`, `Psa 73:25`, `Psa 45:1`, `Psa 45:11` — each 1–3 edges, mostly D112 coupling.

**Network character:** sparse (31 real edges over 80 nodes), predominantly one-directional, dominated by D112 coupling. Only Psa 52 forms a reciprocal loop. Most desire spans are network-isolated once self-loops are removed.

---

## 6. The interior anatomy the data actually names

Assembling only *filled* interior slots:

- **Seat:** the file names an organ exactly **once** — **the soul (nephesh)** at `Psa 63:1 · span 281016 · D104(seat)`. The soul (nephesh, lemma H5315) also surfaces as the *bearer* ("my soul") at `Psa 42:2 · span 278535` and as the desire-word itself at `Psa 78:18 · span 283056` (nephesh "crave") and `Psa 105:22 · span 269436` (nephesh "pleasure / will"). **The heart** is spoken of in D106/D114 prose ("desires of the heart", `Psa 37:4`; "law within my heart") but is **never** a filled D104 seat.
- **Locus:** internal IB state (57) with God as the external pole (21) — the desire's habitat, not an organ.
- **The verbs of the interior in motion** (D106): delight, long, thirst, hunger, pant, crave, envy — the anatomy is one of *motion toward*, not of localised organs.

The file therefore names a **thin** interior anatomy: desire is almost never localised; where it is, the organ is **nephesh/the soul**, and the object is God.

---

## 7. What could not be derived (highlighted)

1. **Seat (D104)** — unstated for 79/80; the interior *location* of desire is essentially unavailable.
2. **Source (D103)** — unstated for 78/80; what *triggers* the desire is almost never given.
3. **Manner (D108)** — unstated for 71/80.
4. **Intensity (D109), Specifier (D110), Effect (D111), Prohibition (D113)** — **entirely absent** (0/80). The file cannot say how strong a desire is, what qualifies it, what it produces, or whether it is forbidden — even for the lust/craving strand where a prohibition reading would be expected (a possible **miss** per the revelation-test intuition, but not assertable from this file).
5. **Cluster typing** — 19/80 instances are `cluster.code = null`; the term-cluster cannot type them.
6. **D112/D116 transposition** — 20/80 must be corrected (§0.2) before any locus/coupling reading.
7. **215 self-loop edges** carry no relational information; the true network is only 31 edges.
8. **Keyword/homograph artefacts** — kalah "fail/be consumed" (`Psa 119:81/82/123`), chebel "lines/lot" (`Psa 16:6`), yashar "straight" (`Psa 5:8`), chaser "want/lack" (`Psa 23:1`), uph "fly away" (`Psa 55:6`): "desire" is imputed by the English rendering, not the Hebrew sense. These are not evidence of the family's movement.

---

## 8. Summary

The `desire-longing-appetite` base source (49 meanings / 80 instances / 55 passages) is a **loose English-keyword grouping that fuses at least six distinct inner-being movements** — God-directed delight/pleasure (M04, largest), disordered craving/lust (M28), bodily-figured thirst/hunger longing for God (M29 + null), rivalrous envy/jealousy/zeal (M02 outliers), the evaluative object "good" (tob), and null-cluster homograph artefacts — rather than one coherent movement. Every instance is typed `characteristic`; desire is read chiefly as *disposition/affect*, held as an *internal IB state* pointing to *God*. The data is **rich on operation (D106) and coupling (D112) but silent on seat, source, manner and — entirely — on intensity, specifier, effect and prohibition**; the interior is localised to an organ only once (nephesh/the soul, Psa 63:1). Before use: correct the 20 D112/D116 swaps, drop the 215 self-loops (true network = 31 sparse, mostly one-directional coupling edges), and treat the 19 null-cluster + homograph items as grouping noise.
