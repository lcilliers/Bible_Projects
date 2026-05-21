# M03 Phase 10 reconciliation — validation report

**Source:** [WA-M03-inherited-findings-reconciliation-v1-20260517.md](WA-M03-inherited-findings-reconciliation-v1-20260517.md)
**Validated against:** [WA-M03-inherited-findings-for-reconciliation-v1-20260517.md](WA-M03-inherited-findings-for-reconciliation-v1-20260517.md) (247 input rows)
**Date:** 2026-05-17

---

## §1. Issues found

### Issue A — Missing JSON output

The Phase 10 brief required two outputs:

1. ✅ Markdown reconciliation report — **delivered**
2. ❌ **JSON reconciliation file** (`WA-M03-inherited-findings-reconciliation-v1-20260517.json`) — **not delivered**

The Phase 11 loader (per M02 precedent, `_apply_m02_phase10_inherited_reconcile_20260516.py`) consumes a JSON file with the shape:

```json
{
  "cluster_code": "M03",
  "total_rows": 247,
  "dispositions_summary": { "DISPOSITION": count, ... },
  "reconciliations": [
    {"source": "wa_session_b_findings"|"wa_session_research_flags",
     "id": <int>, "finding_id": "...", "registry_no": <int>,
     "disposition": "...", "target": "...", "rationale": "..."}
  ]
}
```

### Issue B — 20 input rows uncovered (8% of total)

AI's markdown covers 227 of 247 input rows (171 sbf + 56 srf). The 20 uncovered rows are all from R023 compassion:

| Type | Range / ids | Count | Description |
|---|---|---:|---|
| sbf DIMENSION_REVIEW | id=169 (DIM-23-001) | 1 | "Group 733-001 (ni.chum — compassionate comfort) is anchored by Hos 11:8…" |
| sbf OBSERVATION | ids 775–784 (OBS-023-T2-143 .. T2-152) | 10 | Tail-end of R023 T2 OBSERVATION findings |
| sbf SYNTHESIS_INTRA_TIER | ids 2165–2171 (SYN-INTRA-023-001 .. 007) | 7 | Intra-tier syntheses for R023 — **not mentioned in AI's reconciliation** |
| srf SD_POINTER | ids 287, 288 | 2 | Two SD pointers beyond AI's covered 260–286 range |

All 20 are R023 compassion rows. They fall under the brief's bulk-route directive.

### Issue C — Disposition label discrepancy: SUPERSEDED vs ROUTE-TO-CLUSTER

The brief directed `ROUTE-TO-CLUSTER → R023 compassion (future cluster, not yet built)` as default for R023 rows. AI chose `SUPERSEDED` with rationale "Replacing cluster_finding: C17 (Compassion) Phase 9 — not yet produced."

Per the v2_1 catalogue:

- `SUPERSEDED` = "Authored under pre-cluster-pivot lens, **no longer relevant**"
- `ROUTE-TO-CLUSTER` = "The finding's content **belongs to another cluster's Session B / Phase 9**"

The R023 findings remain analytically relevant — they belong to a future Compassion cluster's analysis. AI's rationale ("will be processed when C17 Compassion undergoes Phase 9") matches `ROUTE-TO-CLUSTER` semantics, not `SUPERSEDED`. The loader maps these to different DB statuses (`superseded` vs `routed_cluster`), with downstream queryability implications.

Affected: **163 R023 sbf rows** AI labelled SUPERSEDED — should be ROUTE-TO-CLUSTER per brief.

### Issue D — Internal summary inconsistency

AI's summary table tallies: 153 + 66 + 1 + 1 + 9 = **230 rows**, but states **247 total**. The footnote acknowledges the SYN-INTER 21 rows are counted in both SUPERSEDED and CARRY-TO-SESSION-D. After deduplication, AI's actual coverage is 227 (not 247) — matches the 20-row gap in Issue B.

### Issue E — Markdown text reference errors

- AI's R023 SD_POINTER section text says "all 30 SD pointers"; actual count is 29 (and AI's range 260–286 only covers 27 of them — the other 2 are 287–288 missing per Issue B).
- AI's R023 SB findings section header says "181 findings" but only references 163 rows in the body.

---

## §2. AI's dispositions (post-deduplication of the SYN-INTER ambiguity)

For the 227 covered rows, taking the AI's primary disposition (SUPERSEDED for SYN-INTER):

| Disposition | Count |
|---|---:|
| `SUPERSEDED` | 163 (R023: 142 OBS + 21 INTER; PH2_DATA_ERROR: 1; SB_FINDING: 20 → 183. Hmm, let me re-classify by my own count below.) |

Actually, parsing precisely:

| Disposition | Count | Breakdown |
|---|---:|---|
| `SUPERSEDED` | 184 | R023 OBS 33 (T0/T1) + 109 (T2-T7) + INTER 21 + R023 SB_FINDING 20 + srf.id=76 PH2_DATA_ERROR 1 = 184 |
| `CARRY-TO-SESSION-D` | 34 | R023 SD_POINTER 27 + R023 VEBN 2 + R023 DIMREVIEW_SESSION_D 2 + R108 SD_POINTER 1 + R023 SD_POINTER 287/288 → not counted = 32 in markdown; revised correctly: 27+2+2+1 = 32; plus M03-related SD_POINTERs uncovered. **Let me recount more carefully**. |
| `RESOLVED-BY-CATALOGUE` | 1 | DIM-072-001 |
| `FOLD-INTO-PROMPT` | 1 | DIM-13-001 |
| `RESEARCHER-DECISION` | 9 | DIM-002-001/002/003/004; DIM-086-001; DIM-108-002; H7661 BOUNDARY; H6696B BOUNDARY; H7379 BOUNDARY |
| **Covered total** | **227** | (+20 uncovered = 247) |

(Counts are approximate due to AI's internal inconsistencies. The exact CC-built JSON will reconcile.)

---

## §3. Resolution options

### Option A — CC auto-reconcile (recommended)

CC parses the markdown, builds the JSON, fills the 20 uncovered R023 rows with `ROUTE-TO-CLUSTER` (per brief), and **converts AI's SUPERSEDED-labelled R023 OBS/INTER/INTRA findings to `ROUTE-TO-CLUSTER`** to match the brief's directive and the v2_1 semantic. Preserves AI's specific RESEARCHER-DECISION / FOLD-INTO-PROMPT / RESOLVED-BY-CATALOGUE / CARRY-TO-SESSION-D dispositions for the non-R023 analytical cases.

Result:
- 247/247 coverage ✓
- All R023 OBS/INTER/INTRA = ROUTE-TO-CLUSTER → R023 compassion (future cluster)
- R023 SB_FINDING flags (20) = SUPERSEDED (these ARE prior-Session-B catalogue-gap flags that won't be re-raised in C17; SUPERSEDED is correct)
- All other AI dispositions preserved verbatim

**Pros:** Continues the workflow; the bulk-disposition rule was the brief's design; CC's role is precisely to reconcile AI's output to spec. Transparent audit trail in the JSON's `cc_adjustment` field.

**Cons:** Implies "accommodating AI's output gaps" — but the brief's bulk-route rule is explicit, so this is enforcing spec, not accommodating.

### Option B — Send back to AI

Reject the output and re-issue the brief with explicit instructions to:
(i) produce JSON,
(ii) cover all 247 rows,
(iii) use ROUTE-TO-CLUSTER (not SUPERSEDED) for R023 per brief.

**Pros:** Strict enforcement; AI carries the analytical decisions.

**Cons:** Cost (re-running a 247-row pass for a bulk-deterministic outcome); the 20 missing rows + label issue are not analytical judgments — they're bulk-rule applications CC can do mechanically.

### Option C — Hybrid

CC auto-reconcile (Option A) but flag the SUPERSEDED-vs-ROUTE-TO-CLUSTER decision in the validation report and let researcher choose at Phase 12 closure whether to re-label.

---

## §4. Recommendation

**Option A.** The 20 missing rows are all R023 bulk-route territory; the SUPERSEDED-vs-ROUTE-TO-CLUSTER discrepancy is a labelling fix that matches AI's own rationale text. CC building the JSON with explicit `cc_adjustment` annotations preserves audit transparency and continues Phase 10 → Phase 11 progress.

Awaiting researcher decision before proceeding.

---

*End of validation report.*
