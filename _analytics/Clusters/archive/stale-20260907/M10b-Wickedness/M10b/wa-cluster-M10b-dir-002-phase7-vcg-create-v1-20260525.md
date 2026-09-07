# wa-cluster-M10b-dir-002-phase7-vcg-create-v1-20260525

> Cluster directive — M10b Phase 7 (VCG structural apply + verse routing)
> Cluster: M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
> Date: 2026-05-25
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

---

## MOTIVATION

Phase 7 AI session produced a VCG design covering all 6 M10b sub-groups: **36 VCGs across 515 verses**. CC's §10.9 validation (existence, no-dual-membership, sum-match, anchor-in-members) returned PASS — see [wa-cluster-M10b-phase7-validation-v1-20260525.md](wa-cluster-M10b-phase7-validation-v1-20260525.md).

Source documents (`files phase 7/`):
- 6 per-sub-group VCG design documents
- Unified VCG creation JSON: `wa-cluster-M10b-vcg-creation-v1-20260525.json`

The three mandatory polysemy VCGs designated by the Phase 6 obslog are all present and routed:
- `M10b-A-VCG-01` Forensic-verdict register (5V) — M10 cross-register flag
- `M10b-B-VCG-01` Cosmic evil / evil one / evil age (13V) — M27 cross-register flag
- `M10b-E-VCG-01` Trouble and distress as the affliction of evil (7V) — M03/M27 cross-register flag

## SCOPE

### Operation A — INSERT `verse_context_group` rows (36)

One per VCG, with `group_code` = JSON's `provisional_code`, `context_description` = JSON's `description`, `vertical_pass_flag=0`.

VCG distribution per sub-group:
- M10b-A: 11 VCGs (190V)
- M10b-B: 6 VCGs (90V)
- M10b-C: 5 VCGs (40V)
- M10b-D: 6 VCGs (99V)
- M10b-E: 5 VCGs (79V)
- M10b-F: 3 VCGs (17V)

### Operation B — INSERT `vcg_term` links

For each VCG, one row per (vcg_id, mti_term_id) where the VCG covers any of the term's verses. Total: 53 rows.

### Operation C — UPDATE `verse_context.group_id`

For all 515 active is_relevant vc rows in M10b, set `group_id` to the new VCG id resolved from the unified JSON's `verses` arrays.

### Operation D — Anchor designation

- Clear existing `is_anchor=1` on M10b verses (35 prior anchors from inherited structure).
- Set `is_anchor=1` on the 36 Phase 7 designated VCG anchors.
- **R4 supplementary anchors:** 6 small terms (bdeluktos, faulos, ponēria, adikia, atopos, mir.sha.at) had their is_relevant verses placed in VCGs whose primary-anchor verse belongs to a different (larger) term. Per R4 (every term with is_relevant ≥1 needs ≥1 anchor), CC adds one supplementary anchor per failing term:

  | Term | Anchor | vc_id | VCG |
  |---|---|---:|---|
  | G0947 bdeluktos | Tit 1:16 | 27 | M10b-C-VCG-02 |
  | G5337 faulos | 2Cor 5:10 | 14486 | M10b-B-VCG-06 |
  | G4189 ponēria | Rom 1:29 | 14411 | M10b-B-VCG-05 |
  | G0093 adikia | Rom 1:18 | 14336 | M10b-B-VCG-05 |
  | G0824 atopos | Act 25:5 | 65874 | M10b-F-VCG-03 |
  | H4849 mir.sha.at | 2Ch 24:7 | 42511 | M10b-A-VCG-11 |

  Result: 5 VCGs end up with >1 anchor (the VCG primary + per-term supplementary). Total `is_anchor=1` on M10b verses: **42** (36 VCG anchors + 6 supplementary).

## OUTCOME REQUIRED

- 36 `verse_context_group` rows for M10b ✓
- 53 `vcg_term` links ✓
- 515 verse_context rows routed to new VCGs ✓
- 0 unrouted is_relevant rows ✓
- 0 H3 health-check violations (every term in a VCG has a vcg_term link) ✓
- R4 anchor gate PASS — every term with is_relevant ≥1 has ≥1 anchor ✓
- 42 `is_anchor=1` rows on M10b verses ✓

## COMPLETION CONFIRMATION

```sql
-- All 515 is_relevant routed to new M10b VCGs
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE mt.cluster_code='M10b' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0
  AND vcg.group_code LIKE 'M10b-%-VCG-%';
-- Returned 515 ✓

-- 36 new M10b VCGs
SELECT COUNT(*) FROM verse_context_group
WHERE group_code LIKE 'M10b-%-VCG-%'
  AND COALESCE(delete_flagged,0)=0;
-- Returned 36 ✓

-- R4 gate
SELECT mt.strongs_number, mt.transliteration,
   (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0) AS n_rel,
   (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0) AS n_anchor
FROM mti_terms mt
WHERE mt.cluster_code='M10b' AND COALESCE(mt.delete_flagged,0)=0;
-- All terms n_rel > 0 have n_anchor >= 1 ✓
```

## ROLLBACK

Restore from `backups/bible_research_backup_20260525_125925_M10b-phase7-vcg-create.db` for full integrity rollback. Alternatively:

```sql
BEGIN;
-- Clear new VCG references
UPDATE verse_context SET group_id=NULL
WHERE group_id IN (SELECT id FROM verse_context_group WHERE group_code LIKE 'M10b-%-VCG-%');
-- Restore prior anchors (cannot — inherited anchor state was cleared by Op D)
UPDATE verse_context SET is_anchor=0
WHERE id IN (SELECT vc.id FROM verse_context vc
  JOIN mti_terms mt ON mt.id = vc.mti_term_id
  WHERE mt.cluster_code='M10b' AND vc.is_anchor=1);
-- Delete new vcg_term + verse_context_group rows
DELETE FROM vcg_term WHERE vcg_id IN (SELECT id FROM verse_context_group WHERE group_code LIKE 'M10b-%-VCG-%');
DELETE FROM verse_context_group WHERE group_code LIKE 'M10b-%-VCG-%';
COMMIT;
```

(Note: inherited anchor state cannot be precisely restored from SQL alone — use the .db backup for that path.)

## SCRIPT

`scripts/_apply_m10b_phase7_vcg_create_20260525.py` — pre-checks, single-transaction apply of Ops A/B/C/D, post-checks including R4 gate. The R4 supplementary anchor patch was applied as an inline follow-on after the primary apply detected 6 failing terms.

---

*Applied 2026-05-25T12:59:25Z. Status: COMPLETE.*
