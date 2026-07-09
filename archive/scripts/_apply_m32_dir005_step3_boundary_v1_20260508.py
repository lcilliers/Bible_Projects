"""_apply_m32_dir005_step3_boundary_v1_20260508.py — DB-modifying.

DIR-20260508-004 (dir-005), Step C — BOUNDARY structural rows.

Inserts 3 rows at obs_id=T1.2.1 keyed to cluster_subgroup_id=19
(M32-BOUNDARY) — one per BOUNDARY term:
  - kardiognōstēs (G2589, mti=599)   — divine-attribute term
  - enthumeomai  (G1760, mti=3392)   — reflective-capacity term
  - autokatakritos (G0843, mti=4848) — outcome-terminus term

Per the directive: "BOUNDARY terms received structural characterisation
notes only. Their rows in cluster_finding are keyed to T1.2.1 only,
with cluster_subgroup_id = NULL or equivalent BOUNDARY designation per
schema." We use the M32-BOUNDARY sub-group id (Option A precedent —
schema enforces obs_id NOT NULL; we choose the M32-BOUNDARY sub-group
to keep BOUNDARY rows queryable by sub-group code).

Each row uses a distinct version ('v1-bnd-<strongs>') so the UNIQUE
constraint allows three rows on the same (obs_id, cluster_code,
cluster_subgroup_id) tuple.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M32"
SOURCE_FILE = "WA-M32-consolidated-findings-v1-20260508-part1.md"
QCODE = "T1.2.1"

# (mti_id, strongs, version_suffix, finding_text)
BOUNDARY_ROWS = [
    (599, "G2589", "kardiognostes",
     "**BOUNDARY characterisation — kardiognōstēs (G2589):** "
     "Divine-attribute term. Names God as the one whose epistemic access "
     "to the human inner being is complete and unmediated. Role in "
     "cluster economy: the outer epistemological frame within which both "
     "M32-A and M32-B operate — God's heart-knowledge is the definitive "
     "court above conscience (1Cor 4:4) and above all human inner-knowing. "
     "Evidence: Act 1:24 (invoked as ground for decisive divine "
     "selection); Act 15:8 (invoked as ground for divine reception of "
     "Gentiles). Both instances: God's heart-knowledge settles what "
     "human knowledge cannot."),
    (3392, "G1760", "enthumeomai",
     "**BOUNDARY characterisation — enthumeomai (G1760):** "
     "Reflective-capacity term. Names the act of sustained inner "
     "deliberation — the person turning something over in the mind. "
     "Role in cluster economy: the cognitive deliberation that bridges "
     "initial attending (M32-B) and moral self-assessment (M32-A). "
     "Evidence: Mat 1:20 (Joseph holds situation in inner reflection "
     "before divine direction); Mat 9:4 (scribes' inner reflection "
     "perceived by Christ — establishes inner deliberation as "
     "transparent to divine perception); Act 10:19 (Peter pondering the "
     "vision before divine communication). The Mat 9:4 instance "
     "connects structurally to kardiognōstēs: inner reflection is not "
     "hidden from God."),
    (4848, "G0843", "autokatakritos",
     "**BOUNDARY characterisation — autokatakritos (G0843):** "
     "Outcome-terminus term. Names the terminal state of conscience — "
     "the condition in which the person's own beliefs or conduct become "
     "the instrument of their condemnation. Role in cluster economy: "
     "shows where conscience leads when a person persists in known "
     "wrong — the conscience-faculty turns prosecutor. Negative "
     "complement to 1Cor 4:4: where sunoida gives a clear verdict and "
     "acknowledges God as final judge, autokatakritos shows conscience "
     "having issued a condemning verdict the person cannot escape "
     "because it comes from within. Evidence: Tit 3:11 (\"such a person "
     "is warped and sinful; he is self-condemned\")."),
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    ts = now_iso()

    # Resolve T1.2.1 obs_id and BOUNDARY sub-group id
    obs_row = cur.execute(
        "SELECT obs_id FROM wa_obs_question_catalogue "
        " WHERE question_code=? AND catalogue_version='v2-2026-04-29'",
        (QCODE,),
    ).fetchone()
    obs_id = obs_row["obs_id"]
    print(f"T1.2.1 obs_id = {obs_id}")

    bnd_row = cur.execute(
        "SELECT id FROM cluster_subgroup "
        " WHERE cluster_code=? AND subgroup_code='M32-BOUNDARY' "
        "   AND COALESCE(delete_flagged,0)=0",
        (CLUSTER_CODE,),
    ).fetchone()
    bnd_sg_id = bnd_row["id"]
    print(f"M32-BOUNDARY sub-group id = {bnd_sg_id}")

    n_inserted = 0
    try:
        cur.execute("BEGIN")
        for mti_id, strongs, version_suffix, body in BOUNDARY_ROWS:
            version = f"v1-bnd-{version_suffix}"
            cur.execute(
                "INSERT OR REPLACE INTO cluster_finding "
                "  (obs_id, cluster_code, cluster_subgroup_id, "
                "   finding_status, finding_text, source_file, "
                "   version, notes, created_at, last_updated_date, "
                "   delete_flagged) "
                "VALUES (?, ?, ?, 'finding', ?, ?, ?, ?, ?, ?, 0)",
                (obs_id, CLUSTER_CODE, bnd_sg_id, body, SOURCE_FILE,
                 version,
                 f"BOUNDARY structural characterisation row for {strongs} "
                 f"(mti={mti_id}). Per dir-005 §11 BOUNDARY treatment.",
                 ts, ts),
            )
            n_inserted += 1
            print(f"  + INSERT {strongs} mti={mti_id} version={version!r}")
        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print(f"BOUNDARY rows inserted: {n_inserted}")

    # Verification
    print()
    print("=== M32-BOUNDARY rows ===")
    for r in cur.execute(
        "SELECT cf.id, cf.version, q.question_code, cf.notes "
        "  FROM cluster_finding cf "
        "  JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id "
        " WHERE cf.cluster_code=? AND cf.cluster_subgroup_id=? "
        "   AND COALESCE(cf.delete_flagged,0)=0 "
        " ORDER BY cf.version",
        (CLUSTER_CODE, bnd_sg_id),
    ):
        print(f"  cf.id={r['id']:5d} q={r['question_code']} "
              f"version={r['version']!r}")

    print()
    print("=== M32 final by status ===")
    for r in cur.execute(
        "SELECT finding_status, COUNT(*) AS n FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY finding_status ORDER BY finding_status",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['finding_status']:25s} {r['n']:5d}")

    print()
    print("=== M32 final by scope ===")
    for r in cur.execute(
        "SELECT "
        "  CASE WHEN cluster_subgroup_id IS NULL THEN 'CLUSTER-LEVEL' "
        "       ELSE (SELECT subgroup_code FROM cluster_subgroup "
        "             WHERE id=cluster_finding.cluster_subgroup_id) END "
        "    AS scope, "
        "  COUNT(*) AS n "
        "  FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY scope ORDER BY scope",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['scope']:15s} {r['n']:5d}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
