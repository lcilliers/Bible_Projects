# Cluster input coverage audit v2 — M07

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M07/inputs/`:
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
| Finding scope-groups | 1323 | 1303 | 1051 | NO |
| Sub-groups (non-BOUNDARY) | 9 | 9 | 0 | YES |
| Characteristics | 6 | 6 | 0 | YES |
| VCG codes | 28 | 28 | 0 | YES |
| Anchor verses | 28 | 28 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (1051)

By tier: T2=217, T3=231, T4=168, T5=147, T6=153, T7=135

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.1.1 | T2 | char | Shame as experienced inner state | silent | **[CHAR-1]** S — No verse in the 224-verse corpus explicitly identifies shame as |
| T2.1.2 | T2 | char | Shame as experienced inner state | silent | **[CHAR-1]** S — Not evidenced. The primary constitutional location across the c |
| T2.1.3 | T2 | char | Shame as experienced inner state | silent | **[CHAR-1]** S — Not directly applicable given the absence of spirit-level locat |
| T2.1.4 | T2 | char | Shame as experienced inner state | silent | **[CHAR-1]** S — The 224-verse CHAR-1 corpus is silent on spirit-level location. |
| T2.10.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Yes. The evidence shows shame moving from inner to outer consis |
| T2.10.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — The primary pattern is: *trigger event → inner collapse → bodil |
| T2.10.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable; constitutional movement is evidenced above. |
| T2.2.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Yes, by location and language. The soul (nefesh) is the locus o |
| T2.2.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Soul-level location confirms that CHAR-1 is an experience of th |
| T2.2.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable; soul-level evidence is present. |
| T2.3.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Yes, with specific evidence. Psa 119:80 (vc=65520): "may my hea |
| T2.3.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Heart-location reveals that shame engages the integrating centr |
| T2.3.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable; heart-location is evidenced. |
| T2.4.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — The cognitive dimension of CHAR-1 is present in several registe |
| T2.4.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Mind-location reveals that shame is not merely emotional — it i |
| T2.4.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable; mind-location is evidenced. |
| T2.5.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Conscience is the most prominent additional soul-location for C |
| T2.5.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Conscience as the additional soul-subset location reveals that  |
| T2.5.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable; conscience as an additional soul-subset is evid |
| T2.6.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Yes, with multiple body-part links evidenced. (1) **The face**  |
| T2.6.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — The face-link is both *indicative* (showing shame's outward vis |
| T2.6.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable; multiple body-part links are evidenced. |
| T2.7.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Primarily **inner → body**: the felt inner shame produces the b |
| T2.7.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — The primarily inner → body direction confirms that CHAR-1 is fi |
| T2.7.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not applicable. |
| T2.8.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — The evidence suggests a functional deposit but not a biological |
| T2.8.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Supporting: Pro 12:4 ("rottenness in the bones"), Eze 32:24-30  |
| T2.8.3 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Not silent; the "rottenness in the bones" and shame-carried-to- |
| T2.9.1 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Multiple origins are evidenced, corresponding to the three sub- |
| T2.9.2 | T2 | char | Shame as experienced inner state | finding | **[CHAR-1]** E — Definitively multiple. CHAR-1 cannot be reduced to a single ori |
| ... | ... | ... | ... | ... | +1021 more |

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
| `wa_session_b_findings` (status pending/open) | 41 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 28 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (41)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 31 | corruption | 1 | DIMENSION_REVIEW |
| 57 | evil | 2 | DIMENSION_REVIEW |
| 80 | humility | 1 | DIMENSION_REVIEW |
| 90 | innocence | 1 | DIMENSION_REVIEW |
| 117 | peace | 31 | DATA_ANOMALY_QA_GAP, DIMENSION_REVIEW, SYNTHESIS_INTER_TIER, SYNTHESIS_INTRA_TIE |
| 131 | rejection | 2 | DIMENSION_REVIEW |
| 146 | shame | 1 | DIMENSION_REVIEW |
| 149 | slander | 1 | DIMENSION_REVIEW |
| 190 | contempt | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `ANOMALY-117-002` (reg=117 peace, type=DATA_ANOMALY_QA_GAP, status=open) — [v1.8 capture audit] Tiered (T0–T7) prompt coverage 188/189 across all v1.8 captures for R117. This obslog: 187 Q&A entries; cumulative DB c
- `DIM-117-001` (reg=117 peace, type=DIMENSION_REVIEW, status=pending) — Peace (#117) carries 15 terms with status=extracted_theological_anchor (818 active verses). These are divine names, titles, and eternal/host
- `DIM-117-002` (reg=117 peace, type=DIMENSION_REVIEW, status=pending) — The peace registry's inner-being content is unusually wide — spanning the felt inner state of rest/peace (Emotion — Positive), the inner pos
- `DIM-131-001` (reg=131 rejection, type=DIMENSION_REVIEW, status=pending) — apobolē (1094-001, Rom 11:15) carries one of the highest concentrations of theological density in the programme — rejection, reconciliation,
- `DIM-131-002` (reg=131 rejection, type=DIMENSION_REVIEW, status=pending) — apoballō (6115-001) covers only two NT verses (Heb 10:35 and Mark 10:50) — one warning against throwing away confidence, one depicting urgen
- `DIM-146-001` (reg=146 shame, type=DIMENSION_REVIEW, status=pending) — Shame vocabulary in Registry 146 operates on two consistent axes: (a) inner shame as felt condition (affective, moral, spiritual) and (b) sh
- `DIM-149-001` (reg=149 slander, type=DIMENSION_REVIEW, status=pending) — The slander registry contains three foot-related groups (6253-001: moral life direction; 6253-002: relational submission/devotion; 6256-001:
- `DIM-190-001` (reg=190 contempt, type=DIMENSION_REVIEW, status=pending) — Contempt vocabulary in Registry 190 operates at three levels: (a) the inner disposition of contempt as evaluative stance (Character/Disposit
- `DIM-31-001` (reg=31 corruption, type=DIMENSION_REVIEW, status=pending) — Registry 31 contains two distinct sub-domains: (1) moral corruption as inner condition (4899-001, 4900-001, 4901-001, 745-001) and (2) escha
- `DIM-57-001` (reg=57 evil, type=DIMENSION_REVIEW, status=pending) — Registry 57 (evil) is the largest in the programme (46 groups) and functions partly as a container for inner-being framing particles (kol H3

### Stray research flags (28)

By flag_code: SD_CLUSTER=1, SD_POINTER=27

First 10:
- `SD_POINTER` reg=146 shame (None) — Registry 146 (shame) and Registry 190 (contempt) are relational inverses in C06: contempt is the inner disposition that assigns worthlessnes
- `SD_POINTER` reg=57 evil (None) — The Affective/Emotional dimension appears extensively in C11 (15 groups assigned) but was absent from C10 assignments, despite groups in C10
- `SD_POINTER` reg=57 evil (None) — The Sin & Vice / Moral/Conscience boundary was systematically refined in C11: Sin & Vice = inner condition of moral failure (wickedness, dec
- `SD_POINTER` reg=185 flesh (None) — The flesh registries reveal a fundamental theological shift: OT ba.sar/be.shar = creaturely somatic solidarity (Somatic/Embodied, Relational
- `SD_POINTER` reg=117 peace (H3070) — H3070 (YHWH-Yireh, YHWH-Jireh) registration anomaly: owner_registry field points to experience (#58) but this term is registered as extracte
- `SD_POINTER` reg=117 peace (H3068G) — H3068G (YHWH/Yahweh) registration anomaly: owner_registry = NULL, active_verse_count = 0. This is the primary divine name; its absence of an
- `SD_POINTER` reg=117 peace (None) — Group 2508-004 (H7965G sha.lom — messianic/eschatological peace) establishes that shalom in the Hebrew prophetic corpus is constitutively id
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer]   Target: R117 (peace) — internal structural question (now resolved: shalom reinstated) Connecting term:  Evidence 
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer] What is the analytical relationship between NT peace and love at the level of these terms? G1518 peacemaker owned b
- `SD_POINTER` reg=117 peace (None) — [v1.8 obslog SD pointer] Is the peace-heart connection constitutive? Is peace-strength (28 verses) grounded in Isa 30:15?  Target: R183 (hea

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 28 / 28.

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
| finding | 972 |
| gap | 20 |
| silent | 142 |

### Cluster observations: 5 active

| target_phase | status | n |
|---|---|---|
| phase_9_findings | confirmed | 3 |
| session_d | confirmed | 2 |
