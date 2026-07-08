"""Proverbs re-read success measures (G0-G8) — READ-ONLY.

Runs the acceptance-test gates from
`verse-analysis/_reports/wa-proverbs-reread-success-criteria-20260708.md`
against the CURRENT active state of Proverbs (book_id=20).

Reusable: run now for the BASELINE (prior/compromised read), and again after the
re-read to show the delta. Measures "active current state" (delete_flagged=0, any
provenance) so the same script captures both before and after; a provenance breakdown
is printed so the shift is visible.

Usage:
  python scripts/_check_proverbs_reread_measures_v1_20260708.py --label baseline
No writes. Prints a structured report to stdout.
"""
import sqlite3, os, argparse

DB = os.path.join('database', 'bible_research.db')
BID = 20
BUDGET = 12  # G0 char-spans/unit ceiling

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', default='baseline')
    args = ap.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    q = lambda s, *a: c.execute(s, a).fetchall()
    one = lambda s, *a: c.execute(s, a).fetchone()[0]

    def hdr(t): print('\n### ' + t)
    print(f"# Proverbs re-read measures — label={args.label}")

    # ---- structural stats ----
    hdr('STRUCTURE')
    print('verses:', one('SELECT COUNT(*) FROM verse WHERE book_id=?', BID))
    tot_cand = one('SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1', BID)
    cand_verses = one('SELECT COUNT(DISTINCT s.verse_id) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1', BID)
    print('candidate char-spans:', tot_cand, '| distinct candidate verses:', cand_verses)
    print('active segment_units (Pro):', one("SELECT COUNT(*) FROM segment_unit WHERE book='Pro' AND COALESCE(delete_flagged,0)=0"))
    print('role distribution (master):')
    for r in q('SELECT COALESCE(role,"(null)") role, COALESCE(role_provenance,"(null)") rp, COUNT(*) n FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? GROUP BY role, role_provenance ORDER BY n DESC', BID):
        print(f'   {r["role"]:20} {r["rp"]:20} {r["n"]}')
    print('active ve_lexical rows by provenance:')
    for r in q('SELECT COALESCE(l.source_provenance,"(null)") p, COUNT(*) n FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND COALESCE(l.delete_flagged,0)=0 GROUP BY l.source_provenance ORDER BY n DESC', BID):
        print(f'   {r["p"]:28} {r["n"]}')

    # ---- G0 digestion budget ----
    hdr('G0 digestion budget (units > %d char-spans)  PASS=0' % BUDGET)
    over = q('''SELECT su.unit_code, su.unit_type, COUNT(*) cs
        FROM segment_unit su JOIN segment_unit_verse suv ON suv.unit_id=su.id
        JOIN verse_span_index s ON s.verse_id=suv.verse_id AND s.char_candidate=1
        WHERE su.book='Pro' AND COALESCE(su.delete_flagged,0)=0
        GROUP BY su.unit_code HAVING COUNT(*) > ? ORDER BY cs DESC''', BUDGET)
    print('units over budget:', len(over))
    for r in over: print(f'   {r["unit_code"]:22} {r["unit_type"]} {r["cs"]}')

    # ---- G1 completeness ----
    hdr('G1 nothing passed over  PASS=0/0')
    g1a = one('SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1 AND s.role IS NULL', BID)
    g1b = one('''SELECT COUNT(DISTINCT v.id) FROM verse v WHERE v.book_id=?
        AND EXISTS (SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1)
        AND v.process_marker IS NULL''', BID)
    print('candidate spans with role NULL (undecided):', g1a)
    print('char-bearing verses not marked processed:', g1b)

    # ---- G2 worked not named ----
    hdr('G2 worked, not named  PASS=0/0')
    g2a = one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND s.role='characteristic'
        AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0)''', BID)
    g2b = one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND s.role='characteristic'
        AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=106 AND COALESCE(l.delete_flagged,0)=0)''', BID)
    print('characteristic spans with NO active lexical:', g2a)
    print('characteristic spans with NO operation(106):', g2b)

    # ---- G3 grounding ----
    hdr('G3 read from the verse  PASS=0/0')
    g3a = one('''SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND COALESCE(l.delete_flagged,0)=0 AND l.value IS NOT NULL AND l.resolution IS NULL''', BID)
    g3b = one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND s.role='characteristic' AND s.char_candidate=0
        AND NOT EXISTS (SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0)''', BID)
    print('values with NO resolution state (ungrounded):', g3a)
    print('over-calls (char role, not seeded, no discovery):', g3b)

    # ---- G4 distinctions ----
    hdr('G4 distinctions preserved  PASS=0 rows')
    g4 = q('''WITH shape AS (
        SELECT s.id span_id, s.primary_strong,
          group_concat(l.ve_nr||':'||COALESCE(l.value,'')||':'||COALESCE(l.resolution,''),'|') sig
        FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        JOIN ve_lexical l ON l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0
        WHERE v.book_id=? AND s.char_candidate=1 GROUP BY s.id)
      SELECT primary_strong, COUNT(*) occ, COUNT(DISTINCT sig) shapes
      FROM shape GROUP BY primary_strong HAVING COUNT(*)>=5 AND COUNT(DISTINCT sig)=1 ORDER BY occ DESC''', BID)
    print('recurring terms (>=5x) reading identically:', len(g4))
    for r in g4[:15]: print(f'   {r["primary_strong"]:10} occ={r["occ"]} shapes={r["shapes"]}')

    # ---- G5 belonging ----
    hdr('G5 belonging honoured  PASS=0 rows (audit each)')
    g5 = q('''SELECT su.unit_code, COUNT(DISTINCT suv.verse_id) verses
        FROM segment_unit su JOIN segment_unit_verse suv ON suv.unit_id=su.id
        WHERE su.book='Pro' AND COALESCE(su.delete_flagged,0)=0 AND su.unit_type IN ('D','T')
        GROUP BY su.unit_code HAVING COUNT(DISTINCT suv.verse_id)>=3
          AND NOT EXISTS (
            SELECT 1 FROM ve_lexical l
            JOIN verse_span_index a ON a.id=l.from_span
            JOIN verse_span_index b ON b.id=l.to_span
            WHERE a.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
              AND b.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
              AND a.verse_id<>b.verse_id AND COALESCE(l.delete_flagged,0)=0)''')
    print('cohesive multi-verse units with NO cross-verse link:', len(g5))
    for r in g5[:20]: print(f'   {r["unit_code"]:22} verses={r["verses"]}')

    # ---- G6 discovery ----
    hdr('G6 unexpected surfaced  PASS=0')
    g6 = one('''SELECT COUNT(DISTINCT v.id) FROM verse v
        WHERE v.book_id=? AND EXISTS (SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1)
        AND NOT EXISTS (SELECT 1 FROM verse_span_index s JOIN ve_lexical l ON l.verse_span_id=s.id
           WHERE s.verse_id=v.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0)''', BID)
    print('candidate verses with NO discovery(114) entry:', g6)

    # ---- G7 honest uncertainty ----
    hdr('G7 honest uncertainty  PASS=0')
    g7 = one('''SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND COALESCE(l.delete_flagged,0)=0
        AND l.value IS NULL AND (l.resolution IS NULL OR l.resolution NOT IN ('none','unknown','inferred','span'))''', BID)
    print('silent blanks (value null, no explicit resolution):', g7)

    # ---- G8 baseline characteristic count (the number to preserve/beat) ----
    hdr('G8 baseline scale (informational — the before)')
    print('current characteristic-role spans:', one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'", BID))
    print('per chapter (chapter: char-role spans):')
    for r in q("SELECT v.chapter ch, COUNT(*) n FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic' GROUP BY v.chapter ORDER BY v.chapter", BID):
        print(f'   ch{r["ch"]:2}: {r["n"]}')
    c.close()

if __name__ == '__main__':
    main()
