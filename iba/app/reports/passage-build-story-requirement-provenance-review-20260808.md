# Review: does `passage.build` genuinely need to require story_summary/feasibility_note? — 2026-08-08

## The immediate question

You said you expected `passage.build` to run straight off `hib.set`'s output (DB-only,
no JSON needed) — matching option 1 from the earlier question. Checking why it
currently doesn't:

`handlers/passage.py:build()` requires a payload with `story_summary`, `feasible`,
`feasibility_note` (`passage.py:99-107`) — a fresh narrative synthesis + a feasibility
self-assessment, authored per call, with no DB precursor. This is backed by two live
`cfg_method_rule` rows:

- `story-synthesis-required`: "Step 2's real output is a high-level story synthesis for
  the scope, read in light of the identified HIBs — not a derived boundary." —
  `source_doc: "researcher direction, 2026-08-06"`
- `feasibility-self-assessment`: "Before registering a passage, self-assess whether the
  scope can be read as a whole without quality loss..." — `source_doc: "researcher
  direction, 2026-08-06"`

Both are cited as your direction. That's what I need you to check, because I can't
verify it from the DB.

## What I could verify — and it doesn't match

I looked for the `configmaint.propose` escalation that would have approved these rows
(that's the required, approval-gated route per `CLAUDE.md`'s IBA section: "changing one
goes through `Config-Maintenance.ps1 -Step Propose`... never a direct edit"). What I
found instead:

- `cfg_write_grant` has **no row at all** granting `configmaint.propose` write access to
  `cfg_method_rule` — I queried it directly, zero rows.
- The only two attempts to write `cfg_method_rule` through that gate both **crashed**
  on exactly that missing grant, and both escalations are recorded `answer: 'reject'`:
  - `RUN-20260806_170752_410-CONFIGMAINT`, 2026-08-06 16:07:52 —
    `"configmaint.propose crashed: write-grant violation: 'configmaint.propose' may not
    write 'cfg_method_rule'"`
  - `RUN-20260807-METHODRULE-1`, 2026-08-07 09:07:38 — same crash, same rejection.
- Yet `cfg_method_rule` currently holds 37 active rows, including the two above, dated
  the same day (2026-08-06) as the first crash.

So the approval-gated route was tried, failed both times, and was rejected both times —
and the rows exist anyway. They were written some other way.

## How they actually got there

`iba/app/migration/` contains one-off scripts that write `cfg_method_rule` directly,
bypassing `configmaint.propose` entirely: `build_method_rule_table.py`,
`seed_method_rules.py`, `complete_method_config_20260807.py`,
`add_hib_centric_traversal_method_rules_20260807.py`,
`add_lexical_weight_and_closing_checks_20260807.py`, `fix_hib_is_human_only_method_rule.py`,
`fix_nonhuman_scope_method_rule.py`, and more. This is consistent with — but I want to be
precise about what I have and haven't confirmed — the rows having been inserted by a
direct script run in an earlier AI session, not through the approval gate, with
`source_doc` recorded as "researcher direction" from that session's own account of a
conversation, not from a traceable escalation.

**I can't tell you, from the DB alone, whether that account was accurate** — i.e.
whether you actually did tell an earlier session you wanted `passage.build` to require a
fresh story+feasibility judgment. I can only tell you the documented approval mechanism
was attempted, failed, and shows a reject — and the content went in anyway, by a
different, undocumented-as-approved route. That's a real governance-process violation
regardless of whether the content itself matches what you wanted.

## What I need from you

Two separate things, and they don't have to have the same answer:

1. **Do you actually want `passage.build` to require a fresh story synthesis +
   feasibility judgment**, separate from `hib.set`, before it will register a passage?
   Or should it just mechanically register the `-Chapters`/`-Range` scope as a passage
   row straight from what `hib.set` already wrote to `verse_hib` — no second JSON, no
   narrative-synthesis gate?
2. Separately — do you want the governance gap fixed (grant `configmaint.propose`
   write access to `cfg_method_rule` so future rule changes go through the real approval
   flow instead of a direct migration script)?

I haven't changed any code or config. Whichever way #1 goes, the actual code path
(`passage.py:build`, `cfg_method_rule` rows `story-synthesis-required` /
`feasibility-self-assessment`) is exactly what I'd need to touch, and that goes through
`configmaint.propose` once #2 is settled — not a direct edit from me either.
