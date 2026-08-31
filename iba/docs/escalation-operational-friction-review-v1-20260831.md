# Escalation system — operational friction review (v1, 2026-08-31)

**Trigger:** researcher, verbatim, 2026-08-31 (Developer Mode session): *"we need to fix
escalations because it is broken. you are constantly falling over because of the way that the
code is written. you have a bunch of restrictions that make no operational sense, and are hugely
disruptive, and the controls you should have working is not followed."*

**Scope of this review:** `iba/app/lib/escalation.py` (1297 lines), `iba/app/ps/Escalation.ps1`
(382 lines), and the `cfg_escalation_requirement`/`cfg_escalation_transition` config rows that
drive them — as they actually behaved today, evidenced from the live `escalation` table, not from
prior design docs' stated intent.

**Method:** pulled every `raised_at >= 2026-08-25` escalation, filtered to `type='run_error'`
("CLI crashed") rows plus rows whose own text says a call failed, read each one's full
`context`/`comment`/`resolution`, then read the exact code path that rejected each call. Two
distinct, structural defects came out of that — not a list of one-off glitches.

---

## Defect 1 — every validation rejection is filed as a system crash

`main()` (`escalation.py:1159-1190`) wraps the entire CLI dispatch in one
`except Exception as exc:` that, on **any** exception, rolls back and auto-raises a brand-new
`run_error` escalation carrying the full traceback (`assigned_to="Claude"`,
`resolution_kind="self_correctable"`).

That block does not distinguish between:

- a **deliberate `ValueError`** — every validation guard in this file (`_title_shape_error`,
  `_check_assignee`, `_check_requirements`, `_require_flag`, ...) raises exactly this, by design,
  when a call is malformed. Rejecting a bad call is the system **working correctly**, the same as
  a shell command exiting 2 on a bad flag.
- a **genuine unanticipated failure** — a file lock (`WinError 32`), a `TypeError`/`KeyError` from
  an actual code defect, a DB error.

Both land in the same bucket: a new escalation row, a full traceback, and — because it's filed as
`run_error`/`self_correctable` — a later manual pass to close it out as "usage error, not a code
defect." That cleanup pass is real, recorded work, done by hand, today, seven separate times:

| # | What actually happened | Resolution (had to be written by hand) |
|---|---|---|
| #1319 | title 62 chars, 2 over the 60-char limit | "Usage error, not a code defect... retried immediately... succeeded" |
| #1313 | title 64 chars | same pattern |
| #1311 | title 69 chars | same pattern |
| #1317 | `ready_for_approval` call omitted `-Resolution` | "Usage error... CLI correctly rejected it" |
| #1318 | same, on the twin call | "Same usage error as #1317" |
| #1328 | `configmaint.propose` missing `-Title` | acknowledged as the caller's own test artifact |
| #1326 | same | same |

None of these seven represent a code defect. Every one is the validation layer doing its job —
and every one still cost a full escalation-table row, a traceback dump, and a hand-written
resolution note explaining that nothing was actually wrong. That is direct, self-inflicted
disruption with no corresponding benefit: the same information (what was wrong, that it was
retried and fixed) is fully available from the shell's own exit code and stderr, with no DB write
needed at all.

**Fix (low-risk, no policy change):** in `main()`, catch `ValueError` separately from the general
`Exception` case. On `ValueError`: rollback (unchanged), print the message to stderr, return
non-zero — no escalation write. Keep the existing auto-escalation-with-traceback behaviour for
every other exception type, where it's actually earning its keep (it is exactly how #1307/#1308's
real `WinError 32` bug and #1330's real `answered_for_run` bug got caught and fixed today).

---

## Defect 2 — commenting on an item you don't "hold" is a dead end, in both directions

Two separate guards compose into a catch-22 for the single most ordinary action in the system:
leaving a clarifying note on an item that's sitting with the other party.

- **D26** (`not_raised_with_content`, `escalation.py:360-362`): an item still in state `raised`
  cannot receive `comment`/`context`/`tried` content — its state must move first.
- **`actor_must_be_assignee`** (`escalation.py:377-394`, researcher instruction 2026-08-31):
  *"the party processing an item... must be the assigned_to"* — whoever currently holds
  `next_action_assigned_to` is the **only** party allowed to call `update` on it at all, to change
  so much as a comment.

Live sequence on escalation **#1337** (assigned to Researcher, awaiting their decision) — Claude
had a clarifying correction to add, not a decision to make:

1. `update 1337 --originator=Claude "You're right, wrong folder..."` (no `-State`) → **#1338**:
   rejected by D26 — content on a still-`raised` item needs a state move first.
2. Retried with `--state=in-progress` added → **#1339**: rejected by `actor_must_be_assignee` —
   #1337 is held by Researcher, so Claude may not touch it *at all*, state-move included.

There is no third option inside `update` — Claude cannot leave a clarifying comment on an item
pending Researcher review through the sanctioned path, full stop.

The same guard blocks the reverse direction too. **#1306** was assigned to Claude (in-progress
build). The Researcher tried to leave feedback: `update 1306 --originator=Researcher
--next-action=revise --assigned-to=Claude --state=in-progress "this report is still not
complete..."` → **#1341**: rejected — "#1306 is currently assigned to 'Claude', only Claude may
act on it (got originator='Researcher')." **The researcher — the system's own final authority —
was blocked from redirecting their own escalation because Claude currently held it.** The only
documented workaround is `correction`, which is explicitly scoped to *"fix something already
recorded wrong,"* not to leaving feedback on work in progress — using it for this would be
misusing the one exemption that exists.

**Root cause:** the guard was written to control who does the substantive *work* on an item — the
researcher's own words: *"who is doing the work, and who is supposed to do the work."* As
implemented, it also controls who may *say anything about it at all*, including a party (the
Researcher) whose authority the rest of this same system already treats as final everywhere else
(D25, `decision_required_approval_requires_researcher`).

**Proposed fix (needs your confirmation — this revisits a same-day instruction, not just a bug):**
narrow `actor_must_be_assignee` so a call that only adds `comment`/`context` (no change to
`next_action`, `resolution`, or a state that hands off ownership) does not require assignee-match
— appending a note is not "processing" the item. Whether the Researcher should additionally be
exempt outright (as the item's ultimate authority, mirroring the exemption `correction()` already
has) is the part I'm not deciding unilaterally — that's the actual judgement call.

---

## What this review does NOT re-litigate

Real code defects already found and fixed live today are out of scope here — #1307/#1308 (file
lock during auto-report), #1330 (`answered_for_run` dead-code state match). Two items already
raised and awaiting your decision through the normal channel, unrelated to this review: **#1329**
(NULL-key `cfg_setting` cleanup) and **#1327** (a new proposed guard, not yet built).

## Addendum — Defect 2 resolved as full removal; a real gap found while re-checking my own report

**Researcher's decision, 2026-08-31, same day:** drop `actor_must_be_assignee` entirely, not
narrow it — the two objectives (control vs. ordinary back-and-forth) worked against each other,
and escalation mechanics were consuming ~80% of project time. Deactivated
(`cfg_escalation_requirement` rowid 17/18/19 → `active=0`), verified live against the real #1337
(the exact call that failed twice earlier as #1338/#1339 — now succeeds). Recorded as #1346.

**Then the researcher caught a real gap in this report's own first pass.** I'd written that the
D25 check "gates an actual decision" without fully verifying it. Pushed on it — verified live,
they were right to doubt it: `requires_prior_ready_for_approval_if_decision_required` (rowid
15/16) only checked that a `ready_for_approval` transition existed *somewhere* in
`escalation_history`, ever — not that the item's *current* `next_action` is `ready_for_approval`
right now. A decision_required item could in principle go
`ready_for_approval → revise → in-progress → approved` and pass, since `ready_for_approval`
happened once, arbitrarily long before. **Pre-existing gap, not caused by the
`actor_must_be_assignee` removal** — that check never inspected `next_action` at all, only
`next_action_assigned_to`.

**Fixed** — renamed to `requires_current_ready_for_approval_if_decision_required`; now checks
`escalation.next_action = 'ready_for_approval'` directly rather than history. Scoped to
`decision_required` only, per the researcher's explicit instruction (`self_correctable` never uses
this vocabulary). `decision_required_approval_requires_researcher` (Claude can never self-approve)
is separate and untouched by anything in this session.

**Verified live, both directions:**
- Negative: real #1340 (sitting at `next_action='review'`, not `ready_for_approval`) — rejected,
  correctly, with zero escalation-row write (per Defect 1's fix).
- Positive: throwaway #1347, raised for exactly this test — `ready_for_approval` then `approved`
  succeeded end to end.

Recorded as #1348. All three changes today (#1345 Defect 1, #1346 the removal, #1348 the
sequencing fix) are in `iba/app/lib/escalation.py` and `cfg_escalation_requirement`, verified
against real records, not just read.

## Addendum 2 — approve-before-build: mostly already built, one row and one gap found

**Researcher, 2026-08-31:** described the intended pattern for a config/code change that needs
approval *before* it's applied (not the usual propose-then-approve-the-already-built-change flow):
Claude flags the item as needing follow-up; the researcher's approval doesn't jump straight to
`completed` — it moves to `approved`, reassigned to Claude; Claude applies the change, then closes
it to `completed` itself, without a second full approval round-trip for the same decision. *"that
is appropriate."*

**This is not a new feature — it mostly already existed.** `needs_claude_followup` (escalation
#1075, 2026-08-30) and the `followup_cleared_was_approved` transition condition (built into
`escalation.py` earlier today, 2026-08-31) implement exactly this. What was missing was one
`cfg_escalation_transition` row activating the second half — already sitting as escalation
**#1340** ("Add followup_cleared_was_approved transition rule"), raised earlier today and never
progressed. Moved it to `ready_for_approval` (assigned to Researcher) as part of this session —
Claude cannot approve it (decision_required, Researcher-only, unaffected by anything else changed
today). **One command finishes activating it:**

```powershell
.\iba\app\ps\Escalation.ps1 -Action Update -Id 1340 -AnsweredBy Researcher -NextAction Approved -Resolution "approved -- activate the missing transition row"
```

**A real gap found while verifying it, fixed the same way as the others — live, not assumed.**
`update()` never actually forced the assignee to Claude when an item moved to `approved` with
`needs_claude_followup` set — it just carried forward whatever `-AssignedTo` was passed (or
nothing). So the researcher could approve-with-followup, forget `-AssignedTo Claude`, and the item
would sit at `state='re-assigned'` still assigned to *themselves* — visually "needs follow-up" but
not actually routed to whoever's supposed to do it. Fixed: `checked_action=='approved'` with
`needs_claude_followup` true now **forces** `next_action_assigned_to='Claude'`, overriding even an
explicit different `-AssignedTo` on that call — the flag's whole meaning is "Claude still has to
act," so there's no legitimate case for assigning it elsewhere.

**Verified live**, throwaway #1349 (closed after, test purpose served): `ready_for_approval` with
`-NeedsFollowup 1` → Researcher approves *without* passing `-AssignedTo` → result:
`next_action='approved'`, `state='re-assigned'`, **`next_action_assigned_to='Claude'`** — forced,
not defaulted. The other half (Claude later clearing the flag and reaching `completed`) still
needs #1340's row active to test end-to-end — that's the one command above.

## Addendum 3 — #1340 applied; the status message was hiding half the story; a stale-backlog gap
found and closed at the root

**Researcher approved #1340.** Applied for real, not just tested on a throwaway: inserted the
`cfg_escalation_transition` row, then cleared `needs_claude_followup` as Claude with no
`-NextAction` supplied — the exact call the whole mechanism exists for. Result:
`state='completed', next_action='approved', assigned_to='Claude'`. The approve-before-build loop
this session built (Addendum 2) is now proven end to end on a real item, not a synthetic one.

**Researcher then caught that `update()`'s own status message was incomplete** — it printed only
`state=`, so `state='re-assigned'` (the routes-back-to-Claude-for-followup state) looked identical
in the output to any other reassignment, with no visible `next_action` to say it was actually
`'approved'`. Fixed: `update()` and `correction()` now report `state`, `next_action`, and
`assigned_to` together on every call. (`resolve_self_correctable()` untouched — its outcome is
always `completed`, no ambiguity to resolve.)

**Then a bigger question: "I had several attempts for you to continue with this task, but... you
just do not pick it up."** Pointed at #1312 and #1314. Investigated both in full rather than
guessing:

- **#1314** ("CSV export should default to suppressed") — the researcher said `proceed` at
  05:28:43Z. Nothing happened after that, ever — only 2 history versions total. **But the actual
  work got done anyway, under a different escalation number.** #1315 (a separate, later-raised
  `configmaint.propose` item implementing exactly what #1314 asked for) was approved and applied —
  verified live: the `cfg_setting` row exists (`configmaint.csv_export_on_auto_report`, value
  `0`), and `cfgreport.py`'s gating code + both call sites (`configmaint.py:412` auto-triggered,
  ungated by default; `:682` explicit report step, always writes) are correct and match the
  approved design. #1315 itself was stuck at `state='re-assigned'` — approved, applied, never
  formally closed. Fixed via `Correction` (record didn't match reality, not a new decision):
  #1315 → `completed`. #1314 → `completed`, cross-referencing #1315 as the escalation that
  actually carries the approved decision (correction reasoning stated plainly, so it's easy to
  reopen if that cross-reference judgement is wrong).
- **#1312** ("cfg_table.category built; grant revocation pending approval") — this one WAS worked
  on after `proceed` (v3 06:25, v4 08:46: both dependent write-grant revocations, #1309/#1310,
  applied and verified) — the substantive work was genuinely done since this morning. It just
  never got pushed to `ready_for_approval` afterward. Moved there now, summarising what's done, so
  the researcher's next action is a real decision (accept the built work) not more digging.

**Root cause, not just the two symptoms:** neither item would ever resurface on its own. The
`start-project` skill's own step 4 (`Escalation.ps1 -Action List`, noting anything
`next_action_assigned_to='Claude'`) is exactly the mechanism that would have caught these at any
normal session start — and this session explicitly skipped `start-project`, by the researcher's
own request, to build the Developer Mode protocol instead. `/developer-mode` never did that cheap
check either. **Fixed at the command, not just this once:** `.claude/commands/developer-mode.md`
now runs `Escalation.ps1 -Action List` as part of its own step 1 and requires reporting anything
assigned to Claude — the one piece of `start-project` worth keeping even when the rest is
deliberately skipped.

**Same sweep also surfaced (git status this session already showed the researcher's escalation-
actions Excel worksheet as modified — approvals below almost certainly came through that tool,
in parallel with this conversation, not through anything said in chat):**

- **#1329** (delete a corrupted NULL-key `cfg_setting` row, left over from an earlier `-Where`/
  `-Set` slip applying #1315) — found already approved, applied: row deleted, verified 0 null-key
  rows remain, closed.
- **#1338/#1339/#1341/#1344** — the four "CLI crashed" noise-escalations from Addendum 1's Defect
  2 investigation (all pre-dating this session's `actor_must_be_assignee` removal). Closed as
  non-defects, each pointing back to this doc.
- **#1316** ("Register the new schema-overview report script") — found already approved
  (`next_action='approved'`, `needs_claude_followup=1`) but **NOT applied** — its own comment,
  written by Claude before the approval, says plainly: *"Superseded... This proposal is no longer
  needed -- please reject it whenever convenient; I won't self-reject my own proposal."* Applying
  an insert Claude itself flagged as stale would be wrong; silently ignoring an approved item would
  also be wrong. Left alone, flagged in chat for a real decision — genuinely not mine to resolve
  either way.
- **#1306** and **#1327** — real, still-open items, untouched, out of this sweep's scope; noted so
  they're not mistaken for cleared.

## Addendum 4 — mechanically enforced, not just a written rule this time

The researcher's own conclusion from Addendum 3: a memory/CLAUDE.md rule already failed once at
exactly this (#1312/#1314 sat open for hours, across multiple sessions, despite the general
"check the backlog" instruction existing). Asked for something that can't be forgotten the same
way. Built a Claude Code `Stop` hook —
`.claude/hooks/stop_check_escalation_backlog.py` + `.claude/settings.json` `hooks.Stop` — that
queries `next_action_assigned_to='Claude'` live, every time Claude tries to end a turn, and blocks
once (never loops — respects `stop_hook_active`) with the open list if anything's there. Design
note: deliberately NOT filtered by type or age — real data checked while building this (#1306,
genuine multi-session work) showed no clean field distinguishes "forgotten" from "still
legitimately in progress," so the hook surfaces everything open and asks Claude to say plainly
what's outstanding, not to force-resolve items that are correctly still pending. All four branches
(nothing open, something open, `stop_hook_active` re-entry, missing/bad DB path) verified live
against real payloads before wiring in.
