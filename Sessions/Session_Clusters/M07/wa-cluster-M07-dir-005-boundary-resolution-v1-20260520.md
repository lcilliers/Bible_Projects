# wa-cluster-M07-dir-005-boundary-resolution-v1-20260520

> Cluster directive — M07 Phase 8.5 BOUNDARY resolution
> Cluster: M07 — Shame, Disgrace and Humiliation
> Date: 2026-05-20
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §11A + §18.2

---

## MOTIVATION

Phase 3 v2 designated 5 BOUNDARY terms covering 27 is_relevant verses (and 1 zero-verse data-gap term). The AI Phase 8.5 disposition pass ([WA-M07-boundary-resolution-v1-20260519.md](WA-M07-boundary-resolution-v1-20260519.md)) produced 24 firm verdicts + 3 researcher-review items + 1 term-level recommendation. Researcher decisions captured in [WA-M07-phase85-researcher-decisions-v1-20260520.md](WA-M07-phase85-researcher-decisions-v1-20260520.md).

A **structural finding** from the AI disposition pass: ROUTE-TO-CLUSTER is **unavailable for all 27 verses** — the co-occurrence list ([WA-M07-boundary-cooccurrence-list-v1-20260519.md](WA-M07-boundary-cooccurrence-list-v1-20260519.md)) shows no other-cluster terms at any of these `wa_verse_records.id`. Per §18.2 eligibility, every disposition is either SET-ASIDE or PROMOTE-TO-SUBGROUP.

**Final disposition mix (post researcher review):**

| Disposition | Count | Verses |
|---|---:|---|
| SET-ASIDE | 4 | Phili 3:2 (katatomē); Isa 52:14 (mish.chat); Psa 113:6 (sha.phel — God's own condescension); Pro 16:19 (sha.phel — voluntary lowliness, M09 pickup note) |
| PROMOTE-TO-SUBGROUP M07-B | 1 | Lam 1:8 (ni.dah → M07-B-VCG-03 shame-as-moral-consequence) |
| PROMOTE-TO-SUBGROUP M07-D | 22 | 20 firm sha.phel "God-abases-the-proud" verses + Pro 29:23 + Eze 17:24 (researcher-confirmed) |
| Term-level SET-ASIDE-TERM | 1 | H8400 te.val.lul (mti_id=4712) — 0 is_relevant verses; no analytical basis for M07 retention |
| **Total** | **27 verses + 1 term** | |

## OPERATIONS

### Op A — SET-ASIDE (×4)

```sql
UPDATE verse_context SET is_relevant=0, set_aside_reason=?,
                         cluster_subgroup_id=NULL, group_id=NULL, is_anchor=0
WHERE id=? AND COALESCE(delete_flagged,0)=0;
```

### Op B — INSERT new mti_term_subgroup links (as needed)

For promoted terms not yet linked to the target sub-group (ni.dah → M07-B; sha.phel → M07-D), INSERT `mti_term_subgroup` row with `placement_note='[Phase 8.5 promotion] from BOUNDARY'`.

### Op C + Op E — PROMOTE-TO-SUBGROUP + VCG follow-on (×23)

Combined: each promoted verse gets `cluster_subgroup_id` and `group_id` updates in one statement.

**VCG sub-routing:**
- Lam 1:8 → M07-B-VCG-03 (shame as natural fruit of moral failure)
- Pro 25:7, Jer 13:18, Eze 21:26 → M07-D-VCG-01 (social/bodily humiliation)
- All other 19 sha.phel verses → M07-D-VCG-03 (divine abasement of pride)

```sql
UPDATE verse_context SET cluster_subgroup_id=?, group_id=?
WHERE id=? AND COALESCE(delete_flagged,0)=0;
```

### Op T — Term-level SET-ASIDE-TERM for H8400

```sql
UPDATE mti_terms SET status='excluded', exclusion_reason=?, delete_flagged=1, last_changed=?
WHERE id=4712 AND cluster_code='M07' AND COALESCE(delete_flagged,0)=0;
```

### Op F — Clear BOUNDARY_DECISION_PENDING flags

Filter to the 5 BOUNDARY-term Strong's codes (G2699, H4893A, H5206, H8213, H8400) on M07's contributing registries; mark `resolved=1` with audit note.

## OUTCOME REQUIRED

- 4 `verse_context.is_relevant=0` UPDATEs with set_aside_reason.
- 23 `verse_context` UPDATEs with new `cluster_subgroup_id` + `group_id`.
- 2 new `mti_term_subgroup` rows (ni.dah → M07-B; sha.phel → M07-D).
- 1 `mti_terms` UPDATE for H8400 te.val.lul (status='excluded', delete_flagged=1).
- M07-BOUNDARY active is_relevant count = 0.
- M07 total is_relevant = 359 (363 − 4 set-aside).
- M07-D count = 50 + 22 = 72.
- M07-B count = 110 + 1 = 111.

## COMPLETION CONFIRMATION

```sql
-- 0
SELECT COUNT(*) FROM verse_context vc
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE cs.cluster_code='M07' AND cs.subgroup_code='M07-BOUNDARY'
  AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0;

-- 359
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M07' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0;

-- 'excluded'
SELECT status FROM mti_terms WHERE id=4712;
```

## CROSS-CLUSTER CARRY-FORWARD NOTES

Recorded for downstream sessions:

- **Lam 1:8 ni.dah** — M12 (purity) dimension flagged for Phase 9 T6 cross-cluster note when M12 opens.
- **Pro 16:19 sha.phel SET-ASIDE** — M09 (Humility/Meekness) pickup note: this verse evidences voluntary-lowliness (M09's characteristic); when M09 session opens, sha.phel may be one of its home-registry terms covering this verse.
- **Pro 29:23 sha.phel PROMOTE M07-D** — Phase 9 T6 cross-cluster relationship note: verse pairs M07 enforced-humiliation with M09 voluntary-lowliness in one proverb; the lowliness-honour half is M09 content.

## SCRIPT

`scripts/_apply_m07_phase85_boundary_resolution_20260520.py` — runs all operations with pre/post checks.

---

*Phase 8.5 BOUNDARY resolution applied. Ready for Phase 8.7 — Characteristic mapping (v2_8 §11B; under v2_8 this is a confirmation step since Phase 5 designed sub-groups to represent characteristics from the start).*
