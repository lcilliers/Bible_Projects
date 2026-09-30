# Session B/D pointers — content mining for term/verse/cluster hooks

**Generated:** 2026-06-01 (read-only, NO writes). Mines the free text + anchor/strongs columns for Strong's codes, verse references, `Reg NNN` mentions, and transliteration/gloss matches; resolves each to a cluster where possible. Flags no-hook pointers as low-value (soft-delete) candidates for study.

Reference data: 3965 strongs→cluster; 23640 distinct verse refs; 2649 transliterations (≥5 chars).

## Routability by content (vs the dedicated columns)

| population | n | has Strong's | has verse ref | has Reg | has translit | **resolves to cluster** | no hook at all |
|---|--:|--:|--:|--:|--:|--:|--:|
| wa_session_b_findings | 2883 | 501 (17%) | 2182 (76%) | 84 (3%) | 2062 (72%) | **2657 (92%)** | 180 |
| SD_POINTER | 346 | 103 (30%) | 186 (54%) | 132 (38%) | 221 (64%) | **284 (82%)** | 37 |
| SB_FINDING | 203 | 23 (11%) | 79 (39%) | 8 (4%) | 165 (81%) | **176 (87%)** | 25 |
| SB_INNER_BEING | 4 | 4 (100%) | 4 (100%) | 1 (25%) | 4 (100%) | **4 (100%)** | 0 |
| SD_CLUSTER | 1 | 0 (0%) | 0 (0%) | 0 (0%) | 1 (100%) | **1 (100%)** | 0 |

## Synthesis

**The mapping is in the text, not the columns.** The dedicated columns are empty/sparse (`term_id` 0/2,883; `strongs_reference` 78/346), yet the free text + `anchor_verses` resolve **~92% of findings and ~82% of SD_POINTERs to a cluster**.

**Confidence tiers (for how to apply):**
- **High** — explicit **Strong's codes** (501 findings, 103 SD_POINTER) and **verse references** (2,182 findings; `anchor_verses` populated on 1,432 + inline refs). Verse→`wa_verse_records`→term→cluster and Strong's→term→cluster are exact.
- **Medium** — **`Reg NNN`** mentions (registry → its terms → clusters; a fan-out, not 1:1).
- **Lower** — **transliteration/gloss substring matches** (2,062 findings). High coverage but possible false positives (a normalised ≥5-char substring can coincide); treat as corroboration. Even ignoring translit, verse-or-Strong's alone routes the large majority.

**Two things this enables (later, on approval — not now):**
1. **Backfill the structured links** from the high-confidence hooks — populate `wa_session_b_findings.term_id` / a verse link from the extracted Strong's + verse refs, so the mapping is *queryable*, not re-mined each time.
2. **Soft-delete the no-hook set** below, once you've judged it.

**Low-value totals:** 180 findings + 37 SD_POINTER + 25 SB_FINDING = **242 pointers** with no extractable hook — *candidates, not confirmed nonsense* (a few may be genuine synthesis notes that cite nothing).

## Low-value / soft-delete candidates (no extractable hook)

These carry no Strong's, verse, registry, or transliteration hook. Sorted shortest-text first (most likely nonsense). **For your study — nothing is deleted.**

### wa_session_b_findings — 180 no-hook

| id | type/label | text |
|---|---|---|
| 524 | OBSERVATION |  |
| 527 | OBSERVATION |  |
| 578 | OBSERVATION |  |
| 583 | OBSERVATION |  |
| 584 | OBSERVATION |  |
| 612 | OBSERVATION |  |
| 620 | OBSERVATION | *Gap identified.* |
| 209 | OBSERVATION | 884-008 NULL — volitional preference; likely Volition (04) candidate |
| 217 | OBSERVATION | DIM-67-001: core analytical question — distinct phenomena vs unified category |
| 208 | OBSERVATION | 884-007 NULL — creation pronouncement; no existing dimension label fits cleanly |
| 2100 | SPIRIT_SOUL_BODY | T2.8.1 data was silent on constitutional body deposit. T5.7 is formally closed. |
| 207 | OBSERVATION | Cognition (03) assigned to 884-004 and 884-006 — both evaluative judgment groups |
| 214 | OBSERVATION | Co-occurrence: R103 (love, 23) > R43 (desire, 18) > R197 (authority, 17) as top 3 |
| 197 | OBSERVATION | Registry-level dimension = Moral/Conscience; groups show wider spread — tension noted |
| 218 | OBSERVATION | DIM-67-001 uses pre-v1.4 dimension vocabulary; needs re-reading against current labels |
| 226 | OBSERVATION | 884-004 anchors rank inner qualities above external power — structural normative claim |
| 232 | OBSERVATION | 884-007 dimension NULL reinforced — needs a divine creative/evaluative agency category |
| 213 | OBSERVATION | R103 (love) deepest structural XREF link; R42 (delight) Hebrew-only; R99 (kindness) Greek |
| 215 | OBSERVATION | R197 (authority) unexpectedly high — likely driven by 884-008 volitional-preference idiom |
| 219 | OBSERVATION | SBF-VCB013-001: tripartite model confirmed; OBS-010 extends distortion pole etymologically |
| 196 | OBSERVATION | Registry description names 3 axes: aesthetic/moral/relational; human goodness is derivative |
| 2035 | SPIRIT_SOUL_BODY | Evidence is silent on constitutional body deposit from forgiveness. T5.7 to close formally. |
| 234 | OBSERVATION | 884-008 NULL likely = Volition (04) — group description explicitly names choosing/preferring |
| 1245 | DATA_ANOMALY_QA_GAP | [v1.8 capture audit] Q&A count 187 < 189 expected. Missing tier_prompt_codes: ['T2.1.4', 'T2.5.3'] |
| 1866 | OBSERVATION | Verse evidence is largely silent on explicit memory faculty engagement with fellowship. Gap noted. |
| 202 | OBSERVATION | TOV root family distributed across R67 (adjectival), R65 (active doing), R103 (relational-affective) |
| 1672 | SPIRIT_SOUL_BODY | The evidence is silent on constitutional body deposit. T5.7 closes formally — all three T5.7 prompts receive N. |
| 1735 | N/A | T2.8 found no constitutional body deposit from contrition. T5.7 is formally closed. All three prompts receive N/A except this closing confir… |
| 2439 | OBSERVATION | Explicitly noted: the evidence does not locate the kindness disposition at the soul level. The soul appears as beneficiary, not as constitut… |
| 1855 | OBSERVATION | Yes — origin shifts across modes: divine → human → existential, corresponding to the ontological → companionship → existential mode levels. … |
| 246 | DATA_ANOMALY_CITATION_GAP | Citation FK resolution exceeds 10% threshold in: sb_s2c_ch2: 7/40 unresolved (18%); sb_s2c_ch4: 11/42 unresolved (26%); sb_s2c_ch5: 8/55 unr… |
| 1843 | SPIRIT_SOUL_BODY | Verse evidence is largely silent on explicit mind-location. The cognitive dimension is implied (discernment of fellowship object) but not na… |
| 1492 | SPIRIT_SOUL_BODY | The evidence is silent on constitutional body deposit from mercy's sustained operation. T5.7 closes formally as a result — all three prompts… |
| 1854 | OBSERVATION | Multiple — three distinct origin points as evidenced in Q&A-062: divine initiative, human volitional alignment, existential given. The origi… |
| 1722 | N/A | The verse evidence is silent on contrition's relation to spiritual beings. No anchor verse addresses this dimension. Gap noted for Session D… |
| 2704 | DATA_ANOMALY_QA_GAP | [v1.8 capture audit] Tiered (T0–T7) prompt coverage 188/189 across all v1.8 captures for R117. This obslog: 187 Q&A entries; cumulative DB c… |
| 1919 | OBSERVATION | Generational consequence: not evidenced from this registry's anchor verses. The fellowship formations described are personal and corporate, … |
| 1830 | OBSERVATION | Primary dimension: Relational Disposition — confirmed. Fellowship is fundamentally about orientation and participation in relation. The pers… |
| 514 | OBSERVATION | Relational Disposition — confirmed in the registry header (dimensions = "Relational/Social"), dim_review_status = "Complete." The dominant_s… |
| 2024 | SPIRIT_SOUL_BODY | Verse evidence is largely silent on explicit soul-faculty naming for forgiveness. Gap noted — the soul-level engagement is inferred from the… |
| 1933 | OBSERVATION | Fellowship vs unity: kind distinction. Fellowship vs covenant: layer distinction (legal vs experiential). Fellowship vs desire: sequential/d… |
| 1686 | OBSERVATION | The evidence is thin on memory as a named faculty in contrition. The implication is that contrition requires honest memory of wrongdoing but… |
| 1045 | OBSERVATION | **No vocabulary sharing at the term level is evidenced (shared_term_count = 0, term_sharing_ratio = 0.0).** The closing condition applies at… |
| 830 | OBSERVATION | The evidence is silent on body deposit. No constitutional somatic deposit from sustained contrition is evidenced in the registry data. **T5.… |
| 1663 | SPIRIT_SOUL_BODY | The verse evidence is largely silent on explicit mind-location for contrition. The spirit and heart are the named loci; the cognitive dimens… |
| 825 | OBSERVATION | The evidence is silent on soul-subset locations beyond spirit, heart, and soul (*nefesh*). No faculty-specific terms (will, conscience, memo… |
| 1852 | SPIRIT_SOUL_BODY | The evidence is partially silent — the wound-mark persists physically, but whether this constitutes a programme-relevant constitutional body… |
| 250 | OBSERVATION | carry_forward=1. This indicates the registry was carried forward from a prior programme phase. It does not affect analytical scope but is no… |
| 2113 | OBSERVATION | Forgiveness vs guilt: kind (condition vs remedy). Forgiveness vs mercy: layer (disposition vs act). Forgiveness vs repentance: sequential (a… |
| 969 | OBSERVATION | **The evidence is silent on constitutional bodily deposit for fellowship.** This conclusion feeds into T5.7: the T5.7 Deposit Consequence pr… |
| 1884 | OBSERVATION | Fellowship is a primary vehicle of conscientiousness formation — the community one fellowships with shapes the moral seriousness and integra… |
| 814 | OBSERVATION | **Dependence / Creatureliness** — confirmed as the primary dimension by Dimension Review. 5 of 9 groups carry this dimension: 7552-003, 7553… |
| 2021 | SPIRIT_SOUL_BODY | The verse evidence is largely silent on explicit spirit-faculty naming as the primary locus of forgiveness. The Spirit is involved in the au… |
| 1911 | OBSERVATION | Yes — the companionship/habituation mechanism (Mechanism 1) and the wound-as-cleansing mechanism (Mechanism 2) are distinct. Mechanism 1 is … |
| 1353 | OBSERVATION | Systematic dimensional sharing data across all 181 registries is not available in the current data package. What is available: co-occurrence… |
| 2051 | OBSERVATION | The pattern reveals affect as simultaneously prerequisite (compassion enabling the act) and product (love and reverence as downstream states… |
| 1860 | OBSERVATION | The pattern reveals perception as a prerequisite for rightly directed fellowship and a casualty of misdirected fellowship. The person who fe… |
| 1881 | OBSERVATION | Conscience is the moral sensitivity that enables the initial distinction between right and wrong fellowship objects; fellowship then either … |
| 122 | DIMENSION_REVIEW | The bondage registry shows a consistent inner-being polarity: enslavement to disordered desires/sin/fear on one side, willing surrender to G… |
| 2023 | SPIRIT_SOUL_BODY | If guilt (R073 — 51 shared verses, strongest co-occurrence signal) operates at the soul level, then forgiveness — which addresses guilt — ne… |
| 249 | OBSERVATION | sb_classification is NULL. The absence of a prior sb_classification means Stage 2b must produce a spirit-soul-body finding from first princi… |
| 597 | OBSERVATION | From Section 5 of the data: seeking (R140: 40 verses), strength (R187: 15), love (R103: 14), desire (R043: 12), evil (R057: 12), will (R173:… |
| 2354 | CROSS_REGISTRY | Precise dimensional sharing counts require CC database query. The inferred pattern (covenant shares dimensions with the widest range of regi… |
| 1920 | OBSERVATION | T2.8 found ambiguous evidence — the wound mark is a physical persisting trace but whether it constitutes a programme-relevant constitutional… |
| 656 | OBSERVATION | The verse evidence is silent on the immediate inner-being response of the *receiver* of compassion. This silence is noted and flagged as a n… |
| 2510 | OBSERVATION | Explicitly noting: the evidence is silent on a constitutional body deposit for kindness, and the covenantal-generational evidence actively c… |
| 2057 | OBSERVATION | Agency is both exercised (in forgiving) and liberated (in receiving forgiveness). The pattern: forgiveness frees the agency of the forgiven … |
| 1869 | OBSERVATION | Fellowship is constitutively affective — it is not a purely cognitive or volitional alignment but a genuine sharing in the affective reality… |
| 1887 | OBSERVATION | Relational capacity is both the vehicle and the product of fellowship. The pattern reveals: fellowship requires relational capacity to begin… |
| 2060 | OBSERVATION | The pattern: forgiveness requires the most precise moral evaluation the inner being is capable of — accurate assessment of what was owed, wh… |
| 2117 | OBSERVATION | The Relational Disposition primary dimension shared with mercy (R111) and love (R103) positions forgiveness within the relational triad oper… |
| 2063 | OBSERVATION | Conscience is both the faculty that makes forgiveness necessary (by delivering the guilt-verdict) and the primary beneficiary of forgiveness… |
| 2093 | OBSERVATION | The mechanisms differ across modes: covenantal-objective mode uses the ritual-atonement mechanism (external, structural). Divine relational-… |
| 577 | OBSERVATION | By inference: the same conditions blocking reception of divine grace likely block reception of human grace — pride, merit-logic, ingratitude… |
| 248 | OBSERVATION | The registry note references repentance (#135) and brokenness (#18) as related registries. The registry description places contrition betwee… |
| 543 | OBSERVATION | Enables a specific form: the grace-inference (SD029). SD048 raises the question of whether right thinking about grace is itself grace-enable… |
| 764 | OBSERVATION | Dimensional sharing data is not yet available in the programme database (dimensions field = None). The analysis above represents inferences … |
| 971 | OBSERVATION | The origin is definitively multiple. Finding 062-ORIG-001 confirms: "both divine initiative and human response generate fellowship." The dat… |
| 905 | OBSERVATION | Full programme-wide dimensional distribution data is not available in the current session. The dimensional sharing analysis above is based o… |
| 1863 | OBSERVATION | The pattern reveals cognition as both prerequisite for and product of fellowship direction — initial cognitive discernment enables right fel… |
| 271 | OBSERVATION | The three Emotion — Negative groups describe a different register: suffering anguish (7552-001), corporate desolation (7554-002), and inner … |
| 269 | OBSERVATION | Dimension distribution: - Dimension 10 — Dependence / Creatureliness: 5 groups (7552-003, 7553-001, 7557-001, 7554-001, 7555-001) - Dimensio… |
| 1689 | OBSERVATION | Affect is not merely a symptom of contrition but constitutive of it — a contrition without feeling is not genuine contrition per the registr… |
| 1748 | OBSERVATION | Contrition vs shame: distinction of direction (God-ward vs socially-oriented) and depth (inner grief vs surface social response). Contrition… |
| 1878 | OBSERVATION | Moral evaluation and fellowship direction are mutually determining: accurate moral evaluation directs fellowship rightly; right fellowship d… |
| 557 | OBSERVATION | Grace produces moral clarity — sharpening rather than blunting moral awareness. The person who recognises grace has made a moral evaluation:… |
| 1684 | OBSERVATION | Memory is implied in contrition's cognitive ground — the person who is genuinely contrite remembers having caused harm or broken trust. Howe… |
| 1937 | OBSERVATION | The Relational Disposition primary dimension shared with love and mercy positions fellowship as one of the relational triad (love, mercy, fe… |
| 1052 | OBSERVATION | **Programme-wide dimensional sharing data is not available in this session.** The fellowship registry's own dimensions are known, but which … |
| 532 | OBSERVATION | Grace is a whole-person phenomenon. The body is integral to its operation — not merely an occasional expression. Grace cannot be adequately … |
| 102 | DIMENSION_REVIEW | Group 851-004 ('the impossibility of inner self-knowledge — the heart's moral corruption exceeds human capacity to understand') is a theolog… |
| 680 | OBSERVATION | The evidence is not fully silent — the womb etymology and the Exod 34:6 generational frame create partial signals — but direct evidence of a… |
| 544 | OBSERVATION | Grace produces a particular cognitive form — reasoned assurance, not merely experienced certainty. Grace can be the ground of inner confiden… |
| 824 | OBSERVATION | The evidence is silent on mind-location as a distinct constitutional site. All cognitive functions of contrition (self-recognition, honest a… |
| 576 | OBSERVATION | Primarily God-to-human receiving is evidenced. Ruth 2:10 shows Ruth receiving favour from Boaz — a human-to-human grace event where Ruth is … |
| 1558 | CROSS_REGISTRY | Top co-occurrence (from §5 data — OBS-111-021): R023 compassion (76), R073 guilt (75), R044 despair (48), R187 strength (39), R117 peace (37… |
| 1932 | OBSERVATION | Fellowship vs unity: kind distinction — fellowship is inner participatory reality; unity is the structural outcome. Fellowship vs covenant (… |
| 72 | DIMENSION_REVIEW | Two groups (1552-001: fierce anger co-existing with grief/loyalty; 37-003: righteous anger co-existing with sorrow at hardness of heart) sho… |
| 1922 | CROSS_REGISTRY | The co-occurrence pattern reveals fellowship as a relational-formative hub — it consistently appears with desire (the motivating state direc… |
| 1196 | CROSS_REGISTRY | Cross-registry dimensional sharing data is not available in the current data package. The dimensions of R67 are confirmed; the formal compar… |
| 110 | DIMENSION_REVIEW | All seven whoredom groups are dominated by spiritual/covenantal whoredom — Israel's heart-departure toward foreign gods. The literal sexual … |
| 2755 | SOMATIC_EVIDENCE | The evidence is not silent but does not confirm a constitutional body deposit. No explicit somatic deposit is evidenced. The data is silent … |
| 2322 | OBSERVATION | The evidence is largely silent on the spiritual beings interface. T4.6.1 and T4.6.3 are S-status (silent). T4.6.2 is partially answered. The… |
| 944 | OBSERVATION | The verse evidence is substantially silent on the *immediate* inner-being response to fellowship encounter as a category. The data addresses… |
| 2506 | DATA_ANOMALY_QA_GAP | [v1.8 capture audit] Tiered (T0-T7) prompt coverage 160/189 (88 Q&A entries; range expansion applied). Missing tier_prompt_codes (29): ['T0.… |
| 2133 | OBSERVATION | Two frameworks: (1) Restorative justice theory — the cancellation of debt model maps onto restorative justice's vocabulary (restoration of r… |
| 298 | OBSERVATION | "You will not despise" — the divine response to the broken and contrite heart is non-rejection. This is an understatement that implies accep… |
| 291 | OBSERVATION | "Revive the spirit... revive the heart" — the divine response to contrition is revitalisation. This is a direct inner-being transformation: … |
| 556 | OBSERVATION | Neither bypassing nor impairing. Grace operates after moral evaluation, not instead of it. SD047 (justice and grace, 7 verses): holding both… |
| 1814 | MEANING_OBSERVATION | Fellowship has constituent elements: (1) an object (what or who is fellowshipped with — God, persons, wickedness, idols); (2) a mode of join… |
| 109 | DIMENSION_REVIEW | The slander registry contains three foot-related groups (6253-001: moral life direction; 6253-002: relational submission/devotion; 6256-001:… |
| 564 | OBSERVATION | Yes — this is the primary faculty engagement of grace. Grace is constitutively relational (T1.8): it requires a giver and receiver, creates … |
| 861 | OBSERVATION | The partial engagement suggests contrition is primarily oriented toward the past and the present encounter with God, not toward future condu… |
| 566 | OBSERVATION | Relational capacity is the faculty most constitutively shaped by grace. The person formed by grace becomes more relationally capable. Grace … |
| 560 | OBSERVATION | Grace and conscience are not opposed but mutually necessary. The deepest encounters with grace are moments of deepest conscience-awareness. … |
| 2112 | OBSERVATION | Forgiveness vs guilt: kind distinction — guilt is the condition; forgiveness is the remedy. Forgiveness vs mercy (R111): layer distinction —… |
| 985 | OBSERVATION | The pattern confirms that fellowship is not primarily an affective phenomenon — it is relational and constitutional at its core — but it has… |
| 856 | OBSERVATION | The pattern reveals that contrition is foundationally a moral-evaluative condition — it cannot exist without the moral evaluation faculty ha… |
| 563 | OBSERVATION | Grace is the constitutive ground of moral integration. The person formed by grace forgives not from calculation or discipline but because th… |
| 518 | OBSERVATION | The origin question is directional: grace originates with God and is received by the human spirit. It does not originate in the human spirit… |
| 247 | OBSERVATION | The registry description identifies contrition explicitly as an inner precondition rather than a correlate or consequence of repentance. Thi… |
| 887 | OBSERVATION | The evidence is largely silent on eschatological trajectory. No verse in the registry explicitly connects contrition to an eschatological fu… |
| 151 | DIMENSION_REVIEW | Psalm 133:1 ('how good and pleasant it is when brothers dwell in unity') appears as a related verse in group 1210-002 (gam — extension funct… |
| 833 | OBSERVATION | Yes — the three modes demonstrate different origins in different contexts, as established above. The origin varies by: (a) whether the crush… |
| 875 | OBSERVATION | The evidence is silent on all three aspects of the spiritual beings interface: adversarial attack, angelic mediation, and general spiritual … |
| 881 | OBSERVATION | Yes — the three modes have distinct mechanisms as established above. The most analytically significant distinction is between the confrontat… |
| 1971 | SYNTHESIS_INTER_TIER | T2's constitutional origin analysis (multiple origins — divine initiative, human volitional alignment, existential given) directly maps onto… |
| 832 | OBSERVATION | The origin is multiple across the three modes: - **Penitential-relational mode**: origin in the encounter of the inner being with its own mo… |
| 2573 | OBSERVATION | The evidence is partially silent on constitutional deposit in the technical sense. The data establishes somatic consequence (in both directi… |
| 843 | OBSERVATION | The partial engagement suggests contrition requires a backward orientation — it is grounded in actual past events (the harm done, the trust … |
| 504 | OBSERVATION | Yes — direction is determinative. Grace operates differently depending on whether direction is God-to-human (constituting, bestowing, enabli… |
| 1968 | SYNTHESIS_INTER_TIER | T1's five-mode structure explains T6's co-occurrence pattern. The desire-R43 co-occurrence (6 shared verses — strongest signal) reflects T1'… |
| 141 | DIMENSION_REVIEW | The blessing vocabulary reveals a mirror structure in Relational Disposition: group 1299-001 names God's inner disposition of love as the so… |
| 496 | OBSERVATION | Yes — directional and relational. The name orients the enquiry toward: a direction of movement (from the greater to the lesser — SD024 encod… |
| 1005 | OBSERVATION | The pattern confirms that fellowship is constitutionally relational in its deepest nature — it is not an emotion, cognition, or volitional a… |
| 850 | OBSERVATION | The pattern reveals that contrition is neither purely passive (something that simply happens to the inner being without the will's involveme… |
| 548 | OBSERVATION | Grace is affectively generative — it produces specific, appropriate affects rather than a generic emotional response. The sequence (fear → m… |
| 993 | OBSERVATION | The pattern confirms that fellowship operates partly through human agency (choice, proclamation, companionship-seeking) and partly through d… |
| 319 | OBSERVATION | The correlation signal structure reveals three structural partners for this registry: (1) guilt (073) — 51 shared verses, making it the prim… |
| 453 | OBSERVATION | The co-occurrence data (Section 5 of R064) provides a ranked list. The top co-occurring registries by shared verse count:  / Rank / Registry… |
| 386 | OBSERVATION | The conscience location, if confirmed, reveals that forgiveness is not only a relational act between two parties but an **inner resolution o… |
| 343 | DATA_ANOMALY_OBSERVATION_REG | Status reverted from Analysis Complete → Pre-Analysis Complete on 2026-04-28. The 2026-04-28 fellowship obslog requested status=Analysis Com… |
| 1602 | SYNTHESIS_INTER_TIER | T1's four modes of mercy's operation (dispositional, mechanical, dialogic, institutional) map directly onto T4's four relational directions.… |
| 838 | OBSERVATION | The pattern reveals that contrition is constitutively open rather than closed in its perceptive orientation. The contrite inner being is ori… |
| 1601 | SYNTHESIS_INTER_TIER | T1 identifies the enabling conditions for mercy-reception (guilt-awareness, humility, persistence, soul-affliction) and T3 maps mercy's facu… |
| 2698 | SYNTHESIS_INTER_TIER | T4's God-to-human direction (peace given through covenant, word, cross, Spirit) maps onto T5's mechanisms (proclamation, covenant-ground, cr… |
| 588 | OBSERVATION | The sequences together reveal a common pattern: encounter with grace → creaturely recognition response (fear, mourning, prostration) → inner… |
| 1559 | CROSS_REGISTRY | The co-occurrence pattern reveals that mercy occupies a central hub position in the inner-being landscape — it connects to the two poles of … |
| 709 | OBSERVATION | The pattern reveals that compassion functions as the enabling context for conscience's constructive operation. Conscience is what creates th… |
| 895 | OBSERVATION | The registry description places contrition in the description of brokenness (R018) and repentance (R135) as related registries — suggesting … |
| 903 | OBSERVATION | R030 carries three dimensions: Dependence/Creatureliness (primary), Emotion — Negative (secondary), and Divine-Human Correspondence (one gro… |
| 1413 | DATA_ANOMALY_QA_GAP | [v1.8 capture audit] Q&A count 143 < 203 expected. In-scope: 189 v2 catalogue + 14 Love Extensions = 203. Missing tier_prompt_codes (60): ['… |
| 1616 | SYNTHESIS_INTER_TIER | T4's asymmetric relational chain (God→human→human) and T6's sequential positioning of mercy as bridge-between-conditions are structurally re… |
| 2385 | SYNTHESIS_INTER_TIER | T1 proposes that covenant is the architectural backbone of the C17 cluster — the structure within which the relational-grace vocabulary oper… |
| 632 | OBSERVATION | **Cultural anthropology**: honour-shame frameworks illuminate the eye-formula ("found favour in the eyes of") and the prostration pattern (R… |
| 2686 | SYNTHESIS_INTER_TIER | T1 establishes peace as a four-dimensional structured reality (covenant → gift → inner condition → eschatological embodiment); T5 shows how … |
| 1608 | SYNTHESIS_INTER_TIER | T2's constitutional architecture (spirit-soul interface origin, soul-level operation, embodied expression) maps directly onto T5's formative… |
| 2383 | SYNTHESIS_INTER_TIER | T1 establishes that covenant has directional, relational, and constitutional implications that orient the entire enquiry (Q&A-015). T4 shows… |
| 2687 | SYNTHESIS_INTER_TIER | T1 establishes peace's central T1 finding (covenant → gift → condition → embodiment in Person); T6 confirms this structure through the causa… |
| 1600 | SYNTHESIS_INTER_TIER | T1 defines mercy as a four-element structure (disposition, mechanism, petition-response, spatial locus) and T2 maps mercy's constitutional a… |
| 398 | OBSERVATION | The perceptive engagement pattern reveals that forgiveness is **not primarily perceptive in its operation** — it does not primarily function… |
| 1025 | OBSERVATION | The sequences reveal a common structural logic: **fellowship operates as a prerequisite-to-participation mechanism** (finding 062-SEQUE-001)… |
| 2185 | SYNTHESIS_INTER_TIER | T3's finding that compassion is the motivational ground of conscientiousness explains the co-occurrence pattern in T6. Conscience (T3.9) and… |
| 1047 | OBSERVATION | Based on the available evidence:  - **Fellowship vs. unity:** A distinction of *direction and process* — fellowship is the process of joinin… |
| 1611 | SYNTHESIS_INTER_TIER | T3 shows mercy activating the full faculty system (perception, cognition, memory, affect, volition, agency, moral evaluation, conscience, co… |
| 2207 | SYNTHESIS_INTER_TIER | T2's origin analysis (grace does not originate in the human constitutional system — it arrives from God) and T4's directional analysis (God-… |
| 1606 | SYNTHESIS_INTER_TIER | T2 maps mercy's constitutional locations (soul, mind, heart, body, spirit-soul interface) and T3 maps its faculty engagements. Reading toget… |
| 1232 | SYNTHESIS_INTER_TIER | T2's constitutional movement (six-step sequence) and T5's transformation sequences (positive arc and moral awareness arc) describe the same … |
| 421 | OBSERVATION | **Enables conscientiousness:** Received divine forgiveness enables a more integrated response in the forgiver — the awareness of received fo… |
| 1230 | SYNTHESIS_INTER_TIER | T2 identified the constitutional movement of goodness from Spirit-level through soul and heart to outward expression (six-step sequence, Q&A… |
| 2393 | SYNTHESIS_INTER_TIER | T3 identifies the new covenant's faculty-level effect as the transformation of volition (from called-for to liberated — Q&A-085) and the pro… |
| 413 | OBSERVATION | The motivational engagement pattern reveals something structurally significant: forgiveness is **both a motivational product and a motivatio… |
| 2878 | SYNTHESIS_INTER_TIER | The relational interfaces (T4 — divine-initiative, human-responsive, covenantal scope) and the formation arc (T5 — constitutive endowment, s… |
| 1218 | SYNTHESIS_INTRA_TIER | T2 as a whole reveals that goodness has a comprehensive multi-level constitutional presence — from Spirit-level origin through soul-orientat… |
| 2375 | SYNTHESIS_INTRA_TIER | T2 as a whole reveals that covenant operates across the full constitutional range of the inner person with no single exclusive location. The… |
| 2389 | SYNTHESIS_INTER_TIER | T2 identifies a shift in constitutional origin across the covenant trajectory: from external bestowal (Noahic) to bilateral reception (Sinai… |
| 2376 | SYNTHESIS_INTRA_TIER | T3 as a whole reveals that covenant comprehensively engages the inner faculties but with a specific structural bias: the faculties it most d… |
| 2392 | SYNTHESIS_INTER_TIER | T3 reveals that the inner faculties covenant most deeply engages are Other-oriented (relational capacity, conscience, moral evaluation, memo… |
| 2877 | SYNTHESIS_INTER_TIER | The faculty engagement pattern (T3 — hearing precedes giving, memory is narrative-temporal, affect is at source and target, conscientiousnes… |
| 857 | OBSERVATION | Yes — conscience is the faculty most directly engaged by the penitential-relational mode of contrition. The conscience is the inner witness … |

### SD_POINTER — 37 no-hook

| id | type/label | text |
|---|---|---|
| 426 | SP-062-001 | SP-062-001 R43 desire (raised in Unit Unit 5) |
| 418 | SP-030-001 | SP-030-001 R105 (lust) (raised in Unit Unit 2) |
| 420 | SP-030-003 | SP-030-003 R061 (fear) (raised in Unit Unit 5) |
| 421 | SP-030-004 | SP-030-004 R123 (pride) (raised in Unit Unit 5) |
| 419 | SP-030-002 | SP-030-002 R151 (sorrow) and R062 (fellowship) (raised in Unit Unit 5) |
| 464 | SP-064-T2-002 | SP-064-T2-002 [Catalogue v2 §11 Session-D implication] The constitutional movement sequence (T2.10) — a map for the forgiveness chapter |
| 465 | SP-064-T2-003 | SP-064-T2-003 [Catalogue v2 §11 Session-D implication] The conscience-resolution framing (T3.9) — a new way to describe forgiveness's deepes… |
| 434 | SP-064-001 | SP-064-001 R122 (prayer) and/or R130 (reconciliation) — or descriptive target: horizontal-vertical worship ordering (raised in Unit Unit 7 G… |
| 466 | SP-064-T2-004 | SP-064-T2-004 [Catalogue v2 §11 Session-D implication] The grace-mercy-forgiveness dimensional cluster (T6.7) — structural positioning for t… |
| 467 | SP-064-T2-005 | SP-064-T2-005 [Catalogue v2 §11 Session-D implication] The threefold eschatological anticipation (T5.6) — eschatological architecture for th… |
| 439 | SP-067-023 | SP-067-023 [Migrated from catalogue GAP-S3-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where … |
| 438 | SP-067-022 | SP-067-022 [Migrated from catalogue GAP-S2-002 2026-04-28 — programme-level methodology question, not a per-word analytical question] Does t… |
| 114 | DIM-112-SD001 | DIM-112-SD001 C01 Theological/Divine-Human density: 62 of 297 groups (21%) reflect a structural reality — the primary inner-being terms are … |
| 124 | DIM-42-SD002 | DIM-42-SD002 Morally negative joy/gladness appears across multiple C03 registries: 355-002 and 365-002 (R97), 1096-001 (R132), 634-002 (R186… |
| 127 | DIM-8-SD001 | DIM-8-SD001 Programme-wide: groups where God is the subject of a volitional or desiderative act are systematically misclassified as Volition… |
| 128 | DIM-43-SD001 | DIM-43-SD001 C04 desiderative density is 62% — 65 of 172 groups carry non-desiderative primary content. Question: is the desiderative vocabu… |
| 441 | SP-067-025 | SP-067-025 [Migrated from catalogue GAP-S4-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where … |
| 294 | DIM-103-SD008 | DIM-103-SD008 Eccl 9:6 — love, hatred, and envy listed as the three constitutive inner orientations that cease at death. This triadic struct… |
| 141 | DIM-57-SD002 | DIM-57-SD002 The Sin & Vice / Moral/Conscience boundary was systematically refined in C11: Sin & Vice = inner condition of moral failure (wi… |
| 123 | DIM-42-SD001 | DIM-42-SD001 The Theological/Divine-Human cluster within delight/joy registries — God's pleasure/displeasure as the criterion of acceptance … |
| 130 | DIM-61-SD001 | DIM-61-SD001 C06 fear cluster shows a tripartite dimension pattern: fear-as-God-ward-orientation (Spiritual/God-ward ~18 groups), fear-as-in… |
| 162 | DIM-6-SD001 | DIM-6-SD001 C16 contains a substantial concentration of GOD-dominant Agency/Power and Transformation groups across anointing, consecration, … |
| 312 | DIM-103-SD026 | DIM-103-SD026 C20 cluster (strength/might/authority/dominion — Regs 187/198/197/199) shares all 8 dimensions with love and co-occurs in 69-1… |
| 140 | DIM-57-SD001 | DIM-57-SD001 The Affective/Emotional dimension appears extensively in C11 (15 groups assigned) but was absent from C10 assignments, despite … |
| 436 | SP-067-020 | SP-067-020 [Migrated from catalogue GAP-S1-002 2026-04-28 — programme-level methodology question, not a per-word analytical question] Does t… |
| 437 | SP-067-021 | SP-067-021 [Migrated from catalogue GAP-S2-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where … |
| 166 | DIM-52-SD001 | DIM-52-SD001 C18 produces 9 groups assigned Divine-Human Correspondence across division (5), rejection (1), strife (1), and unity (2) — 20% … |
| 435 | SP-067-019 | SP-067-019 [Migrated from catalogue GAP-S1-001 2026-04-28 — programme-level methodology question, not a per-word analytical question] Where … |
| 225 | DIM-068-SD007 | DIM-068-SD007 C11 moral failure cluster cooccurrence: evil (57, 12 verses), sin (147, 6 verses), transgression (162, 6 verses), deceit (40, … |
| 327 | DIM-064-SD013 | DIM-064-SD013 The permitting/welcome sense of *aphiēmi* (group 5378-001) names the inner posture of non-obstruction and openness — letting s… |
| 169 | DIM-19-SD001 | DIM-19-SD001 C19 produces 37 of 97 groups (38%) assigned Divine-Human Correspondence — the highest cluster-level concentration in the progra… |
| 412 | SP-067-013 | SP-067-013 R197 (authority) ranks third in co-occurrence with R67 (goodness) at 17 shared verses, above joy, soul, and wisdom. This is unexp… |
| 336 | DIM-064-SD022 | DIM-064-SD022 6 shared verses between forgiveness (064) and evil (057). Forgiveness is structurally the response to evil done — the two regi… |
| 335 | DIM-064-SD021 | DIM-064-SD021 8 shared verses between forgiveness (064) and desire (043). The leave/abandon groups (5376) contain verses about leaving behin… |
| 121 | DIM-160-SD001 | DIM-160-SD001 Directionally-determined inner faculty pattern — a recurring structural principle identified across C02 registries (108, 127, … |
| 232 | DIM-068-SD014 | DIM-068-SD014 C17 cluster synthesis question: all C17 sibling registries appear in grace's cooccurrence signal — peace (117, 10), kindness (… |
| 334 | DIM-064-SD020 | DIM-064-SD020 9 shared verses between forgiveness (064) and faith (059). The NT pattern is consistent: forgiveness is received through faith… |

### SB_FINDING — 25 no-hook

| id | type/label | text |
|---|---|---|
| 480 | SB-068-T2-012 | SB-068-T2-012 [Catalogue v2 gap surfaced 2026-04-30] T2.8.2 (Body — Deposit) — status S, notation: (none).  Prompt: What evidence supports o… |
| 499 | SB-068-T2-031 | SB-068-T2-031 [Catalogue v2 gap surfaced 2026-04-30] T6.5.2 (Distinctions) — status S, notation: (none).  Prompt: Where apparent overlap exi… |
| 503 | SB-068-T2-035 | SB-068-T2-035 [Catalogue v2 gap surfaced 2026-04-30] T7.1.8 (Lexical and Semantic Analysis) — status P, notation: Gap identified.  Prompt: W… |
| 484 | SB-068-T2-016 | SB-068-T2-016 [Catalogue v2 gap surfaced 2026-04-30] T3.3.3 (Memory) — status S, notation: Gap identified.  Prompt: What does the pattern re… |
| 492 | SB-068-T2-024 | SB-068-T2-024 [Catalogue v2 gap surfaced 2026-04-30] T4.4.3 (Human Interface — Receiving) — status S, notation: (none).  Prompt: What is the… |
| 533 | SB-030-T2-009 | SB-030-T2-009 [Catalogue v2 gap surfaced 2026-04-30] T2.4.2 (Mind) — status S, notation: Gap identified.  Prompt: What does mind-location re… |
| 537 | SB-030-T2-013 | SB-030-T2-013 [Catalogue v2 gap surfaced 2026-04-30] T2.5.3 (Other Soul Subsets) — status A, notation: Gap identified.  Prompt: If the evide… |
| 539 | SB-030-T2-015 | SB-030-T2-015 [Catalogue v2 gap surfaced 2026-04-30] T2.8.2 (Body — Deposit) — status S, notation: Gap identified.  Prompt: What evidence su… |
| 540 | SB-030-T2-016 | SB-030-T2-016 [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status A, notation: Gap identified.  Prompt: If the evidence … |
| 594 | SB-062-T2-014 | SB-062-T2-014 [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status A, notation: Gap identified.  Prompt: If the evidence … |
| 519 | SB-023-T2-015 | SB-023-T2-015 [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status S, notation: Consistent with prior analysi… |
| 491 | SB-068-T2-023 | SB-068-T2-023 [Catalogue v2 gap surfaced 2026-04-30] T4.4.2 (Human Interface — Receiving) — status P, notation: Gap identified.  Prompt: Wha… |
| 455 | SB-064-T2-013 | SB-064-T2-013 [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status S, notation: Gap identified.  Prompt: If t… |
| 575 | SB-030-T2-051 | SB-030-T2-051 [Catalogue v2 gap surfaced 2026-04-30] T6.7.3 (Dimensional Sharing) — status A, notation: Gap identified.  Prompt: If dimensio… |
| 534 | SB-030-T2-010 | SB-030-T2-010 [Catalogue v2 gap surfaced 2026-04-30] T2.4.3 (Mind) — status A, notation: Gap identified.  Prompt: If the evidence is silent … |
| 591 | SB-062-T2-011 | SB-062-T2-011 [Catalogue v2 gap surfaced 2026-04-30] T2.5.2 (Other Soul Subsets) — status P, notation: Gap identified.  Prompt: If so, what … |
| 608 | SB-062-T2-028 | SB-062-T2-028 [Catalogue v2 gap surfaced 2026-04-30] T6.7.3 (Dimensional Sharing) — status A, notation: Gap identified.  Prompt: If dimensio… |
| 571 | SB-030-T2-047 | SB-030-T2-047 [Catalogue v2 gap surfaced 2026-04-30] T6.5.2 (Distinctions) — status S, notation: Gap identified.  Prompt: Where the evidence… |
| 588 | SB-062-T2-008 | SB-062-T2-008 [Catalogue v2 gap surfaced 2026-04-30] T1.6.3 (Sustained Effect) — status P, notation: Gap identified.  Prompt: Does the susta… |
| 504 | SB-068-T2-036 | SB-068-T2-036 [Catalogue v2 gap surfaced 2026-04-30] T7.3.4 (Human Science Frameworks) — status P, notation: Gap identified.  Prompt: Does t… |
| 511 | SB-023-T2-007 | SB-023-T2-007 [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status P, notation: Gap identified.  Prompt: If the evidence … |
| 587 | SB-062-T2-007 | SB-062-T2-007 [Catalogue v2 gap surfaced 2026-04-30] T1.5.3 (Immediate Response) — status A, notation: Gap identified.  Prompt: Where the ve… |
| 568 | SB-030-T2-044 | SB-030-T2-044 [Catalogue v2 gap surfaced 2026-04-30] T5.6.3 (Eschatological Trajectory) — status A, notation: Gap identified.  Prompt: If th… |
| 561 | SB-030-T2-037 | SB-030-T2-037 [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status A, notation: Gap identified.  Prompt: If t… |
| 462 | SB-064-T2-020 | SB-064-T2-020 [Catalogue v2 gap surfaced 2026-04-30] T7.3.3 (Human Science Frameworks) — status S, notation: Gap identified.  Prompt: Where … |

