---
name: operational-governance-git-backup-manifest
description: Programme-wide operational governance — git/commit discipline, backups & recovery safeguards, manifest usage, interaction protocols, cost — lives scattered in CLAUDE.md §9/§12/§13 + scripts + the DB-loss incident; no consolidated governing doc (gap)
metadata:
  type: reference
---

REFERENCE (2026-06-14): the programme-wide OPERATIONAL / safeguard governance has **no dedicated instruction doc** — it is scattered, and CLAUDE.md (its main home) is drift-stale. Where each piece lives:

- **Git / commit:** CLAUDE.md §12 — excluded from git (`database/bible_research.db`, `backups/`); commit msg `session YYYYMMDD: brief description`; branch `main`; remote `github.com/lcilliers/Bible_Projects`. Discipline: commit units of work throughout + **commit and push ALWAYS together** — [[feedback_commit_incrementally]].
- **Backups & safeguards:** CLAUDE.md §13 — project off Google Drive since 2026-06-03 (Drive sync corrupted the DB + `.git`). NAS: DB daily 18:00 (`scripts/backup_db_to_nas.py`, task "BibleResearch DB Backup to NAS"); full folder + memory mirror daily 18:30 (`scripts/mirror_to_nas.ps1`, task "BibleResearch Full Mirror to NAS"); memory also committed to git under `memory/`. Engine rolling-10 DB snapshots (`engine/backup.py`, `BACKUP_RETENTION=10`). Incident + lessons: `outputs/markdown/wa-db-loss-incident-20260603.md` — [[project_db_loss_blocker_20260603]]. Core safeguard rule: **all work in the DB and replayable** — [[feedback_all_study_work_in_db]] (June 1–2 handler work was lost because it wasn't).
- **Manifest (use of):** `docs/file-organisation-rules.md` §6 + CLAUDE.md §9 #5; rebuild `scripts/build_file_manifest.py` after file moves / session-log processing; **locate files via the manifest, not the folders** — [[filing-is-first-class-governance]].
- **Interaction protocols & cost:** `docs/interaction-preferences.md` + CLAUDE.md §9 — confirm before non-trivial work · all outputs to `.md` with a chat pointer · factual discipline (no guessing) · cost awareness (§9 #6) — [[feedback_interaction_protocols]].

GAP / open item: this operational layer should be consolidated into one governing doc (or DB-resident register); it currently relies on the drift-stale CLAUDE.md. See [[reference-core-memory-orientation-map]] · [[project_reconstruction_baseline_20260614]].
