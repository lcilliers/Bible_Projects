# wa-cluster-M05-dir-003-term-rebind-v1-20260507

> Framework B Soul Word Analysis Programme — Cluster-process Directive
> Cluster: M05 — Love, Compassion and Kindness
> Directive sequence: dir-003 (term cluster reassignment)
> Version: v1 | Date: 20260507
> Instruction: wa-directive-instruction-v1_4-20260506 §11.3, §11.6
> Session B Instruction: wa-sessionb-cluster-instruction-v1_1-20260507 §7
> Status: READY FOR CC EXECUTION — researcher OQ-001 disposition confirmed 2026-05-07

---

## DIRECTIVE ID

`DIR-20260507-M05-003`

---

## MOTIVATION

During the Phase 4 control read for M05 (`wa-obslog-M05-love-compassion-kindness-v1-20260507`, Phase 4, OQ-001), H4263 mach.mal (mti_id=1264) was found to have a group description that does not match its assigned cluster characteristic.

**The problem:** H4263 mach.mal is currently in M05 with the gloss "compassion." However, its `verse_context_group` description reads: *"Term names the deepest inner yearning of the soul — intense longing for the sanctuary as cherished object."* This describes longing/attachment to the sanctuary, not sparing or compassion. The group evidence and the gloss point to different semantic fields.

**Analytical conclusion:** The term's actual verse evidence (intense longing for the sanctuary) does not carry the compassion characteristic of M05. It may belong in a cluster covering longing, desire, or attachment — but that determination requires researcher review of the underlying verse evidence, which is outside the scope of the current M05 session.

**Researcher confirmation:** OQ-001 disposition confirmed 2026-05-07. Term assigned to M05-BOUNDARY in dir-002 as a provisional holding position. This directive removes the term from M05 entirely and flags it for cluster reassignment review.

**Note on scope:** This directive removes H4263 mach.mal from M05 by clearing its `cluster_code` assignment. The correct destination cluster is not determined here — that requires a separate term-review pass. CC should flag this term in a review register so it is not orphaned.

---

## SCOPE

**Term:** H4263 mach.mal · `mti_id = 1264` · current `cluster_code = 'M05'`

**Tables touched:**

1. `mti_terms` — clear `cluster_code` and `cluster_subgroup_id` for mti_id=1264
2. `verse_context` — no change required (verse rows are retained; the term's verse-context data is preserved for when it is reassigned to the correct cluster)

**Operations:**

```sql
-- Operation 1: Remove from M05 cluster assignment
UPDATE mti_terms
SET cluster_code = NULL,
    cluster_subgroup_id = NULL
WHERE id = 1264
  AND strongs_number = 'H4263'
  AND cluster_code = 'M05';

-- Operation 2: Verify no orphaned cluster_subgroup rows
-- (mach.mal was assigned to M05-BOUNDARY in dir-002 — after this directive,
-- M05-BOUNDARY term count drops from 13 to 12; the cluster_subgroup row itself
-- is retained for the remaining 12 BOUNDARY terms)
```

**Companion action required of CC:** Add H4263 mach.mal (mti_id=1264) to the programme's term-review register (or equivalent tracking mechanism) with note: *"Removed from M05 during Phase 4 control read — group evidence describes longing for sanctuary, not compassion. Correct cluster destination not yet determined. Requires researcher review before reassignment."*

---

## OUTCOME REQUIRED

1. `mti_terms` row for mti_id=1264 (H4263 mach.mal) has `cluster_code = NULL` and `cluster_subgroup_id = NULL`.

2. M05-BOUNDARY sub-group term count is now **12** (was 13 in dir-002 scope; mach.mal removed).

3. Total M05 cluster term count is now **86** (was 87 at cluster open; mach.mal removed).

4. `verse_context` rows for mti_id=1264 are **unchanged** — preserved for future cluster assignment.

5. Term flagged in programme review register for future cluster determination.

6. No `wa_session_b_findings` rows written.

---

## COMPLETION CONFIRMATION

**Query 1 — confirm term removed from M05:**
```sql
SELECT id, strongs_number, transliteration, cluster_code, cluster_subgroup_id
FROM mti_terms
WHERE id = 1264;
```
Expected: `cluster_code = NULL`, `cluster_subgroup_id = NULL`

**Query 2 — updated M05 term counts:**
```sql
SELECT cs.subgroup_code, COUNT(mt.id) AS term_count
FROM cluster_subgroup cs
LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id = cs.id
WHERE cs.cluster_code = 'M05'
GROUP BY cs.subgroup_code
ORDER BY cs.subgroup_code;
```
Expected: M05-BOUNDARY = 12; all other sub-groups unchanged from dir-002; total = 86.

**Query 3 — verse_context rows preserved:**
```sql
SELECT COUNT(*) AS vc_rows_preserved
FROM verse_context
WHERE mti_term_id = 1264;
```
Expected: same count as before this directive (no verse rows deleted or modified).

**Query 4 — no unintended term removals:**
```sql
SELECT COUNT(*) AS m05_total
FROM mti_terms
WHERE cluster_code = 'M05';
```
Expected: 86

---

*wa-cluster-M05-dir-003-term-rebind-v1-20260507*
*Source obslog: wa-obslog-M05-love-compassion-kindness-v1-20260507 Phase 4, OQ-001*
*Companion: wa-cluster-M05-dir-002-subgroup-assign-v1-20260507*
*Application sequence: dir-002 must be applied before dir-003 (dir-003 reduces the M05-BOUNDARY count post dir-002)*
