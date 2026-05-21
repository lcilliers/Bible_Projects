# M01 Fear, Dread and Terror — Inherited findings for Phase 10 reconciliation

**Generated:** 2026-05-16T06:08:50Z  
**Cluster:** `M01` (Fear) · status=Analysis - In Progress · version=v6  
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §13 (Phase 10 — Inherited-finding reconciliation)  
**Source:** `database/bible_research.db`  

**Scope:** every inherited Session B finding, research flag, and Session D pointer attached to this cluster's contributor registries that has **not been resolved** by the legacy pipeline. AI's Phase 10 task is to assign a disposition per row (see §13.2 of the instruction). Resolved rows (`status='resolved_*'` or `resolved=1`) are excluded.

**Linkage path:** cluster's `mti_terms` → `owning_registry_fk` → `word_registry` → matching rows in `wa_session_b_findings`, `wa_session_research_flags`, and `session_d_*`.

---

## Summary

| Source | Total unresolved |
|---|---:|
| `wa_session_b_findings` (status IN (open, pending, confirmed)) | **13** |
| `wa_session_research_flags` (resolved=0) | **11** |
| `session_d_term_links` (this cluster's terms) | **0** |

**Contributor registries:** 12

| no | registry_id | word |
|---:|---:|---|
| 1 | 1 | abomination |
| 4 | 4 | anger |
| 5 | 5 | anguish |
| 7 | 7 | anxiety |
| 11 | 11 | awe |
| 18 | 18 | brokenness |
| 51 | 51 | distress |
| 53 | 53 | dread |
| 61 | 61 | fear |
| 151 | 151 | sorrow |
| 158 | 158 | terror |
| 175 | 175 | wonder |

**Finding types in unresolved set:**

- `DIMENSION_REVIEW`: 13

**Flag codes in unresolved set:**

- `SD_POINTER`: 3
- `VERSE_EVIDENCE_BREADTH_NOTE`: 3
- `PH2_CROSS_REGISTRY_REQUIRED`: 2
- `PH2_THEOLOGICAL_DEPTH_REQUIRED`: 1
- `PH2_DATA_ERROR`: 1
- `PH2_BOUNDARY_QUESTION`: 1

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

### R001 abomination — 1 unresolved

#### sbf.id=106 · finding_id='DIM-001-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> The new covenant transformation group (3272-001: diatithēmi — the covenantal act writing divine law on the inner mind and heart) appears in the abomination registry. This places the new covenant's inner transformation as the divine answer to abomination and inner defilement. Session B should examine whether the abomination cluster's verse evidence shows the new covenant specifically as the remedy for abomination — and whether this pattern recurs across the cluster.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R004 anger — 2 unresolved

#### sbf.id=71 · finding_id='DIM-4-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Anger governance is the paradigmatic inner-being governance challenge in Reg 4. Groups 79-004 (mastery of anger exceeds military conquest), 1554-001 (trembling restraint before God without sin), 38-001 (morally accountable anger under divine command), and 139-003 (wisdom counsel not to let anger kindle) show anger mastery as a distinct and critical sub-theme. Session B should map the vocabulary of anger-governance as a structured inner-being claim about will, character, and spiritual posture.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=72 · finding_id='DIM-4-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Two groups (1552-001: fierce anger co-existing with grief/loyalty; 37-003: righteous anger co-existing with sorrow at hardness of heart) show the inner being holding anger and love, or anger and grief, simultaneously as genuine compound affective states. Session B should examine whether Scripture treats compound anger-with-grief as a distinct inner-being mode and what theological conditions produce it.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R005 anguish — 1 unresolved

#### sbf.id=59 · finding_id='DIM-005-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Group 4667-002 (H7114A qa.tser, be short — divine yielding): assigned Theological/Divine-Human. This group names divine pathos — God himself moved by the misery of his people. It is one of the clearest instances in the anguish registry of Scripture attributing an inner affective response to God. Session B should note this as a significant theological dimension within Registry 5 and consider its relationship to the broader divine-pathos theme across C05.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R007 anxiety — 1 unresolved

#### sbf.id=65 · finding_id='DIM-7-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> merimnaō (G3309) operates in two distinct inner-being registers: anxious affective worry (2709-001, 2709-002) and volitional-attentional directed care (2709-003, 350-001). Session B should map how the same word spans these two registers and what this reveals about anxiety as both an affective state and a directional inner-being act.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R011 awe — 1 unresolved

#### sbf.id=38 · finding_id='DIM-11-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`
- Anchor verses: Psa 27:1; Psa 111:10; Isa 8:13; Deu 6:5

> Awe spans both Affective/Emotional and Spiritual/God-ward dimensions. God-ward groups (1682-001, 1682-003, 703-002, 703-003) show that the deepest fear/awe content is Spiritual/God-ward rather than merely affective. Session B should examine whether awe functions as a distinct inner-being category integrating affective intensity and God-ward orientation — the two are inseparable in the data.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R018 brokenness — 1 unresolved

#### sbf.id=60 · finding_id='DIM-018-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Registry 18 (brokenness) is the most dimensionally uniform registry in C05: all 6 groups converge on Affective/Emotional. The she.ver and related vocabulary names breaking, wounding, and shattering as inner-being conditions. This sub-theme — the inner person as something that can be broken and must be healed — is a coherent and distinctive contribution within the C05 cluster that Session B should treat as a unit.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R051 distress — 3 unresolved

#### sbf.id=31 · finding_id='DIM-051-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-06'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.2-2026-04-06`

> H7379 (riv, strife/contention) has 2 healthy active groups in distress (#51): 234-001 (strife/contention, 19 verses) and 234-002 (pleading one's cause, 26 verses). A third group was created for the indictment/controversy sense — God's legal case against his people in the prophetic tradition — but was never populated with verse_context records and has been delete_flagged. Session B analyst should assess whether this prophetic lawsuit dimension of H7379 belongs within distress and whether the verse evidence warrants a third group. Candidate verses would be found in prophetic lawsuit texts (Isaiah, Jeremiah, Micah) where H7379 names God's formal contention with Israel.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=61 · finding_id='DIM-051-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Group 235-002 (H7451A ra, harmful spirit afflicting Saul): assigned Theological/Divine-Human. This group sits on the boundary between demonological, psychological, and theological dimensions — the harmful spirit is theologically constituted (sent by God per 1 Sam 16) but produces what functions as an inner-psychological affliction. The existing dimension vocabulary may be inadequate to name this precisely. Session B should examine the verse evidence and consider whether a note on the vocabulary gap is warranted.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=62 · finding_id='DIM-051-003' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> Registry 51 (distress) contains a significant cluster of outlier groups arriving via XREF terms that are outside the suffering domain: 242-001 (meditation/contemplation, Cognitive/Mind), 3600-001 (divine forming of the inner person, Theological/Divine-Human), 5129-002 (opened ear as inner receptivity, Spiritual/God-ward), 5168-001 (embrace as expression of fulfilment, Affective/Emotional), 5124-001 and 5126-001 (amazement/astonishment). These should be treated as peripheral in Session B analysis of Registry 51 and may warrant a vocabulary or cluster note.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R061 fear — 2 unresolved

#### sbf.id=67 · finding_id='DIM-61-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> fobeō (G5399) shows a tripartite inner-being structure: (1) theophanic/miraculous fear leading to worship (Spiritual/God-ward), (2) reverential life-shaping fear of God (Spiritual/God-ward), (3) practical self-interested fear before humans or consequences (Affective/Emotional). This tripartite structure is the most analytically important pattern in Registry 61 and should be the organising frame for Session B analysis.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

#### sbf.id=68 · finding_id='DIM-61-002' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`

> ya.re (H3372G) groups add the divine 'Fear not' command (298-001) as a structuring element — showing the divine address to inner fear as a distinct inner-being category. The reassurance pattern (divine declaration of presence + commanded displacement of fear) is significant for understanding how the inner-being state of fear is meant to be transformed.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

### R175 wonder — 1 unresolved

#### sbf.id=47 · finding_id='DIM-175-001' · status=`pending` · type=`DIMENSION_REVIEW`

- Raised: '2026-04-07'  ·  Pass: None  ·  Segment: None
- Instruction version: `WA-DimensionReview-Instruction-v1.3-2026-04-07`
- Anchor verses: Psa 77:14; Isa 9:6; Act 3:10-11; Heb 2:4

> Wonder vocabulary divides between the divine side (Theological/Divine-Human) and the human response (Affective/Emotional). Session B should examine wonder as the inner state at the interface between human capacity and divine transcendence — the point where the inner person's capacity to comprehend is exceeded by what God is and does.

**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________

---

## §2. Unresolved research flags

### R001 abomination — 1 unresolved

#### srf.id=142 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-001-SD001'
- Cross-registry: 39
- Raised: '2026-04-07'  ·  Session target: 'D'

> The new covenant transformation group (3272-001) appears in the abomination registry and salvation vocabulary groups appear in the debauchery registry (Reg 39) — both placing redemptive vocabulary within moral-failure/defilement registries through the XREF mechanism. Session D should examine whether this is a programme-wide pattern: are there other clusters where redemptive/salvation vocabulary appears in moral-failure registries via XREF, and what does this reveal about the inner-being logic connecting defilement and redemption in Scripture?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R004 anger — 6 unresolved

#### srf.id=13 · flag_code=`PH2_CROSS_REGISTRY_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-004-001'
- Strong's ref: `H7307J`
- Raised: '2026-03-24'  ·  Session target: 'D'

> H7307J (ruach: temper) places the governance of anger at the spirit level. Pro 16:32; 17:27; 25:28; 29:11 treat ruling the spirit as the governing capacity for anger. Cross-registry analysis with spirit (reg 184) required before the anger-spirit boundary can be mapped. Session D priority question: is governing anger a spirit operation, and what does that imply for the spirit-soul boundary?

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=14 · flag_code=`PH2_CROSS_REGISTRY_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-004-002'
- Strong's ref: `H2195`
- Raised: '2026-03-24'  ·  Session target: 'D'

> Za.am family (H2194 verbal, H2195 nominal) sits at the boundary of the anger registry (reg 4) and the abomination/indignation registry (reg 1). H2194 verbal form is in reg 1; H2195 noun form is here. Full treatment requires cross-registry comparison. Current analysis treats H2195 as belonging to anger; reg 1 analysis must address the verbal form. Phase 2 to determine primary ownership.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=15 · flag_code=`PH2_THEOLOGICAL_DEPTH_REQUIRED` · priority='MEDIUM'

- Label: 'PH2-004-003'
- Strong's ref: `G3709`
- Raised: '2026-03-24'  ·  Session target: 'D'

> NT orgē as eschatological divine wrath (Rev 6:16-17 wrath of the Lamb; Rev 14:10; 16:1; 19:15) represents a significant theological development of OT divine anger vocabulary. Full treatment requires cross-registry analysis with justice, judgment, and atonement vocabulary. Connection to Isa 53 soul registry (soul poured out) worth exploring: the cross as simultaneous expression of divine anger and divine love.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=16 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='MEDIUM'

- Label: 'PH2-004-004'
- Strong's ref: `G3709`
- Raised: '2026-03-24'  ·  Session target: 'D'

> G3709 orgē has 272 occurrences but only 33 verses in the export. The full Pauline wrath theology and the Revelation bowl judgment sequence require additional verse coverage before synthesis conclusions are drawn. Priority: complete Pauline wrath vocabulary (Romans 1-5, 9, 12, 13; Eph 2, 4, 5; Col 3; 1Th 1, 2, 5) and Revelation wrath sequence (Rev 6, 11, 14, 15, 16, 19).

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=17 · flag_code=`PH2_DATA_ERROR` · priority='MEDIUM'

- Label: 'PH2-004-005'
- Strong's ref: `H7110B`
- Raised: '2026-03-24'  ·  Session target: 'D'

> H7110B (qe.tseph: splinter, Joel 1:7) carries a verse count of 28 erroneously shared with H7110A (qe.tseph: wrath). H7110B is a homonym with no anger content. Assigned delete status in MTI. H7110A holds the correct verse data for the wrath meaning.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=18 · flag_code=`PH2_BOUNDARY_QUESTION` · priority='MEDIUM'

- Label: 'PH2-004-006'
- Strong's ref: `G3948`
- Raised: '2026-03-24'  ·  Session target: 'D'

> G3948 paroxusmos appears both negatively (Act 15:39, Paul-Barnabas sharp dispute) and positively (Heb 10:24, stir up one another to love and good deeds). The stirring-up mechanism that produces relational conflict is also available for positive relational catalysis. Minor but analytically interesting for the relational vocabulary study in Session D.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R007 anxiety — 2 unresolved

#### srf.id=27 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='MEDIUM'

- Label: 'PH2-007-001'
- Strong's ref: `G4329`
- Raised: '2026-03-25'  ·  Session target: 'D'

> G4329 prosdokia has 5 occurrences (STEP) but only 2 verse records in export. The foreboding/apprehension sense (Luk 21:26) is analytically significant but the dataset is too thin for confident conclusions. Phase 2 independent research required before synthesis-level use of this term.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

#### srf.id=28 · flag_code=`VERSE_EVIDENCE_BREADTH_NOTE` · priority='LOW'

- Label: 'PH2-007-002'
- Strong's ref: `G4328`
- Raised: '2026-03-25'  ·  Session target: 'D'

> G4328 prosdokaō has 20 occurrences but only 15 verses in export; anxiety-register content is present in a minority of these. The anxiety dimension is contextual not lexical. Analysis limited to anxiety-valenced verses (Act 27:33, Act 28:6, Mat 24:50/Luk 12:46 context). Full corpus review in Phase 2 recommended.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R011 awe — 1 unresolved

#### srf.id=122 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-11-SD001'
- Raised: '2026-04-07'  ·  Session target: 'D'

> The commanded-inner-state pattern — Scripture commanding specific inner orientations (do not be dismayed / fear the Lord / rejoice always) — appears across Registries 11, 97, 42 and likely others. Session D should trace this pattern across clusters and examine its implications for understanding the inner being as subject to divine instruction.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

### R061 fear — 1 unresolved

#### srf.id=130 · flag_code=`SD_POINTER` · priority='MEDIUM'

- Label: 'DIM-61-SD001'
- Raised: '2026-04-07'  ·  Session target: 'D'

> C06 fear cluster shows a tripartite dimension pattern: fear-as-God-ward-orientation (Spiritual/God-ward ~18 groups), fear-as-inner-affect (Affective/Emotional ~37 groups), fear-as-volitional-collapse (Volitional/Will 5 groups). This tripartite structure — orientation, affect, will-collapse — may be a cross-registry finding about how negative inner states operate in biblical anthropology. Session D should examine whether the same pattern appears in other C06 registries and beyond.

**Disposition (AI):** ____________  ·  **Rationale:** ____________

---

## §3. Session D term links

_(None — no `session_d_term_links` rows reference this cluster's terms.)_

---

## Output reconciliation document (AI authors this)

AI produces `Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-reconciliation-v1-{date}.md` carrying the dispositions and rationales per row.

Then CC executes the reconciliation directive `wa-cluster-{code}-dir-NNN-inherited-findings-reconcile-v1-{date}.md` per v2_0 §13.4.

*End of inherited-findings report.*