# Escalation #1696 — migrate `wa_obs_question_catalogue` to `iba.db`

**Status:** design proposal, decision_required. Nothing built. Part of the sign-off pack with
#1690/#1691/#1692/#1693 (per #1682's banner) — none of the five build until all five are signed
off together.

**Origin:** found live while applying the 2026-09-13 DB fork (#737/#1682) to #1691 — `ib_observation.
question_code` was going to FK to `wa_obs_question_catalogue(question_code)`, which is
`bible_research.db`-only. Researcher's decision: migrate the table into `iba.db`, not drop the FK.

## 1. Why this isn't a fresh data-quality/management thread — it's a location move on top of one

The researcher's own framing: prior escalations on this table were about **data quality and data
management** (question wording, scope classification, orphan-row checks). This one is different in
kind — it's a **database-location migration**, made necessary by the DB fork, not a continuation of
that data-quality work. But it isn't independent of that history either: the live routines built
during that work read/write this table today, and they need to keep working (retargeted, not
rebuilt) once the table moves.

## 2. Live routines affected — checked against `cfg_utility`/`cfg_step`/`cfg_write_grant`, not guessed

All of the following are **active** (`inactive=0`) and hardcode `bible_research.db` as this table's
home. Each needs its DB target updated to `iba.db` as part of this migration — not a rewrite, a
retarget:

| Registration | File | What it does |
|---|---|---|
| `cfg_utility.cataloguewrite` | `iba/app/lib/cataloguewrite.py` | `obs_catalogue.update` — validated partial `UPDATE` of one row by `obs_id`; connects via `cfg.database_path("bible_research")` |
| `cfg_utility.cataloguereport` | `iba/app/lib/cataloguereport.py` | `report.obs_catalogue` — structural review (lifecycle conflicts, naming inconsistencies, tiered-question set); same hardcoded connection |
| `cfg_utility.handlers_catalogue` | `iba/app/handlers/catalogue.py` | thin dispatcher adapter over `cataloguewrite.py` |
| `cfg_step` row `catalogue-update` / `obs_catalogue.update` | — | its own `does` text names `bible_research.db` explicitly — needs updating in the same unit of work as the code |
| `cfg_step` row `catalogue-report` / `report.obs_catalogue` | — | same |
| `cfg_write_grant` (`obs_catalogue.update` → `wa_obs_question_catalogue`) | — | `database` column is literally `'bible_research'` — this row's value must change to `'iba'` |
| `iba/app/ps/Catalogue-Update.ps1`, `iba/app/ps/Catalogue-Report.ps1` | — | thin PS wrappers over the two utilities above; no DB knowledge of their own, but exercise the whole path end to end for testing the migration |

Also present, but **inactive**, so lower priority (retarget if ever reactivated, not before):
`scripts_build_obs_catalogue_export`, `scripts_build_obs_catalogue_tiered_extract`,
`scripts_build_tier_catalogue_update_patch_20260619`, `scripts_export_tier_catalogue` (also flagged
non-compliant, #648, independent of this migration).

## 3. Closed escalations this migration must account for — referenced, not re-litigated

- **#1007** — *"create ps tool to work with catalogue"* — THE escalation that built everything in
  §2's live-routines table (`cataloguewrite.py`/`cataloguereport.py`/both PS tools/both `cfg_step`
  rows/the write grant). Its own resolution already flagged that classification/tooling alone
  couldn't resolve the catalogue's deeper problems (question scope, expected answers, role in
  analysis) — worth remembering this migration doesn't fix that, it just relocates it.
- **#1370** — *"no `wa_obs_question_catalogue` row with `obs_id=999999`"* — closed as "not a
  defect," a deliberate test of `obs_catalogue.update`'s own validation during #1007's build. No
  migration impact, listed for completeness since it's this table's only dedicated data-quality
  escalation with a concrete resolution.
- **#1444** — *"Updates to catalogue"* — produced `iba/app/migration/
  split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py`, a one-off that split 5 bundled
  codes into mechanical/interpretive pairs (soft-deleted the old unified code). Already applied and
  `inactive=1` — not re-run by this migration, but its effects (the split codes, the soft-deleted
  originals) are part of what gets copied into `iba.db`.
- **#1524** — *"Validate catalogue questions against Window 1 evidence"* — **directly anticipated
  this exact question.** Its own resolution, verbatim: *"#737 still has open items that directly
  feed this item's scope — ... the schema-location decision (fresh build in bible_research.db vs
  migrate iba.db) ..."* — recommended holding #1524 until that was settled. It now is (this
  session, #737/#1682) — #1524 can be picked back up once #1696 actually executes, not before.
- **#1018/#1445** — *"Mark `wa_flag_type_question_link` inactive"* — a sibling table in the same
  observation-catalogue family, already retired (`cfg_table.inactive=1`, `bible_research`). Not
  migrated — dead weight stays dead weight, this migration only moves the live table.
- **#1024/#1025/#1030–#1037** — the `wa_finding_catalogue_links` → `finding_question_link`
  migration (2026-08-29, all completed). **Direct prior art, not just history**: an actual precedent
  for migrating data out of this same table family, with a documented pattern worth following here
  — remap via a legacy-reference tag (`source_legacy_ref`-style column) rather than assuming a clean
  1:1 copy, leave rows that can't cleanly migrate in the retained source table rather than forcing
  them, and register the one-off migration script in `cfg_utility` then set it `inactive=1` once
  applied (not left active as a reusable routine).

## 4. What this migration still needs to decide — not resolved here

1. **How the catalogue's own messy lifecycle state travels.** Live state: 434 rows, only 239
   `active`, 243 `deleted`, and `status`/`deleted` disagree in count (`cfg_table`'s own note). Copy
   as-is and let `iba.db` inherit the mess, or clean up in the same move? Not decided.
   `finding_question_link`'s own migration (§3) chose to leave what couldn't cleanly migrate in
   place rather than force it — a candidate pattern, not yet adopted here.
2. **Copy vs. move.** Does the `bible_research.db` copy get dropped once `iba.db` is authoritative,
   or kept read-only for provenance (matching how #1690's legacy `cluster_subgroup` question was
   handled — decoupled, not forced)? Not decided.
3. **Retargeting order** for §2's live routines — one atomic cutover, or a dual-write/read window?
   Given nothing else currently depends on `obs_catalogue.update`/`report.obs_catalogue` running
   mid-migration, a single atomic cutover looks lower-risk, but not decided here.

## 5. What "finalized" would mean

Once §4 is decided and the sign-off pack (#1690/#1691/#1692/#1693/#1696) is approved as a set: a
migration script creates `wa_obs_question_catalogue` in `iba.db` (schema per the live
`bible_research.db` DDL, plus whatever §4 item 1 decides), copies the data, retargets every live
routine in §2's table (code + `cfg_step`/`cfg_write_grant` rows) in the same unit of work, and
restores the real FK on `ib_observation.question_code` (#1691 §7a) that started this whole thread.
