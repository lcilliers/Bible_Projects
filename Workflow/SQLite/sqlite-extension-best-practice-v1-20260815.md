# SQLite Extension — Best Practice Guide — v1 — 2026-08-15

Written in response to the researcher's request, following the review note: "this is done to get
better visibility of the database, and to get around Claude not consistently being helpful with
identifying issues in the DB. The DB is not visible enough for me and Claude have consistently
misled me or simply did not put enough thought into the implications of the data in the DB." That
trust gap is the actual reason this guide exists — the practices below exist to close it, not
just to make the extension tidier.

## What this is

The VS Code SQLite extension lets you open `.db` files directly in the editor — browse tables,
run ad-hoc SQL, see real rows — without going through Claude Code or any script. It writes its
scratch queries as `.sqlite3-query` files wherever you happen to save them.

## The core practice: verify, don't just trust

**Use the extension as an independent check on anything Claude reports about the database,** not
only as a convenience for your own exploration. When a report here claims a row count, a
join result, or "no orphaned records," that claim should be reproducible by you, directly, in the
extension — not something you have to take on faith. Two habits that make this practical:

1. **Ask for the query, not just the number.** If a claim matters to a decision, ask for the
   exact SQL behind it (or read it directly from a report script) so you can re-run it yourself.
2. **Cross-check joins, not just single-table counts.** A count against one table can look clean
   while the join that actually matters (the one a decision depends on) tells a different story —
   this is exactly the kind of gap `feedback_enumerate_link_tables_first` and
   `feedback_evidence_signal_completeness` in memory exist to catch, and the extension is your
   own independent way to catch it too.

If the extension ever contradicts something reported here, that's worth surfacing directly (per
your existing `Workflow/Chat_responses/` review-note pattern) — it's exactly the signal this
guide exists to make actionable, not something to quietly work around.

## Read-only by default — especially against `iba.db`

`iba/app/db/iba.db` runs in WAL mode and is under active write traffic whenever the app is
running (config-maintenance, report generation, cluster-assignment runs, etc.). Two implications:

- **Prefer opening connections read-only** when you're just browsing or checking a claim. Most
  SQLite tools/extensions support a read-only connection mode; use it unless you have a specific
  reason to write.
- **Never write to `iba.db` or `bible_research.db` directly through the extension** as a way to
  fix something. Both databases have a governed write path for a reason:
  - `bible_research.db` — changes go through `scripts/apply_session_patch.py` against a JSON
    patch, so every write is validated and auditable.
  - `iba.db` — config changes go through `iba\app\ps\Config-Maintenance.ps1 -Step Propose`
    (approval-gated); data writes go through the app's own registered utilities.

  A direct `UPDATE`/`INSERT`/`DELETE` from the SQLite extension bypasses both of those, and
  bypasses the audit trail that makes the DB trustworthy in the first place — exactly the kind of
  silent, unaudited change the project's governance rules exist to prevent. Use the extension to
  **see** the problem, then route the actual fix through the normal pipeline (a patch, or a
  `configmaint.propose` run).

## File conventions

- **Location:** save exploration/extraction `.sqlite3-query` scratch files to `scripts/`, not
  loose in whatever folder happened to be open. This is now the standing convention (adopted
  2026-08-15) — Claude Code follows it too when it runs its own explorations.
- **Naming:** prefix every `.sqlite3-query` file `SQLite_`, so they're visually distinct from the
  Python scripts sharing the same folder, and name them for what they actually check —
  `SQLite_prose_section_type_list.sqlite3-query`, not `Untitled-3.sqlite3-query`. A file with no
  name carries no information six months from now about what it was checking or why.
- **The DB path in the header comment matters.** These files carry a `-- database: <relative
  path>` header that only resolves correctly from the folder they're saved in. If a file moves
  (as three did on 2026-08-15, from `database/scripts/` to `scripts/`), check that the path
  comment still points at the right `.db` file relative to the new location.
- **Commit them.** As of 2026-08-15 these are tracked in git like any other script — they're part
  of the project's reusable-scripts catalogue in spirit (ad-hoc SQL is often the fastest way to
  answer a real question), not throwaway. If a query genuinely was one-off and answered, it's fine
  to delete it rather than let it accumulate — but a query worth re-running belongs in
  `scripts/`, findable, not buried in whatever folder the extension happened to default to.

## Connecting to both databases

The project has two databases with a clear split (confirmed 2026-08-15):

- `database/bible_research.db` — prose store + analytic findings. Open here for anything about
  `prose_section`, `prose_section_type`, `finding`, `cluster`, `characteristic`.
- `iba/app/db/iba.db` — process control + the entire base data layer (word initiation through
  verse-lexical analysis). Open here for `cfg_*` tables, `word_strong`, `strong`,
  `strong_meaning_parsed`, `verse_lexical`, `span`, and anything else base-layer.

Don't assume a table lives in the database you happen to have open — if a query returns "no such
table," that's often not a typo, it's the wrong database for that data (per the architecture
split above, not a bug).

## What this doesn't replace

The extension is for **inspection**, not for the kind of structured, repeatable reporting the
project already has scripts for (`report.py`, `build_correlation_extract.py`,
`generate_registry_overview.py`, IBA's `report.*` commands). If a query starts looking like
something you'll want to run again with different parameters, or that should be part of a
standard report, that's a signal to register it properly rather than keep re-running it by hand —
same principle as the cost-awareness guidance already in `CLAUDE.md` §9.6 about not duplicating
existing reports.
