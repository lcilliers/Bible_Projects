---
name: feedback_simple_steps_not_engineered_designs
description: Build in SIMPLE STEPS; a plan full of machinery gets rejected as overengineering.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a3d6e48-d97f-407e-83ba-ecef211af3af
---

**"No. This does not meet my objective. You are overengineering everything. Lets do it in simple steps."** — researcher, 2026-07-16, rejecting a DBSchema plan that had fingerprints, STALE-invalidation, 6 gates, a phased rollout and an adversarial description-grounding gate. What he actually wanted: *"Use the attached json. Bring it up to date by reading the current database."*

**Why:** The programme's whole failure mode is elaborate structure that nobody runs (see `project_lexical_rule_validation_failed_build_headless_app` — 5 gates declared LIVE with no code). Adding more machinery reproduces the disease while claiming to cure it. The researcher measures a design by whether it does the job, not by how much control it asserts.

**How to apply:**
- Start from **what already exists** and bring it current. He often names the artefact ("use the attached json") — that IS the design brief. Don't redesign around it.
- **One script, minimal flags, the obvious data shape.** Ask: what is the smallest thing that produces the deliverable?
- Keep only the machinery with an *earned* reason. Survivors from the cut-down: read-only source, preserve-descriptions-on-rebuild, retire-never-delete — each prevents a concrete loss he has already suffered. Cut: fingerprints, STALE, phase gates.
- **Then verify it hard.** Simple ≠ unverified. He wants the test to actually run and the result stated plainly — the rigour belongs in the *checking*, not in the architecture.
- Related: [[feedback_review_via_files_not_chat]] (he rejects AskUserQuestion — put decisions in a filed .md and let him reject at approval), [[feedback_root_fix_not_one_off]] (fix the cause — but the *simplest* fix that addresses the cause).
