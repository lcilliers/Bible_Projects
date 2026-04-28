# CC Directive — Anchor Verse Correction: Group 6134-001
**Date:** 2026-04-09
**Governing instruction:** WA-DimensionReview-Instruction-v1.8-2026-04-09

## Issue
Group 6134-001 (H4253 ma.cha.la.phah, Reg 134 renewal) has an incorrect anchor verse.

The group description names the departure of inner strength when the Nazirite locks are cut. The anchor verse is currently Judg 16:13 — the misdirection exchange before the cutting. The actual cutting and departure of strength is in Judg 16:19.

## Required action
Identify the `verse_context` record for Judg 16:13 linked to group 6134-001 and update it to Judg 16:19, OR if both records exist, set Judg 16:19 as `is_anchor = 1` and Judg 16:13 as `is_anchor = 0`.

```sql
-- Step 1: Find verse_context records for group 6134-001
SELECT vc.id, vc.verse_record_id, vc.is_anchor, vr.book_name, vr.chapter, vr.verse
FROM verse_context vc
JOIN verse_record vr ON vc.verse_record_id = vr.id
WHERE vc.group_id = (SELECT id FROM verse_context_group WHERE group_code = '6134-001')
ORDER BY vr.book_name, vr.chapter, vr.verse;

-- Step 2: Confirm Judg 16:19 is present in the verse_record table
SELECT id, book_name, chapter, verse FROM verse_record
WHERE book_name LIKE '%Judg%' AND chapter = 16 AND verse = 19;
```

Return results before making any changes. Claude AI will confirm the correction to apply based on what is found.
