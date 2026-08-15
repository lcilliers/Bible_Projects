# Session Log - 2026-08-14 - Prose structure and revision workflow

## Session scope

This session established a navigable prose-store hierarchy, added cross-prose search, created a section-by-section Markdown revision workflow, revised one Programme prose section, and prepared the Programme Chapters 4-6 revision set for the next session.

## Database and hierarchy changes

`prose_section_type` received four hierarchy columns:

- `book_order`
- `book_label`
- `section_order`
- `section_label`

The intended hierarchy is:

```text
Book
  Section
    Chapter
      Prose section
```

The existing fields retain these meanings:

- `label` = chapter title
- `description` = chapter description
- `chapter_no` = chapter number within the section
- `sort_order` = chapter order within the section
- `source_stage` = stable source-stage identifier

Book mappings were populated for Programme, Detail design, Findings, and Essays. Type 78 (`prog_purp_observations_framework`) was corrected from Programme to Detail design, section `Observation framework`, order 6. The existing `source_stage = 'programme'` was retained as provenance.

Backups created during hierarchy work:

- `backups/bible_research_backup_20260814T145046Z_prose_hierarchy.db`
- `backups/bible_research_backup_20260814T182920Z_type78_book_fix.db`

## Exporter

`scripts/build_programme_prose_extract.py` now:

- exports all books by default;
- accepts `--book BOOK_LABEL`;
- accepts `--chapter N` when a book is supplied;
- orders output by book, section, chapter, and sort order;
- excludes soft-deleted section types and prose rows;
- excludes superseded prose rows;
- includes section source-file provenance;
- suppresses the duplicate Programme book/section heading.

Examples:

```powershell
python scripts/build_programme_prose_extract.py --also-markdown --include-body
python scripts/build_programme_prose_extract.py --book Programme --chapter 4 --also-markdown --include-body
```

## Search routine

`scripts/search_prose.py` searches the current active prose through the existing FTS5 index. It supports:

- literal searches;
- raw FTS5 expressions with `--fts`;
- case-insensitive book filtering;
- result limits;
- Markdown report output by default;
- concise terminal summaries.

The report includes book, section, chapter, prose-section ID, version, and source file. The FTS index was checked against `prose_section`; no missing or orphan FTS rows were found. The result count now distinguishes displayed rows from total matches.

## Revision workflow

Two new scripts provide a safe temporary-file round trip:

- `scripts/export_prose_chapter_edit.py`
- `scripts/import_prose_chapter_edit.py`

Export by book/chapter or exact type ID:

```powershell
python scripts/export_prose_chapter_edit.py --type-id 53
python scripts/export_prose_chapter_edit.py --book Programme --chapter 4
```

The edit file contains immutable routing markers for section ID, type code, book, section, chapter, title, sort order, version, and source file. Only the prose body is intended to be edited.

The importer validates the markers and generates a `PROSE` supersede patch. It does not write directly to the database. The patch applicator creates the next version and preserves the prior row through `supersedes_id` and `superseded_by_id`.

## Prose revision applied

The researcher revised type 52 (`prog_disc_tools`). The edit was imported and applied successfully.

- Previous row: `prose_section.id = 19`, version 1
- New row: `prose_section.id = 1040`, version 2
- New word count: 1,284
- New author: `researcher`
- New source file: `outputs/markdown/prose-edit-type-52-20260814.md`
- Patch: `archive/patches/wa-prose-type-52-supersede-20260814.json`

The patch applicator created a pre-apply backup automatically.

## Programme Chapters 4-6 revision set

The first export accidentally included Detail design rows. This was corrected by creating a separate Programme-only folder:

`outputs/markdown/prose-edits/programme-chapters-4-6/`

Current files:

- Chapter 4: 11 files
- Chapter 5: 7 files
- Chapter 6: 13 files
- Total: 31 files

These files represent the populated current Programme section types only. Five seeded handles have no current prose row and therefore have no edit file:

- `sc_v1_ch4`
- `sd_synthesis_Cl4`
- `sc_v1_ch5`
- `sd_synthesis_Cl5`
- `sd_synthesis_Cl6`

The earlier mixed export remains at `outputs/markdown/prose-edits/chapters-4-6/` for reference and was not deleted.

## Documentation updated

The root `README.md` now documents:

- all-book and book-filtered prose extraction;
- chapter-filtered extraction;
- exact type-ID export;
- temporary edit-file handling;
- importer and supersede-patch workflow;
- search, book filtering, FTS mode, limits, and report output;
- the Programme Chapters 4-6 revision folder.

The reusable script catalogue and prose-store architecture reference were also updated for the new routines.

## Validation

Validated during the session:

- exporter and editor scripts compile with Python 3.14;
- type 52 export/import round trip succeeded;
- type 52 supersede patch dry-run passed and live apply succeeded;
- Programme and all-book extracts regenerated successfully;
- FTS row coverage has no missing or orphan rows;
- Programme Chapters 4-6 export contains 31 files with immutable routing markers;
- README and supporting documentation contain the current routine names and paths.

## Next session entry point

Begin with the Programme-only revision files in:

`outputs/markdown/prose-edits/programme-chapters-4-6/`

Revise one file at a time. For each approved edit:

1. run `import_prose_chapter_edit.py`;
2. review the generated `PROSE` supersede patch;
3. run `apply_session_patch.py`;
4. regenerate the relevant prose extract;
5. verify the new version and supersede chain.

No further database work was required to close this session.
