# Psalms DB — grounded current state + integrity findings (2026-07-11)

> Every figure below is a query result run this session against `database/bible_research.db`, not memory or inference. Written after two overstatements were caught: (1) reporting ledger-clean as "full integrity"; (2) claiming a filed doc that was never written. This is the corrected, verifiable record.

## 1. The corrected reread footprint (verified)
- Psalms verses: **2,461**; marked `process_marker='reread-psalms-2026'`: **2,420**; with a `passage_id`: **2,254**; distinct passages: **314**.
- Spans total: **19,657**; `role='characteristic'` under `read-2026`: **2,168**.
- `ve_lexical` rows `source_provenance='reread-psalms-2026'` (active): **48,225**.
- Ledger dimensions present: 101 sense, 102 type, 103 source, 104 seat, 105 bearer, 106 operation, 107 target, 108 manner, 112 coupling, 113 prohibition, 114 discovery, 115 role, 116 locus.
- `role_source_ve_id` on every char-span → its own ve_nr=115 (role) row (2,168/2,168). Internal span↔ledger link only.

## 2. Named-characteristic registries EXIST (correcting an earlier false claim)
- `ib_characteristic`: **29 rows**, 28 tagged `Psa`; provenance `ib-characteristic-registry-v1-20260703` (built **before** the corrected reread). Fields: code, name, colour_range, junctions, open_questions, discovery_doc.
- `characteristic`: **277 rows**, 35 cluster codes (M-code model, 2026-05-18).

## 3. INTEGRITY GAPS (why the DB is NOT at full integrity)
Checks on the 2,168 reread characteristic spans, against per-book method step (e) ("no orphans; forward and backward tracking intact; indexed"):

| check | result | verdict |
|---|--:|---|
| char-spans in a verse with **no passage_id** | **18** | forward link (span→passage) broken |
| char-spans with **no `wa_verse_records`** pointing to them | **261** | **master-index backward orphan** — violates the project invariant |
| char-spans with no active `ve_lexical` ledger | 0 | ledger OK (this is what step-c gates checked) |
| char-spans whose record has NULL `mti_term_id` | 0 | term link OK where a record exists |
| reread char-spans linked to `ib_characteristic`/`characteristic` | **0** | characteristic layer entirely disconnected |

### What this means
- **261 / 2,168 (12%) characteristics cannot be tracked back from the master index.** By the project's own rule (*a char span with no verse-record = a DB integrity violation, repair first*), the DB is not at full integrity.
- **18 characteristics have no passage** — the passage layer (2,254/2,461 verses) is itself incomplete, and these spans fall in the gap.
- **The 2,168 instances are not connected to any named characteristic.** The `ib_characteristic` registry (28 Psa entries) was built from the *old* read and is not linked to the corrected read; the corrected read has no characteristic-identity dimension.

## 4. Where the Psalms work actually stands against the per-book method (b→c→d→e)
- **(c) role/lexical read — DONE and ledger-clean.** This is what was completed and verified.
- **(d) Gate-1 completeness (term recorded, verses pulled, links built — a STEP action) — NOT done.** The 261 master-index orphans are exactly what (d) exists to resolve.
- **(e) book-close full integrity (no orphans, tracking intact) — NOT done.** Proven by items in §3.

## 5. Correction of prior statements
- "0 defects / full integrity" (this session, repeatedly) was scoped **only** to the ledger (G10/God-bearer/pairs/coverage). It was **not** full integrity. Overstated.
- The claim (previous turn) that a grounded-state doc had been filed was **false** — no such file existed. This doc replaces that claim with an actual, verifiable file.

*Filed 2026-07-11. All figures reproducible from the queries in this session.*
