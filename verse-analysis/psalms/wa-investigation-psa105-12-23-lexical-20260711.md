# Lexical analysis — Psa 105:12 and 105:23 (investigation)

> Generated 2026-07-11 from `database/bible_research.db` (schema 3.40.0). Full `ve_lexical` ledger for every span in each verse, exactly as stored.

## Psa 105:12

- **verse_id** 23789 · **passage_id** `None` · **genre** `poetic/wisdom` · **process_marker** `reread-psalms-2026`
- **text:** *Psa 105:12 When they were few in number, of little account, and sojourners in it,*

### span 307353 · `When` · [H9003] · role=**None**
*(no ve_lexical rows)*

### span 307354 · `were` · [H1961] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | were |  |  |  |
| 102 | type | value | action |  |  |  |
| 106 | operation | event | were |  |  |  |
| 115 | role | value | standalone |  |  |  |

### span 307355 · `few` · [H4962] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | few (mat) |  |  |  |
| 114 | discovery | note | v12: 'When they were FEW (mat) in number' - the smallness of the patriarchs, image (char sojourners, 307358). Standalone. |  |  |  |
| 115 | role | value | standalone |  |  |  |

### span 307356 · `number` · [H4557] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | number (mispar) |  |  |  |
| 114 | discovery | note | v12: 'few in NUMBER (mispar)' - the small count, image. Standalone. |  |  |  |
| 115 | role | value | standalone |  |  |  |

### span 307357 · `little account` · [H4592] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | little account |  |  |  |
| 102 | type | value | status |  |  |  |
| 106 | operation | event | (qualifies) sojourners |  | H1481@Psa 105:12 |  |
| 108 | manner | pair | manner-of sojourners | H4592 | H1481@Psa 105:12 | span |
| 112 | coupling | pair | welds sojourners | H4592 | H1481 | span |
| 115 | role | value | standalone |  |  |  |

### span 307358 · `sojourners` · [H1481] · role=**characteristic**
_char_candidate=1 (`READ-EMERGENT-2026`) · master.characteristic=`sojourners (gur)` · ib_char_id=63_

| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | sojourners (gur) |  |  |  |
| 102 | type | value | status |  |  |  |
| 104 | seat | flag | none |  |  | none |
| 105 | bearer | flag | the patriarchs |  | 307358 | inferred |
| 106 | operation | event | be sojourners / strangers |  |  |  |
| 107 | target | flag | in the land |  | 307358 | inferred |
| 108 | manner | flag | none |  |  | none |
| 112 | coupling | flag | internal:ib-state |  | 307358 | inferred |
| 114 | discovery | note | v12: 'When they were few in number, and SOJOURNERS (gur) in it' - the pilgrim status of the patriarchs, strangers in the land of promise. |  |  |  |
| 115 | role | value | characteristic |  |  |  |
| 116 | locus | value | paired with being few in number |  |  |  |

### span 307359 · `it` · [H9003] · role=**None**
*(no ve_lexical rows)*

## Psa 105:23

- **verse_id** 23793 · **passage_id** `None` · **genre** `poetic/wisdom` · **process_marker** `reread-psalms-2026`
- **text:** *Psa 105:23 Then Israel came to Egypt; Jacob sojourned in the land of Ham.*

### span 307382 · `Israel` · [H3478] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | Israel |  |  |  |
| 102 | type | value | status |  |  |  |
| 115 | role | value | standalone |  |  |  |

### span 307383 · `came` · [H0935] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | came (bo) |  |  |  |
| 114 | discovery | note | v23: 'Then Israel CAME (bo) to Egypt' - Israel's entry into Egypt, event. Standalone. |  |  |  |
| 115 | role | value | standalone |  |  |  |

### span 307384 · `Egypt` · [H4714] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | Egypt |  |  |  |
| 102 | type | value | status |  |  |  |
| 105 | bearer | pair | Israel | H3478 | H4714 | span |
| 114 | discovery | note | bearer unreliable (nearest-proper heuristic; subject-agreement not parsed) |  |  |  |
| 115 | role | value | standalone |  |  |  |
| 116 | locus |  | external:proper |  |  |  |

### span 307385 · `Jacob` · [H3290] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | Jacob |  |  |  |
| 102 | type | value | status |  |  |  |
| 105 | bearer | pair | Egypt | H4714 | H3290 | span |
| 114 | discovery | note | bearer unreliable (nearest-proper heuristic; subject-agreement not parsed) |  |  |  |
| 115 | role | value | standalone |  |  |  |
| 116 | locus |  | external:proper |  |  |  |

### span 307386 · `sojourned` · [H1481] · role=**characteristic**
_char_candidate=1 (`READ-EMERGENT-2026`) · master.characteristic=`sojourn (gur)` · ib_char_id=63_

| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | sojourn (gur) |  |  |  |
| 102 | type | value | status |  |  |  |
| 104 | seat | flag | none |  |  | none |
| 105 | bearer | flag | Israel/Jacob |  | 307386 | inferred |
| 106 | operation | event | sojourn as a stranger |  |  |  |
| 107 | target | flag | in the land of Ham |  | 307386 | inferred |
| 108 | manner | flag | none |  |  | none |
| 112 | coupling | flag | internal:ib-state |  | 307386 | inferred |
| 114 | discovery | note | v23: 'Jacob SOJOURNED (gur) in the land of Ham' - Israel a stranger in Egypt, the sojourning renewed a generation on. |  |  |  |
| 115 | role | value | characteristic |  |  |  |
| 116 | locus | value | paired with the patriarch-sojourners (v12) |  |  |  |

### span 307387 · `land` · [H0776] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | land |  |  |  |
| 102 | type | value | status |  |  |  |
| 105 | bearer | pair | Jacob | H3290 | H0776 | span |
| 106 | operation | event | (qualifies) sojourned |  | H1481@Psa 105:23 |  |
| 108 | manner | pair | manner-of sojourned | H0776 | H1481@Psa 105:23 | span |
| 110 | specifier | pair | of Ham | H0776 | H2526 | span |
| 112 | coupling | pair | welds sojourned | H0776 | H1481 | span |
| 114 | discovery | note | bearer unreliable (nearest-proper heuristic; subject-agreement not parsed) |  |  |  |
| 115 | role | value | standalone |  |  |  |
| 116 | locus |  | external:thing |  |  |  |

### span 307388 · `Ham` · [H2526] · role=**standalone**
| ve_nr | label | kind | value | from | to | res |
|---|---|---|---|---|---|---|
| 101 | sense | value | Ham |  |  |  |
| 102 | type | value | status |  |  |  |
| 105 | bearer | pair | Jacob | H3290 | H2526 | span |
| 114 | discovery | note | bearer unreliable (nearest-proper heuristic; subject-agreement not parsed) |  |  |  |
| 115 | role | value | standalone |  |  |  |
| 116 | locus |  | external:proper |  |  |  |

---

## Master records + ib_characteristic (added on request)

### Psa 105:12

**A. Master index — full `verse_span_index` records for this verse**

| id | verse_id | reference | word_index | surface | pos | morph_code | stem | language | strongs | primary_strong | source | built_at | role | role_provenance | role_set_at | role_source_ve_id | char_candidate | char_candidate_tag | characteristic | ib_char_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 307353 | 23789 | Psa 105:12 | 0 | When | preposition | HR |  | Hebrew | H9003 | H9003 | verse_morphology | 2026-07-02 19:43:27 |  |  |  |  |  |  |  |  |
| 307354 | 23789 | Psa 105:12 | 1 | were | verb | HVqcc | Qal | Hebrew | H1961 | H1961 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294546 |  |  |  |  |
| 307355 | 23789 | Psa 105:12 | 2 | few | noun | HNcmpc HSp3mp |  | Hebrew | H4962 H9048 | H4962 | verse_morphology | 2026-07-02 19:43:27 | standalone | read-2026 | 2026-07-10T15:28:49Z | 7674438 |  |  |  |  |
| 307356 | 23789 | Psa 105:12 | 3 | number | noun | HNcmsa |  | Hebrew | H4557 | H4557 | verse_morphology | 2026-07-02 19:43:27 | standalone | read-2026 | 2026-07-10T15:28:49Z | 7674441 |  |  |  |  |
| 307357 | 23789 | Psa 105:12 | 4 | little account | noun | HNcmsa HR |  | Hebrew | H4592 H9004 | H4592 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294559 |  |  |  |  |
| 307358 | 23789 | Psa 105:12 | 5 | sojourners | verb | HVqrmpa | Qal | Hebrew | H1481A | H1481 | verse_morphology | 2026-07-02 19:43:27 | characteristic | read-2026 | 2026-07-10T15:28:49Z | 7674016 | 1 | READ-EMERGENT-2026 | sojourners (gur) | 63 |
| 307359 | 23789 | Psa 105:12 | 6 | it | preposition | HR HSp3fs |  | Hebrew | H9003 H9034 | H9003 | verse_morphology | 2026-07-02 19:43:27 |  |  |  |  |  |  |  |  |

**B. Verse-records — `wa_verse_records` rows for this verse** (the term↔verse↔span master-index links)

| id | term_id | term_inv_id | mti_term_id | reference | verse_id | verse_span_id | target_word | span_strong_match | transliteration | analysis_marker | delete_flagged |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 244719 | H4592 | 1480 | 1335 | Psa 105:12 | 23789 | 307357 | little account | 1 | me.at |  | 0 |
| 244720 | H1481 | 234 | 290 | Psa 105:12 | 23789 | 307358 | sojourners | 1 | gur |  | 0 |

### Psa 105:23

**A. Master index — full `verse_span_index` records for this verse**

| id | verse_id | reference | word_index | surface | pos | morph_code | stem | language | strongs | primary_strong | source | built_at | role | role_provenance | role_set_at | role_source_ve_id | char_candidate | char_candidate_tag | characteristic | ib_char_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 307382 | 23793 | Psa 105:23 | 0 | Israel | noun | HNpl |  | Hebrew | H3478 | H3478 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294820 |  |  |  |  |
| 307383 | 23793 | Psa 105:23 | 1 | came | verb | HVqw3ms | Qal | Hebrew | H0935G | H0935 | verse_morphology | 2026-07-02 19:43:27 | standalone | read-2026 | 2026-07-10T15:28:49Z | 7674513 |  |  |  |  |
| 307384 | 23793 | Psa 105:23 | 2 | Egypt | noun | HNpl |  | Hebrew | H4714G | H4714 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294831 |  |  |  |  |
| 307385 | 23793 | Psa 105:23 | 3 | Jacob | noun | HNpm HC |  | Hebrew | H3290 H9002 | H3290 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294836 |  |  |  |  |
| 307386 | 23793 | Psa 105:23 | 4 | sojourned | verb | HVqp3ms | Qal | Hebrew | H1481A | H1481 | verse_morphology | 2026-07-02 19:43:27 | characteristic | read-2026 | 2026-07-10T15:28:49Z | 7674027 | 1 | READ-EMERGENT-2026 | sojourn (gur) | 63 |
| 307387 | 23793 | Psa 105:23 | 5 | land | noun | HNcfsc HR |  | Hebrew | H0776G H9003 | H0776 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294851 |  |  |  |  |
| 307388 | 23793 | Psa 105:23 | 6 | Ham | noun | HNpl |  | Hebrew | H2526H | H2526 | verse_morphology | 2026-07-02 19:43:27 | standalone | role-reassess-2026 | 2026-07-07T17:08:34Z | 7294856 |  |  |  |  |

**B. Verse-records — `wa_verse_records` rows for this verse** (the term↔verse↔span master-index links)

| id | term_id | term_inv_id | mti_term_id | reference | verse_id | verse_span_id | target_word | span_strong_match | transliteration | analysis_marker | delete_flagged |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 244724 | H0935 | 1488 | 1340 | Psa 105:23 | 23793 | 307383 | came | 1 | bo |  | 0 |
| 244725 | H1481 | 234 | 290 | Psa 105:23 | 23793 | 307386 | sojourned | 1 | gur |  | 0 |

### C. `ib_characteristic` record(s) referenced by these spans

Both verses' characteristic span (H1481 gur) links to `ib_char_id` = [63].

**ib_characteristic id=63:**

| column | value |
|---|---|
| id | 63 |
| code | psa-H1481 |
| name | sojourn (gur) |
| aka |  |
| family |  |
| status | surfaced |
| books |  |
| gist |  |
| colour_range |  |
| junctions |  |
| open_questions |  |
| discovery_doc |  |
| provenance | ib-char-index-v2-reread-2026 |
| created_at | 2026-07-11T07:48:30Z |
| updated_at | 2026-07-11T07:48:30Z |
| char_key | H1481 |
| key_word | sojourn (gur) |
| key_span_id | 280298 |
| operation | band together / stir up |
| ledger | sojourn (gur) [H1481] — 6 occurrence(s) in book 19. Type(s): action, state, status. Senses read: dwell / sojourn (gur - let me dwell in your tent); sojourn (gur); sojourners (gur); stir up strife / band together (gur - stir up strife against me); stir up strife / band together (gur - they stir up strife). Representative operation: band together / stir up |
| instance_count | 6 |
| book_scope | 19 |

_Spans linked to this record (whole DB): 6._
