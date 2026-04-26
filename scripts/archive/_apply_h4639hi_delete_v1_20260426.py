"""_apply_h4639hi_delete_v1_20260426.py

Mark H4639H (mti=3210) and H4639I (mti=3212) as status='delete' and resolve
the corresponding PH2-98-012 / PH2-98-013 quality flags.

Justification (audit-trail):
  - STEP returns 0 verses for both suffix variants; verses tag to parent H4639
    (which is not registered in the project — see investigation 2026-04-26).
  - Same disposition as siblings H4639G (delete), H4639J (candidate_delete),
    H4639K (delete) in the same registry 98 justice.
  - Registry 98 lexical territory already covered by 4 OWNER terms
    (H4941 mishpat, H6664 tsedeq, H6663 tsadaq, H6666 tsedaqah).
  - PH2-98-012/013 say "Independent verse research required before any
    synthesis conclusions"; resolution is term-status fix, not VC classification.

Run --dry-run first; commits only with --live. Single transaction.
Archive to scripts/archive/ after the run.
"""
from __future__ import annotations
import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")

TARGET_TERMS = [
    (3210, "H4639H", "deed: justice"),
    (3212, "H4639I", "deed: judgement"),
]

FLAG_LABELS_TO_RESOLVE = ["PH2-98-012", "PH2-98-013"]

RESOLVE_NOTE = (
    "STEP returns 0 verses for the suffixed variant (verses tag to parent H4639, "
    "which is not registered in the project). Same disposition as siblings "
    "H4639G/J/K. mti_terms.status set to 'delete' on 2026-04-26 — term-status "
    "fix, not VC classification. Registry 98 lexical territory remains covered "
    "by H4941, H6664, H6663, H6666."
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_state(conn, label):
    print(f"--- state ({label}) ---")
    cur = conn.cursor()
    cur.execute(
        "SELECT id, strongs_number, status, last_changed FROM mti_terms "
        "WHERE id IN (?, ?) ORDER BY id",
        (TARGET_TERMS[0][0], TARGET_TERMS[1][0]),
    )
    for r in cur.fetchall():
        print(f"  mti_terms: mti={r[0]} {r[1]:8s} status={r[2]:20s} last_changed={r[3]}")
    cur.execute(
        "SELECT flag_label, flag_code, resolved, resolved_date, "
        "       SUBSTR(COALESCE(resolved_note,''), 1, 80) AS note "
        "FROM wa_session_research_flags WHERE flag_label IN (?, ?) ORDER BY flag_label",
        tuple(FLAG_LABELS_TO_RESOLVE),
    )
    for r in cur.fetchall():
        print(f"  flag: {r[0]:14s} ({r[1]}) resolved={r[2]} date={r[3]} note={r[4]}")


def apply(conn, dry_run):
    ts = now_iso()
    cur = conn.cursor()
    for mti_id, strongs, _gloss in TARGET_TERMS:
        cur.execute(
            "UPDATE mti_terms SET status='delete', last_changed=? WHERE id=?",
            (ts, mti_id),
        )
        assert cur.rowcount == 1, f"expected 1 row updated for mti={mti_id}, got {cur.rowcount}"
    for label in FLAG_LABELS_TO_RESOLVE:
        cur.execute(
            "UPDATE wa_session_research_flags "
            "SET resolved=1, resolved_date=?, resolved_note=? "
            "WHERE flag_label=? AND (resolved=0 OR resolved IS NULL)",
            (ts, RESOLVE_NOTE, label),
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"expected 1 row updated for flag {label}, got {cur.rowcount}")
    if dry_run:
        print("\n[DRY-RUN] rolling back.")
        conn.rollback()
    else:
        conn.commit()
        print("\n[LIVE] committed.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    read_state(conn, "before")
    apply(conn, dry_run=not args.live)
    if args.live:
        conn.close()
        conn = sqlite3.connect(args.db)
    read_state(conn, "after")
    return 0


if __name__ == "__main__":
    sys.exit(main())
