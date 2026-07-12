# Family analysis — Psalms · grace-mercy-compassion (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__grace-mercy-compassion.json` only. Scope `meta.scope.family = grace-mercy-compassion`; counts declared: 11 meanings · 16 instances · 13 passages. Every claim cited `reference · span N · Dnnn(label)`. Nothing imported from outside this file.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling)/D116(locus) field-swap — 10 of 16 instances transposed
Correct order = D116(locus) holds a code (`internal:`/`external:`), D112(coupling) holds a phrase. Where D116 holds a prose phrase and D112 holds the code, the pair is **swapped** and must be read corrected. Swapped instances (read D112↔D116):

| reference · span | D112 as stored | D116 as stored | corrected locus |
|---|---|---|---|
| Psa 109:12 · span 270172 (kindness) | `internal:ib-state` | "paired with none to pity his children" | internal:ib-state |
| Psa 109:16 · span 270197 (kindness) | `internal:ib-state` | "paired with the failure to remember" | internal:ib-state |
| Psa 116:1 · span 270926 (pleas for mercy) | `external:god` | "paired with the love and calling" | external:god |
| Psa 130:2 · span 272809 (pleas for mercy) | `external:god` | "paired with the cry" | external:god |
| Psa 102:14 · span 268928 (pity) | `internal:ib-state` | "paired with holding her stones dear" | internal:ib-state |
| Psa 109:12 · span 270174 (pity) | `internal:ib-state` | "paired with the kindness withheld" | internal:ib-state |
| Psa 112:5 · span 270684 (deals generously) | `internal:ib-state` | "paired with conducting affairs with justice" | internal:ib-state |
| Psa 112:4 · span 270679 (gracious) | `internal:ib-state` | "paired with being merciful and righteous" | internal:ib-state |
| Psa 112:4 · span 270680 (merciful) | `internal:ib-state` | "paired with being gracious" | internal:ib-state |
| Psa 103:13 · span 269084 (shows compassion) | `internal:ib-state` | "paired with God's compassion on those who fear him" | internal:ib-state |

The remaining **6 are correctly ordered** (D116 a code, D112 a phrase): Psa 141:5 · span 273722 (D116 `internal:ib-state`); Psa 140:6 · span 273653 (`internal:ib-state`); Psa 37:21 · span 277679 (`internal:ib-state`); Psa 45:2 · span 278942 (`internal:ib-state`); Psa 55:1 · span 280032 (`external:god`); Psa 72:13 · span 282244 (`internal:ib-state`). Note the three genuine `pair`/`span` couplings (278942, 280032, 282244 — see §0.2) all sit in correctly-ordered rows; every swapped row carries the inferred-flag code, never a real pair.

**Corrected locus tally (D116):** `internal:ib-state` = 13; `external:god` = 3 (Psa 116:1 · span 270926, Psa 130:2 · span 272809, Psa 55:1 · span 280032 — all supplication). No interior seat is ever named by the locus; "internal:ib-state" is a bare marker, not an organ.

### 0.2 Self-loop "edges" are not links — only 4 genuine pair edges, all pointing outside the family
Every instance carries D105(bearer)/D107(target)/D112(coupling) "edges" with `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's own id. These are **self-loops, not network edges** and are discarded.

Genuine `pair`/`resolution:"span"` edges to a **different** span (the only real network):
- Psa 45:2 · span 278942 · D112(coupling) → span **278947** ("the graciousness for which God blessed him").
- Psa 55:1 · span 280032 · D112(coupling) → span **280027** ("twinned with the prayer").
- Psa 72:13 · span 282244 · D107(target) → span **282246** ("the weak and needy").
- Psa 72:13 · span 282244 · D112(coupling) → span **282248** ("paired with saving their lives").

All four targets (278947, 280027, 282246, 282248) are **outside this family file** — none is any of the 16 family spans. **The within-family network is empty:** no family member links to another. The three "connected" spans each bind to a companion span (a blessing, a prayer, the weak/the saving) that this file does not describe.

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in all 16 instances** — the interior location of grace/mercy is never stated anywhere in this family.
- **D108 manner = "none" in 15 of 16.** The sole filled manner: Psa 45:2 · span 278942 · D108(manner) = "poured on his lips" (flag, inferred).

### 0.4 Absent dimensions (across all 16 instances)
No instance carries **D103 source, D109 intensity, D110 specifier, D111 effect, or D113 prohibition** — all five are wholly absent. The only dimensions present are 101 sense, 102 type, 104 seat, 105 bearer, 106 operation, 107 target, 108 manner, 112 coupling, 114 discovery, 115 role, 116 locus. D103(source) being absent means **what moves grace/mercy is never given**.

### 0.5 Cluster NULL / T2
None. Every meaning carries a real term-cluster: M05(Love), M21(Prayer) or M39(Blessing). No null, no T2.

### 0.6 Role (D115)
All 16 instances: D115(role) = "characteristic". No qualifier, no standalone.

---

## 1. Coherence check — the label fuses TWO opposed movements

**The family label "grace-mercy-compassion" does NOT name one coherent inner-being movement.** The keyword "mercy" has fused two distinct, opposite-facing movements:

**Movement A — mercy GIVEN (outgoing disposition toward others).** 13 instances. The IB *is* gracious/merciful/compassionate and shows it to the weak, the needy, others. Clusters M05(Love) + M39(Blessing).
- kindness (chesed): Psa 109:12 · span 270172; Psa 109:16 · span 270197; Psa 141:5 · span 273722 · D101(sense) "rebuke received as kindness".
- pity/graciousness (chanan): Psa 102:14 · span 268928; Psa 109:12 · span 270174; deal generously Psa 112:5 · span 270684; generous Psa 37:21 · span 277679.
- grace/charm (chen): Psa 45:2 · span 278942 · D101(sense).
- gracious (chanun): Psa 112:4 · span 270679; merciful (rachum): Psa 112:4 · span 270680.
- pity/compassion (chus): Psa 72:13 · span 282244; shows compassion (racham): Psa 103:13 · span 269084.

**Movement B — mercy SOUGHT (incoming supplication, directed upward to God).** 3 instances. Not the IB showing mercy but the IB *begging for* it. Cluster M21(Prayer); corrected locus `external:god`.
- pleas for mercy (tachanun): Psa 116:1 · span 270926 · D106(operation) "plead for mercy"; Psa 130:2 · span 272809; Psa 140:6 · span 273653.
- plea for grace / supplication (techinnah): Psa 55:1 · span 280032 · D101(sense).

These face opposite ways: A is a disposition/act flowing **out** to the weak; B is a cry flowing **up** to God, seeking favour the pleader "expects nothing by right" (Psa 55:1 · span 280032 · D114(discovery)). The Hebrew makes the fusion visible: the **chanan** root supplies both directions — chen/chanun/chanan = grace-given (Movement A), while techinnah/tachanun = plea-for-grace (Movement B). The grouping is a lexical keyword coincidence, not one movement. **This is a first-class finding: the family must be split A vs B before synthesis.**

---

## 2. Movement A — mercy given (the outgoing disposition)

### 2.1 What the word is (D101 sense / D102 type)
Dominantly a **disposition**: kindness Psa 109:12 · span 270172 · D102(type) "disposition"; Psa 109:16 · span 270197 · D102; pity Psa 102:14 · span 268928 · D102; Psa 109:12 · span 270174 · D102; gracious Psa 112:4 · span 270679 · D102; merciful Psa 112:4 · span 270680 · D102; shows compassion Psa 103:13 · span 269084 · D102. It surfaces also as **action** (deal generously Psa 112:5 · span 270684 · D102), **volition** (generous Psa 37:21 · span 277679 · D102), **status** (grace Psa 45:2 · span 278942 · D102; pity/chus Psa 72:13 · span 282244 · D102), and once as **affect** (rebuke-as-kindness Psa 141:5 · span 273722 · D102). So the same mercy is read now as settled disposition, now as an act, once as an act of will, once as a received affect.

### 2.2 What it does (D106 operation) and toward whom (D107 target)
The operation is consistently *to extend / show / have* mercy: "extend kindness" Psa 109:12 · span 270172 · D106; "have pity / affection" Psa 102:14 · span 268928 · D106; "be gracious" Psa 112:4 · span 270679 · D106; "be merciful" Psa 112:4 · span 270680 · D106; "show compassion" Psa 103:13 · span 269084 · D106; "have pity / compassion" Psa 72:13 · span 282244 · D106; "deal generously" Psa 112:5 · span 270684 · D106. Targets (all D107) reach the weak and outside: "to the enemy" Psa 109:12 · span 270172; "to the afflicted" Psa 109:16 · span 270197; "for Zion's dust" Psa 102:14 · span 268928; "the weak and needy" Psa 72:13 · span 282244 (genuine pair → span 282246); "to his children" Psa 103:13 · span 269084; "to others" Psa 112:4 · spans 270679 / 270680. Two targets are self-directed/abstract: "embrace-correction" Psa 141:5 · span 273722 · D107; "generosity" Psa 37:21 · span 277679 · D107.

### 2.3 The negation sub-pattern (mercy withheld)
Movement A includes its own inversion — mercy **refused**, read via the wish that the merciless find none:
- Psa 109:12 · span 270172 · D114(discovery): "the wish that the merciless man find no mercy"; D105(bearer) "no one".
- Psa 109:12 · span 270174 · D114(discovery): "the wish that the pitiless find no pity for his own"; D105(bearer) "no one".
- Psa 109:16 · span 270197 · D114(discovery): the enemy "did not remember to show kindness … the root of his condemnation"; D105(bearer) "the enemy".

So within the "grace" family, three instances are mercy *absent* — the characteristic defined by its lack.

### 2.4 The rare inward variant
Psa 141:5 · span 273722 · D106(operation): "a righteous man's blow/rebuke is welcomed as kindness, oil for the head — correction embraced"; D114(discovery) flags it "rare: the interior wants to be corrected, receiving reproof as care." Here mercy is *received inward* as an affect, not dispensed outward — a distinct sub-movement of one instance.

### 2.5 Bearers (D105) — human IB throughout, all inferred
Bearers are human or negated-human: "the man"/God-fearer (Psa 112:4 · spans 270679, 270680; Psa 112:5 · span 270684), "the righteous" (Psa 37:21 · span 277679), "the king" (Psa 45:2 · span 278942; Psa 72:13 · span 282244), "a father" (Psa 103:13 · span 269084), "the servants (of God)" (Psa 102:14 · span 268928), "no one"/"the enemy" (Psa 109 negations). **God is correctly screened out**: Psa 103:13 · span 269084 captures the human *father's* racham ("As a father shows compassion") per D114(discovery), while the parallel "so the Lord shows compassion" is not made an instance. Every D105 is `resolution:"inferred"` — no bearer is stated on the surface.

---

## 3. Movement B — mercy sought (the upward supplication)

### 3.1 Sense / type
Read as **action** (Psa 116:1 · span 270926 · D102(type); Psa 130:2 · span 272809 · D102; Psa 55:1 · span 280032 · D102) and once **affect** (Psa 140:6 · span 273653 · D102). Senses: "pleas for mercy (tachanun)" (270926, 272809), "pleas for mercy voiced" (273653), "plea for grace / supplication (techinnah)" (280032).

### 3.2 Operation, target, locus
Operation = plead/cry: "plead for mercy" Psa 116:1 · span 270926 · D106; Psa 130:2 · span 272809 · D106; "the psalmist lifts a crying voice of supplication, the cry as the counter-move to the schemes" Psa 140:6 · span 273653 · D106; "plead for favour" Psa 55:1 · span 280032 · D106. Target = Godward: "to God" (270926), "before God" (272809), "to God" (280032); once abstracted "crying-out" (273653 · D107). Corrected locus `external:god` for 270926, 272809, 280032; but Psa 140:6 · span 273653 · D116(locus) = `internal:ib-state` (the cry read as an interior state, not yet Godward-coded) — a small inconsistency within Movement B. Bearer = "the psalmist" in all four (D105, inferred). D114 (Psa 140:6 · span 273653): "against the silent scheming, the psalmist's interior goes vocal, appealing upward."

---

## 4. The network (genuine pair edges only)

Only 3 family spans carry any genuine edge, and **all four edges leave the family** (§0.2): Psa 45:2 · span 278942 → 278947 (grace bound to the blessing it earned), Psa 55:1 · span 280032 → 280027 (supplication twinned with the prayer), Psa 72:13 · span 282244 → 282246 (pity → its object, the weak/needy) and → 282248 (pity paired with the saving of their lives). **No family-internal edge exists** — the 16 members are not linked to one another in the data. The network is therefore sparse and outward-only: mercy-given (278942, 282244) binds to blessing / the weak / rescue; mercy-sought (280032) binds to prayer. All other apparent "edges" are inferred self-loops and carry no link.

---

## 5. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seat: nothing.** D104 = "none" in all 16 — no heart, soul, ruach, eye. The organ of grace/mercy is never located.
- **Source: nothing.** D103 absent in all 16 — what moves mercy is never given.
- **Manner: one datum only** — grace "poured on his lips" (Psa 45:2 · span 278942 · D108), locating gracious speech at the lips, the single bodily anchor in the family.
- **Coupling (corrected D112, phrases):** mercy sits *beside* its companions — kindness beside pity/beside the failure to remember (Psa 109:12/16 · spans 270172, 270197); pity beside holding Zion's stones dear (Psa 102:14 · span 268928); generosity beside justice (Psa 112:5 · span 270684, "conducting affairs with justice"); graciousness beside mercy-and-righteousness (Psa 112:4 · spans 270679/270680, "gracious, merciful, and righteous"); compassion beside God's own compassion (Psa 103:13 · span 269084). The genuine pairs bind grace→blessing (278942→278947), pity→the weak and their rescue (282244→282246/282248), supplication→prayer (280032→280027).
- **Locus (corrected):** 13 internal:ib-state, 3 external:god (the supplications). The only externally-oriented members are the pleas to God.

So the anatomy the file *names* is thin: an unlocated interior disposition (mostly "internal:ib-state" with no organ), voiced once at the lips, that couples outward to justice, blessing, the weak, and the prayer — never to a stated bodily seat.

---

## 6. What could not be derived (flagged)

- **Seat (D104):** underivable for all 16 — grace/mercy has no interior location in this source.
- **Source (D103):** absent for all 16 — the mover of mercy is never stated.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113):** absent across the entire family — no degree, no qualifier, no downstream effect, no proscription recorded.
- **Manner (D108):** underivable for 15/16 (only Psa 45:2 · span 278942 filled).
- **Bearer (D105):** stated on no surface — all 16 inferred; identities (the man/king/psalmist/father/servants) are the reader's supply, not the text's.
- **Within-family network:** none — no family span links to another; §4 edges all exit the file, so the internal relational structure cannot be derived here.
- **D112/D116 integrity:** 10/16 stored transposed (§0.1) — any downstream consumer reading the fields as stored will mis-assign locus vs coupling.
- **Locus of Movement B:** inconsistent — Psa 140:6 · span 273653 coded `internal:ib-state` where its siblings are `external:god`.

---

## 7. Summary

11 meanings / 16 instances across 13 Psalms passages, all `role=characteristic`, poetic/wisdom genre. The label **grace-mercy-compassion fuses two opposed movements**: mercy GIVEN (13 instances — an outgoing, mostly unlocated disposition of kindness/pity/graciousness/compassion toward the weak; chesed/chanan/rachum/chus/chen; M05+M39), and mercy SOUGHT (3 instances — an upward supplication/plea to God; techinnah/tachanun; M21, locus external:god). The chanan root spans both directions, which is why the keyword grouping collapsed them. Data-integrity limits are heavy: **seat and source are never given (all 16), four dimensions (D109/110/111/113) are wholly absent, manner is filled once, all bearers are inferred, the within-family network is empty (all real edges exit the file), and 10/16 rows have D112/D116 transposed.** The mercy-withheld negations in Psa 109 and the rare "rebuke-received-as-kindness" (Psa 141:5) are distinct sub-patterns worth preserving. Recommendation: split A/B before any synthesis and treat the family as a keyword cluster, not a single inner-being movement.
