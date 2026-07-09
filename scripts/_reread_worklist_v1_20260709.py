#!/usr/bin/env python
"""
_reread_worklist_v1_20260709.py  --  control table for the isolated-per-chapter re-read loop.

Purpose
-------
Stage the book re-read as discrete, individually-gated chapter units in a control
table, so the per-chapter reading loop can advance WITHOUT a manual trigger between
chapters, while still guaranteeing each chapter is read in isolation (one JSON file,
its own gate check, its own commit).

This is the *scaffolding* only. The reading itself (dimensions / discovery / pair
resolution) is done by the analyst per chapter at full depth -- it is never scripted.

Subcommands
-----------
  --seed   --book Psalms [--prov reread-psalms-2026]
             Create reread_worklist if absent and (re)seed rows for every chapter of
             the book that has characteristic spans. Recomputes status from the DB:
             a chapter is 'done' iff every role=characteristic span has an active
             ve_lexical row under the provenance; else 'pending'. Idempotent.

  --next   --book Psalms [--prov ...] [--claim]
             Print the next pending chapter (lowest number). With --claim, mark it
             in_progress and emit its verse text + characteristic span list (the data
             pull the analyst needs), so the loop does not hand-write the query.

  --close  --book Psalms --chapter N --g10 X --g6 Y [--sha SHA] [--prov ...]
             Write gate results back. status='done' iff g10==0 and g6==0, else
             'needs_review'. Records read_at (caller-supplied timestamp optional).

  --status --book Psalms [--prov ...]
             Report counts (pending / in_progress / done / needs_review) and the next
             few pending chapters. Read-only.

Notes
  * Book-general: pass --book by name (resolved via `books`) or --book-id N.
  * No DB backup taken (control-table writes only; use pre-op snapshot elsewhere).
  * process_marker / ve_lexical are the source of truth; this table is a convenience
    ledger recomputed by --seed, never the authority.
"""
import argparse, sqlite3, os, sys, json

DB = os.path.join('database', 'bible_research.db')

DDL = """
CREATE TABLE IF NOT EXISTS reread_worklist (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  book_id       INTEGER NOT NULL,
  chapter       INTEGER NOT NULL,
  provenance    TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'pending',   -- pending | in_progress | done | needs_review
  char_spans    INTEGER,
  read_spans    INTEGER,
  g10_miss      INTEGER,
  g6_no_disc    INTEGER,
  committed_sha TEXT,
  read_at       TEXT,
  note          TEXT,
  UNIQUE(book_id, chapter, provenance)
);
"""

def conn():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    c.execute(DDL)
    return c

def resolve_book(c, name, book_id):
    if book_id is not None:
        return book_id
    r = c.execute("SELECT id FROM books WHERE lower(name)=lower(?) OR lower(short_code)=lower(?) LIMIT 1", (name, name)).fetchone()
    if not r:
        # fall back: Psalms is 19
        raise SystemExit(f"could not resolve book '{name}' -- pass --book-id")
    return r['id']

def chapter_counts(c, book_id, prov):
    """Return {chapter: (char_spans, read_spans)} for chapters having char spans."""
    rows = c.execute("""
        SELECT v.chapter ch,
               COUNT(DISTINCT s.id) char_spans,
               COUNT(DISTINCT CASE WHEN x.id IS NOT NULL THEN s.id END) read_spans
        FROM verse v
        JOIN verse_span_index s ON s.verse_id=v.id AND s.role='characteristic'
        LEFT JOIN ve_lexical x ON x.verse_span_id=s.id AND x.delete_flagged=0
             AND x.source_provenance=?
        WHERE v.book_id=?
        GROUP BY v.chapter HAVING char_spans>0
        ORDER BY v.chapter""", (prov, book_id)).fetchall()
    return {r['ch']: (r['char_spans'], r['read_spans']) for r in rows}

def cmd_seed(c, book_id, prov):
    counts = chapter_counts(c, book_id, prov)
    seeded = 0
    for ch, (cs, rs) in counts.items():
        derived = 'done' if rs == cs else 'pending'
        row = c.execute("SELECT id,status FROM reread_worklist WHERE book_id=? AND chapter=? AND provenance=?",
                        (book_id, ch, prov)).fetchone()
        if row is None:
            c.execute("""INSERT INTO reread_worklist (book_id,chapter,provenance,status,char_spans,read_spans)
                         VALUES (?,?,?,?,?,?)""", (book_id, ch, prov, derived, cs, rs))
        else:
            # never downgrade a manually-set needs_review; but sync done/pending + counts
            keep = row['status'] if row['status'] == 'needs_review' and derived != 'done' else derived
            c.execute("UPDATE reread_worklist SET status=?, char_spans=?, read_spans=? WHERE id=?",
                      (keep, cs, rs, row['id']))
        seeded += 1
    c.commit()
    d = sum(1 for _, (cs, rs) in counts.items() if rs == cs)
    print(f"seeded/synced {seeded} chapters | done={d} pending={seeded-d} | book_id={book_id} prov={prov}")

def cmd_next(c, book_id, prov, claim):
    r = c.execute("""SELECT chapter FROM reread_worklist
                     WHERE book_id=? AND provenance=? AND status='pending'
                     ORDER BY chapter LIMIT 1""", (book_id, prov)).fetchone()
    if not r:
        print(json.dumps({"next": None, "message": "worklist empty -- all chapters done or in review"}))
        return
    ch = r['chapter']
    if claim:
        c.execute("UPDATE reread_worklist SET status='in_progress' WHERE book_id=? AND chapter=? AND provenance=?",
                  (book_id, ch, prov)); c.commit()
    verses = [dict(x) for x in c.execute(
        "SELECT verse_num, verse_text FROM verse WHERE book_id=? AND chapter=? ORDER BY verse_num", (book_id, ch))]
    chars = [dict(x) for x in c.execute("""
        SELECT v.verse_num vn, s.id, s.surface, s.primary_strong ps, s.morph_code, s.role
        FROM verse_span_index s JOIN verse v ON v.id=s.verse_id
        WHERE v.book_id=? AND v.chapter=? AND (s.role='characteristic' OR s.char_candidate=1)
        ORDER BY v.verse_num, s.word_index""", (book_id, ch))]
    print(json.dumps({"next": ch, "claimed": bool(claim), "verses": verses, "chars": chars}, ensure_ascii=False))

def cmd_close(c, book_id, prov, ch, g10, g6, sha, read_at):
    status = 'done' if (g10 == 0 and g6 == 0) else 'needs_review'
    counts = chapter_counts(c, book_id, prov).get(ch, (None, None))
    c.execute("""UPDATE reread_worklist
                 SET status=?, g10_miss=?, g6_no_disc=?, committed_sha=?, read_at=?, read_spans=?
                 WHERE book_id=? AND chapter=? AND provenance=?""",
              (status, g10, g6, sha, read_at, counts[1], book_id, ch, prov))
    c.commit()
    print(f"chapter {ch} -> {status} (g10={g10} g6={g6} sha={sha or '-'})")

def cmd_status(c, book_id, prov):
    rows = c.execute("""SELECT status, COUNT(*) n FROM reread_worklist
                        WHERE book_id=? AND provenance=? GROUP BY status""", (book_id, prov)).fetchall()
    tally = {r['status']: r['n'] for r in rows}
    total = sum(tally.values())
    nxt = [r['chapter'] for r in c.execute("""SELECT chapter FROM reread_worklist
              WHERE book_id=? AND provenance=? AND status='pending' ORDER BY chapter LIMIT 8""", (book_id, prov))]
    rev = [r['chapter'] for r in c.execute("""SELECT chapter FROM reread_worklist
              WHERE book_id=? AND provenance=? AND status='needs_review' ORDER BY chapter""", (book_id, prov))]
    print(f"book_id={book_id} prov={prov} | total={total} "
          f"done={tally.get('done',0)} pending={tally.get('pending',0)} "
          f"in_progress={tally.get('in_progress',0)} needs_review={tally.get('needs_review',0)}")
    print("next pending:", nxt)
    if rev: print("NEEDS REVIEW:", rev)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', action='store_true')
    ap.add_argument('--next', action='store_true')
    ap.add_argument('--close', action='store_true')
    ap.add_argument('--status', action='store_true')
    ap.add_argument('--book', default='Psalms')
    ap.add_argument('--book-id', type=int, default=None)
    ap.add_argument('--prov', default='reread-psalms-2026')
    ap.add_argument('--claim', action='store_true')
    ap.add_argument('--chapter', type=int)
    ap.add_argument('--g10', type=int)
    ap.add_argument('--g6', type=int)
    ap.add_argument('--sha')
    ap.add_argument('--read-at')
    a = ap.parse_args()
    c = conn()
    bid = resolve_book(c, a.book, a.book_id)
    if a.seed:      cmd_seed(c, bid, a.prov)
    elif a.next:    cmd_next(c, bid, a.prov, a.claim)
    elif a.close:   cmd_close(c, bid, a.prov, a.chapter, a.g10, a.g6, a.sha, a.read_at)
    elif a.status:  cmd_status(c, bid, a.prov)
    else:           ap.print_help()

if __name__ == '__main__':
    main()
