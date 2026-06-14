# Operational & Safeguard Governance — v1.0

> Consolidated governing doc for programme-wide operations: **git/commit · backups & recovery · the file manifest · interaction protocols & cost.** Created 2026-06-14. Consolidates what was scattered across CLAUDE.md §9/§12/§13 (which can lag); this doc is the canonical home. Read at session start via `docs/project-orientation-core-memory-map.md`.

---

## 1. Git & commit

- **Repo:** `github.com/lcilliers/Bible_Projects` · branch **`main`**.
- **Excluded from git:** `database/bible_research.db`, `backups/`. **Committed:** `Sessions/Patches/*.json`, and `memory/` (the git mirror of the `.claude` project memory).
- **Commit message:** `session YYYYMMDD: brief description`, ending with the `Co-Authored-By:` trailer.
- **Discipline:** commit **units of work throughout** the session (in-progress commits are fine), not only at session end. **Commit and push ALWAYS go together — never leave a commit unpushed.**
- **Branching:** work on `main` is normal here; branch first for risky or large changes. Never skip hooks or bypass signing unless explicitly asked.

## 2. Backups & recovery (safeguards)

- **Why this matters:** on 2026-06-03 a Google Drive sync event truncated the live DB to 0 bytes and took the in-Drive backups + `.git` with it (~6 weeks lost; June 1–2 handler work unrecoverable). Incident + lessons: `outputs/markdown/wa-db-loss-incident-20260603.md`. Response: project moved off Drive to `C:\Bible_study_projects`.
- **NAS backups** (`\\LSUK-SYNRACK\HomeMedia\bible_study_projects\`):
  - **DB** → `db_backups\` — daily **18:00**, task *"BibleResearch DB Backup to NAS"*, `scripts/backup_db_to_nas.py`.
  - **Full folder + memory mirror** → `mirror\` + `claude-backup\` — daily **18:30**, task *"BibleResearch Full Mirror to NAS"*, `scripts/mirror_to_nas.ps1` (robocopy `/MIR`).
- **Engine snapshots:** rolling 10 DB backups (`engine/backup.py`, `BACKUP_RETENTION = 10`), pre/post run.
- **Memory:** committed to git under `memory/` (mirror of the `.claude` memory) **and** mirrored to NAS by the 18:30 task. When you write a `.claude` memory file, also copy it to `C:\Bible_study_projects\memory\` and commit.
- **Core safeguard rule:** **all study work must live in the DB and be replayable** (patches in `Sessions/Patches/*.json`, applied via `apply_session_patch.py`, or engine runs). Interactive/handler DB mutations that are *not* captured as a replayable patch are at risk — that is exactly what was lost on June 1–2. Prefer the sanctioned write paths; avoid one-off interactive mutations that cannot be replayed.
- **Drive fallback:** old `G:\My Drive\Bible_study_projects` is retained as a fallback only — never the working copy. ⚠ **Scripts must not hardcode the Drive path** (e.g. `_integrity_full_check.py` was fixed 2026-06-14 to resolve the DB relative to the script).

## 3. The file manifest

- `database/file_manifest.json` — whole-tree index (every file, including archives) with a `currency` signal (`current` · `cross-reference` · `historical` · `backup` · `archived`).
- **Rebuild:** `python scripts/build_file_manifest.py` — after file moves, session-log processing, or creating files. **Search:** `--search "term"` · `"registry:NNN"` · `"type:..."` · `"currency:current"` · `--stats`.
- **Locate files via the manifest, not by browsing folders** — the folder layout is inconsistent (filing audit pending; see `docs/file-organisation-rules.md` + the filing-audit report).

## 4. Interaction protocols & cost (`docs/interaction-preferences.md`, CLAUDE.md §9)

- **Confirm before non-trivial tasks** — summarise, state approach, wait for approval.
- **All substantive output & workings → a `.md` file** (in `docs/`, `outputs/`, or a relevant subfolder); chat is for alerts + a brief summary + a link.
- **Factual discipline:** work from explicit facts; don't guess; verify; stop and ask if unclear. **Never reconstruct DB/architecture state from row counts (that is fabrication) — use the written record + manifest, and cite the source.**
- **File org & versioning:** follow `docs/file-organisation-rules.md`; same base name ⇒ version bump (`-vN`); archive superseded versions; never overwrite a prior version in place; **never silently change a report's shape — version it** (see `docs/reusable-scripts-catalogue.md`).
- **Cost awareness:** advise the cheaper path before acting — Opus on routine pipeline work, whole-file reads vs targeted Read/Grep, subagents vs a direct query, duplicate artefacts, dry-run then live.

## 5. Related governance

`docs/file-organisation-rules.md` (filing) · `docs/reusable-scripts-catalogue.md` (reusable scripts) · `docs/project-orientation-core-memory-map.md` (the entry-point map) · `Workflow/Global_rules/wa-global-rules-all-v2` (GR-* rules).

> **Note:** this doc closes the "no consolidated operational-governance doc" gap recorded in the 2026-06-14 reconstruction (02). CLAUDE.md §9/§12/§13 remain as the compact summary; this is the authoritative detail.
