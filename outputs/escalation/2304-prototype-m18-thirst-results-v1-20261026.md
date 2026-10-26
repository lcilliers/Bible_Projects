# #2304 Prototype results (v1): the reading cycle on one JSON, on M18_thirst

Date: 2026-10-26. Escalation #2304. Design: `outputs/escalation/2304-reading-cycle-one-json-design-v3-20261026.md`.
Ruled: D1 to D5 and D7 b (#2304 v3 to v5). Run on a backup-API copy of `iba/app/db/iba.db` by
`iba/app/tools/temp_2304_reading_cycle_prototype.py`. **Nothing live was written, and Reading.ps1 is not changed.**

## 1. The files, as each step leaves them

The cycle writes one file; here it is kept after each step so each step can be seen. On the copy the file sat in
`M18 - desire-longing/` as D2 rules; these are review copies.

| step | file (`outputs/escalation/2304-prototype/`) | size |
|---|---|---|
| a) 0.C scope | `2304-m18-thirst-a-scope-v1-20261026.json` | 178 KB |
| b) 0.GAP pre, gathered | `2304-m18-thirst-b-gathered-v1-20261026.json` | 615 KB |
| c) observe, slots to fill | `2304-m18-thirst-c-observe-v1-20261026.json` | 722 KB |
| c) the same, filled for the test | `2304-m18-thirst-c-observe-filled-v1-20261026.json` | 751 KB |

## 2. What each step gave

**a) 0.C.** `M18_thirst`: 42 verses, 44 occurrences in the home. The verses also hold 73 occurrences of other
subgroups (54 subgroups), shown and not in scope, and 729 other clustered words as context.

**b) 0.GAP pre.** Per verse: text, passage, `verse_lexical` by occurrence, observations with their nodes, cluster
document lines, open items.

| what was gathered | count |
|---|---|
| live observations with a node on these verses | 28 |
| of them, with a node on one of the 44 home occurrences | **0** |
| nodes that match several occurrences | 0 |
| cluster document lines naming a verse (175 references, 146 lines in 32 files) | 146 |
| of them already imported into `ib_observation` | 7 |
| open items related to the scope | 3 |

The 28 existing observations all sit on other words in these verses (the soul, seek, living). **Correction to design
v3 section 3:** it said 4 nodes fall on the home occurrences; those 4 belong to withdrawn observations, so no live one
does.

The document lines by kind: 51 bullets, 43 headings, 41 table rows, 11 paragraphs. 141 of the 146 lines have distinct
text; the worksheets repeat a few lines.

The 3 open items: `OT-105.10` and `OT-106.7` (the poor, matched on Isa 41:17), `OT-108.8` (matched on cluster M18).
All three reach past the scope, so they can be read in part.

**c) Observe.** 361 slots: 44 home occurrences, 168 qualifiers, 146 document lines, 3 open items.

**Record**, run twice on the copy:
1. With only my two adoptions and one reason filled: **refused, nothing written**, listing every unfilled slot.
2. With every slot filled (the two adoptions; the other slots given test reasons, and the three items a `touched`
   response marked as a test): written in one transaction:
   - observations 12535 and 12536, kind `statement`, stage `reading`, `meaning_source` the document line they adopt;
   - nodes 17316 and 17317 on `thirsts` (H6770) in Psa 42:2 and Psa 63:1, with `verse_lexical_id`, `reading_id` and
     role characteristic;
   - a response on each of the three open items;
   - the reading at state `observed`.

The two adoptions, made by reading the lines (D7 b), not by pattern:

| verse | document line | finding written |
|---|---|---|
| Psa 42:2 | `m18-m25-inner-being-reading-v1-20261009.md:224` (table row: the psalmist; "My soul thirsts for God"; God himself, as the thing thirsted for) | The soul's thirst is turned toward God himself, the living God, as the one thirsted for; the longing names its object as a person, not a gift. |
| Psa 63:1 | `m18-m47-validation-worksheet-v1-20261009.md:507` (bullet: "my soul thirsts for you; my flesh faints for you", soul and flesh together) | Soul and flesh long for God together: the soul thirsts and the flesh faints for him, so the longing is borne by the whole person, in a dry and weary land. |

## 3. What the prototype shows *(inferential where marked)*

1. **The chain works as designed:** one file, each step reading the last; the gathering writes nothing; Record writes
   all or nothing, per occurrence, with the open items answered.
2. **The existing observations do not cover the home words.** None of the 28 is on a thirst word. *(inferential)*
   The earlier readings of these verses were made from other words (the soul, seek); for this subgroup the documents,
   not the table, hold what was already read.
3. **The documents are the main source to adopt from, and they need sorting.** 43 of the 146 lines are headings that
   only name a verse, and some lines are cross-cutting notes on many verses. *(inferential)* Most of the reading
   effort of a scope run will go into the document slots.
4. **The qualifier slots are too many.** Taking every T2 or T5 word in the verse gives 168 slots against 44 home words.
   The design says "bound to the home word"; which qualifier binds to which word is itself a reading.

## 4. Points to decide before the build

| # | point | options | my recommendation *(inferential)* |
|---|---|---|---|
| P1 | Qualifier slots | a) every T2/T5 word in the verse (as now: 168); b) only the qualifiers the reading finds bound to a home word, recorded as part of that word's finding, with no slot of their own | b: the binding is read, not found by pattern, and a qualification finding already applies to both words (design v6 section 2) |
| P2 | Heading lines (43) | a) a slot each, answered with a reason; b) no slot: a heading names the verse and says nothing; it is listed but needs no answer | b |
| P3 | Lines with the same text in one file | a) a slot each; b) one slot for the text, all its lines named | b |

With these, the M18_thirst slots would fall from 361 to about 44 home words, about 98 document texts and 3 open items.
