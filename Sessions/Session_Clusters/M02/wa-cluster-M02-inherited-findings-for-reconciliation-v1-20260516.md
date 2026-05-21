# M02 Anger, Wrath and Indignation — Inherited findings for Phase 10 reconciliation

**Generated:** 2026-05-16T15:13:27Z  
**Cluster:** `M02` (Anger) · status=Analysis - In Progress · version=v6  
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §13 (Phase 10 — Inherited-finding reconciliation)  
**Source:** `database/bible_research.db`  

**Scope:** every inherited Session B finding, research flag, and Session D pointer attached to this cluster's contributor registries that has **not been resolved** by the legacy pipeline. AI's Phase 10 task is to assign a disposition per row (see §13.2 of the instruction). Resolved rows (`status='resolved_*'` or `resolved=1`) are excluded.

**Linkage path:** cluster's `mti_terms` → `owning_registry_fk` → `word_registry` → matching rows in `wa_session_b_findings`, `wa_session_research_flags`, and `session_d_*`.

---

## Summary

| Source | Total unresolved |
|---|---:|
| `wa_session_b_findings` (status IN (open, pending, confirmed)) | **35** |
| `wa_session_research_flags` (resolved=0) | **53** |
| `session_d_term_links` (this cluster's terms) | **0** |

**Contributor registries:** 10

| no | registry_id | word |
|---:|---:|---|
| 1 | 1 | abomination |
| 3 | 3 | ambition |
| 4 | 4 | anger |
| 51 | 51 | distress |
| 56 | 56 | envy |
| 87 | 87 | indignation |
| 103 | 103 | love |
| 128 | 128 | rebellion |
| 152 | 152 | strife |
| 178 | 178 | wrath |

**Finding types in unresolved set:**

- `SYNTHESIS_INTER_TIER`: 21
- `DIMENSION_REVIEW`: 7
- `SYNTHESIS_INTRA_TIER`: 7

**Flag codes in unresolved set:**

- `SD_POINTER`: 40
- `BOUNDARY_DECISION_PENDING`: 4
- `VERSE_EVIDENCE_BREADTH_NOTE`: 3
- `PH2_CROSS_REGISTRY_REQUIRED`: 2
- `PH2_THEOLOGICAL_DEPTH_REQUIRED`: 2
- `PH2_DATA_QUALITY`: 1
- `DIMREVIEW_SESSION_D`: 1

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

### R056 envy — 1 unresolved

#### sbf.id=74 · finding_id='DIM-56-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Reg 56 (envy) holds the full positive-negative dual register of the zeal/jealousy vocabulary. The same inner passion (consuming zealous desire) appears as: (a) destructive human jealousy/envy (Affective/Emotional, Moral/Conscience), (b) positive human zeal for God (Spiritual/God-ward), (c) divine jealousy as exclusive covenantal claim (Theological/Divine-Human). The inner capacity is identical; direction of passion determines valence. Session B should map this tripartite structure and ask what makes the same inner passion sanctified or destructive.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R103 love — 30 unresolved

#### sbf.id=142 · finding_id='DIM-103-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-08'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.4-2026-04-08`

> The love registry spans the broadest relational vocabulary in the programme — agapē, phileō, chesed, and related terms — encompassing God's love for humanity (GOD dominant), human love toward God, mutual love among persons, and disordered love. Session B should map the full spectrum of love's inner-being architecture: what distinguishes the different forms, how they interrelate, and what the coexistence of eros/philia/agapē in the same registry reveals about the inner-being's capacity for love.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=171 · finding_id='DIM-103-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-11'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.9-2026-04-09`

> Group 535-001 (ye.di.dut — beloved of Gods soul, Reg 103) is anchored by Jer 12:7: I have given the beloved of my soul into the hands of her enemies. The phrase ye.di.dut nap.shi (beloved of my soul/nephesh) attributes an intimate inner-being category to God — God has a nephesh, and the beloved relationship is located there. This raises a significant inner-being question for Session B of Reg 103: does the love vocabulary of Reg 103 contain a sub-pattern of terms that attribute inner-being states to God with the same vocabulary used for human inner-being states? The terms ye.di.dut (beloved of my soul), ra.cha.mim (my heart yearns — Jer 31:20 in group 551-001), and the dod vocabulary (God as lover/beloved in Song and prophets) may all encode a divine inner-being reality using the same vocabulary as the human inner person. Session B should investigate whether Reg 103 contains a theological claim about divine inner-being experience, and how this connects to the programmes governing question about the inner characteristics of the human person.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1385 · finding_id='SYN-INTRA-103-001' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '1'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1'
- Structural relationship: 'N/A'

> Love's definition resolves to a structured family of inner-being orientations sharing one mechanism — directed attachment toward an object — whose moral character is entirely determined by the object chosen. Within this shared mechanism, the vocabulary distinguishes three structural registers: love as disposition (the stable inner orientation — chesed, agapē as character), love as act (the commanded and exercised expression — agapaō, enemy-love), and love as condition (the identity-constituting state of being-loved — agapētos). These are not three separate loves but three aspects of love's single operation: the person has a deep stable orientation (disposition), exercises it in specific acts (act), and exists within the love-relationship as constituted by it (condition). The vocabulary arc runs from the ontologically highest (God is love — 1Jo 4:8) through the morally normative (chesed, commanded agapē) to the affective-natural (phileō, dod) to the morally inverted (love of darkness, love of self). No other characteristic in the programme commands a comparable vocabulary range. The definition's boundary with adjacent characteristics (compassion, mercy, kindness) is partially drawn: love is the broader orientation; compassion is love's suffering-triggered mode; mercy and kindness are love's formal relational expressions. The boundaries require Session D precision.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1386 · finding_id='SYN-INTRA-103-002' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '2'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2'
- Structural relationship: 'N/A'

> Love is the programme's most constitutionally comprehensive characteristic — it occupies all five constitutional levels simultaneously: spirit-sourced (implied via Spirit-as-agent, Rom 5:5, Gal 5:22), soul-located (Song 5:6 — soul failing at beloved's absence; Mat 22:37 — love with all your soul; Joh 15:13 — laying down the soul), heart-inscribed (Pro 3:3; Rom 5:5 infused into hearts), mind-engaged (Mat 22:37 — love with all your mind; Joh 15:15 — love as knowledge-sharing), and body-expressed (kiss, embrace, tears, womb-movement across multiple groups). The constitutional movement pattern is consistently downward: Spirit origin → heart reception → soul experience → body expression. Love's heart-inscription (Pro 3:3) is the closest evidence to a constitutional deposit — the metaphorical writing of chesed into the heart's deepest register produces a lasting dispositional quality (the chasid person-type). The primary finding: love is not confined to any single constitutional level but operates across all levels in an integrated movement from deepest to most outward. This comprehensive constitutional architecture is consistent with love's function as the programme's organising characteristic.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1387 · finding_id='SYN-INTRA-103-003' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '3'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3'
- Structural relationship: 'N/A'

> Love engages all eleven inner faculties, but five show the richest engagement: (1) Identity and self-understanding — love is the primary faculty through which the person knows who they are: being-loved (agapētos) constitutes identity from the outside; what-one-loves constitutes identity from the inside. The person is doubly defined by love. (2) Relational capacity — love is the faculty's active content: it builds (Joh 13:34), sustains (Lam 3:22), and restores (Luk 15:20) relational capacity. (3) Memory — love's sustaining faculty: love without memory cannot maintain itself through absence (Jer 31:20 — 'I do remember him still'). (4) Moral sensitivity — love calibrates what the inner person registers as morally significant; the love-of-God requirement generates the hate-evil requirement (Psa 97:10). (5) Attention — love determines what the person perceives as worth attending to (Phili 4:8 — think on what is lovely). The weaker engagements: creativity (indirect, evidenced through Song-form) and conscience (inferred, not directly named). Overall: love is the faculty-most-engaged characteristic in the programme, operating through perception, reason, memory, imagination, desire, emotion, moral sensitivity, conscience (indirectly), identity, and relational capacity simultaneously.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1388 · finding_id='SYN-INTRA-103-004' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '4'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4'
- Structural relationship: 'N/A'

> Love's relational architecture is structured by three directional axes — GOD → HUMAN, HUMAN → GOD, HUMAN → HUMAN — with divine love structurally prior and causally generative of all subsequent love. 1Jo 4:19 ('we love because he first loved us') is the axis-precedence statement: the first axis is not responsive to but constitutive of the second and third. The GOD → HUMAN direction moves through four mechanisms: covenantal declaration (naming the beloved — Jer 12:7, Mat 3:17), Spirit-infusion (Rom 5:5), redemptive acts (Joh 3:16), and covenantal covering (Eze 16:8). The HUMAN → GOD direction requires total inner mobilisation (Mat 22:37 — all heart, soul, mind) and the clearing of rival loves as its condition (1Jo 4:19, 1Ti 6:10). The HUMAN → HUMAN direction spans five structural types (neighbour, enemy, community, friendship, family) and creates the social architecture described in Q&A-088 (restructured kinship, public legibility, competitive generosity). The most significant finding in T4: the human-to-God direction is conditioned by prior reception of divine love — the capacity for human love toward God is itself a gift. The one structural gap: T4.6 (spiritual beings) is absent from the evidence.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1389 · finding_id='SYN-INTRA-103-005' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '5'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T5'
- Structural relationship: 'N/A'

> Love's formation operates through a multi-layered process in the data. The primary pathway is receptive: divine love received (1Jo 4:19) → Spirit infusion (Rom 5:5, Gal 5:22) → heart-reception → soul-response → community expression. Secondary pathways: obedience → soul purification → sincere love (1Pe 1:22); forgiveness received → love generated (Luk 7:47 — via SD-020); training within community (Tit 2:4). Love can grow (1Th 3:12) and increase through the Lord's action. Its reversibility is asymmetric: divine love is irreversible by nature (Jer 31:3 — everlasting; Lam 3:22 — never ceasing); human love is subject to redirection through competing love-allegiances (2Ti 4:10 — Demas). The eschatological trajectory is toward perfection and direct knowledge: partial now (mediated by community, neighbour-teaching), moving toward fullness (perfect love casting out fear — 1Jo 4:18; direct divine knowledge — Jer 31:34; pleasures forevermore — Psa 16:11). Formation requires community — love cannot be formed in isolation; it requires both the divine giver and the human community as the formation context.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1390 · finding_id='SYN-INTRA-103-006' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '6'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T6'
- Structural relationship: 'N/A'

> Love's structural position in the programme is that of the central node in the inner-being vocabulary's relational architecture. Co-occurrence data: 196 with compassion, 105 with strength, 68 with peace, 62 with faith — confirming love's connections to the full range of C17 characteristics and extending to C20 (strength/authority). Shared anchor data: 48 verses shared across multiple registries, with Exo 34:6 (5 registries) and Gal 5:22 (5 registries) as the highest-density shared anchors — confirming love as the vocabulary cluster around which the programme's most significant cross-registry verses gather. Sequential position: love stands downstream of divine action (received) and upstream of the ethical-moral life (generative of commandment-keeping, Spirit-fruits, community identity). Causal productivity: love generates joy, rest, grief, obedience, praise — the programme's most causally productive characteristic. Vocabulary sharing: term sharing ratio 0.701, the highest in C17 — love shares vocabulary with compassion, mercy, kindness, goodness, desire, and peace. The primary gap: distinctions from adjacent characteristics (compassion, mercy, kindness) remain partially drawn; Session D is the resolution context.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1391 · finding_id='SYN-INTRA-103-007' · status=`pending` · type=`SYNTHESIS_INTRA_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '7'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T7'
- Structural relationship: 'N/A'

> Love's evidential foundation is the most comprehensive in the programme. The primary terms (chesed, agapē/agapaō, racham/rachamim, ahavah, dod, phileō) cover the full constitutional range: willed-covenantal (chesed), Spirit-produced self-giving (agapē), somatic-compassionate (racham), intense-erotic (ahavah/dod), and naturally affective (phileō). The vocabulary structure itself distinguishes disposition/act/condition, received/given, and quality/person-type — making it architecturally precise. The semantic range of the primary terms spans from divine ontology (God is love) to moral inversion (love of darkness) — the widest semantic arc in the programme. The primary anchor is Lam 3:22 — love's most definitive affirmation precisely at the moment of maximum empirical falsification: a theological confession rather than an empirical observation. The LXX connection is partially evidenced (agapē as chesed-translated); full LXX analysis is limited by NO_WORD_ANALYSIS flags. The human science frameworks identified (attachment theory, virtue ethics) are named as Session D pointers but not elaborated — the instruction prohibits importing framework content not grounded in the data.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1392 · finding_id='SYN-INTER-103-001' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '1'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T2'
- Structural relationship: 'N/A'

> Love's definition and its constitutional location are mutually illuminating. The definition identifies love as disposition + act + condition operating through directed attachment toward an object. The constitutional mapping shows where this triple operation is located: the disposition is heart-inscribed (Pro 3:3) and spirit-sourced (implied via Rom 5:5), stable across constitutional levels; the act is will-engaged (Mat 22:37 — commanded) and soul-mobilised (Joh 15:13 — soul laid down); the condition of being-loved is received at the heart level (Rom 5:5 — poured in) and experienced at the soul level (Zep 3:17 — quieting). The constitutional movement pattern (Spirit → heart → soul → body) maps directly onto the definition's three registers: the deepest dispositional origin (spirit/heart) grounds the stable orientation; the soul-level is where love is experienced as feeling; the body-level is where act and condition become visible. Together: the constitutional location analysis confirms that love's definition is not a surface account but a constitutional claim — love operates at every depth of the inner person, which is precisely what the 'whole heart, soul, and mind' commandment (Mat 22:37) requires.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1393 · finding_id='SYN-INTER-103-002' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '2'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T3'
- Structural relationship: 'N/A'

> Love's definition as directed-attachment-toward-an-object generates a characteristic pattern of faculty engagement. Because love is always toward an object, it necessarily engages attention (what is attended to is the beloved — Phili 4:8), reason (judgment of the object's worth and the hierarchy of competing loves — Mat 10:37), memory (remembering the beloved sustains love — Jer 31:20), and identity (what is loved constitutes who one is — Q&A-075). The definition's object-determination principle (moral quality determined by object) maps onto the moral sensitivity faculty: the faculty that calibrates moral perception is calibrated by love's direction — you notice what you love, and what you love as most important determines what you register as morally significant (Psa 97:10 — love-of-God generates hate-of-evil). The definition's tripartite structure (disposition/act/condition) maps onto the faculty architecture: disposition engages the will and conscience; act engages the relational capacity and body; condition engages identity and emotion. No faculty operates independently of love's fundamental structure.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1394 · finding_id='SYN-INTER-103-003' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '3'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T4'
- Structural relationship: 'N/A'

> Love's definition as directed attachment reaches its relational specification in T4's three-axis architecture. The object-determination principle (Q&A-144) — that love's moral quality depends entirely on its object — is enacted relationally when the proper objects are named: God (vertical-ascending), neighbour and enemy (horizontal), and the beloved community (horizontal-mutual). The definition's three registers map onto the relational axes: the dispositional register (stable inner orientation) grounds the covenantal-faithful love in the GOD→HUMAN axis (God's chesed never ceasing — Lam 3:22); the active register (commanded, exercised) grounds the love of neighbour and enemy (Lev 19:18, Mat 5:44); the condition register (being-loved as identity) is the GOD→HUMAN axis's effect in the person (agapētos — constituted as beloved). The relational interfaces reveal what the definition describes abstractly: love's mechanism in concrete directional operation. The most significant inter-tier finding: the definition's requirement that love be directed toward an object is fulfilled eschatologically when the object is perfectly and permanently God — Jer 31:34, 1Jo 4:18 (perfect love).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1395 · finding_id='SYN-INTER-103-004' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '4'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T5'
- Structural relationship: 'N/A'

> Love's definition as disposition + act + condition maps onto the developmental sequence in T5. Condition (being-loved) comes first in the sequence — 1Jo 4:19 ('he first loved us') — the person is constituted as beloved before they can love in return. Disposition (stable inner orientation) is formed through the Spirit's infusion (Rom 5:5), obedience-pathway (1Pe 1:22), and training (Tit 2:4) — the formation process produces the stable dispositional form. Act (exercised love) is the formation process's outcome — the person who has been loved, whose disposition has been formed, exercises love toward God, neighbour, and enemy. The reversibility asymmetry (divine love irreversible; human love subject to redirection — Q&A-094) maps onto the definition's three registers: the condition of being-divinely-loved is irreversible (God does not withdraw the beloved-status once conferred — Jer 31:3); the human disposition is subject to redirection through competing loves; the human love-acts can fail without invalidating the conditional ground. The eschatological trajectory (toward perfect love — 1Jo 4:18) describes the movement toward the definition's fullest form: stable disposition + unconstrained act + permanent condition of perfect love.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1396 · finding_id='SYN-INTER-103-005' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '5'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T6'
- Structural relationship: 'N/A'

> Love's definition as the programme's most semantically comprehensive inner-being characteristic is confirmed and deepened by the structural relationship analysis. The term sharing ratio (0.701 — highest in C17) and the co-occurrence breadth (196 with compassion through to 29 with mercy) reflect the definition's conclusion: love is not a bounded standalone characteristic but the semantic centre of a cluster. The sequential finding (love as mediating-and-generative node — Q&A-105) maps onto the definition's tripartite structure: love is downstream (condition-received from God), central (disposition that organises), and upstream (act that generates all subsequent ethical life). The definition's vocabulary arc (from divine being to love of darkness — Q&A-131) is confirmed by the structural relationship data: the vocabulary extends into every adjacent registry (through XREF sharing, co-occurrence, and shared anchors), touching every corner of the programme. The structural analysis thus confirms the definitional claim: love is not merely a characteristic among others but the organising principle of the inner-being vocabulary.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1397 · finding_id='SYN-INTER-103-006' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '6'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T1, T7'
- Structural relationship: 'N/A'

> The evidential foundation confirms and specifies the definition at every point. The vocabulary analysis confirms the four-mode structure of the definition (Q&A-122, Q&A-123): chesed (covenantal-dispositional), racham (somatic-compassionate), ahavah/dod (intense-erotic), phileō/agapē (affective-natural and willed-unconditional). The grammatical range analysis confirms the tripartite definition (Q&A-123): verb (act) + noun (disposition) + adjective-passive (condition). The semantic range analysis confirms the vocabulary arc (Q&A-124, Q&A-131). The primary anchor (Lam 3:22 — Q&A-136, Q&A-137) confirms the definition's most counterintuitive feature: love at its most definitional is not evidenced by love's presence but confessed against its apparent absence. The definition says love is permanent, unwavering, faithful — and the evidential ground for this claim is a verse written in the context of Jerusalem's destruction. The evidential foundation is thus not primarily experiential but confessional — the definition's permanence-claim is a theological assertion, grounded in the character of God rather than in the consistency of human experience.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1398 · finding_id='SYN-INTER-103-007' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '7'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T3'
- Structural relationship: 'N/A'

> Love's constitutional architecture and its faculty engagement are structurally aligned. The heart's engagement with love (Q&A-044, Q&A-045) corresponds to the heart's known integrating function across the programme: the heart is the location of knowing (Joh 15:15 — knowledge-disclosure as love's act), willing (Mat 22:37 — love commanded), feeling (Song 5:2 — heart awake in love-awareness), and moral awareness (Pro 3:3 — chesed inscribed). Each of the heart's functions corresponds to a faculty: knowing → reason and memory; willing → will; feeling → emotion; moral awareness → moral sensitivity. The soul-level constitutional location (Song 5:6 — soul failing at beloved's absence) corresponds to the identity and relational capacity faculties: the soul whose vitality is partly constituted by the love-object is the soul whose identity (T3.10) and relational capacity (T3.11) are most deeply invested in love. The Spirit-sourced origin of love (implied) corresponds to the deep pre-reflective faculty level (L-005 — love below conscious attention): the Spirit's infusion produces love at a depth below ordinary faculty-awareness. Constitutional depth and faculty depth are directly correlated.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1399 · finding_id='SYN-INTER-103-008' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '8'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T4'
- Structural relationship: 'N/A'

> The constitutional location data and the relational interface data converge on the same structural claim: love's inner depth is its relational reach. The deeper love is constitutionally (heart-inscribed, soul-constitutive, Spirit-sourced), the further its relational reach — from neighbour-love (soul-level reciprocal) to enemy-love (will-level against grain) to divine love (Spirit-level transcendent). The constitutional movement pattern (Spirit → heart → soul → body — Q&A-056) maps onto the relational directional pattern: divine love enters at the deepest constitutional level (Spirit, heart) and produces relational acts at the outermost level (community legibility, bodily expression). The GOD→HUMAN axis operates at the constitutional depth where love is received (heart-infusion — Rom 5:5); the HUMAN→GOD axis requires total constitutional mobilisation (Mat 22:37 — all heart, soul, mind); the HUMAN→HUMAN axis is the outward bodily expression of the internal constitutional reality. Constitutional and relational are thus not two separate dimensions of love but the inside and outside of the same movement.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1400 · finding_id='SYN-INTER-103-009' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '9'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T5'
- Structural relationship: 'N/A'

> The formation process in T5 works precisely through the constitutional locations identified in T2. Spirit infusion (Rom 5:5) enters at the deepest level (Spirit → heart), establishing love's constitutional ground. Obedience-pathway purifies the soul (1Pe 1:22) — the soul-level constitutional location is the target of formation's clearing work. Training in the community (Tit 2:4) operates at the body-habit level — forming love through repeated communal acts that imprint the body's relational patterns. The heart-inscription of chesed (Pro 3:3) is the formation's goal-state: love sufficiently formed that it is constitutionally inscribed, no longer needing to be generated afresh for each act. The eschatological trajectory (perfect love, direct knowledge, pleasures forevermore) describes the perfection of the constitutional architecture: all levels operating without obstruction, permanently, toward the proper object. Constitutional location is thus not a static description but a dynamic formation target: each level can be more or less formed in love, and the formation process addresses each level in sequence.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1401 · finding_id='SYN-INTER-103-010' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '10'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T6'
- Structural relationship: 'N/A'

> Love's comprehensive constitutional location (all five levels) is structurally consistent with its position as the programme's central co-occurrence node. A characteristic that operates at every constitutional level will co-occur with the broadest range of other characteristics — because any verse that names soul, heart, mind, spirit, or body is potentially within love's evidential terrain. The co-occurrence breadth (top 25 covering registries from C17 through C20 and beyond) reflects the constitutional breadth: strength and authority (C20) co-occur with love because the same verses that address God's inner character include both love and power vocabulary — the divine portrait (Exo 34:6) is constitutionally comprehensive. The vocabulary sharing ratio (0.701 — highest in C17) similarly reflects the constitutional comprehensiveness: love shares vocabulary with compassion (at the somatic/racham level), with goodness (at the heart/tov level), with desire (at the ahav/phileō root level), with peace (at the soul-rest level). Constitutional breadth and vocabulary breadth are the same phenomenon viewed from different angles.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1402 · finding_id='SYN-INTER-103-011' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '11'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T2, T7'
- Structural relationship: 'N/A'

> The evidential foundation supports and grounds the constitutional location claims. Each constitutional level identified in T2 has specific vocabulary evidence in T7: Spirit-level origin — Gal 5:22 (fruit of the Spirit), Rom 5:5 (poured into hearts through the Spirit); soul-level — Song 5:6 (soul failing), Mat 22:37 (all your soul), Joh 15:13 (lay down the soul); heart-level — Pro 3:3 (heart inscription), Rom 5:5 (into our hearts); mind-level — Mat 22:37 (all your mind), Joh 15:15 (knowledge disclosure); body-level — kiss/embrace/tears/inner-organ-movement vocabulary across multiple groups. The lexical range of the primary terms (Q&A-122 — chesed, racham, agapē, dod, phileō) corresponds precisely to the five constitutional levels: each term carries a different constitutional register as its primary habitat. The evidential foundation thus not only confirms the constitutional claims but shows them to be lexically grounded in the vocabulary's own structure.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1403 · finding_id='SYN-INTER-103-012' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '12'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T4'
- Structural relationship: 'N/A'

> The faculty engagement pattern in T3 is produced by and oriented toward the relational interfaces in T4. Love's identity-faculty (T3.10) is constituted through the relational interface: being-loved by God (GOD→HUMAN axis) establishes the identity of agapētos; what-one-loves (active direction) establishes identity through the chosen object. The relational capacity faculty (T3.11) is the faculty through which the three relational axes are exercised: the GOD→HUMAN axis engages the relational capacity as receiver; the HUMAN→GOD axis engages it as giver; the HUMAN→HUMAN axis engages it in both directions simultaneously. Memory (T3.3) sustains the relational interface: love toward God is sustained through remembering his chesed (Jer 31:20); love in community is sustained through shared history. Moral sensitivity (T3.8) is calibrated by the relational interface structure: love-of-God calibrates the moral perception of what is evil (Psa 97:10); love-of-neighbour calibrates the perception of what is just. The deepest inter-tier finding: the faculty engagement pattern is not incidental — it is precisely the faculty configuration required by the relational architecture. The relational structure generates the faculty requirements.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1404 · finding_id='SYN-INTER-103-013' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '13'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T5'
- Structural relationship: 'N/A'

> Formation in T5 operates through the same faculties identified in T3, producing their development. Memory is formed through the covenantal story — Israel's memory of God's love (Jer 2:2 — 'I remember the devotion of your youth') is the ground for love's formation in both directions; formation requires knowing the love-history. Imagination is formed through eschatological vision: the forward-projection of love's fullness (Psa 27:13, Jer 31:34) orients present formation toward its goal. Identity formation is the T3.10/T5 overlap: being-named-beloved (Mat 3:17, Rom 1:7) is the formation's constitutive moment — identity received through love is the ground from which love-acts are exercised. The relational capacity faculty (T3.11) is the faculty that formation produces: the formation process (Spirit infusion, obedience-purification, training) produces a person with increasing relational capacity for love's three directional axes. The community's role in formation (Q&A-097) corresponds to the relational capacity faculty's communal engagement: the faculty cannot develop in isolation because love cannot exist without a beloved.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1405 · finding_id='SYN-INTER-103-014' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '14'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T6'
- Structural relationship: 'N/A'

> The faculty engagement breadth in T3 is consistent with love's structural position as the programme's central sequential node in T6. A characteristic that engages all eleven faculties will necessarily stand at the intersection of the programme's full inner-being vocabulary — because any characteristic that engages one faculty will co-occur with love insofar as love also engages that faculty. The memory-faculty engagement explains part of the co-occurrence with despair (R044 — 55 shared verses): lament appeals to the memory of God's love (Lam 3:22) as its ground. The identity-faculty engagement explains the co-occurrence with calling (R019 — 51 shared): identity-as-beloved and identity-as-called are grammatically co-ordinate (Rom 1:7). The moral-sensitivity engagement explains co-occurrence with guilt (R073 — 32 shared): moral sensitivity calibrated by love recognises guilt as the state that precedes the forgiveness that generates love (Luk 7:47). Faculty engagement and structural relationships thus form a coherent explanatory system: the faculty profile generates the co-occurrence pattern.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1406 · finding_id='SYN-INTER-103-015' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '15'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T3, T7'
- Structural relationship: 'N/A'

> The vocabulary evidence grounds the faculty claims with lexical precision. Identity faculty (T3.10): agapētos (person-type of being-loved), chasid (person-type of chesed), filos (person-type of phileō) — all three are lexically grounded person-type terms (Q&A-127). Moral sensitivity faculty (T3.8): the hate-vocabulary embedded as OWNER (H8130 sane — Q&A-126) grounds the claim that love requires and produces righteous hatred — the structural opposite provides the moral sensitivity calibration. Memory faculty (T3.3): the verb-form analysis (Q&A-123) shows that chesed as noun-primary form implies a dispositional quality that persists — memory is the chesed-noun's faculty correlate. Attention faculty (T3.1): phileō's etymology (from philos — friend) implies a relational salience structure — the one who is phileō-loved becomes salient to the lover's attention-field. The vocabulary's etymological structure (Q&A-122) is thus the lexical ground of the faculty engagement pattern: the root meanings point toward the faculties each term primarily activates.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1407 · finding_id='SYN-INTER-103-016' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '16'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4, T5'
- Structural relationship: 'N/A'

> The relational interface structure and the formation process are interdependent: the formation process is directed toward equipping the person for love's three relational axes, and the relational axes are the context in which formation occurs. GOD→HUMAN axis as formation ground: divine love received (1Jo 4:19) is the formative act that establishes the person's capacity for all subsequent love — receiving is formation's enabling event. HUMAN→GOD axis as formation goal: total inner mobilisation (Mat 22:37 — all heart, soul, mind) is the fully formed love toward God; partial mobilisation marks love still in formation. HUMAN→HUMAN axis as formation context: community (1Pe 1:22, Tit 2:4) is both the goal-state (mutual love as community identity — Joh 13:35) and the formation context (love formed through exercising love within community). The reversibility asymmetry (divine love irreversible; human love subject to redirection) maps onto the axis structure: the GOD→HUMAN axis is the stable ground; the HUMAN→GOD and HUMAN→HUMAN axes are the formation-dependent expressions. Formation deepens the second and third axes; the first axis does not depend on formation.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1408 · finding_id='SYN-INTER-103-017' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '17'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4, T6'
- Structural relationship: 'N/A'

> The three relational axes in T4 generate the structural relationship pattern in T6. The GOD→HUMAN axis explains love's highest co-occurrences with the programme's theological vocabulary: calling (R019 — 51 shared, identity-as-beloved and identity-as-called), faith (R059 — 62 shared, the inner condition for receiving divine love), and compassion (R023 — 196 shared, the compassionate-responsive mode of divine love). The HUMAN→HUMAN axis explains the co-occurrence with peace (R117 — 68 shared, peacemaking as love's horizontal expression) and community-related vocabulary. The sequential structure (divine love prior → human love responsive → ethical life) explains love's mediating position (Q&A-105): it stands between the GOD→HUMAN axis and the HUMAN→HUMAN axis as the transmission point. Love received from God becomes love given to neighbour — the sequential position is the relational interface described structurally. The 48 shared anchor verses are the evidential sites where these relational intersections are most visible: Exo 34:6 (GOD→HUMAN axis at maximum density), Gal 5:22 (HUMAN→HUMAN axis generated by Spirit), Joh 13:34 (HUMAN→HUMAN axis constituted by GOD→HUMAN love as model).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1409 · finding_id='SYN-INTER-103-018' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '18'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T4, T7'
- Structural relationship: 'N/A'

> The evidential foundation directly supports each of the three relational axes. GOD→HUMAN axis — most densely evidenced: Exo 34:6 (divine self-declaration of love as primary attribute), Jer 12:7 (beloved of God's soul), Mat 3:17 (beloved Son named), Joh 3:16 (God so loved the world), Rom 5:5 (love poured into hearts through Spirit). The lexical evidence for this axis runs from the OT's chesed-God group (169 active verses — largest single group in the registry, Q&A-038) through the NT's agapē-God group (35 relevant). HUMAN→GOD axis — Psa 63:3 (chesed above life), Mat 22:37 (total inner mobilisation), Joh 14:15 (love producing obedience); these are carried by the agapaō-love-of-God group (571-001) and the chesed-human group (536-002). HUMAN→HUMAN axis — Lev 19:18 (neighbour-love commandment), Mat 5:44 (enemy-love), Joh 13:34 (new commandment), Joh 13:35 (community identity); these span the rea-group (173 active), the agapaō-mutual group (571-004, 53 relevant), and the filadelfia group (558-001). The evidential foundation confirms that all three axes have strong lexical and verse-level grounding, with the GOD→HUMAN axis carrying the greatest evidential weight.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1410 · finding_id='SYN-INTER-103-019' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '19'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T5, T6'
- Structural relationship: 'N/A'

> The formation process and the structural relationships are mutually reinforcing systems. The formation pathway (divine love received → Spirit infusion → soul purification → community expression) maps onto the sequential structural position: love's formation follows the same sequence as love's structural position in the programme — first received (downstream of divine action), then formed (mediating), then expressed (generative of ethical life). The growth-capacity of love (1Th 3:12 — Q&A-092) explains the programme's most puzzling co-occurrence finding: strength and authority (C20, 105 and 69 shared verses respectively). Love growing under the Lord's enabling encounters contexts of power — covenantal love among the people of God is exercised within structures of authority, governance, and strength. The love-power co-occurrence reflects the formation context: love formed within communities is formed within structures of authority. The eschatological trajectory (toward perfect love and direct knowledge) describes the structural relationships' completion: when love reaches its eschatological form, the partial sequential relationships (love received → love given → ethical life) are resolved into the direct love-knowledge of the new covenant (Jer 31:34).

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1411 · finding_id='SYN-INTER-103-020' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '20'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T5, T7'
- Structural relationship: 'N/A'

> The evidential foundation grounds the formation claims at the lexical level. The growth-capacity finding (Q&A-092) is grounded in the verbal form agapaō and the noun-verb movement: chesed as noun (stable quality) requires formation before it functions as such; the transition from occasional loving acts (verb) to stable covenantal character (noun-quality) is the formation process in lexical form. The reversibility asymmetry (divine love irreversible; human love redirectable — Q&A-094) is grounded in the vocabulary's own structure: the divine forms of chesed and agapē carry permanence qualifiers (olam — everlasting; Lam 3:22 — never ceasing) that the human love forms do not. The primary anchor (Lam 3:22 — Q&A-136) is itself a formation text: the confession of love's permanence in extremity is a formation of the inner person toward trust in what cannot be seen. The formation process produces the person capable of making the Lam 3:22 confession — the developmental trajectory toward love's perfection includes the formation of the inner person's capacity to confess love against empirical evidence.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=1412 · finding_id='SYN-INTER-103-021' · status=`pending` · type=`SYNTHESIS_INTER_TIER`

- Raised: '2026-04-30T17:22:20Z'  ·  Pass: '21'  ·  Segment: ''
- Instruction version: `wa-sessionb-analysis-output-v1_8-20260430.md`
- Synthesis outcome: 'D'
- Tiers engaged: 'T6, T7'
- Structural relationship: 'N/A'

> The structural relationship data and the evidential foundation are the most mutually confirming pair in the synthesis matrix. The co-occurrence breadth (T6.1) is directly explained by the vocabulary breadth (T7.1.10 — the widest semantic arc in the programme): a vocabulary that spans from divine being to love of darkness will co-occur with every other inner-being characteristic because it occupies every register of the inner-being vocabulary. The shared anchor density (48 verses — T6.6) is explained by the primary anchor's function (Lam 3:22 — T7.2.5/T7.2.6): the programme anchors the most significant cross-registry verses at love because love is the definitional centre from which adjacent characteristics derive their meaning. The vocabulary sharing ratio (0.701 — T6.4) is explained by the root-level connections (T7.1.2): the racham root connects love, compassion, and mercy; the ahav root connects love and desire; the tov root connects love and goodness. The structural relationship data is, at its core, the observable programme-level effect of the lexical architecture that the evidential foundation analysis reveals. Structural breadth and lexical breadth are the same reality at different levels of analysis.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R128 rebellion — 3 unresolved

#### sbf.id=32 · finding_id='DIM-128-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-06'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.2-2026-04-06`
- Anchor verses: Deu 4:9, Deu 7:4, 2Ki 3:3, Num 16:26

> H5493H (sur, to turn aside/depart) in rebellion (#128) has 2 healthy active groups: 6077-001 (departure of God's Spirit, 5 verses) and 6077-003 (departure of inner strength, 3 verses). A third group (6077-002, departure from God) had 4 verse_context records that were all subsequently delete_flagged for unknown reasons. The 4 orphaned verses are: Deu 4:9 (warning not to turn aside from what was seen), Deu 7:4 (intermarriage turning sons from following God), 2Ki 3:3 (not departing from the sin of Jeroboam), Num 16:26 (command to depart from tents of Korah). The group shell has been delete_flagged. Session B analyst should review whether any of these 4 verses meet the inner-being filter for rebellion and should be reassigned to 6077-001 or 6077-003, or whether a distinct apostasy group is warranted.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=88 · finding_id='DIM-128-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> The sur (to turn aside) sub-gloss groups in Reg 128 show a consistent pattern: turning aside can be from God (6076-001 — Spiritual/God-ward negative), from idols toward God (6075-001 — Spiritual/God-ward positive), or toward God (6076-003 — Spiritual/God-ward positive). The same volitional act (turning) is the mechanism for both rebellion and repentance — only the direction differs. Session B should examine whether the turning vocabulary illuminates rebellion as fundamentally a directional problem of the inner being, and what this implies for understanding repentance as the reversal of the same inner movement.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=91 · finding_id='DIM-128-003' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`
- Anchor verses: Deu 4:9, Deu 7:4, 2Ki 3:3, Num 16:26

> Group 6077-002 in Reg 128 (the orphaned group from DIM-128-001) has anchor=0 and related=0. The four orphaned verses are: Deu 4:9 (warning not to turn aside from what was seen), Deu 7:4 (intermarriage turning sons from following God), 2Ki 3:3 (not departing from the sin of Jeroboam), Num 16:26 (command to depart from tents of Korah). Session B analyst should review whether any meet the inner-being filter for rebellion and should be reassigned to 6077-001 or 6077-003, or whether a distinct apostasy group is warranted. (Continuing DIM-128-001 instruction.)

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R178 wrath — 1 unresolved

#### sbf.id=75 · finding_id='DIM-178-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> The cho.mah (wall, H2346G) groups in Reg 178 (6784-001 to 6784-006) represent an XREF pattern where an architectural term's inner-being applications cover: misplaced trust (false security replacing God-trust), self-mastery (undefended city), purity (chaste self-possession), divine protection, divine attentiveness, and prophetic resilience. Session B should assess whether these six wall-groups illuminate a coherent inner-being pattern about security vs. vulnerability and self-possession vs. dissolution, and how this relates to the wrath registry.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

## §2. Unresolved research flags

### R001 abomination — 1 unresolved

#### srf.id=677 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M01-BOUNDARY-H6426'
- Strong's ref: `H6426`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M01 closure (DIR-20260516-007): BOUNDARY term H6426 (pa.lats) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — H6426 pa.lats]. Pending researcher disposition: set-aside / promote-to-M01-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R1 (abomination).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R003 ambition — 1 unresolved

#### srf.id=178 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-3-SD001'
- Raised: '2026-04-09'  ·  Session target: 'D'

> Reg 3 (ambition) contains a majority of terms from the philoxenos/philoxenia/philantropōs/filautos/filofronōs cluster (all Relational Disposition) alongside the core ambition terms (eritheia, filotimeomai = Volition; erethizō = Volition / Emotion — Negative). The registry title does not reflect the actual inner-being content, which is primarily a hospitality-love cluster. Session D should assess: (a) whether the philos-family terms constitute a distinct inner-being cluster from the ambition terms; (b) whether self-directed aspiration (filotimeomai) and other-directed love (filoxenia, filantropōs) are structurally opposite poles of a single self/other orientation axis; (c) whether eritheia (selfish rivalry) and filautos (self-love) together name the inverse of the hospitality cluster.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R051 distress — 3 unresolved

#### srf.id=670 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M01-BOUNDARY-G0085'
- Strong's ref: `G0085`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M01 closure (DIR-20260516-007): BOUNDARY term G0085 (ademoneo) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — G0085 ademoneo]. Pending researcher disposition: set-aside / promote-to-M01-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R51 (distress).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=673 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M01-BOUNDARY-H3735'
- Strong's ref: `H3735`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M01 closure (DIR-20260516-007): BOUNDARY term H3735 (ke.ra) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — H3735 ke.ra]. Pending researcher disposition: set-aside / promote-to-M01-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R51 (distress).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=675 · flag_code=`BOUNDARY_DECISION_PENDING` · priority='MEDIUM'

- Label: 'M01-BOUNDARY-H6125'
- Strong's ref: `H6125`
- Raised: '2026-05-16'  ·  Session target: 'Researcher'

> M01 closure (DIR-20260516-007): BOUNDARY term H6125 (a.qah) reached closure without exit decision. Phase 9 per-term structural characterisation in part4 (WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md) under marker [BOUNDARY — H6125 a.qah]. Pending researcher disposition: set-aside / promote-to-M01-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. Source registry: R51 (distress).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R056 envy — 2 unresolved

#### srf.id=34 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='HIGH'

- Label: 'PH2-056-001'
- Strong's ref: `G3788`
- Raised: '2026-03-25'  ·  Session target: 'D'

> G3788 ophthalmos has 641 occurrences and 88 verses in export. Classified extracted_thin under evil-eye/envy-eye analysis only (Mat 20:15; Mar 7:22; Mat 6:22-23). Full corpus must not be used in synthesis. Phase 2 independent review of the complete ophthalmos corpus required.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=35 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='LOW'

- Label: 'PH2-056-002'
- Strong's ref: `G6041`
- Raised: '2026-03-25'  ·  Session target: 'D'

> G6041 zeleuō (to envy) has 1 occurrence but 0 verse records in export. Genuine envy vocabulary but cannot be analysed. Phase 2 independent research required.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R103 love — 45 unresolved

#### srf.id=7 · flag_code=`PH2_CROSS_REGISTRY_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-103-001'
- Strong's ref: `H0157G`
- Raised: '2026-03-24'  ·  Session target: 'D'

> H0157G a.hev (to love, 207 occurrences) is a XREF term — primary analysis held in desire registry (reg 43). Before Session D love-vocabulary synthesis, review the desire-registry a.hev analysis to confirm it is adequate for love-context conclusions. If not, supplementary analysis is required within this registry.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=8 · flag_code=`PH2_DATA_QUALITY` · priority='MEDIUM'

- Label: 'PH2-103-002'
- Strong's ref: `H7356B`
- Raised: '2026-03-24'  ·  Session target: 'D'

> H7356B rachamim has 69 exported verses but a significant portion are womb-usage verses (rechem: H7358 — physical womb in birth/fertility contexts) that entered via the racham root family bleed. Love-specific compassion verses number approximately 35-40. Before synthesis conclusions are drawn about the scale of the compassion vocabulary, the verse set should be cleaned to isolate compassion-specific occurrences.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=9 · flag_code=`PH2_CROSS_REGISTRY_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-103-003'
- Strong's ref: `G0026`
- Raised: '2026-03-24'  ·  Session target: 'D'

> 1 Jo 4:18 — there is no fear in love, but perfect love casts out fear — is the most analytically precise cross-registry claim in the programme. Requires dedicated cross-registry analysis with the fear registry (reg 61): what kind of fear is displaced by perfect love? Does the OT vocabulary support this structural opposition? This is a Session D priority and potentially one of the most significant structural findings available from the dataset.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=10 · flag_code=`PH2_THEOLOGICAL_DEPTH_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-103-004'
- Strong's ref: `G0026`
- Raised: '2026-03-24'  ·  Session target: 'D'

> 1 Jo 4:8, 16 — God is love (ho theos agapē estin) — is the most radical ontological claim made about the divine nature in the NT. It requires dedicated Session D treatment: how does this claim relate to all other inner-being attributes attributed to God (anger, grief, compassion)? Does this claim govern all other divine emotional attributions? This is the theological summit of the entire programme.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=11 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='MEDIUM'

- Label: 'PH2-103-005'
- Strong's ref: `G0025`
- Raised: '2026-03-24'  ·  Session target: 'D'

> G0025 agapaō has 344 occurrences but only 130 verses in the export. Priority additional coverage: full Pauline love-ethics (Eph 5; 1 Thes 4; Col 3; Gal 5); full Johannine love discourse (Joh 13-17 beyond export); Synoptic love-commandment traditions. Synthesis conclusions about NT love theology should be held provisional pending more complete verse coverage.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=12 · flag_code=`PH2_THEOLOGICAL_DEPTH_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-103-006'
- Strong's ref: `H0160`
- Raised: '2026-03-24'  ·  Session target: 'D'

> Song 8:6 — love is strong as death... the very flame of the LORD — is the OT's nearest approach to a theology of love's ultimate nature. A Phase 2 study of the Song as a whole is needed: its erotic vocabulary within the love architecture, its allegorical tradition (divine-human love as referent), and its canonical significance as the inclusion of embodied desire within the sacred literature. Required before Session D synthesis of the love-eros-agape relationship.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=164 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD001'
- Raised: '2026-04-08'  ·  Session target: 'D'

> Group 1581-001 (katafileō, to kiss) was assigned Emotion — Positive for the inner states expressed through the physical act. The legacy Somatic/Embodied automated label raised a genuine question about whether Scripture encodes inner-being content in bodily expression in ways the v1.4 vocabulary does not capture. Session D should assess whether a Somatic dimension is warranted across the programme — for groups where inner-being content is carried by or expressed through physical/bodily acts (kiss, embrace, prostration, anointing, tears). This may require a v1.4 vocabulary revision.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=165 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD002'
- Cross-registry: 117
- Raised: '2026-04-08'  ·  Session target: 'D'

> C17 shows a significant concentration of Relational Disposition groups with GOD as dominant subject — the divine inner being as relationally oriented toward persons. These span love (God's chesed and agapē), compassion (divine racham), mercy (God's eleos), grace (God's charis/chen), and peace (God's shalom-giving). Combined with the Transformation/GOD groups (atonement, forgiveness, Spirit-impartation) and Moral Character/GOD groups (forgiveness as divine attribute, compassion as God's character), C17 reveals the fullest picture yet of God's inner being. Session D should synthesise across C17 and other clusters to characterise the inner being of God as Scripture describes it — his relational dispositions, inner emotional range, and what this reveals about the divine nature in relation to the human person created in his image.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=242 · flag_code=`DIMREVIEW_SESSION_D` · priority='MEDIUM'

- Label: 'DIM-103-SD000'
- Raised: '2026-04-11'  ·  Session target: 'D'

> The dod groups in Reg 103 (533-001, 1602-001, 545-001) together span the full range of the beloved-love vocabulary: from the Songs human mutual delight to covenantal God-Israel love to intimate address. Session D should examine whether the dod/beloved vocabulary encodes a structural homology: the same inner-being quality of intense, exclusive, covenantal devotion manifests at both the divine-human covenantal level and the human interpersonal level. If confirmed across the full corpus, this would show that the love vocabulary of Scripture treats both divine and human love as expressions of the same inner-being characteristic — not mere analogy.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=289 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD003'
- Strong's ref: `G0025`
- Cross-registry: 140
- Raised: '2026-04-12'  ·  Session target: 'D'

> Mat 5:44 — love of enemies co-occurs with prayer for persecutors and promise of sonship. Agapao + seeking + will + pray intersection. The enemy-love command may be the most cross-registry verse in the NT. Registries implicated: love (103), seeking (140), will (173), pray (212). Question: does the enemy-love command require a prior orientation of seeking God (140) and an act of the will (173) as its structural preconditions?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=290 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD004'
- Strong's ref: `G5368`
- Cross-registry: 182
- Raised: '2026-04-12'  ·  Session target: 'D'

> Joh 12:25 — whoever loves his life loses it, whoever hates his life keeps it for eternal life. Agapao/miseo applied to one's own life. Structural intersection of love (103), hatred (75), soul/life (182), surrender/will (156). Question: is this verse's paradox — loving the self leads to loss, hating it leads to eternal life — the programme's clearest statement about how love and self-orientation stand in opposition as inner-being structures?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=291 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD005'
- Strong's ref: `G5377`
- Cross-registry: 43
- Raised: '2026-04-12'  ·  Session target: 'D'

> 2Ti 3:4 — philotheos vs philēdonos antithesis. Lovers of God directly contrasted with lovers of pleasure in the last-days catalogue. Cross-registry: love (103), desire/pleasure (43), C15 (God-orientation cluster). Question: does the philo- compound family structure reveal that love and desire share the same inner mechanism of attachment — with the moral question being solely the object toward which the attachment is directed?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=292 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD006'
- Strong's ref: `H2617A`
- Raised: '2026-04-12'  ·  Session target: 'D'

> Mic 6:8 — chesed/justice/humility triad. The three requirements of the covenant life placed in parallel. Chesed (love/faithfulness), mishpat (justice), halak-anavah (humble walking with God). Is this the OT equivalent of the NT faith-hope-love triad? Does the programme have registries for justice and humility? If so, the Mic 6:8 triad is a cross-registry structure of fundamental importance for the programme's Session D synthesis of the moral inner life.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=293 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD007'
- Strong's ref: `H7355`
- Cross-registry: 23
- Raised: '2026-04-12'  ·  Session target: 'D'

> Racham root (compassion) etymologically linked to rechem (womb). The womb-compassion-love nexus: divine compassion is described through womb/nursing imagery (Isa 49:15, Jer 31:20). The RACHAM root spans love (103), compassion (23), mercy (111). Question: is there a structural hierarchy within the love cluster — love as the broadest category, compassion as love-responding-to-suffering, mercy as love-overriding-just-consequence? The womb etymology grounds all three in the same bodily-relational origin.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=294 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD008'
- Strong's ref: `H8130`
- Cross-registry: 75
- Raised: '2026-04-12'  ·  Session target: 'D'

> Eccl 9:6 — love, hatred, and envy listed as the three constitutive inner orientations that cease at death. This triadic structure may define a fundamental taxonomy of relational inner states: love (toward/for), hatred (against), envy (desiring what another has). Does the Ecclesiastes triadic structure represent the OT's most explicit inner-being taxonomy? Cross-registry: love (103), hatred (75), envy registry.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=295 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD009'
- Strong's ref: `H2898`
- Cross-registry: 67
- Raised: '2026-04-12'  ·  Session target: 'D'

> Psa 25:7 — divine goodness (tuv) and steadfast love (chesed) co-present in same verse: 'according to your steadfast love remember me, for the sake of your goodness.' TOV root spans love (103) and goodness (67) cross-cluster. Question: is tuv (goodness) the content of chesed (steadfast love) — goodness as what love gives — or are they parallel divine attributes? The cross-cluster root family connection makes this one of the most structurally significant lexical bridges in the programme.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=296 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD010'
- Strong's ref: `H3033`
- Cross-registry: 71
- Raised: '2026-04-12'  ·  Session target: 'D'

> Jer 12:7 — 'I have given the beloved of my soul into the hands of her enemies.' God abandons his beloved Israel. The grief of abandoned love as a divine inner-being state. Does God experience grief as an inner-being characteristic? Cross-registry: love (103), grief (71), soul (182). This verse is one of the most striking in the programme for the divine inner life — God's love expressed through grief at its own loss.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=297 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD011'
- Strong's ref: `G0027`
- Cross-registry: 68
- Raised: '2026-04-12'  ·  Session target: 'D'

> Mat 3:17/Mar 12:6 — Father declares Jesus 'my beloved Son' at baptism. The Father-Son love as the archetype of all love. Does the programme have a registry examining the divine inner life as the model for the human inner life? The love between Father and Son is the origin-point from which all other love in the NT flows (Joh 17:26 — 'the love with which you loved me may be in them'). Cross-registry: love (103), grace (68), calling/identity (19), spirit cluster.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=298 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD012'
- Strong's ref: `H0160`
- Cross-registry: 117
- Raised: '2026-04-12'  ·  Session target: 'D'

> Zep 3:17 — 'He will quiet you by his love.' God's love produces rest/stillness/quietness in the beloved. Cross-registry: love (103), peace/rest (117), surrender (156). Question: is the peace produced by divine love a distinct inner-being state (rest/shalom), or is it the same state as love viewed from the receiving end? The verb 'quiet' (charash — to be still, to silence) suggests love has a stilling effect on inner agitation.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=299 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD013'
- Strong's ref: `G0025`
- Raised: '2026-04-12'  ·  Session target: 'D'

> Mat 5:44 — love of enemies also involves prayer for persecutors and good deeds and lending. The enemy-love complex shows love operating simultaneously across will (173), prayer (212), and action registers. Question: is the enemy-love command the programme's clearest example of a command that requires integration of all three levels of the inner person — affective orientation (love), volitional act (pray, do good), and cognitive reorientation (the rationale from divine character)?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=300 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD014'
- Strong's ref: `G0026`
- Cross-registry: 116
- Raised: '2026-04-12'  ·  Session target: 'D'

> 1Cor 13:4 — shared anchor with patience (116) and pride (123). The passage defines love by its relationship to patience (love is patient) and pride (love does not boast, is not arrogant). Does love produce patience as its characteristic inner quality under pressure? Or are love and patience distinct virtues sharing a common ground (the Spirit)? 1Cor 13 is the programme's richest cross-registry verse for the C17 cluster — nearly every quality named in vv.4-7 has its own registry.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=301 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD015'
- Strong's ref: `G0026`
- Cross-registry: 97
- Raised: '2026-04-12'  ·  Session target: 'D'

> Gal 5:22 — love heads the fruit-of-Spirit list. Subsequent fruits (joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control) may all be aspects or forms of love under different relational pressures. Each fruit has its own registry. Question: is love the source from which all other Spirit-fruits flow, or is it first among equals? If love generates joy, peace, patience, kindness etc., then love is not one inner virtue alongside others but the generative ground of the Spirit-formed inner life.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=302 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD016'
- Strong's ref: `G0027`
- Cross-registry: 19
- Raised: '2026-04-12'  ·  Session target: 'D'

> Mat 3:17 — Trinity nexus: Father declares love for Son as Spirit descends. The three-way structure (Father's love, Son's belovedness, Spirit's appearance) is the ground event of the NT. Cross-registry: love (103), spirit cluster, calling/identity (19). The declaration 'this is my beloved Son' grounds calling in love — identity is constituted by being-loved. Question: does the programme's calling registry (19) treat belovedness as the prior act that constitutes calling?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=303 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD017'
- Strong's ref: `H0160`
- Cross-registry: 71
- Raised: '2026-04-12'  ·  Session target: 'D'

> 2Sa 1:26 — David's lament for Jonathan: 'your love to me was extraordinary, surpassing the love of women.' Expressed in grief at Jonathan's death. The depth of grief reveals the depth of the prior love — grief as love's evidence under loss. Cross-registry: love (103), grief (71). Question: is grief structurally inseparable from love — not its opposite but its expression when love's object is lost? If so, love and grief may be the same inner state viewed from presence and absence.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=304 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD018'
- Strong's ref: `H2617A`
- Raised: '2026-04-12'  ·  Session target: 'D'

> Jer 31:34 — new covenant: universal knowledge of God, no longer needing instruction from neighbour, sin forgiven, love of neighbour fulfilled eschatologically. Cross-registry nexus: love (103), knowledge/thought (160), covenant (34), forgiveness (64), calling (19). The new covenant passage integrates multiple registries into a single eschatological vision. Question: is the programme's Session D synthesis meant to reconstruct this new covenant picture from its component registries?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=305 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD019'
- Strong's ref: `H7349`
- Cross-registry: 68
- Raised: '2026-04-12'  ·  Session target: 'D'

> Exo 34:6 divine self-declaration formula: rachum (compassionate) + grace + patience + chesed + faithfulness — five attributes of the divine inner character. The formula repeats verbatim across 8+ OT texts (Psa 86:15, 103:8, Joel 2:13, Jonah 4:2, Neh 9:17 etc.). Each attribute may have its own registry. Question: does the programme track the five-attribute formula as a cross-registry structure? The formula is the OT's most repeated self-characterisation of God and the model for human inner formation.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=306 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD020'
- Strong's ref: `G2705`
- Cross-registry: 64
- Raised: '2026-04-12'  ·  Session target: 'D'

> Luk 7:38-47 — woman's kisses and tears as bodily expression of love; Jesus' verdict: 'she loved much because she was forgiven much.' One of the most explicit causal chains in the NT: forgiveness → love. Cross-registry: love (103), forgiveness (64), grief/tears (71). Question: is love the primary inner response to forgiveness in the biblical data? If so, forgiveness may be the trigger that produces love, and love may be the inner evidence of received forgiveness.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=307 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD021'
- Strong's ref: `G5384`
- Cross-registry: 112
- Raised: '2026-04-12'  ·  Session target: 'D'

> Joh 15:15 — friendship with Christ defined by shared knowledge of the Father's purposes. 'I have called you friends, for all that I have heard from my Father I have made known to you.' Love takes the form of disclosure: God's inner purposes made known. Cross-registry: love (103), knowledge/thought (160), mind (112), calling (19). Question: is there a structural link between love and knowledge in the programme — does love require knowing and being known, not merely feeling?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=308 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD022'
- Strong's ref: `G0026`
- Cross-registry: 59
- Raised: '2026-04-12'  ·  Session target: 'D'

> 1Th 5:8 — breastplate of faith and love, helmet of hope. The armour metaphor maps virtues anatomically: faith-and-love at the chest (vital organs), hope at the head (mind/thought). Faith-love-hope as bodily armour, each protecting a vital centre. Cross-registry: love (103), faith (59), hope (78). Question: does the faith-love-hope triad represent the programme's three primary inner orientations toward God — trust (faith), attachment (love), expectation (hope)?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=309 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD023'
- Strong's ref: `G2705`
- Cross-registry: 71
- Raised: '2026-04-12'  ·  Session target: 'D'

> Act 20:37 — 'they embraced Paul and kissed him' at farewell. Somatic expression of love at anticipated permanent separation. The farewell scene is simultaneously an expression of love (embrace, kiss) and grief (weeping). Cross-registry: love (103), grief (71), fellowship/community (62). Question: is the farewell scene a structural locus where love and grief converge — where love's attachment is revealed by grief at separation?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=310 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD024'
- Strong's ref: `H8130`
- Cross-registry: 75
- Raised: '2026-04-12'  ·  Session target: 'D'

> Gen 29:31 — 'when the Lord saw that Leah was hated, he opened her womb.' Hated/unloved state triggers divine compassion expressed through fertility. The womb as the site where divine love responds to human hatred. Cross-registry: love (103), hatred (75), grief (71). The unloved woman's womb being opened by God is one of the OT's most concentrated statements about divine love compensating for human lovelessness.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=311 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD025'
- Strong's ref: `H7356B`
- Cross-registry: 23
- Raised: '2026-04-12'  ·  Session target: 'D'

> H7356B rachamim has approximately 23 contamination verses from H7358 rechem (physical womb) — Gen 20:18, 29:31, 30:22, Exo 13:2-15, Num 3:12, 8:16, 18:15 etc. The semantic boundary between rachamim (compassion) and rechem (womb) is productive (Isa 49:15 uses both deliberately), but the contamination verses represent a data quality issue. Session D must work with clean rachamim data. The boundary between anatomical womb and compassion-love is itself a significant theological question: when does the bodily become the inner-being?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=312 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD026'
- Strong's ref: `G0025`
- Cross-registry: 187
- Raised: '2026-04-12'  ·  Session target: 'D'

> C20 cluster (strength/might/authority/dominion — Regs 187/198/197/199) shares all 8 dimensions with love and co-occurs in 69-105 verses. This may be a registry-breadth effect, but the co-occurrence is genuine and large. Question: does the biblical vocabulary connect love and power structurally? Is love the form that power takes in the kingdom of God, and power the form that love takes in creation? The 1Cor 13 sequence — love as greater than gifts of power and knowledge — suggests love and power are in deliberate tension in the NT.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=313 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'DIM-103-SD027'
- Strong's ref: `G0025`
- Cross-registry: 156
- Raised: '2026-04-12'  ·  Session target: 'D'

> Surrender/yielding (Reg 156/180) has 33/4 co-occurrence/shared anchor records with love. The self-giving pattern of agapē (Joh 15:13 — greater love has no one than to lay down his life) and surrender (giving up the self) may be the same inner movement named from different angles: love as orientation, surrender as act. Question: is surrender the inner movement that makes love possible — does love require the prior surrender of self-assertion before it can give itself to another?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=314 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-103-SD028'
- Strong's ref: `G0025`
- Cross-registry: 73
- Raised: '2026-04-12'  ·  Session target: 'D'

> Reg 73 (guilt) has 32 co-occurrences with love — unexpected and analytically significant. Luk 7:47 — 'she loved much because she was forgiven much' — establishes guilt/forgiveness as the prior state that love responds to. Question: is guilt the inner state that love-as-forgiveness-response resolves? If guilt and love are consistently co-present at the verse level, there may be a causal chain: guilt → received forgiveness → love as response. Cross-registry: love (103), guilt (73), forgiveness (64).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=617 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'SP-103-029'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] 1Jo 4:18 — 'perfect love casts out fear.' Is fear the structural inner-being state that love displaces? What kind of fear? Does the OT support this structural opposition (Psa 27:1)? Formalises PH2-103-003.
> 
> Target: R061 (fear) / R103 (love)
> Connecting term: G0026 agapē / G5401 phobos (fear)
> Evidence basis: OBS-103-042/050

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=618 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'SP-103-030'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Luk 15:20 — is compassion the inner state that activates love's outward expression, or is compassion love itself under the condition of the returning?
> 
> Target: R023 (compassion) / R103 (love)
> Connecting term: G2705 katafileō / G4697 splanchnizō
> Evidence basis: OBS-103-057

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=619 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'SP-103-031'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Song 5:6 — 'my soul failed me.' Does love and soul have a constitutive relationship — the soul's vitality depending on the presence of the beloved?
> 
> Target: R182 (Soul) / R103 (love)
> Connecting term: H1730G dod / H5315 nephesh
> Evidence basis: OBS-103-062

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=620 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'SP-103-032'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Eze 16:8 — is love structurally prior to covenant, as the inner disposition that produces the covenant-act?
> 
> Target: R034 (covenant) / R103 (love)
> Connecting term: H1730H dod / berit (covenant)
> Evidence basis: OBS-103-083b

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=621 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'SP-103-033'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Jer 12:7 — does the programme's grief registry (71) evidence divine grief as an inner-being phenomenon? Are divine love and divine grief the same inner orientation under the condition of the beloved's loss?
> 
> Target: R071 (grief) / R103 (love) / R182 (Soul)
> Connecting term: H3033 yedidut / H5315 nephesh
> Evidence basis: OBS-103-086; DIM-103-002

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=622 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'SP-103-034'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Song 8:6 — (a) does the programme have a qinah registry? (b) does 'flame of Yah' support 1Jo 4:8 ('God is love') from the OT side?
> 
> Target: R103 (love) / jealousy-zeal registry (qinah) / divine nature
> Connecting term: H0160 ahavah / H7068 qinah
> Evidence basis: OBS-103-096

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=623 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'SP-103-035'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Isa 63:15 — does the programme's vocabulary for divine inner states include the me'eka somatic language? Does this parallel nephesh-of-God (Jer 12:7) as evidence of Scripture attributing inner-being states to God with the same vocabulary used for humans?
> 
> Target: R023 (compassion) / R103 (love)
> Connecting term: H7356B rachamim / me'eka (inner organs)
> Evidence basis: OBS-103-106

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=624 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'SP-103-036'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] 1Th 2:8 and Joh 15:13 — is there a structural sequence: love → surrender → giving of soul/self?
> 
> Target: R182 (Soul) / R156 (surrender) / R103 (love)
> Connecting term: G0027 agapētos / psuchē (soul)
> Evidence basis: OBS-103-123

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=625 · flag_code=`SD_POINTER` · priority='HIGH'

- Label: 'SP-103-037'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] Rom 5:5 — is the Spirit the structural mediator of divine love's entry into the human inner person across the programme's data?
> 
> Target: Spirit cluster / R103 (love) / R183 (heart)
> Connecting term: G0026 agapē / G4151 pneuma (Spirit)
> Evidence basis: OBS-103-126

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=626 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'SP-103-038'
- Raised: '2026-04-30T17:22:20Z'  ·  Session target: 'D'

> [v1.8 obslog SD pointer] 2Ti 3:2 — does the programme have a self-love registry? Is there a coherent programme account of self-love as both (a) normal self-regard enabling 'love your neighbour as yourself' and (b) disordered self-love heading the last-days inner collapse?
> 
> Target: R103 (love) / self-love (R_unknown — filautos)
> Connecting term: G5367 filautos
> Evidence basis: OBS-103-137

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R152 strife — 1 unresolved

#### srf.id=167 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-152-SD001'
- Strong's ref: `H7230`
- Raised: '2026-04-08'  ·  Session target: 'D'

> rov (H7230, abundance) in the strife registry (group 1142-001) is assigned Divine-Human Correspondence because both anchors have GOD as subject (divine weariness of ritual; divine steadfast love) while related verses carry the human moral-failure pole. This raises a programme-level question: does the biblical vocabulary of magnitude (rov, rabah, and cognates) consistently operate in divine-human correspondence mode — the greatness of divine attributes set against and corresponding to the weight of human moral condition? Session D should examine this across all registries where magnitude vocabulary appears.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

## §3. Session D term links

_(None — no `session_d_term_links` rows reference this cluster's terms.)_

---

## Output reconciliation document (AI authors this)

AI produces `Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-reconciliation-v1-{date}.md` carrying the dispositions and rationales per row.

Then CC executes the reconciliation directive `wa-cluster-{code}-dir-NNN-inherited-findings-reconcile-v1-{date}.md` per v2_0 §13.4.

*End of inherited-findings report.*