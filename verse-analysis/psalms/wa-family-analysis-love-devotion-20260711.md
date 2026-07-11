# Family analysis — `love-devotion` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__love-devotion.json` only. Scope `meta.scope.family = "love-devotion"`; 8 meanings, 35 instances, 28 passages; genre = poetic/wisdom throughout. Every claim cites `reference · span_id · Dnnn(label)`. Nothing here is drawn from outside this file.

## Roster (meaning → lemma → cluster → instances)

| # | char_key | gloss | lemma | cluster.code / all_candidates | inst |
|---|---|---|---|---|---|
| 1 | H0157:love | love (aheb, vb) | H0157 | M05(Love) | 23 |
| 2 | H1692:cling | clings (dabaq) | H1692 | **null / null** | 3 |
| 3 | H0157:lov | loved (aheb, vb) | H0157 | M05(Love) | 3 |
| 4 | H0160:love | love (ahabah, noun) | H0160 | M05(Love) | 2 |
| 5 | H3039:belovedon | beloved ones (yadid) | H3039 | **null / T2(Supplementary)** | 1 |
| 6 | H0157:friend | friends (aheb ptcp) | H0157 | M05(Love) | 1 |
| 7 | H7355:love | love (racham) | H7355 | M05(Love) | 1 |
| 8 | H2836:love | love/cling (chashaq) | H2836 | **null / M28(Envy) \| M44(Relational)** | 1 |

Total 35. 30 typed `M05(Love)`; 5 not typed to Love (rows 2, 5, 8).

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap
Seven instances are transposed — D116 "locus" carries a prose phrase while D112 "coupling" carries an `internal:`/`external:` code. Read them corrected (D112 ← the phrase, D116 ← the code):

| span_id | reference | D112 as-stored | D116 as-stored | corrected D116 |
|---|---|---|---|---|
| 270920 | Psa 116:1 | `external:god` | "paired with God hearing his pleas" | external:god |
| 272422 | Psa 122:6 | `internal:ib-state` | "paired with praying for its peace" | internal:ib-state |
| 285629 | Psa 97:10 | `external:god` | "paired with hating evil" | external:god |
| 270203 | Psa 109:17 | `internal:ib-state` | "paired with cursing / no delight in blessing" | internal:ib-state |
| 270320 | Psa 109:4 | `internal:ib-state` | "paired with the accusation returned for it" | internal:ib-state |
| 270332 | Psa 109:5 | `internal:ib-state` | "paired with the hatred returned" | internal:ib-state |
| 285085 | Psa 91:14 | `external:god` | "paired with knowing God's name" | external:god |

All seven read coherently once corrected (love coupled to a partner-act — God hearing, hating evil, knowing his name — and located external/internal sensibly). The remaining 28 instances are in correct order (D112 = phrase/hyphen-label, D116 = code), e.g. `Psa 119:97 · span 272210 · D112(coupling)="paired with the whole LOVE-arc of the psalm"` / `D116(locus)="external:god"`.

### 0.2 Self-loop "edges" are not real links
Across the file, almost every instance's `edges[]` for D105 bearer, D107 target, D112 coupling are `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = **the span's own id** (e.g. `Psa 116:1 · span 270920 · D105 bearer → to_span 270920`). These are self-loops, **not** network edges — discard for the network.

Genuine `pair`/`event` edges (`resolution:"span"`, to a **different** span):
- `Psa 52:3 · span 279812` → D107 target 279813, D108 manner 279815, D112 coupling 279816
- `Psa 52:4 · span 279821` → D112 coupling **279812** (the only master→master intra-family link — the two Ps 52 tyrant-love spans)
- `Psa 69:36 · span 281856` → D103 source 306609, D107 target 281857
- `Psa 70:4 · span 282022` → D107 target 282023, D108 manner 282027, D112 coupling 282027
- `Psa 45:7 · span 278985` → D107 target 278986, D112 coupling 278987
- `Psa 63:8 · span 302642` → D104 seat 302641, D105 bearer 302641, D112 coupling 302646
- `Psa 60:5 · span 280823` → D103 source 280825, D106 operation 280824, D112 coupling 280818

**Every to_span except 279812 lies outside this file's master set** — they are sibling words in the same verse, not other love-devotion masters, so they cannot be resolved within file scope. The one genuine intra-family edge is `279821 → 279812` (Psa 52:4 ↔ 52:3).

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in 34 of 35** instances. The single filled seat is `Psa 63:8 · span 302642 · D104 seat = "the soul"` (a `pair`, to 302641).
- **D108 manner = "none" in 29 of 35**. Filled in 6: `Psa 52:3 · 279812` ("more than good"), `Psa 52:4 · 279821` ("words that devour"), `Psa 69:36 · 281856` ("dwelling in restored Zion"), `Psa 70:4 · 282022` ("saying evermore, God is great"), `Psa 63:8 · 302642` ("held fast by God's upholding right hand"), `Psa 60:5 · 280823` ("by God's right hand").

### 0.4 Absent dimensions
Across all 35 instances there is **no** D109 intensity, **no** D110 specifier, **no** D111 effect, **no** D113 prohibition. D103 source appears only twice (`Psa 69:36 · 281856`; `Psa 60:5 · 280823`). D115 role = "characteristic" in all 35 (never qualifier/standalone).

### 0.5 Cluster NULL / T2
Five instances cannot be typed by their term-cluster:
- `Psa 119:25 · 271747`, `Psa 119:31 · 271782`, `Psa 63:8 · 302642` — H1692 cling, cluster **null/null**.
- `Psa 60:5 · 280823` — H3039 beloved, cluster null, `all_candidates = T2(Supplementary)` (a reference/qualifier term, not a standalone Love characteristic).
- `Psa 91:14 · 285085` — H2836 chashaq, cluster null, `all_candidates = M28(Envy) | M44(Relational)` — neither candidate is Love; the type is unresolved.

---

## 1. Coherence — does the label fit the data?

**Partially.** The keyword grouping "love-devotion" fuses at least five distinct inner-being movements. The dominant, coherent core is genuine devotional love toward God; the rest are grouping artefacts of the shared verb/root.

**(a) Devotional love toward God, his law, name, house — the true core (~24 instances).** aheb law-love saturates Ps 119 (`119:97 · 272210`, `119:47 · 271871`, `119:113 · 271297`, `119:127 · 307758`, `119:140 · 271466`, `119:159 · 271577`, `119:163 · 271610`, `119:165 · 271619`, `119:167 · 271631`, `119:48 · 271876`, `119:119 · 271333`, `119:132 · 271411`); love of God/name/salvation (`116:1 · 270920`, `5:11 · 280677`, `70:4 · 282022`, `69:36 · 281856`, `97:10 · 285629`, `31:23 · 276798`, `145:20 · 274129`, `122:6 · 272422`); love of God's house (`26:8 · 276177`); racham tender-love opening a deliverance-song (`Psa 18:1 · 274912 · D114 "warm attachment (racham, womb-love)…affection"`); chashaq clinging-devotion (`Psa 91:14 · 285085`); dabaq cleaving to God (`Psa 119:31 · 271782`, `Psa 63:8 · 302642 · D114 "the soul's total attachment to God"`). This block coherently earns "love-devotion".

**(b) Disordered / inverted love — opposite valence, same verb (5 instances).** `Psa 4:2 · 279433 · D101="men love vanity, seek lies"` (D114 "disordered affection…fastened on emptiness"); `Psa 52:3 · 279812 · D114 "perverted affection…loves inverted"`; `Psa 52:4 · 279821 · D101="love all devouring words"`; `Psa 109:17 · 270203 · D101="loved (aheb)"` (loved to curse). This is love-as-faculty **misdirected** — the antithesis of devotion, captured only because the lemma is shared.

**(c) Human-to-human love repaid with enmity (2 instances).** `Psa 109:4 · 270320 · D101="love (ahabah)"` (D114 "goodwill met with accusation"); `Psa 109:5 · 270332` ("hatred for my love"). God-ward devotion is not in view; the movement is relational love betrayed.

**(d) Being loved *by* God — passive status, not the subject's own love-movement (1).** `Psa 60:5 · 280823 · D102 type="status"`, `D101="beloved ones (yadid)"` (D114 "named as God's beloved…they appeal…to being loved"). The bearer is human but the operation is `be delivered (by God)` — belovedness received, not love exercised.

**(e) Abandonment / isolation — a semantic-opposite catch (1).** `Psa 38:11 · 277883 · D101="my friends stand aloof"`, `D107 target="abandonment"`, `D114 "the wound of being deserted"`. The Hebrew is aheb-participle ("friends/lovers") but the movement read is desertion — the family label is inverted here by keyword.

**Verdict:** the label fits block (a) and, loosely, the God-clinging of (b–e's aheb roots), but (b) disordered love, (c) betrayed human love, (d) passive belovedness, and (e) abandonment are distinct movements the grouping has fused. This is a first-class finding: "love-devotion" is a lemma-cluster, not a single inner-being motion.

---

## 2. The movements/operations evidenced (cited)

### 2.1 Love of God's word (the Ps 119 arc)
Read as **disposition** (D102) in nearly every case, seatless, target "God's law/commandments/testimonies" (D107, inferred), coupling "the whole LOVE-arc of the psalm" (D112). Distinct discovery-reads differentiate the instances rather than collapsing them: love set against the divided heart (`119:113 · 271297 · D114`), love drawn by seeing God's justice (`119:119 · 271333 · D114`), love as the mark God favours (`119:132 · 271411`), love pleaded as ground for revival (`119:159 · 271577`), love above the finest gold (`119:127 · 307758`), love that meditates ceaselessly (`119:97 · 272210`), love of the *tested* promise (`119:140 · 271466`), love as source of unstumbling peace (`119:165 · 271619`), love intensified — "exceedingly" (`119:167 · 271631`). The data resists merging these (per the read-notes) even though sense/type/seat/target are near-identical.

### 2.2 Love of God himself / his name / his salvation / his house
`Psa 116:1 · 270920` love born of answered prayer (D114); `Psa 5:11 · 280677 · D114` joy "specifically from love of who God is (his name)"; `Psa 70:4 · 282022` love of God's salvation overflowing in praise (D108 manner="saying evermore, God is great", a genuine span-pair); `Psa 97:10 · 285629` love of God grounding the charge to "hate evil" (corrected D116 pairs love with hating evil); `Psa 26:8 · 276177 · D102 affect` "warm attachment to the very place of God's presence"; `Psa 18:1 · 274912 · D102 affect` racham opening the song "not with thanks but with affection".

### 2.3 Clinging / cleaving (dabaq, chashaq)
`Psa 63:8 · 302642` — the file's richest instance: **seat = "the soul"** (D104, the only named seat), operation "cling / cleave", D108 manner "held fast by God's upholding right hand", D112 coupling "met by God's right hand upholding him" — a mutual grip (D114). `Psa 119:31 · 271782 · D102 action` cling to the testimonies against shame. `Psa 91:14 · 285085` chashaq "hold fast in love" as the ground of deliverance. Counter-pole: `Psa 119:25 · 271747 · D102 state` "My soul CLINGS to the dust" — the same verb at the low estate, clinging downward, `target="none"`.

### 2.4 Disordered / inverted love
`Psa 4:2 · 279433 · D102 affect`, `Psa 52:3 · 279812 · D102 action` (target "evil (more than good)", manner "more than good", both span-pairs), `Psa 52:4 · 279821 · D102 action`, `Psa 109:17 · 270203`. Love as a faculty aimed at emptiness, evil, devouring speech, cursing — the interior fastened on the wrong object.

### 2.5 Betrayed love, belovedness, abandonment
`Psa 109:4-5 · 270320/270332` love returned as accusation and hatred; `Psa 60:5 · 280823` the people appealing to being God's beloved (yadid) under discipline; `Psa 45:7 · 278985 · D102 action` the king's "loved righteousness and hated wickedness" (target and coupling both span-pairs — the moral affection defining his heart); `Psa 38:11 · 277883` friends standing aloof — love's collapse into isolation.

---

## 3. The network

Effectively **no intra-family network**. 34/35 instances carry only self-loop flag-edges (§0.2), which are not links. The seven span-pair edge-sets (§0.2) point, with one exception, to non-master sibling spans outside this file — unresolvable in isolation. The **single genuine master-to-master edge** is `Psa 52:4 · 279821 · D112 coupling → 279812` (Psa 52:3): the tyrant's inverted love of evil (v3) and of devouring words (v4) are welded as "the same inverted love." So the only network the file supports is a two-node disordered-love pair inside Psalm 52 — the devotional core is a set of isolated, unlinked points.

---

## 4. The interior anatomy the data actually names

- **Seat:** named exactly once — `the soul` (`Psa 63:8 · 302642 · D104`). Everywhere else love is **seatless** (D104="none"): the data models love in Psalms as a disposition/affect with no located organ.
- **Type (D102):** disposition dominates (Ps 119 arc + `91:14`, `109:4/5`, `119:140`); affect for God-directed warmth (`18:1`, `26:8`, `5:11`, `145:20`, `4:2`); action for enacted/moral love (`52:3-4`, `45:7`, `69:36`, `70:4`, `119:31`); volition for the summons (`Psa 31:23 · 276798 · D102="volition"` — "LOVE the LORD, all his saints", the interior inviting the community); state for `119:25` and `38:11`; status for `60:5`.
- **Couplings the data binds love to** (corrected): God hearing pleas (`116:1`), exultation (`5:11`), hating evil (`97:10`), being kept/preserved (`145:20 · D112="love-and-be-kept"`), knowing God's name (`91:14`), the mutual grip of God's right hand (`63:8`), and — negatively — vanity (`4:2 · D112="love-vanity"`), lying speech (`52:3-4`), cursing (`109:17`).
- **Bearers** are all human IB (Screen 0 passed): the psalmist, the saints/pilgrims, "those who love", the king (`45:7`), the men (`4:2`), the tyrant (`52:3-4`), the enemy (`109:17`), the beloved people (`60:5`). God is consistently the **target/arena** (D107), never the bearer.

---

## 5. What could not be derived (from this source)

- **The seat of love:** 34/35 unstated — the interior location is not recoverable.
- **Intensity (D109):** absent everywhere, though the text plainly grades it — "love exceedingly" (`119:167 · 271631`), "above gold" (`119:127 · 307758`), racham/womb-love (`18:1 · 274912`). The gradient is in the read-notes (D114) but not coded as D109.
- **D110 specifier, D111 effect, D113 prohibition:** absent across all 35.
- **Manner:** unstated in 29/35.
- **Source (D103):** only 2 instances (`69:36`, `60:5`).
- **The network:** no genuine relational web among the masters beyond the single Ps 52 pair; the other span-pairs reference spans outside the file and cannot be followed here.
- **Cluster typing for 5 instances:** cling (null), beloved (T2), chashaq (M28|M44 unresolved) — the term-cluster does not fix them as Love.
- **Whether (b)–(e) belong here at all:** the file gives them the same `role="characteristic"` and family membership, but the read-notes show disordered love, betrayed love, belovedness and abandonment are distinct movements — a boundary the source asserts by keyword but its own D114 evidence undercuts.

---

## Summary
`love-devotion` = 8 meanings / 35 instances, all poetic, all `role=characteristic`. Its coherent core is seatless devotional love toward God and his law (the Ps 119 aheb arc + racham/dabaq/chashaq cleaving to God), but the keyword grouping fuses four further movements — inverted/disordered love (Ps 4, 52, 109:17), betrayed human love (Ps 109:4-5), passive belovedness (Ps 60:5, T2), and abandonment (Ps 38:11). The interior is almost entirely unlocated (one named seat: "the soul", Ps 63:8), intensity/specifier/effect/prohibition are wholly uncoded, and there is no real intra-family network beyond a single Ps 52 disordered-love pair (34/35 edges are self-loops). Seven instances carry a D112/D116 field-swap (listed §0.1); five instances are cluster-null/T2/ambiguous.
