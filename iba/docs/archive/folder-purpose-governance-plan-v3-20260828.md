# Folder-purpose governance mechanism — plan (v3)

> Escalation #971 (consolidates #929 v8 / #736 v7 carryover, researcher's own instruction to combine
> into one item). This is **a plan for the researcher's decision, not a build** — nothing here is
> implemented yet. **Supersedes v2 (2026-08-28) in full** — v2 corrected the folder-registry table's
> classification (Part C); this version adds Part E (a real config gap this same session's own filing
> surfaced) and points Part C's design at a live folder census for the researcher to set the right
> granularity. Full proposal, not a delta — this document stands alone.

## 0. What #971 consolidated

1. `docs/` — 36 flat files at the project root, no subfolders/archive/naming convention. Main-project
   side, not IBA. The folder census's own 14th pattern, never addressed.
2. #736's own unbuilt gap: a project-wide `filing` `cfg_behaviour_class` + `cfg_behaviour_rule` rows +
   a shared utility generalising `oneoff_path()` + a `configmaint.validate` naming-drift check — fully
   spec'd already in [`file-naming-and-location-governance-plan-v1-20260826.md`](file-naming-and-location-governance-plan-v1-20260826.md)
   §2–§3 (escalation #863), approved in scope but never built.
3. The researcher's own framing this round: a mechanism — "likely a `cfg_folder_purpose` table naming
   every live project folder's intended purpose, **paired with a utility that maps files against
   it**... so we can maintain better overall control of folders." **That utility already exists and
   is in scope here, not a separate later step**: `manifest.py`/`file_manifest` is precisely "a
   utility that maps files against" a folder registry — it walks the whole tree and classifies every
   file by folder today, just off hardcoded rules instead of a governed table. Item 3 IS the
   manifest-integration work; it was never a separate add-on to bolt on afterward.
4. **Added this round:** while filing this plan itself, the researcher caught a real, unresolved
   config gap — where an escalation-associated *deliverable document* (a plan, this document included)
   should be filed is not actually settled by any live rule, only assumed by precedent. Folded into
   Part E below, and generalised: the same ambiguity plausibly exists for other tool-specific
   `*_report_path`/`*_dir` settings, not escalation alone.

## Part A — adopt v1's filing mechanism (item 2 above), as already scoped, plus one new rule (item 4)

No new design needed for the original four — v1 §2 already specifies them cleanly:

1. New `cfg_behaviour_class` row `filing` (naming shape, snapshot-vs-living distinction, archiving
   triggers, the five Claude Code filing obligations — general principles only, not the
   methodology-specific `docs/file-organisation-rules.md` §2.2/§3 patterns, which stay legacy prose).
2. `cfg_behaviour_rule` rows under `filing`, one per principle.
3. `filingkit.versioned_path()` — generalises `reportkit.oneoff_path()`'s same-day `-v{n}` bump /
   archive-before-write / collision handling for **any** caller project-wide, not just
   `iba/app/reports/`.
4. `configmaint.validate` check: flag writes that hand-imitate the naming pattern instead of calling
   the shared utility (advisory, doesn't block — same pattern as every other `configmaint.validate`
   finding).

**5. New this round — a `cfg_behaviour_rule` closing the tool-report-vs-deliverable-document
ambiguity (Part E, detailed below):** auto-generated tool output (an escalation list/history export, a
`CONFIG-REPORT.md`, a validation run's report) stays under that tool's own `*_report_path`/`*_dir`
setting; an authored deliverable produced *while working* an item (a plan, design doc, gap analysis,
investigation write-up) — even one an escalation comment links to — follows
`governance.engineering_documentation_folder` instead, and is referenced from the item's
comment/context/resolution field, never refiled under the tool's own report folder.

**Recommendation: build all five now.** Items 1–4 were already approved in scope (v1 stopped at
"approve scope, I'll build §2 next round"); item 5 is new but the same shape of rule, same class,
same build.

## Part B — is `docs/` in scope?

**Recommendation: yes.** It's item 1 above, named explicitly in #971's own raise, and it's the same
kind of gap Part A's mechanism is built to close (a live project folder with files in it and no
naming/archiving discipline). Once Part A's `filing` rules exist and Part C's folder registry exists,
`docs/` gets one row in each like any other governed folder — it does not need its own special-cased
mechanism. No separate content-taxonomy decision needed unless the researcher wants one (e.g.
reorganising `docs/` into subfolders by topic) — that would be a physical-reorg pass, same category as
the #929 sweep, layered on top of this governance mechanism rather than blocking it.

## Part C — the folder registry: a reference/data table, not a `cfg_*` config table

**Corrected from v1, per researcher feedback:** v1 proposed `cfg_folder_purpose` as a `cfg_*` table,
which would put every row change through the full `Config-Maintenance.ps1 -Step Propose` rigor
(propose → validate → escalate → apply, human approval per change) — the same weight as an operational
*rule*. That's the wrong category. A folder registry states **facts about the project's own
structure** — which folders exist and what they hold — the same kind of thing `books`
(`bible_research.db`) states about the 66 canonical books: reference data that can change (a folder
gets added, retired, renamed) but isn't itself a policy decision requiring per-row governance.

**Confirmed live, same pattern already in use:** `books` is registered in `cfg_table` — as
`governance.tables` requires of *every* table in the project — with `use`: *"The 66 books of the Bible
as canonical reference data... Fully populated and stable."* It is not `cfg_`-prefixed, and its rows
are not maintained through `configmaint.propose`. This is the exact template for the new table.

**Table name: `folder_purpose`** (not `cfg_folder_purpose` — dropping the `cfg_` prefix is the whole
point of the correction). Lives in `iba.db` alongside `file_manifest`, one row per governed folder:

| column | type | purpose |
|---|---|---|
| `folder_path` | TEXT, PK | Project-root-relative prefix, POSIX slashes, no trailing slash (`iba/docs`, `_analytics/word_registry`, `outputs/configs`) |
| `purpose` | TEXT | One-line statement of what belongs here (mirrors `cfg_table.use`/`cfg_column.use` phrasing) |
| `manifest_category` | TEXT | The `file_manifest.category` value this folder should classify as (Part D) |
| `manifest_currency` | TEXT | The `file_manifest.currency` value this folder should classify as |
| `owning_settings` | TEXT, nullable | Free-text list of the `cfg_setting` keys that already point utility output here (e.g. `report.cluster_path, report.strong_verse_output_dir`) — a cross-reference for a human reading the table, not an enforced FK (see below) |
| `active` | INTEGER | 0 once a folder is retired/superseded — never deleted, matching `governance.tables`' "inactive, not removed" convention |
| `added_at` | TEXT | When the row was created — matters more here than in most reference tables, since folders genuinely do come and go over the project's life |

**Maintenance model:** direct INSERT/UPDATE via a dedicated function (`folderpurpose.py`, alongside
`manifest.py`) and a thin PS front door (`Manifest-Rebuild.ps1 -Step SetFolderPurpose` or a small new
`FolderPurpose.ps1 -Action Set/List/Retire`) — no `configmaint.propose` cycle for ordinary additions,
same as nothing gates adding a row to `books`. The **one** config touchpoint is the standing
`cfg_table`/`cfg_column` registration entry for `folder_purpose` itself (required of every table,
`governance.tables`) — that one entry goes through the normal propose/approve cycle once; the table's
*rows* after that don't. A genuinely contested call ("is this folder still live, or should it be
retired/merged into another") is a judgement call and gets escalated per
`feedback_iba_data_judgment_calls_must_escalate_not_silent_report` — the lighter maintenance model
means routine additions don't wait on a proposal, not that ambiguous ones go unflagged.

**Relationship to the ~26 existing `governance.*_dir`/`*.output_dir`/`*.report_path` settings
(#939–969): sits *alongside*, does not replace.** Those settings are precise, per-utility write
targets at report/file granularity (`report.cluster_path` → one exact file). `folder_purpose` is
coarser — one row per folder, covering *every* file that lands there regardless of which utility wrote
it. `owning_settings` is the lightweight link between the two layers, kept as descriptive text (not a
real FK) because a folder can host zero, one, or several settings' output and the mapping isn't
structurally 1:1.

**Granularity — grounded in a live census, not guessed:** [`outputs/folder-census-20260828.csv`](../../outputs/folder-census-20260828.csv)
is a fresh, full scan of every directory in the project tree (793 folders, same `manifest.skip_dirs`
exclusions as the real manifest scan), for the researcher to review before the row-granularity
question is answered. Per folder: `folder_path`, `depth`, `parent_path`, `direct_file_count`,
`recursive_file_count`, `direct_subfolder_count`, `top_ext_direct` (up to 5 extensions by count),
`last_modified_direct`, and `governed_by_setting` (which existing `cfg_setting` already names this
exact path, if any — 793 rows checked live against every `*_dir`/`*_path`/`*folder*` setting).
Shape, for scale: depth 0 = repo root (1), depth 1 = top-level roots (17), depth 2 = 82, depth 3 = 294,
depth 4 = 284, depth 5 = 112, depth 6 = 3. **This plan does not pre-decide how deep `folder_purpose`
rows should go** (every folder? top-level + one level down? only folders a `cfg_setting` already
names, plus a short explicit list like `docs/`?) — that's exactly what the census is for. Seed-row
scope in the build sequence below is written provisionally (existing settings' folders + `docs/` + a
short named list) and will be corrected to whatever depth the researcher settles on after reviewing
the CSV.

## Part D — wiring into the manifest routine, and fixing the manifest itself (both in scope)

**Current state, checked live:** `manifest.py`'s `classify_category()`/`compute_currency()` are
hardcoded Python prefix tables. Confirmed drift, live: the manifest's own `_CURRENCY_RULES`/
`classify_category()` have no entry for `_analytics/` at all — it didn't exist when the classifier was
written — so all `_analytics/*` files (6,577 files per the census above) fall through to
`category='other'`. **The manifest hasn't been rescanned since 2026-08-15** (one `scanned_at` value
across all 18,653 rows) — 13 days old, predates this week's entire reorg; 4,303 rows (23%) already sit
in the `other`/`other` catch-all today. **Fixing this — a rebuild that reflects the current tree — is
explicitly in this escalation's scope, not a deferred follow-on**, per the researcher's own
instruction this round.

**The mechanism (the researcher's item 3, made concrete):**

1. `manifest._scan()` looks up each file's folder against `folder_purpose` first (longest matching
   `folder_path` prefix wins), using its `manifest_category`/`manifest_currency` when found.
2. **Only when no `folder_purpose` row matches** does it fall back to the existing hardcoded
   `classify_category()`/`compute_currency()` logic — non-breaking: nothing reclassifies until a
   folder is actually registered, and the fallback keeps working for any folder not yet in scope.
3. `manifest.rebuild()` upserts a placeholder `folder_purpose` row (`purpose='(unclassified — needs
   review)'`, `active=1`) for any top-level folder it encounters with no existing match, **and** its
   summary/rebuild report gains a line listing exactly which folders those are — the drift-detection
   loop the researcher asked for.
4. A `configmaint.validate` check mirrors the same signal at the config layer (parallel to
   `find_unregistered_project_scripts`): any `folder_path` referenced in a `cfg_setting`
   `*_dir`/`*_path` value that has no corresponding `folder_purpose` row.

**Immediate, separate finding surfaced while grounding this plan (fixed in the same round, not a
design call — a bare compliance gap):** `file_manifest` itself — the live, 18,653-row table this whole
mechanism reads and writes — is **not currently registered in `cfg_table`/`cfg_column`** at all,
violating `governance.tables`/`governance.table_columns`. Registering it (15 columns) is mechanical,
done as part of Part D's build, ahead of anything else. (`folder_purpose` gets its own
`cfg_table`/`cfg_column` entry at the same time it's created, per Part C.)

**Manifest rebuild is a deliverable of this round, not a recommendation for later:** once Parts C/D
are wired in, `Manifest-Rebuild.ps1` runs as the last build step, producing the first fresh scan since
2026-08-15 — with `_analytics/` and every other post-2026-08-15 folder now classified, and any newly
discovered unclassified folder surfacing in the rebuild report, ready for a purpose to be filled in.

## Part E — the config gap this round's own filing surfaced (new)

**What happened:** this plan document itself was filed to `iba/docs/` (per
`governance.engineering_documentation_folder`, which explicitly lists "design docs, plans, gap
analyses" as its scope, and matches every prior escalation-tied plan in the project —
`file-naming-and-location-governance-plan-v1` (#863), `flag-management-proposal-v1` (#833),
`escalation-decision-vs-defect-axis-proposal-v5` (#798/#799), the `prose-*` plan sequence (#784), none
of which live in `outputs/escalation/`). The researcher's recollection was that "all escalation files,
including associated reports" were already ruled to belong in `outputs/escalation/`. **Checked live:
that's not what's actually configured.** `GOVERNANCE.md` §59 (2026-08-27, escalations #929/#736/#934/
#935) repointed exactly two `cfg_setting` rows — `escalation.list_report_path` and
`escalation.history_report_dir` — both scoped narrowly to the two reports `Escalation.ps1` itself
auto-generates (`-Action List`/`-Action History`). No rule anywhere currently states where a
*deliverable document* referenced from an escalation's comment/resolution should live. §59's own text
even flags this as unresolved: *"the `cfg_folder_purpose` table... is also not built here — a second,
larger design item."* Two real rules exist, pointed in different directions for this one case, and
nothing arbitrates between them.

**Proposed resolution (Part A item 5 above, the actual rule text):** a tool's own auto-generated
report output (escalation list/history, `CONFIG-REPORT.md`, a validation run's report, a content-index
rebuild report — every existing `*.report_path`/`*.output_dir` setting) stays exactly where its
setting already points. An authored deliverable — a plan, a design doc, a gap analysis, an
investigation write-up, even one written *while working* a specific escalation and linked from its
comment — follows `governance.engineering_documentation_folder` (`iba/docs/` for IBA-side work) or the
main-project equivalent, never the tool's own report folder. This is one general rule, not a
per-module special case — the same ambiguity could recur for `configmaint.report_path`,
`content_index.report_path`, `validation.output_dir`, etc., and this closes it for all of them at
once rather than one at a time as each is separately noticed.

**Where this lives:** a `folder_purpose` row for `outputs/escalation` (and each other tool-report
folder) states this explicitly in its `purpose` text — e.g. *"Escalation.ps1's own auto-generated
list/history exports only — NOT a destination for escalation-linked deliverable documents, which
follow governance.engineering_documentation_folder instead"* — so the distinction is discoverable by
reading the registry, not only by reading this plan.

## Build sequence (proposed)

1. Register `file_manifest` in `cfg_table`/`cfg_column` (config change — one-time table registration,
   goes through the normal propose/approve cycle, same as #968/#969 did for the two folder-naming
   settings).
2. Part A — `filing` behaviour class + rules (items 1–5, including the new item 5 from Part E) +
   `filingkit.versioned_path()` + naming-drift `configmaint.validate` check (config change, same
   cycle).
3. Create `folder_purpose` (schema + its own one-time `cfg_table`/`cfg_column` registration — config
   change) and `folderpurpose.py` + its PS front door (code, no per-row approval needed).
4. Seed `folder_purpose` rows directly via the new utility — scope and depth set by the researcher's
   review of `outputs/folder-census-20260828.csv` (Part C); provisionally: existing `*_dir`/`*_path`
   folders (each carrying the Part E distinction text where relevant), `docs/`, IBA's own, the
   still-live main-project folders named in Part C.
5. Wire `manifest.py` to read `folder_purpose` first / fallback second, add the rebuild-report drift
   line + auto-placeholder-row behaviour, add the `configmaint.validate` folder-coverage check.
6. Rebuild the manifest (`Manifest-Rebuild.ps1`) — the first fresh scan since 2026-08-15. Verify
   `_analytics/` and the other post-reorg folders now classify correctly and the `other` bucket
   shrinks; review whatever the drift line surfaces.
7. `BUILD.md`/`GOVERNANCE.md`/`USER-GUIDE.md` updated in the same unit of work.

**Not proposed:** a bulk audit/retrofit of every folder in the tree against the new table (v1 §3's
deferred item, unchanged), and no change to `docs/file-organisation-rules.md`'s methodology-specific
§2.2/§3 content (v1's own scope boundary, unchanged).

## Open questions for the researcher

1. **Row granularity (Part C)** — after reviewing `outputs/folder-census-20260828.csv`: how deep
   should `folder_purpose` go? (Every one of the 793 folders? Top-level + one level down only? Only
   folders a `cfg_setting` already names, plus `docs/` and a short explicit list?)
2. **Integration strength (Part D)** — cfg-first-with-code-fallback as described, or a stronger form
   (fully retire the hardcoded prefix tables once seed rows cover them)?
3. **Build sequence** — the 7 steps above as one round, or split (e.g. steps 1–2 shipped separately
   from steps 3–6)?
4. **Part E's rule text** — does the proposed distinction (tool-report-path vs.
   engineering-documentation-folder) match what was actually meant by "repointing escalation files,"
   or was the intent genuinely broader (every escalation-linked file, deliverables included, into
   `outputs/escalation/`)? If the latter, Part A item 5 and every prior escalation-tied plan doc
   (including this one) would need to move — flagging before building either way, not assuming.

Approve scope (and answer 1–4 above), and this builds next round — design → propose → build → verify,
same cycle as every other IBA module.
