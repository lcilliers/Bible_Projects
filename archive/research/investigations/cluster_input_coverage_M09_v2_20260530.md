# Cluster input coverage audit v2 — M09

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M09/inputs/`:
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
| Finding scope-groups | 1323 | 1320 | 1068 | NO |
| Sub-groups (non-BOUNDARY) | 8 | 8 | 0 | YES |
| Characteristics | 6 | 6 | 1 | NO |
| VCG codes | 21 | 21 | 0 | YES |
| Anchor verses | 21 | 21 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (1068)

By tier: T2=214, T3=231, T4=168, T5=147, T6=168, T7=140

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.1.1 | T2 | char | Submission | silent | **[CHAR-2]** S — The Submission corpus does not explicitly name the spirit level |
| T2.1.2 | T2 | char | Submission | finding | **[CHAR-2]** E — Not directly, but the depth implied by several verses is consis |
| T2.1.3 | T2 | char | Submission | finding | **[CHAR-2]** E — To the extent spirit-level depth is implied (T2.1.2), it reveal |
| T2.1.4 | T2 | char | Submission | finding | **[CHAR-2]** E — The evidence is not fully silent but is primarily indirect rega |
| T2.2.1 | T2 | char | Submission | finding | **[CHAR-2]** E — Yes, explicitly. 1Pe1:22 — "having purified your souls by your  |
| T2.2.2 | T2 | char | Submission | finding | **[CHAR-2]** E — 1Pe1:22 reveals that submission, as obedience to truth, is not  |
| T2.2.3 | T2 | char | Submission | finding | **[CHAR-2]** E — The evidence is not silent; soul-level location is explicitly e |
| T2.3.1 | T2 | char | Submission | finding | **[CHAR-2]** E — Yes, explicitly and primarily. Rom6:17 — "obedient from the hea |
| T2.3.2 | T2 | char | Submission | finding | **[CHAR-2]** E — The heart-location engages the heart's *integrating moral and v |
| T2.3.3 | T2 | char | Submission | finding | **[CHAR-2]** E — The evidence is not silent; heart-location is explicit and prim |
| T2.4.1 | T2 | char | Submission | finding | **[CHAR-2]** E — Yes, directly in 2Cor10:5 — "take every thought captive to obey |
| T2.4.2 | T2 | char | Submission | finding | **[CHAR-2]** E — 2Cor10:5 reveals that submission engages the mind's *evaluative |
| T2.4.3 | T2 | char | Submission | finding | **[CHAR-2]** E — The evidence is not silent; mind-location is explicitly evidenc |
| T2.5.1 | T2 | char | Submission | finding | **[CHAR-2]** E — The conscience is surfaced as a distinct soul-level location. P |
| T2.5.2 | T2 | char | Submission | finding | **[CHAR-2]** E — The conscience as distinct soul-level location reveals that gen |
| T2.5.3 | T2 | char | Submission | finding | **[CHAR-2]** E — The evidence is not silent; the conscience is evidenced as a di |
| T2.6.1 | T2 | char | Submission | finding | **[CHAR-2]** E — Yes, in two forms. First, Rom6:12 — "let not sin reign in your  |
| T2.6.2 | T2 | char | Submission | finding | **[CHAR-2]** E — Two different functions. In Rom6:12, the link is *diagnostic*:  |
| T2.6.3 | T2 | char | Submission | finding | **[CHAR-2]** E — Body-part links are evidenced (see T2.6.1 and T2.6.2). |
| T2.7.1 | T2 | char | Submission | finding | **[CHAR-2]** E — The direction differs between the two body-links. In Rom6:12 (b |
| T2.7.2 | T2 | char | Submission | finding | **[CHAR-2]** E — The bidirectionality reveals that submission is engaged in a ge |
| T2.7.3 | T2 | char | Submission | finding | **[CHAR-2]** E — Body links are evidenced and the direction analysed (see T2.7.1 |
| T2.8.1 | T2 | char | Submission | silent | **[CHAR-2]** S — The Submission corpus does not directly evidence a constitution |
| T2.8.2 | T2 | char | Submission | silent | **[CHAR-2]** S — No verse in §3.A directly contradicts the absence of bodily dep |
| T2.8.3 | T2 | char | Submission | silent | **[CHAR-2]** S — The evidence is silent on constitutional bodily deposit from su |
| T2.9.1 | T2 | char | Submission | finding | **[CHAR-2]** E — The corpus evidences multiple constitutional origins varying by |
| T2.9.2 | T2 | char | Submission | finding | **[CHAR-2]** E — The origin is clearly multiple, as T2.9.1 demonstrates. The mos |
| T2.9.3 | T2 | char | Submission | finding | **[CHAR-2]** E — Yes. *Acute-event context* (Heb11:8 — Abraham's obedient depart |
| T2.10.1 | T2 | char | Submission | finding | **[CHAR-2]** E — Yes. The clearest constitutional movement is evidenced in 1Pe1: |
| T2.10.2 | T2 | char | Submission | finding | **[CHAR-2]** E — The pattern from 1Pe1:22 is sequential: (1) hearing truth / enc |
| ... | ... | ... | ... | ... | +1038 more |

### Missing characteristics (1)
- id=22 — Meekness and gentleness

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
| `wa_session_b_findings` (status pending/open) | 186 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 66 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (186)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 30 | contrition | 180 | OBSERVATION, SYNTHESIS_INTER_TIER, SYNTHESIS_INTRA_TIER |
| 80 | humility | 1 | DIMENSION_REVIEW |
| 114 | obedience | 1 | DIMENSION_REVIEW |
| 155 | submission | 1 | DIMENSION_REVIEW |
| 173 | will | 2 | DIMENSION_REVIEW |
| 208 | sloth | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `DIM-114-001` (reg=114 obedience, type=DIMENSION_REVIEW, status=pending) — Reg 114 contains the counter-term to disobedience: [1020-002] names Christ's obedience as the inner act that reverses Adam's. Session B shou
- `DIM-155-001` (reg=155 submission, type=DIMENSION_REVIEW, status=pending) — The submission registry distinguishes two dimensions: relational submission to human authority ([1147-001], Relational/Social) and submissio
- `DIM-173-001` (reg=173 will, type=DIMENSION_REVIEW, status=pending) — The will registry shows the widest dimension spread in C14, spanning Volitional/Will, Theological/Divine-Human, Affective/Emotional, Spiritu
- `DIM-173-002` (reg=173 will, type=DIMENSION_REVIEW, status=pending) — The halakh (to go/walk) groups ([1235-001] through [1235-006]) form a coherent inner-being sub-cluster: inner movement as metaphor for inner
- `DIM-208-001` (reg=208 sloth, type=DIMENSION_REVIEW, status=pending) — Group 1374-001 (the sluggard whose desire craves but whose will refuses to act) names sloth's inner-being structure precisely: not the absen
- `DIM-80-001` (reg=80 humility, type=DIMENSION_REVIEW, status=pending) — Registry 80 (humility) shows the biblical vocabulary of humility operating primarily as Character/Disposition (8 groups) with significant Th
- `OBS-030-004` (reg=30 contrition, type=OBSERVATION, status=open) — carry_forward=1. This indicates the registry was carried forward from a prior programme phase. It does not affect analytical scope but is no
- `OBS-030-010` (reg=30 contrition, type=OBSERVATION, status=open) — H1793B is a homograph — the same Hebrew spelling (dak.ka) carries two semantic entries: "contrite" (H1793A) and "dust" (H1793B). The verses 
- `OBS-030-011` (reg=30 contrition, type=OBSERVATION, status=open) — SBF-036-001 is referenced in the readiness output as a prior-session finding. However, §H shows zero existing session_b_findings for R030. T
- `OBS-030-012` (reg=30 contrition, type=OBSERVATION, status=open) — H1794 is a distinct root from H1792 but carries the same semantic range (crush/contrite/broken). Its sub-sense structure parallels H1792: pa

### Stray research flags (66)

By flag_code: SB_FINDING=56, SD_POINTER=10

First 10:
- `SD_POINTER` reg=173 will (None) — The inheritance sub-cluster in Reg 173 ([3094-001], [3094-002], [3095-001], [3095-002], [3095-003]) is analytically adjacent to the justice/
- `SD_POINTER` reg=30 contrition (None) — Registry 30 (contrition) produces strong convergence: 5 of 9 groups assign Dependence / Creatureliness (7552-003, 7553-001, 7554-001, 7555-0
- `SD_POINTER` reg=30 contrition (None) — R105 (lust) (raised in Unit Unit 2)
- `SD_POINTER` reg=30 contrition (None) — R151 (sorrow) and R062 (fellowship) (raised in Unit Unit 5)
- `SD_POINTER` reg=30 contrition (None) — R061 (fear) (raised in Unit Unit 5)
- `SD_POINTER` reg=30 contrition (None) — R123 (pride) (raised in Unit Unit 5)
- `SD_POINTER` reg=30 contrition (None) — vitality/existence or death registry (registry number not confirmed) (raised in Unit Unit 7 / Group 7552-001 / Psa 143:3)
- `SD_POINTER` reg=30 contrition (None) — R123 (pride) or hardness/stubbornness registry (raised in Unit Unit 7 / Group 7552-003 / Jer 44:10)
- `SD_POINTER` reg=30 contrition (None) — R183 (heart) (raised in Unit Unit 7 / Group 7553-001 / Psa 34:18)
- `SD_POINTER` reg=30 contrition (None) — sacrifice/worship registry or forgiveness registry (registry numbers not confirmed) (raised in Unit Unit 7 / Group 7554-001 / Psa 51:17)

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 21 / 21.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 1323 rows in 1323 scope-groups

| Tier | Total |
|---|---|
| T0 | 84 |
| T1 | 168 |
| T2 | 217 |
| T3 | 231 |
| T4 | 168 |
| T5 | 147 |
| T6 | 168 |
| T7 | 140 |

| Status | Total |
|---|---|
| cluster_synthesis | 189 |
| finding | 917 |
| gap | 3 |
| silent | 214 |

### Cluster observations: 6 active

| target_phase | status | n |
|---|---|---|
| phase_9_findings | confirmed | 5 |
| session_d | confirmed | 1 |
