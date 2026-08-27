# wa-cluster-M15-dir-007-E-mapping-v1-20260509

> Cluster-process directive — M15 Group-Verse Mapping Apply — Sub-group E
> Directive ID: DIR-20260509-007
> Produced by: Claude AI — Session B Phase 7 — M15
> Source document: WA-M15-E-group-verse-mapping-v1-20260508.md
> Companion obslog: wa-obslog-M15-sessionb-v1-20260508.md
> Date: 2026-05-09

---

## DIRECTIVE ID

DIR-20260509-007

## MOTIVATION

Phase 6 Session B for cluster M15 produced a per-verse mapping document for sub-group M15-E (Planning, purposing and deliberative counsel). Document `WA-M15-E-group-verse-mapping-v1-20260508.md` was produced by reading every non-set-aside verse individually (188 verses). Researcher approved the M15-E mapping.

Phase 7 flags for this sub-group:

- Flag E-1 (RESEARCHER APPROVED): vr=15187 (Isa 9:6, ya.ats) — confirmed move from Group 406 to Group 407. Execute.
- Flag E-2 (RESEARCHER APPROVED): vr=130804 (Psa 40:17, H2803I) — confirmed move from Group 1766 to Group 1767. Execute.
- Flag E-3 (RESEARCHER APPROVED): vr=130773 (Gen 50:20, H2803I) — confirmed dual assignment to both Group 1766 and Group 1767. Insert second verse_context row if not already present. Execute.

---

## SCOPE

- **Cluster:** M15
- **Sub-group:** M15-E — Planning, purposing and deliberative counsel
- **Source document:** `WA-M15-E-group-verse-mapping-v1-20260508.md`
- **Tables touched:** `verse_context_group` (UPDATE descriptions, INSERT new if required), `verse_context` (UPDATE assignments, UPSERT analysis_note, toggle is_anchor)
- **Groups in scope:** 406, 407, 408, 1766, 1767, 1768-1776, 2097, 2225-2228 and others per mapping doc
- **Terms in scope:** H2803I cha.shav-I (purposing), H6098 e.tsah, H3289 ya.ats, H4284 mach.sha.vah, G1011 boule, G1014 boulomai, G4286 prothesis, G1106 gnome, G1013 boulema
- **Set-asides:** not re-evaluated unless mapping document explicitly re-includes them

---

## OUTCOME REQUIRED

1. All M15-E non-set-aside verses assigned to a group per the mapping document.
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
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-E')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code ORDER BY vcg.group_code;

-- 2. Anchor integrity (expect 0 rows — every group has exactly 1 anchor)
SELECT vcg.group_code, SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchors
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-E')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code HAVING anchors != 1;

-- 3. Set-aside count
SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-E')
  AND vc.set_aside_reason IS NOT NULL;
```

Save confirmation to: `WA-M15-E-group-mapping-applied-v1-20260509.md`

**Halt-on-error before any write** if pre-flight fails.

---

## NOTES

Mapping document is the sole analytical source. CC parses it at execution time. All observations grounded in per-verse reading.

*wa-cluster-M15-dir-007-E-mapping-v1-20260509 | DIR-20260509-007 | Phase 7 | M15-E | 2026-05-09*
