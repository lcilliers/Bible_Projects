# Open threads register: carrying it in the escalation table (proposal, v2)

**Date:** 2026-10-12 · **Escalation:** #1999 · **Supersedes:** `archive/open-threads-table-proposal-v1-20261012.md`, which proposed three new tables. · **Status:** proposal for the researcher's decision. Nothing is built.

**Researcher, chat 2026-10-12, verbatim:** *"should we not extend escalations, it seems that escalation and open items register are close to each other, and escalation has all the controls already built in."*

## 1. Why extend the escalation table, not build beside it

Escalations already have what v1 would have built again:
- a state machine driven by config (`cfg_escalation_transition`, `cfg_escalation_requirement`)
- a per-version history (`escalation_history`), which would replace v1's "event" table
- an assignee, a next action and a resolution
- one front door (`Escalation.ps1`) and a List report
- a place in session start, which already reads open escalations

A thread is a held item that is waiting for something. An escalation in state `on-hold` is the same shape. So **v1's `open_thread` and `open_thread_event` are not needed.**

## 2. What is missing, and has to be added

| Gap | Why | Proposed change |
|---|---|---|
| **1. Matching by cluster or Strong's** | A thread comes back when a strand reaches its cluster or Strong's numbers. Escalations have no field for this. | A child table, `escalation_trigger`: escalation id; kind (cluster, strong, strand, event, researcher); value; status (open or closed); a note. This is the one genuinely new table. |
| **2. Closure for one cluster** | OT-16 is "closed for M72" and open for others. | A trigger row is closed. The escalation stays `on-hold` while any trigger is open. |
| **3. A type for threads** | Threads must be told apart from tasks and decisions. | A new type `thread` in `cfg_enum` and in `Escalation.ps1`'s `-Type` list. A thread rests in `on-hold`, assigned to Claude, or to the Researcher where it waits on you (OT-99, OT-100). |
| **4. Keeping List readable** | Live escalations today: 12, all tasks. Adding 89 open threads would bury them. | List shows threads in their own section, as counts plus the ones that match the strand in progress. A new action `-Action Match -Cluster M18` (or `-Strong`) gives the check before a pull. |
| **5. The OT numbers** | OT-nn is cited in many files: ledgers, narrative working notes, CLAUDE.md. | Keep it as an alias column (`alias`, for example `OT-16`). The escalation id becomes the key, and OT-nn stays searchable. New threads take the next OT number. |
| **6. Requirement rules** | Some readiness rules were tuned for tasks. For example, `ready_for_approval` needs a resolution (D25). | Check every `cfg_escalation_requirement` row against the `thread` type. A thread is resolved through the same Update path, with its resolution. |

## 3. A rule that changes

The register's rule of use is *"It is not a task list … Decisions stay in escalations."* The intent of that rule still holds: a thread is not worked as a task, and it moves only when a strand reaches it. What changes is that threads now live in the escalation table under their own type. The rule is restated to say so, in GOVERNANCE.md, and as a `cfg_behaviour_rule` if one carries it.

## 4. Migration

- Each of the 100 OT rows becomes an escalation of type `thread`:
  - the alias is the OT number
  - the thread text goes in whole
  - the raised date and source are kept
  - the state follows the status: open or touched becomes `on-hold`; resolved becomes `completed`, with its resolution
- Cluster codes and Strong's numbers are lifted from "comes back when" into trigger rows. Cases like OT-16's "closed for M72" become closed triggers.
- The dated "touched" paragraphs are kept in the migrated text, marked as earlier history. From then on, touches go through Update, so they land in `escalation_history`.
- You get a review list of the rows where the triggers did not separate cleanly.

`open-threads-register.md` becomes a generated report at the same path, produced by List or a small export, so existing links still work.

## 5. Build and governance

This is a change to the IBA app's own escalation module. So it is built in developer mode, with config first:
- `cfg_enum` for the type and the trigger kinds
- a check of `cfg_escalation_requirement`
- a migration
- `lib/escalation.py` and `Escalation.ps1` changes (Match, the List section, the alias)
- tests
- a GOVERNANCE.md section

Session start step 4B switches to `Escalation.ps1 -Action Match`.

## 6. For your decision

1. Approve extending the escalation table as above, in place of v1's separate tables.
2. Closure for one cluster through trigger rows. The alternative is to split such threads into one per cluster.
3. Keep OT-nn as an alias, and keep the generated `.md` at the same path.
