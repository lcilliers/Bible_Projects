# Cost of the rebuilt start-project and session-close (estimate)

> v1, 2026-10-21, escalation #2173. Researcher (verbatim): *"before I approve, I want to deal with
> cost. what is the estimated cost of the two routines."*
>
> **These figures are estimates, not measurements.** Token counts are the measured sizes (in
> characters) of what each step puts in front of Claude, divided by 4 (a rough rule for English
> and markdown). The dollar figures are API-equivalent rates for Claude Opus 5.5. If this project
> runs on a Claude subscription, the cost is a share of the plan's usage limit, not a bill, but the
> relative sizes hold.

## 1. How a session is charged

Rates, Claude Opus 5.5, per million tokens: input $4.00, output $20.00, cache write (1-hour
cache, which this app uses) $8.00, cache read $0.20.

Claude Code re-sends the whole conversation on every turn (every tool call). After the first time,
that history is read from cache at $0.20 per million. So **whatever a routine adds at the start of
a session is paid once to write and then again on every later turn**:

- 1,000 tokens added at start, with 150 later turns: $0.008 (write) + 150 x $0.0002 = **about $0.04**.
- This session had well over 150 turns. A short session has fewer, a long build more.

At close the cost works the other way: the close runs when the history is already large, so each
of its turns re-reads everything. At a history of 300,000 tokens one turn costs about $0.06.

## 2. Start-project

| What enters the session | Size | Tokens (est.) | Cost (est., 150 later turns) |
|---|---|---|---|
| The command file | 6.2k chars | 1,600 | $0.06 |
| `Start-Iba` output, mostly the full text of all 141 rules | 77.2k chars | 19,300 | $0.73 |
| Context report (files of the open escalations) | 7.3k chars | 1,800 | $0.07 |
| Thread audit report (186 findings) | 15.6k chars | 3,900 | $0.15 |
| Other tool output (STEP, checks) | about 8k chars | 2,000 | $0.08 |
| **The compliance file, written by Claude** (141 rows) | 20.8k chars | 5,200 written, plus about as much reasoning | $0.21 output + $0.20 carried |
| **Subtotal, without reading the escalations' files** | | **about 34,000** | **about $1.50** |
| Reading the files the open escalations name, as the command now says ("read the latest file(s) of each open escalation") | 2.6 MB, 23 files | about 650,000 | **about $25**, and near the context limit |
| Same, but only files up to 30 KB (17 files) | 197 KB | about 49,000 | about $1.90 |

**The old start** put about 15,000 tokens in front of Claude (the governance settings about 5,000,
the escalation list about 4,000, the threads list about 2,400, the command and the rest about
3,500): **about $0.60**.

**Increase per session:** about **+$0.90** without the file reading; about **+$2.80** if every file
up to 30 KB is read; about **+$26** if the command is followed literally.

**The real problem is the file reading.** Most of the 2.6 MB is living documents that #2173 itself
names (BUILD.md 1.4 MB, GOVERNANCE.md 360 KB, CLAUDE.md 115 KB, lib/escalation.py 150 KB) and one
cluster report (cluster-assign-v6, 270 KB, named by #2166). Reading those whole at every start
adds nothing to the next action and cannot be afforded. The rule needs a limit (option L1 below).

## 3. Session-close

| Part | Estimate |
|---|---|
| Filling in evidence for the engaged rules during the session (89 rows this session, short edits) | about 3,000 output tokens and a few turns: **about $0.25** |
| The close itself: detection, reading the report, fixes and dispositions, the log (about 1,500 tokens written), a re-run, the export or copy if needed, two commits. About 12 turns at a 300,000-token history | **about $0.95** |
| **Total** | **about $1.20** |

**The old close** took about 8 turns at the same history size, plus the narrative copy and the
threads export at every close: **about $0.55**. **Increase: about +$0.65 per session.** A close
with many findings costs more; this session's close (five code faults fixed while it ran) was not
typical.

## 4. Both routines

| | Old | New, file reading as written | New, with L1 (reading capped at 30 KB) | New, with L1 and L2 |
|---|---|---|---|---|
| Start | about $0.60 | about $26.50 | about $3.40 ($1.50 + $1.90) | about $2.50 ($0.60 + $1.90) |
| Close | about $0.55 | about $1.20 | about $1.20 | about $1.20 |
| **Per session** | **about $1.15** | **about $27.70** | **about $4.60** | **about $3.70** |

The file-reading part scales with how many open escalations there are and what they name; on
2026-10-20 there were six. With the study on hold, most sessions will have fewer.

## 5. Ways to cut it (each is your decision)

- **L1. Limit the file reading (largest saving, recommended).** The start reads in full only the
  files of open escalations that are deliverables (proposals, readings, overviews) up to a size
  limit, for example 30 KB. Living documents (BUILD.md, GOVERNANCE.md, USER-GUIDE.md, CLAUDE.md)
  and code are never read whole at start; a larger file is searched for the part the escalation
  names. The Context report already shows each file's size, so the limit can be applied by the
  code (a setting) rather than left to judgement. Saves about $23 per session against the command
  as written (about $25 down to about $1.90 on 2026-10-20's open escalations); a lower limit saves
  more.
- **L2. Carry the compliance file forward.** The start pre-fills each rule's row from the last
  session's file, and prints in full only the rules that are new or changed since then (the
  config audit table records every change). Claude confirms or rewrites each carried row for the
  work in hand. Saves about 19,000 tokens read and about 5,000 written per session (about $0.90).
  **Trade-off:** it weakens "read every rule every session"; a carried row can be confirmed
  without being re-read. Your close-time check (SC6) and spot checks still apply.
- **L3. Thread audit summary only.** Chat names counts per check; the report is read only when
  the work touches a thread. Saves about $0.15. Small.
- **L4. Fewer close turns.** Run the close's commands in fewer tool calls. Saves perhaps $0.20.
  Small.

I recommend L1 in any case: without it the start, as written, is not workable. L2 is a judgement
on how much the rule-reading control is worth to you. I have changed nothing; #2173 waits for
your direction.
