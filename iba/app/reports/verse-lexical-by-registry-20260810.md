# verse_lexical summarised by word_registry — whole Bible (2026-08-10)

> Regeneration of [`nt-verse-lexical-by-registry-20260809.md`](nt-verse-lexical-by-registry-20260809.md),
> re-run against the live DB, **rescoped from NT-only to the whole Bible**. The 2026-08-09 report
> was titled "NT" and filtered to NT books only; checking `verse_lexical` book coverage live for
> this run found it is now built for **all 66 books** (534,075 rows / 29,037 verses total, OT
> included) — narrower NT-only scoping is no longer the right lens for "how many verses relate to
> a registry word," which is what this regeneration was asked to answer. The 178 active
> `word_registry` / 4,796 active `word_strong` link counts are unchanged from 2026-08-09 (verified
> live) — nothing drifted there; only the book scope of the join changed.
>
> Same join as before: `word_registry → word_strong (exact code) → verse_lexical.strong`, now
> against every book, not just Matt–Rev.
>
> **Purpose of this run:** not a fresh structural audit (§2/§4 of the 2026-08-09 report still
> stand and weren't re-checked here) — this regeneration exists to get a volume reading for the
> new **inline linked-Strong's verse-annotation report** under design (see
> [`eph-1-3-verse-lexical-stream-sample-20260810.md`](eph-1-3-verse-lexical-stream-sample-20260810.md)),
> now that its scope has been set to **every verse a registry word's Strong's occurs in**, not one
> example verse per Strong's. §3 is the new material.

## 1. Headline (whole Bible)

| Metric | Value |
| --- | --- |
| Active `word_registry` entries | 178 |
| Active `word_strong` links | 4,796 |
| Distinct Strong's codes linked to ≥1 registry word | 3,457 |
| `verse_lexical` rows, whole Bible | 534,075 (66/66 books) |
| Distinct verses with a `verse_lexical` row | 29,037 |
| **(registry word, verse) pairs — the new report's real unit of output** | **196,144** |

The last row is the number that matters for the volume question: it's the total count of
"a registry word has ≥1 linked Strong's in this verse" facts across the whole registry — summing
each word's verse count (a verse legitimately counts under more than one word when their Strong's
sets overlap there, same non-disjoint-sum caveat the 2026-08-09 report noted at code level).

## 2. Per-registry verse counts, whole Bible (178 words, sorted by verses touched)

| Word | Status | Strong's linked | codes (whole Bible) | verses (whole Bible) |
| --- | --- | --- | --- | --- |
| reasoning | raw-complete | 39 | 13933 | 10128 |
| calling | raw-complete | 49 | 12190 | 9080 |
| being | raw-complete | 444 | 11350 | 8987 |
| purpose | raw-complete | 39 | 8838 | 7064 |
| endurance | raw-complete | 47 | 7653 | 6201 |
| thought | raw-complete | 47 | 7181 | 5712 |
| meditation | raw-complete | 21 | 5563 | 4561 |
| yielding | raw-complete | 29 | 5189 | 4407 |
| longing | raw-complete | 78 | 5161 | 4245 |
| power | raw-complete | 82 | 4681 | 3852 |
| knowledge | raw-complete | 27 | 4194 | 3572 |
| discernment | raw-complete | 26 | 3631 | 3110 |
| understanding | raw-complete | 47 | 3570 | 3088 |
| the afflicted | raw-complete | 76 | 3558 | 3034 |
| worship | raw-complete | 42 | 3487 | 2923 |
| meaning | raw-complete | 16 | 3179 | 2855 |
| boastfulness | raw-complete | 31 | 3036 | 2773 |
| surrender | raw-complete | 10 | 3047 | 2534 |
| strength | raw-complete | 78 | 2820 | 2368 |
| delight | raw-complete | 56 | 2734 | 2323 |
| mind | raw-complete | 58 | 2624 | 2243 |
| seeking | raw-complete | 30 | 2457 | 2171 |
| listen | raw-complete | 26 | 2679 | 2103 |
| fear | raw-complete | 62 | 2363 | 2061 |
| name | raw-complete | 19 | 2349 | 1915 |
| spirit | raw-complete | 23 | 2248 | 1912 |
| desire | raw-complete | 62 | 2043 | 1811 |
| mourning | raw-complete | 47 | 2059 | 1791 |
| love | raw-complete | 52 | 2104 | 1768 |
| blessing | raw-complete | 20 | 1804 | 1628 |
| heart | raw-complete | 38 | 1856 | 1606 |
| contentment | raw-complete | 26 | 1700 | 1557 |
| Cursing | raw-complete | 29 | 1767 | 1547 |
| slander | raw-complete | 26 | 1670 | 1472 |
| testimony | raw-complete | 22 | 1594 | 1426 |
| sin | raw-complete | 48 | 1808 | 1418 |
| condemnation | raw-complete | 22 | 1664 | 1405 |
| hardness | raw-complete | 42 | 1549 | 1401 |
| deadness | raw-complete | 26 | 1680 | 1398 |
| praise | raw-complete | 60 | 1679 | 1392 |
| goodness | raw-complete | 56 | 1548 | 1369 |
| counsel | raw-complete | 18 | 1501 | 1349 |
| brokenness | raw-complete | 64 | 1540 | 1348 |
| wickedness | raw-complete | 27 | 1557 | 1320 |
| evil | raw-complete | 44 | 1494 | 1314 |
| justice | raw-complete | 26 | 1587 | 1303 |
| kindness | raw-complete | 33 | 1496 | 1294 |
| consecration | raw-complete | 26 | 1493 | 1238 |
| holiness | raw-complete | 31 | 1564 | 1235 |
| experience | raw-complete | 6 | 1331 | 1233 |
| authority | raw-complete | 38 | 1380 | 1222 |
| obedience | raw-complete | 12 | 1293 | 1199 |
| trust | raw-complete | 37 | 1296 | 1187 |
| distress | raw-complete | 58 | 1310 | 1185 |
| dominion | raw-complete | 26 | 1339 | 1161 |
| faith | raw-complete | 25 | 1332 | 1144 |
| faithfulness | raw-complete | 25 | 1332 | 1144 |
| prayer | raw-complete | 19 | 1225 | 1125 |
| devotion | raw-complete | 27 | 1174 | 1098 |
| appetite | raw-complete | 9 | 1222 | 1056 |
| compassion | raw-complete | 47 | 1227 | 1053 |
| flesh | raw-complete | 16 | 1155 | 1035 |
| wealth | raw-complete | 34 | 1153 | 1013 |
| gladness | raw-complete | 24 | 1217 | 1004 |
| bondage | raw-complete | 13 | 1121 | 979 |
| peace | raw-complete | 43 | 1050 | 952 |
| repentance | raw-complete | 14 | 1057 | 945 |
| rejection | raw-complete | 41 | 986 | 902 |
| intention | raw-complete | 22 | 922 | 866 |
| transgression | raw-complete | 17 | 978 | 853 |
| Soul | raw-complete | 15 | 913 | 825 |
| anointing | raw-complete | 21 | 974 | 818 |
| innocence | raw-complete | 24 | 952 | 799 |
| rebellion | raw-complete | 24 | 825 | 788 |
| salvation | raw-complete | 24 | 845 | 763 |
| guilt | raw-complete | 17 | 914 | 761 |
| prophecy | raw-complete | 9 | 837 | 756 |
| anger | raw-complete | 39 | 917 | 692 |
| mercy | raw-complete | 30 | 795 | 689 |
| rejoicing | raw-complete | 36 | 852 | 666 |
| iniquity | raw-complete | 24 | 726 | 658 |
| corruption | raw-complete | 44 | 719 | 656 |
| dread | raw-complete | 38 | 711 | 656 |
| truthfulness | raw-complete | 24 | 712 | 640 |
| deceit | raw-complete | 46 | 723 | 637 |
| terror | raw-complete | 43 | 723 | 630 |
| wrath | raw-complete | 32 | 838 | 624 |
| courage | raw-complete | 15 | 684 | 608 |
| will | raw-complete | 26 | 599 | 565 |
| grace | raw-complete | 9 | 591 | 557 |
| anguish | raw-complete | 36 | 613 | 556 |
| shame | raw-complete | 40 | 665 | 556 |
| awe | raw-complete | 19 | 616 | 549 |
| joy | raw-complete | 29 | 688 | 534 |
| wisdom | raw-complete | 17 | 631 | 531 |
| forgiveness | raw-complete | 14 | 575 | 521 |
| covenant | raw-complete | 11 | 650 | 519 |
| sorrow | raw-complete | 46 | 577 | 516 |
| craving | raw-complete | 18 | 563 | 497 |
| dignity | raw-complete | 12 | 508 | 466 |
| hope | raw-complete | 33 | 503 | 459 |
| despair | raw-complete | 19 | 477 | 453 |
| weakness | raw-complete | 45 | 481 | 449 |
| righteousness | raw-complete | 11 | 483 | 448 |
| contempt | raw-complete | 51 | 501 | 447 |
| patience | raw-complete | 10 | 475 | 441 |
| comfort | raw-complete | 24 | 463 | 433 |
| grief | raw-complete | 30 | 472 | 431 |
| likeness | raw-complete | 36 | 466 | 416 |
| division | raw-complete | 25 | 459 | 408 |
| defilement | raw-complete | 30 | 487 | 383 |
| insight | raw-complete | 16 | 417 | 381 |
| transformation | raw-complete | 5 | 390 | 374 |
| uprightness | raw-complete | 24 | 391 | 374 |
| indignation | raw-complete | 17 | 403 | 364 |
| weeping | raw-complete | 21 | 417 | 360 |
| foolishness | raw-complete | 37 | 404 | 359 |
| wonder | raw-complete | 25 | 416 | 355 |
| stubbornness | raw-complete | 18 | 397 | 347 |
| memory | raw-complete | 13 | 345 | 329 |
| Incurability | raw-complete | 7 | 313 | 293 |
| imagination | raw-complete | 17 | 318 | 293 |
| unity | raw-complete | 3 | 342 | 290 |
| pride | raw-complete | 32 | 325 | 289 |
| image | raw-complete | 25 | 363 | 284 |
| honesty | raw-complete | 6 | 293 | 278 |
| might | raw-complete | 8 | 285 | 272 |
| perverseness | raw-complete | 24 | 272 | 264 |
| malice | raw-complete | 9 | 282 | 263 |
| purity | raw-complete | 18 | 271 | 246 |
| impurity | raw-complete | 11 | 303 | 243 |
| integrity | raw-complete | 27 | 234 | 227 |
| reconciliation | raw-complete | 3 | 244 | 226 |
| worth | raw-complete | 7 | 245 | 222 |
| abomination | raw-complete | 17 | 235 | 211 |
| hatred | raw-complete | 14 | 227 | 211 |
| fellowship | raw-complete | 9 | 213 | 201 |
| envy | raw-complete | 10 | 223 | 192 |
| groaning | raw-complete | 22 | 207 | 189 |
| strife | raw-complete | 30 | 200 | 184 |
| sincerity | raw-complete | 13 | 187 | 176 |
| boldness | raw-complete | 14 | 178 | 171 |
| whoredom | raw-complete | 12 | 210 | 164 |
| covetousness | raw-complete | 15 | 177 | 162 |
| gratitude | raw-complete | 3 | 170 | 161 |
| gentleness | raw-complete | 18 | 170 | 158 |
| bitterness | raw-complete | 22 | 171 | 154 |
| lust | raw-complete | 17 | 164 | 151 |
| renewal | raw-complete | 16 | 157 | 144 |
| jealousy | raw-complete | 8 | 150 | 139 |
| generosity | raw-complete | 3 | 143 | 127 |
| passion | raw-complete | 11 | 131 | 123 |
| yearning | raw-complete | 9 | 134 | 123 |
| treachery | raw-complete | 10 | 136 | 111 |
| self-control | raw-complete | 17 | 102 | 97 |
| Ruthlessness | raw-complete | 9 | 99 | 95 |
| zeal | raw-complete | 7 | 109 | 94 |
| doubt | raw-complete | 10 | 89 | 85 |
| disobedience | raw-complete | 6 | 77 | 75 |
| idolatry | raw-complete | 5 | 80 | 74 |
| sloth | raw-complete | 8 | 73 | 71 |
| submission | raw-complete | 4 | 69 | 62 |
| humility | raw-complete | 12 | 64 | 59 |
| conscience | raw-complete | 3 | 64 | 58 |
| agony | raw-complete | 11 | 63 | 56 |
| greed | raw-complete | 7 | 55 | 53 |
| anxiety | raw-complete | 12 | 54 | 52 |
| intercession | raw-complete | 4 | 54 | 51 |
| temptation | raw-complete | 6 | 43 | 40 |
| devious | raw-complete | 5 | 36 | 35 |
| unbelief | raw-complete | 3 | 31 | 30 |
| contrition | raw-complete | 5 | 29 | 28 |
| sorcery | raw-complete | 7 | 29 | 25 |
| hypocrisy | raw-complete | 5 | 18 | 17 |
| debauchery | raw-complete | 3 | 14 | 14 |
| ambition | raw-complete | 2 | 10 | 10 |
| character | raw-complete | 3 | 10 | 9 |
| blindness | approved | 0 | 0 | 0 |

Note the OT-only words that read "0" in the 2026-08-09 NT-only report (`contrition`, `might`,
`treachery`) now show real counts (28, 272, 111) — they were never actually empty, only invisible
under the NT-only filter. `blindness` is still genuinely empty (no `word_strong` links at all,
per §2 of the 2026-08-09 report — unchanged).

## 3. Volume distribution — what "all verses that relate to the Strong's" means in practice

Bucketed by verses-touched (whole Bible), 178 words:

| verses touched | word count |
| --- | --- |
| 0 | 1 |
| 1–9 | 1 |
| 10–49 | 8 |
| 50–99 | 14 |
| 100–499 | 56 |
| 500–999 | 34 |
| 1000–1999 | 40 |
| 2000+ | 24 |

- **Median 565 verses/word, mean 1,102** — the distribution is heavily right-skewed: a handful of
  broad-scope words (`reasoning`, `calling`, `being`, `purpose`, `endurance` — all 5,000–10,000+
  verses) pull the mean well above the median. Most words (110 of 178, the 100–999 band) sit in a
  workable few-hundred-verse range; a smaller tail (64 words, the 1000+ bands) does not.
- **`blessing`** (the word this design is being tested against) sits at **1,628 verses** whole
  Bible — comfortably mid-tail, not a worst case, but still far too many for one file per verse
  and large for one flat file.

## 4. What each strategy actually produces, using real counts

**(a) One file per (registry word, verse) — rejected.** 196,144 files total; the single word
`reasoning` alone would need 10,128 separate files. No plausible governance reason to generate
this many near-duplicate files (`governance.oneoff_report_dir` is a flat single directory, not
designed for this volume), and it defeats the stated purpose — "get a feeling for the result" —
by scattering it across more files than could be browsed.

**(b) One flat file per registry word, every matched verse inline — works for most words, breaks
at the top of the distribution.** For `blessing` (1,628 verses) a single file is plausible in
principle but already long; for `reasoning` (10,128 verses) or `calling` (9,080) a single
Markdown file at even a conservative ~0.3–0.5 KB per verse-card (verse text + inline annotation +
detail rows, scaled from the Eph 1:3 sample) lands in the **3–5 MB / single-file range** — not
readable as "a feel for the result," the opposite of the stated goal, and this is before adding
the fuller per-span sense breakdown from open-question 3 (exact-variant senses only, still
non-trivial length per match).

**(c) Chunk by book, one file per (registry word, book).** Reduces the worst case but doesn't
solve it: `reasoning` touches all 66 books, with its single largest book (Jer) alone at 700
verses; `blessing` touches 62 books, largest (Luke) at 287 verses. Better than (b) but still
produces a large *number* of files per top word (up to 66), and the top-book chunk for `reasoning`
is still a 700-verse file.

**(d) On-demand, scoped to a requested passage/range — matches the precedent already in this
codebase.** `report.verse_lexical` (`cfg_step`, `word-package: verse-lexical`) already works this
way: "on-demand MD report... per book/passage range... Requires verse_lexical.build to have
already run for this exact range" — nothing is generated speculatively for a whole book or whole
registry word up front. The same pattern fits this new report directly: build it for a chosen
registry word **and** a chosen book/chapter/verse-range, not the whole registry word's full verse
set in one call. `blessing` in Ephesians (a handful of verses) is a normal, fast, readable request
under this model; `blessing`'s full 1,628-verse footprint is only ever materialised if explicitly
requested a range at a time — the researcher controls the scope per run, same as the existing
tool.

## Recommendation

**(d)**, matching `report.verse_lexical`'s existing on-demand-by-range convention, is the only one
of the four that doesn't either explode file count (a), produce unreadable multi-MB files for the
top ~15% of the registry (b), or just push the same problem down one level (c). A per-registry
**index** (word → total verses touched, books touched, largest book) — essentially §2/§3 of this
report, kept live — would tell you up front what a full run for any given word would cost before
you request it.

Not decided here: whether to build this as a genuinely new `cfg_step` (own work package) or as a
scope parameter on the existing `report.verse_lexical`/`report.word_registry_span` steps — a design
question for you, not inferred.
