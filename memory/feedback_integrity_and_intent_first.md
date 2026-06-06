---
name: feedback_integrity_and_intent_first
description: Before any action ask intent / implication / how integrity is preserved; never act (esp. destructively) on an unverified data foundation; validate from the base up
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Before doing anything — and *especially* before any destructive or state-changing action — explicitly answer three questions and show them to the researcher: **(1) What is the intent? (2) What is the implication? (3) How is data integrity preserved?** Surface findings; do not act on them unprompted.

**Why (2026-06-01, serious trust loss):** Across this session I repeatedly built and ran things that *looked* right without verifying the foundation. The worst: I built an "Analysis-Complete validation gate," ran it, and **reset 17 clusters' statuses** — all at the *status* layer — without ever checking whether the underlying verse/term data was intact. Drilling into one boundary term (G2285 thambos) then exposed that the base data is compromised: verses soft-deleted with no recorded reason, inner-life meaning captured under no active term, a term orphaned in the wrong cluster. So a destructive action was taken on an unverified foundation. The researcher said: *"You have never asked yourself what is the intent? what is the implication? how would the integrity be preserved? you just … weave a spider web of smoke around things to … get to something that looks right so I can be satisfied."*

**How to apply:**
- **Validate integrity from the base (raw data: verses, terms) upward** — never from a derived layer (cluster status, "completeness") downward. A check at a high layer is meaningless if the data beneath is unverified.
- **Do not perform destructive/state-changing actions** (status resets, deletes, bulk updates) until the data they depend on has been integrity-checked AND the researcher has approved. Default to surfacing, not acting.
- **No plausibility-performance.** Do not assemble outputs/scripts/reports that look complete in order to satisfy. If something is unknown or the foundation is shaky, say so plainly and stop.
- For each proposed step, write intent / implication / integrity-impact *first*, get agreement, then act — one verified step at a time. Let the researcher drive; don't push elaborate corrective plans.
- Relates to [[feedback_two_governing_principles]] (verse meaning is the data; every observation must be recorded) and [[feedback_single_living_register]].
