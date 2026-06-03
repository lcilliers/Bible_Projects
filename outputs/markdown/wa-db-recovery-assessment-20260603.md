# DB Recovery Assessment — 2026-06-03

Companion to `wa-db-loss-incident-20260603.md`. **Decision required before any restore.**

---

## 1. Recovery point found

After exhausting cloud (Drive version history = current only; Drive Trash = empty of `.db`),
Recycle Bin, `backups/`, DriveFS cache, VSS, and File History, the **only intact recent
database** is a Google-DriveFS "Lost and Found" conflict copy on the Desktop:

| | Detail |
|---|---|
| File | `Desktop\Google Drive (Not synced) (1)\Lost and Found\bible_research (1779959875006).db` |
| Date | **2026-05-28 10:17** (last engine activity inside: 2026-05-28 06:55Z) |
| Size | 210.5 MB |
| Integrity | `quick_check` = ok, `integrity_check` = ok |
| Schema | **3.28.0** (M54, applied 2026-05-27) — current-generation |
| Twin | A second byte-identical copy exists (same SHA-256) — confirms clean |
| Quarantined to | `C:\Users\lerouxc\db_recovery\candidate_20260528.db` (off-Drive) |

**Next-best fallback:** May-18 copy (187.9 MB) → `db_recovery\fallback_20260518.db`.
Older copies (Apr 19 / Mar 31) also exist but are superseded by the above.

D: and M: drives have no DB copies. The live `bible_research.db` is 0 bytes.

## 2. What the May-28 copy contains (cluster status)

- **Analysis Completed (13):** M03, M04, M06, M07, M08, M09, M10, M10b, M10c, M15, M26, M39, M46
- **Analysis Completed (Terms Added) (3):** M01, M02, M20
- **Ready for re-analysis (1):** M05
- **Structurally Ready (2):** M11, M38
- **Not started (29):** FLAG, T2, and the remaining M-codes

## 3. The gap: May 28 → June 2 (what restoring May-28 loses)

The June 1 and June 2 sessions are **not** in this copy. From git, that window includes:

- **Session 20260601:** cluster auditor build/hardening; **M10c closed** (first through the loop);
  M10b A7 set-aside + B7 surfaced; FLAG-cluster classification applied (triaged to 0);
  mti_terms dedup (106 empty dup rows soft-deleted); orphan-VCG dissolution (125);
  pointer `cluster_link` schema + population; M38 sub-group backfill.
- **Session 20260602:** remediation **orchestrator**; **COMMENT_EVALUATION** model + handler suite;
  **M10b, M38, M08 closed**; programme-wide **dedup-ghost repair** (919 verses);
  **M20** Phase A + C1 + B1a; new audit gates **A10** + **VRACT**.

**Important:** the patch-file query for that window is **empty** — June 1–2 work was applied via
the new handler scripts and interactive COMMENT_EVALUATION, **not** via `Sessions/Patches/*.json`.
So it cannot be replayed by re-running patch files alone. However, all the *decisions, registers,
reports, and the handler scripts themselves are committed in git* and can guide re-doing it.

## 4. Options

**Option A — Restore May-28, redo June 1–2 (recommended).**
Clean, verified, current schema. Cost: re-run the June 1–2 remediation (orchestrator + handlers
exist; decisions documented in committed `.md`s). Realistic and bounded.

**Option B — Restore May-28 and roll forward mechanically where possible.**
Re-run any committed JSON patches in the window first (few/none under `Sessions/Patches/`), then
re-drive the handler-based work. Marginal saving over A because most June 1–2 work was handler/interactive.

**Option C — Keep pursuing the exact 06-02 DB.**
Remaining levers are thin: consumer-Drive file-recovery request to Google support (version history
already shows only the 0-byte current version → low odds). Local recovery of 06-02 is exhausted
(no VSS/shadow copy; DriveFS cache overwritten). Not recommended as the primary path; can run in
parallel with A.

## 5. Restore procedure (when approved) — Drive-safe

1. **Pause Google Drive sync** (tray → pause). Prevents a new conflict during the swap.
2. Copy `db_recovery\candidate_20260528.db` → `database\bible_research.db` (overwriting the 0-byte file).
3. CC verifies in place: `integrity_check`, `schema_version`, `--db-status`, cluster counts.
4. **Resume Drive sync**; confirm it uploads the restored file (watch for a fresh 0-byte/conflict).
5. `python -m engine.engine --migrate --dry-run` to confirm schema currency vs engine `EXPECTED_SCHEMA_VERSION`.
6. Re-establish an **off-Drive backup** immediately (e.g. scheduled copy of the DB to `C:\...\db_recovery\` or the NAS), since `backups/` shares Drive's failure domain.

## 6. Hardening (post-recovery)

- Engine `backups/` lives inside Google Drive → same failure domain as the DB. Add an
  off-Drive backup target (local disk or NAS path that File History covers).
- Consider periodic `VACUUM INTO` snapshots to a non-Drive location, retained independently.
