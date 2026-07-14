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
    # role write-back accumulators (§7A row 2): role from ve_nr=115; qualifiers derived from span-id pair endpoints
    role_of = {}          # span_id(int) -> role string  (from the JSON 115 value)
    role_srcid = {}       # span_id(int) -> ve_lexical id of its 115 row (role_source_ve_id)
    endpoint_ids = set()  # span-ids appearing as the OTHER end of a real span-id pair (=> qualifiers, unless themselves a char)
    for sid, obj in spans.items():
        s = int(sid)
        cur.execute('UPDATE ve_lexical SET delete_flagged=1 WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0', (s,))
        for d in obj['dims']:
            fr = d.get('from'); to = d.get('to'); res = d.get('res')
            # pair_kind derivation: a genuine cross-span PAIR requires res='span' with BOTH
            # endpoints. A relational dim tagged k='pair' but unresolved (res none/inferred) is
            # a FLAG, not a pair - tagging it 'pair' pollutes pair analytics and fails G9b.
            if d['k'] == 'pair':
                if res == 'span':
                    if to is not None and fr is None: fr = s   # owner span is the 'from'
                    if fr is not None and to is None: to = s
                    pk = 'pair'
                else:
                    pk = 'flag'                                 # res in (none, inferred)
            else:
                pk = KMAP[d['k']]
            cur.execute('''INSERT INTO ve_lexical (verse_context_id, verse_span_id, ve_nr, ve_label, value,
                 source_provenance, delete_flagged, created_at, from_span, to_span, resolution, pair_kind)
                 VALUES (?,?,?,?,?,?,0,?,?,?,?,?)''',
                (vcid.get(sid), s, d['n'], d['l'], d.get('v'), prov, NOW,
                 fr, to, res, pk))
            if d['n'] == 115 and d.get('v'):
                role_of[s] = d['v']; role_srcid[s] = cur.lastrowid
                if d['v'] == 'characteristic' and obj.get('gloss'):
                    cur.execute('UPDATE verse_span_index SET characteristic=? WHERE id=?', (obj['gloss'], s))  # I11 char-on-master
            # collect real span-id pair endpoints (res='span') that point at a DIFFERENT span => qualifiers
            if d.get('res') == 'span':
                for ep in (d.get('from'), d.get('to')):
                    if ep and int(ep) != s:
                        endpoint_ids.add(int(ep))
    # derive qualifier roles for endpoints that are not themselves a characteristic/standalone in this JSON
    char_or_standalone = set(role_of.keys())
    for ep in endpoint_ids:
        if ep not in char_or_standalone:
            role_of.setdefault(ep, 'qualifier')
    # write roles to the master (role + provenance + set_at + source_ve_id); read-derived = 'read-2026'
    ROLEPROV = 'read-2026'
    rc = {}
    for s, rl in role_of.items():
        cur.execute('''UPDATE verse_span_index
             SET role=?, role_provenance=?, role_set_at=?, role_source_ve_id=?
             WHERE id=?''', (rl, ROLEPROV, NOW, role_srcid.get(s), s))
        rc[rl] = rc.get(rl, 0) + 1
    print(f"master roles written (read-2026): {rc}")
    # mark process_marker only on the verses actually read (the spans in this JSON) — supports partial-chapter (stanza) applies
    marked = sorted({c.execute('SELECT verse_id FROM verse_span_index WHERE id=?', (int(sid),)).fetchone()[0] for sid in spans})
    cur.executemany('UPDATE verse SET process_marker=? WHERE id=?', [(prov, v) for v in marked])
    print(f"process_marker set on {len(marked)} verse(s) actually read")
    c.commit()
    post = cur.execute('SELECT COUNT(*) FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0').fetchone()[0]
    print(f"applied. active ve_lexical {pre} -> {post} (net {post-pre}). committed.")
    # ★ v2 (Proverbs retrospective) — FLAG leftover old-model chars on the read verses.
    # A span that is role='characteristic' with provenance != 'read-2026' on a verse we just
    # read is a span read-but-not-re-selected. Flag it loudly (do NOT auto-demote: demotion is
    # the explicit book-close 'demote-then-measure' step). Prevents these accumulating unseen.
    if marked:
        qv = ','.join('?' * len(marked))
        emitted = set(int(s) for s in spans)
        leftover = [r for r in c.execute(
            f"""SELECT si.id, si.surface, v.reference FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                WHERE si.verse_id IN ({qv}) AND si.role='characteristic' AND si.role_provenance!='read-2026'""",
            marked) if r[0] not in emitted]
        if leftover:
            print(f"  !! LEFTOVER legacy chars on read verses ({len(leftover)}) — read-but-not-re-selected; "
                  f"demote at book-close (see cadence v2 'demote-then-measure'):")
            for sid, surf, ref in leftover[:20]:
                print(f"     {ref}  [{sid}] {(surf or '')[:22]}")
    c.close()

if __name__ == '__main__':
    main()
