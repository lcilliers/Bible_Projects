# Cross-reference script v3: book carried to a bare "(ch:v)" after a quotation

**Escalation:** #1994 (raised from #1993). **Date:** 2026-10-09. **Narrative files:** not edited.

## 1. The defect

`verse-narrative-ot-crossref-v2-20261006.py`, `cites()`, carried a book to a bare citation only across a short connective gap (`CARRY_GAP`: spaces, `;`, `,`, brackets, "and", "see"…). When a quotation stood between the last full citation and the bare one, the book was not carried, so the verse was reported as not cited:

> … (Ecclesiastes 6:9). He finds envy: "all toil … wind" (4:4).

On #1993, 18 M18 × M47 placements and Isa 58:5 in 10.7 were confirmed only by direct search (validation register §2; claim register v34 cross-reference note).

## 2. The change

| File | Change |
|---|---|
| `verse-narrative-ot-crossref-v3-20261009.py` | New. `tokens()` holds the carry logic; `cites()`, `narrative_index()`, `main()` and the output columns are unchanged in form. |
| `archive/verse-narrative-ot-crossref-v2-20261006.py` | v2, archived (`git mv`). |
| `verse-narrative-ot-crossref-v3-test-v1-20261009.py` | New. Synthetic cases, whole-narrative check, CSV diff against the archived v2. |
| 7 scripts that load the parser by path | Path line changed from v2 to v3 (one line each; plus the docstring line naming the parser in `m18-shared-analysis-crossref-v1`). Archiving v2 would otherwise have broken them: `m18-m47-narrative-weave-v1`, `m18-m47-validation-worksheet-build-v1`, `m18-shared-analysis-crossref-v1` (M18); `m64-H6942H-verses-pull-v1`, `m64-choose-verses-pull-v3`, `m64-m47-marked-verses-m47-trace-v1`, `m64-m47-uncited-pull-v1` (M64). |

**The rule (as asked):** a bare citation that opens its own brackets, as in "(4:4)", "(2:24–25)" or "(65:12; 66:4)", takes the book of the last citation in the same paragraph, whatever text lies between. The note on the place is *book carried across text*. The v2 short-gap carry is unchanged.

**Scope:**
- A paragraph is one line of a chapter file. Prose paragraphs in the narrative are single lines; I checked this and found 0 continuation lines.
- A list bullet is its own line, so nothing carries from bullet to bullet.
- In the open-threads register a row is one line, and the rule never carries across a `|` cell boundary.
- A citation that names another book becomes the new book carried.

**Guards added after testing.** Applied to the whole narrative, the bare rule as asked gave wrong books in a few places. Each guard below was added for a wrong carry actually found. When a guard holds, the citation is left uncarried, as in v2.

| Guard | Wrong carry it stops (narrative text) |
|---|---|
| The text between names another book without chapter:verse | "Ephesians speaks of … (4:23)" read as 1Cor 4:23. "Psalm 106 calls it jealousy (106:16)" read as Num. "Nehemiah named it … (6:8)", "(6:9)" read as Acts. "Matthew gives the setting … (12:14)" and the next three read as Isa. "Ecclesiastes leaves … (3:21)" read as Psa. |
| The last citation was not in brackets | "He goes back to Genesis 2:7 … (15:45)" and "(15:49)" read as Gen; these are 1 Cor 15. |
| The last citation is a parallel, sharing its brackets with a bare citation that had no book | "(15:54; Isaiah 25:8) … (15:55)" read as Isa; this is 1 Cor 15. |
| The book has no such chapter (static table of 66 books and 1,189 chapters) | "(Ecclesiastes 7:9) … (15:28)" read as Ecc; this is Pro 15:28. |

Book names are matched in full and case-sensitive, so "numbers" or "acts" in prose do not stop a carry. The `verse` table in iba.db was not used for the chapter guard because it is incomplete (29,760 rows; Gen 15:21, for example, is missing).

**Cost of the guards:** one correct carry is lost. In "Job 7:15 is his own would-be choice … (7:13–16)" (10.7) the last citation is in prose, not in brackets. It stays uncarried, as in v2.

## 3. Tests

Run: `python verse-narrative-ot-crossref-v3-test-v1-20261009.py "../M18 - desire-longing/m18-m47-validation-register-v1-20261009.csv"`. Exit code 0.

**Synthetic:** 22 of 22 pass. The cases cover:
- a quotation between the citations
- a range, and a chain of bare citations
- a book reset by a citation that names another book
- no book anywhere in the line
- a bare citation not in its own brackets, or with text after it inside the brackets
- a table cell boundary
- the v2 short gap kept
- prose naming another book, the same book, or a lowercase common word
- an unbracketed source
- a parallel source
- a chapter the book does not have
- a bare citation at the start of a line followed by a named book
- a bracket holding only bare citations
- comma verses
- no carry to the next line
- the chapter table

**The 19 known cases.** All are now found by v3:
- 18 rows of the M18 × M47 register with decision a or c: Pro 13:19, Ecc 2:24, Ecc 4:4, Ecc 4:6, Gal 5:24, Ecc 6:3, 2Pe 2:10, Eze 24:21, 1Sa 16:16, 1Th 2:8, Num 11:18, Jon 4:8, 1Sa 16:23, Pro 16:19, Ecc 6:2, Pro 15:15, Ecc 2:26, Ecc 7:2.
- **Isa 58:5 in 10.7** (*Others around a choice* ¶10). v2 found Isa 58:5 only in 13.1 *Delight*.

**CSV diff, v2 against v3** (`m18-m47-validation-register-v1-20261009.csv`, 208 rows):
- **places lost: 0**
- places gained: 31, all in `narrative_refs` and all marked *book carried across text*
- `ot_refs` and `ot_pairing` unchanged
- every other column unchanged
- verses not cited in v2 and cited in v3: exactly the 18 above. The other 13 gains add places for verses already cited, such as Deu 18:6, 2Sa 13:28, 1Ch 28:9 and Psa 19:14.

**Whole narrative** (the current version of every chapter file):
- places found: v2 3,935, v3 4,414
- **places lost: 0**
- 429 bare citations carried across text:
  - **367** have a quotation right before them whose words are found in the ESV text of the carried verse (iba.db `verse`, read-only)
  - **62** have no quotation there, or the quotation is not in that verse. I read all 62 in context and each carries the right book. They are listed below.

| Chapter file | Read and confirmed |
|---|---|
| 02 Life, breath and death | Eze 37:9, Rev 20:15 |
| 04 The heart | 2Ch 26:19, 1Sa 17:17–20, Pro 4:20–27 |
| 05 The soul | 2Ki 1:15 |
| 06 The spirit | 1Sa 16:16 |
| 08 Conscience and bosom | Rom 13:4 |
| 10.1 Feeling | 1Sa 18:29 |
| 10.2 Knowing and hearing | Psa 19:14 |
| 10.5 Speaking | Judg 4:21 |
| 10.6 Wanting | Ecc 4:4, Ecc 6:3 |
| 10.7 Choosing and setting direction | Jos 24:31; Act 15:22, 25; 2Sa 6:20 (twice); 2Sa 6:8–10; 2Pe 1:5–7; Deu 16:11; 1Ki 8:39; 1Sa 20:33; 1Sa 20:42; Joh 15:18; Psa 106:6; Act 15:12; Psa 119:30; Luk 10:40; Act 27:11; Dan 6:4; 1Ki 12:32; 2Sa 13:28; 2Sa 14:29–30; Jam 3:5; Dan 4:27; Dan 4:34; Isa 8:6; Isa 65:12; Isa 56:4 |
| 10.9 Relating to God | 2Ch 28:15, Exo 34:8 |
| 10.10 Relating to others | 2Sa 19:23, Est 5:14, 2Sa 13:28, 2Sa 14:29–31 |
| 10.13 Anger | Hab 2:16, Exo 32:11–13, Psa 80:4, Lam 3:21–22, Num 22:27 |
| 11 Patterns of the inner life | Exo 14:5, Exo 14:8, Est 5:13, 1Sa 1:16, Pro 16:3, Jer 36:24, 1Sa 18:10 |
| 12 When the inner being goes wrong | Exo 14:8 |
| 13.1 Divine | Isa 58:3–5, Jer 50:45, Isa 58:6 |
| 13.2 Angels | 1Pe 1:10 |

## 4. What this does not change

- No narrative file is edited.
- Earlier outputs made with v2 are not rerun. A rerun of any of the 7 loading scripts now uses v3 and will count more citations; v3 loses none of v2's.
- The note in the M18 handoff (`m18-strand-handoff-v1-20261009.md`, open items) and the claim register v34 cross-reference note describe the v2 limitation. Both stay as written records of that pass.
