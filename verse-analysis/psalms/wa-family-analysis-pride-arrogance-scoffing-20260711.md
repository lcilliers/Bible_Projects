# Family analysis — Psalms · `pride-arrogance-scoffing`

> Source (in isolation): `verse-analysis/psalms/_base-sources/psalms__pride-arrogance-scoffing.json`. Method: `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md`. Scope: 26 meanings · 42 instances · 27 passages, all genre `poetic/wisdom`. Every claim cites `reference · span · Dnnn(label)`. Nothing outside this file has been read.

---

## 0. Data-integrity screen

### 0.1 D112(coupling) / D116(locus) field-swap — 8 instances transposed
Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. The following carry the code in **D112** and a prose phrase in **D116** (item_type `value`) — they are transposed and must be read corrected:

| # | reference · span | D112 (holds code — belongs in D116) | D116 (holds phrase — belongs in D112) |
|---|---|---|---|
| 1 | Psa 97:7 · 285690 | `internal:ib-state` | "paired with worshipping images" |
| 2 | Psa 102:8 · 269041 | `internal:ib-state` | "paired with being derided" |
| 3 | Psa 101:5 · 268848 | `internal:ib-state` | "paired with the arrogant heart" |
| 4 | Psa 138:6 · 273352 | `internal:ib-state` | "paired with the lowly he regards" |
| 5 | Psa 101:5 · 268850 | `internal:ib-state` | "paired with the haughty look" |
| 6 | Psa 102:8 · 269042 | `internal:ib-state` | "paired with the taunting" |
| 7 | Psa 89:50 · 284837 | `internal:ib-state` | "paired with bearing the insults in the heart" |
| 8 | Psa 123:4 · 272475 | `internal:ib-state` | "paired with those at ease" |

All other instances are in correct order (D116 a code, D112 a phrase/`none`), e.g. Psa 119:122 · 271359 · D112(coupling)="paired with the whole INSOLENT-foe arc", D116(locus)=`internal:ib-state`. **Read corrected: every swapped instance sits `internal:ib-state`, and its D112 coupling is the phrase now mis-filed in D116.**

### 0.2 Self-loop "edges" are not links
The overwhelming majority of entries in every `edges[]` array are self-loops: `item_type:"flag"`, `from_span:null`, `to_span` = the span's own id (bearer D105, target D107, coupling D112, and some operation D106 / manner D108 / seat D104). Per method these are **not** network edges. Genuine `pair`/`resolution:"span"` edges to a **different** span exist on only ~13 instances (see §3), and of those only **one** links two masters that both live in this file (Psa 75:4 · 282717 ↔ 282719).

### 0.3 seat(D104)=none — 41 of 42
Only **one** instance names a seat: Psa 75:5 · 282729 · D104(seat)="the neck" (inferred). All other 41 leave D104=`none`. Pride is essentially **unseated** in the structured data.

### 0.4 manner(D108)=none — 33 of 42
Filled on 9: Psa 44:8 · 278850 "continually"; Psa 52:1 · 279798 "all the day long"; Psa 42:10 · 278514 "like a deadly wound in the bones"; Psa 75:5 · 282729 "with a stiff, outstretched neck"; Psa 52:6 · 279842 "in derision"; Psa 73:6 · 282500 "as an ornament, openly displayed"; Psa 73:8 · 282512 "loftily"; Psa 74:10 · 282532 "how long? forever?"; Psa 44:13 · 278714 "derision and scorn of neighbours".

### 0.5 Absent dimensions — across all 42
**D109 (intensity), D110 (specifier), D111 (effect), D113 (prohibition) do not occur on a single instance.** Also **D103 (source) occurs on only 3** (Psa 44:8 · 278850; Psa 52:1 · 279798; Psa 59:12 · 280553) — and in all three it points not to the *origin* of the pride but to the divine counter-pole (God's past deeds / steadfast love / consuming wrath), i.e. D103 is used here as a contrast-anchor, not a causal source. **D115 (role)="characteristic" on all 42** — no `qualifier`, no `standalone`; the role dimension is uniform and therefore uninformative.

### 0.6 Cluster NULL / T2
Three meanings carry `cluster.code = null` — the term-cluster cannot type them: Psa 101:5 · 268850 (H7342 "arrogant"); Psa 123:4 · 272475 (H3238 "proud"); Psa 73:8 · 282512 (H4167 "scoff"). No T2 clusters present.

### 0.7 Outliers (is_outlier=true)
Two meanings are genuine cross-cluster: H1431 "deals insolently" → **M22(Praise)** (Psa 55:12 · 280055) and H7832 "laugh" → **M04(Joy)** (Psa 52:6 · 279842). Expected cluster for the family is M08(Pride).

---

## 1. Coherence check — the label fuses ~6 distinct IB movements

**The keyword grouping does not name one movement.** It gathers the vocabulary of height and derision, but by bearer/target/type the 42 instances split into at least six heterogeneous inner-being movements:

**(A) Active pride as a standing disposition/status of the wicked** (the core, ~M08/M16). The proud interior itself: Psa 73:6 · 282500 · D101(sense)="pride/arrogance (gaavah — pride is their necklace)"; Psa 59:12 · 280553 "pride/arrogance (gaon)"; Psa 94:2 · 285380 "proud (geeh)"; Psa 123:4 · 272475 "proud"; Psa 10:2 · 270434 "arrogant hot pursuit"; Psa 101:5 · 268848 "haughty (gaboah)" + 268850 "arrogant (rachab) heart"; Psa 138:6 · 273352 "haughty"; Psa 75:5 · 282729 "haughty neck"; Psa 17:10 · 274780 "closed to pity, arrogant"; Psa 73:3 · 282484 "arrogant/boastful (halal)"; the 7 Psa-119 + Psa 86:14 "insolent (zed)" spans (271359, 271722, 271899, 272009, 272080, 272124, 284281). D102(type) here is `disposition` or `status`.

**(B) The verbal aggression *from* the proud** — taunt / scoff / mock / deride as an outward act (clustered **M06 Hate**, and M16). Psa 74:10 · 282532 · D106(operation)="scoff/reproach", D107(target)="God"; Psa 89:51 · 284845 + 284848 "mock (charaph)" → God / the anointed's steps; Psa 73:8 · 282512 "scoff/mock (muq)"; Psa 119:51 · 271901 "deride (luts)"; Psa 119:42 · 271836, Psa 42:10 · 278514, Psa 55:12 · 280051 "taunt (charaph)". These are D102(type)=`action` directed at a target — not a disposition of the psalmist.

**(C) The *reception* of derision — a status of disgrace borne by the sufferer** (recipient IB). Psa 102:8 · 269041 · D101="be taunted (charaph)" + 269042 "be derided (halal)"; Psa 89:50 · 284837 "be mocked (cherpah)"; Psa 44:13 · 278714 "reproach/taunt (cherpah)", D105(bearer)="the nation (made a taunt)". D102(type)=`state`/`status`; these are conditions imposed from outside, borne "in my heart" (Psa 89:50 · 284837 · D114). See §5 — the *interior* content of these is thin.

**(D) Right / God-directed boasting — opposite valence.** Psa 44:8 · 278850 · D101="boast/glory (halal)", D116(locus)=`external:god`, D103(source)="grounded in God's past saving deeds". This is the inverse of pride (glorying *in God*), swept into the family only by the shared root *halal*.

**(E) Reflexive self-guarding against pride** (first-person IB resisting pride in itself). Psa 19:13 · 275270 · D101="kept from presumptuous sin", D102(type)=`volition`, D105(bearer)="the psalmist".

**(F) Derisive laughter as vindication, not pride** (outlier M04 Joy). Psa 52:6 · 279842 · D101="laugh/deride (sachaq)", D105(bearer)="the righteous", D114 explicitly "not cruelty but the vindication of justice".

**Finding:** the family is a *lexical* set (height/derision words), not a single IB movement. Movements A (self-exaltation), B (mockery outward), C (disgrace received), D (right boasting in God), E (self-guarding), F (righteous vindication) are distinct — some are opposite in valence. Any downstream synthesis must not read them as one process.

---

## 2. The movements evidenced, dimension by dimension

### 2.1 What the words *are* (D101/D102)
Nouns of the proud state (`status`): "pride" (Psa 73:6 · 282500; Psa 59:12 · 280553), "proud" (Psa 94:2 · 285380; Psa 123:4 · 272475), "insolent/zed" (all 7 H2086 spans, `status`), "haughty" (Psa 138:6 · 273352; Psa 75:5 · 282729), "boastful" (Psa 75:4 · 282717), "arrogant (halal)" (Psa 73:3 · 282484), "taunt (cherpah)" (Psa 44:13 · 278714). Dispositions (`disposition`): "arrogance" (Psa 10:2 · 270434), "arrogant heart" (Psa 101:5 · 268850), "haughty look" (Psa 101:5 · 268848), "arrogant (rachab/athaq/proud)" (Psa 140:5 · 273636; Psa 94:4 · 285410), "boasts of his soul's desire" (Psa 10:3 · 270443), "arrogantly" (Psa 17:10 · 274780). Acts (`action`): the boasting/mocking/taunting/scoffing/deriding/laughing verbs (§1 B, D, F). States received (`state`): being taunted/derided/mocked (Psa 102:8 · 269041, 269042; Psa 89:50 · 284837). Volition (`volition`): Psa 19:13 · 275270.

### 2.2 Whose IB — bearer (D105, all inferred)
Three bearer-classes: **the proud/wicked/foes** (majority — "the wicked" Psa 10:3 · 270443, "the proud" Psa 94:2 · 285380, "the insolent" ×7, "the enemies" Psa 17:10 · 274780 / Psa 89:51 · 284845, "the idolaters" Psa 97:7 · 285690, "the rich" Psa 49:6 · 279393, "the tyrant" Psa 52:1 · 279798); **the sufferer / God's people** (recipient — "the psalmist" Psa 102:8 · 269041, "the servants of God" Psa 89:50 · 284837, "the nation" Psa 44:13 · 278714, and the first-person guarder Psa 19:13 · 275270, and the God-boasting nation Psa 44:8 · 278850); **the righteous** (Psa 52:6 · 279842). All bearers are human/human-group — the Screen-0 IB test passes throughout (targets, not bearers, are God: Psa 74:10 · 282532 · D107="God"; Psa 89:51 · 284845 · D107="God").

### 2.3 What it does — operation / target (D106/D107)
Pride is repeatedly read as *expressing itself in predation and speech*: Psa 10:2 · 270434 · D106="pride expressed as predatory chase"; Psa 140:5 · 273636 · D106="pride expresses itself as covert trap-setting"; Psa 94:4 · 285410 · D106="speak arrogantly"; Psa 75:5 · 282729 · D106="speak with arrogance". Targets, where directed, are the weak (Psa 123:4 · 272475 · D107="the afflicted"), God's people (Psa 94:2 · 285380 · D107="against God's people"), the psalmist (Psa 119:51 · 271901), or God himself (Psa 74:10 · 282532; Psa 89:51 · 284845). Several targets are reflexive/abstract place-holders rather than real objects — "self-glorying-greed" (Psa 10:3 · 270443), "merciless-arrogance" (Psa 17:10 · 274780), "proud entrapment" (Psa 140:5 · 273636), "arrogance" (Psa 10:2 · 270434) — flagged in §5 as non-derivable targets. D106(operation)=`none` on Psa 73:3 · 282484 and Psa 44:13 · 278714; D107=`none` on several (Psa 75:4 · 282717/282719; Psa 73:3 · 282484; Psa 59:12 · 280553; Psa 44:13 · 278714).

### 2.4 Coupling / locus (D112/D116, corrected)
Corrected loci: most instances `internal:ib-state`; `external:god` on the God-directed items (Psa 44:8 · 278850; Psa 89:51 · 284845/284848); `external:person` on the person-directed taunts (Psa 119:42 · 271836; Psa 55:12 · 280051, 280055; Psa 119:51 · 271901; Psa 52:6 · 279842). Couplings (D112, phrase) bind pride to its companion sins and to the foil: "paired with violence covering them" (Psa 73:6 · 282500), "the sin of their mouths and cursing" (Psa 59:12 · 280553), "paired with trusting in wealth" (Psa 49:6 · 279393), "hidden-snare" (Psa 140:5 · 273636), "the same wicked whose prosperity is described" (Psa 73:3 · 282484), and (right-boast) "paired with giving thanks" (Psa 44:8 · 278850).

---

## 3. The network (genuine `pair`/span edges only)

Removing self-loops (§0.2), the genuine inter-span edges are:

- Psa 44:8 · 278850 — D103(source)→278843, D112(coupling)→278852
- Psa 49:6 · 279393 — D112(coupling)→279391
- Psa 52:1 · 279798 — D103(source)→279801, D107(target)→279799
- **Psa 75:4 · 282717 ↔ 282719** — D106(operation) 282717→282719 and D112(coupling) 282717→282720, 282719→282717 (the boastful ↔ the boasting; **the only edge whose both endpoints are masters in this file**)
- Psa 73:3 · 282484 — D112(coupling)→282487
- Psa 55:12 · 280051 — D112(coupling)→280052; · 280055 — D112(coupling)→280054
- Psa 75:5 · 282729 — D104(seat)→282730, D108(manner)→282730, D112(coupling)→282722
- Psa 52:6 · 279842 — D112(coupling)→279841
- Psa 59:12 · 280553 — D103(source)→280559, D112(coupling)→280548
- Psa 73:6 · 282500 — D112(coupling)→282502
- Psa 73:8 · 282512 — D107(target)→282514, D112(coupling)→282514
- Psa 74:10 · 282532 — D112(coupling)→282534
- Psa 44:13 · 278714 — D108(manner)→278716

**The network is sparse and outward-pointing.** Except the single Psa 75:4 pair, every genuine edge targets a span **not present among this file's 42 masters** (e.g. 278843, 279801, 282720, 280559, 282514) — i.e. companion spans in the same verse that lie outside the family. So *within the family's own scope* the network is effectively one 2-node bidirectional link (Psa 75:4) plus a set of leaves whose far end is not describable from this file. No hub, no chain, no cross-passage bridge is expressible here.

---

## 4. The interior anatomy the data actually names

Assembling only the **filled** D103/D104/D112:

- **Seat (D104):** only "**the neck**" (Psa 75:5 · 282729) — the stiff-necked speaker. Nothing else. Heart, eye/look, mouth, tongue, soul appear in verse text and in D114 discovery notes (e.g. "arrogant heart" Psa 101:5 · 268850 · D114; "hearts overflow" implied in the Psa 73 passage text; "haughty look" Psa 101:5 · 268848 · D114) **but are not captured in the seat dimension** — the structured interior of pride is, on this data, almost empty (see §5).
- **Source (D103):** three, all the divine counter-pole — God's past saving deeds (Psa 44:8 · 278850), God's enduring steadfast love (Psa 52:1 · 279798), God's consuming wrath (Psa 59:12 · 280553). The *origin* of pride is nowhere given a D103.
- **Coupling (D112, corrected):** pride is bound to violence (Psa 73:6 · 282500), to lying/cursing speech (Psa 59:12 · 280553), to trust in wealth (Psa 49:6 · 279393), to concealed snares (Psa 140:5 · 273636), to prosperity (Psa 73:3 · 282484); right-boasting is bound to thanksgiving (Psa 44:8 · 278850). This is the richest filled dimension and carries most of the anatomy.

---

## 5. What could not be derived (flags)

1. **Seat is unusable as anatomy** — 41/42 D104=`none` (§0.3). The bodily/interior seats of pride (heart, eye, mouth, neck) live only in D114 notes and verse text, not the seat field. The one filled seat (neck, Psa 75:5 · 282729) is inferred.
2. **No intensity / specifier / effect / prohibition** anywhere (D109/D110/D111/D113 absent, §0.5) — the data cannot say how strong, of what particular kind, to what consequence, or under what prohibition any pride-movement runs.
3. **Source is a foil, not an origin** — the 3 D103 fields anchor the divine contrast, so the *genesis* of pride in the IB is not derivable.
4. **Placeholder targets** — several D107 values are abstract restatements, not objects ("self-glorying-greed" Psa 10:3 · 270443; "merciless-arrogance" Psa 17:10 · 274780; "proud entrapment" Psa 140:5 · 273636; "boasting" Psa 94:4 · 285410; "arrogance" Psa 10:2 · 270434). Treat as non-derivable targets.
5. **Reception items have thin interior content** — "be taunted/derided/mocked" (Psa 102:8 · 269041, 269042; Psa 89:50 · 284837; Psa 44:13 · 278714) are external conditions imposed on the sufferer; their claim to be an *inner-being* movement rests only on Psa 89:50's "bear in my heart the insults" (D114). Role=`characteristic` is asserted but the IB content is largely the disgrace-status, not an interior operation.
6. **Role dimension carries no information** — all 42 = "characteristic" (§0.5); it cannot discriminate.
7. **8 swapped D112/D116 pairs** (§0.1) — corrected here, but flagged as a systematic source defect (note the swap clusters on the M06/M08 status-words; it is not random).
8. **3 untyped meanings** (NULL cluster, §0.6) — "arrogant" (H7342, Psa 101:5 · 268850), "proud" (H3238, Psa 123:4 · 272475), "scoff" (H4167, Psa 73:8 · 282512) cannot be cluster-placed from this file.
9. **Network is not derivable within scope** — every genuine edge but one points outside the 42 masters (§3); the family's internal web cannot be reconstructed here.

---

## 6. Summary

The `pride-arrogance-scoffing` family is a **lexical bundle of height/derision words, not one inner-being movement**: it fuses (A) the wicked's self-exalting disposition, (B) their outward mockery, (C) the sufferer's received disgrace, (D) right boasting *in God* (opposite valence), (E) the psalmist's self-guarding against presumption, and (F) the righteous' vindicating laughter (both D/E/F swept in by shared roots *halal*/*sachaq*). The structured anatomy is thin — pride is essentially **unseated** (41/42 seat=none; only "the neck"), has **no intensity/specifier/effect/prohibition**, and its **source** field records only the divine counter-pole. Its one rich dimension is **coupling**, which binds pride to violence, lying speech, wealth-trust, and concealed snares. The **network is sparse and outward-pointing** — a single intra-family pair (Psa 75:4 · 282717 ↔ 282719); all else leaves the file. Eight instances carry a **D112/D116 field-swap** (corrected herein), three meanings are **cluster-NULL**, and two are **genuine outliers** (M22 Praise, M04 Joy).
