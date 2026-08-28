# Family analysis — `praise-extol-sing` (Psalms), in isolation

> Source: `verse-analysis/psalms/_base-sources/psalms__praise-extol-sing.json` only. Scope: 42 meanings · 172 instances · 94 passages (`meta.counts`). Every claim cites `reference · span_id · Dnnn(label)` into that file. Nothing imported from outside it.

---

## 0. Data-integrity screen (done first)

**D112(coupling)/D116(locus) field-swap — 67 of 172 instances transposed.** In the correct order D116 holds a code (`internal:…`/`external:…`) and D112 holds a prose phrase. In 67 instances the fields are reversed: D112 holds the code and D116 holds the phrase. Read corrected. Examples: `Psa 102:18 · span 268952 · D112="external:god" / D116="paired with the recorded testimony"` (swapped); `Psa 106:1 · span 269572` (swapped); `Psa 96:7 · span 285597` (swapped); `Psa 132:16 · span 272945 · D112="internal:ib-state"` (swapped). The remaining 105 are correctly ordered (D116=code, D112=phrase), e.g. `Psa 100:4 · span 268793`. Corrected locus tally across all 172: **external:god 130 · internal:ib-state 40 · external:person 2** (D116 locus). The swap is a mechanical export defect, not a reading difference; it does not change the corrected values, only which field they live in.

**Self-loop "edges" are not links — 469 of them.** Every instance carries `item_type:"flag" · resolution:"inferred"` self-references whose `to_span` = the span's own id: D105 bearer 172/172, D107 target 154, D112 coupling 112, D108 manner 25, D104 seat 6. These are per-instance flags, **not** network edges, and are excluded from the network (§ network). Genuine network = only `pair` edges (`resolution:"span"`) to a different span: **92** (see network).

**D106 operation "events" — 10, mostly self-inferred.** Ten `item_type:"event"` items sit on D106. Seven are self-inferred (`resolution:"inferred"`, to own span), e.g. `Psa 57:8 · span 280433 · D106(operation) event`. Three link operation to another span (`resolution:"span"`): `Psa 66:2 · span 281320 → 281318`, `Psa 66:8 · span 281381 → 281382`, `Psa 71:8 · span 282216 → 282215`. Per the method's rule (only `pair`/`span` count) these events are held out of the network but noted as operation-chains.

**seat(D104)/manner(D108)="none".** Seat unfilled in **166/172** (only 6 name an organ: mouth/tongue/lips, e.g. `Psa 51:15 · span … · D104="the mouth"` — 2 mouth, 2 tongue, 1 "mouth / opened lips", 1 lips). Manner unfilled ("none") in **138/172**; only 34 carry a manner.

**Absent dimensions (0/172 across the whole family):** D109 intensity, D110 specifier, D111 effect, D113 prohibition. None of the four appears on any instance — no graded intensity, no specifier, no downstream effect, no prohibition anywhere in this family.

**Thinly-filled dimensions:** D103 source present on only **17/172** (all prose reasons for praise, e.g. `Psa 9:2 · … · D103="God made known as a fortress in Zion (v3)"`).

**Cluster NULL — 31 instances / 7 meanings.** No T2 anywhere (0). Null-cluster meanings: `H7891:sing "sing"` (21 inst), `H3051:ascrib "Ascribe"` (4), `H7891:singer "singers"` (2), `H5849:crown` (1), `H5042:pourforth` (1), `H7891:sang` (1), `H5791:wrong` (1). The core family verb **shir/"sing" (H7891, 24 instances across the three sing/singer/sang records) has no term-cluster at all** — the term-cluster layer cannot type the family's own signature act.

**D115 role — no variation.** All 172 instances are `role="characteristic"`; qualifier and standalone never occur. The role dimension carries no discriminating information in this family.

---

## 1. Coherence — does the label fit?

**Largely yes, with a keyword-fusion fringe.** The centre of mass is one coherent inner-being movement: the human interior turning outward in vocal worship — halal/praise (`H1984`, 38+2 inst), yadah/give-thanks-praise (`H3034`, 18+1), tehillah/praise (`H8416`, 15), zamar/sing-praises (`H2167`, 14+6+2+2+1+1), shir/sing (`H7891`, 21+2+1), ranan/sing-for-joy-shout (`H7442`, 4+3+2+1+1+1), rum/extol (`H7311:extol`), kabed/glorify (`H3513`), gadal/magnify (`H1431`), shabach/high-praise (`H7318`). D106 operation is dominated by praise (37), sing (18), sing praises (15). This is a real, single movement.

**But the keyword grouping has drawn in non-praise homographs** — a first-class finding. Distinct movements fused in:

- **Affliction / iniquity (not praise) — 3 instances.** `H0205:troubl "trouble"` (aven): `Psa 55:3 · span 280176 · D106="drop / bring down" · D105(bearer)="the wicked"` and `Psa 90:10 · span 284958 · D101="trouble (aven)" · D105="our life"`; and `H5791:wrong "wronged"` (avath): `Psa 119:78 · span 272083 · D106="wrong the psalmist" · D105="the insolent"`. These are harm done *to* the IB, the opposite valence from praise; matched only on an English keyword collision ("trouble", "wronged").
- **Self-exaltation / pride against God — 1–2 instances.** `H7311:exalt "exalt"` at `Psa 66:7 · span 281374 · D101="exalt / lift up oneself (rum)" · D105="the rebellious" · D107="against God"` is negative self-exaltation (M08 Pride sense), not worship. Borderline spatial: `H7311:higher "higher"` at `Psa 61:2 · span 280870 · D101="be high / higher (rum)" · D107="the rock higher than I"` — rum used of elevation, not praise.
- **God's action on man (IB as recipient, not agent) — 1 instance.** `H5849:crown "crowned"` at `Psa 8:5 · span 284927 · D106="the meditation on…" · D105="mankind" · D107="dignity"` — God crowns; the human IB is object, not the one praising.
- **Physical breath — 1 instance.** `H5397:breath "breath"` at `Psa 150:6 · span 274602 · D105(bearer)="all that breathe"` — the breath is the *bearer/instrument* of praise, not itself the praise act (cluster M25 Life).

**Term-cluster codes are unreliable here and must not be read as the movement.** The `is_outlier` flag correctly marks 10 meanings as cluster-crossovers, but for most of these the *sense* is plainly praise while the M-code points elsewhere because the lemma's home cluster differs: `H7311:extol → M08 Pride` yet `Psa 118:28 · span 271139 · D106="extol" · D107="God"` is worship; `H7623 (shabach) → M33 Peace` yet `Psa 117:1 · … · praise`; `H1984:glory → M08 Pride` yet `Psa 105:3 · span 269471 · D106="glory / boast" · D107="in God's holy name"` is doxological. So M22 Praise (12 meanings) + M42 Speech (12) capture the true centre; **M08 Pride (4), M33 Peace (4), M10 Sin (1), M04 Joy (1), M25 Life (1) are term-cluster artefacts of the lemma, not distinct IB movements** — except the genuine misfits listed above (trouble, wronged, exalt-rebellious). Bottom line: the family is coherent as "outward vocal worship"; strip the ~4–5 homograph misfits and the M-code noise, and one movement remains.

---

## 2. The movements / operations evidenced

### 2.1 The core act: interior → voiced worship of God (the family)
Type is overwhelmingly **action (128/172)** with an **affect (23)** undertone, plus status (9), volition (6), state (4), cognition (2) (D102). The operation (D106) is speech-act praise: praise 37, sing 18, sing praises 15, glorify 4, extol/ascribe 3 each. Target (D107) is God under many names — "the LORD" 18, "God" 18, "to God" 14, "God's word" 5, "to God's name" 4 (`Psa 138:2` type), "a new song to the LORD" (`Psa 96:1 · span 307141`). Corrected locus (D116) puts **130/172 external:god** — the movement is centrifugal, the interior directed outward and upward to God. Illustrative: `Psa 9:1 · … · D101="give thanks (yadah)"`; `Psa 30:1 · span 276570 · D101="extol you, for you drew me up" · D102=affect`; `Psa 150:6 · span 274602 · D101="every breath praises"`.

### 2.2 The affect / volitional sub-current (praise as inner state, not only act)
40/172 sit **internal:ib-state** (D116 corrected) — praise turned inward as disposition rather than outward act. The D112 coupling phrases name it: `praise-all-my-life`, `praise-is-fitting`, `praise-response`, `extol-forever`, `saints-horn-praise`, `not-be-silent`, `sing-for-bounty` (all `internal:ib-state`, one instance each). Volition (6) and affect (23) instances carry this: `Psa 57:7 · span 280430` (steadfast-heart singing), `Psa 108:1 · span 270079 · D108="…the steadfast heart"`. So the data models praise as both an act performed and a settled interior orientation ("my heart is steadfast, I will sing").

### 2.3 Bearer — whose inner being
The IB is predominantly the individual worshipper: **the psalmist 60**, the worshipper(s) 24+3, David 6, the saints/godly 4+3 (D105). But it widens to the collective and cosmic: worshippers 24, the servants 6, the peoples 6, the people 2, plus **cosmic/collective bearers that strain the "individual human IB" frame** — "all the earth" 9, "all nations" 2, "the kingdoms of the earth" 2, "the nations" 2+1, "all that breathes" 1, "the heavenly beings / worshippers" 1. The summons-to-praise psalms (Psa 96–100, 117, 148–150) deliberately dilate the bearer from the self to all creation; the file records this faithfully (e.g. `Psa 117:1 · span 271023 · D105="all nations"`), but it is worship *ascribed to* creation, not an individual interior process.

### 2.4 What moves it (source, D103) — thin but consistent
Source is filled only 17 times, always as the *ground/prompt* for praise, and always God's prior act: "God made known as a fortress in Zion" (`Psa 9:2`), "prompted by God's steadfast love, meditated in the temple", "prompted by God's deliverance, salvation and righteousness" (`Psa 9:14`), "because God's faithfulness reaches to the clouds". Where source is given, praise is **response**, not spontaneous — the interior is moved by remembered divine action. But 155/172 leave the source unstated (see § not-derivable).

### 2.5 Manner (D108) — mostly unstated, occasionally embodied
138/172 "none". The 34 filled manners are performative/embodied: "with the lyre", "with the harp", "with joyful lips", "with a song", "in the morning", "to the ends of the earth", "exulting before him", "rousing his glory, harp, lyre, and the dawn" (`Psa 108:2` type), "forever and ever". One is counter-current: `Psa 137:4 · span 308025 · D108="unwilling, overruled"` — song refused in exile, the only negated manner.

### 2.6 Seat (D104) — almost never localised
166/172 unlocalised. The interior organ is named only where the act is explicitly oral: mouth (2), tongue (2), "mouth / opened lips" (1), lips (1) — e.g. `Psa 51:15`-type "open my lips". The family locates praise at the **voice**, not the heart, on the rare occasions it localises at all; the heart appears in couplings/manner (steadfast heart) but not as a filled D104 seat.

---

## The network (genuine `pair` edges only)

**92 pair edges** (`resolution:"span"`, to a different span). Direction is `None` on all 92 — the network is undirected. Distribution by dimension:

- **D112 coupling — 51 edges (the backbone).** Praise-spans bound to adjacent worship-acts in the same passage: `Psa 56:10 · span 280229 ↔ 280233` (reciprocal — both directions present), `Psa 63:5 · span 281066 → 281062`, `Psa 69:30 · span 281826 → 281830`, `Psa 74:21 · span 282624 → 282622`. Coupling is what actually knits the family together: praise links to praise/thanks/blessing/song across neighbouring verses.
- **D107 target — 15 edges.** Shared object of worship linked across spans: `Psa 69:30 · span 281826 → 281827`, `Psa 71:22 · span 282144 → 282146`, `Psa 68:4 · span 281650 → 281653` — parallel praise-verbs converging on the same divine target.
- **D103 source — 17 edges.** Shared ground linked across spans: `Psa 48:1 · span 279161 → 306337`, `Psa 57:7 · span 280430 → 280405`, `Psa 68:4 · span 281650 → 281655`.
- **D108 manner — 9 edges.** Shared performative manner: `Psa 63:5 · span 281066 → 281067`, `Psa 67:3 · span 281403 → 281407`, `Psa 66:2 · span 281320 → 281319`.

The network is **sparse and passage-local** (edges connect spans within the same psalm, e.g. all the Psa 66–71 clusters) and **undirected**. There is no cross-passage or family-wide graph — praise instances are chained to their immediate liturgical neighbours, chiefly by coupling. The 469 self-loops and the self-inferred D106 events are excluded per method.

## The interior anatomy the data actually names

Assembling only filled fields: the family names a **voice-seated, God-directed, response-driven** interior. Filled **seats**: mouth, tongue, lips (voice only; heart never a filled D104). Filled **sources**: God's steadfast love, faithfulness, deliverance, salvation, being-a-fortress (always divine prior act). Filled **internal couplings** (40 internal:ib-state): praise-all-my-life, praise-is-fitting, extol-forever, steadfast-heart singing, not-be-silent, saints-horn-praise — the disposition of continual, fitting, unsilenceable praise. Filled **manners**: lyre/harp/joyful-lips/morning/exulting. The corrected **locus** anatomy is 130 external:god / 40 internal:ib-state / 2 external:person — an interior whose native motion is outward toward God, with a settled inward reservoir of praise-as-orientation.

## What could not be derived from this source

- **No intensity, specifier, effect, or prohibition anywhere** (D109/D110/D111/D113 = 0/172). The data cannot say how strong the praise is, what it specifies, what it produces in the IB downstream, or where it is forbidden. The one exilic refusal (`Psa 137:4`, "unwilling, overruled") is coded as manner, not as D113 prohibition.
- **Source/motive unstated for 155/172.** For all but 17 instances the file does not say *why* the IB praises — whether spontaneous or prompted is not derivable.
- **Seat unlocalised for 166/172.** Where in the interior praise arises (heart? spirit? ruach?) is not derivable except as "the voice" in 6 oral instances.
- **Manner unstated for 138/172.** How praise is performed is mostly blank.
- **Role carries no information** (172/172 "characteristic"); qualifier/standalone distinctions are not derivable here.
- **Term-cluster typing is unreliable** for this family: shir/"sing" (24 inst) is NULL-clustered, and M08/M33/M10/M04/M25 codes are lemma artefacts, not IB movements. Cluster code cannot be trusted to name the movement — the sense (D101) and operation (D106) must.
- **Bidirectionality/agency of the network is not derivable** — all 92 pair edges have `direction:null`.
- **D112/D116 must be read corrected** for 67 instances before any coupling/locus value is trusted.
- **Bearer of ~19 instances is cosmic/collective** ("all the earth", "all nations", "all that breathes"), which is worship ascribed to creation rather than an individuated human interior — the individual-IB reading is not derivable for those.

## Summary

`praise-extol-sing` is one coherent inner-being movement — the human interior turning outward in voiced, God-directed worship (halal/yadah/zamar/shir/ranan; action-with-affect; 130/172 external:god; response to God's remembered acts where source is given). It is voice-seated (never heart-seated in D104), sparsely and undirectedly networked chiefly by coupling (51 of 92 pair edges), and flat in intensity/effect (D109–D111/D113 wholly absent). The keyword grouping has fused in ~4–5 non-praise homographs (aven "trouble" ×2, avath "wronged", rum self-exaltation of the rebellious, God-crowns-man, physical "breath"), and the term-cluster codes (M08/M33/M10/M25 outliers; shir NULL) do not name the movement — sense and operation do. Integrity caveats: 67 D112/D116 swaps, 469 non-edge self-loops, 166 empty seats, 138 empty manners.
