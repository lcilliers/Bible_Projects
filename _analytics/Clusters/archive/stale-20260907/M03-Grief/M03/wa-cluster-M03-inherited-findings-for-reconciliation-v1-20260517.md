# M03 Grief, Sorrow and Mourning — Inherited findings for Phase 10 reconciliation

**Generated:** 2026-05-17T04:48:07Z  
**Cluster:** `M03` (Grief) · status=Analysis - In Progress · version=v6  
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §13 (Phase 10 — Inherited-finding reconciliation)  
**Source:** `database/bible_research.db`  

**Scope:** every inherited Session B finding, research flag, and Session D pointer attached to this cluster's contributor registries that has **not been resolved** by the legacy pipeline. AI's Phase 10 task is to assign a disposition per row (see §13.2 of the instruction). Resolved rows (`status='resolved_*'` or `resolved=1`) are excluded.

**Linkage path:** cluster's `mti_terms` → `owning_registry_fk` → `word_registry` → matching rows in `wa_session_b_findings`, `wa_session_research_flags`, and `session_d_*`.

---

## Summary

| Source | Total unresolved |
|---|---:|
| `wa_session_b_findings` (status IN (open, pending, confirmed)) | **189** |
| `wa_session_research_flags` (resolved=0) | **58** |
| `session_d_term_links` (this cluster's terms) | **0** |

**Contributor registries:** 12

| no | registry_id | word |
|---:|---:|---|
| 2 | 2 | agony |
| 5 | 5 | anguish |
| 13 | 13 | bitterness |
| 23 | 23 | compassion |
| 51 | 51 | distress |
| 71 | 71 | grief |
| 72 | 72 | groaning |
| 86 | 86 | impurity |
| 108 | 108 | meditation |
| 113 | 113 | mourning |
| 151 | 151 | sorrow |
| 188 | 188 | weeping |

**Finding types in unresolved set:**

- `OBSERVATION`: 152
- `SYNTHESIS_INTER_TIER`: 21
- `DIMENSION_REVIEW`: 9
- `SYNTHESIS_INTRA_TIER`: 7

**Flag codes in unresolved set:**

- `SD_POINTER`: 30
- `SB_FINDING`: 20
- `BOUNDARY_DECISION_PENDING`: 3
- `VERSE_EVIDENCE_BREADTH_NOTE`: 2
- `DIMREVIEW_SESSION_D`: 2
- `PH2_DATA_ERROR`: 1

---

## Disposition options (AI assigns one per row)

Per v2_0 §13.2:

| Disposition | Meaning |
|---|---|
| `RESOLVED-BY-CATALOGUE` | finding is already captured in one of the new cluster_finding rows (T0–T7) — name the cluster_finding id(s) |
| `FOLD-INTO-PROMPT` | finding adds new evidence to an existing cluster_finding — name target prompt + scope |
| `NEW-CLUSTER-FINDING` | finding is real new evidence that doesn't fit any existing prompt — name a target T-code |
| `SUPERSEDED` | finding was authored under the pre-cluster-pivot lens and is no longer relevant — name replacing cluster_finding |
| `CARRY-TO-SESSION-D` | finding is cross-cluster / cross-registry and belongs to Session D, not this cluster |
| `RESEARCHER-DECISION` | AI cannot decide — surface for researcher |

---

## §1. Unresolved Session B findings

### R002 agony — 4 unresolved

#### sbf.id=56 · finding_id='DIM-002-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Registry 2 (agony) contains two analytically distinct sub-clusters: (1) the agōn- word family (6 terms: G0075, G0073, G0464, G1864, G2610, G4865), all Volitional/Will, naming directed spiritual striving rather than suffering — these are misaligned with C05's dominant suffering theme; (2) the basanizō/basanismos/basanos torment family (5 terms), all Affective/Emotional, naming eschatological and post-mortem suffering. Session B should treat these sub-clusters separately.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=57 · finding_id='DIM-002-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Groups 4652-001 and 4654-001 (H2258A cha.vol and H2258B cha.vo.lah, pledge): assigned Moral/Conscience but the inner-being filter is borderline — pledge-handling is primarily an external economic act whose moral significance is diagnostic of inner character rather than a direct inner-being engagement. Session B should examine whether the verse evidence sustains the Moral/Conscience assignment or whether these groups are better treated as externalised moral diagnostics.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=58 · finding_id='DIM-002-003' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Group 4651-001 (H2259 cho.vel, pilot): assigned Spiritual/God-ward but the boundary with Volitional/Will is uncertain. The helmsman figure calling the crew to prayer in extremity may name an authority/directional dimension rather than a personal God-ward orientation. Session B should examine the verse evidence to determine whether the inner-being engagement is volitional direction, spiritual appeal, or some combination.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=64 · finding_id='DIM-002-004' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Group 4595-001 (H4865 mish.be.tsot, filigree): assigned Character/Disposition on the basis of the metaphor of inner adornment with honour. Single-verse term with 8 set-aside verses; the description is working from a narrow evidential base. Session B should verify whether the verse evidence sustains the character/adornment reading or whether the inner-being application is marginal.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R013 bitterness — 1 unresolved

#### sbf.id=73 · finding_id='DIM-13-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Bitterness in Reg 13 operates in two structural registers: (a) affective quality — bitter grief, anguish, affliction (something that happens to the inner person), and (b) dispositional-character state — root of bitterness, bitter jealousy as heart-state, bitter rebellion (something the inner person becomes). Session B should examine whether biblical bitterness is primarily an experience or a condition, and whether the two registers are sequential or independent.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R023 compassion — 181 unresolved

#### sbf.id=169 · finding_id='DIM-23-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-11'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.9-2026-04-09`

> Group 733-001 (ni.chum — compassionate comfort, Reg 23) is anchored by Hos 11:8: "my heart recoils within me; my compassion grows warm and tender." This verse names the divine inner life with visceral specificity — the heart recoiling, compassion warming. Session B for Reg 23 should examine whether this visceral inner-movement language for God represents a unique category within the compassion vocabulary: divine inner-being experience described through embodied sensation. The question for Session B is whether the compassion vocabulary of Reg 23 contains a sub-pattern of "visceral inner movement" terms (splanchnizō, ni.chum, ra.cha.mim) that share a somatic/embodied description of the inner compassion movement, and whether this sub-pattern spans the divine-human boundary (both God and humans described as "moved within" by compassion).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=633 · finding_id='OBS-023-T2-001' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T0.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The verse evidence for compassion reveals God's character with unusual explicitness and density. Several distinct qualities emerge from the data:
> 
> **God is constitutively compassionate — not occasionally so.** The Exodus 34:6 formula (rachum ve-channum — "merciful and gracious") is a divine self-declaration, not a description of a particular act. It names God's character before and apart from any specific occasion. This formula is cited or echoed across the entire OT corpus: Neh 9:17; Psa 86:15; 103:8; 145:8; Joel 2:13; Jon 4:2 (SD-017). God's compassion is not a response contingent on circumstances — it is what God is.
> 
> **God's compassion is visceral and somatic in its scriptural description.** The RACHAM/SPLANCHN root families describe divine compassion in the language of bodily inner movement. Hos 11:8 uses the most striking formulation: "My heart recoils within me; my compassion grows warm and tender" (ni.chum). The divine inner life is described as deliberative — God's compassion contends with and overcomes the competing inner disposition of judgment (Pass 2, FRAMEWORK SIGNAL on ni.chum). This is not the language of detached decree; it is the language of felt, warm, bodily-imaged inner experience.
> 
> **God's compassion has a maternal character.** H7356A ra.cham (group 729-001) grounds divine compassion in the image of the womb: "carried from the womb" (Isa 46:3). The womb is the space of origination, protection, and intimate care. God's compassion is described in terms of what a mother's body does for the child she carries — the most interior, involuntary, and complete form of care the vocabulary has access to.
> 
> **God's compassion is temporally asymmetric with judgment.** Isa 54:8 establishes an explicit temporal contrast: a moment of anger versus everlasting chesed/racham. Judgment is temporary; compassion is permanent (SD-019). This asymmetry is not incidental — it is a structural statement about which characteristic is more fundamental to God's inner nature.
> 
> **God's compassion is sovereignly free.** Rom 9:15 (oikteirō) — "I will have compassion on whom I have compassion" — grounds compassion in divine sovereignty, not in human condition or merit. Compassion flows from what God is, not from what the recipient has done or become.
> 
> **God's compassion is deep beyond ordinary range.** The NT hapax legomenon polusplanchnos (Jas 5:11) — "very compassionate" — was coined because existing vocabulary was insufficient to name the depth of God's compassion at the point of maximum permitted suffering (SD-014). The intensity of the coinage is itself data about the character being named.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=634 · finding_id='OBS-023-T2-002' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T0.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Scripture attributes compassion to God with unusual directness, frequency, and vocabulary density. The GOD_AS_SUBJECT flag is warranted for H2587 chan.nun (13 occurrences, almost exclusively divine epithet), H2617B che.sed (predominant divine referent across Psalter, prophets, and historical books), H5150 ni.chum (2/3 occurrences divine), H7358 re.chem (God as actor over the womb in ~9/25 occurrences), H2551 chem.lah (Gen 19:16), G3627 oikteirō (Rom 9:15, exclusively divine sovereignty), G4697 splanchnizō (Jesus as primary subject in Gospels), and G4184 polusplanchnos (Jas 5:11) — as confirmed in the Pass 2 God-as-Subject table.
> 
> What does this attribution reveal about the significance of compassion in the human person?
> 
> Two implications follow from the data:
> 
> First, compassion in the human person is a reflection of something that belongs primarily and essentially to God. The attribution of compassion to God is not metaphorical embellishment — it is the primary usage, and human compassion is derivative. The human person's capacity for compassion is therefore not merely a natural emotional response but a participation in the character of the one in whose image the person is made. This is reinforced by the fact that the RACHAM root is anatomical (re.chem, womb) — the human person's body is the ground from which the vocabulary of divine compassion is drawn. The direction of meaning flows from the human body to the divine inner life, but the direction of significance flows the other way: what the human experiences somatically, God possesses constitutively.
> 
> Second, the divine character formula of Exod 34:6 (rachum ve-channum) functions as the standard of inner being that human compassion aspires to reflect. Joel 2:13 explicitly deploys this formula as the ground for human repentance and heart-rending ("return to the LORD your God, for he is gracious and merciful" — SD-029). The divine character is not merely the source of compassion but the norm against which human compassion is measured.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=635 · finding_id='OBS-023-T2-003' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T0.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data addresses this prompt with evidence sufficient for several observations, though the question of original created purpose is not directly stated in the verse evidence and must be assembled from the data's implications.
> 
> **Compassion equips the person to face outward toward the suffering of others.** The registry description states: "Compassion always faces outward toward the one suffering and produces action." This is the functional description confirmed across the vocabulary. Splanchnizō (G4697) is consistently triggered by the sight of suffering — crowds without a shepherd, a widow's grief, a leper's condition, a wounded stranger (Pass 1, group 730-001). Compassion equips the person to be moved by what they see in another, not merely to observe it from a safe distance.
> 
> **Compassion equips the person to participate in another's experience.** The SYM-PATH root family (sumpatheō, sumpaschō, sumpathēs) names compassion as genuine entry into another's experience — suffering-with, not merely sympathising-from-outside. 1 Pet 3:8 places sumpathēs (sympathetic) as a defining character quality in the list of community virtues. This equips the person for genuine relational solidarity.
> 
> **Compassion equips the person to bear the image of God in concrete social and relational contexts.** The eleēmosunē vocabulary (G1654) shows how compassion arrives at its normative social form — almsgiving. Luke 11:41 grounds almsgiving in inner purity; Matt 6:2-4 addresses the manner of giving. The inner quality of compassion is what gives the outward act its validity (Pass 1, term 20 sense analysis). Compassion equips the person to embody in social practice what God is in his inner character.
> 
> **What is missing (P):** The data does not directly address whether compassion as created purpose is specifically oriented toward a pre-fall relational ideal or whether its current expression is already conditioned by the presence of suffering (i.e., whether compassion presupposes a fallen world). This is named explicitly at T0.2 Prompt 2.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=636 · finding_id='OBS-023-T2-004' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T0.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides partial evidence.
> 
> **Eschatological signals present:** SD-012 identifies Rom 8:17 — "if we suffer with him (sumpaschō) we may also be glorified with him (syndoxazō)" — as placing compassion/fellow-suffering within an explicitly eschatological framework. Suffering-with-Christ is named as the condition of glorification-with-Christ. This is the clearest evidence in the data that the compassion vocabulary carries a future-orientation: present fellow-suffering is oriented toward future shared glory.
> 
> Jas 5:11 (polusplanchnos) connects divine deep compassion to the "purpose of the Lord" in the context of endurance and suffering, suggesting that the full expression of compassion belongs to a telos not yet reached.
> 
> **What is missing (P):** The data does not contain a verse that explicitly names compassion as moving toward eschatological fullness in the human person — as something the person is becoming, not only doing. The eschatological trajectory is more visible in the divine direction (God's everlasting chesed) and in the sumpaschō/syndoxazō frame, than in a direct statement about the human person's compassion moving toward completeness. This is a genuine gap; SD-012 partially addresses it but does not close it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=637 · finding_id='OBS-023-T2-005' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T0.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Compassion expresses the divine image in the human person through a specific and unusual mechanism: **the human body is the etymological ground of the divine attribute.**
> 
> The RACHAM root (H7355, H7356A, H7356B) names both the womb (anatomical) and compassion (abstract). The relationship is not the usual one where an abstract quality is later extended metaphorically to the body — it is the reverse. The abstract term (ra.cham, compassion) is named after the concrete anatomical reality (re.chem, womb). As the Pass 1 term analysis states: "the abstract (compassion) is named after the concrete (womb), not the other way around. This is unusual in Hebrew word formation and gives the compassion vocabulary a somatic grounding that is built into the language itself rather than being a later metaphorical extension."
> 
> This means that the divine image expressed in compassion is not a purely spiritual quality projected downward into the human — it is a quality named upward from the human body into the divine character. When Scripture says God is rachum (compassionate), it is drawing on the most intimate human bodily experience — the experience of carrying life from within — to describe what God is in his inner being.
> 
> The aspect of the divine image instantiated is therefore: **the capacity for interior, involuntary, body-grounded movement toward the other.** Compassion as image-bearer expression is not merely benevolent feeling — it is the quality of being moved from within, constitutively, toward those who need.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=638 · finding_id='OBS-023-T2-006' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T0.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The evidence strongly suggests genuine sharing, not merely analogical correspondence.
> 
> Three lines of evidence support this:
> 
> **1. The same vocabulary applies to both.** Splanchnizō (G4697) is used of Jesus (Synoptic Gospels, 11 occurrences) and of the human person (Luke 10:33 — the Good Samaritan; Luke 15:20 — the father of the prodigal; Matt 18:27 — the king in the parable). The vocabulary does not bifurcate into a divine term and a human term — the same term governs both. This implies the inner-being reality being named is the same, not merely analogous.
> 
> **2. The sumpatheō vocabulary grounds the sharing Christologically.** Heb 4:15 names Christ's capacity to sympathise (sumpatheō) with human weaknesses, grounded in his own experience of temptation. The priestly solidarity is genuine: Christ shares in the human condition in order to share in the human inner experience of suffering. This is not analogy — it is participation (SD-002).
> 
> **3. The mirroring principle.** 2 Sam 22:26 / Psa 18:25 (H2616A cha.sad): "With the merciful you show yourself merciful." This establishes that God's compassionate disposition toward the human person is itself responsive to the person's inner character. The sharing runs in both directions: not only does God's compassion establish the pattern for human compassion, but human compassionate character draws out corresponding divine response (SD-007).
> 
> The data does not support a reading in which compassion is exclusively a creaturely analogue — the vocabulary, the Christological grounding, and the mirroring principle all point toward genuine sharing across the Creator-creature boundary.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=639 · finding_id='OBS-023-T2-007' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T0.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Two contrasting cases in the data address this directly:
> 
> **Presence — Lam 4:10:** The adjectival form ra.cha.ma.ni (compassionate) names the settled character quality of compassion. The verse describes compassionate women (ra.cha.ma.ni) doing something that violates the deepest expression of compassionate character — boiling their own children in the siege of Jerusalem. The data's observation is precise: "These are compassionate women — yet this is what they did. The term names the inner quality at the moment of its most catastrophic inversion." The verse reveals that compassion as a character quality is not indestructible — extreme external pressure can force its violation. This implies that the divine image, as expressed in compassion, can be damaged, distorted, or temporarily overwhelmed by circumstances of sufficient severity.
> 
> **Absence — Rev 3:17 (eleeinos):** The Laodiceans are described as pitiable (eleeinos) — the condition that ought to evoke compassion — without recognising their own condition. The data notes: "The word names the failure of the second condition. Compassion requires both the disposition (in the giver) and the recognition of need (in the receiver or an observer)." Self-deceived prosperity is identified as the inner state that prevents both the recognition of one's own pitiable condition and, by implication, the capacity to perceive and respond to the pitiable condition of others (SD-015). The absence of compassion-awareness signals a condition in which the divine image is obscured by self-sufficiency.
> 
> Taken together: the presence of compassion, even where it is violated, reveals that the image remains structurally in place. The absence of compassion-perception, particularly when masked by prosperity and self-deception, reveals an image condition that has been occluded at the level of inner orientation.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=640 · finding_id='OBS-023-T2-008' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T0.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes. The data contains clear typological uses, operating in multiple directions.
> 
> **Christological typology:** The splanchnizō vocabulary in the Gospels functions typologically in that Jesus's compassion-movements enact what the Hebrew womb-vocabulary had named as God's character. The Synoptic pattern — Jesus "moved with compassion" before healing, feeding, and restoring — is not merely biographical detail. It is the embodied enactment of the divine character formula of Exod 34:6. Jesus's compassion-in-action is the Christological realisation of what the OT had named as God's inner disposition. The Good Samaritan parable (Luke 10:33 — splanchnizō) deploys compassion typologically as well: the Samaritan's act of compassion answers the question "who is my neighbour?" in a way that points beyond the immediate story to the nature of covenant membership and the shape of the new humanity (SD-010).
> 
> **Covenantal typology:** The Exod 34:6 formula (rachum ve-channum) operates as a covenantal anchor — it is cited whenever the community's relationship with God is re-established or renewed (Neh 9:17; Joel 2:13; Jon 4:2). The compassion of God is the covenantal ground that makes return and restoration possible. In this usage, compassion is not merely a divine attribute — it is the character that holds the covenant open at the moment of its violation.
> 
> **Eschatological typology:** Rom 8:17 (sumpaschō → syndoxazō) places present fellow-suffering within an eschatological frame: suffering-with-Christ now participates in glory-with-Christ then. Jas 5:11 (polusplanchnos) connects divine deep compassion to the "purpose (telos) of the Lord" — present suffering is held within a divine compassionate purpose that is not yet fully disclosed.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=641 · finding_id='OBS-023-T2-009' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T0.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals that the typological direction runs primarily from divine to human — but with a distinctive structural complication.
> 
> **Primary direction: divine to human.** The Exod 34:6 formula is the originating divine self-declaration that establishes the pattern. Joel 2:13 makes the direction explicit: God's compassion-character is cited as the reason the human is to "rend your hearts and return." The divine instance establishes the norm; human compassion is the responsive pattern. Similarly, the splanchnizō pattern in the Gospels shows Jesus's compassion establishing the pattern that is then named as the shape of neighbour-love (Luke 10:33 — "go and do likewise," v.37).
> 
> **Structural complication: the vocabulary runs upward.** As noted at T0.3 Prompt 1, the RACHAM root moves from the anatomical human (re.chem, womb) to the divine attribute (ra.cham, compassion). This means that at the level of vocabulary origin, the human bodily experience is the ground from which the divine character is named. The typological direction of the text (divine → human) and the etymological direction of the vocabulary (human body → divine attribute) run in opposite directions.
> 
> This is not a contradiction — it is analytically significant. The divine character of compassion is named through the human body precisely because that body is made in the image of God. The womb-language points back to the source from which it was drawn: what the human person experiences as the most intimate bodily care is what God is in his essential inner character. The typology is therefore bidirectional at a deep level, even if the normative movement of the text runs divine-to-human.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=642 · finding_id='OBS-023-T2-010' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The characteristic is named **compassion** in the programme (Registry 23, word field: "compassion"). The name signals three things about its essential nature immediately:
> 
> **1. Movement, not merely feeling.** "Compassion" derives from the Latin *com* (with) + *pati* (to suffer) — suffering-with. The name encodes participation, not observation. This aligns precisely with the vocabulary the data confirms: splanchnizō (visceral inner movement toward the suffering person), sumpatheō (entering into another's experience), sumpaschō (suffering together). The name announces that compassion is not a passive emotional state but an inner movement directed outward.
> 
> **2. The other as the defining reference point.** Compassion cannot exist without a suffering other. Unlike characteristics that name a quality the person possesses independently (e.g., integrity, purity), compassion is relationally constituted — it requires an object. The name already encodes the outward orientation confirmed by the registry description: "Compassion always faces outward toward the one suffering and produces action."
> 
> **3. Bodily resonance.** The etymology of the English name and the Hebrew root vocabulary converge on the same point: compassion is felt in the body. The womb-root (RACHAM) and the entrails-root (SPLANCHN) both name the abdominal interior as the seat of compassion's stirring. The name "compassion" in English carries this somatic resonance indirectly (through the Latin *pati* — to endure, to undergo physically); the Hebrew and Greek terms carry it directly and anatomically.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=643 · finding_id='OBS-023-T2-011' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The primary terms immediately signal the following at the definitional level:
> 
> **Hebrew:** The dominant primary terms are H7356B ra.cha.mim (compassion, 39 XREF occurrences, plural noun), H7355 ra.cham (to have compassion, 43 XREF), and H7349 ra.chum (compassionate, 13 XREF). All three are from the RACHAM root, which is the same root as H7358 re.chem (womb). Before any deeper analysis, this root tells us: compassion is named after the most intimate space of the human body. Its definitional ground is somatic, maternal, and generative. The plural form ra.cha.mim (mercies/compassions) signals that compassion is not a single act but a settled, multiple, ongoing disposition — grammatically plural in its most common form.
> 
> **Greek:** The primary term is G4697 splanchnizō (to pity, 12 active occurrences). Its root is splanchnon (G4698, entrails/affections) — the abdominal organs. Before any deeper analysis, this tells us: the Greek vocabulary also grounds compassion in the body's interior. The compound G4184 polusplanchnos (very compassionate) intensifies this: literally "of many/great entrails." At definitional entry, the Greek term already announces that compassion is a gut-movement, a bodily stirring, not a cognitive determination.
> 
> The convergence of the Hebrew and Greek primary terms at the definitional level is itself analytically significant: two distinct root families, drawn from two linguistic traditions, both independently ground compassion in the body's interior cavity (womb; entrails). This is not coincidence — it is a shared anthropological perception across linguistic traditions that compassion is felt from the inside, in the deepest bodily space.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=644 · finding_id='OBS-023-T2-012' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> All three implications are present and carry significant analytical weight:
> 
> **Directional:** The name encodes a specific direction — outward, toward the suffering other. Compassion does not turn inward (unlike grief or shame); it faces the other. The registry description confirms: "Compassion always faces outward toward the one suffering." The vocabulary confirms it: splanchnizō is always triggered by the sight of the other's condition; ra.cham always has an object. The enquiry is oriented from the outset toward the relational interface — T4 will be particularly rich.
> 
> **Relational:** The name presupposes a two-party structure — the one moved and the one suffered-with. Unlike forgiveness (which also presupposes two parties but in a judicial/moral frame), compassion's relational structure is one of vulnerability and need on one side, and responsive movement on the other. The name does not encode a moral claim (debt, guilt, obligation) — it encodes a condition (suffering, need) that calls forth a response. This orients the enquiry away from judicial frameworks and toward constitutional and affective ones.
> 
> **Constitutional:** The womb-root and entrails-root both point toward the deep inner body as the constitutional seat of compassion. This orients the enquiry toward T2 (constitutional location) with a strong prior signal: compassion will be located in the body's interior in a way that few characteristics in the programme are. The constitutional question is not merely whether compassion has a body-level expression — the root vocabulary indicates that the body is its originating ground.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=645 · finding_id='OBS-023-T2-013' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals that compassion is not a single kind of inner-being phenomenon — it operates across multiple kinds simultaneously, and the vocabulary differentiates them precisely.
> 
> **Compassion as constitutive character quality (disposition):** H7349 ra.chum (compassionate) and G4835 sumpathēs (sympathetic) are adjectival forms naming the settled character quality — what kind of person one is. Lam 4:10 uses ra.cha.ma.ni (compassionate women) to name a character type. The person who is ra.chum or sumpathēs is constitutively compassionate — it describes their inner being, not a single act.
> 
> **Compassion as inner movement (event/act):** G4697 splanchnizō and H5150 ni.chum both name the moment of compassion as a movement — a stirring, a kindling, a being-moved. Hos 11:8 ("my compassion grows warm and tender") captures the event quality: something happens inside at a specific moment. Splanchnizō in the Gospels consistently names a discrete event that precedes action.
> 
> **Compassion as condition of the one who needs it:** G1652 eleeinos (pitiful) names the condition that calls forth compassion — the pitiable state. This is not compassion itself but its proper object, and its presence in the vocabulary reveals that compassion's operation is constitutionally linked to a condition of need.
> 
> **Compassion as externalised act:** G1654 eleēmosunē (almsgiving) names the normalised outer form of compassion — the concrete act into which the inner movement arrives. The semantic development from inner pity to outer giving is encoded in this term's history (Pass 1).
> 
> **Summary:** Compassion in this registry is a layered inner-being phenomenon: a character disposition that generates event-movements when triggered by need, which produce outward acts. The vocabulary differentiates all three layers, and the distinction between them is analytically essential.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=646 · finding_id='OBS-023-T2-014' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Compassion has a clearly complex structure at first encounter. The vocabulary itself reveals four distinct root families, each naming a different constituent dimension:
> 
> 1. **RACHAM/SPLANCHN** — visceral, somatic, movement-compassion (womb/bowels origin): the inner-body stirring
> 2. **CHESED/CHANNUM** — covenantal, characterological, steadfast compassion (loyalty/faithfulness): the constitutive character quality of loyal, enduring care
> 3. **SYM-PATH** — participatory, solidarity compassion (shared-suffering/fellow-feeling): genuine entry into another's experience
> 4. **ELEEIN/CHUS** — relational, responsive compassion (pity/mercy/almsgiving): the response to perceived need, including its externalised form
> 
> These are not synonyms. They name genuinely different aspects of what the programme registers under "compassion." Pass 1 identifies these four families explicitly. SD-016 proposes a three-stage movement model (visceral stirring → mercy orientation → concrete act of giving) that assembles elements from RACHAM/SPLANCHN, ELEEIN, and the almsgiving vocabulary into a developmental sequence.
> 
> The structural complexity of compassion is therefore already visible at definitional entry. This has significant implications for T2 (where to locate each element constitutionally) and T3 (which faculties each element engages).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=647 · finding_id='OBS-023-T2-015' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Drawing directly from the registry description, the term analyses, and the group descriptions:
> 
> **Compassion is the inner-being movement of a person toward the suffering of another, arising from the deepest bodily and relational centre of the self, expressed as a felt stirring that produces orientation, action, and solidarity.** It is constitutively outward-facing: it cannot exist without an other who suffers. Its constitutional ground is somatic (womb/entrails), but its expression traverses the full constitutional range — from visceral bodily movement through affective response, moral evaluation, and volitional action, arriving at externalised gift or presence.
> 
> In the giver, compassion produces: inner movement (splanchnizō), warmth (ni.chum), a disposition of mercy (ra.cham), an orientation of loyal care (chesed), and a practical act of giving or presence (eleēmosunē, sumpatheō). In the receiver, compassion produces: the experience of being met in need, the possibility of restored relational standing, and (by implication from the data) a capacity to extend compassion to others (though the data addresses this only indirectly).
> 
> The characteristic's sb_classification in the programme is **Soul-body interface** — a classification confirmed by the vocabulary's grounding in the body's interior as the seat of compassion's movement.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=648 · finding_id='OBS-023-T2-016' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data surfaces two structural opposites, each operating at a different level:
> 
> **The judicial suspension of compassion — deliberate hardness:** H2347 chus appears most frequently in prohibition contexts: "your eye shall not pity" (Deut 7:16; 13:8; 19:13; Ezek 7:4,9; 8:18; 9:5,10). The structural opposite named here is not the absence of compassion but its active overriding by judicial will. The vocabulary reveals that compassion is the default inner orientation — the impulse of pity naturally arises — and its structural opposite is the deliberate suppression of that impulse in the service of righteous judgment (Pass 1, term 4; SD-004). This implies a specific inner act: choosing not to spare, against the natural movement toward sparing.
> 
> **Self-deception and self-sufficiency — compassion-blindness:** Rev 3:17 (eleeinos) describes the Laodiceans as pitiable without being able to perceive their own condition. The data identifies this as a failure of the recognition of need — the second condition compassion requires (Pass 1, term 19). The structural opposite at this level is not cruelty but self-enclosed prosperity: the inner state of believing oneself to need nothing, which closes off both the capacity to recognise one's own need and the capacity to perceive the need of others (SD-015).
> 
> These are two distinct structural opposites: the first is willed hardness (judicial non-pity); the second is unwilled blindness (self-deceived non-perception of need). They attack compassion from different angles.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=649 · finding_id='OBS-023-T2-017' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals several things that compassion explicitly excludes or resists:
> 
> **Distance and non-involvement.** The SYM-PATH vocabulary (sumpatheō, sumpaschō) explicitly names compassion as entry into another's experience — the opposite of responding from a safe distance. Compassion as defined by this vocabulary is incompatible with detached sympathy. Heb 4:15 makes this Christologically explicit: Jesus sympathises because he has been tempted as we are — shared experience, not management from above.
> 
> **Ritual boundary maintenance over human need.** Mark 1:41 — splanchnizō produces physical touch across the ritual-purity boundary (SD-020). Compassion resists the inner orientation toward self-protection and social boundary maintenance when those boundaries conflict with the movement toward the one who suffers.
> 
> **Merit-based restriction.** The chesed vocabulary (steadfast love/compassion) is defined by its unconditional character — it is the loyal love that holds even when the covenantal partner has violated the covenant. Jon 4:11 — God's pity for Nineveh — explicitly names a case where compassion extends beyond the expected boundary (a pagan city, uninformed about moral order). Compassion resists the inner logic that only the deserving receive it.
> 
> **Stoic distance.** The metriopatheō (G3356) term is notable here: it draws on the Stoic philosophical tradition of moderating the passions, but Heb 5:2 reframes it away from philosophical self-mastery and grounds it instead in shared vulnerability (SD-013). The data implies a resistance to compassion defined as controlled, disengaged moderation — the scriptural reframing insists on grounding even measured compassion in genuine participation.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=650 · finding_id='OBS-023-T2-018' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides boundary observations but the formal distinction work between compassion and its nearest adjacent characteristics is explicitly deferred to Session D across multiple SD pointers.
> 
> **What the data establishes:**
> 
> Compassion is not mercy (eleos/eleeō), though they are closely related. SD-009 raises the question directly: Rom 9:15 pairs oikteirō (compassion) and eleeō (mercy) as parallel verbs — are they distinguishable or purely rhetorical parallelism? The question is deferred; the boundary is not resolved in the current data.
> 
> Compassion is not grace (chen/channum), though they share the same root (CHIN/CHEN). SD-006 raises: is graciousness (channum, the character quality) distinct from grace (chen, the relational gift)? The inner-being boundary between them is unresolved.
> 
> Compassion is not steadfast love (chesed/agapē), though the chesed vocabulary is extensively present in the OWNER terms. The chesed in Reg 23 carries the negative-pole (shame) and the covenantal-character senses; the primary chesed content belongs to R103 (love) and R104 (kindness/loyalty).
> 
> Compassion is not pity in the modern sense — the vocabulary resists sentimentality. The chus (pity) term appears predominantly in judicial contexts where it is withheld; the ra.cham vocabulary grounds it in bodily-constitutional movement, not in sentiment.
> 
> **What is missing (P):** The precise inner-being boundary between compassion and mercy, and between compassion and grace, is not established in the current data. These are the most critical boundary questions and both are explicitly Session D targets (SD-006, SD-009). No new gap is required — the existing pointers capture the need.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=651 · finding_id='OBS-023-T2-019' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals four distinct modes of operation, mapped to the four root families identified in Pass 1:
> 
> **Mode 1 — Visceral stirring (RACHAM/SPLANCHN):** Compassion operates as a somatic event — an involuntary inner movement triggered by the perception of suffering. Splanchnizō and ni.chum both name this mode. It is pre-volitional in character: the movement happens before the person chooses to act. Hos 11:8 captures this vividly: the divine inner life is moved before judgment can proceed.
> 
> **Mode 2 — Constitutive character quality (CHESED/CHANNUM):** Compassion operates as a settled inner disposition that defines what kind of person one is. Ra.chum (compassionate), sumpathēs (sympathetic), and channum (gracious) all name this mode. The characteristic is not merely something that happens — it is something one is. This mode operates continuously rather than in response to specific triggers.
> 
> **Mode 3 — Participatory solidarity (SYM-PATH):** Compassion operates as genuine entry into another's experience. Sumpatheō and sumpaschō name this mode — not feeling-for but feeling-with, suffering-with. This mode involves a constitutional movement toward the other's inner space, not merely an emotional response to their condition from one's own.
> 
> **Mode 4 — Responsive pity and mercy (ELEEIN/CHUS):** Compassion operates as a relational response to perceived need — the inner impulse to spare, to help, to give. This mode is the most explicitly action-generating: eleēmosunē (almsgiving) is its normalised social form. Chus names the pity that naturally arises toward the needy; eleeinos names the pitiable condition that calls it forth.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=652 · finding_id='OBS-023-T2-020' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data reveals significant variation across all three axes:
> 
> **Context:** Compassion operates differently in contexts of physical suffering (healing miracles, splanchnizō toward the sick and blind), spiritual destitution (splanchnizō toward "sheep without a shepherd"), physical hunger (feeding crowds), relational/moral crisis (prodigal son, unforgiving servant), and eschatological suffering (sumpaschō within the context of glorification). The four semantic domains of splanchnizō mapped in Pass 1 confirm this contextual differentiation.
> 
> **Direction:** Compassion operates distinctly in the God-to-human direction (constitutive divine character, sovereign freedom, covenant faithfulness — ra.cham, chesed, oikteirō), in the human-to-human direction (responsive pity, participatory solidarity, almsgiving — chus, eleēmosunē, sumpatheō), and in the human-to-God direction (implicit in the supplication vocabulary: H8467 techinah, H8469 tahanun — the act of pleading for mercy assumes divine compassion as its ground, SD-021). The God-to-human direction is the most richly evidenced; the human-to-human direction produces the most action-language; the human-to-God direction is present but operates differently — as appeal and orientation rather than as extension.
> 
> **Constitutional level:** At the somatic level, compassion operates as visceral stirring (womb, entrails). At the soul level, it operates as settled character quality and affective disposition. At the volitional level, it operates as the impulse to spare, help, or give. The constitutional movement sequence (Mode 1 → Mode 2 → Mode 4 in T1.4 terms) runs from somatic to volitional. This is addressed more fully at T2.10.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=653 · finding_id='OBS-023-T2-021' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides partial evidence.
> 
> **Speech as the expression of compassion:** Zec 1:13 (group 733-001) — "gracious and comforting words" (ni.chum words). Compassionate inner movement produces comforting speech. Luke 7:13 — Jesus, "moved with compassion" (splanchnizō), says to the widow of Nain: "Do not weep." The compassion-movement produces a direct speech-act of comfort.
> 
> **The supplication vocabulary as compassion-seeking speech:** H8467 techinah (supplication) and H8469 tahanun (entreaty) are XREF terms in the compassion vocabulary. They name the speech-acts by which the person appeals to God's compassion — pleading as the verbal form of vulnerability and need (SD-021). This is the communicative mode of compassion's reception: the person who needs compassion verbalises that need in the form of earnest appeal.
> 
> **What is missing (P):** The data does not contain a developed analysis of the speech-based mode of compassion. Whether compassion has a normative verbal form — a word, a tone, a genre of speech — is not examined. The comforting-words evidence is suggestive but not fully developed. This is a gap; no existing SD pointer addresses it specifically.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=654 · finding_id='OBS-023-T2-022' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data is most explicit about the immediate response of the *giver* (the inner movement that precedes compassionate action) rather than the receiver. What follows is drawn from the available evidence:
> 
> **In the giver:** The most immediate inner-being response in the one from whom compassion flows is the gut-stirring of splanchnizō — an involuntary somatic event prior to volitional engagement. This is the pre-reflective, body-prior movement that the vocabulary captures. In Hos 11:8, the ni.chum (compassionate warmth) is named at the moment it contends with judgment — it is the first inner movement before deliberation resolves.
> 
> **In the receiver:** The data is largely silent on this point directly. Gen 19:16 (chem.lah — God's mercy toward Lot) shows the receiver of compassion being physically acted upon — taken by the hand and led out of danger. The compassion-act produces a rescue; the internal response of the recipient is not named. Luke 7:13-15 — Jesus, moved with compassion toward the widow, raises her son. The widow's immediate inner response is not stated.
> 
> **Partial evidence from the pitiable condition:** The eleeinos (pitiful) evidence implies that the person who cannot recognise their own pitiable condition cannot receive compassion. The first response to receiving compassion may therefore require a prior inner movement: the recognition of need.
> 
> **What is missing (P):** The data does not contain an explicit account of the receiver's immediate inner-being response to receiving compassion. This is a genuine gap; no SD pointer covers it directly. It is a new gap for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=655 · finding_id='OBS-023-T2-023' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The immediate response in the *giver* is consistent: across the splanchnizō uses in the Gospels, the pattern is uniform — the compassion-movement precedes the action. The somatic stirring is the invariant first event. This consistency is confirmed across diverse contexts: healing, feeding, teaching, consoling. The movement is the same; only its occasion differs.
> 
> **Variation in the receiver's response:** The data does not provide enough evidence on the receiver's side to assess consistency. This follows from the gap identified at Prompt 1 above.
> 
> **What is missing (P):** Consistency of the receiver's immediate response remains unaddressed in the data.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=656 · finding_id='OBS-023-T2-024' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The verse evidence is silent on the immediate inner-being response of the *receiver* of compassion. This silence is noted and flagged as a new gap for Session D. The evidence addresses the immediate response of the giver comprehensively but does not track what happens first in the inner being of the one who receives.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=657 · finding_id='OBS-023-T2-025' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data addresses sustained effect more through the chesed/channum vocabulary than through the splanchnizō/ra.cham vocabulary.
> 
> **Chesed as sustained constitutional state:** The chesed vocabulary (H2617B, H2617A as XREF) names God's compassion-love as *everlasting* (Lam 3:22 — "his mercies never come to an end"; Isa 54:8 — "everlasting chesed"). In the human person, cha.sad (2 Sam 22:26) names the settled character quality of covenantal mercy-faithfulness that defines the person's inner orientation. Over time, chesed produces the character type of the chasid (devoted/loyal person, H2623 XREF) — the one whose inner life is constitutively shaped by covenantal loyalty.
> 
> **Sumpatheō and community formation:** The 1 Pet 3:8 community portrait (unity of mind, sympathy, brotherly love, tender heart, humble mind) suggests that sustained operation of the sumpathēs quality produces an inner fabric of community solidarity — a person shaped for genuine relational presence.
> 
> **What is missing (P):** The data does not directly address what sustained *reception* of divine compassion produces in the inner being over time. What does a person become, constitutionally, as the sustained object of divine ra.cham and chesed? This is implied by the supplication vocabulary and the covenantal frame but not stated. This is a gap; no SD pointer addresses it directly.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=658 · finding_id='OBS-023-T2-026' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> From the data:
> 
> **Sustained possession** of compassion appears to produce: a character orientation toward the suffering other (the chasid type — devoted, loyal, responsive); a constitutive outward-facing inner disposition (ra.chum as adjective, sumpathēs as adjective); and an integration of inner movement with outer act (eleēmosunē as the normalised social form of sustained compassion).
> 
> **Sustained exposure** (being the recipient of divine compassion) appears to produce, by implication: the capacity for supplication (the XREF supplication vocabulary assumes a recipient who has learned to return to the compassionate God); a trust orientation (Psa 25:7 — "according to your steadfast love remember me"; Psa 48:9 — "we have thought on your steadfast love"); and a corresponding compassionate character (the mirroring principle of 2 Sam 22:26).
> 
> **What is missing (P):** The data does not trace this developmental arc explicitly. These observations are assembled from adjacent data rather than from direct statements. The sustained-effect question is genuinely underdeveloped in the current data for this registry.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=659 · finding_id='OBS-023-T2-027' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data implies a difference but does not state it explicitly.
> 
> The immediate response in the giver is a somatic event (splanchnizō — a movement). The sustained effect in the giver appears to be a character quality (ra.chum, sumpathēs — a settled disposition). The difference between these is the difference between an inner-being event and an inner-being state. The vocabulary differentiates them (verb vs adjective), but the data does not trace how the event produces the state over time — what the formation process looks like.
> 
> This is a gap. The formation question (how does repeated compassion-movement produce the compassionate character?) is not addressed in the current data and is not captured by any existing SD pointer. It is a new gap for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=660 · finding_id='OBS-023-T2-028' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides partial evidence, primarily from the negative side (what blocks reception) rather than positive conditions.
> 
> **Need-recognition as enabling condition:** Rev 3:17 (eleeinos) and its SD-015 pointer establish that receiving compassion requires the ability to recognise one's own pitiable condition. The Laodiceans cannot receive the compassion they need because they cannot perceive their own need. The enabling condition implied is: awareness of need — the inner openness that comes from recognising one's own insufficiency.
> 
> **Vulnerability and humility:** The supplication vocabulary (techinah, tahanun) implies that earnest appeal — the verbal expression of need and vulnerability before God — is an enabling posture for the reception of divine compassion. The one who cries out is positioned to receive.
> 
> **What is missing (P):** The data does not provide a direct positive account of what inner conditions enable reception of compassion from another human person. The God-to-human reception conditions are partially addressed; the human-to-human reception conditions are not addressed at all. This is a partial gap.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=661 · finding_id='OBS-023-T2-029' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data is relatively explicit here, yielding two distinct blocking conditions:
> 
> **Self-sufficiency and prosperity-blindness (Rev 3:17, SD-015):** The Laodicean condition — "I am rich, I have prospered, I need nothing" — is named as the precise inner state that prevents recognition of the pitiable condition. Self-enclosed prosperity is identified as an inner orientation that renders the person incapable of perceiving their own need. If need-recognition is the condition for receiving compassion, then its absence (self-sufficiency) is the primary blocking condition.
> 
> **Judicial hardness — the deliberately closed eye (H2347 chus):** The prohibition contexts ("your eye shall not pity") reveal that the impulse toward compassion can be deliberately overridden. While these are primarily divine-judicial or legal contexts, they reveal a structural reality: the inner movement toward compassion can be closed by an act of will oriented toward judgment rather than mercy. Applied to the receiving side, a person oriented primarily toward justice and merit — expecting to receive what one deserves — may block the reception of compassion by treating it as inappropriate or unearned.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=662 · finding_id='OBS-023-T2-030' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data addresses one specific case directly and implies others:
> 
> **The explicitly pitiable but self-unaware (Rev 3:17):** The person who encounters compassion but cannot receive it — because they cannot perceive their own pitiable condition — remains in a state of spiritual destitution without being aware of it. The inner state is one of self-deceptive sufficiency masking actual need. The irony named in the data is pointed: those who most need compassion may be those least able to receive it.
> 
> **The one in extreme duress (Lam 4:10 context):** The compassionate women who violate their own compassion under siege conditions represent a different case — a person whose compassion-capacity has been overwhelmed by external catastrophe. The inner state is one of constitutional rupture: the characteristic that defines the person has been forced into violation. This is not a failure of reception but a failure of the character under unbearable pressure.
> 
> **What is missing (P):** The data does not directly address the inner-being state of a person who encounters human compassion but refuses or cannot receive it for reasons other than self-deception (e.g., shame, distrust, grief, pride). This is a gap not covered by existing SD pointers.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=663 · finding_id='OBS-023-T2-031' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T1.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The registry header shows `dimensions: None` — the dimension field has not been populated in the database record. However, the Dimension Review (`dim_review_status: Complete`, under `WA-DimensionReview-Instruction-v1.9-2026-04-09`) has been completed. The programme's dimension vocabulary (v1.4) includes: Emotion — Positive, Emotion — Negative, Cognition, Volition, Moral Character, Relational Disposition, Vitality / Existence, Transformation, Agency / Power, Dependence / Creatureliness.
> 
> From the data, the primary dimension is: **Relational Disposition**. Compassion is constitutively relational — it cannot exist without an other; it defines the person's inner orientation toward the suffering other; it produces relational solidarity and action. The registry description confirms: "Compassion always faces outward toward the one suffering." The outward relational orientation is the defining characteristic.
> 
> **Secondary dimension:** **Emotion — Positive** is a strong secondary candidate. The visceral inner stirring of splanchnizō and ra.cham is experiential and felt — an affective event that precedes and motivates action. The SYM-PATH vocabulary also carries strong affective content.
> 
> The sb_classification (**Soul-body interface**) is consistent with Relational Disposition as primary — compassion is the inner disposition that crosses the boundary between self and other at the soul-body level.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=664 · finding_id='OBS-023-T2-032' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T1.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **For Relational Disposition:**
> - The splanchnizō pattern in the Gospels is invariably triggered by the other's condition — not by internal spiritual state
> - The CHESED vocabulary names covenantal loyalty toward the other as the constitutive character quality
> - The sumpatheō/sumpaschō vocabulary defines compassion as participation in the other's experience — paradigmatically relational
> - Luke 10:33 (Good Samaritan) — compassion answers the question "who is my neighbour?" — making it the defining quality of relational extension
> 
> **For Emotion — Positive as secondary:**
> - Splanchnizō is somatic-affective — a felt inner stirring
> - Ni.chum (Hos 11:8) — "my compassion grows warm and tender" — uses temperature language for emotional quality
> - The maternal imagery (womb, carrying) carries strong affective resonance
> - 1 Cor 12:26 (sumpaschō) — the body suffering together — is both relational and deeply felt
> 
> The two dimensions are not in competition; they describe different aspects of the same phenomenon. Relational Disposition names what compassion is *about*; Emotion — Positive names what compassion *feels like* from the inside.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=665 · finding_id='OBS-023-T2-033' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T1.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three secondary dimensions are evidenced:
> 
> **1. Emotion — Positive** (as above): strongly evidenced, does not compete with Relational Disposition — it names the inner texture of the relational movement.
> 
> **2. Agency / Power:** The compassion vocabulary consistently generates action. Splanchnizō produces healing, feeding, teaching, raising the dead. Eleēmosunē is the normalised outer act. The chus/chem.lah vocabulary is explicitly about sparing — an act of will. Compassion is not merely felt; it acts. This is a secondary Agency dimension.
> 
> **3. Vitality / Existence:** The womb vocabulary (re.chem, H7358) grounds compassion in the very space of life-origination. The womb is the threshold of human existence (group 1613-001 — "the space where divine compassion, calling, and consecration originate before birth"). Compassion in this register is connected to the giving and sustaining of life itself — a Vitality dimension that is not immediately obvious from the word but is intrinsic to the RACHAM root.
> 
> None of these secondary dimensions compete with the primary Relational Disposition classification. They describe the depth, energy, and existential ground of the relational orientation rather than redirecting the analysis.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=666 · finding_id='OBS-023-T2-034' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the evidence consistently locates compassion at the soul level, primarily through the chesed and channum vocabulary and the character-quality (adjectival) terms.
> 
> H7349 ra.chum (compassionate) is an adjectival form naming the settled soul-level disposition — what kind of person one is constitutively. H2587 channum (gracious) is similarly a soul-level character descriptor, used almost exclusively as a divine attribute in the epithet formula. G4835 sumpathēs (sympathetic, 1 Pet 3:8) is placed in a list of soul-level character qualities alongside unity of mind, brotherly love, tender heart, and humble mind — all soul-level orientations.
> 
> The chesed vocabulary (H2617B, H2617A as XREF) names compassion-love as a settled inner disposition of covenantal loyalty — a soul-level character reality, not a momentary event. The group descriptions for 1633-001 (God's steadfast love), 1633-002 (human disposition of covenantal loyalty), and 1633-003 (trust and hope grounded in chesed) all operate at the soul level.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=667 · finding_id='OBS-023-T2-035' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Soul-level location reveals that compassion is not merely an emotional response to circumstances — it is a constitutive inner orientation that defines the person's relationship to others at the deepest personal level. Three implications emerge from the data:
> 
> **Compassion as the soul's outward face.** The soul-level character qualities associated with compassion (ra.chum, sumpathēs, channum) are all constitutively other-oriented. This distinguishes compassion from inner-being characteristics that orient the person primarily toward God (worship, fear, trust) or primarily toward the self (integrity, purity). Compassion is the soul's fundamental orientation toward the suffering other — its outward relational face.
> 
> **Compassion as identity-constituting quality.** The adjectival forms (ra.chum, ra.cha.ma.ni, sumpathēs) name what kind of person one is, not merely what one does. Lam 4:10 — "compassionate women" who violate their compassion — shows that this soul-level quality is understood as identity-constituting: the tragedy is precisely that persons whose identity is defined by compassion were forced to act against it.
> 
> **Chesed as the deepest covenantal form of compassion.** The chesed vocabulary at the soul level names compassion in its most constitutive and enduring form — the loyal love that holds through covenant violation, exile, and judgment. This is compassion at the level of settled inner character, not responsive feeling. Its soul-level location is confirmed by its persistence: "his mercies never come to an end" (Lam 3:22).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=668 · finding_id='OBS-023-T2-036' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the most theologically and emotionally dense verse in the data explicitly locates compassion in the heart. Hos 11:8: "My heart recoils within me; my compassion grows warm and tender." The Hebrew lev (heart) is the anatomical and constitutional reference. The heart recoiling is the precursor to the ni.chum (compassionate warmth) that follows — the heart's movement is what produces the compassion-stirring.
> 
> Joel 2:13 deploys the heart in a connected context: "rend your hearts and not your garments. Return to the LORD your God, for he is gracious and merciful (rachum ve-channum)." The divine compassion-character is the ground for a call to heart-rending (SD-029). Compassion here is both a divine heart-quality and the basis for a demand upon the human heart.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=669 · finding_id='OBS-023-T2-037' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Hos 11:8 engages all four aspects of the heart's integrating function simultaneously, which is what makes it the most complex single verse in the compassion data:
> 
> **Knowing:** The heart "recoils" — this is a form of inner-being recognition. God knows what Ephraim is and what will happen to him; the heart's recoiling is the response to that knowledge. Compassion at the heart level involves knowing the condition of the other and being moved by what one knows.
> 
> **Willing:** The verse narrates a divine inner deliberation: the heart's recoiling precedes and overrides the judgment that would have been executed. Compassion engages the heart's willing function — it contends with competing volitional orientations (judgment, withdrawal) and wins. The ni.chum is not the suppression of judgment but the outcome of an inner-heart contest (Pass 2 FRAMEWORK SIGNAL on ni.chum).
> 
> **Feeling:** The warmth of ni.chum — "my compassion grows warm and tender" — is the felt quality of the heart's compassion. Temperature language (warm) names the affective quality at the heart level.
> 
> **Moral awareness:** The deliberation in Hos 11:8 turns on a moral question — whether to execute judgment or withhold it. Compassion at the heart level is morally engaged: it is not pre-moral sentimentality but the moral determination that mercy is more constitutive of who God is than judgment.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=670 · finding_id='OBS-023-T2-038' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The evidence partially addresses the mind in the context of compassion, primarily through the 1 Pet 3:8 community list and the metriopatheō term.
> 
> 1 Pet 3:8 places sumpathēs (sympathetic/compassionate) alongside "unity of mind" (homophrōn) — the same verse positions compassion and cognitive unity as companion virtues. The mind (phronēma) is implicated but not as the seat of compassion itself — rather as a co-operating faculty.
> 
> G3356 metriopatheō (Heb 5:2) — "deal gently" — draws on the Stoic metriopatheia tradition of moderating the passions through reasoned self-governance. The term places a form of calibrated compassion in proximity to the mind's regulating function: compassion that is wise rather than raw. However, Heb 5:2 regrounds this in shared vulnerability rather than cognitive mastery — the moderation comes from knowing human weakness from the inside, not from philosophical reasoning (SD-013).
> 
> **What is missing (P):** The data does not locate compassion directly in the mind using nous or equivalent terms. Mind-engagement is evidenced as secondary and co-operative rather than primary.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=671 · finding_id='OBS-023-T2-039' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> From the metriopatheō evidence: compassion engages the mind's function of discernment — knowing how to respond appropriately to the one who is weak or wayward, calibrating the expression of compassion to the situation. This is compassion shaped by understanding of the other's condition rather than by raw visceral response alone.
> 
> From the Hos 11:8 evidence: the divine inner deliberation involves something mind-like — the inner contest between judgment and compassion is not purely affective but involves a form of reasoning through competing claims. Whether this belongs strictly to the "mind" in the programme's framework or to the heart's integrating function is not resolved in the data.
> 
> **What is missing (P):** The mind's role in compassion — whether discernment, understanding of need, or moral reasoning — is not developed in the data beyond these partial signals. This is a gap; no SD pointer addresses it specifically.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=672 · finding_id='OBS-023-T2-040' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the will and the conscience are both implicated by the data, though not named in those terms explicitly.
> 
> **Will as soul subset:** The chus (pity) vocabulary — "your eye shall not pity" (Deut 19:13; Ezek 7:4) — locates the compassion-impulse in a place that the will can engage or override. The phrase "your eye shall not pity" addresses an inner faculty that sees and responds — a seeing-faculty that generates a compassion-impulse which can then be volitionally suppressed. This implies a soul-level layer at which compassion arises prior to volitional engagement. The will is then the faculty that either acts on or suppresses this arising impulse.
> 
> **Tender heart as a named soul subset:** 1 Pet 3:8 names "a tender heart" (eusplanchnos — literally: of good entrails/affections) as a distinct soul-level quality alongside sympathy. This is a named inner-being orientation that the verse treats as a separate faculty or quality from sympathy itself — the predisposing inner tenderness from which sumpathēs flows.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=673 · finding_id='OBS-023-T2-041' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The tender heart (eusplanchnos) reveals that compassion is not only a disposition that engages with the other when they appear — it is grounded in a prior inner softness or receptivity. The person who has a tender heart (eusplanchnos) is constitutionally open to being moved. This is the pre-dispositional condition for compassion-movement: a heart that has not been hardened, calloused, or closed against the suffering of others.
> 
> This is analytically significant: it implies a gradient of inner receptivity to compassion. The fully compassionate person is eusplanchnos AND sumpathēs — internally tender AND actively sympathetic. The hardened person (implied by the judicial-eye-that-will-not-pity) lacks the eusplanchnos quality at the soul-subset level. This inner tenderness is a constitutional precondition, not merely an incidental quality.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=674 · finding_id='OBS-023-T2-042' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — and this is among the strongest and most explicit body-part links in the programme. Two primary anatomical anchors:
> 
> **The womb (re.chem / ra.cham):** H7358 re.chem and H7356A ra.cham link compassion directly and etymologically to the womb. The word for compassion (ra.cham) is the same root as the word for womb (re.chem). This is not a metaphorical extension — the lexical relationship is built into the language. Isa 46:3 ("carried from the womb") and Psa 22:10 ("from my mother's womb you have been my God") use the womb as the originating space of divine care and compassion.
> 
> **The entrails / gut (splanchnon / splanchnizō):** G4697 splanchnizō names the gut-movement of compassion. Its root is G4698 splanchnon (entrails, affections). The abdominal organs were understood in the ancient world as the seat of the deepest emotions. Jesus's compassion movements in the Synoptics are all named through this gut-vocabulary. Jas 5:11 (polusplanchnos — "of great gut-compassion") intensifies the somatic grounding.
> 
> **The heart (lev):** Hos 11:8 — "my heart recoils within me." The heart is a secondary body-part link, functioning here as the organ of inner deliberation and feeling rather than as the primary etymological ground.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=675 · finding_id='OBS-023-T2-043' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Scripture is doing several distinct things simultaneously through these body-part links:
> 
> **Etymological / constitutive (womb):** The womb-link is not a rhetorical device added to an abstract concept — it is the etymological ground of the abstract concept. Scripture did not choose to illustrate compassion with a womb metaphor; the language itself was built from the womb upward. The body-part link in the RACHAM vocabulary is constitutive of the meaning, not expressive of it. This makes the womb-link unique in its depth: it does not merely describe what compassion feels like — it is what compassion is named after.
> 
> **Expressive (splanchnizō):** The gut-movement vocabulary names what compassion feels like from the inside — where in the body one experiences being moved by another's suffering. This is expressive: it communicates the somatic texture of the inner experience.
> 
> **Indicative (splanchnizō in the Gospels):** Jesus's splanchnizō-movements are consistently visible to the observers — they precede his actions and are reported as inner events that explain the external actions. The body-movement is indicative of the inner state: it shows the observers (and the reader) what is happening inside before the action takes place.
> 
> **Mediating (heart in Hos 11:8):** The heart's recoiling mediates between the divine knowledge of Israel's condition and the compassion-response. The heart is the organ of inner deliberation at which compassion overcomes judgment.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=676 · finding_id='OBS-023-T2-044' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals that the body-characteristic link for compassion runs in both directions, and that the directionality differs by body part and vocabulary:
> 
> **From soul to body (expressive direction):** In the splanchnizō Gospels pattern, the inner compassion-disposition (soul level) expresses itself through the gut-stirring (body level) and then through action. The movement is: inner character → somatic event → outward act. The body is the vehicle through which the soul's compassion arrives at expression and action.
> 
> **From body to soul (constitutive direction):** In the RACHAM etymology, the direction is reversed. The body's most intimate space (womb) is the ground from which the abstract compassion concept was named. The physical reality precedes and constitutes the inner-being concept. This is the unusual etymological direction noted at T0.3 Prompt 1 — the womb feeds the meaning upward into the soul-level concept.
> 
> **Mutual / participatory direction (sumpatheō):** The classical philosophical usage of sumpatheō (soul and body sympathising with each other — Aristotle, as noted in the Pass 1 term 14 analysis) introduces a bidirectional model: the soul and body suffer-together, each affecting the other. The NT reappropriation of this term for Christian community and Christology (SD-011) carries this bidirectionality into the new context: genuine fellow-feeling involves both soul and body moving in concert.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=677 · finding_id='OBS-023-T2-045' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The bidirectionality has a significant consequence: compassion is not adequately described either as a purely interior soul-quality that incidentally uses the body as its vehicle, nor as a purely somatic reflex. It is a genuinely soul-body integrated phenomenon in which the body is both the originating ground (RACHAM etymology) and the expressive medium (splanchnizō movement) and the participatory instrument (sumpatheō — suffering with).
> 
> This means that the programme's sb_classification of **Soul-body interface** is precisely right for compassion — not merely as a category assignment but as a description of the characteristic's constitutional operation. Compassion lives at the interface in both directions simultaneously. The person who is compassionate is someone whose soul and body are integrated in their response to the suffering other: they feel it in their gut, they are moved from the inside, and that inner-bodily movement produces action.
> 
> An important implication: compassion cannot be fully present as a purely cognitive determination (a decision to act compassionately without the somatic component). The vocabulary insists on the body's participation. A compassion that bypasses the gut is, in the terms of this vocabulary, not the full phenomenon.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=678 · finding_id='OBS-023-T2-046' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data does not contain direct evidence of a constitutional body deposit from sustained compassion in the individual. However, two lines of evidence approach this question without closing it:
> 
> **The womb as generational threshold:** H7358 re.chem and H7356A ra.cham ground compassion in the womb — the very space of biological transmission. Groups 1613-001 and 1613-002 name the womb as "the threshold of human existence over which God exercises sovereign care" and "the origin of human existence." If compassion is etymologically grounded in the womb, and the womb is the space through which life and formation are transmitted generationally, this creates an implicit but unconfirmed connection between compassion as a constitutive quality and its potential generational transmission through the womb-space.
> 
> **The Exod 34:6 formula and generational consequence:** The divine compassion-character formula (rachum ve-channum) is embedded in a passage (Exod 34:6-7) that explicitly names generational consequence — "visiting the iniquity of the fathers on the children and the children's children, to the third and the fourth generation." The positive complement (compassion, steadfast love) is named in the same breath. The structural implication is that God's compassionate character is generationally operative, though the text names the generational dimension for iniquity more explicitly than for compassion.
> 
> **What is missing (P):** The data does not provide direct evidence of a body deposit from sustained human compassion, nor any verse that names a generational compassion-transmission in human biological terms. The womb-link is suggestive but not probative. This finding feeds directly into T5.7.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=679 · finding_id='OBS-023-T2-047' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Supporting (indirect):** The womb etymology creates a structural resonance between compassion and biological transmission. The eusplanchnos (tender heart) quality in 1 Pet 3:8 names a pre-dispositional inner softness — a constitutional quality that may be formed over time rather than simply present or absent. If tenderness of inner being can be formed and sustained, it is plausible (though not stated) that it could be constitutionally embedded.
> 
> The mirroring principle (2 Sam 22:26 — "with the merciful you show yourself merciful") operates reciprocally: God's compassion is responsive to human compassionate character. If sustained divine compassion shapes the human person's inner being constitutively over time, a long-term constitutional effect is implied — though not named as a body deposit.
> 
> **Contradicting / limiting:** No verse explicitly names a body-level deposit from sustained compassion in the human person. The Lam 4:10 evidence (compassionate women under siege violating their compassion) implies that even deeply formed compassionate character can be overwhelmed by extreme circumstance — which may suggest that the constitutional formation has limits under pressure, rather than that it produces an indestructible deposit.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=680 · finding_id='OBS-023-T2-048' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T2.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The evidence is not fully silent — the womb etymology and the Exod 34:6 generational frame create partial signals — but direct evidence of a constitutional body deposit is absent. T5.7 will be handled as a partial/conditional finding: the womb-related generational dimension will be noted, but no deposit will be affirmed as established from the data. The question is a genuine gap for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=681 · finding_id='OBS-023-T2-049' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.9'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals multiple distinct origin points operating simultaneously, differentiated by vocabulary and direction:
> 
> **Bestowed by God — divine constitutive origin:** The dominant direction in the OT vocabulary is that compassion originates in God's character (rachum ve-channum as divine epithet, Exod 34:6) and flows from God toward the human person and toward Israel as a covenant community. God's compassion is the primary source from which all other compassion derives. This is not merely a theological assertion — it is embedded in the vocabulary structure: the most theologically charged terms (ra.cham, chesed, oikteirō) are predominantly divine-subject terms.
> 
> **Generated from within — somatic origin:** The splanchnizō vocabulary names compassion as arising from within the person's own body (gut-stirring). In this register, compassion is not received from outside but generated from within — a response arising from one's own inner being when confronted with the suffering other. Luke 10:33 (Good Samaritan — human subject) and Luke 15:20 (father of prodigal — human subject) both show compassion arising from within the human person without any external divine causation named in the text.
> 
> **Received through encounter — relational origin:** The supplication vocabulary (techinah, tahanun) implies that the human person receives compassion through earnest appeal — compassion is extended from God in response to the person's cry. In this mode, compassion is received rather than generated.
> 
> **Carried generationally — womb origin (partial):** As noted at T2.8, the womb etymology creates a suggestive but unconfirmed connection to generational transmission.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=682 · finding_id='OBS-023-T2-050' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.9'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The origin is clearly multiple. The vocabulary differentiates at least three distinct origin-modes (divine bestowal, inner generation, relational reception), and these are not synonyms or alternative descriptions of the same event — they are genuinely distinct constitutional movements.
> 
> The most significant observation: the same characteristic (compassion) can originate from within the person (splanchnizō — gut-stirring in the Good Samaritan) and from God's sovereign freedom (oikteirō — Rom 9:15: "I will have compassion on whom I have compassion"). These two origin-points are not in tension in the data — they are describing different registers of the same fundamental characteristic. The implication for the programme is that compassion has a multi-origin constitutional structure: it is simultaneously a divine gift, a creaturely capacity, and an inner-body event.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=683 · finding_id='OBS-023-T2-051' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T2.9'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the contextual variation in origin is one of the structurally significant features of the compassion vocabulary:
> 
> **In prophetic/covenantal contexts:** Origin is predominantly divine — God's inner movement (Hos 11:8), God's sovereign freedom (Rom 9:15), God's everlasting chesed (Isa 54:8). The human person's compassion is derivative and responsive.
> 
> **In Synoptic Gospel contexts:** Origin is primarily Christological — Jesus's gut-movement (splanchnizō) as the incarnate embodiment of divine compassion enacted in human form. This is neither purely divine-origin nor purely human-origin — it is the point where the two meet in the Incarnation.
> 
> **In Epistle and community contexts:** Origin is located in the character formed within the community of faith — sumpathēs and eusplanchnos (1 Pet 3:8) as qualities cultivated within the new humanity. In this context, compassion originates from within the person's formed character, shaped by community and by the gospel.
> 
> **In parable contexts:** Origin is presented as arising naturally within the human person in response to need — the father running to the prodigal (Luke 15:20), the Samaritan stopping for the wounded man (Luke 10:33). In these contexts, no divine causation is explicitly named — compassion arises as the human inner response to human need.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=684 · finding_id='OBS-023-T2-052' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T2.10'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data reveals a clear constitutional movement pattern, running from the body's interior upward through the soul, and then outward through action. This is the most structurally significant finding of T2.
> 
> The movement sequence, assembled from the vocabulary:
> 
> **Stage 1 — Somatic arousal (body level):** The gut stirs (splanchnizō), the compassion grows warm (ni.chum — Hos 11:8), the heart recoils (lev — Hos 11:8). These are body-level and heart-level events — involuntary, pre-volitional, arising from the deepest constitutional interior.
> 
> **Stage 2 — Soul engagement:** The somatic arousal engages the soul-level disposition — either activating the already-present ra.chum / chesed / sumpathēs quality (if it is formed) or producing a one-time response of mercy. The chesed vocabulary names this soul-level engagement as the constitutive quality that gives the somatic arousal its character direction.
> 
> **Stage 3 — Volitional engagement:** The compassion-movement reaches the will. In the judicial-prohibition contexts (chus — "your eye shall not pity"), this is the point at which compassion can be overridden. In the Synoptic Gospel pattern, it is the point at which action is determined: "stretched out his hand and touched him" (Mark 1:41).
> 
> **Stage 4 — Outward action:** Eleēmosunē (almsgiving), physical touch (Mark 1:41), raising the dead (Luke 7:15), feeding the crowd (Matt 15:32). Compassion arrives at its constitutional destination in outward action. SD-016 names this as the three-stage model: visceral stirring → mercy orientation → concrete act.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=685 · finding_id='OBS-023-T2-053' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T2.10'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The sequence is consistently bottom-up and inside-out in the data:
> 
> - It begins in the deepest body interior (womb/gut/heart)
> - It moves through the soul-level disposition
> - It engages the will
> - It arrives at the other through action
> 
> This is not a top-down cognitive process (deciding to be compassionate, then feeling it, then acting). The vocabulary insists on the pre-volitional somatic origin: compassion arises before it is chosen. The volitional engagement is real — the will can suppress or direct it — but it does not initiate it.
> 
> The Hos 11:8 pattern makes this sequence explicit in divine terms: the heart recoils (somatic) → the compassion grows warm (affective/soul) → the judgment is overridden (volitional) → the promised restoration follows (action-oriented). The four stages of T2.10 Prompt 1 are all visible in a single verse.
> 
> The one significant complication: the chesed/channum vocabulary (soul-level constitutive disposition) may precede the somatic event in terms of formation — the person who is ra.chum (constitutively compassionate) has a formed soul-level quality that enables the somatic response to arise more readily. This suggests a circular or reciprocal pattern over time: somatic events form the soul-level disposition; the soul-level disposition enables and channels future somatic events.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=686 · finding_id='OBS-023-T2-054' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — sight is the primary perceptive faculty engaged, and it is engaged consistently and structurally across the vocabulary.
> 
> **Sight as the trigger of compassion:** In every splanchnizō occurrence in the Gospels, the compassion-movement is triggered by seeing. Matt 9:36: "When he saw the crowds, he had compassion for them." Luke 7:13: "When the Lord saw her, he had compassion on her." Mark 1:41: the leper comes to Jesus; Jesus sees and is moved. Luke 15:20: "But while he was still a long way off, his father saw him and felt compassion." The pattern is structurally invariant: sight precedes and triggers the gut-stirring. Compassion is a response to perceived suffering — it cannot operate without the perception of need.
> 
> **The chus vocabulary and the eye:** H2347 chus (pity) appears repeatedly in the phrase "your eye shall not pity" (Deut 7:16; 13:8; 19:13; Ezek 7:4; 9:5). The eye is named as the organ through which the pity-impulse arises. The judicial prohibition addresses the eye directly — because the eye's perception of the other's condition naturally generates the pity-response. The eye is the perceptive organ that activates the compassion-faculty. Suppressing compassion requires overriding what the eye generates.
> 
> **Spiritual discernment (eleeinos — Rev 3:17):** The Laodiceans' failure to perceive their own pitiable condition (eleeinos) is a failure of spiritual discernment — an inner-sense blindness that prevents both self-recognition and the capacity to receive compassion. Compassion requires not only external sight but the inner-sense capacity to recognise need, including one's own.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=687 · finding_id='OBS-023-T2-055' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Compassion both depends on and deepens perception in the verse evidence.
> 
> **Compassion depends on perception:** As established at Prompt 1, compassion cannot arise without the sight (or its inner equivalent) of the other's condition. It does not bypass the perceptive faculty — it is triggered by it. In this sense, compassion is perceptively dependent: blind to suffering, it cannot move.
> 
> **Compassion deepens perception — the neighbour question:** Luke 10:33-37 connects compassion directly to the capacity to see rightly. The question "who is my neighbour?" is answered by the parable of the Good Samaritan, whose compassion causes him to see the wounded man as someone worthy of full engagement. The priest and Levite also see (and pass by) — their failure is not perceptual absence but perceptual closure: they see without being moved. Compassion in the Samaritan deepens his perception to the point where the wounded stranger becomes a full person, not an obstacle. The priest and Levite's non-compassion leaves their perception impaired in the sense that it does not arrive at the full truth of what they are seeing.
> 
> **Compassion can be blocked by perceptive failure (eleeinos):** Where the person cannot perceive their own pitiable condition (Rev 3:17), compassion cannot reach them. Impaired inner perception blocks the reception of compassion. This is not compassion impairing perception — it is the absence of compassion's perceptive ground blocking its operation.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=688 · finding_id='OBS-023-T2-056' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The consistent sight-trigger pattern reveals that compassion is fundamentally a responsive characteristic — it does not arise in the absence of perceived need. This distinguishes it from characteristics that operate independently of external stimulus (e.g., integrity, which operates whether or not one is observed; faithfulness, which is constitutive regardless of circumstances). Compassion requires the other to be present and perceptible.
> 
> This has a structural implication: compassion's operation is contingent on perception, but its character is not contingent on the perceived person's merit. The splanchnizō movements in the Gospels are not triggered by the moral worthiness of the recipients — they are triggered by the sight of suffering, need, and lostness. Jon 4:11 (God's pity for Nineveh) is triggered by the sight of people "who do not know their right hand from their left" — moral ignorance, not moral achievement. Compassion is perceptively triggered but merit-independent in its response.
> 
> The non-engagement pattern (the priest and Levite in Luke 10, the judicial eye that will not pity) reveals the complementary truth: the suppression of compassion requires a deliberate act of non-seeing — a refusal to let the perception of need produce its natural response. Compassion's connection to sight is so strong that suppressing it requires overriding what the eye generates.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=689 · finding_id='OBS-023-T2-057' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data evidences cognitive engagement at two distinct points in compassion's operation.
> 
> **Cognition as co-operating faculty in the compassion-movement:** Hos 11:8 shows divine inner deliberation — the heart recoils, the compassion warms, but the process involves something recognisably deliberative. God knows what Ephraim has done; God knows what judgment would mean; God deliberates and compassion wins. The cognitive faculty (knowing, discerning) is engaged in the resolution of the inner contest between judgment and compassion.
> 
> **Cognition in the moderation of compassion (metriopatheō):** G3356 metriopatheō (Heb 5:2) — "deal gently with the ignorant and wayward" — names a form of compassion shaped by understanding. The high priest can deal gently because he understands (knows from inside) the condition of weakness. Compassion here requires cognitive engagement with the other's situation: to moderate one's response appropriately requires understanding the condition that needs responding to.
> 
> **Cognition in the recognition of need:** The eleeinos (pitiful) evidence at Rev 3:17 shows that compassion's reception requires a cognitive act — recognising one's own pitiable condition. This is a form of self-knowledge (gnōsis applied inwardly) that enables the reception of compassion. Its absence is described as a failure of knowing: "not realising that you are wretched, pitiable, poor, blind, and naked."

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=690 · finding_id='OBS-023-T2-058' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion deepens cognition in the Good Samaritan pattern:** As noted at T3.1, the Samaritan's compassion deepens his perception and by extension his understanding of the wounded man's full humanity. Compassion-generated sight produces a form of moral knowledge — the knowledge of what the other truly is, beyond category and boundary.
> 
> **Compassion can operate before cognition (pre-cognitive somatic movement):** The splanchnizō gut-stirring is pre-volitional and, by implication, pre-reflective. The somatic arousal precedes deliberation. In this sense, compassion does not bypass cognition but precedes it — the inner body moves before the cognitive faculty has evaluated the situation. Cognition follows the gut-stirring and gives it direction and form.
> 
> **What is missing (P):** The data does not address whether sustained compassion deepens the cognitive faculty over time — whether the compassionate person becomes a more discerning perceiver of need, or whether compassion and cognition are structurally linked in a developmental relationship. This is a gap; no SD pointer addresses it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=691 · finding_id='OBS-023-T2-059' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The pattern reveals that compassion is not a cognitively-initiated characteristic — it does not begin with a reasoned assessment of need that then produces a feeling. It begins in the body and the heart (gut-stirring, heart-recoiling) and then engages the cognitive faculty as a co-operating and moderating agent. This is constitutionally significant: compassion is not a conclusion of moral reasoning but an inner-being event that moral reasoning then shapes, directs, and — in judicial contexts — can override.
> 
> The metriopatheō evidence adds nuance: compassion can be cognitively shaped without being cognitively initiated. Understanding of the other's condition (shared weakness — Heb 5:2) produces a calibrated, appropriate compassion rather than a raw, undirected one. Cognition here is a forming agent, not an originating one. This distinction is analytically important for T5 (formation and development).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=692 · finding_id='OBS-023-T2-060' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data reveals a specific and significant engagement with memory, operating in two directions.
> 
> **Memory as the appeal ground in supplication:** The supplication vocabulary (H8467 techinah, H8469 tahanun, H2603A chanan as XREF) names the inner act of earnest appeal to God for compassion. Psa 25:7 (group 1633-003): "Remember not the sins of my youth or my transgressions; according to your steadfast love remember me, for the sake of your goodness, O Lord!" The petition explicitly asks God to remember the person through the lens of chesed rather than through the lens of the person's sin-history. This is a direct engagement with God's memory as the ground of compassion's extension: the appeal asks that divine memory selectively retrieve the covenantal loyalty rather than the moral record.
> 
> **God's remembering as compassion-act:** The inverse is also present — God remembering with compassion is a specific inner act. Psa 25:7 treats divine memory as something that can be oriented differently depending on whether it operates through chesed or through the record of transgressions. This makes memory a structural component of compassion's operation in the divine-human relationship.
> 
> **Memory as the context of compassion's sustaining:** Psa 48:9 (group 1633-003): "We have thought on your steadfast love, O God, in the midst of your temple." Meditating on God's chesed is named as a sustained inner act — holding the memory of divine compassion-love in the mind as an orienting reality. This is memory in service of compassion's sustaining effect: remembering the divine compassion shapes the inner life of the one who remembers.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=693 · finding_id='OBS-023-T2-061' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion enables and orients memory:** The supplication pattern shows that the person who approaches God for compassion does so by invoking specific memories — God's past acts of chesed, the person's own history of need and divine response. Compassion is sought through memory and is itself a form of remembering (God "remembering" the person through chesed). The receipt of compassion deepens the person's capacity to return to that memory as a sustaining resource (Psa 48:9 — meditation on steadfast love).
> 
> **The womb-memory connection:** Groups 1613-001 and 1613-002 describe the womb as the origin of human existence and the space from which God's compassionate sovereignty begins. Psa 22:10 — "from my mother's womb you have been my God" — grounds the appeal in an origin-memory: the relationship with God predates conscious memory. This is the deepest form of memory — the inner-being knowing that one has been held by God before one could remember being held.
> 
> **What is missing (P):** The data does not address whether receiving compassion heals or restores damaged memory — whether, for example, the person whose history is marked by the absence of compassion (neglect, abandonment) is restored at the level of memory when they receive it. This is a gap; no SD pointer addresses it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=694 · finding_id='OBS-023-T2-062' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The memory engagement reveals that compassion operates not only in the present moment but across time — it has a retrospective dimension (God's past acts of chesed as the ground of present appeal) and a prospective dimension (meditation on chesed as the orienting resource for future navigation). Compassion is temporally extended, not merely momentary.
> 
> This temporal extension is structurally connected to the chesed vocabulary: steadfast love (chesed) is by definition a loyalty that holds across time, through violation and return, through exile and restoration. Memory is the inner faculty that holds the continuity of that loyalty for the person — it is how the person retains access to compassion's sustaining reality between moments of active encounter.
> 
> The womb-origin dimension adds depth: the person who knows they have been held by God from before conscious memory has a memory-ground that is deeper than any specific experience of compassion. This prior-to-memory knowing is the deepest possible grounding of the capacity to return to God in supplication — one returns not merely to past kindnesses but to the originating relationship itself.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=695 · finding_id='OBS-023-T2-063' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — affect is the most directly and extensively evidenced faculty in the compassion data. The characteristic is constitutively affective: its primary vocabulary names the felt quality of the inner experience.
> 
> **Splanchnizō as the paradigmatic affective term:** The gut-stirring named by splanchnizō is an affective event — something felt, not merely cognised or willed. The abdominal location of the term in ancient anthropology (the entrails as the seat of the deepest emotions) confirms that this is affect at its most visceral and pre-reflective.
> 
> **Ni.chum as affective warmth:** Hos 11:8 — "my compassion grows warm and tender" — names the felt quality of compassion in temperature terms. Warmth is an affective quality: it names how the inner experience of compassion feels, not merely what it does or produces.
> 
> **Ra.cha.mim (plural) as accumulated affective depth:** The plural form of ra.cham (ra.cha.mim — compassions/mercies) names the affective quality as multiple, accumulated, and deep. Lam 3:22 — "his mercies never come to an end" — uses the plural to convey that this is not a single felt impulse but an inexhaustible reservoir of affective compassion.
> 
> **The maternal imagery:** The womb vocabulary carries deep affective resonance — the bond between mother and carried child is among the most affectively charged relationships in human experience. When Scripture uses this to describe divine compassion, it is reaching for the deepest available affective language.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=696 · finding_id='OBS-023-T2-064' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion enables affect — the eusplanchnos quality:** 1 Pet 3:8 — "tender heart" (eusplanchnos) — names the inner constitution that is open to affective movement. Compassion both requires and, over time, enables a tenderness of inner being that makes affective movement possible. The person formed in compassion becomes more affectively open, not less.
> 
> **Compassion deepens affect toward the suffering other:** The splanchnizō pattern shows that compassion does not merely acknowledge suffering intellectually — it is moved by it. The movement deepens the affective engagement with the other's condition: the person who is splanchnizō toward the widow of Nain (Luke 7:13) is not merely noting her grief but is affected by it in the body. Compassion deepens affect by requiring the person to be genuinely present to the other's emotional reality.
> 
> **The metriopatheō exception:** G3356 metriopatheō (Heb 5:2) names a form of compassion in which the affective response is moderated. This is not impairment of affect but calibration — compassion shaped by wisdom rather than overwhelmed by feeling. The data explicitly regrounds this moderation in shared vulnerability rather than philosophical suppression, which preserves the affective dimension while giving it appropriate form. Compassion does not bypass affect even when it moderates it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=697 · finding_id='OBS-023-T2-065' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The pattern reveals that compassion is one of the most constitutively affective characteristics in the programme vocabulary. It does not merely produce affective side-effects — affect is structurally integral to what compassion is. The vocabulary (gut-stirring, warmth, womb-bond, tender heart) insists on the felt quality of the inner experience. A compassion that is not felt is, in these terms, not the full phenomenon.
> 
> This has an important implication for the programme's understanding of the relationship between affect and moral action. In the splanchnizō pattern, the affective event (being moved) is not separable from the moral response (acting). Affect is not the accompaniment of compassion — it is the mechanism of its movement. The person who feels nothing upon perceiving suffering does not produce the compassion-action that the vocabulary describes. This places compassion in a unique position: it is a characteristic in which affect and moral action are structurally unified rather than sequentially related.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=698 · finding_id='OBS-023-T2-066' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the volitional faculty is engaged at two distinct points in compassion's constitutional movement, and in opposite directions depending on context.
> 
> **Volition as the suppressor of compassion (judicial contexts):** The chus vocabulary — "your eye shall not pity" (Deut 19:13; Ezek 7:4) — addresses the will directly. The compassion-impulse arises from perception; the will can then override it in contexts where judicial requirements demand non-pity. This is volition engaged against compassion: the capacity to choose suppresses the natural arising impulse. The fact that judicial prohibitions must be stated — "shall not pity" — reveals that the volitional suppression of compassion is not automatic; it requires a deliberate inner act.
> 
> **Volition as the executor of compassion (action contexts):** In the Synoptic pattern, the splanchnizō-movement produces volitional engagement in the service of compassion: "stretched out his hand" (Mark 1:41), "touched their eyes" (Matt 20:34). The will acts on the compassion-movement — choosing to cross boundaries, extend help, or initiate action. The volitional faculty here translates the affective stirring into directed action.
> 
> **The divine inner deliberation (Hos 11:8):** The divine heart recoiling and compassion warming in Hos 11:8 is presented as a volitional contest — compassion competing with judgment for the outcome of the divine will. Compassion wins; judgment is overridden. This is the most complex volitional engagement in the data: not suppression of compassion by will, and not simple execution of compassion through will, but a genuine deliberative resolution in which compassion determines the volitional outcome.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=699 · finding_id='OBS-023-T2-067' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion engages and tests volitional capacity:** The judicial-prohibition pattern shows that suppressing compassion requires a willed act — the capacity to choose is actively exercised. This tests volitional capacity: the person must choose to override a strong natural impulse. The frequency with which this prohibition is stated (seven times in Ezekiel alone — Pass 3 analysis) suggests that the volitional suppression of compassion is genuinely difficult — it must be repeatedly commanded because the will's natural inclination runs the other way.
> 
> **Compassion interacts with justice and righteousness at the volitional level:** The constraints under which volitional compassion operates are named in the data. Justice (Reg 98) and righteousness (Reg 139) are the characteristics that interact with compassion at the volitional level — they are what constrain or redirect the will when compassion would otherwise operate unchecked (SD-018). The volitional engagement is therefore not between compassion and absence of compassion but between compassion and other moral characteristics that lay claim on the will simultaneously.
> 
> **Compassion enables bold volitional action:** Mark 1:41 — compassion produces the crossing of the ritual-purity boundary. Luke 10:33 — the Good Samaritan stops, approaches, touches, and invests in the wounded stranger. Compassion appears to enable volitional acts that self-protective or socially-conventional inner states would not produce. The characteristic enables a quality of volitional boldness directed specifically toward the suffering other.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=700 · finding_id='OBS-023-T2-068' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The pattern reveals that compassion occupies a unique position relative to the volitional faculty: it is pre-volitional in origin (the somatic stirring precedes the choice) but volitionally engageable in both directions (toward action or toward suppression). This makes it unlike characteristics that are purely volitional (choice-dependent from the outset) and unlike characteristics that are purely affective (purely felt, not enacted).
> 
> Compassion is the inner-being reality that the will must reckon with — it is the natural arising that judgment must deliberately override, and it is the affective ground that courage-in-action enacts. The will does not initiate compassion but it determines what compassion produces: either restrained (judicial suppression) or released (boundary-crossing action). This positions compassion as the characteristic that most directly tests the moral quality of the will — whether the will serves the natural outward movement toward the suffering other or serves other moral demands that require its suppression.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=701 · finding_id='OBS-023-T2-069' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — agency is one of the most directly and consistently evidenced faculty-engagements in the compassion data. The registry description states: "Compassion always faces outward toward the one suffering and produces action." The production of action is definitional to compassion in this programme.
> 
> **Splanchnizō as action-generating:** Every splanchnizō event in the Gospels produces action: healing (Mark 1:41; Matt 20:34), feeding (Matt 15:32; Mark 8:2), raising the dead (Luke 7:14-15 — following v.13's compassion), teaching (Mark 6:34), crossing social boundaries (Luke 10:33-35 — the Samaritan's full investment in the stranger's recovery). The compassion-movement is never terminal — it always arrives at agency.
> 
> **Eleēmosunē as institutionalised agency:** G1654 (almsgiving) is the normalised social form of compassion-agency: the concrete act of giving through which the inner disposition becomes external action. The semantic development from pity to almsgiving (Pass 1, term 20) traces how compassion's agency becomes institutionalised in the community's social practice.
> 
> **The parable of the prodigal (Luke 15:20):** The father is splanchnizō, then runs, falls on the son's neck, kisses him — a cascade of agency. The compassion-movement produces an urgent, immediate, uninhibited expression of agency. Nothing intervenes between the gut-stirring and the running. This is compassion at its most agentive: the inner movement is immediately and fully expressed in action without hesitation or restraint.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=702 · finding_id='OBS-023-T2-070' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion enables bold and boundary-crossing agency:** As established at T3.6, compassion enables volitional acts that self-protective inner states would not produce. Mark 1:41 — physical touch of a leper; Luke 10:33-35 — the Samaritan's investment of time, money, and care in a stranger from the opposing cultural group; Matt 18:27 — the king releasing an enormous debt. In each case, the compassion-movement enables an act of agency that crosses a social, ritual, financial, or cultural boundary. Compassion expands the scope of what the person's agency will reach.
> 
> **Compassion produces urgent and uninhibited agency:** Luke 15:20 — the father runs. The compassion-generated agency is characterised by urgency and the absence of hesitation. The normal social constraints on a father's dignity (running in public, embracing before the son had spoken) are suspended by the compassion-movement. The inner event bypasses social restraints on agency.
> 
> **Compassion does not impair agency:** There is no evidence in the data that compassion impairs the agency faculty. The one limiting case — metriopatheō (Heb 5:2), dealing gently rather than acting unchecked — is not impairment of agency but its calibration. The high priest's gentleness is itself an act of agency, shaped by understanding.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=703 · finding_id='OBS-023-T2-071' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The consistent agency-generation pattern reveals that compassion is not a terminal inner state — it does not complete itself in feeling. It completes itself in action directed toward the one who is suffering. The registry description captures this precisely: "Compassion always faces outward toward the one suffering and produces action."
> 
> This has significant implications for the programme's understanding of the relationship between inner being and outward behaviour. Compassion is the clearest example in the data of a characteristic that structurally requires an outer expression to be fully itself. A compassion that feels but does not act is, in the terms of the data, incomplete. This places compassion in a structurally distinct category: it is a characteristic whose inner reality is constitutively incomplete without its outward expression. The eleēmosunē evidence confirms this from the social side: compassion that does not give has not fully arrived (Pass 1, term 20).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=704 · finding_id='OBS-023-T2-072' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — moral evaluation is engaged at several points in the compassion data.
> 
> **The judicial-prohibition pattern:** The chus vocabulary in judicial contexts presupposes a moral evaluation: the law identifies cases in which the compassion-impulse is morally wrong to follow (Deut 7:16; 19:13 — the cases of idolaters, murderers). The moral evaluation faculty is what identifies these as cases where justice requires the suppression of compassion. Compassion interacts with moral evaluation by providing an impulse that moral evaluation then assesses as appropriate or inappropriate to the context.
> 
> **Compassion as the moral standard in the Good Samaritan (Luke 10:33):** In the parable, compassion (splanchnizō) is the moral criterion by which the Samaritan is judged to have acted rightly and the priest and Levite are judged to have acted wrongly. The moral evaluation faculty in the hearer (and the lawyer asking the question) is asked to assess the three travellers, and compassion is the standard by which the assessment is made. Compassion here is not only an inner experience — it is a moral norm.
> 
> **The chesed-as-moral-requirement vocabulary:** Mic 6:8 — "love kindness" (chesed) — places the chesed-compassion quality within an explicit moral framework alongside doing justice and walking humbly. Moral evaluation of one's life includes the assessment of whether one has practised chesed. The Hos 6:6 anchor — "I desire steadfast love and not sacrifice" — makes chesed the moral standard by which ritual observance is evaluated. Compassion is the measure of authentic moral life.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=705 · finding_id='OBS-023-T2-073' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion deepens moral evaluation:** The Good Samaritan pattern shows that compassion produces a deeper moral perception — seeing the wounded man as a full person, a neighbour, worthy of complete investment. The compassion-movement enables the moral evaluation faculty to assess the situation rightly. Without it, the priest and Levite assessed incorrectly — they saw the situation through the lens of ritual risk and social distance rather than through the lens of human need.
> 
> **Compassion is the moral evaluative standard in key contexts:** Hos 6:6 — "I desire steadfast love (chesed) and not sacrifice" — places compassion above ritual observance as the moral norm. Jesus cites this verse twice (Matt 9:13; 12:7 — though these are not anchor verses in this registry, the Hos 6:6 anchor links to the Synoptic pattern). Compassion as moral standard deepens the moral evaluation of all other practices — sacrifice, ritual, observance — by providing the criterion against which they are measured.
> 
> **Compassion does not bypass moral evaluation:** The judicial prohibition pattern (chus — "shall not pity") shows that compassion can be assessed as morally wrong to follow in specific contexts. The moral evaluation faculty retains authority over the compassion-impulse. Compassion does not claim exemption from moral assessment — it is itself subject to the moral evaluation of whether and how it should be expressed.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=706 · finding_id='OBS-023-T2-074' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.8'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The pattern reveals a complex bidirectional relationship: compassion is both subject to moral evaluation (it can be assessed as appropriate or inappropriate in context) and itself a moral evaluative standard (the criterion against which other practices and persons are assessed). This is not a contradiction — it is the mark of a morally mature characteristic.
> 
> Compassion operates within the moral order (it can be rightly suppressed by justice) while simultaneously providing the inner standard by which the moral order's authenticity is tested (chesed as the criterion of genuine covenant relationship). This places compassion at the centre of the programme's moral anthropology: not above the moral order (exempt from evaluation) and not below it (merely a feeling to be assessed) but within and constitutive of it — the characteristic whose presence or absence is the most direct indicator of authentic moral life.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=707 · finding_id='OBS-023-T2-075' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.9'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides partial evidence of conscience-engagement, primarily through the guilt and supplication vocabulary.
> 
> **Conscience in the supplication context:** The supplication vocabulary (techinah, tahanun — "supplication for mercy") implies a conscience-engagement: one appeals for compassion because one is aware of one's own moral condition and need. The act of earnest appeal for divine compassion presupposes that the petitioner has a conscience that recognises their own insufficiency, unworthiness, or sin. Psa 25:7 — "Remember not the sins of my youth" — is addressed to the God of chesed, and it implies an acute awareness of the moral record that makes the appeal necessary.
> 
> **Conscience and the chesed/grace vocabulary:** The channum (gracious) vocabulary's "guilt resolution" note in the data (Pass 1, term 6 sense analysis) indicates that the graciousness dimension of compassion engages conscience: it is specifically the response to guilt that needs resolving. The person appealing for divine channum (graciousness) does so from a position of guilt-awareness — conscience has done its work and produced the appeal.
> 
> **What is missing (P):** The data does not directly address whether receiving compassion heals or silences the conscience — whether the person who has received divine compassion-forgiveness is released from the inner-witness of guilt. The connection between compassion and conscience-healing is implied (particularly through the chesed vocabulary and its link to the forgiveness registry) but not established in the current data. No SD pointer covers this specific question; it is a new gap.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=708 · finding_id='OBS-023-T2-076' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.9'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion may enable conscience indirectly:** The recognition of one's own pitiable condition (eleeinos — Rev 3:17) requires a form of inner-witness function that is conscience-adjacent — the capacity to see one's own true moral and spiritual state. Where compassion creates the inner environment for honest self-perception, it may enable the conscience to function more accurately. The self-deceived Laodiceans' failure of conscience is linked to their failure of compassion-reception.
> 
> **Compassion as the ground of moral return (Joel 2:13):** "Rend your hearts... for he is gracious and merciful (rachum ve-channum)." The divine compassion-character is the reason given for the inner act of moral rending. Compassion here enables the conscience to act: knowing that God is compassionate makes it possible to face and act on conscience's witness. Without the certainty of divine compassion, conscience might produce paralysis rather than return.
> 
> **What is missing (P):** Whether compassion heals or restores damaged or silenced conscience is not addressed. This is a gap for Session D, potentially intersecting with the forgiveness registry (R064).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=709 · finding_id='OBS-023-T2-077' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.9'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The pattern reveals that compassion functions as the enabling context for conscience's constructive operation. Conscience is what creates the awareness of need that makes appeal for compassion possible; compassion is what makes it safe for conscience to do its work without producing despair or paralysis.
> 
> This is a structural relationship: conscience creates the inner pressure that drives the person toward compassion; compassion creates the inner safety that allows conscience to speak. They are mutually enabling rather than sequential or competitive. The data supports this partial picture but does not fully develop it — the conscience-compassion relationship is a significant gap in the current analysis that belongs to Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=710 · finding_id='OBS-023-T2-078' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.10'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — and compassion may be the most directly conscience-action-integrating characteristic in the programme vocabulary.
> 
> The eleēmosunē (almsgiving) evidence is the clearest: Luke 11:41 — "Give as alms those things that are within, and behold, everything is clean for you." The inner disposition (compassion/mercy) produces the outer act (almsgiving), and the outer act is valid only when it expresses the inner quality. This is conscientiousness in its fullest form: the integration of inner moral awareness (the person knows they have compassion-capacity and a moral obligation to use it) with volitional decision (choosing to give) and action (the actual giving).
> 
> **The Mic 6:8 integration:** "Do justice, love kindness (chesed), and walk humbly with your God." This is the programme's most compressed statement of integrated moral life. Chesed/compassion is placed alongside justice and humility as a co-equal dimension of the conscientiously lived life. The verb "love" (ahav) names the inner quality; the implied outward expression is the practice of chesed in daily life. The integration of inner disposition and outer practice is explicitly required.
> 
> **The Good Samaritan as the paradigmatic conscientious act:** Luke 10:33-35 — compassion (splanchnizō) → crossing the boundary → binding wounds → carrying to the inn → investing resources → promising continued care. This is a complete conscientious sequence: inner moral awareness (seeing the need), volitional engagement (choosing to stop), and sustained action. The parable is presented as the answer to a moral question (what must I do to inherit eternal life? — Luke 10:25), making the compassion-generated action a direct instantiation of conscientiousness.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=711 · finding_id='OBS-023-T2-079' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.10'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion enables conscientiousness by providing the motivational ground:** The sequence at T3.10 Prompt 1 shows that compassion provides the inner energy that drives the conscientious act. Without the gut-stirring, the priest and Levite did not stop. The Samaritan stopped because he was moved. Conscientiousness requires not only moral awareness and volitional capacity but a motivating inner force — and compassion provides that force. It is the affective-relational energy that makes conscientious action possible rather than merely obligatory.
> 
> **Compassion does not bypass conscientiousness:** Matt 6:2-4 explicitly addresses the manner of almsgiving — it must not be for public display. The inner quality of compassion must govern the form of the conscientious act. Conscientiousness here is not replaced by compassion but shaped by it: the how of the act (privately, from inner purity) is governed by the inner character of the compassion that motivates it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=712 · finding_id='OBS-023-T2-080' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.10'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The pattern reveals that compassion is uniquely positioned as the motivational ground of conscientiousness. Other characteristics may engage conscientiousness cognitively (moral awareness) or volitionally (the will to act rightly); compassion provides the affective-relational energy that makes the conscientious act self-sustaining rather than effortful. The person who acts compassionately is not primarily performing a duty — they are expressing what they feel and who they are. This is why the eleēmosunē vocabulary connects inner disposition to outer act so directly: the act is the natural overflow of the inner state, not an external moral requirement superimposed on an unwilling or neutral inner being.
> 
> This places compassion in an important structural position within the programme's moral anthropology: it is the characteristic whose presence most directly converts moral knowledge into motivated action. This is a finding with implications for Session D synthesis — particularly for understanding how the programme conceives the relationship between inner character and outer moral life.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=713 · finding_id='OBS-023-T2-081' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T3.11'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — relational capacity is the most central faculty in compassion's operation. Compassion is constitutively relational: it cannot exist without an other, and it defines the person's inner equipment for genuine connection.
> 
> **Compassion as genuine entry into another's experience:** The SYM-PATH vocabulary (sumpatheō, sumpaschō, sumpathēs) names the relational capacity dimension of compassion most precisely — it is the capacity for genuine entry into another's inner experience rather than engagement from a safe relational distance. Heb 4:15 — Christ sympathising with our weaknesses because he has been tempted — is the paradigm of relational capacity at its fullest: the one who has shared the experience from the inside is constitutionally equipped to be genuinely present to it in another.
> 
> **The Good Samaritan and the neighbour question:** Luke 10:33 — splanchnizō as the defining act of the one who correctly answers "who is my neighbour?" — makes compassion the constitutional ground of extended relational capacity. The Samaritan's compassion equips him to relate across cultural, ethnic, and social distance. This is relational capacity in its expansive form: not merely relating within established bonds but across boundaries of difference and distance.
> 
> **1 Pet 3:8 — compassion as community-constituting:** Sumpathēs (sympathetic) within the list of community virtues (unity of mind, brotherly love, tender heart, humble mind) names compassion as a constitutive quality of the relational fabric of the community. Relational capacity at the community level requires this quality: without sympathy, genuine community connection is impaired.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=714 · finding_id='OBS-023-T2-082' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T3.11'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Compassion expands relational capacity beyond natural boundaries:** The Good Samaritan pattern is the clearest evidence: compassion extends relational capacity to those outside the natural in-group (the wounded Jew, the stranger). Mark 1:41 — compassion toward the leper — crosses the ritual-impurity boundary. The compassion-characteristic enables the person to relate genuinely across boundaries that would otherwise exclude.
> 
> **Compassion deepens relational capacity through solidarity:** Sumpaschō (1 Cor 12:26 — "if one member suffers, all suffer together") names the deepest form of relational connection within the community: a genuine constitutional solidarity in which the suffering of one is felt by all. Compassion deepens relational capacity to the point where the boundary between self and other becomes permeable at the affective level — the other's suffering becomes one's own inner experience.
> 
> **Compassion does not bypass relational capacity:** The data shows no evidence of compassion operating in isolation from genuine relational engagement. Even the metriopatheō (moderated compassion) of Heb 5:2 is a form of deepened relational engagement — not a distancing strategy but a calibrated presence. Compassion is never described as operating at a distance or substituting for genuine relational contact.
> 
> **The eusplanchnos (tender heart) as the relational pre-condition:** The tender heart of 1 Pet 3:8 names the inner quality that makes genuine relational capacity possible. Without this constitutional openness, compassion cannot arise and relational capacity remains closed or defended. The tender heart is the relational pre-condition that compassion both requires and, over time, deepens.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=715 · finding_id='OBS-023-T2-083' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T3.11'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The instruction note for T3.11 asks for a distinction between characteristics that build/sustain relational connection and those that restore/repair it. The compassion data reveals that compassion does both, but in distinct modes corresponding to the two vocabulary families:
> 
> **Building and sustaining:** The chesed vocabulary (steadfast love, covenantal loyalty) describes compassion as the quality that builds and sustains relational bonds across time, through violation, and in the face of unfaithfulness. Chesed builds and sustains relational connection — it is the loyal love that does not withdraw when the other fails.
> 
> **Restoring and repairing:** The splanchnizō and chus/eleēmosunē vocabulary describes compassion as a movement toward those who are broken, lost, or in need — it repairs relational rupture and restores those who have been excluded (the leper, the lost son, the wounded stranger). This is compassion as restoring agent rather than sustaining quality.
> 
> **Extending (new category):** The Good Samaritan pattern adds a third mode not captured by either building/sustaining or restoring/repairing: extending relational capacity to those with whom no prior relationship exists. This is compassion as relational pioneer — opening new relational territory where none previously existed. This is a *New finding* that may have implications for other registries in the programme.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=716 · finding_id='OBS-023-T2-084' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T4.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the God-to-human direction is the most extensively evidenced direction in the entire compassion data. It is the dominant structural direction of the vocabulary.
> 
> The Pass 2 God-as-Subject table confirms that the GOD_AS_SUBJECT flag is warranted for the majority of the primary terms: H2587 channum (almost exclusively divine epithet), H2617B chesed (predominant divine referent across Psalter, prophets, and historical books), H5150 ni.chum (2/3 occurrences divine), H2551 chem.lah (Gen 19:16 — divine), G3627 oikteirō (Rom 9:15 — exclusively divine sovereignty), G4697 splanchnizō (Jesus as primary Synoptic subject), G4184 polusplanchnos (Jas 5:11 — divine).
> 
> **How it operates:** The God-to-human direction operates across several distinct modes:
> 
> - **Constitutional declaration:** Exod 34:6 — God declares his own compassion-character as a defining attribute. This is not a response to a specific human situation but a self-revelation of inner character. God's compassion operates toward the human person as a prior fact of his nature.
> 
> - **Responsive mercy in individual need:** Gen 19:16 (chem.lah — Lot), Jon 4:11 (chus — Nineveh), Isa 57:18 (ni.chum — the straying healed). God perceives the condition and moves toward the person in mercy.
> 
> - **Sustained covenantal presence:** The chesed vocabulary in the Psalter (Psa 25:7; 48:9; Lam 3:22) names God's compassion as the continuous covenantal orientation toward the human person — not episodic but ongoing, "never ceasing."
> 
> - **Incarnate movement:** Jesus's splanchnizō-movements (Matt 9:36; Luke 7:13; Mark 1:41) are the God-to-human direction of compassion in its most embodied, immediate form. The Incarnation does not merely describe divine compassion — it enacts it in the space of direct human encounter.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=717 · finding_id='OBS-023-T2-085' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T4.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals that God's compassion operates on multiple bases simultaneously, and these are not in contradiction:
> 
> **Sovereignly free (unconditional at the divine initiative level):** Rom 9:15 — oikteirō — "I will have compassion on whom I have compassion." This is the most direct statement in the data: divine compassion is sovereignly free, not earned or elicited by human merit or condition. God's compassion is not a response to human worthiness.
> 
> **Covenantal (constitutive of the covenant relationship):** The chesed vocabulary is definitionally covenantal — steadfast love is the loyalty that holds the covenant from God's side regardless of Israel's faithfulness. Lam 3:22 — "his mercies never come to an end" — names chesed as the unbreakable covenantal commitment. This is not unconditional in the sense of indifferent to covenant — it is the covenant's foundation on the divine side.
> 
> **Responsive (to need and suffering):** The splanchnizō pattern in the Gospels shows God-in-Christ responding to what he sees — the crowd without a shepherd, the widow's grief, the leper's condition. This responsiveness does not contradict sovereign freedom — it is the form that sovereign compassion takes when it encounters actual human suffering.
> 
> **Temporally asymmetric with judgment:** Isa 54:8 — a moment of anger, then everlasting chesed/racham. God's compassion is the characteristic that re-asserts itself after judgment. This is responsive in a temporal sense: it is what God returns to. The anger is real but temporary; the compassion is permanent. This temporal structure is itself data about the basis of divine compassion — it is the ground state of God's orientation toward the human person.
> 
> **Key finding:** The data does not support a reading of divine compassion as merely conditional (earned by human behaviour) or merely unconditional (indifferent to the human situation). It is sovereignly free, covenantally grounded, and situationally responsive — all simultaneously.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=718 · finding_id='OBS-023-T2-086' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T4.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals three dimensions of divine disposition:
> 
> **Constitutive orientation toward the human:** God's compassion is not a decision made in response to human need — it is the character of his inner being that precedes and underlies all encounter with the human person. The Exod 34:6 self-declaration names this as the constitutive truth about who God is. God's disposition toward the human person is compassionate before the human person does anything or becomes anything.
> 
> **Deliberative retention of compassion over judgment:** Hos 11:8 — the divine inner contest in which compassion wins over judgment — reveals a disposition that actively maintains compassion against the claims of righteousness and justice. God does not merely feel compassion; he chooses it against competing inner orientations. The deliberate character of the divine compassion-commitment means it is not a sentiment but a sustained volitional orientation.
> 
> **Maternal intimacy:** The womb-language (ra.cham, re.chem; Isa 46:3) reveals that God's disposition toward the human person is not that of a distant benevolent authority but of the one who carries life from within. The most intimate possible relational stance — bearing another inside one's own body — is the image Scripture uses for God's compassionate disposition. This is the deepest available statement about divine inner orientation toward the human person: God is disposed toward the person as a mother toward the child she is carrying.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=719 · finding_id='OBS-023-T2-087' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T4.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the human-to-God direction is well-evidenced through the supplication vocabulary, which is structurally embedded in the compassion data as a significant XREF set.
> 
> **Supplication as the human-to-God compassion-interface:** H8467 techinah (supplication, 24 XREF occurrences) and H8469 tahanun (entreaty, 18 XREF occurrences) both derive from the CHANAN root (grace/favour/compassion). They name the verbal acts through which the human person appeals for divine compassion. The structural relationship established by this vocabulary: God's compassion is the presupposed ground that makes earnest appeal possible (SD-021). The human person who approaches God in supplication is acting on the knowledge that God is compassionate — the appeal would be irrational if God were not.
> 
> **Psalm vocabulary of seeking chesed:** Psa 25:7 (group 1633-003) — "according to your steadfast love remember me" — is directed toward God. Psa 48:9 — "we have thought on your steadfast love, O God, in the midst of your temple." These are human-to-God movements in which the human inner being orients itself toward and rests in divine chesed. This is not supplication under duress but contemplative orientation — the human person's inner being actively seeking and dwelling in the reality of divine compassion.
> 
> **Covenantal return enabled by compassion (Joel 2:13):** "Return to the LORD your God, for he is gracious and merciful (rachum ve-channum)." The divine compassion-character is the basis and motivation for the human movement back toward God. The human-to-God direction here is one of return — the inner act of repentance and reorientation toward God, enabled and motivated by the certainty of his compassion.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=720 · finding_id='OBS-023-T2-088' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T4.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three inner postures emerge from the data as required for the human-to-God compassion-movement:
> 
> **Vulnerability and need-recognition:** The supplication vocabulary presupposes that the person knows they need what they are asking for. The act of earnest appeal (techinah, tahanun) is constitutively a posture of acknowledged insufficiency. The person who believes themselves self-sufficient (the Laodicean pattern — Rev 3:17) cannot make this movement. Vulnerability — the open awareness of one's own pitiable condition — is the enabling inner posture.
> 
> **Heart-openness (Joel 2:13 — heart-rending):** "Rend your hearts and not your garments." The inner posture required for the movement toward God's compassion is not ritual performance but heart-level openness — the tearing apart of inner defences and self-protection. This is a posture of radical inner availability: the person brings not a performance but an exposed inner life.
> 
> **Trust in divine chesed as the ground:** Psa 25:7 grounds the supplication in "your steadfast love" — the person approaches God not on the basis of their own worthiness but on the basis of God's established character. The inner posture required is trust in the divine compassion-character as the reliable ground of appeal. Without this trust, the appeal cannot be made with the confidence implied by the word techinah (earnest supplication, not tentative request).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=721 · finding_id='OBS-023-T2-089' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T4.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The human-to-God direction of compassion reveals a relationship characterised by three structural features:
> 
> **Asymmetric but genuinely reciprocal:** The human person does not extend compassion to God in the same way God extends it to the human person — the human person's movement toward God is one of appeal, seeking, and return, not of mercy-giving. Yet the movement is genuinely relational: the person is not passive before a sovereign who dispenses; they actively seek, contemplate, and return. The relationship is asymmetric in power and in the direction of compassion's primary flow but genuinely reciprocal in its relational character.
> 
> **Grounded in divine character rather than human performance:** The human person's appeal is always addressed to what God is, not to what the person has done. Psa 25:7 — "according to your steadfast love" — is the recurring structural feature: the ground of appeal is divine character, not human merit. This reveals a relationship in which the human person's movement toward God is constitutively humble — it cannot be based on self-presentation.
> 
> **Enabled by the certainty of divine compassion:** The very existence of the supplication vocabulary — earnest, expectant, persistent appeal — reveals that the human person's relationship with God is characterised by the expectation that divine compassion will respond. Techinah is not a tentative request; it is earnest appeal grounded in the knowledge of who God is. The relationship is one in which the human person can approach with confidence — not in their own standing but in the divine compassion-character that is the ground of all approach.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=722 · finding_id='OBS-023-T2-090' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T4.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the human-to-human giving direction is well-evidenced, primarily through the splanchnizō Gospels pattern (human subjects), the sumpatheō/sumpaschō vocabulary, and the eleēmosunē evidence.
> 
> **Luke 10:33 — the Good Samaritan:** The most explicit human-to-human compassion-giving in the data. The Samaritan is splanchnizō toward the wounded man and extends an extraordinary investment of care: binding wounds, providing transport, shelter, and ongoing financial provision. This is compassion-giving in its fullest and most complete form — extending across cultural distance, at personal cost, to a stranger.
> 
> **Luke 15:20 — the father of the prodigal:** Splanchnizō in a relational-moral context. The father's compassion-movement produces immediate, uninhibited action: running, embracing, kissing, restoring to full sonship. This is compassion-giving within a broken relational bond — the restoration of what was lost.
> 
> **Matt 18:27 — the king in the parable:** Splanchnizō producing release of debt. Compassion-giving in a judicial-moral context — mercy rather than judgment, at great personal financial cost to the king.
> 
> **Heb 10:34 — sumpatheō in the community:** The readers showing compassion (sumpatheō) to those in prison, expressed through the joyful acceptance of property plundering. This is participatory compassion-giving in the context of persecution — sharing in another's loss as an act of genuine solidarity.
> 
> **G1654 eleēmosunē:** Almsgiving as the normalised social form of compassion-giving. Matt 6:2-4 establishes the manner: privately, from inner purity, not for display. Luke 11:41 — "give as alms those things that are within" — grounds the outer act in the inner quality.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=723 · finding_id='OBS-023-T2-091' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T4.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Four inner conditions emerge from the data:
> 
> **Perceptive openness (sight of the other's condition):** As established at T3.1, compassion-giving requires seeing the other's condition genuinely. The Good Samaritan sees and is moved; the priest and Levite see and pass by. The enabling inner condition is not merely physical sight but the perceptive openness that allows what is seen to produce inner movement. This cannot be forced — it is the condition of the person who has not closed their inner perception against the reality of suffering.
> 
> **Eusplanchnos — tender heart (1 Pet 3:8):** The constitutional pre-condition for compassion-giving is a tender inner being — one that has not been hardened against the suffering of others. This is the inner quality from which the splanchnizō movement can arise naturally. A hardened heart cannot give compassion because it cannot be moved.
> 
> **Inner purity as the ground of authentic giving (Luke 11:41; Matt 6:2-4):** Genuine compassion-giving requires that the inner disposition match the outer act. Matt 6:2 identifies the failure mode: almsgiving done "to be praised by others" is compassion-giving divorced from its inner ground. The enabling condition is that the giving flows from the actual inner movement of compassion rather than from social motivation.
> 
> **Prior reception (implied by the mirroring principle, 2 Sam 22:26):** The data suggests that genuine compassion-giving is enabled by having received compassion — the person who has been shown mercy by God has the inner ground from which to show mercy to others. The mirroring principle (with the merciful you show yourself merciful) implies that God's compassion toward the person constitutes the inner ground from which the person's compassion toward others flows. This is implicit in the data rather than directly stated, but it is consistent with the structural logic of the vocabulary.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=724 · finding_id='OBS-023-T2-092' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T4.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **What the evidence suggests:** The mirroring principle (2 Sam 22:26) implies that prior reception of divine compassion is constitutively connected to the capacity for human compassion-giving. The devout person (chasid — H2623 XREF) is the one whose inner life embodies chesed — a quality formed through the sustained experience of divine chesed. The Exod 34:6 formula grounds human compassion in the divine character: to give chesed to others, one must first have been sustained by divine chesed.
> 
> The sumpatheō Christological grounding (Heb 4:15 — Christ sympathising because he has been tempted) establishes the participatory principle: genuine compassion-giving requires having been in the inner experience one is responding to. Christ can sympathise with human weakness because he has shared it. By implication, the human person who has suffered, been in need, and received compassion in that need has the inner ground to give compassion genuinely to those in a similar condition.
> 
> **What is missing (P):** The data does not directly state that prior reception of compassion is a necessary condition for genuine compassion-giving — it implies it through the structural logic of the vocabulary. Whether compassion-giving is possible without prior reception (e.g., through formation rather than experience) is not addressed. This is a gap; no SD pointer covers it directly.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=725 · finding_id='OBS-023-T2-093' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T4.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data addresses reception of compassion from God toward the human person extensively (covered at T4.1), but reception of compassion from one human person to another is partially evidenced and the inner-being dynamics of reception are largely unaddressed.
> 
> **What is evidenced:** Gen 19:16 — Lot receives divine compassion (chem.lah) when the angels physically take him and his family by the hand and lead them out. The reception is enacted bodily — the compassion-act reaches him physically and produces rescue. Isa 57:18 — the straying person receives divine comfort (ni.chum) — "I will heal him; I will lead him and restore comfort to him." The reception produces healing and restoration.
> 
> In the Synoptic pattern, the recipients of Jesus's splanchnizō-movements receive healing (Matt 20:34 — "their eyes were opened"), restoration (Luke 7:14-15 — the widow's son raised), and feeding (Matt 15:32ff). The reception of compassion in these contexts produces material change in the recipient's condition.
> 
> **What is missing (P):** The inner-being dynamics of receiving compassion — what happens inside the person at the moment of reception — are almost entirely absent from the data. The focus of the vocabulary is on the giver's inner movement and the outer act of compassion, not on the receiver's inner experience. The gap identified at T1.5 P1 (receiver's immediate inner response) is reproduced and deepened here.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=726 · finding_id='OBS-023-T2-094' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T4.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Enabling conditions (partial):** The eleeinos evidence (Rev 3:17) establishes that the capacity to recognise one's own pitiable condition is necessary for reception. Without this recognition, compassion cannot reach the person who needs it. Need-recognition is therefore the primary enabling condition for reception — the inner openness that comes from knowing one is in need.
> 
> The supplication posture — earnest appeal (techinah, tahanun) — implies that active seeking of compassion is an enabling inner condition. The person who cries out positions themselves to receive.
> 
> **Blocking conditions:** Self-sufficiency and prosperity-blindness (the Laodicean pattern) block reception by preventing need-recognition. The person who believes they need nothing cannot open to what is being extended toward them.
> 
> **What is missing (P):** Reception of compassion specifically from another human person (rather than from God) is not addressed in terms of its enabling and blocking conditions. The human-to-human reception dynamics are entirely silent in the data. This is a significant gap; no SD pointer addresses it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=727 · finding_id='OBS-023-T2-095' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T4.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data addresses one case directly (already named at T1.7 P3) and implies others:
> 
> **The self-deceived (Rev 3:17):** The Laodiceans encounter the implicit compassion of the divine warning (Rev 3:17-20 — Jesus standing at the door, knocking) but cannot receive it because they cannot perceive their own pitiable condition. Their inner-being state is one of self-enclosed sufficiency — the door is closed from the inside (v.20 — "I will come in to him... if anyone hears my voice and opens the door"). The person who does not receive compassion in this mode remains in their actual condition of destitution while believing themselves rich.
> 
> **The hardened (implied by judicial non-pity):** The person whose inner orientation has been set toward judgment — whose eye has been trained not to pity — may encounter compassion from another and be unable to receive it because their inner constitution is oriented against it. This is speculative from the data and should be flagged as interpretation.
> 
> **What is missing (P):** The data does not describe the inner state of a person who encounters human compassion but cannot or will not receive it — who is in genuine need but closed against the compassion being extended. The inner experience of that closure is entirely absent from the data. This is a significant gap; no SD pointer addresses it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=728 · finding_id='OBS-023-T2-096' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '4'  ·  Segment: 'T4.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The receiving direction is partially evidenced (outer acts of compassion reach the recipient and produce material change) but the inner-being dynamics of reception are largely silent. The gap is specifically in the interior experience of the receiver — what happens inside the person at the moment compassion reaches them. This is the programme's most significant unaddressed question for this registry and is named as a new gap for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=729 · finding_id='OBS-023-T2-097' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T4.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data reveals that compassion operates distinctly in both modes, and the distinction is analytically important.
> 
> **Within existing relational bonds (chesed):** The chesed vocabulary is definitionally relational — it names the loyal love that sustains bonds through time and across failure. Chesed operates within the covenantal relationship: between God and Israel, between king and vassal, between person and community. Within these bonds, compassion functions as the quality that holds the bond together when it would otherwise break — it sustains rather than initiates.
> 
> **Across relational distance and difference (splanchnizō):** The Synoptic compassion-movements operate primarily across distance: toward crowds of strangers (Matt 9:36), toward a widow unknown to Jesus (Luke 7:13), toward a leper (Mark 1:41 — ritually excluded). The most explicit example is Luke 10:33: the Good Samaritan's compassion crosses the sharpest relational boundary in the data — the Jewish/Samaritan divide, a boundary of ethnic, cultural, and religious hostility. Compassion here is explicitly operating across difference rather than within existing bonds.
> 
> **Key finding:** The vocabulary differentiates these two operational modes: chesed operates within bonds; splanchnizō operates across distance and difference. These are not in competition — they name different relational registers of the same characteristic. But they are distinct enough that the programme should not conflate them.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=730 · finding_id='OBS-023-T2-098' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T4.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data clearly establishes that compassion crosses covenantal boundaries — this is one of its most structurally significant features.
> 
> **Jon 4:11 — Nineveh:** God's pity (chus) for Nineveh — a pagan city — is one of the data's most pointed boundary-crossings. The 120,000 people who "do not know their right hand from their left" are not covenant members; they are outside Israel's covenantal relationship with God entirely. God's compassion extends to them. Jonah's resistance to this extension (the narrative context of Jon 4) confirms that the covenantal boundary-crossing is deliberate and theologically significant — it is precisely the point of the passage.
> 
> **Luke 10:33 — the Good Samaritan:** The Samaritan extends compassion to the Jew, crossing not only an ethnic and cultural boundary but a specifically religious and covenantal one. In this parable, compassion defines who the neighbour is — and the answer explicitly includes the person outside one's own covenantal community.
> 
> **Matt 18:27 — the king's mercy:** The parable's king shows compassion (splanchnizō) toward his servant — a relationship of power and obligation rather than covenant. Compassion here is not contingent on covenantal membership.
> 
> The covenantal vocabulary (chesed) does operate primarily within covenantal relationships. But the wider compassion vocabulary (splanchnizō, chus, oikteirō) explicitly crosses covenantal boundaries. The data supports a reading in which compassion's inner character is broader than the covenantal forms through which it is often expressed.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=731 · finding_id='OBS-023-T2-099' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T4.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals a progressive expansion of relational scope across the vocabulary and the canon:
> 
> **Included (evidenced):** The covenant community (chesed toward Israel); individuals within the covenant in specific need (Lot, the widow of Nain, the leper); the morally wayward within the covenant (the prodigal, the unforgiving servant's debtor); those outside the covenant in conditions of suffering or ignorance (Nineveh, the wounded Jew in Luke 10); and those who suffer within the community of faith regardless of merit (the imprisoned believers in Heb 10:34).
> 
> **The scope-limiting factor — withheld pity (H2347 chus):** The judicial-prohibition contexts establish that there are cases in which compassion is deliberately withheld — specifically in the execution of divine judgment against covenant-violators (Deut 7:16; 13:8; Ezek 7:4). These are not the absence of compassion but its deliberate suspension. The chus evidence establishes that compassion's scope is not unlimited in all contexts — it is bounded by justice.
> 
> **The excluded (by implication):** Those who are wilfully impenitent and who have exhausted the patience of divine judgment may be outside the scope of active compassion-extension in specific judicial moments. However, the temporal asymmetry of Isa 54:8 (anger is momentary; chesed is everlasting) suggests that even these exclusions are temporary rather than permanent.
> 
> **Summary:** The scope of compassion as evidenced in the data extends from the covenant community outward to the stranger, the pagan city, and the victim across cultural boundaries. Its outer limit is not ethnic, religious, or moral standing — it is defined primarily by the presence of suffering and need perceived by the one who is moved to respond. Its only evidenced limitation is the deliberate suspension of compassion in specific judicial contexts.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=732 · finding_id='OBS-023-T2-100' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data evidences transformation in both modes, differentiated by the direction and vocabulary involved.
> 
> **Transformation of condition:** The splanchnizō action-pattern in the Gospels produces material change in the recipient's condition. Matt 20:34 — "their eyes were opened." Luke 7:14-15 — the widow's son raised to life. Mark 1:41-42 — the leper cleansed. These are not changes in the person's orientation to their condition (the leper is not helped to accept his leprosy) — they are changes in the condition itself. Divine compassion enacted through Jesus changes what is actually the case for the recipient.
> 
> **Transformation of orientation:** The chesed and ni.chum vocabulary points toward a different kind of transformation. Isa 57:18 — "I have seen his ways, but I will heal him; I will lead him and restore comfort (ni.chum) to him and his mourners." The healing and comfort here produces a change in inner orientation — the straying is restored to a right relationship with God. The transformation is not primarily external but in the person's inner bearing and direction.
> 
> The Joel 2:13 call — "rend your hearts and return to the LORD your God, for he is gracious and merciful" — names a transformation of orientation that divine compassion makes possible: the knowledge of God's rachum ve-channum character enables the inner act of heart-rending and return. The person's orientation toward God is transformed by the encounter with divine compassion.
> 
> **Both simultaneously:** Luke 15:20-24 — the prodigal receives both. The father's compassion produces material restoration (robe, ring, shoes, feast — condition changed) and relational restoration (the son who was "lost is found, dead and is alive" — orientation and relational status transformed). The parable presents both dimensions as inseparable consequences of a single compassion-event.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=733 · finding_id='OBS-023-T2-101' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data addresses reversibility indirectly through two contrasting lines of evidence:
> 
> **Reversibility evidenced (Lam 4:10):** The compassionate character quality (ra.cha.ma.ni) of the women in Lam 4:10 is violated under the extreme pressure of the siege. The character quality that defined them as compassionate persons was not proof against external catastrophe — it was violated, inverted, and forced into its opposite. This suggests that the transformation of character produced by compassion (becoming a compassionate person) is not irreversible under all conditions. Sufficient external pressure can force the violation of the deepest formed inner qualities.
> 
> **Durability evidenced (chesed vocabulary):** Lam 3:22 — "his mercies never come to an end; they are new every morning." The everlasting chesed vocabulary names divine compassion as inherently irreversible on God's side — it does not cease, does not withdraw permanently, and does not fail. On the human side, the chasid type (the devout, chesed-embodying person) is presented as a stable character identity, not a momentary state.
> 
> **The Matt 18:35 parallel (from instruction T5.1 note):** The programme instruction notes Mat 18:35 as the primary reversibility data point for forgiveness. The compassion data does not contain an equivalent direct verse on reversibility. The unforgiving servant parable (Matt 18:27) shows the king's compassion (splanchnizō) producing debt-release, which is then effectively reversed by the servant's own failure to extend compassion. The structural implication: the transformation produced by received compassion can be forfeited if the recipient fails to embody what they have received. This is a significant finding — it places compassion within an integrated moral framework in which reception without corresponding character-formation does not hold.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=734 · finding_id='OBS-023-T2-102' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data supports a reconstruction of the sequence, though it must be assembled from multiple passages rather than being stated in a single verse.
> 
> **In the giver:**
> 
> *Before:* The perceptive openness that allows seeing (T3.1). The eusplanchnos (tender heart) pre-condition (1 Pet 3:8, T2.5). A soul-level character disposition (chesed, ra.chum) that predisposes the person to be moved.
> 
> *During:* The gut-stirring of splanchnizō — the involuntary somatic event at the moment of perceiving need. The heart recoiling (Hos 11:8). The ni.chum warmth kindling. The volitional engagement that follows — the choice to act on or suppress the movement.
> 
> *After:* Outward action (healing, feeding, giving, touching). The eleēmosunē as the social form that sustains compassion-giving beyond the moment. For the character being formed: deepened eusplanchnos — the cycle of compassion-experience reinforcing the tenderness that enables future compassion.
> 
> **In the recipient (partial):**
> 
> *Before:* The pitiable condition (eleeinos) — need that has not yet been met.
> 
> *During:* The compassion-act reaching the person — bodily (Mark 1:41 — touch; Luke 7:14 — touch; Gen 19:16 — taken by the hand).
> 
> *After:* Changed condition (healed, fed, raised, rescued) and/or restored orientation (returned, comforted — Isa 57:18). The inner-being state following reception is largely silent, as established at T4.4.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=735 · finding_id='OBS-023-T2-103' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The sequence reveals three things about how compassion works:
> 
> **Compassion is bottom-up and inside-out.** The sequence in the giver begins in the body (gut-stirring, heart-recoiling) before it engages the soul (character disposition) and the will (choice of action). This confirms the constitutional movement sequence assembled at T2.10: compassion does not begin with a cognitive or volitional determination. It begins with a body-event triggered by perception and moves upward and outward.
> 
> **The before-state is constitutive of the quality of the during-state.** The eusplanchnos (tender heart) pre-condition is not merely a nice-to-have antecedent — it is what allows the somatic stirring to arise naturally and fully. A person without the pre-condition of inner tenderness may still choose to act compassionately (volitionally), but the full splanchnizō movement — the involuntary body-prior arousal — requires the inner constitution to be already oriented toward the other. The quality of the compassion-during depends on the formation of the before-state.
> 
> **The after-state feeds back into the before-state of future compassion.** The experience of giving compassion — being moved, acting, extending — reinforces and deepens the character qualities (eusplanchnos, ra.chum) that constitute the before-state for future encounters. This creates a formative cycle: compassion-experience deepens the inner constitution that enables richer compassion-experience in the future. The character of the compassionate person is not static — it is progressively formed through the experience of being moved and moving toward others.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=736 · finding_id='OBS-023-T2-104' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals that compassion produces change through at least three distinct mechanisms, operating in different directions and at different constitutional levels:
> 
> **Encounter (sudden transformation):** The splanchnizō healing-miracles are sudden transformative encounters — the leper is immediately cleansed (Mark 1:42 — "immediately the leprosy left him"), the blind men's eyes immediately opened (Matt 20:34). The compassion-event produces instantaneous change in condition. This is encounter-mechanism: the sudden meeting of divine compassion with human need produces immediate transformation.
> 
> **Covenantal sustaining (gradual formation):** The chesed vocabulary names a mechanism of gradual constitutional formation through sustained exposure to divine steadfast love. The person who meditates on chesed (Psa 48:9), who returns to God in supplication and receives, who forms the habit of looking to divine compassion as their ground — this person is formed by chesed over time into the chasid type (the devout, chesed-embodying person). This is not encounter-mechanism but sustained-formation: the steady orientation toward divine compassion constitutes the person's character gradually.
> 
> **Participation (transformative solidarity):** The sumpaschō vocabulary (Rom 8:17 — suffering with Christ as the condition of glorification with Christ) names a mechanism of change through participation in Christ's suffering. This is neither sudden encounter nor gradual formation but a participatory identification that transforms the person's eschatological trajectory. The mechanism is ontological solidarity: by suffering-with, the person is joined to Christ's own path through suffering to glory.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=737 · finding_id='OBS-023-T2-105' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data clearly differentiates mechanisms by context:
> 
> **In healing/miracle contexts:** Encounter-mechanism — immediate, condition-changing, externally initiated by divine compassion. The recipient receives; the mechanism operates from outside.
> 
> **In covenantal/Psalm contexts:** Sustaining-formation mechanism — meditative, orientation-forming, building the inner ground of trust and return over time. The person participates actively through contemplation, supplication, and return.
> 
> **In community/epistle contexts:** Participatory-solidarity mechanism — the community's shared suffering and shared compassion (sumpaschō, sumpatheō) forms each member through the experience of genuine mutual engagement. The mechanism is relational and communal rather than individual.
> 
> **In judgment/prophetic contexts:** The judicial withholding of compassion (chus) represents a mechanism of inverse operation — the absence or suspension of compassion as the mechanism of judicial consequence. This is compassion-deprivation as a formative (or de-formative) mechanism: the inner experience of living outside the range of divine compassion is itself a transforming condition.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=738 · finding_id='OBS-023-T2-106' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the relationship between compassion and suffering is one of the most central structural features of the entire registry. Compassion is constitutively oriented toward suffering: the registry description states that compassion "feels the pain of another from the inside — not observing suffering from a distance but being moved by it in the gut." Suffering is the occasion that calls compassion into operation.
> 
> **Compassion as response to suffering:** The splanchnizō pattern is entirely organised around the sight of suffering — crowds harassed and helpless (Matt 9:36), a widow's grief (Luke 7:13), a leper's condition (Mark 1:41), the blind (Matt 20:34). Every splanchnizō event is a compassion-response to perceived suffering. The response is not optional or calculated — it is the inner-body's movement toward what it perceives.
> 
> **Compassion as context for suffering (sumpaschō):** The SYM-PATH vocabulary reverses the direction: the compassionate person enters into the suffering rather than responding from outside it. Rom 8:17 (sumpaschō — suffering with Christ) and 1 Cor 12:26 (suffering together in the body) make suffering the context within which compassion operates as solidarity. Here suffering is not merely the occasion for compassion's response — it is the shared experience that constitutes the compassion-relationship.
> 
> **Compassion as deliberate product of suffering (polusplanchnos in Jas 5:11):** The hapax compound polusplanchnos names God's deep compassion in the specific context of Job's permitted suffering. The pairing of deep compassion and divinely permitted suffering (SD-014) is the data's most complex statement: compassion and suffering are held in tension without resolution — God is deeply compassionate and yet permits the suffering. The suffering does not disprove the compassion; the compassion does not prevent the suffering.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=739 · finding_id='OBS-023-T2-107' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data reveals all four relationships, operating at different levels:
> 
> **Suffering reveals compassion:** Lam 4:10 — the siege reveals the depth of the women's compassion by showing its violation. The compassionate character is revealed precisely at the moment it is overwhelmed. Suffering exposes the inner constitution of the person: what they are capable of, and where their constitutional limits lie.
> 
> **Suffering tests compassion:** Jas 5:11 — Job's endurance in permitted suffering is the test-context for the revelation of God's polusplanchnos. Human patience and divine deep-compassion are held in tension. Suffering tests whether the compassion being claimed is genuine — whether it holds when the cost is sustained.
> 
> **Suffering deepens compassion (sumpatheō/sumpaschō):** Heb 4:15 — Christ sympathises with human weaknesses because he was tempted in the same way. Shared suffering deepens compassion by providing the experiential ground from which genuine fellow-feeling arises. The person who has suffered is constitutionally equipped to be present to suffering in another in a way that the person who has not suffered cannot be. Suffering deepens the compassionate person's capacity for genuine inner solidarity.
> 
> **Suffering produces compassion (implied):** The participatory solidarity vocabulary (sumpaschō) implies that the experience of shared suffering in the community of faith produces a quality of mutual compassion that would not exist without the shared experience of suffering. Persecution and loss (Heb 10:34 — the plundering of property) produce a community of compassionate solidarity forged in shared vulnerability.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=740 · finding_id='OBS-023-T2-108' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data provides evidence that compassion participates in the longer arc of character formation, primarily through the chesed vocabulary and the community-formation pattern.
> 
> **The chasid as the formed-character type:** H2623 chasid (devout/loyal person, 33 XREF occurrences) names the person whose inner life embodies chesed — the constitutive quality of covenantal loyalty and compassion. The chasid is not a person who occasionally feels compassion but one whose character has been formed by it into a stable, defining quality. The existence of this character-type term in the vocabulary confirms that compassion participates in long-arc formation — it can become constitutive of personal identity over time.
> 
> **The community portrait of 1 Pet 3:8:** Sumpathēs (sympathetic), eusplanchnos (tender-hearted), and the associated community virtues are presented as qualities to be cultivated — not merely experienced momentarily. The epistle context implies formation: these are qualities that shape the community's inner life over time through repeated practice and mutual formation.
> 
> **The meditative practice of Psa 48:9:** "We have thought on your steadfast love, O God, in the midst of your temple." Meditation on divine chesed as a sustained inner practice is a formative activity — the sustained turning of the inner being toward God's compassion-character shapes the meditator's inner orientation over time. This is the contemplative-formation dimension of compassion: being shaped by what one contemplates.
> 
> **The mirroring principle as formation:** 2 Sam 22:26 — "with the merciful you show yourself merciful." The sustained experience of divine compassion toward the person forms the person into a corresponding compassionate character. This is formation through encounter repeated over a lifetime: the inner being is constituted by what it consistently receives and reflects.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=741 · finding_id='OBS-023-T2-109' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The evidence positions compassion as playing a dual role in the longer arc of character formation:
> 
> **As the character quality being formed:** The chasid type, the eusplanchnos quality, and the sumpathēs disposition are all end-states of a formative process — what the person is becoming through sustained exposure to divine compassion and through the practice of compassion toward others. Compassion is the target of formation as well as the vehicle.
> 
> **As the motivational ground of formation:** Compassion is also what makes continued engagement with the formative process possible. The Joel 2:13 pattern — "return to the LORD your God, for he is gracious and merciful" — shows that divine compassion is the motivation for the human's sustained engagement with God through repentance and return. The person returns to the formative relationship because God is rachum ve-channum. Compassion is what keeps the relationship alive through failure and return — it is the characteristic that makes the longer arc survivable.
> 
> **Critical observation:** Compassion functions in both directions within the formation arc: it is what the person is being formed into (character target) and what makes formation possible through repeated failure and return (formative context). This bidirectional role makes compassion structurally central to the programme's understanding of sanctification — more so than characteristics that function only as targets of formation.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=742 · finding_id='OBS-023-T2-110' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides partial eschatological evidence, strongest in the sumpaschō/syndoxazō frame and in the polusplanchnos/telos language of Jas 5:11.
> 
> **Rom 8:17 (sumpaschō → syndoxazō):** SD-012 identifies this as the clearest eschatological trajectory in the data. Present fellow-suffering (sumpaschō — a compassion-solidarity act) is oriented toward future shared glorification (syndoxazō). The compassion-solidarity of the present age is moving toward an eschatological fullness in which that solidarity is transformed into shared glory. Compassion as suffering-with is therefore not merely a present-age virtue — it is participation in a trajectory that ends in glorification.
> 
> **Jas 5:11 (polusplanchnos + telos):** The verse explicitly names the "purpose (telos) of the Lord" in the context of God's deep compassion and human endurance. The telos is referenced but not described — it is the intended end toward which the arc of suffering and divine compassion is oriented. The eschatological signal is present but not developed in the data.
> 
> **The everlasting chesed:** Lam 3:22-23 — "his mercies never come to an end; they are new every morning." The perpetual renewal of divine chesed carries an implicit eschatological trajectory: if chesed never ceases and is perpetually renewed, it is oriented toward a fullness that has not yet arrived. The present experience of divine compassion is a foretaste of an inexhaustible reality.
> 
> **What is missing (P):** The data does not contain a verse that explicitly names compassion itself as moving toward an eschatological fullness in the human person — as a characteristic that the person will possess or experience more completely in the age to come. The eschatological orientation is present but underdeveloped for the human person specifically. SD-012 partially addresses this; the question of compassion's eschatological fullness in the human remains an open gap.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=743 · finding_id='OBS-023-T2-111' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> From the available evidence:
> 
> **Present splanchnizō anticipates the fullness of divine compassion enacted without constraint.** The Synoptic compassion-movements operate within the constraints of the present age — limited by what healing can accomplish, by what one meal can provide, by the finitude of the encounter. The eschatological fullness anticipated is a compassion that acts without these constraints — where the gut-stirring of God-in-Christ toward human need finds its complete expression.
> 
> **Present sumpaschō anticipates syndoxazō.** The present experience of suffering-with is incomplete — it is the experience of solidarity in suffering, not yet in glory. The future fullness anticipated is the transformation of the shared suffering into shared glory: compassion-solidarity arriving at its eschatological destination.
> 
> **Present chesed anticipates its own inexhaustibility.** The daily renewal of chesed (Lam 3:23 — "new every morning") anticipates a fullness in which the renewal is no longer needed because the reality is complete and uninterrupted. Present chesed is the foretaste of an inexhaustible compassion-love that requires no renewal because it is permanently full.
> 
> **What is missing (P):** The data does not address what the human person's compassion looks like in its eschatological fullness — whether the human capacity for compassion is itself transformed, expanded, or completed in the age to come. The eschatological anthropology of compassion is a gap for Session D; SD-012 covers the sumpaschō dimension but not the wider question.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=744 · finding_id='OBS-023-T2-112' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T5.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> T2.8 found no direct evidence of a constitutional body deposit but identified two partial signals: the womb etymology as a generational resonance, and the Exod 34:6 generational frame. This prompt is therefore handled as conditional — addressing what can be said given the partial evidence, without affirming a deposit as established.
> 
> **From the womb-etymology signal:** If the RACHAM root's grounding in the womb carries a generational dimension, the developmental consequence implied is that compassion as a constitutive inner quality may be transmitted through the generational threshold of birth — not as a determinate deposit but as a predisposition or constitutional openness formed in the earliest stages of human existence. Groups 1613-001 and 1613-002 name the womb as the space where "divine compassion, calling, and consecration originate before birth" — if compassion is already present as a divine action at this threshold, its developmental consequence may be a prior orientation toward compassion built into the person before conscious formation begins.
> 
> **From the Exod 34:6 generational frame:** The divine compassion-character named in this formula operates across generations in Israel's experience — the chesed that holds through exile, return, and renewal is generationally sustained. The developmental consequence in the community is a transgenerational formation in which each generation receives the chesed-character of God and is thereby constituted as a compassion-formed people.
> 
> **What is missing (P):** Neither signal constitutes direct evidence of a body deposit producing specific developmental consequences in the individual. The question remains partially open and is a genuine gap for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=745 · finding_id='OBS-023-T2-113' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T5.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The most direct evidence of generational consequence in the compassion data is not at the body-deposit level but at the community-covenantal level.
> 
> **Chesed as transgenerational covenantal reality:** The chesed vocabulary operates across Israel's entire covenantal history — from the Exod 34:6 declaration through the Psalter, the prophets, and into the NT (Lam 3:22). Each generation inherits the prior generation's experience of divine chesed and lives within the covenantal framework it establishes. In this sense, chesed produces a generational consequence that is not biological but covenantal-formative: the community shaped by divine chesed across generations develops a shared inner orientation toward compassion as the defining quality of its relationship with God.
> 
> **The chasid as a generational character type:** The devout/loyal person (chasid) is presented in the wisdom and Psalm literature as a recognisable character type — the person whose inner life embodies chesed. The existence of this as a stable, named type across the biblical corpus suggests that chesed-formation produces recognisable generational patterns.
> 
> **What is missing (P):** Biological or body-deposit generational consequence is not established from the data. The generational consequence that is evidenced is covenantal and communal, not individual-genetic. This distinction is important for the programme's constitution framework.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=746 · finding_id='OBS-023-T2-114' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T5.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> T2.8 found no direct body deposit. Partial signals were identified and have been carried through T5.7 as conditional analysis. T5.7 is now formally closed. The generational dimension of compassion is a genuine gap requiring Session D attention, particularly regarding the relationship between the womb-etymology, the RACHAM root's generational resonances, and the covenantal-transgenerational chesed pattern.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=747 · finding_id='OBS-023-T2-115' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The co-occurrence table (Section 5 of the data package) provides definitive quantitative data. The top co-occurrences against R023's OWNER active verses (351 verses):
> 
> | Registry | Word | Shared verses |
> |---|---|---|
> | R103 | love | 196 |
> | R111 | mercy | 76 |
> | R117 | peace | 37 |
> | R059 | faith | 37 |
> | R044 | despair | 28 |
> | R173 | will | 25 |
> | R187 | strength | 24 |
> | R197 | authority | 23 |
> | R156 | surrender | 21 |
> | R121 | praise | 20 |
> | R099 | kindness | 20 |
> | R043 | desire | 19 |
> | R112 | mind | 18 |
> | R182 | Soul | 17 |
> | R034 | covenant | 17 |
> | R073 | guilt | 17 |
> | R051 | distress | 16 |
> | R057 | evil | 16 |
> | R140 | seeking | 15 |
> | R004 | anger | 15 |
> 
> **The most significant co-occurrence by a substantial margin is love (R103 — 196 shared verses).** This is more than twice the count of the next highest (mercy, 76). The love co-occurrence is so dominant that it constitutes more than half of all active OWNER verses (196/351 = 55.8%). This is not incidental clustering — it signals a deep structural connection between compassion and love that the programme must address in Session D (SD-001, SD-005).
> 
> **The mercy co-occurrence (76 shared verses) is the second highest** — consistent with the direct shared vocabulary (XREF terms G1653, G1656, G3628) and the shared anchor verses (Rom 9:15, Jas 5:11, Num 6:25). The compassion-mercy structural boundary is the most urgent distinction question in the programme (SD-009).
> 
> **Unexpected high signals:**
> - Peace (R117 — 37 verses): higher than might be expected given the apparent conceptual distance. SD-025 raises this connection: the co-occurrence (37 verses) suggests a structural relationship between divine compassion and human peace/surrender that warrants investigation.
> - Faith (R059 — 37 verses): SD-022 identifies this: chesed and faith appear together extensively in the Psalter. The structural question is whether faith operates as the receptive capacity by which divine compassion is appropriated.
> - Despair (R044 — 28 verses): compassion and despair co-occurring at 28 verses points toward the structural relationship between distress/need and compassion's operation — compassion is most active where despair is most present.
> - Will (R173 — 25 verses) and Surrender (R156 — 21 verses): SD-025 flags this cluster; the co-occurrence suggests a covenantal-response pattern: divine compassion calls forth human will-engagement and surrender.
> - Anger (R004 — 15 verses): Isa 54:8 anchor verse frames the temporal contrast between anger and chesed/racham. The co-occurrence reflects the structural boundary between compassion and judgment in the divine inner life.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=748 · finding_id='OBS-023-T2-116' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three structural observations emerge from the co-occurrence pattern:
> 
> **Compassion sits at the centre of the love-mercy-kindness cluster (C17).** The three highest co-occurrences — love (196), mercy (76), kindness (20) — are all within-cluster adjacencies. This confirms that compassion is not a peripheral member of C17 but its structural centre of gravity. The dominance of the love co-occurrence (196 verses) raises the question whether compassion and love are truly separable in the programme's data, or whether the vocabulary is naming different aspects of a single phenomenon — a Session D question (SD-001, SD-005, SD-017).
> 
> **Compassion is structurally connected to the human relational and volitional response cluster.** Peace (37), faith (37), will (25), surrender (21), seeking (15) — these are all characteristics naming the human person's inner response to or orientation toward God. Their co-occurrence with compassion reveals a pattern: divine compassion generates a cluster of corresponding inner-being responses in the human person. The co-occurrence pattern maps the structural consequence of divine compassion in human inner life.
> 
> **Compassion is connected to distress and need as its constitutive context.** Despair (28), distress (16), guilt (17), evil (16) — these are the conditions of human inner life that compassion most consistently addresses. Their co-occurrence confirms what the vocabulary already implies: compassion operates most characteristically in the presence of human need, suffering, and moral failure. The co-occurrence landscape positions compassion as the characteristic most directly responsive to the full range of human inner-being distress.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=749 · finding_id='OBS-023-T2-117' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data reveals several sequential relationships, differentiated by direction and vocabulary:
> 
> **Compassion precedes mercy (as inner movement precedes relational act):** SD-010 and SD-016 both point toward a sequence within the compassion-mercy relationship. Luke 10:33-37 is the clearest instance: splanchnizō (compassion-movement, v.33) precedes and generates the eleos-act (mercy — the verb "go and do likewise" responding to "who showed mercy?" in v.37). The inward compassion-movement produces the outward mercy-act. This is not simultaneity — compassion is the prior event that generates mercy as its expression.
> 
> **Compassion precedes action consistently (splanchnizō pattern):** In every Synoptic use, splanchnizō precedes the action. The sequence is invariant: perceive → be moved → act. Compassion occupies the middle position in the action-sequence: it follows perception and precedes agency. This is the constitutional movement sequence assembled at T2.10 — compassion is the inner event that converts perception into action.
> 
> **Repentance follows divine compassion as its ground (Joel 2:13; Jon 4:2):** The divine compassion-character (rachum ve-channum) is cited as the reason and ground for human repentance. The sequence here runs: divine compassion is announced → human repentance is called for and enabled → return to God follows. Divine compassion is not the consequence of repentance — it is its precondition and ground.
> 
> **Suffering accompanies or precedes compassion as its occasion:** The co-occurrence of despair (28), distress (16), and guilt (17) with compassion, alongside the consistent suffering-trigger of splanchnizō, establishes suffering as the chronological antecedent of compassion's operation. Compassion follows perceived suffering; it does not precede it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=750 · finding_id='OBS-023-T2-118' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The sequential relationships are predominantly causal rather than merely correlational:
> 
> **Compassion → mercy:** Causal. The inward movement (splanchnizō) produces the outward act (eleos). This is a constitutional cause-and-effect: the inner event generates the outer expression. SD-016 proposes this as the three-stage model (visceral stirring → mercy orientation → concrete act), which is a causal developmental sequence.
> 
> **Divine compassion → human repentance:** Causal-enabling. Divine compassion does not mechanically produce repentance — it creates the inner environment in which repentance becomes possible. Joel 2:13 names the compassion as the reason for the call to repent; it is the enabling cause rather than the efficient cause. The human will remains engaged.
> 
> **Suffering → compassion:** Causal at the perceptive level. The sight of suffering triggers the compassion-movement. This is the most direct causal relationship in the data: perceived suffering causes splanchnizō. However, the cause is not sufficient without the pre-conditions (eusplanchnos, perceptive openness) — the same suffering does not produce compassion in all observers (the priest and Levite in Luke 10).
> 
> **Compassion → praise (R121 — 20 co-occurrence):** Likely correlational rather than directly causal. Praise and compassion appear in the same covenantal and Psalmic contexts (chesed frequently paired with praise in the Psalter) but the sequential relationship is not established from the data. This co-occurrence belongs in Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=751 · finding_id='OBS-023-T2-119' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data evidences multiple produced characteristics:
> 
> **Compassion produces mercy (eleos/eleēmosunē):** The clearest causal relationship in the data. SD-016 names this explicitly: the three-stage sequence (visceral stirring → mercy disposition → concrete act of giving) makes mercy the produced characteristic of compassion. Luke 10:33-37 is the paradigm verse. Mechanism: constitutional movement from somatic event through soul-level disposition to outward relational act.
> 
> **Compassion produces action and agency:** As established at T3.7, compassion is constitutively action-generating. Every splanchnizō event produces a specific act. The mechanism is volitional: compassion engages the will and produces directed agency toward the suffering other.
> 
> **Compassion produces comfort (ni.chum → comforting):** Hos 11:8 and Isa 57:18 both show the ni.chum warmth of compassion producing the act of comfort. Compassion in this register is the inner movement that motivates and constitutes the comforting act. Mechanism: the affective warmth of compassion generates the speech and presence of comfort.
> 
> **Compassion produces solidarity (sumpaschō → community):** The SYM-PATH vocabulary shows that compassion-solidarity produces the community reality of mutual suffering and mutual rejoicing (1 Cor 12:26). The mechanism is participatory: genuine entry into another's experience constitutes a solidarity that shapes the community's inner life.
> 
> **Compassion enables repentance as its ground:** Joel 2:13 and Jon 4:2 show divine compassion enabling human repentance. The mechanism is enabling-causal: divine compassion creates the safe inner environment within which the human person can risk the exposure of heart-rending return.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=752 · finding_id='OBS-023-T2-120' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides partial evidence of what produces compassion:
> 
> **Suffering produces compassion (situational cause):** The consistent perceptive trigger of splanchnizō — sight of suffering — establishes suffering/need as the situational cause of compassion-arousal. The characteristic is produced, event by event, by encounter with perceived suffering.
> 
> **Divine chesed produces human chesed (mirroring principle):** 2 Sam 22:26 — "with the merciful you show yourself merciful" — and the structural logic of the chasid type establish that sustained divine compassion produces corresponding human compassionate character. The mechanism is formative: sustained reception of divine chesed forms the human person into a chesed-bearing person (the chasid type).
> 
> **Shared suffering produces sumpatheō/sumpaschō:** Heb 4:15 — Christ's sympathy produced by his own experience of temptation. Heb 10:34 — community compassion forged in shared persecution. Experience of the same inner condition produces the capacity for genuine fellow-feeling.
> 
> **What is missing (P):** The data does not fully address whether a distinct inner-being characteristic (other than suffering and divine chesed) produces compassion — whether, for example, humility, or love, or faith is a necessary antecedent. The mirroring principle implies that received compassion produces given compassion, but the full causal chain is not established. This is a gap for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=753 · finding_id='OBS-023-T2-121' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T6.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data provides clear evidence on both sides:
> 
> **Compassion as a constituent element of love (R103):** The dominant co-occurrence signal (196 shared verses with love) and the shared RACHAM root (SD-001) indicate that compassion is at minimum a constituent element of the love vocabulary in the programme. The RACHAM root underlies both love (Reg 103) and compassion (Reg 23). The question raised by SD-001 and SD-005 is whether compassion is a constituent of love (one form that love takes when directed toward suffering) or whether they are genuinely distinct characteristics at the same constitutional level. This is the programme's most urgent constitutive boundary question for this registry.
> 
> **Compassion as a constituent of the chesed cluster:** The chesed vocabulary (H2617A — XREF in love and kindness registries; H2617B — OWNER in compassion registry carrying the shame/negative pole) demonstrates that compassion participates in the chesed semantic field that also constitutes love (R103) and kindness (R099). Compassion is constitutively embedded within the chesed cluster — it is not separable from it at the root level.
> 
> **Mercy as a constituent of compassion:** The three-stage SD-016 model (stirring → mercy disposition → act) positions mercy as a stage within compassion's operation rather than as a distinct parallel characteristic. If this model holds, mercy is a constituent element of compassion — its soul-level dispositional form — rather than a separate characteristic that compassion produces. This is a critical question for the programme that SD-009 defers to Session D.
> 
> **What does not constitute part of compassion:** The judicial-prohibition vocabulary (chus — "your eye shall not pity") reveals that hardness of judicial will is definitionally outside the constitutive structure of compassion. It is the active exclusion of compassion's constituent elements, not a form of them.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=754 · finding_id='OBS-023-T2-122' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the registry header confirms: shared_term_count = 56, term_sharing_ratio = 0.577. Of the 97 total terms, 56 (57.7%) are shared with other registries. This is a very high sharing ratio, reflecting the structural position of compassion within a dense cluster of adjacent characteristics.
> 
> Key XREF terms (shared vocabulary carried in other registries as OWNER):
> - G1653 eleeō / G1656 eleos / G3628 oiktirmos — mercy (R111)
> - H2617A chesed — love/kindness (R103/R099)
> - H2603A chanan — grace (R68)
> - H2623 chasid — devotion/loyalty (R46/R104)
> - H7349 rachum / H7355 racham / H7356B rachamim — also in love (R103)
> - H5162G/H nacham — comfort (R192)
> - H8467 techinah / H8469 tahanun — prayer/supplication (R212/R122)
> 
> The breadth of vocabulary sharing confirms that compassion occupies a structurally central position in the programme — its vocabulary reaches across multiple clusters including C17 (love, mercy, kindness), C14 (will, surrender), prayer/supplication registries, and the comfort cluster.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=755 · finding_id='OBS-023-T2-123' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data identifies three root families that cross registry boundaries at root level (from Pass 2 and the XREF analysis):
> 
> **RACHAM root:** H7356A ra.cham (womb/compassion, OWNER in R23) and H7356B ra.cha.mim (compassion, XREF in R23) share the same root as the love vocabulary in R103. SD-001 raises: does the womb-root function as a unifying somatic image across both compassion and love, or does it serve different semantic purposes in each? The root-level connection is structural: the same root generates both the compassion vocabulary and a significant portion of the love vocabulary.
> 
> **CHASAD root:** H2616A cha.sad (be kind, OWNER in R23) and H2617B chesed/shame (OWNER in R23) share the CHASAD root with H2616B cha.sad (to shame, OWNER in R146) and H2617A chesed (kindness, XREF in R23/R99/R104). This root crosses two clusters — C17 (compassion, love, kindness) and the shame cluster (C06 or equivalent). SD-008 raises the most theologically acute question: does the root-level connection between chesed and shame reflect a genuine semantic relationship — covenantal violation producing shame as its consequence — or is this purely lexicographic?
> 
> **ATAR root:** The data notes a shared root between mercy (R111) and compassion (R23) through the ATAR vocabulary (Pass 2 root families table). Both remain within C17.
> 
> **CHIN/CHEN root collision:** The data notes a Stage 1 flag on the root collision between channum (graciousness, OWNER in R23) and chen (favour/grace, XREF in R23, OWNER in R68). The shared root raises the SD-006 boundary question between graciousness (character quality) and grace (relational gift).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=756 · finding_id='OBS-023-T2-124' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T6.4'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three insights emerge from the vocabulary-sharing pattern:
> 
> **High sharing ratio (57.7%) reveals structural embeddedness rather than lexical uniqueness.** Compassion does not have a sharply bounded vocabulary that distinguishes it cleanly from adjacent characteristics. Its vocabulary is deeply interwoven with love, mercy, grace, kindness, and comfort. This is not a weakness in the programme's categorisation — it reflects the data's genuine structure. Compassion in Scripture is not a lexically isolated phenomenon; it is constitutively embedded in a cluster of adjacent characteristics that share its deepest roots.
> 
> **Root-level sharing (RACHAM, CHASAD, CHIN/CHEN) reveals conceptual relationships at a deeper level than lexical sharing.** These shared roots suggest not merely that compassion and love sometimes use the same words, but that they draw on the same foundational anthropological realities — the womb, the covenant bond, the disposition of favour. The conceptual relationship is not one of overlap between distinct categories but of shared constitutional ground.
> 
> **The CHASAD root crossing two clusters (compassion/love and shame) is the most structurally significant finding.** The same root family names both covenantal loyalty-love and shame/exposure. SD-008 identifies this as a programme-level question: if the depth of mercy presupposes the depth of shame (the root family spans both), then the inner-being connection between compassion and shame is structural rather than incidental. This has implications for how the programme understands the relationship between compassion and the conditions of moral failure it most consistently addresses.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=757 · finding_id='OBS-023-T2-125' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data identifies mercy (R111) as the most closely resembling adjacent characteristic, based on:
> - Direct XREF relationship (G1653, G1656, G3628 as XREF terms in R23)
> - Shared anchor verses (Rom 9:15, Jas 5:11, Num 6:25)
> - Co-occurrence of 76 shared verses
> - SD-009 naming this as the most direct test of whether R23 and R111 are genuinely separable
> 
> **What the data suggests about the distinction (partial):** SD-016's three-stage model implies a directional distinction: compassion is the inner somatic-movement (splanchnizō), mercy is the soul-level dispositional form (eleos), and almsgiving (eleēmosunē) is the external act. On this model, compassion and mercy are not parallel alternatives but sequential stages — compassion precedes and generates mercy. If this is correct, the distinction is one of constitutional level and sequence rather than of kind.
> 
> However, SD-009 raises the specific counter-evidence of Rom 9:15, where oikteirō (compassion) and eleeō (mercy) are deployed in parallel — suggesting they may be synonymous in that context. The parallel structure does not resolve whether the terms are truly interchangeable or whether the parallelism is rhetorical.
> 
> **What is missing (P):** The precise inner-being boundary between compassion and mercy is not established in the current data and is explicitly deferred to Session D (SD-009). This is the most critical unresolved distinction question in the registry.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=758 · finding_id='OBS-023-T2-126' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three apparent overlaps are identified in the data, with their current boundary status:
> 
> **Compassion / mercy (R111):** The boundary is unresolved. Partial evidence suggests a sequential model (compassion generates mercy) but Rom 9:15 parallel usage challenges this. Deferred to Session D (SD-009).
> 
> **Compassion / love (R103):** The boundary is the programme's most structurally significant open question. The 196-verse co-occurrence and the RACHAM root-sharing make the boundary between compassion and love the most urgent distinction work in C17. SD-001, SD-005, and SD-017 all approach this question from different angles without closing it. The distinction, if it holds, may be: love is the constitutive relational disposition toward the other; compassion is the specific form love takes when the other is suffering. But this is inference from the data, not a finding.
> 
> **Compassion / grace (R68):** The CHIN/CHEN root collision (SD-006) raises the boundary between channum (gracious character) and chen (grace as relational gift). The inner-being boundary: is graciousness (channum) a character quality that produces grace (chen), or are they two names for the same inner reality in different registers? Deferred to Session D.
> 
> **What is missing (P):** All three critical boundaries are Session D targets. None is established in the current data. These are the most significant structural gaps in T6.5.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=759 · finding_id='OBS-023-T2-127' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T6.5'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> From the partial evidence available:
> 
> **Compassion vs mercy — potentially constitutional level:** If the SD-016 three-stage model holds, the distinction is one of constitutional level (somatic event vs soul-level disposition) rather than of kind or degree. This would make compassion and mercy two stages in a single constitutional movement rather than two alternative expressions of the same inner quality. This is the most analytically productive hypothesis from the data but is not confirmed.
> 
> **Compassion vs love — potentially directional:** The data implies that love is the wider relational disposition and compassion is love directed specifically toward suffering. If so, the distinction is directional: the same inner quality oriented differently. But the RACHAM root-sharing makes this uncertain — the same vocabulary roots carry both concepts.
> 
> **Compassion vs grace — potentially directional:** Channum (gracious character) moves toward those who need favour; chen (grace) is the favour extended. The distinction may be directional (the inner character vs the relational act), similar to the compassion/mercy question.
> 
> **What is missing (P):** The precise nature of the distinction — degree, kind, direction, or constitutional level — cannot be determined from the current data for any of the three critical boundary pairs. All three require Session D synthesis across the full vocabulary of the adjacent registries. These are not new gaps — they are all captured in existing SD pointers.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=760 · finding_id='OBS-023-T2-128' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the shared anchor verse table (Section 6 of the data package) is definitive and is used directly:
> 
> | Reference | Also anchored in |
> |---|---|
> | Exo 33:19 | love (R103) |
> | Exo 34:6 | anger (R4); patience (R116); love (R103); faith (R59); calling (R19) |
> | Num 6:25 | mercy (R111) |
> | Psa 4:1 | anguish (R5) |
> | Psa 89:14 | justice (R98) |
> | Lam 3:22 | love (R103); longing (R102) |
> | Hos 6:6 | love (R103); knowledge (R100) |
> | Hos 11:8 | faithfulness (R60); perverseness (R120); sorrow (R151) |
> | Mic 6:8 | love (R103); goodness (R67); kindness (R99); will (R173); humility (R80); condemnation (R24) |
> | Mat 9:36 | distress (R51); listen (R213) |
> | Rom 9:15 | mercy (R111) |
> | Jam 5:11 | mercy (R111) |
> | 1Pe 3:8 | love (R103); mind (R112) |
> | Rev 3:17 | vulnerability (R206) |
> 
> **Total: 14 shared anchor verses across 16 distinct registries.**

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=761 · finding_id='OBS-023-T2-129' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.6'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Several analytically significant shared-anchor relationships emerge:
> 
> **Exo 34:6 (shared with anger R4, patience R116, love R103, faith R59, calling R19):** This is the programme's most anchored single verse. Its five-registry membership confirms SD-017's observation that Exod 34:6 functions as a unified theological statement about God's inner character that multiple registries access from different angles. The shared anchoring reveals that compassion, anger, patience, love, faith, and calling are not independent characteristics but aspects of a single divine inner-being reality disclosed in this formula. Session D must decide whether to treat Exod 34:6 as a cluster-level synthesis anchor rather than as a property of individual registries.
> 
> **Hos 11:8 (shared with faithfulness R60, perverseness R120, sorrow R151):** The shared anchoring with faithfulness (R60) reveals that the divine inner deliberation in Hos 11:8 is not only about compassion — it is also a statement about God's faithfulness to covenant despite Israel's perverseness. The triple anchoring shows that compassion, faithfulness, perverseness, and sorrow are simultaneously present in a single divine inner-being moment. This is the richest anchor verse for Session D cluster synthesis.
> 
> **Mic 6:8 (shared with love R103, goodness R67, kindness R99, will R173, humility R80, condemnation R24):** Six registries share this anchor — the most clustered single verse after Exod 34:6. The verse integrates justice, chesed (compassion/kindness), and humility as three co-equal requirements. The shared anchoring reveals that compassion (chesed) is constitutively linked to justice and humility in the programme's moral anthropology — it cannot be understood in isolation from either.
> 
> **Mat 9:36 (shared with distress R51, listen R213):** The Synoptic splanchnizō anchor is shared with distress and listening. The connection to listening (R213 — a recently added registry) is particularly notable: Jesus sees the crowds and is moved — the compassion-movement follows perceiving-and-hearing. Compassion and listening may be constitutively linked in a way the programme has not yet fully explored.
> 
> **Rev 3:17 (shared with vulnerability R206):** The shared anchoring with vulnerability confirms the structural connection between compassion and vulnerability identified at T1.7: the pitiable condition (eleeinos) is also a condition of vulnerability. Compassion and vulnerability share the same anchor because they are constitutively related — compassion is most directly addressed to the condition of vulnerability.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=762 · finding_id='OBS-023-T2-130' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T6.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The registry header shows dimensions: None — the dimension field has not been populated in the database record. From the T1.8 analysis in this document, the dimensions assembled from the data are:
> 
> - Primary: Relational Disposition
> - Secondary: Emotion — Positive, Agency / Power, Vitality / Existence
> 
> These are analytical conclusions from this second-tier analysis, not database-confirmed entries. Without confirmed dimension data for the adjacent registries, the formal dimensional sharing count cannot be established.
> 
> **What can be inferred from available data:** Relational Disposition is the primary dimension of multiple C17 registries (love, mercy, kindness) — dimensional sharing with these registries at the primary level is highly probable. Emotion — Positive is likely shared with love (R103) and several other C17 members. Whether Agency / Power is shared with mercy (R111 — which also produces action) is unresolved without R111's dimension data.
> 
> **What is missing (P):** Formal dimensional sharing data is not available at this stage of the programme. The answer will be available once Session B DataPrep and dimension assignment are complete across the adjacent registries. This is a programme-stage gap rather than a data gap.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=763 · finding_id='OBS-023-T2-131' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T6.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Without confirmed dimension data, the pattern cannot be formally stated. From the assembled analysis:
> 
> **If primary Relational Disposition is shared with love, mercy, and kindness (highly probable):** The dimensional sharing would confirm that compassion, love, mercy, and kindness are all expressions of the same primary constitutional orientation — toward the other in relationship. The distinction between them would then need to operate at a sub-dimensional level — the specific form, constitutional location, or directional quality of the relational disposition, rather than the dimension itself.
> 
> **If Emotion — Positive is shared across C17:** The secondary dimensional sharing would confirm that the entire C17 cluster is characterised by a positive affective quality — all of its members involve a felt inner movement toward rather than away from the other.
> 
> **What is missing (P):** This analysis must await confirmed dimension data. The pattern will be a significant Session B and D finding.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=764 · finding_id='OBS-023-T2-132' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T6.7'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Dimensional sharing data is not yet available in the programme database (dimensions field = None). The analysis above represents inferences from the second-tier analysis findings rather than from confirmed database entries. This is noted explicitly. The question is properly a Session B DataPrep output that will be available for Session D synthesis.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=765 · finding_id='OBS-023-T2-133' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The primary terms and their root meanings, drawn from the term inventory and Pass 1 sense analyses:
> 
> **Hebrew primary terms:**
> 
> - **H7355 ra.cham / H7356B ra.cha.mim** (XREF, 43/39 occurrences): verbal and plural noun forms from the RACHAM root. Root meaning: the womb (re.chem, H7358). Compassion named from the body's most interior generative space. The plural form (ra.cha.mim) signals a multiple, accumulated, inexhaustible quality — grammatically plural in the most common form.
> 
> - **H7349 ra.chum** (XREF, 13 occurrences): adjectival form — "compassionate" as character quality. Used almost exclusively as a divine epithet in the Exod 34:6 formula.
> 
> - **H2347 chus** (OWNER, 24 active occurrences): verbal — "to pity, spare." Root connection to darkened (H2345 chum) through phonological similarity rather than semantic affinity. Appears predominantly in judicial-prohibition contexts.
> 
> - **H2617B chesed / H2616A chasad** (OWNER, 169/2 occurrences): steadfast love / be kind. Root: CHASAD — spanning covenantal loyalty and shame/disgrace. The most theologically weighted vocabulary in the OT; foundational to covenantal relationship.
> 
> - **H2587 channum** (OWNER, 13 occurrences): gracious — adjective from the CHANAN root (favour/grace). Divine epithet in Exod 34:6 paired with rachum.
> 
> **Greek primary terms:**
> 
> - **G4697 splanchnizō** (OWNER, 12 active occurrences): verbal — "to be moved with compassion." Root: splanchnon (G4698, entrails/affections). The gut-movement verb — the most precise single term for compassion as inner somatic event in the NT.
> 
> - **G4698 splanchnon** (XREF, 11 occurrences): noun — entrails/affections/compassion. The anatomical root of the splanchnizō family.
> 
> - **G4184 polusplanchnos** (OWNER, 1 occurrence): compound hapax — "very/deeply compassionate" (polus + splanchnon). Coined for Jas 5:11 to name divine compassion beyond the range of existing vocabulary.
> 
> - **G4834/4835 sumpatheō/sumpathēs** (OWNER, 2/1 occurrences): verbal and adjectival — "to sympathise / sympathetic." Root: sum (with) + pathos (suffering/experience). Names compassion as participatory solidarity — suffering-with.
> 
> **Root meanings summary:** Both primary root families (RACHAM/womb; SPLANCHN/entrails) ground compassion in the body's interior. Both move from concrete anatomical reality to abstract inner-being concept. The convergence of two independent linguistic traditions on the same anatomical grounding is the defining lexical feature of this characteristic.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=766 · finding_id='OBS-023-T2-134' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The vocabulary covers the full grammatical range, and each grammatical form reveals a distinct operational mode:
> 
> **Verbal forms (ra.cham, splanchnizō, sumpatheō, sumpaschō, chus):** Name compassion as an event — something that happens. The verb form captures the moment of inner movement, the act of being moved, the event of gut-stirring. Compassion as verb is compassion in its most dynamic and event-specific form.
> 
> **Noun forms (ra.cha.mim, splanchnon, chesed, eleēmosunē, ni.chum):** Name compassion as a reality, a substance, a quality that exists and can be quantified, accumulated, or given. The plural noun (ra.cha.mim — compassions/mercies) is particularly revealing: it names compassion as multiple and inexhaustible rather than singular and bounded. Chesed as noun names it as a relational substance — something that holds and can be appealed to.
> 
> **Adjectival forms (ra.chum, ra.cha.ma.ni, channum, sumpathēs, eusplanchnos):** Name compassion as a character quality — what kind of person one is. The adjective form is the most constitutional: it describes the inner being rather than an act or a reality. Ra.chum (compassionate) and sumpathēs (sympathetic) name the person whose inner being is constituted by this quality.
> 
> **Compound forms (polusplanchnos, sumpatheō, sumpaschō, eusplanchnos):** Name compassion in its intensified, combined, or modified expressions. Compounds reveal: the characteristic can be intensified (polusplanchnos — deeply compassionate); it can be combined with participation (sumpaschō — suffering-with); it can be grounded in inner constitution (eusplanchnos — of good/tender entrails).
> 
> **What the range reveals:** Compassion is a constitutional quality (adjective), an inner event (verb), an existing reality (noun), and an intensifiable experience (compound). The full grammatical range confirms that compassion is not reducible to any single operational mode — it is simultaneously a character disposition, an event-movement, a relational substance, and a constitutional quality.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=767 · finding_id='OBS-023-T2-135' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The SEMANTIC_RANGE_BREADTH flag is raised for the primary active term G4697 splanchnizō. Pass 1 identifies four semantic domains for splanchnizō:
> 
> 1. Compassion toward physical suffering or need — healing miracles (Matt 20:34; Mark 1:41; Luke 7:13)
> 2. Compassion toward spiritual destitution — "sheep without a shepherd" (Matt 9:36; Mark 6:34)
> 3. Compassion toward physical hunger — crowds without food (Matt 15:32; Mark 8:2)
> 4. Compassion in relational/moral context — parable of prodigal (Luke 15:20), unforgiving servant (Matt 18:27), Good Samaritan (Luke 10:33)
> 
> The four-domain breadth of splanchnizō across physical, spiritual, material, and relational-moral contexts is the primary semantic range evidence. The flag is confirmed fully warranted (Pass 1).
> 
> For the chesed vocabulary, the semantic range spans: divine constitutive character (Exod 34:6), covenant loyalty (sustained through time and violation), steadfast love (Lam 3:22 — inexhaustible), human character quality (Prov 19:22; Hos 6:6; Mic 6:8), and covenantal faithfulness (2 Sam 22:26). The chesed range is wider than any single English term can capture — hence the programme retaining it under "compassion" alongside "kindness" (R99) and "love" (R103) in multiple registries.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=768 · finding_id='OBS-023-T2-136' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '4'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the vocabulary makes all three distinctions explicitly:
> 
> **Disposition vs act:** Ra.chum / channum / sumpathēs (adjectival — disposition) vs ra.cham / splanchnizō / sumpatheō (verbal — act). The adjectival terms name what the person is; the verbal terms name what the person does or what happens within them. The vocabulary holds both and distinguishes them grammatically.
> 
> **Received vs given:** The supplication vocabulary (techinah, tahanun — terms for seeking/receiving compassion) vs the splanchnizō/chesed vocabulary (terms for extending/giving compassion). These are distinct vocabulary families with distinct grammatical positions: the supplication terms name the human act of receiving-oriented appeal; the character terms name the giver's inner state.
> 
> **Condition vs quality:** G1652 eleeinos (pitiful — the condition of the one who needs compassion) vs G4835 sumpathēs / H7349 rachum (sympathetic/compassionate — the quality of the one who gives it). The vocabulary explicitly names both the condition that calls for compassion and the quality that responds to it, which is unusual in the programme data. Most characteristics name only the quality, not the condition of its proper object.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=769 · finding_id='OBS-023-T2-137' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '5'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the vocabulary includes multiple terms for the opposite or absence, operating at different levels:
> 
> **The judicial-prohibition vocabulary (chus in negative):** "Your eye shall not pity (chus)" is the most direct verbal naming of compassion's absence — or more precisely, its deliberate suppression. This is not merely the absence of compassion but the active overriding of it.
> 
> **H2617B chesed as shame (negative semantic pole):** The CHASAD root includes H2617B as the negative pole — shame/disgrace. The same root that names steadfast love also names the condition that is its opposite: relational exposure and violation. This is the most structurally interesting "opposite" term in the data — it is embedded within the compassion vocabulary itself, not in a separate antonym.
> 
> **G1652 eleeinos (pitiable — condition requiring compassion):** This names not the opposite of compassion but the state that exists in its absence — the pitiable condition of the person who has not received compassion. It is the absence-marker on the receiving side rather than the giving side.
> 
> **Implied hardness:** The judicial-prohibition contexts imply a named absence on the character side — the hard heart, the closed eye. While not a single term, the phrase "your eye shall not pity" functions as the inverse character statement: the person who does not pity, whose eye is closed to need.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=770 · finding_id='OBS-023-T2-138' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '6'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the data contains multiple person-type terms:
> 
> **H2623 chasid** (XREF, 33 occurrences): "devout/pious/loyal person" — the one whose inner life is constituted by chesed. The chasid is the person-type whose character is defined by covenantal compassion-loyalty. This is the most developed person-type term in the vocabulary.
> 
> **H7349 rachum** (XREF, 13 occurrences): as a divine epithet, this names God as the paradigmatic compassionate person-type. When applied to humans, it names the one who is constitutively compassionate.
> 
> **H7362 ra.cha.ma.ni** (OWNER, 1 occurrence, Lam 4:10): adjectival — "compassionate (women)." Names the person-type by character quality. Used at the moment of its catastrophic violation — which reveals that the term was understood as a stable character-type identifier.
> 
> **G4835 sumpathēs** (OWNER, 1 occurrence, 1 Pet 3:8): "sympathetic" as a character quality of the community member. The person who is sumpathēs is constitutively open to the inner experience of others.
> 
> **G3356 metriopatheō context (Heb 5:2):** The high priest who "deals gently" is implicitly named as a person-type: the one who exercises calibrated, wise compassion arising from shared vulnerability.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=771 · finding_id='OBS-023-T2-139' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '7'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — the supplication vocabulary is a substantive and structurally significant XREF set in the data:
> 
> **H8467 techinah** (XREF, 24 occurrences): "supplication/plea for favour" — the earnest appeal for divine compassion and grace. Derived from the CHANAN root.
> 
> **H8469 tahanun** (XREF, 18 occurrences): "entreaty/supplication" — closely related; names the act of earnest pleading for divine mercy.
> 
> **H2603A chanan** (XREF, 72 occurrences): "be gracious" — the verbal form often rendered "have mercy" in contexts of prayer. The imperative form (chonneni — "be gracious to me") is the prayer-appeal for divine compassion.
> 
> **H5165 nech.amah / H5164 no.cham** (XREF, 2/1 occurrences): seeking comfort/compassion from God in the context of grief.
> 
> The supplication vocabulary establishes that compassion has a well-developed seeking-language — the human person's acts of appeal to God for compassion are named and differentiated in the vocabulary. This is not merely incidental: the existence of a supplication sub-vocabulary confirms that compassion is understood as something that can be sought, approached, and appealed for — it is not merely received passively but actively sought in earnest petition.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=772 · finding_id='OBS-023-T2-140' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '8'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The data package shows NO_WORD_ANALYSIS flag for 98 terms — indicating that detailed lexical analysis (including LXX usage) has not been completed for the majority of the vocabulary. The flag count of 98 out of 97 total terms (more than the term count, suggesting some flags apply at the group level) indicates a significant lexical analysis gap across the registry.
> 
> **What the data does provide (partial):** Pass 1 includes brief observations on LXX-related terminology for specific terms:
> 
> - G4697 splanchnizō: "the verb appears in LXX and NT" (LSJ note, term 13 analysis). The term's presence in the LXX indicates continuity of the somatic-compassion vocabulary across the Testaments.
> - G1654 eleēmosunē: Pass 1 term 20 traces the semantic development "classical Greek pity/mercy → LXX almsgiving/charitable giving → NT acts of generosity." This is the most developed cross-Testament lexical trajectory in the data — compassion arriving at its normative social form through the LXX period.
> - G3356 metriopatheō: drawn from Stoic philosophical tradition; the LXX does not appear to be the primary carrier of this term's background.
> 
> **What is missing (P):** The systematic LXX analysis for the RACHAM and CHESED vocabulary — how ra.cham and chesed were rendered in the LXX (primarily as eleos/oiktirmos) and what that translation choice reveals about cross-Testament conceptual development — is not present in the data. The NO_WORD_ANALYSIS flag is the indicator. This is a substantial lexical gap; no SD pointer captures it directly.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=773 · finding_id='OBS-023-T2-141' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '9'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Yes — G4184 polusplanchnos (Jas 5:11) is a NT hapax legomenon — a term coined (or first attested in the NT) for this specific expression of divine compassion. Pass 1 term 18 analysis addresses this directly:
> 
> "The use of a compound hapax for this single statement signals that the writer needed a stronger term than the existing vocabulary supplied. Polusplanchnos — intensely, deeply compassionate — is coined for the moment when God's compassion needs to be named as something beyond the ordinary range of the word."
> 
> **What the coinage reveals:**
> 
> The coinage of polusplanchnos reveals two things:
> 
> **1. The existing vocabulary was insufficient for the theological claim being made.** The splanchnizō/splanchnon vocabulary was already in use; polusplanchnos intensifies it beyond its standard range. This signals that the compassion vocabulary was experiencing conceptual pressure — the claim about God's deep compassion in the context of Job's suffering required a stronger term than existed. The coinage is a lexical signal that the theological content was exceeding the available vocabulary.
> 
> **2. The coinage occurs at the point of maximum theological tension.** Jas 5:11 holds deep divine compassion (polusplanchnos) in direct proximity to divinely permitted suffering (Job's endurance). The new word is coined precisely for the moment where compassion and suffering are most acutely in tension. The term's uniqueness signals that this tension is not resolved in the existing vocabulary — a new word is required to hold both simultaneously. This is SD-014's finding: the most theologically complex and unresolved statement in the compassion data is the one that required a new word.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=774 · finding_id='OBS-023-T2-142' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '10'  ·  Segment: 'T7.1'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The full vocabulary arc — from the most intimate to the most structural expression — reveals a characteristic with extraordinary semantic breadth and constitutional depth:
> 
> **Most intimate (RACHAM/womb):** Compassion begins at the body's most interior space — the womb. The most intimate possible human experience — carrying life from within — is the etymological ground of the most fundamental compassion vocabulary. Compassion at its most intimate is a pre-conscious, pre-volitional, body-constituted reality.
> 
> **Somatic-movement layer (splanchnizō/ni.chum):** Moving outward from the etymological ground, compassion is named as a felt body-event — the gut-stirring, the warmth-kindling. This is compassion as inner experience at the level of felt somatic reality.
> 
> **Character-disposition layer (chesed/channum/rachum/sumpathēs):** At the soul level, compassion is named as a settled constitutional quality — what kind of person one is. The character-adjective vocabulary names this layer.
> 
> **Relational-responsive layer (chus/chem.lah/oikteirō):** Compassion as the responsive movement toward the one who is in need — the pity-impulse that moves to spare, help, and protect.
> 
> **Participatory-solidarity layer (sumpatheō/sumpaschō):** Compassion as genuine entry into another's inner experience — suffering-with, not merely sympathising-from-outside. This is compassion at the level of interpersonal constitutional connection.
> 
> **Social-institutional layer (eleēmosunē):** Compassion arriving at its normalised social form — almsgiving. The most structural and institutionalised expression: compassion has produced a social practice that embodies it across communities and cultures.
> 
> **The full arc:** From womb to almsgiving, from pre-conscious body-reality to institutionalised social practice, the compassion vocabulary spans the complete range of human inner-being and outer expression. No other characteristic in the programme data traverses this complete arc with equivalent lexical clarity.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=775 · finding_id='OBS-023-T2-143' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T7.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The primary active term is G4697 splanchnizō, and the primary anchor verse selected for this analysis is Matt 9:36: "When he saw the crowds, he had compassion for them (splanchnizō), because they were harassed and helpless, like sheep without a shepherd."
> 
> **Grammatical function:** Splanchnizō is the main verb of the clause — it is the central action of the sentence. Jesus saw (aorist participle — prior action); he was moved with compassion (aorist indicative — the main event); the following clause (Matt 9:37-38 — the harvest/prayer saying) and context (Matt 10:1 — the commissioning of the twelve) are the consequences. The compassion-verb is the structural hinge of the pericope: it is the inner event that explains and generates everything that follows.
> 
> **Argumentative function:** The verse functions as an explanation and motivation for both the harvest teaching (Matt 9:37-38) and the mission commissioning (Matt 10:1). The argument structure is: Jesus saw the condition of the crowds → was moved with compassion → declared the harvest great and the labourers few → commissioned the twelve. The compassion-event is the logical ground of the missional response. This makes splanchnizō not merely an emotional footnote but the theological engine of the entire pericope.
> 
> **The simile:** "like sheep without a shepherd" identifies the condition that triggered the compassion-movement: not primarily physical suffering but spiritual destitution — lostness, leaderlessness, vulnerability. This specifies which of the four semantic domains (T7.1 Prompt 3) is operative here: compassion toward spiritual destitution.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=776 · finding_id='OBS-023-T2-144' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T7.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The compassion evidence spans multiple literary forms, each requiring different interpretive care:
> 
> **Gospel narrative (splanchnizō — Matt 9:36; Mark 1:41; Luke 7:13):** The primary splanchnizō evidence is narrative — biographical accounts of Jesus's inner life and actions. Narrative requires attention to: what the narrator is reporting (inner state named explicitly — unusual in ancient narrative), what follows the inner state (action — always), and what the narrative context frames as the interpretive meaning. The narrator's access to Jesus's inner state (splanchnizō) is a theological claim, not merely a psychological observation. Responsible interpretation reads the narrative's theological intent.
> 
> **Parable (Luke 10:33; 15:20; Matt 18:27):** The parable form carries splanchnizō in didactic contexts — the compassion-movement is named in parables to instruct on the nature of the kingdom, neighbourly love, and divine mercy. Parables require attention to the point of comparison: not every detail carries weight, but the splanchnizō verb in each parable is structurally central to the teaching. Luke 10:33 — the compassion is the moral criterion of the whole parable.
> 
> **Prophetic poetry (Hos 11:8; Isa 46:3; 54:8):** The primary Hebrew compassion evidence is in prophetic poetry — lyrical, imagistic, affectively charged. Prophetic poetry requires attention to: the images being deployed (womb, warmth, momentary anger vs everlasting love), the speaker (God in first person — unusually direct), and the rhetorical context (judgment about to be pronounced, then withdrawn or reframed). The visceral language of prophetic poetry is not hyperbole — it is the form most suited to conveying inner-being reality precisely because it does not reduce to propositional statement.
> 
> **Wisdom and covenant formula (Exod 34:6; Mic 6:8; Hos 6:6):** The formulaic covenant declarations and wisdom sayings carry the structural-definitional claims. These require attention to: the canonical function of the formula (Exod 34:6 cited across the canon), the imperative form of the wisdom saying (Mic 6:8 — "what does the LORD require?"), and the polemical function of Hos 6:6 (chesed over sacrifice). The formula carries more definitional weight than any single narrative instance.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=777 · finding_id='OBS-023-T2-145' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T7.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three key argument structures emerge from the data:
> 
> **Argument 1 — The compassion-mission logic (Matt 9:36-10:1):**
> - Premise 1: The crowds are harassed and helpless, like sheep without a shepherd (condition of need)
> - Premise 2: Jesus sees them and is moved with compassion (splanchnizō — inner event)
> - Conclusion 1: The harvest is great, the labourers few — pray for workers (assessment and prayer-imperative)
> - Conclusion 2: The twelve are commissioned and sent (missional consequence)
> The argument: compassion toward perceived need generates mission. The inner-being event (compassion) is the logical engine of the outward missional response.
> 
> **Argument 2 — The divine compassion-repentance ground (Joel 2:13):**
> - Premise 1: God is gracious and merciful (rachum ve-channum), slow to anger, abounding in steadfast love (established divine character)
> - Premise 2: He relents of disaster (responsive character evidenced)
> - Conclusion: Therefore rend your hearts and return to the LORD (imperative of human response)
> The argument: divine compassion-character is the ground and motivation of human repentance. Repentance is possible and warranted because God is what he is. The inner-being claim (God's compassion) supports the behavioural imperative (rend your hearts).
> 
> **Argument 3 — The Good Samaritan's moral logic (Luke 10:25-37):**
> - Question: What must I do to inherit eternal life? (moral question)
> - Counter-question: What is written? (Torah as criterion)
> - Sub-question: Who is my neighbour? (definitional question)
> - Parable: Three people see the wounded man; one is splanchnizō and acts fully
> - Question: Which of these was a neighbour? (evaluative question)
> - Answer: The one who showed mercy (eleos) — go and do likewise (imperative)
> The argument: compassion (splanchnizō) defines the neighbour relationship and constitutes the answer to the moral question. The inner-being event (gut-stirring) is the criterion of moral adequacy. "Go and do likewise" makes the argument prescriptive: compassion-based action is the form eternal-life-inheriting conduct takes.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=778 · finding_id='OBS-023-T2-146' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '4'  ·  Segment: 'T7.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> The primary verse evidence is distributed across four major contextual settings:
> 
> **Covenantal-crisis setting (Hos 11:8; Isa 54:8; Lam 3:22; Joel 2:13):** The deepest Hebrew compassion evidence arises in contexts of covenantal breach and exile — the moment of maximum relational rupture between God and Israel. The setting reveals that compassion operates most powerfully and is most clearly defined at the point of relationship's greatest strain. Divine compassion is not primarily experienced in stable covenantal peace but in the moment of judgment, exile, and potential abandonment. This contextual setting gives the compassion vocabulary its extraordinary theological depth: it is forged in crisis.
> 
> **Healing and restoration setting (Mark 1:41; Matt 20:34; Luke 7:13; Matt 9:36):** The primary Synoptic evidence arises in encounters between Jesus and those in acute physical, spiritual, or material need. The setting reveals that compassion is the characteristic most directly responsive to human need and suffering as it presents itself in ordinary encounter. This is not the compassion of crisis-and-exile but of immediate, perceptive response to the person in front of the compassionate person.
> 
> **Parable and didactic setting (Luke 10:33; 15:20; Matt 18:27):** Compassion appears in parable to instruct on the nature of divine action (prodigal father), moral duty (Good Samaritan), and eschatological warning (unforgiving servant). The didactic setting reveals that compassion is not merely a natural emotional response but a moral norm — it is what is taught, modelled, and required.
> 
> **Community and epistle setting (1 Pet 3:8; Heb 4:15; 1 Cor 12:26; Heb 10:34):** The NT epistle evidence carries compassion in the context of community formation and Christological grounding. The setting reveals that compassion is a community-constituting virtue and a Christological reality — not merely a private feeling but a shared inner quality that shapes the community's corporate inner life.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=779 · finding_id='OBS-023-T2-147' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '5'  ·  Segment: 'T7.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Two candidates emerge from the data, each capturing a different dimension of the essential character:
> 
> **Candidate 1 — Hos 11:8 (for divine compassion at its deepest):** "My heart recoils within me; my compassion grows warm and tender." This verse names divine compassion with the greatest constitutional specificity in the data: it locates compassion in the heart, names its felt quality (warmth, tenderness), shows its deliberative character (competing with judgment), and demonstrates its outcome (restoration rather than abandonment). No other verse in the data so fully and directly describes the inner-being reality of compassion at its constitutional depth.
> 
> **Candidate 2 — Luke 10:33 (for human compassion at its fullest expression):** "But a Samaritan, as he journeyed, came to where he was, and when he saw him, he had compassion (splanchnizō)." This verse names human compassion at its fullest: cross-boundary, perception-triggered, fully acted-upon, morally normative, and the answer to the question of what love of neighbour looks like. It also connects splanchnizō to the Good Samaritan's complete investment — the fullest chain from inner-movement to outer action in the data.
> 
> **Assessment:** Neither alone captures the full essential character — Hos 11:8 is the definitive statement of compassion as divine inner-being; Luke 10:33 is the definitive statement of compassion as human moral norm. Together they form the essential character's two faces: the divine originating reality and its human instantiation.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=780 · finding_id='OBS-023-T2-148' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '6'  ·  Segment: 'T7.2'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Hos 11:8 uniquely reveals:** The deliberative inner contest within the divine character — the moment at which compassion wins against judgment. No other verse in the data shows compassion as the outcome of a divine inner deliberation in which competing characteristics (judgment, righteousness) are present simultaneously. The verse is unique in naming the inner process rather than merely the outcome: not "I had compassion" but "my heart recoils... my compassion grows warm and tender" — the progressive unfolding of the inner event in real time. This is the only verse in the data that shows the inside of a compassion-movement as it happens.
> 
> **Luke 10:33 uniquely reveals:** That compassion defines the human moral identity — who one is, who one's neighbour is, and what the answer to the moral question of eternal life looks like. The verse is the only one in the data in which splanchnizō is simultaneously (1) the inner event, (2) the moral criterion, (3) the answer to a definitional question ("who is my neighbour?"), and (4) the model for the imperative that follows ("go and do likewise"). No other verse holds all four of these simultaneously.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=781 · finding_id='OBS-023-T2-149' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '1'  ·  Segment: 'T7.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three frameworks are relevant, each addressing a different dimension of the compassion data:
> 
> **1. Affective neuroscience / embodied cognition psychology (most relevant for the somatic vocabulary):** The splanchnizō/ra.cham vocabulary's insistence on the body's interior as the seat of compassion aligns with contemporary affective neuroscience's understanding of emotion as fundamentally embodied — arising from interoceptive signals in the body's interior (particularly the gut and heart). The research on gut-brain connection and the role of the vagus nerve in empathic response provides a contemporary framework that illuminates what the ancient vocabulary was naming. The somatic reality the biblical vocabulary targets has a contemporary neurological correlate.
> 
> **2. Moral philosophy — virtue ethics (most relevant for the character-quality vocabulary):** The chesed/rachum/sumpathēs vocabulary names compassion as a virtue — a stable character disposition (hexis) that defines what kind of person one is and enables characteristic action. Aristotelian virtue ethics provides the most coherent framework for understanding the relationship between the character-quality vocabulary and the action-generating vocabulary: virtue is the stable disposition from which characteristic action arises naturally. The Good Samaritan as the paradigmatic compassionate person maps directly onto the virtue-ethics model of the person whose actions flow from formed character rather than from deliberated calculation.
> 
> **3. Developmental psychology — attachment theory (most relevant for the womb and formative vocabulary):** The RACHAM root's womb-grounding and the eusplanchnos (tender heart) pre-condition vocabulary align with attachment theory's understanding of primary relational bonds as constitutional in their effect. The capacity for compassion-based connection may be constitutively shaped in earliest developmental stages (before conscious memory — the "from the womb" language of Psa 22:10). Attachment security as the constitutional ground of the capacity for compassion-giving is a productive framework for understanding how early relational formation shapes later compassionate character.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=782 · finding_id='OBS-023-T2-150' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '2'  ·  Segment: 'T7.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> **Affective neuroscience illuminates the somatic vocabulary:** Contemporary understanding of interoception (the body's inner sensing of its own state) and gut-brain signalling provides a physiological account of what splanchnizō and ra.cham are naming. The gut-stirring of compassion is not poetic embellishment — it is an accurate description of a real physiological event (vagal activation in response to the perception of another's distress, producing the characteristic sensation in the abdominal interior). The framework makes the vocabulary more coherent: the ancient anatomical language is describing a real somatic event that neuroscience can now characterise.
> 
> **Virtue ethics illuminates the character-formation arc:** The relationship between the event-mode vocabulary (splanchnizō as inner event) and the character-mode vocabulary (rachum as stable disposition) becomes more coherent through virtue ethics: virtuous character is the stable disposition from which virtuous action arises naturally, without deliberate calculation. This explains the Good Samaritan's immediate response — he stops because compassion is what he is, not because he calculated the right thing to do. The virtue framework makes the before-state → during-state sequence in T5.2 more analytically precise.
> 
> **Attachment theory illuminates the eusplanchnos pre-condition:** The tender heart (eusplanchnos) as the constitutional pre-condition for compassion-movement parallels attachment theory's understanding of secure attachment as the constitutional ground of the capacity for empathic connection. The person formed in secure relational bonds has the inner softness (eusplanchnos) that allows compassion to arise readily; the person formed in insecure or avoidant attachment may have a constitutionally defended inner being (hard heart) that resists the compassion-movement. This illuminates why the suppression of compassion requires an explicit act of will (chus prohibition) — the natural movement of the securely attached person is toward the other in need.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=783 · finding_id='OBS-023-T2-151' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '3'  ·  Segment: 'T7.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Three divergences are analytically significant:
> 
> **Divergence 1 — Sovereignty vs automatic response:** Affective neuroscience and attachment theory tend to model compassion as a largely automatic, bottom-up response to perceived distress signals. The verse evidence introduces a dimension the frameworks do not account for: sovereign freedom. Rom 9:15 — "I will have compassion on whom I have compassion" — is the direct theological counter to an automatic-response model. Divine compassion is sovereign and free, not mechanically triggered by perceived need. The divergence reveals that the biblical understanding of compassion includes a dimension of deliberate, free, personal choice that cannot be reduced to neurological automaticity.
> 
> **Divergence 2 — Cross-boundary extension:** Attachment theory accounts well for compassion within established bonds (secure attachment → compassion toward attachment figures). It does not account well for the cross-boundary extension evidenced in Jon 4:11 (Nineveh), Luke 10:33 (Samaritan/Jew), and Mark 1:41 (leper). The biblical compassion vocabulary regularly transcends the natural in-group/out-group boundaries that psychological frameworks expect to limit empathic response. The divergence reveals that biblical compassion has a scope that exceeds what natural developmental processes produce — it involves a reorientation of the inner-being that crosses natural relational limits.
> 
> **Divergence 3 — Compassion through suffering (polusplanchnos/Jas 5:11):** Psychological frameworks tend to model compassion as incompatible with causing or permitting suffering — the compassionate person removes suffering from the other. Jas 5:11 holds deep divine compassion (polusplanchnos) and divinely permitted suffering (Job's endurance) simultaneously without resolution. The divergence reveals that the biblical framework operates with a teleological understanding that psychological frameworks lack: suffering-within-compassion can be purposive, oriented toward a telos that transforms its meaning. The psychological model cannot account for this without importing a theological frame.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=784 · finding_id='OBS-023-T2-152' · status=`pending` · type=`OBSERVATION`

- Raised: '2026-04-30T07:56:14Z'  ·  Pass: '4'  ·  Segment: 'T7.3'
- Instruction version: `WA-second-tier-analysis-instruction-v1-2026-04-30.md`

> Two dimensions surfaced by the frameworks that the verse evidence has not addressed:
> 
> **1. Compassion fatigue / moral injury (from psychology):** Contemporary psychology identifies "compassion fatigue" — the depletion of compassionate capacity through sustained exposure to others' suffering. The Lam 4:10 evidence (compassionate women violating their compassion under siege) is the closest equivalent in the data, but the verse evidence does not address the gradual depletion of compassionate capacity through sustained exposure rather than acute catastrophe. Whether the biblical vocabulary addresses the sustainability of compassion under sustained demand is not explored in the current data. This may require further verse investigation in the wisdom literature (Prov) and the lament Psalms.
> 
> **2. Mirror neurons / embodied simulation (from neuroscience):** Contemporary neuroscience has identified the role of mirror neuron systems in empathic response — the automatic inner simulation of another's experience in one's own neural system. The sumpatheō/sumpaschō vocabulary names something structurally similar (suffering-with as genuine inner participation), but whether the biblical vocabulary intends a claim about the mechanism of this participation — whether it involves actual inner replication of the other's experience — is not addressed. Further verse investigation of the sumpaschō vocabulary (particularly 1 Cor 12:26 and Rom 8:17) may illuminate whether the bodily solidarity named there has implications for the biblical understanding of how compassion works at the constitutional level.
> 
> **What is missing (P):** Both gaps would benefit from further verse investigation, but neither is clearly covered by existing SD pointers. They are new gaps of different character: (1) is a potential verse gap (further investigation within the existing corpus); (2) is a methodological question about the mechanism implied by the vocabulary. Both are noted for Session D.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2165 · finding_id='SYN-INTRA-023-001' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '1'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1'
- Structural relationship: 'N/A'
- SD pointer ref: "NEW GAP — receiver's inner-being experience (not currently registered)"

> T1 reveals compassion as a definitionally complex characteristic that simultaneously operates as character quality (ra.chum — the settled disposition of the compassionate person), inner event (splanchnizō — the moment of being-moved), condition of its object (eleeinos — the pitiable state that calls compassion forth), and externalised act (almsgiving, mercy-act). No other characteristic in the programme review set operates across all four kinds simultaneously. The four root families (RACHAM, CHASAD, SPLANCHN, OIKTIROM) identify four constituent dimensions of the single characteristic, each naming a distinct register — somatic-maternal, covenantal-relational, visceral-immediate, and deliberative-pitying respectively. The structural opposites are two distinct kinds: willed judicial hardness (the hardened heart that refuses compassion) and unwilled prosperity-blindness (Eze 16:49 — the one who does not see the need because they are satiated). The dimension classification (Relational Disposition as primary) is confirmed by the consistent outward-facing structure: compassion cannot exist without a suffering other. The definitional tier's most critical gap — the receiver's inner-being experience — is entirely absent from the data, affecting T1.5, T1.6, and T1.7 throughout. This gap is the single most significant analytical absence in the registry.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2166 · finding_id='SYN-INTRA-023-002' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '2'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2'
- Structural relationship: 'N/A'
- SD pointer ref: 'NEW GAP — spirit-level dimension (not currently registered)'

> T2 produces the most distinctive constitutional portrait in the current review set. Spirit-level location is entirely absent — three consecutive S ratings — forming a new gap. By contrast, soul-level (chesed as covenantal-soul character), heart-level (Hos 11:8 — "my heart recoils"), and somatic-level (re.chem, splanchnon) are all richly evidenced. The constitutional architecture is bottom-up: the womb and entrails are the originating ground; the soul and heart are the engagement points; the act is the constitutional expression. Four body-part functions are identified: constitutive (womb — the generative image of compassion), expressive (gut — the felt movement), indicative (Synoptic pattern — splanchnizō signals the compassion-event), and mediating (heart in Hos 11:8 — the deliberative locus where compassion and judgment contend). The four-stage constitutional movement sequence (somatic arousal → soul engagement → volitional engagement → outward action) is uniquely evidenced in this registry — consistently inside-out and bottom-up. T2.8 established no body deposit; T5.7 is formally closed. The constitutional portrait confirms the sb_classification (soul-body interface) and extends it: compassion is the most somatically grounded characteristic in the programme, with its originating logic residing in the body's deepest interior.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2167 · finding_id='SYN-INTRA-023-003' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '3'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3'
- Structural relationship: 'N/A'

> T3 reveals two structurally distinctive findings about compassion's faculty engagement. First, creativity is entirely silent (three S ratings) — the most informative absence in the tier: compassion responds, it does not originate or create. It is the most responsive of the faculties-engaging characteristics. Second, affect and moral action are structurally unified in compassion — not sequentially related but simultaneous. Affect is the mechanism of movement (splanchnizō is both the felt inner event and the cause of the action), not a precursor or accompaniment. This is unique among the characteristics reviewed: in most other registries, affect and volition are distinguishable stages; in compassion, the felt movement is already the morally motivated action beginning. A third distinctive finding: compassion converts moral knowledge into motivated action — it is the motivational ground of conscientiousness, not a product of it. The conscience faculty engagement reveals compassion as conscience-healing: it addresses the pitiable condition that conscience perceives as a moral claim, resolving the tension between moral knowledge and moral incapacity. The three relational modes (building/sustaining — chesed; restoring/repairing — splanchnizō; extending across difference — Good Samaritan) are a new finding not in the instruction typology.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2168 · finding_id='SYN-INTRA-023-004' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '4'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4'
- Structural relationship: 'N/A'
- SD pointer ref: 'SD-009 (compassion/mercy boundary — most critical for T4.3/T4.5)'

> T4 reveals the most structurally developed relational architecture for compassion's scope. God's compassion operates simultaneously on three bases: sovereignly free (Rom 9:15 — "I will have compassion on whom I have compassion"), covenantally grounded (chesed as the bond-loyalty that grounds the characteristic), and situationally responsive (splanchnizō — triggered by the specific sight of suffering). These three bases are not in tension but in integration: divine compassion is free, covenanted, and responsive simultaneously. The scope finding is among the most analytically significant in the registry: compassion explicitly and repeatedly crosses covenantal boundaries (Nineveh, the Samaritan/Jew axis, the power-asymmetric relationship). Scope is defined by perceived need, not moral standing or covenantal membership — this is formally confirmed in the data and distinguishes compassion from many other relational characteristics. The chesed/splanchnizō distinction maps onto distinct relational registers: chesed sustains within established bonds; splanchnizō extends across distance and difference. T4.4 (receiver's inner-being experience) is the most significant gap — four P-rated prompts, entirely absent from the data. T4.6 (spiritual beings interface) is entirely silent across all four prompts.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2169 · finding_id='SYN-INTRA-023-005' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '5'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T5'
- Structural relationship: 'N/A'
- SD pointer ref: 'SD-014 (polusplanchnos — compassion and permitted suffering)'

> T5 produces three inter-related formation findings. First, transformation is evidenced in both modes simultaneously (Luke 15:20-24 — the father's compassion produces condition-change in the son's standing AND orientation-change in his reception of identity). Second, the formative cycle is self-reinforcing: the after-state of compassion-received feeds back into the before-state of compassion-readiness in the future — the person who has received compassion becomes more capable of extending it. Third, compassion plays a dual role in the sanctification arc: it is simultaneously the character target being formed (the person becoming compassionate over time) and the motivational ground that makes the formative relationship survivable through failure and return. Matthew 18:27 introduces the most critical formative warning: received compassion can be forfeited by failure to extend it — compassion is not a permanently possessed gift but a participatory moral framework. Three distinct mechanisms of change operate across contexts: encounter/sudden (splanchnizō — the moment of being moved), covenantal-sustaining/gradual (chesed — the steady faithfulness over time), and participatory-ontological (2Pe 1:4 pattern — sharing in what God is). T5.7 is formally closed: no body deposit established. All four relationships between suffering and compassion are evidenced — suffering reveals, tests, deepens, and produces compassion.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2170 · finding_id='SYN-INTRA-023-006' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '6'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T6'
- Structural relationship: 'N/A'
- SD pointer ref: 'SD-008 (CHASAD crossing clusters), SD-017 (Exod 34:6 anchor), SD-009 (compassion/mercy boundary)'

> T6 reveals compassion as the structural centre of the C17 cluster rather than a peripheral member. The love co-occurrence (196/351 = 55.8% of all OWNER verses) is uniquely dominant — compassion and love co-occur in more than half of all active verses, raising the programme-level question whether they are truly separable at the data level. Three structural observations from the co-occurrence landscape: (1) compassion sits at C17's centre of gravity (love, mercy, kindness as top three co-occurrences — all within-cluster); (2) compassion generates a human-response cluster (peace, faith, will, surrender, seeking co-occurring at significant levels — the pattern of divine compassion generating human inner-being responses); (3) compassion is constitutively responsive to human distress (despair, guilt, distress, evil all present in the co-occurrence table — compassion operates most characteristically in the presence of need). The CHASAD root crossing compassion (C17) and shame (C06) is the programme's most structurally unexpected finding — a root family that bridges two clusters. Exod 34:6 as the programme's most multiply-anchored verse (6 registries) must be treated as a cluster-level synthesis anchor. The compassion/mercy boundary (SD-009) is the most critical unresolved distinction. T6.7 (dimensional sharing) is programme-stage limited — formally deferred.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2171 · finding_id='SYN-INTRA-023-007' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '7'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T7'
- Structural relationship: 'N/A'
- SD pointer ref: 'NEW GAP — LXX systematic analysis (not currently registered)\n\nIntra-tier pass COMPLETE: 2026-04-30. D: 7. F: 0. N: 0.\n\n---'

> T7 produces the most vocabulary-analytically significant findings in the registry. The full vocabulary arc (from womb — most intimate — to almsgiving — most institutional) is unique in the programme: no other characteristic traverses this complete arc with equivalent lexical clarity. The CHASAD root includes shame as the negative semantic pole embedded within the compassion vocabulary itself — not an external antonym but an internal semantic component of the root family. The dual primary anchor finding (Hos 11:8 for divine compassion at constitutional depth; Luke 10:33 for human compassion as moral norm) establishes the two poles of the characteristic's evidential range. Three key argument structures: compassion-mission logic (Matt 9:36-10:1 — compassion as the theological engine of missional response), divine compassion-repentance ground (Joel 2:13 — divine character as the ground of human response-posture), Good Samaritan's moral logic (Luke 10:25-37 — compassion as the answer to "who is my neighbour?"). Three human science frameworks illuminate the vocabulary with genuine alignment (affective neuroscience, virtue ethics, attachment theory) and all three diverge from the biblical account at specific points (sovereignty vs automaticity; cross-boundary extension exceeding natural empathic scope; purposive suffering in Jas 5:11 requiring teleological frame). The LXX systematic analysis gap (NO_WORD_ANALYSIS flag on 98 terms) is the most significant methodological limitation — a new gap for the programme.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2172 · finding_id='SYN-INTER-023-008' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '8'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T2'
- Structural relationship: 'constitutive'

> T1's four-kind structure (character quality, inner event, condition of object, externalised act) maps precisely onto T2's constitutional levels. The character-quality kind (ra.chum — dispositional compassionate character) operates at the soul level (T2.2 — chesed as soul-character). The inner-event kind (splanchnizō — the moment of being-moved) operates at the somatic level (T2.6 — the gut as the site of the stirring). The condition-of-object kind (eleeinos — the pitiable state) is the constitutional trigger that activates the somatic-constitutional movement. The externalised-act kind is the constitutional endpoint of T2.10's four-stage movement sequence. T1's definition and T2's constitutional account are co-determining: the characteristic cannot be adequately defined without specifying the constitutional levels at which its four kinds operate.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2173 · finding_id='SYN-INTER-023-009' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '9'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T3'
- Structural relationship: 'constitutive'

> T1's four kinds explain T3's most distinctive finding: that affect and moral action are structurally unified rather than sequential. In T1 terms, compassion-as-inner-event (splanchnizō) and compassion-as-externalised-act are not two separate kinds but a continuous movement — the felt-movement is the beginning of the act. T3 confirms this: affect is the mechanism of movement, not its precursor. T1's finding that compassion converts moral knowledge into motivated action (the unique position as motivational ground of conscientiousness) maps onto T3.10's finding of the same: the definitional claim (T1) that compassion is constitutively outward-facing explains T3's finding that it is the driving faculty between moral knowledge and moral action.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2174 · finding_id='SYN-INTER-023-010' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '10'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T4'
- Structural relationship: 'constitutive'

> T1's scope finding (compassion requires a suffering other; scope is determined by perceived need, not moral standing) is precisely confirmed in T4's relational analysis. The explicit crossing of covenantal boundaries (Nineveh, Samaritan/Jew) evidenced in T4 is the relational expression of T1's boundary-definition: compassion ends where the condition (pitiable need) is absent, not where covenantal membership ends. T1's four modes of operation (T1.4) — intra-covenantal, cross-boundary, anticipatory, Christological — map onto T4's chesed/splanchnizō distinction (within-bond sustaining vs across-distance extending) and the scope analysis (covenantal and transcovenantal registers). Definition and relational scope are structurally co-determining.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2175 · finding_id='SYN-INTER-023-011' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '11'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T5'
- Structural relationship: 'sequential'

> T1's sustained-effect analysis (largely P-rated because the receiver's inner-being experience is absent) and T5's formation arc together reveal a gap that is structurally significant: the formation process from single compassion-event to compassion-character is the most important untraced developmental relationship in the registry. T5 provides the directional finding (the formative cycle feeds back from after-state to before-state) and names the three mechanisms (encounter/sudden, covenantal-sustaining/gradual, participatory-ontological). T1 provides the definitional starting point (compassion as character quality is the endpoint of formation). Together they frame an arc that is identified but not filled: how does the moment of splanchnizō (T1 inner-event) accumulate into the settled character of ra.chum (T1 character quality)? T5's mechanisms suggest the answer but the data does not trace the path explicitly — a gap confirmed by both tiers.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2176 · finding_id='SYN-INTER-023-012' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '12'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T6'
- Structural relationship: 'constitutive'

> T1's primary dimension (Relational Disposition) and T6's co-occurrence landscape are mutually confirming. The love co-occurrence dominance (196 verses) is the co-occurrence expression of T1's relational-disposition classification: love and compassion co-occur at this extraordinary rate because they share the relational-disposition register. T1's finding that compassion is constitutively outward-facing explains why the co-occurrence landscape shows the C17 cluster (love, mercy, kindness) as the primary co-occurrence family. T6's unresolved compassion/mercy distinction (SD-009) is the most critical consequence of T1's definitional incompleteness — the boundary between compassion and mercy as adjacent Relational Disposition characteristics is the definitional question T1 cannot answer without T6 data.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2177 · finding_id='SYN-INTER-023-013' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '13'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T7'
- Structural relationship: 'constitutive'

> T1's four-kind structure is encoded in T7's vocabulary architecture. The character-quality kind (ra.chum) is carried by the adjectival forms (H7349, G4835); the inner-event kind (splanchnizō) by the verbal forms (G4697, H7355); the externalised-act kind by the noun forms and compound forms (G1656, H2617B). T7's vocabulary arc (womb to almsgiving) is the lexical expression of T1's range from the most interior character quality to the most exterior externalised act — the same spectrum named by the definition is traversed by the vocabulary. The dual primary anchor (T7) maps onto T1's dimensional analysis: Hos 11:8 provides the evidence for the divine relational disposition; Luke 10:33 provides the evidence for the human relational disposition as moral norm.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2178 · finding_id='SYN-INTER-023-014' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '14'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T3'
- Structural relationship: 'constitutive'

> T2's four-stage constitutional movement sequence (somatic arousal → soul engagement → volitional engagement → outward action) maps directly onto T3's faculty engagement sequence. The somatic-arousal stage (T2.6 — gut stirring, splanchnizō) corresponds to T3.1's perceptive-trigger stage (sight activates the somatic response) and T3.4's affect stage (the stirring is the affective movement). The soul-engagement stage (T2.2 — chesed as soul-character) corresponds to T3.8 moral evaluation (the soul assesses the need) and T3.9 conscience (the conscience activates the response). The volitional-engagement stage (T2.3 — heart-locus as deliberative site) corresponds to T3.6 volition (the will directs the action). The outward-action stage corresponds to T3.7 agency. T2 and T3 describe the same movement sequence from two perspectives: T2 maps the constitutional levels; T3 maps the faculties active at each level.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2179 · finding_id='SYN-INTER-023-015' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '15'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T4'
- Structural relationship: 'causal'

> T2's constitutional origin analysis (somatic-relational-covenantal triple ground) and T4's relational direction analysis are structurally aligned. The somatic origin (womb, gut) grounds the cross-boundary relational direction in T4: splanchnizō's somatic immediacy is precisely what enables it to cross covenantal boundaries — the gut-movement toward the suffering other precedes any covenantal assessment of the relationship. The covenantal origin (chesed) grounds the within-bond sustaining direction in T4. The constitutional origin therefore predicts the relational direction: somatic = cross-boundary; covenantal = within-bond. T2's soul-body interface classification explains T4's scope-by-need finding: because compassion originates at the soul-body interface (before covenantal-rational assessment), its scope is determined by the pre-rational recognition of need rather than the post-rational assessment of covenantal standing.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2180 · finding_id='SYN-INTER-023-016' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '16'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T5'
- Structural relationship: 'constitutive'

> T2's four-stage constitutional movement (somatic arousal → soul → volition → action) and T5's three mechanisms of change (encounter/sudden, covenantal-sustaining/gradual, participatory-ontological) are structurally complementary. T2 describes the movement within a single compassion-event; T5 describes how that event accumulates into character over time. The encounter/sudden mechanism (T5) corresponds to the full four-stage sequence of T2 in a single instance. The covenantal-sustaining mechanism (T5) corresponds to the repeated operation of the somatic-soul pathway (T2.2 — soul-level chesed as the sustaining character) over time. The participatory-ontological mechanism (T5) corresponds to the constitutional direction T2 identifies but leaves at spirit-level gap: if the deepest formation is participatory-ontological, the spirit-level dimension (T2.1 — entirely silent) may be where this operates — a convergent gap from two tiers.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2181 · finding_id='SYN-INTER-023-017' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '17'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T6'
- Structural relationship: 'constitutive'

> T2's somatic-constitutional location explains several T6 structural connections. The shared anchor at Isa 53:5 (with R030 contrition) confirms that the somatic wound vocabulary intersects both compassion and contrition at the constitutional-somatic level — both characteristics have somatic-body language as part of their evidential ground. The CHASAD root's crossing of compassion and shame clusters (T6.4 — most unexpected structural finding) is partly explainable from T2: if CHASAD names a covenantal-soul disposition, it can operate in both the positive register (chesed — steadfast love/compassion) and the negative register (bōsheth — shame as the opposite soul-condition of exposed vulnerability). T2's constitutional portrait (soul-body interface) is the constitutional ground for the root-level cluster-crossing that T6 identifies.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2182 · finding_id='SYN-INTER-023-018' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '18'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T7'
- Structural relationship: 'constitutive'

> T2's constitutional levels are each carried by specific vocabulary families in T7. The somatic-body level (T2.6 — gut, womb) is carried by the RACHAM/SPLANCHN root families — the body's interior as the etymological ground of both. The soul-character level (T2.2) is carried by the CHASAD family — chesed as the settled covenantal character disposition. The heart-deliberative level (T2.3) is evidenced most richly in Hos 11:8 (T7's primary anchor for divine compassion). T7's vocabulary arc (womb to almsgiving) traverses exactly the constitutional range T2 maps: from the most interior somatic level (womb) through the character-soul level to the externalised action level. The dual primary anchor (T7) maps onto T2's constitutional depth: Hos 11:8 evidences constitutional depth (heart-level deliberation of compassion over judgment); Luke 10:33 evidences constitutional breadth (the full four-stage movement from sight to action).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2183 · finding_id='SYN-INTER-023-019' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '19'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T4'
- Structural relationship: 'parallel'

> T3's perceptive-trigger finding (compassion is activated by sight — splanchnizō is perceptively dependent) and T4's scope-by-need finding (scope is determined by perceived need, not covenantal standing) are the same finding from two analytical perspectives. T3 names the faculty (perception) and its function (triggering compassion by seeing the pitiable condition); T4 names the relational consequence (scope defined by what is seen). The cross-boundary extension in T4 (Nineveh, Samaritan/Jew) is the relational expression of T3's merit-independence: compassion is perceptively dependent (it must see the need) but merit-independent (it does not assess the moral standing of the one seen). The three relational modes in T3.11 (building/sustaining, restoring/repairing, extending across difference) correspond precisely to T4's chesed/splanchnizō/cross-boundary structure.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2184 · finding_id='SYN-INTER-023-020' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '20'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T5'
- Structural relationship: 'sequential'

> T3's affect-moral-action unity (affect is the mechanism, not the precursor) and T5's formation finding (compassion is simultaneously character target and motivational ground) are structurally connected. T5 names compassion as the motivational ground that makes the sanctification arc survivable through failure and return — but T3 has already established that affect is the mechanism of this motivational ground: the character formation that T5 describes is accomplished through the affective mechanism that T3 identifies. The person who is formed into compassionate character (T5) is the person whose affective faculty has been trained to respond immediately and morally to perceived suffering (T3). T3's finding that affect and moral action are unified is T5's mechanism of formation: the person becoming compassionate is the person in whom the affective-moral unity is deepening and stabilising.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2185 · finding_id='SYN-INTER-023-021' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '21'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T6'
- Structural relationship: 'constitutive'

> T3's finding that compassion is the motivational ground of conscientiousness explains the co-occurrence pattern in T6. Conscience (T3.9) and moral evaluation (T3.8) are the faculties that register the pitiable need as a moral claim; compassion is the affective-motivational response that converts that moral knowledge into action. The co-occurrence of will (R173 — 25 verses) and surrender (R156 — 21 verses) in T6 is the co-occurrence expression of T3's volitional faculty finding: compassion engages and redirects the will toward the suffering other. The sequential relationship confirmed in T6 (compassion → mercy — constitutionally causal) is the relational expression of T3's finding that compassion converts moral knowledge into motivated action: the mercy-act is the action that compassion's motivation produces.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2186 · finding_id='SYN-INTER-023-022' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '22'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T7'
- Structural relationship: 'constitutive'

> T3's perceptive-trigger and affect-mechanism findings are grounded in T7's primary anchor evidence. The Synoptic pattern of splanchnizō — always triggered by sight, always preceding action — is the textual ground for T3.1's finding (compassion is perceptively dependent) and T3.4's finding (affect is the mechanism of movement). T7's argument structure finding (Matt 9:36 — compassion as the theological engine of missional response) is the evangelist's literary expression of T3.10's analytical claim (compassion converts moral knowledge into motivated action). T7's framework divergences (human science frameworks failing at sovereignty, cross-boundary extension, and purposive suffering) correspond to the three areas where T3's faculty analysis finds its most distinctive results: the sovereign freedom of divine compassion exceeds the natural automaticity of empathic response; the cross-boundary extension exceeds natural empathic scope; the purposive suffering (T5.4/T5.5) requires the teleological frame that T7.3 identifies.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2187 · finding_id='SYN-INTER-023-023' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '23'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4, T5'
- Structural relationship: 'parallel'

> T4's finding that divine compassion operates on three simultaneous bases (sovereignly free, covenantally grounded, situationally responsive) and T5's three mechanisms of change (encounter/sudden, covenantal-sustaining/gradual, participatory-ontological) are structurally isomorphic. The sovereignly-free basis corresponds to the encounter/sudden mechanism: divine compassion operating freely produces the sudden compassion-event (splanchnizō). The covenantally-grounded basis corresponds to the covenantal-sustaining mechanism: chesed as the sustaining relational ground operates gradually and consistently. The situationally-responsive basis opens toward the participatory-ontological mechanism: formation at the deepest constitutional level produces a person who is dispositionally responsive to every situation of need. T4's relational architecture and T5's formation mechanisms are the same structural reality described from relational and developmental perspectives respectively.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2188 · finding_id='SYN-INTER-023-024' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '24'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4, T6'
- Structural relationship: 'causal'

> T4's scope-by-need finding (compassion crosses covenantal boundaries) and T6's co-occurrence landscape (the human-response cluster — peace, faith, will, surrender — co-occurring with compassion) reveal a structural pattern: divine compassion reaching across boundaries generates a characteristic cluster of human inner-being responses regardless of the covenantal position of the recipient. The Nineveh response (repentance and turning) and the pattern of peace/faith/will/surrender co-occurring with compassion both confirm this: compassion-received generates a recognisable inner-being response cluster that is structurally consistent across relational positions. T6's mapping of the human-response cluster is the co-occurrence evidence for T4's structural finding about scope and response.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2189 · finding_id='SYN-INTER-023-025' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '25'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4, T7'
- Structural relationship: 'constitutive'

> T4's three bases of divine compassion (sovereignly free, covenantally grounded, situationally responsive) are each grounded in specific textual evidence from T7. The sovereignly-free basis is evidenced in Rom 9:15 (T7's argument structure analysis — divine compassion as sovereign determination). The covenantally-grounded basis is evidenced in Exod 34:6 (T7's most multiply-anchored verse — the divine self-declaration in the covenant context). The situationally-responsive basis is evidenced in the Synoptic splanchnizō pattern (T7.2 — the sight-event structure of the Gospels). T7's framework divergences (sovereignty vs automaticity) map directly onto T4's relational analysis: the framework correctly identifies that divine compassion's sovereign freedom (T4.1) is what exceeds the natural empathic automaticity that human science frameworks describe.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2190 · finding_id='SYN-INTER-023-026' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '26'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T5, T6'
- Structural relationship: 'causal'

> T5's three mechanisms of change explain the structural pattern visible in T6's co-occurrence landscape. The encounter/sudden mechanism (splanchnizō producing immediate transformation) corresponds to the high co-occurrence with despair (28 verses) and distress (16 verses) — these are the conditions that trigger the sudden compassion-event. The covenantal-sustaining mechanism corresponds to the high co-occurrence with love (196 verses), mercy (76 verses), and covenant (17 verses) — these are the characteristics that share the sustaining, gradual register with chesed. The participatory-ontological mechanism corresponds to the sequential relationship (compassion → mercy confirmed as constitutionally causal in T6.2) — the deepest formation mechanism produces the person who naturally extends mercy as the externalised form of the compassion-character formed within. Formation mechanisms (T5) explain co-occurrence patterns (T6).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2191 · finding_id='SYN-INTER-023-027' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '27'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T5, T7'
- Structural relationship: 'constitutive'

> T5's finding that suffering reveals, tests, deepens, and produces compassion is grounded in T7's vocabulary and textual evidence. The polusplanchnos hapax (T7 — coined because existing vocabulary was insufficient for the depth of compassion at the point of maximum permitted suffering) is the lexical expression of T5's most profound formation claim: suffering in the context of compassion-formation produces a depth of compassion that transcends ordinary vocabulary. T7's framework divergence at purposive suffering (Jas 5:11 — teleological frame required) is the analytical expression of T5.4's finding that suffering in the biblical frame produces compassion (as a formative outcome) rather than merely accompanying it. The dual primary anchor (Hos 11:8 and Luke 10:33) maps onto T5's dual-role finding: Hos 11:8 evidences compassion as the character being formed in God (which the human images); Luke 10:33 evidences compassion as the formed character in the human person (the moral norm).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=2192 · finding_id='SYN-INTER-023-028' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-05-01T09:19:01Z'  ·  Pass: '28'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T6, T7'
- Structural relationship: 'constitutive'

> T6's structural connections and T7's vocabulary analysis are mutually confirming at the most analytically significant points. The CHASAD root crossing two clusters (T6.4 — most unexpected structural finding) is confirmed and extended by T7's vocabulary analysis: the CHASAD root includes shame as the negative semantic pole embedded within the root itself (T7.1 P5), not as an external antonym. This means the cluster-crossing T6 identifies is not an external structural anomaly but an internal semantic feature: the compassion vocabulary contains its own opposite at the root level. Exod 34:6 as the programme's most multiply-anchored verse (T6.6 — 6 registries) is also T7's most evidentially rich single text — the verse that carries the most structural connections is the same verse that is most analytically central to the vocabulary analysis. The love co-occurrence dominance (T6.1 — 196/351 verses) is confirmed by T7's vocabulary arc: the vocabulary's fullest range (womb to almsgiving) overlaps extensively with the love vocabulary's range, which is why they co-occur across more than half of all active verses.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R072 groaning — 1 unresolved

#### sbf.id=63 · finding_id='DIM-072-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`
- Anchor verses: Rom 8:26

> Group 899-001 (G4726 stenagmos, the Spirit's inarticulate groaning in Romans 8): assigned Spiritual/God-ward. This is a pneumatological dimension unique in the C05 cluster — the Spirit interceding within the inner being through groaning that is beyond the person's own capacity for articulation. Session B should examine this group as a distinctive case of the inner being as the locus of the Spirit's intercessory activity.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R086 impurity — 1 unresolved

#### sbf.id=108 · finding_id='DIM-086-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Group 5574-001 (akathartos — unclean spirit) presents the unclean spirit as an inner occupant whose presence produces inner captivity and whose expulsion by Christ restores inner freedom. Session B should examine this as a model of inner-being occupation and liberation — the inner person as the site of spiritual occupancy — and how this relates to the programme's understanding of the inner being's relationship to spiritual forces.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R108 meditation — 1 unresolved

#### sbf.id=34 · finding_id='DIM-108-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`
- Anchor verses: Psa 19:14; Psa 9:16

> Higgayon (H1902H) operates as a directionally-determined cognitive act — the same reflective faculty deployed in devout meditation toward God (975-001) and in hostile scheming against others (5883-001). The act is morally neutral in itself; direction determines its character. This is Sub-pattern A of the directionally-determined inner faculty pattern identified across C02.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

## §2. Unresolved research flags

### R005 anguish — 1 unresolved

#### srf.id=678 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M01-BOUNDARY-H7661'
- Strong's ref: `H7661`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M01 closure (DIR-20260516-007): BOUNDARY term H7661 (sha.vats) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — H7661 sha.vats]. Pending researcher disposition: set-aside / promote-to-M01-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R5 (anguish).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R023 compassion — 54 unresolved

#### srf.id=74 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='MEDIUM'

- Label: 'PH2-023-001'
- Strong's ref: `G1656`
- Raised: '2026-03-26'  ·  Session target: 'D'

> G1656 (mercy) — 240 occ, 26 verses (11%).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=75 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='MEDIUM'

- Label: 'PH2-023-002'
- Strong's ref: `G3628`
- Raised: '2026-03-26'  ·  Session target: 'D'

> G3628 (compassion) — 36 occ, 5 verses (14%).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=76 · flag_code=`PH2_DATA_ERROR` · priority='HIGH'

- Label: 'PH2-023-003'
- Strong's ref: `H0854`
- Raised: '2026-03-26'  ·  Session target: 'B'

> EXTRACTION ANOMALY — seventh consecutive registry. H0854 et (with, 932 occ HFA preposition) incorrectly extracted. Reclassified to delete. See PH2-034-005.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=236 · flag_code=`DIMREVIEW_SESSION_D` · priority='MEDIUM'

- Label: 'DIM-23-SD001'
- Raised: '2026-04-11'  ·  Session target: 'D'

> The Hebrew root CHASAD (Reg 23) crosses into Reg 146 (shame): H2616A cha.sad (be kind) and H2617B che.sed (steadfast love) are in Reg 23; H2616B cha.sad (to shame) is in Reg 146. The same root family spans the two poles of relational experience: covenantal love/mercy (chus, chesed) and shame/exposure. This is not incidental — the same etymological root covers both the relational bond at its most loyal and the relational wound at its most exposed. Session D should examine whether this root-family crossing reveals a structural relationship between mercy and shame in the inner-being vocabulary of Scripture: whether the depth of mercy presupposes the depth of shame, or whether the vocabulary itself encodes the relational restoration movement (from shame/exposure to mercy/covering). Relevant registries: C17 (compassion/love/kindness/mercy) and C06 or equivalent shame cluster.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=237 · flag_code=`DIMREVIEW_SESSION_D` · priority='MEDIUM'

- Label: 'DIM-23-SD002'
- Raised: '2026-04-11'  ·  Session target: 'D'

> Group 734-001 (sumpatheō — sympathy, Reg 23) is anchored by Heb 4:15: Christ's capacity to sympathize with human weaknesses, grounded in his own temptation. This is a case of genuine divine-human solidarity — the same inner capacity for fellow-feeling is attributed to the incarnate Son in his priestly role. Session D should examine whether the sympathy/compassion vocabulary of Reg 23 contains a sub-pattern of terms that describe the capacity for trans-boundary solidarity (God/human, Christ/human): splanchnizō (divine-human compassion in the Synoptics), oikteirō (sovereign divine compassion), sumpatheō (priestly solidarity through shared humanity), ra.cham (mother-womb metaphor). This sub-pattern may map onto a unique dimension of the C17 cluster: compassion as the inner quality that crosses boundaries of power, vulnerability, and status.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=260 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD001'
- Cross-registry: 103
- Raised: '2026-04-12'  ·  Session target: 'D'

> H7356A ra.cham (womb, Reg 23) and H7358 re.chem (womb, anatomical) share the same root as the RACHAM family in Love (Reg 103). The womb-metaphor grounds divine compassion; the same root grounds divine and human love. The question for Session D: does the womb-root function as a unifying somatic image across both compassion and love, or does it serve different semantic purposes in each registry? Evidence: Isa 46:3 (compassion context); Gen 29:31 (love/provision context — God opening the unloved wife's womb).
> 
> ---
> 
> #### Term 2: H7358 re.chem — womb, anatomical (occ=26, extracted)
> *Sense structure: 25 verses in export, all anatomical usage. The womb as: closed by God (Gen 20:18 — divine sovereignty over fertility); opened by God (Gen 29:31, 30:22 — compassion on the unloved); firstborn that opens (Exod 13:2,12 — consecration); the origin-space from which Israel was carried (Isa 46:3 — the same verse as H7356A's metaphorical anchor). The term is almost exclusively anatomical throughout the corpus.
> 
> Semantic observation: The word re.chem names the physical organ; ra.cham names the compassion that originates from it. The relationship is the reverse of the usual direction — the abstract (compassion) is named after the concrete (womb), not the other way around. This is unusual in Hebrew word formation and gives the compassion vocabulary a somatic grounding that is built into the language itself rather than being a later metaphorical extension.
> 
> Session C check: Section 4 identifies this correctly as "the anatomical root." Section 1 correctly notes the womb-metaphor. No correction required.
> 
> meaning_numbered gap:* Null. GAP noted.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=261 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD002'
- Cross-registry: 103
- Raised: '2026-04-12'  ·  Session target: 'D'

> H7358 re.chem (womb, 26 occ) is primarily a fertility and creation-order term. Its 26 occurrences include divine sovereignty over conception and birth (Gen 20:18; 29:31; 30:22) — language closely associated with the Love (Reg 103) and potentially Calling (Reg 19) registries. The question: does divine sovereignty over the womb constitute a cross-registry connection between Compassion (the response to suffering), Love (the relational disposition), and Calling (divine purpose from before birth)? Isa 49:1 ("The Lord called me from the womb") and Jer 1:5 ("before you were born I consecrated you") belong to other registries but are semantically adjacent.
> 
> ---
> 
> #### Term 3: H7362 ra.cha.ma.ni — compassionate (occ=1, extracted_thin)
> *Sense structure: Adjective from the RACHAM root. Single occurrence: Lam 4:10 — the compassionate (ra.cha.ma.ni) women who boiled their children. The adjective names the settled character quality of compassion. The verse's force depends entirely on the characterisation: these are compassionate women — yet this is what they did. The term names the inner quality at the moment of its most catastrophic inversion.
> 
> Semantic observation: This is the only adjectival form in the OWNER vocabulary for this registry. It establishes that compassion is a character quality (the adjective names what kind of person one is, not what one does in a moment). The tragedy of Lam 4:10 is that character qualities are not indestructible — extreme circumstance can force violations of the deepest human dispositions.
> 
> Session C check:* Section 3 annotation confirmed accurate and complete.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=262 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD003'
- Cross-registry: 214
- Raised: '2026-04-12'  ·  Session target: 'D'

> The Lam 4:10 usage raises the question of compassion's resilience as an inner characteristic — whether characteristics can be permanently destroyed by circumstance, or temporarily violated. This connects to the Suffering registry (Reg 214) and potentially to Brokenness (Reg 18) and Anguish (Reg 5). The verse also appears in the C05 cluster context (grief, mourning) — the violation of compassion is itself a form of communal grief.
> 
> ---
> 
> #### Term 4: H2347 chus — to pity (occ=24, extracted)
> *Sense structure: Two groups: pity as an inner disposition that moves toward or spares (group 3182-001), and the judicial withholding of pity (group 3182-002). The related-words list shows only one entry: darkened (H2345 chum). This is an unusual related-word — pity and darkness do not share obvious semantic territory, suggesting the connection is through root similarity rather than semantic affinity. No meaning_numbered field.
> 
> From verse corpus: H2347 is used in two distinct frames — (a) the injunction not to pity (most frequently: Deut 7:16; 13:8; 19:13; Ezek 7:4,9; 8:18; 9:5,10 — all judicial/warfare contexts where compassion is explicitly prohibited); (b) the affirmative pity toward the weak (Ps 72:13; Jon 4:11). The negative usage (withhold pity) is more frequent than the positive (show pity). This is noteworthy: the term appears most often in the context of its prohibition.
> 
> Semantic boundary: Chus describes the impulse of pity — the instinctive sparing of the other. When the law or the prophets say "your eye shall not pity," they are acknowledging that this impulse naturally arises and must be consciously overridden in judicial contexts. This makes the term a window into the default orientation of the inner person toward those in need — compassion as the natural state that judgment suspends.
> 
> Session C check:* Section 3 annotations for both groups confirmed accurate. Section 2 paragraph on judicial suspension confirmed and deepened by the frequency observation above.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=263 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD004'
- Cross-registry: 98
- Raised: '2026-04-12'  ·  Session target: 'D'

> The high frequency of chus in judicial-prohibition contexts (Deut, Ezek) reveals a structural relationship between compassion and justice in the inner life: the default orientation is toward sparing; justice requires the deliberate overriding of that default. This is a programme-level observation about the architecture of the moral inner life. Connects to Justice (Reg 98), Guilt (Reg 73), and potentially Conscience (Reg 26). Question for Session D: does the inner life have a default orientation toward compassion that other moral demands must actively override, and if so, what does this reveal about the programme's understanding of the moral constitution of the human person?
> 
> ---
> 
> #### Term 5: H2551 chem.lah — compassion (occ=2, extracted_thin)
> *Sense structure: The related-words are to spare (H2550 cha.mal) and compassion — confirming this term sits in the sparing/mercy semantic space. Two verses: Gen 19:16 (God's mercy toward Lot despite his lingering) and Isa 63:9 ("in his love and in his pity he redeemed them"). Isa 63:9 is significant — chem.lah appears alongside divine love (ahavah) as the motivating disposition of God's redemptive act.
> 
> Semantic observation: Chem.lah (compassion/pity) and cha.mal (to spare) share a root that emphasises restraint on behalf of the other* — the withholding of force or judgment in response to need. This is compassion expressed not as emotional movement but as mercy-in-action.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=264 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD005'
- Cross-registry: 103
- Raised: '2026-04-12'  ·  Session target: 'D'

> Isa 63:9 names ahavah (love) and chem.lah (pity/compassion) together as co-motivating God's redemption. This is a direct verse-level co-occurrence of Love (Reg 103) and Compassion (Reg 23) vocabularies within a single clause about divine inner motivation for salvation. Raise: the inner architecture of divine redemption — what roles do love and compassion play distinctly, and do they always appear together? Cross-registry: Love (Reg 103), shared anchor verse candidate.
> 
> ---
> 
> #### Term 6: H2587 chan.nun — gracious (occ=13, extracted)
> *Sense structure: Adjective; used almost exclusively as a divine epithet. Status note: "guilt resolution vocabulary." The related words are: beauty (chin), favour (chen), for nothing (chinam), be gracious (chanan), be loathsome (H2603B), supplication (techinah), Tower of Hananel. The term describes the settled character quality of graciousness — not a momentary act but an attribute. Exod 34:6 is the defining verse: rachum ve-channum ("merciful and gracious") as paired divine attributes.
> 
> Semantic observation: Chan.nun (gracious) describes the character disposition from which compassion flows — the inner quality of being inclined toward favour. It is related to chen (favour/grace) through the root chanan (to be gracious). This root family bridges Compassion (Reg 23) and Grace (Reg 68): channum names God's character as gracious; chen names the favour that flows from it.
> 
> Sense tension: Status note says "guilt resolution vocabulary" — this positions graciousness as the response to guilt. But the Exod 34:6 usage is a divine character declaration unprompted by guilt. The "guilt resolution" frame applies to many instances of grace/graciousness, not to the term's primary semantic content.
> 
> Session C check:* Section 4 description of H2587 confirmed accurate.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=265 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD006'
- Cross-registry: 68
- Raised: '2026-04-12'  ·  Session target: 'D'

> Chan.nun (gracious, Reg 23) and chen (favour/grace, XREF in Reg 23, OWNER in Reg 68 Grace) share the same Hebrew root (חנן — the CHIN/CHEN root code collision noted in Stage 1). Exod 34:6 is a shared anchor verse for Reg 23 and Reg 68. The question: is graciousness (the character quality, channum) distinct from grace (the relational gift, chen), and if so, where does the inner-being boundary lie between them? This is the most direct compassion/grace boundary question in the programme.
> 
> ---
> 
> #### Term 7: H2594 cha.ni.nah — favour (occ=1, extracted_thin)
> *Sense structure: Single occurrence: Jer 16:13. The verse is a divine judgment speech — "I will hurl you out of this land into a land that neither you nor your fathers have known, and there you shall serve other gods day and night, for I will show you no favour (cha.ni.nah)." The term names the withdrawing of divine favour as judicial consequence. Same root as chan.nun and chen. The term occurs once in a context of its absence — like H2617B che.sed (shame), which is another register of chesed absence.
> 
> Semantic observation: This is the noun form of the gracious-favour vocabulary. Its single occurrence in a withdrawal-of-favour context mirrors the pattern seen in H2347 chus (pity mostly appearing in prohibition contexts) and H2617B che.sed (shame as the negative pole of chesed). The compassion vocabulary defines itself in part through naming its own absence and its judicial withdrawal.
> 
> ---
> 
> #### Term 8: H2616A cha.sad — be kind (occ=2, extracted_thin)
> Sense structure: The verbal form of the chesed root. Two occurrences, both the identical verse: 2 Sam 22:26 = Ps 18:25 ("With the merciful you show yourself merciful"). The hitpael form (hitchasad) means "to act kindly/show kindness toward." The verse establishes the mirror principle: God responds in kind to the inner disposition the person brings.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=266 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD007'
- Raised: '2026-04-12'  ·  Session target: 'D'

> The Divine-Human Correspondence principle embedded in 2 Sam 22:26 / Ps 18:25 operates across multiple inner-being characteristics simultaneously (merciful, blameless, pure, crooked — v.26-27). The programme should examine whether this mirroring principle is a general structural feature of the divine-human relationship visible across multiple registries, or specific to certain characteristics. Cross-registry candidates: Faithfulness (Reg 60), Blamelessness (Reg 14), Purity (Reg 125), Integrity (Reg 92).
> 
> ---
> 
> #### Term 9: H2617B che.sed — shame (occ=3, extracted_thin; 169 verses in export)
> *Sense structure: This is the negative semantic pole of the chesed root. The status note confirms: "the semantic range of chesed includes disgrace as its opposite pole." Three occurrences in the verses carrying this sub-gloss. The related words name the full root range: be kind, to shame, kindness — the positive form, its verbal cognate of shaming, and the primary positive noun.
> 
> Critical observation: H2617B appears here because chesed can mean both "steadfast love/kindness" and "shame/disgrace" depending on context and vocalisation — a semantic paradox documented in the CHASAD root flag. The 169 verses in the export are the full chesed corpus (H2617A is the XREF term owned by Reg 99/104; H2617B is this registry's OWNER term carrying the shame/negative-pole sense). This means the compassion registry carries the negative semantic pole of one of Israel's most theologically weighty words.
> 
> Session C check:* Sections 1-4 address this correctly. The CHASAD root paradox is accurately noted.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=267 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD008'
- Cross-registry: 146
- Raised: '2026-04-12'  ·  Session target: 'D'

> The CHASAD root (Reg 23 H2617B shame vs Reg 146 shame) and the CHASAD root (Reg 23 H2616A be kind) cross two clusters — C17 (compassion, love, mercy) and C06 (shame, contempt). The question for Session D: does the root-level connection between chesed (steadfast love) and shame reflect a genuine semantic relationship — that the violation of covenantal faithfulness produces shame as its consequence — or is this purely a lexicographic artefact? If genuine, it suggests the inner experience of shame is structurally connected to the failure of chesed in a way the programme should explore.
> 
> ---
> 
> #### Term 10: H5150 ni.chum — comfort (occ=3, extracted)
> *Sense structure: Noun from the na.cham root (to comfort/relent). Three verses: Isa 57:18 (divine comfort restored to the straying); Hos 11:8 (divine compassion "grows warm and tender" — ni.chumay nikmeru, "my compassions are kindled"); Zec 1:13 ("gracious and comforting words"). The term names the compassionate warmth that produces comfort — the inner stirring that precedes and motivates the comforting act.
> 
> Semantic observation: Ni.chum sits at the intersection of compassion and comfort. It is not comfort as consolation-received but compassion as the motivating warmth from which comfort flows. Hos 11:8 is the key verse: the divine inner life stirs with ni.chum in response to the prospect of judgment — this stirring overrides the judicial decision. The term names the felt, warm, visceral quality of compassion at the moment it becomes action.
> 
> Session B finding DIM-23-001 engaged: The Dimension Review finding asked whether ni.chum, splanchnizō, and ra.cham share a sub-pattern of "visceral inner movement" terms. Pass 1 confirms this: all three name compassion as a bodily movement from within — warm kindling (ni.chum), gut-stirring (splanchnizō), womb-love (ra.cham). This sub-pattern spans the divine-human boundary: God's compassion and human compassion are described with the same visceral language.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=268 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD009'
- Cross-registry: 111
- Raised: '2026-04-12'  ·  Session target: 'D'

> Rom 9:15 pairs eleeō (mercy, Reg 111) and oikteirō (compassion, Reg 23) as parallel verbs of divine sovereign freedom. The pairing raises the question: are mercy and compassion distinguishable in this verse, or is the parallelism purely rhetorical? The answer to this question is one of the most direct tests of whether Reg 23 and Reg 111 are genuinely separable characteristics.
> 
> ---
> 
> #### Term 13: G4697 splanchnizō — to pity / be moved in the gut (occ=12, extracted)
> *Sense structure: Mounce: "to have compassion on, have pity on." LSJ: the verb appears in LXX and NT. Status note: "the compassion-movement verb — Jesus 'moved with compassion' in Matt 9:36, 14:14, 15:32, 20:34; Mark 1:41, 6:34, 8:2; Luke 7:13, 10:33, 15:20." SEMANTIC_RANGE_BREADTH flag present.
> 
> From verse corpus: 12 occurrences — all Gospels. The objects of the splanchnizō movement are: the multitude (sheep without a shepherd — Matt 9:36); crowds needing food (Matt 15:32; Mark 8:2); two blind men (Matt 20:34); a leper (Mark 1:41); the disciples' unbelief context (Mark 6:34); the widow of Nain's grief (Luke 7:13); the Samaritan toward the wounded man (Luke 10:33 — the only human subject outside the parables); the father of the prodigal (Luke 15:20); the king toward the servant (Matt 18:27 — the parable).
> 
> Semantic breadth — four domains identified (SEMANTIC_RANGE_BREADTH flag):
> 1. Compassion toward physical suffering or need — healing miracles (Matt 20:34; Mark 1:41; Luke 7:13)
> 2. Compassion toward spiritual destitution — "sheep without a shepherd" (Matt 9:36; Mark 6:34)
> 3. Compassion toward physical hunger — crowds without food (Matt 15:32; Mark 8:2)
> 4. Compassion in relational/moral context — parable of prodigal (Luke 15:20), unforgiving servant (Matt 18:27), Good Samaritan (Luke 10:33)
> 
> Critical observation: The SEMANTIC_RANGE_BREADTH flag is fully justified.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=269 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD010'
- Cross-registry: 99
- Raised: '2026-04-12'  ·  Session target: 'D'

> Luke 10:33 — the Good Samaritan is splanchnizō toward the wounded man. This is the only unambiguous human use of the term outside parables. The verse connects compassion directly to the question "who is my neighbour?" — making compassion the defining quality of the one who correctly answers that question. This connects to Love (Reg 103 — "love your neighbour") and potentially Mercy (Reg 111 — "go and do likewise" in v.37 uses eleos). The structural observation: compassion (splanchnizō) generates mercy (eleos) in Luke 10:33-37 — the inward movement produces the outward act. This sequence matters for Session D.
> 
> ---
> 
> #### Term 14: G4834 sumpatheō — to sympathise (occ=2, extracted)
> *Sense structure: Two occurrences: Heb 4:15 (Christ sympathising with our weaknesses) and Heb 10:34 ("you had compassion on those in prison"). The verb names entering into another's experience — literally "suffering-with." LSJ first meaning: "to be sympathetically affected, to have the same thing happen to one"; notes the classical philosophical use of the soul and body sympathising with each other.
> 
> Semantic observation:* The classical philosophical usage (soul-body sympatheia) is significant for the spirit-soul-body classification work in Pass 4. The term originated in Stoic philosophy to describe the interconnection of parts of a whole — the way the wellbeing of one part affects all others. The NT reappropriates this concept for the community of faith and for Christology.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=270 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD011'
- Raised: '2026-04-12'  ·  Session target: 'D'

> The classical sumpatheō (soul and body sympathise with each other, Aristotle) is imported into NT anthropology as the ground of Christian community. This raises a programme-level question: does the NT use of sym- compounds (sumpatheō, sumpaschō) draw on Greek philosophical anthropology about the unity of the person, and does this inform the programme's spirit-soul-body framework? Cross-registry: potentially Soul (Reg 182), Spirit (Reg 184), the whole C01 cluster.
> 
> ---
> 
> #### Term 15: G4835 sumpathēs — sympathetic (occ=1, extracted_thin)
> *Sense structure: Adjective form. Single occurrence: 1 Pet 3:8. LSJ notes: "affected by like feelings, sympathetic" — with classical examples citing the greater sympathy of mothers for their children. The term describes the settled character quality of being capable of fellow-feeling, not a momentary act of it.
> 
> Semantic observation: The adjectival form establishes sympatheia as a character trait — the person who is sumpathēs is consistently responsive to others' suffering. 1 Pet 3:8 places it in a list of community virtues: unity of mind, sympathy, brotherly love, tender heart, humble mind. This is the community portrait — sympathy as one thread in the fabric of the new humanity.
> 
> ---
> 
> #### Term 16: G4841 sumpaschō — to suffer with (occ=3, extracted_thin)
> Sense structure: 1 Cor 12:26 (the body suffers together), Rom 8:17 ("if children, then heirs — heirs of God and fellow heirs with Christ, provided we suffer with him"), and one other occurrence. LSJ: "have the same thing happen to one; to be affected in common with."
> 
> Semantic observation: Sumpaschō* has two distinct usages: (a) mutual suffering within the body of Christ (1 Cor 12:26 — the ontological suffering-together that is a property of membership in the body); (b) sharing in Christ's sufferings as the condition of sharing in his glory (Rom 8:17 — the eschatological frame).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=271 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD012'
- Cross-registry: 55
- Raised: '2026-04-12'  ·  Session target: 'D'

> Rom 8:17 — "if we suffer with him (sumpaschō) we may also be glorified with him (syndoxazō)" — places fellow-suffering within an eschatological framework. Suffering-with-Christ is the condition of glorification-with-Christ. This connects Compassion/suffering-with vocabulary (Reg 23) to the Endurance (Reg 55), Surrender (Reg 156), and potentially Hope (Reg 78) registries. The eschatological dimension of compassion — suffering-with as the path to glory — is not addressed in Session C and should be incorporated in Stage 3.
> 
> ---
> 
> #### Term 17: G3356 metriopatheō — be gentle / moderate feeling (occ=1, extracted_thin)
> *Sense structure: Heb 5:2. Mounce: "to deal gently." LSJ: "feel moderately, bear reasonably with the ignorant and wayward." The Stoic term for metriopatheia names the philosophical ideal of moderating the passions — neither suppressing them (apatheia) nor being ruled by them. In Heb 5:2 the term is given a new ground: the high priest can moderate his response because he shares human weakness, not because he has mastered the passions philosophically.
> 
> Semantic observation:* This is compassion shaped by wisdom rather than compassion as raw feeling. It introduces the distinction between compassion's motivational force and its expression — calibrated, moderate, appropriate. The scriptural reframing grounds this moderation in shared vulnerability rather than philosophical self-mastery, which is a significant divergence from the Stoic usage.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=272 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD013'
- Raised: '2026-04-12'  ·  Session target: 'D'

> Metriopatheō (Reg 23) draws from Stoic metriopatheia — a deliberate philosophical distance from the Hebrew womb/visceral model. The contrast between these two models of compassion (Stoic moderate feeling vs Hebrew bodily movement) may be significant for the programme's understanding of how Greek and Hebrew anthropologies interact in the NT. Cross-registry: potentially Patience (Reg 116), Self-Control (Reg 142), Gentleness (Reg 66).
> 
> ---
> 
> #### Term 18: G4184 polusplanchnos — very compassionate (occ=1, extracted_thin)
> *Sense structure: NT hapax legomenon — appears only in Jas 5:11. Compound: polus (much/many) + splanchnon (bowels/entrails/compassion). Mounce: "compassionate." LSJ: "of great mercy." The intensifying compound makes explicit what the SPLANCHN root already implies: God is full of the visceral compassion movement. The context is suffering and endurance (Job's patience; the Lord's telos).
> 
> Semantic observation: The use of a compound hapax for this single statement signals that the writer needed a stronger term than the existing vocabulary supplied. Polusplanchnos* — intensely, deeply compassionate — is coined for the moment when God's compassion needs to be named as something beyond the ordinary range of the word. This intensification in the context of Job's suffering is theologically significant: God's deep compassion is announced at the point of maximum permitted suffering.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=273 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD014'
- Cross-registry: 214
- Raised: '2026-04-12'  ·  Session target: 'D'

> Jas 5:11 holds in tension God's deep compassion (polusplanchnos) with God's permitted suffering (Job's endurance). The verse does not resolve the tension — it holds both. This is the clearest instance in the programme data where compassion and suffering are explicitly co-present as divine attributes/actions. Cross-registry: Suffering (Reg 214), Endurance (Reg 55). Question for Session D: does the programme data reveal a structural relationship between divine compassion and divinely-permitted suffering?
> 
> ---
> 
> #### Term 19: G1652 eleeinos — pitiful (occ=2, extracted_thin)
> *Sense structure: Rev 3:17 (the Laodiceans are pitiable — eleeinos — without knowing it) and 1 Cor 15:19 ("if in Christ we have hope in this life only, we are of all people most to be pitied"). The term names the condition that calls forth compassion — not compassion itself but its proper object. The pitiable condition may be physical (1 Cor 15:19 — life without resurrection hope) or spiritual (Rev 3:17 — self-deceived prosperity).
> 
> Semantic observation: Eleeinos reveals compassion's counterpart: the pitiable condition is the one that ought* to evoke compassion. Rev 3:17 is particularly sharp — the Laodiceans cannot receive the compassion they need because they cannot perceive their own pitiable condition. Compassion requires both the disposition (in the giver) and the recognition of need (in the receiver or an observer). The word names the failure of the second condition.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=274 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD015'
- Cross-registry: 44
- Raised: '2026-04-12'  ·  Session target: 'D'

> Rev 3:17 — the pitiable condition (eleeinos) masked by prosperity — connects to Despair (Reg 44), Shame (Reg 146), and potentially Pride/Boastfulness (Reg 123). The verse shows that the inner condition requiring compassion can be concealed from the person who most needs it. This has implications for the programme's understanding of self-knowledge and the conditions under which compassion becomes operative.
> 
> ---
> 
> #### Term 20: G1654 eleēmosunē — charity/almsgiving (occ=36, extracted_thin)
> *Sense structure: The noun naming compassion made concrete in giving. Two groups: group 3167-001 (almsgiving as outward expression of inward mercy disposition). Mounce: "gift to the poor, alms, charitable gift." LSJ traces the semantic development: classical Greek pity/mercy → LXX almsgiving/charitable giving → NT acts of generosity to those in need. The word represents compassion arriving at its outward form — the inner disposition externalised as gift.
> 
> Semantic observation: The semantic development from pity (classical) to almsgiving (LXX/NT) is significant: it shows how the inner characteristic of compassion was understood in Second Temple Judaism and early Christianity to have a normative outward form. Compassion that does not give alms has not fully arrived. Matt 6:2-4 and Luke 11:41 both address the manner* of almsgiving (not for public display; from inner purity) — establishing that the inner quality of compassion is what gives the outward act its validity.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=275 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD016'
- Cross-registry: 111
- Raised: '2026-04-12'  ·  Session target: 'D'

> Eleēmosunē (Reg 23) represents the outer form of eleos (mercy, Reg 111) and splanchnizō (inner movement, Reg 23). The sequence: inner movement → mercy disposition → concrete act of giving. The programme data may support a model of compassion as a three-stage movement (visceral stirring → mercy orientation → outward gift) that could be a Session D finding. Cross-registry: Mercy (Reg 111), Generosity (Reg 65).
> 
> ---
> 
> ### PASS 1 — SUMMARY AND SESSION C CHECKS
> 
> *Primary sense structure confirmed: The compassion vocabulary divides into four root families with distinct but related semantic territory:
> 1. RACHAM/SPLANCHN — visceral, somatic, movement-compassion (womb/bowels origin)
> 2. CHESED/CHANNUM — covenantal, characterological, steadfast compassion (loyalty/faithfulness)
> 3. SYM-PATH — participatory, solidarity compassion (shared-suffering/fellow-feeling)
> 4. ELEEIN/CHUS — relational, responsive compassion (pity/mercy/almsgiving)
> 
> Sense tensions identified:
> - H2617B che.sed carries both the positive peak (steadfast love) and negative pole (shame) of covenantal character. The positive content belongs to XREF terms (Reg 99/104); what remains as OWNER in Reg 23 is partly the shame/disgrace pole.
> - H2347 chus appears most in judicial-prohibition contexts — compassion is defined partly by where it is suspended.
> - G4697 splanchnizō spans four semantic domains — not a narrow technical term but the most versatile compassion verb in the Gospels.
> 
> meaning_numbered gaps: All Hebrew active OWNER terms lack meaning/meaning_numbered fields. All Greek terms except H2587 group lack meaning fields; Greek terms have Mounce short_def. These are extraction gaps. Note for Pass 5.
> 
> Session D pointers raised this pass: SD-001 through SD-016. These will be verified and compiled in Pass 6.
> 
> Session C check results:
> - Sections 1 and 2: all major claims confirmed from verse and lexical evidence.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=276 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD017'
- Cross-registry: 68
- Raised: '2026-04-12'  ·  Session target: 'D'

> The Exod 34:6 formula (rachum ve-channum — merciful and gracious) names God's two core compassion attributes in a paired formula that is cited or echoed across the entire OT corpus (Neh 9:17; Ps 86:15; 103:8; 145:8; Joel 2:13; Jon 4:2). The programme has at least three registries anchored to this verse (Compassion reg 23, Grace reg 68, Mercy reg 111). Session D must determine whether Exod 34:6 functions as a unified theological statement about God's inner character that should be analysed as a whole, or whether its component parts (compassion, grace, patience, steadfast love, faithfulness) map independently to their respective registries.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=277 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD018'
- Raised: '2026-04-12'  ·  Session target: 'D'

> God's judicial withholding of compassion (H2347 chus in Ezek 7:4; H2594 cha.ni.nah in Jer 16:13) appears structurally alongside his active exercise of it (Jon 4:11; Gen 19:16). The inner-being question: what does the deliberate suspension of compassion reveal about its nature as a characteristic? Does it indicate that compassion is a disposition subject to governance by other attributes (justice, righteousness), or that it is a capacity that can be directed or withheld? Cross-registry: Justice (Reg 98), Righteousness (Reg 139), Anger/Wrath (Reg 4/178).
> 
> 
> ---
> 
> ### PASS 2 — Divine Dimension
> 
> *Date: 2026-04-11
> 
> #### God-as-Subject pattern by term
> 
> | Term | Divine verses / Total | Pattern |
> |---|---|---|
> | H2347 chus | ~14/24 | God primarily as the one who withholds pity in judgment (Ezek); also shows pity (Jon 4:11). Dominant: divine judicial withdrawal |
> | H2587 chan.nun | ~11/13 | Almost exclusively divine epithet. God as the gracious one. GOD_AS_SUBJECT flag warranted. |
> | H2617B che.sed | ~87/169 | Predominantly divine. God's steadfast love is primary referent across the Psalter, prophets, historical books. GOD_AS_SUBJECT flag warranted. |
> | H5150 ni.chum | 2/3 | Divine. God's compassionate comfort-movement. GOD_AS_SUBJECT flag warranted. |
> | H7356A ra.cham | 1/5 | The womb-metaphor verse (Isa 46:3) is divine. Anatomical uses are human. Partial. |
> | H7358 re.chem | ~9/25 | God as actor over the womb (opening, closing, consecrating). GOD_AS_SUBJECT flag warranted for these verses. |
> | H2551 chem.lah | 1/2 | Gen 19:16 — divine. GOD_AS_SUBJECT flag warranted. |
> | G3627 oikteirō | 1/1 | Rom 9:15 — exclusively divine sovereignty. GOD_AS_SUBJECT flag warranted. |
> | G4697 splanchnizō | ~3/12 | Jesus (God incarnate) as primary subject in Gospels. Human in one parable context (Lk 10:33). GOD_AS_SUBJECT flag warranted for Christological uses. |
> | G4184 polusplanchnos | 1/1 | Jas 5:11 — divine. GOD_AS_SUBJECT flag warranted.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=278 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD019'
- Cross-registry: 4
- Raised: '2026-04-12'  ·  Session target: 'D'

> Isa 54:8 — moment of anger vs everlasting chesed/racham — establishes a temporal asymmetry in divine inner-being: judgment is temporary, compassion is permanent. This directly addresses the question of which divine characteristic is more fundamental. Cross-registry: Anger (Reg 4), Love (Reg 103). The verse is a candidate for the C17 cluster synthesis anchor verse.
> 
> *G4697 splanchnizō — Mar 1:41 (non-anchor, somatic)
> "Moved with pity, he stretched out his hand and touched him." The compassion movement (splanchnizō*) is immediately followed by physical touch — Jesus reaches out and touches a leper (socially and ritually untouchable). The inner movement produces a boundary-crossing bodily act. This is the most direct example in the corpus of visceral compassion producing physical contact.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=279 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD020'
- Cross-registry: 125
- Raised: '2026-04-12'  ·  Session target: 'D'

> Mark 1:41 — compassion (splanchnizō) produces touch across the ritual-purity boundary. This connects compassion to purity/defilement vocabulary (Reg 125, Reg 41) in a structurally significant way: compassion overrides the inner orientation toward self-protection and social boundary-maintenance. Cross-registry: Purity (Reg 125), Defilement (Reg 41).
> 
> *H5150 ni.chum — Hos 11:8 (group 733-001)
> Session C annotation confirmed accurate and complete. Additional observation: the verse opens with four rhetorical questions — "How can I give you up? How can I hand you over? How can I make you like Admah? How can I treat you like Zeboiim?" — before naming the inner movement. The questions record God's inner deliberation between judgment and compassion. The ni.chum is not presented as the suppression of judgment but as the winning of an inner debate. This has significant implications for theological anthropology: the inner life of God (as the text presents it) is not static but deliberative.
> 
> FRAMEWORK SIGNAL noted: H5150 ni.chum / Hos 11:8 — the divine inner deliberation between judgment and compassion represents a unique category in the programme data: the dynamic quality of divine compassion, where it contends with and overcomes competing inner dispositions. This is relevant to the spirit-soul-body classification and to the session B finding DIM-23-001.
> 
> G4834 sumpatheō — Heb 10:34 (non-anchor)
> "You had compassion (sumpatheō) on those in prison, and you joyfully accepted the plundering of your property, since you knew that you yourselves had a better possession and an abiding one." This is the only NT verse where sumpatheō clearly has a human-to-human subject (the readers showing compassion to imprisoned believers). The compassion is expressed through material sacrifice and joy — not grief.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=280 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD021'
- Cross-registry: 212
- Raised: '2026-04-12'  ·  Session target: 'D'

> 11 shared terms including supplication vocabulary (H8467 techinah, H8469 tahanun, H2603A chanan). The supplication vocabulary sits at the intersection of compassion and prayer: the inner act of pleading for mercy assumes that God is compassionate. The structural relationship: compassion in the recipient (God) grounds the act of supplication in the petitioner. Cross-registry: Pray (Reg 212), Prayer (Reg 122), Intercession (Reg 94).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=281 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD022'
- Cross-registry: 59
- Raised: '2026-04-12'  ·  Session target: 'D'

> 6 shared terms and 37 co-occurrence verses. The chesed vocabulary and faith appear together extensively in the Psalter (Ps 25:10; 31:7; 33:18; 57:3; 62:12; 85:10). The structural question: does faith operate as the receptive capacity by which the compassion of God is appropriated? Ps 33:18 — "the eye of the Lord is on those who fear him, on those who hope in his steadfast love" — pairs fear/hope with chesed. Cross-registry: Faith (Reg 59), Hope (Reg 78), Trust (Reg 163).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=282 · flag_code=`SD_POINTER` · priority='LOW'

- Label: 'DIM-023-SD023'
- Cross-registry: 46
- Raised: '2026-04-12'  ·  Session target: 'D'

> 6 shared terms. Devotion (chasid — the devout/loyal person) is etymologically from the CHASAD root — the same root as chesed. The devout person is the one who embodies covenantal faithfulness. This is the human character-type whose inner quality mirrors divine chesed. Cross-registry: Devotion (Reg 46), Loyalty (Reg 104), Faithfulness (Reg 60).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=283 · flag_code=`SD_POINTER` · priority='LOW'

- Label: 'DIM-023-SD024'
- Cross-registry: 179
- Raised: '2026-04-12'  ·  Session target: 'D'

> 3 shared terms each. The RACHAM and CHESED vocabulary overlaps with the desire/yearning cluster (C04). The Hebrew chashaq (desire) and ta'avah (craving) may co-occur with compassion vocabulary in contexts of intimate longing. This connection warrants investigation: is the compassion vocabulary capable of describing yearning toward the beloved (erotic/devotional register), or does the overlap reflect purely vocabulary borrowing? Cross-registry: Yearning (Reg 179), Desire (Reg 43), Longing (Reg 102).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=284 · flag_code=`SD_POINTER` · priority='LOW'

- Label: 'DIM-023-SD025'
- Cross-registry: 117
- Raised: '2026-04-12'  ·  Session target: 'D'

> Co-occurrence (37, 21, 28 verses respectively). These cross-cluster connections (C17 compassion with C14 volitional characteristics) suggest that divine compassion and human surrender/will appear together in specific verse contexts — possibly the covenantal response pattern: God's compassion calls forth human submission/will/peace. Cross-registry: Peace (Reg 117), Surrender (Reg 156), Will (Reg 173).
> 
> *Root families (3):
> 
> | Root | Registries | Cross-cluster |
> |---|---|---|
> | RACHAM | 103 (love), 23 (compassion) | No — both C17 |
> | CHASAD | 146 (shame), 23 (compassion) | Yes — C06/C17 |
> | ATAR | 111 (mercy), 23 (compassion) | No — both C17 |
> 
> All three covered in existing pointers (SD-001, SD-008, Stage 1 notes).
> 
> Shared anchor verses (34 entries):*
> 
> Key registries with shared anchors:
> - Love (103): 6 shared anchors
> - Mercy (111): 3 shared anchors
> - Mind (112): 2 shared anchors
> - Anger (4): 2 shared anchors
> - Patience (116): 2 shared anchors
> - Faith (59): 2 shared anchors
> - Calling (19): 2 shared anchors

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=285 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-023-SD026'
- Cross-registry: 4
- Raised: '2026-04-12'  ·  Session target: 'D'

> 2 shared anchor verses with Anger (Reg 4). Isa 54:8 names the temporal contrast between a moment of anger and everlasting chesed/racham (SD-019 already raised). The shared anchor with Anger confirms this is not an incidental pairing — the inner-being boundary between anger and compassion in the divine character is structurally significant. Cross-registry: Anger (Reg 4). Already partially covered by SD-019.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=286 · flag_code=`SD_POINTER` · priority='LOW'

- Label: 'DIM-023-SD027'
- Cross-registry: 116
- Raised: '2026-04-12'  ·  Session target: 'D'

> 2 shared anchors each. Patience (Reg 116) shares anchors — the connection likely runs through Jas 5:11 (polusplanchnos + Job's patience). Calling (Reg 19) shares anchors — likely through Jer 1:5 (womb → calling) and Isa 46:3 (carried from womb → sustained). The womb vocabulary creates a structural link between compassion and divine calling/vocation. Cross-registry: Calling (Reg 19), Patience (Reg 116).
> 
> #### Connection summary for Session C Section 5 update
> 
> *All existing Section 5 connections confirmed by signal data:
> Mercy (111) — xref/cooc/root/shared_anchor → HIGH ✓
> Love (103) — xref/cooc/root/shared_anchor → HIGH ✓
> Grace (68) — xref/cooc → HIGH ✓
> Kindness (99) — xref/cooc/dim → HIGH ✓
> Comfort (192) — xref → HIGH ✓
> Repentance (135) — xref → MEDIUM ✓
> Guilt (73) — xref/cooc → MEDIUM ✓
> Pray (212) — xref → MEDIUM (was not in Section 5 — add)
> Shame (146) — xref/root → MEDIUM ✓
> Passion (115) — xref → MEDIUM ✓
> Desire (43) — xref/cooc → LOWER ✓
> Yearning (179) — xref → LOWER ✓
> Faith (59) — xref/cooc/shared_anchor → LOWER → should be MEDIUM (37 co-occurrence)
> Peace (117) — cooc → LOWER ✓
> Loyalty (104) — xref → LOWER ✓
> Heart (183) — xref/shared_anchor → LOWER ✓
> Sorrow (151) — xref/shared_anchor → LOWER ✓
> 
> New connections to add to Section 5:
> - Devotion (46): xref (6 terms, CHASAD root) — LOWER
> - Suffering (214): NOT IN CORRELATION SIGNAL (registry just created, no correlation data yet) — INFERENTIAL, flag explicitly
> - Anger (4): shared_anchor (2), verse co-occurrence — LOWER/MEDIUM
> - Calling (19): shared_anchor (2) — LOWER
> - Patience (116): shared_anchor (2) — LOWER
> 
> SB-13 integrity check:* Session D pointers were raised across Passes 1–4 (SD-001 to SD-020) and Pass 6 (SD-021 to SD-027). Pass 6 was not the primary generating pass — confirmed. SB-13 satisfied.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=287 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD028'
- Cross-registry: 111
- Raised: '2026-04-12'  ·  Session target: 'D'

> The five-stage divine pattern (character → act → withdrawal → demand → correspondence) is a structural observation about how the compassion vocabulary maps the divine-human relationship. The question for Session D: is this five-stage pattern specific to compassion, or does it operate across the whole compassion/mercy/grace cluster (Reg 23, 68, 111)? If it is a cluster-level pattern, it is a significant finding for the C17 synthesis.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=288 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-023-SD029'
- Cross-registry: 135
- Raised: '2026-04-12'  ·  Session target: 'D'

> Joel 2:13 — "rend your hearts and not your garments. Return to the LORD your God, for he is gracious (channum) and merciful (rachum)..." — the divine character formula (Exod 34:6 echo) appears as the ground for a call to repentance. This verse links divine compassion directly to human repentance and to the inner act of heart-rending. Cross-registry: Repentance (Reg 135), Heart (Reg 183), Contrition (Reg 30).
> 
> ---
> 
> ### PASS 3 — Verse Annotations
> 
> *Date: 2026-04-11
> 
> Pass 3 produces structured annotations for all OWNER anchor verses. These build on the Session C annotations (which were written from the same verse data) and add the analytical depth from Passes 1–2.
> 
> Annotation additions / corrections to Session C Section 3:
> 
> H2347 chus — Jon 4:11 (group 3182-001)
> Session C annotation accurate. Addition: Jon 4:10 (not an anchor but contextually essential) shows Jonah pitying the plant (chus) — the same verb used in v.11 of God's pity for Nineveh. The rhetorical force depends on the parallelism: you pity the plant without moral basis; should I not pity 120,000 people? The verse establishes that chus can operate in morally trivial cases (plant) and morally weighty cases (city), and it is the same inner movement in both.
> 
> H2347 chus — Ezek 7:4 (group 3182-002)
> Additional observation from full verse scan: the phrase "my eye will not spare, nor will I have pity" (chus) appears seven times in Ezekiel (5:11; 7:4,9; 8:18; 9:5,10; 20:17 — the last being the exception where God does spare). This repetition in one prophetic book is not random. It creates a cumulative effect: the withdrawal of divine pity is presented as a weighty, deliberate, repeated act — not a single judicial decision but a sustained posture. God names his own pity-withdrawal in the first person repeatedly, which means the compassion being suspended was real and felt.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=505 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-001'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T0.2.2 (Created Purpose) — status S, notation: Gap identified.
> 
> Prompt: Does the evidence indicate whether this characteristic is part of the original created design, a response to the fallen condition, or both?
> 
> AI response excerpt: The data is silent on this question directly. No verse in the evidence base addresses whether compassion belongs to the original created design or is a response to the conditions introduced by the fall.
> 
> An observation can be made — carefully distinguished as interpretation, not data: the RACHAM root is anatomical (womb), and the womb-vocabulary is used for God's care of Israel "from before your b

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=506 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-002'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T1.3.3 (Boundary) — status P, notation: Gap identified.
> 
> Prompt: What is this characteristic not — where does it end and something else begin?
> 
> AI response excerpt: The data provides boundary observations but the formal distinction work between compassion and its nearest adjacent characteristics is explicitly deferred to Session D across multiple SD pointers.
> 
> **What the data establishes:**
> 
> Compassion is not mercy (eleos/eleeō), though they are closely related. SD-009 raises the question directly: Rom 9:15 pairs oikteirō (compassion) and eleeō (mercy) as par

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=507 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-003'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T1.6.3 (Sustained Effect) — status P, notation: Gap identified.
> 
> Prompt: Does the sustained effect differ from the immediate response — and if so, how?
> 
> AI response excerpt: The data implies a difference but does not state it explicitly.
> 
> The immediate response in the giver is a somatic event (splanchnizō — a movement). The sustained effect in the giver appears to be a character quality (ra.chum, sumpathēs — a settled disposition). The difference between these is the difference between an inner-being event and an inner-being state. The vocabulary differentiates them (

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=508 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-004'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T2.1.1 (Spirit-Level Location) — status S, notation: Gap identified.
> 
> Prompt: Is this characteristic explicitly located at the spirit level in the verse evidence?
> 
> AI response excerpt: The data does not contain a verse that explicitly locates compassion at the spirit level using spirit (ruach/pneuma) language. The vocabulary is consistently anchored in the womb (re.chem/ra.cham), the entrails (splanchnon/splanchnizō), the heart (lev — Hos 11:8: "my heart recoils within me"), and the soul-level character vocabulary (chesed, channum). None of the anchor verses or group description

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=509 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-005'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T2.1.2 (Spirit-Level Location) — status S, notation: Gap identified.
> 
> Prompt: Does the evidence indicate that this characteristic originates in or is primarily a spirit-level phenomenon?
> 
> AI response excerpt: The data does not address origin at the spirit level. The originating language is somatic (womb, entrails) and relational-covenantal (chesed, channum). The registry's sb_classification is Soul-body interface — which positions compassion below the spirit level in the programme's constitutional framework. No term analysis, group description, or SD pointer addresses spirit-level origination.
> 
> This is

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=510 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-006'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T2.1.3 (Spirit-Level Location) — status S, notation: Gap identified.
> 
> Prompt: What does spirit-level location reveal about the nature and depth of this characteristic?
> 
> AI response excerpt: Since the evidence does not establish spirit-level location, this prompt cannot be answered from the data. The silence is noted. If Session D synthesis were to identify a spirit-level dimension of compassion — for example, through the cross-boundary and boundary-crossing pattern of splanchnizō — it would significantly deepen the constitutional analysis. That question is properly deferred.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=511 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-007'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T2.8.3 (Body — Deposit) — status P, notation: Gap identified.
> 
> Prompt: If the evidence is silent, note this explicitly. This finding feeds directly into T5.7.
> 
> AI response excerpt: The evidence is not fully silent — the womb etymology and the Exod 34:6 generational frame create partial signals — but direct evidence of a constitutional body deposit is absent. T5.7 will be handled as a partial/conditional finding: the womb-related generational dimension will be noted, but no deposit will be affirmed as established from the data. The question is a genuine gap for Session D.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=512 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-008'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T3.5.1 (Creativity) — status S, notation: Gap identified.
> 
> Prompt: Does this characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how?
> 
> AI response excerpt: The data does not contain evidence that directly connects compassion to the creative faculty or to imagination. No verse or term analysis addresses creativity, imagination, or origination in the context of compassion.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=513 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-009'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T3.5.2 (Creativity) — status S, notation: Gap identified.
> 
> Prompt: Does this characteristic enable, deepen, bypass, or impair creativity in the person?
> 
> AI response excerpt: The data is silent on this question. An interpretive observation can be made — carefully flagged as inference, not data: the capacity to enter genuinely into another's experience (sumpatheō, sumpaschō) may involve imaginative engagement — the inner act of envisioning what the other is experiencing from the inside. If so, compassion would engage imagination as a co-operating faculty. However, the d

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=514 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-010'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T3.5.3 (Creativity) — status S, notation: Gap identified.
> 
> Prompt: What does the pattern of engagement or non-engagement with creativity reveal about the nature of this characteristic?
> 
> AI response excerpt: The silence on creativity is itself informative: compassion in the biblical vocabulary is grounded in perception (sight of suffering), affect (gut-movement), and relational action — not in imagination or creative origination. The characteristic's operation does not require the creative generation of new realities; it requires the responsive engagement with the reality of another's suffering that i

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=515 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-011'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T4.4.4 (Human Interface — Receiving) — status P, notation: Gap identified.
> 
> Prompt: If the evidence is silent on the receiving direction, note this explicitly.
> 
> AI response excerpt: The receiving direction is partially evidenced (outer acts of compassion reach the recipient and produce material change) but the inner-being dynamics of reception are largely silent. The gap is specifically in the interior experience of the receiver — what happens inside the person at the moment compassion reaches them. This is the programme's most significant unaddressed question for this regist

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=516 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-012'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T4.6.1 (Spiritual Beings Interface) — status S, notation: Gap identified.
> 
> Prompt: Does the verse evidence show this characteristic operating in relation to other spiritual beings — angelic or adversarial — and if so, how?
> 
> AI response excerpt: The data does not contain evidence of compassion operating in relation to angelic beings as subjects or recipients. The spiritual beings interface is entirely absent from the verse evidence and the term analyses. No group description, anchor verse, SD pointer, or term analysis raises the angelic or adversarial dimension in relation to compassion.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=517 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-013'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T4.6.2 (Spiritual Beings Interface) — status S, notation: Gap identified.
> 
> Prompt: Is this characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial spiritual powers?
> 
> AI response excerpt: The data is silent on this question. An observation can be made — carefully flagged as inference, not data: the Lam 4:10 evidence (compassionate women violating their compassion under siege) and the judicial-hardening pattern (the eye trained not to pity) show that compassion can be overwhelmed by external pressure and suppressed by internal orientation. Whether adversarial spiritual powers are im

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=518 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-014'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T4.6.3 (Spiritual Beings Interface) — status S, notation: Gap identified.
> 
> Prompt: Is this characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?
> 
> AI response excerpt: The data is silent on angelic mediation of compassion. No verse in the evidence base connects angelic ministry to the communication or strengthening of compassion. This silence is noted explicitly.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=519 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-015'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T4.6.4 (Spiritual Beings Interface) — status S, notation: Consistent with prior analysis.
> 
> Prompt: If the evidence is silent on the spiritual beings interface, note this explicitly.
> 
> AI response excerpt: The spiritual beings interface is entirely silent across all three prompts. This is consistent with the pattern noted in the instruction for T4.6 — this component is frequently silent in the registry data. The silence is complete and is noted. The gap is new and is not covered by any existing SD pointer.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=520 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-016'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T6.5.1 (Distinctions) — status P, notation: Gap identified.
> 
> Prompt: Which adjacent characteristic most closely resembles this one — and what precisely distinguishes them?
> 
> AI response excerpt: The data identifies mercy (R111) as the most closely resembling adjacent characteristic, based on:
> - Direct XREF relationship (G1653, G1656, G3628 as XREF terms in R23)
> - Shared anchor verses (Rom 9:15, Jas 5:11, Num 6:25)
> - Co-occurrence of 76 shared verses
> - SD-009 naming this as the most direct test of whether R23 and R111 are genuinely separable
> 
> **What the data suggests about the distinction

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=521 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-017'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T6.5.2 (Distinctions) — status P, notation: Gap identified.
> 
> Prompt: Where the evidence shows apparent overlap, what is the precise boundary?
> 
> AI response excerpt: Three apparent overlaps are identified in the data, with their current boundary status:
> 
> **Compassion / mercy (R111):** The boundary is unresolved. Partial evidence suggests a sequential model (compassion generates mercy) but Rom 9:15 parallel usage challenges this. Deferred to Session D (SD-009).
> 
> **Compassion / love (R103):** The boundary is the programme's most structurally significant open que

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=522 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-018'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T6.7.1 (Dimensional Sharing) — status P, notation: Gap identified.
> 
> Prompt: How many of this characteristic's confirmed analytical dimensions are shared with another characteristic in the programme?
> 
> AI response excerpt: The registry header shows dimensions: None — the dimension field has not been populated in the database record. From the T1.8 analysis in this document, the dimensions assembled from the data are:
> 
> - Primary: Relational Disposition
> - Secondary: Emotion — Positive, Agency / Power, Vitality / Existence
> 
> These are analytical conclusions from this second-tier analysis, not database-confirmed entries.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=523 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-019'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T6.7.2 (Dimensional Sharing) — status P, notation: Gap identified.
> 
> Prompt: What does the pattern of dimensional sharing reveal about the relationship between this characteristic and those it shares dimensions with?
> 
> AI response excerpt: Without confirmed dimension data, the pattern cannot be formally stated. From the assembled analysis:
> 
> **If primary Relational Disposition is shared with love, mercy, and kindness (highly probable):** The dimensional sharing would confirm that compassion, love, mercy, and kindness are all expressions of the same primary constitutional orientation — toward the other in relationship. The distinction

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=524 · flag_code=`SB_FINDING` · priority='MEDIUM'

- Label: 'SB-023-T2-020'
- Raised: '2026-04-30T07:56:14Z'  ·  Session target: 'B'

> [Catalogue v2 gap surfaced 2026-04-30] T7.1.8 (Lexical and Semantic Analysis) — status P, notation: Gap identified.
> 
> Prompt: What does the LXX use of the vocabulary reveal about continuity or development of this characteristic across the Testaments?
> 
> AI response excerpt: The data package shows NO_WORD_ANALYSIS flag for 98 terms — indicating that detailed lexical analysis (including LXX usage) has not been completed for the majority of the vocabulary. The flag count of 98 out of 97 total terms (more than the term count, suggesting some flags apply at the group level) indicates a significant lexical analysis gap across the registry.
> 
> **What the data does provide (pa

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R051 distress — 2 unresolved

#### srf.id=686 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M02-BOUNDARY-H6696B'
- Strong's ref: `H6696B`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M02 closure (DIR-20260516-014): BOUNDARY term H6696B (tsur) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M02-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — H6696B tsur]. Pending researcher disposition: set-aside / promote-to-M02-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R51 (distress).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=687 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M02-BOUNDARY-H7379'
- Strong's ref: `H7379`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M02 closure (DIR-20260516-014): BOUNDARY term H7379 (riv) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M02-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — H7379 riv]. Pending researcher disposition: set-aside / promote-to-M02-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R51 (distress).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R108 meditation — 1 unresolved

#### srf.id=375 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'Inner-word / inner-speech dimension of meditation — does registry 108 capture the interior/exterior boundary of word and thought (hagah, siach)?'
- Strong's ref: `H1897; H7878; H7881; H1900; H1902H`
- Raised: '2026-04-25T00:00:00Z'  ·  Session target: 'D'

> Session D Investigation Prompt — Registry 108 (Meditation) — Inner Word / Inner Speech Dimension
> 
> During a pre-Session D exploratory discussion, the question was raised whether the Framework B programme adequately captures the concept of word / voice / speak / thought as phenomena that are at least partly located in the inner being, rather than being purely physical or communicative acts.
> 
> The discussion identified a convergence across three domains:
> 
> Biblical-theological: Hebrew dabar (דָּבָר) carries both word and reality/event, suggesting the spoken word is an extension of the speaker's inner being. Hebrew lev (heart) is the seat of inner speech and thought — "the heart says..." is a genuine idiom for interior thought-speech. Greek logos carries the Stoic distinction between logos endiathetos (inner word/reason) and logos prophorikos (uttered word). Augustine's verbum mentis (word of the mind) is his pre-linguistic inner word, located in the soul.
> 
> Philosophical: From Plato onward, thought is treated as inner dialogue — "the soul talking to itself." The logos endiathetos / prophorikos distinction runs from Stoics through Augustine and remains philosophically significant.
> 
> Psychological/cognitive: Inner speech is a well-established phenomenon (Vygotsky, modern neuroscience). It activates speech-production brain areas and is partly constitutive of conscious thought, not merely a report of it.
> 
> Programme gap identified: The programme has no dedicated registry for word, voice, speak, or logos. This is probably a principled scope decision — the programme covers inner states and dispositions, not communicative acts. However, the gap raises a specific question for Session D analysis of meditation (108, C02):
> 
> Does the meditation registry adequately capture the inner-speech dimension of its core terms — particularly הָגָה (hagah, to murmur/muse inwardly) and שִׂיחַ (siach, to muse/speak inwardly) — as terms that sit at the interior/exterior boundary of word and thought? Or does the registry treat these primarily as contemplative states, missing the inner-speech signal?
> 
> Specific investigation questions for Session D:
> 
> 1. Are הָגָה and שִׂיחַ present in the meditation term inventory, and are they glossed in a way that preserves their inner-speech quality?
> 2. Does the analysis distinguish meditation-as-inner-speech from meditation-as-quiet-reflection?
> 3. Is there any cross-reference to thought (160) or counsel (32) that picks up the inner-word dimension?
> 
> Note (registry-state observation, 2026-04-25): In the current registry-108 inventory, H1897 hagah ("to mutter") and H7878 siach verb ("to muse") are present as XREF terms — owned elsewhere — while the meditation nouns H1900 hagut, H1902H higgayon, and H7881 sichah are OWNER. The inner-speech verbs that most directly carry the interior/exterior-boundary signal are therefore not OWNER in 108. Session D may need to consider whether this ownership pattern is itself part of the gap: the meditation registry holds the noun-form contemplative-state terms while the action-form inner-speech verbs sit in their OWNER registries. Cross-registry ownership of H1897 and H7878 should be confirmed when this pointer is taken up.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

## §3. Session D term links

_(None — no `session_d_term_links` rows reference this cluster's terms.)_

---

## Output reconciliation document (AI authors this)

AI produces `Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-reconciliation-v1-{date}.md` carrying the dispositions and rationales per row.

Then CC executes the reconciliation directive `wa-cluster-{code}-dir-NNN-inherited-findings-reconcile-v1-{date}.md` per v2_0 §13.4.

*End of inherited-findings report.*