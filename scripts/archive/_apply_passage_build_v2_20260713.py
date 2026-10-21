"""Passage build v2 — candidate-driven, per book (Stage 0 of the cycle).

Implements wa-passage-completeness-rule-v2-20260708.md: a passage = a MAXIMAL RUN of
consecutive candidate-bearing verses (verse_span_index.char_candidate=1) within a chapter.
Non-candidate verses are OUTSIDE every passage (never read). Single-verse passages allowed.
Writes ONLY: passage rows (source='passage-build-2026'), verse.passage_id, verse.is_passage_anchor.
Rebuilds the book cleanly: clears the book's prior passages + verse.passage_id/is_passage_anchor first.

Precondition (integrity invariant): every char_candidate span has an active wa_verse_records
(I2=0). The build asserts this and refuses if violated.

Usage: python scripts/_apply_passage_build_v2_20260713.py --book 20 [--dry-run|--live]
"""
import sqlite3, os, argparse, datetime

DB = os.path.join('database', 'bible_research.db')
SRC = 'passage-build-2026'


import re as _re


def _base(s):
    m = _re.match(r'([HG]\d+)', s or '')
    return m.group(1) if m else None


def candidate_verses(c, book):
    """Per candidate-bearing verse: chapter, verse_num, id, reference, and the SET of
    candidate base-Strong's on it (the chars). Canonical order."""
    rows = c.execute(
        """SELECT v.chapter, v.verse_num, v.id, v.reference, GROUP_CONCAT(si.primary_strong) strs
           FROM verse v JOIN verse_span_index si ON si.verse_id = v.id
           WHERE v.book_id = ? AND si.char_candidate = 1
           GROUP BY v.id ORDER BY v.chapter, v.verse_num""", (book,)).fetchall()
    out = []
    for r in rows:
        d = dict(r)
        d['chars'] = {_base(x) for x in (r['strs'] or '').split(',')} - {None}
        out.append(d)
    return out


def build_runs(rows, rule='char-continuity'):
    """Group candidate verses into passages.

    rule='maximal'        — maximal run of consecutive candidate verses (genre-blind;
                            bundles independent proverbs — use only for discourse/poetry).
    rule='char-continuity'— SEGMENTATION AROUND THE CHARS (researcher 2026-07-13): a run
                            continues only while consecutive verses SHARE >=1 candidate
                            characteristic; when the char focus changes, it breaks. Keeps
                            genuine char-runs (e.g. the 'fool' cluster) together and splits
                            independent proverbs into their own passages. Not thematic."""
    runs = []
    cur = []
    for r in rows:
        if not cur:
            cur = [r]; continue
        prev = cur[-1]
        consec = (r['chapter'] == prev['chapter'] and r['verse_num'] == prev['verse_num'] + 1)
        join = consec and (rule != 'char-continuity' or bool(r.get('chars', set()) & prev.get('chars', set())))
        if join:
            cur.append(r)
        else:
            runs.append(cur); cur = [r]
    if cur:
        runs.append(cur)
    return runs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', type=int, required=True)
    ap.add_argument('--rule', choices=['char-continuity', 'maximal'], default='char-continuity',
                    help="char-continuity (around the chars; default) or maximal (discourse/poetry)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--dry-run', action='store_true')
    g.add_argument('--live', action='store_true')
    a = ap.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row

    # integrity invariant: no candidate span without an active verse-record (I2=0)
    import re
    baseof = lambda s: (re.match(r'([HG]\d+)', s).group(1) if s and re.match(r'([HG]\d+)', s) else None)
    cand = c.execute("""SELECT si.id, v.id vid, si.primary_strong FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                        WHERE v.book_id=? AND si.char_candidate=1""", (a.book,)).fetchall()
    cov = set()
    for r in c.execute("""SELECT wr.verse_id, m.strongs_number FROM wa_verse_records wr LEFT JOIN mti_terms m ON m.id=wr.mti_term_id
                          WHERE wr.book_id=? AND COALESCE(wr.delete_flagged,0)=0""", (a.book,)):
        cov.add((r[0], baseof(r[1])))
    uncov = [r for r in cand if (r['vid'], baseof(r['primary_strong'])) not in cov]
    if uncov:
        print(f"REFUSING: {len(uncov)} candidate spans lack a verse-record (I2 violation). Fix before passage build.")
        return

    rows = candidate_verses(c, a.book)
    runs = build_runs(rows, rule=a.rule)
    print(f"rule = {a.rule}")
    nverses = sum(len(r) for r in runs)
    sizes = [len(r) for r in runs]
    print(f"book {a.book}: {len(rows)} candidate-bearing verses -> {len(runs)} passages "
          f"(verses in passages={nverses}; size min={min(sizes)} max={max(sizes)} "
          f"mean={nverses/len(runs):.1f}; single-verse={sizes.count(1)})")
    big = sorted(runs, key=len, reverse=True)[:6]
    for r in big:
        print(f"   largest: {r[0]['reference']}..{r[-1]['reference']} ({len(r)} verses)")

    if a.dry_run:
        # existing state for comparison
        ex = c.execute("SELECT COUNT(*) FROM passage WHERE book_id=?", (a.book,)).fetchone()[0]
        print(f"\n(dry-run) would REPLACE {ex} existing passages with {len(runs)}. No writes.")
        return

    now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
    cur = c.cursor()
    # clear book's prior passages + verse links
    old_ids = [r[0] for r in cur.execute("SELECT id FROM passage WHERE book_id=?", (a.book,))]
    cur.execute("UPDATE verse SET passage_id=NULL, is_passage_anchor=0 WHERE book_id=?", (a.book,))
    if old_ids:
        cur.execute(f"DELETE FROM passage WHERE book_id=?", (a.book,))
    # insert new passages + set links
    for run in runs:
        a0, aN = run[0], run[-1]
        ref = a0['reference'] if len(run) == 1 else f"{a0['reference']}-{aN['verse_num']}"
        cur.execute(
            "INSERT INTO passage (ref, anchor_verse_id, book_id, start_chapter, start_verse, "
            "end_chapter, end_verse, verse_count, source, created_at) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (ref, a0['id'], a.book, a0['chapter'], a0['verse_num'], aN['chapter'], aN['verse_num'],
             len(run), SRC, now))
        pid = cur.lastrowid
        for r in run:
            cur.execute("UPDATE verse SET passage_id=? WHERE id=?", (pid, r['id']))
        cur.execute("UPDATE verse SET is_passage_anchor=1 WHERE id=?", (a0['id'],))
    c.commit()
    # gate
    nullp = cur.execute("""SELECT COUNT(DISTINCT v.id) FROM verse v JOIN verse_span_index si ON si.verse_id=v.id
                           WHERE v.book_id=? AND si.char_candidate=1 AND v.passage_id IS NULL""", (a.book,)).fetchone()[0]
    noncand = cur.execute("""SELECT COUNT(*) FROM verse v WHERE v.book_id=? AND v.passage_id IS NOT NULL
        AND v.id NOT IN (SELECT verse_id FROM verse_span_index WHERE char_candidate=1)""", (a.book,)).fetchone()[0]
    print(f"\n[LIVE] built {len(runs)} passages (source={SRC}). "
          f"candidate-verses with NULL passage={nullp} (expect 0); non-candidate with passage={noncand} (expect 0).")


if __name__ == '__main__':
    main()
