# Family analysis — Psalms · `rebellion-stubbornness` (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__rebellion-stubbornness.json` only. 20 meanings · 31 instances · 27 passages · all genre `poetic/wisdom`. Every claim cited `reference · span_id · Dnnn(label)`. Nothing imported from outside this file.

## Roster (meaning → instances, lemma, cluster)

| # | meaning (char_key) | lemma | cluster | inst | is_outlier |
|---|---|---|---|---|---|
| 1 | rebelled (H4784:rebell) | H4784 | M30(Obedience) | 5 | no |
| 2 | forsaken (H5800:forsaken) | H5800 | M20(Doubt) | 3 | **yes** |
| 3 | rebellious (H5637:rebelliou) | H5637 | **null** | 3 | no |
| 4 | forsake (H5800:forsak) | H5800 | M20(Doubt) | 2 | **yes** |
| 5 | rebellious (H4784:rebelliou) | H4784 | M30(Obedience) | 2 | no |
| 6 | refuses (H3985:refus) | H3985 | **null** | 2 | no |
| 7 | Refrain (H7503:refrain) | H7503 | M24(Weakness) | 1 | **yes** |
| 8 | despised (H3988:despis) | H3988 | M06(Hate) | 1 | no |
| 9 | despised (H0959:despis) | H0959 | M06(Hate) | 1 | no |
| 10 | fall away (H7846:fallaway) | H7846 | **null** | 1 | no |
| 11 | hide (H3582:hide) | H3582 | **null** | 1 | no |
| 12 | leave (H5800:leav) | H5800 | M20(Doubt) | 1 | **yes** |
| 13 | rebel (H4784:rebel) | H4784 | M30(Obedience) | 1 | no |
| 14 | rebelled against (H4784:rebelledagainst) | H4784 | M30(Obedience) | 1 | no |
| 15 | revile (H5006:revil) | H5006 | M06(Hate) | 1 | no |
| 16 | sits (H3427:sit) | H3427 | **null / T2(Supplementary)** | 1 | no |
| 17 | spurned (H5006:spurn) | H5006 | M06(Hate) | 1 | no |
| 18 | stubborn (H5637:stubborn) | H5637 | **null** | 1 | no |
| 19 | stubborn (H8307:stubborn) | H8307 | M30(Obedience) | 1 | no |
| 20 | worm (H8438:worm) | H8438 | **null** | 1 | no |

Cluster tally by instance: M30 Obedience 10 · M20 Doubt 6 (outlier) · M06 Hate 4 · M24 Weakness 1 (outlier) · null 9 · null/T2 1 = 31.

---

## 0. Data-integrity screen

### 0.1 D112(coupling) / D116(locus) field-swap — **7 of 31 instances transposed**
Correct order = D116 locus holds a code (`internal:`/`external:`), D112 coupling holds a phrase. The following invert that (D112 holds the code, D116 holds a prose phrase) and must be **read corrected**:

| span_id | reference | D112(coupling) raw | D116(locus) raw | corrected locus |
|---|---|---|---|---|
| 269848 | Psa 106:7 | `external:god` | "paired with the failure to remember" | external:god |
| 269871 | Psa 107:11 | `external:god` | "paired with spurning his counsel" | external:god |
| 269772 | Psa 106:43 | `external:god` | "paired with their self-willed counsel" | external:god |
| 269666 | Psa 106:24 | `internal:ib-state` | "paired with having no faith" | internal:ib-state |
| 268833 | Psa 101:3 | `internal:ib-state` | "paired with the hated work" | internal:ib-state |
| 307393 | Psa 105:28 | `external:god` | "paired with performing the signs" | external:god |
| 269874 | Psa 107:11 | `external:god` | "paired with rebelling" | external:god |

The other 24 instances carry the fields in correct order (code in D116, phrase in D112). Note the borderline: `Psa 5:10 · span 280669 · D112(coupling)` = "rebelled-against-God" is a phrase (no `internal:`/`external:` prefix), D116 = `internal:ib-state` — **not** swapped.

### 0.2 Self-loop "edges" are not real links
Every instance's `bearer`(D105)/`target`(D107)/`coupling`(D112) flag-edge is `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span`= the span's own id. These are **self-loops, not network edges** and are excluded. That covers all edges on **26 of 31** instances.

Genuine cross-span edges (`resolution:"span"`, `to_span` ≠ own id) exist on only **5** instances — and **every one points OUT to a co-text span that is not itself a family master** (targets 281370, 281374, 281483, 281673, 282949, 282951, 282532, 282535 are none of the 31 instance ids). See §The network.

### 0.3 seat(D104) / manner(D108) = "none"
- **seat D104 "none" in 30 of 31.** The only filled seat: `Psa 77:2 · span 282950 · D104(seat)` = "the soul (nephesh)" (`pair`, span→282949).
- **manner D108 "none" in 28 of 31.** Filled: `Psa 77:2 · span 282950 · D108(manner)` = "resolute inconsolability"; `Psa 68:6 · span 281676 · D108(manner)` = "in a sun-scorched land"; `Psa 74:10 · span 282534 · D108(manner)` = "forever". All three `inferred`.

### 0.4 Absent dimensions
- **D109 intensity, D110 specifier, D111 effect, D113 prohibition — absent from all 31 instances.** No ledger carries them.
- **D103 source — present in only 1 of 31:** `Psa 66:7 · span 281373 · D103(source)` = "watched by God's eyes on the nations (v7)" (`pair`, span→281370). Absent in the other 30.

### 0.5 Cluster null / T2
- **Cluster code null in 9 instances:** rebellious-sarar 281373/281491/281676 (Psa 66:7, 68:18, 68:6); refuses/refused 282950/283013 (Psa 77:2, 78:10); fall away 268833 (Psa 101:3); hide 283197 (Psa 78:4); stubborn-sarar 283442 (Psa 78:8); worm 275781 (Psa 22:6). The term-cluster cannot type these.
- **Cluster code null with candidate T2:** `Psa 1:1 · span 275352` (H3427:sit, `all_candidates:"T2(Supplementary)"`). Coded `D115(role)=characteristic` despite the T2 (supplementary/reference) candidacy — a role/candidate mismatch worth flagging.

### 0.6 Uniform fields (no discrimination)
- **D115(role) = "characteristic" for all 31.** No qualifier/standalone anywhere, including the T2 candidate (275352) and the outliers.
- **D105(bearer) resolution `inferred` for all 31.** No bearer is asserted from the surface.

---

## 1. Coherence check — the label does NOT hold; it fuses ≥5 movements

The core defiance terms genuinely cohere (marah "rebel" H4784, sarar "rebellious/stubborn" H5637, sheriruth "stubborn" H8307, naats "spurn/revile" H5006, maas "despise" H3988, set "fall away" H7846, maen "refuse" H3985) — a coherent **revolt-against-God** movement. But the keyword grouping (chiefly the lemma **azab H5800 "forsake/leave"** and several **negations/commands**) has pulled in material that is not rebellion and in places its opposite. Distinct movements fused under the one label:

- **A. Active rebellion against God** (the true core, coherent) — e.g. `Psa 78:17 · span 283047 · D106(operation)` "rebel"; `Psa 106:43 · span 269772 · D101(sense)` "rebellious (marah)"; `Psa 81:12 · span 283803 · D101(sense)` "stubborn (sheriruth)"; `Psa 78:10 · span 283013 · D106(operation)` "refuse" (to walk in the law); `Psa 106:24 · span 269666 · D106(operation)` "despise" (the land); `Psa 107:11 · span 269874 · D106(operation)` "spurn" (his counsel); `Psa 101:3 · span 268833 · D106(operation)` "fall away". ≈17 instances.
- **B. Felt divine abandonment / lament** (not rebellion) — `Psa 22:1 · span 275573 · D114(discovery)` "not doubt that God exists but the agony of his felt absence"; `Psa 22:6 · span 275781 · D101(sense)` "I am a worm, not a man" (self-worth collapse); `Psa 77:2 · span 282950 · D101(sense)` "refuse (maen — refuses to be comforted)" — grief, not defiance.
- **C. Trust that outlasts abandonment** (opposite of rebellion) — `Psa 27:10 · span 306194 · D101(sense)` "though parents forsake, God takes me in".
- **D. Mortality / dispossession** (not IB-defiance) — `Psa 49:10 · span 279279 · D101(sense)` "leave / abandon (azab — wealth to others)".
- **E. Being despised BY others** (passive estate, not the subject rebelling) — `Psa 119:141 · span 271469 · D101(sense)` "be despised (bazah)"; and the enemy's revolt against God `Psa 74:10 · span 282534 · D101(sense)` "revile / spurn (naats)".
- **F. Commanded self-mastery / negated rebellion — VIRTUE, the label's inverse** — `Psa 1:1 · span 275352 · D114(discovery)` "nor sits in the seat of scoffers" (the blessed man's refusal); `Psa 78:4 · span 283197 · D101(sense)` "hide (kachad, **refused** — we will NOT hide)"; `Psa 37:8 · span 277849 · D101(sense)` "refrain from anger, forsake wrath"; `Psa 105:28 · span 307393 · D101(sense)` "rebel (marah, **negated** — did not rebel)" (Moses & Aaron's obedience); `Psa 119:87 · span 272143 · D101(sense)` "forsake (azab, **negated** — I have NOT forsaken your precepts)".

**First-class finding:** the family conflates revolt-against-God (A) with its own opposites — lament (B), trust (C), and explicitly negated/commanded virtue (F) — plus death (D) and passive being-despised (E). The fusion is driven by shared ESV keyword and by the azab homograph, not by a shared inner-being movement. The four `is_outlier` records (all H5800 azab → M20 Doubt: 275573/306194/272143/271916/284674; and H7503 → M24 Weakness: 277849; expected M10 Sin) are the visible seam of this fusion.

---

## 2. The movements/operations evidenced (cited)

### 2.1 Rebel — marah (H4784), the dominant motion (9 instances)
Type ranges over action/volition/disposition; operation "rebel". Consistently targets God and is `external:god` (corrected where swapped):
- `Psa 106:7 · span 269848 · D106(operation)` "rebel"; D114 "the first act of the catalogue, defiance at the very edge of deliverance."
- `Psa 107:11 · span 269871 · D107(target)` "against the words of God"; coupled with spurning his counsel.
- `Psa 5:10 · span 280669 · D102(type)` "volition"; D114 "their interior is set against God himself; their treachery to the psalmist is really revolt against God." (locus `internal:ib-state`.)
- `Psa 78:17 · span 283047` (passage anchor) · D114 "defiance in the very place of God's provision."
- `Psa 78:40 · span 283209 · D114(discovery)` "the recurring, wearying defiance."
- `Psa 106:43 · span 269772 · D102(type)` "disposition"; "deliverance met again with rebellion."
- `Psa 78:8 · span 283443 · D102(type)` "status" — "a stubborn and rebellious generation" (anchor).
- `Psa 78:56 · span 283324 · D106(operation)` "rebel" — "defiance persisting into settled possession."
- **Negated:** `Psa 105:28 · span 307393 · D106(operation)` "not rebel" — Moses & Aaron's obedience (movement F).

### 2.2 Stubborn / rebellious as settled status — sarar (H5637), sheriruth (H8307)
- `Psa 66:7 · span 281373 · D102(type)` "status"; D106(operation) "exalt themselves"; the only record with D103(source) filled.
- `Psa 68:18 · span 281491 · D106(operation)` "receive gifts (even they), that God may dwell" — D114 "grace reaching even the defiant."
- `Psa 68:6 · span 281676 · D106(operation)` "dwell in a parched land" — D114 "rebellion's reward is a scorched, homeless waste."
- `Psa 78:8 · span 283442 · D101(sense)` "be stubborn (sarar)" (anchor); coupled with "rebelliousness and the unsteady heart."
- `Psa 81:12 · span 283803 · D114(discovery)` "the obstinacy God finally left them to, judgment by abandonment"; D107(target) "in heart".

### 2.3 Refuse / spurn / despise / fall away — the refusal cluster
- `Psa 77:2 · span 282950` refuse (maen) — grief refusing comfort; **the one seated instance** (nephesh); movement B.
- `Psa 78:10 · span 283013 · D106(operation)` "refuse" (to walk in the law) — willed rejection of obedience.
- `Psa 107:11 · span 269874 · D106(operation)` "spurn" (the counsel of the Most High).
- `Psa 74:10 · span 282534 · D106(operation)` "revile / spurn" (naats) — the enemy reviling God's name; D108(manner) "forever".
- `Psa 106:24 · span 269666 · D106(operation)` "despise" (the pleasant land).
- `Psa 119:141 · span 271469` be despised (bazah) — passive estate (movement E).
- `Psa 101:3 · span 268833 · D106(operation)` "fall away / turn aside" — the apostates David hates.

### 2.4 Forsake / leave — azab (H5800), the fusion seam
- **Defiance:** `Psa 119:53 · span 271916 · D106(operation)` "forsake the law" (the wicked); `Psa 89:30 · span 284674 · D114(discovery)` "the apostasy of the sons."
- **Lament/trust/mortality (not defiance):** `Psa 22:1 · span 275573` (anchor) felt abandonment; `Psa 27:10 · span 306194` (anchor) trust; `Psa 49:10 · span 279279` leave wealth at death.
- **Negated virtue:** `Psa 119:87 · span 272143 · D101(sense)` "forsake (azab, negated)".

### 2.5 The commanded / negated virtues (movement F, cited above)
`Psa 1:1 · span 275352` sit-not; `Psa 78:4 · span 283197` hide-refused; `Psa 37:8 · span 277849` refrain from anger.

---

## The network

Using only genuine cross-span edges (`resolution:"span"`, different span; §0.2), **the family has no internal network** — no master links to another master. All genuine edges radiate outward from 5 instances to their own verse's co-text:

- `Psa 66:7 · span 281373`: D103(source)→281370; D106(operation)→281374; D112(coupling)→281374.
- `Psa 68:18 · span 281491`: D112(coupling)→281483.
- `Psa 68:6 · span 281676`: D112(coupling)→281673.
- `Psa 77:2 · span 282950`: D104(seat)→282949; D107(target)→282951; D112(coupling)→282949.
- `Psa 74:10 · span 282534`: D107(target)→282535; D112(coupling)→282532.

The remaining 26 instances carry only self-loop non-edges. The network is therefore **maximally sparse**: 8 real edges, all one-directional (`direction:null`), none between two family members, concentrated in just 5 spans. No movement-to-movement relationship inside this family can be read from the data.

## The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seat:** only one interior seat is named across all 31 — **the soul / nephesh** (`Psa 77:2 · span 282950 · D104(seat)`). "Heart" appears in verse text (Psa 81:12 "stubborn hearts", Psa 78:8 "heart not steadfast") but is **not** coded into D104 for any span — so the interior locus of rebellion is left unstated by the ledger.
- **Source:** only one — **God's watching eyes on the nations** (`Psa 66:7 · span 281373 · D103(source)`). What moves rebellion is otherwise unnamed.
- **Coupling (corrected):** where genuine, rebellion is bound to self-exaltation (281373→281374), to the paradox of God dwelling among the rebellious (281491→281483), to the barren land set against the homed (281676→281673), and grief is bound to the soul and refused comfort (282950→282949). Otherwise coupling is a flag phrase (e.g. "paired with the sinning" 283047; "paired with grieving him" 283209; "paired with the testing" 283324).
- **Locus (corrected):** the field resolves to either `external:god` (rebellion aimed outward at God/his word — 283047, 283209, 269848, 269871, 271916, 284674, 283324, 307393, 283013) or `internal:ib-state` (the settled inner condition — 280669, 283442, 283443, 283803, 281373, 281491, 281676, 275573, 306194, 275352, 277849, 275781, 282950, 271469, 282534) — plus one `external:person` (283197). The data thus splits rebellion between an outward act against God and an inward stubborn state, but names no seat for the latter beyond one nephesh.

## What could not be derived

- **No interior seat for rebellion/stubbornness.** 30 of 31 have D104(seat)="none"; the coded anatomy gives no heart/spirit/ruach location for the family's core motion, though the verse text repeatedly says "heart".
- **No source/cause for 30 of 31.** D103 filled once only (281373).
- **No intensity, specifier, effect, or prohibition anywhere** (D109/D110/D111/D113 absent) — degree, sub-type, consequence and any "thou-shalt-not" cannot be read.
- **No manner for 28 of 31** (D108 "none").
- **No inner-being network.** No master-to-master edge; movement interrelation is not derivable (§The network).
- **Whose IB is under study is often not the psalmist's own interior** — bearers are largely third-party groups ("the fathers", "the prisoners", "the enemies", "the rebellious", "David's children"), all `inferred`; the reflexive first-person interior is confined to a handful (282950, 275573, 275781, 272143, 271469).
- **Cluster typing fails for 10 of 31** (null, incl. one T2 candidate coded as role=characteristic — a mismatch), and mis-types 6 more as M20 Doubt / M24 Weakness against the expected M10 Sin (the outliers).
- **Role gives no discrimination** — uniformly "characteristic" (31/31), so qualifier vs standalone vs characteristic cannot separate the fused movements.

## Summary

`rebellion-stubbornness` is a **fused** family: a coherent revolt-against-God core (marah/sarar/sheriruth/naats/maas/set/maen, ~17 instances) has been keyword-merged — chiefly via the azab "forsake" homograph and several negations/commands — with felt divine abandonment, trust, death, passive being-despised, and explicitly negated/commanded **virtue** (its own opposite). Integrity issues: 7 D112/D116 swaps (listed), all networks are self-loop non-edges except 8 outward edges on 5 spans (no internal network), seat named once (nephesh, Psa 77:2), source named once (Psa 66:7), and D109/D110/D111/D113 wholly absent. The ledger names rebellion's outward object (God) far better than its interior seat, which it almost never records.
