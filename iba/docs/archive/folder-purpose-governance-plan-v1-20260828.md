# Folder-purpose governance mechanism — plan (v1)

> Escalation #971 (consolidates #929 v8 / #736 v7 carryover, researcher's own instruction to combine
> into one item). This is **a plan for the researcher's decision, not a build** — nothing here is
> implemented yet, per `governance.project_change_rule` / `governance.config_control` (design work is
> `decision_required`, routed through `Config-Maintenance.ps1 -Step Propose`, never built silently).
> Scope steer this round (researcher, 2026-08-28 chat): *"ensure that the folder [purpose] table
> processing integrates with manifest routine"* — folded into Part D below, which is the genuinely
> new design work; Parts A–C mostly settle #971's carried-forward open questions against material
> already drafted.

## 0. What #971 consolidated

1. `docs/` — 36 flat files at the project root, no subfolders/archive/naming convention. Main-project
   side, not IBA. The folder census's own 14th pattern, never addressed.
2. #736's own unbuilt gap: a project-wide `filing` `cfg_behaviour_class` + `cfg_behaviour_rule` rows +
   a shared utility generalising `oneoff_path()` + a `configmaint.validate` naming-drift check — fully
   spec'd already in [`file-naming-and-location-governance-plan-v1-20260826.md`](file-naming-and-location-governance-plan-v1-20260826.md)
   §2–§3 (escalation #863), approved in scope but never built.
3. The researcher's own framing this round: a mechanism — "likely a `cfg_folder_purpose` table naming
   every live project folder's intended purpose, paired with a utility that maps files against it... so
   we can maintain better overall control of folders." This is the location-governance table v1's §3
   explicitly deferred as a second-phase decision, pending confirmation of which folders are actually
   still live — which this week's #929 reorg has now done for the two trees it touched
   (`_analytics/word_registry`, `_analytics/Bible_Books`).

## Part A — adopt v1's filing mechanism (items 2 above), as already scoped

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

**Recommendation: build this now, unchanged from v1.** It was already approved in scope; the only
reason it wasn't built was sequencing (v1 stopped at "approve scope, I'll build §2 next round").

## Part B — is `docs/` in scope?

**Recommendation: yes.** It's item 1 above, named explicitly in #971's own raise, and it's the same
kind of gap Part A's mechanism is built to close (a live project folder with files in it and no
naming/archiving discipline). Once Part A's `filing` rules exist and Part C's `cfg_folder_purpose`
table exists, `docs/` gets one row in each like any other governed folder — it does not need its own
special-cased mechanism. No separate content-taxonomy decision needed unless the researcher wants one
(e.g. reorganising `docs/` into subfolders by topic) — that would be a physical-reorg pass, same
category as the #929 sweep, layered on top of this governance mechanism rather than blocking it.

## Part C — `cfg_folder_purpose` table design

New table, one row per **governed folder** (a directory prefix the project treats as a distinct,
named location — not every physical subdirectory):

| column | type | purpose |
|---|---|---|
| `folder_path` | TEXT, PK | Project-root-relative prefix, POSIX slashes, no trailing slash (`iba/docs`, `_analytics/word_registry`, `outputs/configs`) |
| `purpose` | TEXT | One-line statement of what belongs here (mirrors `cfg_table.use`/`cfg_column.use` phrasing) |
| `manifest_category` | TEXT | The `file_manifest.category` value this folder should classify as (Part D) |
| `manifest_currency` | TEXT | The `file_manifest.currency` value this folder should classify as |
| `owning_settings` | TEXT, nullable | Free-text list of the `cfg_setting` keys that already point utility output here (e.g. `report.cluster_path, report.strong_verse_output_dir`) — a cross-reference for a human reading the table, not an enforced FK (see below) |
| `active` | INTEGER | 0 once a folder is retired/superseded — never deleted, matching `governance.tables`' "inactive, not removed" convention |

**Relationship to the ~26 existing `governance.*_dir`/`*.output_dir`/`*.report_path` settings
(#939–969): sits *alongside*, does not replace.** Those settings are precise, per-utility write
targets at report/file granularity (`report.cluster_path` → one exact file). `cfg_folder_purpose` is
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

## Part D — integration with the manifest routine (this round's new steer)

**Current state, checked live:** `manifest.py`'s `classify_category()`/`compute_currency()` are
hardcoded Python prefix tables (deliberately kept as code "facts," not `cfg_setting`, per the module's
own docstring — a defensible line when written, but superseded by the researcher's principle stated
this same session in `GOVERNANCE.md`: *"folder locations and naming conventions must live in `cfg_*`
configuration, not only in an instruction or guidance document."*). Confirmed drift from that
hardcoding, live: the manifest's own `_CURRENCY_RULES`/`classify_category()` have no entry for
`_analytics/` at all — it didn't exist when the classifier was written — so all `_analytics/*` files
(the very trees #929 just reorganised) fall through to `category='other'`. **The manifest hasn't been
rescanned since 2026-08-15** (one `scanned_at` value across all 18,653 rows) — 13 days old, predating
this week's entire reorg; 4,303 rows (23%) already sit in the `other`/`other` catch-all today.

**Proposed integration** (this is the actual design decision — flagging it explicitly rather than
picking silently):

1. `manifest._scan()` looks up each file's folder against `cfg_folder_purpose` first (longest
   matching `folder_path` prefix wins), using its `manifest_category`/`manifest_currency` when found.
2. **Only when no `cfg_folder_purpose` row matches** does it fall back to the existing hardcoded
   `classify_category()`/`compute_currency()` logic — non-breaking: nothing reclassifies until a
   folder is actually registered, and the fallback keeps working for any folder not yet in scope.
3. `manifest.rebuild()`'s summary (and rebuild report) gains one more line: count of files that hit
   the fallback path grouped by their top-level folder — i.e. **which live folders still have no
   `cfg_folder_purpose` row**. This is the drift-detection loop the researcher asked for: the manifest
   rebuild itself becomes the mechanism that surfaces "here's a folder nobody has classified yet,"
   rather than that going undetected until someone happens to notice (as `_analytics/` did here).
4. A `configmaint.validate` check mirrors the same signal at the config layer (parallel to
   `find_unregistered_project_scripts`): any `folder_path` referenced in a `cfg_setting`
   `*_dir`/`*_path` value that has no corresponding `cfg_folder_purpose` row.

**Immediate, separate finding surfaced while grounding this plan (fixed in the same round, not a
design call — a bare compliance gap):** `file_manifest` itself — the live, 18,653-row table this whole
mechanism reads and writes — is **not currently registered in `cfg_table`/`cfg_column`** at all,
violating `governance.tables`/`governance.table_columns`. Registering it (15 columns) is mechanical,
not a design decision; done as part of Part D's build, ahead of anything else, so the table this plan
extends is itself compliant first.

**Also recommended, once Parts C/D land:** rebuild the manifest (`Manifest-Rebuild.ps1`) so the first
fresh scan since 2026-08-15 already reflects governed folders (`_analytics/` included) rather than
needing a second rebuild immediately after.

## Build sequence (proposed)

1. Register `file_manifest` in `cfg_table`/`cfg_column` (compliance fix, no approval needed —
   `governance.config_control` treats a missing-registration fix as mechanical, matching how #973/#974
   were self-caught and applied this same session).
2. Part A — `filing` behaviour class + rules + `filingkit.versioned_path()` + naming-drift
   `configmaint.validate` check (already-approved scope, v1 §2).
3. Part C — `cfg_folder_purpose` table + seed rows (existing `*_dir`/`*_path` folders, `docs/`, IBA's
   own, the still-live main-project folders named above).
4. Part D — wire `manifest.py` to read `cfg_folder_purpose` first / fallback second, rebuild-report
   drift line, `configmaint.validate` folder-coverage check.
5. Rebuild the manifest; verify `_analytics/` and the other post-2026-08-15 folders now classify
   correctly and the `other` bucket shrinks.
6. `BUILD.md`/`GOVERNANCE.md`/`USER-GUIDE.md` updated in the same unit of work (governance requires
   this for any code or rule change — not deferred).

**Not proposed:** a bulk audit/retrofit of every folder in the tree against the new table (v1 §3's
deferred item, unchanged — seed rows cover the folders already named by settings or this plan, not an
exhaustive sweep), and no change to `docs/file-organisation-rules.md`'s methodology-specific §2.2/§3
content (v1's own scope boundary, unchanged).

## Open questions for the researcher

1. **Table shape (Part C)** — does the `cfg_folder_purpose` column set above look right, or is
   more/less wanted (e.g. an explicit owning-utility FK instead of free-text `owning_settings`)?
2. **Integration approach (Part D)** — cfg-first-with-code-fallback as described, or a stronger form
   (fully retire the hardcoded prefix tables once seed rows cover them)? The fallback approach is
   recommended as the lower-risk migration path — nothing currently working stops working.
3. **Build sequence** — the 6 steps above as one round, or split (e.g. Part A shipped separately from
   Parts C/D, since Part A was already approved scope and Parts C/D are the newly-designed piece)?

Approve scope (and answer 1–3 above), and this builds next round — design → propose → build → verify,
same cycle as every other IBA module.
