# DB Loss Incident — 2026-06-03

**Status:** OPEN — recovery required before any pipeline work resumes.
**Discovered:** while attempting to "restart last session" (resume M20 cluster remediation).
**Severity:** CRITICAL — live database destroyed; no current local copy.

---

## 1. What happened

`database/bible_research.db` was truncated to **0 bytes** today at **05:10** (should be ~165 MB).
No `-wal` / `-shm` / `-journal` sidecars exist, so there is no in-place recovery.

Signature points to a **Google Drive sync-corruption event**:
- Three conflict copies of the DB were placed in Google DriveFS `lost_and_found`, then deleted to the Recycle Bin.
- DriveFS content cache holds only an old (Apr 19) blob.
- Newest DriveFS log `drive_fs_22.txt` ends 05:00:23 today, minutes before the truncation.

## 2. Local copies inventory (all STALE — pre-date May–June work)

| Source | Size | Date | Path |
|---|---|---|---|
| Live DB (destroyed) | 0 MB | 2026-06-03 05:10 | `database/bible_research.db` |
| Recycle bin copy 1 | 141 MB | content 2026-03-31, deleted 04-14 | from `…\DriveFS\lost_and_found\…` |
| Recycle bin copy 2 | 141 MB | content 2026-04-01, deleted 04-14 | from `…\DriveFS\lost_and_found\…` |
| Recycle bin copy 3 | 141 MB | content 2026-04-01, deleted 04-14 | from `…\DriveFS\lost_and_found\…` |
| DriveFS content cache blob | 159.7 MB | 2026-04-19 | `…\DriveFS\115528034466248103449\content_cache\d44\d128\80913` |
| Dryrun snapshot | 159.7 MB | 2026-04-19 | `backups/dryrun/bible_research_trial_audit_r1_20260419.db` |

All predate: the four 06-02 cluster closures (M10c/M10b/M38/M08), the COMMENT_EVALUATION handler suite, the dedup-ghost repair, M20 progress, and the May–June schema migrations. **Restoring any of these loses ~6 weeks of work — last resort only.**

## 3. The only viable recovery: Google Drive version history

Google Drive retains prior versions of non-Google files for ~30 days / 100 versions. The good
~165 MB version from **2026-06-02** should still be available online.

**Recovery steps (researcher, in Google Drive web UI — CC cannot do this from the filesystem):**
1. **Stop all DB writes.** Do not run the engine, `apply_session_patch.py`, or any script that opens the DB. Opening the 0-byte path creates a fresh empty SQLite file that Drive syncs, pushing empty versions over the good one.
2. **Pause Google Drive sync** (tray icon → pause) to stop the race.
3. drive.google.com → `Bible_study_projects/database/` → right-click `bible_research.db` → **Manage versions / Version history**.
4. Find the last **~165 MB** version dated **2026-06-02** (before today 05:10). Download/restore it.
5. Place it at `database\bible_research.db`; resume Drive sync.

## 4. Verification (CC, once a candidate file is in place)

- `PRAGMA integrity_check;`
- `SELECT version FROM schema_version ORDER BY ... ;` — expect the 06-02 schema.
- Confirm 06-02 state: clusters **M10c, M10b, M38, M08** = `Analysis Complete`; M20 mid-remediation; dedup-ghost repair (0 orphaned active VC verses).
- Row sanity: ~133k active OWNER verses; ~5,500 OWNER + ~1,500 XREF terms.

## 4b. Where the full backups went (investigated 2026-06-03)

The engine *was* making full DB backups: `engine/backup.py` writes pre-run
(`bible_research_backup_<ts>_<run>.db`), post-run (`..._post.db`), manual, and
pre-migration snapshots to `backups/`, keeping 10 of each. A week ago that folder held
dozens of full `.db` files (researcher confirms). **Now `backups/` contains only the
Apr 19 dryrun `.db` + 38 tiny JSON row-snapshots — zero full engine backups.**

They are **not** in the Windows Recycle Bin (only the three April `bible_research` copies
+ May-25 cluster `.zip`s are there). Drive-side deletions bypass the Windows Recycle Bin
and go to **Google Drive Trash** (online, 30-day retention). → Strong indication the same
Google Drive sync event that zeroed the live DB also removed the backups.

**ROOT-CAUSE / DESIGN FLAW:** `backups/` lives inside the Google-Drive-synced tree, so the
database and all its backups shared one failure domain — a single Drive event took out
both. Backups must have an **off-Drive copy**. Action after recovery: add a local
(non-Drive) backup target.

**Recovery leads (researcher, online):**
- **Google Drive Trash** (drive.google.com/drive/trash) → search `bible_research` → restore
  recent `bible_research_backup_*.db` / `*_post.db` / `*_manual_*.db`. Do NOT empty trash.
- **Version history** on `bible_research.db` → restore the ~165 MB 2026-06-02 version.

## 5. Notes / follow-ups

- Git repo is INTACT through 06-02 (scripts, instruction docs, and `Sessions/Patches/*.json` all committed). Only the gitignored DB was lost.
- After recovery, consider a **regular local DB backup** outside Google Drive's sync path (the engine `BACKUP_RETENTION=10` snapshots go to `backups/`, which is itself inside Drive — vulnerable to the same sync event). A copy to a non-Drive location would harden against this.
- If Drive version history does NOT reach 06-02, fallback is the Apr 19 snapshot + replay of committed patches — large effort, partial; escalate before attempting.
