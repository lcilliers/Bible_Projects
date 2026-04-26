"""_apply_outlier1_extraction_anomaly_delete_v1_20260426.py

Outlier-1 corrective action: mark 6 extraction-anomaly terms (function words,
demonstratives, pronouns, animals, proper-noun fragments) as status='delete'.
All sit in legacy-Complete registries with `vc_status=not_done`, lumped into
a single catch-all group with hundreds of verses each — the diligence pattern
at registry-residue scale.

Targets:
  - H2088  "this"     in reg 99 kindness        (mti=951, ti=1006, 245v, 17 vc_rows)
  - H0369  "nothing"  in reg 142 self-control   (mti=1110, ti=1202, 218v, 1 vc_row)
  - H0595  "I"        in reg 140 seeking        (mti=1102, ti=1192, 156v, 1 vc_row)
  - H5704  "till"     in reg 173 will           (mti=1236, ti=1367, 260v, 13 vc_rows)
  - H0352A "ram"      in reg 187 strength       (mti=7013, ti=7081, 139v, 12 vc_rows)
  - H4997  "wineskin" in reg 213 listen         (mti=7499, ti=7566, 6v, 6 vc_rows)

Actions (single transaction):
  1. mti_terms.status='delete' on the 6 mti_ids.
  2. wa_verse_records.delete_flagged=1 on all active verses for the 6 ti_ids.
  3. verse_context.delete_flagged=1 on all active vc rows for the 6 mti_ids.
  4. verse_context_group.delete_flagged=1 on all active groups for the 6 mti_ids.

Justification (audit trail):
  Same precedent as today's diligence registry exclusion (reg 48) and the
  H4639H/I status fix (reg 98). Outlier scan 2026-04-26 surfaced the pattern;
  the 6 selected are unambiguous extraction anomalies (Hebrew function words
  and concrete-noun fragments) that lump into 1-group catch-alls and have
  not yet been touched by v3 VC. Cleaning them now removes wasted classifier
  cycles when each registry next rolls through VC. Verses preserved as
  delete_flagged=1 (soft delete, reversible).

Run --dry-run first; commits only with --live. Archive after run.
"""
from __future__ import annotations
import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")

TARGETS = [
    # (mti_id, ti_id, strongs, gloss, reg, word)
    (951,  1006, "H2088",  "this",     99,  "kindness"),
    (1110, 1202, "H0369",  "nothing",  142, "self-control"),
    (1102, 1192, "H0595",  "I",        140, "seeking"),
    (1236, 1367, "H5704",  "till",     173, "will"),
    (7013, 7081, "H0352A", "ram",      187, "strength"),
    (7499, 7566, "H4997",  "wineskin", 213, "listen"),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_state(conn, label):
    print(f"--- state ({label}) ---")
    cur = conn.cursor()
    for mti_id, ti_id, strongs, gloss, reg, word in TARGETS:
        cur.execute("SELECT status, last_changed FROM mti_terms WHERE id=?", (mti_id,))
        s, lc = cur.fetchone()
        cur.execute(
            "SELECT COUNT(*) AS active, SUM(CASE WHEN delete_flagged=1 THEN 1 ELSE 0 END) AS deleted "
            "FROM wa_verse_records WHERE term_inv_id=?", (ti_id,))
        v = cur.fetchone()
        cur.execute(
            "SELECT SUM(CASE WHEN delete_flagged=0 THEN 1 ELSE 0 END) AS active, "
            "       SUM(CASE WHEN delete_flagged=1 THEN 1 ELSE 0 END) AS deleted "
            "FROM verse_context WHERE mti_term_id=?", (mti_id,))
        vc = cur.fetchone()
        cur.execute(
            "SELECT SUM(CASE WHEN delete_flagged=0 THEN 1 ELSE 0 END) AS active, "
            "       SUM(CASE WHEN delete_flagged=1 THEN 1 ELSE 0 END) AS deleted "
            "FROM verse_context_group WHERE mti_term_id=?", (mti_id,))
        g = cur.fetchone()
        active_v = v[0] - (v[1] or 0)  # rough; the active count equals total - deleted
        cur.execute(
            "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id=? AND delete_flagged=0", (ti_id,))
        active_v = cur.fetchone()[0]
        print(f"  reg {reg:3d} {word:13s} {strongs:7s} mti={mti_id:5d} ti={ti_id:5d}  "
              f"status={s:10s}  verses(active/deleted)={active_v}/{v[1] or 0}  "
              f"vc({vc[0] or 0}/{vc[1] or 0})  groups({g[0] or 0}/{g[1] or 0})")


def apply(conn, dry_run):
    ts = now_iso()
    cur = conn.cursor()

    mti_ids = [t[0] for t in TARGETS]
    ti_ids = [t[1] for t in TARGETS]
    placeholders_mti = ",".join(["?"] * len(mti_ids))
    placeholders_ti = ",".join(["?"] * len(ti_ids))

    # 1. mti_terms → delete
    cur.execute(
        f"UPDATE mti_terms SET status='delete', last_changed=? WHERE id IN ({placeholders_mti})",
        (ts, *mti_ids),
    )
    print(f"  mti_terms updated: {cur.rowcount}")
    assert cur.rowcount == len(mti_ids), f"expected {len(mti_ids)} mti_terms updated, got {cur.rowcount}"

    # 2. wa_verse_records → soft-delete
    cur.execute(
        f"UPDATE wa_verse_records SET delete_flagged=1, last_changed=? "
        f"WHERE term_inv_id IN ({placeholders_ti}) AND delete_flagged=0",
        (ts, *ti_ids),
    )
    print(f"  wa_verse_records soft-deleted: {cur.rowcount}")

    # 3. verse_context → soft-delete (orphaned classification rows)
    cur.execute(
        f"UPDATE verse_context SET delete_flagged=1 "
        f"WHERE mti_term_id IN ({placeholders_mti}) AND delete_flagged=0",
        mti_ids,
    )
    print(f"  verse_context soft-deleted: {cur.rowcount}")

    # 4. verse_context_group → soft-delete (orphaned groups)
    cur.execute(
        f"UPDATE verse_context_group SET delete_flagged=1 "
        f"WHERE mti_term_id IN ({placeholders_mti}) AND delete_flagged=0",
        mti_ids,
    )
    print(f"  verse_context_group soft-deleted: {cur.rowcount}")

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
    print()
    apply(conn, dry_run=not args.live)
    print()
    if args.live:
        conn.close()
        conn = sqlite3.connect(args.db)
    read_state(conn, "after")
    return 0


if __name__ == "__main__":
    sys.exit(main())
