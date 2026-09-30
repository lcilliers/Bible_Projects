# Cluster input coverage audit v2 — M20

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M20/inputs/`:
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
| Finding scope-groups | 525 | 523 | 34 | NO |
| Sub-groups (non-BOUNDARY) | 4 | 4 | 0 | YES |
| Characteristics | 4 | 4 | 0 | YES |
| VCG codes | 23 | 23 | 14 | NO |
| Anchor verses | 23 | 23 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (34)

By tier: T2=5, T3=7, T4=8, T5=6, T6=7, T7=1

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.1.3 | T2 | synth | — | silent | The absence of spirit-level location across the entire cluster is itself a findi |
| T2.1.4 | T2 | synth | — | cluster_synthesis | Spirit-level location is silent across all four sub-groups and all 57 verses. Th |
| T2.3.3 | T2 | synth | — | cluster_synthesis | All four sub-groups have heart-location evidence. No silence.  ---  ### T2.4 — M |
| T2.8.2 | T2 | synth | — | silent | No evidence on bodily deposit from the verse data. |
| T2.8.3 | T2 | synth | — | cluster_synthesis | T2.8 is silent across all four sub-groups. This finding feeds directly into T5.7 |
| T3.4.3 | T3 | synth | — | cluster_synthesis | M20 is a predominantly affective cluster — the characteristics are felt states t |
| T3.5.1 | T3 | synth | — | silent | No M20 term is linked to the creative faculty (imagination, origination) in the  |
| T3.5.2 | T3 | synth | — | cluster_synthesis | S. |
| T3.5.3 | T3 | synth | — | cluster_synthesis | The creative faculty is not engaged by M20 characteristics in the verse evidence |
| T3.6.3 | T3 | synth | — | cluster_synthesis | M20 characteristics are consistently associated with volitional impairment — eac |
| T3.7.3 | T3 | synth | — | cluster_synthesis | M20 characteristics consistently impair agency across all sub-groups. The cluste |
| T3.8.3 | T3 | synth | — | cluster_synthesis | M20 characteristics show consistent adverse effects on moral evaluation: anxiety |
| T4.1.3 | T4 | synth | — | cluster_synthesis | God's disposition toward the M20-experiencing person is consistently one of move |
| T4.1.4 | T4 | synth | — | cluster_synthesis | No silence — God's movement toward the M20-experiencing person is evidenced acro |
| T4.2.3 | T4 | synth | — | cluster_synthesis | Every M20 sub-group has a God-ward resolution: cast onto God (M20-A), rely on Go |
| T4.2.4 | T4 | synth | — | cluster_synthesis | No silence — God-ward movement is present in all four sub-groups.  ---  ### T4.3 |
| T4.5.3 | T4 | synth | — | cluster_synthesis | The relational scope of M20 is wide: within families (athumeō, relational-da.ag) |
| T4.6.2 | T4 | synth | — | silent | No explicit adversarial-spiritual activity is evidenced in the M20 verse data. H |
| T4.6.3 | T4 | synth | — | silent | No angelic mediation is evidenced in the M20 verse data. |
| T4.6.4 | T4 | synth | — | cluster_synthesis | The spiritual beings interface is silent across all four sub-groups in the direc |
| T5.1.3 | T5 | synth | — | cluster_synthesis | No silence — transformation evidence is present in all four sub-groups.  ---  ## |
| T5.2.3 | T5 | synth | — | cluster_synthesis | All four sub-groups have sequencing evidence.  ---  ### T5.3 — Mechanism of Chan |
| T5.4.3 | T5 | synth | — | cluster_synthesis | Suffering and affliction are evidenced across all four sub-groups. No silence.   |
| T5.7.1 | T5 | synth | — | cluster_synthesis | T2.8 found no constitutional bodily deposit from any M20 characteristic. T5.7 is |
| T5.7.2 | T5 | synth | — | silent | No generational consequence is evidenced. |
| T5.7.3 | T5 | synth | — | cluster_synthesis | T2.8 found no deposit across all sub-groups. T5.7 is closed: silent, no deposit, |
| T6.1.3 | T6 | synth | — | cluster_synthesis | All four sub-groups have co-occurrence evidence. No silence.  ---  ### T6.2 — Se |
| T6.2.3 | T6 | synth | — | cluster_synthesis | Sequential relationships are strong across all four sub-groups.  ---  ### T6.3 — |
| T6.3.4 | T6 | synth | — | cluster_synthesis | Causal and constitutive relationships are evidenced across all four sub-groups.  |
| T6.4.4 | T6 | synth | — | cluster_synthesis | Significant vocabulary sharing evidenced in M20-C and M20-D. M20-A and M20-B hav |
| ... | ... | ... | ... | ... | +4 more |

### Missing VCG codes (14)
- `M20-A-NEW-01`
- `2078-001`
- `808-001`
- `M20-C-NEW-01`
- `M20-C-NEW-02`
- `M20-B-NEW-01`
- `M20-B-NEW-02`
- `M20-B-NEW-03`
- `1398-001`
- `1403-001`
- `M20-C-NEW-03`
- `M20-C-NEW-04`
- `M20-C-NEW-05`
- `1288-001`

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
| `wa_session_b_findings` (status pending/open) | 39 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 32 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (39)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 35 | covetousness | 1 | DIMENSION_REVIEW |
| 44 | despair | 1 | DIMENSION_REVIEW |
| 78 | hope | 1 | DIMENSION_REVIEW |
| 112 | mind | 17 | DIMENSIONAL_PATTERN, DIMENSION_REVIEW, ETYMOLOGY, TERM_BEHAVIOUR, THEOLOGICAL_NO |
| 182 | Soul | 13 | DIMENSION_REVIEW, ETYMOLOGY, TERM_BEHAVIOUR, THEOLOGICAL_NOTE, VERSE_PATTERN |
| 183 | heart | 5 | DIMENSIONAL_PATTERN, DIMENSION_REVIEW |
| 191 | doubt | 1 | DIMENSION_REVIEW |

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

### Stray research flags (32)

By flag_code: SD_POINTER=32

First 10:
- `SD_POINTER` reg=78 hope (None) — The trust/refuge vocabulary of Registry 78 (hope) and the desiderative vocabulary of Registry 43 (desire) share the inner-being ground of or
- `SD_POINTER` reg=183 heart (None) — Repentance vocabulary spans Registries 112 (na.cham, metanoia, metanoeo, metamellomai), 182 (na.cham soul-level), and 183 (le.vav circumcisi
- `SD_POINTER` reg=183 heart (None) — God-ward orientation pattern — four groups across three roots and two registries name the characteristic of human inner-being oriented towar
- `SD_POINTER` reg=183 heart (None) — Yearning correspondence — meim 1801-001 names divine yearning (Jer 31:20) and human yearning (Song of Songs 5:4) using the same term. Splagc
- `SD_POINTER` reg=183 heart (None) — Somatic-figurative dimensional split within root families — pattern observed at Phase C r183. Multiple roots show dimensional breadth determ
- `SD_POINTER` reg=183 heart (None) — H3820A lev + H3824 le.vav synthesis candidate. lev cluster: 8 sense-splits covering §7.7 dimensions 02, 03, 04, 05, 05, 11, 11, 11. le.vav c
- `SD_POINTER` reg=35 covetousness (None) — The positive desire vocabulary (prothumia, prothumos, prothumōs) in Reg 35 may have natural affinity with volitional vocabulary elsewhere. T
- `SD_POINTER` reg=182 Soul (G5591) — G5591 psuchikos establishes soul-spirit boundary from within the soul registry. Structural overlap with spirit registry (184) — the soul wit
- `SD_POINTER` reg=182 Soul (H5315L) — H5315L ne.phesh:appetite is a SHARED_TERM with desire registry (043). The soul IS the desiring capacity — ne.phesh and ta.a.vah used in syno
- `SD_POINTER` reg=182 Soul (G5590H) — Mat 10:28 — soul introduced as dimension surviving bodily death in fear context. Soul and fear registries share verse at the intersection of

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 23 / 23.

Findings encapsulate VCG content via the verses they quote and the inline VCG codes. The standalone `context_description` is reference material the AI does not require for prose authoring. Tracked for completeness only.

---

## DB inventory

### Findings

Total active: 525 rows in 525 scope-groups

| Tier | Total |
|---|---|
| T0 | 44 |
| T1 | 94 |
| T2 | 80 |
| T3 | 89 |
| T4 | 46 |
| T5 | 49 |
| T6 | 53 |
| T7 | 70 |

| Status | Total |
|---|---|
| cluster_synthesis | 34 |
| finding | 430 |
| gap | 2 |
| silent | 59 |

### Cluster observations: 0 active

| target_phase | status | n |
|---|---|---|
