---
name: feedback_remediation_stop_points
description: Cluster remediation must have structural stop points for researcher review of judgement decisions
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 55b65c4e-7bc5-4e5a-98db-5d25382b8a12
---

Researcher involvement in reviewing **judgement decisions** during cluster remediation is crucial (stated 2026-06-02). The remedial process MUST have explicit stop points for confirmation and review — the orchestrator may not cross a judgement boundary on its own.

**Why:** mechanical re-derivation is safe to automate, but content calls (which flag to set aside, which finding to extend, which finding a pointer is adopted into) are the researcher's to validate. Auto-applying them would be exactly the "perform plausibility" failure the researcher rejects.

**How to apply:** in the remediation orchestrator [[project_remediation_orchestrator_active]], handlers are MECH (deterministic — run inline) vs SPEC (judgement — applied ONLY when the cluster spec file is present AND carries top-level `"approved": true`, the researcher's review signature). No spec → STOP REQUIRES-INPUT; present-but-unapproved → STOP REQUIRES-REVIEW. `--apply` advances one stage then stops. Aligns with [[feedback_integrity_and_intent_first]], [[feedback_review_via_files_not_chat]] (surface decisions in files, don't auto-decide).
