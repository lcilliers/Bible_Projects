# Cluster input coverage audit v2 — M03

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: FAIL
- Stray SB / SD findings: PASS

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M03/inputs/`:
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
| Finding scope-groups | 328 | 320 | 75 | NO |
| Sub-groups (non-BOUNDARY) | 8 | 8 | 0 | YES |
| Characteristics | 7 | 7 | 7 | NO |
| VCG codes | 25 | 25 | 0 | YES |
| Anchor verses | 81 | 81 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (75)

By tier: T0=1, T2=12, T3=24, T4=6, T5=8, T6=13, T7=11

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T0.1.3 | T0 | synth | — | silent | The evidence is not silent; the corpus shows grief attributed to God in three di |
| T2.1.2 | T2 | synth | — | silent | The evidence does not indicate that M03's characteristic is primarily spirit-lev |
| T2.2.2 | T2 | synth | — | cluster_synthesis | Soul-level location reveals that grief reaches the innermost personal experience |
| T2.3.1 | T2 | synth | — | cluster_synthesis | Yes, prominently. Heart-location is one of the most frequently evidenced constit |
| T2.3.2 | T2 | synth | — | cluster_synthesis | Heart-location in M03 engages the feeling and integrating function of the heart  |
| T2.5.2 | T2 | synth | — | silent | No additional soul subset beyond heart is evidenced with sufficient specificity  |
| T2.5.3 | T2 | synth | — | silent | The M03 corpus is silent on soul subsets beyond heart for the grief characterist |
| T2.6.1 | T2 | synth | — | cluster_synthesis | Yes, and this is one of M03's most striking features — the body-part linkage is  |
| T2.7.2 | T2 | synth | — | cluster_synthesis | The primarily inner-to-outer direction means that the body's grief expressions ( |
| T2.9.1 | T2 | synth | — | cluster_synthesis | The corpus evidences multiple constitutional origins for grief, varying by sub-g |
| T2.9.2 | T2 | synth | — | cluster_synthesis | The origin is clearly multiple. The corpus evidences four distinct origins: exte |
| T2.9.3 | T2 | synth | — | cluster_synthesis | Yes. In M03-A-VCG-02 (penitential weeping), grief originates from moral self-rec |
| T2.10.2 | T2 | synth | — | cluster_synthesis | Two dominant movement patterns appear. Pattern 1 (Expressive): inner grief condi |
| T3.1.1 | T3 | synth | — | cluster_synthesis | Yes. Several perceptive faculties are engaged. Sight: Elisha's weeping follows a |
| T3.1.2 | T3 | synth | — | cluster_synthesis | Grief deepens moral perception. The conscience-driven sighing of Eze 9:4 (M03-E- |
| T3.1.3 | T3 | synth | — | cluster_synthesis | Grief is a perception-responsive characteristic: it arises when the inner person |
| T3.2.1 | T3 | synth | — | cluster_synthesis | Grief engages cognition in two ways. First, cognitive recognition produces grief |
| T3.2.3 | T3 | synth | — | cluster_synthesis | Grief is not primarily a cognitive characteristic but it has cognitive consequen |
| T3.3.1 | T3 | synth | — | cluster_synthesis | Yes, prominently. Memory is a recurring trigger for grief in M03-A. The exiles'  |
| T3.3.2 | T3 | synth | — | cluster_synthesis | Memory deepens grief: the exile's grief is sustained by and deepened through the |
| T3.3.3 | T3 | synth | — | cluster_synthesis | Grief is memory-sensitive: it is frequently triggered, sustained, and deepened b |
| T3.4.1 | T3 | synth | — | cluster_synthesis | M03 is by far the most affectively concentrated cluster in the programme. Every  |
| T3.4.2 | T3 | synth | — | cluster_synthesis | Grief is itself a form of affect; it does not operate on affect from outside but |
| T3.4.3 | T3 | synth | — | cluster_synthesis | M03 is constitutively affective — it is not a characteristic that engages the af |
| T3.5.3 | T3 | synth | — | cluster_synthesis | Grief generates a specific and distinctive creative form — lament — which is a c |
| T3.6.2 | T3 | synth | — | cluster_synthesis | Four patterns: (1) grief bypassing the will (overwhelming grief where the will i |
| T3.6.3 | T3 | synth | — | cluster_synthesis | The volition-grief relationship is one of the cluster's most analytically signif |
| T3.7.1 | T3 | synth | — | cluster_synthesis | Yes. Grief activates agency in the prayer-deliverance pattern (M03-D-VCG-01): di |
| T3.7.2 | T3 | synth | — | cluster_synthesis | Grief can impair agency: anguish seizing the person so that hands fall helpless  |
| T3.7.3 | T3 | synth | — | cluster_synthesis | Grief's relationship with agency mirrors its relationship with volition. The cha |
| ... | ... | ... | ... | ... | +45 more |

### Missing characteristics (7)
- id=57 — Weeping and tears
- id=58 — Mourning and lamentation
- id=59 — Sorrow and inner grief
- id=60 — Anguish and distress
- id=61 — Groaning and sighing
- id=62 — Pain and inner ache
- id=63 — Bitterness of soul

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

- 28 unresolved `BOUNDARY_DECISION_PENDING` flag(s) for this cluster (of 28 total).

### BOUNDARY inventory

- BOUNDARY sub-group present: no
- BOUNDARY_DECISION_PENDING flags: 28 total, 28 unresolved

Unresolved flags:
- M03-BOUNDARY-G0928G (G0928G) — M03 closure (DIR-20260517-003): BOUNDARY term G0928G (basanizō) reached closure without exit decision. Phase 9 per-term 
- M03-BOUNDARY-G0928H (G0928H) — M03 closure (DIR-20260517-003): BOUNDARY term G0928H (basanizō) reached closure without exit decision. Phase 9 per-term 
- M03-BOUNDARY-G0931 (G0931) — M03 closure (DIR-20260517-003): BOUNDARY term G0931 (basanos) reached closure without exit decision. Phase 9 per-term st
- M03-BOUNDARY-G2346 (G2346) — M03 closure (DIR-20260517-003): BOUNDARY term G2346 (thlibō) reached closure without exit decision. Phase 9 per-term str
- M03-BOUNDARY-G4192 (G4192) — M03 closure (DIR-20260517-003): BOUNDARY term G4192 (ponos) reached closure without exit decision. Phase 9 per-term stru
- M03-BOUNDARY-G4660 (G4660) — M03 closure (DIR-20260517-003): BOUNDARY term G4660 (skullō) reached closure without exit decision. Phase 9 per-term str
- M03-BOUNDARY-G4729 (G4729) — M03 closure (DIR-20260517-003): BOUNDARY term G4729 (stenochōreō) reached closure without exit decision. Phase 9 per-ter
- M03-BOUNDARY-G4841 (G4841) — M03 closure (DIR-20260517-003): BOUNDARY term G4841 (sumpaschō) reached closure without exit decision. Phase 9 per-term 
- M03-BOUNDARY-H1742 (H1742) — M03 closure (DIR-20260517-003): BOUNDARY term H1742 (dav.va) reached closure without exit decision. Phase 9 per-term str
- M03-BOUNDARY-H2254C (H2254C) — M03 closure (DIR-20260517-003): BOUNDARY term H2254C (cha.val) reached closure without exit decision. Phase 9 per-term s
- … +18 more
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

Total active: 360 rows in 328 scope-groups

| Tier | Total |
|---|---|
| T0 | 39 |
| T1 | 33 |
| T2 | 83 |
| T3 | 45 |
| T4 | 60 |
| T5 | 45 |
| T6 | 29 |
| T7 | 26 |

| Status | Total |
|---|---|
| cluster_synthesis | 102 |
| finding | 142 |
| gap | 8 |
| silent | 108 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
