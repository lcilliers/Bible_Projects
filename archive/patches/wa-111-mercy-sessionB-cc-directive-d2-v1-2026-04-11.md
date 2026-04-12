# Session B — CC Directive D2
## Registry 111 — mercy
## Passes 4–6 Directives
## Version: v1 | 2026-04-11
## Governing instruction: WA-SessionB-Analysis-Instruction-v4.7-2026-04-11
## Delivery point: D2 — after Pass 6 PASS COMPLETE

---

## Context

This directive delivers all database operations generated during Passes 4, 5, and 6 of Stage 2 Session B for Registry 111 (mercy). After these operations are applied and confirmed, Claude Code produces fresh extract R3. Stage 3 (Session C validation and update) cannot begin until R3 is in hand and spot-checked.

---

## D2 Operations

### Operation D2-001 — SOMATIC_INNER_LINK flags (wa_term_phase2_flags, flag_id=3)

**Basis (Pass 4a/4b):** Four owner terms where the body is central to the term's functional meaning — blood/hand/soul in the atonement act (kip.per), blood/face at the mercy seat (kap.po.ret), face/eye/soul/fasting/weeping in grace-seeking (cha.nan), heart/hand/eyes in supplication (te.chin.nah).

**SQL:**
```sql
-- First confirm flag_id for SOMATIC_INNER_LINK in phase2_flag_types
SELECT id, flag_code FROM phase2_flag_types WHERE flag_code = 'SOMATIC_INNER_LINK';

-- Insert (assuming flag_id=3 per WA-Reference Section 13.3):
INSERT OR IGNORE INTO wa_term_phase2_flags (term_inv_id, flag_id, description, source, raised_date)
VALUES
  (3304, 3, 'Blood/hand/soul/face — body is instrument and recipient of atoning act. Lev 17:11 (blood-for-soul), Lev 1:4 (laying on of hand), Gen 32:20 (cover the face).', 'Session B v4.7 Pass 4', '2026-04-11'),
  (1042, 3, 'Blood/face — blood sprinkled on mercy seat (Lev 16:14); cherubim faces overshadowing (Exo 25:20). Body and its products are the ritual instrument.', 'Session B v4.7 Pass 4', '2026-04-11'),
  (1045, 3, 'Face/eye/soul/fasting/weeping — grace mediated through face-direction (Num 6:25), sought through bodily self-denial (2Sa 12:22, Isa 30:19).', 'Session B v4.7 Pass 4', '2026-04-11'),
  (1046, 3, 'Heart/hand/eyes — supplication posture: knowing affliction of heart (1Ki 8:38), stretched hands toward temple, eyes open to plea (1Ki 8:52).', 'Session B v4.7 Pass 4', '2026-04-11');
-- term_inv_ids: H3722A=3304, H3727=1042, H2603A=1045, H8467=1046
```

---

### Operation D2-002 — BODY_INNER_EXPRESSION flags (wa_term_phase2_flags, flag_id=4)

**Basis (Pass 4b):** Body expresses the inner state of mercy-seeking and mercy-response.

**SQL:**
```sql
-- Confirm flag_id for BODY_INNER_EXPRESSION
SELECT id, flag_code FROM phase2_flag_types WHERE flag_code = 'BODY_INNER_EXPRESSION';

INSERT OR IGNORE INTO wa_term_phase2_flags (term_inv_id, flag_id, description, source, raised_date)
VALUES
  (3311, 4, 'Eyes/breast/beating (Luk 18:13) — tax collector enacts inner posture of total humility through three simultaneous somatic gestures: distance, downcast eyes, chest-beating.', 'Session B v4.7 Pass 4', '2026-04-11'),
  (1057, 4, 'Body/bodies (Rom 12:1) — presenting bodies as response to oiktirmos of God; splagchna oiktirmou (Col 3:12) — compassionate hearts as inner garment expressed through conduct.', 'Session B v4.7 Pass 4', '2026-04-11'),
  (1045, 4, 'Fasting/weeping as bodily expression of mercy-seeking inner state (2Sa 12:22, Isa 30:19). H2603A receives both SOMATIC_INNER_LINK and BODY_INNER_EXPRESSION.', 'Session B v4.7 Pass 4', '2026-04-11'),
  (1046, 4, 'Stretched hands (1Ki 8:38/54) as bodily expression of supplication inner posture. H8467 receives both SOMATIC_INNER_LINK and BODY_INNER_EXPRESSION.', 'Session B v4.7 Pass 4', '2026-04-11');
-- term_inv_ids: G2433=3311, G3628=1057, H2603A=1045, H8467=1046
```

---

### Operation D2-003 — sb_classification and sb_classification_reasoning

**SQL:**
```sql
UPDATE word_registry
SET
  sb_classification = 'Spirit-soul interface',
  sb_classification_reasoning = 'Mercy is received at spirit level — it originates in God and is mediated through the propitiation mechanism (a divine provision, not human achievement). It is expressed at soul level as compassion toward the other, directed in supplication toward God, and enacted in concrete acts of favour. The body mediates both directions: atoning blood provides the spirit-level covering (Lev 17:11); supplication posture expresses the soul-level appeal (Luk 18:13, 1Ki 8:38). Confidence: medium. Trichotomy-spanning alternative considered: the atonement sub-vocabulary has deep somatic involvement, but this operates instrumentally rather than as primary locus. Spirit-soul interface holds unless Session D corpus evidence indicates body-level transformation as an independent outcome of mercy.'
WHERE no = 111;
```

**Verification:**
```sql
SELECT sb_classification, sb_classification_reasoning FROM word_registry WHERE no = 111;
```

---

### Operation D2-004 — Session D pointer flags (wa_session_research_flags)

Insert SD_POINTER flags for all new cross-registry pointers raised in Passes 4–6. The existing DIM-111-SD001 flag (label) uses DIMREVIEW_SESSION_D code and is not touched. New flags use SD_POINTER code and PH2-111-NNN label sequence starting at PH2-111-001.

**SQL:**
```sql
INSERT INTO wa_session_research_flags
  (registry_id, flag_code, flag_label, priority, session_target, description, session_raised, raised_date, resolved)
VALUES

-- PH2-111-001: Power/mercy structural relationship (new in Pass 6)
(111, 'SD_POINTER', 'PH2-111-001', 'HIGH', 'D',
 'Strength/power/authority/dominion registries (Reg 187/196/197/198/199) share all 4 of mercy dimensions (Relational Disposition, Moral Character, Dependence/Creatureliness, Divine-Human Correspondence). This is the strongest unexpected dimensional overlap. Structural question: is mercy the moral direction of power toward the vulnerable — mercy as the inner disposition that determines how power is used? Evidence: Psa 78:38 (God restrained his anger — mercy as restraint of power); God rich in mercy (Eph 2:4) — abundance of mercy alongside sovereignty. Session D to examine whether power and mercy form a structural inner-being pair: power names the capacity; mercy names its relational direction.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-002: Guilt as precondition of mercy-seeking
(111, 'SD_POINTER', 'PH2-111-002', 'HIGH', 'D',
 'Reg 73 (guilt) shares 9 terms with mercy — primarily the supplication vocabulary (cha.nan, te.chin.nah). Guilt appears as the inner condition that generates authentic mercy-seeking. Evidence: Dan 9:20 (Daniel confesses sin while presenting te.chin.nah); Luk 18:13 (tax collector identifies as sinner in his mercy cry); Psa 51:1 (mercy appeal grounded in acknowledged transgression). Structural question: is guilt the anthropological precondition of mercy-reception — can mercy be received without prior acknowledgement of the condition that requires it? Session D to examine the guilt-mercy sequence.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-003: Mercy-justice structural relationship
(111, 'SD_POINTER', 'PH2-111-003', 'HIGH', 'D',
 'Jam 2:13 and Mat 23:23 both encode a mercy-justice structural relationship. Jam 2:13: judgment without mercy vs. mercy triumphing over judgment — mercy is not the absence of judgment but the stronger category. Mat 23:23: justice, mercy, faithfulness as the three weightier matters of the law. Structural question: does mercy operate as a judicial category in its own right, or as the suspension/transformation of justice? Cross-reference Mic 6:8 (do justice, love mercy, walk humbly) for a third triad. Session D to examine whether the programme data encodes a mercy-justice-faithfulness cluster as a coherent inner-being portrait of covenantal character.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-004: Love → mercy causal chain (primary evidence 1Jo 4:10, Eph 2:4)
(111, 'SD_POINTER', 'PH2-111-004', 'HIGH', 'D',
 '1Jo 4:10 states the causal sequence: divine love → sending of Son → propitiation → mercy received. Eph 2:4 pairs love and mercy as motivation and expression: "God, being rich in mercy, because of the great love with which he loved us." Love is the cause; mercy is love directed toward the guilty/needy. Structural question: is mercy a form of love (love toward the undeserving specifically), or is love a broader category of which mercy is one expression? Session D to examine the love-mercy structural relationship across Reg 103 (love) and Reg 111 (mercy).',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-005: Mercy-wrath shared persistence structure
(111, 'SD_POINTER', 'PH2-111-005', 'MEDIUM', 'D',
 'The od particle (H5750) names sustained divine inner dispositions in two opposite directions: God''s mercy endures (Hab 2:3 — the vision still awaits); God''s anger is stretched out still (Isa 5:25). Both mercy and wrath are characterised by duration and sustenance using the same vocabulary. Structural question: do mercy and wrath share a structural feature (both sustained, both arising from divine inner character) that unifies them at a deeper level — both as expressions of the same divine faithfulness? Session D to examine the mercy-wrath persistence structure across the anger registries (pool1-anger-pair) and Reg 111.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-006: Mercy-induced shame (distinct from shame-of-exposure)
(111, 'SD_POINTER', 'PH2-111-006', 'MEDIUM', 'D',
 'Eze 16:63 names shame as the inner experience of having received comprehensive mercy for the unforgivable: "you may remember and be confounded, and never open your mouth again because of your shame, when I atone for you." This is not the shame of exposure (pre-forgiveness) but the reverent silence of the fully forgiven. Structural question: does the shame vocabulary contain a distinct category of mercy-induced shame that functions differently from judgment-shame? Session D to examine with Reg 146 (shame) — specifically whether the shame that follows comprehensive mercy is structurally distinct and how the programme data represents it.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-007: Prayer producing divine inner movement (2Ch 33:13)
(111, 'SD_POINTER', 'PH2-111-007', 'MEDIUM', 'D',
 '2Ch 33:13 uses the Niphal of a.tar for both Manasseh''s prayer and God''s response: he prayed (va.ye.ta.r) and God was moved by his entreaty (va.ye.a.ter lo). The same root names the human act and the divine inner movement it produces. This encodes a theology of divine responsiveness: prayer can affect the divine inner disposition. Structural question: does the prayer vocabulary (Reg 212) consistently encode a theology of divine responsiveness as a structural feature, or is 2Ch 33:13 exceptional? Session D to examine across prayer and mercy registries.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-008: Mercy → comfort causal chain and Paraclete question
(111, 'SD_POINTER', 'PH2-111-008', 'MEDIUM', 'D',
 '2Cor 1:3 pairs "Father of mercies" (oiktirmos) with "God of all comfort" (paraklesis). The Father of mercies produces comfort. Structural question: is comfort the pastoral/experiential output of received mercy? And does this connect to the Spirit as Paraclete (parakletos) — is the Spirit''s comforting function structurally grounded in divine mercy? Session D to examine the mercy-comfort-Spirit triangle across relevant registries.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-009: Blood-atonement somatic vocabulary and flesh/body registries
(111, 'SD_POINTER', 'PH2-111-009', 'MEDIUM', 'D',
 'Pass 4 somatic scan confirmed blood as the dominant somatic element in the atonement sub-vocabulary (H3722A kip.per, H3727 kap.po.ret, G2435 hilastērios, H3725 kip.pu.rim). Lev 17:11 grounds this: "the life of the flesh is in the blood... the blood makes atonement for the soul." This is the most concentrated overlap between mercy and flesh/body registries. Structural question: does the mercy-through-blood mechanism reflect a structural relationship between mercy, body, and the atonement of the flesh-condition? Session D to examine with Reg 185 (flesh).',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-010: Self-knowledge as supplication prerequisite
(111, 'SD_POINTER', 'PH2-111-010', 'MEDIUM', 'D',
 '1Ki 8:38: "each knowing the affliction of his own heart (yada et nega levavo) and stretching out his hands toward this house." Authentic te.chin.nah (supplication) presupposes self-knowledge of inner condition. The supplicant who comes to God in mercy must know their own inner state. Structural question: does authentic mercy-seeking require prior self-knowledge of inner condition as a structural feature? Session D to examine whether conscience/self-knowledge vocabulary consistently co-occurs with mercy-seeking vocabulary.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-011: Chinnam/chen root — gratuitous suffering and gratuitous grace
(111, 'SD_POINTER', 'PH2-111-011', 'MEDIUM', 'D',
 'Job 2:3: God permits destroying Job "without reason" (chinnam — H2600, from cha.nan root). The same root that names grace-freely-given (cha.nan) also names suffering-without-cause (chinnam). Pass 3 identified this: gratuitousness is shared — mercy is given freely; Job''s affliction comes freely. Structural question: is there a structural relationship between unmerited suffering and unmerited favour through the cha.nan root? Does the programme data support a connection between the vocabulary of grace-freely-given and suffering-without-cause? Session D.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-012: Faith as mercy-seat access (Rom 3:25)
(111, 'SD_POINTER', 'PH2-111-012', 'MEDIUM', 'D',
 'Rom 3:25: Christ is put forward as hilastērios "to be received by faith." Faith is the mode of accessing the mercy seat — the mechanism that brings the supplicant to the locus of propitiation. Structural question: does the faith vocabulary (Reg 59) consistently function as the mechanism of access to mercy in the NT? Is faith the NT equivalent of the priestly blood-sprinkling as the means of mercy-seat approach? Session D to examine the faith-mercy-seat connection across Reg 59 and Reg 111.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-013: Peace as mercy''s relational outcome
(111, 'SD_POINTER', 'PH2-111-013', 'MEDIUM', 'D',
 'Reg 117 (peace) shares 3 dimensions with mercy (Dependence/Creatureliness, Moral Character, Relational Disposition). Isa 54:10 names covenant of peace alongside steadfast love/mercy. Structural question: is peace the relational state that mercy produces in the restored relationship? Does mercy precede peace sequentially — mercy covers the breach; peace names the restored condition? Session D to examine the mercy-peace sequence in the prophetic tradition.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-014: Mercy seat as locus of divine communication
(111, 'SD_POINTER', 'PH2-111-014', 'LOWER', 'D',
 'Exo 25:22: "from above the mercy seat I will speak with you." The mercy seat is not only the place of atonement but the place of divine speech. Mercy and revelation share a location — the architectural ground of divine-human communication is the mercy seat. Structural question: does mercy provide the structural ground for divine-human communication? Is it only from the mercy-provided standing that God can speak and humans can hear? Session D to examine whether the word/revelation vocabulary has structural dependence on the mercy vocabulary.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0),

-- PH2-111-015: Pity/compassion overlap with yearning/desire vocabulary
(111, 'SD_POINTER', 'PH2-111-015', 'LOWER', 'D',
 'Reg 179 (yearning), 43 (desire), 42 (delight) share 3 terms each with mercy — H2550 chamad (to show compassion/pity) and related terms. The chamad root covers both desire and pity — a semantic overlap between what one longs for and what one has compassion toward. Structural question: does the compassion/pity vocabulary share a semantic root with desire/yearning in Hebrew, and if so, what does this reveal about the inner-being structure of mercy — is mercy related to longing? Session D.',
 'WA-SessionB-Analysis-Instruction-v4.7-2026-04-11', '2026-04-11', 0);
```

**Verification:**
```sql
SELECT flag_label, flag_code, session_target FROM wa_session_research_flags
WHERE registry_id = 111 ORDER BY flag_label;
-- Expected: DIM-111-SD001 + PH2-111-001 through PH2-111-015 = 16 total
```

---

## R3 Extract Request

After D2-001 through D2-004 are applied and confirmed, produce fresh extract R3:

```
CC DIRECTIVE — FRESH EXTRACT R3
Registry: 111 — mercy
Action: Produce fresh complete export
Filename: wa-111-mercy-complete-2026-04-11-r3.json
Reason: D2 directives (Passes 4–6) applied and confirmed. Stage 3 requires fully updated extract.
Confirm:
  - wa_term_phase2_flags: SOMATIC_INNER_LINK (flag_id=3) on H3722A, H3727, H2603A, H8467
  - wa_term_phase2_flags: BODY_INNER_EXPRESSION (flag_id=4) on G2433, G3628, H2603A, H8467
  - word_registry: sb_classification = 'Spirit-soul interface' and sb_classification_reasoning populated
  - wa_session_research_flags: 16 total records (DIM-111-SD001 + PH2-111-001 through PH2-111-015)
  - All Stage 1 and D1 changes still present
```

---

## D2 Delivery Summary

| Op | Type | Target | Count |
|---|---|---|---|
| D2-001 | SQL insert — wa_term_phase2_flags | 4 terms | SOMATIC_INNER_LINK flag_id=3 |
| D2-002 | SQL insert — wa_term_phase2_flags | 4 terms | BODY_INNER_EXPRESSION flag_id=4 |
| D2-003 | SQL update — word_registry | registry 111 | sb_classification + reasoning |
| D2-004 | SQL insert — wa_session_research_flags | 15 new SD_POINTER flags | PH2-111-001 to 015 |

**Note on flag_ids:** Confirm SOMATIC_INNER_LINK=flag_id 3 and BODY_INNER_EXPRESSION=flag_id 4 from phase2_flag_types table before inserting D2-001 and D2-002. If IDs differ, adjust and report.

**Return to Claude AI:** Confirmation of all four operations, flag_id values used, and filename of R3 extract.

---
