# No-link pointers — retention / close inspection (step a)

> **⚠ SUPERSEDED by [pointer-full-linkage-20260601.md](pointer-full-linkage-20260601.md).** This doc judged "no link" on `cluster_link` + verse only, and **omitted the subsidiary link tables** (`wa_finding_catalogue_links` tier-question links, etc.). 781 of the 846 "no-link" findings here are in fact tier-question-linked. The genuinely orphaned set is **30 findings + 72 flags**, not the counts below. Kept for history only.

**Generated:** 2026-06-01 (read-only). `cluster_link IS NULL` = no named-term link to a cluster. Split so evidenced items are NOT closed as 'non-evidenced'.

## Summary

- **wa_session_b_findings no-link: 846** → truly non-evidenced **183** · verse-evidenced (keep/decide) **663**
- **pointer flags no-link: 168** → truly non-evidenced **78** · has strongs-ref/verse (keep/decide) **90**

**Clean set-aside-non-evidenced candidates = the 'truly non-evidenced' rows** (no term, no verse). The verse-evidenced rows have evidence but no named subject term — closing them as non-evidenced would be wrong; they need a separate call (route via verse as last resort, or hold).

finding_type of truly-non-evidenced findings: OBSERVATION=116, SYNTHESIS_INTER_TIER=25, DIMENSION_REVIEW=22, SPIRIT_SOUL_BODY=7, DATA_ANOMALY_QA_GAP=4, SYNTHESIS_INTRA_TIER=3, CROSS_REGISTRY=2, DATA_ANOMALY_FINDING_UNCITED=1, DATA_ANOMALY_CITATION_GAP=1, DATA_ANOMALY_OBSERVATION_REGISTER_MISSING=1, MEANING_OBSERVATION=1

## Truly non-evidenced — wa_session_b_findings (clean close candidates)

| id | type | status | text |
|---|---|---|---|
| 524 | OBSERVATION | pending |  |
| 527 | OBSERVATION | pending |  |
| 578 | OBSERVATION | pending |  |
| 583 | OBSERVATION | pending |  |
| 584 | OBSERVATION | pending |  |
| 612 | OBSERVATION | pending |  |
| 620 | OBSERVATION | pending | *Gap identified.* |
| 209 | OBSERVATION | resolved_qa | 884-008 NULL — volitional preference; likely Volition (04) candidate |
| 217 | OBSERVATION | resolved_qa | DIM-67-001: core analytical question — distinct phenomena vs unified category |
| 208 | OBSERVATION | resolved_qa | 884-007 NULL — creation pronouncement; no existing dimension label fits cleanly |
| 2100 | SPIRIT_SOUL_BODY | resolved_qa | T2.8.1 data was silent on constitutional body deposit. T5.7 is formally closed. |
| 207 | OBSERVATION | resolved_qa | Cognition (03) assigned to 884-004 and 884-006 — both evaluative judgment groups |
| 214 | OBSERVATION | resolved_qa | Co-occurrence: R103 (love, 23) > R43 (desire, 18) > R197 (authority, 17) as top 3 |
| 197 | OBSERVATION | resolved_qa | Registry-level dimension = Moral/Conscience; groups show wider spread — tension noted |
| 218 | OBSERVATION | resolved_qa | DIM-67-001 uses pre-v1.4 dimension vocabulary; needs re-reading against current labels |
| 226 | OBSERVATION | resolved_qa | 884-004 anchors rank inner qualities above external power — structural normative claim |
| 232 | OBSERVATION | resolved_qa | 884-007 dimension NULL reinforced — needs a divine creative/evaluative agency category |
| 213 | OBSERVATION | resolved_qa | R103 (love) deepest structural XREF link; R42 (delight) Hebrew-only; R99 (kindness) Greek |
| 215 | OBSERVATION | resolved_qa | R197 (authority) unexpectedly high — likely driven by 884-008 volitional-preference idiom |
| 219 | OBSERVATION | resolved_qa | SBF-VCB013-001: tripartite model confirmed; OBS-010 extends distortion pole etymologically |
| 196 | OBSERVATION | resolved_qa | Registry description names 3 axes: aesthetic/moral/relational; human goodness is derivative |
| 2035 | SPIRIT_SOUL_BODY | resolved_qa | Evidence is silent on constitutional body deposit from forgiveness. T5.7 to close formally. |
| 234 | OBSERVATION | resolved_qa | 884-008 NULL likely = Volition (04) — group description explicitly names choosing/preferring |
| 1245 | DATA_ANOMALY_QA_GAP | open | [v1.8 capture audit] Q&A count 187 < 189 expected. Missing tier_prompt_codes: ['T2.1.4', 'T2.5.3'] |
| 1866 | OBSERVATION | resolved_qa | Verse evidence is largely silent on explicit memory faculty engagement with fellowship. Gap noted. |
| 202 | OBSERVATION | resolved_qa | TOV root family distributed across R67 (adjectival), R65 (active doing), R103 (relational-affective) |
| 245 | DATA_ANOMALY_FINDING_UNCITED | open | 2 resolved findings have no citation in any current chapter for registry 067: OBS-067-OBS-003, OBS-067-OBS-048 |
| 244 | OBSERVATION | resolved_qa | SBF-VCB013-001 confirmed and extended: presence/absence holds for full registry; distortion etymological not textual |
| 1855 | OBSERVATION | resolved_qa | Yes — origin shifts across modes: divine → human → existential, corresponding to the ontological → companionship → existential mode levels. OBS-062-01… |
| 246 | DATA_ANOMALY_CITATION_GAP | open | Citation FK resolution exceeds 10% threshold in: sb_s2c_ch2: 7/40 unresolved (18%); sb_s2c_ch4: 11/42 unresolved (26%); sb_s2c_ch5: 8/55 unresolved (1… |
| 1843 | SPIRIT_SOUL_BODY | resolved_qa | Verse evidence is largely silent on explicit mind-location. The cognitive dimension is implied (discernment of fellowship object) but not named. Gap n… |
| 888 | OBSERVATION | pending | T2.8 found no body deposit. T5.7 is formally closed. All three prompts in this component are not applicable on the basis of the T2.8 finding. This clo… |
| 1854 | OBSERVATION | resolved_qa | Multiple — three distinct origin points as evidenced in Q&A-062: divine initiative, human volitional alignment, existential given. The origin differs … |
| 2704 | DATA_ANOMALY_QA_GAP | open | [v1.8 capture audit] Tiered (T0–T7) prompt coverage 188/189 across all v1.8 captures for R117. This obslog: 187 Q&A entries; cumulative DB coverage. M… |
| 1919 | OBSERVATION | resolved_qa | Generational consequence: not evidenced from this registry's anchor verses. The fellowship formations described are personal and corporate, not explic… |
| 1830 | OBSERVATION | resolved_qa | Primary dimension: Relational Disposition — confirmed. Fellowship is fundamentally about orientation and participation in relation. The person is orie… |
| 514 | OBSERVATION | pending | Relational Disposition — confirmed in the registry header (dimensions = "Relational/Social"), dim_review_status = "Complete." The dominant_subject for… |
| 2015 | OBSERVATION | resolved_qa | Primary dimension: Relational Disposition — confirmed by v1 analysis (10/14 groups). Forgiveness is fundamentally a relational act — the release of a … |
| 2024 | SPIRIT_SOUL_BODY | resolved_qa | Verse evidence is largely silent on explicit soul-faculty naming for forgiveness. Gap noted — the soul-level engagement is inferred from the guilt-for… |
| 1933 | OBSERVATION | resolved_qa | Fellowship vs unity: kind distinction. Fellowship vs covenant: layer distinction (legal vs experiential). Fellowship vs desire: sequential/directional… |
| 1045 | OBSERVATION | pending | **No vocabulary sharing at the term level is evidenced (shared_term_count = 0, term_sharing_ratio = 0.0).** The closing condition applies at the term-… |
| 830 | OBSERVATION | pending | The evidence is silent on body deposit. No constitutional somatic deposit from sustained contrition is evidenced in the registry data. **T5.7 (Deposit… |
| 825 | OBSERVATION | pending | The evidence is silent on soul-subset locations beyond spirit, heart, and soul (*nefesh*). No faculty-specific terms (will, conscience, memory, affect… |
| 1852 | SPIRIT_SOUL_BODY | resolved_qa | The evidence is partially silent — the wound-mark persists physically, but whether this constitutes a programme-relevant constitutional body deposit i… |
| 250 | OBSERVATION | open | carry_forward=1. This indicates the registry was carried forward from a prior programme phase. It does not affect analytical scope but is noted as con… |
| 2113 | OBSERVATION | resolved_qa | Forgiveness vs guilt: kind (condition vs remedy). Forgiveness vs mercy: layer (disposition vs act). Forgiveness vs repentance: sequential (access-post… |
| 123 | DIMENSION_REVIEW | pending | Reg 114 contains the counter-term to disobedience: [1020-002] names Christ's obedience as the inner act that reverses Adam's. Session B should examine… |
| 969 | OBSERVATION | pending | **The evidence is silent on constitutional bodily deposit for fellowship.** This conclusion feeds into T5.7: the T5.7 Deposit Consequence prompts will… |
| 1884 | OBSERVATION | resolved_qa | Fellowship is a primary vehicle of conscientiousness formation — the community one fellowships with shapes the moral seriousness and integrated moral … |
| 814 | OBSERVATION | pending | **Dependence / Creatureliness** — confirmed as the primary dimension by Dimension Review. 5 of 9 groups carry this dimension: 7552-003, 7553-001, 7554… |
| 2021 | SPIRIT_SOUL_BODY | resolved_qa | The verse evidence is largely silent on explicit spirit-faculty naming as the primary locus of forgiveness. The Spirit is involved in the authority to… |
| 1911 | OBSERVATION | resolved_qa | Yes — the companionship/habituation mechanism (Mechanism 1) and the wound-as-cleansing mechanism (Mechanism 2) are distinct. Mechanism 1 is gradual an… |
| 2051 | OBSERVATION | resolved_qa | The pattern reveals affect as simultaneously prerequisite (compassion enabling the act) and product (love and reverence as downstream states) of forgi… |
| 1860 | OBSERVATION | resolved_qa | The pattern reveals perception as a prerequisite for rightly directed fellowship and a casualty of misdirected fellowship. The person who fellowships … |
| 1881 | OBSERVATION | resolved_qa | Conscience is the moral sensitivity that enables the initial distinction between right and wrong fellowship objects; fellowship then either deepens or… |
| 122 | DIMENSION_REVIEW | pending | The bondage registry shows a consistent inner-being polarity: enslavement to disordered desires/sin/fear on one side, willing surrender to God/Christ … |
| 2023 | SPIRIT_SOUL_BODY | resolved_qa | If guilt (R073 — 51 shared verses, strongest co-occurrence signal) operates at the soul level, then forgiveness — which addresses guilt — necessarily … |
| 249 | OBSERVATION | resolved_qa | sb_classification is NULL. The absence of a prior sb_classification means Stage 2b must produce a spirit-soul-body finding from first principles. The … |
| 597 | OBSERVATION | pending | From Section 5 of the data: seeking (R140: 40 verses), strength (R187: 15), love (R103: 14), desire (R043: 12), evil (R057: 12), will (R173: 11), call… |
| 2354 | CROSS_REGISTRY | resolved_qa | Precise dimensional sharing counts require CC database query. The inferred pattern (covenant shares dimensions with the widest range of registries due… |
| 1920 | OBSERVATION | resolved_qa | T2.8 found ambiguous evidence — the wound mark is a physical persisting trace but whether it constitutes a programme-relevant constitutional deposit i… |
| 656 | OBSERVATION | routed_cluster | The verse evidence is silent on the immediate inner-being response of the *receiver* of compassion. This silence is noted and flagged as a new gap for… |
| 137 | DIMENSION_REVIEW | pending | Registry 6 (anointing) spans 7 dimensions across 38 groups — the widest dimensional range in C16. Session B should examine whether this breadth cohere… |
| 2057 | OBSERVATION | resolved_qa | Agency is both exercised (in forgiving) and liberated (in receiving forgiveness). The pattern: forgiveness frees the agency of the forgiven person for… |
| 131 | DIMENSION_REVIEW | pending | [5696-001] names the Spirit's intercession within the person in wordless groanings — the intersection of the Spirit's inner work and the human inner-b… |
| 1869 | OBSERVATION | resolved_qa | Fellowship is constitutively affective — it is not a purely cognitive or volitional alignment but a genuine sharing in the affective reality of the fe… |
| 1887 | OBSERVATION | resolved_qa | Relational capacity is both the vehicle and the product of fellowship. The pattern reveals: fellowship requires relational capacity to begin; it deepe… |
| 2060 | OBSERVATION | resolved_qa | The pattern: forgiveness requires the most precise moral evaluation the inner being is capable of — accurate assessment of what was owed, what is bein… |
| 2117 | OBSERVATION | resolved_qa | The Relational Disposition primary dimension shared with mercy (R111) and love (R103) positions forgiveness within the relational triad operating in C… |
| 2063 | OBSERVATION | resolved_qa | Conscience is both the faculty that makes forgiveness necessary (by delivering the guilt-verdict) and the primary beneficiary of forgiveness received … |
| 2093 | OBSERVATION | resolved_qa | The mechanisms differ across modes: covenantal-objective mode uses the ritual-atonement mechanism (external, structural). Divine relational-personal m… |
| 28 | DIMENSION_REVIEW | pending | Registry 184 has the highest Theological/Divine-Human density of any C01 registry: 17 of 37 groups (46%) assigned Theological/Divine-Human. Session B:… |
| 132 | DIMENSION_REVIEW | pending | The doxa/glory sub-cluster ([1047-001] through [1047-004]) in Reg 121 shows glory operating as: (1) supreme inner orientation target, (2) transforming… |
| 248 | OBSERVATION | resolved_qa | The registry note references repentance (#135) and brokenness (#18) as related registries. The registry description places contrition between these — … |
| 543 | OBSERVATION | pending | Enables a specific form: the grace-inference (SD029). SD048 raises the question of whether right thinking about grace is itself grace-enabled — implyi… |
| 764 | OBSERVATION | routed_cluster | Dimensional sharing data is not yet available in the programme database (dimensions field = None). The analysis above represents inferences from the s… |
| 121 | DIMENSION_REVIEW | pending | Registry 135 shows a consistent human-divine mirroring structure: nearly every human inner-being act (turning, relenting, comforting, recalling) has a… |
| 971 | OBSERVATION | pending | The origin is definitively multiple. Finding 062-ORIG-001 confirms: "both divine initiative and human response generate fellowship." The data establis… |
| 51 | DIMENSION_REVIEW | pending | Registry 43 (desire) shows a consistent divine/human register split: divine desire, will, and longing = Theological/Divine-Human; human desire and wil… |
| 52 | DIMENSION_REVIEW | pending | Misdirected desire dominates a large segment of Registry 43 — 10+ groups (464-001, 469-001, 480-001, 481-001, 481-003, 492-003, 497-001, 498-001, 504-… |
| 905 | OBSERVATION | pending | Full programme-wide dimensional distribution data is not available in the current session. The dimensional sharing analysis above is based on named re… |
| 1863 | OBSERVATION | resolved_qa | The pattern reveals cognition as both prerequisite for and product of fellowship direction — initial cognitive discernment enables right fellowship; h… |
| 271 | OBSERVATION | resolved_qa | The three Emotion — Negative groups describe a different register: suffering anguish (7552-001), corporate desolation (7554-002), and inner terror/pan… |
| 269 | OBSERVATION | resolved_qa | Dimension distribution: - Dimension 10 — Dependence / Creatureliness: 5 groups (7552-003, 7553-001, 7557-001, 7554-001, 7555-001) - Dimension 02 — Emo… |
| 1878 | OBSERVATION | resolved_qa | Moral evaluation and fellowship direction are mutually determining: accurate moral evaluation directs fellowship rightly; right fellowship deepens mor… |
| 557 | OBSERVATION | pending | Grace produces moral clarity — sharpening rather than blunting moral awareness. The person who recognises grace has made a moral evaluation: they know… |
| 1937 | OBSERVATION | resolved_qa | The Relational Disposition primary dimension shared with love and mercy positions fellowship as one of the relational triad (love, mercy, fellowship) … |
| 1052 | OBSERVATION | pending | **Programme-wide dimensional sharing data is not available in this session.** The fellowship registry's own dimensions are known, but which other regi… |
| 532 | OBSERVATION | pending | Grace is a whole-person phenomenon. The body is integral to its operation — not merely an occasional expression. Grace cannot be adequately described … |
| 102 | DIMENSION_REVIEW | pending | Group 851-004 ('the impossibility of inner self-knowledge — the heart's moral corruption exceeds human capacity to understand') is a theologically sig… |
| 544 | OBSERVATION | pending | Grace produces a particular cognitive form — reasoned assurance, not merely experienced certainty. Grace can be the ground of inner confidence even wh… |
| 824 | OBSERVATION | pending | The evidence is silent on mind-location as a distinct constitutional site. All cognitive functions of contrition (self-recognition, honest assessment … |
| 138 | DIMENSION_REVIEW | pending | Multiple Transformation groups in Reg 6 have GOD as dominant subject (167-001, 179-002, 4697-001, 4701-001, 4701-002). Session B should explore the fu… |
| 1932 | OBSERVATION | resolved_qa | Fellowship vs unity: kind distinction — fellowship is inner participatory reality; unity is the structural outcome. Fellowship vs covenant (R34): laye… |
| 72 | DIMENSION_REVIEW | routed_cluster | Two groups (1552-001: fierce anger co-existing with grief/loyalty; 37-003: righteous anger co-existing with sorrow at hardness of heart) show the inne… |
| 1922 | CROSS_REGISTRY | resolved_qa | The co-occurrence pattern reveals fellowship as a relational-formative hub — it consistently appears with desire (the motivating state directing it), … |
| 110 | DIMENSION_REVIEW | pending | All seven whoredom groups are dominated by spiritual/covenantal whoredom — Israel's heart-departure toward foreign gods. The literal sexual dimension … |
| 2322 | OBSERVATION | resolved_qa | The evidence is largely silent on the spiritual beings interface. T4.6.1 and T4.6.3 are S-status (silent). T4.6.2 is partially answered. The programme… |
| 944 | OBSERVATION | pending | The verse evidence is substantially silent on the *immediate* inner-being response to fellowship encounter as a category. The data addresses longer-te… |
| 2506 | DATA_ANOMALY_QA_GAP | open | [v1.8 capture audit] Tiered (T0-T7) prompt coverage 160/189 (88 Q&A entries; range expansion applied). Missing tier_prompt_codes (29): ['T0.1.3', 'T0.… |
| 2133 | OBSERVATION | resolved_qa | Two frameworks: (1) Restorative justice theory — the cancellation of debt model maps onto restorative justice's vocabulary (restoration of right relat… |
| 298 | OBSERVATION | resolved_qa | "You will not despise" — the divine response to the broken and contrite heart is non-rejection. This is an understatement that implies acceptance: God… |
| 140 | DIMENSION_REVIEW | pending | Registry 124 (prophecy) shows a consistent pattern of Agency/Power (Spirit-enabled capacity exercised) alongside Relational Disposition (inner orienta… |
| 291 | OBSERVATION | resolved_qa | "Revive the spirit... revive the heart" — the divine response to contrition is revitalisation. This is a direct inner-being transformation: the contri… |
| 556 | OBSERVATION | pending | Neither bypassing nor impairing. Grace operates after moral evaluation, not instead of it. SD047 (justice and grace, 7 verses): holding both simultane… |
| 728 | OBSERVATION | routed_cluster | The receiving direction is partially evidenced (outer acts of compassion reach the recipient and produce material change) but the inner-being dynamics… |
| 1814 | MEANING_OBSERVATION | resolved_qa | Fellowship has constituent elements: (1) an object (what or who is fellowshipped with — God, persons, wickedness, idols); (2) a mode of joining (volit… |
| 69 | DIMENSION_REVIEW | pending | Shame vocabulary in Registry 146 operates on two consistent axes: (a) inner shame as felt condition (affective, moral, spiritual) and (b) shame as soc… |
| 109 | DIMENSION_REVIEW | pending | The slander registry contains three foot-related groups (6253-001: moral life direction; 6253-002: relational submission/devotion; 6256-001: teaching … |
| 564 | OBSERVATION | pending | Yes — this is the primary faculty engagement of grace. Grace is constitutively relational (T1.8): it requires a giver and receiver, creates standing b… |
| 861 | OBSERVATION | pending | The partial engagement suggests contrition is primarily oriented toward the past and the present encounter with God, not toward future conduct as such… |
| 566 | OBSERVATION | pending | Relational capacity is the faculty most constitutively shaped by grace. The person formed by grace becomes more relationally capable. Grace is the pri… |
| 560 | OBSERVATION | pending | Grace and conscience are not opposed but mutually necessary. The deepest encounters with grace are moments of deepest conscience-awareness. Grace does… |
| 2112 | OBSERVATION | resolved_qa | Forgiveness vs guilt: kind distinction — guilt is the condition; forgiveness is the remedy. Forgiveness vs mercy (R111): layer distinction — mercy is … |
| 985 | OBSERVATION | pending | The pattern confirms that fellowship is not primarily an affective phenomenon — it is relational and constitutional at its core — but it has consisten… |
| 856 | OBSERVATION | pending | The pattern reveals that contrition is foundationally a moral-evaluative condition — it cannot exist without the moral evaluation faculty having been … |
| 563 | OBSERVATION | pending | Grace is the constitutive ground of moral integration. The person formed by grace forgives not from calculation or discipline but because they have be… |
| 518 | OBSERVATION | pending | The origin question is directional: grace originates with God and is received by the human spirit. It does not originate in the human spirit — it arri… |
| 247 | OBSERVATION | resolved_qa | The registry description identifies contrition explicitly as an inner precondition rather than a correlate or consequence of repentance. This is an an… |
| 887 | OBSERVATION | pending | The evidence is largely silent on eschatological trajectory. No verse in the registry explicitly connects contrition to an eschatological fullness. Th… |
| 833 | OBSERVATION | pending | Yes — the three modes demonstrate different origins in different contexts, as established above. The origin varies by: (a) whether the crushing is mor… |
| 87 | DIMENSION_REVIEW | pending | Group 26-003 (Paul's paradoxical boasting in weakness — sustained inner act of inverting normal pride to reveal divine power) is analytically distinct… |
| 875 | OBSERVATION | pending | The evidence is silent on all three aspects of the spiritual beings interface: adversarial attack, angelic mediation, and general spiritual beings ope… |
| 881 | OBSERVATION | pending | Yes — the three modes have distinct mechanisms as established above. The most analytically significant distinction is between the confrontation mechan… |
| 1971 | SYNTHESIS_INTER_TIER | pending | T2's constitutional origin analysis (multiple origins — divine initiative, human volitional alignment, existential given) directly maps onto T4's rela… |
| 832 | OBSERVATION | pending | The origin is multiple across the three modes: - **Penitential-relational mode**: origin in the encounter of the inner being with its own moral condit… |
| 2573 | OBSERVATION | resolved_qa | The evidence is partially silent on constitutional deposit in the technical sense. The data establishes somatic consequence (in both directions) but n… |
| 74 | DIMENSION_REVIEW | folded | Reg 56 (envy) holds the full positive-negative dual register of the zeal/jealousy vocabulary. The same inner passion (consuming zealous desire) appear… |
| 843 | OBSERVATION | pending | The partial engagement suggests contrition requires a backward orientation — it is grounded in actual past events (the harm done, the trust broken). T… |
| 504 | OBSERVATION | pending | Yes — direction is determinative. Grace operates differently depending on whether direction is God-to-human (constituting, bestowing, enabling), human… |
| 62 | DIMENSION_REVIEW | routed_cluster | Registry 51 (distress) contains a significant cluster of outlier groups arriving via XREF terms that are outside the suffering domain: 242-001 (medita… |
| 90 | DIMENSION_REVIEW | pending | Group 1374-001 (the sluggard whose desire craves but whose will refuses to act) names sloth's inner-being structure precisely: not the absence of desi… |
| 1968 | SYNTHESIS_INTER_TIER | pending | T1's five-mode structure explains T6's co-occurrence pattern. The desire-R43 co-occurrence (6 shared verses — strongest signal) reflects T1's finding … |
| 141 | DIMENSION_REVIEW | pending | The blessing vocabulary reveals a mirror structure in Relational Disposition: group 1299-001 names God's inner disposition of love as the source of hi… |
| 496 | OBSERVATION | pending | Yes — directional and relational. The name orients the enquiry toward: a direction of movement (from the greater to the lesser — SD024 encodes this in… |
| 1005 | OBSERVATION | pending | The pattern confirms that fellowship is constitutionally relational in its deepest nature — it is not an emotion, cognition, or volitional act that *h… |
| 850 | OBSERVATION | pending | The pattern reveals that contrition is neither purely passive (something that simply happens to the inner being without the will's involvement) nor pu… |
| 548 | OBSERVATION | pending | Grace is affectively generative — it produces specific, appropriate affects rather than a generic emotional response. The sequence (fear → mourning → … |
| 993 | OBSERVATION | pending | The pattern confirms that fellowship operates partly through human agency (choice, proclamation, companionship-seeking) and partly through divine agen… |
| 88 | DIMENSION_REVIEW | routed_cluster | The sur (to turn aside) sub-gloss groups in Reg 128 show a consistent pattern: turning aside can be from God (6076-001 — Spiritual/God-ward negative),… |
| 319 | OBSERVATION | resolved_qa | The correlation signal structure reveals three structural partners for this registry: (1) guilt (073) — 51 shared verses, making it the primary struct… |
| 453 | OBSERVATION | pending | The co-occurrence data (Section 5 of R064) provides a ranked list. The top co-occurring registries by shared verse count:  / Rank / Registry / Word / … |
| 386 | OBSERVATION | pending | The conscience location, if confirmed, reveals that forgiveness is not only a relational act between two parties but an **inner resolution of the self… |
| 343 | DATA_ANOMALY_OBSERVATION_REGISTER_MISSING | open | Status reverted from Analysis Complete → Pre-Analysis Complete on 2026-04-28. The 2026-04-28 fellowship obslog requested status=Analysis Complete but … |
| 1602 | SYNTHESIS_INTER_TIER | pending | T1's four modes of mercy's operation (dispositional, mechanical, dialogic, institutional) map directly onto T4's four relational directions. The dispo… |
| 838 | OBSERVATION | pending | The pattern reveals that contrition is constitutively open rather than closed in its perceptive orientation. The contrite inner being is oriented outw… |
| 1601 | SYNTHESIS_INTER_TIER | pending | T1 identifies the enabling conditions for mercy-reception (guilt-awareness, humility, persistence, soul-affliction) and T3 maps mercy's faculty engage… |
| 2698 | SYNTHESIS_INTER_TIER | pending | T4's God-to-human direction (peace given through covenant, word, cross, Spirit) maps onto T5's mechanisms (proclamation, covenant-ground, cross-accomp… |
| 588 | OBSERVATION | pending | The sequences together reveal a common pattern: encounter with grace → creaturely recognition response (fear, mourning, prostration) → inner transform… |
| 709 | OBSERVATION | routed_cluster | The pattern reveals that compassion functions as the enabling context for conscience's constructive operation. Conscience is what creates the awarenes… |
| 895 | OBSERVATION | pending | The registry description places contrition in the description of brokenness (R018) and repentance (R135) as related registries — suggesting contrition… |
| 903 | OBSERVATION | pending | R030 carries three dimensions: Dependence/Creatureliness (primary), Emotion — Negative (secondary), and Divine-Human Correspondence (one group). The p… |
| 1413 | DATA_ANOMALY_QA_GAP | resolved_qa | [v1.8 capture audit] Q&A count 143 < 203 expected. In-scope: 189 v2 catalogue + 14 Love Extensions = 203. Missing tier_prompt_codes (60): ['T0.4.3', '… |
| 1616 | SYNTHESIS_INTER_TIER | pending | T4's asymmetric relational chain (God→human→human) and T6's sequential positioning of mercy as bridge-between-conditions are structurally related. T6 … |
| 964 | OBSERVATION | pending | The soul-subset locations implied are conscience (moral self-assessment under complicity), desire (the motivating faculty driving fellowship-seeking),… |
| 2385 | SYNTHESIS_INTER_TIER | pending | T1 proposes that covenant is the architectural backbone of the C17 cluster — the structure within which the relational-grace vocabulary operates. T6 p… |
| 2686 | SYNTHESIS_INTER_TIER | pending | T1 establishes peace as a four-dimensional structured reality (covenant → gift → inner condition → eschatological embodiment); T5 shows how peace move… |
| 1785 | SYNTHESIS_INTER_TIER | pending | The constitutional tier (T2) establishes that contrition's primary loci are spirit and heart; the faculty tier (T3) shows that the faculties most enga… |
| 1608 | SYNTHESIS_INTER_TIER | pending | T2's constitutional architecture (spirit-soul interface origin, soul-level operation, embodied expression) maps directly onto T5's formative sequences… |
| 2383 | SYNTHESIS_INTER_TIER | pending | T1 establishes that covenant has directional, relational, and constitutional implications that orient the entire enquiry (Q&A-015). T4 shows how these… |
| 2687 | SYNTHESIS_INTER_TIER | pending | T1 establishes peace's central T1 finding (covenant → gift → condition → embodiment in Person); T6 confirms this structure through the causal and cons… |
| 1600 | SYNTHESIS_INTER_TIER | pending | T1 defines mercy as a four-element structure (disposition, mechanism, petition-response, spatial locus) and T2 maps mercy's constitutional architectur… |
| 398 | OBSERVATION | pending | The perceptive engagement pattern reveals that forgiveness is **not primarily perceptive in its operation** — it does not primarily function through t… |
| 1025 | OBSERVATION | pending | The sequences reveal a common structural logic: **fellowship operates as a prerequisite-to-participation mechanism** (finding 062-SEQUE-001). In every… |
| 2185 | SYNTHESIS_INTER_TIER | routed_cluster | T3's finding that compassion is the motivational ground of conscientiousness explains the co-occurrence pattern in T6. Conscience (T3.9) and moral eva… |
| 1047 | OBSERVATION | pending | Based on the available evidence:  - **Fellowship vs. unity:** A distinction of *direction and process* — fellowship is the process of joining; unity i… |
| 1611 | SYNTHESIS_INTER_TIER | pending | T3 shows mercy activating the full faculty system (perception, cognition, memory, affect, volition, agency, moral evaluation, conscience, conscientiou… |
| 2207 | SYNTHESIS_INTER_TIER | pending | T2's origin analysis (grace does not originate in the human constitutional system — it arrives from God) and T4's directional analysis (God-to-human i… |
| 1606 | SYNTHESIS_INTER_TIER | pending | T2 maps mercy's constitutional locations (soul, mind, heart, body, spirit-soul interface) and T3 maps its faculty engagements. Reading together: the c… |
| 1232 | SYNTHESIS_INTER_TIER | pending | T2's constitutional movement (six-step sequence) and T5's transformation sequences (positive arc and moral awareness arc) describe the same developmen… |
| 421 | OBSERVATION | pending | **Enables conscientiousness:** Received divine forgiveness enables a more integrated response in the forgiver — the awareness of received forgiveness … |
| 1230 | SYNTHESIS_INTER_TIER | pending | T2 identified the constitutional movement of goodness from Spirit-level through soul and heart to outward expression (six-step sequence, Q&A-064). T3 … |
| 2393 | SYNTHESIS_INTER_TIER | pending | T3 identifies the new covenant's faculty-level effect as the transformation of volition (from called-for to liberated — Q&A-085) and the production of… |
| 413 | OBSERVATION | pending | The motivational engagement pattern reveals something structurally significant: forgiveness is **both a motivational product and a motivational produc… |
| 2878 | SYNTHESIS_INTER_TIER | pending | The relational interfaces (T4 — divine-initiative, human-responsive, covenantal scope) and the formation arc (T5 — constitutive endowment, sustained n… |
| 1218 | SYNTHESIS_INTRA_TIER | pending | T2 as a whole reveals that goodness has a comprehensive multi-level constitutional presence — from Spirit-level origin through soul-orientation, heart… |
| 2375 | SYNTHESIS_INTRA_TIER | pending | T2 as a whole reveals that covenant operates across the full constitutional range of the inner person with no single exclusive location. The heart is … |
| 2389 | SYNTHESIS_INTER_TIER | pending | T2 identifies a shift in constitutional origin across the covenant trajectory: from external bestowal (Noahic) to bilateral reception (Sinai) to gener… |
| 2874 | SYNTHESIS_INTER_TIER | pending | The faculty engagement pattern (T3 — perception, affect, volition, relational capacity all engaged) and the relational interface structure (T4 — God-t… |
| 2376 | SYNTHESIS_INTRA_TIER | pending | T3 as a whole reveals that covenant comprehensively engages the inner faculties but with a specific structural bias: the faculties it most deeply and … |
| 2392 | SYNTHESIS_INTER_TIER | pending | T3 reveals that the inner faculties covenant most deeply engages are Other-oriented (relational capacity, conscience, moral evaluation, memory). T4 re… |
| 2877 | SYNTHESIS_INTER_TIER | pending | The faculty engagement pattern (T3 — hearing precedes giving, memory is narrative-temporal, affect is at source and target, conscientiousness is the a… |
| 857 | OBSERVATION | pending | Yes — conscience is the faculty most directly engaged by the penitential-relational mode of contrition. The conscience is the inner witness that convi… |

## Truly non-evidenced — pointer flags (clean close candidates)

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
| 130 | SD_POINTER | DIM-61-SD001 — C06 fear cluster shows a tripartite dimension pattern: fear-as-God-ward-orientation (Spiritual/God-ward ~18 groups), fear-as-inner-affe… |
| 380 | SD_POINTER | SP-067-003 — Registry 197 (authority) is the third-highest co-occurrence partner with R67 at 17 shared verses — higher than joy, soul, or wisdom. The … |
| 594 | SB_FINDING | SB-062-T2-014 — [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status A, notation: Gap identified.  Prompt: If the evidence is silen… |
| 216 | SD_POINTER | DIM-068-SD047 — Justice (Reg 98, C13) cooccurrence 7 verses. Grace and justice co-occurring raises the foundational inner-being tension: can a person … |
| 162 | SD_POINTER | DIM-6-SD001 — C16 contains a substantial concentration of GOD-dominant Agency/Power and Transformation groups across anointing, consecration, and bles… |
| 218 | SD_POINTER | DIM-068-SD049 — Appetite (Reg 8, C04) cooccurrence 4 verses. Appetite names the deep inner longing or craving. For Session D: do the 4 co-occurring ve… |
| 140 | SD_POINTER | DIM-57-SD001 — The Affective/Emotional dimension appears extensively in C11 (15 groups assigned) but was absent from C10 assignments, despite groups i… |
| 436 | SD_POINTER | SP-067-020 — [Migrated from catalogue GAP-S1-002 2026-04-28 — programme-level methodology question, not a per-word analytical question] Does the word … |
| 437 | SD_POINTER | SP-067-021 — [Migrated from catalogue GAP-S2-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where the word… |
| 142 | SD_POINTER | DIM-001-SD001 — The new covenant transformation group (3272-001) appears in the abomination registry and salvation vocabulary groups appear in the deb… |
| 519 | SB_FINDING | SB-023-T2-015 — [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status S, notation: Consistent with prior analysis.  Prom… |
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
| 515 | SB_FINDING | SB-023-T2-011 — [Catalogue v2 gap surfaced 2026-04-30] T4.4.4 (Human Interface — Receiving) — status P, notation: Gap identified.  Prompt: If the evid… |
| 568 | SB_FINDING | SB-030-T2-044 — [Catalogue v2 gap surfaced 2026-04-30] T5.6.3 (Eschatological Trajectory) — status A, notation: Gap identified.  Prompt: If the eviden… |
| 228 | SD_POINTER | DIM-068-SD010 — Will (Reg 173, C14) cooccurrence: 11 verses. Grace and will co-occurring across 11 verses raises the foundational inner-being question… |
| 561 | SB_FINDING | SB-030-T2-037 — [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status A, notation: Gap identified.  Prompt: If the evide… |
| 462 | SB_FINDING | SB-064-T2-020 — [Catalogue v2 gap surfaced 2026-04-30] T7.3.3 (Human Science Frameworks) — status S, notation: Gap identified.  Prompt: Where the vers… |
| 169 | SD_POINTER | DIM-19-SD001 — C19 produces 37 of 97 groups (38%) assigned Divine-Human Correspondence — the highest cluster-level concentration in the programme so f… |
| 412 | SD_POINTER | SP-067-013 — R197 (authority) ranks third in co-occurrence with R67 (goodness) at 17 shared verses, above joy, soul, and wisdom. This is unexpected gi… |
| 121 | SD_POINTER | DIM-160-SD001 — Directionally-determined inner faculty pattern — a recurring structural principle identified across C02 registries (108, 127, 160, 174… |
| 232 | SD_POINTER | DIM-068-SD014 — C17 cluster synthesis question: all C17 sibling registries appear in grace's cooccurrence signal — peace (117, 10), kindness (99, 7), … |

## Verse-evidenced but unanchored (NOT auto-close) — counts only

- findings: 663 (have `anchor_verses`/inline verse but no named subject term)
- flags: 90

These need your call: they carry verse evidence, so they are not 'non-evidenced'. Options: (i) route via verse as a last-resort lower-confidence link, (ii) hold for the owning cluster's analysis, (iii) treat 'no named term' as itself disqualifying and set aside. Listed on request.
