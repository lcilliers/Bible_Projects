# Folder analysis — analytic-file management across the project

Prepared for escalation #929. **Scope:** every project folder holding analytic files (findings,
session logs, patches, extracts, analysis/design docs, reports) — not code, not raw source data,
not the SQLite databases themselves. **Aim, as instructed:** surface the different variations of
file management in use, as the basis for later consolidation — this document catalogues and
groups, it does not itself decide which pattern should win.

**Method:** every top-level directory walked (`find`/`ls`), analytic-bearing folders grouped by
structural pattern where many leaf folders share one (e.g. `Sessions-v2`'s 49 cluster folders,
`verse-analysis`'s 23 book folders) rather than listed 49/23 times over. Grouping is by naming +
archiving *convention*, not by owning system.

---

## 1. The folders, grouped by convention

| # | Location(s) | Content | Naming convention | Versioning | Archiving |
|---|---|---|---|---|---|
| A | `Workflow/Instructions/`, `Workflow/Global_rules/`, `Workflow/Catalogue/`, `Workflow/reference/`, `Workflow/registry/`, `Workflow/schema/`, `Workflow/methodology/`, `Workflow/Sessionlogs/`, `Sessions/Patches/` | Instruction docs, patches, session logs, methodology notes | `wa-{topic}-{qualifier}-v{N}-{YYYYMMDD}.md`/`.json`, lowercase, no dashes in date | Explicit `-v{N}-` in filename, integer, bumped on same-name reissue | Local `archive/` subfolder, sibling to the working folder |
| B | `iba/docs/` | Design proposals, method specs, narrative guidance | `WA-{Topic}-v{N}-{YYYY-MM-DD}.md`, Title-Case prefix, **dashed** date | `-v{N}-` in filename, same idea as A but different case/date format | No local `archive/` seen — superseded versions left in place alongside current, distinguished only by the version number in the name |
| C | `Logs/` | Session logs (current, mandated by `governance.session_log_dir`) | `SESSION-LOG-{YYYYMMDD}-{topic}.md`, all-caps prefix, no version number | None — one file per session, topic-suffixed instead of versioned | `Logs/archive/` subfolder, but holds *older-format* logs (`wa-...-sessionlog-v{N}-{date}.md`, pattern A) — i.e. the archive folder's own contents follow a different naming convention than the live folder it sits beside |
| D | `outputs/markdown/`, `outputs/csv/`, `outputs/json/`, `outputs/docx/`, `outputs/pdf/` | One-off reports, extracts, analyses (`governance.oneoff_report_dir`) | `{topic}-{YYYYMMDD}.md`, free-form topic, no prefix convention, no version number | Same-topic reissue relies on `-v{n}` being added by the author *if remembered* (per `docs/file-organisation-rules.md`'s "same-name = version bump" rule) — not structurally enforced | `outputs/archive/` (flat, one folder for the whole `outputs/` tree) — a **third** archiving shape: neither local-sibling (A) nor embedded-in-the-live-folder (C), but one shared archive for a whole top-level tree |
| E | `research/investigations/`, `research/discovery/`, `research/notes/`, `research/projects/`, `research/templates/` | Exploratory findings, STEP discovery pulls, investigation notes | Mixed: `{NNN}_{word}_step_data_{YYYYMMDD}.{json,md}` (numbered-prefix, `discovery/`) alongside free-topic `{Topic}-{YYYYMMDD}.md` (`investigations/`) — **two conventions inside the same top-level folder** | Ad hoc — some files carry a second date suffix for a redo (`002_agony_step_data_20260706.json` beside the original `...20260328.json`), no `-v{N}` | No archive subfolder in most of `research/`; `research/VE-lexical/` is the one exception, with its own `archive/`, `exploratory/`, `extracts/`, `findings/` split |
| F | `Sessions-v2/{M-code}-{Name}/` (49 folders, one per cluster) | Cluster analysis, data, essays, findings | Not filename-versioned — **the folder structure itself is the convention**: fixed subfolders `Analysis/`, `Data/`, `essays/`, `findings/` inside every cluster folder | Whatever's inside each subfolder follows its own local convention (not surveyed per-file at this depth — 49 folders × 4 subfolders each) | No archive subfolder pattern observed at this level |
| G | `verse-analysis/{book}/` (23 book folders + `characteristics/`, `_gate1-recovery/`, `_methodology/`, `_reports/`, `_synthesis/`, `_tracks/`) | Book-by-book debate work | Again folder-structure-as-convention, but a **different** fixed set than F: `_seg/`, `phase1-views/`, `readings/` | Local to each subfolder | No archive subfolder pattern observed at this level |
| H | `Sessions/Session_A/`, `Session_B/`, `Session_C/`, `Session_D/`, `Session_Clusters/` | The pre-`Sessions-v2` per-word/per-stage pipeline output (now read-only cross-reference per `CLAUDE.md` §2) | `Session_B/` alone has yet another shape: **numbered stage-prefix folders** (`01_Verse_Context_Process_input` … `12_Session_B_Status`) — a fourth folder-as-convention scheme, distinct from both F and G | N/A — frozen, historical | No archiving needed (already the historical record) |
| I | `iba/app/reports/` | Escalation histories, config reports, one-off analysis (governed by `governance.oneoff_report_naming_pattern`) | `{topic}-{YYYYMMDD}.{format}` generally, but escalation-history reports use `{id}-escalation-history-v{N}-{YYYYMMDD}.md` — numeric-id-first, its own sub-pattern within I | `-v{N}-` bumped per re-generation of the *same* report (e.g. `739-escalation-history-v3-...`) | `iba/app/reports/archive/` per `governance.oneoff_report_archive_dir` — config-declared, unlike every pattern above which is convention-only |
| J | Top-level `archive/` (`Clusters/`, `Logs/`, `Programme_prose/`, `References/`, `Sessions/`, `docs/`, `patches/`, `scripts/`) | A **second, separate** archive mechanism — a whole mirrored tree at the project root, alongside every local `archive/` subfolder named above | Mirrors whatever convention the source folder used | N/A | This *is* the archive — but it coexists with local `archive/` subfolders (A, C, I) doing the same job for their own areas; nothing distinguishes when a superseded file goes to its folder's local `archive/` versus this top-level one |
| K | `Workflow/Programme/programme_prose/`, `programme_analysis/`, `Corpus_prose/` | Programme-level prose extracts (superseded by the DB-canonical prose store, Chapter 4) | `wa-{topic}-{YYYYMMDD}.md`/`.json` pairs (md + json sibling for the same extract) | Date-suffix only, no `-v{N}` | Local `archive/` (pattern A) |
| L | `database/archive/` | One file: `file_manifest.json`, a frozen 2026-08-15 snapshot (superseded by IBA's own `file_manifest` DB table) | Single fixed filename, no date/version in the name at all | N/A — one frozen snapshot | Is itself the archive destination |
| M | `memory/` | Claude's own persistent memory mirror, one fact per file | `{type}_{kebab-case-slug}.md`, `type` = `feedback`/`project`/`reference`/`user` prefix | None — a memory is edited in place or superseded by editing the same file | None — memory files are corrected in place, not versioned/archived |

---

## 2. The variations, summarised

**Naming conventions in live use, project-wide:**
1. `wa-{topic}-{qualifier}-v{N}-{YYYYMMDD}` — lowercase, no-dash date (A, K).
2. `WA-{Topic}-v{N}-{YYYY-MM-DD}` — Title-Case, dashed date (B) — a near-duplicate of #1 with two independent surface differences (case, date format), not the same convention.
3. `SESSION-LOG-{YYYYMMDD}-{topic}` — all-caps, no version (C).
4. `{topic}-{YYYYMMDD}` — free-form, no prefix, no version (D, most of E).
5. `{NNN}_{word}_step_data_{YYYYMMDD}` — numbered-prefix (E/`discovery`).
6. `{id}-escalation-history-v{N}-{YYYYMMDD}` — numeric-id-first (I).
7. `{type}_{kebab-slug}` — no date at all (M).

**Versioning approaches:** explicit `-v{N}-` in the filename (1, 2, 6); a second date suffix standing in for a version (E); no versioning at all, same-name overwrite or topic-suffix instead (3, 4, 7).

**Archiving shapes — the most material inconsistency for consolidation:**
- **Local sibling** `archive/` next to the live folder (A, K, and I — I additionally has this declared in config, `governance.oneoff_report_archive_dir`, where every other local `archive/` is convention-only, undeclared anywhere).
- **One shared archive per top-level tree** (`outputs/archive/` for all of `outputs/`).
- **One project-root archive mirroring the whole tree** (top-level `archive/`, J) — coexisting with every local `archive/` above, no rule found anywhere naming which a given file should go to.
- **No archive at all** — superseded files left in place, distinguished only by a version number in the name (B), or never superseded because the folder is itself already a frozen historical record (H, L).
- **The archive folder's own naming convention doesn't always match its live folder's** — `Logs/archive/` holds files in convention #1 while `Logs/` itself uses convention #3.

**Folder-structure-as-convention** (F, G, H's `Session_B`) is a fourth organising principle entirely, orthogonal to filename convention — three different fixed-subfolder schemes across three different areas, none documented as a named pattern anywhere `grep`-able.

---

## 3. Governance already on record, and where it stops

`docs/file-organisation-rules.md` states the "same-name = version bump" principle (`CLAUDE.md` §9
item 4) — but this is a *rule about what to do*, not a scan of what has actually happened, and this
report is the first place the resulting variety has been laid out side by side. `governance.oneoff_report_dir`/`_archive_dir`/`_naming_pattern` (IBA's own config) govern exactly one of the
thirteen groups above (I) — everything else (A–H, J–M, spanning the large majority of the project's
analytic-file volume) has no config-level naming or archiving rule at all, only inherited convention.

This document does not propose which convention should become the standard, or whether the
top-level `archive/` (J) or the local-sibling pattern (A/K/I) should be the one kept — that is the
consolidation decision the researcher's instruction names as the next step, not something settled
here.
