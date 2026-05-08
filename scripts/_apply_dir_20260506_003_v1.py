"""_apply_dir_20260506_003_v1.py — DB-modifying.

Apply DIR-20260506-003 (root, dimensional, BOUNDARY findings for M06).

Operation A1 — Resolved gap findings (T6.4.2, T6.7.1, T6.7.3, T7.1.9):
  Already complete from prior gap-resolution work. Verified by pre-flight.

Operation A2 — Root-connection sub-group findings (3 INSERTs):
  - T6.4.2 / M06-A — SATAM root extending into BOUNDARY (sho.tet)
  - T6.4.2 / M06-E — CHARAPH root linking cher.pah to cha.raph
  - T6.4.2 / M06-G — SUT root linking she.at to shut (M06-B)

Operation B — BOUNDARY term characterisations (4 INSERTs):
  Each BOUNDARY term gets a row at a closely-aligned prompt code, carrying
  verbatim characterisation text from the directive's Scope section.
  - T1.4.3 (speech-based mode) — cha.raph H2778A
  - T2.6.2 (body-link purpose) — ba.ash H0887
  - T0.3.1 (image-bearer expression) — afilagathos G0865
  - T1.4.1 (modes of operation) — sho.tet H7850

Idempotent: ON CONFLICT DO UPDATE for each row's unique key.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

DIRECTIVE_ID = "DIR-20260506-003"
SOURCE_FILE = "wa-cluster-M06-dir-003-root-boundary-v1-20260506.md"
COMPANION_FILE = "WA-M06-sessionC-readiness-v1-20260506.md"
VERSION = "v1"

# (question_code, scope_letter or 'BOUNDARY', finding_status, finding_text)
ROWS = [
    # --- Operation A2: root-connection findings at sub-group scope ---
    ("T6.4.2", "A", "finding",
     "**Root-architecture finding (DIR-20260506-003).** The SATAM root "
     "extends from M06-A's settled-hatred and atmospheric-hatred terms "
     "(H7852 sa.tam — grudge-bearing hatred; H4895 mas.te.mah — communal "
     "hostile climate) to the BOUNDARY scourge term (H7850 sho.tet). The "
     "shared root is structurally significant: sho.tet names the active "
     "driving / scourging behavioural form of what sa.tam holds as inner "
     "disposition. Hatred-at-its-most-active becomes a structural force "
     "against another (Num 33:55; Isa 28:15, 18). The lexical sharing is "
     "evidence that BOUNDARY terms are not unrelated to the cluster's "
     "core characteristics — they are their behavioural expression layer."),
    ("T6.4.2", "E", "finding",
     "**Root-architecture finding (DIR-20260506-003).** The CHARAPH root "
     "is shared between H2781 cher.pah (M06-E — reproach as inner-social "
     "condition) and H2778A cha.raph (BOUNDARY — to taunt). The shared "
     "root confirms at lexical level what the analysis identifies "
     "structurally: the taunt is the speech-act form of the reproach. "
     "Cha.raph names the verbal instrument that makes the cher.pah "
     "condition real and public in the recipient (Psa 42:10, Psa 44:16, "
     "Job 27:6). M06-E's inner-social condition has a corresponding "
     "BOUNDARY delivery mechanism — the taunt is what creates and "
     "sustains the reproach."),
    ("T6.4.2", "G", "finding",
     "**Root-architecture finding (DIR-20260506-003).** H7589 she.at "
     "(M06-G — malice) and H7590 shut (M06-B — contempt) are linked as "
     "related words sharing the SUT root family. The lexical link "
     "confirms the analytical claim that contempt is a constituent "
     "element of malice — malice (M06-G) is the compound of sustained "
     "enmity (M06-A elements) + contempt (M06-B / SUT-shared element) + "
     "pleasure in destruction. The vocabulary architecture mirrors the "
     "constitutive structure: she.at's SUT-relatedness with shut is the "
     "lexical signature of malice's contempt-element."),

    # --- Operation B: BOUNDARY term characterisations ---
    ("T1.4.3", "BOUNDARY", "finding",
     "**BOUNDARY characterisation — H2778A cha.raph (to taunt).** "
     "The taunting term — the speech-act through which reproach "
     "(cher.pah, M06-E) is actively delivered by the agent. Shares the "
     "CHARAPH root with cher.pah. In Psa 42:10, Psa 44:16, and Job 27:6 "
     "the taunt is the verbal instrument that makes the reproach-"
     "condition real and public in the recipient. The BOUNDARY role: "
     "cha.raph is the delivery mechanism for M06-E, operating at the "
     "speech-act surface of what cher.pah names as an inner-social "
     "condition. Recorded under T1.4.3 (communicative / speech-based "
     "mode of operation) as the closest catalogue prompt for a BOUNDARY "
     "structural-characterisation note."),
    ("T2.6.2", "BOUNDARY", "finding",
     "**BOUNDARY characterisation — H0887 ba.ash (to stink / make "
     "offensive).** The stench / offensiveness term — the social-sensory "
     "mark of being made repugnant to others. The root BASH names the "
     "condition of being regarded as a stench, which is the social "
     "register of M06-C's abhorrence. Where ta.av names the inner "
     "visceral recoil (M06-C), ba.ash names what the rejected person "
     "becomes in others' perception. The BOUNDARY role: ba.ash marks "
     "the outer social result of abhorrence being directed at a person "
     "or community — the social form of what M06-C names as an inner-"
     "being response. Recorded under T2.6.2 (body-link purpose — what "
     "Scripture is doing by making a body-link) because the stench "
     "metaphor is the body-sensory form Scripture uses for the "
     "abhorrence-recipient condition."),
    ("T0.3.1", "BOUNDARY", "finding",
     "**BOUNDARY characterisation — G0865 afilagathos (not loving good / "
     "hating good).** The NT compound hating-good term — the alpha-"
     "privative negation of filagathos (loving good), appearing only in "
     "2Ti 3:3's vice list. Confirmed NT-attested only via LSJ (no "
     "classical precedent — see T7.1.9). Shares the AGATH root with "
     "goodness vocabulary (M05 cluster). The BOUNDARY role: afilagathos "
     "names the characterological orientation that produces and sustains "
     "M06's disordered characteristics — the person who does not love "
     "good is the person from whom hatred, contempt, abhorrence, "
     "cruelty, and malice proceed. It is the inner-being ground-"
     "condition, not a characteristic itself. Recorded under T0.3.1 "
     "(image-bearer expression) as the closest catalogue prompt — "
     "afilagathos names a comprehensive disordering of the divine "
     "image's love-of-the-good orientation."),
    ("T1.4.1", "BOUNDARY", "finding",
     "**BOUNDARY characterisation — H7850 sho.tet (scourge / driving "
     "force).** The scourge / driving term — shares the SATAM root with "
     "H7852 sa.tam (M06-A grudge-bearing hatred) and H4895 mas.te.mah "
     "(M06-A hostile atmosphere). In Num 33:55 the scourge is what the "
     "remaining nations will be in Israel's sides; in Isa 28:15, 18 the "
     "'scourging whip' (sho.tet) is the instrument of the covenant with "
     "death. The BOUNDARY role: sho.tet names the active driving / "
     "scourging function of M06-A's settled hatred when it becomes a "
     "sustained structural force against another — the behavioural "
     "expression of sa.tam hatred at its most active and persistent. "
     "Recorded under T1.4.1 (distinct ways the characteristic operates) "
     "as the closest catalogue prompt for a BOUNDARY active-mode note."),
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_DIR, f"bible_research_{ts}_pre_dir003.db")
    shutil.copy2(DB_PATH, dest)
    return dest


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Pre-flight obs_id and subgroup lookups
    obs_by_code = {
        r["question_code"]: r["obs_id"]
        for r in conn.execute(
            "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
            " WHERE tier IS NOT NULL AND COALESCE(deleted,0)=0"
        )
    }
    sg_by_code = {
        r["subgroup_code"]: r["id"]
        for r in conn.execute(
            "SELECT id, subgroup_code FROM cluster_subgroup "
            " WHERE cluster_code='M06' AND COALESCE(delete_flagged,0)=0"
        )
    }

    # Verify Op A1 (resolved gaps already complete)
    print("Operation A1 — verifying resolved gap rows already present:")
    a1_ok = True
    for code in ("T6.4.2", "T6.7.1", "T6.7.3", "T7.1.9"):
        r = conn.execute("""
            SELECT cf.finding_status FROM cluster_finding cf
              JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
             WHERE cf.cluster_code='M06' AND oqc.question_code=?
               AND cf.cluster_subgroup_id IS NULL
               AND COALESCE(cf.delete_flagged,0)=0
        """, (code,)).fetchone()
        ok = r is not None and r["finding_status"] == "finding"
        a1_ok = a1_ok and ok
        print(f"  {code}: {r['finding_status'] if r else 'MISSING'}  "
              f"{'OK' if ok else 'NEEDS_FIX'}")
    if not a1_ok:
        print("  ! Op A1 not complete — halting before Op A2/B writes.")
        return 2
    print()

    # Apply Op A2 + Op B
    note = (
        f"Applied via {DIRECTIVE_ID} on 2026-05-06; "
        f"directive: {SOURCE_FILE}; "
        f"obslog: wa-obslog-M06-m06-method-v1-20260506"
    )
    n_inserted = n_updated = 0
    actions = []

    try:
        conn.execute("BEGIN")
        for qcode, scope, status, text in ROWS:
            obs_id = obs_by_code.get(qcode)
            if not obs_id:
                raise RuntimeError(f"unknown question_code {qcode}")
            if scope == "CLUSTER":
                sg_id = None
            elif scope == "BOUNDARY":
                sg_id = sg_by_code.get("BOUNDARY")
            else:
                sg_id = sg_by_code.get(f"M06-{scope}")
            if scope != "CLUSTER" and not sg_id:
                raise RuntimeError(f"unknown sub-group scope {scope}")

            # Source file: BOUNDARY characterisations cite the companion
            # readiness doc; root-connection findings cite this directive.
            src = COMPANION_FILE if scope == "BOUNDARY" else SOURCE_FILE

            # Try UPDATE first; if no row, INSERT.
            if sg_id is None:
                cur = conn.execute("""
                    UPDATE cluster_finding
                       SET finding_status=?, finding_text=?,
                           source_file=?, notes=?, last_updated_date=?
                     WHERE obs_id=? AND cluster_code='M06'
                       AND cluster_subgroup_id IS NULL AND version=?
                """, (status, text, src, note, now_iso(),
                      obs_id, VERSION))
            else:
                cur = conn.execute("""
                    UPDATE cluster_finding
                       SET finding_status=?, finding_text=?,
                           source_file=?, notes=?, last_updated_date=?
                     WHERE obs_id=? AND cluster_code='M06'
                       AND cluster_subgroup_id=? AND version=?
                """, (status, text, src, note, now_iso(),
                      obs_id, sg_id, VERSION))
            if cur.rowcount == 0:
                conn.execute("""
                    INSERT INTO cluster_finding
                      (obs_id, cluster_code, cluster_subgroup_id,
                       finding_status, finding_text, source_file, version,
                       notes, delete_flagged, created_at, last_updated_date)
                    VALUES (?, 'M06', ?, ?, ?, ?, ?, ?, 0, ?, ?)
                """, (obs_id, sg_id, status, text, src, VERSION,
                      note, now_iso(), now_iso()))
                n_inserted += 1
                actions.append(f"INSERT  {qcode:8s} {scope:9s} ok")
            else:
                n_updated += 1
                actions.append(f"UPDATE  {qcode:8s} {scope:9s} ok")
        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print("Operation A2 + B writes:")
    for a in actions:
        print(f"  {a}")
    print(f"\nINSERTs: {n_inserted}, UPDATEs: {n_updated}")

    # ---- Completion confirmation queries (per directive §Completion)
    print()
    print("=" * 70)
    print("Completion confirmation")
    print("=" * 70)

    print("\n1. Resolved-gap rows (T6.4.2, T6.7.1, T6.7.3, T7.1.9 / CLUSTER):")
    for r in conn.execute("""
        SELECT oqc.question_code, cf.finding_status,
               SUBSTR(cf.finding_text,1,80) AS excerpt
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
         WHERE cf.cluster_code='M06'
           AND oqc.question_code IN ('T6.4.2','T6.7.1','T6.7.3','T7.1.9')
           AND cf.cluster_subgroup_id IS NULL
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY oqc.question_code
    """):
        print(f"  {r['question_code']:8s} status={r['finding_status']:8s} "
              f"\"{r['excerpt']}\"")

    print("\n2. Root-connection findings (T6.4.2 / M06-A, M06-E, M06-G):")
    for r in conn.execute("""
        SELECT oqc.question_code, cs.subgroup_code, cf.finding_status,
               SUBSTR(cf.finding_text,1,80) AS excerpt
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
          JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code='M06' AND oqc.question_code='T6.4.2'
           AND cs.subgroup_code IN ('M06-A','M06-B','M06-E','M06-G')
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY cs.subgroup_code
    """):
        print(f"  {r['question_code']} {r['subgroup_code']:6s} "
              f"status={r['finding_status']:8s} \"{r['excerpt']}\"")

    print("\n3. BOUNDARY findings:")
    for r in conn.execute("""
        SELECT oqc.question_code, cs.subgroup_code, cf.finding_status,
               SUBSTR(cf.finding_text,1,60) AS excerpt
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
          JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code='M06' AND cs.subgroup_code='BOUNDARY'
           AND cf.finding_text NOT LIKE '[Sub-group not%'
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY oqc.question_code
    """):
        print(f"  {r['question_code']:8s} status={r['finding_status']:8s} "
              f"\"{r['excerpt']}\"")

    print("\n4. Remaining gap rows for M06:")
    n = conn.execute(
        "SELECT COUNT(*) FROM cluster_finding "
        " WHERE cluster_code='M06' AND finding_status='gap' "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  remaining_gaps = {n}")
    for r in conn.execute("""
        SELECT oqc.question_code, cs.subgroup_code
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code='M06' AND cf.finding_status='gap'
           AND COALESCE(cf.delete_flagged,0)=0
    """):
        print(f"    {r['question_code']:8s} "
              f"scope={r['subgroup_code'] or 'CLUSTER'}")

    print("\n5. wa_session_b_findings — confirm no rows written today:")
    n = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
         WHERE COALESCE(raised_date,'') LIKE '2026-05-06%'
            OR COALESCE(raised_date,'') LIKE '20260506%'
    """).fetchone()[0]
    print(f"  rows with 2026-05-06 raised_date = {n}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
