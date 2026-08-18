# SESSION LOG — 2026-08-17 (continued through 2026-08-18 close) — escalation tool fixed for real use, engine-controls migration closed out, a live 29-day backup incident found and fixed, `wa_rule_registry` retired, content-index (round B) built and run

Direct continuation of the same day's earlier sessions (commits `28156834`, `f98682a8`,
`Logs/SESSION-LOG-20260817-escalation-state-machine-fix-cross-db-write-grants-log-consolidation.md`).
Opened on `start-project`, clean git state, all systems ready. Ran long — into 2026-08-18 by close —
so this log covers a genuinely large body of work, grouped by theme rather than strict chronology.

## 1. The escalation tool itself, made actually usable — not just documented around

Repeated, concrete friction, not abstract: the researcher hit "no pending escalation for run..."
on `#648`, `#678`, **and** `#691` in one session, each time typing `-Decision resume` — `Resume` is
a separate `-Action`, not a decision value. Three repeats of the identical mistake was treated as
the real signal it is: `answer_for_run()` now auto-resumes a `MANUAL-` item from `on-hold`/
`re-assign` before applying the answer — one call does what used to need two. Real dispatcher-tied
rows are deliberately untouched (their resume path is re-running the original paused command, a
different mechanism).

Separately: *"process changed escalations... I do not see 696/708 in the esc table"* — traced both
times to real causes, not researcher error: `#696`'s DB record genuinely hadn't changed (whatever
was typed didn't land); `#708` was there all along, confirmed live and via a fresh report
regeneration. Along the way, the report itself (`escalation-list.md`) was reworked from the ground
up — it was missing `type`/`comment`/`related_activity`/`context` entirely, flat `id`-ordered
instead of grouped, and — the specific complaint, *"not a single resolution is filled in"* — showed
only open items, so anything just resolved (with its resolution) simply vanished from view. Fixed:
all four columns added, grouped by `related_activity`, and a new **"Recently resolved"** section
so "what's actually been done" has a home outside a raw SQL query.

**`CONFIG-REPORT.md` found stuck at 2026-08-05** — `report.version_on_regenerate` (turned on that
day) had every regenerate write a new versioned file instead of ever refreshing the plain filename
every doc points at by name. Root-fixed in `reportkit.write_report()` for every report using it
(~24 types), not special-cased to this one report: both the versioned archive copy and the plain
current-state file are written on every regenerate now. This is very likely why the researcher's
own orphan-config discovery (`escalation.control_*`, `backup.*`) looked newly surfaced — those
settings postdate 2026-08-05, so the stale file could never have shown them.

`escalation.control_objectives`/`escalation.control_process` — found orphaned (never read by any
code) via the researcher spotting stale `CONFIG-REPORT` findings. Fixed by having `-Action List`
actually read and state both live, in the report's own header — the module's natural "status
check" moment, not a bolted-on check.

## 2. Governance-alignment register — items #1, #2, #4/#5, #6 all closed

- **#1** (`CLAUDE.md` §4/5/7/8 presenting the retired `engine/`/STEP pipeline as live) — a
  superseded-by banner added (top-of-file + inline per section, matching §3's existing convention),
  content marked provenance-only, not deleted.
- **#2** — confirmed duplicate of #650, folded in rather than run separately.
- **#4/#5** (`wa_rule_registry` vs. `iba/app/GOVERNANCE.md`) — first delivered the requested
  *review*: all 34 active rows read in full, triaged into keep/obsolete/partially-stale/real-
  conflict buckets, cross-referenced against all 30 live `governance.*` settings (`wa-rule-
  registry-full-review-v1-20260817.md`). Then the researcher gave a **blanket decision superseding
  that triage**: *"the table wa-rule-register must be set to inactive... this table is therefore no
  longer operational."* Applied as given: all 59 rows (34 previously active) marked `obsolete=1`,
  `CLAUDE.md` references corrected in three places (the table-groups row struck through, the
  `wa-global-general-rules` document row marked superseded, all three `GR-REF-002` citations
  replaced with a direct statement of the convention it named — the convention itself, already
  fully defined in `CLAUDE.md`'s own text, is unaffected). Flagged, not silently dropped: six
  principles the review had called out as still genuinely live (`GR-DB-001`, `GR-REF-001`,
  `GR-PROC-001`, `GR-PROG-001`/`002`/`009`) now have no operational home anywhere.
- **#6 part B** (content-index) — see §7 below.

## 3. Engine-controls migration (`#648`/`#698`/`#699`) — closed for real

Traced `#648` to being Phase 2/3 of the already-approved `engine-controls-migration-plan-v4`, gated
by the researcher's own prior answer ("on hold until phase 0 and 1 is completed"). Phase 0
(`governance.new_utility_registration_timing`, code built earlier but never actually applied)
proposed and applied for real (`#698`). Phase 2/3 (`#699`, "register all, mark any not clearly
alive inactive") executed as one governed batch — 343 previously-unregistered scripts registered
into `cfg_utility` (202 active / 141 inactive by filename date-stamp), not 343 individual
proposals. One corrupted file found in the process (`scripts/word_full_extract.py` — chat text
literally pasted into a `.py` file, broken since its only commit, 2026-03-19) — raised as `#701`,
not silently patched.

`#648`'s *actual* remaining content — a review of hardcoded values that should be `cfg_setting`-
driven — delivered separately: 232 scripts scanned via `ast.parse` for module-level ALL_CAPS
constants, split into 105 files/263 real candidates vs. 177 files/423 structural false positives
(a first regex-alternation cut hung outright at this key count, same lesson as §7 below).

Then the researcher's own follow-on: *"scripts that dont comply must be in the register marked as
inactive... when put into use it should signal the script needs revision."* All 105 flagged
`inactive=1` with the finding in their own `purpose` text. Enforcement built where it's real —
`Cfg.assert_utility_compliant()`, wired into the 2 of 105 files with an actual dispatcher-reachable
caller (`narrativegenerate.py`, `wordregistryspanreport.py`), verified live to raise before any
real work happens. For the other 103 (standalone scripts, no dispatch point to hook into in code)
— `governance.noncompliant_script_gate` documents that enforcement there is process discipline, not
automatic. No false promise of coverage that doesn't exist.

## 4. `bible_research.db` table review applied (`#678`)

The researcher's full 150-row table-by-table review had nowhere to land: `cfg_table` had **no
`inactive` column at all** — traced to escalation `#310`'s own bootstrap, which had deliberately
excluded `cfg_table`/`cfg_column` as "schema-of-schema, not toggleable," never reconciled with
`governance.tables`' explicit requirement. New migration
(`add_cfg_table_inactive_column.py`) reverses the exclusion for `cfg_table` only. Applied the full
CSV as one governed batch: 55 changed to `inactive=1`, 95 already matched the new column's default,
0 missing — verified against the researcher's own data exactly.

## 5. A live, 29-day NAS backup incident — found while working an unrelated task, fixed the same session

Checking `#703` ("give iba.db its own dedicated backup, same location as research_db") turned up
`scripts/backup_db_to_nas.py`'s `DEFAULT_SOURCE` already silently pointing at `iba.db`, not
`bible_research.db`. Traced with `git blame`: an unrelated-sounding commit from 2026-07-19
(`216314b9`, "config->configurator restructure") made the change with no mention of backups at
all. The scheduled task passes no `--source`, so it's used this default the whole time — confirmed
against the NAS itself, not assumed: the most recent `bible_research_*.db` backup file was
byte-identical in size to `iba.db`, not `bible_research.db`. **`bible_research.db` had no
dedicated, integrity-checked NAS backup for ~29 days** — only the passive whole-folder mirror.

Root-fixed, not just reverted: restored the correct default, but also made the filename prefix,
pruning lineage, and alert job identity all DERIVED from `--source` instead of hardcoded, so a
future default-source change can't silently mislabel backups the same way again.
`notify_backup_alert.ps1`'s `-Job` `ValidateSet` widened (`dbbackup`/`dbbackup_iba`) so the two
databases' status/alerts can never overwrite each other. `iba.db` now has its own real, separate
scheduled task (`IBA DB Backup to NAS`, daily 18:10). Verified live: real backups run for both
databases, both confirmed correctly named/sized on the NAS. Residual, not cleaned up: ~29 days of
mislabelled `iba.db` snapshots remain on the NAS under `bible_research_` names — a bulk cleanup
needs its own explicit decision.

## 6. Content-index (round B) — built, refined per real findings, run for real

Predefined-key concordance over every `.md` file (`strong.strongNumber`/`stepGloss`,
`word_registry.word`) — see the plan's own §2 design decisions. A single `re` alternation over the
~9,300 gloss+word keys was tried first and hung outright, confirmed live before committing to the
tokenize+n-gram+set-lookup design actually shipped.

**Running the real rebuild surfaced a genuine design issue, not a performance bug alone**: one file
(the programme-prose extract, 144,866 lines) produced ~597,000 hits by itself — the project's own
analysis prose is saturated with the very biblical vocabulary being indexed. Stopped rather than
pushed through or silently descoped; taken to the researcher as a real finding. Response, built in
order: (1) a read-only size-profile report (7,874 files, 558.6 MB; 74 files ≥1MB hold 270.1 MB — 1%
of files, 48% of mass) so exclusions would be decided from real data, not a guess; (2) a governed
`cfg_content_index_exclude` table (not JSON — `cfg.py`'s own rule is the DB is the only config
source), "include all `.md` except."

Then three concrete refinements, each a direct researcher instruction: **exclude programme prose**
(folder-prefix pattern, covers the live extract + its `archive/` copy); **50MB auto-exclude by
default, manually releasable** (`content_index.exclude_size_threshold_bytes` + a symmetric
`cfg_content_index_size_override` table); **exclude glosses for any T2 cluster term** (T2 = "the
landing zone for codes not included in analysis" — filtered by STRONG, not gloss text, so a gloss
shared with a real-cluster term stays indexed; 9,165 → 7,951 distinct glosses).

Full rebuild run for real (background, ~26 min): **7,869 files, 14,118,338 rows**. Two costs
reported plainly, not smoothed over: **`iba.db` grew from ~675MB to 8.06GB**; and verified real
searches confirm `strong:H2734` is precise and fast (938 hits, 0.68s) while `gloss:compassion`/
`word:anger` are technically correct but not browsable (23,098 / 19,991 hits) — the project's own
subject matter saturates its own vocabulary regardless of filtering. Left for the researcher to
decide whether that's acceptable as delivered.

A live example of the trade-off, found by the researcher's own first test: `gloss:satan` returned
zero results — both Strong's codes glossed "Satan" (`H7854`/`G4567`) are T2-assigned, so correctly
excluded by the filter just built. Working as designed, and a concrete illustration of an open
question the researcher named directly: how "other beings" (non-human agents) should be handled is
still unresolved in the study's own thinking — left as-is for now, not acted on further.

`-Csv` added to `ContentIndex-Search.ps1` on request ("a simple powershell utility to produce a
search result to a csv") — the `.md` report caps at 500 rows for readability, so a common query
needs the untruncated CSV for real spreadsheet review. One real bug caught testing it: `run.py`'s
JSON nests every handler kwarg under `"counts"`, so `$res.csv_path` under `Set-StrictMode` failed —
fixed to `$res.counts.csv_path` before calling it done.

## 7. A structural `configmaint.propose` gap, found trying to use it, fixed — follow-on still open

Proposing the programme-prose exclusion failed: `'cfg_content_index_exclude' is not a recognised
cfg_* table`. `CFG_TABLES` (`handlers/configmaint.py`) is a hardcoded tuple, not derived from
`cfg_table` — checked and found **4 pre-existing tables** (`cfg_escalation`/`cfg_index`/
`cfg_method_rule`/`cfg_quality_check`) were ALSO missing, predating today entirely. Fixed by adding
all 6 names directly — not switched to a dynamic `SELECT FROM cfg_table`, because the 20
foundational `cfg_*` tables (`cfg_meta`, `cfg_table`, `cfg_setting`, ...) aren't themselves
registered in `cfg_table` yet, a separate, deeper backfill gap discovered while checking. Escalation
`#712` raised for that two-part follow-on; the researcher's own answer, *"set this as
configurable,"* is recorded but **not yet built** — genuinely open at close.

## Open at close

- **`#650`** (main-project/IBA filing consolidation) — on-hold, researcher's own deferral, unchanged.
- **`#654`** (move debate-pipeline tables `iba.db` → `research_db`) — on-hold, explicitly *"until
  work on analytic phase is restarted"* — this is the trigger item for the researcher's own next
  session, not a blocker.
- **`#668`** (cluster-assignment exceptions) — on-hold, researcher's own ruling: resolved via
  individual verse-context analysis during analysis work, not before it.
- **`#712`** (`CFG_TABLES` "set as configurable") — approved, not yet built.
- Content-index's two reported costs (`iba.db` at 8.06GB; common gloss/word queries returning very
  large result sets) — reported, not further acted on; the researcher's call on whether to refine
  further (result caps, rarity ranking, Strong's-only) is open.
- ~29 days of mislabelled `iba.db` snapshots still sit on the NAS under `bible_research_` names —
  not cleaned up, needs its own decision.
- The analysis pipeline itself (`VerseLexical.ps1`/`Debate-Run.ps1`, the `hib`/`phenomenon`/
  `operation` tables) was not touched or tested this session — today's work was entirely the
  governance/config/base layer. The researcher is aware significant work remains there and intends
  to do it as part of resuming analysis, not before.

**Researcher's own close**: *"I am sure there are some open ends, but it is time to move on"* —
explicit decision to shift focus to the analysis phase, restructuring work accepted as at a stable
enough point per the evidence above.

## Files touched, this session

**Code:** `iba/app/lib/escalation.py` (`answer_for_run` auto-resume, `write_list_report` rework),
`iba/app/lib/reportkit.py` (`write_report` plain-name refresh), `iba/app/lib/cfgquality.py`
(`tokenize.TokenizeError`→`TokenError` typo), `iba/app/handlers/configmaint.py` (`CFG_TABLES` +6),
`iba/app/lib/cfg.py` (`NonCompliantUtility`, `assert_utility_compliant`),
`iba/app/lib/narrativegenerate.py`/`wordregistryspanreport.py` (compliance-gate calls),
`iba/app/lib/contentindex.py` (new — full round-B module), `iba/app/handlers/reports.py` (+5
handlers: rebuild/search/size_profile for content-index, CSV export), `scripts/
backup_db_to_nas.py` (root-fixed default + derived naming), `scripts/notify_backup_alert.ps1`
(`-Job` widened). **Migrations (new):** `add_cfg_table_inactive_column.py`,
`bootstrap_content_index.py`. **PS (new):** `ContentIndex-Rebuild.ps1`, `-Search.ps1`,
`-SizeProfile.ps1`. **Docs:** `CLAUDE.md` §3/§9/§10, `iba/app/USER-GUIDE.md` §4.3/§4.4/§4.6/§13a/
§13b, `iba/app/BUILD.md` §130–144, `docs/governance-alignment-register.md`. **Data:** `wa_rule_
registry` (59 rows, all `obsolete=1`), `cfg_utility` (+343 registrations, 105 flagged
non-compliant), `cfg_table` (+`inactive` column, 55 `bible_research.db` rows flipped),
`content_index`/`content_index_scan` (new, 14.1M rows), `cfg_content_index_exclude`/`_size_
override` (new tables), `cfg_write_grant` (`report.debate` inactive), `backup.iba_db_gap` (config
row resolved). **Reports:** `wa-rule-registry-full-review-v1-20260817.md`,
`hardcoded-constants-sweep-20260817.md`, `unregistered-scripts-batch-registration-20260817.md`,
`cfg-table-inactive-applied-20260817.md`, `content-index-size-profile.md`, plus several
content-index search exports.
