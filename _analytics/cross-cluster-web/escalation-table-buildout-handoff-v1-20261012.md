# Escalation table build-out: handoff for a new chat

**Date:** 2026-10-12 · **Escalation:** #2000 (supersedes #1999) · **Status:** for a new chat. Nothing is built.

## 1. What the researcher said, verbatim and in order (chat 2026-10-12)

1. *"Do you think we should push the Open threads register to a table, it seems that we many be better able to control and manage the follow-up as a table. you can add the open register as a standard item when a new session is started."*
2. *"should we not extend escalations, it seems that escalation and open items register are close to each other, and escalation has all the controls already built in."*
3. *"I am prepared to work with you to re-align the escalation system, your suggested are well made, and I have some more. create a new escalation to build out the escalation table, add all the notes related to it in the session to it. We can then work on it in a new chat."*

**The researcher has further suggestions. Start the new chat by asking for them.** Do not build from §3 alone.

## 2. Facts, measured 2026-10-12

**The register.** `_analytics/cross-cluster-web/open-threads-register.md` is one Markdown table, set up under #1935 on 2026-10-02.
- It has 100 rows and runs to 98 KB. The median row is 858 characters; the longest is 3,137.
- By status: 84 open, 5 touched, 11 resolved or closed.

**Problems seen:**
- **"Comes back when" is prose.** Finding the threads that bear on a strand means reading every row.
- **History piles up in the status cell.** OT-16, OT-97 and OT-98 each hold several dated paragraphs.
- **Closure for one cluster only has no field.** OT-16 and OT-98 are "closed for M72" but stay open for other clusters.
- **The status words have drifted.** The set is meant to be open, touched and resolved. The cells now also say "closed", "closed for M72" and "**resolved** (#…)".
- **Records scripts edit cells by splitting rows on " | ".** This session's examples: `../Clusters/M72 - authority-dominion/m72-group-B-records-update-v1-20261012.py`, `-v2-`.

**The escalation table in iba.db.** Columns:
- id, version, run_id, source, at_step, type, short_description, context, comment, tried
- state, next_action, next_action_assigned_to, originator, resolution
- raised_at, answered_at, resolution_kind, needs_claude_followup

**Config tables:** `cfg_escalation`, `cfg_escalation_transition`, `cfg_escalation_requirement`.

**Escalations by state:**

| State | Count |
|---|---|
| completed | 1,095 |
| withdraw | 93 |
| closed | 38 |
| supersede | 34 |
| on-hold | 5 |
| raised | 5 |
| in-progress | 1 |
| re-assigned | 1 |

The 12 live (non-terminal) escalations are all type `task`. The `-Type` values allowed today are task, run_error, issue, notice, config and note.

## 3. The proposal so far

Proposal v2 is `open-threads-table-proposal-v2-20261012.md`. v1, which proposed three new tables, is in `archive/`.

**Extend the escalation table; do not build a parallel one.** It already has a state machine driven by config, a per-version history (`escalation_history`), an assignee, a next action and a resolution, one front door (`Escalation.ps1`), a List report, and a place in session start.

**The gaps to close:**
1. **Matching by cluster or Strong's.** One new child table, `escalation_trigger`: escalation id; kind (cluster, strong, strand, event, researcher); value; status (open or closed); a note.
2. **Closure for one cluster.** The trigger row closes. The escalation stays `on-hold` while any trigger is open.
3. **A `thread` type.** It goes in `cfg_enum` and in `Escalation.ps1`. A thread rests in `on-hold`, assigned to Claude, or to the Researcher where it waits on the researcher (OT-99, OT-100).
4. **A readable List.** Threads get their own section, so they do not bury the 12 live items. A new action, `-Action Match -Cluster Mnn` (or `-Strong`), runs the check before a pull.
5. **The OT numbers.** OT-nn stays as an alias column, because it is cited across ledgers, narrative working notes and CLAUDE.md. New threads take the next OT number. `open-threads-register.md` becomes a generated report at the same path.
6. **Requirement rules.** Check every `cfg_escalation_requirement` row against the `thread` type.

**A rule changes.** The register's *"It is not a task list … Decisions stay in escalations"* keeps its intent: a thread moves only when a strand reaches it. It is restated, because threads would now live in the escalation table under their own type.

**Migration:**
- Each of the 100 OT rows becomes an escalation of type `thread`.
  - The thread text goes in whole.
  - The OT number becomes the alias.
  - open and touched become `on-hold`; resolved becomes `completed`, with its resolution.
- "Comes back when" is split into trigger rows by pattern (M-codes and Strong's). Partial closures become closed triggers.
- The dated "touched" history is kept in the migrated text.
- A review list names the rows where the split was not clean.

**Build:** a change to the IBA app's own escalation module, so it is built in developer mode, with config first:
- `cfg_enum`
- a check of `cfg_escalation_requirement`
- a migration
- `lib/escalation.py` and `Escalation.ps1` (Match, the List section, the alias)
- tests
- a GOVERNANCE.md section

**Decisions still open in v2:**
1. Closure for one cluster through trigger rows, or split such threads into one per cluster.
2. Keep OT-nn as an alias, and keep the `.md` at the same path.

## 4. Done already, on instruction

- `.claude/commands/start-project.md` step 4B reads the open threads register at every session start. It reports the counts by status, the threads that bear on the strand in progress, and the threads waiting on the researcher. Once the build is done, it switches to `Escalation.ps1 -Action Match`.
- CLAUDE.md, under the M72 strand, points to this work.

## 5. Escalation.ps1 behaviour met this session (useful for the redesign)

- **Raise needs both `-Question` and `-Comment`.**
- **The Raise title is `-Question`.** It must be one line of 60 characters or fewer, with no "--". `-ShortDescription` is read only by `-Action Correction`.
- **D26:** an Update carrying `-Comment`, `-Context` or `-Tried` cannot leave the item at state `raised`. Pass `-State in-progress`, for example.
- **D25:** `-NextAction ready_for_approval` needs `-Resolution`. So a decision item waiting on the researcher cannot be marked ready before the decision; it sits at `in-progress` / `review` instead.
- **`-AnsweredBy` is required on every write action.**
