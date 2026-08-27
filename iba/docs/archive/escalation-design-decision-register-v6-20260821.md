# Escalation design — decision register (v6, 2026-08-21)

Supersedes [`escalation-design-decision-register-v5-20260821.md`](escalation-design-decision-register-v5-20260821.md).
One new entry, D27 — everything else unchanged, not restated; see v5.

---

## D27 — `ready_for_approval` has no explicit transition rule; `review`'s absence is correct

Checked systematically, per the researcher's direct question — every value in every live
`next_action*` enum group cross-referenced against `cfg_escalation_transition`, not assumed complete:

| Shape | Enum value | Explicit row? | Verdict |
|---|---|---|---|
| dispatcher | `hold`, `noted` | yes | correct |
| dispatcher | `approve`, `reject`, `revise` | no — priority-3 catch-all | correct, confirmed intentional |
| manual | `approved`, `reject`, `revise`, `noted` | yes | correct |
| manual | `ready_for_approval` | **no** — only reachable via the generic `assignee_changed` fallback, nothing requires that pairing | **real gap** |
| manual | `review` | no — falls to catch-all | correct — `review` is meant to be a marker with no state consequence of its own |

**The gap, concretely**: `Update -NextAction ready_for_approval` without *also* passing a `-AssignedTo`
that differs from the current value produces no state change at all — the item silently stays
wherever it was, not `re-assigned`. The earlier holistic-vocabulary table (v4) documented
`re-assigned` as the guaranteed result; the live `cfg_escalation_transition` rows don't actually
enforce that pairing, so the documented intent and the built behaviour disagree.

**Fix**: an explicit, unconditional row, so the result doesn't depend on whether the assignee happened
to textually change this specific call:

```
priority=5  shape='manual'  next_action='ready_for_approval'  condition_key='always'
  resulting_status_key='next_action=ready_for_approval'
```

Existing priority 5 (`assignee_changed`, generic) shifts to 6; the priority-6 catch-all shifts to 7.
Content unchanged, only their position — `ready_for_approval` now matches before the generic
fallback gets a chance to (or fails to).

**Configs touched:** **(a) new** — 1 `cfg_escalation_transition` row (above), plus 1 new
`cfg_status_flow` row/extension (`entity='escalation'`, `status='re-assigned'`) so
`next_action=ready_for_approval` resolves via `_status_for()` the same way the existing
`assignee_changed`-triggered path already does — same target status, a second `set_by` path into it,
subject to the same dedup-key check already flagged unconfirmed in D11/D21 (v3). **(b) validate** —
the two existing priority-5/6 rows' `priority` values get renumbered to 6/7 (a value change, not new
content). **(c) remove** — none.

---

## Everything else

**Unchanged from v5.**
