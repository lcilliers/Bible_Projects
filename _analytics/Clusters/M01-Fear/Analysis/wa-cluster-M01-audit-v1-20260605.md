# Cluster audit — in-progress clusters

**Generated:** 2026-06-01 (read-only). Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`. Target status: `M01` (1 clusters).
GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. INFO = advisory. INCR = re-submit/clear work for the incremental update.

## M01 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed (Terms Added)`
- **Outstanding:** **4 GATE-blocking** (A5, B1b, B3, B7); 2 structural (B2, C1); 2 advisory-review (A2, A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 805 | 805 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 1 | id=8104 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | FAIL | 7 | id=671 M01-BOUNDARY-G2285<br>id=672 M01-BOUNDARY-H2189<br>id=674 M01-BOUNDARY-H4867<br>id=676 M01-BOUNDARY-H6178<br>id=679 M01-BOUNDARY-H8047G<br>id=680 M01-BOUNDARY-H8312<br>id=681 M01-BOUNDARY-H8539 |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | PASS | 0 | none |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 10 | 10 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 945/945 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 945 | 0/945 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 4 | 941/945 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 7 char-subgroup links; 7/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 64 'Reverential Fear / Fear of God as Governing Orientation': 141<br>char 65 'Acute Fear and Alarm': 111<br>char 66 'Terror as Overwhelming Force': 64<br>char 67 'Dismay and Inner Collapse': 88<br>char 68 'Trembling / Fear Made Somatic': 76<br>char 69 'Anticipatory Dread and Anxiety': 80<br>char 70 'Timidity and Cowardly Shrinking': 88 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1618 | 1618 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 34 | 34 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 2 | 2 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 2 | 81/83 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 2 | 2 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 1 | 0 findings + 1 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M01-*disposition*.json` in the cluster folder)._

---

## Cross-cluster summary

| Cluster | Verdict | GATE fails | New terms (D1) | Unalloc pointers (D2) |
|---|---|--:|--:|--:|
| M01 | FAIL | 4 | 2 | 1 |

**PASS 0 · FAIL 1** of 1.

## Consolidated incremental worklist (re-submit / clear / adopt)

| Cluster | Action | Item |
|---|---|---|
| M01 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (7) |
| M01 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (945) |
| M01 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M01 | RE-SUBMIT | B7 every anchor verse covered in findings (34) |
| M01 | REVIEW | A2 nonsense/gap synthesis rows (1) |
| M01 | REVIEW | A9 no orphan findings (10) |
| M01 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (4) |
| M01 | RE-SUBMIT | C1 old-format VCGs dissolved (2) |
| M01 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (2) |
| M01 | ADOPT | D2 unallocated pointers routed here (1) |
