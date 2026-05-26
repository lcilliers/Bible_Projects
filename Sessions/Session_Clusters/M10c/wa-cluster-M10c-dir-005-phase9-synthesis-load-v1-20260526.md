# Directive — M10c Phase 9 cluster-synthesis findings load

**Directive ID:** `wa-cluster-M10c-dir-005-phase9-synthesis-load-v1-20260526`
**Cluster:** M10c — Defilement and Impurity
**Phase:** 9 (catalogue findings — cluster-synthesis session, last of 5 sessions)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_9-20260526` §12
**Issued:** 2026-05-26
**Applied:** 2026-05-26 (live commit)

## §1 Required-inputs declaration

| # | Type | Path | Version |
|---|---|---|---|
| 1 | Instruction | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_9-20260526.md` | v2_9 |
| 2 | AI synthesis findings | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-cluster-synthesis-findings-v1_0-20260526.md` | v1_0 |
| 3 | Loader script | `scripts/_apply_phase9_cluster_synthesis_20260519.py` | unchanged |

**No AI step.** The AI authored its synthesis under the Phase 9 synthesis brief built earlier today (commit c5907e8); this directive loads the output.

## §2 Out-of-scope

- Phase 11 fold / validation
- Phase 12 closure
- T7.3 science-extract gap fix-up (deferred — researcher decision)

## §3 Pre-decisions

1. **Parser-safe synthesis output verified** — 189 prompt blocks, all using `[CLUSTER]` marker, no forbidden `[CHAR-N]` / `[SUB-]` / `[VCG-]` markers.
2. **Appendix split-off automatic** — the loader detects `## Appendix` and writes the prose appendix to a sibling file. M10c synthesis appendix saved to `wa-cluster-M10c-phase9-cluster-synthesis-appendix-v1_0-20260526.md` (16.5K).
3. **All 4 cluster_observation rows confirmed** — Self-check evidence ties each carry-forward to specific synthesis-tier prompt evidence (see §4.2 below).

## §4 Operations

### §4.1 Synthesis row load

| Op | Target | Rows | Effect |
|---|---|---:|---|
| A | `cluster_finding` (synthesis) | 189 INSERT | `characteristic_id=NULL`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`, `finding_status='cluster_synthesis'` for all 189 rows (parsed E/S/G outcome folded into `finding_text` body) |

Tally from parser: E=181, S=4, G=4 (= 189). Source file: `wa-cluster-M10c-phase9-cluster-synthesis-findings-v1_0-20260526.md`.

### §4.2 Carry-forward observation status advancement (open → confirmed)

| obs_id | type | linked char | new status | resolution_note (excerpt) |
|---:|---|---:|---|---|
| 247 | SPLIT_DESIGN_RATIONALE | 1 | confirmed | Confirmed at synthesis T1.2.2 — M10c-A and M10c-B treated throughout as complementary registers of one condition (mechanism vs verdict). |
| 248 | INTEGRATION_NOTE | 4 | confirmed | Confirmed at synthesis T6.1.1, T6.3.3, T6.6.1-2 — M27 = agency-dimension; M10c Char 4 = defilement-condition. Shared anchors: Mar 3:11, Mat 10:1. |
| 249 | INTEGRATION_NOTE | 3 | confirmed | Confirmed at synthesis T6.3.3 — Ezekiel idolatry corpus simultaneously M10b (abomination) and M10c Char 3 (defilement-condition). |
| 250 | INTEGRATION_NOTE | 2 | confirmed | Confirmed at synthesis T6.1.1 — Char 2 surrounded by five-node network: M10 (upstream), M29 (desire), M08 (pride), M09 (consecration positive), M11 (cleansing downstream). |

## §5 Post-checks (all PASS)

- ✓ 189 synthesis rows inserted
- ✓ Loader's UNIQUE pre-check passed (0 prior cluster-synthesis rows for M10c)
- ✓ Loader's post-verify confirmed 189 rows present
- ✓ 4 cluster_observation rows status='confirmed' with non-empty resolution_note
- ✓ Total M10c cluster_finding rows: **945** (4 × 189 CHAR + 189 CLUSTER)

## §6 Result

**APPLIED.** Phase 9 complete. Cluster status remains `Analysis - In Progress`. Next: Phase 11 fold + validation, then Phase 12 closure (per researcher direction).

The 8 new cross-characteristic patterns discovered during synthesis (recorded in the Self-check section of the findings file) are not seeded as new cluster_observation rows by this directive — they live in the synthesis finding bodies and the appendix prose, where they belong analytically. Phase 11 / Session C consume them from there.
