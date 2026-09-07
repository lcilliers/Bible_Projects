# Cluster audit — in-progress clusters

**Generated:** 2026-06-01 (read-only). Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`. Target status: `M10c` (1 clusters).
GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. INFO = advisory. INCR = re-submit/clear work for the incremental update.

## M10c — audit verdict **PASS**

- **Cluster status (DB):** `Analysis Complete`
- **Outstanding:** 1 advisory-review (A2)

| ID | Aspect | Sec | Sev | Status | Count | Detail |
|---|---|---|---|---|--:|---|
| A1 | findings present | A | GATE | PASS | 945 | 945 active cluster_finding rows |
| A2 | nonsense/gap synthesis rows | A | INFO | REVIEW | 5 | id=20385<br>id=20412<br>id=20450<br>id=20568<br>id=20571 |
| A3 | every characteristic has findings | A | GATE | PASS | 0 | 4 characteristics all have findings |
| A4 | BOUNDARY sub-group empty | A | GATE | PASS | 0 | no BOUNDARY sub-group |
| A5 | BOUNDARY_DECISION_PENDING resolved | A | GATE | PASS | 0 |  |
| A6 | gating flags resolved (registry→cluster, non-excl) | A | GATE | PASS | 0 | none |
| A7 | no stray Session-B findings | A | GATE | PASS | 0 | 0 pending/open SB findings (term→sub-group) |
| A8 | actionable observations confirmed | A | GATE | PASS | 0 |  |
| A9 | no orphan findings | A | INFO | PASS | 0 | 0 dangling findings |
| B1a | Phase A: verse MEANINGS on every is_relevant (mandatory) | B | GATE | PASS | 0 | 263/263 is_relevant verses have analysis_note |
| B1b | Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster) | B | GATE | PASS | 0 | 263/263 is_relevant verses have keywords |
| B2 | Phase B: is_relevant verses grouped (subgroup+group) | B | STRUCT | PASS | 0 | 263/263 grouped |
| B3 | characteristics table complete (chars + every sub-group linked) | B | GATE | PASS | 0 | 4 characteristics, 5 char-subgroup links; 5/5 non-BOUNDARY sub-groups linked |
| B4 | Phase D: findings per characteristic | B | INFO | PASS | 4 | char 53 'Ritual defilement-state': 189<br>char 54 'Moral-inner defilement-state': 189<br>char 55 'Corporate/covenantal defilement': 189<br>char 56 'Defilement by external spiritual agency': 189 |
| B5 | every active VCG has an anchor verse | B | GATE | PASS | 0 | 0 active VCGs without an anchor |
| B6 | Phase D: citation traceability | B | STRUCT | PASS | 3242 | 3242 finding_citation rows |
| B7 | every anchor verse covered in findings | B | GATE | PASS | 0 | 0 anchor verses not cited in any finding |
| C1 | old-format VCGs dissolved | C | STRUCT | PASS | 0 | 0 active old-format VCGs tied to cluster terms (dissolve at Phase C) |
| C2 | term→sub-group linkage present | C | STRUCT | PASS | 0 | 8/8 live terms linked to a sub-group |
| D1 | new terms to place (cluster_code set, no sub-group) | D | INCR | PASS | 0 | 0 terms to place into a sub-group + analyse |
| D2 | unallocated pointers routed here | D | INCR | PASS | 0 | 0 findings + 0 flags to adopt into findings |

### Corrective actions — dispositions & workings

_source: `wa-cluster-M10c-pointer-dispositions-v1-20260601.json` — v3_0 §10.1 inherited-finding reconciliation + v2_9 §18 disposition vocab; each item evaluated on content, not marker-flipped._

| Item | Action | Evaluation (workings) | Reason |
|---|---|---|---|
| wa_session_b_findings id=55 (DIMENSION_REVIEW) | **set_aside** | Registry-115 (passion) Phase-C structural observation: it noted reg-115 contributed zero desiderative groups and asked Session B to clarify the passion registry's coverage. The term-anchor re-clustering has since dissolved registry-as-clustering-driver and placed reg-115's defilement terms into M10c (defiling passion / moral defilement). The observation is therefore superseded and no longer a standing M10c analytical finding. | Set aside (superseded): registry-level Phase-C dimension note made moot by the term-anchor re-clustering; not M10c analytical content. (Valid ground: out-of-scope/superseded structural note, not a forbidden spiritual-framing reason.) |
| wa_session_research_flags id=364 (SB_FINDING) | **resolve** | G3392 (miaino) at Joh 18:28 names ceremonial ritual-status defilement-avoidance ('not be defiled, but could eat the Passover'). The inner-being content (hypocrisy of ceremonial scrupulousness while plotting unjust execution) is carried by narrative juxtaposition with v.30+, NOT by miaino, which here names the ritual-status mechanism. Per the valid set-aside ground 'the term refers to something other than an inner state (ritual procedure)', the verse-level relevance for the inner-being profile is wrong_face. | Resolved: borderline-retain question closed — Joh 18:28 miaino = ceremonial ritual-status (not an inner-being defilement state); inner-being content is narrative, not term-borne. Verse is wrong_face for the inner-being profile; no standing M10c finding required. |
| cluster_finding (A2 advisory-review) id=20385, 20412, 20450, 20568, 20571 (nonsense/gap heuristic on cluster_synthesis rows) | **review — no action (false positives)** | All five are legitimate cluster_synthesis essays that analytically discuss the cluster's gaps and silences — which is the synthesis layer's actual job (e.g. 'the cluster's combined silence on divine possession reveals a differentiated picture…', 'the four frameworks surface four gap-areas that the verse evidence has not addressed'). The A2 text-match heuristic over-triggered on the words silence / gap-areas / has not addressed. None is a broken or content-empty row. | False positives: substantive cross-characteristic synthesis content, not nonsense. No fix required. (Auditor refinement noted: A2 should exclude finding_status='cluster_synthesis' or tighten the gap-pattern, since discussing analytic gaps is that layer's purpose.) |

---

## Cross-cluster summary

| Cluster | Verdict | GATE fails | New terms (D1) | Unalloc pointers (D2) |
|---|---|--:|--:|--:|
| M10c | PASS | 0 | 0 | 0 |

**PASS 1 · FAIL 0** of 1.

## Consolidated incremental worklist (re-submit / clear / adopt)

| Cluster | Action | Item |
|---|---|---|
| M10c | REVIEW | A2 nonsense/gap synthesis rows (5) |
