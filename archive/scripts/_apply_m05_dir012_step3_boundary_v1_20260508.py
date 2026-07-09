"""_apply_m05_dir012_step3_boundary_v1_20260508.py — DB-modifying.

DIR-20260507-M05-012, Step 3 — BOUNDARY structural rows.

Creates 5 rows on M05-BOUNDARY (cluster_subgroup_id=16), one per
structural category from WA-M05-BOUNDARY-findings-v1-20260507.md.

Per Option A (M06 precedent), each row uses a real obs_id from the
T-code that best matches the category's analytical function. The
finding_text is prefixed with '**BOUNDARY characterisation —**' so
SQL filtering on these rows remains easy.

Mapping:
  Cat 1 — Physical embodiment    -> T2.6.1 (body-part location)
  Cat 2 — Attractive qualities   -> T1.5.1 (immediate inner-being response)
  Cat 3 — Freedom from disorder  -> T1.4.2 (context / direction / level)
  Cat 4 — Assembly occasions     -> T1.7.1 (conditions for reception)
  Cat 5 — Demonstrative acts     -> T1.4.3 (communicative / speech mode)
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M05"
BOUNDARY_SG_ID = 16
PATCH_VERSION = "v1"
SOURCE_FILE = "WA-M05-BOUNDARY-findings-v1-20260507.md"

ROWS = [
    # (qcode_anchor, finding_text)
    ("T2.6.1",
     "**BOUNDARY characterisation — Category 1: Physical locations and "
     "acts of relational expression.** Terms: H2436G cheq (bosom/embrace), "
     "G5370 filēma (kiss), G2705 katafileō (to kiss). These terms name "
     "the bodily, spatial, and somatic register through which the "
     "cluster's inner characteristics are expressed outward. The bosom "
     "is the physical location of intimacy — the space where cherishing "
     "is enacted in the body (Rut 4:16; 2Sa 12:3; Isa 40:11). The kiss "
     "is the enacted outward sign of the inner relational state: holy "
     "kiss of greeting (Rom 16:16; 1Cor 16:20; 2Cor 13:12; 1Th 5:26; "
     "1Pe 5:14); kiss of Judas (Mat 26:49; Mar 14:45; Luk 22:48). "
     "Why BOUNDARY: these terms name the expressive act or spatial "
     "location — the point where the inner characteristic contacts the "
     "body and the social world. Cheq is where love is held, not love "
     "itself; filēma is what love does with the face, not what love is. "
     "What this reveals: the cluster's inner characteristics are not "
     "merely cognitive or volitional but seek embodied expression."),

    ("T1.5.1",
     "**BOUNDARY characterisation — Category 2: Qualities of objects "
     "that direct inner attention.** Terms: H5000 na.eh (lovely / "
     "fitting / becoming), G4375 prosfilēs (lovely / commendable / "
     "praiseworthy). These terms name the quality in an object or act "
     "that makes it fitting, beautiful, or praiseworthy — the "
     "attractiveness that draws the inner person's attention and "
     "evaluation toward it. Na.eh appears in aesthetic-evaluative "
     "contexts (Psa 33:1 — Group 1591; Song 2:14, 4:3, 6:4 — Group "
     "1591; Pro 17:7, 19:10, 26:1 — Group 1591). Prosfilēs appears in "
     "Phili 4:8 (Group 1552): 'whatever is lovely, whatever is "
     "commendable... think about these things' — directing the mind's "
     "moral attentiveness. Why BOUNDARY: these terms name the quality "
     "of the object that elicits inner-being response — they describe "
     "what calls forth the love, admiration, or attention, not the love "
     "itself. What this reveals: the cluster's characteristics are "
     "always responsive to something that is genuinely lovely, fitting, "
     "or commendable. Love is constitutively directional, defined by "
     "its object."),

    ("T1.4.2",
     "**BOUNDARY characterisation — Category 3: Freedom from disordered "
     "love.** Term: G0866 afilarguros (not greedy / not a lover of "
     "money / free from love of money). Names the inner character "
     "quality of freedom from the love of money — required of leaders "
     "(1Ti 3:3 — Group 1549; Heb 13:5 — Group 1549). Why BOUNDARY: "
     "afilarguros is a negative qualifier — it names the absence of a "
     "disordered love orientation rather than the presence of a "
     "positive one. The positive love characteristic is in M05-A; "
     "afilarguros names the removal of an obstacle to that love. "
     "What this reveals: love-of-money is a structural distortion of "
     "the love characteristic — a misdirection of the love-orientation "
     "toward material goods. Genuine love-orientation requires a "
     "cleared inner space — the love-of-money must be absent before "
     "the love of God and community can be primary. This confirms M05's "
     "understanding of love as constitutively directional: the wrong "
     "direction (money) structurally crowds out the right direction "
     "(God, neighbour)."),

    ("T1.7.1",
     "**BOUNDARY characterisation — Category 4: Assembly occasions.** "
     "Terms: G1577 ekklēsia (assembly/church), H4744 miq.ra (assembly/"
     "convocation), H6116 a.tsa.rah (solemn assembly). These three terms "
     "name the communal occasions — the gathered assembly — in which "
     "the cluster's characteristics are collectively expressed, tested, "
     "and embodied. Ekklēsia names the church as the gathered community "
     "(Acts, Pauline epistles — Group 1712); miq.ra names the holy "
     "convocation of Israel (Lev 23); a.tsa.rah names the solemn "
     "assembly (Lev 23:36; Num 29:35; Deu 16:8; 2Ch 7:9; Joel 1:14; "
     "2:15; Amo 5:21 — Group 2148). Why BOUNDARY: the assembly terms "
     "name the occasion rather than the characteristic. What happens "
     "in the assembly — love, fellowship, worship, compassion — belongs "
     "to the characteristics; the assembly itself is the social occasion "
     "that gathers and structures those expressions. The a.tsa.rah "
     "exception (Group 2148, Amo 5:21): God's rejection of the assembly "
     "reveals that the inner moral state of participants is the decisive "
     "factor — but this evidence supports M05-A and M05-D rather than "
     "making a.tsa.rah itself characteristic-bearing. What this reveals: "
     "M05's characteristics are constitutively communal — tested and "
     "exposed in gathered community life. The outer form of communal "
     "worship without the inner characteristics it is meant to embody "
     "is abhorrent (Amo 5:21)."),

    ("T1.4.3",
     "**BOUNDARY characterisation — Category 5: Demonstrative and "
     "expressive acts.** Terms: G1731 endeiknumi (to show/demonstrate), "
     "G1517 eirēnopoieō (to make peace), G1433 dōreō (to give/grant). "
     "Endeiknumi (Group 3218): the act of showing or demonstrating love "
     "(2Cor 8:24), divine power (Rom 9:17), patience and wrath (Rom "
     "9:22), and the work of the law on hearts (Rom 2:15). The act of "
     "showing reveals the characteristic; it is not the characteristic. "
     "Eirēnopoieō (Group 1712, Col 1:20): Christ's reconciling work "
     "that restores the broken relationship — the means to fellowship, "
     "not fellowship itself. Dōreō (Group 2597, 2Pe 1:3): God's "
     "granting of all things needed for inner transformation; the "
     "giving act enables M05-G participation but is not itself the "
     "participation. Why BOUNDARY: these acts demonstrate, express, or "
     "enable the cluster's characteristics without being them. What "
     "this reveals: the cluster's characteristics need to be shown, "
     "enacted, and enabled before they are fully real in the human "
     "community. Love must be demonstrated; fellowship requires the "
     "peace-making that removes enmity; participation in divine life "
     "requires the divine granting act."),
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    print(f"DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Resolve obs_ids
    obs_by_q = {}
    for r in cur.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        " WHERE catalogue_version='v2-2026-04-29' "
        "   AND COALESCE(deleted,0)=0"
    ):
        obs_by_q[r["question_code"]] = r["obs_id"]

    halts = []
    for qc, _ in ROWS:
        if qc not in obs_by_q:
            halts.append(qc)
    if halts:
        print(f"[err] obs_ids not found for: {halts}")
        return 1

    n_inserted = 0
    n_skipped = 0
    ts = now_iso()

    try:
        cur.execute("BEGIN")
        for qc, body in ROWS:
            obs_id = obs_by_q[qc]
            cur.execute(
                "INSERT OR IGNORE INTO cluster_finding "
                "  (obs_id, cluster_code, cluster_subgroup_id, "
                "   finding_status, finding_text, source_file, "
                "   version, created_at, last_updated_date, "
                "   delete_flagged) "
                "VALUES (?, ?, ?, 'finding', ?, ?, ?, ?, ?, 0)",
                (obs_id, CLUSTER_CODE, BOUNDARY_SG_ID,
                 body, SOURCE_FILE, PATCH_VERSION, ts, ts),
            )
            if cur.rowcount:
                n_inserted += 1
            else:
                n_skipped += 1
        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print(f"BOUNDARY rows inserted: {n_inserted}")
    print(f"Already-present (skipped): {n_skipped}")

    # Verification
    print()
    print("=== M05-BOUNDARY rows ===")
    for r in cur.execute(
        "SELECT cf.id, q.question_code, cf.finding_status, "
        "       SUBSTR(cf.finding_text, 1, 90) AS preview "
        "  FROM cluster_finding cf "
        "  JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id "
        " WHERE cf.cluster_code=? AND cf.cluster_subgroup_id=? "
        "   AND COALESCE(cf.delete_flagged,0)=0 "
        " ORDER BY cf.id",
        (CLUSTER_CODE, BOUNDARY_SG_ID),
    ):
        print(f"  cf.id={r['id']} q={r['question_code']:8s} "
              f"status={r['finding_status']:10s}")
        print(f"    {r['preview']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
