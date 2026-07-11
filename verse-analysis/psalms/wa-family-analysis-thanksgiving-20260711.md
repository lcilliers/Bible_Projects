# Family analysis — Psalms `thanksgiving` (in isolation)

> Source: `outputs/data/psalms-family-base-sources/psalms__thanksgiving.json` only. Scope `meta.scope.family = "thanksgiving"`; counts `meanings: 6 · instances: 49 · passages: 38`. Every claim cites `reference · span_id · Dnnn(label)` into that file. Nothing imported from outside it.

## Family shape (6 meanings, all cluster M22 Praise, `is_outlier:false`)

| # | char_key | meaning | lemma | n | word |
|---|---|---|---|---|---|
| 1 | H3034:givethank | give thanks | H3034 | 29 | yādāh (verb, Hiphil) |
| 2 | H3034:thank | thank | H3034 | 9 | yādāh (verb, Hiphil) |
| 3 | H8426:thanksgiv | thanksgiving | H8426 | 7 | tôdāh (noun) |
| 4 | H3034:giveyouthank | give you thanks | H3034 | 2 | yādāh (verb) |
| 5 | H3034:givethanksto | give thanks to | H3034 | 1 | yādāh (verb) — Psa 142:7 |
| 6 | H8426:thankoffer | thank offerings | H8426 | 1 | tôdāh (noun) — Psa 56:12 |

29+9+7+2+1+1 = 49 ✓. Two lemmas only: yādāh (H3034, 41 instances) and tôdāh (H8426, 8 instances). Every meaning is clustered **M22 (Praise)**.

---

## 0. Data-integrity screen (done first)

### 0.1 D112 (coupling) / D116 (locus) field-swap — SYSTEMIC (32 of 49)
Per method, correct order = **D116 a code, D112 a phrase**. In 32 instances the file has it reversed: **D112 coupling holds the bare code `external:god`** and **D116 locus holds a prose phrase** (`paired with …`). These are transposed; read corrected as *locus = external:god, coupling = the "paired with …" phrase*.

Swapped instances (D112=`external:god`, D116=phrase):
- **Meaning 1 (20):** Psa 100:4·268794 · Psa 105:1·269364 · Psa 106:1·269574 · Psa 106:47·269801 · Psa 107:1·269860 · Psa 108:3·270112 · Psa 111:1·270564 · Psa 118:1·271039 · Psa 118:19·271090 · Psa 118:28·271137 · Psa 118:29·271141 · Psa 122:4·272408 · Psa 136:1·273151 · Psa 136:2·273176 · Psa 136:26·273218 · Psa 136:3·273225 · Psa 138:2·273319 · Psa 86:12·284263 · Psa 92:1·285157 · Psa 97:12·285650.
- **Meaning 2 (6):** Psa 107:15·269890 · Psa 107:21·269926 · Psa 107:31·269975 · Psa 107:8·270060 · Psa 109:30·270302 · Psa 118:21·271104.
- **Meaning 3 (4):** Psa 100:4·268791 · Psa 107:22·269934 · Psa 116:17·270951 · Psa 95:2·285471.
- **Meaning 4 (2):** Psa 138:1·273310 · Psa 138:4·308052.

All cite `D112 coupling` + `D116 locus`. The swap is not random: it coincides exactly with the "template" instances (bare inferred `external:god` coupling). The remaining 17 instances are in **correct order** — D112 carries a real coupling phrase (or `none`) and D116 carries a code (`external:god` or `internal:ib-state`), e.g. Psa 44:8·278852 (`D112 paired with boasting` / `D116 external:god`), Psa 9:1·285865 (`D112 thank-whole-heart` / `D116 internal:ib-state`). One of these 17, Psa 50:14·279514, has `D112 coupling = none`.

**Net effect once corrected:** locus is a code in all 49 — `external:god` for ~43, `internal:ib-state` for 6 (Psa 9:1·285865, Psa 140:13·273601, Psa 145:10·274041, Psa 7:17·283622, Psa 35:18·277364, Psa 142:7·273835). Coupling is a phrase or `none`.

### 0.2 Self-loop "edges" are not network links
Almost every `edges` entry is a self-loop: `item_type:flag`, `resolution:inferred`, `from_span:null`, `to_span` = the span's own id (bearer D105, target D107, and the swapped coupling D112). These carry no network information and are excluded from §"The network". Example: Psa 100:4·268794 has three self-loop flags (D105, D107, D112) to `268794`.

Genuine `pair` edges (`resolution:span`, to a **different** span) exist on only ~10 instances:
- Psa 44:8·278852 — D112 coupling → 278850 (boasting).
- Psa 54:6·280009 — D103 source→280015, D107 target→280010, D108 manner→280007, D112 coupling→280007.
- Psa 57:9·280439 — D103 source→280356, D112 coupling→280442.
- Psa 75:1·282696 — D103 source→282699, D107 target→282699, D108 manner→282698, D112 coupling→282698.
- Psa 75:1·282698 — D112 coupling→282696 (reciprocal to 282696).
- Psa 50:14·279514 — D103 source→279499.
- Psa 50:23·279576 — D112 coupling→279578.
- Psa 69:30·281831 — D112 coupling→281830.
- Psa 52:9·279866 — D108 manner→279867, D112 coupling→279870.
- Psa 56:12·280247 — D112 coupling→280246.

Only **one** genuine link is intra-family: Psa 75:1 · 282696 ⇄ 282698 (`D112 coupling`) — the emphatic doubled "we give thanks". All other pair edges reach spans **outside** the 49 family masters.

### 0.3 seat (D104) / manner (D108) = "none"
- **D104 seat = `none` in all 49/49.** The interior organ is never recorded in the seat dimension (e.g. Psa 100:4·268794 · D104(seat)=`none`).
- **D108 manner = `none` in 43/49.** Filled only on: Psa 44:8·278852 (`forever`), Psa 54:6·280009 (`with a freewill offering`), Psa 57:9·280439 (`among the peoples/nations`), Psa 75:1·282696 (`doubled, emphatic`), Psa 75:1·282698 (`emphatic repetition`), Psa 52:9·279866 (`forever (for what God has done)`).

### 0.4 Absent dimensions (across all 49)
- **D109 intensity — absent everywhere.**
- **D110 specifier — absent everywhere.**
- **D111 effect — absent everywhere.**
- **D113 prohibition — absent everywhere.**
- **D103 source — present on only 4/49** (Psa 54:6·280009, Psa 57:9·280439, Psa 75:1·282696, Psa 50:14·279514); absent on the other 45.

### 0.5 Cluster NULL / T2
None. All 49 instances are `cluster.code = M22 (Praise)`; no NULL, no T2. Term-cluster typing succeeds on every instance.

### 0.6 Minor
- Psa 75:1·282698 has `esv_word: null` (the un-glossed second half of the doubled "we give thanks").
- `passage_ref` vs `verse_refs` mismatches (non-blocking): passage 1692 labelled "Psa 69:26-32" lists 69:26–36; 1725 "Psa 79:11-13" lists 79:10–13; 1791 "Psa 106:38-48" lists from 106:36. Text integrity unaffected.

---

## 1. Coherence — does the label fit the data?

**Yes — the family is coherent, not fused.** All 6 meanings are the same two-word lexical field (yādāh / tôdāh) for grateful acknowledgement directed to God, uniformly clustered M22 (Praise), all `is_outlier:false`. Operation (D106) is `give thanks` / `thank` / `offer` throughout; target (D107, corrected of self-loops) is always God / God's name; role (D115) = `characteristic` on all 49. There is no second, unrelated movement smuggled in by the keyword.

One real internal distinction the data does draw (a sub-structure, not a fracture):
- **yādāh verb (meanings 1,2,4,5)** = the **act** of thanking — `D102 type = action` on the great majority.
- **tôdāh noun (meanings 3,6)** = the **offering/state** — `D102 type = status` on the sacrifice reads (Psa 50:14·279514, Psa 50:23·279576, Psa 69:30·281831, Psa 56:12·280247) and `action` on the "come/enter with thanksgiving" reads (Psa 100:4·268791, Psa 95:2·285471, Psa 107:22·269934, Psa 116:17·270951).

Type distribution (D102): action 39 · affect 5 · status 4 · volition 1.

---

## 2. The movement evidenced — thanksgiving as outward-directed act, thinly interior

The dominant reading is **thanksgiving as directed behaviour, not an interior process**. Across the family: seat is never filled (0.3), locus corrects to `external:god` for ~43/49, target is God/God's name, and operation is the outward act "give thanks / offer". The IB "inner workings" are represented only obliquely — the verse text repeatedly says "with my **whole heart**" (Psa 9:1·285865, Psa 86:12·284263, Psa 111:1·270564, Psa 138:1·273310) but this lands in the coupling/locus phrase, never in `D104 seat`. So the organ of gratitude is *attested in text but unrecorded in the anatomy dimension*.

### 2a. The interior sub-set (6 instances, `internal:ib-state`)
The only instances the data locates **inside** the IB — typed `affect` or `volition`, locus (corrected) `internal:ib-state`:
- Psa 9:1·285865 · D102(type)=`affect`, D106(operation)="the self resolves to thank the LORD with its whole heart… undivided gratitude", D116(locus)=`internal:ib-state`. D114: "the interior gives itself entire to gratitude, nothing held back."
- Psa 140:13·273601 · D102=`affect`, D114: "the interior moves from threat through assurance to thanks."
- Psa 145:10·274041 · D102=`affect`, bearer `the saints`, D114: "the interior of the whole godly community turns grateful."
- Psa 7:17·283622 · D102=`affect`, D114: "the interior lands in gratitude; the righteous judge trusted, the self already praises."
- Psa 35:18·277364 · D102=`volition`, D106="the self vows to thank God in the great congregation… gratitude discharged publicly."
- Psa 142:7·273835 · D102=`affect`, sense=`anticipated thanksgiving`, D106="the self already reaches past rescue to thanks — gratitude anticipated", D114: "the interior leans forward into future praise, gratitude pre-formed in hope."

These six are the family's actual "inner-being" evidence: thanksgiving as an interior state/resolve that **precedes or outruns** the deliverance (Psa 142:7·273835 anticipatory; Psa 35:18·277364 vowed; Psa 140:13·273601 an arc from threat to thanks).

### 2b. The outward act / offering (the other 43)
Thanksgiving as summons, approach, and sacrifice, directed to God:
- **Summons / call to thank** (imperatives): Psa 100:4·268794, Psa 105:1·269364, Psa 106:1·269574, Psa 107:1·269860, Psa 118:1·271039, Psa 136:1·273151 (+136:2·273176, 136:3·273225, 136:26·273218), Psa 97:12·285650 — all D106(operation)=`give thanks`, D107 target God.
- **The refrain "Let them thank the LORD for his steadfast love"** — Psa 107:8·270060, 107:15·269890, 107:21·269926, 107:31·269975 (meaning 2), each D116(locus corrected)/D114 tying thanks to "his wondrous works (refrain)".
- **Thank-offering (tôdāh as status/sacrifice)**: Psa 50:14·279514 (D114: "the worship God actually desires, not slaughtered bulls"), Psa 50:23·279576 ("gratitude is the true sacrifice… glorifies me"), Psa 69:30·281831 ("more pleasing… than ox or bull"), Psa 56:12·280247 ("gratitude become worship, the fruit of trust vindicated"), Psa 116:17·270951, Psa 107:22·269934. All D102(type)=`status`/`action`, D106(operation)=`offer`.
- **Vow of perpetual/public thanks**: Psa 44:8·278852 (`D108 manner = forever`), Psa 79:13·283493 ("across generations even out of desolation"), Psa 52:9·279866 ("I will thank you forever"), Psa 57:9·280439 / Psa 108:3·270112 ("among the peoples/nations").

### 2c. Motivating ground (D103 source, the 4 filled)
Where recorded, thanks is grounded in something God is/does:
- Psa 54:6·280009 · D103(source)="because God has delivered him from every trouble (v7) in his faithfulness (v5)".
- Psa 57:9·280439 · D103(source)="because God's steadfast love is great to the heavens (v10)".
- Psa 75:1·282696 · D103(source)="because God's name is near (v1)".
- Psa 50:14·279514 · D103(source)="the God who owns all and needs nothing (v10-12)".

On the other 45 the ground is unrecorded in D103 (though D114 notes often gesture at "for his steadfast love").

### 2d. Bearer (D105) — all human IB, all inferred
Bearers span individual and corporate: the psalmist, the worshippers, the redeemed (Psa 106:47·269801, Psa 107:1·269860), the tribes (Psa 122:4·272408), the nation (Psa 44:8·278852), "we your people" (Psa 79:13·283493), the righteous (Psa 97:12·285650), the upright (Psa 140:13·273601), the saints (Psa 145:10·274041), the prisoners/healed/sailors/wanderers (Psa 107 refrains), the kings of the earth (Psa 138:4·308052). All pass the human-IB screen; none is God-as-bearer. Every D105 is `resolution:inferred` (a self-loop flag, §0.2).

---

## 3. The network (genuine pair edges only)

Sparse and almost entirely **outward** (§0.2). Corrected couplings bind thanksgiving to adjacent worship acts and to its grounds — not to other thanksgiving instances:
- → **boasting**: Psa 44:8·278852 · D112(coupling)→278850.
- → **freewill offering**: Psa 54:6·280009 · D112→280007 (and D108 manner→280007, D103 source→280015, D107 target→280010).
- → **singing praises among the nations**: Psa 57:9·280439 · D112→280442 (D103 source→280356).
- → **the doubled thanks + recounting**: Psa 75:1·282696 · D112→282698 (D103→282699, D107→282699, D108→282698).
- → **waiting for God's name**: Psa 52:9·279866 · D112→279870 (D108 manner→279867).
- → **glorifying God**: Psa 50:23·279576 · D112→279578.
- → **the magnifying**: Psa 69:30·281831 · D112→281830.
- → **what he renders**: Psa 56:12·280247 · D112→280246.
- → **God who owns all**: Psa 50:14·279514 · D103(source)→279499.

**The single intra-family link:** Psa 75:1 · 282696 ⇄ 282698 (`D112 coupling`, both family masters) — the emphatic doubling "We give thanks… we give thanks". Directionality is unusable (`direction:null` on every edge). Otherwise there is **no** thanksgiving-to-thanksgiving web; the movement is evidenced as bound *outward* to accompanying acts and grounds.

---

## 4. The interior anatomy the data actually names

Assembling only filled dimensions:
- **Seats (D104):** none — 0/49. The anatomy has no organ recorded, despite "whole heart" in the text of Psa 9:1·285865, Psa 86:12·284263, Psa 111:1·270564, Psa 138:1·273310.
- **Interior locus (D116 corrected = internal:ib-state):** 6 instances only (§2a) — the sole "inside the IB" placements.
- **Sources (D103):** 4 — God's deliverance/faithfulness, steadfast love, nearness, self-sufficiency (§2c).
- **Operation (D106):** uniformly `give thanks` / `thank` / `offer`.
- **Target (D107 corrected):** God / God's name — always upward/external.
- **Couplings (D112 corrected, genuine):** boasting, freewill/thank offering, singing, recounting, waiting, glorifying, magnifying (§3).

The named anatomy is therefore **outward-facing**: a movement from the human self (seat unspecified) toward God, occasionally recorded as an interior affect/resolve (6×), grounded (4×) in what God has done.

---

## 5. What could not be derived (flagged)

1. **No interior seat anywhere** (D104=`none`, 49/49) — the organ of gratitude is unrecorded even where the text says "whole heart".
2. **D109 intensity, D110 specifier, D111 effect, D113 prohibition — wholly absent** across all 49. No reading of degree, kind, consequence, or any prohibition of thanksgiving.
3. **D103 source present on only 4/49** — the motivating ground of thanks is mostly not captured in-dimension.
4. **D108 manner `none` on 43/49.**
5. **D112/D116 swap on 32/49** (§0.1) — the recorded locus/coupling is unreliable until corrected; findings above use the corrected reading.
6. **Network is effectively empty of intra-family structure** — 1 reciprocal pair only (Psa 75:1); no directional information (`direction:null` throughout); self-loops dominate the edges arrays and were discarded.
7. **The "inner workings" of the IB are thinly evidenced** — the family overwhelmingly reads thanksgiving as directed outward behaviour/offering; interior process appears in just 6 affect/volition instances (§2a).

---

## Summary

`thanksgiving` is a **coherent, single-cluster (M22 Praise) family** of two lemmas — yādāh (41) and tôdāh (8), 49 instances — reading the human IB's **grateful acknowledgement of God**. The data present it mainly as an **outward-directed act/offering** (seat never filled, locus corrects to `external:god`, target always God), with only 6 instances placing it **inside** the IB as an affect/resolve (`internal:ib-state`), notably the *anticipatory* thanks of Psa 142:7·273835 and the *vowed* thanks of Psa 35:18·277364. Major integrity load: a **systemic D112/D116 swap on 32/49** and self-loop pseudo-edges; the genuine network is near-empty (one intra-family reciprocal at Psa 75:1). Intensity/specifier/effect/prohibition and seat are **entirely underived**; source recorded only 4×.
