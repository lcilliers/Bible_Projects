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
