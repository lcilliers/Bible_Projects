# Family analysis — `prayer-petition-crying-out` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__prayer-petition-crying-out.json` only. Scope strictly that one file. Counts (meta): **33 meanings · 103 instances · 70 passages**. Provenance: ib_characteristic v3 + family grouping v1 + term-based cluster v2. Every claim cited `reference · span · Dnnn(label)`. Dimension legend from `meta`.

---

## 0. Data-integrity screen (done first)

**D112(coupling)/D116(locus) field-swap — 32 of 103 instances are transposed.** In these, D116(locus) holds a prose phrase and D112(coupling) holds the `external:`/`internal:` code — i.e. the code sits in the wrong field. Corrected order = D116 a code, D112 a phrase.
- Example: `Psa 102:2 · span 268978 · D112(coupling)="external:god"` + `D116(locus)="paired with the plea for a speedy answer"` → read corrected as locus=`external:god`, coupling=`paired with the plea…`.
- All 32 swapped instances carry the same code, `external:god`: `Psa 102:2(268978), 105:1(269366), 116:13(270934), 116:17(270952), 116:2(270973), 116:4(270984), 118:5(271165), 120:1(272296), 138:3(273334), 91:15(285092), 99:6(285833), 99:6(285836), 102:1(268898), 109:4(270323), 102:17(307203), 102:17(307208), 130:1(272799), 89:26(284645), 106:44(269782), 102:1(268894), 107:13(269883), 107:19(269908), 116:11(307626), 107:28(269957), 107:6(270047), 102:1(268900), 122:6(272418), 106:15(269616), 106:30(269707), 106:38(269726), 116:4(270988), 104:15(269245)`.
- The other **71 instances are in correct orientation** (D116 holds the code, D112 the phrase), e.g. `Psa 141:1 · span 273682 · D116(locus)="internal:ib-state"` + `D112(coupling)="call-and-hasten"`. **All D112/D116 reasoning below uses the corrected reading.**

**Self-loop "edges" are not links.** 337 edge-records exist; **300 are self-loops** (`item_type:"flag"`, `resolution:"inferred"`, `to_span`==own span, `from_span`:null) and carry no network. Breakdown: `(flag,inferred)=294`, `(event,inferred)=6`, plus `(event,span)=1`. Only **36 genuine `pair` edges** (`resolution:"span"`, to a *different* span) exist, across **22 source instances**. The network below uses only these 36.

**seat(D104)="none" in 100 of 103.** Only 3 name an interior seat — all the speech organ: `Psa 54:2 · span 279975 · D104(seat)="the mouth (words of my mouth)"`; `Psa 66:17 · span 281294 · D104="the mouth"`; `Psa 69:3 · span 281818 · D104="the throat"`.

**manner(D108)="none" in 91 of 103.** 12 filled (listed in §5).

**Absent dimensions — entirely unfilled across all 103:** D109 intensity, D110 specifier, D111 effect, D113 prohibition. **D103 source present in only 12/103.** D101,102,104,105,106,107,108,112,114,115,116 present in all 103.

**Cluster NULL / T2.** 19 instances sit under meanings whose `cluster.code` is null (term-cluster cannot type them): the meanings `H2648:alarm(2), H6817:cri(2), H7775:cry(2), H8159:lookaway(1), H0380:appl(1), H7596:ask(1), H0935:come(1), H7768:cri(1), H6817:cry(1), H6818:cry(1), H7768:cry(1), H6817:cryout(1), H5258:pourout(1), H8210:pouredout(1), H0577:pray(1), H6670:shin(1)`. **No T2 instances.**

**role(D115)="characteristic" in all 103** — uniform; the file marks none as qualifier or standalone.

---

## 1. Coherence — does the label fit the data?

**Largely yes, but the keyword grouping has fused in one clear outlier band and a few non-IB artefacts.** The dominant mass is one coherent movement — the inner being turning outward in vocal appeal to God. Cluster spread (instance-weighted): **M37 Calling 44 · M21 Prayer 24 · M42 Speech 9** = 77 of 103 form the core petitionary-vocal movement; **None 19** (untyped, but mostly cry/pour-out senses that belong); **M03 Grief 5 · M15 Wisdom 1 · M10 Sin 1** = the flagged outliers.

Distinct movements the grouping actually contains:

1. **Core petition / calling / crying-out to God** (~77, plus most of the untyped 19). The recurring appeal: `Psa 102:2 · span 268978 · D101(sense)="call (qara)"`; `Psa 17:6 · span 274858 · D101="call, confident of an answer"`; `Psa 143:1 · span 273846 · D101="prayer for a hearing"`; `Psa 34:6 · span 277260 · D101="this poor man cried and was heard"`.
2. **Complaint / lament (siach)** — a distinct *affective outpouring*, marked outlier: `Psa 102:1 · span 268894 · D101="complaint (siach)"` (M03 Grief); `Psa 142:2 · span 273778 · D101="pour out complaint"`; `Psa 55:2 · span 280124 · D101="complaint / lament (siach)"`; `Psa 55:17 · span 280094 · D101="complaint / musing (siach)"` (M15 Wisdom); `Psa 64:1 · span 281092`. This is petition-adjacent but is grief/musing, not appeal — correctly flagged `is_outlier=true`.
3. **Petition for cleansing** — `Psa 51:7 · span 279764 · D101="purge / un-sin (chata piel)"` (M10 Sin, outlier); still an imperative plea to God.
4. **Entreat** — `Psa 119:58 · span 271941 · D101="entreat (chalah)"` (M03, outlier).
5. **Alarm / inner panic (chaphaz)** — the *state behind* the cry, not itself an appeal: `Psa 31:22 · span 276785 · D101="in alarm I said 'I am cut off'"` (D102 state); `Psa 116:11 · span 307626 · D101="alarm (chaphaz)"` (D102 state). Cluster None.

**Non-IB / keyword artefacts that do NOT belong to this movement (flag):**
- `Psa 17:8 · span 274876 · D101="keep me as the apple of your eye"` (`H0380:appl`, D102 affect) — a protection metaphor, not prayer.
- `Psa 104:15 · span 269245 · D101="shine (tsahal)"` (`H6670:shin`, D102 state) — oil making the face shine; gladness, not prayer. (Also one of the 32 swapped.)
- `Psa 49:11 · span 279290 · D101="call / name (qara — lands by their names)"` (`H7121:call`) — naming of lands, a homographic `qara`, not appeal.
- `Psa 16:4 · span 274716 · D101="refuse the idolaters' offerings"` (D102 volition) — idolatry-refusal (drink-offering homograph), tangential to petition.

Two instances are **negated / non-psalmist bearers** — the movement described by its absence: `Psa 53:4 · span 279924 · D105(bearer)="the evildoers (who do not)"` / `D101="call upon (qara — do not call upon God)"`; `Psa 79:6 · span 283535 · D105(bearer)="the kingdoms"` / `D101="call upon (qara, negated)"`.

---

## 2. Sense (D101) and type (D102) — what the word is

Type distribution across 103: **action 72 · affect 24 · volition 3 · state 3 · status 1.**
- **Action (72)** — the outward act of appeal: call, cry, cry out, pray, pour out. E.g. `Psa 3:1 spans` under `H7121:call` (`D102="action"`); `H8605:prayer` (20), `H2199:cri` (cried).
- **Affect (24)** — the appeal read as an inner-felt cry rather than a bare act: `Psa 18:6 · span 275203 · D101="cry in distress" · D102="affect"`; `Psa 30:8 · span 276641 · D101="cry and plead for mercy"`; `Psa 9:12 · span 285892 · D101="the cry of the afflicted"`; `Psa 39:12 · span 278051 · D101="hold not your peace at my tears"`.
- **Volition (3)** — willed appeal: `Psa 141:1 · span 273682 · D101="call urgently"`; `Psa 32:6 · span 276938 · D101="let the godly pray while you may be found"`; `Psa 16:4 · span 274716` (the refusal artefact).
- **State (3):** the two alarm spans (276785, 307626) + shine (269245).
- **Status (1):** `Psa 42:8 · span 278608 · D101="prayer (tefillah)" · D102="status"` — prayer as a standing thing, not an act.

---

## 3. Bearer (D105) — whose inner being

All 103 have D105 filled; **68 = "the psalmist"**; every value is inferred (the self-loop D105 edges are all `resolution:"inferred"`). The IB is overwhelmingly the individual suppliant. Other bearers widen it to communal and typological figures: `the fathers` (4, e.g. `Psa 22:5 · span 275774 · D105="the fathers"`), `David` (2), `the destitute` (2), and singletons `the worshippers, the poor man, the afflicted, the prisoners, the sick, the sailors, the wanderers, the pilgrims, the godly, the penitent, we (the people), your people`, plus the OT figures `Moses and Aaron`, `Samuel`, `Phinehas` (`Psa 106:30 · span 269707`). Two bearers are the negated non-suppliants of §1 (`the evildoers`, `the kingdoms`). **Bearer is the human IB in every case that belongs to the movement.**

---

## 4. Operation (D106) and target (D107) — what it does, toward what

**Operation (D106, all 103 filled).** The verbs of appeal: `pray 13 · call upon 11 · call 9 · cry out 8 · cry 8 · pour out complaint 4 · cry for help 2 · pray/cry out 2`, plus richer read-phrases on individual spans (e.g. `Psa 141:1 · span 273682 · D106="an urgent appeal — 'make haste to me' — the interior pressing for a quick hearing"`; `Psa 145:18 · span 274103 · D106="the operation of calling on God sincerely, in truth — not mere formula but real appeal"`).

**Target (D107, all 103 filled) — the appeal is near-uniformly Godward.** `to God 20 · God's word 5 · God 5 · God's name 4 · to the LORD in trouble 4 · to God in distress 3 · on the name of the LORD 3 · before God 2` and similar. A few targets are the appeal's own answer-structure rather than a person: `crying-out 4`, `crying-answered 2`, `supplication 2` — e.g. `Psa 65:2 · span 281193 · D107(target)="God" ` links to a neighbouring span (see network). The interior faces **outward and upward**: God, God's name, God's word.

---

## 5. Manner (D108) and the interior circumstances

12 filled manner-values sketch the *setting and posture* of the cry:
- Time / persistence: `Psa 55:17 · span 280094 · D108="evening, morning, and at noon"`; `Psa 42:8 · span 278608 · D108="at night, a song"`; `Psa 50:15 · span 279519 · D108="in the day of trouble"`.
- Bodily/vocal: `Psa 54:2 · span 279975 · D108="aloud, the words of his mouth"`; `Psa 66:17 · span 281294 · D108="high praise on his tongue"`; `Psa 77:1 · span 282861 · D108="aloud"`; `Psa 69:3 · span 281818 · D108="until the throat is parched"`.
- Inner condition: `Psa 61:2 · span 280864 · D108="from the end of the earth, heart fainting"`; `Psa 55:2 · span 280124 · D108="restlessly"`.
- Grounds of appeal: `Psa 55:1 · span 280027 · D108="begging God not to hide himself"`; `Psa 69:13 · span 281716 · D108="appealing to God's abundant steadfast love"`; ritual `Psa 51:7 · span 279764 · D108="with hyssop"`.

---

## 6. Source (D103) — what grounds/answers the appeal (12/103)

The 12 filled sources are almost all **God's hearing / saving response**, i.e. the appeal is grounded in an answer: `Psa 50:15 · span 279519 · D103="answered by God's deliverance (v15)"`; `Psa 55:16 · span 280085 · D103="and the LORD will save him"`; `Psa 66:19 · span 281314 · D103="which God has listened to and attended"`; `Psa 55:17 · span 280094 · D103="and he hears the psalmist's voice"`; `Psa 69:13 · span 281716 · D103="resting on God's steadfast love and saving faithfulness"`; `Psa 57:2 · span 280372 · D103="to God who fulfils his purpose for him"`; `Psa 42:8 · span 278608 · D103="grounded by God's steadfast love commanded by day"`. The movement is thus read as a *call-and-answer* coupling, not a cry into the void — even where D107 target is bare.

---

## 7. Coupling (D112) / locus (D116) — bound to what, sitting where (corrected)

Using the corrected reading (§0): the **locus code** partitions cleanly — **`external:god` 70 · `internal:ib-state` 33** (no other codes). The appeal predominantly sits *externally oriented*, fixed on God (70), with a substantial minority read as an internal state of the IB (33, e.g. `Psa 141:1 · span 273682 · locus="internal:ib-state"`; `Psa 145:18 · span 274103`; `Psa 17:6 · span 274858`). The **coupling phrase** (D112, in the 71 correct-orientation rows) names what the appeal is welded to within its psalm: `Psa 141:1 · D112="call-and-hasten"`; `Psa 145:18 · D112="call-in-truth"`; `Psa 17:6 · D112="call-for-answer"`; `Psa 119:146 · D112="paired within its char-arc across the psalm"`. In the 32 swapped rows the coupling phrase is the prose in D116, e.g. `Psa 116:13 · span 270934 · D112(code)="external:god"`→locus, phrase `"paired with lifting the cup"`; `Psa 105:1 · span 269366` phrase `"paired with giving thanks"`; `Psa 116:17 · span 270952` phrase `"paired with the thank-offering"` — coupling the cry to thanksgiving/vow acts.

---

## 8. The network — genuine `pair` edges only (36 edges, 22 source instances)

Sparse and almost entirely **one-directional** (all 36 have `direction:null`; no reciprocated pairs). Edges cluster on four dimensions: **coupling(D112) 18 · source(D103) 12 · manner(D108) 4 · target(D107) 2.** They tie a calling-span to a *neighbouring span in the same passage* — chiefly the answer, the steadfast-love ground, or a parallel cry:
- **source-edges (D103)** link the cry to God's response span: `Psa 50:15 · span 279519 —D103→ 279522`; `Psa 55:16 · 280085 —D103→ 280089`; `Psa 42:8 · 278608 —D103→ 278605`; `Psa 66:19 · 281314 —D103→ 281311`; `Psa 69:13 · 281716 —D103→ 281723`; `Psa 57:2 · 280372 —D103→ 280377`; plus 61:1(280860→280858), 61:1(280856→280855), 54:2(279975→279968), 55:1(280027→280026), 64:1(281092→281089), 55:17(280094→280096).
- **coupling-edges (D112)** weld cry to cry / to the vow-act: `Psa 55:2 · span 280124 —D112→ 280094` (complaint welded to the thrice-daily cry); `Psa 66:20 · 281327 —D112→ 281321`; `Psa 116:4 chain` etc.; 18 total.
- **manner-edges (D108):** `Psa 61:2 · 280864 —D108→ 280866`; `Psa 55:2 · 280124 —D108→ 280122`; `Psa 66:17 · 281294 —D108→ 281297`; `Psa 77:1 · 282861 —D108→ 282862`.
- **target-edges (D107):** `Psa 65:2 · 281193 —D107→ 281192`; `Psa 77:1 · 282861 —D107→ 282868`.

**Network verdict:** the IB's prayer is not densely inter-linked; 81 of 103 instances have no genuine outward edge at all. Where links exist they are the *call→answer* and *call→co-located cry/vow* couplings, always pointing outward within the same passage, never returning.

---

## 9. The interior anatomy the data actually names

Assembling only *filled* structural fields, the file names a very thin interior for this movement — appropriately, because prayer is read as an *outward act* rather than a located faculty:
- **Seat:** only the speech organ — `the mouth` (279975, 281294) and `the throat` (281818). No heart/soul/spirit seat is ever assigned (100 "none").
- **Locus:** `external:god` (70) vs `internal:ib-state` (33) — the appeal's centre of gravity is God, outside the self.
- **Coupling:** cry welded to *answer*, to *steadfast-love*, and to *thanksgiving/vow acts* (§7–8).
- **Manner:** persistence in time (evening/morning/noon; night; day of trouble), vocality (aloud, parched throat), and a fainting/restless heart (§5).
- **Bearer:** the psalmist and, by extension, every afflicted, poor, communal, and typological suppliant (§3).

The named anatomy is therefore: **a human self, in distress, at a time of trouble, lifting a vocal appeal (mouth/throat) outward to God, grounded on/answered by God's hearing and steadfast love, and often coupled to thanksgiving or a vow.**

---

## 10. What could not be derived (from this source)

- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — absent in all 103; no gradation, sub-typing, downstream effect, or prohibition is recorded for this movement.
- **Seat** — unstated in 100/103; the interior *location* of prayer is essentially not derivable here.
- **Manner** — unstated in 91/103.
- **Source/grounding** — recorded in only 12/103; for 91 the call's answer/ground is not derivable.
- **Network** — 81/103 have no genuine link; edges are one-directional only (no reciprocity derivable).
- **Cluster typing** — 19 instances untyped (`cluster=None`); the term-cluster cannot classify their movement.
- **Data hazards carried forward:** the D112/D116 swap (32 rows) must be corrected before any locus/coupling reading; the 300 self-loop "edges" must be excluded from any network measure; four keyword artefacts (17:8 apple, 104:15 shine, 49:11 name-lands, 16:4 idol-offering) and the two negated bearers (53:4, 79:6) sit inside the family but are not the IB's prayer act and should not be counted as such.

---

## Summary

`prayer-petition-crying-out` is a **coherent single movement** — the human self in distress lifting a vocal, Godward appeal — dominated by M37 Calling / M21 Prayer / M42 Speech (77/103), read mostly as **action** (72) with an affective cry band (24). The interior is deliberately thin: **no heart/soul seat** (only mouth/throat ×3), **no intensity/specifier/effect/prohibition anywhere**, **manner in 12, source in 12**. Structurally it is **outward-facing** (locus `external:god` 70 vs `internal:ib-state` 33, corrected) and **welded to God's answer, steadfast love, and thanksgiving/vow acts** via a **sparse, one-directional 36-edge network** (81/103 unlinked). The grouping is sound apart from a correctly-flagged **complaint/lament (siach)** sub-band (§1.2) and a handful of **non-IB keyword artefacts** (apple, shine, land-naming, idol-offering) plus two negated non-suppliant bearers. **Integrity caveats are load-bearing:** 32 D112/D116 swaps and 300 self-loop pseudo-edges must be corrected/excluded before use.
