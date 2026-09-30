# Cluster input coverage audit v2 — M15

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: FAIL
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M15/inputs/`:
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
| Finding scope-groups | 1701 | 1692 | 1 | NO |
| Sub-groups (non-BOUNDARY) | 8 | 8 | 0 | YES |
| Characteristics | 8 | 8 | 0 | YES |
| VCG codes | 58 | 58 | 4 | NO |
| Anchor verses | 55 | 55 | 1 | NO |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (1)

By tier: T7=1

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T7.1.8 | T7 | synth | — | finding | [BOUNDARY — structural characterisation note only; full catalogue pass not appli |

### Missing VCG codes (4)
- `M15-BOUNDARY-VCG01`
- `523-002`
- `528-001`
- `525-001`

### Missing anchor verses (1)
- `M15-BOUNDARY-VCG01` — 1 anchor(s)

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

- BOUNDARY sub-group `Functional, supporting, and cluster-reassignment candidates` has active members (verses=14, terms=13, VCGs=1). Resolve before publishing.

### BOUNDARY inventory

- BOUNDARY sub-group present: YES — Functional, supporting, and cluster-reassignment candidates
  - active verses: 14
  - active terms: 13
  - active VCGs: 1
- BOUNDARY_DECISION_PENDING flags: 0 total, 0 unresolved
- BOUNDARY mentions in cluster_observation (informational only — not gating): 0

---

## D. Stray Session B / Session D findings

Cluster must have no still-floating analytical findings from prior Session B / Session D work on its contributing registries.

| Source | Count | Pass |
|---|---|---|
| `wa_session_b_findings` (status pending/open) | 35 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 31 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (35)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 26 | conscience | 1 | DIMENSION_REVIEW |
| 43 | desire | 3 | DIMENSION_REVIEW |
| 52 | division | 3 | DIMENSION_REVIEW |
| 57 | evil | 2 | DIMENSION_REVIEW |
| 112 | mind | 17 | DIMENSIONAL_PATTERN, DIMENSION_REVIEW, ETYMOLOGY, TERM_BEHAVIOUR, THEOLOGICAL_NO |
| 127 | reasoning | 1 | DIMENSION_REVIEW |
| 149 | slander | 1 | DIMENSION_REVIEW |
| 160 | thought | 1 | DIMENSION_REVIEW |
| 174 | wisdom | 1 | DIMENSION_REVIEW |
| 187 | strength | 1 | DIMENSION_REVIEW |
| 191 | doubt | 1 | DIMENSION_REVIEW |
| 201 | image | 2 | DIMENSION_REVIEW |
| 206 | vulnerability | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `112-F001` (reg=112 mind, type=TERM_BEHAVIOUR, status=pending) — Memory in biblical vocabulary is an active, covenantal, morally significant act — not passive cognitive retrieval. God's remembering produce
- `112-F002` (reg=112 mind, type=THEOLOGICAL_NOTE, status=pending) — The mind is a moral organ before it is an intellectual one. It can be debased, blinded, corrupted, renewed, and transferred (mind of Christ)
- `112-F003` (reg=112 mind, type=ETYMOLOGY, status=pending) — The ye.tser (formed inclination) is the OT anthropology's closest approach to a foundational moral disposition. Gen 6:5 and 8:21 establish i
- `112-F004` (reg=112 mind, type=VERSE_PATTERN, status=pending) — The cha.shav root documents that the same mental faculty produces artistic design, moral reasoning, and malicious plotting — there is no sep
- `112-F005` (reg=112 mind, type=THEOLOGICAL_NOTE, status=pending) — Fronēma (the set mindset) in Romans 8:5-7 is the determinative factor for life or death, peace or enmity with God — making the mind's fundam
- `112-F006` (reg=112 mind, type=THEOLOGICAL_NOTE, status=pending) — Suneidēsis (conscience) is the NT's distinctive contribution with no direct Hebrew equivalent. The conscience can be weak, clear, seared, or
- `112-F007` (reg=112 mind, type=VERSE_PATTERN, status=pending) — Deu 4:9 functionally links the sha.mar attentiveness cluster with the za.khar memory cluster: vigilant attentiveness is the means by which m
- `112-F008` (reg=112 mind, type=TERM_BEHAVIOUR, status=pending) — The 1 Cor 14:14-15 nous/pneuma distinction is the sharpest NT terminological boundary between mind-level and spirit-level inner operation — 
- `112-F009` (reg=112 mind, type=VERSE_PATTERN, status=pending) — Double-mindedness (dipsuchos/se.eph) documents inner division as a cross-testament pathology. James presents inner unity as a condition for 
- `112-F010` (reg=112 mind, type=THEOLOGICAL_NOTE, status=pending) — The Hebrews new covenant quotation (Heb 8:10; 10:16) names both dianoia (mind) and kardia (heart) as sites of internalized law — anticipatin

### Stray research flags (31)

By flag_code: SB_FINDING=2, SD_POINTER=29

First 10:
- `SD_POINTER` reg=112 mind (G3340) — G3340 metanoeō, G3341 metanoia, G3338 metamellomai, and H5162H na.cham (relent) all present in Reg 112 and Reg 135 (repentance). Structural 
- `SD_POINTER` reg=112 mind (H5162G) — H5162G na.cham (comfort) likely shared with Reg 071 (grief) and Reg 135. Na.cham root operates across mind-change (112), comfort of the grie
- `SD_POINTER` reg=112 mind (H5068) — H5068 na.dav (willing) likely shared with desire and will registries. Volitional inner movement of na.dav borders desire and will clusters.
- `SD_POINTER` reg=112 mind (G4893) — G4893 suneidēsis has no Hebrew counterpart in this registry. Intersection with heart (183) and spirit (184) registries for Session D investi
- `SD_POINTER` reg=112 mind (H8104G) — H8104G sha.mar/obey (195v) has significant overlap with will/obedience registries. Cross-registry boundary review recommended — may belong p
- `SD_POINTER` reg=112 mind (G1271) — Heb 8:10 and 10:16 name both dianoia (mind) and kardia (heart) as sites of new covenant law-writing. Structural overlap between Reg 112 and 
- `SD_POINTER` reg=112 mind (H2142) — H2142 za.khar operates across memory, worship, and ritual domains. Possible overlap with worship or praise registries (1 Chr 16:4 Levitical 
- `SD_POINTER` reg=112 mind (G3340) — Spirit-mind distinction in 1 Cor 14:14-15 is the sharpest NT terminological boundary between nous and pneuma. Session D: map against Reg 184
- `SD_POINTER` reg=112 mind (H3336) — Ye.tser (formed inclination) in Gen 6:5 and 8:21 is the OT closest equivalent to fundamental moral disposition. Session D: relationship betw
- `SD_POINTER` reg=112 mind (G5426) — 1 Cor 2:16 and Phil 2:5 present mind-orientation as transferable through participation in Christ. Key integration point for transformation o

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 58 / 58.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 1724 rows in 1701 scope-groups

| Tier | Total |
|---|---|
| T0 | 111 |
| T1 | 218 |
| T2 | 292 |
| T3 | 297 |
| T4 | 216 |
| T5 | 189 |
| T6 | 221 |
| T7 | 180 |

| Status | Total |
|---|---|
| cluster_synthesis | 23 |
| finding | 1454 |
| gap | 9 |
| silent | 238 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
