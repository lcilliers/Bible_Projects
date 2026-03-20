"""
Apply phase2-flag-reassessment-20260319-v1.json

Pre-step — INSERT 19 new flag codes into wa_quality_flag_types (TERM_ANALYSIS group)
            HIGH_FREQUENCY_ANCHOR goes to DATA_COVERAGE; all others TERM_ANALYSIS

Phase 1   — DELETE 141 rows from wa_data_quality_flags
             match: file_id (via term_inv_id) + term_id (strongs_number) + flag_id (by code)

Phase 2   — INSERT 2361 rows into wa_data_quality_flags
             file_id resolved from wa_term_inventory, term_id = strongs_number,
             flag_id resolved by flag_code from wa_quality_flag_types
"""

import sqlite3
import json
import os
from datetime import datetime, timezone

DB_PATH    = os.path.join("data", "bible_research.db")
PATCH_PATH = os.path.join("data", "imports", "WA", "Patches",
                          "phase2-flag-reassessment-20260319-v1.json")

# New flag codes and their groups
NEW_FLAGS = [
    ("ARAMAIC_FORM",                    "TERM_ANALYSIS"),
    ("BODY_INNER_EXPRESSION",           "TERM_ANALYSIS"),
    ("CAUSATIVE_OF_INNER_STATE",        "TERM_ANALYSIS"),
    ("CROSS_TESTAMENT_SHIFT",           "TERM_ANALYSIS"),
    ("DIVINE_HUMAN_PARALLEL",           "TERM_ANALYSIS"),
    ("ESCHATOLOGICAL_USAGE",            "TERM_ANALYSIS"),
    ("GENERATION_RESOLUTION_PAIR",      "TERM_ANALYSIS"),
    ("GOD_AS_SUBJECT",                  "TERM_ANALYSIS"),
    ("HIGH_FREQUENCY_ANCHOR",           "DATA_COVERAGE"),
    ("METAPHOR_ROOT",                   "TERM_ANALYSIS"),
    ("MULTI_REGISTRY_ANCHOR",           "TERM_ANALYSIS"),
    ("NT_FACULTY_NAMING",               "TERM_ANALYSIS"),
    ("RELATIONAL_DIRECTION",            "TERM_ANALYSIS"),
    ("SEMANTIC_RANGE_BREADTH",          "TERM_ANALYSIS"),
    ("SOMATIC_EXPRESSION",              "TERM_ANALYSIS"),
    ("SOMATIC_INNER_LINK",              "TERM_ANALYSIS"),
    ("THEOLOGICAL_ANCHOR",              "TERM_ANALYSIS"),
    ("VOLITIONAL_COMPONENT",            "TERM_ANALYSIS"),
    ("WISDOM_LITERATURE_CONCENTRATION", "TERM_ANALYSIS"),
]

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    with open(PATCH_PATH, encoding="utf-8") as f:
        patch = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # ── build lookups ───────────────────────────────────────────────────────
    cur.execute("SELECT flag_code, id FROM wa_quality_flag_types")
    flag_lookup = {r["flag_code"]: r["id"] for r in cur.fetchall()}

    cur.execute("SELECT id, file_id, strongs_number FROM wa_term_inventory")
    term_rows = cur.fetchall()
    term_to_file  = {r["id"]: r["file_id"]       for r in term_rows}   # term_inv_id → file_id
    term_to_strongs = {r["id"]: r["strongs_number"] for r in term_rows} # term_inv_id → strongs

    # ══════════════════════════════════════════════════════════════════════
    # Pre-step — add new flag types
    # ══════════════════════════════════════════════════════════════════════
    pre_added   = 0
    pre_skipped = 0
    for code, group in NEW_FLAGS:
        if code in flag_lookup:
            pre_skipped += 1
            continue
        cur.execute(
            "INSERT INTO wa_quality_flag_types (flag_group, flag_code) VALUES (?, ?)",
            (group, code)
        )
        flag_lookup[code] = cur.lastrowid
        pre_added += 1

    print("Pre-step — wa_quality_flag_types:")
    print("  Added  : " + str(pre_added))
    print("  Already existed: " + str(pre_skipped))

    # ══════════════════════════════════════════════════════════════════════
    # Phase 1 — Delete
    # ══════════════════════════════════════════════════════════════════════
    p1_deleted  = 0
    p1_notfound = 0
    p1_noterm   = 0
    for row in patch["deletes"]:
        tid = row["term_inv_id"]
        flag_id = flag_lookup.get(row["flag_code"])
        if flag_id is None:
            p1_notfound += 1
            continue
        file_id = term_to_file.get(tid)
        strongs = term_to_strongs.get(tid)
        if file_id is None:
            p1_noterm += 1
            continue
        cur.execute("""
            DELETE FROM wa_data_quality_flags
            WHERE file_id = ? AND term_id = ? AND flag_id = ?
        """, (file_id, strongs, flag_id))
        p1_deleted += cur.rowcount

    print("\nPhase 1 — deletes:")
    print("  Deleted  : " + str(p1_deleted))
    print("  Not found (flag): " + str(p1_notfound))
    print("  Not found (term): " + str(p1_noterm))
    print("  (rows already absent are expected — flags were reset to DATA_COVERAGE only)")

    # ══════════════════════════════════════════════════════════════════════
    # Phase 2 — Insert
    # ══════════════════════════════════════════════════════════════════════
    p2_inserted  = 0
    p2_skipped   = 0
    p2_duplicate = 0
    p2_errors    = []

    for row in patch["inserts"]:
        tid = row["term_inv_id"]
        flag_id = flag_lookup.get(row["flag_code"])
        if flag_id is None:
            p2_skipped += 1
            p2_errors.append("  Unknown flag_code: " + str(row["flag_code"]))
            continue
        file_id = term_to_file.get(tid)
        strongs = term_to_strongs.get(tid)
        if file_id is None:
            p2_skipped += 1
            p2_errors.append("  term_inv_id not found: " + str(tid))
            continue
        # Guard against duplicates
        cur.execute("""
            SELECT 1 FROM wa_data_quality_flags
            WHERE file_id = ? AND term_id = ? AND flag_id = ?
        """, (file_id, strongs, flag_id))
        if cur.fetchone():
            p2_duplicate += 1
            continue
        cur.execute("""
            INSERT INTO wa_data_quality_flags (file_id, term_id, flag_id, last_changed)
            VALUES (?, ?, ?, ?)
        """, (file_id, strongs, flag_id, NOW))
        p2_inserted += 1

    print("\nPhase 2 — inserts:")
    print("  Inserted   : " + str(p2_inserted))
    print("  Duplicates skipped: " + str(p2_duplicate))
    print("  Errors/skipped: " + str(p2_skipped))
    if p2_errors:
        for e in p2_errors[:10]:
            print(e)
        if len(p2_errors) > 10:
            print("  ... and " + str(len(p2_errors) - 10) + " more")

    # ══════════════════════════════════════════════════════════════════════
    # Verification
    # ══════════════════════════════════════════════════════════════════════
    cur.execute("SELECT COUNT(*) FROM wa_data_quality_flags")
    total = cur.fetchone()[0]
    cur.execute("""
        SELECT qt.flag_group, COUNT(*) AS n
        FROM wa_data_quality_flags dq
        JOIN wa_quality_flag_types qt ON qt.id = dq.flag_id
        GROUP BY qt.flag_group
        ORDER BY n DESC
    """)
    groups = cur.fetchall()
    cur.execute("""
        SELECT qt.flag_code, COUNT(*) AS n
        FROM wa_data_quality_flags dq
        JOIN wa_quality_flag_types qt ON qt.id = dq.flag_id
        WHERE qt.flag_group = 'TERM_ANALYSIS'
        GROUP BY qt.flag_code
        ORDER BY n DESC
        LIMIT 25
    """)
    ta_dist = cur.fetchall()
    cur.execute("""
        SELECT COUNT(*) FROM wa_data_quality_flags
        WHERE flag_id NOT IN (SELECT id FROM wa_quality_flag_types)
    """)
    orphans = cur.fetchone()[0]

    print("\n── Verification ──")
    print("  Total wa_data_quality_flags: " + str(total))
    print("  By group:")
    for g in groups:
        print("    " + str(g[0]).ljust(25) + str(g[1]))
    print("  TERM_ANALYSIS flag distribution:")
    for r in ta_dist:
        print("    " + str(r[0]).ljust(35) + str(r[1]))
    print("  Orphaned flag rows: " + str(orphans))

    conn.commit()
    print("\nPatch applied and committed.")


if __name__ == "__main__":
    main()
