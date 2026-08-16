# Response to "iba table review" (2026-08-16)

> Source documents: [`Workflow/Chat_responses/iba table review`](../../Workflow/Chat_responses/iba%20table%20review)
> + [`Workflow/Chat_responses/export.cfg_settings shortcomings.csv`](../../Workflow/Chat_responses/export.cfg_settings%20shortcomings.csv).
> Prior context still in focus: [`project-review-response-2-20260815.md`](project-review-response-2-20260815.md),
> [`docs/governance-alignment-register.md`](../../docs/governance-alignment-register.md).
>
> **Status: EXECUTED, 2026-08-16, same day.** §§1-6 below are the original plan, written before any
> change landed — kept as-is for the record of what was reasoned through and why. The researcher's
> follow-up (`Workflow/Chat_responses/response-tablereviewresponse v1`) confirmed the open judgement
> calls and gave an explicit "build it" instruction; §7 (bottom of this file) is the execution
> record — what was actually built, run, verified, and what's still open. Everything below §1's
> heading is grounded against the **live** DB/code as queried at plan-time; §7 is grounded against
> the live DB/code as it stands after execution.

## 1. What I understand the review to be saying

1. The IBA App's `cfg_*` layer is the control mechanism for the whole project now (per
   `governance.scope_iba_app`, dated by decree from 2026-08-15) — not just IBA's own base-data
   layer. Any operation anywhere in the project, past or present, is expected to migrate under it.
2. The `governance` module inside `cfg_setting` has drifted into **incident notes** (rules written
   to explain one specific violation after the fact) rather than **standing, unambiguous rules**.
   That's identified as the root cause of me missing `governance.past_precedent_investigation_
   signals_missing_config` earlier this session-set — not a one-off reading failure, a config
   authoring problem.
3. **Escalations are being reset** before anything else, because the current shape can't carry the
   weight being put on it (three-way approve/reject/revise only, no severity/owner/priority
   routing, no duplicate suppression rule, no module-blocking rule). Everything else — the CSV's
   other rows, the backlog items, the doc propagation — is explicitly sequenced **after** that
   reset ("once this is reset, then escalations can be used to elevate all the other actions").
4. The CSV is **not** a row-by-row spec for me to transcribe. Most rows are either (a) an existing
   setting with a `new_value`/`new_use` revision already fully worded, or (b) a bare stub (key only,
   or an incomplete key like `naming.`) that the researcher is explicitly leaving to me to design
   and codify, per the review text itself ("I am not expecting to give you detail row for row...
   The app design and codification is your role with my guidance").

## 2. Grounded against the live DB (differences from the CSV's own framing)

| CSV says | Live DB actually shows |
|---|---|
| table is `cfg_settings` (CSV filename, and review prose "note new config rows in cfg.settings") | table is **`cfg_setting`** (singular) — 119 rows, columns `key, value, use, module, inactive`. Using this name in every change below. |
| "create new cfg.escalation table" | No `cfg_escalation` table exists. This is a genuinely new table — parallel to the pattern IBA already uses for other utilities (`cfg_candidate_rule`, `cfg_method_rule`), i.e. a utility's own declarative rule table, distinct from the `escalation` *data* table (which already exists and holds the 634 escalation rows themselves). |
| Rename `word`→`source`, `question`→`short_description`, `preset`→`context`, add `next_action_assigned_to`, add `answer`, add `related_activity`, widen `type`/`state` enums, add `answered_by` | The live `escalation` table already has: `id, run_id, word, at_step, type, question, preset, tried, state, answer, answered_at, raised_at, comment`. Renames map cleanly **except one collision**, flagged in §4 below: `answer` already exists and already means something else (the approve/reject/revise decision) — the CSV's "add column for answer" describing a resolution note is a **second, different meaning** for a name already in use. |
| "3 lib modules missing a cfg_utility row" (escalation #643) | Confirmed by direct diff: `iba/app/lib/*.py` (32 files) vs `cfg_utility` (29 rows) — missing are `clusterassign.py`, `clusterreport.py`, `strongreconcile.py`. |
| #591/#597 (`cfg_report_csv_table` naming bad tables) | `report.registry`'s three `cfg_report_csv_table` rows are now clean (`word_registry`, `word_registry_strong_pairing` [virtual], `word_strong`) — the bad `table_name='registry'` row is gone. **Fixed in substance**, matches the "not yet done from previous session" note that these are unclosed in *state*, not unresolved in *substance*. |
| #642 (`manifest.skip_dirs` names unknown module `manifest`) | `config_module` enum already includes `manifest` (18 values, `manifest` present). **Fixed in substance.** |
| #578/#643 ("N lib module(s) missing a cfg_utility row") | #578 was raised against `CONFIG-REPORT-v66-20260809.md` (1 missing); #643 against `CONFIG-REPORT-v66→v99-20260815.md` (3 missing) — these are the **same finding recurring**, not two different ones; #578 should retract/supersede into #643, not both stay open. |

## 3. Backlog escalations — disposition per the review's instructions

| # | State now | Review's instruction | Disposition once escalation reset lands |
|---|---|---|---|
| 575 | raised | Retract; raise "NT verse-lexicals" as a new, separate item | Retract 575 with reason; new escalation: *"No verse_lexical rows exist for any New Testament book — confirm whether NT verse-lexical build is in scope and, if so, sequence it."* Needs your confirmation this is a real gap before I raise it as fact — I haven't independently verified zero NT coverage yet (see open question in §5). |
| 576 | raised | Retract (bundled with 575) | Retract, same reason, cross-ref 575. |
| 577 | raised | Retract — "not a word to load" | Retract, reason: test/placeholder input, no action needed. |
| 593 | raised | Investigate `report.word_registry_span` producing this error class; see also 577 | `incureability` is also not a registry word — same shape as 577 (bad/test input, not a code bug). I read this as: confirm the *error handling* is correct (clean "not in registry" message, no crash) rather than a defect to fix. Will verify the handler behaves the same way for genuine typos before closing — flagging as **substance-checked, not yet formally verified**. |
| 578 | raised | Resolve through the config work | Superseded by 643 (§2) — retract 578 as a duplicate, work 643. |
| 579 | raised | Resolve through the config work | `configmaint.propose` crash ("Expecting value: line 1 column 1") — this is a genuine unhandled-exception bug (a crash, not a coherence finding), not something a cfg_setting row fixes by itself. Needs its own look at `configmaint.py`'s propose path once the escalation-table code changes are in and I'm touching that file anyway. |
| 591 | raised | Resolve through the config work | Fixed in substance (§2) — mark answered/closed once new state enum exists. |
| 597 | raised | Resolve through the config work | Fixed in substance (§2) — mark answered/closed. |
| 598 | raised | Resolve through the config work | `step.span_html`'s regex value fails `json.loads()` — a real still-open coherence bug (quoting problem in the stored setting), not resolved by anything above. Needs an actual value fix (re-quote as a JSON string) via `configmaint.propose`. |
| 626 | raised | Resolve through the config work | Same defect class as 598 (`cluster.quality_report_path` plain string not JSON-quoted) — same fix path. |
| 632 | raised | Resolve through the config work | This is a judgement-call acknowledgement (428 + 481 strongs with cluster/word_registry exceptions), not a config-mechanics bug. Per `feedback_iba_data_judgment_calls_must_escalate_not_silent_report`, this stays a live judgement escalation for you to decide (acknowledge as known-state, or investigate further) — I won't resolve it as part of the config-mechanics cleanup. |
| 642 | raised | Resolve through the config work | Fixed in substance (§2) — mark answered/closed. |
| 643 | raised | Resolve through the config work | Real, current gap — add `cfg_utility` rows for `clusterassign`, `clusterreport`, `strongreconcile` (module/file_path only; purpose text needs a real one-line description each, not a placeholder). |

Net: of the 13 open escalations, **3 retract** (575/576/577), **1 duplicate-retract** (578), **4 are
already fixed and just need formal closure** (591/597/642, plus 593 pending a quick behavioural
check), **3 are real remaining defects** (579 crash, 598/626 bad JSON quoting), **1 stays open by
design** (632), **1 gets a real fix** (643 — add the 3 rows).

## 4. Judgement calls I'm not resolving silently

These are genuine ambiguities in the CSV/review, not things I'll pick an answer for on my own:

1. **The `answer` column name collision.** Live `escalation.answer` already stores the approve/
   reject/revise/yes/no decision (read and written throughout `escalation.py`, e.g.
   `answer_for_run`, `answer_for_word`). The CSV's new "answer" column is described as *"a short
   description or reference for the action taken to resolve"* — a resolution note, not a decision
   value. My proposed resolution: keep the existing decision column as-is (rename it `decision` to
   free the name, since every other rename in this pass is already touching column names) and add
   the new resolution-note column as `resolution`. **Flagging for your confirmation before I build
   it this way** rather than assuming.
2. **The blank/stub `cfg_setting` rows** (`governance.scope_project`, `governance.startup`,
   `governance.project_databases`, the bare `governance` row, and the two duplicate-keyed `naming.`
   rows with no suffix) carry no `new_value` at all — just a date stamp. Per the review's own
   framing, these are placeholders for me to design, not transcribe. I'll draft concrete wording for
   each as part of the escalation-reset work package and put the draft through `configmaint.propose`
   (which pauses for your approval on every write) rather than invent and silently apply — that IS
   the "with my guidance" loop the review describes, just run through the app's own approval gate
   instead of a chat back-and-forth.
3. **`governance.oneoff_report_dir` new_value `"/reports/"`.** The `new_use` note says one-off
   reports move from `iba/app/reports/` to `/reports/` — read literally that's a **project-root**
   folder, i.e. one-off reports move out from under `iba/app/` entirely. That's a bigger filing
   decision (it also collides with register item #2, main-project filing rules) than a path tweak.
   Before I create a new top-level `/reports/` directory and repoint `reportkit.oneoff_path()`, I
   want to confirm that's really the intent and not a typo for `iba/app/reports/` shortened in
   your own notes.
4. **`governance.scope_research_db` says `research_db`** — the live database file is
   `bible_research.db` (`database/bible_research.db`, CLAUDE.md §3). Treating `research_db` in the
   config as shorthand for `bible_research.db`, not a third database — flagging in case that's
   wrong.

## 5. Open question (data, not judgement)

Item 575's retraction is conditioned on NT verse-lexicals genuinely not existing yet. I haven't run
that check independently — happy to before raising the replacement escalation, a one-query check
against `verse_lexical`/`book_order` (or `cfg_book_order`) for NT-testament coverage. Say the word
and I'll run it before drafting the new escalation text.

## 6. Proposed sequencing (nothing below has started)

1. **Escalation reset** — new `cfg_escalation` rule table (duplicate-suppression, module-blocking-
   on-unresolved-escalation, priority-preemption, source-enumeration rules verbatim from the
   review); `escalation` table schema migration (renames + new columns, per §4.1's proposed
   resolution); `escalation.py` updated to match (column names, the `source` module-prefix rule for
   code-generated escalations, the duplicate-suppression check, the module-blocking check); new
   `cfg_setting` rows `governance.escalation.scope` / `governance.utility.config` (verbatim from the
   review) via `configmaint.propose`.
2. **Backlog escalations** — apply §3's dispositions (retract 3, close 4, fix 3, leave 1 open,
   add the 3 `cfg_utility` rows for #643) using the reset escalation mechanics.
3. **Doc propagation** — `GOVERNANCE.md`, `BUILD.md`, `USER-GUIDE.md` updated to reflect 1–2, per
   `governance.governance_md_on_rule_change`/`build_md_on_code_change` (same unit of work, not a
   follow-up).
4. **`cfg_work_package` completeness check** — confirm no work package runs outside a registered
   `cfg_work_package`/`cfg_step` row, and that `run.py` actually checks registration (the review's
   explicit instruction: "ensure that the python run command check that the work package are
   registered").
5. **Project-wide config-driven-rule sweep** — the review's instruction to check scripts across the
   *whole* project (not just `iba/app/`) for hardcoded variables/rules/lookups that should be
   `cfg_*`-driven. This is the biggest-radius item; I'd scope it as its own register row rather than
   fold it into this pass, given `feedback_alignment_work_is_register_driven_plan_gated`.
6. **Remaining CSV rows** — the rows not already covered above (`governance.rules_must_be_config_
   driven`'s revised text, `governance.project_change_rule`, `governance.project_lookups_and_naming_
   convensions`, `governance.primary_responsibility`, `governance.programme_stages`, etc.) — apply
   via `configmaint.propose` in the same pass as step 1, since they're already fully worded in the
   CSV (not stubs).

Each of steps 1–2 above is small enough to run as one `configmaint.propose` + migration unit; I'd
suggest starting there once you confirm §4's three judgement calls, rather than waiting for the
whole sequence to be pre-approved at once.

---

## 7. Execution record (2026-08-16, same day, after the researcher's confirmation)

Your response resolved §4's three judgement calls: `answer`→`next_action` (expanded with hold/
noted) + a new `resolution` column (not `answer`/`decision` as I'd proposed); real wording for the
blank stub rows; `configmaint.propose` recalibrated as one path among several, not the default
gate. You then instructed: *"Build the new escalation structure/table/code updates so we can start
to use it."* Full build record: `BUILD.md` §113, `GOVERNANCE.md` §39. Summary:

**Built and verified end-to-end** (not just written — `raise`/`answer-run`/`list` round-tripped
through both the Python CLI and the `Escalation.ps1` PS wrapper, `configmaint.validate` run clean
before and after):
- `escalation` table retrofitted (634 rows, config-driven DDL, explicit backfill mapping — not a
  blind copy): `word`→`source`, `question`→`short_description`, `preset`→`context`,
  `answer`→`next_action` (+hold/noted); new `resolution`/`related_activity`/
  `next_action_assigned_to`/`answered_by`.
- New `cfg_escalation` rule table (5 rules) + 4 `cfg_enum` groups updated.
- 22 new + 2 revised `cfg_setting` rows (§6's stub content, plus every other fully-worded CSV
  governance/escalation row) — written directly, per your "don't make this a drag" correction.
- 3 missing `cfg_utility` rows added (escalation #643's finding).
- **Every direct writer/reader of the `escalation` table fixed, not assumed** — found by grepping
  the whole app, not just `lib/escalation.py`: `run.py` had 3 direct writes bypassing
  `lib/escalation.py` entirely (would have broken every crash/pause/report-stop path if missed),
  `handlers/registry.py`, 7 more handlers' read-sites, `lib/retention.py`, `tools/purge_word.py`
  (a real deletion tool), `migration/legacy_import.py`.
- `escalation.py` itself rewritten: new column shape, `source`-classification rule, `answered_by`
  required at every terminal state, `Escalation.ps1` widened to match (new `-Resolution`/
  `-AnsweredBy`/`-AssignedTo`/`-Type` flags, `Decision` set widened to include Hold/Noted).
- `USER-GUIDE.md` §4 rewritten to match the live behaviour (not just BUILD.md/GOVERNANCE.md).

**Two real bugs found and fixed mid-build** (not left for later): an enum-upsert bug that left
`raised` stuck inactive right after migration (`escalation.raise_manual` failed immediately —
caught by actually running it, not just reading the code back); the `escalation.run_id`→`run.run_id`
FK had never actually been checked before (enforcement is OFF app-wide) — surfaced 32 pre-existing
orphans, 27 documented-by-design, **5 genuine** (one, #579, is the same run_id as the still-open
`configmaint.propose` crash — useful lead, not yet chased).

**Backlog processed** exactly as directed in §3/your response — 11 of 13 closed (3 retracted, 2
closed as duplicates/verified-already-fixed-in-substance, 2 real JSON-quoting bugs fixed, 1 real
gap closed), #579 and #632 deliberately left open (genuine issues/judgement calls, not
config-mechanics). 6 new task escalations raised for what this surfaced but didn't do — NT
verse-lexical coverage check, `module_blocking` enforcement wiring, work-package
registration-check verification, the project-wide config-driven-rule sweep, the 5 FK orphans, and
the filing/consolidation decision (§4.3 — assigned to you, needs judgement).

**Deliberately not done in this pass** (each is its own escalation now, not silently dropped):
wiring `cfg_escalation.module_blocking` into `run.py`'s dispatcher; the `governance.oneoff_report_dir`
relocation; investigating the `configmaint.propose` crash (#579) itself; the project-wide
config-driven-rule sweep beyond `iba/app/`.

Current open-escalation count: **8** (`Escalation.ps1 -Action List` / `iba/app/reports/
escalation-list.md`).
