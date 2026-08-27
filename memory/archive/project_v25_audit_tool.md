---
name: project-v25-audit-tool
description: v2_5 compliance audit script + corrective-actions plan format. Use when revisiting closed clusters under v2_5; canonical 5-step cascade defines the corrective workflow.
metadata: 
  node_type: memory
  type: project
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

The v2_5 compliance audit lives at `scripts/_audit_cluster_against_instruction_v25_v1_20260518.py`. Run it on any cluster (`--cluster M01`) to produce a markdown compliance report at `Sessions/Session_Clusters/{code}/WA-{code}-audit-against-v25-v1-{date}.md`.

**Output structure:** §1 corrective-actions plan (primary output), §2 legacy phase-restart verdict (informational), §3 summary by check, §4 per-check detail, §5 next steps.

**Canonical cascade** (every verse-level structural change walks through these steps, entering at the step appropriate to its error type):

1. **Phase 2** — Pass A meaning (author `verse_context.analysis_note`)
2. **Phase 5/6** — Sub-group review (fit existing OR propose new)
3. **Phase 7** — VCG review (fit existing OR create new with anchor)
4. **Phase 9/11** — Findings review (confirm / extend / contradict / new)
5. **Session C** — Publication review (re-publish affected chapters)

**Check list implemented** (see [project-cluster-schema-live](project_cluster_schema_live.md) for DB columns referenced):

- AUDIT-V25-STATUS-SUFFIX — `cluster.status` post-closure suffix detection
- AUDIT-V25-PIPELINE-INCOMPLETE — missing Pass A / sub-group / VCG / anchor / UT verses
- AUDIT-V25-BOUNDARY-PENDING — `BOUNDARY_DECISION_PENDING` flags
- AUDIT-V25-FORBIDDEN-SETASIDE — §4.5.1 forbidden-grounds pattern scan
- AUDIT-V25-TERSE-SETASIDE — terse set_aside_reason values
- AUDIT-V25-BOUNDARY-PARKING — STAYS-verdict terms with verses in BOUNDARY (§8.4.1)
- AUDIT-V25-EVIDENCE-GROUNDING — cluster_finding rows with no verse/VCG/anchor reference
- AUDIT-V25-COMPLETENESS — prompt × scope cells with no row (over-counts: catalogue includes legacy C-NNN codes)
- AUDIT-V25-REGISTER-FAMILIES — Pass A keyword scan of BOUNDARY corpus for §1.1 register families

**Verdict levels:**

- `COMPLIANT` — no actions
- `BOUNDED-FIXES` — all surgical; cluster status unchanged
- `BOUNDED-SYSTEMIC` — surgical + structural additions (new sub-groups/VCGs) but existing structure untouched
- `SYSTEMIC` — at least one action exceeds 50% of corpus denominator; phase-restart on affected scope warranted

**Known limitations of v1:**

- Completeness check over-counts (catalogue has legacy C-NNN codes alongside v2_5 T-codes). Filter to T0–T7 prompts to drop the count.
- Evidence-grounding regex misses sub-group references like `(M02-D)` and `M02-A`. Should widen to count those.
- Cluster-synthesis rows held to same evidence standard as scoped findings; should have looser standard.
- Placeholder vs ungrounded split is estimated from sample ratio (sample is capped at 30 rows).

**Initial audit results (2026-05-18):**

- M02: BOUNDED-SYSTEMIC (7 actions, mostly small; G4088 pikria needs sub-group routing post-closure)
- M04: SYSTEMIC (terse_setaside 66% of set-asides triggers systemic; bias-flagged RESCUE review needed)
- M05: SYSTEMIC (Phase 2 never populated analysis_note — methodology-era artefact, 1426 verses to backfill)

**How to apply:**

- Researcher direction is to defer revisiting closed clusters (M01, M02, M03, M05, M15, etc.) until later in the programme. The audit tool is ready when needed.
- M04 completion is the immediate focus — audit findings are inputs to its v2_5 retrofit.
- Next: test v2_5 on a new cluster (no prior closure to retrofit), to validate the instruction works end-to-end.

Related: [[feedback-inner-being-full-scope]], [[feedback-boundary-resolution-required]], [[feedback-cross-cluster-co-occurrence]], [[project-m04-paused-at-phase9]].
