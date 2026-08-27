# Session log — 2026-07-26 (continuation 2) — prior session's backlog fully cleared, strong_meaning_tree root cause fixed, escalation backlog closed out, strong-meaning report regenerated

**Session closing 2026-07-26 (researcher moving to review/clear) — the next session starts fresh,
with no memory of this conversation.** This log is a cold-start entry point: read it first, then
follow its pointers. Directly continues
[`SESSION-LOG-20260726-verse-analysis-report-config-driven-step-rule-passage-retirement-ambiguity-fix.md`](SESSION-LOG-20260726-verse-analysis-report-config-driven-step-rule-passage-retirement-ambiguity-fix.md)
(same calendar day, separate conversation — that log's own "where to start" list (6 items) is
exactly what this session worked through, in order).

---

## What this session did, in order

### 0. IBA app restarted
`iba/app/ps/Start-Iba.ps1` — config already loaded, 22 data tables present, STEP up and tagged
(`http://localhost:8989`, `ESV_th`), known-answer probe passed.

### 1. Prior session's "where to start" list (6 items) worked through in order

1. **Auto-backfill wiring — answered "yes".** New `cfg_setting` `report.auto_backfill_before_render`
   (module `report`, default `true`) proposed via `configmaint.propose` and approved (escalation
   `#321` — the researcher's direct in-conversation "yes" stood as the approval, same pattern as
   prior sessions' §21/§22). `handlers/raw.py:backfill_meaning`'s core factored out into
   `backfill_meaning_for(ctx, book, lo_ch, hi_ch, verse_lo, verse_hi) -> dict` (same shape as
   `handlers/lexicon.py`'s own factoring precedent); `handlers/reports.py:verse_span_meaning_report`
   now calls it for the exact book+range being rendered, before writing the report, when the
   setting is true.
2. **Dan 2:1-16 rerun** — left at 49% coverage last session specifically because item 1 was open.
   Re-ran via `VerseSpanMeaning-Report.ps1`: auto-backfilled 75 previously-unregistered strongs,
   rendered at **100% coverage** in one call. Dan 1:7-21 also auto-backfilled (34 strongs) on its
   own re-run.
3. **`strong_meaning_tree`'s base-collapse root cause fixed properly** — the researcher's own
   words, answering the exact open question named in every session since. Root cause: the write
   guard was keyed on `lemma_key` alone, so whichever sibling code got detailed FIRST silently
   claimed the base row and every other sibling's own (already correctly fetched) tree text was
   discarded — real data loss for 108/470 (23%) genuine homonym collapses (harmless for the other
   362, same-root stem-splits sharing one legitimate combined STEP entry). Fixed: `strong_variant`
   column added to both `strong_meaning_tree` and `strong_meaning_parsed` (mirrors
   `candidate_seed.strong_variant`'s own precedent exactly, GOVERNANCE.md §10); write guard in
   `handlers/raw.py:detail_one` now keyed on `(lemma_key, strong_variant=resolved)`; tree-writing
   factored into `write_tree_rows()` for reuse; `lib/lexiconparse.py`/`handlers/lexicon.py` carry
   `strong_variant` through the parse rebuild; readers (`lib/versespanmeaningreport.py` +
   `tools/build_verse_span_meaning_extract.py`, kept in sync) now prefer an exact `strong_variant`
   match, falling back to the base/unsplit row. New migration
   `migration/fix_strong_meaning_tree_collapse.py` live-detected all 108 genuine collapses
   system-wide (matching the prior session's own measured count exactly) and backfilled each via a
   live STEP re-fetch — **108/108, 0 remaining**, verified. Two new `cfg_column` rows registered via
   `configmaint.propose` (escalations `#322`/`#323`, approved on the same explicit instruction).
   Spot-checked live: `H3581B` now renders its own "strength, power, might..." permanently, distinct
   from `H3581`'s "reptile" content, no live STEP call needed any more; `H0935G`/`H0935P` (the
   stem-split majority shape) correctly left sharing one base row, untouched.
4. **`iba/docs/Passage read guidance.md` read** for context (the researcher's own manual
   step-by-step definition of the passage-reading "movement"/operation method — subject/operation/
   source/target per operation). No action taken at the time, per "do not pre-empt" — signed off
   later this session (§3 below).
5. **No new passage design** — confirmed still parked, correct, untouched.
6. **git status batched and committed** — 7 commits: this session's code/migration/BUILD.md fix;
   the regenerated Daniel reports + their auto-archived prior versions; the session-log/plan
   folder relocation (renames, pre-existing from an earlier session, `iba/app/` → `iba/logs/` +
   `iba/app/docs/`); config-report/escalation-list archive snapshots; the Daniel WA debate/working
   notes; the Passage read guidance docs (two draft locations, not reconciled); the unrelated
   "AI failures" research thread. All pre-existing untracked items the prior log said not to touch
   were in fact cleared this session, per this session's own explicit instruction to do so.
   Full detail: BUILD.md §25/§26.

### 2. Outstanding/parked audit, then closed out per researcher instruction
Asked directly whether anything was still outstanding. Investigated the live `escalation` table
(not just BUILD.md prose) and found **15 open escalations**, none touched by the day's work so far:
13 tied to `candidate.validate`/`candidate.load` (2026-07-22, predating the 2026-07-23 candidate-
system retraction — confirmed live that every step in `handlers/candidate.py` is `inactive=1`), plus
two standalone manual notes (`#269` `report.output_dir` misplaced, `#306` `cfg_candidate_rule`
claimed unused). Researcher's closing instructions, each carried out and verified:

- **Movement definition** — signed off with `Passage read guidance.md` as the deliverable. Recorded
  in memory (`project_movement_operation_definition_written`, both the live `.claude` store and this
  repo's `memory/` mirror) since there was no DB escalation tracking it — linked back to
  `project_RESET_characteristics_to_movements_changeover` with an explicit note that this closes the
  *definition* only, not the wider cluster rollout.
- **13 candidate escalations closed as withdrawn** — `#228` (the one `MANUAL-` run_id among them)
  retracted directly (a true withdrawal); the other 12 are dispatcher-tied (`RUN-...`), and
  `retract_run` is hard-restricted to `MANUAL-` run_ids (`lib/escalation.py:_manual_only`) — so they
  were closed via `AnswerRun reject`, the identical closest-fit substitute this app's own passage
  retraction already used (BUILD.md §23) for exactly this situation.
- **`#269` signed off `approve`/completed** — checked `cfg_change_detail` first rather than assuming:
  the fix (`report.output_dir` → `"iba/app/reports"`) was already applied 2026-07-23
  (`RUN-20260723_063400_268-CONFIGMAINT`, change id 38); only the escalation bookkeeping was left
  open.
- **`#306` signed off `approve`/no-longer-relevant** — verified live before signing off rather than
  taking the premise on faith: `cfg_candidate_rule` (289 rows) is still referenced in code
  (`handlers/candidate.py`, `lib/cfg.py`, `lib/cfgload.py`, `lib/cfgquality.py`, `lib/cfgreport.py`),
  so the ORIGINAL 2026-07-22 claim ("not used in any routine") was factually wrong at the time — but
  every step that would read it (`candidate.seed`/`set`/`curate`/`load`/`validate`) is `inactive=1`
  since the 2026-07-23 retraction, so it genuinely is unused in any LIVE routine today. Signed off
  with that corrected reasoning, not a blind echo of the original premise.

**Escalation table confirmed clean afterward: 0 raised, 0 paused** (312 answered, 3 retracted).

### 3. Strong-meaning report regenerated
Researcher's request: run the strong-table report via the app's own registered report scripts,
config-driven. `iba/app/ps/StrongMeaning-Report.ps1` → work package `strong-meaning-report`, step
`report.strong_meaning` → wrote `iba/app/reports/strong-meaning.md` (config path
`report.strong_meaning_path`) + the CSV pairing (`export/strong_sense.csv`,
`export/strong_meaning_tree.csv`, gitignored, both now carrying the new `strong_variant` column).
Coverage: 3,635 `strong` rows, 100% with `strong_sense`, 92% with `strong_meaning_tree`, 41% with
lexicon detail, 0% with neither — reflects this session's 108-collapse backfill and every
registration since the prior (2026-07-23, pre-data) run of this report.

---

## Where to start a fresh session

**Nothing outstanding within the IBA app as of this log** — `configmaint.validate` clean, escalation
table at 0 raised/0 paused, working tree clean and pushed-pending (see Artifacts). The researcher is
moving to review/clear context next; nothing here needs pre-empting.

The only genuinely open item is **outside this session's scope and not to be pre-empted**: the wider
characteristics→movements ROLLOUT across clusters (the main Bible-study programme,
`project_RESET_characteristics_to_movements_changeover`) — the operational *definition* is now
written (`Passage read guidance.md`, signed off this session) but applying it across the cluster
backlog is separate, much larger, ongoing work the researcher owns.

## Artifacts this session

**Code** (`iba/app/`): `handlers/raw.py` (`backfill_meaning_for`/`write_tree_rows` factored out,
`detail_one`'s write guard fixed), `handlers/reports.py` (`report.auto_backfill_before_render`
wiring), `handlers/lexicon.py` (`strong_variant` carried through `rebuild_parsed_tables`),
`lib/lexiconparse.py` (`strong_variant` pass-through), `lib/versespanmeaningreport.py` +
`tools/build_verse_span_meaning_extract.py` (exact-variant/base-fallback reader, kept in sync),
`migration/fix_strong_meaning_tree_collapse.py` (new).

**Config**: `report.auto_backfill_before_render` (new `cfg_setting`, approved escalation `#321`);
`strong_meaning_tree.strong_variant` + `strong_meaning_parsed.strong_variant` (new `cfg_column`
rows, approved escalations `#322`/`#323`).

**Data**: `strong_meaning_tree`/`strong_meaning_parsed` gain `strong_variant` (backfilled to
`lemma_key` for pre-existing rows); 108 genuine base-collapses backfilled with their own exact-code
tree rows via live STEP re-fetch. Escalation table: 13 candidate escalations closed (1 retracted,
12 rejected), `#269`/`#306` approved — 0 open remaining.

**Reports**: `verse-analysis/Daniel/dan-{1-1-7,1-7-21,2-1-16}-verse-span-meaning.md` (regenerated,
prior versions auto-archived); `reports/strong-meaning.md` (regenerated, prior tiny version
auto-archived).

**Docs**: `BUILD.md` §25/§26 (updated in the same unit of work as their triggering code/config
change, per `governance.build_md_on_code_change`).

**Memory**: `project_movement_operation_definition_written` (new, both the live store and this
repo's `memory/` mirror).

**Git**: 9 commits this session (see `git log` — `19768a27` back through `cd5cbd73`), plus this log.
Per `governance.session_log_triggers_commit` / CLAUDE.md §12: this log itself is staged, committed,
and pushed in the same unit of work.
