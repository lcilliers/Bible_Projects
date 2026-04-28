# WA — Claude Code Directive: Re-extraction and Investigation Queries — C02 Phase C
**File:** wa-dim-cc-directive-reextract-C02-v1-2026-04-07.md
**Date:** 2026-04-07
**Prepared by:** Claude AI — Dimension Review C02 Phase C
**For:** Claude Code
**Governing instruction:** WA-DimensionReview-Instruction-v1.2-2026-04-06 Section 9.2
**Preceding outputs:** wa-dim-grpverify-C02-batch1-v1-2026-04-07.json (extract with errors) | wa-dim-refinement-log-C02-v1.7-2026-04-07.md

---

## Purpose

Two tasks required:

1. **Task A — Re-extraction of 3 groups with incorrect data** in the batch1 extract
2. **Task B — Investigation query for group 527-001** (tu.shiy.yah — researcher decision pending)

---

## Task A — Re-extraction of 3 Groups

The batch1 extract (`wa-dim-grpverify-C02-batch1-v1-2026-04-07.json`) returned incorrect data for three groups. The `verse_context_group_id` values sent were correct, but the content returned does not match those IDs. The descriptions and anchor verses returned belong to other groups. The error appears to be a join on the wrong key.

**Groups requiring re-extraction:**

| group_code | verse_context_group_id | Expected content | What was returned |
|---|---|---|---|
| 524-001 | 2484 | te.vu.nah (H8394) — understanding as divine attribute (infinite discernment by which God creates) | Prudence description with Pro 14:8 anchor — belongs to a different group |
| 532-001 | 2488 | sofia (G4678) — wisdom as divine attribute (infinite understanding belonging to God) | or.mah prudence description with Pro 8:12 anchor — belongs to different group |
| 532-002 | 2489 | sofia (G4678) — wisdom as person of Christ (incarnate divine wisdom) | Craftiness description with Exo 21:14 anchor — belongs to different group |

**Required query logic:**

For each group, retrieve from `verse_context_group` and `verse_context`:

```sql
-- For each vcg_id (2484, 2488, 2489):
SELECT
    vcg.id AS verse_context_group_id,
    vcg.group_code,
    vcg.context_description,
    wdi.dimension,
    wdi.dimension_confidence,
    wdi.id AS dimension_index_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    wr_book.name AS book,
    wa_vr.chapter,
    wa_vr.verse,
    wa_vr.verse_text,
    vc.is_anchor,
    vc.is_related,
    vc.verse_record_id
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
    AND vc.delete_flagged = 0
JOIN wa_verse_records wa_vr ON wa_vr.id = vc.verse_record_id
JOIN books wr_book ON wr_book.id = wa_vr.book_id
JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
JOIN mti_terms mt ON mt.id = wdi.mti_term_id
WHERE vcg.id IN (2484, 2488, 2489)
ORDER BY vcg.id, vc.is_anchor DESC, wr_book.book_order, wa_vr.chapter, wa_vr.verse;
```

**Verification step before returning:** Confirm that the `context_description` returned for vcg 2484 contains the word "understanding" or "discernment" and references te.vu.nah or H8394. If it still returns prudence content, there is a deeper data issue to investigate.

**Output format:** Append the three groups to a new file:
**`wa-dim-grpverify-C02-reextract-v1-2026-04-07.json`**

Use the same structure as the batch1 extract:
```json
{
  "extract_meta": {
    "extract_type": "group_verification_reextract",
    "cluster": "C02",
    "batch": "reextract-phase-c-corrections",
    "produced_date": "YYYY-MM-DD",
    "note": "Re-extraction of 3 groups with data errors in batch1"
  },
  "groups": [
    {
      "group_code": "524-001",
      "verse_context_group_id": 2484,
      "context_description": "...",
      "dimension": "...",
      "dimension_confidence": "...",
      "issue": "te.vu.nah — divine attribute — data error in batch1",
      "anchor_verses": [...],
      "related_verses": [...]
    },
    ... (532-001 and 532-002)
  ]
}
```

---

## Task B — Investigation Query for Group 527-001

**Context:** Group 527-001 (H8454 tu.shiy.yah, wisdom registry 174) has 3 verses all of which appear to name tu.shiy.yah as a divine attribute with no direct human inner-being engagement. Claude AI requires confirmation of how these verses entered this group before a dimension recommendation can be made.

**Specific question:** For each of the 3 verses in group 527-001, was the `verse_context` record created with H8454 tu.shiy.yah as the OWNER term, or was a different term the OWNER and tu.shiy.yah an XREF participant?

**Query:**

```sql
-- Step 1: Confirm the group and its verses
SELECT
    vcg.id AS vcg_id,
    vcg.group_code,
    vcg.context_description,
    vc.verse_record_id,
    vc.is_anchor,
    vc.is_related,
    mt_owner.id AS owner_mti_id,
    mt_owner.strongs_number AS owner_strongs,
    mt_owner.transliteration AS owner_transliteration,
    wr.name AS book,
    wa_vr.chapter,
    wa_vr.verse,
    wa_vr.verse_text
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id AND vc.delete_flagged = 0
JOIN wa_verse_records wa_vr ON wa_vr.id = vc.verse_record_id
JOIN books wr ON wr.id = wa_vr.book_id
JOIN mti_terms mt_owner ON mt_owner.id = vc.mti_term_id
WHERE vcg.id = 2495  -- verse_context_group_id for 527-001
ORDER BY vc.is_anchor DESC, wr.book_order, wa_vr.chapter, wa_vr.verse;
```

**What to look for in the result:**
- `vc.mti_term_id` should match H8454 tu.shiy.yah if this group was classified under that OWNER term
- If `vc.mti_term_id` is a different term (e.g. a different wisdom term), the verses may have entered this group via a different OWNER classification and tu.shiy.yah may be present in those verses as context, not as the classified term

**Step 2: Cross-check — does H8454 appear in any of those verses under a different verse_context record?**

```sql
-- For each verse_record_id returned above, check all active vc records
SELECT
    vc.verse_record_id,
    mt.strongs_number,
    mt.transliteration,
    mt.gloss,
    vcg2.group_code,
    vcg2.context_description,
    vc.is_anchor,
    vc.delete_flagged
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
LEFT JOIN verse_context_group vcg2 ON vcg2.id = vc.group_id
WHERE vc.verse_record_id IN (
    -- paste the verse_record_ids from Step 1 result here
    SELECT vc2.verse_record_id
    FROM verse_context vc2
    JOIN verse_context_group vcg3 ON vcg3.id = vc2.group_id
    WHERE vcg3.id = 2495
    AND vc2.delete_flagged = 0
)
AND vc.delete_flagged = 0
ORDER BY vc.verse_record_id, mt.strongs_number;
```

**Output format:** Return as a structured `.md` file (not JSON — this is an investigative query result for CA reading):

**`wa-dim-inv-527001-tu.shiy.yah-v1-2026-04-07.md`**

Include:
1. The result of Step 1 (all 3 verses with their owner mti_term_id and verse text)
2. The result of Step 2 (all vc records for those 3 verses, across all terms)
3. A brief note from Claude Code confirming whether H8454 was the OWNER term for the verse_context records in group 527-001

---

## Summary of Outputs Required

| File | Task | Format |
|---|---|---|
| `wa-dim-grpverify-C02-reextract-v1-2026-04-07.json` | Task A — re-extract 3 groups | JSON per Section 9.2 format |
| `wa-dim-inv-527001-tu.shiy.yah-v1-2026-04-07.md` | Task B — investigation query | Markdown with query results |

---

## After Claude Code Returns

Once both files are available:
- Claude AI will complete Phase C dimension assessment for 524-001, 532-001, and 532-002 from the corrected extract
- Claude AI will review the 527-001 investigation and make a recommendation to the researcher (delete-flag, Theological/Divine-Human, or verse-level re-run)
- The consolidated C02 dimension patch will then be built

---

*wa-dim-cc-directive-reextract-C02-v1-2026-04-07.md | 2026-04-07 | Re-extraction of 3 groups with data errors + investigation query for 527-001 | Governing: WA-DimensionReview-Instruction-v1.2 | Preceding: wa-dim-grpverify-C02-batch1-v1-2026-04-07.json*
