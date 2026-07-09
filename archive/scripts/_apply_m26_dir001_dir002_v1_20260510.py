"""_apply_m26_dir001_dir002_v1_20260510.py — DB-modifying.

Apply two cluster-process directives for M26 — REVISED 2026-05-10
under the "BOUNDARY-as-staging" framing confirmed by researcher:

  DIR-M26-20260510-001 — M26-A2 description update; the 10 (revised:
                         11) vc reassignments are realised as
                         soft-deletes of redundant sibling rows
  DIR-M26-20260510-002 — M26-A1 description update + reassign 11
                         vc rows (the originals) from M26-A1 to
                         M26-BOUNDARY

Why the revision: the M26-A apply script created sibling vc rows for
the 11 'both' verses (DEC-3 of m39), giving each verse two active vc
rows (M26-A1 + M26-A2). Under the 'staging-then-promote' model,
'both' verses sit in BOUNDARY as single rows awaiting analytical
promotion — the DEC-3 sibling pattern was over-engineered. Applying
both directives literally as written would cause UNIQUE-constraint
collisions when both copies converge on the same BOUNDARY slot.

Resolution:
  - DIR-002's 11 M26-A1 originals are moved (UPDATE) to M26-BOUNDARY
  - DIR-001's vc reassignment is realised as SOFT-DELETE of the
    redundant M26-A2 siblings (all 11, including vr_id 25168 which
    DIR-001 did not list — under the staging model it's a redundant
    sibling regardless)
  - Each soft-deleted vc row gets a note explaining provenance

Operations (single transaction, foreign_keys=ON):

  Op-1a  UPDATE cluster_subgroup.core_description for M26-A2
  Op-1b  UPDATE cluster_subgroup.core_description for M26-A1
  Op-2a  UPDATE verse_context SET cluster_subgroup_id=<BOUNDARY>
         for the 11 M26-A1 originals (DIR-002)
  Op-2b  UPDATE verse_context SET delete_flagged=1, notes=...
         for the 11 M26-A2 siblings of all 11 'both' vr_ids

NO API calls. ~1 sec wall time. No cost.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

DIR1_REF = "DIR-M26-20260510-001"
DIR2_REF = "DIR-M26-20260510-002"

DIR1_VR_IDS = [93748, 93750, 28726, 25165, 28307, 25190, 25214, 93744,
               169505, 28747]
DIR2_VR_IDS = [93748, 93750, 28726, 25165, 28307, 25168, 25190, 25214,
               93744, 169505, 28747]

DIR1_DESC = (
    "Located in the character, conduct, and covenantal standing of the "
    "human person; the term names the state of being rightly oriented "
    "toward God and toward others — a governing inner condition from "
    "which just thought, truthful speech, generous action, stability "
    "under adversity, and appropriate response to God (fear, trust, "
    "joy, prayer) all flow. The state is never directly defined in the "
    "text; its content is evidenced by what the righteous person is "
    "and does. It is assessed before God, not before human observers. "
    "Structurally opposed by wickedness (rasha, M26-G) and injustice "
    "(aval, M26-G). Distinguished from M26-A1 (God's own righteousness) "
    "and from M26-C (the divine act of declaring a person righteous). "
    "Verses where both God and a human person are foregrounded as "
    "active subjects are held in M26-BOUNDARY."
)

DIR2_DESC = (
    "Located in the character, judgments, acts, and covenant "
    "faithfulness of God himself; the term names God's own "
    "righteousness — a foundational, permanent attribute that is "
    "self-grounded, never defined in the text but consistently "
    "evidenced by what God is and does. God's righteousness is "
    "expressed through judgments that conform to what is right, "
    "through covenant faithfulness that extends across generations, "
    "and through saving acts directed toward his people. It is the "
    "standard against which human unrighteousness is measured, and "
    "the ground on which his people appeal for deliverance. In the "
    "NT, God's righteousness is revealed through the gospel and "
    "resolved through the cross — where the justice/mercy tension is "
    "explicitly reconciled by the declaration that God is "
    "simultaneously just and the justifier of those who have faith. "
    "The sub-group also includes messianic verses where the "
    "Righteous One (Christ) is defined by this quality and where "
    "God's righteousness becomes the means of transfer to human "
    "persons. Distinguished from M26-A2 (human righteousness) and "
    "from M26-C (the divine act of declaring a person righteous). "
    "Verses where both God and a human person are foregrounded as "
    "active subjects are held in M26-BOUNDARY."
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    path = os.path.join(BACKUP_DIR,
                        f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, path)
    return path


def get_subgroup_ids(conn) -> dict:
    rows = conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    ).fetchall()
    return {r[0]: r[1] for r in rows}


def preflight(conn):
    msgs = []
    ok = True
    sg = get_subgroup_ids(conn)
    needed = {"M26-A1", "M26-A2", "M26-BOUNDARY"}
    missing = needed - set(sg.keys())
    if missing:
        msgs.append(f"[ERR] missing sub-groups: {sorted(missing)}")
        return False, msgs, sg
    msgs.append(f"[ok] M26-A1={sg['M26-A1']} · M26-A2={sg['M26-A2']} · "
                f"M26-BOUNDARY={sg['M26-BOUNDARY']}")

    # For DIR-001: each vr_id in DIR1_VR_IDS must have AT LEAST ONE
    # active vc row at M26-A2.
    ph1 = ",".join("?" * len(DIR1_VR_IDS))
    found_dir1 = {
        r[0]: r[1] for r in conn.execute(
            f"SELECT verse_record_id, COUNT(*) FROM verse_context "
            f" WHERE verse_record_id IN ({ph1}) "
            f"   AND cluster_subgroup_id=? "
            f"   AND COALESCE(delete_flagged,0)=0 "
            f" GROUP BY verse_record_id",
            (*DIR1_VR_IDS, sg["M26-A2"]),
        )
    }
    missing_dir1 = [v for v in DIR1_VR_IDS if v not in found_dir1]
    if missing_dir1:
        msgs.append(f"[ERR] DIR-001: {len(missing_dir1)} vr_ids have no "
                    f"active vc row in M26-A2: {missing_dir1}")
        ok = False
    else:
        msgs.append(f"[ok] DIR-001: all {len(DIR1_VR_IDS)} vr_ids resolve "
                    f"to active M26-A2 vc rows")

    # For DIR-002: each vr_id in DIR2_VR_IDS must have AT LEAST ONE
    # active vc row at M26-A1.
    ph2 = ",".join("?" * len(DIR2_VR_IDS))
    found_dir2 = {
        r[0]: r[1] for r in conn.execute(
            f"SELECT verse_record_id, COUNT(*) FROM verse_context "
            f" WHERE verse_record_id IN ({ph2}) "
            f"   AND cluster_subgroup_id=? "
            f"   AND COALESCE(delete_flagged,0)=0 "
            f" GROUP BY verse_record_id",
            (*DIR2_VR_IDS, sg["M26-A1"]),
        )
    }
    missing_dir2 = [v for v in DIR2_VR_IDS if v not in found_dir2]
    if missing_dir2:
        msgs.append(f"[ERR] DIR-002: {len(missing_dir2)} vr_ids have no "
                    f"active vc row in M26-A1: {missing_dir2}")
        ok = False
    else:
        msgs.append(f"[ok] DIR-002: all {len(DIR2_VR_IDS)} vr_ids resolve "
                    f"to active M26-A1 vc rows")

    return ok, msgs, sg


def run_apply(conn, sg):
    cur = conn.cursor()
    counts = {}
    ts = now_iso()
    SOFT_DELETE_NOTE = (
        "Soft-deleted 2026-05-10 (DIR-001 + DIR-002 apply): redundant "
        "DEC-3 sibling vc row. The 'both'-classified verse is held in "
        "M26-BOUNDARY as a single row (the M26-A1 original moved by "
        "DIR-002) under the staging-then-promote model."
    )

    # Op-1a — DIR-001 description update
    rc = cur.execute(
        "UPDATE cluster_subgroup "
        "   SET core_description=?, last_updated_date=? "
        " WHERE cluster_code='M26' AND subgroup_code='M26-A2'",
        (DIR1_DESC, ts),
    ).rowcount
    counts["dir001_description_update"] = rc
    print(f"  [Op-1a] M26-A2 description updated: {rc} row")

    # Op-1b — DIR-002 description update
    rc = cur.execute(
        "UPDATE cluster_subgroup "
        "   SET core_description=?, last_updated_date=? "
        " WHERE cluster_code='M26' AND subgroup_code='M26-A1'",
        (DIR2_DESC, ts),
    ).rowcount
    counts["dir002_description_update"] = rc
    print(f"  [Op-1b] M26-A1 description updated: {rc} row")

    # Op-2a — DIR-002: UPDATE the 11 M26-A1 originals → M26-BOUNDARY.
    # Done before Op-2b so the BOUNDARY slot is occupied by the original
    # before its sibling is soft-deleted (provenance is preserved).
    ph2 = ",".join("?" * len(DIR2_VR_IDS))
    rc = cur.execute(
        f"UPDATE verse_context "
        f"   SET cluster_subgroup_id=? "
        f" WHERE verse_record_id IN ({ph2}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (sg["M26-BOUNDARY"], *DIR2_VR_IDS, sg["M26-A1"]),
    ).rowcount
    counts["dir002_vc_moved_A1_to_BOUNDARY"] = rc
    print(f"  [Op-2a] DIR-002 vc moves M26-A1 → M26-BOUNDARY: {rc} "
          f"(expected 11)")

    # Op-2b — DIR-001 (revised): SOFT-DELETE the M26-A2 sibling rows
    # for ALL 11 'both' vr_ids (DIR2_VR_IDS — DIR-001 listed only 10
    # but the 11th, vr_id 25168, is also a redundant sibling under the
    # staging model). Note appended for audit trail.
    rc = cur.execute(
        f"UPDATE verse_context "
        f"   SET delete_flagged=1, "
        f"       notes=COALESCE(notes || ' | ', '') || ? "
        f" WHERE verse_record_id IN ({ph2}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (SOFT_DELETE_NOTE, *DIR2_VR_IDS, sg["M26-A2"]),
    ).rowcount
    counts["dir001_vc_siblings_soft_deleted"] = rc
    print(f"  [Op-2b] DIR-001 soft-deletes 'both' siblings at M26-A2: "
          f"{rc} (expected 11 — 10 from DIR-001 list + vr_id 25168)")

    return counts


def verify(conn, sg):
    invariants = {}

    # Counts per relevant sub-group (active, not set-aside)
    for code in ("M26-A1", "M26-A2", "M26-BOUNDARY"):
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context vc "
            " WHERE vc.cluster_subgroup_id=? "
            "   AND COALESCE(vc.delete_flagged,0)=0",
            (sg[code],),
        ).fetchone()[0]
        invariants[f"active vc rows in {code}"] = n

    # All 11 'both' vr_ids: zero ACTIVE rows remain at M26-A1 or M26-A2
    ph2 = ",".join("?" * len(DIR2_VR_IDS))
    n = conn.execute(
        f"SELECT COUNT(*) FROM verse_context "
        f" WHERE verse_record_id IN ({ph2}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (*DIR2_VR_IDS, sg["M26-A1"]),
    ).fetchone()[0]
    invariants["'both' vr_ids still ACTIVE in M26-A1 (expected 0)"] = n

    n = conn.execute(
        f"SELECT COUNT(*) FROM verse_context "
        f" WHERE verse_record_id IN ({ph2}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (*DIR2_VR_IDS, sg["M26-A2"]),
    ).fetchone()[0]
    invariants["'both' vr_ids still ACTIVE in M26-A2 (expected 0)"] = n

    # 11 'both' vr_ids land in BOUNDARY (one active row per vr_id)
    n = conn.execute(
        f"SELECT COUNT(*) FROM verse_context "
        f" WHERE verse_record_id IN ({ph2}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (*DIR2_VR_IDS, sg["M26-BOUNDARY"]),
    ).fetchone()[0]
    invariants["'both' vr_ids ACTIVE in M26-BOUNDARY (expected 11)"] = n

    # Sibling soft-deletes: 11 'both' vr_ids should each have a
    # delete_flagged=1 sibling at M26-A2
    n = conn.execute(
        f"SELECT COUNT(*) FROM verse_context "
        f" WHERE verse_record_id IN ({ph2}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND delete_flagged=1",
        (*DIR2_VR_IDS, sg["M26-A2"]),
    ).fetchone()[0]
    invariants["'both' siblings soft-deleted at M26-A2 (expected 11)"] = n

    # Description sanity (first 80 chars match expected prefix)
    for code, expect_prefix in (
        ("M26-A1", DIR2_DESC[:80]),
        ("M26-A2", DIR1_DESC[:80]),
    ):
        actual = conn.execute(
            "SELECT core_description FROM cluster_subgroup "
            " WHERE cluster_code='M26' AND subgroup_code=?",
            (code,),
        ).fetchone()[0]
        ok = (actual or "").startswith(expect_prefix)
        invariants[f"{code} description matches expected prefix"] = ok

    return invariants


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2
    if args.dry_run and args.live:
        print("ERROR: --dry-run and --live are mutually exclusive",
              file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"M26 directives apply  ({DIR1_REF} + {DIR2_REF})")
    print(f"  Mode: {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:   {DB_PATH}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs, sg = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed — exiting without changes.")
        return 1

    if args.live:
        print("Taking pre-apply backup...")
        b = take_backup("m26_dir001_dir002")
        print(f"  Backup saved: {b}")
        print()

    print("EXECUTE")
    print("-" * 72)
    try:
        conn.execute("BEGIN")
        counts = run_apply(conn, sg)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fk_violations = list(conn.execute("PRAGMA foreign_key_check"))
        if fk_violations:
            print(f"  [ERR] {len(fk_violations)} FK violations")
            raise RuntimeError("foreign_key_check failed")
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn, sg)
        for k, v in invariants.items():
            print(f"  {k}: {v}")
        print()
        if args.dry_run:
            conn.execute("ROLLBACK")
            print("DRY-RUN: changes rolled back.")
        else:
            conn.execute("COMMIT")
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {type(e).__name__}: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:45s} {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
