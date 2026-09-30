# Cluster input coverage audit v2 — M04

**Generated:** 2026-05-30 07:39

## Verdict

**Overall: FAIL**

- Coverage: FAIL
- Exclusion: PASS
- BOUNDARY readiness: PASS
- Stray SB / SD findings: FAIL

---

## Inputs audited

7 chapter input file(s) in `Sessions/Session_Clusters/M04/inputs/`:
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
| Finding scope-groups | 1512 | 1491 | 1203 | NO |
| Sub-groups (non-BOUNDARY) | 17 | 17 | 0 | YES |
| Characteristics | 7 | 7 | 0 | YES |
| VCG codes | 47 | 47 | 0 | YES |
| Anchor verses | 73 | 73 | 0 | YES |
| Publication-targeted observations | 0 | 0 | 0 | YES |

### Missing findings (1203)

By tier: T2=248, T3=264, T4=192, T5=168, T6=171, T7=160

| question_code | tier | scope | char | status | preview |
|---|---|---|---|---|---|
| T2.1.1 | T2 | char | Exultation | silent | **[CHAR-1]** S — No verse in M04-A explicitly names the spirit (ruach/pneuma) as |
| T2.1.2 | T2 | char | Exultation | silent | **[CHAR-1]** S — The evidence does not support spirit-level origin for exultatio |
| T2.1.3 | T2 | char | Exultation | silent | **[CHAR-1]** S — Not applicable — spirit-level location is not evidenced in this |
| T2.1.4 | T2 | char | Exultation | silent | **[CHAR-1]** S — The evidence is silent on spirit-level location for exultation. |
| T2.2.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — Yes, explicitly. Psa 35:9 — "my soul will rejoice in the Lord,  |
| T2.2.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — Soul-level location places exultation at the centre of the pers |
| T2.2.3 | T2 | char | Exultation | finding | **[CHAR-1]** E — Soul-level location is not silent; it is explicitly confirmed a |
| T2.3.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — Yes, explicitly and repeatedly. Psa 13:5 — "my heart shall rejo |
| T2.3.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — The heart in OT anthropology is the integrating centre of the p |
| T2.3.3 | T2 | char | Exultation | finding | **[CHAR-1]** E — Heart-location is extensively evidenced; no silence to note. |
| T2.4.1 | T2 | char | Exultation | silent | **[CHAR-1]** S — No verse in the M04-A corpus explicitly names the mind (leb as  |
| T2.4.2 | T2 | char | Exultation | silent | **[CHAR-1]** S — Not directly evidenced. The cognitive element of exultation (kn |
| T2.4.3 | T2 | char | Exultation | silent | **[CHAR-1]** S — The evidence is silent on mind-level location for exultation sp |
| T2.5.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — Yes: the **whole being** (Psa 16:9 — "my whole being rejoices"; |
| T2.5.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — "My whole being" (Psa 16:9) suggests exultation does not remain |
| T2.5.3 | T2 | char | Exultation | finding | **[CHAR-1]** E — Not silent; whole-being location is evidenced at Psa 16:9. |
| T2.6.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — Yes, explicitly. (1) **Bones** — Psa 51:8: "let the bones that  |
| T2.6.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — Three functions are evidenced: (1) **Emphasis** — bones as the  |
| T2.6.3 | T2 | char | Exultation | finding | **[CHAR-1]** E — Body-part links are evidenced at multiple verses. |
| T2.7.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — The primary direction is **inner to outer**: soul exults → mout |
| T2.7.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — The soul-to-body direction shows exultation as fundamentally an |
| T2.7.3 | T2 | char | Exultation | finding | **[CHAR-1]** E — Link is evidenced; see T2.7.1–T2.7.2. |
| T2.8.1 | T2 | char | Exultation | silent | **[CHAR-1]** S — The evidence does not explicitly address constitutional deposit |
| T2.8.2 | T2 | char | Exultation | silent | **[CHAR-1]** S — No supporting evidence for constitutional deposit. The absence  |
| T2.8.3 | T2 | char | Exultation | silent | **[CHAR-1]** S — The evidence is silent on constitutional deposit from sustained |
| T2.9.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — The evidence shows two origin-patterns: (1) **Responsive origin |
| T2.9.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — Multiple origins: both external-responsive (God's acts received |
| T2.9.3 | T2 | char | Exultation | finding | **[CHAR-1]** E — Yes, with a clear pattern: in the Psalms, exultation predominan |
| T2.10.1 | T2 | char | Exultation | finding | **[CHAR-1]** E — Yes. The evidence shows a consistent movement from soul/heart → |
| T2.10.2 | T2 | char | Exultation | finding | **[CHAR-1]** E — The sequence is consistently: inner locus (soul, heart) → expre |
| ... | ... | ... | ... | ... | +1173 more |

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
| `wa_session_b_findings` (status pending/open) | 77 | NO |
| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | 82 | NO |
| `session_d_runs` rows referencing cluster | 0 | YES |

### Stray Session B findings (77)

Grouped by registry:

| Registry | Word | Stray findings | Sample types |
|---|---|---|---|
| 35 | covetousness | 1 | DIMENSION_REVIEW |
| 42 | delight | 3 | DIMENSION_REVIEW |
| 43 | desire | 3 | DIMENSION_REVIEW |
| 67 | goodness | 32 | DATA_ANOMALY_CITATION_GAP, DATA_ANOMALY_FINDING_UNCITED, DATA_ANOMALY_QA_GAP, DI |
| 69 | gratitude | 1 | DIMENSION_REVIEW |
| 97 | joy | 3 | DIMENSION_REVIEW |
| 117 | peace | 31 | DATA_ANOMALY_QA_GAP, DIMENSION_REVIEW, SYNTHESIS_INTER_TIER, SYNTHESIS_INTRA_TIE |
| 186 | gladness | 1 | DIMENSION_REVIEW |
| 187 | strength | 1 | DIMENSION_REVIEW |
| 194 | blessing | 1 | DIMENSION_REVIEW |

First 10 stray Session B findings (by content preview):

- `ANOMALY-067-001` (reg=67 goodness, type=DATA_ANOMALY_FINDING_UNCITED, status=open) — 2 resolved findings have no citation in any current chapter for registry 067: OBS-067-OBS-003, OBS-067-OBS-048
- `ANOMALY-067-002` (reg=67 goodness, type=DATA_ANOMALY_CITATION_GAP, status=open) — Citation FK resolution exceeds 10% threshold in: sb_s2c_ch2: 7/40 unresolved (18%); sb_s2c_ch4: 11/42 unresolved (26%); sb_s2c_ch5: 8/55 unr
- `ANOMALY-067-068` (reg=67 goodness, type=DATA_ANOMALY_QA_GAP, status=open) — [v1.8 capture audit] Q&A count 187 < 189 expected. Missing tier_prompt_codes: ['T2.1.4', 'T2.5.3']
- `ANOMALY-117-002` (reg=117 peace, type=DATA_ANOMALY_QA_GAP, status=open) — [v1.8 capture audit] Tiered (T0–T7) prompt coverage 188/189 across all v1.8 captures for R117. This obslog: 187 Q&A entries; cumulative DB c
- `DIM-117-001` (reg=117 peace, type=DIMENSION_REVIEW, status=pending) — Peace (#117) carries 15 terms with status=extracted_theological_anchor (818 active verses). These are divine names, titles, and eternal/host
- `DIM-117-002` (reg=117 peace, type=DIMENSION_REVIEW, status=pending) — The peace registry's inner-being content is unusually wide — spanning the felt inner state of rest/peace (Emotion — Positive), the inner pos
- `DIM-186-001` (reg=186 gladness, type=DIMENSION_REVIEW, status=pending) — Ya.tav (H3190) produces three materially distinct dimension patterns: Affective/Emotional (merry heart), Moral/Conscience (moral goodness), 
- `DIM-187-001` (reg=187 strength, type=DIMENSION_REVIEW, status=pending) — Group 7013-001 (a.yil, ram) carries a verse-level valuation in which obedience (H8085H sha.ma) and attentive listening (H7181 qashav) are de
- `DIM-194-001` (reg=194 blessing, type=DIMENSION_REVIEW, status=pending) — The blessing vocabulary reveals a mirror structure in Relational Disposition: group 1299-001 names God's inner disposition of love as the so
- `DIM-35-001` (reg=35 covetousness, type=DIMENSION_REVIEW, status=pending) — Reg 35 contains two analytically distinct sub-clusters: (1) willing-spirit/eager-disposition (prothumia, prothumos, prothumōs, euthumeō, eut

### Stray research flags (82)

By flag_code: SB_FINDING=24, SD_POINTER=58

First 10:
- `SD_POINTER` reg=42 delight (None) — The Theological/Divine-Human cluster within delight/joy registries — God's pleasure/displeasure as the criterion of acceptance — names a str
- `SD_POINTER` reg=42 delight (None) — Morally negative joy/gladness appears across multiple C03 registries: 355-002 and 365-002 (R97), 1096-001 (R132), 634-002 (R186). The same i
- `SD_POINTER` reg=42 delight (None) — Two groups name the inner life as designed toward an end: 378-002 (chara — joy as the goal/completion of the inner life in God) and 6701-001
- `SD_POINTER` reg=42 delight (None) — Group 3090-001 (hēdonē) occupies a counter-position to the positive delight vocabulary. The pleasure/delight tension in the NT — where hēdon
- `SD_POINTER` reg=35 covetousness (None) — The positive desire vocabulary (prothumia, prothumos, prothumōs) in Reg 35 may have natural affinity with volitional vocabulary elsewhere. T
- `SD_POINTER` reg=187 strength (None) — Programme-level registry validation gap identified during C20 Dimension Review (2026-04-08). Root cause: STEP Bible treats suffix variants o
- `SD_POINTER` reg=187 strength (None) — The oikos/oikia family in Reg 187 generates groups across at least seven distinct inner-being dimensions (Moral Character, Transformation, A
- `SD_POINTER` reg=187 strength (None) — The AMTS root family (am.mits, am.tsah, o.mets in Reg 187) is closely cognate with the CHAZAQ family (Reg 33/C08) in the biblical courage fo
- `SD_POINTER` reg=187 strength (None) — The directionally-determined pattern appears with particular density in C20 strength vocabulary. The same Hebrew root generates groups in op
- `SD_POINTER` reg=43 desire (None) — C04 desiderative density is 62% — 65 of 172 groups carry non-desiderative primary content. Question: is the desiderative vocabulary of Scrip

---

## E. Informational (not gating)

VCG `context_description` carried in DB but not in chapter inputs: 47 / 47.

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
| finding | 1231 |
| gap | 21 |
| silent | 71 |

### Cluster observations: 4 active

| target_phase | status | n |
|---|---|---|
| phase_9_findings | confirmed | 4 |
