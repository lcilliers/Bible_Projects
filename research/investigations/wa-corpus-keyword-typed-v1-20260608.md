# Corpus keyword map v2 — typed + glue-filtered

> READ-ONLY (`scripts/_assess_corpus_keyword_typed.py`). Each term: its **thing-type** (ACTION/STATUS/QUALITY, dominant morph POS) + keywords with **glue + lexicon-prose removed**. No DB writes. Full map: `wa-corpus-keyword-typed-v1-20260608.csv`.

**1660 terms · 10802 keywords (glue-filtered) · 6.5 avg/term.**

## Thing-type distribution

| type | terms | % |
|---|---|---|
| STATUS | 756 | 46% |
| ACTION | 566 | 34% |
| QUALITY | 301 | 18% |
| — | 37 | 2% |

## Signature keywords BY TYPE (does each type read differently?)

- **ACTION**: strong, mind, desire, god, away, think, cry, self, consider, afraid, fear, prevail, grow, strengthen, speak, wait, power, treat, praise, utter
- **STATUS**: god, terror, strength, mind, power, distress, thought, purpose, sorrow, desire, sin, fear, object, love, pain, gift, pride, praise, human, joy
- **QUALITY**: strong, mighty, god, innocent, evil, loving, pure, right, free, rich, compassionate, mind, pious, holy, proud, sound, foolish, wise, strength, humble

## Per-cluster type mix

| Cluster | ACTION | STATUS | QUALITY | lean |
|---|---|---|---|---|
| M01 (Fear) | 22 | 48 | 15 | STATUS |
| M02 (Anger) | 15 | 22 | 10 | STATUS |
| M03 (Grief) | 24 | 49 | 7 | STATUS |
| M04 (Joy) | 22 | 26 | 10 | STATUS |
| M05 (Love) | 25 | 36 | 29 | STATUS |
| M06 (Hate) | 12 | 16 | 6 | STATUS |
| M07 (Shame) | 14 | 17 | 2 | STATUS |
| M08 (Pride) | 12 | 22 | 13 | STATUS |
| M09 (Humility) | 6 | 7 | 2 | STATUS |
| M10 (Sin) | 15 | 43 | 6 | STATUS |
| M10b (Wickedness) | 1 | 12 | 4 | STATUS |
| M10c (Defilement) | 2 | 4 | 2 | STATUS |
| M11 (Repentance) | 10 | 3 | 1 | ACTION |
| M12 (Purity) | 16 | 12 | 20 | QUALITY |
| M13 (Truth) | 5 | 11 | 9 | STATUS |
| M14 (Deceit) | 8 | 29 | 5 | STATUS |
| M15 (Wisdom) | 34 | 36 | 15 | STATUS |
| M16 (Folly) | 8 | 14 | 8 | STATUS |
| M17 (Counsel) | 2 | 14 | 1 | STATUS |
| M18 (Hope) | 13 | 12 | 3 | ACTION |
| M19 (Trust) | 10 | 15 | 6 | STATUS |
| M20 (Doubt) | 11 | 1 | 3 | ACTION |
| M21 (Prayer) | 13 | 12 | 4 | ACTION |
| M22 (Praise) | 10 | 27 | 9 | STATUS |
| M23 (Strength) | 41 | 47 | 31 | STATUS |
| M24 (Weakness) | 30 | 28 | 12 | ACTION |
| M25 (Life) | 5 | 6 | 4 | STATUS |
| M26 (Righteousness) | 12 | 20 | 10 | STATUS |
| M27 (Evil) | 5 | 11 | 3 | STATUS |
| M28 (Envy) | 11 | 23 | 5 | STATUS |
| M29 (Desire) | 3 | 5 | 4 | STATUS |
| M30 (Obedience) | 15 | 13 | 1 | ACTION |
| M31 (Faith) | 3 | 5 | 5 | STATUS |
| M33 (Peace) | 13 | 24 | 7 | STATUS |
| M34 (Perseverance) | 10 | 5 | 7 | ACTION |
| M35 (Testing) | 12 | 10 | 2 | ACTION |
| M36 (Service) | 10 | 12 | 1 | STATUS |
| M37 (Calling) | 19 | 1 | 2 | ACTION |
| M38 (Salvation) | 4 | 8 | 1 | STATUS |
| M39 (Blessing) | 7 | 7 | 2 | STATUS |
| M41 (Remembrance) | 12 | 5 | 0 | — |
| M42 (Speech) | 18 | 14 | 0 | ACTION |
| M43 (Prophecy) | 2 | 7 | 4 | STATUS |
| M44 (Relational) | 9 | 6 | 1 | ACTION |
| M45 (Transformation) | 7 | 4 | 2 | ACTION |
| M46 (Abundance) | 8 | 7 | 7 | ACTION |
