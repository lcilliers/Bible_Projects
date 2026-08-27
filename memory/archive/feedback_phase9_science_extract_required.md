---
name: feedback-phase9-science-extract-required
description: "Every AI-facing Phase 9 package (single-char brief, bundle brief, cluster synthesis brief) MUST list the cluster's science extract as a required input. CC's earlier guidance that 'no programme-specific science doc exists' was wrong — Workflow/Sciences/wa-m{NN}-{short}-scienceextract-v*.md exists per cluster."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

The programme maintains a per-cluster **science extract** at `Workflow/Sciences/wa-m{NN}-{short}-scienceextract-v{N}_{M}-{date}.md` (e.g. `wa-m04-joy-scienceextract-v1_0-20260513.md`). These are pre-analytical assets prepared for Phase 8's T7.3 prompts — they hold the scientific lens (positive psychology, affective neuroscience, attachment theory, etc.) alongside which the biblical pass is read.

**Why:** When asked early whether a "science file" was needed for Phase 9, CC said no — assuming AI's general knowledge of psychology / philosophy / sociology would suffice. The researcher corrected: every cluster has a dedicated science extract that **must** be loaded into every AI Phase 9 session. Without it the AI lacks the programme's chosen scientific framing (which researchers and reviewers expect to be cited consistently), and the T7.3 findings end up grounded in whatever frameworks the model happens to surface rather than in the curated set.

**How to apply:**
1. The single-char brief builder (`_build_m04_characteristic_phase9_package_20260518.py`) and bundle builder (`_build_m04_characteristic_phase9_bundle_20260519.py`) MUST include the science extract in their `Required inputs` table.
2. Filename pattern: `Workflow/Sciences/wa-m{NN}-{short}-scienceextract-v*.md` where `{NN}` is the cluster's zero-padded number (e.g. `m04`, `m15`).
3. Purpose label: "Programme-curated scientific lens for T7.3 (human science framework) prompts; ensures consistent framing across clusters and reviewers."
4. The same convention applies to the cluster-scope synthesis brief (the 8th session at end of each cluster's Phase 9).
5. When backfilling closed clusters (M01–M03, M05, M06, M15, M20, M26, M39, M46), include the matching science extract in their Phase 9 packages too.

Related: [[feedback_ai_package_self_declaration]] (Required-inputs block convention).
