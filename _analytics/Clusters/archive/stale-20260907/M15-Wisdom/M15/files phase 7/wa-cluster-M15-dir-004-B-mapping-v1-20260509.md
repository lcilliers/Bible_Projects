# wa-cluster-M15-dir-004-B-mapping-v1-20260509

> Cluster-process directive — M15 Group-Verse Mapping Apply — Sub-group B
> Directive ID: DIR-20260509-004
> Produced by: Claude AI — Session B Phase 7 — M15
> Source document: WA-M15-B-group-verse-mapping-v1-20260508.md
> Companion obslog: wa-obslog-M15-sessionb-v1-20260508.md
> Date: 2026-05-09

---

## DIRECTIVE ID

DIR-20260509-004

## MOTIVATION

Phase 6 Session B for cluster M15 produced a per-verse mapping document for sub-group M15-B (Understanding as inner faculty). Document `WA-M15-B-group-verse-mapping-v1-20260508.md` was produced by reading every non-set-aside verse individually (285 verses). Researcher approved the M15-B mapping.

Phase 7 flags for this sub-group:

- Flag B-1: vr=7138 (Hos 13:2, te.vu.nah) — proposed move to M15-A (craft-skill use). CC to verify and execute move if consistent with mapping.
- Flag B-2: Groups 2341 and 2343 — may merge. CC to verify verse content and merge if no distinct phenomena lost.
- Flag B-3: vr=173355 (1Sa 3:8) and vr=27737 (Job 13:1) — may be misassigned to failure-group 1363. CC to verify and reassign if misassigned.

---

## SCOPE

- **Cluster:** M15
- **Sub-group:** M15-B — Understanding as inner faculty
- **Source document:** `WA-M15-B-group-verse-mapping-v1-20260508.md`
- **Tables touched:** `verse_context_group` (UPDATE descriptions, INSERT new if required), `verse_context` (UPDATE assignments, UPSERT analysis_note, toggle is_anchor)
- **Groups in scope:** 2341, 2342, 2343, 2494, 1363, and others per mapping doc
- **Terms in scope:** H0995 bin, H8394 te.vu.nah, G4907 sunesis, G4920 suniemi (understanding register), H0998 bi.nah, G3563 nous (understanding register)
- **Set-asides:** not re-evaluated unless mapping document explicitly re-includes them

---

## OUTCOME REQUIRED

1. All M15-B non-set-aside verses assigned to a group per the mapping document.
2. Every group has exactly one anchor verse (is_anchor = TRUE).
3. Group descriptions updated to match mapping document.
4. Per-verse analysis_note populated from 'What the verse shows' column.
5. All researcher-approved flag operations executed as specified above.
6. Set-aside row count unchanged (except where flags explicitly change SA status).

---

## COMPLETION CONFIRMATION

CC runs the following after applying:

```sql
-- 1. Verse count per group
SELECT vcg.group_code, COUNT(vc.id) as verse_count,
       SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchor_count
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-B')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code ORDER BY vcg.group_code;

-- 2. Anchor integrity (expect 0 rows — every group has exactly 1 anchor)
SELECT vcg.group_code, SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchors
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-B')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code HAVING anchors != 1;

-- 3. Set-aside count
SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-B')
  AND vc.set_aside_reason IS NOT NULL;
```

Save confirmation to: `WA-M15-B-group-mapping-applied-v1-20260509.md`

**Halt-on-error before any write** if pre-flight fails.

---

## NOTES

Mapping document is the sole analytical source. CC parses it at execution time. All observations grounded in per-verse reading.

*wa-cluster-M15-dir-004-B-mapping-v1-20260509 | DIR-20260509-004 | Phase 7 | M15-B | 2026-05-09*
