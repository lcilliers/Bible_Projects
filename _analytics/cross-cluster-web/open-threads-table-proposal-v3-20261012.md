# Open threads register: carrying it in the escalation table (proposal, v3)

**Date:** 2026-10-12 · **Escalation:** #2000 (supersedes #1999) · **Supersedes:** `archive/open-threads-table-proposal-v2-20261012.md` · **Status:** approved (round 6) and **built 2026-10-12** in a Developer Mode session: `iba/app/BUILD.md` §336, `iba/app/GOVERNANCE.md` §93. Imported as #2002–#2103. Test plan: `iba/docs/2000-open-threads-test-plan-v1-20261012.md` (to run in a standard session).

**Researcher, verbatim:** *"should we not extend escalations, it seems that escalation and open items register are close to each other, and escalation has all the controls already built in."* and *"adopt open register into escalation. propose the changes in a md."*

**Import preview (for review before anything is imported):**
- `_analytics/cross-cluster-web/escalation-2000-open-threads-register-import-preview-v1-20261012.json`: the 100 escalation rows, with each one's item rows
- built by `escalation-2000-open-threads-import-preview-v1-20261012.py`, which is read-only
- the threads rebuilt from closed escalations come from `escalation-2000-rebuilt-threads-v1-20261012.json`

---

## 0. Round 1 rulings (researcher, chat 2026-10-12, verbatim)

1. *"Add a new type as Thread … build the config rules for the type thread to control the behaviour of the threads. One of these rules should be that open threads must be read before commencing with a task or issue, to determine if any threads relate to the task or issue escalation. This is mechanism to re-direct Rule 4 to include threads with match to cluster/strong/verse."*
2. *"Adjust the new escalation create to default to raised, but allow for asigning the status on create to on-hold or in progress. Threads can be created to on-hold, however, when a thread is identified as relevant to a open escalation (e.g. 1) above) then the thread must always change from on-hold to in progress."*
3. *"decision type - I am ok if threads are assigned as self-correctable."*
4. *"the thread title limit to 60 MUST be maintained. There are ample place in the comment and context for long text. The title is meant for easy identification of the thread."*
5. *"what is module blocking about - this sounds like a rule that I am not aware of."* Answered in §2.1.
6. *"session start will check all the on-hold threads and change them to in progress if an existing open task or issue escalation reference them. Open threads should be a easy query on -action thread only."*
7. *"completion of a thread is achieved by moving the thread to approved. Partial completion of a thread will move the thread back to on-hold. al individual completions are recorded in the additional table."*
8. *"any additional notes, or comments on the thread is captured through history."*

On the §9 decisions:
- *"1 - approve new thread type, columns and table, with taking the above modification into account"*
- *"2) closure of individual items on additional table level. do not split threads."*
- *"3) agree (add the escalation number in the file reference as per standing file naming conventions for escalations"*
- *"4) option (a)"*
- *"5) re-build threads from closed escalations only if the have open items to be resolved."*
- *"I would like to see a json for the new entries in the escalation, and the associated new table entries for each escalation before it is imported into the current table."*

**Round 2 (chat 2026-10-12, verbatim):**
- *"Q1 in-progress only. This implies that a escalation can be closed without resolving all its threads, which is intended"*. T5 and T6 are changed (§4).
- *"Q2 approve all three only if there are open threads registered for the incomplete items in these escalations"*. Each candidate was checked, with the outcome in §6:
  - #1930: rebuilt.
  - #1898: rebuilt, narrowed to its one incomplete item.
  - #1888: not rebuilt, because nothing is left open.
- *"Q3 correct."* The open thread-like tasks stay tasks.
- *"I do not see the json for the open register."* The preview is renamed so that its name says it is the register: `escalation-2000-open-threads-register-import-preview-v1-20261012.json`.

**Round 5 (chat 2026-10-12, verbatim):** *"approve Q5 and Q6, regenerate the json with responses"*
- §3.3 (the response table) and §3.4 (item references) are approved.
- The JSON is regenerated. Every item now carries `item_no`, `ref`, `opened_at`, `opened_by` and a `responses` list. The item row no longer has closing columns.
- There are 50 responses:
  - 48 `closed`, one for each item already closed
  - 2 `forward`: OT-16.1 forwards Eze 19:14 to M03, adding OT-16.2 and OT-16.3; OT-98's M72 item forwards Gen 31:29 to M58
- Where the status cell gives no date, the closure takes the closing escalation's answered date. Those rows are on the review list.

---

## 1. Facts, measured 2026-10-12

**The register.** 100 rows. The preview reads them as 84 open, 7 touched and 9 resolved or closed. (The handoff's 84 / 5 / 11 counted the status words differently.)
- OT-10 is struck through as resolved, but its status cell still begins "open". The preview treats it as resolved and puts it on the review list.

**Items.** The preview lifts **278 item rows** from the register:

| Kind | Rows |
|---|---|
| cluster | 148 |
| verse | 73 |
| strong | 31 |
| escalation | 11 |
| researcher | 7 |
| strand | 4 |
| chapter | 3 |
| event | 1 |

- 48 of the item rows are already closed.
- 87 threads match by pattern. 13 needed their items set by hand (§6).

**Live escalations: 11**, all type `task`.

---

## 2. How today's escalation rules meet threads

### 2.1 Module blocking (ruling 5: what it is)

`cfg_escalation` row 3, `module_blocking`, built under #646 (2026-08-17) and corrected under #746. It is enforced in `iba/app/run.py`, `run_step()`, as the third gate before a step runs.

It covers only the IBA app's own pipeline modules and steps, the ones registered in `cfg_utility` and `cfg_step`. When code (a validation or quality check) raises an escalation against a module or step, that module or step is refused while the escalation is at `raised` or `re-assigned`. The point is that a module with an unanswered error cannot be run again on top of it.

It never touches study work. Every escalation raised by you or by Claude in chat has `source` = researcher or Claude, which no module carries.

**Its bearing here:** ruling 2 lets an escalation be created at `on-hold` or `in-progress`. If code-raised escalations could do the same, they would skip `raised` and the gate would never fire. **So the choice of state at create is offered on the manual Raise (`Escalation.ps1 -Action Raise`) only. The code path (`raise_()` in `lib/escalation.py`) keeps `raised`.**

### 2.2 The clashes, as now ruled

| # | Live rule | Ruling | Change |
|---|---|---|---|
| C1 | `cfg_escalation` 4 `resolution_precedence`: open items assigned to Claude come before other work | Ruling 1: redirect it, so threads count only where they match the task or issue | Rule 4 is amended. A thread counts under it only while it is `in-progress`, that is, while it matches an open task or issue (§4, rules T1 and T5). An `on-hold` thread is never "work first". |
| C2 | Raise always lands at `raised`; D26 then forbids content until the item moves | Ruling 2 | Raise defaults to `raised`. A manual Raise may set `-State on-hold` or `-State in-progress`, for every type. A thread is normally raised at `on-hold`. |
| C3 | `resolution_kind` required at Raise | Ruling 3 | Every thread is `self_correctable`. Claude closes it, through `approved`, when all its items are closed (T6). |
| C4 | Title check: one line, 60 characters or fewer, no "--" | Ruling 4 | It is kept as it stands. 84 register titles run over 60 characters. The preview gives every thread a title of 60 characters or fewer, and the long text stays whole in `comment`. |
| C5 | `module_blocking` | §2.1 | The choice of state at create is for manual Raise only. |
| C6 | Session start reads List, and step 4B names a non-existent `OpenThreads.ps1` | Ruling 6 | Session start runs the thread check (T5). Open threads are listed with `-Action Thread`. Step 4B is already corrected to `Escalation.ps1`. |

---

## 3. Changes to the tables

### 3.1 The `escalation` table, and `escalation_history`, which mirrors it

Two new columns:

| Column | Holds |
|---|---|
| `alias` | `OT-nn` for threads; empty for other types. It has a unique index where set. New threads take the next OT number. |
| `comes_back_when` | the "comes back when" text, whole, as a person reads it |

Field mapping (as in the preview):

| Register | Escalation field |
|---|---|
| id | `alias` |
| title (written to 60 characters or fewer) | `short_description` |
| thread cell, whole | `comment` |
| raised | `raised_at` (the date); the cell goes whole into `context.raised_in` |
| comes back when | `comes_back_when`, plus item rows |
| files named in the row | `context.files`, as full repo-relative paths (`cfg_escalation` 7) |
| status cell, for open or touched rows | `tried`, headed *History before migration* (decision 4, option a) |
| status cell, for resolved rows | `resolution`, with `next_action` = approved and `state` = completed |
| (none) | `type` = thread, `resolution_kind` = self_correctable, `next_action_assigned_to` = Claude, `source` and `originator` = Researcher where the register says the researcher raised it, otherwise Claude |

From the migration on, every note or comment on a thread is an Update, so it lands in `escalation_history` (ruling 8).

### 3.2 The item table: `escalation_thread_item`

v3's first draft named this table `escalation_trigger`. Because it also records each completion (ruling 7), it is renamed `escalation_thread_item`.

| Column | Holds |
|---|---|
| `id` | key |
| `escalation_id` | the thread |
| `kind` | `cluster` · `strong` · `verse` · `strand` · `chapter` · `event` · `researcher` · `escalation` (`cfg_enum` `escalation_thread_item_kind`) |
| `value` | e.g. `M72`, `M10c`, `H5782`, `Rom 7:15-21`, `10.13`, `#1993` |
| `status` | `open` or `closed` |
| `note` | what this item asks for (e.g. "7 verses", "Eze 19:14 forward to M03") |
| `opened_at`, `opened_by` | when, and under which escalation, it was added |
| `closed_at`, `closed_by`, `closed_note` | the individual completion: when, under which escalation, and what was done |

**Kind `escalation`** is how a task or issue references a thread (ruling 6). When the thread check (T1) finds a match, an item `#nnnn` is added to the thread. The item closes when that task or issue reaches a terminal state.

### 3.3 Responses at item level (round 3; approved round 5)

**Researcher, chat 2026-10-12, verbatim:** *"looking at the json, I can see a diversity of responses, most of the responses will be at item level. how will these responses be captured?"*

**The gap.** As drafted, an item row holds only its current status and one closing note. Every other response would land in the thread's history, with no tie to the item it answers. The register already shows the kinds of response an item gets, and how many each item can collect:

| Kind | Example from the register |
|---|---|
| touched | evidence added by a strand, e.g. OT-02 by unit 2 (#1939) and unit 4 (#1949) |
| narrowed | the scope cut down by a ruling, e.g. OT-16's M72 verses, from 23 to 4 (#1998) |
| forward | a verse sent on to another cluster, e.g. OT-16's Eze 19:14 to M03 |
| ruling | the researcher's decision, quoted verbatim |
| closed | an individual completion |
| reopened | a closed item that comes back into play |

**Proposed: one more table, `escalation_thread_item_response`.** Each response is a row. Nothing is overwritten.

| Column | Holds |
|---|---|
| `id` | key |
| `item_id` | the item answered |
| `escalation_id` | the thread (repeated, for easy querying) |
| `kind` | touched · narrowed · forward · ruling · note · closed · reopened (`cfg_enum` `escalation_thread_item_response_kind`) |
| `text` | the response. A researcher's response is quoted verbatim (`cfg_escalation` 5). |
| `via_escalation` | the task or issue whose work gave the response, e.g. #1998 |
| `responded_by` | Claude or Researcher |
| `responded_at` | date and time |
| `files` | full repo-relative paths (`cfg_escalation` 7) |

**How the pieces work together:**
- **The item row keeps only the current state** (open or closed). Its `closed_at`, `closed_by` and `closed_note` columns are dropped. A closure is a `closed` response, so every completion is in one place, as ruling 7 asks.
- **A `forward` response adds a new item** to the same thread. For example, Eze 19:14 forward to M03 adds `cluster:M03`. So the forward mark can itself be matched later (T1).
- **Thread history still gets a version for every Update** (ruling 8), with a one-line summary such as "OT-16: M72 item closed; M03 item added". So the thread's history stays readable as a timeline. The detail is in the response rows.
- **One front door:** `Escalation.ps1 -Action Update -Id OT-16 -Item cluster:M72 -Respond "…" -ResponseKind closed -Via 1998`. Several items can be answered in one call by repeating `-Item`, all sharing one `-Via`.
- **Reading back:** `-Action Thread -Id OT-16` shows each item with its responses in date order. The generated register shows, for each item, its latest response.

**Your responses, in practice.** As now, you answer in chat and Claude records the answer verbatim, against the item, in the same turn (`cfg_escalation` 5, chat routing). If you would rather enter them yourself, the escalation actions worksheet (`open-excel-tools`) could gain an items sheet. That is a separate choice, and is not proposed here.

**Effect on the migration (decision 4 stays option a).**
- The register's status cells stay whole in the thread's `tried`, as *History before migration*. They are **not** split into responses, because their dates and ledger ids are not uniform.
- Each item that is already closed gets one `closed` response, taken from the status cell. That is 48 rows, including the M72 items of OT-16 and OT-98 (#1998). Those two also get a `forward` response, for Eze 19:14 to M03 and Gen 31:29 to M58.
- The preview JSON gains a `responses` list under each item. This is shown before import, like the rest.

### 3.4 Item references, for responses in chat (round 4; approved round 5)

**Researcher, chat 2026-10-12, verbatim:** *"if I write the responses in chat - what references will I need to use to allow you to get back to the correct line items."*

**Each item gets a short reference: `{thread}.{n}`**, for example `OT-16.1` for the M72 item of OT-16.
- The number is the item's place in its thread, stored as an `item_no` column on `escalation_thread_item`.
- It is never renumbered. A new item (including one added by a `forward` response) takes the next number.
- The reference is shown wherever items are shown: the preview JSON (`ref`), `-Action Thread`, and the generated register.

**Two other ways to refer, both accepted:**
- **By value:** `OT-16 M72`, or `OT-01 Eze 20:11`. The preview has no value repeated within a thread (checked), so this is unambiguous. Strand, researcher and event items have long values, so use the number for those.
- **The thread alone:** `OT-16`, for a response about the whole thread. It goes to the thread's history.

**The kind of response** is read from your words: close, forward to M58, narrowed, ruling, note, reopen. Where it is unclear, Claude asks before recording.

**Rebuilt threads take the next OT numbers now:** OT-101 is the style guide v3, and OT-102 is the Num 11:15 pointer. So they can be referred to before import.

**Example message:**
```
OT-16.2 close: Eze 19:14 read with M03, no anger in the verse
OT-97 M12 note: hold until the righteousness strand
OT-102 ruling: ...
```

---

## 4. Config rules for the `thread` type

All of these go through `Config-Maintenance.ps1 -Step Propose`, before any code.

| Rule | What it says | Where it lives |
|---|---|---|
| **T0** type | `thread` is added to `cfg_enum` `escalation_type`; the item kinds go into a new `cfg_enum` | `cfg_enum` |
| **T1** thread check before work | Before a task or issue is started (moved to `in-progress`), and when one is raised, its clusters, Strong's numbers and verses are matched against the items of every thread not completed. Each match adds an `escalation` item `#nnnn` to the thread. This is rule 4 redirected (ruling 1). | new `cfg_escalation` row; `Escalation.ps1 -Action Match -For nnnn` |
| **T2** state at create | Raise defaults to `raised`. A manual Raise may choose `on-hold` or `in-progress`. Code-raised items stay `raised` (§2.1). | new `cfg_escalation` row; `Escalation.ps1 -State` on Raise |
| **T3** a matched thread moves | When a thread gains an open `escalation` item, it moves from `on-hold` to `in-progress`, always (ruling 2). | new `cfg_escalation_transition` row |
| **T4** self-correctable | Every thread is raised `self_correctable` (ruling 3). | new `cfg_escalation_requirement` row (Raise, type thread) |
| **T5** session start | Session start checks every `on-hold` thread. If a task or issue **at state `in-progress`** references it (an open `escalation` item), the thread moves to `in-progress` (ruling 6; round 2, *"in-progress only"*). A reference from a raised or on-hold task waits until that task is started. Rule 4 then applies to `in-progress` threads only. | `.claude/commands/start-project.md` step 4B; `cfg_escalation` 4 amended |
| **T6** completion | A thread is completed by moving it to `approved`, which lands at `completed`, with a resolution. This needs every item closed. Closing items while others stay open is a partial completion, and the thread returns to `on-hold`. Each individual completion is recorded on its item row (ruling 7). **A task or issue can close without resolving its threads** (round 2: *"which is intended"*). When it closes, its `escalation` item on each thread closes, with a note of what that work settled. A thread with other items still open returns to `on-hold`. | new `cfg_escalation_requirement` check kind `no_open_thread_items`; new `cfg_escalation_transition` row |
| **T7** at least one item | A thread cannot be raised without at least one item. | `cfg_escalation_requirement` (check kind `exists`) |
| **T8** notes through history | Notes and comments on a thread are Updates, never edits to the register file (ruling 8). | `cfg_behaviour_rule` `open-threads-carried-as-escalations` |
| **T9** title | The 60-character title check applies unchanged (ruling 4). | existing (#759) |

`cfg_behaviour_rule` `open-threads-carried-as-escalations` restates the register's rule of use: a thread is not worked as a task, it moves only when a strand reaches it, and new held items are raised as threads at ledger approval. It replaces the "How it is used" block at the head of the `.md`.

---

## 5. Changes to `Escalation.ps1` and `lib/escalation.py`

| Change | Detail |
|---|---|
| `-Type thread` | Raise takes `-ComesBackWhen` and one or more `-Item kind:value[:note]`. The alias is assigned automatically. |
| `-State` on Raise | `on-hold` or `in-progress` (T2), on manual Raise only |
| `-Id OT-16` | Every action that takes `-Id` also accepts the alias. |
| **`-Action Thread`** | Lists the open threads (`on-hold` and `in-progress`): alias, escalation id, title, the open items. `-State in-progress` narrows it (ruling 6). |
| `-Action Match` | `-Cluster` / `-Strong` / `-Verse`, with `-For nnnn` to record the match on the thread (T1, T3). A cluster matches its sub-codes (M10 ↔ M10c). A Strong's number matches its exact code, then its base, zero-padded. A verse matches inside a range, and a chapter item. |
| Item upkeep on Update | `-AddItem kind:value[:note]` and `-CloseItem kind:value -Note "…"`. Each lands as a history version. T6 then sets the thread's state. |
| List report | Threads get a short section: counts by state, then the `in-progress` threads only. |
| Register export | `-Action Export -Type thread` writes `open-threads-register.md` at the same path, marked as generated. Each row shows the alias with its escalation number, e.g. `OT-16 · #2016` (decision 3). Session-close regenerates it. |

The records scripts that edit the `.md` by splitting rows on " | " are retired for threads.

**File naming (decision 3).** No written `cfg_*` rule for naming files after an escalation was found. The standing practice in the repo is `escalation-NNNN-{description}-vN-YYYYMMDD` (e.g. `iba/app/docs/escalation-304-orphan-justification-review-v1-20260723.md`). The preview files for this work follow it. The register keeps its path, and its rows carry the escalation number.

---

## 6. The import preview (decision: see it before import)

The JSON gives, per thread:
- `escalation`: every field of the new row; the id is assigned at import
- `items`: every item row, each with its source (comes back when, set by hand, thread text, or status cell)
- `session_start_effect`: whether T5 moves the thread to `in-progress` at the first session start
- `review_notes`

**The review list: 12 rows.**
- **No date in "raised":** OT-03, 04, 05, 07 ("candidate v2 §7" and similar). They take the register's set-up date, 2026-10-02, which is the date of candidate v2.
- **Items set by hand, matched only by strand, chapter, researcher or escalation:** OT-03, 06, 08, 10, 12, 13, 14.
- **OT-10:** struck through, but the status cell begins "open". Imported as completed.
- **Partial closures:** OT-16 and OT-98 have their M72 item closed (#1998). What stays open is taken from the status cell:
  - OT-16: Eze 19:14, forward to M03
  - OT-98: Gen 31:29, forward to M58

**At the first session start, T5 moves one thread to `in-progress`:** OT-09, by #1993 (in-progress, M18).

OT-05 (through #1891, on-hold) and OT-14 (through #1944 to #1947, raised) keep their reference items. They wait until those tasks are started.

**Threads rebuilt from closed escalations (decision 5; round 2).** 22 closed study escalations from #1880 on were read, where the text says an item was held, deferred, carried forward or left open. The earlier closed escalations are IBA app build items, not study threads. A thread is rebuilt only where an item is still incomplete and no open thread carries it. It then registers one open item for each incomplete point.

| From | Outcome | Checked against |
|---|---|---|
| #1930 | **Rebuilt:** *Narrative style guide v3* | `cfg_setting narrative.inner_being_style_guide_path` still points to v2, and no v3 file exists. No thread carries it. |
| #1898 | **Rebuilt, narrowed:** *Num 11:15: Moses asks to die, a pointer for ruling*. Items: Num 11:15, M25, M02, M47. | The other points are AN-H2 in the 1 Oct anger ledger, ruled status quo on 2026-09-30, and Rom 13:5 is also in OT-07. Num 11:15 is not in AN-H2. The recovery data (U2 L1747) still says "Still for ruling (carried to #1897)". #1897 closed without ruling it, and the narrative does not cite the verse. |
| #1888 | **Not rebuilt** | The Batch A clarification is AN-H1, withdrawn by the researcher on 2026-10-01. Nothing is left open. |

The other 19 are listed in the JSON, with the reason each was not rebuilt. One of them, #1880's Batch A–H delta (155 M47 pairs), is marked for review: no escalation records it as done.

---

## 7. Migration (after you approve the preview)

1. Back up iba.db. Freeze the current `.md` as `archive/open-threads-register-frozen-20261012.md`.
2. Config (§4), then the schema (§3), then the code (§5), each tested (§8).
3. Import from the approved JSON. Check the counts: 100 threads plus 2 rebuilt, and 278 items plus 6.
4. Export the register, and compare it with the frozen copy row by row.
5. Run session start once, and check that only OT-09 moves to `in-progress`.

## 8. Build order and tests (developer mode; a checkpoint after each step)

| Step | Build | Test |
|---|---|---|
| 1 | Config T0 to T8 | `cfg_*` read-back |
| 2 | Schema: two columns on both tables; `escalation_thread_item` | Applied on a copy; history mirrors the new columns |
| 3 | Raise: state at create (T2), thread with items (T4, T7) | A thread with no item is refused. A code raise stays `raised`. A manual raise at `on-hold` passes D26. |
| 4 | Match and the transitions (T1, T3, T6) | A match moves `on-hold` to `in-progress`. Closing one of two items returns the thread to `on-hold`. Approving with an item open is refused. Approving with all closed reaches `completed`. M10 finds OT-70. |
| 5 | `-Action Thread`, List section, Export | An export of a test set equals the input. |
| 6 | Rule 4 and session start (T5) | Only `in-progress` threads appear as work first. |
| 7 | Import (§7) | As in §7 |
| 8 | GOVERNANCE.md section, BUILD.md, USER-GUIDE.md, session-close | One full session start and close on the new path |

---

## 9. Still for your decision

- Q1 to Q3 are answered (§0, round 2).
- Q5 and Q6 are approved (round 5).
- **Q4. The preview itself:** titles, items, and the review list (§6). **Once you approve it, the build starts in developer mode (§8). The import comes last, from the approved JSON.**

## 10. The researcher's further suggestions

Round 1 is in §0. Further rounds are added there, in place, until approval.
