# Folder-purpose governance mechanism — plan (v4)

> Escalation #971 (consolidates #929 v8 / #736 v7 carryover, researcher's own instruction to combine
> into one item). This is **a plan for the researcher's decision, not a build** — nothing here is
> implemented yet. **Supersedes v3 (2026-08-28) in full** — Part C is redesigned per researcher
> instruction: full coverage (all 793 census folders get a row, not a curated subset), the complete
> census column set carried in verbatim, three new researcher-facing columns
> (`type`/`status`/`usage_description`), and three named processing methods (manifest / configmaint /
> table-editor) replacing the earlier vaguer "maintenance model" paragraph. Full proposal, not a
> delta — this document stands alone.

## 0. What #971 consolidated

1. `docs/` — 36 flat files at the project root, no subfolders/archive/naming convention. Main-project
   side, not IBA. The folder census's own 14th pattern, never addressed.
2. #736's own unbuilt gap: a project-wide `filing` `cfg_behaviour_class` + `cfg_behaviour_rule` rows +
   a shared utility generalising `oneoff_path()` + a `configmaint.validate` naming-drift check — fully
   spec'd already in [`file-naming-and-location-governance-plan-v1-20260826.md`](file-naming-and-location-governance-plan-v1-20260826.md)
   §2–§3 (escalation #863), approved in scope but never built.
3. The researcher's own framing this round: a mechanism — "likely a `cfg_folder_purpose` table naming
   every live project folder's intended purpose, **paired with a utility that maps files against
   it**... so we can maintain better overall control of folders." That utility already exists:
   `manifest.py`/`file_manifest` walks the whole tree and classifies every file by folder today, just
   off hardcoded rules instead of a governed table — item 3 IS the manifest-integration work.
4. A real, unresolved config gap the researcher caught while this plan itself was being filed: no
   rule distinguishes a tool's own auto-generated report output from an authored deliverable document
   referenced from an escalation. Folded into Part E, generalised beyond escalations alone.
5. **Added this round:** the folder-purpose table (Part C) needs a properly designed column set and,
   just as important, **named methods that actually keep it current** — a table that's accurate once
   and drifts forever after is no better than the manifest's own 13-day-stale scan. Two-part purpose,
   stated directly by the researcher: *"partly to give me visibility what is going on, and partly to
   allow you to make the right filing decisions."*

## Part A — adopt v1's filing mechanism (item 2), plus the Part E rule (item 4)

No new design needed for the original four — v1 §2 already specifies them cleanly:

1. New `cfg_behaviour_class` row `filing` (naming shape, snapshot-vs-living distinction, archiving
   triggers, the five Claude Code filing obligations — general principles only, not the
   methodology-specific `docs/file-organisation-rules.md` §2.2/§3 patterns, which stay legacy prose).
2. `cfg_behaviour_rule` rows under `filing`, one per principle.
3. `filingkit.versioned_path()` — generalises `reportkit.oneoff_path()`'s same-day `-v{n}` bump /
   archive-before-write / collision handling for **any** caller project-wide, not just
   `iba/app/reports/`.
4. `configmaint.validate` check: flag writes that hand-imitate the naming pattern instead of calling
   the shared utility (advisory, doesn't block).
5. **New (Part E):** a `cfg_behaviour_rule` stating that a tool's own auto-generated report output
   stays at its own `*_report_path`/`*_dir` setting, while an authored deliverable — even one linked
   from an escalation — follows `governance.engineering_documentation_folder` instead. One general
   rule covering every `*.report_path` setting, not escalation alone (Part E has the full detail and
   the still-open question about whether this matches the researcher's original intent).

**Recommendation: build all five now** — items 1–4 already approved in scope, item 5 new but same
class, same build.

## Part B — is `docs/` in scope?

**Recommendation: yes.** It's item 1 above, named explicitly in #971's own raise, and it's the same
kind of gap Part A's mechanism is built to close. Once Part A's `filing` rules exist and Part C's
folder registry exists, `docs/` gets one row in each like any other governed folder — it does not need
its own special-cased mechanism. No separate content-taxonomy decision needed unless the researcher
wants one (e.g. reorganising `docs/` into subfolders by topic) — that would be a physical-reorg pass,
layered on top of this governance mechanism rather than blocking it.

## Part C — `folder_purpose`: full column design + the three methods that keep it current

**Coverage, settled this round: every folder in the census, not a curated subset.** All 793 rows from
[`outputs/folder-census-20260828.csv`](../../outputs/folder-census-20260828.csv) become `folder_purpose`
rows. This answers v3's open question 1 directly — the table's whole point, per the researcher, is
*"to give me visibility what is going on"*, which a partial table can't do.

**Category, unchanged from v3's correction:** a reference/data table, not `cfg_*` — same template as
`books` (`bible_research.db`): registered once in `cfg_table`/`cfg_column` (governance.tables applies
to every table), but its *rows* are maintained directly by the three methods below, not through
`configmaint.propose` per change.

### Column design

**Every column from the census, carried in verbatim** (same names, same meaning — the census output
*is* the seed data for these columns, not a separate thing to reconcile against):

| column | type | source | purpose |
|---|---|---|---|
| `folder_path` | TEXT, PK | census | Project-root-relative prefix, POSIX slashes, no trailing slash |
| `top_level_root` | TEXT | census | First path segment — cheap grouping/filter key |
| `depth` | INTEGER | census | Path segment count (0 = repo root) |
| `parent_path` | TEXT | census | Immediate parent folder's `folder_path` |
| `direct_file_count` | INTEGER | census, refreshed by Method A | Files directly in this folder (not subfolders) |
| `recursive_file_count` | INTEGER | census, refreshed by Method A | Files in this folder and everything under it |
| `direct_subfolder_count` | INTEGER | census, refreshed by Method A | Immediate child folders |
| `top_ext_direct` | TEXT | census, refreshed by Method A | Up to 5 extensions by count, direct files only |
| `last_modified_direct` | TEXT | census, refreshed by Method A | Latest mtime among direct files |
| `governed_by_setting` | TEXT | census, refreshed by Method B | Which `cfg_setting` key(s) already point at this exact path |

**New columns, this round:**

| column | type | values | purpose |
|---|---|---|---|
| `manifest_category` | TEXT, nullable | `file_manifest.category`'s existing 17-value set (`iba`, `session`, `script`, `cluster`, `discovery`, `workflow`, `investigation`, `patch`, `report`, `doc`, `log`, `directive`, `code`, `export`, `import`, `backup`, `other`) | What `file_manifest.category` a file in this folder should get — feeds Part D's manifest lookup. Kept as its own column, separate from `type` below, because the manifest's existing category taxonomy is 17 values wide and can't be represented by a 3-value field without losing information consumers of `file_manifest` already depend on. |
| `manifest_currency` | TEXT, nullable | `file_manifest.currency`'s existing 6-value set (`current`, `archived`, `cross-reference`, `historical`, `backup`, `other`) | Same reasoning, for `file_manifest.currency` |
| `type` | TEXT | `archive` \| `operations` \| `results` | The researcher-facing coarse classification: is this folder for archived material, active operational/working files, or output/results? Registered in `cfg_enum` (name `folder_purpose_type`) per `governance.project_lookups_and_naming_convensions` |
| `status` | TEXT | `authoritative` \| `mixed` \| `reallocate` \| `stale` \| `deleted` | The folder's audit/health status — `authoritative` = single clean source of truth for its purpose; `mixed` = holds a jumble of content that needs sorting; `reallocate` = should move somewhere else; `stale` = old, not actively maintained, not yet formally archived; `deleted` = folder no longer exists on disk (Method A sets this — replaces a separate `active` flag entirely, so there's one status field, not two overlapping ones). Registered in `cfg_enum` (name `folder_purpose_status`) |
| `usage_description` | TEXT, nullable | free text | What this folder is actually for, in the researcher's or Claude's own words — the human-authored content `cfg_table.use`/`cfg_column.use` model, scoped to a folder instead of a table |
| `added_at` | TEXT | ISO timestamp | When the row was first created |
| `last_reviewed_at` | TEXT, nullable | ISO timestamp | When `type`/`status`/`usage_description` were last confirmed accurate by a human or the table-editor utility — lets Method A/B flag a row whose judgement fields haven't been looked at since the folder's disk-derived facts changed materially |

**The governing invariant, stated directly by the researcher: "no folder is used by the system, without
a `governed_by_setting`."** Concretely: any row with `type='operations'` (the system actively
reads/writes there) is expected to carry a non-empty `governed_by_setting`. A row with `type='operations'`
and an empty `governed_by_setting` is an anomaly — either something writes there that isn't declared in
any `cfg_setting` (a `governance.rules_must_be_config_driven` violation, needs a setting added), or the
folder isn't really system-operational and `type` is wrong. This is Method B's core check, not just a
guideline in prose.

### The three methods

**a) Manifest validate** — a new step in the manifest routine (`Manifest-Rebuild.ps1 -Step
ValidateFolders`, or folded into the existing rebuild as its last stage — build-time decision, not a
design one), run every time the manifest is rebuilt:
1. **New folders** — any directory the fresh scan finds with no matching `folder_purpose` row gets one
   inserted: all the disk-derived columns computed immediately (`direct_file_count` through
   `governed_by_setting`'s placeholder), `type`/`status`/`usage_description` left blank/`'(new — needs
   review)'`. Surfaced in the rebuild report as "N new folders discovered."
2. **Deleted folders** — any `folder_purpose` row whose `folder_path` no longer exists on disk gets
   `status='deleted'` (never physically removed — matches the project's soft-delete convention
   everywhere else). Surfaced as "N folders no longer present."
3. **Refresh** — every existing row's disk-derived columns (`direct_file_count`,
   `recursive_file_count`, `direct_subfolder_count`, `top_ext_direct`, `last_modified_direct`) are
   updated from the current scan; the researcher-authored columns (`type`, `status`,
   `usage_description`) are never touched by this step.
4. **Exceptions** — folders whose disk-derived facts look inconsistent with their researcher-set
   classification (e.g. `type='archive'` but `recursive_file_count` grew significantly since
   `last_reviewed_at`, suggesting active use) are listed in the rebuild report as "for review," not
   auto-corrected.

**b) Configmaint cross-check** — a new `configmaint.validate` check, run on the existing
`configmaint.validate` cadence:
1. Re-derives `governed_by_setting` for every row from the current `cfg_setting` table (config-side
   truth, distinct from Method A's disk-side truth) — a folder's governing setting can change without
   any file on disk moving, so this can't be Method A's job.
2. **Enforces the invariant above**: any `type='operations'` row with an empty `governed_by_setting`
   is flagged. Also flags the inverse (already planned in Part D): any `cfg_setting` `*_dir`/`*_path`
   value with no matching `folder_purpose` row at all.
3. Anomalies report through the existing `configmaint.validate` mechanism — advisory findings that
   become an escalation for review, same pattern #972 just went through.

**c) Table editor (PS)** — a new `FolderPurpose.ps1` front door, the *only* sanctioned way to change
`type`, `status`, or `usage_description` by hand (`-Action Set -FolderPath ... -Type ... -Status ...
-UsageDescription "..."`, `-Action List [-Type ...] [-Status ...]`, `-Action Show -FolderPath ...`).
Deliberately narrow — it cannot touch the disk-derived or config-derived columns (Methods A/B own
those and would overwrite a hand edit on the next run anyway); setting any of the three judgement
columns updates `last_reviewed_at` automatically. No `configmaint.propose` gate, matching the `books`
maintenance model — this is what makes "visibility + the right filing decisions" actually usable
day-to-day rather than requiring a formal proposal to record "this folder is `stale`."

**Relationship to the ~26 existing `governance.*_dir`/`*.output_dir`/`*.report_path` settings
(#939–969): sits *alongside*, does not replace.** Those are precise, per-utility write targets at
report/file granularity; `folder_purpose` is coarser, one row per folder. `governed_by_setting` is the
live, machine-maintained (Method B) link between the two layers — no longer a hand-typed cross-
reference as v2/v3 had it, an improvement this redesign makes possible.

## Part D — manifest integration (folded into Part C's methods above)

**Current state, checked live:** `manifest.py`'s `classify_category()`/`compute_currency()` are
hardcoded Python prefix tables. Confirmed drift, live: no entry for `_analytics/` at all (6,577 files,
per the census) — falls through to `category='other'`. **The manifest hasn't been rescanned since
2026-08-15** (13 days, predates this week's entire reorg); 4,303 rows (23%) already sit in `other`.
**Fixing this is explicitly in scope, not a deferred follow-on.**

**The two-way flow (item 3's manifest-integration, made concrete, now split cleanly across Part C's
methods rather than described separately):**

1. `manifest._scan()` looks up each file's folder against `folder_purpose.manifest_category`/
   `manifest_currency` first (longest matching `folder_path` prefix wins); falls back to the existing
   hardcoded `classify_category()`/`compute_currency()` only when no row matches — non-breaking.
2. Method A (above) is what keeps `folder_purpose` itself in sync with the disk, driven by the same
   scan `manifest._scan()` already performs — one walk of the tree, two tables updated from it.
3. Method B (above) is what keeps `governed_by_setting` in sync with `cfg_setting`, and enforces the
   operations-needs-a-setting invariant.

**Immediate, separate finding (fixed in the same round, mechanical, not a design call):**
`file_manifest` itself — 18,653 live rows — is **not currently registered in `cfg_table`/`cfg_column`**
at all, violating `governance.tables`/`governance.table_columns`. Registered as part of this build,
ahead of anything else. (`folder_purpose` gets its own `cfg_table`/`cfg_column` entry when created.)

**Manifest rebuild is a deliverable of this round:** `Manifest-Rebuild.ps1` runs as the last build
step — the first fresh scan since 2026-08-15, with `_analytics/` and every other post-reorg folder
correctly classified, and Method A's new/deleted-folder reconciliation exercised for real against all
793 current folders.

## Part E — the config gap this round's own filing surfaced

**What happened:** this plan document was filed to `iba/docs/` (per
`governance.engineering_documentation_folder`, matching every prior escalation-tied plan —
`file-naming-and-location-governance-plan-v1` (#863), `flag-management-proposal-v1` (#833),
`escalation-decision-vs-defect-axis-proposal-v5` (#798/#799), the `prose-*` sequence (#784), none in
`outputs/escalation/`). The researcher's recollection was that "all escalation files, including
associated reports" already belonged in `outputs/escalation/`. **Checked live: not what's actually
configured.** `GOVERNANCE.md` §59 (2026-08-27) repointed exactly two settings —
`escalation.list_report_path`/`escalation.history_report_dir` — scoped to `Escalation.ps1`'s own
auto-generated reports only. No rule states where a linked deliverable document should live. §59's own
text flags this as unresolved: *"the `cfg_folder_purpose` table... is also not built here — a second,
larger design item."*

**Proposed resolution (Part A item 5):** a tool's auto-generated report output stays at its own
`*_report_path`/`*_dir` setting; an authored deliverable — even one linked from an escalation — follows
`governance.engineering_documentation_folder`, never the tool's report folder. One general rule, not a
per-module special case.

**Where this lives:** the `folder_purpose` row for `outputs/escalation` carries this in
`usage_description` — e.g. *"Escalation.ps1's own auto-generated list/history exports only — NOT a
destination for escalation-linked deliverable documents, which follow
governance.engineering_documentation_folder instead"* — `type='operations'`, `status='authoritative'`
— discoverable by reading the registry, not only this plan.

## Build sequence (proposed)

1. Register `file_manifest` in `cfg_table`/`cfg_column` (config change, normal propose/approve cycle).
2. Part A — `filing` behaviour class + rules (items 1–5) + `filingkit.versioned_path()` + naming-drift
   `configmaint.validate` check (config change, same cycle).
3. Register `folder_purpose_type`/`folder_purpose_status` in `cfg_enum`, and `folder_purpose` itself in
   `cfg_table`/`cfg_column` (config change, same cycle).
4. Build `folder_purpose` schema + `folderpurpose.py` + `FolderPurpose.ps1` (Method C) — code, no
   per-row approval.
5. Seed all 793 rows from the census — disk-derived columns populated directly; `type`/`status`/
   `usage_description` left for the researcher/Claude to fill in via Method C afterward, starting with
   the ~26 already-`cfg_setting`-governed folders (fastest to classify — `governed_by_setting` already
   tells us `type='operations'`) and `outputs/escalation` (Part E's example row).
6. Build Method A (manifest validate step) and Method B (configmaint cross-check) — code.
7. Wire `manifest.py`'s classification lookup to `folder_purpose` (Part D point 1) — code.
8. Rebuild the manifest (`Manifest-Rebuild.ps1`) — first fresh scan since 2026-08-15; verify
   `_analytics/` and other post-reorg folders classify correctly, Method A's reconciliation runs
   clean against all 793 rows.
9. `BUILD.md`/`GOVERNANCE.md`/`USER-GUIDE.md` updated in the same unit of work.

**Not proposed:** hand-classifying (`type`/`status`/`usage_description`) all 793 rows as part of this
build — that's ongoing use of Method C after the mechanism ships, not a one-time bulk task blocking
delivery. No change to `docs/file-organisation-rules.md`'s methodology-specific §2.2/§3 content.

## Open questions for the researcher

1. ~~Row granularity~~ — **settled this round: all 793 folders, full coverage.**
2. **Integration strength (Part D)** — cfg-first-with-code-fallback as described, or fully retire the
   hardcoded prefix tables once seed rows cover them?
3. **Build sequence** — the 9 steps above as one round, or split (e.g. steps 1–2 shipped separately
   from 3–8)?
4. **Part E's rule text** — does the proposed distinction match what was meant by "repointing
   escalation files," or was the intent genuinely broader (every escalation-linked file, deliverables
   included)? If the latter, Part A item 5 and every existing escalation-tied plan doc (this one
   included) would need to move.
5. **New, from this redesign:** `manifest_category`/`manifest_currency` as separate columns from
   `type`/`status`, or should the coarser `type`/`status` pair be made to do both jobs (at the cost of
   `file_manifest.category`'s existing 17-value granularity)? Recommendation above is to keep both —
   confirm or override.

Approve scope (and answer 2–5 above), and this builds next round — design → propose → build → verify,
same cycle as every other IBA module.
