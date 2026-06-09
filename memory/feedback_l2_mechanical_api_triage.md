---
name: feedback_l2_mechanical_api_triage
description: L2 mechanical-vs-API decision (2026-06-09). It is a JUDGEMENT on the COMPLEXITY of the verse / the adequacy of the MECHANICAL OUTCOME, not a fixed input rule. Mechanical pass runs first; if the verse is simple the API call is not even necessary (ACCEPT). If the mechanical outcome is clearly inadequate, CC routes the verse to API. If CC cannot make the judgement (borderline), it is escalated to the RESEARCHER to decide whether the verse goes to API. Default = mechanical-accept; API is the exception; researcher resolves the uncertain middle.
metadata:
  type: feedback
---

**Researcher rule (2026-06-09), for the L2 per-term-per-verse finding ([[feedback_characteristic_is_typed_term_in_verse]]).**

The mechanical-vs-API choice is **based on the complexity of the verse** — a **judgement call on the
evaluation of the mechanical outcome**, made *after* the mechanical pass, not a fixed input rule.

**The ladder (per verse):**
1. **Mechanical pass first** (CC script): STEP sense-branch via morph · type · the clear tier identifications
   → candidate finding + complexity signals.
2. **CC evaluates the mechanical OUTCOME for adequacy:**
   - **Simple / clean → ACCEPT** — the mechanical finding stands; **the API call is not even necessary.**
     (Most verses.)
   - **Clearly inadequate, CC can see it needs a read → send the verse to API** to complete the finding.
   - **CC cannot make the judgement (borderline) → escalate to the RESEARCHER**, who decides whether the
     verse goes to API.
3. Researcher calls on the borderline middle **calibrate the threshold** over time.

**Key:** the trigger is the **adequacy of the mechanical OUTCOME**, not the raw input — a multi-sense term
whose stem cleanly resolved is still an ACCEPT. **Default = mechanical-accept; API is the exception;
researcher resolves the uncertain middle.** Cost-efficient ([[feedback_cc_only_pipeline_verdict]],
[[feedback_chat_vs_api_for_classification]] — most verses need no API).

**First-draft adequacy signals (drive the judgement, not fixed rules; refine with use):** multi-sense residue
unresolved · within-stem shade ambiguity (fear vs reverence) · relevance/metaphor doubt (Song-6 class) ·
interacting multi-term array (roles depend on each other) · morph-type vs keyword-type conflict ·
numbered-sense homonym present · sibling-span pairing. **None present → ACCEPT candidate; present → weigh;
CC-unsure → RESEARCHER.** The escalation set is itself surfaced for review (no silent guessing).
