# Escalation redesign — plan v3 (two-stage approval, more illustration)

v2: [`archive/escalation-redesign-plan-v2-20260819.md`](archive/escalation-redesign-plan-v2-20260819.md).
Digested from your third round of comments. All six of v2's open questions are now resolved below
— five from your direct answers, one (the `state`-vs-`next_action` wording around "approved") I've
resolved myself by reasoning through your worked description rather than asking again, given your
note on Q5 that you expected me to pick that class of thing up. §7 now carries two full worked
scenarios with explicit incoming/outgoing columns, per your "more illustration" ask.

---

## 0. What changed from v2

| Area | v2 | v3 |
|---|---|---|
| Approval | Single `next_action=approve` → `completed` | **Two-stage handshake**: `ready_for_approval` (requester) → `approved` (reviewer) → system-validated → `completed`. Produces two history rows, not one. |
| `re-assign` | Open question — who sets it | **Renamed `re-assigned`; system-set automatically** whenever `next_action_assigned_to` changes and no more specific terminal rule applies |
| `reject` | Ambiguous "completed and either withdraw or supersede" | **Resolved**: `reject` is the action; the **party** (not the system) explicitly chooses the resulting state, `withdraw` or `supersede`; `comment` mandatory either way |
| `supersede` | Open question | **Resolved**: not auto-derived — a party's explicit choice at reject-time (validity condition: `next_action=reject` + non-empty `comment`); also the intended path for correcting a wrong `short_description` (§4) |
| Notification | Open question | **Resolved for now: chat only** — no new push mechanism built this round. A "pre-formatted chat item on new entry" idea is noted for later, not in scope |
| Approval authority | Open question | **Resolved: contextual, not role-locked** — Claude may complete its own low-judgement fixes; researcher approval is required when researcher judgement was needed or the researcher raised it |
| Reporting | Not designed | **Two reports specified**: the open-items list now includes full history inline; a new per-item deep-history report follows `related`/`supersede` links |
| Illustration | One scenario, end-states only | **Two scenarios**, every step showing incoming → outgoing `state`/`next_action` explicitly |

---

## 1. The incoming/outgoing framing — the conceptual model underneath everything below

Your general comment sets the frame for reading every rule and every illustration from here on:

> *"The action incoming (present value) is about what is expected from the reader. The action
> (update value) is about what action the next reader should take or be aware of. In the same way,
> state incoming (current value) designates where the item is now; the new state is the state the
> update causes it to be in."*

Concretely: every `Update` transaction has a **before** (`state`/`next_action` as they stand when
you open the item) and an **after** (what you set them to before posting). The *before* value tells
you, the current reader, what's expected of you. The *after* value is your instruction to whoever
reads it next — including yourself, next time. No schema change follows from this (a snapshot
already implies "before" = the previous version's "after") — but every illustration in §7 now shows
both columns explicitly, since that's the point you're making: the transitions matter, not just the
end state.

---

## 2. `next_action` — six values now (two-stage approval)

| Value | Set by | Meaning |
|---|---|---|
| `ready_for_approval` *(renamed from `approve`)* | Whoever finished the work | "I believe this is done — reviewer, please confirm." Reassigns to the reviewer, `resolution` filled in here |
| `approved` *(new)* | The reviewer | Confirms the work. Triggers system validity checks → `state=completed` |
| `reject` | Either party | Item is not being carried forward as-is — the party also picks `withdraw` or `supersede` (§3); `comment` mandatory |
| `revise` | Either party | Needs rework, based on `comment`/`context` |
| `noted` | Either party | Information-only, no action required — pairs with `state=closed` |
| `review` | System, at Raise (default) | Signals the assignee to act on a newly raised item |

**On the wording you used ("add new approved state") vs. the worked procedure ("set the action to
approved")**: I read these as describing the same thing with the same looseness you've used before
(state/action interchangeably in prose). The step-by-step procedure is unambiguous and I've built
to that: `approved` is a **`next_action` value**, not a ninth `state`. No new state is added beyond
`supersede` (already added in v2). If that's wrong, it's a one-line fix — but I'd rather build to
the concrete procedure you spelled out than the more casual opening sentence.

---

## 3. Auto-state rules — reordered, precedence matters now

With `re-assigned` now firing on *any* assignee change, the rules need a priority order — otherwise
a `revise` (which also changes the assignee) would ambiguously match two rules at once. Evaluated
**top to bottom, first match wins**:

| Priority | Condition | Resulting `state` |
|---|---|---|
| 1 | `next_action=approved` AND `resolution` is non-empty (validity check) | `completed` |
| 2 | `next_action=reject` | Whatever the party explicitly set — `withdraw` or `supersede` (both require non-empty `comment`, checked at write time) |
| 3 | `next_action=revise` | `in-progress` |
| 4 | `next_action=noted` | `closed` |
| 5 | `next_action_assigned_to` differs from the current value | `re-assigned` — *this is why `ready_for_approval` lands here*: it changes the assignee and matches no more specific rule above it |
| 6 | none of the above | `state` unchanged, or whatever value either party set directly (`on-hold`/`in-progress`/`closed` are still directly settable per the original either-party list) |

This ordering is *why* a two-stage approval naturally produces exactly two history rows without any
special-casing: `ready_for_approval` falls through to rule 5 (`re-assigned`); `approved` (with
`resolution` present) hits rule 1 directly (`completed`). Confirmed against your expectation in §7
of the last round: *"I am expecting to see two history rows for an approval — the first the request
to approve, the second the completion."*

---

## 4. Correcting a wrong `short_description` — the intended path, now concrete

Your inclination, confirmed: *"if the short_description is wrong, then a new item is raised with a
supersede of the old... superseded means the later item redefines, or builds on the previous item."*

Mechanically, using machinery already in this plan (no new special case needed):
1. **Raise** a new item with the corrected `short_description`, `related_activity` naming the old
   item ("supersedes #0900").
2. **Update** the old item: `next_action=reject`, party sets `state=supersede`, `comment` explains
   the correction (mandatory, per §3 rule 2).

Worked as Scenario B in §7.

---

## 5. Reporting — two deliverables, not designed in v2

### 5a. The open-items report (`-Action List` equivalent) — revised

Must show each open item's **full history inline**, not just current state — every
`escalation_history` row for that id, in version order, under its current-state summary line. This
replaces today's single-row-per-item table.

### 5b. New: item deep-history report (`-Action History` or similar)

Given one item id, produces: that item's complete `escalation_history`, plus — by following
`related_activity` text references and `supersede` chains — the same for every item it names or is
named by. This is the "full story of one thread" view: for the wrong-title example in §4, asking
for either #0900 or #0901's deep history would show both items' full histories together, in one
place, because they're linked.

Both are report-shape decisions for the build step, not code here — flagging them now so the schema
work accounts for "which items reference this one" being a real, expected query (an index on
`related_activity` at minimum).

---

## 6. Notification — resolved: chat only, for now

> *"At the moment the notification will be through the chat for both parties... I am OK for the
> moment to just use chat."*

No new mechanism built this round. The "pre-formatted chat item jumping up on a new table entry"
idea is noted here as a possible future enhancement, explicitly **out of scope** for this redesign.

---

## 7. Two full worked scenarios — every step, incoming → outgoing

### Scenario A — the two-stage approval, start to finish

**Step 1 — Raise.** Claude raises a run-error item.

| Field | Incoming | Outgoing |
|---|---|---|
| `state` | *(new)* | `raised` |
| `next_action` | *(new)* | `review` (default) |
| `next_action_assigned_to` | *(new)* | `Claude` (default) |
`escalation`: `id=0900, version=1, source="scripts/word_full_extract.py", type=run_error,
short_description="word_full_extract.py throws on H1234", comment="ValueError at line 210, full
traceback in context", context="<traceback>"`.

**Step 2 — Update: Claude tries a fix, it fails, asks the researcher.**

| Field | Incoming | Outgoing |
|---|---|---|
| `state` | `raised` | `re-assigned` *(rule 5 — assignee changed to Researcher)* |
| `next_action` | `review` | `revise` |
| `next_action_assigned_to` | `Claude` | `Researcher` |
`escalation`: `version=2, tried="patched the None check at line 210, re-ran — same error at line
244"`, `comment=<v1 text> + "second failure looks like a data issue — can you confirm H1234's verse
span is intact?"`. *(Note: rule 3 — `revise` — would also match here, and takes priority over rule
5 per the ordering in §3: `state=in-progress`, not `re-assigned`, since `revise` is more specific
than a bare assignee change.)*

**Step 3 — Update: Researcher confirms and fixes the data, requests sign-off.**

| Field | Incoming | Outgoing |
|---|---|---|
| `state` | `in-progress` | `re-assigned` *(rule 5 — no more specific rule matches `ready_for_approval`)* |
| `next_action` | `revise` | `ready_for_approval` |
| `next_action_assigned_to` | `Researcher` | `Claude` |
`escalation`: `version=3, resolution="confirmed H1234's span was truncated by the 07-19 backfill;
re-ran the gap-fill"`, `comment=<prior text> + "fixed the data — can you confirm the script now
runs clean?"`. **This is the first of the two history rows you expect for an approval.**

**Step 4 — Update: Claude confirms, approves.**

| Field | Incoming | Outgoing |
|---|---|---|
| `state` | `re-assigned` | `completed` *(rule 1 — `approved` + `resolution` already present)* |
| `next_action` | `ready_for_approval` | `approved` |
| `next_action_assigned_to` | `Claude` | *(unchanged — Claude)* |
`escalation`: `version=4, comment=<prior text> + "confirmed — script re-ran clean against H1234"`.
**This is the second history row — the completion.**

Four history rows total for the item's full life; the approval itself is rows 3–4, exactly two, as
you expected.

### Scenario B — correcting a wrong title via supersede (§4, worked)

**Old item, #0900** (typo in title, already raised and in progress from Scenario A — imagine it's
caught before Scenario A's Step 2):

| Field | Incoming | Outgoing |
|---|---|---|
| `state` | `raised` | `supersede` *(rule 2 — `reject`, party's explicit choice)* |
| `next_action` | `review` | `reject` |
`escalation` (#0900): `version=2, comment="superseded by #0901 — short_description had a typo,
raising a corrected item instead of editing this one"` (mandatory, non-empty, per §3 rule 2).

**New item, #0901** (raised in the same turn):

`escalation`: `id=0901, version=1, state=raised, next_action=review,
short_description="word_full_extract.py throws on H1234"` (corrected), `related_activity="supersedes
#0900"`, `source`/`type`/`context` carried over from what #0900 was about.

A deep-history request (§5b) on either id would now surface both items together, in full, as one
thread.

---

## 8. Everything else from v2 — unchanged, carried forward

Columns (§3 of v2), the `escalation`/`escalation_history` full-snapshot model (§2 of v2), the
`Raise`/`Update` transaction shapes and required/optional/conditional fields (§6 of v2), the
processing pipeline and single-transaction atomicity (§8 of v2), the code footprint (§12 of v2), and
the #653/#664 correction and #677 deferred-closure decisions (§10/§11 of v2) all stand as written —
nothing in this round changed them. Only the approval vocabulary, the `re-assign`→`re-assigned`
rule, the `reject`/`supersede` rule, notification, approval authority, and reporting scope changed,
as captured above.

---

## 9. Remaining open item — genuinely one, not six this time

Only the §2 wording call (`approved` as `next_action` vs. a ninth `state`) is a judgement call I
made rather than confirmed — everything else this round had a clear answer in your comments. Flag
if I read that one wrong; otherwise this is ready to move to schema DDL + code as the next step.
