# Escalation design plan (v1, 2026-08-20)

Prepared against `Workflow/Chat_responses/Escalation design plan prompt.txt`, following its section
headings exactly. This is **not a memory-recall document** — every claim below is sourced from a
live read of the file/DB it comes from, listed in §Resources. Where the live system contradicts an
earlier document (including the rebuild done earlier today), both are stated and the contradiction
is flagged as its own finding, not silently resolved in the rebuild's favour.

**Verdict up front, since it governs how to read everything below:** the 2026-08-20 rebuild
(`escalation-rebuild-design-v1-20260820.md`, shipped as `BUILD.md` §161) fixed the mechanism it set
out to fix — the delta/cumulative split, the config-driven transition and requirement engines, the
no-default-originator rule, two-stage approval — and all of that is verified correct below. But
working back through the resources it was itself supposed to be answering to (principally escalation
`#753` and its own supporting note) surfaces **two explicit researcher instructions the rebuild did
not carry out, and did not flag back as not carried out** (§Governance), plus **a live id-collision
the rebuild's own later action caused** (§tables and columns) and **three stale/orphan config items**
it left behind on the very tables it rebuilt. None of these are hidden — they are traceable in the
rebuild's own documents — but none of them were surfaced to the researcher as open before the rebuild
was reported "tested... ready for real use." That gap — reporting done without reconciling against
the standing instruction that gated it — is the design defect this document exists to correct.

---

## Resources

Every source document actually read for this plan, in the order gathered, not the order most
convenient to cite:

**The prompt driving this document:**
- `Workflow/Chat_responses/Escalation design plan prompt.txt` — the template these headings follow.

**The standing instruction this whole thread answers to:**
- Escalation `#753` (live table wiped 2026-08-20; full 5-version text recovered from
  `iba/app/db/archive/escalation-export-20260820.json`) — *"This task will stay open until all the
  aspects covered in this note have been fully covered and signed off."* Last live state before the
  wipe: `re-assigned`, `next_action=review`, `next_action_assigned_to=Researcher` — **not**
  `completed`, **not** signed off.
- `Workflow/Chat_responses/escallation utility refinement 2026-08-20` — the researcher's own note
  #753 was raised from. Contains the four explicit directives cross-checked in §Governance below
  ("finding 1... don't guess, just fix it", "proceed with implementing this functionality... in all
  the routines", "finding 3 - fix it", "finding 4 - clear it, don't just park and report it").
- `Workflow/Chat_responses/archive/comments - escalation-system-mechanics` — the researcher's
  original, column-by-column, state-by-state review that started the whole redesign lineage
  (2026-08-18), plus a second block of comments on redesign plan v1.

**The full design lineage (read in full, not summarised from memory):**
- `iba/docs/escalation-system-mechanics-20260818.md` — full mechanics of the pre-redesign system,
  live-code-sourced.
- `iba/docs/archive/escalation-redesign-plan-v1-20260818.md` — first plan draft, five open questions.
- `iba/docs/escalation-redesign-plan-v3-20260819.md` — the plan actually built from (v2 is
  superseded in-place by v3's own §0 changelog; v2's file exists at
  `iba/docs/archive/escalation-redesign-plan-v2-20260819.md`, not separately re-read in full here
  since v3 §0/§8 already states everything carried forward unchanged from it).
- `iba/docs/escalation-config-review-v1-20260820.md` — first config-compliance pass, 4 findings.
- `iba/docs/escalation-config-review-v2-20260820.md` — the redo, after the researcher's "finding 1
  ... unclear... don't guess, just fix it" pushback — inventory A–F of every validate/complete rule
  against whether config actually drives it.
- `iba/docs/escalation-rebuild-design-v1-20260820.md` — the design actually built to.
- `iba/app/BUILD.md` §113–161 (32 sections spanning 2026-07-23 → 2026-08-20; headers enumerated,
  §153/154/161 read in full) — the build record.
- `iba/app/USER-GUIDE.md` §4.1–4.7 — current user-facing description, read in full and cross-checked
  against live code/config (found accurate).
- `iba/app/GOVERNANCE.md` — searched for every escalation-mechanism term (`two-stage`,
  `ready_for_approval`, `cumulative`, `state-derivation`, `escalation_history`) — zero matches (§Governance).
- `Workflow/Chat_responses/iba table review` (2026-08-16) — the original instruction that started
  the escalation reset, including the verbatim `governance.escalation.scope`/
  `governance.utility.config` wording and the explicit *"work through Governance.md and ensure that
  all references in Governance are properly updated to adhere to the config... ensure that the User
  Guide is updated"* instruction.
- `Workflow/Chat_responses/Additional configs` — smaller follow-on items, cross-checked against
  `cfg_escalation` content.
- `Workflow/Chat_responses/response-tablereviewresponse v1` (archive copy; the root-folder copy is
  empty) — researcher's response to the 2026-08-16 table review, including the "configmaint must not
  become a bureaucratic compliance exercise" steer that bears on §control items below.
- `iba/docs/escalation-compliance-review-v1-20260820.md` — my own prior-turn review (re-verified
  here, not re-asserted; both its findings carry forward into this document's §Governance).

**Live system, queried directly this session (not recalled):** `cfg_table`, `cfg_column`,
`cfg_escalation`, `cfg_escalation_transition`, `cfg_escalation_requirement`, `cfg_status_flow`,
`cfg_write_grant`, `cfg_enum`, `cfg_setting`, `cfg_utility`, `cfg_unique` (all rows scoped to
`escalation`/`escalation_history`/the two new rule tables); `sqlite_sequence`; `escalations_old`;
`escalation`; a live `configmaint.validate` run; `iba/app/lib/escalation.py` (full, 692 lines);
`iba/app/ps/Escalation.ps1` (full); a `grep` sweep of every `.py`/`.ps1` file in `iba/app` that
touches the `escalation`/`escalation_history` tables.

---

## Purpose

**What the researcher's own words define it as** (plan v1 §1, written to be carried into config
verbatim): *"the only sanctioned researcher interaction. All runtime errors are reported in it; both
Claude and Researcher record emerging issues, tasks, followups as feedback or to get feedback. It is
the authoritative record of open items in the project. It will pause a running process, and allow it
to resume at `resume_point` when answered."*

**How it meets that purpose, mechanically:**
- *Authoritative record of open items* — one `escalation` row per item (current state) backed by an
  append-only `escalation_history` (true per-version delta since today's rebuild — see
  §tables and columns). `governance.escalation.scope` (2026-08-16 setting, still live, unchanged):
  *"all open items, discovery of anomalies, clarifications and other forms of escalation must be
  recorded in escalation using escalation rules."*
- *Pauses a running process* — the **dispatcher-tied** shape: `run.py` writes/reads `escalation` at
  real pipeline pause points (crash, quality-check finding, `configmaint.propose`), correlated by
  `run_id`, answered via `-Action AnswerRun`, and `cfg_escalation.module_blocking` (rule 3, confirmed
  live in `run.py`) refuses to run a step while an unresolved escalation stands against it.
- *Both parties record issues/feedback* — the **manual** shape: raised via `-Action Raise`, updated
  via `-Action Update`, two-stage `ready_for_approval → approved` handshake requiring different
  parties (§control items).

**Where the live `cfg_utility.purpose` and `cfg_table.use` text do NOT yet say this** — see
§Governance/§configs: the corrected, broader purpose statement above was written into plan v1 as
"to be written into config verbatim," but `cfg_utility.purpose` for module `escalation` still reads
the original, narrower 2026-08-16 one-liner (*"The only sanctioned researcher interaction"* — true,
but the rest of the purpose statement was never carried into that row), and `cfg_table.use` for
`escalation`/`escalation_history` describes the design retired earlier today (§tables and columns).

---

## Type of entries

`escalation.type` (`cfg_enum escalation_type`, 5 active values) — an orthogonal classification axis,
set once at Raise, never branched on by code (confirmed: `type` is read/written but never appears in
an `if`/`_evaluate_transition` condition anywhere in `escalation.py`):

| type | why it exists | how it's raised |
|---|---|---|
| `task` | Default. General work item — a to-do, not an error and not a decision request per se. | `-Action Raise` (default `-Type task`) |
| `run_error` | A code-generated crash or exception, caught by a dispatcher-tied pause OR the standalone-CLI crash-wrapper (`escalation.py`'s own `main()` — confirmed live-tested this session, escalations #2/#3). | `run.py`'s crash path; `escalation.py main()`'s own `except Exception` wrapper |
| `issue` | A defect/gap found during investigation, not a crash. Used for this very document's own findings (e.g. escalation #4, raised this session). | `-Action Raise -Type issue` |
| `notice` | Information-only, no decision needed — pairs naturally with `next_action=noted → state=closed`. | `-Action Raise -Type notice` |
| `config` | A `configmaint.propose` pause specifically. | `handlers/configmaint.py`'s dispatcher-tied raise |

**Each type does NOT go through a different workflow** — this is the one place the design deliberately
keeps a single mechanism rather than branching per type (matches
`feedback_simple_steps_not_engineered_designs`). What differs by *item* is not `type` but **shape**
(dispatcher-tied vs manual, §control items) — a `run_error` can be either shape (a dispatcher crash,
or a manually-raised bug report about a past crash), so `type` and `shape` are independent axes, not
a hierarchy. This is implicit in the code (nothing enforces it) rather than stated anywhere in config
or docs — worth a one-line note in `cfg_column.escalation.type.use` or `USER-GUIDE.md` §4.2 since a
reader could reasonably assume `type=run_error` implies dispatcher-tied, and it doesn't.

**Life of each type, illustrated by what actually happens (not exhaustive, per the prompt's own
"illustrative" framing):**
- A **task**: raised (`state=raised`, `next_action=review`) → someone works it → `-Action Update
  -NextAction ready_for_approval -Resolution "..."` → assignee changes, `state=re-assigned` → the
  other party `-NextAction approved` → `state=completed`. If instead it needs input before work can
  continue, `-NextAction revise` at any point → `state=in-progress`, assignee flips to whoever must
  answer; when they respond, another `revise` or a `ready_for_approval` continues the cycle. If it
  turns out wrong/duplicate, `-NextAction reject -State withdraw`; if it's superseded by a better-
  scoped item, `-NextAction reject -State supersede` (§4.7 `USER-GUIDE.md`, worked in
  §transaction types below).
- A **run_error**: raised automatically (dispatcher pause, or the CLI crash-wrapper) → `-Action
  AnswerRun -Decision Approve|Reject|Revise|Hold|Noted` resolves the pause and the paused code either
  resumes or is told to stop, depending on the handler's own `cfg_on_fail` routing (outside
  `escalation.py`'s own scope — it only records the decision, `run.py` acts on it).
- **When something needs clarification mid-item**: not a separate linked item under the current
  design — it's the SAME item, `-NextAction revise` with `-AssignedTo` the party who must clarify,
  `-Comment`/`-Context` carrying the question. A genuinely separate but related item (e.g. a new bug
  found while working this one) is a **new** `-Action Raise` with `-RelatedActivity` naming this
  item's id — plain free text, not a structural link (§tables and columns, `related_activity`).

---

## transaction types

Two, by the researcher's own stated principle (redesign-plan-v1 comments, carried unchanged through
every later round): *"In principle there are only two transaction types... the resulting state will
be determined by the values in the fields."* Confirmed still true in the live code — `escalation.py`
exposes exactly `raise_new()`/`raise_()` (create) and `update()`/`answer_for_run()` (the two shapes'
own update function) — no third write path exists.

### Raise (`-Action Raise`, manual shape only — the dispatcher shape's equivalent is `raise_()`, called only from `run.py`/crash-wrappers, not user-invoked)

| Aspect | Detail |
|---|---|
| Preconditions | None — brand new item |
| Required | `short_description` (≤60 chars, one line, no `--`; `_title_shape_error()`, escalation #759), `comment` (`cfg_escalation_requirement`, action=raise), `originator`/`-AnsweredBy` (no default anywhere, §control items) |
| Optional | `context`, `related_activity`, `-Type` (default `task`), `-AssignedTo` (default `Claude`), `-Source` (default `researcher`) |
| Effect | New `escalation` row, `version=1`; matching `escalation_history` row (v1's row IS the full row — no delta/envelope split needed at creation, `_create()`) |
| Automation | `state='raised'` (from `cfg_status_flow`, `set_by LIKE '%at Raise%'`), `next_action='review'` |

### Update (`-Action Update`, manual shape) / AnswerRun (`-Action AnswerRun`, dispatcher shape)

| Aspect | Manual (`update()`) | Dispatcher (`answer_for_run()`) |
|---|---|---|
| Preconditions | Item must be `run_id` starting `MANUAL-`; current `state` in `_OPEN_STATES` | A `raised` row exists for this `run_id` |
| Required | `originator`/`-AnsweredBy` (no default) | `answered_by`/`-AnsweredBy` (no default) |
| Vocabulary validated against | `cfg_enum('escalation_next_action_manual')` | `cfg_enum` is declared (`escalation_next_action_dispatcher`) but **not actually consulted here** — `answer_for_run()`/`Escalation.ps1`'s `-Decision` `ValidateSet` both hardcode the 5-value tuple independently (see §configs cross-check — this is unchanged from the gap `escalation-config-review-v1` Finding 2 named, and the enum SPLIT fixed the vocabulary-leak half of that finding but not the "code doesn't read the enum" half) |
| Conditional requirements | `resolution`@`next_action=approved`; `state`@`next_action=reject`; `tried`@`next_action=revise` when `originator=Claude` (`cfg_escalation_requirement`) | None beyond the enum membership |
| Two-stage check | `next_action=approved` refused if `originator` = whoever last set `ready_for_approval` on this item | N/A — dispatcher shape has no two-stage concept |
| Effect | New `escalation_history` row (delta: only fields supplied this call are non-NULL, envelope always populated); `escalation` gets append-cols (`comment`/`context`) merged onto the running text, replace-cols (`resolution`/`related_activity`/`tried`/`short_description`) overwritten if supplied, `version` incremented | Same delta/current-state split, same `_snapshot()` function — both shapes share one write mechanism |
| State derivation | `cfg_escalation_transition WHERE shape='manual'`, priority order | `cfg_escalation_transition WHERE shape='dispatcher'`, priority order |

**Worked illustration (traced against the live code, not the plan doc's own worked example, which
predates the config-driven engine):** raising a `task`, then `revise` (assignee flips, `tried`
required if Claude is the reviser), then `ready_for_approval` (assignee flips again, `resolution`
now on the row), then `approved` by the *other* party (`resolution` already present → rule 1 fires →
`completed`) — four `escalation_history` rows, matching the researcher's own expectation in
redesign-plan-v2 §7 (*"I am expecting to see two history rows for an approval"* — confirmed still
true: rows 3–4 of this sequence are exactly that pair).

---

## tables and columns

### `escalation` — 18 columns, current state (unchanged in shape by the rebuild — see full column
list already captured verbatim in `iba/docs/escalation-compliance-review-v1-20260820.md` §Finding 1;
not repeated column-by-column here, only what changed/is newly wrong):

**Confirmed correct:** every column's `cfg_column.use` text matches live code behaviour, cross-
checked column-by-column against `escalation.py`'s `_COLS`/`_ENVELOPE_COLS`/`_APPEND_COLS`/
`_REPLACE_COLS`/`_IMMUTABLE_COLS` groupings — no drift found in the 18 individual column rows.

**Newly found this pass — the `id` column's own `cfg_column.use` text is now false, and the failure
is LIVE, not cosmetic:**

> `cfg_column.escalation.id.use`: *"serial PK, 4-digit display; **continues from escalations_old's
> max (735)** so ids stay unambiguous across the cutover"*

Live query: `sqlite_sequence` for table `escalation` = **4**, not 736+. `BUILD.md` §161's own test
section explains why: *"then that test item removed, id sequences reset again, live tables left
empty and ready for real use."* — a second reset, after the migration that implemented the
735-continuation promise, that was never reconciled back into the column's own description.

**This is not cosmetic — it is a live collision, confirmed by direct query, not inferred:**

```
escalations_old:  id=1 "Register the new word 'hypocrisy'?"        (completed, archived)
escalations_old:  id=3 "Register the new word 'malice'?"           (completed, archived)
escalations_old:  id=4 "Register the new word 'abomination'?"      (completed, archived)
escalation (live): id=1 (the earlier configmaint.validate pause this session)
escalation (live): id=4 "escalation cfg_table.use text still describes retired design" (this session's finding)
```

**"Escalation #4" is now genuinely ambiguous** — the exact failure mode the `735`-continuation
design was built to prevent, and the exact failure mode `escalation-redesign-plan-v1` §2's "open
question" answer chose to prevent (*"keep `escalation.id` as today's plain integer serial PK
(unchanged)... every existing cross-reference in the app and in prior escalations that cites `#715`
etc. keeps working"*). Every historical reference anywhere in `BUILD.md`/`GOVERNANCE.md`/prior
design docs to a low-numbered escalation (`#1`–`#96`, the range `escalations_old` actually populates
low ids in) is now collision-prone against any newly-raised live item in that same range.

**Fix required:** re-seed `escalation`'s `sqlite_sequence` to 735 (matching the original, correct
design intent, still stated as true in the live column text) before any further real use — this
table currently has only 4 live rows (2 from this session's own testing, already closable), so the
reseed is cheap and safe right now; it will not be once real backlog accumulates on top of the
colliding range.

### `escalation_history` — 19 columns, append-only delta (rebuilt today)

Column-level `cfg_column.use` text is correct (confirmed against code — see
`escalation-compliance-review-v1`). **Table-level `cfg_table.use` is not** — carried forward
unchanged from the finding already raised as escalation `#4`:

> *"one FULL SNAPSHOT row per update to an escalation item, every column's value at that version...
> `escalation` always mirrors the latest row here by construction"* — false under the live delta
> design; not re-litigated in full here, see `escalation-compliance-review-v1-20260820.md` Finding 1
> and escalation `#4`.

### `cfg_escalation_transition` / `cfg_escalation_requirement` — new this rebuild

Both fully registered (`cfg_table`/`cfg_column`/`cfg_unique`), content verified correct against
`escalation.py`'s actual branching (full dumps in §configs below). `cfg_unique` confirms both
tables' dedup keys are declared (`(shape, priority)`, `(action, field)`) — matches their `PRIMARY
KEY` in the design doc's DDL.

### `escalations_old` — the frozen pre-2026-08-19 table, 735 rows, archival only

Not itself part of the live mechanism, but its max id is the number every "continues from" claim in
the live schema's own documentation depends on being true — see the `id` finding above. Worth a
`cfg_table.use` row of its own stating plainly it is frozen/read-only archival (checked: it has one,
not independently re-verified in this pass, lower priority than the live defects above).

---

## Governance

Every `governance.*` `cfg_setting` printed at session start (`Start-Iba.ps1`'s own output, the
authoritative live list — not recalled from memory), checked for applicability to escalation
specifically:

| governance rule | applies? | compliant? |
|---|---|---|
| `governance.escalation.scope` | **Directly** — this is escalation's own scope rule | ✅ — every anomaly this session, including this document's own findings, was raised as a real `escalation` row (§4/#4), not just written to a doc |
| `governance.utility.config` | **Directly** — escalation must have its own cfg table(s) | ✅ — `cfg_escalation` + the two new rule tables |
| `governance.module.config` | **Directly** | ✅ — same three tables |
| `governance.rules_must_be_config_driven` | **Directly** — the whole point of the 2026-08-20 rebuild | **Partial** — `cfg_escalation_transition`/`cfg_escalation_requirement` genuinely closed the two biggest gaps (state-derivation, field-requirements) `escalation-config-review-v2` found. NOT closed: the dispatcher-shape enum still isn't actually read at runtime (table above); `escalation_shape` enum exists but is never looked up by code either (confirmed by grep — zero `cfg.enum("escalation_shape")` call sites; it escapes `configmaint.validate`'s orphan-enum check only because a `cfg_column.expectation='enum.escalation_shape'` string satisfies that check's structural-declaration exemption, not because the value list is actually enforced anywhere — see §configs) |
| `governance.new_utility_registration_timing` | **Directly** — the two new rule tables, built same session as the code that reads them | ✅ — confirmed registered same-day |
| `governance.table_columns` / `governance.tables` | **Directly** | **Partial** — see `escalation-compliance-review-v1` Finding 1, carried forward: `escalation`/`escalation_history`'s table-level `use` text is stale; every individual column is correct |
| `governance.governance_md_on_rule_change` | **Directly — and explicitly instructed twice** (see below) | ❌ — not done |
| `governance.build_md_on_code_change` | **Directly** | ✅ — `BUILD.md` §161, detailed and honest about what was deferred |
| `governance.reports_must_persist` | **Directly** — both escalation reports | ✅ (persists to a `cfg_setting`-defined path) but **not** registered in `cfg_report`/`cfg_report_section` like every other report in the app — see below, this is the explicitly-instructed "finding 3 - fix it" that wasn't |
| `governance.redundancy_archiving` | Applies to the one-off review docs this thread produced | Not yet actioned — `escalation-config-review-v1`, `-v2`, `escalation-system-mechanics-20260818` are all superseded-in-substance by the rebuild design doc; none archived yet. Flagging, not fixing here — archiving is a filing action, not a design decision |
| `governance.past_precedent_investigation_signals_missing_config` | Applies to how this very investigation was conducted | Self-check: this document required reading `BUILD.md`/session history to reconstruct what #753 actually said, because the live escalation table no longer holds it (wiped). That is itself an instance of this rule — the wipe destroyed the config's own record of a standing instruction, forcing exactly the kind of precedent-archaeology this governance rule says should never be necessary. Escalated below. |
| `governance.escalation.scope`'s sibling requirement (from the 2026-08-16 founding note, not a `governance.*` setting but an explicit direct instruction) | *"work through Governance.md and ensure that all references in Governance are properly updated to adhere to the config... ensure that the User Guide is updated"* | **Half done** — `USER-GUIDE.md` §4 is accurate and current (verified line-by-line against live code this pass). `GOVERNANCE.md` was never touched — zero mentions anywhere of `cfg_escalation_transition`, `cfg_escalation_requirement`, the delta/cumulative split, or two-stage approval, across the entire redesign lineage (not just today's rebuild) |

### Two explicit researcher directives not carried out, and not flagged as not carried out

Cross-referencing `Workflow/Chat_responses/escallation utility refinement 2026-08-20`'s four
point-by-point instructions against what actually shipped:

| # | Researcher's instruction (verbatim) | What shipped |
|---|---|---|
| 1 | *"finding 1... don't guess, just fix it, governance is clear"* (cfg_status_flow empty) | ✅ Done — 8 rows populated |
| 2 | *"Proceed with implementing this functionality for all error trapping and escalation type notifications in all the routines"* (every module/utility's crashes should auto-escalate, not just this one) | ❌ **Not done.** `escalation-rebuild-design-v1` §10 explicitly defers this: *"Auto-escalating every standalone-CLI module's crashes, not just this one... out of scope for an escalation-module rebuild specifically."* The scope-narrowing is stated in the design doc, but was never put back to the researcher as "I'm not doing what you asked here, confirm the deferral" — it reads as a design decision, not a deviation flagged for approval |
| 3 | *"finding 3 - fix it"* (the two escalation reports bypass `reportkit`/`cfg_report`, the standard every other of the app's 22 reports goes through) | ❌ **Not done.** Same document, same §10: *"Explicitly deferred... full `reportkit`/`cfg_report` registration for the two reports... Next piece of work once this lands, not dropped."* Deferred a second time (it was already deferred once, in `escalation-config-review-v1` §5, pending the rebuild) |
| 4 | *"finding 4 - clear it, don't just park and report it"* (orphan `cfg_write_grant(escalation→word_registry)`) | ✅ Done — retired, confirmed `inactive=1` live |

**Two of four direct, explicit instructions were deferred rather than carried out**, and the
deferral was framed in the design doc as a reasonable scoping call rather than surfaced as "the
researcher told me to do X, I am choosing not to, please confirm." Per
`feedback_fix_standard_violations_dont_ask` ("deviation from an established, documented standard =
a bug, fix it, don't ask — only ask on genuine judgement calls") — these are not genuine judgement
calls once the researcher has already given a direct instruction; deferring them without a flag is
itself the violation, independent of whether the deferral reasoning is individually sound.

### `#753` itself — the standing item this whole thread reports to

`#753`'s own text: *"This task will stay open until all the aspects covered in this note have been
fully covered and signed off."* It was last `re-assigned`/`review`/`Researcher` — never
`completed`. The export+wipe (`reset_escalation_tables_20260820.py`) removed it from the live table
along with everything else, under the researcher's general *"delete all the records"* instruction
given in the same conversational turn that ordered the rebuild — so the wipe itself was authorised.
**What was not done: re-raising a fresh #753-equivalent tracking item, live, in the rebuilt system,
carrying forward the two still-open buckets (directives 2 and 3 above) that #753 was tracking.** The
standing-open item's function — "don't let this get called done while things are still open" — was
lost at exactly the moment it mattered most, because the tracking mechanism and the thing it was
tracking were the same table.

---

## control items

`type` × `next_action` × `state` × `next_action_assigned_to` × `originator` — the five columns whose
*combination*, not individual value, determines what an item means and what may legally happen to it
next. Table form, since the prompt asks for "all the combinations":

| Combination | Meaning | Enforced by |
|---|---|---|
| `state=raised`, `next_action=review` | Freshly raised, nobody has acted | Default at Raise |
| `state=in-progress`, `next_action=revise`, `assigned_to=X` | X owes a response | `cfg_escalation_transition` priority 3 (manual) |
| `state=re-assigned`, `next_action=ready_for_approval`, `assigned_to=<reviewer>`, `resolution` present | Work claimed done, awaiting confirmation from a **different** party than whoever set this | `cfg_escalation_transition` priority 5 + the two-stage same-party check in `update()` |
| `state=completed`, `next_action=approved` | Confirmed done by a different party than requested it | `cfg_escalation_transition` priority 1 (`has_resolution`) |
| `state=withdraw` or `state=supersede`, `next_action=reject` | Party's explicit terminal choice, `comment` mandatory | `cfg_escalation_transition` priority 2, `__explicit__` — validated against exactly these two values in code |
| `state=closed`, `next_action=noted` | Acknowledged, no action needed | `cfg_escalation_transition` priority 4 |
| `state=on-hold` | Deliberately paused (either party, or dispatcher `hold`) | Directly settable (manual, via `-State`) or `cfg_escalation_transition` dispatcher priority 1 |
| `originator=Claude`, `next_action=approved` | **Illegal** if the same `originator` most recently set `ready_for_approval` on this item | `update()`'s `_last_next_action_originator` check — refuses with a clear message, verified live-tested (BUILD.md §161's test list) |
| `type` (any value) | Never itself gates a transition | Confirmed — `type` appears in no `cfg_escalation_transition`/`cfg_escalation_requirement` row and no code condition |

**What the researcher's own "not a bureaucratic compliance exercise" steer (`response-
tablereviewresponse v1`) means for this table:** the two-stage approval is deliberately *not*
required on every item — plan v3 §"approval authority" is explicit that Claude may self-approve
straightforward fixes; the separation-of-duties check only bites when a `ready_for_approval` row
already names a specific requester, at which point the *same* person confirming their own work is
what's blocked, not approval-by-Claude generally. This matches the researcher's stated intent
directly and is implemented correctly (verified in code, not just in the design doc).

---

## automation

| Column | Automated how |
|---|---|
| `id` | SQLite autoincrement — **currently mis-seeded**, see §tables and columns |
| `version` | `_snapshot()`/`_create()`: `cur['version'] + 1`, or `1` at creation |
| `state` | `_evaluate_transition()` reading `cfg_escalation_transition`, resolved to a concrete value via `_status_for()`/`cfg_status_flow` |
| `next_action` | Caller-supplied (validated against the shape-appropriate enum for manual; hardcoded tuple for dispatcher, see §configs) |
| `next_action_assigned_to` | Caller-supplied; drives `assignee_changed` which feeds priority-5 (manual) transition |
| `originator` | **Never** automated/defaulted — this is itself the automation fix: a REQUIRED explicit argument at every call site, Python `TypeError` on omission, `ValueError` on explicit `None` (`_check_assignee`) |
| `answered_at` | `_now()`, UTC, every write |
| `raised_at` | `_now()`, set once |
| `comment`/`context` | Cumulative in `escalation` (`_append()`), raw delta in `escalation_history` |
| `resolution`/`tried`/`related_activity`/`short_description` | Replace-on-supply in `escalation`, raw delta in `escalation_history` |
| Reports | `write_list_report()`/`write_history_report()` — automated regeneration on every `-Action List`/`History` call, `reportkit.archive_before_write()` archives the prior version automatically first |
| CLI crash | `main()`'s `except Exception` wrapper — automatically raises a `run_error` escalation for ANY uncaught exception in `escalation.py`'s own CLI (live-tested this session, twice, both correctly auto-recorded and then closed) |

**Gap, cross-referenced from §Governance directive 2:** this crash-automation exists **only** for
`escalation.py`'s own CLI. No equivalent wrapper exists for any other standalone module's CLI in the
app — the researcher's *"proceed with implementing this... in all the routines"* instruction, not
carried out.

---

## configs

Full inventory, cross-checked per the prompt's own instruction — *"if there are 5 items in Enum, you
would expect the same list to be applied when [the] column is described, and the rules on selecting
it is described, and the automation is handled, and the validation is done."*

### `escalation_state` (9 active + 3 inactive)

Active: `raised, in-progress, on-hold, re-assigned, closed, withdraw, supersede, completed` (8 —
count matches `cfg_status_flow`'s 8 rows exactly, one-to-one, confirmed). **Wait — that's 8, and the
enum lists 9 active values including a stray**: live dump shows `escalation_state` has active values
`raised, on-hold, closed, withdraw, completed, in-progress, supersede, re-assigned` = 8, not 9 — the
"9" in `escalation-config-review-v1`'s inventory table (`escalation_state(9)`) was itself counting
active+inactive together at the time it was written (pre-rebuild); recount confirms 8 active today,
matching `cfg_status_flow` exactly. **No cross-check gap here** — correcting my own arithmetic while
verifying, not a system defect.

Inactive, correctly retired (superseded, not deleted, `governance.tables`-consistent): `answered`,
`paused`, `retracted` — each superseded by a named active value, self-documented as such in
`escalation-system-mechanics-20260818.md` §3.

### `escalation_next_action` (the RETIRED merged enum, 8 values, ALL now inactive)

Correctly fully retired — confirmed zero active rows, replaced by the two split enums below. **Not
deleted, only deactivated** — consistent with `governance.tables`'s "deactivated, not deleted"
pattern used everywhere else in the app (392 rows project-wide, per `CONFIG-REPORT`). No action
needed; flagged only because the prompt asks to check for "redundant configs" — this ISN'T redundant,
it's the historical record of what used to validate against, correctly preserved inactive.

### `escalation_next_action_dispatcher` (5) / `escalation_next_action_manual` (6) — the split

| | dispatcher (5) | manual (6) |
|---|---|---|
| Enum values | approve, reject, revise, hold, noted | ready_for_approval, approved, reject, revise, noted, review |
| Column description says | `escalation.next_action`'s `cfg_column.use` names both vocabularies correctly | same |
| Rule (`cfg_escalation_transition`) coverage | 3 rows (hold, noted, catch-all-default) — **does not enumerate `approve`/`reject`/`revise` individually**, they all fall into the priority-3 catch-all | 6 rows, one per real branch |
| **Actually validated by code at write time?** | **No** — `answer_for_run()`'s `_check_next_action_dispatcher()` does call `db.cfg.enum("escalation_next_action_dispatcher")` (confirmed reading the code again this pass — CORRECTING `escalation-config-review-v1`'s original Finding 2, which was written against the PRE-split single merged enum and is no longer accurate as stated) | `update()`'s `_check_next_action_manual()` calls `cfg.enum("escalation_next_action_manual")` |
| `Escalation.ps1`'s own `ValidateSet` | `-Decision`: `Approve, Reject, Revise, Hold, Noted` — 5, matches | `-NextAction`: 6, matches |

**Correction to carry forward:** the split enums ARE both consulted at runtime — the "code doesn't
consult the config" half of the old Finding 2 was fixed by the rebuild (both `_check_next_action_*`
helpers do call `cfg.enum(...)`), even though `escalation-rebuild-design-v1`'s own §9 only claimed
the vocabulary-leak half was fixed. Stated plainly since finding something MORE compliant than
documented is as worth recording as the reverse.

### `escalation_shape` (2: manual, dispatcher) — declared, not enforced

Both values exist, both correctly describe the two real shapes. **Zero runtime call sites** —
grepped the full `iba/app` tree: no `cfg.enum("escalation_shape")` anywhere. `_evaluate_transition()`
takes `shape: str` and queries `cfg_escalation_transition WHERE shape=?` directly; a typo'd shape
string produces "no active rows for this shape" (a real error, but not "not a valid escalation_shape
value" — a different, less specific failure mode). This enum escapes `configmaint.validate`'s
orphan-config check only because `cfg_column.expectation='enum.escalation_shape'` (on
`cfg_escalation_transition.shape`) satisfies that check's structural-declaration exemption — the
check treats "some column declares this enum as its expected value-set" as proof of use, without
confirming the value-set is actually read and validated against at runtime anywhere. **This is a
blind spot in `cfgquality.find_orphan_configs()` itself**, not unique to escalation — worth a
separate note (not fixed here, this document is a plan) since it means the "0 orphan configs" figure
`configmaint.validate` reports project-wide is systematically undercounting this exact pattern
wherever else it occurs.

### `escalation_type` (5 active + 4 inactive) / `escalation_assignee` (2 active)

Both clean — active/inactive counts match every downstream consumer (`_check_type`/`_check_assignee`),
no orphans, no redundancy.

### `cfg_escalation` (7 rules) — re-verified this pass, not just cited from `escalation-config-review-v2`

All 7 `enforced_by` claims re-checked against the CURRENT (post-rebuild) code, not the pre-rebuild
code `-v2` checked: still accurate — no new drift introduced by the rebuild. `module_blocking`'s
`enforced_by` text (*"not yet wired — scheduled as a task escalation, see the reset's backlog
pass"*) is confirmed **still stale** (the code has been live since 2026-08-17, per
`escalation-system-mechanics-20260818.md` §11.1) — pre-existing, not new, but its own text now points
at a "reset's backlog pass" that, after today's wipe, may no longer contain the task item it refers
to. Not independently re-traced in this pass (flagged as a "not yet checked" item, honestly, per
`feedback_no_hedge_pointers_in_complete_records` — this is a real open question, not a resolved one).

### `cfg_escalation_transition` (9 rows) / `cfg_escalation_requirement` (5 rows)

Both fully dumped and cross-checked line-by-line against `_evaluate_transition()`/
`_check_requirements()` in §control items/§transaction types above — no discrepancy found between
config content and code behaviour for either table.

---

## validation

| Validation | What it checks | Configured? | On violation |
|---|---|---|---|
| `_check_state`/`_check_type`/`_check_next_action_manual`/`_check_next_action_dispatcher`/`_check_assignee` | Value is an active member of the relevant `cfg_enum` group | ✅ live DB lookup, not hardcoded | `ValueError`, CLI crash-wrapper auto-raises a new `run_error` escalation recording the failure (verified live, twice, this session) |
| `_title_shape_error` | `short_description` ≤60 chars, one line, no `--` | **Partial** — `_TITLE_MAX_CHARS=60` is a Python constant, not a `cfg_setting`; the RULE that a check exists is not itself in config, only the enum/table registrations around it are | Same — `ValueError`/crash-wrapper |
| `_check_requirements` | Field-presence per action | ✅ `cfg_escalation_requirement`, fully config-driven | `ValueError` naming the specific missing field, from the config row's own `message` |
| `_evaluate_transition`'s "no rows for shape" / "no rule matched" | Config-table integrity itself | ✅ — a genuinely empty or non-matching rule set is a hard error, not a silent fallback (deliberate design choice, `escalation-rebuild-design-v1` confirms: "a missing rule row is a hard error, not a silent guess") | `ValueError` |
| Two-stage same-party check | `originator` of `approved` ≠ `originator` of the last `ready_for_approval` | Code-only (`_last_next_action_originator`), no config row states this rule exists | A returned string (not an exception) explaining why, from `update()` |
| `_grant`/`_grant_both` | `cfg_write_grant` permits this writer→table | ✅ | `PermissionError` |
| `Db.write()` column existence check | Insert-only, not update (unchanged limitation, noted in the pre-redesign mechanics doc §6, still true — `Db.update()` used by every `escalation.py` write has no equivalent) | N/A | N/A — **an existing, still-open gap, not introduced by this rebuild, not re-verified independently this pass** |

---

## scripts

Every script that reads or writes `escalation`/`escalation_history`, confirmed by grep this session
(not the pre-rebuild code-footprint list in `escalation-redesign-plan-v1` §8, which is now stale):

| Script | How it uses escalation | Configs it reads for this |
|---|---|---|
| `iba/app/lib/escalation.py` | The mechanism itself — every write goes through here | `cfg_enum`, `cfg_escalation_transition`, `cfg_escalation_requirement`, `cfg_status_flow`, `cfg_write_grant`, `cfg_setting(escalation.*)` |
| `iba/app/ps/Escalation.ps1` | The one PS front door — light client-side validation, shells to `python -m iba.app.lib.escalation` | None directly — mirrors the Python enums as hardcoded `ValidateSet`s (a duplicated, not shared, source of truth — pre-existing pattern, not new) |
| `iba/app/run.py` | Dispatcher-tied raise/answer at real pause points; the `module_blocking` gate query | `cfg_escalation` (module_blocking rule) |
| `iba/app/handlers/candidate.py`, `cluster.py`, `configmaint.py`, `lexicon.py`, `narrative.py`, `passage.py`, `registry.py`, `reports.py` | Each raises its own dispatcher-tied pauses via `lib.escalation` | Each handler's own `cfg_step`/`cfg_on_fail` rows determine WHEN, `lib.escalation` handles the write itself |
| `iba/app/tools/purge_word.py` | Deletes a word's own escalation rows as part of test-data cleanup | None specific to escalation |
| `iba/app/lib/retention.py` | `retention.report` — read-only log-retention/run-health report over `run`/`escalation`/`validation_result` | Own `cfg_report` registration (unlike escalation's own two reports) |
| `iba/app/lib/cfgquality.py` | `find_missing_report_paths` and similar checks reference `escalation` as one of several tables it profiles | `cfg_setting`, `cfg_report` |
| `iba/app/validation.py`, `iba/app/lib/schemareport.py` | Reference `escalation` in schema/validation reporting (not investigated line-by-line this pass — flagged as not yet checked, not asserted clean) | — |

**Every config referenced above IS actually used by the script it's listed against** — cross-checked
in §configs, not merely asserted here.

---

## report

| Report | Purpose | Configs used |
|---|---|---|
| `write_list_report()` (`-Action List`) | Every open item, full history inline, grouped by `related_activity` — the "what needs attention" view | `escalation.control_objectives`/`.control_process` (header line), `escalation.list_report_path` (output path) — **NOT** `cfg_report`/`cfg_report_section` (the standard every other of the app's 22 reports uses) — this is Governance directive 3, still open |
| `write_history_report()` (`-Action History`) | One item's complete version-by-version story, plus everything its `related_activity` links to — the "full thread" view | `escalation.history_report_dir` — same `cfg_report` gap |

**Does the content support the purpose?** Yes, verified by direct read of both functions
(§transaction types/§tables and columns above) — the delta-vs-envelope distinction is rendered
correctly, `_gist()` truncates long fields sensibly, both reports archive their predecessor before
writing. **The gap is registration, not content** — both reports are functionally sound but sit
outside the app's own config-driven reporting standard, and this is the one item the researcher gave
the most direct, least ambiguous instruction on ("finding 3 - fix it") that still isn't done.

---

## Summary — what this plan asks the researcher to decide, before anything further is built

1. **Reseed `escalation`'s id sequence to continue from `escalations_old`'s max (735)** — a live
   collision exists right now, cheap to fix while only 4 rows are live, not cheap once real backlog
   accumulates on top of it.
2. **`escalation`/`escalation_history`'s `cfg_table.use` text** — correct to state the true-delta
   design (already raised as escalation `#4`).
3. **Directive 2** (auto-escalate every routine's crashes, not just `escalation.py`'s own CLI) —
   confirm the deferral, or have it built now rather than re-deferred a second time.
4. **Directive 3** (register both escalation reports through `reportkit`/`cfg_report` like the other
   22) — same question, this is the second deferral of an explicit "fix it."
5. **`GOVERNANCE.md`** — never updated across the entire redesign lineage, not just today. Needs a
   section describing the mechanism (state-derivation engine, field-requirement engine, two-stage
   approval), matching the treatment already given to `configmaint.propose` a few sections away.
6. **A live `#753`-equivalent tracking item**, re-raised, carrying #3/#4 above forward, so "this
   stays open until signed off" survives the next reset the way it didn't survive this one.
7. **`cfg_utility.escalation.purpose`** — update to the full corrected purpose statement (§Purpose)
   rather than the original narrower one-liner.
8. **`escalation_shape`'s orphan-check blind spot** — a `cfgquality.py` fix, out of scope for this
   module alone but worth its own escalation, since the same blind spot likely exists wherever else
   a `cfg_column.expectation` references an enum group without a matching runtime `.enum()` call.

Nothing above is built in this document — per the same standing practice this module's every prior
redesign round followed (design first, approval, then code) — reinforced today, since building past
an ungated point is exactly what triggered the original "not ready for production" ruling.
