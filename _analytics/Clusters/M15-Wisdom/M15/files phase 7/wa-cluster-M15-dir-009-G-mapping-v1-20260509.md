# wa-cluster-M15-dir-009-G-mapping-v1-20260509

> Cluster-process directive — M15 Group-Verse Mapping Apply — Sub-group G
> Directive ID: DIR-20260509-009
> Produced by: Claude AI — Session B Phase 7 — M15
> Source document: WA-M15-G-group-verse-mapping-v1-20260509.md
> Companion obslog: wa-obslog-M15-sessionb-v1-20260508.md
> Date: 2026-05-09

---

## DIRECTIVE ID

DIR-20260509-009

## MOTIVATION

Phase 6 Session B for cluster M15 produced a per-verse mapping document for sub-group M15-G (Inner thought-content — the mind's formed thoughts). Document `WA-M15-G-group-verse-mapping-v1-20260509.md` was produced by reading every non-set-aside verse individually (27 verses). Researcher approved the M15-G mapping.

Phase 7 flags for this sub-group:

- Note: Prior 34-line batch-pass document superseded. CC uses WA-M15-G-group-verse-mapping-v1-20260509.md (173 lines, per-verse) as sole source.
- No researcher-approved verse-move flags for M15-G. All 27 verses assigned per mapping document.

---

## SCOPE

- **Cluster:** M15
- **Sub-group:** M15-G — Inner thought-content — the mind's formed thoughts
- **Source document:** `WA-M15-G-group-verse-mapping-v1-20260509.md`
- **Tables touched:** `verse_context_group` (UPDATE descriptions, INSERT new if required), `verse_context` (UPDATE assignments, UPSERT analysis_note, toggle is_anchor)
- **Groups in scope:** 1516, 1517, 2298, 2299, 2300, 2301, 2285, 2098, 1824, 1748, 1793
- **Terms in scope:** H4093 mad.da (thought-content register), H6248 ash.tut, G3540 noema, G5424 fren, G1771 ennoia, G1963 epinoia, G1270 dianoema, H6250 esh.to.nah, H7476 ra.yon, H7454 re.a
- **Set-asides:** not re-evaluated unless mapping document explicitly re-includes them

---

## OUTCOME REQUIRED

1. All M15-G non-set-aside verses assigned to a group per the mapping document.
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
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-G')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code ORDER BY vcg.group_code;

-- 2. Anchor integrity (expect 0 rows — every group has exactly 1 anchor)
SELECT vcg.group_code, SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchors
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-G')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code HAVING anchors != 1;

-- 3. Set-aside count
SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-G')
  AND vc.set_aside_reason IS NOT NULL;
```

Save confirmation to: `WA-M15-G-group-mapping-applied-v1-20260509.md`

**Halt-on-error before any write** if pre-flight fails.

---

## NOTES

Mapping document is the sole analytical source. CC parses it at execution time. All observations grounded in per-verse reading.

*wa-cluster-M15-dir-009-G-mapping-v1-20260509 | DIR-20260509-009 | Phase 7 | M15-G | 2026-05-09*
