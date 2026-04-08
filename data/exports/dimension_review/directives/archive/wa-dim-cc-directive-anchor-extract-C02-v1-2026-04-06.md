# WA — Claude Code Directive: Anchor Verse Extracts for C02 Phase C
**File:** wa-dim-cc-directive-anchor-extract-C02-v1-2026-04-06.md
**Date:** 2026-04-06
**Prepared by:** Claude AI — Dimension Review C02 Phase C
**For:** Claude Code
**Governing instruction:** WA-DimensionReview-Instruction-v1.2-2026-04-06 Section 4.5 and Section 9.2
**Preceding outputs:** wa-dim-refinement-log-C02-v1.6-2026-04-06.md

---

## Purpose

Phase C dimension discernment for C02 is complete for all QA-CLEAR groups. 28 groups received a QA-REVIEW flag during Phase B and require anchor verse text consultation before their dimensions can be assigned.

Claude Code must construct a group verification extract for each group listed below, per the format specified in Section 9.2 of the governing instruction.

---

## Required Output Format

Per Section 9.2, for each group produce a JSON extract containing:
- Group metadata (group_code, context_description, current dimension, dimension_confidence)
- Anchor verses (verse_record_id, book, chapter, verse, verse_text) — all active, non-delete-flagged anchors
- Related verses (same fields) — all active, non-delete-flagged related verses

Deliver as a single consolidated JSON file:
**`wa-dim-grpverify-C02-batch1-v1-2026-04-06.json`**

Structure:
```json
{
  "extract_meta": {
    "extract_type": "group_verification_batch",
    "cluster": "C02",
    "batch": "anchor-review-phase-c",
    "produced_date": "YYYY-MM-DD"
  },
  "groups": [
    {
      "group_code": "...",
      "verse_context_group_id": ...,
      "context_description": "...",
      "dimension": "...",
      "dimension_confidence": "...",
      "issue": "...",
      "anchor_verses": [...],
      "related_verses": [...]
    }
  ]
}
```

---

## Groups Requiring Anchor Verse Extraction

### Registry 32 (counsel)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 2110-001 | 401 | Dual inner-being engagements — plotter's will and victim's shaped inner life. Single anchor — confirm which verse and whether description accurately reflects it. |
| 748-001 | 416 | Bidirectional compression at 50 verses — "given or received" may cover distinguishable uses. Confirm anchor and dominant sense. |
| 749-001 | 405 | Bidirectional compression at 37 verses. Confirm anchor and dominant sense. |
| 751-001 | 410 | Relational-spiritual dimension — divine intimate friendship. Dimension: Theological/Divine-Human or Spiritual/God-ward? Confirm anchor. |
| 751-002 | 411 | Membership in divine council — covenantal access. Confirm anchor. |
| 751-004 | 413 | Trustworthiness in keeping confidence — Character/Disposition. Confirm anchor. |
| 753-003 | 421 | Names site (mouth) rather than inner act of vow. Confirm anchor — is the inner act of commitment named? |
| 753-004 | 422 | God's mouth as authoritative pronouncement — human inner-being engagement implicit. Confirm anchor — is human reception named? |

### Registry 85 (imagination)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 916-001 | 1292 | Possible conflation — fanciful inner content and false image of security. Confirm anchor and two related verses. |

### Registry 100 (knowledge)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 955-001 | 1504 | Generic description for 49 verses. Confirm anchor — what does the verse show that grounds the description? |
| 958-005 | 1513 | God's revelatory knowledge — human reception implicit. Confirm anchor — is human inner-being reception named? |
| 959-001 | 1502 | Divine attribute named; human inner-being engagement absent. Confirm anchor — is there a human inner-being dimension? |
| 961-002 | 1501 | "Measure of divine perfection" opaque. Confirm anchor to understand what this means. |
| 963-004 | 1498 | Covers divine and human knowing. Confirm anchor — which direction does the anchor verse address? |

### Registry 126 (purpose)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 3373-001 | 2097 | Dual use — governance foresight vs. provision for fleshly desire. Confirm both anchor verses. |

### Registry 160 (thought)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 1175-001 | 2294 | Broad — intending, planning, aspiration, design. Confirm anchor — what is the dominant characterisation? |
| 3445-001 | 2296 | Divine giving of thought — human inner-being engagement implicit. Confirm anchor. |
| 3459-001 | 2292 | Holds positive prudence and self-deceiving pride together. Confirm anchor — which pole does the anchor verse represent? |

### Registry 166 (understanding)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 1203-001 | 2346 | God hears — currently Spiritual/God-ward. Potential Theological/Divine-Human (being heard by God is constitutively relational). Confirm anchor — what inner-being engagement does the verse evidence? |
| 1203-004 | 2349 | Broad response range — fear, grief, anger, joy, worship, courage. Confirm anchor — what response does the anchor verse name? |
| 1204-001 | 2344 | Too compressed — "divinely given inner capacity." Confirm anchor — what capacity and in what context? |

### Registry 174 (wisdom)

| group_code | verse_context_group_id | Issue |
|---|---|---|
| 518-001 | 2483 | Inner devotional origin implied; names external act (song). Confirm anchor — is devotional inner origin named? |
| 519-002 | 2491 | Outer result (success) named rather than inner dimension. Confirm anchor — is inner dimension present? |
| 523-001 | 2471 | Divine attribute only — human inner-being absent from description. Confirm anchor — is there any human inner-being engagement? |
| 524-001 | 2484 | Same as 523-001. |
| 527-001 | 2495 | Same as 523-001. |
| 532-001 | 2488 | Divine attribute only — candidate QA-EXTERNALISED. Confirm anchor. |
| 532-002 | 2489 | Christological — wisdom as person of Christ. Confirm anchor — what inner-being engagement does the verse evidence? |
| 6670-001 | 2479 | Physical condition leads; inner recognition at endpoint. Confirm anchor — is inner recognition named? |
| 6672-001 | 2481 | Physical mark named; inner pride as cause. Confirm anchor — is inner pride named in anchor verse? |
| 6672-002 | 2482 | Physical feature named; inner desire as subordinate clause. Confirm anchor — is inner desire named? |

---

## Total Groups: 28

---

## Post-Extraction Next Steps

Once Claude Code returns the extract:
1. Claude AI reads all anchor and related verse texts
2. Claude AI completes Phase C dimension assessment for all 28 QA-REVIEW groups
3. Claude AI updates the refinement log
4. Claude AI produces the consolidated C02 dimension patch

---

## Notes for Claude Code

- Use `verse_context_group_id` values as the primary lookup key — these are the IDs from the `verse_context_group` table
- Include only active (non-delete-flagged) verse_context records
- Include full `verse_text` from `wa_verse_records`
- For groups with many related verses (e.g. 748-001 with 49 related), include all related verses in the extract — Claude AI needs the full picture for the bidirectional compression assessment
- The `issue` field in each group output is for Claude AI's reference — it summarises what the anchor verse consultation needs to resolve

---

*wa-dim-cc-directive-anchor-extract-C02-v1-2026-04-06.md | 2026-04-06 | Claude Code directive — 28 anchor verse extracts for C02 Phase C QA-REVIEW groups | Governing: WA-DimensionReview-Instruction-v1.2 | Preceding: wa-dim-refinement-log-C02-v1.6-2026-04-06.md*
