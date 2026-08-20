# Escalation utility — config review (v1, 2026-08-20)

Prepared per escalation **#753 v2**: *"prepare a detail report of all the existing configs related
to escalation utility before any changes are made; validate that all the existing configs are used,
align with the intent, and are complete."* This is the report — **no config or code changes are
made in this pass**. Method: read the live `cfg_*` tables in `iba/app/db/iba.db` directly (not
docs), then read `iba/app/lib/escalation.py`, `iba/app/ps/Escalation.ps1`, and `iba/app/run.py` to
check whether the code actually consults what's configured, per
`feedback_iba_gap_analysis_requires_live_build_inspection`.

Supporting documents (per the review notes,
`Workflow/Chat_responses/escallation utility refinement 2026-08-20`):
[`escalation-redesign-plan-v3-20260819.md`](escalation-redesign-plan-v3-20260819.md) (the live
design), `Workflow/Chat_responses/archive/comments - escalation-system-mechanics` (the researcher's
own review notes that drove the redesign).

---

## 1. Full config inventory — every cfg_* row that governs the escalation module

Searched all 31 `cfg_*` tables for rows naming `escalation`/`escalation_history`, or scoped to the
`escalation` module. 11 tables have relevant rows; 20 have none (correctly — e.g. `cfg_step` has 0
rows, matching the design decision that a standard PS routine is no longer escalation-scoped, only
genuine errors are).

| cfg table | rows | what it governs here |
|---|---|---|
| `cfg_table` | 2 | `escalation`, `escalation_history` — grain + use text |
| `cfg_column` | 37 | every column on both tables (18 + 19) |
| `cfg_enum` | 34 (8 active groups incl. legacy) | `escalation_state`(9), `escalation_next_action`(8), `escalation_type`(5), `escalation_assignee`(2), `escalation_answer`(3, all inactive) |
| `cfg_write_grant` | 4 | `escalation`→`escalation`, `run`→`escalation`, `escalation`→`escalation_history`, `escalation`→`word_registry` |
| `cfg_utility` | 1 | the module registration itself |
| `cfg_escalation` | 7 | the rule table governing escalation.py's *own* behaviour (duplicate suppression, module blocking, etc.) |
| `cfg_setting` | 4 | `escalation.control_objectives`, `.control_process`, `.history_report_dir`, `.list_report_path` |
| `cfg_report` / `cfg_report_section` | 0 / 0 | **none** — see Finding 3 |
| `cfg_status_flow` | 0 | **none** — see Finding 1 |
| `cfg_step` | 0 | correctly empty (design decision, not a gap) |

---

## 2. What's correct and complete — stated plainly, not just problems

- **Table/column registration is genuinely complete.** All 18 `escalation` and 19
  `escalation_history` columns have a `cfg_column` row with real `use` text that matches what the
  code actually does (checked every column's `use` against `escalation.py`'s field handling —
  no stale or invented descriptions found).
- **All 4 `cfg_setting` rows are actually consulted** — `control_objectives`/`control_process` in
  `write_list_report()`'s header line, `history_report_dir`/`list_report_path` in the CLI's `list`/
  `history` handlers. No orphan settings.
- **`cfg_write_grant`'s `escalation`→`escalation` and `escalation`→`escalation_history` rows are
  both live and both checked** — `_grant_both()` (escalation.py:124) checks both explicitly on
  every write, the fix built for escalation #745.
- **`cfg_step` correctly has zero rows** — matches the design decision (`escalation.py`'s own
  docstring) that a standard operational routine is no longer escalation-scoped.

---

## 3. Findings — new, not yet tracked elsewhere

### Finding 1 — `cfg_status_flow` exists for exactly this and has zero escalation rows

`cfg_status_flow` (columns: `entity, status, set_by, ordinal, inactive`) exists specifically to
record, per entity, which party/mechanism is allowed to set which status. The escalation state
machine is the single most detailed state machine in the app — plan v3 §3 is a whole priority-
ordered table of exactly this shape (which `next_action` yields which `state`, and plan v2 §7
explicitly separates states either party may set directly (`on-hold`/`in-progress`/`closed`) from
ones only logic may set (`completed`, `withdraw`, `supersede`)) — and none of it is in
`cfg_status_flow`. It lives only in Python (`_derive_state()`, escalation.py:269-285) and in the
plan-v3 prose doc. This is the clearest instance of the researcher's stated concern — *"not
convinced that the rules for the new functionality is actually encapsulated in the configs"* — a
table built for precisely this purpose, sitting empty, while the actual rule lives in code + a
planning doc instead.

### Finding 2 — `escalation_next_action` conflates two vocabularies the design says must stay separate, and code doesn't consult the config consistently

Plan v3 is explicit both vocabularies are "deliberately NOT unified." In practice:

- The **manual** path (`update()`, escalation.py:288) validates `next_action` against
  `cfg_enum('escalation_next_action')` via `_check_next_action()` — correctly config-driven.
- The **dispatcher-tied** path (`answer_for_run()`, escalation.py:226) does **not** consult
  `cfg_enum` at all — it validates against a hardcoded Python tuple
  `("approve", "reject", "revise", "hold", "noted")` (escalation.py:231).
- `Escalation.ps1` duplicates this a third time as a hardcoded PowerShell `ValidateSet` on
  `-Decision` (line 81) — a third independent copy of the same 5 values.

Net effect: `cfg_enum('escalation_next_action')` holds all 8 values (both vocabularies merged,
undifferentiated) but is **only actually enforced for the manual shape**. Because the merged enum
is undifferentiated, `update()`'s enum check will currently **accept** dispatcher-only values
(`approve`, `hold`) as valid for a manual item via the direct Python CLI (`python -m
iba.app.lib.escalation update <id> --next-action=hold`) — `_derive_state()` has no case for
`hold`, so it would silently fall through to a no-op state change while still recording
`next_action='hold'` on a manual row, which is meaningless there. `Escalation.ps1`'s own
`-NextAction` `ValidateSet` (line 82) correctly restricts to the 6 manual values and blocks this at
the PS front door — but the underlying Python function has no equivalent scoping of its own, so the
gap is only closed by one caller's discipline, not by the config.

Cosmetic issue in the same enum, found while checking it: `escalation_next_action` has `approve`
and `reject` both at `ordinal=0` (a genuine duplicate), and `ordinal=4` is skipped entirely (3→5).
Display-order only, not a validation bug, but confirms the row set was hand-edited across the
redesign rounds without a final pass.

### Finding 3 — the escalation module's two reports bypass the app's own config-driven reporting standard entirely

Every other report-producing step in the app (22 registered: `report.word`, `candidate.validate`,
`configmaint.report`, etc.) goes through `reportkit.render_scaffold()`, which reads its title/ToC/
footer/section list from `cfg_report`/`cfg_report_section` rows — enforced by a real, wired check,
`cfgquality.find_missing_cfg_report_rows()` (`iba/app/lib/cfgquality.py:60`), run as part of
`configmaint.validate`.

`escalation.py`'s `write_list_report()` and `write_history_report()` (escalation.py:328, 384) do
**neither**: both hand-build their `L = [...]` line lists directly in Python — headings, table
columns, section order, all hardcoded — and never call `reportkit.render_scaffold()` or touch
`cfg_report` at all. The escalation module isn't even named in `cfgquality.py`'s hardcoded
`REPORT_STEPS` tuple (line 43-48), so `configmaint.validate` has no way to ever flag this drift —
it doesn't know these two reports exist.

This directly matches two independent researcher observations that turn out to be the same root
cause: the notes file's *"Reports / Open escalations: report layout does not comply with the
project standard"*, and the 2026-08-18 comments doc's *"there should be a development config in
place to set the folder for this report, it should not be `iba\app\reports`"* (that folder-location
half of the complaint is the already-open filing decision, escalation **#736** — cross-referenced,
not re-raised here; this finding is the report-*shape* half, which #736 doesn't cover).

### Finding 4 — an orphan write-grant row

`cfg_write_grant(writer='escalation', table_name='word_registry')` — grepped the entire codebase:
`escalation.py` never writes `word_registry`, and no other module checks `cfg.may_write("escalation")`
against `word_registry` either. Nothing exercises this grant. Likely a leftover from an earlier
design (word-scoped escalation touching registry status directly) that never made it into the
redesign, or a copy-paste artifact. Low severity — an unused permission, not a missing one — but it
sits alongside the (separately tracked, escalation **#750**) opposite problem: a *needed* grant
row now dead the other way (`writer='run'`). Flagging both together here since they were found in
the same pass over the same table.

---

## 4. Cross-references — already open, not re-litigated here

- **#746** — `cfg_escalation` (the 7-row rule table governing escalation.py's own behaviour, e.g.
  `module_blocking`) still describes pre-redesign mechanics in places; a known-stale
  `enforced_by` value never fixed. Open, assigned Claude.
- **#748** — 2 orphan-config findings from the frozen `#735` never resolved; needs a fresh
  `configmaint.validate` run under the live system. Open, assigned Researcher.
- **#750** — `cfg_write_grant(writer='run', table_name='escalation')` is dead the *other*
  direction from Finding 4 above — confirmed again in this pass: `run.py` no longer writes
  `escalation` directly, it goes through `lib.escalation.raise_()` (imported as `esc_raise`,
  `run.py:25`), which checks `writer='escalation'`, never `writer='run'`. Open, assigned
  Researcher.

---

## 5. "Specific configs to create and enforce" — candidates for your decision (per #753's note that this section was left blank for me to propose)

None of these are built — they're proposals, gated on your review, per #753's "before any changes
are made":

1. **Populate `cfg_status_flow` for `entity='escalation'`** — one row per `(status, set_by)` pair,
   turning plan v3 §3's priority table (and v2 §7's either-party-vs-system-only split) from
   code+prose into config `_derive_state()` can be checked against. Closes Finding 1.
2. **Register `escalation.list` and `escalation.history` as `cfg_report`/`cfg_report_section` rows**
   and route `write_list_report()`/`write_history_report()` through `reportkit.render_scaffold()`
   like the other 22 reports; add both step names to `cfgquality.REPORT_STEPS` so drift is caught
   going forward. Closes Finding 3.
3. **Disambiguate `escalation_next_action`** so the manual and dispatcher-tied vocabularies can't
   leak into each other via the config — e.g. a `scope` column on `cfg_enum` (dispatcher/manual),
   or two separately-named enums (`escalation_next_action_manual` /
   `escalation_next_action_run`) with `update()`/`answer_for_run()` each checking only its own.
   Also fix the `ordinal` duplicate/gap while touched. Closes Finding 2.
4. **Retire or justify** `cfg_write_grant(writer='escalation', table_name='word_registry')` — mark
   `inactive=1` if truly dead, or document the real (currently unbuilt) use it's reserved for.
   Closes Finding 4.

Recommend deciding items 1-2 first (they're the two your own notes already flagged from the outside
— the state-machine-in-code concern and the report-layout concern); 3-4 are smaller cleanup found
while investigating.

---

## 6. What this report does not cover

Per #753's remaining buckets, not addressed here (separate, smaller items once you've reviewed
this):
- `escalation_history`'s "short-description does not comply with" — the note in
  `Workflow/Chat_responses/escallation utility refinement 2026-08-20` cuts off after "with", no
  object stated. Needs a clarifying word from you before I can act on it — not guessed here.
- USER-GUIDE.md completeness/accuracy pass — separate write-up once the config decisions above
  land, since the guide should describe the *settled* config shape, not get rewritten twice.
