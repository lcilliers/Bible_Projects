# #2484 — Node surface against verse_lexical surface: findings

Read-only check, 2026-11-12, iba/app/db/iba.db. Nothing changed. Asked by the researcher: are many node surfaces no longer matching the verse_lexical surface?

## What I read first (B:123)

- `ib_node.surface`: "was span_surface -- matches span.surface".
- `verse_lexical.surface`: the English that belongs to this code (#2381, 2026-11-07): its own word, or for an affix code its own STEP gloss. `unit_surface` is the whole unit's rendering. `surface_kind`: `own`, `shared` (a content code of a unit with two or more content codes whose word could not be found: surface is the unit's rendering and the owner is not decided) or `gloss`.
- `ib_node.verse_lexical_id`: the occurrence the node reads; NULL until #2296 fills it.

Comparison is lower-cased and trimmed, on live nodes (`deleted = 0`).

## Result 1: nodes linked to a verse_lexical row (63,371)

| node surface against its verse_lexical row | nodes |
|---|---|
| equals `verse_lexical.surface` | 63,370 |
| node surface empty (node 49716, kind `shared`) | 1 |
| different, partial, or equal to `unit_surface` only | 0 |

Strong's code differs between node and its verse_lexical row in 0 of 63,371. No linked row points at a deleted verse_lexical row. By node creation month (2026-09: 12,431; 2026-10: 43,201; 2026-11: 7,739), mismatches are 0 in each.

By `surface_kind` of the linked row: own 59,026, shared 4,281, gloss 63, plus the one empty node.

## Result 2: nodes with no verse_lexical_id (14,728)

Tested by verse (`ib_node.verse_reference` to `verse.osisId`) and Strong's code against live verse_lexical rows:

| group | nodes |
|---|---|
| no Strong's code (question and cluster-level nodes) | 10,177 |
| surface equals the own surface of a verse_lexical row at that verse and code | 4,503 |
| no verse_reference | 46 |
| surface equals the unit surface only (node 11600, 'these', H9010, Ezra.6.8) | 1 |
| no surface (node 36374, H6586, 2Kgs.8.22) | 1 |
| different surface at a matching verse and code | 0 |

For the 4,503, a row exists at that verse and code with the same surface; where a verse holds the code more than once I did not decide which occurrence the node reads. That is the #2485 fill.

## What this means

The suspicion is not borne out in this data: no node whose verse and code can be tested carries a surface that disagrees with verse_lexical. Limits of the check:
- It tests agreement now, not whether the node surface was ever the old span surface. Equal to the whole table suggests the node surfaces were taken from, or re-synced with, verse_lexical; I did not look for how.
- 10,177 + 46 nodes have no Strong's code or verse and cannot be tested this way.

For #2484 (design D1): 4,282 linked nodes read a `shared` row, where the surface is the unit's rendering and the owning word is not decided (for example 'diligence' on a unit of 3 codes). Of these, 4,255 have a `surface_term` row and 274 are multi-word. Mapping these through their surface to a collection is therefore less certain than for `own` rows (58,657 of 59,026 have a `surface_term` row). Mapping through the verse_lexical row's Strong's code is an alternative the design can weigh.
