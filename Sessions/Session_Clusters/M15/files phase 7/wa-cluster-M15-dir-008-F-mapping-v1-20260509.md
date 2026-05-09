# wa-cluster-M15-dir-008-F-mapping-v1-20260509

> Cluster-process directive — M15 Group-Verse Mapping Apply — Sub-group F
> Directive ID: DIR-20260509-008
> Produced by: Claude AI — Session B Phase 7 — M15
> Source document: WA-M15-F-group-verse-mapping-v1-20260508.md
> Companion obslog: wa-obslog-M15-sessionb-v1-20260508.md
> Date: 2026-05-09

---

## DIRECTIVE ID

DIR-20260509-008

## MOTIVATION

Phase 6 Session B for cluster M15 produced a per-verse mapping document for sub-group M15-F (Meditative and reflective inner activity). Document `WA-M15-F-group-verse-mapping-v1-20260508.md` was produced by reading every non-set-aside verse individually (63 verses). Researcher approved the M15-F mapping.

Phase 7 flags for this sub-group:

- Flag F-1: P-status vr=157995 (Psa 69:12, si.ach) — assign to Group 799. Execute.
- Note: Prior 42-line batch-pass document superseded. CC uses WA-M15-F-group-verse-mapping-v1-20260508.md (215 lines, per-verse) as sole source.

---

## SCOPE

- **Cluster:** M15
- **Sub-group:** M15-F — Meditative and reflective inner activity
- **Source document:** `WA-M15-F-group-verse-mapping-v1-20260508.md`
- **Tables touched:** `verse_context_group` (UPDATE descriptions, INSERT new if required), `verse_context` (UPDATE assignments, UPSERT analysis_note, toggle is_anchor)
- **Groups in scope:** 798, 799, 1165, 1619, 1621, 1623, 1290, 1291, 1364, 1736, 1737, 1746, 1747, 2302
- **Terms in scope:** H7878 si.ach, H1901 ha.gig, G1761 enthumesis, H7881 si.chah, H1900 ha.gut, G1261 dialogismos, H7808 se.ach, G1260 dialogizomai, G1760 enthumeomai, H1902H hig.ga.von
- **Set-asides:** not re-evaluated unless mapping document explicitly re-includes them

---

## OUTCOME REQUIRED

1. All M15-F non-set-aside verses assigned to a group per the mapping document.
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
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-F')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code ORDER BY vcg.group_code;

-- 2. Anchor integrity (expect 0 rows — every group has exactly 1 anchor)
SELECT vcg.group_code, SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchors
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-F')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code HAVING anchors != 1;

-- 3. Set-aside count
SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-F')
  AND vc.set_aside_reason IS NOT NULL;
```

Save confirmation to: `WA-M15-F-group-mapping-applied-v1-20260509.md`

**Halt-on-error before any write** if pre-flight fails.

---

## NOTES

Mapping document is the sole analytical source. CC parses it at execution time. All observations grounded in per-verse reading.

*wa-cluster-M15-dir-008-F-mapping-v1-20260509 | DIR-20260509-008 | Phase 7 | M15-F | 2026-05-09*
