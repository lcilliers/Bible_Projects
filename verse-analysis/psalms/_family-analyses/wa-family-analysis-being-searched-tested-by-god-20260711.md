# In-depth analysis — base source `psalms__being-searched-tested-by-god`

> **Source:** `verse-analysis/psalms/_base-sources/psalms__being-searched-tested-by-god.json` (7 meanings, 14 instances, 13 passages). **Method:** worked **only** from the source file. Every finding is back-trackable to `reference · span_id · Dn(dimension)`. Where the data does not support a reading, or a field is unusable, it is **flagged, not filled**. Discovery notes (D14) are the original reader's own read, carried in the source, and are cited as such. Filed 2026-07-11.

---

## 0. Data-integrity screen (what is usable, done first)
Before reading meaning, the source must be screened for what it can and cannot bear:

- **`seat` (D104) = "none" on 9 of 14 instances.** Where in the interior the act happens is *unstated* for most. Only three name a seat: **the eye** (Psa 54:7 span 280020; Psa 59:10 span 280535, D104), **the spirit / ruach** (Psa 77:6 span 282978, D104, item_type `pair`→282977), and — implicitly, via coupling only — **the heart** (Psa 78:18 span 283050, D112 "paired with the heart and the craving").
- **`manner` (D108) = "none" on all 6 testing/proof instances** and several others. The *how* of testing God is not specified beyond the operation.
- **D112/D116 (coupling/locus) are TRANSPOSED on 4 instances** — the known field-swap. On these, D116 "locus" holds a coupling-phrase and D112 "coupling" holds the `external:god` locus code: **Psa 106:14 (269613), Psa 95:9 test (285517), Psa 95:9 proof (285518), Psa 107:24 (269939).** They are read **corrected** below (locus = `external:god`; coupling = the phrase). The other 10 are correctly ordered.
- **"Inferred-flag" edges are self-loops, not network links.** Every `bearer`/`target` edge with `item_type:"flag"` and `resolution:"inferred"` has `to_span` = the span's *own* id (e.g. 269613→269613). These are **not** relational edges and are excluded from the network reading. **Only `pair` edges (resolution `span`) linking to a *different* span are genuine** (see §5).
- **Cluster is NULL on 8 of 14 instances** — every `raah` look/see/saw (T2 Supplementary) plus `search` and `test`(H6884). The term-cluster layer cannot type them; only the 6 `nasah`/`bachan` testing acts carry a cluster (M35 Testing). This is itself evidence (see §1).

---

## 1. HEADLINE FINDING — the family label does not match its data
The file is named *being-searched-tested-**by-god***, implying the inner being as the **object** of divine examination. **The data shows the reverse: in 12 of 14 instances the human is the acting subject.** The keyword grouping ("test / search / see / prove / proof") has swept together **three unrelated inner-being movements**:

| movement | instances | subject → object | cluster |
|---|--:|---|---|
| **A. the human tests GOD** (nasah/bachan) | 6 | human → God | M35 Testing |
| **B. the human SEES** (raah) | 6 | human → enemies / God / deeds | none (T2) |
| **C. the human self-searches / invites God's test** | 2 | human → self (God as examiner) | none |

**Not one instance is "God searches the passive human."** The nearest, Psa 26:2 (span 276139), is the human's *active invitation* (D102 = **volition**, the only volitional record). Support: the cluster-NULL split (§0) independently confirms the divide — the M35-Testing terms are all movement A; the perception verbs (raah) are all T2. This corroborates the family-vs-cluster comparison, where this family's expected twin (M35) covered only its testing half.

**This is the first thing the base source teaches: the grouping is a lexical artefact, and the real inner workings live in the three movements, not the label.**

---

## 2. MOVEMENT A — the human tests God: presumption born of appetite, hardening into rebellion
Six acts (5× `nasah` "test", 1× `bachan` "proof"), all **D102 = action**, all bearer = the wilderness generation ("they" / "the fathers", D105, inferred), all target = **God** (D107), locus `external:god` (D116, corrected where swapped).

**The source names appetite as the origin.** Testing God is repeatedly *coupled to craving*:
- Psa 106:14 (269613): D116-corrected coupling "**paired with the craving**"; D114 "the presumptuous trying of God **born of appetite**."
- Psa 78:18 (283050): D112 "paired with **the heart and the craving**"; D114 "tested God **in their heart** by demanding the food they craved." — the one place the **heart** is named as the interior seat of this testing.

**It compounds into habit and rebellion** — traceable across the four Ps 78/95 instances by their operations and couplings:
- Psa 78:41 (283213): D106 operation = "**test again and again**"; D112 "paired with **provoking** the Holy One"; D114 "testing turned **habitual**."
- Psa 78:56 (283323): D112 "paired with **rebelling and not keeping**"; D114 "testing renewed even in the promised land."
- Psa 95:9 test (285517) + proof (285518): D114 "put me to the proof, **though they had seen my work**" — the testing persists *against evidence already seen*.

**Inner working (A):** appetite/craving (seated in the heart, 78:18) → issues in the presumptuous testing of God → repeated until habitual (78:41) → bound to rebellion and covenant-breaking (78:56) → and it does so *in defiance of what has been seen* (95:9). The movement is a hardening: desire → presumption → habit → rebellion. Every link is on the page (D106 operations + D112 couplings + D114 notes); none is imported.

---

## 3. MOVEMENT B — the human sees (raah): the eye as faculty of vindication, contemplation, and witness
Six acts of `raah`, seat = **the eye** where named (54:7, 59:10, D104). Three sub-modes, each grounded:

**(i) The vindicated gaze — God-granted, not self-taken.** Psa 54:7 (280020) + 59:10 (280535): D106 "look in triumph"; D108 manner "in triumph / vindication". Critically the source makes it **God's gift, not gloating**:
- 54:7 D103 source = "**because God put an end to the enemies**" (`pair`→280004); D112 coupling "**the fruit of God's deliverance**" (`pair`→280015); D114 "not gloating cruelty but the settled assurance of God's justice done."
- 59:10 D112 coupling "**granted by the God who meets him in love**" (`pair`→280532); D108 "by God's grant."

**(ii) Contemplation that answers desire.** Psa 63:2 (281041): D106 "look upon / gaze"; D107 target = **God, his power and glory** (`pair`→281044); D112 coupling "**the vision that answers the thirst**" (`pair`→281016 — the thirst span); D114 "the vision the longing soul feeds on even in the wilderness." Here seeing is the interior's *satisfaction of longing* — a direct edge from sight to thirst.

**(iii) Witness of God's deeds.** Psa 66:5 (281350): D103 source "for God is awesome in his deeds" (`pair`→281353); D112 "paralleled by the summons to **come and hear**" (`pair`→281284). Psa 107:24 (269939): the sailors "saw the deeds of the LORD" (D114).

**(iv) The dark inverse — presuming *not* to be seen.** Psa 64:5 (281135) is the only `raah` typed **D102 = status**: D106 "**presume none can see**"; bearer "the wicked (presuming)"; locus `internal:ib-state`; D114 "the presumption that their scheming is unobserved... **not reckoning that God sees and searches the deepest heart**." This single instance is the *only* one that touches the family's nominal theme (being-seen by God) — and it does so as the wicked's **denial** of it.

**Inner working (B):** the eye is the interior's organ of relation to what is beyond it — beholding enemies (vindication, always God-enabled: 54:7/59:10), beholding God (contemplation feeding thirst: 63:2), beholding God's works (witness: 66:5/107:24) — and its corruption is the will to be unseen (64:5).

---

## 4. MOVEMENT C — self-search and invited test: the interior turned on itself
Two acts, both locus `internal:ib-state`, and these are the file's true "interior under examination":

- **Self-searching (Psa 77:6, span 282978, `chaphas`):** D104 seat = "**the spirit (ruach)**" (`pair`→282977); D106 "search / examine thoroughly"; D107 target = "**the questions of v7-9**" (`pair`→282980); D108 "diligent, thorough"; D114 "the deep self-searching, the mind ransacking itself: has God forever spurned...?" The spirit is the *organ*, and its object is the self's own anxious questions — introspection that **issues in** the lament-questions.
- **Invited test (Psa 26:2, span 276139, `H6884`):** the only **D102 = volition**. D106 "the self invites God to prove, try and test its heart and mind — **a confidence willing to be assayed**"; D107 "confident-self-submission"; D114 "only an integrity sure of itself asks to be tested." The examiner here **is** God — but the movement is the human's *offering* of the inmost self.

**Inner working (C):** the interior can turn on itself either in **anxiety** (77:6 — the ruach ransacking, born of distress) or in **confident submission** (26:2 — integrity inviting the assay). Same reflexive shape, opposite affective root.

---

## 5. THE NETWORK (genuine `pair` edges only)
Excluding self-loops (§0), the real relational links the source encodes:

| from | dimension | to span | meaning of the link |
|---|---|---|---|
| 280020 (Psa 54:7 look) | D103 source | 280004 | the looking flows *from* God ending the enemies |
| 280020 | D112 coupling | 280015 | coupled to God's deliverance |
| 281041 (Psa 63:2 look) | D107 target | 281044 | the gaze *lands on* God's power/glory |
| 281041 | D112 coupling | 281016 | the vision *answers* the thirst-span |
| 281135 (Psa 64:5 see) | D112 coupling | 281107 | presumption *behind* the secret snares |
| 281350 (Psa 66:5 see) | D103 source / D112 | 281353 / 281284 | grounded in God's deeds; paralleled to "come and hear" |
| 282978 (Psa 77:6 search) | D104 seat / D107 / D112 | 282977 / 282980 | the **spirit** performs it; targets the questions |

**Observation:** the network is **sparse and one-directional** — every genuine edge is a `raah`/`chaphas` instance (movements B and C). The six testing acts of movement A carry **no genuine pair edges at all** (only self-loops), so movement A is, in this data, relationally *flat* — its couplings were recorded as inferred flags, not linked spans. That is a coverage fact about the read, not a claim about the theology.

---

## 6. THE INTERIOR ANATOMY THE DATA ACTUALLY NAMES
Assembled strictly from filled D104/D103/D112 values:
- **Seats named:** the **heart** (78:18, via coupling), the **spirit/ruach** (77:6), the **eye** (54:7, 59:10). Everything else: seat unstated.
- **Source named:** **craving/appetite** (106:14, 78:18) for the testing; **God's prior act** (54:7 "God put an end to the enemies"; 66:5 "God is awesome in his deeds") for the seeing.
- **Affective poles:** presumption (A, 64:5) vs. confident submission (26:2) vs. anxious introspection (77:6) vs. satisfied contemplation (63:2).

---

## 7. WHAT COULD NOT BE DERIVED (explicit)
- **The seat of "testing God"** — 5 of 6 testing acts have D104 = none; only 78:18 implies the heart. The interior organ of presumption is largely **unlocated** in this data.
- **Manner of testing** — D108 = none on all 6; the *how* is unread.
- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113)** — **absent on all 14 instances** (not in the ledger). No data on how strong, what constrains, or what results — these aspects of the inner working are simply not captured here.
- **The 4 swapped instances (§0)** — their locus/coupling were only recoverable by reading D112/D116 transposed; taken at face value they would mislead. Flagged, not trusted.
- **Movement A's relational context** — no genuine edges (§5); its couplings are unlinked.

---

## 8. SUMMARY
Read honestly and only from the source, this base source is **not** a portrait of the inner being under God's search. It is three movements the lexicon fused: **(A)** the appetite-driven testing *of* God that hardens into rebellion (6×, the only clustered, relationally-flat set); **(B)** the seeing eye — vindication always God-granted, contemplation that feeds thirst, witness of God's deeds, and its inversion in the wicked's will-to-be-unseen (6×, where the real network lives); and **(C)** the interior turned on itself in anxious self-search or confident invited-test (2×, the true "interior examined"). The seats the data will name are **heart, spirit, eye**; the source it will name is **craving** (for A) and **God's prior act** (for B). Everything about intensity, effect, constraint, and the seat/manner of testing is **unread** and must not be invented.

*Every claim above cites reference · span_id · dimension in the source file; nothing is imported from outside it.*
