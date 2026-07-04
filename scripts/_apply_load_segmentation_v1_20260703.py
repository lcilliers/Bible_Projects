"""Load an inner-being SEGMENTATION (units) into the generic segment store.

Book-agnostic (researcher: the segmentation preamble may apply to other books too).
Idempotent per (book, provenance): soft-deletes prior units, re-inserts.

Input JSON:
{
  "book": "Pro", "book_id": 20,
  "provenance": "proverbs-segmentation-v1-20260703",
  "units": [
    {"code":"PRO-01-A","chapter":1,"type":"D","characteristics":"formation of the inner being",
     "multi":true,"is_thread":false,"gist":"the aims of wisdom...","verses":["1-6"]},
    {"code":"PRO-10-speech","chapter":10,"type":"T","characteristics":"speech legibility",
     "multi":true,"is_thread":true,"gist":"...","verses":[11,"13-14","18-20"]}
  ]
}

verses: list of ints and/or "a-b" ranges (verse numbers within the unit's chapter).

Usage: python scripts/_apply_load_segmentation_v1_20260703.py --in PATH.json [--live]
"""
import sqlite3, os, sys, io, json
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')

def arg(n, d=None):
    k = f'--{n}'
    if k in sys.argv:
        i = sys.argv.index(k)
        if i+1 < len(sys.argv): return sys.argv[i+1]
    return d

def expand(verses):
    out = []
    for v in verses:
        if isinstance(v, int): out.append(v)
        elif isinstance(v, str) and '-' in v:
            a, b = v.split('-'); out += list(range(int(a), int(b)+1))
        else: out.append(int(v))
    return out

def expand_refs(verse_refs):
    """Cross-chapter unit support (prophetic oracles). Each entry is 'ch:vn' or 'ch:a-b'
    (range within one chapter). Yields (chapter, verse_num) tuples in order."""
    out = []
    for r in verse_refs:
        ch_s, v_s = str(r).split(':')
        ch = int(ch_s)
        if '-' in v_s:
            a, b = v_s.split('-'); out += [(ch, n) for n in range(int(a), int(b)+1)]
        else:
            out.append((ch, int(v_s)))
    return out

def unit_pairs(u):
    """(anchor_chapter, [(chapter,verse_num),...]) for a unit - supports single-chapter
    (chapter+verses) and cross-chapter (verse_refs) forms."""
    if u.get('verse_refs'):
        pairs = expand_refs(u['verse_refs'])
        anchor = u.get('chapter') or (pairs[0][0] if pairs else None)
        return anchor, pairs
    ch = u['chapter']
    return ch, [(ch, vn) for vn in expand(u['verses'])]

def main():
    src = arg('in'); LIVE = '--live' in sys.argv
    if not src: print("need --in"); return
    spec = json.load(io.open(src, encoding='utf-8'))
    book = spec['book']; bid = spec['book_id']; prov = spec['provenance']
    units = spec['units']
    NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; cur = conn.cursor()
    # resolve verse ids up front + validate
    problems = []
    resolved = []  # (unit, [(verse_id, ref, seq)])
    for u in units:
        anchor, pairs = unit_pairs(u)
        u['_anchor'] = anchor
        vids = []
        for seq, (ch, vn) in enumerate(pairs):
            r = cur.execute("SELECT id, reference FROM verse WHERE book_id=? AND chapter=? AND verse_num=?",
                            (bid, ch, vn)).fetchone()
            if not r: problems.append(f"{u['code']} {book} {ch}:{vn} not found"); continue
            vids.append((r['id'], r['reference'], seq))
        resolved.append((u, vids))
    print(f"units: {len(units)} | verse-links: {sum(len(v) for _,v in resolved)} | unresolved: {len(problems)}")
    for p in problems[:20]: print("  !", p)
    if not LIVE:
        print("DRY-RUN. Re-run with --live."); return
    # idempotent per SECTION: soft-delete prior units only for the CHAPTERS present in this file
    # (so incremental section loads don't clobber other sections of the same book+provenance)
    chs = sorted({u['_anchor'] for u in units})
    qmarks = ",".join("?" for _ in chs)
    cur.execute(f"UPDATE segment_unit SET delete_flagged=1 WHERE book=? AND source_provenance=? AND chapter IN ({qmarks})",
                (book, prov, *chs))
    ins = 0
    for u, vids in resolved:
        cur.execute("""INSERT INTO segment_unit
            (book,chapter,unit_code,unit_type,characteristics,multi,is_thread,gist,verse_ref_summary,source_provenance,delete_flagged,created_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,0,?)""",
            (book, u['_anchor'], u['code'], u['type'], u.get('characteristics',''),
             1 if u.get('multi') else 0, 1 if u.get('is_thread') else 0, u.get('gist',''),
             u.get('ref_summary') or (','.join(str(x) for x in u['verse_refs']) if u.get('verse_refs') else ','.join(str(x) for x in u['verses'])), prov, NOW))
        uid = cur.lastrowid
        for vid, ref, seq in vids:
            cur.execute("INSERT OR REPLACE INTO segment_unit_verse (unit_id,verse_id,reference,seq) VALUES (?,?,?,?)",
                        (uid, vid, ref, seq))
        ins += 1
    conn.commit()
    n = cur.execute("SELECT COUNT(*) k FROM segment_unit WHERE book=? AND source_provenance=? AND COALESCE(delete_flagged,0)=0",(book,prov)).fetchone()['k']
    print(f"loaded {ins} units; active units for {book}/{prov}: {n}")

if __name__ == '__main__':
    main()
