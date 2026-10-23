# 2236 — Open-Item.ps1: test results (v1)

Escalation #2236 (outputs/escalation/2236-open-item-design-v2-20261023.md). Run 2026-10-23 by iba/app/tools/temp_2236_open_item_test_run.py on a copy of iba.db (lib/dbsnapshot.copy_db) with the migration applied to the copy; expected values by plain SQL. Result: 20/20 PASS.

| # | case | result | evidence |
|---|---|---|---|
| O0 | migration applied (or already), then skipped | PASS | ["50 write(s) applied (run DEVMODE-2236-OPEN-ITEM-20261023, logged to cfg_change_detail); columns added: ['origin_escalation_id', 'anchor', 'source_terms', 'target_cluster', 'target_terms', 'read_for', 'why', 'comes_back_when', 'target_verses', 'worded_at']; table escalation_thread_item_verse created", 'already applied -- 0 write(s); columns to add: []'] |
| O1 | Add OT-103 H0639G x H7489A (M58): a worded item, its 4 verses kept, thread history written | PASS | OT-103.71 added: M58: H0639G x H7489A (4 verses); verses 4 |
| O2a | Add refused: no read-for; nothing written | PASS | -ReadFor is required and states it in words (an item without a clear purpose is refused) |
| O2b | Add refused: origin not a task or issue; nothing written | PASS | -Origin '2109' must be the task or issue of the analysis that raises the item |
| O2c | Add refused: anchor kind unknown; nothing written | PASS | -Anchor 'file:abc' must be one of strong:<value>, verse:<value>, observation:<value>, claim:<value>, block:<value> |
| O2d | Add refused: target term not in the cluster; nothing written | PASS | target term(s) ['H0639G'] are not in cluster M58 |
| O2e | Add refused: both verse and cluster; nothing written | PASS | give the target either as -Verse, or as -Source with -TargetCluster and -TargetTerms, not both |
| O2f | Add refused: no verse in common; nothing written | PASS | the target 'M58: G0002 x H7489A' holds no verse (the source and target terms never stand in the same verse) |
| O2g | Add refused: over 200 verses; nothing written | PASS | the target 'M15: H3068G x H3045' holds 303 verses, over open_item.max_verses 200: split it into separate items, one purpose each |
| O3 | Add refused: duplicate (same target, same read-for); nothing written | PASS | OT-103 already has an open item on 'M58: H0639G x H7489A' reading for the same thing |
| O4 | Reword OT-103.1 (cluster:M58, legacy): now worded, scoped; the old wording in its history | PASS | OT-103.1 reworded: M58: H0639G x H7489A (how the anger of H0639G meets H7489A of ) (4 verses); history: reworded (#2236); was: cluster:M58 |
| O5 | Reword again to a verse target: the earlier target verses kept as deleted, the new one live | PASS | OT-103.1 reworded: Pro 29:22 (1 verses); deleted 4, live 1 |
| O6 | Split OT-103.2 into two: the old one superseded naming them; the thread still open | PASS | OT-103.2 split into OT-103.72, OT-103.73; old superseded; thread on-hold |
| O7 | Matching: a worded item matches its target verses only; its home cluster only when home is on | PASS | in 1, other verse 0, home 1, no home 0 |
| O8 | Collation: the worded item shows on its target verse, not on another M58 verse | PASS | {'Num 11:10': ['OT-103.11', 'OT-103.71'], 'Deu 29:17': []} |
| O9 | Due -Cluster M58 lists the worded M58 items | PASS | 1 open item(s) come back when M58 is worked
  OT-103.71 M58: H0639G x H7489A (4 verses): how the anger of H0639G meets H7489A of the wicked in these verses |
| O10 | Review: the report written; its worded total equals the tables | PASS | open-items-review-v1-20261023.md; worded 4 |
| O11 | A -File batch with one bad spec: refused, nothing written (one unit) | PASS | -ReadFor is required and states it in words (an item without a clear purpose is refused) |
| O12 | Thread audit raises nothing on the worded items | PASS | [] |
| O13 | configmaint.validate hard checks on the copy (a migration not yet archived set aside) | PASS | none |

