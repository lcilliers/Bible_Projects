# Escalation module — rebuild design (v1, 2026-08-20)

Full reset directed by the researcher after a cascade of defects in one session: `short_description`
column-spec violations (twice), originator misattributed on ≥39 rows, `cfg_escalation` rows claiming
enforcement by a function (`raise_manual`) that no longer exists, `escalation_history` storing
cumulative text instead of per-version deltas, the deep-history report silently dropping 7 of 19
columns, and the entire validate/complete rule engine having no config representation at all
(`iba/docs/escalation-config-review-v2-20260820.md`). Both live tables exported to
`iba/app/db/archive/escalation{,_history}-export-20260820.json` and emptied
(`migration/reset_escalation_tables_20260820.py`).

This is the design before the rebuild, not written after. Every element below is either fixed
(with a stated reason) or explicitly deferred (with a stated reason) — nothing silently dropped.

---

## 1. What changes from the version just retired

| Area | Before (retired) | Now |
|---|---|---|
| `escalation_history` content fields (`comment`/`context`/`resolution`/`tried`) | Full cumulative snapshot every version — the whole running text, repeated and growing | **True delta** — NULL unless this transaction actually set it; the value stored is exactly what the caller supplied, nothing merged in |
| `escalation_history` envelope fields (`state`/`next_action`/`next_action_assigned_to`/`originator`/`answered_at`/`version`) | Always populated | **Unchanged — still always populated.** These describe the transaction's outcome, not accumulated text; a reader needs them on every row to follow the story without scanning backward |
| `escalation.comment`/`.context` (current-state table) | Cumulative, appended | **Unchanged.** Never disputed — cumulative belongs here, per the researcher's own words this turn: "the cumulative is only in escalation" |
| `originator`/`answered_by` | Defaulted to `"Researcher"` in 4 places if not passed | **No default, anywhere.** Required, explicit, every call site — same treatment as `comment` at Raise |
| State-derivation priority rules | Hardcoded `if`/`elif` chain, no config, no way to inspect or change the order without editing Python | **Config-driven**: new `cfg_escalation_transition` table, evaluated in priority order, target status resolved via the already-built `_status_for()`/`cfg_status_flow` lookup |
| Field-requirement rules (comment@Raise, resolution@approved, state@reject, tried@Claude-after-failure) | Hardcoded checks scattered through 3 functions; `tried`'s rule was never even implemented | **Config-driven**: new `cfg_escalation_requirement` table, one `_check_requirements()` call site |
| Two-stage approval (`ready_for_approval` → `approved`) | No check that the two parties differ | **Enforced**: `update()` looks up the last `ready_for_approval` row's `originator`; rejects `approved` from the same party |
| `cfg_escalation`'s stale `enforced_by` claims | 2 of 7 rows named `raise_manual`, a function deleted in the last redesign | **Corrected** to name what actually enforces each rule today, or state plainly that nothing does |
| Deep-history report | 6 of 19 columns shown; `comment` shown as the (wrongly cumulative) full text | **All columns**, delta fields clearly labelled as "set this version" and omitted (not blanked) when NULL |
| `cfg_write_grant` orphans (`escalation`→`word_registry`, `run`→`escalation`) | Both dead, found in `#755`/`#750`, never cleared | **Cleared** as part of this rebuild |
| `escalation_next_action` enum's dispatcher/manual vocabulary merge, duplicate ordinal, dispatcher path not consulting the enum | Flagged in `#755` finding 2, not fixed | **Fixed**: enum split into two named groups the code actually validates against per shape |

---

## 2. Schema

### 2.1 `escalation` / `escalation_history` — no column changes

Same 18/19 columns as before. Only the *write semantics* of `escalation_history`'s content fields
change (§1). `_COLS` in code stays the same tuple; what goes into it per-call changes.

### 2.2 New: `cfg_escalation_transition` — the state-derivation rule table

```sql
CREATE TABLE cfg_escalation_transition (
    priority INTEGER NOT NULL,
    shape TEXT NOT NULL,              -- 'manual' | 'dispatcher'
    next_action TEXT,                 -- a value from cfg_enum('escalation_next_action'), or NULL = any
    condition_key TEXT NOT NULL,      -- named condition, see §2.4
    resulting_status_key TEXT NOT NULL,   -- substring matched against cfg_status_flow.set_by
    notes TEXT,
    active INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (shape, priority)
)
```

Evaluated in `priority` order (ascending, first match wins) per shape. This is a genuine rules
table — `_derive_state()`/`_terminal_state_for()` become a loop over it, not an `if`/`elif` chain.
Editable via `configmaint.propose` from here on, same as any other `cfg_*` row.

### 2.3 New: `cfg_escalation_requirement` — the field-requirement rule table

```sql
CREATE TABLE cfg_escalation_requirement (
    action TEXT NOT NULL,             -- 'raise', or a next_action value
    field TEXT NOT NULL,              -- the column that must be filled in
    condition_key TEXT NOT NULL,      -- 'always', or a named condition (§2.4)
    message TEXT NOT NULL,            -- shown to the caller on violation
    active INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (action, field)
)
```

### 2.4 Named conditions — the fixed, small vocabulary both tables reference

A closed set of booleans the code already computes from its inputs — not a general expression
language (that would be over-engineering for ~8 conditions that never change shape). Config names
*which* one applies and in what order; code supplies the actual boolean:

`always` · `has_resolution` · `is_reject` · `is_revise` · `is_noted` · `is_approved` ·
`assignee_changed` · `assignee_unchanged_or_none` · `assigned_to_claude_after_failed_tried`

Adding a genuinely new condition still needs a code change (a new named boolean) — but the RULE
that consumes it (which action, what priority, what resulting status, what message) is config from
that point on, matching every other `cfg_*`-driven part of this app (`cfg_on_fail`, `cfg_step`).

---

## 3. Field-by-field: what's a delta, what's an envelope, in `escalation_history`

| Field | Kind | Populated when |
|---|---|---|
| `id`, `escalation_id`, `version` | structural | always |
| `state`, `next_action`, `next_action_assigned_to`, `originator`, `answered_at` | envelope | always — the outcome of this transaction |
| `comment`, `context`, `resolution`, `tried` | delta | only if the caller supplied a value this call; else `NULL` |
| `short_description` | delta, rare | only at creation (v1), or an explicit title-correction transaction |
| `source`, `at_step`, `type`, `run_id`, `related_activity`, `raised_at` | delta, structural | only at creation (v1), or when `related_activity` is explicitly updated (the one field of this group `update()` allows changing) |

Reconstructing "what did the item look like as of version N" is `escalation_history`'s job read
as a fold — the row at N plus every non-NULL delta at or before N for content fields, envelope
fields taken straight from row N. `escalation` (current state) is exactly this fold already
materialised. Neither report needs to *perform* the fold — the fold is `escalation`; the history
report's job is showing what changed at each step, which is what a delta already is directly.

---

## 4. Reports

### 4.1 Deep-history report (`write_history_report`, `-Action History`)

Per version: envelope fields always shown (`state`, `next_action`, `next_action_assigned_to`,
`originator`, `answered_at`); each delta field shown ONLY when non-NULL, clearly labelled ("set
this version", not "the story so far"). `short_description` shown once per version it actually
changed (not once at the top, since a title can now legitimately be corrected mid-thread).

### 4.2 Open-items report (`write_list_report`, `-Action List`)

Same per-version table as today, but the `comment` column becomes "what changed" (the delta, blank
when this version didn't touch it) instead of a gist of the wrongly-cumulative text.

Both keep going through `reportkit`/`cfg_report` — deferred from `#755` finding 3 (holding until the
schema/logic rebuild lands, so the report-registration work isn't done twice against a shape about
to change underneath it); registered as the next piece of work once this rebuild is verified.

---

## 5. Validation rules, concretely (what `cfg_escalation_requirement` will hold)

| action | field | condition | 
|---|---|---|
| raise | comment | always |
| raise | short_description | always (shape-checked by `_title_shape_error`, unchanged from `#759`) |
| approved | resolution | always |
| reject | state | always (must resolve to `withdraw`/`supersede`, enum-validated separately) |
| update (any) | tried | assigned_to_claude_after_failed_tried |

---

## 6. `originator`/`answered_by` — no default, root cause closed

Four call sites lose their `"Researcher"` default: `Escalation.ps1`'s `-AnsweredBy` becomes
`Mandatory`; `answer_for_run()`'s `answered_by` parameter loses its default; both CLI dispatch
fallbacks (`originator or "Researcher"`) become `originator` required, `ValueError` if absent. This
is the actual mechanism fix for the bug that triggered this whole rebuild (≥39 misattributed rows) —
not a reminder to "remember the flag," a wall that makes forgetting it impossible.

---

## 7. Two-stage approval — separation of duties enforced

`update()`, when `next_action='approved'`: looks up the most recent history row for this item with
`next_action='ready_for_approval'`; if its `originator` equals the current call's `originator`,
reject with a clear message ("the same party cannot both request and confirm their own approval").

---

## 8. `cfg_escalation` corrections

`document_reference_grouping` and the `raise_manual` half of `source_classification`:
`enforced_by` corrected to state plainly that nothing currently enforces them (matching the honest
`"session practice ... not mechanically enforced"` wording already used for 3 of the other 5 rows),
until/unless a real check is built. No claim left pointing at dead code.

---

## 9. `cfg_write_grant` / `cfg_enum` cleanup

- `cfg_write_grant(writer=run, table_name=escalation)` — retired (`#750`).
- `cfg_write_grant(writer=escalation, table_name=word_registry)` — retired (`#755` finding 4).
- `escalation_next_action` — split into two enum groups the code actually validates against:
  `escalation_next_action_dispatcher` (`approve|reject|revise|hold|noted`) and
  `escalation_next_action_manual` (`ready_for_approval|approved|reject|revise|noted|review`).
  `answer_for_run()` validates against the dispatcher group (closing the "hardcodes its own tuple"
  gap); `update()` validates against the manual group. Fixes the duplicate-ordinal/skipped-ordinal
  data bug found in `#755` at the same time (new groups seeded clean).

---

## 10. Explicitly deferred, and why

- **Full `reportkit`/`cfg_report` registration for the two reports** (`#755` finding 3) — the report
  *content* is changing in this rebuild (§4); registering it now means registering it twice. Next
  piece of work once this lands, not dropped.
- **A general condition/expression language for `cfg_escalation_transition`** — the 9 named
  conditions in §2.4 cover every rule this module actually has; a generic evaluator would be
  building for requirements that don't exist yet (`feedback_simple_steps_not_engineered_designs`).
- **Auto-escalating every standalone-CLI module's crashes**, not just this one (`#755` finding 2's
  wider half) — `escalation.py`'s own CLI already got this fix; extending it to every other
  standalone module in the app is a separate, larger inventory, out of scope for an escalation-
  module rebuild specifically.

---

## 11. Test plan (run before reporting this done, not after)

1. Every `cfg_escalation_transition`/`cfg_escalation_requirement` row exercised at least once:
   raise → revise → noted; raise → reject/withdraw; raise → reject/supersede; ready_for_approval →
   approved (two different parties); ready_for_approval → approved (SAME party, must reject);
   assignee change with no other action → re-assigned; dispatcher hold/noted/approve.
2. `escalation_history` delta correctness: a 3-call sequence (comment only, then context only, then
   both) must show exactly one non-NULL field per row where expected, envelope fields present on
   all three.
3. `originator` omitted anywhere → `ValueError`, no silent default, checked at every call site
   (`raise_new`, `update`, `answer_for_run`, both CLI dispatch paths).
4. Both reports render against a fresh multi-item, multi-version dataset; every column verified
   present/absent correctly per §3's table.
5. `cfg_write_grant`/`cfg_enum` changes: confirm `may_write()` still resolves correctly for
   `escalation`/`escalation_history`/`word_registry` cases; confirm both enum groups validate the
   right vocabulary and reject the other shape's values.
