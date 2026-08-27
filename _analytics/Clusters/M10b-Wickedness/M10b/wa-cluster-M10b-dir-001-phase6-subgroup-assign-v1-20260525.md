# wa-cluster-M10b-dir-001-phase6-subgroup-assign-v1-20260525

> Cluster directive — M10b Phase 6 (sub-group structural apply + verse routing)
> Cluster: M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
> Date: 2026-05-25
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §9

---

## MOTIVATION

Phase 5 produced a sub-group design with 6 characteristics → 6 sub-groups (1:1, no volume-splits), all within the 40% / 206-verse distribution gate. Source documents:

- Design: [WA-M10b-subgroup-design-v1-20260525.md](WA-M10b-subgroup-design-v1-20260525.md)
- Mapping (term-level + split rules): [wa-cluster-M10b-subgroup-mapping-v1-20260525.json](wa-cluster-M10b-subgroup-mapping-v1-20260525.json)
- Validation: [wa-cluster-M10b-phase5-validation-v1-20260525.md](wa-cluster-M10b-phase5-validation-v1-20260525.md) (PASS)
- Resolved flat mapping: [wa-cluster-M10b-subgroup-mapping-resolved-v1-20260525.json](wa-cluster-M10b-subgroup-mapping-resolved-v1-20260525.json) (written by the apply script)

The to.e.vah C/D split was resolved by parsing the AI's D-passage-group list (Lev, Deu, historical reforms, Ezr, Jer, Eze idolatry corpus) against active verse references; any to.e.vah verse not in the D-list defaults to C (moral-character abomination — the broader category). Result: to.e.vah → 35 C / 72 D.

## SCOPE

### Operation A — INSERT cluster_subgroup rows (6)

| code | label | est. verses |
|---|---|---:|
| M10b-A | The wicked person — settled inner orientation of wickedness | 190 |
| M10b-B | Evil as the constitutional nature of the inner person | 90 |
| M10b-C | Abomination — divine revulsion at corrupt moral character and conduct | 40 |
| M10b-D | Idolatrous abomination — will conformed to detestable false devotion | 99 |
| M10b-E | Iniquity — evil as an active inner process of scheming and harm-generation | 79 |
| M10b-F | Blasphemy and defaming evil — wickedness flowing through the instrument of speech | 17 |

Each row gets `core_description` from §2 of the design document, `sort_order` matching the listing above, `status='active'`, `version='v1'`, `source=DIRECTIVE_ID`.

Distribution: largest sub-group (M10b-A) at 190 / 515 = **36.9%**, within the 40% / 206-verse gate.

### Operation B — INSERT mti_term_subgroup rows

For each term in M10b (17 active OWNERs), insert one row per (term, sub-group) it touches:

- Primary placement (`[primary] N verses`) — the sub-group carrying the majority of the term's verses.
- Secondary placement (`[secondary] N verses`) — for the three multi-faceted terms:
  - to.e.vah primary M10b-D (72V) + secondary M10b-C (35V)
  - bdelugma primary M10b-C (4V) + secondary M10b-D (2V)
  - ro.a primary M10b-E (13V) + secondary M10b-A (1V, 1Sa 17:28)

Total: 17 primary + 3 secondary = **20 rows**.

### Operation C — UPDATE verse_context.cluster_subgroup_id

For all 515 active is_relevant vc rows in M10b, set `cluster_subgroup_id` to the sub-group ID resolved from the term-level mapping + per-verse split rules.

### Operation D — Cluster status

`cluster.M10b.status` `'Data - In Progress'` → `'Analysis - In Progress'` (Phase 4 was skipped per §7.5; this directive carries the transition per §7.6 / §9.5).

## OUTCOME REQUIRED

- 6 `cluster_subgroup` rows for M10b ✓
- 20 `mti_term_subgroup` rows (17 primary + 3 secondary) ✓
- 515 vc rows with `cluster_subgroup_id` set ✓
- 0 unrouted is_relevant vc rows ✓
- cluster status = 'Analysis - In Progress' ✓

## COMPLETION CONFIRMATION

```sql
SELECT subgroup_code, COUNT(vc.id) AS verses
FROM cluster_subgroup cs
LEFT JOIN verse_context vc ON vc.cluster_subgroup_id = cs.id
  AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
WHERE cs.cluster_code='M10b' AND COALESCE(cs.delete_flagged,0)=0
GROUP BY subgroup_code ORDER BY subgroup_code;

SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id=vc.mti_term_id
WHERE mt.cluster_code='M10b' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL;
-- Returned 0 ✓

SELECT status FROM cluster WHERE cluster_code='M10b';
-- Returned 'Analysis - In Progress' ✓
```

## ROLLBACK

```sql
BEGIN;
UPDATE verse_context SET cluster_subgroup_id=NULL
WHERE cluster_subgroup_id IN (SELECT id FROM cluster_subgroup WHERE cluster_code='M10b');
DELETE FROM mti_term_subgroup
WHERE cluster_subgroup_id IN (SELECT id FROM cluster_subgroup WHERE cluster_code='M10b');
DELETE FROM cluster_subgroup WHERE cluster_code='M10b';
UPDATE cluster SET status='Data - In Progress' WHERE cluster_code='M10b';
COMMIT;
```

(Restore from `backups/bible_research_backup_20260525_*_M10b-phase6-subgroup-assign.db` for full integrity rollback.)

## SCRIPT

`scripts/_apply_m10b_phase6_subgroup_assign_20260525.py` — resolves the term-level mapping (with per-verse split rules + to.e.vah passage-group parsing) to a flat vc_id → subgroup mapping, writes the resolved JSON, runs pre-checks, applies Ops A/B/C/D in a single transaction, runs post-checks.

---

*Applied 2026-05-25T~10:35Z. Status: COMPLETE.*
