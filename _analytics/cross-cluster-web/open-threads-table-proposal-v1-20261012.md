# Open threads register: moving it to a table (proposal, v1)

**Date:** 2026-10-12 · **Status:** proposal for the researcher's decision. Nothing is built.

**Researcher, chat 2026-10-12, verbatim:** *"Do you think we should push the Open threads register to a table, it seems that we many be better able to control and manage the follow-up as a table. you can add the open register as a standard item when a new session is started."*

## 1. What the register is now

`open-threads-register.md` is one Markdown table, set up on 2026-10-02 under #1935.

**Size:** 100 rows and 98 KB. A row runs 858 characters at the median, and the longest runs 3,137.

**Status, read from the status cell:**

| Status | Rows |
|---|---|
| open | 84 |
| touched | 5 |
| resolved or closed | 11 |

**Where it strains:**
- **Matching a new strand to its threads is done by reading.** The "comes back when" cell is free text, and the clusters and Strong's numbers are buried in prose. Before each unit pull (rule of use 2), someone has to read all 100 rows.
- **History piles up in one cell.** Each touch is appended to the status cell, so status and history are mixed. OT-16, OT-97 and OT-98 now hold several dated paragraphs each.
- **A thread can close for one strand and stay open for others, with nowhere to record that.** Examples are OT-16 and OT-98, "closed for M72". There is no field for this, so it lives inside the text.
- **Edits are fragile.** Today's records scripts change cells by splitting on " | " inside 3,000-character rows.
- **The status words have drifted.** The set is meant to be open, touched and resolved. The cells now also say "closed", "closed for M72" and "**resolved** (#…)".

## 2. Recommendation: yes, as a table in iba.db, with the Markdown file kept as a generated view

iba.db already holds observations, escalations and config, and bible_research.db is now prose only (GOVERNANCE.md §81). So the threads belong in iba.db.

| Table | One row per | Main fields |
|---|---|---|
| `open_thread` | thread | `ot_id` (OT-nn, kept as is); `title`; `body` (the thread text, verbatim quotes kept); `raised_at`; `raised_from` (ledger, escalation or reading file); `status` (enum: open, touched, resolved, withdrawn); `resolution` |
| `open_thread_trigger` | "comes back when" condition | `ot_id`; `kind` (enum: cluster, strong, strand, event, researcher); `value` (for example M72, H3027H, "researcher re-read"); `status` (open or closed, so a thread can close for one cluster and stay open for another); `closed_note` |
| `open_thread_event` | touch | `ot_id`; `at`; `kind` (enum: touched, resolved, note); `source` (escalation, ledger, file); `text` |

**One front door,** in the same style as Escalation.ps1: `iba\app\ps\OpenThreads.ps1`.

| Action | What it does |
|---|---|
| `List` | Writes `open-threads-register.md` as a generated report. You keep reading the same file, but it is no longer edited by hand. |
| `Match -Cluster M18` (or `-Strong H0183`) | Lists the threads whose open triggers name that cluster or Strong's number. This is the "before each unit's pull" check, done by query. |
| `Add` | Raises a new thread. |
| `Touch` | Records a touch as an event. |
| `Resolve` | Resolves a thread. |
| `CloseTrigger` | Closes a thread for one cluster, as with OT-16 for M72. |

**Migration:**
- Every row is carried over, including resolved ones, so no history is lost.
- The thread text goes in whole.
- Cluster codes and Strong's numbers are lifted from "comes back when" by pattern into trigger rows. A trigger with none stays as one free-text trigger.
- The dated "touched" paragraphs become event rows.
- A review list names every row where the split was not clean. You check that list; you do not re-read all 100.

**What does not change:** the rules of use. A thread is not a task, it moves only when a strand reaches it, and decisions stay in escalations.

**Governance:**
- the enums go in `cfg_enum`
- the report path goes in `cfg_setting`
- a GOVERNANCE.md section
- built under developer mode, with tests

## 3. The cheaper alternative

Keep the Markdown file, and change two things:
- add a column listing the trigger codes
- move the history into a separate dated log

This removes the cell-splitting and lets you grep by code. It does not give closure per cluster, or a query you can run at session start. I would not recommend it, because the register is growing by several rows per strand.

## 4. For your decision

1. Build it in iba.db as in §2, or take the alternative in §3.
2. Closure per trigger (§2): is a thread "closed for M72" the right model, or should such threads be split into one thread per cluster?
3. The generated `.md` view: keep it at the same path, so that existing links still work?

## 5. Already done (instructed)

Session start now reads the register as a standard item: `.claude/commands/start-project.md`, step 4. Until the table exists, it reads the Markdown file. It gives the counts by status, and names the open threads whose "comes back when" mentions the strand in progress. If the table is built, that step will switch to `OpenThreads.ps1 -Action Match`.
