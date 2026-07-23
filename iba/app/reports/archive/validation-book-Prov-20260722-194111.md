# Base validation report — book 'Prov'

> Generated 2026-07-21T19:36:12Z. Read-only. Candidate (L4b) + passages. Sections shown are config-governed (`cfg_setting validation.show_*`).

## Verdict: ✗ FAIL   (11 pass · 3 warn · 1 fail)

## 1. App & DB
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | config loaded | a config_version | app-0.1.0 |  |
| ✓ PASS | data tables present | 18 tables | 18 present |  |
| ✓ PASS | STEP known-answer | expected answer | H0430G 'God', 2088 verses |  |

## 3. Candidate (L4b)
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | span_candidate -> span resolves | 0 orphan | 0 orphan |  |
| ✓ PASS | candidate_seed -> lemma_inventory | 0 orphan | 0 orphan |  |
| ✓ PASS | candidate spans stamped (book) | >=0 | 3173 |  |
| ⚠ WARN | candidate missing registry words (double control) | informational | 190 lemma(s) | candidate lemmas no registry word carries — grow the registry |

## 4. Passages
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✗ FAIL | candidate-bearing verses unpassaged | 0 | 10 | completeness gate |
| ✓ PASS | verse in at most one passage | 0 dup | 0 dup |  |
| ✓ PASS | anchors = passage count | 752 | 752 |  |
| ✓ PASS | passages do not cross chapters | 0 | 0 |  |
| ✓ PASS | passages needing review (> review_over verses) | reviewed | 0 flagged | a long run may be several passages — confirm the rule |

## 6. Value quality
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | span.surface (notblank, this book) | 0 violations | 0/9215 |  |
| ⚠ WARN | candidate_seed.tag (pattern:candidate.tag_clean_pattern, programme-wide) | 0 violations | 226/1732 | see candidate-quality.md for detail |
| ⚠ WARN | lemma_inventory.gloss (pattern:candidate.tag_clean_pattern, programme-wide) | 0 violations | 494/11421 | see candidate-quality.md for detail |

