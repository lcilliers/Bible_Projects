# Family analysis (in isolation) — Psalms · `wickedness-ungodliness`

> Source: `outputs/data/psalms-family-base-sources/psalms__wickedness-ungodliness.json` only. Method: `verse-analysis/psalms/_family-analysis-method-20260711.md`. Scope: strictly this one file. 20 meanings · 56 instances · 42 passages. Every claim cited `reference · span · Dnnn(label)`. Absent/underivable data is flagged, not filled.

---

## 0. Data-integrity screen (done first)

**Shape.** 56 instances across 14 lemmas; genre `poetic/wisdom` for all 56; only 4 are passage anchors (`position.is_passage_anchor`). Role (D115) is uniform: **characteristic on all 56** — no qualifier, no standalone.

**D112(coupling) / D116(locus) field-swap — 18 of 56 transposed.** Correct order (per method) = D116 a code, D112 a phrase; that holds in 38 instances. In 18 the code sits in D112 and the "paired with …" prose sits in D116 — read them corrected. Swapped instances:
`Psa 101:8·268881`, `Psa 104:35·269340`, `Psa 109:2·270229`, `Psa 129:4·272713`, `Psa 92:7·285234`, `Psa 94:3·302411`, `Psa 107:34·269991`, `Psa 109:20·270243`, `Psa 109:5·270326`, `Psa 125:3·272534`, `Psa 94:21·285393`, `Psa 106:6·269838` (code `external:god`), `Psa 125:5·272557`, `Psa 94:20·285382`, `Psa 109:6·270334`, `Psa 112:10·270652`, `Psa 107:42·270035`, `Psa 94:23·285405`. (17 carry `internal:ib-state`; `Psa 106:6` carries `external:god`.) All D112/D116(locus) citations below use the corrected reading.

**Corrected locus distribution (D116).** `internal:ib-state` 49/56 · `external:person` 4 · `external:god` 3. So the data locates wickedness overwhelmingly as an inner state.

**Self-loop "edges" are not links.** Of 171 edge entries, **146 are self-loops** (`item_type:"flag"`, `resolution:"inferred"`, `to_span == own span`) on D105(bearer)/D107(target)/D112(coupling) — inferred flags, not network links. Only **25 genuine `pair` edges** (`resolution:"span"`, distinct target) exist; of these only **4 point to a span inside this family** (two reciprocal pairs: `Psa 52:1·279799↔Psa 52:3·279813`; `Psa 56:5·280297↔Psa 56:7·280307`). The other **21 point to spans not in this file** — the edge is attested but its target's identity is **not derivable within this file's scope**.

**Seat (D104) = "none" on all 56.** The interior *seat* of wickedness is never located (heart/soul/spirit never named as its seat). **Manner (D108) = "none" on 50 of 56**; only 6 filled: `Psa 58:3·280483` "from the womb / birth", `Psa 68:2·281509` "as wax melts before fire", `Psa 71:4·282187` "unjust and cruel", `Psa 73:3·282487` "prospering, at ease", `Psa 55:15·280081` "in their dwelling place, among them", `Psa 60:11·280793` "vain (shav), of man".

**Absent dimensions (across all 56).** D109(intensity), D110(specifier), D111(effect), D113(prohibition) appear on **no instance**. D103(source) appears on only **3** (`Psa 58:3·280483`, `Psa 54:5·280000`, `Psa 56:7·280307`). Dimensions present anywhere: 101,102,103,104,105,106,107,108,112,114,115,116.

**Cluster NULL / T2.** T2: none. **Cluster `null` on 15 instances** — the term-cluster cannot type them: 13× `H7451:evil` (`Psa 107:34·269991`, `Psa 109:20·270243`, `Psa 109:5·270326`, `Psa 37:27·277716`, `Psa 40:12·278245`, `Psa 50:19·279549`, `Psa 51:4·279740`, `Psa 52:1·279799`, `Psa 52:3·279813`, `Psa 54:5·280000`, `Psa 55:15·280081`, `Psa 56:5·280297`, `Psa 64:5·281128`), plus `H6466:evildoer Psa 125:5·272557` and `H3607:holdback Psa 119:101·271215`. Cluster distribution (by instance): M10(Sin) 33 · null 15 · M26(Righteousness) 2 · M27(Evil) 2 · M06(Hate) 1 · M38(Salvation) 1 · M03(Grief) 1 · M28(Envy) 1. **5 meanings flagged `is_outlier`** (see §1).

---

## 1. Coherence — does the label fit its data?

**Partly. The keyword grouping fuses at least four distinct movements, and the dominant one is not the reader's own inner being.**

**(a) The wicked-as-observed-other (dominant, ~44 instances).** Bearer (D105) is a third party in the large majority: "the wicked" ×25, "the enemies" ×5, "the evildoers" ×3, "the wicked man" ×2, "the tyrant" ×2, plus "wicked rulers", "the accusers", "the betrayers", "the fools", etc. Type (D102) is `status` on 42/56. This strand is a portrait of the *antagonist* — a settled moral status the psalmist observes, fears, and prays against (`Psa 101:8·268881·D114`: "the godless the king purges daily"; `Psa 104:35·269340·D114`: "the wicked whose end the psalmist longs for"; `Psa 139:19·273455·D102(disposition)`: "the bloodthirsty carry a settled murderous disposition the psalmist recoils from"). As inner-being data it describes *another's* interior, held at arm's length.

**(b) Penitential self-guilt (small, genuine human-IB core: 3).** Only here is the bearer the reader's own inner being carrying wickedness: `Psa 40:12·278245·D105(the psalmist)` — "iniquities have overtaken me … my heart fails" (D106 "being swamped by guilt", D102 `state`); `Psa 51:4·279740·D105(the penitent)` — "done what is evil in your sight" (self-condemnation before God); `Psa 106:6·269838·D105(we and our fathers)` — "we have done wickedness" (confession, D102 `action`).

**(c) Volitional turning-from-evil (2).** `Psa 37:27·277716·D102(volition)` — "the twofold moral turn … the interior reorients its whole direction"; `Psa 119:101·271215·D106` — "hold back my feet from evil" (restraint). Here wickedness is the *thing willed away from*, not borne.

**(d) Mis-fused strands — keyword collisions, not wickedness at all (the 5 outliers + kin).** Lexically the family swept in senses that are *suffering / revulsion / futility*, not a moral trait:
- `Psa 88:3·284473 H7451:troubl` (outlier M03 Grief) — `ra` = "troubles … the evils crowding the soul"; affliction, not the sufferer's wickedness.
- `Psa 88:8·284507 H8441:horror` — `toebah` = the sufferer "become repugnant … abandonment sharpened to revulsion"; the psalmist as object of horror, not agent of evil.
- `Psa 60:11·280793 H8668:salvation` (outlier M38 Salvation) — `teshuah` = "vain is the salvation of man"; the futility of *human help*, not wickedness (grouped only by the "vain/worthless" reading).
- `Psa 94:20·285382 H1942:wick` (outlier M28 Envy) — `havvah` "wicked rulers"; a real wicked-status but clustered under Envy.
- `Psa 94:21·285393` and `Psa 106:6·269838` `H7561` (outliers M26 Righteousness) — the *rasha* verb ("condemn", "do wickedness") landing in the Righteousness cluster.

**Verdict.** The family coheres as a *lexical field* around רשע/רע/און, but as an **inner-being movement it is not one motion**: it is chiefly the observed wicked-other (a), with a thin but real seam of the reader's own guilt/turning (b,c), and several keyword mis-fusions of suffering and futility (d). The genuine human-IB "wickedness" content is a minority of the file.

---

## 2. The movements/operations evidenced (D106, cited)

Operation (D106) is filled on all 56 but is "none" on 6 (`Psa 37:14·283602`-adjacent pure-status cases). The attested motions:

**Wickedness as settled status / being.** "be wicked" (`Psa 104:35·269340`, `Psa 109:2·270229`), "forsake the law / ensnare" ×6 (the Ps 119 wicked, e.g. `Psa 119:110·271280`, `Psa 119:119·271328`), "be destroyed" (`Psa 101:8·268881`), "perish before God" (`Psa 68:2·281509`), "sprout like grass" (`Psa 92:7·285234`), "prosper" (`Psa 73:3·282487`), "exult / triumph" (`Psa 94:3·302411`). The recurring arc: the wicked *are* a status, they *act* against the righteous, and they are *undone*.

**Wickedness gestated from within (interior generation).** `Psa 7:14·283602·D106` (D102 `cognition`): "the wicked conceives evil, is pregnant with mischief, and gives birth to lies — harm gestated from within" — the one instance reading wickedness as an *interior productive process*.

**Wickedness as disposition / bent.** `Psa 139:19·273455` "settled murderous disposition"; `Psa 107:34·269991` "be evil" (the inhabitants' evil that "turns fruitfulness to salt"); `Psa 109:20·270243` "speak evil"; `Psa 109:5·270326` "render evil".

**Wickedness done, spoken, loved, clung to (as act).** "worked"/"work / practise" (`H7489`/`H6466` evildoers), "speak evil" (`Psa 50:19·279549` "give free rein to"), "boasted in" (`Psa 52:1·279799`), "loved" (`Psa 52:3·279813`), "held fast / clung to" (`Psa 64:5·281128` "their evil purpose"), "plot / devise" (`Psa 59:5·280631`), "frame injustice" (`Psa 94:20·285382`), "rule oppressively" (`Psa 94:20`-arc). Evil here is chosen and cherished, not merely suffered.

**Guilt inundating the self.** `Psa 40:12·278245·D106`: "the interior is buried under uncountable guilt and its courage gives out" — the sole instance where wickedness moves *within the reader's own IB* to the point of collapse ("my heart fails").

**Moral turning.** `Psa 37:27·277716` "the double movement of the will: away from evil, toward good"; `Psa 119:101·271215` restraint of the feet.

**Recoil back on the sinner.** `Psa 7:16`-arc / `Psa 94:23·285405·D106` "bear wickedness" — "sin recoiling on the sinner"; `Psa 109:5`/`Psa 54:5·280000` evil returned upon the enemies.

---

## 3. The network (genuine `pair` edges only)

25 genuine edges; **21 target spans outside this file** (identity not derivable here) and **4 target inside**:
- `Psa 52:1·279799 —D112(coupling)→ 279813` and reciprocally `Psa 52:3·279813 —D112→ 279799`: within Ps 52 the boast-in-evil and love-of-evil are coupled (`Psa 52:1·280...`-arc).
- `Psa 56:5·280297 —D112→ 280307` and reciprocally `Psa 56:7·280307 —D112→ 280297`: the enemies' "thoughts against me for evil" coupled to "their crime God's wrath will not let escape".

Edge dimensions: D112(coupling) 19 · D103(source) 3 (`Psa 58:3·280483→306392` venom "from the womb"; `Psa 54:5·280000→279999`; `Psa 56:7·280307→280311`) · D108(manner) 2 (`Psa 73:3·282487→282486`; `Psa 60:11·280793→280792`) · D107(target) 1 (`Psa 53:1·279887→279888`). All `direction: null` — **no edge carries a direction**; the network is undirected and, within this family, extremely sparse (2 reciprocal couplings only). **The inner-being "web" for this family is essentially unbuilt in this file**: the bearer/target/coupling relations are carried almost entirely as *inferred self-flags* (§0), which are not links.

---

## 4. The interior anatomy the data actually names

Assembling only filled interior fields:
- **Seat:** never named (D104 "none" ×56). The data gives wickedness no anatomical seat.
- **Locus (D116, corrected):** almost always `internal:ib-state` (49/56) — wickedness is read as an *inner condition* even though no organ is named; `external:person` 4 and `external:god` 3 mark the few cases pinned to another agent or to God's judgement.
- **Source (D103):** named only 3×, and each time it is an *external* origin/handler, not an inner spring — venom "from the womb/birth" (`Psa 58:3·280483`, cf. D108 "from the womb / birth"), and God who "will return it" / "will not let escape" (`Psa 54:5·280000`, `Psa 56:7·280307`).
- **The one interior-mechanism image:** `Psa 7:14·283602` — conception→pregnancy→birth of evil, the only place the file gives wickedness an internal *productive* anatomy.
- **The one interior-collapse image:** `Psa 40:12·278245` — the heart failing under guilt.
- **Bearers actually inhabiting the human IB from inside:** `the psalmist` (`Psa 40:12·278245`, `Psa 119:101·271215`, and the mis-fused sufferer cases `Psa 88:3·284473`, `Psa 88:8·284507`), `the penitent` (`Psa 51:4·279740`), `we and our fathers` (`Psa 106:6·269838`). Everything else is another's interior observed.

---

## 5. What could not be derived (from this file)

- **No seat for wickedness anywhere** — D104 empty on all 56; the heart/soul/spirit is never named as its seat (contrast the *text* of `Psa 55:21` "war in his heart", `Psa 64:6` "inward mind and heart", which the ledgers do not code to D104).
- **No intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — absent on all 56, so gradation, sub-typing, downstream consequence, and any "shall not" framing are not derivable.
- **Manner unstated on 50/56**; **source unstated on 53/56** — the *how* and *whence* of wickedness are mostly blank.
- **The network is not resolvable here** — 21 of 25 genuine edges point to spans outside this file; their partners cannot be identified within scope, and 146 "edges" are inferred self-flags, not links. No edge has a direction.
- **The bearer is a person/group by inference (`resolution:"inferred"`)** in the vast majority; whether any given "the wicked" is a specific antagonist or a type is not fixed by the data.
- **15 instances are cluster-`null`** — the term-cluster cannot type them, so their placement in an inner-being taxonomy is unresolved from this file.
- **The D112/D116 swap (18 instances)** had to be corrected by rule; the file as stored is internally inconsistent on which field holds the code.

---

## 6. Summary

The `wickedness-ungodliness` family (20 meanings / 56 instances, all poetic/wisdom, role=characteristic ×56) is, as inner-being data, **predominantly a portrait of the observed wicked-other** (status ×42, bearer "the wicked"/"the enemies" ×~44) rather than the reader's own interior; only a thin seam — guilt inundating the self (`Psa 40:12·278245`), penitential self-condemnation (`Psa 51:4·279740`, `Psa 106:6·269838`), and the will turning from evil (`Psa 37:27·277716`, `Psa 119:101·271215`) — reads the *human* IB from inside, plus one interior-generation image (`Psa 7:14·283602`). The label additionally **fuses in non-wickedness senses** (affliction `Psa 88:3`, revulsion `Psa 88:8`, futility `Psa 60:11`) via keyword collision (5 `is_outlier`, 15 cluster-null). Interior anatomy is almost unnamed (seat "none" ×56; locus `internal:ib-state` by default; source ×3, manner ×6), the network is unbuilt within scope (2 reciprocal couplings; 21 edges point outside; 146 self-flags), and D109–D111/D113 are absent throughout — with an 18-instance D112/D116 swap corrected before reading.
