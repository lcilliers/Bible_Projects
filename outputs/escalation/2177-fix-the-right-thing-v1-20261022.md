# 2177 — Fixing the right thing: where the app work goes next

Escalation: #2177 (the IBA app reset), with #2207. Status: your judgement call; nothing is started.

## What you said

Researcher, chat 2026-10-22 (verbatim): "I think you are now starting to unravel.  it is right that
you identify all the weaknesses, omissions and errors of the past. but because the actual methods are
not delivering what it supposed to, you are in danger of fixing the wrong issues.  I am not sure what
to do - leave everything in the air, as so many times in the past,  say no to the fixes - that will
just mean you will continue to make the same errors, or first focus on the real objective and that is
to perform operations that make sense, is valuable and deliver the objectives of the study."

## Claude's assessment

You are right, and today's session shows it.
- **The target was the checks' own output.** The #2207 backlog is the list of findings that
  `configmaint.validate` prints. It is not a list of things that stop the study working.
- **The approved table was wrong on 2 of the 7 utilities.** I had proposed retiring `lexicalscope`
  and `batchcontrol`; three and five live steps depend on them. Checking the live code caught it
  this time, but the plan itself came from reading counts, not from what the study needs.
- **The work is drifting into the checks themselves.** The five open decisions in
  `outputs/escalation/2207-item2-utility-decisions-v1-20261022.md` are mostly about whether a file
  should be exempt from a check. Settling them changes no result the study produces.
- **The same goes for most of what is left.** Items 3 and 4 (13 rules, errors-only validate) are
  still about controls on the controls.

The control the study actually lacks is already on record. The hold reason in
`governance.study_status` is #2172: readings did not reliably reach the narrative and the claims
register, and no control enforces that completeness. You said then (#2172 v2): "I have no way to tell
how large this problem is, and there is no way that I can check on you." No #2207 item touches that.

## Options

| Option | What happens | Cost |
|---|---|---|
| A. Stop #2207 here | Commit what is built and tested (sections 381 to 383, all live and validated). Remaining items and the five decisions go on-hold with their reason. Nothing more is built for the checks' sake. | The 4 utility and 13 rule findings stay visible in validate. |
| B. Finish #2207 first | Answer the five decisions, then items 3 and 4. | Probably two or more sessions on controls that do not change study results. |
| C. Leave it in the air | Nothing committed or parked. | The pattern you named. |

Then, for whichever of A or B you choose, the next app work is one of these two:

| Next | What it is |
|---|---|
| 1. #2172 first | Build the one control the hold names: for a reading, show mechanically what reached the narrative and the claims register and what did not, so you can check it without trusting me. App work only; no reading is done. |
| 2. Nothing until you re-open the study | The app waits; the study stays on hold. |

**Claude recommends A then 1:**
- **A** keeps the tested work and stops the drift.
- **1** is the only app work that deals with your stated reason for the hold.

Re-opening the study stays your decision (`governance.study_status`). Option 1 builds the check, and
does no study work.

## Decision

| | Your choice | Comment |
|---|---|---|
| #2207: A, B or C | | |
| Next: 1 or 2 | | |
