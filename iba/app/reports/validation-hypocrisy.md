# Validation report — 'hypocrisy'

> Generated 2026-07-22T18:39:15Z · run `RUN-smoketest-0b-reportword2`. Read-only; the authoritative gate is `raw.validate`. Sections shown are config-governed (`cfg_setting validation.show_*`).

## Verdict: ⚠ WARN   (63 pass · 3 warn · 0 fail)

## Contents

- [1. App & DB](#1-app-db)
- [2. Pre/post](#2-prepost)
- [3. Integrity](#3-integrity)
- [4. References](#4-references)
- [5. Expectations](#5-expectations)
- [6. Value quality](#6-value-quality)

## 1. App & DB

| verdict | check | expected | actual | detail |
| --- | --- | --- | --- | --- |
| ✓ PASS | config loaded | a config_version | app-0.1.0+8ae3a4e7d5c9 |  |
| ✓ PASS | data tables present | 18 tables | 18 present |  |
| ✓ PASS | STEP known-answer | expected answer | H0430G 'God', 2088 verses |  |
| ✓ PASS | latest run complete | done | done | RUN-smoketest-0b-reportword2 |
## 2. Pre/post

| table | pre | post | delta |
| --- | --- | --- | --- |
| candidate_seed | 2087 | 2087 | 0 |
| cfg_change_detail | 37 | 37 | 0 |
| escalation | 248 | 248 | 0 |
| lemma_inventory | 11781 | 11781 | 0 |
| passage | 18571 | 18571 | 0 |
| run | 799 | 799 | 0 |
| span | 534075 | 534075 | 0 |
| span_candidate | 85064 | 85064 | 0 |
| strong | 3463 | 3463 | 0 |
| strong_lexicon | 1506 | 1506 | 0 |
| strong_meaning_tree | 9454 | 9454 | 0 |
| strong_sense | 3463 | 3463 | 0 |
| strong_verse | 112446 | 112446 | 0 |
| validation_result | 15579 | 15597 | 18 |
| verse | 29037 | 29037 | 0 |
| verse_passage | 24847 | 24847 | 0 |
| word_registry | 178 | 178 | 0 |
| word_strong | 4796 | 4796 | 0 |
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
| ✓ PASS | candidate_seed.strong_variant not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | candidate_seed.sense_seq not-null | 0 NULL | 0 NULL |  |
| ✓ PASS | candidate_seed dedup key (lemma_key, strong_variant, sense_seq) | 0 dup | 0 dup |  |
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
| ⚠ WARN | word_strong.strong -> strong.strongNumber | 0 orphan | 29 orphan | expected for the raw model |
| ✓ PASS | strong_sense.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_lexicon.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_verse.strong -> strong.strongNumber | 0 orphan | 0 orphan |  |
| ✓ PASS | strong_verse.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ✓ PASS | span.verse_id -> verse.id | 0 orphan | 0 orphan |  |
| ⚠ WARN | span.strong_variant -> strong.strongNumber | 0 orphan | 411011 orphan | expected for the raw model |
| ✓ PASS | candidate_seed.lemma_key -> lemma_inventory.lemma_key | 0 orphan | 0 orphan |  |
| ⚠ WARN | candidate_seed.strong_variant -> strong.strongNumber | 0 orphan | 442 orphan | expected for the raw model |
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
