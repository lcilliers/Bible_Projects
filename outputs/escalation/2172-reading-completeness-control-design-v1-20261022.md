# 2172 — A control that shows whether a reading reached the narrative

Escalation: #2172 (with #2177). Status: a design for your decision. Nothing is built.

The researcher chose this (2026-10-22, verbatim): "A then 1". Option 1 of
`outputs/escalation/2177-fix-the-right-thing-v1-20261022.md`: build the one control the study hold
names, app work only, no reading.

## The failure it must catch

From #2172 (2026-10-19):
- **The flesh-and-body reading was closed before it began.** 426 of 606 verses were told nowhere,
  and corrections found in readings were never applied (Heb 10:22, 1Co 6:19b-20, Neh 6:13,
  Psa 69:9).
- **Researcher (verbatim):** "there is nothing that enforces completeness, and the check that is
  built in every session-close is just junk".
- **And:** "there is no way that I can check on you".

Why nothing caught it:
- **What the database already holds:** what the narrative says. That is `narrative_claim`, the
  passages that tell each claim (`narrative_claim_telling`), and every verse each passage cites
  (`narrative_citation`, 7,562 rows).
- **What it does not hold:** what a reading proposed. That lives only in md files.
- **So every existing check compares records with records.** None compares what a reading proposed
  with what the narrative now says.

## The design

**1. Readings record their proposals as rows.** One new table, `reading_proposal`. Each row is one
thing a reading says should change the narrative:

| column | holds |
|---|---|
| escalation_id | the escalation the reading belongs to |
| source_file | the reading file the proposal comes from |
| verse_id | the verse (when the proposal is about a verse) |
| kind | `tell` (the verse should be told), `correct` (a told passage or claim is wrong), `new-claim`, `change-claim` |
| target | the chapter, or the claim_ref, it is meant to reach |
| proposal_text | what the reading says, in a sentence |
| disposition | `open`, `done` or `declined` |
| disposition_ref / reason | what shows it is done (a claim_ref or passage id), or why it was declined |

A reading is not finished until its proposals are rows. The action that records them is
`Narrative-Register.ps1 -Action Propose`, through run.py like the other register actions.

**2. "Done" is checked by the database, not taken from me.** A proposal can be set to `done` only
if the register shows it:
- `tell`: `narrative_citation` has that verse in the target chapter;
- `new-claim` / `change-claim`: the claim exists or has changed since the proposal
  (`narrative_claim_change`);
- `correct`: the passage or claim has changed since the proposal.

Otherwise the action is refused. `declined` needs a reason, and the reason is shown to you. I cannot
mark something done that is not in the narrative.

**3. Nothing closes with open rows.** An escalation that has open proposals cannot move to completed
or closed; `Escalation.ps1` refuses it. Session-close lists every open proposal by escalation.

**4. You can check it in one page.** `Narrative-Register.ps1 -Action Proposals -Id <escalation>`
writes a report: every proposal, its disposition, and for each `done` the narrative passage it
landed in, quoted. For each `declined` it shows the reason. It is computed from the database, so it
does not depend on my account.

## What it does not do

- It does not judge whether a reading is good. It only shows that what was proposed was carried, or
  was consciously declined.
- It does not find proposals I failed to write down. The rule that a reading's proposals are rows
  is the safeguard, and the report shows a reading file with no rows at all.
- It does no reading. Recording the proposals of past readings (#2162, #2171 batch 1, the
  OT-05.11 corrections) is study work and waits until you re-open the study.

## Size

- **New:** one table, two register actions (Propose, Dispose), one report action, one refusal in
  `Escalation.ps1`, one session-close line.
- **Config:** the table and its columns, two steps, write grants, the `kind` and `disposition`
  enums.
- **Test plan, run on a copy:**
  - every kind recorded and disposed;
  - `done` refused when the register does not show it;
  - `declined` refused without a reason;
  - an escalation refused at close while rows are open;
  - the report on a synthetic reading.
- **Estimate:** one Developer Mode session.

## Decision

| Point | Your choice | Comment |
|---|---|---|
| 1. Build this design (approve / revise / reject) | | |
| 2. Granularity: one row per verse (as above), or one per claim only | | |
| 3. Close gate: refuse the close (as above), or warn only | | |
