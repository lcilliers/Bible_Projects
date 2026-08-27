# Proposal — a real gate on `resolution_kind=self_correctable`, not just a documented convention

**Escalation:** #921 (decision_required). **Status:** proposal only — nothing built. Prepared for
approval per the researcher's instruction on #921 v2 ("proceed to prepare this for approval").

## 1. The problem, precisely

`resolution_kind` (`decision_required` / `self_correctable`) is hard-enforced in exactly two
places today:

- `configmaint.propose`'s pause — always `decision_required` in code (`handlers/configmaint.py`,
  `GOVERNANCE.md` §48: "a config change is definitionally a design decision").
- `reports.py`'s `.validate()`-step escalations — always `decision_required` (same section).

Everywhere else — every escalation raised through the generic `Escalation.ps1 -Action Raise
-ResolutionKind ...` path — the value is a free choice made by whoever raises it, with **no
config-level or code-level check** on whether the choice fits what the item actually describes.
This is the gap escalation #920 fell straight through: I raised a table-drop-plus-new-mechanism as
`self_correctable` and closed it myself in the same breath. Nothing in the system could have
refused that, because nothing checks the *content* of a manually-raised item against its declared
`resolution_kind` at all.

## 2. What a real gate needs to do

Catch the specific, confirmed failure mode — design/build work (schema changes: new/dropped
tables, new patch-operation types, new mechanisms) declared `self_correctable` — without requiring
new infrastructure this project doesn't already have (no cross-database write log links an
escalation id to "which files/tables a fix actually touched"; migrations are run directly by
Claude Code, not through a mechanism that stamps its writes with the current escalation id).
Given that constraint, the only signal available today is the **text already being written** —
`comment` at Raise, `resolution`/`tried` at Resolve — so the gate has to work on that.

## 3. Options considered

**A. Documented rule only (`cfg_behaviour_rule`, no code check).** Matches how most working-method
rules in this project are recorded. Rejected as insufficient here specifically because the
researcher's complaint is that *this exact kind of rule already existed in my own judgement* and I
still violated it minutes after correctly applying it elsewhere in the same conversation — a
documented-only rule didn't hold the first time and there's no reason to expect it holds next time
either.

**B. A time/session gap between raise and resolve.** E.g. refuse `resolve-self-correctable` if
called within N seconds/same run of `raise`. Rejected: purely mechanical, trivially defeated by
waiting, and would have blocked plenty of genuinely-instant, genuinely-correct self-corrections
(e.g. #915/#916/#917/#918/#919 this same session, all legitimately resolved immediately).

**C. Pattern gate on the escalation's own text.** A new `cfg_enum` group (e.g.
`design_work_indicator_pattern`) holding a short list of substrings/patterns that, if found in
`comment` (at Raise) or `resolution`/`tried` (at `resolve-self-correctable`) when
`resolution_kind=self_correctable`, cause a **hard refusal** — not a warning — with a message
pointing at the correct path (raise as `decision_required` directly, or `escalate_to_decision` if
already raised as self_correctable). Seed list, drawn directly from what #920's own comment/
resolution actually said (i.e., the words that WOULD have caught it): `migration/`, `CREATE TABLE`,
`DROP TABLE`, `ALTER TABLE`, `new cfg_table`, `new cfg_step`, `new cfg_write_grant`, `new patch
operation`, `new mechanism`, `schema change`.

**Honest limitation, stated plainly:** this is a text-pattern check, not a structural one. It will
catch this failure mode and close variants of it (which is what's confirmed to have happened); it
will not catch a future misclassification that avoids all the trigger words while still describing
real design work. It is a real, testable, code-enforced gate — not nothing — but it is not a
complete solution to "can Claude be trusted to classify its own escalations correctly," which no
purely mechanical check fully closes.

## 4. Recommendation

**Option C**, seeded with the pattern list above, enforced in two places:

- `raise_new()` — refuse at Raise if `resolution_kind=self_correctable` and `comment` matches a
  live pattern.
- `resolve_self_correctable()` — refuse at Resolve if `resolution` or `tried` matches a live
  pattern, even if the item was raised clean (catching a case where the fix grew into design work
  between raise and resolve, which is exactly what happened with #920 — the comment at raise time
  was still fairly narrow; it was the resolution that revealed the full scope).

Pattern list lives in `cfg_enum` (module-governed, changeable via `Config-Maintenance.ps1 -Step
Propose` like any other enum, not hardcoded) so it can be extended the next time a new failure
shape is found, per this project's own standing pattern (§48/§49 grew the same way).

## 5. What is NOT proposed here

No change to `configmaint.propose` or `reports.py`'s existing hardcoded behaviour (unaffected). No
attempt to retroactively reclassify #920 (left as-is, per the no-erasing discipline already agreed
on #921). No code written yet — this document is the proposal only.

## 6. Decision needed

Approve as described / reject / revise (e.g. a different or shorter seed pattern list, or a
different enforcement point). On approval, the build is small: one new `cfg_enum` group + two
`if`-checks in `iba/app/lib/escalation.py`, migration-registered, tested live against a synthetic
case reproducing #920's own text before being considered done.
