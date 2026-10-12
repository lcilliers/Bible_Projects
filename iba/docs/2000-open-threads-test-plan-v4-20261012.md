# #2000 Open threads in the escalation table: test plan (results)

**Escalation:** #2000 · **Date:** 2026-10-12 · **Rule:** `cfg_behaviour_rule` 46 `test-plan-per-module-utility`
**Design:** `_analytics/cross-cluster-web/open-threads-table-proposal-v3-20261012.md` (§8 tests) · **Build:** `iba/app/BUILD.md` §336
**Supersedes:** v3, now in `archive/` with v1 and v2. Sections 1 to 8 are v2's results, unchanged. Section 9 (v3) retests the D1 fix (`BUILD.md` §337). Section 10 (v4) tests the thread lifecycle (`BUILD.md` §338). Sections 9 and 10 have blank results.

**Run:** 2026-10-12, standard (App Mode) session, on the researcher's instruction (*"can you run the test plan"*). Write cases ran on scratch copies of iba.db made with the SQLite backup API (session scratchpad, not in the repo), driven by two temp_ harness scripts. PS-level cases ran on live data, read-only or refused only. The exceptions are listed under "Live writes during the run".

## Outcome

**Every case passes except one defect (D1), found outside the listed cases and reproduced on a copy. Two cases (6.3, 8) wait for this session's `/session-close`.**

- **D1, a thread is stranded by a plain reassignment.** `Update -Id OT-nn -AssignedTo X`, with no `-State` and no item change, moves the thread to `re-assigned`. That state is outside `_THREAD_OPEN_STATES` (on-hold, in-progress), so the thread drops out of `-Action Thread`, `Match` and `ThreadCheck`, and it shows in the List counts as "re-assigned 1". The `update/state` thread requirement only checks completed/closed (T6), so nothing refuses it. Found live: OT-09 was reassigned to the researcher at session start (in answer to the stop hook) and vanished from the thread listing (5.1, 5.2). Reproduced on a copy: thread in-progress → `-AssignedTo Researcher` → `re-assigned`, and Match no longer finds it. **The fix is a design choice and is not made here.** Either a reassignment keeps a thread's state (the transition skips the `re-assigned` row for type thread), or a requirement refuses any state outside on-hold/in-progress/completed for a thread. Decision for the researcher, on #2000.
- **Out of scope, noted only:** `find_ps_worksheet_drift` reports drift on five non-escalation scripts (Copy-NarrativeToLearning4Comfort, Purge-SoftDeletes, RelationalReading, Run-Stage1Batch, VerseReading). None of it is from #2000; the escalation worksheet check (2.5) is clean.

### Live writes during the run

- OT-09 (#2010): v2 (ThreadCheck at session start, → in-progress), v3 (reassigned to the Researcher → `re-assigned`, which is D1), v4 (state restored to in-progress with a comment; it stays with the Researcher for OT-09.3).
- `Escalation.ps1 -Action Export -Type thread` regenerated `_analytics/cross-cluster-web/open-threads-register.md` (v4-20261012).
- Thread, history and list reports were written to `outputs/escalation/` (the normal output of those actions).
- No escalation was raised by any refused or usage-error call: max id 2105 and 1,378 rows before and after section 5.

---

## 1. Config (build step 1)

| # | Check | Expected | Result |
|---|---|---|---|
| 1.1 | `cfg_enum` read-back | `escalation_type` has `thread`. `escalation_thread_item_kind` has 8 values, `_status` 2, `_response_kind` 7, `escalation_raise_state` 3. `escalation_requirement_check_kind` has `no_open_thread_items` and `must_be_self_correctable` | **Pass.** type has thread; kind 8 (cluster, strong, verse, strand, chapter, event, researcher, escalation); status 2; response_kind 7; raise_state 3 (raised, on-hold, in-progress); check_kind has both |
| 1.2 | `cfg_escalation` | row 4 text names threads/T5. New rows: `thread_check_before_work`, `raise_state_choice`, `thread_completion` | **Pass.** Row 4 `resolution_precedence` names type thread / T5; rows 16, 17, 18 present and active |
| 1.3 | `cfg_escalation_transition` | 2 rows at shape=manual priority 0, with condition keys `thread_items_changed_and_referenced` and `thread_items_changed_partly_closed` | **Pass** |
| 1.4 | `cfg_escalation_requirement` | 4 rows with condition `thread_type` (raise/items, raise/resolution_kind, update/state, resolve_self_correctable/state) | **Pass**, all 4 active. See D1: update/state covers completed/closed only |
| 1.5 | `cfg_behaviour_rule` 74 | `open-threads-carried-as-escalations`, active. Rule 43's exception (2) names Match/ThreadCheck | **Pass.** Rule 74 active (`partially_enforced`); rule 43 (2) lists Match/ThreadCheck |
| 1.6 | `Config-Maintenance.ps1 -Step Validate` (or `cfgquality.find_unregistered_tables_and_columns`) | 0 unregistered tables or columns | **Pass**, 0 (run through `cfgquality` directly, read-only) |

## 2. Schema (build step 2)

| # | Check | Expected | Result |
|---|---|---|---|
| 2.1 | `PRAGMA table_info` on escalation and escalation_history | `alias` and `comes_back_when` on both | **Pass** |
| 2.2 | Unique alias | Setting a second row's alias to an existing `OT-nn` fails on `idx_escalation_alias`. Two NULL aliases are fine | **Pass.** "UNIQUE constraint failed: escalation.alias"; 1,276 NULL aliases coexist |
| 2.3 | History mirrors | After an Update with `comes_back_when`, the new history row carries it. `alias` appears in v1 only | **Pass.** v1 alias=OT-103, cbw None; v2 alias None, cbw "when M90 is read" |
| 2.4 | Config rebuilds the tables (`lib/db.py:table_ddl()` for both new tables) | escalation_thread_item: inline `UNIQUE (escalation_id, item_no)` + 2 indexes; _response: 3 indexes; index names identical to the live ones (`idx_{table}_{col}`) | **Pass.** Inline UNIQUE present on the item table; index names generated = live (item: escalation_id, opened_by; response: escalation_id, item_id, via_escalation). The generated DDL quotes the names; the live names are the same unquoted |
| 2.5 | `find_escalation_worksheet_drift` | No finding | **Pass**, `[]` |

## 3. Raise (build step 3: T2, T4, T7)

| # | Case | Expected | Result |
|---|---|---|---|
| 3.1 | Thread with no item | Refused (T7 message); nothing written | **Pass.** "a thread needs at least one item at Raise … rule T7" |
| 3.2 | Thread with `resolution_kind='decision_required'` | Refused (T4) | **Pass.** "a thread is raised self_correctable … rule T4" |
| 3.3 | Thread, 2 items, no state | Lands on-hold. `next_action` NULL; assigned to Claude. Alias = next OT number (OT-103 on a copy with 102). Items numbered 1 and 2 | **Pass.** on-hold, next_action None, Claude, OT-103, items [1, 2] |
| 3.4 | Thread with `state='raised'` | Refused | **Pass.** "never 'raised' (cfg_escalation raise_state_choice)" |
| 3.5 | Thread with `state='in-progress'` | Lands in-progress | **Pass** |
| 3.6 | Task with `state='on-hold'` | Lands on-hold, `next_action='review'`. The comment is accepted | **Pass** |
| 3.7 | Task with `state='closed'` | Refused | **Pass.** "'closed' is not a member of cfg_enum 'escalation_raise_state'" |
| 3.8 | Task with `items` | Refused ("for type thread only") | **Pass** |
| 3.9 | Code raise `raise_()` | Still lands `raised` | **Pass** |
| 3.10 | Item spec `verse:Rom 7:15-21 :: 7 verses` | kind=verse, value=`Rom 7:15-21`, note=`7 verses` | **Pass** |
| 3.11 | Duplicate item on the same thread | Refused, naming the existing item number | **Pass.** "already exists on #2110 as item 1 (open)" |
| 3.12 | Title of 61 characters | Refused (T9) | **Pass.** "61 chars, over the 60-char title limit" |

## 4. Match and transitions (build step 4: T1, T3, T5, T6)

Test thread T (OT-106) with items `cluster:M10`, `strong:H7067`, `verse:Rom 7:15-21`, `strong:H0530`; T2 (OT-107) with `strong:H7067G`; task A raised, task B in-progress. A `-For` match writes to every matching thread, so the live M10/M11 threads on the copy (OT-24, OT-43, OT-70) also took items; that is the designed behaviour.

| # | Case | Expected | Result |
|---|---|---|---|
| 4.1 | Match `-Cluster M10c`, no `-For` | Thread listed; nothing written | **Pass.** Listed; history unchanged |
| 4.2 | Match `-Cluster M1` | Not matched | **Pass** |
| 4.3 | `-Strong H7067G` vs item H7067; `-Strong H7067H` vs item `H7067G` | First matches; second does not | **Pass** |
| 4.4 | `-Strong H530` vs item `H0530` | Matches | **Pass** |
| 4.5 | `-Verse "Rom 7:18"`, `"Rom 7"`, `"Rom 8:1"` | First two match; third does not | **Pass** |
| 4.6 | M10 finds OT-70 | OT-70 listed | **Pass** |
| 4.7 | Match `-For A` (A raised) | Item added; thread stays on-hold; one history version | **Pass.** Item OT-106.5 #A; on-hold; history +1 |
| 4.8 | Match `-For B` (B in-progress) | Item added; on-hold → in-progress | **Pass** |
| 4.9 | Match `-For B` again | "already referenced"; nothing written | **Pass.** "already referenced (item 6)"; history +0 |
| 4.10 | Move A to in-progress | Every on-hold thread referencing A moves to in-progress; message lists it | **Pass.** The test thread referencing only A moved on-hold → in-progress, listed in the message |
| 4.11 | Close B (`ResolveSelfCorrectable`) | B's item closes with a `closed` response citing B's resolution. If no other in-progress work references the thread and items remain, on-hold (T6) | **Pass.** Item closed, response "#B reached completed: B done in test". On T (still referenced by in-progress A) the thread stays in-progress, correctly. **Extra case 4.11b:** a thread referenced only by in-progress B2; B2 resolved → thread on-hold, its #B2 item closed, the others open |
| 4.12 | Close item 1 of two | Item 1 closed; thread on-hold | **Pass** |
| 4.13 | Approve with an item open | Refused (T6, open count); rolled back | **Pass.** "(1 open item(s) on #2116)" |
| 4.14 | Close the last item, then approve | completed | **Pass** |
| 4.15 | Close the last item and approve in one call | completed | **Pass** |
| 4.16 | `ResolveSelfCorrectable` on a thread with open items | Refused (T6) | **Pass** |
| 4.17 | `forward` without `-AddItem` | Refused | **Pass** |
| 4.18 | `forward -AddItem cluster:M03 -Via 1998` | Forward response; new item next number, `opened_by=1998` | **Pass.** item 2, opened_by 1998 |
| 4.19 | `reopened` on a closed item | Item open again; response row | **Pass** |
| 4.20 | `closed` on an already-closed item | Refused | **Pass.** "is already closed" |
| 4.21 | `-Item OT-16.1` against OT-17 | Refused ("does not belong") | **Pass** |
| 4.22 | `-Item M72`, `cluster:M72`, `1` on OT-16 | Same item | **Pass.** All resolve to item id 61 |
| 4.23 | `-Item … -Respond …`, no `-ResponseKind` | Refused | **Pass** |
| 4.24 | `-Item` on a task | Refused | **Pass** |
| 4.25 | `ThreadCheck` on the import (fresh live copy) | Only OT-09 moves to in-progress (through #1993) | **Pass.** First live run at session start: "1 thread change: OT-09 (#2010) -> in-progress". On a copy taken after D1 (OT-09 at `re-assigned`) nothing moved; with OT-09 set back to on-hold on that copy, the first run moved only OT-09 |
| 4.26 | `ThreadCheck` run twice | Second run changes nothing | **Pass**, `[]` |

## 5. Views (build step 5)

| # | Case | Expected | Result |
|---|---|---|---|
| 5.1 | `-Action Thread` | Every on-hold and in-progress thread with its open items; console lines; report | **Pass**, with D1 visible: OT-09 was missing while at `re-assigned`; after v4 it lists |
| 5.2 | `-Action Thread -State in-progress` | In-progress threads only | **Pass.** Empty while OT-09 sat at `re-assigned` (D1); after v4: OT-09 only |
| 5.3 | `-Action Thread -State completed` | Clean usage error; no run_error escalation | **Pass.** "usage error, not recorded as an escalation"; max id unchanged |
| 5.4 | `-Action Thread -Id OT-16` | OT-16.1 closed, `closed` then `forward` in date order; OT-16.2, OT-16.3 open | **Pass** (report `2017-escalation-threads-v1-20261012.md`) |
| 5.5 | `-Action Thread -Id OT-999` | Clean usage error; no escalation raised | **Pass** |
| 5.6 | `-Action History -Id OT-16` | Deep history for #2017 | **Pass** (`2017-escalation-history-v1-20261012.md`) |
| 5.7 | `-Action List` | No thread in the per-item body or "Recently resolved"; "Open threads" shows counts by state and in-progress threads only | **Pass.** 0 thread rows in the body; counts "completed 9, on-hold 92, re-assigned 1" (the 1 is D1) |
| 5.8 | Export, then the compare script against the frozen register | 100 rows equal; old status text 100 of 100; OT-101/102 extra | **Pass.** raised 100/100, comes back when 100/100, status text 100/100, OT-101/102 extra. Thread cell 99/100: OT-09 differs only by today's appended notes (the T3/T5 line and the reassignment comment); the frozen text is carried whole as its prefix |
| 5.9 | Export without `-Type thread` | Refused in PS | **Pass** |
| 5.10 | `-Id OT-16` on Update etc. | Resolves to #2017 | **Pass** at library level (`resolve_id`, 4.21/4.22). The PS Update call with `-Id OT-16` reached the item check (refused as intended for a missing `-ResponseKind`), so the alias resolved |

## 6. Session start and rule 4 (build step 6)

| # | Case | Expected | Result |
|---|---|---|---|
| 6.1 | `/start-project` step 4B in full | ThreadCheck first (OT-09 moves); Thread lists; Match reads the strand; researcher-waiting threads named | **Pass** (this session's start) |
| 6.2 | Rule 4 | Only in-progress threads reported as "work first" | **Pass.** Only OT-09 was reported |
| 6.3 | `/session-close` step 6b | Register regenerated; summary line quoted | **Pending.** Step 6b is in `session-close.md`; it runs at this session's close |
| 6.4 | Stop hook | On-hold threads not listed; OT-09 listed once in-progress | **Pass.** After the ThreadCheck the hook listed exactly "#2010 (thread, in-progress/None)"; no on-hold thread. (After v4, OT-09 is assigned to the Researcher, so it is no longer Claude's backlog) |

## 7. Import (build step 7)

| # | Check | Expected | Result |
|---|---|---|---|
| 7.1 | Counts | 102 threads (#2002–#2103), 284 items, 50 responses (48 closed, 2 forward), 102 v1 history rows | **Pass**, exactly |
| 7.2 | Re-run the import script | "already imported"; nothing written | **Pass** (on a copy): "already imported (102 alias(es) present, e.g. OT-01) -- nothing written" |
| 7.3 | Completed threads | 9, none with an open item | **Pass** |
| 7.4 | OT-16, OT-98 | M72 items closed with the #1998 responses; the forward items open | **Pass.** OT-16.1 and OT-98.1 (M72) closed with closed + forward via #1998; OT-16.2–.3 and OT-98.2–.10 open |

## 8. Full cycle

One full `/start-project` and `/session-close` on the new path, in the same standard session. **Start done; close pending** (with 6.3).

## 9. D1 fix: a reassigned thread keeps its state (BUILD.md §337)

Built 2026-10-12 in a Developer Mode session; **to be run in a standard session** (CHARTER.md §4). Write cases run on a scratch copy of iba.db, as in sections 3 to 7.

| # | Case | Expected | Result |
|---|---|---|---|
| D1.1 | Config: `cfg_escalation_transition` shape manual | one active row priority 6, condition `thread_reassigned`, next_action NULL → `__unchanged__`; priority 7 `assignee_changed` unchanged | |
| D1.2 | An **on-hold** thread: `Update -Id OT-nn -AssignedTo Researcher` (no `-State`, no item change), then back to Claude | state stays on-hold both times; the thread is still listed by `-Action Thread`, found by `Match` on one of its items, and seen by `ThreadCheck` | |
| D1.3 | An **in-progress** thread (e.g. a copy of OT-09): same as D1.2 | state stays in-progress; still in Thread/Match/ThreadCheck; List shows no "re-assigned" thread | |
| D1.4 | Non-thread regression: a task with `-AssignedTo` changed alone; a thread with `-AssignedTo X -State on-hold` | the task still goes to `re-assigned` (priority 7); the thread takes the explicit state | |

**Noted, not in scope of the fix (on #2000 for the researcher):** `-NextAction ready_for_approval` (priority 5) or `approved` with needs_followup (priority 1) on a thread still resolve to `re-assigned`. Record what each does if tried on a copy; do not treat it as a failure of D1.

## 10. Thread lifecycle (BUILD.md §338)

Built 2026-10-12 in a Developer Mode session; **to be run in a standard session**. Write cases run on a scratch copy of iba.db. Review: `iba/docs/2000-thread-lifecycle-review-v1-20261012.md`. For every case, also check `-Action History -Id OT-nn`: each item response appears in the history comment with its kind, who responded and the full text (G5).

| # | Case | Expected | Result |
|---|---|---|---|
| 10.1 | Config | `cfg_enum` item status open/closed/withdrawn/superseded; response kinds include withdrawn and superseded; transition priority 0 `thread_items_all_settled` → `completed`; `cfg_status_flow` completed set_by carries `thread: every item settled`; requirement (reject, superseded_by, thread_superseding) | |
| 10.2 | Withdraw one of two open items: `-Item n -ResponseKind withdrawn -Respond "…"` | item `withdrawn`; thread → on-hold (partial, T6); history has the full text | |
| 10.3 | Supersede an item without a reference in the text | refused ("names what carries the item on"); nothing written | |
| 10.4 | Supersede an item with `-Respond "carried by OT-nn.n: …"` | item `superseded` | |
| 10.5 | Settle the last open item (closed) | thread `completed` in the same call; resolution lists every item with its status and latest response; next_action NULL | |
| 10.6 | Settle a settled item again (closed on a withdrawn item) | refused ("already withdrawn -- reopen it first") | |
| 10.7 | `-ResponseKind reopened` on a withdrawn item of an open thread | item `open` again | |
| 10.8 | Thread withdraw: `-NextAction reject -State withdraw -Comment "…"` with 2 open items | thread `withdraw`; both items `withdrawn` with the reason; history lists them | |
| 10.9 | Thread supersede without `-SupersededBy` | refused by the requirement; nothing written | |
| 10.10 | Thread supersede with `-SupersededBy` a completed thread, or itself, or a task | refused ("must be another thread" / "must be open") | |
| 10.11 | Thread supersede with `-SupersededBy OT-mm` (open), one item a duplicate of one already on OT-mm (settled), one new | old thread `supersede`; each old item `superseded by OT-mm.k`; on OT-mm the new item added with a `note`, the duplicate reopened; OT-mm history has a version naming the old thread | |
| 10.12 | `-SupersededBy` without reject/supersede, or on a task | refused | |
| 10.13 | Task linked to a thread (escalation item via Match -For): withdraw the task | its thread item `withdrawn` (not closed); text "#nnnn reached withdraw: …" | |
| 10.14 | Same, task superseded / task completed | item `superseded` / `closed` | |
| 10.15 | The task's item was the thread's last open item | thread completes via `_restate_thread`, with the generated resolution | |
| 10.16 | `-NextAction approved -Resolution "…"` on a thread with all items settled but still open (if constructed) | completed with the given resolution (unchanged path) | |
| 10.17 | Regression: a plain task Update, a decision_required approve, a non-thread reassignment | unchanged behaviour (priority 0 thread rows never fire for non-threads) | |
| 10.18 | Views: `-Action Thread -Id OT-nn` and `-Action Export -Type thread` with withdrawn/superseded items | statuses shown as stored; register regenerates | |

## 11. Config audit and corrections (BUILD.md §339)

Added 2026-10-12 (same day, same version: v4 was not yet run). To be run in a standard session.

| # | Case | Expected | Result |
|---|---|---|---|
| 11.1 | `cfg_change_detail` by run_id | `DEVMODE-2000-BACKFILL-20261012` 87 rows (81 insert, 6 update with before_json); `DEVMODE-2000-CONFIG-CORRECTIONS-20261012` 9 rows (8 update with before_json, 1 insert) | |
| 11.2 | Re-run the backfill | "already recorded -- nothing written" | |
| 11.3 | Re-run the corrections migration | every row "already current"/"present -- skipped"; no new log rows | |
| 11.4 | A `Config-Maintenance.ps1 -Step Propose` round trip on a scratch copy (propose, approve, re-run with -RunId) | applied and logged exactly as before (`apply_logged` path) | |
| 11.5 | `configmaint.validate` | no Escalation.ps1/worksheet drift; thread rows unchanged otherwise | |
| 11.6 | Worksheet rows 50–53 in Excel | the PS instruction formulas build valid commands | |

