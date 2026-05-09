# wa-cluster-M15-dir-003-A-mapping-v1-20260509

> Cluster-process directive — M15 Group-Verse Mapping Apply — Sub-group A
> Directive ID: DIR-20260509-003
> Produced by: Claude AI — Session B Phase 7 — M15 Wisdom, Understanding and Knowledge
> Source document: WA-M15-A-group-verse-mapping-v2-20260508.md
> Companion obslog: wa-obslog-M15-sessionb-v1-20260508.md
> Date: 2026-05-09

---

## DIRECTIVE ID

DIR-20260509-003

## MOTIVATION

Phase 6 of Session B for cluster M15 produced a per-verse group-verse mapping document for sub-group M15-A (Wisdom as inner character and capacity). The mapping document `WA-M15-A-group-verse-mapping-v2-20260508.md` (542 lines) was produced by reading every non-set-aside verse individually and confirming or revising group assignments from the verse text. It supersedes the prior v1 (insufficient batch-pass). The researcher approved the M15-A mapping.

This directive instructs CC to apply that mapping to the database: updating group descriptions, anchor designations, per-verse analysis notes, and carrying two accumulated Phase 7 flags:

- **Flag A-1:** Groups 2473 and 2474 require splitting. Group 2473 (cha.kham craft-wisdom with Spirit-given competence) and 2474 ('wise men' in court/professional contexts) are distinct phenomena and must be separated into clean groups before Phase 8.
- **Flag A-2:** vr=54610 (2Sa 14:14, H4191 mut) is misassigned from registry 1751 to M15-E context; correct assignment is within M15-A under the wise-woman-of-Tekoa group. This is a cross-sub-group misassignment to be verified and corrected.

---

## SCOPE

- **Cluster:** M15
- **Sub-group:** M15-A — Wisdom as inner character and capacity
- **Source document:** `WA-M15-A-group-verse-mapping-v2-20260508.md`
- **Tables touched:** `verse_context_group` (UPDATE descriptions, INSERT new groups if splits required), `verse_context` (UPDATE group assignments, UPSERT analysis_note, toggle is_anchor)
- **Groups in scope:** 392, 393, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 2221, 2473, 2474 (subject to split), and any new group codes produced by the 2473/2474 split
- **Terms in scope:** H2450 cha.kham, H2454 chokmot, H7922 se.khel, G4678 sofia, G4679 sofizō, G5429 fronimos, G5430 fronimōs, G5426 froneō, G4920 suniēmi-A (wisdom register), H7919B sa.khal, H2449 cha.kam, H6493 piqqeach, G3861 paradoxos, H8454 tu.shi.yah, G4680 sofos, G781 asofos
- **Set-asides:** not re-evaluated unless the mapping document explicitly re-includes them
- **Flag A-1 scope:** Split groups 2473 and 2474. Create two new groups from 2473 (Spirit-given craft-competence / inner wisdom endowment) and retain/revise 2474 (court professional wisdom). Reassign affected verse_context rows to correct new groups. One anchor per new group.
- **Flag A-2 scope:** Verify vr=54610 (2Sa 14:14) assignment; correct if misassigned.

---

## OUTCOME REQUIRED

1. All M15-A non-set-aside verses assigned to a group per the mapping document.
2. Every group has exactly one anchor verse (`is_anchor = TRUE`).
3. Group descriptions updated to match mapping document descriptions.
4. Per-verse `analysis_note` populated from the 'What the verse shows' column of the mapping document.
5. Groups 2473 and 2474 split into clean sub-groups with non-overlapping verse sets and independent anchors.
6. vr=54610 assignment verified and corrected if misassigned.
7. Set-aside row count for M15-A terms unchanged.

---

## COMPLETION CONFIRMATION

CC runs the following after applying:

```sql
-- 1. Verse count per group for M15-A terms
SELECT vcg.group_code, vcg.description, COUNT(vc.id) as verse_count,
       SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchor_count
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-A')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code, vcg.description
ORDER BY vcg.group_code;

-- 2. Anchor count check (every group must have exactly 1)
SELECT vcg.group_code, SUM(CASE WHEN vc.is_anchor THEN 1 ELSE 0 END) as anchors
FROM verse_context_group vcg
JOIN verse_context vc ON vc.group_id = vcg.id
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15' AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-A')
  AND mt.status IN ('extracted','extracted_thin')
GROUP BY vcg.group_code HAVING anchors != 1;
-- Expected: 0 rows (every group has exactly 1 anchor)

-- 3. Set-aside count unchanged
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M15'
  AND mt.cluster_subgroup_id = (SELECT id FROM cluster_subgroup WHERE subgroup_code = 'M15-A')
  AND vc.set_aside_reason IS NOT NULL;
```

Save confirmation report to: `WA-M15-A-group-mapping-applied-v1-20260509.md`

**Halt-on-error before any write** if pre-flight fails (verse references unresolvable, group_id mismatches, term not in M15-A sub-group).

---

## NOTES

- The M15-A mapping document (v2) supersedes the prior v1 (42 lines, batch-pass). CC uses v2 as the sole source.
- Flag A-1 (group split) may produce new group codes; CC assigns sequential codes following the cluster's existing group-code pattern.
- Flag A-2 is a verification task: CC confirms vr=54610's current group assignment and corrects if not consistent with the mapping document's determination.

*wa-cluster-M15-dir-003-A-mapping-v1-20260509 | DIR-20260509-003 | Phase 7 | M15-A | 2026-05-09*
