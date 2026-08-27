# Escalation deep history

## #771 — Snapshot Creation Running Out of Control
type=task source=researcher related_activity=snapshot-retention-redesign, spawned from #758 from_id=758

**v1** (2026-08-21T15:03:41Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Snapshot Creation Running Out of Control
> **comment (set this version):** Investigate the snapshot creation, which is running out of control, and design a real fix. Split off from #758 as its own tracked item, per researcher instruction, rather than left buried inside the content-index item it was found investigating.
> **context (set this version):** Findings already established investigating #758 (2026-08-21), carried forward here as the starting point, not re-derived:

ROOT CAUSE: run.py's _ensure_run() calls dbsnapshot.snapshot() unconditionally on EVERY new run -- a full raw copy of iba.db, no compression, before ANY step, including pure read-only reports (escalation.list/history, configmaint.validate/report, content_index.size_profile, etc). retention.snapshot_keep_count=20 was presumably sized when the DB was much smaller; at the DB's recent real size (7.5-8GB before this session's content_index clear) the snapshot directory (iba/app/db/snapshots/) held exactly 20 files x ~7.5GB = ~150GB. In one session's worth of escalation/configmaint report calls (8-10 dispatches), several fresh multi-GB snapshots were minted purely for read-only reporting -- nothing to roll back, pure waste. Researcher had to manually delete snapshots several times already because of this.

WHY IT IS NOT A ONE-LINE FIX, checked before proposing anything: cfg_step.kind ('operations'/'utility') looked like the obvious gate (skip snapshot when kind='utility'), but it does NOT mean read-only -- configmaint.propose (which genuinely writes cfg_* tables and needs its rollback point) is ALSO classified 'utility'. Using kind as the gate would silently remove rollback protection on real config writes -- a durability regression, not a fix. A real per-step write-classification is needed (new cfg_step column or equivalent), not a guess -- and this is governed territory: governance.behaviour_boundary.backup_recovery / cfg_behaviour_rule 'writes-must-be-replayable' (sqlite class) explicitly protects this area, so the fix needs a real design, not a unilateral code change.

OPTIONS ALREADY ON THE TABLE, none built yet, all still your call:
1. IMMEDIATE RELIEF (safe, reversible, low-risk): prune existing local snapshots down to a handful -- NOT the only backup, NAS gets iba.db backed up nightly separately (backup.nas_db_backup_schedule / backup.iba_db_gap).
2. STOPGAP (config-only): lower retention.snapshot_keep_count from 20 to something much smaller (e.g. 3-5) via configmaint.propose -- caps future growth even before any code fix lands.
3. ROOT FIX (code + config, needs design): add an explicit per-step write-classification so _ensure_run() can correctly skip the pre-run snapshot for genuinely read-only steps, without touching steps that actually write. Needs the exact schema/config shape designed and approved, not guessed.

Also worth folding into the same investigation: retention.snapshot_keep_count's sizing assumption itself (20 kept, calibrated for a ~670MB DB per feedback_pre_op_db_snapshots_prune_or_skip) is now stale even before any code fix -- the DB has grown ~10x since that number was chosen (content_index alone added >7GB before today's clear). Whatever the eventual write-classification design settles on, the retention COUNT for genuinely-written-to snapshots may need its own review too, separate from the skip-when-read-only question.
> **related activity (set this version):** snapshot-retention-redesign, spawned from #758

**v2** (2026-08-21T15:14:34Z, Researcher) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** Set the retention of snapshots to a maximum of 5 ensure that it is maintained as such 

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

**v5** (2026-08-21T15:05:31Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** All three instructed actions done, in order -- see resolution for verification detail.
> **resolution (set this version):** All three instructed actions complete, in order, live-verified:

1. #770 raised ("Content-Index Search: Current Design Unsupportable"), from_id=758 set correctly (learned from the #767/#768 lesson earlier this session -- verified, not just claimed). Context carries the full design lineage quoted: the original plan doc's design decisions (predefined Strong's/gloss/word concordance keys, explicitly chosen over free-text FTS), BUILD.md sec141-143 in full including sec143's own never-actioned warning about unbrowsable common-word hit counts, and this item's own live scale figures.

2. content_index + content_index_scan emptied (iba/app/migration/clear_content_index_20260821.py, registered in cfg_utility): 14,118,338 -> 0 and 7,869 -> 0 rows. Cleared both together, not content_index alone, so a future refresh() doesn't silently think everything is already scanned. VACUUM run afterward -- iba.db: 8.06GB -> 0.66GB, 17.6s. Verified via direct file-size check, not assumed.

3. #771 raised ("Snapshot Creation Running Out of Control"), from_id=758, carrying this item's own already-established investigation forward as its starting point (root cause, the cfg_step.kind complication, the 3 options on the table) rather than re-deriving it.

configmaint.validate re-run clean after all of it. BUILD.md sec167 documents the full sequence.

**v6** (2026-08-21T15:09:06Z, Researcher) state=completed next_action=approved assigned_to=Researcher

**downward chain (spawned from #758):** #770, #771

## #770 — Content-Index Search: Current Design Unsupportable
type=task source=researcher related_activity=content-index-redesign, spawned from #758 from_id=758

**v1** (2026-08-21T14:59:51Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Content-Index Search: Current Design Unsupportable
> **comment (set this version):** The current method of search index creates prohibitively large tables in IBA which cannot be supported. Another solution needs to be considered. This escalation will design and build a new index search facility.
> **context (set this version):** DESIGN MATERIAL, quoted in full per instruction.

=== SOURCE 1: outputs/markdown/manifest-and-content-search-into-iba-plan-v1-20260815.md, sec2 (original design decisions, researcher, 2026-08-15) ===

sec2.1 Both A and B live in iba.db -- "IBA App is the engine for all processing related tables. Search result and utilities is process. Research_db will be used for analytic findings and there will be different reports to be defined for exploring the research_db."

sec2.2 The search flow chains metadata -> content -> index update, results carry file + location -- "search must search the file metadata, and then the content, and then update the index so that the search result will include the file reference and location."

sec2.3 Search keys are predefined, sourced from IBA's own DB tables -- NOT free-text/FTS -- "we can use DB tables (e.g. strong numbers and gloss) as the keys for the search build" / "the search keys will be predefined." Explicit rejection of the original draft's generic FTS5 free-text index (modelled on prose_section_fts) in favour of a concordance-style inverted index: for each predefined key (strong.strongNumber, strong.stepGloss, word_strong), record every .md file+line where it occurs. This is the design decision now proven unsupportable at scale.

sec2.4 Scope: all .md files, project-wide, including archive/ -- confirmed, only database/backups/.git excluded structurally.

=== SOURCE 2: BUILD.md sec141 (2026-08-17, build-time finding) ===

"Real design issue found running the actual rebuild, not a performance bug alone: one file (wa-programme-prose-extract-20260814.md, 144,866 lines) produced ~597,000 hits by itself -- the project's own analysis prose is saturated with the very biblical vocabulary being indexed. A full rebuild across all 7,874 .md files (558 MB) was projected at 15-30+ minutes for a multi-million-row index of doubtful value. Not run to completion -- stopped, the finding taken to the researcher." Researcher's response then: "we should definitely exclude the prose files. but there may be others also... I would first like to see the [size] check."

Built in response: cfg_content_index_exclude table, content_index.size_profile report (7,874 files/558.6MB, 74 files >=1MB hold 270.1MB), a ~100-word stopword filter for single-word gloss/word keys (strong.stepGloss genuinely carries entries like "and"/"not"/"this" -- real Hebrew/Greek conjunction/particle glosses -- matching nearly every line project-wide).

=== SOURCE 3: BUILD.md sec142 (2026-08-17, refinement) ===

T2 gloss exclusion (filtered by STRONG not gloss text, 9,165 -> 7,951 distinct glosses, ~13% reduction). exclude_size_threshold_bytes (50MB default) + release-override table. programme_prose exclusion proposed.

=== SOURCE 4: BUILD.md sec143 (2026-08-17, first real full rebuild -- THE KEY PRIOR WARNING) ===

Full rebuild: "7,869 files scanned, 19,348,411 total hits found, 14,118,338 rows actually written... Split: 10,722,246 gloss / 1,825,204 word / 1,570,888 strong."

"Two real costs, reported as found, not smoothed over: 1. iba.db grew from ~675MB to 8.06 GB -- a >10x increase from this one table. Real consequence: the daily IBA DB Backup to NAS task now transfers/stores 8GB nightly instead of 675MB. 2. Verified search itself, not just the build: strong:H2734 -- 938 hits, 0.68s, genuinely precise and useful. gloss:compassion -- 23,098 hits, 5.8s. word:anger -- 19,991 hits, 2.3s. Both technically correct... but not a browsable result set -- confirms the concern raised before the rebuild: common domain-central gloss/word keys will always produce very large hit counts, T2/stopword filtering notwithstanding, because the vocabulary IS the project's own subject."

"Not fixed or further descoped here -- reported to the researcher for a decision on whether this is acceptable as delivered or needs more refinement (e.g., a per-search result cap, rarity-based ranking, or dropping single-word gloss/word matching in favour of Strong's-number-only, which is demonstrably the highest-value, lowest-noise key type)." THIS DECISION WAS NEVER MADE -- the item was left as delivered, and the same concern flagged here on 2026-08-17 is exactly what has now forced the issue via #758.

=== SOURCE 5: escalation #758 (2026-08-21, current state) ===

content_index: 14,118,338 rows, 14x the next-biggest table in iba.db. Raw text payload ~3.45GB before its 3 indexes. iba.db total 7.5GB, freelist_count=0 (real data, not reclaimable without deletion). 76% of rows are key_type=gloss; top gloss values are ordinary English words coinciding with Strong's glosses (sense: 152,430 lines; word: 101,985; which: 71,830) -- NOT caught by the existing stopword list, since those are real content words, not conjunctions/particles. Two folders alone (iba/app/verse-analysis/**, Sessions/Session_Clusters/**) are 63.4% of all rows combined.

Researcher's own framing, closing this out (2026-08-21): "excluding the suggested folders to reduce the size defeats the object of the index. The index functionality needs to be re-considered."

=== ALREADY-PROPOSED ALTERNATIVES ON THE TABLE (from sec143, never decided) ===
1. A per-search result cap.
2. Rarity-based ranking (surface uncommon/precise hits first, suppress saturated common-word hits).
3. Drop single-word gloss/word matching entirely, keep Strong's-number-only (sec143: "demonstrably the highest-value, lowest-noise key type" -- strong:H2734 = 938 precise hits vs gloss:compassion = 23,098 unbrowsable hits).
> **related activity (set this version):** content-index-redesign, spawned from #758

**v2** (2026-08-21T15:11:26Z, Researcher) state=on-hold next_action=review assigned_to=Researcher
> **comment (set this version):** the search indexing will be redesign when the analytics are being revisited
