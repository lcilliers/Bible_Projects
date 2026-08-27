# Escalation design — decision register (v7, 2026-08-21) — batch 1

Supersedes [`escalation-design-decision-register-v6-20260821.md`](escalation-design-decision-register-v6-20260821.md).
Batch 1 of the full completion pass: three settled decisions (D9, D12, D14) that were marked
`SETTLED` in every status table since they were confirmed, but never actually got their own dedicated
"configs touched" section — an omission this batch closes, catching one real knock-on correction in
the process. Plus D28 (the PS `ValidateSet` drift gap, raised in chat, formalised here). Everything
else unchanged from v6, not restated.

---

## D9 — Five-type model: configs touched

**Confirmed correct, 2026-08-21.** Checked live, not assumed: `cfg_enum('escalation_type')` already
holds all five active values (`task`, `run_error`, `issue`, `notice`, `config`) — this predates the
whole design conversation, so **D9 itself adds no new enum content.** What D9 actually settled is
that these five are meaningfully *distinct in behaviour*, not just five labels — and the behaviour
differentiation is fully accounted for elsewhere, not duplicated here: `notice`'s self-closing default
(D12), `issue`'s vocabulary (D11/D21, now simplified to reuse manual's in full), the
produced-documentation-task pattern (D18).

**Configs touched:** **(a) new** — none. **(b) validate** — confirm the 5 active `escalation_type`
values still exactly match the settled model (done — no drift found). **(c) remove** — none.

---

## D12 — Type-keyed defaults at Raise: configs touched, and a correction D11's simplification implies

**A knock-on correction, caught by cross-checking rather than left standing**: v2's original D12 said
*"issues open instead of defaulting to `review`"* — but that referenced the `open` `next_action`
value from the 3-value `issue` vocabulary **withdrawn in D11/D21's simplification**. That value no
longer exists. **Corrected**: only `notice` gets a special Raise default. `task`/`issue`/`run_error`/
`config` all default identically — `state='raised'`, `next_action='review'` — no special-casing for
`issue` beyond what already exists generically. This is simpler than what was previously stated, not
a new mechanism.

**`notice`'s default** — `state='closed'`, `next_action=NULL`, set at creation, no second transaction.

**Config vs. code, stated as a judgement call, not asserted as obvious**: this is proposed as a
**code branch** in `raise_new()` (`if type == 'notice': ... else: ...`), not a new config table
mapping type→defaults. Reasoning: there are five types and exactly one behavioural exception among
them — a whole new table for one boolean branch is more machinery than the case warrants
(`feedback_simple_steps_not_engineered_designs`), matching how `_condition_true`'s small fixed
vocabulary is already handled (*"a new condition still needs a code change... which RULE consumes it
is config, the boolean itself is code"*). Flagged as a judgement call because it's a real tradeoff,
not because it's uncertain which way is technically feasible.

**Configs touched:** **(a) new** — none. **(b) validate** — none. **(c) remove** — none. Purely a
code-branch correction/clarification.

---

## D14 — `from_id`/`related_activity`: the mechanism's own configs, gathered into one place

**Never previously given its own register entry** — its content existed only as prose in the design
plan (v3), not itemised here the way D1–D6 were. Closed now:

**New column**: `escalation.from_id INTEGER NULL` — needs its own `cfg_column` row
(`governance.table_columns` applies to this column same as any other):
```
database='iba'  table_name='escalation'  name='from_id'  notnull=0
use='the id of the escalation this item builds on -- optional, mutable (settable on Raise or
  Update alike), paired with related_activity describing the relationship. State of the referenced
  item is irrelevant -- any state is a valid target.'
```

**Validation — the 4 `cfg_escalation_requirement` rows already drafted in the design plan, formally
assigned to this decision now:**
```
action='raise'/'update'  field='from_id'            check_kind='exists'   condition_key='from_id_set'
action='raise'/'update'  field='from_id'            check_kind='not_self' condition_key='from_id_set'
action='raise'/'update'  field='related_activity'   check_kind='paired'   condition_key='from_id_set'
action='raise'/'update'  field='from_id'            check_kind='paired'   condition_key='related_activity_set'
```

**Configs touched:** **(a) new** — 1 `cfg_column` row, 4 `cfg_escalation_requirement` rows (all
above). **(b) validate** — none. **(c) remove** — **none formally**, worth stating plainly: the
earlier `cfg_escalation_link`/`escalation_link_type` proposal (v2) was withdrawn *before* ever being
built, so there is nothing live to retire — a design correction, not a config cleanup.

---

## D28 — `Escalation.ps1`'s `ValidateSet` is a third, disconnected copy of the enum (from chat, formalised)

**The gap**: Python's `_check_next_action_manual`/`_check_next_action_dispatcher` read
`cfg_enum(...)` live — confirmed, this is correct. `Escalation.ps1`'s own `[ValidateSet(...)]` on
`-NextAction`/`-Decision` is a **hardcoded PowerShell literal**, currently matching by coincidence of
having been written correctly at rebuild time, with nothing keeping it in sync if the enum changes
later (exactly what D27 does — its new row wouldn't reach the PS validation at all without a manual
edit).

**Proposed fix**: not a dynamically-querying `ValidateSet` (PowerShell supports this via a custom
`IValidateSetValuesGenerator` class, but that's real additional machinery for a list that changes
rarely — not proportionate). Instead, a **drift-detection check**, same shape as `cfgquality.py`'s
existing orphan-config checks: parse `Escalation.ps1`'s source for its `ValidateSet` literals, compare
against the live `cfg_enum` values for the corresponding group, flag any mismatch. Runs as part of
`configmaint.validate`, same as every other structural drift check in the app.

**Configs touched: N/A** — a code-level consistency check (a new function alongside
`cfgquality.find_orphan_configs()` and its siblings), not a config table change. Correctly parked
alongside D8/D22 in that respect, not a gap in the register.

---

## Everything else

**Unchanged from v6.**
