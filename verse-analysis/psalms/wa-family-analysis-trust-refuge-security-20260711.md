# Family analysis — `trust-refuge-security` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__trust-refuge-security.json` only. 18 meanings · 77 instances · 57 passages. Every claim is cited `reference · span · Dnnn(label)` into that file. Nothing imported from outside it.

---

## 0. Data-integrity screen (done first)

**Dimension coverage (of 77 instances).** Filled on every instance: D101 sense, D102 type, D104 seat, D105 bearer, D106 operation, D107 target, D108 manner, D112 coupling, D114 discovery, D115 role, D116 locus (all 77). **Sparse:** D103 source = 6 only. **Near-empty:** D113 prohibition = 1 only (`Psa 44:6 · span 278837 · D113(prohibition)` = "negated ('NOT in my bow do I trust')"). **Entirely absent across all 77:** D109 intensity, D110 specifier, D111 effect — no instance carries them; nothing about degree, specifier, or downstream effect is derivable from this source.

**Seat (D104) = "none": 76 of 77.** Only one interior seat is filled: `Psa 57:1 · span 280347 · D104(seat)` = "the soul". For every other instance the interior locus of the movement is unstated in the seat field (see §7 — heart/eyes appear only in D114 prose, not captured as seats).

**Manner (D108) = "none": 66 of 77.** The 11 filled: `Psa 52:7·279850` ("instead of making God his refuge"), `Psa 52:8·279861` ("forever and ever"), `Psa 56:3·280276` ("in the moment of fear"), `Psa 56:4·280283` ("without fear"), `Psa 56:11·280236` ("without fear"), `Psa 57:1·280351` ("till the storms of destruction pass by"), `Psa 62:8·280986` ("at all times"), `Psa 71:1·282040` ("pleading never to be put to shame"), `Psa 71:5·282195` ("from his youth"), `Psa 71:6·282201` ("from before birth, from the womb"), `Psa 73:28·282477` ("that he may tell of God's works") — all D108.

**D112 (coupling) / D116 (locus) field-swap: 18 instances transposed.** In these, D116 "locus" holds a prose phrase and D112 "coupling" holds an `internal:`/`external:` code — read them corrected (D116 = the code, D112 = the phrase). Swapped spans: `270270` (Psa 109:24), `270702` (Psa 112:7), `270830` (Psa 115:10), `270838` (Psa 115:11), `270911` (Psa 115:8), `270914` (Psa 115:9), `271183` (Psa 118:8), `271186` (Psa 118:8), `271189` (Psa 118:9), `271192` (Psa 118:9), `272473` (Psa 123:4), `272524` (Psa 125:1), `273099` (Psa 135:18), `285107` (Psa 91:2), `285112` (Psa 91:2), `285127` (Psa 91:4), `285148` (Psa 91:9), `285609` (Psa 96:8). The other 59 are correctly ordered (D116 code, D112 phrase). All locus figures in this analysis are the **corrected** reading.

**Self-loop "edges" are not real links.** Of the edge sub-set: **213 edges are `item_type` flag/event with `resolution:"inferred"` whose `to_span` equals the span's own id** (a string/int identity — e.g. `Psa 112:7·270702` carries flag edges on D105/D107/D112 all pointing back to `270702`). These are self-loops, not network links, and are excluded. Only **37 `pair` edges (`resolution:"span"`) to a different span** are genuine (§6).

**Cluster NULL / T2.** No T2. **Cluster null on 5 instances** (the term-cluster cannot type them): `Psa 37:5·277828` (commit), `Psa 109:24·270270` (become gaunt), `Psa 3:5·278177` (lie down/sleep), `Psa 71:6·282201` (leaned), `Psa 91:9·285148` (made).

**Role (D115).** All 77 = `characteristic`. No `qualifier`, no `standalone` anywhere in the source.

---

## 1. Coherence — does the label fit its data?

**Dominantly yes, with a fused minority.** ~66 of 77 instances are one coherent inner-being movement — the self placing its reliance/shelter on (or wrongly off) God: trust (`batach`, H0982, 39), take refuge/refuge (`chasah`, H2620, 15+4), refuge (`machseh`, H4268, 3), trust/confidence (`mibtach`, H4009, 1: `Psa 71:5·282195`), lean/be sustained (`samak`, H5564, 1: `Psa 71:6·282201`), lie down and sleep in trust (`Psa 3:5·278177`), commit one's way (`Psa 37:5·277828`), taste and see (`Psa 34:8·277275`), make God one's dwelling (`Psa 91:9·285148`), trust the name not chariots (`Psa 20:7·275456`). This mass is genuinely "trust-refuge-security".

**But the keyword/lemma grouping has fused in ~9 instances of distinct movements** — a first-class finding:

1. **Self-separation from evil** — "depart" (`sur`, H5493, 3), cluster **M30 Obedience**, all flagged `is_outlier`: `Psa 119:115·271304 · D106(operation)`="put the evildoers away"; `Psa 139:19·273459 · D106`="actively commands distance from bloodthirsty men, drawing a line"; `Psa 6:8·281978 · D106`="dismisses the workers of evil". This is aversive self-positioning, not reliance/shelter.
2. **Lemma-collision on H5375 (`nasa`, "to lift")** — grouped only because that lemma also glosses "trust/aid": "bring an offering" (`Psa 96:8·285609 · D106`="bring", a worship act) and "show partiality" (`Psa 82:2·283896 · D106`="show favour to the wicked", judicial injustice). Neither is trust; both sit under cluster M19 Trust misleadingly by lemma.
3. **Bodily wasting** — "become gaunt" (`kachash`, H3584, 1): `Psa 109:24·270270 · D102(type)`=state, `D106`="grow lean from fasting" — a physical state, cluster null.
4. **Complacent ease** — "at ease" (`shaanan`, H7600, 1), cluster **M46 Abundance**, outlier: `Psa 123:4·272473 · D106`="be at ease", `D107(target)`="scorning the afflicted" — false security curdling into contempt.
5. **Intimate betrayal** — "close/trusted friend" (H7965, 1), cluster **M33 Peace**, outlier: `Psa 41:9·278491 · D106`="close friend, in whom it trusted... has lifted his heel" — trust-adjacent, but the movement is the betrayal-wound.

Borderline (kept as an **inversion within the movement**, not a fusion): "sought refuge / grew strong" (`azaz`, H5810, 1), cluster M23 Strength, outlier: `Psa 52:7·279853 · D106`="grow strong / seek refuge", `D107`="in his own destruction / greed" — the tyrant making his ruin his stronghold, a false refuge mirroring the true.

**Internal polarity within the coherent core (carried by D105 bearer + D107 target, since no pole/D-field exists).** The trust movement is split into *true trust in God* vs *misplaced/false trust*:
- in **idols**: `Psa 115:8·270911`, `Psa 135:18·273099`, `Psa 31:6·276840` (D107 "in idols" / "dead idols");
- in **wealth**: `Psa 49:6·279391`, `Psa 52:7·279850`, `Psa 62:10·280921` (D107 "their wealth" / "extortion");
- in **man/princes**: `Psa 118:8·271186`, `Psa 118:9·271192`, `Psa 146:3·274210` (D107 "in man"/"in princes");
- **failed/withheld** trust: `Psa 78:22·283097 · D106`="fail to trust", D107="his saving power".
This antithesis is the strongest structuring feature of the family; the source encodes it only in bearer/target/discovery, never in a dedicated dimension.

---

## 2. The trust movement (`batach`, H0982 — 39 instances, the family's core)

**What the word is.** D101 sense clusters as: bare "trust (batach)" plus read-variants — "trust in the LORD", "trust in steadfast love", "trust that keeps unmoved", "trust flows from knowing the name". **D102 type** is mixed: disposition (the settled reliance, e.g. `Psa 84:12·284070`, `Psa 86:2·284332`), affect (the felt turn, e.g. `Psa 13:5·273572`, `Psa 28:7·276390`), action (the deliberate act, e.g. `Psa 55:23·280166`, `Psa 56:3·280276`), volition (the commanded/redirected reliance, e.g. `Psa 37:3·277739`, `Psa 146:3·274210`).

**Operation (D106).** The motion the verb performs: the self "plants itself on God's steadfast love" (`Psa 13:5·273572`), "grounds the self in God so as to be immovable" (`Psa 125:1·272524`), "entrusts itself... timing hope to the dawn" (`Psa 143:8·273936`), "hands over... the timing of its whole life" (`Psa 31:14·276708`), "the heart's reliance meeting God's aid" (`Psa 28:7·276390`), "knowledge grounding reliance" (`Psa 9:10·285875`). Inverted: "misplaced reliance that deadens the truster" (`Psa 115:8·270911`), "reliance on wealth that cannot ransom him from death" (`Psa 49:6·279391`).

**Target (D107).** Overwhelmingly "in the LORD / in God / God's word / God's steadfast love"; the false pole targets "in idols", "in wealth", "in man", "in princes", "in extortion" (§1).

**Locus (D116, corrected).** Two settled values only: `external:god` (trust reaching to God — e.g. `Psa 112:7·270702`, `Psa 115:9·270914`, `Psa 84:12·284070`, `Psa 52:8·279861`) and `internal:ib-state` (trust as the interior's own posture — e.g. `Psa 13:5·273572`, `Psa 21:7·275539`, `Psa 25:2·276026`).

## 3. The refuge / shelter movement (`chasah` H2620 ×19; `machseh` H4268 ×3; `sim` "make dwelling" ×1)

**Operation (D106).** "takes refuge... and rejects the counsel to flee" (`Psa 11:1·272228`); "shelter as the opening posture" (`Psa 16:1·274668`); "shelter in a cluster of strongholds" (rock/fortress/shield, `Psa 18:2·274972`); "shelter blossoming into song" (`Psa 5:11·280672`); "the eyes are fixed on God, seeking refuge" (`Psa 141:8·273754`); "make God his refuge... that he may tell of God's works" (`Psa 73:28·282477`); "deliberate choosing of God as refuge, the act of faith" (`Psa 91:9·285148`). Target (D107) is "in God / under the shelter of God's wings / under God's wings / the Lord GOD". Locus (D116, corrected) is `external:god` for most `chasah`/`machseh` (e.g. `Psa 61:4·280880`, `Psa 64:10·281101`, `Psa 57:1·280347`, `Psa 91:2·285107`) and `internal:ib-state` for the earlier acrostic/plea instances (e.g. `Psa 7:1·283567`, `Psa 31:1·276660`, `Psa 34:22·277236`).

**This is the only instance with a named interior seat:** `Psa 57:1·span 280347 · D104(seat)`="the soul" — "for in you my soul takes refuge".

## 4. Dimensions across the family (aggregate, cited)

- **D102 type distribution:** affect 28, action 22, disposition 18, volition 5, state 2, status 2. The family is predominantly felt/enacted, not stative; the 2 states are `Psa 3:5·278177` (sleep-in-trust) and `Psa 109:24·270270` (become gaunt); the 2 statuses are `Psa 123:4·272473` (at ease) and `Psa 71:5·282195` (mibtach as settled trust).
- **D116 locus (corrected):** `internal:ib-state` 46 · `external:god` 30 · `external:person` 1 (the single person-locus = `Psa 119:115·271304`, the "depart from me, evildoers" separation). Roughly split between trust-as-interior-posture and trust-as-reach-to-God.
- **D103 source (only 6, all God's character):** God's steadfast love (`Psa 52:8·279861`), God's grace (`Psa 56:3·280276`), God as refuge (`Psa 62:8·280986`), God his refuge/strong tower (`Psa 61:4·280880`), God's righteousness (`Psa 71:1·282040`), God's mercy (`Psa 57:1·280347`). Where the source of trust is named, it is always something in God — never the self.
- **D108 manner (11, §0):** the qualifiers are chiefly temporal-total ("forever", "at all times", "from the womb", "from his youth", "till the storms pass") and affective ("without fear" / "in the moment of fear") — trust described as lifelong and fear-facing.
- **D113 prohibition:** the single negation, `Psa 44:6·278837` — trust disowned from the bow/sword.

## 5. The network (genuine `pair` edges only)

37 genuine pair edges exist, **but 26 of their 32 targets lie outside this file** — the real inner-being network mostly leaves the family scope and cannot be traced from this source. Only **6 targets are in-file**, forming three tight passage-internal clusters:

- **Psa 52 (true vs false trust welded):** `279850 (v7, tyrant trusts riches) ↔ 279861 (v8, psalmist trusts God)` on D112(coupling), both directions; plus `279853 (v7, azaz) → 279850` on D112. The antithesis is a bidirectional coupling.
- **Psa 56 (the trust-refrain self-linking):** `280276 (v3) ↔ 280283 (v4)` on D112(coupling), both directions; `280236 (v11) → 280283` on D112. Trust restated across the psalm and knit to itself.
- **Psa 57 (soul's refuge restated):** `280347 ↔ 280351` on D112(coupling), both directions — the soul's refuge and its "shadow of your wings" restatement.

Every other genuine edge (source/target/manner/coupling on Psa 49, 55, 61, 62, 64, 71, 73) points to an out-of-scope span. **Verdict: the in-family network is sparse and passage-local; nothing links across psalms within this file.**

## 6. The interior anatomy the data actually names

Filled seats: **just one — "the soul"** (`Psa 57:1·280347·D104`). Named sources: **God's steadfast love, grace, righteousness, mercy, and God-as-refuge** (the 6 D103 values, §4). Couplings (D112, corrected) name what trust is bound to: the firm/trusting heart (`Psa 112:7·270702`, `Psa 28:7·276390`), fearing God (`Psa 115:11·270838`), taking refuge (`Psa 118:8·271186`), pouring out the heart (`Psa 62:8·280986`), casting one's burden on God (`Psa 55:23·280166`), dwelling in God's tent (`Psa 61:4·280880`), continual praise (`Psa 71:6·282201`). The assembled anatomy: an interior (heart/soul) that leans its whole weight on God's covenant character, coupled to fear, refuge, prayer, and praise — but **located** only once (the soul); the "heart" appears repeatedly in D114 discovery prose yet is never entered as a D104 seat.

## 7. What could not be derived

- **Intensity (D109), specifier (D110), effect (D111): absent on all 77** — no degree, no specifier, no stated consequence is recoverable.
- **Interior seat: unstated on 76 of 77.** "Heart" (`Psa 112:7`, `Psa 28:7`) and "eyes" (`Psa 141:8·273754`) are named in D114 discovery text but were **not captured in the D104 seat field** — a systematic under-population, not a genuine absence of interior location in the text.
- **Source (D103): unstated on 71 of 77** — for most trust/refuge acts the ground is not dimensionally recorded (though often present in the verse/discovery).
- **True-vs-false trust polarity is undimensionalised** — carried only by bearer/target/discovery; no pole or valence field exists to hold it.
- **The cross-verse network is largely untraceable here** — 26 of 32 genuine-edge targets fall outside the file; only 6 in-file links exist (§5).
- **5 instances are cluster-untyped** (§0) and **~9 are fused-in from other movements** (§1) — the term/lemma-cluster cannot, by itself, separate the coherent core from the intrusions.

## 8. Summary

The family is a **genuine, dominant trust→refuge→security movement (~66/77)** — the interior (heart/soul) leaning its whole weight on God's covenant character, structured by a strong but undimensionalised **true-vs-false trust** antithesis (God vs idols/wealth/man/princes). It is diluted by **~9 fused intrusions** (self-separation from evil ×3, `nasa` lemma-collisions ×2, bodily wasting, complacent ease, betrayal) and one inversion (`azaz`). Data-wise the source is **thin on interior anatomy** (1 seat, 6 sources, 0 intensity/specifier/effect), carries **18 D112/D116 swaps** and **213 self-loop non-edges**, and its genuine network is **sparse and passage-local**, with most edges reaching spans outside this file.
