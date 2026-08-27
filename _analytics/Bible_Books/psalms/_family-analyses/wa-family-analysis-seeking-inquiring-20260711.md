# Family analysis — Psalms `seeking-inquiring` (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__seeking-inquiring.json` only. Scope: 9 meanings · 37 instances · 28 passages. Every claim cites `reference · span · Dnnn(label)` into that file. Discovery notes cited as D114.

Lexical spread (from `evidence.stems` / `read_sense_variants`): **baqash** H1245 (15: 14 `seek` + 1 `sought`), **darash** H1875 (18: 13 `seek` + 4 `sought` + 1 `studied`), **shachar** H7836 (2), **chalah** H2470 (1), **yaats** H3289 (1). Term-clusters: **M41 Remembrance** ×35, **M15 Wisdom** ×1 (Psa 83:3), **M03 Grief** ×1 (Psa 45:12). No `is_outlier=true` records; no null/T2 clusters.

---

## 0. Data-integrity screen

### 0.1 D112(coupling)/D116(locus) field-swap
Correct order = D116 a code, D112 a phrase. **Five instances are transposed** — D112 holds an `external:` code and D116 holds a prose phrase:

| ref · span | D112(coupling) as stored | D116(locus) as stored | corrected reading |
|---|---|---|---|
| Psa 105:3 · 269475 | `external:god` | "paired with the rejoicing heart" | locus=external:god; coupling=rejoicing heart |
| Psa 105:4 · 269497 (baqash) | `external:god` | "paired with seeking his strength" | locus=external:god; coupling=seeking his strength |
| Psa 122:9 · 272439 | `external:person` | "paired with the sake of brothers and God's house" | locus=external:person; coupling=brothers/God's house |
| Psa 105:4 · 269494 (darash) | `external:god` | "paired with seeking his presence" | locus=external:god; coupling=seeking his presence |
| Psa 111:2 · 270586 | `external:god` | "paired with delighting in them" | locus=external:god; coupling=delighting in the works |

All other instances carry D112 as a phrase and D116 as a code (correct order), e.g. Psa 27:4 · 276264 · D112(coupling)="one-thing-I-ask" / D116(locus)="internal:ib-state".

### 0.2 Self-loop "edges" are not network links
Every instance's `edges` array is dominated by self-loops (`from_span:null`, `to_span`=own id, `resolution:"inferred"`) on D105 bearer, D107 target, and sometimes D106 operation / D108 manner. Per method these are **not** network edges. Genuine `pair`/`span` edges (to a different span) exist on only 11 instances (§ Network).

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" on all 37 instances** — the anatomy's seat dimension is never filled anywhere in the family, though verse text repeatedly names heart/soul (see §Interior anatomy, and note this as a derivation gap).
- **D108 manner = "none" on 33 of 37.** Filled only 4×: Psa 63:1 · 281014 · D108(manner)="earnestly, at first light"; Psa 77:2 · 282941 · D108(manner)="hand stretched out untiring through the night"; Psa 45:12 · 278902 · D108(manner)="with gifts"; Psa 71:24 · 282169 · D108(manner)="put to shame and disappointed".

### 0.4 Absent dimensions (across all 37)
- **D109 intensity — absent everywhere.**
- **D110 specifier — absent everywhere.**
- **D111 effect — absent everywhere.**
- **D113 prohibition — absent everywhere.**
- **D103 source — present once only:** Psa 53:2 · 279903 · D103(source)="the object of God's looking down from heaven (v2)".
- **D112 coupling = "none" once:** Psa 45:12 · 278902 · D112(coupling)="none".

### 0.5 Cluster null / T2
None. All records typed (M41 ×35, M15 ×1, M03 ×1). Note the cross-family oddity that a *seeking* family maps overwhelmingly to **M41 Remembrance**, with the two non-M41 records being the two non-God-seeking verbs (yaats "consult", chalah "entreat favour").

### 0.6 Other integrity notes
- **D116 semantic inconsistency:** locus conflates "where it sits" (`internal:ib-state`) with "what it is directed at" (`external:god`, `external:person`). These are different axes stored in one field.
- **Psa 86:14 · 284286 · D116(locus)="internal:ib-state"** for the *enemies* seeking the psalmist's life — inconsistent with the parallel hostile-seek records Psa 54:3 · 279985 and Psa 70:2 · 282005, which carry D116="external:person". Probable mislabel.
- **Role uniform:** D115 role = "characteristic" on **all 37** — no qualifier/standalone differentiation is recoverable, even where the content is qualifier-like (e.g. the divine search of Psa 53:2 · 279903).

---

## 1. Coherence — does the label fit its data?

**Finding: lexically coherent, movement-wise fused.** All 9 meanings are seek/inquire verbs, but they carry at least **six distinct inner-being movements of opposite valence** under one keyword. The file itself flags this: the *same verb* baqash bears "seek God (blessed)" and "seek my life (deadly)" — Psa 70:4 · 282019 · D114 "the same verb, opposite ends"; Psa 70:2 · 282005 · D114 "two kinds of seeking, one deadly, one blessed"; Psa 63:9 · 281080 · D114 "the dark mirror of his own seeking (shachar) of God".

Distinct movements (with counts + representative citations):

1. **Godward seeking / longing** (the dominant genuine IB pursuit) — ~25 instances. E.g. Psa 27:4 · 276264 · D106(operation)="the self reduces all its desire to one thing… longing consolidated onto a single object"; Psa 63:1 · 281014 · D101(sense)="seek early / earnestly (shachar)"; Psa 34:4 · 277244 · D101(sense)="I sought the LORD, freed from fears"; Psa 119:2 · 271711, Psa 119:10 · 271203 (whole-heart seeking).
2. **Predatory / hostile seeking** (enemies hunt the life/hurt — external malice, not longing) — 6 instances: Psa 54:3 · 279985, Psa 63:9 · 281080, Psa 70:2 · 282005, Psa 71:13 · 282056, Psa 71:24 · 282169, Psa 86:14 · 284286. E.g. Psa 54:3 · 279985 · D114 "the deadly pursuit… the enemies' settled aim to take his life".
3. **Failure / refusal to seek** (the wicked) — 2 instances: Psa 10:4 · 270453 · D101(sense)="pride crowds God out" (D102 type="cognition"); Psa 119:155 · 271554 · D101(sense)="seek (darash, negated)" (D102 type="disposition"), D106(operation)="fail to seek".
4. **Seeking peace / a city's good** — 2 instances: Psa 34:14 · 277173 · D106(operation)="an active chase after peace"; Psa 122:9 · 272439 · D107(target)="the good of Jerusalem".
5. **Enemy consulting / plotting** (yaats, M15 Wisdom) — 1: Psa 83:3 · 283998 · D106(operation)="take counsel together", D107(target)="against God's hidden ones".
6. **Seeking a human's favour** (chalah, M03 Grief) — 1: Psa 45:12 · 278902 · D101(sense)="seek favour / entreat (chalah)", D107(target)="the queen (her favour)".

A seventh borderline case: **enemies driven to seek God's name** (hoped conversion) — Psa 83:16 · 283971 · D114 "that even the foes' humbling might bend them to seek God".

The label thus groups the God-seeking *disposition* together with its predatory homonym and its negation. This is the family's central finding: seeking here is a directed vector whose meaning is fixed only by its target (D107), not by the verb.

---

## 2. The movements / operations evidenced

### 2.1 Godward seeking — the consolidating longing
The strongest reads make seeking a gathering and narrowing of desire. Psa 27:4 · 276264 · D102(type)="volition", D106(operation)="the interior's many desires collapse into the desire to behold God"; D114 "the gathering of all wants into one". Psa 63:1 · 281014 · D102="action", D108(manner)="earnestly, at first light", D112(coupling)="the seeking expressed as thirst and fainting" (pair→281016) — seeking as bodily thirst. Psa 77:2 · 282941 · D108(manner)="hand stretched out untiring through the night", D112(coupling)="paired with the soul that refuses comfort" (pair→282949) — persistence against un-comfort.

### 2.2 Seeking as the mark of a people / the reciprocated pursuit
Psa 24:6 · 275911 · D106(operation)="a whole company oriented to seeking him", D114 "defines a people by the direction of its desire". Psa 14:2 · 274526 · D102="volition", D114 "what makes a person not-a-fool"; its twin Psa 53:2 · 279903 · D103(source)="the object of God's looking down from heaven" — the one dimensioned *source* in the family: God's gaze is what the seeking is object of.

### 2.3 Seeking rewarded — the answered vector
Psa 34:4 · 277244 · D102="affect", D106(operation)="the turning-to-God that empties the interior of its fears". Psa 34:10 · 277140 · D102="affect", D107(target)="satisfied-seeking", D114 "the interior that seeks God wants for nothing good". Psa 22:26 · 275715 · D102="affect", D106="seeking rewarded with life". Psa 40:16 · 278285 · D102="affect", D106 "seeking that ends in joyful praise".

### 2.4 Seeking God's word (the Psa 119 arc)
Six Psa 119 instances read seeking as pursuit of the word: 119:2 · 271711, 119:10 · 271203, 119:45 · 271860, 119:94 · 272195 (all D107(target)="God's word"), and the negated 119:155 · 271554 (wicked "do not seek your statutes"). All carry D112(coupling)="paired within its char-arc across the psalm" (flag, inferred) — i.e. no resolved cross-span link.

### 2.5 Predatory seeking (the hostile pole)
Psa 54:3 · 279985 · D101(sense)="seek / hunt (baqash - seek my life)", D107(target)="my life (nefesh)" (pair→279986), D112(coupling)="the murderous intent of the ruthless men" (pair→279984). Psa 70:2 · 282005, Psa 71:13 · 282056, Psa 86:14 · 284286 (D114 "the murderous intent of the godless"). These are external acts (bearers "the enemies"/"ruthless men"); their inclusion under an IB family is only by verb identity.

### 2.6 The refusal / absence of seeking
Psa 10:4 · 270453 · D102(type)="cognition", D106(operation)="a mind so full of self that God is simply absent from every calculation", D107(target)="practical-atheism", D112(coupling)="no-room-for-God". Psa 119:155 · 271554 · D102="disposition" — the wicked's non-seeking as cause of distance from salvation.

### 2.7 Compelled seeking
Psa 78:34 carries two spans for one clause: 283157 (darash) · D114 "the seeking that only the sword could compel" and 283159 (shachar) · D101(sense)="seek earnestly", D114 "the eager, early seeking under the rod of judgment". Seeking here is extracted by affliction, not free longing.

### 2.8 Non-God targets
Psa 34:14 · 277173 · D106(operation)="the interior does not merely wish peace but hunts it" (target peace). Psa 45:12 · 278902 (chalah) · seeking a human's favour with gifts. Psa 83:3 · 283998 (yaats) · enemy deliberation. Psa 111:2 · 270586 · D101(sense)="study (darash)", D106="study / seek out", D107="the works of the LORD" — seeking as *inquiry* (the "inquiring" half of the label), the only clearly cognitive-investigative read.

### 2.9 Type (D102) distribution
action (majority) · volition ×5 (27:4·276264, 34:14·277173, 14:2·274526, 24:6·275911, 9:10·285879) · affect ×4 (40:16·278285, 22:26·275715, 34:10·277140, 34:4·277244) · cognition ×1 (10:4·270453) · disposition ×1 (119:155·271554).

---

## 3. The network (genuine `pair`/`span` edges only)

Eleven instances carry real edges; the rest are self-loops (§0.2). Most edges point to **companion spans in the same verse that are not part of this family** (their content is not in this file — noted "external endpoint").

| from (ref · span) | dim | to_span | intra-family? |
|---|---|---|---|
| Psa 53:2 · 279903 | D103 source | 279893 | no (God's looking-down) |
| Psa 53:2 · 279903 | D112 coupling | 279902 | no (understanding) |
| Psa 54:3 · 279985 | D107 target | 279986 | no (nefesh/"my life") |
| Psa 54:3 · 279985 | D112 coupling | 279984 | no (murderous intent) |
| Psa 63:1 · 281014 | D112 coupling | 281016 | no (thirst/fainting) |
| **Psa 63:9 · 281080** | D107 target | 281082 | no (destroy-life) |
| **Psa 63:9 · 281080** | **D112 coupling** | **281014** | **YES → Psa 63:1 shachar (the "dark mirror")** |
| Psa 69:6 · 281889 | D112 coupling | 281883 | no (those who hope) |
| Psa 69:32 · 281841 | D112 coupling | 281845 | no (hearts revive) |
| Psa 70:2 · 282005 | D107 target | 282006 | no |
| Psa 70:2 · 282005 | D112 coupling | 282010 | no (delight-in-hurt) |
| Psa 70:4 · 282019 | D112 coupling | 282020 | no (rejoicing/gladness) |
| **Psa 71:13 · 282056** | D107 target | 282058 | no (hurt) |
| **Psa 71:13 · 282056** | **D112 coupling** | **282169** | **YES → Psa 71:24 (reciprocal)** |
| **Psa 71:24 · 282169** | **D112 coupling** | **282056** | **YES → Psa 71:13 (reciprocal)** |
| Psa 71:24 · 282169 | D107 target | 282170 | no (hurt) |
| Psa 77:2 · 282941 | D112 coupling | 282949 | no (soul refuses comfort) |

**Network shape:** essentially a set of parallel monads. Only **two intra-family links** exist: (1) Psa 63:9 · 281080 → Psa 63:1 · 281014 — one-directional, hostile-seek pointing at God-seek (the explicit antithesis); (2) Psa 71:13 · 282056 ↔ Psa 71:24 · 282169 — a reciprocal pair binding the enemies' "seek my hurt" to its shamed answer at the psalm's close. Every other edge reaches a companion span outside the family whose text this file does not carry; those endpoints are **not derivable here**.

---

## 4. The interior anatomy the data actually names

Assembling only the *filled* dimensions:

- **Seat (D104): none — never named** (37/37 "none"). The family gives no interior organ for seeking. (Verse text names heart at 119:2, 119:10, 105:3, 22:26, 69:32, 27:4/27:8 and soul at 63:1, 77:2, but the D104 field does not capture it — see §5.)
- **Bearer (D105): always inferred, human throughout** — "the worshippers", "the psalmist", "those who seek", "the wicked", "the enemies"/"ruthless men", "those who delight", "the people of Tyre". No bearer is span-resolved.
- **Source (D103):** named once — Psa 53:2 · 279903 (God's downward look).
- **Operation (D106):** seek / seek-hunt / seek-resort-to / seek-earnestly / study-seek-out / take-counsel / fail-to-seek, plus expanded event-clauses of consolidation (27:4·276264), satisfaction (34:10·277140), and absence (10:4·270453).
- **Target (D107):** the polarising dimension — God / God's presence·face·name / God's word·precepts·statutes·works / the psalmist's life·hurt / peace / the city's good / a human's favour / practical-atheism / consolidated-longing.
- **Manner (D108):** filled 4× only (§0.3) — dawn-earnestness (63:1), untiring night-reaching (77:2), gifts (45:12), shame (71:24).
- **Coupling (D112, corrected):** binds seeking to the rejoicing/reviving heart (105:3, 69:32), to thirst/fainting (63:1), to the soul refusing comfort (77:2), to hope (69:6), to understanding (53:2), to repenting (78:34), and — at the hostile pole — to murderous intent (54:3) and to its own shamed answer (71:13↔71:24).
- **Locus (D116, corrected):** `internal:ib-state` for the reflexive/consolidating reads (27:4, 34:14, 22:26, 24:6, 34:10, 34:4, 14:2, 9:10, 10:4) vs `external:god` / `external:person` for target-directed reads — the axis is unstable (§0.6).
- **Role (D115):** "characteristic" uniformly.

---

## 5. What could not be derived

- **Seat** — the whole family (37/37) leaves D104 "none"; the heart/soul that the verse text names for seeking is not carried into the anatomy dimension.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — absent on every instance; no gradation, no negation-flag, no consequence dimensioned. (The reward/answer of seeking is present only inside D106 prose and D114 notes, never as D111 effect.)
- **Source (D103)** — dimensioned only once (53:2); what moves the seeking is otherwise unstated.
- **Manner** — unstated for 33 of 37.
- **Bearer identity** — always inferred, never span-anchored; "the psalmist"/"the enemies" not resolved to a person-span.
- **The network's far endpoints** — the paired target/coupling spans (279986 nefesh, 279902 understanding, 281883 hope, 281016 thirst, 282020 gladness, 281845 hearts-revive, etc.) are referenced by id but their content is outside this file; the couplings are describable only by the pointing note, not the pointed-to span.
- **Qualifier/standalone role** — flattened to "characteristic" everywhere; the qualifier-like divine gaze (53:2) cannot be distinguished on D115.
- **Corrupted locus/coupling** on 5 swapped instances (§0.1) is readable only after correction.
- **Cross-valence unification** — the file gives no dimension that separates "seek God" from "seek my life"; the distinction lives only in D107 target and D114 discovery notes, not in any typed field.

---

## Summary
`seeking-inquiring` is **lexically one family, motionally at least six** — a Godward longing (dominant, ~25), a predatory hunt of the life (6), a wicked refusal to seek (2), plus peace-seeking, enemy-plotting, and human-favour-seeking outliers. Seeking is a directed vector whose valence is set entirely by its **target (D107)**, not its verb: the same baqash blesses and kills (explicit at 70:2·282005·D114, 70:4·282019·D114). The anatomy is thin — **seat never named, D109/D110/D111/D113 wholly absent, source once, manner 4×** — and the **network is near-empty** (two intra-family links: 63:9→63:1 and 71:13↔71:24; all else self-loops or external endpoints). Integrity: **5 D112/D116 swaps** (105:3, 105:4×2, 122:9, 111:2), one coupling="none" (45:12), one probable locus mislabel (86:14), and a uniformly flattened D115="characteristic".
