# wa-cluster-M07-dir-003-vcg-create-v1-20260519

> Cluster directive — M07 Phase 7 VCG creation
> Cluster: M07 — Shame, Disgrace and Humiliation
> Date: 2026-05-19
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10.5

---

## MOTIVATION

Phase 7 AI design produced **29 VCGs across 9 sub-groups** for M07's 363 is_relevant verses. Source: 9 per-sub-group design documents ([WA-M07-M07-A-vcg-design-v1-20260519.md](WA-M07-M07-A-vcg-design-v1-20260519.md) through [WA-M07-M07-BOUNDARY-vcg-design-v1-20260519.md](WA-M07-M07-BOUNDARY-vcg-design-v1-20260519.md)) + unified JSON ([WA-M07-vcg-creation-v1-20260519.json](WA-M07-vcg-creation-v1-20260519.json)).

CC validation (per §10.9) PASSED:
- 363 verses across 29 VCGs — per-sub-group sums match DB.
- No phantom vc_ids, no duplicates, every anchor in its VCG's `verses` array.
- BOUNDARY VCG (M07-BOUNDARY-VCG-01) holds all 27 BOUNDARY-term verses.
- No `key_verses` / `members` field misuse — complete `verses` arrays per §10.8.

Per-sub-group VCG counts: M07-A: 5, M07-B: 5, M07-C: 4, M07-D: 4, M07-E: 2, M07-F: 3, M07-G: 3, M07-H: 2, M07-BOUNDARY: 1 → total 29.

Cross-register flag preservation observed in the VCG context_descriptions: M07-G VCGs distinguish dismissive contempt / active mockery / verbal attack mechanisms with M06 source-side noted inline. M07-H VCGs note the M12 purity register alongside the M07 shield-against-shame angle.

## OPERATIONS

### Op A — INSERT `verse_context_group` rows (×29)

One row per VCG. `group_code` = provisional code from JSON (`M07-A-VCG-01` form). `context_description` from the JSON. `vertical_pass_flag = 0`.

### Op B — INSERT `vcg_term` rows (×~126)

For each VCG, one row per (vcg_id, mti_term_id) where the VCG covers any of the term's verses. `placement_note='Phase 7 routing'`.

### Op C — UPDATE `verse_context.group_id` (×363)

Set each is_relevant vc row's `group_id` to its new VCG. WHERE includes `delete_flagged=0`.

### Op D — UPDATE `verse_context.is_anchor`

Two-stage:
1. Clear prior anchors on M07 verses (`UPDATE ... SET is_anchor=0 WHERE cluster_code=M07 AND is_anchor=1`).
2. Set `is_anchor=1` on the 29 Phase-7-designated anchor verses.

## OUTCOME REQUIRED

- 29 `verse_context_group` rows inserted with M07 group_codes.
- ~126 `vcg_term` rows inserted.
- 363 `verse_context` rows have `group_id` set to a new M07 VCG.
- 29 `verse_context` rows have `is_anchor=1` within the cluster (one per VCG).
- Old (inherited) VCGs still present in DB but no is_relevant verse references them — Phase 8 dissolves them with researcher comparison report.

## COMPLETION CONFIRMATION

```sql
-- Should return 29
SELECT COUNT(*) FROM verse_context_group WHERE group_code LIKE 'M07%-VCG-%' AND COALESCE(delete_flagged,0)=0;

-- Should return 363
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE mt.cluster_code='M07' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0
  AND vcg.group_code LIKE 'M07%-VCG-%';

-- Should return 29
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M07' AND vc.is_anchor=1
  AND COALESCE(vc.delete_flagged,0)=0;
```

## POST-CHECK FINDINGS (informational, non-blocking)

- **H3 = 1**: H8400 te.val.lul (mti_id=4712) has no vcg_term link because it has zero is_relevant verses (data-gap flagged at Phase 3 BOUNDARY). Will be dispositioned at Phase 8.5.
- **R4 = 20 OWNER terms without active anchor**: anchors are designated per-VCG, not per-term. Terms whose verses sit in VCGs whose anchor is on a different term naturally lack their own anchor. Strict per-term R4 (≥1 anchor) is verified at Phase 12 closure; at Phase 7 the VCG-level anchor is the operative requirement.

## ROLLBACK

Use the pre-run DB backup. The script reverses are:

```sql
-- Op D reset: rely on backup (prior anchor state is cluster-specific)
-- Op C reset: UPDATE verse_context SET group_id=NULL WHERE id IN (Phase 7 routed set)
DELETE FROM vcg_term WHERE vcg_id IN (SELECT id FROM verse_context_group WHERE group_code LIKE 'M07%-VCG-%');
DELETE FROM verse_context_group WHERE group_code LIKE 'M07%-VCG-%';
```

## SCRIPT

`scripts/_apply_m07_phase7_vcg_create_20260519.py` — runs all four operations with pre/post checks.

---

*Phase 7 directive applied. Ready for Phase 8 (dissolve inherited VCGs with researcher comparison).*
