# Cluster audit — in-progress clusters

**Generated:** 2026-06-01 (read-only). Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`. Target status: `Analysis - In Progress` (13 clusters).
GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. INFO = advisory. INCR = re-submit/clear work for the incremental update.

## M01 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **5 GATE-blocking** (A5, B1a, B1b, B3, B7); 2 structural (B2, C1); 2 advisory-review (A2, A9)

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
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 1 | 945/946 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 946 | 0/946 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 5 | 941/946 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 7 char-subgroup links; 7/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 64 'Reverential Fear / Fear of God as Governing Orientation': 141<br>char 65 'Acute Fear and Alarm': 111<br>char 66 'Terror as Overwhelming Force': 64<br>char 67 'Dismay and Inner Collapse': 88<br>char 68 'Trembling / Fear Made Somatic': 76<br>char 69 'Anticipatory Dread and Anxiety': 80<br>char 70 'Timidity and Cowardly Shrinking': 88 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 2612 | 2612 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 34 | 34 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 2 | 2 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 8 | 81/89 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 8 | 8 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 1 | 0 findings + 1 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M01-*disposition*.json` in the cluster folder)._

## M02 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
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
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 2 | 43/45 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 2 | 2 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 0 | 0 findings + 0 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M02-*disposition*.json` in the cluster folder)._

## M03 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **5 GATE-blocking** (A5, B1a, B1b, B3, B7); 2 structural (B2, C1); 1 advisory-review (A9)

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
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 24 | 681/705 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 705 | 0/705 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 15 | 690/705 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 7 char-subgroup links; 7/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 57 'Weeping and tears': 49<br>char 58 'Mourning and lamentation': 31<br>char 59 'Sorrow and inner grief': 36<br>char 60 'Anguish and distress': 44<br>char 61 'Groaning and sighing': 27<br>char 62 'Pain and inner ache': 25<br>char 63 'Bitterness of soul': 25 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1373 | 1373 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 31 | 31 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 1 | 1 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 4 | 78/82 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 4 | 4 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 3 | 0 findings + 3 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M03-*disposition*.json` in the cluster folder)._

## M04 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **6 GATE-blocking** (A6, A7, B1a, B1b, B3, B7); 2 structural (B2, C1); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1512 | 1512 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 2 | id=10345<br>id=10365 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 67 | SD_POINTER: 43<br>SB_FINDING: 24 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 66 | 66 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 2 | 1116/1118 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 1118 | 0/1118 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 2 | 1116/1118 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 7 characteristics, 17 char-subgroup links; 16/17 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 1 'Exultation': 189<br>char 2 'Joy': 189<br>char 3 'Gladness': 189<br>char 4 'Delight': 189<br>char 5 'Pleasure': 189<br>char 6 'Wonder': 189<br>char 7 'Suffering-Joy': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 8890 | 8890 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 10 | 10 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 1 | 1 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 3 | 58/61 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 3 | 3 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 178 | 0 findings + 178 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M04-*disposition*.json` in the cluster folder)._

## M06 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **7 GATE-blocking** (A4, A6, A7, B1a, B1b, B5, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1516 | 1516 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | FAIL | 60 | BOUNDARY 'Boundary/expression': 56 verses, 4 terms |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 3 | SD_POINTER: 2<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 5 | 5 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 158 | 158 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 441 | 151/592 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 592 | 0/592 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 163 | 429/592 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 7 characteristics, 7 char-subgroup links; 7/7 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 84 'Hatred': 189<br>char 85 'Contempt': 189<br>char 86 'Abhorrence': 189<br>char 87 'Cruelty/Ruthlessness': 189<br>char 88 'Reproach': 189<br>char 89 'Hostility/Enmity': 189<br>char 90 'Malice': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 3 | 3 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 2070 | 2070 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 4 | 4 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 61 | 61 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 11 | 34/45 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 11 | 11 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 1 | 0 findings + 1 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M06-*disposition*.json` in the cluster folder)._

## M07 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **5 GATE-blocking** (A6, A7, B1b, B3, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1323 | 1323 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 4 | id=11579<br>id=11580<br>id=11581<br>id=11688 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 6 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 24 | SD_POINTER: 24 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 36 | 36 pending/open SB findings (term→sub-group) |
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
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 1 | 33/34 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 1 | 1 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 1 | 0 findings + 1 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M07-*disposition*.json` in the cluster folder)._

## M09 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **4 GATE-blocking** (A6, A7, B1b, B7); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1323 | 1323 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 7 | id=13999<br>id=14032<br>id=14052<br>id=14080<br>id=14101<br>id=14125<br>id=14145 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 6 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 52 | SB_FINDING: 47<br>SD_POINTER: 5 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 181 | 181 pending/open SB findings (term→sub-group) |
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
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 1 | 17/18 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 1 | 1 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 0 | 0 findings + 0 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M09-*disposition*.json` in the cluster folder)._

## M10 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **5 GATE-blocking** (A6, A7, A8, B3, B7)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 4158 | 4158 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 22 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 4 | SD_POINTER: 2<br>PH2_DATA_ERROR: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 12 | 12 pending/open SB findings (term→sub-group) |
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
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 1 | 63/64 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 1 | 1 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 2 | 0 findings + 2 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M10-*disposition*.json` in the cluster folder)._

## M15 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **7 GATE-blocking** (A4, A6, A7, B1a, B1b, B5, B7); 2 structural (B2, C1)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1724 | 1724 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 8 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | FAIL | 27 | BOUNDARY 'Functional, supporting, and cluster-reassignment candidates': 14 verses, 13 terms |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 19 | SD_POINTER: 11<br>SB_FINDING: 2<br>PH2_DATA_ERROR: 2<br>PH2_THEOLOGICAL_DEPTH_REQUIRED: 1<br>PH2_EXEGETICAL_STUDY_REQUIRED: 1<br>PH2_ESCHATOLOGICAL_STUDY_REQUIRED: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 26 | 26 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 607 | 1099/1706 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 1706 | 0/1706 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 52 | 1654/1706 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 8 characteristics, 8 char-subgroup links; 8/8 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 8 | char 91 'Logos — the word as inner-being engagement': 189<br>char 92 'Wisdom as holistic inner character and orientation': 189<br>char 93 'Understanding as inner perceptive faculty': 189<br>char 94 'Knowledge as inner content and covenantal knowing': 189<br>char 95 'Discernment and practical judgment': 189<br>char 96 'Deliberative planning, counsel, and purposive intent': 189<br>char 97 'Meditative and reflective inner activity': 189<br>char 98 'Inner thought-content — the mind's formed thoughts': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 3 | 3 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 2602 | 2602 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 4 | 4 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 11 | 11 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 10 | 85/95 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 10 | 10 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 5 | 0 findings + 5 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M15-*disposition*.json` in the cluster folder)._

## M20 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **3 GATE-blocking** (A6, A7, B1b); 1 structural (B2); 2 advisory-review (A2, A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 525 | 525 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 1 | id=6459 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 4 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 34 | SD_POINTER: 30<br>PH2_THEOLOGICAL_DEPTH_REQUIRED: 1<br>PH2_EXEGETICAL_STUDY_REQUIRED: 1<br>PH2_ESCHATOLOGICAL_STUDY_REQUIRED: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 39 | 39 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 9 | 9 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 72/72 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 11 | 61/72 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 15 | 57/72 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 4 characteristics, 4 char-subgroup links; 4/4 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 4 | char 99 'Anxiety and Worry': 125<br>char 100 'Despair and Hopelessness': 110<br>char 101 'Discouragement and Loss of Heart': 127<br>char 102 'Doubt and Indecision': 120 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 775 | 775 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | PASS | 0 | 0 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 7 | 12/19 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 7 | 7 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 2 | 0 findings + 2 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M20-*disposition*.json` in the cluster folder)._

## M26 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **7 GATE-blocking** (A6, A7, B1a, B1b, B3, B5, B7); 2 structural (B2, C1); 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 677 | 677 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 4 | id=3635<br>id=3894<br>id=3903<br>id=4270 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 8 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 29 | SD_POINTER: 26<br>SB_FINDING: 1<br>PH2_DATA_ERROR: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 46 | 46 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 1167 | 0/1167 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 1167 | 0/1167 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 302 | 865/1167 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 8 characteristics, 8 char-subgroup links; 8/9 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 8 | char 103 'God Righteousness': 64<br>char 104 'Human Righteousness — State of being right': 80<br>char 105 'Moral Uprightness: Inner Disposition of Straightness': 61<br>char 106 'Justification: Declaring or Making Righteous': 74<br>char 107 'Avenging Justice: Retribution for Wrongdoing': 68<br>char 108 'Condemnation: Judicial Sentence Against': 67<br>char 109 'Moral Reckoning: Evaluative Faculty of Worth': 69<br>char 110 'Structural Opposites: Wickedness and Injustice': 60 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 5 | 5 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1721 | 1721 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 44 | 44 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 56 | 56 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 10 | 38/48 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 10 | 10 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 3 | 0 findings + 3 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M26-*disposition*.json` in the cluster folder)._

## M39 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **6 GATE-blocking** (A6, A7, B1a, B1b, B3, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 384 | 384 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 2 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 120 | SD_POINTER: 66<br>SB_FINDING: 54 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 180 | 180 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 3 | 3 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 730 | 1/731 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 731 | 0/731 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 17 | 714/731 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | FAIL | 1 | 2 characteristics, 2 char-subgroup links; 2/3 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 2 | char 111 'Blessing and Grace': 187<br>char 112 'Goodness': 187 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1208 | 1208 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 16 | 16 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 35 | 35 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 3 | 15/18 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 3 | 3 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 22 | 0 findings + 22 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M39-*disposition*.json` in the cluster folder)._

## M46 — audit verdict **FAIL**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** **6 GATE-blocking** (A6, A7, B1a, B1b, B5, B7); 2 structural (B2, C1); 1 advisory-review (A9)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 381 | 381 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | PASS | 0 |  |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 4 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | FAIL | 21 | SD_POINTER: 21 |
| A7 | no stray Session-B findings | A | GATE | FAIL | 31 | 31 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | REVIEW | 10 | 10 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | FAIL | 278 | 1/279 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | FAIL | 279 | 0/279 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | FAIL | 83 | 196/279 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 4 characteristics, 4 char-subgroup links; 4/4 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 4 | char 113 'Inner closure': 88<br>char 114 'Hardness and insatiability': 69<br>char 115 'The ordering of character and wealth': 73<br>char 116 'The inner life beyond material circumstance': 90 |
| B5 | every active VCG has an anchor verse | B | GATE | FAIL | 9 | 9 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 1492 | 1492 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | FAIL | 6 | 6 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | FAIL | 34 | 34 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 3 | 22/25 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 3 | 3 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 10 | 0 findings + 10 flags to adopt into findings |

### Corrective actions — dispositions & workings

_None recorded yet (no `wa-cluster-M46-*disposition*.json` in the cluster folder)._

---

## Cross-cluster summary

| Cluster | Verdict | GATE fails | New terms (D1) | Unalloc pointers (D2) |
|---|---|--:|--:|--:|
| M01 | FAIL | 5 | 8 | 1 |
| M02 | FAIL | 5 | 2 | 0 |
| M03 | FAIL | 5 | 4 | 3 |
| M04 | FAIL | 6 | 3 | 178 |
| M06 | FAIL | 7 | 11 | 1 |
| M07 | FAIL | 5 | 1 | 1 |
| M09 | FAIL | 4 | 1 | 0 |
| M10 | FAIL | 5 | 1 | 2 |
| M15 | FAIL | 7 | 10 | 5 |
| M20 | FAIL | 3 | 7 | 2 |
| M26 | FAIL | 7 | 10 | 3 |
| M39 | FAIL | 6 | 3 | 22 |
| M46 | FAIL | 6 | 3 | 10 |

**PASS 0 · FAIL 13** of 13.

## Consolidated incremental worklist (re-submit / clear / adopt)

| Cluster | Action | Item |
|---|---|---|
| M01 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (7) |
| M01 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (1) |
| M01 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (946) |
| M01 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M01 | RE-SUBMIT | B7 every anchor verse covered in findings (34) |
| M01 | REVIEW | A2 nonsense/gap synthesis rows (1) |
| M01 | REVIEW | A9 no orphan findings (10) |
| M01 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (5) |
| M01 | RE-SUBMIT | C1 old-format VCGs dissolved (2) |
| M01 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (8) |
| M01 | ADOPT | D2 unallocated pointers routed here (1) |
| M02 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (4) |
| M02 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (645) |
| M02 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M02 | RE-SUBMIT | B5 every active VCG has an anchor verse (1) |
| M02 | RE-SUBMIT | B7 every anchor verse covered in findings (19) |
| M02 | REVIEW | A9 no orphan findings (17) |
| M02 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (4) |
| M02 | RE-SUBMIT | C1 old-format VCGs dissolved (2) |
| M02 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (2) |
| M03 | CLEAR | A5 BOUNDARY_DECISION_PENDING resolved (28) |
| M03 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (24) |
| M03 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (705) |
| M03 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M03 | RE-SUBMIT | B7 every anchor verse covered in findings (31) |
| M03 | REVIEW | A9 no orphan findings (18) |
| M03 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (15) |
| M03 | RE-SUBMIT | C1 old-format VCGs dissolved (1) |
| M03 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (4) |
| M03 | ADOPT | D2 unallocated pointers routed here (3) |
| M04 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (67) |
| M04 | CLEAR | A7 no stray Session-B findings (66) |
| M04 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (2) |
| M04 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (1118) |
| M04 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M04 | RE-SUBMIT | B7 every anchor verse covered in findings (10) |
| M04 | REVIEW | A2 nonsense/gap synthesis rows (2) |
| M04 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (2) |
| M04 | RE-SUBMIT | C1 old-format VCGs dissolved (1) |
| M04 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (3) |
| M04 | ADOPT | D2 unallocated pointers routed here (178) |
| M06 | CLEAR | A4 BOUNDARY sub-group empty (60) |
| M06 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (3) |
| M06 | CLEAR | A7 no stray Session-B findings (5) |
| M06 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (441) |
| M06 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (592) |
| M06 | RE-SUBMIT | B5 every active VCG has an anchor verse (3) |
| M06 | RE-SUBMIT | B7 every anchor verse covered in findings (4) |
| M06 | REVIEW | A9 no orphan findings (158) |
| M06 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (163) |
| M06 | RE-SUBMIT | C1 old-format VCGs dissolved (61) |
| M06 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (11) |
| M06 | ADOPT | D2 unallocated pointers routed here (1) |
| M07 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (24) |
| M07 | CLEAR | A7 no stray Session-B findings (36) |
| M07 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (359) |
| M07 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M07 | RE-SUBMIT | B7 every anchor verse covered in findings (4) |
| M07 | REVIEW | A2 nonsense/gap synthesis rows (4) |
| M07 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (1) |
| M07 | ADOPT | D2 unallocated pointers routed here (1) |
| M09 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (52) |
| M09 | CLEAR | A7 no stray Session-B findings (181) |
| M09 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (97) |
| M09 | RE-SUBMIT | B7 every anchor verse covered in findings (22) |
| M09 | REVIEW | A2 nonsense/gap synthesis rows (7) |
| M09 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (1) |
| M10 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (4) |
| M10 | CLEAR | A7 no stray Session-B findings (12) |
| M10 | CLEAR | A8 actionable observations confirmed (23) |
| M10 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M10 | RE-SUBMIT | B7 every anchor verse covered in findings (3) |
| M10 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (1) |
| M10 | ADOPT | D2 unallocated pointers routed here (2) |
| M15 | CLEAR | A4 BOUNDARY sub-group empty (27) |
| M15 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (19) |
| M15 | CLEAR | A7 no stray Session-B findings (26) |
| M15 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (607) |
| M15 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (1706) |
| M15 | RE-SUBMIT | B5 every active VCG has an anchor verse (3) |
| M15 | RE-SUBMIT | B7 every anchor verse covered in findings (4) |
| M15 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (52) |
| M15 | RE-SUBMIT | C1 old-format VCGs dissolved (11) |
| M15 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (10) |
| M15 | ADOPT | D2 unallocated pointers routed here (5) |
| M20 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (34) |
| M20 | CLEAR | A7 no stray Session-B findings (39) |
| M20 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (11) |
| M20 | REVIEW | A2 nonsense/gap synthesis rows (1) |
| M20 | REVIEW | A9 no orphan findings (9) |
| M20 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (15) |
| M20 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (7) |
| M20 | ADOPT | D2 unallocated pointers routed here (2) |
| M26 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (29) |
| M26 | CLEAR | A7 no stray Session-B findings (46) |
| M26 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (1167) |
| M26 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (1167) |
| M26 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M26 | RE-SUBMIT | B5 every active VCG has an anchor verse (5) |
| M26 | RE-SUBMIT | B7 every anchor verse covered in findings (44) |
| M26 | REVIEW | A2 nonsense/gap synthesis rows (4) |
| M26 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (302) |
| M26 | RE-SUBMIT | C1 old-format VCGs dissolved (56) |
| M26 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (10) |
| M26 | ADOPT | D2 unallocated pointers routed here (3) |
| M39 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (120) |
| M39 | CLEAR | A7 no stray Session-B findings (180) |
| M39 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (730) |
| M39 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (731) |
| M39 | RE-SUBMIT | B3 characteristics table complete (chars + every sub-group linked) (1) |
| M39 | RE-SUBMIT | B7 every anchor verse covered in findings (16) |
| M39 | REVIEW | A9 no orphan findings (3) |
| M39 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (17) |
| M39 | RE-SUBMIT | C1 old-format VCGs dissolved (35) |
| M39 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (3) |
| M39 | ADOPT | D2 unallocated pointers routed here (22) |
| M46 | CLEAR | A6 gating flags resolved (registry→cluster, non-excl) (21) |
| M46 | CLEAR | A7 no stray Session-B findings (31) |
| M46 | RE-SUBMIT | B1a Phase A: verse MEANINGS on every is_relevant (mandatory) (278) |
| M46 | RE-SUBMIT | B1b Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) (279) |
| M46 | RE-SUBMIT | B5 every active VCG has an anchor verse (9) |
| M46 | RE-SUBMIT | B7 every anchor verse covered in findings (6) |
| M46 | REVIEW | A9 no orphan findings (10) |
| M46 | RE-SUBMIT | B2 Phase B: is_relevant verses grouped (subgroup+group) (83) |
| M46 | RE-SUBMIT | C1 old-format VCGs dissolved (34) |
| M46 | RE-SUBMIT | D1 new terms to place (cluster_code set, no sub-group) (3) |
| M46 | ADOPT | D2 unallocated pointers routed here (10) |
