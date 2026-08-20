# Escalation redesign — plan v2 (rethought around two transactions)

v1: [`archive/escalation-redesign-plan-v1-20260818.md`](archive/escalation-redesign-plan-v1-20260818.md).
Digested from your second round of comments, appended to `Workflow/Chat_responses/comments -
escalation-system-mechanics`. This is a substantial rethink, not a patch on v1 — the biggest
change: **there are only two transaction types, `Raise` and `Update`** (your words: *"In principle
there are only two transaction types. The resulting state will be determined by the values in the
fields."*), replacing v1's ten separate named actions with a rules-driven single `Update` path. §7
below is a worked, step-by-step illustration of that, as requested.

---

## 0. What changed from v1, at a glance

| Area | v1 | v2 |
|---|---|---|
| Transaction types | 10 named actions (Answer/AnswerRun/Reassign/Pause/Resume/Retract/Complete/Edit/...) | **2**: `Raise`, `Update` — resulting state derived from field values, not the verb called |
| History row shape | Only the columns that changed | **Full snapshot** — every column's value at that version, unchanged fields carried forward from current `escalation` |
| `related_activity` | Open question: single link vs. link table | **Decided: plain free-text information field**, no structural linking, not now |
| `id`/`version` | Open question | **Decided: two real columns, `NNNN-NN` is a derived display format** — confirmed, matches v1's recommendation |
| `next_action` | approve / reject / revise (3) | **approve / reject / revise / noted / review (5)** — `review` is new: raising/reassigning something asks the assignee to act |
| States | 7 (raised, re-assign, on-hold, in-progress, closed, completed, withdraw) | **8** — added `supersede` |
| `short_description` | Editable via `Edit` action | **Immutable after Raise** — no edit path in the new model (flagged explicitly below, §3) |
| Projection mechanism | Open question (Python vs. trigger) | **Decided: whichever fits the tech better, but both writes must succeed together or neither does** — resolved as one atomic transaction, §8 |

---

## 1. Purpose — unchanged, confirmed correct in v1

> **Escalation use:** the only sanctioned researcher interaction. All runtime errors are reported
> in it; both Claude and Researcher record emerging issues, tasks, followups as feedback or to get
> feedback. It is the authoritative record of open items in the project. It will pause a running
> process, and allow it to resume at `resume_point` when answered.

---

## 2. `escalation` + `escalation_history` — the snapshot model, corrected

You disagreed with v1's partial-column history design: *"the history record include all the fields
set in the transaction, including the auto generated fields. fields that is not set because they
do not change and are not included in the input is derived from the current escalation record."*

**Corrected model:** every `escalation_history` row is a **complete snapshot** — all columns, every
time. When a transaction supplies a value for a field, that value goes into the new row; every
field the transaction didn't touch is carried forward unchanged from the current `escalation` row.
`escalation` itself always holds exactly the latest snapshot (i.e. it's redundant with the newest
`escalation_history` row by construction — that redundancy is deliberate, so every existing reader
of `escalation` keeps working unmodified).

This also reconciles something that looked like a contradiction between your two comments:
- Round 1: *"the comment and context in escalation is not cumulative — the full story is the sum of
  the history rows."*
- Round 2: *"context/comment — provide incremental updates... if not null, escalation will add it to
  the previous [value]."*

Read together: **you only ever type the new increment.** The system appends it onto the current
full value to produce the new current value — so `escalation.context`/`comment` end up holding the
complete running text (not just the latest fragment), and each `escalation_history` snapshot
naturally carries that same complete text at its point in time. Both statements are describing the
same design from two ends: input is incremental, storage is cumulative, at every layer.

---

## 3. Column-by-column — corrected (added the two you flagged as missing: `state`, `next_action`)

| Column | Immutable after Raise? | Update behaviour |
|---|---|---|
| `id` | yes (auto) | Serial, 4-digit display |
| `version` | yes (auto, per-row) | Increments every `escalation_history` write for this id |
| `source` | **yes** | What triggered the item: script name \| module \| issue area |
| `at_step` | **yes** | Only set if code-generated/run-error; blank otherwise |
| `short_description` | **yes** | Label/title — **no longer editable after Raise** (see callout below) |
| `state` | no | See §4 — mostly logic-derived, some values either-party-settable |
| `next_action` | no | See §5 — five values, drives the auto-state rules |
| `context` | no | Cumulative — new text appended to current value (§2) |
| `comment` | no | Cumulative — new text appended to current value (§2) |
| `tried` | no | Conditionally required (§6) — the corrective action taken |
| `answered_at` | no | Set by code on every update — the current row mirrors the latest history row's timestamp |
| `raised_at` | yes (auto) | Set once, at Raise |
| `resolution` | no | Conditionally required (§6) — what was actually done |
| `related_activity` | no | **Decided: plain free-text information field**, not a structural link — optional |
| `next_action_assigned_to` | no | Claude / Researcher — unspecified on Update = stays with current owner |
| `originator` (was `answered_by`) | no | Auto-populated: whoever created the latest history row |

**Callout — `short_description` is now immutable.** This is a real behaviour change from today's
system (which has a dedicated `Edit` action). Under the new model there is no path to correct a
typo or reword the title after Raise — the title becomes a fixed identity field, same tier as
`source`/`at_step`. I'm carrying this forward as decided since you listed it explicitly among the
"cannot be edited by Update" fields, not flagging it as an open question — but naming it plainly
here in case it wasn't meant to be a permanent lock.

---

## 4. States — 8 total, `supersede` added

| State | Meaning | Who can set it |
|---|---|---|
| `raised` | New, open item | System, at Raise only |
| `re-assign` | Attention/responsibility handed to the other party | **Open question — not bucketed in your either-party/logic-only lists, see §9.1** |
| `on-hold` | Action is paused | Either party |
| `in-progress` | Item is being worked; multiple update iterations expected | Either party, or logic (`next_action=revise`) |
| `closed` | No further action needed | Either party |
| `completed` | All actions fulfilled and validated | **Logic only** (`next_action=approve`) |
| `withdraw` | No longer required | **Logic only** (a `reject` outcome — see §9.2) |
| `supersede` | Replaced by other work | **Open question — new state, trigger not yet specified, see §9.3** |

`answered` and `paused` (already `cfg_enum`-inactive today) are dropped entirely, confirmed.

---

## 5. `next_action` — 5 values, with the new `review`

| Value | Meaning |
|---|---|
| `approve` | The comment + context is accepted; the assigned party can act on the full history context |
| `reject` | The item is rejected; comment + context provide the detail |
| `revise` | This item needs revision, based on the comment + context |
| `noted` | Information-only update, no action required — pairs with `state=closed` |
| **`review`** *(new)* | Triggers the assigned party to act on the item — this is the Raise-time default |

### Auto-state rules (yours, restated precisely)

| Condition | Resulting `state` |
|---|---|
| `next_action = approve` | `completed` — **requires `resolution` to be filled in** |
| `next_action = revise` | `in-progress` |
| `next_action = reject` | A terminal, non-`completed` outcome — **needs your clarification, §9.2** — **requires `comment`** |
| `state` set directly to `re-assign` | The history row for that update must record its own `originator` correctly — **wording needs your confirmation, §9.4** |

---

## 6. The two transactions, in full

### Auto-generated fields (system-set, never caller-supplied)
`id`, `version`, `raised_at`.

### Logic-generated fields (system-set, conditional)
`at_step` — only populated if the item is run-error/code-generated.

### `Raise` — new item

| | |
|---|---|
| **Required** | `short_description`, `source`, `type`, `comment` (minimum: what the item is about) |
| **Optional** | `context`, `related_activity` |
| **Defaults** | `next_action_assigned_to` → `Claude`; `next_action` → `review` |
| **Blank at creation** | `tried`, `answered_at`, `resolution`, `originator` |
| **Resulting state** | `raised` |
| **Resulting operation** | *Alert `next_action_assigned_to`* — see §9.5, no concrete mechanism decided yet |

### `Update` — every subsequent change, on any open state

| | |
|---|---|
| **Required** | The item's `id`. Every other field only needs a value if it's changing — anything omitted keeps its current value (§2) |
| **Cannot be touched** | `source`, `at_step`, `version`, `short_description` |
| **Auto-set by code** | `originator` (whoever is making this call), `version` (+1), `answered_at` (now) |
| **`context`/`comment`** | Appended onto the current value, not replacing it (§2) |
| **`related_activity`** | Free-text, optional |
| **`next_action_assigned_to`** | Omitted → stays with current owner. Given → control passes to the new party |
| **`tried`** | **Conditionally required**: if `next_action_assigned_to = Claude` and a prior corrective action failed, this field must hold what was tried |
| **`resolution`** | **Conditionally required**: whenever `next_action = approve` |
| **Feedback-request pattern** | To ask the other party for clarification: set `next_action = revise` and `next_action_assigned_to` to the other party, with `comment`/`context` stating what's needed |

Two standing rules you restated, carried forward as governance (not new mechanics — already true
today via `cfg_escalation.chat_routing`/§9's `resolution_precedence`, just reaffirmed for the new
system):
- *"Claude will channel all requests for action from researcher through escalations."*
- *"Nothing is signed off until researcher has approved and resolution is filled in."* — this reads
  to me as implying `next_action=approve` may be **researcher-only**, not something Claude sets on
  its own items. Flagged as an open question, §9.6 — I don't want to silently build an access
  restriction you didn't explicitly state as one.

---

## 7. Worked illustration — one item, start to finish

You asked the plan to *illustrate how the changes will be handled*. Here's a single item run through
the full lifecycle, showing exactly what lands in `escalation` (current state) vs.
`escalation_history` (every snapshot) at each step. Field values omitted from a step's "caller
supplies" column simply carry forward unchanged, per §2/§6.

**Step 1 — Raise.** Claude raises an item about a failed script.

> Caller supplies: `short_description="word_full_extract.py throws on H1234"`,
> `source="scripts/word_full_extract.py"`, `type="run_error"`, `comment="ValueError at line 210,
> full traceback in context"`, `context="<traceback>"`.
> System fills: `id=0900`, `version=1`, `raised_at=2026-08-19T09:00:00Z`, `next_action_assigned_to=
> Claude` (default), `next_action=review` (default), `state=raised`.

| Table | Row after step 1 |
|---|---|
| `escalation` | `id=0900, version=1, state=raised, next_action=review, next_action_assigned_to=Claude, comment="ValueError at line 210, full traceback in context", context="<traceback>", short_description="word_full_extract.py throws on H1234", originator=Claude` |
| `escalation_history` | One row, `escalation_id=0900, version=1`, identical full snapshot of the above |

**Step 2 — Update (Claude tries a fix, it fails).** Claude supplies: `tried="patched the None
check at line 210, re-ran — same error at a different line (244)"`.

| Table | Row after step 2 |
|---|---|
| `escalation` | `version=2`, `tried="patched the None check..."` (new), everything else carried forward from v1 |
| `escalation_history` | New row, `version=2`, full snapshot including the carried-forward `comment`/`context`/`short_description` unchanged, `tried` now set |

**Step 3 — Update (Claude asks the researcher for input).** Claude supplies: `next_action="revise"`,
`next_action_assigned_to="Researcher"`, `comment="second failure looks like a data issue, not code
— can you confirm H1234's verse span is intact before I keep patching?"` (appended to the existing
comment, per §2).

| Table | Row after step 3 |
|---|---|
| `escalation` | `version=3`, `state=in-progress` (auto, `revise` rule), `next_action=revise`, `next_action_assigned_to=Researcher`, `comment=<v1 text> + <v3 addition>` |
| `escalation_history` | New row, `version=3`, full snapshot |

**Step 4 — Update (Researcher approves, work is done).** Researcher supplies: `next_action=
"approve"`, `resolution="confirmed H1234's span was truncated by the 07-19 backfill; re-ran the
gap-fill, script now completes clean"`.

| Table | Row after step 4 |
|---|---|
| `escalation` | `version=4`, `state=completed` (auto, `approve` rule — `resolution` present, so valid), `resolution=<text>`, `originator=Researcher` |
| `escalation_history` | New row, `version=4`, full snapshot — final state |

**What this fixes, concretely:** every one of the 4 steps above is a real, separate, permanently
readable row in `escalation_history`. Today's system would have overwritten `comment` at step 3 and
`resolution`/`state` at step 4, with step 2's `tried` note visible only until the next write — this
is exactly the shape of loss that happened to escalation #715.

---

## 8. Processing pipeline + atomicity

Both `Raise` and `Update` follow the same sequence:

1. **Validate** — required fields present for the transaction type (§6); conditional requirements
   checked (`tried`/`resolution` per their trigger conditions).
2. **Merge** — build the full new snapshot: caller-supplied fields as given, everything else copied
   from the current `escalation` row (or defaulted, for `Raise`).
3. **Apply auto-state rules** (§5) — derive `state` from `next_action` where applicable.
4. **Write** `escalation_history` (the new full snapshot, next `version`).
5. **Project**: `escalation` is updated to match the row just written.

On your open question about mechanism (Python projection vs. a real trigger) — your answer was
*"depends on what works better within the chosen technology, [but] script success is based on both
routines ran successfully."* That's an atomicity requirement, not a mechanism choice: whichever way
it's implemented, steps 4 and 5 must commit together or not at all — a failure partway through must
never leave `escalation_history` with a row that `escalation` doesn't reflect, or vice versa.
**Concretely: both writes wrapped in a single SQLite transaction, one commit.** I'd still do this in
plain Python (matches every other write pattern in the app, easiest to test) rather than a trigger,
but the atomicity guarantee is the same either way — flag if you specifically want the trigger form
for a different reason (e.g. protecting against a future direct write that bypasses the sanctioned
function entirely).

---

## 9. Open questions — genuinely unclear from the text, need your answer before I build

1. **`re-assign` state — who can set it?** Not listed among "either party" or "logic only." Is
   moving an item to `re-assign` a direct action either party takes (like `on-hold`), or does it
   only happen as a side-effect of changing `next_action_assigned_to`?
2. **The `reject` rule reads as self-contradictory as written**: *"when next_action = reject then
   state must be completed and be either withdraw or supersede."* `completed`, `withdraw`, and
   `supersede` are three different values in your own §4 list — a single `state` column can't hold
   all three. My best reading: `reject` always lands on a **terminal** state, and specifically
   either `withdraw` or `supersede` (never literally `completed`, which is reserved for `approve`).
   Confirm or correct.
3. **`supersede` — what triggers it, mechanically?** Is it a value the rejecting/raising party picks
   explicitly (a third option alongside `withdraw` at reject-time), or is it system-derived from
   something else (e.g. a newer item referencing this one via `related_activity`)?
4. **"When state = re-assign, the next history record must have originator = re-assign of the
   current record"** — I read this as: the history row created by the reassignment itself must
   record its `originator` as whoever *performed* the reassignment, not the newly assigned party
   (ordinary `originator` semantics, just restated for this case). Confirm that's what you meant —
   the sentence is genuinely ambiguous to me as written.
5. **The "alert `next_action_assigned_to`" operation on Raise has no mechanism yet.** Per the
   mechanics report (§9 of that document), there is currently no push/notification channel anywhere
   in this app — only session-start polling (`start-project` reading the list report) and the
   dispatch-blocking gate. Do you want an actual notification mechanism built as part of this
   redesign (and if so, what — a file, a flag Claude's session-start check treats as urgent,
   something else?), or is "alert" satisfied by making `-Action List`/the report surface `review`-
   flagged items more prominently than today? I'd rather not invent a delivery mechanism you didn't
   ask for.
6. **Is `next_action = approve` Researcher-only?** Your phrasing ("nothing is signed off until
   researcher has approved") reads that way to me but doesn't say so explicitly as an access rule.
   If yes, I'll build it as a hard check (Claude-originated `approve` refused); if it's just
   describing today's normal usage pattern rather than a rule to enforce, I won't restrict it.

---

## 10. #653 / #664 — a correction, checked live just now

Your comment: *"#653 can you explain why the yes/no wording is still causing an issue and remain
open."* I queried both ids directly in `iba.db` before answering, rather than trust either your
pasted extract or my own prior summary:

- **#653, live today, is a different item entirely** — "retirement of research_db tables superseded
  by IBA," `state='completed'`, answered 2026-08-17. It has nothing to do with GOVERNANCE.md §6 or
  Yes/No wording.
- **The actual Yes/No item is #664** — same batch, answered one second apart (03:17:31 vs
  03:17:32Z) on 2026-08-16, which is almost certainly why the two got crossed when copying from an
  old extract. #664's `state='closed'`, decision recorded: *"leave as pure history, add pointer to
  confirm vocab moved on."*
- **The forward pointer is already live** — I read GOVERNANCE.md §6 directly just now: *"(Historical
  note, left as-is per researcher decision 2026-08-17, escalation #664: the vocabulary itself has
  since moved on — see §39 and BUILD.md §115–117 for the current type/next_action/state model.)"*

**So: nothing is open here, and nothing is causing an issue.** It was resolved and applied on
2026-08-17. No action needed — just the id mix-up corrected.

---

## 11. #677 — confirmed, but deliberately not touched in the live (still-broken) system

You confirmed #677 is superseded by this redesign work. I'm **not** writing that closure into the
current `escalation` table right now — doing so would go through the exact same overwrite-only
mechanism that lost #715's updates, for no benefit, since the row will be rebuilt/migrated once the
new system lands anyway. I'll close it for real as part of the migration in §12, with a resolution
note citing this plan.

---

## 12. Code footprint — smaller than v1's plan, now that there are 2 verbs not 10

`iba/app/lib/escalation.py`: two public functions (`raise_new`, `update`) plus the shared
validate/merge/auto-state/write pipeline (§8), replacing the ten functions listed in the mechanics
report. `iba/app/ps/Escalation.ps1`: two actions, `-Action Raise` / `-Action Update`, with the
completeness checks from §6 done in PowerShell before the Python call (per your original §4
comment) as well as re-checked in Python (defense in depth, matches how validation already works
elsewhere in this app). Same downstream footprint as v1 identified: `run.py` (3 direct writes +
`module_blocking` query), the handlers reading `answered_for_run`-equivalent, `lib/retention.py`,
`tools/purge_word.py`, `migration/legacy_import.py`, `write_list_report()` (now can show real
history per item, not just current state). Migration script backfills one `version=1` snapshot per
existing row, and separately closes out #677 with a resolution note as described in §11.

---

## 13. Still to confirm before build starts

Everything in §9 (six items) plus: does §7's worked illustration match what you had in mind for how
the mechanics should read to someone using it day to day? If the shape is right, next step after
your answers is the actual schema DDL + rewritten code — as its own build step, still not folded
into this plan.
