# Cluster input coverage audit v2 — M01

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: FAIL
- Stray SB / SD findings: PASS

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M01/inputs/`:
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
| Finding scope-groups | 797 | 797 | 20 | NO |
| Sub-groups (non-BOUNDARY) | 8 | 8 | 0 | YES |
| Characteristics | 7 | 7 | 0 | YES |
| VCG codes | 36 | 36 | 0 | YES |
| Anchor verses | 89 | 89 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (20)

By tier: T2=2, T3=11, T5=2, T6=4, T7=1

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.8.2 | T2 | synth | — | silent | No verse in M01 explicitly addresses constitutional deposit in the body. The Heb |
| T2.8.3 | T2 | synth | — | silent | The evidence across all M01 sub-groups is silent on constitutional deposit in th |
| T3.1.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that fear is a perceptively-saturated characteristic: it is  |
| T3.2.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that fear has a fundamental cognitive dimension: it either o |
| T3.3.3 | T3 | synth | — | cluster_synthesis | Fear's engagement with memory reveals that it is a temporally situated character |
| T3.4.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that fear is the inner-being characteristic with the widest  |
| T3.5.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that disordered fear captures the imagination for negative p |
| T3.6.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that fear is fundamentally a volitional characteristic: its  |
| T3.7.3 | T3 | synth | — | cluster_synthesis | The pattern confirms that fear is an agency-shaping characteristic at its core:  |
| T3.8.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that fear-of-God is the constitutive interior moral faculty  |
| T3.9.3 | T3 | synth | — | cluster_synthesis | The pattern confirms a structural relationship between fear of God and conscienc |
| T3.10.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that ordered fear of God is not an isolated inner experience |
| T3.11.3 | T3 | synth | — | cluster_synthesis | The pattern reveals that fear is fundamentally a relational characteristic — its |
| T5.7.1 | T5 | synth | — | silent | T2.8 found the verse evidence across all M01 sub-groups silent on constitutional |
| T5.7.3 | T5 | synth | — | silent | T2.8 found no constitutional deposit in the body. T5.7 is closed. The generation |
| T6.4.3 | T6 | synth | — | cluster_synthesis | The vocabulary sharing within M01 reveals that its sub-groups are facets of a si |
| T6.6.2 | T6 | synth | — | cluster_synthesis | [E] Shared anchors reveal that M01 is structurally central in the programme's in |
| T6.7.2 | T6 | synth | — | silent | Cannot be fully answered pending adjacent cluster completion. The anticipated pa |
| T6.7.3 | T6 | synth | — | silent | Dimensional sharing data across the programme is not yet available. M01 is an ea |
| T7.1.10 | T7 | synth | — | cluster_synthesis | The full vocabulary arc of M01 — from ya.re / yir.ah / pa.chad (Hebrew) through  |

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

- 7 unresolved `BOUNDARY_DECISION_PENDING` flag(s) for this cluster (of 12 total).

### BOUNDARY inventory

- BOUNDARY sub-group present: no
- BOUNDARY_DECISION_PENDING flags: 12 total, 7 unresolved

Unresolved flags:
- M01-BOUNDARY-G2285 (G2285) — M01 closure (DIR-20260516-007): BOUNDARY term G2285 (thambos) reached closure without exit decision. Phase 9 per-term st
- M01-BOUNDARY-H2189 (H2189) — M01 closure (DIR-20260516-007): BOUNDARY term H2189 (za.a.vah) reached closure without exit decision. Phase 9 per-term s
- M01-BOUNDARY-H4867 (H4867) — M01 closure (DIR-20260516-007): BOUNDARY term H4867 (mish.bar) reached closure without exit decision. Phase 9 per-term s
- M01-BOUNDARY-H6178 (H6178) — M01 closure (DIR-20260516-007): BOUNDARY term H6178 (a.ruts) reached closure without exit decision. Phase 9 per-term str
- M01-BOUNDARY-H8047G (H8047G) — M01 closure (DIR-20260516-007): BOUNDARY term H8047G (sham.mah) reached closure without exit decision. Phase 9 per-term 
- M01-BOUNDARY-H8312 (H8312) — M01 closure (DIR-20260516-007): BOUNDARY term H8312 (sar.ap.pim) reached closure without exit decision. Phase 9 per-term
- M01-BOUNDARY-H8539 (H8539) — M01 closure (DIR-20260516-007): BOUNDARY term H8539 (ta.mah) reached closure without exit decision. Phase 9 per-term str
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

VCG `context_description` carried in DB but not in chapter inputs: 36 / 36.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 805 rows in 797 scope-groups

| Tier | Total |
|---|---|
| T0 | 82 |
| T1 | 148 |
| T2 | 141 |
| T3 | 119 |
| T4 | 82 |
| T5 | 70 |
| T6 | 75 |
| T7 | 88 |

| Status | Total |
|---|---|
| cluster_synthesis | 147 |
| finding | 543 |
| silent | 115 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
