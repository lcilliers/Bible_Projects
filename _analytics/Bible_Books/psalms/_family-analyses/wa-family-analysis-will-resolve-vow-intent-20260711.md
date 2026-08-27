# Family analysis — `will-resolve-vow-intent` (Psalms, in isolation)

> Source: `verse-analysis/psalms/_base-sources/psalms__will-resolve-vow-intent.json` only. 28 meanings · 35 instances · 32 passages. Every instance is a `poetic/wisdom` genre span. Citations = `reference · span_id · Dnnn(label)`. Where the source cannot bear a reading it is flagged, not filled.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap
Correct order = D116 a code (`internal:`/`external:`), D112 a prose phrase. **11 of 35 instances are transposed** — D112 holds the code, D116 holds a phrase. Read them corrected (the code belongs to locus, the phrase to coupling):

| # | reference · span_id | D112 holds (→ real locus) | D116 holds (→ real coupling) |
|---|---|---|---|
| 1 | Psa 116:14 · 270937 | `external:god` | "paired with the presence of all his people" |
| 2 | Psa 116:18 · 270955 | `external:god` | "paired with the presence of all his people" |
| 3 | Psa 132:2 · 272961 (vow) | `external:god` | "paired with his oath" |
| 4 | Psa 103:14 · 269094 | `internal:ib-state` | "paired with God knowing and remembering" |
| 5 | Psa 110:3 · 270518 | `external:god` | "paired with the king's God-given exaltation" |
| 6 | Psa 115:8 · 270908 | `internal:ib-state` | "paired with trusting in them" |
| 7 | Psa 106:35 · 307474 | `internal:ib-state` | "paired with learning their ways" |
| 8 | Psa 111:10 · 270577 | `external:god` | "paired with good understanding" |
| 9 | Psa 106:43 · 269773 | `internal:ib-state` | "paired with rebelliousness" |
| 10 | Psa 116:12 · 307631 | `external:god` | "paired with lifting the cup of salvation" |
| 11 | Psa 132:2 · 272959 (swore) | `external:god` | "paired with the vow to the Mighty One" |

The remaining 24 instances carry the fields in correct order (D116 a code, D112 a phrase/flag). All corrected loci are used in §3–§4 below.

### 0.2 Self-loop "edges" are not network links
The `edges` arrays are dominated by `item_type:"flag"` / `resolution:"inferred"` items whose `to_span` = the span's own id (chiefly D105 bearer, and D107 target / D108 manner / D112 coupling where inferred). These are self-loops, **not** links. Every one of the 35 spans carries a self-loop D105 bearer edge (bearer is `inferred` throughout — see §0.4).

**Genuine `pair` edges (`resolution:"span"`, to a different span)** exist on: Psa 61:8·280907 (D107→280908, D112→280904); Psa 65:1·281170 (D107→281169, D112→281165); Psa 76:11·282793 (D107→282790, D112→282790); Psa 55:22·280143 (D103→280148, D107→280144, D112→280151); Psa 76:11·282790 (D108→282793, D112→282793); Psa 58:2·280477 (D104→280476, D107→280478, D108→280476, D112→280478); Psa 54:6·280007 (D112→280009); Psa 64:6·281138 (D108→281141, D112→281141); Psa 62:4·280953 (D112→280956); Psa 56:12·280246 (D107→280247, D112→280247).

**Critical: only ONE genuine edge links two family masters.** The reciprocal pair **Psa 76:11 · 282790 (vow) ⇄ 282793 (perform)** — "Make your vows to the LORD your God and perform them." Every other genuine `pair` edge points to a `to_span` that is **not** a master in this file (a neighbouring word in the same verse). So the family's internal network is effectively a single edge; all other relational data reaches *outside* the family scope. The network is extremely sparse (see §5).

### 0.3 seat(D104) / manner(D108) = "none"
- **seat**: 34 of 35 are `none`. The sole named seat is **Psa 58:2 · 280477 · D104(seat)="the heart"** (`pair`→280476) — "in your hearts you devise wrongs."
- **manner**: 28 of 35 are `none`. The 7 filled: Psa 61:8·280907 "day after day"; Psa 66:13·306497 "with burnt offerings, in God's house"; Psa 76:11·282790 "and perform them"; Psa 58:2·280477 "in the heart"; Psa 54:6·280007 "freely, ungrudgingly"; Psa 64:6·281138 "diligently, as a perfected search"; Psa 56:12·280246 "as a debt of gratitude."

### 0.4 Absent dimensions
- **D109 intensity, D110 specifier, D111 effect, D113 prohibition: absent from ALL 35 instances.** No instance carries these ve_nrs.
- **D103 source: present on exactly ONE instance** — Psa 55:22 · 280143 · D103(source)="and he will sustain you (v22)". Absent from the other 34.
- **D105 bearer: `resolution:"inferred"` on all 35** — no bearer is textually explicit; every one is a reader inference.

### 0.5 Cluster NULL / T2
`is_outlier` = false for every meaning. Cluster typing:
- **Null cluster (code + candidates null) — 10 meanings / 16 instances**: perform H7999 (4), cast H7993 (2), pay H7999 (2), vow H5087 (2), chosen H4490 (1), devise H6466 (1), mix H6148 (1), plan H5186 (1), render H7999 (1), vow H5088 (1). The term-cluster cannot type these.
- **T2(Supplementary) candidate, code still null — 5 meanings / 5 instances**: freely H5071 (Psa 110:3·270518), freewill-offering H5071 (Psa 54:6·280007), make H6213 (Psa 115:8·270908), practice H6213 (Psa 111:10·270577), swore H7650 (Psa 132:2·272959). T2 = supplementary/reference — not standalone inner-being types.
- **Real M-cluster — 13 meanings / 14 instances**: M37 Calling (chosen H0977 ×2 + rather H0977 ×1 = 3), M29 Desire (frame ×1), M10 Sin (injustice ×1), M14 Deceit (malicious intent ×1), M15 Wisdom (plan H2803, plan H3289, planned H2803, plans H6250, purposed H2161 = 5), M17 Counsel (plans H5475, purposes H6098 = 2), M45 Transformation (render H7725 ×1).

**21 of 35 instances (60%) cannot be cluster-typed** (null or T2). The term-cluster layer is largely silent for this family.

---

## 1. Coherence — does the label fit its data?

**No. The keyword grouping `will-resolve-vow-intent` fuses at least four distinct inner-being movements, plus lemma-gloss strays.** The fusion mechanism is English-keyword / gloss homography (plan/purpose/intent/devise; frame; make/practice; chosen; render), not one interior motion. This is a first-class finding.

**Movement A — Vow bound and discharged to God (the coherent core; ~16 instances).**
Making, swearing, and above all *paying* what was pledged. Corrected locus almost all `external:god`.
- vow/swear: Psa 76:11·282790 · D101 "vows (neder)"; Psa 132:2·272961 · D101 "vow (nadar)"; Psa 132:2·272959 · D101 "swear (shaba)"; Psa 22:25·275708 · D101 "perform my vows before the fearers."
- perform/pay/render (all shalam H7999): Psa 61:8·280907; Psa 65:1·281170; Psa 76:11·282793; Psa 66:13·306497; Psa 116:14·270937; Psa 116:18·270955; Psa 56:12·280246. Plus render (shuv H7725) Psa 116:12·307631.
- freewill devotion (nedabah H5071): Psa 110:3·270518 · D101 "offer freely"; Psa 54:6·280007 · D101 "freewill offering."
This block genuinely answers "will/resolve/vow" — the self binding itself to God and proving devotion by fulfilment.

**Movement B — Deliberate choosing/preferring (M37 Calling; ~3-4 instances).**
Psa 119:173·271679 & Psa 119:30·271777 · D101 "choose (bachar)"; Psa 84:10·284043 · D101 "would rather (bachar)". Borderline: Psa 16:5·274724 · D101 "the LORD my chosen portion" is the **noun** (menath, "portion"), D102(type)=affect, `internal:ib-state` — God-as-inheritance, not the verb *choose*. Fused by the English word "chosen."

**Movement C — Resolve to integrity (1 instance).**
Psa 17:3·274843 · D101 "tested heart, purposed not to sin" · D102(type)=volition · M15 — the settled inner resolve ("I have purposed that my mouth will not transgress"). The purest "will-resolve" datum in the file.

**Movement D — The wicked's scheming / malicious intent (~10 instances; opposite valence and bearer).**
Grouped with the label under "intent/plan/purpose/devise," but this is the *dark* counterpart — enemies calculating harm, not the devout will:
- Psa 58:2·280477 "devise (paal)"; Psa 139:20·308088 "malicious intent (mezimmah)" M14; Psa 140:2·273608 "plan evil in the heart" M15; Psa 21:11·275489 "devise doomed evil"; Psa 62:4·280953 "plan/take counsel (yaats)" M15; Psa 140:4·273632 "planned to trip the feet" M15; Psa 83:3·283995 "plans (sod)" M17; Psa 106:43·269773 "purposes (etsah), rebellious" M17; Psa 64:6·281138 "injustice (olah)" M10. Also Psa 146:4·274224 "plans perish at death" M15 (mortal man's designs — mortality-reckoning, distinct again).
D102(type) here is mostly `cognition`, not `volition`.

**Strays fused by lemma/gloss homography (no fit to will/vow/intent):**
- Psa 103:14·269094 · D101 "frame (yetser)" · D102=state · M29 — bodily *constitution* ("he knows our frame... we are dust"), not intention.
- Psa 106:35·307474 · D101 "mix (arab)" — assimilation to the nations.
- Psa 115:8·270908 · D101 "make (asah)" — idol-making.
- Psa 111:10·270577 · D101 "practice (asah)" — practising the fear of the LORD.
- Psa 55:22·280143 · D101 "cast your burden on the LORD (shalak)" — trust/entrusting; and Psa 2:3·305964 · D101 "cast off the cords (shalak)" · D102=volition — rebellion. Two opposite senses of one verb.

**Diagnostic corroboration:** (i) D102 type is scattered across action/cognition/volition/disposition/status/affect/state/faculty — a coherent "will" family would skew to volition; only 3 instances are typed volition (Psa 2:3·305964, Psa 17:3·274843, Psa 22:25·275708). (ii) Corrected D116 locus splits ~17 `external:god` (Movements A/B) vs ~18 `internal:ib-state` (Movements C/D + strays). (iii) Bearer splits the devout self (psalmist/David/worshippers/God-fearing/people) from the ungodly (rebels/wicked/rulers/enemies/idolaters/fathers) — see §3.

---

## 2. sense (D101) / type (D102) — what the words are
All D101 values are read-phrases keyed to the verse; all D102 present. Type spread:
- **action (17)**: perform/pay/render (shalam) ×7, cast-burden Psa 55:22·280143, vows H5087 ×2 (282790, 272961... 272961 is action), make 270908, mix 307474, plan H3289 280953, plans H5475 283995, practice 270577, render H7725 307631, swore 272959, devise 280477. (See per-instance JSON.)
- **cognition (5)**: malicious intent 308088, plan H2803 273608, plan H5186 275489, planned 273632, plans H6250 274224.
- **volition (3)**: cast-cords Psa 2:3·305964, purposed Psa 17:3·274843, perform-vows Psa 22:25·275708.
- **disposition (2)**: freely 270518, rather 284043.
- **status (2)**: freewill-offering 280007, injustice 281138.
- **affect (1)**: chosen-portion 274724. **state (1)**: frame 269094. **faculty (1)**: purposes etsah 269773.

## 3. bearer (D105) — whose inner being (all `inferred`, all human)
No God-attribute intrudes (IB-screen passes). The bearer cleanly sorts the two valences:
- **Devout self**: "the psalmist" (280907, 271679, 271777, 306497 "individual", 270937, 270955, 274724, 269...  , 280246, 307631, 275708, 284043), "David" (272961, 272959), "the worshippers" (281170, 282793, 282790), "the God-fearing" (270577), "the people" (270518), "the believer (self-exhortation)" (280143).
- **The ungodly / generic mortal**: "the rebels" (305964), "the wicked" (281138, 308088, 273608, 273632), "the enemies" (275489, 280953, 283995), "the unjust rulers" (280477), "the idolaters" (270908), "the fathers" (307474, 269773), "man / mortal man" (269094, 274224).

## 4. source (D103) / operation (D106) / target (D107) / manner (D108) / coupling(D112) / locus(D116)
- **D106 operation** filled on all 35 (`item_type:"event"`); it restates the verse-motion (e.g. Psa 116:12·307631 "render/repay"; Psa 140:4·273632 "a specific ambush is premeditated").
- **D103 source** only Psa 55:22·280143 (see §0.4).
- **D107 target** filled everywhere but genuine (`pair`) only at 280907→280908, 281170→281169, 282793→282790, 280143→280144, 280477→280478, 280246→280247; the rest are inferred self-loops.
- **D108 manner / D104 seat**: mostly "none" (§0.3).
- **Corrected D112 coupling** (the phrase) ties the vow-block to praise/thanksgiving (Psa 61:8·280907 "singing praises"; Psa 65:1·281170 "praise due to God"; Psa 54:6·280007 "giving thanks to God's name") and ties Psa 76:11's vow⇄perform pair; ties the scheming-block to the wrong devised (Psa 58:2·280477 "the wrongs devised"; Psa 64:6·281138 "their diligent scheming").
- **Corrected D116 locus**: `external:god` for the vow/offer/choose-toward-God data; `internal:ib-state` for the scheming/frame/resolve-within data (counts in §1 diagnostic ii).

## 5. The interior network (genuine pair edges only)
**One intra-family edge**: Psa 76:11 · 282790(vow) ⇄ 282793(perform) — reciprocal on D107(target)/D108(manner)/D112(coupling): the pledge and its discharge bound in one line. This is the only place two family members link.

Every other genuine `pair` edge exits the family — target/coupling/source/manner links to neighbour spans (280908, 280904, 281169, 281165, 280148, 280144, 280151, 280478, 280476, 280009, 281141, 280956, 280247) that are **not** masters in this file. The inner-being network *within* the family is therefore a single point-to-point link; the family does not internally interlock. All other structure is either self-loop (not a link) or a reach into verse context outside scope.

## 6. Interior anatomy the data actually names
Only the filled seats/sources/couplings, corrected:
- **The one named seat**: the heart, as the workshop of devised wrong — Psa 58:2·280477 · D104="the heart", D108="in the heart" (echoed thematically, though unfilled as seat, at Psa 140:2·273608 "plan evil in the heart" and Psa 64:6·281138 "the inward mind and heart of a man are deep").
- **The one named source**: God's sustaining, as the ground of casting one's burden — Psa 55:22·280143·D103="and he will sustain you."
- **The devotional axis** (corrected loci `external:god`): vow/oath → perform/pay/render → freewill/thank offering, coupled to praise and thanksgiving.
- **The scheming axis** (corrected loci `internal:ib-state`): devise/plan/purpose/malicious-intent, coupled to the wrong contrived and (once) seated in the heart.

## 7. What could not be derived from this source
- **No intensity, specifier, effect, or prohibition anywhere** (D109/D110/D111/D113 absent — §0.4): the source cannot say how strong, how qualified, to what effect, or whether prohibited.
- **Seat is essentially unavailable** — 34/35 "none"; the interior *location* of vow, choice, resolve, and (most) scheming is unstated (§0.3).
- **Bearer is never explicit** — every one inferred (§0.4); the source does not textually fix whose IB.
- **Source (what moves it) is derivable once only** (§0.4).
- **The family does not cohere as one movement** (§1) — meaning at the family level cannot be derived; it must be read per-movement. Any "will-resolve-vow-intent" synthesis over all 35 would be an artefact of keyword grouping.
- **60% of instances are cluster-untyped** (null/T2, §0.5): the term-cluster layer cannot corroborate the interior read for most of the family.
- **The network cannot support a web reading** (§5): one intra-family edge only; relational meaning beyond Psa 76:11 is not derivable within scope.
- **Two homograph noun/verb collisions** flagged, not resolved: "chosen" as portion (274724) vs. choose (271679/271777/284043); "render" as shalam-pay (280246) vs. shuv-repay (307631). D116 swap corrected for 11 instances but not otherwise repaired in-source.

## 8. Summary
`will-resolve-vow-intent` is **not one inner-being movement** but a keyword fusion of: (A) a coherent *vow-bound-and-paid-to-God* core (~16, `external:god`, coupled to praise/thanks), (B) *deliberate choosing of God* (M37, ~3-4), (C) a single *resolve-to-integrity* (Psa 17:3), and (D) the *wicked's scheming/malicious intent* (~10, `internal:ib-state`, mostly cognition) — plus lemma/gloss strays (frame=constitution, mix, make idols, practise, cast). Data-integrity: 11/35 carry the D112/D116 swap (corrected here); D109/D110/D111/D113 absent throughout; D103 once, seat once (Psa 58:2 "the heart"), manner 7×; every bearer inferred; 60% cluster-null/T2; and the internal network is a single edge (Psa 76:11 vow⇄perform). Meaning is derivable per-movement, not for the family as named.
