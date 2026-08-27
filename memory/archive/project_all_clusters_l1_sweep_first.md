---
name: project_all_clusters_l1_sweep_first
description: Strategy direction (2026-06-08) — work through ALL 46 clusters now, but reframed to protect against paying twice: run the L1 angle-sweep (read-only) across all clusters → a CROSS-CLUSTER ROLL-UP first; HOLD the expensive L2 synthesis (+DB writes) until that roll-up is read, because the cross-cluster understanding is expected to reshape the verse-synergy phase. Enabling step = one-time morph backfill (all clusters). Awaiting confirm before the backfill.
metadata:
  type: project
---

**Researcher conviction (2026-06-08):** work through **all** clusters to L2 now; a **cross-cluster
understanding will emerge** that is valuable across clusters, and the later **verse-synergy phase may be
completely reshaped** by it.

**CC reframe (agreed approach, protects against [[feedback_no_rework_paid_twice]]):** "bring all clusters to
L2" = run the **L1 angle-sweep across all 46 clusters (read-only)** → a **cross-cluster roll-up**. This brings
every cluster to L2's *doorstep* (narrowed, each with its residue worklist) — exactly where the cross-cluster
understanding emerges. **HOLD full L2 synthesis (the verse read + DB writes) until the roll-up is read**,
because the synergy frame the researcher expects to be reshaped is *decided by the sweep*; committing
per-cluster synthesis first risks doing the expensive judgement in a frame the sweep would change.

**Why the data backs it:** M01 alone is 64% cross-cluster (S5) + 45% qualifier (S4); the fabric is
overwhelmingly cross-cluster, and the study end-point already says clusters dissolve into cross-cluster
groupings ([[reference_study_end_point_and_milestones]]). The cross-cluster map is the right unit to see
*before* synthesis.

**Sequence:** (1) **morph backfill** — one-time DB write, all clusters (populate `morph_code`/`stem` from
STEP; M01-validated 100%; backup + dry-run, M01 first then scale) — the enabling step that makes the
morph/sense angle a cheap DB read. (2) **L1 angle-sweep, all clusters (read-only)** → per-cluster reports +
**cross-cluster roll-up** (qualifier map · cross-cluster co-occurrence matrix · shared-term/homonym index ·
scenario-type distribution); also stress-tests/hones the angle scripts across the full variation. (3) **read
the roll-up → decide the synthesis/synergy frame** (per-cluster vs cross-cluster-first), then build/run L2.

The roll-up is the deliverable; per-cluster reports are backing detail (not 200 disconnected files).
Implements [[feedback_l1_l2_is_multi_angle_report_then_synthesise]]. Detail:
`research/investigations/wa-v3_2-l1-l2-architecture-synthesis-v1-20260608.md` §6.

**STATUS (2026-06-08): L0 morph backfill COMPLETE** — all 46 clusters, 4 batches with review points,
**31106/31112 verse-rows (100.0%) carry morph_code/stem** (`scripts/_apply_morph_backfill.py`, matched on
`(mti_term_id, reference)`; pre-sweep backup `bible_research_pre_l1_sweep_20260608.db`). The sweep's only
structural write is done; layers A–F are read-only. **Next: run angle layers A–F → cross-cluster roll-up,
then read it to decide the synthesis/synergy frame.**
