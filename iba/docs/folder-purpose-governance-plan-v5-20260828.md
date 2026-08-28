# Folder-purpose governance mechanism — plan (v5)

> Escalation #971 (consolidates #929 v8 / #736 v7 carryover, researcher's own instruction to combine
> into one item). This is **a plan for the researcher's decision, not a build** — nothing here is
> implemented yet. **Supersedes v4 (2026-08-28) in full.** Changes this round: the build sequence is
> rephased into the researcher's own explicit ordering (build table → run manifest to populate it →
> use configs to populate the extra columns → identify config/script gaps → work through
> needs-attention folders to *plan* migration); the actual file-migration step is split out to a new
> escalation, **#976**, raised this round to collect migration notes as this escalation's
> classification work proceeds; and Part C's column question is resolved (retain both column sets,
> merged rather than replaced). Full proposal, not a delta — this document stands alone.

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
5. The folder-purpose table needs a properly designed column set and named methods that keep it
   current, not accurate-once-then-drifting like the manifest's own 13-day-stale scan. Two-part
   purpose, stated directly by the researcher: *"partly to give me visibility what is going on, and
   partly to allow you to make the right filing decisions."*
6. **Added this round:** the build itself is sequenced explicitly by the researcher — table, then
   manifest population, then config population, then gap-identification, then per-folder migration
   *planning* — with the actual file-moving step split into its own escalation, **#976**, so this
   escalation stays about the governance mechanism and #976 owns the physical cleanup that mechanism
   eventually recommends.

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
layered on top of this governance mechanism rather than blocking it (and, per this round's split,
would itself land in #976 when it happens).

## Part C — `folder_purpose`: full column design + the three methods that keep it current

**Coverage: every folder in the census, not a curated subset.** All 793 rows from
[`outputs/folder-census-20260828.csv`](../../outputs/folder-census-20260828.csv) become `folder_purpose`
rows — the table's whole point, per the researcher, is *"to give me visibility what is going on,"*
which a partial table can't do.

**Category, unchanged from v3's correction:** a reference/data table, not `cfg_*` — same template as
`books` (`bible_research.db`): registered once in `cfg_table`/`cfg_column` (governance.tables applies
to every table), but its *rows* are maintained directly by the three methods below, not through
`configmaint.propose` per change.

### Column design — resolved: both sets retained, merged (open question 5, answered)

The researcher's `type`/`status`/`usage_description` columns and the earlier
`manifest_category`/`manifest_currency` proposal measure different things and don't conflict — the
researcher's own instruction was to augment, not replace, so both stand. **Every column from the
census, carried in verbatim** (the census output *is* the seed data for these columns):

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

**Plus, confirmed this round — both new-column groups kept:**

| column | type | values | purpose |
|---|---|---|---|
| `manifest_category` | TEXT, nullable | `file_manifest.category`'s existing 17-value set (`iba`, `session`, `script`, `cluster`, `discovery`, `workflow`, `investigation`, `patch`, `report`, `doc`, `log`, `directive`, `code`, `export`, `import`, `backup`, `other`) | What `file_manifest.category` a file in this folder should get — feeds Part D's manifest lookup. Kept separate from `type` because the manifest's category taxonomy is 17 values wide and can't be represented by a 3-value field without losing information existing `file_manifest` consumers depend on. |
| `manifest_currency` | TEXT, nullable | `file_manifest.currency`'s existing 6-value set (`current`, `archived`, `cross-reference`, `historical`, `backup`, `other`) | Same reasoning, for `file_manifest.currency` |
| `type` | TEXT | `archive` \| `operations` \| `results` | The researcher-facing coarse classification. Registered in `cfg_enum` (name `folder_purpose_type`) per `governance.project_lookups_and_naming_convensions` |
| `status` | TEXT | `authoritative` \| `mixed` \| `reallocate` \| `stale` \| `deleted` | The folder's audit/health status — `deleted` replaces what would've been a separate `active` flag entirely. Registered in `cfg_enum` (name `folder_purpose_status`) |
| `usage_description` | TEXT, nullable | free text | What this folder is actually for — the `cfg_table.use`/`cfg_column.use` model, scoped to a folder |
| `added_at` | TEXT | ISO timestamp | When the row was first created |
| `last_reviewed_at` | TEXT, nullable | ISO timestamp | When `type`/`status`/`usage_description` were last confirmed accurate |

**The governing invariant, stated directly by the researcher: "no folder is used by the system, without
a `governed_by_setting`."** Any row with `type='operations'` and an empty `governed_by_setting` is an
anomaly — either something writes there undeclared in any `cfg_setting`, or `type` is wrong. This is
Method B's core check, not just a guideline in prose.

### The three methods

**a) Manifest validate** — a new step in the manifest routine, run every time the manifest is
rebuilt: inserts a row (disk-derived columns computed, judgement columns blank) for any new folder;
sets `status='deleted'` (never physically removed) for any folder no longer on disk; refreshes every
existing row's disk-derived columns without touching `type`/`status`/`usage_description`; lists
exceptions (disk facts inconsistent with recorded classification) in the rebuild report for review.

**b) Configmaint cross-check** — a new `configmaint.validate` check: re-derives `governed_by_setting`
for every row from the live `cfg_setting` table (config-side truth, can change without any file moving
— can't be Method A's job); enforces the invariant above (`type='operations'` with no
`governed_by_setting` flagged; the inverse gap — a `cfg_setting` pointing at a folder with no
`folder_purpose` row — flagged too); reports anomalies through the existing `configmaint.validate`
mechanism, same pattern #972 just went through.

**c) Table editor (PS)** — a new `FolderPurpose.ps1` front door, the *only* sanctioned way to change
`type`, `status`, or `usage_description` by hand. Cannot touch the disk- or config-derived columns
(Methods A/B own those); setting any judgement column updates `last_reviewed_at` automatically. No
`configmaint.propose` gate, matching the `books` maintenance model.

**Relationship to the ~26 existing `governance.*_dir`/`*.output_dir`/`*.report_path` settings
(#939–969): sits *alongside*, does not replace.** `governed_by_setting` is the live, machine-maintained
(Method B) link between the two layers.

## Part D — manifest integration (folded into Part C's methods above)

**Current state, checked live:** `manifest.py`'s `classify_category()`/`compute_currency()` are
hardcoded Python prefix tables with no entry for `_analytics/` (6,577 files, per the census) — falls
through to `category='other'`. **The manifest hasn't been rescanned since 2026-08-15** (13 days,
predates this week's entire reorg); 4,303 rows (23%) already sit in `other`. **Fixing this is
explicitly in scope.**

**The two-way flow:**

1. `manifest._scan()` looks up each file's folder against `folder_purpose.manifest_category`/
   `manifest_currency` first (longest matching `folder_path` prefix wins); falls back to the existing
   hardcoded logic only when no row matches — non-breaking.
2. Method A is what keeps `folder_purpose` itself in sync with the disk, driven by the same scan
   `manifest._scan()` already performs — one walk of the tree, two tables updated from it.
3. Method B is what keeps `governed_by_setting` in sync with `cfg_setting`, and enforces the
   operations-needs-a-setting invariant.

**Immediate, separate finding (fixed in the same round, mechanical, not a design call):**
`file_manifest` itself — 18,653 live rows — is **not currently registered in `cfg_table`/`cfg_column`**
at all, violating `governance.tables`/`governance.table_columns`. Registered as part of this build.
(`folder_purpose` gets its own `cfg_table`/`cfg_column` entry when created.)

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
— discoverable by reading the registry, not only this plan. This is also the first concrete instance
of Part D's "identify the gaps for changes in configs" phase below.

## Build sequence — rephased into the researcher's own explicit ordering

**Physical file migration is explicitly OUT of this escalation's scope, split to escalation #976
(raised this round).** This escalation's build stops at *planning* what should move where; #976 owns
executing those moves, whenever the researcher is ready for that separate step.

**Phase 1 — build the table.**
1. Register `file_manifest` in `cfg_table`/`cfg_column` (config change, normal propose/approve cycle)
   — mechanical compliance fix, ahead of everything else.
2. Register `folder_purpose_type`/`folder_purpose_status` in `cfg_enum`, and `folder_purpose` itself in
   `cfg_table`/`cfg_column` (config change, same cycle).
3. Build `folder_purpose` schema + `folderpurpose.py` + `FolderPurpose.ps1` (Method C) — code, no
   per-row approval.
4. Part A — `filing` behaviour class + rules (items 1–5) + `filingkit.versioned_path()` + naming-drift
   `configmaint.validate` check (config change, same cycle) — bundled into this phase since it's
   independent, already-approved-scope work with no ordering dependency on the rest.

**Phase 2 — fix and run the manifest to populate the table.**
5. Wire `manifest.py`'s classification lookup to `folder_purpose` (Part D point 1) and build Method A
   (manifest validate: new/deleted-folder reconciliation + disk-derived column refresh + exceptions)
   — code.
6. Run `Manifest-Rebuild.ps1` — the first fresh scan since 2026-08-15. Seeds/refreshes all 793 rows'
   disk-derived columns (`direct_file_count` through `governed_by_setting`'s placeholder);
   `_analytics/` and every other post-reorg folder now classifies correctly in `file_manifest` itself.

**Phase 3 — use configs to populate the known extra columns.**
7. Build and run Method B (configmaint cross-check): derives `governed_by_setting` for every row from
   live `cfg_setting` values, and — since a folder already named by a `governance.*`/`report.*` etc.
   setting has an obvious `type='operations'`/`status='authoritative'` — pre-fills those two judgement
   columns wherever the config data already makes the answer unambiguous (the ~26 settings-governed
   folders, at minimum). Rows with no governing setting are left for Phase 5.

**Phase 4 — identify the gaps for changes in configs and scripts.**
8. Review Method B's anomaly output: `type='operations'` rows with no `governed_by_setting`
   (undeclared system use — needs a new `cfg_setting`, or the folder isn't really operational);
   `cfg_setting` values with no matching `folder_purpose` row. Apply Part E's own resolution as the
   first concrete case (the new filing rule + the `outputs/escalation` row's `usage_description`).
   Output of this phase: a reviewed list of config/script gaps, each either fixed directly (mechanical)
   or escalated (a judgement call) — not silently left as an advisory list.

**Phase 5 — work through the needs-attention folders and plan (not execute) migration.**
9. Using `FolderPurpose.ps1` (Method C), go through every row still `status`-blank or in
   `mixed`/`reallocate`/`stale` after Phases 3–4, and record in `usage_description` what *should*
   happen to it (stays as-is, gets merged into another folder, gets archived, needs a `cfg_setting`
   created, etc.) — a plan per folder, not a move. **Every concrete migration candidate this phase
   produces gets logged as a note on escalation #976**, so #976 accumulates a real, reviewed worklist
   rather than starting blank when the researcher is ready to execute it.

**Phase 6 (separate escalation #976, not this one).**
10. Physical file migration, executed against #976's accumulated worklist, once the researcher decides
    to run it. `BUILD.md`/`GOVERNANCE.md`/`USER-GUIDE.md` updates for the mechanism itself (Phases
    1–4) land in the same unit of work as those phases, per the standing rule — not deferred to #976.

## Open questions for the researcher

1. ~~Row granularity~~ — **settled: all 793 folders, full coverage.**
2. ~~Integration strength / build sequence~~ — **settled this round**, per the phased sequence above.
3. ~~Column design (`manifest_category`/`manifest_currency` vs. `type`/`status`)~~ — **settled: both
   retained, merged.**
4. **Part E's rule text — still open.** Does the proposed distinction (tool-report-path vs.
   engineering-documentation-folder) match what was meant by "repointing escalation files," or was the
   intent genuinely broader (every escalation-linked file, deliverables included, into
   `outputs/escalation/`)? If the latter, Part A item 5 and every existing escalation-tied plan doc
   (this one included) would need to move — this is Phase 4's first test case, so worth settling
   before that phase runs.

Approve scope (and answer 4 above), and this builds next round — Phase 1 first, verified, before
Phase 2 starts.
