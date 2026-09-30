# Cluster input coverage audit v2 — M02

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: FAIL
- Stray SB / SD findings: PASS

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M02/inputs/`:
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
| Finding scope-groups | 354 | 351 | 44 | NO |
| Sub-groups (non-BOUNDARY) | 7 | 7 | 0 | YES |
| Characteristics | 6 | 6 | 0 | YES |
| VCG codes | 25 | 25 | 0 | YES |
| Anchor verses | 53 | 53 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (44)

By tier: T2=2, T3=9, T4=7, T5=2, T6=13, T7=11

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.9.2 | T2 | synth | — | cluster_synthesis | The origin is multiple. The cluster evidences at least four distinct origins: (1 |
| T3.4.3 | T3 | synth | — | cluster_synthesis | The affective faculty is universally engaged but the quality of its engagement v |
| T3.6.3 | T3 | synth | — | cluster_synthesis | The characteristic consistently engages and drives the will, but the quality of  |
| T3.8.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that the characteristic is the affective dimension of the mo |
| T3.9.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that conscience is the moral faculty through which the anger |
| T3.11.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that this characteristic is both produced by relational capa |
| T4.1.4 | T4 | synth | — | silent | Not applicable. The God-to-human direction is the most extensively evidenced dir |
| T4.2.4 | T4 | synth | — | silent | Not applicable. The human-to-God direction is evidenced in both the jealous-zeal |
| T4.3.4 | T4 | synth | — | silent | Not applicable. The giving direction is evidenced through both the provocation a |
| T4.4.4 | T4 | synth | — | silent | Not applicable. Receiving direction is evidenced in M02-B-VCG-07 and M02-D-VCG-0 |
| T4.5.4 | T4 | synth | — | silent | Not applicable. The relational scope is extensively evidenced. |
| T4.6.3 | T4 | synth | — | silent | No angelic mediation of anger is evidenced in the corpus. The destroying angels  |
| T4.6.4 | T4 | synth | — | silent | The evidence is not entirely silent — adversarial spiritual anger is evidenced ( |
| T5.7.3 | T5 | synth | — | silent | T2.8 found deposit evidence. This prompt is not applicable. |
| T6.1.2 | T6 | synth | — | cluster_synthesis | The co-occurrence pattern reveals that anger rarely operates as an isolated sing |
| T6.1.3 | T6 | synth | — | silent | Not applicable. Multiple significant co-occurrence patterns are evidenced. |
| T6.2.3 | T6 | synth | — | silent | Not applicable. Multiple sequential patterns are evidenced. |
| T6.3.4 | T6 | synth | — | silent | Not applicable. Multiple causal and constitutive relationships are evidenced. |
| T6.4.4 | T6 | synth | — | silent | Not applicable. Significant vocabulary sharing is evidenced at multiple points. |
| T6.5.4 | T6 | synth | — | silent | Not applicable. Distinction work is required and performed above. |
| T6.6.3 | T6 | synth | — | silent | Not applicable. Shared anchors are identified and discussed. |
| T7.1.1 | T7 | synth | — | cluster_synthesis | Primary Hebrew: *cha.rah* (H2734) — root meaning to burn/kindle; reveals anger a |
| T7.1.2 | T7 | synth | — | cluster_synthesis | The cluster shows a comprehensive grammatical range. *Cha.rah* (H2734) and *qa.t |
| T7.1.4 | T7 | synth | — | cluster_synthesis | Yes, clearly: (1) Disposition vs act: *orgilos* (G3711, adjective) names the dis |
| T7.1.8 | T7 | synth | — | cluster_synthesis | The relationship evidences substantial continuity with significant development i |
| T7.1.10 | T7 | synth | — | cluster_synthesis | The full vocabulary arc reveals a characteristic that spans: (1) the most intern |
| T7.2.2 | T7 | synth | — | cluster_synthesis | M02 is carried across all major literary forms: (1) Narrative (Genesis–Kings, Da |
| T7.2.4 | T7 | synth | — | cluster_synthesis | Multiple contextual settings are evidenced: (1) Judicial/legal: Heb 3:11 (oath o |
| T7.2.5 | T7 | synth | — | cluster_synthesis | Multiple high-claim anchors across the cluster. For the judicial-wrath register: |
| T7.3.1 | T7 | synth | — | cluster_synthesis | Three frameworks are relevant and identified in the science extract: (1) Clinica |
| ... | ... | ... | ... | ... | +14 more |

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

**FAIL — 1 issue(s).**

- 4 unresolved `BOUNDARY_DECISION_PENDING` flag(s) for this cluster (of 6 total).

### BOUNDARY inventory

- BOUNDARY sub-group present: no
- BOUNDARY_DECISION_PENDING flags: 6 total, 4 unresolved

Unresolved flags:
- M02-BOUNDARY-G0485 (G0485) — M02 closure (DIR-20260516-014): BOUNDARY term G0485 (antilogia) reached closure without exit decision. Phase 9 per-term 
- M02-BOUNDARY-G2042 (G2042) — M02 closure (DIR-20260516-014): BOUNDARY term G2042 (erethizō) reached closure without exit decision. Phase 9 per-term s
- M02-BOUNDARY-G2200 (G2200) — M02 closure (DIR-20260516-014): BOUNDARY term G2200 (zestos) reached closure without exit decision. Phase 9 per-term str
- M02-BOUNDARY-H3708B (H3708B) — M02 closure (DIR-20260516-014): BOUNDARY term H3708B (ka.a.s) reached closure without exit decision. Phase 9 per-term st
- BOUNDARY mentions in cluster_observation (informational only — not gating): 0

---

## D. Stray Session B / Session D findings

Cluster must have no still-floating analytical findings from prior Session B / Session D work on its contributing registries.

| Source | Count | Pass |
|---|---|---|
| `wa_session_b_findings` (status pending/open) | 0 | YES |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 0 | YES |
| `session_d_runs` rows referencing cluster | 0 | YES |

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 25 / 25.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 389 rows in 354 scope-groups

| Tier | Total |
|---|---|
| T0 | 53 |
| T1 | 64 |
| T2 | 60 |
| T3 | 65 |
| T4 | 46 |
| T5 | 40 |
| T6 | 35 |
| T7 | 26 |

| Status | Total |
|---|---|
| cluster_synthesis | 56 |
| finding | 289 |
| gap | 3 |
| silent | 41 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
