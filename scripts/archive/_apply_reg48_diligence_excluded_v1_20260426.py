"""_apply_reg48_diligence_excluded_v1_20260426.py

L1 + L2 + exclude registry 48 diligence: concept covered by zeal (181).

Actions (single transaction):
  1. word_registry no=48:
       verse_context_status = NULL  (was 'Complete' but no groups exist — inconsistent)
       session_b_status     = NULL  (was 'Verse Context Reset')
       inference_note       = (covered-by-zeal rationale; preserves audit trail)
  2. mti_terms — mark 5 HFA / proper-noun OWNER terms as 'delete':
       H0608 'you' (mti=5074)
       H3606 'all' (mti=5076)
       H3635A 'to complete' (mti=5078)
       H3644H '[Geruth] Chimham' (mti=5079)
       H3660 'thus' (mti=815)
  3. mti_terms — mark H0629 'diligently' (mti=814) as 'excluded'
     (legitimate term but registry now excluded; verses preserved for reference).
  4. wa_verse_records — soft-delete (delete_flagged=1) the 75 verses of the
     5 HFA/proper-noun terms (1+61+7+1+5 = 75). H0629's 7 verses stay active.

Justification:
  - Registry 48 inventory was an extraction-anomaly residue: 5 of 6 OWNER terms
    are Aramaic/Hebrew function words (you, all, thus, like) plus one proper-noun
    fragment ([Geruth] Chimham). Same pattern as covenant/faith/purpose/thought
    PH2_DATA_ERROR series.
  - The genuine NT 'diligence' family (G4710 spoudē, G4704 spoudazō, G4705
    spoudaios) is owned by registry 181 zeal. STEP literally glosses G4710 as
    'diligence'. Hebrew diligence terms not in MTI (H2742 cha.ruts, H8104
    sha.mar, H4106 mahir misplaced in fear). The 'diligence' concept is
    operationally covered by zeal.
  - Investigation: outputs/investigations/diligence-registry-investigation-v1-20260426.md.

Run --dry-run first; commits only with --live. Archive after the run.
"""
from __future__ import annotations
import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")

REGISTRY_NO = 48

DELETE_TARGETS = [
    (5074, "H0608",  "you"),
    (5076, "H3606",  "all"),
    (5078, "H3635A", "to complete"),
    (5079, "H3644H", "[Geruth] Chimham"),
    (815,  "H3660",  "thus"),
]

EXCLUDED_TARGETS = [
    (814, "H0629", "diligently"),
]

INFERENCE_NOTE = (
    "Registry excluded 2026-04-26: concept of diligence is covered by registry "
    "181 zeal. The classic NT diligence family (G4710 spoudē — STEP's literal "
    "gloss is 'diligence' — plus G4704 spoudazō and G4705 spoudaios) lives in "
    "zeal as OWNER. Hebrew diligence vocabulary is either absent from the MTI "
    "(H2742 cha.ruts, H8104 sha.mar, G4709 spoudaiōs, G1567 ekzēteō) or "
    "mis-placed (H4106 mahir in registry 61 fear). Of registry 48's original "
    "6 OWNER terms, 5 were extraction-anomaly function words (you/all/to "
    "complete/proper-noun/thus) — set to status=delete; only H0629 os.par.na "
    "'diligently' (7 Aramaic verses, Daniel/Ezra) was on-topic, set to "
    "status=excluded with verses preserved for reference. The diligence "
    "concept is not lost — it lives under zeal. Investigation: "
    "outputs/investigations/diligence-registry-investigation-v1-20260426.md."
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_state(conn, label):
    print(f"--- state ({label}) ---")
    cur = conn.cursor()
    cur.execute(
        "SELECT no, word, verse_context_status, session_b_status, "
        "       SUBSTR(COALESCE(inference_note,''), 1, 80) AS note "
        "FROM word_registry WHERE no=?", (REGISTRY_NO,)
    )
    r = cur.fetchone()
    print(f"  reg {r[0]} {r[1]}: vc_status={r[2]} sb_status={r[3]}")
    print(f"    inference_note: {r[4] or '(none)'}")
    cur.execute(
        "SELECT id, strongs_number, status, last_changed FROM mti_terms "
        "WHERE id IN (5074, 5076, 5078, 5079, 815, 814) ORDER BY id"
    )
    for r in cur.fetchall():
        print(f"  mti_terms: mti={r[0]:5d} {r[1]:8s} status={r[2]:18s} last_changed={r[3]}")
    cur.execute("""
        SELECT mt.strongs_number,
               (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id AND vr.delete_flagged=0) AS active,
               (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id AND vr.delete_flagged=1) AS deleted
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE wr.no=? AND mt.id IN (5074, 5076, 5078, 5079, 815, 814)
         ORDER BY mt.strongs_number""", (REGISTRY_NO,))
    for r in cur.fetchall():
        print(f"  verses for {r[0]:8s}: active={r[1]}  deleted={r[2]}")


def apply(conn, dry_run):
    ts = now_iso()
    cur = conn.cursor()

    # 1. Registry update
    cur.execute(
        "UPDATE word_registry SET verse_context_status=NULL, session_b_status=NULL, "
        "       inference_note=? WHERE no=?",
        (INFERENCE_NOTE, REGISTRY_NO),
    )
    assert cur.rowcount == 1, f"expected 1 word_registry row updated, got {cur.rowcount}"

    # 2. mti_terms → delete
    for mti_id, _strongs, _gloss in DELETE_TARGETS:
        cur.execute(
            "UPDATE mti_terms SET status='delete', last_changed=? WHERE id=?",
            (ts, mti_id),
        )
        assert cur.rowcount == 1, f"expected 1 mti_terms row for mti={mti_id}, got {cur.rowcount}"

    # 3. mti_terms → excluded (H0629)
    for mti_id, _strongs, _gloss in EXCLUDED_TARGETS:
        cur.execute(
            "UPDATE mti_terms SET status='excluded', last_changed=? WHERE id=?",
            (ts, mti_id),
        )
        assert cur.rowcount == 1, f"expected 1 mti_terms row for mti={mti_id}, got {cur.rowcount}"

    # 4. wa_verse_records → delete_flagged=1 for the 5 HFA/proper-noun terms
    delete_strongs = tuple(s for _, s, _ in DELETE_TARGETS)
    placeholders = ",".join(["?"] * len(delete_strongs))
    cur.execute(f"""
        UPDATE wa_verse_records
           SET delete_flagged = 1, last_changed = ?
         WHERE delete_flagged = 0
           AND term_inv_id IN (
               SELECT ti.id FROM wa_term_inventory ti
                 JOIN wa_file_index fi ON fi.id = ti.file_id
                 JOIN word_registry wr ON wr.id = fi.word_registry_fk
                WHERE wr.no = ?
                  AND ti.term_owner_type = 'OWNER'
                  AND ti.delete_flagged = 0
                  AND ti.strongs_number IN ({placeholders})
           )
    """, (ts, REGISTRY_NO, *delete_strongs))
    print(f"  wa_verse_records: {cur.rowcount} rows soft-deleted")

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
