# CC Directive — Registry 068 Grace — Root Family Records: H2587, H2603A, H8467
**File:** wa-068-grace-sessionB-cc-directive-v4-2026-04-10.md
**Date:** 2026-04-10
**From:** Claude AI — Session B Stage 1 — Gap 6, 7, 8
**Registry:** 068 — grace
**Source export:** wa-068-grace-complete-2026-04-10.json

---

## What this directive covers

Three active XREF terms in Reg 068 are missing root_family records for the CHEN root. Two existing active terms in this registry (H2580 chen and H8469 ta.cha.nun) already carry CHEN root_family records. The three terms below share the same Hebrew root and must be brought into consistency.

**Note:** Claude AI is responsible for determining the correct root assignments and specifying the insertions. CC is responsible for applying them to the database. CC does not determine root assignments.

---

## Etymology — why CHEN is correct for all three

All three terms derive from the primary Hebrew root חנן (chanan — to be gracious, to show favour):

- **H2587 chan.nun** — adjective meaning *gracious*. Direct adjectival form of the chanan verb root.
- **H2603A cha.nan** — verb meaning *to be gracious, to show favour*. This is the primary verb of the CHEN root family — the root itself.
- **H8467 te.chin.nah** — feminine noun meaning *supplication, plea for grace*. Derived noun from chanan, naming the act of seeking grace.

These three terms, together with H2580 chen (noun — favour, grace) and H8469 ta.cha.nun (noun — supplication, pleas for mercy), form a single coherent Hebrew root family: the chen/chanan cluster. All five belong to root_code=CHEN.

---

## Operations required

Insert three records into `wa_term_root_family`. Model each insertion on the existing CHEN records (ids 1361 and 1362) as the reference pattern.

**Insertion 1 — H2587 (chan.nun)**
- term_inv_id = 5589
- root_code = 'CHEN'
- root_language = 'Hebrew'
- root_gloss = 'favor'
- note = 'Added 2026-04-10 Session B Stage 1 audit — etymological member of chen/chanan root family'
- delete_flagged = 0

**Insertion 2 — H2603A (cha.nan)**
- term_inv_id = 5586
- root_code = 'CHEN'
- root_language = 'Hebrew'
- root_gloss = 'favor'
- note = 'Added 2026-04-10 Session B Stage 1 audit — primary verb of the chen/chanan root family'
- delete_flagged = 0

**Insertion 3 — H8467 (te.chin.nah)**
- term_inv_id = 5588
- root_code = 'CHEN'
- root_language = 'Hebrew'
- root_gloss = 'favor'
- note = 'Added 2026-04-10 Session B Stage 1 audit — etymological member of chen/chanan root family'
- delete_flagged = 0

---

## Expected state after application

Five Hebrew terms in Reg 068 will carry CHEN root_family records:

| Strong | Transliteration | term_inv_id | CHEN record |
|---|---|---|---|
| H2580 | chen | 928 | existing (id=1361) |
| H8469 | ta.cha.nun | (existing) | existing (id=1362) |
| H2587 | chan.nun | 5589 | new |
| H2603A | cha.nan | 5586 | new |
| H8467 | te.chin.nah | 5588 | new |

Note: H2594 and H2600, reinstated in Directive v2, also belong to the CHEN root family. Their root_family records will be addressed in a subsequent directive once the reinstated terms are confirmed stable.

---

## Reporting required

Confirm:
1. Three records inserted successfully with correct term_inv_id values
2. No duplicate records created (check that no CHEN record already existed for these term_inv_ids before insertion)
3. root_family_count in statistics updated if the extract script recalculates it — report the new value

Do not produce a fresh export yet.
