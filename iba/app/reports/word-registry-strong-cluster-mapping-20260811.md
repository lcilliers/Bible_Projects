# word_registry.strongNumber → old-project cluster mapping — 2026-08-11

**Revises** [`word-strong-cluster-mapping-20260810.md`](word-strong-cluster-mapping-20260810.md). That
version reduced each word down to one "dominant cluster" — not what was asked for. This version is the flat
mapping: **every row of `word_registry.strongNumber` against every old-DB cluster it maps to, one row per
hit, with no reduction.** A `strongNumber` that maps to more than one old cluster produces more than one row.

## Source

- **New:** [`iba/app/reports/export/word_registry.csv`](export/word_registry.csv) — the exact file open in
  the IDE, columns `registry_word, status, source, strongNumber, stepGloss, language, count, sense_head`.
  4,849 rows (179 distinct registry words, 3,447 distinct `strongNumber` values — a Strong's repeats across
  words it's shared with).
- **Old:** `database/bible_research.db` → `mti_terms.strongs_number` / `.cluster_code` ⋈ `cluster.short_name`,
  same lookup as the 08-10 report (formats match directly, no conversion needed).

## Method

For every row in `word_registry.csv`, look up its `strongNumber` in the old DB's `mti_terms.cluster_code`
and emit one output row per **distinct** cluster_code found (duplicate `mti_terms` rows for the same
Strong's — the known OT-DBR-009 issue — are still deduplicated to their distinct `cluster_code` values, not
double-counted). Where a `strongNumber` has no cluster_code in the old DB at all, one row is still emitted
with the cluster fields blank — so the output is a complete accounting of every registry row, not a filtered
match-only list.

## Coverage

| | count |
|---|---:|
| `word_registry.csv` rows | 4,849 |
| — rows producing ≥1 cluster match | 2,994 |
| — rows unmatched: old DB has the Strong's but never clustered it | 642 |
| — rows unmatched: old DB has no row at all for that Strong's | 1,213 |
| Output rows (one per word↔strong↔cluster hit, plus one per unmatched strong) | 4,972 |

**Distinct `strongNumber` values (3,447 total):**

| | count |
|---|---:|
| Maps to 0 old clusters | 1,605 |
| Maps to exactly 1 old cluster | 1,771 |
| Maps to 2+ old clusters | 71 (max seen: 2, e.g. `H8552`) |

So the "more than one cluster" case is real but narrow — 71 of 3,447 distinct Strong's numbers (2.1%), never
more than 2 clusters for any one Strong's.

## Full mapping

The complete list — every `word_registry.csv` row against every old cluster it hits (blank cluster fields
= no old-DB match) — is in the companion CSV:
[`word-registry-strong-cluster-mapping-20260811.csv`](word-registry-strong-cluster-mapping-20260811.csv).

Columns: `registry_word, strongNumber, language, stepGloss, cluster_code, cluster_name`.

## Note

This is the same underlying old-DB lookup as the 08-10 report; only the shape of the output changed —
per the instruction, no word-level "dominant cluster" collapsing this time, and the base table is the
`word_registry.csv` export itself rather than the `word_strong` DB table (the two are near-identical in
content; the export has 179 words / 4,849 rows against the DB table's 178 words / 4,848 rows — a 1-row/
1-word difference not chased here since it wasn't material to either report's question).
