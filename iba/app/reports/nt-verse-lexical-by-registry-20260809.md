# NT verse_lexical summarised by word_registry — 2026-08-09

Follow-on to [`nt-verse-lexical-analysis-20260809.md`](nt-verse-lexical-analysis-20260809.md). That report covered `verse_lexical` on its own terms (coverage, role split, resolution status). This one attributes the same NT `verse_lexical` rows to the **178 active `word_registry` entries**, via the chain:

```
word_registry (id, word)
  └─ word_strong (word_id → strong, exact code incl. suffix, e.g. H0430G)
       └─ verse_lexical.strong  (exact match — no LIKE/prefix logic needed;
                                  word_strong already stores full suffixed codes)
            └─ verse (osisId → NT book filter)
```

The join is an exact string match on `strong` — `word_strong.strong` already carries suffix letters (e.g. `H0205G`) in the same form `verse_lexical.strong` uses, so no base/suffix reconciliation was needed.

## 1. Headline

| Metric | Value |
| --- | --- |
| Active `word_registry` entries | 178 |
| Active `word_strong` links (registry→Strong's) | 4,796 |
| Distinct Strong's codes linked to ≥1 registry word | 3,457 |
| Distinct Strong's codes appearing in NT `verse_lexical` | 5,399 |
| — of those, linked to a registry word | 1,264 (23.4%) |
| — of those, **not** linked to any registry word | 4,135 (76.6%) |
| NT `verse_lexical` rows (codes) attributable to ≥1 registry word | 30,854 / 111,410 (27.7%) |
| NT verses touched by ≥1 registry word | 7,590 / 7,605 (99.8%) |

Reading this correctly: the low code-level attribution (27.7%) is not a data-quality problem — the registry is a **curated set of ~178 inner-life vocabulary words**, not an exhaustive NT lexicon. Splitting by role makes the shape clear:

| Role | Covered by a registry word | Uncovered |
| --- | --- | --- |
| `content` (81,509 total) | 27,282 (33.5%) | 54,227 (66.5%) |
| `function` (29,901 total) | 3,572 (12.0%) | 26,329 (88.0%) |

Even restricted to content-bearing codes, two-thirds of NT lexical items sit outside the current registry vocabulary — expected for a targeted study, and the reason 99.8% of NT verses still get *some* registry-word hit is that the 178 words are broadly distributed, not that they cover most of each verse's content.

880 Strong's codes are linked to **more than one** registry word (synonym/overlap cases, e.g. shared roots across near-synonyms) — this is why the per-registry code counts below sum to more than the 30,854 distinct-code figure (45,340) if you add them up; a single verse_lexical row can legitimately count under two or more registry words.

## 2. Structural gaps found

| Word (id) | Issue |
| --- | --- |
| `blindness` (183, status `approved`) | **Zero `word_strong` links at all** — the only registry entry with no Strong's attached. Cannot appear in any lexical summary until linked. |
| `contrition` (Strong's: H1792, H1793A, H1793B, H1794, H5223) | Linked, but all 5 Strong's are Hebrew-only — 0 NT hits is correct, not a gap (OT-only word). |
| `might` (H1369, H1370, H3581A, H3581B, H5797, H6978, H8632A, H8632B) | Same — all-Hebrew, 0 NT hits is expected. |
| `treachery` (H0899A, H0900, H0901, H3585, H4603, H4604, H4820, H7195, H8649A, H8649B) | Same — all-Hebrew, 0 NT hits is expected. |

Only `blindness` is a genuine gap (missing linkage); the other three "zero NT" cases are legitimate — they're OT-vocabulary words with no Greek counterpart registered yet.

One outlier worth a sanity check rather than a fix: **`being`** carries **444 distinct Strong's** — far above the next-highest (`longing` and `strength` at 78, `power` at 82). That's plausible if "being" was scoped as a broad existence/ontology category, but it's an order of magnitude above every other registry word and worth you confirming it's intentional scope, not an over-broad tagging pass.

## 3. Full per-registry NT breakdown (178 words, sorted by NT codes)

| Word | Status | Strong's linked | NT codes | NT verses |
| --- | --- | --- | --- | --- |
| being | raw-complete | 444 | 4606 | 3468 |
| calling | raw-complete | 49 | 3630 | 2889 |
| reasoning | raw-complete | 39 | 1929 | 1644 |
| purpose | raw-complete | 39 | 1664 | 1390 |
| fear | raw-complete | 62 | 1501 | 1285 |
| boastfulness | raw-complete | 31 | 1341 | 1245 |
| meaning | raw-complete | 16 | 1322 | 1229 |
| longing | raw-complete | 78 | 1213 | 1052 |
| blessing | raw-complete | 20 | 1192 | 1092 |
| understanding | raw-complete | 47 | 1057 | 911 |
| desire | raw-complete | 62 | 759 | 678 |
| love | raw-complete | 52 | 710 | 585 |
| spirit | raw-complete | 23 | 709 | 553 |
| holiness | raw-complete | 31 | 686 | 530 |
| power | raw-complete | 82 | 656 | 561 |
| faith | raw-complete | 25 | 630 | 545 |
| faithfulness | raw-complete | 25 | 630 | 545 |
| yielding | raw-complete | 29 | 604 | 527 |
| trust | raw-complete | 37 | 584 | 525 |
| anointing | raw-complete | 21 | 551 | 517 |
| testimony | raw-complete | 22 | 550 | 493 |
| endurance | raw-complete | 47 | 512 | 448 |
| listen | raw-complete | 26 | 480 | 438 |
| mind | raw-complete | 58 | 468 | 402 |
| name | raw-complete | 19 | 467 | 413 |
| strength | raw-complete | 78 | 439 | 380 |
| praise | raw-complete | 60 | 437 | 368 |
| deadness | raw-complete | 26 | 420 | 359 |
| thought | raw-complete | 47 | 411 | 368 |
| the afflicted | raw-complete | 76 | 388 | 377 |
| worship | raw-complete | 42 | 376 | 336 |
| consecration | raw-complete | 26 | 375 | 344 |
| knowledge | raw-complete | 27 | 360 | 348 |
| goodness | raw-complete | 56 | 351 | 306 |
| sin | raw-complete | 48 | 348 | 296 |
| dominion | raw-complete | 26 | 347 | 310 |
| unity | raw-complete | 3 | 342 | 290 |
| will | raw-complete | 26 | 329 | 310 |
| craving | raw-complete | 18 | 305 | 260 |
| authority | raw-complete | 38 | 294 | 265 |
| brokenness | raw-complete | 64 | 271 | 250 |
| Incurability | raw-complete | 7 | 253 | 238 |
| kindness | raw-complete | 33 | 250 | 221 |
| heart | raw-complete | 38 | 239 | 219 |
| forgiveness | raw-complete | 14 | 238 | 215 |
| condemnation | raw-complete | 22 | 233 | 197 |
| guilt | raw-complete | 17 | 227 | 203 |
| rejoicing | raw-complete | 36 | 226 | 188 |
| evil | raw-complete | 44 | 223 | 201 |
| rejection | raw-complete | 41 | 212 | 187 |
| flesh | raw-complete | 16 | 206 | 172 |
| intention | raw-complete | 22 | 203 | 193 |
| salvation | raw-complete | 24 | 201 | 188 |
| truthfulness | raw-complete | 24 | 201 | 182 |
| joy | raw-complete | 29 | 196 | 166 |
| seeking | raw-complete | 30 | 195 | 189 |
| wonder | raw-complete | 25 | 195 | 161 |
| delight | raw-complete | 56 | 186 | 168 |
| grace | raw-complete | 9 | 181 | 167 |
| wealth | raw-complete | 34 | 181 | 170 |
| prayer | raw-complete | 19 | 174 | 157 |
| dignity | raw-complete | 12 | 173 | 156 |
| gratitude | raw-complete | 3 | 170 | 161 |
| gladness | raw-complete | 24 | 168 | 142 |
| devotion | raw-complete | 27 | 159 | 152 |
| comfort | raw-complete | 24 | 158 | 143 |
| justice | raw-complete | 26 | 157 | 149 |
| terror | raw-complete | 43 | 146 | 136 |
| peace | raw-complete | 43 | 144 | 134 |
| righteousness | raw-complete | 11 | 142 | 131 |
| sincerity | raw-complete | 13 | 141 | 130 |
| envy | raw-complete | 10 | 139 | 122 |
| likeness | raw-complete | 36 | 138 | 126 |
| distress | raw-complete | 58 | 136 | 116 |
| imagination | raw-complete | 17 | 125 | 123 |
| surrender | raw-complete | 10 | 125 | 117 |
| passion | raw-complete | 11 | 124 | 116 |
| innocence | raw-complete | 24 | 123 | 113 |
| compassion | raw-complete | 47 | 115 | 104 |
| slander | raw-complete | 26 | 114 | 101 |
| generosity | raw-complete | 3 | 109 | 98 |
| experience | raw-complete | 6 | 108 | 104 |
| weakness | raw-complete | 45 | 108 | 98 |
| Soul | raw-complete | 15 | 103 | 93 |
| obedience | raw-complete | 12 | 97 | 87 |
| hope | raw-complete | 33 | 94 | 86 |
| discernment | raw-complete | 26 | 90 | 82 |
| covetousness | raw-complete | 15 | 87 | 80 |
| patience | raw-complete | 10 | 87 | 81 |
| indignation | raw-complete | 17 | 84 | 73 |
| mercy | raw-complete | 30 | 83 | 74 |
| pride | raw-complete | 32 | 82 | 72 |
| Cursing | raw-complete | 29 | 80 | 75 |
| doubt | raw-complete | 10 | 77 | 73 |
| foolishness | raw-complete | 37 | 77 | 73 |
| integrity | raw-complete | 27 | 77 | 75 |
| wisdom | raw-complete | 17 | 75 | 67 |
| hardness | raw-complete | 42 | 73 | 70 |
| mourning | raw-complete | 47 | 73 | 50 |
| boldness | raw-complete | 14 | 71 | 67 |
| anger | raw-complete | 39 | 70 | 60 |
| deceit | raw-complete | 46 | 70 | 65 |
| grief | raw-complete | 30 | 66 | 54 |
| impurity | raw-complete | 11 | 66 | 56 |
| anguish | raw-complete | 36 | 65 | 59 |
| corruption | raw-complete | 44 | 65 | 59 |
| shame | raw-complete | 40 | 65 | 63 |
| lust | raw-complete | 17 | 64 | 57 |
| repentance | raw-complete | 14 | 64 | 58 |
| iniquity | raw-complete | 24 | 63 | 57 |
| sorrow | raw-complete | 46 | 63 | 53 |
| contentment | raw-complete | 26 | 62 | 60 |
| insight | raw-complete | 16 | 62 | 58 |
| awe | raw-complete | 19 | 59 | 56 |
| appetite | raw-complete | 9 | 57 | 56 |
| wrath | raw-complete | 32 | 57 | 49 |
| contempt | raw-complete | 51 | 56 | 53 |
| worth | raw-complete | 7 | 54 | 52 |
| bondage | raw-complete | 13 | 53 | 50 |
| transgression | raw-complete | 17 | 53 | 48 |
| weeping | raw-complete | 21 | 50 | 43 |
| defilement | raw-complete | 30 | 49 | 40 |
| prophecy | raw-complete | 9 | 49 | 48 |
| covenant | raw-complete | 11 | 46 | 35 |
| hatred | raw-complete | 14 | 46 | 42 |
| strife | raw-complete | 30 | 45 | 41 |
| submission | raw-complete | 4 | 44 | 37 |
| wickedness | raw-complete | 27 | 40 | 35 |
| temptation | raw-complete | 6 | 39 | 36 |
| humility | raw-complete | 12 | 38 | 34 |
| rebellion | raw-complete | 24 | 37 | 37 |
| gentleness | raw-complete | 18 | 36 | 31 |
| division | raw-complete | 25 | 35 | 32 |
| courage | raw-complete | 15 | 34 | 32 |
| conscience | raw-complete | 3 | 33 | 32 |
| counsel | raw-complete | 18 | 33 | 31 |
| fellowship | raw-complete | 9 | 33 | 30 |
| disobedience | raw-complete | 6 | 32 | 31 |
| image | raw-complete | 25 | 32 | 24 |
| unbelief | raw-complete | 3 | 31 | 30 |
| zeal | raw-complete | 7 | 31 | 30 |
| whoredom | raw-complete | 12 | 30 | 27 |
| uprightness | raw-complete | 24 | 28 | 28 |
| self-control | raw-complete | 17 | 25 | 23 |
| purity | raw-complete | 18 | 23 | 22 |
| jealousy | raw-complete | 8 | 21 | 21 |
| greed | raw-complete | 7 | 20 | 20 |
| malice | raw-complete | 9 | 19 | 16 |
| dread | raw-complete | 38 | 17 | 17 |
| groaning | raw-complete | 22 | 15 | 15 |
| debauchery | raw-complete | 3 | 14 | 14 |
| agony | raw-complete | 11 | 13 | 13 |
| hypocrisy | raw-complete | 5 | 13 | 12 |
| abomination | raw-complete | 17 | 12 | 12 |
| anxiety | raw-complete | 12 | 12 | 12 |
| memory | raw-complete | 13 | 12 | 12 |
| perverseness | raw-complete | 24 | 12 | 11 |
| ambition | raw-complete | 2 | 10 | 10 |
| bitterness | raw-complete | 22 | 10 | 10 |
| meditation | raw-complete | 21 | 10 | 10 |
| renewal | raw-complete | 16 | 9 | 8 |
| transformation | raw-complete | 5 | 9 | 9 |
| yearning | raw-complete | 9 | 9 | 9 |
| character | raw-complete | 3 | 8 | 7 |
| intercession | raw-complete | 4 | 8 | 8 |
| stubbornness | raw-complete | 18 | 7 | 7 |
| reconciliation | raw-complete | 3 | 6 | 6 |
| sorcery | raw-complete | 7 | 6 | 6 |
| idolatry | raw-complete | 5 | 5 | 5 |
| sloth | raw-complete | 8 | 5 | 5 |
| despair | raw-complete | 19 | 3 | 3 |
| honesty | raw-complete | 6 | 3 | 3 |
| Ruthlessness | raw-complete | 9 | 2 | 2 |
| devious | raw-complete | 5 | 1 | 1 |
| blindness | approved | 0 | 0 | 0 |
| contrition | raw-complete | 5 | 0 | 0 |
| might | raw-complete | 8 | 0 | 0 |
| treachery | raw-complete | 10 | 0 | 0 |

## 4. Not investigated here

- Which registry words are strong in the OT but thin/absent in the NT (would need the same join against OT `verse_lexical`, currently only 6 books built there — a partial comparison, not decided to run without you confirming it's wanted).
- Whether `being`'s 444-Strong's scope is deliberate — flagged in §2, not resolved.
- Whether the 4,135 NT Strong's codes with no registry link represent words that *should* eventually get a registry entry, or are legitimately out of scope for this study — that's a scope judgement, not a data question, and belongs to you.
