# Escalation utility — config review v2 (2026-08-20)

**Supersedes [`escalation-config-review-v1-20260820.md`](escalation-config-review-v1-20260820.md)
in scope, not in the 4 findings it already made** — those stand. v1 asked "does every `cfg_*` table
have rows and are they used" and found 4 specific gaps. It never asked the actual question: **is
the operational rule set that governs *validating* and *completing* an escalation — and the
automation that executes it — represented in config at all.** It is almost entirely not, and v1
didn't report that. This is the redo, done as a rule-by-rule inventory of `iba/app/lib/escalation.py`
against what's in config, not a table-presence checklist.

---

## Method

Read every function in `escalation.py` (609 lines, current as of this pass) line by line. For every
distinct rule it enforces — a required field, a state transition, a default, a validation — recorded:
what the rule is, where it lives (file:line), and whether ANY `cfg_*` row drives it, is merely
described by it (text only, not read by code), or has no config presence whatsoever.

---

## Inventory

### A. Field-requirement rules (what must be filled in for a given action)

| Rule | Enforced at | Config? |
|---|---|---|
| `comment` required at Raise | `raise_new():313-314`, hardcoded `if not comment: raise` | **No** |
| `short_description` must be ≤60 chars, one line, no `--` | `_title_shape_error():119-138` (escalation #759, built this session) | **No** — `_TITLE_MAX_CHARS=60` is a Python constant |
| `resolution` required when `next_action=approved` | `update():382-383`, hardcoded | **No** |
| `state` must be `withdraw`\|`supersede` when `next_action=reject` | `_derive_state():351-355`, hardcoded | **No** |
| `tried` required when `next_action_assigned_to=Claude` after a failed correction (plan v1/v2 comments — the researcher's own spec) | **nowhere** | **No** — not even implemented in code, let alone config. A designed rule that was never built at all. |
| `originator` required (must resolve to Claude\|Researcher) | `_check_assignee():104-113` | **Partial** — the valid VALUE SET is `cfg_enum('escalation_assignee')` (config-driven); that it's *required*, and the `.strip().capitalize()` normalisation, are hardcoded |

### B. State-derivation rules (which `next_action`/condition produces which `state`)

| Rule | Enforced at | Config? |
|---|---|---|
| The **target status value** for each of 8 derivation outcomes (raised/in-progress/on-hold/re-assigned/closed/withdraw/supersede/completed) | `_status_for()` lookups throughout `_derive_state()`/`_terminal_state_for()`/`raise_new()`/`raise_()` | **Code, with fallback** — `cfg_status_flow` rows exist in the schema for this (escalation #755 finding 1) but the 8 rows for `entity='escalation'` are still unapproved, blocked behind `#756`. Even once approved, this only fixes the TARGET VALUE, not the next row down. |
| The **priority-ordered rule structure itself** — which condition (`next_action=approved`+resolution, `=reject`, `=revise`, `=noted`, assignee-changed, else) fires, and in what order when more than one could match | `_derive_state():349-362`, a hardcoded `if`/`elif` chain | **No, and cannot be with the current schema** — `cfg_status_flow` is a flat `(entity, status, set_by)` table; it has no column for a *condition* or a *priority*. Populating it (per v1's own finding-1 proposal) closes NONE of this — the branching logic stays 100% Python either way. |
| Dispatcher-tied decision → state mapping (`hold`→on-hold, `noted`→closed, else→completed) | `_terminal_state_for():209-218` | Same as above — target values partially config-backed once `#756` clears, the `if`/`elif` branching is not and cannot be with this schema |

### C. Two-stage approval semantics (the actual workflow, not just its output states)

| Rule | Enforced at | Config? |
|---|---|---|
| `ready_for_approval` → `approved` → `completed` is a two-party handshake (requester sets the first, a *different* party the second) | Plan v3 §2 (a **doc**), and `_derive_state()`'s branches implement the two OUTCOMES — but **nothing checks the two parties are actually different**. `update(next_action='approved', ...)` succeeds even if the same identity that set `ready_for_approval` also sets `approved` in the next call. | **No** — not in config, not even in code. A design intent stated in the plan doc with zero enforcement anywhere. |
| Which `next_action` values belong to the manual vocabulary vs the dispatcher-tied vocabulary | `cfg_enum('escalation_next_action')` holds all 8 values undifferentiated (escalation #755 finding 2, unresolved) | **No** — flagged in v1, still open |

### D. Automation / dispatch rules (`cfg_escalation`'s own 7 rows)

This table exists specifically to hold rules like these — checked whether it's current, not just
whether it has rows (v1 only checked the latter).

| `rule_key` | `enforced_by` claims | Actually true? |
|---|---|---|
| `duplicate_suppression` | `escalation.open_duplicate` | **True** — grepped: called from `handlers/configmaint.py:311,394`, real and live |
| `module_blocking` | `run.py` since #646 | **True** — `run.py:135-154`, confirmed live this session (it's what blocked 8 of my own config proposals) |
| `resolution_precedence` | "session practice ... not mechanically enforced" | Honest about being unenforced |
| `chat_routing` | "session practice ... not mechanically enforced" | Honest about being unenforced |
| `document_reference_grouping` | **"escalation.raise_manual"** | **False.** `raise_manual()` does not exist anywhere in the current codebase — grepped, zero hits outside old migration-script comments. It was fully replaced by `raise_new()` in this redesign, which has NO equivalent check. This rule currently has **zero enforcement**, not the enforcement its own config row claims. |
| `source_classification` | `escalation.raise_ / raise_manual` | **Half-false**, same reason — the `raise_manual` half is dead |
| `full_path_file_references` | "not mechanically checked" | Honest about being unenforced |

`#746` (open, assigned Claude) already flagged this table as "still describes the pre-redesign
single-table mechanism" in general terms. This pass makes it concrete: 2 of 7 rows actively lie
about what enforces them.

### E. Defaults with no justification anywhere (config or code)

The bug that triggered this whole redo: `originator`/`answered_by` defaults to `"Researcher"` in
**four separate hardcoded locations** — `Escalation.ps1:88` (`$AnsweredBy = 'Researcher'`),
`escalation.py:286` (`answered_by: str = "Researcher"`), and two CLI fallbacks (`escalation.py:573,
588`, `originator or "Researcher"`). No config row states or justifies this default. It has no
basis — Claude runs this CLI as often as the researcher does — and it silently misattributed
**≥39 history rows this session alone** (38 found earlier this turn, plus `#753` v4 itself,
written moments before this report, still wrong).

### F. Dead code found in the same pass (not a config gap, but found while reading every line)

- `_resolve_id()` (`escalation.py:280-282`) — defined, never called anywhere in the codebase.

---

## What this means

Populating `cfg_status_flow` (v1 finding 1, still blocked behind `#756`) would fix **one row of
table B** — the target status *values*. It does nothing for: the priority-ordered branching logic
(B), the two-party handshake check (C), the stale/false `enforced_by` claims (D), or the
unjustified default that just caused a real, repeated, live data-integrity failure (E). Building
the raise-time title guardrail (`#759`) fixed exactly one symptom (a bad title) the same way —
real, tested, but a fix at the point a violation would show up, not at the mechanism that let
untracked rules exist in the first place.

Per `cfg_behaviour_rule` (class=`development`, `rule_key=root-fix-not-one-off`): *"A defect that is
an instance of a class ... is fixed at the shared mechanism so every future case is correct, not
remediated case-by-case while the mechanism stays broken."* Every fix this session on this module
has been case-by-case. The shared mechanism — a config representation for validate/complete rules
that code actually reads, the way `cfg_on_fail` drives `run.py`'s path routing or `cfg_step` drives
its handler resolution — does not exist for this module at all.

## Not proposed here

A concrete schema/design for that shared mechanism is the next step, not this document — this is
the inventory the design has to be built against, following this project's own established
practice for this exact module (three review rounds, v1→v2→v3, before anything was built the first
time). Producing a v1 design proposal is the next piece of work, pending your direction on scope.
