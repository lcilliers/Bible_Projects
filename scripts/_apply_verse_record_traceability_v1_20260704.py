"""Add analysis-traceability columns to wa_verse_records (the primary control table).

Researcher (2026-07-04): the verse-record must carry (i) an explicit analysis marker and
(ii) a link to the passage/unit the verse was incorporated in. Both were skipped; analysis
state lived only on verse.process_marker. This adds them, back-filled from the live stores.

Additive + non-destructive: two nullable TEXT columns; a covering index; no existing data changed.
Idempotent: skips columns/index that already exist; re-running refreshes the backfill values.

  analysis_marker  <- verse.process_marker (via verse_id)   e.g. 'Job-1-poetic-lexical-20260703'
  incorporated_in  <- the segment_unit unit_code(s) covering the verse (comma-joined),
                      or 'chapter-driven' for a Phase-1 verse in a book with no segment layer (Psalms),
                      or NULL if not analysed.

Scope: back-fills the 5 wisdom books by default (others left NULL); --all-books to do every book.

Usage:
  python scripts/_apply_verse_record_traceability_v1_20260704.py            # dry-run (report only)
  python scripts/_apply_verse_record_traceability_v1_20260704.py --live
  python scripts/_apply_verse_record_traceability_v1_20260704.py --live --all-books
"""
import sqlite3, os, sys
from collections import defaultdict

DB = os.path.join('database', 'bible_research.db')
WISDOM = (18, 19, 20, 21, 25)

def main():
    LIVE = '--live' in sys.argv
    ALLB = '--all-books' in sys.argv
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; cur = conn.cursor()

    cols = [d[1] for d in cur.execute("PRAGMA table_info(wa_verse_records)").fetchall()]
    to_add = [c for c in ('analysis_marker', 'incorporated_in') if c not in cols]
    print(f"columns to add: {to_add or '(already present)'}")

    # book scope
    if ALLB:
        book_ids = [r[0] for r in cur.execute("SELECT DISTINCT book_id FROM verse WHERE process_marker IS NOT NULL")]
    else:
        book_ids = list(WISDOM)
    ph = ",".join("?" * len(book_ids))

    # build lookups (in-memory; verse_span_index is unindexed but we don't need it here)
    marker = {}   # verse_id -> process_marker
    for r in cur.execute(f"SELECT id, process_marker FROM verse WHERE book_id IN ({ph}) AND process_marker IS NOT NULL", book_ids):
        marker[r['id']] = r['process_marker']
    units = defaultdict(list)  # verse_id -> [unit_code]
    for r in cur.execute("""SELECT suv.verse_id vid, su.unit_code uc FROM segment_unit_verse suv
                            JOIN segment_unit su ON su.id=suv.unit_id AND COALESCE(su.delete_flagged,0)=0"""):
        units[r['vid']].append(r['uc'])
    incorporated = {}
    for vid, mk in marker.items():
        if vid in units:
            incorporated[vid] = ",".join(sorted(set(units[vid])))
        else:
            incorporated[vid] = 'chapter-driven'   # analysed but no segment layer (Psalms)

    # rows to update
    rows = cur.execute(f"""SELECT id, verse_id FROM wa_verse_records
                           WHERE book_id IN ({ph}) AND COALESCE(delete_flagged,0)=0 AND verse_id IS NOT NULL""", book_ids).fetchall()
    n_marker = sum(1 for r in rows if r['verse_id'] in marker)
    n_unit = sum(1 for r in rows if incorporated.get(r['verse_id'], '') not in ('', 'chapter-driven'))
    n_chap = sum(1 for r in rows if incorporated.get(r['verse_id']) == 'chapter-driven')
    print(f"scope: {len(book_ids)} book(s); {len(rows)} verse-record rows")
    print(f"  will set analysis_marker on {n_marker} rows")
    print(f"  incorporated_in: {n_unit} unit-linked · {n_chap} chapter-driven (Psalms)")

    if not LIVE:
        print("DRY-RUN. Re-run with --live.")
        return

    for col in to_add:
        cur.execute(f"ALTER TABLE wa_verse_records ADD COLUMN {col} TEXT")
        print(f"  added column {col}")
    # covering index for the verse-record -> verse traceability join
    cur.execute("CREATE INDEX IF NOT EXISTS ix_wavr_verse_marker ON wa_verse_records(verse_id, analysis_marker)")

    upd = 0
    for r in rows:
        vid = r['verse_id']
        cur.execute("UPDATE wa_verse_records SET analysis_marker=?, incorporated_in=? WHERE id=?",
                    (marker.get(vid), incorporated.get(vid), r['id']))
        upd += 1
    conn.commit()
    print(f"updated {upd} verse-record rows. committed.")

    # verify
    v = cur.execute(f"""SELECT COUNT(*) tot,
        SUM(CASE WHEN analysis_marker IS NOT NULL THEN 1 ELSE 0 END) m,
        SUM(CASE WHEN incorporated_in IS NOT NULL THEN 1 ELSE 0 END) i
        FROM wa_verse_records WHERE book_id IN ({ph}) AND COALESCE(delete_flagged,0)=0 AND verse_id IS NOT NULL""", book_ids).fetchone()
    print(f"verify (scope): {v['tot']} rows, analysis_marker set on {v['m']}, incorporated_in set on {v['i']}")

if __name__ == '__main__':
    main()
