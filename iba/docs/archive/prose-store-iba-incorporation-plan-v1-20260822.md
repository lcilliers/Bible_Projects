# Prose store — IBA incorporation build plan

**For escalation #784** (v8's instruction, 2026-08-21 chat turn — quoted in full in §1). Filed here
per the researcher's request to write the full build to a plan for review before applying anything
further. Note: the researcher's message said "use 874 to record and reference" — read as a typo
for **#784** (the escalation this whole thread lives under; no #874 exists — max escalation id is
787 as of writing). Flag if that reading is wrong.

**Status: code written and tested (read-only against the live DB, verified below). Config changes
NOT YET APPLIED — 13 approval-gated `configmaint.propose` proposals are needed; 1 is already raised
(#787) and pending your decision; 12 more are specified in full in §3, not yet submitted.**

---

## 1. The instruction this plan implements

Researcher, 2026-08-21 (recorded verbatim on escalation #784 v8):

> "staying in #784 you have rightly identified that the tables, columns and scripts are not
> incorporated in IBA. activate the 4 scripts, make them compliant, activate the tables and
> columns, and align it with the architecture. add this chat content to comment as the
> instruction."

Facts established before building anything (per `feedback_iba_gap_analysis_requires_live_build_
inspection` — inspect live code+DB, don't guess):

- `cfg_table`/`cfg_column` already fully catalogue `prose_section` and its five siblings —
  `inactive=0` throughout. There is no dormant flag on the tables/columns themselves to "activate".
- Zero `iba/app/handlers/*.py` or `iba/app/lib/*.py` code touched `prose_section` before this
  build (confirmed by grep — only docs/reports/migration-scripts mentioned the string). No
  `cfg_step`/`cfg_work_package` row named anything `prose*` existed.
- `cfg_write_grant` had exactly 2 rows for the whole prose domain (`cfg_prose_chapter`,
  `cfg_prose_concept`, both `configmaint.propose`-only) — nothing for `prose_section` itself. Its
  writer vocabulary (`candidate.load`, `cluster.assign`, `lexicon.parse`, ...) is exclusively
  `cfg_step`-dispatched IBA steps; `prose_section` is written through a different, legacy path
  (a PROSE-type patch applied by `scripts/apply_session_patch.py`, the project-wide universal patch
  applicator) that was never brought under that governance layer.
- `cfg_utility` had all 15 prose-related script rows `inactive=1`; 4 of those (including 2 of the
  4 named scripts) additionally carried a `NON-COMPLIANT (escalation #648)` flag for hardcoded
  module-level constants that should be `cfg_setting`-driven.

Conclusion: **"activate the tables and columns" means give them a real, live IBA consumer** — the
schema catalogue described them; nothing operated on them. That is the gap this build closes.

---

## 2. Code already written and tested (no config changes yet — these files exist on disk now)

All four items below were exercised directly against the live `bible_research.db` this session.
Every read path (extract/search/export) produced correct output; the one write-adjacent path
(import) confirmed it writes a patch file only — `database/bible_research.db`'s mtime was checked
unchanged before and after.

### 2.1 `iba/app/lib/prosestore.py` (new file)

The real, shared implementation — ported from the four scripts with two changes: (a) the DB
connection goes through `cfg.database_path('bible_research')` instead of a hardcoded path (the
first real operational consumer of that setting beyond `init.py`'s startup drift check), and (b)
the four constants flagged under escalation #648 are read from `cfg_setting` with the original
values kept as in-code fallback defaults, never a silent behaviour change. Exposes:
`run_extract`, `run_search`, `run_export_chapter`, `run_import_chapter` (plus the lower-level
functions each composes).

### 2.2 `iba/app/handlers/prose.py` (new file)

Four thin `def h(ctx) -> Outcome` adapters (`extract`, `search`, `export_chapter`,
`import_chapter`) over 2.1, following the exact contract every other registered work package uses
(`iba/app/handlers/base.py`; modelled directly on `iba/app/handlers/reports.py`).

### 2.3 `iba/app/ps/Prose.ps1` (new file)

PS wrapper following the `Reports.ps1` template (`-Step Extract|Search|ExportChapter|
ImportChapter`) — every existing work package has one (`cfg_work_package.ps_script` is `NOT NULL`
on every live row), so this keeps the pattern rather than being a special case. **Not yet
reachable** — `python -m iba.app.run prose ...` will refuse to dispatch until §3's `cfg_work_
package`/`cfg_step` rows exist (`run.py`'s dispatch gate treats an unknown package as
inactive/unroutable).

### 2.4 The four `scripts/*.py` CLI files — rewritten, not replaced

Each is now a thin argparse wrapper that imports its logic from 2.1 instead of defining it
locally. The documented CLI usage in `docs/prose-store-architecture.md` §8 is unchanged (same
flags, same default output paths) — verified live:

| Script | Test run | Result |
|---|---|---|
| `build_programme_prose_extract.py --book Programme --also-markdown` | ✅ | `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260821.{json,md}` — 51 types, 51 sections |
| `search_prose.py grace --limit 3` | ✅ | `outputs/markdown/prose-search-grace-20260821.md` — 3 of 146 shown |
| `export_prose_chapter_edit.py --book Programme --chapter 1` | ✅ | `outputs/markdown/prose-edit-programme-chapter-1-20260821.md` — 6 sections |
| `import_prose_chapter_edit.py <the file above>` (unmodified round-trip) | ✅ | valid PROSE-supersede patch, 6 sections validated, **`database/bible_research.db` mtime unchanged** |

The same four operations were also exercised **directly through the new handler functions**
(`iba.app.handlers.prose.extract/search/export_chapter/import_chapter`, bypassing the not-yet-
registered dispatcher) with a second chapter (Programme ch.2) and a "inner being" search — all four
returned `ok`, all four produced correct output, the DB write-adjacent one again left the DB file
untouched.

**Nothing here required a config change to build or test** — the fallback defaults inside
`prosestore.py` make it behave exactly as the old hardcoded scripts did until §3 is applied.

---

## 3. Config changes — NOT YET APPLIED, full literal payload for review

Every `configmaint.propose` call is single-row and approval-gated; the dispatcher additionally
enforces **strict serialisation** — a raised-but-unanswered proposal blocks every subsequent
`configmaint.propose` call outright (confirmed live: proposal #2 below was attempted and refused
with `PermissionError: ... blocked by unresolved escalation #787`). So these 13 changes can only be
applied one at a time, each waiting on its own `Escalation.ps1 -Action AnswerRun` decision — this
plan exists so that decision can be made once, over the whole batch, by reading the actual content
below, rather than 13 separate blind approvals.

### 3.1 Already raised — escalation #787, pending

| Table | Op | Where | Set |
|---|---|---|---|
| `cfg_setting` | insert | `{}` | `{"value": "\"1.1\"", "module": "prose", "use": "prosestore.extract's JSON meta.extractor_version -- escalation #648 compliance fix, was a module-level constant in build_programme_prose_extract.py"}` |

Question on file: *"New cfg_setting 'prose.extractor_version' = '1.1' -- the prose-extract JSON
meta.extractor_version, was hardcoded EXTRACTOR_VERSION in scripts/build_programme_prose_extract.py,
flagged NON-COMPLIANT by escalation #648. Part of #784's incorporation of the prose store into IBA.
Module='prose' chosen over cfg_prose_chapter/cfg_prose_concept (prose's dedicated tables) because
this is a tooling/runtime constant, not chapter-registry data."*

### 3.2 Not yet submitted — cfg_setting inserts (2 more)

**`prose.chapter_names`**

| Table | Op | Where | Set |
|---|---|---|---|
| `cfg_setting` | insert | `{}` | `{"value": "{\"0\":\"Preamble\",\"1\":\"Programme purpose\",\"2\":\"Research methodology\",\"3\":\"Research approach\",\"4\":\"Data architecture\",\"5\":\"Data integrity & governance\",\"6\":\"Instruction corpus\"}", "module": "prose", "use": "prosestore chapter-number -> name map, used by extract/docx rendering -- was hardcoded CHAPTER_NAMES in build_programme_prose_extract.py, escalation #648"}` |

**`prose.book_stage_map`**

| Table | Op | Where | Set |
|---|---|---|---|
| `cfg_setting` | insert | `{}` | `{"value": "{\"Programme\":[\"programme\"],\"Detail design\":[\"session_a\",\"session_b\",\"session_b_phase9\",\"session_c\",\"session_d\"],\"Findings\":[\"synthesis\",\"verse-analysis\"],\"Essays\":[\"essay\"]}", "module": "prose", "use": "prosestore book_label -> allowed source_stage set, used to validate --book on extract -- was hardcoded BOOK_STAGE_MAP in build_programme_prose_extract.py, escalation #648"}` |

**`prose.search_default_limit`**

| Table | Op | Where | Set |
|---|---|---|---|
| `cfg_setting` | insert | `{}` | `{"value": "100", "module": "prose", "use": "prosestore.search's default result cap when --limit/-Limit is omitted -- was hardcoded DEFAULT_LIMIT in search_prose.py, escalation #648"}` |

### 3.3 cfg_utility updates (4) — activate the scripts

All four: `Where = {"file_path": "<path>"}`, `Set` includes `"inactive": 0` plus a `purpose` string
replacing the current `INACTIVE 2026-08-18 (escalation #729)` / `NON-COMPLIANT (escalation #648)`
prefix now that both are resolved.

| file_path | new `purpose` |
|---|---|
| `scripts/build_programme_prose_extract.py` | "Programme-stage prose extract (JSON/MD/DOCX) from prose_section_type + prose_section. Reactivated 2026-08-21 (escalation #784): EXTRACTOR_VERSION/CHAPTER_NAMES/BOOK_STAGE_MAP moved to cfg_setting (module='prose'), resolving the escalation #648 NON-COMPLIANT flag. Core logic now in iba/app/lib/prosestore.py, also reachable via the registered 'prose' work package (prose.extract)." |
| `scripts/search_prose.py` | "Search prose_section across all prose books via FTS5. Reactivated 2026-08-21 (escalation #784): DEFAULT_LIMIT moved to cfg_setting 'prose.search_default_limit', resolving the escalation #648 NON-COMPLIANT flag. Core logic now in iba/app/lib/prosestore.py, also reachable via the registered 'prose' work package (prose.search)." |
| `scripts/export_prose_chapter_edit.py` | "Export one current prose chapter or section as an editable Markdown file. Reactivated 2026-08-21 (escalation #784) -- no hardcoded constants were flagged for this file. Core logic now in iba/app/lib/prosestore.py, also reachable via the registered 'prose' work package (prose.export_chapter)." |
| `scripts/import_prose_chapter_edit.py` | "Turn an edited prose chapter Markdown file into a PROSE supersede patch (no DB write). Reactivated 2026-08-21 (escalation #784) -- no hardcoded constants were flagged for this file. Core logic now in iba/app/lib/prosestore.py, also reachable via the registered 'prose' work package (prose.import_chapter)." |

### 3.4 cfg_work_package insert (1) — register the `prose` package

| Table | Op | Where | Set |
|---|---|---|---|
| `cfg_work_package` | insert | `{}` | `{"name": "prose", "ps_script": "iba/app/ps/Prose.ps1", "runs_over": "none", "chained": 0, "inactive": 0}` |

### 3.5 cfg_step inserts (4) — register the four operations

All four: `scope = "global"` (not word/book-scoped — `Book`/`Chapter` are optional filter params,
matching how other non-word utility reports like `report.schema_overview` are scoped), `kind =
"utility"`.

| ordinal | step | handler | does |
|---:|---|---|---|
| 0 | `prose.extract` | `iba.app.handlers.prose:extract` | "Programme-stage prose extract (JSON, optional MD/DOCX) from prose_section_type + prose_section." |
| 1 | `prose.search` | `iba.app.handlers.prose:search` | "FTS5 search across active, non-superseded prose sections." |
| 2 | `prose.export_chapter` | `iba.app.handlers.prose:export_chapter` | "Export one current prose chapter/section as an editable Markdown file." |
| 3 | `prose.import_chapter` | `iba.app.handlers.prose:import_chapter` | "Validate an edited prose chapter file and generate a PROSE supersede patch (no DB write)." |

Each `Set` (table = `cfg_step`, op = `insert`, `Where = {}`):
`{"work_package": "prose", "ordinal": N, "step": "<step>", "handler": "<handler>", "scope": "global", "does": "<does>", "kind": "utility"}`

No `cfg_on_fail` rows are proposed — a missing row defaults to `report-stop` (confirmed in
`run.py`), which is the correct terminal behaviour for the one failure condition these handlers can
raise (`bad-params`).

### 3.6 Not attempted — no `cfg_write_grant` row proposed

Considered and deliberately **not** proposed: `cfg_write_grant`'s writer vocabulary is
`cfg_step`-dispatched steps that write directly via `Cfg`/`Db`. None of the four new prose steps
write to `prose_section` — three are read-only and `prose.import_chapter` only emits a patch file
(the actual write still happens through `scripts/apply_session_patch.py`, unchanged, outside this
governance layer, exactly as before this build). Adding a grant that nothing exercises would be
inert config, not a real incorporation — flagging this explicitly rather than silently omitting it.

---

## 4. Still to do after §3 is applied (part of "align with the architecture")

Per `governance.build_md_on_code_change`, `BUILD.md` needs a new section recording this build in
the same unit of work as the code — not yet written, held until config is confirmed applied so the
entry can state the real, final `cfg_step`/`cfg_setting` state rather than a plan.

`docs/prose-store-architecture.md` §8 (Retrieval) currently describes the four scripts as
standalone CLI tools with no mention of IBA. Once §3 is applied, that section needs a short
addition: the same four operations are now also reachable via `Prose.ps1` / `python -m iba.app.run
prose --step ...`, with `iba/app/lib/prosestore.py` named as the canonical implementation the CLI
scripts now delegate to. Not done yet — held for the same reason as BUILD.md.

---

## 5. What I need from you

1. Confirm the "#874" → "#784" reading, or correct it.
2. Review §3's literal payloads (13 proposals: 1 pending, 12 not yet submitted).
3. Decide how the 13 approvals get answered: you answer each `AnswerRun` yourself, or you authorise
   me to self-answer (as Claude, on the record, citing this plan) since you've now reviewed the
   exact content in writing.
4. On approval, I run §3 in order (3.1 already raised → 3.2 → 3.3 → 3.4 → 3.5), each proposal
   answered before the next is submitted (the serialisation is mechanical, not optional), then §4.
