# Session log — 2026-07-26 (continuation) — config-driven STEP rule, verse-analysis report built + registered, passage system retired, AMBIGUOUS false-positives fixed

**Session paused 2026-07-26 (running low on tokens) — the next session starts fresh, with no
memory of this conversation.** This log is a cold-start entry point: read it first, then follow its
pointers. Directly continues
[`SESSION-LOG-20260726-lexicon-parse-layer-span-model-fix-raw-backfill-strong-meaning-tree-root-cause.md`](SESSION-LOG-20260726-lexicon-parse-layer-span-model-fix-raw-backfill-strong-meaning-tree-root-cause.md)
(same calendar day, separate conversation — that log's own "where to start" items #2/#3 (the Dan
1:1-7 report usable now, progressive backfill workflow) are the starting point this conversation
picked up from).

---

## What this session did, in order

### 1. STEP live disambiguation added to the verse-span-meaning report, then a real process violation caught and fixed
Extended `tools/build_verse_span_meaning_extract.py`: whenever a span's `meaning_tree` was flagged
`[AMBIGUOUS]` (base shared with a sibling code), the report calls STEP's `call2_getInfo(code)` for
the EXACT code and shows its own resolved sense — the researcher's ask, working from `H3581B`
(Dan 1:4) rendering the wrong sense. **A real violation followed**: the first version let the
report degrade to a DB-only note when STEP was down, and was then *tested and reported as passing*
while STEP was actually down — the opposite of this app's stated rule ("runs refuse to start
without STEP"). Separately, GOVERNANCE.md/BUILD.md were not read at session start, only
`Start-Iba.ps1`'s one-line teasers. Both corrected: the report now refuses (no file written) if
STEP is down. Full detail: BUILD.md §19/§20.

### 2. `step.required_for_runs` made a real `cfg_setting` — the general standard set
Researcher's correction, general this time: *"ALL rules must be config driven. NO rules should be
specified only in Governance or Build or Memory or User Guide that is not in the config. Reading the
config MUST be a startup rule and MUST be executed with every startup instruction."* Two new
`cfg_setting` rows proposed via `configmaint.propose` (approval-gated — raised, then explicitly
approved by the researcher in this conversation, then applied):
- `governance.rules_must_be_config_driven` (module `governance`) — the general standard itself,
  read at every startup via `init.py`'s existing generic governance-module print.
- `step.required_for_runs=true` (module `step`) — the concrete fix: `init.py`'s STEP preflight and
  the report's `build()` both read this ONE row instead of each hardcoding "STEP is mandatory."
  Also fixed a second, independent bug found while wiring this in: `init.py` printed the right
  warning but `return 0`'d regardless of STEP's state — the exit code never actually enforced the
  stated rule. Now returns `1`/`NOT READY` when required and down. Full detail: BUILD.md §21,
  GOVERNANCE.md §16.

### 3. Verse-span-meaning report promoted from a `tools/` one-off to a real, registered, config-governed report
Researcher's request: a `verse-analysis` folder under `iba/app/`, sub-foldered by book, "included in
the app," folder location config-driven, not hardcoded. Built exactly on the established
report-registration pattern (GOVERNANCE.md §14): new `lib/versespanmeaningreport.py` (a separate
governed copy of the `tools/` script's logic, per the established "tools/ stays standalone, not
imported from" precedent — BUILD.md §17), new work package `verse-analysis-report` → step
`report.verse_span_meaning` → `handlers/reports.py:verse_span_meaning_report`, new PS wrapper
`VerseSpanMeaning-Report.ps1`. Output path fully config-driven: `report.verse_analysis_output_dir`
+ `report.verse_analysis_output_pattern` (both new `cfg_setting` rows), book subfolder is a
per-call parameter (`-BookLabel`, e.g. "Daniel"), not a setting — same boundary as `table_export`'s
`-Out`/`-Table`. Registered via a bootstrap migration (`migration/bootstrap_verse_analysis_report.py`,
idempotent), not `configmaint.propose` row-by-row, per the established infrastructure-registration
carve-out (§9B/§14) — the researcher's own request was the up-front design approval. A real latent
bug caught before shipping: copying the old bootstrap script's insert helpers verbatim would have
broken, since `cfg_setting`/`cfg_step` gained an `inactive` column after that script last ran; fixed
by naming columns explicitly. Full detail: BUILD.md §22.

**Reports generated this session** (all in `iba/app/verse-analysis/Daniel/`, regenerated again in
step 5 below after the ambiguity fix):
- `dan-1-1-7-verse-span-meaning.md`
- `dan-1-7-21-verse-span-meaning.md`
- `dan-2-1-16-verse-span-meaning.md` (49% meaning coverage — flagged, not backfilled this session;
  see "where to start" below)

### 4. The `passage`/`verse_passage` system retired — recorded, then cleared
Asked to "revisit the passages set of tables." Investigated live (not assumed): `passage`/
`verse_passage` were still config-active, but `passage.build()` derives boundaries entirely from
`span_candidate`, which the candidate system (retracted 2026-07-23, §15D) no longer maintains — a
real inconsistency. Three `passage.validate` escalations (`#195`/`#256`/`#262`) had sat open since
2026-07-21/22, all asking the same unanswered question about the 81%-single-verse distribution.
Researcher's ruling: *"the assembly of the passages is no longer based on the same premise... the
current data is no longer relevant and is getting in the way... there is nothing to migrate...not
worth [reconciling]."* Recorded FIRST (`reports/passage-system-retirement-record-20260726.md` + a
full verbatim CSV export of both tables, `reports/passage-retirement-export-20260726/`), THEN
retired: `migration/retract_passage_system.py` — 2 work packages/2 steps/5 settings/1 report row+2
sections/4 on_fail rows/2 write-grants → `inactive=1` (mirrors the candidate retraction's own
mechanism), AND `passage`+`verse_passage` (18,504 + 24,763 rows) soft-deleted — one step further
than the candidate precedent, per this specific ask. The three escalations answered `reject`,
pointing at the retirement record. No successor design proposed or assumed. Full detail: BUILD.md
§23.

### 5. The `[AMBIGUOUS]`/live-STEP-call logic itself was wrong — most flags were false positives
Researcher's direct challenge, working the Dan 2:1-16 report: *"why can you not resolve the meaning
from the parsings with H0935G. You know what H0935G renders, why do you first decide it is
ambiguous and then need to do a span call to resolve it."* Investigated and confirmed: `strong.
stepGloss` is fetched per EXACT code, never base-collapsed, so `H0935G`'s own gloss was already
correct the whole time. The `[AMBIGUOUS]` flag fired on "does ANY sibling exist," too blunt —
measured directly: of 470 sub-lettered codes with a sibling, **362 (77%) are same-root stem-splits**
(H0935G Qal "come" / H0935P Hiphil "bring" — one legitimate combined dictionary entry, not a
collapse), only **108 (23%)** are genuine collapses like the original `H3581A`/`H3581B`. Fixed in
both `lib/versespanmeaningreport.py` and `tools/build_verse_span_meaning_extract.py`: new
`gloss_supported_by_tree()` — only flag + call STEP when the code's own stepGloss shares NO
vocabulary with the shared tree. Verified re-running all three Daniel reports: Dan 2:1-16 8→0
genuine, Dan 1:1-7 22→2 genuine (`H3581B`, `H7227B`, both still correctly caught), Dan 1:7-21 31→2
genuine (`H7356B`, `H1524B`). Full detail: BUILD.md §24.

### 6. A real, unresolved misunderstanding — surfaced, not yet acted on
Researcher: *"I thought the rule is that the strongs not yet registered will automatically be
pulled into the Database when a new report is renerated, and that the process for this have already
been established."* Checked against BUILD.md §17 before answering: **no such rule exists** — this
was explicitly one of three options offered 2026-07-25 (bulk-pull / live-fetch-at-render-time /
progressive-persisted-as-its-own-step) and the researcher chose the THIRD, not the second. The
report is read-only; `Raw-Backfill.ps1 -Book <book> -Range <c:v-v>` is the separate, deliberate
command that does this (and, since §18, folds in the parsed-layer refresh automatically — its own
docstring was stale on this point, fixed this session, see Artifacts below). **Asked the researcher
directly whether to now wire backfill into report generation automatically, or keep it a separate
step as originally decided — not yet answered when the session paused.**

---

## Where to start a fresh session

1. **Unanswered question from step 6, ask again if not otherwise resolved**: does the researcher
   want `report.verse_span_meaning` to auto-run backfill for any gap in its range before rendering,
   or keep it a deliberate separate step (`Raw-Backfill.ps1`)? Do not assume either way.
2. **Dan 2:1-16's report sits at 49% meaning coverage**, un-backfilled — a live decision point tied
   directly to item 1 above (if backfill gets wired in, this resolves itself; if not, run
   `Raw-Backfill.ps1 -Book Dan -Range 2:1-16` manually before treating that report as complete).
3. **`strong_meaning_tree`'s underlying base-collapse root cause is STILL not fixed** (BUILD.md §19
   item 4, unchanged since 2026-07-25/26) — session 5's fix means the report no longer PAYS for it
   on the 77% of cases where it doesn't matter, but the actual schema decision (does
   `strong_meaning_tree` gain a `strong_variant`-keyed column, matching `candidate_seed`'s own
   earlier fix?) is still open, still needs deciding, not attempted this session.
4. **The "movement" definition is still open** (unchanged for several sessions running) —
   researcher working this manually; do not pre-empt.
5. **No new passage design proposed** (item 4 above) — the researcher is still working out how a
   future passage concept fits together; do not guess at or scaffold one.
6. `git status` after this log — stage only this session's own files (see Artifacts below), not the
   several pre-existing untracked items already sitting there before this conversation started (the
   session-log-folder relocation pairs, an "AI failures" research thread, "Passage read guidance"
   files, `iba/logs/WA-session-log-dan1-1-7-v1.0-2026-07-26.md`) — none of those are this session's
   work and their provenance wasn't investigated here.

## Artifacts this session

**Code** (`iba/app/`):
- `lib/versespanmeaningreport.py` (new), `handlers/reports.py` (extended),
  `migration/bootstrap_verse_analysis_report.py` (new), `migration/retract_passage_system.py` (new),
  `ps/VerseSpanMeaning-Report.ps1` (new), `ps/Raw-Backfill.ps1` (docstring corrected — stale
  "re-run Lexicon-Parse.ps1" instruction removed, §18 already folded that in),
  `tools/build_verse_span_meaning_extract.py` (STEP-required refusal, then the AMBIGUOUS-logic fix),
  `init.py` (STEP-required exit code now config-driven and actually enforced).

**Config** (via `configmaint.propose`, approved and applied): `governance.rules_must_be_config_driven`,
`step.required_for_runs=true`, `report.verse_analysis_output_dir`, `report.verse_analysis_output_pattern`
(the latter two via the bootstrap migration, not propose, per the infrastructure-registration
carve-out). Retired via direct migration (not propose, same carve-out): the whole `passage`/
`verse_passage` config surface, `inactive=1`.

**Data**: `passage` (18,504 rows) + `verse_passage` (24,763 rows) soft-deleted. Full CSV export kept
at `reports/passage-retirement-export-20260726/`.

**Reports**: `reports/passage-system-retirement-record-20260726.md`,
`verse-analysis/Daniel/dan-{1-1-7,1-7-21,2-1-16}-verse-span-meaning.md` (all regenerated after the
step-5 ambiguity fix — current versions reflect it), plus one intermediate one-off
`reports/dan-1-1-7-verse-span-meaning-20260726-v2.md` from before the report was registered.

**Docs**: `BUILD.md` §19–§24, `GOVERNANCE.md` §16, `USER-GUIDE.md` (STEP-required line) — all
updated in the same unit of work as their triggering code/config change, per
`governance.build_md_on_code_change`/`governance_md_on_rule_change`.
