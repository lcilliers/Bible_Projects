# Programme Cluster Audit — all started clusters

**Generated:** 2026-06-03 (read-only re-run on the recovered 2026-05-28 DB). Engine: `scripts/audit_cluster_v1_20260601.py`. Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`.

> DB = recovered **2026-05-28** snapshot; the June 1–2 remediation is NOT in this DB, so gate failures here may reflect that gap rather than original analytical defects. See `wa-db-recovery-assessment-20260603.md`.

GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. INFO/REVIEW = advisory. INCR = re-submit/clear work.

**Scope:** 19 started clusters.

## M03 Grief — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **5 GATE-blocking** (A5, B1a, B1b, B3, B7); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 360 | 360 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | FAIL | 28 | id=688 M03-BOUNDARY-G0928G<br>id=689 M03-BOUNDARY-G0928H<br>id=690 M03-BOUNDARY-G0931<br>id=691 M03-BOUNDARY-G2346<br>id=692 M03-BOUNDARY-G4192<br>id=693 M03-BOUNDARY-G4660<br>id=694 M03-BOUNDARY-G4729<br>id=695 M03-BOUNDARY-G4841<br>id=696 M03-BOUNDARY-H1742<br>id=697 M03-BOUNDARY-H2254C<br>id=698 M03-BOUNDARY-H2256M<br>id=699 M03-BOUNDARY-H2470I<br>... (+16 more) |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | PASS | 0 | none |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 18 | 18 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 1 | 681/682 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 682 | 0/682 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 682/682 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 7 char-subgroup links; 7/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 57 'Weeping and tears': 49<br>char 58 'Mourning and lamentation': 31<br>char 59 'Sorrow and inner grief': 36<br>char 60 'Anguish and distress': 44<br>char 61 'Groaning and sighing': 27<br>char 62 'Pain and inner ache': 25<br>char 63 'Bitterness of soul': 25 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1373 | 1373 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 31 | 31 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 78/78 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M03-*disposition*.json` in the cluster folder)._

## M04 Joy — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **5 GATE-blocking** (A6, A7, B1b, B3, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1512 | 1512 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 2 | id=10345<br>id=10365 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 83 | SD_POINTER: 58<br>SB_FINDING: 24<br>PH2_DATA_ERROR: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 77 | 77 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 1116/1116 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 1116 | 0/1116 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 1116/1116 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 17 char-subgroup links; 16/17 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 1 'Exultation': 189<br>char 2 'Joy': 189<br>char 3 'Gladness': 189<br>char 4 'Delight': 189<br>char 5 'Pleasure': 189<br>char 6 'Wonder': 189<br>char 7 'Suffering-Joy': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 8890 | 8890 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 10 | 10 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 58/58 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M04-*disposition*.json` in the cluster folder)._

## M06 Hate — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **7 GATE-blocking** (A4, A6, A7, B1a, B1b, B5, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1516 | 1516 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | FAIL | 60 | BOUNDARY 'Boundary/expression': 56 verses, 4 terms |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 9 | SD_POINTER: 8<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 7 | 7 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 158 | 158 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 280 | 151/431 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 431 | 0/431 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 2 | 429/431 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 7 characteristics, 7 char-subgroup links; 7/7 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 84 'Hatred': 189<br>char 85 'Contempt': 189<br>char 86 'Abhorrence': 189<br>char 87 'Cruelty/Ruthlessness': 189<br>char 88 'Reproach': 189<br>char 89 'Hostility/Enmity': 189<br>char 90 'Malice': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 3 | 3 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 2070 | 2070 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 4 | 4 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 51 | 51 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 34/34 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M06-*disposition*.json` in the cluster folder)._

## M07 Shame — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **5 GATE-blocking** (A6, A7, B1b, B3, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1323 | 1323 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 4 | id=11579<br>id=11580<br>id=11581<br>id=11688 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 6 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 27 | SD_POINTER: 27 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 41 | 41 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 359/359 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 359 | 0/359 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 359/359 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 6 characteristics, 8 char-subgroup links; 8/9 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 6 | char 8 'Shame as experienced inner state': 189<br>char 9 'Humiliation as enforced abasement': 189<br>char 10 'Dishonour as relational worth-denial': 189<br>char 11 'Shamefulness as moral-evaluative judgment': 189<br>char 12 'Shame produced by contempt and rejection': 189<br>char 13 'Innocence as structural counter to shame': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 4179 | 4179 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 4 | 4 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 33/33 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M07-*disposition*.json` in the cluster folder)._

## M08 Pride — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **4 GATE-blocking** (A6, A7, B1b, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1134 | 1134 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 6 | id=12635<br>id=12641<br>id=12663<br>id=12755<br>id=12757<br>id=12822 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 5 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 11 | SD_POINTER: 10<br>PH2_DATA_ERROR: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 11 | 11 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 293/293 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 293 | 0/293 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 293/293 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 5 characteristics, 8 char-subgroup links; 8/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 5 | char 14 'Arrogant self-elevation': 189<br>char 15 'Presumptuous defiance': 189<br>char 16 'Boasting and self-display': 189<br>char 17 'Vain conceit': 189<br>char 18 'Pride of power and position': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 5645 | 5645 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 1 | 1 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 46/46 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M08-*disposition*.json` in the cluster folder)._

## M09 Humility — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **4 GATE-blocking** (A6, A7, B1b, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1323 | 1323 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 7 | id=13999<br>id=14032<br>id=14052<br>id=14080<br>id=14101<br>id=14125<br>id=14145 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 6 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 66 | SB_FINDING: 56<br>SD_POINTER: 10 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 186 | 186 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 97/97 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 97 | 0/97 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 97/97 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 6 characteristics, 8 char-subgroup links; 8/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 6 | char 19 'Humility': 189<br>char 20 'Submission': 189<br>char 21 'Contrition': 189<br>char 22 'Meekness and gentleness': 189<br>char 23 'Dignity': 189<br>char 24 'Willing-heartedness': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1604 | 1604 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 22 | 22 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 17/17 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M09-*disposition*.json` in the cluster folder)._

## M10 Sin — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **5 GATE-blocking** (A6, A7, A8, B3, B7)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 4158 | 4158 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 22 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 28 | SD_POINTER: 26<br>PH2_DATA_ERROR: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 44 | 44 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | FAIL | 23 | id=29 CROSS_CLUSTER_HANDOFF [open]<br>id=169 SELF_CHECK_OBSERVATION [open]<br>id=170 SELF_CHECK_OBSERVATION [open]<br>id=171 SELF_CHECK_OBSERVATION [open]<br>id=172 SELF_CHECK_OBSERVATION [open]<br>id=173 SELF_CHECK_OBSERVATION [open]<br>id=174 SELF_CHECK_OBSERVATION [open]<br>id=175 SELF_CHECK_OBSERVATION [open]<br>id=176 SELF_CHECK_OBSERVATION [open]<br>id=177 SELF_CHECK_OBSERVATION [open]<br>id=178 SELF_CHECK_OBSERVATION [open]<br>id=179 SELF_CHECK_OBSERVATION [open]<br>... (+11 more) |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 1320/1320 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 1320/1320 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 1320/1320 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 22 characteristics, 22 char-subgroup links; 22/23 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 22 | char 25 'Wilful sinning': 189<br>char 26 'Unintentional sinning': 189<br>char 27 'Confession': 189<br>char 28 'Conscience suppression': 189<br>char 29 'Refusal to repent': 189<br>char 30 'Habitual defection': 189<br>char 31 'Contagious sin': 189<br>char 32 'Political revolt': 189<br>char 33 'Sinful speech': 189<br>char 34 'Specialised sinful mechanisms': 189<br>char 35 'Sin as universal condition': 189<br>char 36 'Sin as enslaving power': 189<br>... (+10 more) |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 23656 | 23656 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 3 | 3 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 63/63 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M10-*disposition*.json` in the cluster folder)._

## M10b Wickedness — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **3 GATE-blocking** (A6, A7, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1323 | 1323 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 4 | id=19474<br>id=19485<br>id=19506<br>id=19626 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 6 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 2 | SD_POINTER: 2 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 2 | 2 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 515/515 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 515/515 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 515/515 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 6 characteristics, 6 char-subgroup links; 6/6 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 6 | char 47 'Wickedness as settled person-identity': 189<br>char 48 'Evil as constitutional inner nature': 189<br>char 49 'Abomination — divine revulsion on moral character': 189<br>char 50 'Idolatrous abomination': 189<br>char 51 'Iniquity as active inner scheming and evil generation': 189<br>char 52 'Evil expressed through speech': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 7784 | 7784 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 2 | 2 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 17/17 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_source: `wa-cluster-M10b-pointer-dispositions-v1-20260601.json` — v3_0 §10.1 inherited-finding reconciliation + v2_9 §18 disposition vocab; each item evaluated on content, not marker-flipped. A7 applied; A2 review-only; B7 surfaced as analytical residual (no DB change here)._

| Item | Action | Evaluation (workings) | Reason |
|---|---|---|---|
| wa_session_b_findings id=101 (DIMENSION_REVIEW (DIM-57-001, registry 57 'evil')) | **set_aside** | DIM-57-001 is a Phase-C dimension note about the OLD registry model: it observes that registry 57 (evil) is the programme's largest (46 groups) and 'functions partly as a container for inner-being framing particles (kol H3605, mi H4310, na H4994, zamam H2161)', and asks Session B to assess whether that breadth is analytically productive. Its own cluster_link is M15,T2 — it surfaces under M10b only because a reg-57 term sits in an M10b sub-group (term to sub-group is non-exclusive). The concern it raises — registry-57 breadth and framing-particle noise — is exactly what the term-anchor re-clustering resolved: registry-57-as-a-unit is no longer an analytical object; its terms are distributed to clusters by characteristic and the framing particles fall to set-aside/T2. The note is therefore superseded and is not a standing analytical finding for M10b (or for M15/T2). | Set aside (superseded): registry-scope DIMENSION_REVIEW about the pre-re-clustering registry model; made moot by the term-anchor re-clustering. Same class as M10c finding 55. Valid ground: superseded structural/methodological note, not a forbidden spiritual-framing reason. Set aside globally (status field) — correct, since it is superseded for every cluster it was linked to, not M10b-specific. |
| cluster_finding (A2 advisory-review) id=19474, 19485, 19506, 19626 (nonsense/gap heuristic on cluster_synthesis rows) | **review — no action (false positives)** | All four are legitimate cluster_synthesis essays that analytically discuss the cluster's silences and gaps — the synthesis layer's actual job (e.g. 'the cluster is collectively silent on explicit spirit-level location… none of the six characteristics uses ruach vocabulary', 'the five frameworks collectively surface one shared gap: the developmental origins of the six inner-evil forms'). The A2 text-match heuristic over-triggered on silent / gap / has-not-addressed. None is a broken or content-empty row. | False positives: substantive cross-characteristic synthesis content, not nonsense. No fix required. (Same auditor refinement noted under M10c: A2 should exclude finding_status='cluster_synthesis' or tighten the gap-pattern.) |
| verse_context (B7 anchor coverage — analytical residual) id=Hos 10:13 (H7562 resha), 2Ch 24:7 (H4849 mirshaath) (anchor verses not cited in any M10b finding) | **surface — analytical residual (no DB change here; routes to Phase-D analytical handler)** | Both are anchors of VCG M10b-A-VCG-11 / sub-group 156 (M10b-A, 'the wicked person — settled inner orientation of wickedness'), characteristic 47 (seq 1, 'Wickedness as settled person-identity'), and both are genuinely, strongly relevant (is_relevant=1): Hos 10:13 'wickedness is the inward soil that produces injustice and lies… self-trust and reliance on strength rather than God cultivated an inner field of moral corruption'; 2Ch 24:7 (Athaliah, 'that wicked woman') 'a woman whose inner character is defined as wicked had channeled that disposition into desecrating sacred space… wickedness expressed as religious violation'. Neither is cited in any of the ~190 char-47 findings (or anywhere cluster-wide); the citation extractor has already run, so this is not a citation-extract gap. So the analysis designated two valid anchors but no finding actually uses them — a genuine Phase-D coverage gap, not a mechanical-citation matter. | Do NOT fabricate a citation (the extractor re-derives finding_citation from finding text; a citation not backed by text would be deleted on the next run). Correct resolution is ANALYTICAL and needs the researcher's call: (a) extend/author the relevant char-47 'settled person-identity' finding to use these two exemplars (preferred — both genuinely evidence the characteristic), or (b) confirm de-anchor (is_anchor=0, keep is_relevant=1) if the VCG's findings legitimately rest on other exemplars. M10b stays OPEN on this single gate item until resolved. |

## M10c Defilement — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **2 GATE-blocking** (A6, A7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 945 | 945 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 5 | id=20385<br>id=20412<br>id=20450<br>id=20568<br>id=20571 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 4 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 1 | SB_FINDING: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 1 | 1 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 263/263 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 263/263 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 263/263 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 4 characteristics, 5 char-subgroup links; 5/5 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 4 | char 53 'Ritual defilement-state': 189<br>char 54 'Moral-inner defilement-state': 189<br>char 55 'Corporate/covenantal defilement': 189<br>char 56 'Defilement by external spiritual agency': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 4765 | 4765 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | PASS | 0 | 0 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 8/8 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_source: `wa-cluster-M10c-pointer-dispositions-v1-20260601.json` — v3_0 §10.1 inherited-finding reconciliation + v2_9 §18 disposition vocab; each item evaluated on content, not marker-flipped._

| Item | Action | Evaluation (workings) | Reason |
|---|---|---|---|
| wa_session_b_findings id=55 (DIMENSION_REVIEW) | **set_aside** | Registry-115 (passion) Phase-C structural observation: it noted reg-115 contributed zero desiderative groups and asked Session B to clarify the passion registry's coverage. The term-anchor re-clustering has since dissolved registry-as-clustering-driver and placed reg-115's defilement terms into M10c (defiling passion / moral defilement). The observation is therefore superseded and no longer a standing M10c analytical finding. | Set aside (superseded): registry-level Phase-C dimension note made moot by the term-anchor re-clustering; not M10c analytical content. (Valid ground: out-of-scope/superseded structural note, not a forbidden spiritual-framing reason.) |
| wa_session_research_flags id=364 (SB_FINDING) | **resolve** | G3392 (miaino) at Joh 18:28 names ceremonial ritual-status defilement-avoidance ('not be defiled, but could eat the Passover'). The inner-being content (hypocrisy of ceremonial scrupulousness while plotting unjust execution) is carried by narrative juxtaposition with v.30+, NOT by miaino, which here names the ritual-status mechanism. Per the valid set-aside ground 'the term refers to something other than an inner state (ritual procedure)', the verse-level relevance for the inner-being profile is wrong_face. | Resolved: borderline-retain question closed — Joh 18:28 miaino = ceremonial ritual-status (not an inner-being defilement state); inner-being content is narrative, not term-borne. Verse is wrong_face for the inner-being profile; no standing M10c finding required. |
| cluster_finding (A2 advisory-review) id=20385, 20412, 20450, 20568, 20571 (nonsense/gap heuristic on cluster_synthesis rows) | **review — no action (false positives)** | All five are legitimate cluster_synthesis essays that analytically discuss the cluster's gaps and silences — which is the synthesis layer's actual job (e.g. 'the cluster's combined silence on divine possession reveals a differentiated picture…', 'the four frameworks surface four gap-areas that the verse evidence has not addressed'). The A2 text-match heuristic over-triggered on the words silence / gap-areas / has not addressed. None is a broken or content-empty row. | False positives: substantive cross-characteristic synthesis content, not nonsense. No fix required. (Auditor refinement noted: A2 should exclude finding_status='cluster_synthesis' or tighten the gap-pattern, since discussing analytic gaps is that layer's purpose.) |

## M15 Wisdom — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **7 GATE-blocking** (A4, A6, A7, B1a, B1b, B5, B7); 1 structural (C1)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1724 | 1724 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 8 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | FAIL | 27 | BOUNDARY 'Functional, supporting, and cluster-reassignment candidates': 14 verses, 13 terms |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 36 | SD_POINTER: 29<br>PH2_DATA_ERROR: 5<br>SB_FINDING: 2 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 35 | 35 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 545 | 1099/1644 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 1644 | 0/1644 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 1644/1644 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 8 characteristics, 8 char-subgroup links; 8/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 8 | char 91 'Logos — the word as inner-being engagement': 189<br>char 92 'Wisdom as holistic inner character and orientation': 189<br>char 93 'Understanding as inner perceptive faculty': 189<br>char 94 'Knowledge as inner content and covenantal knowing': 189<br>char 95 'Discernment and practical judgment': 189<br>char 96 'Deliberative planning, counsel, and purposive intent': 189<br>char 97 'Meditative and reflective inner activity': 189<br>char 98 'Inner thought-content — the mind's formed thoughts': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 3 | 3 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 2602 | 2602 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 4 | 4 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 3 | 3 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 85/85 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M15-*disposition*.json` in the cluster folder)._

## M26 Righteousness — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **7 GATE-blocking** (A6, A7, B1a, B1b, B3, B5, B7); 2 structural (B2, C1); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 677 | 677 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 4 | id=3635<br>id=3894<br>id=3903<br>id=4270 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 8 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 40 | SD_POINTER: 37<br>SB_FINDING: 1<br>PH2_DATA_ERROR: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 49 | 49 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 869 | 0/869 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 869 | 0/869 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 5 | 864/869 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 8 characteristics, 8 char-subgroup links; 8/9 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 8 | char 103 'God Righteousness': 64<br>char 104 'Human Righteousness — State of being right': 80<br>char 105 'Moral Uprightness: Inner Disposition of Straightness': 61<br>char 106 'Justification: Declaring or Making Righteous': 74<br>char 107 'Avenging Justice: Retribution for Wrongdoing': 68<br>char 108 'Condemnation: Judicial Sentence Against': 67<br>char 109 'Moral Reckoning: Evaluative Faculty of Worth': 69<br>char 110 'Structural Opposites: Wickedness and Injustice': 60 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 5 | 5 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1721 | 1721 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 44 | 44 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 56 | 56 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 1 | 38/39 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 1 | 1 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M26-*disposition*.json` in the cluster folder)._

## M39 Blessing — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **6 GATE-blocking** (A6, A7, B1a, B1b, B3, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 384 | 384 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 2 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 166 | SD_POINTER: 106<br>SB_FINDING: 59<br>PH2_DATA_ERROR: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 219 | 219 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 3 | 3 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 717 | 1/718 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 718 | 0/718 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 4 | 714/718 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 2 characteristics, 2 char-subgroup links; 2/3 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 2 | char 111 'Blessing and Grace': 187<br>char 112 'Goodness': 187 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1208 | 1208 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 16 | 16 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 34 | 34 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 1 | 15/16 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 1 | 1 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M39-*disposition*.json` in the cluster folder)._

## M46 Abundance — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed`
- **Outstanding:** **6 GATE-blocking** (A6, A7, B1a, B1b, B5, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 381 | 381 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 4 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 31 | SD_POINTER: 30<br>PH2_DATA_ERROR: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 38 | 38 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 10 | 10 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 196 | 1/197 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 197 | 0/197 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 1 | 196/197 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 4 characteristics, 4 char-subgroup links; 4/4 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 4 | char 113 'Inner closure': 88<br>char 114 'Hardness and insatiability': 69<br>char 115 'The ordering of character and wealth': 73<br>char 116 'The inner life beyond material circumstance': 90 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 9 | 9 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1492 | 1492 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 6 | 6 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 34 | 34 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 22/22 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M46-*disposition*.json` in the cluster folder)._

## M01 Fear — verdict **FAIL**

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
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 2612 | 2612 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 34 | 34 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 2 | 2 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 2 | 81/83 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 2 | 2 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M01-*disposition*.json` in the cluster folder)._

## M02 Anger — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed (Terms Added)`
- **Outstanding:** **5 GATE-blocking** (A5, B1b, B3, B5, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 389 | 389 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 6 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | FAIL | 4 | id=682 M02-BOUNDARY-G0485<br>id=683 M02-BOUNDARY-G2042<br>id=684 M02-BOUNDARY-G2200<br>id=685 M02-BOUNDARY-H3708B |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | PASS | 0 | none |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 17 | 17 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 645/645 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 645 | 0/645 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 4 | 641/645 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 6 characteristics, 6 char-subgroup links; 6/7 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 6 | char 71 'Divine Wrath as Judicial Force': 59<br>char 72 'Burning Rage and Inner Heat': 127<br>char 73 'Indignation and Moral Displeasure': 39<br>char 74 'Provocation — Anger Aroused': 35<br>char 75 'Jealousy, Zeal and Possessive Passion': 38<br>char 76 'Strife, Quarrel and Contentious Anger': 18 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 1 | 1 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1443 | 1443 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 19 | 19 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 2 | 2 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 1 | 43/44 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 1 | 1 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M02-*disposition*.json` in the cluster folder)._

## M20 Doubt — verdict **FAIL**

- **Cluster status (DB):** `Analysis Completed (Terms Added)`
- **Outstanding:** **4 GATE-blocking** (A6, A7, B1a, B1b); 2 structural (B2, C1); 2 advisory-review (A2, A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 525 | 525 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 1 | id=6459 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 4 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 39 | SD_POINTER: 32<br>PH2_DATA_ERROR: 3<br>PH2_THEOLOGICAL_DEPTH_REQUIRED: 1<br>PH2_EXEGETICAL_STUDY_REQUIRED: 1<br>PH2_ESCHATOLOGICAL_STUDY_REQUIRED: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 39 | 39 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 9 | 9 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 56 | 11/67 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 67 | 0/67 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 11 | 56/67 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 4 characteristics, 4 char-subgroup links; 4/4 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 4 | char 99 'Anxiety and Worry': 125<br>char 100 'Despair and Hopelessness': 110<br>char 101 'Discouragement and Loss of Heart': 127<br>char 102 'Doubt and Indecision': 120 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 775 | 775 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | PASS | 0 | 0 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 12 | 12 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 3 | 12/15 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 3 | 3 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M20-*disposition*.json` in the cluster folder)._

## M05 Love — verdict **FAIL**

- **Cluster status (DB):** `Ready for re-analysis`
- **Outstanding:** **7 GATE-blocking** (A6, A7, B1a, B1b, B3, B5, B7); 2 structural (B2, C1); 2 advisory-review (A2, A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1517 | 1517 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 2 | id=3010<br>id=3012 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 183 | SD_POINTER: 121<br>SB_FINDING: 58<br>PH2_DATA_ERROR: 4 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 338 | 338 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 122 | 122 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 1264 | 166/1430 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 1430 | 0/1430 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 197 | 1233/1430 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 7 char-subgroup links; 7/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 77 'Love': 189<br>char 78 'Compassion': 189<br>char 79 'Mercy': 189<br>char 80 'Kindness and Goodness': 189<br>char 81 'Gentleness': 189<br>char 82 'Comfort and Encouragement': 189<br>char 83 'Fellowship and Participation': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 1 | 1 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1356 | 1356 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 52 | 52 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 123 | 123 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 2 | 86/88 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 2 | 2 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M05-*disposition*.json` in the cluster folder)._

## M11 Repentance — verdict **FAIL**

- **Cluster status (DB):** `Structurally Ready`
- **Outstanding:** **5 GATE-blocking** (A1, A3, A6, A10, B7); 2 structural (B6, C2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | FAIL | 0 | 0 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | FAIL | 5 | char 117 'Atonement' has 0 findings<br>char 118 'Divine forgiveness' has 0 findings<br>char 119 'Release (broader sense)' has 0 findings<br>char 120 'Repentance and turning' has 0 findings<br>char 121 'Reconciliation' has 0 findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 70 | SD_POINTER: 49<br>SB_FINDING: 21 |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | FAIL | 9 | id=251 M11 multi-characteristic framing under v3_0<br>id=252 Cross-cluster characteristic-legs (forgive-text scatter)<br>id=253 kip.per/sa.lach internal arc (M11-A ↔ M11-B canonical pair)<br>id=254 Christic surrender → cosmic reconciliation arc (M11-A-VCG-10 ↔ M11-E-VCG-01)<br>id=255 Negative pole runs across M11-A, M11-B, M11-C<br>id=256 M03 cross-register flag for divine grief (na.cham)<br>id=257 G0863G afiēmi (leave) cross-register flag — M30/M29 primary<br>id=258 G0863I afiēmi (permit) cross-register flag — M29 primary<br>id=259 H5749A ud — marginal STAYS structural-opposite |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 288/288 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 288/288 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 288/288 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 5 characteristics, 5 char-subgroup links; 5/5 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 5 | char 117 'Atonement': 0<br>char 118 'Divine forgiveness': 0<br>char 119 'Release (broader sense)': 0<br>char 120 'Repentance and turning': 0<br>char 121 'Reconciliation': 0 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | FAIL | 0 | 0 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 42 | 42 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | FAIL | 15 | 0/15 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 15 | 15 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M11-*disposition*.json` in the cluster folder)._

## M38 Salvation — verdict **FAIL**

- **Cluster status (DB):** `Structurally Ready`
- **Outstanding:** **5 GATE-blocking** (A1, A3, A6, A10, B7); 2 structural (B6, C2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | FAIL | 0 | 0 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | FAIL | 7 | char 122 'Eschatological salvation received by faith' has 0 findings<br>char 123 'Physical rescue from mortal danger' has 0 findings<br>char 124 'Healing wholeness through faith exercised' has 0 findings<br>char 125 'Conscience cleansed through atonement received' has 0 findings<br>char 126 'Priestly mediation machinery of atonement' has 0 findings<br>char 127 'Salvation anticipated and hope sustained' has 0 findings<br>char 128 'Ransomed identity gratitude and memory' has 0 findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 27 | SD_POINTER: 27 |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | FAIL | 17 | id=260 G1431 dōrea cross-register flag<br>id=261 G1434 dōrēma cross-register flag<br>id=262 G2433 hilaskomai cross-register flag<br>id=263 G2434 hilasmos cross-register flag<br>id=264 G2435 hilastērios cross-register flag<br>id=265 G2436 hileōs cross-register flag<br>id=266 G4990 sōtēr cross-register flag<br>id=267 G4991 soteria cross-register flag<br>id=268 G4992 sōtērion cross-register flag<br>id=269 H3444 ye.shu.ah cross-register flag<br>id=270 H6299 pa.dah cross-register flag<br>id=271 M38 cluster is multi-characteristic under v3_0<br>... (+5 more) |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 309/309 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 309/309 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 309/309 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 7 characteristics, 7 char-subgroup links; 7/7 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 122 'Eschatological salvation received by faith': 0<br>char 123 'Physical rescue from mortal danger': 0<br>char 124 'Healing wholeness through faith exercised': 0<br>char 125 'Conscience cleansed through atonement received': 0<br>char 126 'Priestly mediation machinery of atonement': 0<br>char 127 'Salvation anticipated and hope sustained': 0<br>char 128 'Ransomed identity gratitude and memory': 0 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | FAIL | 0 | 0 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 45 | 45 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | FAIL | 13 | 0/13 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 13 | 13 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | ERR:no such column: cluster_linkERR:no such column: cluster_link | ERR:no such column: cluster_link findings + ERR:no such column: cluster_link flags to adopt into findings |

### Corrective actions — dispositions & workings

_source: `wa-cluster-M38-pointer-dispositions-v1-20260602.json` — REVIEW REQUIRED: evaluate each item on its full _text (v3_0 §10.1 / v2_9 §18); set action (set_aside|resolve|fold|review) + evaluation + reason. Underscore-prefixed fields are read-only evidence. Set top-level "approved": true after researcher review to let the orchestrator apply._

| Item | Action | Evaluation (workings) | Reason |
|---|---|---|---|
| wa_session_research_flags id=155 () | **** |  |  |
| wa_session_research_flags id=170 () | **** |  |  |
| wa_session_research_flags id=171 () | **** |  |  |
| wa_session_research_flags id=172 () | **** |  |  |
| wa_session_research_flags id=173 () | **** |  |  |
| wa_session_research_flags id=246 () | **** |  |  |
| wa_session_research_flags id=247 () | **** |  |  |
| wa_session_research_flags id=248 () | **** |  |  |
| wa_session_research_flags id=249 () | **** |  |  |
| wa_session_research_flags id=250 () | **** |  |  |
| wa_session_research_flags id=251 () | **** |  |  |
| wa_session_research_flags id=252 () | **** |  |  |
| wa_session_research_flags id=253 () | **** |  |  |
| wa_session_research_flags id=254 () | **** |  |  |
| wa_session_research_flags id=255 () | **** |  |  |
| wa_session_research_flags id=256 () | **** |  |  |
| wa_session_research_flags id=257 () | **** |  |  |
| wa_session_research_flags id=258 () | **** |  |  |
| wa_session_research_flags id=259 () | **** |  |  |
| wa_session_research_flags id=627 () | **** |  |  |
| wa_session_research_flags id=628 () | **** |  |  |
| wa_session_research_flags id=629 () | **** |  |  |
| wa_session_research_flags id=630 () | **** |  |  |
| wa_session_research_flags id=631 () | **** |  |  |
| wa_session_b_findings id=33 () | **** |  |  |
| wa_session_b_findings id=107 () | **** |  |  |
| wa_session_b_findings id=127 () | **** |  |  |
| wa_session_b_findings id=128 () | **** |  |  |
| wa_session_b_findings id=144 () | **** |  |  |
| wa_session_b_findings id=146 () | **** |  |  |
| wa_session_b_findings id=147 () | **** |  |  |
| wa_session_b_findings id=148 () | **** |  |  |
| wa_session_b_findings id=158 () | **** |  |  |
| wa_session_b_findings id=1593 () | **** |  |  |
| wa_session_b_findings id=1594 () | **** |  |  |
| wa_session_b_findings id=1595 () | **** |  |  |
| wa_session_b_findings id=1596 () | **** |  |  |
| wa_session_b_findings id=1597 () | **** |  |  |
| wa_session_b_findings id=1598 () | **** |  |  |
| wa_session_b_findings id=1599 () | **** |  |  |
| wa_session_b_findings id=1600 () | **** |  |  |
| wa_session_b_findings id=1601 () | **** |  |  |
| wa_session_b_findings id=1602 () | **** |  |  |
| wa_session_b_findings id=1603 () | **** |  |  |
| wa_session_b_findings id=1604 () | **** |  |  |
| wa_session_b_findings id=1605 () | **** |  |  |
| wa_session_b_findings id=1606 () | **** |  |  |
| wa_session_b_findings id=1607 () | **** |  |  |
| wa_session_b_findings id=1608 () | **** |  |  |
| wa_session_b_findings id=1609 () | **** |  |  |
| wa_session_b_findings id=1610 () | **** |  |  |
| wa_session_b_findings id=1611 () | **** |  |  |
| wa_session_b_findings id=1612 () | **** |  |  |
| wa_session_b_findings id=1613 () | **** |  |  |
| wa_session_b_findings id=1614 () | **** |  |  |
| wa_session_b_findings id=1615 () | **** |  |  |
| wa_session_b_findings id=1616 () | **** |  |  |
| wa_session_b_findings id=1617 () | **** |  |  |
| wa_session_b_findings id=1618 () | **** |  |  |
| wa_session_b_findings id=1619 () | **** |  |  |
| wa_session_b_findings id=1620 () | **** |  |  |

---

## Cross-cluster summary

| Cluster | Name | DB status | Verdict | GATE | STRUCT | REVIEW | New terms (D1) | Unalloc ptrs (D2) |
|---|---|---|---|--:|--:|--:|--:|--:|
| M03 | Grief | Analysis Completed | FAIL | 5 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M04 | Joy | Analysis Completed | FAIL | 5 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M06 | Hate | Analysis Completed | FAIL | 7 | 2 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M07 | Shame | Analysis Completed | FAIL | 5 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M08 | Pride | Analysis Completed | FAIL | 4 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M09 | Humility | Analysis Completed | FAIL | 4 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M10 | Sin | Analysis Completed | FAIL | 5 | 0 | 0 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M10b | Wickedness | Analysis Completed | FAIL | 3 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M10c | Defilement | Analysis Completed | FAIL | 2 | 0 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M15 | Wisdom | Analysis Completed | FAIL | 7 | 1 | 0 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M26 | Righteousness | Analysis Completed | FAIL | 7 | 2 | 1 | 1 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M39 | Blessing | Analysis Completed | FAIL | 6 | 2 | 1 | 1 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M46 | Abundance | Analysis Completed | FAIL | 6 | 2 | 1 | 0 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M01 | Fear | Analysis Completed (Terms Added) | FAIL | 4 | 2 | 2 | 2 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M02 | Anger | Analysis Completed (Terms Added) | FAIL | 5 | 2 | 1 | 1 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M20 | Doubt | Analysis Completed (Terms Added) | FAIL | 4 | 2 | 2 | 3 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M05 | Love | Ready for re-analysis | FAIL | 7 | 2 | 2 | 2 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M11 | Repentance | Structurally Ready | FAIL | 5 | 2 | 0 | 15 | ERR:no such column: cluster_linkERR:no such column: cluster_link |
| M38 | Salvation | Structurally Ready | FAIL | 5 | 2 | 0 | 13 | ERR:no such column: cluster_linkERR:no such column: cluster_link |

**PASS 0 · FAIL 19** of 19 started clusters.

## Consolidated worklist (re-submit / clear / adopt / review)

| Cluster | Action | Item |
|---|---|---|
| M03 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (28) |
| M03 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (1) |
| M03 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (682) |
| M03 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M03 | RE-SUBMIT | B7 every anchor verse covered in findings (31) |
| M03 | REVIEW | A9 no orphan findings (18) |
| M04 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (83) |
| M04 | CLEAR | A7 no stray Session-B findings (77) |
| M04 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (1116) |
| M04 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M04 | RE-SUBMIT | B7 every anchor verse covered in findings (10) |
| M04 | REVIEW | A2 nonsense/gap synthesis rows (2) |
| M06 | CLEAR | A4 BOUNDARY sub-group empty (60) |
| M06 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (9) |
| M06 | CLEAR | A7 no stray Session-B findings (7) |
| M06 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (280) |
| M06 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (431) |
| M06 | RE-SUBMIT | B5 every active VCG has an anchor verse (3) |
| M06 | RE-SUBMIT | B7 every anchor verse covered in findings (4) |
| M06 | REVIEW | A9 no orphan findings (158) |
| M06 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (2) |
| M06 | RE-SUBMIT | C1 old-format VCGs dissolved (51) |
| M07 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (27) |
| M07 | CLEAR | A7 no stray Session-B findings (41) |
| M07 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (359) |
| M07 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M07 | RE-SUBMIT | B7 every anchor verse covered in findings (4) |
| M07 | REVIEW | A2 nonsense/gap synthesis rows (4) |
| M08 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (11) |
| M08 | CLEAR | A7 no stray Session-B findings (11) |
| M08 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (293) |
| M08 | RE-SUBMIT | B7 every anchor verse covered in findings (1) |
| M08 | REVIEW | A2 nonsense/gap synthesis rows (6) |
| M09 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (66) |
| M09 | CLEAR | A7 no stray Session-B findings (186) |
| M09 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (97) |
| M09 | RE-SUBMIT | B7 every anchor verse covered in findings (22) |
| M09 | REVIEW | A2 nonsense/gap synthesis rows (7) |
| M10 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (28) |
| M10 | CLEAR | A7 no stray Session-B findings (44) |
| M10 | CLEAR | A8 actionable observations confirmed (23) |
| M10 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M10 | RE-SUBMIT | B7 every anchor verse covered in findings (3) |
| M10b | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (2) |
| M10b | CLEAR | A7 no stray Session-B findings (2) |
| M10b | RE-SUBMIT | B7 every anchor verse covered in findings (2) |
| M10b | REVIEW | A2 nonsense/gap synthesis rows (4) |
| M10c | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (1) |
| M10c | CLEAR | A7 no stray Session-B findings (1) |
| M10c | REVIEW | A2 nonsense/gap synthesis rows (5) |
| M15 | CLEAR | A4 BOUNDARY sub-group empty (27) |
| M15 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (36) |
| M15 | CLEAR | A7 no stray Session-B findings (35) |
| M15 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (545) |
| M15 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (1644) |
| M15 | RE-SUBMIT | B5 every active VCG has an anchor verse (3) |
| M15 | RE-SUBMIT | B7 every anchor verse covered in findings (4) |
| M15 | RE-SUBMIT | C1 old-format VCGs dissolved (3) |
| M26 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (40) |
| M26 | CLEAR | A7 no stray Session-B findings (49) |
| M26 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (869) |
| M26 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (869) |
| M26 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M26 | RE-SUBMIT | B5 every active VCG has an anchor verse (5) |
| M26 | RE-SUBMIT | B7 every anchor verse covered in findings (44) |
| M26 | REVIEW | A2 nonsense/gap synthesis rows (4) |
| M26 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (5) |
| M26 | RE-SUBMIT | C1 old-format VCGs dissolved (56) |
| M26 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (1) |
| M39 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (166) |
| M39 | CLEAR | A7 no stray Session-B findings (219) |
| M39 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (717) |
| M39 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (718) |
| M39 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M39 | RE-SUBMIT | B7 every anchor verse covered in findings (16) |
| M39 | REVIEW | A9 no orphan findings (3) |
| M39 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (4) |
| M39 | RE-SUBMIT | C1 old-format VCGs dissolved (34) |
| M39 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (1) |
| M46 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (31) |
| M46 | CLEAR | A7 no stray Session-B findings (38) |
| M46 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (196) |
| M46 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (197) |
| M46 | RE-SUBMIT | B5 every active VCG has an anchor verse (9) |
| M46 | RE-SUBMIT | B7 every anchor verse covered in findings (6) |
| M46 | REVIEW | A9 no orphan findings (10) |
| M46 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (1) |
| M46 | RE-SUBMIT | C1 old-format VCGs dissolved (34) |
| M01 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (7) |
| M01 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (945) |
| M01 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M01 | RE-SUBMIT | B7 every anchor verse covered in findings (34) |
| M01 | REVIEW | A2 nonsense/gap synthesis rows (1) |
| M01 | REVIEW | A9 no orphan findings (10) |
| M01 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (4) |
| M01 | RE-SUBMIT | C1 old-format VCGs dissolved (2) |
| M01 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (2) |
| M02 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (4) |
| M02 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (645) |
| M02 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M02 | RE-SUBMIT | B5 every active VCG has an anchor verse (1) |
| M02 | RE-SUBMIT | B7 every anchor verse covered in findings (19) |
| M02 | REVIEW | A9 no orphan findings (17) |
| M02 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (4) |
| M02 | RE-SUBMIT | C1 old-format VCGs dissolved (2) |
| M02 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (1) |
| M20 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (39) |
| M20 | CLEAR | A7 no stray Session-B findings (39) |
| M20 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (56) |
| M20 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (67) |
| M20 | REVIEW | A2 nonsense/gap synthesis rows (1) |
| M20 | REVIEW | A9 no orphan findings (9) |
| M20 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (11) |
| M20 | RE-SUBMIT | C1 old-format VCGs dissolved (12) |
| M20 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (3) |
| M05 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (183) |
| M05 | CLEAR | A7 no stray Session-B findings (338) |
| M05 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (1264) |
| M05 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (1430) |
| M05 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M05 | RE-SUBMIT | B5 every active VCG has an anchor verse (1) |
| M05 | RE-SUBMIT | B7 every anchor verse covered in findings (52) |
| M05 | REVIEW | A2 nonsense/gap synthesis rows (2) |
| M05 | REVIEW | A9 no orphan findings (122) |
| M05 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (197) |
| M05 | RE-SUBMIT | C1 old-format VCGs dissolved (123) |
| M05 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (2) |
| M11 | RE-SUBMIT | A1 findings present (0) |
| M11 | RE-SUBMIT | A3 every characteristic has findings (5) |
| M11 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (70) |
| M11 | RE-SUBMIT | A10 no open Session-D observations (Session D moot) (9) |
| M11 | RE-SUBMIT | B7 every anchor verse covered in findings (42) |
| M11 | RE-SUBMIT | B6 Phase D: citation traceability (0) |
| M11 | RE-SUBMIT | C2 term→sub-group linkage present (15) |
| M11 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (15) |
| M38 | RE-SUBMIT | A1 findings present (0) |
| M38 | RE-SUBMIT | A3 every characteristic has findings (7) |
| M38 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (27) |
| M38 | RE-SUBMIT | A10 no open Session-D observations (Session D moot) (17) |
| M38 | RE-SUBMIT | B7 every anchor verse covered in findings (45) |
| M38 | RE-SUBMIT | B6 Phase D: citation traceability (0) |
| M38 | RE-SUBMIT | C2 term→sub-group linkage present (13) |
| M38 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (13) |

---
*Read-only. Generated by `scripts/generate_full_cluster_audit_v1_20260603.py` (reuses `audit_cluster_v1_20260601.audit_cluster`).*
