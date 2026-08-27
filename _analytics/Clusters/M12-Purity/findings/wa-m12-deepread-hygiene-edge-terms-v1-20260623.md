# M12 (Purity) — DEEP-READ hygiene test of the FLAGGED / edge terms (Step 5)

- **File:** wa-m12-deepread-hygiene-edge-terms-v1-20260623.md · **v1 · 2026-06-23 · Author:** Claude Code.
- **What this is:** Step-5 deep-dive applied to the §G hygiene flags in `wa-m12-draft-units-from-lexical-read-v1-20260623.md`. It **TESTS** whether the flagged/edge terms belong in M12. **The read is the test** — no ownership fix, no reassignment, no DB write. Output = evidence + a flagged VERDICT/recommendation per term (markers: ⚠ HYGIENE · ❓ CLARIFY · ⚖ BORDER).
- **Inputs:** extract `Sessions-v2\M12-Purity\Data\wa-ve-lexical-extract-M12-20260623.json` (1,552 verses · 3,247 occ); object-kinds lens `wa-m10-section10-object-kinds-typology-provisional-v1-20260623.md`; draft-units §G.
- **Method:** per term, queried the extract (focus-cluster occurrences only), tabulated senses / valence / divine-involvement / stem / in-verse co-occurrence, and read sample verses.

---

## Headline verdicts

| Test | Term(s) | Verdict | Recommendation (flagged, NOT executed) |
|---|---|---|---|
| 1 | **na.tan H5414G "give" (1,065 focus occ)** | ⚠ HYGIENE — **noise; effectively 0 purity-relevant** | **Exclude entirely** from M12 purity units; flag ownership fix |
| 2 | tum.ah H2932 / miainō G3392 / anosios G0462 | ⚖ BORDER — **genuine M10c defilement vocabulary, owned here as the deliberate contrast pole** | **Keep as referenced contrast pole** (not a positive unit); primary home = M10c — confirm cross-ref vs ownership |
| 3 | enchriō/epichriō, morfoō, tsur, me.tom, mikh.lah, tikh.lah | mixed — see per-term | Mostly ⚠ **mis-grouped / not present**; recommend drop/re-home |

**na.tan headline (the question asked):** of 1,065 na.tan focus occurrences, **none carry a purity/consecration sense in the term itself.** It is literal "give/gave/given" throughout. 1,054 of 1,065 verses contain **no other M12 term at all** (pure noise). The 11 that share a verse with a real purity term still read na.tan as plain "give/given" — the consecration sense lives in the *co-term* (qa.dash, ta.hor), never in na.tan. **Purity-relevant na.tan ≈ 0.** Recommend exclude in full.

---

## Test 1 — na.tan H5414G "give" (1,065 occ): the NOISE test ⚠ HYGIENE

### Sense distribution (focus occurrences, n = 1,065)
Top senses are all literal transfer:

| sense | n | | sense | n |
|---|---|---|---|---|
| give | 297 | | grant | 11 |
| gave | 213 | | deliver | 8 |
| given | 182 | | granted | 8 |
| giving | 51 | | exchanged | 6 |
| gives | 39 | | (long tail: yield, bring, issue, send, bestow, trade, lend, hand over…) | — |
| Give (cap.) | 25 | | **offer / offered** | **3 + 3** |
| delivered | 16 | | **dedicated** | **1** |

The entire distribution is the semantic field of **giving/handing over/granting**. No "consecrate", no "sanctify", no "devote to the Lord" sense surfaces as the meaning of na.tan.

### Valence & divine-involvement (the purity signal is absent)
- **Valence:** none **970** · neutral 60 · righteous 21 · forbidden 11 · commanded 3. → 91 % carry *no* moral/cultic valence at all. A consecration term would be commanded/righteous-dominant; na.tan is valence-empty.
- **Divine involvement:** UNRESOLVED 665 · none 303 · agent 52 · giver 23 · object 20. → not a God-directed dedication signal.
- **Object_type:** thing/abstract 823 · person 92 — ordinary transfer objects, not "self / offering / firstfruits to YHWH".
- **Stem:** Qal 1,011 · Niphal 52 · Hophal 2 — the plain active "give"; no dedicatory stem pattern.

### Co-occurrence test (decisive)
- **1,054 / 1,065** na.tan focus verses contain **no other M12 focus term** → pure literal-give noise, exactly as §G predicted (truncation `--full` co-term recovery dragged na.tan in with home tagged M12).
- Only **11** na.tan verses also hold a real purity term. Reading all 11: na.tan is still plain "give/given" and the purity meaning is carried by the **co-term**, e.g.:
  - 1Ki 9:7 / 2Ch 7:20 — "the land that I have **given** … and this house I have **consecrated** (qa.dash)" — give = land transfer; consecrate is the separate term.
  - Lev 10:14 — breast/thigh "**given** as a due … eat in a **clean** (ta.hor) place" — give = portion allotment.
  - Eze 20:12 — "I **gave** them my Sabbaths … that they might know I **sanctify** (qa.dash) them" — give = bestow; sanctify is the co-term.
  - Psa 84:11 — "the Lord **bestows** favor" alongside ta.mim "blameless" — unrelated.

### Even keyword-baited "offer/dedicate/devote" hits are not na.tan-as-consecration
Filtering na.tan for any cause/object/sense containing dedicat/offer/devote/consecrate/vow/tithe/sacrifice/firstfruit returned **17** occurrences — and **every one** is literal give where the keyword sits in the *surrounding verse* or the *object*, not in na.tan's meaning:
- Deu 26:12 "**giving** [it] to the Levite" (tithe distribution — give); Lev 23:10 "**give** … of the harvest"; Deu 14:21 "**give** it to the sojourner".
- 1Sa 21:6 the priest "**gave** him the holy bread" (give; "holy" is the bread).
- 2Ki 23:11 "horses the kings had **dedicated** to the **sun**" — the lone "dedicated" sense, and it is **pagan idolatry**, not M12 consecration.
- Psa 51:16 "I would **give** [a sacrifice]"; Ecc 5:1 "to **offer** the sacrifice of fools" — give/offer of an object, term still = give.

**VERDICT ⚠ HYGIENE:** na.tan is literal "give/gave/given" noise. **Purity/consecration-relevant occurrences ≈ 0** (no na.tan occurrence means "consecrate/dedicate to the Lord"; the single "dedicated" is idolatrous). It does not denote, evidence, or modify any purity object.

**RECOMMENDATION (flagged, NOT executed):** **Exclude na.tan H5414G entirely from M12 purity units** — it is not an M12 object and bloats the fan-out (1,065 of 3,247 occ ≈ 33 %). Flag for an ownership fix (its M12 tag is a truncation-recovery artefact). No small "dedicate-sense subset" is worth keeping — the would-be subset is empty. Where na.tan genuinely co-narrates a consecration (the 11 co-verses), the purity meaning is already captured by the co-term, so dropping na.tan loses nothing.

---

## Test 2 — Negation pole: tum.ah H2932 + miainō G3392 + anosios G0462: the CONTRAST-pole test ⚖ BORDER

### Senses, valence, type
| term | n | senses | valence | type | faculty |
|---|---|---|---|---|---|
| **tum.ah** (uncleanness) | 28 | uncleanness 20 / uncleannesses 4 / unclean 3 / "nothing unclean" 1 | **sinful 16** · forbidden 4 · neutral 7 | status (28/28) | none |
| **miainō** (to stain) | 4 | defiled 3 / defile 1 | **sinful 3** · neutral 1 | action | none |
| **anosios** (unholy) | 2 | unholy 2 | **sinful 2** | quality | **moral_evaluation** |

All three are **defilement/unholiness vocabulary** — negative valence-dominant, no positive purity meaning. They are the precise lexical inverse of the M12 positive units (U1 ritual cleanness, U2 inner purity, U3 holiness). In the §10 object-kinds lens these are **CONDITION/STATE (defilement-states, M10 anchors #29–31)** plus, for anosios, an **IDENTITY** edge (moral_evaluation verdict).

### Are they owned as the deliberate contrast, or mis-owned?
The in-verse co-occurrence test shows they function as the **explicit contrast pole**: **10 / 34** negation-pole verses pair the term directly with a positive purity term in the same verse:
- Lev 14:19 / 2Ch 29:16 / Eze 24:13 / **Eze 36:25** "I will sprinkle **clean** water … you shall be **clean** (ta.her/ta.hor) from all your **uncleannesses** (tum.ah)" — the cleanse-from-defilement seam.
- Lev 16:19 "**cleanse** it (ta.her) and **consecrate** it (qa.dash) from the **uncleannesses** (tum.ah)".
- Lev 15:31 "keep Israel **separate** (na.zar) from their **uncleanness**"; Num 5:19 "**free** (na.qah) … from uncleanness".
- **Tit 1:15** "to the **pure** (katharos), all things are pure, but to the **defiled** (miainō) … nothing is pure" — pure↔defiled in one breath.

So the defilement terms are genuinely engaged *as the opposite pole that the purity terms remove/contrast*. This is the H3 pole-pair structure (defilement ↔ purity, M12↔M10c) the typology predicts.

**VERDICT ⚖ BORDER (confirms §G):** these are **M10c defilement vocabulary**, not positive M12 units. They are present in M12 as the **deliberate contrast pole** (10/34 verses pair them directly with a purity term), so they are *analytically useful here*, but their **substantive home is M10c**. anosios in particular (moral_evaluation / IDENTITY-edge, vice-list company in 1Ti 1:9 & 2Ti 3:2) is squarely an M10 sin-identity term.

**RECOMMENDATION (flagged, NOT executed):** **Do NOT create a positive M12 unit from these.** Keep them only as a **referenced contrast pole** within the M12 purity units (cite the cleanse-from-uncleanness verses to anchor the inverse). Treat **M10c as the owning home** and cross-reference into M12; confirm with the researcher whether to formally cross-ref (preferred) vs leave the M12 tag. Per memory `feedback_t2_reference_flag_reclassify`/`feedback_external_pole_not_inner_state`, a contrast pole is a reference, never analysed standalone as an M12 object.

---

## Test 3 — Edge terms: per-term verdict

| term [Strong's] | focus occ | sense / data | verdict |
|---|---|---|---|
| **enchriō G1472** (anoint/rub-on) | 1 (Rev 3:18) | "**anoint** your eyes" with eyesalve — action, val commanded, obj=eyes | ⚠ **mis-grouped.** Physical/figurative eye-salve, not purity/cleansing. Not an M12 object. |
| **epichriō G2025** (rub on) | 2 (Joh 9:6, 9:11) | "**anointed** my eyes" (mud, healing-of-blindness) — action, val neutral, obj=eyes | ⚠ **mis-grouped.** Physical anointing in a healing miracle → closer to **M24 (weakness/healing)** or simply not inner-being. Not purity. |
| **morfoō G3445** (form) | 1 (Gal 4:19) | "until **Christ is formed** in you" — action, val righteous, obj=none | ⚖ **BORDER → re-home.** Spiritual *formation/transformation*, not purity. Fits the **renewal/new-creation axis (M11/M38/M45)** far better than M12. Drop from purity. |
| **tsur H6696C** (form) | **0** | — not present in the extract | ❓ **CLARIFY.** Zero occurrences here — named in the draft family but absent from M12 data. Nothing to own; remove from the M12 family list. |
| **me.tom H4974** (soundness) | 3 (Psa 38:3, 38:7, Isa 1:6) | "no **soundness** in my **flesh**/body" — status, val neutral/sinful, faculty none | ⚠ **mis-grouped → M24.** Bodily soundness/health under affliction (Psa 38, Isa 1:6 "no soundness … bruises and sores"). This is physical **wholeness/sickness**, not moral purity → **M24 (weakness/suffering)**. Confirms §G. |
| **mikh.lah H4357** (perfection) | **0** | — not present in the extract | ❓ **CLARIFY.** Zero occurrences in M12 data; named in the perfection family but absent. Remove from the M12 family list. |
| **tikh.lah H8502** (perfection) | 1 (Psa 119:96) | "I have seen a limit to all **perfection**, but your commandment is broad" — status, val neutral, faculty none | ⚖ **BORDER.** "Perfection/completeness" = limit of created things, not moral purity. Wisdom/Torah context (Psa 119) → better M13/M15 than M12. Minor; recommend drop from purity units. |

### Edge-term summary
- **No edge term is a genuine positive-purity object.** The two "form" terms (morfoō, tsur) and the "perfection/soundness" cluster (me.tom, mikh.lah, tikh.lah) are either *bodily soundness* (→ M24), *spiritual formation* (→ M11/M38/M45 renewal), or *completeness* (→ M13/M15) — and two of them (tsur, mikh.lah) **do not even appear** in the M12 extract.
- The anoint/rub-on pair (enchriō/epichriō) is **physical anointing** (eye-salve / healing-mud), not cultic anointing-for-consecration, so it is not the qa.dash consecration sense either.

**RECOMMENDATION (flagged, NOT executed):** drop all six edge terms from the M12 purity units. Specifically: route **me.tom → M24**; route **morfoō → renewal (M11/M38/M45)**; treat **enchriō/epichriō** as physical (likely not inner-being / M24-adjacent); treat **tikh.lah** as completeness (M13/M15-adjacent, minor); and **remove tsur H6696C + mikh.lah H4357** from the family list (no M12 occurrences). None require DB action now — flagged for the researcher.

---

## Net effect on M12 (informational)
Excluding na.tan alone removes ~1,065 of 3,247 focus occurrences (≈ 33 %) of pure noise. With the negation-pole reclassed to *referenced contrast* and the six edge terms re-homed, the M12 **positive** purity corpus is the six read-derived units (U1 ritual cleanness · U2 inner/moral purity · U3 holiness/consecration · U4 innocence/blamelessness · U5 sincerity · U6 incorruptibility) — clean, with the defilement pole engaged only as the contrast. **All recommendations are flagged; nothing has been executed.**

*Step-5 hygiene deep-read — the read is the test. na.tan = noise (≈0 purity-relevant); negation-pole = M10c contrast pole (keep referenced); edge terms = mis-grouped/absent. No reassignment performed.*
