"""_apply_m08_setasides_20260621.py — apply the M08 (Pride) set-asides confirmed by wa-m08-set-asides-v1_0.

Researcher direction 2026-06-21: "proceed with set asides". Inclusion-by-default — only items the
set-aside file CONFIRMS are removed; everything with residual doubt stays in.

  (I)  archO  (G0757)  inceptive-auxiliary / ruler-status — no inner-being pride content. TERM-LEVEL
       (all in-scope M08 occurrences; the file's 8 Mat/Mar/Luk uses). 55 already set aside.
  (I)  ro.hav (H7296)  Psa 90:10 'span/extent' sense, gloss/sense mismatch — not pride. TERM-LEVEL (1).
  (III) literal/physical height — only the occurrences the file NAMES as set-aside:
        qo.mah (H6967) @ 1Sa 16:7, 2Ki 19:23, Isa 37:24
        ga.vo.ah (H1364) @ 1Sa 16:7
        ma.rom (H4791) @ 2Ki 19:23, Isa 37:24
       (all other height-noun occurrences kept in-scope — pride-of-self or residual doubt — pending
        per-occurrence detail confirmation; akrates G0193 KEPT, cat II ownership flag only.)

Occurrence-level set_aside_reason (reversible; keeps term assignment; honoured by extract + FA-11).
  python scripts/_apply_m08_setasides_20260621.py --dry-run | --live
"""
import argparse, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
R_ARCHO = "M08 set-aside (researcher 2026-06-21): archO inceptive-auxiliary / ruler-status — no inner-being pride content (set-aside file cat I)"
R_ROHAV = "M08 set-aside (researcher 2026-06-21): ro.hav 'span/extent' sense (Psa 90:10), not pride (set-aside file cat I, gloss/sense mismatch)"
R_HEIGHT = "M08 set-aside (researcher 2026-06-21): literal/physical height (stature/mountains/tallest cedars), not pride-of-self (set-aside file cat III, file-named)"

# term-level set-asides (all in-scope occurrences of the lemma)
TERMS = [("G0757", R_ARCHO), ("H7296", R_ROHAV)]
# occurrence-level literal-height: (strongs, [refs], reason)
HEIGHT = [
    ("H6967", ["1Sa 16:7", "2Ki 19:23", "Isa 37:24"], R_HEIGHT),
    ("H1364", ["1Sa 16:7"], R_HEIGHT),
    ("H4791", ["2Ki 19:23", "Isa 37:24"], R_HEIGHT),
]


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
               WHERE m.cluster_code='M08' AND m.strongs_number=? AND COALESCE(vc.delete_flagged,0)=0 AND vc.set_aside_reason IS NULL"""
        p = [strongs]
        if refs:
            q += " AND vc.verse_record_id IN (SELECT id FROM wa_verse_records WHERE reference IN (%s))" % ",".join("?" * len(refs))
            p += refs
        return [r["id"] for r in cur.execute(q, p)]

    print("== M08 set-asides ==")
    for sn, reason in TERMS:
        ids = target(sn)
        tr = cur.execute("SELECT transliteration tr, gloss FROM mti_terms WHERE strongs_number=? AND cluster_code='M08' LIMIT 1", (sn,)).fetchone()
        print(f"   [I  ] {sn} {tr['tr']:10} ({tr['gloss']}): {len(ids)} in-scope occurrence(s) -> set aside (term-level)")
        if a.live and ids:
            cur.executemany("UPDATE verse_context SET set_aside_reason=? WHERE id=?", [(reason, i) for i in ids])
        total += len(ids)
    for sn, refs, reason in HEIGHT:
        ids = target(sn, refs)
        tr = cur.execute("SELECT transliteration tr, gloss FROM mti_terms WHERE strongs_number=? AND cluster_code='M08' LIMIT 1", (sn,)).fetchone()
        print(f"   [III] {sn} {tr['tr']:10} ({tr['gloss']}) @ {refs}: {len(ids)} occurrence(s) -> set aside")
        if a.live and ids:
            cur.executemany("UPDATE verse_context SET set_aside_reason=? WHERE id=?", [(reason, i) for i in ids])
        total += len(ids)

    if a.dry_run:
        print(f"\n[DRY-RUN] would set aside {total} occurrences. No changes."); return 0
    conn.commit()
    db_in = cur.execute("""SELECT COUNT(DISTINCT CASE WHEN vc.set_aside_reason IS NULL THEN vr.reference END) n
        FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        WHERE m.cluster_code='M08' AND COALESCE(vc.delete_flagged,0)=0""").fetchone()["n"]
    print(f"\nLIVE: {total} occurrences set aside. M08 in-scope verses now: {db_in}.")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
