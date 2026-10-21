# Escalation #795 — what's actually outstanding, checked against live code (2026-08-22)

**Requested:** "check what is outstanding on 795," after approving #798/#799's build. Checked the
live `escalation` row (#795, still `state=re-assigned`, `next_action=review`, assigned to
Researcher, no `resolution` set) against the actual code as it stands today — not assumed from the
comment history alone.

## Bottom line

#795 raised two concrete findings plus one attached proposal document. **None of the three were
resolved by #798/#799's build** — that build answered a different, though related, question
(`resolution_kind`: decision-required vs self-correctable). #795's own comment says its two
findings were *"folded into #798's scope as concrete evidence/consequences rather than solved
separately here"* — checked against what #798 (all 5 versions) actually specified and built:
they were cited as motivating context, not addressed as deliverables. #798's own resolution text
confirms this scope, plainly: config axis + 3 real code-gap fixes (narrative/passage/raw) + the
`cfg_passage` table + debugging fixes — nothing about `AnswerRun`'s decision vocabulary or its
`-RunId` matching.

## Item 1 — Dispatcher `AnswerRun` still collapses approve/reject/revise into `completed`

**Still true, unchanged, confirmed live** — `cfg_escalation_transition` for `shape='dispatcher'`:

| priority | next_action | → state |
|---|---|---|
| 1 | `hold` | `on-hold` |
| 2 | `noted` | `closed` |
| 3 | *(anything else)* | `completed` — row's own stored note: *"approve/reject/revise all just complete the pause"* |

This is exactly what #795 originally flagged. **What #798/#799 actually changed here** is
additive, not a fix to this: a dispatcher-tied item whose `resolution_kind='decision_required'`
(which now includes every `configmaint.propose` pause and every `.validate`-step issue, per
`reports.py`/`cluster.py`/`lexicon.py`) can now ALSO be closed through `-Action Update`'s richer
manual vocabulary (`ready_for_approval` → `approved`, with a real two-stage handshake) instead of
`AnswerRun`. But `AnswerRun` itself still exists, unchanged, and still collapses approve/reject/
revise if someone uses it. So the exposure #795 named is now *avoidable* (use Update instead) but
not *closed* — nothing stops `AnswerRun` from being used, and it still behaves the same flat way
if it is.

## Item 2 — `AnswerRun -RunId` still only accepts the full run_id string, not the short escalation id

**Still true, unchanged, confirmed live** — `pending_for_run()` (`lib/escalation.py:503`) looks up
by the literal `run_id` column only; `Escalation.ps1`'s `'AnswerRun'` block passes `$RunId`
straight through with no short-id resolution. This is the exact UX gap the researcher hit live on
#796 (*"the researcher tried the escalation's short numeric id (796) instead and it failed with
'no pending escalation for run 796'"*). No code touches this anywhere in #798/#799's build.

## Item 3 — The attached proposal (`escalation-type-routing-proposal-v1-20260822.md`) is still just a proposal

That document (referenced directly from #795) is the genuine design question behind item 1: should
`task`/`issue`/`run_error` stop using `AnswerRun`'s flat vocabulary at all? It lays out:

- `run_error` → no structural obstacle, could move to the richer two-stage flow with zero
  conflict, independent of anything else.
- `task`/`issue` → genuinely blocked pending your choice between two options, both of which touch
  code outside `escalation.py` itself:
  - **Option A** — stop `.validate`-style steps from pausing at all (treat a validation finding
    like a crash: record it, let the run finish, decide later, asynchronously).
  - **Option B** — keep the pause, but have it unblock only as a side effect of the richer flow's
    `ready_for_approval` stage, not a directly-typed flat decision.

**Not decided, not built.** #798/#799 never picked A or B, and never removed anything from
`AnswerRun`. The document's own closing line is still accurate: *"I'm not picking between these...
task/issue wait on your choice of A or B above (or a third option you prefer) before I write
anything."*

One footnote worth naming plainly: since #798/#799 made `config`/`issue` types always
`decision_required`, and a `decision_required` dispatcher item can now go through `Update`'s
richer flow, **item 1 of the proposal ("run_error gets the two-stage flow now — safe to do
independently") is effectively already true as a side effect** for `run_error`, `config`, and
`issue` alike — they all CAN use the richer flow today. What's still missing is the actual
decision this proposal asks for: whether `AnswerRun`'s flat path should be closed off for these
types, not just made optional.

## Things checked and confirmed NOT outstanding

- **#797** (the `Update -NextAction Review` case-sensitivity crash) — already `state=completed`,
  `next_action=approved`. Closed as a correctly-caught input error, as the proposal doc itself
  recorded; no separate fix was requested or is pending.
- **The debugging/logging rethink** (v4 §6.2/§7) — explicitly scoped in v5's "open input 3" to
  files *inside* #798/#799's own build only, per your instruction ("only raise a new escalation if
  this touches scripts outside this build's scope"). Both concrete fixes it found (the CLI
  crash-wrapper's silent `except: pass`, and `run.py`'s two unwrapped `esc_raise()` calls) were
  built in Stage 2/3. No file *outside* this build's scope was found needing the same treatment —
  correctly not escalated further, per your own rule.
- **The prose module/utility classification note** — already tracked as "revisit when that stage
  of work comes up," not part of #795's own core content; unaffected either way by this review.

## What this needs from you

Two live gaps (items 1/2) plus one still-open design choice (item 3, A vs B, or a third option) —
genuine judgement calls, not something to resolve unilaterally. Options as I see them, not a
recommendation:

1. Leave #795 open, tracking exactly these three items, and pick up the type-routing decision
   (A/B/other) as its own follow-on build once you've reviewed the proposal document.
2. Fold the short-`RunId` UX fix (item 2) into a much smaller, standalone `self_correctable` fix
   now — it's a pure lookup convenience with no design ambiguity (accept either the short id or the
   full string, prefer an exact `run_id` match, fall back to the escalation `id`) — independent of
   the A/B decision on item 1/3.
3. Something else you'd rather do with #795 at this point.
