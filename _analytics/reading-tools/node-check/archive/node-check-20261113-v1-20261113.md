# Node and observation check

Run RUN-20261113_063042_448-NODECHECK, 2026-11-13T06:30:46Z. Reads only; nothing is written to a table. Each check is a part of behaviour rules B:130 (nodes) and B:131 (observations); a finding says what is wrong or missing, not what to do. Every row is in the workbook of the same name, one sheet for each check. Candidates marked 'to be read' need a reading and are not judged here.

## Totals

| | count |
|---|---|
| live nodes | 61,473 |
| live nodes with a finding | 29,906 |
| live nodes with no finding | 31,567 |
| live observations | 14,947 |
| member surfaces | 3,437 |
| verses in scope | 24,847 |

## Findings by check

| check | rule | what it lists | count |
|---|---|---|---|
| N-no-live-observation | B:130 | live node whose observation is deleted or missing | 0 |
| N-no-surface | B:130 | live node with no surface | 74 |
| N-no-occurrence | B:130 | live node with no verse_lexical_id | 4,268 |
| N-occurrence-mismatch | B:130 | node whose surface, Strong's code, morph code or verse differs from its verse_lexical row | 0 |
| N-no-strong | B:130 | live node with a surface and no Strong's code | 0 |
| N-no-morph | B:130 | live node with a surface and no morph code | 2 |
| N-no-role | B:130 | node that names a word and has no role, or a role outside cfg_enum observation_role | 15,457 |
| N-out-of-scope | B:130 | live node on a verse that holds no member surface of a live collection | 0 |
| N-no-collection | B:130 | in-scope node with no collection (collection surface: derivable; other surface: what its observation offers) | 16,097 |
| N-collection-disagrees | B:130 | node whose collection is not the one collection of its surface, or is not a live collection | 0 |
| N-duplicate | B:130 | live node with the same indexing columns as another live node of its observation | 2,092 |
| O-no-live-node | B:131 | live observation with no live node | 63 |
| O-not-tied | B:131 | observation none of whose live nodes has a surface (malformed: not tied to a surface) | 3 |
| O-no-role-node | B:131 | observation with no node of role characteristic, qualifier or standalone | 7,414 |
| O-duplicate-text | B:131 | live observations with the same text | 42 |
| O-no-collection | B:131 | observation none of whose live nodes carries a collection (not discoverable through a collection) | 2,247 |
| O-verse-copy | B:131 | candidate, to be read: observation repeating more than max_verse_words_copied consecutive words of a verse of its nodes | 3,362 |
| O-out-of-scope | B:131 | observation all of whose live nodes are out of scope | 0 |
| C-surface-no-node | B:130 | member surface of a live collection with no live node | 1,381 |

### N-no-live-observation (B:130): 0

live node whose observation is deleted or missing

### N-no-surface (B:130): 74

live node with no surface

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 17329 | 12536 | Gen.27.33 |  |  |
| 17408 | 12549 | 1Sam.4.13 |  |  |
| 17409 | 12549 | 2Kgs.4.13 |  |  |
| 17410 | 12549 | Esth.4.4 |  |  |
| 17411 | 12549 | Ruth.3.8 |  |  |

... and 69 more in the workbook.

### N-no-occurrence (B:130): 4,268

live node with no verse_lexical_id

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 453 | 333 | 1Tim.5.13 | idlers |  |
| 454 | 334 | 1Tim.5.13 | idlers |  |
| 756 | 594 | 1Tim.5.13 | idlers |  |
| 757 | 594 | 1Tim.5.13 | idlers |  |
| 842 | 627 | 1Tim.5.13 | idlers |  |

... and 4,263 more in the workbook.

### N-occurrence-mismatch (B:130): 0

node whose surface, Strong's code, morph code or verse differs from its verse_lexical row

### N-no-strong (B:130): 0

live node with a surface and no Strong's code

### N-no-morph (B:130): 2

live node with a surface and no morph code

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 10694 | 9269 | 2Cor.8.16 | who |  |
| 11117 | 9668 | 1Tim.5.13 | what |  |

### N-no-role (B:130): 15,457

node that names a word and has no role, or a role outside cfg_enum observation_role

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 308 | 216 | 2Pet.1.8 | ineffective | no role |
| 309 | 216 | Matt.12.36 | careless | no role |
| 310 | 217 | 2Pet.1.8 | ineffective | no role |
| 311 | 218 | Matt.12.36 | careless | no role |
| 338 | 231 | 2Cor.7.11 | earnestness | no role |

... and 15,452 more in the workbook.

### N-out-of-scope (B:130): 0

live node on a verse that holds no member surface of a live collection

### N-no-collection (B:130): 16,097

in-scope node with no collection (collection surface: derivable; other surface: what its observation offers)

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 308 | 216 | 2Pet.1.8 | ineffective | supportive (other); no node of the observation carries a collection |
| 309 | 216 | Matt.12.36 | careless | supportive (other); no node of the observation carries a collection |
| 310 | 217 | 2Pet.1.8 | ineffective | supportive (other); same verse: [31] |
| 311 | 218 | Matt.12.36 | careless | supportive (other); same verse: [12, 201] |
| 452 | 332 | Jas.2.20 | useless | supportive (other); no node of the observation carries a collection |

... and 16,092 more in the workbook.

### N-collection-disagrees (B:130): 0

node whose collection is not the one collection of its surface, or is not a live collection

### N-duplicate (B:130): 2,092

live node with the same indexing columns as another live node of its observation

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 8795 | 216 | 2Pet.1.8 | ineffective | same indexing columns as node 308 |
| 9237 | 216 | 2Pet.1.8 | ineffective | same indexing columns as node 308 |
| 8794 | 216 | Matt.12.36 | careless | same indexing columns as node 309 |
| 8735 | 217 | 2Pet.1.8 | ineffective | same indexing columns as node 310 |
| 9219 | 217 | 2Pet.1.8 | ineffective | same indexing columns as node 310 |

... and 2,087 more in the workbook.

### O-no-live-node (B:131): 63

live observation with no live node

| node | observation | verse | surface | detail |
|---|---|---|---|---|
|  | 2949 |  |  | char-subgroup |
|  | 2950 |  |  | char-subgroup |
|  | 2951 |  |  | char-subgroup |
|  | 2952 |  |  | char-subgroup |
|  | 2953 |  |  | char-subgroup |

... and 58 more in the workbook.

### O-not-tied (B:131): 3

observation none of whose live nodes has a surface (malformed: not tied to a surface)

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 17408 | 12549 | 1Sam.4.13 |  | stage prior-capture; 4 node(s), none with a surface |
| 19108 | 12896 | Ezek.16.12 |  | stage prior-capture; 1 node(s), none with a surface |
| 68151 | 20314 | Josh.7.15 |  | stage prior-capture; 1 node(s), none with a surface |

### O-no-role-node (B:131): 7,414

observation with no node of role characteristic, qualifier or standalone

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 308 | 216 | 2Pet.1.8 | ineffective | stage verse-reading; roles ['None'] |
| 310 | 217 | 2Pet.1.8 | ineffective | stage verse-reading; roles ['None'] |
| 311 | 218 | Matt.12.36 | careless | stage verse-reading; roles ['None'] |
| 338 | 231 | 2Cor.7.11 | earnestness | stage verse-reading; roles ['None'] |
| 340 | 232 | 2Cor.7.11 | earnestness | stage verse-reading; roles ['None'] |

... and 7,409 more in the workbook.

### O-duplicate-text (B:131): 42

live observations with the same text

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 990 | 692 | 2Pet.2.3 | idle | same text as observation 646 |
| 9067 | 7698 | Rom.12.8 | contributes | same text as observation 7668 |
| 10197 | 8813 | Rom.12.8 | zeal | same text as observation 7668 |
| 11234 | 9776 | Rom.12.8 | generosity | same text as observation 7668 |
| 9070 | 7701 | Rom.12.8 | contributes | same text as observation 7671 |

... and 37 more in the workbook.

### O-no-collection (B:131): 2,247

observation none of whose live nodes carries a collection (not discoverable through a collection)

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 308 | 216 | 2Pet.1.8 | ineffective | stage verse-reading; 5 node(s), none with a collection |
| 452 | 332 | Jas.2.20 | useless | stage verse-reading; 1 node(s), none with a collection |
| 453 | 333 | 1Tim.5.13 | idlers | stage verse-reading; 3 node(s), none with a collection |
| 454 | 334 | 1Tim.5.13 | idlers | stage verse-reading; 3 node(s), none with a collection |
| 458 | 338 | Jas.2.20 | useless | stage verse-reading; 1 node(s), none with a collection |

... and 2,242 more in the workbook.

### O-verse-copy (B:131): 3,362

candidate, to be read: observation repeating more than max_verse_words_copied consecutive words of a verse of its nodes

| node | observation | verse | surface | detail |
|---|---|---|---|---|
| 1240 | 820 | 2Cor.7.11 | earnestness | repeats more than 7 consecutive words of 2Cor.7.11 |
| 1275 | 836 | Ezra.6.12 | diligence | repeats more than 7 consecutive words of Ezra.6.12 |
| 1280 | 838 | Ezra.7.26 | strictly | repeats more than 7 consecutive words of Ezra.7.26 |
| 1303 | 852 | Ezra.7.23 | full | repeats more than 7 consecutive words of Ezra.7.23 |
| 1307 | 856 | Ezra.6.13 | diligence | repeats more than 7 consecutive words of Ezra.6.13 |

... and 3,357 more in the workbook.

### O-out-of-scope (B:131): 0

observation all of whose live nodes are out of scope

### C-surface-no-node (B:130): 1,381

member surface of a live collection with no live node

| node | observation | verse | surface | detail |
|---|---|---|---|---|
|  |  |  | a sinner | collection sin |
|  |  |  | abiding | collection endure |
|  |  |  | able-bodied | collection skill |
|  |  |  | abundantly | collection rich |
|  |  |  | accept circumcision | collection reject |

... and 1,376 more in the workbook.
