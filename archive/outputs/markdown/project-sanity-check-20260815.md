# Project Sanity Check — Maintenance & Coherency — 2026-08-15

Scope: whole repo (main Bible-study programme + `iba/app/` sub-project). Method: direct
inspection of git state, live DB schema, config tables, and governance docs — no assumptions
carried over from prior session summaries.

## 1. Open question — not resolved here, needs your call

**2026-08-14 session did substantial work on the main study's DB and prose store**
(`bible_research.db`: `prose_section_type` hierarchy columns added, Programme book/section
mappings populated, a chapter-level revision workflow built — `export_prose_chapter_edit.py` /
`import_prose_chapter_edit.py` / `search_prose.py`, a Chapters 4-6 revision set staged). This is
real, substantial new work on the *main* programme, not the IBA app.

Current memory records two things that don't obviously cover this:
- `project_study_closed_20260803` — whole study (main DB **and** IBA) closed 2026-08-03.
- `project_iba_study_reopened_20260805_v4` — reopens **only the IBA verse-lexical line**
  (2026-08-05), explicitly scoped to IBA's v4 lexical-reading instruction.

Neither memory records a reopening of main-study prose/Programme work. Was there a separate
instruction (given directly in the 2026-08-14 session, not yet written to memory) to resume
Programme prose revision on the main DB? If so I'll write that memory now — I don't want to
guess at its scope and get it wrong a second time.

## 2. Git hygiene — standing rule not followed

Per `CLAUDE.md` §12, completing a session log requires the full commit-and-push cycle in the
same unit of work. `SESSION-LOG-20260814-prose-structure-and-revision-workflow.md` is a
complete, filled-in log sitting **uncommitted** at repo root, alongside 55 other changed/new
files it describes (26 archived Programme-prose files deleted, new prose export/import/search
scripts, new patch JSON, new outputs). Nothing from 2026-08-14 has been committed or pushed —
last commit is `aab47254` (2026-08-13 15:32), and today is 2026-08-15. Local `main` is otherwise
in sync with `origin` (0 ahead / 0 behind on committed history), so this isn't a push problem,
it's that the close-out step never ran.

**Action:** once §1 is answered, this is a straightforward catch-up commit (the working tree
diff is coherent and matches the session log's own description — nothing looks accidental).

## 3. Repo-hygiene drift (small, worth a sweep)

- **`.obsidian/` at two locations** (project root and `Workflow/Programme/`) are untracked but
  not fully gitignored — `.gitignore` only excludes `workspace.json`/`workspace-mobile.json`
  inside `.obsidian/`, not the folder itself, so `app.json`/`appearance.json` etc. would be
  picked up by a blanket `git add`. Worth adding a blanket `.obsidian/` ignore rule.
- **`database/scripts/`** (new, untracked) holds VS Code SQLite-extension scratch query files —
  `Untitled-3.sqlite3-query` is a literal editor-generated throwaway, not a project artefact.
  `database/` per `CLAUDE.md` §2 is meant to hold only the DB file and `file_manifest.json`.
- **`query_db.py` at repo root** — an ad-hoc one-off query script outside `scripts/` and outside
  the `_tmp_*`/prefix conventions in `CLAUDE.md` §6. Same content is presumably now superseded
  by the registered `scripts/search_prose.py` built the same session.

None of these are destructive; they're just clutter that a routine `git add` sweep would either
commit accidentally (the sqlite-query scratch files, the obsidian app state) or leave orphaned
(`query_db.py`). Recommend deciding per §12's "read before staging" rule when the 2026-08-14
catch-up commit happens.

## 4. Documentation currency — self-disclosed, not a hidden bug

`CLAUDE.md` §3's own header already flags this, but for completeness: the file cites schema
**3.31.0** (§10), **3.33.0** (§3 title / §4 `EXPECTED_SCHEMA_VERSION` reference), and **3.35.0**
(top banner) at different points, while the live DB is at **3.40.0** and `engine/constants.py`
`EXPECTED_SCHEMA_VERSION` is correctly set to `"3.40.0"` — the *code* is current, only the
prose in `CLAUDE.md` has fallen behind across several method resets. This is the expected shape
given the file's own "compact reference, can lag" caveat and the pointer to
`outputs/markdown/project-reconstruction/` as authoritative — but that reconstruction is dated
2026-06-14, now two months stale relative to a huge amount of intervening IBA/cluster work. Not
urgent to fix, just worth knowing the fallback-authoritative doc is itself dated.

## 5. IBA app — internally coherent, no action needed

Checked because it's the sub-project the request called out specifically:

- `git status --short -- iba/` is **clean** — everything through commit `aab47254` is fully
  committed. No orphaned local-only IBA work.
- Live `iba.db` schema-version tracking (`cfg_change_log`) and the two live governance rules —
  `governance.build_md_on_code_change` and `governance.governance_md_on_rule_change` (both
  approved+applied 2026-07-22, escalations #238/#239) — are being honoured: `BUILD.md` (Aug 13)
  and `USER-GUIDE.md` (Aug 13) track the same recent work described in the git log
  (M10b/M10c/M27/T2/T3 taxonomy cleanup, M32 cluster creation, cluster-assignment module).
  `GOVERNANCE.md` is a few days older (Aug 9) than `BUILD.md`, but nothing in the Aug 10-13
  commits reads as a *rule* change (vs. ordinary feature/data work), so that gap looks
  consistent with the rule's actual scope rather than a violation of it.
- 23 `cfg_*` tables present and populated; `EXPECTED_SCHEMA_VERSION` in code matches the DB's
  latest applied migration.

## 6. Not concerning — logged for completeness

- `iba/app/db/iba.db` has grown from ~113MB (July snapshots) to ~669MB current. Large but
  consistent with the volume of taxonomy/cluster/backfill work logged across the last week of
  commits; not itself a red flag.
- `backups/` holds 4 local pre-op DB snapshots (~3GB total, all from 2026-08-14 plus one from
  2026-07-14) — well inside the `BACKUP_RETENTION = 10` ceiling.

## Bottom line

The project is **not incoherent** — the IBA sub-app in particular is in good order: clean git
state, live governance rules actually being followed, code/schema in sync. The one real gap is
process, not content: **2026-08-14's main-study work was never closed out** (§2), and its scope
relative to the "study closed / IBA-only reopened" memory record isn't yet confirmed (§1).
Everything else is minor filing clutter (§3) or already-acknowledged doc lag (§4).
