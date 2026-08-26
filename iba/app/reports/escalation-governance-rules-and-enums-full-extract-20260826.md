# All governance rules + all enums related to escalation — live extract

> Extracted 2026-08-26 for escalation #857. Two parts, both pulled complete (every active row,
> plus every inactive row for the enum groups — inactive status is itself the finding in several
> cases below, so it is not filtered out this time).
>
> **★ 2026-08-26 CORRECTION (found tracing `iba/app/lib/escalation.py`'s own config-read path,
> filed as `escalation-scripts-config-paths-20260826.md`): §B3 below is wrong.** It checked
> `cfg_enum` for `name='escalation_next_action'` — real, and really fully inactive, but a
> **retired predecessor** (the module's own docstring says so). The code actually validates
> `next_action` against two split, fully **active** groups — `escalation_next_action_manual`
> (includes `review`) and `escalation_next_action_dispatcher`. Part A (governance rules) and B1/
> B2/B5/B6 (the other enum groups) are unaffected and stand as extracted. Corrected text is inline
> at §B3/§B4/Summary below, struck through rather than deleted.

## Part A — Governance rules related to escalation

### A1. `cfg_escalation` — the escalation module's OWN rule table (10 active rows, full text)

This is the dedicated table for escalation-module behaviour rules — every row below governs the
escalation mechanism directly, not by cross-reference.

| id | rule_key | rule_text | enforced_by |
|---|---|---|---|
| 1 | `source_classification` | The source of an escalation is one of: code-generated (value = the generating module name), raised-by-Claude, or raised-by-Researcher. A code-generated row's `source` column must include the module as the source. | `escalation.raise_` (source parameter) for the dispatcher shape; the manual-shape half is stale (named function removed in the redesign) — manual raises take `source` as a direct required parameter, no separate classification logic exists |
| 2 | `duplicate_suppression` | A duplicate of the same issue in the same state must not be raised again. | `escalation.open_duplicate` |
| 3 | `module_blocking` | Running a module registered in `cfg_utility` (or a step in `cfg_step`) is blocked while it has an unresolved escalation against it (state `raised`/`re-assign`). | `run.py:run_step()`'s third dispatch gate (escalation #646) — checks for an unresolved escalation against the exact step or owning module, refuses to dispatch. Live and wired; corrected #746 (was stale after #646 closed) |
| 4 | `resolution_precedence` | Escalation resolution takes precedence over any other activity; open items with `next_action_assigned_to='Claude'` must be addressed before other work. | session practice — **not mechanically enforced** |
| 5 | `chat_routing` | Chat discussions must be actioned through escalations. Extended 2026-08-16: any judgement call reported only in chat prose that's a genuine open question or unfinished work must get its own escalation the same turn it's mentioned — a closed, fully-reasoned decision doesn't need one. Extended 2026-08-20: applies symmetrically to researcher feedback given in chat, not just Claude's self-reported items. Extended 2026-08-21: content captured under this rule quotes the operative instruction/correction VERBATIM. | session practice — **not mechanically enforced**. A real violation was caught live 2026-08-16 (3 deferred items reported, only 1 escalated until asked) |
| 6 | `document_reference_grouping` | A package of related tasks raised as multiple rows: each records its planning document as JSON in `context`, and shares one `related_activity` string so the group can be found/worked as a unit. | **not currently enforced** — the function this named (`escalation.raise_manual`) was removed in the 2026-08-20 redesign with no replacement check |
| 7 | `full_path_file_references` | Any file mentioned in an escalation's text fields must be given as its full repo-relative path, never a bare filename — verified 2026-08-16 that "run.py" alone resolves to 5 different files in this repo. | **not mechanically checked** (free text, no reliable regex for "is this ambiguous") — writing discipline only. Researcher caught escalation #647 violating this live |
| 11 | `standing_items_survive_reset` | Any item marked to stay open until signed off must be re-raised, carrying its unresolved scope forward, in the same unit of work as any full export+wipe of the escalation table. Checked/flagged before a wipe proceeds. | session practice — **not mechanically enforced** (register v9 D6) |
| 12 | `issue_decisions_produce_documentation_tasks` | When an issue reaches `next_action=approved` and its resolution states a new/changed project/governance rule, or a task changes user-facing app behaviour, the party closing it raises a companion documentation task (GOVERNANCE.md / USER-GUIDE.md) in the same turn. | session practice — **not mechanically enforced** (register v9 D18) |
| 13 | `chat_start_work_moves_to_in_progress` | The researcher saying "start work" means the next Update on that item carries `-State in-progress` before content is generated. | **mechanically enforced** via `cfg_escalation_requirement` (`action='update'`, `check_kind='not_raised_with_content'`) — the one row in this table with real teeth |

**8 of these 10 rows say "not mechanically enforced" / "session practice."** Only `module_blocking`
(id 3) and `chat_start_work_moves_to_in_progress` (id 13, via the requirement table) are actually
checked by running code. That ratio is itself a governance fact worth naming plainly.

### A2. `cfg_setting` — `governance.escalation.*` and the module's own `escalation.*` settings

- `governance.escalation.scope` = *"all open items, discovery of anomalies, clarifications and
  other forms of escalation must be recorded in escalation using escalation rules"* — the single
  project-wide charter statement for the whole mechanism.
- `escalation.control_objectives` = *"the escalation table manages all open items, irrespective
  of source or reason -- AI or researcher raise the escalation when discovered or raised, using
  the escalation module"*
- `escalation.control_process` = *"escalations are raised, processed, and completed using the
  escalation utility module"*
- `escalation.list_report_path` = `"iba/app/reports/escalation-list.md"`
- `escalation.history_report_dir` = `"iba/app/reports"`

### A3. Other `governance.*` settings that name escalation as part of a different rule's mechanism

These are not escalation-specific rules — they're project-wide governance rules that happen to
route their own violation-handling or completeness check through escalation:

- `governance.reports_must_persist` — a report step with nowhere to persist "is not sufficient" on
  its own; escalation is named as insufficient too (persistence is required in addition).
- `governance.rules_must_be_config_driven` — *"Any deviation discovered requires escalation."*
- `governance.table_columns` — *"Deviation from the rules must be escalated."*
- `governance.project_lookups_and_naming_convensions` — *"a missing definition must be escalated."*
- `governance.prose_canonical_authority` — references "escalation pending" for chapters 4-6 (a
  live pointer to escalation #739, on-hold).
- `governance.engineering_documentation_folder` — references escalation #650's filing review as a
  parked, related item.
- `governance.module_utility_test_plan` — test results go "in the build's escalation resolution,
  not just asserted."

### A4. `cfg_behaviour_rule` — rows genuinely ABOUT the escalation mechanism (not merely sourced from one)

| id | class | rule_key | governs |
|---|---|---|---|
| 21 | chat | `chat-items-become-escalations` | Pointer restating `cfg_escalation.chat_routing` at the chat behaviour-class level — deliberately not a duplicate, per `documentation.single-authority-pointer-not-copy`. |
| 40 | development | `open-items-route-through-escalation` | The non-chat general case of the same principle — any open item found anywhere (code review, validation run, doc sweep) goes into `escalation`, not a silent fix. |
| 42 | development | `user-guide-updated-same-unit-of-work` | Not escalation-specific itself, but cites escalation #732/#715 as its origin and names the same "same unit of work" discipline this table's own id-12 rule uses. |
| 43 | development | `every-active-ps-script-dispatches-through-run-py` | Names `Escalation.ps1`'s `-Action Raise/Update/AnswerRun` as one of only 2 permanent, architectural exceptions to the run.py-dispatch rule (a deliberate manual front door onto the backlog workflow) — its `-Action List/History` DO dispatch through run.py. |
| 45 | development | `decision-required-answered-via-update-not-answerrun` | Directly governs escalation reply mechanics: `AnswerRun`'s flat vocabulary is refused for both `resolution_kind` values; `decision_required` must go through `Update`'s richer vocabulary. Mechanically enforced in `answer_for_run()`. |
| 46 | development | `test-plan-per-module-utility` | Not escalation-specific, but its own enforcement text says test results belong "in the build's escalation resolution." |

Two more rows (`llm_output.cost-cap-before-call` id 7, `llm_output.never-expose-api-key` id 10)
mention escalation only in passing ("escalate for approval," "not... in an escalation payload")
— included in the search but not really rules *about* escalation. Two further rows (`sqlite.
wa-session-research-flags-retained-as-is` id 47, `sqlite.prose-section-session-a-replace-author-
gate` id 52) merely cite an escalation number (#833, #836) as their origin — also not rules about
the mechanism itself. Excluded from the table above for that reason, noted here for completeness
since the search matched them.

## Part B — All enums related to escalation (every value, active AND inactive)

### B1. `escalation_state` — 12 values total, 8 active, 4 inactive (retired, same ordinal slots reused)

| value | ordinal | active? |
|---|---|---|
| raised | 0 | ✓ |
| answered | 1 | ✗ retired |
| re-assign | 1 | ✗ retired |
| on-hold | 2 | ✓ |
| paused | 2 | ✗ retired |
| closed | 3 | ✓ |
| retracted | 3 | ✗ retired |
| withdraw | 4 | ✓ |
| completed | 5 | ✓ |
| in-progress | 6 | ✓ |
| supersede | 7 | ✓ |
| re-assigned | 8 | ✓ |

Note: the retired values share ordinal numbers with their live replacements (`answered`/
`re-assign` both at 1, `paused` at 2 alongside `on-hold`, `retracted` at 3 alongside `closed`) —
consistent with each retired value being superseded by the one now occupying a nearby active slot
(pre-redesign vocabulary), not a live collision (inactive rows are excluded from validation).

### B2. `escalation_type` — 9 values total, 5 active, 4 inactive (same reuse-of-ordinal pattern)

| value | ordinal | active? |
|---|---|---|
| prompted | 0 | ✗ retired |
| task | 0 | ✓ |
| interactive | 1 | ✗ retired |
| run_error | 1 | ✓ |
| issue | 2 | ✓ |
| report-stop | 2 | ✗ retired |
| crash | 3 | ✗ retired |
| notice | 3 | ✓ |
| config | 4 | ✓ |

### B3. ~~`escalation_next_action` — 8 values, ALL 8 marked inactive — sharpest finding of this extract~~ CORRECTED: that group is a retired predecessor; the LIVE groups are fully active

| value | ordinal | active? |
|---|---|---|
| approve | 0 | ✗ |
| reject | 0 | ✗ |
| revise | 1 | ✗ |
| noted | 2 | ✗ |
| hold | 3 | ✗ |
| review | 5 | ✗ |
| ready_for_approval | 6 | ✗ |
| approved | 7 | ✗ |

This table is accurate as data — `escalation_next_action` really is 8-for-8 inactive. **The error
was treating it as the live enum.** It is a retired, superseded group (confirmed by
`iba/app/lib/escalation.py`'s own docstring: *"`escalation_next_action` (the old merged cfg_enum)
is retired"*). The code actually validates `next_action` against two split groups, checked live,
**both fully active**:

| Group | Values | Active |
|---|---|---|
| `escalation_next_action_manual` | `ready_for_approval`, `approved`, `reject`, `revise`, `noted`, **`review`** (ordinal 5) | **6 of 6** |
| `escalation_next_action_dispatcher` | `approve`, `reject`, `revise`, `hold`, `noted` | **5 of 5** |

~~24 of 132 current rows sit at `next_action='review'`, set 310 times historically, the single
most-used value with its whole backing enum switched off.~~ The row counts (24/132, 310 historical
sets) are accurate and unaffected — what's wrong is the conclusion drawn from them. `review` is a
**live, actively-validated** enum member being used exactly as the config says it may be. There is
no enum-level gap here at all.

### B4. `escalation_answer` — 3 values, all inactive — a fully retired predecessor group (unaffected by the correction)

`approve`/`reject`/`revise`, all inactive. This group's own retirement claim stands regardless of
the B3 correction — it names `escalation_next_action` as its successor, and that succession is
real; `escalation_next_action` was itself later superseded again by the
`_manual`/`_dispatcher` split, a second retirement B3 originally missed. Three generations of the
same vocabulary: `escalation_answer` → `escalation_next_action` → `escalation_next_action_manual`/
`_dispatcher` (live).

### B5. `escalation_assignee` — 2 values, both active, correctly maintained

`Claude`, `Researcher` — backs `next_action_assigned_to` and `originator`. No issues found.

### B6. `resolution_kind` — 2 values, both active, correctly maintained

`decision_required`, `self_correctable` — backs the `resolution_kind` column. No issues found.

## Summary (corrected)

Of the 8 enum groups touching the escalation table (6 originally listed + the 2 live
`_manual`/`_dispatcher` groups the B3 correction surfaced), **6 are fully live and clean**
(`escalation_assignee`, `resolution_kind`, `escalation_next_action_manual`,
`escalation_next_action_dispatcher`, plus `escalation_state`/`escalation_type`'s live values), and
**2 named vocabularies are genuinely, correctly retired** (`escalation_answer` and
`escalation_next_action` itself — both real predecessors, not live gaps). There is **no** enum
group backing this table that is inactive while still governing live behaviour — the "2 entirely
inactive while in heavy use" claim in the original summary was the same error as B3 and is
withdrawn. Of the escalation module's own 10 governance rules (`cfg_escalation`), 8 are still
correctly found to be self-documented as "not mechanically enforced" — Part A is unaffected by
this correction. The corrected overall shape: the escalation mechanism's *documentation* of its
own rules (`cfg_escalation`, `cfg_column.use`) is thorough, its *enum validation* is more
completely live than this report first found, and the *mechanical enforcement of process rules*
(as opposed to value validation) remains genuinely sparse — most of what governs this module's
day-to-day behaviour is still session practice, not config-checked code, but that claim rests on
Part A, not on the enum findings this correction retracts.
