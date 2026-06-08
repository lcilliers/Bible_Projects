# Cross-cluster link correlation — contextual × semantic (roll-up synthesis)

> READ-ONLY (`scripts/_assess_link_correlation.py`). Ties **angle 1** (co-occurrence = appear together) to **angle 5** (keyword Jaccard = mean the same) + **angle 3** (shared forms). **SAME-ish** = high both (merge candidate) · **RELATIONAL** = co-occur but differ (a real relationship) · **KIN** = similar meaning, rarely together (parallel facets). No DB writes.

## A · Top 30 links by CO-OCCURRENCE — with their semantic kinship

| Cluster A | Cluster B | co-occur | %A | kw-Jaccard | shared forms | class |
|---|---|---|---|---|---|---|
| Life | Relational | 211 | 28% | 0.03 | 1 | RELATIONAL |
| Wisdom | Strength | 126 | 8% | 0.07 | 0 | SAME-ish |
| Praise | Strength | 112 | 9% | 0.06 | 0 | RELATIONAL |
| Sin | Repentance | 109 | 9% | 0.03 | 0 | RELATIONAL |
| Sin | Righteousness | 104 | 8% | 0.04 | 0 | RELATIONAL |
| Repentance | Salvation | 99 | 30% | 0.05 | 0 | RELATIONAL |
| Joy | Praise | 95 | 9% | 0.06 | 1 | RELATIONAL |
| Fear | Strength | 92 | 10% | 0.03 | 0 | RELATIONAL |
| Strength | Weakness | 91 | 4% | 0.05 | 0 | RELATIONAL |
| Love | Strength | 90 | 7% | 0.08 | 0 | SAME-ish |
| Sin | Purity | 88 | 7% | 0.06 | 0 | SAME-ish |
| Wickedness | Righteousness | 86 | 17% | 0.03 | 1 | RELATIONAL |
| Love | Praise | 85 | 7% | 0.06 | 0 | SAME-ish |
| Strength | Calling | 83 | 4% | 0.05 | 0 | RELATIONAL |
| Love | Truth | 81 | 7% | 0.05 | 0 | RELATIONAL |
| Sin | Strength | 80 | 6% | 0.02 | 0 | RELATIONAL |
| Joy | Love | 78 | 7% | 0.05 | 0 | RELATIONAL |
| Joy | Wisdom | 76 | 7% | 0.04 | 0 | RELATIONAL |
| Anger | Strength | 75 | 12% | 0.03 | 1 | RELATIONAL |
| Truth | Righteousness | 75 | 11% | 0.04 | 0 | RELATIONAL |
| Sin | Salvation | 75 | 6% | 0.03 | 0 | RELATIONAL |
| Purity | Strength | 74 | 8% | 0.03 | 1 | RELATIONAL |
| Wisdom | Righteousness | 72 | 5% | 0.08 | 0 | SAME-ish |
| Pride | Strength | 71 | 11% | 0.04 | 0 | RELATIONAL |
| Wisdom | Remembrance | 71 | 5% | 0.07 | 0 | SAME-ish |
| Wisdom | Calling | 69 | 5% | 0.07 | 0 | SAME-ish |
| Joy | Strength | 67 | 6% | 0.04 | 0 | RELATIONAL |
| Sin | Wickedness | 65 | 5% | 0.07 | 1 | SAME-ish |
| Strength | Remembrance | 65 | 3% | 0.03 | 0 | RELATIONAL |
| Strength | Service | 65 | 3% | 0.03 | 0 | RELATIONAL |

## B · Top 30 links by SEMANTIC kinship — with their co-occurrence

| Cluster A | Cluster B | kw-Jaccard | co-occur | shared forms | class |
|---|---|---|---|---|---|
| Repentance | Transformation | 0.23 | 22 | 1 | KIN |
| Grief | Weakness | 0.16 | 57 | 2 | SAME-ish |
| Speech | Prophecy | 0.12 | 3 | 0 | KIN |
| Pride | Folly | 0.10 | 9 | 1 | KIN |
| Prayer | Remembrance | 0.10 | 22 | 0 | KIN |
| Strength | Perseverance | 0.10 | 18 | 1 | KIN |
| Hope | Trust | 0.09 | 7 | 0 | KIN |
| Love | Blessing | 0.09 | 60 | 0 | SAME-ish |
| Strength | Righteousness | 0.09 | 64 | 0 | SAME-ish |
| Righteousness | Faith | 0.09 | 34 | 0 | SAME-ish |
| Wickedness | Evil | 0.09 | 27 | 0 | SAME-ish |
| Wisdom | Righteousness | 0.08 | 72 | 0 | SAME-ish |
| Pride | Praise | 0.08 | 51 | 1 | SAME-ish |
| Righteousness | Peace | 0.08 | 23 | 0 | KIN |
| Joy | Blessing | 0.08 | 52 | 1 | SAME-ish |
| Repentance | Obedience | 0.08 | 9 | 0 | KIN |
| Love | Peace | 0.08 | 47 | 0 | SAME-ish |
| Sin | Deceit | 0.08 | 29 | 0 | SAME-ish |
| Truth | Faith | 0.08 | 11 | 0 | KIN |
| Peace | Perseverance | 0.08 | 3 | 0 | KIN |
| Love | Strength | 0.08 | 90 | 0 | SAME-ish |
| Trust | Perseverance | 0.08 | 11 | 0 | KIN |
| Wisdom | Remembrance | 0.07 | 71 | 0 | SAME-ish |
| Fear | Grief | 0.07 | 28 | 1 | SAME-ish |
| Desire | Blessing | 0.07 | 15 | 0 | KIN |
| Sin | Wickedness | 0.07 | 65 | 1 | SAME-ish |
| Love | Prayer | 0.07 | 32 | 0 | SAME-ish |
| Fear | Weakness | 0.07 | 33 | 0 | SAME-ish |
| Wisdom | Strength | 0.07 | 126 | 0 | SAME-ish |
| Truth | Trust | 0.07 | 15 | 1 | KIN |

## C · RELATIONAL links — high co-occurrence, LOW semantic overlap (appear together, differ)

| Cluster A | Cluster B | co-occur | kw-Jaccard |
|---|---|---|---|
| Life | Relational | 211 | 0.03 |
| Praise | Strength | 112 | 0.06 |
| Sin | Repentance | 109 | 0.03 |
| Sin | Righteousness | 104 | 0.04 |
| Repentance | Salvation | 99 | 0.05 |
| Joy | Praise | 95 | 0.06 |
| Fear | Strength | 92 | 0.03 |
| Strength | Weakness | 91 | 0.05 |
| Wickedness | Righteousness | 86 | 0.03 |
| Strength | Calling | 83 | 0.05 |
| Love | Truth | 81 | 0.05 |
| Sin | Strength | 80 | 0.02 |
| Joy | Love | 78 | 0.05 |
| Joy | Wisdom | 76 | 0.04 |
| Anger | Strength | 75 | 0.03 |
