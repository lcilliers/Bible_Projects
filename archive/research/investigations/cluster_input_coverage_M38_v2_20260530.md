# Cluster input coverage audit v2 — M38

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: PASS

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M38/inputs/`:
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
| Finding scope-groups | 1512 | 1459 | 1 | NO |
| Sub-groups (non-BOUNDARY) | 7 | 7 | 0 | YES |
| Characteristics | 7 | 7 | 0 | YES |
| VCG codes | 45 | 45 | 0 | YES |
| Anchor verses | 45 | 45 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (1)

By tier: T5=1

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T5.7.3 | T5 | synth | — | cluster_synthesis | **[CLUSTER]** G — All seven characteristics record a gap at T5.7.3, none able to |

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
- BOUNDARY mentions in cluster_observation (informational only — not gating): 3
  These rows mention BOUNDARY in title/description but observation_type signals
  they are typically design-notes documenting past resolutions, not pending issues.
  - id=271 target=D type=design-note — M38 cluster is multi-characteristic under v3_0
  - id=274 target=D type=design-note — sōzō sense-split honoured at sub-group level
  - id=275 target=D type=design-note — ka.phar dual-register honoured at sub-group level

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

VCG `context_description` carried in DB but not in chapter inputs: 45 / 45.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 1512 rows in 1512 scope-groups

| Tier | Total |
|---|---|
| T0 | 96 |
| T1 | 192 |
| T2 | 248 |
| T3 | 264 |
| T4 | 192 |
| T5 | 168 |
| T6 | 192 |
| T7 | 160 |

| Status | Total |
|---|---|
| cluster_synthesis | 189 |
| finding | 1160 |
| gap | 53 |
| silent | 110 |

### Cluster observations: 17 active

| target_phase | status | n |
|---|---|---|
| D | open | 16 |
| Session_D | open | 1 |
