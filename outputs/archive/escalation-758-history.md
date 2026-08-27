# Escalation deep history

## #758 — content_index Size / DB-Bloat Investigation
type=issue source=iba.app.lib.contentindex related_activity= from_id=

**v1** (2026-08-21T11:44:23Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** content_index Size / DB-Bloat Investigation
> **comment (set this version):** content_index (14.1M rows) is the large majority of iba.db's 7.5GB. Two folders never added to cfg_content_index_exclude now dominate: iba/app/verse-analysis/** (31.8%) and Sessions/Session_Clusters/** (31.6%) -- same failure mode already fixed once for programme_prose (2026-08-17). Needs your decision on scope before excluding.

[data corrected 2026-08-20, escalation #759: short_description reshaped to a <=60-char title; prior full text redistributed into context (background) / comment (what needs to be done) / resolution (what was actually done) per the researcher's column-spec correction. No prior escalation_history row altered.]

[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description was a compressed sentence, not a composed title -- researcher: "it looks like you just cut whatever was there previous to 57 chars". Redone as an actual noun-phrase title, matching #753's own style. comment/context/resolution from round 1 are unchanged.]
> **context (set this version):** DB itself: 7.5GB, freelist_count=0 -- real data, not reclaimable. content_index: 14,118,338 rows, 14x the next-biggest table. Raw text payload ~3.45GB before its 3 indexes. 76% of rows are key_type=gloss; top gloss values are ordinary English words coinciding with Strong's glosses (sense: 152,430 lines; word: 101,985; which: 71,830), not caught by the existing conjunction-only stoplist. iba/app/verse-analysis/**: 4,487,358 rows across 303 files. Sessions/Session_Clusters/**: 4,460,980 rows. ContentIndex-SizeProfile.ps1 already exists for pre-decision review.

**v2** (2026-08-21T13:54:22Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** the sytem running out of space is a major issue, I had to manually delete snapshots now several time.  I would suggest that it is not necessary to keep snapshots past confirming the update has worked properly.  or alternatively come up with another solution.  We also need to see if there is any other way to handle the content index because it massively inflates IBA and rapidly cause the drive to run out of space because of the multiplicity of the backups and snapshots

**v3** (2026-08-21T14:02:59Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Investigated per your instruction -- found the dominant cause, separate from the content_index question this item started with.
> **resolution (set this version):** ROOT CAUSE: run.py's _ensure_run() calls dbsnapshot.snapshot() unconditionally on EVERY new run -- a full raw copy of iba.db, no compression, before ANY step, including pure read-only reports (escalation.list/history, configmaint.validate/report, etc). retention.snapshot_keep_count=20 was presumably sized when the DB was much smaller; at today's real size the snapshot directory (iba/app/db/snapshots/) holds exactly 20 files x 7.51GB = 150.16GB RIGHT NOW. In just this session's escalation/configmaint report calls (maybe 8-10 dispatches), several fresh 7.51GB snapshots were minted purely for read-only reporting -- nothing to roll back, pure waste. This is very likely the dominant contributor to the repeated manual deletions.

NOT a simple fix, checked before proposing: cfg_step.kind ('operations'/'utility') looked like the obvious gate (skip snapshot when kind='utility'), but it does NOT mean read-only -- configmaint.propose (which genuinely writes cfg_* tables and needs its rollback point) is ALSO classified 'utility'. Using kind as the gate would silently remove your rollback protection on real config writes -- would have been a durability regression, not a fix. This needs a real, explicit per-step write-classification (new cfg_step column or similar), not a shortcut -- a design decision, not something to build unilaterally given governance.behaviour_boundary.backup_recovery/writes-must-be-replayable.

RECOMMENDATION, your call on each:
1. IMMEDIATE RELIEF (safe, reversible, low-risk): prune the existing 20 local snapshots down to a handful now -- they are NOT your only backup (NAS gets iba.db backed up nightly separately, backup.nas_db_backup_schedule/backup.iba_db_gap), so this is disposable rollback convenience, not data loss risk.
2. STOPGAP (config-only): lower retention.snapshot_keep_count from 20 to something much smaller (e.g. 3-5) via configmaint.propose -- caps future growth even before the code fix lands.
3. ROOT FIX (code + config, needs design): add an explicit per-step classification (e.g. cfg_step.writes_data or similar) so _ensure_run() can skip the pre-run snapshot for genuinely read-only steps -- correctly classified per-step, not guessed from kind. I can propose the exact config/schema shape if you want me to build this.

content_index folder-exclusion question (the item's original topic) is separate and still open -- your decision on scope needed before I touch cfg_content_index_exclude.

**v4** (2026-08-21T14:57:20Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** excluding the suggeested folders to reduce the size defeats the object of the index.  The index functionality need to be re-considered. Create a new escalation for indexed Search. in the context quote all the design material related to index search. The comment should ready that the current method of search index creates prhibitively large tables in IBA which cannot be supported. another solution need to be considered. after creating the new escalation, delete all the rows in the index table so that the size of the database can reduce again. The new escalation will design and build a new index search facility.  finally, another escalation, spawned from this item, must be created to investigate the snapshot creation, which is running out of control
