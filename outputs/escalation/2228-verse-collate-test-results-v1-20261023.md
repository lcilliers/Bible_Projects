# 2228 — Collating a scope: test results (v1)

Escalation #2228 tools 3-5 (outputs/escalation/2228-verse-collate-design-v1-20261023.md). Run 2026-10-23 by iba/app/tools/temp_2228_verse_collate_test_run.py on a copy of iba.db (lib/dbsnapshot.copy_db) with the #2228 migrations and the reading index built on the copy from the live files (read-only on the files); expected values by plain SQL on the copy. Result: 14/14 PASS.

| # | case | result | evidence | s |
|---|---|---|---|---|
| C0 | migrations applied (or already), then skipped | PASS | ['already applied -- 0 write(s); tables to create: []', 'already applied -- 0 write(s); tables to create: []', 'already applied -- 0 write(s)', 'already applied -- 0 write(s)'] |  |
| C1 | M02 -OnlyStrong H3708A (22 verses): per verse, observations, strand hits, claims, citing blocks and file lines equal plain SQL | PASS | {'obs': (47, 47), 'hits': (33, 33), 'claims': (0, 0), 'blocks': (29, 29), 'lines': (351, 351)} | 0.6 |
| C2 | every extracted file line is the line that names the verse (holds the reference as written) | PASS | 351 lines; odd [] |  |
| C3 | the gaps follow their rules for every verse; the totals equal the per-verse gaps | PASS | {'not read': 0, 'read in files only': 0, 'hit unread': 0, 'observed, no claim': 22, 'claim not told': 0, 'open item': 22, 'meaning missing': 0}; off [] |  |
| C4 | Ecc 7:9: observation 12478 and the anger strand's faced hits are collated | PASS | {'obs': [11924, 11956, 12141, 12467, 12478], 'hits': [('anger', True), ('anger', True)]} |  |
| C5 | -Verse "Eze 20:11" (an open thread item's verse): the item is collated as an open item | PASS | [{'item': 'OT-01.2', 'kind': 'cluster', 'value': 'M12', 'matched_on': 'M12', 'note': None}, {'item': 'OT-01.3', 'kind': 'verse', 'value': 'Eze 20:11', 'matched_on': 'Eze 20:11', 'note': 'named in the thread'}, {'item': 'OT-05.25', 'kind': 'cluster', 'value': 'M15', 'matched_on': 'M15', 'note': "A6 natural against spiritual: psychikos (G5591) is tagged M15; 1Co 2:14 'does not accept the things of t | 0.3 |
| C6 | -Verse "Jam 3:5" (holds G6094, an M-cluster Greek word with no Mounce entry, #2205): 'meaning missing' | PASS | ['not read', 'read in files only', 'open item', 'meaning missing'] | 0.3 |
| C7 | the lexicon has an entry for every inner-being word in the scope | PASS | [] |  |
| C8 | -Thread OT-108: refused by the scope guard | PASS | the request is too wide -- verses in the result (29743 against the limit 4000); reform it to a narrower scope. Verses by selector, widest first: clust |  |
| C9 | collate time guard (max_seconds 0 on the copy): refused | PASS | collating stopped at the time limit (verse_collate.max_seconds 0) while reading the words; reform the scope to a narrower one |  |
| C10 | a cluster file changed since it was indexed is named | PASS | ['_analytics/Clusters/M01 - fear-awe/fear-cross-ledger-overview-v1-20261004.md', '_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit3-v1-20261004.md', '_analytics/Clusters/M02 - anger-wrath/anger-cross-ledger-overview-v2-20261005.md'] |  |
| C11 | through the handler: the .json and .md written; the .md gap table equals the JSON | PASS | -> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/17ac2129-4964-4787-9bc5-5c1c32d28250/scratchpad/t2228vc/out/t-anger-20261023.md
  -> C:/Users/lerouxc/AppData/Local/Temp/claude/C- |  |
| C12 | speed: M25 Life and death (2,027 verses) within the guard | PASS | {'verses': 2027, 'with_a_gap': 2027, 'observations': 1101, 'claims': 139, 'file_lines': 8035, 'open_items': 200, 'seconds': 1.5} | 1.5 |
| C13 | read-only: no row written by collating | PASS | 0 -> 0 |  |

