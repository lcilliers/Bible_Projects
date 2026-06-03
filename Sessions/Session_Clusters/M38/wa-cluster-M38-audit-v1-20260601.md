# Cluster audit — in-progress clusters

**Generated:** 2026-06-01 (read-only). Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`. Target status: `M38` (1 clusters).
GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. INFO = advisory. INCR = re-submit/clear work for the incremental update.

## M38 — audit verdict **PASS**

- **Cluster status (DB):** `Analysis - In Progress`
- **Outstanding:** 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 1514 | 1514 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 24 | id=21896<br>id=21900<br>id=21913<br>id=21927<br>id=21938<br>id=21961<br>id=21980<br>id=21985<br>id=22004<br>id=22009<br>id=22010<br>id=22025<br>... (+12 more) |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 7 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | PASS | 0 | none |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| A10 | no open Session-D observations (Session D moot) | A | GATE | PASS | 0 |  |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 309/309 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 309/309 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 309/309 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 7 characteristics, 7 char-subgroup links; 7/7 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 7 | char 122 'Eschatological salvation received by faith': 191<br>char 123 'Physical rescue from mortal danger': 189<br>char 124 'Healing wholeness through faith exercised': 189<br>char 125 'Conscience cleansed through atonement received': 189<br>char 126 'Priestly mediation machinery of atonement': 189<br>char 127 'Salvation anticipated and hope sustained': 189<br>char 128 'Ransomed identity gratitude and memory': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 6581 | 6581 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | PASS | 0 | 0 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 13/13 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 0 | 0 findings + 0 flags to adopt into findings |

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

| Cluster | Verdict | GATE fails | New terms (D1) | Unalloc pointers (D2) |
|---|---|--:|--:|--:|
| M38 | PASS | 0 | 0 | 0 |

**PASS 1 · FAIL 0** of 1.

## Consolidated incremental worklist (re-submit / clear / adopt)

| Cluster | Action | Item |
|---|---|---|
| M38 | REVIEW | A2 nonsense/gap synthesis rows (24) |
