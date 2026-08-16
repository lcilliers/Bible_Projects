# SESSION LOG — 2026-08-16 — Escalation system reset (schema, own rule table, wider vocabulary), 22 governance `cfg_setting` rows, 13-item backlog cleared

Session opened with the standard `/start-project` orientation (STEP already up, IBA bootstrap
READY, governance-alignment register reviewed — nothing else done at that point). The substantive
work was the researcher's "iba table review" (2026-08-16) + `export.cfg_settings shortcomings.csv`
— a corrective review of how escalation/config governance had been drifting, with an explicit
"build it" instruction once the open judgement calls were resolved in chat. Full plan + execution
record: `outputs/markdown/iba-table-review-response-v1-20260816.md` (§1-6 plan, §7 execution).

## 1. Grounding the review against the live app before touching anything

Read `Workflow/Chat_responses/iba table review` + `export.cfg_settings shortcomings.csv` in full,
then checked every claim against the live DB/code rather than trusting the CSV's own framing:
table is `cfg_setting` (singular), not `cfg_settings`; the CSV's "N lib modules missing a
cfg_utility row" (escalation #643) checked out exactly — `clusterassign.py`/`clusterreport.py`/
`strongreconcile.py`; escalations #591/#597/#642 were already fixed in substance, just not
formally closed; none of the CSV's `governance.*` rows existed live yet (the CSV is an input
document, not an export of applied state). Wrote a grounded plan doc and stopped — did not execute,
per the register's plan-gated convention — flagging one real naming collision (the CSV's new
"answer" column collides with the existing decision column of the same name) and several judgement
calls (blank stub rows, the `oneoff_report_dir` relocation, `research_db`'s exact database name).

## 2. Researcher's response resolved the open calls; explicit build instruction

Read `Workflow/Chat_responses/response-tablereviewresponse v1`. Resolved: `answer`→`next_action`
(expanded with hold/noted, not just approve/reject/revise) + a new `resolution` column (not
`answer`/`decision` as originally proposed) to record what was actually done — nothing previously
captured that. Real content given for the blank stub rows (`governance.scope_project`,
`governance.project_databases`). Explicit recalibration: **`configmaint.propose`'s approve/reject/
revise gate is not the default path for every escalation** — "not all escalations goes through
propose / approved, lots of it would raise, schedule, notify... only when you really need my
agreement on choices or different approach, then channel it back to me." Instruction: "Build the
new escalation structure/table/code updates so we can start to use it. Then use escalation system
to structure the tasks for the rest of the actions."

## 3. Schema retrofit (`iba/app/migration/escalation_reset_v1_20260816.py`, BUILD.md §113)

Config-driven retrofit (same method as `retrofit_debate_lexicon_tables.py`), not hand DDL:
`escalation.word`→`source` (NOT NULL), `question`→`short_description`, `preset`→`context`,
`answer`→`next_action`; new `resolution`/`related_activity`/`next_action_assigned_to`/
`answered_by`. All 634 live rows backfilled by an explicit CASE mapping (documented inline), not a
blind copy — `type` reclassified from crash|interactive|prompted|report-stop into
task|run_error|issue|notice|config by `at_step`/word-presence pattern. New `cfg_escalation` rule
table (same shape as `cfg_method_rule`) seeded with 5 rules: source-classification,
duplicate-suppression (already enforced), module-blocking (recorded, **not yet wired**),
resolution-precedence, chat-routing. 4 `cfg_enum` groups updated. 22 new + 2 revised `cfg_setting`
rows written directly (not via `configmaint.propose`) per the researcher's "don't make this a drag"
correction — full list in the response doc §6.

**Two real bugs found and fixed mid-build, by actually running the thing, not just reading the code
back:**
1. First migration run crashed immediately post-apply: `escalation.raise_manual` errored `'raised'
   is not a member of cfg_enum 'escalation_state'`. Cause: the "mark old inactive, `INSERT OR
   IGNORE` new" enum-update pattern silently no-ops on any value shared between old and new sets —
   `raised` is valid in both, so the blanket `inactive=1` sweep left it stuck with nothing to
   reactivate it. Fixed the live row, then replaced the pattern with a real upsert
   (`ON CONFLICT...DO UPDATE`) in the migration source.
2. The retrofit's FK-check (`escalation.run_id`→`run.run_id`) surfaced 32 pre-existing orphans —
   never actually checked before (`PRAGMA foreign_keys` is OFF app-wide). 27 are the documented-
   by-design `MANUAL-*` synthetic run_ids; **5 are genuinely undocumented**
   (`#539/#550/#559/#561/#579`) — accepted (same exception class `retrofit_debate_lexicon_tables.py`
   already established), raised as its own tracked escalation rather than silently absorbed. `#579`
   shares its run_id with the still-open `configmaint.propose` crash escalation — a real lead for
   that bug's root cause, not yet chased.

## 4. Every direct writer/reader of `escalation` fixed, not assumed

Grepped the whole app for `write("escalation"`/`update("escalation"` and every `["answer"]` read —
found `run.py` writes to the table **directly**, three times (crash handler, pause-continue,
report-stop), bypassing `lib/escalation.py` entirely; the rename would have broken every one of
those paths app-wide if only the module had been touched. Fixed all three, plus
`handlers/registry.py` (`ans["answer"]=="yes"/"no"` → `ans["next_action"]=="approve"/"reject"`), 7
more handlers' `answered["answer"]` reads, `lib/retention.py` (health-report queries),
`iba/app/tools/purge_word.py` (a real deletion tool — word-scoped rows now matched via `source`),
`iba/app/migration/legacy_import.py`'s `pending` lookup. `escalation.py` itself rewritten in full;
`Escalation.ps1` widened to match (new `-Resolution`/`-AnsweredBy`/`-AssignedTo`/`-Type` flags,
`-Decision` set widened to include Hold/Noted) and smoke-tested end to end through the actual PS
wrapper, not just the Python CLI. `configmaint.validate` run clean before and after (structurally
coherent; only the 2 new `escalation.control_*` settings flagged as expected "orphan" advisories,
same class as most `governance.*` rows).

## 5. Backlog cleared (all 13 items the researcher named)

- **Retracted** (3): #575/#576 (NT verse-lexical coverage rescheduled as its own task, not answered
  inline), #577 (test/placeholder input).
- **Closed as duplicate**: #578 (same finding as #643, re-raised on a later `CONFIG-REPORT`
  regenerate).
- **Closed `noted`, verified already fixed in substance**: #591/#597 (`cfg_report_csv_table`'s bad
  `table_name` rows confirmed gone), #593 (verified clean by-design error handling — `fail
  ("word-not-found", ...)`, not a crash — same shape as #577), #642 (`manifest` confirmed present in
  `config_module` enum).
- **Closed `approve`, real fix applied**: #598/#626 (two `cfg_setting.value`s re-quoted as valid
  JSON — `step.span_html`, `cluster.quality_report_path`), #643 (the 3 missing `cfg_utility` rows
  added).
- **Left open, deliberately**: #579 (crash — real bug, not chased this session), #632 (a genuine
  judgement call, per `feedback_iba_data_judgment_calls_must_escalate_not_silent_report`).

**6 new task escalations raised** for what this surfaced but didn't do (each referencing this
session's planning doc rather than duplicating detail, per the researcher's explicit allowance):
NT verse-lexical coverage check, `module_blocking` enforcement wiring into `run.py`'s dispatcher,
work-package registration-check verification, the project-wide config-driven-rule sweep (scripts
across the whole project, not just `iba/app/`), the 5 FK orphans, and the filing/consolidation
decision from the researcher's §4.3 (assigned to the researcher — needs judgement, not a mechanical
apply).

## 6. Documentation updated in the same unit of work

`BUILD.md` §113 (full build record), `GOVERNANCE.md` §39 (the two governing corrections —
escalation's own rule table + wider vocabulary, and `configmaint.propose` recalibrated as one path
among several), `USER-GUIDE.md` §4 (rewritten to match live behaviour: new state names, new
actions, the two behavioural corrections called out up front) — per `governance.build_md_on_code_
change`/`governance_md_on_rule_change`, not deferred.

## Left open, not silently dropped

- **`cfg_escalation.module_blocking`** — rule recorded, not wired into `run.py`'s dispatcher. Own
  escalation raised.
- **`governance.oneoff_report_dir` relocation** — the CSV's proposed `/reports/` (project-root)
  move not applied; a filing decision needing the researcher's own judgement (§4.3), not a
  mechanical config write. Own escalation raised, assigned Researcher.
- **`governance.startup` and the two bare `naming.` CSV rows** — genuinely no content given; not
  invented.
- **Escalation #579** (the `configmaint.propose` crash) and **#632** (cluster-assignment exceptions)
  — real open items, not config-mechanics bugs, deliberately left for their own attention.
- **The project-wide config-driven-rule sweep** beyond `iba/app/` — scoped as its own future
  register/escalation item per `feedback_alignment_work_is_register_driven_plan_gated`, not folded
  into this pass.

## Files touched (this session)

**New code:** `iba/app/migration/escalation_reset_v1_20260816.py`.

**Rewritten code:** `iba/app/lib/escalation.py`.

**Modified code:** `iba/app/run.py` (3 direct `escalation` writes + 2 new classification helpers),
`iba/app/handlers/registry.py`, `iba/app/handlers/{candidate,cluster,configmaint,lexicon,
narrative,passage,reports}.py` (mechanical `answer`→`next_action` read-site rename),
`iba/app/lib/retention.py`, `iba/app/tools/purge_word.py`, `iba/app/migration/legacy_import.py`.

**Scripts:** `iba/app/ps/Escalation.ps1` (new flags, widened `-Decision` set).

**Docs:** `iba/app/BUILD.md` (§113), `iba/app/GOVERNANCE.md` (§39), `iba/app/USER-GUIDE.md` (§4
rewritten). `outputs/markdown/iba-table-review-response-v1-20260816.md` (plan + execution record,
new this session).

**Schema:** `escalation` table retrofitted (4 columns renamed, 4 added, all 634 rows backfilled);
new `cfg_escalation` table (5 rules seeded); `escalation`/`cfg_escalation` registered in
`cfg_table`/`cfg_column`.

**Config:** 4 `cfg_enum` groups updated (`escalation_type`, `escalation_state`,
`escalation_next_action` replacing `escalation_answer`, new `escalation_assignee`); 22 new + 2
revised `cfg_setting` rows (module `governance`/`escalation`); 3 new `cfg_utility` rows
(`clusterassign`/`clusterreport`/`strongreconcile`).

**Data:** `escalation` — 11 of 13 named backlog items closed/retracted, 6 new task escalations
raised; net open count 13 → 8.

**DB snapshot:** `iba-20260816T163904Z-escalation-reset-v1-20260816.db` (pre-migration, taken
before any schema change).

**Housekeeping:** an early ad hoc DB query accidentally created a stray empty `iba.db` at the
project root (working-directory drift between tool calls) — caught immediately (0 bytes, wrong
schema) and deleted before it could be mistaken for the real DB.

## Next

Work the 6 new task escalations as their own units — `module_blocking` wiring and the
work-package registration-check verification are the two most directly load-bearing (they close
gaps this exact session's own build depends on being real, per `governance.rules_must_be_config_
driven`'s "establish the rules are captured correctly" standard). The filing/consolidation decision
(§4.3) needs the researcher's own judgement before any doc/folder move. `Escalation.ps1 -Action
List` / `iba/app/reports/escalation-list.md` is now the live tracking surface for all of it.

## 7. Addendum, same day — `Workflow/Chat_responses/Additional configs` processed

Full record: `BUILD.md` §114, `outputs/markdown/iba-table-review-response-v1-20260816.md` §7a.
Registered the atomic-transaction/pre-run-snapshot facts (already true, confirmed live at
`GOVERNANCE.md`/`BUILD.md` §66, previously only in prose) and the NAS backup schedule (previously
main-project-only, `CLAUDE.md` §13) as 6 new `cfg_setting` rows, module `backup` — surfacing a
real, previously-undocumented gap: `iba.db` has no dedicated NAS backup+integrity script the way
`bible_research.db` does, only the whole-folder mirror as a side effect. Caught and fixed a second
real bug the same shape as #598/#626: two of the new rows' UNC paths failed `json.loads()` from
hand-escaped backslashes, caught by verifying every new row actually parses rather than assuming a
clean write. Added a new `cfg_escalation` rule (`document_reference_grouping`) formalising the
document-reference pattern this whole reset already used raising its own follow-on escalations.
Raised 6 new escalations for the remaining items in the researcher's note: migrating the
main-project `engine/` controls into IBA (scope-first — the natural first case of the project-wide
config-driven-rule sweep already tracked), `research_db` table retirement/consolidation ×3
(explicitly worded as gated on the design-audit item completing first), a standing notice against
auto-adopting old `research_db`/`engine/` routines verbatim, and the design audit itself.
`configmaint.validate` re-run clean (orphan-setting advisories 2→8, all expected — same
documentation-only class as the `escalation.control_*` rows, not a defect). Open-escalation count:
8 → 14.

## 8. Addendum, same day — `document_reference_grouping` found written but not applied by its own code

Researcher, looking directly at escalation #653: *"I notice in none of the new escalations the
column context is filled in... does the escalation script check any of the escalation configs?"*
Checked, confirmed: all 14 escalations from §§1–7 had `context='{}'` — the
`document_reference_grouping` rule (§1) was written and then never applied by the same session's
own code raising the very escalations it governs. Answered the actual question straight: only the
four enum-constrained columns are checked live against `cfg_enum`; `cfg_escalation` itself was pure
documentation, nothing read it. Fixed for real: `raise_manual()` gained `reference_doc`; a
non-default `related_activity` now REQUIRES it or raises `ValueError`. Smoke-tested both the
refusal and the success path, Python CLI and `Escalation.ps1` directly. Backfilled `context` on all
12 real grouped escalations. `cfg_escalation.document_reference_grouping`'s `enforced_by` updated
from "not yet wired" to the real function. Full record: `BUILD.md` §115.

## 9. Addendum, same day — a bare `run.py` mention proved genuinely ambiguous; `full_path_file_references` rule added

Researcher, still on #647: `related_activity` said `"run.py work-package registration check"` —
searched for the file, couldn't find it. Checked: `run.py` resolves to **5 different files** in
this repo (3 vendored inside a `docx` library, 1 real at `iba/app/run.py`) — not just unhelpful,
actively ambiguous. Fixed #646/#647's text to full paths; added `cfg_escalation.
full_path_file_references`, honestly marked NOT mechanically enforced (no reliable regex for "is
this really an ambiguous filename mention"). Full record: `BUILD.md` §115 (same section as §8's
fix — both landed in one pass).

## 10. Addendum, same day — USER-GUIDE.md §4.2 was stale AND two live behavioural bugs were hiding behind it

Researcher, reading §4.2 directly: it only described the three *shapes* (word/run/manual), never
the five *types* (task/run_error/issue/notice/config) added this session — "does it make you think
to ask if the new methods... been incorporated into the script itself and the ps command?" Checked
rather than assumed clean — three real gaps, not one doc gap:

1. `type` has zero behavioural effect anywhere (grepped the whole app) — disclosed as
   classification-only in the rewritten docs, not built into something it wasn't.
2. **Real, live bug:** all 7 handlers that resume a real pause only understand `approve`/`reject`,
   with a fallback that treated `hold`/`noted` exactly like a rejection — because
   `answer_for_run`/`answer_for_word` always wrote `state='completed'` regardless of value. Fixed
   at the root (`_terminal_state_for`): `hold`→`on-hold` (run correctly stays paused), `noted`→
   `closed`. Second bug caught fixing it: `answer_for_word` would have wrongly REJECTED a word
   answered `hold` — word-scoped decisions now restricted to approve/reject only. 12 historical
   rows from earlier today retroactively corrected to match.
3. `state='re-assign'` was documented, never producible. Built `reassign_run()` for real, wired
   into the CLI and `Escalation.ps1 -Action Reassign`; widened edit/pause/retract to recognise it
   as an open state (they didn't before).

Verified end to end through both the Python CLI and `Escalation.ps1` directly for every change.
USER-GUIDE.md §4 substantially rewritten, not patched. Full record: `BUILD.md` §116.

## 11. Addendum, same day — the stale 3-option vocabulary swept everywhere, including a LIVE runtime message; `chat_routing` strengthened after a real violation caught live

Grepped the whole `iba/app` tree for the `Approve|Reject|Revise` pattern rather than fixing only
the one cheat-sheet line the researcher flagged — found 9 more places, one of them not
documentation at all: `notification.paused_banner_guided`, the actual text `run.py` prints to the
researcher's terminal every real pause, fixed live and re-rendered through `cfg.setting()` +
`.format()` to confirm. Plus `configmaint.py`'s duplicate copy, `GOVERNANCE.md` §9D, and 7 PS
scripts' own pause-and-point-back help text. Also found the old `Yes|No` word-scoped vocabulary
still live in `registry.py`'s docstring (fixed) and in `GOVERNANCE.md` §6 (a historical,
`CORRECTED 2026-07-22`-dated section — deliberately left as-is, `Yes|No` still works as an alias).
Full record: `BUILD.md` §117.

Researcher then caught the meta-pattern: *"I would expect that this comment will automatically
create an escalation to anchor the 'not yet done' pointer."* Also asked directly whether today's 42
new `governance`/`backup`/`escalation` settings are actually active — checked and answered
precisely (`inactive=0`/`active=1`, live data; enforcement is a separate, already-disclosed
question). Triaged the three "not touched" items from §11's own report: two were closed decisions
with no further action possible; `GOVERNANCE.md` §6's note was a genuine judgement call reported
only in chat, exactly the pattern `feedback_iba_data_judgment_calls_must_escalate_not_silent_report`
already names — raised as its own escalation, assigned Researcher.
`cfg_escalation.chat_routing` extended: any judgement call or genuinely open item reported only in
chat prose must get its own escalation in the same turn, not after being asked — honestly still
marked a practice commitment, not a code change (nothing can reliably scan this session's own
prose). Full record: `BUILD.md` §118.

## Updated: files touched, this whole session (supersedes the §"Files touched" list above for anything changed again in §§8–11)

**Further modified code:** `iba/app/lib/escalation.py` (`_terminal_state_for`, `reassign_run`,
`raise_manual`'s `reference_doc` requirement, `edit_question`/`pause_run`/`retract_run` widened, 2
new CLI subcommand flags), `iba/app/ps/Escalation.ps1` (`-Action Reassign`,
`-RelatedActivity`/`-ReferenceDoc`), `iba/app/handlers/configmaint.py`, `iba/app/handlers/
registry.py`, `iba/app/ps/{BookNarrative-Generate,Candidate-Curate,Candidate-Quality,
Cluster-Assign,Config-Maintenance,Lexicon-Parse,Passage-Quality}.ps1`.

**Further docs:** `iba/app/BUILD.md` (§§115–118), `iba/app/GOVERNANCE.md` (§39 addendum),
`iba/app/USER-GUIDE.md` (§4 substantially rewritten a second time).

**Further config/data:** `cfg_escalation` (+1 rule `full_path_file_references`,
`document_reference_grouping`/`chat_routing` rule text/enforced_by updated), `notification.
paused_banner_guided` (live value fixed), 12 historical `escalation` rows corrected from
`completed` to `closed`, 12 grouped rows backfilled with `context`, 2 escalation-text rows fixed
(#646/#647 bare filename), 1 new escalation raised (GOVERNANCE.md §6 judgement call). Final
open-escalation count: **15**.

## Next (supersedes the prior "Next" above)

Same priorities as before, unchanged in substance: `module_blocking` wiring and the work-package
registration-check verification are the two most load-bearing of the 6 §7 task escalations. Add to
the queue: the GOVERNANCE.md §6 cross-reference decision (§11, assigned Researcher) is small and
quick whenever picked up. `Escalation.ps1 -Action List` remains the live tracking surface.
