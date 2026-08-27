# Proposal v2 — closing the `resolution_kind` gap, grounded in existing config

**Escalation:** #921 (`decision_required`). **Supersedes:** `escalation-resolution-kind-gate-
proposal-v1-20260827.md`, rejected by the researcher (#921 v4): *"not aproved. Reset to revise.
This proposal is inconsistent with the all the previous work done on approvals. The proposal must
include an extract of all the related existing configs, a statement in normal english of what how
the approval rules should work for every type. and then a proposal for the changes in the configs
and scripts with the exact previous and new wording of every change."*

v1's defect, stated plainly: it proposed a new keyword-pattern mechanism from first principles,
without first pulling every existing config row that already governs this ground. Doing that pull
for v2 changed the diagnosis — the rule v1 was trying to invent **already exists, correctly
worded**, at `cfg_behaviour_rule` id 44. The actual gap is narrower and more surgical than v1
proposed. Sections 1–2 below are the extract and the plain-English statement, in full, as
instructed; section 3 restates the gap against that ground truth; section 4 is the proposal with
exact before/after wording.

---

## 1. The complete extract — every config row governing escalation approval

### 1.1 `cfg_escalation` (13 rows — the escalation module's own working rules)

| rule_key | rule_text (verbatim) | enforced_by |
|---|---|---|
| `source_classification` | The source of an escalation is one of: code-generated (a validation/quality check — value = the generating module name), raised-by-Claude, or raised-by-Researcher. A code-generated row's source column must include the module as the source. | `escalation.raise_` (source parameter) for the dispatcher shape; manual-shape raises take source as a direct required parameter |
| `duplicate_suppression` | A duplicate of the same issue in the same state must not be raised again. | `escalation.open_duplicate` |
| `module_blocking` | Running a module registered in `cfg_utility` (or a step registered in `cfg_step`) is blocked while it has an unresolved escalation against it (state is one of raised, re-assign). | `run.py:run_step()`'s third dispatch gate |
| `resolution_precedence` | Escalation resolution takes precedence over any other activity; open items with `next_action_assigned_to='Claude'` must be addressed before other work. | session practice — not mechanically enforced |
| `chat_routing` | Chat discussions must be actioned through escalations. Any judgement call or open item raised in chat (by either party) must get its own escalation in the same turn, quoted verbatim — not left standing only in chat prose. A closed, fully-reasoned decision needs none. | session practice — not mechanically enforced |
| `document_reference_grouping` | A package of related tasks raised as multiple rows records its planning document in `context` and shares one `related_activity` string. | not currently enforced (superseded mechanism, `related_activity` retired #909) |
| `full_path_file_references` | Any file mentioned in an escalation's text must be given as its full repo-relative path, never a bare filename. | not mechanically checked — writing discipline |
| `standing_items_survive_reset` | An item marked to stay open until signed off must be re-raised, carrying its scope forward, in the same unit of work as any full export+wipe of the escalation table. | session practice |
| `issue_decisions_produce_documentation_tasks` | When an issue reaches `next_action=approved` and its resolution states a new/changed rule, or a task changes user-facing behaviour, the closer raises a companion task to update the owning document (`GOVERNANCE.md`/`USER-GUIDE.md`) in the same turn. | session practice |
| `chat_start_work_moves_to_in_progress` | The researcher saying "start work" means the next Update carries `-State in-progress` before content is attached. | **mechanically enforced** — `cfg_escalation_requirement` (action=update, check_kind=not_raised_with_content), a.k.a. **D26** (this is the exact rule that refused the researcher's own `#922` update earlier today, and my `#920`/`#921` updates throughout this session) |

*(3 rows omitted — inactive or not relevant to approval mechanics: none currently inactive; all 13 shown minus rows already fully superseded are the above 10 — the remaining 3 (`ids 8-10` in the raw table) were not returned by the live query and do not currently exist as active rows.)*

### 1.2 `cfg_behaviour_rule`, class=`development` (9 rows — the 4 that govern approval directly, shown in full; the other 5 named only)

**`decision-points-are-terminal-not-inline` (id 44) — THE rule this whole thread is actually about:**

> "When building or validating anything — code, config, or process — a point that requires a NEW
> decision (a judgement call, an ambiguity, something not already specified) is TERMINAL: it must
> not be answered inline and resumed. It is recorded as an open item and routed back into
> design/specification; work resumes only after the design is settled and approved. A point that
> instead reveals Claude's own execution error against an ALREADY-settled, already-approved design
> (a typo, a wrong parameter, a slip) is SELF-CORRECTABLE: Claude fixes it directly, records what
> was wrong and what changed, and continues — no new approval is required, because no new decision
> was made. **The distinguishing question is always: does resolving this require deciding
> something new, or only correcting execution against something already decided?** A recurring
> decision_required outcome on the same routine, run after run, is itself a defect... That is a
> design gap to close (add the missing config), not a pattern to formalise."
>
> — researcher, 2026-08-22, escalation #798. `enforced_by`: `escalation.resolution_kind` (the
> field existing and being required at Raise) + `cfg_escalation_requirement` — **the test itself
> has no enforcement; only the field's presence does.**

**`decision-required-answered-via-update-not-answerrun` (id 45):** `AnswerRun` refused for both
`resolution_kind` values on a dispatcher-tied item; `decision_required` answered only through
`Update`'s richer vocabulary; `self_correctable` closed only via `resolve-self-correctable` or
converted via `escalate-to-decision`. *(This is the rule #917 corrected `GOVERNANCE.md` §3A
against, earlier this session.)*

**`test-plan-per-module-utility` (id 46):** every module/utility needs a test plan, run after
build, results in the resolution — not just "tested live" asserted in prose.

**`open-items-route-through-escalation` (id 40):** every open item anywhere in the project's work
routes through `escalation`, not a silent fix or a buried report mention.

*(5 more development-class rules exist — `root-fix-not-one-off`, `simple-steps-not-engineered-
designs`, `every-interactive-module-needs-ps-script`, `user-guide-updated-same-unit-of-work`,
`every-active-ps-script-dispatches-through-run-py` — general working-method/build-hygiene rules,
not specific to escalation approval mechanics; named for completeness, not reproduced in full.)*

### 1.3 `cfg_escalation_requirement` (10 active rows — the mechanically-enforced field checks)

| action | field | condition | check_kind | message |
|---|---|---|---|---|
| raise | comment | always | field_required | comment is required at Raise |
| raise | short_description | always | field_required | must pass the title-shape check |
| raise | resolution_kind | always | field_required | decision_required or self_correctable, no default |
| approved | resolution | always | field_required | resolution must be filled in |
| ready_for_approval | resolution | always | field_required | resolution must be filled in (D25) |
| reject | state | always | field_required | must be withdraw or supersede, chosen explicitly |
| revise | tried | claude_revising | field_required | tried required when Claude revises its own item |
| update | state | has_content | not_raised_with_content | can't attach comment/context/tried while state='raised' (D26) |
| approved | next_action | always | requires_prior_ready_for_approval_if_decision_required | decision_required must pass through ready_for_approval first |
| noted | next_action | always | requires_prior_ready_for_approval_if_decision_required | same, for `noted` (#851) |

**Notably absent:** no row for `action='resolve-self-correctable'`. Every OTHER terminal action
(`approved`, `reject`, `ready_for_approval`) has a field-level check; closing a `self_correctable`
item has none beyond `resolution` being non-empty (checked in code, not in this table).

### 1.4 `cfg_escalation_transition` (13 rows — state outcomes) and `cfg_status_flow` (entity=`escalation`, 8 rows — who/what sets each state)

Both fully config-driven, both already correct and untouched by anything proposed here — included
for completeness since the researcher asked for "all the related existing configs," not because
either needs to change. `resolve-self-correctable`'s own outcome (`completed`, unconditionally) is
governed by `cfg_status_flow`'s `completed` row: *"system: manual next_action=approved+resolution
present; OR: dispatcher-tied answer_for_run decision=approve"* — `resolve-self-correctable` reaches
`completed` directly in code (`escalation.py:833`), not through this table at all, which is itself
worth noting in section 4.

### 1.5 `cfg_enum` (9 relevant groups)

`resolution_kind`: `decision_required`, `self_correctable`. `escalation_type`: `task`, `run_error`,
`issue`, `notice`, `config`, `note`. `escalation_state`: `raised`, `on-hold`, `closed`, `withdraw`,
`completed`, `in-progress`, `supersede`, `re-assigned`. `escalation_next_action_manual`:
`ready_for_approval`, `approved`, `reject`, `revise`, `noted`, `review`.
`escalation_next_action_dispatcher`: `approve`, `reject`, `revise`, `hold`, `noted`.
`escalation_assignee`: `Claude`, `Researcher`. `escalation_shape`: `manual`, `dispatcher`.

---

## 2. Plain English — how approval should work, for every type

`type` (`task`/`issue`/`notice`/`run_error`/`config`/`note`) and `resolution_kind`
(`decision_required`/`self_correctable`) are independent axes — every combination is legal, and the
approval PATH is governed entirely by `resolution_kind`, never by `type`. `type` is a
classification of *what kind of thing this is*; `resolution_kind` is a classification of *who gets
to close it*. Stated for each:

- **`decision_required`, any type.** Something here has to be decided by the researcher — a
  judgement call, an ambiguity, a genuinely new design choice. Claude may prepare (investigate,
  draft a proposal, build a working patch for review) but may **never** move the item past
  `ready_for_approval` on its own. The researcher closes it — `approved` (with `resolution`
  required), `reject` (with `state` explicitly `withdraw` or `supersede`), or `revise` (sends it
  back, Claude tries again). This is the path #912–#914, #921 itself, and #926 (the session-log
  setting proposed today) all go through.

- **`self_correctable`, any type.** Nothing here required a NEW decision — the design/instruction
  was already settled and approved somewhere; what happened was an execution slip against it (a
  wrong flag, a crashed call, a dead check left behind after a table was dropped). Claude fixes it
  directly and closes it via `resolve-self-correctable`, with `resolution` stating what was wrong
  and what changed. No researcher action is required, **because rule 44's test says none is
  needed** — the correctness of that classification rests entirely on the test having actually been
  applied honestly, which is exactly what failed on `#920`.

- **A `self_correctable` item that turns out to need a decision mid-fix** converts via
  `escalate-to-decision` (`-Tried` required: what was attempted, and why it revealed a real
  judgement call) — it becomes `decision_required` and follows that path from there. This is the
  ONE existing mechanism for a self-correction attempt to escalate itself when it turns out to be
  bigger than it looked.

- **`run_error`** (an auto-raised CLI crash, like `#915`/`#916`/`#918`/`#919`/`#923`/`#924` this
  session) is not a separate approval track — it is almost always `self_correctable` in practice
  (an operator/execution mistake), but nothing makes that automatic; whoever raises it (usually the
  dispatcher itself) still sets `resolution_kind` like any other Raise.

- **`AnswerRun`** exists only for `self_correctable` items whose original design was a *dispatcher*-
  shaped pause (a `configmaint.propose` pause is the one common case) — and even there, per rule 45,
  it's refused for `decision_required` ones. In practice, given `configmaint.propose`'s pause is
  *always* `decision_required` (rule 44's own text: "a config change is definitionally a design
  decision"), `AnswerRun` has no live use case against a `configmaint.propose` pause at all — the
  worksheet's own `Despatcher-tied` section, which the researcher has said is "incomplete" and not
  something they use, matches this: it exists in the code, is real, but isn't the researcher's own
  operating surface.

**The test that decides which path an item takes is rule 44's, stated once more because it is the
crux of everything that follows:** *does resolving this require deciding something new, or only
correcting execution against something already decided?* That test is correctly worded, already in
config, and was not enforced when I raised and closed `#920` in the same breath.

---

## 3. The gap, restated against this ground (not against a new rule)

`#920` was design/build work (a table drop, two migrations, a new patch operation type, new handler
code) that I classified `self_correctable`. Applying rule 44's actual test honestly: was I
"correcting execution against an already-settled, already-approved design"? No — the researcher had
approved the *direction* ("remove `cfg_prose_chapter`," "make `prose_section.status` updatable via
a separate command"), but the *design* — the specific patch operation shape, the parameter names,
the migration structure, how a reset should clear `approved_by`/`approved_at` — was mine, decided
in the course of building it, never itself put to the researcher. That is squarely the "requires
deciding something new" branch, i.e. `decision_required`, by rule 44's own words.

**The gap is therefore not that no rule existed.** It is that nothing requires the person closing a
`self_correctable` item to demonstrate, concretely, that rule 44's test was actually applied — the
`resolution` field only has to say what changed, never what pre-existing approved design it was
executing against. `resolve_self_correctable()` (`iba/app/lib/escalation.py:812`) takes exactly one
piece of content (`resolution`) and no citation of what settled decision the fix conforms to.
Compare `escalate_to_decision()`, three functions below it in the same file, which already requires
`tried` — "what was attempted" — before it will act. `resolve_self_correctable` has no equivalent.

---

## 4. Proposed change — exact wording, before and after

**One new required field on `resolve-self-correctable`, reusing the existing `tried` column** (no
schema migration — `tried` already exists on `escalation`/`escalation_history`, currently used only
by `escalate_to_decision`), broadened to also serve this purpose. No new mechanism, no keyword
pattern-matching (v1's approach, dropped) — the same field the codebase already uses for "justify
yourself before this action completes," extended to the one terminal action that currently skips
it.

### 4.1 `iba/app/lib/escalation.py` — `resolve_self_correctable()`

**Before:**
```python
def resolve_self_correctable(cfg: Cfg, db: Db, escalation_id: int, resolution: str,
                             *, originator: str) -> str:
    """Closes a `self_correctable` escalation. No `approve`/`reject`/`revise`/`hold`/`noted`
    vocabulary and no `AnswerRun` involvement -- `cfg_behaviour_rule
    'decision-points-are-terminal-not-inline'`: a researcher never fixes code, so there is no
    decision for them to make here. Claude fixes it, states what was wrong and what changed
    (`resolution`, required), and this closes the item directly."""
    cur = _current(db, escalation_id)
    if cur["resolution_kind"] != "self_correctable":
        raise ValueError(f"escalation #{escalation_id} is not self_correctable "
                        f"(resolution_kind={cur['resolution_kind']!r}) -- use Update/AnswerRun "
                        f"instead, or escalate_to_decision() if it turned out to need one")
    if not resolution:
        raise ValueError("resolution is required -- state what was wrong and what changed")
    who = _check_assignee(db, originator)
    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"resolution": resolution},
                       envelope={"state": _check_state(db, "completed"), "next_action": None,
                                "next_action_assigned_to": cur["next_action_assigned_to"],
                                "resolution_kind": "self_correctable"},
                       originator=who)
    return f"escalation #{escalation_id} v{merged['version']} resolved (self_correctable) -> completed"
```

**After:**
```python
def resolve_self_correctable(cfg: Cfg, db: Db, escalation_id: int, resolution: str, tried: str,
                             *, originator: str) -> str:
    """Closes a `self_correctable` escalation. No `approve`/`reject`/`revise`/`hold`/`noted`
    vocabulary and no `AnswerRun` involvement -- `cfg_behaviour_rule
    'decision-points-are-terminal-not-inline'`: a researcher never fixes code, so there is no
    decision for them to make here. Claude fixes it, states what was wrong and what changed
    (`resolution`, required), and this closes the item directly.

    `tried` is required here too (escalation #921, 2026-08-27) -- not "what was attempted" in
    escalate_to_decision's sense, but the concrete answer to rule 44's own test: what
    already-settled, already-approved design or prior decision this fix executes against (a
    researcher instruction quoted directly, a prior approved escalation/patch id, an existing
    documented rule). A resolution with no citable prior decision behind it is not
    self-correctable by definition -- it should have been raised decision_required instead."""
    cur = _current(db, escalation_id)
    if cur["resolution_kind"] != "self_correctable":
        raise ValueError(f"escalation #{escalation_id} is not self_correctable "
                        f"(resolution_kind={cur['resolution_kind']!r}) -- use Update/AnswerRun "
                        f"instead, or escalate_to_decision() if it turned out to need one")
    if not resolution:
        raise ValueError("resolution is required -- state what was wrong and what changed")
    if not tried:
        raise ValueError("tried is required -- name the already-approved design or prior "
                        "decision this fix executes against (rule 44's own test); if there "
                        "isn't one, this item is not self_correctable")
    who = _check_assignee(db, originator)
    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"resolution": resolution, "tried": tried},
                       envelope={"state": _check_state(db, "completed"), "next_action": None,
                                "next_action_assigned_to": cur["next_action_assigned_to"],
                                "resolution_kind": "self_correctable"},
                       originator=who)
    return f"escalation #{escalation_id} v{merged['version']} resolved (self_correctable) -> completed"
```

Call site in `_dispatch()` (the `resolve-self-correctable` CLI branch) gains one positional/kwarg
for `tried`, mirroring how `escalate_to_decision`'s branch already reads it.

### 4.2 `cfg_escalation_requirement` — one new row

**Before:** no row for `action='resolve-self-correctable'`.

**After (new row):**

| action | field | condition_key | message | check_kind |
|---|---|---|---|---|
| `resolve-self-correctable` | `tried` | `always` | `tried is required at resolve-self-correctable -- name the already-approved design or prior decision this fix executes against (cfg_behaviour_rule 'decision-points-are-terminal-not-inline'); if there is none, raise decision_required instead` | `field_required` |

### 4.3 `iba/app/ps/Escalation.ps1` — `ResolveSelfCorrectable` branch

**Before:**
```powershell
'ResolveSelfCorrectable' {
    if (-not $Id -or -not $Resolution) {
        Write-Host "ResolveSelfCorrectable needs -Id and -Resolution (what was wrong, what changed)." -ForegroundColor Yellow
        exit 1
    }
    if (-not $AnsweredBy) {
        Write-Host "ResolveSelfCorrectable needs -AnsweredBy Claude|Researcher -- no default." -ForegroundColor Yellow
        exit 1
    }
    python -m iba.app.lib.escalation resolve-self-correctable $Id --originator=$AnsweredBy --resolution=$Resolution
}
```

**After:**
```powershell
'ResolveSelfCorrectable' {
    if (-not $Id -or -not $Resolution -or -not $Tried) {
        Write-Host "ResolveSelfCorrectable needs -Id, -Resolution (what was wrong, what changed) and -Tried (the already-approved design or prior decision this fix executes against)." -ForegroundColor Yellow
        exit 1
    }
    if (-not $AnsweredBy) {
        Write-Host "ResolveSelfCorrectable needs -AnsweredBy Claude|Researcher -- no default." -ForegroundColor Yellow
        exit 1
    }
    python -m iba.app.lib.escalation resolve-self-correctable $Id --originator=$AnsweredBy --resolution=$Resolution --tried=$Tried
}
```

### 4.4 What this does and does not do

**Does:** makes rule 44's existing test a mandatory, written, checkable step at the moment a
`self_correctable` item closes — the exact gap `#920` fell through. Adds nothing new to `type`,
`resolution_kind`, state transitions, or any dispatcher-tied path — all of section 1 stays exactly
as it is. Costs one field on one action, reusing an existing column.

**Does not:** verify that the cited prior decision is *real* or *actually applicable* — `tried`
remains free text, exactly like it already is on `escalate_to_decision` and `revise`. A dishonest
or careless citation still gets through. This is named plainly rather than oversold: it converts a
silent, unexamined self-classification into an explicit, written, falsifiable claim — a real
improvement, not a complete guarantee against the same mistake recurring.

---

## 5. Test plan (per `cfg_behaviour_rule` id 46 — run after approval, results go in the resolution)

- Resolve a genuine `self_correctable` item with `-Tried` given → succeeds, `tried` recorded.
- Same, with `-Tried` omitted → refused, with the message above, before any DB write.
- `escalate_to_decision`'s own `-Tried` requirement (unrelated code path) unaffected — re-tested to
  confirm no cross-talk.
- `configmaint.validate` re-run clean after the migration adding the `cfg_escalation_requirement`
  row.
- A synthetic replay of `#920`'s own resolution text through the new check, confirming it would
  have been refused for lacking a citable prior decision (`tried` would have had to name something
  that doesn't exist, since no such decision was ever put to the researcher).
