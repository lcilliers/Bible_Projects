# Cluster input coverage audit v2 — M06

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: FAIL
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M06/inputs/`:
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
| Finding scope-groups | 1512 | 1511 | 0 | YES |
| Sub-groups (non-BOUNDARY) | 7 | 7 | 0 | YES |
| Characteristics | 7 | 7 | 0 | YES |
| VCG codes | 51 | 51 | 27 | NO |
| Anchor verses | 57 | 57 | 5 | NO |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing VCG codes (27)
- `14-001`
- `90-001`
- `1568-001`
- `5179-001`
- `1643-001`
- `903-001`
- `5518-001`
- `902-002`
- `550-001`
- `902-003`
- `902-001`
- `3200-001`
- `550-NEW-04`
- `550-NEW-03`
- `1663-001`
- `337-001`
- `339-001`
- `339-002`
- `317-001`
- `7009-001`
- `6968-001`
- `7001-001`
- `1275-001`
- `550-002`
- `5519-001`
- `247-002`
- `1663-NEW-04`

### Missing anchor verses (5)
- `1643-001` — 1 anchor(s)
- `339-002` — 1 anchor(s)
- `550-002` — 1 anchor(s)
- `550-NEW-01` — 1 anchor(s)
- `90-001` — 1 anchor(s)

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

- BOUNDARY sub-group `Boundary/expression` has active members (verses=56, terms=4, VCGs=5). Resolve before publishing.

### BOUNDARY inventory

- BOUNDARY sub-group present: YES — Boundary/expression
  - active verses: 56
  - active terms: 4
  - active VCGs: 5
- BOUNDARY_DECISION_PENDING flags: 0 total, 0 unresolved
- BOUNDARY mentions in cluster_observation (informational only — not gating): 0

---

## D. Stray Session B / Session D findings

Cluster must have no still-floating analytical findings from prior Session B / Session D work on its contributing registries.

| Source | Count | Pass |
|---|---|---|
| `wa_session_b_findings` (status pending/open) | 7 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 8 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (7)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 65 | generosity | 1 | DIMENSION_REVIEW |
| 98 | justice | 3 | DIMENSION_REVIEW |
| 146 | shame | 1 | DIMENSION_REVIEW |
| 187 | strength | 1 | DIMENSION_REVIEW |
| 190 | contempt | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `DIM-146-001` (reg=146 shame, type=DIMENSION_REVIEW, status=pending) — Shame vocabulary in Registry 146 operates on two consistent axes: (a) inner shame as felt condition (affective, moral, spiritual) and (b) sh
- `DIM-187-001` (reg=187 strength, type=DIMENSION_REVIEW, status=pending) — Group 7013-001 (a.yil, ram) carries a verse-level valuation in which obedience (H8085H sha.ma) and attentive listening (H7181 qashav) are de
- `DIM-190-001` (reg=190 contempt, type=DIMENSION_REVIEW, status=pending) — Contempt vocabulary in Registry 190 operates at three levels: (a) the inner disposition of contempt as evaluative stance (Character/Disposit
- `DIM-65-001` (reg=65 generosity, type=DIMENSION_REVIEW, status=pending) — agathos (G0018) groups in Reg 65 frame the inner being's relationship to goodness in four registers: (1) goodness as character source (good 
- `DIM-98-001` (reg=98 justice, type=DIMENSION_REVIEW, status=pending) — H4941G mish.pat (Reg 98) and H4941H mish.pat (Reg 24) are the same Hebrew term across two registries: five groups in Reg 98 and three groups
- `DIM-98-002` (reg=98 justice, type=DIMENSION_REVIEW, status=pending) — The dikaios/dikaiosunē/dikaiōsis/dikaioō family (G1342, G1343, G1344, G1347) shows a consistent tension: righteousness as divine act/attribu
- `DIM-98-003` (reg=98 justice, type=DIMENSION_REVIEW, status=pending) — H6664G tsedeq and H6663 tsadeq produce four distinct groups: (1) human inner quality [942-001], (2) divine attribute [942-002], (3) pursued 

### Stray research flags (8)

By flag_code: SD_POINTER=8

First 10:
- `SD_POINTER` reg=75 hatred (None) — Group 902-003 (sin.ah: hatred listed alongside love and envy as constitutive inner orientations of the person that cease at death) makes an 
- `SD_POINTER` reg=146 shame (None) — Registry 146 (shame) and Registry 190 (contempt) are relational inverses in C06: contempt is the inner disposition that assigns worthlessnes
- `SD_POINTER` reg=187 strength (None) — Programme-level registry validation gap identified during C20 Dimension Review (2026-04-08). Root cause: STEP Bible treats suffix variants o
- `SD_POINTER` reg=187 strength (None) — The oikos/oikia family in Reg 187 generates groups across at least seven distinct inner-being dimensions (Moral Character, Transformation, A
- `SD_POINTER` reg=187 strength (None) — The AMTS root family (am.mits, am.tsah, o.mets in Reg 187) is closely cognate with the CHAZAQ family (Reg 33/C08) in the biblical courage fo
- `SD_POINTER` reg=187 strength (None) — The directionally-determined pattern appears with particular density in C20 strength vocabulary. The same Hebrew root generates groups in op
- `SD_POINTER` reg=98 justice (None) — Reg 98 (justice) shows repeated convergence between inner moral quality (Moral/Conscience) and divine action (Theological/Divine-Human) — pa
- `SD_POINTER` reg=98 justice (None) — Two groups in Reg 98 — [3186-001] H0197H ulam (Hall of Justice) and [3188-001] H0197I ulam (Hall of Throne) — are QA-EXTERNALISED: they desc

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 51 / 51.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 1516 rows in 1512 scope-groups

| Tier | Total |
|---|---|
| T0 | 97 |
| T1 | 194 |
| T2 | 249 |
| T3 | 264 |
| T4 | 192 |
| T5 | 168 |
| T6 | 192 |
| T7 | 160 |

| Status | Total |
|---|---|
| cluster_synthesis | 31 |
| finding | 1483 |
| gap | 1 |
| silent | 1 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
