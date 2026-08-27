# Config folder-destination alignment — extract for review (v1, 2026-08-27)

> Filed here (`outputs/escalation/`) per your instruction this session that this is the folder for
> all escalation reports and investigations. Escalation: [#929](../../iba/app/reports/escalation-list-v10-20260827.md)
> ("Folder analysis"), following your caution that the folder reorg may have made prior folder
> analysis / config folder-destinations stale.

## 1. Context — this isn't a fresh gap

Escalation **#863** (2026-08-26) already investigated this exact class of question — "does cfg_\*
actually govern where files go?" — and its finding was **superseded into #736** ("Main-Project /
IBA Filing Consolidation"), currently **on-hold** ("until escalation usage has stabilised"). Its
scope plan is filed at
[`iba/docs/file-naming-and-location-governance-plan-v1-20260826.md`](../../iba/docs/file-naming-and-location-governance-plan-v1-20260826.md).
Headline finding from that thread, still true today: **no `cfg_folder_purpose`-style table exists**
covering project folders generally — only two narrow IBA-only mechanisms
(`report.version_on_regenerate`, `governance.oneoff_*`) exist, both scoped to `iba/app/reports/`
report-writing code, never wired to the rest of the project.

This extract re-checks the live `cfg_setting`/`cfg_report`/`cfg_utility` state against the
post-reorg filesystem directly (not from memory or prior docs), per your instruction.

## 2. IBA-side folder/file-path settings (`cfg_setting`) — all still resolve

All 33 active path-shaped settings were checked against the filesystem after the reorg. **None are
broken** — the reorg moved `Logs/`, `Workflow/Chat_responses/`, `outputs/*`, `iba/docs/`, `memory/`,
`research/VE-lexical/` archival subfolders; it did not touch code, config-registered script paths,
or the databases.

| key | module | current value | **decided target** |
|---|---|---|---|
| governance.oneoff_report_dir | governance | `iba/app/reports/` | `outputs/[sub-folder]` — **catch-all only, for reports that fit none of the named buckets**; shrinks as its current callers get individually reclassified (see "still outstanding" below) |
| governance.scripts_ps_dir | governance | `iba/app/ps` | **decision recorded: `scripts/ps`** — see code-relocation caution below, not applied |
| governance.scripts_python_dir | governance | `iba/app/tools` | **decision recorded: `scripts/tools`** — see code-relocation caution below, not applied |
| *(no existing setting)* | — | `iba/app/lib` | **decision recorded: `scripts/lib`** — no `cfg_setting` currently governs this path at all; would need a new setting added, not just a value change |
| governance.session_log_dir | governance | `Logs/` | **confirmed unchanged**, `Logs/[sub-folder if applicable]` — which subfolders, if any, not yet specified |
| database.bible_research.path | database | `database/bible_research.db` | out of scope — the DB file itself, not a report; parked separately (see prior chat exchange) |
| database.iba.path | database | `iba/app/db/iba.db` | out of scope — same as above |
| behaviour.list_report_path | behaviour | `iba/app/reports/behaviour-rules-list.md` | **still outstanding** — general/config-health, not book/cluster/registry/raw_data; your own placeholder was `outputs/configs/...`, not yet finalised |
| configmaint.report_path | configmaint | `iba/app/config/CONFIG-REPORT.md` | **still outstanding** — same reason |
| content_index.report_path | content_index | `iba/app/reports/content-index-rebuild.md` | **still outstanding** — same reason |
| content_index.size_profile_report_path | content_index | `iba/app/reports/content-index-size-profile.md` | **still outstanding** — same reason |
| cluster.quality_report_path | cluster | `iba/app/reports/cluster-assign.md` | `_analytics/Clusters/` |
| lexicon.quality_report_path | lexicon | `iba/app/reports/lexicon-parse.md` | `research/discovery/lexicon-parse.md` |
| manifest.report_path | manifest | `iba/app/reports/file-manifest.md` | `research/discovery/file-manifest.md` |
| method.inner_being_narrative_guidance_path | method | `iba/docs/WA-inner-being-narrative-guidance-v1-2026-07-28.md` | `workflow/instructions/` (confirmed unchanged) |
| method.interpretation_questions_path | method | `iba/docs/WA-interpretation-questions-v1.4-2026-08-02.md` | `workflow/instructions/` (confirmed unchanged) |
| method.passage_read_guidance_path | method | `iba/docs/WA-passage-read-guidance-v1.5-2026-08-02.md` | `workflow/instructions/` (confirmed unchanged) |
| method.narrative_hard_constraints_path | narrative | `iba/docs/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` | `workflow/instructions/` (confirmed unchanged) |
| narrative.scope_check_report_path | narrative | `iba/app/reports/book-narrative-scope-check.md` | **still outstanding** — single rolling file, not really per-book (see chat); tentatively `research/discovery/` but your call |
| narrative.usage_log_path | narrative | `iba/app/reports/export/narrative-generate-usage.csv` | **still outstanding** — single cross-book audit CSV, doesn't fit a per-book `[book]` slot; suggest `_analytics/Bible_Books/narrative-generate-usage.csv` sitting beside the book folders rather than inside one, but flagging rather than deciding for you |
| report.cluster_path | report | `iba/app/reports/cluster.md` | `_analytics/Clusters/cluster-overview.md` |
| report.registry_path | report | `iba/app/reports/registry.md` | `_analytics/Registry/registry-overview.md` |
| report.schema_overview_path | report | `iba/app/reports/schema-overview.md` | `workflow/schema/` — "database reports" |
| report.seed_candidate_path | report | `iba/app/reports/seed-candidate.md` | `research/discovery/seed-candidate.md` |
| report.span_analysis_path | report | `iba/app/reports/span-analysis.md` | `research/discovery/span-analysis.md` |
| report.strong_meaning_path | report | `iba/app/reports/strong-meaning.md` | `research/discovery/strong-meaning.md` |
| report.output_dir (→ `report.word`, per-registry-word) | report | `iba/app/reports` | `_analytics/Registry/[word]` |
| report.strong_verse_output_dir | report | `iba/app/verse-analysis/word_registry` | `_analytics/Registry/[word]` |
| report.word_registry_span_output_dir | report | `iba/app/verse-analysis/word_registry` | `_analytics/Registry/[word]` |
| report.verse_analysis_output_dir | report | `iba/app/verse-analysis` | `_analytics/Bible_Books/[book]` |
| retention.report_path | retention | `iba/app/reports/log-retention.md` | `research/discovery/log-retention.md` |
| table_export.output_dir | table_export | `iba/app/reports/export` | `_raw_data/[sub-folder]/[group]` — raw table dump; exact sub-folder name not yet given |
| validation.output_dir (→ `validation.book`) | validation | `iba/app/reports` | `_analytics/Bible_Books/[book]` — **needs a code change**, see split note below |
| validation.output_dir (→ `validation.word`) | validation | `iba/app/reports` | `_analytics/Registry/[word]` — **needs a code change**, see split note below |

**`validation.output_dir` split — flagged, not yet buildable as a value edit.** One `cfg_setting`
currently serves both `validation.book` (book-specific) and `validation.word` (registry-specific) —
your rule sends them to two different `_analytics/[type]/` trees, which a single setting can't do.
Needs either two new settings (`validation.book_output_dir` / `validation.word_output_dir`) or
equivalent code change in `validation.py`, not a config-only move — same shape of dependency as the
`report.strong_verse_output_dir` family already being registry-specific despite living under a
book-shaped folder name today.

**`governance.scripts_ps_dir` / `_python_dir` (+ the un-configured `iba/app/lib`) — decision
recorded, NOT a simple repoint.** Unlike every report-path setting above, these name **code**
locations, not output destinations. `iba/app/tools` and `iba/app/lib` are live Python package
namespaces (`iba.app.tools`, `iba.app.lib`) imported throughout the app — moving them means editing
every `import`/`python -m` reference, not just a config value, plus every `cfg_utility.file_path`
row (51 active), every PowerShell script's relative cross-references, `.gitignore` if applicable,
and the `CLAUDE.md`/`GOVERNANCE.md`/`USER-GUIDE.md` text that names these paths directly. Same risk
class as the `iba.db` relocation question from earlier this session — recording the decision here,
but treating it as its own scoped project (backup first, full reference sweep, verify every entry
point), not something to fold into this report-path pass.

`cfg_report.archive_dir` is uniform across all 22 active report types — always the literal
`"archive"`, i.e. each report's own output dir plus `/archive`. No per-report override exists, so
no discrepancy there.

`cfg_utility.file_path` — 51 active rows checked, **0 stale**.

## 3. The live discrepancy — escalation reports specifically

| | config says | you say (this session) | physical reality |
|---|---|---|---|
| Escalation report destination | `iba/app/reports/` (`escalation.list_report_path`, `escalation.history_report_dir`, `governance.oneoff_report_dir`) | `outputs/escalation` = the folder for **all** escalation reports and investigations | **both folders are live and hold different things right now:** `outputs/escalation/` holds 36 hand-filed investigation write-ups (accumulated across sessions, never written by `Escalation.ps1` itself); `iba/app/reports/` + its `archive/` holds 183 archived + 3 current escalation-report files that `Escalation.ps1 -Action List/History` actually writes (config-governed, versioned, auto-archived) |

This is the same split #863/#736 already diagnosed in general — here it's concrete and specific to
escalations. Nothing in `cfg_*` currently points `Escalation.ps1`'s own output at `outputs/escalation`.

## 4. Main-project-side folders — zero config representation

`docs/`, `outputs/` (and all its subfolders — `escalation`, `markdown`, `csv`, `docx`, `archive`),
`Sessions-v2/`, `Workflow/`, `research/`, `Logs/`, `archive/` at project root have **no**
`cfg_setting`/`cfg_behaviour_rule` row naming them at all. They're governed only by CLAUDE.md §2's
directory map and `docs/file-organisation-rules.md` — the latter last touched 2026-06-27, predating
several methodology resets per #863's own finding, and itself a mix of still-live general principles
and dead methodology-specific patterns.

## 5. Decision needed from you

Given `outputs/escalation` is now stated as canonical for escalation reports and investigations,
three ways to reconcile it with what's currently config-driven:

**(a)** Repoint `escalation.list_report_path` / `escalation.history_report_dir` /
`governance.oneoff_report_dir` (or add an escalation-specific override) to `outputs/escalation`,
and migrate the 183 files currently in `iba/app/reports/archive` + 3 in `iba/app/reports/` there.

**(b)** Keep `outputs/escalation` as the main-project-side home for investigation write-ups only
(like this document); leave `Escalation.ps1`'s own operational report output
(`escalation-list.md`/history reports) in `iba/app/reports/` where IBA's own report machinery
expects it.

**(c)** Something else.

This is also the natural point to reconsider whether **#736** (on-hold "until escalation usage has
stabilised") should come off hold — you're actively re-declaring canonical folders right now, which
is the condition that plan was waiting on.

No config changes made in producing this extract — read-only investigation only, per your
instruction not to assume a folder destination until baselines are reset.
