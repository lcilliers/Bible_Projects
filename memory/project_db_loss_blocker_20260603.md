---
name: project-db-loss-blocker-20260603
description: 2026-06-03 DB loss RESOLVED — project moved to C:\Bible_study_projects; DB recovered to 2026-05-28 state so June 1-2 work must be redone
metadata: 
  node_type: memory
  type: project
  originSessionId: b103bd50-49b2-4bd0-9b30-596461d15432
---

On 2026-06-03 a Google Drive sync/trash event zeroed `bible_research.db` (0 bytes) AND corrupted the local `.git` object store. Drive version history and Trash held nothing usable. RESOLVED by recovering an intact **2026-05-28** DB copy (schema 3.28.0, integrity ok) from a DriveFS "Lost and Found" folder on the Desktop.

**Permanent outcomes:**
- **Working directory moved off Google Drive to `C:\Bible_study_projects`.** Old `G:\My Drive\Bible_study_projects` retained as a read-only fallback only (do not work there). Reopen Claude Code / terminals in `C:\`.
- **Git rebuilt clean** at C:\ from GitHub remote (history through 2026-05-27 `d44d5f5`) + a single baseline commit `4ce4168` capturing the 2026-06-02 working tree. Granular June 1-2 *commit* history is gone; file *content* is intact.
- **Off-Drive NAS backups live:** `scripts/backup_db_to_nas.py` + daily 18:00 scheduled task "BibleResearch DB Backup to NAS" → `\\LSUK-SYNRACK\HomeMedia\bible_study_projects\db_backups` (consistent online-backup, integrity+hash verified, GFS retention, refuses <50MB/corrupt source).

**CRITICAL — DB is at the 2026-05-28 state, not 06-02.** The June 1 + June 2 *database* work must be REDONE: remediation orchestrator runs, COMMENT_EVALUATION findings, **M10b/M38/M08 closures**, the dedup-ghost verse repair, and **M20** Phase A/C1/B1a. So memories/registers describing that progress (e.g. [[project_remediation_orchestrator_active]], the 06-02 close report) are AHEAD of the actual DB — verify cluster status in the DB before trusting them. The scripts + decision records survive on disk to guide the redo.

Note: engine `EXPECTED_SCHEMA_VERSION` (3.27.0) is behind the recovered DB (3.28.0) — pre-existing drift; don't blindly `--migrate`. Full record: `outputs/markdown/wa-db-loss-incident-20260603.md` + `wa-db-recovery-assessment-20260603.md`.
