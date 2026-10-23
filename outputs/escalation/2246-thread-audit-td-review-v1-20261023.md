# #2246 -- Thread audit T-d flags open catch-up items as stale

Researcher 2026-10-23, verbatim: "ThreadAudit (escalation-thread-audit-v8-20261023.md) found five
items under T-d, should have been cleared: each sits on a strand whose escalations are all completed
but is still open.  Can you verify and close them"

## Finding: the five items are open by design, so none was closed

Each item is a #2172 catch-up (decision 5) item: prose reading files of 6 to 19 October not yet
recorded as observations. Checked against the live database (`iba/app/db/iba.db`, read-only):

| item | cluster | files named | in `reading_file` with `imported_observations` set | `ib_observation` rows since 2026-10-06 | item opened | strand escalations completed |
|---|---|---|---|---|---|---|
| OT-108.3 | M64 Will & Resolve | 13 | 0 of 13 | 46, all run CATCHUP-2172-B-20261022-origin-of-thought (the origin-of-thought strand, not these files) | 2026-10-22 | #1978 2026-10-08, #1986 2026-10-08 |
| OT-108.4 | M72 Authority & Dominion | 3 | 0 of 3 | 0 | 2026-10-22 | #1998 2026-10-12 |
| OT-108.5 | M08 Pride & Arrogance | 6 | 0 of 7 indexed | 0 | 2026-10-22 | #2156 2026-10-15 |
| OT-108.6 | M09 Humility & Lowliness | 7 | 0 of 7 | 0 | 2026-10-22 | #2148 2026-10-15 |
| OT-108.8 | M18 Desire & Longing | 20 | 0 of 20 | 0 | 2026-10-22 | #1993 2026-10-14 |

The readings were written as prose but never reached the tables, which is what each item records.
They come back when those files are recorded through `iba\app\ps\Reading.ps1` (Open, Record).

## Cause

`iba/app/lib/threadaudit.py` T-d treats a cluster as worked when every escalation listed for it in
`cfg_setting escalation.worked_strand_escalations` is completed, and then calls every open
`cluster:` or `strong:` item on it stale. It does not look at when the item was opened. Each of
these five items was opened a week or more after its strand closed, about work that strand left
unrecorded, so the strand's completion cannot have cleared it.

## Options (decision)

- **A. Date rule in T-d (recommended).** An item counts as "should have been cleared" only if it
  was opened before the last listed escalation for its cluster was completed. An item raised after
  the strand closed is new work, not a leftover. A small change in `iba/app/lib/threadaudit.py`,
  plus a test on the five items (they drop out) and one synthetic item opened before completion
  (it stays a finding).
- **B. Take the five clusters out of `escalation.worked_strand_escalations`** until their catch-up
  readings are recorded. Config only, but T-d then stops checking every other item on those
  strands, and the setting has to be edited back by hand later.
- **C. Leave T-d as it is** and accept these five findings at every start until the readings are
  recorded. Nothing to build, but the startup report keeps showing findings that need no action
  (the P0 instruction on reports with no meaning).

Decision: ______
