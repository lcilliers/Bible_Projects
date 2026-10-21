# IBA Config Tables Dump

- Database: C:\Bible_study_projects\iba\app\db\iba.db
- Generated (UTC): 2026-07-18T05:55:56Z
- Table filter: cfg_%
- Matched tables: 15

## Table List

- cfg_api
- cfg_book_order
- cfg_change_log
- cfg_column
- cfg_connection
- cfg_enum
- cfg_meta
- cfg_on_fail
- cfg_setting
- cfg_status_flow
- cfg_step
- cfg_table
- cfg_unique
- cfg_work_package
- cfg_write_grant

## cfg_api

- Columns: 4
- Rows: 3

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | name | TEXT | 0 |  | 1 |
| 1 | route | TEXT | 0 |  | 0 |
| 2 | input | TEXT | 0 |  | 0 |
| 3 | returns | TEXT | 0 |  | 0 |

Data rows:

| name | route | input | returns |
|---|---|---|---|
| call1_meanings | rest/search/masterSearch/version={version}\|meanings={word} | the English word | definitions[] (the seed strongs) + results[] (verses) |
| call2_getInfo | rest/module/getInfo/{version}//{strong}// | a strong | vocabInfos[0] — the detail and the meaning |
| call3_strong | rest/search/masterSearch/strong={strong}\|version={version} | a strong | results[] — verses, each preview a full interlinear |

## cfg_book_order

- Columns: 2
- Rows: 66

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | book | TEXT | 0 |  | 1 |
| 1 | ordinal | INTEGER | 0 |  | 0 |

Data rows:

| book | ordinal |
|---|---|
| Gen | 0 |
| Exod | 1 |
| Lev | 2 |
| Num | 3 |
| Deut | 4 |
| Josh | 5 |
| Judg | 6 |
| Ruth | 7 |
| 1Sam | 8 |
| 2Sam | 9 |
| 1Kgs | 10 |
| 2Kgs | 11 |
| 1Chr | 12 |
| 2Chr | 13 |
| Ezra | 14 |
| Neh | 15 |
| Esth | 16 |
| Job | 17 |
| Ps | 18 |
| Prov | 19 |
| Eccl | 20 |
| Song | 21 |
| Isa | 22 |
| Jer | 23 |
| Lam | 24 |
| Ezek | 25 |
| Dan | 26 |
| Hos | 27 |
| Joel | 28 |
| Amos | 29 |
| Obad | 30 |
| Jonah | 31 |
| Mic | 32 |
| Nah | 33 |
| Hab | 34 |
| Zeph | 35 |
| Hag | 36 |
| Zech | 37 |
| Mal | 38 |
| Matt | 39 |
| Mark | 40 |
| Luke | 41 |
| John | 42 |
| Acts | 43 |
| Rom | 44 |
| 1Cor | 45 |
| 2Cor | 46 |
| Gal | 47 |
| Eph | 48 |
| Phil | 49 |
| Col | 50 |
| 1Thess | 51 |
| 2Thess | 52 |
| 1Tim | 53 |
| 2Tim | 54 |
| Titus | 55 |
| Phlm | 56 |
| Heb | 57 |
| Jas | 58 |
| 1Pet | 59 |
| 2Pet | 60 |
| 1John | 61 |
| 2John | 62 |
| 3John | 63 |
| Jude | 64 |
| Rev | 65 |

## cfg_change_log

- Columns: 5
- Rows: 3

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | id | INTEGER | 0 |  | 1 |
| 1 | config_version | TEXT | 0 |  | 0 |
| 2 | seed_hash | TEXT | 0 |  | 0 |
| 3 | loaded_at | TEXT | 0 |  | 0 |
| 4 | validated | INTEGER | 0 |  | 0 |

Data rows:

| id | config_version | seed_hash | loaded_at | validated |
|---|---|---|---|---|
| 1 | app-0.1.0 | 6d99b2d0554df65e | 2026-07-18T03:26:55Z | 1 |
| 2 | app-0.1.0 | 6d99b2d0554df65e | 2026-07-18T03:27:45Z | 1 |
| 3 | app-0.1.0 | 6d99b2d0554df65e | 2026-07-18T03:27:46Z | 1 |

## cfg_column

- Columns: 13
- Rows: 85

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | table_name | TEXT | 0 |  | 1 |
| 1 | name | TEXT | 0 |  | 2 |
| 2 | ordinal | INTEGER | 0 |  | 0 |
| 3 | type | TEXT | 0 |  | 0 |
| 4 | is_pk | INTEGER | 0 |  | 0 |
| 5 | notnull | INTEGER | 0 |  | 0 |
| 6 | is_unique | INTEGER | 0 |  | 0 |
| 7 | dflt | TEXT | 0 |  | 0 |
| 8 | fk | TEXT | 0 |  | 0 |
| 9 | use | TEXT | 0 |  | 0 |
| 10 | expectation | TEXT | 0 |  | 0 |
| 11 | source | TEXT | 0 |  | 0 |
| 12 | filled_by | TEXT | 0 |  | 0 |

Data rows:

| table_name | name | ordinal | type | is_pk | notnull | is_unique | dflt | fk | use | expectation | source | filled_by |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| word_registry | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| word_registry | word | 1 | TEXT | 0 | 1 | 1 |  |  | the English word |  | run.param.Word |  |
| word_registry | source | 2 | TEXT | 0 | 0 | 0 |  |  | why it was registered — the growth trigger |  | run.param.Source |  |
| word_registry | status | 3 | TEXT | 0 | 0 | 0 |  |  | registry processing stage | enum.word_status |  | registry+raw+signoff |
| word_registry | created_at | 4 | TEXT | 0 | 0 | 0 |  |  | when registered |  |  | registry.create |
| word_registry | deleted | 5 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| word_strong | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| word_strong | word_id | 1 | INTEGER | 0 | 1 | 0 |  | word_registry.id | the word |  | run.context.word_id |  |
| word_strong | strong | 2 | TEXT | 0 | 1 | 0 |  | strong.strongNumber | a strong the word returned |  | call1.definitions[].strongNumber |  |
| word_strong | deleted | 3 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| strong | strongNumber | 0 | TEXT | 1 | 0 | 0 |  |  | the resolved Strong's code — the key |  | call2.vocabInfos[0].strongNumber |  |
| strong | accentedUnicode | 1 | TEXT | 0 | 0 | 0 |  |  | the actual Hebrew/Greek word |  | call2.vocabInfos[0].accentedUnicode |  |
| strong | stepGloss | 2 | TEXT | 0 | 0 | 0 |  |  | short English sense |  | call2.vocabInfos[0].stepGloss |  |
| strong | stepTransliteration | 3 | TEXT | 0 | 0 | 0 |  |  | romanised form; never shown without the gloss |  | call2.vocabInfos[0].stepTransliteration |  |
| strong | language | 4 | TEXT | 0 | 0 | 0 |  |  | Hebrew/Greek from the code prefix |  | derived:call2.strongNumber |  |
| strong | count | 5 | INTEGER | 0 | 0 | 0 |  |  | STEP token frequency — NOT a verse count, may be capped |  | call2.vocabInfos[0].count |  |
| strong | freqList | 6 | TEXT | 0 | 0 | 0 |  |  | raw frequency distribution |  | call2.vocabInfos[0].freqList |  |
| strong | created_at | 7 | TEXT | 0 | 0 | 0 |  |  | when first fetched |  |  | raw.detail |
| strong | deleted | 8 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| strong_sense | strong | 0 | TEXT | 1 | 0 | 0 |  | strong.strongNumber | the strong |  |  |  |
| strong_sense | head | 1 | TEXT | 0 | 0 | 0 |  |  | the sense — THE SPAN'S MEANING |  | derived:call2.mediumDef.head |  |
| strong_sense | is_own_lemma | 2 | INTEGER | 0 | 0 | 0 |  |  | 1 = no ': ' head; the code is its own lemma and the gloss is the sense |  | derived:call2.mediumDef |  |
| strong_sense | deleted | 3 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| strong_meaning_tree | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| strong_meaning_tree | lemma_key | 1 | TEXT | 0 | 1 | 0 |  |  | the base code the tree belongs to |  | derived:call2.strongNumber.base |  |
| strong_meaning_tree | sense_code | 2 | TEXT | 0 | 0 | 0 |  |  | the tree position: 1), 1a), 1b1) |  | derived:call2.mediumDef.tree |  |
| strong_meaning_tree | sense_text | 3 | TEXT | 0 | 0 | 0 |  |  | the sense line |  | derived:call2.mediumDef.tree |  |
| strong_meaning_tree | sort | 4 | INTEGER | 0 | 0 | 0 |  |  | order within the tree |  | derived:call2.mediumDef.tree |  |
| strong_meaning_tree | deleted | 5 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| strong_lexicon | strong | 0 | TEXT | 1 | 0 | 0 |  | strong.strongNumber | the strong |  |  |  |
| strong_lexicon | lsj | 1 | TEXT | 0 | 0 | 0 |  |  | LSJ entry (Greek) |  | call2.vocabInfos[0].lsjDefs |  |
| strong_lexicon | mounce | 2 | TEXT | 0 | 0 | 0 |  |  | Mounce short def (Greek) |  | call2.vocabInfos[0].shortDefMounce |  |
| strong_lexicon | deleted | 3 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| verse | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| verse | osisId | 1 | TEXT | 0 | 1 | 1 |  |  | the machine key, e.g. Matt.23.28 |  | call3.results[].osisId |  |
| verse | reference | 2 | TEXT | 0 | 0 | 0 |  |  | human reference, e.g. Mat 23:28 |  | call3.results[].key |  |
| verse | preview | 3 | TEXT | 0 | 0 | 0 |  |  | the full interlinear HTML — the source of span |  | call3.results[].preview |  |
| verse | step_version | 4 | TEXT | 0 | 0 | 0 |  |  | provenance — which STEP module |  | run.context.step_version |  |
| verse | created_at | 5 | TEXT | 0 | 0 | 0 |  |  | when first built |  |  | raw.verses |
| verse | deleted | 6 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| strong_verse | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| strong_verse | strong | 1 | TEXT | 0 | 1 | 0 |  | strong.strongNumber | the strong searched |  | call3.query.strong |  |
| strong_verse | verse_id | 2 | INTEGER | 0 | 1 | 0 |  | verse.id | the verse returned |  | call3.results[].osisId |  |
| strong_verse | deleted | 3 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| span | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| span | verse_id | 1 | INTEGER | 0 | 1 | 0 |  | verse.id | the verse |  | parse:verse.preview |  |
| span | position | 2 | INTEGER | 0 | 1 | 0 |  |  | running code index in the verse — the key with verse_id |  | parse:verse.preview |  |
| span | surface | 3 | TEXT | 0 | 0 | 0 |  |  | the English word this code belongs to; repeats across a word's codes |  | parse:verse.preview |  |
| span | strong_variant | 4 | TEXT | 0 | 0 | 0 |  | strong.strongNumber | ONE strong code |  | parse:verse.preview |  |
| span | morph_code | 5 | TEXT | 0 | 0 | 0 |  |  | the grammatical layer — one, aligned with the code |  | parse:verse.preview |  |
| span | is_particle | 6 | INTEGER | 0 | 0 | 0 |  |  | 1 if a grammar-particle code (H9xxx/G9xxx) |  | derived:strong_variant |  |
| span | built_at | 7 | TEXT | 0 | 0 | 0 |  |  | raw time |  |  | raw.verses |
| span | deleted | 8 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| run | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| run | run_id | 1 | TEXT | 0 | 1 | 1 |  |  | the run identifier |  |  | run.start |
| run | work_package | 2 | TEXT | 0 | 0 | 0 |  |  | which package |  |  | run.start |
| run | params | 3 | TEXT | 0 | 0 | 0 |  |  | JSON of the run params |  |  | run.start |
| run | runs_over | 4 | TEXT | 0 | 0 | 0 |  |  | the scope value, e.g. the word |  |  | run.start |
| run | config_version | 5 | TEXT | 0 | 0 | 0 |  |  | the config that ran — pinned before any work |  |  | run.start |
| run | state | 6 | TEXT | 0 | 0 | 0 |  |  | running \| paused \| done \| failed | enum.run_state |  | run |
| run | resume_point | 7 | TEXT | 0 | 0 | 0 |  |  | the step to resume at on continue |  |  | run |
| run | started_at | 8 | TEXT | 0 | 0 | 0 |  |  | start |  |  | run.start |
| run | ended_at | 9 | TEXT | 0 | 0 | 0 |  |  | end |  |  | run.end |
| run | outcome | 10 | TEXT | 0 | 0 | 0 |  |  | the final result |  |  | run.end |
| validation_result | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| validation_result | run_id | 1 | TEXT | 0 | 1 | 0 |  | run.run_id | the run that ran the check |  |  |  |
| validation_result | word | 2 | TEXT | 0 | 0 | 0 |  |  | the word the check was over |  |  | validate |
| validation_result | step | 3 | TEXT | 0 | 0 | 0 |  |  | the step that ran it |  |  | validate |
| validation_result | check_name | 4 | TEXT | 0 | 0 | 0 |  |  | which check |  |  | validate |
| validation_result | result | 5 | TEXT | 0 | 0 | 0 |  |  | pass \| fail |  |  | validate |
| validation_result | detail | 6 | TEXT | 0 | 0 | 0 |  |  | the specifics — counts, what failed |  |  | validate |
| validation_result | ran_at | 7 | TEXT | 0 | 0 | 0 |  |  | when |  |  | validate |
| validation_result | deleted | 8 | INTEGER | 0 | 0 | 0 | 0 |  | soft delete |  |  |  |
| escalation | id | 0 | INTEGER | 1 | 0 | 0 |  |  | surrogate key |  |  |  |
| escalation | run_id | 1 | TEXT | 0 | 1 | 0 |  | run.run_id | the paused run |  |  |  |
| escalation | word | 2 | TEXT | 0 | 0 | 0 |  |  | the word this interaction is about — durable across runs |  |  | escalation.raise |
| escalation | at_step | 3 | TEXT | 0 | 0 | 0 |  |  | where to resume — makes it a pause not a fork |  |  | escalation.raise |
| escalation | type | 4 | TEXT | 0 | 0 | 0 |  |  | prompted \| interactive | enum.escalation_type |  | escalation.raise |
| escalation | question | 5 | TEXT | 0 | 0 | 0 |  |  | the question |  |  | escalation.raise |
| escalation | preset | 6 | TEXT | 0 | 0 | 0 |  |  | the context that lets it be answered (JSON) |  |  | escalation.raise |
| escalation | tried | 7 | TEXT | 0 | 0 | 0 |  |  | what the app attempted before asking |  |  | escalation.raise |
| escalation | state | 8 | TEXT | 0 | 0 | 0 |  |  | raised \| answered \| resumed |  |  | escalation |
| escalation | answer | 9 | TEXT | 0 | 0 | 0 |  |  | the researcher's decision |  |  | escalation.answer |
| escalation | answered_at | 10 | TEXT | 0 | 0 | 0 |  |  | when |  |  | escalation.answer |
| escalation | raised_at | 11 | TEXT | 0 | 0 | 0 |  |  | when raised |  |  | escalation.raise |

## cfg_connection

- Columns: 2
- Rows: 3

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | key | TEXT | 0 |  | 1 |
| 1 | value | TEXT | 0 |  | 0 |

Data rows:

| key | value |
|---|---|
| base_url | http://localhost:8989 |
| version | ESV_th |
| timeout_seconds | 30 |

## cfg_enum

- Columns: 3
- Rows: 15

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | name | TEXT | 0 |  | 1 |
| 1 | value | TEXT | 0 |  | 2 |
| 2 | ordinal | INTEGER | 0 |  | 0 |

Data rows:

| name | value | ordinal |
|---|---|---|
| word_status | proposed | 0 |
| word_status | approved | 1 |
| word_status | raw-complete | 2 |
| word_status | signed-off | 3 |
| word_status | rejected | 4 |
| run_state | running | 0 |
| run_state | paused | 1 |
| run_state | done | 2 |
| run_state | failed | 3 |
| escalation_type | prompted | 0 |
| escalation_type | interactive | 1 |
| on_fail | report-continue | 0 |
| on_fail | pause-continue | 1 |
| on_fail | report-stop | 2 |
| on_fail | self-heal | 3 |

## cfg_meta

- Columns: 2
- Rows: 2

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | key | TEXT | 0 |  | 1 |
| 1 | value | TEXT | 0 |  | 0 |

Data rows:

| key | value |
|---|---|
| database | iba |
| config_version | app-0.1.0 |

## cfg_on_fail

- Columns: 5
- Rows: 7

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | step | TEXT | 0 |  | 1 |
| 1 | condition | TEXT | 0 |  | 2 |
| 2 | path | TEXT | 0 |  | 0 |
| 3 | resolver | TEXT | 0 |  | 0 |
| 4 | message | TEXT | 0 |  | 0 |

Data rows:

| step | condition | path | resolver | message |
|---|---|---|---|---|
| registry.exists | word-exists | report-stop |  | the word already exists; use a refresh run, not new-word |
| registry.create | needs-approval | pause-continue |  | a new word needs researcher approval |
| registry.create | word-rejected | report-stop |  | the researcher rejected the word |
| raw.discover | zero-strongs | pause-continue |  | the word maps to no strongs — a researcher question |
| raw.detail | no-vocab | report-continue |  | a strong returned no vocab — recorded STEP gap |
| raw.verses | shortfall | report-continue |  | a strong returned fewer rows than STEP's total |
| raw.validate | parse-mismatch | report-stop |  | span does not recover strong_verse |

## cfg_setting

- Columns: 3
- Rows: 18

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | key | TEXT | 0 |  | 1 |
| 1 | value | TEXT | 0 |  | 0 |
| 2 | use | TEXT | 0 |  | 0 |

Data rows:

| key | value | use |
|---|---|---|
| step.probe_strong | "H0430" | STEP preflight known-answer probe |
| step.expect_gloss_contains | "God" | STEP preflight known-answer probe |
| step.expect_min_verses | 1000 | STEP preflight known-answer probe |
| step.cap | 60 | STEP's hard result cap; > this triggers the forward-walk |
| step.walk_start | "Gen.1.1" | forward-walk lower bound |
| step.walk_end | "Rev.22.21" | forward-walk upper bound |
| step.walk_max_iter | 400 | forward-walk safety bound |
| discovery.particle_pattern | "^[HG]9\\d{3}$" | grammar-particle codes; excluded from discovery, flagged on a span |
| discovery.follow_related | false | relatedNos is root-family noise (H2519 -> 'to divide', 'Mount Halak'). Not followed. |
| meaning.head_marker | ": " | a mediumDef starting with this is a SENSE: head + the lemma's tree. Else the code is its own lemma. |
| language.greek_prefix | "G" | a strong starting with this is Greek; else Hebrew |
| registry.strip_ends_pattern | "[^A-Za-z]" | on entry, strip runs of these from BOTH ends of the word ('[hypocrisy]' -> 'hypocrisy'); internal hyphens/spaces kept. Word matching is case-insensitive. |
| report.sample_verses | 3 | how many sample verses to show the span layer for |
| report.show_verse_text | true | show the verse's plain text above its spans |
| report.show_validation | true | show the validation results (util.validation) for the word |
| report.strong_fields | ["stepGloss", "accentedUnicode", "stepTransliteration", "head", "count", "verses"] | which columns the L1->L2 strong table shows |
| report.span_fields | ["position", "surface", "strong_variant", "morph_code", "is_particle", "sense"] | which columns the span table shows |
| step.span_html | "<span[^>]*\\bmorph='([^']*)'[^>]*\\bstrong='([^']*)'[^>]*>([^<]*)</span>" | how STEP formats an interlinear span in a verse preview: (morph, strong, surface). The forward-walk and the span parse read it. |

## cfg_status_flow

- Columns: 4
- Rows: 5

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | entity | TEXT | 0 |  | 1 |
| 1 | status | TEXT | 0 |  | 2 |
| 2 | set_by | TEXT | 0 |  | 0 |
| 3 | ordinal | INTEGER | 0 |  | 0 |

Data rows:

| entity | status | set_by | ordinal |
|---|---|---|---|
| word | proposed | registry (on new word, before approval) | 0 |
| word | approved | registry.create | 1 |
| word | raw-complete | raw.write | 2 |
| word | signed-off | registry.signoff (not in this slice) | 3 |
| word | rejected | escalation (researcher declines) | 4 |

## cfg_step

- Columns: 6
- Rows: 7

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | work_package | TEXT | 0 |  | 1 |
| 1 | ordinal | INTEGER | 0 |  | 0 |
| 2 | step | TEXT | 0 |  | 2 |
| 3 | handler | TEXT | 0 |  | 0 |
| 4 | scope | TEXT | 0 |  | 0 |
| 5 | does | TEXT | 0 |  | 0 |

Data rows:

| work_package | ordinal | step | handler | scope | does |
|---|---|---|---|---|---|
| new-word | 0 | registry.exists | iba.app.handlers.registry:exists | word | stop if the word already exists (a refresh run handles that) |
| new-word | 1 | registry.create | iba.app.handlers.registry:create | word | create the word, status proposed->approved |
| new-word | 2 | raw.discover | iba.app.handlers.raw:discover | word | CALL 1 meanings= -> word_strong (the seed strongs) |
| new-word | 3 | raw.detail | iba.app.handlers.raw:detail | word | CALL 2 getInfo per strong -> strong + sense + tree + lexicon (the meaning) |
| new-word | 4 | raw.verses | iba.app.handlers.raw:verses | word | CALL 3 per strong -> strong_verse + verse + span (span parsed from preview) |
| new-word | 5 | raw.write | iba.app.handlers.raw:write | word | commit; mark raw-complete |
| new-word | 6 | raw.validate | iba.app.handlers.raw:validate | word | the parse-check: span vs strong_verse must agree |

## cfg_table

- Columns: 3
- Rows: 12

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | name | TEXT | 0 |  | 1 |
| 1 | grain | TEXT | 0 |  | 0 |
| 2 | use | TEXT | 0 |  | 0 |

Data rows:

| name | grain | use |
|---|---|---|
| word_registry | one row per English inner-being word | the study's entry point; scope of a new-word run |
| word_strong | one row per (word, strong) the STEP word-search returned | L1 — the discovery record: which strongs a word maps to. These strongs are the basis for L2. Carries the link only, no strong detail. |
| strong | one row per strong — unique, global to the study | L2 — the strong's identity. The meaning is normalised out (O4): it lives in strong_sense / strong_meaning_tree / strong_lexicon. |
| strong_sense | one row per strong — the sense HEAD | the span's meaning, read constantly. The head is the first line of mediumDef (the sense); is_own_lemma marks a code that is its own lemma, where the gloss carries the sense. |
| strong_meaning_tree | one row per sense-node of a LEMMA's definition tree | the lemma's full range — read rarely, only when the broader context is needed. Keyed on the lemma (shared across its senses, which the prototype proved). |
| strong_lexicon | one row per strong that has LSJ/Mounce (Greek) | the large lexicon text — separate because rarely scanned |
| verse | one row per verse — unique. Does NOT belong to a strong. | L3 — the addressable verse. preview is the full interlinear, kept verbatim so span is re-derivable. |
| strong_verse | one row per (strong, verse) — unique. The m:m index. | the source's assertion 'this strong is in this verse'. The check side against span (what the parse found). |
| span | ONE ROW PER CODE of a verse (O3) — particles get their own row | L4a — SOURCE, immutable. A parse of verse.preview. position is the running code index; (verse, position) is the key. |
| run | one row per work-package run — the control record | what ran, pinned to a config version, and RESUMABLE (O7): state + resume_point persisted so a pause survives the process. |
| validation_result | one row per check a validate step ran | util.validation — the outcome of a check, persisted so it can be inspected and reported. A passed check is a recorded fact, not just an advancing run. |
| escalation | one row per researcher interaction — the pause | the only sanctioned researcher interaction. A pause, not a fork: the run resumes at resume_point when answered. |

## cfg_unique

- Columns: 3
- Rows: 6

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | table_name | TEXT | 0 |  | 1 |
| 1 | col | TEXT | 0 |  | 2 |
| 2 | ordinal | INTEGER | 0 |  | 0 |

Data rows:

| table_name | col | ordinal |
|---|---|---|
| word_strong | word_id | 0 |
| word_strong | strong | 1 |
| strong_verse | strong | 0 |
| strong_verse | verse_id | 1 |
| span | verse_id | 0 |
| span | position | 1 |

## cfg_work_package

- Columns: 3
- Rows: 1

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | name | TEXT | 0 |  | 1 |
| 1 | ps_script | TEXT | 0 |  | 0 |
| 2 | runs_over | TEXT | 0 |  | 0 |

Data rows:

| name | ps_script | runs_over |
|---|---|---|
| new-word | iba/app/ps/New-Word.ps1 | word |

## cfg_write_grant

- Columns: 2
- Rows: 17

Schema columns:

| cid | name | type | notnull | default | pk_ordinal |
|---|---|---|---|---|---|
| 0 | writer | TEXT | 0 |  | 1 |
| 1 | table_name | TEXT | 0 |  | 2 |

Data rows:

| writer | table_name |
|---|---|
| call1_meanings | word_strong |
| call2_getInfo | strong |
| call2_getInfo | strong_sense |
| call2_getInfo | strong_meaning_tree |
| call2_getInfo | strong_lexicon |
| call3_strong | strong_verse |
| call3_strong | verse |
| call3_strong | span |
| registry.create | word_registry |
| registry.create | escalation |
| raw.write | word_registry |
| raw.validate | validation_result |
| run | run |
| run | escalation |
| run | word_registry |
| escalation | escalation |
| escalation | word_registry |

