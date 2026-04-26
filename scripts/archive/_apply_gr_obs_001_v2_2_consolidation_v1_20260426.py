"""_apply_gr_obs_001_v2_2_consolidation_v1_20260426.py

One-off applier — bakes the v3 consolidation draft (gr-obs-001-consolidation-draft-v3-20260426.md)
into wa_rule_registry.

Actions (single transaction):
  1. UPDATE GR-OBS-001 → version=2_2 with new subject, rule_text, application_notes, last_modified.
  2. UPDATE GR-OBS-003 → obsolete=1 with superseded_by/obsolete_reason.
  3. UPDATE GR-OBS-004 → obsolete=1 with superseded_by/obsolete_reason.

Run with --dry-run first; commits only with --live. Verifies post-state by reading rows back.

This script is single-use; archive to scripts/archive/ after the run.
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")

NEW_SUBJECT = "Observations log — write discipline, segmentation, and filename convention"
NEW_VERSION = "2_2"

NEW_RULE_TEXT = (
    "The observations log — referred to as the obslog — is the authoritative record of every session's "
    "working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); "
    "no substantive work may begin until it exists. While the session is live, every finding, decision, "
    "gap, patch consequence, and open question is written to the obslog at the moment it is determined. "
    "Every substantive chat output also appears in the obslog. When a researcher message is received, "
    "the researcher's feedback is recorded verbatim in the obslog before a response is formulated. "
    "At every pass close, items requiring database persistence are written via a patch or directive, "
    "and a fresh extract confirming the write becomes the working source for the next pass. "
    "This discipline persists for the life of the session.\n\n"
    "The obslog and the session log are separate files with separate purposes. The obslog is the "
    "working paper, written continuously as defined above. The session log is the handoff record, "
    "produced at session close. A session that closes without a session log has not closed cleanly — "
    "the session log is always produced before the session ends.\n\n"
    "The obslog filename is version-incremented within the same session, at the end of a logical "
    "session batch, to keep the working file in manageable segments. The version bump is for size "
    "control, not for marking a new working scope: each new version continues the same logical obslog "
    "trail without loss of continuity. A version bump is not triggered by per-save writes within a "
    "batch, only by the close of a logical batch.\n\n"
    "The obslog filename follows the pattern "
    "`wa-obslog-[reference]-[session-name-abbreviated]-[version]-[date]`, where `reference` is "
    "declared at session startup (default `ref`), `session-name-abbreviated` is a short topic token "
    "(lowercase, hyphens only, maximum 16 characters), `version` follows GR-FILE-003 "
    "(`v1`, `v2`, …), and `date` follows GR-FILE-009 (`YYYYMMDD`). This pattern is a carve-out from "
    "GR-FILE-001's standard `[prefix]-[reference]-[short description]-[version]-[date]` order: for "
    "obslogs, the literal token `obslog` sits between the `wa-` prefix and the reference, so that "
    "all observation logs sort together regardless of their reference.\n\n"
    "This rule is non-waivable."
)

NEW_APPLICATION_NOTES = (
    "Compliance test. A useful shorthand: if something is not in the observations log, it has not "
    "been received or done. This is not literal — the thought existed — but it captures the rule's "
    "operational meaning: nothing that is only in chat or in memory counts as work.\n\n"
    "Capture scope. The list of content types caught by continuous-write includes: findings, "
    "decisions, gaps, patch consequences, flags, open questions, clarification requests, and "
    "researcher feedback verbatim. New content types arising in a session are logged on the same "
    "discipline.\n\n"
    "Verbatim researcher capture. 'Verbatim' means the researcher's message is reproduced exactly, "
    "not paraphrased or summarised. If the message is long, the full text is still captured; "
    "summaries appear elsewhere in the log if needed.\n\n"
    "Logical batch boundary for version bumps. A logical batch is a coherent unit of work declared "
    "at startup or at the boundary itself — for example, processing batch 1 of N within a registry, "
    "or a clean Q&A round close. The bump is initiated at an explicit pause point, not by file size "
    "alone (file size is the reason the rule exists, but not the trigger — the trigger is the "
    "logical close).\n\n"
    "New session vs new batch. Crossing into a new session resets the obslog to a new file (new "
    "session-name-abbreviated, version reset to v1). Bumps within a single session continue under "
    "the same session-name-abbreviated and increment v1 → v2 → v3 …. The obslog never spans two "
    "sessions in the same file.\n\n"
    "Reference defaulting. If the researcher does not declare a reference at startup, the obslog "
    "filename uses `ref`. The reference identifies the working scope (e.g. a registry, a cluster, "
    "a programme-wide pass) and is set once per session.\n\n"
    "Session-name abbreviation. The token must be ≤ 16 characters, lowercase, hyphens only — chosen "
    "to keep total filename length short while preserving recognisability of the session topic. "
    "Examples: rules-review, flags-valid, vc-review, regmgmt, preamble. If a topic cannot be "
    "expressed in 16 characters, abbreviate aggressively rather than truncate (e.g. database-review "
    "→ db-review).\n\n"
    "Forward-only application. Existing obslog files predating GR-OBS-001 v2_2 are not retro-"
    "renamed. The new pattern applies to all obslogs created from this rule's effective date onward."
)

OBS_003_REASON = (
    "Substance folded into GR-OBS-001 v2_2 (obslog vs session log clause; batch-boundary trigger "
    "for session log dropped). Consolidated 2026-04-26."
)
OBS_004_REASON = (
    "Substance folded into GR-OBS-001 v2_2 (version increment clause; semantic reversed from "
    "new-session bump to in-session batch boundary). Consolidated 2026-04-26."
)
SUPERSEDED_BY = "GR-OBS-001 v2_2"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_state(conn: sqlite3.Connection, label: str) -> None:
    print(f"--- state ({label}) ---")
    rows = conn.execute(
        "SELECT rule_id, category, version, obsolete, superseded_by, "
        "       SUBSTR(subject,1,90) AS subj, LENGTH(rule_text) AS rt_len, "
        "       LENGTH(application_notes) AS an_len, last_modified "
        "FROM wa_rule_registry WHERE rule_id IN ('GR-OBS-001','GR-OBS-003','GR-OBS-004') "
        "ORDER BY rule_id"
    ).fetchall()
    for r in rows:
        print(
            f"  {r['rule_id']:12s} cat={r['category']:24s} v{r['version']:5s} "
            f"obs={r['obsolete']} sup={r['superseded_by'] or '-':18s} "
            f"rt_len={r['rt_len']} an_len={r['an_len'] or 0} lm={r['last_modified']}"
        )
        print(f"    subj: {r['subj']}")


def apply(conn: sqlite3.Connection, dry_run: bool) -> None:
    ts = now_iso()

    # GR-OBS-001 → v2_2
    conn.execute(
        """UPDATE wa_rule_registry
              SET subject = ?, version = ?, rule_text = ?, application_notes = ?,
                  last_modified = ?
            WHERE rule_id = 'GR-OBS-001'""",
        (NEW_SUBJECT, NEW_VERSION, NEW_RULE_TEXT, NEW_APPLICATION_NOTES, ts),
    )

    # GR-OBS-003 → obsolete
    conn.execute(
        """UPDATE wa_rule_registry
              SET obsolete = 1, obsolete_reason = ?, superseded_by = ?, last_modified = ?
            WHERE rule_id = 'GR-OBS-003'""",
        (OBS_003_REASON, SUPERSEDED_BY, ts),
    )

    # GR-OBS-004 → obsolete
    conn.execute(
        """UPDATE wa_rule_registry
              SET obsolete = 1, obsolete_reason = ?, superseded_by = ?, last_modified = ?
            WHERE rule_id = 'GR-OBS-004'""",
        (OBS_004_REASON, SUPERSEDED_BY, ts),
    )

    if dry_run:
        print("\n[DRY-RUN] rolling back all changes")
        conn.rollback()
    else:
        conn.commit()
        print("\n[LIVE] committed.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true", help="commit changes (default: dry-run)")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    read_state(conn, "before")
    apply(conn, dry_run=not args.live)
    # Re-open to read committed state cleanly when --live
    if args.live:
        conn.close()
        conn = sqlite3.connect(args.db)
        conn.row_factory = sqlite3.Row
    read_state(conn, "after")
    return 0


if __name__ == "__main__":
    sys.exit(main())
