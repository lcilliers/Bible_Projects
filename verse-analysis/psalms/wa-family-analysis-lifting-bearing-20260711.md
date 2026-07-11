# Family analysis (in isolation) — Psalms family `lifting-bearing`

> Source: `outputs/data/psalms-family-base-sources/psalms__lifting-bearing.json` only. Scope strictly this one file. Method: `verse-analysis/psalms/_family-analysis-method-20260711.md`.
> Counts (meta): **7 meanings · 21 instances · 17 passages.** All genre `poetic/wisdom`. Every claim cited `reference · span_id · Dnnn(label)`.

The 21 masters:

| # | ref | span | meaning (char_key) | lemma | cluster | D101 sense | D102 type |
|---|-----|------|--------------------|-------|---------|-----------|-----------|
| 1 | Psa 116:13 | 270931 | lift up | H5375 | M19 Trust | lift up (nasa) | action |
| 2 | Psa 119:48 | 271872 | lift up | H5375 | M19 Trust | lift up (nasa) | action |
| 3 | Psa 121:1 | 272330 | lift up | H5375 | M19 Trust | lift up the eyes | action |
| 4 | Psa 134:2 | 273040 | lift up | H5375 | M19 Trust | lift up the hands | action |
| 5 | Psa 143:8 | 273942 | lift up | H5375 | M19 Trust | lift up the soul | affect |
| 6 | Psa 24:4 | 275894 | lift up | H5375 | M19 Trust | soul not lifted to falsehood | volition |
| 7 | Psa 25:1 | 275947 | lift up | H5375 | M19 Trust | lift up my soul to you | affect |
| 8 | Psa 63:4 | 281058 | lift up | H5375 | M19 Trust | lift up (the hands) | action |
| 9 | Psa 86:4 | 284349 | lift up | H5375 | M19 Trust | lift up (nasa) | action |
| 10 | Psa 123:1 | 307798 | lift up | H5375 | M19 Trust | lift up the eyes | action |
| 11 | Psa 126:6 | 272588 | bear | H5375 | M19 Trust | bear (nasa) | action |
| 12 | Psa 126:6 | 272594 | bear | H5375 | M19 Trust | bring (nasa) | action |
| 13 | Psa 55:12 | 280052 | bear | H5375 | M19 Trust | bear / endure | action |
| 14 | Psa 89:50 | 284838 | bear | H5375 | M19 Trust | bear (nasa) | action |
| 15 | Psa 110:7 | 270560 | lift up | H7311 | M08 Pride \| T2 | lift up (rum) | state |
| 16 | Psa 75:4 | 282722 | lift up | H7311 | M08 Pride \| T2 | lift up / exalt (rum, forbidden) | action |
| 17 | Psa 55:20 | 280130 | violated | H2490 | null (T2) | profane / violate (chalal) | action |
| 18 | Psa 89:31 | 284680 | violated | H2490 | null (T2) | violate (chalal) | action |
| 19 | Psa 131:1 | 272859 | lifted up | H1361 | M08 Pride | lifted up (gabah, negated) | disposition |
| 20 | Psa 131:1 | 272862 | raised | H7311 | M08 Pride \| T2 | raise the eyes (rum, negated) | action |
| 21 | Psa 89:15 | 307041 | shout | H8643 | null (null) | festal shout (teruah) | action |

---

## 0. Data-integrity screen

### 0.1 D112(coupling)/D116(locus) field-swap
Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. **11 of 21 instances are transposed** (D112 holds the code, D116 holds a prose phrase). Read corrected:

**SWAPPED (11)** — read `locus` from D112, `coupling` from D116:
- Psa 116:13 · 270931 (D112 `external:god`, D116 "calling on God's name")
- Psa 121:1 · 272330 (`external:god` / "help that comes from the LORD")
- Psa 134:2 · 273040 (`external:god` / "blessing the LORD")
- Psa 123:1 · 307798 (`external:god` / "servant's upward look for mercy")
- Psa 126:6 · 272588 (`internal:ib-state` / "bringing sheaves home")
- Psa 126:6 · 272594 (`internal:ib-state` / "bearing the seed out")
- Psa 89:50 · 284838 (`internal:ib-state` / "servants' being mocked")
- Psa 110:7 · 270560 (`external:god` / "drinking from the brook")
- Psa 131:1 · 272859 (`internal:ib-state` / "the unproud heart")
- Psa 131:1 · 272862 (`internal:ib-state` / "not occupying with great things")
- Psa 89:15 · 307041 (`external:god` / "knowing and walking in the light")

**CORRECT order (10)** — D116 already a code: 119:48·271872 (`external:god`), 143:8·273942 (`internal:ib-state`), 24:4·275894 (`internal`), 25:1·275947 (`internal`), 63:4·281058 (`external:god`), 86:4·284349 (`external:god`), 55:12·280052 (`internal`), 75:4·282722 (`internal`), 55:20·280130 (`internal`), 89:31·284680 (`external:god`).

**Corrected locus tally:** `internal:ib-state` = 11 · `external:god` = 10. The interior self-offering / pride / bearing movements read internal; the gesture-toward-God and covenant-toward-God movements read external.

### 0.2 Self-loop "edges" are not real links
Every instance carries "edges" on D105/D107/D112 that are `item_type:flag`, `resolution:inferred`, `from_span:null`, `to_span:<own id>` — **self-loops, not network links.** Discard all of these.

**Genuine `pair` edges (`resolution:span`, to a different span) — only 7, on 4 spans:**
- Psa 63:4 · 281058 · D112(coupling) → span 281054 ("gesture of the lifelong blessing")
- Psa 55:12 · 280052 · D107(target) → span 280051 ("an enemy's taunt"); D112(coupling) → span 280057 ("hiding from an open adversary")
- Psa 75:4 · 282722 · D107(target) → span 282723 ("the horn"); D112(coupling) → span 282729 ("haughty neck", v5)
- Psa 55:20 · 280130 · D107(target) → span 280132 ("his covenant"); D112(coupling) → span 280126 ("hand stretched against friends")

**Every genuine to_span (281054, 280051, 280057, 282723, 282729, 280132, 280126) lies OUTSIDE this file's 21 masters.** No family member links to another family member. The inner-being network *among lifting-bearing instances is empty* (see §7).

### 0.3 seat(D104)=none / manner(D108)=none
- **Seat unfilled in 20 of 21.** The sole filled seat is Psa 63:4 · 281058 · D104 "the hands" (inferred). Soul/heart/eyes appear in the verse text and D101/D106/D114 but are never coded into D104.
- **Manner unfilled in 19 of 21.** Filled: Psa 63:4 · 281058 · D108 "in God's name"; Psa 75:4 · 282722 · D108 "on high, with haughty neck".

### 0.4 Absent dimensions (across all 21)
**D103 source, D109 intensity, D110 specifier, D111 effect, D113 prohibition are absent from every instance.** Present dims are only 101,102,104,105,106,107,108,112,114,115,116. Note the **D103(source) gap**: nothing codes what moves the operation. Note the **D113(prohibition) gap**: Psa 75:4·282722, Psa 24:4·275894, Psa 131:1·272859/272862 are grammatical negations/prohibitions in the text, but this is carried only in the D101 sense wording, never in D113.

### 0.5 Cluster NULL / T2
- **Fully NULL:** Psa 89:15 · 307041 (H8643 shout) — cluster.code, name, all_candidates all null.
- **NULL code, T2 candidate:** Psa 55:20 · 280130 and Psa 89:31 · 284680 (H2490 violated) — code null, all_candidates `T2(Supplementary)`.
- **M08 code but T2 in candidates:** Psa 110:7·270560, Psa 75:4·282722, Psa 131:1·272862 (H7311) — `M08(Pride) | T2(Supplementary)`.
- **3 instances are untypeable by the term-cluster** (307041 fully null; 280130, 284680 null-coded). All 7 meanings carry `is_outlier:false` — so the M08/T2/null crossovers are *not* flagged as outliers even though M08 Pride and T2 are non-adjacent to the family's M19 Trust core (see §1).

---

## 1. Coherence — does the label fit its data?

**The label "lifting-bearing" is a lexical grouping that fuses at least five distinct inner-being movements.** It coheres only around the surface act of raising/carrying; the underlying IB motions diverge and, in two cases, are unrelated.

- **A. Upward self-offering to God (coherent core) — 10.** H5375 nasa "lift up the soul/eyes/hands/cup" toward God: trust, dependence, worship. (spans 270931, 271872, 272330, 273040, 273942, 275894, 275947, 281058, 284349, 307798; all M19 Trust.)
- **B. Bearing / enduring / carrying a burden — 4.** Same lemma H5375, but the *opposite vector*: a load carried, not a self raised — seed borne in grief (126:6·272588), sheaves brought in joy (126:6·272594), a taunt endured (55:12·280052), reproach carried in the heart (89:50·284838). One lemma, two contrary movements; the family label conflates them.
- **C. Pride / self-exaltation — 4.** H7311 rum + H1361 gabah "lift up the horn/head", "raise the eyes", "heart lifted" (110:7·270560, 75:4·282722, 131:1·272859, 131:1·272862; M08 Pride). Distinct movement; mostly *forbidden or negated* (only 110:7 is a positive, God-given exaltation of the king).
- **D. Covenant profanation — 2 — MIS-GROUPED.** H2490 chalal "violate/profane" the covenant (55:20·280130) and God's statutes (89:31·284680). This is neither lifting nor bearing; a different lemma with no raise/carry semantics, swept in (null cluster / T2). Flag as a grouping error.
- **E. Festal shout — 1 — marginal.** H8643 teruah "festal shout" (89:15·307041), the only *nominal* instance (morph `HNcfsa`, empty stem, null cluster). A raised voice, related to "lifting" only by loose analogy.

**First-class finding:** the family name is honest for A+B (the nasa "lift/bear" verb, one Strong's H5375, 14 instances) but the keyword net has pulled in the *pride* verbs (rum/gabah, C) as a genuinely distinct movement and two non-lifting intruders (chalal profanation D, teruah shout E). Movements A and B are themselves antithetical (upward reach vs downward load) under one lemma.

---

## 2. Movement A — Upward self-offering / trust (H5375 nasa, M19)

The dominant movement (10). The self, or an organ of it, is raised toward God as an act of dependence, devotion or thanks.

- **The whole soul offered up.** "To you, O LORD, I lift up my soul" (Psa 25:1 · 275947 · D101 "lift up my soul to you", D102 **affect**); "to you I lift up my soul" (Psa 143:8 · 273942 · D101 "lift up the soul", D102 **affect**, D106 "the whole soul is lifted toward God — the self offered upward as the ground of the plea"); "for to you… do I lift up my soul" (Psa 86:4 · 284349 · D106 "lift up the soul"). D114 reads these as raising "the entire interior toward God" (275947), "an oblation of trust" (273942).
- **The soul withheld from falsehood** (the negated form). Psa 24:4 · 275894 · D101 "the soul not lifted to falsehood", D102 **volition**, D106 "the self refuses to devote itself to an idol or a lie" (D114) — devotion guarded, the same lift refused toward emptiness.
- **The eyes raised.** Psa 121:1 · 272330 · D106 "lift up the eyes" ("seeking gaze of the pilgrim… to God for help", D114); Psa 123:1 · 307798 · D106 "lift up the eyes" ("upward look of dependence… to the enthroned God", D114).
- **The hands raised.** Psa 63:4 · 281058 · D106 "lift up (the hands in worship)", the **only seat-filled** instance (D104 "the hands") and manner-filled (D108 "in God's name") — "the outward act of a heart lifted to God, worship enacted with the whole self" (D114); Psa 119:48 · 271872 · "lifted hands of devotion toward the loved commandments" (D114); Psa 134:2 · 273040 · D106 "lift up the hands" toward the sanctuary, "the body enacting the blessing" (D114, bearer "the servants").
- **The cup raised.** Psa 116:13 · 270931 · D107 "the cup of salvation" — "the thankful gesture, raising the cup in acknowledgement of God's rescue" (D114); an external object but the movement is thanksgiving. Passage anchor (1813).

Type-depth tracks interiority: the soul-instances are coded **affect/volition** (273942, 275947, 275894); the body-gesture instances (hands/eyes/cup) are **action**. The interior self is the thing raised in the first; the body enacts in the second.

## 3. Movement B — Bearing / enduring / carrying (H5375 nasa, M19)

Four instances invert the vector — a burden borne rather than a self raised.

- **Seed and sheaves.** Psa 126:6 · 272588 · D101 "bear (nasa)", D106 "carry the seed out", D107 "in grief" — "the burdened going-out, carrying the precious seed to be given up to the ground" (D114); its pair Psa 126:6 · 272594 · D101 "bring (nasa)", D106 "carry the sheaves home", D107 "in joy" — "the joyful return-burden, the same arms that carried seed in tears now full of sheaves" (D114). A grief→joy arc within one verse — but linked only by the (swapped) D116 phrases, **not** by a genuine edge (§7).
- **Enduring a taunt.** Psa 55:12 · 280052 · D101 "bear / endure", D106 "bear / endure (hypothetically)" — "the endurance that open enmity allows… a strength that the betrayal of a friend dissolves" (D114). Genuine edges: D107→280051 (the enemy's taunt), D112→280057 (hiding from an adversary).
- **Carrying reproach inwardly.** Psa 89:50 · 284838 · D101 "bear (nasa)", D107 "the insults of the nations in the heart" — "the inward carrying of reproach, humiliation lodged in the heart" (D114). The verse names the heart as the site of the load, though D104 seat is still coded none.

## 4. Movement C — Pride / self-exaltation (H7311 rum, H1361 gabah, M08)

A distinct movement: the interior lifted *itself* — mostly forbidden or renounced.

- **Forbidden horn.** Psa 75:4 · 282722 · D101 "lift up / exalt (rum — do not lift up your horn)", D106 "lift up the horn (forbidden self-exaltation)", D108 "on high, with haughty neck" — "the arrogant self-exaltation God forbids… for lifting up is God's to give (v7)" (D114). Bearer "the wicked". Genuine edges D107→282723 (the horn), D112→282729 (haughty neck). Passage anchor (1709).
- **Renounced pride** (Psa 131:1, two instances, both passage anchors). D101 "lifted up (gabah, negated)" · 272859 · D102 **disposition**, D106 "not exalt the heart" — "the pride deliberately negated, the heart kept from rising" (D114); D101 "raise the eyes (rum, negated)" · 272862 · D106 "not raise the eyes too high" — "the gaze kept from reaching above its station" (D114).
- **God-given exaltation.** Psa 110:7 · 270560 · D101 "lift up (rum)", D102 **state**, D106 "lift up his head" — "the king's triumphant exaltation… after God has shattered his foes" (D114). Bearer "the king"; the one non-negated pride-lift, and it is conferred, not self-taken.

## 5. Movement D — Covenant profanation (H2490 chalal, null/T2) — mis-grouped

- Psa 55:20 · 280130 · D101 "profane / violate (chalal — he violated his covenant)", D106 "profane / break" — "the sacred bond profaned… trust desecrated" (D114). Genuine edges D107→280132 (his covenant), D112→280126 (hand against friends).
- Psa 89:31 · 284680 · D101 "violate (chalal)", D107 "God's statutes" — "the profaning of God's ordinances by the sons" (D114). Bearer "David's children".

No lift/bear semantics; included by grouping error (see §1.D). Retained here only to account for all data.

## 6. Movement E — Festal shout (H8643 teruah, null) — marginal

Psa 89:15 · 307041 · D101 "festal shout (teruah)", D106 "raise the festal shout" — "the joyful acclamation of God as king, worship as jubilant cry" (D114). Bearer "the people". The only nominal, null-cluster instance; belongs by loose analogy of "raising" a voice.

---

## The network (genuine pair edges only)

Seven genuine `pair` edges on four spans (§0.2), **all pointing to co-text spans outside the 21 masters**:
- 281058 →281054 · Psa 63:4 · D112 (the lifelong blessing the raised hands enact)
- 280052 →280051 · Psa 55:12 · D107 (the taunt endured) · and →280057 · D112 (hiding from an adversary)
- 282722 →282723 · Psa 75:4 · D107 (the horn) · and →282729 · D112 (haughty neck)
- 280130 →280132 · Psa 55:20 · D107 (the covenant) · and →280126 · D112 (hand against friends)

**Findings:** (a) the network is *sparse* — only 4 of 21 instances carry any real edge; (b) it is *entirely outward* — every target is a co-text span, never another lifting-bearing member; (c) it is *one-directional* (from_span = the family member, direction null); (d) even the obvious same-verse pairs — 126:6 (272588/272594) and 131:1 (272859/272862) — carry **no** genuine edge and are joined only by the swapped-D116 prose. **There is no inner-being network internal to this family in the edge data.**

## The interior anatomy the data actually names

Assembling only *filled* fields:
- **Seat (D104):** "the hands" — once only (Psa 63:4 · 281058). No heart/soul/spirit/eye is ever coded as a seat.
- **Corrected locus (D116):** the movements split evenly — `internal:ib-state` (self-offering of soul, bearing, pride, negations) vs `external:god` (hands/eyes/voice toward God, covenant toward God).
- **Operation (D106):** the verbs of motion — raising (soul/eyes/hands/cup/head/horn), carrying (seed/sheaves/reproach), enduring, and their negations. This is where the family's real content sits.
- **Type-depth (D102):** the interior organ raised is **affect/volition/disposition** (soul: 273942, 275947, 275894; heart: 272859); the body enacting or object lifted is **action**; the king's conferred lift is **state**. Interiority correlates with type, not with seat (which is blank).
- **Interior organs named in text but NOT in the seat field:** soul/nephesh (25:1, 143:8, 86:4, 24:4), heart (89:50, 131:1), eyes (121:1, 123:1, 131:1) — recoverable from D101/D106/D114 only.
- **Bearers (D105, all inferred):** the psalmist (majority), the worshipper (24:4), the servants (134:2), the sower (126:6), the king (110:7), the wicked (75:4), the betrayer (55:20), David's children (89:31), the people (89:15). All human IB (no God-as-bearer). Movements C–E carry the non-introspective bearers (wicked, betrayer, king, corporate people/children).

## What could not be derived

- **D103 source** — absent in all 21. What *moves* each lift/bear (God, desire, spirit) is never coded.
- **D109 intensity · D110 specifier · D111 effect · D113 prohibition** — absent in all 21. In particular the four negations/prohibitions (75:4·282722, 24:4·275894, 131:1·272859, 131:1·272862) are not captured in D113; the negation survives only in D101 wording.
- **D104 seat** — 20/21 blank; interior organs uncoded.
- **D108 manner** — 19/21 blank.
- **Cluster typing** — 307041 (shout) fully null; 280130, 284680 (violate) null-coded/T2; the term-cluster cannot type these 3.
- **is_outlier** — all `false`, so the M08-Pride / T2 / null crossovers into the M19-Trust family are unflagged despite being non-adjacent (a gap between the label's data and its own outlier field).
- **Edge contents** — the 7 genuine targets (281054, 280051, 280057, 282723, 282729, 280132, 280126) are outside this file; their spans cannot be read here, only their D107/D112 gloss phrases.

## Summary

`lifting-bearing` is a lexical net, not one inner-being movement. Its honest core is H5375 nasa (14): **A. upward self-offering to God** (10 — soul/eyes/hands/cup raised in trust, coded affect/volition where the soul itself is raised) and its inverse **B. bearing/enduring a burden** (4). The net then fuses a genuinely distinct **C. pride / self-exaltation** (4, rum/gabah, mostly forbidden or renounced) and two intruders — **D. covenant profanation** (2, chalal — not lifting at all) and **E. festal shout** (1, teruah). Integrity: **11/21 have the D112/D116 code-phrase swapped** (corrected here); **all "edges" but 7 are self-loops**, and those 7 point outside the family so **no intra-family network exists**; **seat blank 20/21, manner blank 19/21**; **D103/D109/D110/D111/D113 absent throughout**; 3 instances untypeable by cluster; no crossover flagged as outlier. The interior anatomy the data actually names is thin: one seat ("the hands"), a clean internal/external locus split, and the operation verbs — with soul, heart and eyes present in the text but never coded as seats.
