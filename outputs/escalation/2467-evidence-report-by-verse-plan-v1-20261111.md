# Evidence report for a verse or list of verses: plan (for approval, B:17)

Session 8ca87189, Developer Mode, 2026-11-11. Request (researcher, chat): "this report looks handy, can you add a switch that will allow for the same report to be generated for a verse or list of verses (be clear on the format for the references to use)". Nothing built yet.

## The switch

`Collection-Build.ps1 -Action Evidence -Verse "<references>" [-Check]`, used instead of `-Collection` (giving both, or neither, is refused with nothing written).

## Reference format (read from the existing parser, `parse_refs` in `iba/app/lib/narrativeregister.py`, and the verse table)

- One verse: `Pro 6:14`. A range: `Pro 6:14-16`. Across chapters: `Pro 6:30-7:2`. A whole chapter: `Pro 6`. A list: separate the items with a semicolon, in quotes: `"Pro 6:14-16; Mat 11:29; 1Sa 24:5"`.
- Book names: the book as the verse table writes it (`Mat`, `Mar`, `Joh`, `1Sa`, `Phili`, `Phile`, `Song`) or any alias in `narrative.book_alias_map` (194 entries, for example `Matt`, `Matthew`, `1Sam`, `1 Samuel`, `Ps`, `Psalms`, `Philemon`). A name that is not an alias is refused, naming it.
- A verse that is not in the verse table is refused, naming it; nothing is written. A reference given twice is refused, as a collection named twice is.
- The report prints each verse's reference as the verse table writes it.

## Order and organisation (researcher, chat 2026-11-11: "the report must be organised by verse, and consecutively by Scripture chapter and verse")

- The report is one section for each verse, and inside it the whole chain below. Nothing is grouped by word, collection, observation or claim at the top level.
- The sections run in Scripture order: book in the project's book order (`cfg_book_order`), then chapter, then verse, whatever order the references were given in. `Pro 6:14` comes after `Pro 6:2`, and `Mat 11:29` after every Old Testament verse.
- Inside a verse the words follow their position in the verse (`verse_lexical.position`, then code ordinal), the observations follow their id, and each claim and narrative section is shown once at the verse where it first applies and cited by reference at later verses of the same report (so a section that tells many verses is not printed many times). The CSV carries one row for each word, node, claim and telling and is sorted in the same Scripture order.
- Stated for the collection report: it stays organised by member word as built and approved (#2464); say if it should be reordered by verse as well.

## Two orderings for every report (researcher, chat 2026-11-11, after reading the collection-by-word report)

The researcher: the report must have two orderings, "by word, by type" (the default) and "by type" (an additional switch), used in different circumstances.

- **Default, by word then by type:** the report is one section for each word (for a collection report: each member surface, in alphabetical order), and inside it the types in chain order: the word's occurrences (`verse_lexical`), observations and nodes, change history, claims, narrative tellings and sections. Verses inside a type follow Scripture order. For a verse report the unit is the verse (as above), then the types.
- **`-ByType`:** the report is one section for each type across everything in scope (all occurrences, then all observations, and so on, as the approved #2464 report is laid out today), the rows inside a type in Scripture order (collection report: by word then Scripture order; verse report: Scripture order).
- The two orderings hold the same rows; only the grouping differs. A claim or narrative section that serves several words or verses is printed in full once and cited by id at its other places in the by-word layout; in the `-ByType` layout it appears once in its type section anyway. The CSV is unchanged by `-ByType` (one sorted chain), except that its sort follows the chosen ordering.
- The collection report as approved (#2464) is today the `-ByType` layout; the default changes to by word then by type. This re-lays-out the closed #2464 output and so is part of this build.

## What the report holds for a verse (the same chain, keyed by verse instead of by collection)

1. The verse (ESV text, osisId).
2. Every word of it in `verse_lexical` (all words, not only collection members), each with the collections and tiers its surface belongs to (stored links only; blank when none).
3. Every observation node on those words, with its observation and the change history.
4. The claims that name the verse or one of those observations, and the narrative sections that tell them, with their text.
5. Stored-data faults, by the same rules where they apply to a verse.

Same rules as before: nothing evaluated, inferred or written to a table; a missing link is stated as no rows.

## Build (small, no schema change)

- `iba/app/lib/collectionevidence.py`: `resolve_verses(...)` (uses the existing parser, refuses as above) and `build_verse(...)`; the renderer and CSV reuse the existing sections.
- `iba/app/handlers/collectionbuild.py`: the handler takes `-Verse`; `iba/app/ps/Collection-Build.ps1`: the `-Verse` parameter.
- Config through `apply_logged`: setting `collection.evidence_verse_name` (the file stem, `verse-evidence`), and the step text updated.
- USER-GUIDE 8.14 and BUILD.md updated. Tests: a single verse, a range, a list, a chapter, a bad book, a verse not in the table, both switches, neither, and counts against independent queries.

## Decisions for you (recommendation first)

1. Show all words of the verse, with their collections (recommended), or only the words that belong to some collection.
2. A list gives one report with a section for each verse (recommended).
