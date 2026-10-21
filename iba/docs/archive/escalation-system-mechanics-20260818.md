# Escalation system — full mechanics

**Purpose:** a complete, evidence-based description of how `escalation` actually works today —
every transaction type, every state, every permission, how Claude gets notified to act on it, what
happens to terminal input, and every config row that governs it. Written in direct response to
today's incident (escalation #715's repeated updates never persisting) and the researcher's
question of whether the config system is doing anything real.

**Every claim below is sourced from live code (`iba/app/lib/escalation.py`, `iba/app/ps/
Escalation.ps1`, `iba/app/run.py`) and a live query of `iba.db` on 2026-08-18** — nothing here is
recalled from memory or from prior documentation. Where documentation and live behaviour disagree,
both are stated and the disagreement is flagged.

## 0. This report's own compliance (the researcher asked to see it)

This file itself was produced using the live config, not a hardcoded path or guess:

| What | Live value read | Source |
|---|---|---|
| Where one-off reports live | `iba/app/reports/` | `cfg_setting` key `governance.oneoff_report_dir` |
| Naming pattern | `{topic}-{YYYYMMDD}.{format}` | `cfg_setting` key `governance.oneoff_report_naming_pattern` |
| Format | `md` | `cfg_setting` key `governance.oneoff_report_format` |
| Archive dir for superseded reports | `archive` | `cfg_setting` key `governance.oneoff_report_archive_dir` |
| Document category | (a) planning/investigatory | `governance.procedural_document_taxonomy` — this is a hand-compiled investigation, not a `cfg_*`-generated extract, so it is category (a), not (b) |

Filename applied: `escalation-system-mechanics-20260818.md` (checked first — no existing file of
this base name today, so no `-v2` version bump needed per `docs/file-organisation-rules.md`).

This is a one-time hand-written report, so it does **not** go through `Escalation.ps1`'s own
`write_list_report()`/`archive_before_write()` machinery (that function is specific to the live
open-items list, regenerated on every `-Action List` call) — but it lives in the same governed
directory under the same naming convention, per `governance.oneoff_report_dir`/
`governance.oneoff_report_naming_pattern`.

---

## 1. What `escalation` is, per its own config registration

`cfg_table` (`database='iba'`, `name='escalation'`) describes it as:

> grain: **one row per researcher interaction — the pause**
> use: *"the only sanctioned researcher interaction. A pause, not a fork: the run resumes at
> resume_point when answered."*

That's the design intent in one sentence: an escalation is a **single pause point**, not a running
conversation thread. Everything below follows from that — including why repeated follow-up
comments on one item don't behave the way a conversation would.

---

## 2. The table itself — every column

`iba.db`, table `escalation` (17 columns, no history/audit table alongside it, no triggers):

| Column | Type | What it holds |
|---|---|---|
| `id` | INTEGER PK | The number shown as `#` in every report — **not** the identifier the CLI/PS scripts take (`run_id` is) |
| `run_id` | TEXT | Real pipeline run id (`RUN-...-<STEP>`) or synthetic `MANUAL-<UTC timestamp>` for a standalone item |
| `source` | TEXT | `new-word: <word>` (word-scoped), or `claude`/`researcher` (manual), or a generating module name (code-raised) |
| `at_step` | TEXT | The pipeline step it paused, or literal `manual` |
| `type` | TEXT | `task \| run_error \| issue \| notice \| config` (validated against `cfg_enum escalation_type`) |
| `short_description` | TEXT | The question/description — what the list report shows |
| `context` | TEXT (JSON) | Structured extra detail; for grouped items, `{"reference_doc": "..."}` |
| `tried` | TEXT | Free text; also where `edit_question()` preserves a superseded wording |
| `state` | TEXT | See §3 |
| `next_action` | TEXT | The decision recorded: `approve \| reject \| revise \| hold \| noted` |
| `answered_at` | TEXT | UTC timestamp of the *last* state-changing call — overwritten every time, not appended |
| `raised_at` | TEXT | Set once, at creation |
| `comment` | TEXT | **Single mutable field** — every `AnswerRun`/`Pause`/`Reassign`/`Retract` call that carries a comment overwrites it |
| `resolution` | TEXT | What was actually done — set by `Complete`, or optionally on any terminal answer |
| `related_activity` | TEXT | Groups a package of related rows (see §7) |
| `next_action_assigned_to` | TEXT | `Claude \| Researcher` |
| `answered_by` | TEXT | `Claude \| Researcher` |

**There is no `escalation_history`, `escalation_comment`, or `escalation_log` table.** `comment`,
`short_description` (partially — see §5.6), `next_action`, `answered_at`, `answered_by`,
`next_action_assigned_to`, and `resolution` are all single-value columns on the one row — every
write to them is a destructive overwrite of whatever was there before, with **one exception**:
`edit_question()` appends the old `short_description` into `tried` with a timestamp before
overwriting it. No equivalent exists for `comment`.

---

## 3. State machine — every value, live from `cfg_enum`

Queried directly (not from documentation):

| State | Meaning | Active? |
|---|---|---|
| `raised` | Open, unanswered, awaiting a decision | ✅ |
| `re-assign` | Open, bounced to the other party, no decision made | ✅ |
| `on-hold` | Set aside deliberately (`Pause`, or `hold` decision) | ✅ |
| `in-progress` | **Decided** (approve/revise on a MANUAL item) but work not yet done — added 2026-08-17 | ✅ |
| `closed` | Acknowledged/dismissed (a `noted` decision) — not a real decision | ✅ |
| `withdraw` | Retracted — "never mind," not reviewed | ✅ |
| `completed` | Terminal — decision resolved (dispatcher-tied) or work finished (`Complete` on a MANUAL item) | ✅ |
| `answered` | — | ❌ inactive, superseded by the split above |
| `paused` | — | ❌ inactive, superseded by `on-hold` |
| `retracted` | — | ❌ inactive, superseded by `withdraw` |

`type` (`cfg_enum escalation_type`): active = `task \| run_error \| issue \| notice \| config`;
inactive/retired = `prompted \| interactive \| report-stop \| crash`.

`next_action` (the decision, `cfg_enum escalation_next_action`): `approve \| reject \| revise \|
hold \| noted` — all five active, no retired values.

`assignee` (`cfg_enum escalation_assignee`): `Claude \| Researcher` — exactly two, both active.

**Every one of these is a live DB lookup, not a hardcoded Python list** — `_check_state()`,
`_check_type()`, `_check_next_action()`, `_check_assignee()` in `escalation.py` all query
`cfg.enum(...)` at call time and raise `ValueError` on anything not currently active. This part of
the config is genuinely load-bearing: change a `cfg_enum` row and the code's behaviour changes on
its next call, no redeploy needed.

---

## 4. The two entry points and what happens to your terminal input

### 4.1 `Escalation.ps1` (what you actually type)

`[CmdletBinding()]` with `[ValidateSet(...)]` on `-Action` and `-Decision` — PowerShell itself
rejects an invalid action/decision keyword before anything runs. Ten actions:
`List, Answer, AnswerRun, Raise, Edit, Pause, Resume, Retract, Reassign, Complete`.

Each `switch` branch does **light validation only** (required-parameter presence, e.g. "AnswerRun
needs -RunId and -Decision") and then shells out:

```
python -m iba.app.lib.escalation <verb> <positional args> [--flag=value ...] [free-text comment]
```

**No PowerShell-side logging.** `Escalation.ps1` prints nothing to a file — only `Write-Host`
warnings on bad input, and whatever the Python process prints to stdout on success. Nothing about
the invocation itself (who ran it, when, with what exact arguments) is captured anywhere once the
terminal scrolls past it — confirmed by grepping the script for any file write: there is none.

### 4.2 `iba.app.lib.escalation` (the Python CLI, `main()`)

Parses `sys.argv` directly (no `argparse`) — the first token selects the verb, `_extract_flag()`
pulls `--name=value` tokens out of the remainder, whatever's left becomes the free-text comment/
question. Calls the matching function (§5), then `print()`s exactly one line: the function's
return string. **That print is the only output — win or fail — and it goes nowhere but your
terminal.** No file, no table, no log captures it.

### 4.3 End-to-end trace for one real command

```
Escalation.ps1 -Action AnswerRun -RunId MANUAL-20260818_042639_283281 -Decision Approve -Comment "approved to proceed refer to ..."
  -> python -m iba.app.lib.escalation answer-run MANUAL-... approve --by=Researcher "approved to proceed refer to ..."
    -> main() parses argv, calls answer_for_run(cfg, db, run_id, "approve", comment=..., answered_by="Researcher")
      -> _resolve_run_id()          -- run_id used as-is (already a real run_id, not a bare #)
      -> cfg.enum("escalation_next_action") -- confirms "approve" is valid
      -> pending_for_run()          -- row found in state='raised'
      -> _grant(cfg, "escalation")  -- confirms cfg_write_grant permits writer='escalation' -> table='escalation'
      -> _terminal_state_for("approve", is_manual=True) -- MANUAL + approve -> 'in-progress' (NOT 'completed')
      -> db.update("escalation", {id: esc_id}, state='in-progress', next_action='approve',
                    comment=<your text>, resolution=None, answered_by='Researcher', answered_at=<now>)
    -> returns "escalation 715 (run 'MANUAL-...', step 'manual') answered 'approve' -> in-progress
       -- use Escalation.ps1 -Action Complete when the work is actually done — '<your comment>'"
  -> printed to your terminal, nothing else written anywhere
```

That single `db.update` is the entire transaction. It is not wrapped in any audit/logging layer —
`cfg_change_detail` (the real, working before/after audit table — see §8) is **never touched**,
because it is wired only into `handlers/configmaint.py`'s `configmaint.propose` path, not into
`escalation.py`.

---

## 5. Every transaction type — preconditions, effect, what's destroyed

All ten, from `escalation.py`, in the order a real workflow would hit them:

| # | Function / `-Action` | Valid FROM state(s) | Resulting state | What it overwrites |
|---|---|---|---|---|
| 1 | `raise_()` / `raise_manual()` — `-Action Raise` | *(new row)* | `raised` | *(nothing — new row)* |
| 2 | `answer_for_word()` — `-Action Answer` (word-scoped only) | `raised` | `completed` | `next_action`, `resolution`, `answered_by`, `answered_at`; also sets `word_registry.status` |
| 3 | `answer_for_run()` — `-Action AnswerRun` | `raised` (or `on-hold`/`re-assign` via **auto-resume**, §5.1) | `on-hold` (hold) / `closed` (noted) / `in-progress` (approve/revise, MANUAL only) / `completed` (everything else) | `state`, `next_action`, **`comment`** (full overwrite), `resolution`, `answered_by`, `answered_at` |
| 4 | `reassign_run()` — `-Action Reassign` | `raised`, `on-hold`, `re-assign`, `in-progress` | `re-assign` (or stays `in-progress` if it was already, §5.2) | `next_action_assigned_to`, `comment` |
| 5 | `complete_run()` — `-Action Complete` | `in-progress` **only** | `completed` | `resolution` |
| 6 | `edit_question()` — `-Action Edit` | `raised`, `on-hold`, `re-assign`, `in-progress` | *(unchanged)* | `short_description` (old value appended to `tried` first — the one field with real history) |
| 7 | `pause_run()` — `-Action Pause` | `raised`, `re-assign`, `in-progress` | `on-hold` | `state`, `comment` |
| 8 | `resume_run()` — `-Action Resume` | `on-hold`, `re-assign` | `raised` | `state` |
| 9 | `retract_run()` — `-Action Retract` | `raised`, `on-hold`, `re-assign`, `in-progress` | `withdraw` | `state`, `comment`, `answered_by`, `answered_at` |
| 10 | `open_duplicate()` — internal only, not a `-Action` | *(read-only)* | — | Suppresses a new `raise` if a matching one is already `raised` for the same step |

### 5.1 The auto-resume — and its documented limit

`answer_for_run()` will silently flip a `MANUAL-` item from `on-hold`/`re-assign` back to `raised`
and then answer it in the same call, **if** it's in one of those two states. This was built
2026-08-17 specifically because the researcher hit "no pending escalation" three times in one
session on items that were on-hold. **It does not cover `in-progress`.** The docstring is explicit
that this was a deliberate scope decision, and `in-progress` items must go through `-Action
Complete` instead. **This is the exact mechanism behind today's #715 incident**: once an item
reaches `in-progress` (which happens the moment it's first approved), every subsequent `AnswerRun`
call — however many were typed — hits `if not rows: return "no pending escalation for run ..."`
and returns without writing anything.

### 5.2 Reassign's special case for `in-progress`

Fixed 2026-08-17 (escalation #692) for the opposite reason: reassigning an `in-progress` item used
to discard the decision (forced back to `re-assign`, requiring a fresh `AnswerRun`, "re-approving
something already approved" — the researcher's own words, recorded in the code comment). Now it
changes only `next_action_assigned_to` and leaves `state='in-progress'` intact.

### 5.3 `hold`/`noted` are not `completed` — and only for MANUAL items in one respect

`_terminal_state_for()` maps `hold -> on-hold` and `noted -> closed` for **every** escalation, word-
or run-scoped. This exists because, before 2026-08-16, any decision that wasn't literally `approve`
fell through to a hardcoded `'rejected'`/`'completed'` — meaning answering `hold` on a real
dispatcher-tied pause was silently treated as if it meant "needs revision." Confirmed fixed by
reading the current code, not assumed from the changelog.

### 5.4 `is_manual` gate on `in-progress`

Only `MANUAL-`-prefixed run_ids can land on `in-progress`. A real dispatcher-tied escalation
(e.g. `configmaint.propose`) still resolves `approve`/`revise` straight to `completed` — its 7
downstream handlers only understand approve/reject and apply the change the moment it resolves, so
introducing `in-progress` there would break the apply-on-resume flow. This boundary is enforced in
code (`_terminal_state_for(decision, is_manual=run_id.startswith("MANUAL-"))`), not just documented.

### 5.5 The `_manual_only` boundary

`Edit`, `Pause`, `Resume`, `Retract`, `Complete`, and `Reassign` all refuse to operate on a real
(non-`MANUAL-`) run_id — `_manual_only()` checks the prefix and returns an error string instead of
touching the row. Reason given in code: a real dispatcher-tied row is read by other live machinery
(`answered_for_run`'s `state='completed'` filter, `run.py`'s own duplicate-raise dedup checking
`state='raised'`) that these five actions would desynchronise from if allowed to touch it.

### 5.6 `_resolve_run_id` — the `#` vs `run_id` trap

Typing the bare `#` shown in the report (e.g. `715`) as `-RunId` **does work** — `_resolve_run_id`
detects a digits-only identifier and looks up the real `run_id` string for you. This was itself a
2026-07-30 fix for a prior version of the same class of confusion (a researcher typed `-RunId 384`
expecting it to work, and it didn't, before this fix).

---

## 6. Rights — who may write the table, and how that's actually checked

`cfg_write_grant` (queried live) currently authorises exactly two writers for `database='iba'`,
`table_name='escalation'`, both active:

| Writer | Meaning |
|---|---|
| `escalation` | `lib/escalation.py` itself — every function in §5 |
| `run` | `run.py`'s dispatcher, which writes `escalation` **directly** at 3 call sites (pause records, crash records) — bypassing `lib/escalation.py` entirely, by its own code comment's admission |

**Enforcement mechanism:** `_grant(cfg, "escalation")`, called individually inside every
write-performing function in §5, does exactly one thing:

```python
if table not in cfg.may_write("escalation"):
    raise PermissionError(...)
```

This is real — it queries `cfg_write_grant` live and will hard-stop a write if the grant is ever
revoked or deactivated. **What it does not do**: log the check, log the write, or leave any trace
that the check happened. Contrast this directly with `handlers/configmaint.py`'s `configmaint.
propose` path, which performs the equivalent grant check **and** writes a full before/after JSON
row to `cfg_change_detail` (277 real rows, confirmed live) every time. `escalation.py`'s grant check
is real permission enforcement with zero audit trail — a narrower and more consequential gap than
"no history," because it means even a *rejected* write attempt leaves no record either.

`Db.write()` separately validates that every column being inserted exists in the config's schema
(`cfg.column_names(table)`) — but `Db.update()` (used by every `escalation.py` write) has **no**
such check. Column validation only applies to inserts, not updates.

---

## 7. Grouping — the closest thing to "related items," and how it's enforced

`related_activity` plus `context.reference_doc` is the pattern used to keep a package of connected
escalations findable as a unit (e.g. this session's `operational-behaviour-rules-cfg` items #715/
#734, or yesterday's `engine-controls-migration` chain #648→#669→#670→#672→#677→#680→#699→#701).
This is **mechanically enforced** by `raise_manual()`: any `related_activity` other than the
default `"manual"` requires a `reference_doc`, or the write is refused outright with a `ValueError`
— found necessary 2026-08-16 when 14 rows landed with `context='{}'` despite the rule already being
written in `cfg_escalation`.

**Important:** this pattern is a chain of **separate escalation IDs**, cross-referencing each other
by number inside free-text `short_description`/`comment` fields (e.g. "Escalation #669 revision:
v2 of..."). It is not a thread on one row — it's the same overwrite-per-row limitation as
everything else, just distributed across multiple rows instead of one. Reconstructing "the full
history of this package" means manually reading every row in the group in id order; there is no
query or report that assembles them into one narrative automatically.

---

## 8. Is there a real audit trail anywhere? — precise answer

**Yes, but it does not cover `escalation`.** `cfg_change_detail` (277 rows, confirmed live) is a
genuine, working, before/after JSON audit log with `applied_at` timestamps. Every single row I
found has a `run_id` of the shape `RUN-...-CONFIGMAINT` — it is wired into exactly one code path,
`handlers/configmaint.py`, and fires only for `cfg_*` table changes proposed through
`configmaint.propose`. `escalation.py` never calls into it. `cfg_change_log` is narrower still —
one row per whole-config-store reload, not per change.

The `run` table (the record of actual pipeline executions, `cfg_table`'s own description: "the
control record") **never gets a row for a `MANUAL-` escalation** — `raise_manual()`'s docstring
states this as a deliberate, documented design choice ("no 'run' row exists for it... this needs
no special-casing"). So there is no execution-level log to fall back on for manual items either.

**PowerShell's own command history** (`ConsoleHost_history.txt`, PSReadLine) was checked directly
this session and confirmed to hold zero entries for #715/#725/#734, and to never capture anything
run through the Claude Code tool interface at all (verified: this session's own `Get-
NetTCPConnection`/`Start-Iba.ps1` calls, run minutes earlier, are absent from it) — it only records
commands typed into a genuine interactive PowerShell console.

**Net finding:** there is no layer, anywhere in the stack, that would have preserved a second or
third update to escalation #715 once the first `AnswerRun` moved it to `in-progress`.

---

## 9. How Claude gets notified to act — there is no push mechanism

Checked explicitly, because this is the "how do you get notified" half of the question. There is
**no automated/event-driven notification** of any kind — no hook, no polling loop, no DB trigger.
What actually happens:

1. **Session start convention**: the `start-project` skill's step 4 explicitly runs
   `Escalation.ps1 -Action List` and instructs reading the resulting report for anything
   `raised`/`in-progress`/`on-hold`/`re-assign` relevant to the session, especially rows with
   `next_action_assigned_to='Claude'`. This is a documented procedure Claude follows when invoked,
   not something the system enforces on its own.
2. **`cfg_escalation.resolution_precedence`** (rule 4): *"Escalation resolution takes precedence
   over any other activity; open items with `next_action_assigned_to='Claude'` must be addressed
   before other work."* Its own `enforced_by` field states plainly: **"session practice (Claude
   Code) — not mechanically enforced."**
3. **`cfg_escalation.chat_routing`** (rule 5): the rule that a genuine open judgement call surfaced
   in chat prose must get its own escalation in the same turn. Also self-documented as **"not
   mechanically enforced (nothing can reliably scan this session's own prose...)"** — and its own
   text records a real violation the researcher caught live on 2026-08-16.
4. **The one mechanically enforced consequence — `cfg_escalation.module_blocking`** (rule 3): a step
   or module with an unresolved (`raised`/`re-assign`) escalation against it is refused at dispatch
   time. This **is** real code, confirmed live in `run.py` (`run_step()`, "Third gate," citing
   escalation #646, dated 2026-08-17) — it queries `escalation` directly before allowing a step to
   run and raises `PermissionError` if a match is found. **However: `cfg_escalation`'s own row for
   this rule is stale** — its `enforced_by` text still reads *"not yet wired — scheduled as a task
   escalation, see the reset's backlog pass,"* even though the code implementing it has been live
   for a day. This is a live, concrete instance of the config's own documentation drifting out of
   sync with the code it describes — surfaced by writing this report, not previously known.

So: three of the four rules that would make Claude "notice" an escalation are explicitly,
self-admittedly session-practice-only. Only one enforces anything mechanically, and it enforces
*dispatch-blocking*, not *drawing Claude's attention to a pending item* — those are different
things.

---

## 10. Reporting — `write_list_report()`

`Escalation.ps1 -Action List` calls this. It:
- Selects every row in `_OPEN_STATES = (raised, re-assign, on-hold, in-progress)`, grouped by
  `related_activity`, then `id`.
- Splits the open count into active / in-progress / on-hold explicitly (added 2026-08-17 so
  "awaiting a decision" and "decided, work under way" read as different things at a glance).
- Appends a **"Recently resolved (last 15)"** section — rows in `completed`/`closed` with a
  non-null `resolution`, newest first — added 2026-07-23 specifically because, before that, a
  resolved item and its resolution simply vanished from the only report that existed.
- Reads `escalation.control_objectives` and `escalation.control_process` from `cfg_setting` live
  and prints them as the report's own header line — confirmed these settings existed since the
  2026-08-16 reset with no code ever reading them until this fix (found via the orphan-config
  check).
- Archives the previous report (`reportkit.archive_before_write`) before writing the new one —
  same convention used by every other report/export in the app, so a `-Action List` run never
  destroys the prior snapshot.

---

## 11. Every config row governing `escalation` — full inventory

### 11.1 `cfg_escalation` (7 active rules, verbatim)

1. **`source_classification`** — enforced by `raise_`/`raise_manual`'s `source` parameter. ✅ live.
2. **`duplicate_suppression`** — "a duplicate of the same issue in the same state must not be
   raised again." Enforced by `open_duplicate()`. ✅ live, but scoped narrowly (substring match on
   a caller-supplied stable key, only wired into a few validate-style callers — not generic).
3. **`module_blocking`** — see §9. Config text says *not yet wired*; code shows it **is**, since
   2026-08-17. ⚠ documentation drift, found while writing this report.
4. **`resolution_precedence`** — "Claude-assigned open items must be addressed first." **Not
   mechanically enforced** (self-declared).
5. **`chat_routing`** — genuine open judgement calls in chat must get their own escalation same-
   turn. **Not mechanically enforced** (self-declared); records a real 2026-08-16 violation.
6. **`document_reference_grouping`** — see §7. ✅ mechanically enforced (`ValueError` on violation).
7. **`full_path_file_references`** — file mentions must be full repo-relative paths. **Not
   mechanically checked** (self-declared free-text discipline).

**So: of 7 rules, 3 are real, checked, code-enforced (`source_classification`,
`document_reference_grouping`, and `module_blocking` despite its stale description); 3 explicitly
admit they are session-practice only; 1 (`duplicate_suppression`) is real but narrow.** None of the
7 addresses repeat-update history — that gap was never named as a rule to begin with.

### 11.2 `cfg_enum` groups — see §3 for full values: `escalation_state`, `escalation_type`,
`escalation_next_action`, `escalation_assignee`.

### 11.3 `cfg_setting`, module `escalation` (3 rows, all active)
- `escalation.control_objectives` — the mission statement printed at the top of every list report.
- `escalation.control_process` — likewise.
- `escalation.list_report_path` — `iba/app/reports/escalation-list.md`.

### 11.4 `cfg_write_grant` — see §6: `writer='escalation'` and `writer='run'`, both
`database='iba'`, `table_name='escalation'`, both active.

### 11.5 `cfg_utility` — one row: `module='escalation'`, `file_path='iba/app/lib/escalation.py'`,
`inactive=0`, `config_exempt=0`. It is **not** registered as a `cfg_work_package`/`cfg_step` —
it's a standalone utility, not a chained pipeline stage.

---

## 12. Structural findings — summary, most consequential first

1. **No append-only history anywhere for `escalation`.** `comment`, `next_action`,
   `answered_by`, `answered_at`, `resolution`, and (mostly) `short_description` are single mutable
   fields, overwritten on every state-changing call. This is why #715's later updates are
   unrecoverable.
2. **No supported path to add a comment to an `in-progress` item without terminating it.**
   `AnswerRun` only resolves `raised`/`on-hold`/`re-assign`; `Complete` requires a `-Resolution` and
   closes the item. There is no "just add a note, stay open" action — this is the exact mechanism
   behind today's incident.
3. **Write-grant enforcement has zero audit trail.** `_grant()` is real but silent — unlike
   `configmaint.propose`, no `cfg_change_detail` row (or equivalent) is written when `escalation.py`
   writes, succeeds, or is refused.
4. **`run` never logs a `MANUAL-` escalation's execution** — by explicit design, so there's no
   fallback audit trail there either.
5. **Claude's own attention to open escalations is not mechanically enforced** — 3 of the 4
   relevant `cfg_escalation` rules self-declare "session practice only." The one real enforcement
   mechanism (`module_blocking`) blocks *dispatch*, not *attention*, and its own config description
   is stale.
6. **The config's own documentation of itself has drifted at least once** (`module_blocking`'s
   `enforced_by` text), found only by cross-checking code against config directly for this report —
   the same kind of drift the researcher suspected going into this request.

---

## 13. Direct answer to "are you using the new configs for this process"

Yes — concretely, in producing this report I read live, rather than assumed or recalled:
`governance.oneoff_report_dir`, `governance.oneoff_report_naming_pattern`,
`governance.oneoff_report_format`, `governance.oneoff_report_archive_dir`,
`governance.procedural_document_taxonomy`, all 7 `cfg_escalation` rows, all values in
`cfg_enum` for `escalation_state`/`escalation_type`/`escalation_next_action`/
`escalation_assignee`, all `escalation.*` rows in `cfg_setting`, the `cfg_write_grant` rows for
`table_name='escalation'`, the `cfg_utility` row for module `escalation`, and 277 rows of
`cfg_change_detail` (to establish what it does and does not cover). Every table/column reference
above was checked against the live schema, not written from memory. The one place config and code
disagree (§9, `module_blocking`) was found *by* doing this check, not asserted from prior
knowledge — which is itself the honest answer to the question: the config system is real and
readable, and cross-checking it against code is exactly how this kind of drift gets caught, but
nothing here caught it automatically — I found it because you asked me to look.
