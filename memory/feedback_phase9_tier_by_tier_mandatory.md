---
name: feedback-phase9-tier-by-tier-mandatory
description: Phase 9 catalogue findings MUST be authored tier-by-tier (T0..T7) with mandatory per-tier file write + STOP gate. One tier per response. AI drifts when allowed to hold all 189 prompts in working memory.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

For any Phase 9 cluster-finding session (per-characteristic or bundle), the brief MUST enforce tier-by-tier staged execution. One tier per response. Mandatory STOP gate at the end of each tier.

**Why:** M04, M07, and the start of M08 CHAR-1 all showed the same drift pattern when the AI was given the full 189-prompt task as a single pass — carries prior-tier reasoning into later tiers, performs analysis between tiers, substitutes fluency for citation, sometimes skips prompts entirely. The "OK to split by tier-pair if too large" hint in older briefs was treated as optional, and the AI default behaviour is one-shot processing.

**How to apply:** When building any Phase 9 input package:

1. Lead with a "**⚠️ TIER-BY-TIER STAGED EXECUTION — MANDATORY ⚠️**" section near the top, *before* the discipline list. Include a prior-failure callout naming M04, M07, M08 CHAR-1.
2. Specify the **hard procedural sequence per tier**:
   - OPEN TIER (announce tier name)
   - RE-READ EVIDENCE for the tier's lens (don't rely on memorised summaries)
   - AUTHOR THIS TIER'S PROMPTS (every prompt; no skipping; no bulk-classification)
   - WRITE TO FILE (T0 creates with header + T0 section; T1..T7 APPEND)
   - SELF-EVALUATE the tier (gate of 6-7 checks; see below)
   - DECIDE: if PASS, announce *"Proceeding to Tier T{N+1}"* and immediately begin the next tier in the SAME response; if FAIL, announce *"ALERT — {issue}. Pausing for researcher review."* and STOP.
3. **Self-evaluation gate** (per tier) — checks (a) prompt count matches tier size, (b) all [CHAR-N] markers correct, (c) every E finding has at least one verse-ref or VCG citation, (d) no cross-tier references to future tiers, (e) no two prompts share an identical 80-char opening, (f) verse references look valid against §3, (g) for bundles: no cross-batch references. Result is documented inline at the end of the tier section.
3. List explicit drift signals under "What NOT to do" (multi-tier responses, skipping prompts, inter-tier analysis, fluency-without-citation, bulk-classification).
4. Provide a recovery protocol: if drift detected, STOP and restart that tier from scratch.
5. Set cadence expectations explicitly — per-characteristic ≈ 9 responses (8 tiers + Self-check); bundle ≈ 36 responses for 4 chars × 9. "You are being asked to be correct, not fast."

**Tier sizes** (Catalogue v as of 2026-05-21): T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20 → 189 total.

For **bundles**, the discipline is **two-level** (batch + tier nested). Both the batch STOP-gate and the tier STOP-gate must be present. The bundle brief must enforce: no Batch N+1 until Batch N's file is written and CC has validated.

This applies to **every cluster** entering Phase 9 (M09+ going forward). The M08 builders [[scripts/_build_m08_characteristic_phase9_package_20260521.py]] and [[scripts/_build_m08_characteristic_phase9_bundle_20260521.py]] carry the canonical pattern; clone from these for future clusters rather than from M07's (which preceded this hardening).

Related: [[feedback_small_chunks_over_elaborate_pipelines]] — same principle (small atomic chunks beat one-shot pipelines) applied at the catalogue-finding scale.
