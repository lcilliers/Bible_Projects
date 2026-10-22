# 2219 — Open items in strand reading: what is built, and design options

Escalation: #2219 (from #2172). Status: findings and design options for your decision. Nothing
built.

Researcher, chat 2026-10-22 (verbatim): "I just want to get confirmation that you firmly built in
the handling of the open items - both in terms of creating new ones on discovery, and reading the
open items into the analysis to ensure that they are taken into account, and on completion, the
update/resolution of the open items."

## 1. The answer: no, not firmly

I checked the built code, `iba/app/lib/strandreading.py` and `iba/app/handlers/strandreading.py`,
on 2026-10-22.

| Part you asked about | What the tool does | Firm? |
|---|---|---|
| **Reading open items in** | Step 1 Context (`context()`, lines 214-225) lists the open thread items that match the strand in its context file. An item matches on four things: the strand's Strong's codes (exact code only), the strand's home cluster, the strand's code, or a verse among its hits. | Partial: the items are shown, but nothing requires them to be taken into account |
| **Creating new ones on discovery** | Step 4 Map: a narrative statement that has no claim is written as one comment on the strand's escalation (handler lines 84-99), not as an open item. Step 5 Derive: an observation disposed as `held` must name an item that **already exists** (lines 544-548). Making the item is a separate, manual `Escalation.ps1` call. | No |
| **Updating or resolving them on completion** | No step answers the items Context matched. The close gate `strand_account_clean` (`account_gaps()`, lines 630-637) checks two things only: hits with no face or reason, and observations still at `draft`. The Account page does not list the matched items. | No |

## 2. The gaps

1. **Items shown, not answered.** A strand can close with every matched item untouched, and there
   is no record of whether each one was taken into account.
2. **The match is narrower than the escalation tool's.**
   - `Escalation.ps1 -Action Match` (`iba/app/lib/escalation.py`, `match_threads`) matches a
     Strong's number on its exact code or its zero-padded base. Context matches the exact code only.
   - Context matches only the strand's home cluster, not the other clusters its words sit in. For
     example, origin of thought homed at M64 Will & Resolve would not see the items OT-108.10 to
     OT-108.17 added today for M06 Malice & Enmity, M15 Knowing & Understanding and the others.
3. **A held statement becomes a comment, not an item.** Map's held statements go into a comment
   on the strand's escalation. A later strand's Context cannot match a comment.
4. **No way to create an item from inside the tool.** `held` needs an item that already exists, so
   the reader has to leave the step, raise the item, and come back.

## 3. Design options

**A. Items made part of the strand's lifecycle (recommended).**
1. **Read in.** Context reuses `escalation.match_threads`, so matching is the same as Match:
   exact code or zero-padded base, and every cluster of the strand's words. It records each matched
   item against the strand in a new table, `reading_strand_item`, as an item to answer.
2. **Create on discovery.**
   - Record, Map and Derive can each name a new item (`kind:value :: note`). The tool adds it to
     the strand's thread in the same call: an item is added through the existing thread code, and
     the strand's thread is raised on first use.
   - A Map statement held as `item` becomes a thread item, not a comment.
   - Derive's `held` can name a new item instead of an existing one.
3. **Answer and settle.**
   - Each matched item gets a response before close: touched, closed, forward, narrowed or note.
     The response goes through the existing thread-response path, so it lands in the thread's
     history.
   - Account lists every matched item with its response.
   - The close gate refuses while any matched item has no response since the strand opened.
4. **Tests on a copy (rule 97).** Changes would go to `strandreading.py`, the handler and
   `Strand-Reading.ps1`, plus a migration for the table and a gate check kind.
   Records: BUILD.md, USER-GUIDE.md and GOVERNANCE.md.

**B. Shown, not gated.** Same as A, parts 1 and 2. Account lists the matched items and any response,
but the close gate does not refuse. This is lighter, but it leaves gap 1 to discipline. That has
not held before (#2172 itself: readings did not reliably reach the narrative and the claims
register).

**C. Leave as built.** The reader raises and answers items by hand through `Escalation.ps1`. Gaps 1
to 4 stay.

I recommend A. It is the only option where the record shows that each item was taken into
account, and where nothing closes while an item is untouched.

## 4. Effect on #2172 catch-up

Catch-up B (the October ledgers imported as observations) does not depend on this. It reads
nothing, and its observations stay at `draft` until step C. A strand closing through the gate would
depend on it. So would the redo (F) when the study re-opens.
