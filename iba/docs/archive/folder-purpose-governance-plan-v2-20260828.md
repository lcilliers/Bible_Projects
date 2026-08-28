# Folder-purpose governance mechanism — plan (v2)

> Escalation #971 (consolidates #929 v8 / #736 v7 carryover, researcher's own instruction to combine
> into one item). This is **a plan for the researcher's decision, not a build** — nothing here is
> implemented yet. **Supersedes v1 (2026-08-28) in full** — v1's own "config table" framing for the
> new folder-purpose mechanism was wrong; corrected in Part C below per researcher feedback. Full
> proposal, not a delta — this document stands alone.

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
   manifest-integration work; it was never a separate add-on to bolt on afterward. This plan's Part C
   designs the registry table, Part D wires it into the manifest routine that already exists to
   consume it — one mechanism, not two.

## Part A — adopt v1's filing mechanism (item 2 above), as already scoped

No new design needed here — v1 §2 already specifies this cleanly:

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

This part genuinely is config-governed: it's a set of *rules* about how naming/archiving must behave
project-wide, which is exactly what `cfg_behaviour_class`/`cfg_behaviour_rule` exist for, and belongs
in the normal propose → validate → escalate → apply cycle like any other rule change.

**Recommendation: build this now, unchanged from v1.** It was already approved in scope; the only
reason it wasn't built was sequencing (v1 stopped at "approve scope, I'll build §2 next round").

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
point of the correction, so the name itself doesn't misclassify it going forward). Lives in `iba.db`
alongside `file_manifest`, one row per governed folder:

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
`governance.tables`) — that one entry goes through the normal propose/approve cycle once, same as
registering any other table; the table's *rows* after that don't. If a genuinely ambiguous or
contested folder-purpose call comes up (not "here's a new folder, here's its obvious purpose" but "is
this folder still live or should it be retired/merged"), that's a judgement call and gets escalated
per `feedback_iba_data_judgment_calls_must_escalate_not_silent_report` — the lighter maintenance model
doesn't mean silent, it means routine additions don't need to wait on a formal proposal.

**Relationship to the ~26 existing `governance.*_dir`/`*.output_dir`/`*.report_path` settings
(#939–969): sits *alongside*, does not replace.** Those settings are precise, per-utility write
targets at report/file granularity (`report.cluster_path` → one exact file). `folder_purpose` is
coarser — one row per folder, covering *every* file that lands there regardless of which utility wrote
it, including files no `cfg_setting` currently points at (hand-filed research notes, session logs,
git-tracked docs). Merging them would force one-row-per-file granularity onto folders that hold many
unrelated file types, or lose the exact per-utility path the existing settings already give correctly.
`owning_settings` is the lightweight link between the two layers, kept as descriptive text (not a real
FK) because a folder can host zero, one, or several settings' output and the mapping isn't
structurally 1:1.

**Coverage scope for the seed data:** every folder currently named in a `governance.*` or `report.*`
etc. `cfg_setting` value (the ~26 from #939–969), plus `docs/` (Part B), plus IBA's own
(`iba/app`, `iba/docs`, `iba/config`), plus the handful of main-project folders v1 §4 already named as
still-live-but-unrepresented (`Sessions-v2/`, `research/investigations/`, `Workflow/methodology/`,
`Logs/`, `archive/`). **Not** a folder-by-folder audit of the entire tree in this round — that's the
bulk-cleanup item v1 §3 already deferred, unchanged here.

## Part D — wiring into the manifest routine, and fixing the manifest itself (both in scope)

**Current state, checked live:** `manifest.py`'s `classify_category()`/`compute_currency()` are
hardcoded Python prefix tables. Confirmed drift, live: the manifest's own `_CURRENCY_RULES`/
`classify_category()` have no entry for `_analytics/` at all — it didn't exist when the classifier was
written — so all `_analytics/*` files (the very trees #929 just reorganised) fall through to
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
   summary/rebuild report gains a line listing exactly which folders those are. This is the
   drift-detection loop the researcher asked for: the manifest rebuild itself becomes the mechanism
   that surfaces "here's a folder nobody has classified yet" (as `_analytics/` did here), rather than
   that going unnoticed until someone happens to look.
4. A `configmaint.validate` check mirrors the same signal at the config layer (parallel to
   `find_unregistered_project_scripts`): any `folder_path` referenced in a `cfg_setting`
   `*_dir`/`*_path` value that has no corresponding `folder_purpose` row.

**Immediate, separate finding surfaced while grounding this plan (fixed in the same round, not a
design call — a bare compliance gap):** `file_manifest` itself — the live, 18,653-row table this whole
mechanism reads and writes — is **not currently registered in `cfg_table`/`cfg_column`** at all,
violating `governance.tables`/`governance.table_columns`. Registering it (15 columns) is mechanical,
not a design decision; done as part of Part D's build, ahead of anything else, so the table this plan
extends is itself compliant first. (`folder_purpose` gets its own `cfg_table`/`cfg_column` entry at
the same time it's created, per Part C.)

**Manifest rebuild is a deliverable of this round, not a recommendation for later:** once Parts C/D
are wired in, `Manifest-Rebuild.ps1` runs as the last build step, producing the first fresh scan since
2026-08-15 — with `_analytics/` and every other post-2026-08-15 folder now classified, and any newly
discovered unclassified folder surfacing in the rebuild report per point 3 above, ready for a purpose
to be filled in rather than left silently in `other`.

## Build sequence (proposed)

1. Register `file_manifest` in `cfg_table`/`cfg_column` (config change — one-time table registration,
   goes through the normal propose/approve cycle, same as #968/#969 did for the two folder-naming
   settings).
2. Part A — `filing` behaviour class + rules + `filingkit.versioned_path()` + naming-drift
   `configmaint.validate` check (already-approved scope, v1 §2; also a config change, same cycle).
3. Create `folder_purpose` (schema + its own one-time `cfg_table`/`cfg_column` registration — config
   change) and `folderpurpose.py` + its PS front door (code, no per-row approval needed).
4. Seed `folder_purpose` rows directly via the new utility — existing `*_dir`/`*_path` folders,
   `docs/`, IBA's own, the still-live main-project folders named in Part C — ordinary data writes, not
   config proposals.
5. Wire `manifest.py` to read `folder_purpose` first / fallback second, add the rebuild-report drift
   line + auto-placeholder-row behaviour, add the `configmaint.validate` folder-coverage check.
6. Rebuild the manifest (`Manifest-Rebuild.ps1`) — the first fresh scan since 2026-08-15. Verify
   `_analytics/` and the other post-reorg folders now classify correctly and the `other` bucket
   shrinks; review whatever the drift line surfaces.
7. `BUILD.md`/`GOVERNANCE.md`/`USER-GUIDE.md` updated in the same unit of work (governance requires
   this for any code or rule change — not deferred).

**Not proposed:** a bulk audit/retrofit of every folder in the tree against the new table (v1 §3's
deferred item, unchanged — seed rows cover the folders already named by settings or this plan, not an
exhaustive sweep), and no change to `docs/file-organisation-rules.md`'s methodology-specific §2.2/§3
content (v1's own scope boundary, unchanged).

## Open questions for the researcher

1. **Table shape (Part C)** — does the `folder_purpose` column set above look right, or is more/less
   wanted (e.g. an explicit owning-utility FK instead of free-text `owning_settings`)?
2. **Integration strength (Part D)** — cfg-first-with-code-fallback as described, or a stronger form
   (fully retire the hardcoded prefix tables once seed rows cover them)? The fallback approach is
   recommended as the lower-risk migration path — nothing currently working stops working.
3. **Build sequence** — the 7 steps above as one round, or split (e.g. steps 1–2 shipped separately
   from steps 3–6, since Part A was already approved scope and Parts C/D are the newly-designed
   piece)?

Approve scope (and answer 1–3 above), and this builds next round — design → propose → build → verify,
same cycle as every other IBA module.
