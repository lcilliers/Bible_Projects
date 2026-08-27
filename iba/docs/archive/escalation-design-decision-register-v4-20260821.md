# Escalation design — decision register (v4, 2026-08-21)

Supersedes [`escalation-design-decision-register-v3-20260821.md`](escalation-design-decision-register-v3-20260821.md).
This round: D11/D21 simplified (a real reduction — a proposal withdrawn, not expanded), and a new
entry, D25, for a genuine defect in already-shipped code found by working through the approval
semantics properly. Every other row unchanged from v3 — not restated, see v3 for full text.

---

## D11 / D21 — Simplified: `issue` reuses the manual vocabulary in full, no separate scheme

**v3's proposal withdrawn.** Working through a real scenario (raise → active work → rounds of
back-and-forth → "I think this is resolved, please evaluate it") showed the terminal moment is
structurally identical to `ready_for_approval`/`approved` — inventing `open`/`decided`/`abandoned`
solved nothing the existing six manual values don't already cover (`reject`→`withdraw` already means
abandoned; `revise` already means another round; `review`/`noted` already exist).

**`state` during the back-and-forth**: no new mechanism — `in-progress` while someone's working
alone, `re-assigned` the moment it's explicitly handed to the other party, via the *already-existing*
generic "assignee changed, nothing more specific matched" rule. `next_action` mostly carries forward
unchanged through plain content-only updates; it only moves at real decision points.

**Individual points within one issue** (this register's own D-numbers) are **not** each their own
`next_action` state — that granularity lives in the issue's reference document (or, once built, a
`from_id`-linked child item once a point is ready to become its own task). The issue's own
`next_action`/`state` describe the whole thread. This document is itself the live proof of that
pattern working.

**Configs touched:** **(a) new** — none (retracted: v3's 3 `cfg_enum` rows and 5
`cfg_escalation_transition` rows for `shape='issue'` are withdrawn, not built). **(b) validate** —
confirm the existing `manual`-shape `cfg_escalation_transition` rows apply uniformly regardless of
`type` (they should already — `shape`, not `type`, drives them; worth a direct check once anything in
this plan is actually built, not assumed). **(c) remove** — nothing to remove; the withdrawn proposal
was never built.

---

## D25 — Authority-based approval, not same-party (new: a real defect in shipped code)

**The corrected semantics**, stated precisely: `ready_for_approval` is a *readiness* check —
`resolution` and any other required content actually present. `approved` is an *authority* check —
does the party setting it hold authority to approve this item — not "is it a different individual
from whoever set `ready_for_approval`." Resolution is written once, at `ready_for_approval`,
describing what makes the item ready; `approved` doesn't add content, it confirms the prior version
was genuinely complete and that authority to sign off exists. Claude preparing *and* approving the
same item is legitimate whenever Claude holds that authority for it — consistent with what
`escalation-redesign-plan-v3` already said (*"Claude may complete its own straightforward,
fully-recorded fixes"*) — the code built this session implemented a same-party ban instead, which is
a defect against that stated intent, not a correct stricter reading of it.

**The mechanical fix**: authority is expressed through a field that already exists —
`next_action_assigned_to`, as set by the `ready_for_approval` transaction. Whoever it names is who
may set `approved`. Claude assigning the item to itself at `ready_for_approval` is an explicit,
visible, auditable declaration of authority for that item; assigning it to the researcher means only
the researcher may approve. Replaces `update()`'s current `_last_next_action_originator` same-party
refusal, which blocks unconditionally regardless of assignment.

**A second, smaller correction the same reasoning surfaces**: the `resolution`-required check
currently fires only at `approved`. Per *"ready for approval validates that everything is in place to
be approved,"* it belongs at `ready_for_approval` itself — kept at `approved` too, as the confirming
re-check, not moved away from there.

**Configs touched:** **(a) new** — 1 `cfg_escalation_requirement` row:
```
action='ready_for_approval'  field='resolution'  condition_key='always'
message='resolution must be filled in before requesting approval -- ready_for_approval is the readiness check, not approved'
```
**(b) validate** — the existing `action='approved', field='resolution'` row stays, re-purposed in
documentation (not content) as the confirming re-check rather than the sole check. **(c) remove** —
none.

**Not a design-plan item only — this is a defect in code shipped earlier this session.** Recorded
here rather than raised as its own live task yet, since this design thread is still active and the
fix should land as part of one coherent build pass, not piecemeal mid-review — flagged plainly so it
isn't lost, matching the whole point of this register.

---

## Everything else

**Unchanged from v3** — D1–D9, D12, D14–D23 stand exactly as written there, not restated.
