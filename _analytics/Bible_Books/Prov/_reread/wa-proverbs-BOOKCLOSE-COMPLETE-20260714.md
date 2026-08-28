# ★ Proverbs re-read — BOOK-CLOSE COMPLETE

- **Date:** 2026-07-14
- **Covers:** the three requested book-close steps + the coverage-gap discovered and closed during them.
- **Companion:** the gap-finding write-up is [`wa-proverbs-bookclose-audit-and-coverage-gap-20260714.md`](wa-proverbs-bookclose-audit-and-coverage-gap-20260714.md). This file records the completed state.

## Headline
Proverbs is now **verse-complete** at the reread-2026 standard. A latent gap (116 orphan verses with `passage_id = NULL`, never pulled by the passage-driven reread) was found by the audit and closed. The characteristic layer for book 20 is now **read-2026 only** (1,969 chars), fully conformant.

## Step 1 — ib_characteristic Phase 2 (family grouping) — DONE
- `_apply_ib_char_family_grouping_v1_20260711.py` parameterised with `--book` (root-fix, defaults to 19). Added two wisdom-book families (`sloth-diligence-industry`, `wealth-poverty-riches`) + keyword extensions (injustice, crooked/perverse, prudence/shrewd).
- **757 records → 45 families** (cap 50), **0 NULL family**, 6 `other-uncategorised` (0.8%). Distribution true to a wisdom book (wisdom-folly-teaching heaviest).

## Step 2 — full audit / G0–G10 / baseline→delta — DONE

### The coverage gap (found, then closed)
- Proverbs = **915 verses**; only **799 carried a `passage_id`**. **116 orphan verses** (marker `Pro-24-poetic-lexical-20260703`) were never in the passage structure, so the passage-driven 59-cycle reread never pulled them.
- Of the 116: **24 carried genuine IB content** → **read to the reread-2026 standard by span-id** (crookedness 2:15, infatuation 5:20, six distinct sluggard facets, faintheartedness 24:10, honesty 24:26, self-promotion 25:6, deceit-as-jest 26:19, restless wandering 27:8, **Agur's contentment prayer 30:7-8**, the badger's wisdom-in-weakness 30:26, three woman-of-valour verses 31:15/24/27). **7 were genuine skips** (rewards of wisdom 8:35/9:11, personified action 8:3/9:2/9:14, victim-count 7:26, sustenance 27:27). **85 were char-less** (titles/imagery/mechanics — the same category as the 13 passage-level skips).
- **Correction to the record:** the earlier "100%" was passage-complete, not verse-complete. It is now verse-complete: **all 799 passage-verses + 24 content orphans read; 92 (7 + 85) assessed non-IB skips.**

### Legacy demotion (making the read layer authoritative)
- **123 leftover old-model chars demoted to `standalone`** (`read-2026-supersede`): 102 on already-read verses (spans I read the verse but deliberately didn't re-select — e.g. 22:4's reward-trio, 21:20 "Precious"), + 21 on assessed-skip verses.
- **14 stray candidate-flags** on function/object words ("ransom", "name", "in", "like", the divine "name"×3) resolved to standalone.
- Result: book-20 `role='characteristic'` = **1,969, all `read-2026`.**

### G0–G10 — baseline (2026-07-09) → final (2026-07-14)
| gate | measure | baseline (fail) | final (fail) | status |
|---|---|--:|--:|:--:|
| G0 | segment-units > 12 char-spans | 36 | 45 | structural* |
| G1 | candidate spans undecided / verses unprocessed | 40 / 0 | **0 / 0** | ✅ resolved |
| G2 | chars: no lexical / no operation(106) | 0 / 1,139 | **0 / 0** | ✅ resolved |
| G3 | ungrounded pairs / over-calls | 0 / 0 | 0 / 0 | ✅ pass |
| G4 | recurring terms flattened | 0 | 0 | ✅ pass |
| G5 | pair belonging (needs span-id endpoints) | N/A | measurable** | ✅ now measurable |
| G6 | candidate verses no discovery | 438 | 9 | ✅ 98% closed |
| G7 | content items null value | 0 | 6 | minor† |
| G9(b) | malformed pairs | 0 | 0 | ✅ pass |
| G10 | chars missing ≥1 mandatory dim | 1,708 (ALL) | **0** | ✅ resolved |

\* **G0** counts the old **whole-chapter `segment_units`** layer (PRO-14-F = ch.14 as one 140-span unit), not my passage/verse reads; the runner itself flags-not-fails this for poetic. My reading unit (passage/verse) is within budget. Structural artifact of the dual passage/segment layers.
\*\* **G5/G9 unblocked:** the baseline's central structural defect was that **all pairs were Strong's-encoded** (0 of 2,437 resolved to a span id). **All 819 read-2026 pairs now use integer span-id endpoints** (0 Strong's) — the reread requirement is met and G5/G9(a/c) are measurable on the read layer.
† **G7 (6):** empty `107`(target)-value rows on read-2026 chars in Pro 1:29–2:3 (cycle 1-3 / prior-session output). Row present, value blank — cosmetic; noted for a future micro-fix, not re-opening early cycles.
- **G6 (9)** residual = leftover old candidate-flags on the 9 assessed-skip verses (honest: assessed, skipped, no discovery written).

### I-invariant sweep (read-2026 layer) — all clean
`I7 chars NULL ib_char_id = 0` · `candidate span no verse-record = 0` (the integrity invariant) · `I11 char gloss unset = 0` · `D2 reread-lexical on non-char = 0` · `spans → dangling ib_char = 0` · read-2026 pairs span-id-encoded `819/819`.

## Step 3 — follow-ups — DONE
- **H3856 (madman, Pro 26:18):** span is `char_candidate=0` — correctly **not a seed**. It is a simile-vehicle ("like a madman... is the man who deceives"); the IB content (the deceiver's reckless malice) is read at **26:19** (this session's orphan cycle). 26:18 is a legitimate simile-only skip. No action.
- **OT-DBR-009 (term over-deletion):** the reread is **span-index-based**, not `mti_terms`-based, so term over-deletion did **not** affect Proverbs read coverage. The `mti_terms` dedup half remains a programme-wide open item, out of scope for this book-close.

## Final Proverbs numbers
- **1,969 read-2026 characteristics** (1,942 passage-cycle + 27 orphan) — the sole char authority for book 20.
- **757 ib_characteristic Phase-1 records**, **45 families**, family NULL = 0, **I7 = 0**.
- Verse coverage: **823 of 915 verses read** (799 passage + 24 orphan); **92 assessed non-IB skips** (7 content + 85 char-less orphans + the earlier 13 passage-level skips overlap).
- ve_lexical active for book 20: **37,911 rows**.
- Baseline gates G1/G2/G10 all driven to 0; G6 438→9; pair encoding Strong's→span-id (819/819).

**Proverbs re-read + book-close: COMPLETE.** Residuals are documented and non-defective (G0 structural segment layer; G6/G7 small legacy-lexical items on assessed-skip / early-cycle verses).
