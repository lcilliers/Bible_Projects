#!/usr/bin/env python
"""_apply_psalm_role_reassess_v1_20260706.py — Step 2: re-assess the role dimension for a psalm.

Role is read BY MEANING at chapter scope and recorded on ve_lexical (ve_nr=115). The ordered rule:
  characteristic -> qualifier -> standalone (default). I author, per psalm, the lists of
  CHARACTERISTIC and QUALIFIER strongs (their span-sense role in THIS psalm); every other real-strong
  span defaults to STANDALONE. Optional per-'verse:strong' overrides for context-varying cases.

Writes: for every real-strong span in the psalm, set its ve_lexical ve_nr=115 role value (update the
existing role row, or insert one keyed on the span). Idempotent by (span, ve_nr=115). Provenance stamped
'role-reassess-2026' so the corrective pass is identifiable/reversible.

Input JSON: {"psalm": N, "characteristic": [strongs], "qualifier": [strongs], "overrides": {"v:strong":"role"}}
Read-only unless --live.
"""
import sqlite3, os, sys, json, re
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
def arg(n):
    for a in sys.argv[1:]:
        if a.startswith('--%s='%n): return a.split('=',1)[1]
    return None
JF=arg('json')
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
def base(s): m=re.match(r'(H\d+)', s or ''); return m.group(1) if m else (s or '')

data=json.load(open(JF,encoding='utf-8'))
N=data['psalm']; CH=set(base(s) for s in data.get('characteristic',[])); QU=set(base(s) for s in data.get('qualifier',[]))
OV={k: v for k,v in data.get('overrides',{}).items()}
pb=cur.execute("SELECT id FROM books WHERE name='Psalms'").fetchone()['id']
spans=cur.execute("""SELECT vsi.id sid, v.verse_num vn, vsi.word_index wi, vsi.surface, substr(vsi.primary_strong,1,5) s
  FROM verse_span_index vsi JOIN verse v ON v.id=vsi.verse_id
  WHERE v.book_id=? AND v.chapter=? AND vsi.primary_strong LIKE 'H%' AND vsi.primary_strong NOT LIKE 'H9%'
  ORDER BY v.verse_num, vsi.word_index""",(pb,N)).fetchall()

def role_for(vn, s):
    ov=OV.get(f"{vn}:{s}")
    if ov: return ov
    if s in CH: return 'characteristic'
    if s in QU: return 'qualifier'
    return 'standalone'

from collections import Counter
plan=[]; dist=Counter()
for sp in spans:
    r=role_for(sp['vn'], sp['s']); dist[r]+=1; plan.append((sp['sid'], r, sp['vn'], sp['surface'], sp['s']))
# sanity: authored strongs that don't occur in the psalm
present=set(sp['s'] for sp in spans)
missing_ch=[s for s in CH if s not in present]; missing_qu=[s for s in QU if s not in present]
print(f"Psalm {N}: {len(spans)} real-strong spans | roles: {dict(dist)}")
if missing_ch: print(f"  WARN authored characteristics not in psalm: {missing_ch}")
if missing_qu: print(f"  WARN authored qualifiers not in psalm: {missing_qu}")
if not LIVE:
    print("\nDRY-RUN. Re-run with --live."); sys.exit(0)

NOW='2026-07-06T00:00:00Z'
ins=upd=0
for sid, r, vn, surf, s in plan:
    ex=cur.execute("SELECT id FROM ve_lexical WHERE verse_span_id=? AND ve_nr=115 AND COALESCE(delete_flagged,0)=0 LIMIT 1",(sid,)).fetchone()
    if ex:
        cur.execute("UPDATE ve_lexical SET value=?, source_provenance='role-reassess-2026' WHERE id=?",(r,ex['id'])); upd+=1
    else:
        cur.execute("""INSERT INTO ve_lexical (verse_span_id, gate, ve_nr, ve_label, value, pair_kind, source_provenance, delete_flagged, created_at)
          VALUES (?, NULL, 115, 'role', ?, 'value', 'role-reassess-2026', 0, ?)""",(sid, r, NOW)); ins+=1
c.commit()
print(f"  LIVE: role set on {len(plan)} spans (updated {upd}, inserted {ins}).")
