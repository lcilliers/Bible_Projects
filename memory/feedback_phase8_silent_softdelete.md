---
name: feedback-phase8-silent-softdelete
description: "Phase 8 (old VCG dissolution) is silent CC mechanical soft-delete in v2_9+ — no comparison report, no researcher gate"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

Phase 8 in the Session B cluster pipeline is reduced (v2_9, 2026-05-26) to a silent CC mechanical soft-delete of inherited VCGs. The v2_0–v2_8 researcher comparison report and researcher gate are removed.

**Why:** by Phase 7 commit, every is_relevant verse routes to a new (Phase 7) VCG. The old VCGs are orphaned by the routing. Researcher review at Phase 5 (sub-group design) + Phase 7 (VCG design) already covers the structural decision; a separate Phase 8 sign-off is duplicative. Researcher direction 2026-05-26: *"we no longer need to compare the old VCGs with the new ... Scale down the phase 8 processes."*

**How to apply:**
- After Phase 7 commits, run a CC-only directive with two ops: soft-delete inherited `verse_context_group` rows (Op A) + their `vcg_term` links (Op B).
- Pre-check: unrouted-guard — no is_relevant verse may still reference an inherited VCG. If any do, STOP and return to Phase 7.
- For post-split clusters (e.g. M10c — constituted 2026-05-22 with 0 inherited VCGs), Phase 8 is a recorded no-op. Obslog records "no-op" and the cluster proceeds to Phase 8.5 / 8.7.
- Do NOT produce a comparison report. Do NOT seek researcher approval for the soft-delete. The mechanical operation is silent.

Authoritative spec: `wa-sessionb-cluster-instruction [current]` §11.
