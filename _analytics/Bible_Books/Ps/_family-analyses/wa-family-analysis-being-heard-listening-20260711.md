# Family analysis — `being-heard-listening` (Psalms)

> Source: `verse-analysis/psalms/_base-sources/psalms__being-heard-listening.json` (in isolation). Scope = that one file only.
> Counts (meta): 6 meanings · 20 instances · 16 passages. Cited as `reference · span · Dnnn(label)`.

Family membership (char_key → cluster → instances):
- `H8085:hear` → M41(Remembrance) — 10 instances
- `H8085:heard` → M41(Remembrance) — 5
- `H8085:listen` → M41(Remembrance) — 2
- `H0238:giveear` → M41(Remembrance) — 1
- `H7592:ask` (asked) → M21(Prayer) — 1
- `H2795:deaf` → cluster **null** — 1

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling)/D116(locus) field-swap — 4 instances transposed
Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. These four hold a prose phrase in D116 and the code in D112, i.e. **swapped** — read them corrected:

| span | ref | recorded D116 locus (phrase) | recorded D112 coupling (code) | corrected D116 locus | corrected D112 coupling |
|---|---|---|---|---|---|
| 285506 | Psa 95:7 | "paired with not hardening the heart" | `external:god` | `external:god` | paired with not hardening the heart |
| 285696 | Psa 97:8 | "paired with being glad" | `internal:ib-state` | `internal:ib-state` | paired with being glad |
| 272972 | Psa 132:6 | "paired with going to worship" | `external:god` | `external:god` | paired with going to worship |
| 285174 | Psa 92:11 | "paired with seeing their downfall" | `internal:ib-state` | `internal:ib-state` | paired with seeing their downfall |

All four carry the coupling as `item_type:flag / resolution:inferred`, so the correction affects the read only, not the genuine-edge set. All remaining 16 instances have D112/D116 in correct order.

### 0.2 Self-loop "edges" are not real links
Every instance carries a D105(bearer) edge `from_span:null → to_span:<own id>` (`flag`, `inferred`) — a self-marker, **not a network edge**. Several instances add the same pattern on D106/D107/D108/D112 as `flag/inferred` to self (e.g. `Psa 58:5 · span 280502` on D106, D107, D108). None of these are links.

**Genuine `pair` edges (`resolution:"span"`, to a different span) — 9 total, from 5 instances:**
- `Psa 51:8 · span 279771 · D107 target` → 279772 (joy and gladness)
- `Psa 51:8 · span 279771 · D112 coupling` → 279776 (broken bones rejoicing)
- `Psa 58:5 · span 280502 · D112 coupling` → 280492 (incorrigibility of their venom)
- `Psa 59:7 · span 280640 · D112 coupling` → 280643 (God's mocking laughter, v8)
- `Psa 66:16 · span 281284 · D112 coupling` → 281286 (God-fearers summoned; parallels come-and-see)
- `Psa 62:11 · span 280933 · D107 target` → 280935 (power/steadfast love belong to God)
- `Psa 62:11 · span 280933 · D108 manner` → 280931 (once God spoke, twice heard)
- `Psa 66:8 · span 281382 · D107 target` → 281381 (sound of God's praise)
- `Psa 66:8 · span 281382 · D112 coupling` → 281376 (blessing God)

**All nine to_spans lie OUTSIDE the family's 20 spans.** There is **no intra-family edge** — nothing in this file links one family span to another. Direction is `null` on every edge (no directionality derivable). Network is therefore sparse (9 edges from 5 of 20 spans) and outward-pointing only.

### 0.3 seat(D104)/manner(D108) = "none"
- **D104 seat = "none" in all 20 instances** (100% unfilled). No interior seat is named anywhere, even where the verse text supplies an organ — e.g. `Psa 78:1 · span 283001` "incline your ears", `Psa 92:11 · span 285174` "my ears have heard", `Psa 95:8` "harden your hearts" — none captured as a seat. A derivation gap, not an absence in the text.
- **D108 manner = "none" in 18 of 20.** Filled only in `Psa 58:5 · span 280502 · D108(manner)` ("stopping its ear, willfully deaf", flag/inferred) and `Psa 62:11 · span 280933 · D108(manner)` ("once God spoke, twice heard", pair).

### 0.4 Absent dimensions (across all 20)
Never present on any instance: **D103 source · D109 intensity · D110 specifier · D111 effect · D113 prohibition.** Each instance's ledger is only 101,102,104,105,106,107,108,112,114,115,116. So source, intensity, specifier, effect and prohibition cannot be derived for this family at all.

### 0.5 Cluster NULL / T2
- `H2795:deaf` (`Psa 38:13 · span 277903`) has `cluster.code=null` — the term-cluster cannot type it. 1 NULL, no T2.
- The remaining 19 spans are M41(Remembrance) ×18 and M21(Prayer) ×1.
- **`is_outlier` = false on all 6 meanings** — including the M21 and the null-cluster meanings, which diverge from the M41 core (see §1). The outlier flag did not fire where it plausibly should.
- Note also that the core auditory verbs (shama/azan) are typed under **M41 "Remembrance"**, not an obvious hearing/heeding cluster; the term-cluster name is a loose fit for the reception movement.

---

## 1. Coherence — does the label fit the data?

The label `being-heard-listening` fits **18 of 20** instances but **fuses three distinct movements**:

**(a) Core — auditory reception (shama/azan): 18 instances, all M41.** hear / heed / listen / give ear. Coherent single movement. Split by valence:
- *Attentive/summoned hearing of God or tradition* — `Psa 85:8 · span 284224` (let me hear what God will speak), `Psa 81:5 · span 283847` (I hear a language not known), `Psa 81:8 · span 283868` (Hear, O my people), `Psa 95:7 · span 285506` (if you hear his voice), `Psa 78:3 · span 306759` (things we have heard), `Psa 78:1 · span 283001 · D101(sense)` give ear/attend (azan), `Psa 62:11 · span 280933` (twice have I heard), `Psa 132:6 · span 272972` (we heard of it).
- *Refused / failed hearing* — `Psa 81:11 · span 283796 · D101(sense)` "listen (shama, failed)", `Psa 58:5 · span 280502` (does not hear the charmers), `Psa 59:7 · span 280640` ("Who will hear us?").
- *Longed-for / wistful hearing* — `Psa 51:8 · span 279771` (let me hear joy), `Psa 81:13 · span 306919` (Oh that my people would listen).
- *Hearing of vindication / news* — `Psa 92:11 · span 285174`, `Psa 97:8 · span 285696`, `Psa 66:16 · span 281284`, `Psa 66:8 · span 281382` (make heard).

**(b) Petition-and-answer: 1 instance, M21(Prayer)** — `Psa 21:4 · span 275515 · D106(operation)` "he asked life of God, who gave it". Read is *asking-and-receiving*, not hearing/listening. Different movement, pulled in by the being-heard-by-God theme (`D101 sense` = "asked life, received it"; `D102 type` = volition).

**(c) Chosen silence / self-deafness: 1 instance, cluster null** — `Psa 38:13 · span 277903 · D106(operation)` "the self becomes like a deaf man who does not hear... deliberate silence before accusers" (`D102 type` = volition). This is the interior *refusing to answer*, not receiving — thematically adjacent (deafness) but the opposite motion.

**Finding:** the keyword grouping is dominantly coherent (auditory reception) but has fused in one *petition* movement (span 275515) and one *chosen-silence/non-answering* movement (span 277903). Both are marked `is_outlier:false` despite non-M41 / null clusters.

---

## 2. The movements/operations evidenced

Working the dimensions as the IB's anatomy, all cited.

### 2.1 sense (D101) / type (D102)
Two Hebrew roots: **shama** (H8085, 17 spans) and **azan** (H0238, 1 span, `Psa 78:1 · span 283001`); plus **ask** (H7592, `Psa 21:4 · span 275515`) and the adjective **deaf** (H2795, `Psa 38:13 · span 277903`). Types spread as:
- **action** (11): the plain hearing/attending — e.g. `Psa 85:8 · span 284224 · D102(type)`, `Psa 78:1 · span 283001 · D102`, `Psa 66:8 · span 281382 · D102`.
- **status** (2): `Psa 58:5 · span 280502 · D102(type)` and `Psa 59:7 · span 280640 · D102` — a settled deafness/presumption, not an act.
- **disposition** (3): the *listen/heed* spans — `Psa 81:8 · span 283873 · D102`, `Psa 81:11 · span 283796 · D102`, `Psa 81:13 · span 306919 · D102`.
- **volition** (2): `Psa 21:4 · span 275515 · D102(type)` (ask) and `Psa 38:13 · span 277903 · D102` (chosen deafness).

The type layer already separates *hearing as event* (action) from *hearing as settled stance* (status/disposition) from *willed act* (volition) — the family's real internal structure.

### 2.2 seat (D104)
**Unstated in every instance** (all "none"; §0.3). No heart/soul/spirit/ear seat is recorded even where the verse names the ear or heart. The interior *locus of hearing* is therefore not derivable from this source.

### 2.3 bearer (D105) — whose IB
Human throughout (IB screen passes); **`inferred` on all 20**, `item_type:flag`, never stated on the span. Bearers are largely corporate:
- Corporate Israel/people: "my people" (`Psa 81:8 · span 283868`, `Psa 81:11 · span 283796`, `Psa 81:13 · span 306919`, `Psa 78:1 · span 283001`), "Israel" (`Psa 81:8 · span 283873`), "the people" (`Psa 95:7 · span 285506`), "the peoples" (`Psa 66:8 · span 281382`), "we" (`Psa 78:3 · span 306759`, `Psa 132:6 · span 272972`), "Zion" (`Psa 97:8 · span 285696`), "all who fear God" (`Psa 66:16 · span 281284`).
- Individual: "the psalmist" (`Psa 85:8 · span 284224`, `Psa 62:11 · span 280933`, `Psa 92:11 · span 285174`, `Psa 38:13 · span 277903`), "the penitent" (`Psa 51:8 · span 279771`), "the king" (`Psa 21:4 · span 275515`).
- Adversarial: "the wicked (like the deaf adder)" (`Psa 58:5 · span 280502`), "the enemies (presuming)" (`Psa 59:7 · span 280640`).

So the "inner being" here is frequently the *community's* hearing, not only the individual's — a corporate IB.

### 2.4 source (D103) / operation (D106) / target (D107) / manner (D108)
- **source (D103): absent everywhere** — what moves the hearing cannot be derived.
- **operation (D106):** the motion is well filled (19 spans have D106). Ranges: *long to hear* (`Psa 51:8 · span 279771 · D106`), *refuse to hear/heed* (`Psa 58:5 · span 280502 · D106`, inferred), *presume none hears* (`Psa 59:7 · span 280640 · D106`, inferred), *come and hear* (`Psa 66:16 · span 281284 · D106`), *hear/receive* (`Psa 81:5 · span 283847 · D106`), *fail to listen* (`Psa 81:11 · span 283796 · D106`), *make heard / cause to resound* (`Psa 66:8 · span 281382 · D106`), and the two outliers: *ask life, answered beyond measure* (`Psa 21:4 · span 275515 · D106`) and *become like a deaf/mute man, deliberate silence* (`Psa 38:13 · span 277903 · D106`).
- **target (D107):** what is heard — God's speech/voice (`Psa 85:8 · span 284224 · D107` to what God will speak; `Psa 95:7 · span 285506 · D107` God's voice today; `Psa 81:8 · span 283868 · D107` God's admonition), tradition (`Psa 78:3 · span 306759 · D107`; `Psa 78:1 · span 283001 · D107`), judgment/vindication news (`Psa 92:11 · span 285174 · D107` the doom of assailants; `Psa 97:8 · span 285696 · D107` God's judgments), or "none" where the verse gives no object (`Psa 59:7 · span 280640 · D107` = none). Two targets are genuine pairs (§0.2): span 279771→279772, span 280933→280935, span 281382→281381.
- **manner (D108):** filled only twice (§0.3) — willful self-deafness (`Psa 58:5 · span 280502 · D108`) and the "once spoken, twice heard" cadence (`Psa 62:11 · span 280933 · D108`).

### 2.5 coupling (D112) / locus (D116) — corrected for swaps
- **locus (D116), corrected:** `external:god` on the God-directed hearings (e.g. `Psa 66:16 · span 281284`, `Psa 81:5 · span 283847`, `Psa 85:8 · span 284224`, `Psa 95:7 · span 285506` [corrected], `Psa 132:6 · span 272972` [corrected]); `external:person` on `Psa 78:1 · span 283001 · D116(locus)` (give ear to the human teacher); `internal:ib-state` on the interior-state reads (`Psa 51:8 · span 279771`, `Psa 58:5 · span 280502`, `Psa 59:7 · span 280640`, `Psa 78:3 · span 306759`, `Psa 21:4 · span 275515`, `Psa 38:13 · span 277903`, plus corrected `Psa 97:8 · span 285696` and `Psa 92:11 · span 285174`). So the hearing sits mostly toward God (external) but is registered as an internal state in the reflective/vindication verses.
- **coupling (D112):** what the hearing is bound to — the broken bones rejoicing (`Psa 51:8 · span 279771 · D112`, genuine pair), the venom's incorrigibility (`Psa 58:5 · span 280502 · D112`, pair), God's mocking laughter (`Psa 59:7 · span 280640 · D112`, pair), blessing God (`Psa 66:8 · span 281382 · D112`, pair), the refusal to submit (`Psa 81:11 · span 283796 · D112`, inferred), walking in his ways (`Psa 81:13 · span 306919 · D112`, inferred). Hearing is repeatedly coupled to a *consequent* — gladness, worship, obedience, or (refused) to incorrigibility.

### 2.6 role (D115)
**`characteristic` on all 20** — no qualifier or standalone in the family. Every span is read as a characteristic of the IB.

### 2.7 discovery notes (D114) — the reader's read (source)
D114 present on all 20 and carries the interpretive weight. Notable reads: `Psa 51:8 · span 279771 · D114` "the plea to be told the word of pardon that brings back joy — sorrow turning toward hope"; `Psa 58:5 · span 280502 · D114` "willful, self-stopped deafness of the wicked... deaf to all correction"; `Psa 59:7 · span 280640 · D114` "practical atheism... which God answers with derisive laughter"; `Psa 81:11 · span 283796 · D114` "the tragic refusal, the summons of v8 met with deafness"; `Psa 62:11 · span 280933 · D114` "the taking-in of the two great truths... power AND steadfast love"; `Psa 38:13 · span 277903 · D114` "a chosen refusal to answer... leaves its case to God".

---

## 3. The network

Nine genuine `pair` edges from 5 spans (§0.2). Every edge points to a **non-family** span; no family span links to another family span; all directions null. The relational picture is therefore **thin and outward**: the family's hearings are each locally coupled (to a joy, a bones-rejoicing, a blessing, a laughter, a twofold word) but those couplings resolve to spans held outside this file — not derivable here. The densest nodes are `span 279771` (Psa 51:8) and `span 281382` (Psa 66:8), each with 2 outward edges; `span 280933` (Psa 62:11) carries the only manner-pair. Fourteen of the twenty spans carry **no** genuine edge.

---

## 4. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings:
- **Seats: none named** (D104 all "none") — the anatomy of *where* the hearing sits is blank in this source, despite the verses supplying ear/heart.
- **Source: none** (D103 absent).
- **What is named** is the *motion* (D106 operation) and the *object* (D107 target: God's voice, tradition, vindication) and the *bond* (D112 coupling: to gladness, worship, obedience, laughter). The IB here is drawn as an organ-less *reception surface* turned toward God's speech — its structure given by what it hears and what that hearing then produces, not by any located seat.
- **Valence axis** the data does name: reception splits into *received/attended* (God's word, tradition), *refused* (the wicked's self-deafness, Israel's failure), and *longed-for* (let me hear; Oh that they would listen) — this three-way is the family's clearest internal anatomy.

---

## 5. What could not be derived
- **Seat (D104)** for any instance — 100% "none"; interior locus of hearing unknown even where the text names ears/heart.
- **Source (D103), intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — absent on all 20; not derivable for this family.
- **Manner (D108)** for 18 of 20.
- **The network's far ends** — all 9 genuine edges resolve to spans outside this file; what the hearings couple *to* is only labelled, not resolvable here. No intra-family and no directional links.
- **Outlier separation** — the M21(Prayer) petition span (275515) and the null-cluster chosen-silence span (277903) are fused into the family with `is_outlier:false`; the file does not itself flag them as distinct movements (§1 does, from the data).
- **The M41 "Remembrance" typing** of the shama/azan spans is asserted by the term-cluster but not explained; whether "hearing" belongs under Remembrance is not derivable from this source.

---

## 6. Summary
`being-heard-listening` is a mostly coherent **auditory-reception** family: 18 shama/azan spans (M41) reading as *hearing / heeding / listening / giving ear*, structured by a clear valence axis (attended vs refused vs longed-for) and typed action/status/disposition. Two intruders are fused in: a *petition-answered* movement (`Psa 21:4 · span 275515`, M21) and a *chosen-silence/self-deafness* movement (`Psa 38:13 · span 277903`, cluster null), both mis-marked `is_outlier:false`. The IB is drawn without a seat (D104 all "none") and without source/intensity/specifier/effect/prohibition — an organ-less reception surface turned toward God's voice, its meaning carried by operation, target, coupling and the reader's D114 notes. Network is thin (9 outward pair-edges from 5 spans, no intra-family links). Data-integrity flags: 4 D112/D116 swaps (spans 285506, 285696, 272972, 285174), pervasive self-loop non-edges, and one null-cluster term.
