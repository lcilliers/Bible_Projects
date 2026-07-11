# Family analysis — `hope-waiting` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__hope-waiting.json` only. 17 meanings · 45 instances · 36 passages. Every finding cited `reference · span_id · Dnnn(label)` into that file. Nothing imported from outside it.

Lemmas fused under the family keyword (from `meaning.lemma` + `evidence`): H3176 *yachal*, H6960 *qavah*, H8615 *tiqvah*, H7664 *sever*, H7663 *sabar*, H2442 *chakah*, H2342 *chul*, H4009 *mibtach*, H3689 *kesel*, H7725 *shuv*, H0693 *arab*, H1747 *dumiyyah*, H6186 *arak*.

---

## 0. Data-integrity screen (done first)

**0.1 D112(coupling) / D116(locus) field-swap — 6 instances transposed.** Correct order = D116 a `internal:`/`external:` code, D112 a prose phrase. These carry the code in D112 and prose in D116, so read them **corrected** (D116 locus = `external:god`; D112 coupling = the prose phrase):
- `Psa 130:5 · span 272828 · D112/D116` (D112 `external:god`, D116 "paired with the waiting")
- `Psa 130:7 · span 272837` (D116 "paired with God's steadfast love and redemption")
- `Psa 131:3 · span 272882` (D116 "paired with the stilled soul")
- `Psa 130:5 · span 272822` (D116 "paired with the soul's waiting and hope")
- `Psa 130:5 · span 272825` (D116 "paired with the soul and hope")
- `Psa 106:13 · span 269606` (D116 "paired with forgetting")

All other instances are correctly ordered (D116 = a code, D112 = a phrase), e.g. `Psa 147:11 · span 274289 · D112(coupling)="hope-in-chesed" · D116(locus)="internal:ib-state"`.

**0.2 Self-loop "edges" are not network.** 121 edges are `item_type:flag` + `resolution:inferred` with `to_span` = the span's own id (bearer/target/coupling self-flags, e.g. `Psa 119:114 · span 271301 · D105 bearer` → to_span 271301). A further set of D106 operation self-references (`item_type:event`, to_span = self, e.g. `Psa 62:5 · span 280969 · D106 operation`) are likewise **not** links. None enter the network.

**0.3 Genuine `pair` edges = 31, but 28 point outside this file.** 28 of 31 pair edges (`resolution:span`, to_span ≠ self) link to spans **not present in this base source** (e.g. `Psa 42:11 · span 278527 · D105 bearer` → 278524; `Psa 52:9 · span 279870 · D103 source` → 279873). Their targets are named by span-id only — **the linked interior is not derivable from this file**. Only **3** pair edges stay in-family, forming a single bidirectional link (see §"The network").

**0.4 seat(D104)=none: 42 / 45.** Only three seats filled: `Psa 62:5 · span 280969 · D104 seat`="the soul"; `Psa 69:3 · span 281823 · D104 seat`="the eyes"; `Psa 62:1 · span 280918 · D104 seat`="the soul".

**0.5 manner(D108)=none: 37 / 45.** Eight filled, e.g. `Psa 71:14 · span 282060 · D108 manner`="continually, praising more and more"; `Psa 40:1 · span 278212 · D108 manner`="patient-waiting"; `Psa 62:1 · span 280918 · D108 manner`="in silence, for God alone".

**0.6 Absent dimensions (all 45).** D109 intensity, D110 specifier, D111 effect, D113 prohibition are **entirely absent** across every instance. D103 source is present only on the relationally-paired instances; D114 discovery and D115 role are on all.

**0.7 Cluster NULL — 3 instances** (term-cluster cannot type them): `Psa 78:7 · span 306765` (H3689 *kesel*); `Psa 59:3 · span 280602` (H0693 *arab*); `Psa 62:1 · span 280918` (H1747 *dumiyyah*).

**0.8 Cluster T2 — 1 instance:** `Psa 5:3 · span 280702` (H6186 *arak*), `cluster.all_candidates="T2(Supplementary) | M26(Righteousness)"` — a supplementary/qualifier reading, not a native hope-cluster term.

**0.9 Role.** D115 role = "characteristic" on **all 45** — no qualifier, no standalone in the file.

---

## 1. Coherence — does the label fit its data?

**Partly. A coherent core, but the keyword has fused in at least two foreign movements.** The genuine inner-being movement — *the human self hoping / waiting on God* — accounts for the large majority (M18 Hope, M17 Counsel-as-wait, M19 Trust; ~38 instances). But grouping on the surface words "wait / hope" has pulled in:

**(a) Adversarial "lie in wait / ambush" — 3 instances, NOT the studied IB movement.** Bearer is the wicked / enemies, and the operation is predatory watching, the opposite of hope:
- `Psa 119:95 · span 272198 · D105 bearer`="the wicked", `D106 operation`="lie in wait", target = the psalmist.
- `Psa 56:6 · span 280303 · D105 bearer`="the enemies", `D106 operation`="lie in wait for", `D107 target`="my life (nefesh)".
- `Psa 59:3 · span 280602 · D105 bearer`="the enemies", `D106 operation`="lie in wait / ambush" (H0693 *arab*).
These are a homograph fusion (*qavah*/*arab* "wait" in a hostile sense). They should be screened out of a hope-waiting reading — the human IB is present but it is the aggressor's, not the hoper's.

**(b) Peripheral / cluster-outlier readings** where the keyword is adjacent but the movement differs:
- `Psa 5:3 · span 280702` H6186 *arak* "prepare and watch at dawn" — cluster T2/M26 Righteousness; an ordering/liturgical act, `is_outlier=true`.
- `Psa 23:6 · span 275858` H7725 *shuv* "I shall dwell with God forever" — cluster M45 Transformation, `is_outlier=true`; settled-hope by inference, not a wait/hope term.
- `Psa 37:7 · span 277841` H2342 *chul* "be still and wait patiently" — cluster M03 Grief, `is_outlier=true`.
- `Psa 69:20 · span 281773` H6960 *qavah* "looked for pity, but there was none" — genuine IB (disappointed hope) but the affect is dashed expectation, `D108 manner`="in vain - there was none".

`is_outlier=true` on the file marks 7 meanings (H6960:wait/M17, H7725:dwell/M45, H7663:hope/M17, H6960:hope/M17, H6960:look/M17, H6186:prepar/M26, H2342:wait/M03) — the file itself flags the crossovers.

**Net:** the label fits the ~38-instance core (self → hope/wait → God); it does **not** fit the 3 adversarial "lie-in-wait" spans, which are a distinct (hostile) movement, and sits loosely over the ~4 peripheral outliers.

---

## 2. The core movement — self hoping / waiting on God

**2.1 What the word is (D101/D102).** The family reads across the whole anatomy of the inner being, not one register — D102 type: **disposition 13, action 12, affect 11, status 5, volition 4**. So hope-waiting is at once:
- a **settled disposition** — the recurring Ps 119 refrain `Psa 119:114/119:147/119:43/119:49/119:81/119:74/119:116/119:166 · D102(type)="disposition"`, sense "hope (*yachal/sabar*)", each `D107 target`="in God's word".
- an **action / event** — `Psa 130:5 · span 272828 · D106 operation`="hope"; `Psa 42:5 · span 278572 · D102(type)="action"` "hope / wait (*yachal*)".
- an **affect** — `Psa 147:11 · span 274289 · D102(type)="affect"` "hope in steadfast love"; `Psa 9:18 · span 285943 · D101 sense`="the poor's hope shall not perish".
- a **status** — `Psa 71:5 · span 282194 · D102(type)="status"` "you, O Lord GOD, are my hope"; `Psa 62:5 · span 280969` "hope / expectation (*tiqvah*)".
- a **volition** — self-exhortation: `Psa 27:14 · span 276229 · D102(type)="volition"` "wait for the LORD, take courage"; `Psa 37:34 · span 277773` "wait for the LORD and keep his way".

**2.2 Whose inner being (D105 bearer).** Overwhelmingly the first-person self: `D105 bearer`="the psalmist" on 24 instances. Widened to the collective in the closing exhortations — `Psa 130:7 · span 272837 · D105 bearer`="Israel"; `Psa 131:3 · span 272882`="Israel"; `Psa 33:22 · span 277080`="the community"; `Psa 146:5 · span 274230`="the blessed"; `Psa 9:18 · span 285943`="the poor / needy"; `Psa 78:7 · span 306765`="the children"; `Psa 106:13 · span 269606`="the fathers". Every bearer is `resolution:inferred` **except** the three self-command spans (below), which are `resolution:span`. **Flag:** `Psa 65:5 · span 281218 · D105 bearer`="all the ends of the earth and the farthest seas" — a cosmic/collective bearer, not a discrete human interior; the human-IB screen sits loosely here.

**2.3 What moves it and toward what (D106 operation / D107 target).** The operation is consistently *hope / wait*, and the target is almost always God or God's word: `D107 target`="in God's word" across the Ps 119 arc; "in the LORD" (`Psa 130:7 · span 272837`); "in God" (`Psa 42:11 · span 278527`); "from God" (`Psa 62:5 · span 280969`, tiqvah "my hope is from him"). The wait is time-stretched — `Psa 25:5 · span 276069 · D107 target`="sustained-waiting" "for you I wait all day"; `Psa 40:1 · span 278212` "I waited patiently, he heard my cry".

**2.4 How (D108 manner)** — filled on 8, and it names the *quality* of the waiting: "continually, praising more and more" (`Psa 71:14 · span 282060`); "from his youth, lifelong" (`Psa 71:5 · span 282194`); "in silence, for God alone" (`Psa 62:1 · span 280918`); "until the eyes grow dim" (`Psa 69:3 · span 281823`); "in vain - there was none" (`Psa 69:20 · span 281773`).

**2.5 What it is bound to (D112 coupling, corrected) / where it sits (D116 locus, corrected).** Locus splits two ways: **outward to God** (`external:god`, ~26 once the 6 swaps are corrected) and **an interior state** (`internal:ib-state`, 16, e.g. `Psa 25:3 · span 276058`, `Psa 146:5 · span 274230`). Three couple to God's covenant love: `Psa 147:11 · span 274289 · D112(coupling)="hope-in-chesed"`; `Psa 33:18 · span 277045`; `Psa 33:22 · span 277080`. The Ps 119 spans couple to "the whole HOPE-arc of the psalm" (e.g. `Psa 119:114 · span 271301 · D112 coupling`). D114 discovery reads hope as leaning **forward** onto covenant love, distinct from fear looking up: `Psa 147:11 · span 274289 · D114(discovery)` ("hope leans forward onto covenant love where fear looks up in reverence").

**2.6 The self-commanded sub-pattern.** Three spans are `D105 bearer`="the soul (self-commanded)" with `resolution:span` — the self ordering its own interior to hope: `Psa 42:5 · span 278572`, `Psa 42:11 · span 278527`, `Psa 43:5 · span 278676` (the "Why are you cast down, O my soul… Hope in God" refrain). Alongside these, `Psa 62:1 · span 280918 · D105 bearer`="the psalmist (his soul)" — the soul as the waiting agent.

---

## 3. The network (genuine links only)

Of 31 `pair` edges, **28 leave the family** (targets not in this file — not derivable). **One** genuine bidirectional link stays in-family:

- `Psa 62:1 · span 280918` (soul waits in silence, *dumiyyah*) ⇄ `Psa 62:5 · span 280969` (hope, *tiqvah*): 280969 couples out on `D108(manner)` and `D112(coupling)` → 280918, and 280918 couples back on `D112(coupling)` → 280969.

This is the only intra-family relational structure the file can bear: within Psalm 62 the **silent waiting of the soul (v1)** and the **hope/expectation (v5)** are read as one interlocked posture ("the same posture self-commanded"). Everywhere else the network is one-directional and points at spans outside the file — **sparse, and mostly non-derivable**.

---

## 4. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seats named:** the *soul* (nefesh) — `Psa 62:5 · span 280969 · D104 seat`, `Psa 62:1 · span 280918 · D104 seat`; the *eyes* — `Psa 69:3 · span 281823 · D104 seat` ("my eyes grow dim with waiting"). No heart, spirit/ruach, or other seat is coded (though verse text mentions "heart" at e.g. Psa 27:14, it is not lexicalised on the hope span).
- **Couplings named:** hope bound to *chesed* / steadfast love (147:11, 33:18, 33:22); to God's *word* (Ps 119 arc, 130:5); to *trust* from youth (`Psa 71:5 · span 282194 · D112 coupling`="paired with trust from youth"); to *thanksgiving* (`Psa 52:9 · span 279870`); to *not-forgetting* (`Psa 78:7 · span 306765`; and its negation `Psa 106:13 · span 269606`, corrected, "paired with forgetting" — failure to wait = forgetting).
- **The named interior of hope-waiting is therefore:** soul + eyes as seats; and hope tethered to covenant love, the word, trust, thanksgiving, and remembrance — but the tethers themselves point mostly to spans this file does not contain.

---

## 5. What could not be derived (flag)

- **D109 intensity, D110 specifier, D111 effect, D113 prohibition** — never coded on any of the 45 instances; no measure of degree, no specifier, no stated effect/outcome, no prohibition form. The *effect* of hope (deliverance, non-shame) is present in verse text but **not lexicalised** on the hope span.
- **28 of 31 network links** resolve to span-ids absent from this file — the interior they connect to cannot be described from this source.
- **42/45 seats** and **37/45 manners** unfilled — the *where* and *how* of most hoping is unstated.
- **3 cluster-NULL + 1 cluster-T2** instances (`Psa 78:7 · 306765`, `Psa 59:3 · 280602`, `Psa 62:1 · 280918`; `Psa 5:3 · 280702`) — the term-cluster cannot type them, so their family membership rests on the keyword alone.
- **The 3 "lie-in-wait" spans** (272198, 280303, 280602) are a **foreign movement** (adversary's predatory watching) mis-fused by keyword — flagged, not part of the hope-waiting IB.
- Bearer humanity is loose at `Psa 65:5 · span 281218` ("all the ends of the earth") — cosmic, not a discrete human interior.

---

## Summary

17 meanings / 45 instances; a coherent core movement — **the self (and, widened, Israel) hoping and waiting on God, read across disposition, action, affect, status and volition, tethered to covenant love, the word and trust** — but the keyword has fused in **3 adversarial "lie-in-wait" spans** (a different, hostile movement) plus ~4 cluster-outlier peripherals; the network is all but non-derivable (28/31 edges leave the file; one genuine Psalm-62 soul-wait ⇄ hope link); seats (42/45) and manner (37/45) mostly unfilled, and D109/D110/D111/D113 wholly absent; 6 instances carry a D112/D116 swap and 121 self-loop "edges" are not network.
