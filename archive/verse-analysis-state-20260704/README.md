# Archived: old _STATE report (retired 2026-07-04)

Retired as **defunct**:
- `_STATE-20260703-DEFUNCT.md` — the auto-generated "mission control" page. Stale (showed only trial
  books Exodus/Ezekiel/Leviticus/Psalms, pre wisdom-corpus); `--stdout` path crashed (cp1252/Unicode).
- `wa-report-def-state-DEFUNCT.md` — its report-definition spec. Declared `ib_observation` +
  `verse_analysis_progress` (legacy transitional stores) as source of truth — outdated; the live
  stores are `verse.process_marker` / `ve_lexical` / `lexical_prose_chapter`.

Generator `scripts/_assess_study_state.py` is left in place (provenance) but is **superseded** — do
not run it as the state page. Its scoreboard role → `verse-analysis/_reports/wa-state-report-*.md`;
its (new) diagnostic role → `scripts/_assess_pipeline_integrity_v1_20260704.py` →
`verse-analysis/_reports/wa-pipeline-integrity-report-*.md`.
