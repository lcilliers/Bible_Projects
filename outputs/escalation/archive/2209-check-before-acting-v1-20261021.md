# 2209 — Check before acting: rules read at the point of use, not only at start

Escalation: #2209 (an element of the #2177 reset). Status: a design for the researcher's decision.
Nothing built.

## The requirement

Researcher, chat 2026-10-21 (verbatim): "When I started with the IBA and config journey, I was hoping
that the before you proceed to perform a specific process, you would be wise enough to read the
instructions and rules associated with it, in stead of what you normally do and that is to just head
off in any direction based on your common knowledge. Where we are now, is that you read all the rules
and instructions at start up, and then in any case follow your own head, and sometimes you remember
some of the rules and instructions. [...] my requirement is so simple - before you do something, just
check that you do it in the right way."

## This session's record proves it

Each slip below had an instruction or rule that already stated how to do the action. None of those
instructions was read at the moment of acting.

| What I did | What already said how to do it | Cost |
|---|---|---|
| `Escalation.ps1 -Action Raise`, 3 attempts | USER-GUIDE.md section 3.2 gives the exact command | 2 failed calls |
| Withdrew #2197 with `-NextAction noted`, then `reject` without `-Comment` | The escalation transition rules (`cfg_escalation_transition`) | 2 failed calls; 2 extra versions on #2197 from validate runs in between |
| Handed #2208 over without `-NeedsFollowup 1` | Rule 63, which the Stop hook text also repeats every turn | Your approval closed an unbuilt item; 2 corrections |
| `\a` in a Python string turned into a control character | Rule 108, which names this exact trap | 1 failed write |
| Ran Compliance.ps1 under the wrong shell; `git commit -F -` with a here-string | Rule 27 and the PowerShell tool notes | 2 failed runs |
| Options v1 proposed removing controls without asking why they existed | Rule 104 (check existing rules first); rule 19 (no proceeding on assumption) | You had to send it back |

The app already has a mechanism for this, and it was never connected.
`iba/app/lib/compliance.py` says method rules "are delivered by area when work in that area starts",
and has `method_rule_lines()` to do it. Nothing calls that function.

## Why reading at start does not work

The start routine delivers about 140 rules. By the time an action comes up, the one that applies is
a long way back in context, and nothing brings it forward. A restatement at start proves the rule was
read once. It does not make me look again before the action it governs.

## Proposed control: the rules come to the action

A `PreToolUse` hook that runs before every IBA command, the same kind as the existing retired-script
gate (`.claude/hooks/gate_retired_script.py`). When a command names a PS tool, the hook puts in front
of me, before the command runs:

1. **The tool's own usage for that action,** from config. This is the documented syntax and required
   parameters, not prose I have to remember. It needs one place that holds usage per tool and action:
   a `cfg_*` table filled from USER-GUIDE.md section 3.2 and the PS help blocks.
2. **The rules tied to that action,** from config. For example:
   - Escalation Update/Raise brings rules 63 and 45 and escalation rules 5 and 13;
   - a migration brings rules 75 and 62;
   - a commit brings rule 26.

   This needs a link from each behaviour rule to the tools and actions it governs. That link does not
   exist today, and adding it is the main design work.
3. **A stop when a required parameter is missing.** For example, `-NeedsFollowup` on a hand-over of
   an item whose approval leads to more work. The hook refuses the command and says why, instead of
   letting it run and fail.

What it changes: the check happens at the moment of acting, every time, and does not rely on me
remembering. It costs a few lines of context per command, instead of the failed calls and
corrections listed above.

What it does not cover: actions that are not commands, such as writing analysis or choosing an
approach. For those, `method_rule_lines()` should be called by the PS entry point of each work area
when that work starts.

## Decision

| Question | Your answer |
|---|---|
| A. Build the pre-action hook (parts 1 to 3)? |  |
| B. Start with which tools? Claude suggests Escalation.ps1 and migrations, where most of this session's slips were |  |
| C. Connect `method_rule_lines()` to the work-area entry points? |  |
