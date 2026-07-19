# Base validation report — book 'Prov'

> Generated 2026-07-18T09:34:56Z. Read-only. Candidate (L4b) + passages.

## Verdict: ⚠ WARN   (11 pass · 1 warn · 0 fail)

## 1. App & DB
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | config loaded | a config_version | app-0.1.0 |  |
| ✓ PASS | data tables present | 17 tables | 17 present |  |
| ✓ PASS | STEP known-answer | expected answer | H0430G 'God', 2088 verses |  |

## 3. Candidate (L4b)
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | span_candidate -> span resolves | 0 orphan | 0 orphan |  |
| ✓ PASS | candidate_seed -> lemma_inventory | 0 orphan | 0 orphan |  |
| ✓ PASS | candidate spans stamped (book) | >=0 | 254 |  |
| ⚠ WARN | candidate missing registry words (double control) | informational | 1712 lemma(s) | candidate lemmas no registry word carries — grow the registry |

## 4. Passages
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | candidate-bearing verses unpassaged | 0 | 0 | completeness gate |
| ✓ PASS | verse in at most one passage | 0 dup | 0 dup |  |
| ✓ PASS | anchors = passage count | 56 | 56 |  |
| ✓ PASS | passages do not cross chapters | 0 | 0 |  |
| ✓ PASS | passages needing review (> review_over verses) | reviewed | 0 flagged | a long run may be several passages — confirm the rule |

