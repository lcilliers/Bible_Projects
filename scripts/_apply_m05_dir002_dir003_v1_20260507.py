"""_apply_m05_dir002_dir003_v1_20260507.py — DB-modifying.

Applies two M05 cluster-process directives in sequence:

  DIR-20260507-M05-002 (sub-group assignment):
    - Create / upsert 8 cluster_subgroup rows (M05-A..M05-G + M05-BOUNDARY)
    - Assign mti_terms.cluster_subgroup_id for all 87 M05 terms
    - Transition cluster.status from 'Data - In Progress' to
      'Analysis - In Progress'

  DIR-20260507-M05-003 (term rebind):
    - Remove H4263 mach.mal (mti_id=1264) from M05 cluster
      (cluster_code=NULL, cluster_subgroup_id=NULL)
    - Verse_context rows preserved
    - Reduces M05-BOUNDARY from 13 → 12, M05 total from 87 → 86

Application order is fixed (dir-002 must apply before dir-003).
Idempotent: re-running detects existing rows and re-applies safely.
Backed up first.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

DIR002_ID = "DIR-20260507-M05-002"
DIR003_ID = "DIR-20260507-M05-003"
SOURCE_FILE_002 = (
    "Sessions/Session_Clusters/M05/files phase 4/"
    "wa-cluster-M05-dir-002-subgroup-assign-v1-20260507.md"
)
SOURCE_FILE_003 = (
    "Sessions/Session_Clusters/M05/files phase 4/"
    "wa-cluster-M05-dir-003-term-rebind-v1-20260507.md"
)

# ---- Sub-group definitions (Operation A of dir-002) -----------------------
SUBGROUPS = [
    ("M05-A",        "Love",                        1),
    ("M05-B",        "Compassion",                  2),
    ("M05-C",        "Mercy",                       3),
    ("M05-D",        "Kindness and Goodness",       4),
    ("M05-E",        "Gentleness",                  5),
    ("M05-F",        "Comfort and Encouragement",   6),
    ("M05-G",        "Fellowship and Participation", 7),
    ("M05-BOUNDARY", "Boundary",                    8),
]
# Long descriptions for each sub-group (verbatim from dir-002)
SUBGROUP_DESCRIPTIONS = {
    "M05-A": (
        "Terms naming the inner orientation of directed attachment toward "
        "an object — person, God, community, or stranger. Spans covenantal "
        "steadfast love (che.sed, a.ha.vah), self-giving love (agapē, "
        "agapaō), natural affection and friendship (fileō, a.hev, filia, "
        "filos, re.eh), and the philo- compound family naming specific "
        "relational directions of the same orientation. Includes "
        "person-types constituted by love (cha.sid, a.hav) and the "
        "beloved-designation (ye.di.dut) as the relational object at "
        "love's most intimate register."
    ),
    "M05-B": (
        "Terms naming the inward movement triggered by encountering "
        "suffering or need — visceral, directional toward the sufferer. "
        "Core families: the Hebrew RACHAM root (ra.cha.mim, ra.cha.min, "
        "ra.cham, ra.chum, ra.cha.ma.ni) naming womb-rooted compassion; "
        "the Greek splanchn- root (splanchnizō, eusplanchnos) naming "
        "bowel-rooted compassion; the sym-pathos group (sumpathēs, "
        "sumpatheō) naming fellow-feeling; and the sparing/pity register "
        "(chus, cha.mal, chem.lah). Also includes the Greek oiktir- "
        "family (oiktirmos, oiktirmōn, oikteirō) of compassionate mercy."
    ),
    "M05-C": (
        "Terms naming the compassionate disposition of the greater "
        "toward the lesser — covenantally and judicially framed. The "
        "eleos/eleeō family: God's mercy as defining inner attribute "
        "(eleos), the act of mercy (eleeō), mercifulness as character "
        "quality (eleēmōn), and the structural opposites (aneleēmōn, "
        "anileōs — merciless). Includes eleeinos (pitiable) as the "
        "condition-term that defines the mercy characteristic's scope "
        "and calls it forth."
    ),
    "M05-D": (
        "Terms naming the inner quality of gracious generous goodwill — "
        "expressed as goodness toward others and as God's character "
        "that leads to repentance. The chrēstos/chrēstotēs/chrēsteuomai "
        "family (kindness as Spirit-produced inner quality) and the "
        "agathos compound family (goodness as inner moral orientation, "
        "activity, and person-type). Also includes haplotēs "
        "(singleness/generosity as undivided inner orientation) and "
        "pronoeō (purposive care as inner intention)."
    ),
    "M05-E": (
        "Terms naming the inner disposition of yielding, non-coercive, "
        "non-retaliatory strength — operating in conflict, correction, "
        "and community as the mark of the renewed person. The "
        "praus/praotēs/prautēs family (Greek meekness/gentleness), the "
        "Hebrew an.vah/a.na.vah family (humility/gentleness), and "
        "epieikeia/epieikēs (gracious reasonable fairness). Also "
        "includes anochē (divine tolerance/forbearance — restrained "
        "from exacting what is deserved) and anexikakos (patient "
        "endurance of evil without resentment)."
    ),
    "M05-F": (
        "Terms naming the inner orientation directed specifically toward "
        "the distressed or faltering — bringing consolation, "
        "strengthening, calling alongside. Hebrew na.cham (to "
        "comfort/console, including divine relenting) and tan.chum "
        "(consolation as God's gift); Greek parakaleō (to comfort, "
        "exhort, plead) and paraklēsis (encouragement/comfort as inner "
        "experience); and la.vav (to captivate/encourage the heart)."
    ),
    "M05-G": (
        "Terms naming the inner-relational bond of shared life — mutual "
        "belonging, common participation, generous sharing as expression "
        "of the participation bond. The koinōnia/koinōnos family "
        "(fellowship and the participant), katallagē (reconciliation "
        "as inner-relational restoration), homofrōn and isopsuchos "
        "(communal unity of inner orientation as the fellowship "
        "characteristic in its harmony expression), and epoikodomeō "
        "(building up the community as the participation characteristic "
        "in its formative expression)."
    ),
    "M05-BOUNDARY": (
        "Terms that qualify, contextualise, or express the cluster's "
        "characteristics without themselves being inner-being "
        "characteristics. Includes: assembly occasions (ekklēsia, "
        "miq.ra, a.tsa.rah); physical expressions of love (filēma/kiss, "
        "katafileō/to kiss, cheq/bosom); expressive and demonstrative "
        "acts (endeiknumi, eirēnopoieō, dōreō); freedom from disordered "
        "love (afilarguros); the lovely/fitting quality of objects that "
        "direct inner attention (na.eh, prosfilēs); and H4263 mach.mal "
        "(held in BOUNDARY pending cluster reassignment — see dir-003)."
    ),
}

# ---- Term → subgroup_code mapping (Operation B of dir-002) ----------------
# Source: dir-002 §SCOPE Operation B tables, in order.
ASSIGNMENTS = [
    # M05-A — Love (23)
    ("H2617A", "M05-A"), ("G0025", "M05-A"), ("G0026", "M05-A"),
    ("H0160",  "M05-A"), ("H0158", "M05-A"), ("G5368", "M05-A"),
    ("H0157H", "M05-A"), ("G5360", "M05-A"), ("G5387", "M05-A"),
    ("G5362",  "M05-A"), ("G5388", "M05-A"), ("G5363", "M05-A"),
    ("G5381",  "M05-A"), ("G5382", "M05-A"), ("G5391", "M05-A"),
    ("G5358",  "M05-A"), ("G5361", "M05-A"), ("G5373", "M05-A"),
    ("H2623",  "M05-A"), ("H2616A","M05-A"), ("G5384", "M05-A"),
    ("H7463",  "M05-A"), ("H3033", "M05-A"),
    # M05-B — Compassion (15)
    ("H7356B", "M05-B"), ("H7359", "M05-B"), ("H7355", "M05-B"),
    ("H7349",  "M05-B"), ("H7362", "M05-B"), ("G3628", "M05-B"),
    ("G3629",  "M05-B"), ("G3627", "M05-B"), ("G4697", "M05-B"),
    ("G2155",  "M05-B"), ("G4835", "M05-B"), ("G4834", "M05-B"),
    ("H2347",  "M05-B"), ("H2550", "M05-B"), ("H2551", "M05-B"),
    # M05-C — Mercy (6)
    ("G1656", "M05-C"), ("G1653", "M05-C"), ("G1655", "M05-C"),
    ("G0415", "M05-C"), ("G0448", "M05-C"), ("G1652", "M05-C"),
    # M05-D — Kindness and Goodness (10)
    ("G5544", "M05-D"), ("G5543", "M05-D"), ("G5541", "M05-D"),
    ("G0018", "M05-D"), ("G0015", "M05-D"), ("G0014", "M05-D"),
    ("G0016", "M05-D"), ("G0017", "M05-D"), ("G0572", "M05-D"),
    ("G4306", "M05-D"),
    # M05-E — Gentleness (9)
    ("G4239", "M05-E"), ("G4236", "M05-E"), ("G4240", "M05-E"),
    ("H6038", "M05-E"), ("H6037", "M05-E"), ("G1932", "M05-E"),
    ("G1933", "M05-E"), ("G0463", "M05-E"), ("G0420", "M05-E"),
    # M05-F — Comfort and Encouragement (5)
    ("H5162G", "M05-F"), ("G3870", "M05-F"), ("G3874", "M05-F"),
    ("H3823A", "M05-F"), ("H8575", "M05-F"),
    # M05-G — Fellowship and Participation (6)
    ("G2842", "M05-G"), ("G2844", "M05-G"), ("G2643", "M05-G"),
    ("G3675", "M05-G"), ("G2473", "M05-G"), ("G2026", "M05-G"),
    # M05-BOUNDARY — Boundary (13)
    ("G1577", "M05-BOUNDARY"), ("H4744", "M05-BOUNDARY"),
    ("H6116", "M05-BOUNDARY"), ("G5370", "M05-BOUNDARY"),
    ("G2705", "M05-BOUNDARY"), ("H2436G","M05-BOUNDARY"),
    ("H5000", "M05-BOUNDARY"), ("G4375", "M05-BOUNDARY"),
    ("G0866", "M05-BOUNDARY"), ("G1433", "M05-BOUNDARY"),
    ("G1731", "M05-BOUNDARY"), ("G1517", "M05-BOUNDARY"),
    ("H4263", "M05-BOUNDARY"),  # Provisional — removed by dir-003
]

EXPECTED_COUNTS_AFTER_DIR002 = {
    "M05-A": 23, "M05-B": 15, "M05-C": 6, "M05-D": 10,
    "M05-E": 9,  "M05-F": 5,  "M05-G": 6, "M05-BOUNDARY": 13,
}
EXPECTED_COUNTS_AFTER_DIR003 = dict(EXPECTED_COUNTS_AFTER_DIR002)
EXPECTED_COUNTS_AFTER_DIR003["M05-BOUNDARY"] = 12  # mach.mal removed

REBIND_TARGET = ("H4263", 1264)  # (Strong's, mti_id) — dir-003


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_DIR,
                        f"bible_research_{ts}_pre_m05_dir002_003.db")
    shutil.copy2(DB_PATH, dest)
    return dest


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ---- Pre-flight: every Strong's in ASSIGNMENTS must exist in M05
    all_strongs = [s for s, _ in ASSIGNMENTS]
    placeholders = ",".join("?" * len(all_strongs))
    found = {
        r["strongs_number"]: r["id"]
        for r in conn.execute(
            f"SELECT id, strongs_number FROM mti_terms "
            f" WHERE strongs_number IN ({placeholders}) "
            f"   AND cluster_code='M05' "
            f"   AND COALESCE(delete_flagged,0)=0",
            all_strongs,
        )
    }
    missing = [s for s in all_strongs if s not in found]
    if missing:
        print(f"[err] Missing M05 Strong's: {missing}")
        return 2
    print(f"Pre-flight OK — all {len(all_strongs)} Strong's resolve in M05.")
    print()

    # Counts of unassigned terms before
    n_unassigned_before = conn.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M05' AND cluster_subgroup_id IS NULL "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    n_total_m05_before = conn.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"Pre-state: M05 has {n_total_m05_before} terms, "
          f"{n_unassigned_before} with cluster_subgroup_id=NULL")

    actions = []
    sg_id_by_code = {}

    try:
        conn.execute("BEGIN")

        # =========================================================
        # DIR-20260507-M05-002 — Operation A: cluster_subgroup rows
        # =========================================================
        for code, label, sort_order in SUBGROUPS:
            descr = SUBGROUP_DESCRIPTIONS[code]
            existing = conn.execute(
                "SELECT id FROM cluster_subgroup "
                " WHERE cluster_code='M05' AND subgroup_code=?",
                (code,),
            ).fetchone()
            if existing:
                conn.execute(
                    "UPDATE cluster_subgroup "
                    "   SET label=?, sort_order=?, "
                    "       core_description=?, status=?, version=?, "
                    "       source=?, last_updated_date=? "
                    " WHERE id=?",
                    (label, sort_order, descr, "Data - In Progress",
                     "v1", DIR002_ID, now_iso(), existing["id"]),
                )
                sg_id_by_code[code] = existing["id"]
                actions.append(f"UPDATE cluster_subgroup {code} "
                               f"(id={existing['id']})")
            else:
                cur = conn.execute(
                    "INSERT INTO cluster_subgroup "
                    "  (cluster_code, subgroup_code, label, "
                    "   core_description, sort_order, status, version, "
                    "   source, delete_flagged, created_at, "
                    "   last_updated_date) "
                    "VALUES ('M05', ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)",
                    (code, label, descr, sort_order,
                     "Data - In Progress", "v1", DIR002_ID,
                     now_iso(), now_iso()),
                )
                sg_id_by_code[code] = cur.lastrowid
                actions.append(f"INSERT cluster_subgroup {code} "
                               f"(new id={cur.lastrowid})")

        # =========================================================
        # DIR-20260507-M05-002 — Operation B: assign cluster_subgroup_id
        # =========================================================
        n_assigned = 0
        for sn, code in ASSIGNMENTS:
            mti_id = found[sn]
            sg_id = sg_id_by_code[code]
            cur = conn.execute(
                "UPDATE mti_terms SET cluster_subgroup_id=? "
                " WHERE id=?",
                (sg_id, mti_id),
            )
            if cur.rowcount:
                n_assigned += 1
        actions.append(f"UPDATE mti_terms SET cluster_subgroup_id "
                       f"for {n_assigned} terms")

        # =========================================================
        # DIR-20260507-M05-002 — Operation C: cluster status
        # =========================================================
        cur = conn.execute(
            "UPDATE cluster SET status='Analysis - In Progress', "
            "       last_updated_date=? "
            " WHERE cluster_code='M05'",
            (now_iso(),),
        )
        actions.append(f"UPDATE cluster.status M05 → "
                       f"'Analysis - In Progress' (rows={cur.rowcount})")

        # =========================================================
        # DIR-20260507-M05-003 — Term rebind: H4263 mach.mal
        # =========================================================
        sn003, mti003 = REBIND_TARGET
        # Verify pre-state
        pre = conn.execute(
            "SELECT cluster_code, cluster_subgroup_id FROM mti_terms "
            " WHERE id=? AND strongs_number=?",
            (mti003, sn003),
        ).fetchone()
        if not pre:
            raise RuntimeError(
                f"DIR-003 target {sn003} (mti={mti003}) not found"
            )
        if pre["cluster_code"] != "M05":
            raise RuntimeError(
                f"DIR-003 target {sn003} not in M05 "
                f"(actual cluster_code={pre['cluster_code']})"
            )
        cur = conn.execute(
            "UPDATE mti_terms "
            "   SET cluster_code=NULL, cluster_subgroup_id=NULL "
            " WHERE id=? AND strongs_number=? AND cluster_code='M05'",
            (mti003, sn003),
        )
        actions.append(
            f"UPDATE mti_terms id={mti003} ({sn003}) "
            f"cluster_code → NULL (DIR-003 / rows={cur.rowcount})"
        )

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print("Actions:")
    for a in actions:
        print(f"  - {a}")
    print()

    # =============================================================
    # Completion confirmation queries (per dir-002 + dir-003)
    # =============================================================
    print("=" * 70)
    print("COMPLETION CONFIRMATION")
    print("=" * 70)

    # Q1: per-subgroup term counts (post dir-003 — i.e. final state)
    print()
    print("Query 1 — sub-group term counts (final, post dir-003):")
    print(f"{'subgroup_code':14s} {'expected':>9s} {'actual':>7s} {'status'}")
    total_actual = 0
    for code, _, _ in SUBGROUPS:
        n = conn.execute(
            "SELECT COUNT(*) FROM mti_terms mt "
            "  JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id "
            " WHERE cs.subgroup_code=? AND cs.cluster_code='M05' "
            "   AND mt.cluster_code='M05' "
            "   AND COALESCE(mt.delete_flagged,0)=0",
            (code,),
        ).fetchone()[0]
        expected = EXPECTED_COUNTS_AFTER_DIR003[code]
        ok = "OK" if n == expected else "MISMATCH"
        print(f"  {code:14s} {expected:>7d}   {n:>5d}   {ok}")
        total_actual += n
    expected_total = sum(EXPECTED_COUNTS_AFTER_DIR003.values())
    ok = "OK" if total_actual == expected_total else "MISMATCH"
    print(f"  {'TOTAL':14s} {expected_total:>7d}   {total_actual:>5d}   {ok}")

    # Q2: zero unassigned M05 terms
    n_unassigned = conn.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M05' AND cluster_subgroup_id IS NULL "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print()
    print(f"Query 2 — M05 terms with cluster_subgroup_id=NULL: "
          f"{n_unassigned} (expected 0)  "
          f"{'OK' if n_unassigned == 0 else 'MISMATCH'}")

    # Q3: cluster status
    r = conn.execute(
        "SELECT cluster_code, status FROM cluster "
        " WHERE cluster_code='M05'"
    ).fetchone()
    print()
    print(f"Query 3 — cluster status: M05 = '{r['status']}' "
          f"{'OK' if r['status'] == 'Analysis - In Progress' else 'MISMATCH'}")

    # Q4: sample rows
    print()
    print("Query 4 — sample term assignments:")
    for r in conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, cs.subgroup_code
          FROM mti_terms mt
          JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id
         WHERE mt.cluster_code='M05'
           AND mt.strongs_number IN
             ('G0026','H7356B','G1656','G5544','G4236',
              'H5162G','G2842','G1577')
         ORDER BY cs.subgroup_code
    """):
        print(f"  {r['strongs_number']:8s} → {r['subgroup_code']}")

    # DIR-003 verification
    print()
    print("Query DIR-003 — mach.mal (H4263, mti=1264) post-state:")
    r = conn.execute(
        "SELECT id, strongs_number, transliteration, "
        "       cluster_code, cluster_subgroup_id "
        "  FROM mti_terms WHERE id=1264"
    ).fetchone()
    print(f"  cluster_code: {r['cluster_code']}  "
          f"cluster_subgroup_id: {r['cluster_subgroup_id']}  "
          f"{'OK' if r['cluster_code'] is None else 'MISMATCH'}")

    n_vc = conn.execute(
        "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=1264 "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  verse_context rows for mti=1264 (preserved): {n_vc}")

    n_total_m05_after = conn.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print()
    print(f"M05 cluster total: {n_total_m05_after} "
          f"(expected 86 after dir-003)  "
          f"{'OK' if n_total_m05_after == 86 else 'MISMATCH'}")

    # Q5: wa_session_b_findings unchanged (no rows raised today)
    n_sb = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
         WHERE COALESCE(raised_date,'') LIKE '2026-05-07%'
            OR COALESCE(raised_date,'') LIKE '20260507%'
    """).fetchone()[0]
    print()
    print(f"Query 5 — wa_session_b_findings rows raised 2026-05-07: "
          f"{n_sb}  {'OK' if n_sb == 0 else 'CHECK'}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
