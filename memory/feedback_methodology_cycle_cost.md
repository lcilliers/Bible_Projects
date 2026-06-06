---
name: feedback-methodology-cycle-cost
description: "The 2026-05-21 methodology hardenings (tier-by-tier discipline, per-tier self-eval, spot-checks after every char) increased Claude API cycle consumption noticeably. Researcher hit context budget sooner. Watch the discipline-vs-budget trade-off."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

The Phase 9 hardenings introduced on 2026-05-21 — tier-by-tier staged write-out, per-tier self-evaluation gate, spot-checks of every char findings file, brief regenerations across runs — collectively increased the AI session cycle cost. Researcher feedback (2026-05-21): *"the recent changes in the methodology and program steps have increased the overall cycles of processing within the context of Claude and the available cycles, and I run out of capacity much sooner."*

**Why:** Each characteristic now takes ~9 AI responses (8 tiers + Self-check) instead of 1. Spot-check + verdict for each char adds another ~1 CC response. For a 4-batch bundle that's ~40 AI responses vs the pre-hardening ~4. The cost is intentional — drift was real and the discipline is correct — but it materially affects how much can be done per chat-context window.

**How to apply:**

1. **Don't undo the discipline reflexively.** The tier-by-tier + self-eval pattern fixed concrete drift (M04, M07, M08 CHAR-1 v1). The fix is doing its job.
2. **But look for opportunities to compress where the gate is safely passing**:
   - The 2026-05-21 STOP→self-evaluate-then-proceed change already reduces researcher-prompt cycles (was 9 prompts per char, now potentially 1).
   - When spot-check rates settle (consistent >85% citation, 0 cross-char drift, 0 bulk-classification), consider sampling rather than running full spot-checks every characteristic.
   - For early-closure cluster retrofits, batch-plan rather than per-cluster — share the v2_5 audit infrastructure across M01/M03/M05/M06/M39/M46.
3. **Defer optional CC work**:
   - Filename canonicalisation pass (done 2026-05-21) was important but expensive. Future similar pushes — schedule into a dedicated session rather than mid-pipeline.
   - Overview generator hardening (post-closure-drift detection) is good but was a 30-min CC pass that competed with researcher time.
4. **When the researcher signals capacity limits**: don't propose ambitious additional work in that turn. Wrap up tightly, save state, commit, and let the researcher restart fresh.
5. **Within a chat session**: don't re-read large files unnecessarily. Use targeted Grep / Read with offset+limit rather than full-file reads. Use the build_file_manifest search instead of glob+ls.

This is not a rule against discipline — it is a budget awareness reminder. The right discipline is correct; the question is which checks fire automatically vs which the researcher chooses to run.
