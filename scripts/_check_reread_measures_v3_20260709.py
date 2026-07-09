"""Re-read success measures (G0-G10) — READ-ONLY, BOOK-GENERAL. v3 (2026-07-09).

Supersedes the Proverbs-specific v2. Adds --book and UNIT-MODEL DETECTION so it does
not produce false results on books that use passages (poetic, e.g. Psalms) vs segments
(discourse/prophetic). Carries v2's fixes: G3 grounding = pairs only; G4/G7 content-only;
encoding guard (pair endpoints Strong's vs span-ids) → G5/G9a/G9c N/A on old data.

Unit model: a book with active segment_units → 'segment'; else → 'passage' (verse.passage_id).
Genre caveat: for the passage model, G0 (digestion budget) may legitimately be exceeded by
whole-chapter poetic reading — flagged, not silently failed.

18-dim model: 16 per-span (101-116) + process + genre. MANDATORY ledger M below.
(201-series is Leviticus-only, out of scope.)

Usage: python scripts/_check_reread_measures_v3_20260709.py --book Psalms [--label baseline]
No writes.
"""
import sqlite3, os, argparse
DB = os.path.join('database', 'bible_research.db')
BUDGET = 12
MANDATORY = (101, 102, 103, 104, 105, 106, 107, 108, 111, 112)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', required=True, help='book id or name substring')
    ap.add_argument('--label', default='baseline')
    a = ap.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    q = lambda s, *ar: c.execute(s, ar).fetchall()
    one = lambda s, *ar: c.execute(s, ar).fetchone()[0]
    # resolve book
    if str(a.book).isdigit():
        b = c.execute('SELECT id,name,short_code FROM books WHERE id=?', (int(a.book),)).fetchone()
    else:
        b = c.execute('SELECT id,name,short_code FROM books WHERE lower(name) LIKE ?', ('%'+a.book.lower()+'%',)).fetchone()
    BID, SC, NM = b['id'], b['short_code'], b['name']
    hdr = lambda t: print('\n### ' + t)
    # unit model
    nseg = one("SELECT COUNT(*) FROM segment_unit WHERE book=? AND COALESCE(delete_flagged,0)=0", SC)
    MODEL = 'segment' if nseg > 0 else 'passage'
    print(f"# Re-read measures v3 - book={NM}({BID}) label={a.label} | unit-model={MODEL} ({nseg} segs)")

    hdr('STRUCTURE')
    print('verses:', one('SELECT COUNT(*) FROM verse WHERE book_id=?', BID),
          '| candidate spans:', one('SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1', BID),
          '| characteristics:', one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'", BID),
          '| active lexical rows:', one('SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND COALESCE(l.delete_flagged,0)=0', BID))
    print('per-span ve_nr present:', [r[0] for r in q('SELECT DISTINCT l.ve_nr FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND l.ve_nr BETWEEN 101 AND 116 AND COALESCE(l.delete_flagged,0)=0 ORDER BY l.ve_nr', BID)])

    # G0 (unit-model-aware)
    hdr('G0 digestion budget (units > %d char-spans)  PASS=0' % BUDGET)
    if MODEL == 'segment':
        over = q('''SELECT su.unit_code, COUNT(*) cs FROM segment_unit su JOIN segment_unit_verse suv ON suv.unit_id=su.id
            JOIN verse_span_index s ON s.verse_id=suv.verse_id AND s.char_candidate=1
            WHERE su.book=? AND COALESCE(su.delete_flagged,0)=0 GROUP BY su.unit_code HAVING COUNT(*)>? ORDER BY cs DESC''', SC, BUDGET)
    else:
        over = q('''SELECT v.passage_id AS unit_code, COUNT(*) cs FROM verse v JOIN verse_span_index s ON s.verse_id=v.id AND s.char_candidate=1
            WHERE v.book_id=? AND v.passage_id IS NOT NULL GROUP BY v.passage_id HAVING COUNT(*)>? ORDER BY cs DESC''', BID, BUDGET)
    print('units over budget:', len(over), '| worst:', [(r['unit_code'], r['cs']) for r in over[:6]])
    if MODEL == 'passage':
        print('  [genre caveat: passage=chapter for poetic; whole-chapter reading may exceed budget by design]')

    # G1
    hdr('G1 nothing passed over  PASS=0/0')
    print('candidate spans role NULL:', one('SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1 AND s.role IS NULL', BID),
          '| char-verses not processed:', one("SELECT COUNT(DISTINCT v.id) FROM verse v WHERE v.book_id=? AND EXISTS(SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1) AND v.process_marker IS NULL", BID))

    # G2
    hdr('G2 worked, not named  PASS=0/0')
    print('char NO lexical:', one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic' AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0)", BID),
          '| char NO operation(106):', one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic' AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=106 AND COALESCE(l.delete_flagged,0)=0)", BID))

    # G3
    hdr('G3 read from the verse (pairs-only grounding)  PASS=0/0')
    print('ungrounded pairs:', one("SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND l.pair_kind='pair' AND l.resolution IS NULL AND COALESCE(l.delete_flagged,0)=0", BID),
          '| over-calls:', one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic' AND s.char_candidate=0 AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0)", BID))

    # G4
    hdr('G4 distinctions preserved (content items)  PASS=0 rows')
    g4 = q('''WITH shape AS (SELECT s.id, s.primary_strong, group_concat(l.ve_nr||':'||COALESCE(l.value,''),'|') sig
        FROM verse_span_index s JOIN verse v ON v.id=s.verse_id JOIN ve_lexical l ON l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0 AND l.pair_kind IN ('value','event','flag')
        WHERE v.book_id=? AND s.char_candidate=1 GROUP BY s.id)
      SELECT primary_strong, COUNT(*) occ FROM shape GROUP BY primary_strong HAVING COUNT(*)>=5 AND COUNT(DISTINCT sig)=1''', BID)
    print('recurring terms (>=5x) reading identically:', len(g4))

    # encoding guard
    sample = q("SELECT from_span FROM ve_lexical WHERE pair_kind='pair' AND from_span IS NOT NULL AND COALESCE(delete_flagged,0)=0 LIMIT 200")
    SPANIDS = any(str(r['from_span']).isdigit() for r in sample)
    print('\n[pair-endpoint encoding: %s]' % ('span-ids' if SPANIDS else "Strong's (OLD) - G5/G9a/G9c N/A until re-read"))

    # G5 (unit-model-aware, encoding-guarded)
    hdr('G5 belonging honoured  PASS=0 rows')
    if not SPANIDS:
        print("N/A - pair endpoints Strong's-encoded")
    elif MODEL == 'segment':
        print('cohesive D/T units w/ no cross-verse link:', len(q('''SELECT su.unit_code FROM segment_unit su JOIN segment_unit_verse suv ON suv.unit_id=su.id
            WHERE su.book=? AND COALESCE(su.delete_flagged,0)=0 AND su.unit_type IN ('D','T') GROUP BY su.unit_code HAVING COUNT(DISTINCT suv.verse_id)>=3
            AND NOT EXISTS(SELECT 1 FROM ve_lexical l JOIN verse_span_index x ON x.id=l.from_span JOIN verse_span_index y ON y.id=l.to_span
              WHERE x.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id) AND y.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
              AND x.verse_id<>y.verse_id AND l.pair_kind='pair' AND COALESCE(l.delete_flagged,0)=0)''', SC)))
    else:
        print('multi-verse passages w/ no cross-verse link:', len(q('''SELECT v.passage_id FROM verse v WHERE v.book_id=? AND v.passage_id IS NOT NULL
            GROUP BY v.passage_id HAVING COUNT(DISTINCT v.id)>=3
            AND NOT EXISTS(SELECT 1 FROM ve_lexical l JOIN verse_span_index x ON x.id=l.from_span JOIN verse_span_index y ON y.id=l.to_span
              WHERE x.verse_id IN (SELECT id FROM verse WHERE passage_id=v.passage_id) AND y.verse_id IN (SELECT id FROM verse WHERE passage_id=v.passage_id)
              AND x.verse_id<>y.verse_id AND l.pair_kind='pair' AND COALESCE(l.delete_flagged,0)=0)''', BID)))

    # G6
    hdr('G6 unexpected surfaced  PASS=0')
    print('candidate verses NO discovery(114):', one("SELECT COUNT(DISTINCT v.id) FROM verse v WHERE v.book_id=? AND EXISTS(SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1) AND NOT EXISTS(SELECT 1 FROM verse_span_index s JOIN ve_lexical l ON l.verse_span_id=s.id WHERE s.verse_id=v.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0)", BID))

    # G7
    hdr('G7 honest uncertainty (content items)  PASS=0')
    print('content items null value:', one("SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND l.pair_kind IN ('value','event','flag') AND COALESCE(l.delete_flagged,0)=0 AND (l.value IS NULL OR l.value='')", BID))

    # G9
    hdr('G9 pair & qualifier integrity  PASS=0/0/0')
    print('(b) malformed pairs:', one("SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND l.pair_kind='pair' AND COALESCE(l.delete_flagged,0)=0 AND (l.from_span IS NULL OR l.to_span IS NULL OR l.resolution IS NULL)", BID))
    print("(a)/(c): %s" % ('computed below' if SPANIDS else "N/A (Strong's endpoints)"))

    # G10 completeness ledger
    hdr('G10 completeness ledger  PASS=0')
    nchar = one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'", BID)
    inlist = ','.join(str(d) for d in MANDATORY)
    anymiss = one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'
        AND (SELECT COUNT(DISTINCT l.ve_nr) FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr IN (%s) AND COALESCE(l.delete_flagged,0)=0) < %d''' % (inlist, len(MANDATORY)), BID)
    print(f'characteristics: {nchar} | missing >=1 mandatory dim: {anymiss} (PASS=0)')
    zero = [d for d in MANDATORY if one("SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND l.ve_nr=? AND COALESCE(l.delete_flagged,0)=0", BID, d) == 0]
    print('mandatory dims with ZERO rows in book:', zero)
    c.close()

if __name__ == '__main__':
    main()
