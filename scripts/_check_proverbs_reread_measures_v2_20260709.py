"""Proverbs re-read success measures (G0-G10) — READ-ONLY. v2 (2026-07-09).

Supersedes v1 (`_check_proverbs_reread_measures_v1_20260708.py`), which had a
FALSE-RESULT in G3: it flagged value/event/flag items as "ungrounded" because they
carry no `resolution` (resolution is meaningful only for PAIRs). v2 fixes G3/G4/G7 and
adds G9 (pair & qualifier integrity) and G10 (completeness ledger).

Dimension model (18): 16 per-span ve_nr 101-116 + 2 verse-level (process, genre).
  MANDATORY per-span ledger set M = 101,102,103,104,105,106,107,108,111,112
  OPTIONAL (none-by-default ok)   = 109,110,113,116
  COVERED ELSEWHERE               = 114 discovery (G6), 115 role (G1)
  VERSE-LEVEL                     = process (passage), genre (G0 precondition)
  (201-series is Leviticus-only, out of scope.)

Measures ACTIVE current state (delete_flagged=0, provenance-agnostic) so one script
gives BASELINE now and the AFTER delta post-reread.

Usage: python scripts/_check_proverbs_reread_measures_v2_20260709.py --label baseline
No writes.
"""
import sqlite3, os, argparse

DB = os.path.join('database', 'bible_research.db')
BID = 20
BUDGET = 12
MANDATORY = (101, 102, 103, 104, 105, 106, 107, 108, 111, 112)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--label', default='baseline')
    args = ap.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    q = lambda s, *a: c.execute(s, a).fetchall()
    one = lambda s, *a: c.execute(s, a).fetchone()[0]
    def hdr(t): print('\n### ' + t)
    print(f"# Proverbs re-read measures v2 - label={args.label}")

    hdr('STRUCTURE')
    print('verses:', one('SELECT COUNT(*) FROM verse WHERE book_id=?', BID))
    print('candidate char-spans:', one('SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1', BID),
          '| candidate verses:', one('SELECT COUNT(DISTINCT s.verse_id) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1', BID))
    print('per-span ve_nr present in Pro:',
          [r[0] for r in q('SELECT DISTINCT l.ve_nr FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND l.ve_nr BETWEEN 101 AND 116 AND COALESCE(l.delete_flagged,0)=0 ORDER BY l.ve_nr', BID)])

    # G0
    hdr('G0 digestion budget (units > %d char-spans)  PASS=0' % BUDGET)
    over = q('''SELECT su.unit_code, COUNT(*) cs FROM segment_unit su
        JOIN segment_unit_verse suv ON suv.unit_id=su.id
        JOIN verse_span_index s ON s.verse_id=suv.verse_id AND s.char_candidate=1
        WHERE su.book='Pro' AND COALESCE(su.delete_flagged,0)=0
        GROUP BY su.unit_code HAVING COUNT(*)>? ORDER BY cs DESC''', BUDGET)
    print('units over budget:', len(over), '| worst:', [(r['unit_code'], r['cs']) for r in over[:6]])

    # G1
    hdr('G1 nothing passed over  PASS=0/0')
    print('candidate spans role NULL:', one('SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.char_candidate=1 AND s.role IS NULL', BID))
    print('char-verses not processed:', one("SELECT COUNT(DISTINCT v.id) FROM verse v WHERE v.book_id=? AND EXISTS(SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1) AND v.process_marker IS NULL", BID))

    # G2
    hdr('G2 worked, not named  PASS=0/0')
    print('char spans NO lexical:', one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'
        AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0)''', BID))
    print('char spans NO operation(106):', one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'
        AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=106 AND COALESCE(l.delete_flagged,0)=0)''', BID))

    # G3 (REFINED: grounding applies to PAIRS only)
    hdr('G3 read from the verse  PASS=0/0  [v2: pairs-only grounding]')
    print('PAIR items with no resolution (ungrounded pairs):', one('''SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND l.pair_kind='pair' AND l.resolution IS NULL AND COALESCE(l.delete_flagged,0)=0''', BID))
    print('over-calls (char role, not seeded, no discovery):', one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND s.role='characteristic' AND s.char_candidate=0
        AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0)''', BID))

    # G4 (REFINED: content-item sig only, exclude pairs so span-ids don't distort)
    hdr('G4 distinctions preserved  PASS=0 rows  [v2: content items only]')
    g4 = q('''WITH shape AS (
        SELECT s.id span_id, s.primary_strong,
          group_concat(l.ve_nr||':'||COALESCE(l.value,''),'|') sig
        FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        JOIN ve_lexical l ON l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0
             AND l.pair_kind IN ('value','event','flag')
        WHERE v.book_id=? AND s.char_candidate=1 GROUP BY s.id)
      SELECT primary_strong, COUNT(*) occ, COUNT(DISTINCT sig) shapes
      FROM shape GROUP BY primary_strong HAVING COUNT(*)>=5 AND COUNT(DISTINCT sig)=1 ORDER BY occ DESC''', BID)
    print('recurring terms (>=5x) reading identically:', len(g4), '| e.g.', [(r['primary_strong'], r['occ']) for r in g4[:6]])

    # detect pair-endpoint encoding: integer span-ids (new model) vs Strong's strings (old model)
    sample = q("SELECT from_span FROM ve_lexical WHERE pair_kind='pair' AND from_span IS NOT NULL AND COALESCE(delete_flagged,0)=0 LIMIT 200")
    SPANIDS = any(str(r['from_span']).isdigit() for r in sample)
    print('\n[pair-endpoint encoding: %s]' % ('span-ids (new model)' if SPANIDS else "Strong's strings (OLD model) - G5/G9a/G9c N/A until re-read writes span-ids"))

    # G5
    hdr('G5 belonging honoured  PASS=0 rows (audit each)')
    if not SPANIDS:
        print("N/A on baseline - pair endpoints are Strong's-encoded, not span-ids; gate valid after re-read")
    else:
        g5 = q('''SELECT su.unit_code, COUNT(DISTINCT suv.verse_id) verses FROM segment_unit su
            JOIN segment_unit_verse suv ON suv.unit_id=su.id
            WHERE su.book='Pro' AND COALESCE(su.delete_flagged,0)=0 AND su.unit_type IN ('D','T')
            GROUP BY su.unit_code HAVING COUNT(DISTINCT suv.verse_id)>=3
              AND NOT EXISTS(SELECT 1 FROM ve_lexical l
                JOIN verse_span_index a ON a.id=l.from_span JOIN verse_span_index b ON b.id=l.to_span
                WHERE a.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
                  AND b.verse_id IN (SELECT verse_id FROM segment_unit_verse WHERE unit_id=su.id)
                  AND a.verse_id<>b.verse_id AND l.pair_kind='pair' AND COALESCE(l.delete_flagged,0)=0)''')
        print('cohesive multi-verse units with NO cross-verse link:', len(g5))

    # G6
    hdr('G6 unexpected surfaced  PASS=0')
    print('candidate verses NO discovery(114):', one('''SELECT COUNT(DISTINCT v.id) FROM verse v WHERE v.book_id=?
        AND EXISTS(SELECT 1 FROM verse_span_index s WHERE s.verse_id=v.id AND s.char_candidate=1)
        AND NOT EXISTS(SELECT 1 FROM verse_span_index s JOIN ve_lexical l ON l.verse_span_id=s.id
           WHERE s.verse_id=v.id AND l.ve_nr=114 AND COALESCE(l.delete_flagged,0)=0)''', BID))

    # G7 (REFINED: content items with a null value = blank; pairs handled by G9)
    hdr('G7 honest uncertainty  PASS=0  [v2: content items only]')
    print('content items (value/event/flag) with NULL value:', one('''SELECT COUNT(*) FROM ve_lexical l
        JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND l.pair_kind IN ('value','event','flag') AND COALESCE(l.delete_flagged,0)=0 AND (l.value IS NULL OR l.value='')''', BID))

    # G9 pair & qualifier integrity
    hdr('G9 pair & qualifier integrity  PASS=0/0/0')
    print('(b) malformed pairs (endpoint/resolution missing):', one('''SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND l.pair_kind='pair' AND COALESCE(l.delete_flagged,0)=0 AND (l.from_span IS NULL OR l.to_span IS NULL OR l.resolution IS NULL)''', BID))
    if not SPANIDS:
        print("(a) orphan qualifiers: N/A on baseline (Strong's-encoded endpoints)")
        print("(c) dangling endpoints: N/A on baseline (Strong's-encoded endpoints)")
    else:
        c.execute('''CREATE TEMP TABLE _pairends AS
            SELECT from_span AS sid FROM ve_lexical WHERE pair_kind='pair' AND from_span IS NOT NULL AND COALESCE(delete_flagged,0)=0
            UNION SELECT to_span FROM ve_lexical WHERE pair_kind='pair' AND to_span IS NOT NULL AND COALESCE(delete_flagged,0)=0''')
        c.execute('CREATE INDEX _pe_idx ON _pairends(sid)')
        print('(a) orphan qualifiers (bound to no pair):', one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
            WHERE v.book_id=? AND s.role IN ('qualifier','process-qualifier') AND s.id NOT IN (SELECT sid FROM _pairends)''', BID))
        print('(c) dangling endpoints (endpoint span not in Proverbs):', one('''SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
            WHERE v.book_id=? AND l.pair_kind='pair' AND COALESCE(l.delete_flagged,0)=0 AND l.to_span IS NOT NULL
            AND NOT EXISTS(SELECT 1 FROM verse_span_index x JOIN verse vv ON vv.id=x.verse_id WHERE x.id=l.to_span AND vv.book_id=?)''', BID, BID))

    # G10 completeness ledger
    hdr('G10 completeness ledger (chars missing an explicit MANDATORY dim)  PASS=0')
    nchar = one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'", BID)
    print('characteristic spans:', nchar, '| mandatory set M =', MANDATORY)
    for d in MANDATORY:
        miss = one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'
            AND NOT EXISTS(SELECT 1 FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.ve_nr=? AND COALESCE(l.delete_flagged,0)=0)''', BID, d)
        print(f'   dim {d}: {miss} chars with NO explicit entry')
    inlist = ','.join(str(d) for d in MANDATORY)
    anymiss = one('''SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND s.role='characteristic'
        AND (SELECT COUNT(DISTINCT l.ve_nr) FROM ve_lexical l
             WHERE l.verse_span_id=s.id AND l.ve_nr IN (%s) AND COALESCE(l.delete_flagged,0)=0) < %d''' % (inlist, len(MANDATORY)), BID)
    print('TOTAL chars missing >=1 mandatory dim:', anymiss, '(PASS=0)')
    c.close()

if __name__ == '__main__':
    main()
