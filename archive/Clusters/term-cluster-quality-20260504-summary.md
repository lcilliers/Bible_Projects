# Cluster quality summary (Hebrew + Greek)

**Generated:** 2026-05-04T09:24:32Z

## Quality breakdown

| Pool | TIGHT | MODERATE | LOOSE | Total |
|---|---|---|---|---|
| Hebrew | 27 | 46 | 7 | 80 |
| Greek | 8 | 25 | 7 | 40 |

## Reading the metrics

- **cohesion** = mean cosine similarity of members to centroid. Range [0,1]. Higher = tighter.
- **theme%** = top theme word frequency / cluster size. Higher = more thematically concentrated.
- **TIGHT** = cohesion ≥ 0.60 OR (n ≤ 12 AND cohesion ≥ 0.50). Lock in as analytical units.
- **MODERATE** = in between. Acceptable but inspect.
- **LOOSE** = cohesion < 0.45 OR (n ≥ 30 AND cohesion < 0.55). Get sub-clustered automatically.