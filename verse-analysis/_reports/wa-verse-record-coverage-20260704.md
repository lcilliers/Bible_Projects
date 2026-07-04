# Verse-record coverage by book (> 75%), excluding the 5 completed — 2026-07-04

> Measure: **distinct verses in `wa_verse_records` (active) ÷ the book's canonical verse count.** Live from DB. Excludes the 5 completed wisdom books.

## ★ CORRECTED FOR PURE-T2 VERSES (researcher, 2026-07-04)
**T2 = reference/qualifier terms (never analysed standalone).** A verse present in `wa_verse_records` *only* because of a T2 term is not genuine inner-being content — counting it inflates coverage, badly, in proper-noun-heavy books. Re-measured as **distinct verses with ≥1 non-T2 term ÷ canonical**:

- **Only 20 books remain > 75%** (down from 42 on the raw count).
- The skew is huge in narrative: Genesis **81.5% → 52.4%** (446 pure-T2 verses), Numbers **78.3% → 44.1%** (441), Judges **90.0% → 57.4%** (201), Ruth **84.7% → 52.9%**, Song of Solomon **79.5% → 49.6%** (35 pure-T2).
- The high-coverage field is now dominated by the **epistles** and a few **prophets** — genres that argue/exhort about the inner life rather than narrate.

### The 20 books > 75% by GENUINE (non-T2) coverage
| Book | genuine % | (raw %) | pure-T2 |
|---|---|---|---|
| Titus | 93.5 | 97.8 | 2 |
| Jude | 92.0 | 100.0 | 2 |
| Romans | 87.1 | 94.7 | 33 |
| 2 Corinthians | 86.8 | 89.9 | 8 |
| Malachi | 85.5 | 94.5 | 5 |
| 2 John | 84.6 | 84.6 | 0 |
| 2 Peter | 83.6 | 90.2 | 4 |
| Colossians | 82.1 | 85.3 | 3 |
| 1 Peter | 81.9 | 85.7 | 4 |
| Philippians | 81.7 | 86.5 | 5 |
| Hosea | 81.2 | 97.0 | 31 |
| Ephesians | 79.4 | 88.4 | 14 |
| 1 Corinthians | 78.3 | 89.0 | 47 |
| Isaiah | 77.9 | 94.7 | 216 |
| 1 Thessalonians | 77.5 | 82.0 | 4 |
| Zephaniah | 77.4 | 90.6 | 7 |
| Micah | 77.1 | 95.2 | 19 |
| 2 Thessalonians | 76.6 | 80.9 | 2 |
| James | 75.9 | 83.3 | 8 |
| 2 Timothy | 75.9 | 79.5 | 3 |

### Borderline (73–75% genuine)
Jonah 75.0 · Habakkuk 75.0 · Deuteronomy 73.5

### ⚠ Song of Solomon — correction retracted
My earlier note called the "<25%" figure wrong and Song "well-covered." **Half-right:** the raw figure is 79.5%, but **genuine (non-T2) coverage is only 49.6%** — Song is thick with proper nouns and geography (35 of 93 verse-record verses are pure-T2). So the *original instinct to hold Song was sound* — its genuine inner-being-term density (~50%) is well below the real candidates (76–94%). The specific "<25%" number was wrong, but Song is genuinely under-covered in the IB register. **Keep Song on hold / treat as a special case.**

---
## (superseded) Raw answer: 42 books > 75% on the un-corrected count
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
