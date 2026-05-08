"""_apply_m06_subgroup_assignments_v1_20260506.py — DB-modifying.

Executes DIR-20260506-001 (wa-global-dir-001-m06-subgroup-assign-v1-20260506):

  Operation A — seed 8 cluster_subgroup rows for M06 and assign 34 M06
  terms to their sub-group via mti_terms.cluster_subgroup_id.

  Operation B — reassign 2 terms (H6887E tsa.rar, H7520 ra.tsad) out of
  M06 into M28 (Envy, Greed and Lust). Their primary inner-being content
  is envy/jealousy.

Sub-group structure approved in obslog Exchange 11 (OQ-002):
  M06-A Hatred · M06-B Contempt · M06-C Abhorrence ·
  M06-D Cruelty/Ruthlessness · M06-E Reproach · M06-F Hostility/Enmity ·
  M06-G Malice · BOUNDARY Boundary/expression

Schema dependency: cluster_subgroup table + mti_terms.cluster_subgroup_id
(both established by _apply_cluster_subgroup_schema_v1_20260506.py / M44 /
schema 3.18.0).

No verse_context / verse_context_group / wa_dimension_index / prose_section
rows are touched. Idempotent: re-running detects existing sub-groups and
skips / re-applies cleanly. Backed up first.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

DIRECTIVE_ID = "DIR-20260506-001"
DIRECTIVE_FILE = (
    "Sessions/Session_Clusters/M06/"
    "wa-global-dir-001-m06-subgroup-assign-v1-20260506.md"
)

# ---- Sub-groups (Operation A) -----------------------------------------------

SUBGROUPS = [
    # (subgroup_code, label, sort_order, core_description)
    ("M06-A", "Hatred", 1,
     "Sustained inner hostility directed at a person."),
    ("M06-B", "Contempt", 2,
     "Inner posture of regarding as beneath regard."),
    ("M06-C", "Abhorrence", 3,
     "Visceral moral revulsion from evil or the repugnant."),
    ("M06-D", "Cruelty/Ruthlessness", 4,
     "Character disposition of merciless destructiveness."),
    ("M06-E", "Reproach", 5,
     "Experienced condition of public contempt and shame."),
    ("M06-F", "Hostility/Enmity", 6,
     "Relational posture of structured opposition."),
    ("M06-G", "Malice", 7,
     "Compound inner disposition: hostility + contempt + soul-level "
     "pleasure in another's destruction."),
    ("BOUNDARY", "Boundary/expression", 8,
     "Edge-of-scope characteristics — expressive acts, quality terms, "
     "character disorder, or metaphorical usage; retained in M06 with "
     "explicit boundary marker, not internally sub-grouped."),
]

# (strongs_number, subgroup_code) for the 34 M06 terms
TERM_ASSIGNMENTS = [
    # M06-A Hatred (5)
    ("H8130", "M06-A"), ("H8131", "M06-A"), ("H8135", "M06-A"),
    ("H7852", "M06-A"), ("H4895", "M06-A"),
    # M06-B Contempt (6)
    ("H0959", "M06-B"), ("H5006", "M06-B"), ("H0937", "M06-B"),
    ("H7590", "M06-B"), ("H0963", "M06-B"), ("H5007B", "M06-B"),
    # M06-C Abhorrence (5)
    ("H8581", "M06-C"), ("G0948", "M06-C"), ("H1860", "M06-C"),
    ("H8263", "M06-C"), ("H8374", "M06-C"),
    # M06-D Cruelty/Ruthlessness (4)
    ("H0394", "M06-D"), ("H0393", "M06-D"), ("H0395", "M06-D"),
    ("H6184", "M06-D"),
    # M06-E Reproach (5)
    ("H2781", "M06-E"), ("H8103", "M06-E"), ("G5195", "M06-E"),
    ("H8146", "M06-E"), ("H5007A", "M06-E"),
    # M06-F Hostility/Enmity (4)
    ("H0340", "M06-F"), ("H3401", "M06-F"), ("G0476", "M06-F"),
    ("H7009", "M06-F"),
    # M06-G Malice (1)
    ("H7589", "M06-G"),
    # BOUNDARY (4)
    ("H2778A", "BOUNDARY"), ("H0887", "BOUNDARY"),
    ("G0865", "BOUNDARY"), ("H7850", "BOUNDARY"),
]
assert len(TERM_ASSIGNMENTS) == 34

# Operation B — out of M06, into M28
REASSIGN = [
    ("H6887E", "M28"),
    ("H7520",  "M28"),
]

EXPECTED_COUNTS = {
    "M06-A": 5, "M06-B": 6, "M06-C": 5, "M06-D": 4,
    "M06-E": 5, "M06-F": 4, "M06-G": 1, "BOUNDARY": 4,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m06_subgroups.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def main() -> int:
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Pre-flight: capture untouched-table row counts
    pre_counts = {}
    for tbl in ("verse_context", "verse_context_group",
                "wa_dimension_index", "prose_section"):
        r = conn.execute(f"SELECT COUNT(*) AS n FROM {tbl}").fetchone()
        pre_counts[tbl] = r["n"]

    # Pre-flight: every Strong's must exist in mti_terms
    all_strongs = (
        [s for s, _ in TERM_ASSIGNMENTS]
        + [s for s, _ in REASSIGN]
    )
    placeholders = ",".join("?" * len(all_strongs))
    found = {
        r["strongs_number"]: r["id"]
        for r in conn.execute(
            f"SELECT id, strongs_number FROM mti_terms "
            f"WHERE strongs_number IN ({placeholders}) "
            f"  AND COALESCE(delete_flagged,0)=0",
            all_strongs,
        ).fetchall()
    }
    missing = [s for s in all_strongs if s not in found]
    if missing:
        print(f"✗ Missing Strong's in mti_terms: {missing}")
        return 2
    print(f"All {len(all_strongs)} Strong's resolved in mti_terms.\n")

    try:
        conn.execute("BEGIN")

        # ---- Operation A — sub-group rows (upsert by cluster_code+code) ----
        sg_id_by_code = {}
        for code, label, sort_order, descr in SUBGROUPS:
            existing = conn.execute(
                "SELECT id FROM cluster_subgroup "
                "WHERE cluster_code='M06' AND subgroup_code=?",
                (code,),
            ).fetchone()
            if existing:
                conn.execute(
                    "UPDATE cluster_subgroup "
                    "   SET label=?, sort_order=?, core_description=?, "
                    "       status=?, version=?, source=?, "
                    "       last_updated_date=? "
                    " WHERE id=?",
                    (label, sort_order, descr, "Data - In Progress", "v1",
                     f"{DIRECTIVE_ID}", now_iso(), existing["id"]),
                )
                sg_id_by_code[code] = existing["id"]
            else:
                cur = conn.execute(
                    "INSERT INTO cluster_subgroup "
                    "  (cluster_code, subgroup_code, label, "
                    "   core_description, sort_order, status, version, "
                    "   source, delete_flagged, created_at, "
                    "   last_updated_date) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)",
                    ("M06", code, label, descr, sort_order,
                     "Data - In Progress", "v1", DIRECTIVE_ID,
                     now_iso(), now_iso()),
                )
                sg_id_by_code[code] = cur.lastrowid

        # ---- Operation A — assign 34 mti_terms.cluster_subgroup_id -------
        a_results = []
        for sn, code in TERM_ASSIGNMENTS:
            mti_id = found[sn]
            sg_id = sg_id_by_code[code]
            cur = conn.execute(
                "UPDATE mti_terms SET cluster_subgroup_id=? "
                " WHERE id=?",
                (sg_id, mti_id),
            )
            a_results.append((sn, code, sg_id, cur.rowcount))

        # ---- Operation B — reassign cluster_code -------------------------
        b_results = []
        for sn, new_cluster in REASSIGN:
            mti_id = found[sn]
            old = conn.execute(
                "SELECT cluster_code FROM mti_terms WHERE id=?",
                (mti_id,),
            ).fetchone()["cluster_code"]
            conn.execute(
                "UPDATE mti_terms SET cluster_code=? WHERE id=?",
                (new_cluster, mti_id),
            )
            b_results.append((sn, mti_id, old, new_cluster))

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n✗ ERROR — rolled back: {e}")
        raise

    # ---- Reporting -----------------------------------------------------
    print("Operation A — sub-group seeding:")
    for code, label, _, _ in SUBGROUPS:
        print(f"  {code:9s} id={sg_id_by_code[code]:4d}  {label}")
    print()

    print("Operation A — term assignments (34):")
    for sn, code, sg_id, rc in a_results:
        print(f"  {sn:8s} -> {code:9s} (sg_id={sg_id}, rows={rc})")
    print()

    print("Operation B — cluster reassignment (2):")
    for sn, mti_id, old, new in b_results:
        print(f"  {sn:8s} mti={mti_id}  {old} -> {new}")
    print()

    # ---- Verification 1: sub-group counts ------------------------------
    print("Verification 1 — sub-group counts (mti_terms with subgroup):")
    rows = conn.execute(
        "SELECT cs.subgroup_code, cs.label, COUNT(mt.id) AS n "
        "  FROM cluster_subgroup cs "
        "  LEFT JOIN mti_terms mt "
        "    ON mt.cluster_subgroup_id = cs.id "
        "   AND COALESCE(mt.delete_flagged,0)=0 "
        " WHERE cs.cluster_code='M06' "
        " GROUP BY cs.id ORDER BY cs.sort_order"
    ).fetchall()
    total = 0
    all_ok = True
    for r in rows:
        expected = EXPECTED_COUNTS.get(r["subgroup_code"], 0)
        ok = (r["n"] == expected)
        all_ok &= ok
        total += r["n"]
        print(f"  {r['subgroup_code']:9s} "
              f"{r['label']:24s} count={r['n']:3d} "
              f"expected={expected:3d}  {'OK' if ok else 'MISMATCH'}")
    print(f"  {'TOTAL':9s} {'':24s} count={total:3d} expected= 34  "
          f"{'OK' if total == 34 else 'MISMATCH'}")
    print()

    # ---- Verification 2: M06 cluster_code now 34 -----------------------
    n_m06 = conn.execute(
        "SELECT COUNT(*) AS n FROM mti_terms "
        " WHERE cluster_code='M06' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()["n"]
    n_m28 = conn.execute(
        "SELECT COUNT(*) AS n FROM mti_terms "
        " WHERE cluster_code='M28' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()["n"]
    print(f"Verification 2 — cluster_code totals:")
    print(f"  M06: {n_m06} (expected 34)  {'OK' if n_m06==34 else 'CHECK'}")
    print(f"  M28: {n_m28} (was 35; expected 37)  "
          f"{'OK' if n_m28==37 else 'CHECK'}")
    print()

    # ---- Verification 3: H6887E + H7520 reassigned --------------------
    print("Verification 3 — Operation B targets:")
    for sn in ("H6887E", "H7520"):
        r = conn.execute(
            "SELECT cluster_code, cluster_subgroup_id FROM mti_terms "
            " WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",
            (sn,),
        ).fetchone()
        print(f"  {sn:8s} cluster_code={r['cluster_code']}  "
              f"cluster_subgroup_id={r['cluster_subgroup_id']}")
    print()

    # ---- Verification 4: untouched-table row counts unchanged ---------
    print("Verification 4 — untouched-table row counts:")
    for tbl, before in pre_counts.items():
        after = conn.execute(
            f"SELECT COUNT(*) AS n FROM {tbl}"
        ).fetchone()["n"]
        ok = (before == after)
        print(f"  {tbl:25s} before={before:7d}  after={after:7d}  "
              f"{'OK' if ok else 'CHANGED'}")

    conn.close()
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
