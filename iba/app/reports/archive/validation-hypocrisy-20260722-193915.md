# Validation report — 'hypocrisy'

> Generated 2026-07-21T19:36:11Z · run `RUN-20260718_152117_153-NEW-WORD`. Read-only; the authoritative gate is `raw.validate`. Sections shown are config-governed (`cfg_setting validation.show_*`).

## Verdict: ✗ FAIL   (60 pass · 2 warn · 1 fail)

## 1. App & DB
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | config loaded | a config_version | app-0.1.0 |  |
| ✓ PASS | data tables present | 18 tables | 18 present |  |
| ✓ PASS | STEP known-answer | expected answer | H0430G 'God', 2088 verses |  |
| ✗ FAIL | latest run complete | done | failed | RUN-20260718_152117_153-NEW-WORD |

## 2. Pre/post
| table | pre | post | delta |
| --- | --- | --- | --- |
| candidate_seed | 2218 | 0 | -2218 |
| escalation | 67 | 0 | -67 |
| lemma_inventory | 11781 | 0 | -11781 |
| passage | 143 | 0 | -143 |
| run | 285 | 0 | -285 |
| span | 455926 | 0 | -455926 |
| span_candidate | 617 | 0 | -617 |
| strong | 1243 | 0 | -1243 |
| strong_lexicon | 508 | 0 | -508 |
| strong_meaning_tree | 1081 | 0 | -1081 |
| strong_sense | 1243 | 0 | -1243 |
| strong_verse | 52006 | 0 | -52006 |
| validation_result | 4995 | 0 | -4995 |
| verse | 24019 | 0 | -24019 |
| verse_passage | 146 | 0 | -146 |
| word_registry | 67 | 0 | -67 |
| word_strong | 1473 | 0 | -1473 |

## 3. Integrity
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | word_registry.word not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | word_registry dedup key (word) | 0 dup | 0 dup |  |
| ✓ PASS | word_strong.word_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | word_strong.strong not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | word_strong dedup key (word_id, strong) | 0 dup | 0 dup |  |
| ✓ PASS | strong dedup key (strongNumber) | 0 dup | 0 dup |  |
| ✓ PASS | strong_sense dedup key (strong) | 0 dup | 0 dup |  |
| ✓ PASS | strong_meaning_tree.lemma_key not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | strong_meaning_tree dedup key (id) | 0 dup | 0 dup |  |
| ✓ PASS | strong_lexicon dedup key (strong) | 0 dup | 0 dup |  |
| ✓ PASS | verse.osisId not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | verse dedup key (osisId) | 0 dup | 0 dup |  |
| ✓ PASS | strong_verse.strong not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | strong_verse.verse_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | strong_verse dedup key (strong, verse_id) | 0 dup | 0 dup |  |
| ✓ PASS | span.verse_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | span.position not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | span dedup key (verse_id, position) | 0 dup | 0 dup |  |
| ✓ PASS | lemma_inventory.lemma_key not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | lemma_inventory dedup key (lemma_key) | 0 dup | 0 dup |  |
| ✓ PASS | candidate_seed.lemma_key not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | candidate_seed dedup key (lemma_key) | 0 dup | 0 dup |  |
| ✓ PASS | span_candidate.span_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | span_candidate dedup key (span_id) | 0 dup | 0 dup |  |
| ✓ PASS | passage.book not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | passage.anchor_verse_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | passage dedup key (id) | 0 dup | 0 dup |  |
| ✓ PASS | verse_passage.passage_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | verse_passage.verse_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | verse_passage dedup key (verse_id) | 0 dup | 0 dup |  |
| ✓ PASS | cfg_change_detail.run_id not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | cfg_change_detail.table_name not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | cfg_change_detail.op not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | cfg_change_detail.applied_at not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | cfg_change_detail dedup key (id) | 0 dup | 0 dup |  |

## 4. References
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | word_strong.word_id -> word_registry.id | 0 orphan | 0 orphan |  |
| ⚠ WARN | word_strong.strong -> strong.strongNumber | 0 orphan | 30 orphan | expected for the raw model |
| ✓ PASS | strong_sense.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_lexicon.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_verse.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_verse.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ✓ PASS | span.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ⚠ WARN | span.strong_variant -> strong.strongNumber | 0 orphan | 411011 orphan | expected for the raw model |
| ✓ PASS | candidate_seed.lemma_key -> lemma_inventory.lemma_key | 0 orphan | 0 orphan |  |
| ✓ PASS | span_candidate.span_id -> span.id | 0 orphan | 0 orphan |  |
| ✓ PASS | passage.anchor_verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ✓ PASS | verse_passage.passage_id -> passage.id | 0 orphan | 0 orphan |  |
| ✓ PASS | verse_passage.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ✓ PASS | cfg_change_detail.run_id -> run.run_id | 0 orphan | 0 orphan |  |

## 5. Expectations
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | registry built | raw-complete | raw-complete |  |
| ✓ PASS | registry source set | non-empty | set |  |
| ✓ PASS | word_strong present | >=1 | 5 |  |
| ✓ PASS | word_strong non-particle | 0 particles | 0 |  |
| ✓ PASS | every strong has a sense | 0 missing | 0 missing |  |
| ✓ PASS | span recovers strong_verse | 0 missed | 0 strong(s) missed |  |
| ✓ PASS | verse.osisId unique | 0 dup | 0 dup |  |

## 6. Value quality
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | strong_sense.head (nohtml) | 0 violations | 0/5 |  |
| ✓ PASS | span.surface (notblank) | 0 violations | 0/262 |  |
| ✓ PASS | word_registry.word (pattern:candidate.tag_clean_pattern) | 0 violations | 0/1 |  |

