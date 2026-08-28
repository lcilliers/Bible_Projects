# Session log — 2026-08-28 — folder realignment completion, word_registry/Bible_Books cleanup, self-caught config fixes

**Scope:** continuation of 2026-08-27's folder-destination realignment (escalations #929/#736).
Applied the remaining approved settings, decoupled the config-CSV export path with a real code
change, reorganised `_analytics/word_registry` and `_analytics/Bible_Books` against their live
canonical sources, registered the resulting naming conventions as config (not documentation-only,
per direct researcher instruction), closed out #929/#736 with a full sweep, and raised a new
consolidated escalation for what's genuinely still open. Self-caught 4 advisory findings via
`configmaint.validate`, fixed all of them, re-validated clean.

## Escalations touched

| id | outcome |
|---|---|
| #964 | completed — `table_export.output_dir` → `workflow/schema` |
| #965 | completed — `validation.output_dir` → `outputs/validations` (one flat shared folder; the earlier book-vs-word split concern didn't need a code change after all) |
| #966 | completed — `governance.oneoff_report_dir` → `outputs/` (catch-all default only; callers still parked) |
| #967 | completed — `configmaint.csv_export_dir` (new setting) — **caught mid-session that it had been approved but never applied** (same class of miss as `GOVERNANCE.md` §58); applied and verified live |
| #929 | completed — full sweep done, resolution recorded (`GOVERNANCE.md` §60); still-open items spun out into #971 rather than silently closed |
| #736 | completed — same sweep; its own carried-forward "general filing mechanism" gap explicitly named as unresolved, not silently approved-away |
| #968 | completed — new setting `registry.folder_naming_convention` |
| #969 | completed — new setting `report.book_folder_naming_convention` |
| #971 | **raised, untouched, parked** — consolidated "Folder-purpose governance mechanism": `docs/`'s unaddressed flat-file pattern, #736's unbuilt general filing mechanism, and a `cfg_folder_purpose`-shaped table/utility idea. `decision_required`, assigned to researcher. Explicitly not started this session, per instruction. |
| #973 | completed — self-caught fix: `registry.folder_naming_convention` module `registry`→`governance` |
| #974 | completed — self-caught fix: `report.book_folder_naming_convention` module `report`→`governance` |

## Decisions made

**Researcher's own decisions:**
- `table_export.output_dir` and the config-CSV pairing both → `workflow/schema` ("all table
  exports go to workflow/schema").
- `validation.output_dir` → one shared `outputs/validations` (not split by book/word).
- `governance.oneoff_report_dir` default → `outputs/` (its specific callers stay parked, per
  instruction, for "a deeper dive into hardcoded scripts" later).
- Proceed with both (a) the physical CSV migration and (b) the real code decoupling for
  `configmaint.csv_export_dir`, once the tradeoff was explained.
- `_analytics/word_registry` per-word folders: registry number = `iba.db`'s own live
  `word_registry.id` (confirmed different from the old `bible_research.db` numbering already
  embedded in most existing files) — explicit correction after Claude started reverse-engineering
  the old/inactive table instead of asking ("NEVER do extra work by trying to figure out the
  inactive tables").
- `_analytics/Bible_Books` folders must match `cfg_book_order.book` exactly, "so there are no
  mis-filings when working with verse references."
- The 14 word_registry root files with no confident word match: leave as-is.
- New governing principle: folder locations/naming conventions must live in `cfg_*`, never in a
  document alone — the two new naming-convention settings (#968/#969) exist specifically to close
  that gap for the two trees this session touched.
- Raise one consolidated new escalation (#971) for the three remaining open areas rather than leave
  them scattered across #929/#736's own resolution text.

**Claude's self-caught fixes (found via `configmaint.validate`, run deliberately after every
config-touching step, not skipped):**
- #967 approved-but-unapplied gap, found by actually checking rather than assuming completion.
- 3 orphan-config findings after adding the two naming-convention settings: both were filed under
  the wrong `module` (should be `governance`, matching every other policy-statement setting's
  orphan-check exemption) — fixed via #973/#974. `configmaint.csv_export_dir` was read via a raw
  SQL `SELECT` instead of the real `cfg.setting()` accessor — a genuine non-compliance with "THE
  ONLY WAY THE APP READS CONFIG" (`cfg.py`'s own words) — fixed directly in `cfgreport.py` (code
  fix, no approval needed). Re-validated clean after both fixes applied.

## Files / deliverables changed

- `iba/app/lib/cfgreport.py` — `configmaint.csv_export_dir` now read via `Cfg(...).setting(...)`,
  not raw SQL.
- `iba/app/GOVERNANCE.md` §60 (written, then extended twice with the self-caught-findings
  addendum) — full record of the completed realignment, the word_registry/Bible_Books
  reorganisation, the new governing principle, and everything still carried forward.
- `cfg_setting`: 5 rows this session (`table_export.output_dir`, `validation.output_dir`,
  `governance.oneoff_report_dir` updated; `configmaint.csv_export_dir`, `registry.folder_naming_
  convention`, `report.book_folder_naming_convention` inserted — 6 total, 2 of those corrected
  again for `module`).
- `_analytics/word_registry/`: 27 subfolders renamed (old `bible_research.db` numbering →
  `iba.db` `word_registry.id`); 249 of 263 loose root files sorted into their matching `NNN_word`
  folder.
- `_analytics/Bible_Books/`: 35 of 66 subfolders renamed to their exact `cfg_book_order.book`
  form; all 66 canonical books confirmed present and correctly named.
- 8 archived validation snapshots → `outputs/validations/archive/`; 35 live config-table CSVs →
  `Workflow/schema/`.
- This file.

## Open items carried into next session

**For the researcher:**
- #971 — decide scope: does `cfg_folder_purpose` replace the individual folder-destination
  settings already in place, or index them from above; is `docs/` in scope for the same mechanism.
- `docs/` (36 flat files) still has no naming/archiving convention at all.
- Main-project-side folders generally (`Sessions-v2/`, `Workflow/`, `research/`, `Logs/`,
  `archive/`) still have zero `cfg_*` representation — unchanged from #863's original finding.
- Scripts (`iba/app/ps`/`tools`/`lib` → `scripts/ps`/`tools`/`lib`) and database
  (`database.iba.path`/`database.bible_research.path`) relocation both remain parked, to be
  considered alongside a future "IBA relocation" review.
- 14 word_registry root files intentionally left unsorted (no confident word match).

**For Claude, next session:** none assigned — #971 stays untouched until the researcher directs it.

## Git state

To be confirmed after commit — branch, hash, and push status will be shown in chat per
`governance.session_log_required_content` item 6, then recorded back into this file in a small
follow-up commit (same pattern as 2026-08-27's close).
