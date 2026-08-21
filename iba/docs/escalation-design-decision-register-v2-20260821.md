# Escalation design — decision register (v2, 2026-08-21)

Supersedes [`escalation-design-decision-register-v1-20260821.md`](escalation-design-decision-register-v1-20260821.md).
v1's real failure, named directly: it listed decisions without the actual configs each one touches —
so acting on any row still meant going back to invent the concrete detail on the fly, exactly the
failure this whole document exists to prevent. Every row below now carries a **Configs touched**
field: **(a) new** config rows/columns, **(b) validate** — existing config confirmed still correct,
**(c) remove** — redundant config retired. Where the answer is "none," that's stated explicitly, not
left blank.

**Done to this standard this round: D1, D3, D4, D5, D6** — the five named directly. **Not yet
brought to this standard: everything else** — stated honestly as still owing this treatment, not
padded to look complete. Bringing the rest up to this bar is its own piece of work, not done here
by assertion.

---

## D1 — Rebuild the escalation table from the JSON export, converted, not copied

**Corrected understanding**, replacing v1's flat "reseed the id sequence":

- Source: `iba/app/db/archive/escalation-export-20260820.json` /
  `escalation_history-export-20260820.json` (24 + 96 + 1 rows — the interim-redesign-era items,
  live 2026-08-19/20 before this session's reset). **`escalations_old`'s 735 rows are NOT touched or
  rebuilt** — frozen archival, stays as-is.
- The id sequence is reseeded to 735 **first**, so replay lands the exported items back on their
  original numbers (every `#7xx` citation across `BUILD.md`/`GOVERNANCE.md` stays meaningful).
- **Not a data copy — a conversion.** Every exported item gets re-expressed in the *new* model: new
  `type` classification (task/issue/notice/run_error/config, per the model confirmed this session),
  new state machine, `short_description` brought into the title-shape rule if it violates it,
  `from_id`/`related_activity` set wherever the export's own free-text already implies a relationship
  (the `#648`-series chain, the `#712` cascade — real conversion targets, not left flat).
- **Process, using the real code path, not a raw insert:** a one-off processor
  (`iba/app/migration/rebuild_escalation_from_export_20260821.py`, following the naming convention
  every other one-off migration in this session used) reads the export chronologically per item,
  and for each one:
  1. Builds a `-Action Raise` call from the item's v1 state (its `short_description`, `type`,
     `source`, `comment`) — converted to the new model's requirements.
  2. Builds a `-Action Update` call per subsequent history row, replaying the sequence of decisions
     in order.
  3. **Posts every call through `Escalation.ps1` itself** — the actual front door, not a direct DB
     write — so the rebuilt data has to pass every live validation the new design enforces, and the
     rebuild doubles as a real stress test of the new mechanism against real historical complexity.
- **A review checkpoint before execution**: the processor's first pass produces a **proposed
  conversion table** (old fields → the Raise/Update calls it intends to post, one row per item) as a
  report, not executed yet — the type-classification and `from_id` inference specifically need a
  human check before 24 items get committed under a possibly-wrong conversion, matching this whole
  session's design-before-build discipline.

**Configs touched:** **(a) new** — none. **(b) validate** — none beyond what's already built (the
conversion exercises existing `cfg_escalation_transition`/`cfg_escalation_requirement` rows as
written, doesn't add to them). **(c) remove** — none. This is a data rebuild using the standard code
path, not a configuration change.

---

## D3 — A real control mechanism for "every module reviewed for crash auto-escalation"

**Corrected from "build it everywhere" to an actual tracked mechanism**, per the researcher's
"checkbox against every registered module... to show it was considered and fixed if needed (and what
was fixed)":

- **New columns on `cfg_utility`**: `crash_escalation_reviewed INTEGER NOT NULL DEFAULT 0` (the
  checkbox) and `crash_escalation_note TEXT` (what was found — "already has a wrapper," "added one,"
  "N/A — no CLI entry point," etc.). Queryable: *"how many of N active modules reviewed"* becomes a
  one-line `SELECT`, not a manual scan.
- Rollout: one pass over every active `cfg_utility` row (397 total, ~39 active non-exempt per this
  session's own earlier count), each one gets `crash_escalation_reviewed=1` and a real note once
  actually checked — not defaulted to 1 in bulk, which would just relabel the same blind spot.

**Configs touched:** **(a) new** — 2 new columns on `cfg_utility` (`crash_escalation_reviewed`,
`crash_escalation_note`), each needing its own `cfg_column` row (`governance.table_columns` applies
to every column of every table, including this one) — 2 new `cfg_column` rows follow directly from
the 2 new columns. **(b) validate** — `cfg_utility`'s own `cfg_table.use` text needs a one-line
addition once these land, so it isn't immediately stale the way `escalation`'s was (`#4`). **(c)
remove** — none.

---

## D4 — The exact config rows for registering `escalation.list`/`escalation.history`

**v1 named the mechanism; this is the actual content**, checked against live schema this round
(`cfg_work_package`: `name, ps_script, runs_over, chained, complete_message, next_step_hint,
paused_message, inactive`; `cfg_step`: `work_package, ordinal, step, handler, scope, does, inactive,
kind`; `cfg_report`: `step, title, show_toc, footer_text, output_kind, naming_scheme, archive_dir,
inactive`; `cfg_report_section`: `step, ordinal, section_key, heading, toc_label, include,
inactive`) — real examples (`log-retention`/`retention.report`) modelled from, not guessed:

**`cfg_work_package`** (1 new row):
```
name='escalation-reporting'  ps_script='iba/app/ps/Escalation.ps1'  runs_over='none'  chained=0
complete_message=NULL  next_step_hint=NULL  paused_message=NULL  inactive=0
```

**`cfg_step`** (2 new rows) — handler functions land in `handlers/reports.py`, the existing home for
every other miscellaneous report (`retention_report`, `table_export`, etc. all live there — matching
that convention rather than a new file):
```
work_package='escalation-reporting'  ordinal=0  step='escalation.list'
handler='iba.app.handlers.reports:escalation_list'  scope='none'
does='open-items report, full history inline per item, grouped by related_activity'
kind='utility'  inactive=0

work_package='escalation-reporting'  ordinal=1  step='escalation.history'
handler='iba.app.handlers.reports:escalation_history'  scope='none'
does='deep-history report for one item, downward chain via from_id, plus the report-time exception checks'
kind='utility'  inactive=0
```

**`cfg_report`** (2 new rows):
```
step='escalation.list'     title='Open escalations'          show_toc=1  footer_text=NULL
  output_kind='md+csv'  naming_scheme='stable'  archive_dir='archive'  inactive=0
step='escalation.history'  title='Escalation deep history'    show_toc=1  footer_text=NULL
  output_kind='md'      naming_scheme='stable'  archive_dir='archive'  inactive=0
```
(`history` gets no CSV — it's one item's narrative, not a tabular export; the exception rows are a
`list`-level concept.)

**`cfg_report_section`** (7 rows for `escalation.list`, 2 for `escalation.history`):
```
escalation.list  0  open_items           '## Open items'                          include=1
escalation.list  1  cycle                '## Exception: cycle detected'           include=1
escalation.list  2  dangling             '## Exception: dangling reference'       include=1
escalation.list  3  mismatched_pairing   '## Exception: incomplete pairing'       include=1
escalation.list  4  missing_link         '## Exception: missing link'             include=1
escalation.list  5  incoherent_link      '## Exception: incoherent link'          include=1
escalation.list  6  recently_resolved    '## Recently resolved (last 15)'         include=1

escalation.history  0  item_history      '## Item history'                       include=1
escalation.history  1  downward_chain    '## Downward chain'                     include=1
```
(`toc_label` = the heading text minus the `##`, per the pattern every existing report uses —
omitted above for width, not undecided.)

**`cfg_report_csv_table`** (1 row):
```
step='escalation.list'  table_name='escalation_exceptions'  join_note='this run''s flagged exceptions across all five categories'
  inactive=0  virtual=1
```
**Flagged honestly, not asserted with false confidence**: `virtual`'s exact semantics (a computed
export vs. a literal table dump) haven't been confirmed against `reportkit`'s CSV-export code this
round — needs that check before this row is actually written, not guessed here.

**Configs touched:** **(a) new** — 1 `cfg_work_package` row, 2 `cfg_step` rows, 2 `cfg_report` rows,
9 `cfg_report_section` rows, 1 `cfg_report_csv_table` row — 15 new config rows total, all listed
above verbatim, not summarised. **(b) validate** — `cfg_write_grant`: confirmed no new grant needed,
these are read-only report generators, not writers. **(c) remove** — none.

---

## D5 — What `GOVERNANCE.md` actually needs, enumerated

**v1 said "open." Here's the list**, cross-checked against what's genuinely undocumented there
(confirmed by direct search this session — zero hits for any of these terms):

1. The current-state/history split and the true-delta model (why `escalation_history` isn't a
   snapshot).
2. The state-derivation rule engine (`cfg_escalation_transition`) — what it is, how priority-ordered
   evaluation works, per shape.
3. The field-requirement rule engine (`cfg_escalation_requirement`).
4. The two-stage approval separation-of-duties check.
5. The five-type model and per-type lifecycle differences, **once D9/the type model is actually
   built** (not before — `GOVERNANCE.md` documents live config, not a pending design).
6. The `from_id`/`related_activity` relationship mechanism, same caveat — once built.
7. This session's `chat_routing` extension (researcher-side capture) — already live in config now,
   so this one genuinely could be written today, independent of anything else in this plan.

**Placement**: a new dedicated section, alongside the existing treatment `configmaint.propose`
already gets a few sections away — the exact section number needs checking against the live file's
current highest number, not invented here.

**Configs touched:** **(a) new** — none (this is a documentation update, not a config change — it
documents config already built or about to be). **(b) validate** — every config-driven mechanism
named above gets re-confirmed live-correct at the point `GOVERNANCE.md` is actually written, not
assumed unchanged from when this register was drafted. **(c) remove** — none.

---

## D6 — The actual config for "a standing tracker survives a reset"

**v1 marked this DONE because `#6` exists. The researcher's point: existence isn't the same as a
rule that guarantees it happens again next time.** Proposed, concrete, not yet built:

**New `cfg_escalation` row:**
```
rule_key: 'standing_items_survive_reset'
rule_text: 'Any item explicitly marked to stay open until signed off (a standing tracker -- a
  review, audit, or multi-round work item) must be re-raised, carrying its unresolved scope forward,
  in the SAME unit of work as any full export+wipe of the escalation table -- never left implicitly
  closed by the wipe itself. Before a wipe proceeds, open standing items are checked for and flagged
  if found, not silently carried away with everything else.'
enforced_by: 'not yet mechanically checked -- session practice only, same honest category as
  resolution_precedence/chat_routing'
active: 1
```

**Configs touched:** **(a) new** — 1 new `cfg_escalation` row (verbatim above). **(b) validate** —
none. **(c) remove** — none.

---

## Everything else (D2, D7, D8, D9–D24)

**Not yet brought to this standard.** Stated plainly rather than padded: each of these still needs
the same "configs touched, concretely, a/b/c" treatment before any of them is genuinely buildable
without going back to invent detail on the fly. Doing all of them to this depth in one pass risks the
opposite failure — rushed, under-checked entries that look complete but aren't. This is the next
piece of work, not assumed done by writing this sentence.

| # | Decision point | Status |
|---|---|---|
| D2 | Fix stale `cfg_table.use` text | OPEN — configs touched not yet detailed |
| D7 | `cfg_utility.escalation.purpose` still narrow | OPEN — configs touched not yet detailed |
| D8 | `escalation_shape` orphan-check blind spot | OPEN, out of scope (→ `#9`) |
| D9 | Five-type model | **SETTLED** |
| D11/D21 | Complete vocabulary (`next_action`×`state`×`type`) | OPEN — proposed in v4, not yet confirmed, configs touched (new `escalation_next_action_issue` enum) named there but not itemised to this standard |
| D12 | Type-keyed Raise defaults | **SETTLED** |
| D14 | `from_id`/`related_activity` | **SETTLED** |
| D15 | Five report exception categories | OPEN |
| D16 | `run.py` re-plumbing scope/timing | OPEN |
| D18 | Produced-documentation-task pattern | OPEN — proposed in v4, configs touched not yet detailed |
| D19 | Chat-capture convention | OPEN — proposed in v4 as a `cfg_escalation.chat_routing` addition, wording not yet drafted verbatim the way D6's was |
| D22 | PS front-door crash-safety-net gap | OPEN |
| D23 | Keep PS, fix the dispatch | OPEN — recommendation given, not yet a decision |
