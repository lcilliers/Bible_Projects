# Family analysis — `faith-faithfulness-truth` (Psalms), in isolation

> Source: `verse-analysis/psalms/_base-sources/psalms__faith-faithfulness-truth.json` only. 10 meanings · 25 instances · 24 passages. Every claim cited `reference · span · Dnnn(label)`. British spelling. Nothing imported from outside this file.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling)/D116(locus) field-swap
Correct order = **D116 a code** (`internal:`/`external:`), **D112 a phrase**. The following **8 instances are transposed** (D112 holds the code, D116 holds a prose phrase) and are read corrected below:

| Instance | Raw D112 | Raw D116 | Corrected D116 locus | Corrected D112 coupling |
|---|---|---|---|---|
| Psa 106:12 · span 269595 | `external:god` | "paired with singing his praise" | external:god | paired with singing his praise |
| Psa 116:10 · span 270927 | `external:god` | "paired with being greatly afflicted" | external:god | paired with being greatly afflicted |
| Psa 116:15 · span 270948 | `internal:ib-state` | "paired with the preciousness of their death" | internal:ib-state | paired with the preciousness of their death |
| Psa 132:16 · span 272943 | `internal:ib-state` | "paired with the shout of joy" | internal:ib-state | paired with the shout of joy |
| Psa 132:9 · span 272990 | `internal:ib-state` | "paired with the shout of joy" | internal:ib-state | paired with the shout of joy |
| Psa 97:10 · span 285635 | `internal:ib-state` | "paired with being delivered from the wicked" | internal:ib-state | paired with being delivered from the wicked |
| Psa 101:6 · span 268855 | `internal:ib-state` | "paired with the blameless who minister" | internal:ib-state | paired with the blameless who minister |
| Psa 106:24 · span 269670 | `external:god` | "paired with despising the land" | external:god | paired with despising the land |

The remaining 17 instances are in **correct order** (D116 a code, D112 a phrase or a genuine pair). All corrected loci and couplings below use these corrections.

### 0.2 Self-loop "edges" are not links
Almost every instance carries edges on `D105 bearer`, `D107 target`, `D112 coupling` with `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's **own id**. These are **self-loops, not network edges** and are excluded from the network (§ Network). Only `pair`/`span` edges to a **different** span count.

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in 24 of 25 instances.** The **only** filled seat in the whole family is Psa 51:6 · span 279758 · D104 seat = "in the inward being".
- **D108 manner = "none" in 25 of 25 instances** — manner is never filled anywhere.

### 0.4 Absent dimensions (across all 25)
- **D109 intensity — absent everywhere.**
- **D110 specifier — absent everywhere.**
- **D111 effect — absent everywhere.**
- **D113 prohibition — absent everywhere.**
- **D103 source — present in only 2 of 25:** Psa 51:6 · span 279758 (source = "what God delights in / desires (v6)") and Psa 50:5 · span 279604 (source = "summoned by God who comes to judge (v1,3-4)"). Absent in the other 23.
- **D106 operation = "none" and D107 target = "none"** in 4 instances: Psa 52:9 · span 279875; Psa 45:4 · span 278961; Psa 51:6 · span 279758; Psa 50:5 · span 279604.

### 0.5 Cluster NULL / T2
- **Psa 149:9 · span 274496** and **Psa 149:7 · span 308216** (H6213 `execute`) both have `cluster.code = null`, `all_candidates = T2(Supplementary)` — the term-cluster cannot type them.

### 0.6 Declared outlier
- **Psa 119:158 · span 271569** (H0898 `faithless`) is flagged `is_outlier:true`: family expects M13(Truth) but the term-cluster is **M10(Sin)**.

### 0.7 Bearer integrity (human-IB screen)
Every `D105 bearer` is an **inferred self-loop flag** (§0.2) — the "whose inner being" is always an inference, never span-anchored. All bearers are human (fathers, psalmist, "they", the godly/saints, the penitent, the king). **Borderline:** Psa 45:4 · span 278961 · D105 bearer = "the king (his cause)" — here `truth` is a **moral cause the king champions**, an abstract virtue rather than an interior movement; retained but flagged.

---

## 1. Coherence — does the label fit its data?

**No — the label fuses at least three distinct movements plus two intruders.** The English keyword net "faith / faithful / truth" has gathered five different Hebrew lemmas that do not form one inner-being movement:

1. **H0539 `aman` — believing / trusting (or its collapse).** 10 instances (`believe` ×6, `faithful` ×3, `faith` ×1), cluster **M13(Truth)**. A genuine interior **disposition/affect of trust in God**, present *and* negated. E.g. Psa 27:13 · span 276222 · D102 type = affect ("a faith that steadies against despair", D114); Psa 78:22 · span 283094 · D106 operation = "fail to believe". This is the only cluster that is faith *proper*.
2. **H2623 `chasid` — the godly / covenant-loyal (a status).** 10 instances (`saints` ×5, `godly` ×3, `faithful` ×1, `faithful ones` ×1), cluster **M05(Love)**. Overwhelmingly **D102 type = status** — a class-identity of persons (e.g. Psa 116:15 · span 270948; Psa 50:5 · span 279604), not an interior act. The interior content is thin; operations are outward (Psa 132:9 · span 272990 · D106 = "shout for joy"; Psa 97:10 · span 285635 · D106 = "be godly"/preserved).
3. **H0571 `emeth` — truth / inner integrity.** 2 instances, M13(Truth): Psa 51:6 · span 279758 (inner truthfulness "in the inward being") and Psa 45:4 · span 278961 (truth as the king's public cause). Distinct from both trust and piety.
4. **Intruder — H6213 `asah` "execute".** 2 instances (Psa 149:7 · span 308216; Psa 149:9 · span 274496), **cluster null/T2**. This is **judgment-agency / dignified obedience** (D114: "obedience felt as honour"), *not* a faith term; grouped only by the "godly ones" context of Ps 149.
5. **Intruder — H0898 `bagad` "faithless".** 1 instance (Psa 119:158 · span 271569), **M10(Sin)** — treachery, the declared outlier.

So the family conflates **trust (aman)**, **piety-as-status (chasid)**, and **integrity (emeth)**, and then admits **judgment-agency (asah)** and **treachery (bagad)**. Only aman and emeth (both M13) belong together; chasid is a persons-category (M05); asah and bagad do not belong.

**Polarity finding (real):** the `aman` strand carries its own presence-and-collapse arc — faith held under affliction (Psa 116:10 · span 270927 · D114 "belief speaking through pain") against root unbelief that even miracles could not cure (Psa 78:32 · span 283150 · D114; Psa 106:24 · span 269670 · D106 "have no faith"). The same interior capacity is shown both alive and failed.

---

## 2. The movements evidenced (cited)

### 2.1 `aman` — the interior of trust
- **Type:** mostly **disposition** (Psa 106:12 · span 269595 · D102; Psa 119:66 · span 271995 · D102; Psa 78:22 · span 283094 · D102), once **affect** (Psa 27:13 · span 276222 · D102 = affect).
- **Operation:** `believe` (Psa 106:12 · span 269595 · D106) vs `fail to believe` / `have no faith` (Psa 78:22 · span 283094 · D106; Psa 78:32 · span 283150 · D106; Psa 106:24 · span 269670 · D106).
- **Target / locus:** bound to God and his word — corrected locus **external:god** at Psa 106:12 · span 269595 · D116, Psa 116:10 · span 270927 · D116, Psa 78:22 · span 283094 · D116, Psa 106:24 · span 269670 · D116; target "God's words/word/promise/saving power" (Psa 106:12 · span 269595 · D107; Psa 119:66 · span 271995 · D107).
- **Interior-preserving function:** Psa 27:13 · span 276222 · D106 operation = "a faith that keeps the interior from collapse" (locus **internal:ib-state**, D116) — trust turned inward as what holds the self against despair. This is the deepest interior reading in the strand.

### 2.2 `chasid` — being one of the godly (status, thin interior)
- Uniformly **D102 type = status** (Psa 116:15 · span 270948; Psa 132:16 · span 272943; Psa 85:8 · span 284235; Psa 97:10 · span 285635; Psa 52:9 · span 279875; Psa 86:2 · span 284329; Psa 79:2 · span 283508; Psa 50:5 · span 279604) — except **Psa 12:1 · span 272740 · D102 = affect** (the psalmist's *grief* that the godly have vanished — the one genuine interior movement in this strand: D114 "the interior grieves a social collapse").
- **Devotion-not-merit** self-claim: Psa 86:2 · span 284329 · D114 "the covenant-devotion David claims, not merit but belonging to God" (locus internal:ib-state, D116).
- Otherwise the operations are corporate/outward (shout for joy, be preserved) — interior anatomy largely unstated (seat = none throughout).

### 2.3 `emeth` — truth as inner integrity
- **Psa 51:6 · span 279758** is the family's richest interior record: **D104 seat = "in the inward being"** (the only filled seat), **D116 locus = internal:heart**, **D103 source = "what God delights in / desires"**, coupled to "wisdom taught in the secret heart" (D112, pair→279762). D114: "the honesty of the hidden self … not outward conformity."
- **Psa 45:4 · span 278961**: `emeth` as the **king's public cause** (locus internal:ib-state, D116), coupled with meekness and righteousness (D112 pair→278962) — a virtue-triad, borderline as human interior (§0.7).

### 2.4 `asah` "execute" (T2/null — not faith)
- Psa 149:9 · span 274496 · D102 = affect ("dignity in obedience", D114); Psa 149:7 · span 308216 · D102 = volition ("interior resolve turns outward as commissioned action", D114). Interior of **honour/resolve in carrying out decreed judgment** — a real inner state, but not of this family (cluster null/T2, §0.5).

### 2.5 `bagad` "faithless" (M10 Sin — declared outlier)
- Psa 119:158 · span 271569 · D106 = "deal faithlessly", D102 = status, target = the psalmist (D107), locus external:person (D116). Treachery viewed with disgust; the negative pole named as a *persons*-category, not the psalmist's own movement.

---

## The network (genuine `pair`/`span` edges only)
Self-loops excluded (§0.2). Only **6 genuine edges, from 4 spans**, and **every one points outward to a span not in this family** (no family-internal links, `direction:null` throughout):

| From | On dimension | To span | Meaning of the link |
|---|---|---|---|
| Psa 52:9 · span 279875 | D112 coupling | 279870 | the godly community in whose presence he waits and gives thanks |
| Psa 45:4 · span 278961 | D112 coupling | 278962 | truth paired with meekness/righteousness (virtue-triad) |
| Psa 51:6 · span 279758 | D103 source | 279757 | what God delights in / desires |
| Psa 51:6 · span 279758 | D104 seat | 279759 | "in the inward being" |
| Psa 51:6 · span 279758 | D112 coupling | 279762 | wisdom taught in the secret heart |
| Psa 50:5 · span 279604 | D103 source | 279485 | summoned by God who comes to judge |

**Network is sparse and one-directional.** Half the edges belong to a single span (Psa 51:6 · span 279758). No two family instances link to each other; the interior web the file names reaches *out* of the family, never within it.

## The interior anatomy the data actually names
Assembling only filled fields:
- **Seat:** one only — "the inward being" / secret heart (Psa 51:6 · span 279758 · D104; locus internal:heart, D116).
- **Sources:** God's delight/desire (Psa 51:6 · span 279758 · D103); God's summons to judgement (Psa 50:5 · span 279604 · D103). Both external-divine.
- **Couplings (genuine):** trust/piety knit to praise, integrity, and the godly community — but only as pair-edges out to non-family spans (see Network).
- **Loci (corrected):** `external:god` (the aman-trust strand), `internal:ib-state` (chasid self-claims + the interior-holding faith of Psa 27:13), `internal:heart` (Psa 51:6), `external:person` (the faithless, Psa 119:158).
- **The functional heart of the family:** trust that *holds the interior against collapse* (Psa 27:13 · span 276222 · D106) and *speaks through pain* (Psa 116:10 · span 270927 · D114) — versus root unbelief immune to evidence (Psa 78:32 · span 283150; Psa 106:24 · span 269670).

## What could not be derived
- **Seat:** unstated in 24/25 (§0.3) — the interior *location* of belief/piety is almost never given.
- **Manner:** unstated in 25/25 (§0.3) — *how* the movement happens is never derivable.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113):** absent entirely (§0.4) — no strength, qualification, downstream effect, or interdiction anywhere.
- **Source (D103):** only 2/25 (§0.4).
- **Operation/target:** "none" in 4 status-instances (§0.4) — pure labels with no motion.
- **Cluster:** null/T2 for the two `execute` spans (§0.5) — cannot be typed to the family.
- **Bearer:** every bearer is an inferred self-loop, never span-anchored (§0.2, §0.7); "whose IB" is inference throughout.
- **Chasid interior:** the `chasid` strand (10 instances) is largely status/persons-category; its interior movement is derivable in only two places (grief, Psa 12:1 · span 272740; devotion-claim, Psa 86:2 · span 284329).

## Summary
The `faith-faithfulness-truth` family is a **keyword fusion, not one movement**: `aman` (trust/unbelief, M13), `chasid` (the godly-as-status, M05), and `emeth` (inner integrity, M13), plus two intruders — `asah` "execute" (judgment-agency, T2/null) and `bagad` "faithless" (M10 Sin, declared outlier). Its genuine inner-being core is the **`aman` disposition of trust that holds the interior against collapse and persists through affliction, set against a root unbelief impervious to evidence**, with a single deep seat-record of `emeth` "in the inward being" (Psa 51:6). Data is thin on anatomy: seat filled once, manner never; intensity/specifier/effect/prohibition wholly absent; the network is 6 outward, one-directional pair-edges with no family-internal links. Integrity caveats: 8 D112/D116 swaps corrected, all bearers inferred self-loops, 2 null/T2 clusters, 1 declared outlier.
