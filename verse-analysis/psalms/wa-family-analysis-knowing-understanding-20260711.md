# Family analysis — `knowing-understanding` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__knowing-understanding.json` (only). Scope: `meta.scope.family = knowing-understanding`. Counts declared: **43 meanings · 99 instances · 73 passages**. Every claim cites `reference · span_id · Dnnn(label)` into that file. Nothing outside the file is used. British spelling.

Dimension legend used below: D101 sense · D102 type · D103 source · D104 seat · D105 bearer · D106 operation · D107 target · D108 manner · D109 intensity · D110 specifier · D111 effect · D112 coupling · D113 prohibition · D114 discovery · D115 role · D116 locus.

---

## 0. Data-integrity screen (done first)

**Dimension coverage across the 99 instances** (count of instances carrying a value):

| Dim | Present | Note |
|---|---|---|
| D101 sense | 99 | full |
| D102 type | 99 | full |
| D103 source | **2** | near-absent (only Psa 46:10 · 279031, Psa 67:2 · 306501) |
| D104 seat | 99 slots, but 96 = `none` | see below |
| D105 bearer | 99 | full |
| D106 operation | 99 (5 = `none`) | full |
| D107 target | 99 (11 = `none`) | full |
| D108 manner | 99 slots, but 87 = `none` | see below |
| D109 intensity | **0** | absent from every instance |
| D110 specifier | **0** | absent from every instance |
| D111 effect | **0** | absent from every instance |
| D112 coupling | 99 | full (but see swap) |
| D113 prohibition | **1** | only Psa 49:20 · 279373 · D113(prohibition) = "absent ('without UNDERSTANDING')" |
| D114 discovery | 99 | full — treated as source (reader's read) |
| D115 role | 99 | uniform (see below) |
| D116 locus | 99 | full (but see swap) |

**Absent dimensions (all 99):** D109 intensity, D110 specifier, D111 effect are never populated. D103 source (2/99) and D113 prohibition (1/99) are effectively unavailable. Any statement about how *strongly* the interior knows, about specifiers, about the effect knowing produces, or about what grounds it, is **not derivable from this source** for 97–99% of instances.

**D104 seat = `none` in 96/99.** Only three seats are named, all "heart": Psa 49:3 · 279380 · D104(seat) "the heart (lebab)"; Psa 66:18 · 281302 · D104(seat) "the heart"; Psa 77:6 · 282974 · D104(seat) "heart (its musing)". The interior *organ* of knowing is essentially unlocated in this family.

**D108 manner = `none` in 87/99.** Twelve carry a manner, e.g. Psa 46:10 · 279031 · D108 "be still / cease striving"; Psa 74:9 · 282690 · D108 "no signs, no prophet"; Psa 77:6 · 282974 · D108 "in the watches of the night"; Psa 63:6 · 281073 · D108 "in the watches of the night"-type nocturnal framing; Psa 55:13 · 280066 · D108 "a man his equal, his companion"; Psa 73:16 · 282394 · D108 "a wearisome task, until the sanctuary".

**D112 (coupling) / D116 (locus) field-swap — 19 instances transposed.** Correct order = D116 holds an `internal:`/`external:` code, D112 holds a phrase. In these 19, D112 holds the code and D116 the phrase; read corrected. Swapped instances:

- Psa 101:4 · 268841 (internal:ib-state) · Psa 91:14 · 285089 (external:god) · Psa 92:6 · 285229 (internal:ib-state) · Psa 89:15 · 307040 (external:god) · Psa 100:3 · 307174 (external:god) · Psa 109:27 · 307576 (external:god) · Psa 135:5 · 307888 (external:god) · Psa 92:6 · 285232 (internal:ib-state) · Psa 94:8 · 285428 (internal:ib-state) · Psa 105:1 · 269368 (external:person) · Psa 89:1 · 284531 (external:person) · Psa 95:10 · 285459 (external:god) · Psa 107:43 · 270040 (external:god) · Psa 106:7 · 269842 (internal:ib-state) · Psa 101:2 · 268814 (internal:ib-state) · Psa 94:11 · 285314 (internal:ib-state) · Psa 104:34 · 269331 (external:god) · Psa 101:3 · 268826 (internal:ib-state) · Psa 111:10 · 270579 (internal:ib-state).

**Corrected D116 locus distribution (all 99):** internal:ib-state **57**, external:god **38**, external:person **3**, internal:heart **1**. Knowing sits predominantly as an interior state, but ~41% is oriented externally, almost always toward God.

**Self-loop "edges" are not network links.** Of **311** edge entries, **269** are self-loops (`item_type` = flag or event, `resolution:"inferred"`, `to_span` = the span's own id) — non-links, discarded. Only **42** genuine `pair` edges (`resolution:"span"`, to a different span) are real. See §"The network".

**Cluster NULL / T2.** No instance carries `T2`. **Six** instances have `cluster.code = null` (the term-cluster cannot type them): Psa 39:5 · 278104 (breath) · Psa 144:4 · 308122 (breath) · Psa 66:18 · 281302 (cherished) · Psa 4:4 · 279450 (ponder) · Psa 78:7 · 306764 (set) · Psa 139:4 · 273499 (word). **Ten** further instances are flagged `is_outlier=true` — genuine non-Wisdom crossovers (listed in §1).

**D115 role uniform.** All 99 = `characteristic` (no qualifier, no standalone). The whole family is typed as characteristic-bearing.

**Bearer screen (D105):** every bearer is human or a human group — psalmist (51), David (4), enemies, nations, worshippers, judges, the fool, the wicked, the next generation, etc. **No instance has God as bearer**, so the human-IB requirement holds throughout.

---

## 1. Coherence — does the label fit its data?

**Partly.** The core is coherent; the keyword grouping has fused in three foreign movements plus mis-swept marginal terms. Cluster split of the 43 meanings: **M15 Wisdom** carries the large majority (all the yada / bin / sakal / chashab knowing-and-considering senses); the remainder scatter.

**(A) Coherent centre — cognition/knowing (M15 Wisdom).** yada `know/known/knowledge/consider/regard/familiar-friend/ignorant` (H3045, 28+6+3+1+1+1+1 spans), bin `understanding/consider/discern/mark/can-discern` (H0995), sakal `consider/ponder/understand/more-understanding/skillful` (H7919, H8394), chashab `consider/count/regard/think/thought` (H2803), plus nouns da'ath H1847, tushiyyah/tebunah H7922/H8394, rea H7454. This is one movement: the interior grasping, reckoning, and settling into knowledge — e.g. Psa 20:6 · 275438 · D106(operation) "the moment confidence solidifies into knowledge"; Psa 140:12 · 273591 · D114 "the interior resolves from plea into confidence; the outcome is already owned."

**(B) Fused movement 1 — meditation / musing.** siach `meditate/meditation` (H7878 ×10, H7879, H7881), hagah `meditates/ponder` (H1897), higgayon (H1900). This is a distinct devotional operation (sustained inward dwelling on God's works/word), and the data itself flags the seam: hagah is typed **M42 Speech** (vocalised musing) at Psa 1:2 · 275359, Psa 63:6 · 281073, Psa 77:12 · 282884; and H7879 meditation is typed **M03 Grief** (musing-as-complaint) at Psa 104:34 · 269331. Meditation overlaps knowing but is not identical to it — it is process, not grasp: Psa 77:12 · 282884 · D106 "meditate / muse".

**(C) Fused movement 2 — thought-content / reckoning (nouns).** machashabah `thoughts` (H4284, typed **M14 Deceit** at Psa 56:5 · 280295, Psa 94:11 · 285314), H8312 `thoughts` (typed **M01 Fear** at Psa 139:23 · 273489), rea `thoughts` (H7454). These are the *contents/plans* of the mind, not the act of knowing — a different node (mental furniture vs cognitive act).

**(D) Mis-swept marginal terms (keyword artefacts).** Grouped by ESV gloss overlap ("consider/think/regard/set/mark"), not by cognition:
- hevel `breath` (H1892, null cluster) Psa 39:5 · 278104, Psa 144:4 · 308122 — **transience/vanity**, not cognition at all.
- millah `word` (H4405, null) Psa 139:4 · 273499 — **speech**, God's knowledge *of* the word.
- amar `ponder` (H0559, null) Psa 4:4 · 279450 — "say in the heart".
- shith / sum `set` (H7896 M15 / H7760 null) Psa 78:7 · 306764 — "set the heart/hope".
- ra'ah `cherished` (H7200, null) Psa 66:18 · 281302 — regard/look.
- yaqar `precious` (H3365, **M29 Desire**) Psa 139:17 · 273440 — valuing, not knowing.
- shamar `Mark` (H8104, **M30 Obedience**) Psa 37:37 · 277795.
- zakar `think` (H2142, **M41 Remembrance**) Psa 119:52 · 271906.

**Verdict (first-class finding):** the family label names a real, dominant movement (**cognition/knowing = M15 Wisdom**, the bulk of the 99), but the grouping is keyword-driven and fuses **four distinct nodes** — knowing (A), meditating (B), thought-content (C), and a residue of non-cognitive terms swept in by shared ESV glosses (D). The 10 outlier crossovers (M42/M14/M03/M01/M29/M30/M41) and 6 null-cluster spans mark exactly these seams.

---

## 2. The movements/operations evidenced (cited)

**2.1 Knowing as arrival at settled assurance (dominant sub-arc of A).** Repeatedly the operation is confidence crystallising into knowledge, locus external:god:
- Psa 20:6 · 275438 · D106 "a settled assurance arrives — now I know the LORD saves his anointed"; D101(sense) "'now I know the LORD saves'".
- Psa 140:12 · 273591 · D114 "the interior resolves from plea into confidence; the outcome is already owned."
- Psa 56:9 · 280331 · D101 "this I know, that God is for me"; coupling (D112, corrected) "the assurance that grounds the calling".
- Psa 41:11 · 278410 · D114 "by this I know you delight in me … assurance read from the outcome."
- Psa 135:5 · 307888 (swap-corrected external:god) · "I know that the LORD is great."

**2.2 Knowing sought / petitioned (volition-tinged, D102 volition = 3).** The interior asks to be *made* to know:
- Psa 143:8 · 273937 · D114 "the interior wants direction … to be taught where to step"; D107(target) "guidance-seeking".
- Psa 39:4 · 278083 · D106 "a request to grasp its own mortality"; D107 "mortality-awareness".
- Psa 25:4 · 306186 · D101 "make me know your ways".
- Psa 119:125 · 271370 · D114 "the knowing sought through understanding" (bin→yada chain within one verse).

**2.3 Meditation / musing as sustained process (B).** D106 "meditate / muse" (10×). Nocturnal, work-directed dwelling:
- Psa 63:6 · 281073 · D108(manner) nocturnal framing; typed M42 Speech.
- Psa 77:6 · 282974 · D104(seat) "heart (its musing)" — one of only three named seats; D108 "a diligent search of the spirit".
- Psa 1:2 · 275359 · meditates on the law "day and night" (M42 Speech crossover).
- Psa 104:34 · 269331 · meditation typed M03 Grief (musing shading to lament).

**2.4 Failure / absence of knowing (negation as a movement).** yada negated (D101 "know (yada, negated)", 4×) and D113 prohibition (1×):
- Psa 92:6 · 285229 & 285232 · D106 "fail to know" / "the failure to understand" (the two co-verse spans cross-couple, see network).
- Psa 82:5 · 283913 / 283915 · D106 "know nothing" — "they neither know nor understand."
- Psa 49:20 · 279373 · **D113(prohibition)** "absent ('without UNDERSTANDING')" — the sole prohibition datum: man in pomp *without* understanding.
- Psa 94:8 · 285428 · D106 (call to the "stupid"/"fools" to gain sense).

**2.5 Making-known (outward transfer, D101 "make known").** Psa 105:1 · 269368 (swap-corrected external:person) "make known his deeds among the peoples"; Psa 78:3–7 · 306760/306764 the fathers→children transmission of what is known (Psa 78:6 · 283351).

**2.6 Deliberate not-knowing / refusal.** Psa 101:4 · 268841 · D114 "the deliberate ignorance of wickedness, refusing intimacy with evil"; coupling "the evil refused" — knowing as moral withholding.

**Type profile (D102) across all 99:** action 40, cognition 17, disposition 15, status 13, faculty 6, volition 3, affect 3, state 1, speech 1. Knowing in Psalms is read predominantly as an **act** (40) and secondarily as **cognition/disposition/status**, only rarely as a standing **faculty** (6) — the family is motion far more than organ.

---

## 3. The network (genuine `pair` edges only)

**42 genuine edges across 23 instances.** By dimension: **D112 coupling 24**, D107 target 9, D108 manner 3, D104 seat 3, D103 source 2, D105 bearer 1. **Of the 42, only 5 link within this family's own span set; 37 point to co-verse spans outside the family** — i.e. the network of "knowing" is overwhelmingly *outward*, binding the knowing-span to non-cognitive material in the same verse, not to other knowing-spans. The internal network is therefore **sparse**.

Representative edges:
- Psa 51:3 · 279731 → 279732 · D107(target) and → 279733 · D112(coupling) — "I know my transgressions" bound to sin "ever before me".
- Psa 59:13 · 280563 → 280566 · D107 and → 280553 · D112 — knowing bound to "the goal of the judgment on the proud."
- Psa 46:10 · 279031 → 279035 · **D103(source)** "grounded in God's exaltation over the nations" — one of only two source edges; "be still and know."
- Psa 67:2 · 306501 → 281397 · **D103(source)** "the purpose of God's gracious blessing" + → 306500 · D107 + → 306504 · D112 — the richest single node (source+target+coupling).
- Psa 77:6 · 282974 → 282976 · D104(seat) + → 282978 · D108(manner) + → 282977 · D112 — the musing-in-the-night node, its seat and manner both relational.
- Psa 66:18 · 281302 → 281304 · D104(seat) + → 281303 · D107 + → 281304 · D108 + → 281307 · D112 — "if I had cherished iniquity in my heart."
- Psa 73:16→17 · 282394↔282404 reciprocal D112 coupling — "when I thought … until I went into the sanctuary" (the one near-bidirectional link, both within-family).
- Psa 50:22 · 279567 → 279570 · **D105(bearer)** + D112 — the sole bearer-edge; addressed to "you who forget God."

`direction` is null on all 42 edges, so **edge directionality is not derivable**; only the from→to span and dimension are.

---

## 4. The interior anatomy the data actually names

Assembling only filled fields:

- **Seat (D104):** essentially unnamed — 96/99 `none`. The interior's knowing is *placeless* in this source. Where named, it is the **heart** (lebab): Psa 49:3 · 279380, Psa 66:18 · 281302, Psa 77:6 · 282974 (the heart as the organ of musing).
- **Locus (D116, corrected):** internal:ib-state 57, external:god 38, external:person 3, internal:heart 1 — a state of the inner being, but with a strong Godward orientation.
- **Source (D103):** only two — God's self-exaltation (Psa 46:10 · 279031) and the purpose of God's blessing (Psa 67:2 · 306501). What *causes* knowing is otherwise unstated.
- **Operation (D106):** the verbs the interior performs — meditate/muse (10), know (8), come-to-know (5), fail-to-know (3), make-known (2), consider/discern (2), have-understanding (2), plus one-off assurance-crystallising phrases (§2.1).
- **Target (D107):** where knowing points — **God's word / precepts / statutes / promise (16 combined)**, God himself (several), assurance, one's own mortality (Psa 39:4), God's ways (Psa 25:4). Knowing in Psalms is overwhelmingly *of God and God's word*.
- **Manner (D108):** stillness (Psa 46:10), the night-watches (Psa 63:6, 77:6), diligent search of the spirit (Psa 77:6), a wearisome task until the sanctuary (Psa 73:16).
- **Coupling (D112, corrected phrases):** knowing is bound to moral and covenantal matter — "the evil refused" (Psa 101:4), "sin ever before him" (Psa 51:3), "the assurance that grounds the calling" (Psa 56:9), "the goal of the judgment on the proud" (Psa 59:13), and repeatedly "paired within its char-arc across the psalm" (the Psa 119 acrostic instances).

---

## 5. What could not be derived (flagged)

1. **Intensity (D109), specifier (D110), effect (D111): 0/99.** No datum on how strongly the interior knows, on any specifier, or on what knowing *produces*. Entirely unread from this source.
2. **Source (D103): 2/99; prohibition (D113): 1/99.** Causation and prohibition of knowing are effectively unavailable.
3. **Seat (D104): 96/99 `none`.** The organ of knowing is unlocated except for three "heart" spans.
4. **Manner (D108): 87/99 `none`.** How the knowing is carried out is unread for the great majority.
5. **Edge directionality: null on all 42 genuine edges.** Direction of the network links is not derivable; and the internal (within-family) network is only 5 edges — the family barely links to itself.
6. **The D112/D116 swap (19 instances, §0)** had to be corrected by inference from field content; the raw file is internally inconsistent on these two dimensions.
7. **6 null-cluster + 10 outlier spans** cannot be typed to the family's own cluster (M15 Wisdom); several (breath/hevel, word/millah, precious/yaqar) are not cognition at all and are present only as keyword artefacts (§1D).

---

## Summary

`knowing-understanding` (Psalms) = **43 meanings / 99 instances / 73 passages**, all human-borne, all typed `characteristic`. Its coherent centre is **cognition/knowing (M15 Wisdom)** — read overwhelmingly as an *act* that arrives at settled, Godward assurance and is targeted at God and God's word — but the keyword grouping fuses in three further nodes (**meditation/musing**, self-flagged as M42 Speech / M03 Grief; **thought-content nouns**, M14/M01; and a residue of **non-cognitive mis-swept terms** — breath/transience, word/speech, precious/valuing). The interior anatomy is thin: **seat unnamed in 96/99, manner in 87/99, and intensity/specifier/effect wholly absent**; the network is sparse (only 42 real edges, just 5 within-family, no directions) after discarding 269 self-loops; and 19 instances required a D112/D116 swap correction.
