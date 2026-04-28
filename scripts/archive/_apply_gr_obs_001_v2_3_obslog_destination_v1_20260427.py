"""_apply_gr_obs_001_v2_3_obslog_destination_v1_20260427.py

Bump GR-OBS-001 v2_2 → v2_3 with destination-folder rule:

  Obslogs (and session logs) are written to
  `data/imports/WA/Session_B_Analysis/` — the home for word-analysis
  outputs.

This closes the gap that caused obslog files to land in
`data/imports/WA/Patches/` (which is for JSON patches only).

Usage:
  python scripts/archive/_apply_gr_obs_001_v2_3_obslog_destination_v1_20260427.py
  python scripts/archive/_apply_gr_obs_001_v2_3_obslog_destination_v1_20260427.py --live
"""
from __future__ import annotations
import argparse
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


NEW_RULE_TEXT = """The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session.

The obslog and the session log are separate files with separate purposes. The obslog is the working paper, written continuously as defined above. The session log is the handoff record, produced at session close. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.

The obslog filename is version-incremented within the same session, at the end of a logical session batch, to keep the working file in manageable segments. The version bump is for size control, not for marking a new working scope: each new version continues the same logical obslog trail without loss of continuity. A version bump is not triggered by per-save writes within a batch, only by the close of a logical batch.

The obslog filename follows the pattern `wa-obslog-[reference]-[session-name-abbreviated]-[version]-[date]`, where `reference` is declared at session startup (default `ref`), `session-name-abbreviated` is a short topic token (lowercase, hyphens only, maximum 16 characters), `version` follows GR-FILE-003 (`v1`, `v2`, …), and `date` follows GR-FILE-009 (`YYYYMMDD`). This pattern is a carve-out from GR-FILE-001's standard `[prefix]-[reference]-[short description]-[version]-[date]` order: for obslogs, the literal token `obslog` sits between the `wa-` prefix and the reference, so that all observation logs sort together regardless of their reference.

The obslog and its companion session log are written to `data/imports/WA/Session_B_Analysis/` — the home for word-analysis outputs. This folder is the canonical destination for any analytical artefact produced during a Session B analytical pass, including obslogs, session logs, and pre-Architecture-v2 word-analysis `.md` files. The `data/imports/WA/Patches/` folder is reserved for JSON patches only and must not receive obslog or analysis-output files.

This rule is non-waivable."""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR, f"bible_research_pre_gr_obs_001_v2_3_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    ts = now_iso()

    conn = sqlite3.connect(args.db)
    try:
        if args.live:
            conn.execute("BEGIN")

        cur = conn.execute("""
            SELECT id, version, last_modified
              FROM wa_rule_registry
             WHERE rule_id = 'GR-OBS-001' AND (obsolete = 0 OR obsolete IS NULL)
        """).fetchone()
        if not cur:
            print("ERROR: no active GR-OBS-001 row found.")
            return 1

        rule_id, prior_version, prior_modified = cur[0], cur[1], cur[2]
        print(f"Current GR-OBS-001 row: id={rule_id} v={prior_version} mod={prior_modified}")

        if not args.live:
            print("[DRY-RUN] would UPDATE rule_text + bump version → v2_3")
            print(f"           new rule_text length: {len(NEW_RULE_TEXT)} chars")
            return 0

        conn.execute("""
            UPDATE wa_rule_registry
               SET rule_text = ?,
                   version = 'v2_3',
                   last_modified = ?
             WHERE id = ?
        """, (NEW_RULE_TEXT, ts, rule_id))

        conn.commit()
        print("[LIVE] GR-OBS-001 → v2_3 committed.")

    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
