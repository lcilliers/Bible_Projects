# Family analysis (in isolation) — `keeping-guarding-vigilance` (Psalms)

> Source: `outputs/data/psalms-family-base-sources/psalms__keeping-guarding-vigilance.json` only. Scope-bounded: nothing imported from outside this one file. Method: `verse-analysis/psalms/_family-analysis-method-20260711.md`.
> Counts (meta): 10 meanings · 49 instances · 29 passages. All 49 accounted for below.

Lemma spread: **H8104 (shamar)** 32 inst — keep 23, observe 3, watch 3, guard 2, attend-to 1; **H5341 (natsar)** 14 inst — keep 11, kept 2, observe 1; **H7737 (set)** 2; **H7650 (swears)** 1.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling)/D116(locus) field-swap
Correct order per method = **D116 a code, D112 a phrase**. **6 of 49 instances are transposed** (D112 holds the `internal:`/`external:` code, D116 holds a prose phrase); read them corrected:

| span_id | reference | D112(coupling) holds | D116(locus) holds | corrected reading |
|---|---|---|---|---|
| 269120 | Psa 103:18 | `external:god` | "paired with remembering to obey" | locus=external:god; coupling=remembering-to-obey |
| 269533 | Psa 105:45 | `external:god` | "paired with observing his laws" | locus=external:god; coupling=observing-his-laws |
| 272916 | Psa 132:12 | `external:god` | "paired with the throne promised" | locus=external:god; coupling=throne-promised |
| 269699 | Psa 106:3 | `internal:ib-state` | "paired with the blessedness and righteousness" | locus=internal:ib-state; coupling=blessedness/righteousness |
| 270039 | Psa 107:43 | `internal:ib-state` | "paired with considering God's love" | locus=internal:ib-state; coupling=considering-God's-love |
| 269535 | Psa 105:45 | `external:god` | "paired with keeping his statutes" | locus=external:god; coupling=keeping-his-statutes |

The other 43 instances are in correct order (D116 = a code, D112 = a phrase). All citations below use the **corrected** locus/coupling. `Psa 103:18 · span 269120 · D112/D116 swap`.

### 0.2 Self-loop "edges" are not real links
**46 of 49 instances** carry only self-loop pseudo-edges: `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's own id, on D105 bearer / D107 target / D112 coupling (and D108 manner for the two enemy instances). These are **not network edges** and are excluded. `Psa 119:8 · span 272094 · D105/D107/D112 self-loops`.

**Only the 3 `watch` instances** carry genuine `pair` edges (`resolution:"span"`, to_span ≠ own id) — see §"The network" (§4). Critically, **every genuine to_span points to a span that is NOT one of the 49 masters in this file** → within family scope the inter-master network is **empty**; the only real relations exit the file and cannot be resolved here.

### 0.3 D104 seat / D108 manner = "none"
- **D104 seat = "none" in 49 / 49** — no interior seat is ever named. `Psa 119:167 · span 271629 · D104 seat=none` (even where the verse says "My **soul** keeps your testimonies", seat is left unfilled — a miss; see §5).
- **D108 manner = "none" in 47 / 49.** Filled only in the two predatory-vigilance instances: `Psa 56:6 · span 280300 · D108="lurking / in ambush"` and `Psa 71:10 · span 282046 · D108="consulting together"`.

### 0.4 Absent dimensions
Across **all 49** instances the following never occur: **D109 intensity, D110 specifier, D111 effect, D113 prohibition** (0 occurrences each). **D103 source** occurs **once only** — `Psa 59:9 · span 280648 · D103="because God is his fortress who meets him in steadfast love (v9-10)"` (pair). D110/D111/D113 blanks are unremarkable for an action verb; D103 near-absence and D104 total-absence are the notable gaps.

### 0.5 Cluster NULL / T2
**3 instances have `cluster.code = null`** (the term-cluster cannot type them); **no T2**:
- `Psa 119:30 · span 271780` (H7737 "set") — null.
- `Psa 16:8 · span 274745` (H7737 "set") — null.
- `Psa 15:4 · span 274645` (H7650 "swears") — null.
The other 46 are all `M30 (Obedience)`; `is_outlier=false` on every meaning.

---

## 1. Coherence — does the label fit the data?

**Partly.** The label `keeping-guarding-vigilance` fits the **H8104/H5341 core (46 of 49 instances)** — one coherent inner-being movement: *maintaining attentive custody over something*. But the grouping is **meaning-keyed on ESV surface**, and it has **fused in two distinct movements** via the two null-cluster lemmas:

- **H7737 "set" (2 inst)** — *fixing/orienting the self before an object*, not custody: `Psa 119:30 · span 271780` ("I **set** your rules before me"); `Psa 16:8 · span 274745` ("I have **set** the LORD always before me", coupling `set-the-LORD`, locus internal:ib-state). Distinct movement (self-orientation), cluster NULL.
- **H7650 "swears" (1 inst)** — *oath-binding*: `Psa 15:4 · span 274645` ("who **swears** to his own hurt and does not change", coupling `swear-to-own-hurt`, locus internal:ib-state). Distinct movement (oath), cluster NULL.

These 3 (all cluster-NULL, §0.5) are a **keyword-fusion artefact**; they should be read as adjacent, not as instances of keeping/guarding proper.

**Second coherence finding — one operation, three valences (within the coherent core).** The same lexical movement (shamar/natsar = keep watch over) runs in **three opposite directions**; the difference is the finding (resist collapsing them):
1. **Pious keeping** (majority) — the IB keeps God's word/covenant: e.g. `Psa 119:167 · span 271629`, `Psa 103:18 · span 269120`, `Psa 105:45 · span 269533`.
2. **Failed / lamented keeping** — negated, of Israel/the fathers/others: `Psa 78:10 · span 283010` ("did not keep"), `Psa 78:56 · span 283328`, `Psa 89:31 · span 284683`, `Psa 119:136 · span 271433` ("people do not keep"), `Psa 119:158 · span 271573` ("they do not keep").
3. **Predatory vigilance** — the same verb inverted; **enemies** watch the psalmist: `Psa 56:6 · span 280300` ("they watch my steps"), `Psa 71:10 · span 282046` ("those who watch for my life"). Bearer = enemies (still human IB, hostile).
   - Its mirror-answer: the believer turning the enemies' watching back Godward — `Psa 59:9 · span 280648` ("I will watch for you… you are my fortress"), D114 note: "the turn from the watching enemies to the watching believer".

---

## 2. What the movement is (D101 sense / D102 type)

**D102 type = "action" in 49 / 49** — the family is uniformly verbal/active; no status, state, disposition, affect, faculty, cognition or volition is typed. `Psa 119:2 · span 271709 · D102=action`.

**D101 sense** clusters by lemma/gloss (lexical_gloss on every H8104 record: "to keep: obey; to keep: guard; to keep: look at; to keep: careful"):
- keep / observe (shamar & natsar) — the bulk: `Psa 119:44 · span 271851 · D101="keep / observe (shamar)"`.
- keep, negated/failed — `Psa 78:10 · span 283010 · D101` (read-sense variant "keep (shamar, negated/failed)" per evidence block).
- watch / keep an eye on — predatory: `Psa 56:6 · span 280300 · D101="watch / keep an eye on (shamar - they watch my steps)"`.
- watch / wait expectantly — Godward: `Psa 59:9 · span 280648 · D101="watch / keep watch (shamar - I will watch for you)"`.
- guard — `Psa 39:1 · span 278017` ("guard my ways, muzzle my mouth"), `Psa 119:9 · span 272162` ("guarding it according to your word").
- set (orientation) — `Psa 119:30 · span 271780`; `Psa 16:8 · span 274745`.
- swears (oath) — `Psa 15:4 · span 274645`.

**D106 operation** tracks the sense: `keep` / `keep / observe` / `watch / spy on` / `watch / wait expectantly` / `watch / lie in wait` (all `item_type:"event"`). `Psa 71:10 · span 282046 · D106="watch / lie in wait"`.

---

## 3. Bearer / target / coupling / locus (D105 / D107 / D112 / D116)

**D105 bearer — always human IB, always `inferred` (49/49 inferred; seat never given).** Three bearer groups:
- **the psalmist / the individual** — most H8104 & H5341 keeps: `Psa 119:168 · span 271633 · D105="the psalmist"`.
- **a God-keeping community / the people** — `Psa 103:18 · span 269120 · D105="those who keep covenant"`; `Psa 105:45 · span 269533 · D105="the people (of God)"`; `Psa 119:63 · span 271987` ("those who keep your precepts").
- **the enemies** (hostile human IB) — `Psa 56:6 · span 280300 · D105="the enemies"`; `Psa 71:10 · span 282046 · D105="the enemies"`.
No instance has God as bearer; the IB-screen holds (God appears only as target/object, §below).

**D107 target — what the keeping is over.** Overwhelmingly **God's word/covenant/statutes** (`God's word`, `God's covenant`, `God's statutes`): `Psa 119:106 · span 271250 · D107="God's word"`; `Psa 103:18 · span 269120 · D107="God's covenant"`. Exceptions: **God himself** as the watched-for — `Psa 59:9 · span 280648 · D107="for God (my Strength, my fortress)"`; and **the psalmist's own life/steps** as prey — `Psa 56:6 · span 280300 · D107="my steps"`, `Psa 71:10 · span 282046 · D107="for the psalmist's life"`.

**D116 locus (corrected):** three values only —
- `external:god` — the dominant locus (keeping bound to God's word/covenant): `Psa 119:44 · span 271851 · D116=external:god`.
- `external:person` — the two enemy-watch instances: `Psa 56:6 · span 280300 · D116=external:person`; `Psa 71:10 · span 282046`.
- `internal:ib-state` — **7 instances** where keeping/orienting is seated in the inner state: `Psa 25:10 · span 275955` (coupling `keep-covenant`), `Psa 34:13 · span 277160` (coupling `keep-tongue`), `Psa 39:1 · span 278017` (coupling `muzzle-my-mouth`), `Psa 16:8 · span 274745` (coupling `set-the-LORD`), `Psa 15:4 · span 274645` (coupling `swear-to-own-hurt`), plus the two swap-corrected ones `Psa 106:3 · span 269699` and `Psa 107:43 · span 270039`.

**D112 coupling (corrected) — what the keeping is welded to.** Two shapes:
- **The whole KEEP-arc of the psalm** — a self-referential coupling on nearly every Psalm 119 instance: `Psa 119:60 · span 271966 · D112="paired with the whole KEEP-arc of the psalm"`. This is a bulk pairing to the psalm's own repetition, not a discrete link.
- **Concrete inner pairings** — `keep-covenant` (Psa 25:10), `keep-tongue` (Psa 34:13, restraint of speech), `muzzle-my-mouth` (Psa 39:1), `set-the-LORD` (Psa 16:8), `swear-to-own-hurt` (Psa 15:4); and the failure-pairings `paired with the refusal to walk in his law` (`Psa 78:10 · span 283010`), `paired with turning away treacherously` (`Psa 78:56 · span 283328`), `paired with violating the statutes` (`Psa 89:31 · span 284683`).

**D115 role = "characteristic" in 49 / 49.** No qualifier, no standalone. `Psa 15:4 · span 274645 · D115=characteristic`.

---

## 4. The network (genuine `pair` edges only)

Only the 3 `watch` instances have real edges; **all point outside the 49-master set** (unresolvable in scope):

| from_span | reference | dimension | → to_span | note |
|---|---|---|---|---|
| 280300 | Psa 56:6 | D107 target | 280301 | "my steps" — enemy target |
| 280300 | Psa 56:6 | D112 coupling | 280303 | "waiting for his life" |
| 280648 | Psa 59:9 | D103 source | 280651 | "God is his fortress" (only D103 in the file) |
| 280648 | Psa 59:9 | D107 target | 280647 | "for God (my Strength/fortress)" |
| 280648 | Psa 59:9 | D112 coupling | 280573 | "the refrain answered in singing (v16-17)" |
| 282046 | Psa 71:10 | D107 target | 282047 | "the psalmist's life" |
| 282046 | Psa 71:10 | D112 coupling | 282056 | "the foes who seek his hurt" |

**Network finding:** the inner-being network *within this family* is **null** — no keeping-master links to another keeping-master. The relational life of the movement is entirely (a) self-referential ("the whole KEEP-arc") and (b) the 3 watch-instances reaching to non-family spans in their own verses. The keeping-family is, in this data, a **dense cloud of parallel, un-networked repetitions** (32 of the 49 instances fall in Psalm 119 alone), with a small vigilant sub-movement (Psa 56 / 59 / 71) that actually reaches outward.

---

## 5. The interior anatomy the data actually names

Assembling only filled interior fields:
- **Seat (D104): nothing.** No heart, soul, spirit, eye, tongue is ever recorded as seat (0/49), even where the verse-text supplies one — `Psa 119:167 · span 271629` ("My **soul** keeps") leaves D104=none; `Psa 34:13 · span 277160` ("**Keep** your tongue from evil") records the tongue only as coupling (`keep-tongue`), not as seat. The anatomy is therefore carried **entirely by D116 locus + D112 coupling**, not by seat.
- **Named inner loci (via internal:ib-state, 7 inst):** covenant-keeping (Psa 25:10), tongue-restraint (Psa 34:13), mouth-muzzling (Psa 39:1), self-orientation to the LORD (Psa 16:8), self-costly oath (Psa 15:4), and the two Godward inner turns (Psa 106:3, 107:43). These are the only places the movement is located *inside* the person.
- **Speech-restraint as the concrete interior act:** `keep-tongue` (Psa 34:13) and `muzzle-my-mouth` (Psa 39:1) are the clearest evidence that "keeping" is felt as an inward guarding of speech — the interior gate the movement actually names.
- **The Godward object:** the constant partner of keeping is `external:god` (God's word/covenant) — the movement is defined by what it is bound *to*, not by where it sits.

---

## 6. What could not be derived (flagged)

- **Interior seat (D104): unrecoverable from this source** — "none" 49/49; the study cannot say *where* keeping is seated except by falling back on locus/coupling. Where the verse names a seat ("soul", "tongue", "mouth", "heart"), it was **not captured** — a systematic miss for this family.
- **Source / cause (D103): absent in 48/49** — only Psa 59:9 records why the keeping/watching arises. The motive-anatomy of keeping is essentially unread.
- **D109 intensity / D110 specifier / D111 effect / D113 prohibition: absent in all 49** — no gradation, no result, no explicit prohibition captured (even where the text negates: Psa 78:10 "did not keep" is coded via negated *sense*, not D113).
- **Manner (D108): absent in 47/49** — how the keeping is done is recorded only for the two enemy instances; the *manner* of pious keeping (diligently, continually, hastily — all present in the verse-texts, e.g. Psa 119:4 "kept diligently", 119:44 "continually", 119:60 "hasten") is **not captured**.
- **Cluster typing fails for 3 instances** (Psa 119:30, Psa 16:8 "set"; Psa 15:4 "swears") — cluster NULL; the term-cluster machinery cannot place the two fused non-keeping movements.
- **Network within scope: not derivable** — no genuine edge joins two family masters; the 7 real edges all exit the file and their to_spans (280301/280303/280651/280647/280573/282047/282056) are absent here, so the relations cannot be followed.
- **Field-swap (6 inst)** must be corrected before use (§0.1) or coupling/locus read backwards.

---

## Summary

`keeping-guarding-vigilance` is a **uniformly action-typed (49/49), role=characteristic (49/49) movement of attentive custody**, carried by **shamar (32) + natsar (14)** and bound overwhelmingly to **God's word/covenant** (D116 `external:god`); its one lexical operation runs in **three valences** — pious keeping, lamented/failed keeping, and predatory enemy-watching (with a Godward answer at Psa 59:9). The interior is named **only** via locus/coupling — speech-restraint (keep-tongue Psa 34:13, muzzle-my-mouth Psa 39:1) is the clearest inward act — because **seat (D104) is empty in every instance**. Data debts: seat, source, manner, intensity/specifier/effect/prohibition largely or wholly unread; the within-family network is null (only 3 watch-instances have real edges, all exiting scope); **6 instances are D112/D116-swapped** and **3 are cluster-NULL** (the fused non-keeping lemmas H7737 "set" ×2, H7650 "swears" ×1 — a keyword-fusion artefact the label should not claim).
