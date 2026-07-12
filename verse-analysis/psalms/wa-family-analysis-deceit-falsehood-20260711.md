# Family analysis — `deceit-falsehood` (Psalms), in isolation

> Source: `verse-analysis/psalms/_base-sources/psalms__deceit-falsehood.json` only. 29 meanings · 45 instances · 31 passages. Genre = poetic/wisdom throughout. All citations are `reference · span_id · Dnnn(label)` into that file. D114 discovery notes cited as source.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling)/D116(locus) field-swap
Correct order = D116 holds a code (`internal:`/`external:`), D112 holds a phrase. **13 instances are transposed** (D112 carries the `internal:ib-state` code, D116 carries a "paired with…" prose phrase):

| span_id | reference | D112 (holds code) | D116 (holds phrase) |
|---|---|---|---|
| 270096 | Psa 108:12 | internal:ib-state | paired with doing valiantly through God |
| 272606 | Psa 127:1 | internal:ib-state | paired with the watchman's vain vigil |
| 272613 | Psa 127:1 | internal:ib-state | paired with the builders' vain toil |
| 272614 | Psa 127:2 | internal:ib-state | paired with the anxious bread and God's gift of sleep |
| 270230 | Psa 109:2 | internal:ib-state | paired with the wicked and lying mouths |
| 272308 | Psa 120:2 | internal:ib-state | paired with the lying lips |
| 272314 | Psa 120:3 | internal:ib-state | paired with the judgment it invites |
| 268873 | Psa 101:7 | internal:ib-state | paired with the deceit expelled |
| 270235 | Psa 109:2 | internal:ib-state | paired with the deceit |
| 272305 | Psa 120:2 | internal:ib-state | paired with the deceitful tongue |
| 268867 | Psa 101:7 | internal:ib-state | paired with the liar expelled |
| 307629 | Psa 116:11 | internal:ib-state | paired with the alarm |
| 268844 | Psa 101:5 | internal:ib-state | paired with being destroyed by the king |

Read corrected: for these 13, the **locus is `internal:ib-state`** and the **coupling is the prose phrase**. All 13 are otherwise the "self-loop-only" instances (§0.2) — the swap co-occurs with the aggregate/inferred profile.

Note three instances (`277520` Psa 36:2 D112(coupling)="flatter-himself"; `279472` Psa 4:8 D112="sleep-in-safety"; `274626` Psa 15:3 D112="no-slander") carry a hyphen-slug phrase in D112 and a code in D116 — these are **correctly ordered** (D112 phrase, D116 code) and are NOT counted as swaps.

### 0.2 Self-loop "edges" are not real links
Every instance's `edges[]` array is dominated by self-loops: `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's own id (bearer/target/coupling/seat/operation). These are **not network links** and are discarded for the network (§ The network). Only `pair` edges (`resolution:"span"`) to a **different** span are genuine.

### 0.3 seat(D104) / manner(D108) unfilled
- **D104 seat = "none" in 43 of 45.** Filled only twice, both inferred: `279825 · Psa 52:4 · D104(seat)="the tongue"` and `280556 · Psa 59:12 · D104(seat)="the mouth"`.
- **D108 manner = "none" in 44 of 45.** Filled only once: `279816 · Psa 52:3 · D108(manner)="more than speaking righteousness"` (pair).

### 0.4 Absent dimensions
- **D109 intensity — absent across all 45.**
- **D110 specifier — absent across all 45.**
- **D111 effect — absent across all 45.**
- **D113 prohibition — present in 1 only:** `278742 · Psa 44:17 · D113(prohibition)="negated ('we have NOT been false to your covenant')"`.

### 0.5 Cluster NULL / T2 (term-cluster cannot type them)
- **Cluster fully null (code, name, all_candidates all null) — 4:** `283817 · Psa 81:15` (cringe, H3584); `306806 · Psa 78:36` (flattered, H6601); `279472 · Psa 4:8` (lie down, H7901); `280556 · Psa 59:12` (lies, H3585).
- **Cluster null but `all_candidates="T2(Supplementary)"` — 2:** `277520 · Psa 36:2` (flatters, H2505); `274626 · Psa 15:3` (slander, H7270). Per method, T2 = qualifier/reference-only; these cannot stand as a typed M-cluster.
- **Declared outliers (`is_outlier:true`) — 2:** `278742 · Psa 44:17` (H8266 false) → cluster **M13(Truth)**, not M14; `268844 · Psa 101:5` (H3960 slanders) → cluster **M42(Speech)**, not M14.
- The remaining 37 instances carry an M-cluster: **M14(Deceit)** dominant, plus **M06(Hate)** ×1 (`271608` abhor), **M10(Sin)** ×3 (`283331`, `282391`, `280630`).

### 0.6 role
**D115(role)="characteristic" for all 45.** No qualifier, no standalone anywhere.

---

## 1. Coherence — does the label fit its data?

**Partly. The core coheres; the keyword bucket has fused at least four distinct inner-being movements.** "deceit-falsehood" is an ESV-keyword grouping and it has pulled in English homographs and mere associations.

**Coherent core (majority, ~26 instances) — the lying tongue of the wicked/foe.** mirmah, sheqer, remiyyah, kazab, kachash, lashan realised as deceitful/lying mouths, tongues, lips, false accusation and fraud — e.g. `270230 · Psa 109:2 · D101(sense)="deceitful (mirmah)"`; `271609 · Psa 119:163 · D101="falsehood / false way (sheqer)"`; `279811 · Psa 52:2 · D101="deceit / treachery (remiyyah - working deceit)"`; `280044 · Psa 55:11 · D101="fraud / deceit (mirmah)"`; `280491 · Psa 58:3 · D101="lies / falsehood (kazab)"`. This is a single, tight movement and fully justifies the label.

**Fused-in movement A — FUTILITY / vanity (shav), not falsehood (homograph "vain/vanity").** The whole H7723 group reads as futility of human effort or human frailty, not lying: `272606 · Psa 127:1 · D106(operation)="labour in vain"`, `272613 · Psa 127:1 · D106="keep watch in vain"`, `272614 · Psa 127:2 · D106="toil anxiously in vain"`, `270096 · Psa 108:12 · D106="reckon human help vain"`, `284803 · Psa 89:47 · D101(sense)="vanity (shav)"` / `D114`="frailty and fleetingness of human life". The DB nonetheless files them M14(Deceit). Only `271326 · Psa 119:118 · D114`="the vain deceit of the strayers" (H8267 sheqer, "their cunning is in vain") genuinely bends toward deceit. **This strand is really futility/trust, mis-bucketed by the English word "vain".**

**Fused-in movement B — REST / security (homograph "lie down").** `279472 · Psa 4:8 · D101(sense)="in peace lie down and sleep"`, `D102(type)="state"`, `D114`="sleep is the body's confession of security in God". H7901 (recline) has nothing to do with H-lie (falsehood); cluster null. **Outright homograph artefact — it is the opposite pole (trust), not deceit.**

**Fused-in movement C — covenant-faithlessness / betrayal (bagad, shaqar).** Relational treachery toward God/people, distinct from verbal lying: `283331 · Psa 78:57 · D101="act treacherously (bagad)"` (M10 Sin); `282391 · Psa 73:15 · D101="betray / deal faithlessly (bagad)"` — the psalmist's *avoided* betrayal (M10 Sin); `280630 · Psa 59:5 · D101="deal treacherously (bagad)"` (M10 Sin); `278742 · Psa 44:17 · D101="be false / deal falsely (shaqar - to your covenant, negated)"` (M13 Truth, outlier). Betrayal of relationship ≠ the lying-tongue movement, and the DB itself splits them off into M10/M13.

**Fused-in counter-movement D — the psalmist's reaction to / refusal of falsehood (the virtue, not the vice).** `271608 · Psa 119:163 · D101="abhor (taab)"`, M06(Hate); `274626 · Psa 15:3 · D101="refuses to slander"`, `D102(type)="volition"`, cluster T2 — the *governed* tongue. These are the opposing disposition, grouped with what they oppose.

**Sub-strand — self-deception.** `277520 · Psa 36:2 · D102(type)="cognition"`, `D114`="the interior tells itself its sin is invisible and unhateable" — deceit turned inward, distinct from deceit-as-weapon; and `306806 · Psa 78:36 · D101="flatter / deceive (pathah)"` (hollow, coaxing words toward God).

So: **one strong core movement + homograph fusion ("vain", "lie down") + an adjacent betrayal movement + the counter-disposition + a self-deception sub-strand.** The label names the core honestly but over-collects.

---

## 2. The movements / operations evidenced (cited)

### 2.1 The lying tongue as weapon against the psalmist
Deceit predicated of the foe, aimed at the psalmist: `270230 · Psa 109:2 · D106(operation)="be deceitful" · D107(target)="in speech"`; `270235 · Psa 109:2 · D106="speak lies" · D107="against the psalmist"`; `272308 · Psa 120:2 · D106="deceive" · D107="with the tongue"`; `272305 · Psa 120:2 · D106="lie"`; `281869 · Psa 69:4 · D101="lies / falsehood (sheqer) · D114`="false accusation as the enemies' weapon … falsehood pressed as if it were justice"; `272084 · Psa 119:78` and `272135 · Psa 119:86 · D106="lie / deceive" · D107="against the psalmist and the truth"`. Operation is verbal, target is the psalmist or "the truth".

### 2.2 Deceit as the settled character of the wicked man
The lie names the whole man: `278631 · Psa 43:1 · D101="deceit / treachery (mirmah - the deceitful man)" · D102(type)="status"`; `279825 · Psa 52:4 · D101="deceit / treachery (mirmah - deceitful tongue)" · D114`="the whole man summed in his lying speech … his very name"; `280161 · Psa 55:23 · D101="treachery / deceit (mirmah - men of blood and treachery)" · D114`="the deceit that marks the doomed"; `307629 · Psa 116:11 · D101="liars (kazab)" · D105(bearer)="all mankind"`; `280491 · Psa 58:3 · D114`="falsehood as the native tongue of the wicked … from birth".

### 2.3 Deceit worked / framed (the tongue harnessed)
`279811 · Psa 52:2 · D106(operation)="work / practise"`; `279552 · Psa 50:19 · D106="frame / harness" · D114`="the tongue harnessed to lies"; `280556 · Psa 59:12 · D106="utter" · D104(seat)="the mouth"`; `280044 · Psa 55:11 · D101="fraud / deceit (mirmah)"` (pervading the marketplace).

### 2.4 Inverted / delighted loves
Deceit chosen for its own sake: `279816 · Psa 52:3 · D101="lying / falsehood (sheqer - lying more than speaking right)" · D108(manner)="more than speaking righteousness" · D114`="deceit chosen for its own sake"; `280957 · Psa 62:4 · D101="falsehood / lie (kazab - pleasure in falsehood)" · D114`="the lie that is the enemies' delight … blessing with the mouth while cursing within".

### 2.5 Self-deception
`277520 · Psa 36:2 · D102(type)="cognition" · D106="he flatters himself … self-deception about guilt"` — the only cognition-typed instance; deceit folded inward.

### 2.6 False submission / hollow repentance toward God
`283817 · Psa 81:15 · D101="cringe (kachash)" · D116(locus)="external:god" · D114`="feigned submission of the cowed foe, homage without love"; `306806 · Psa 78:36 · D101="flatter / deceive (pathah)"` + `306809 · Psa 78:36 · D101="lie (kazab)" · D116="external:god" · D114`="a repentance not seated in the heart".

### 2.7 Betrayal / covenant-faithlessness (adjacent movement)
`283331 · Psa 78:57 · D106="betray / deal faithlessly" · D107="with God"`; `280630 · Psa 59:5 · D106="act treacherously / plot" · D107(target)="evil"`; `278742 · Psa 44:17 · D106="be false (negated)" · D113(prohibition)="negated" · D116="external:god"` — fidelity *maintained*; `282391 · Psa 73:15 · D106="betray (hypothetically, avoided)" · D114`="the restraint of a man who will not spread his doubt".

### 2.8 The counter-disposition (the psalmist / the righteous)
`271608 · Psa 119:163 · D106="abhor falsehood"`; `274626 · Psa 15:3 · D102(type)="volition" · D106="he does not slander … restrained speech that protects others"`; and the whole hated-false-way refrain of Ps 119: `271239 · Psa 119:104`, `271379 · Psa 119:128`, `271765 · Psa 119:29`, `271609 · Psa 119:163` — falsehood as the object of the psalmist's hatred, set against love of the law.

### 2.9 Fused futility / rest strands (see §1)
`272606/272613/272614/270096` (labour/watch/toil/help "in vain"); `284803 · Psa 89:47` (human "vanity"/frailty); `279472 · Psa 4:8` (peaceful lying-down = rest). These carry no deceit operation — D106 is futility or rest, not lying.

---

## 3. The network (genuine pair edges only)

Discarding all self-loops (§0.2), the genuine `pair`/`resolution:"span"` edges to a different span are:

**In-family (both endpoints among the 45 masters) — 2 mutual dyads:**
- `Psa 52:2 ↔ Psa 52:4` on D112(coupling): `279811 → 279825` ("the deceitfulness voiced by the deceitful tongue (v4)") and `279825 → 279811` ("the deceit worked in v2 (remiyyah)"). The worked-deceit (remiyyah, v2) and the named deceitful-tongue (mirmah, v4) bind to each other.
- `Psa 55:11 ↔ Psa 55:23` on D112(coupling): `280044 → 280161` and `280161 → 280044` ("the same mirmah as…"). The city's *fraud* and the betrayer's *treachery* are read as one mirmah across the psalm.

**Pair edges pointing OUT of the family's master set (to_span not among the 45) — link into co-text, not into this network:** `278631→278632` (Psa 43:1), `281869→281864` (Psa 69:4), `279816→279819` (D108) and `279816→279812` (D112) (Psa 52:3), `282391→282394` (Psa 73:15), `279552→279549` (Psa 50:19), `278742→278744` (D107) and `278742→278740` (D112) (Psa 44:17), `280957→280959` (Psa 62:4), `280491→280487` (Psa 58:3), `280556→280555` (Psa 59:12), `280630→280631` (D107 & D112) (Psa 59:5).

**Network finding:** the family is **almost edgeless as a network** — only two mutual dyads connect its own members, both intra-passage (Ps 52, Ps 55). Every other genuine edge reaches to a span outside the family, and the overwhelming majority of "edges" in the file are non-links (self-loops). There is no cross-passage deceit web here; connectivity is confined within a single psalm at a time.

---

## 4. The interior anatomy the data actually names

Assembling only filled fields:
- **Seat:** the interior is named only at the organ of speech — **the tongue** (`279825 · Psa 52:4`) and **the mouth** (`280556 · Psa 59:12`); 43/45 leave seat="none". The heart appears in passage *text* (e.g. Psa 55:21, Psa 62:4 "inwardly they curse") but is **not** captured in D104 — a derivation gap (§5).
- **Bearer:** overwhelmingly the **wicked other**, never the psalmist's own interior in the vice-instances — "the enemies" (`270230`, `272308`, `280957`), "the wicked" (`280491`, `279552`), "the tyrant" (`279825`, `279811`, `279816`), "the liar" (`268873`), "the deceitful man" (`278631`), "all mankind" (`307629`, `284803`), "they" (`283335`, `306806`, `306809`). The psalmist/righteous bears only the **counter** or **avoided** cases (`271608` abhor; `274626` refuse to slander; `282391` betrayal avoided; `279472` peaceful rest; `270096` reckons human help vain). Every bearer is `resolution:"inferred"` — none stated with a first/second-person possessive on the verse.
- **Source (D103):** **not present in any ledger** — no instance carries a D103 item. What moves deceit is never named.
- **Operation (D106):** the movement's verbs — lie/deceive, speak/utter lies, work/frame deceit, flatter/coax, slander, betray, act treacherously; "none" on the noun-status instances (`278631`, `279825`, `280161`, `280044`).
- **Target (D107):** the psalmist, the truth, the neighbour, God, the covenant; often "none".
- **Manner (D108):** essentially unnamed (only `279816`).
- **Coupling / locus (corrected):** locus is `internal:ib-state` for most, `external:god` for the God-directed treachery/false-submission (`283331 · Psa 78:57`, `283817 · Psa 81:15`, `306806/306809 · Psa 78:36`, `278742 · Psa 44:17`).

**Anatomy summary:** deceit in this family is a **speech-organ phenomenon of the wicked other**, observed from outside (inferred bearer, no source, seat only at tongue/mouth), oriented either against the psalmist (internal:ib-state horizontal) or against God (external:god). The psalmist's own interior enters only as abhorrence, restraint, or avoidance.

---

## 5. What could not be derived (flagged)

- **D103 source — never populated.** The origin/impulse of deceit is nowhere named across all 45 instances.
- **D109 intensity, D110 specifier, D111 effect — absent across all 45** (§0.4). No gradation, qualification, or downstream effect is captured, though the text supplies candidates (e.g. Psa 52:5 "God will break you down", Psa 55:23 "shall not live out half their days" = effect of treachery — uncaptured).
- **Seat left "none" in 43/45** while passage text repeatedly locates deceit in the **heart** (Psa 55:21 "war was in his heart"; Psa 62:4 "inwardly they curse"; Psa 36:1–2 "deep in his heart"). The heart-seat is derivable from the text but was **not** entered in D104 — a systematic under-derivation.
- **Manner "none" in 44/45** — the *how* of deceit (smooth as butter / softer than oil, Psa 55:21; secretly, Psa 101:5) is in the text but uncaptured.
- **Bearer resolution — 100% inferred, 0% stated.** No instance anchors the bearer to an explicit surface pronoun; all are reader-supplied.
- **The D112/D116 swap (§0.1)** means any downstream consumer reading D116 as locus would mis-read 13 instances' locus as a prose phrase; corrected here.
- **Homograph mis-bucketing (§1):** the "vain/vanity" (H7723, 5 instances) and "lie down" (H7901, `279472`) strands are grouped by English keyword, not by inner-being movement — they are futility and rest, respectively. The DB compounds this by filing the H7723 "vain" set under M14(Deceit) despite their D106 reading "labour/watch/toil in vain".
- **Two declared outliers** (`278742` → M13 Truth; `268844` → M42 Speech) and **6 untypeable instances** (4 null-cluster, 2 T2) mean the term-cluster layer disagrees with the family label for ~8 of 45.
- **Network is effectively unfilled** (§3): 2 in-family dyads only; the file cannot support a family-wide deceit network.

---

## 6. Summary

The `deceit-falsehood` family (29 meanings / 45 instances, all poetic) has a **strong, coherent core** — the lying tongue of the wicked (mirmah / sheqer / remiyyah / kazab / kachash), a speech-organ phenomenon predicated of the **enemy**, aimed at the psalmist or at God, with the psalmist's interior present only as abhorrence, restraint or avoidance. But the English-keyword grouping has **fused four distinct movements**: futility ("vain/vanity", shav — Ps 127/108/89), rest ("lie down", H7901 — Ps 4:8), covenant-betrayal (bagad/shaqar — M10/M13), and the counter-disposition (hatred/refusal of falsehood). Data-integrity load: **13 D112/D116 swaps**; **seat "none" 43/45, manner "none" 44/45**; **D103/D109/D110/D111 wholly absent**, D113 present once; **6 untypeable + 2 outlier clusters**; the network reduces to **2 intra-passage mutual dyads** (Ps 52, Ps 55) once self-loops are discarded. Every role = characteristic; every bearer inferred.
