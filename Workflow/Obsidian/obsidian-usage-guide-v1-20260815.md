# Obsidian Usage Guide — v1 — 2026-08-15

Written in response to the researcher's request for a comprehensive Obsidian usage guide, given
increasing use of Obsidian to read and prepare `.md` files across this project.

## What Obsidian is for here, and what it is not for

**Obsidian is a reading/navigation layer over the project's `.md` files. It is never a second
source of truth.** For anything the project already treats as DB-canonical — prose
(`prose_section` in `bible_research.db`), findings/analysis, IBA's `cfg_*` config, `word_registry`
— the database row is authoritative and the `.md` file is a generated view or a working draft on
its way back into the DB via a patch. Editing a generated `.md` file in Obsidian does not change
the database; it only changes that file, and a regenerated export overwrites it. This matters
because Obsidian makes it very easy to build a private mental model of "the state of things" from
what's open in the vault — keep that model pointed at the DB, not at whatever files happen to be
in the graph.

Where Obsidian earns its place: the huge body of governance, instruction, session-log, and
review-note `.md` files that are **not** DB-backed and genuinely benefit from backlinks, tags,
and full-text search across thousands of files — exactly the file-navigation pain point already
raised.

## Vault scope — one vault at the repo root

Use a single Obsidian vault rooted at `C:\Bible_study_projects`, not separate vaults per
subfolder (`Workflow/`, `iba/`, etc.). Obsidian's backlinks and graph view only connect files
that share a vault — the whole value of the tool for this project is seeing how a `Workflow/
Instructions/` doc, an `iba/app/` doc, a session log, and a `Sessions-v2/` output relate, and that
only works if they're all in the same vault. A `.obsidian/` folder already exists at the repo
root and is now fully gitignored (as of the 2026-08-15 catch-up commit) — per-machine UI state,
never committed.

**One caveat already found:** a second `.obsidian/` folder had also appeared at
`Workflow/Programme/` — a nested vault opened separately at some point. Nested vaults inside a
vault confuse Obsidian's own indexing (it doesn't recurse into a sub-vault). If that folder is
still in use, decide whether `Workflow/Programme/` should be its own vault (in which case the
root-vault approach above doesn't apply to it) or whether it was opened by accident and should be
closed so everything lives in the one root vault. Worth a deliberate choice, not left as
incidental duplication.

## Frontmatter and tags — the real fix for "hard to navigate"

The single highest-leverage habit: give every `.md` file in the vault (or at least every one
worth finding again) YAML frontmatter with a small, consistent set of tags. Without this,
Obsidian's search and graph are only marginally better than `grep` — the payoff comes from being
able to filter and pivot.

Suggested tag dimensions, matching how work is actually organised in this project:

```yaml
---
tags:
  - project/main          # or project/iba — which side of the DB split this belongs to
  - book/hosea             # book-folder scope, where applicable (matches verse-analysis/{Book}/)
  - cluster/M33            # M-code cluster, where applicable
  - doctype/session-log     # session-log | instruction | governance | review-note | report | prose-edit
  - status/draft            # draft | current | superseded
---
```

Not every file needs every tag — a session log doesn't need a `cluster/` tag, a cluster
instruction doesn't need a `book/` tag. The point is consistency *within* a doctype so that
"show me every governance doc," "show me every Hosea-scoped file," or "show me every review note"
is a one-click filter (Obsidian's search: `tag:#doctype/review-note`) rather than a manual
`file_manifest.json --search` guess.

This can be adopted gradually — retrofitting thousands of existing files with frontmatter is its
own project (folds into the file-store-consolidation step already on the roadmap). New files
going forward are the cheap win: add the frontmatter block when writing a new session log,
review note, or instruction doc.

## Backlinks and the graph view — the actual navigation answer

Once files reference each other with `[[wikilinks]]` (or even just tags), two built-in views do
the work that "file management is still hard to navigate" is asking for:

- **Backlinks pane** (open on any file): every other file that links to it. For a governance doc
  like `CLAUDE.md` or `GOVERNANCE.md`, this becomes a live "everything that cites this rule" list
  — better than grepping for the doc's filename, because it also catches `[[wikilink]]`-style
  references that don't spell out the full path.
- **Graph view**: a visual map of the vault's link structure. Filter it by tag (e.g.
  `tag:#doctype/instruction`) to see just the instruction-doc web, or by folder to see one area
  in isolation. This is the practical answer to "I can't see the shape of the project's own
  documentation" — the graph *is* that shape, once files link to each other.

Link deliberately: when a new doc supersedes or extends an old one, put a `[[wikilink]]` to it (as
`CLAUDE.md` already does with plain-text cross-refs like "see `docs/interaction-preferences.md`"
— Obsidian will resolve a `[[docs/interaction-preferences]]` link the same way and make it
clickable/backlink-able, which the plain-text version can't be).

## Search

Obsidian's built-in search (`Ctrl+Shift+F` / the search pane) is full-text across the whole vault
— this is the one thing `file_manifest.json` genuinely cannot do today (it indexes filenames and
extracted metadata, not file bodies — see the 2026-08-15 review response for the fuller gap
analysis). For "find every file that mentions Strong's H1234" or "find every file discussing
grace," Obsidian's search already does this, right now, with no build step — a real near-term
answer to the "find files by keyword" need while a proper cross-corpus content index (the bigger,
DB-integrated version of the same idea) gets scoped separately.

Two practical notes: (1) Obsidian's search only covers files inside the open vault — if a vault is
scoped narrower than the repo root, results will silently miss files outside it (another reason
for the single-root-vault recommendation above); (2) it searches file content as saved to disk,
so DB-canonical `.md` exports are only as current as the last export run.

## Optional: Dataview plugin

If the frontmatter-tagging habit above takes hold, the community **Dataview** plugin can build
live index pages from it — e.g. a query that lists every `doctype/session-log` file with its date,
auto-updating as new logs are added, without hand-maintaining an index. This is worth trying once
there's enough tagged content to query, not before. Flagging as an option, not a recommendation to
install today — it adds a dependency and a query language to learn, and the tag-only approach
above already delivers most of the navigation value on its own.

## Summary of concrete steps

1. Keep (or deliberately choose) one vault at the repo root; resolve the nested
   `Workflow/Programme/.obsidian/` question.
2. `.obsidian/` is already fully gitignored — nothing further needed there.
3. Start tagging new `.md` files with the frontmatter block above; retrofitting old files is a
   later, separate piece of work (file-store consolidation).
4. Use `[[wikilinks]]` for doc cross-references going forward so the backlinks pane and graph
   view carry real information.
5. Use Obsidian's full-text search as the practical near-term answer to "find files by keyword,"
   while a real content index is scoped as part of file-store consolidation.
6. Never treat an Obsidian-edited copy of a DB-generated `.md` file as itself authoritative —
   the database is still the source of truth for prose, findings, and config.
