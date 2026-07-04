# Verse-record coverage by book (> 75%), excluding the 5 completed — 2026-07-04

> Measure: **distinct verses in `wa_verse_records` (active) ÷ the book's canonical verse count.** Live from DB. Excludes the 5 completed wisdom books (Psalms, Proverbs, Ecclesiastes, Job, Lamentations). Cross-checked: `wa_verse_records` and the `verse` (measure) table agree verse-for-verse on the books sampled, so the figure is consistent across both stores.

## Answer: **42 books** sit above 75% verse-record coverage.
The ~214 inner-life words touch verses densely across almost the whole canon; only the narrative-heavy history books fall below 75%.

### Prophets (15)
Hosea 97.0 · Micah 95.2 · Isaiah 94.7 · Habakkuk 94.6 · Malachi 94.5 · Haggai 92.1 · Nahum 91.5 · Daniel 91.3 · Zephaniah 90.6 · Jonah 85.4 · Jeremiah 85.1 · Amos 83.6 · Zechariah 82.5 · Joel 80.8 · Obadiah 76.2

### NT epistles + short books (18)
Jude 100.0 · Titus 97.8 · Romans 94.7 · 2 Peter 90.2 · 2 Corinthians 89.9 · 1 Corinthians 89.0 · Ephesians 88.4 · Philippians 86.5 · 1 Peter 85.7 · Colossians 85.3 · 2 John 84.6 · James 83.3 · 1 Thessalonians 82.0 · 2 Thessalonians 80.9 · 2 Timothy 79.5 · 3 John 78.6 · Hebrews 78.5 · 1 Timothy 76.1

### OT Torah / history (8)
Judges 90.0 · Ruth 84.7 · Deuteronomy 84.6 · Genesis 81.5 · Esther 80.8 · Leviticus 80.1 · Numbers 78.3 · 1 Samuel 78.1

### Wisdom / poetry not yet completed (1)
**Song of Solomon 79.5** (93/117) — see correction below

## ⚠ Correction to the earlier assessment
`wa-book-coverage-assessment-20260703.md` recorded **Song of Songs as "LOW (<25%)"** and put it on hold. That figure was **wrong** — the DB shows **Song of Solomon at 79.5% (93/117 verses)** in both the verse-record and verse-table stores. Song is *well-covered* and needs no special hold; it is a normal full-book candidate (its "held pending a what-it-indexes check" note is moot).

## Just-below-75% (for reference)
Galatians 73.8 · 1 John 72.4 · Philemon 72.0 · Ezekiel 70.6 · 2 Samuel 69.6 · Matthew 68.4 · Revelation 68.1 · 2 Chronicles 67.0 · Nehemiah 66.5 · Exodus 65.4 · Luke 64.3 · Mark 63.3 · 2 Kings 61.1 · 1 Kings 60.8 · Acts 59.9 · Joshua 58.8 · Ezra 50.7 · 1 Chronicles 36.6

## Implication for sequencing
The next-book field is wide open — essentially every prophet, every epistle, and the Torah/history except Chronicles/Ezra/Kings/Joshua is >75%. Densest and most inner-being-rich clusters: the **Minor Prophets** (Hosea, Micah, the Twelve), **Isaiah/Jeremiah/Daniel**, and the **Pauline + catholic epistles** (Romans, the Corinthians, Ephesians, the Petrine/Johannine letters). Method note (still open): oracle/argument/narrative genres differ from lyric — the segmentation-first variant (method §15) should transfer with genre-specific unit typing.
