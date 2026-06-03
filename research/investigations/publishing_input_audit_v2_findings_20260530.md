# Publishing input audit v2 — findings + BOUNDARY readiness

**Generated:** 2026-05-30
**Trigger:** researcher direction 2026-05-30 — *findings encapsulate the evidence; rerun the audit on that basis, surface evidence that did not find a home, flag any unresolved BOUNDARY content.*

This document replaces [publishing_input_audit_findings_v1_20260530.md](publishing_input_audit_findings_v1_20260530.md). The v1 framing was wrong — it tested for the presence of standalone VCG `context_description` and term-inventory blocks, which the v3_0 pipeline does not need because findings carry that content verbatim. v2 tests the right thing.

---

## 1. What the audit tests now

Three pass/fail sections + one informational section.

### A. Coverage — every required DB evidence row has its identifier appearing in at least one chapter input

| Evidence | Identifier looked for in inputs |
|---|---|
| `cluster_finding` rows (status ≠ `gap`) | `question_code` |
| `cluster_subgroup` (non-BOUNDARY) | `label` |
| `characteristic` | `short_name` |
| `verse_context_group` (active, linked to cluster sub-groups) | `group_code` |
| `verse_context` (active anchors) | verse `reference` |
| `cluster_observation` (`target_phase IN ('session_c','E','publication')`, status open/confirmed/refined) | title slug |

### B. Exclusion — policy-excluded rows must not appear

| Row type | Reason |
|---|---|
| `cluster_finding` status=`gap` | Absence is the finding; surfaced via silence-principle prose, not as a finding row |
| `cluster_observation` `target_phase` ∉ publication phases | Targeted at other phases |

Leak detection uses a **unique fingerprint** (first 80 chars of `finding_text` or title slug), not just identifier match — because identifiers can be shared across scope-groups.

### C. BOUNDARY readiness — no unresolved BOUNDARY items

Two gating checks:

1. **No active BOUNDARY sub-group with active members.** A `cluster_subgroup` with `subgroup_code='BOUNDARY'` and live verses / terms / VCGs means the cluster has not finished its BOUNDARY resolution work.
2. **No unresolved `BOUNDARY_DECISION_PENDING` flags** in `wa_session_research_flags` for this cluster (resolved=0).

A third, non-gating informational check surfaces cluster_observation rows mentioning BOUNDARY; many of those are design-notes documenting past resolutions, so they are not used as readiness signals.

### D. Informational — VCG `context_description` coverage

Tracked but not gated. The standalone `context_description` field is reference material the AI does not need for prose writing because findings already quote the verses verbatim and name the VCG codes inline.

---

## 2. Results on three clusters

Script: [scripts/_audit_cluster_input_coverage_v2_20260530.py](../../scripts/_audit_cluster_input_coverage_v2_20260530.py)

| Cluster | Coverage | Exclusion | BOUNDARY | Verdict |
|---|---|---|---|---|
| **M38** (post-split, fresh chapter inputs) | FAIL (1 finding) | PASS | PASS | FAIL |
| **M15** (pre-v3_0 closed cluster) | FAIL (1 finding, 4 VCGs, 1 anchor) | PASS | FAIL (28 active BOUNDARY members) | FAIL |
| **M06** (pre-v3_0 closed cluster) | FAIL (27 old-format VCG codes, 5 anchors) | PASS | FAIL (65 active BOUNDARY members) | FAIL |

Per-cluster detail reports:
- [outputs/markdown/cluster_input_coverage_M38_v2_20260530.md](cluster_input_coverage_M38_v2_20260530.md)
- [outputs/markdown/cluster_input_coverage_M15_v2_20260530.md](cluster_input_coverage_M15_v2_20260530.md)
- [outputs/markdown/cluster_input_coverage_M06_v2_20260530.md](cluster_input_coverage_M06_v2_20260530.md)

---

## 3. Orphan evidence by cluster

### M38 — one orphan, in the cluster-synthesis spine

| Orphan | Detail |
|---|---|
| **T5.7.3 cluster-synthesis finding** | "All seven characteristics record a gap at T5.7.3, none able to confirm or deny a T2.8 null finding because…" — `finding_status='cluster_synthesis'` but the body content is a meta-observation that *every* characteristic recorded a gap. The synthesis itself is essentially a gap acknowledgment. The generator did not route it to Chapter 5 (T5 chapter) because the chapter doesn't currently surface cluster-synthesis findings at every tier — only T0/T1 in Ch1 and T0 in Ch3. |

**Verdict.** Real coverage hole. Minor. Two fixes possible: (1) generator emits cluster-synthesis findings into the chapter for their tier; (2) re-classify this particular row to `silent` since it documents the absence of evidence rather than asserting a finding.

### M15 — one finding, four VCGs, one anchor — ALL BOUNDARY-derived

| Orphan | Detail |
|---|---|
| **T7.1.8 synthesis finding** | "[BOUNDARY — structural characterisation note only; full catalogue pass not applicable]" — a BOUNDARY meta-note recording that the BOUNDARY sub-group was not put through the full T7 catalogue |
| **VCG `M15-BOUNDARY-VCG01`** | BOUNDARY meaning-group, with 1 anchor verse |
| **VCGs `523-002`, `528-001`, `525-001`** | Three older-format VCG codes inside the BOUNDARY sub-group |
| **1 anchor verse in M15-BOUNDARY-VCG01** | The verse linked to the BOUNDARY VCG |

**Verdict.** Every M15 orphan is downstream of the BOUNDARY-readiness failure. If BOUNDARY is resolved (route to clusters / set-aside / promote-to-sub-group), the coverage failures resolve with it.

### M06 — 27 missing VCG codes + 5 missing anchors

| Orphan | Detail |
|---|---|
| **27 old-format VCG codes** (`14-001`, `90-001`, `1568-001`, `5179-001`, `1643-001`, …) | M06 was constructed under an older VCG-naming scheme — Strong's-number-based codes like `90-001`. The current generator does not surface these codes in chapter inputs (and the codes themselves carry no cluster/sub-group semantics — they cannot be referenced meaningfully in prose). |
| **5 anchor verses inside the 27 old-format VCGs** | Same — these are M06-BOUNDARY anchors |

**Verdict.** Two distinct issues:
- For the old-format VCG codes, the gate should probably tolerate absence of the code in inputs when the code is not semantically referenceable. Need a policy call: are old-format codes part of the gate, or excluded?
- The 5 missing anchor verses inside BOUNDARY are downstream of M06's BOUNDARY-readiness failure — same as M15.

---

## 4. BOUNDARY readiness — the bigger finding

Two published clusters (M15 and M06) still carry active BOUNDARY material in their cluster_subgroup tables.

| Cluster | BOUNDARY label | Verses | Terms | VCGs | BOUNDARY_DECISION_PENDING |
|---|---|---|---|---|---|
| **M15** | Functional, supporting, and cluster-reassignment candidates | 14 | 13 | 1 | 0 |
| **M06** | Boundary/expression | 56 | 4 | 5 | 0 |

Both clusters were published (M15 has a book on disk, M06 likewise) without the BOUNDARY resolution work having been completed in the DB.

Per feedback_boundary_resolution_required: BOUNDARY-pending is not valid cluster closure. The valid resolutions are *set aside*, *route to cluster*, *move to sub-group*. None of these has happened for these 14+56 verses and 13+4 terms.

**Implication.** Under the v1_0 publishing baseline, both M15 and M06 should fail the gate. A re-publication of either cluster would require a BOUNDARY-resolution pass first.

**Note on `BOUNDARY_DECISION_PENDING` flags across the programme:** 46 such flag rows exist programme-wide; 26 are resolved=0 (unresolved). These flags are primarily on M01 and other early clusters. They should be cleared in a programme-level housekeeping pass.

---

## 5. Recommended gate behaviour

The gate runs after Step 1 input generation, before Step 2 chapter authoring.

```text
python scripts/_audit_cluster_input_coverage_v2_{date}.py --cluster {CODE} --strict
```

Exit code 1 if any of:
- Any required Category-A row's identifier is not in any chapter input.
- Any Category-B excluded row's fingerprint leaks into a chapter input.
- BOUNDARY sub-group has active members.
- Any unresolved `BOUNDARY_DECISION_PENDING` flag.

Exit code 0 only when all three (A, B, C) pass.

Step 2 (chapter authoring) MUST NOT begin until the gate returns 0.

---

## 6. Proposed publishing-instruction additions

The current `wa-cluster-publishing-instruction-v1_0-20260530.md` should be extended with three sections:

### §4.1 Evidence inclusion contract

Category A — MUST appear (gate enforces ≥1 reference):
- `cluster_finding` (status != 'gap')
- `cluster_subgroup` (non-BOUNDARY)
- `characteristic`
- `verse_context_group` (active for this cluster)
- `verse_context.is_anchor=1` (active for this cluster)
- `cluster_observation` (target_phase ∈ {session_c, E, publication}; status open/confirmed/refined)

Category B — MUST NOT appear (gate enforces 0 references):
- `cluster_finding` (status = 'gap')
- `cluster_observation` (target_phase ∉ publication phases)
- Any row with `delete_flagged=1`

Category C — Informational (not gating):
- VCG `context_description` text
- Non-anchor verses
- Sub-group term inventory beyond anchor verses

### §4.2 BOUNDARY readiness pre-condition

Before Step 1 generation begins for a cluster:

1. `cluster_subgroup` rows with `subgroup_code='BOUNDARY'` must either be `delete_flagged=1` OR have zero active member verses/terms/VCGs. If neither, BOUNDARY-resolution work must complete first.
2. No `wa_session_research_flags` rows with `flag_code='BOUNDARY_DECISION_PENDING'` AND `resolved=0` for the cluster.

If either condition fails, Step 1 must not run. The researcher disposes of the BOUNDARY material first (route, set aside, promote).

### §4.3 Step 1 gate

After input generation, run the audit in `--strict` mode. Exit 0 to continue; exit 1 halts the pipeline.

---

## 7. Open policy questions for the researcher

1. **Old-format VCG codes in M06 (and possibly other pre-v3_0 clusters):** are these expected in chapter inputs, or excluded from the gate? Recommendation: exclude — they are not semantically referenceable in prose. The audit could check VCG codes only when they match the modern pattern.

2. **The M38 T5.7.3 cluster-synthesis finding:** is the row mis-classified (should be `silent` not `cluster_synthesis`), or should the generator emit cluster-synthesis findings into every relevant chapter? Recommendation: re-classify the specific row to `silent` (its body is a gap acknowledgment) and verify the generator routes cluster-synthesis findings to their tier chapter.

3. **M15 and M06 BOUNDARY backlog:** when is the BOUNDARY resolution work scheduled? Both clusters have existing publication artefacts on disk; under v1_0 they cannot be republished without the resolution work.

4. **Programme-wide 26 unresolved `BOUNDARY_DECISION_PENDING` flags:** housekeeping pass needed. Not blocking M38 publishing, but blocks the affected clusters (mostly M01, M02, M05).

---

## 8. Recommended next steps

1. Researcher confirms the inclusion contract (§6) and BOUNDARY readiness rules (§4.2).
2. Amend `wa-cluster-publishing-instruction-v1_0-20260530.md` with §4.1, §4.2, §4.3.
3. Decide policy on old-format VCG codes (§7 q1).
4. Re-classify the M38 T5.7.3 row (§7 q2).
5. Wire the gate into Step 1 — Step 1 runs generator, then runs audit, exits nonzero on failure.
6. Schedule BOUNDARY resolution for M15 and M06 (and the 26 programme-wide pending flags) before any republication under v1_0.

---

*v2 of the audit reflects the correct framing: findings carry the evidence; the gate tests reachability + exclusion + BOUNDARY readiness, not standalone descriptor presence.*
