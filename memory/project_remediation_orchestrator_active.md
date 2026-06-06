---
name: project_remediation_orchestrator_active
description: Per-cluster remediation orchestrator is the active vehicle for closing the in-progress clusters
metadata: 
  node_type: memory
  type: project
  originSessionId: 55b65c4e-7bc5-4e5a-98db-5d25382b8a12
---

Cluster-closure work runs through a packaged per-cluster orchestrator: `scripts/_remediate_cluster_v1_20260602.py` (design: `Workflow/methodology/wa-cluster-remediation-orchestrator-design-v1-20260602.md`; playbook: `wa-cluster-remediation-playbook-v1-20260601.md`; auditor: `scripts/audit_cluster_v1_20260601.py`). Loop per cluster: AUDIT → dispatch each failing aspect to its handler → RE-AUDIT → REPORT → CLOSE. Stop points are structural — see [[feedback_remediation_stop_points]]. Comment handling = [[feedback_comment_to_findings_model]]; Session D moot = [[project_session_d_moot]].

**Progress (end of 2026-06-02):** CLOSED — M10c, M10b, M38, M08 (4). Master audit `outputs/markdown/cluster_audit_v1_20260601.md`: ~13 in-progress. **M20 IN PROGRESS** (next to finish): B1a meaning + B1b keywords + C1 dissolution done; 3 mis-classified ra.ga verses set is_relevant=0. OUTSTANDING on M20: **B2 = Phase-6/7 re-grouping** of 15 verses orphaned from dissolved old-format VCGs (sub-group homes decided by meaning: anxiety/double-minded→M20-A, perplexity aporeo/diaporeo/shevash→M20-D; VCG creation still to build), then **A6 34 / A7 39 COMMENT_EVALUATION**, then D1 7 / D2 2 → close.

**Handlers built this session:** citation extractor (B6/B7), citation-extension (B7 residual), pointer-dispositions, `_apply_comment_findings_v1` (COMMENT_EVALUATION: new_findings/new_observations/new_flags/fold/rehome/resolve/confirm_observations/exclude_terms), `_apply_keyword_backfill_v1` (B1b), `_apply_meaning_backfill_v1` (B1a — wraps Pass A; NB needs same-day patch-version-bump fix on re-run collision), `_apply_vcg_dissolution_v1` (C1), `_repair_dedup_ghost_verses_v1` (programme-wide verse repair). Auditor gates added: **A10** (no open Session-D observations) and **VRACT** (B1a/B1b/B2 exclude verses whose verse-record is soft-deleted). TO BUILD: full new-term **pipeline** (D1 with real verses), **B2 grouping/VCG creation**, **D2 pointer-adoption** applier.

**Key 2026-06-02 fixes:** programme-wide dedup-ghost verse repair (919: 753 re-point / 54 dup-del / 112 gone-del; 0 remain). Verse-change→revalidation principle ([[feedback_verse_change_revalidation]]).
