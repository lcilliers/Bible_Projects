# 4-way term split — bucket summary (v2)

**Generated:** 2026-05-04T08:50:04Z

## Filter validation

- Working set: **2,491 terms** (intersection of semantic and co-occurrence vectors)
- Excluded as 0-verse: **66 terms** (no active OWNER verse-record)
- All working-set terms have:
  - `mti_terms.delete_flagged = 0`
  - `wa_term_inventory.delete_flagged = 0` (OWNER row)
  - At least one `wa_verse_records.delete_flagged = 0` row

## Bucket sizes

| Bucket | Count |
|---|---|
| LOCI | 36 |
| GENERICS | 97 |
| EXTRACTION-NOISE | 26 |
| CHARACTERISTICS (Hebrew + Greek) | 2332 |
|   ↳ Hebrew | 1408 |
|   ↳ Greek | 924 |

## Note on registry

Registry has **no weight in clustering**. Clustering uses only:
1. Weighted semantic vector (root + gloss + meaning text)
2. Co-occurrence vector (verse co-occurrence with other OWNER terms)

Registry is omitted entirely from the cluster table outputs to avoid suggesting otherwise.