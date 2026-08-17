# Engine-controls migration into IBA — scoping plan

> Generated 2026-08-17, in response to escalation #652 (researcher, 2026-08-16, `Workflow/Chat_responses/Additional configs`):
> *"there should be one set of engine controls, controlled by IBA."* Researcher's answer to #652
> ("investigate, provide plan for migration, raise new escalation for approval of plan") is the
> instruction this document satisfies — **this is the plan, not the migration**. Nothing in
> `engine/` or `database/bible_research.db` is touched by writing this.

## 1. What "engine controls" concretely is

`engine/` (repo root, 8,239 lines across 11 modules), invoked `python -m engine.engine [options]`,
against `database/bible_research.db`. Five live modes (per `CLAUDE.md` §4): `AUDIT_WORD`,
`MIGRATE`, `REGISTER`, `REPORT`, `EXPORT` (+`EXPORT_REGISTRY`). Only `gap_fill`/`audit_word` remain
real `argparse` choices in `engine/engine.py` today — `gap_fill` is itself already marked
superseded (`CLAUDE.md` §4: *"`new_word.py` is RETIRED... `gap_fill.py` superseded"*), so in
practice **one live mode**, `audit_word`.

- **`audit.py`** — 47 named checks (`WR-01`…`WR-47`, not 20 as `CLAUDE.md` §4's "WR-01..WR-20"
  currently says — that line is itself stale and should be corrected as part of any migration,
  small finding noted here rather than silently fixed, since `CLAUDE.md` is main-project territory
  the alignment register (`docs/governance-alignment-register.md`) already tracks separately).
  Outcome PASS / REVIEW / STOP per word.
- **`constants.py`** — hardcoded: `EXPECTED_SCHEMA_VERSION`, `LOCK_SENTINEL`,
  `STALE_LOCK_SECONDS`, `BACKUP_RETENTION`, `HIGH_FREQ_THRESHOLD`, `THIN_DATA_THRESHOLD`,
  `SMALL_VERSE_SAMPLE_THRESHOLD`, `VERSE_OCCURRENCE_RATIO_THRESHOLD`/`_MIN_COUNT`, `LANG_PREFIX`,
  version/sentinel strings. **This is exactly the shape `governance.rules_must_be_config_driven`
  forbids** in IBA's own code — a hardcoded threshold with no `cfg_*` row behind it.
  `EXPECTED_SCHEMA_VERSION = "3.40.0"` is itself a live finding: `bible_research.db`'s schema has
  moved to (at least) 3.40.0 per `CLAUDE.md` §3, so this constant is a duplicate, driftable copy of
  a fact that belongs in one place.
- **`register.py`/`report.py`/`db.py`/`backup.py`/`run_log.py`/`softdelete.py`/`span_filter.py`/
  `meaning_parser.py`/`flag_engine.py`** — the supporting modules `audit_word` calls through.

## 2. Overlap with what IBA already owns

Per `governance.scope_iba_db`/`governance.project_change_rule`/`governance.primary_responsibility`,
IBA is already the base-data/process-control layer for the whole project. Concretely overlapping:

| engine/ piece | IBA equivalent already built |
|---|---|
| word onboarding (`--register`, `audit_word`'s ingest half) | `New-Word.ps1` / `raw.discover`+`raw.write` — config-governed, escalation-gated |
| schema-version check | `cfg_meta.config_version` + `init.py` step 1-2 |
| lock/backup mechanics | `lib/dbsnapshot.py` (real pre-write snapshot, built 2026-07-22 after engine's own `_apply_*` snapshot gap was identified — see `[[project_backup_alerting_and_outlook_smtp_block]]`-adjacent history) |
| audit checks (WR-01..47) | no direct IBA equivalent yet — closest is `configmaint.validate`'s hard-error checks (§119/§120 above), but those check the *config*, not a *word's* onboarded data quality |
| REPORT/EXPORT modes | `Config-Maintenance.ps1 -Step Report`, IBA's own `report.*` family |

**Not a like-for-like swap.** `audit.py`'s 47 checks are `bible_research.db`-specific (verse
records, term inventory, XREF architecture — none of which iba.db's tables model the same way), so
"migrate" cannot mean "port the Python 1:1 into `iba/app/`" — per
`[[feedback_iba_backfill_cluster_assignment_via_analysis_not_bulk_automation]]`-adjacent standing
rule (escalation #656, this same session: *"old routines... must NOT be auto-adopted... each one
migrated must be deliberately reviewed/redesigned to fit IBA's config-governed model, not copied
as-is"*).

## 3. Sequencing dependency

`governance.scope_research_db` states `bible_research.db` is "the home for prose and findings" —
but escalations #653/#654/#655 (this session) are actively working out exactly which
`bible_research.db` tables are base-data-superseded-by-iba.db vs. genuinely-prose/findings, and
that work is itself gated on #657 (the config-eyes design audit). **This plan should not begin
execution before #653's table-disposition work lands** — migrating `audit.py`'s 47 checks before
knowing which `bible_research.db` tables are staying vs. retiring risks building checks against
tables about to be marked inactive.

## 4. Proposed approach (for approval, not yet executed)

1. **Retire outright, no migration**: `gap_fill.py`, `new_word.py` (already deleted) — already
   superseded, nothing to port.
2. **Fold into config, not code**: every `constants.py` threshold becomes a `cfg_setting` (module
   `engine` or a new dedicated `cfg_engine_threshold`-style table, per
   `governance.module.config`) — small, mechanical, no logic change, can start independently of
   the rest.
3. **Redesign, don't port**: `audit.py`'s 47 WR-checks reviewed one-by-one against IBA's own data
   model once #653 settles which `bible_research.db` tables persist — each becomes either a new
   `configmaint`-style validate check (if it's a structural/config fact) or a new `cfg_step` in a
   `word-audit`-shaped IBA work package (if it's a per-word data-quality check, which is most of
   them) — not a lift-and-shift.
4. **Retire the standalone CLI**: once (2) and (3) land, `python -m engine.engine` itself retires
   in favour of IBA's `run.py` dispatcher — one entry point for the whole project, per
   `governance.scope_iba_app`.

## 5. What this plan does NOT decide

Whether `bible_research.db` itself eventually becomes IBA-managed data (vs. staying a
separately-owned DB IBA's `cfg_table`/`cfg_column` merely *describes*, per #653/#655) is explicitly
out of scope here — that's #653/#657's question, not this one's.
