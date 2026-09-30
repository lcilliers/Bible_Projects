# Corpus-wide preliminary keyword allocation (P1, all clusters)

> READ-ONLY (`scripts/_assess_corpus_keyword_map.py`). Validated P1 method (whole-word + filters + self-check) over every active characteristic term, all 46 clusters. **Preliminary** — keyword source-scope not yet normalised; concatenation/glue-word artifacts flagged `suspect`. No DB writes. Full per-term map: `wa-corpus-keyword-map-v1-20260608.csv`.

**1660 terms · 12059 keyword-allocations · self-check PASS 1660/1660 · 21 terms with suspect tokens (concatenation).**

## Per-cluster keyword allocation

| Cluster | terms | total kw | distinct vocab | avg kw/term | self-check fail | suspect |
|---|---|---|---|---|---|---|
| M01 (Fear) | 85 | 396 | 182 | 4.7 | 0 | 1 |
| M02 (Anger) | 47 | 284 | 170 | 6.0 | 0 | 0 |
| M03 (Grief) | 80 | 439 | 225 | 5.5 | 0 | 0 |
| M04 (Joy) | 58 | 273 | 163 | 4.7 | 0 | 1 |
| M05 (Love) | 91 | 694 | 459 | 7.6 | 0 | 2 |
| M06 (Hate) | 34 | 116 | 84 | 3.4 | 0 | 0 |
| M07 (Shame) | 33 | 203 | 136 | 6.2 | 0 | 0 |
| M08 (Pride) | 47 | 241 | 150 | 5.1 | 0 | 1 |
| M09 (Humility) | 17 | 131 | 106 | 7.7 | 0 | 0 |
| M10 (Sin) | 64 | 359 | 197 | 5.6 | 0 | 3 |
| M10b (Wickedness) | 17 | 138 | 96 | 8.1 | 0 | 1 |
| M10c (Defilement) | 8 | 41 | 31 | 5.1 | 0 | 0 |
| M11 (Repentance) | 15 | 240 | 139 | 16.0 | 0 | 0 |
| M12 (Purity) | 48 | 477 | 227 | 9.9 | 0 | 1 |
| M13 (Truth) | 26 | 196 | 122 | 7.5 | 0 | 1 |
| M14 (Deceit) | 42 | 234 | 174 | 5.6 | 0 | 2 |
| M15 (Wisdom) | 85 | 700 | 390 | 8.2 | 0 | 1 |
| M16 (Folly) | 30 | 147 | 102 | 4.9 | 0 | 1 |
| M17 (Counsel) | 17 | 137 | 111 | 8.1 | 0 | 1 |
| M18 (Hope) | 28 | 166 | 107 | 5.9 | 0 | 0 |
| M19 (Trust) | 31 | 173 | 133 | 5.6 | 0 | 0 |
| M20 (Doubt) | 15 | 73 | 50 | 4.9 | 0 | 0 |
| M21 (Prayer) | 32 | 241 | 177 | 7.5 | 0 | 0 |
| M22 (Praise) | 46 | 303 | 214 | 6.6 | 0 | 0 |
| M23 (Strength) | 120 | 1055 | 506 | 8.8 | 0 | 0 |
| M24 (Weakness) | 76 | 452 | 277 | 5.9 | 0 | 0 |
| M25 (Life) | 15 | 197 | 110 | 13.1 | 0 | 0 |
| M26 (Righteousness) | 42 | 369 | 231 | 8.8 | 0 | 1 |
| M27 (Evil) | 19 | 144 | 120 | 7.6 | 0 | 0 |
| M28 (Envy) | 40 | 220 | 165 | 5.5 | 0 | 0 |
| M29 (Desire) | 12 | 84 | 70 | 7.0 | 0 | 0 |
| M30 (Obedience) | 29 | 301 | 132 | 10.4 | 0 | 0 |
| M31 (Faith) | 13 | 186 | 126 | 14.3 | 0 | 1 |
| M33 (Peace) | 44 | 363 | 194 | 8.2 | 0 | 0 |
| M34 (Perseverance) | 22 | 235 | 195 | 10.7 | 0 | 2 |
| M35 (Testing) | 25 | 329 | 167 | 13.2 | 0 | 0 |
| M36 (Service) | 23 | 183 | 82 | 8.0 | 0 | 0 |
| M37 (Calling) | 22 | 255 | 137 | 11.6 | 0 | 0 |
| M38 (Salvation) | 13 | 123 | 93 | 9.5 | 0 | 0 |
| M39 (Blessing) | 16 | 162 | 119 | 10.1 | 0 | 0 |
| M41 (Remembrance) | 33 | 341 | 131 | 10.3 | 0 | 0 |
| M42 (Speech) | 34 | 155 | 111 | 4.6 | 0 | 0 |
| M43 (Prophecy) | 13 | 91 | 81 | 7.0 | 0 | 1 |
| M44 (Relational) | 17 | 82 | 73 | 4.8 | 0 | 0 |
| M45 (Transformation) | 14 | 172 | 137 | 12.3 | 0 | 0 |
| M46 (Abundance) | 22 | 158 | 119 | 7.2 | 0 | 0 |

_Self-check fails = hyphen/edge tokens (rare); suspect = over-long concatenations to clean in the source-normalisation step. Both are surfaced, not hidden._