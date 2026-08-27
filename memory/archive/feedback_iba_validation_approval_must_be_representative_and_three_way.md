---
name: feedback_iba_validation_approval_must_be_representative_and_three_way
description: "Any researcher-approval/escalation in the IBA app must present REPRESENTATIVE data (everything needed to actually judge the change, tailored per proposal kind, not a generic diff) and offer three outcomes — Approve / Not approve / Resubmit with comment — never a bare yes/no."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T14:14:05.777Z
---

Researcher's standing rule for the IBA app's `escalation` mechanism (2026-07-21, stated while designing
`configuration_maintenance`'s approval-gated config-write step): *"one of the rules for validations by
me, is that the data presented to approve must be representative of what I need to approve. That means
what you are showing me to consider is vital. Approve / not approve / resubmit with an opportunity to
provide a comment."*

**Two requirements, binding on every escalation the app raises — not just config-maintenance's:**

1. **Representative payload.** The `question`/`preset` shown must contain everything the researcher
   actually needs to judge *that specific* change — tailored to the kind of proposal, not a generic
   before/after value dump. E.g. a passage-rule change needs example affected passages and
   before/after stats attached, not just `min_shared_strongs: 1 -> 2`.
2. **Three-way answer, not yes/no.** Approve / Not approve / **Resubmit with comment.** "Resubmit with
   comment" is not a rejection — it sends the proposal back to be revised and re-raised, incorporating
   the comment. `registry.py`'s `create()` currently only supports yes/no — that's the old, now-superseded
   shape. Supporting three-way needs a `comment` column on `escalation` and a third `answer` value; this
   should propagate to every escalation user, not stay config-maintenance-only.

**Why:** the whole point of gating a high-blast-radius change behind researcher approval collapses if the
approval screen doesn't show enough to actually judge it — a rubber-stamp yes/no on an under-informative
diff is not real oversight.

**How to apply:** whenever designing any escalation/approval flow in this app (config changes, registry
approval, future analytic-layer confirmations), design the payload FIRST around "what would the
researcher need to see to make this call," and always offer the three-way answer with an optional
comment — never assume yes/no is enough. Related:
[[feedback_iba_config_changes_require_researcher_approval_never_silent]].
