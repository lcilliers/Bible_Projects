# Family analysis — `inner-seat-heart-soul-spirit` (Psalms)

> In-isolation analysis of a single base source: `verse-analysis/psalms/_base-sources/psalms__inner-seat-heart-soul-spirit.json`. Nothing outside that file is used. Every claim cites `reference · span_id · Dnnn(label)`.
> Scale (from `meta.counts`): **31 meanings · 185 instances · 109 passages**. Genre uniform: all 185 `poetic/wisdom`; 20 are passage anchors.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap — **50 of 185 transposed**
Correct order per method = D116 holds a code (`internal:`/`external:`), D112 holds a prose phrase.
- **Correct (D116=code, D112=phrase): 135 instances.**
- **Swapped (D112 holds the code, D116 holds the phrase): 50 instances** — read them corrected.
- No instance has both fields as codes or both as phrases; every instance carries both D112 and D116 (185/185), so the swap is a clean binary.

The 50 swapped span_ids (all show `D112 = internal:… / external:god` where the *code* actually belongs in D116):
`269054 (Psa 103:1)`, `269134 (103:2)`, `269169 (103:22)`, `269205 (104:1)`, `269345 (104:35)`, `270045 (107:5)`, `270068 (107:9)`, `270070 (107:9)`, `270318 (109:31)`, `270991 (116:4)`, `271003 (116:7)`, `271010 (116:8)`, `272469 (123:4)`, `272824 (130:5)`, `272829 (130:6)`, `272872 (131:2)`, `272879 (131:2)`, `273338 (138:3)`, `285374 (94:19)`, `302659 (94:17)`, `269447 (105:25)`, `269474 (105:3)`, `269877 (107:12)`, `270076 (108:1)`, `270262 (109:22)`, `270700 (112:7, external:god)`, `270704 (112:8)`, `272857 (131:1)`, `273312 (138:1)`, `285351 (94:15)`, `285646 (97:11)`, `302589 (102:4)`, `268821 (101:2)`, `268838 (101:4)`, `268851 (101:5)`, `269241 (104:15)`, `269249 (104:15)`, `270567 (111:1)`, `285456 (95:10)`, `285510 (95:8)`, `307463 (106:33)`, `272497 (124:4)`, `272500 (124:5)`, `272317 (120:6)`, `272512 (124:7)`, `270269 (109:24)`, `272551 (125:4)`, `272302 (120:2)`, `268837 (101:4)`, `269901 (107:18)`.
Note the swap clusters heavily in the Psa 94–131 range (Books IV–V), i.e. it is a batch artefact of one coding run, not random.

**Corrected D116 (locus) code distribution** (code taken from whichever field holds it):
`internal:ib-state 151 · internal:seat 15 · internal:heart 13 · internal:spirit 3 · external:god 3`.
→ The interior is overwhelmingly **internal (182/185)**; only 3 spans locate the coupling **outside** the self, and all 3 are `external:god` (`270700 · Psa 112:7 · D116(locus) external:god` — the heart firm because *trusting in the LORD*; plus the two swap-corrected god-locus spans).

### 0.2 Self-loop / non-edge "edges"
- **0 flag/inferred self-loops** (no `flag`+`inferred` edge points to its own span).
- **15 `pair` edges are self-pairs** (`to_span == from_span`) — all on **D104(seat)** — and are therefore **not** network links: `278509 (Psa 42:1)`, `278524 (42:11)`, `278534 (42:2)`, `278555 (42:4)`, `278569 (42:5)`, `278578 (42:6)`, `278673 (43:5)`, `278791 (44:25)`, `279323 (49:15)`, `278870 (45:1)`, `279381 (49:3)`, `302624 (44:18)`, `302640 (44:21)`, `279350 (49:18)`, `279194 (48:13)`. These are "the seat is itself" self-references, discarded from the network.
- The `edges[]` arrays also carry 475 `flag`/`inferred` items on D105/D107/D112/D104/D108 — these are the relational *sub-set copies* of value-flags, **not** genuine links; excluded.
- **Genuine cross-span `pair`/`span` edges: 60** (see §Network).

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none": 150/185 (81%)** — the seat is left unnamed. (Filled 35: `the heart itself` 11, `soul (self)` 10, `heart (self)` 5, plus one-offs `within the penitent` 2, `the mouth`, `within me`, `the inward being itself`, etc.) The family is *about* seats, yet in 81% of instances the term **is** the seat, so D104 is redundantly "none".
- **D108 manner = "none": 158/185 (85%)**. The 27 filled manners are all lament/rescue textures — `cast down and in turmoil` (×3), `bowed down to the dust`, `broken / shattered`, `from the power of Sheol`, `willing / free (nadib)`, `right / steadfast (nakon)`, etc.

### 0.4 Absent dimensions (across all 185)
- **D109 intensity — absent in all 185.**
- **D110 specifier — absent in all 185.**
- **D111 effect — absent in all 185.**
- **D113 prohibition — present in exactly 1** (`302624 · Psa 44:18 · D113` = negated: "Our heart has **not** turned back").
- **D103 source — present in only 8** (all relational; see §Network / §Interior anatomy).
Dimensions present in all 185: D101, D102, D104, D105, D106, D107, D108, D112, D114, D115, D116.

### 0.5 Cluster NULL / T2
- **NULL cluster: 11 instances** (the term-cluster cannot type them). All are *non-seat* reads pulled in by keyword co-occurrence, not constitutional seats:
  `270479 (Psa 10:7)` & `280555 (59:12)` H0423 *cursing*; `270364 (10:11)` & `270469 (10:6)` H0559 *says*; `276830 (31:5)` H6485 *commit*; `271296 (119:113)` H5588 *double-minded*; `274743 (16:7)` H3629 *heart/kidney (instructs)*; `278221 (40:10)` H3680 *hidden*; `279759 (51:6)` H2910 *inward being*; `273403 (139:13)` H3629 *inward parts (kilyah)*; `272028 (119:70)` H2459 *unfeeling*.
- **T2 cluster: 0 instances.**
- **role(D115) = `characteristic` for all 185** — no qualifier/standalone rows; every span is typed as a characteristic.

---

## 1. Coherence — does the family label fit its data?

**Mostly yes, with a definable contamination edge.** 170/185 instances (92%) sit in **M47 Constitution**, and the D101/lexical inventory names exactly the constitutional seats the label promises: **soul (nephesh, H5315)**, **heart (leb H3820 / lebab H3824 / H3826 / kidney H3629)**, **spirit (ruach H7307)**, **flesh (basar H1320)**, **inward being (tuchoth H2910)**. So the keyword grouping has genuinely fused **one coherent movement: the interior seat of the self**, addressed, roused, cast down, restored.

But three seams break the coherence and are first-class findings:

1. **4 flagged outliers** (`is_outlier=true`) are non-constitutional crossovers dragged in by co-text:
   - `H7908:bereft · 285… · M03(Grief)` — "my soul bereft" (`Psa 35:12`).
   - `H6869:troubl · M03(Grief)` — "the troubles of my heart enlarged" (`Psa 25:17`).
   - `H6141:pervers · M14(Deceit)` — "perverse (iqqesh)" heart (`Psa 101:4`).
   - `H4974:soundnes · M12(Purity)` — "no soundness in my flesh" (`Psa 38:3`).
   These are *qualities predicated of* a seat, not seats.
2. **11 NULL-cluster reads** (§0.5) are verbs/qualities co-located with a seat-word — *cursing, says, commit, hidden, double-minded, unfeeling, inward parts* — not seats themselves. The label over-collects them.
3. **Grammatical fragmentation of one seat into many "meanings":** `nephesh` (H5315) is split by ESV surface rendering into **7 char_keys** — `:soul` (65), `:us`, `:i`, `:we`, `:he`, `:me`, `:they` — and `leb` (H3820) into `:heart` (57), `:accord`, `:doubl`, `:themselv`, `:well`; `basar` into `:flesh`/`:body`. These are **not distinct movements**; they are the same seat under different pronoun renderings (`char_key` is ESV-keyed, per `meta.structure`). The "31 meanings" therefore overstate the distinct inner-being objects — the real seats number roughly **5** (soul, heart, spirit, flesh, inward parts).

Net: the family is a **coherent "constitutional seat" movement** with a thin contamination rim (~15 non-seat instances) and internal over-splitting.

---

## 2. What the term is — sense(D101) / type(D102)

- **D101 sense is effectively free-text** — the reader's phrase, near-unique per instance (`soul (nephesh)` 34 and `heart (leb)` 24 are the only repeated values; the remaining ~90 are one-off read-phrases like `my heart melted like wax`, `spirit faints within`). It is a read label, **not** a controlled value — usable as evidence but not as a category.
- **D102 type is controlled** and gives the anatomy of the family:
  `faculty 92 · status 30 · state 20 · affect 13 · seat 12 · cognition 8 · volition 4 · action 4 · disposition 2` (=185).
  → The interior here is read predominantly as an **operative faculty** (92) — a working organ of the self — then as a **standing status/state** (50 combined), with **affect** (13) and explicit **cognition/volition** (12) minor. Only 12 spans are typed as bare **seat**; i.e. even the seat-words are mostly caught *in operation*, not at rest.

---

## 3. Whose interior — bearer(D105)

All 185 bearers are `item_type=flag, resolution=inferred` — **every bearer is inferred**, none stated outright, and none is God (God appears only as external source/locus, §Interior). The bearer is human IB throughout:
`the psalmist 103`, then `the people/community/nation` (~13 combined), `David` 6 (+ 3 "David addressing his own soul", the reflexive interior turned on itself, e.g. `Psa 103:1`), `the penitent` 6, **the wicked/enemies/insolent/betrayer/fool/proud** (~15 — the *adversary's* inner being, still human IB, e.g. `270469 · Psa 10:6 · D105 the wicked`), `the pilgrim` 4, `the upright` 3, plus one-offs (`the prisoners`, `the sick`, `the king`, `all flesh / mankind`). The family reads the interior of the righteous and the wicked alike.

---

## 4. The motion — source(D103) / operation(D106) / target(D107) / manner(D108)

### Operation (D106, all 185 filled)
Operation carries the movement. Repeated controlled operations cluster into a few motions:
- **Devotion / disposing the seat:** `devote / dispose the heart` 14, `long / cling / keep with the soul` 7, `set the heart` — the seat *aimed* Godward.
- **Blessing / thanks / joy:** `bless the LORD` 5, `give thanks` 3, `sing for joy` 2, `be gladdened` 2.
- **Rescue / deliverance (passive, by God):** `be delivered` 4, `be saved`, `be strengthened` 2, `be satisfied/filled`.
- **Collapse:** `faint`, `fail to be fixed` 2, `be bowed/cast down`, `grow faint`, `be broken (by reproaches)`.
- **14 operations = "none"** (the seat simply named, no motion).
- A long tail (~120) are one-off *narrated* operations written as full clauses (e.g. `279759 · Psa 51:6 · D106` "the inmost seat of emotion/conscience is woven in the womb"; `270045 · Psa 107:5` "the inmost self failing under hunger"). These are read-prose in the operation field, not controlled verbs.

### Target (D107) — where the motion points
`none` 41; then a strong **Godward vector**: `toward (or against) God's word` 14 + `toward God's word` 7 + `toward God` 4 + `to the living God` 2 + `before God` 2 + `against God` 4 (the wicked's interior). Plus reflexive/interior targets `in heart` 5, `in the heart` 2, `with the whole heart` 3, `in the soul`. The rest (~90) are one-off hyphenated coinages (`death-defying-trust`, `self-summons`, `besieged-hope`) — again reader-labels, not a controlled target set.

### Source (D103) — only 8, all God, all relational
Every D103 is an `item_type=pair` edge and every one names **God as the one who moves/keeps the seat**:
`278791 · Psa 44:25 · D103` redeeming steadfast love; `279323 · Psa 49:15` ransomed from Sheol; `280100 · Psa 55:18` God redeems from the battle; `280251 · Psa 56:13` delivered from death; `281384 · Psa 66:9` kept/tested/brought out; `302640 · Psa 44:21` known by God who searches; `279650 · Psa 51:10` sustained by God's Holy Spirit; `282673 · Psa 74:8` (profaning God's dwelling). → **Source is used only when God is the mover of the interior; there is no self-originated "source" in the data.**

### Manner (D108) — 27 filled (§0.3): lament textures
`cast down and in turmoil` ×3 (the Psa 42–43 refrain), `bowed down to the dust`, `broken / shattered`, `willing / free (nadib)` (`Psa 51:12`), `right / steadfast (nakon)` (`Psa 51:10`), `from the power of Sheol`, `in safety / peace`. Manner is where the seat's *condition* (crushed vs. steadfast) is recorded.

---

## 5. Where it sits — coupling(D112) / locus(D116), corrected

After correcting the 50 swaps (§0.1): the seat is **internal in 182/185** (`internal:ib-state` 151, `internal:seat` 15, `internal:heart` 13, `internal:spirit` 3) and **external only 3×**, all `external:god`. The coupling **phrase** (D112 when unswapped, D116 when swapped) is almost always a *state-pairing*: the seat coupled to blessing (`269054 · Psa 103:1` "paired with the blessing"), to fainting/longing/hunger (`270045/270068/270070 · Psa 107`), to waiting and hope (`272824 · Psa 130:5`), to the weaned child (`272872 · Psa 131:2`), to integrity/perverseness/arrogance (`268821/268838/268851 · Psa 101`). → The interior is read as **bound to an affective/moral state**, seated **inside the self**, reaching outside itself only toward God.

---

## 6. The inner-being network — 60 genuine cross-span pair edges

Genuine `pair`/`span` edges linking to a **different** span, by dimension:
**D112 coupling 38 · D108 manner 13 · D103 source 8 · D107 target 1.** 96 distinct spans participate.

Character of the network:
- **Sparse and largely one-directional.** Only **2 reciprocal welds** exist:
  - `280392 (Psa 57:4) ↔ 280416 (Psa 57:6)` on D112 — soul/heart coupled across the psalm's turn.
  - `279650 (Psa 51:10) ↔ 279667 (Psa 51:12)` on D112 — **"create in me a clean heart" welded to "renew a right spirit"**: the clearest heart↔spirit constitutional link in the family.
- **Intra-passage laments dominate the D112 web** — the Psa 42–43 "cast-down soul" refrain links its own verses (`278509→…`, `278524→278527`, `278569→278572`), and Psa 55/56/77 chain soul↔manner↔source across adjacent verses.
- **The D103 source edges (8)** are the *God-as-mover* links of §4 — every one points the seat outward to God as redeemer/keeper.
- **D107 target has exactly one genuine edge** (`278870 · Psa 45:1 → 278872`) — the heart "overflowing with a goodly theme" toward its object; targets are otherwise flags, not links.
- Discarded as non-edges: 15 D104 self-pairs (§0.2) and 475 flag/inferred relational copies.

The network is therefore **not a dense inner-being web**; it is a scatter of **local, mostly one-way couplings within single psalms**, with two genuine heart↔spirit / soul↔heart welds standing out (Psa 51, Psa 57).

---

## 7. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings/loci:
- **Seats named** (D104 filled, 35 spans + the seat-terms themselves): **heart** (the heart itself / heart (self)), **soul** (soul (self)), **spirit** (`internal:spirit`), plus **the mouth** (`Psa 10:7` cursing) and **the inward being / hidden self** (`279759 · Psa 51:6`). Lemma inventory adds **flesh (basar)** and **kidneys / inward parts (kilyah, H3629; tuchoth, H2910)**.
- **Locus** (D116 corrected): the anatomy is **inside** (`internal:ib-state / seat / heart / spirit`, 182×); the only outward pole is **God** (`external:god`, 3×).
- **Source** (D103): the only named mover of the interior is **God** (redeems, ransoms, delivers, keeps, sustains by his Spirit, searches — 8×).
- **Coupling** (D112 phrases): the seat is bound to **states** — blessing, fainting, hunger/longing, waiting/hope, integrity/perverseness/arrogance, uprightness.

So the named anatomy is: **seat (heart / soul / spirit / flesh / inward parts / mouth) → seated internally → coupled to a moral-affective state → moved (when moved at all) by God.**

---

## 8. What could not be derived

- **Intensity (D109), specifier (D110), effect (D111): unread across all 185** — the family carries no graded intensity, no sub-specifier, and no recorded downstream effect. Any "how strong / with what result" reading is **not derivable from this source.**
- **Prohibition (D113): only 1 data point** (`Psa 44:18`, negated heart) — no basis for a prohibition pattern.
- **Seat (D104) unstated in 81%** and **manner (D108) unstated in 85%** — for most instances *where* precisely in the interior, and *in what manner*, is not recorded.
- **Source (D103) only 8 / target(D107) 41 "none" / operation 14 "none"** — for many spans the *mover* and *direction* of the seat are absent; the God-ward source is only the recorded 8.
- **D101 sense and much of D106/D107 are free-text read-phrases, not controlled values** — they support description but cannot be aggregated as categories without over-reading.
- **Bearer is inferred in 100% of cases** — no span states its bearer explicitly; every "whose interior" is a reader inference.
- **Cluster typing fails for 11 spans (NULL)** — the term-cluster cannot classify the non-seat reads (cursing, says, commit, hidden, double-minded, unfeeling, inward parts); their inner-being role is undetermined by cluster.
- **The "31 meanings" over-count the objects** — pronoun/ESV-surface fragmentation splits ~5 real seats (soul, heart, spirit, flesh, inward parts) into 31 char_keys; distinct-movement counts must not be read off the meaning count.
- **The 50-instance D112/D116 swap** means any downstream consumer reading the raw fields (uncorrected) would mis-locate the coupling/locus for 27% of the family — flagged, corrected here, but a live data-quality defect in the source.

---

## 9. Summary

The `inner-seat-heart-soul-spirit` family is a **coherent constitutional-seat movement**: 170/185 spans (92%) are M47 Constitution, naming **soul (nephesh), heart (leb/lebab/kidney), spirit (ruach), flesh (basar), inward parts** as the interior of the human self — read chiefly as an **operative faculty** (D102 faculty 92), seated **internally** (locus internal 182/185), **coupled to moral-affective states**, and **moved outward only toward/by God** (D103 source = God in all 8 filled cases; external locus = god in all 3). Its motions are **devotion/disposing the seat, blessing/thanks/joy, God-wrought rescue, and collapse/fainting**. The network is **sparse and mostly one-directional** (60 genuine edges, only 2 reciprocal welds — Psa 51 heart↔spirit, Psa 57 soul↔heart). Data defects: a **50-instance D112/D116 swap** (Books IV–V batch), **11 NULL-cluster non-seat reads + 4 M03/M12/M14 outliers** contaminating the rim, **pronoun fragmentation** inflating 31 "meanings" over ~5 real seats, **15 D104 self-pairs** that are not links, and **D109/D110/D111 entirely unread** — so intensity, sub-specifier, and effect are not derivable from this source.
