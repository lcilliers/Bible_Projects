# Cluster input coverage audit v2 — M39

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M39/inputs/`:
- `ch1`
- `ch2`
- `ch3`
- `ch4`
- `ch5`
- `ch6`
- `ch7`

---

## A. Coverage

Every required evidence row's identifier must appear in at least one chapter input.

| Evidence | In DB | Required (excl. gap-status) | Missing | Pass |
|---|---|---|---|---|
| Finding scope-groups | 383 | 383 | 1 | NO |
| Sub-groups (non-BOUNDARY) | 3 | 3 | 0 | YES |
| Characteristics | 2 | 2 | 0 | YES |
| VCG codes | 34 | 34 | 3 | NO |
| Anchor verses | 49 | 49 | 17 | NO |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (1)

By tier: T3=1

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T3.5.3 | T3 | synth | — | silent | The silence of both sub-groups on the creative faculty is consistent. The grace/ |

### Missing VCG codes (3)
- `111-002`
- `494-002`
- `6837-005`

### Missing anchor verses (17)
- `111-002` — 1 anchor(s)
- `1299-001` — 1 anchor(s)
- `1299-003` — 1 anchor(s)
- `1299-004` — 2 anchor(s)
- `1301-001` — 1 anchor(s)
- `494-002` — 1 anchor(s)
- `632-002` — 2 anchor(s)
- `632-003` — 2 anchor(s)
- `888-004` — 1 anchor(s)
- `889-001` — 2 anchor(s)
- `889-002` — 1 anchor(s)
- `889-003` — 1 anchor(s)
- `984-001` — 1 anchor(s)

---

## B. Exclusion

Policy-excluded rows must not be referenced by any chapter input.

| Exclusion rule | Leaks |
|---|---|
| `gap`-status findings (silence-principle) | 0 |
| Non-publication observations | 0 |

---

## C. BOUNDARY readiness

Cluster must have no unresolved BOUNDARY items before publishing.

**PASS — no unresolved BOUNDARY items.**

### BOUNDARY inventory

- BOUNDARY sub-group present: no
- BOUNDARY_DECISION_PENDING flags: 0 total, 0 unresolved
- BOUNDARY mentions in cluster_observation (informational only — not gating): 0

---

## D. Stray Session B / Session D findings

Cluster must have no still-floating analytical findings from prior Session B / Session D work on its contributing registries.

| Source | Count | Pass |
|---|---|---|
| `wa_session_b_findings` (status pending/open) | 219 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 116 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (219)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 6 | anointing | 2 | DIMENSION_REVIEW |
| 42 | delight | 3 | DIMENSION_REVIEW |
| 43 | desire | 3 | DIMENSION_REVIEW |
| 68 | grace | 178 | DIMENSION_REVIEW, OBSERVATION, SYNTHESIS_INTER_TIER, SYNTHESIS_INTRA_TIER |
| 111 | mercy | 29 | DIMENSION_REVIEW, SYNTHESIS_INTER_TIER, SYNTHESIS_INTRA_TIER |
| 180 | yielding | 2 | DIMENSION_REVIEW |
| 186 | gladness | 1 | DIMENSION_REVIEW |
| 194 | blessing | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `DIM-068-001` (reg=68 grace, type=DIMENSION_REVIEW, status=pending) — Group 890-001 (ta.cha.nun, supplication) — Dan 9:3 anchor shows earnest supplication enacted somatically: fasting, sackcloth, ashes. The bod
- `DIM-111-001` (reg=111 mercy, type=DIMENSION_REVIEW, status=pending) — The atonement/propitiation vocabulary (kipper, kaphar, kapporet, hilasmos, hilastērios) within the mercy registry produces a cluster of Tran
- `DIM-180-001` (reg=180 yielding, type=DIMENSION_REVIEW, status=pending) — The paradidōmi (G3860) cluster in Reg 180 ([6835-001] through [6835-012]) spans 12 distinct inner-being uses: betrayal, Christ's passion, vo
- `DIM-180-002` (reg=180 yielding, type=DIMENSION_REVIEW, status=pending) — The dōron/didōmi gift-vocabulary sub-cluster in Reg 180 shows a consistent pattern: giving as the domain where inner character is most direc
- `DIM-186-001` (reg=186 gladness, type=DIMENSION_REVIEW, status=pending) — Ya.tav (H3190) produces three materially distinct dimension patterns: Affective/Emotional (merry heart), Moral/Conscience (moral goodness), 
- `DIM-194-001` (reg=194 blessing, type=DIMENSION_REVIEW, status=pending) — The blessing vocabulary reveals a mirror structure in Relational Disposition: group 1299-001 names God's inner disposition of love as the so
- `DIM-42-001` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — The delight vocabulary spans every dimension of the inner being. This breadth suggests delight is not a single category but a family of enga
- `DIM-42-002` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — H2654A (cha.phets) and H2654B (cha.phats) produce parallel three-group structures with equivalent classifications. Their functional equivale
- `DIM-42-003` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — Group 3090-001 (hēdonē — pleasure as the competing inner orientation, desires that war within) occupies a significant counter-position to th
- `DIM-43-001` (reg=43 desire, type=DIMENSION_REVIEW, status=pending) — Registry 43 (desire) shows a consistent divine/human register split: divine desire, will, and longing = Theological/Divine-Human; human desi

### Stray research flags (116)

By flag_code: SB_FINDING=36, SD_POINTER=80

First 10:
- `SD_POINTER` reg=68 grace (None) — Zec 12:10 is an anchor verse in both 889-001 (chen — divine relational favour) and 890-001 (ta.cha.nun — supplication). The same verse conne
- `SD_POINTER` reg=68 grace (None) — charizō carries both the giving sense and the forgiving sense as primary senses of the same term — not metaphorical extension but direct lex
- `SD_POINTER` reg=68 grace (None) — charizō's juridical sense (handing over to custody — Lk 23:25: Jesus handed over; Acts 27:24: Paul granted to those sailing) sits alongside 
- `SD_POINTER` reg=68 grace (None) — charis and chairo (to rejoice, be glad) share the lexical root χαρ-. Grace and joy are not merely theologically related — they share a root.
- `SD_POINTER` reg=68 grace (None) — The four semantic faces of charis suggest a possible sequential inner-being architecture: divine disposition (face 1) → relational standing 
- `SD_POINTER` reg=68 grace (None) — charis means 'gracious words' in Luk 4:22 and 'speech seasoned with grace' in Col 4:6 — the chen/grace-as-speech-quality sense carried into 
- `SD_POINTER` reg=68 grace (None) — charitoō is a biblical coinage — it does not appear in classical Greek. The need to create a new word for 'to grace someone' (to make someon
- `SD_POINTER` reg=68 grace (None) — The CHEN root family (chen, chanan, chanun, tachanum, techinah, chinnam) spans the giving side (chen — favour, chanan — be gracious), the st
- `SD_POINTER` reg=68 grace (None) — chen and chesed appear together in Exo 34:6 and other divine character formulas as distinct divine attributes. Proposed semantic distinction
- `SD_POINTER` reg=68 grace (None) — Zec 12:10: God pours out 'a spirit of grace and supplication' — the supplication is itself outpoured by God. The act by which the creature a

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 34 / 34.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 384 rows in 383 scope-groups

| Tier | Total |
|---|---|
| T0 | 29 |
| T1 | 50 |
| T2 | 62 |
| T3 | 65 |
| T4 | 49 |
| T5 | 40 |
| T6 | 49 |
| T7 | 40 |

| Status | Total |
|---|---|
| cluster_synthesis | 5 |
| finding | 353 |
| silent | 26 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
