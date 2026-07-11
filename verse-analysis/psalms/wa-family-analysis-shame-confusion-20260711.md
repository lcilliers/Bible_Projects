# Psalms inner-being family analysis — `shame-confusion`

> Source (sole): `outputs/data/psalms-family-base-sources/psalms__shame-confusion.json`. Described **in isolation** per `_family-analysis-method-20260711.md`. Every claim cites `reference · span_id · Dnnn(label)` into that file. Provenance: `ib_characteristic v3 (meaning-keyed) + family grouping v1 + term-based cluster v2`. Scope counts (meta): **13 meanings · 28 instances · 21 passages**; all instances `genre = poetic/wisdom`.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap
Correct order = **D116 a code** (`internal:`/`external:`) + **D112 a phrase**. **8 of 28 instances are transposed** (D116 holds a `paired with …` phrase; D112 holds the `internal:ib-state` code). Read them corrected — true locus = `internal:ib-state`, true coupling = the phrase:

| span_id | reference | D116 holds (phrase) | D112 holds (code) |
|---|---|---|---|
| 270284 | Psa 109:28 | paired with the servant's gladness | internal:ib-state |
| 272640 | Psa 127:5 | paired with the blessed man | internal:ib-state |
| 272717 | Psa 129:5 | paired with the hatred of Zion | internal:ib-state |
| 285689 | Psa 97:7 | paired with worshipping images | internal:ib-state |
| 284759 | Psa 89:41 | paired with the enemies' rejoicing | internal:ib-state |
| 270289 | Psa 109:29 | paired with the accusers and shame | internal:ib-state |
| 270292 | Psa 109:29 | paired with the dishonor | internal:ib-state |
| 270275 | Psa 109:25 | paired with the wagging heads | internal:ib-state |

The remaining 20 instances are in correct order (D116 = `internal:ib-state`, or `external:god` for `281896`/`281905` Psa 69:7,9 · D116(locus); D112 = a phrase).

### 0.2 Self-loop "edges" are not real links
The overwhelming majority of `edges[]` entries are `item_type:"flag"` + `resolution:"inferred"` with `from_span:null` and `to_span` = the span's own id (the bearer/target/coupling/seat/operation inference restated). These are **self-loops, not network edges**. Only `pair`/`resolution:"span"` edges to a **different** span are genuine (§ The network). Net effect: **~22 of 28 instances contribute no genuine edge at all** — their entire `edges[]` is self-referential.

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in 27 of 28.** The **only** filled seat is `Psa 69:7 · span 281897 · D104(seat)` = "the face" (and it is a surface, not an interior organ).
- **D108 manner = "none" in 24 of 28.** Filled in 4: `Psa 69:7 · span 281896 · D108(manner)` "dishonor covering his face"; `Psa 44:15 · span 278724 · D108(manner)` "at the taunter and avenger"; `Psa 44:15 · span 278722 · D108(manner)` "all day long before me"; `Psa 74:21 · span 282619 · D108(manner)` "not turned back in shame".

### 0.4 Absent dimensions
Across **all 28 instances** the following are entirely absent: **D109 intensity · D110 specifier · D111 effect · D113 prohibition.** **D103 source** is present in only **3** instances (`278722` Psa 44:15; `282619` Psa 74:21; `279936` Psa 53:5). D101, D102, D105, D106, D107, D108, D112, D114, D115, D116 are present on every instance (D104 present but almost always "none").

### 0.5 Cluster NULL / T2
No T2. **2 instances carry `cluster.code = null`** (the term-cluster cannot type them): `Psa 74:21 · span 282619` (H1790 dak, "downtrodden") and `Psa 34:5 · span 277254` (H5102, "radiant"). Both are read-included by their verse's shame-context, not by a shame-cluster term.

### 0.6 Other integrity notes
- **D115 role = "characteristic" on all 28** — no qualifiers, no standalones.
- **D105 bearer = `resolution:"inferred"` on all 28** — no bearer is stated outright.
- **6 instances flagged `is_outlier:true`** (cluster M06(Hate), not the family-expected M07(Shame)) — all lemma **H2781 cherpah**: `276683` Psa 31:11, `281896` Psa 69:7, `281905` Psa 69:9, `283511` Psa 79:4, `284759` Psa 89:41, `270275` Psa 109:25.

---

## 1. Coherence — does the label fit its data?

**Partially.** The core is coherent; the label over-reaches on one half and the grouping has fused three adjacent-but-distinct movements plus one antonym.

**Coherent core (M07 Shame, bosh/bosheth/bushah/kelimmah/chapher):** the disgrace/humiliation field — `H0954` put-to-shame (11+1+1 inst.), `H1322` shame (`270292`, `278724`), `H0955` shame (`284786`), `H3639` dishonor/disgrace (`270289`, `281897`, `278722`), `H2659` disgrace (`283978`). One inner-being movement: **shame as exposure/loss of standing**.

**Problems with the label and grouping:**
1. **"confusion" is unsupported.** No meaning, sense (D101) or discovery (D114) in the file reads as *confusion/dismay* in its own right; every head-term is shame / disgrace / reproach / scorn. The "confusion" half of the family name has **no data behind it** (it is presumably carried over from bosh's lexical range "be ashamed/confounded", but no instance is so read).
2. **A distinct reproach/scorn movement (M06 Hate, cherpah, 6 inst.)** is fused in as outliers: `Psa 31:11 · span 276683` (a reproach, dreaded, fled from), `Psa 69:7/9 · spans 281896/281905` (reproach borne for God), `Psa 79:4 · span 283511` (become a taunt), `Psa 89:41 · span 284759` (become a scorn), `Psa 109:25 · span 270275` (object of scorn). This is **being-the-object-of-others'-contempt (social rejection)**, adjacent to but not identical with the internal state of being-ashamed; the outlier flag is correct.
3. **One antonym is included:** `Psa 34:5 · span 277254 · D102(type)=affect`, "those who look to him are **radiant**, and their faces shall never be ashamed" (H5102, cluster null). This is the **positive opposite** of shame, pulled in only because its verse names "ashamed". It belongs to the arc solely as its negation.

**First-class structural finding — shame is two-directional by bearer (D105).** The single most important pattern the data carries: the same shame-movement falls on **two opposite parties**:
- **Feared/borne by the righteous / people / king:** `271316` 119:116, `271786` 119:31, `271867` 119:46, `271956` 119:6, `272104` 119:80 (all "let me **not** be put to shame"); `278724`/`278722` 44:15 (the nation); `281896`/`281905`/`281897` 69:7–9 (borne for God); `282619` 74:21 (downtrodden); `284759`/`284786` 89:41,45 (the king); `283511` 79:4 (we); `270275` 109:25 & `276683` 31:11 (the psalmist).
- **Imprecated upon the wicked / enemies / idolaters:** `270284` 109:28, `270289`/`270292` 109:29, `272717` 129:5, `283974`/`283978` 83:17, `284318` 86:17, `285689` 97:7, `279936` 53:5, `272081` 119:78; and negated for the righteous man vs. his foes `272640` 127:5.

Shame is thus **a mobile weapon of vindication**: the psalmist prays it *off* himself and *onto* his adversaries — the two poles meet explicitly at `Psa 109:28 · span 270284 · D114(discovery)` ("the foes shamed, the servant gladdened").

---

## 2. The movements evidenced (grounded, cited)

### 2a. Shame feared as the endpoint of hope — warded off by torah-fidelity (Ps 119, bosh)
The dominant sub-pattern: shame is the **feared outcome averted by clinging to the word**. `Psa 119:6 · span 271956 · D114` shame "averted by fixing the eyes on the commandments"; `Psa 119:31 · span 271786 · D114` "the plea against shame, clinging to the word"; `Psa 119:80 · span 272104 · D114` "shame guarded against by a blameless heart"; `Psa 119:116 · span 271316 · D114` "the hope that must not end in shame"; `Psa 119:46 · span 271867 · D114` "bold testimony without shame before kings". D102(type)=state; D106(operation)="be (or not be) put to shame"; D112(coupling, corrected)="paired with the whole SHAME-arc of the psalm". Movement: **shame is the negative telos of hope; fidelity to the word is what holds it off.**

### 2b. Shame as covering / garment on the face (kelimmah, bosheth)
Shame is imaged as something that **veils or clothes**. `Psa 44:15 · span 278724 · D114(discovery)` "shame as a veil over the countenance"; `Psa 69:7 · span 281897 · D114` "humiliation veiling the psalmist like a garment", the one instance with `D104(seat)=the face`; `Psa 109:29 · spans 270289/270292 · D106(operation)` "be clothed with dishonor" / "be wrapped in shame … as a cloak"; `Psa 89:45 · span 284786 · D106` "be covered with shame". Movement: **shame is worn — put on the interior from outside, settling visibly on the face.**

### 2c. Reproach borne on God's account (cherpah — M06 outlier)
`Psa 69:7 · span 281896 · D114(discovery)` "shame suffered on God's account … his disgrace bound up with God's"; `Psa 69:9 · span 281905 · D114` "identification with God so complete that God's shame becomes his"; both `D116(locus)=external:god`. `Psa 31:11 · span 276683 · D106(operation)` "the wound of being shunned; the interior suffers the withdrawal of everyone", D112(coupling)="reproach-shunned". Movement: **social rejection as an inner wound, and reproach voluntarily carried out of devotion to God.**

### 2d. Communal / royal humiliation (cherpah, bushah — become/covered)
`Psa 79:4 · span 283511 · D114` "the communal humiliation … disgrace felt as an inner wound"; `Psa 89:41 · span 284759 · D114` "the king's humiliation, the anointed made a reproach"; `Psa 89:45 · span 284786 · D114` "glory turned to humiliation". Bearer (D105) = "we (the people)" / "the king". Movement: **corporate and royal shame — a whole people or its anointed made an object of scorn.**

### 2e. Shame imprecated on the wicked / idolaters (bosh, kelimmah, chapher)
`Psa 53:5 · span 279936 · D103(source)` "because God has rejected them", D114 "the inner ruin of exposure and defeat"; `Psa 83:17 · spans 283974/283978 · D114` "the enemies' humiliation invoked … honour stripped away"; `Psa 86:17 · span 284318 · D114` "the confounding of the foes when God vindicates his servant"; `Psa 97:7 · span 285689 · D114` "the confounding of idolaters when the true God appears"; `Psa 109:28/29 · spans 270284/270289/270292`; `Psa 119:78 · span 272081`; `Psa 129:5 · span 272717 · D114` "the haters of Zion routed and shamed". Movement: **shame as the invoked collapse of the enemy — the mirror-image of 2a.**

### 2f. The antonym — radiance instead of shame (H5102, cluster null)
`Psa 34:5 · span 277254 · D102(type)=affect · D114(discovery)` "transformation by gaze: the interior that turns to God is lit and kept from shame". The **only positive affect** in the file, and the family's structural negation: looking to God is the operation that forecloses shame.

---

## 3. The network (genuine `pair`/`span` edges only)

After discarding self-loops (§0.2), only the 6 `status`-typed instances of Ps 44 / Ps 53 / Ps 69 / Ps 74 carry genuine edges. **Two connected components lie inside the file; the rest dangle to spans outside this family scope.**

**Component A — Psa 69:7–9 (reproach / dishonor knot):**
- `span 281896 (69:7 reproach) → 281897 (69:7 dishonor)` on **D108(manner)** — reproach manifest as dishonor covering the face.
- `span 281896 (69:7) ↔ 281905 (69:9 reproaches)` on **D112(coupling)** — reciprocal (`281896→281905` and `281905→281896`): the reproach borne (v7) and the reproaches that fell (v9) are one.
- `span 281897 (69:7 dishonor) → 281896 (69:7 reproach)` on **D112(coupling)**.
→ A tight triangle: reproach ⇄ its coupled reproaches ⇄ the dishonour on the face. All three in-file.

**Component B — Psa 44:15 (disgrace / shame pair):**
- `span 278722 (disgrace) ↔ 278724 (shame)` on **D112(coupling)**, reciprocal — "my disgrace before me" welded to "shame has covered my face".

**Genuine edges dangling out of scope** (target span not in this file — real links whose other end is undescribed here):
- `281905 (69:9) → 281907` on D106(operation, span).
- `278722 (44:15) → 278857` on D103(source, span).
- `278724 (44:15) → 278730` on D108(manner, span).
- `282619 (74:21) → 282522` (D103 source), `→ 282621` (D108 manner), `→ 282622` (D112 coupling) — all span, all out-of-file.
- `279936 (53:5) → 279939` (D103 source), `→ 279928` (D112 coupling) — both out-of-file.

**Network verdict: extremely sparse.** Only 2 small in-file components (5 spans of 28); the other 23 spans are network-isolated within this source, and every non-self-loop edge on the 3 "source"-bearing spans (74:21, 53:5, and half of 44:15/69:9) reaches spans that this base source does not contain.

---

## 4. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seat (D104):** one named — **"the face"** (`281897`, Psa 69:7). The face recurs in the *discovery* prose as the surface shame covers (44:15, 69:7, and the "covered with shame" of 89:45, "cover his face" of 44:15) but is coded as a seat only once. **No interior organ (heart/soul/spirit) is ever named as shame's seat.**
- **Source (D103):** three, all **God as the agent who shames/rejects/afflicts** — `Psa 44:15 · span 278722 · D103` "God's rejecting and disgracing (v9)"; `Psa 53:5 · span 279936 · D103` "because God has rejected them"; `Psa 74:21 · span 282619 · D103` "whom God is implored not to cast off". Where a source is given, **shame originates from God's rejection/withdrawal**, not from the enemies (the enemies are the occasion/target, D107).
- **Coupling (D112, corrected):** shame is bound to — the psalm's whole shame-arc (Ps 119 group), disgrace/shame covering the face (44:15 pair), the reproach borne for God (69:7↔69:9), terror (53:5, "paired with their terror"), being mocked/derided (79:4), the enemies' rejoicing (89:41), the poor who praise (74:21), the servant's gladness (109:28). Couplings run **either to co-located shame-words or to the answering emotion of the opposite party**.
- **Locus (D116, corrected):** `internal:ib-state` for 26 of 28; **`external:god`** for the two Ps 69 reproach spans (`281896`, `281905`) — shame located *in the God-relation* rather than in the bare interior.
- **Target (D107):** consistently the audience of exposure — "before God/men", "before enemies at the gate" (127:5), "to his accusers" (109:25), "to the neighbours" (79:4). Shame is inherently **relational/public**.

---

## 5. What could not be derived (from this source)

- **The whole "confusion" half of the family label** — no confusion/dismay is read on any instance (§1.1).
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — absent on all 28; the *degree*, *sub-type*, *downstream effect*, and any *prohibitive* framing of shame cannot be read here.
- **The interior seat** — unstated in 27/28; where shame "sits" in the inner being (beyond the surface "face") is **not derivable**.
- **The manner** of the movement — "none" in 24/28; *how* shame comes upon the bearer is mostly unspecified.
- **Source of shame** in 25/28 — only 3 give a source (all = God's rejection); for the enemy-imprecations and the Ps 119 pleas the causal origin is not coded.
- **The far side of most genuine edges** — every `source`/`operation`/`manner` span-edge except the Ps 69 and Ps 44 in-file pairs points to a span **outside this base source** (`281907, 278857, 278730, 282522, 282621, 282622, 279939, 279928`); those linked movements cannot be described from this file.
- **Bearer identity** is inferred, never stated (all D105 `resolution:inferred`) — attributions (psalmist / king / nation / enemies / idolaters) are the reader's inference (D114), not asserted data.
- **Typing of 2 instances** — `282619` (downtrodden) and `277254` (radiant) have `cluster.code=null`; the term-cluster does not assign them to the shame movement.

---

## 6. Summary

The `shame-confusion` base source is a **coherent shame/disgrace corpus with a mislabelled second half and three adjacent movements fused in**. Core = M07 Shame (bosh/kelimmah/chapher, ~19 inst.): **shame as public exposure and loss of standing**, worn like a garment on the face, feared as the negative telos of hope and warded off by torah-fidelity (Ps 119), invoked as the collapse of the wicked, and sourced — where sourced at all — in **God's rejection**. Its defining structure is **two-directional by bearer**: prayed *off* the righteous and *onto* the enemy, meeting where the foe's shame is the servant's gladness (Psa 109:28). Grafted in: a reproach/scorn movement (M06 cherpah, 6 outliers) = social rejection borne for God; and one antonym, radiance (Psa 34:5), the shame-arc's negation. Data is thin on anatomy (seat named once = "the face"; intensity/specifier/effect/prohibition wholly absent), the network is very sparse (2 tiny in-file components; most span-edges dangle out of scope), **8 instances have D112/D116 transposed**, and the label's "confusion" is **unsupported by any instance**.
