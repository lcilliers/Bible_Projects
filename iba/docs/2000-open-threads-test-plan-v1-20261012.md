# #2000 Open threads in the escalation table: test plan

**Escalation:** #2000 · **Date:** 2026-10-12 · **Rule:** `cfg_behaviour_rule` 46 `test-plan-per-module-utility`
**Design:** `_analytics/cross-cluster-web/open-threads-table-proposal-v3-20261012.md` (§8 tests) · **Build:** `iba/app/BUILD.md` §336

**When to run:** in a fresh **standard (App Mode)** session, not the Developer Mode session that built it (CHARTER.md §4). Paste each case's actual result into the "Result" column. The per-case results go into #2000's resolution when it is put up for approval.

---

## 0. Set-up

**Write tests run on a scratch copy, never on live iba.db.** A test thread on live data would use up an OT number and appear in the generated register. Make the copy with the SQLite backup API, which is WAL-safe:

```python
import sqlite3; s = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
d = sqlite3.connect(r'<scratch>/iba-test.db'); s.backup(d); d.close()
```

Then drive the library against the copy: `cfg = Cfg(pathlib.Path(r'<scratch>/iba-test.db')); db = Db(cfg)`, and call `esc.raise_new / update / match_threads / thread_check / resolve_self_correctable / write_*`. Call `db.close()` (it commits) after each case that should write. After a case that should be refused, call `db.conn.rollback()`.

**PS-level cases** (§6) run against live data, but only where nothing is written (read-only actions and refused calls).

---

## 1. Config (build step 1)

| # | Check | Expected | Result |
|---|---|---|---|
| 1.1 | `cfg_enum` read-back | `escalation_type` has `thread`. `escalation_thread_item_kind` has 8 values, `_status` 2, `_response_kind` 7, `escalation_raise_state` 3. `escalation_requirement_check_kind` has `no_open_thread_items` and `must_be_self_correctable` | |
| 1.2 | `cfg_escalation` | row 4 text names threads/T5. New rows: `thread_check_before_work`, `raise_state_choice`, `thread_completion` | |
| 1.3 | `cfg_escalation_transition` | 2 rows at shape=manual priority 0, with condition keys `thread_items_changed_and_referenced` and `thread_items_changed_partly_closed` | |
| 1.4 | `cfg_escalation_requirement` | 4 rows with condition `thread_type` (raise/items, raise/resolution_kind, update/state, resolve_self_correctable/state) | |
| 1.5 | `cfg_behaviour_rule` 74 | `open-threads-carried-as-escalations`, active. Rule 43's exception (2) names Match/ThreadCheck | |
| 1.6 | `Config-Maintenance.ps1 -Step Validate` (or `cfgquality.find_unregistered_tables_and_columns`) | 0 unregistered tables or columns | |

## 2. Schema (build step 2)

| # | Check | Expected | Result |
|---|---|---|---|
| 2.1 | `PRAGMA table_info` on escalation and escalation_history | `alias` and `comes_back_when` on both | |
| 2.2 | Unique alias | Setting a second row's alias to an existing `OT-nn` fails on `idx_escalation_alias`. Two NULL aliases are fine | |
| 2.3 | History mirrors | After an Update with `comes_back_when`, the new history row carries it. `alias` appears in v1 only | |
| 2.4 | Config rebuilds the tables (`lib/db.py:table_ddl()` for both new tables) | escalation_thread_item: inline `UNIQUE (escalation_id, item_no)` + 2 indexes; _response: 3 indexes; index names identical to the live ones (`idx_{table}_{col}`) | |
| 2.5 | `find_escalation_worksheet_drift` | No finding: every Escalation.ps1 parameter is a `-Flag` header in `escalation actions worksheet.xlsx` (Threads block, rows 37–49) | |

## 3. Raise (build step 3: T2, T4, T7)

| # | Case | Expected | Result |
|---|---|---|---|
| 3.1 | Thread with no item | Refused (T7 message); nothing written | |
| 3.2 | Thread with `resolution_kind='decision_required'` | Refused (T4) | |
| 3.3 | Thread, 2 items, no state | Lands on-hold. `next_action` NULL; assigned to Claude (CLI default). Alias = next OT number (OT-103 on a copy with 102). Items numbered 1 and 2 | |
| 3.4 | Thread with `state='raised'` | Refused (never raised) | |
| 3.5 | Thread with `state='in-progress'` | Lands in-progress | |
| 3.6 | Task with `state='on-hold'` | Lands on-hold, `next_action='review'`. The comment is accepted (D26 is an Update check only) | |
| 3.7 | Task with `state='closed'` | Refused (not in `escalation_raise_state`) | |
| 3.8 | Task with `items` | Refused ("for type thread only") | |
| 3.9 | Code raise `raise_()` | Still lands `raised`; it takes no state parameter | |
| 3.10 | Item spec `verse:Rom 7:15-21 :: 7 verses` | kind=verse, value=`Rom 7:15-21`, note=`7 verses` | |
| 3.11 | Duplicate item on the same thread | Refused, naming the existing item number | |
| 3.12 | Title of 61 characters | Refused (T9, unchanged) | |

## 4. Match and transitions (build step 4: T1, T3, T5, T6)

Use a test thread with items `cluster:M10`, `strong:H7067`, `verse:Rom 7:15-21`, and test tasks A (raised) and B (in-progress).

| # | Case | Expected | Result |
|---|---|---|---|
| 4.1 | Match `-Cluster M10c`, no `-For` | Thread listed; nothing written | |
| 4.2 | Match `-Cluster M1` | Not matched (M1 is not M10) | |
| 4.3 | Match `-Strong H7067G`; then `-Strong H7067H` against an item `H7067G` | First matches (base); second does not (different suffix) | |
| 4.4 | Match `-Strong H530` against item `H0530` | Matches (zero-padded) | |
| 4.5 | Match `-Verse "Rom 7:18"`, `-Verse "Rom 7"`, `-Verse "Rom 8:1"` | First two match; third does not | |
| 4.6 | **M10 finds OT-70** (live copy, read-only) | OT-70 listed | |
| 4.7 | Match `-For A` (A raised) | Item `escalation #A` added; thread **stays on-hold** (round 2: in-progress only); one history version with the summary | |
| 4.8 | Match `-For B` (B in-progress) | Item `#B` added; thread **on-hold → in-progress** (T3) | |
| 4.9 | Match `-For B` again | "already referenced"; nothing written | |
| 4.10 | Move A to in-progress (Update `-State in-progress`) | Every on-hold thread referencing A moves to in-progress; the message lists it | |
| 4.11 | Close B (`ResolveSelfCorrectable`, or Update approved) | B's item closes with a `closed` response citing B's resolution. If no other in-progress work references the thread and items remain, the thread goes **on-hold** (T6) | |
| 4.12 | Thread Update `-Item 1 -ResponseKind closed -Respond ...` (one of two open) | Item 1 closed (response row); thread **on-hold** (partial completion) | |
| 4.13 | Thread Update `-NextAction approved -Resolution ...` with an item open | Refused (T6, names the open count); rolled back | |
| 4.14 | Close the last item, then `-NextAction approved -Resolution ...` | **completed** | |
| 4.15 | Close the last item **and** approve in one call | completed (the item close is visible to the check in the same transaction) | |
| 4.16 | `ResolveSelfCorrectable` on a thread with open items | Refused (T6) | |
| 4.17 | `-ResponseKind forward` without `-AddItem` | Refused | |
| 4.18 | `-ResponseKind forward -AddItem cluster:M03 -Via 1998` | Forward response; new item with the next number and `opened_by=1998` | |
| 4.19 | `-ResponseKind reopened` on a closed item | Item open again; response row | |
| 4.20 | `-ResponseKind closed` on an already-closed item | Refused | |
| 4.21 | `-Item OT-16.1` against OT-17 | Refused ("does not belong") | |
| 4.22 | `-Item M72` (value), `-Item cluster:M72`, `-Item 1` | All resolve to the same item | |
| 4.23 | `-Item ... -Respond ...` with no `-ResponseKind` | Refused (needs all three) | |
| 4.24 | `-Item` on a task | Refused ("for type thread only") | |
| 4.25 | `ThreadCheck` on the import (fresh live copy) | **Only OT-09 moves to in-progress** (through #1993); nothing else changes (proposal §7.5) | |
| 4.26 | `ThreadCheck` run twice | The second run changes nothing | |

## 5. Views (build step 5)

| # | Case | Expected | Result |
|---|---|---|---|
| 5.1 | `-Action Thread` | Every on-hold and in-progress thread with its open items; console lines; report in `outputs/escalation/` | |
| 5.2 | `-Action Thread -State in-progress` | In-progress threads only | |
| 5.3 | `-Action Thread -State completed` | Clean usage error (report-continue); **no run_error escalation raised** | |
| 5.4 | `-Action Thread -Id OT-16` | OT-16.1 closed, with `closed` then `forward` responses in date order; OT-16.2 and OT-16.3 open | |
| 5.5 | `-Action Thread -Id OT-999` | Clean usage error; no escalation raised | |
| 5.6 | `-Action History -Id OT-16` | Deep history for #2017 | |
| 5.7 | `-Action List` | No thread in the per-item body or in "Recently resolved"; the "Open threads" section shows counts by state and the in-progress threads only | |
| 5.8 | `-Action Export -Type thread`, then `escalation-2000-register-export-compare-v1-20261012.py` against `archive/open-threads-register-frozen-20261012.md` | 100 rows equal in thread / raised / comes back when; old status text carried 100 of 100; OT-101 and OT-102 extra. **Export of the test set equals the input** | |
| 5.9 | `-Action Export` without `-Type thread` | Refused in PS | |
| 5.10 | `-Id OT-16` on Update / Correction / ResolveSelfCorrectable / EscalateToDecision | Resolves to #2017 | |

## 6. Session start and rule 4 (build step 6)

| # | Case | Expected | Result |
|---|---|---|---|
| 6.1 | `/start-project` step 4B in full | ThreadCheck runs first (OT-09 moves on the first live run); Thread lists; Match reads the strand in progress; researcher-waiting threads named | |
| 6.2 | Rule 4 | Only in-progress threads are reported as "work first" | |
| 6.3 | `/session-close` step 6b | Register regenerated; summary line quoted | |
| 6.4 | Stop hook `.claude/hooks/stop_check_escalation_backlog.py` | On-hold threads are not listed. Once OT-09 is in-progress (after the first ThreadCheck) it **is** listed, as are tasks and issues assigned to Claude | |

## 7. Import (build step 7; already run 2026-10-12 in the build session, re-checked here)

| # | Check | Expected | Result |
|---|---|---|---|
| 7.1 | Counts | 102 threads (#2002–#2103), 284 items, 50 responses (48 closed, 2 forward), 102 v1 history rows | |
| 7.2 | Re-run the import script | "already imported"; nothing written | |
| 7.3 | Completed threads | 9, none with an open item | |
| 7.4 | OT-16, OT-98 | M72 items closed with the #1998 responses; the forward items open | |

## 8. Full cycle

One full `/start-project` and `/session-close` on the new path, in the same standard session.
