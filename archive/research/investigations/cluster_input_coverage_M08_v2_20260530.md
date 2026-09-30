# Cluster input coverage audit v2 — M08

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M08/inputs/`:
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
| Finding scope-groups | 1134 | 1117 | 901 | NO |
| Sub-groups (non-BOUNDARY) | 8 | 8 | 0 | YES |
| Characteristics | 5 | 5 | 0 | YES |
| VCG codes | 24 | 24 | 0 | YES |
| Anchor verses | 24 | 24 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (901)

By tier: T2=186, T3=198, T4=140, T5=126, T6=131, T7=120

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.1.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Yes. Three verses explicitly name the spirit as a location of C |
| T2.1.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The evidence does not indicate that CHAR-1 originates primarily |
| T2.1.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Spirit-level location in Pro 16:18 (vc=34073, M08-A1-VCG-03) an |
| T2.1.4 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The evidence is not silent: spirit-level location is confirmed  |
| T2.2.1 | T2 | char | Arrogant self-elevation | silent | **[CHAR-1]** S — The verse evidence does not locate CHAR-1 constitutionally in t |
| T2.2.2 | T2 | char | Arrogant self-elevation | silent | **[CHAR-1]** S — Since the verse evidence is silent on CHAR-1 being constitution |
| T2.2.3 | T2 | char | Arrogant self-elevation | silent | **[CHAR-1]** S — The verse evidence is silent on CHAR-1 being constitutionally l |
| T2.3.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Yes, extensively. M08-A1 (30 verses) was constituted specifical |
| T2.3.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Heart-location engages multiple aspects of the heart's integrat |
| T2.3.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Heart-location is extensively confirmed across 30 verses in M08 |
| T2.4.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Yes, in the NT vocabulary specifically. Luk 1:51 (vc=33930, M08 |
| T2.4.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Mind-location reveals that CHAR-1 operates in the cognitive fac |
| T2.4.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Mind-location is confirmed in Luk 1:51 (vc=33930), Psa 10:4 (vc |
| T2.5.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Yes — the spirit (ruach), as confirmed in T2.1. Pro 16:18 (vc=3 |
| T2.5.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The spirit-location (confirmed T2.1) reveals that CHAR-1 penetr |
| T2.5.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Spirit-level location is confirmed. Not silent. |
| T2.6.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Yes, extensively. M08-A2 (11 verses) was constituted by body-pa |
| T2.6.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The body-part links are consistently expressive and indicative: |
| T2.6.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Body-part links are extensively evidenced across eyes, face, he |
| T2.7.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The direction is consistently soul-to-body: the inner pride of  |
| T2.7.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The soul-to-body directionality has two consequences. First, CH |
| T2.7.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Body-characteristic direction confirmed as soul-to-body. Not si |
| T2.8.1 | T2 | char | Arrogant self-elevation | silent | **[CHAR-1]** S — The verse evidence does not explicitly evidence a constitutiona |
| T2.8.2 | T2 | char | Arrogant self-elevation | silent | **[CHAR-1]** S — No verse in the 149-verse corpus supports a physical bodily con |
| T2.8.3 | T2 | char | Arrogant self-elevation | silent | **[CHAR-1]** S — The verse evidence is silent on constitutional body-deposit fro |
| T2.9.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The verse evidence consistently evidences CHAR-1 as generated f |
| T2.9.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The evidence reveals a multiple-but-unified origin. Single gene |
| T2.9.3 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The constitutional origin-site is invariant across contexts: CH |
| T2.10.1 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — Yes. The evidence evidences movement from the deepest constitut |
| T2.10.2 | T2 | char | Arrogant self-elevation | finding | **[CHAR-1]** E — The sequence is evidenced as: interior constitutional origin (h |
| ... | ... | ... | ... | ... | +871 more |

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
| `wa_session_b_findings` (status pending/open) | 11 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 10 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (11)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 16 | boldness | 1 | DIMENSION_REVIEW |
| 42 | delight | 3 | DIMENSION_REVIEW |
| 121 | praise | 1 | DIMENSION_REVIEW |
| 123 | pride | 2 | DIMENSION_REVIEW |
| 142 | self-control | 1 | DIMENSION_REVIEW |
| 173 | will | 2 | DIMENSION_REVIEW |
| 187 | strength | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `DIM-121-001` (reg=121 praise, type=DIMENSION_REVIEW, status=pending) — The doxa/glory sub-cluster ([1047-001] through [1047-004]) in Reg 121 shows glory operating as: (1) supreme inner orientation target, (2) tr
- `DIM-123-001` (reg=123 pride, type=DIMENSION_REVIEW, status=pending) — Registry 123 (pride) carries the most analytically complex dual-register in the cluster: human pride and divine majesty share the same vocab
- `DIM-123-002` (reg=123 pride, type=DIMENSION_REVIEW, status=pending) — Group 26-003 (Paul's paradoxical boasting in weakness — sustained inner act of inverting normal pride to reveal divine power) is analyticall
- `DIM-142-001` (reg=142 self-control, type=DIMENSION_REVIEW, status=pending) — Registry 142 (self-control) shows the self-governance vocabulary operating in three registers: (a) human self-control as character virtue (1
- `DIM-16-001` (reg=16 boldness, type=DIMENSION_REVIEW, status=pending) — parrēsia (G3954/3955) shows a tripartite inner-being structure: (1) access to God in prayer/worship (Spiritual/God-ward, 713-001), (2) apost
- `DIM-173-001` (reg=173 will, type=DIMENSION_REVIEW, status=pending) — The will registry shows the widest dimension spread in C14, spanning Volitional/Will, Theological/Divine-Human, Affective/Emotional, Spiritu
- `DIM-173-002` (reg=173 will, type=DIMENSION_REVIEW, status=pending) — The halakh (to go/walk) groups ([1235-001] through [1235-006]) form a coherent inner-being sub-cluster: inner movement as metaphor for inner
- `DIM-187-001` (reg=187 strength, type=DIMENSION_REVIEW, status=pending) — Group 7013-001 (a.yil, ram) carries a verse-level valuation in which obedience (H8085H sha.ma) and attentive listening (H7181 qashav) are de
- `DIM-42-001` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — The delight vocabulary spans every dimension of the inner being. This breadth suggests delight is not a single category but a family of enga
- `DIM-42-002` (reg=42 delight, type=DIMENSION_REVIEW, status=pending) — H2654A (cha.phets) and H2654B (cha.phats) produce parallel three-group structures with equivalent classifications. Their functional equivale

### Stray research flags (10)

By flag_code: SD_POINTER=10

First 10:
- `SD_POINTER` reg=42 delight (None) — The Theological/Divine-Human cluster within delight/joy registries — God's pleasure/displeasure as the criterion of acceptance — names a str
- `SD_POINTER` reg=42 delight (None) — Morally negative joy/gladness appears across multiple C03 registries: 355-002 and 365-002 (R97), 1096-001 (R132), 634-002 (R186). The same i
- `SD_POINTER` reg=42 delight (None) — Two groups name the inner life as designed toward an end: 378-002 (chara — joy as the goal/completion of the inner life in God) and 6701-001
- `SD_POINTER` reg=42 delight (None) — Group 3090-001 (hēdonē) occupies a counter-position to the positive delight vocabulary. The pleasure/delight tension in the NT — where hēdon
- `SD_POINTER` reg=121 praise (None) — Reg 121 (praise) and Reg 176 (worship) both contain avodah/service/devotion vocabulary and multiple overlapping terms. Session D should asse
- `SD_POINTER` reg=173 will (None) — The inheritance sub-cluster in Reg 173 ([3094-001], [3094-002], [3095-001], [3095-002], [3095-003]) is analytically adjacent to the justice/
- `SD_POINTER` reg=187 strength (None) — Programme-level registry validation gap identified during C20 Dimension Review (2026-04-08). Root cause: STEP Bible treats suffix variants o
- `SD_POINTER` reg=187 strength (None) — The oikos/oikia family in Reg 187 generates groups across at least seven distinct inner-being dimensions (Moral Character, Transformation, A
- `SD_POINTER` reg=187 strength (None) — The AMTS root family (am.mits, am.tsah, o.mets in Reg 187) is closely cognate with the CHAZAQ family (Reg 33/C08) in the biblical courage fo
- `SD_POINTER` reg=187 strength (None) — The directionally-determined pattern appears with particular density in C20 strength vocabulary. The same Hebrew root generates groups in op

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 24 / 24.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 1134 rows in 1134 scope-groups

| Tier | Total |
|---|---|
| T0 | 72 |
| T1 | 144 |
| T2 | 186 |
| T3 | 198 |
| T4 | 144 |
| T5 | 126 |
| T6 | 144 |
| T7 | 120 |

| Status | Total |
|---|---|
| cluster_synthesis | 189 |
| finding | 787 |
| gap | 17 |
| silent | 141 |

### Cluster observations: 5 active

| target_phase | status | n |
|---|---|---|
| phase_9_findings | confirmed | 5 |
