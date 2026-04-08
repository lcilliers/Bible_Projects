# wa-dim-cc-directive-grpverify-3012-001-2026-04-06
**Framework B — Soul Word Analysis Programme**
**Directive to Claude Code — Group Description Verification Extract**
**Date:** 2026-04-06 | **Raised by:** CA — Dimension Review Phase B | **Priority:** Required before Phase C can proceed for Registry 183 (heart)

---

## Purpose

During Phase B (group quality review) of the Dimension Review for Cluster C01, CA flagged group `3012-001` (H7608 sha.a.rah, Registry 183 heart) as **QA-VAGUE**. The current `context_description` is a phrase fragment:

> *"Sha.a.rah as kinship bond creating moral prohibition"*

This does not meet the quality standard required for Phase C dimension assignment — it does not form a complete sentence and does not explicitly name what the inner being is doing through this term. Before CA can propose a corrected description, the anchor and related verse texts for this group must be reviewed.

This extract follows the specification in **WA-DimensionReview-Instruction-v1.1-2026-04-06 Section 9.2**.

---

## Action Required

Construct and return the group description verification extract for group `3012-001`.

**Output filename:** `wa-dim-grpverify-3012-001-2026-04-06.json`

**Return to:** CA for verse reading, description proposal, and researcher confirmation. CA will then produce a group description correction patch if the proposal is confirmed.

---

## Extract Specification

```json
{
  "extract_meta": {
    "extract_type": "group_description_verification",
    "group_code": "3012-001",
    "produced_date": "YYYY-MM-DD"
  },
  "group": {
    "id": "<verse_context_group.id WHERE group_code = '3012-001'>",
    "group_code": "3012-001",
    "mti_term_id": "<verse_context_group.mti_term_id>",
    "strongs_number": "<mti_terms.strongs_number>",
    "transliteration": "<mti_terms.transliteration>",
    "owning_registry_no": 183,
    "owning_registry_word": "heart",
    "current_description": "<verse_context_group.context_description>",
    "notes": "<verse_context_group.notes>"
  },
  "anchor_verses": [
    {
      "verse_record_id": "<verse_context.verse_record_id WHERE is_anchor = 1>",
      "book": "<books.name>",
      "chapter": "<wa_verse_records.chapter>",
      "verse": "<wa_verse_records.verse>",
      "verse_text": "<wa_verse_records.verse_text>",
      "is_anchor": 1,
      "is_related": 0
    }
  ],
  "related_verses": [
    {
      "verse_record_id": "<verse_context.verse_record_id WHERE is_related = 1>",
      "book": "<books.name>",
      "chapter": "<wa_verse_records.chapter>",
      "verse": "<wa_verse_records.verse>",
      "verse_text": "<wa_verse_records.verse_text>",
      "is_anchor": 0,
      "is_related": 1
    }
  ]
}
```

---

## Join Path

| Step | Table | Condition |
|---|---|---|
| 1 | `verse_context_group` | `WHERE group_code = '3012-001'` |
| 2 | `verse_context` | `WHERE group_id = verse_context_group.id AND delete_flagged = 0 AND is_relevant = 1` |
| 3 | `wa_verse_records` | `WHERE id = verse_context.verse_record_id` |
| 4 | `books` | `WHERE id = wa_verse_records.book_id` |
| 5 | `mti_terms` | `WHERE id = verse_context_group.mti_term_id` |

**Filter:** `verse_context.delete_flagged = 0` AND `verse_context.is_relevant = 1` only. Set-aside verses are not required.

**Order:** Anchor verses first (`is_anchor = 1`), then related verses (`is_related = 1`).

---

## Context for CC

- This is a single-group extract — one `verse_context_group` row, with all its relevant `verse_context` records and their verse texts
- The extract does not require any dimension index data — source tables are `verse_context_group`, `verse_context`, `wa_verse_records`, `books`, and `mti_terms` only
- CC does not make any analytical decisions about the description — return the verse data as specified and pass to CA

---

*Governing instruction: WA-DimensionReview-Instruction-v1.1-2026-04-06 §9.2*
*Raised during: C01 Phase B quality review — Registry 183 (heart)*
*Next step after return: CA reads verse texts → proposes corrected description → researcher confirms → CA produces DIMREVIEW-GRPDESC patch*
