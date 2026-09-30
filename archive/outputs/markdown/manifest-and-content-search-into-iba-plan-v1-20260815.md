# Plan: Manifest Management + Content Search — Built Into the IBA App

**Status: A built, verified, and delivered (2026-08-15) — B not started.** `manifest.rebuild` /
`manifest.search` are live: `iba/app/lib/manifest.py`, `iba/app/migration/bootstrap_file_manifest.py`,
`iba/app/handlers/reports.py` additions, `iba/app/ps/Manifest-Rebuild.ps1` /
`Manifest-Search.ps1`, `USER-GUIDE.md` §13a, `BUILD.md` §112. Ran for real (18,653 files indexed,
`configmaint.validate` clean). §3 below (originally "open questions") is now a settled-decisions
record. §4 below is B's plan, still entirely unbuilt — no `cfg_*` rows, no code, no migration for
it yet. This is the concrete scoping for
[`docs/governance-alignment-register.md`](../../docs/governance-alignment-register.md) item #2
(filing/archiving rules → step 2, file-store consolidation) and item #6, and the manifest
content-search gap flagged in
[`project-review-response-2-20260815.md`](project-review-response-2-20260815.md) §3.

## 1. The two capabilities (confirmed distinct, confirmed in scope)

| # | Capability | Confirmed scope |
|---|---|---|
| A | **Manifest** — build, update, search file *metadata* | Ported from `scripts/build_file_manifest.py` into IBA, governed, config-driven. **Build and deliver first.** |
| B | **File content search** | Only file search — explicitly *not* prose search (`prose_section_fts`, already exists, out of scope) and *not* a `bible_research.db` analytic-findings search (that's a separate, future "reports for exploring research_db" thread, not this one). Round 1 restricted to `.md` files, project-wide, **including `archive/`**. |

## 2. Design decisions (researcher, 2026-08-15) — checked against live governance, not just recorded

### 2.1 Both A and B live in `iba.db`

Researcher's framing: *"IBA App is the engine for all processing related tables. Search result and
utilities is process. Research_db will be used for analytic findings and there will be different
reports to be defined for exploring the research_db."* This resolves the placement question I'd
flagged as murky — and it's not just a policy call, it's structurally correct: I checked, and the
**predefined key source for B (§2.3) already lives in `iba.db`**, not `bible_research.db` —
`strong` (15,293 rows: `strongNumber`, `stepGloss`, `stepTransliteration`, …), `strong_sense`,
`strong_lexicon`, `word_strong` are all IBA's own base-data tables (concordance-driven per-Strong's
onboarding, per `governance.verse_gap_by_design`). So this design needs **no cross-database read** —
everything both A and B need is already inside `iba.db`.

### 2.2 The search flow chains metadata → content → index update, and results carry file + location

Researcher: *"search must search the file metadata, and then the content, and then update the
index so that the search result will include the file reference and location."*

**My reading, stated plainly since the exact mechanics weren't spelled out — flag if this isn't
what you meant:** a `maintenance.content_search` call (i) runs an incremental index refresh first
(mtime-based — only `.md` files that are new or changed since the index's last pass, not a full
rescan every search), so the index is never stale at query time, then (ii) executes the key lookup
against the now-current index, then (iii) returns hits enriched with the manifest's own metadata
(category, type, registry/cluster/date if the filename carries them) alongside the content hit's
**file path and location** (line number). That's "metadata, then content, then keep the index
current, result carries file + location" as one composed operation — built on top of A rather than
duplicating it. If the intent was instead a strict three-step *user-visible* flow (search metadata
→ separately search content → separately trigger a reindex), say so and I'll split it into three
steps instead of one composed one.

### 2.3 Search keys are predefined, sourced from IBA's own DB tables — not free-text/FTS

Researcher: *"we can use DB tables (e.g. strong numbers and gloss) as the keys for the search
build"* / *"the search keys will be predefined."* This is a real design change from my original
draft (which assumed a generic FTS5 free-text index, modelled loosely on `prose_section_fts`) to a
**concordance-style inverted index**: for each predefined key, record every `.md` file (+ line) where
it occurs. Confirmed key sources already in `iba.db`:

- `strong.strongNumber` (e.g. `H2734`) — 15,293 rows
- `strong.stepGloss` — the English gloss text for each Strong's number
- `word_strong` — the project's own English-word ↔ Strong's-number mapping (the ~214-word list)

This is a **narrower, more precise, and more buildable** capability than open-vocabulary full-text
search, and it's the right shape for the stated purpose: finding every file across
`Sessions/`/`Sessions-v2/`/`Workflow/`/etc. that touches a specific Strong's number, gloss, or word
while consolidating findings into prose. **Not decided yet, flagging rather than assuming:** whether
cluster/characteristic names should be added as a second key category in round 1 or held for a later
round — round 1 as specified is Strong's-number/gloss/word only; I'd suggest holding
cluster/characteristic keys for round 2 once the Strong's-based index is proven, but say if you want
them in round 1.

### 2.4 Scope: all `.md` files, project-wide, including `archive/`

Confirmed. Scan root = the whole project tree, filtered to `.md` only. Still excluded on structural
grounds (not text, or already DB-native): `database/` (binary DB files), `backups/`, `.git/`. Prose
itself is DB-native (`prose_section.body`), not filed as loose `.md`, so there's no real overlap risk
there — but `iba/app/verse-analysis/**/*.md` (the app's own generated verse-lexical/verse-span-
meaning/debate output) **is** in scope, since it's real `.md` content on disk, not DB-stored prose,
and is exactly the kind of file the consolidation phase needs to search.

### 2.5 Governance: this must be built as a properly classified IBA utility

Researcher: *"the work package must follow the governance for utilities in IBA."* Checked directly
against live governance rather than assumed:

- **`cfg_step.kind` is mandatory** (`GOVERNANCE.md` §27) — dispatch refuses any step with
  `kind IS NULL`. A's two delivered steps (`manifest.rebuild`, `manifest.search` — see §3; the
  `maintenance.*` names originally sketched here didn't survive contact with the build, in favour
  of the project's own `<subject>.<verb>` convention, e.g. `table.export`) are both `kind='utility'`
  — the same classification every existing `report.*`/`configmaint.*` step carries (read-only or
  index-maintenance work, not the study's substantive analytic content, which is what `kind=
  'operations'` is reserved for: `raw`/`registry`/`lexicon`/passage-debate-prep/`narrative`). B's
  steps (working names `content_index.rebuild`/`content_index.search`) will follow the same rule.
- **A separate `cfg_utility` row is also required** (`GOVERNANCE.md` §26) for the new library
  module(s) that implement this — one row per `iba/app/lib/*.py` module (module name, file path,
  purpose), checked by `configmaint.validate`'s unregistered-module and config-density checks.
  `iba/app/lib/manifest.py` (A) already has its row. B's module — proposed `iba/app/lib/
  contentindex.py` — will need its own when built.
- **Config density is enforced, not advisory-only in spirit.** Every new setting this introduces —
  scan roots, the `.md` filter, index/manifest table names — must be a genuine `cfg_setting` the
  code actually reads, not a literal; `find_orphan_configs` will flag it live if it isn't.
- **Steps register via a direct `bootstrap_*` migration** (the established carve-out,
  `GOVERNANCE.md` §9B/§14 — direct `cfg_*` inserts, not routed through `configmaint.propose`
  row-by-row), same as `bootstrap_book_narrative_generate.py`.

## 3. A — delivered (2026-08-15)

Built as two independently-invokable work packages (`file-manifest-rebuild` / `file-manifest-search`
— same shape as the existing `log-retention`/`table-export` precedent, not one chained package),
not the `maintenance.*` step names originally sketched above — `manifest.rebuild` / `manifest.search`
fits the project's own naming (`table.export`, `retention.report`) better than an invented
`maintenance` namespace, so that changed during the build.

- `iba/app/lib/manifest.py` — classification (category/type/currency + date/registry/version/
  cluster/word extraction) ported near-verbatim from `scripts/build_file_manifest.py` as code
  (project-naming fact, not a config decision — see the module's own docstring for the reasoning),
  plus one addition: an `iba` category/type-set for the `iba/` subtree, which the original script
  left as "other." `manifest.skip_dirs`/`manifest.exclude_exts`/`manifest.report_path` are
  `cfg_setting` (module `manifest`).
- `iba/app/migration/bootstrap_file_manifest.py` — DDL for the new `file_manifest` table (`iba.db`,
  replacing the loose 8.3 MB `database/file_manifest.json`) + `cfg_work_package`/`cfg_step`
  (`kind='utility'`, §27) / `cfg_setting` / `cfg_utility` (§26) / `cfg_report`+`cfg_report_section`
  rows, the established direct-bootstrap carve-out (§9B/§14).
- `iba/app/handlers/reports.py`: `manifest_rebuild`/`manifest_search`. `iba/app/ps/
  Manifest-Rebuild.ps1` / `Manifest-Search.ps1`.
- `USER-GUIDE.md` §13a, `BUILD.md` §112 — both updated in the same unit of work, per
  `governance.build_md_on_code_change`.

**Verified, not just written:** migration ran idempotently; `manifest.rebuild` run for real via the
dispatcher — 18,653 files indexed (10,099 active, 8,554 archived); `manifest.search` run with both
a field query (`type:iba-migration`, 89 matches) and free text (`governance-alignment`, 1 match,
correctly located); `configmaint.validate` clean on everything this migration touched.

**One own bug found and fixed mid-build:** the first `configmaint.validate` pass failed —
`manifest` had been used as a `cfg_setting.module` value without being added to
`enum.config_module` first. Fixed in the same migration (added the missing `cfg_enum` insert),
re-ran idempotently, re-validated clean.

**Two pre-existing, unrelated errors surfaced incidentally, left open, not fixed here:**
`cfg_report_csv_table` rows for `report.registry`/`report.cluster` name table names that aren't
real tables. Confirmed pre-existing — still present after the manifest-specific errors were fixed,
so not caused by this work. Recorded as escalation #642 for your judgement (which of the two rows
is wrong, or whether a table is missing, needs a look I haven't taken — out of scope for this build).

## 4. B — not started; still the plan as scoped in §2

Nothing built for B: no `cfg_*` rows, no `contentindex.py`, no migration. §2 above is the settled
design — predefined-key concordance (Strong's number/gloss/word) over all `.md` files project-wide
including `archive/`, in `iba.db`, reusing `file_manifest` (§3) as its coverage baseline — ready to
build the same way A was, on your go-ahead.

**One follow-up not yet decided, flagged rather than assumed:** whether/when to retire
`scripts/build_file_manifest.py` and `database/file_manifest.json` now that IBA owns this
capability. Same shape of question as governance-alignment register item #1 (a superseded-by
banner, not deletion) — raised here for your call, not acted on.
