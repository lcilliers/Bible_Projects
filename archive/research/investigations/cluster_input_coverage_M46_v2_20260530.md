# Cluster input coverage audit v2 — M46

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M46/inputs/`:
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
| Finding scope-groups | 381 | 378 | 46 | NO |
| Sub-groups (non-BOUNDARY) | 4 | 4 | 0 | YES |
| Characteristics | 4 | 4 | 0 | YES |
| VCG codes | 33 | 33 | 31 | NO |
| Anchor verses | 30 | 30 | 7 | NO |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (46)

By tier: T2=6, T3=14, T4=4, T5=2, T6=7, T7=13

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.1.1 | T2 | synth | — | silent | The cluster's 197 relevant verses contain no explicit spirit-level (ruach / pneu |
| T2.1.2 | T2 | synth | — | silent | No verse in the cluster assigns origin to the human spirit. The wealth-domain ch |
| T2.1.3 | T2 | synth | — | silent | no spirit-level evidence to interpret. |
| T2.1.4 | T2 | synth | — | cluster_synthesis | The complete silence of spirit-level location across all 197 relevant verses and |
| T2.3.3 | T2 | synth | — | cluster_synthesis | Heart-location is present across all four sub-groups, though M46-A has the only  |
| T2.9.2 | T2 | synth | — | cluster_synthesis | Multiple origins are the rule across all four sub-groups. The cluster does not e |
| T3.1.3 | T3 | synth | — | cluster_synthesis | The wealth domain systematically engages the perceptive faculty — but primarily  |
| T3.2.3 | T3 | synth | — | cluster_synthesis | Cognition is the primary faculty that distinguishes M46-C and M46-D from M46-A a |
| T3.3.3 | T3 | synth | — | cluster_synthesis | The memory faculty is silent across M46-B, M46-C, and M46-D. M46-A's engagement  |
| T3.4.3 | T3 | synth | — | cluster_synthesis | The wealth domain profoundly engages the affective faculty — but again in opposi |
| T3.5.1 | T3 | synth | — | silent | The creative faculty (imagination and origination) is not evidenced as a signifi |
| T3.5.2 | T3 | synth | — | silent | No engagement with creativity evidenced across any sub-group. |
| T3.5.3 | T3 | synth | — | silent | No engagement with creativity evidenced across any sub-group.  [Cluster-level ad |
| T3.6.3 | T3 | synth | — | cluster_synthesis | The volitional faculty is the hinge of the wealth domain. The direction in which |
| T3.7.3 | T3 | synth | — | cluster_synthesis | Agency is consistently engaged across all four sub-groups, but its direction var |
| T3.8.3 | T3 | synth | — | cluster_synthesis | The wealth domain is one of Scripture's primary testing grounds for the moral ev |
| T3.9.3 | T3 | synth | — | cluster_synthesis | The wealth domain is specifically identified across M46 as a domain in which con |
| T3.10.2 | T3 | synth | — | cluster_synthesis | Conscientiousness is impaired in M46-A and M46-B, enabled and exercised in M46-C |
| T3.10.3 | T3 | synth | — | cluster_synthesis | Conscientiousness is impaired in M46-A and M46-B, enabled and exercised in M46-C |
| T3.11.3 | T3 | synth | — | cluster_synthesis | Relational capacity is one of the most consistently engaged faculties across all |
| T4.1.3 | T4 | synth | — | cluster_synthesis | The cluster reveals God's disposition toward the human person in the wealth doma |
| T4.2.3 | T4 | synth | — | cluster_synthesis | The wealth domain is one of Scripture's primary tests of whether the human perso |
| T4.5.2 | T4 | synth | — | cluster_synthesis | The wealth domain crosses covenantal boundaries in both directions. The prosperi |
| T4.5.3 | T4 | synth | — | cluster_synthesis | The relational scope of M46 is universal: all four sub-groups operate across cov |
| T5.3.2 | T5 | synth | — | cluster_synthesis | The wealth domain reveals rather than produces inner conditions. Material prospe |
| T5.5.2 | T5 | synth | — | cluster_synthesis | The wealth domain is one of Scripture's primary formation arenas. The person's r |
| T6.1.2 | T6 | synth | — | cluster_synthesis | The cluster's co-occurrence pattern reveals that M46 sits at the intersection of |
| T6.3.3 | T6 | synth | — | cluster_synthesis | Inner closure (M46-A) may constitute or contribute to idolatry (the fat-heart →  |
| T6.4.1 | T6 | synth | — | cluster_synthesis | The cluster shares vocabulary with multiple adjacent programme areas. Sha.men (f |
| T6.4.2 | T6 | synth | — | cluster_synthesis | SHA.MAN root shares: sha.men (rich adj, H8082), sha.man verb (to grow fat, H8080 |
| ... | ... | ... | ... | ... | +16 more |

### Missing VCG codes (31)
- `111-001`
- `4697-002`
- `4697-001`
- `4898-001`
- `3836-001`
- `1142-001`
- `7586-002`
- `7010-001`
- `681-001`
- `7578-001`
- `7586-001`
- `7579-001`
- `7109-001`
- `7583-003`
- `7585-002`
- `4702-001`
- `7577-001`
- `7577-002`
- `7577-003`
- `7579-002`
- `7580-001`
- `7581-001`
- `7581-002`
- `7582-001`
- `7583-001`
- `7583-002`
- `7584-001`
- `7584-002`
- `7585-003`
- `7585-001`
- … +1 more

### Missing anchor verses (7)
- `1142-001` — 2 anchor(s)
- `4695-001` — 1 anchor(s)
- `4898-001` — 1 anchor(s)
- `7109-001` — 1 anchor(s)
- `7577-001` — 1 anchor(s)
- `7586-002` — 1 anchor(s)

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
| `wa_session_b_findings` (status pending/open) | 38 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 30 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (38)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 6 | anointing | 2 | DIMENSION_REVIEW |
| 29 | contentment | 1 | DIMENSION_REVIEW |
| 42 | delight | 3 | DIMENSION_REVIEW |
| 117 | peace | 31 | DATA_ANOMALY_QA_GAP, DIMENSION_REVIEW, SYNTHESIS_INTER_TIER, SYNTHESIS_INTRA_TIE |
| 187 | strength | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `ANOMALY-117-002` (reg=117 peace, type=DATA_ANOMALY_QA_GAP, status=open) — [v1.8 capture audit] Tiered (T0–T7) prompt coverage 188/189 across all v1.8 captures for R117. This obslog: 187 Q&A entries; cumulative DB c
- `DIM-117-001` (reg=117 peace, type=DIMENSION_REVIEW, status=pending) — Peace (#117) carries 15 terms with status=extracted_theological_anchor (818 active verses). These are divine names, titles, and eternal/host
- `DIM-117-002` (reg=117 peace, type=DIMENSION_REVIEW, status=pending) — The peace registry's inner-being content is unusually wide — spanning the felt inner state of rest/peace (Emotion — Positive), the inner pos
- `DIM-187-001` (reg=187 strength, type=DIMENSION_REVIEW, status=pending) — Group 7013-001 (a.yil, ram) carries a verse-level valuation in which obedience (H8085H sha.ma) and attentive listening (H7181 qashav) are de
- `DIM-29-001` (reg=29 contentment, type=DIMENSION_REVIEW, status=pending) — Both contentment terms name a stable inner condition independent of circumstances — a learned/acquired disposition of sufficiency, not a tra
- `DIM-42-001` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — The delight vocabulary spans every dimension of the inner being. This breadth suggests delight is not a single category but a family of enga
- `DIM-42-002` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — H2654A (cha.phets) and H2654B (cha.phats) produce parallel three-group structures with equivalent classifications. Their functional equivale
- `DIM-42-003` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — Group 3090-001 (hēdonē — pleasure as the competing inner orientation, desires that war within) occupies a significant counter-position to th
- `DIM-6-001` (reg=6 anointing, type=DIMENSION_REVIEW, status=pending) — Registry 6 (anointing) spans 7 dimensions across 38 groups — the widest dimensional range in C16. Session B should examine whether this brea
- `DIM-6-002` (reg=6 anointing, type=DIMENSION_REVIEW, status=pending) — Multiple Transformation groups in Reg 6 have GOD as dominant subject (167-001, 179-002, 4697-001, 4701-001, 4701-002). Session B should expl

### Stray research flags (30)

By flag_code: SD_POINTER=30

First 10:
- `SD_POINTER` reg=6 anointing (None) — C16 contains a substantial concentration of GOD-dominant Agency/Power and Transformation groups across anointing, consecration, and blessing
- `SD_POINTER` reg=117 peace (H3070) — H3070 (YHWH-Yireh, YHWH-Jireh) registration anomaly: owner_registry field points to experience (#58) but this term is registered as extracte
- `SD_POINTER` reg=117 peace (H3068G) — H3068G (YHWH/Yahweh) registration anomaly: owner_registry = NULL, active_verse_count = 0. This is the primary divine name; its absence of an
- `SD_POINTER` reg=117 peace (None) — Group 2508-004 (H7965G sha.lom — messianic/eschatological peace) establishes that shalom in the Hebrew prophetic corpus is constitutively id
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer]   Target: R117 (peace) — internal structural question (now resolved: shalom reinstated) Connecting term:  Evidence 
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer] What is the analytical relationship between NT peace and love at the level of these terms? G1518 peacemaker owned b
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer] Is the peace-heart connection constitutive? Is peace-strength (28 verses) grounded in Isa 30:15?  Target: R183 (hea
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer] Is the Isa 30:15 sequence (returning → rest → quietness → trust → strength) a structural node?  Target: R163 (trust
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer]   Target: R19 (calling) — shared anchor Hos 2:16 Connecting term: H1180 ba.ali Evidence basis: OBS-117-057
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer] Is there a systematic pattern locating peace/restlessness in the belly (meah)?  Target: R183 (heart/inner being), R

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 33 / 33.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 381 rows in 381 scope-groups

| Tier | Total |
|---|---|
| T0 | 38 |
| T1 | 71 |
| T2 | 68 |
| T3 | 84 |
| T4 | 33 |
| T5 | 28 |
| T6 | 30 |
| T7 | 29 |

| Status | Total |
|---|---|
| cluster_synthesis | 51 |
| finding | 292 |
| gap | 3 |
| silent | 35 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
