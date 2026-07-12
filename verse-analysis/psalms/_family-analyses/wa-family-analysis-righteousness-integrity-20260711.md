# Family analysis — Psalms `righteousness-integrity` (in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__righteousness-integrity.json` (only). Scope: this one file. Counts (meta): **25 meanings · 69 instances · 42 passages**. All findings cited `reference · span_id · Dnnn(label)`. Discovery notes cited as D114. No external data used.

---

## 0. Data-integrity screen (done first)

**Dimension coverage across all 69 instances.** Present on every instance: D101 sense, D102 type, D104 seat, D105 bearer, D106 operation, D107 target, D108 manner, D112 coupling, D114 discovery, D115 role, D116 locus (69/69 each). **D103 source is present on exactly ONE instance** — `Psa 73:1 · 282360 · D103(source)="to whom God is good (v1)"`. Everywhere else the mover is unstated.

**Absent dimensions (0/69) — a whole band of the model is unfilled:** **D109 intensity, D110 specifier, D111 effect, D113 prohibition are absent across all 69 instances.** No instance records how strong, further-specified, what-it-produces, or any prohibition. This family carries no measured intensity and no stated effect anywhere.

**D112(coupling)/D116(locus) field-swap.** The method's correct order is D116 = an `internal:`/`external:` code, D112 = a prose phrase. **27 of 69 instances are transposed** (D112 holds the code, D116 holds the phrase) and must be read corrected; **42 are already in correct order.** No instance has both-code or both-phrase — every instance carries exactly one code, so the swap is cleanly detectable and fully repairable.

Swapped instances (read D112↔D116 corrected) — all 27 carry the code `internal:ib-state`:
`Psa 112:4·270681`, `Psa 112:6·270690`, `Psa 118:15·271061`, `Psa 118:20·271101`, `Psa 125:3·272539`, `Psa 125:3·272541`, `Psa 92:12·285177`, `Psa 97:11·285643`, `Psa 97:12·285649`, `Psa 107:42·270031`, `Psa 111:1·270570`, `Psa 112:2·270666`, `Psa 112:4·270678`, `Psa 125:4·272549`, `Psa 97:11·285645`, `Psa 101:2·268816`, `Psa 101:6·268862`, `Psa 106:3·269702`, `Psa 106:31·269711`, `Psa 112:3·270671`, `Psa 112:9·270715`, `Psa 101:2·268820`, `Psa 132:9·272989`, `Psa 106:3·269700`, `Psa 112:5·270688`, `Psa 94:21·285394`, `Psa 94:15·285348` — all on D112(coupling)/D116(locus).

**Self-loop non-edges.** The `edges` arrays are dominated by self-references that are **not** network links: **177 `flag`+`inferred` edges whose `to_span` = the span's own id, plus 11 `event`+`inferred` self edges (188 total).** Under the method these are discarded. Genuine cross-span links: **28 `pair`+`resolution:span` edges to a *different* span** (the network proper), plus 5 `event`+`span` cross-span operation edges (noted separately; not `pair`, so outside the strict network).

**D104 seat = "none": 64 of 69** (only 5 seated — see §5). **D108 manner = "none": 59 of 69.** **D105 bearer: all 69 are `inferred`** (never stated outright).

**Cluster NULL / T2.** No `T2` instances. **5 instances have `cluster.code = null`** — the term-cluster cannot type them: `Psa 82:3·283900` + `Psa 82:4·283906` (weak/*dal*), `Psa 17:15·274821` (behold), `Psa 15:5·274652` (interest/usury), `Psa 15:5·274661` (moved). These are examined in §1.

**Role.** D115 role = `characteristic` on all 69 (no qualifier, no standalone). Every span is typed as a characteristic even where that is doubtful (see §1 on *the weak* and *wrong*).

---

## 1. Coherence — does the family label fit its data?

**Largely yes, with a describable leakage margin.** The bulk — **59/69 instances** in three adjacent clusters — forms one coherent moral-integrity constellation: **M26 Righteousness (31), M13 Truth/uprightness (15), M12 Purity/cleanness (13).** Their senses interlock: *tsaddiq/tsedeq/tsedaqah* (righteous/righteousness), *yashar/tom* (upright/integrity), *tahor/bar/zakah/naqi* (clean/pure/innocent), *tamim* (blameless), *mishpat* (justice). These are one movement — the settled moral rectitude of the inner being — read repeatedly across Pss 7, 15, 18, 24, 45, 51, 72, 73, 82, 94, 97, 101, 106, 111, 112, 118, 119, 125, 132.

**The keyword grouping has, however, fused in 10 instances that are not that movement:**

- **The negative pole (2) — M10 Sin, flagged outlier.** *evel* "wrong/injustice": `Psa 58:2·280478·D101(sense)="wrongs / injustice"` ("you devise wrongs"), `Psa 7:3·283641·D101="oath of innocence"` ("if there is wrong in my hands"). D114 at 280478 itself calls it "the opposite of the 'righteousness' they were meant to decree" — the antonym pulled in by shared oath/justice co-text.
- **Objects/recipients of righteous action, not IB-characteristics (2) — NULL cluster.** *dal* "the weak": `Psa 82:3·283900` ("give justice to the weak") and `Psa 82:4·283906` ("rescue the weak"). D106(operation) reads them as *"be denied justice"* / *"need rescue"* and D105(bearer)="the weak" — i.e. the party acted **upon**, yet D115 still types them `characteristic`. This is a role mis-fit: the weak is the recipient of justice, not an inner disposition of righteousness.
- **Stability/steadfastness co-located with righteousness (2) — NULL / M11 outlier.** `Psa 15:5·274661` moved ("never be moved", D102 state) and `Psa 20:8·275465` stand-upright ("we rise and stand upright", M11 Repentance outlier, D102 state). These read as the *result* of integrity (D114 274661: "character as bedrock") rather than righteousness itself.
- **A behaviour-refusal and a vision (2) — NULL cluster.** `Psa 15:5·274652` interest/usury ("does not put out money at interest", D102 volition) — a specific just act; and `Psa 17:15·274821` behold ("behold your face in righteousness", D102 affect) — a beatific vision co-located with the word "righteousness", not righteousness as a trait.
- **Cluster-typing outliers that remain semantically in-family (2).** `Psa 64:4·? tam` blameless (M34 Perseverance) and `Psa 73:13·282386` innocence/*niqqayon* (M07 Shame) — the single-term→cluster map lands them elsewhere, but their senses (blameless, innocent hands) belong to the purity/integrity movement.

**Finding:** the label fits the core; the fusion is (a) the antonym pole (*evel*), (b) recipients of justice (*dal*), (c) resultant stability (*moved*, *stand upright*), (d) a co-located vision (behold) — grouped by surface keyword proximity, not by shared inner movement. The 5 NULL-cluster and the M10/M11/M34/M07 outliers are exactly the seams.

---

## 2. What the family is (D101 sense / D102 type)

The family is read **predominantly as a STATUS — a standing/condition, not an active faculty-operation.** D102 distribution across 69: **status 38, disposition 16, volition 4, state 4, cognition 3, affect 3, action 1.** Over half (38) are a *standing* ("the righteous", "the upright", "blameless"); disposition (16) the settled bent; only **one** instance is an action — `Psa 73:13·282382·D102(type)=action` ("I have kept my heart clean"). Righteousness in this data is chiefly something the inner being **is**, seldom something it **does**.

Volition appears only in deliberate refusals — `Psa 15:5·274652·D102(volition)` (no usury/no bribe). Cognition/affect appear at the edges — `Psa 7:3·283641·D102(cognition)` (self-audit oath), `Psa 17:15·274821·D102(affect)` (behold-and-be-satisfied).

---

## 3. Whose inner being (D105 bearer)

**All 69 bearers are `inferred`** (never explicit). Named bearers cluster on the righteous person: "the righteous", "the man", "the psalmist", "the pure in heart", "the upright", "the people". Two bearers fall outside the righteous IB and mark the leakage: **"the unjust rulers"** (`Psa 58:2·280478·D105(bearer)` — bearer of *wrong*, the negative pole) and **"the weak"** (`Psa 82:3·283900` / `82:4·283906·D105(bearer)` — a recipient group, not an agent-IB). Every bearer is human; no bearer is God (God appears only as arena/addressee in the verse texts, never typed as the characteristic's bearer).

---

## 4. What moves it (D103 source / D106 operation / D107 target / D108 manner)

- **Source (D103): essentially unnamed.** Only `Psa 73:1·282360·D103(source)="to whom God is good (v1)"` records a mover — purity of heart sourced in the God who is good to Israel. The other 68 instances leave the source blank: the data does not say what produces the righteousness.
- **Operation (D106): present on all 69**, but read as the verse's action, e.g. `Psa 112:6·270690·D106(operation)="never be moved"`, `Psa 15:5·274661·D106="...shall never be moved — the settled, unshakeable stability that integrity produces"`, `Psa 7:3·283641·D106="the self submits itself to a conditional self-curse ... rigorous self-examination staked on integrity"`, `Psa 73:13·282382·D106="keep clean / purify"`. Many operations are stative ("be righteous", "never be moved") consistent with the status reading.
- **Target (D107): present on all 69 but overwhelmingly `inferred` abstractions** — "in dealings", "being steadfast", "financial-integrity", "steadfastness", "God-face-satisfaction", "unshakeableness". Two carry genuine cross-span targets (see network): `Psa 73:13·282382·D107(target)="his heart"` → span 282381.
- **Manner (D108): none on 59/69.** Where filled it is the crisis colour, not a method: `Psa 73:13·282382` / `282386·D108(manner)="in vain, so it seemed"` (Asaph's doubt).

---

## 5. The interior anatomy the data actually names (D104 seat, D116 locus corrected)

**Seat is named on only 5/69 instances, and only where the verse text itself says "heart" or "hands":**
- heart — `Psa 73:1·282360·D104(seat)="the heart"` (pure in heart), `Psa 51:10·279645·D104="the heart"` (clean heart), `Psa 73:13·282382·D104="the heart"` (kept my heart clean), `Psa 64:10·281103·D104="the heart"` (upright in heart);
- hands — `Psa 73:13·282386·D104(seat)="the hands"` (washed my hands in innocence, `inferred`).

Seating occurs **only in the purity/cleanness sub-movement (M12)** and follows the surface word — righteousness/uprightness *as such* is left **seatless** (64/69 "none"). The interior this file actually names is therefore narrow: **the heart** (as the locus of cleanness/uprightness) and **the hands** (as the locus of innocence/clean conduct). No soul, no spirit/*ruach*, no eye is named as a seat of this family.

**Locus (D116, corrected).** Corrected codes distribute: **`internal:ib-state` ~58, `internal:heart` 3** (`Psa 64:10·281103`, `Psa 51:10·279645`, `Psa 73:13·282382`), **`external:person` 7** (`Psa 52:6·279839`, `Psa 58:10·280455`, `Psa 64:10·281098`, `Psa 72:7·282331`, `Psa 75:10·282709`, `Psa 72:1·282234`, `Psa 72:1·282232`), **`external:god` 1** (`Psa 68:3·281583`). The family sits overwhelmingly *inside* as an inner-being state; the `external:person` loci are the cases where righteousness is read against another party (the wicked, the king, the upright company), and the single `external:god` locus binds gladness to God.

---

## 6. The network (genuine `pair` edges only)

**The network is sparse.** Of all edges, only **28 `pair`+`resolution:span` links reach a different span**; the remaining 188 are self-loops (§0). The genuine links concentrate in a handful of passages, mostly on **D112(coupling)** — binding a righteousness-span to a co-occurring characteristic in the same verse/passage:

- **Reciprocal (bidirectional) couplings** — the strongest nodes:
  - `Psa 72:1·282232 ⇄ 282234 · D112(coupling)` — righteousness ⇄ justice given to the royal son (the two royal virtues mutually bound).
  - `Psa 51:2·279725 ⇄ Psa 51:7·279767 · D112(coupling)` — the purity longed for ⇄ the cleansing that answers it (a cross-verse arc within Ps 51).
  - `Psa 73:13·282382 ⇄ 282386 · D112(coupling)` — clean heart ⇄ innocent hands (the psalmist's twinned integrity).
  - `Psa 64:10·281098 ⇄ 281103 · D112(coupling)` — the righteous ⇄ the upright-in-heart rejoicing.
- **Directional couplings:** `Psa 52:6·279839→279841`, `Psa 55:22·280151→280143`, `Psa 58:10·280455→280456`, `Psa 75:10·282709→282720`, `Psa 45:4·278963→278961`, `Psa 45:7·278986→278985`, `Psa 58:2·280478→280481`, `Psa 73:1·282360→282382 · D112(coupling)`, `Psa 51:7·279767→279725`.
- **Non-coupling genuine links** (the only ones off D112): seat pairs `Psa 64:10·281103→281104 · D104(seat)`, `Psa 73:1·282360→282361 · D104(seat)`, `Psa 51:10·279645→279646 · D104(seat)`, `Psa 73:13·282382→282381 · D104(seat)`; a source pair `Psa 73:1·282360→282357 · D103(source)`; manner pair `Psa 73:1... `→ (see 281103) `Psa 64:10·281103→281104 · D108(manner)`; target pair `Psa 73:13·282382→282381 · D107(target)`.
- **Cross-span operation events** (5; `event`+`span`, outside the strict `pair` network but real cross-span links): `Psa 64:10·281098→281099`, `Psa 68:3·281583→281584`, `Psa 72:7·282331→282332`, `Psa 75:10·282709→282710`, `Psa 64:10·281103→281105` — all on D106(operation).

**Network shape:** one small dense knot in **Psalm 73** (282360/282382/282386 linked across source, seat, coupling, target — Asaph's integrity-in-crisis is the most interconnected sub-graph), a royal pair in **Psalm 72**, a cleansing arc in **Psalm 51**, and a scatter of single couplings elsewhere. The overwhelming majority of the 69 characteristics are **isolated** — no genuine edge — so this family is read as a set of largely free-standing states rather than an interlocking web.

---

## 7. What could not be derived (from this source)

- **Source of the movement:** absent on 68/69 (D103 filled once, `Psa 73:1·282360`). The data does not say what generates righteousness/integrity in nearly every instance.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113): entirely absent (0/69).** No strength, no produced-effect, no prohibition anywhere — a structural gap, not a per-verse omission.
- **Seat: unstated on 64/69.** Interior location is derivable only for the 5 heart/hands cases; for righteousness/uprightness proper the seat is not in the data.
- **Manner: unstated on 59/69.**
- **Bearer: never explicit** — all 69 inferred (defensible from text, but not stated).
- **Role reliability:** D115 = `characteristic` is applied uniformly, including to *the weak* (`82:3·283900`, `82:4·283906` — recipients) and the antonym *wrong* (`58:2·280478`, `7:3·283641`); these role-typings are not supported by the sense and should be treated as suspect, not derived.
- **Cluster typing** cannot place 5 instances (NULL) and mis-places 5 (M10/M11/M34/M07 outliers) — see §1.
- **D112/D116 must be read corrected on 27 instances** before any coupling/locus claim is trusted (§0).

---

## 8. Summary

Righteousness-integrity in Psalms reads, in this source, as a **coherent moral-integrity constellation** — righteousness (M26) + uprightness/truth (M13) + purity/cleanness (M12), 59/69 — carried predominantly as a **status/standing (38/69)** of the inner being rather than an operation (only 1 action), overwhelmingly **seatless** (seated only at heart/hands, and only where the verse says so), **sourceless** (D103 once), with **no intensity/effect/prohibition anywhere**, borne by an **always-inferred human bearer**, and forming only a **sparse network** (28 genuine couplings, one dense knot in Ps 73). The label fits its core but has fused a describable margin — the antonym pole (*evel*, M10), recipients of justice (*dal*, NULL), resultant stability (moved/stand-upright), and a co-located vision (behold). Data hygiene required: **27 D112/D116 swaps** and **188 self-loop non-edges** must be discarded/corrected before reading.
