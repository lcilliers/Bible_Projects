# wa-cluster-M10-dir-002-phase6-subgroup-assign-v1-20260523

> Cluster directive — M10 Phase 6 (sub-group structural apply + verse routing)
> Cluster: M10 — Sin, Guilt and Transgression (post-split)
> Date: 2026-05-23
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §9

---

## MOTIVATION

Phase 5 produced a sub-group design with 9 characteristics + 1 BOUNDARY (10 sub-groups total), all within the 40% distribution gate. Source documents:

- Design: [files phase 5/wa-cluster-M10-subgroup-design-v1-20260523.md](files%20phase%205/wa-cluster-M10-subgroup-design-v1-20260523.md)
- Mapping (term-level + split rules): [files phase 5/wa-cluster-M10-subgroup-mapping-v1-20260523.json](files%20phase%205/wa-cluster-M10-subgroup-mapping-v1-20260523.json)
- Resolved (flat vc_id → subgroup_code): [files phase 5/wa-cluster-M10-subgroup-mapping-resolved-v1-20260523.json](files%20phase%205/wa-cluster-M10-subgroup-mapping-resolved-v1-20260523.json) (written by the apply script)

Two CC corrections applied before resolution:
1. **chet H2399** mti_id (126) + est_verses (33) patched into the term-level mapping; routed to M10-B (sin-as-condition).
2. **pa.sha H6586** split rule normalised from prose-only `secondary_verses_rule` to explicit `secondary_verses` list (9 political-revolt references → M10-A secondary).

## SCOPE

### Operation A — INSERT cluster_subgroup rows (10)

| code | label | est. verses |
|---|---|---:|
| M10-A | Sin as committed act | 274 |
| M10-B | Sin as moral condition / state | 339 |
| M10-C | The sinner as moral character | 64 |
| M10-D | Guilt as inner-being state | 97 |
| M10-E | Iniquity as accumulated moral crime | 162 |
| M10-F | Transgression / rebellion as deliberate boundary-crossing | 147 |
| M10-G | Faithlessness / treachery as covenant-breaking sin | 101 |
| M10-H | Perversion / moral corruption as inner inversion | 64 |
| M10-I | Injustice as moral failure of right conduct | 72 |
| M10-BND | Boundary — analytically undecided terms | 5 |

Each row gets `core_description` from §2 of the design document, `sort_order` matching the listing above, `status='active'`, `version='v1'`, `source=DIRECTIVE_ID`.

Distribution: largest sub-group (M10-B) at 339 / 1,325 = **25.6%**, well within the 40% / 530-verse gate.

### Operation B — INSERT mti_term_subgroup rows

For each term in M10 (63 active OWNERs), insert one row per (term, sub-group) it touches:

- Primary placement (`[primary] N verses`) — the sub-group carrying the majority of the term's verses.
- Secondary placement (`[secondary] N verses`) — for the two multi-faceted terms (pa.sha → M10-A secondary; paraptōma → M10-F secondary).
- Empty-corpus BOUNDARY terms (mash.chit / mash.chet / ma.she.chat / cha.loph) attach to M10-BND with `[primary] 0 verses (empty-corpus BOUNDARY term)`.

### Operation C — UPDATE verse_context.cluster_subgroup_id

For all 1,325 active is_relevant vc rows in M10, set `cluster_subgroup_id` to the sub-group ID resolved from the term-level mapping + per-verse split rules.

### Operation D — Cluster status

No-op. `cluster.M10.status` is already `Analysis - In Progress` (Phase 4 advance).

## OUTCOME REQUIRED

- 10 `cluster_subgroup` rows for M10.
- 65 `mti_term_subgroup` rows (63 primary + 2 secondary).
- 1,325 vc rows with `cluster_subgroup_id` set.
- 0 unrouted is_relevant vc rows.

## COMPLETION CONFIRMATION

```sql
SELECT subgroup_code, COUNT(vc.id) AS verses
FROM cluster_subgroup cs
LEFT JOIN verse_context vc ON vc.cluster_subgroup_id = cs.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
WHERE cs.cluster_code='M10' AND COALESCE(cs.delete_flagged,0)=0
GROUP BY subgroup_code ORDER BY subgroup_code;

SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id=vc.mti_term_id
WHERE mt.cluster_code='M10' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL;
-- Should return 0
```

## ROLLBACK

```sql
BEGIN;
UPDATE verse_context SET cluster_subgroup_id=NULL
WHERE cluster_subgroup_id IN (SELECT id FROM cluster_subgroup WHERE cluster_code='M10');
DELETE FROM mti_term_subgroup
WHERE cluster_subgroup_id IN (SELECT id FROM cluster_subgroup WHERE cluster_code='M10');
DELETE FROM cluster_subgroup WHERE cluster_code='M10';
COMMIT;
```

## SCRIPT

`scripts/_apply_m10_phase6_subgroup_assign_20260523.py` — resolves the term-level mapping (with split rules) to a flat vc_id → subgroup mapping, writes the resolved JSON, runs pre-checks, applies Ops A/B/C in a single transaction, runs post-checks.

---

*M10 Phase 6 directive. Ready for execution.*
