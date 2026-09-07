# Directive — M10c Phase 9 characteristic findings load

**Directive ID:** `wa-cluster-M10c-dir-004-phase9-char-findings-load-v1-20260526`
**Cluster:** M10c — Defilement and Impurity
**Phase:** 9 (catalogue findings — 4 per-characteristic batches)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_9-20260526` §12
**Issued:** 2026-05-26
**Applied:** 2026-05-26T11:0X:XXZ

## §1 Required-inputs declaration

| # | Type | Path | Version |
|---|---|---|---|
| 1 | Instruction | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_9-20260526.md` | v2_9 |
| 2 | AI findings — char 1 | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char1-Ritual-defilement-state-findings-v1_0-20260526.md` | v1_0 |
| 3 | AI findings — char 2 | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char2-Moral-inner-defilement-state-findings-v1_0-20260526.md` | v1_0 |
| 4 | AI findings — char 3 | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char3-Corporate-covenantal-defilement-findings-v1_0-20260526.md` | v1_0 |
| 5 | AI findings — char 4 | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char4-Defilement-by-external-spiritual-agency-findings-v1_0-20260526.md` | v1_0 |
| 6 | AI worklog (cumulative, phases 3-5-7-9) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-AI-worklog-phases3-5-7-9-v1-20260526.md` | v1 (renamed from `wa-obslog-M10c-phase3-v1_0` to canonical pattern) |
| 7 | Loader script | `scripts/_apply_phase9_characteristic_findings_20260518.py` | unchanged |

**No AI step in this directive** — the 4 AI batches were authored under the Phase 9 briefs (`wa-cluster-M10c-phase9-char{N}-...-brief-v1-20260526.md`); this directive loads their outputs to `cluster_finding`.

## §2 Out-of-scope

- Cluster-synthesis batch (separate directive after this one)
- Phase 11 fold / validation
- Phase 12 closure

## §3 Pre-decisions

1. **All 4 AI batches validated by the loader** — each parses to 189 prompt blocks with consistent `[CHAR-N]` markers and no forbidden scope markers (SUB/CLUSTER/VCG).
2. **T7.3 science-extract gap noted** — char 1 Self-check flagged Section 4 (Defilement) of the science extract was not uploaded during the AI session. T7.3 findings are partial across all 4 chars. Researcher to supply Section 4 if T7.3 augmentation is needed (post-load fix-up directive).
3. **Carry-forward observation status advancement** — to be applied in a follow-up directive after researcher review of the Self-check summaries (status `open` → `confirmed` / `refined` per §11B.3).

## §4 Operations

| Op | Target | Rows | Effect |
|---|---|---:|---|
| A | `cluster_finding` (char 1) | 189 INSERT | finding_status: E=158, S=27, G=4 |
| B | `cluster_finding` (char 2) | 189 INSERT | finding_status: E=177, S=9, G=3 |
| C | `cluster_finding` (char 3) | 189 INSERT | finding_status: E=173, S=13, G=3 |
| D | `cluster_finding` (char 4) | 189 INSERT | finding_status: E=145, S=41, G=3 |
| **Total** | — | **756 INSERT** | E=653, S=90, G=13 |

Per-row fields: `cluster_code='M10c'`, `characteristic_id=<53/54/55/56>`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`, `obs_id=<from question_code>`, `finding_status=<finding|silent|gap>`, `finding_text=<body>`, `source_file=<findings .md>`, `version='v1'`.

## §5 Post-checks (all PASS)

- ✓ char 1: 189 rows (E=158, S=27, G=4)
- ✓ char 2: 189 rows (E=177, S=9, G=3)
- ✓ char 3: 189 rows (E=173, S=13, G=3)
- ✓ char 4: 189 rows (E=145, S=41, G=3)
- ✓ Total: 756 rows
- ✓ Loader's per-batch UNIQUE pre-check passed (no duplicate inserts)
- ✓ Loader's per-batch post-verify passed

## §6 Result

**APPLIED.** Cluster state remains `Analysis - In Progress`. Next: cluster-synthesis batch (CHAR + CLUSTER scope), then Phase 11 fold and Phase 12 closure.
