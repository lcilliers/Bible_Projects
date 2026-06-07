# Task 1 — mti_terms dedup: dry-run (for eyeball; HOLD execution)

> **2026-06-07 · CC. NO DB WRITE YET.** Proposed soft-delete of **56 mti_terms rows that are already
> `status='delete'` / `'candidate_delete'`** (re-doing the lost June-1 dedup). Sets `delete_flagged=1` to
> match their status — the safest possible cleanup. FLAG-cluster parked terms are untouched. Approve → I
> back up the DB, then run the UPDATE.

## A · Duplicate-group rows (delete-status; a keeper remains) — 14

| id | strongs | translit | status | cluster |
|---|---|---|---|---|
| 2038 | G3844 | para | delete | FLAG |
| 2182 | G3844 | para | delete | FLAG |
| 2377 | G3844 | para | delete | FLAG |
| 4186 | G3844 | para | candidate_delete | FLAG |
| 2704 | G4862 | sun | delete | FLAG |
| 2716 | G4862 | sun | delete | FLAG |
| 3092 | G4862 | sun | delete | FLAG |
| 3278 | G4862 | sun | delete | FLAG |
| 3882 | G4862 | sun | delete | FLAG |
| 1927 | H6031A | a.nah | delete | FLAG |
| 2486 | H6031A | a.nah | delete | FLAG |
| 2487 | H6033 | a.na | delete | FLAG |
| 2488 | H6039 | e.nut | delete | FLAG |
| 2757 | H7067G | qan.na | delete | FLAG |

## B · Ghost rows (status=delete, NULL cluster, no inventory) — 42

| id | strongs | translit |
|---|---|---|
| 41 | G3949_related | parorgismos |
| 299 | H4116A | ma.har |
| 300 | H5590 | sa.ar |
| 303 | H7200B | ra.ah |
| 346 | H6424 | pa.las |
| 557 | G0080 | adelfos |
| 702 | H0834A | a.sher |
| 732 | H0854 | et |
| 742 | H3588A | ki |
| 755 | H5921A | al |
| 768 | H1961 | ha.yah |
| 769 | H0637 | aph |
| 844 | H0518A | im |
| 870 | G1722 | en |
| 946 | H5186 | na.tah |
| 1066 | G0846 | autos |
| 1074 | G1223 | dia |
| 1076 | G2573 | kalōs |
| 1077 | G3778 | houtos |
| 1078 | G2761 | kenōs |
| 1172 | H0559 | a.mar |
| 1323 | H4932G | mish.neh |
| 1452 | H0226H | ot |
| 1453 | H0865 | et.mol |
| 1454 | H3487 | yat |
| 1456 | H0409 | al |
| 1457 | H0432 | il.lu |
| 1471 | H5921B |    |
| 1472 | H3651C | ken |
| 2358 | H7593 | she.el |
| 2382 | H6760 | tsa.la |
| 2383 | H6761 | tse.la |
| 7546 | G1643 | elaunō |
| 7547 | H3715A | ke.phir |
| 7548 | H3713A | ke.phor |
| 7549 | H3713B | ke.phor |
| 7550 | H3723H | ka.phar |
| 7551 | H3715M | ke.phi.rim |
| 7559 | H5221 | na.khah |
| 7560 | H4347 | mak.kah |
| 7561 | H5224H | ne.kho |
| 7575 | H2275H | chev.ron |

## The exact statement (run only on your go, after backup)

```sql
UPDATE mti_terms SET delete_flagged = 1 WHERE id IN (
  41,299,300,303,346,557,702,732,742,755,768,769,844,870,946,1066,1074,1076,1077,1078,
  1172,1323,1452,1453,1454,1456,1457,1471,1472,1927,2038,2182,2358,2377,2382,2383,2486,
  2487,2488,2704,2716,2757,3092,3278,3882,4186,7546,7547,7548,7549,7550,7551,7559,7560,
  7561,7575
);  -- 56 rows, all already status delete/candidate_delete
```

## Held for YOUR judgement — duplicate groups NOT in the proposal (20 groups)

These have no clear delete-status row (status `None` / `xref`), so which to keep is your call — not
auto-touched:

| strongs | rows (id:status) |
|---|---|
| G3077 | 2713:xref_sorrow, 5191:None, 6370:None |
| H0206G | 5607:None, 6366:None |
| H2256C | 6401:None, 7474:None |
| H2258A | 6407:None, 7481:None |
| H2258B | 6409:None, 7483:None |
| H2259 | 6406:None, 7480:None |
| H2260 | 6410:None, 7484:None |
| H2603B | 2436:delete, 3137:delete, 3938:delete, 5479:delete |
| H4714I | 6088:None, 6875:None |
| H4714J | 6087:None, 6874:None |
| H5796 | 7277:None, 7295:None |
| H5798G | 7046:None, 7274:None, 7292:None |
| H5808 | 6886:None, 7275:None, 7293:None |
| H5822 | 7047:None, 7276:None, 7294:None |
| H5998 | 4687:None, 6442:None |
| H6001B | 4688:None, 6443:None |
| H6087B | 4676:None, 5195:None, 6391:None |
| H6089B | 4678:None, 5203:None, 6393:None |
| H6090B | 4679:None, 5204:None, 6394:None |
| H6092 | 4680:None, 5205:None, 6395:None |