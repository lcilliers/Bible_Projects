# SESSION LOG — 2026-08-17 — 15 escalations actioned, a real cross-database schema bug found and fixed before it could corrupt iba.db, `bible_research.db` fully registered in config, engine-controls Phase 0/1 built and live

Session opened with two plain-chat questions, not a task: did a terminal-run startup script reach
this session, and are escalation-file changes picked up automatically. Answered from evidence, not
assertion (no ambient visibility into anything outside a tool call this session makes) — and that
answer turned out to matter immediately, because the researcher had already answered all 15 open
escalations from the 2026-08-16 sessions via the terminal minutes before this session started.

## 1. `/start-project`, then `USER-GUIDE.md` §2 brought current (`BUILD.md` §119)

Standard orientation — git dirty (no uncommitted `SESSION-LOG`), STEP already up, IBA bootstrap
READY. Comparing the live `Start-Iba.ps1` transcript against `USER-GUIDE.md` §2 (asked for
explicitly, since the guide's own "updated 2026-08-08" banner claimed currency past when the
feature shipped) found real staleness: stale example counts, missing hash-suffixed
`config_version`, and — the substantive gap — the "governance rules" print block (`init.py` step 6,
added 2026-07-23) was never documented at all. Fixed.

## 2. The 15 escalations — triaged, not rubber-stamped (`BUILD.md` §120–121)

Full table in the chat record; short version: 3 holds (#648/#650/#654, left alone), 2 no-action
closures (#655 duplicate, #656 standing-rule note), 10 real items. Notable ones:

- **#632** (T2/T3 cluster exception): re-ran `cluster.validate` live rather than trusting the
  stale report — the T2/T3 exemption was *already* correctly configured; the 428→746 growth in
  real exceptions is legitimate ongoing work, not a bug. Fresh judgement call escalated as #668.
- **#579** (`configmaint.propose` crash, 2026-08-10): root-caused from the escalation's own
  recorded traceback — `json.loads(Where or "{}")` doesn't catch a *whitespace-only* value.
  Fixed, verified against the reproduced old crash and the fix.
- **#646** (`module_blocking` wired) + **#649** (orphaned `run_id`s): built the third `run.py`
  dispatch gate, live-verified with a synthetic escalation, then watched it fire for real,
  unprompted, minutes later when it correctly refused a second `configmaint.propose` while the
  first was still pending — production verification, not just a synthetic probe.
- **#645** (NT `verse_lexical` coverage): measured, not assumed — 27/27 NT books, 7,855/7,857
  verses (the 2 gaps are the accepted verse-gap-by-design pattern). Already complete; no build
  needed.
- **#652** (engine-controls migration plan): investigated, planned, escalation raised for
  approval — the seed of everything that followed in §§4–7 below.
- **#664** (GOVERNANCE.md §6 forward pointer): small, direct doc fix.

## 3. `configmaint.propose` itself found missing its own write grant (`BUILD.md` §120)

Wiring #646 crashed immediately on its own follow-up: `cfg_escalation` (added by the 2026-08-16
reset) had never been given a `configmaint.propose` write grant, unlike every other `cfg_*` table —
a real `governance.config_control` violation, not a side-effect of tonight's work. Swept the whole
grant table and found **four** tables in this state, not one; `cfg_method_rule`'s gap is the live,
still-reproducible root cause of the historical #539/#550 crashes. Added a permanent
`configmaint.validate` check (`find_cfg_tables_missing_configmaint_grant`) so this class of gap
can't ship silently again. One grant fixed and applied same session; three queued behind
`module_blocking`'s own one-pending-change-at-a-time serialisation (working as designed — watched
it refuse a second `configmaint.propose` for exactly this reason).

## 4. Engine-controls migration plan — v1 through v4, each revision earning its keep

`escalation #652` → v1 (a straight `engine/` inventory + port plan) → **researcher: "moving in the
right direction, but not holistically planned... should cater for what is intended... rather than
silently ignore [that the project is changing]"** → v2 (goal-first, sized the real fragmentation at
345 files, added a forward-looking capture mechanism) → **researcher: "I want to see the config
stubs and the plan as an integrated whole"** → v3 (Concept→Configs→Code→Daily-running-rules per
phase, not a separate stub doc) → the `kind`/`operations` classification questioned by the
researcher → v4 (resolved with evidence, found 2 of 12 drafted steps were outright redundant with
`run.py`'s own `_ensure_run()`/`_snapshot()`, one real re-classification). Each revision was a real
correction earning a version bump, not cosmetic — full trail: `iba/app/reports/archive/
engine-controls-migration-plan-{v1,v2,v3}-20260817.md`, live version `-v4-`.

## 5. `state='completed'` ≠ task done — a real confusion, traced to its exact line (`BUILD.md` §123)

Researcher: *"how can escalation 653 and 657 be completed, it is still in progress or on hold... may
be others in the same class."* Traced to `lib/escalation.py:_terminal_state_for()` — `approve`/
`reject`/`revise` map to `state='completed'` unconditionally, by design; that's "the decision is
final," not "the work is done." Scanned the whole batch: **three**, not two, fell in this class
(#653, #657, and #672 — the last one answered minutes before this was even raised). Fixed
practically with three dedicated open trackers rather than editing the historical decision rows
(which are factually correct as they stand). Structural fix (a `cfg_escalation` rule requiring a
companion tracker) drafted but not yet proposed — queued behind the same `configmaint.propose`
serialisation as everything else config-side.

## 6. "Proceed with 653 and 657, they're blocking Phase 1 and leaving too many open ends" — real execution, not more planning

Researcher's instruction, and the real work behind it (`BUILD.md` §125–127):

**The actual blocker, found before any data was written**: `cfg_table.name`/`cfg_column
(table_name, name)` had no way to distinguish `iba.db` from `bible_research.db` — and the two
genuinely share 4 table names (`cluster`/`passage`/`verse`/`word_registry`) for **completely
different tables**. Bulk-registering `bible_research.db`'s 110 tables under the existing schema
would have collided outright, or — worse — silently let `lib/db.py:build_data_tables()` (confirmed
by reading its own docstring, not assumed) try to create `bible_research.db`'s tables *inside*
`iba.db`. Fixed properly: `migration/add_cfg_table_database_column.py` widened both PKs to include
`database`, all 40/350 existing rows backfilled `database='iba'` (zero behaviour change), and every
one of the 5 live consumers that read these tables unscoped (`lib/cfg.py`, `handlers/
configmaint.py`, `lib/cfgreport.py`, `lib/cfgquality.py`, `validation.py`) updated to filter
`database='iba'`. Verified end-to-end: `Cfg().tables()` still exactly 40, `Cfg().columns
('word_registry')` resolves to `iba.db`'s own 6 columns not `bible_research.db`'s 32, full live
`Start-Iba.ps1` clean before AND after.

**Then #653 for real**: recaptured `iba/config/DBSchema/DBSchema.json` live
(`build_dbschema.py --db bible_research`, 110 tables/1,181 columns, real profiled descriptions —
not hand-written), bulk-loaded via `migration/bootstrap_research_db_cfg_table.py`,
`database='bible_research'`. Verified: correct row counts, all 4 name-collision tables show the
right database's own distinct description, no bleed. `governance.table_columns` ("applies to all
databases") satisfied for the first time. Follow-up raised per #653's own instruction: confirm
which tables are actually inactive.

**Then #657, closed with the flagship finding being the schema bug above** — plus the write-grant
coverage check from §3. Honest, not a claim of total completion: an audit of an app this size is
never fully "done."

**Then Phase 1 (`engine/`) — approved to proceed ahead of its original #653/#657 gate**:
`migration/bootstrap_word_audit.py` registered 15 `cfg_utility` rows, 1 `cfg_work_package`, the
corrected 10-step `cfg_step` sequence (kinds re-derived with evidence, not defaulted), 2
`cfg_on_fail` rows. `handlers/wordaudit.py` — deliberately honest stubs, not
`engine/audit_word.py`'s logic ported (escalation #656's standing rule) — live-verified dispatch
(`module_blocking`/`step_kind`/write-grant gates all confirmed applying), then found a **second**
cross-database question while writing the handlers: `iba.db` and `bible_research.db` have two
different `word_registry` tables, and nothing states which one a `word-audit` run is actually
about. Raised as its own escalation rather than guessed at inside the handler.

Every synthetic/live probe run tonight had its test artefacts (`run`/`validation_result`/
auto-raised `escalation` rows, DB snapshot files) cleaned up afterward — none left as debris in the
live DB. Four DB snapshots taken before the risky writes (schema DDL, bulk data load, word-audit
bootstrap).

## Open at close

**9 open escalations** (5 active, 4 on-hold). Active: `RUN-20260817_052130_987-CONFIGMAINT`
(`cfg_index` write-grant, still unanswered — the one blocking the remaining `cfg_method_rule`/
`cfg_quality_check` grants and Phase 0's own governance setting), the confirm-inactive-tables
follow-up (#653), the cross-database write-mechanism/word-identity follow-up (Phase 1), and two
smaller ones from earlier in the session. On-hold: #648 (project-wide script sweep), #650 (filing
decision), #654 (debate-work relocation).

## Files touched, whole session

**Code:** `iba/app/run.py` (`module_blocking` gate), `iba/app/lib/cfgquality.py` (2 new integrity
checks), `iba/app/handlers/configmaint.py` (both checks wired, `Where`/`Set` parsing hardened,
`PROJECT_ROOT`, `database='iba'` scoping), `iba/app/lib/cfg.py` (`database='iba'` scoping),
`iba/app/lib/cfgreport.py` (same), `iba/app/validation.py` (same), `iba/app/handlers/wordaudit.py`
(new). **Migrations (new):** `add_cfg_table_database_column.py`,
`bootstrap_research_db_cfg_table.py`, `bootstrap_word_audit.py`. **Docs:** `iba/app/USER-GUIDE.md`
§2, `iba/app/GOVERNANCE.md` §6 pointer, `iba/app/BUILD.md` §119–127. **Reports:**
`engine-controls-migration-plan-{v1..v4}-20260817.md` (v1–v3 archived), `cluster-assign-v2-
20260817.md`, `engine-controls-config-stubs-draft-20260817.md` (archived, folded into v3+).
**Config/data:** `cfg_write_grant` (+1 applied), `cfg_table`/`cfg_column` (+`database` column,
+110/+1,181 `bible_research` rows), `cfg_utility`/`cfg_work_package`/`cfg_step`/`cfg_on_fail`
(word-audit), ~15 `escalation` rows answered/raised/edited across the session.

## Next

Waiting on the researcher for: `cfg_index` write-grant decision (unblocks the rest of config-side
work), the confirm-inactive-tables list, the cross-database write-mechanism/word-identity decision,
and the three on-hold items whenever picked back up.
