"""_apply_m07_setaside_jkresid_20260621.py — set aside the M07 J / K / RESID bands (researcher decision 2026-06-21).

Occurrence-level set_aside_reason (reversible; keeps term assignment; honoured by the ve_lexical extract + FA-11).
  J  innocence antonym  — niq.qa.von (H5356A, 4) + qe.ha.von (H5356B, 4) = 8
  K  silencing/casting  — fimoO (G5392, 8) + afOnos (G0880, 4) + apoballO (G0577, 2) = 14   (ni.dah retained)
  RESID ka.lam non-shame "harm/injure" sense — H3637 @ 1Sa 25:7, 1Sa 25:15 = 2 (occurrence-level only)

  python scripts/_apply_m07_setaside_jkresid_20260621.py --dry-run | --live
"""
import argparse, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
J_REASON = "M07 J set-aside (researcher 2026-06-21): innocence/cleanness antonym pole — not an inner-being shame characteristic"
K_REASON = "M07 K set-aside (researcher 2026-06-21): silencing/casting term — behavioural/physical, not inner-being shame"
R_REASON = "M07 RESID set-aside (researcher 2026-06-21): ka.lam non-shame 'harm/injure' sense"
TERMS = [("H5356A", J_REASON), ("H5356B", J_REASON), ("G5392", K_REASON), ("G0880", K_REASON), ("G0577", K_REASON)]
RESID = ("H3637", ["1Sa 25:7", "1Sa 25:15"], R_REASON)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    total = 0

    def target(strongs, refs=None):
        q = """SELECT vc.id FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
               WHERE m.cluster_code='M07' AND m.strongs_number=? AND COALESCE(vc.delete_flagged,0)=0 AND vc.set_aside_reason IS NULL"""
        p = [strongs]
        if refs:
            q += " AND vc.verse_record_id IN (SELECT id FROM wa_verse_records WHERE reference IN (%s))" % ",".join("?" * len(refs))
            p += refs
        return [r["id"] for r in cur.execute(q, p)]

    print("== M07 J/K/RESID set-aside ==")
    for sn, reason in TERMS:
        ids = target(sn)
        tr = cur.execute("SELECT transliteration tr, gloss FROM mti_terms WHERE strongs_number=? LIMIT 1", (sn,)).fetchone()
        band = "J" if reason is J_REASON else "K"
        print(f"   [{band}] {sn} {tr['tr']:12} ({tr['gloss']}): {len(ids)} occurrence(s) -> set aside")
        if a.live and ids:
            cur.executemany("UPDATE verse_context SET set_aside_reason=? WHERE id=?", [(reason, i) for i in ids])
        total += len(ids)
    rids = target(RESID[0], RESID[1])
    print(f"   [RESID] {RESID[0]} ka.lam @ {RESID[1]}: {len(rids)} occurrence(s) -> set aside")
    if a.live and rids:
        cur.executemany("UPDATE verse_context SET set_aside_reason=? WHERE id=?", [(RESID[2], i) for i in rids])
    total += len(rids)

    if a.dry_run:
        print(f"\n[DRY-RUN] would set aside {total} occurrences. No changes."); return 0
    conn.commit()
    # verify new M07 in-scope count
    db_in = cur.execute("""SELECT COUNT(DISTINCT CASE WHEN vc.set_aside_reason IS NULL THEN vr.reference END) n
        FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        WHERE m.cluster_code='M07' AND COALESCE(vc.delete_flagged,0)=0""").fetchone()["n"]
    print(f"\nLIVE: {total} occurrences set aside. M07 in-scope verses now: {db_in}.")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
