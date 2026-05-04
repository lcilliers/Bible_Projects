# 5-way term split — bucket summary (v3)

**Generated:** 2026-05-04T09:03:04Z

- Working set: **2,491 terms** (0-verse and delete_flagged terms excluded)

## Bucket sizes

| Bucket | Count | Role in clustering |
|---|---|---|
| LOCI | 36 | Clustered separately |
| GENERICS | 97 | Excluded entirely |
| EXTRACTION-NOISE | 37 | Excluded entirely |
| QUALIFIERS | 54 | Excluded from primary clustering; attached post-hoc |
| CHARACTERISTICS | 2267 | **Primary clustering pool** |
|   ↳ Hebrew | 1378 | k=80 |
|   ↳ Greek | 889 | k=40 |

## Note on registry

Registry has **no weight in clustering**. Clustering uses only:
1. Weighted semantic vector (root + gloss + meaning text)
2. Co-occurrence vector (verse co-occurrence with other OWNER terms)