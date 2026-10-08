# learning4comfort search: verse-reference matching (#1988)

**Date:** 2026-10-08 · **Escalation:** #1988 · **Repo changed:** `C:\learning4comfort` (separate site repo; not committed or pushed. Pushing to `main` deploys the live site, so that waits for the researcher.)

Researcher instruction, verbatim: *"proceed with 1988. Search for specific verses must not be broken up in loose segments."*

## What was wrong

Both search boxes (`site/global-search.js`, `site/book-search.js`) split the query into letter and number runs. They kept a section if every run appeared anywhere in it as a substring. "Rom 8:27" became `rom` + `8` + `27`, so "from", "promise" and any number containing 8 or 27 counted as hits. In the site-wide search this gave 98 sections.

## What changed

| File | Change |
| --- | --- |
| `site/search-match.js` (new) | One shared matcher used by both boxes: query parsing, reference reading, word matching, excerpt |
| `site/global-search.js`, `site/book-search.js` | Use the shared matcher. They show "N results citing Romans 8:27"; an unreadable reference shows "No matches found" with the reason |
| `site/search/index.html` | Loads `search-match.js` before `global-search.js` |
| `scripts/build_book_search_indexes.py` | Book pages get `search-match.js` before `book-search.js` |
| `tests/test_book_search_indexes.py` | Checks the matcher loads before the book search |

### A reference query is matched as a whole reference

- A query reads as a reference when it is **book + chapter[:verse[-verse]]** ("Rom 8:27", "Romans 8:26-27", "1 cor 13:4", "1cor 13:4", "Song of Solomon 2:4", "Psalm 23"), or a bare **chapter:verse** ("8:27", which matches that verse in any book).
- Book names: all 66 books, full names plus common abbreviations, including the ones used on the site (Rom, Eph, Col, 1 Cor, 2 Sam, Jdg/Judg, Psa, Pro, Phili, Jas…).
- It is matched only against **references written in the text**, never against letter or number fragments. A section matches when one of its references **overlaps** the query:
  - **Ranges:** "Romans 8:26–27" is found by "Rom 8:27". Hyphen and en dash both work, and so do cross-chapter ranges ("Genesis 29:16–30:24").
  - **Lists:** "Hebrews 9:14; 10:22", "Ephesians 3:16, 20" and "Romans 5:5; 8:26–28; 12:2, 19–21" each yield every reference. "Romans 8:28, 1 Corinthians 2:9" is not misread as Romans 8:1.
  - **Follow-on references with no book,** such as "(8:27)" or "(see 14:2)", take the last book named earlier in the same section.
  - **Appendix lists** written as "Matthew: 1:18, 1:20, 12:18" (Holy Spirit Appendix B).
  - **Whole chapters:** "Psalm 23" written in the text counts as the whole chapter. This applies to full book names only, so abbreviations never turn ordinary words into references.
- Book names in the text must start with a capital letter, so "the job 7 hours" or "mark 2:3" in running text are not references.
- An unknown book with chapter:verse ("Xyz 8:27"), or any query containing chapter:verse that cannot be read, returns **"No matches found"** with the reason. It never falls back to loose fragments.

### Word search

- Each word must match **from the start of a word**. "rom" finds "Romans" but no longer "from" or "promise"; "fear" still finds "fears" and "fearful".
- **"Quoted phrases"** match as a whole phrase, words in order.
- Unquoted words still all have to appear in the section, in any order (unchanged).

## Test results (site built locally exactly as `deploy-pages.yml` does; site-wide index, sections matched)

| Query | Before | After |
| --- | --- | --- |
| Rom 8:27 | 98 | 7 (incl. 10.9 and 13.1) |
| Romans 8:26-27 | 26 | 9 |
| Romans 8 | 79 | 35 |
| Psalm 23 | 60 | 3 |
| Gen 50:20 | 23 | 8 |
| 2Sa 14:14 | 0 | 4 |
| Joshua 24:15 | 18 | 7 |
| Isa 42:1 | 39 | 2 |
| Mat 12:18 | 56 | 1 (Holy Spirit App. B list) |
| Job 7:15 | 50 | 1 |
| Xyz 8:27 | 0 | 0, with message "not a book of the Bible this search recognises" |
| Romans 99:1 | 2 | 0 |
| fear | 135 | 135 |
| fear of the Lord | 94 | 94 |
| "fear of the Lord" (quoted) | 94 | 15 |
| rom | 451 | 95 |
| heart | 243 | 241 |
| will | 278 | 275 |

- **Mat 12:18** finds no inner-being section yet. 13.1 v9, which carries it, is in the publication inbox and is not published yet; it is found once published.
- **"heart" and "will"** dropped by 2 and 3. Those were matches inside another word, which word-start matching drops by design.
- Book search was checked on `/books/holy_spirit/?q=Mat 12:18`: "1 result citing Matthew 12:18 in this book", from Appendix B.
- Python tests: 2 run, OK.

## For the researcher to decide

1. **Go live:** commit and push the learning4comfort changes, which redeploys the site. Not done; it needs your go-ahead.
2. **Word matching** is "starts a word" rather than strict whole-word. Strict whole-word would stop "fear" finding "fears". Say if you want strict.
3. A bare "8:27" query matches that verse in **any** book. Say if you would rather it ask for a book.
