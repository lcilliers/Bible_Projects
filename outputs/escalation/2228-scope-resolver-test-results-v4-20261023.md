# 2228 — Scope resolver: test results (v4)

Escalation #2228. Run 2026-10-23 by iba/app/tools/temp_2228_verse_scope_test_run.py on a copy of iba.db (lib/dbsnapshot.copy_db) after the size guard was set to 2500 and made a hold for review (researcher 2026-10-23: 'any verse selection above 2500 should be subject to a review before proceeding'). New: T2a (M25+M02, 2,672 verses, held), T2 (the same with -Reviewed, the review recorded), T2b (no review recorded under the limit); T12g/T12 OT-108 held, then resolved with -Reviewed. v3 is in outputs/escalation/archive/. Result: 38/38 PASS.

| # | case | result | evidence | s |
|---|---|---|---|---|
| T0 | migrations: applied (or already applied on the live source), then skipped on a re-run | PASS | already applied -- 0 write(s) / already applied -- 0 write(s) / 1 write(s) applied (run DEVMODE-2228-VERSE-SCOPE-20261022, logged to cfg_change_detail) / already applied -- 0 write(s) / 1 write(s) applied (run DEVMODE-2228-READING-INDEX-20261023, logged to cfg_change_detail); tables created: [] / already applied -- 0 write(s); tables to create: [] / already applied -- 0 write(s) / already applied  |  |
| T1 | -Cluster M25: the verses of its live strongs; every route names an M25 strong | PASS | 2027 verses, SQL 2027 | 0.46 |
| T2a | -Cluster M25,M02 (2,672 verses, over 2,500): held for review | PASS | the request is too wide -- verses in the result (2672 against the limit 2500); it is held for review: reform it to a narrower scope, or, once the researcher has reviewed it, re-run with -Reviewed "<th |  |
| T2 | -Cluster M25,M02 -Reviewed: the union, the review recorded; a verse in both carries routes from both | PASS | 2672 verses, SQL 2672; 36 in both; reviewed 'test review' | 0.51 |
| T2b | -Cluster M25 (2,027, under the limit) with -Reviewed: no review recorded (none was needed) | PASS | {'verses': 2027, 'selectors': 1, 'not_resolved': 0} | 0.61 |
| T3 | -Strong H0430 (bare): decomposed to every derivative that occurs | PASS | derivatives ['H0430G', 'H0430H', 'H0430I', 'H0430J']; 2231 verses | 0.45 |
| T3b | -Strong H430: zero-padded to H0430, same derivatives | PASS | [{'code': 'H0430G', 'sense': 'God'}, {'code': 'H0430H', 'sense': '[LORD]-Elohe'}, {'code': 'H0430I', 'sense': '[Gibeath]-elohim'}, {'code': 'H0430J', 'sense': 'gods'}] | 0.44 |
| T3c | -Strong G0002 (a bare code that occurs itself): taken as it is | PASS | [{'code': 'G0002', 'sense': 'Aaron'}] | 0.38 |
| T4 | -Strong H0430H: only that code | PASS | 1 verses | 0.43 |
| T5 | -Strong H9999 (occurs nowhere): refused, naming it | PASS | 'H9999' occurs in no verse and has no derivative that does |  |
| T5b | -Strong H0430Q (occurs nowhere): refused, naming it | PASS | 'H0430Q' occurs in no verse -- did you mean H0430G, H0430H, H0430I, H0430J? |  |
| T6 | -Cluster M02 -OnlyStrong H3708A: only the M02 verses holding H3708A | PASS | 22 verses, SQL 22; dropped 659 | 0.42 |
| T7a | -Verse "Rom 8": the whole chapter | PASS | 39 verses, SQL 39 | 0.28 |
| T7b | -Verse "Luk 14:12-14; Psa 10:2": 4 verses, Psalms before Luke | PASS | ['Psa 10:2', 'Luk 14:12', 'Luk 14:13', 'Luk 14:14'] | 0.29 |
| T7c | -Verse "Gen 1:30-2:2": a range across chapters | PASS | ['Gen 1:30', 'Gen 1:31', 'Gen 2:1', 'Gen 2:2'] | 0.27 |
| T8 | -Verse "Neh 10:35" (no verse row): listed as not resolved, by design | PASS | [{'kind': 'verse', 'value': 'Neh 10:35', 'reason': 'no verse row (by design: governance.verse_gap_by_design)'}] | 0.28 |
| T9a | -Chapter 10.13: the cited verses of its current blocks; blocks that cite none listed | PASS | 414 verses, SQL 414; 2 blocks with no citation, SQL 2 | 0.34 |
| T9b | -Chapter 10.13 -Section "The words": that block's cited verses only | PASS | 16 verses, SQL 16 | 0.32 |
| T9c | -Section that does not exist: refused | PASS | chapter 10.13 has no current block headed 'no such heading' |  |
| T10a | -Claim I-2 (no verse source): zero verses, with the reason | PASS | [{'kind': 'claim', 'value': 'I-2', 'reason': 'claim has no verse source'}] | 0.28 |
| T10b | -Claim C-330: its verse sources | PASS | 4 verses, SQL 4 | 0.28 |
| T11a | -Observation 2949 (no node): zero verses, with the reason | PASS | [{'kind': 'observation', 'value': '2949', 'reason': 'observation is grounded on no verse'}] | 0.28 |
| T11b | -Observation 12478: Ecc 7:9 | PASS | [1056] | 0.28 |
| T12g | -Thread OT-108 under the guard (verse_scope.max_verses 2500): held for review | PASS | the request is too wide -- verses in the result (29743 against the limit 2500); it is held for review: reform it to a narrower scope, or, once the researcher has reviewed it, re-run with -Reviewed "<t |  |
| T12 | -Thread OT-108 -Reviewed: every open item resolved or reported; kinds that name no verse reported | PASS | 17 open items (cluster, escalation); 29743 verses; 2 with no verse kind | 3.48 |
| T12b | -Item OT-108.1: one item | PASS | {'verses': 0, 'selectors': 0, 'not_resolved': 1} | 0.36 |
| T13a | {'Strand': 'anger'}: the verses of its word family | PASS | 681 verses, SQL 681 | 0.40 |
| T13b | {'Subgroup': 'A_thanksgiving_act'}: the verses of its word family | PASS | 38 verses, SQL 38 | 0.41 |
| T13c | -Word corruption (real: its list holds the bare H4654): decomposed to H4654A, H4654B, nothing unresolved | PASS | ['G0853', 'G0889', 'G1311', 'G1312', 'G1612', 'G2585', 'G2679', 'G2692', 'G2704', 'G3393', 'G3394', 'G4550', 'G4595', 'G4646', 'G4938', 'G5349', 'G5351', 'G5356', 'H0006', 'H0444', 'H1097', 'H1100I', 'H1942', 'H2015', 'H2254B', 'H2610', 'H3589', 'H3832', 'H4072', 'H4167', 'H4654A', 'H4654B', 'H4743', 'H4889', 'H4893B', 'H5754', 'H5856', 'H7591', 'H7703', 'H7843', 'H7844', 'H7845G', 'H7845H', 'H839 | 0.43 |
| T13d | -Word courage (synthetic: H9998 added to its list on the copy): the stale code reported, the rest resolved | PASS | [{'kind': 'word', 'value': 'courage: H9998', 'reason': "'H9998' occurs in no verse and has no derivative that does"}] | 0.42 |
| T14 | -File {cluster M02, only_strong H3708A} through the handler: same verses as T6 | PASS | t14-20261023.json: {'verses': 22, 'selectors': 1, 'not_resolved': 0} |  |
| T15 | same label twice in a day: v2 live, the first archived | PASS | live ['t15-20261023-v2.json']; archive ['t15-20261023.json'] |  |
| T15b | no selector: refused, no file | PASS | the request has no selector (-Cluster, -Subgroup, -Strand, -Word, -Strong, -Verse, -Chapter, -Claim, -Observation, -Item, -Thread or -File) |  |
| T15c | -File that does not exist: refused | PASS | request file not found: C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/17ac2129-4964-4787-9bc5-5c1c32d28250/scratchpad/t2228/nofile.json |  |
| T16 | read-only: no row written on the copy by any case | PASS | total_changes 0 -> 0 |  |
| T17 | every case within 5 seconds | PASS | slowest 3.48s |  |
| T18 | #2233: the rule row and its two point-of-use scopes | PASS | [(113, 'study_method', 'mechanically_enforced')] [('ps', 'Strand-Reading.ps1'), ('ps', 'Verse-Scope.ps1')] |  |
| T19 | configmaint.validate hard checks on the copy: no coherence error | PASS | none |  |

