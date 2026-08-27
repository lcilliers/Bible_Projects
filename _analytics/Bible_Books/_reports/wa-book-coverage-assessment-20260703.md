# Book coverage in the corpus — next full-book candidates (2026-07-03)

> **★ STATUS UPDATE (2026-07-03, end of day):** the **wisdom/poetry corpus is COMPLETE** — Psalms (150), Proverbs (31), **Ecclesiastes (12, ids 624-635)**, **Job (42, ids 636-677)**, **Lamentations (5, ids 678-682)** all through the full pipeline (backfill → Phase-1 → segmentation → Phase-2), DB-canonical + reproducible. Song of Songs remains **held** (LOW coverage — investigate what-it-indexes before treating). **Next tranche = the well-covered prophets** (Isaiah 95 · Hosea 97 · the Twelve) **and Pauline epistles** (Romans 95 · Ephesians 88 · Colossians 85), with a method note that oracle/argument genres differ from poetry (the segmentation-first variant, method §15, should transfer). See `project_poetic_chapter_driven_method` (memory) and `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` §15.

> Researcher: freeze the characteristic list (provisional; can rebuild from the corpus anytime) and go to the next phase — analysing more books. Question: *which other books are largely covered in the corpus, so we can use the full-book coverage on them?* Measure: verses present in the `verse` table (study-term-touched) ÷ the book's true length.

## Finding — coverage is broad
**~34 books sit at ≥80% verse coverage.** The ~214 inner-life words touch verses densely across most of the Bible, so many books are near-complete and (like Ps/Pro) can be backfilled to 100% for full-book treatment.

### Remaining WISDOM / POETRY books — the natural continuation (proven method)
| book | coverage | why next |
|---|---|---|
| **Ecclesiastes** | **91%** | direct wisdom sibling to Proverbs; home of the insatiable, vanity, weariness, *"the inner life beyond material circumstance"* (M46) — extends the desire/appetite + contentment threads we just mapped |
| **Job** | **90%** | the deepest inner-being book — the tested/afflicted self, grief, voiced complaint, integrity-under-suffering, the argument with God |
| **Lamentations** | **87%** | concentrated grief/lament (five acrostic poems) — sibling to the Psalter's laments |
| Song of Songs | raw 79.5% · **GENUINE (non-T2) 49.6% (58/117)** | ⚠ The specific "<25%" number was wrong, **but the instinct to HOLD was right.** Raw verse-record coverage is 79.5%, but excluding pure-T2 (reference/proper-noun) verses it is only **49.6%** — 35 of 93 verse-record verses are pure-T2 (Solomon, place names, geography). Song is genuinely under-covered in the inner-life register vs the real candidates (76–94%). **Keep on hold / special case.** See `wa-verse-record-coverage-20260704.md`. |

### Well-covered non-poetic books (method needs light adaptation for oracle / narrative / argument)
- **Prophets:** Hosea 97 · Isaiah 95 · Micah 95 · Habakkuk 95 · Malachi 95 · Nahum 91 · Zephaniah 91 · Haggai 92 · Joel 81 · Amos 84 · Zechariah 82 · Jeremiah 85 · Daniel 91 · Ezekiel 71
- **Torah / history:** Deuteronomy 85 · Genesis 82 · Leviticus 80 · Ruth 85 · Esther 81 · Numbers 78
- **NT:** Romans 95 · Ephesians 88 · Colossians 85 · 2 Peter 90 · 1 Peter 86 · 1 Thess 82 · 2 Thess 81 · 2 Timothy 80 · (Hebrews ~78)

## Recommendation
Complete the **poetic/wisdom corpus** next — the chapter-driven + segmentation method is proven there — in this order: **Ecclesiastes → Job → Lamentations.** Start with **Ecclesiastes**: it is the direct sibling to Proverbs, its coverage is 91% (small backfill to 100%), and its themes pick up exactly where Proverbs left off (the never-satisfied eye, contentment, the heart under vanity, the inner life beyond circumstance). Then Job (the giant of inner-being suffering), then Lamentations. Song of Songs is held pending a coverage/what-it-indexes check.

After the poetic corpus, the well-covered **prophets** (Isaiah, Hosea, the Twelve) and **Pauline epistles** (Romans, Ephesians, Colossians) are the next tranches — with a method note that oracle/argument genres differ from poetry.

## Data-quality flag (minor)
`book_id 58` (Hebrews) contains a stray mis-filed verse "1Pe 4:11", which collided a coverage label (showed an impossible 224% for "1Pe"). One mis-assigned verse; worth a cleanup pass but does not affect the assessment (real 1 Peter = book_id 60, 86%).
