"""_apply_m15_dir001_dir002_v1_20260508.py — DB-modifying.

Applies M15 Phase 4 directives in sequence:

  DIR-20260508-001 — Sub-group assignment (8 sub-groups + 90 term assignments)
  DIR-20260508-002 — Reassignment of 5 terms out of M15 to FLAG cluster

Researcher decisions captured 2026-05-08:
  - frēn (G5424, mti=2493) — missing from DIR-001 — assigned to M15-G
  - 5 reassignment terms — all move to FLAG (cluster_code='FLAG')

Notes on the directive vs DB:
  - DIR-001 declared 89 term assignments; DB has 90 active M15 terms.
    The missing one (frēn / G5424 / mti=2493) is added here under
    M15-G per researcher confirmation.
  - DIR-001 has 3 Strong's-label typos (mti=3392 G3392→G1760, mti=3372
    G3372→G1771, mti=3375 G3375→G1963). The mti_id is the canonical
    reference and is correct in all 3 cases; the labels are doc-only
    and do not affect this apply.

Single transaction with PRAGMA foreign_keys = ON.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

CLUSTER_CODE = "M15"
DIRECTIVE_DIR001 = "DIR-20260508-001"
DIRECTIVE_DIR002 = "DIR-20260508-002"

SUBGROUPS = [
    ("M15-A", "Wisdom as holistic inner character and orientation",
     "Terms that name wisdom as a constituted holistic quality of the "
     "inner person — a settled orientation of the whole person that "
     "shapes perception, decision, and character. Includes the "
     "structural opposite (unwise). Spirit-given, covenantally "
     "oriented, morally constitutive."),
    ("M15-B", "Understanding as inner perceptive faculty",
     "Terms that name the inner faculty of understanding — the "
     "capacity to receive, perceive, and grasp what is being revealed "
     "or communicated. Morally conditioned: the faculty is enabled by "
     "humility before God and blocked by heart-dullness. Includes the "
     "structural opposite (senseless)."),
    ("M15-C", "Knowledge as inner content and covenantal knowing",
     "Terms that name knowledge as both inner content held in the "
     "knowing self and the constitutive relational orientation of "
     "knowing God. Includes the covenantal knowing of God and its "
     "structural opposite (spiritual ignorance/agnoeō)."),
    ("M15-D", "Discernment and practical judgment",
     "Terms that name the applied perceptive act — judging situations "
     "wisely, making right moral-practical distinctions, and the "
     "conscience-adjacent evaluation of thoughts. Includes "
     "directionally neutral terms (same inner quality serves "
     "righteousness or cunning depending on object)."),
    ("M15-E", "Deliberative planning, counsel, and purposive intent",
     "Terms that name the inner capacity of purposive forward-"
     "orientation — forming intent, devising plans, giving and "
     "receiving counsel, making deliberate decisions. Includes divine "
     "and human purposive activity."),
    ("M15-F", "Meditative and reflective inner activity",
     "Terms that name the inner turning of the mind on received "
     "material — musing, pondering, the inner dialogue of self-"
     "reasoning, and the contemplative considering of a person before "
     "God. Activity-oriented (distinct from static thought-content)."),
    ("M15-G", "Inner thought-content — the mind's formed thoughts",
     "Terms that name the formed thoughts held within the mind — "
     "inner content as objects held, which can be guarded, captured, "
     "led astray, or disclosed. Static (distinct from reflective "
     "activity)."),
    ("BOUNDARY",
     "Functional, supporting, and cluster-reassignment candidates",
     "Terms that carry inner-being relevance in their confirmed verses "
     "but do not carry an inner characteristic as their primary "
     "semantic load: functional roles (translation, arbitration, "
     "teaching), formative activities (training), speech acts "
     "(insisting), comparators (resembling), or terms flagged for "
     "cluster reassignment (see DIR-20260508-002)."),
]

# (mti_id, target_subgroup_code) — 90 terms total
# 89 from DIR-001 + frēn (mti=2493) → M15-G per researcher
ASSIGNMENTS = [
    # M15-A (12 declared + frēn-not-here = 12)
    (532, "M15-A"), (4458, "M15-A"), (530, "M15-A"), (6676, "M15-A"),
    (6696, "M15-A"), (528, "M15-A"), (6668, "M15-A"), (527, "M15-A"),
    (996, "M15-A"), (3459, "M15-A"), (1174, "M15-A"), (525, "M15-A"),
    # M15-B (10)
    (932, "M15-B"), (523, "M15-B"), (1204, "M15-B"), (816, "M15-B"),
    (1205, "M15-B"), (524, "M15-B"), (531, "M15-B"), (1207, "M15-B"),
    (1201, "M15-B"), (1202, "M15-B"),
    # M15-C (7)
    (958, "M15-C"), (955, "M15-C"), (961, "M15-C"), (959, "M15-C"),
    (962, "M15-C"), (963, "M15-C"), (1838, "M15-C"),
    # M15-D (9)
    (519, "M15-D"), (4487, "M15-D"), (4486, "M15-D"), (1285, "M15-D"),
    (818, "M15-D"), (3409, "M15-D"), (5099, "M15-D"), (3336, "M15-D"),
    (3335, "M15-D"),
    # M15-E (13)
    (749, "M15-E"), (2109, "M15-E"), (509, "M15-E"), (847, "M15-E"),
    (754, "M15-E"), (3482, "M15-E"), (3445, "M15-E"), (3578, "M15-E"),
    (3280, "M15-E"), (3373, "M15-E"), (1179, "M15-E"), (1001, "M15-E"),
    (3334, "M15-E"),
    # M15-F (11)
    (242, "M15-F"), (975, "M15-F"), (1181, "M15-F"), (896, "M15-F"),
    (977, "M15-F"), (5883, "M15-F"), (1184, "M15-F"), (1081, "M15-F"),
    (3392, "M15-F"), (917, "M15-F"), (5662, "M15-F"),
    # M15-G (9 from directive + frēn = 10)
    (1188, "M15-G"), (3372, "M15-G"), (3375, "M15-G"), (3408, "M15-G"),
    (1178, "M15-G"), (3449, "M15-G"), (3453, "M15-G"), (3442, "M15-G"),
    (960, "M15-G"),
    (2493, "M15-G"),  # frēn — researcher decision 2026-05-08
    # BOUNDARY (18)
    (5278, "BOUNDARY"), (973, "BOUNDARY"), (5865, "BOUNDARY"),
    (5864, "BOUNDARY"), (6085, "BOUNDARY"), (6256, "BOUNDARY"),
    (7333, "BOUNDARY"), (7419, "BOUNDARY"), (7085, "BOUNDARY"),
    (1080, "BOUNDARY"), (1171, "BOUNDARY"), (454, "BOUNDARY"),
    (4190, "BOUNDARY"), (999, "BOUNDARY"), (1108, "BOUNDARY"),
    (1396, "BOUNDARY"), (743, "BOUNDARY"), (1846, "BOUNDARY"),
]

# DIR-002: 5 mti_ids to move out of M15 to FLAG
DIR002_MOVES = [
    (743,  "G0841", "autarkeia"),
    (999,  "G4993", "sōfroneō"),
    (4190, "G4994", "sōfronizō"),
    (1108, "G4997", "sōfrosunē"),
    (1396, "G5591", "psuchikos"),
]
DIR002_TARGET_CLUSTER = "FLAG"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    ts = now_iso()

    # ── Pre-flight ────────────────────────────────────────────────────
    print("=" * 65)
    print("PRE-FLIGHT")
    print("=" * 65)

    halts = []

    # 1. Each assignment mti_id exists in M15
    for mti_id, _ in ASSIGNMENTS:
        r = cur.execute(
            "SELECT cluster_code, COALESCE(delete_flagged,0) AS df "
            "  FROM mti_terms WHERE id=?", (mti_id,)
        ).fetchone()
        if r is None:
            halts.append(f"mti={mti_id} not found")
        elif r["cluster_code"] != "M15":
            halts.append(
                f"mti={mti_id} cluster_code={r['cluster_code']!r} (expected M15)"
            )
        elif r["df"] == 1:
            halts.append(f"mti={mti_id} is delete_flagged")

    # 2. Coverage: all 90 active M15 terms covered
    in_db = {r["id"] for r in cur.execute(
        "SELECT id FROM mti_terms "
        " WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0"
    )}
    declared = {a[0] for a in ASSIGNMENTS}
    missing_from_directive = in_db - declared
    extra_in_directive = declared - in_db
    if missing_from_directive:
        halts.append(
            f"M15 terms in DB not in assignment list: "
            f"{sorted(missing_from_directive)}"
        )
    if extra_in_directive:
        halts.append(
            f"Assignment list contains mti_ids not in M15: "
            f"{sorted(extra_in_directive)}"
        )

    # 3. No M15 sub-groups exist yet
    n_sg = cur.execute(
        "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M15'"
    ).fetchone()[0]
    if n_sg != 0:
        halts.append(
            f"cluster_subgroup already has {n_sg} M15 row(s) — "
            "expected 0 pre-DIR-001"
        )

    # 4. FLAG cluster exists for DIR-002
    n_flag = cur.execute(
        "SELECT COUNT(*) FROM cluster WHERE cluster_code='FLAG'"
    ).fetchone()[0]
    if n_flag != 1:
        halts.append(f"FLAG cluster row count {n_flag} (expected 1)")

    if halts:
        print("HALT — pre-flight failed:")
        for h in halts:
            print(f"  {h}")
        return 1

    print(f"OK — {len(ASSIGNMENTS)} assignments, all 90 M15 active terms covered.")

    # ── Execute (single transaction) ─────────────────────────────────
    print()
    print("=" * 65)
    print("EXECUTE")
    print("=" * 65)

    counts = {
        "subgroups_inserted": 0,
        "terms_assigned": 0,
        "terms_moved_to_flag": 0,
    }

    try:
        cur.execute("BEGIN")

        # DIR-001 §A: Insert 8 sub-groups
        sg_id_by_code = {}
        for i, (code, label, desc) in enumerate(SUBGROUPS, start=1):
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, "
                "   sort_order, status, version, source, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'Active', 'v1', ?, 0, ?, ?)",
                (CLUSTER_CODE, code, label, desc, i,
                 DIRECTIVE_DIR001, ts, ts),
            )
            sg_id_by_code[code] = cur.lastrowid
            counts["subgroups_inserted"] += 1
            print(f"  + cluster_subgroup INSERT {code} -> id={cur.lastrowid}")

        # DIR-001 §B: Assign 90 mti_terms
        for mti_id, target_code in ASSIGNMENTS:
            sg_id = sg_id_by_code[target_code]
            rc = cur.execute(
                "UPDATE mti_terms "
                "   SET cluster_subgroup_id=?, last_changed=? "
                " WHERE id=? AND cluster_code='M15' "
                "   AND COALESCE(delete_flagged,0)=0",
                (sg_id, ts, mti_id),
            ).rowcount
            if rc != 1:
                raise RuntimeError(
                    f"mti_terms UPDATE mti={mti_id} expected 1 row, got {rc}"
                )
            counts["terms_assigned"] += 1

        print(f"  ~ mti_terms.cluster_subgroup_id assigned: "
              f"{counts['terms_assigned']} terms")

        # DIR-002: Move 5 terms to FLAG
        for mti_id, strongs, transl in DIR002_MOVES:
            rc = cur.execute(
                "UPDATE mti_terms "
                "   SET cluster_code=?, cluster_subgroup_id=NULL, "
                "       last_changed=? "
                " WHERE id=? AND cluster_code='M15' "
                "   AND COALESCE(delete_flagged,0)=0",
                (DIR002_TARGET_CLUSTER, ts, mti_id),
            ).rowcount
            if rc != 1:
                raise RuntimeError(
                    f"DIR-002 UPDATE mti={mti_id} expected 1 row, got {rc}"
                )
            counts["terms_moved_to_flag"] += 1
            print(f"  ~ mti_terms UPDATE {strongs} (mti={mti_id}) "
                  f"M15/BOUNDARY -> FLAG, sg_id=NULL")

        cur.execute("COMMIT")
        print("\nCOMMIT successful.")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    # ── Verification ──────────────────────────────────────────────
    print()
    print("=" * 65)
    print("POST-WRITE VERIFICATION")
    print("=" * 65)

    print()
    print("Q1 — Sub-group counts (expected: A=12, B=10, C=7, D=9, E=13, "
          "F=11, G=10, BOUNDARY=13 after FLAG move; total=85):")
    for r in cur.execute(
        "SELECT cs.subgroup_code, COUNT(mt.id) AS n "
        "  FROM cluster_subgroup cs "
        "  LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id=cs.id "
        "    AND mt.cluster_code='M15' "
        "    AND COALESCE(mt.delete_flagged,0)=0 "
        " WHERE cs.cluster_code='M15' "
        "   AND COALESCE(cs.delete_flagged,0)=0 "
        " GROUP BY cs.subgroup_code "
        " ORDER BY cs.sort_order"
    ):
        print(f"  {r['subgroup_code']:10s} {r['n']:3d}")

    n_unassigned = cur.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M15' AND cluster_subgroup_id IS NULL "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  Unassigned M15 terms: {n_unassigned} (expected 0)")

    n_m15 = cur.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  Total M15 active terms: {n_m15} (expected 85)")

    print()
    print("Q2 — Reassigned terms now on FLAG:")
    for r in cur.execute(
        "SELECT id, strongs_number, transliteration, cluster_code, "
        "       cluster_subgroup_id "
        "  FROM mti_terms "
        " WHERE id IN (743, 999, 4190, 1108, 1396) "
        " ORDER BY strongs_number"
    ):
        print(f"  mti={r['id']:5d} {r['strongs_number']:8s} "
              f"{r['transliteration']:18s} -> cc={r['cluster_code']!r} "
              f"sg={r['cluster_subgroup_id']}")

    n_flag_total = cur.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  FLAG total: {n_flag_total} (was 121 + 5 = expected 126)")

    print()
    print("Q3 — Sample term assignments (representative):")
    for s in ('H3045', 'G4678', 'H0995', 'H3289', 'H7878', 'G5424'):
        r = cur.execute(
            "SELECT mt.strongs_number, mt.transliteration, "
            "       cs.subgroup_code "
            "  FROM mti_terms mt "
            "  LEFT JOIN cluster_subgroup cs "
            "    ON cs.id=mt.cluster_subgroup_id "
            " WHERE mt.cluster_code='M15' AND mt.strongs_number=? "
            "   AND COALESCE(mt.delete_flagged,0)=0",
            (s,),
        ).fetchone()
        if r:
            print(f"  {r['strongs_number']:8s} {r['transliteration']:18s} "
                  f"-> {r['subgroup_code']}")

    print()
    print("Operations applied:")
    for k, v in counts.items():
        print(f"  {k:30s} {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
