"""
_apply_drop_code_softdelete.py — MODIFIES DB. Soft-delete every finding referencing the §3 DROP tier codes
(catalogue restructured v2), plus the underlying Session B findings and their catalogue links.

Approved 2026-06-11: the DROP families are peppered with fabricated/templated data not worth validating.
Soft-delete only (reversible: set the delete flag back to 0). Session D layer is empty (nothing to delete).

Scope (active rows referencing DROP obs_ids 241,257-259,282-284,366-368,387-392):
  - cluster_finding            -> delete_flagged = 1   (cluster-level DROP findings)
  - wa_session_b_findings      -> delete_flag = 1      (underlying Session B findings, via catalogue links)
  - wa_finding_catalogue_links -> delete_flagged = 1   (the DROP links, for consistency)

Usage:  python scripts/_apply_drop_code_softdelete.py --dry-run
        python scripts/_apply_drop_code_softdelete.py --live
"""
import os, sqlite3, argparse, datetime

DB = os.path.join('database', 'bible_research.db')
DROP_OBS = [241, 257, 258, 259, 282, 283, 284, 366, 367, 368, 387, 388, 389, 390, 391, 392]
REASON = "DROP per catalogue restructure v2 §3 (2026-06-11): fabricated/templated DROP-family finding, not validated"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--dry-run', action='store_true')
    g.add_argument('--live', action='store_true')
    args = ap.parse_args()
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()
    ph = ','.join('?' * len(DROP_OBS))

    qn = c.execute(f"SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE obs_id IN ({ph}) AND deleted=0", DROP_OBS).fetchone()[0]
    cf = c.execute(f"SELECT COUNT(*) FROM cluster_finding WHERE obs_id IN ({ph}) AND delete_flagged=0", DROP_OBS).fetchone()[0]
    sb = c.execute(f"""SELECT COUNT(DISTINCT sb.id) FROM wa_finding_catalogue_links l
                       JOIN wa_session_b_findings sb ON sb.id=l.finding_id
                       WHERE l.question_id IN ({ph}) AND sb.delete_flag=0""", DROP_OBS).fetchone()[0]
    lk = c.execute(f"SELECT COUNT(*) FROM wa_finding_catalogue_links WHERE question_id IN ({ph}) AND delete_flagged=0", DROP_OBS).fetchone()[0]

    print(f"DROP soft-delete scope (active):")
    print(f"  wa_obs_question_catalogue   : {qn}  (the 16 §3 DROP questions)")
    print(f"  cluster_finding             : {cf}")
    print(f"  wa_session_b_findings       : {sb}  (underlying Session B)")
    print(f"  wa_finding_catalogue_links  : {lk}  (links)")
    print(f"  session_d                   : 0   (empty layer)")

    if args.dry_run:
        print("\n[DRY-RUN] no changes written.")
        return

    # ---- LIVE ----
    with conn:
        conn.execute(f"""UPDATE wa_obs_question_catalogue SET deleted=1, status='dropped', review_note=?
                         WHERE obs_id IN ({ph}) AND deleted=0""", [REASON] + DROP_OBS)
        conn.execute(f"""UPDATE cluster_finding SET delete_flagged=1, last_updated_date=?,
                         notes = COALESCE(notes||' | ','')||? WHERE obs_id IN ({ph}) AND delete_flagged=0""",
                     [now, REASON] + DROP_OBS)
        sb_ids = [r[0] for r in conn.execute(f"""SELECT DISTINCT sb.id FROM wa_finding_catalogue_links l
                         JOIN wa_session_b_findings sb ON sb.id=l.finding_id
                         WHERE l.question_id IN ({ph}) AND sb.delete_flag=0""", DROP_OBS)]
        if sb_ids:
            iph = ','.join('?' * len(sb_ids))
            conn.execute(f"""UPDATE wa_session_b_findings SET delete_flag=1, obsolete_date=?,
                             obsolete_reason=? WHERE id IN ({iph})""", [now, REASON] + sb_ids)
        conn.execute(f"""UPDATE wa_finding_catalogue_links SET delete_flagged=1
                         WHERE question_id IN ({ph}) AND delete_flagged=0""", DROP_OBS)

    # verify
    cf2 = c.execute(f"SELECT COUNT(*) FROM cluster_finding WHERE obs_id IN ({ph}) AND delete_flagged=0", DROP_OBS).fetchone()[0]
    sb2 = c.execute(f"""SELECT COUNT(DISTINCT sb.id) FROM wa_finding_catalogue_links l
                        JOIN wa_session_b_findings sb ON sb.id=l.finding_id
                        WHERE l.question_id IN ({ph}) AND sb.delete_flag=0""", DROP_OBS).fetchone()[0]
    lk2 = c.execute(f"SELECT COUNT(*) FROM wa_finding_catalogue_links WHERE question_id IN ({ph}) AND delete_flagged=0", DROP_OBS).fetchone()[0]
    qn2 = c.execute(f"SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE obs_id IN ({ph}) AND deleted=0", DROP_OBS).fetchone()[0]
    print(f"\n[LIVE] soft-deleted. Remaining active DROP refs -> catalogue_questions {qn2}, cluster_finding {cf2}, session_b {sb2}, links {lk2} (expect 0/0/0/0).")


if __name__ == '__main__':
    main()
