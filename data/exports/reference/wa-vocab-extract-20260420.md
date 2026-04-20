# WA Controlled Vocabularies — 2026-04-20

_Schema 3.13.0 · extractor v1.0_

_Source: DB `wa_vocab_set` + `wa_vocab_member`._

---

## Summary

**Sets:** 5  ·  **Total members:** 27

### DIMENSION_CONFIDENCE — Dimension Review — Classification Confidence

**Governing:** wa-dimensionreview-instruction [current]  
**Applies to:** `wa_dimension_index.dimension_confidence`  
**Members:** 3

_Source/confidence marker for a dimension assignment. KEYWORD_WEAK / KEYWORD_STRONG are automated-classifier outputs pending review. CLAUDE_AI is post-review analyst assignment._

| Value | Description |
|---|---|
| `KEYWORD_WEAK` | Automated classifier weak match — starting hypothesis, pending review |
| `KEYWORD_STRONG` | Automated classifier strong match — starting hypothesis, pending review |
| `CLAUDE_AI` | Claude AI post-review analyst assignment — reviewed and confirmed |

### DIMENSION_LABEL — Dimension Review — 11 Inner-Being Dimensions

**Governing:** wa-dimensionreview-instruction [current] §7.7  
**Applies to:** `wa_dimension_index.dimension`  
**Members:** 11

_Canonical 11-dimension vocabulary used to classify verse-context groups during Dimension Review. Researcher-ratified 2026-04-20. Extension requires researcher decision per DR-13._

| Value | Description |
|---|---|
| `01 — Emotion — Positive` | Inner states of pleasure, joy, delight, or satisfaction |
| `02 — Emotion — Negative` | Inner states of pain, distress, grief, fear, anger, shame, or anxiety |
| `03 — Cognition` | Inner acts of knowing, perceiving, remembering, understanding, and discerning |
| `04 — Volition` | Inner acts of willing, purposing, choosing, desiring, and deciding |
| `05 — Moral Character` | Stable inner qualities of moral nature — goodness, justice, integrity, purity, faithfulness |
| `06 — Relational Disposition` | Inner orientation toward another — love, compassion, favour, attachment, contempt, hatred |
| `07 — Vitality / Existence` | Animating life of the inner person — constitution, continuation, fragility, and end |
| `08 — Transformation` | Inner change — renewal, healing, purification, formation, or degradation |
| `09 — Agency / Power` | Exercise of inner capacity — sovereignty, authority, strength, restraint, self-giving |
| `10 — Dependence / Creatureliness` | Inner posture of reliance — humility, dependence, trust, security |
| `11 — Divine-Human Correspondence` | Inner-being characteristics that operate across the boundary between God and the human person |

### DOMINANT_SUBJECT — Dimension Review — Dominant Subject

**Governing:** wa-dimensionreview-instruction [current] §7.7 Dimension 11 note; DR-12  
**Applies to:** `wa_dimension_index.dominant_subject`  
**Members:** 5

_Who is the primary agent in a verse-context group's analytical frame. GOD, HUMAN, OTHER_HUMAN, UNSEEN, or NONE when the subject is genuinely dual (e.g. divine-human correspondence)._

| Value | Description |
|---|---|
| `HUMAN` | Human being is the primary inner-being agent in the group |
| `GOD` | God is the primary inner-being agent in the group |
| `OTHER_HUMAN` | Another human is the object/target of the inner-being state |
| `UNSEEN` | Unseen realm or spiritual entity (angels, demons) — rare |
| `NONE` | Subject is genuinely dual (divine and human both explicit) — typically at Dimension 11 |

### MANUAL_OVERRIDE — Dimension Review — Manual Override Flag

**Governing:** wa-dimensionreview-instruction [current] + DR-8  
**Applies to:** `wa_dimension_index.manual_override`  
**Members:** 2

_Boolean flag: 1 = dimension locked by researcher review (DR-8 protected); 0 = open for reassignment. Post M29-family DimReview convention: dim_review_status=Complete anchors the assignment, MO=0 is expected._

| Value | Description |
|---|---|
| `0` | Dimension is open for reassignment — default post-review state (dim_review_status=Complete anchors) |
| `1` | Dimension locked by researcher review — DR-8 protected; updates require explicit MO in set clause |

### QA_FLAG — Dimension Review — Phase B QA Flag

**Governing:** wa-dimensionreview-instruction [current] §6.3 + §7.3  
**Applies to:** `(logged in observations, not a DB column)`  
**Members:** 6

_Per-group quality assessment outcome raised during Phase B. QA-CLEAR (no action), QA-TERMCENTRIC (description rewrite), QA-VAGUE (vague — needs sharpening), QA-BROAD (spans multiple dimensions, needs split), QA-EXTERNALISED (description names external-circumstance not inner-being), QA-REVIEW (flag for Phase C reassignment)._

| Value | Description |
|---|---|
| `QA-CLEAR` | No action — description, dimension, and subject are coherent |
| `QA-TERMCENTRIC` | Description phrased from lexical definition rather than inner-being action — rewrite needed |
| `QA-VAGUE` | Description too vague to identify the specific inner-being characteristic — sharpen |
| `QA-BROAD` | Description spans multiple inner-being dimensions — may need group split |
| `QA-EXTERNALISED` | Description names external circumstance rather than inner-being engagement |
| `QA-REVIEW` | Dimension or dominant_subject incorrect/uncertain — flag for Phase C reassignment |

---
*Generated 2026-04-20T16:45:01Z.*