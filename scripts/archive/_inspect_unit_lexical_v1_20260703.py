"""Read-back inspector: lay a segmentation UNIT's verse text alongside its Phase-1
ve_lexical (roles, characteristics, pairs, flags) so the unit meaning-synthesis can
VALIDATE the lexical buildup, check the pairs for sensibility, and surface hidden
inner-being characteristics.

Read-only. Usage:
  python scripts/_inspect_unit_lexical_v1_20260703.py --unit PRO-01-A
  python scripts/_inspect_unit_lexical_v1_20260703.py --book Pro --chapter 1   (all units in a chapter)
"""
import sqlite3, os, sys

DB = os.path.join('database', 'bible_research.db')

def arg(n, d=None):
    k=f'--{n}'
    if k in sys.argv:
        i=sys.argv.index(k)
        if i+1<len(sys.argv): return sys.argv[i+1]
    return d

def dump_unit(c, u):
    print(f"\n### {u['unit_code']}  [{u['unit_type']}{'*thread' if u['is_thread'] else ''}]  vv. {u['verse_ref_summary']}  multi={u['multi']}")
    print(f"    characteristics(provisional): {u['characteristics']}")
    print(f"    gist: {u['gist']}")
    vs = c.execute("""SELECT suv.verse_id, suv.reference, v.verse_num, v.verse_text
        FROM segment_unit_verse suv JOIN verse v ON v.id=suv.verse_id
        WHERE suv.unit_id=? ORDER BY v.verse_num""", (u['id'],)).fetchall()
    for vr in vs:
        vn=vr['verse_num']; ref=vr['reference']
        txt=(vr['verse_text'] or '').replace(ref,'').strip()
        print(f"  v{vn}: {txt}")
        # spans + lexical for this verse
        rows = c.execute("""SELECT s.surface, s.primary_strong, l.ve_label, l.value, l.from_span, l.to_span, l.pair_kind, l.gate
            FROM verse_span_index s
            JOIN ve_lexical l ON l.verse_span_id=s.id AND COALESCE(l.delete_flagged,0)=0
            WHERE s.verse_id=? ORDER BY s.word_index, l.ve_nr""", (vr['verse_id'],)).fetchall()
        # group by span surface
        bysurf={}
        for r in rows:
            bysurf.setdefault((r['surface'],r['primary_strong']), []).append(r)
        for (surf,strong),items in bysurf.items():
            role=[i['value'] for i in items if i['ve_label']=='role']
            role=role[0] if role else '?'
            feats=[f"{i['ve_label']}={i['value']}" for i in items if i['ve_label'] not in ('role',) and i['value']]
            pairs=[f"{i['ve_label']}:{i['from_span']}->{i['to_span']}({i['pair_kind']})" for i in items if i['pair_kind']=='pair']
            line=f"      [{role}] {surf} {strong}"
            if feats: line+="  | "+"; ".join(feats[:8])
            if pairs: line+="  | PAIRS: "+"; ".join(pairs)
            print(line)

def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    unit=arg('unit'); book=arg('book'); ch=arg('chapter')
    if unit:
        u=c.execute("SELECT * FROM segment_unit WHERE unit_code=? AND COALESCE(delete_flagged,0)=0",(unit,)).fetchone()
        if u: dump_unit(c,u)
        else: print("unit not found")
    elif book and ch:
        us=c.execute("SELECT * FROM segment_unit WHERE book=? AND chapter=? AND COALESCE(delete_flagged,0)=0 ORDER BY id",(book,int(ch))).fetchall()
        print(f"== {book} {ch}: {len(us)} units ==")
        for u in us: dump_unit(c,u)
    else:
        print("need --unit CODE  or  --book B --chapter N")

if __name__=='__main__':
    main()
