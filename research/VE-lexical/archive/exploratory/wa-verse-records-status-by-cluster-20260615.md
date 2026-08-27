# Verse-records status by cluster — lexical/meaning columns (2026-06-15)

> Active `wa_verse_records` per cluster. **morph/stem/span** = the bedrock lexical columns on the record; **vc** = has an analytic `verse_context` row; **VE-analysed** = the term-in-verse has VE analysis (distinct `verse_context` with rows in `ve_lexical`).

| cluster | active | morph | stem | span=1 | mti-linked | has vc | VE-analysed |
|---|---|---|---|---|---|---|---|
| T2 | 23,666 | 99% | 5,049 | 100% | 100% | 10,146 | 1,176 |
| M23 | 2,588 | 99% | 798 | 100% | 100% | 1,582 | 1,574 |
| M15 | 1,713 | 100% | 890 | 100% | 100% | 1,713 | 1,734 |
| M26 | 1,707 | 100% | 350 | 100% | 100% | 1,426 | 1,075 |
| M22 | 1,668 | 100% | 434 | 100% | 100% | 1,067 | 1,029 |
| M47 | 1,584 | 100% | 0 | 100% | 100% | 1,311 | 276 |
| M05 | 1,569 | 99% | 200 | 100% | 100% | 1,542 | 1,886 |
| M10 | 1,520 | 100% | 392 | 100% | 100% | 1,487 | 1,487 |
| M41 | 1,487 | 100% | 1,246 | 100% | 100% | 1,163 | 1,165 |
| M25 | 1,395 | 100% | 369 | 100% | 100% | 1,319 | 1,208 |
| M04 | 1,236 | 99% | 412 | 99% | 100% | 1,236 | 1,235 |
| M37 | 1,107 | 100% | 923 | 100% | 100% | 1,063 | 1,063 |
| M01 | 1,044 | 100% | 558 | 100% | 100% | 1,036 | 1,036 |
| M44 | 1,006 | 100% | 402 | 100% | 100% | 716 | 486 |
| M03 | 970 | 100% | 228 | 100% | 100% | 936 | 940 |
| M12 | 960 | 100% | 526 | 100% | 100% | 741 | 741 |
| M30 | 896 | 100% | 813 | 100% | 100% | 648 | 643 |
| M24 | 838 | 100% | 346 | 100% | 100% | 626 | 631 |
| M39 | 744 | 100% | 505 | 100% | 100% | 743 | 743 |
| M02 | 703 | 100% | 267 | 100% | 100% | 703 | 703 |
| M13 | 699 | 100% | 145 | 100% | 100% | 591 | 593 |
| M08 | 689 | 100% | 258 | 100% | 100% | 678 | 679 |
| M33 | 672 | 100% | 266 | 100% | 100% | 545 | 545 |
| M36 | 621 | 100% | 308 | 100% | 100% | 360 | 362 |
| M28 | 573 | 100% | 159 | 100% | 100% | 373 | 374 |
| M27 | 558 | 100% | 259 | 100% | 100% | 392 | 392 |
| M21 | 545 | 99% | 167 | 100% | 100% | 508 | 512 |
| M10b | 537 | 100% | 0 | 100% | 100% | 537 | 537 |
| M42 | 534 | 100% | 327 | 100% | 100% | 422 | 424 |
| M06 | 437 | 100% | 262 | 100% | 100% | 437 | 448 |
| M14 | 393 | 100% | 63 | 100% | 100% | 367 | 372 |
| M07 | 375 | 100% | 198 | 100% | 100% | 374 | 374 |
| M19 | 366 | 100% | 184 | 100% | 100% | 329 | 329 |
| M38 | 355 | 99% | 140 | 100% | 100% | 355 | 355 |
| M11 | 343 | 100% | 183 | 100% | 100% | 289 | 289 |
| M31 | 320 | 100% | 0 | 100% | 100% | 311 | 313 |
| M29 | 297 | 100% | 44 | 100% | 100% | 296 | 296 |
| M46 | 294 | 100% | 34 | 100% | 100% | 291 | 291 |
| M17 | 280 | 100% | 49 | 100% | 100% | 252 | 256 |
| M18 | 276 | 100% | 93 | 100% | 100% | 267 | 271 |
| M10c | 275 | 100% | 128 | 100% | 100% | 275 | 275 |
| M34 | 229 | 96% | 13 | 100% | 100% | 170 | 169 |
| M35 | 208 | 100% | 0 | 100% | 100% | 181 | 181 |
| M45 | 182 | 100% | 77 | 100% | 100% | 182 | 182 |
| M16 | 165 | 100% | 25 | 100% | 100% | 165 | 165 |
| M43 | 144 | 100% | 0 | 100% | 100% | 89 | 89 |
| M09 | 131 | 100% | 33 | 100% | 100% | 131 | 131 |
| M20 | 67 | 100% | 20 | 100% | 100% | 67 | 68 |
| **TOTAL** | **58,966** | 99% | 18,143 | 99% | 100% | 40,438 | **30,103** |

## Reading notes

- **Bedrock columns are clean everywhere.** morph_code 99%, span_strong_match=1 99%, mti-linked 100%. The lexical *truth on the record* (mode/morph, span, language, link) is solid and is **not** part of any backtrack — these are per-occurrence facts, not derived.
- **stem** is populated only where the morph is a verb (binyan/conjugation); a low or zero stem count (e.g. M47, M10b, M31, M35, M43 = 0) means those clusters are noun/adjective-dominant, not a gap.
- **has vc vs VE-analysed** — the gap between the two is where a term-in-verse has a `verse_context` row but no `ve_lexical` analysis yet. Largest absolute gaps are **T2** (10,146 vc → 1,176 analysed; correct — T2 is a reference, not analysed standalone) and **M47** (1,311 → 276). The remaining M-clusters track close to 1:1.
- The `ve_lexical` *values* themselves (sense, type, faculty, etc.) are the layer under review — they are **not** assessed as correct/incorrect here; this table only reports presence of an analysis row, not its quality. Value-level validation is the step-wise work to follow.

*Source: read-only query over active `wa_verse_records` joined to `mti_terms.cluster_code`; `verse_context` and `ve_lexical` coverage counted via `verse_record_id` / `verse_context_id`. Generated 2026-06-15.*
