# Validation report — 'anger'

> Generated 2026-07-18T09:53:14Z · run `RUN-20260718_105306_756-NEW-WORD`. Read-only; the authoritative gate is `raw.validate`.

## Verdict: ✗ FAIL   (52 pass · 1 warn · 1 fail)

## 1. App & DB
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | config loaded | a config_version | app-0.1.0 |  |
| ✓ PASS | data tables present | 17 tables | 17 present |  |
| ✓ PASS | STEP known-answer | expected answer | H0430G 'God', 2088 verses |  |
| ✗ FAIL | latest run complete | done | failed | RUN-20260718_105306_756-NEW-WORD |

## 2. Pre/post
| table | pre | post | delta |
| --- | --- | --- | --- |
| candidate_seed | 1836 | 0 | -1836 |
| escalation | 7 | 0 | -7 |
| lemma_inventory | 11781 | 0 | -11781 |
| passage | 143 | 0 | -143 |
| run | 38 | 0 | -38 |
| span | 33471 | 0 | -33471 |
| span_candidate | 617 | 0 | -617 |
| strong | 107 | 0 | -107 |
| strong_lexicon | 32 | 0 | -32 |
| strong_meaning_tree | 91 | 0 | -91 |
| strong_sense | 107 | 0 | -107 |
| strong_verse | 2011 | 0 | -2011 |
| validation_result | 676 | 0 | -676 |
| verse | 1673 | 0 | -1673 |
| verse_passage | 146 | 0 | -146 |
| word_registry | 7 | 0 | -7 |
| word_strong | 114 | 0 | -114 |

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

## 4. References
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | word_strong.word_id -> word_registry.id | 0 orphan | 0 orphan |  |
| ✓ PASS | word_strong.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_sense.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_lexicon.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_verse.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_verse.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ✓ PASS | span.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ⚠ WARN | span.strong_variant -> strong.strongNumber | 0 orphan | 31387 orphan | expected for the raw model |
| ✓ PASS | candidate_seed.lemma_key -> lemma_inventory.lemma_key | 0 orphan | 0 orphan |  |
| ✓ PASS | span_candidate.span_id -> span.id | 0 orphan | 0 orphan |  |
| ✓ PASS | passage.anchor_verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ✓ PASS | verse_passage.passage_id -> passage.id | 0 orphan | 0 orphan |  |
| ✓ PASS | verse_passage.verse_id -> verse.id | 0 orphan | 0 orphan |  |

## 5. Expectations
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | registry built | raw-complete | raw-complete |  |
| ✓ PASS | registry source set | non-empty | set |  |
| ✓ PASS | word_strong present | >=1 | 36 |  |
| ✓ PASS | word_strong non-particle | 0 particles | 0 |  |
| ✓ PASS | every strong has a sense | 0 missing | 0 missing |  |
| ✓ PASS | span recovers strong_verse | 0 missed | 0 strong(s) missed |  |
| ✓ PASS | verse.osisId unique | 0 dup | 0 dup |  |

