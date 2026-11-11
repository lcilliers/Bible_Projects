# #2457 Stored verse counts below STEP counts: findings (read-only investigation)

Session 8ca87189, 2026-11-11. Nothing was written to any table. Every figure is from queries over `iba.db`; the queries are in the scratchpad of this session.

## The question (#2457)

For G4433 (6 against 1), G5219 (79 against 21), H1431 (123 against 114) and H1396 (25 against 24), `strong.count` is higher than what `verse_lexical` and `strong_verse` hold. What does `strong.count` count, and are verses missing from the load?

## What `strong.count` is (recorded meaning, `cfg_column`)

"STEP token frequency, NOT a verse count, may be capped." `strong.freqList` is "raw frequency distribution": a list of `tokens@verses` entries (`tokens` alone when equal), one for each of 31 or 18 sources (Greek and Hebrew codes differ in length). The sources are not named in the database.

## Findings

1. **For the four codes named, nothing is missing.** The first entry of `freqList` equals what iba.db stores, exactly: G4433 1 token in 1 verse (ours 1/1), G5219 21/21 (ours 21/21), H1431 117 tokens in 114 verses (ours 117/114), H1396 25 tokens in 24 verses (ours 25/24). `strong.count` (6, 79, 123, 25) is not this entry and not a verse count.
2. **`strong.count` is a different measure.** Over all 15,452 strongs with a first entry: `count` equals the first entry's tokens for 10,318, is higher for 4,992 and lower for 142. What it counts (for G5219 79 where the first source has 21) is not recorded in the database; the STEP response that holds it is not stored beyond the two columns. Not established.
3. **The first `freqList` entry matches iba.db for 13,545 of 15,452 strongs (87.7%)** on both rows and verses. Of the 1,907 that differ: 1,779 have fewer verses in iba.db than the first entry; 113 have the same verses and one or a few more rows in iba.db (for example G0191: 429 rows, 428 tokens, 398 verses both); 14 have more verses in iba.db; 1 fewer rows with the same verses.
4. **The verse table has gaps, and that is the likely source of the 1,779.** `verse` is recorded as "one row per verse of the ESV text, all 66 books". Stored: 29,760 live verses. All 1,189 chapters are present, but 1,222 verses are absent inside chapters (the sum of each chapter's highest stored verse is 30,982), and 22 chapters have no verse 1: 1 Chronicles 5, Genesis 4 (Gen 1:1 is absent, Gen 1 holds verses 2 to 31), Acts 3, Song 2, 1 Kings, Isaiah, John, Joshua 1 each. 1,222 is a lower bound (verses after a chapter's last stored verse cannot be seen this way). That a missing verse accounts for a strong's one-verse shortfall is consistent with this; it is not proven for any one strong, because the list of verses STEP counts is not in the database.
5. The recorded meaning of `verse` says 25,634 rows; the table holds 29,762 (2 deleted). The text is out of date.

## What this means for the work

- The four codes of #2457 are answered: no loss for them; `count` is not their verse count.
- Reports and counts that depend on "every verse where a word occurs" (the evidence report, the surface and collection work) can miss occurrences in the absent verses, for the strongs in the 1,779.
- A new item is raised for the gaps (#2471): why verses are absent, and which; a design for loading them goes to the researcher (B:105).

## Not done

No attempt to load or repair verses. The meaning of `strong.count` was not looked up at STEP (no outside call made).
