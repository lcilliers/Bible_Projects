# 2228 — Cluster reading index: design (v1)

Escalation: #2228 v20. Status: design for your review; nothing is built (rule 105). This is tool 2 of
`outputs/escalation/2228-discovery-scope-and-known-v3-20261022.md` (section 3). Tool 1, the scope
resolver, is built and approved (BUILD.md sec 391). The facts below come from a read-only trial run
of the project's own reference parser over every live file in `_analytics/Clusters`, 2026-10-23.

**What it does.** It reads the cluster reading files once and records, for every verse reference in
them, the file, the section and the line where it stands. Afterwards, "what do the cluster files say
about these verses" is a query on that record, not a read of the files. The next tool, the verse
extract, uses the line positions to return only the lines that speak of a verse.

---

## 1. What the trial found

| Measure | Count |
|---|---|
| Live files in `_analytics/Clusters` (outside `archive/`) | 230, in 12 cluster folders and the root; 6.5 MB |
| Sections (split on `#` to `####` headings) | 4,946, of which 3,795 hold at least one reference |
| Verse references found, expanded to single verses | 51,950: 50,088 resolve to a verse, 1,030 name a whole chapter, 832 resolve to nothing |
| Distinct verses named across all files | 11,284 |
| Files with no reference at all | 14 (process notes, READMEs, proposals, surface-form lists) |
| Files whose rows are already in `ib_observation` | 18 (the October ledgers of the four strands; 717 observations name their file) |

**How references are written, counted per occurrence (before range expansion):**

| How the reference is written | Prose | Table row | What it is |
|---|---|---|---|
| **Explicit:** a book named (`Jer 8:18`, `1Co 15:5, 7, 8`) | 19,557 | 12,606 | reliable |
| **Follow-on with chapter and verse:** `(8:18)` after a named reference | 2,307 | 393 | the book is taken from the last named reference |
| **Follow-on with `v.` or `vv.`:** `(v. 12)` | 971 | 228 | book and chapter taken from the last named reference |
| **Bare follow-on:** `(220)` | 984 | 554 | **mostly not a verse**: word counts in tables ("good (220), better (58)") and list counts ("other (10)") |

**Why the 832 do not resolve:** 419 name a verse past the end of the chapter, 304 a chapter the book
does not have, and 109 a verse with no verse row (by design). Nearly all of the first two are
follow-ons that took the wrong book or chapter. Examples: "good (220)" read as 2Ch 32:220; "(16:14)"
after a Nahum reference, where the text is quoting Proverbs. So the same misreading also produces
some references that do resolve, wrongly. That cannot be counted without reading, which is why each
reference keeps how it was found (section 2).

## 2. The design

### Tables (in `iba.db`, registered in `cfg_table` and `cfg_column`)

| Table | One row per | Columns |
|---|---|---|
| `reading_file` | indexed file | path, cluster (from the folder: `M02 - anger-wrath` → M02; root files none), size, sha256, indexed_at, sections, refs, removed (1 when the file is gone or archived) |
| `reading_section` | heading section | file, ordinal, level, heading, the parent headings (path), first and last line |
| `reading_ref` | verse reference occurrence, one row per verse after range expansion | section, file, verse_id (none if it resolves to nothing), book and chapter (for a whole-chapter reference), as written, normalised, **found_by** (`explicit`, `follow-on c:v` or `follow-on v.`), line number, **line_kind** (`heading`, `table row`, `bullet` or `paragraph`), reason when not resolved |

Indexed on `reading_ref.verse_id` and on book plus chapter, so a verse collection finds its rows in
one query.

### Rules the index applies

1. **Which files:** every `.md` under the folders named in a new setting, `reading_index.roots`, which
   starts as `["_analytics/Clusters"]`. Folders named `archive` are skipped. Nothing else of
   `_analytics` is in it, by your exclusions.
2. **References:** by the parser the narrative register already uses (`narrativeregister.parse_refs`),
   over the whole file, so a follow-on takes its book from the reference before it. **Bare
   follow-ons are not taken** (section 1). This needs one optional argument on `parse_refs`; the
   narrative register's own calls keep today's behaviour, and that is tested.
3. **A whole-chapter reference** (`Psa 51`) is kept as a chapter, not spread over all its verses. A
   verse collection finds it through book and chapter, marked as a chapter mention.
4. **A reference that resolves to nothing** is kept with its reason and listed in the report. The
   files are records of past work and are not edited.
5. **Incremental:** a file is read again only when its sha256 changes. A file gone or archived is
   marked removed; its rows stay for history but are not read.
6. **Already imported:** the 18 ledger files are indexed like any other. `reading_file` carries how
   many observations name the file, so a later tool can show that a file's rows are also in the
   tables rather than present them twice (D2).

### Tool

`Reading-Index.ps1`, through `run.py`, work package `reading-index`:

| Step | Does | Writes |
|---|---|---|
| `-Step Build` | indexes new and changed files and marks removed ones | the three tables (write grants) |
| `-Step Report` | the coverage report: per cluster folder, files, sections with and without references, references by found_by and line_kind, the unresolved with reasons, the files with no reference | `reading_index.output_dir` (read-only on the tables) |

Config, through `apply_logged`: the work package, both steps, their refused routes, write grants,
the two settings, a `cfg_report` row, `cfg_utility` rows for the new files, the three tables in
`cfg_table` and `cfg_column`, and any `cfg_enum` values for found_by and line_kind.

## 3. Test plan (on a `dbsnapshot.copy_db` copy, files in a scratch folder)

| # | Case | Expected |
|---|---|---|
| 1 | Build over a scratch copy of `_analytics/Clusters` | 230 files; section and reference counts equal the trial's, less the bare follow-ons |
| 2 | Build again, nothing changed | no file re-read; no row written |
| 3 | One file edited | only that file re-read; its rows replaced |
| 4 | One file removed, one moved into `archive/` | both marked removed; their rows not returned |
| 5 | A synthetic file with each written form (explicit, `(c:v)`, `(v. n)`, bare `(n)`, a range, a list, a whole chapter, a table row, a bullet, a heading) | each recorded with the right found_by, line number and line_kind; the bare follow-on not recorded |
| 6 | A reference past the end of a chapter; one with no verse row | kept with the right reason; in the report |
| 7 | Query by a verse collection (tool 1's output for M02 -OnlyStrong H3708A) | the rows on those 22 verses, in one query |
| 8 | `parse_refs` with its default arguments, against the narrative register's current citations | unchanged: the same references as `narrative_citation` holds |
| 9 | Report | written to the setting's folder; its totals equal the tables |
| 10 | `configmaint.validate` hard checks on the copy | clean |
| 11 | Speed | a full build within a minute; an unchanged rebuild within seconds |

## 4. What is not in this design

- **The verse extract (tool 3):** it reads the lines this index points to. A separate design follows.
- **Reading or judging the content of a file:** the index records where verses are named, not what
  is said about them.
- **The other folders of `_analytics`:** excluded by you. The setting allows a folder to be added
  later, but none is proposed.

## Decisions for you

| # | Question | Your choice | Comment |
|---|---|---|---|
| D1 | Approve this design for the build? | | |
| D2 | Index the 18 ledger files already in `ib_observation`, flagged as imported (recommended), or leave them out of the index? | | |
| D3 | Leave out the bare follow-ons `(220)` (recommended: mostly word counts), or keep them flagged as a weak form? | | |
