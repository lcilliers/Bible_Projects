# Escalation redesign — plan v1 (for review, nothing built yet)

Digested directly from `Workflow/Chat_responses/comments - escalation-system-mechanics`
(2026-08-18) against the live mechanics captured in
[`escalation-system-mechanics-20260818.md`](escalation-system-mechanics-20260818.md). Every
numbered decision below traces to a specific sentence in your review; where you didn't specify
something, it's marked as an **open question**, not assumed. Nothing in this document is built —
this is the plan to approve or correct before any code/schema work starts.

**Scope decision, per your close:** rewrite `escalation.py`/`Escalation.ps1` in place — not a new
ticketing application, not GitHub Issues. Your own words: *"following working through everything, I
think it is feasible, and would be less work to re-write the escalation routine to make it fit for
purpose, rather than implement a new application."*

---

## 1. Corrected purpose (replaces `cfg_table.escalation.use`)

Your wording, to be written into config verbatim as the new `cfg_table` description and
`escalation.control_objectives`/`control_process`:

> **Escalation use:** the only sanctioned researcher interaction. All runtime errors are reported
> in it; both Claude and Researcher record emerging issues, tasks, followups as feedback or to get
> feedback. It is the authoritative record of open items in the project. It will pause a running
> process, and allow it to resume at `resume_point` when answered.

This is broader than the current registration ("a pause, not a fork") — it now explicitly names
*runtime errors*, *feedback in both directions*, and *the authoritative open-items record*, not
only pipeline pauses. That framing drives the rest of this plan.

---

## 2. Core architectural change: `escalation` becomes a current-state view over a real history table

Your diagnosis: *"The lack of a history record is the single most critical failure of this
system... the comment and context in escalation is not cumulative. The full story of the item is
the sum total of all the history rows for the item."*

**Two tables, not one:**

- **`escalation`** — one row per item, **current state only** (exactly as today's table does), plus
  a new `version` column.
- **`escalation_history`** — new, **append-only**, one row per update to an item, ever. Never
  updated or deleted once written.

**Write path changes shape entirely:** every mutating action writes a new `escalation_history` row
first, then a second step re-derives `escalation`'s current-state columns from that latest history
row (your own architecture: *"you will also need a second processor which will be triggered by the
history update, to update the escalation"*). See §6 for the two ways to implement that second step
— needs your call before I build it.

### `id` / `version`

Your spec: *"ID = NNNN-NN: serial number (4 digits) + Version (2 digits), each item runs its own
version increments — this comes from history record."*

**Proposed implementation** (confirm or correct): keep `escalation.id` as today's plain integer
serial PK (unchanged — every existing cross-reference in the app and in prior escalations that
cites `#715` etc. keeps working). Add `escalation.version` (integer, starts at 1, incremented by
the history-write step every time a new `escalation_history` row lands for that id).
`escalation_history` gets its own row PK plus `(escalation_id, version)` as a unique key. The
`NNNN-NN` form is a **display format** (`f"{id:04d}-{version:02d}"`), not a new physical key — e.g.
today's #715 approval would display as `0715-01`, and if you'd been able to add the follow-ups you
tried to add, they'd show as `0715-02`, `0715-03`, etc.

**Open question:** is `NNNN-NN` meant to be the literal stored identifier (a text PK), or is the
derived-display reading above what you intended? I've assumed the latter as the lower-disruption
option — flag if you meant the former.

---

## 3. Column-by-column redefinition

| Column | Lives on | New definition (yours, lightly formatted) |
|---|---|---|
| `id` | `escalation` | Serial number, 4-digit display |
| `version` | `escalation` (new) | Increments per update; sourced from the history record count |
| `source` | `escalation` | What triggered the item: script name \| module \| issue area |
| `at_step` | `escalation` | Only used for pipeline reference, if code-generated |
| `short_description` | `escalation` + `escalation_history` | Label/title — what this item is about |
| `context` | `escalation` (current) + `escalation_history` (every value ever set) | What must be done, or the error message, plus a link to external documents |
| `comment` | `escalation` (current) + `escalation_history` | Additional information for the re-assigned party |
| `tried` | `escalation` + `escalation_history` | Record of the iterations of self-correction |
| `answered_at` | `escalation_history` | **Becomes the history record's own datetime** — no longer a single mutable field on `escalation`; `escalation.answered_at` (if kept at all) just mirrors the latest history row's timestamp |
| `raised_at` | `escalation` | First creation datetime — set once, unchanged |
| `resolution` | `escalation` (current) + `escalation_history` | What was done |
| `related_activity` | `escalation` — **redefined** | Links this item with any other item(s) that relate to it, **by item id** — not a shared free-text label as today |
| `next_action_assigned_to` | `escalation` | Claude / Researcher |
| `answered_by` → **renamed `originator`** | `escalation`, auto-set | Auto-populated from whoever created the latest `escalation_history` row — no longer a value the caller passes by hand |

### `related_activity` — open question

Today it's a shared text label grouping a package of rows (e.g. `operational-behaviour-rules-cfg`).
You've redefined it as **an item id link**. That raises a design fork I don't want to guess on:

- **(a) Single link** — `related_activity` holds one other escalation id (simplest, matches the
  column's current single-value shape, but can't express "this relates to three other items").
- **(b) Real link table** — a new `escalation_link(from_id, to_id, link_type)` table, `link_type`
  drawn from a `cfg_enum` (e.g. `relates-to` / `supersedes` / `duplicate-of` / `blocks`), letting one
  item link to many others with a typed relationship. This is what the existing manual
  chain-by-text-reference pattern (yesterday's `#648→#669→#670→#672→#677→#680→#699→#701`) was
  already straining to do by hand.

I'd lean (b) — it's a small table and it's the one piece of the old design that was visibly
buckling under real use — but this is your call, not mine to assume.

---

## 4. State machine — redefined, decision-response framing removed

Your correction: *"The state machine is currently built around decision response. This must
change. Every step destination is not a decision."* Concretely: states are status, not decision
outcomes — moving to `on-hold`/`re-assign`/`in-progress` should be a direct status change, not
something only reachable via an approve/reject/revise gate.

Seven live states carried forward, redefined per your text:

| State | Meaning (yours) |
|---|---|
| `raised` | New, open item |
| `re-assign` | Mechanism to raise the attention of a party — shows who has responsibility for the current action |
| `on-hold` | Action is paused |
| `in-progress` | Item is worked on; multiple iterations of updates is likely (**this is the state today's history gap broke** — now every one of those iterations is a real `escalation_history` row) |
| `closed` | Item has no actions associated and needs no further attention |
| `completed` | Item's actions have all been fulfilled and validated |
| `withdraw` | Item is no longer required |

`answered` and `paused` — already `inactive=0` in `cfg_enum` today (superseded by `completed`-split
and `on-hold` respectively) — confirmed for removal, not just deactivation, since nothing reads
them live.

### `next_action` (the decision vocabulary) — narrowed

Your replacement, exactly three values:

| Value | Meaning (yours) |
|---|---|
| `approve` | The comment + context is accepted; the re-assigned party can act on the full history context |
| `reject` | The item is rejected; comment + context provide detail for the decision |
| `revise` | This item needs to be revised based on the comment + context |

`hold` dropped as a decision — you noted *"hold is already a state, so does not need to be an
action also."*

**Open question:** `noted` isn't mentioned in your list either way. Today it exists specifically for
"acknowledged, not a real decision" (maps to `state='closed'`). Under the new model, is that need
now covered by directly setting `state='closed'` without going through `next_action` at all (my
reading — matches "every step destination is not a decision"), or do you want `noted` kept as a
fourth `next_action` value? I've assumed **dropped** below; flag if wrong.

`type` — unchanged, you confirmed: *"differentiate the type of item, active list is fine"*
(`task | run_error | issue | notice | config`).

---

## 5. Entry points — what changes

Your comments on §4/§5 of the mechanics report, combined:

- **Code/error entry point** (today: `run.py`'s 3 direct writes + `raise_()`): must be adapted to
  put the right values in the right columns per the redefinitions above — e.g. a runtime error now
  explicitly belongs under the broadened purpose statement (§1), not just a pipeline pause.
- **Terminal/PS entry point**: needs real completeness checks per transaction type before writing —
  today's `Escalation.ps1` only checks "is the parameter present," not "does this transaction type
  actually need it." (§7 below is exactly this table, worked through.)
- **Write path**: every write becomes *write to `escalation_history` first*, not a direct
  `UPDATE escalation`.
- **A second processor**, triggered by the history write, projects the latest history row's values
  onto `escalation`'s current-state columns (and bumps `version`).

---

## 6. The "second processor" — two ways to build it, needs your call

You specified the shape (history write triggers an escalation update) but not the mechanism. Two
real options:

- **(A) Plain Python, same transaction.** Every mutating function does: validate → `INSERT INTO
  escalation_history` → call one shared `_project(escalation_id)` helper that reads the just-written
  history row and does the matching `UPDATE escalation`. No new DB machinery, same pattern the rest
  of the app already uses (`_grant()`, `db.update()`). Simpler, easier to reason about, matches your
  stated preference for simple steps over engineered machinery.
- **(B) A real SQLite trigger** on `escalation_history` (`AFTER INSERT`) that performs the
  `escalation` update itself, so it fires even for a write that doesn't go through
  `lib/escalation.py` (e.g. a stray direct write, if one ever happens again). More robust against
  bypass, but it's the only trigger in either database today, and SQL-side logic is harder to test
  and to extend later (e.g. for the link-table aggregation in §3).

**My recommendation is (A)** — it's simple, testable, and consistent with how every other part of
this app is built; I'd only reach for (B) if you specifically want the guarantee to hold even
against code that doesn't go through the sanctioned functions. Confirm before I build either.

---

## 7. The two tables you asked for

### 7a. Transaction types under the new model (replaces mechanics report §5)

Draft only — column requirements marked `?` are the completeness-check design your §4 comment
asked for, and need your confirmation, not my guess, since getting a required field wrong here is
exactly what broke today.

| Transaction | Valid FROM state(s) | Resulting state | Required fields | Notes |
|---|---|---|---|---|
| Raise | *(new item)* | `raised` | `short_description`, `source`, `type` | `context` optional at raise, addable via Update |
| Decide (was AnswerRun) | `raised` | `completed` (approve/reject) or unchanged-but-flagged (revise — see open question below) | `next_action`, `comment`? | Replaces today's 5-way decision with the 3-way vocabulary in §4 |
| Update / Comment (**new** — doesn't exist today) | `in-progress`, `on-hold`, `re-assign`, any open state | *(unchanged — this is the gap that broke #715)* | `comment` and/or `context` | The missing "add a note while it stays open" action |
| Reassign | any open state | `re-assign` (or stays as-is if you want in-progress items reassignable without losing status — carried from old #677, see §9) | `next_action_assigned_to`, `comment`? | |
| Pause | `raised`, `re-assign`, `in-progress` | `on-hold` | `comment`? | |
| Resume | `on-hold`, `re-assign` | `raised` (or back to prior state — see #677 in §9) | — | |
| Complete | `in-progress` | `completed` | `resolution` | |
| Close | any open state | `closed` | `resolution`? | New direct path, replaces `noted` |
| Withdraw | any open state | `withdraw` | `comment`? | |
| Edit | any open state | *(unchanged)* | `short_description` | Old value now goes into `escalation_history` properly instead of the `tried`-append hack |

### 7b. Column-effect table (per transaction, what gets written where)

This is the "knock-on effect" table you asked for — what a trigger/action must push into
`escalation_history` and which of those values then get projected onto `escalation`. Sketched for
the two most important transactions as a worked example; I'll complete the rest once the table
shape in §7a is confirmed, since every row depends on the vocabulary decided there:

| Transaction | Written to `escalation_history` | Projected onto `escalation` |
|---|---|---|
| Update / Comment | new row: `escalation_id`, `version+1`, `state=<unchanged>`, `comment=<new text>`, `context=<new text or unchanged>`, `originator=<caller>`, `at=<now>` | `escalation.comment`, `escalation.context` (if given), `escalation.version`, `escalation.originator` |
| Decide (approve) | new row: `version+1`, `state='completed'`, `next_action='approve'`, `comment`, `resolution`, `originator`, `at` | `escalation.state`, `next_action`, `comment`, `resolution`, `version`, `originator` |

---

## 8. Code footprint (unchanged from today's actual writers — confirmed via `git log`/grep, not guessed)

Everything that currently writes or reads `escalation` needs to move to the new write path:
`iba/app/lib/escalation.py` (full rewrite), `iba/app/ps/Escalation.ps1` (rewrite — new actions +
real completeness checks per §7a), `iba/app/run.py` (3 direct writes + the `module_blocking`
dispatch-gate query), the 7+ handlers that read `answered_for_run`, `lib/retention.py`,
`tools/purge_word.py`, `migration/legacy_import.py`, and `write_list_report()` (needs to read
current-state from `escalation` but can now optionally show real history per item, which the old
report never could). A migration script backfills one `version=1` `escalation_history` row per
existing `escalation` row as the clean starting point — **not** an attempt to recover what's
already lost, per your own call not to chase that.

---

## 9. Carrying forward two items from your pasted extracts

- **#653** (GOVERNANCE.md §6 stale Yes|No wording) — still an open, unrelated judgement call; not
  part of this redesign, just noting it's still waiting on your confirm/leave-as-is decision.
- **#677** (the reassign/in-progress design gap, and the researcher pushback quoted in it: *"it does
  not make a lot of sense that all progression must go back to a new raise, and reapprove"*) — **this
  redesign resolves it architecturally, not as a separate patch.** Under the new model, Reassign is
  just a status/assignee change recorded in history like any other update — it no longer has to
  discard `in-progress` to move, because there's no more "the row only remembers one current
  decision" constraint once every state really is just current-state-over-history. I'll fold #677's
  three options (a/b/c) into this plan rather than resolving it separately, unless you'd rather
  decide it on its own first.

---

## 10. Open questions — need your answer before I write any code

1. `id`/`version`: derived display format (`NNNN-NN` from integer `id` + integer `version`), or a
   literal stored compound key? (§2)
2. `related_activity`: single-link column, or a real `escalation_link` table with typed
   relationships? (§3)
3. `next_action`: is `noted` fully dropped (direct `state='closed'` instead), or kept as a fourth
   value? (§4)
4. Second-processor mechanism: plain Python projection (A) or a real SQLite trigger (B)? (§6) — my
   recommendation is (A).
5. §7a's transaction table is a first draft — confirm the shape (particularly the new "Update /
   Comment" transaction, which didn't exist before) before I fill in §7b for every row.

Once these are answered I'll write the actual schema DDL, the rewritten `escalation.py`/
`Escalation.ps1`, the migration script, and the call-site updates listed in §8 — as a separate
build step, not folded into this plan.
