# Validation report — 'malice'

> Generated 2026-07-18T07:30:59Z · run `RUN-MALICE-SNAP`. Read-only; the authoritative gate is `raw.validate`.

## Verdict: ⚠ WARN   (36 pass · 1 warn · 0 fail)

## 1. App & DB
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | config loaded | a config_version | app-0.1.0 |  |
| ✓ PASS | data tables present | 12 tables | 12 present |  |
| ✓ PASS | STEP known-answer | expected answer | H0430G 'God', 2088 verses |  |
| ✓ PASS | latest run complete | done | done | RUN-MALICE-SNAP |

## 2. Pre/post
| table | pre | post | delta |
| --- | --- | --- | --- |
| escalation | 2 | 2 | 0 |
| run | 6 | 6 | 0 |
| span | 4628 | 4628 | 0 |
| strong | 14 | 14 | 0 |
| strong_lexicon | 6 | 6 | 0 |
| strong_meaning_tree | 14 | 14 | 0 |
| strong_sense | 14 | 14 | 0 |
| strong_verse | 288 | 288 | 0 |
| validation_result | 14 | 28 | 14 |
| verse | 278 | 278 | 0 |
| word_registry | 2 | 2 | 0 |
| word_strong | 14 | 14 | 0 |

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
| ⚠ WARN | span.strong_variant -> strong.strongNumber | 0 orphan | 4328 orphan | expected for the raw model |

## 5. Expectations
| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | registry built | raw-complete | raw-complete |  |
| ✓ PASS | registry source set | non-empty | set |  |
| ✓ PASS | word_strong present | >=1 | 9 |  |
| ✓ PASS | word_strong non-particle | 0 particles | 0 |  |
| ✓ PASS | every strong has a sense | 0 missing | 0 missing |  |
| ✓ PASS | span recovers strong_verse | 0 missed | 0 strong(s) missed |  |
| ✓ PASS | verse.osisId unique | 0 dup | 0 dup |  |

