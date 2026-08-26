# Full `escalation`/`escalation_history` `cfg_column` extract — every column, live

> Extracted 2026-08-26 for escalation #857, per the researcher's direct correction: the two prior
> extracts (`next_action=review`, `comment`/`context`/`resolution`) picked specific columns rather
> than pulling the whole `cfg_column` set for the `escalation` table first — this fills that gap.
> All 20 `escalation` columns and all 21 `escalation_history` columns, every field, queried live,
> nothing summarised away.

## 1. `escalation` — all 20 columns (ordinal order)

| # | Column | Type | NN | PK | FK | `use` (verbatim) | `expectation` | `filled_by` |
|---|---|---|---|---|---|---|---|---|
| 0 | `id` | INTEGER | Y | Y | | serial PK, 4-digit display; continues from escalations_old's max (735) so ids stay unambiguous across the cutover | | |
| 1 | `version` | INTEGER | Y | | | current version number for this id — count of its escalation_history rows; the NNNN-NN display format is id+version, not a stored key | | raise_new/update |
| 2 | `run_id` | TEXT | | | | restored 2026-08-20 (v1 dropped it, broke dispatch, rolled back — BUILD.md §152/§153). Set for a DISPATCHER-TIED item (a real run.py pause) or a synthetic MANUAL-<timestamp> for a manual item. NULL for neither. | | raise_/raise_new |
| 3 | `source` | TEXT | Y | | | what triggered the item: script name \| module \| issue area. **Immutable after Raise.** | | raise_new |
| 4 | `at_step` | TEXT | | | | pipeline reference, only set if code-generated/run-error. **Immutable after Raise.** | | raise_new |
| 5 | `type` | TEXT | Y | | | differentiates the kind of item | `enum.escalation_type` | raise_new |
| 6 | `short_description` | TEXT | Y | | | label/title. **IMMUTABLE after Raise** — a wrong title is corrected by raising a new item with `state=supersede` on the old one, never edited in place. | | raise_new |
| 7 | `context` | TEXT | | | | what must be done or the error message, **plus links to external documents**. Cumulative: an Update's input is the increment, appended onto the current value. | | raise_new/update |
| 8 | `comment` | TEXT | | | | additional information for the assigned party. Cumulative, same rule as `context`. | | raise_new/update |
| 9 | `tried` | TEXT | | | | the corrective action taken — **REQUIRED when `next_action_assigned_to`=Claude and a prior corrective action failed.** | | update |
| 10 | `state` | TEXT | Y | | | current status — `raised` at Raise; mostly logic-derived on Update per the auto-state rules, some values either-party-settable (`on-hold`/`in-progress`/`closed`). | `enum.escalation_state` | raise_new/update |
| 11 | `next_action` | TEXT | | | | what's expected of the current reader / what the next reader should do — **TWO vocabularies share this column**: dispatcher-tied (`approve/reject/revise/hold/noted`, unchanged) and manual (`ready_for_approval/approved/reject/revise/noted/review`). | `enum.escalation_next_action` | raise_new/update |
| 12 | `next_action_assigned_to` | TEXT | | | | Claude \| Researcher | `enum.escalation_assignee` | raise_new/update |
| 13 | `originator` | TEXT | | | | who created the latest `escalation_history` row — auto-populated, replaces `answered_by`. Not caller-supplied. | `enum.escalation_assignee` | raise_new/update |
| 14 | `resolution` | TEXT | | | | what was actually done — **REQUIRED when `next_action=approved`** (validity check). | | update |
| 15 | `related_activity` | TEXT | | | | free-text field linking this item to any other item(s) that relate to it — plain text, not a structural link table (decided). | | raise_new/update |
| 16 | `raised_at` | TEXT | Y | | | first creation datetime — set once, immutable | | raise_new |
| 17 | `answered_at` | TEXT | | | | mirrors the latest `escalation_history` row's timestamp | | update |
| 18 | `from_id` | INTEGER | | | `escalation.id` | the id this item builds on — optional, **MUTABLE** (settable on Raise or Update alike). Paired with `related_activity`. Sentinel **-1** = audited, no discoverable spawn parent (deliberately non-falsy, distinguishable from NULL/never-checked). Set via `-Action Correction`. | | raise_new |
| 19 | `resolution_kind` | TEXT | | | | `decision_required` or `self_correctable` — required at Raise. `decision_required` is terminal, routes to design; `self_correctable` is fixed directly by Claude, no approval gate. Mutable one direction only: `self_correctable` → `decision_required` via `escalate_to_decision()`, never the reverse. | | `add_resolution_kind_column_v1_20260822.py` |

## 2. `escalation_history` — all 21 columns (ordinal order, **anomaly found — see §3.1**)

| # (ordinal) | Column | NN | FK | `use` (verbatim) |
|---|---|---|---|---|
| 0 | `id` | Y | | surrogate PK, row order = write order |
| 1 | `escalation_id` | Y | `escalation.id` | which item this snapshot belongs to |
| 2 | `version` | Y | | this item's version number at the time of this snapshot |
| 3 | `run_id` | | | snapshot of `escalation.run_id` (constant per item) |
| 4 | `source` | | | delta: NULL after v1 unless corrected — was wrongly NOT NULL under the retired full-snapshot design |
| 5 | `at_step` | | | snapshot of `escalation.at_step` at this version |
| 6 | `type` | | | delta: NULL after v1 unless corrected |
| 7 | `short_description` | | | delta: NULL after v1 unless the title is explicitly corrected (rare, exceptional) |
| 8 | `context` | | | delta: the raw increment THIS version added, NULL if untouched |
| 9 | `comment` | | | delta: the raw increment THIS version added, NULL if untouched |
| 10 | `tried` | | | snapshot of `escalation.tried` at this version |
| 11 | `state` | Y | | snapshot of `escalation.state` at this version |
| 12 | `next_action` | | | snapshot of `escalation.next_action` at this version |
| 13 | `next_action_assigned_to` | | | snapshot of `escalation.next_action_assigned_to` at this version |
| 14 | `originator` | | | who created THIS specific snapshot — the real per-update author, never overwritten by a later row (the #715 loss-of-history fix) |
| 15 | `resolution` | | | snapshot of `escalation.resolution` at this version |
| 16 | `related_activity` | | | snapshot of `escalation.related_activity` at this version |
| 17 | `raised_at` | | | delta, structural: only ever set at v1 |
| **18** | `answered_at` | Y | | THIS row's own write timestamp |
| **18** | `from_id` | | `escalation.id` | Delta: NULL unless THIS version's own transaction set/changed `from_id` — mutable, not structural. -1 is a legitimate value here too. |
| 20 | `resolution_kind` | | | per-version snapshot of `escalation.resolution_kind` at that version |

## 3. Findings from pulling the complete set (not visible from the partial extracts)

### 3.1 `escalation_history.ordinal` is corrupt — `answered_at` and `from_id` both claim ordinal 18; nothing claims 19

Checked live, not assumed: `answered_at` and `from_id` are **both** stored with `ordinal=18`;
`resolution_kind` is `ordinal=20`; **no row holds `ordinal=19`.** `cfg_column.ordinal` exists to
record real column position (per its role everywhere else in the schema) — a duplicate plus a
gap means this table's own self-description of its column order is wrong, most likely from
`from_id`/`resolution_kind` being bolted on later (escalations #763/#822-ish) without their
`ordinal` being set correctly against the live table's actual `PRAGMA table_info` position.

**Confirmed on self-review (2026-08-26), checked against the live DDL rather than left as "not yet
checked":** `PRAGMA table_info(escalation_history)` gives the true, sequential order —
`answered_at`=18, `from_id`=**19**, `resolution_kind`=20. This is not a duplicate-plus-gap
mystery; it is exactly **one off-by-one error**: `cfg_column`'s `from_id` row for
`escalation_history` should read `ordinal=19` and currently reads `18`. A one-row `UPDATE
cfg_column SET ordinal=19 WHERE database='iba' AND table_name='escalation_history' AND
name='from_id'` (via `configmaint.propose`, per `governance.config_control`) would close it
exactly — not a design question, a data-entry fix.

### 3.2 `tried`'s own column description doesn't match its enforced condition wording

`escalation.tried`'s `cfg_column.use` text: *"REQUIRED when `next_action_assigned_to`=Claude and
a prior corrective action failed."* The actual `cfg_escalation_requirement` row (from the prior
extract) is: `action='revise'`, `field='tried'`, `condition_key='claude_revising'`, message
*"tried is required when Claude sets next_action=revise on its own item."* These describe
recognisably related but **not identically worded** triggers — one keyed to
`next_action_assigned_to` state, the other to the action being `revise` plus a `claude_revising`
condition. Whether `claude_revising` is implemented to mean exactly what the column's `use` text
says is a code-level question outside this extract's scope, but the two self-descriptions
disagree on their face — the same shape of drift already caught project-wide by
`governance.rules_must_be_config_driven`'s own review discipline.

### 3.3 `next_action`'s own column definition already names `review` — confirms, doesn't contradict, the earlier finding

Missed in the first (`next_action=review`) extract: `escalation.next_action`'s `cfg_column.use`
text is the **one place in config that actually lists `review` as legitimate** — quoted above in
§1 row 11: *"manual (ready_for_approval/approved/reject/revise/noted/review)."* This should have
been quoted directly as primary evidence the first time, not left to be inferred from the
transition table's absence. It does not change the earlier conclusion — `review` is still named
nowhere in `cfg_enum` or `cfg_escalation_transition` — but the column's own documentation is where
`review` is asserted as valid at all, and that assertion was not previously surfaced.

### 3.4 `cfg_write_grant` — only the `escalation` module itself may write these two tables

```
writer='run',        table_name='escalation',         inactive=1   (retired)
writer='escalation',  table_name='escalation',         inactive=0   (live)
writer='escalation',  table_name='word_registry',      inactive=1   (retired)
writer='escalation',  table_name='escalation_history', inactive=0   (live)
```

`run.py`'s own former direct write grant to `escalation` is retired — consistent with the
dispatcher calling into the `escalation` module's functions rather than writing the table
directly. No gap found here; included for completeness since it's part of what actually governs
writes to these two tables alongside the column-level rules above.

### 3.5 Supporting enums, for completeness

`cfg_enum.escalation_assignee` = `Claude`, `Researcher` (active) — backs `next_action_assigned_to`
and `originator`. `cfg_enum.resolution_kind` = `decision_required`, `self_correctable` (active) —
backs `resolution_kind`. Both are live and correctly populated, unlike `escalation_next_action`
(inactive, per the first extract) and `escalation_state` (active, per the first extract).
