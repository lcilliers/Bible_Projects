"""Psalms re-read progress monitor — READ-ONLY. Run anytime to see how far the re-read has got.

Reports: chapters done, characteristics re-read (provenance reread-psalms-2026), % complete,
and a quick gate summary. No DB writes.

Usage: python scripts/_check_psalms_reread_progress_v1_20260709.py
"""
import sqlite3, os
DB = os.path.join('database', 'bible_research.db')
PROV = 'reread-psalms-2026'
BID = 19

def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    one = lambda s, *a: c.execute(s, a).fetchone()[0]
    tot_ch = one("SELECT COUNT(DISTINCT chapter) FROM verse WHERE book_id=?", BID)
    tot_char = one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND s.role='characteristic'", BID)
    reread_char = one(f"""SELECT COUNT(DISTINCT s.id) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        JOIN ve_lexical l ON l.verse_span_id=s.id
        WHERE v.book_id=? AND s.role='characteristic' AND l.source_provenance=? AND COALESCE(l.delete_flagged,0)=0""", BID, PROV)
    # chapters where every characteristic has been re-read
    done_ch = []
    for r in c.execute("SELECT DISTINCT chapter FROM verse WHERE book_id=? ORDER BY chapter", (BID,)):
        ch = r['chapter']
        nch = one("SELECT COUNT(*) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND v.chapter=? AND s.role='characteristic'", BID, ch)
        if nch == 0:
            continue
        ndone = one(f"""SELECT COUNT(DISTINCT s.id) FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
            JOIN ve_lexical l ON l.verse_span_id=s.id
            WHERE v.book_id=? AND v.chapter=? AND s.role='characteristic' AND l.source_provenance=? AND COALESCE(l.delete_flagged,0)=0""", BID, ch, PROV)
        if ndone == nch:
            done_ch.append(ch)
    span_pairs = one(f"""SELECT COUNT(*) FROM ve_lexical l JOIN verse_span_index s ON s.id=l.verse_span_id JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND l.source_provenance=? AND l.pair_kind='pair' AND l.resolution!='none' AND COALESCE(l.delete_flagged,0)=0""", BID, PROV)
    print("=== Psalms re-read progress ===")
    print(f"chapters done (all chars re-read): {len(done_ch)} / {tot_ch}   {done_ch if done_ch else ''}")
    print(f"characteristics re-read: {reread_char} / {tot_char}  ({100*reread_char/tot_char:.1f}%)")
    print(f"span-id pairs written (new model): {span_pairs}")
    print("\nmonitor commands:")
    print("  git log --oneline | grep -i psalm         # per-chapter commits")
    print("  python scripts/_check_reread_measures_v3_20260709.py --book Psalms   # live gate state")
    print("  python scripts/_check_psalms_reread_progress_v1_20260709.py          # this report")
    c.close()

if __name__ == '__main__':
    main()
