---
name: Q&A findings have marginal/indicative value, not term-level
description: The Session B Q&A/findings process operated at registry-scope; findings cannot be applied directly to term-and-verse analysis. Use as directional context only.
type: feedback
originSessionId: 0b9d95eb-ab3c-4fd3-9dd9-6341794c07de
---
The Session B Q&A / findings process (table `wa_session_b_findings`) was — in the researcher's words — *"largely a process of shooting from the hip with a broad shotgun"*. The findings have at most **marginal or indicative analytic value** for term-level analysis under the new (v6) named-characteristic pipeline.

**Structural evidence (recorded 2026-05-05 from M05 coverage report):**
1. **0 of 2,883 active findings have `term_id` set.** Findings attach only to `registry_id`.
2. **All terms from a single registry share the same Find (R) registry-context count** — e.g. all 27 R103-love terms show Find (R) = 198 indistinguishably. The findings cannot say which specific term they address.
3. **~80% of M05 terms have no direct Strong's mention in any finding text.** Direct term-level traceability is rare.
4. Where there ARE direct mentions (e.g. chesed = 61, chasid = 31), they cluster on a few high-frequency terms; the long tail is silent.

**How to apply (the principle):**
- Do NOT inherit findings as term-level inputs to M-cluster analysis. The data model can't support it.
- Use findings + SD pointers as a **directional appendix** — useful for:
  * Cross-cluster claims (*"forgiveness produces love"* — Luk 7:47)
  * Shared anchor verses (verses where multiple characteristics meet)
  * Negative-space framing (closed heart vs compassion)
- The term-level work (verse selection, group decisions, characteristic-in-operation reading) must be done **fresh** against `wa_verse_records` for each term in the M-cluster.

**Why:** the Q&A was framed at registry scope, not term scope, and used broad theological observation prompts rather than term-grounded interrogation. The findings reflect that frame — they say things about *the registry's territory* (love-as-a-whole, forgiveness-as-a-whole), not about *what each specific term contributes to that territory*.

**Affinity-scan implication:** orphan-finding scans (cross-cluster M-affinity hits) surface useful directional pointers but should not produce term-level migration recommendations. They identify *territory* relevance, not term relevance.
