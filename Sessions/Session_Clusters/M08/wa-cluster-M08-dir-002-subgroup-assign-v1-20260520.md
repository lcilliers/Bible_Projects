# wa-cluster-M08-dir-002-subgroup-assign-v1-20260520

> Cluster directive — M08 Phase 6 sub-group structural apply + verse routing
> Cluster: M08 — Pride, Arrogance and Boasting
> Date: 2026-05-20
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §9

---

## MOTIVATION

Phase 5 v2 (post-resubmission) designed **8 substantive sub-groups + 1 BOUNDARY** under the v2_8 §8.0 characteristic-driven discipline. CHAR-1 (Arrogant self-elevation, 151 verses, 51.2% on v1) was volume-split by **seat-of-pride axis** (per §8.6) into M08-A1 (heart) / M08-A2 (eyes & outward bearing) / M08-A3 (national / collective) / M08-A4 (general dispositional). CHAR-2 through CHAR-5 each carry a single sub-group (M08-B through M08-E). The 1 BOUNDARY verdict term G0193 akratēs has its own sub-group `M08-BOUNDARY`.

Phase 5.5 set-aside (researcher Option 2 direction, 2026-05-20) removed 174 non-M08-content verses from the substantive corpus (122 M22-register polysemic-residual + 52 narrative-marker / neutral-assertiveness). Substantive corpus dropped 470 → 296. §8.6 gate **PASS** post-resubmission: biggest substantive sub-group `M08-C` at 23.7% of 295.

Sources:
- Phase 5 v2 design: [WA-M08-subgroup-design-v2-20260520.md](files%20phase%205%20a/WA-M08-subgroup-design-v2-20260520.md)
- Phase 5 v2 mapping (AI): [WA-M08-subgroup-mapping-v2-20260520.json](files%20phase%205%20a/WA-M08-subgroup-mapping-v2-20260520.json)
- Phase 5 v2 mapping (CC-resolved, flat vc_id → sg): [WA-M08-subgroup-mapping-resolved-v2-20260520.json](WA-M08-subgroup-mapping-resolved-v2-20260520.json)
- §8.6 validation v2: [WA-M08-phase5-distribution-validation-v2-20260520.md](WA-M08-phase5-distribution-validation-v2-20260520.md)
- Phase 5.5 set-aside script: `scripts/_apply_m08_phase5_5_setaside_20260520.py` (applied 2026-05-20T19:01:43Z)

---

## SCOPE

### Sub-group catalogue

| subgroup_code | label | core_description (summary) | Char | Verses |
|---|---|---|---|---:|
| M08-A1 | Heart-Elevation — Pride Seated in the Heart | CHAR-1 split by seat_of_pride: heart (lev/kardia idiom) | CHAR-1 | 32 |
| M08-A2 | Eye-Elevation and Outward Bearing — Pride's Visible Register | CHAR-1 split by seat_of_pride: eyes_bearing (haughty eyes, posture) | CHAR-1 | 11 |
| M08-A3 | National and Collective Pride — Pride as a Corporate Inner Characteristic | CHAR-1 split by seat_of_pride: national_collective (nations, peoples, kings as subject) | CHAR-1 | 40 |
| M08-A4 | General Dispositional Pride — Individual Self-Elevation (Unspecified Seat) | CHAR-1 split by seat_of_pride: general_dispositional (Wisdom maxims, NT vice catalogues) | CHAR-1 | 68 |
| M08-B | Presumptuous Defiance — Pride as Willful Transgression | CHAR-2 (zid / za.don / zed / authadēs / tolmētēs) | CHAR-2 | 45 |
| M08-C | Boasting and Self-Display — Pride's Verbal and Public Form | CHAR-3 (kauchaomai family + alazoneia + ha.lal self-boast) — **M22 cross-register flag** | CHAR-3 | 70 |
| M08-D | Vain Conceit — Inflated Self-Estimate in the Mind | CHAR-4 (tufoō, fusioō, fusiōsis, huperfroneō) | CHAR-4 | 12 |
| M08-E | Pride of Power and Position — Arrogance in Strength, Wealth, and Authority | CHAR-5 (ga.on proud-might + archō domineering + hupsēlofroneō + ga.vah Eze 28:5 etc.) — **M23 cross-register flag** | CHAR-5 | 17 |
| M08-BOUNDARY | BOUNDARY — Qualifying / Supportive Register | G0193 akratēs (§6.3.1 reason 3 — supportive/qualifying) | — | 1 |

Total: **296 is_relevant** verses routed (295 substantive + 1 BOUNDARY).

### Operations

**Op A — INSERT cluster_subgroup rows**

```sql
INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description,
                              sort_order, status, version, source, created_at, last_updated_date)
VALUES (?, ?, ?, ?, ?, 'active', 'v1', 'wa-cluster-M08-dir-002-subgroup-assign-v1-20260520', ?, ?);
```

Insert 9 rows (M08-A1 .. M08-A4, M08-B, M08-C, M08-D, M08-E, M08-BOUNDARY).

Pre-check: `SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0` → 0.
Post-check: same query → 9.

**Op B — INSERT mti_term_subgroup rows**

For every distinct (mti_term_id, sub-group) pair derived from the resolved mapping, insert one `mti_term_subgroup` row. The primary sub-group for each term receives `placement_note = "[primary] {N} verses"`; additional rows are tagged `[secondary] {N} verses`.

```sql
INSERT INTO mti_term_subgroup (mti_term_id, cluster_subgroup_id, placement_note,
                               delete_flagged, created_at, last_updated_date)
VALUES (?, ?, ?, 0, ?, ?);
```

**Op C — UPDATE verse_context.cluster_subgroup_id**

For every is_relevant vc row in the resolved mapping, set `cluster_subgroup_id` to the matching cluster_subgroup.id.

```sql
UPDATE verse_context
SET cluster_subgroup_id = ?
WHERE id = ? AND COALESCE(delete_flagged,0) = 0;
```

296 UPDATE statements expected.

**Op D (skipped)** — `cluster.M08.status` already advanced to `'Analysis - In Progress'` by Phase 4 (dir-001). Confirm post-state still equals that value.

---

## OUTCOME REQUIRED

- 9 `cluster_subgroup` rows created for M08.
- ~46 `mti_term_subgroup` rows (one per distinct term/sub-group pair).
- 296 `verse_context.cluster_subgroup_id` populated.
- 0 `is_relevant=1` M08 verses with `cluster_subgroup_id IS NULL` after apply.
- `cluster.M08.status` remains `'Analysis - In Progress'`.

## COMPLETION CONFIRMATION

```sql
-- 9 sub-groups
SELECT COUNT(*) FROM cluster_subgroup
WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0;

-- 296 routed verses
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M08' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NOT NULL;

-- 0 unrouted
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code='M08' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL;

-- Per-sub-group breakdown
SELECT cs.subgroup_code, COUNT(vc.id)
FROM cluster_subgroup cs
LEFT JOIN verse_context vc ON vc.cluster_subgroup_id = cs.id AND vc.is_relevant=1
WHERE cs.cluster_code='M08' AND COALESCE(cs.delete_flagged,0)=0
GROUP BY cs.subgroup_code ORDER BY cs.sort_order;
```

## ROLLBACK

```sql
UPDATE verse_context SET cluster_subgroup_id=NULL
WHERE cluster_subgroup_id IN (SELECT id FROM cluster_subgroup WHERE cluster_code='M08');

DELETE FROM mti_term_subgroup
WHERE cluster_subgroup_id IN (SELECT id FROM cluster_subgroup WHERE cluster_code='M08');

DELETE FROM cluster_subgroup WHERE cluster_code='M08';
```

## SCRIPT

`scripts/_apply_m08_phase6_subgroup_assign_20260520.py` — runs Op A, Op B, Op C with pre/post checks.

---

*M08 Phase 6 sub-group assignment directive. Cross-register flags (M22 on M08-C; M23 on M08-E) carried forward via the design doc for Phase 7 VCG consumption. Characteristic mapping (CHAR-1..CHAR-5) is structural — to be loaded into `characteristic` + `characteristic_subgroup` tables at Phase 8.7 confirmation step under v2_8.*
