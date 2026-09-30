# mti_terms Deduplication & OWNER/XREF Fix — Investigation Report

**Date:** 2026-03-30
**Trigger:** Claude AI stopped VCB-001 classification — 262 term entries but only 122 unique mti_term_id values. Investigation revealed two compounding data integrity issues.

---

## 1. Problem Summary

Two related issues prevent Verse Context from proceeding:

### Issue A: mti_terms has 3,616 duplicate rows

`mti_terms` should hold **one row per Strong's number** (programme-wide). Instead it holds 7,487 rows for 3,871 unique Strong's — 3,616 excess rows created when audit_word extracted the same term for multiple registries.

| Metric | Count |
|--------|-------|
| Total mti_terms rows | 7,487 |
| Unique Strong's numbers | 3,871 |
| Excess (duplicate) rows | 3,616 |
| Strong's with duplicates | 1,780 |

### Issue B: 1,006 Strong's numbers are OWNER in multiple registries

Each shared Strong's should have **one OWNER** and the rest **XREF**. Currently 1,006 Strong's are marked OWNER in every registry they appear in, creating 1,872 excess OWNER records.

| Metric | Count |
|--------|-------|
| Multi-registry Strong's (all OWNER) | 1,006 |
| Multi-registry Strong's (correctly 1 OWNER + XREF) | 614 |
| Single-registry Strong's (no issue) | 2,073 |
| Excess OWNER records to flip to XREF | 1,872 |

---

## 2. Root Cause

The Session A engine (`audit_word.py`) inserts a new `mti_terms` row each time a Strong's number is encountered during extraction for a registry. It does not check whether an mti_terms row already exists for that Strong's. When the same term appears across multiple registries (e.g. H2617B chesed appears in 8 registries), 8 separate mti_terms rows are created.

The OWNER/XREF classification was partially applied during the March 2028 housekeeping session, but only for terms that were clearly cross-references. The 1,006 genuinely shared terms were never resolved.

---

## 3. Data Pattern (guides the fix)

**Key finding:** For 1,648 of the 1,780 duplicated Strong's, exactly **one** mti_terms row has verse records linked via `wa_verse_records.mti_term_id`. The remaining rows are empty shells with 0 verses.

| Pattern | Count |
|--------|-------|
| 1 mti row has verses, rest have 0 | 1,648 |
| 0 mti rows have verses (all empty) | 132 |

**Status consistency:** 1,170 duplicated Strong's have **inconsistent** status across their mti rows (e.g. one is `extracted`, others are `NULL`). 610 have consistent status.

**owning_registry_fk:** Mostly NULL — only 1,658 of 7,487 mti rows have this set.

---

## 4. Proposed Fix — Three Phases

### Phase 1: mti_terms Deduplication

**Goal:** Consolidate to exactly one mti_terms row per Strong's number.

**Survivor selection rule** (deterministic, no judgement required):

1. If exactly one mti row has `wa_verse_records` linked → that is the survivor
2. If multiple rows have verses → the one with the most verses survives
3. If no rows have verses → the one with a non-NULL `status` survives (prefer `extracted` > `extracted_thin` > others > NULL)
4. If still tied → lowest `id` survives

**Operations per duplicated Strong's:**
1. Select survivor mti_terms.id
2. Repoint all `wa_verse_records.mti_term_id` from duplicate ids → survivor id
3. Repoint all `verse_context.mti_term_id` from duplicate ids → survivor id (currently empty but future-proofs)
4. Repoint all `verse_context_group.mti_term_id` from duplicate ids → survivor id (currently empty)
5. Transfer the best `status` to the survivor (if survivor has NULL but a duplicate has `extracted`, take `extracted`)
6. Transfer `owning_registry_fk` to the survivor if it's NULL on survivor but set on a duplicate
7. Delete the duplicate mti_terms rows

**Scale:** 3,616 rows to delete, 1,780 Strong's to process.

### Phase 2: OWNER/XREF Assignment

**Goal:** For each Strong's appearing in multiple registries, exactly one wa_term_inventory record is OWNER, the rest are XREF.

**Owner selection rule:**

1. If `mti_terms.owning_registry_fk` is set and matches a registry → that registry is OWNER
2. If not set: the registry with the **lowest `word_registry.no`** is OWNER (deterministic, stable, matches the extraction order)
3. All other wa_term_inventory records for that Strong's → set `term_owner_type = 'XREF'`

**XREF verse handling:** When a ti record flips from OWNER to XREF, its verse records must be delete_flagged (per XREF convention). The verse data is not lost — the OWNER registry's verses remain active.

**Scale:** 1,872 ti records to flip from OWNER to XREF. Associated verse records to delete_flag.

### Phase 3: Set owning_registry_fk

**Goal:** Every surviving mti_terms row has `owning_registry_fk` set to the OWNER registry's word_registry.id.

**Rule:** After Phase 2, query the single remaining OWNER ti record per Strong's → get its word_registry_fk → write to mti_terms.owning_registry_fk.

**Scale:** All 3,871 unique Strong's (many already set correctly, but verify/update all).

---

## 5. Validation Checks (post-fix)

```sql
-- V1: No duplicate mti_terms
SELECT strongs_number, COUNT(*) FROM mti_terms
GROUP BY strongs_number HAVING COUNT(*) > 1;
-- Expected: 0 rows

-- V2: Every multi-registry Strong's has exactly 1 OWNER
SELECT ti.strongs_number, SUM(CASE WHEN ti.term_owner_type = 'OWNER' THEN 1 ELSE 0 END) as owners
FROM wa_term_inventory ti WHERE ti.delete_flagged = 0
GROUP BY ti.strongs_number HAVING owners != 1;
-- Expected: 0 rows (single-registry terms will show 1 owner too)

-- V3: All XREF verse records are delete_flagged
SELECT COUNT(*) FROM wa_verse_records vr
JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
WHERE ti.term_owner_type = 'XREF' AND ti.delete_flagged = 0
  AND vr.delete_flagged = 0;
-- Expected: 0

-- V4: Every mti_terms has owning_registry_fk set
SELECT COUNT(*) FROM mti_terms WHERE owning_registry_fk IS NULL;
-- Expected: 0

-- V5: owning_registry_fk matches the OWNER ti record's registry
SELECT COUNT(*) FROM mti_terms mt
WHERE NOT EXISTS (
    SELECT 1 FROM wa_term_inventory ti
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE ti.strongs_number = mt.strongs_number
      AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
      AND fi.word_registry_fk = mt.owning_registry_fk
);
-- Expected: 0

-- V6: Programme counts
SELECT term_owner_type, COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 GROUP BY term_owner_type;
-- OWNER count should decrease, XREF count should increase
-- Total should remain the same (6,988)
```

---

## 6. Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Verse data loss | No verses deleted — XREF verses are delete_flagged, not removed. OWNER verses remain active. |
| mti_terms FK breakage | All FKs repointed before deletes. Verse_context tables are empty (no data at risk). |
| Status loss | Best status transferred to survivor before duplicate deletion |
| Irreversibility | Database backup before any writes. All operations logged. |
| Engine compatibility | audit_word must be checked — it should not re-create duplicates on next run |

---

## 7. Engine Fix Required

After the data fix, `audit_word.py` step A6 (term insertion) needs a guard: before inserting into mti_terms, check if a row already exists for the Strong's number. If yes, reuse the existing mti_terms.id rather than inserting a new row. Without this, the next audit_word run would recreate duplicates.

---

## 8. Impact on Verse Context

After this fix:
- Each Strong's has exactly one mti_terms.id
- Each Strong's has exactly one OWNER wa_term_inventory record
- The batch construction query will produce exactly one entry per term
- VCB-001 can be rebuilt cleanly

**Expected post-fix counts:**
- mti_terms: ~3,871 rows (down from 7,487)
- OWNER ti records: ~3,646 (down from 5,518)
- XREF ti records: ~3,342 (up from 1,470)
- Active verses: unchanged (OWNER verses stay active)

---

*Produced 2026-03-30 by Claude Code. Awaiting researcher approval before any data modifications.*
