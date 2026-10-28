# Escalation deep history

## #2301 — Named pre-run snapshots are pruned by the run snapshots
type=issue source=researcher

**v1** (2026-10-26T04:56:34Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Named pre-run snapshots are pruned by the run snapshots
> **comment (set this version):** Found in the #2298 bulk run (2026-10-26): run.py takes a full snapshot of iba.db (about 870 MB) before every new run and prunes iba/app/db/snapshots to retention.snapshot_keep_count (5), oldest first, without regard to name. The named pre-run snapshots taken before Developer Mode migrations are pruned with them: the folder now holds only the 5 latest run snapshots, so pre-2292, pre-2293, pre-2294, pre-2298-tail-ceiling and pre-2298-bulk are gone, as are the earlier ones BUILD.md names (pre-2273, pre-2271-2272). A recorded "snapshot first" therefore protects nothing once five runs follow. Each dispatch also spends the time of a full copy. Not fixed: a design choice (B:105).
> **context (set this version):** iba/app/lib/dbsnapshot.py; cfg_setting retention.snapshot_keep_count; cfg_setting backup.pre_run_snapshot_policy; iba/app/BUILD.md sections 406 to 413; #2298

**v2** (2026-10-26T06:11:17Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Options for the design (iba/app/lib/dbsnapshot.py prune; cfg_setting retention.snapshot_keep_count 5; backup.pre_run_snapshot_policy). (a) prune only the automatic run snapshots (names ending in a run slug, iba-<ts>-<package>-run-...): a named pre-run snapshot (iba-<ts>-pre-<id>-...) is never pruned by them and is kept until archived or removed by hand; (b) named snapshots go to their own folder (iba/app/db/snapshots/kept) with their own keep count, cfg_setting retention.kept_snapshot_keep_count; (c) raise retention.snapshot_keep_count so five runs no longer reach back past a migration. Each run snapshot is a full copy of iba.db, about 870 MB, so (c) costs the most disk; (a) and (b) keep the run snapshots at 5. Recommended (inferential): (a), the smallest change; the BUILD.md records 406 to 413 that name pruned snapshots stay as written (history) and the pruning is stated on this item.
> **resolution (set this version):** Decision sought: (a) prune only automatic run snapshots, never a named pre-run snapshot (recommended); (b) a separate kept folder with its own keep count; (c) a larger keep count for all. On the answer Claude builds it as its own small unit and tests it on a copy.

**v3** (2026-10-26T06:33:18Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, chat 2026-10-26 (verbatim, on #2298 Q4): "prune the snaphots, after taking a backup if not already done.  but delay this pruning for a couple of days just to give time to validated there are no serious damage to the database and its data."

**v4** (2026-10-26T06:36:56Z, Claude) state=on-hold next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Done 2026-10-26, Claude: a full backup of live iba.db taken with lib/dbsnapshot.copy_db, outside the pruned folder: iba/app/db/iba.db.pre-2301-prune-20261026.bak (875 MB, integrity_check ok, 13,411 surface_subgroup pairs; it also holds RO13, run DEVMODE-2298-LARGE-SUBGROUP-20261026). Pruning held for the validation window, as ruled. To prune when it falls due, shown again for the go-ahead before anything is deleted: (1) the 5 run snapshots in iba/app/db/snapshots (each about 870 MB) and the stale pre-2273 -shm and -wal; (2) the older .bak copies in iba/app/db: pre-2110-claim-register and pre-2110-import (20261013), pre-2163-flesh-body with its -shm and -wal (20261018), pre-2173-session-routines (20261020). Kept: the new pre-2301 backup, and the daily NAS copies (backup.nas_db_backup_schedule). Still open: the design choice (a), (b) or (c) for the pruning itself; the Q4 words do not choose one, so it is asked again when the item comes back.

**v5** (2026-10-26T17:37:14Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** approved to prune the snapshots

**v6** (2026-10-26T17:43:12Z, Claude) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-26: prune the stale pre-2273 files and the older backups. Done by Claude, checked by listing iba/app/db and iba/app/db/snapshots after: removed the pre-2273 -shm and -wal, iba.db.pre-2110-claim-register-20261013.bak, iba.db.pre-2110-import-20261013.bak, iba.db.pre-2163-flesh-body-20261018.bak with its -shm and -wal, and iba.db.pre-2173-session-routines-20261020.bak. Kept: iba.db.pre-2301-prune-20261026.bak and the 5 run snapshots (the instruction did not name them). Still open: the 5 run snapshots, and the design choice (a), (b) or (c) for the pruning itself.

**v7** (2026-10-27T05:10:39Z, Claude) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-26 (verbatim): "we do not have much tokens left for this session - so lets tackle smaller cleanup tasks.  I approved 2301 for your action."
Researcher, chat 2026-10-26 (verbatim): "I'll run the deletion command myself; then close the pruning part of 2301."
Claude: the deletion was refused by the permission classifier; the researcher then instructed, in chat: "prune the stale pre-2273 files and the older backups", which was done and recorded in v6. Still open: the 5 run snapshots and the design choice (a), (b) or (c).
