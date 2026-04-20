# Directive DIR-20260420-001 — r183 Phase B verification extracts (3 groups)

> Produced by: wa-directive-instruction-v1_1-20260418
> Governed by: wa-global-general-rules-v2_11-20260418
> Registry: 183 (heart)
> Produced date: 2026-04-20
> Researcher approval: PENDING

---

## Motivation

Phase B r183 of the C01 Dimension Review surfaced three QA flags that the researcher has directed should be resolved by reading the actual verse evidence before Phase C dimension assignment proceeds. Without the verse text, Phase C dimension assignment for these three groups would be made on description alone — for three groups where the Phase B review has specifically identified that the description may or may not reflect the verse content accurately.

The three groups and the Phase B issues:

1. **580-001 `H3825 le.vav` (Aramaic heart, 6 verses)** — QA-BROAD. Description spans three inner-being dimensions (thought, will, moral orientation). Resolution requires reading the 6 Aramaic verses to determine whether one dominant characteristic is present or whether the three named characteristics are each represented.

2. **579-008 `H3824 le.vav` (affective register)** — QA-REVIEW. Description reads *"Term names the heart in its experiential states — the inner register of grief, gladness, sorrow, longing, and moral reflection."* The "moral reflection" element is cognitive-evaluative and may overlap descriptively with 579-002 (heart as seat of inner moral character). Resolution requires reading the verses in 579-008 to determine whether "moral reflection" appears in the verse evidence or is a description-level artefact.

3. **577-005 `H7130H qe.rev` (hostile intent)** — QA-REVIEW. Description reads *"Term names the inner parts as the seat of hostile intent — what lies within as the source of evil plotting against others."* Potential descriptive overlap with 577-002 (seat of moral character / source of conduct). Resolution requires reading the verses in 577-005 to confirm the hostile-plotting characteristic is the genuine sense-split rather than a re-framing of the general moral-character content.

The verification extracts will allow Phase C r183 to proceed on verified descriptions and — if revisions are needed — allow the description corrections to be encoded in the r183 patch alongside the Phase C dimension assignments, avoiding a later patch revision cycle.

This directive requests read-only verse extracts. No database writes are required. Any description revisions arising from the verification will be authored by Claude AI in the next session and encoded in the r183 patch.

---

## Scope

**Tables involved (read-only):**
- `verse_context_group` (for group identification — IDs already known)
- `verse_context` (link table between group and verse records)
- `wa_verse_records` (verse text source)

**Target verse_context_group IDs:**

| Group code | Strongs | Transliteration | verse_context_group.id |
|---|---|---|---:|
| 580-001 | H3825 | le.vav (Aramaic) | 2752 |
| 579-008 | H3824 | le.vav | 2749 |
| 577-005 | H7130H | qe.rev | 2763 |

**Registry filter:** `owning_registry_no = 183` (heart) — all three groups belong to r183.

**Verse selection criterion:** For each target group, return all verse records that meet these two conditions simultaneously:
- `verse_context.group_id = {target vcg.id}`
- `verse_context.delete_flagged = 0`
- `verse_context.is_relevant = 1` (exclude the NOT_RELEVANT records)

Then join to `wa_verse_records` via `verse_context.verse_record_id = wa_verse_records.id` (with `wa_verse_records.delete_flagged = 0`) to obtain the verse text.

**Expected verse counts:**
- 580-001 (H3825 Aramaic le.vav): approximately 6 verses (Daniel context)
- 579-008 (H3824 affective le.vav): unknown, probably 15-30 verses
- 577-005 (H7130H hostile qe.rev): unknown, probably 3-8 verses
- Exact counts to be determined by CC.

---

## Outcome required

A single markdown file (not a patch — this is a report) returned to Claude AI and the researcher, containing for each of the three target groups:

1. **Group header** with group_code, Strongs, transliteration, gloss, verse_context_group_id, current context_description, and total relevant anchor/classified verses found.

2. **Verse list** — one verse per row, in canonical Bible order (book_id ascending, chapter ascending, verse_num ascending). For each verse:
   - Reference (e.g., "Daniel 2:30")
   - Full ESV verse text from `wa_verse_records.verse_text`
   - `is_anchor` flag (1 or 0)

3. **A brief CC completion note** stating the number of verses returned per group.

**Filename suggestion:** `wa-183-heart-dirresult-001-phaseb-verify-v1-20260420.md` (or CC's preferred convention for directive results).

No database changes are produced by this directive. The file is the deliverable.

---

## Completion confirmation

CC returns the following three queries and their row counts before returning the extract file:

```sql
-- Query 1: verses for 580-001 (H3825 Aramaic le.vav)
SELECT COUNT(*) FROM verse_context vc
JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
WHERE vc.group_id = 2752
  AND vc.delete_flagged = 0
  AND vc.is_relevant = 1
  AND vr.delete_flagged = 0;
-- Expected: approximately 6

-- Query 2: verses for 579-008 (H3824 affective le.vav)
SELECT COUNT(*) FROM verse_context vc
JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
WHERE vc.group_id = 2749
  AND vc.delete_flagged = 0
  AND vc.is_relevant = 1
  AND vr.delete_flagged = 0;
-- Expected: count to be determined by CC

-- Query 3: verses for 577-005 (H7130H hostile qe.rev)
SELECT COUNT(*) FROM verse_context vc
JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
WHERE vc.group_id = 2763
  AND vc.delete_flagged = 0
  AND vc.is_relevant = 1
  AND vr.delete_flagged = 0;
-- Expected: count to be determined by CC
```

CC returns the counts, then returns the extract file. Claude AI reviews counts against expected (6 for query 1; TBD for queries 2 and 3).

---

## Notes

**Relation to programme state:**
- Phase C r112 is complete; r112 patch already produced and pending application: `wa-dim-c01-reg112-patch-v1-20260420.json`.
- Phase C r183 is paused pending this verification. No r183 patch has been produced yet.
- The r183 patch (when produced in the next session) may include description revisions for one or more of these three groups, encoded as `verse_context_group` updates alongside the Phase C dimension assignments. Pattern precedent: the r112 patch encoded a similar Phase B description revision for `1010-001 nefros`.

**No database writes:** This directive is read-only. Halt condition §6.4 applies only if the target group IDs are not found or returned verse counts are zero (which would indicate the groups are empty or delete-flagged — unexpected given the extract shows all three groups with `manual_override = 1`).

**Verse text field:** Per the schema (v3_11_0), `wa_verse_records.verse_text` holds the ESV text. If for any of the three groups the ESV text is empty or null, CC should note this per-verse in the extract rather than omit the verse.

**If the `is_relevant = 1` filter misrepresents the group corpus:** The Dimension Review instruction §4.2 describes group corpus as "all classified verses" for dimension purposes. If there is a policy mismatch between `is_relevant = 1` (classified-as-in-scope) and "all verses in the group" (which could include `is_related` or `set_aside_reason` records), CC should either clarify or return both filtered and unfiltered counts so Claude AI can assess. The three RD items are about the dominant characteristic in the active corpus, so the `is_relevant = 1` filter is the intended frame.

**Session continuity:** Next session will: (1) receive this extract; (2) read verses for each of the three groups; (3) determine whether description revisions are warranted and, if so, draft them; (4) run Phase C r183 on all 59 groups; (5) produce the r183 patch.

---

*Directive DIR-20260420-001 | Three verification extracts for Phase C r183 preparation | Produced 2026-04-20*
