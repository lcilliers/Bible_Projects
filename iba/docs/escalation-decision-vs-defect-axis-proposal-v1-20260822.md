# Escalation core model — the decision-vs-defect axis (proposal, nothing built)

**Master: #753** (open since 2026-08-21, its own v1/v3: *"a real config representation for
validate/complete rules [is] still awaiting your direction"*). **Trigger: #795** + your process
statement this session. This does **not** re-litigate D1–D28 (decision register v9) — that work is
built and approved. This is #753's own still-open item, now sharpened.

---

## 1. The problem, restated precisely

Two different working modes have been sharing one mechanism:

- **Mine, habitually:** build → hit a problem → get a quick answer → resume where I left off.
- **Yours, stated directly:** design → specify → resolve every open question by debate → validate
  → *then* build and test.

The escalation module's `type` (task/issue/run_error/config) and `shape` (dispatcher/manual)
don't encode this distinction anywhere. #795 found it concretely: the dispatcher shape's single
decision (`approve`/`reject`/`revise`/`hold`/`noted`) treats all three of approve/reject/revise
identically — `completed`, regardless — because that mechanism was built for "the run is paused,
give me one answer," not for "is this actually a decision, or just a mistake to fix."

## 2. The missing axis

Propose a new classification, independent of `type` and `shape` — tentatively `resolution_kind`:

- **`decision_required`** — something genuinely needs deciding or specifying. **Always terminal.**
  Never resumed inline. Its only valid outcome vocabulary is the rich one manual items already
  have (`ready_for_approval` → `approved`/`reject`/`revise`/`noted`) — "revise" here means *go
  refine the design*, not *try the command again*. Conceptually routes into planning, not back
  into a build.
- **`self_correctable`** — the design was already settled; what failed is my own execution against
  it. No approval gate. I fix it, state what was wrong and what changed, and (if something was
  paused) the run proceeds. Still always **recorded** — never silent — but recorded is not the
  same as gated.

## 3. Why `type` alone can't carry this — from real history, not hypothetically

- **`config`** (#787→#793→#794): the underlying proposal ("should `prose.extractor_version` exist
  at all") was `decision_required`. My own `key=NULL` insert mistake fixing the approved version of
  it was `self_correctable`. Same `type`, both kinds, back to back.
- **`run_error`**: a crash from a genuinely unhandled case is `decision_required`. A crash from a
  typo in already-specified logic is `self_correctable`. `type` doesn't distinguish these either.

So `resolution_kind` has to be set per-instance, by whoever/whatever raises the escalation — it
can't be derived from `type`.

## 4. What already exists — build on this, don't duplicate it

- `cfg_escalation_transition`/`cfg_escalation_requirement` (built in the D1–D28 pass) — the
  mechanical rule-engine skeleton is real; extend it, don't replace it.
- The manual shape's `ready_for_approval` → `approved` handshake, with D25's authority check
  (*who* may approve, not *whether the same party* may), is already the right vocabulary for
  `decision_required` — it needs to become reachable by dispatcher-tied items, not reinvented.
- The decision-register discipline itself (#6/#753, register v9) — full inventory before any
  build, explicit "not built yet" markers — is the process to reuse here, not a new one.

## 5. What accepting this axis would imply — consequences to confirm, not a build list

a. Every raise site (`raise_new`, `raise_()`, every handler's `escalate()` call) states
   `resolution_kind` at raise time — a new required field, config-driven via
   `cfg_escalation_requirement`.
b. `AnswerRun` branches on `resolution_kind`: `self_correctable` keeps something like today's flat
   decision; `decision_required` routes to the same `ready_for_approval`/`approved` handshake
   manual items use — meaning `Update()` (or its equivalent) becomes reachable for dispatcher-tied
   items under this condition. That's a real change to "two shapes, deliberately not unified,"
   which needs your explicit re-confirmation since that was previously stated as settled.
c. `run.py`'s pause-continue currently assumes one answer resumes the run. For a
   `decision_required` item raised that way (e.g. a validation step), "resuming" probably can't
   mean "re-run the same command" any more — likely the run stays terminal, the design question
   gets resolved separately, and a fresh run starts afterward. Same fork #795's proposal already
   named as option A, now a direct consequence of this axis rather than a standalone question.
d. `Escalation.ps1`/the CLI need a way to set `resolution_kind` at raise time, and updated help
   text.
e. `GOVERNANCE.md`/`USER-GUIDE.md`/`BUILD.md` get this documented in the same unit of work as any
   build — the existing standing rule, not a new one.

## 6. Open questions — nothing decided, no code touched

1. Is `resolution_kind` (two values) the right shape, or did you have a different mechanism in
   mind?
2. For a `decision_required` item raised via pause-continue — option A (the process terminates,
   the decision is resolved later, a fresh run starts afterward) or option B (the process stays
   paused until the richer flow's first stage completes), from #795's earlier proposal — now
   framed as a consequence of this axis rather than standalone?
3. Should `resolution_kind` be required with no default on every raise, or should some paths get a
   sensible default (e.g. the crash-wrapper defaults to `decision_required` unless the handler says
   otherwise)?
4. Does this stay as #753's own next decision point, or does its scope warrant becoming its own
   master thread?

## 7. What I am not doing

Not proposing `cfg_*` row content. Not touching `escalation.py`. Not touching `run.py`. Staying at
the concept/design level until the open questions above are answered.
