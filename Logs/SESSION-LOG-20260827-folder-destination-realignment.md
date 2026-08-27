# Session log — 2026-08-27 (continued) — folder-destination realignment

**Scope:** following the researcher's own large-scale folder reorganisation (committed earlier this
session, `8bdc16bc`), worked through escalations #929 ("Folder analysis") and #736 ("Main-Project /
IBA Filing Consolidation", taken off hold this session) to realign every IBA report/config output
path against the researcher's stated destination rules, apply the approved changes, and migrate the
physical files.

## Escalations touched

| id | outcome |
|---|---|
| #736 | in-progress — taken off hold by researcher this session (v5); updated with progress notes; not closed, more folders still outstanding |
| #929 | in-progress — updated with progress notes; original v1/v2 census deliverables stand, not closed |
| #934 | completed — `escalation.list_report_path` → `outputs/escalation/escalation-list.md` |
| #935 | completed — `escalation.history_report_dir` → `outputs/escalation` |
| #936 | completed, self_correctable — Claude's own CLI mistake (passed `-Comment` where `-Resolution` was required for a `ready_for_approval` transition); fixed immediately by re-running correctly |
| #937 | completed, self_correctable — same mistake as #936, second call in the same batch |
| #938 | completed, self_correctable — Claude's own CLI mistake (`-NextAction revise` without the required `-Tried`); fixed by switching to a plain comment-only `Update` instead |
| #939–#962 (24 items) | completed, approved — batch folder-destination repoint (behaviour, configmaint, content_index ×2, cluster.quality, lexicon, manifest, method ×4, narrative ×2, report ×8, retention) |
| #963 | withdrawn — stray duplicate test escalation, Claude's own debug artifact, not a real proposal |
| #964 | **ready_for_approval, pending** — `table_export.output_dir` → `workflow/schema` |
| #965 | **ready_for_approval, pending** — `validation.output_dir` → `outputs/validations` |

## Decisions made

**Researcher's own decisions this session:**
- `outputs/escalation` = canonical folder for all escalation reports and investigations.
- Filing rule: `_analytics/[type]/[group_folder]` for bible_book/cluster/registry-specific reports
  (aggregate/non-subsection-specific reports go to the *root* of their type folder, not a subfolder);
  `research/discovery` or `research/investigations` for general, non-section-specific
  discovery/investigatory reports; `_raw_data/[sub-folder]/[group]` for raw table-data dumps.
- `iba/app/reports` discontinued as a filing destination — folder itself kept on disk (not deleted,
  in case an unfound script still reads a plain path there).
- Script folders (`iba/app/ps`→`scripts/ps`, `iba/app/tools`→`scripts/tools`, `iba/app/lib`→
  `scripts/lib`) — decision recorded, execution **parked** until "IBA relocation" is considered
  (same risk class as moving `iba.db`, per earlier chat discussion).
- `database.iba.path` / `database.bible_research.path` — parked, untouched.
- `Logs/` stays at its current root; subfolders only where specifically warranted (none identified
  yet). `method.*` confirmed unchanged at `workflow/instructions/`.
- `narrative.scope_check_report_path` + `narrative.usage_log_path` → `_analytics/essay/` (root —
  neither is meaningfully per-book: scope-check is a single rolling file, usage-log is a
  cross-book audit CSV).
- `behaviour.list_report_path`/`configmaint.report_path` → `outputs/configs/`;
  `content_index.report_path`/`content_index.size_profile_report_path` → `outputs/content_index/`
  (researcher's own earlier placeholder, confirmed final this round).
- `table_export.output_dir` → `workflow/schema` ("all table exports").
- `validation.output_dir` → `outputs/validations` — single shared folder, resolving the
  book-vs-word split concern Claude had flagged (filenames already disambiguate
  `validation-{word}.md` / `validation-book-{book}.md`; no code change needed after all).
- `iba/app/config/export/archive/`'s **7,011 archived config-table CSV snapshots deleted outright**
  — "these files can be produced on demand if needed, history is irrelevant." Verified safe first:
  no code anywhere reads them back; the real structured audit trail is `cfg_change_detail` (322
  rows, one per actual config write), untouched by the deletion. Folder is gitignored — deletion is
  permanent, no git history to recover from (stated to the researcher before/while acting).
- `governance.oneoff_report_dir`'s specific callers (content-index-search, manifest-search,
  span-strongtree/span-meaning extracts) — parked this round, flagged as needing "a deeper dive
  into hardcoded scripts" before its exact catch-all value is finalised.
- Remaining items (below) explicitly deferred to tomorrow morning; folder-reorg sign-off deferred
  until then.

**Claude's investigative findings, not decisions (informational, fed the above choices):**
- `iba/app/verse-analysis/` no longer exists on disk at all — the researcher's own prior manual
  reorg had already consolidated it into `_analytics/Bible_Books`, so 3 of the 24 settings
  (`report.verse_analysis_output_dir`/`strong_verse_output_dir`/`word_registry_span_output_dir`)
  needed only a config-pointer update, no file migration.
- `CONFIG-REPORT.md` auto-regenerates after every `configmaint.propose` apply — this produced one
  genuine mid-batch conflict (a stale `iba/app/config/CONFIG-REPORT.md` vs. an already-fresher
  auto-regenerated copy at the new location); resolved by archiving the stale copy under a
  disambiguating name, keeping the fresher one live.
- `cfg_api.csv` and its 16 siblings traced to `reportkit.write_csv_pairing()`'s `cfg_*` wildcard row
  under `configmaint.report` — confirmed zero code reads these files back; this directly informed
  the researcher's deletion decision above.

## Files / deliverables changed

- `8bdc16bc` (earlier this session) — large folder-reorg + backlog catch-up commit, 8,146 files.
- [`outputs/escalation/config-folder-destination-alignment-extract-v1-20260827.md`](../outputs/escalation/config-folder-destination-alignment-extract-v1-20260827.md) — created, then
  revised across several rounds (researcher's own markup + Claude's classification passes).
- [`iba/app/GOVERNANCE.md`](../iba/app/GOVERNANCE.md) §59 — records the escalation-report repoint (#934/#935).
- 24 `cfg_setting` rows updated (escalation-report pair earlier + the 24-item batch this round — see
  table above for the full key list).
- 202 physical files migrated (report outputs + their archives + the 4 method docs) from
  `iba/app/reports/`, `iba/app/config/`, `iba/docs/` into `outputs/configs/`,
  `outputs/content_index/`, `_analytics/Clusters/`, `_analytics/Registry/`, `_analytics/essay/`,
  `research/discovery/`, `workflow/schema/`, `workflow/instructions/`.
- 187 escalation-report files migrated earlier this session from `iba/app/reports`(+archive) into
  `outputs/escalation`(+archive); numerous `*-escalation-history-*.md` snapshots generated there
  as a side effect of `Escalation.ps1 -Action History` calls throughout.
- `iba/app/config/export/archive/` — 7,011 files deleted per researcher's explicit instruction.
- This file.

## Open items carried into next session

**For the researcher, tomorrow morning:**
- Approve/reject #964 (`table_export.output_dir` → `workflow/schema`) and #965
  (`validation.output_dir` → `outputs/validations`).
- Decide whether `iba/app/config/export/`'s remaining 35 live CSVs should also move to
  `workflow/schema` now that the 7,011-file archive problem is gone.
- Decide `governance.oneoff_report_dir`'s exact catch-all subfolder name, once its specific callers
  are individually reviewed.
- Decide the exact `_raw_data/[sub-folder]/[group]` name if `table_export.output_dir` is revisited.
- Continue script (`ps`/`tools`/`lib`) and database relocation planning whenever "IBA relocation" is
  taken up.
- Final sign-off on the whole folder reorg once the above are settled.

**For Claude, next session (once directed):**
- Apply #964/#965 once approved, migrate any physical files found at their old locations.
- Do the per-caller `governance.oneoff_report_dir` review when instructed.
- Classify/relocate the 92 ad hoc files still sitting in `iba/app/reports/` root — never covered by
  the 24-setting batch, not yet reviewed against the researcher's 3-bucket rule.

## Git state

Committing this log now — see chat for the actual `git log`/`git status` output confirming branch,
commit hash, and push, per `governance.session_log_required_content` item 6.
