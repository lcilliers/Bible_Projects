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

## 4. Decided — researcher's rules, 2026-09-14

1. **RESOLVED — inclusion filter.** *"do not migrate any soft deleted items. only active open items
   must be migrated. ignore status"* — the filter is `deleted=0` alone; `status` plays no role in
   deciding what migrates. **Live-checked, and this matters a lot more than the original estimate
   suggested:** the doc's original snapshot (2026-09-13) read 239 `status='active'`/243 `deleted`
   from `cfg_table`'s own note; the actual live crosstab, re-checked 2026-09-14, is starker —
   **216 rows carry `status='active'`, but 118 of those are ALSO `deleted=1`.** Only **98 rows**
   are genuinely live under the researcher's rule (`deleted=0`, `status` ignored). This is exactly
   why "ignore status" was the right call — `status='active'` alone would have pulled in 118
   soft-deleted rows.
2. **RESOLVED — copy vs. move.** *"set bible_research_db all catalogue related tables all as
   inactive. iba.db is authoritative going forward and nothing should access the research_db
   tables."* Not a physical drop — `cfg_table.inactive=1` on the source side, `iba.db` sole
   authoritative target. **Checked live which tables this actually touches, not assumed:**
   `wa_obs_question_catalogue` itself (currently `inactive=0` — needs flipping) is the only table
   this instruction cleanly covers among genuinely catalogue-scoped tables; its siblings
   `wa_finding_catalogue_links` and `wa_flag_type_question_link` are already `inactive=1` (prior
   migrations, §3) — nothing to do there. **`wa_quality_flag_types` is NOT catalogue-related**
   (checked its `cfg_table.use` text: repurposed 2026-08-23, escalation #833, as the unrelated
   prose-quality-check flag vocabulary) — excluded, not part of this instruction.
   **RESOLVED, 2026-09-14 — `finding_question_link` is OUT of scope for this migration.**
   Researcher's own words: *"finding[_]question_link is replaced by ib_node. no need to migrate
   it."* Confirms it as the old finding-based mechanism `ib_node` supersedes — not migrated, not
   marked inactive, not touched by #1696 at all. Its own retirement (once `ib_node` is built and
   populated for real) is a separate, later disposition question, not decided or actioned here.
3. **RESOLVED — retargeting order.** *"the active catalogue items will be inserted into the iba
   table. there should not be any related items to transfer."* Confirmed: no live production data
   references these rows today (only the registered routines in §2, and the FK #1691 §7a is
   waiting on this), so there's no dual-write/read window to design — a straight bulk insert of the
   98 rows plus the §2 routine retargeting, in one atomic unit of work.
4. **NEW, scope boundary — RESOLVED.** *"the work done in #1690 was prototype work, we will redo it
   for real. ignore the jsons with pointers to the catalogue, they will not be transferred into the
   iba database."* This migration moves ONLY the catalogue table itself (question definitions) —
   no prototype JSON output (the `_analytics/Clusters/1682-test-m10-*`/`1692-ib-node-*` files,
   including the phantom mockup, #1699) is migrated, referenced, or treated as real data by this
   escalation. Those get redone against the real pipeline once it's built.
5. **Deliverable, per your instruction — done.** Full-field CSV of the 98 candidate rows (every
   column, `deleted=0` filter applied, live-queried 2026-09-14) for your review before anything
   executes: [`1696-catalogue-migration-candidate-rows-v1-20260914.csv`](1696-catalogue-migration-candidate-rows-v1-20260914.csv).

## 5. What "finalized" would mean

**Narrowed further, 2026-09-14 — every §4 item now resolved.** Once you've reviewed the CSV (§4
item 5) and the sign-off pack (#1690/#1691/#1692/#1693/#1696) is approved as a set: a migration
script creates `wa_obs_question_catalogue` in `iba.db` (schema
per the live `bible_research.db` DDL), bulk-inserts the 98 `deleted=0` rows, retargets every live
routine in §2's table (code + `cfg_step`/`cfg_write_grant` rows), sets `wa_obs_question_catalogue.
inactive=1` in `bible_research.db`'s `cfg_table`, and restores the real FK on `ib_observation.
question_code` (#1691 §7a) that started this whole thread — all in one unit of work, per item 3.

researcher notes

§4.1 do not migrate any soft deleted items. only active open items must be migrated.  ignore status
§4.2 set bible_research_db all catelogue related tables all as inactive. iba.db is authorative going forward and nothing should access the research_db tables.  
§4.2 the work done in #1690 was prototype work, we will redo it for real. ignore the jsons with pointers to the catelogue, they will not be transferred into the iba database.
§4.3 the active catelogue items will be inserted into the iba table.  there should not be any related items to transfer.

Before the migration allow me to have a thorough review of a complete list of all the catalogue items that will be migrated. push all the fields that will be migrated to a csv.
