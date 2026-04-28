# WA — Level 1 Audit: Verse Context Integrity
## Claude Code Directive

**File:** wa-dim-cc-directive-level1-audit-v2-2026-04-06.md
**Supersedes:** wa-dim-cc-directive-level1-audit-v1-2026-04-06.md
**Date:** 2026-04-06
**Produced by:** Claude AI — WA-DimensionReview-Instruction-v1.2-2026-04-06
**Preceding output:** wa-dim-session-log-audit-v3-2026-04-06.md (Level 0 closure)
**Status:** Instruction to Claude Code — execute in sequence, report results to Claude AI

**Change control:**

| Version | Change |
|---|---|
| v1 | Initial directive — Tier A (L1-A1 through L1-A5), Tier B (L1-B1 through L1-B3), L1-INV1 |
| v2 | Three query corrections following first execution: (1) L1-A1 — removed `wa_term_inventory` join that produced 62,235 false positives from XREF path; query now joins `mti_terms` directly. (2) L1-A4 — added `AND vc.is_relevant = 1` to exclude set-aside verses whose `group_id = NULL` is correct by design. (3) L1-B2 — added `relevant_records > 0` filter to exclude AVF terms whose `group_count = 0` is correct by design. (4) L1-B3 — removed JOIN on `verse_context_group` that excluded set-aside rows; group count now via subquery. (5) L1-INV2 and L1-INV3 added — investigation queries for the two genuine empty groups (vcg 789 H7379 riv/distress; vcg 2130 H5493H sur/rebellion). |

---

## Purpose

Level 0 established that the right terms are attributed to the right registries. Level 1 establishes whether the verse_context records produced during the Verse Context stage are structurally sound and analytically trustworthy.

Three tiers of questions are addressed. Tiers A and B are query-verifiable. Tier C requires verse text review and will be scoped by Claude AI after Tier A and B results are returned.

**Execution rule:** Run each query in sequence. After each query, record the row count. If a query returns rows where zero is expected, return the full result set to Claude AI before proceeding to the next query. Do not proceed past a non-zero result without Claude AI confirmation.

---

## Tier A — Structural Integrity

### Query L1-A1 — Contamination check

Identifies `verse_context` records attached to terms that should not have them: XREF terms, delete-flagged terms, or terms with non-extracted `mti_terms.status`.

```sql
SELECT vc.id, vc.mti_term_id, mt.strongs_number, mt.status AS mti_status,
       mt.delete_flagged AS mti_deleted,
       wr.no AS registry_no, wr.word AS registry_word
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE vc.delete_flagged = 0
AND (
    mt.status NOT IN ('extracted', 'extracted_thin',
                      'extracted_theological_anchor', 'phase2_enrichment')
    OR mt.delete_flagged = 1
)
LIMIT 50;
```

**Design note:** `verse_context` links to `mti_terms` via `mti_term_id`. This is an MTI-level join — do not join through `wa_term_inventory` to check OWNER/XREF status here, as that path finds XREF rows for the same term and produces false positives. The contamination check operates at the `mti_terms` level only: wrong status or delete_flagged on the MTI record itself.

**Expected result:** 0 rows.
**If rows returned:** Return full result set to Claude AI. Do not proceed.

---

### Query L1-A2 — Anchor integrity: groups with zero anchors

Every active group must have at least one anchor verse. Groups with zero anchors are structurally incomplete.

```sql
SELECT vcg.id, vcg.group_code, vcg.context_description,
       COUNT(vc.id) AS total_vc_records,
       SUM(CASE WHEN vc.is_anchor = 1 THEN 1 ELSE 0 END) AS anchor_count
FROM verse_context_group vcg
LEFT JOIN verse_context vc ON vc.group_id = vcg.id AND vc.delete_flagged = 0
WHERE vcg.delete_flagged = 0
GROUP BY vcg.id
HAVING anchor_count = 0;
```

**Expected result:** 0 rows.
**If rows returned:** Return full result set to Claude AI. Do not proceed.

---

### Query L1-A3 — Anchor integrity: flag consistency

No verse_context record should be flagged as both anchor and set-aside simultaneously. A verse is set aside when `is_relevant = 0`; an anchor must have `is_relevant = 1`.

```sql
SELECT vc.id, vc.mti_term_id, vc.group_id, vc.verse_record_id,
       vc.is_anchor, vc.is_relevant, vc.is_related,
       vcg.group_code
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.delete_flagged = 0
AND vc.is_anchor = 1
AND vc.is_relevant = 0;
```

**Expected result:** 0 rows.
**If rows returned:** Return full result set to Claude AI. Do not proceed.

---

### Query L1-A4 — Orphaned verse_context records

`verse_context` records must link to a valid active `verse_context_group`. Records with a null or invalid `group_id` are orphaned.

```sql
SELECT vc.id, vc.mti_term_id, vc.group_id, vc.verse_record_id,
       vc.is_relevant
FROM verse_context vc
WHERE vc.delete_flagged = 0
AND vc.is_relevant = 1
AND (
    vc.group_id IS NULL
    OR NOT EXISTS (
        SELECT 1 FROM verse_context_group vcg
        WHERE vcg.id = vc.group_id AND vcg.delete_flagged = 0
    )
);
```

**Design note:** Set-aside verses (`is_relevant = 0`) have `group_id = NULL` by design — they do not belong to any group per the VCB instruction R1 rule. This query restricts to `is_relevant = 1` records only, which must always have a valid group.

**Expected result:** 0 rows.
**If rows returned:** Return full result set to Claude AI. Do not proceed.

---

### Query L1-A5 — Groups with no verse_context records

Every active group must have at least one verse_context record. A group with no records is an empty shell.

```sql
SELECT vcg.id, vcg.group_code, vcg.context_description,
       mt.strongs_number, mt.transliteration,
       wr.no AS registry_no, wr.word AS registry_word
FROM verse_context_group vcg
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE vcg.delete_flagged = 0
AND NOT EXISTS (
    SELECT 1 FROM verse_context vc
    WHERE vc.group_id = vcg.id AND vc.delete_flagged = 0
);
```

**Expected result:** 0 rows.
**If rows returned:** Return full result set to Claude AI. Do not proceed.

---

## Tier A — Genuine Findings Investigation

### Query L1-INV1 — Empty group detail (vcg 789 and vcg 2130)

Two groups confirmed to have zero verse_context records. Return full detail for both.

```sql
SELECT vcg.id, vcg.group_code, vcg.context_description,
       vcg.notes, vcg.delete_flagged,
       mt.strongs_number, mt.transliteration, mt.status AS mti_status,
       mt.delete_flagged AS mti_deleted,
       wr.no AS registry_no, wr.word AS registry_word,
       wr.verse_context_status,
       -- Check whether any delete_flagged vc records exist for this group
       (SELECT COUNT(*) FROM verse_context vc2
        WHERE vc2.group_id = vcg.id) AS total_vc_including_deleted,
       (SELECT COUNT(*) FROM verse_context vc2
        WHERE vc2.group_id = vcg.id AND vc2.delete_flagged = 0) AS active_vc_count,
       (SELECT COUNT(*) FROM verse_context vc2
        WHERE vc2.group_id = vcg.id AND vc2.delete_flagged = 1) AS deleted_vc_count
FROM verse_context_group vcg
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE vcg.id IN (789, 2130);
```

**Return full result to Claude AI before proceeding.**

---

## Tier B — Coverage Integrity

### Query L1-B1 — Terms with verses but no verse_context records

For every registry marked `verse_context_status = Complete`, all active OWNER extracted terms that have active verses must have at least one verse_context record. Terms that have verses but no classification represent missed VCB coverage.

```sql
SELECT wr.no AS registry_no, wr.word AS registry_word,
       mt.strongs_number, mt.transliteration, mt.status AS mti_status,
       COUNT(DISTINCT vr.id) AS active_verse_count
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
    AND wr.verse_context_status = 'Complete'
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE mt.status IN ('extracted', 'extracted_thin')
    AND mt.delete_flagged = 0
    AND NOT EXISTS (
        SELECT 1 FROM verse_context vc
        WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
    )
GROUP BY wr.no, wr.word, mt.strongs_number, mt.transliteration, mt.status
ORDER BY wr.no, active_verse_count DESC;
```

**Expected result:** 0 rows (or only Reg 15 boastfulness if VCB-030 has not yet propagated — confirm).
**If rows returned beyond Reg 15:** Return grouped count by registry to Claude AI before proceeding.

---

### Query L1-B2 — Terms classified but not grouped

A verse_context record must always belong to a group (`group_id` not null, linked to an active group). A term with verse_context records but no corresponding group record would indicate a classification that was not grouped — an intermediate state that should not exist in a Complete registry.

```sql
SELECT mt.strongs_number, mt.transliteration,
       wr.no AS registry_no, wr.word AS registry_word,
       COUNT(vc.id) AS vc_records,
       SUM(CASE WHEN vc.is_relevant = 1 THEN 1 ELSE 0 END) AS relevant_records,
       COUNT(DISTINCT vc.group_id) AS group_count
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE vc.delete_flagged = 0
    AND mt.status IN ('extracted', 'extracted_thin')
    AND mt.delete_flagged = 0
GROUP BY mt.strongs_number, mt.transliteration, wr.no, wr.word
HAVING relevant_records > 0 AND group_count = 0;
```

**Design note:** AVF terms have all verses set aside (`is_relevant = 0`), so `group_count = 0` is correct for them. This query restricts to terms that have at least one relevant verse (`relevant_records > 0`) — these must always have a group. AVF terms (`relevant_records = 0`) are correctly excluded.

**Expected result:** 0 rows.
**If rows returned:** Return full result set to Claude AI. Do not proceed.

---

### Query L1-B3 — Summary coverage statistics

Provides a programme-wide picture of verse accounting at the verse_context level for Claude AI to assess overall coverage quality.

```sql
SELECT
    COUNT(DISTINCT CASE WHEN vc.is_relevant = 1 AND vc.delete_flagged = 0 THEN vc.id END) AS total_relevant,
    COUNT(DISTINCT CASE WHEN vc.is_anchor = 1 AND vc.delete_flagged = 0 THEN vc.id END) AS total_anchors,
    COUNT(DISTINCT CASE WHEN vc.is_relevant = 0 AND vc.delete_flagged = 0 THEN vc.id END) AS total_set_aside,
    COUNT(DISTINCT CASE WHEN vc.delete_flagged = 0 THEN vc.id END) AS total_active_vc_records,
    (SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged = 0) AS total_active_groups,
    COUNT(DISTINCT CASE WHEN mt.status = 'extracted' AND mt.delete_flagged = 0 THEN mt.id END) AS extracted_terms_with_vc,
    COUNT(DISTINCT CASE WHEN mt.status = 'extracted_thin' AND mt.delete_flagged = 0 THEN mt.id END) AS extracted_thin_terms_with_vc
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id;
```

**Design note:** Set-aside verses have `group_id = NULL` and must not be excluded by a JOIN on `verse_context_group`. This query joins only on `mti_terms` and computes group count via a subquery. `total_relevant + total_set_aside` should equal `total_active_vc_records`.

**Expected result:** Single summary row. Return to Claude AI for assessment regardless of values.

---

## Reporting Format

Return results in this format:

```
L1-A1: [row count] rows — [CLEAR / ISSUE: brief description]
L1-A2: [row count] rows — [CLEAR / ISSUE: brief description]
L1-A3: [row count] rows — [CLEAR / ISSUE: brief description]
L1-A4: [row count] rows — [CLEAR / ISSUE: brief description]
L1-A5: [row count] rows — [CLEAR / ISSUE: brief description]
L1-B1: [row count] rows — [CLEAR / ISSUE: brief description]
L1-B2: [row count] rows — [CLEAR / ISSUE: brief description]
L1-B3: [summary row values}
```

If any query is blocked by a prior non-zero result, state: `[query id]: BLOCKED — awaiting Claude AI confirmation on [prior query id]`

---

## After Tier A and B

Claude AI will assess results and determine:
- Whether any structural issues require remediation before Tier C
- The sampling strategy for Tier C (anchor verse quality review)
- Whether any registries require targeted investigation based on Tier B coverage gaps

Do not begin Tier C work independently. Return Tier A and B results to Claude AI first.

---

*wa-dim-cc-directive-level1-audit-v1-2026-04-06.md | 2026-04-06 | Preceding: wa-dim-session-log-audit-v3-2026-04-06.md | Claude Code execute in sequence — report results to Claude AI before proceeding past any non-zero Tier A result*

---

## Tier A — Empty Group Resolution

### Query L1-INV2 — H7379 (riv) other groups in distress (#51)

Before delete-flagging vcg 789, confirm whether H7379 has other active groups in registry 51 and whether it has any active verse_context records at all.

```sql
-- All active groups for H7379 in any registry
SELECT vcg.id, vcg.group_code, vcg.context_description,
       wr.no AS registry_no, wr.word AS registry_word,
       COUNT(vc.id) AS active_vc_count,
       SUM(CASE WHEN vc.is_anchor = 1 THEN 1 ELSE 0 END) AS anchor_count
FROM verse_context_group vcg
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
    AND mt.strongs_number = 'H7379'
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
LEFT JOIN verse_context vc ON vc.group_id = vcg.id AND vc.delete_flagged = 0
WHERE vcg.delete_flagged = 0
GROUP BY vcg.id, vcg.group_code, vcg.context_description, wr.no, wr.word;
```

Return full result to Claude AI.

---

### Query L1-INV3 — H5493H (sur) other groups in rebellion (#128)

Before delete-flagging vcg 2130, confirm whether H5493H has other active groups in registry 128 and whether the 4 deleted verse_context records' verses are accounted for elsewhere.

```sql
-- All active groups for H5493H in any registry
SELECT vcg.id, vcg.group_code, vcg.context_description,
       wr.no AS registry_no, wr.word AS registry_word,
       COUNT(vc.id) AS active_vc_count,
       SUM(CASE WHEN vc.is_anchor = 1 THEN 1 ELSE 0 END) AS anchor_count
FROM verse_context_group vcg
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
    AND mt.strongs_number = 'H5493H'
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
LEFT JOIN verse_context vc ON vc.group_id = vcg.id AND vc.delete_flagged = 0
WHERE vcg.delete_flagged = 0
GROUP BY vcg.id, vcg.group_code, vcg.context_description, wr.no, wr.word;

-- Also: what were the 4 deleted vc records' verse_record_ids?
SELECT vc.id, vc.verse_record_id, vc.is_anchor, vc.is_relevant,
       vr.book_id, vr.chapter, vr.verse
FROM verse_context vc
JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
WHERE vc.group_id = 2130 AND vc.delete_flagged = 1;
```

Return full result to Claude AI.

---

*wa-dim-cc-directive-level1-audit-v2-2026-04-06.md | 2026-04-06 | Supersedes v1 | v2: four query corrections (L1-A1 XREF false positive; L1-A4 set-aside exclusion; L1-B2 AVF exclusion; L1-B3 set-aside JOIN fix); L1-INV2 and L1-INV3 added for empty group investigation*
