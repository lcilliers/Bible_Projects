# Analysis-Complete validation report

**Mode:** APPLY (resets performed)
**Target statuses:** Analysis Complete, Analysis Completed, Analysis Completed (Terms Added) — 17 clusters
**Gate:** Workflow/methodology/wa-cluster-readiness-gate-design.md §3 (two-condition gate)
**Reset target on FAIL:** `Analysis - In Progress`

> HARD checks gate completion (a single HARD failure → cluster is not validly complete → reset). ADVISORY checks are reported for review but do not by themselves demote.

## Per-cluster detail

### M01 — current `Analysis Completed (Terms Added)` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 1 | id=8104: The science framework surfaces three modest gaps: (1) the dissociative dimension of M01-D's freeze-collapse (Porges); (2 |
| C2 BOUNDARY_DECISION_PENDING flags | Condition 2 | HARD | 7 | id=671 M01-BOUNDARY-G2285<br>id=672 M01-BOUNDARY-H2189<br>id=674 M01-BOUNDARY-H4867<br>id=676 M01-BOUNDARY-H6178<br>id=679 M01-BOUNDARY-H8047G<br>id=680 M01-BOUNDARY-H8312<br>id=681 M01-BOUNDARY-H8539<br>(link: flag_label prefix) |
| C2 orphan findings | Condition 2 | ADVISORY | 10 | 10 non-synthesis findings with no characteristic AND no sub-group (dangling). |

### M02 — current `Analysis Completed (Terms Added)` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 BOUNDARY_DECISION_PENDING flags | Condition 2 | HARD | 4 | id=682 M02-BOUNDARY-G0485<br>id=683 M02-BOUNDARY-G2042<br>id=684 M02-BOUNDARY-G2200<br>id=685 M02-BOUNDARY-H3708B<br>(link: flag_label prefix) |
| C2 orphan findings | Condition 2 | ADVISORY | 17 | 17 non-synthesis findings with no characteristic AND no sub-group (dangling). |

### M03 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 BOUNDARY_DECISION_PENDING flags | Condition 2 | HARD | 28 | id=688 M03-BOUNDARY-G0928G<br>id=689 M03-BOUNDARY-G0928H<br>id=690 M03-BOUNDARY-G0931<br>id=691 M03-BOUNDARY-G2346<br>id=692 M03-BOUNDARY-G4192<br>id=693 M03-BOUNDARY-G4660<br>id=694 M03-BOUNDARY-G4729<br>id=695 M03-BOUNDARY-G4841<br>id=696 M03-BOUNDARY-H1742<br>id=697 M03-BOUNDARY-H2254C<br>id=698 M03-BOUNDARY-H2256M<br>id=699 M03-BOUNDARY-H2470I<br>id=700 M03-BOUNDARY-H4157<br>id=701 M03-BOUNDARY-H4620<br>id=702 M03-BOUNDARY-H4689<br>(link: flag_label prefix) |
| C2 orphan findings | Condition 2 | ADVISORY | 18 | 18 non-synthesis findings with no characteristic AND no sub-group (dangling). |

### M04 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 2 | id=10345: **[CLUSTER]** G — Full dimensional sharing data is not yet available; Session D is required for the complete cross-chara<br>id=10365: **[CLUSTER]** E — The frameworks surface two cluster-level gaps: (1) **Habituation and anti-habituation** — positive psy |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 83 | SD_POINTER: 58<br>SB_FINDING: 24<br>PH2_DATA_ERROR: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 77 | 77 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M06 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 active BOUNDARY members | Condition 2 | HARD | 65 | BOUNDARY sub-group 'Boundary/expression' still has 56 verses, 4 terms, 5 VCGs (cluster-direct link). |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 9 | SD_POINTER: 8<br>PH2_CROSS_REGISTRY_REQUIRED: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 7 | 7 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |
| C2 orphan findings | Condition 2 | ADVISORY | 158 | 158 non-synthesis findings with no characteristic AND no sub-group (dangling). |

### M07 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 4 | id=11579: **[CLUSTER]** S — All six characteristics are silent on the creative faculty. M07's shame-field does not engage imaginat<br>id=11580: **[CLUSTER]** S — All six characteristics are silent on the creative faculty. M07's shame-field does not engage imaginat<br>id=11581: **[CLUSTER]** S — All six characteristics are silent on the creative faculty. M07's shame-field does not engage imaginat<br>id=11688: **[CLUSTER]** G — The human science frameworks surface five developmental and neurological gaps across the cluster that  |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 27 | SD_POINTER: 27<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 41 | 41 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M08 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 6 | id=12635: **[CLUSTER]** E — Scripture does not attribute any of the five M08 characteristics to God. The cluster-level finding is <br>id=12641: **[CLUSTER]** E — All five characteristics are confirmed exclusively creaturely. The cluster comparison surfaces one qua<br>id=12663: **[CLUSTER]** E — Yes, consistently across all five characteristics. The immediate experience of each M08 characteristic<br>id=12755: **[CLUSTER]** G — All five characteristics are gaps on adversarial spiritual activity, with the partial exception of CHA<br>id=12757: **[CLUSTER]** S — Angelic ministry is universally absent from M08's evidence across all five characteristics. Adversaria<br>id=12822: **[CLUSTER]** E — The science extract surfaces two cross-characteristic gaps that benefit from further verse investigati |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 11 | SD_POINTER: 10<br>PH2_DATA_ERROR: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 11 | 11 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M09 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 7 | id=13999: **[CLUSTER]** E — Constitutional movement is evidenced for all six characteristics. No characteristic in the cluster is <br>id=14032: **[CLUSTER]** E — The relational pattern reveals that M09 is constitutively a relational cluster — its characteristics c<br>id=14052: **[CLUSTER]** E — All six enable and deepen moral evaluation; none bypass or impair it. Humility (CHAR-1) enables accura<br>id=14080: **[CLUSTER]** E — Five of six characteristics are silent on direct spiritual-beings interface in their verse corpora. Hu<br>id=14101: **[CLUSTER]** S — T2.8 found no constitutional bodily deposit for any of the six characteristics. T5.7 is accordingly cl<br>id=14125: **[CLUSTER]** E — Dimensional sharing analysis is available from within-session evidence (T6.7.1 and T6.7.2). Programme-<br>id=14145: **[CLUSTER]** E — The science frameworks surface three cluster-wide gaps. *Developmental origins*: none of the six chara |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 66 | SB_FINDING: 56<br>SD_POINTER: 10<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 186 | 186 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M10 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 28 | SD_POINTER: 26<br>PH2_DATA_ERROR: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 44 | 44 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |
| C2 unconfirmed actionable observations | Condition 2 | HARD | 23 | id=29 CROSS_CLUSTER_HANDOFF [open] M10c pickup note: H2256D che.vel Mic 2:10 (Phase 8.5 set-aside)<br>id=169 SELF_CHECK_OBSERVATION [open] M10 Char 1 Phase 9 Self-check meta-observations<br>id=170 SELF_CHECK_OBSERVATION [open] M10 Char 10 Phase 9 Self-check meta-observations<br>id=171 SELF_CHECK_OBSERVATION [open] M10 Char 11 Phase 9 Self-check meta-observations<br>id=172 SELF_CHECK_OBSERVATION [open] M10 Char 12 Phase 9 Self-check meta-observations<br>id=173 SELF_CHECK_OBSERVATION [open] M10 Char 13 Phase 9 Self-check meta-observations<br>id=174 SELF_CHECK_OBSERVATION [open] M10 Char 14 Phase 9 Self-check meta-observations<br>id=175 SELF_CHECK_OBSERVATION [open] M10 Char 15 Phase 9 Self-check meta-observations<br>id=176 SELF_CHECK_OBSERVATION [open] M10 Char 16 Phase 9 Self-check meta-observations<br>id=177 SELF_CHECK_OBSERVATION [open] M10 Char 17 Phase 9 Self-check meta-observations<br>id=178 SELF_CHECK_OBSERVATION [open] M10 Char 18 Phase 9 Self-check meta-observations<br>id=179 SELF_CHECK_OBSERVATION [open] M10 Char 19 Phase 9 Self-check meta-observations<br>id=180 SELF_CHECK_OBSERVATION [open] M10 Char 2 Phase 9 Self-check meta-observations<br>id=181 SELF_CHECK_OBSERVATION [open] M10 Char 20 Phase 9 Self-check meta-observations<br>id=182 SELF_CHECK_OBSERVATION [open] M10 Char 21 Phase 9 Self-check meta-observations |

### M10b — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 4 | id=19474: **[CLUSTER]** S — The cluster is collectively silent on explicit spirit-level location. None of the six characteristics <br>id=19485: **[CLUSTER]** E — Mind-location across the cluster reveals the cognitive faculty's corruption in three distinct modes: (<br>id=19506: **[CLUSTER]** E — The cluster reveals a consistent impairment-pattern across all six characteristics for the moral-spiri<br>id=19626: **[CLUSTER]** E — The cluster's five frameworks collectively surface one shared gap: the developmental origins of the si |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 2 | SD_POINTER: 2<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 2 | 2 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M10c — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 5 | id=20385: **[CLUSTER]** E — The cluster's combined silence on divine possession reveals a differentiated picture of the characteri<br>id=20412: **[CLUSTER]** E — Yes, across all four characteristics the sustained effect differs from the immediate response, but the<br>id=20450: **[CLUSTER]** E — All four characteristics engage the perceptive faculty, but through distinct modes that together map t<br>id=20568: **[CLUSTER]** E — The four most useful frameworks together reveal the M10c domain's multi-disciplinary breadth. Characte<br>id=20571: **[CLUSTER]** G — The four frameworks surface four gap-areas that the verse evidence has not addressed. Characteristic 1 |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 1 | SB_FINDING: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 1 | 1 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M15 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 active BOUNDARY members | Condition 2 | HARD | 28 | BOUNDARY sub-group 'Functional, supporting, and cluster-reassignment candidates' still has 14 verses, 13 terms, 1 VCGs (cluster-direct link). |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 36 | SD_POINTER: 29<br>PH2_DATA_ERROR: 5<br>SB_FINDING: 2<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 35 | 35 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M20 — current `Analysis Completed (Terms Added)` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 1 | id=6459: Shared verse anchors are likely across multiple sub-groups — however, confirmation of what functions as a primary anchor |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 39 | SD_POINTER: 32<br>PH2_DATA_ERROR: 3<br>PH2_THEOLOGICAL_DEPTH_REQUIRED: 1<br>PH2_EXEGETICAL_STUDY_REQUIRED: 1<br>PH2_ESCHATOLOGICAL_STUDY_REQUIRED: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 39 | 39 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |
| C2 orphan findings | Condition 2 | ADVISORY | 9 | 9 non-synthesis findings with no characteristic AND no sub-group (dangling). |

### M26 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 4 | id=3635: **[CLUSTER]** The pattern of silence in T0.1.3 reveals a consistent structure: the divine-to-human direction is source-t<br>id=3894: **[CLUSTER — T1.8.1 through T1.8.3]** G — CC should run the dimension vocabulary query against the current database (`wa<br>id=3903: **[CLUSTER — T2.1]** S. The cluster is entirely silent on spirit-level location. This is a significant finding: across 9<br>id=4270: **[CLUSTER]** E. Yes — several terms in M26 are NT-specific or extremely rare before the NT:
- **autokatakritos (G0843)* |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 40 | SD_POINTER: 37<br>SB_FINDING: 1<br>PH2_DATA_ERROR: 1<br>PH2_CROSS_REGISTRY_REQUIRED: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 49 | 49 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |

### M38 — current `Analysis Complete` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C1 synthesis-as-gap (heuristic) | Condition 1 | ADVISORY | 24 | id=21896: **[CLUSTER]** E — Across the seven characteristics, the verse evidence collectively identifies a coherent cluster of pur<br>id=21900: **[CLUSTER]** E — The cluster finding across all seven characteristics is a consistent pattern of *dual structure*: none<br>id=21913: **[CLUSTER]** E — When enabling conditions are compared across all seven characteristics, the cluster reveals a consiste<br>id=21927: **[CLUSTER]** E — Every characteristic evidences at least some zones of silence on immediate response, and the pattern o<br>id=21938: **[CLUSTER]** S — All seven characteristics are silent on constitutional bodily deposit, DNA-level consequence, or gener<br>id=21961: **[CLUSTER]** S — Across the seven characteristics comprising Cluster M38, spirit-level (pneuma/rûaḥ) location is the ex<br>id=21980: **[CLUSTER]** E — The cluster shows moral evaluation enabled or deepened across all seven characteristics, with bypassin<br>id=21985: **[CLUSTER]** E — The comparative pattern across seven characteristics reveals a consistent structural principle: cognit<br>id=22004: **[CLUSTER]** E — The cluster reveals that enabling and blocking conditions for person-to-person reception are unevenly <br>id=22009: **[CLUSTER]** E — This question generates the sharpest cluster-level finding: across every characteristic where the evid |
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 27 | SD_POINTER: 27<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |

### M39 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 166 | SD_POINTER: 106<br>SB_FINDING: 59<br>PH2_DATA_ERROR: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 219 | 219 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |
| C2 orphan findings | Condition 2 | ADVISORY | 3 | 3 non-synthesis findings with no characteristic AND no sub-group (dangling). |

### M46 — current `Analysis Completed` → **FAIL**

| Check | Condition | Severity | Count | Detail |
|---|---|---|---:|---|
| C2 unresolved gating flags (SB/SD/PH2) | Condition 2 | HARD | 31 | SD_POINTER: 30<br>PH2_DATA_ERROR: 1<br>(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session) |
| C2 stray Session-B findings | Condition 2 | HARD | 38 | 38 stray Session-B findings (status pending/open; link: term→sub-group→cluster). |
| C2 orphan findings | Condition 2 | ADVISORY | 10 | 10 non-synthesis findings with no characteristic AND no sub-group (dangling). |

---

## Cross-cluster summary

- Clusters validated: **17** — PASS **0**, FAIL **17**.
- Failing on Condition 1 (findings): **0** — none
- Failing on Condition 2 (leftovers): **17** — M01, M02, M03, M04, M06, M07, M08, M09, M10, M10b, M10c, M15, M20, M26, M38, M39, M46
- **Reset to `Analysis - In Progress`:** 17 — M01, M02, M03, M04, M06, M07, M08, M09, M10, M10b, M10c, M15, M20, M26, M38, M39, M46

### Failures by type

| Failure type (HARD) | # clusters | Clusters |
|---|---:|---|
| C2 unresolved gating flags (SB/SD/PH2) | 14 | M04, M06, M07, M08, M09, M10, M10b, M10c, M15, M20, M26, M38, M39, M46 |
| C2 stray Session-B findings | 13 | M04, M06, M07, M08, M09, M10, M10b, M10c, M15, M20, M26, M39, M46 |
| C2 BOUNDARY_DECISION_PENDING flags | 3 | M01, M02, M03 |
| C2 active BOUNDARY members | 2 | M06, M15 |
| C2 unconfirmed actionable observations | 1 | M10 |
