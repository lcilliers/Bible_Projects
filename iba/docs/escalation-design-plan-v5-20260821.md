# Escalation design plan (v5, 2026-08-21)

Supersedes [`escalation-design-plan-v4-20260821.md`](escalation-design-plan-v4-20260821.md). This
round exists solely to reconcile the plan against
[`escalation-design-decision-register-v9-20260821.md`](escalation-design-decision-register-v9-20260821.md)
— three places where v4 was actively wrong (not just behind), fixed; four decisions v4 predates,
folded in. **Structural change this round, going forward**: this document narrates *why*; the
register is the single source for exact config rows. Where the two would otherwise duplicate content,
this document now points at the register instead of re-copying it — the CSV/vocabulary errors below
happened *because* the same content lived in two places and only one got corrected. Not repeating
that.

---

## What changed from v4 — three corrections, four additions

| # | What v4 said | What's actually true (register v9) |
|---|---|---|
| 1 | `issue` has its own `open`/`decided`/`abandoned` vocabulary, own transition table | **D11/D21**: withdrawn — `issue` reuses the manual vocabulary in full, no separate scheme |
| 2 | `approved` is refused if the same party set `ready_for_approval` (identity check) | **D25**: refused only if the caller isn't who `ready_for_approval` assigned it to (authority check) — same party is fine when that party holds authority |
| 3 | The CSV export is "the flagged-exception rows" | **D4 (corrected)**: the CSV is a raw, unprocessed table dump; exceptions are markdown-only sections |
| 4 | *(absent)* | **D26**: work cannot land on a `raised` item — mechanical guard + the "start work" chat trigger |
| 5 | *(absent)* | **D27**: `ready_for_approval` had no explicit transition row; fixed with one, existing generic rules renumbered |
| 6 | *(absent)* | **D28**: `Escalation.ps1`'s `ValidateSet` is a third, disconnected copy of the enum — a drift check proposed, not a dynamic query |
| 7 | *(absent)* | **D3, answered**: the crash-wrapper itself needs `from_id`-awareness once `from_id` exists, and is one of the `cfg_utility` rows its own rollout has to walk through |

---

## Resources / Purpose / Type of entries

**Unchanged from v3/v4** in substance — five types, each behaviourally distinct, reasoning stands.
**One line corrected**: v2's original claim that `issue` gets a special Raise default (*"opens instead
of defaulting to review"*) referenced the now-withdrawn `open` value — per D12, only `notice` is
special; `issue` defaults exactly like `task`/`run_error`/`config` (`state='raised'`,
`next_action='review'`).

---

## Document integration / Chat capture (D18–D20)

**Unchanged in mechanism** — the produced-documentation-task pattern, the four-document mapping, the
verbatim-quote chat convention all stand. **One wording fix**: D18's `cfg_escalation` rule text said
*"next_action=decided"* — that value no longer exists; corrected to `approved`, the actual terminal
value an issue now reaches via the reused manual vocabulary.

---

## The complete vocabulary — corrected, and now pointing at the register for exact rows

**Dispatcher shape**: unchanged, complete — see v4 for the reasoning (why `revise` resolves
differently there than for manual items), still accurate.

**Manual shape *and* `issue` alike** (D11/D21 — this is the real structural change): both now share
one vocabulary, one set of transition rules, one set of requirement rules. No separate `issue` table.
`approved`'s check is **authority-based** (D25): the party `ready_for_approval` assigned the item to
is who may approve — Claude assigning to itself is a legitimate, visible self-authorisation for items
Claude holds authority over; assigning to the researcher means only the researcher may. `resolution`
is now required at `ready_for_approval` (the readiness check), re-confirmed at `approved` (D25).
`ready_for_approval` itself now has an explicit transition row rather than relying on an incidental
assignee change (D27) — exact priorities and the renumbering this required: register v9, D27.

**`notice`**: unchanged — closes at Raise, never re-enters the decision machinery; disagreement
becomes a new `issue` pointing at it.

**New this round**: an item cannot receive `comment`/`context`/`tried` while still `raised` — a
mechanical guard, plus the researcher's "start work" chat cue moving the state explicitly (D26). Full
config: register v9, D26.

**Exact enum values, transition priorities, requirement rows**: register v9 is now the single source
— not re-listed here to avoid the exact drift that produced this correction round.

---

## The PS front door — exact behaviour, plus one gap not previously named

**Unchanged from v4**: the validation/error-handling/engine-landing description, and the
keep-PS-fix-the-dispatch recommendation (D23) — both still accurate.

**Added**: `Escalation.ps1`'s `ValidateSet` on `-NextAction`/`-Decision` is a third, hardcoded copy of
the vocabulary, alongside the two enum groups Python actually reads live — nothing keeps it in sync
if the enum changes (D27's own fix wouldn't reach it without a manual edit). Proposed as a
drift-detection check in `configmaint.validate`, not a dynamically-querying `ValidateSet` — D28.

---

## Report

**Unchanged from v4/v3 in mechanism** (`cfg_report`/`cfg_report_section`/`cfg_report_csv_table`, the
`run.py` re-plumbing this implies). **The CSV row description was wrong and is corrected**: raw table
dump (`table_name='escalation'`, `virtual=0`), not a computed exceptions view — exact row: register
v9, D4.

---

## Everything else

**Unchanged from v4** — tables and columns, Governance's requirement/response table, control items,
automation, configs cross-check, scripts, validation. Exact config content for anything mentioned here
is in the register, not duplicated a second time in this document going forward.

---

## Summary

Reconciled. Nothing left in this document that contradicts the register. Ready, per the researcher's
own assessment, to move from design to the actual build and migration — starting from
`escalation-design-decision-register-v9-20260821.md` as the operative specification, this document as
the narrative companion.
