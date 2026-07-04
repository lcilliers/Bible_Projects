---
name: feedback_pre_op_db_snapshots_prune_or_skip
description: "OPERATIONAL: the reusable _apply_* scripts take a full ~670MB pre-op DB snapshot into backups/ on EVERY invocation; called in a loop over dozens of chapters/registries these balloon and can fill the C: drive (hit 100% / 82MB free 2026-07-04). Prune the transient snapshot families or use --no-backup; keep only milestone-named backups."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 92aed34e-8a28-44a4-8d9d-4bdf6df70a12
---

**Discovered 2026-07-04 mid-Isaiah (disk 100% full, 82MB free, blocking further filing).**

**What:** Several `_apply_*` engine scripts `shutil.copy2` the whole live DB (~670MB) into `backups/` as a pre-operation safety snapshot on **every run**. Run in a loop over many chapters/registries, these transient snapshots accumulate into tens/hundreds of GB. On 2026-07-04 the `backups/` dir held **211 transient files (~136GB)**: `bible_research.pre-backfill.*Z.db` (from the Phase-1/backfill script) + `bible_research.pre-chapprose.*Z.db` (from `_apply_file_chapter_lexical_prose`, one per chapter filed) — enough to fill the 475GB C: drive.

**Why it's safe to prune them:** these are *pre-op* copies for operations already completed + committed; the live DB is current; the real safety net is (a) the **milestone-named** backups (`pre_migration_v3.*`, `KEEP-RESET-baseline-*`, `pre-faculty-reset*`, `AUDIT_WORD-reg*`, etc.), (b) the **NAS daily DB backup** (`db_backups\`, 18:00 task), and (c) the **git memory mirror**. See [[project_backup_alerting_and_outlook_smtp_block]], [[reference_operational_governance_git_backup_manifest]].

**How to apply:**
- Distinguish the two backup classes by name: **timestamped auto-snapshots** (`*.pre-<op>.YYYYMMDDThhmmssZ.db`) are transient/prunable; **descriptively-named** ones are intentional milestones — KEEP.
- To reclaim space: `rm -f backups/bible_research.pre-backfill.*Z.db backups/bible_research.pre-chapprose.*Z.db` (keep milestone-named files).
- `_apply_file_chapter_lexical_prose_v1_20260702.py` now has **`--no-backup`** and **self-prunes to the 3 most-recent** pre-chapprose snapshots (fixed 2026-07-04). For any *other* loop-invoked `_apply_*` script, pass a skip-backup flag if it has one, or prune its snapshot family afterward. When adding pre-op snapshots to a reusable script, always pair with a keep-N prune + a `--no-backup` opt-out.
- Check free space before long batch runs: `df -h /c`.
