# Family analysis — `humility-lowliness-contrition` (Psalms, in isolation)

> Source: `outputs/data/psalms-family-base-sources/psalms__humility-lowliness-contrition.json` only. 21 meanings · 39 instances · 27 passages. All genre `poetic/wisdom`. Every claim cited `reference · span_id · Dnnn(label)`. Nothing imported from outside this file.

---

## 0. Data-integrity screen (done first)

**Field completeness across all 39 instances.** Filled on every instance: D101 sense, D102 type, D104 seat, D105 bearer, D106 operation, D107 target, D108 manner, D112 coupling, D114 discovery, D115 role, D116 locus (39/39 each).

**Absent dimensions (0/39 — cannot be derived from this source):** D109 intensity, D110 specifier, D111 effect, D113 prohibition. No instance carries any of these; any intensity/effect/prohibition reading would be invention.

**D103 source present on only 3/39:** `Psa 70:5 · span 282030 · D103(source)`, `Psa 69:33 · span 306604 · D103(source)`, `Psa 51:17 · span 279701 · D103(source)`. Source of the movement is otherwise unstated.

**D104 seat = "none" on 36/39.** Only three name an interior seat, all in one verse: `Psa 51:17 · span 279698 · D104(seat)="the spirit"`, `Psa 51:17 · span 279700 · D104(seat)="the heart"`, `Psa 51:17 · span 279701 · D104(seat)="the heart"`. The family is almost entirely seat-silent.

**D108 manner = "none" on 36/39.** Only three fill it: `Psa 70:5 · span 282030 · D108="pleading God's haste"`, `Psa 69:33 · span 306604 · D108="not despised, though prisoners"`, `Psa 51:17 · span 279701 · D108="broken and crushed"`. Manner is effectively unread across the family.

**D112(coupling)/D116(locus) field-swap — 13 instances transposed.** In these, D112 holds the `internal:`/`external:` code and D116 holds a prose phrase — the reverse of the correct order (D116 = code, D112 = phrase). Read them corrected. Swapped instances:
`Psa 107:41 · 270026`, `Psa 109:16 · 270200`, `Psa 109:22 · 270260`, `Psa 113:7 · 270767`, `Psa 109:16 · 270199`, `Psa 109:22 · 270259`, `Psa 109:16 · 270201`, `Psa 102:17 · 307204`, `Psa 138:6 · 273351`, `Psa 109:31 · 270312`, `Psa 113:7 · 270763`, `Psa 132:15 · 307869`, `Psa 106:42 · 269764`. In all 13 the corrected locus (D116) = `internal:ib-state` and the corrected coupling (D112) = the phrase now sitting in D116 (e.g. `Psa 138:6 · 273351`: locus `internal`, coupling "paired with the haughty God knows from afar"). The other 26 instances are already in correct order.

**Corrected D116 locus distribution (after de-swapping):** `internal:ib-state` dominant (~31), `internal:heart` ×2 (`Psa 51:17 · 279700`, `· 279701`), `internal:spirit` ×1 (`Psa 51:17 · 279698`), `external:god` ×3 (`Psa 69:33 · 306604`, `Psa 89:22 · 284632`, `Psa 81:11 · 283800`), `external:person` ×2 (`Psa 69:32 · 281838`, `Psa 76:9 · 282853`).

**Cluster NULL — 2 instances the term-cluster cannot type:** `Psa 88:15 · span 284445 · [H6323:helpless] cluster=null`, `Psa 113:7 · span 270763 · [H1800:poor] cluster=null`. These carry no M-code and float unattached to any characteristic-cluster.

**Self-loop non-edges.** 100 "edges" across the file are D105/D107/D112/etc. flags with `resolution:"inferred"`, `from_span:null`, `to_span=own id` — self-loops, **not** network links. Excluded from the network (§Network). Only 19 genuine `pair`/`span` edges linking a different span remain.

**D115 role = "characteristic" on 39/39; D105 bearer = "inferred" on 39/39.** No stated bearers; no qualifier/standalone roles. Every span is read as a characteristic borne by an inferred human subject.

---

## 1. Coherence — does the label fit its data?

**Partial. The keyword grouping fuses three related-but-distinct inner-being movements, plus a socio-material status that is not a disposition at all.** Cluster tally: **M24(Weakness) 31/39**, M09(Humility) 2, null 2, and four singleton outliers (M20 Doubt, M11 Repentance, M05 Love, M29 Desire). The label's own three words map onto three separable movements:

- **(a) Destitution / affliction as STATUS** — the largest group. `needy`(ebyon, ×8), `poor`(ani, ×6), `humble`(anav, several), `destitute` (H7326, H6199), `needy one`, `poor`(dal), `poor`(ebyon). D102 type = **status** on 24/39 (e.g. `Psa 107:41 · 270026 · D102="status"`; `Psa 109:22 · 270260 · D102="status"`). This is largely an **outward/social condition** owned before God, not an interior act. It is the "lowliness" pole but skews to material poverty (`lexical_gloss` = "afflicted"/"needy").
- **(b) Humility / meekness as DISPOSITION or STATE** — `humble`(anav, `Psa 25:9 · 276100 · D102="state"`), `humble`(H6041, `Psa 18:27 · 275028`), `meek`(anav, `Psa 37:11 · 277600 · D102="affect"`), `lowly`(shaphal, `Psa 138:6 · 273351`, M09), `subjection`(kana, `Psa 106:42 · 269764`, M09), `meekness`(anvah, `Psa 45:4 · 278962`, M05). This is humility proper — the teachable, God-raised posture.
- **(c) Contrition / brokenness** — `broken`(shabar, `Psa 51:17 · 279698`, `· 279700`), `contrite`(dakah, `Psa 51:17 · 279701`), `brokenhearted`(shabar, `Psa 147:3 · 274329`, `Psa 34:18 · 277202`), `brokenhearted`(kaah, `Psa 109:16 · 270201`, M20), `dust`(dakka, `Psa 90:3 · 307067`, M11). The shattered-heart movement — distinct from both poverty and meekness.
- **(d) Volitional submission (single, and its refusal)** — `submit`(abah, `Psa 81:11 · 283800`, M29 Desire, outlier): read as **failed** submission, "the unwilling heart, obedience declined" (`D114`). A volition item, opposite in polarity to the rest.

**Finding:** the family is a loose semantic net, not one movement. Its coherent core is "the lowly self before God," but it welds (a) a socio-material *status* to (b)–(c) interior *dispositions/states*, and admits (d) a volitional refusal that is the family's inverse. The four `is_outlier=True` records (M20/M11/M05/M29) are the file's own flag that these cross out of the expected M24 cluster.

---

## 2. The movements evidenced (cited)

### 2.1 Destitution owned before God, met by divine reversal (M24, status)
The recurring shape: the bearer *is* poor/needy (a status), and the operation is something God does to that status — usually a **reversal upward**. `Psa 107:41 · 270026 · D106(operation)="be raised"` (out of affliction); `Psa 113:7 · 270767 · D106="be lifted"` (from the ash heap); `Psa 132:15 · 307869 · D106="be satisfied"` (with bread); `Psa 109:31 · 270312 · D106="be defended"` (by God at his right hand); `Psa 102:17 · 307204 · D106="be stripped bare"` with target "yet heard by God". The interior contribution is dependence: `Psa 86:1 · 306975 · D114` "the lowly estate David pleads as his claim on God, humility the ground of the appeal." The confident pole is explicit at `Psa 40:17 · 278295 · D102="affect"`, D106 "the interior owns its poverty yet rests in being remembered by God" — the one instance typed *affect*, holding weakness and confidence together.

### 2.2 Destitution as victim-status under enemies (M24)
The same words also carry pure affliction with no reversal: `Psa 109:16 · 270199 · D106="be pursued"` (by the enemy) and its parallel `· 270200`; `Psa 82:4 · 283907 · D106="need deliverance"` (from the wicked's hand); `Psa 82:3 · 283904 · D106="be left in want"` (by the court); `Psa 88:15 · 284445 · D106="be helpless / distracted"` under terror (cluster null). Here "lowliness" is imposed suffering, not chosen posture.

### 2.3 Humility as the teachable, God-raised posture (M24/M09)
Meekness read as an interior state God favours: `Psa 25:9 · 276100 · D106="God leads the humble in what is right and teaches them his way"` with D114 "only the humble are teachable"; `Psa 147:6 · 274349 · D106` "the humble are the ones God lifts up"; `Psa 149:4 · 274480 · D106` "God beautifies with salvation — lowliness crowned"; `Psa 18:27 · 275028 · D106` "God saves a humble people but brings down haughty eyes"; `Psa 138:6 · 273351 · D101="lowly"` "he regards the lowly, but the haughty he knows from afar" (M09). D107 target on these = "humility" (inferred). The movement is a **posture-met-with-lifting** contrast against haughtiness.

### 2.4 Meekness that ends in delight/peace (M24/M05)
`Psa 37:11 · 277600 · D102="affect"`, D106 "the meek shall inherit the land and delight themselves in abundant peace", D114 "meekness ends not in loss but in a peace it delights in." And the royal-virtue reading `Psa 45:4 · 278962 · [H6037:meekness] D114` "humility as a royal virtue the king advances… the surprising heart of true kingship" (M05, outlier). D106 is "none" on 278962 — the movement is named only by locus/coupling, its operation unread.

### 2.5 Contrition — the shattered heart God will not despise (M24, action)
The family's densest interior node, all in `Psa 51:17`: `span 279698 · D101="broken / shattered (shabar - a broken spirit)" · D104="the spirit" · D102="action"`; `span 279700 · D104="the heart" · D101="broken (shabar - a broken and contrite heart)"`; `span 279701 · D101="crushed / contrite (dakah)" · D104="the heart" · D103(source)="such a heart God will not despise"`. This is the only place the family names its seat (heart/spirit) and the only place contrition is read as an *action/event* on the interior rather than a status. Complemented by `Psa 147:3 · 274329 · D106` "the broken heart and its wounds are the object of God's healing" and `Psa 34:18 · 277202 · D106` "the LORD is near to the brokenhearted and saves the crushed in spirit." Outlier `Psa 109:16 · 270201 · [H3512:brokenhearted/kaah] D106="be pursued to death"` (M20 Doubt) — brokenness hounded to the grave.

### 2.6 Creatureliness and (failed) submission — the edges of the family
`Psa 90:3 · 307067 · [H1793:dust/dakka] D106="be turned back to dust"` (M11 Repentance, outlier), D114 "the creatureliness and mortality of man." `Psa 106:42 · 269764 · [H3665:subjection/kana] D106="be brought into subjection"` (M09). `Psa 89:22 · 284632 · [H6031:humble/anah] D106="seek to humble"` — the *wicked's* attempt to humble the anointed, thwarted (locus corrected `external:god`). `Psa 81:11 · 283800 · [H0014:submit/abah] D102="disposition" · D106="refuse to submit"` — the family's inverse: humility withheld.

---

## 3. The network (genuine `pair`/`span` edges only)

19 genuine edges survive after excluding 100 self-loops. They are **sparse and locally clustered**, not a family-wide web. Three sites:

- **Poor↔needy welding (word-pair "poor and needy").** `Psa 70:5`: `span 282030 → 282029 · D112(coupling)` and reciprocal `span 282029 → 282030 · D112`; plus `span 282030 → 282031 · D103(source)` (God the help/deliverer). `Psa 74:21 · 282622 → 282624 · D106(operation)` and `· D112(coupling)` — the poor issuing in praise.
- **The 69:32–69:33 dependence pair.** `Psa 69:33 · 306604 → 306603 · D103(source)` and `· D106(operation)` — "the LORD hears the needy"; `Psa 69:32 · 281838 → 281840 · D106` and `· D112` — the humble see and are glad. `Psa 76:9 · 282853 → 282851 · D106` and `→ 282849 · D112` — the humble saved by God's judgment.
- **The contrition triangle in Psa 51:17.** Internally linked: `279698 → 279699 · D104/D112`; `279700 → 279702 · D104`, `→ 279701 · D112`; `279701 → 279702 · D104`, `→ 279699 · D112`, `→ 279705 · D103`. Spirit, heart, and contrite-heart are welded to one another and to the "God-will-not-despise" source — the one genuinely networked interior node in the family.
- **Singleton:** `Psa 45:4 · 278962 → 278961 · D112(coupling)` — meekness paired with truth and righteousness.

**Network finding:** the family has no cross-passage backbone. Edges are within-verse or within-word-pair only; 34 of 39 spans participate in no genuine outgoing link. The interior "movement" is asserted per-instance via D106/D114, not built as a graph.

---

## 4. The interior anatomy the data actually names

Assembling only *filled* seats/sources/couplings:

- **Seats named (3, all `Psa 51:17`):** the spirit (`279698`), the heart (`279700`, `279701`). This is the family's entire named interior anatomy — contrition alone locates itself; poverty and humility do not.
- **Corrected loci:** overwhelmingly `internal:ib-state` (a generic interior condition, un-anatomised); `internal:heart`/`internal:spirit` only at 51:17; `external:god` where the movement is God-directed (69:33, 89:22, 81:11); `external:person` where the bearer is a witnessing group (69:32, 76:9).
- **Sources named (3):** God as the one who hears/does-not-despise (`Psa 69:33 · 306604 · D103`; `Psa 51:17 · 279701 · D103`; `Psa 70:5 · 282030 · D103` = God the help/deliverer). Where source is read, it is always God.
- **Couplings (corrected D112):** consistently pair the low estate with (i) its twin word (poor↔needy, broken↔contrite), (ii) the affliction it sits in, or (iii) the divine act that answers it (raised, satisfied, healed, regarded, saved). The interior is defined relationally — by what it is bound to and what God does to it — far more than by any faculty.

**Net anatomy:** heart + spirit (contrition only) + a pervasive un-located "ib-state," directed toward or answered by God. The dominant reading is **posture/status before God**, not an internal mechanism.

---

## 5. What could not be derived (flagged)

- **D109 intensity, D110 specifier, D111 effect, D113 prohibition:** absent on all 39 — no basis in this source.
- **Seat unread on 36/39; manner unread on 36/39** — the interior location and mode of the movement are simply not carried outside `Psa 51:17` (seat) and two verses (manner).
- **Source unread on 36/39** — what moves the lowliness is stated only 3 times.
- **Two cluster-null instances** (`Psa 88:15 · 284445`, `Psa 113:7 · 270763`) — the term-cluster cannot type them; their characteristic-membership is underivable here.
- **D112/D116 swap on 13 instances** — usable only after the correction listed in §0; a naive read of those fields would mis-assign locus vs coupling.
- **`Psa 45:4 · 278962` operation "none"** — meekness-as-royal-virtue is asserted by D114/D116 but its D106 movement is unread.
- **All 39 bearers inferred** — no instance states its subject; every "whose inner being" is a reader inference (defensible — psalmist / the humble / God's afflicted people — but not stated).
- **Family-level movement** is not derivable as a network: 100 self-loops are non-edges, and the 19 genuine edges are local; any "arc across the Psalter" would be invention.

---

## 6. Summary

`humility-lowliness-contrition` in Psalms = **21 meanings / 39 instances, all poetic/wisdom, 31/39 clustered M24(Weakness)**, read as a loosely-fused net of four movements — destitution-as-status met by divine reversal (largest), humility-as-teachable-posture, contrition-of-the-shattered-heart (the only seat-naming, only genuinely networked node, at Psa 51:17), and a single volitional *refusal* to submit (Psa 81:11, the family's inverse). The interior is defined almost entirely relationally (locus `internal:ib-state`, source = God) rather than by faculty; intensity/specifier/effect/prohibition are wholly absent, seat and manner unread on 36/39, and the file carries a 13-instance D112/D116 swap plus 2 null-cluster and 4 flagged-outlier records — all corrected/flagged above.
