---
name: project_passage_reading_checkback_gate
description: "STANDING PROCESS (2026-07-04, researcher-mandated): every narrative passage reading MUST pass an external check-back gate before it is trusted, to regulate my two devastating tendencies - BIAS (eisegesis) and THEME-BUILDING (skipping the detail). Script: scripts/_check_passage_reading_coverage_v1_20260704.py --unit-code=X."
metadata: 
  node_type: memory
  type: project
  originSessionId: 92aed34e-8a28-44a4-8d9d-4bdf6df70a12
---

The researcher mandated (2026-07-04) that I *build in a check-back to regulate my tendencies* — the two named as devastating: **bias** (reading in meaning not on the verse) and **theme-building / skipping the detail** (jumping to synthesis). A check that lives only in my head will not hold; it must be external, run against the raw data.

**The gate:** `scripts/_check_passage_reading_coverage_v1_20260704.py --unit-code=<UNIT>` (read-only). After drafting each passage reading, run it. It lists every non-T2 span in the passage and reports: (1) **verses not referenced** by ch:vn in the reading; (2) **glosses not mentioned**; (3) **repeated glosses** (each must be treated DISTINCTLY, never lumped); and prints a **4-point bias self-audit**. Fix every miss (or explicitly justify a skip), re-file, re-run until the detail-skipping signal is CLEAN.

**Proof it works:** on my very first reading (GEN-01) the gate caught that I had compressed the three namings (qara 1:5/1:8/1:10) and the two living-creature days (1:20-21 vs 1:24) into single lumped operations — exactly the theme-building tendency. Fixed → v2 (prose_section 917), clean. GEN-02 passed clean first time.

**How to apply:**
- Gate is MANDATORY per passage before the reading is trusted/committed. Never file-and-forget.
- CLEAN verse/gloss coverage is necessary, not sufficient — still answer the bias self-audit: every finding read OFF a span (stated/inferred, no unanchored claim = no [[feedback_verse_meaning_grounded_not_imported]] violation); 'why is THIS one different' asked for each repeat ([[feedback_resist_grouping_preserve_distinctions]]); no NT/theology import; no theme built before the detail was exhausted.
- The gate is genre-general — reusable for the prophet/wisdom **depth-pass** later ([[project_prophets_wisdom_read_at_movement_depth_debt]]), where it will flag the 8-28% touch-rate directly.
- Coverage ≠ depth was the lesson; this gate is how coverage-of-attention is now enforced.
