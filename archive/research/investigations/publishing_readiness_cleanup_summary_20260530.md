# Publishing readiness — programme-level cleanup summary

**Generated:** 2026-05-30
**Audit driver:** [scripts/_audit_all_analysis_complete_clusters_v1_20260530.py](../../scripts/_audit_all_analysis_complete_clusters_v1_20260530.py)
**Per-cluster audit:** [scripts/_audit_cluster_input_coverage_v2_20260530.py](../../scripts/_audit_cluster_input_coverage_v2_20260530.py)
**Detailed matrix:** [outputs/markdown/publishing_readiness_programme_v1_20260530.md](publishing_readiness_programme_v1_20260530.md)

---

## 1. Headline

**0 of 17 Analysis Complete clusters would pass the publishing gate today.**

The gate now tests four sections: Coverage, Exclusion, BOUNDARY readiness, Stray Session B / Session D findings. The cleanup work surfaces immediately when all four are applied.

| Result | Count |
|---|---|
| PASS | 0 |
| FAIL | 14 |
| NO INPUTS (cannot run gate) | 3 |

| Failure category | Clusters affected |
|---|---|
| Coverage | 14 / 14 |
| Exclusion | 0 / 14 (good) |
| BOUNDARY readiness | 5 / 14 |
| Stray SB / SD findings | 10 / 14 |

---

## 2. Cluster-by-cluster readiness matrix

| Cluster | Word | Coverage | BOUNDARY | Stray | Notable cleanup load |
|---|---|---|---|---|---|
| **M38** | Salvation | 1 miss | clean | clean | Fix 1 finding routing → could pass gate quickly |
| M01 | Fear | 20 finding miss | 7 pending flags | clean | BOUNDARY flag resolution; small generator gap |
| M02 | Anger | 44 finding miss | 4 pending flags | clean | BOUNDARY flag resolution; small generator gap |
| M03 | Grief | 75 finding miss, 7 char miss | **28 pending flags** | clean | Worst BOUNDARY backlog; significant coverage gap |
| M15 | Wisdom | 1 finding, 4 VCG, 1 anchor | 28 active BOUNDARY members | 35 SB, 31 flags | Mixed cleanup; mostly BOUNDARY-derived |
| M06 | Hate | 27 old-VCG, 5 anchor | 65 active BOUNDARY members | 7 SB, 8 flags | Old-format VCGs + BOUNDARY backlog |
| M07 | Shame | **1051 finding miss** | clean | 41 SB, 28 flags | Severe coverage gap |
| M08 | Pride | **901 finding miss** | clean | 11 SB, 10 flags | Severe coverage gap |
| M09 | Humility | **1068 finding miss**, 1 char | clean | 186 SB, 66 flags | Severe coverage + stray load |
| M04 | Joy | **1203 finding miss** | clean | 77 SB, 82 flags | Severe coverage + stray load |
| M20 | Doubt | 34 finding, 14 VCG | clean | 39 SB, 32 flags | Moderate cleanup |
| M26 | Righteousness | 60 finding, 18 VCG, 47 anchor | clean | 49 SB, 37 flags | Moderate cleanup |
| M39 | Blessing | 1 finding, 3 VCG, 17 anchor | clean | **219 SB**, 116 flags | Biggest stray-findings load programme-wide |
| M46 | Abundance | 46 finding, 31 VCG, 7 anchor | clean | 38 SB, 30 flags | Moderate cleanup |
| **M10** | Sin | n/a | n/a | n/a | **No chapter inputs generated** |
| **M10b** | Wickedness | n/a | n/a | n/a | **No chapter inputs generated** |
| **M10c** | Defilement | n/a | n/a | n/a | **No chapter inputs generated** |

---

## 3. The four cleanup workstreams

### 3.1 Coverage — generator misses (varies in size)

**Small (1–80 missing findings):** M38 (1), M15 (1), M39 (1), M01 (20), M02 (44), M20 (34), M46 (46), M26 (60), M03 (75).

These look like generator-routing bugs — findings that exist but don't get emitted into the right chapter input. M38 already has a known cause (one cluster-synthesis row at T5.7.3 mis-classified). The pattern in M01–M03 suggests similar systematic issues at the tier-routing layer.

**Large (900–1200 missing findings):** M07 (1051), M08 (901), M09 (1068), M04 (1203).

These cannot be generator routing bugs at that scale. Almost certainly the finding rows for these clusters use a different `obs_id` / `question_code` mapping than the generator's tier query expects, OR the generator is producing inputs from a stale version of the data, OR the input files in `inputs/` are from a pre-rationalisation generator run.

**Recommendation:** open these four clusters' input files and the generator query side-by-side. If the inputs are from an old generator run, regenerate and re-audit. If the findings genuinely don't fit the new tier model, decide whether to re-run the analytical pipeline or amend the generator to map old-style findings.

### 3.2 BOUNDARY — 5 clusters need resolution work

**Active BOUNDARY sub-group members (sub-group not yet emptied):**

- **M15 Wisdom** — sub-group `Functional, supporting, and cluster-reassignment candidates`: 14 verses, 13 terms, 1 VCG.
- **M06 Hate** — sub-group `Boundary/expression`: 56 verses, 4 terms, 5 VCGs.

Both need researcher disposition: route each member to a cluster, set aside, or promote to sub-group.

**Unresolved `BOUNDARY_DECISION_PENDING` flags (no sub-group, just pending flags):**

- **M01 Fear:** 7 of 12 pending.
- **M02 Anger:** 4 of 6 pending.
- **M03 Grief:** 28 of 28 pending — the worst.

Each flag is a per-term decision (e.g., "BOUNDARY term G0085 ademoneo from M01 closure. Pending researcher disposition: set-aside / promote-to-M01-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale.") — 39 individual decisions still owed.

**Recommendation:** schedule a BOUNDARY-disposition session covering M01 (7), M02 (4), M03 (28), M06 (5 VCGs + 56 verses), M15 (14 verses + 13 terms). Some of this can be batched if the resolution pattern repeats.

### 3.3 Stray Session B findings — 10 clusters, 695 floating rows

`wa_session_b_findings` rows in status `pending` or `open`, on registries that contribute to a cluster:

| Cluster | Stray SB | Stray SB/SD flags |
|---|---|---|
| M39 Blessing | **219** | 116 |
| M09 Humility | 186 | 66 |
| M04 Joy | 77 | 82 |
| M26 Righteousness | 49 | 37 |
| M07 Shame | 41 | 28 |
| M20 Doubt | 39 | 32 |
| M46 Abundance | 38 | 30 |
| M15 Wisdom | 35 | 31 |
| M08 Pride | 11 | 10 |
| M06 Hate | 7 | 8 |
| **Total** | **702** | **440** |

These are findings from the older Session B pipeline that were never folded into the cluster analysis, never resolved via Q&A, never routed to a cluster, and never marked `resolved_qa` / `routed_cluster` / `superseded` / `folded`. They sit on registry-scope and would in principle contribute to the cluster's evidence base.

**Two reading of "stray":**

- *Strict:* every pending SB finding for a cluster's contributing registry must be resolved before publishing. Resolution = mark `routed_cluster` (with absorption into `cluster_finding`) or `superseded` (with reason) or `folded` (with note).
- *Pragmatic:* per [feedback_findings_marginal_value](../../C:/Users/lerouxc/.claude/projects/g--My-Drive-Bible-study-projects/memory/feedback_findings_marginal_value.md) — SB findings are registry-scope shotgun; cannot be applied to term-and-verse analysis directly. The stray-finding load may be acceptable as historical residue.

**Recommendation:** the gate should treat stray findings as a WARNING by default, not a HARD FAIL — with a flag (`--strict-stray`) to elevate. Pragmatically, force the researcher to assess them per cluster, but allow publishing without resolving each one.

**Caveat:** M39's 219 stray findings is unusual enough to merit individual investigation. That cluster's registry contribution probably overlaps something heavily-trafficked in older Session B work.

### 3.4 Clusters with NO chapter inputs (M10, M10b, M10c)

M10 Sin, M10b Wickedness, M10c Defilement — Analysis Complete, but no chapter inputs exist in `Sessions/Session_Clusters/{code}/inputs/`. The input generator was never run on these three.

**Recommendation:** run [scripts/_generate_cluster_session_c_inputs_v2_20260512.py](../../scripts/_generate_cluster_session_c_inputs_v2_20260512.py) on each, then re-audit. They will likely surface their own cleanup load (BOUNDARY, stray SB, etc.).

---

## 4. Session D — none stray (good)

All `session_d_*` tables are empty (0 rows). Session D never wrote analytical output to the DB tables. The relevant residue is in `wa_session_research_flags` with `flag_code='SD_POINTER'` — 273 such rows programme-wide, unresolved. The audit captures these as stray SB/SD research flags.

---

## 5. Programme-wide totals

| Category | Count |
|---|---|
| Active `BOUNDARY_DECISION_PENDING` flags (resolved=0) | 39 |
| Active `SB_FINDING` flags (resolved=0) | 183 |
| Active `SD_POINTER` flags (resolved=0) | 273 |
| Active `SD_CLUSTER` flags (resolved=0) | 1 |
| Active `SB_INNER_BEING` flags (resolved=0) | 4 |
| `wa_session_b_findings` status=pending | 1,003 |
| `wa_session_b_findings` status=open | 25 |
| Total stray Session B findings across all clusters' registries (with dup, since registries span clusters) | ~702 |

---

## 6. Priority recommendation

Given the methodology pivot from per-registry Session B to per-cluster v3_0 analysis, much of the stray Session B load is historical. The right ordering is:

**Tier 1 — Fix the gate's small generator misses first.**

M38 (1 miss), M15 (1 miss, BOUNDARY aside), M39 (1 miss). M38 is the test case; close its single coverage gap and run a strict gate to validate the gate's end-to-end behaviour.

**Tier 2 — Resolve BOUNDARY work.**

5 clusters with active BOUNDARY material. 39 individual disposition decisions across M01 (7), M02 (4), M03 (28). Plus 2 BOUNDARY sub-groups to empty (M06, M15).

This is the smallest-volume / highest-impact cleanup: it produces real disposition decisions, not just status hygiene.

**Tier 3 — Investigate the large coverage gaps.**

M04 (1203), M07 (1051), M08 (901), M09 (1068). Diagnose the root cause (stale input files? generator-tier-routing mismatch? old finding schema?). Solve at the systemic level rather than per-cluster.

**Tier 4 — Generate inputs for M10 / M10b / M10c.**

Then re-audit those three to see what surfaces.

**Tier 5 — Stray Session B finding disposition.**

702 rows is a real backlog but pragmatically can be deferred until publication of the affected cluster is actually scheduled — at which point a per-cluster disposition pass becomes a real task.

Within Tier 5, M39 (219 stray SB) is large enough to warrant its own dedicated session before publishing M39.

---

## 7. What the gate enforces (proposed)

Per the v2 audit's four sections:

**Hard fail (blocks publishing):**
- Coverage failure (any DB evidence not in any chapter input)
- Exclusion failure (any policy-excluded row leaked into chapter inputs)
- BOUNDARY readiness failure (active BOUNDARY sub-group members OR unresolved BOUNDARY_DECISION_PENDING flags)

**Warning by default, hard fail with `--strict-stray`:**
- Stray Session B / Session D findings on contributing registries

Recommend the default behaviour — stray findings are a warning, not a hard fail. This keeps the gate practical given the 702-row historical load.

---

## 8. Recommended next steps

1. **Researcher policy calls** on each cleanup workstream — accept the prioritisation above? amend tier ordering? change gate strictness on stray findings?

2. **Tier 1 quick wins:** close M38's 1-finding gap, then run `--strict` to confirm gate produces PASS on M38 end-to-end. This validates the gate before applying it programme-wide.

3. **Tier 2 BOUNDARY:** schedule the 39-decision disposition session on M01 / M02 / M03; schedule the sub-group-emptying work on M06 and M15.

4. **Tier 3 investigation:** root-cause the 4 large coverage gaps (M04, M07, M08, M09) before committing to fix-per-cluster.

5. **Tier 4 input generation:** run the input generator on M10 / M10b / M10c.

6. **Add §4.1–4.4 to the publishing instruction** once policy calls in (1) are settled: inclusion contract, BOUNDARY pre-condition, stray-findings policy, Step 1 gate.

---

*This audit is the first time the publishing pipeline has been tested against the v1_0 baseline at programme scale. The cleanup load is substantial but tractable; the gate behaves as expected and surfaces real issues at every cluster.*
