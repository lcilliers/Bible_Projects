# Session B/D pointers — CORRECTED full-linkage assessment

**Generated:** 2026-06-01 (read-only). Supersedes pointer-nolink-retention: that omitted the subsidiary link tables (notably `wa_finding_catalogue_links`). A pointer is genuinely orphaned only if it has NO linkage route at all.

## Subsidiary link tables now included
- `wa_finding_catalogue_links` (6,199) — finding → tier/observation-catalogue question. **2,632/2,883 findings linked.**
- `finding_citation` (75,080) — structured verse/strongs/vcg citations, but for `cluster_finding`/`cluster_observation` (NOT Session B findings).
- `cluster_finding` (21,508) / `cluster_observation` (276) — the cluster-analysis finding layer (own citations).
- `wa_prose_section_citations` — cited_sd_pointer_id (38), cited_finding_id (310).

## wa_session_b_findings (2,883 active) — linkage routes (a finding may have several)

- tier_question: 2631
- verse: 2298
- cluster_link: 2037
- session_c: 336
- sd/related_ref: 86

**Genuinely orphaned findings (NO route at all): 30**

## wa_session_research_flags pointer flags — linkage routes

- cluster_link: 386
- verse: 282
- strongs_ref: 95
- resolved: 93
- prose_cited: 18

**Genuinely orphaned flags (NO route, not resolved): 72**

## Genuinely orphaned — the true set-aside-non-evidenced candidates

### findings

| id | type | status | text |
|---|---|---|---|
| 1245 | DATA_ANOMALY_QA_GAP | open | [v1.8 capture audit] Q&A count 187 < 189 expected. Missing tier_prompt_codes: ['T2.1.4', 'T2.5.3'] |
| 245 | DATA_ANOMALY_FINDING_UNCITED | open | 2 resolved findings have no citation in any current chapter for registry 067: OBS-067-OBS-003, OBS-067-OBS-048 |
| 246 | DATA_ANOMALY_CITATION_GAP | open | Citation FK resolution exceeds 10% threshold in: sb_s2c_ch2: 7/40 unresolved (18%); sb_s2c_ch4: 11/42 unresolved (26%); sb_s2c_ch5: 8/55 unresolved (1… |
| 2704 | DATA_ANOMALY_QA_GAP | open | [v1.8 capture audit] Tiered (T0–T7) prompt coverage 188/189 across all v1.8 captures for R117. This obslog: 187 Q&A entries; cumulative DB coverage. M… |
| 250 | OBSERVATION | open | carry_forward=1. This indicates the registry was carried forward from a prior programme phase. It does not affect analytical scope but is noted as con… |
| 123 | DIMENSION_REVIEW | pending | Reg 114 contains the counter-term to disobedience: [1020-002] names Christ's obedience as the inner act that reverses Adam's. Session B should examine… |
| 122 | DIMENSION_REVIEW | pending | The bondage registry shows a consistent inner-being polarity: enslavement to disordered desires/sin/fear on one side, willing surrender to God/Christ … |
| 137 | DIMENSION_REVIEW | pending | Registry 6 (anointing) spans 7 dimensions across 38 groups — the widest dimensional range in C16. Session B should examine whether this breadth cohere… |
| 131 | DIMENSION_REVIEW | pending | [5696-001] names the Spirit's intercession within the person in wordless groanings — the intersection of the Spirit's inner work and the human inner-b… |
| 28 | DIMENSION_REVIEW | pending | Registry 184 has the highest Theological/Divine-Human density of any C01 registry: 17 of 37 groups (46%) assigned Theological/Divine-Human. Session B:… |
| 132 | DIMENSION_REVIEW | pending | The doxa/glory sub-cluster ([1047-001] through [1047-004]) in Reg 121 shows glory operating as: (1) supreme inner orientation target, (2) transforming… |
| 121 | DIMENSION_REVIEW | pending | Registry 135 shows a consistent human-divine mirroring structure: nearly every human inner-being act (turning, relenting, comforting, recalling) has a… |
| 51 | DIMENSION_REVIEW | pending | Registry 43 (desire) shows a consistent divine/human register split: divine desire, will, and longing = Theological/Divine-Human; human desire and wil… |
| 52 | DIMENSION_REVIEW | pending | Misdirected desire dominates a large segment of Registry 43 — 10+ groups (464-001, 469-001, 480-001, 481-001, 481-003, 492-003, 497-001, 498-001, 504-… |
| 102 | DIMENSION_REVIEW | pending | Group 851-004 ('the impossibility of inner self-knowledge — the heart's moral corruption exceeds human capacity to understand') is a theologically sig… |
| 138 | DIMENSION_REVIEW | pending | Multiple Transformation groups in Reg 6 have GOD as dominant subject (167-001, 179-002, 4697-001, 4701-001, 4701-002). Session B should explore the fu… |
| 72 | DIMENSION_REVIEW | routed_cluster | Two groups (1552-001: fierce anger co-existing with grief/loyalty; 37-003: righteous anger co-existing with sorrow at hardness of heart) show the inne… |
| 110 | DIMENSION_REVIEW | pending | All seven whoredom groups are dominated by spiritual/covenantal whoredom — Israel's heart-departure toward foreign gods. The literal sexual dimension … |
| 2506 | DATA_ANOMALY_QA_GAP | open | [v1.8 capture audit] Tiered (T0-T7) prompt coverage 160/189 (88 Q&A entries; range expansion applied). Missing tier_prompt_codes (29): ['T0.1.3', 'T0.… |
| 140 | DIMENSION_REVIEW | pending | Registry 124 (prophecy) shows a consistent pattern of Agency/Power (Spirit-enabled capacity exercised) alongside Relational Disposition (inner orienta… |
| 69 | DIMENSION_REVIEW | pending | Shame vocabulary in Registry 146 operates on two consistent axes: (a) inner shame as felt condition (affective, moral, spiritual) and (b) shame as soc… |
| 109 | DIMENSION_REVIEW | pending | The slander registry contains three foot-related groups (6253-001: moral life direction; 6253-002: relational submission/devotion; 6256-001: teaching … |
| 87 | DIMENSION_REVIEW | pending | Group 26-003 (Paul's paradoxical boasting in weakness — sustained inner act of inverting normal pride to reveal divine power) is analytically distinct… |
| 74 | DIMENSION_REVIEW | folded | Reg 56 (envy) holds the full positive-negative dual register of the zeal/jealousy vocabulary. The same inner passion (consuming zealous desire) appear… |
| 62 | DIMENSION_REVIEW | routed_cluster | Registry 51 (distress) contains a significant cluster of outlier groups arriving via XREF terms that are outside the suffering domain: 242-001 (medita… |
| 90 | DIMENSION_REVIEW | pending | Group 1374-001 (the sluggard whose desire craves but whose will refuses to act) names sloth's inner-being structure precisely: not the absence of desi… |
| 141 | DIMENSION_REVIEW | pending | The blessing vocabulary reveals a mirror structure in Relational Disposition: group 1299-001 names God's inner disposition of love as the source of hi… |
| 88 | DIMENSION_REVIEW | routed_cluster | The sur (to turn aside) sub-gloss groups in Reg 128 show a consistent pattern: turning aside can be from God (6076-001 — Spiritual/God-ward negative),… |
| 343 | DATA_ANOMALY_OBSERVATION_REGISTER_MISSING | open | Status reverted from Analysis Complete → Pre-Analysis Complete on 2026-04-28. The 2026-04-28 fellowship obslog requested status=Analysis Complete but … |
| 1413 | DATA_ANOMALY_QA_GAP | resolved_qa | [v1.8 capture audit] Q&A count 143 < 203 expected. In-scope: 189 v2 catalogue + 14 Love Extensions = 203. Missing tier_prompt_codes (60): ['T0.4.3', '… |

### flags

| id | code | text |
|---|---|---|
| 426 | SD_POINTER | SP-062-001 — R43 desire (raised in Unit Unit 5) |
| 418 | SD_POINTER | SP-030-001 — R105 (lust) (raised in Unit Unit 2) |
| 420 | SD_POINTER | SP-030-003 — R061 (fear) (raised in Unit Unit 5) |
| 421 | SD_POINTER | SP-030-004 — R123 (pride) (raised in Unit Unit 5) |
| 419 | SD_POINTER | SP-030-002 — R151 (sorrow) and R062 (fellowship) (raised in Unit Unit 5) |
| 464 | SD_POINTER | SP-064-T2-002 — [Catalogue v2 §11 Session-D implication] The constitutional movement sequence (T2.10) — a map for the forgiveness chapter |
| 465 | SD_POINTER | SP-064-T2-003 — [Catalogue v2 §11 Session-D implication] The conscience-resolution framing (T3.9) — a new way to describe forgiveness's deepest functi… |
| 434 | SD_POINTER | SP-064-001 — R122 (prayer) and/or R130 (reconciliation) — or descriptive target: horizontal-vertical worship ordering (raised in Unit Unit 7 Group 537… |
| 466 | SD_POINTER | SP-064-T2-004 — [Catalogue v2 §11 Session-D implication] The grace-mercy-forgiveness dimensional cluster (T6.7) — structural positioning for the C17 s… |
| 467 | SD_POINTER | SP-064-T2-005 — [Catalogue v2 §11 Session-D implication] The threefold eschatological anticipation (T5.6) — eschatological architecture for the forgiv… |
| 480 | SB_FINDING | SB-068-T2-012 — [Catalogue v2 gap surfaced 2026-04-30] T2.8.2 (Body — Deposit) — status S, notation: (none).  Prompt: What evidence supports or contra… |
| 499 | SB_FINDING | SB-068-T2-031 — [Catalogue v2 gap surfaced 2026-04-30] T6.5.2 (Distinctions) — status S, notation: (none).  Prompt: Where apparent overlap exists, wha… |
| 503 | SB_FINDING | SB-068-T2-035 — [Catalogue v2 gap surfaced 2026-04-30] T7.1.8 (Lexical and Semantic Analysis) — status P, notation: Gap identified.  Prompt: What does… |
| 484 | SB_FINDING | SB-068-T2-016 — [Catalogue v2 gap surfaced 2026-04-30] T3.3.3 (Memory) — status S, notation: Gap identified.  Prompt: What does the pattern reveal?  A… |
| 492 | SB_FINDING | SB-068-T2-024 — [Catalogue v2 gap surfaced 2026-04-30] T4.4.3 (Human Interface — Receiving) — status S, notation: (none).  Prompt: What is the inner s… |
| 439 | SD_POINTER | SP-067-023 — [Migrated from catalogue GAP-S3-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where a regist… |
| 245 | SD_POINTER | DIM-111-SD001 — Strength/power/authority/dominion registries (Reg 187/196/197/198/199) share all 4 of mercy dimensions. Structural question: is mercy … |
| 438 | SD_POINTER | SP-067-022 — [Migrated from catalogue GAP-S2-002 2026-04-28 — programme-level methodology question, not a per-word analytical question] Does the verse… |
| 158 | SD_POINTER | DIM-94-SD001 — Reg 94 (intercession), Reg 122 (prayer), and Reg 212 (pray) cover closely related inner-being territory. Session D should assess whethe… |
| 117 | SD_POINTER | DIM-184-SD001 — Registry 184 (spirit) has the highest Theological/Divine-Human concentration in C01 (46%). The human spirit exists primarily in relati… |
| 143 | SD_POINTER | DIM-24-SD001 — The polarity structure of condemnation (verdict/no-verdict) is the governing framework of Reg 24 and maps onto the no-condemnation free… |
| 157 | SD_POINTER | DIM-59-SD001 — Reg 59 (faith) and Reg 163 (trust) share the same inner-being territory — both name the inner disposition of reliance on God. Session D… |
| 114 | SD_POINTER | DIM-112-SD001 — C01 Theological/Divine-Human density: 62 of 297 groups (21%) reflect a structural reality — the primary inner-being terms are constitu… |
| 126 | SD_POINTER | DIM-42-SD004 — Group 3090-001 (hēdonē) occupies a counter-position to the positive delight vocabulary. The pleasure/delight tension in the NT — where … |
| 154 | SD_POINTER | DIM-173-SD001 — The inheritance sub-cluster in Reg 173 ([3094-001], [3094-002], [3095-001], [3095-002], [3095-003]) is analytically adjacent to the ju… |
| 129 | SD_POINTER | DIM-78-SD001 — The trust/refuge vocabulary of Registry 78 (hope) and the desiderative vocabulary of Registry 43 (desire) share the inner-being ground … |
| 152 | SD_POINTER | DIM-137-SD001 — Reg 137 (resolve) has zero verse context groups — no inner-being verse evidence exists for this domain. Session D should assess whethe… |
| 156 | SD_POINTER | DIM-180-SD002 — The water groups ([6836-001] through [6836-008]) cluster around inner transformation, inner thirst/satisfaction, and conscience cleans… |
| 160 | SD_POINTER | DIM-138-SD001 — Reg 138 (reverence) has zero verse context groups — no inner-being verse evidence exists for this domain. The fear-of-God vocabulary (… |
| 533 | SB_FINDING | SB-030-T2-009 — [Catalogue v2 gap surfaced 2026-04-30] T2.4.2 (Mind) — status S, notation: Gap identified.  Prompt: What does mind-location reveal — w… |
| 161 | SD_POINTER | DIM-176-SD001 — Two groups in Reg 176 ([1248-003] and [1249-003]) carry the non-standard automated label Somatic/Embodied. These have been corrected t… |
| 124 | SD_POINTER | DIM-42-SD002 — Morally negative joy/gladness appears across multiple C03 registries: 355-002 and 365-002 (R97), 1096-001 (R132), 634-002 (R186). The s… |
| 127 | SD_POINTER | DIM-8-SD001 — Programme-wide: groups where God is the subject of a volitional or desiderative act are systematically misclassified as Volitional/Will … |
| 638 | SD_POINTER | SP-034-007 — [v1.8 obslog SD pointer] Which other programme registries share each of covenant's eight dimensions? CC should produce the dimensional sh… |
| 128 | SD_POINTER | DIM-43-SD001 — C04 desiderative density is 62% — 65 of 172 groups carry non-desiderative primary content. Question: is the desiderative vocabulary of … |
| 131 | SD_POINTER | DIM-146-SD001 — Registry 146 (shame) and Registry 190 (contempt) are relational inverses in C06: contempt is the inner disposition that assigns worthl… |
| 441 | SD_POINTER | SP-067-025 — [Migrated from catalogue GAP-S4-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where the prog… |
| 447 | SB_FINDING | SB-064-T2-005 — [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status S, notation: Gap identified.  Prompt: If the evidence is silen… |
| 141 | SD_POINTER | DIM-57-SD002 — The Sin & Vice / Moral/Conscience boundary was systematically refined in C11: Sin & Vice = inner condition of moral failure (wickedness… |
| 537 | SB_FINDING | SB-030-T2-013 — [Catalogue v2 gap surfaced 2026-04-30] T2.5.3 (Other Soul Subsets) — status A, notation: Gap identified.  Prompt: If the evidence is s… |
| 148 | SD_POINTER | DIM-98-SD001 — Reg 98 (justice) shows repeated convergence between inner moral quality (Moral/Conscience) and divine action (Theological/Divine-Human)… |
| 123 | SD_POINTER | DIM-42-SD001 — The Theological/Divine-Human cluster within delight/joy registries — God's pleasure/displeasure as the criterion of acceptance — names … |
| 539 | SB_FINDING | SB-030-T2-015 — [Catalogue v2 gap surfaced 2026-04-30] T2.8.2 (Body — Deposit) — status S, notation: Gap identified.  Prompt: What evidence supports o… |
| 540 | SB_FINDING | SB-030-T2-016 — [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status A, notation: Gap identified.  Prompt: If the evidence is silen… |
| 135 | SD_POINTER | DIM-170-SD001 — The weakness-strength reversal (Reg 170: 6642-002, 1219-002) and the boasting-in-weakness posture (Reg 123: 26-003) together form a co… |
| 594 | SB_FINDING | SB-062-T2-014 — [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status A, notation: Gap identified.  Prompt: If the evidence is silen… |
| 216 | SD_POINTER | DIM-068-SD047 — Justice (Reg 98, C13) cooccurrence 7 verses. Grace and justice co-occurring raises the foundational inner-being tension: can a person … |
| 162 | SD_POINTER | DIM-6-SD001 — C16 contains a substantial concentration of GOD-dominant Agency/Power and Transformation groups across anointing, consecration, and bles… |
| 218 | SD_POINTER | DIM-068-SD049 — Appetite (Reg 8, C04) cooccurrence 4 verses. Appetite names the deep inner longing or craving. For Session D: do the 4 co-occurring ve… |
| 140 | SD_POINTER | DIM-57-SD001 — The Affective/Emotional dimension appears extensively in C11 (15 groups assigned) but was absent from C10 assignments, despite groups i… |
| 436 | SD_POINTER | SP-067-020 — [Migrated from catalogue GAP-S1-002 2026-04-28 — programme-level methodology question, not a per-word analytical question] Does the word … |
| 437 | SD_POINTER | SP-067-021 — [Migrated from catalogue GAP-S2-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where the word… |
| 455 | SB_FINDING | SB-064-T2-013 — [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status S, notation: Gap identified.  Prompt: If the evide… |
| 166 | SD_POINTER | DIM-52-SD001 — C18 produces 9 groups assigned Divine-Human Correspondence across division (5), rejection (1), strife (1), and unity (2) — 20% of the c… |
| 575 | SB_FINDING | SB-030-T2-051 — [Catalogue v2 gap surfaced 2026-04-30] T6.7.3 (Dimensional Sharing) — status A, notation: Gap identified.  Prompt: If dimensional shar… |
| 435 | SD_POINTER | SP-067-019 — [Migrated from catalogue GAP-S1-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where the word… |
| 220 | SD_POINTER | DIM-068-SD002 — Seeking (Reg 140) cooccurrence: 40 verses — the strongest cooccurrence signal in the grace registry. Grace and seeking co-occur at a s… |
| 215 | SD_POINTER | DIM-068-SD046 — Desire (Reg 43, C04) cooccurrence 12 verses. Grace and desire co-occur substantively. The inner-being question: is desire the faculty … |
| 534 | SB_FINDING | SB-030-T2-010 — [Catalogue v2 gap surfaced 2026-04-30] T2.4.3 (Mind) — status A, notation: Gap identified.  Prompt: If the evidence is silent on mind-… |
| 591 | SB_FINDING | SB-062-T2-011 — [Catalogue v2 gap surfaced 2026-04-30] T2.5.2 (Other Soul Subsets) — status P, notation: Gap identified.  Prompt: If so, what is that … |
| 225 | SD_POINTER | DIM-068-SD007 — C11 moral failure cluster cooccurrence: evil (57, 12 verses), sin (147, 6 verses), transgression (162, 6 verses), deceit (40, 5 verses… |
| 608 | SB_FINDING | SB-062-T2-028 — [Catalogue v2 gap surfaced 2026-04-30] T6.7.3 (Dimensional Sharing) — status A, notation: Gap identified.  Prompt: If dimensional shar… |
| 571 | SB_FINDING | SB-030-T2-047 — [Catalogue v2 gap surfaced 2026-04-30] T6.5.2 (Distinctions) — status S, notation: Gap identified.  Prompt: Where the evidence shows a… |
| 588 | SB_FINDING | SB-062-T2-008 — [Catalogue v2 gap surfaced 2026-04-30] T1.6.3 (Sustained Effect) — status P, notation: Gap identified.  Prompt: Does the sustained eff… |
| 587 | SB_FINDING | SB-062-T2-007 — [Catalogue v2 gap surfaced 2026-04-30] T1.5.3 (Immediate Response) — status A, notation: Gap identified.  Prompt: Where the verse evid… |
| 568 | SB_FINDING | SB-030-T2-044 — [Catalogue v2 gap surfaced 2026-04-30] T5.6.3 (Eschatological Trajectory) — status A, notation: Gap identified.  Prompt: If the eviden… |
| 228 | SD_POINTER | DIM-068-SD010 — Will (Reg 173, C14) cooccurrence: 11 verses. Grace and will co-occurring across 11 verses raises the foundational inner-being question… |
| 561 | SB_FINDING | SB-030-T2-037 — [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status A, notation: Gap identified.  Prompt: If the evide… |
| 462 | SB_FINDING | SB-064-T2-020 — [Catalogue v2 gap surfaced 2026-04-30] T7.3.3 (Human Science Frameworks) — status S, notation: Gap identified.  Prompt: Where the vers… |
| 169 | SD_POINTER | DIM-19-SD001 — C19 produces 37 of 97 groups (38%) assigned Divine-Human Correspondence — the highest cluster-level concentration in the programme so f… |
| 121 | SD_POINTER | DIM-160-SD001 — Directionally-determined inner faculty pattern — a recurring structural principle identified across C02 registries (108, 127, 160, 174… |
| 232 | SD_POINTER | DIM-068-SD014 — C17 cluster synthesis question: all C17 sibling registries appear in grace's cooccurrence signal — peace (117, 10), kindness (99, 7), … |
