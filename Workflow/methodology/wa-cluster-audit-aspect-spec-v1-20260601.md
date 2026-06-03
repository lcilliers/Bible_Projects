# Cluster audit — aspect specification (the canonical checklist)

**Living document** · **Doc version:** 1 · **2026-06-01** · grounds `scripts/audit_cluster_v1_20260601.py` (the reusable cluster auditor).
**Purpose:** the consolidated, well-founded set of aspects a cluster audit checks — synthesised from prior work, not re-imagined. Each aspect cites its source so the audit stays anchored to the methodology.

**Sources synthesised:**
- `archive/scripts/_validate_analysis_complete_v1_20260531.py` — the proven two-condition gate that reset the 17 clusters (8 checks).
- `Workflow/methodology/wa-cluster-readiness-gate-design.md` §3 — the gate definition (Conditions 1/2; four homes; data-substrate prerequisites §3.3).
- `Workflow/Instructions/wa-sessionb-cluster-instruction-v3_0-20260527.md` §10 — Phase F exit gate (10-point per-phase completeness checklist).
- `scripts/_audit_cluster_input_coverage_v2_20260530.py` (F6) — findings/anchor coverage.
- `scripts/_audit_all_analysis_complete_clusters_v1_20260530.py` (F7) — per-cluster summary shape.
- This session's registers — incremental-update inputs (new terms / pointers / boundaries).

**Severity key:** `GATE` = hard, blocks Analysis Complete (a single GATE failure ⇒ not validly complete). `STRUCT` = structural-completeness (v3_0 Phase F); a fresh-v3_0 cluster must pass, a legacy cluster reports for awareness. `INFO` = reported, never gates. `INCR` = an item to **re-submit/clear in the incremental update** (not a defect — work to do).

---

## A. Analysis-Complete gate — the two-condition contract  (source: validate-script + gate-design §3)

### Condition 1 — verse/tier findings captured (reads `cluster_finding`)
| ID | Aspect | DB read | Sev |
|---|---|---|---|
| A1 | Findings present | `cluster_finding` active rows > 0 | **GATE** |
| A2 | No nonsense/mis-classified rows | `cluster_synthesis` rows whose text is only a gap acknowledgment (M38 T5.7.3 pattern) | INFO* |
| A3 | Every characteristic has findings | each `characteristic` has ≥1 active `cluster_finding` | **GATE** |

### Condition 2 — every leftover resolved to observation-or-deleted
| ID | Aspect | DB read | Sev |
|---|---|---|---|
| A4 | No active BOUNDARY sub-group members | `cluster_subgroup` code='BOUNDARY' → live verse_context / mti_term_subgroup / VCG members = 0 | **GATE** |
| A5 | No unresolved BOUNDARY_DECISION_PENDING | `wa_session_research_flags` code=BOUNDARY_DECISION_PENDING, resolved=0, cluster named in label/desc | **GATE** |
| A6 | No unresolved gating flags | SD_POINTER/SB_FINDING/PH2_* resolved=0 on the cluster's registries (registry→cluster, **non-exclusive**) | **GATE** |
| A7 | No stray Session-B findings | `wa_session_b_findings` status∈(pending,open), linked term→sub-group→cluster | **GATE** |
| A8 | No unconfirmed actionable observations | `cluster_observation` type∈(CROSS_CLUSTER_HANDOFF, SELF_CHECK_OBSERVATION) status≠confirmed | **GATE** |
| A9 | No orphan findings | active non-synthesis `cluster_finding` with no characteristic AND no sub-group | INFO |

\*A2 is INFO not GATE because it's a heuristic (text match); surfaced for review, fixed under Condition 1.

---

## B. Structural / phase completeness  (source: v3_0 §10 Phase F exit gate)

**Researcher direction 2026-06-01:** verse meaning + keywords are a **cross-cluster analytic necessity, not optional** → B1a/B1b are **GATE**. VCG-anchor and anchor-coverage are likewise mandatory → B5/B7 GATE.

| ID | Aspect | DB read | Sev |
|---|---|---|---|
| B1a | Phase A — verse **meanings** | every is_relevant=1 `verse_context` has non-empty `analysis_note` | **GATE** |
| B1b | Phase A — **keywords** | every is_relevant=1 `verse_context` has non-empty `keywords` | **GATE** |
| B2 | Phase B — verses grouped | is_relevant `verse_context` have `cluster_subgroup_id` AND `group_id` | STRUCT |
| B3 | characteristics table complete | `characteristic` rows present; `characteristic_subgroup` links present; **every non-BOUNDARY sub-group is linked to a characteristic** | **GATE** |
| B4 | Phase D — findings per characteristic | active `cluster_finding` count per characteristic (legacy clusters vary; v3_0 expects 189 ea.) | INFO |
| B5 | every active VCG has an anchor | each active VCG (cluster's sub-groups) has ≥1 `is_anchor=1` verse | **GATE** |
| B6 | Citation traceability | `finding_citation` rows present for the cluster's findings | STRUCT |
| B7 | every anchor verse covered in findings | each active anchor verse's reference is cited (`finding_citation` verse) by a cluster finding | **GATE** |
| B8 | Distribution health (future) | no substantive sub-group > 40% of substantive verses (§6.2.7) — *not yet implemented* | INFO |

---

## C. Data-substrate prerequisites  (source: gate-design §3.3; this session's cleanups)

| ID | Aspect | DB read | Sev |
|---|---|---|---|
| C1 | Old-format VCGs dissolved | no active old-format (`^\d+-\d+`) VCG tied to the cluster's terms (else: dissolve at Phase C) | STRUCT |
| C2 | Term→sub-group linkage present | `mti_term_subgroup` links exist for the cluster's live terms (M38 had 0) | STRUCT |
| C3 | No live duplicate term rows | each of the cluster's strongs has exactly 1 live `mti_terms` row | INFO |

---

## D. Incremental-update inputs — the re-submit / clear worklist  (source: this session)

| ID | Aspect | DB read | Sev |
|---|---|---|---|
| D1 | New terms to place | terms with `cluster_code`=this cluster but no `mti_term_subgroup` link (e.g. FLAG-classified) → place + analyse | INCR |
| D2 | Unallocated pointers | findings/flags routed (`cluster_link`) here, not yet adopted into a finding | INCR |
| D3 | Unresolved boundaries | BOUNDARY_DECISION_PENDING for this cluster (= A5) | INCR |
| D4 | Old VCGs to dissolve | this cluster's own old VCGs awaiting Phase-C dissolution (= C1) | INCR |

---

## Verdict & output

- **Gate verdict** = PASS unless any **GATE** aspect fails → **FAIL** (not validly Analysis Complete).
- **Incremental worklist** = the D items + any GATE/STRUCT failures, expressed as "re-submit (re-run a phase / add terms / adopt pointers)" vs "clear (resolve boundary / flag / observation; dissolve old VCG)".
- Per-cluster detail + a cross-cluster summary table + the consolidated worklist.
- Read-only; the auditor never writes. (Status demotion stays in the separate closure routine `_validate_analysis_complete`.)
