# Escalation type routing — proposal (not yet built)

**Escalation #795.** Your intent, recorded there: task and issue types shouldn't be answerable
through the flat `AnswerRun` approve/reject/revise method; run_error should be handled the same
way. This is the proposal, for your decision — nothing below is built yet.

## The one fact that changes the picture

I traced exactly when each escalation `type` gets created, in `run.py`:

| Type | Only ever created from | Does answering it need to "resume" a live process? |
|---|---|---|
| `config` | `configmaint.propose`'s pause | **Yes.** The `Propose` command is sitting exited with code 2. Re-running it re-checks the answer and applies the change. |
| `task` | A word-scoped step's pause (`escalate()`) | **Yes.** Same mechanism — the step's own command is paused, re-running it resumes. |
| `issue` | A `.validate` step's pause (e.g. `validation_word`) | **Yes.** Same mechanism. |
| `run_error` | A crash, or a `report-stop` | **No.** Both mark the run `state='failed'` immediately. Nothing is waiting. Answering a `run_error` escalation is pure record-keeping — it never resumes anything. |

So `run_error` is already structurally different from the other three — it's the ONE type that's
always terminal. `config`/`task`/`issue` are currently ALL the same shape: something real is
paused, waiting for exactly one decision before it can continue.

## What this means for your instruction

**`run_error` → easy, no conflict.** Since it never resumes anything, there's no structural reason
it couldn't be answered through a slower, richer flow (the same `ready_for_approval` →
`approved` two-stage process manual items use) instead of the flat single decision. This part can
be built without touching how any run actually executes.

**`task`/`issue` → not just an `escalation.py` change.** These two types are *only* ever raised
by a step that is genuinely paused, waiting for that one decision so the CLI invocation can
continue (or report what happened). To take them off the flat method means one of two things, and
both go beyond `escalation.py`:

- **Option A — stop these steps from pausing at all.** Change `validation_word`/`validation_book`
  (and any other `.validate`/word-scoped step that calls `escalate()`) to use `report-stop`
  instead of `pause-continue` — i.e., treat a validation finding the same way a crash is already
  treated: record it and let the run finish, rather than blocking it. The follow-up decision (was
  this finding acceptable?) then happens later, asynchronously, through the richer flow — not by
  re-running the same command. This changes real CLI behavior: today, re-running
  `.\Reports.ps1 -Step ValidationWord ...` after answering picks up the decision and reports
  success; under this option it wouldn't need to be re-run at all, but the researcher no longer
  gets an immediate "did that pass" answer from the same command.
- **Option B — keep the pause, but let a *different* command supply just enough to unblock it.**
  The live process still needs exactly one thing to resume (some signal it can check for). This
  would mean the fast decision keeps existing internally, but is only ever set as a *side effect*
  of the richer flow's first step (`ready_for_approval`) rather than being a thing you type
  directly — a smaller behavior change, but it means "revise" mid-review would need its own
  handling for what the paused process actually does while revision is happening.

I'm not picking between these — Option A is the more thorough answer to "task/issue shouldn't use
this method" but changes how validation-style commands feel to run; Option B keeps today's CLI
feel closer to what it is now but is a more delicate change inside `run.py`'s own resume logic.

## What I'd actually build, if told to proceed

1. `run_error` gets the two-stage flow now — no dependency on A vs B, safe to do independently.
2. `task`/`issue` wait on your choice of A or B above (or a third option you prefer) before I write
   anything, since both touch code outside `escalation.py` itself (`reports.py` at minimum for A).
3. `config` is untouched either way — it's the one type where "something is genuinely waiting" is
   inherent to what `configmaint.propose` does, not a coincidence of current step design.

## Aside, not part of this proposal

Escalation #797 (the crash from your `Update -NextAction Review` attempt) was a correctly-caught
case error: `_check_next_action_manual` compares case-sensitively (`'Review' != 'review'`), while
the neighbouring `_check_assignee` check normalises case first (`.strip().capitalize()`). That's a
small internal inconsistency, not a bug that lost anything — closing #797 as input-error, same as
#788/#789/#791, unless you want the case-sensitivity difference looked at too.
