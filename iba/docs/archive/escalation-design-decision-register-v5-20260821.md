# Escalation design — decision register (v5, 2026-08-21)

Supersedes [`escalation-design-decision-register-v4-20260821.md`](escalation-design-decision-register-v4-20260821.md).
One new entry, D26 — everything else unchanged, not restated; see v4.

---

## D26 — Work cannot land on a `raised` item; "start work" moves it in the same turn

**The gap**: nothing today stops a `comment`/`context`/`tried` update from being written while an
item still shows `state='raised'` — the current fallback rule (§D11/D21, v3) leaves state
*unchanged* when nothing more specific matches, so a raised item can silently accrue real work while
still displaying "nobody's touched this yet." **Researcher, direct: "task work or issue work should
not happen while the item is in raise."**

**Mechanical half — a hard write-time guard, checked live against the existing table (confirmed no
`action='update'` row exists yet, no PK conflict):**

New `cfg_escalation_requirement` row:
```
action='update'  field='state'  condition_key='always'
message="cannot add comment/context/tried while state is still 'raised' -- set -State in-progress
  (or a next_action that derives it) as part of this same update; work does not happen against a
  raised item"
```
Applied via a new `check_kind` (`not_raised_with_content`, alongside `presence`/`exists`/`not_self`/
`paired` already in the design): if `comment`, `context`, or `tried` is supplied this call, and the
resulting state (after applying whatever `-State`/`next_action` this same call also sets) would still
be `raised`, the call is refused. Applies uniformly to every type that can sit at `raised` at all —
`task`/`issue`/`run_error`/`config` — `notice` never does (closes at raise), so the rule is naturally
moot for it, not a special case.

**Chat-behaviour half — the "start work" trigger, honestly split from the mechanical half since a
verbal cue can't be machine-detected the way content-presence can:**

New `cfg_escalation` row:
```
rule_key: 'chat_start_work_moves_to_in_progress'
rule_text: 'When the researcher says "start work" (or an unambiguous equivalent) about a specific
  open item in chat, Claude'"'"'s next escalation Update on that item -- whatever else it carries --
  includes -State in-progress, in the same turn, before any research or drafting content is
  generated and reported back. An item never accrues real work while it still shows state=raised.'
enforced_by: 'the underlying invariant (no raised item receives comment/context/tried) IS
  mechanically enforced -- see cfg_escalation_requirement action=update field=state. Recognising
  "start work" as the specific trigger phrase is session practice only, same honest category as
  chat_routing -- not mechanically detectable the same way content-presence is.'
active: 1
```

**Configs touched:** **(a) new** — 1 `cfg_escalation_requirement` row (above, needs the new
`check_kind` value `not_raised_with_content` added to the small closed vocabulary alongside the
existing four); 1 `cfg_escalation` row (above). **(b) validate** — none. **(c) remove** — none.

---

## Everything else

**Unchanged from v4.**
