# Escalation design — decision register (v3, 2026-08-21)

Supersedes [`escalation-design-decision-register-v2-20260821.md`](escalation-design-decision-register-v2-20260821.md).
This round: D1 substantially widened (a second source, real data-quality work, a dry-run step); D3
answered; D4 corrected (the CSV/report split was backwards); D5 widened (the chat-behaviour/session
rules were missing entirely); **every remaining row now brought to the same "configs touched"
standard**, per direct instruction to continue down the track.

---

## D1 — Rebuild, widened: two sources, real data-quality work, a dry run first

**Corrected, per this round's review — three things v2 missed:**

1. **A second source, not accounted for at all**: the ~10 rows now live in `escalation` (`#1`–`#9`+),
   created *this session*, against the id sequence that was reset to 0 during today's testing. These
   are not in the JSON export (they postdate it) and are not `escalations_old` (they postdate that
   too) — they're real, current design-thread content (`#6` alone carries this whole conversation's
   working record) sitting on numbers that will collide with nothing *today* but represent a second,
   disconnected numbering epoch that has to be reconciled, not left as-is or silently dropped when
   the table gets rebuilt.
2. **Cross-source relations must survive the rebuild.** `#6`'s own text references `#753`, `#746`,
   `#755` — all in the JSON export. Once both sources are replayed through the standard code path in
   true chronological order (`escalations_old` end → JSON-export items → this session's own items),
   `#6`'s eventual `from_id`/text references to those items must resolve to whatever id they land on
   after replay — which, if the export replays first and lands back on its original numbers, means
   this session's own items become `#760`+ (or wherever the export's range actually ends), not
   restarting at `#1`. The rebuild plan needs this stated as an explicit **ordering + cross-reference
   integrity requirement**, not just "replay everything."
3. **`context`/`comment`/`resolution` must be *restructured*, not carried across as-is.** The
   JSON-exported items were written under the *retired* full-cumulative-snapshot design — every
   history row holds the whole running text, not a delta. Converting into the new true-delta model
   means **diffing consecutive versions** to recover what each version actually *added*, not copying
   the cumulative blob forward version by version (which would just re-create the old, wrong shape
   inside the new schema). This is real per-item text-processing work, not a field rename.

**Data quality, not just structure — per the instruction to question every blank, not assume it's
correct:**
- Missing/blank `resolution` on an item that's actually `completed` needs checking against
  `BUILD.md`'s own session-log record for that period before being accepted as genuinely blank —
  the DB's own record may itself be incomplete, and the rebuild is a real opportunity to recover what
  the DB lost, not just faithfully reproduce its gaps.
- Every `context.reference_doc` pointer gets verified to still resolve to a real file, not carried
  forward broken.
- `next_action`/`state`/`type` conversion per item needs the vocabulary mapping made explicit (old →
  new), and — per this round's note — genuinely affects **all three fields together per item**, not
  independently; a wrong `type` classification changes which state-machine the converted item's
  history has to make sense against.

**Adopted: a dry run before any commitment**, exactly as suggested. Two phases, not one:
- **Phase 1 (dry run)**: the processor reads both sources, proposes the full conversion (type, state,
  `next_action`, restructured `context`/`comment`/`resolution`, `from_id` inference, id-landing per
  item) as a **report**, nothing written. This is expected to surface design gaps the plan hasn't
  found yet — treated as a real test of the design, not a formality before a rubber stamp.
- **Phase 2 (execute)**: only after the dry-run report is reviewed and corrected, the same processor
  re-runs and actually posts through `Escalation.ps1`.

**Configs touched:** **(a) new** — none. **(b) validate** — none. **(c) remove** — none. Still a
data/process exercise, not a config change — restated because it's genuinely true, not skipped.

---

## D3 — Answered: does the crash-escalation routine itself need revision, and is it tracked?

**Yes, on both counts, not previously checked.**

- **`escalation.py`'s own `main()` crash-wrapper needs updating for everything else in this plan**:
  once `type`/`from_id` are real, a CLI crash should probably set `from_id` to whatever item the
  failing command was operating on (an `Update`/`AnswerRun` failure clearly relates to the item it
  named), not raise a fully disconnected standalone item the way it does today. Not previously
  identified — found by asking exactly the question the researcher raised.
- **Is it tracked?** No. The crash-wrapper is a piece of `escalation.py` itself, not a separate
  `cfg_utility` row — there's nothing for the D3 checkbox to attach to individually. **Resolution**:
  the checkbox tracks per-*module*, and `escalation.py`'s own `cfg_utility` row is where this gets
  recorded once reviewed — not a gap in D3's design, a reminder that `escalation.py` is itself one of
  the ~39 rows D3's rollout has to actually walk through, not exempt just because it's the module
  that inspired the rule.

**Configs touched:** **(a) new** — none beyond D3's original two `cfg_utility` columns (v2) — this
module's row gets `crash_escalation_reviewed=1`, `crash_escalation_note='updated for from_id
awareness — see BUILD.md §NNN'` once actually done. **(b) validate** — none. **(c) remove** — none.

---

## D4 — Corrected: the CSV is the raw table, not a computed exceptions view

**Wrong in v2, corrected now**: *"the CSV export is the raw tables. The reports will sort and apply
and include exception highlights."* The exception categories (cycle/dangling/mismatched-pairing/
missing-link/incoherent-link) belong **only** in the `.md` report's own sections (already correctly
specified as 5 of the 7 `cfg_report_section` rows in v2 — unchanged) — the CSV is a straight,
unprocessed dump of the underlying table, for the researcher's own tools, not a pre-sorted or
annotated view.

**`cfg_report_csv_table` row corrected:**
```
step='escalation.list'  table_name='escalation'  join_note=NULL  inactive=0  virtual=0
```
(was: `table_name='escalation_exceptions'`, `virtual=1` — wrong on both fields, retracted, not kept
as an alternative.)

**Configs touched:** **(a) new** — the 14 rows from v2's D4 stand unchanged (`cfg_work_package` ×1,
`cfg_step` ×2, `cfg_report` ×2, `cfg_report_section` ×9) — only the 1 `cfg_report_csv_table` row
changes, as shown above. **(b) validate** — none new. **(c) remove** — none.

---

## D5 — Widened: the chat-behaviour and session-discipline rules were missing entirely

**v2's 7-item list covered the module's internal mechanics only — none of what this session actually
spent most of its time building.** Added:

8. `cfg_escalation.chat_routing`'s full current text (both the original 2026-08-16 rule and this
   session's 2026-08-20 symmetric-capture extension) — the rule that chat content must become part of
   an escalation, for both parties, is a `GOVERNANCE.md`-level statement about how this project is
   actually run, not an implementation detail of one table.
9. The "configs touched" discipline this register itself now enforces (D1–D6's new standard) — worth
   a `governance.*` statement of its own: *decisions are not considered specified until their config
   footprint is listed, new/validate/remove* — otherwise this register's own discipline has no config
   anchor and could quietly lapse the way `#753`'s standing-tracker pattern already did once.
10. The produced-documentation-task pattern (D18) and the verbatim-quote chat-capture convention
    (D19), **once each has its own `cfg_escalation` row** (proposed below) — `GOVERNANCE.md`
    documents live config, so these get written up only after, not before, those rows exist.

**Configs touched:** unchanged from v2 (a documentation update, not a config change) — the list is
just longer and more honest about what's actually in scope.

---

## D2 — Fix stale `cfg_table.use` text — exact wording, not just "fix it"

**Proposed replacement text** (a `configmaint.propose` update, 2 rows):

```
escalation.use: "One row per item, CURRENT STATE ONLY. NOT redundant with escalation_history --
history stores true per-version deltas (most fields NULL per row); escalation is the only place the
full current state is materialised. Ids continue from escalations_old's max (735) once D1's rebuild
lands."

escalation_history.use: "One row per update to an item, ever -- append-only, a TRUE DELTA per
version (NULL unless that version's own transaction set the field), not a full snapshot. Envelope
fields (state/next_action/next_action_assigned_to/originator/answered_at) always populated; content
fields NULL unless touched this version. escalation is the current-state materialisation of the
latest row here, not the reverse."
```

**Configs touched:** **(a) new** — none. **(b) validate** — 2 `cfg_table.use` rows updated via
`configmaint.propose`; re-confirm the "continues from 735" clause is actually true *after* D1 lands,
not before. **(c) remove** — none.

---

## D7 — `cfg_utility.escalation.purpose` — exact replacement text

```
"escalation.py -- util.escalation. The authoritative record of open items in the project: errors,
issues, and building tasks. All runtime errors are reported in it; both Claude and Researcher record
emerging issues, tasks, followups as feedback or to get feedback. It pauses a running process and
allows it to resume at resume_point when answered (dispatcher-tied), or tracks a backlog item through
raise/update (manual). Five types (task/issue/notice/run_error/config), each a distinct shape of
life -- see USER-GUIDE.md sec4."
```

**Configs touched:** **(a) new** — none. **(b) validate** — 1 `cfg_utility.purpose` row, via
`configmaint.propose`. **(c) remove** — none.

---

## D8 — `escalation_shape` orphan-check blind spot

**Confirmed out of this module's own scope** — a code fix to `cfgquality.py`'s `find_orphan_configs()`
(the structural-declaration exemption it grants any enum named in a `cfg_column.expectation`, without
confirming a real `.enum()` call exists). Not a config change at all — a shared-library code fix.
**Configs touched: N/A.** Stays parked for `#9` (on hold), not solved here as a side effect of
touching escalation's own tables.

---

## D11/D21 — Issue's `next_action` vocabulary — exact config rows

**New `cfg_enum` group** `escalation_next_action_issue`: `open` (0), `decided` (1), `abandoned` (2),
all active.

**New `cfg_escalation_transition` rows, shape='issue':**
```
priority=1  next_action='decided'   condition_key='has_resolution'   resulting_status_key='next_action=decided'
priority=2  next_action='abandoned' condition_key='always'           resulting_status_key='next_action=abandoned'
priority=3  next_action='open'      condition_key='always'           resulting_status_key='next_action=open'
priority=4  next_action=NULL        condition_key='assignee_changed' resulting_status_key='no more specific rule'
priority=5  next_action=NULL        condition_key='always'           resulting_status_key='__unchanged__'
```

**`cfg_status_flow` — flagged, not asserted**: `next_action=decided`/`abandoned`/`open` resolve to
the *existing* `completed`/`withdraw`/`in-progress` statuses, which already have rows for
`entity='escalation'`. Whether `cfg_status_flow`'s dedup key is `(entity, status)` (meaning the
*existing* row's `set_by` text needs extending to also mention "OR system: next_action=open (issue)"
rather than a new row) hasn't been confirmed this round — genuinely don't know without checking the
live `cfg_unique` row for that table, flagged honestly rather than guessed either way.

**Initial state at Raise, settled explicitly (not previously nailed down)**: an issue starts at
`state='raised'`, same as every other type — **not** `in-progress` immediately — because the generic
Raise default is one mechanism everything shares, and the first `next_action='open'` update (even a
trivial one) is what moves it to `in-progress`, consistent with the rest of the design rather than a
special case.

**Configs touched:** **(a) new** — 3 `cfg_enum` rows, 5 `cfg_escalation_transition` rows, `cfg_status_flow`
extension (1 row's `set_by` text edited, pending the dedup-key check above). **(b) validate** — none.
**(c) remove** — none.

---

## D15 — Report exception categories — configs touched

**Already fully specified** — the 5 `cfg_report_section` rows in D4 (v2, unchanged) *are* the config
representation; nothing additional needed. **If** the incoherent-link heuristic needs a tunable
threshold once actually tested against real data (D1's dry run is exactly where that evidence would
show up), a `cfg_setting` (`escalation.incoherent_link_min_cluster_size` or similar) would be a
follow-on, evidence-driven addition — **not built ahead of that evidence**, per
`feedback_simple_steps_not_engineered_designs`.

**Configs touched:** **(a) new** — none beyond D4. **(b) validate** — none. **(c) remove** — none.

---

## D16 — `run.py` re-plumbing scope/timing

**Not a separate config decision** — D4's 15 rows (v2/v3) *are* the re-plumbing. D16 is purely a
sequencing question: build those rows now, alongside the rest of this round, or hold them until
later. **Configs touched: same as D4, nothing additional.**

---

## D18 — Produced-documentation-task pattern — exact config row

**New `cfg_escalation` row:**
```
rule_key: 'issue_decisions_produce_documentation_tasks'
rule_text: 'When an issue is set to next_action=decided and its resolution states a new or changed
  project/governance rule, or when a task changes user-facing app behaviour, the party closing it out
  raises a companion task (from_id pointing back, related_activity naming the document it updates) to
  update the owning document -- GOVERNANCE.md for a rule change, USER-GUIDE.md for user-facing
  behaviour -- in the same turn, not left to be remembered separately. A code change'"'"'s BUILD.md
  entry remains governed independently (governance.build_md_on_code_change); this rule covers the
  documentation obligations that rule does not.'
enforced_by: 'not yet mechanically checked -- session practice only, same honest category as
  resolution_precedence/chat_routing'
active: 1
```

**Configs touched:** **(a) new** — 1 `cfg_escalation` row (above). **(b) validate** — none. **(c)
remove** — none.

---

## D19 — Chat-capture verbatim-quote convention — exact addition

**Not a new row — a further extension of the same `cfg_escalation.chat_routing` row this session
already extended once.** Appended text (via `configmaint.propose`, same pattern as before):

```
"Extended 2026-08-21: content captured under this rule is recorded with the operative instruction or
correction quoted VERBATIM (in quotation marks) inside comment/context, not paraphrased -- Claude's
own connective framing may surround it, clearly distinguishable from the quoted part."
```

**Configs touched:** **(a) new** — none. **(b) validate** — 1 `cfg_escalation.rule_text` row extended
further, via `configmaint.propose`. **(c) remove** — none.

---

## D22 — PS-side crash-safety-net gap

**A code fix** (`Escalation.ps1` gains a top-level `trap`, shelling out to record a PS-side failure
before exiting) — not a config change. **Configs touched: N/A**, correctly, not a gap in this
register.

---

## D23 — Keep PS, fix the dispatch

**Not a separate config decision** — if confirmed, implemented entirely by D4's already-specified
rows. **Configs touched: same as D4, nothing additional.**

---

## Status summary

Every row in this register (D1–D23, minus the always-N/A code-only ones D8/D22) now carries a
concrete, checked "configs touched" statement. Still genuinely open — nothing here is a decision
made, only a decision made *specific enough to act on once approved*:

D1 (widened, dry-run adopted), D2, D3 (answered), D4 (corrected), D5 (widened), D7, D11/D21 (one
unconfirmed mechanic — `cfg_status_flow`'s dedup key), D15, D16, D18, D19, D23. **Settled, unchanged:**
D6, D9, D12, D14. **Parked:** D8 (→ `#9`), D22 (code, not config, and not yet built).
