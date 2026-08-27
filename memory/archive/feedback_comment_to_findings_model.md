---
name: feedback_comment_to_findings_model
description: "A6/A7/D2 comments are AI-evaluated into findings per affected cluster (multi-cluster, interactive debate), not mechanically dispositioned"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 55b65c4e-7bc5-4e5a-98db-5d25382b8a12
---

In cluster remediation, the A6 gating flags / A7 stray Session-B findings / D2 pointers are NOT noise to clear — their full `description`/`finding` text is analytical raw material to be **evaluated into findings**. One operation (`COMMENT_EVALUATION`), three rules (decided 2026-06-02):

1. **Per-affected-cluster seeding:** a comment creates a finding in EACH cluster it links to (comment-centric). Each seeded finding is reviewed in the light of that cluster's own analysis when its turn comes. No programme-wide inter-cluster resolution — the data will never fit one AI context. Seed, then validate per cluster.
2. **No Session-D routing** — see [[project_session_d_moot]]. Outcomes per comment shrink to: create finding(s) | set aside non-evidenced (still recorded as informing, not deletion).
3. **AI-evaluated, interactive, NOT mechanical:** understand the underlying data through researcher↔AI debate to the right conclusion. Not a fit-all auto-classifier. CC prepares the data package + writes agreed findings as patches; `"approved": true` = researcher sign-off on proposed findings.

**Why:** the data IS the authority (verse/comment meaning rules analytics); these comments carry real observations that belong in the narrative, and absence/supersession must be judged, not assumed. **How to apply:** don't pre-automate; run small interactive batches, debate, patch. Merges the old DISPOSITIONS+ADOPTION handlers. Relates to [[feedback_two_governing_principles]], [[project_pointer_lifecycle_model]], [[feedback_small_chunks_over_elaborate_pipelines]].

**Mechanics (proven on M38 comment 33 / DIM-039-001, salvation × debauchery, 2026-06-02):** evaluate against the cluster's FINDINGS digest (not just structure); VERSE-CHECK the relationship's nature (co-occurrence vs lexical/structural — state which in the finding); a new concept is a SEPARATE finding, never merged into an existing one; reciprocal pointers queued for another cluster use flag_code **`SD_CLUSTER`** (NOT `SD_POINTER` — that is an A6 gating code and would re-gate the source cluster via the shared registry). Applier: `scripts/_apply_comment_findings_v1_20260602.py` (new_findings INSERT / new_flags INSERT / fold_findings; guarded, needs `"approved": true`). Digest builder: `scripts/build_cluster_findings_digest.py`.
