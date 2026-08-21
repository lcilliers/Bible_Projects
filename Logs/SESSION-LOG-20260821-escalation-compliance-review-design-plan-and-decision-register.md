# Session log — escalation: compliance review, full design-plan rewrite, and a 24-point decision register (2026-08-20/21)

Direct continuation of the prior session's closing log
(`SESSION-LOG-20260820-escalation-first-production-review-full-reset-and-rebuild.md`) — the module
rebuilt and left "live and ready for real use" there got a formal governance-compliance review here,
which found real defects, which led to a full design-plan rewrite (five rounds, most rejected or
substantially corrected before landing), which converged into a 24-point decision register meant to
be the actual buildable specification. Recorded honestly, including three real mistakes of my own
found along the way (a documentation table wrongly prefixed `cfg_`, a same-party approval check that
implemented the wrong semantics, a CSV-export design that had the report content backwards) and one
genuine defect in already-shipped code (the same-party check) found only by working carefully through
a real scenario with the researcher, not by inspection alone.

## 1. Governance compliance review — asked to confirm, found real defects instead

Researcher asked for confirmation the rebuilt escalation module was governance-compliant and ready
for review, with an explicit standard: one missing piece and the whole design fails. Live-checked
against `cfg_table`, `cfg_column`, `cfg_escalation*`, a real `configmaint.validate` run, and a direct
text search of `GOVERNANCE.md`/`BUILD.md` — not a re-read of the rebuild's own design doc. Found:
`cfg_table.use` for `escalation`/`escalation_history` still described the retired full-snapshot
design (the exact defect class that triggered the original rebuild — a config claim naming a
mechanism that no longer exists); `GOVERNANCE.md` never updated for the mechanism, across the entire
redesign lineage, despite an explicit 2026-08-16 instruction to do so in the same unit of work.
Raised as escalations `#4`/discussed live. `escalation-compliance-review-v1-20260820.md`.

## 2. "Redo the escalation plan" — resource archaeology surfaces two dropped directives

Researcher: redo the design plan using `Workflow/Chat_responses/Escalation design plan prompt.txt`,
working back through every resource, not memory. Recovered `#753`'s full text from the JSON export
(the standing item explicitly meant to *"stay open until all the aspects... have been fully covered
and signed off"* — it wasn't, when the table was wiped). Found two of `#753`'s four explicit
directives (auto-escalate every routine's crashes app-wide; register both reports through
`reportkit`/`cfg_report`) were silently deferred a second time in the rebuild, narrated as reasonable
scoping rather than flagged as deviations. Found a live, active id collision: the id sequence was
reset during testing, so `escalations_old`'s historical low ids (`#1`, `#3`, `#4`...) now collide with
newly-raised live items of the same number. Raised `#5` (id collision) and `#6` (a standing tracker
in `#753`'s place — this escalation carried the rest of this session's whole record).
`escalation-design-plan-v1-20260820.md`.

## 3. Design plan v1 rejected — flat, no perspective

Researcher: the document just answered the template's prompts as Q&A instead of actually thinking
about the domain — every item treated as flat and worked in isolation, `type` treated as inert
metadata. Concrete evidence for this the researcher pointed at directly: `#712`'s cascade of follow-on
items landed under a *different* `related_activity` label than `#712` itself — the parent→child
relationship exists nowhere in the data, only in `BUILD.md` prose. Worked through what `task`
(execution), `issue` (deliberation, often the whole `v1→v2→v3` redesign-plan lineage itself is one
long issue that never lived inside the escalation mechanism), and `notice` (no action needed) actually
are as distinct kinds of things, not one flat shape.

## 4. Design plan v2 — five types, a link table that was wrong twice over

Built all five types with real distinct lifecycles (`task`/`run_error`/`config` share the two-stage
handshake; `issue` gets its own vocabulary; `notice` closes itself). Proposed `cfg_escalation_link`, a
typed many-to-many relationship table — **rejected by the researcher on two counts**: `cfg_` is
reserved for configuration, never data about specific item instances (a real naming-discipline mistake
of my own, not a judgement call); and a typed many-to-many table solved a problem never actually
observed — every real chain found this session is single-parent.

## 5. Design plan v3 — `from_id`, and the existing report-config system I'd missed

Corrected to `escalation.from_id` (one column, mutable on both Raise and Update) + `related_activity`
as the free-text description — replacing the rejected link table with something simpler and matching
what was actually needed. Researcher's own next correction: *"why do you want to add another table —
does the reports not have a config table?"* — `cfg_report`/`cfg_report_section`/`cfg_report_csv_table`
already existed for exactly this, checked live and modelled from real examples
(`configmaint.report`, `retention.report`) rather than invented alongside them. Surfaced a bigger fact
in checking it: every live `cfg_report` row without exception is tied to a `run.py`-dispatched
`cfg_step` — there is no precedent for a report invoked outside the dispatcher, meaning `Escalation.
ps1` itself (which calls Python directly) is one of the ungoverned scripts this same session's
earlier work (escalation `#8`, see below) had already found a wider version of.

## 6. `#8`/`#9` — how far the governance gap actually runs

Asked to characterise it rather than estimate: 8 of 45 PS scripts in `iba/app/ps` bypass `run.py`'s
dispatcher entirely, leaving zero execution record — not a partial one, none — for whatever they do.
`Debate-Run.ps1` was found to be worse than a clean bypass: it dispatches its main step correctly,
then tacks on an ungoverned side-operation afterward. Raised `#8`. Researcher's follow-up — *"we are a
long way off having IBA being governance compliant... unless I poke, it does not surface"* — led to
`#9`, naming the actual mechanism (every finding this session came from following one thread
depth-first, never from a general sweep) and five concrete, mechanically-groundable sweep categories.
Put on hold at the researcher's direction — the design-plan work continued first.

## 7. Design plan v4 — every open question answered with real content, not deferred a third time

Researcher walked through the plan's own prior Summary point by point and named five real gaps: how
code changes get recorded (answered — `BUILD.md` stays a separate, standing obligation, cross-
referenced, not replaced); how chat gets captured (verbatim-quote the operative sentence, formalised
as a `cfg_escalation.chat_routing` extension, applied live to `#6` the same turn); the relationship to
`GOVERNANCE.md`/`USER-GUIDE.md`/`CLAUDE.md`/`BUILD.md` (mapped against the project's own existing
`governance.procedural_document_taxonomy`, not a new scheme); a complete `next_action`×`state`×`type`
vocabulary, reasoned for gaps rather than just listed; and the PS front door's exact behaviour plus a
direct recommendation (keep PS, fix the dispatch — the same fix `#8` already needed, not a new one).

## 8. "The document is incomplete" — every decision needs its actual configs listed

Researcher: decisions without the concrete config rows they touch just mean inventing the detail
later anyway — exactly the failure this whole review was meant to prevent. Built a **decision
register**, a new document type distinct from the plan: every decision point gets a
new/validate/remove config accounting. First pass on five named items (`D1` widened into a genuine
two-source, two-phase, dry-run-first rebuild plan, not a simple reseed; `D3` given an actual tracking
mechanism; `D4` given all 15 exact config rows; `D5` and `D6` given real content instead of "open").
Corrected again the next round — `D1` needed a *second* source (this session's own live rows, created
after the JSON export, not accounted for at all); `D4`'s CSV design had the report content backwards
(raw table, not computed exceptions — a real mistake of my own, corrected on the spot).

## 9. Two defects found in already-shipped code, not just the design

Working through a concrete issue-lifecycle scenario with the researcher (raise → active work →
rounds of back-and-forth → "please evaluate it") surfaced that the invented three-value `issue`
vocabulary (`open`/`decided`/`abandoned`) was solving nothing the existing manual vocabulary didn't
already cover — withdrawn, a real simplification, not scope creep. That same conversation surfaced a
genuine defect in code shipped *this session's own rebuild*: the two-stage approval's same-party
refusal was built as an identity check ("must be a different person"), when the researcher's actual
intent was an **authority** check ("does this party have authority to approve"). Claude preparing and
approving the same item is legitimate when Claude holds that authority — the shipped check blocked it
unconditionally. Fix designed (authority via `next_action_assigned_to`, the field that already exists
for this), flagged for one coherent build pass rather than patched mid-review. A second, independently
found defect: cross-checking every `next_action` enum value against the live `cfg_escalation_
transition` rows (the researcher's own direct question, not assumed complete) found `ready_for_
approval` had no explicit transition row at all — reachable only by incidental coincidence of an
assignee actually changing in the same call, nothing requiring that pairing.

## 10. The decision register — consolidated, then cross-checked against the plan

Nine register versions later (`v1`–`v9`), a single 24-point consolidated reference:
6 settled, 1 rejected, 3 parked as genuine code-only fixes, 14 open with a complete, buildable
specification — exact config table names, exact field values, exact rule wording, not descriptions of
mechanism. Asked directly whether the design plan (`v4`) was already consistent with it — checked
rather than assumed yes, and found it wasn't: three places actively wrong (the withdrawn `issue`
vocabulary still shown, the same-party check still described as identity-based rather than the
authority fix, the CSV export still described backwards), four items missing entirely. Corrected in
`escalation-design-plan-v5-20260821.md`, with a structural change going forward — the plan narrates
*why*, the register is the sole source for exact config content, so the two documents can't drift
against each other silently again the way `v4` just had.

## Where this leaves things

**Nothing built.** Every artifact this session is design/specification — `escalation-design-plan-
v1` through `-v5`, `escalation-design-decision-register-v1` through `-v9`
(`iba/docs/`), plus the running record in escalation `#6` itself (16 versions). Open escalations:
`#4` (stale table text), `#5` (id collision), `#6` (the standing tracker, now the whole session's own
record), `#8` (PS/`run.py` governance gap), `#9` (on hold — the systematic-discovery gap). The
researcher's own review of the consolidated register surfaced no further changes; next session is the
actual build and migration, starting from `escalation-design-decision-register-v9-20260821.md` as the
operative specification.
