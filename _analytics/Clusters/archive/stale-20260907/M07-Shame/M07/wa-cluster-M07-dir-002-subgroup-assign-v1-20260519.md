# wa-cluster-M07-dir-002-subgroup-assign-v1-20260519

> Cluster directive — M07 Phase 6 sub-group structural apply
> Cluster: M07 — Shame, Disgrace and Humiliation
> Date: 2026-05-19
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §9

---

## MOTIVATION

Phase 5 produced an 8-sub-group + BOUNDARY design representing 6 inner-being characteristics ([WA-M07-subgroup-design-v1-20260519.md](WA-M07-subgroup-design-v1-20260519.md), mapping [WA-M07-subgroup-mapping-v1-20260519.json](WA-M07-subgroup-mapping-v1-20260519.json)). Per v2_8 §8.0, sub-groups represent characteristics: CHAR-1 (Shame as experienced inner state) is volume-split into M07-A/B/C (33%/15%/15% of substantive); CHAR-2 through CHAR-6 each map 1:1 to M07-D/E/F/G/H. M07-G carries a cross-register flag to M06; M07-H to M12.

Distribution gate ([WA-M07-phase5-distribution-validation-v1-20260519.md](WA-M07-phase5-distribution-validation-v1-20260519.md)): biggest sub-group M07-B at 32.7% — **PASS** (under 40%).

## OPERATIONS

### Op 0 — Soft-delete 2 orphan vc rows

The 2 orphan verse_context rows from Phase 2 (vr.delete_flagged=1, no analysis_note) cannot be routed to a sub-group. Same cleanup pattern as M04 Step 1 orphan precedent. Soft-delete brings M07 is_relevant count from 365 → 363, matching the Phase 5 mapping exactly.

| vc_id | mti_id | Strong's | Reference |
|---:|---:|---|---|
| 34973 | 324 | G0152 aischunē | Php 3:19 |
| 49397 | 628 | G2699 katatomē | Php 3:2 |

```sql
UPDATE verse_context SET delete_flagged=1, last_changed=?
WHERE id IN (34973, 49397) AND COALESCE(delete_flagged,0)=0;
```

### Op A — INSERT `cluster_subgroup` rows (×9)

One row per sub-group (M07-A through M07-H + M07-BOUNDARY). Fields per §A1: `cluster_code='M07'`, `subgroup_code`, `label`, `core_description`, `sort_order` (0-based by listed order), `status='active'`, `version='v1'`, `source` (directive id), timestamps.

### Op B — INSERT `mti_term_subgroup` rows

For every (term, sub-group) pair derived from the mapping. Primary placement = sub-group with the largest verse count for the term; secondary placements for multi-faceted terms (per Phase 5 §3). `placement_note` records `[primary] N verses` or `[secondary] N verses`.

### Op C — UPDATE `verse_context.cluster_subgroup_id` (×363)

Set each is_relevant vc row's cluster_subgroup_id per the mapping. WHERE includes `id=? AND COALESCE(delete_flagged,0)=0` (post-Op-0 the 2 orphans are soft-deleted and excluded).

### Op D — Skipped

`cluster.M07.status` was advanced to `Analysis - In Progress` at Phase 4 (dir-001). Op D N/A.

## OUTCOME REQUIRED

- 2 orphan vc rows soft-deleted (delete_flagged=1).
- 9 `cluster_subgroup` rows created for M07.
- N `mti_term_subgroup` rows created (~50 expected — one per primary plus secondaries for multi-faceted terms).
- 363 `verse_context` rows have non-NULL `cluster_subgroup_id`.
- 0 M07 is_relevant verse_context rows remain unrouted.

## COMPLETION CONFIRMATION

```sql
-- Should return 9
SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0;

-- Should return 0 (no unrouted is_relevant)
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M07' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL;

-- Should return 363
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M07' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NOT NULL;
```

## ROLLBACK

```sql
-- Reverse Op C (UPDATEs are not safely reversible without a snapshot; rely on
-- the pre-run DB backup taken by the patch-applier convention).
-- Op B + Op A: delete inserted rows.
DELETE FROM mti_term_subgroup WHERE cluster_subgroup_id IN
  (SELECT id FROM cluster_subgroup WHERE cluster_code='M07');
DELETE FROM cluster_subgroup WHERE cluster_code='M07';
-- Op 0: un-soft-delete orphans
UPDATE verse_context SET delete_flagged=0 WHERE id IN (34973, 49397);
```

(Full rollback should use the pre-run row-level backup from `archive/patches/` or DB snapshot taken before this directive applied.)

## SCRIPT

`scripts/_apply_m07_phase6_subgroup_assign_20260519.py` — runs all operations with pre/post checks.

---

*Phase 6 directive. Ready for execution.*
