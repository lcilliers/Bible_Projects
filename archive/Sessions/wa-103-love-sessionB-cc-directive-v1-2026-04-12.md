# CC Directive — Registry 103 (love) — Stage 1 Remediation
## WA Framework B Soul Word Analysis Programme
**File:** wa-103-love-sessionB-cc-directive-v1-2026-04-12.md
**Date:** 2026-04-12
**Companion patch:** PATCH-20260412-103-PREANALYSIS-V1.json
**Governing instruction:** WA-SessionB-Instruction-v4.7 — Stage 1 Step A (manual operations)
**Previous outputs:** wa-103-love-sessionC-log-v1-2026-04-12.md, wa-103-love-sessionB-log-v1-2026-04-12.md

---

## Purpose

This directive covers four categories of manual operations required for Registry 103 (love) Stage 1 remediation that cannot be handled by the patch applicator:

1. G7493 — add to strongs_list as delete entry
2. H2898 — inventory reinstatement (restore_delete_flagged + owner_type update)
3. Root family gap corrections — 7 terms requiring wa_term_root_family inserts
4. H2898 — Verse Context sub-process instructions

Apply PATCH-20260412-103-PREANALYSIS-V1.json first. Then apply all operations in this directive in the order given.

---

## DIR-001 — Add G7493 to strongs_list

**Context:** G7493 (eraō, "to love passionately") has extracted status in mti_terms but 0 verses and is absent from the registry strongs_list. PATCH-20260412-103-PREANALYSIS-V1 sets its status to delete. The strongs_list must be updated to include it as a delete entry so the record is consistent.

**Action:** Append G7493 to the `word_registry.strongs_list` JSON array for registry 103 with count = 0.

**SQL:**
```sql
UPDATE word_registry
SET strongs_list = json_insert(
    strongs_list,
    '$[#]',
    json_object('strong', 'G7493', 'count', 0)
)
WHERE no = 103;
```

**Verify:** `SELECT strongs_list FROM word_registry WHERE no = 103` — confirm G7493 appears in the array with count 0.

---

## DIR-002 — H2898 Inventory Reinstatement

**Context:** H2898 (tuv, goodness) has been reinstated to extracted status by PATCH-20260412-103-PREANALYSIS-V1. The inventory record must also be updated: `delete_flagged` must be set to 0, and `owner_type` must be set to OWNER.

**Action A — Restore inventory delete_flag:**
```sql
UPDATE wa_term_inventory
SET delete_flagged = 0
WHERE term_id = (
    SELECT id FROM mti_terms WHERE strongs_number = 'H2898'
);
```

**Action B — Set owner_type in mti_terms:**
```sql
UPDATE mti_terms
SET owning_registry_fk = 103
WHERE strongs_number = 'H2898'
  AND (owning_registry_fk IS NULL OR owning_registry_fk = 0);
```

**Action C — Update word_registry strongs_list count for H2898:**
H2898 is already in strongs_list with count = 31. No change needed to strongs_list count — the count reflects verse records, which remain as-is. Verse Context classification (not deletion) will handle the 17 set-aside verses.

**Verify:**
```sql
SELECT ti.delete_flagged, mt.status, mt.owning_registry_fk
FROM wa_term_inventory ti
JOIN mti_terms mt ON ti.term_id = mt.id
WHERE mt.strongs_number = 'H2898';
```
Expected: delete_flagged = 0, status = extracted, owning_registry_fk = 103.

---

## DIR-003 — Root Family Gap Corrections

**Context:** Seven active owner/xref terms are missing root family records. These gaps were identified in audit check 10a. All root_gloss values are null (consistent with multi-registry roots per v4.4 rule — do not force a gloss).

### DIR-003a — FILOS root family (5 terms missing)

Terms: G5370 (mti.id=1580), G5373 (mti.id=1588), G5384 (mti.id=1579), G2705 (mti.id=1581), G5382 (mti.id=1582)

```sql
INSERT INTO wa_term_root_family (mti_term_id, root_code, root_gloss, registry_id)
VALUES
  (1580, 'FILOS', NULL, 103),
  (1588, 'FILOS', NULL, 103),
  (1579, 'FILOS', NULL, 103),
  (1581, 'FILOS', NULL, 103),
  (1582, 'FILOS', NULL, 103);
```

### DIR-003b — AHAV root family (1 term missing)

Term: H0157H (mti.id=1600)

```sql
INSERT INTO wa_term_root_family (mti_term_id, root_code, root_gloss, registry_id)
VALUES (1600, 'AHAV', NULL, 103);
```

### DIR-003c — DOD root family (1 term missing)

Term: H1730G (mti.id=1602)

```sql
INSERT INTO wa_term_root_family (mti_term_id, root_code, root_gloss, registry_id)
VALUES (1602, 'DOD', NULL, 103);
```

**Verify — confirm 7 new records:**
```sql
SELECT mt.strongs_number, rf.root_code
FROM wa_term_root_family rf
JOIN mti_terms mt ON rf.mti_term_id = mt.id
WHERE mt.strongs_number IN ('G5370','G5373','G5384','G2705','G5382','H0157H','H1730G')
  AND rf.root_code IN ('FILOS','AHAV','DOD')
ORDER BY rf.root_code, mt.strongs_number;
```
Expected: 7 rows.

---

## DIR-004 — H2898 Verse Context Sub-Process

**Context:** H2898 (tuv, goodness) has been reinstated to extracted. It has 31 verse records. Verse-level inspection identified 14 as inner-being relevant (INCLUDE) and 17 as material goods/property (SET ASIDE). A verse_context_group must be created and verse_context records inserted/updated accordingly.

**This is a targeted Verse Context operation for a single term within an otherwise Complete registry. It does not reset the registry's verse_context_status.**

### Step 1 — Create verse_context_group for H2898

```sql
INSERT INTO verse_context_group (mti_term_id, group_code, context_description, notes, delete_flagged)
VALUES (
    546,
    '2898-001',
    'Term names divine goodness as an inner-being attribute and object of orientation — the abundant goodness of God stored up for those who fear him, gazed upon in the land of the living, satisfying the soul. Distinguished from tuv as material prosperity (set aside).',
    'Group created Stage 1 remediation 2026-04-12 — H2898 reinstated from delete.',
    0
);
```

### Step 2 — Insert verse_context records

**INCLUDE verses (14) — is_anchor and is_relevant:**

Designate the following as anchor (is_anchor=1): Exo 33:19 (divine goodness as character), Psa 27:13 (eschatological longing), Jer 31:14 (satisfaction of the soul), Hos 3:5 (relational return to divine goodness).
Remaining 10 INCLUDE verses: is_relevant=1, is_anchor=0.

```sql
-- Anchor verses (4)
INSERT INTO verse_context (verse_record_id, mti_term_id, group_id, is_anchor, is_relevant, is_related, notes, delete_flagged)
SELECT id, 546, (SELECT id FROM verse_context_group WHERE group_code = '2898-001'), 1, 1, 0, NULL, 0
FROM verse_records WHERE id IN (4325, 4336, 4348, 4349);

-- Related include verses (10)
INSERT INTO verse_context (verse_record_id, mti_term_id, group_id, is_anchor, is_relevant, is_related, notes, delete_flagged)
SELECT id, 546, (SELECT id FROM verse_context_group WHERE group_code = '2898-001'), 0, 1, 0, NULL, 0
FROM verse_records WHERE id IN (4327, 4331, 4335, 4337, 4338, 4339, 4341, 4344, 4347, 4351);

-- SET ASIDE verses (17) — is_relevant=0, no group assignment
INSERT INTO verse_context (verse_record_id, mti_term_id, group_id, is_anchor, is_relevant, is_related, notes, delete_flagged)
SELECT id, 546, NULL, 0, 0, 0, 'Material goods/property — set aside', 0
FROM verse_records WHERE id IN (4321, 4322, 4323, 4324, 4326, 4328, 4329, 4330, 4332, 4333, 4334, 4340, 4342, 4343, 4345, 4346, 4350);
```

**Note:** If `verse_records` is the correct table name for verse records in this database, use as shown. If the table is named differently (e.g. `wa_verse_records`), adjust accordingly.

### Step 3 — Verify R1–R4 consistency rules

```sql
-- R1: is_relevant=0 rows should have group_id NULL
SELECT COUNT(*) FROM verse_context WHERE mti_term_id = 546 AND is_relevant = 0 AND group_id IS NOT NULL;
-- Expected: 0

-- R2: is_anchor=1 rows should have is_relevant=1, is_related=0, group_id NOT NULL
SELECT COUNT(*) FROM verse_context WHERE mti_term_id = 546 AND is_anchor = 1 AND (is_relevant = 0 OR is_related = 1 OR group_id IS NULL);
-- Expected: 0

-- R4: term has at least one anchor
SELECT COUNT(*) FROM verse_context WHERE mti_term_id = 546 AND is_anchor = 1;
-- Expected: 4
```

---

## Confirmation Required

After applying all operations in this directive, confirm:

1. [ ] PATCH-20260412-103-PREANALYSIS-V1.json applied successfully
2. [ ] G7493 added to strongs_list as delete entry (DIR-001)
3. [ ] H2898 inventory reinstated: delete_flagged=0, owning_registry_fk=103 (DIR-002)
4. [ ] 7 root family records inserted (DIR-003): 5×FILOS, 1×AHAV, 1×DOD
5. [ ] verse_context_group 2898-001 created (DIR-004 Step 1)
6. [ ] 31 verse_context records inserted for H2898: 4 anchor, 10 related, 17 set aside (DIR-004 Step 2)
7. [ ] R1–R4 consistency rules: 0 violations (DIR-004 Step 3)
8. [ ] Fresh complete JSON export produced: wa-103-love-complete-[date].json

**When confirmed, Claude AI will proceed to Stage 2 (analytical passes).**

