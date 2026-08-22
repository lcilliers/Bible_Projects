# Escalation core model — decision-vs-defect axis (v4, CONSOLIDATED)

**Escalation #798** (`from_id=753`). **This is the one document — supersedes v1/v2/v3 entirely,
stands alone, nothing to cross-reference.** Still nothing built. Per your instruction: build
starts only once this single document has every config value literal, every code change specified
in enough detail that no decision remains at code-writing time, every stage has a concrete test,
and documentation updates are named explicitly.

**What changed since v3, honestly, so nothing is hidden:** three of the nine `escalate()` sites I
called `decision_required` in v3 were wrong — I checked the actual code and found the real problem
in each is a missing or unenforced config threshold, not a genuine recurring decision. One site
(`candidate.py`) I included at all without checking whether it's even live. Both are corrected
below, not papered over.

---

## §1 — the governance rule (unchanged from v2/v3, restated in full)

**New `cfg_behaviour_rule` row:**
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
              already decided? A recurring decision_required outcome on the same routine, run
              after run, is itself a defect -- it means a threshold or parameter that should have
              been specified once, in config, during design, was left to be re-asked every time
              instead. That is a design gap to close (add the missing config), not a pattern to
              formalise.
source:       researcher, 2026-08-22, escalation #798 v2/v4
enforced_by:  escalation.resolution_kind (decision_required | self_correctable) for
              escalation-raised items -- see cfg_enum 'resolution_kind' and
              cfg_escalation_requirement below.
active:       1
```
(Last sentence added in v4, per your point that constant `decision_required` output is itself a
design failure — makes that principle part of the rule text, not just this document's prose.)

## §2 — the `resolution_kind` axis (unchanged from v2/v3, restated in full)

**New `cfg_enum`:**
```
name: resolution_kind   value: decision_required   ordinal: 0
name: resolution_kind   value: self_correctable     ordinal: 1
```

**New `cfg_escalation_requirement` row:**
```
action: raise    field: resolution_kind   condition_key: always   check_kind: field_required
  message: "resolution_kind is required at Raise -- decision_required or self_correctable
            (cfg_enum resolution_kind). See cfg_behaviour_rule
            'decision-points-are-terminal-not-inline'."
```

---

## §3 — every `escalate()` site, final, no site left unreviewed

### §3.0 — Excluded: `candidate.py` (3 sites)

Checked live before including anything: `cfg_work_package` rows `set-candidates`,
`candidate-quality`, `candidate-curation`, `seed-candidate-report` are **all `inactive=1`**. All
three `candidate.py` `escalate()` calls (lines 288, 416, 702) are unreachable dead code today.
Out of scope entirely — not classified, not fixed, not touched. Revisit only if/when one of these
work packages is reactivated.

### §3.1–§3.3 — genuinely `decision_required`, design already sound

Checked each of these three against the same standard §3.4–§3.6 failed: does it only fire on a
real, non-trivial finding, or unconditionally on every run?

| Site | Gate before `escalate()` fires | Verdict |
|---|---|---|
| `cluster.py:125` (`cluster.validate`) | `if not total_findings: return ok(...)` — silent pass on zero exceptions | Sound. `decision_required`: each exception set is a novel case, no pre-approvable threshold exists for *which* strongs may lack a link. |
| `lexicon.py:214` (`lexicon.validate`) | `if not total_findings: return ok(...)` | Sound, same reasoning. |
| `configmaint.py:406` (`configmaint.validate`) | `if not any(preset.values()): return ok(...)` | Sound, same reasoning. |

All three: `resolution_kind = decision_required`, hardcoded at the call site — confirmed, not
guessed, by reading the gate that precedes each one.

### §3.4 — `narrative.py:187` — NOT `decision_required`. A real code gap, config already exists.

`narrative.generate_max_cost` (currently `3.00`) **already exists** and is **already enforced**
as a hard `fail()` at lines 151–156 when the estimated cost exceeds it — this already matches your
"if spend above, that's a failure requiring review of call vs. limit" exactly, correctly built.

**The actual gap:** when the estimated spend is *within* the approved cap, the code still pauses
and asks for approval every single call (line 187) instead of proceeding. The approved cap **is**
the approval, per §4b's own rule — asking again adds nothing.

**Fix, specified in full (self_correctable-shaped once approved — this is fixing code to match a
principle you've already stated, not a new decision):**
- Delete the `answered_for_run()` check (lines 161–167) and the `escalate()` call (lines 187–198).
- The function's flow becomes: assemble package → cap check (unchanged) → **directly** call
  `narrativegenerate.call_api(package)`, exactly the code currently under `if decision != "reject"
  and decision != "revise"` — no branch, no pause, since there is no longer a decision pending.
- Net effect: `book-narrative` becomes a single-invocation operation for any call within the
  approved cap. Only over-cap calls still involve any decision (the cap-raise, already correctly
  a `fail()` today, unaffected by this fix).

### §3.5 — `passage.py:332` — NOT `decision_required`. Missing thresholds — **your input needed, not mine to invent.**

Checked: `validate()` computes the live distribution and calls `escalate()` **unconditionally on
every run**, with no threshold check of any kind. This is exactly the "ask every time" pattern you
named as a design failure.

**Fix, partially specified — two literal values are missing and I have no basis to choose them:**
- **New `cfg_setting passage.max_single_verse_pct`** — escalate only if `single/total*100` exceeds
  this. *Value: not proposed — genuinely yours to set.*
- **New `cfg_setting`** for an acceptable average-verses-per-passage band (e.g.
  `passage.min_avg_verses` / `passage.max_avg_verses`) — escalate only if the live average falls
  outside it. *Values: not proposed — same reason.*
- **Code change:** `validate()` keeps computing the distribution exactly as now, but only reaches
  `escalate()` if a bound is breached; otherwise returns `ok(...)` directly — same shape as
  §3.1–§3.3.

I can't finish this site's specification without those two numbers. **Open input 1, below.**

### §3.6 — `raw.py:94` — NOT `decision_required`. Registration is researcher-instructed; re-asking is redundant.

Checked `discover()` in full: when `seeds` is empty, it unconditionally escalates
`"{word!r} maps to no strongs. Register anyway, or reject?"` — every time, for every word that
resolves to zero strongs, regardless of the fact that the researcher already named this exact word
for registration.

**Fix, specified in full — one value needs your confirmation:**
- **New `cfg_setting raw.zero_strongs_action`** (`cfg_enum`: `proceed` | `reject`). *Proposed
  literal default: `proceed`* — reasoning: naming the word for registration is itself the
  researcher's approval; a downstream zero-match result doesn't undo that. **Confirm or override —
  open input 2, below.**
- **Code change:** replace the `escalate("zero-strongs", ...)` call with:
  ```
  if not seeds:
      action = ctx.cfg.setting("raw.zero_strongs_action", "proceed")
      if action == "reject":
          return fail("zero-strongs", f"{ctx.word!r} maps to no strongs (raw.zero_strongs_action=reject)")
      return ok(f"{ctx.word!r} maps to no strongs — proceeding per raw.zero_strongs_action=proceed",
                word_strong_new=0)
  ```
  (There are no `word_strong` rows to write when `seeds` is empty either way — "proceed" means
  "let registration continue with zero strongs," not "write something anyway.")

### §3.7 — `reports.py:65` (`validation_word`/`validation_book`) — built now as `decision_required`, per your explicit instruction

Your words: *"§6.1 build these now as decision_required. I will very quickly complain if there are
missing configs when these modules are run."* Taken as: ship uniformly `decision_required` for
this pass; the per-check classification v3 raised as a smaller open question is **not** being
built now. Accepted, on the record, that if this fires often because a check's own threshold
should have been config (the same class of gap §3.4/§3.5/§3.6 just found), that's a real finding
to bring back, not something I'm claiming won't happen.

---

## §4 — Crash / report-stop (`run.py` lines 192, 244) — "pure coding logic," self_correctable-first

Your correction: these are code-bug territory by nature, not open design questions. Model:

1. Raised as `self_correctable` by default.
2. Claude investigates and fixes.
3. **If the fix reveals the problem isn't just execution — it needs new information or a genuine
   decision** — the **same item** converts to `decision_required` (not closed-and-reopened), with
   `tried` recording exactly what was attempted first. This is the mechanism you named as `tried`'s
   original purpose.

**New transaction needed** (name not yet fixed — proposing `escalate_to_decision()`, open to a
better name): takes an existing `self_correctable` escalation id, requires a non-empty `tried`
value describing the failed attempt, flips `resolution_kind` to `decision_required`, forces
`type='issue'`, and from that point behaves exactly like any other `decision_required` item
(§5 below) — including the run terminating `failed` if it hadn't already.

---

## §5 — `decision_required`'s full effect (unchanged from v3, confirmed correct)

1. The run terminates immediately, `run.state = 'failed'`.
2. An escalation is auto-raised (or, per §4, an existing `self_correctable` one is converted),
   `type` forced to `issue` regardless of what type the raising code would otherwise pick.
3. Nothing resumes this run. A **fresh run**, started once the issue reaches a settled, approved
   answer, is the test.

## §6 — `self_correctable`'s full effect (unchanged from v3, confirmed correct)

- No `approve`/`reject`/`revise`/`hold`/`noted` vocabulary. `AnswerRun` is never invoked.
- Flow: raised → Claude fixes → Claude records the resolution → closes. No approval gate.
- If it paused a run: fixed → Claude re-runs the same `run_id`/command (the existing informal
  pattern from this session, formalised).
- Bound strictly by §1's own rule: valid only when the fix makes reality match something
  *already, specifically* approved. The moment new judgement is needed, §4's conversion applies —
  it is never Claude's call to quietly stay in `self_correctable` and decide anyway.

## §7 — split out, not solved here: the debugging/logging rethink

Your words: *"this need a rethink of the debugging and logging in the code to trap errors. current
code seems to be sloppy."* This is its own investigation — not answerable as a `resolution_kind`
default, and not something I'm folding a rushed answer into here. **Proposing to raise this as its
own separate escalation once #798 itself is approved**, so it gets the same design-first treatment
rather than a hasty fix inside this document. Not raised yet — confirm you want it split out this
way (open input 3, below), rather than assuming.

---

## §8 — Consolidated config list (every literal value, in one place)

| Table | Row | Value |
|---|---|---|
| `cfg_behaviour_rule` | `development` / `decision-points-are-terminal-not-inline` | full text in §1 |
| `cfg_enum` | `resolution_kind` = `decision_required` | ordinal 0 |
| `cfg_enum` | `resolution_kind` = `self_correctable` | ordinal 1 |
| `cfg_escalation_requirement` | `raise` / `resolution_kind` / `always` / `field_required` | message in §2 |
| `cfg_setting` | `passage.max_single_verse_pct` | **value needed from you (open input 1)** |
| `cfg_setting` | `passage.min_avg_verses` / `passage.max_avg_verses` | **values needed from you (open input 1)** |
| `cfg_setting` | `raw.zero_strongs_action` | proposed `"proceed"` (**confirm — open input 2**) |

No other new `cfg_*` rows in this proposal. `narrative.py`'s fix (§3.4) needs **no new config** —
`narrative.generate_max_cost` already exists.

## §9 — Consolidated code-change list (every file, in one place)

| File | Change |
|---|---|
| `iba/app/lib/escalation.py` | `raise_new()`/`raise_()` require + store `resolution_kind`; `decision_required` forces `type='issue'` at creation; new `escalate_to_decision()` transaction (§4); new self-close transaction for `self_correctable` (no `AnswerRun` path) |
| `iba/app/run.py` | Pause-continue/crash/report-stop branch on `resolution_kind`: `decision_required` → terminate `failed`; `self_correctable` → stays retryable via same-`run_id` re-invocation |
| `iba/app/handlers/base.py` | `escalate()` gains a `resolution_kind` parameter |
| `iba/app/handlers/cluster.py`, `lexicon.py`, `configmaint.py` | Pass `resolution_kind="decision_required"` at their existing `escalate()` calls — no other change |
| `iba/app/handlers/narrative.py` | §3.4's fix — remove the pause, spend proceeds automatically within the existing cap |
| `iba/app/handlers/passage.py` | §3.5's fix — add the threshold check, escalate only on breach (pending your 2 values) |
| `iba/app/handlers/raw.py` | §3.6's fix — config-driven zero-strongs branch, no escalation |
| `iba/app/handlers/reports.py` | Pass `resolution_kind="decision_required"` at `_validation_outcome()`'s `escalate()` — no other change (§3.7) |
| `iba/app/ps/Escalation.ps1` | New `-ResolutionKind DecisionRequired\|SelfCorrectable` on `-Action Raise`, required |
| `iba/app/lib/escalation.py` CLI (`_dispatch`) | New `--resolution-kind=` flag on the `raise` verb, required |

## §10 — Documentation updates, named explicitly

- **`GOVERNANCE.md`** — new section (next available number) recording `cfg_behaviour_rule
  decision-points-are-terminal-not-inline` in full, alongside the existing `development`-class
  rules (`root-fix-not-one-off`, etc. — matches their existing presentation).
- **`USER-GUIDE.md`** sec4 (the escalation reference) — new subsection explaining
  `resolution_kind`, the two flows (§5/§6), and the updated `-Action Raise` flag reference
  including `-ResolutionKind`.
- **`BUILD.md`** — one new section per build stage (§11) as it lands, not a single section at the
  end — matches the existing standing practice for this file.
- Each of the above updated **in the same unit of work as the stage that makes it true** (existing
  standing rule, not a new one) — not batched to a final documentation pass.

## §11 — Build stages, with concrete tests (not vague)

**Stage 1 — pure config.** §1/§2's rows + §8's `passage.*`/`raw.zero_strongs_action` rows (once
their values are supplied).
*Test:* `Config-Maintenance.ps1 -Step Validate` exits clean. Then, on a scratch copy of `iba.db`:
`python -m iba.app.lib.escalation raise "test" --originator=Claude --comment=test` (no
`--resolution-kind`) must fail with the new requirement's exact message.

**Stage 2 — `escalation.py` internals.** `resolution_kind` storage, `decision_required` forcing
`type='issue'`, the new `escalate_to_decision()` transaction, the new `self_correctable`
self-close transaction.
*Test (scratch DB):* raise one `decision_required` item and one `self_correctable` item via the
CLI directly; confirm the first has `type='issue'` regardless of what `--type` was passed, confirm
the second has no reachable `AnswerRun` path (attempting it should refuse, citing `resolution_kind`);
close the `self_correctable` one via its new transaction and confirm `state='completed'` with the
resolution text stored; convert it to `decision_required` instead via `escalate_to_decision()` and
confirm `tried` is required and stored.

**Stage 3 — `run.py`.** Branch pause-continue/crash/report-stop on `resolution_kind`.
*Test:* one real work-package run forced down each path (e.g. `configmaint.propose` for
`decision_required`; a deliberately-broken but easily-fixed step for `self_correctable`) — confirm
`run.state` and the escalation's fields match §5/§6 exactly, on the real DB, not a scratch copy.

**Stage 4 — the handler sites.** §3's 6 live sites (cluster/lexicon/configmaint unchanged classify;
narrative/passage/raw's actual fixes; reports.py's pass-through).
*Test:* re-run each of the 6 affected steps live: `cluster.validate`, `lexicon.validate`,
`configmaint.validate` should raise `decision_required`/`type=issue` exactly as before but now
with the field populated; `book-narrative generate` on a within-cap book should complete in one
call with no pause; `passage.validate` should return `ok()` on an in-bounds live distribution and
only escalate if temporarily given an out-of-bounds config value to force it; `new-word` on a
real zero-strongs word should complete per `raw.zero_strongs_action` with no pause.

**Stage 5 — CLI/PS + docs, same unit of work as the stage each belongs to** (§10) — not a separate
stage on its own.

---

## Open inputs needed from you before this can be finished (not decisions I'm making)

1. §3.5 — the two `passage.*` threshold values (`max_single_verse_pct`, and the avg-verses band).
2. §3.6 — confirm `raw.zero_strongs_action` defaults to `proceed`, or tell me it should be
   `reject`.
3. §7 — confirm the debugging/logging rethink should be raised as its own separate escalation
   once #798 is approved, rather than folded in here.
4. §4's new `escalate_to_decision()` transaction name — acceptable, or you have one you prefer.
