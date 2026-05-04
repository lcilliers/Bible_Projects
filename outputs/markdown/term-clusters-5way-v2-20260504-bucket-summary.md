# 5-way term split — bucket summary (v4 with verse profile)

**Generated:** 2026-05-04T09:16:45Z

- Working set: **2,491 terms** (0-verse and deleted excluded)

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

## Verse profile fields

Each term entry in JSON now carries:
- `verse_count` — number of distinct OWNER-active verses term appears in
- `multi_term_count` — verses where another OWNER term also appears
- `multi_term_pct` — multi_term_count / verse_count × 100