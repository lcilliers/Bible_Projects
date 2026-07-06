"""Master-index -> wa_verse_records backfill (per book).

The role/span layer (verse_span_index) is built from the FULL Hebrew text and is complete;
the verse-record layer (STEP-derived) is not. This backfills fully-scaffolded verse-records
from the master index for every registered OWNER term occurrence that lacks one — closing the
"book-reading added zero verse-records" gap with the AUTHORITATIVE source (not STEP, not the
rejected bypass: these carry term_inv_id + word_registry_fk + mti_term_id + verse_span_id).

v1 handles the UNAMBIGUOUS tier (base strong -> exactly one active OWNER term). Spans whose
strong maps to multiple OWNER sub-entries (sense-ambiguous) or to no active OWNER are logged
for a second pass, not written.

Usage:
  python scripts/_apply_master_index_backfill_v1_20260706.py --book 19 [--dry-run|--live] [--limit N]
"""
import sqlite3, argparse, json, os
from datetime import datetime, timezone

DB='database/bible_research.db'
NOTE='master-index-backfill-2026'

def base(s): return s[:-1] if (s and len(s)>1 and s[-1].isalpha() and s[0] in 'HG') else s

def ctx(verse_text, surface):
    # strip leading "Ref c:v " then split around surface
    if not verse_text: return '',''
    body=verse_text
    # drop a leading reference token like 'Psa 1:1 '
    parts=body.split(' ',2)
    if len(parts)==3 and ':' in parts[1]: body=parts[2]
    if surface and surface in body:
        i=body.find(surface)
        before=' '.join(body[:i].split()[-5:])
        after=' '.join(body[i+len(surface):].split()[:5])
        return before, after
    return '',''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--book',type=int,required=True)
    g=ap.add_mutually_exclusive_group(required=True); g.add_argument('--dry-run',action='store_true'); g.add_argument('--live',action='store_true')
    ap.add_argument('--limit',type=int)
    ap.add_argument('--with-ambiguous',action='store_true',
                    help='resolve multi-OWNER-sub-entry bases to the dominant sense (most existing verse-records)')
    a=ap.parse_args()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # OWNER resolution: base -> list of owner dicts
    owners={}
    for r in c.execute('''SELECT mt.id mti_id, mt.strongs_number, mt.transliteration, mt.owning_registry_fk reg_fk,
        ti.id inv_id, ti.file_id
      FROM mti_terms mt JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
        AND ti.term_owner_type='OWNER' AND COALESCE(ti.delete_flagged,0)=0
      WHERE COALESCE(mt.delete_flagged,0)=0'''):
        owners.setdefault(base(r['strongs_number']),[]).append(dict(r))

    # dominant-sense picker for ambiguous bases: OWNER sub-entry with most existing active verse-records
    def dominant(cands):
        best=None; bestn=-1
        for o in cands:
            n=c.execute("SELECT COUNT(*) FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",(o['mti_id'],)).fetchone()[0]
            if n>bestn or (n==bestn and o['strongs_number']<best['strongs_number']):
                best=o; bestn=n
        return best

    have=set()
    for r in c.execute('SELECT verse_id, term_id FROM wa_verse_records WHERE book_id=? AND COALESCE(delete_flagged,0)=0',(a.book,)):
        have.add((r['verse_id'], base(r['term_id'])))

    spans=c.execute('''SELECT vsi.id span_id, vsi.verse_id, vsi.reference, vsi.surface, vsi.morph_code, vsi.stem,
        vsi.primary_strong, v.chapter, v.verse_num, v.verse_text, v.testament
      FROM verse_span_index vsi JOIN verse v ON v.id=vsi.verse_id WHERE v.book_id=?''',(a.book,)).fetchall()

    to_write=[]; amb=noown=already=0
    for sp in spans:
        b=base(sp['primary_strong'])
        if (sp['verse_id'], b) in have: already+=1; continue
        o=owners.get(b)
        if not o: noown+=1; continue
        if len(o)>1:
            if not a.with_ambiguous: amb+=1; continue
            ow=dominant(o)
        else:
            ow=o[0]
        before,after=ctx(sp['verse_text'], sp['surface'])
        to_write.append((sp,ow,before,after))
        have.add((sp['verse_id'],b))  # dedupe within this run (multiple spans same verse+strong)
        if a.limit and len(to_write)>=a.limit: break

    print(f'book {a.book}: spans={len(spans)} already_covered={already} '
          f'ambiguous(skip)={amb} no_owner(skip)={noown}  TO_BACKFILL={len(to_write)}')

    if a.dry_run:
        for sp,ow,b,af in to_write[:5]:
            print("  would write: %-12s %s -> mti%s inv%s reg%s span%s" % (
                sp['reference'], sp['primary_strong'], ow['mti_id'], ow['inv_id'], ow['reg_fk'], sp['span_id']))
        print('  (dry-run, no writes)')
        return

    cur=c.cursor(); n=0
    for sp,ow,before,after in to_write:
        cur.execute('''INSERT INTO wa_verse_records
            (file_id, term_inv_id, term_id, transliteration, testament, reference, verse_text,
             book_id, chapter, verse_num, translation, note, target_word, span_strong_match,
             context_before, context_after, delete_flagged, mti_term_id, morph_code, stem,
             word_registry_fk, verse_id, verse_span_id, created_at, last_changed)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0,?,?,?,?,?,?,?,?)''',
            (ow['file_id'], ow['inv_id'], sp['primary_strong'], ow['transliteration'], sp['testament'],
             sp['reference'], sp['verse_text'], a.book, sp['chapter'], sp['verse_num'], 'ESV', NOTE,
             sp['surface'], 1, before, after, ow['mti_id'], sp['morph_code'], sp['stem'],
             ow['reg_fk'], sp['verse_id'], sp['span_id'], now, now))
        n+=1
    c.commit()
    print(f'  wrote {n} verse-records (note={NOTE!r})')

if __name__=='__main__':
    main()
