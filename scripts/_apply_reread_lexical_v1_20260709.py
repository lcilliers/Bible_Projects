"""Apply a char-driven re-read lexical JSON to ve_lexical. REUSABLE per chapter/book.

Reads a reading JSON (see verse-analysis/<book>/_read/*.json): per characteristic span, a full
re-read ledger with SPAN-ID pair endpoints, explicit `none`, discovery. For each listed span it
SOFT-DELETES the span's prior active ve_lexical rows (the old Strong's-encoded / shallow lexical)
and inserts the new ledger with source_provenance from the JSON. Sets verse.process_marker for the
chapter's verses. Dry-run default; --live writes (backup first unless --no-backup).

Usage:
  python scripts/_apply_reread_lexical_v1_20260709.py --in verse-analysis/psalms/_read/psalm-004-reread-v1.json
  python scripts/_apply_reread_lexical_v1_20260709.py --in <json> --live
"""
import sqlite3, os, sys, json, shutil
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')
def arg(name, d=None):
    for a in sys.argv[1:]:
        if a.startswith('--%s=' % name): return a.split('=', 1)[1]
    return d
LIVE = '--live' in sys.argv
NO_BACKUP = '--no-backup' in sys.argv
INP = arg('in')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
KMAP = {'value': 'value', 'pair': 'pair', 'event': 'event', 'note': 'note', 'flag': 'flag'}

def main():
    if not INP or not os.path.isfile(INP):
        print('ERROR: --in <reading.json> required'); sys.exit(1)
    R = json.load(open(INP, encoding='utf-8'))
    bid = R['book_id']; chap = R['chapter']; prov = R['provenance']
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    # chapter verse ids
    vids = [r['id'] for r in c.execute('SELECT id FROM verse WHERE book_id=? AND chapter=?', (bid, chap))]
    spans = R['spans']
    print(f"# reread-lexical apply | {R.get('book')} ch{chap} | prov={prov} | {'LIVE' if LIVE else 'DRY-RUN'}")
    print(f"chapter verses: {len(vids)} | characteristic spans in JSON: {len(spans)}")
    # validate span ids exist + are in this chapter
    bad = []
    vcid = {}
    for sid in spans:
        row = c.execute('SELECT s.id, s.verse_id, (SELECT verse_context_id FROM ve_lexical l WHERE l.verse_span_id=s.id AND l.verse_context_id IS NOT NULL LIMIT 1) vc FROM verse_span_index s WHERE s.id=?', (int(sid),)).fetchone()
        if not row or row['verse_id'] not in vids: bad.append(sid); continue
        vcid[sid] = row['vc']
    if bad:
        print('ERROR: span ids not in this chapter:', bad); sys.exit(1)
    # plan
    tot_del = tot_ins = tot_pairs_spanid = 0
    for sid, obj in spans.items():
        old = c.execute('SELECT COUNT(*) FROM ve_lexical WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0', (int(sid),)).fetchone()[0]
        dims = obj['dims']
        pairs_spanid = sum(1 for d in dims if d.get('k') == 'pair' and (d.get('from') or d.get('to')) and d.get('res') != 'none')
        tot_del += old; tot_ins += len(dims); tot_pairs_spanid += pairs_spanid
    print(f"would SOFT-DELETE {tot_del} prior active rows; INSERT {tot_ins} new rows ({tot_pairs_spanid} span-id pairs); mark {len(vids)} verses process_marker={prov}")
    if not LIVE:
        # show a sample
        s0 = next(iter(spans)); print(f"\nsample span {s0} ({spans[s0]['gloss']}):")
        for d in spans[s0]['dims']:
            fr = d.get('from'); to = d.get('to'); res = d.get('res', '')
            print(f"   {d['n']} {d['l']:11} [{KMAP[d['k']]}] {str(d.get('v'))[:40]:40} {fr or ''}->{to or ''} {res}")
        print('\nDRY-RUN only. Re-run with --live to apply.'); c.close(); return
    # backup
    if not NO_BACKUP:
        os.makedirs('backups', exist_ok=True)
        bpath = os.path.join('backups', 'bible_research_prereread_%s_ch%d_%s.db' % (R.get('book'), chap, datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')))
        shutil.copy2(DB, bpath); print('backup:', bpath)
    cur = c.cursor()
    pre = cur.execute('SELECT COUNT(*) FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0').fetchone()[0]
    for sid, obj in spans.items():
        cur.execute('UPDATE ve_lexical SET delete_flagged=1 WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0', (int(sid),))
        for d in obj['dims']:
            cur.execute('''INSERT INTO ve_lexical (verse_context_id, verse_span_id, ve_nr, ve_label, value,
                 source_provenance, delete_flagged, created_at, from_span, to_span, resolution, pair_kind)
                 VALUES (?,?,?,?,?,?,0,?,?,?,?,?)''',
                (vcid.get(sid), int(sid), d['n'], d['l'], d.get('v'), prov, NOW,
                 d.get('from'), d.get('to'), d.get('res'), KMAP[d['k']]))
    # mark process_marker only on the verses actually read (the spans in this JSON) — supports partial-chapter (stanza) applies
    marked = sorted({c.execute('SELECT verse_id FROM verse_span_index WHERE id=?', (int(sid),)).fetchone()[0] for sid in spans})
    cur.executemany('UPDATE verse SET process_marker=? WHERE id=?', [(prov, v) for v in marked])
    print(f"process_marker set on {len(marked)} verse(s) actually read")
    c.commit()
    post = cur.execute('SELECT COUNT(*) FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0').fetchone()[0]
    print(f"applied. active ve_lexical {pre} -> {post} (net {post-pre}). committed.")
    c.close()

if __name__ == '__main__':
    main()
