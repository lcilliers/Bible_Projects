# Escalation core model — decision-vs-defect axis (v2, built out)

**Escalation #798** (`from_id=753`, the master). Replaces v1 (kept for history). Your v2 response:
principles agreed; build the proposal out with the governance config for the working method
itself, the full script impact list, literal config wording for every change, §5's items all in
scope — with open questions listed at the end, not decided by me. Still **nothing built**.

---

## 1. The governance rule — the working method, for all development work

This is broader than escalation.py. It's the general rule; `resolution_kind` (§2) is escalation's
own mechanical enforcement of it for escalation-raised items specifically. Not every decision has
to go through an escalation row (a plan doc + chat approval, as used for the prose-store work this
session, is an equally valid way to route to design) — the rule is about the *distinction*, not
about mandating one specific channel.

**New `cfg_behaviour_rule` row** (class `development`, alongside the existing `root-fix-not-one-off`,
`simple-steps-not-engineered-designs`, etc.):

```
class:        development
rule_key:     decision-points-are-terminal-not-inline
rule_text:    When building or validating anything -- code, config, or process -- a point that
              requires a NEW decision (a judgement call, an ambiguity, something not already
              specified) is TERMINAL: it must not be answered inline and resumed. It is recorded
              as an open item and routed back into design/specification; work resumes only after
              the design is settled and approved. A point that instead reveals Claude's own
              execution error against an ALREADY-settled, already-approved design (a typo, a
              wrong parameter, a slip) is SELF-CORRECTABLE: Claude fixes it directly, records what
              was wrong and what changed, and continues -- no new approval is required, because no
              new decision was made. The distinguishing question is always: does resolving this
              require deciding something new, or only correcting execution against something
              already decided?
source:       researcher, 2026-08-22, escalation #798 v2
enforced_by:  escalation.resolution_kind (decision_required | self_correctable) for
              escalation-raised items -- see cfg_enum 'resolution_kind' and
              cfg_escalation_requirement below. Not mechanically enforced outside escalations
              (e.g. a plan-doc-and-chat-approval cycle also satisfies this rule; nothing currently
              checks that one happened).
active:       1
```

## 2. The `resolution_kind` axis itself

**New `cfg_enum`** (2 rows):
```
name: resolution_kind   value: decision_required   ordinal: 0
name: resolution_kind   value: self_correctable     ordinal: 1
```

**New `cfg_escalation_requirement` rows** (mirrors how `comment` is already required at Raise):
```
action: raise    field: resolution_kind   condition_key: always   check_kind: field_required
  message: "resolution_kind is required at Raise -- decision_required or self_correctable
            (cfg_enum resolution_kind). See cfg_behaviour_rule
            'decision-points-are-terminal-not-inline'."
```
One row, `action='raise'` — this applies to **both** shapes (manual and dispatcher-tied) equally,
since the axis is meant to cut across the shape split, not respect it.

## 3. Every script this actually touches — checked live, not guessed

**Raise sites that need to start supplying `resolution_kind`** (11 `escalate()` calls + 3
dispatcher-tied `esc_raise()`/`raise_()` calls, all found by grep, not assumed complete from
memory):

| File | Line | Current type | `resolution_kind` this call should probably carry (my read, not decided — see open questions) |
|---|---:|---|---|
| `iba/app/handlers/candidate.py` | 288 | (per step) | needs review — not inspected in this pass |
| `iba/app/handlers/candidate.py` | 416 | (per step) | needs review |
| `iba/app/handlers/candidate.py` | 702 | (per step) | needs review |
| `iba/app/handlers/cluster.py` | 125 | (per step) | needs review |
| `iba/app/handlers/configmaint.py` | 406 | config (`validate`) | needs review |
| `iba/app/handlers/configmaint.py` | 558 | config (`propose`) | `decision_required` — a config proposal is always a new decision by definition |
| `iba/app/handlers/lexicon.py` | 214 | (per step) | needs review |
| `iba/app/handlers/narrative.py` | 187 | (per step) | needs review |
| `iba/app/handlers/passage.py` | 332 | (per step) | needs review |
| `iba/app/handlers/raw.py` | 94 | (per step) | needs review |
| `iba/app/handlers/reports.py` | 65 | issue (`validation_word`/`validation_book`) | `self_correctable` in the common case (a known/expected finding to acknowledge) but can legitimately be `decision_required` (a genuinely new kind of finding) — this one call site may need to pass it in as a parameter, not hardcode one value |
| `iba/app/run.py` | 192 | run_error (crash) | `decision_required` by default (an uncaught exception is, by definition, a case nobody decided how to handle) unless the crash message itself indicates a known/re-occurring pattern |
| `iba/app/run.py` | 223 | task/issue/config (pause-continue) | depends on the handler's own `escalate()` call — carries through from whichever value that call supplied |
| `iba/app/run.py` | 244 | run_error (report-stop) | same reasoning as the crash case |

**8 more `escalate()` sites I haven't individually inspected this pass** (candidate.py ×3,
cluster.py, configmaint.py's `validate` step, lexicon.py, narrative.py, passage.py, raw.py) — each
needs its own short review of what it's actually asking, before a `resolution_kind` default can be
assigned. Not guessing these — see open question 5.

**Also touched, not raise sites but consumers/surface:**
- `iba/app/handlers/base.py` — `escalate()`'s own signature gains a `resolution_kind` parameter.
- `iba/app/lib/escalation.py` — `raise_new()`, `raise_()`, `answer_for_run()`, `update()`,
  `_check_requirements()` all need to know about the new field; `answer_for_run()` needs the actual
  branching logic (§4b).
- `iba/app/run.py` — the pause-continue block's resume semantics (§4c).
- `iba/app/ps/Escalation.ps1` — new `-ResolutionKind` parameter on `-Action Raise`; help text.
- `python -m iba.app.lib.escalation` CLI (`_dispatch()` in `escalation.py`) — new `--resolution-kind`
  flag on the `raise` verb.
- `GOVERNANCE.md`, `USER-GUIDE.md`, `BUILD.md` — same unit of work, per existing standing rule.

## 4. Section 5's items, built out with literal content

### 4a. Raise-time requirement
Covered in full in §2 above — the `cfg_escalation_requirement` row is the literal content.

### 4b. `AnswerRun` branching on `resolution_kind`

This is the one piece that is **not** just new config rows — it's a real code branch, because the
two `resolution_kind` values need genuinely different downstream mechanics, not just different
target values in the same shape:

- `self_correctable` → keeps today's dispatcher mechanism as-is: `AnswerRun -Decision
  Approve|Reject|Revise|Hold|Noted`, resolved via `cfg_escalation_transition` (shape=`dispatcher`)
  exactly like now.
- `decision_required` → routes to the **manual** shape's own machinery instead:
  `ready_for_approval` → `approved`/`reject`/`revise`/`noted`, with D25's authority check. This
  means `Update()`'s current hard refusal of any dispatcher-tied item (`"answer it via AnswerRun,
  not Update"`) needs a carve-out: refuse *unless* `resolution_kind='decision_required'`, in which
  case allow it through the same path a manual item uses.

This is the one place I'd be writing real logic into `escalation.py`, not just adding config rows
— flagged plainly, not disguised as "just config."

### 4c. `run.py` pause-continue semantics for `decision_required`

For a step that pauses via `escalate()` with `resolution_kind='decision_required'` (e.g. a
validation step raising a genuinely new kind of finding): today, re-running the exact same command
checks `answered_for_run()` and reports success/ack based on whatever decision was given. Under
this design, since the decision now goes through the *manual* multi-stage flow instead, there's no
longer a single moment where "the decision is in" — `ready_for_approval` and `approved` can be
far apart in time, by different parties. Concretely, `run.py`'s pause-continue block would need to
either:
- stop treating this class of pause as literally resumable at all (mark the run `failed`/terminal
  immediately, same shape as a `run_error`, with the escalation living independently) — this is
  option A from #795's earlier proposal, or
- keep the run paused indefinitely and let `run.py` re-check on each invocation whether the manual
  flow has reached `approved` yet, rather than any single answer — option B.

**Not choosing between these here — open question 2.**

### 4d. CLI / PS surface

- `Escalation.ps1 -Action Raise` gains `-ResolutionKind DecisionRequired|SelfCorrectable`
  (`ValidateSet`), required (no default — matching the existing "no silent default" discipline
  from the `originator` fix).
- `python -m iba.app.lib.escalation raise ... --resolution-kind=decision_required|self_correctable`,
  same requirement.
- Dispatcher-tied raises (`escalate()` calls in handler code) take `resolution_kind` as a real
  Python parameter, not a CLI flag — the handler author decides it in code, per row in §3's table.

### 4e. Documentation

- `USER-GUIDE.md` sec4 (the escalation reference) — new subsection on `resolution_kind`, updated
  `-Action Raise` flag reference.
- `GOVERNANCE.md` — new entry for `cfg_behaviour_rule
  decision-points-are-terminal-not-inline`, same unit of work as the config change (existing
  standing rule, `governance.governance_md_on_rule_change`).
- `BUILD.md` — new section recording the build, once it happens.

---

## 5. Open questions — nothing decided, no code touched

1. §3's per-call-site `resolution_kind` assignments are my first read, not confirmed — 8 call
   sites (`candidate.py` ×3, `cluster.py`, `configmaint.py`'s `.validate` step, `lexicon.py`,
   `narrative.py`, `passage.py`, `raw.py`) need their own individual review before any default is
   assigned. Do you want that review done as part of this same build, or decided case-by-case as
   each one is actually touched?
2. §4c — option A (pause-continue for `decision_required` becomes terminal, same as `run_error`)
   or option B (stays paused, `run.py` re-checks for `approved` on each re-invocation)?
3. §4b is real new logic in `escalation.py`, not just config — confirm that's acceptable scope for
   this build, given the process this whole proposal is following is specifically about not
   building without confirming first.
4. Should `reports.py`'s `validation_word`/`validation_book` (the one call site that's
   legitimately sometimes one kind and sometimes the other) take `resolution_kind` as a parameter
   the *handler's own logic* decides at runtime (e.g. "is this finding already in the known-issues
   list"), or should it always default to one value and let the researcher override at answer
   time?
5. Does this build happen as one pass (matching #6/#753's own "full build pass complete" precedent
   once its design settled), or in stages with review points in between, given its size (11+ call
   sites, 2 CLI surfaces, `escalation.py` internals, `run.py` internals, 3 docs)?
