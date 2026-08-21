# Escalation design — decision register (v9, 2026-08-21) — consolidated

**Single coherent reference**, combining every decision point across v1–v8 into one place. Each
section below states the *current, final* content — corrections and withdrawals from earlier rounds
are not repeated; the provenance (what changed, when, why) lives in the dated version files
(`escalation-design-decision-register-v1` through `-v8-20260821.md`) if that history is ever needed.
This is the version to read going forward.

**Status key:** `SETTLED` · `OPEN — fully specified, awaiting decision` · `REJECTED` · `PARKED —
code-only, not a config decision` · `RETIRED — numbering artifact, not a real item`.

---

## Summary table

| # | Decision | Status |
|---|---|---|
| D1 | Rebuild `escalation` from both sources (JSON export + this session's own live rows), converted through the real code path, dry-run first | OPEN — fully specified |
| D2 | Fix stale `cfg_table.use` text (`escalation`/`escalation_history`) | OPEN — exact wording given |
| D3 | Crash-escalation control mechanism (`cfg_utility` checkbox columns); crash-wrapper itself needs `from_id`-awareness | OPEN — fully specified |
| D4 | Register `escalation.list`/`escalation.history` through `cfg_report`/`cfg_report_section`/`cfg_report_csv_table` | OPEN — all 15 rows listed |
| D5 | `GOVERNANCE.md` content list (10 items) | OPEN — enumerated |
| D6 | A standing tracker survives a reset — `cfg_escalation` rule | **SETTLED** |
| D7 | `cfg_utility.escalation.purpose` — exact replacement text | OPEN — wording given |
| D8 | `escalation_shape` orphan-check blind spot | PARKED — code fix, → `#9` |
| D9 | Five-type model | **SETTLED** |
| D10 | `cfg_escalation_link` typed link table | **REJECTED** |
| D11/D21 | Issue's `next_action` vocabulary — reuses manual's in full | **SETTLED** |
| D12 | Type-keyed Raise defaults — only `notice` is special | **SETTLED** |
| D13 | — | RETIRED — never assigned |
| D14 | `from_id`/`related_activity` mechanism — column + validation | OPEN — fully specified |
| D15 | Report exception categories (cycle/dangling/mismatched-pairing/missing-link/incoherent-link) | OPEN — sections specified in D4 |
| D16 | `run.py` re-plumbing scope/timing | OPEN — same config as D4, sequencing only |
| D17 | — | RETIRED — v1 placeholder, not a real item |
| D18 | Produced-documentation-task pattern (absorbs D20) | OPEN — `cfg_escalation` rule given |
| D19 | Chat-capture verbatim-quote convention | OPEN — wording given |
| D20 | Document relationship (BUILD/GOVERNANCE/CLAUDE/USER-GUIDE) | folded into D18 |
| D21 | (same as D11) | — |
| D22 | PS-side crash-safety-net gap | PARKED — code fix |
| D23 | Keep PS, fix the dispatch | OPEN — same config as D4/D16 |
| D24 | This register's own completeness | ongoing, not a config row |
| D25 | Authority-based approval, not same-party (fixes shipped code) | OPEN — fully specified |
| D26 | Work cannot land on a `raised` item; "start work" chat trigger | OPEN — fully specified |
| D27 | `ready_for_approval` missing transition rule | OPEN — fully specified |
| D28 | PS `ValidateSet` vs. live `cfg_enum` drift check | OPEN — fully specified |

**24 real decision points** (5 numbers retired/folded/self-referential): 6 settled, 1 rejected, 3
parked as code-only, 14 open with a complete, buildable specification.

---

## Settled

### D6 — standing trackers survive a reset
New `cfg_escalation` row, `rule_key='standing_items_survive_reset'`:
> *"Any item explicitly marked to stay open until signed off... must be re-raised, carrying its
> unresolved scope forward, in the SAME unit of work as any full export+wipe of the escalation
> table... Before a wipe proceeds, open standing items are checked for and flagged if found."*

### D9 — five-type model
`task`/`issue`/`notice`/`run_error`/`config` — each behaviourally distinct, not just labelled.
`cfg_enum('escalation_type')` already holds all five; no new enum content. Behaviour lives in D12
(defaults), D11/D21 (vocabulary), D18 (produced-documentation).

### D11 / D21 — issue reuses the manual vocabulary in full
No separate `open`/`decided`/`abandoned` scheme. `review`/`revise`/`ready_for_approval`/`approved`/
`reject`/`noted` — the same six values, same transition rules, same requirement rules as any other
manual-shape item. `state` during back-and-forth: `in-progress` while worked solo, `re-assigned` the
moment it's handed to the other party (existing generic fallback, no new mechanism). Individual
points within one issue are **not** separately state-tracked — that's the reference document's job
(or this register's, as its own live proof).

### D12 — type-keyed Raise defaults
Only `notice` is special: `state='closed'`, `next_action=NULL` at creation, no second transaction.
Every other type — `task`/`issue`/`run_error`/`config` — defaults identically: `state='raised'`,
`next_action='review'`. (Corrects v2's original claim that `issue` also got a special default — that
referenced the withdrawn `open` value.) Config vs. code: a `raise_new()` branch, not a new table — one
behavioural exception among five types doesn't warrant its own mapping table.

---

## Rejected

### D10 — `cfg_escalation_link`
A typed, many-to-many, `cfg_`-prefixed link table. Wrong prefix (data, not config — `cfg_` is
configuration only). Wrong shape (every real chain found this session is single-parent). Superseded
by D14.

---

## Fully specified, open

### D1 — Rebuild `escalation`, both sources, converted, dry-run first

**Sources**: the JSON export (`escalation{,_history}-export-20260820.json`, 24+96+1 rows) **and**
this session's own live rows (`#1`–`#9`+, created after the wipe, not in the export). `escalations_old`
(735 rows) is **not** touched. Id sequence reseeded to 735 first; both sources replayed in true
chronological order (export, then this session's rows) so numbering continues correctly and every
`#7xx` citation in `BUILD.md`/`GOVERNANCE.md` stays meaningful.

**Not a copy — a conversion**: `type`/`state`/`next_action` reclassified into the new model together
(not independently); `short_description` brought into the title-shape rule; `context`/`comment`/
`resolution` **diffed** from the old cumulative-snapshot shape into true deltas, not copied forward as
one growing blob; `from_id`/`related_activity` inferred wherever the old free text already implies a
relationship (the `#648` chain, the `#712` cascade); cross-source references (`#6` citing `#753`)
must resolve correctly post-replay.

**Data quality**: every blank field checked against `BUILD.md`'s own record before being accepted as
genuinely blank — the DB's record may itself be incomplete; this is a real chance to recover what it
lost, not just reproduce the gap.

**Process**: `iba/app/migration/rebuild_escalation_from_export_20260821.py`, reading both sources,
posting every Raise/Update through `Escalation.ps1` itself (the real front door, exercising every live
validation). **Two phases**: (1) dry run — produces a reviewable proposed-conversion report, writes
nothing; (2) execute — only after the dry run is reviewed and corrected.

**Configs touched**: none — a data/process exercise using existing mechanisms, not a config change.

### D2 — stale `cfg_table.use` text
```
escalation.use: "One row per item, CURRENT STATE ONLY. NOT redundant with escalation_history --
history stores true per-version deltas (most fields NULL per row); escalation is the only place the
full current state is materialised. Ids continue from escalations_old's max (735) once D1's rebuild
lands."

escalation_history.use: "One row per update to an item, ever -- append-only, a TRUE DELTA per
version (NULL unless that version's own transaction set the field), not a full snapshot. Envelope
fields always populated; content fields NULL unless touched this version. escalation is the
current-state materialisation of the latest row here, not the reverse."
```
Via `configmaint.propose`, 2 rows updated. Re-confirm the "continues from 735" clause after D1 lands.

### D3 — crash-escalation control + the wrapper's own revision

New `cfg_utility` columns: `crash_escalation_reviewed INTEGER NOT NULL DEFAULT 0`,
`crash_escalation_note TEXT` — plus their own `cfg_column` rows. Rollout: one real pass over every
active module, each getting `reviewed=1` and a genuine note, not bulk-defaulted. `escalation.py`'s
own crash-wrapper is itself one of the rows this rollout has to walk through — not exempt — and needs
updating to set `from_id` to whatever item a failing command was operating on, once `from_id` exists
(D14).

### D4 — report registration, all 15 rows (CSV corrected)

`cfg_work_package` (1): `name='escalation-reporting'`, `ps_script='iba/app/ps/Escalation.ps1'`,
`runs_over='none'`, `chained=0`.

`cfg_step` (2): `escalation.list`/`escalation.history`, `work_package='escalation-reporting'`,
`kind='utility'`, handlers `iba.app.handlers.reports:escalation_list`/`:escalation_history`
(matching where every other misc. report handler already lives).

`cfg_report` (2): `escalation.list` (`title='Open escalations'`, `output_kind='md+csv'`),
`escalation.history` (`title='Escalation deep history'`, `output_kind='md'`, no CSV — one item's
narrative, not tabular).

`cfg_report_section` (9): 7 for `escalation.list` (`open_items`, `cycle`, `dangling`,
`mismatched_pairing`, `missing_link`, `incoherent_link`, `recently_resolved`); 2 for
`escalation.history` (`item_history`, `downward_chain`).

`cfg_report_csv_table` (1) — **corrected**: `step='escalation.list'`, `table_name='escalation'` (the
**raw table**, unprocessed), `virtual=0`. The exception categories are report *sections* (markdown),
never CSV content — that was backwards in the first draft, fixed.

### D5 — `GOVERNANCE.md` content list (10 items)

1. Current-state/history split, true-delta model.
2. State-derivation engine (`cfg_escalation_transition`).
3. Field-requirement engine (`cfg_escalation_requirement`).
4. Two-stage approval — **authority-based** (per D25's correction), not same-party.
5. Five-type model and per-type behaviour, once built.
6. `from_id`/`related_activity`, once built.
7. `chat_routing` — both extensions (2026-08-16 original, 2026-08-20 symmetric, 2026-08-21 verbatim-
   quote), already live in config, could be written today independent of the rest.
8. This register's own "configs touched" discipline — worth its own `governance.*` statement so it
   doesn't lapse the way the standing-tracker pattern already did once.
9. The produced-documentation-task pattern (D18) and verbatim-quote convention (D19), once each has
   its `cfg_escalation` row.
10. The "start work" / raised-state-guard rule (D26).

Placement: a new dedicated section, number TBD against the live file's current highest.

### D7 — `cfg_utility.escalation.purpose`
```
"escalation.py -- util.escalation. The authoritative record of open items in the project: errors,
issues, and building tasks. All runtime errors are reported in it; both Claude and Researcher record
emerging issues, tasks, followups as feedback or to get feedback. It pauses a running process and
allows it to resume at resume_point when answered (dispatcher-tied), or tracks a backlog item through
raise/update (manual). Five types (task/issue/notice/run_error/config), each a distinct shape of
life -- see USER-GUIDE.md sec4."
```
Via `configmaint.propose`, 1 row.

### D14 — `from_id`/`related_activity` mechanism

New column: `escalation.from_id INTEGER NULL` + `cfg_column` row (use text given in v7).

New `cfg_escalation_requirement` rows (4): `from_id` exists (when set) · `from_id` ≠ self (when set)
· `related_activity` paired with `from_id` · `from_id` paired with `related_activity` (both
directions checked).

### D15 — report exceptions
Fully covered by D4's `cfg_report_section` rows — nothing additional. A tunable threshold for the
incoherent-link heuristic would be a follow-on `cfg_setting`, **only if** D1's dry run shows it's
actually needed — not built ahead of that evidence.

### D16 — `run.py` re-plumbing
Not a separate config decision — D4's rows *are* the re-plumbing. Purely a sequencing question: build
now or hold.

### D18 — produced-documentation-task pattern (absorbs D20)
```
rule_key: 'issue_decisions_produce_documentation_tasks'
rule_text: 'When an issue is set to next_action=decided [now: approved, per D11/D21's reuse of the
  manual vocabulary] and its resolution states a new or changed project/governance rule, or when a
  task changes user-facing app behaviour, the party closing it out raises a companion task (from_id
  pointing back, related_activity naming the document it updates) to update the owning document --
  GOVERNANCE.md for a rule change, USER-GUIDE.md for user-facing behaviour -- in the same turn, not
  left to be remembered separately. A code change'"'"'s BUILD.md entry remains governed independently
  (governance.build_md_on_code_change); this rule covers the documentation obligations that rule does
  not.'
```
**Note**: the bracketed correction above is new this consolidation — D18's original wording (v3) still
said `next_action=decided`, which no longer exists after D11/D21's simplification; corrected here to
`approved`, the actual terminal value an issue now reaches.

### D19 — chat-capture verbatim-quote convention
Appended to the existing `cfg_escalation.chat_routing` row: *"Extended 2026-08-21: content captured
under this rule is recorded with the operative instruction or correction quoted VERBATIM... Claude's
own connective framing may surround it, clearly distinguishable from the quoted part."*

### D23 — keep PS, fix the dispatch
Recommendation given, not yet confirmed. Same config as D4/D16 — nothing additional if approved.

### D25 — authority-based approval (fixes shipped code)
`ready_for_approval` = readiness check (resolution present). `approved` = authority check (does this
party hold authority), not identity difference. Fix: `update()`'s same-party refusal replaced with a
check against `next_action_assigned_to` as set by the `ready_for_approval` transaction — whoever it
names may approve. New `cfg_escalation_requirement` row: `action='ready_for_approval'`,
`field='resolution'`, `condition_key='always'` (moves the readiness check earlier; the existing
`approved`/`resolution` row stays as the confirming re-check).

### D26 — work cannot land on a `raised` item
New `cfg_escalation_requirement` row (new `check_kind`, `not_raised_with_content`):
`action='update'`, `field='state'` — refuses any `comment`/`context`/`tried` write that would leave
the resulting state at `raised`. New `cfg_escalation` row, `rule_key=
'chat_start_work_moves_to_in_progress'`: the researcher saying "start work" means the next Update on
that item carries `-State in-progress`, before content is generated — session-practice half, honestly
distinguished from the mechanically-enforced guard.

### D27 — `ready_for_approval`'s missing transition rule
New `cfg_escalation_transition` row: `priority=5`, `shape='manual'`, `next_action='ready_for_approval'`,
`condition_key='always'` → resolves to `re-assigned` regardless of whether the assignee happened to
change this call. Existing generic `assignee_changed` (was priority 5) and catch-all (was priority 6)
shift to 6 and 7.

### D28 — PS `ValidateSet` drift check
A new `cfgquality.py`-style function comparing `Escalation.ps1`'s hardcoded `ValidateSet` literals
against the live `cfg_enum` values, run as part of `configmaint.validate`. Not a dynamically-querying
`ValidateSet` — disproportionate machinery for a rarely-changing list.

---

## Parked — code fixes, not config decisions

- **D8** — `escalation_shape` orphan-check blind spot in `cfgquality.find_orphan_configs()`. → `#9`
  (on hold), not this module's own scope.
- **D22** — `Escalation.ps1` needs a top-level `trap` so a PS-side validation failure (the `#754`
  shape) records itself instead of vanishing.

---

## Retired numbers

D13, D17 (never real items — v1 numbering gaps/placeholders). D20 (folded into D18, above). D24
(self-referential, addressed by this register's own ongoing existence).
