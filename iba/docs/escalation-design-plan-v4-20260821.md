# Escalation design plan (v4, 2026-08-21)

Supersedes [`escalation-design-plan-v3-20260820.md`](escalation-design-plan-v3-20260820.md). Full
decision-by-decision status: [`escalation-design-decision-register-v1-20260821.md`](escalation-design-decision-register-v1-20260821.md).
This round answers D18–D23 — the review confirmed D9/D14 settled, and named five real gaps: how
code changes get recorded, how chat gets captured, the relationship to the project's other governing
documents, a genuinely complete vocabulary treatment (not scattered examples), and the PS front door
— both its exact behaviour and whether it's the right choice at all. Sections unchanged since v3 are
marked as such, not restated.

---

## Resources / Purpose / Type of entries

**Unchanged from v3.** Five-type model confirmed correct (D9); type-keyed Raise defaults confirmed
(D12). Not restated — see v3.

---

## Document integration — how an item relates to BUILD.md / GOVERNANCE.md / CLAUDE.md / USER-GUIDE.md (D18, D20)

This wasn't designed at all before this round — a real gap, not an oversight to wave past. The
project already has a taxonomy for exactly this question, stated once and not yet connected to
escalation's own type model: `governance.procedural_document_taxonomy` — *"(a) planning/investigatory
— plans, explorations, decision docs; (b) config-extract — generated...; (c) history-of-changes —
BUILD.md-shaped change records...; (d) guidance/baseline instructions — GOVERNANCE.md, USER-GUIDE.md,
CLAUDE.md-shaped."* Mapped against the five types:

| Content produced | Home document (taxonomy category) | Escalation's role |
|---|---|---|
| The debate/exploration itself | An `issue`'s own `context.reference_doc` — category (a), already designed (v2) | The issue **is** the control record; the document **is** the content. Not duplicated between them. |
| What actually changed in the code | `BUILD.md` — category (c) | **Not replaced by a `task`'s `resolution` field.** `governance.build_md_on_code_change` is a standing, independent obligation — a `task` that involved a code change is not complete just because `resolution` says so; the `BUILD.md` entry is a separate, required companion, and once written, the task's `resolution` should reference its section number (cross-reference, not restate — matching `documentation.single-authority-pointer-not-copy`, the same principle already used for `cfg_behaviour_rule`'s own pointer rows). |
| A rule/decision about how the project or app operates | `GOVERNANCE.md` (via `cfg_*` first) — category (d) | **This is the specific gap that's been open all session (D5).** The fix isn't a new mechanism — it's a discipline: an `issue` whose `decided` resolution states a new or changed rule **produces** a `task` ("update `GOVERNANCE.md` to reflect X"), `from_id` pointing back to the issue, in the same turn the issue is decided — not left implicit, not assumed to happen because the code changed. This is exactly what didn't happen for this module's own rebuild, twice (the 2026-08-19/20 redesign, and this session's own new `chat_routing` rule until routed through `configmaint.propose` properly). |
| How to use a feature | `USER-GUIDE.md` — category (d) | Same pattern: a `task` that changes user-facing behaviour produces a companion documentation task, not an assumption it'll get remembered. `USER-GUIDE.md` §4 is the one part of this module's own documentation that *has* stayed current across every round — because updating it has consistently been treated as part of the same unit of work, not a follow-up. That's the standard to generalise, not an accident to repeat only there. |
| Compact, project-wide, cross-session orientation | `CLAUDE.md` | Rarely touched by this module specifically — only for genuinely project-wide (not IBA-internal) rule changes. Same produced-task pattern when it does apply. |

**The concrete fix, stated as a rule, not left as a norm:** a `task`/`issue` whose resolution implies
a documentation obligation should **produce** the documentation task explicitly (`from_id` +
`related_activity`) rather than trust it'll be remembered. This can't be fully mechanically enforced
— detecting "did this decision imply a `GOVERNANCE.md` change" from free text isn't reliable — so,
matching the honest pattern already used for `cfg_escalation`'s unenforceable rules (`resolution_
precedence`, `chat_routing`'s original half), this is a **discipline**, checked at review time, not a
write-time gate.

---

## Chat capture — how a chat comment becomes escalation content (D19)

`cfg_escalation.chat_routing` (extended this session, live) says *what* must be captured. It doesn't
say *how* — verbatim, or Claude's own summary. That gap is real: a paraphrase risks exactly the kind
of subtle misreading this session already produced once (misreading "immutable" into a design where
the researcher never said that). **Proposed rule, formalising what's already been done ad hoc in
`#6`'s own history this session:** the operative sentence(s) — the actual instruction, correction, or
judgement — are quoted **verbatim**, in quotation marks, inside `comment`/`context`. Surrounding
framing (why it matters, what it connects to) may be Claude's own prose, clearly distinguishable from
the quoted part. This is not a new mechanism to build — it's a documentation convention, added to
`cfg_escalation.chat_routing`'s own rule text via `configmaint.propose` (the same table, not a new
row) the same way this session's symmetry extension was.

---

## The complete vocabulary — `next_action` × `state` × `type`, held together (D21, absorbs D11)

Every value, every vocabulary, reasoned as one picture rather than assembled from separate sections
— checked against the live `cfg_enum`/`cfg_escalation_transition` rows this session, not recalled:

### Dispatcher shape (`task`/`run_error`/`config`, when tied to a real `run.py` pause) — unchanged, closed, complete

| `next_action` | Fires | → `state` |
|---|---|---|
| `hold` | always | `on-hold` |
| `noted` | always | `closed` |
| `approve` / `reject` / `revise` | always (all three, one catch-all rule) | `completed` |

**Why `revise` resolves straight to `completed` here, not `in-progress` the way manual's does:** a
dispatcher-tied item's own life ends the moment the pause is answered — the pipeline itself decides
what to do with a "revise" answer (retry with changes), which may or may not raise a fresh escalation
if it hits another pause. The escalation's job was only ever to unblock the pause, not track the
pipeline's further work. **Complete as five values, three resulting states** — no gap found; a
dispatcher item never reaches `in-progress`, `re-assigned`, `withdraw`, or `supersede`, correctly,
since none of those describe a real pipeline-pause outcome.

### Manual shape (`task`/`run_error`/`config`, backlog workflow) — unchanged, six values

| `next_action` | Fires | → `state` |
|---|---|---|
| `review` | default at Raise; otherwise matches no specific rule | unchanged (falls to the catch-all — `review` is a marker, not a trigger) |
| `ready_for_approval` | always (matches no more specific rule) | `re-assigned` |
| `approved` | `resolution` present (this call or a prior one) | `completed` — **refused** if same party set `ready_for_approval` |
| `reject` | always | `withdraw`/`supersede`, the party's explicit choice |
| `revise` | always | `in-progress` |
| `noted` | always | `closed` |
| *(no `next_action`, assignee changed)* | always | `re-assigned` |

**Complete** — six values, four resulting states beyond `raised`, plus the generic assignee-changed
fallback. `on-hold`/`in-progress`/`closed` remain directly settable by either party via `-State`,
independent of `next_action`, per the original design (`escalation-redesign-plan-v1` §4) — not a gap,
a deliberate second entry path for informal state changes that aren't really "decisions."

### Issue shape (`issue`, proposed new vocabulary) — three values, reasoned for completeness this round

| `next_action` | Fires | → `state` |
|---|---|---|
| `open` | every round still under discussion | `in-progress` |
| `decided` | `resolution` present (what was decided, and why) | `completed` |
| `abandoned` | `comment` present (why) | `withdraw` |
| *(no `next_action`, assignee changed)* | always | `re-assigned` — **the same generic fallback manual already has**, reused rather than inventing a fourth issue-specific value. This is literally "your turn" — handing a round to the other party |

**Deliberately no two-party check on `decided`**, unlike `approved`'s same-party refusal. Different
risk: `approved` guards against someone certifying their *own* finished work; a debate converging on
a decision isn't the same shape of risk — the researcher deciding "going with option B" alone is a
legitimate, common outcome, not something to structurally block. Stated as a considered difference,
not an inconsistency.

**New `cfg_enum` group needed:** `escalation_next_action_issue` (`open`/`decided`/`abandoned`) — a
third group alongside the existing dispatcher/manual split, same pattern.

### `notice` — settled, no vocabulary at all

`next_action` stays `NULL` for its whole life; `state='closed'` from the moment of Raise, never
revisited. **Closing the one real edge case left open in v2:** what if someone disagrees with a
notice? Answer, stated now rather than left implicit: that's a **new `issue`**, `from_id` pointing at
the notice, not a reopening of the notice itself — a notice never re-enters the decision machinery,
by design, full stop.

### `state` — all 8 active values, cross-checked against every vocabulary above

`raised`, `in-progress`, `on-hold`, `re-assigned`, `closed`, `withdraw`, `supersede`, `completed` —
**every one is reachable by at least one of the three vocabularies above; none is orphaned, none is
missing.** (`answered`/`paused`/`retracted` remain correctly retired-inactive, superseded, per v3
§configs — not re-litigated.)

---

## The PS front door — exact behaviour (D22)

Read from the live `Escalation.ps1` and `escalation.py`, not assumed:

**Client-side, before any Python runs:** `[ValidateSet(...)]` on `-Action`/`-Decision`/`-NextAction`/
`-Type`/`-AnsweredBy`/`-AssignedTo`/`-State` — PowerShell itself rejects an invalid keyword. Each
action's branch then checks required-parameter *presence* only (e.g. *"AnswerRun needs -RunId and
-Decision,"* *"-AnsweredBy required — no default"*) — on failure: a `Write-Host` yellow warning,
`exit 1`. **Nothing is recorded anywhere when this happens** — not even a crash escalation, since
Python is never invoked. This is a real, currently open gap, not theoretical: escalation `#754` (this
session's own history) was exactly a PS-side failure — a missing `-Comment` dash — that *"never
reached the escalation DB on its own... no mechanism auto-captures a PS-side terminating error as an
escalation row."*

**On success:** shells to `python -m iba.app.lib.escalation <verb> [flags] [free text]`.

**Python-side error:** `main()`'s top-level `except Exception` catches anything uncaught and
auto-raises a `run_error` via `raise_new()` — built and live-tested this session (escalations `#2`/
`#3`).

**How it lands in the engine — the two shapes diverge completely here, and this is the crux of D23:**
- **Dispatcher-tied**: the pause is created *by* `run.py` itself, mid-execution of a real dispatched
  run; `AnswerRun` resumes that same run. Fully inside the engine already.
- **Manual**: `run_id` is a synthetic `MANUAL-<timestamp>` string. `run.py` is **never invoked, at
  all** — no `run` table row is ever created for a manual Raise/Update, ever, by design (the original
  `raise_manual()` docstring stated this plainly: *"no 'run' row exists for it."*). Every manual
  escalation — which is most of them, including this entire design-plan thread's own tracking item
  `#6` — has zero execution-audit trail beyond what the escalation row itself holds.

**Proposed fix to the validation-gap specifically:** wrap the whole script in a top-level
`trap`/`try`-`catch` that, on any PS-side terminating error (not just a Python exception), still
shells out to Python to record the failure before exiting — so a bad flag combination gets the same
safety net a Python-side crash already has, instead of vanishing into terminal scrollback.

---

## Is PS the right choice, and what are the alternatives? (D23)

**The honest answer: PS isn't the problem — the specific fact that `Escalation.ps1` calls Python
directly instead of dispatching through `run.py` is, and that's the exact same gap `#8` already found
in 7 other scripts.** Making this module's own front door correct is the same fix as D16 (the report
registration's `run.py` re-plumbing), looked at from the interface side rather than the reporting
side — not a second, separate piece of work.

What that fix actually buys: a real `run` row for every manual escalation invocation, not just
dispatcher-tied ones — full execution audit trail where there is currently none; automatic
`module_blocking` coverage, uniformly, instead of only for the dispatcher shape; and the crash safety
net becomes `run.py`'s own standard handling instead of a bespoke wrapper this module had to build
for itself.

**Real alternatives considered, and why not:**

| Alternative | Why not recommended |
|---|---|
| Drop the PS wrapper, use the Python CLI directly | Loses consistency with all 44 other project scripts and the researcher's own PowerShell-primary working environment — a step backward in ergonomics for no governance gain the `run.py` fix doesn't already provide |
| A GUI/TUI tool | Real engineering cost for a single-user, low-volume tool — against `feedback_simple_steps_not_engineered_designs`, and solves nothing the dispatch fix doesn't already solve |
| Route everything through Claude, no direct researcher CLI use | The researcher already uses `Escalation.ps1` directly and unprompted (confirmed this session — self-answered a pause without being asked) — removing that would be a real regression, not an improvement |

**Recommendation: keep PS, fix the dispatch.** Nothing about PowerShell itself makes this hard to
control — an *un-dispatched* script is what's hard to control, in any language.

---

## Everything else

**Unchanged from v3** — transaction types, tables and columns, Governance's core table, automation,
configs, validation (D15 still open), scripts (carried, now supplemented by the PS spec above),
report (D16 still open). Not restated; see v3.

---

## Summary — decisions for this round

1. **D18/D20** — the produced-documentation-task pattern (an `issue`'s `decided` resolution, or a
   `task` involving code/user-facing change, spins out its own companion documentation task rather
   than trusting it'll be remembered). Confirm the pattern, or correct it.
2. **D19** — verbatim-quote-the-operative-sentence as the chat-capture convention, added to
   `cfg_escalation.chat_routing` via `configmaint.propose`.
3. **D21** — the three-value `issue` vocabulary, the shared assignee-changed fallback instead of a
   fourth value, and the no-two-party-check-on-`decided` distinction from `approved`. Confirm the
   vocabulary is complete, or name what's still missing.
4. **D22/D23** — build the PS-side crash-safety-net gap now, or hold it. And: is "keep PS, fix the
   dispatch" the right call, or is there a reason to weigh the alternatives differently than I have?
5. **Everything still open from the register** — D1–D8, D15, D16 — unresolved, not superseded by this
   round's additions.

Nothing built. Register updated to reflect this round once these are confirmed.
