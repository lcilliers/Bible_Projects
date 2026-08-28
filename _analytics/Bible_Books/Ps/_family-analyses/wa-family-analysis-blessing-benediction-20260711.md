# Family analysis — `blessing-benediction` (Psalms, in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__blessing-benediction.json` only. Method: `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md`. Every claim cites `reference · span_id · Dnnn(label)` into that one file. Nothing imported from outside it.
>
> **Scope of the file:** 5 meanings · 65 instances · 49 passages · provenance `ib_characteristic v3 (meaning-keyed) + family grouping v1 + term-based cluster v2`. All 65 instances are `genre = poetic/wisdom`; 15 are passage anchors.

The 5 meanings:
| char_key | meaning | lemma | cluster | n | outlier |
|---|---|---|---|---|---|
| `H1288:bles` | bless (barak, verbal act) | H1288 | M39 Blessing | 22 | no |
| `H1288:bless` | Blessed (barak, "blessed be…") | H1288 | M39 Blessing | 21 | no |
| `H0835:bless` | Blessed (esher, beatitude) | H0835 | M39 Blessing | 20 | no |
| `H3444:salvation` | Salvation | H3444 | **M38 Salvation** | 1 | **yes** |
| `H3867:lend` | lending | H3867 | **null** | 1 | no |

---

## 0. Data-integrity screen

**0.1 D112(coupling)/D116(locus) field-swap — 32 of 65 instances are transposed.** Correct order is D116 = code (`internal:`/`external:`), D112 = phrase. In 32 instances D112 holds the code and D116 holds the prose phrase; they must be read swapped. The 33 remaining instances are correctly ordered (D116 = code, D112 = phrase, the latter often a genuine `pair`). Swapped instances (read D112↔D116):

`Psa 100:4·268795`, `Psa 103:1·269052`, `Psa 103:2·269132`, `Psa 103:22·269167`, `Psa 104:1·269203`, `Psa 104:35·269343`, `Psa 115:18·270873`, `Psa 134:1·273030`, `Psa 134:2·273043`, `Psa 135:20·273103`, `Psa 135:20·273107`, `Psa 96:2·285566`, `Psa 135:19·307926`, `Psa 135:19·307930`, `Psa 106:48·269807`, `Psa 112:2·270667`, `Psa 113:2·270729`, `Psa 118:26·271128`, `Psa 118:26·271132`, `Psa 124:6·272504`, `Psa 128:4·272665`, `Psa 135:21·273109`, `Psa 89:52·284851`, `Psa 106:3·269698`, `Psa 112:1·270645`, `Psa 127:5·272633`, `Psa 128:1·272648`, `Psa 128:2·272659`, `Psa 94:12·285319`, `Psa 89:15·307038`, `Psa 137:8·308039`, `Psa 137:9·308043`.

Read corrected, the code split is clean: **32 instances `external:god`** (blessing directed at God) vs **33 instances `internal:ib-state`** (the beatitude / interior condition) — this split is load-bearing for the coherence finding (§1).

**0.2 Self-loop "edges" are not links — 183 of them.** Every instance carries `item_type:"flag"`, `resolution:"inferred"` pseudo-edges on D105(bearer), D107(target), D112(coupling) with `from_span:null` and `to_span` = the span's own id (e.g. `Psa 100:4·268795 · D105 bearer → 268795`). These are self-references, **not** network links; excluded from the network (§4).

**0.3 Genuine `pair` edges — 24 (from 12 source spans).** Only `item_type:"pair"`, `resolution:"span"`, to a **different** span. Of the 24, **21 point OUT of the family** (to spans not in this file — other characteristics in the same verse); their target content is **not derivable here**. Only **3 in-family** edges exist (§4).

**0.4 seat(D104) = "none" in 64 of 65.** The sole filled seat is `Psa 62:4·280959 · D104(seat)="the mouth"` (`resolution:inferred`). The interior seat is otherwise wholly unstated.

**0.5 manner(D108) = "none" in 57 of 65.** 8 are filled (§3.5).

**0.6 Absent dimensions — D109(intensity), D110(specifier), D111(effect), D113(prohibition) are absent in ALL 65 instances.** The family carries no intensity, specifier, effect or prohibition data at all.

**0.7 Cluster null / outlier.** One instance has `cluster.code = null`: `Psa 37:26·277711` (`H3867:lend`) — the term-cluster cannot type it. No T2. One meaning is a flagged crossover: `H3444:salvation` (`Psa 3:8·278202`), `is_outlier=true`, cluster **M38 Salvation** (not M39).

**0.8 Every bearer is inferred (D105 `resolution:inferred` in 65/65); D107(target) inferred in 58/65; D112(coupling) inferred in 54/65.** No bearer is stated on the surface; all are read-in. D103(source) is present in only **4** instances (§3.4).

---

## 1. Coherence — does the label fit? (first-class finding)

**The label `blessing-benediction` fuses at least two distinct inner-being movements, plus two keyword-bleed intruders.** The keyword "bless(ed)/blessing" has gathered senses that move in opposite directions.

**Movement A — *barak*: the interior's act of blessing God (doxology / praise).** 43 instances (`H1288:bles` 22 + `H1288:bless` 21). `D102(type)="action"` dominant; the IB's **output directed at God**: corrected `D112(coupling)="external:god"` on ~32 spans. Sense variants "bless (barak)", "blessed be (barak)". E.g. `Psa 103:1·269052 · D101(sense)="bless (barak)"·D114="'BLESS the LORD, O my soul' — the self-summons to praise"`; `Psa 41:13·278423 · D106(operation)` seals Book I in blessing.

**Movement B — *esher*: the state of blessedness/happiness (beatitude).** 20 instances (`H0835:bless`). `D102(type)="state"`/"affect"; a **condition predicated of the human IB**, not an act. Corrected `D116(locus)` reads `internal:ib-state`. E.g. `Psa 1:1·275341 · D101="blessed (esher)"·D114="the psalter opens by weighing a whole life as happy"`; `Psa 128:1·272648 · D106="the settled well-being of the man whose life is shaped by avoidance-of-evil and delight-in-law"`. Direction is the inverse of A: A is the IB reaching **up to God**; B is a **felt interior condition** pronounced over a person.

**Two intruders (keyword bleed, not blessing movements):**
- `Psa 3:8·278202 · H3444:salvation · D102(type)="cognition"·D101="salvation belongs to the LORD"` — a settled **confession**, cluster M38, `is_outlier=true`. Enters the family only because "your **blessing** be on your people" sits in the same verse. `D114`: "against the taunt of v2 … the interior lands on the opposite settled conviction."
- `Psa 37:26·277711 · H3867:lend · D102(type)="volition"·D101="ever lending generously"` — habitual **generosity**, `cluster=null`. Enters only because "his children become a **blessing**" is in the verse text. Not a blessing act or state.

**Sub-variation inside Movement A (same barak sense, opposite valence):**
- **Hypocritical blessing:** `Psa 62:4·280959 · D106(operation)="bless (outwardly)"·D108(manner)="outwardly, hypocritically"·D104(seat)="the mouth"·D114="the split of the hypocrite … the mouth and the heart at war"` (bearer = "the enemies"). A *false* blessing.
- **Reflexive self-blessing:** `Psa 49:18·279352 · D101="bless / count blessed (barak - himself)"·D114="the rich man blessing his own soul, the smug self-satisfaction that death will silence"` (bearer = "the rich man").
- **Imprecatory beatitude (Movement B turned harsh):** `Psa 137:8·308039` and `Psa 137:9·308043 · D101="blessed (esher)"` pronounce blessedness on Babylon's executioner — `D114`: "the harshest imprecation of the Psalter … pronounced as a blessing."

**Verdict:** the M39 grouping of barak + esher is defensible as "blessing" lexically, but analytically the file **fuses an act (A, IB→God) with a state (B, condition-of-IB)**, and additionally mis-grabs a confession and a generosity span. Any downstream synthesis must keep A and B separate and drop the two intruders.

---

## 2. Type anatomy (D102, all 65 cited by distribution)

`D102(type)` across the family: **action 32 · state 16 · affect 14 · status 1 · cognition 1 · volition 1**. Actions = Movement A (barak, the blessing-act, e.g. `Psa 100:4·268795`). State/affect/status = Movement B (esher beatitudes, e.g. `Psa 128:2·272659 · D102="state"`) plus affect-loaded doxologies. cognition = the salvation-confession (`Psa 3:8·278202`); volition = the lending-habit (`Psa 37:26·277711`). `D115(role)="characteristic"` in **all 65** — no qualifier, no standalone; the family is uniformly read as characteristic-level.

---

## 3. The dimensions, grounded

### 3.1 sense (D101)
Two lexical cores: **barak** "bless (barak)" ×20 + variants, and **esher** "blessed (esher)" ×14 + variants. The read-sense phrases are richly specified per verse (e.g. `Psa 16:7·274737 · D101="bless the LORD who gives me counsel"`; `Psa 65:4·281202 · D101="blessed / happy (esher - blessed is the one you choose)"`). Singletons: `Psa 3:8·278202 "salvation belongs to the LORD"`, `Psa 37:26·277711 "ever lending generously"`.

### 3.2 seat (D104)
Effectively **unnamed** (§0.4): 64/65 = "none". The one filled seat is `Psa 62:4·280959="the mouth"` — and it names the seat of a *false* blessing. Note: the "O my soul" self-summons (Ps 103–104) is **not** coded as a D104 seat; nephesh survives only as a D116 locus phrase, e.g. `Psa 103:1·269052 · D116(locus)="paired with the soul stirred to bless"` (swapped field). The family therefore supplies almost no positive interior-seat anatomy.

### 3.3 bearer (D105) — all human IB, all inferred
Dominant bearers: "the psalmist" ×18, "the worshippers" ×9, "the people" ×4, "the God-fearer(s)" ×4, corporate bodies ("the great congregation", "house of Levi/Israel/Aaron", "the priests"). All are human inner beings (Screen 0 passes — the blessing is the human act/state; God is the arena/target, not the bearer). Edge cases still human: "the enemies" (`Psa 62:4·280959`, hypocrites), "the rich man" (`Psa 49:18·279352`), "the avenger" ×2 (`Psa 137:8·308039`, `Psa 137:9·308043`). Every D105 is `resolution:inferred`.

### 3.4 source (D103) — present in only 4 (all the *ground* of doxology)
- `Psa 66:20·281321 · D103="because God has not removed his steadfast love (v20)"`
- `Psa 68:19·281495 · D103="because God daily bears us up, the God of our salvation (v19)"`
- `Psa 68:26·281552 · D103="of the God who has worked/summoned his power for them (v28)"`
- `Psa 68:35·281648 · D103="the God who gives power and strength to his people (v35)"`

These four name **why** the IB blesses: God's chesed, daily sustaining, and power. For the other 61 instances the source/cause of the blessing act or state is **not derivable**.

### 3.5 operation (D106) & target (D107)
`D106` is the verbal act: "bless" ×27, "be blessed" ×16, plus richly-glossed event strings (e.g. `Psa 34:1·277128 · D106="the self resolves to bless the LORD at all times, his praise continually in the mouth — unbroken praise"`). `D107(target)` for Movement A points to God: "the LORD" ×10, "doxology" ×4, "God's name" ×2, etc. For Movement B `D107` names the *ground* of the beatitude, not a target of address: "beatitude" ×3, "in fearing God" ×2, "in keeping justice", "beatitude-of-pardon" (`Psa 32:1·276872`), "rightly-placed-trust" (`Psa 40:4·278326`). 3 instances have `D107="none"`.

### 3.6 manner (D108) — 8 filled (§0.5)
`Psa 62:4·280959="outwardly, hypocritically"`; `Psa 63:4·281054="as long as he lives, lifting up his hands"`; `Psa 66:8·281376="making the sound of his praise heard"`; `Psa 68:26·281552="in the great congregation"`; `Psa 66:20·281321="for not rejecting his prayer nor removing his love"`; `Psa 68:19·281495="daily"`; `Psa 72:19·282288="forever, the whole earth filled with his glory"`; `Psa 65:4·281202="chosen, brought near to dwell in God's courts"`. The rest = "none".

### 3.7 coupling (D112) / locus (D116) — read corrected (§0.1)
Corrected codes: **`external:god` on 32** (blessing bound to God — the doxology axis), **`internal:ib-state` on 33** (the beatitude/interior-condition axis). The corrected *phrases* (in D112 for the correctly-ordered rows, or D116 for swapped rows) tie each blessing to a companion movement, e.g. `Psa 128:1·272648` couples blessedness with "fearing and walking"; `Psa 106:3·269698` with "observing justice and doing righteousness"; `Psa 84:5·284105`-class rows couple with dwelling/strength-in-God. This is the file's richest relational layer, but it lives as **flag/value phrases**, not as network edges.

### 3.8 discovery (D114) — source read, present in all 65
D114 is filled on every instance and is the reader's primary evidence (cited throughout above). It repeatedly distinguishes near-duplicates the census would merge, e.g. `Psa 145:2·274121 · D114="distinct from the forever-vow: praise distributed into … ordinary time, a habit not just an oath"`; `Psa 144:15·308152 · D114="read distinct from v15a: the interior corrects prosperity-happiness with covenant-happiness"`. These per-verse distinctions are findings in their own right.

---

## 4. The network (genuine `pair` edges only)

24 genuine edges from 12 source spans, on dimensions D103/D107/D108/D112. **21 point OUT of this family** (target span not in the file) — so only the *fact* of a link is derivable, not the partner's content. Out-of-family sources: `Psa 62:4·280959`, `Psa 63:4·281054`, `Psa 66:8·281376`, `Psa 66:20·281321`, `Psa 68:19·281495`, `Psa 68:26·281552`, `Psa 49:18·279352`, `Psa 65:4·281202` (each linking a blessing to its verse-mate qualifier/reason/manner span).

**In-family edges — only 3, forming the Book II doxology reciprocal:**
- `Psa 72:18·282281 · D112(coupling) → 282288`
- `Psa 72:19·282288 · D112(coupling) → 282281` (reciprocal with the above: "Blessed be the LORD…" ↔ "Blessed be his glorious name")
- `Psa 68:35·281648 · D112(coupling) → 281495` (`Psa 68:19`) — the closing doxology couples back to the opening one within Ps 68.

**Network verdict:** the inner-being network *within* this family is **extremely sparse** — one reciprocal pair (Ps 72:18↔19) and one directed back-link (Ps 68:35→19). All other relational weight is either self-loop noise (§0.2) or points to spans this file does not contain. The family is, as a network, almost entirely a set of isolated nodes.

---

## 5. The interior anatomy the data actually names

Assembling only filled fields:
- **Seats:** just one — "the mouth" (`Psa 62:4·280959`), and it is the seat of hypocritical blessing. No heart/soul/spirit seat is coded (the soul appears only as locus prose).
- **Sources/grounds:** God's steadfast love, daily sustaining, and power (`Psa 66:20`, `68:19`, `68:26`, `68:35`) — the only stated *causes* of blessing.
- **Couplings (corrected):** two axes — blessing bound **to God** (`external:god`, ×32, the doxology) and blessedness as an **interior state** (`internal:ib-state`, ×33), the latter repeatedly tied to fear-of-God, trust, keeping-justice, and dwelling-with-God (D112/D116 phrases, §3.7).
- **Manner:** lifted hands, ceaseless/daily, corporate/in-the-congregation, audible praise (§3.6).

The named anatomy is thus **relational and postural** (God-directed act, corporate setting, lifted hands, daily rhythm) rather than **somatic-interior** (the heart/soul/spirit seats are not coded).

---

## 6. What could not be derived (from this file)

1. **No intensity, specifier, effect, or prohibition anywhere** — D109/D110/D111/D113 absent in all 65 (§0.6). The strength, sub-type, consequence, and any negation of blessing are unread.
2. **Interior seat is unread for 64/65** (§0.4, §3.2) — where in the IB blessing arises is not stated except the mouth of a hypocrite.
3. **Cause/source unread for 61/65** — D103 filled only 4 times (§3.4).
4. **The out-of-family edge partners (21 edges) are opaque** — the file gives no content for those target spans (§4), so the movements barak/esher connect *to* cannot be described from here.
5. **Every bearer is inferred, not surface-stated** (65/65, §0.3); confidence in "whose IB" rests on read-in judgement.
6. **The intruder spans cannot be properly typed here:** `Psa 37:26·277711` has `cluster=null`, and `Psa 3:8·278202` is a flagged M38 crossover — their membership in this family is a keyword artefact, not a derivable inner-being link (§1).
7. **Two coded fields are unreliable as stored** — 32 instances need the D112↔D116 swap applied before use (§0.1); consumers reading the raw fields will invert coupling/locus.

---

## 7. Summary

`blessing-benediction` is not one movement but **two** — *barak*, the IB's **act of blessing God** (43 instances, action, `external:god`, doxology and self-summons to praise), and *esher*, the **state of blessedness/happiness** pronounced over a person (20 instances, state/affect, `internal:ib-state`, the beatitude) — with **two keyword intruders** (a salvation-confession, `Psa 3:8·278202`; a generosity-habit, `Psa 37:26·277711`) that should be dropped. Within *barak* sit a hypocritical blessing (`Psa 62:4`) and a self-blessing (`Psa 49:18`); within *esher* sit the two harshest imprecatory beatitudes of the Psalter (`Psa 137:8-9`). The data is dimensionally **thin** — no intensity/specifier/effect/prohibition, seat unnamed in 64/65, source in only 4 — and, as a network, **almost empty** (one in-family reciprocal pair, Ps 72:18↔19; one back-link, Ps 68:35→19; everything else self-loop noise or out-of-family). Its richest layer is the corrected D112/D116 coupling axis and the per-verse D114 reads, which keep near-duplicate blessings distinct. **Integrity caveats:** 32/65 have the D112↔D116 field swap; all bearers inferred; one null-cluster and one flagged M38 outlier.
